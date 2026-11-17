"""Ayudante de los cuadernos de Técnico-Profesional Vestuario y Confección Textil, 3.º y 4.º medio (student_content_tp_vcte_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel (o cuaderno); una calculadora simple es opcional. Todos los talleres, prendas, telas, medidas, tallas, tolerancias, tiempos, precios y cantidades "
             "son inventados y están rotulados «de ejemplo»: no hay marcas ni empresas reales y no necesitas taller, telas, máquinas ni software. "
             "Los valores de ejemplo no reemplazan los que fijan la ficha técnica real, el manual del fabricante ni la norma vigente. Aquí no hay procedimientos de corte, costura, planchado ni confección paso a paso, ni ajustes u operación de máquinas: solo conceptos, documentos, cálculos y reglas generales. "
             "Tijeras, cortadoras, agujas, máquinas de coser industriales, planchas, vapor y productos químicos (tintes, quitamanchas) se estudian solo como concepto. Ante un accidente, se avisa de inmediato a un adulto responsable y a emergencias. "
             "Esto es aprendizaje conceptual en papel. El trabajo con máquinas de coser industriales, cortadoras, planchas, vapor, tijeras, agujas y productos químicos requiere instructor/docente de la especialidad y norma vigente; este cuaderno no te habilita para trabajar.")

build = make_build(MATERIALS)
