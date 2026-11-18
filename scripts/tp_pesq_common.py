"""Ayudante de los cuadernos de Técnico-Profesional Pesquería, 3.º y 4.º medio (student_content_tp_pesq_*)."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora y elementos de protección "
         "(incluido equipo de flotación cuando corresponda); este cuaderno no te habilita para trabajar ni para operar embarcaciones o equipos.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas embarcaciones, redes, cabos, winches, artes de pesca, equipos de cubierta, cuchillos, hielo, combustible, "
             "equipos de seguridad, instrumentos, computador ni internet: las cartas, los planos, las bitácoras, los registros de captura, las planillas y los documentos están descritos por escrito en el enunciado, "
             "son inventados y están rotulados «de ejemplo». Las capturas, cuotas, tallas, vedas, distancias, velocidades, consumos, temperaturas, rendimientos, costos y precios son solo números de ejemplo "
             "para un cálculo en papel: los valores reales dependen de la especie, de la zona y de «la norma vigente» de la autoridad marítima o pesquera. Las especies se nombran como «especie A» y «especie B». "
             "Este cuaderno no contiene instrucciones para navegar ni maniobrar embarcaciones, calar o virar redes, usar artes de pesca, cabos o winches, trabajar en cubierta con mal tiempo, bucear, usar equipos "
             "o maquinaria, manipular combustibles, eviscerar o procesar con cuchillos o maquinaria, ni combatir incendios o rescatar personas. " + AVISO)

EMER = ("Ante un accidente, una caída al agua, un hombre al agua, un atrapamiento, hipotermia o un incendio a bordo: no te acerques a la zona de riesgo ni entres al agua, avisa a un adulto responsable y a emergencias.")

build = make_build(MATERIALS)
