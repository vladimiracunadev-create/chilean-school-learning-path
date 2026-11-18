"""Ayudante de los cuadernos de Técnico-Profesional Asistencia en Geología, 3.º y 4.º medio (student_content_tp_asge_*)."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la autoridad minera y elementos de protección; "
         "este cuaderno no te habilita para trabajar en terreno minero ni para operar equipos o maquinaria.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas rocas, minerales, herramientas, equipos, instrumentos, vehículos, computador, aplicaciones ni internet: los planos, "
             "mapas, planillas, registros, fichas y documentos están descritos por escrito en el enunciado, son inventados y están rotulados «de ejemplo». Las coordenadas, cotas, distancias, pesos, "
             "capacidades, metros, porcentajes y consumos son solo números de ejemplo para un cálculo en papel: los valores reales dependen del proyecto, del fabricante, del terreno y de «la norma vigente» "
             "de la autoridad minera. Los nombres de proyectos, empresas, sondajes y personas son ficticios. Este cuaderno no contiene instrucciones para ingresar a faenas o terrenos mineros, armar campamentos, "
             "instalar o armar equipos, perforar, abrir calicatas, tomar muestras en terreno, usar explosivos, trabajar en altura o en espacios confinados, ni operar vehículos, máquinas o instrumentos. " + AVISO)

EMER = ("Ante un accidente, un derrumbe, una caída de rocas, una falla de maquinaria, un incendio, una tormenta o una persona lesionada: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

build = make_build(MATERIALS)
