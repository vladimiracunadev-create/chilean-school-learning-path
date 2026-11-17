"""Ayudante de los cuadernos de Técnico-Profesional Electricidad, 3.º y 4.º medio (student_content_tp_elec_*). Riesgo ALTO: solo conceptos y lectura de documentos."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora (SEC) y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para intervenir instalaciones eléctricas.")

EMER = ("Si alguien sufre una descarga eléctrica, una quemadura o un incendio: no toques a la persona si sigue en contacto con la energía, corta el suministro solo si estás autorizado, "
        "avisa a un adulto responsable y llama a emergencias.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas cables, herramientas, instrumentos, tableros, computador ni internet: los planos y diagramas "
             "(descritos por escrito con leyendas y listas de conexiones), los cuadros de carga, las memorias de cálculo, los presupuestos, las órdenes de trabajo y los catálogos están escritos "
             "en el enunciado, son inventados y están rotulados «de ejemplo». Las tensiones, potencias, resistencias, límites y precios son de ejemplo y sirven solo para calcular en una planilla; "
             "los valores reales los fija «la norma vigente» y el proyecto. Este cuaderno no contiene procedimientos de conexión, instalación, medición, mantenimiento ni trabajo con energía. "
             + AVISO + " " + EMER)

build = make_build(MATERIALS)
