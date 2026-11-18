"""Ayudante de los cuadernos de Técnico-Profesional Mecánica Industrial, mención Matricería (4.º medio) (student_content_tp_mema_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora de tu sector y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para operar máquinas, herramientas o equipos.")

EMER = ("Ante un accidente, un atrapamiento, un corte, una quemadura, una descarga eléctrica o un incendio: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas piezas, máquinas, herramientas, instrumentos, equipos, computador ni internet: los planos y despieces (descritos por escrito), las fichas de moldes y matrices, las planillas de producción y de calidad, las hojas de registro y los documentos de gestión de residuos "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo». Las medidas, tolerancias, tiempos, rendimientos, consumos, pesos, presiones, cargas y precios son números de ejemplo "
             "para calcular en una planilla; los valores reales los fijan el fabricante, el proyecto y «la norma vigente». Este cuaderno no contiene procedimientos para fabricar, montar, desmontar, ajustar, mantener, retocar ni probar matrices o moldes, ni para operar prensas, inyectoras, máquinas o software de diseño, ni para manipular residuos. " + AVISO + " " + EMER)

build = make_build(MATERIALS)
