"""Ayudante común del módulo 4 de HGCS EPJA Media N1 (OAD-13 a OAD-16): fija materiales y la función K."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Todas las fuentes, relatos, tablas y datos de comunidades que se usan están escritos en cada ficha y son inventados «de ejemplo»; "
             "no necesitas internet, mapas, fotos ni videos. Los hechos históricos que se nombran son los básicos de cualquier texto escolar. "
             "Se trabaja con respeto: las memorias dolorosas, los pueblos originarios y las comunidades migrantes merecen cuidado, y nadie está obligado a contar su historia personal ni a tomar partido. "
             "Lo que sepa la comunidad o quienes portan una tradición lo enseñan ellas y ellos; este cuaderno no reemplaza esa voz.")
build = make_build(MATERIALS)

PRIOR = ["Sé leer textos breves, tablas simples y fechas.", "He escuchado hablar de hechos del pasado de Chile en mi familia, en el trabajo o en las noticias.",
         "Distingo lo que dice un texto de lo que yo supongo."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo, criterios, evidencia, errores, retroalimentación)."""
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=op, reinforce=rf, extend=ex_)
