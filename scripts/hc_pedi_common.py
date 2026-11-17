"""Apoyo del cuaderno de «Probabilidades y estadística descriptiva e inferencial» (electivo HC, 3.º y 4.º medio).

`build` fija los materiales de la asignatura; `R(expr, nd)` calcula una respuesta decimal (con coma y signo «−») para
los ejercicios cuyo resultado no es entero, de modo que la clave no pueda discrepar del cálculo.
"""
from __future__ import annotations

import math

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel cuadriculado; calculadora simple opcional (no se necesita software). Todos los datos están escritos en la ficha de la clase y son de ejemplo. "
             "Las herramientas digitales (hoja de cálculo, calculadora estadística) se describen por escrito y se razonan a mano; si tu docente te deja usarlas, comprueba con ellas lo que hiciste en papel. "
             "Las tablas de valores (z, t, chi cuadrado) vienen dentro de la ficha.")
build = make_build(MATERIALS)


def R(expr: str, nd: int = 2, unit: str = "") -> str:
    """Resultado de `expr` redondeado a `nd` decimales, con coma decimal y signo menos «−»."""
    value = eval(expr, {"__builtins__": {}}, {"sqrt": math.sqrt})  # noqa: S307 - expresiones escritas por el autor
    text = f"{value:.{nd}f}" if nd else str(int(round(value)))
    return text.replace(".", ",").replace("-", "−") + unit
