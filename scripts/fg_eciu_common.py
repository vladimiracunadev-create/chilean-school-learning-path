"""Ayudante de los cuadernos de Educación Ciudadana de 3.º y 4.º medio Formación General (student_content_fg_eciu_*).

No registra clases por sí mismo. Forma compacta de ejercicio:
  (q, a, why)                          respuesta breve
  ("ab", stem, correcta, incorrecta, why)          dos opciones (el registro las balancea)
  ("abc", stem, correcta, mala1, mala2, why)       tres opciones
  ("=", q, expr, why[, unidad])                   respuesta calculada
«{F}» dentro del enunciado se reemplaza por la ficha de la clase.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

MATERIALS = "Lápiz y papel. Todos los casos, textos y datos están escritos en cada ejercicio (son casos de ejemplo, inventados para este cuaderno); no necesitas libros ni internet."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _why(why, good):
    """La justificación debe explicar por sí sola; ya no se completa de forma automática."""
    assert len(why.split()) >= 6, f"justificación demasiado breve ({why!r}): escribe por qué es correcta"
    return why


def _e(item, ficha):
    kind = item[0]
    need = {"=": (4, 5), "ab": (5, 5), "abc": (6, 6)}.get(kind, (3, 3))
    assert need[0] <= len(item) <= need[1], f"ejercicio mal formado ({len(item)} campos): {str(item[1] if kind in need else item[0])[:80]}"
    if kind == "=":
        _, q, expr, why, *rest = item
        return arith(q.replace("{F}", ficha), expr, why, rest[0] if rest else "")
    if kind == "ab":
        _, stem, good, bad, why = item
        why = _why(why, good)
        return ex(f"{stem} A) {good} B) {bad}".replace("{F}", ficha), f"A) {good}", why)
    if kind == "abc":
        _, stem, good, b1, b2, why = item
        why = _why(why, good)
        return ex(f"{stem} A) {good} B) {b1} C) {b2}".replace("{F}", ficha), f"A) {good}", why)
    q, a, why = item
    why = _why(why, a)
    return ex(q.replace("{F}", ficha), a, why)


def build(oa, n, F, use, prior, explain, vocab, worked, mistakes, T, ctx, sc, op, reinforce, extend):
    """T: 13 ejercicios (3/3/3/2/2). worked: (título, problema, pasos, respuesta). mistakes: (error, causa, corrección)."""
    assert len(T) == 13, (oa, n, len(T))
    cuts = (0, 3, 6, 9, 11, 13)
    names = ("recovery", "understand", "apply", "reason", "challenge")
    tiers = {names[i]: [_e(x, F) for x in T[cuts[i]:cuts[i + 1]]] for i in range(5)}
    register(
        oa, n,
        materials=MATERIALS, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=tiers,
        context=[_e(ctx, F)],
        selfcheck=[_e(x, F) for x in sc],
        open_task=task(op[0].replace("{F}", F), *op[1:]),
        reinforce=reinforce, extend=extend,
    )
