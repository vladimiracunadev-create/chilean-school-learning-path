"""Student material for 5.º básico Música, OA 01 (lenguaje musical y propósito expresivo) y OA 02 (respuesta elaborada a la música escuchada).

Todas las músicas de los ejercicios son descripciones o patrones originales inventados para esta clase; las audiciones reales las selecciona el docente.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1, OA2 = "MU05 OA 01", "MU05 OA 02"

TA, TT, TAA, SIL, TIRI = "TA", "ti-ti", "TAA", "SIL", "tiri-tiri"
LEY = ("TA = 1 sonido en 1 pulso; ti-ti = 2 sonidos rápidos en 1 pulso; tiri-tiri = 4 sonidos muy rápidos en 1 pulso; "
       "TAA = 1 sonido largo que dura 2 pulsos; SIL = 1 pulso de silencio")
_PULSOS = {TA: 1, TT: 1, TIRI: 1, TAA: 2, SIL: 1}
_SONIDOS = {TA: 1, TT: 2, TIRI: 4, TAA: 1, SIL: 0}


def P(*tokens: str) -> str:
    return " – ".join(tokens)


def pulses(*tokens: str) -> int:
    return sum(_PULSOS[t] for t in tokens)


def sounds(*tokens: str) -> int:
    return sum(_SONIDOS[t] for t in tokens)


def diff(a: tuple, b: tuple) -> int:
    assert len(a) == len(b)
    return sum(1 for x, y in zip(a, b) if x != y)


def N(*notes: int) -> str:
    return "-".join(str(n) for n in notes)


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- OA 01 · clase 1 (pulso, acento, compás)
CA, CB, CC, CD = (TA, TT, TAA), (TAA, TA, SIL), (TT, TT, TA, SIL), (TA, TAA, TAA)

L(
    OA1, 1,
    f"Lápiz, tus palmas y tus pies. Leyenda de ritmo: {LEY}. Todos los patrones están escritos en los ejercicios. Toca a volumen bajo.",
    "Aprenderé a leer el compás: cuántos pulsos tiene cada grupo y dónde cae el acento. Sirve para describir un ritmo y tocarlo sin perderme.",
    ["Sé que el pulso es el latido parejo de la música.", "Sé contar pulsos de un patrón con TA, ti-ti, TAA y SIL.", "Sé que el acento es el pulso más fuerte."],
    [
        "El pulso es el latido parejo de la música, como tus pasos al caminar. Los pulsos se agrupan en compases, que son grupos del mismo tamaño. El primer pulso de cada compás lleva el acento, o sea, se marca más fuerte. Si cuentas 1-2-3, 1-2-3, el acento cae en cada 1 y estás en un compás de 3 pulsos.",
        "En una partitura, el compás se escribe como una fracción: 2/4, 3/4 o 4/4. Por ahora, fíjate en el número de arriba: dice cuántos pulsos tiene cada compás. Un 3/4 tiene 3 pulsos por compás y un 4/4 tiene 4. Las líneas verticales que separan los compases se llaman barras de compás.",
        f"Un patrón rítmico es una secuencia de sonidos y silencios que se repite sobre el pulso. Para saber si un patrón llena un compás, suma lo que ocupa cada símbolo. Con la leyenda de la clase, {P(*CA)} ocupa 1 + 1 + 2 = {pulses(*CA)} pulsos, así que llena un compás de 4 pulsos. Si da más, sobra; si da menos, falta.",
    ],
    [("compás", "grupo de pulsos del mismo tamaño"), ("acento", "pulso que se marca más fuerte, el primero de cada compás"), ("barra de compás", "línea vertical que separa un compás de otro"), ("patrón rítmico", "secuencia de sonidos y silencios que se repite"), ("3/4 y 4/4", "compases de 3 y de 4 pulsos")],
    [
        ("Ver si llena el compás", f"¿El patrón {P(*CD)} llena un compás de 4 pulsos?", ["TA ocupa 1 pulso.", "Cada TAA ocupa 2 pulsos.", "1 + 2 + 2 = 5 pulsos, más de 4."], "No: tiene 5 pulsos y sobra 1"),
        ("Ubicar acentos", "Cuento 15 pulsos en compases de 3. ¿En qué números cae el acento?", ["Los compases son 1-2-3, 4-5-6, 7-8-9, 10-11-12 y 13-14-15.", "El acento va en el primer pulso de cada compás."], "En los pulsos 1, 4, 7, 10 y 13"),
    ],
    [
        ("Creer que el acento cae en cualquier pulso del compás.", "El acento va en el primer pulso, no al azar.", "Marca fuerte el 1 de cada compás y suaves los demás."),
        ("Contar un símbolo como un pulso aunque sea TAA.", "TAA dura 2 pulsos, aunque sea un solo sonido.", "Suma los pulsos que ocupa cada símbolo, no cuántos símbolos hay."),
    ],
    [
        ex("En un compás de 3 pulsos, ¿cuántos pulsos llevan acento?", "1", "Solo el primer pulso de cada compás lleva acento."),
        ex(f"¿Llena el patrón {P(TA, TA, SIL)} un compás de 3 pulsos? Responde sí o no.", "Sí", "Los tres símbolos ocupan 1 pulso cada uno, y el silencio también cuenta."),
        ex("Cuentas 12 pulsos en compases de 3, con acento en el primero de cada compás. ¿En qué números cae el acento?", "1, 4, 7 y 10", "Cada compás parte tres números después del anterior."),
    ],
    [
        ex(f"¿Cuántos pulsos ocupa el patrón {P(*CA)}?", str(pulses(*CA)), "TA ocupa 1, ti-ti ocupa 1 y TAA ocupa 2."),
        ex("En la partitura aparece 3/4. ¿Qué dice el número de arriba?", "Que cada compás tiene 3 pulsos", "El número de arriba indica cuántos pulsos lleva cada compás."),
        ex(f"Al patrón {P(*CD)} se le pide caber en un compás de 4 pulsos. ¿Sobra o falta, y cuánto?", "Sobra 1 pulso", "Ocupa 5 pulsos y el compás tiene 4."),
    ],
    [
        arith(f"Un tema tiene dos compases de 4 pulsos: {P(*CA)} y {P(*CB)}. ¿Cuántos pulsos hay en total?", f"{pulses(*CA)}+{pulses(*CB)}", "Se suman los pulsos de los dos compases.", " pulsos"),
        arith("Una pieza en compás de 3 pulsos dura 15 pulsos. ¿Cuántos compases completos tiene?", "15//3", "Cada compás tiene 3 pulsos y se reparten 15.", " compases"),
        ex(f"¿Cuál de estos patrones completa un compás de 3 pulsos: (a) {P(TA, TAA)} o (b) {P(TA, TA, TAA)}?", "(a)", "El (a) ocupa 1 + 2 = 3 pulsos; el (b) ocupa 4."),
    ],
    [
        ex(f"Luis dice que {P(TAA, TAA, TA)} cabe en un compás de 4 pulsos porque tiene solo 3 símbolos. ¿Cuántos pulsos ocupa realmente?", "5", "Dos TAA ocupan 4 pulsos y el TA suma 1: no se cuentan símbolos, se cuentan pulsos."),
        ex(f"Al compás {P(TA, TA)} de 4 pulsos le faltan 2 pulsos. ¿Qué único símbolo de la leyenda de la clase los completa?", "TAA", "Los dos TA ocupan 2 pulsos y faltan 2, que es lo que dura un TAA."),
    ],
    [
        ex(f"El patrón {P(*CC)} llena un compás de 4. ¿Cuántos sonidos suenan en él?", str(sounds(*CC)), "Cada ti-ti son 2 sonidos (2 + 2), el TA suma 1 y el silencio no suena."),
        arith("Una pieza tiene 7 compases de 3 pulsos y otra tiene 5 compases de 4 pulsos. ¿Cuántos pulsos más tiene la primera?", "7*3-5*4", "La primera tiene 21 pulsos y la segunda 20; se restan.", " pulso más"),
    ],
    [ex("En un desfile se marcha en compases de 2 pulsos y se pisa más fuerte el primero. Tras 10 compases, ¿cuántos pasos fuertes y cuántos suaves se dieron?", "10 fuertes y 10 suaves", "Cada compás tiene 1 pulso fuerte y 1 suave, y son 10 compases.")],
    [ex("¿Cómo se llama el grupo de pulsos del mismo tamaño?", "Compás", "El compás agrupa los pulsos."), ex("¿Qué número de pulsos tiene un compás 4/4?", "4", "El número de arriba es 4."), ex("¿Qué pulso del compás se marca más fuerte?", "El primero", "Ahí cae el acento.")],
    (
        f"Camina en tu lugar con paso parejo y cuenta de a 4 (1-2-3-4), pisando más fuerte en el 1. Toca con las palmas el compás {P(*CA)} cuatro veces seguidas. Escribe cuántos pulsos tiene un compás y cuántos pulsos tocaste en total, y marca con una X en qué pulsos pisaste fuerte.",
        "Un compás tiene 4 pulsos. Toqué 4 compases: 16 pulsos. Pisé fuerte en los pulsos 1, 5, 9 y 13: X – – – X – – – X – – – X – – –.",
        ["mantiene el paso parejo", "marca fuerte solo el primer pulso de cada compás", "escribe los conteos correctos"],
        ["interpretación", "conteo escrito"],
        ["marcar fuerte pulsos que no son el primero", "contar TAA como un pulso"],
        "Reconoce el pulso estable y pide mostrar con el dedo dónde empieza cada compás y dónde dura 2 pulsos el TAA.",
    ),
    "Cuenta de a 3 hasta 12 pisando fuerte en cada 1 y di cuántos pasos fuertes diste.",
    "Escribe un compás de 4 pulsos con ti-ti, TA y SIL y comprueba con una suma que ocupe 4 pulsos.",
)

# ---------------------------------------------------------------- OA 01 · clase 2 (patrones y diseños melódicos)
NOTAS = "1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si, 8 = do agudo"
M1, M2, M3 = (1, 2, 3, 5, 3, 1), (3, 3, 4, 5, 5, 4), (5, 5, 5, 3, 2, 1)


def moves(m: tuple) -> list[str]:
    return ["sube" if b > a else "baja" if b < a else "repite" for a, b in zip(m, m[1:])]


def leaps(m: tuple) -> int:
    return sum(1 for a, b in zip(m, m[1:]) if abs(b - a) >= 2)


L(
    OA1, 2,
    f"Lápiz y papel. Escala de números: {NOTAS}. Si tienes un metalófono, una flauta o un teclado puedes tocar las melodías, pero no es necesario: todas están escritas con números. Cuida el volumen.",
    "Aprenderé a describir una melodía por su diseño (si sube, baja o repite; si va por grados o da saltos) y a reconocer un patrón melódico que vuelve. Sirve para describir una melodía sin cantarla.",
    ["Sé que los sonidos pueden ser agudos o graves.", "Sé ordenar los números del 1 al 8.", "Sé que una melodía es una sucesión de sonidos de distinta altura."],
    [
        f"Una melodía es una sucesión de sonidos de distinta altura. Para escribirla usamos números: {NOTAS}. Mientras más alto el número, más agudo el sonido. Por ejemplo, la melodía {N(*M1)} parte en do, sube hasta sol (5) y vuelve a do.",
        "El diseño melódico es la forma que dibuja la melodía. Cada paso puede subir, bajar o repetir. Si la nota cambia al número vecino (de 2 a 3), es un paso por grado. Si la nota cambia dos o más números (de 3 a 5, que se salta el 4), es un salto. Una melodía de grados suena más suave y una con saltos suena más abierta. El rango es la distancia entre la nota más grave y la más aguda.",
        f"Un patrón melódico es una pequeña idea de notas que se repite. Si la idea vuelve empezando en otra nota, se llama secuencia. Por ejemplo, {N(1, 2, 3)} y luego {N(2, 3, 4)} son una secuencia: cada nota subió un grado. Reconocer el diseño y los patrones te permite explicar por qué una melodía suena como suena.",
    ],
    [("melodía", "sucesión de sonidos de distinta altura"), ("diseño melódico", "forma que dibuja la melodía: sube, baja o repite"), ("grado y salto", "grado: a la nota vecina; salto: cambia dos o más números"), ("secuencia", "patrón que vuelve empezando en otra nota"), ("rango", "distancia entre la nota más grave y la más aguda")],
    [
        ("Describir el diseño", f"Describe la melodía {N(*M1)}: ¿cuántas veces sube, baja o repite?", ["Pares: 1→2 sube, 2→3 sube, 3→5 sube, 5→3 baja, 3→1 baja.", "No hay repeticiones."], f"Sube {moves(M1).count('sube')} veces, baja {moves(M1).count('baja')} veces y repite {moves(M1).count('repite')}"),
        ("Medir el rango", f"En la melodía {N(*M3)}, ¿cuál es la nota más grave, la más aguda y el rango (la resta)?", ["Más grave: 1.", "Más aguda: 5.", "Rango: 5 − 1 = 4."], "Grave 1, aguda 5, rango 4"),
    ],
    [
        ("Pensar que un número mayor es una nota más grave.", "Mientras más alto el número, más agudo el sonido.", "El 8 es el sonido más agudo y el 1 el más grave."),
        ("Llamar salto a un paso de 2 a 3.", "Un salto se salta por lo menos un número; de 2 a 3 es un grado.", "Si las notas son vecinas, es grado; si no, es salto."),
    ],
    [
        ex("¿Qué nota es el 5 en la escala de la clase?", "Sol", "Según la escala, 5 = sol."),
        ex(f"En la melodía {N(*M2)}, ¿con qué número termina?", "4", "El último número de la melodía es 4."),
        ex(f"En la melodía {N(*M3)}, el paso de 5 a 5, ¿sube, baja o repite?", "Repite", "Es la misma nota dos veces."),
    ],
    [
        ex(f"Cuenta los saltos (pasos de dos o más números) de la melodía {N(*M1)}.", str(leaps(M1)), "Son los pasos 3→5, 5→3 y 3→1; los otros dos son de un grado."),
        ex(f"Cuenta cuántas veces repite la melodía {N(*M2)}.", str(moves(M2).count("repite")), "Repite en 3→3 y en 5→5."),
        ex(f"¿Cuál es la nota más aguda de la melodía {N(*M1)}?", "5", "Es el número mayor de la lista."),
    ],
    [
        arith(f"La melodía {N(*M1)} tiene como nota más aguda el 5 y como más grave el 1. ¿Cuál es su rango?", "5-1", "El rango es la resta entre la más aguda y la más grave.", ""),
        ex(f"La melodía {N(1, 2, 3, 2, 3, 4, 3, 4, 5)} repite una idea de tres notas que sube un grado cada vez. ¿Cómo se llama ese recurso: secuencia o salto?", "Secuencia", "El patrón 1-2-3 vuelve empezando en 2 y luego en 3."),
        ex(f"Escribe cómo seguiría la secuencia {N(1, 3, 5)}, {N(2, 4, 6)}, ... si cada vez sube un grado.", "3-5-7", "Cada nota del patrón sube un número."),
    ],
    [
        ex(f"Ana dice que la melodía {N(*M3)} baja desde su primera nota. ¿Es cierto?", "No: primero repite el 5 tres veces y recién después baja", "Los primeros pasos son 5→5 y 5→5; la bajada parte en el 5 del tercer sonido."),
        ex("Una melodía sube de 1 a 8 de un grado a la vez. ¿Cuántos pasos da?", "7", "Va por 1-2-3-4-5-6-7-8: hay 7 pasos entre 8 notas."),
    ],
    [
        arith("Una melodía tiene 4 compases y en cada uno hay 2 saltos. Un segundo tema tiene 3 compases con 3 saltos en cada uno. ¿Cuántos saltos hay entre los dos temas?", "4*2+3*3", "Se multiplica en cada tema y se suman los resultados.", " saltos"),
        arith("Una melodía tiene 12 pasos: 9 son por grado y el resto son saltos. ¿Cuántos saltos tiene?", "12-9", "Se restan los grados del total de pasos.", " saltos"),
    ],
    [ex("Una canción de cuna baja suavemente por grados: 5-4-3-2-1. ¿Qué diseño tiene: baja por grados o sube con saltos?", "Baja por grados", "Cada paso baja a la nota vecina.")],
    [ex("¿Qué dibuja el diseño melódico?", "Cómo sube, baja o repite la melodía", "Describe la forma de la línea de notas."), ex("¿Qué número es la nota do?", "1", "Según la escala de la clase."), ex("Un paso de 4 a 6, ¿es grado o salto?", "Salto", "Se salta el 5.")],
    (
        f"Inventa una melodía de 6 números del 1 al 5 que parta en 1, termine en 1 y tenga exactamente 2 saltos. Escríbela, marca los saltos y escribe su nota más aguda y su rango. Si tienes un instrumento melódico, tócala despacio; si no, cántala con «la».",
        "Melodía 1-3-4-5-4-1: los saltos son 1→3 y 4→1 (son 2). La nota más aguda es 5 y el rango es 5 − 1 = 4.",
        ["parte y termina en 1", "usa 6 números del 1 al 5", "marca los saltos y calcula el rango"],
        ["melodía escrita", "saltos marcados"],
        ["contar un paso por grado como salto", "no cerrar en 1"],
        "Reconoce la melodía y pide contar los saltos paso por paso: si la diferencia es 2 o más, es salto.",
    ),
    "Escribe una melodía de 5 números que solo suba por grados.",
    "Escribe una secuencia: un patrón de 3 notas que se repita tres veces, cada vez un grado más agudo.",
)
