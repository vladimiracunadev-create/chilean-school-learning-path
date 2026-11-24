"""Ayudante común del módulo 1 de HGCS EPJA Media N1 (OAD-01 a OAD-04): fija materiales y la lista de saberes previos."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Todas las fuentes, tablas y datos están escritos en cada ficha y son inventados («de ejemplo»); no necesitas internet, "
             "mapas ni libros. Donde la clase habla de un mapa o de un gráfico, usa la tabla o la descripción escrita. "
             "Tu experiencia de trabajo y de vida es un buen punto de partida, pero nadie te pide contar datos personales: puedes trabajar solo con los casos del cuaderno.")
build = make_build(MATERIALS)

PRIOR_BASE = ["Sé leer textos breves y tablas sencillas, con apoyo si lo necesito.",
              "Ubico en el tiempo cosas que ya pasaron: «antes», «después» y «hace años».",
              "Tengo experiencia de vida y de trabajo que me sirve para entender cómo cambian las cosas."]
