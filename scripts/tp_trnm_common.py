"""Ayudante de los cuadernos de Técnico-Profesional Tripulación de Naves Mercantes y Especiales, 3.º y 4.º medio (student_content_tp_trnm_*)."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la autoridad marítima y elementos de protección "
         "(incluido equipo de flotación); este cuaderno no te habilita para trabajar ni para operar naves o equipos.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas naves, botes, balsas, equipos, máquinas, herramientas, cartas náuticas reales, instrumentos, computador ni internet: "
             "las cartas, las planillas, las bitácoras, los registros, los planes de guardia y los documentos de la nave están descritos por escrito en el enunciado, son inventados y están rotulados «de ejemplo». "
             "Los rumbos, las distancias, las velocidades, los consumos, los tiempos, las capacidades, los costos y los precios son solo números de ejemplo para un cálculo en papel: los valores reales dependen de la nave, "
             "del fabricante, del armador y de «la norma vigente» de la autoridad marítima. Este cuaderno no contiene instrucciones para navegar ni maniobrar una nave, fondear o amarrar, abandonar una nave, rescatar a una persona del agua, "
             "usar botes o balsas salvavidas, combatir incendios, trabajar en cubierta con mal tiempo, manejar combustibles o carga peligrosa, trabajar en altura o en espacios cerrados, ni operar máquinas, calderas o equipos de maniobra. "
             + AVISO)

EMER = ("Ante un accidente, una caída al agua, un hombre al agua, un incendio o una escora peligrosa (inclinación peligrosa de la nave): no te acerques a la zona de riesgo ni entres al agua, "
        "da la alarma, avisa a un adulto responsable y a emergencias.")

build = make_build(MATERIALS)
