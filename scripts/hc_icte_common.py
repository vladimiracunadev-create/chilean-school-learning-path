"""Ayudante de los cuadernos de Interpretación y creación en teatro, 3.º y 4.º medio HC (student_content_hc_icte_*).

Forma compacta de ejercicio (ver hc_common): (q, a, why) · ("ab", stem, ok, mal, why) · ("abc", stem, ok, mal1, mal2, why) · ("=", q, expr, why[, unidad]).
«{F}» dentro del enunciado se reemplaza por la ficha de la clase.
"""
from __future__ import annotations

import re

from hc_common import make_build

MATERIALS = ("Lápiz y papel (mejor si es cuadriculado, para hacer planos de escena y tablas de registro). Todas las escenas, diálogos, personajes, fichas de obras y casos están escritos en cada ejercicio: "
             "son originales e inventados para este cuaderno, así que no necesitas video, obras con derechos de autor ni internet. "
             "Si tu docente organiza práctica en sala, usa un espacio despejado, ropa cómoda y calzado seguro, sin contacto físico riesgoso, caídas, acrobacias, cargas ni objetos peligrosos; "
             "haz siempre un calentamiento corporal y vocal suave antes y un cierre tranquilo después, y cuida la voz (agua, pausas, sin forzar ni gritar). "
             "Nadie está obligado a mostrar su trabajo ni a exponer experiencias personales: se actúa con personajes y situaciones ficticias, y no se evalúan los cuerpos de las personas, sino las decisiones de la obra. "
             "Los temas sensibles se tratan con casos inventados y sobrios; si algo te incomoda, detén el ejercicio y avisa a una persona adulta de confianza. "
             "Para grabar, fotografiar o difundir un ensayo o una función se necesita el consentimiento de quienes aparecen, y todo texto o idea ajena se cita con su autoría.")

_build = make_build(MATERIALS)

_MATCHING = re.compile(r"\b(?:une|unir|relaciona|clasifica|empareja|asocia|ordena|completa la tabla|escribe las letras)\b", re.I)


def _item(item, ficha):
    if item[0] in ("ab", "abc"):
        text = " ".join(str(x) for x in item[1:-1]).replace("{F}", ficha)
        found = _MATCHING.search(text)
        assert not found, f"palabra que desactiva el balanceo de alternativas ({found.group(0)!r}): {text[:90]}"
        for opt in item[2:-1]:
            assert not re.search(r"[.?!]\s+[A-ZÁÉÍÓÚ¿¡]", str(opt)), f"alternativa con dos oraciones: {opt[:60]}"
    return item


def build(oa, n, F, use, prior, explain, vocab, worked, mistakes, T, ctx, sc, op, reinforce, extend):
    _build(oa, n, F, use, prior, explain, vocab, worked, mistakes,
           [_item(x, F) for x in T], _item(ctx, F), [_item(x, F) for x in sc], op, reinforce, extend)
