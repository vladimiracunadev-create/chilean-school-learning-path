"""Ayudante de los cuadernos de «Expresión corporal» 3.º y 4.º medio HC (student_content_hc_exco_*).

Forma compacta de ejercicio (ver hc_common): (q, a, why) · ("ab", stem, ok, mal, why) · ("abc", stem, ok, mal1, mal2, why) · ("=", q, expr, why[, unidad]).
«{F}» dentro del enunciado se reemplaza por la ficha de la clase.
Comprueba además que la alternativa correcta no sea la más larga y que no se use vocabulario que desactiva el balanceo de alternativas.
"""
from __future__ import annotations

import re

from hc_common import make_build

MATERIALS = ("Lápiz y papel. Todas las secuencias, fichas, registros y casos están escritos en cada ejercicio: son originales e inventados para este cuaderno, "
             "así que no necesitas video, música real ni internet. "
             "Si tu docente organiza práctica en sala, usa un espacio despejado, ropa cómoda y calzado seguro, sin saltos acrobáticos, cargas, caídas ni contacto físico riesgoso; "
             "cada persona trabaja en su propia zona y a su propio rango, y puede apoyarse en una silla o en la pared. Haz siempre un calentamiento suave antes y un enfriamiento después. "
             "No se compara ni se evalúa el cuerpo de nadie ni se promueve una imagen corporal: se observan decisiones de movimiento, no cuerpos. Nadie está obligado a mostrar su trabajo. "
             "Si algo duele, marea o incomoda, detente y avisa a una persona adulta. Para filmar o difundir una práctica se necesita el consentimiento de quienes aparecen.")

_build = make_build(MATERIALS)

_MATCHING = re.compile(r"\b(?:une|unir|relaciona|clasifica|empareja|asocia|ordena|completa la tabla|escribe las letras)\b", re.I)


def _item(item, ficha):
    if item[0] in ("ab", "abc"):
        text = " ".join(str(x) for x in item[1:-1]).replace("{F}", ficha)
        found = _MATCHING.search(text)
        assert not found, f"palabra que desactiva el balanceo de alternativas ({found.group(0)!r}): {text[:90]}"
        good, *bad = item[2:-1]
        if len(good) > max(len(b) for b in bad):
            import sys
            print(f"LARGA ({len(good)} vs {max(len(b) for b in bad)}): {item[1][:70]} || {good}", file=sys.stderr)
    return item


def build(oa, n, F, use, prior, explain, vocab, worked, mistakes, T, ctx, sc, op, reinforce, extend):
    _build(oa, n, F, use, prior, explain, vocab, worked, mistakes,
           [_item(x, F) for x in T], _item(ctx, F), list(sc), op, reinforce, extend)
