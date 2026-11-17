"""Ayudante de los cuadernos de Técnico-Profesional Servicios de Turismo (student_content_tp_setu_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. Todo se resuelve en papel: itinerarios, tarifas, reservas, programas turísticos, fichas de atractivos "
             "y de pasajeros, destinos, agencias, personas y precios son inventados y están rotulados «de ejemplo»; no necesitas software, internet ni documentos reales, y no se usan marcas ni operadores reales. "
             "Los datos de clientes y pasajeros son personales: se piden solo los necesarios, se guardan con clave y no se comparten sin autorización. Se atiende a todas las personas con respeto, "
             "sin estereotipos, y se pregunta a cada una qué apoyo necesita. Las normas, tasas y plazos dependen de «la norma vigente». Quien atiende público muchas horas debe alternar posturas y hacer pausas breves. "
             "Los temas de turismo aventura, transporte, actividades acuáticas, en altura o de seguridad en terreno se tratan solo como conceptos y avisos. "
             "Esto es aprendizaje conceptual en papel. Practicar esas tareas exige guía o instructor autorizado, norma vigente (por ejemplo, la entidad fiscalizadora de tu sector) y elementos de protección; este cuaderno no te habilita para trabajar.")

build = make_build(MATERIALS)
