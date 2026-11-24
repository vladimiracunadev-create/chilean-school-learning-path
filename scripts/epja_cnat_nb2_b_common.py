"""Ayudante de los cuadernos de Ciencias Naturales EPJA Básica N2, módulo 2 (student_content_epja_cnat_nb2_b*).

Uso: `from epja_cnat_nb2_b_common import K`. Forma de los ejercicios (la de hc_common):
  (q, a, why) · ("ab", stem, correcta, incorrecta, why) · ("abc", stem, correcta, mala1, mala2, why) · ("=", q, expr, why[, unidad])
«{F}» dentro del enunciado se reemplaza por la ficha de la clase. Todo dato de ejemplo está escrito en la ficha: no se hacen experimentos reales.
"""
from __future__ import annotations

from hc_common import make_build


MATERIALS = (
    "Lápiz, goma y cuaderno. No se hace ningún experimento real: todo se resuelve leyendo los datos, tablas y textos de ejemplo escritos en cada ficha, "
    "que son inventados para este cuaderno. No hace falta calculadora, internet ni materiales. Si quieres comprobar algo con objetos de tu casa, "
    "usa solo agua del grifo y cosas seguras, sin calor, sin electricidad de red y sin mezclar productos de limpieza."
)
build = make_build(MATERIALS)

PRIOR = [
    "Ya observo cómo se comportan el agua, el hielo y los alimentos en mi vida diaria.",
    "Leo cifras con unidades, como gramos, litros o grados, en etiquetas y recetas.",
]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo de respuesta, criterios, errores, retroalimentación, evidencia)."""
    stmt, example, crit, err, fb, ev = op
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=(stmt, example, crit, ev, err, fb), reinforce=rf, extend=ex_)
