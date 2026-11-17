"""Ayudante de los cuadernos de Técnico-Profesional Instalaciones Sanitarias, 3.º y 4.º medio (student_content_tp_insa_*)."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para intervenir instalaciones.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas tuberías, artefactos, herramientas, instrumentos, computador ni internet: los planos y esquemas "
             "(descritos con listas de artefactos, tramos y cotas), las leyendas, las planillas, las listas de materiales, los presupuestos y los precios están escritos en el enunciado, "
             "son inventados y están rotulados «de ejemplo». Los diámetros, las pendientes, los caudales y los consumos son solo números de ejemplo para un cálculo en papel: los valores reales "
             "dependen del proyecto y de «la norma vigente» de la entidad fiscalizadora de tu sector. Este cuaderno no contiene instrucciones para cortar, unir ni instalar tuberías o artefactos, "
             "conectar redes de agua, alcantarillado o gas, excavar, entrar a cámaras o pozos, probar presiones ni desinfectar. " + AVISO)

EMER = ("Ante un accidente, una intoxicación, una caída, un atrapamiento, un olor a gas o una sospecha de fuga: no entres al lugar, avisa a un adulto responsable y a emergencias.")

build = make_build(MATERIALS)
