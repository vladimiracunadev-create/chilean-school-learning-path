"""Ayudantes del módulo 4 de Matemática EPJA Media N1 (probabilidad: regla de Laplace, reglas multiplicativa y aditiva, árboles). Todo en papel; datos inventados, sin dinero en juego."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma. Todos los datos están escritos en la ficha y son de ejemplo (inventados). No se usa calculadora: las cuentas son amables y se hacen en papel. Nadie apuesta dinero: las urnas, los dados y las monedas son solo modelos para aprender."
build = make_build(MATERIALS)

PRIOR = ["Ya sé operar con fracciones sencillas y con porcentajes, por ejemplo 1/2 es 50 %.", "He leído tablas y listas de datos en boletas, cuentas y avisos, y sé que no todo lo que pasa se puede asegurar de antemano."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo, criterios, evidencia, errores, retroalimentación)."""
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=op, reinforce=rf, extend=ex_)
