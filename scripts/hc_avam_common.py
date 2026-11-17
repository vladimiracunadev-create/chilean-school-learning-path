"""Ayudante de los cuadernos de Artes visuales, audiovisuales y multimediales (student_content_hc_avam_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y papel. Todas las fichas, obras, guiones y casos están escritos en cada ejercicio: son originales e inventados para este cuaderno, "
             "así que no necesitas imágenes, audio, video ni internet. Si tu docente organiza práctica en sala, usa materiales escolares seguros "
             "(papel, cartulina, témpera lavable, pegamento en barra, tijeras de punta roma) en un lugar ventilado, sin solventes, calor ni objetos cortantes. "
             "No fotografíes ni grabes a otras personas sin su permiso, y avisa a una persona adulta si algo te incomoda o te pone en riesgo.")

build = make_build(MATERIALS)
