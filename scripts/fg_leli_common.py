"""Ayudantes comunes del cuaderno del estudiante de Lengua y Literatura, 3.º y 4.º medio Formación General."""
from __future__ import annotations

from student_lessons import arith, ex, register

E = ex

MAT = "Este cuaderno, lápiz y los textos y datos escritos en cada ejercicio. No necesitas libros especiales ni internet."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def L(oa, n, use, prior, explain, vocab, worked, mistakes, tiers, ctx, sc, open_task, reinforce, extend, materials=MAT):
    """worked: lista de (title, problem, steps, answer); mistakes: lista de (wrong, why, fix);
    tiers: 5 listas de ejercicios (recovery 3, understand 3, apply 3, reason 2, challenge 2);
    open_task: (statement, example, criteria, evidence, errors, feedback)."""
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=dict(zip(("recovery", "understand", "apply", "reason", "challenge"), tiers)),
        context=ctx, selfcheck=sc, open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )
