"""Ayudas del módulo 3 de Matemática EPJA Básica N2 (movimientos de figuras 2D, ángulos, perímetro y área): materiales, conocimientos previos y constructor de clases."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel cuadriculado o una hoja con cuadrados dibujados a mano, lápiz y goma. Todas las figuras se describen con coordenadas o medidas escritas en la ficha; "
             "los montos de dinero son de ejemplo, no se usa dinero real ni calculadora. Las cuentas se hacen a mano con números amigables.")
build = make_build(MATERIALS)

PRIOR = ["Ya sé sumar, restar y multiplicar con números de uso diario.",
         "Reconozco figuras como rectángulos, cuadrados y triángulos en puertas, ventanas, pisos y planos."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo, criterios, evidencia, errores, retroalimentación)."""
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=op, reinforce=rf, extend=ex_)
