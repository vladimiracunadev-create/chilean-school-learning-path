"""Utilidades de los cuadernos de Matemática de 3.º y 4.º medio Formación General (student_content_fg_mate_*).

No registra clases. Las funciones comprueban numéricamente la respuesta antes de registrar el ejercicio.
"""
from __future__ import annotations

import math
from fractions import Fraction as F

from student_lessons import arith, ex, register  # noqa: F401

MATERIALS = "Cuaderno, lápiz, regla y, si quieres, una calculadora. Todos los datos que necesitas están escritos en cada ejercicio."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


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


def chk(cond: bool, msg: str = "") -> None:
    assert cond, msg


def num(x, nd: int = 2) -> str:
    """Número con coma decimal; sin ceros sobrantes; miles con punto."""
    if isinstance(x, F):
        x = float(x)
    r = round(x, nd)
    if abs(r - round(r)) < 1e-12:
        r = int(round(r))
        s = f"{abs(r):,}".replace(",", ".") if abs(r) >= 1000 else str(abs(r))
        return ("−" if r < 0 else "") + s
    s = f"{abs(r):,.{nd}f}".rstrip("0").rstrip(".")
    s = s.replace(",", "§").replace(".", ",").replace("§", ".")
    return ("−" if r < 0 else "") + s


def fr(x) -> str:
    """Fracción irreductible a/b (o entero)."""
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


# ---------------------------------------------------------------- números complejos
class C:
    """Número complejo con partes racionales."""

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(s, o):
        o = o if isinstance(o, C) else C(o)
        return C(s.a + o.a, s.b + o.b)

    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, C) else C(o)
        return C(s.a - o.a, s.b - o.b)

    def __rsub__(s, o):
        return C(o) - s

    def __mul__(s, o):
        o = o if isinstance(o, C) else C(o)
        return C(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)

    __rmul__ = __mul__

    def conj(s):
        return C(s.a, -s.b)

    def __truediv__(s, o):
        o = o if isinstance(o, C) else C(o)
        n = o.a * o.a + o.b * o.b
        t = s * o.conj()
        return C(t.a / n, t.b / n)

    def mod2(s):
        return s.a * s.a + s.b * s.b

    def __str__(s):
        return cs(s.a, s.b)


def cs(a, b) -> str:
    """Escribe a + bi con signos correctos y fracciones."""
    a, b = F(a), F(b)
    if b == 0:
        return fr(a).replace("-", "−")
    if abs(b) == 1:
        bt = "i"
    elif abs(b).denominator == 1:
        bt = fr(abs(b)) + "i"
    else:
        bt = "(" + fr(abs(b)) + ")i"
    if a == 0:
        return ("−" if b < 0 else "") + bt
    return fr(a).replace("-", "−") + (" − " if b < 0 else " + ") + bt


def cx(q: str, expr: str, why: str):
    """Ejercicio cuya respuesta compleja se calcula desde `expr` (Python con la clase C)."""
    v = eval(expr, {"__builtins__": {}}, {"C": C, "F": F})
    return ex(q, str(v), why)


# ---------------------------------------------------------------- estadística y probabilidad
def mean(xs):
    return F(sum(F(x) for x in xs), len(xs))


def var_pop(xs):
    m = mean(xs)
    return sum((F(x) - m) ** 2 for x in xs) / len(xs)


def binom(n: int, k: int, p: F) -> F:
    p = F(p)
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)
