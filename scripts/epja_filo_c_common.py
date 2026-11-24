"""Ayudante común de Filosofía EPJA Media N1 y N2, módulo 3 (OAD-09 a OAD-12): problema filosófico ético-moral. Textos y casos originales, con personas ficticias; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma. Todos los textos, casos y diálogos son originales y de ejemplo (personas y situaciones ficticias); no se usa internet ni libro. Todo se resuelve con lo escrito en la ficha."
build = make_build(MATERIALS)

PRIOR = ["Alguna vez he conversado con otras personas sobre qué es justo o qué es correcto hacer.",
         "Sé distinguir entre contar lo que pasó y dar mi opinión sobre lo que pasó."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    stmt, example, crit, ev, err, fb = op
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=(stmt, example, crit, ev, err, fb), reinforce=rf, extend=ex_)
