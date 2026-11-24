"""Ayudante de Artes Visuales EPJA Media N1 y N2, módulo 4 (OAD-13 a OAD-16): difusión de trabajos y proyectos. Todo en papel; fichas, cronogramas y presupuestos inventados."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma. Todas las obras, fichas, cronogramas, presupuestos y pautas son de ejemplo (personas, grupos y lugares ficticios); no se compra nada ni se exige cámara, internet ni calculadora. Todo se resuelve con lo escrito en la ficha."
build = make_build(MATERIALS)

O13 = "EPJA-AVIS-NM1y2-OAD-13"
O14 = "EPJA-AVIS-NM1y2-OAD-14"
O15 = "EPJA-AVIS-NM1y2-OAD-15"
O16 = "EPJA-AVIS-NM1y2-OAD-16"
PRIOR = ["He visto una exposición, una feria o una muestra en un centro cultural, una biblioteca o una sede vecinal, o he colgado algo en una pared.", "Sé decir si algo me gusta o no me gusta de una imagen y por qué."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=tuple(op), reinforce=rf, extend=ex_)
