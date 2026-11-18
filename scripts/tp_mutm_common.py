"""Ayudante de los cuadernos de Técnico-Profesional Muebles y Terminaciones en Madera, 3.º y 4.º medio (student_content_tp_mutm_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para operar máquinas o herramientas.")

EMER = ("Ante un accidente, un corte, una amputación, una proyección de partículas, un incendio o una intoxicación por solventes: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas madera, tableros, máquinas, herramientas, adhesivos, barnices, solventes, instrumentos, computador ni internet: los planos y despieces "
             "(descritos por escrito con leyenda, cotas y escala), las listas de piezas y de corte, las planillas de cubicación, los presupuestos, las programaciones, los registros de calidad y los documentos del taller "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo». Las medidas, humedades, escuadrías, rendimientos, mermas, tolerancias, intervalos, pesos y precios son de ejemplo "
             "y sirven solo para calcular en una planilla; los valores reales los fijan «la norma vigente», el fabricante y el proyecto. Este cuaderno no contiene procedimientos de uso de sierras, cepillos, tupí, lijadoras, canteadoras "
             "u otras máquinas y herramientas de corte, afilado, armado, ensamble, encolado, prensado, aplicación de barnices, lacas, solventes o pinturas, ni secado de madera. "
             + AVISO + " " + EMER)

build = make_build(MATERIALS)
