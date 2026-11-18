"""Ayudante de los cuadernos de Técnico-Profesional Operaciones Portuarias, 3.º y 4.º medio (student_content_tp_opor_*)."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente de la entidad fiscalizadora y elementos de protección; "
         "este cuaderno no te habilita para trabajar ni para operar equipos o intervenir en un puerto.")

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas muelles, naves, grúas, montacargas, contenedores, equipos, herramientas, computador ni internet: los documentos de comercio exterior y de transporte "
             "(conocimientos de embarque, manifiestos, guías, listas de embalaje y planillas), los planes y los cronogramas están descritos por escrito en el enunciado, son inventados y están rotulados «de ejemplo». "
             "Los pesos, los volúmenes, las capacidades, los tiempos, los rendimientos, las tasas y los precios son solo números de ejemplo para un cálculo en papel: los valores reales dependen del proyecto, del fabricante, "
             "del puerto y de «la norma vigente» de la autoridad marítima y portuaria. Este cuaderno no contiene instrucciones para izar, estibar, trincar, amarrar, operar grúas, montacargas o tractos, trabajar en muelles o a bordo, "
             "ni manipular mercancías peligrosas. " + AVISO)

EMER = ("Ante un accidente, una caída al agua, un aplastamiento o un derrame: no te acerques a la zona de riesgo ni entres al agua, avisa a un adulto responsable y a emergencias.")

build = make_build(MATERIALS)
