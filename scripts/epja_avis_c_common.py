"""Ayudante común de Artes Visuales EPJA Media N1 y N2, módulo 3 (OAD-09 a OAD-12): lenguaje audiovisual.
Todo se enseña en papel: guiones, escaletas, storyboards descritos y tablas de planos con obras y casos inventados. Sin video ni audio."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Todas las obras, guiones y casos de la ficha son inventados («de ejemplo»); no se usan películas ni artistas reales. "
             "Todo se resuelve con lo escrito en la ficha, sin ver video ni oír audio. Grabar con el celular es una actividad opcional y no se evalúa.")
build = make_build(MATERIALS)

PRIOR = ["He visto avisos, videos, películas o series en mi vida diaria.", "Sé contar algo que me pasó o que vi en mi barrio o en mi trabajo."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    stmt, example, crit, ev, err, fb = op
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=(stmt, example, crit, ev, err, fb), reinforce=rf, extend=ex_)
