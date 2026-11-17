"""Ayudante de los cuadernos de Creación y composición musical, 3.º y 4.º medio HC (student_content_hc_ccmu_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y papel. Todas las obras, motivos, ritmos, formas, arreglos, programas y casos están descritos por escrito en cada ejercicio: "
             "son originales e inventados para este cuaderno, así que no necesitas audio, partituras, instrumentos ni internet. "
             "Este cuaderno no usa software de música ni grabación real: si tu docente lo ofrece, es un complemento que aquí queda como vacío. "
             "Si tu docente organiza práctica en sala, trabaja a volumen moderado, haz pausas de silencio y no pongas auriculares a todo volumen. "
             "No grabes ni publiques a otras personas sin su permiso, y avisa a una persona adulta si algo te incomoda.")

# Clave de lectura de la notación en texto que se repite en las fichas (cada ficha debe bastarse sola).
CLAVE = ("Clave de lectura (notación en texto): cada palabra es un pulso; un nombre de nota (Do, Re, Mi, Fa, Sol, La, Si; escala de Do mayor) "
         "es un sonido que dura un pulso; «-» prolonga el sonido anterior un pulso más; «.» es un silencio de un pulso; «|» separa compases de 4 pulsos.")

build = make_build(MATERIALS)
