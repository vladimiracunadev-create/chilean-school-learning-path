"""Ayudante de los cuadernos de Técnico-Profesional Contabilidad (student_content_tp_cont_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. Todos los documentos, cuentas, empresas, personas, RUT e importes "
             "son inventados y están rotulados «de ejemplo»: no necesitas software, internet ni documentos reales. Las tasas, plazos y valores legales "
             "dependen de «la norma vigente»: tu docente o el Servicio de Impuestos Internos informan los reales; aquí se usan tasas rotuladas «de ejemplo». "
             "No uses datos personales reales de nadie. Esto es aprendizaje en papel: no te habilita para firmar, presentar ni declarar documentos de una empresa.")

build = make_build(MATERIALS)
