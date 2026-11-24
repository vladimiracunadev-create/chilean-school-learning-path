"""Ayudante común de Artes Visuales EPJA Media N1 y N2, módulo 1 (OAD-01 a OAD-04): materiales y forma de `K`.

Todo en papel: las obras son DESCRITAS, inventadas y rotuladas «obra de ejemplo»; la producción real es una actividad abierta con materiales cotidianos y seguros.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Para la actividad práctica opcional: hojas, recortes de revistas o cajas, tijeras de punta redonda, pegamento escolar y témpera. "
             "Las obras, los letreros y las cifras de las fichas son de ejemplo, inventados para el cuaderno; todo el análisis se resuelve con lo escrito en la ficha.")
build = make_build(MATERIALS)

PRIOR = ["Ya miro letreros, afiches y murales cuando camino por mi barrio o mi ciudad.",
         "Alguna vez he dibujado, recortado, pegado o pintado algo, aunque sea una nota o un cartel."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    stmt, example, crit, ev, err, fb = op
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=(stmt, example, crit, ev, err, fb), reinforce=rf, extend=ex_)
