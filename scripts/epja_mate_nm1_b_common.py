"""Ayudas del módulo 2 de Matemática EPJA Media N1 (función cuadrática y productos notables): formato y ejercicios."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Todo se resuelve en papel, con las tablas de valores y los datos escritos en la ficha; las cifras y las situaciones son inventadas. "
             "No se necesita calculadora ni programa de gráficos: las curvas se describen con palabras y con tablas de valores.")
build = make_build(MATERIALS)
PRIOR = ["Ya calculo áreas, precios y totales en mi vida diaria (pisos, pinturas, compras, arriendos).",
         "Sé operar con números enteros, usar una letra para un valor desconocido y calcular potencias de exponente 2."]


def Q(stem, ok, b1, b2, why):
    assert len({ok, b1, b2}) == 3, (stem, ok, b1, b2)
    return ("abc", stem, ok, b1, b2, why)


def T2(stem, good, bad, why):
    assert good != bad
    return ("ab", stem, good, bad, why)


def C(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_):
    build(oa, n, F, use=use, prior=PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=op, reinforce=rf, extend=ex_)
