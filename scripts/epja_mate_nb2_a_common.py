"""Ayudas del módulo 1 de Matemática EPJA Básica N2 (fracciones y decimales): formato y aritmética exacta con Fraction."""
from __future__ import annotations

from decimal import Decimal
from fractions import Fraction

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Todo se resuelve en papel y pantalla, con lo escrito en la ficha; las cifras de dinero y los datos son inventados. "
             "No se usa calculadora real: donde se nombra, se lee una pantalla de ejemplo escrita en el enunciado.")
build = make_build(MATERIALS)
PRIOR = ["Ya reparto, mido y calculo en mi vida diaria: partes de una cosa, litros, metros, dinero.", "Sé sumar, restar, multiplicar y dividir con números naturales."]


def f(s):
    """Fraction desde '3/4', '1.25' o entero; para escribir datos."""
    return Fraction(str(s))


def S(x):
    """Fracción como texto 3/4 (o entero)."""
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def M(x):
    """Número mixto como texto: 1 1/2; fracción propia o entero si corresponde."""
    x = Fraction(x)
    w, r = divmod(x.numerator, x.denominator)
    if r == 0:
        return str(w)
    return f"{w} {r}/{x.denominator}" if w else f"{r}/{x.denominator}"


def D(x):
    """Decimal exacto con coma chilena (el número debe tener expansión finita)."""
    x = Fraction(x)
    den = x.denominator
    while den % 2 == 0:
        den //= 2
    while den % 5 == 0:
        den //= 5
    assert den == 1, f"{x} no es decimal exacto"
    s = format(Decimal(x.numerator) / Decimal(x.denominator), "f")
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    ent, _, dec = s.partition(".")
    if len(ent) > 3:
        ent = f"{int(ent):,}".replace(",", ".")
    return ent + ("," + dec if dec else "")


def Q(stem, ok, b1, b2, why):
    assert len({ok, b1, b2}) == 3, (stem, ok, b1, b2)
    return ("abc", stem, ok, b1, b2, why)


def T2(stem, good, bad, why):
    assert good != bad
    return ("ab", stem, good, bad, why)


def C(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_):
    build(oa, n, F, use=use, prior=PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=op, reinforce=rf, extend=ex_)
