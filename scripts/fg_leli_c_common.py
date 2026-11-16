"""Ayuda de autoría para los módulos student_content_fg_leli_c* (Lengua y literatura, 4.º medio FG, OA 03 a 08).

P recibe los 13 ejercicios cerrados como tuplas (enunciado, respuesta, porqué) y los reparte 3/3/3/2/2.
"""
from __future__ import annotations

from fg_leli_common import E, L


def _items(rows):
    return [E(q, a, w) for q, a, w in rows]


def P(oa, n, use, prior, explain, vocab, worked, mistakes, ex, ctx, sc, ot, reinforce, extend):
    assert len(ex) == 13, (oa, n, len(ex))
    cuts = (0, 3, 6, 9, 11, 13)
    tiers = [_items(ex[cuts[i]:cuts[i + 1]]) for i in range(5)]
    L(oa, n, use, prior, explain, vocab, worked, mistakes, tiers, _items([ctx]), _items(sc), ot, reinforce, extend)
