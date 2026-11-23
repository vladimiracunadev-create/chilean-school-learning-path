"""Ayudante de los cuadernos de Lenguaje y Comunicación, EPJA Educación Básica Nivel 1 (student_content_epja_leco_*).

Uso: `from epja_leco_common import build`. La forma de los ejercicios es la de hc_common:
  (q, a, why)                                  respuesta breve
  ("ab", stem, correcta, incorrecta, why)      dos opciones (el registro las balancea)
  ("abc", stem, correcta, mala1, mala2, why)   tres opciones
«{F}» dentro del enunciado se reemplaza por la ficha o el texto de la clase.
"""
from __future__ import annotations

import hc_common
from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los textos, fichas y datos están escritos en cada ejercicio y son inventados para este cuaderno: "
    "no necesitas video, audio, fotografías ni internet. Cuando la clase habla de un video, un audio o una foto, usa el guion o la descripción "
    "escritos aquí; si quieres, que otra persona los lea en voz alta. Si algo te cuesta leer, pide apoyo a quien te acompañe: "
    "pedir ayuda es parte de aprender. No escribas datos personales reales (cédula, dirección ni teléfono)."
)



def _why4(why):
    # El brief pide >= 3 palabras; la validación exige 3; el contenido procura explicar con más palabras.
    assert len(why.split()) >= 3, f"justificación demasiado breve ({why!r}): escribe por qué es correcta"
    return why


hc_common._why = _why4
build = make_build(MATERIALS)
