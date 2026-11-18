"""Ayudante de los cuadernos de Técnico-Profesional Explotación Minera (3.º y 4.º medio; student_content_tp_exmi_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la autoridad minera de tu sector y elementos de protección; "
         "este cuaderno no te habilita para trabajar en una faena minera ni para intervenir labores, equipos, explosivos o instalaciones. Las tareas de riesgo las hace solo personal formado y autorizado por la empresa.")

EMER = ("Ante un accidente, un derrumbe, una caída de rocas, un incendio, una fuga, un atrapamiento, una descarga eléctrica o un equipo que se mueve de forma inesperada: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas faena, rocas, equipos, herramientas, instrumentos, computador ni internet: los planos, mapas, planillas, diagramas, registros e informes "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo». Las medidas, escalas, leyes, caudales, tonelajes, tiempos, distancias y precios son números de ejemplo "
             "para calcular en una planilla; los valores reales los fijan el proyecto, la empresa y «la norma vigente» de la autoridad minera. Este cuaderno no contiene procedimientos para perforar, tronar, manejar explosivos, fortificar, trabajar bajo tierra o en altura, "
             "entrar a espacios confinados, operar maquinaria ni rescatar personas. " + AVISO + " " + EMER)

build = make_build(MATERIALS)
