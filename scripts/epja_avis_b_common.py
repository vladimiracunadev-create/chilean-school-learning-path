"""Ayudante propio de Artes Visuales EPJA Media N1 y N2, módulo 2 (OAD-05 a OAD-08): materiales, conocimientos previos y la función K.

Todas las obras son inventadas y descritas con palabras (rotuladas «obra de ejemplo»); no se usan imágenes, láminas ni obras reales.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma; opcional lápices de colores, restos de cartón y papel de diario. Todas las obras, fichas y casos son de ejemplo, inventados y descritos con palabras: "
             "no hace falta internet, láminas ni imágenes. Todo se resuelve con lo escrito en la ficha; la parte de producción usa solo materiales cotidianos y seguros.")
build = make_build(MATERIALS)

PRIOR = ["He mirado carteles, murales, fotografías o artesanías en mi barrio, en el trabajo o en un trámite.",
         "Alguna vez he elegido un color, una forma o un dibujo para decorar, rotular o avisar algo."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    stmt, example, crit, ev, err, fb = op
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=(stmt, example, crit, ev, err, fb), reinforce=rf, extend=ex_)
