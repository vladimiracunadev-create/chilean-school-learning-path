"""Ayudantes del módulo 4 de Matemática EPJA Básica N2 (estadística: media, moda y mediana). Todo en papel; datos inventados."""
from __future__ import annotations

from collections import Counter

from hc_common import make_build
from student_lessons import fmt

MATERIALS = "Papel, lápiz y goma. Todos los datos están escritos en la ficha y son de ejemplo (inventados); el dinero es de ejemplo. No se usa calculadora: las cuentas son amables y se hacen en papel."
build = make_build(MATERIALS)

PRIOR = ["Ya sé sumar, restar, multiplicar y dividir con números naturales y decimales sencillos.", "He leído tablas y listas de datos en boletas, cuentas y avisos."]


def ls(data):
    """Lista de datos como texto: 12, 15, 18."""
    return ", ".join(fmt(x) if not isinstance(x, str) else x for x in data)


def S(data):
    """Suma como expresión: 12+15+18."""
    return "+".join(str(x) for x in data)


def mean_expr(data):
    return f"({S(data)})/{len(data)}"


def mean(data):
    return fmt(sum(data) / len(data))


def med(data):
    s = sorted(data)
    n = len(s)
    return fmt(s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2)


def modes(data):
    c = Counter(data)
    m = max(c.values())
    return sorted(k for k, v in c.items() if v == m)


def mode(data):
    ms = modes(data)
    assert len(ms) == 1, data
    return fmt(ms[0])


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo, criterios, evidencia, errores, retroalimentación)."""
    build(oa, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=op, reinforce=rf, extend=ex_)
