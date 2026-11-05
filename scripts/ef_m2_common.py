"""Ayuda compartida para los módulos ef_m2_* (Educación Física y Salud, 2.º medio)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register  # noqa: F401


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, r, u, a, z, ch, context, selfcheck, open_task, reinforce, extend):
    """Registra una clase con forma compacta."""
    register(
        oa, n,
        materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": ans} for t, p, s, ans in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": r, "understand": u, "apply": a, "reason": z, "challenge": ch},
        context=context, selfcheck=selfcheck, open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )
