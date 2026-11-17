"""Ayudante de los cuadernos de Técnico-Profesional Refrigeración y Climatización, 3.º y 4.º medio (student_content_tp_recl_*). Riesgo ALTO: solo conceptos, lectura de documentos y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para intervenir equipos.")

EMER = ("Ante un accidente, una fuga, una intoxicación, un atrapamiento en una cámara o una descarga eléctrica: no entres ni toques, avisa a un adulto responsable y llama a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas equipos, herramientas, instrumentos, refrigerantes, tuberías, computador ni internet: los planos y esquemas "
             "(descritos por escrito con leyendas y listas), las planillas de cubicación, los registros de lecturas, las fichas técnicas, las fichas de datos de seguridad, los planes de mantención, "
             "las bitácoras y las listas de materiales están escritos en el enunciado, son inventados y están rotulados «de ejemplo». Las temperaturas, presiones, potencias, cargas, límites, índices y precios "
             "son de ejemplo y sirven solo para calcular en una planilla; los valores reales los fijan el fabricante, el proyecto y «la norma vigente». Este cuaderno no contiene procedimientos de manejo, carga, "
             "recuperación, soldadura, evacuación, conexión, puesta en marcha, medición ni prueba de equipos reales, ni de trabajo en altura, en techos o en cámaras frigoríficas. "
             + AVISO + " " + EMER)

build = make_build(MATERIALS)
