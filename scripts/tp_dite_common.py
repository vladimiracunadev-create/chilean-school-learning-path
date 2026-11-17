"""Ayudante de los cuadernos de Técnico-Profesional Dibujo Técnico (student_content_tp_dite_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, papel (o cuaderno) y, si tienes, regla y escuadra; una calculadora simple es opcional. Todo se resuelve en papel: los planos, vistas, cortes, cotas, símbolos, "
             "tablas y listas de materiales están DESCRITOS por escrito dentro del enunciado, con datos inventados y rotulados «de ejemplo». Este cuaderno no trae imágenes ni usa software de dibujo "
             "(CAD) ni de modelado 3D: lo digital se trabaja solo como concepto y en cálculos. Las normas de dibujo se mencionan solo en general («la norma de dibujo vigente»). "
             "Los planos y diseños son propiedad intelectual de quien los crea y confidenciales para quien los encarga: no los copies ni los compartas sin permiso. Si dibujas muchas horas, cuida la postura y haz pausas breves. "
             "Esto es aprendizaje conceptual en papel. Practicar tareas de medición en terreno, construcción, instalaciones o fabricación mecánica exige instructor autorizado, norma vigente "
             "(por ejemplo, la entidad fiscalizadora de tu sector) y elementos de protección; este cuaderno no te habilita para trabajar.")

build = make_build(MATERIALS)
