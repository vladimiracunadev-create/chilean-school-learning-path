"""Ayudante de los cuadernos de Ciencias Naturales EPJA Media N1, módulo 2 (student_content_epja_cnat_nm1_b*).

Uso: `from epja_cnat_nm1_b_common import K`. Forma de los ejercicios (la de hc_common):
  (q, a, why) · ("ab", stem, correcta, incorrecta, why) · ("abc", stem, correcta, mala1, mala2, why) · ("=", q, expr, why[, unidad])
«{F}» dentro del enunciado se reemplaza por la ficha de la clase. Todo dato de ejemplo está escrito en la ficha: no se hace ningún experimento real.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. No se hace ningún experimento real ni se mezcla ningún producto de limpieza: todo se resuelve leyendo los datos, tablas, fórmulas y textos "
    "de ejemplo escritos en cada ficha, que son inventados o simplificados para este cuaderno. No hace falta calculadora científica, internet ni materiales. "
    "La seguridad en el hogar se trabaja solo leyendo etiquetas de ejemplo."
)
build = make_build(MATERIALS)

PRIOR = [
    "Ya observo cambios en mi vida diaria: la comida que se cocina, el hierro que se oxida, la masa que sube.",
    "Leo cifras con unidades, como gramos, litros o grados, en etiquetas y recetas.",
]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo de respuesta, criterios, evidencia, retroalimentación); los errores son los frecuentes de la clase."""
    stmt, example, crit, ev, fb = op
    worked = [(t, p.replace("{F} ", ""), st, a) for t, p, st, a in worked]
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=(stmt, example, crit, ev, [m[0] for m in mistakes], fb), reinforce=rf, extend=ex_)
