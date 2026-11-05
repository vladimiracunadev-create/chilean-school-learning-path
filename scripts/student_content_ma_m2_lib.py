"""Utilidades de los cuadernos de 2.º medio Matemática (ma_m2_*). No registra clases.

Las funciones `rx`, `qz`, `near` comprueban numéricamente la respuesta antes de registrar el ejercicio,
para que una respuesta escrita a mano no pueda contradecir al enunciado.
"""
from __future__ import annotations

import math
import re
from fractions import Fraction as F

from student_content_ma08_lib import L, cx, show, task  # noqa: F401
from student_lessons import arith, ex  # noqa: F401


def sr(n: int) -> str:
    """Raíz cuadrada simplificada de n como texto: 72 -> «6√2», 49 -> «7», 13 -> «√13»."""
    a, b, k = 1, n, 2
    while k * k <= b:
        while b % (k * k) == 0:
            b //= k * k
            a *= k
        k += 1
    if b == 1:
        return str(a)
    return (str(a) if a > 1 else "") + "√" + str(b)


_SUP = {"³": 3, "⁴": 4, "⁵": 5}


def _rt(a: float, n: int) -> float:
    return -((-a) ** (1 / n)) if a < 0 else a ** (1 / n)


def val(s: str) -> float:
    """Valor numérico de una expresión escrita con √, raíces enésimas (³√), ², ³, ^ y fracciones."""
    s = re.sub(r"(?<=\d)\.(?=\d{3}(?!\d))", "", s)
    t = s.replace("−", "-").replace("·", "*").replace("×", "*").replace("÷", "/").replace(",", ".")
    t = t.replace("π", "math.pi")
    for sup, n in _SUP.items():
        t = re.sub(sup + r"√\(([^()]*)\)", lambda m, n=n: f"rt({m.group(1)},{n})", t)
        t = re.sub(sup + r"√(\d+)", lambda m, n=n: f"rt({m.group(1)},{n})", t)
    t = re.sub(r"√\(([^()]*)\)", r"math.sqrt(\1)", t)
    t = re.sub(r"√(\d+)", r"math.sqrt(\1)", t)
    t = t.replace("²", "**2").replace("^", "**")
    t = re.sub(r"(\d|\))\s*(math\.|rt\(|\()", r"\1*\2", t)
    t = re.sub(r"\)\s*(\d)", r")*\1", t)
    return float(eval(t, {"__builtins__": {}}, {"math": math, "rt": _rt}))


def near(a: float, b: float, tol: float = 1e-9) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def rx(q: str, expr: str, ans: str, why: str):
    """Ejercicio cuya respuesta `ans` se comprueba numéricamente contra la expresión `expr`."""
    assert near(val(expr), val(ans)), f"{q[:60]}: {expr} = {val(expr)} pero {ans} = {val(ans)}"
    return ex(q, ans, why)


def qz(q: str, a, b, c, roots, ans: str, why: str):
    """Ecuación a·x² + b·x + c = 0: comprueba que cada raíz de `roots` (fracciones) la cumple."""
    for r in roots:
        r = F(r)
        assert a * r * r + b * r + c == 0, f"{q[:60]}: {r} no es solución"
    return ex(q, ans, why)


def chk(cond: bool, msg: str = "") -> None:
    assert cond, msg
