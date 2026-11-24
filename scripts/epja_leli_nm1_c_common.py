"""Ayudante de los cuadernos de Lengua y Literatura, EPJA Educación Media Nivel 1, módulo 3 (student_content_epja_leli_nm1_c*).

Uso: `from epja_leli_nm1_c_common import build`. La forma de los ejercicios es la de hc_common:
  (q, a, why)                                  respuesta breve
  ("ab", stem, correcta, incorrecta, why)      dos opciones (el registro las balancea)
  ("abc", stem, correcta, mala1, mala2, why)   tres opciones
  ("=", q, expr, why[, unidad])                respuesta calculada
«{F}» dentro del enunciado se reemplaza por los textos de la clase.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todas las personas, fuentes, fichas y textos de este cuaderno son inventados y están escritos en cada ejercicio: "
    "no necesitas libros, internet, audio ni video. Cuando la clase habla de una persona o de un sitio web, trabajas con la descripción escrita aquí. "
    "Si algo te cuesta leer o escribir, pide apoyo: pedir ayuda es parte de aprender. No escribas datos personales reales (cédula, dirección ni teléfono)."
)

build = make_build(MATERIALS)
