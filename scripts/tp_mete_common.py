"""Ayudante de los cuadernos de Técnico-Profesional Metalurgia Extractiva, 3.º y 4.º medio (student_content_tp_mete_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora de tu sector y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para operar plantas, equipos o maquinaria.")

EMER = ("Ante un accidente, un incendio, un derrame, un atrapamiento, una fuga de gas o vapor, una quemadura o una persona lesionada: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas minerales, muestras, reactivos, instrumentos, equipos, herramientas, computador ni internet: las planillas, "
             "los balances, las fichas, los informes y los documentos de la planta están descritos por escrito en el enunciado, son inventados y están rotulados «de ejemplo». "
             "Los tonelajes, leyes, porcentajes, tamaños, consumos, costos y precios son números de ejemplo para calcular en papel; los valores reales los fijan el proyecto, el laboratorio, el fabricante "
             "y «la norma vigente». Los nombres de plantas, empresas, laboratorios y personas son ficticios. Este cuaderno no contiene procedimientos para operar chancadores, molinos, celdas, pilas, hornos, "
             "equipos de electroobtención ni otros equipos; tampoco para manipular reactivos, ácidos, cianuro u otras sustancias químicas, preparar soluciones, tomar muestras, trabajar con altas temperaturas, "
             "metal fundido, gases, espacios confinados ni en altura. " + AVISO + " " + EMER)

build = make_build(MATERIALS)
