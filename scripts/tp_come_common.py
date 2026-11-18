"""Ayudante de los cuadernos de Técnico-Profesional Construcciones Metálicas, 3.º y 4.º medio (student_content_tp_come_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora de tu sector y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para operar máquinas, herramientas o equipos.")

EMER = ("Ante un accidente, un corte, una quemadura, un atrapamiento, una descarga eléctrica, un derrame o un incendio: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas piezas, perfiles, planchas, máquinas, herramientas, instrumentos, equipos, pinturas, computador ni internet: los planos "
             "(descritos por escrito con listas de piezas y cotas), las planillas, las pautas, los registros y los documentos de la obra o del taller están escritos en el enunciado, son inventados y están rotulados «de ejemplo». "
             "Las medidas, masas por metro, rendimientos, espesores, tolerancias, consumos, tiempos y precios son números de ejemplo para calcular en una planilla; los valores reales los fijan el proyecto, el fabricante "
             "y «la norma vigente». Este cuaderno no contiene procedimientos para trazar, cortar, soldar, esmerilar, taladrar, doblar, forjar, armar, montar, izar, trabajar en altura, preparar superficies, pintar, "
             "manipular residuos peligrosos ni operar herramientas, máquinas o equipos. " + AVISO + " " + EMER)

build = make_build(MATERIALS)
