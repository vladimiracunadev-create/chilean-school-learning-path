"""Ayudante de los cuadernos de Técnico-Profesional Atención de Enfermería, mención Adulto Mayor (student_content_tp_adma_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales."""
from __future__ import annotations

from hc_common import make_build
from tp_aten_common import AVISO, EMER

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas personas mayores, instrumentos, alimentos, medicamentos, computador ni internet: las fichas, planillas, minutas, registros y casos "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo»; los nombres, residencias y familias no existen y no hay datos de personas reales. Los pesos, volúmenes, horarios y cantidades son números de ejemplo "
             "para leer o calcular una planilla, nunca para decidir sobre una persona. Las personas mayores tienen derecho a la dignidad, la privacidad, la autonomía y la confidencialidad de sus datos. "
             "Este cuaderno no contiene técnicas clínicas ni procedimientos paso a paso (no enseña a alimentar, movilizar, bañar, dar medicamentos, hacer primeros auxilios ni RCP), ni dosis, ni diagnósticos. "
             + AVISO + " " + EMER)

LIM = " " + AVISO

build = make_build(MATERIALS)
