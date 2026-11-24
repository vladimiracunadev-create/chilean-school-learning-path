"""Ayudas del módulo 3 de Matemática EPJA Media N1 (sistemas de ecuaciones lineales 2x2, homotecia y teorema de Thales): materiales, conocimientos previos y constructor de clases."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel cuadriculado o una hoja con cuadrados dibujados a mano, lápiz, goma y, si se tiene, una regla. Todos los datos, tablas y medidas están escritos en la ficha de la clase; "
             "los montos de dinero y las medidas son de ejemplo. No se necesita calculadora: las cuentas se hacen a mano con números amigables.")
build = make_build(MATERIALS)

PRIOR = ["Ya sé resolver una ecuación simple como x + 5 = 12 y hacer una regla de tres con números de uso diario.",
         "Sé leer una tabla de valores y reconozco figuras como rectángulos y triángulos en planos, escaleras y techos."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo, criterios, evidencia, errores, retroalimentación)."""
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=op, reinforce=rf, extend=ex_)
