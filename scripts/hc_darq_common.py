"""Ayudante de los cuadernos de Diseño y arquitectura (student_content_hc_darq_*)."""
from __future__ import annotations

import re

from hc_common import make_build

MATERIALS = ("Lápiz, papel (mejor si es cuadriculado) y regla. Todas las fichas, planos descritos, proyectos y obras están escritos en cada ejercicio: son originales e inventados "
             "para este cuaderno, así que no necesitas imágenes, planos reales ni internet. Si tu docente organiza práctica en sala, usa solo materiales escolares seguros "
             "(cartón reciclado limpio, papel, cinta de papel, pegamento en barra, tijeras de punta roma) en un lugar ventilado, sin herramientas eléctricas, calor ni objetos cortantes. "
             "Los conceptos de estructura, normas y seguridad de este cuaderno son generales y de ejemplo: construir de verdad requiere una persona profesional habilitada y la normativa vigente. "
             "Avisa a una persona adulta si algo te incomoda o te pone en riesgo.")

_build = make_build(MATERIALS)


def _fix(text):
    """Evita palabras que el registro toma por consignas de «une/relaciona» y desactivan el balanceo de alternativas."""
    text = re.sub(r"\brelaciona\b", "vincula", text)
    return re.sub(r"\bRelaciona\b", "Vincula", text)


def _item(item):
    item = tuple(_fix(x) if isinstance(x, str) else x for x in item)
    if item[0] == "abc":
        item = item[:2] + tuple(x.replace("; ", ", ") for x in item[2:5]) + item[5:]
    return item


def build(oa, n, F, use, prior, explain, vocab, worked, mistakes, T, ctx, sc, op, reinforce, extend):
    _build(oa, n, _fix(F), use, prior, explain, vocab, worked, mistakes,
           [_item(x) for x in T], _item(ctx), [(_fix(a), b, c) for a, b, c in sc], op, reinforce, extend)
