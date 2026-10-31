"""Student material for 3.º básico Música, OA 05 (improvisar y crear con un propósito) y OA 06 (presentar el trabajo musical)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA5, OA6 = "MU03 OA 05", "MU03 OA 06"

TA, TT, TAA, SIL = "TA", "ti-ti", "TAA", "SIL"
LEY = "TA = 1 sonido en 1 pulso; ti-ti = 2 sonidos rápidos en 1 pulso; TAA = 1 sonido largo que dura 2 pulsos; SIL = 1 pulso de silencio"
_PULSOS = {TA: 1, TT: 1, TAA: 2, SIL: 1}
_SONIDOS = {TA: 1, TT: 2, TAA: 1, SIL: 0}


def P(*tokens: str) -> str:
    return " – ".join(tokens)


def pulses(*tokens: str) -> int:
    return sum(_PULSOS[t] for t in tokens)


def sounds(*tokens: str) -> int:
    return sum(_SONIDOS[t] for t in tokens)


def count_motif(seq: tuple, motif: tuple) -> int:
    n = len(motif)
    return sum(1 for i in range(len(seq) - n + 1) if seq[i:i + n] == motif)


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- OA 05 · clase 1
CONS = "Consigna: 4 pulsos, solo con TA y SIL, y con al menos un SIL"
IM = {
    "a": (TA, SIL, TA, TA),
    "b": (TA, TA, TA, TA),
    "c": (TA, TT, SIL, TA),
    "d": (SIL, TA, TA),
    "e": (SIL, TA, SIL, TA),
}


def cumple(x: tuple) -> bool:
    return pulses(*x) == 4 and set(x) <= {TA, SIL} and SIL in x


OK1 = [k for k, v in IM.items() if cumple(v)]
IM_TXT = " ".join(f"({k}) {P(*v)}." for k, v in IM.items())

L(
    OA5, 1,
    f"Lápiz y tus palmas. Leyenda: {LEY}. {CONS}. Propuestas de improvisación escritas: {IM_TXT}",
    "Aprenderé a improvisar dentro de una consigna: inventar música en el momento, pero cumpliendo reglas. Sirve para crear sin quedar paralizado y con un propósito.",
    ["Sé contar pulsos.", "Sé leer TA, ti-ti, TAA y SIL.", "Sé mantener un pulso con palmas."],
    [
        "Improvisar es inventar música en el momento, sin haberla preparado. No significa tocar cualquier cosa. Una improvisación tiene una consigna: reglas que dicen qué se puede usar y cuánto debe durar. La consigna le da un propósito y ayuda a decidir.",
        f"Veamos una consigna: «{CONS}». Una improvisación que la cumple es {P(*IM['a'])}: dura 4 pulsos, usa solo TA y SIL, y tiene un SIL. En cambio {P(*IM['b'])} no tiene ningún silencio, y {P(*IM['c'])} usa un ti-ti, que la consigna no permite.",
        "Mientras improvisas, mantén el pulso parejo con el pie. Si te equivocas, sigue y ajusta en la siguiente vuelta: improvisar no es tocar perfecto, es decidir sobre la marcha. Después revisa si tu improvisación cumplió cada regla de la consigna, una por una. Puedes improvisar con distintos medios sonoros: tus palmas, la voz, objetos seguros o un instrumento.",
    ],
    [("improvisar", "inventar música en el momento"), ("consigna", "reglas que dicen qué usar y cuánto dura"), ("propósito", "para qué se hace la música"), ("cumplir", "respetar todas las reglas de la consigna"), ("pulso", "latido parejo que se mantiene")],
    [
        ("Revisar una improvisación", f"{CONS}. Improvisación: {P(*IM['a'])}. ¿Cumple la consigna?", ["Cuento los pulsos: 1 + 1 + 1 + 1 = 4.", "Solo usa TA y SIL.", "Tiene un SIL."], "Sí, cumple"),
        ("Encontrar la regla que falla", f"{CONS}. Improvisación: {P(*IM['c'])}. ¿Qué regla no cumple?", ["Duración: TA, ti-ti, SIL, TA son 4 pulsos, está bien.", "Usa ti-ti, y la consigna solo permite TA y SIL."], "Usa ti-ti, que la consigna no permite"),
    ],
    [
        ("Tocar cualquier cosa y decir que es improvisación.", "Una improvisación debe seguir la consigna.", "Revisa cada regla antes de decir que cumple."),
        ("Parar cuando te equivocas.", "Improvisar es decidir sobre la marcha.", "Sigue con el pulso y ajusta en la vuelta siguiente."),
    ],
    [
        ex(f"{CONS}. Improvisación {P(*IM['b'])}. ¿Cumple la consigna?", "No", "No tiene ningún SIL."),
        ex("¿Improvisar es inventar música en el momento o repetir una música aprendida?", "Inventar música en el momento", "Improvisar significa decidir al tocar."),
        ex(f"¿Cuántos pulsos tiene {P(*IM['e'])}?", str(pulses(*IM["e"])), "Cada símbolo ocupa un pulso."),
    ],
    [
        ex(f"{CONS}. Improvisación {P(*IM['d'])}. ¿Qué regla no cumple?", "No dura 4 pulsos", "Tiene 3 pulsos, uno menos."),
        ex(f"{CONS}. Improvisación {P(*IM['e'])}. ¿Cumple?", "Sí", "Dura 4 pulsos, usa solo TA y SIL y tiene dos SIL."),
        ex(f"{CONS}. Propuestas: {IM_TXT} ¿Cuáles cumplen la consigna? Escribe las letras.", " y ".join(OK1), "Solo (a) y (e) cumplen las tres reglas."),
    ],
    [
        ex(f"{CONS}. ¿Cuántas propuestas de {IM_TXT} cumplen la consigna?", str(len(OK1)), "Cumplen la (a) y la (e)."),
        ex(f"Propuestas: {IM_TXT} ¿Cuál es la única que usa un ti-ti?", "La (c)", "Solo la (c) tiene un ti-ti."),
        arith("En las propuestas (a) y (e) de la lista, ¿cuántos TA hay en total?", "3+2", "La (a) tiene 3 TA y la (e) tiene 2 TA.", " TA"),
    ],
    [
        ex("Ana improvisa sin parar y toca 10 pulsos cuando la consigna pedía 4. ¿Qué debe hacer la próxima vez?", "Contar los pulsos y parar en 4", "La consigna dice cuánto debe durar."),
        ex("Dos niños tienen la misma consigna y tocan improvisaciones distintas. ¿Es posible que las dos cumplan la consigna?", "Sí", "Una consigna permite varias improvisaciones distintas."),
    ],
    [
        ex("Con la consigna «4 pulsos, solo TA y SIL, con al menos un SIL», ¿cuál improvisación cumple: (a) TA – SIL – SIL – TA, (b) TAA – TA – SIL?", "(a)", "La (b) usa TAA, que la consigna no permite."),
        arith("Una consigna pide improvisar 8 pulsos con SIL en exactamente 2 de ellos. ¿En cuántos pulsos suena algo?", "8-2", "A los 8 pulsos se les quitan los 2 silenciosos.", " pulsos"),
    ],
    [ex("Para el rato de música del curso, la profesora pide una improvisación de 4 pulsos con solo palmas y silencios. ¿Qué debe revisar un estudiante antes de mostrarla?", "Que dura 4 pulsos y solo usa palmas y silencios", "Cada regla de la consigna se revisa.")],
    [ex("En Música: ¿Qué es improvisar?", "Inventar música en el momento", "No se prepara antes."), ex("¿Qué dice una consigna?", "Qué usar y cuánto dura", "Son las reglas de la improvisación."), ex("¿Para qué sirve revisar una improvisación con la consigna?", "Para comprobar que cumple cada regla", "La consigna dice qué reglas revisar.")],
    (
        f"Con la consigna «{CONS}», inventa tres improvisaciones distintas, escríbelas con la leyenda y tócalas con palmas a pulso parejo. Revisa cada una con la lista: ¿dura 4 pulsos?, ¿usa solo TA y SIL?, ¿tiene al menos un SIL? Marca con ✓ o ✗. Después repite una de ellas con otro medio sonoro (por ejemplo, golpeando suavemente una caja con la mano) y di qué cambió en el sonido.",
        f"1) {P(TA, SIL, TA, TA)} ✓✓✓. 2) {P(SIL, SIL, TA, TA)} ✓✓✓. 3) {P(TA, TA, SIL, TA)} ✓✓✓.",
        ["escribe tres improvisaciones distintas", "las revisa con las tres reglas", "toca con pulso parejo"],
        ["escritura", "interpretación con palmas"],
        ["olvidar el silencio", "pasarse de 4 pulsos"],
        "Reconoce la revisión regla por regla; si una falla, pide que explique cuál y la corrija.",
    ),
    "Improvisa con las palmas 4 pulsos con un solo silencio y cuéntale a una persona de tu casa qué regla seguiste.",
    "Inventa tu propia consigna de 3 reglas y escribe una improvisación que la cumpla.",
)

# ---------------------------------------------------------------- OA 05 · clase 2
MOT = (TA, TA, TT)
SEQ1 = (TA, TA, TT, SIL, TA, TA, TT, TAA, TA, TA, TT)
SEQ2 = (TA, TA, TA, TT, SIL, TAA, TA, TA, TT, TA)

L(
    OA5, 2,
    f"Lápiz y palmas. Leyenda: {LEY}. Motivo de trabajo: {P(*MOT)}.",
    "Aprenderé a crear un motivo reconocible: una idea musical corta que se puede repetir y reconocer. Sirve para que una pieza tenga identidad.",
    ["Sé improvisar con una consigna.", "Sé contar pulsos.", "Sé qué es repetir y contrastar."],
    [
        f"Un motivo es una idea musical muy corta, de pocos pulsos, que se repite en una pieza. Se reconoce porque siempre tiene la misma forma. Por ejemplo, el motivo {P(*MOT)} tiene {pulses(*MOT)} pulsos y {sounds(*MOT)} sonidos. Cuando lo oyes de nuevo, dices «ese es mi motivo».",
        f"Un motivo bueno es corto, fácil de recordar y distinto de lo que hay a su alrededor. Si lo repites, la gente lo reconoce. Veamos una secuencia: {P(*SEQ1)}. Allí el motivo aparece {count_motif(SEQ1, MOT)} veces, separado por otros sonidos.",
        "Para crear tu motivo, elige 3 o 4 símbolos de la leyenda y ordénalos. Tócalo varias veces hasta que lo recuerdes sin mirar. Después puedes ponerlo en una pieza entre otros sonidos. Si todo suena distinto, el motivo no se reconoce; si todo suena igual, no hay contraste.",
    ],
    [("motivo", "idea musical corta que se repite y se reconoce"), ("identidad", "lo que hace que algo se reconozca como el mismo"), ("reconocer", "darse cuenta de que algo ya sonó antes"), ("crear", "hacer una idea nueva y trabajarla"), ("secuencia", "serie de símbolos en orden")],
    [
        ("Contar un motivo", f"Motivo: {P(*MOT)}. Secuencia: {P(*SEQ1)}. ¿Cuántas veces aparece el motivo completo?", ["Busco TA – TA – ti-ti seguidos.", "Aparece al comienzo, después del primer SIL y al final."], f"{count_motif(SEQ1, MOT)} veces"),
        ("Pulsos de un motivo", f"¿Cuántos pulsos tiene el motivo {P(*MOT)}?", ["TA 1, TA 1, ti-ti 1.", "1 + 1 + 1 = 3."], f"{pulses(*MOT)} pulsos"),
    ],
    [
        ("Crear un motivo tan largo que no se recuerda.", "Un motivo es una idea corta.", "Usa de 3 a 4 símbolos."),
        ("Cambiar el motivo cada vez que aparece.", "Si cambia, ya no se reconoce.", "Mantén los mismos símbolos en el mismo orden."),
    ],
    [
        ex(f"Motivo: {P(*MOT)}. ¿Cuántos sonidos tiene?", str(sounds(*MOT)), "TA 1, TA 1 y ti-ti 2."),
        ex("¿Un motivo es una idea larga o una idea corta?", "Una idea corta", "El motivo es breve para poder recordarse."),
        ex(f"Motivo: {P(*MOT)}. En {P(TA, TA, TT, SIL)}, ¿aparece el motivo?", "Sí", "Los tres primeros símbolos son el motivo."),
    ],
    [
        ex(f"Motivo: {P(*MOT)}. Secuencia: {P(*SEQ2)}. ¿Cuántas veces aparece el motivo completo?", str(count_motif(SEQ2, MOT)), "Aparece en los símbolos 2 a 4 y en los símbolos 7 a 9."),
        ex(f"Secuencia: {P(*SEQ2)}. ¿Cuántos pulsos tiene?", str(pulses(*SEQ2)), "TA 1, TA 1, TA 1, ti-ti 1, SIL 1, TAA 2, TA 1, TA 1, ti-ti 1 y TA 1."),
        ex("Un niño toca TA – TA – ti-ti, luego TA – TA – ti-ti y luego TA – TA – ti-ti. ¿Qué hace con su motivo?", "Lo repite", "Lo toca igual tres veces."),
    ],
    [
        ex(f"Motivo: {P(*MOT)}. Secuencia: {P(*SEQ1)}. ¿Cuántos pulsos hay entre el final de la primera aparición y el comienzo de la segunda?", "1", "Entre ellas solo hay un SIL, que ocupa un pulso."),
        arith(f"El motivo {P(*MOT)} se toca 4 veces seguidas. ¿Cuántos sonidos se tocan en total?", f"{sounds(*MOT)}*4", "Cada motivo tiene 4 sonidos y se repite 4 veces.", " sonidos"),
        ex("Quieres que tu motivo se reconozca. ¿Qué te sirve más: (a) cambiarlo cada vez o (b) repetirlo igual entre otros sonidos?", "(b)", "Lo que se repite igual se reconoce."),
    ],
    [
        ex(f"Ana dice que {P(TA, TT, TA)} es el mismo motivo que {P(*MOT)}. ¿Tiene razón?", "No", "Los símbolos y el orden son distintos."),
        ex("Un motivo de 3 pulsos aparece 5 veces en una pieza de 20 pulsos. ¿Cuántos pulsos de la pieza son de otros sonidos?", "5", "5 apariciones × 3 pulsos = 15; 20 − 15 = 5."),
    ],
    [
        arith("Un motivo de 3 pulsos se repite 4 veces con un SIL entre cada aparición. ¿Cuántos pulsos hay en total?", "3*4+3", "Hay 12 pulsos de motivo y 3 silencios entre las 4 apariciones.", " pulsos"),
        ex(f"Escribe un motivo de exactamente 3 pulsos con un TA, un ti-ti y un SIL, en este orden: TA primero, SIL al final.", P(TA, TT, SIL), "Va TA, luego ti-ti y SIL al final."),
    ],
    [ex("En una pieza para el curso, el motivo se toca al comienzo, en el medio y al final. ¿Para qué sirve eso?", "Para que el público lo reconozca", "La repetición ayuda a reconocer la idea.")],
    [ex("¿Qué es un motivo?", "Una idea musical corta que se repite", "Se reconoce porque vuelve igual."), ex("¿Cuántos símbolos conviene que tenga un motivo?", "3 o 4", "Así es corto y fácil de recordar."), ex("¿Qué pasa si el motivo cambia cada vez?", "No se reconoce", "Pierde su identidad.")],
    (
        "Crea un motivo de 3 o 4 símbolos con la leyenda. Escríbelo, calcula sus pulsos y sus sonidos. Después arma una secuencia de 10 símbolos en que tu motivo aparezca exactamente 2 veces, separado por otros sonidos. Márcalo con un círculo y cuenta las apariciones.",
        f"Motivo: {P(TA, TT, TAA)} (4 pulsos y 4 sonidos). Secuencia: {P(TA, TT, TAA, SIL, TA, TA, TA, TT, TAA, SIL)}. El motivo aparece 2 veces.",
        ["crea un motivo corto", "calcula sus pulsos y sonidos", "lo ubica 2 veces en una secuencia"],
        ["escritura", "interpretación con palmas"],
        ["hacer el motivo demasiado largo", "cambiarlo en la segunda aparición"],
        "Reconoce el motivo claro y pide que lo toque dos veces para comprobar que es igual.",
    ),
    "Toca tu motivo tres veces y pregunta a una persona de tu casa si lo reconoce.",
    "Crea un motivo y escribe una secuencia donde aparezca 3 veces.",
)

# ---------------------------------------------------------------- OA 05 · clase 3
VER = {
    "1": (MOT, "suave", "moderado"),
    "2": (MOT, "fuerte", "moderado"),
    "3": (MOT, "suave", "rápido"),
    "4": ((TAA, TAA, SIL), "suave", "moderado"),
}
VER_TXT = " ".join(f"Versión {k}: ritmo {P(*r)}, {i}, {t}." for k, (r, i, t) in VER.items())


def cambian(a: str, b: str) -> list[str]:
    ra, ia, ta = VER[a]
    rb, ib, tb = VER[b]
    out = []
    if ra != rb:
        out.append("ritmo")
    if ia != ib:
        out.append("intensidad")
    if ta != tb:
        out.append("tempo")
    return out


L(
    OA5, 3,
    f"Lápiz y palmas. Leyenda: {LEY}. Versiones de trabajo del motivo: {VER_TXT}",
    "Aprenderé a variar una cualidad de un motivo conservando su identidad. Sirve para que una pieza no aburra, pero siga reconociéndose.",
    ["Sé qué es un motivo.", "Sé qué es la variación.", "Sé qué son intensidad y tempo."],
    [
        f"Variar un motivo es cambiar algo de él sin que deje de reconocerse. Para conservar la identidad, cambia solo una cualidad a la vez. Puedes cambiar la intensidad (suave o fuerte), el tempo (lento o rápido), la altura (aguda o grave) o la duración. El ritmo del motivo, {P(*MOT)}, se mantiene. Ojo: en la clase de repetición, contraste y variación cambiábamos un símbolo del ritmo; aquí, para variar el motivo, conservamos su ritmo y cambiamos otra cualidad.",
        f"Mira las versiones: {VER_TXT} Entre la 1 y la 2 cambia solo {', '.join(cambian('1', '2'))}. Entre la 1 y la 3 cambia solo {', '.join(cambian('1', '3'))}. Entre la 1 y la 4 cambia el ritmo, y ahí se pierde la identidad: ya no es el mismo motivo.",
        "Antes de cambiar, di qué cualidad cambiarás y cómo esperas que suene. Después tócalo y comprueba si se reconoce. Si cambias dos o tres cualidades a la vez, es más difícil reconocer el motivo. Cambiar una sola es una variación; cambiar todo es un contraste.",
    ],
    [("variar", "cambiar algo conservando la identidad"), ("cualidad", "altura, intensidad, tempo o duración"), ("identidad", "lo que hace reconocible al motivo"), ("versión", "forma en que se toca el motivo"), ("conservar", "mantener sin cambios")],
    [
        ("Detectar el cambio", f"{VER_TXT} ¿Qué cualidad cambia entre la versión 1 y la versión 2?", ["El ritmo es el mismo.", "El tempo es el mismo: moderado.", "La intensidad pasa de suave a fuerte."], "La intensidad"),
        ("Decidir si conserva la identidad", f"{VER_TXT} ¿La versión 4 conserva la identidad del motivo?", ["El ritmo de la versión 4 es TAA – TAA – SIL.", "Es distinto de TA – TA – ti-ti."], "No, porque cambió el ritmo"),
    ],
    [
        ("Cambiar el ritmo y decir que es una variación.", "Si cambia el ritmo, el motivo ya no es el mismo.", "Cambia intensidad o tempo y conserva el ritmo."),
        ("Cambiar tres cualidades a la vez.", "Cuesta reconocer el motivo.", "Cambia una cualidad por vez."),
    ],
    [
        ex(f"{VER_TXT} ¿Qué cualidad cambia entre la versión 1 y la versión 3?", "El tempo", "El ritmo y la intensidad son iguales; pasa de moderado a rápido."),
        ex("Si cambias solo la intensidad de un motivo, ¿conserva su identidad?", "Sí", "El ritmo sigue siendo el mismo."),
        ex(f"{VER_TXT} ¿Cuántas de las versiones 1, 2 y 3 tienen el ritmo {P(*MOT)}?", "3", "Las tres conservan el ritmo."),
    ],
    [
        ex(f"{VER_TXT} ¿Cuántas cualidades cambian entre la versión 1 y la versión 4?", str(len(cambian("1", "4"))), "Solo cambia el ritmo."),
        ex(f"{VER_TXT} ¿Cuántas cualidades cambian entre la versión 2 y la versión 3?", str(len(cambian("2", "3"))), "Cambian la intensidad y el tempo."),
        ex("Tocas el motivo suave y luego lo tocas igual, pero fuerte. ¿Qué cualidad variaste?", "La intensidad", "El ritmo y el tempo no cambiaron."),
    ],
    [
        ex(f"{VER_TXT} Quieres una versión nueva que cambie la intensidad y el tempo de la versión 1 y conserve el ritmo. ¿Cómo debe ser: (a) fuerte y rápida, (b) fuerte y moderada?", "(a)", "La versión 1 es suave y moderada; (a) cambia las dos cualidades y (b) solo la intensidad."),
        arith("Tocas el motivo de 3 pulsos en 4 versiones distintas seguidas. ¿Cuántos pulsos tocas?", "3*4", "Son 4 versiones de 3 pulsos.", " pulsos"),
    ],
    [
        ex("Pedro dice: «cambié el ritmo del motivo, pero sigue siendo el mismo motivo». ¿Tiene razón?", "No", "Si el ritmo cambia, el motivo cambia."),
        ex("Quieres variar un motivo sin perder su identidad. ¿Cambias una cualidad o las tres a la vez?", "Una cualidad", "Cambiar tres a la vez dificulta reconocerlo."),
    ],
    [
        ex(f"{VER_TXT} ¿Cuántas de las versiones 2, 3 y 4 conservan la identidad del motivo de la versión 1?", "2", "La 2 y la 3 conservan el ritmo; la 4 lo cambia."),
        ex("Escribe en orden las tres versiones del motivo: suave y lenta, suave y rápida, fuerte y rápida. ¿Cuántas cualidades cambian de la primera a la última?", "2", "Cambian el tempo y la intensidad."),
    ],
    [ex("En una pieza para bailar, el motivo suena primero lento y suave, después rápido y suave. ¿Qué cualidad cambió y qué se conservó?", "Cambió el tempo; se conservó el ritmo y la intensidad", "Pasó de lento a rápido y sigue siendo suave con el mismo ritmo.")],
    [ex("¿Qué es variar un motivo?", "Cambiar algo conservando su identidad", "El motivo debe seguir reconociéndose."), ex("¿Qué se mantiene al variar un motivo?", "El ritmo", "Si cambia, ya es otro motivo."), ex("¿Cuántas cualidades conviene cambiar a la vez?", "Una", "Así la identidad se conserva.")],
    (
        f"Toma el motivo {P(*MOT)}. Tócalo con las palmas en tres versiones: (1) suave y a tempo moderado; (2) igual, pero fuerte; (3) igual que la primera, pero a tempo rápido. Escribe qué cualidad cambió en cada paso y cuál se conservó. Después toca una cuarta versión que cambie el ritmo y explica por qué ya no es el mismo motivo.",
        "Versión 2 cambia la intensidad. Versión 3 cambia el tempo. En ambas se conserva el ritmo. La versión 4 cambia el ritmo (por ejemplo TAA – TAA – SIL) y por eso ya no se reconoce como el mismo motivo.",
        ["toca las tres versiones con el ritmo igual", "nombra la cualidad que cambió", "explica por qué la cuarta pierde la identidad"],
        ["interpretación con palmas", "explicación escrita"],
        ["cambiar dos cualidades en un paso", "no conservar el ritmo"],
        "Reconoce que el ritmo se conserva y pregunta qué cambió en cada paso.",
    ),
    "Toca un motivo suave y luego fuerte, con el mismo ritmo.",
    "Haz tres versiones del mismo motivo cambiando una cualidad distinta en cada una.",
)

# ---------------------------------------------------------------- OA 05 · clase 4
QA_Q = (TA, TA, TT, TA)
QA_REGLAS = "Reglas de pregunta y respuesta de esta clase: las dos frases duran 4 pulsos; la respuesta empieza igual que la pregunta (sus 2 primeros símbolos); la respuesta termina en TAA (sonido largo)"
QA_R = {
    "r1": (TA, TA, TAA),
    "r2": (TA, TA, TA, TA),
    "r3": (TT, TA, TAA),
    "r4": (TA, TA, TAA, SIL),
}


def resp_ok(q, r):
    return pulses(*r) == 4 and r[:2] == q[:2] and r[-1] == TAA


OK4 = [k for k, v in QA_R.items() if resp_ok(QA_Q, v)]
QA_TXT = " ".join(f"{k}: {P(*v)}." for k, v in QA_R.items())

L(
    OA5, 4,
    f"Lápiz y palmas. Leyenda: {LEY}. {QA_REGLAS}. Pregunta de trabajo: {P(*QA_Q)}.",
    "Aprenderé a organizar una pregunta y una respuesta musical. Sirve para armar pequeñas conversaciones musicales entre dos personas.",
    ["Sé qué es una frase.", "Sé qué es variar.", "Sé contar pulsos."],
    [
        "En una pregunta y respuesta musical, la primera frase queda como «abierta», como si preguntara. La segunda frase responde: se parece a la primera y termina de manera que se siente cerrada. Dos personas pueden hacerlo: una toca la pregunta y la otra responde.",
        f"{QA_REGLAS}. Pregunta de trabajo: {P(*QA_Q)}, que dura {pulses(*QA_Q)} pulsos. Una respuesta posible es {P(*QA_R['r1'])}: dura {pulses(*QA_R['r1'])} pulsos, empieza igual (TA – TA) y termina en TAA. En cambio {P(*QA_R['r2'])} no termina en TAA, y {P(*QA_R['r3'])} empieza distinto.",
        "Cuando improvises una respuesta, escucha primero la pregunta, mantén el pulso y respeta el silencio entre las dos frases. La respuesta es una variación de la pregunta: conserva el comienzo y cambia el final. Esa es una forma sencilla de crear una conversación musical.",
    ],
    [("pregunta musical", "frase que queda abierta, como esperando respuesta"), ("respuesta musical", "frase que contesta y cierra"), ("cierre", "final que se siente terminado"), ("conversación musical", "turnos entre dos personas que se contestan"), ("turno", "momento en que le toca tocar a una persona")],
    [
        ("Revisar una respuesta", f"{QA_REGLAS}. Pregunta: {P(*QA_Q)}. Respuesta: {P(*QA_R['r1'])}. ¿Cumple las reglas?", ["Dura 1 + 1 + 2 = 4 pulsos.", "Empieza con TA – TA, como la pregunta.", "Termina en TAA."], "Sí, cumple las tres reglas"),
        ("Encontrar la regla que falla", f"{QA_REGLAS}. Pregunta: {P(*QA_Q)}. Respuesta: {P(*QA_R['r3'])}. ¿Qué regla no cumple?", ["Dura 4 pulsos y termina en TAA.", "Empieza con ti-ti – TA, distinto de TA – TA."], "No empieza igual que la pregunta"),
    ],
    [
        ("Responder con una frase que no se parece a la pregunta.", "La respuesta es una variación de la pregunta.", "Mantén el comienzo y cambia el final."),
        ("Tocar la respuesta sin esperar al terminar la pregunta.", "Se rompe el turno.", "Espera tu turno y mantén el pulso."),
    ],
    [
        ex(f"{QA_REGLAS}. ¿Con qué símbolo termina la respuesta?", "TAA", "La tercera regla dice que termina en TAA."),
        ex(f"Pregunta: {P(*QA_Q)}. ¿Cuántos pulsos dura?", str(pulses(*QA_Q)), "TA 1, TA 1, ti-ti 1, TA 1."),
        ex(f"{QA_REGLAS}. Respuesta: {P(*QA_R['r2'])}. ¿Cumple las reglas?", "No", "No termina en TAA."),
    ],
    [
        ex(f"{QA_REGLAS}. Pregunta: {P(*QA_Q)}. Respuestas: {QA_TXT} ¿Cuáles cumplen las reglas? Escribe los nombres.", " y ".join(OK4), "Solo r1 cumple las tres reglas."),
        ex(f"Respuesta r4: {P(*QA_R['r4'])}. ¿Cuántos pulsos dura?", str(pulses(*QA_R["r4"])), "TA 1, TA 1, TAA 2, SIL 1."),
        ex(f"{QA_REGLAS}. ¿Qué regla no cumple r4: {P(*QA_R['r4'])}? Pregunta: {P(*QA_Q)}.", "Dura 5 pulsos y no termina en TAA", "Termina en SIL y suma 5 pulsos."),
    ],
    [
        ex("Dos personas se turnan: una toca la pregunta (4 pulsos), la otra responde (4 pulsos). Si repiten 3 veces, ¿cuántos pulsos tocan entre las dos?", "24", "Cada vuelta tiene 8 pulsos, y son 3 vueltas."),
        arith("En una conversación musical, hay 5 preguntas y 5 respuestas de 4 pulsos cada una. ¿Cuántos pulsos hay en total?", "5*4+5*4", "Se suman 20 pulsos de preguntas y 20 de respuestas.", " pulsos"),
        ex("Una pregunta termina con un sonido corto. La respuesta termina con un sonido largo. ¿Cuál de las dos suena más cerrada?", "La respuesta", "En las reglas de esta clase, la respuesta termina en un sonido largo, que da sensación de cierre."),
    ],
    [
        ex("Luis dice que da lo mismo cambiar el comienzo o el final de la respuesta. ¿Tiene razón según las reglas de esta clase?", "No", "El comienzo se conserva y el final cambia."),
        ex("Una pregunta tiene 6 pulsos. Quieres una respuesta de la misma duración que termine en TAA. ¿Cuántos pulsos ocupa el TAA?", "2", "TAA dura 2 pulsos."),
    ],
    [
        ex(f"Escribe una respuesta que cumpla las reglas para la pregunta {P(TA, TT, TA, TA)}. La respuesta debe dar 4 pulsos, empezar con TA – ti-ti y terminar en TAA.", P(TA, TT, TAA), "TA 1, ti-ti 1 y TAA 2 suman 4 pulsos."),
        arith("Una conversación musical tiene 6 turnos de 4 pulsos cada uno. ¿Cuántos pulsos dura?", "6*4", "Hay 6 turnos de 4 pulsos.", " pulsos"),
    ],
    [ex("En el recreo, dos amigos juegan a contestarse con palmas. Uno hace 4 palmas y el otro responde con 4 palmas parecidas. ¿Qué tipo de organización musical juegan?", "Pregunta y respuesta", "Una frase contesta a la otra.")],
    [ex("¿La respuesta es igual a la pregunta o una variación?", "Una variación", "Conserva el comienzo."), ex("¿Cuánto dura TAA?", "2 pulsos", "Es un sonido largo."), ex("¿Qué haces mientras la otra persona toca?", "Escuchas y esperas tu turno", "Así la conversación musical funciona.")],
    (
        f"Con una persona de tu casa (o tú solo, tocando con dos manos), inventa una pregunta de 4 pulsos con la leyenda y una respuesta que cumpla las reglas: {QA_REGLAS}. Escribe ambas, tócalas con palmas y marca con ✓ cada regla que cumple la respuesta.",
        f"Pregunta: {P(TA, TT, TA, TA)}. Respuesta: {P(TA, TT, TAA)}. Dura 4 pulsos ✓, empieza igual ✓ y termina en TAA ✓.",
        ["escribe pregunta y respuesta de 4 pulsos", "la respuesta cumple las tres reglas", "toca con turnos y pulso parejo"],
        ["escritura", "interpretación con palmas"],
        ["no esperar el turno", "olvidar terminar en TAA"],
        "Reconoce la respuesta con la revisión regla por regla y pregunta cómo suena el cierre.",
    ),
    "Haz una pregunta con 4 palmadas y pide a una persona de tu casa que te responda con 4 parecidas.",
    "Crea dos parejas distintas de pregunta y respuesta y escribe sus pulsos.",
)

# ---------------------------------------------------------------- OA 05 · clase 5
A_PART = (TA, TA, TT, TA)
B_PART = (TAA, SIL, TA)
BORR = {
    "borrador 1": (A_PART, B_PART, A_PART),
    "borrador 2": (A_PART, (TAA, TAA, SIL), (TA, TA, TT, TA)),
    "borrador 3": ((TA, TA, TT, TA), (TAA, SIL, TAA, TA), (TA, TA, TT, TA)),
}
LISTA = "Lista de revisión: (1) forma ABA, con la A repetida igual; (2) cada sección dura 4 pulsos; (3) la B es distinta de la A"


def revisar(b):
    a1, bb, a2 = b
    return (a1 == a2, all(pulses(*x) == 4 for x in b), bb != a1)


BORR_TXT = " ".join(f"{k}: A = {P(*v[0])}; B = {P(*v[1])}; A = {P(*v[2])}." for k, v in BORR.items())

L(
    OA5, 5,
    f"Lápiz y palmas. Leyenda: {LEY}. {LISTA}. Borradores escritos: {BORR_TXT}",
    "Aprenderé a construir y revisar una pieza breve en forma ABA con un propósito. Sirve para terminar una creación comprobando que cumple lo que pedía.",
    ["Sé crear un motivo.", "Sé qué es la forma ABA.", "Sé revisar con una lista."],
    [
        "Una pieza breve se construye en pasos: primero el propósito (¿para qué es?), luego las secciones y por último la revisión. Una forma ABA tiene una sección A, una B distinta y vuelve la A. Si cada sección dura 4 pulsos, la pieza dura 12 pulsos.",
        f"Para revisar usamos una lista. {LISTA}. Aplicamos la lista al borrador 1: A = {P(*A_PART)} (4 pulsos), B = {P(*B_PART)} ({pulses(*B_PART)} pulsos), vuelve A igual. Cumple las tres condiciones. Un borrador revisado se corrige solo donde falla, sin rehacer todo.",
        "Revisar es parte de crear. Después de tocar la pieza, pregunta qué condición no se cumple, corrige solo esa parte y vuelve a tocar. Así la pieza mejora con evidencia. Al final escribe cuántos pulsos dura y cuál es su propósito, por ejemplo «para empezar un juego». Puedes tocar la pieza con distintos medios sonoros: palmas, voz, objetos seguros o un instrumento.",
    ],
    [("pieza", "obra musical breve"), ("revisar", "comprobar con una lista si algo cumple"), ("sección", "parte de la pieza"), ("propósito", "para qué se hace la pieza"), ("borrador", "primera versión que se puede mejorar")],
    [
        ("Revisar con la lista", f"{LISTA}. Borrador 1: A = {P(*BORR['borrador 1'][0])}; B = {P(*BORR['borrador 1'][1])}; A = {P(*BORR['borrador 1'][2])}. ¿Cumple las tres condiciones?", ["La A vuelve igual: 1.", "Cada sección dura 4 pulsos: 4, 4 y 4.", "La B es distinta de la A: 3."], "Sí, cumple las tres"),
        ("Calcular la duración", "Una pieza ABA tiene tres secciones de 4 pulsos. ¿Cuántos pulsos dura?", ["Cada sección dura 4 pulsos.", "4 + 4 + 4 = 12."], "12 pulsos"),
    ],
    [
        ("Corregir toda la pieza cuando falla una sola condición.", "Se pierde lo que ya estaba bien.", "Corrige solo la condición que falla."),
        ("No revisar la pieza con la lista.", "No sabes si cumple lo pedido.", "Aplica las tres condiciones una por una."),
    ],
    [
        ex(f"{LISTA}. Borrador 1: A = {P(*A_PART)}; B = {P(*B_PART)}; A = {P(*A_PART)}. ¿Cuántos pulsos tiene la sección B?", str(pulses(*B_PART)), "TAA 2, SIL 1 y TA 1."),
        ex("¿Qué forma tiene una pieza con una sección A, una B y otra vez la A?", "ABA", "La A vuelve al final."),
        ex("¿Revisar es parte de crear?", "Sí", "Se mejora una pieza comprobándola."),
    ],
    [
        ex(f"{LISTA}. {BORR_TXT} ¿Qué condición no cumple el borrador 2?", "Que la sección B dura 5 pulsos y no 4", "La B (TAA – TAA – SIL) suma 2 + 2 + 1 = 5 pulsos; las otras condiciones sí se cumplen."),
        ex(f"{LISTA}. Borrador 3: A = {P(*BORR['borrador 3'][0])}; B = {P(*BORR['borrador 3'][1])}; A = {P(*BORR['borrador 3'][2])}. ¿Cuántos pulsos tiene la B?", str(pulses(*BORR["borrador 3"][1])), "TAA 2, SIL 1, TAA 2 y TA 1."),
        ex("¿Cuántas condiciones tiene la lista de revisión de esta clase?", "3", "La lista tiene tres condiciones numeradas."),
    ],
    [
        ex(f"{LISTA}. {BORR_TXT} ¿Cuál borrador cumple las tres condiciones?", "El borrador 1", "El 2 tiene una B de 5 pulsos y el 3 tiene una B de 6 pulsos."),
        arith("Una pieza ABA tiene secciones de 4, 4 y 4 pulsos. Si la tocas 2 veces seguidas, ¿cuántos pulsos tocas?", "(4+4+4)*2", "La pieza dura 12 pulsos y se repite 2 veces.", " pulsos"),
        ex("Un borrador falla solo en la duración de la B. ¿Corriges toda la pieza o solo la B?", "Solo la B", "Se corrige únicamente lo que falla."),
    ],
    [
        ex("Ana dice que una pieza ABA con la misma A al principio y al final cumple la forma, aunque la B sea igual a la A. ¿Tiene razón?", "No", "La B debe ser distinta de la A."),
        ex("Una pieza ABA tiene A de 4 pulsos, B de 4 pulsos y A de 4 pulsos, y tú la tocas a 1 pulso por segundo. ¿Cuántos segundos dura?", "12", "12 pulsos a un pulso por segundo son 12 segundos."),
    ],
    [
        arith("Una pieza ABA tiene secciones de 4, 6 y 4 pulsos. Quieres que todas duren 4 pulsos. ¿Cuántos pulsos debes quitar a la B?", "6-4", "La B tiene 6 y debe quedar en 4.", " pulsos"),
        ex(f"Corrige el borrador 2: la sección B es {P(TAA, TAA, SIL)} (5 pulsos). Escribe una B de 4 pulsos con TAA y TA.", P(TAA, TA, TA), "TAA 2 + TA 1 + TA 1 suman 4 pulsos."),
    ],
    [ex("Para abrir un juego en el patio, el curso crea una pieza ABA de 12 pulsos. Si la tocan 3 veces, ¿cuántos pulsos suenan?", "36", "12 pulsos por 3 veces.")],
    [ex("¿Qué se revisa en una pieza breve?", "Si cumple la lista de condiciones", "La lista dice qué debe cumplir."), ex("¿Cuántas secciones tiene la forma ABA?", "3", "A, B y otra vez A."), ex("¿Qué escribes al final de la pieza?", "Su duración y su propósito", "Así sabes cuánto dura y para qué es.")],
    (
        f"Crea una pieza ABA de 12 pulsos con la leyenda: A de 4 pulsos, B de 4 pulsos distinta de A, y A de nuevo igual. Elige un propósito (por ejemplo, «para empezar un juego» o «para despedir al curso»). Revísala con la lista ({LISTA}), corrige una condición que falle y escribe cuántos pulsos tocaste y qué cambiaste. Toca la pieza con dos medios sonoros distintos (por ejemplo, palmas y una caja golpeada suavemente) y di qué cambió en el sonido.",
        f"Propósito: para empezar un juego. A: {P(TA, TA, TT, TA)}. B: {P(TAA, TA, TA)}. A igual. Revisé: ✓✓✓. Dura 12 pulsos. No cambié nada porque todo cumplía.",
        ["crea las tres secciones de 4 pulsos", "revisa con las tres condiciones", "escribe duración y propósito"],
        ["escritura", "interpretación con palmas", "revisión escrita"],
        ["que la B se parezca a la A", "no contar los pulsos de cada sección"],
        "Reconoce la revisión condición por condición y pide que toque la pieza completa con pulso parejo.",
    ),
    "Toca una pieza ABA de 12 pulsos con un pie marcando el pulso.",
    "Escribe un segundo borrador con otra B y revísalo con la lista.",
)

# ---------------------------------------------------------------- OA 06 · clase 1
ROLES = ("presentador/a", "director/a de señales", "encargado/a de material", "intérpretes")
EQUIPO = 7

L(
    OA6, 1,
    f"Lápiz y papel. Un equipo imaginario de {EQUIPO} estudiantes prepara una presentación para el curso. Roles posibles: {', '.join(ROLES)}. Nadie debe quedar obligado a tocar solo; hay roles para todos.",
    "Aprenderé a definir el propósito, la audiencia y los roles de una presentación musical. Sirve para presentar con compromiso y responsabilidad.",
    ["Sé hacer una pieza breve.", "Sé qué es una señal de entrada.", "Sé escuchar a los demás."],
    [
        "Presentar es mostrar tu trabajo musical a otras personas, la audiencia: el curso, otro curso o la comunidad. Antes de presentar hay que decidir tres cosas: el propósito (¿para qué presentamos?), la audiencia (¿para quién?) y los roles (¿quién hace qué?).",
        f"Un equipo puede tener estos roles: {', '.join(ROLES)}. El presentador anuncia la pieza. El director de señales da la entrada y el final. El encargado de material trae y guarda los instrumentos. Los intérpretes tocan o cantan. Cada rol es importante y se puede presentar de forma individual o en grupo.",
        "Un plan de presentación escribe: propósito, audiencia, roles con nombres y orden de las piezas. Por ejemplo, el propósito puede ser «mostrar lo que aprendimos» y la audiencia «el curso paralelo». Un plan claro da seguridad y evita discusiones el día de la presentación.",
    ],
    [("presentación", "momento en que se muestra un trabajo a otras personas"), ("audiencia", "personas que escuchan y ven la presentación"), ("rol", "tarea que cumple cada persona del equipo"), ("propósito", "para qué se presenta"), ("programa", "lista del orden de las piezas")],
    [
        ("Repartir roles", f"En un equipo de {EQUIPO} estudiantes hay 1 presentador, 1 director de señales y 1 encargado de material. Los demás son intérpretes. ¿Cuántos intérpretes hay?", ["Los roles fijos son 1 + 1 + 1 = 3.", f"{EQUIPO} − 3 = {EQUIPO - 3}."], f"{EQUIPO - 3} intérpretes"),
        ("Calcular el programa", "El programa tiene 3 piezas de 2 minutos cada una y 1 minuto de presentación por pieza. ¿Cuántos minutos dura en total?", ["Cada pieza con su presentación dura 2 + 1 = 3 minutos.", "3 piezas × 3 minutos = 9 minutos."], "9 minutos"),
    ],
    [
        ("Decidir la presentación sin definir la audiencia.", "No se sabe qué conviene mostrar ni cómo hablarles.", "Escribe para quién presentas."),
        ("Que una persona haga todos los roles.", "Se cansa y el equipo no aprende.", "Reparte los roles entre todos."),
    ],
    [
        ex("¿Cómo se llama la persona que anuncia la pieza?", "Presentador o presentadora", "Es quien anuncia la pieza."),
        ex("¿Quién da la señal de entrada y el final?", "El director o directora de señales", "Ese rol marca los comienzos y finales."),
        ex("¿Quién trae y guarda los instrumentos?", "El encargado o encargada de material", "Ese rol cuida el material."),
    ],
    [
        ex(f"En un equipo de {EQUIPO} estudiantes hay 1 presentador, 1 director de señales y 1 encargado de material. ¿Cuántos son intérpretes?", str(EQUIPO - 3), f"{EQUIPO} menos 3 roles fijos."),
        ex("¿Se puede presentar solo y en grupo?", "Sí", "Ambas formas son posibles."),
        ex("Tu plan dice «mostrar lo que aprendimos al curso paralelo». ¿Cuál es la audiencia?", "El curso paralelo", "Es quien escucha."),
    ],
    [
        arith("Un programa tiene 4 piezas de 2 minutos cada una. ¿Cuántos minutos suena la música, sin presentaciones?", "4*2", "Son 4 piezas de 2 minutos.", " minutos"),
        arith("Cada pieza se anuncia en 1 minuto y hay 4 piezas. ¿Cuántos minutos de anuncios hay?", "4*1", "Un minuto por cada pieza.", " minutos"),
        ex("Un estudiante prefiere no tocar ni hablar frente al curso. ¿Cuál de los cuatro roles no lo exige?", "El encargado o encargada de material", "Ese rol trae y guarda los instrumentos, sin tocar ni hablar ante el público."),
    ],
    [
        ex("Luis dice: «no hace falta plan, improvisamos el día». ¿Qué problema puede ocurrir?", "No se sabe quién hace qué", "Sin roles y orden, hay confusión."),
        arith("Un programa de 4 piezas dura 12 minutos con las presentaciones. Si cada pieza dura 2 minutos, ¿cuántos minutos suman los anuncios?", "12-4*2", "Al total se le quitan 8 minutos de música.", " minutos"),
    ],
    [
        arith("El equipo de 7 tiene 3 roles fijos. Si los intérpretes se reparten en 2 piezas por igual y las dos tienen la misma cantidad, ¿cuántos intérpretes toca en cada pieza?", "4//2", "Hay 4 intérpretes y 2 piezas.", " intérpretes"),
        ex("Escribe en una frase el propósito de una presentación para mostrar lo aprendido sobre pulso y acento a otro curso.", "Mostrar al otro curso lo aprendido sobre pulso y acento", "El propósito dice para qué se presenta."),
    ],
    [ex("Un curso organiza una muestra musical para el resto de la escuela. ¿Cuál es la audiencia?", "El resto de la escuela", "La audiencia es quien escucha y ve la presentación.")],
    [ex("¿Qué es la audiencia?", "Las personas que escuchan y ven", "Es para quien se presenta."), ex("En Música: ¿Qué es un rol?", "Una tarea que cumple cada persona", "Se reparte en el equipo."), ex("¿Qué escribe un plan de presentación?", "Propósito, audiencia, roles y orden", "Con eso todos saben qué hacer.")],
    (
        "Escribe el plan de una presentación de tu curso con estas partes: propósito, audiencia, roles (con nombres inventados, no de personas reales) y orden de tres piezas. Calcula cuántos minutos dura si cada pieza dura 2 minutos y cada anuncio, 1 minuto. Puedes presentar solo o en grupo, y puedes elegir un rol que no sea tocar frente al público.",
        "Propósito: mostrar el pulso y el acento. Audiencia: el curso. Roles: Ana presenta, Luis da señales, Sofía trae el material, 4 intérpretes. Orden: pieza 1, 2 y 3. Duración: 3 × (2 + 1) = 9 minutos.",
        ["define propósito y audiencia", "reparte los roles", "calcula la duración"],
        ["plan escrito"],
        ["olvidar la audiencia", "dar todos los roles a una sola persona"],
        "Reconoce el plan completo y revisa que cada estudiante tenga un rol.",
    ),
    "Cuenta a una persona de tu casa a quién le gustaría presentar tu trabajo musical.",
    "Escribe un programa de tres piezas con su duración total.",
)

# ---------------------------------------------------------------- OA 06 · clase 2
ENS = {"ensayo 1": (4, 6, 2), "ensayo 2": (3, 4, 1), "ensayo 3": (1, 2, 0)}
ENS_TXT = " ".join(f"{k}: errores en A = {a}, en B = {b}, en A final = {c}." for k, (a, b, c) in ENS.items())
ENS_TOT = {k: sum(v) for k, v in ENS.items()}

L(
    OA6, 2,
    f"Lápiz y papel. Registro de errores de un equipo (cada ensayo anota los errores por sección): {ENS_TXT}",
    "Aprenderé a ensayar por secciones y a usar evidencia, como un registro de errores, para decidir qué practicar. Sirve para llegar mejor preparado a la presentación.",
    ["Sé revisar una pieza con una lista.", "Sé contar errores.", "Sé qué es una sección."],
    [
        "Ensayar es practicar varias veces para tocar mejor. En vez de repetir la pieza entera, conviene ensayar por secciones: se practica la parte más difícil hasta que sale parejo y después se une con las demás. Eso ahorra tiempo.",
        f"Para saber qué sección practicar, usamos un registro de errores: anotamos en cada ensayo cuántos errores hubo en cada sección. Registro de ejemplo: {ENS_TXT} En el ensayo 1 hubo {ENS_TOT['ensayo 1']} errores, en el 2 hubo {ENS_TOT['ensayo 2']} y en el 3 hubo {ENS_TOT['ensayo 3']}. Los errores bajan: el ensayo funcionó.",
        "La evidencia ayuda a decidir. La sección B tuvo más errores en cada ensayo, así que conviene practicarla primero. Un error no es una falla personal, es una pista de qué practicar. Cuida tu voz y tus manos: descansa entre ensayos y toma agua.",
    ],
    [("ensayo", "práctica repetida para mejorar"), ("sección", "parte de la pieza"), ("registro de errores", "tabla donde se anotan los errores por sección"), ("evidencia", "dato que sirve para decidir"), ("mejora", "avance que se ve en el registro")],
    [
        ("Leer el registro", f"{ENS_TXT} ¿Cuántos errores hubo en total en el ensayo 1?", ["Sumo los errores de A, B y A final.", "4 + 6 + 2 = 12."], f"{ENS_TOT['ensayo 1']} errores"),
        ("Decidir qué practicar", f"{ENS_TXT} ¿Qué sección tuvo más errores en el ensayo 2?", ["Comparo 3, 4 y 1.", "El mayor es 4, en la sección B."], "La sección B"),
    ],
    [
        ("Repetir siempre la pieza entera aunque falle una sola parte.", "Se pierde tiempo en lo que ya sale bien.", "Practica por secciones la parte que falla."),
        ("Enojarse por los errores.", "Los errores son pistas para mejorar.", "Anota el error y practica esa parte."),
    ],
    [
        ex(f"{ENS_TXT} ¿Cuántos errores hubo en la sección A en el ensayo 3?", "1", "El registro dice que en A hubo 1 error."),
        ex(f"{ENS_TXT} ¿Cuántos errores hubo en el ensayo 3 en total?", str(ENS_TOT["ensayo 3"]), "1 + 2 + 0."),
        ex("¿Conviene ensayar la pieza entera o la sección más difícil?", "La sección más difícil", "Así se aprovecha mejor el tiempo."),
    ],
    [
        ex(f"{ENS_TXT} ¿En qué ensayo hubo menos errores en total?", "En el ensayo 3", "Tuvo 3 errores contra 12 y 8."),
        ex(f"{ENS_TXT} ¿Cuántos errores menos hubo en el ensayo 2 que en el 1?", str(ENS_TOT["ensayo 1"] - ENS_TOT["ensayo 2"]), "12 − 8 = 4."),
        ex(f"{ENS_TXT} ¿En qué sección hubo más errores en el ensayo 1?", "En la sección B", "La B tuvo 6 errores."),
    ],
    [
        arith(f"Suma los errores de la sección B en los tres ensayos de este registro: B = 6, 4 y 2.", "6+4+2", "Se suman los errores de la sección B de los tres ensayos.", " errores"),
        arith(f"Si cada ensayo dura 10 minutos y hicieron 3 ensayos, ¿cuántos minutos ensayaron?", "10*3", "Son 3 ensayos de 10 minutos.", " minutos"),
        ex("El registro muestra: ensayo 1 con 12 errores, ensayo 2 con 8 y ensayo 3 con 3. ¿Los errores bajan o suben?", "Bajan", "Cada ensayo tiene menos errores."),
    ],
    [
        ex("Pedro dice «no necesito registro, lo recuerdo». ¿Qué ventaja da el registro?", "Muestra con evidencia qué sección falla", "Recordar no basta; el registro lo prueba."),
        ex(f"{ENS_TXT} ¿Qué sección conviene practicar primero y por qué?", "La B, porque tuvo más errores en los tres ensayos", "En todos los ensayos la B superó a las demás."),
    ],
    [
        arith("Una pieza tiene tres secciones. Quieres ensayar la B 3 veces y las otras dos 1 vez cada una. ¿Cuántas veces ensayas secciones en total?", "3+1+1", "Se suman las veces de cada sección.", " veces"),
        ex("En el siguiente ensayo, el equipo registra A = 0, B = 1 y A final = 0. ¿Cuántos errores fueron en total y mejoró respecto del ensayo 3?", "1 error; mejoró", "El ensayo 3 tuvo 3 errores y este tiene 1."),
    ],
    [ex("Antes de la presentación, el equipo tiene 30 minutos para ensayar. Si cada ensayo dura 10 minutos, ¿cuántos ensayos pueden hacer?", "3", "30 dividido en 10 minutos da 3.")],
    [ex("¿Qué es un registro de errores?", "Una tabla donde se anotan los errores por sección", "Sirve de evidencia."), ex("¿Qué haces con la sección que más falla?", "La practicas primero", "Así se mejora más rápido."), ex("¿Un error es una falla personal o una pista?", "Una pista", "Indica qué practicar.")],
    (
        "Usa un registro propio: toca 3 veces una pieza breve (por ejemplo, tu pieza ABA de la clase anterior) y anota cuántos errores tuviste en la sección A, en la B y en la A final cada vez. Escribe cuál sección falló más, cuántos errores hubo en cada ensayo y si los errores bajaron. Si no tienes una pieza, usa el motivo TA – TA – ti-ti repetido 4 veces en cada sección.",
        "Ensayo 1: A 1, B 3, A 0 (4). Ensayo 2: A 0, B 2, A 0 (2). Ensayo 3: A 0, B 1, A 0 (1). La B falló más y los errores bajaron de 4 a 1.",
        ["anota los errores de cada ensayo", "identifica la sección que más falla", "dice si los errores bajaron"],
        ["registro escrito", "ensayos"],
        ["practicar siempre la pieza entera", "no escribir los errores"],
        "Reconoce el uso del registro y pregunta qué sección practicará primero y por qué.",
    ),
    "Practica solo una sección difícil 3 veces y anota si mejoró.",
    "Dibuja una tabla de errores para tres ensayos y llena un ejemplo.",
)

# ---------------------------------------------------------------- OA 06 · clase 3
SEC_P, TRANS_P, N_SEC = 8, 2, 3
TOTAL_P = SEC_P * N_SEC + TRANS_P * (N_SEC - 1)

L(
    OA6, 3,
    f"Lápiz y papel. Plan de una pieza A – B – A: cada sección dura {SEC_P} pulsos y entre secciones hay una transición de {TRANS_P} pulsos en silencio con una señal de la mano. Cada pulso dura 1 segundo.",
    "Aprenderé a ajustar las transiciones entre secciones y a cuidar el sonido y los instrumentos. Sirve para que la presentación fluya y sea segura.",
    ["Sé qué es una sección.", "Sé contar pulsos.", "Sé seguir una señal."],
    [
        f"Una transición es el momento de paso de una sección a otra. Una buena transición es clara: todos saben cuándo termina una sección y cuándo comienza la siguiente. En el plan, entre secciones hay {TRANS_P} pulsos de silencio y una señal de la mano. Eso da tiempo de respirar y de cambiar de instrumento.",
        f"Calculamos la duración: {N_SEC} secciones de {SEC_P} pulsos son {SEC_P * N_SEC} pulsos, y hay {N_SEC - 1} transiciones de {TRANS_P} pulsos, que son {TRANS_P * (N_SEC - 1)} pulsos. En total son {TOTAL_P} pulsos, es decir, {TOTAL_P} segundos si cada pulso dura 1 segundo.",
        "El cuidado sonoro significa tocar a un volumen que no dañe los oídos ni tape a los demás, y tratar bien los instrumentos: no lanzarlos, no golpearlos de más y guardarlos en su lugar. Si algo suena demasiado fuerte, baja el volumen. Cuida también el espacio: deja pasillos libres.",
    ],
    [("transición", "paso de una sección a otra"), ("señal", "gesto que avisa cuándo empezar o terminar"), ("cuidado sonoro", "tocar sin dañar los oídos ni tapar a otros"), ("volumen", "qué tan fuerte suena"), ("ordenar", "dejar el material en su lugar")],
    [
        ("Calcular la duración con transiciones", f"Una pieza A – B – A tiene secciones de {SEC_P} pulsos y {N_SEC - 1} transiciones de {TRANS_P} pulsos. ¿Cuántos pulsos dura?", [f"Secciones: {N_SEC} × {SEC_P} = {SEC_P * N_SEC}.", f"Transiciones: {N_SEC - 1} × {TRANS_P} = {TRANS_P * (N_SEC - 1)}.", f"{SEC_P * N_SEC} + {TRANS_P * (N_SEC - 1)} = {TOTAL_P}."], f"{TOTAL_P} pulsos"),
        ("Ajustar la señal", "Un equipo no sabe cuándo termina la sección B. ¿Qué pueden agregar para que quede claro?", ["Hace falta algo que todos vean o escuchen.", "Una señal de la mano al final de la sección."], "Una señal de la mano al terminar la sección"),
    ],
    [
        ("Pasar de una sección a otra sin avisar.", "Algunos del equipo se pierden.", "Usa una señal y un silencio breve."),
        ("Tocar fuerte para que se oiga más.", "Daña los oídos y tapa a los demás.", "Baja el volumen y escucha al grupo."),
    ],
    [
        ex(f"Plan: {N_SEC} secciones de {SEC_P} pulsos. ¿Cuántos pulsos suman solo las secciones?", str(SEC_P * N_SEC), f"{N_SEC} × {SEC_P}."),
        ex("¿Qué es una transición?", "El paso de una sección a otra", "Une dos secciones."),
        ex("Si algo suena demasiado fuerte, ¿qué haces?", "Bajas el volumen", "Así cuidas los oídos."),
    ],
    [
        ex(f"Plan: {N_SEC - 1} transiciones de {TRANS_P} pulsos. ¿Cuántos pulsos suman las transiciones?", str(TRANS_P * (N_SEC - 1)), f"{N_SEC - 1} × {TRANS_P}."),
        ex(f"Plan completo: {N_SEC} secciones de {SEC_P} pulsos y {N_SEC - 1} transiciones de {TRANS_P}. ¿Cuántos segundos dura si cada pulso es 1 segundo?", str(TOTAL_P), f"{TOTAL_P} pulsos son {TOTAL_P} segundos."),
        ex("Nombra una forma de cuidar un instrumento durante la presentación.", "No lanzarlo, ni golpearlo de más, y guardarlo en su lugar", "El cuidado evita dañarlo."),
    ],
    [
        arith(f"Si se agrega una cuarta sección de {SEC_P} pulsos y otra transición de {TRANS_P}, ¿cuántos pulsos dura la pieza?", f"4*{SEC_P}+3*{TRANS_P}", "4 secciones y 3 transiciones.", " pulsos"),
        arith(f"Quieres que la transición dure 4 pulsos en vez de {TRANS_P}. ¿Cuántos pulsos dura la pieza de {N_SEC} secciones?", f"{N_SEC}*{SEC_P}+{N_SEC - 1}*4", "Se cambian los pulsos de las transiciones.", " pulsos"),
        ex("El director de señales levanta la mano para pedir silencio. ¿Es una señal clara?", "Sí", "Todos la pueden ver."),
    ],
    [
        ex("Ana dice que no hace falta silencio entre secciones porque se entiende. ¿Qué problema puede haber?", "Algunos entran antes o después y se pierden", "El silencio y la señal ordenan las entradas."),
        ex("Una niña ve que el volumen es muy alto en la sala. ¿Qué debe decidir el equipo?", "Bajar el volumen", "Cuidar los oídos es prioridad."),
    ],
    [
        arith(f"La pieza dura {TOTAL_P} segundos. Si la ensayan 3 veces seguidas, ¿cuántos segundos ensayan?", f"{TOTAL_P}*3", "Se multiplica la duración por 3.", " segundos"),
        ex("Dos estudiantes quieren el mismo instrumento a la vez. ¿Cómo lo resuelven con cuidado?", "Se turnan, uno después del otro", "Los turnos evitan conflictos y daños."),
    ],
    [ex("En una muestra en el patio, el volumen debe permitir conversar con alguien que está al lado. ¿Es un buen criterio de cuidado sonoro?", "Sí", "Un volumen que permite conversar cuida los oídos.")],
    [ex("En Música: ¿Qué es una señal?", "Un gesto que avisa cuándo empezar o terminar", "Ordena las entradas."), ex("¿Qué haces con el material al final?", "Lo ordenas", "Dejas todo en su lugar."), ex("¿Qué debes cuidar al tocar fuerte?", "Los oídos y los demás", "El volumen no debe dañar ni tapar.")],
    (
        f"Planifica la transición de tu pieza: dibuja tres cajas A | B | A con dos espacios de {TRANS_P} pulsos entre ellas. Escribe qué señal usarás y cómo cuidarás el sonido y el material. Calcula cuántos pulsos y cuántos segundos dura tu presentación con secciones de {SEC_P} pulsos y {TRANS_P} pulsos de transición. Si puedes, ensáyala con palmas.",
        f"Cajas A | B | A con dos silencios de {TRANS_P} pulsos. Señal: levantar la mano. Cuidado: volumen bajo y guardar el material. Duración: {TOTAL_P} pulsos, {TOTAL_P} segundos.",
        ["incluye transiciones con silencio y señal", "explica el cuidado sonoro", "calcula la duración"],
        ["plan escrito", "ensayo con palmas"],
        ["no incluir señal", "olvidar sumar las transiciones"],
        "Reconoce la señal clara y pide que muestre cómo se entra en la sección B; revisa la suma.",
    ),
    "Practica una señal de la mano para empezar y otra para terminar con una persona de tu casa.",
    "Escribe tres reglas de cuidado sonoro para una presentación.",
)

# ---------------------------------------------------------------- OA 06 · clase 4
COMENT = {
    1: ("«Tocaron parejo y el pulso se mantuvo.»", True),
    2: ("«Fue fome.»", False),
    3: ("«En la sección B se oyó muy fuerte y tapó la voz; podrían bajar el volumen.»", True),
    4: ("«Qué malos son.»", False),
    5: ("«Me gustó cómo empezaron todos juntos con la señal.»", True),
}
COM_TXT = " ".join(f"{k}) {t}" for k, (t, _v) in COMENT.items())
COM_OK = [k for k, (_t, v) in COMENT.items() if v]

L(
    OA6, 4,
    f"Lápiz y papel. Comentarios de ejemplo para clasificar: {COM_TXT} Regla de la clase: un buen comentario describe algo que se oyó o se vio y nunca ataca a la persona.",
    "Aprenderé a presentar mi trabajo con responsabilidad y a recoger y dar retroalimentación respetuosa. Sirve para mejorar y para cuidar a los demás.",
    ["Sé ensayar por secciones.", "Sé escuchar a los demás.", "Sé que los errores son pistas."],
    [
        "El día de la presentación, cada persona cumple su rol, respeta las señales y cuida el material. Si alguien se equivoca, el equipo sigue con el pulso, sin detenerse ni burlarse. Al terminar, se agradece a la audiencia con una inclinación de cabeza o con un «gracias».",
        f"La retroalimentación es lo que la audiencia y el equipo dicen sobre la presentación para ayudarla a mejorar. Un buen comentario describe lo que se oyó o se vio y sugiere algo. Ejemplos: {COM_TXT} Los comentarios {', '.join(str(k) for k in COM_OK)} son buenos. Los otros solo juzgan y no ayudan.",
        "Una forma sencilla de dar retroalimentación es «dos logros y un deseo»: dices dos cosas que salieron bien, con evidencia, y una cosa que podrían mejorar, también con evidencia. Escucha los comentarios sin defenderte y anota lo que usarás en el próximo ensayo.",
    ],
    [("retroalimentación", "comentarios que ayudan a mejorar"), ("evidencia", "algo que se oyó o se vio"), ("logro", "algo que salió bien"), ("deseo", "algo que se puede mejorar"), ("respeto", "tratar bien a quien presenta")],
    [
        ("Clasificar comentarios", f"Regla: un buen comentario describe algo que se oyó o se vio y nunca ataca a la persona. {COM_TXT} ¿Cuáles son buenos comentarios?", ["Reviso cada uno.", "El 1, el 3 y el 5 describen algo.", "El 2 y el 4 solo juzgan."], " y ".join(str(k) for k in COM_OK)),
        ("Armar «dos logros y un deseo»", "Un equipo tocó parejo, empezó junto con la señal y en la sección B subió el volumen y tapó la voz. Arma la retroalimentación.", ["Dos logros: tocaron parejo y empezaron juntos.", "Un deseo: bajar el volumen en B."], "Logros: pulso parejo y entrada juntos; deseo: bajar el volumen en la sección B"),
    ],
    [
        ("Defenderse apenas alguien comenta.", "Impide escuchar la sugerencia.", "Escucha y anota; después decide qué usar."),
        ("Comentar solo con «me gustó» o «qué fome».", "No ayuda a mejorar.", "Di qué oíste o viste y qué cambiarías."),
    ],
    [
        ex("¿Qué debe hacer un equipo si alguien se equivoca durante la presentación?", "Seguir con el pulso, sin burlarse", "Así la presentación continúa."),
        ex("En Música: ¿Qué es la retroalimentación?", "Comentarios que ayudan a mejorar", "Se dan con respeto."),
        ex("En «dos logros y un deseo», el comentario «Podrían mirar al director de señales al empezar» ¿es un logro o un deseo?", "Un deseo", "Sugiere algo que se puede mejorar."),
    ],
    [
        ex(f"{COM_TXT} ¿Cuántos comentarios son buenos?", str(len(COM_OK)), "Son el 1, el 3 y el 5."),
        ex(f"{COM_TXT} ¿Cuál comentario sugiere un cambio concreto?", "El 3", "El 3 dice que bajen el volumen."),
        ex("Una niña dice «qué malos son». ¿Es un comentario que ayuda?", "No", "No describe nada ni sugiere un cambio."),
    ],
    [
        ex("Reescribe «fue fome» como un comentario con evidencia. Elige: (a) «Fue fome.», (b) «El pulso se aceleró en la sección B.»", "(b)", "La (b) describe algo que se oyó."),
        arith("Si 5 compañeros dan retroalimentación y cada uno dice 2 logros y 1 deseo, ¿cuántos comentarios hay?", "5*(2+1)", "Cada compañero dice 3 comentarios.", " comentarios"),
        ex("Un equipo recibe tres comentarios: 2 logros y 1 deseo. ¿Qué anota para el próximo ensayo?", "El deseo", "El deseo dice qué mejorar."),
    ],
    [
        ex("Pedro recibe un deseo y responde enojado «yo lo hice bien». ¿Qué puede hacer en cambio?", "Escuchar, anotar y decidir después", "Así aprovecha la sugerencia."),
        ex("Una niña se equivoca en la presentación y algunos se ríen. ¿Qué acuerdo de respeto falta?", "No burlarse de los errores", "Los errores son pistas, no motivo de burla."),
    ],
    [
        arith("En una muestra de 4 piezas, cada pieza recibe 3 comentarios de ayuda. ¿Cuántos comentarios recibe el curso en total?", "4*3", "Son 4 piezas con 3 comentarios cada una.", " comentarios"),
        ex("Escribe «dos logros y un deseo» sobre una presentación en que empezaron juntos, mantuvieron el pulso y en un momento se oyó muy bajo el instrumento de la sección A. Elige: (a) Logros: empezaron juntos y mantuvieron el pulso; deseo: subir un poco el instrumento en A. (b) Logros: nada; deseo: tocar mejor.", "(a)", "La (a) usa evidencia concreta."),
    ],
    [ex("Después de que un curso presenta una canción al resto de la escuela, una profesora pide dar un logro y un deseo. ¿Qué debe tener cada comentario?", "Algo que se oyó o se vio", "Eso lo vuelve evidencia.")],
    [ex("¿Qué se hace al terminar la presentación?", "Se agradece a la audiencia", "Es una muestra de respeto."), ex("¿Un comentario debe atacar a la persona?", "No", "Debe describir lo que se oyó o vio."), ex("¿Qué haces con el deseo que recibes?", "Lo anotas para el próximo ensayo", "Te sirve para mejorar.")],
    (
        "Presenta tu pieza ABA (o el motivo de la clase anterior) a una persona de tu casa o a tu curso, cumpliendo tu rol, la señal de entrada y el cuidado del material. Al terminar, agradece. Pide un comentario del tipo «dos logros y un deseo» y escríbelo. Anota qué cambiarás en el próximo ensayo. No hace falta exponerte solo: puedes presentar en grupo o con un rol de apoyo.",
        "Logros: mantuvieron el pulso y empezaron juntos con la señal. Deseo: bajar un poco el volumen en la sección B. Cambiaré: tocar más suave en B.",
        ["cumple su rol", "agradece y escucha sin defenderse", "anota dos logros y un deseo con evidencia"],
        ["presentación", "comentarios escritos"],
        ["defenderse ante el deseo", "recibir comentarios sin evidencia"],
        "Reconoce el cuidado y pide que lea el deseo y diga qué cambiará; si hay burla, vuelve al acuerdo de respeto.",
    ),
    "Pide a una persona de tu casa que te diga un logro y un deseo sobre algo que hayas tocado.",
    "Escribe tres frases que usarías para dar retroalimentación respetuosa.",
)
