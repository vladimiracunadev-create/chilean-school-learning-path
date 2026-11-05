"""Ayudantes compartidos por los módulos student_content_in_m2_* (Inglés oficial, 2.º medio).

`ml` arma una pregunta de escucha (el guion va escrito en el enunciado y lo lee un adulto) y `mr` una pregunta de
lectura. Las alternativas se escriben con la correcta primera: el registro balancea su posición.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

ADULT = "Un adulto lee en voz alta (tapa el guion): "
MAT_L = "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz."
MAT_R = "Los textos escritos en cada ejercicio, lápiz y una hoja para anotar."


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def mc(stem, right, wrongs, why):
    options = [o.strip().rstrip(".?!,;") for o in [right] + list(wrongs)]
    q = stem + " " + " ".join(f"{'ABC'[i]}) {o}" for i, o in enumerate(options))
    return ex(q, f"A) {right}", why)


def ml(text, q, right, wrongs, why):
    """Pregunta de escucha: el guion va dentro del enunciado."""
    return mc(ADULT + text + " " + q, right, wrongs, why)


def mr(text, q, right, wrongs, why):
    """Pregunta de lectura: el texto va dentro del enunciado."""
    return mc(text + " " + q, right, wrongs, why)


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )
