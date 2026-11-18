"""Ayudante de los cuadernos de Técnico-Profesional Agropecuaria (mención Pecuaria), 4.º medio (student_content_tp_agpe_*)."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora de tu sector y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para operar maquinaria, manejar animales o aplicar productos.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas animales, corrales, instalaciones, balanzas, equipos de ordeña, medicamentos, forrajes, máquinas, instrumentos, computador ni internet: las fichas, los registros, las planillas, "
             "los informes y los documentos están descritos por escrito en el enunciado, son inventados y están rotulados «de ejemplo». Las superficies, los caudales, los pesos, las producciones, "
             "las dosis, los plazos, los costos, los precios y las temperaturas son solo números de ejemplo para un cálculo en papel: los valores reales dependen del predio, de la especie, del "
             "asesor técnico y de «la norma vigente» de la entidad fiscalizadora de tu sector. Los predios, las empresas y las personas de los casos son ficticios. Este cuaderno no contiene instrucciones para sujetar, conducir, transportar, inseminar, ordeñar, medicar o tratar animales, ni para operar equipos o maquinaria. " + AVISO)

EMER = ("Ante un accidente, un atrapamiento, una caída, un animal que se descontrola, una intoxicación, un incendio o un derrame: no te acerques a la zona de riesgo, "
        "avisa a un adulto responsable y a emergencias.")

build = make_build(MATERIALS)
