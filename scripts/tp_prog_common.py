"""Ayudante de los cuadernos de Técnico-Profesional Programación (student_content_tp_prog_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas computador, internet ni instalar nada: el código "
             "(Python breve o pseudocódigo), las tablas, los usuarios, las empresas y los datos están escritos en el enunciado, son inventados y están "
             "rotulados «de ejemplo», y se razonan «a mano». Nunca escribas contraseñas reales ni datos personales de nadie. Los plazos, versiones y requisitos "
             "reales dependen de la empresa y de «la norma vigente»: aquí se usan valores rotulados «de ejemplo». Si el trabajo con pantalla es largo, haz pausas "
             "y cuida tu postura. Esto es aprendizaje en papel: no te habilita para instalar, modificar ni administrar sistemas de una organización sin autorización.")

build = make_build(MATERIALS)
