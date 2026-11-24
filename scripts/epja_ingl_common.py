"""Ayudante de los cuadernos de Inglés, EPJA Educación Básica Nivel 2 (student_content_epja_ingl_*).

Uso: `from epja_ingl_common import build, GUION`. La forma de los ejercicios es la de hc_common:
  (q, a, why)                                  respuesta breve
  ("ab", stem, correcta, incorrecta, why)      dos opciones (el registro las balancea)
  ("abc", stem, correcta, mala1, mala2, why)   tres opciones
  ("=", q, expr, why[, unidad])                respuesta calculada
«{F}» dentro del enunciado se reemplaza por los textos de la clase.
Inglés estadounidense. Todo lo que se «escucha» va escrito (guion) y lo lee otra persona en voz alta o se lee en silencio.
"""
from __future__ import annotations

from hc_common import make_build

GUION = "Otra persona lee en voz alta (o lee tú en voz baja el guion): "

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los textos, diálogos y guiones están escritos en cada ejercicio y son inventados para este cuaderno: "
    "no necesitas audio, video ni internet. Cuando la clase habla de escuchar, usa el guion escrito aquí: pide a otra persona que lo lea en voz alta "
    "o léelo tú mismo, despacio. Si algo te cuesta, pide apoyo: pedir ayuda es parte de aprender. "
    "No escribas datos personales reales (cédula, dirección ni teléfono): usa datos de ejemplo."
)

build = make_build(MATERIALS)
