"""Ayudante de los cuadernos de Lengua y Literatura, EPJA Educación Media Nivel 1, módulo 2 (student_content_epja_leli_nm1_b*).

Uso: `from epja_leli_nm1_b_common import build`. Forma de los ejercicios (la de hc_common):
  (q, a, why)                                  respuesta breve
  ("ab", stem, correcta, incorrecta, why)      dos opciones (el registro las balancea)
  ("abc", stem, correcta, mala1, mala2, why)   tres opciones
  ("=", q, expr, why[, unidad])                respuesta calculada
«{F}» dentro del enunciado se reemplaza por los textos de la clase.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los textos, fichas y datos están escritos en cada ejercicio y son inventados para este cuaderno: "
    "los nombres, lugares, precios y fechas son de ejemplo y no corresponden a personas, comercios ni instituciones reales. "
    "No necesitas libros, audio, video ni internet. Cuando la clase habla de escuchar un anuncio, usa el guion escrito aquí y, si quieres, "
    "pide a otra persona que lo lea en voz alta. Si algo te cuesta leer, pide apoyo: pedir ayuda es parte de aprender. "
    "No escribas datos personales reales (cédula, dirección ni teléfono)."
)

build = make_build(MATERIALS)
