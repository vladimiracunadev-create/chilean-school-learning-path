"""Ayudante de los cuadernos de Técnico-Profesional Mecánica Industrial, mención Máquinas-Herramientas (4.º medio) (student_content_tp_memh_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora de tu sector y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para operar máquinas, herramientas o equipos.")

EMER = ("Ante un accidente, un atrapamiento, un corte, una quemadura, una descarga eléctrica o un incendio: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas piezas, máquinas, herramientas, instrumentos, equipos, computador ni internet: los planos y hojas de proceso (descritos por escrito), las tablas de parámetros de ejemplo, las planillas de tiempos y de costos, las listas de herramientas y los registros "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo». Las medidas, tolerancias, tiempos, rendimientos, consumos, pesos, presiones, cargas y precios son números de ejemplo "
             "para calcular en una planilla; los valores reales los fijan el fabricante, el proyecto y «la norma vigente». Este cuaderno no contiene procedimientos de uso de tornos, fresadoras, rectificadoras, taladros, centros de mecanizado ni máquinas CNC, ni programas de control numérico ejecutables, ni instrucciones de montaje de piezas, herramientas de corte o refrigerantes. " + AVISO + " " + EMER)

build = make_build(MATERIALS)
