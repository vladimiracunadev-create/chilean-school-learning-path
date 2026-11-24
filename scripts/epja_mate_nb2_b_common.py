"""Ayudas del módulo 2 de Matemática EPJA Básica N2 (patrones y sucesiones): materiales, conocimientos previos y constructor de clases."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Todas las tablas, listas y situaciones están escritas en la ficha; los montos de dinero son de ejemplo, no se usa dinero real "
             "ni calculadora. Las cuentas se hacen con números amigables, a mano o de memoria.")
build = make_build(MATERIALS)

PRIOR = ["Ya sé sumar, restar y multiplicar con números de uso diario.",
         "Reconozco que muchas cosas de la vida se repiten con orden: turnos, horarios, filas y calendarios."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo, criterios, evidencia, errores, retroalimentación)."""
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=op, reinforce=rf, extend=ex_)


def t(a, d, k):
    """Término de posición k (desde 1) de la sucesión que parte en a y suma d."""
    return a + d * (k - 1)


def S(a, d, n, sep=", "):
    """Primeros n términos como texto."""
    return sep.join(str(t(a, d, k)) for k in range(1, n + 1))
