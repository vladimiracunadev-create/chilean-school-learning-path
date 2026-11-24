"""Ayudas de Matemática EPJA Media N1: formato de ejercicios y registro de clases. Datos inventados; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Todo se resuelve en papel y pantalla, con lo escrito en la ficha; los datos, medidas y cifras son inventados "
             "o aproximaciones redondeadas. No se usa calculadora científica real: donde se nombra, se lee una pantalla de ejemplo escrita en el enunciado. "
             "Los gráficos se reemplazan por tablas de valores y descripciones.")
build = make_build(MATERIALS)
PRIOR = ["Ya calculo áreas, medidas, porcentajes y vueltos en mi trabajo y en mi casa.",
         "Sé operar con números enteros, fracciones y decimales, y conozco los cuadrados y las potencias más simples."]


def Q(stem, ok, b1, b2, why):
    assert len({ok, b1, b2}) == 3, (stem, ok, b1, b2)
    return ("abc", stem, ok, b1, b2, why)


def T2(stem, good, bad, why):
    assert good != bad
    return ("ab", stem, good, bad, why)


def C(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_):
    build(oa, n, F, use=use, prior=PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=op, reinforce=rf, extend=ex_)
