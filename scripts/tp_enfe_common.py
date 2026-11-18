"""Ayudante de los cuadernos de Técnico-Profesional Atención de Enfermería, mención Enfermería (student_content_tp_enfe_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales."""
from __future__ import annotations

from hc_common import make_build
from tp_aten_common import AVISO, EMER

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas pacientes, equipos, instrumentos, muestras, medicamentos, computador ni internet: las fichas, indicaciones, planillas, registros y casos "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo»; no hay datos de personas reales. Los valores de signos vitales, volúmenes, horarios, unidades y cantidades son números de ejemplo "
             "para leer o calcular una planilla, nunca para decidir sobre una persona. Los datos de los pacientes son confidenciales y su identificación correcta es una regla de seguridad. "
             "Este cuaderno no contiene técnicas clínicas ni procedimientos paso a paso (no enseña a tomar signos vitales, tomar muestras, administrar medicamentos, hacer curaciones, manejar sondas o catéteres, ni a operar equipos), ni dosis, ni diagnósticos. "
             + AVISO + " " + EMER)

LIM = " " + AVISO

build = make_build(MATERIALS)
