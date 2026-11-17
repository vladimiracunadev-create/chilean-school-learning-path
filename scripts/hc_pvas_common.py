"""Ayudante del electivo «Promoción de estilos de vida activos y saludables» (3.º y 4.º medio HC), módulos student_content_hc_pvas_*.

Solo fija los materiales y reglas de seguridad; la forma de los ejercicios es la de hc_common.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y papel. Todos los datos (minutos, registros, encuestas, planes, rutas y resultados) y los casos son inventados «de ejemplo» y están escritos en cada ejercicio; no necesitas video, internet, aplicaciones ni equipos. "
             "Si tu docente organiza práctica, hazla en un espacio despejado, con ropa y calzado cómodos, agua a mano, calentamiento antes y vuelta a la calma después, sin cargas, sin saltos ni acrobacias y sin retener la respiración. "
             "Ante dolor, mareo, falta de aire inusual o lesión, detente y avisa de inmediato a una persona adulta. "
             "Este cuaderno analiza casos ficticios y enseña a planificar en general: no entrega dietas, suplementos, dosis ni diagnósticos, ni indica ejercicios para personas reales (eso lo define un profesional). "
             "Nadie compara, mide ni comenta los cuerpos de otras personas; cuando un tema te afecte (ánimo, consumo de sustancias, violencia), cuéntaselo a una persona adulta de confianza o a un profesional.")

build = make_build(MATERIALS)
