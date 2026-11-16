"""Ayudante de los cuadernos de Mundo global, 3.º y 4.º medio FG (student_content_fg_mglo_*).

No registra clases por sí mismo. Forma compacta de ejercicio (la primera opción es la correcta; el registro las balancea):
  (q, a, why)                              respuesta breve
  (stem, correcta, mala, why)              dos opciones
  (stem, correcta, mala1, mala2, why)      tres opciones
  ("=", q, expr, why[, unidad])            respuesta calculada
«{F}» dentro del enunciado se reemplaza por la ficha de la clase. Todos los casos son de ejemplo, inventados.
"""
from __future__ import annotations

import os
import zlib

from student_lessons import _LETTER_IN_WHY, arith, ex, register

MATERIALS = "Lápiz y papel. Todos los casos, textos y datos están escritos en cada ejercicio (son casos de ejemplo, inventados para este cuaderno); no necesitas libros ni internet."
PRIOR = ["Sé leer una tabla, un mapa o un texto breve y sacar de él una idea principal.", "Sé distinguir un hecho de una opinión.", "Conozco lo básico de cómo se organiza un Estado y de qué es un territorio."]
_PROBLEMS: list[str] = []


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _why(why):
    if len(why.split()) < 5:
        _PROBLEMS.append(f"justificación breve: {why!r}")
    return why


def _check_opts(stem, good, bads):
    # La correcta puede ser la más larga, la más corta o intermedia: el reparto se revisa por clase, no por ítem.
    if any(len(b) < 0.45 * len(good) for b in bads):
        _PROBLEMS.append(f"distractor muy corto: {stem[:60]}")


def _e(item, ficha):
    if item[0] == "=":
        _, q, expr, why, *rest = item
        return arith(q.replace("{F}", ficha), expr, _why(why), rest[0] if rest else "")
    if len(item) == 3:
        q, a, why = item
        return ex(q.replace("{F}", ficha), a, _why(why))
    if len(item) in (4, 5):
        stem, good, *bads, why = item
        _check_opts(stem, good, bads)
        letters = "ABC"
        options = [good] + bads
        pos = 0
        if not _LETTER_IN_WHY.search(why):
            # La ficha puede traer sus propias «A) B) C)», lo que impide al registro reordenar: se coloca la correcta aquí, con un reparto fijo por hash.
            pos = zlib.crc32((stem + "|" + "|".join(sorted(options))).encode("utf-8")) % len(options)
        options = bads[:pos] + [good] + bads[pos:]
        opts = " ".join(f"{letters[i]}) {o}" for i, o in enumerate(options))
        return ex(f"{stem} {opts}".replace("{F}", ficha), f"{letters[pos]}) {good}", _why(why))
    raise AssertionError(f"ejercicio mal formado: {str(item[0])[:80]}")


def build(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rx, prior=None):
    """T: 13 ejercicios (3/3/3/2/2). worked: (título, problema, pasos, respuesta). mistakes: (error, causa, corrección)."""
    assert len(T) == 13, (oa, n, len(T))
    del _PROBLEMS[:]
    cuts = (0, 3, 6, 9, 11, 13)
    names = ("recovery", "understand", "apply", "reason", "challenge")
    tiers = {names[i]: [_e(x, F) for x in T[cuts[i]:cuts[i + 1]]] for i in range(5)}
    context = [_e(ctx, F)]
    selfcheck = [_e(x, F) for x in sc]
    words = len(" ".join(explain).split())
    if words < 95:
        _PROBLEMS.append(f"explicación de {words} palabras")
    if _PROBLEMS:
        if os.environ.get("MGLO_SOFT"):
            print(f"## {oa} clase {n}: " + " | ".join(_PROBLEMS))
        else:
            raise AssertionError(f"{oa} clase {n}: " + " | ".join(_PROBLEMS))
    register(
        oa, n,
        materials=MATERIALS, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=tiers, context=context, selfcheck=selfcheck,
        open_task=task(op[0].replace("{F}", F), *op[1:]),
        reinforce=rx[0], extend=rx[1],
    )
