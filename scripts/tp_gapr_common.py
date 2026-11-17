"""Ayudante de los cuadernos de Técnico-Profesional Gastronomía, mención Pastelería y Repostería de 4.º medio (student_content_tp_gapr_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel (o cuaderno); una calculadora simple es opcional. Todos los establecimientos, proveedores, productos, cantidades, precios, horarios, temperaturas y plazos "
             "son inventados y están rotulados «de ejemplo»: no hay marcas ni restaurantes reales y no necesitas cocina, alimentos, software ni equipos. "
             "Los valores de ejemplo no reemplazan los límites que fija la norma vigente (autoridad sanitaria). Aquí no hay recetas ni técnicas de cocción o corte paso a paso: solo conceptos, registros, cálculos y reglas generales. "
             "Alérgenos: se estudian como concepto y rotulado; ante una reacción de una persona, se avisa de inmediato a un adulto responsable y a los servicios de emergencia. "
             "Esto es aprendizaje conceptual en papel. El trabajo con alimentos, fuego, gas, freidoras, cuchillos, hornos, equipos y productos de limpieza requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria); este cuaderno no te habilita para trabajar.")

build = make_build(MATERIALS)
