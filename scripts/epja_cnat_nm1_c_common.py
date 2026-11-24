"""Ayudante de los cuadernos de Ciencias Naturales, EPJA Educación Media Nivel 1, módulo 3, desempeños 09 a 12 (student_content_epja_cnat_nm1_c*).

Uso: `from epja_cnat_nm1_c_common import K, OA`. Forma de los ejercicios (la de hc_common):
  ("ab", stem, correcta, incorrecta, why) · ("abc", stem, correcta, mala1, mala2, why) · ("=", q, expr, why[, unidad])
«{F}» dentro del enunciado se reemplaza por la ficha de la clase. Todo dato es de ejemplo e inventado: no se hace laboratorio ni experimento real.
Los textos de salud son información general y respetuosa: no reemplazan la consulta con un profesional del consultorio.
"""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. No se hace ningún experimento ni medición real: todo se resuelve con los datos, tablas y textos de ejemplo escritos en cada ficha, "
    "que son inventados para este cuaderno. No hace falta calculadora científica, internet ni materiales. Este cuaderno da información general sobre el cuerpo y la salud: "
    "no entrega diagnósticos ni indicaciones personales. Ante dudas sobre tu salud o la de alguien cercano, consulta en tu consultorio o centro de salud."
)
build = make_build(MATERIALS)

OA = {9: "EPJA-CNAT-NM1-OAD-09", 10: "EPJA-CNAT-NM1-OAD-10", 11: "EPJA-CNAT-NM1-OAD-11", 12: "EPJA-CNAT-NM1-OAD-12"}

PRIOR = [
    "Reconozco que el cuerpo está formado por sistemas que trabajan coordinados.",
    "Leo tablas simples y comparo números con unidades.",
]


def _mix(items, seed):
    """Rota la posición de la respuesta correcta (A, B o C) de forma determinista y equilibrada."""
    out = []
    for i, it in enumerate(items):
        if it[0] == "abc":
            _, stem, good, b1, b2, why = it
            p = (i + seed) % 3
            opts = [b1, b2]
            opts.insert(p, good)
            out.append((f"{stem} A) {opts[0]} B) {opts[1]} C) {opts[2]}", f"{'ABC'[p]}) {good}", why))
        else:
            out.append(it)
    return out


def K(oa, n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    """op = (consigna, ejemplo de respuesta, criterios, evidencia, retroalimentación); los errores son los frecuentes de la clase."""
    stmt, example, crit, ev, fb = op
    seed = oa + n
    T = _mix(T, seed)
    ctx = _mix([ctx], seed + 1)[0]
    build(OA[oa], n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc,
          op=(stmt, example, crit, ev, [m[0] for m in mistakes], fb), reinforce=rf, extend=ex_)
