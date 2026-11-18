"""Ayudante de los cuadernos de Técnico-Profesional Mecánica Automotriz (3.º y 4.º medio; student_content_tp_meau_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora de tu sector y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para intervenir vehículos, herramientas o equipos.")

EMER = ("Ante un accidente, un atrapamiento, un corte, una quemadura, una descarga eléctrica, un derrame o un incendio: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas vehículos, piezas, herramientas, instrumentos, equipos, computador ni internet: los manuales, los diagramas, las órdenes de trabajo, las pautas de mantenimiento, las planillas de control, los registros y los demás documentos del taller "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo». Las medidas, tolerancias, presiones, tensiones, tiempos, kilometrajes, consumos, volúmenes, límites de emisiones y precios son números de ejemplo "
             "para calcular en una planilla; los valores reales los fijan el fabricante y «la norma vigente». Este cuaderno no contiene procedimientos para desarmar, reparar, diagnosticar ni probar vehículos reales, para trabajar bajo un vehículo elevado, "
             "para manejar combustibles, baterías, gases de escape, refrigerantes, sistemas de frenos o airbags, ni para conducir. " + AVISO + " " + EMER)

build = make_build(MATERIALS)
