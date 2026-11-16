"""Ayudante de los cuadernos de Artes Visuales de 3.º y 4.º medio Formación General (student_content_fg_arte_*).

No registra clases por sí mismo. Forma compacta de ejercicio:
  (q, a, why)                                  respuesta breve
  ("ab", stem, correcta, incorrecta, why)      dos opciones (el registro las balancea)
  ("abc", stem, correcta, mala1, mala2, why)   tres opciones
  ("=", q, expr, why[, unidad])                respuesta calculada
Las obras, artistas, medios y datos son de ejemplo, inventados para este cuaderno.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

MATERIALS = "Lápiz y papel; si quieres, lápices de colores, témpera y cartulina. Todas las obras, artistas y casos están descritos por escrito en cada ejercicio (son de ejemplo, inventados para este cuaderno); no necesitas imágenes ni internet. Si tu docente muestra obras reales, úsalas con las mismas preguntas."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _why(why):
    if len(why.split()) < 6:
        import sys
        print(f"WHY CORTO: {why!r}", file=sys.stderr)
    return why


def _e(item):
    kind = item[0]
    need = {"=": (4, 5), "ab": (5, 5), "abc": (6, 6)}.get(kind, (3, 3))
    assert need[0] <= len(item) <= need[1], f"ejercicio mal formado ({len(item)} campos): {str(item[1] if kind in need else item[0])[:80]}"
    if kind == "=":
        _, q, expr, why, *rest = item
        return arith(q, expr, why, rest[0] if rest else "")
    if kind == "ab":
        _, stem, good, bad, why = item
        return ex(f"{stem} A) {good} B) {bad}", f"A) {good}", _why(why))
    if kind == "abc":
        _, stem, good, b1, b2, why = item
        return ex(f"{stem} A) {good} B) {b1} C) {b2}", f"A) {good}", _why(why))
    q, a, why = item
    return ex(q, a, _why(why))


def build(oa, n, use, prior, explain, vocab, worked, mistakes, T, ctx, sc, op, reinforce, extend, materials=MATERIALS):
    """T: 13 ejercicios (3/3/3/2/2). worked: (título, problema, pasos, respuesta). mistakes: (error, causa, corrección)."""
    assert len(T) == 13, (oa, n, len(T))
    assert len(sc) == 3, (oa, n, len(sc))
    cuts = (0, 3, 6, 9, 11, 13)
    names = ("recovery", "understand", "apply", "reason", "challenge")
    tiers = {names[i]: [_e(x) for x in T[cuts[i]:cuts[i + 1]]] for i in range(5)}
    register(
        oa, n,
        materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=tiers,
        context=[_e(ctx)],
        selfcheck=[_e(x) for x in sc],
        open_task=task(*op),
        reinforce=reinforce, extend=extend,
    )
