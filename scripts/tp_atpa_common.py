"""Ayudante de los cuadernos de Técnico-Profesional Atención de Párvulos (student_content_tp_atpa_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel (o cuaderno); una calculadora simple es opcional. Todos los jardines infantiles, niños, niñas, familias, horarios, listas y cantidades "
             "son inventados y están rotulados «de ejemplo»: no hay datos de niños reales, fotos ni marcas, y no necesitas software, internet ni equipos. "
             "Los casos se resuelven en papel con los datos escritos en el enunciado. Los antecedentes de los niños y sus familias son personales y confidenciales. "
             "El trato es siempre respetuoso, sin estereotipos de género y con respeto a la diversidad cultural y de capacidades. "
             "Ante un accidente, un malestar o la sospecha de maltrato, no se actúa por cuenta propia: se avisa de inmediato a la educadora o al adulto responsable y, si corresponde, a emergencias o a las redes de protección según el protocolo del establecimiento. "
             "Esto es aprendizaje conceptual en papel. Trabajar con niños y niñas exige práctica supervisada por la educadora y la norma vigente; este cuaderno no reemplaza esa práctica ni te habilita para trabajar.")

LIM = (" Esto es aprendizaje conceptual en papel, con casos ficticios: trabajar con niños y niñas exige la supervisión de la educadora y la norma vigente, "
       "y este cuaderno no te habilita para trabajar.")

build = make_build(MATERIALS)
