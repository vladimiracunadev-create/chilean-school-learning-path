"""Ayudante común de Ciencias Naturales EPJA Media N1, módulo 1 (OAD-01 a OAD-04): materiales y fábrica del registrador por desempeño."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Papel, lápiz y goma. Todo se resuelve con los datos y textos de ejemplo escritos en la ficha de la clase: no se hace ningún experimento ni se necesita "
             "observar el cielo, usar internet ni materiales especiales. Las fichas son inventadas para practicar el método.")
build = make_build(MATERIALS)


def make_k(code, prior):
    """Devuelve K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_) fijado al código del desempeño."""
    def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_):
        if len(op) == 5:  # (enunciado, ejemplo, criterios, evidencia, retroalimentación): los errores son los frecuentes de la clase
            op = (*op[:4], [m[0] for m in mistakes], op[4])
        build(code, n, F, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)
    return K
