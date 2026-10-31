"""Ayudante común de los cuadernos de 6.º básico Historia (no registra clases)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register  # noqa: F401

MAT = "Este cuaderno y un lápiz. Los mapas, tablas y textos que se usan están escritos en cada ejercicio."


def _e(items):
    return [i if isinstance(i, dict) else ex(*i) for i in items]


def lesson(oa, n, use, prior, explain, vocab, worked, mistakes, r, c, a, z, h, ctx, sc, op, reinforce, extend, materials=MAT):
    """Registra una clase con datos compactos: ejercicios como tuplas (enunciado, respuesta, porqué) o resultados de arith."""
    register(
        oa, n,
        materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": an} for t, p, s, an in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": _e(r), "understand": _e(c), "apply": _e(a), "reason": _e(z), "challenge": _e(h)},
        context=_e(ctx), selfcheck=_e(sc), open_task=task(*op), reinforce=reinforce, extend=extend,
    )
