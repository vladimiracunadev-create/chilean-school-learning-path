"""Ayudante de los cuadernos de Técnico-Profesional Electrónica, 3.º y 4.º medio (student_content_tp_eltr_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas componentes, herramientas, instrumentos, computador ni internet: los esquemas "
             "(descritos con listas de componentes y conexiones), los códigos de colores, las hojas de datos, las tablas de mediciones, los inventarios y los precios están escritos "
             "en el enunciado, son inventados y están rotulados «de ejemplo». Todas las tensiones son bajas y de ejemplo; los valores reales dependen del fabricante, del proyecto y de "
             "«la norma vigente» (por ejemplo, la de la Superintendencia de Electricidad y Combustibles, SEC). Este cuaderno no contiene instrucciones de armado, soldadura, conexión a la red "
             "eléctrica ni medición en equipos reales. Esto es aprendizaje conceptual en papel: la red eléctrica domiciliaria, las baterías, los condensadores cargados, la soldadura y las "
             "herramientas requieren instructor/docente de la especialidad y norma vigente (SEC); este cuaderno no te habilita para trabajar.")

AVISO = ("Esto es aprendizaje conceptual en papel: la red eléctrica domiciliaria, las baterías, los condensadores cargados, la soldadura y las herramientas requieren "
         "instructor/docente de la especialidad y norma vigente (SEC); este cuaderno no habilita para trabajar.")

EMER = ("Si alguien sufre una descarga eléctrica, una quemadura o un incendio: no toques a la persona si sigue en contacto con la energía, corta el suministro solo si estás autorizado, "
        "avisa a un adulto responsable y llama a emergencias.")

build = make_build(MATERIALS)
