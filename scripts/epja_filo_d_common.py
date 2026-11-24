"""Ayudante común de Filosofía EPJA Media N1 y N2, módulo 4 (OAD-13 a OAD-16): el problema filosófico del conocimiento humano.

Los textos y casos son inventados para el ejercicio; las ideas de autores reales se resumen con palabras propias, sin citas.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Todos los textos, casos y fichas son inventados para el ejercicio (de ejemplo); las ideas de autores reales se resumen con palabras propias. "
             "No hace falta internet ni libros. Todo se resuelve con lo escrito en la ficha. Las posiciones personales se escriben solo en la actividad abierta.")
build = make_build(MATERIALS)

O13 = "EPJA-FILO-NM1y2-OAD-13"
O14 = "EPJA-FILO-NM1y2-OAD-14"
O15 = "EPJA-FILO-NM1y2-OAD-15"
O16 = "EPJA-FILO-NM1y2-OAD-16"
PRIOR = ["Alguna vez he dudado de algo que me contaron o de algo que yo mismo creía.", "En el trabajo o en la casa he tenido que decidir sin estar del todo seguro."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    stmt, example, crit, ev, err, fb = op
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=(stmt, example, crit, ev, err, fb), reinforce=rf, extend=ex_)
