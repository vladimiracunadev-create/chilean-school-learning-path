"""Ayudante de los cuadernos de Técnico-Profesional Montaje Industrial, 3.º y 4.º medio (student_content_tp_moin_*)."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para intervenir equipos o estructuras.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas estructuras, piezas, equipos, herramientas, instrumentos, computador ni internet: los planos y esquemas "
             "(descritos por escrito con listas de piezas, ejes, cotas y leyendas), las planillas, las listas de materiales, los programas de obra, los documentos y los precios están escritos en el enunciado, "
             "son inventados y están rotulados «de ejemplo». Los pesos, las cargas, las capacidades, las tolerancias, los rendimientos y las distancias son solo números de ejemplo para un cálculo en papel: "
             "los valores reales dependen del proyecto, del fabricante y de «la norma vigente» de la entidad fiscalizadora de tu sector. Este cuaderno no contiene instrucciones para izar, amarrar, soldar, cortar, "
             "atornillar, torquear, alinear, pintar, trabajar en altura, entrar a espacios cerrados, bloquear equipos ni operar herramientas o maquinaria. " + AVISO)

EMER = ("Ante un accidente, una caída, un aplastamiento o un atrapamiento: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

build = make_build(MATERIALS)
