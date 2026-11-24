"""Ayudante común de Filosofía EPJA Media N1 y N2, módulo 2 (OAD-05 a OAD-08): el problema filosófico del ser humano.

Los textos «de ejemplo» son paráfrasis breves y originales escritas para las fichas; no son citas de autores.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma. Los textos, casos y diálogos de las fichas son de ejemplo, con personajes ficticios; no se necesita internet, libro ni calculadora. Todo se resuelve con lo escrito en la ficha."
build = make_build(MATERIALS)

PRIOR = ["Alguna vez me he preguntado para qué hago lo que hago, en el trabajo o en la vida diaria.", "Sé que dos personas pueden pensar distinto y ambas dar buenas razones."]


def make_K():
    def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
        build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
              op=op, reinforce=rf, extend=ex_)
    return K
