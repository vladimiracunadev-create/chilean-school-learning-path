"""Student-facing lesson layer: explanation, worked examples, exercises and solutions.

The planning modules describe how a teacher can run a class. This module holds what a
student needs in order to learn: the explanation, resolved examples, graded exercises
with every datum written out, and a reasoned answer key. Content is registered per
(OA, lesson number) by `student_*.py` modules and rendered into Markdown and HTML.
A registered lesson is the single source of truth for its concrete resource,
exact prompt and reference answer; no keyword-matched fallback may override it.
"""
from __future__ import annotations

import ast
import html
import operator
import re

REGISTRY: dict[tuple[str, int], dict] = {}

TIERS = (
    ("recovery", "Recuperación", "R"),
    ("understand", "Comprensión", "C"),
    ("apply", "Aplicación", "A"),
    ("reason", "Razonamiento y análisis", "Z"),
    ("challenge", "Desafío", "D"),
)
MIN_CLOSED = 12
MIN_TIERS = 5
MIN_WORKED = 2
MIN_SELFCHECK = 3
MIN_EXPLAIN_WORDS = 90
PLACEHOLDER = re.compile(r"\b(preparar|prepara|preparen|inventa|inventen|elige|elegir|busca|buscar)\s+(tres|dos|cuatro|algunos|varios|unos|los)\s+(casos|ejemplos|datos|problemas)\b", re.I)


def ex(q: str, a: str, why: str, calc: str | None = None) -> dict:
    """One closed exercise. `calc` is an arithmetic expression the validator re-evaluates."""
    return {"q": q, "a": a, "why": why, "calc": calc}


def arith(q: str, expr: str, why: str, unit: str = "") -> dict:
    """Closed exercise whose answer is computed from `expr`, so it cannot disagree."""
    value = evaluate(expr)
    shown = expr.replace("//", " ÷ ").replace("*", " × ").replace("-", " − ").replace("+", " + ")
    shown = " ".join(shown.split())
    return ex(q, f"{fmt(value)}{unit}", f"{why} Cálculo: {shown} = {fmt(value)}.", calc=expr)


def fmt(value: int | float) -> str:
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    if isinstance(value, int):
        return f"{value:,}".replace(",", ".") if abs(value) >= 1000 else str(value)
    return str(value).replace(".", ",")


_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.FloorDiv: operator.floordiv, ast.Div: operator.truediv}


def evaluate(expr: str):
    """Evaluate integer arithmetic only; anything else raises ValueError."""
    def walk(node):
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](walk(node.left), walk(node.right))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -walk(node.operand)
        raise ValueError(f"expresión no permitida: {expr}")
    return walk(ast.parse(expr, mode="eval"))


_MARK = re.compile(r"(?:(?<=\s)|^)(\(?)([AaBbCc])(\)|\.)(?=\s)")
_ANSWER = re.compile(r"^(\(?)([AaBb])(\)?[\).]?)(\s.*)?$")
_LETTER_IN_WHY = re.compile(r"(?:opci[oó]n|alternativa|letra)\s+\(?[AaBb]\b|\(?\b[AaBb]\)")


def _swap_options(item: dict) -> None:
    """Place the correct option of an A/B question at a position fixed by a hash of its content.

    Authors tend to put the right option first. Deciding the position from a hash of the statement
    and of the two options (not from where the author put it) keeps about half of the answers on
    each side, and the answer key is rewritten to match.
    """
    import zlib
    q, answer = item["q"], str(item["a"])
    marks = list(_MARK.finditer(q))
    letters = [m.group(2) for m in marks]
    if len(marks) != 2 or letters[0].upper() != "A" or letters[1].upper() != "B" or letters[0].islower() != letters[1].islower():
        return
    am = _ANSWER.match(answer.strip())
    if not am or _LETTER_IN_WHY.search(item.get("why", "")):
        return
    first, second = marks
    a_raw = q[first.end():second.start()]
    sep = re.search(r"(?:\s+[oO]|\s*[,;])\s*$", a_raw)
    a_text = (a_raw[:sep.start()] if sep else a_raw).strip()
    separator = sep.group(0).rstrip() if sep else ""
    b_raw = q[second.end():].strip()
    tail = re.search(r"[?.!]*$", b_raw).group(0)
    b_text = b_raw[:len(b_raw) - len(tail)].strip()
    if not a_text or not b_text or chr(10) in q:
        return
    stem = q[:first.start()]
    correct_is_a = am.group(2).upper() == "A"
    key = stem + "|" + "|".join(sorted((a_text, b_text)))
    want_a = zlib.crc32(key.encode("utf-8")) % 2 == 0
    if want_a == correct_is_a:
        return
    lo = letters[0].islower()
    la, lb = ("a", "b") if lo else ("A", "B")
    ma, mb = first.group(1), second.group(1)
    ca, cb = first.group(3), second.group(3)
    item["q"] = f"{stem}{ma}{la}{ca} {b_text}{separator} {mb}{lb}{cb} {a_text}{tail}"
    flipped = ("b" if am.group(2) == "a" else "B") if am.group(2) in "aA" else ("a" if am.group(2) == "b" else "A")
    item["a"] = f"{am.group(1)}{flipped}{am.group(3)}{am.group(4) or ''}"


def balance_options(content: dict) -> None:
    for group in list(content.get("tiers", {}).values()) + [content.get("context", []), content.get("selfcheck", [])]:
        for item in group:
            if isinstance(item, dict) and "q" in item and "a" in item:
                _swap_options(item)


def register(oa_code: str, number: int, **content) -> None:
    key = (oa_code, number)
    if key in REGISTRY:
        raise ValueError(f"contenido de estudiante duplicado: {key}")
    balance_options(content)
    REGISTRY[key] = content


def student_for(oa_code: str, number: int) -> dict | None:
    return REGISTRY.get((oa_code, number))


def load_all() -> None:
    """Import every student content module so the registry is populated."""
    import importlib
    import pkgutil
    import sys
    from pathlib import Path
    here = Path(__file__).resolve().parent
    if str(here) not in sys.path:
        sys.path.insert(0, str(here))
    for module in sorted(info.name for info in pkgutil.iter_modules([str(here)]) if info.name.startswith("student_content_")):
        importlib.import_module(module)


def closed_exercises(content: dict) -> list[dict]:
    items = []
    for key, _label, _prefix in TIERS:
        items.extend(content.get("tiers", {}).get(key, []))
    items.extend(content.get("context", []))
    return items


def all_questions(content: dict) -> list[dict]:
    return closed_exercises(content) + content.get("selfcheck", [])


def problems(oa_code: str, number: int, content: dict) -> list[str]:
    """Structural and arithmetic defects of one student lesson (empty list = passes)."""
    where = f"{oa_code} clase {number}"
    found = []
    words = len(" ".join(content.get("explain", [])).split())
    if words < MIN_EXPLAIN_WORDS:
        found.append(f"{where}: explicación de {words} palabras (mínimo {MIN_EXPLAIN_WORDS})")
    for field in ("use", "prior", "vocab", "mistakes", "reinforce", "extend"):
        if not content.get(field):
            found.append(f"{where}: falta «{field}»")
    worked = content.get("worked", [])
    if len(worked) < MIN_WORKED:
        found.append(f"{where}: {len(worked)} ejemplos resueltos (mínimo {MIN_WORKED})")
    for example in worked:
        if len(example.get("steps", [])) < 2 or not example.get("answer"):
            found.append(f"{where}: ejemplo resuelto sin pasos o sin respuesta")
    tiers = content.get("tiers", {})
    present = [key for key, _l, _p in TIERS if tiers.get(key)]
    if len(present) < MIN_TIERS:
        found.append(f"{where}: sólo {len(present)} niveles de ejercicio de {MIN_TIERS}")
    closed = closed_exercises(content)
    if len(closed) < MIN_CLOSED:
        found.append(f"{where}: {len(closed)} ejercicios cerrados (mínimo {MIN_CLOSED})")
    if not content.get("context"):
        found.append(f"{where}: sin problema contextualizado")
    if len(content.get("selfcheck", [])) < MIN_SELFCHECK:
        found.append(f"{where}: autoevaluación con menos de {MIN_SELFCHECK} preguntas")
    questions = [item["q"].strip().lower() for item in all_questions(content)]
    if len(set(questions)) != len(questions):
        found.append(f"{where}: ejercicios con enunciado repetido")
    for item in all_questions(content):
        if not item["a"].strip() or len(item["why"].split()) < 3:
            found.append(f"{where}: ejercicio sin respuesta o sin explicación: {item['q'][:50]}")
        if item.get("calc"):
            try:
                value = evaluate(item["calc"])
            except (ValueError, SyntaxError, ZeroDivisionError):
                found.append(f"{where}: cálculo no verificable «{item['calc']}»")
                continue
            if fmt(value) not in item["a"] and str(value) not in item["a"]:
                found.append(f"{where}: «{item['calc']}» da {fmt(value)} pero la respuesta dice «{item['a']}»")
    open_task = content.get("open_task")
    if not open_task:
        found.append(f"{where}: falta actividad abierta")
    else:
        for field in ("statement", "example", "criteria", "evidence", "errors", "feedback"):
            if not open_task.get(field):
                found.append(f"{where}: actividad abierta sin «{field}»")
    text = _plain(content)
    if PLACEHOLDER.search(text):
        found.append(f"{where}: instrucción que delega inventar o preparar los casos")
    return found


def _plain(content: dict) -> str:
    parts: list[str] = []
    def collect(value):
        if isinstance(value, str):
            parts.append(value)
        elif isinstance(value, dict):
            for item in value.values():
                collect(item)
        elif isinstance(value, (list, tuple)):
            for item in value:
                collect(item)
    collect({k: v for k, v in content.items() if k != "open_task"})
    collect(content.get("open_task", {}).get("statement", ""))
    return " ".join(parts)


def derived_artefact(content: dict) -> dict:
    """Concrete resource, prompt and reference derived from the student content."""
    open_task = content["open_task"]
    return {
        "resource": content["materials"],
        "prompt": open_task["statement"],
        "reference": open_task["example"],
    }


def _numbered(content: dict):
    for key, label, prefix in TIERS:
        rows = content.get("tiers", {}).get(key, [])
        yield label, [(f"{prefix}{index}", item) for index, item in enumerate(rows, 1)]
    if content.get("context"):
        yield "Situaciones auténticas", [(f"S{index}", item) for index, item in enumerate(content["context"], 1)]
    yield "Autoevaluación", [(f"E{index}", item) for index, item in enumerate(content.get("selfcheck", []), 1)]


def render_markdown(content: dict) -> str:
    out = ["### Cuaderno del estudiante", ""]
    out += [f"**Lo que aprenderé y para qué sirve.** {content['use']}", ""]
    out += ["**Lo que ya debo saber.** " + " ".join(content["prior"]), ""]
    out += ["**Explicación.**", ""] + [f"{paragraph}\n" for paragraph in content["explain"]]
    out += ["**Palabras importantes**", "", "| Palabra | Qué significa |", "|---|---|"]
    out += [f"| {term} | {meaning} |" for term, meaning in content["vocab"]] + [""]
    out += ["**Ejemplos resueltos paso a paso**", ""]
    for number, example in enumerate(content["worked"], 1):
        out += [f"*Ejemplo {number}. {example['title']}*", "", f"Problema: {example['problem']}", ""]
        out += [f"{step_no}. {step}" for step_no, step in enumerate(example["steps"], 1)]
        out += ["", f"Respuesta: {example['answer']}", ""]
    out += ["**Errores frecuentes y cómo reconocerlos**", ""]
    out += [f"- **Error:** {m['wrong']} **Por qué ocurre:** {m['why']} **Cómo corregirlo:** {m['fix']}" for m in content["mistakes"]] + [""]
    out += ["**Ejercicios**", ""]
    for label, rows in _numbered(content):
        if not rows:
            continue
        out += [f"*{label}*", ""] + [f"- **{code}.** {item['q']}" for code, item in rows] + [""]
    out += ["**Actividad abierta.** " + content["open_task"]["statement"], ""]
    out += ["**Solucionario razonado**", ""]
    for _label, rows in _numbered(content):
        out += [f"- **{code}.** {item['a']}. {item['why']}" for code, item in rows]
    open_task = content["open_task"]
    out += ["", "**Actividad abierta · ejemplo de respuesta.** " + open_task["example"], ""]
    out += ["**Criterios para evaluarla:** " + "; ".join(open_task["criteria"]) + ".", ""]
    out += ["**Evidencias aceptables:** " + "; ".join(open_task["evidence"]) + ".", ""]
    out += ["**Errores que conviene detectar:** " + "; ".join(open_task["errors"]) + ".", ""]
    out += ["**Retroalimentación constructiva:** " + open_task["feedback"], ""]
    out += [f"**Refuerzo.** {content['reinforce']}", "", f"**Profundización.** {content['extend']}", ""]
    return "\n".join(out)


def render_html(content: dict) -> str:
    def esc(value) -> str:
        return html.escape(str(value), quote=True)
    parts = ['<section class="student-notebook"><p class="eyebrow">Para el estudiante</p><h3>Cuaderno del estudiante</h3>']
    parts.append(f'<p><strong>Lo que aprenderé y para qué sirve.</strong> {esc(content["use"])}</p>')
    parts.append(f'<p><strong>Lo que ya debo saber.</strong> {esc(" ".join(content["prior"]))}</p>')
    parts.append("<h4>Explicación</h4>" + "".join(f"<p>{esc(p)}</p>" for p in content["explain"]))
    parts.append('<h4>Palabras importantes</h4><div class="table-scroll"><table><thead><tr><th>Palabra</th><th>Qué significa</th></tr></thead><tbody>'
                 + "".join(f"<tr><td><strong>{esc(t)}</strong></td><td>{esc(m)}</td></tr>" for t, m in content["vocab"]) + "</tbody></table></div>")
    parts.append("<h4>Ejemplos resueltos paso a paso</h4>")
    for number, example in enumerate(content["worked"], 1):
        parts.append(f'<div class="worked-example"><h5>Ejemplo {number}. {esc(example["title"])}</h5><p><strong>Problema:</strong> {esc(example["problem"])}</p><ol>'
                     + "".join(f"<li>{esc(s)}</li>" for s in example["steps"]) + f'</ol><p><strong>Respuesta:</strong> {esc(example["answer"])}</p></div>')
    parts.append("<h4>Errores frecuentes y cómo reconocerlos</h4><ul>"
                 + "".join(f"<li><strong>Error:</strong> {esc(m['wrong'])} <strong>Por qué ocurre:</strong> {esc(m['why'])} <strong>Cómo corregirlo:</strong> {esc(m['fix'])}</li>" for m in content["mistakes"]) + "</ul>")
    parts.append("<h4>Ejercicios</h4>")
    for label, rows in _numbered(content):
        if not rows:
            continue
        parts.append(f"<h5>{esc(label)}</h5><ol class=\"exercise-list\">"
                     + "".join(f'<li value="{index}"><span class="exercise-code">{esc(code)}</span> {esc(item["q"])}</li>' for index, (code, item) in enumerate(rows, 1)) + "</ol>")
    parts.append(f'<p><strong>Actividad abierta.</strong> {esc(content["open_task"]["statement"])}</p>')
    answers = []
    for _label, rows in _numbered(content):
        answers += [f"<li><strong>{esc(code)}.</strong> {esc(item['a'])}. {esc(item['why'])}</li>" for code, item in rows]
    open_task = content["open_task"]
    parts.append('<details class="answer-key"><summary>Solucionario razonado y pauta de la actividad abierta</summary><ul>' + "".join(answers) + "</ul>"
                 f'<p><strong>Ejemplo de respuesta:</strong> {esc(open_task["example"])}</p>'
                 f'<p><strong>Criterios:</strong> {esc("; ".join(open_task["criteria"]))}.</p>'
                 f'<p><strong>Evidencias aceptables:</strong> {esc("; ".join(open_task["evidence"]))}.</p>'
                 f'<p><strong>Errores que conviene detectar:</strong> {esc("; ".join(open_task["errors"]))}.</p>'
                 f'<p><strong>Retroalimentación constructiva:</strong> {esc(open_task["feedback"])}</p></details>')
    parts.append(f'<p><strong>Refuerzo.</strong> {esc(content["reinforce"])}</p><p><strong>Profundización.</strong> {esc(content["extend"])}</p></section>')
    return "".join(parts)
