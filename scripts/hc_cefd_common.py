"""Ayudante del electivo «Ciencias del ejercicio físico y deportivo» (3.º y 4.º medio HC), módulos student_content_hc_cefd_*.

Solo fija los materiales y reglas de seguridad; la forma de los ejercicios es la de hc_common.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y papel. Todos los datos (frecuencias cardíacas, tiempos, minutos, planes, registros y resultados) son inventados «de ejemplo» y están escritos en cada ejercicio; no necesitas video, internet ni equipos. "
             "Si tu docente organiza práctica, hazla en un espacio despejado, con ropa y calzado cómodos, agua a mano, calentamiento antes y enfriamiento después, sin cargas máximas ni retener la respiración. "
             "Ante dolor, mareo, falta de aire inusual o lesión, detente y avisa de inmediato a una persona adulta o a un profesional de la salud. "
             "Este cuaderno analiza casos ficticios y planifica en general: no entrega dietas, suplementos, dosis ni diagnósticos, ni indica ejercicios personales (eso lo define un profesional). "
             "Nadie compara ni comenta los cuerpos de otras personas.")

build = make_build(MATERIALS)
