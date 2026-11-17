"""Ayudante de los cuadernos de Técnico-Profesional Gráfica (student_content_tp_graf_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel (o cuaderno); una calculadora simple es opcional. Todos los trabajos, clientes, archivos, medidas, especificaciones, mediciones, precios y plazos "
             "son inventados y están rotulados «de ejemplo»: no hay imágenes, marcas ni clientes reales, y no necesitas software de diseño, internet ni máquinas. "
             "Lo que se describe por escrito (una composición, un color, una prueba) se razona con los datos del enunciado; este cuaderno no reemplaza el taller ni el programa real. "
             "No uses en un trabajo real imágenes, tipografías ni textos ajenos sin revisar su licencia. Si trabajas frente a una pantalla, haz pausas breves y regulares y cuida tu postura. "
             "Esto es aprendizaje conceptual en papel. Practicar tareas con máquinas de impresión, corte o terminación y con tintas o solventes exige instructor autorizado, norma vigente "
             "y elementos de protección; este cuaderno no te habilita para trabajar.")

build = make_build(MATERIALS)
