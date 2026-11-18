"""Ayudante de los cuadernos de Técnico-Profesional Acuicultura, 3.º y 4.º medio (student_content_tp_acui_*)."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora y elementos de protección "
         "(incluido equipo de flotación cuando corresponda); este cuaderno no te habilita para trabajar ni para operar equipos o embarcaciones.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas peces, moluscos, algas, agua, redes, balsas, embarcaciones, equipos de buceo, grúas, productos, "
             "instrumentos, computador ni internet: los planos, esquemas, planillas, registros, fichas y documentos de los centros de cultivo están descritos por escrito en el enunciado, son inventados "
             "y están rotulados «de ejemplo». Las densidades, pesos, temperaturas, oxígeno, alimentos, mortalidades, costos, precios y rendimientos son solo números de ejemplo para un cálculo en papel: "
             "los valores reales dependen de la especie, del plan de manejo, del fabricante y de «la norma vigente» de la entidad fiscalizadora de tu sector. Las especies se nombran como «especie A» y «especie B». "
             "Este cuaderno no contiene instrucciones para trabajar en el mar, operar embarcaciones, bucear, maniobrar balsas jaula, redes o fondeos, usar grúas o equipos, manejar oxígeno u otros gases, "
             "manipular o aplicar medicamentos, vacunas, desinfectantes o químicos, ni realizar cosecha o sacrificio. " + AVISO)

EMER = ("Ante un accidente, una caída al agua, un ahogamiento, hipotermia o una intoxicación: no te acerques a la zona de riesgo ni entres al agua, avisa a un adulto responsable y a emergencias.")

build = make_build(MATERIALS)
