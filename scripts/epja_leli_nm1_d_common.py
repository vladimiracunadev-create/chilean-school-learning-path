"""Ayudante de los cuadernos de Lengua y Literatura, EPJA Educación Media Nivel 1, módulo 4 (student_content_epja_leli_nm1_d*).

Uso: `from epja_leli_nm1_d_common import build`. La forma de los ejercicios es la de hc_common:
  (q, a, why)                                  respuesta breve
  ("ab", stem, correcta, incorrecta, why)      dos opciones (el registro las balancea)
  ("abc", stem, correcta, mala1, mala2, why)   tres opciones
  ("=", q, expr, why[, unidad])                respuesta calculada
«{F}» dentro del enunciado se reemplaza por los textos de la clase.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los textos, resúmenes de obras, fichas y tablas están escritos en cada ejercicio: "
    "los textos nuevos son inventados para este cuaderno y los resúmenes de obras clásicas están escritos con palabras propias. "
    "No necesitas libros, audio, video ni internet: cuando la clase habla de imágenes o sonidos, están descritos en una tabla escrita. "
    "Si algo te cuesta leer, pide apoyo a otra persona: pedir ayuda es parte de aprender. "
    "No escribas datos personales reales (cédula, dirección ni teléfono)."
)

build = make_build(MATERIALS)
