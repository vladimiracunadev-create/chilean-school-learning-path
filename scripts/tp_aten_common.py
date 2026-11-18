"""Ayudante de los cuadernos de Técnico-Profesional Atención de Enfermería, tronco de 3.º medio (student_content_tp_aten_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad y prevención."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel, con casos ficticios. Trabajar con personas exige la supervisión de un profesional de salud, un instructor autorizado y la norma vigente de la autoridad sanitaria; "
         "este cuaderno no te habilita para trabajar ni para atender pacientes.")

EMER = ("Ante una emergencia, una caída, una reacción adversa, un atragantamiento o un paro: no actúes por cuenta propia; avisa de inmediato a la enfermera o profesional responsable y a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas pacientes, instrumentos, insumos, medicamentos, computador ni internet: las fichas, planillas, registros y casos "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo». No hay datos de personas reales; las cifras (pesos, temperaturas, presiones, volúmenes, horarios, cantidades) son números de ejemplo "
             "para leer o calcular una planilla, nunca para decidir sobre una persona. Los datos de salud de las personas son confidenciales y el trato es siempre digno, con consentimiento y respeto de sus derechos. "
             "Este cuaderno no contiene técnicas clínicas ni procedimientos paso a paso (no enseña a tomar signos vitales, curar, inyectar, dar medicamentos, movilizar, hacer RCP ni instalar sondas), ni dosis, ni diagnósticos. "
             + AVISO + " " + EMER)

LIM = " " + AVISO

build = make_build(MATERIALS)
