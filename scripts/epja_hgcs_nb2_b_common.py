"""Ayudante común del módulo 2 de HGCS EPJA Básica N2 (OAD-05 a OAD-08): fija materiales y la función K."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Mapas, tablas, fotografías y textos son de ejemplo y están descritos en palabras en cada ficha; no se necesita internet, "
             "ni mapas reales, ni salir de casa. Los datos de localidades son inventados y se rotulan así.")
build = make_build(MATERIALS)

PRIOR = ["Conozco lugares por haberlos recorrido, vivido o escuchado de otras personas.", "Leo textos breves y tablas sencillas con apoyo.", "Sé que Chile es largo y que su clima y su paisaje cambian de norte a sur."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo, criterios, evidencia, errores, retroalimentación)."""
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=op, reinforce=rf, extend=ex_)
