"""Ayudante de los cuadernos de Técnico-Profesional Mecánica Industrial (tronco de especialidad, 3.º medio) (student_content_tp_mein_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora de tu sector y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para operar máquinas, herramientas o equipos.")

EMER = ("Ante un accidente, un atrapamiento, un corte, una quemadura, una descarga eléctrica o un incendio: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas piezas, máquinas, herramientas, instrumentos, equipos, computador ni internet: los planos y listas de piezas (descritos por escrito), las planillas de control, las pautas de mantenimiento, las fichas de proceso, los registros y los documentos del taller "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo». Las medidas, tolerancias, tiempos, rendimientos, consumos, pesos, presiones, cargas y precios son números de ejemplo "
             "para calcular en una planilla; los valores reales los fijan el fabricante, el proyecto y «la norma vigente». Este cuaderno no contiene procedimientos para cortar, soldar, esmerilar, taladrar, sujetar, ajustar, lubricar, desarmar ni operar herramientas, máquinas o equipos, ni para usar gases, combustibles o equipos de izaje. " + AVISO + " " + EMER)

build = make_build(MATERIALS)
