"""Ayudante de los cuadernos de los Objetivos de aprendizaje genéricos de la formación técnico-profesional (student_content_tp_gene_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel (o cuaderno); una calculadora simple es opcional. Todas las empresas, personas, documentos, horarios, precios, sueldos, tasas, cuotas y cifras "
             "son inventados y están rotulados «de ejemplo»: no hay marcas ni instituciones concretas como protagonistas y no necesitas software, internet ni equipos. "
             "Los casos escritos (una oficina, un taller, una cocina, una bodega, una obra, un centro de salud) se resuelven con los datos del enunciado. "
             "Los datos personales de compañeros, clientes y pacientes son confidenciales; el trato es respetuoso, accesible y sin discriminación. "
             "Este cuaderno no es asesoría legal, previsional, financiera ni de seguridad: sirve para entender conceptos y aprender a informarse con las fuentes oficiales y con tu profesor, tu jefatura o la entidad que corresponda. "
             "Ante un accidente, un malestar o una situación de acoso o violencia, avisa de inmediato a una persona adulta responsable o a quien corresponda en tu establecimiento o empresa. "
             "Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente (por ejemplo, la entidad fiscalizadora de tu sector) y elementos de protección; este cuaderno no te habilita para trabajar.")

build = make_build(MATERIALS)
