"""Ayudante de los cuadernos de Técnico-Profesional Forestal, 3.º y 4.º medio (student_content_tp_fore_*)."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para operar herramientas o maquinaria.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas árboles, plantas, herramientas, máquinas, productos, instrumentos, computador ni internet: los planos, mapas, "
             "planillas, registros, fichas y documentos están descritos por escrito en el enunciado, son inventados y están rotulados «de ejemplo». Las superficies, densidades, volúmenes, rendimientos, "
             "dosis, costos, precios y distancias son solo números de ejemplo para un cálculo en papel: los valores reales dependen del predio, del plan de manejo, del fabricante y de «la norma vigente» "
             "de la entidad fiscalizadora de tu sector. Las especies se nombran como «especie A» y «especie B». Este cuaderno no contiene instrucciones para usar motosierras ni herramientas de corte, "
             "voltear o trozar árboles, operar maquinaria, hacer quemas ni usar fuego, combatir incendios, aplicar productos sanitarios o agroquímicos, ni trabajar en terrenos con pendiente, con tormentas o en altura. " + AVISO)

EMER = ("Ante un accidente, la caída de un árbol, un incendio, un corte grave o una intoxicación: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

build = make_build(MATERIALS)
