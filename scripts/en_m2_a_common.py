"""Ayudas comunes de los cuadernos de Inglés (propuesta) de 2.º medio, módulos student_content_en_m2_a*.

Las «escuchas» las lee una persona adulta en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Todos los textos son originales, con pista en español.
"""
from __future__ import annotations

import re

import student_lessons as sl
from student_content_ma01_b import task  # noqa: F401  (se reexporta)
from student_lessons import arith, ex, register  # noqa: F401

ADULT = "Una persona adulta lee en voz alta (tapa el guion): "
MAT = "Los textos y guiones escritos en cada ejercicio (los guiones los lee una persona adulta en voz alta), una hoja para tapar el guion, lápiz y cuaderno."
MAT_READ = "Los textos escritos en cada ejercicio, lápiz, cuaderno y, si quieres, lápices de colores para subrayar."
MAT_SPEAK = "Los datos y textos escritos en cada ejercicio, lápiz, cuaderno y, si puedes, una persona de tu casa que escuche tus respuestas en voz alta."

_OPT = re.compile(r"(?:(?<=\s)|^)(\(?)([AaBbCc])(\)|\.)(?=\s)")


def _tidy(item):
    """Quita la puntuación final de las opciones A)/B)/C) para que el balanceo automático no duplique puntos."""
    q = item["q"]
    marks = list(_OPT.finditer(q))
    letters = [m.group(2).upper() for m in marks]
    if letters not in (["A", "B"], ["A", "B", "C"]) or sl._is_matching(q, str(item["a"])):
        return item
    parts = [q[:marks[0].start()]]
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(q)
        seg = re.sub(r"[\s.?!]+$", "", q[m.end():end].strip())
        parts.append(f"{m.group(1)}{m.group(2)}{m.group(3)} {seg}")
    item["q"] = "".join(parts[:1]) + " ".join(parts[1:])
    if re.match(r"^\(?[A-Ca-c][\).]\s", str(item["a"])):
        item["a"] = re.sub(r"[\s.?!]+$", "", item["a"])
    return item


def E(rows):
    return [_tidy(r if isinstance(r, dict) else ex(*r)) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )
