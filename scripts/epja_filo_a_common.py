"""Ayudante común de Filosofía EPJA Media N1 y N2, módulo 1 (OAD-01 a OAD-04).

Los textos filosóficos son paráfrasis originales; las posiciones personales solo van en la actividad abierta."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Todos los textos, diálogos y casos son de ejemplo, escritos para esta clase (personas ficticias); no se usa internet ni libros. "
             "Todo se resuelve con lo escrito en la ficha. Las preguntas cerradas tienen una respuesta defendible con las razones que se entregan; tu postura personal se escribe solo en la actividad abierta.")
build = make_build(MATERIALS)

PRIOR = ["Me he preguntado alguna vez «¿por qué las cosas son así?» en el trabajo, la familia o la comunidad.",
         "He discutido con alguien dando razones para defender lo que pienso."]


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    stmt, example, crit, ev, err, fb = op
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=(stmt, example, crit, ev, err, fb), reinforce=rf, extend=ex_)
