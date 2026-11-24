"""Ayudante de los cuadernos de Lenguaje y Comunicación, EPJA Educación Básica Nivel 2 (student_content_epja_leco_nb2_*).

Uso: `from epja_leco_nb2_common import build`. La forma de los ejercicios es la de hc_common:
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
    "no necesitas libros, audio, video ni internet. Cuando la clase habla de escuchar a alguien, usa el guion escrito aquí y, si quieres, "
    "pide a otra persona que lo lea en voz alta. Si algo te cuesta leer, pide apoyo: pedir ayuda es parte de aprender. "
    "No escribas datos personales reales (cédula, dirección ni teléfono)."
)

build = make_build(MATERIALS)
