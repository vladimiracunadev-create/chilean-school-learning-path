"""Ayudante de los cuadernos de Técnico-Profesional Mecánica de Mantenimiento de Aeronaves (3.º y 4.º medio; student_content_tp_meae_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la autoridad aeronáutica y de la entidad fiscalizadora de tu sector y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para intervenir aeronaves, motores, componentes o equipos. La liberación de una aeronave a servicio la firma siempre personal certificado.")

EMER = ("Ante un accidente, un incendio, una fuga, un atrapamiento, una descarga eléctrica o una pieza que se mueve de forma inesperada: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas aeronaves, motores, piezas, herramientas, instrumentos, equipos, computador ni internet: los manuales, los esquemas, las tarjetas de tarea, las órdenes de trabajo, las planillas y los demás documentos del hangar "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo». Las medidas, límites, horas, ciclos, temperaturas, tensiones, intervalos y precios son números de ejemplo "
             "para calcular en una planilla; los valores reales los fijan el fabricante, el manual de mantenimiento y «la norma vigente». Este cuaderno no contiene procedimientos para inspeccionar, desarmar, armar, reparar ni probar aeronaves o motores, "
             "para manejar combustible, oxígeno, sistemas hidráulicos o eléctricos, ni para trabajar en altura. " + AVISO + " " + EMER)

build = make_build(MATERIALS)
