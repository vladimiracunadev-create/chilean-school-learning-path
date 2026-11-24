"""Ayudante común del módulo 2 de HGCS EPJA Media N1 (OAD-05 a OAD-08): fija materiales y la función K."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Todas las fuentes, tablas y datos que se usan están escritos en cada ficha y son inventados «de ejemplo»; no necesitas internet, "
             "mapas, fotos ni videos. Cuando la clase habla de ubicaciones o de territorio, se describen en palabras o en tablas. "
             "Los hechos históricos que se nombran son los básicos de cualquier texto escolar. Tu experiencia de vida es un buen punto de partida, "
             "pero nadie te pide contar datos personales ni tomar partido: trabajamos con respeto y con evidencia.")
build = make_build(MATERIALS)

PRIOR = ["Sé leer textos breves, tablas simples y fechas.", "He escuchado hablar de hechos históricos en mi familia, en el trabajo o en las noticias.",
         "Distingo lo que dice un texto de lo que yo supongo."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo, criterios, evidencia, errores, retroalimentación)."""
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=op, reinforce=rf, extend=ex_)
