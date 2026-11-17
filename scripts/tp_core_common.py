"""Ayudante de los cuadernos de Técnico-Profesional Conectividad y Redes (student_content_tp_core_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. Todas las redes, planos, diagramas, direcciones, nombres de equipos y de redes, "
             "mediciones y configuraciones son inventados y están rotulados «de ejemplo»: se usan solo direcciones privadas o ficticias, no hay claves ni credenciales reales "
             "y no necesitas software, internet ni equipos. No pruebes lo aprendido en redes ajenas ni sin autorización de la persona responsable. "
             "Esto es aprendizaje conceptual en papel. Practicar tareas de cableado, trabajo en altura o con electricidad exige instructor autorizado, norma vigente y elementos de protección; "
             "este cuaderno no te habilita para trabajar.")

build = make_build(MATERIALS)
