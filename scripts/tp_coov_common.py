"""Ayudante de los cuadernos de Técnico-Profesional Construcción (mención Obras Viales e Infraestructura), 4.º medio (student_content_tp_coov_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para intervenir obras.")

EMER = ("Ante un accidente, una caída, un derrumbe, un atrapamiento o una electrocución: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas herramientas, maquinaria, materiales de construcción, instrumentos, computador ni internet: los planos "
             "(descritos por escrito con leyenda, cotas y escala), las especificaciones, las planillas de cubicación, los presupuestos, las programaciones, los registros y los documentos de obra "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo». Las cantidades, resistencias, dosificaciones, espesores, pendientes, distancias, cargas y precios son de ejemplo "
             "y sirven solo para calcular en una planilla; los valores reales los fijan «la norma vigente» y el proyecto. Este cuaderno no contiene procedimientos de excavación, moldaje, armadura, hormigonado, "
             "montaje, trabajo en altura, uso de maquinaria o herramientas, demolición, pavimentación, instalaciones ni aplicación de productos. "
             + AVISO + " " + EMER)

build = make_build(MATERIALS)
