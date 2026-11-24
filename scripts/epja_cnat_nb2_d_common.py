"""Ayudante de Ciencias Naturales EPJA Básica N2, módulo 4 (student_content_epja_cnat_nb2_d*).

Uso: `from epja_cnat_nb2_d_common import K, O13, O14, O15, O16`. La forma de los ejercicios es la de hc_common.
«{F}» dentro del enunciado se reemplaza por la ficha de la clase.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los datos, tablas y descripciones están escritos en cada ejercicio y son de ejemplo, inventados para este cuaderno. "
    "No se hacen experimentos en la clase: los procedimientos se describen y se analizan sus datos. No necesitas internet, calculadora ni instrumentos. "
    "No manipules químicos, fuego ni electricidad de red para ninguna actividad. No escribas datos personales reales."
)


build = make_build(MATERIALS)

O13 = "EPJA-CNAT-NB2-OAD-13"
O14 = "EPJA-CNAT-NB2-OAD-14"
O15 = "EPJA-CNAT-NB2-OAD-15"
O16 = "EPJA-CNAT-NB2-OAD-16"
PRIOR = ["Ya observo el aire, el agua, el suelo, el día y la noche en mi vida diaria.",
         "Sé leer una tabla sencilla y comparar números."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo, criterios, evidencia, errores, retroalimentación)."""
    if len(op) == 5:
        stmt, example, crit, errors, feedback = op
        evidence = ["Producción escrita en el cuaderno que muestra: " + crit[0], "Explicación breve de cómo llegó a su respuesta, escrita o dicha en voz alta"]
        op = (stmt, example, crit, evidence, errors, feedback)
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
          T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)
