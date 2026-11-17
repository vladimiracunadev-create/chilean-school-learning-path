"""Ayudante de los cuadernos de Técnico-Profesional Telecomunicaciones (student_content_tp_tele_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas computador, internet ni equipos: los esquemas, "
             "las señales, los enlaces, las tablas, las empresas y los datos están escritos en el enunciado, son inventados y están rotulados «de ejemplo», "
             "y todo se resuelve en papel. Los valores de potencia, frecuencia, distancia y costo son solo para practicar; los valores reales dependen del "
             "fabricante, del proyecto y de «la norma vigente» (por ejemplo, la de la Subsecretaría de Telecomunicaciones, Subtel). Nunca escribas contraseñas "
             "reales ni datos personales de nadie. Esto es aprendizaje conceptual en papel. Practicar tareas con electricidad, antenas, torres, trabajo en altura "
             "o instalación de equipos exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar.")

AVISO = ("Esto es aprendizaje conceptual en papel: practicar esta tarea exige instructor autorizado, norma vigente (por ejemplo, la de la entidad fiscalizadora de tu sector) "
         "y elementos de protección; este cuaderno no te habilita para trabajar.")

build = make_build(MATERIALS)
