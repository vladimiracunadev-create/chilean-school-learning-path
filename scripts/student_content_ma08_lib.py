"""Utilidades compartidas por los cuadernos de 8.º básico Matemática (ma08_*). No registra clases."""
from __future__ import annotations

import re
from fractions import Fraction as F

from student_lessons import ex, register

MATERIALS = "Cuaderno, lápiz, regla y, si quieres, una calculadora. Todos los datos que necesitas están escritos en cada ejercicio."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _int(n: int) -> str:
    text = f"{abs(n):,}".replace(",", ".") if abs(n) >= 1000 else str(abs(n))
    return ("−" if n < 0 else "") + text


def show(value, form: str = "frac") -> str:
    """Formatea un valor exacto: entero, fracción irreductible a/b o decimal con coma."""
    if isinstance(value, (int, float)):
        value = F(value).limit_denominator(10**6)
    if value.denominator == 1:
        return _int(int(value))
    neg = value < 0
    value = abs(value)
    if form == "dec":
        den = value.denominator
        for p in (2, 5):
            while den % p == 0:
                den //= p
        assert den == 1, f"decimal no exacto: {value}"
        text = f"{float(value):.6f}".rstrip("0").rstrip(".").replace(".", ",")
    else:
        text = f"{value.numerator}/{value.denominator}"
    return ("−" if neg else "") + text


def cx(q, expr, why, unit="", form="frac"):
    """Ejercicio cerrado cuya respuesta se calcula exactamente desde `expr` (Python con F(n, d))."""
    value = eval(expr, {"__builtins__": {}}, {"F": F, "sol": sol})
    return ex(q, show(value, form) + unit, why)


def sol(a, b, c, d):
    """Solución de a·x + b = c·x + d (a ≠ c), como fracción exacta."""
    return F(F(d) - F(b)) / (F(a) - F(c))


def _py(text: str) -> str:
    """Convierte una expresión algebraica escrita con ² ³ y producto implícito en una expresión de Python en x e y."""
    t = text.replace("²", "**2").replace("³", "**3").replace("−", "-").replace("·", "*").replace("×", "*")
    t = re.sub(r"(\d)\s*([xy(])", r"\1*\2", t)
    t = re.sub(r"([xy)])\s*\(", r"\1*(", t)
    t = re.sub(r"\)\s*([xy])", r")*\1", t)
    t = re.sub(r"([xy])\s*([xy])", r"\1*\2", t)
    t = re.sub(r"(\d)/(\d)", r"F(\1,\2)", t)
    return t


def pe(q, answer, why, lhs, points=((2, 1), (3, -2), (-4, 5), (7, 3))):
    """Ejercicio algebraico: comprueba numéricamente que `answer` equivale a `lhs` (Python en x, y) antes de registrarlo."""
    for xv, yv in points:
        env = {"x": F(xv), "y": F(yv), "F": F}
        left = eval(lhs, {"__builtins__": {}}, env)
        right = eval(_py(answer), {"__builtins__": {}}, env)
        assert left == right, f"{q[:50]}: {lhs} != {answer} en x={xv}, y={yv}"
    return ex(q, answer, why)


def L(oa, n, use, prior, explain, vocab, worked, mist, R, C, A, Z, D, ctx, chk, op, reinforce, extend, mat=MATERIALS):
    """Registra una clase con forma compacta (misma estructura que register)."""
    register(
        oa, n,
        materials=mat, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mist],
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=chk, open_task=task(*op), reinforce=reinforce, extend=extend,
    )
