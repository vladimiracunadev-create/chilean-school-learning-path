"""Student material for 6.º básico Música, OA 01 (describir la música con los elementos del lenguaje musical y su propósito expresivo).

Todas las músicas de los ejercicios son descripciones, melodías numeradas o esquemas originales inventados para esta clase; las audiciones reales las selecciona y pone el docente.
Este módulo también define los ayudantes (L, P, pulses, sounds, N, moves, leaps) que usan los demás módulos mu6_*.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "MU06 OA 01"

NEG, CC, BLA, BP, RED, SN, SB = "negra", "2 corcheas", "blanca", "blanca con puntillo", "redonda", "silencio de negra", "silencio de blanca"
LEY = ("negra = 1 pulso; 2 corcheas = 1 pulso (cada corchea dura medio pulso); blanca = 2 pulsos; blanca con puntillo = 3 pulsos; "
       "redonda = 4 pulsos; silencio de negra = 1 pulso; silencio de blanca = 2 pulsos")
_PUL = {NEG: 1, CC: 1, BLA: 2, BP: 3, RED: 4, SN: 1, SB: 2}
_SON = {NEG: 1, CC: 2, BLA: 1, BP: 1, RED: 1, SN: 0, SB: 0}
NOTAS = "1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si, 8 = do agudo"


def P(*tokens: str) -> str:
    return " – ".join(tokens)


def pulses(*tokens: str) -> int:
    return sum(_PUL[t] for t in tokens)


def sounds(*tokens: str) -> int:
    return sum(_SON[t] for t in tokens)


def N(*notes: int) -> str:
    return "-".join(str(n) for n in notes)


def moves(m: tuple) -> list[str]:
    return ["sube" if b > a else "baja" if b < a else "repite" for a, b in zip(m, m[1:])]


def leaps(m: tuple) -> int:
    return sum(1 for a, b in zip(m, m[1:]) if abs(b - a) >= 2)


def diff(a: tuple, b: tuple) -> int:
    assert len(a) == len(b)
    return sum(1 for x, y in zip(a, b) if x != y)


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- OA 01 · clase 1 (pulso, acento y compás con figuras)
PA, PB, PC, PD, PE = (NEG, CC, BLA), (BP, NEG), (NEG, NEG, NEG), (BLA, BP), (CC, CC, NEG, SN)

L(
    OA1, 1,
    f"Lápiz, tus palmas y tus pies. Leyenda de figuras: {LEY}. Todos los patrones están escritos en los ejercicios. Toca a volumen bajo.",
    "Aprenderé a medir un patrón rítmico con figuras (negra, blanca, redonda…) y a decir cuántos pulsos tiene cada compás y dónde cae el acento. Sirve para describir un ritmo con precisión y tocarlo sin perderme.",
    ["Sé que el pulso es el latido parejo de la música.", "Sé que el acento es el pulso que se marca más fuerte.", "Sé sumar números de uno y dos dígitos."],
    [
        "El pulso es el latido parejo de la música, como tus pasos al caminar. Los pulsos se agrupan en compases, que son grupos del mismo tamaño separados por barras de compás. El primer pulso de cada compás lleva el acento principal. En una partitura el compás se escribe como 2/4, 3/4 o 4/4: el número de arriba dice cuántos pulsos tiene cada compás.",
        f"La duración de cada sonido se escribe con una figura. Con la leyenda de la clase ({LEY}), una negra dura 1 pulso y una blanca dura 2. Para saber si un patrón llena un compás, se suma lo que dura cada figura, y los silencios también cuentan porque ocupan tiempo aunque no suenen.",
        f"Un patrón rítmico es una secuencia de sonidos y silencios que se repite sobre el pulso. Por ejemplo, {P(*PA)} dura 1 + 1 + 2 = {pulses(*PA)} pulsos y llena un compás de 4/4. Si la suma es mayor que el compás, el patrón se pasa; si es menor, falta una figura para completarlo.",
    ],
    [("compás", "grupo de pulsos del mismo tamaño, separado por barras de compás"), ("acento", "pulso que se marca más fuerte; el principal es el primero del compás"), ("figura", "signo que indica cuánto dura un sonido"), ("patrón rítmico", "secuencia de sonidos y silencios que se repite"), ("2/4, 3/4, 4/4", "compases de 2, 3 y 4 pulsos")],
    [
        ("Ver si llena el compás", f"¿El patrón {P(BLA, NEG, CC, SN)} llena un compás de 4 pulsos?", ["Blanca = 2 pulsos, negra = 1, 2 corcheas = 1 y silencio de negra = 1.", "2 + 1 + 1 + 1 = 5 pulsos, más que 4."], "No: tiene 5 pulsos y sobra 1"),
        ("Ubicar acentos", "Cuento 18 pulsos en compases de 3. ¿En qué números cae el acento principal?", ["Los compases son 1-2-3, 4-5-6, 7-8-9, 10-11-12, 13-14-15 y 16-17-18.", "El acento va en el primer pulso de cada compás."], "En los pulsos 1, 4, 7, 10, 13 y 16"),
    ],
    [
        ("Creer que el acento cae en cualquier pulso del compás.", "El acento principal va en el primer pulso, no al azar.", "Marca fuerte el 1 de cada compás y suaves los demás."),
        ("Contar solo cuántas figuras hay y olvidar cuánto dura cada una.", "Una blanca es una figura pero dura 2 pulsos.", "Suma los pulsos que dura cada figura, silencios incluidos."),
    ],
    [
        ex("En un compás 2/4, ¿cuántos pulsos hay y cuántos llevan acento principal?", "2 pulsos y 1 con acento principal", "El número de arriba es 2 y solo el primer pulso lleva el acento principal."),
        ex("¿Cuántos pulsos dura una blanca según la leyenda de la clase?", "2", "La leyenda dice que la blanca equivale a 2 pulsos."),
        ex("Cuentas 8 pulsos en compases de 4. ¿En qué números cae el acento principal?", "En 1 y 5", "Hay dos compases, 1-2-3-4 y 5-6-7-8, y el acento va en el primer pulso de cada uno."),
    ],
    [
        ex(f"¿Cuántos pulsos ocupa el patrón {P(*PB)}?", str(pulses(*PB)), "La blanca con puntillo dura 3 pulsos y la negra suma 1."),
        ex(f"¿Cabe exactamente en un compás de 3/4 el patrón {P(BLA, NEG)}? Responde sí o no.", "Sí", "La blanca dura 2 pulsos y la negra 1: suman 3."),
        ex("Un compás de 3/4 lleva una redonda. ¿Cabe en él?", "No: la redonda dura 4 pulsos y el compás tiene 3", "El compás de 3/4 tiene 3 pulsos y la redonda ocupa 4."),
    ],
    [
        arith(f"En un compás 3/4 suena {P(NEG, CC, NEG)} y en el siguiente {P(BLA, NEG)}. ¿Cuántos pulsos hay entre los dos compases?", f"{pulses(NEG, CC, NEG)}+{pulses(BLA, NEG)}", "Se suman los pulsos de cada compás.", " pulsos"),
        arith("Una pieza en 4/4 dura 20 pulsos. ¿Cuántos compases completos tiene?", "20//4", "Cada compás tiene 4 pulsos y se reparten los 20.", " compases"),
        ex(f"El compás de 4/4 tiene escrito {P(BP)} y le falta una figura para completarse. ¿Cuánto debe durar la que falta?", "1 pulso (una negra o un silencio de negra)", "La blanca con puntillo ocupa 3 pulsos y faltan 4 − 3 = 1."),
    ],
    [
        ex(f"Pedro dice que {P(*PD)} cabe en un compás de 4 pulsos porque solo tiene 2 figuras. ¿Cuántos pulsos ocupa realmente?", str(pulses(*PD)), "La blanca (2) más la blanca con puntillo (3) dan 5: se cuentan pulsos, no figuras."),
        ex("Un patrón dura 6 pulsos y se reparte en compases completos iguales. ¿En cuál de 2/4, 3/4 o 4/4 no se puede repartir sin que sobre o falte?", "En 4/4", "6 se reparte en 3 compases de 2 y en 2 compases de 3, pero en 4/4 sobrarían 2 pulsos."),
    ],
    [
        ex(f"En el patrón {P(*PE)} cuenta cuántos sonidos se oyen en total (los silencios no suenan).", str(sounds(*PE)), "Cada 2 corcheas son 2 sonidos (2 + 2), la negra suma 1 y el silencio no suena."),
        arith("Una pieza tiene 11 compases de 3 pulsos y otra tiene 8 compases de 4 pulsos. ¿Cuántos pulsos más tiene la primera?", "11*3-8*4", "La primera tiene 33 pulsos y la segunda 32; se restan.", " pulso más"),
    ],
    [ex("Un vals se baila en compás de 3/4 y una versión dura 30 compases. ¿Cuántos pulsos tiene y cuántos llevan el acento principal?", "90 pulsos y 30 con acento principal", "30 compases × 3 pulsos = 90, y hay un acento principal por compás.")],
    [ex("¿Cómo se llama la línea que separa un compás de otro?", "Barra de compás", "Esa línea vertical marca dónde termina un compás."), ex("¿Cuántos pulsos dura una redonda?", "4", "La leyenda la define con 4 pulsos."), ex("¿Qué indica el 3 de arriba en un compás 3/4?", "Que cada compás tiene 3 pulsos", "El número de arriba cuenta los pulsos por compás.")],
    (
        f"Camina en tu lugar con paso parejo y cuenta de a 4 (1-2-3-4), pisando más fuerte en el 1. Palmea el patrón {P(BLA, NEG, NEG)} cuatro veces seguidas. Escribe cuántos pulsos tiene un compás, cuántos pulsos palmeaste en total y marca con una X en qué pulsos pisaste fuerte.",
        "Un compás tiene 4 pulsos (2 + 1 + 1). Palmeé 4 compases: 16 pulsos. Pisé fuerte en los pulsos 1, 5, 9 y 13: X – – – X – – – X – – – X – – –.",
        ["mantiene el paso parejo", "marca fuerte solo el primer pulso de cada compás", "escribe los conteos correctos"],
        ["interpretación", "conteo escrito"],
        ["marcar fuerte pulsos que no son el primero", "contar la blanca como 1 pulso"],
        "Reconoce el pulso estable y pide mostrar con el dedo dónde empieza cada compás y cuánto dura la blanca.",
    ),
    "Cuenta de a 3 hasta 15 pisando fuerte en cada 1 y di cuántos pasos fuertes diste.",
    "Escribe un compás de 4 pulsos que use 2 corcheas, blanca y un silencio, y comprueba con una suma que dura 4 pulsos.",
)

# ---------------------------------------------------------------- OA 01 · clase 2 (patrones melódicos, diseños y secuencia)
MA, MB, MC, ME = (3, 4, 5, 5, 4, 3, 2, 3), (1, 3, 5, 3, 1, 5, 3), (8, 7, 6, 5, 5, 4, 3, 1), (5, 6, 5, 4, 3, 4, 5)
MW = (2, 3, 4, 6, 5, 3)

L(
    OA1, 2,
    f"Lápiz y papel. Escala de números: {NOTAS}. Si tienes un metalófono, una flauta o un teclado puedes tocar las melodías, pero no es necesario: todas están escritas con números. Cuida el volumen.",
    "Aprenderé a describir una melodía por su diseño (si sube, baja o repite; si avanza por grados o da saltos) y a reconocer patrones melódicos que vuelven. Sirve para explicar cómo es una melodía sin cantarla.",
    ["Sé que una melodía es una sucesión de sonidos de distinta altura.", "Sé ordenar los números del 1 al 8.", "Sé restar números pequeños."],
    [
        f"Una melodía se puede escribir con números: {NOTAS}. Mientras más alto el número, más agudo el sonido. El diseño melódico es la forma que dibuja la melodía: cada paso puede subir, bajar o repetir la nota. Si la nota cambia al número vecino (de 4 a 5) es un paso por grado; si se salta uno o más números (de 4 a 6) es un salto.",
        "El contorno de toda la melodía puede ser ascendente (sube casi siempre), descendente (baja casi siempre), en arco (sube y luego baja) u ondulado (sube y baja varias veces). El rango es la distancia entre la nota más grave y la más aguda; se calcula restando. Una melodía de grados suena suave y una con muchos saltos suena más abierta.",
        f"Un motivo es una idea melódica corta. Si el motivo vuelve empezando en otra nota, se llama secuencia. Por ejemplo, {N(1, 2, 3)} y luego {N(2, 3, 4)} forman una secuencia: el motivo subió un grado. Reconocer el diseño y los motivos permite explicar por qué una melodía suena como suena.",
    ],
    [("diseño melódico", "forma que dibuja la melodía: sube, baja o repite"), ("grado y salto", "grado: a la nota vecina; salto: cambia dos o más números"), ("contorno", "forma general de la melodía: ascendente, descendente, en arco u ondulado"), ("rango", "distancia entre la nota más grave y la más aguda"), ("motivo y secuencia", "idea corta; y esa idea repetida desde otra nota")],
    [
        ("Describir el diseño", f"Describe la melodía {N(*MW)}: ¿cuántos saltos tiene y cuál es su rango?", ["Pares: 2→3 grado, 3→4 grado, 4→6 salto, 6→5 grado, 5→3 salto.", "Hay 2 saltos. La nota más grave es 2 y la más aguda es 6.", "Rango: 6 − 2 = 4."], "2 saltos y rango 4"),
        ("Continuar una secuencia", f"El motivo {N(5, 4, 3)} vuelve como {N(4, 3, 2)}. Si sigue la secuencia, ¿cuál es el tercer motivo?", ["El motivo bajó un grado: de 5-4-3 a 4-3-2.", "Bajamos otro grado cada nota: 3-2-1."], "3-2-1"),
    ],
    [
        ("Pensar que un número mayor es una nota más grave.", "Mientras más alto el número, más agudo el sonido.", "El 8 es el más agudo y el 1 el más grave."),
        ("Llamar salto a un paso de 5 a 6.", "Un salto se salta por lo menos un número; de 5 a 6 son notas vecinas.", "Si son vecinas es grado; si hay un número en medio, es salto."),
    ],
    [
        ex("¿Qué nota es el 6 en la escala de la clase?", "La", "Según la escala, 6 = la."),
        ex(f"En la melodía {N(*MA)}, ¿con qué número termina?", "3", "El último número escrito es 3."),
        ex(f"En la melodía {N(*MC)}, el paso de 5 a 5, ¿sube, baja o repite?", "Repite", "Es la misma nota dos veces."),
    ],
    [
        ex(f"Cuenta cuántos saltos (pasos de dos o más números) hay en la melodía {N(*MB)}.", str(leaps(MB)), "Todos los pasos de esa melodía se saltan al menos un número, y son 6 pasos."),
        ex(f"Cuenta cuántas veces repite la nota la melodía {N(*MA)}.", str(moves(MA).count("repite")), "Solo repite en el paso 5→5."),
        ex(f"¿Cuál es la nota más aguda de la melodía {N(*ME)}?", "6", "Es el mayor número de la lista."),
    ],
    [
        arith(f"La melodía {N(*MC)} parte en 8 y llega a 1 como nota más grave. ¿Cuál es su rango?", "8-1", "El rango es la resta entre la nota más aguda y la más grave.", ""),
        ex(f"La melodía {N(1, 2, 3, 2, 3, 4, 3, 4, 5)} repite una idea de tres notas desde un grado más arriba cada vez. ¿Qué recurso es: secuencia o salto?", "Secuencia", "El motivo 1-2-3 vuelve empezando en 2 y luego en 3."),
        ex(f"Si la secuencia sigue subiendo un grado cada vez, ¿cuál es el motivo que viene después de {N(1, 3, 5)}?", "2-4-6", "Cada nota del motivo sube un número."),
    ],
    [
        ex(f"Ana dice que la melodía {N(*MC)} es ascendente. ¿Tiene razón?", "No: baja casi siempre, es descendente", "Parte en 8 y va bajando hasta 1; solo repite el 5."),
        ex("Una melodía baja de 8 a 1 de un grado a la vez. ¿Cuántos pasos da?", "7", "Pasa por 8 notas distintas y entre ellas hay 7 pasos."),
    ],
    [
        ex(f"Describe el contorno de {N(*ME)}: ¿ascendente, descendente, en arco u ondulado?", "Ondulado", "Sube a 6, baja a 3 y vuelve a subir a 5: cambia de dirección varias veces."),
        arith("Una melodía tiene 4 compases con 2 saltos en cada uno. Una segunda tiene 3 compases con 3 saltos en cada uno. ¿Cuántos saltos más tiene la segunda?", "3*3-4*2", "La primera tiene 8 saltos y la segunda 9; se restan.", " salto más"),
    ],
    [ex("Una canción de cuna baja suave de a un grado: 5-4-3-2-1. ¿Qué diseño tiene: baja por grados o sube con saltos?", "Baja por grados", "Cada paso baja a la nota vecina.")],
    [ex("¿Qué muestra el diseño melódico de una melodía?", "Cómo sube, baja o repite", "Describe la forma de la línea de notas."), ex("En la escala de la clase, ¿qué número corresponde a do?", "1", "La escala dice 1 = do."), ex("Un paso de 3 a 6, ¿es grado o salto?", "Salto", "Se saltan el 4 y el 5.")],
    (
        "Inventa una melodía de 7 números del 1 al 6 que parta en 2, termine en 2 y tenga exactamente 3 saltos. Escríbela, marca los saltos, escribe su nota más aguda, su rango y su contorno. Si tienes un instrumento melódico, tócala despacio; si no, cántala con «la».",
        "Melodía 2-4-5-3-1-2-2: los saltos son 2→4, 5→3 y 3→1 (son 3); 4→5 y 1→2 son grados y el último paso repite. La nota más aguda es 5, el rango es 5 − 1 = 4 y el contorno es en arco (sube a 5 y baja a 1).",
        ["parte y termina en 2", "usa 7 números del 1 al 6", "marca los saltos y calcula el rango"],
        ["melodía escrita", "saltos marcados"],
        ["contar un paso por grado como salto", "no cerrar en 2"],
        "Reconoce la melodía y pide contar los saltos paso por paso: si la diferencia entre dos notas vecinas es 2 o más, es salto.",
    ),
    "Escribe una melodía de 5 números que solo suba por grados y di su rango.",
    "Escribe un motivo de 3 notas y repítelo tres veces en secuencia, cada vez un grado más agudo.",
)

# ---------------------------------------------------------------- OA 01 · clase 3 (reiteración, contraste, variación, pregunta-respuesta)
F1, F2, F3, F4 = (3, 3, 4, 5), (3, 3, 4, 5), (5, 4, 3, 1), (3, 3, 4, 3)

L(
    OA1, 3,
    "Lápiz y papel. Las frases están escritas con números de la escala de la clase anterior (1 = do … 8 = do agudo) y se pueden cantar con «la» o tocar en un instrumento melódico, pero no es necesario. Cuida el volumen.",
    "Aprenderé a describir cómo se organiza una música: qué frase se repite igual (reiteración), cuál es distinta (contraste), cuál cambia un poco (variación) y cuál pregunta y cuál responde. Sirve para explicar por qué una música se siente ordenada y variada.",
    ["Sé que una melodía se escribe con números.", "Sé comparar dos listas de números y ver qué cambió.", "Sé que una frase es un trozo de música con sentido, como una oración."],
    [
        "Una frase musical es un trozo de música con sentido, como una oración. Cuando una frase vuelve exactamente igual hay reiteración. Cuando aparece una frase distinta en notas, ritmo o dirección hay contraste. Cuando vuelve casi igual pero cambia algo (una nota, el ritmo, el final) hay variación. Reiteración da sensación de orden; contraste da novedad; variación mezcla las dos cosas.",
        f"Para decidir, compara frase con frase. Si {N(3, 3, 4, 5)} aparece otra vez igual, es reiteración. Si aparece {N(3, 3, 4, 3)}, cambió una de cuatro notas: es variación. Si aparece {N(5, 4, 3, 1)}, que baja mientras la primera sube, es contraste. Una buena descripción nombra el recurso y da la evidencia: qué se mantiene y qué cambia.",
        "Las frases también pueden dialogar. En una pregunta-respuesta, la primera frase (pregunta) termina en una nota que queda abierta, y la segunda (respuesta) termina en una nota de reposo. En esta clase usaremos la regla: la pregunta termina en 5 y la respuesta termina en 1, que es la nota de descanso.",
    ],
    [("reiteración", "una frase que vuelve exactamente igual"), ("contraste", "una frase distinta de la anterior"), ("variación", "una frase que vuelve casi igual, con algún cambio"), ("pregunta y respuesta", "dos frases que dialogan: una queda abierta y la otra descansa"), ("frase", "trozo de música con sentido, como una oración")],
    [
        ("Clasificar una frase", f"La frase 1 es {N(2, 2, 3, 4)} y la frase 2 es {N(2, 2, 3, 2)}. ¿Es reiteración, contraste o variación?", ["Comparo nota por nota: 2=2, 2=2, 3=3, pero 4≠2.", "Cambia solo la última nota, así que vuelve casi igual."], "Variación"),
        ("Preguntar y responder", f"La frase {N(1, 3, 4, 5)} es una pregunta porque termina en 5. ¿Cuál sirve de respuesta: {N(4, 3, 2, 1)} o {N(4, 3, 2, 5)}?", ["La respuesta debe terminar en 1.", "La primera termina en 1; la segunda termina en 5 y quedaría abierta."], f"{N(4, 3, 2, 1)}"),
    ],
    [
        ("Llamar contraste a toda frase que no es idéntica.", "Si cambia solo un poco y se reconoce la idea, es variación, no contraste.", "Cuenta cuántas notas coinciden: si coinciden casi todas, es variación."),
        ("Describir con «me gusta» o «suena lindo» sin decir qué se oye.", "Una descripción necesita evidencia audible: notas, ritmo o dirección.", "Di qué se repite y qué cambia."),
    ],
    [
        ex("Dos frases iguales seguidas, ¿son reiteración, contraste o variación?", "Reiteración", "La frase vuelve exactamente igual."),
        ex("Una frase sube y la siguiente baja con otras notas. ¿Qué recurso hay entre ellas?", "Contraste", "Las dos frases son distintas en dirección y en notas."),
        ex("Una frase vuelve igual pero cambia solo su última nota. ¿Qué recurso es?", "Variación", "Se reconoce la idea, con un cambio pequeño."),
    ],
    [
        ex(f"Una pieza tiene cuatro frases: F1 {N(*F1)}, F2 {N(*F2)}, F3 {N(*F3)} y F4 {N(*F4)}. ¿Qué frase repite exactamente a F1?", "F2", "F2 tiene los mismos cuatro números, en el mismo orden."),
        ex(f"En esa pieza (F1 {N(*F1)}, F3 {N(*F3)}), ¿qué hay entre F1 y F3: reiteración, contraste o variación?", "Contraste", "F1 sube y F3 baja, y ninguna nota coincide en su lugar."),
        ex(f"En esa pieza, ¿qué es F4 {N(*F4)} respecto de F1 {N(*F1)}?", "Variación", f"Coinciden {len(F1) - diff(F1, F4)} de 4 notas y cambia solo la última."),
    ],
    [
        ex(f"¿Cuántas frases de la pieza (F1 {N(*F1)}, F2 {N(*F2)}, F3 {N(*F3)}, F4 {N(*F4)}) empiezan con 3-3-4?", "3", "Empiezan así F1, F2 y F4; F3 empieza en 5."),
        ex(f"La frase {N(1, 2, 3, 5)}, ¿es pregunta o respuesta según la regla de la clase?", "Pregunta", "Termina en 5, que deja la frase abierta."),
        arith("Cada frase de una pieza dura 2 compases de 4 pulsos. Si la pieza tiene 4 frases, ¿cuántos pulsos dura en total?", "4*2*4", "Hay 4 frases × 2 compases × 4 pulsos.", " pulsos"),
    ],
    [
        ex(f"Ana dice que {N(3, 3, 4, 3)} es un contraste de {N(3, 3, 4, 5)} porque no son iguales. ¿Qué responderías?", "Que es una variación: coinciden 3 de las 4 notas", "Se reconoce la idea de la frase y cambia solo la última nota."),
        ex(f"Una pregunta termina en 5. ¿Cuál es una respuesta adecuada con la regla de la clase: (a) {N(4, 3, 2, 5)} o (b) {N(4, 3, 2, 1)}?", "(b)", "La respuesta debe terminar en 1, la nota de reposo."),
    ],
    [
        ex("Una pieza tiene seis frases: a (1-2-3), a igual (1-2-3), b (5-4-3), a con la última nota cambiada (1-2-4), a igual (1-2-3), b igual (5-4-3). ¿Cuántas frases son reiteración exacta de la primera?", "2", "Son la segunda y la quinta; la cuarta cambió la última nota y es variación."),
        ex(f"Compara {N(2, 3, 4, 5)} con {N(2, 3, 4, 4)}. ¿Cuántas notas cambian?", str(diff((2, 3, 4, 5), (2, 3, 4, 4))), "Solo la última nota pasa de 5 a 4."),
    ],
    [ex("En una canción el coro vuelve igual tres veces y las estrofas entre medio tienen otra melodía. ¿Qué recurso es el coro y cuál son las estrofas respecto del coro?", "El coro es reiteración y las estrofas son contraste", "El coro vuelve exactamente igual; las estrofas traen una melodía distinta.")],
    [ex("¿Cómo se llama una frase que vuelve casi igual con un cambio?", "Variación", "Se mantiene la idea y cambia algo."), ex("¿En qué nota termina una pregunta según la regla de la clase?", "5", "Queda abierta en el 5."), ex("¿Qué debe incluir una buena descripción además del nombre del recurso?", "La evidencia: qué se mantiene y qué cambia", "Describir con evidencia audible es el criterio de la clase.")],
    (
        f"Mira esta pieza: F1 {N(1, 2, 3, 1)}, F2 {N(1, 2, 3, 1)}, F3 {N(5, 5, 4, 2)}, F4 {N(1, 2, 3, 3)}. Escribe para F2, F3 y F4 si son reiteración, contraste o variación respecto de F1, y justifica cada una con lo que se mantiene y lo que cambia. Si puedes, cántala con «la» marcando cada frase con la mano.",
        "F2 es reiteración: es idéntica a F1. F3 es contraste: usa notas distintas y baja de 5 a 2. F4 es variación: mantiene 1-2-3 y cambia la última nota de 1 a 3.",
        ["nombra bien el recurso de cada frase", "da evidencia (qué se mantiene y qué cambia)", "no usa solo «me gusta»"],
        ["tabla de frases", "justificaciones escritas"],
        ["llamar contraste a la variación", "no dar evidencia"],
        "Reconoce el análisis y pide mostrar con el dedo nota por nota qué coincide con F1.",
    ),
    "Escribe una frase de 4 números y luego una variación que cambie solo una nota.",
    "Escribe una pregunta de 4 notas que termine en 5 y dos respuestas distintas que terminen en 1.",
)

# ---------------------------------------------------------------- OA 01 · clase 4 (dinámica, tempo y propósito expresivo)
DIN = "pp = muy suave; p = suave; mp = medio suave; mf = medio fuerte; f = fuerte; ff = muy fuerte"
TEM = "lento = 70 pulsos por minuto o menos; moderado = de 71 a 110; rápido = 111 o más (rangos de referencia de esta clase)"
_ORDEN = ["pp", "p", "mp", "mf", "f", "ff"]

L(
    OA1, 4,
    f"Lápiz y papel. Dinámicas: {DIN}. Tempos: {TEM}. Para practicar puedes marcar el pulso con palmas suaves y probar lento, moderado y rápido. Cuida el volumen.",
    "Aprenderé a describir la dinámica (qué tan fuerte o suave suena) y el tempo (qué tan rápido va el pulso), y a explicar para qué los usa la música: calma, tensión, alegría, sorpresa. Sirve para describir el propósito expresivo con evidencia.",
    ["Sé que el pulso es el latido parejo de la música.", "Sé que un sonido puede ser fuerte o suave.", "Sé multiplicar y dividir números pequeños."],
    [
        f"La dinámica es lo fuerte o suave que suena la música. Se escribe con letras: {DIN}. De la más suave a la más fuerte el orden es pp, p, mp, mf, f, ff. Si la música aumenta poco a poco hay un crescendo, y si disminuye poco a poco hay un diminuendo. Un cambio brusco de suave a fuerte se oye como sorpresa.",
        f"El tempo es la velocidad del pulso, y se mide en pulsos por minuto. En esta clase usamos tres rangos de referencia: {TEM}. Si el tempo aumenta poco a poco hay un accelerando, y si disminuye poco a poco hay un ritardando. Con el tempo se calcula cuánto dura una pieza: a 60 pulsos por minuto, cada pulso dura 1 segundo.",
        "Dinámica y tempo no se eligen al azar: tienen un propósito expresivo, es decir, comunican algo. Un tempo lento con dinámica p suele comunicar calma o ternura; un tempo rápido con dinámica f suele comunicar energía o fiesta; un crescendo prepara una llegada importante. Una buena descripción nombra el recurso y dice qué efecto produce.",
    ],
    [("dinámica", "qué tan fuerte o suave suena la música"), ("crescendo y diminuendo", "aumentar o disminuir el volumen poco a poco"), ("tempo", "velocidad del pulso, en pulsos por minuto"), ("accelerando y ritardando", "acelerar o frenar el tempo poco a poco"), ("propósito expresivo", "lo que la música quiere comunicar con sus recursos")],
    [
        ("Ordenar dinámicas", "Ordena de la más suave a la más fuerte: f, p, ff, mf.", ["Según la lista: p es suave, mf medio fuerte, f fuerte, ff muy fuerte.", "El orden es p, mf, f, ff."], "p, mf, f, ff"),
        ("Duración con el tempo", "Una pieza tiene 90 pulsos y se toca a 90 pulsos por minuto. ¿Cuántos segundos dura?", ["A 90 pulsos por minuto, 90 pulsos duran 1 minuto.", "1 minuto = 60 segundos."], "60 segundos"),
    ],
    [
        ("Creer que f significa «rápido».", "f habla de la fuerza del sonido, no de la velocidad; la velocidad es el tempo.", "Dinámica = fuerte/suave; tempo = rápido/lento."),
        ("Decir «va bonito» sin nombrar el recurso.", "Describir es nombrar el recurso y su efecto.", "Di, por ejemplo, «tempo lento y p: comunica calma»."),
    ],
    [
        ex("¿Qué indica pp?", "Muy suave", "Según la lista de dinámicas, pp = muy suave."),
        ex("Si la música sube de volumen poco a poco, ¿hay crescendo o diminuendo?", "Crescendo", "Crescendo es aumentar poco a poco."),
        ex("Una pieza va a 60 pulsos por minuto. ¿En qué rango de la clase está?", "Lento", "60 es menor que 70, el máximo de lento."),
    ],
    [
        ex("¿Cuál es más fuerte, mf o mp?", "mf", "En el orden pp, p, mp, mf, f, ff, mf viene después de mp."),
        ex("¿En qué rango de la clase está un tempo de 120 pulsos por minuto?", "Rápido", "120 es mayor que 110."),
        ex("Un cuento musical pasa de un suave p a un fuerte ff en un solo golpe. ¿Qué efecto expresivo busca más probablemente: sorpresa o calma?", "Sorpresa", "Un cambio brusco de suave a muy fuerte sorprende."),
    ],
    [
        arith("Una marcha va a 120 pulsos por minuto y suena 60 pulsos. ¿Cuántos segundos dura?", "60*60//120", "A 120 pulsos por minuto cada pulso dura medio segundo: 60 pulsos × 60 s ÷ 120.", " segundos"),
        ex("Ordena de menor a mayor fuerza: mf, pp, f, p.", "pp, p, mf, f", "Se ordenan según la lista pp, p, mp, mf, f, ff."),
        arith("Una canción de cuna tiene 96 pulsos y va a 48 pulsos por minuto. ¿Cuántos segundos dura?", "96*60//48", "A 48 por minuto, 48 pulsos duran un minuto, así que 96 pulsos duran 2 minutos (120 segundos).", " segundos"),
    ],
    [
        ex("Marta dice que una pieza en p va lenta porque suena suave. ¿Tiene razón?", "No: p es dinámica (suave) y el tempo puede ser rápido", "Dinámica y tempo son dos recursos distintos."),
        ex("Una pieza comienza en p y termina en f con un crescendo continuo. ¿Cuántas dinámicas hay entre p y f en el orden de la clase, sin contarlas a ellas?", "2", "Entre p y f están mp y mf."),
    ],
    [
        ex("Una pieza va a 100 pulsos por minuto en dinámica mf y al final hace ritardando y diminuendo. ¿Qué efecto tiene el final: cierre tranquilo o arranque enérgico?", "Cierre tranquilo", "Frenar y bajar el volumen deja la sensación de terminar y calmarse."),
        arith("Si una pieza de 160 pulsos va a 80 pulsos por minuto y otra, también de 160 pulsos, va a 160, ¿cuántos segundos más dura la que va a 80 pulsos por minuto?", "160*60//80-160*60//160", "La primera dura 120 s y la segunda 60 s; se restan.", " segundos más"),
    ],
    [ex("Para una escena de un cuento donde un gato se acerca despacio sin hacer ruido, ¿qué combinación expresa mejor: tempo lento con p o tempo rápido con ff?", "Tempo lento con p", "Lento y suave comunican cuidado y silencio.")],
    [ex("¿Qué es el tempo?", "La velocidad del pulso", "Se mide en pulsos por minuto."), ex("¿Cómo se llama frenar el tempo poco a poco?", "Ritardando", "Es lo contrario de accelerando."), ex("¿Qué letra de dinámica significa fuerte?", "f", "En la lista de la clase f = fuerte.")],
    (
        "Lee este esquema y descríbelo: «Compases 1-4: p, tempo lento. Compases 5-8: crescendo y accelerando. Compases 9-12: ff, tempo rápido. Compases 13-14: diminuendo y ritardando.» Escribe qué hace la música en cada parte y qué propósito expresivo crees que tiene el conjunto (por ejemplo, qué historia podría contar). Si quieres, marca el pulso con palmas y practica cada parte.",
        "Parte 1: suave y lenta, calma. Parte 2: sube el volumen y acelera, crece la tensión. Parte 3: muy fuerte y rápido, momento de más energía. Parte 4: baja y frena, vuelve la calma. Podría contar un amanecer: el pueblo despierta, la fiesta llega a su punto más alto y la noche vuelve a calmarse.",
        ["nombra la dinámica y el tempo de cada parte", "usa crescendo, accelerando, diminuendo o ritardando bien", "explica un propósito expresivo con evidencia"],
        ["descripción escrita", "palmas practicadas"],
        ["confundir dinámica con tempo", "describir sin evidencia"],
        "Reconoce la descripción y pide señalar en el esquema qué compases justifican el propósito dicho.",
    ),
    "Practica marcar el pulso lento, moderado y rápido con palmas suaves.",
    "Escribe un esquema de 3 partes con dinámica y tempo que cuente la historia de una tormenta que llega y se va.",
)

# ---------------------------------------------------------------- OA 01 · clase 5 (secciones A-AB-ABA y texturas)
L(
    OA1, 5,
    "Lápiz y papel. Todas las piezas son esquemas escritos en los ejercicios con letras de sección y descripciones de instrumentos y voces. Si quieres, representa las texturas con tu voz y golpes suaves sobre una mesa. Cuida el volumen.",
    "Aprenderé a describir una música por sus secciones (A, AB, ABA y otras formas) y por su textura (cuántas capas suenan a la vez). Sirve para explicar cómo está armada una pieza completa.",
    ["Sé que una frase puede repetirse o cambiar.", "Sé que hay instrumentos melódicos y de percusión.", "Sé sumar y restar números pequeños."],
    [
        "Una sección es una parte grande de la pieza. Se nombran con letras: A es la primera idea y B una idea distinta. Si la pieza tiene una sección A y luego una B, su forma es AB. Si después de B vuelve A, la forma es ABA. También hay otras formas, como AABA o ABAC, según cuántas veces vuelve cada sección. Una sección que vuelve cambiada se escribe con una marca, por ejemplo A'.",
        "La textura es cuántas capas de sonido suenan a la vez y cómo se relacionan. Hay tres texturas principales. En una sola melodía hay una única línea, sin acompañamiento. En una melodía con acompañamiento, una voz canta la melodía y otras tocan acordes o ritmos de fondo. En una textura polifónica suenan dos o más melodías a la vez, como en un canon, donde una voz imita a otra unos compases después.",
        "Para describir una pieza se dicen las dos cosas: la forma y la textura de cada sección. Por ejemplo, «forma ABA: A es una melodía sola y B es una melodía con acompañamiento, y al final vuelve A como al comienzo». Eso permite explicar el propósito: A da calma, B da más energía y el regreso de A da sensación de cierre.",
    ],
    [("sección", "parte grande de una pieza, nombrada con una letra"), ("forma AB / ABA", "pieza con dos secciones distintas; o con una que vuelve al final"), ("textura", "cuántas capas de sonido suenan a la vez y cómo se relacionan"), ("melodía con acompañamiento", "una melodía principal con otras voces de fondo"), ("polifonía y canon", "varias melodías a la vez; en el canon una imita a otra")],
    [
        ("Hallar la forma", "Una pieza tiene esta estructura: primera parte flauta sola; segunda parte guitarra y bombo con ritmo distinto; tercera parte flauta sola, igual que la primera. ¿Qué forma tiene?", ["La primera parte es A.", "La segunda es distinta, B.", "La tercera vuelve A: A, B, A."], "ABA"),
        ("Reconocer la textura", "Una cantante canta la melodía mientras un guitarrista toca acordes de fondo. ¿Qué textura hay?", ["Hay una melodía principal.", "Otra voz acompaña con acordes de fondo."], "Melodía con acompañamiento"),
    ],
    [
        ("Pensar que la forma ABA tiene tres secciones distintas.", "En ABA la tercera es la A que vuelve; solo hay dos ideas distintas.", "Cuenta las ideas distintas, no las partes."),
        ("Decir polifonía cada vez que suenan muchos instrumentos.", "La polifonía exige varias melodías a la vez; si todos tocan la misma melodía no lo es.", "Pregunta cuántas melodías distintas suenan a la vez."),
    ],
    [
        ex("Una pieza tiene una sección A y luego una sección B distinta. ¿Qué forma tiene?", "AB", "Dos secciones distintas, una después de la otra."),
        ex("Una voz canta sola, sin ningún acompañamiento. ¿Cuántas melodías suenan a la vez?", "1", "Una voz sola es una única melodía."),
        ex("Dos voces cantan melodías distintas al mismo tiempo. ¿Qué textura hay: polifonía o melodía sola?", "Polifonía", "Hay más de una melodía a la vez."),
    ],
    [
        ex("Una pieza va A, B, A, C. ¿Cuántas ideas distintas tiene?", "3", "Las ideas distintas son A, B y C; A se repite."),
        ex("Una pieza va AABA. ¿Cuántas veces suena la sección A?", "3", "Aparece en la primera, segunda y cuarta parte."),
        ex("Una ronda donde una voz empieza una melodía y otro grupo la repite 4 compases después. ¿Cómo se llama esa imitación?", "Canon", "Una voz imita a la otra con un desfase."),
    ],
    [
        arith("Cada sección de una pieza ABA dura 8 compases. ¿Cuántos compases dura la pieza completa?", "3*8", "Son tres secciones de 8 compases.", " compases"),
        arith("En una pieza AABA, A dura 8 compases y B dura 4. ¿Cuántos compases tiene en total?", "3*8+4", "Tres veces A y una vez B.", " compases"),
        ex("La sección B de una pieza tiene flauta, tambor y guitarra, y solo la flauta toca la melodía. ¿Qué textura tiene B?", "Melodía con acompañamiento", "Una melodía principal y el resto acompaña."),
    ],
    [
        ex("Carla dice que una pieza ABA tiene tres secciones distintas. ¿Cuántas ideas distintas tiene realmente?", "2", "La tercera sección es A que vuelve."),
        ex("Un grupo toca todos la misma melodía a la vez, a distintos volúmenes. ¿Es polifonía? Responde sí o no.", "No", "Hay una sola melodía, aunque la toquen varios."),
    ],
    [
        ex("Una pieza va A (8 compases, flauta sola, tempo 100), B (8 compases, flauta con guitarra) y A' (8 compases, flauta sola, tempo 70, misma melodía). ¿Qué cambió en A' respecto de A?", "El tempo", "La melodía y la textura son las mismas; solo cambia la velocidad del pulso de 100 a 70."),
        arith("Una pieza tiene 4 secciones: A de 8 compases, B de 8, A de 8 y C de 4. Cada compás tiene 3 pulsos. ¿Cuántos pulsos tiene?", "(8+8+8+4)*3", "Se suman los compases y se multiplica por los pulsos de cada compás.", " pulsos"),
    ],
    [ex("Una canción tiene un verso que suena dos veces igual, un puente distinto y el mismo verso al final. ¿Qué forma tiene?", "AABA", "Verso, verso, puente distinto y verso otra vez: AABA.")],
    [ex("En una pieza musical, ¿cómo se llama cada parte grande que se señala con una letra?", "Sección", "A, B y las demás letras nombran secciones."), ex("¿Qué textura tiene una melodía con acordes de fondo?", "Melodía con acompañamiento", "Hay una principal y otra de fondo."), ex("¿Qué letra se usa para la segunda idea distinta?", "B", "A es la primera y B la segunda distinta.")],
    (
        "Describe esta pieza con forma y textura: «Primera parte (6 compases): un xilófono toca una melodía lenta, solo. Segunda parte (6 compases): el xilófono sigue y se suman tambor y maracas con ritmo parejo. Tercera parte (6 compases): vuelve el xilófono solo, igual que al principio.» Escribe la forma, la textura de cada sección, cuántos compases tiene en total y qué propósito expresivo crees que tiene el regreso de la primera parte.",
        "Forma ABA. Sección A: una melodía sola; sección B: melodía con acompañamiento (tambor y maracas); sección A: una melodía sola otra vez. Total: 18 compases. El regreso de A da sensación de cierre y vuelta a la calma después de la parte más energética.",
        ["escribe la forma correcta", "indica la textura de cada sección", "calcula los compases y explica el propósito"],
        ["descripción escrita", "conteo de compases"],
        ["contar tres ideas distintas en ABA", "llamar polifonía a la melodía con acompañamiento"],
        "Reconoce la descripción y pide señalar en el texto qué parte cambia y cuál vuelve.",
    ),
    "Representa con tu voz y golpes suaves una textura de melodía sola y otra con acompañamiento.",
    "Inventa en un esquema una pieza de forma ABA con una textura distinta en B y explica el efecto.",
)
