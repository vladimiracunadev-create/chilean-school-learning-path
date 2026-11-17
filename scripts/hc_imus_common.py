"""Ayudante de los cuadernos de Interpretación musical, 3.º y 4.º medio HC (student_content_hc_imus_*)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y papel. Todas las piezas, ritmos, partes, programas, bitácoras y casos están descritos por escrito en cada ejercicio: "
             "son originales e inventados para este cuaderno, así que no necesitas audio, partituras, instrumentos ni internet. "
             "Si tu docente organiza ensayo en sala, trabaja a volumen moderado, haz pausas de silencio, calienta voz o manos con suavidad "
             "y detente si sientes dolor, tensión fuerte o fatiga en la voz, el cuello, las manos o los oídos. "
             "No grabes ni publiques a otras personas sin su permiso, y avisa a una persona adulta si algo te incomoda. "
             "Las obras y los intérpretes reales los aporta tu docente: aquí no se reproduce ninguna melodía ni letra con derechos.")

# Clave de lectura de la notación en texto; se repite en las fichas para que cada una se baste sola.
CLAVE = ("Clave de lectura (notación en texto): cada casilla es un pulso; «X» es un sonido o golpe, «.» es un silencio de un pulso, «-» prolonga el sonido anterior; "
         "«|» separa compases de 4 pulsos; los nombres Do Re Mi Fa Sol La Si son notas de la escala de Do mayor; «p» es suave, «mf» es medio, «f» es fuerte; "
         "«<» es ir subiendo la fuerza poco a poco y «>» es ir bajándola; «/» marca una respiración o un corte entre frases.")

build = make_build(MATERIALS)
