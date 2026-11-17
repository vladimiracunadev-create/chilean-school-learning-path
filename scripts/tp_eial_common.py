"""Ayudante de los cuadernos de Técnico-Profesional Elaboración Industrial de Alimentos, 3.º y 4.º medio (student_content_tp_eial_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel (o cuaderno); una calculadora simple es opcional. Todas las plantas, proveedores, productos, lotes, cantidades, precios, horarios, temperaturas, plazos y límites "
             "son inventados y están rotulados «de ejemplo»: no hay marcas ni empresas reales y no necesitas planta, alimentos, software ni equipos. "
             "Los valores de ejemplo no reemplazan los límites que fija la norma vigente (autoridad sanitaria). Aquí no hay formulaciones ni procedimientos de elaboración, esterilización, conservación, fermentación, envasado ni operación de máquinas: solo conceptos, registros, cálculos y reglas generales. "
             "Aditivos, conservantes y alérgenos se estudian solo como concepto y rotulado; ante una intoxicación, una reacción alérgica o un accidente, se avisa de inmediato a un adulto responsable y a emergencias. "
             "Esto es aprendizaje conceptual en papel. El trabajo con maquinaria industrial, calderas, congelación y cámaras de frío, atmósferas peligrosas y productos químicos de limpieza requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria, SEC, etc.); este cuaderno no te habilita para trabajar.")

build = make_build(MATERIALS)
