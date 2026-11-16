"""Ayudante de los cuadernos de Educación Física y Salud 2 de 3.º y 4.º medio Formación General (student_content_fg_efs2_*).

No registra clases por sí mismo. Forma compacta de ejercicio:
  (q, a, why)                                      respuesta breve
  ("ab", stem, correcta, incorrecta, why)          dos opciones (el registro las balancea)
  ("abc", stem, correcta, mala1, mala2, why)       tres opciones
  ("=", q, expr, why[, unidad])                    respuesta calculada
«{F}» dentro del enunciado se reemplaza por la ficha de la clase.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

MATERIALS = ("Lápiz y papel. Todos los casos, fichas y datos están escritos en cada ejercicio (son inventados «de ejemplo» para este cuaderno); no necesitas video ni internet. "
             "Si tu docente organiza práctica, usa un espacio despejado, ropa y calzado cómodos, agua a mano y balones blandos o implementos livianos, sin cargas máximas, sin retener la respiración ni exigir el cuerpo al límite. "
             "Haz siempre un calentamiento general antes y un enfriamiento después, con pausas. Ante dolor, mareo o malestar, detente y avisa a una persona adulta. Nadie comenta ni compara los cuerpos de otras personas. "
             "La prueba del habla, la escala de esfuerzo de 1 a 10 con zona de 4 a 6, las duraciones y la referencia de una hora diaria de actividad son orientaciones generales de ejemplo, no indicaciones personales ni médicas.")


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _why(why):
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
        return ex(f"{stem} A) {good} B) {bad}".replace("{F}", ficha), f"A) {good}", _why(why))
    if kind == "abc":
        _, stem, good, b1, b2, why = item
        return ex(f"{stem} A) {good} B) {b1} C) {b2}".replace("{F}", ficha), f"A) {good}", _why(why))
    q, a, why = item
    return ex(q.replace("{F}", ficha), a, _why(why))


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
