"""Ayudante de los cuadernos de Interpretación y creación en danza, 3.º y 4.º medio HC (student_content_hc_icda_*).

Forma compacta de ejercicio (ver hc_common): (q, a, why) · ("ab", stem, ok, mal, why) · ("abc", stem, ok, mal1, mal2, why) · ("=", q, expr, why[, unidad]).
«{F}» dentro del enunciado se reemplaza por la ficha de la clase.
"""
from __future__ import annotations

import re

from hc_common import make_build

MATERIALS = ("Lápiz y papel (mejor si es cuadriculado, para hacer mapas de piso y tablas de conteo). Todas las secuencias, fichas, obras y casos están escritos en cada ejercicio: "
             "son originales e inventados para este cuaderno, así que no necesitas video, música real ni internet. "
             "Si tu docente organiza práctica en sala, usa un espacio despejado, ropa cómoda y calzado seguro, sin saltos acrobáticos, cargas, caídas ni contacto físico riesgoso; "
             "cada persona trabaja en su zona y a su propio rango. Haz siempre un calentamiento suave antes y un enfriamiento después. "
             "No se compara ni se evalúa el cuerpo de nadie: se observan decisiones de movimiento, no cuerpos. Nadie está obligado a mostrar su trabajo frente a otras personas. "
             "Si algo duele, marea o incomoda, detente y avisa a una persona adulta. Para filmar o difundir una práctica se necesita el consentimiento de quienes aparecen.")

_build = make_build(MATERIALS)

_MATCHING = re.compile(r"\b(?:une|unir|relaciona|clasifica|empareja|asocia|ordena|completa la tabla|escribe las letras)\b", re.I)


def _item(item, ficha):
    if item[0] in ("ab", "abc"):
        text = " ".join(str(x) for x in item[1:-1]).replace("{F}", ficha)
        found = _MATCHING.search(text)
        assert not found, f"palabra que desactiva el balanceo de alternativas ({found.group(0)!r}): {text[:90]}"
    return item


def build(oa, n, F, use, prior, explain, vocab, worked, mistakes, T, ctx, sc, op, reinforce, extend):
    _build(oa, n, F, use, prior, explain, vocab, worked, mistakes,
           [_item(x, F) for x in T], _item(ctx, F), [x for x in sc], op, reinforce, extend)
