"""Ayudante de los cuadernos de Técnico-Profesional Servicios de Hotelería (student_content_tp_seho_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel (o cuaderno); una calculadora simple es opcional. Todos los hoteles, personas, reservas, tarifas, precios, tipos de cambio, horarios e inventarios "
             "son inventados y están rotulados «de ejemplo»: no hay marcas ni cadenas reales y no necesitas software hotelero, internet ni equipos. "
             "Lo que se describe por escrito (una reserva, un folio, un informe de habitaciones) se resuelve con los datos del enunciado. "
             "Los datos de los huéspedes son personales y confidenciales: en un trabajo real no se comentan ni se entregan a terceros. El trato es respetuoso, accesible y sin discriminación. "
             "Ante una emergencia, un accidente o un malestar de una persona, se avisa de inmediato a personal capacitado o a los servicios de emergencia. "
             "Esto es aprendizaje conceptual en papel. La limpieza con productos químicos, la lavandería, la cocina del desayuno, la evacuación y el combate de incendios exigen instructor autorizado, "
             "norma vigente y elementos de protección; este cuaderno solo da conceptos y reglas generales y no te habilita para trabajar.")

build = make_build(MATERIALS)
