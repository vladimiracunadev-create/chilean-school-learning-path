"""Ayudante compartido por los módulos student_content_hi5_*: arma una clase a partir de datos compactos."""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _e(item, ficha):
    """Convierte (q, a, why) o ('=', q, expr, why[, unidad]) en un ejercicio cerrado; «{F}» se reemplaza por la ficha."""
    if item[0] == "=":
        _, q, expr, why, *rest = item
        return arith(q.replace("{F}", ficha), expr, why, rest[0] if rest else "")
    q, a, why = item
    return ex(q.replace("{F}", ficha), a, why)


def build(oa, n, F, use, prior, explain, vocab, worked, mistakes, T, ctx, sc, op, reinforce, extend, materials=None):
    """T: 13 ejercicios (3/3/3/2/2). worked: (título, problema, pasos, respuesta). mistakes: (error, causa, corrección)."""
    assert len(T) == 13, (oa, n, len(T))
    cuts = (0, 3, 6, 9, 11, 13)
    names = ("recovery", "understand", "apply", "reason", "challenge")
    tiers = {names[i]: [_e(x, F) for x in T[cuts[i]:cuts[i + 1]]] for i in range(5)}
    register(
        oa, n,
        materials=materials or "Lápiz y papel. Todas las fichas, textos y datos están escritos en cada ejercicio; no necesitas libros ni internet.",
        use=use,
        prior=prior,
        explain=explain,
        vocab=vocab,
        worked=[{"title": t, "problem": p.replace("{F}", F), "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=tiers,
        context=[_e(ctx, F)],
        selfcheck=[_e(x, F) for x in sc],
        open_task=task(op[0].replace("{F}", F), *op[1:]),
        reinforce=reinforce,
        extend=extend,
    )
