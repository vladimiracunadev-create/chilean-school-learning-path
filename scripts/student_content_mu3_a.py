"""Student material for 3.º básico Música, OA 01 (cualidades del sonido y lenguaje musical) y OA 02 (respuestas a la música escuchada)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1, OA2 = "MU03 OA 01", "MU03 OA 02"

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


def diff(a: tuple, b: tuple) -> int:
    """Number of positions where two equally long patterns differ."""
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


# ---------------------------------------------------------------- OA 01 · clase 1
REG = [("campana", "agudo", "fuerte", 2), ("tambor", "grave", "fuerte", 1), ("flauta", "agudo", "suave", 4), ("bombo", "grave", "suave", 3)]
REG_TXT = " ".join(f"{i}) {n}: {a}, {f}, dura {d} {'pulso' if d == 1 else 'pulsos'}." for i, (n, a, f, d) in enumerate(REG, 1))
REG_TOTAL = sum(d for *_x, d in REG)
CODIGO = "o = sonido suave, O = sonido fuerte, cada ━ = 1 pulso de duración"

L(
    OA1, 1,
    f"Lápiz y papel. Todos los sonidos están descritos por escrito en un «registro de escucha». Si quieres practicar, usa tus palmas, una olla o una caja con una cuchara de madera, a volumen bajo. Código de dibujo: {CODIGO}.",
    "Aprenderé a localizar en una escucha las cuatro cualidades del sonido: altura, timbre, intensidad y duración. Sirve para decir con precisión qué se oyó y dónde.",
    ["Sé que un sonido puede ser fuerte o suave.", "Sé distinguir un sonido fino de uno hondo.", "Sé qué es un pulso."],
    [
        "Localizar es decir en qué momento de la escucha pasó algo. Para eso anotamos los sonidos en un registro, en el orden en que suenan, y a cada uno le ponemos sus cuatro cualidades. La altura dice si es agudo (fino) o grave (hondo). La intensidad dice si suena fuerte o suave. La duración dice cuántos pulsos suena. El timbre dice qué lo produce.",
        f"Cada cualidad se decide con su propia pregunta. Una campana pequeña suena aguda, y puede sonar suave si la tocas despacio. Un tambor grande suena grave, y puede sonar fuerte o suave. Por eso agudo y fuerte no son lo mismo. También podemos dibujar un sonido con este código: {CODIGO}.",
        "Cuando escuchas, no lo hagas todo a la vez. En la primera escucha anotas la altura. En la segunda anotas la intensidad. En la tercera cuentas los pulsos. Así cada dato queda ligado a un momento del registro y puedes volver a revisarlo.",
    ],
    [("altura", "qué tan agudo o grave es un sonido"), ("timbre", "el color del sonido; dice qué lo produce"), ("intensidad", "qué tan fuerte o suave suena"), ("duración", "cuántos pulsos suena"), ("registro de escucha", "lista de sonidos en el orden en que suenan, con sus cualidades")],
    [
        ("Localizar el sonido más largo", f"Registro de escucha: {REG_TXT} ¿Cuál es el sonido más largo?", ["Miro la duración de cada uno: 2, 1, 4 y 3 pulsos.", "El mayor número es 4.", "El 4 es el sonido número 3."], "El sonido 3, la flauta, con 4 pulsos"),
        ("Separar altura de intensidad", "Una niña dice: «el sonido número 2 es grave, entonces es suave». Registro de escucha: " + REG_TXT + " ¿Tiene razón?", ["Grave habla de la altura; suave habla de la intensidad.", "El tambor (número 2) es grave y es fuerte."], "No: es grave pero fuerte; son cualidades distintas"),
    ],
    [
        ("Decir que un sonido es largo porque empezó con un golpe fuerte.", "Se confunden duración e intensidad.", "Cuenta cuántos pulsos suena, no qué tan fuerte parte."),
        ("Pensar que si dos sonidos son graves, los dos suenan igual.", "Se olvidan el timbre y las otras cualidades.", "Compara las cuatro cualidades, una por una."),
    ],
    [
        ex(f"Registro de escucha: {REG_TXT} ¿Qué instrumento hace el sonido número 1?", "La campana", "El registro dice que el sonido 1 es la campana."),
        ex(f"Registro de escucha: {REG_TXT} ¿Cuántos pulsos dura el sonido número 4?", "3 pulsos", "Al lado del bombo, el registro dice «dura 3 pulsos»."),
        ex("Un cascabel suena fino. ¿Su altura es aguda o grave?", "Aguda", "Un sonido fino es agudo."),
    ],
    [
        ex(f"Registro de escucha: {REG_TXT} Escribe los números de los sonidos que son graves.", "2 y 4", "El tambor (2) y el bombo (4) están anotados como graves."),
        ex(f"Registro de escucha: {REG_TXT} ¿Cuántos sonidos son fuertes?", "2", "La campana (1) y el tambor (2) son los únicos fuertes."),
        ex(f"Registro de escucha: {REG_TXT} Dibuja con el código ({CODIGO}) el sonido número 3.", "o ━━━━", "La flauta es suave (o minúscula) y dura 4 pulsos (cuatro rayas)."),
    ],
    [
        arith(f"Registro de escucha: {REG_TXT} ¿Cuántos pulsos suenan en total sumando los cuatro sonidos?", "+".join(str(d) for *_x, d in REG), "Se suman las duraciones de los cuatro sonidos.", " pulsos"),
        ex("Un sonido es agudo, fuerte y corto. Otro es agudo, suave y corto. ¿Qué cualidad es la única distinta?", "La intensidad", "Los dos son agudos y cortos; solo cambia fuerte contra suave."),
        ex(f"Registro de escucha: {REG_TXT} ¿Qué dos sonidos tienen la misma altura y la misma intensidad?", "Ninguno", "Los pares agudos son fuerte y suave, y los graves también son fuerte y suave."),
    ],
    [
        ex("Dos tambores se golpean con la misma fuerza y el mismo tiempo, pero uno es de lata y otro de madera, y suenan distinto. ¿Qué cualidad explica la diferencia y por qué no es la intensidad?", "El timbre; la fuerza fue la misma", "Si la fuerza es igual, lo distinto es el material que suena: el timbre."),
        ex(f"Registro de escucha: {REG_TXT} Si el sonido 3 durara 2 pulsos y no 4, ¿cuál pasa a ser el sonido más largo?", "El sonido 4, el bombo", "Con 2 pulsos la flauta queda bajo los 3 pulsos del bombo."),
    ],
    [
        arith(f"Registro de escucha: {REG_TXT} Tocas el sonido 1 y después el sonido 3. ¿Cuántos pulsos dura tu secuencia?", "2+4", "Se suman los 2 pulsos de la campana y los 4 de la flauta.", " pulsos"),
        ex(f"Registro de escucha: {REG_TXT} Código: {CODIGO}. Quieres dibujar los sonidos 2 y 4. Escribe los dos dibujos en orden.", "O ━ y o ━━━", "El tambor es fuerte y dura 1 pulso; el bombo es suave y dura 3."),
    ],
    [ex("En el recreo suena una campana fuerte y larga. Después una pelota hace un «pof» suave y breve. Di la intensidad y la duración de cada una.", "Campana: fuerte y larga; pelota: suave y corta", "La campana se oye fuerte y dura; el «pof» es flojo y se acaba rápido.")],
    [ex("¿Qué cualidad cambia cuando pasas de un susurro a un grito?", "La intensidad", "Se pasa de suave a fuerte."), ex("Un trueno lejano, ¿es agudo o grave?", "Grave", "El trueno suena hondo."), ex("Nombra las cuatro cualidades del sonido.", "Altura, timbre, intensidad y duración", "Son las cuatro preguntas para describir cualquier sonido.")],
    (
        f"Haz tu propio registro de escucha con tres sonidos hechos por ti con objetos seguros de tu casa, por ejemplo golpear una olla con una cuchara de madera, golpear la mesa con la palma o frotar dos hojas de papel. Para cada sonido escribe su número, el objeto, la altura (agudo o grave), la intensidad (fuerte o suave) y la duración en pulsos. Dibuja los tres con el código ({CODIGO}).",
        "1) olla: grave, fuerte, 2 pulsos (O ━━). 2) mesa con la palma: grave, suave, 1 pulso (o ━). 3) papel frotado: agudo, suave, 3 pulsos (o ━━━).",
        ["anota los tres sonidos en orden", "nombra las cuatro cualidades de cada uno", "dibuja cada sonido con el código"],
        ["registro escrito", "dibujo con código", "sonidos producidos"],
        ["decir fuerte para un sonido agudo sin comprobar", "dibujar una duración distinta de la que anotó"],
        "Reconoce el registro claro y pide que repita un sonido para comprobar su duración; si mezcla altura e intensidad, vuelve a hacer una pregunta por vez.",
    ),
    "Elige dos objetos seguros de tu casa y golpéalos suavemente. Di de cada uno si suena agudo o grave.",
    "Haz un registro de cuatro sonidos con orden, altura e intensidad, y pide a una persona de tu casa que lo toque sin mirar tus dibujos.",
)

# ---------------------------------------------------------------- OA 01 · clase 2
P1 = (TA, TT, TAA, SIL)
P2 = (TT, TA, TA, SIL, TAA)
P3 = (TA, TAA, TT, TT, TA, SIL)
P4 = (TAA, TA, TA, TT)

L(
    OA1, 2,
    f"Lápiz, tus palmas y tus pasos. Leyenda de ritmo: {LEY}. Todos los patrones están escritos en los ejercicios.",
    "Aprenderé a distinguir pulso, acento y patrón, y a calcular cuántos pulsos y cuántos sonidos tiene un patrón. Sirve para tocar con otras personas sin perderse.",
    ["Sé caminar al mismo paso.", "Sé contar hasta 20.", "Sé que TA dura un pulso y ti-ti son dos sonidos rápidos."],
    [
        "El pulso es el latido parejo de la música, como tus pasos al caminar. El acento es el pulso que se marca más fuerte, y va al comienzo de cada grupo de pulsos. Si cuentas de a 3, dices 1-2-3, 1-2-3, y el acento cae en cada 1. También se puede contar de a 2 y de a 4.",
        f"El patrón es una secuencia de sonidos y silencios que se repite sobre el pulso. Hoy sumamos TAA, un sonido largo que dura 2 pulsos. Leyenda: {LEY}. Para contar pulsos sumamos lo que ocupa cada símbolo. Para contar sonidos sumamos lo que suena. El silencio ocupa pulso, pero no suena.",
        f"Un ejemplo: {P(*P1)}. Los pulsos son 1 + 1 + 2 + 1 = {pulses(*P1)}. Los sonidos son 1 + 2 + 1 + 0 = {sounds(*P1)}. Ojo: ti-ti ocupa un solo pulso, aunque tenga dos sonidos, y TAA ocupa dos pulsos, aunque tenga un solo sonido. Ritmo y pulso no son lo mismo: el pulso se mantiene parejo mientras el patrón cambia.",
    ],
    [("pulso", "latido parejo de la música"), ("acento", "pulso que se marca más fuerte, al inicio de cada grupo"), ("patrón", "secuencia de sonidos y silencios que se repite"), ("TAA", "un sonido largo que dura 2 pulsos"), ("grupo de pulsos", "pulsos que se cuentan juntos, de a 2, 3 o 4")],
    [
        ("Contar pulsos y sonidos", f"¿Cuántos pulsos y cuántos sonidos tiene {P(*P2)}?", ["Pulsos: ti-ti 1, TA 1, TA 1, SIL 1, TAA 2.", "1 + 1 + 1 + 1 + 2 = 6 pulsos.", "Sonidos: 2 + 1 + 1 + 0 + 1 = 5 sonidos."], f"{pulses(*P2)} pulsos y {sounds(*P2)} sonidos"),
        ("Ubicar los acentos", "Cuento 12 pulsos en grupos de 3, con acento en el primero de cada grupo. ¿En qué números caen los acentos?", ["Los grupos son 1-2-3, 4-5-6, 7-8-9 y 10-11-12.", "El acento va al inicio de cada grupo."], "En los pulsos 1, 4, 7 y 10"),
    ],
    [
        ("Decir que ti-ti son dos pulsos.", "Se cuentan los sonidos y no los latidos.", "ti-ti son dos sonidos dentro de un solo pulso."),
        ("Contar TAA como un pulso porque es un solo sonido.", "Se confunden sonidos con pulsos.", "TAA es un sonido que dura 2 pulsos; el segundo pulso se mantiene sonando."),
    ],
    [
        ex(f"¿Cuántos pulsos ocupa {TAA}?", "2", "Según la leyenda, TAA es un sonido largo que dura 2 pulsos."),
        ex("Cuentas de a 4: 1-2-3-4, 1-2-3-4. Si el acento va en el 1, ¿qué números se dicen suaves?", "2, 3 y 4", "Solo el 1 lleva acento; los otros pulsos van suaves."),
        ex(f"¿Cuántos pulsos tiene {P(TA, TA, SIL)}?", str(pulses(TA, TA, SIL)), "Cada símbolo ocupa un pulso y el silencio también cuenta."),
    ],
    [
        ex(f"Cuenta los pulsos de este patrón: {P(*P3)}.", str(pulses(*P3)), "Se suma lo que ocupa cada símbolo: 1 + 2 + 1 + 1 + 1 + 1."),
        ex(f"Cuenta los sonidos de este patrón: {P(*P3)}.", str(sounds(*P3)), "Suenan 1 + 1 + 2 + 2 + 1 y el silencio no suena."),
        ex("Cuentas de a 3: 1-2-3, 1-2-3, 1-2-3, con acento en cada 1. ¿Cuántos acentos hay?", "3", "Hay tres grupos y cada grupo tiene un acento."),
    ],
    [
        ex("Escribe los números donde caen los acentos si cuentas 12 pulsos en grupos de 4.", "1, 5 y 9", "Cada grupo parte cuatro números después del anterior."),
        arith(f"Un patrón de 6 pulsos tiene 1 silencio. ¿Cuántos pulsos suenan?", "6-1", "A los 6 pulsos se les quita el pulso en silencio.", " pulsos"),
    ],
    [
        ex(f"Luis dice que {P(*P4)} tiene 4 pulsos porque son 4 símbolos. ¿Cuántos pulsos tiene realmente?", str(pulses(*P4)), "TAA ocupa 2 y los otros tres ocupan 1 cada uno: 2 + 1 + 1 + 1."),
        ex(f"En {P(*P4)}, ¿cuántos sonidos hay?", str(sounds(*P4)), "TAA suena 1, TA suena 1, TA suena 1 y ti-ti suena 2."),
    ],
    [
        ex(f"¿Cuántos sonidos tiene un patrón de 4 pulsos formado por {P(TT, TT, TT, TT)}?", "8", "Cada ti-ti tiene 2 sonidos y hay 4 ti-ti: 2 × 4."),
        arith(f"El patrón {P(*P1)} se repite 3 veces. ¿Cuántos sonidos se tocan en total?", f"{sounds(*P1)}*3", "Cada vuelta tiene 4 sonidos y hay 3 vueltas.", " sonidos"),
    ],
    [arith(f"Un patrón de 5 pulsos se repite 4 veces seguidas. ¿Cuántos pulsos se tocan en total?", "5*4", "Cada vuelta tiene 5 pulsos y hay 4 vueltas.", " pulsos")],
    [ex(f"¿Cuántos pulsos tiene {P(SIL, TA, SIL, TA)}?", "4", "Los silencios también ocupan un pulso."), ex(f"¿Cuántos sonidos tiene {P(TA, TA, SIL, SIL)}?", "2", "Solo suenan los dos TA."), ex("¿Qué es un patrón de ritmo?", "Una secuencia que se repite sobre el pulso", "Un patrón es una secuencia de sonidos y silencios que vuelve a sonar.")],
    (
        f"Camina en tu lugar con paso parejo. Toca con las palmas el patrón {P(TA, TT, TAA, SIL)} cuatro veces seguidas, marcando más fuerte el primer pulso de cada vuelta. Escribe cuántos pulsos y cuántos sonidos tiene el patrón y cuántos pulsos tocaste en total.",
        "El patrón tiene 5 pulsos y 4 sonidos. Lo toqué 4 veces: 20 pulsos en total.",
        ["mantiene el pulso parejo con los pies", "toca el patrón con el silencio en su lugar", "escribe los conteos correctos"],
        ["interpretación", "conteo escrito"],
        ["no contar el silencio como pulso", "contar TAA como un pulso"],
        "Reconoce el pulso estable y pide que marque con el dedo dónde está el silencio y dónde dura 2 pulsos TAA.",
    ),
    "Camina 16 pasos parejos y aplaude solo en el primer paso de cada grupo de 4. Cuenta cuántos aplausos diste.",
    "Inventa un patrón de 8 pulsos con TA, ti-ti, TAA y SIL, y calcula sus pulsos y sus sonidos.",
)

# ---------------------------------------------------------------- OA 01 · clase 3
F1 = (TA, TA, TT, TA)
F2 = (TA, TA, TT, TA)
F3 = (TAA, TAA, SIL, TA)
F4 = (TA, TA, TT, TAA)

L(
    OA1, 3,
    f"Lápiz y palmas. Leyenda: {LEY}. Cada frase tiene 4 símbolos y todas están escritas en los ejercicios.",
    "Aprenderé a reconocer la repetición, el contraste y la variación, y también la pregunta y respuesta. Sirve para entender cómo está armada una música.",
    ["Sé contar pulsos en un patrón.", "Sé qué es una frase musical corta.", "Sé comparar dos sonidos."],
    [
        "Una música se arma con frases. Si una frase vuelve igual, hay repetición (también se dice reiteración). Si llega una frase muy distinta, hay contraste. Si vuelve casi igual, pero cambia una parte, hay variación. La variación es parecida y distinta a la vez, por eso la reconocemos como «la misma frase, cambiada».",
        f"Para decidir, compara las frases símbolo por símbolo. Frase 1: {P(*F1)}. Frase 2: {P(*F2)}. No cambia ningún símbolo: es repetición. Frase 3: {P(*F3)}. Cambia casi todo: es contraste. Frase 4: {P(*F4)}. Cambia solo el último símbolo: es variación.",
        "Hay otra forma de organizar frases: pregunta y respuesta. La primera frase queda como «abierta», como si preguntara. La segunda frase contesta y da la sensación de terminar. A veces la respuesta es una variación de la pregunta. Las preguntas y respuestas se pueden repartir entre dos personas, una pregunta y la otra responde.",
    ],
    [("repetición (reiteración)", "una frase vuelve igual"), ("contraste", "llega una frase muy distinta"), ("variación", "vuelve casi igual, con algo cambiado"), ("pregunta y respuesta", "una frase abierta y otra que contesta"), ("frase", "grupo corto de sonidos que forma una idea musical")],
    [
        ("Clasificar una frase", f"Frase A: {P(*F1)}. Frase B: {P(*F4)}. ¿Es repetición, contraste o variación?", ["Comparo símbolo por símbolo.", "Los tres primeros son iguales y el último cambia de TA a TAA.", "Cambia una sola parte: es parecida y distinta."], "Variación"),
        ("Contar lo que cambia", f"Frase A: {P(*F1)}. Frase C: {P(*F3)}. ¿En cuántos lugares cambian?", ["Posición 1: TA y TAA, cambia.", "Posición 2: TA y TAA, cambia.", "Posición 3: ti-ti y SIL, cambia.", "Posición 4: TA y TA, igual."], f"En {diff(F1, F3)} lugares: es un contraste"),
    ],
    [
        ("Llamar variación a una frase donde cambió casi todo.", "La variación conserva la mayor parte de la frase.", "Si cambió casi todo, es contraste; si cambió una parte, es variación."),
        ("Pensar que repetición es que suene parecido.", "En la repetición no cambia nada.", "Si hay un cambio, aunque sea pequeño, ya no es repetición."),
    ],
    [
        ex(f"Frase 1: {P(*F1)}. Frase 2: {P(*F2)}. ¿Repetición, contraste o variación?", "Repetición", "Las dos frases tienen los mismos cuatro símbolos."),
        ex("Suena una frase que queda «abierta» y después otra que la contesta y termina «cerrada». ¿Cuál de las dos es la respuesta: la primera o la segunda?", "La segunda", "La respuesta es la frase que contesta y cierra."),
        ex("Una frase que «pregunta» queda abierta y otra «responde». ¿Qué organización musical es?", "Pregunta y respuesta", "Una frase abierta y otra que contesta forman pregunta y respuesta."),
    ],
    [
        ex(f"Compara {P(*F1)} con {P(*F4)}. ¿En cuántos lugares cambia?", str(diff(F1, F4)), "Solo cambia el último símbolo, de TA a TAA."),
        ex(f"Compara {P(*F1)} con {P(*F3)}. ¿Repetición, contraste o variación?", "Contraste", "Cambian tres de cuatro símbolos: es muy distinta."),
        ex(f"Pregunta: {P(*F1)}. Respuesta: {P(TA, TA, TT, SIL)}. ¿En cuántos lugares cambia la respuesta respecto de la pregunta?", "1", "Solo el último símbolo cambia, de TA a SIL; la respuesta es una variación de la pregunta."),
    ],
    [
        ex(f"Ordena de menos a más cambio respecto de {P(*F1)}: (a) {P(*F3)}, (b) {P(*F2)}, (c) {P(*F4)}.", "b, c, a", "La b no cambia, la c cambia 1 símbolo y la a cambia 3."),
        ex("Una música tiene las frases A, A, B, A. ¿Cuántas veces se repite la frase A?", "3", "La A aparece en la primera, la segunda y la cuarta posición."),
    ],
    [
        ex(f"Piensa en esta pregunta: {P(TA, TA, TT, TAA)}. Su respuesta es una variación que cambia solo el último símbolo por SIL. Escribe la respuesta.", P(TA, TA, TT, SIL), "Se copian los tres primeros símbolos y se cambia el último por SIL."),
        arith(f"La frase {P(*F1)} suena 3 veces seguidas y luego suena la frase {P(*F3)} una vez. ¿Cuántos pulsos son en total?", f"{pulses(*F1)}*3+{pulses(*F3)}", "Se multiplican los pulsos de la primera por 3 y se suman los de la segunda.", " pulsos"),
    ],
    [
        arith(f"La frase {P(*F1)} suena 2 veces y su variación {P(*F4)} suena 2 veces. ¿Cuántos pulsos son en total?", f"{pulses(*F1)}*2+{pulses(*F4)}*2", "Se suman los pulsos de las dos frases, cada una por 2.", " pulsos"),
        ex(f"¿Cuántos sonidos tiene la frase {P(*F3)}?", str(sounds(*F3)), "TAA suena 1, TAA suena 1, SIL no suena y TA suena 1."),
    ],
    [ex("En una canción, el mismo estribillo vuelve idéntico después de cada verso. ¿Qué recurso es?", "Repetición", "El estribillo vuelve igual.")],
    [ex("Si una frase cambia solo una parte, ¿qué recurso hay?", "Variación", "Es la misma frase con una parte cambiada."), ex("Una frase muy distinta de la anterior, ¿qué recurso es?", "Contraste", "Lo muy distinto es contraste."), ex("¿Qué organización hay cuando una frase contesta a otra?", "Pregunta y respuesta", "En pregunta y respuesta, la segunda frase responde a la primera.")],
    (
        f"Toca con las palmas esta frase base: {P(*F1)}. Después crea otra frase de 4 símbolos que sea una variación (cambia solo uno), otra que sea un contraste (cambia tres o cuatro) y otra que sea una repetición. Escríbelas, indica cuántos símbolos cambian respecto de la base y toca las tres en orden.",
        f"Base: {P(*F1)}. Variación: {P(TA, TA, TT, SIL)} (cambia 1). Contraste: {P(TAA, SIL, TAA, SIL)} (cambian 4). Repetición: {P(*F1)} (cambian 0).",
        ["escribe tres frases de 4 símbolos", "cuenta correctamente lo que cambia", "toca las frases con pulso parejo"],
        ["frases escritas", "interpretación con palmas"],
        ["llamar variación a un cambio total", "olvidar que la repetición no cambia nada"],
        "Reconoce el conteo de cambios; si el estudiante duda, pide que alinee las frases una bajo otra y compare símbolo por símbolo.",
    ),
    "Escribe una frase de 4 símbolos y una variación de ella que cambie solo uno.",
    "Crea una pregunta y una respuesta de 4 símbolos cada una, y toca la pregunta y la respuesta con una persona de tu casa.",
)

# ---------------------------------------------------------------- OA 01 · clase 4
L(
    OA1, 4,
    "Lápiz, tus palmas y un reloj con segundero para contar 10 segundos (si no tienes, cuenta «mil uno, mil dos…» como un segundo cada uno). Cuida el volumen: nunca más fuerte que una conversación animada.",
    "Aprenderé a leer y dibujar la dinámica (fuerte, suave y sus cambios) y el tempo (lento, rápido). Sirve para tocar una música con el carácter que pide.",
    ["Sé que fuerte y suave son intensidades.", "Sé qué es un pulso.", "Sé comparar rápido y lento."],
    [
        "La dinámica es cómo cambia la intensidad a lo largo de la música. Se escribe con letras: p significa suave (piano) y f significa fuerte (forte). Una flecha que se abre «<» es crescendo: el sonido sube poco a poco. Una flecha que se cierra «>» es diminuendo: el sonido baja poco a poco.",
        "El tempo es qué tan rápido va el pulso. Un tempo lento tiene pocos pulsos en un tiempo dado, y uno rápido tiene muchos. Si das un pulso por segundo, en 10 segundos das 10 pulsos. Si das el doble de rápido, das 20 pulsos en esos mismos 10 segundos. Más pulsos en el mismo tiempo es más rápido.",
        "Dinámica y tempo son distintos. Se puede tocar fuerte y lento, o suave y rápido. Un tambor puede ir rápido y suave. Para no confundirlos pregunta primero «¿qué tan fuerte suena?» (dinámica) y después «¿qué tan seguidos van los pulsos?» (tempo).",
    ],
    [("dinámica", "cambios de intensidad en la música"), ("p (piano)", "suave"), ("f (forte)", "fuerte"), ("crescendo (<)", "sube la intensidad poco a poco"), ("diminuendo (>)", "baja la intensidad poco a poco"), ("tempo", "qué tan rápido o lento va el pulso")],
    [
        ("Leer una dinámica", "Una música tiene esta dinámica: p – < – f – > – p. ¿Cómo cambia?", ["Parte suave (p).", "Sube poco a poco (<).", "Llega a fuerte (f).", "Baja poco a poco (>) y termina suave (p)."], "Suave, sube a fuerte, baja y termina suave"),
        ("Comparar tempos", "Una persona da 10 pulsos en 10 segundos. Otra da 20 pulsos en los mismos 10 segundos. ¿Quién va más rápido?", ["El tiempo es igual: 10 segundos.", "Quien da más pulsos en ese tiempo va más rápido.", "20 es mayor que 10."], "La segunda persona"),
    ],
    [
        ("Decir que crescendo es ir más rápido.", "El crescendo cambia la intensidad, no el tempo.", "Crescendo es subir la intensidad; ir más rápido es otro cambio."),
        ("Pensar que lento significa suave.", "Se confunden tempo e intensidad.", "Lento habla de los pulsos; suave habla de la intensidad."),
    ],
    [
        ex("¿Qué significa la letra f en una partitura?", "Fuerte", "La letra f viene de forte, que significa fuerte."),
        ex("¿Qué significa la flecha que se abre «<»?", "Crescendo: subir poco a poco", "La flecha abierta indica que la intensidad crece."),
        ex("Si en 10 segundos das 10 pulsos, ¿el tempo es más lento o más rápido que dar 20 pulsos en 10 segundos?", "Más lento", "Diez pulsos son menos que veinte en el mismo tiempo."),
    ],
    [
        ex("Dinámica f – > – p. ¿Cómo cambia la intensidad?", "Parte fuerte y baja hasta suave", "La flecha cerrada baja la intensidad de f a p."),
        ex("Una música va rápida y suave. Otra va lenta y fuerte. ¿Cuál tiene más pulsos en el mismo tiempo?", "La que va rápida y suave", "Rápida significa más pulsos en el mismo tiempo, sin importar la intensidad."),
        ex("Dibuja con signos una música que parta suave, suba hasta fuerte y se quede fuerte.", "p – < – f", "Suave es p, subir es la flecha abierta y fuerte es f."),
    ],
    [
        arith("Das 1 pulso por segundo durante 30 segundos. ¿Cuántos pulsos das?", "1*30", "Con un pulso por segundo, los pulsos son tantos como segundos.", " pulsos"),
        arith("Das 2 pulsos por segundo durante 10 segundos. ¿Cuántos pulsos das?", "2*10", "Cada segundo tiene 2 pulsos y pasan 10 segundos.", " pulsos"),
        ex("Una música tiene p – < – f – > – p. ¿Cuántas veces cambia la intensidad poco a poco (flechas)?", "2", "Hay una flecha abierta y una cerrada."),
    ],
    [
        ex("Ana dice: «el crescendo acelera la música». ¿Tiene razón?", "No; el crescendo sube la intensidad, no la velocidad", "Crescendo es sobre la intensidad y el tempo es otro cambio."),
        ex("Una música da 15 pulsos en 10 segundos y otra 12 pulsos en 10 segundos. ¿Cuál es más lenta?", "La de 12 pulsos", "Con el mismo tiempo, menos pulsos es más lento."),
    ],
    [
        arith("Una música lenta da 1 pulso por segundo. Otra más rápida da 2 pulsos por segundo. En 20 segundos, ¿cuántos pulsos más da la rápida?", "2*20-1*20", "Rápida: 2 × 20 = 40; lenta: 1 × 20 = 20; se restan.", " pulsos más"),
        ex("Escribe una dinámica de cinco signos que parta fuerte, baje poco a poco hasta suave y luego vuelva a subir hasta fuerte.", "f – > – p – < – f", "f, flecha cerrada hasta p, flecha abierta hasta f."),
    ],
    [ex("Una persona canta una canción de cuna: la música va lenta y suave. Otra marcha rápido y fuerte. ¿Qué dinámica y qué tempo tiene cada una?", "Cuna: suave y lenta; marcha: fuerte y rápida", "La canción de cuna va suave y lenta; la marcha va fuerte y rápida.")],
    [ex("¿Qué significa p?", "Suave", "p viene de piano, que significa suave."), ex("¿La flecha cerrada «>» sube o baja la intensidad?", "Baja", "Es el diminuendo."), ex("Más pulsos en el mismo tiempo, ¿es más lento o más rápido?", "Más rápido", "El tempo rápido tiene más pulsos en el mismo tiempo.")],
    (
        "Elige un patrón de palmas de 4 pulsos (por ejemplo TA – TA – TA – SIL). Tócalo 3 veces seguidas con esta dinámica: primero suave (p), luego crescendo hasta fuerte (f) en la segunda vuelta y en la tercera diminuendo hasta suave. Cuida el volumen. Después toca el mismo patrón con un tempo más lento y otro más rápido. Dibuja la dinámica con signos y escribe cuál tempo fue más rápido y por qué.",
        "Dinámica: p – < – f – > – p. El tempo rápido fue más rápido porque di más pulsos en 10 segundos que en el lento.",
        ["dibuja la dinámica con signos", "cambia la intensidad poco a poco", "explica cuál tempo fue más rápido"],
        ["dibujo de signos", "interpretación con palmas", "explicación breve"],
        ["cambiar el tempo cuando debía cambiar la intensidad", "olvidar que más pulsos en el mismo tiempo es más rápido"],
        "Reconoce el cambio gradual de intensidad y pide contar pulsos en 10 segundos para justificar el tempo.",
    ),
    "Di una frase en voz suave y luego la misma frase en voz fuerte. Escribe p y f en el orden en que lo hiciste.",
    "Haz crescendo y diminuendo con tus palmas y dibuja las flechas en el orden en que sonaron.",
)

# ---------------------------------------------------------------- OA 01 · clase 5
SEC = [("A", "flauta suave y lenta", 8), ("B", "tambores fuertes y rápidos", 8), ("A", "flauta suave y lenta", 8)]
SEC_TXT = "; ".join(f"sección {i}: {d}, {n} pulsos" for i, (_l, d, n) in enumerate(SEC, 1))
SEC_TOTAL = sum(n for *_x, n in SEC)

L(
    OA1, 5,
    "Lápiz y papel. Las músicas están descritas por escrito, con secciones marcadas con letras. Para practicar puedes aplaudir una sección suave y otra fuerte.",
    "Aprenderé a distinguir secciones A, AB y ABA y a representarlas con letras. Sirve para ver cómo está construida una música.",
    ["Sé reconocer repetición y contraste.", "Sé contar pulsos.", "Sé comparar suave y fuerte."],
    [
        "Una sección es una parte de la música con un carácter propio. Le ponemos una letra: la primera parte distinta es A. Si llega una parte contrastante, es B. Si la música tiene solo A, se llama forma A. Si tiene A y luego B, se llama forma AB. Si vuelve A al final, se llama forma ABA.",
        f"Un ejemplo con ABA: {SEC_TXT}. Hay tres secciones, pero solo dos distintas: A y B. La A vuelve al final igual que al principio. En total son {SEC_TOTAL} pulsos. Para saber la forma, mira en qué orden aparecen las secciones, no cuántos pulsos dura cada una.",
        "Representar una forma es dibujar cajas con letras, una caja por sección, en orden: A | B | A. El largo de la caja puede mostrar cuánto dura. Si la sección vuelve, se usa la misma letra. Si vuelve un poco cambiada, se escribe A con una marca, por ejemplo A'.",
    ],
    [("sección", "parte de la música con carácter propio"), ("forma A", "una sola sección"), ("forma AB", "una sección y luego otra distinta"), ("forma ABA", "A, luego B, y vuelve A"), ("forma", "el orden en que aparecen las secciones")],
    [
        ("Reconocer la forma", f"Una música tiene {SEC_TXT}. ¿Qué forma tiene y cuántas secciones distintas hay?", ["Ordeno por letras: A, B, A.", "Vuelve A al final.", "Las letras distintas son A y B."], "Forma ABA; 2 secciones distintas"),
        ("Calcular la duración", "Una música tiene la sección A de 8 pulsos, la B de 6 pulsos y vuelve la A de 8 pulsos. ¿Cuántos pulsos dura en total?", ["Sumo las tres secciones.", "8 + 6 + 8 = 22."], "22 pulsos"),
    ],
    [
        ("Pensar que ABA tiene tres secciones distintas.", "La A que vuelve es la misma sección.", "Cuenta las letras distintas: en ABA son dos."),
        ("Llamar forma AB a una música que termina volviendo a A.", "AB termina en B, sin volver a A.", "Si vuelve A al final, es ABA."),
    ],
    [
        ex("Música: una parte lenta y suave, y luego una parte rápida y fuerte. No vuelve la primera. ¿Qué forma tiene?", "AB", "Hay dos partes distintas y no vuelve la primera."),
        ex("Si una música tiene solo una sección, ¿qué forma tiene?", "A", "Una sola sección es forma A."),
        ex("En la forma ABA, ¿qué sección vuelve?", "La A", "Después de B vuelve la sección A."),
    ],
    [
        ex(f"Una música tiene {SEC_TXT}. ¿Cuántas secciones tiene en total?", "3", "Se cuentan las tres partes aunque dos sean iguales."),
        ex("Una música tiene cuatro partes: A, B, A, B. Escribe cuántas letras distintas usa.", "2", "Solo se usan A y B."),
        ex("Dibuja la forma de una música con una parte A, una B y otra vez la A, en cajas con letras.", "A | B | A", "Se dibuja una caja por sección, en el orden en que suenan."),
    ],
    [
        arith("Una música tiene A de 8 pulsos, B de 4 pulsos y A de 8 pulsos. ¿Cuántos pulsos suenan en total?", "8+4+8", "Se suman los pulsos de las tres secciones.", " pulsos"),
        ex("Una música tiene A de 8 pulsos y B de 8 pulsos. Otra tiene A, B, A con 8 pulsos cada una. ¿Cuántos pulsos más dura la segunda?", "8 pulsos", "La segunda tiene una sección A de 8 pulsos adicional."),
        ex("En una música, A es suave y B es fuerte. Está escrita así: A B A B A. ¿Cuántas veces suena la parte suave?", "3", "La A aparece en las posiciones 1, 3 y 5."),
    ],
    [
        ex("Pedro dice: «si cada sección dura 8 pulsos, la forma AB y la forma ABA duran lo mismo». ¿Tiene razón?", "No; AB dura 16 pulsos y ABA dura 24", "AB tiene dos secciones de 8 pulsos y ABA tiene tres."),
        ex("Una música es A B A', donde A' es la A un poco cambiada. ¿Cuántas secciones distintas hay si A' se considera parte de A?", "2", "A' sigue siendo la sección A con un cambio, así que las distintas son A y B."),
    ],
    [
        arith("Una música ABA dura 24 pulsos. La A dura 8 pulsos cada vez que suena. ¿Cuántos pulsos dura la B?", "24-8-8", "Al total se le quitan las dos veces que suena la A.", " pulsos"),
        ex("Escribe una forma de cinco secciones en que la B esté en el lugar 3 y todas las demás sean A.", "A A B A A", "La B va en el centro y las otras cuatro secciones son A."),
    ],
    [ex("En una obra se escucha una melodía tranquila, luego otra con ritmo marcado y al final la tranquila de nuevo. ¿Qué forma tiene?", "ABA", "La primera parte vuelve al final.")],
    [ex("¿Cómo se llama una música con las partes A y luego B?", "AB", "Dos secciones distintas, sin volver a la primera."), ex("En ABA, ¿cuántas letras distintas hay?", "2", "A y B."), ex("¿La forma depende del orden o del largo de las secciones?", "Del orden", "La forma muestra en qué orden aparecen las secciones.")],
    (
        "Crea una forma ABA con tus palmas: la sección A es suave, con 4 pulsos (por ejemplo TA – TA – TA – SIL), la B es fuerte, con 4 pulsos distintos, y vuelve A. Dibuja tres cajas con las letras y escribe cuántos pulsos dura en total tu música.",
        "A: TA – TA – TA – SIL (suave); B: TAA – TAA (fuerte); A de nuevo. Forma A | B | A. Total 12 pulsos.",
        ["crea las dos secciones con carácter distinto", "vuelve la A igual", "dibuja las cajas y calcula el total"],
        ["interpretación con palmas", "dibujo de cajas", "cálculo escrito"],
        ["que la B suene casi igual que la A", "contar mal los pulsos del total"],
        "Reconoce que la A vuelve igual y pregunta qué hizo diferente la B; revisa el total sumando.",
    ),
    "Escucha o recuerda una canción que conozcas y di si repite una parte. Anótala con letras sin copiar la letra de la canción.",
    "Crea una forma ABAB con dos sonidos distintos de tu casa y dibújala con cajas.",
)

# ---------------------------------------------------------------- OA 02 · clase 1
TEXTO = "Una música dura 8 pulsos. Suena una flauta suave, con sonidos agudos y largos, que va lenta. No hay otros instrumentos."

L(
    OA2, 1,
    f"Lápiz. La música que se escucha está descrita por escrito en cada ejercicio. Texto de trabajo: «{TEXTO}».",
    "Aprenderé a separar lo que se oye (evidencia sonora) de lo que imagino o siento. Sirve para dar una respuesta a la música que otros puedan comprobar.",
    ["Sé nombrar las cualidades del sonido.", "Sé que cada persona puede sentir algo distinto.", "Sé usar la frase «yo escuché»."],
    [
        "Cuando escuchas música puedes decir dos tipos de cosas. Una es lo escuchado: que es lenta, que es suave, que suena una flauta. Eso se puede comprobar volviendo a escuchar. La otra es lo imaginado o sentido: que parece un río, que te dio calma, que te recordó un lugar. Eso es personal y no se comprueba igual.",
        "Una respuesta bien elaborada junta las dos. Primero dices qué oíste, la evidencia sonora, y después dices qué imaginaste o sentiste gracias a eso. Por ejemplo: «Escuché una flauta suave y lenta, por eso sentí calma». La palabra «por eso» une lo que oíste con lo que sentiste.",
        "Dos personas pueden imaginar cosas distintas con la misma música, y ambas pueden estar bien si cada una explica qué oyó para pensarlo. Lo que no sirve es decir solo «me gustó» o «parecía un perro» sin decir qué sonido lo mostró.",
    ],
    [("sensación", "lo que sientes en el cuerpo o el ánimo al escuchar"), ("emoción", "calma, alegría, miedo, tristeza u otras que sientes"), ("idea", "algo que imaginas al escuchar"), ("evidencia sonora", "lo que se oye y se puede comprobar volviendo a escuchar"), ("imaginado", "lo que tu mente crea a partir de la música")],
    [
        ("Clasificar una frase", f"Texto: «{TEXTO}». La frase «Parecía una mañana tranquila en el campo». ¿Es evidencia sonora o es imaginado?", ["Pregunto si se puede comprobar volviendo a escuchar.", "«Mañana tranquila» no se oye, se imagina."], "Imaginado"),
        ("Unir evidencia e idea", f"Texto: «{TEXTO}». Completa: «Imaginé un pájaro porque …».", ["Busco en el texto un rasgo audible.", "Los sonidos agudos y largos de la flauta se parecen a un canto de pájaro."], "Imaginé un pájaro porque la flauta sonaba aguda y suave"),
    ],
    [
        ("Decir solo «me gustó» y no explicar qué se oyó.", "Una opinión sin evidencia no muestra qué escuchaste.", "Agrega algo que oíste: suave, lento, agudo, una flauta."),
        ("Creer que la idea de otra persona está mal porque es distinta.", "La música puede sugerir cosas distintas.", "Pregunta «¿qué oíste para pensar eso?»."),
    ],
    [
        ex(f"Texto: «{TEXTO}». ¿«Suena una flauta» es evidencia sonora o imaginado?", "Evidencia sonora", "Se puede comprobar volviendo a escuchar qué instrumento suena."),
        ex(f"Texto: «{TEXTO}». ¿«Me dio ganas de dormir» es evidencia sonora o sensación personal?", "Sensación personal", "Dormir no se oye; es lo que la persona sintió."),
        ex(f"Texto: «{TEXTO}». ¿Los sonidos son agudos o graves?", "Agudos", "El texto dice que la flauta tiene sonidos agudos."),
    ],
    [
        ex(f"Texto: «{TEXTO}». Escribe cuántas frases de la lista son evidencia sonora: (a) es lenta, (b) parecía una nube, (c) es suave, (d) me dio frío.", "2", "Solo (a) y (c) se pueden comprobar; (b) y (d) son imaginados o sentidos."),
        ex("¿Qué palabra une lo que oíste con lo que sentiste en una buena respuesta?", "Por eso", "«Por eso» conecta la evidencia con la sensación."),
        ex("Dos niños escuchan lo mismo. Uno imagina un río y el otro una lluvia suave. Los dos explican que oyeron sonidos suaves y seguidos. ¿Alguno está equivocado?", "Ninguno", "Los dos dan evidencia sonora y sus ideas son personales."),
    ],
    [
        ex("Ordena de menos a más elaborada: (a) «me gustó», (b) «escuché una flauta suave y por eso sentí calma», (c) «suena una flauta».", "a, c, b", "(a) opina; (c) da evidencia; (b) une evidencia y sensación."),
        ex("Luisa dice: «esta música es triste porque yo lo digo». ¿Qué le falta?", "Evidencia sonora", "Le falta decir qué se oye que la hace pensar eso."),
    ],
    [
        ex("Se escucha una música con tambores fuertes y rápidos. ¿Qué respuesta une evidencia sonora e idea: (a) «Me gustó.», (b) «Escuché tambores fuertes y rápidos, por eso imaginé una carrera.», (c) «Imaginé una carrera.»?", "b", "La (b) dice qué se oyó y la idea que sugirió; (a) solo opina y (c) no da evidencia."),
        ex("Una persona dice «la música sonó fuerte y rápida». Otra dice «me dio miedo». ¿Cuál de las dos frases es sobre lo oído y cuál sobre lo sentido?", "La primera sobre lo oído; la segunda sobre lo sentido", "Fuerte y rápida son cualidades que se oyen; el miedo es una sensación."),
    ],
    [
        ex("Una persona dice: «Escuché una flauta suave y por eso me sentí tranquila». ¿Cuál es la evidencia sonora y cuál es la sensación?", "Evidencia: flauta suave; sensación: tranquila", "La flauta suave se oyó; sentirse tranquila es personal."),
        ex("Dos personas escuchan lo mismo. A una le dio alegría y a otra calma. ¿Pueden ser ciertas las dos?", "Sí", "Las sensaciones son personales y pueden ser distintas."),
    ],
    [ex("Un niño escucha una música lenta y suave de cuna y dice: «parece un barco meciéndose». ¿Qué evidencia sonora sostiene su idea: (a) «Suena lenta y suave.» (b) «Suena fuerte y rápida.»?", "(a)", "Lo lento y suave se parece al balanceo tranquilo de un barco.")],
    [ex("¿«Es lenta» es evidencia sonora o imaginado?", "Evidencia sonora", "El tempo se puede comprobar volviendo a escuchar."), ex("¿«Me recordó mi casa» es evidencia sonora o imaginado?", "Imaginado", "Es un recuerdo personal."), ex("En «Escuché una flauta suave, por eso sentí calma», ¿qué va después de «por eso»: la evidencia sonora o la sensación?", "La sensación", "Después de «por eso» va lo que se sintió o imaginó.")],
    (
        "Un adulto toca despacio con una cuchara de madera sobre una mesa, 8 golpes suaves y lentos, y después 8 golpes fuertes y rápidos (con cuidado de no dañar la mesa). Escucha cada parte. Escribe para cada una una frase de evidencia sonora y una frase de lo que imaginaste o sentiste, usando «por eso».",
        "Parte 1: escuché golpes suaves y lentos, por eso imaginé pasos tranquilos. Parte 2: escuché golpes fuertes y rápidos, por eso sentí ganas de correr.",
        ["escribe evidencia sonora de cada parte", "agrega una idea o sensación", "usa «por eso» para unirlas"],
        ["frases escritas", "conversación"],
        ["escribir solo la idea sin la evidencia", "mezclar lo oído con lo imaginado en una sola palabra"],
        "Reconoce la evidencia y pregunta «¿qué oíste para pensar eso?»; no corrige la idea si hay evidencia.",
    ),
    "Escucha un sonido de tu casa y escribe una frase de lo oído y otra de lo imaginado.",
    "Pide a una persona de tu casa que te cuente una idea y qué oyó para pensarla.",
)

# ---------------------------------------------------------------- OA 02 · clase 2
L(
    OA2, 2,
    "Un espacio libre y seguro, sin objetos en el suelo, y calzado cómodo o pies descalzos. Todas las músicas están descritas por escrito. Si algún movimiento te molesta, haz una versión más pequeña con las manos.",
    "Aprenderé a expresar lo que escucho con el cuerpo y el movimiento, y a explicar por qué elegí ese movimiento. Sirve para mostrar la música cuando no tengo palabras.",
    ["Sé caminar y detenerme.", "Sé qué es una evidencia sonora.", "Sé que lento y rápido son tempos."],
    [
        "El movimiento puede mostrar cualidades de la música. Si la música es lenta, los movimientos pueden ser lentos. Si es fuerte, los movimientos pueden ser grandes y firmes. Si es suave, pueden ser pequeños y delicados. Si los sonidos son agudos, puedes estirarte hacia arriba; si son graves, hacia abajo.",
        "Un movimiento bien elegido tiene un porqué sonoro. Por ejemplo: «hice movimientos lentos porque los pulsos iban lentos». Así tu movimiento no es solo bonito: está unido a lo que escuchaste. También puedes marcar el pulso con los pies y los acentos con un movimiento más grande.",
        "Cuida tu cuerpo y el de los demás. Mueve solo lo que te acomode. Si no quieres bailar, puedes hacer gestos con las manos o con la cabeza. No hay un movimiento correcto único, pero cada movimiento debe poder explicarse con algo que se oyó.",
    ],
    [("movimiento", "cambio de posición del cuerpo"), ("gesto", "movimiento pequeño, por ejemplo de las manos"), ("pulso", "latido parejo que puedes marcar con los pies"), ("grande y firme", "movimiento amplio con fuerza controlada"), ("pequeño y delicado", "movimiento corto y suave")],
    [
        ("Elegir movimiento para una música", "Música: suave, lenta y grave. ¿Qué movimiento le queda bien: (a) saltos grandes y rápidos, (b) movimientos pequeños y lentos hacia abajo?", ["La música es suave: movimientos suaves.", "La música es lenta: movimientos lentos.", "Es grave: hacia abajo."], "(b), porque coincide con suave, lenta y grave"),
        ("Contar movimientos", "Marchas 4 pasos al ritmo de la música y repites la marcha 3 veces. ¿Cuántos pasos das?", ["Cada marcha tiene 4 pasos.", "Se repite 3 veces: 4 × 3."], "12 pasos"),
    ],
    [
        ("Hacer un movimiento grande porque «se ve más bonito», sin relación con la música.", "El movimiento debe responder a lo que se escucha.", "Escucha primero y elige un movimiento que coincida con suave, fuerte, lento o rápido."),
        ("Mover todo el cuerpo cuando la música es muy suave.", "No coincide con la intensidad.", "Si la música es suave, los movimientos son pequeños."),
    ],
    [
        ex("La música es muy fuerte y firme. ¿El movimiento será pequeño o grande?", "Grande", "Fuerte y firme combina con movimientos amplios."),
        ex("Los sonidos son agudos. ¿Hacia dónde puedes estirar tu cuerpo?", "Hacia arriba", "Los sonidos agudos se asocian a lo alto."),
        ex("La música va lenta. ¿Qué tipo de pasos eliges: lentos o rápidos?", "Lentos", "El tempo del movimiento sigue el tempo de la música."),
    ],
    [
        ex("Música: rápida y suave. ¿Qué movimiento le queda bien: pasitos rápidos y pequeños o pasos lentos y grandes?", "Pasitos rápidos y pequeños", "Rápido combina con pasitos rápidos y suave con movimiento pequeño."),
        arith("Das un paso en cada pulso y la música tiene 16 pulsos. ¿Cuántos pasos das?", "16*1", "Un paso por pulso hace tantos pasos como pulsos.", " pasos"),
        ex("Música: A (suave y lenta) y B (fuerte y rápida). ¿Qué sección pide movimientos más grandes?", "La B", "La sección B es fuerte y rápida."),
    ],
    [
        ex("Tu movimiento es lento, pero la música suena rápida. ¿Cómo corriges?", "Aceleras el movimiento", "El movimiento debe seguir el tempo de la música."),
        arith("En una sección haces un gesto grande cada 4 pulsos para marcar el acento. En 16 pulsos, ¿cuántos gestos grandes haces?", "16//4", "Se reparten 16 pulsos en grupos de 4.", " gestos"),
    ],
    [
        ex("Para la música A suave y lenta usas gestos pequeños con las manos. Para la B, fuerte y rápida, usas pasos grandes. Si A dura 8 pulsos, B 8 y vuelve A 8, ¿cuántos pulsos hay de gestos pequeños?", "16", "Las dos secciones A suman 8 + 8 = 16 pulsos."),
        ex("¿Qué explicación une el movimiento con lo oído: (a) «Me moví porque sí.», (b) «Me moví despacio porque la música iba lenta.»?", "b", "La (b) da una razón basada en el tempo oído."),
    ],
    [
        arith("La música tiene 3 secciones de 8 pulsos cada una y das un paso por pulso. ¿Cuántos pasos das?", "3*8", "Son 3 secciones de 8 pasos cada una.", " pasos"),
        ex("Haces un gesto grande en cada acento, que cae cada 3 pulsos, durante 9 pulsos. ¿En qué pulsos haces el gesto grande?", "1, 4 y 7", "Los grupos son 1-2-3, 4-5-6 y 7-8-9; el gesto va al inicio de cada uno."),
    ],
    [ex("Una niña no quiere bailar frente a otras personas. ¿Qué puede hacer para mostrar la música sin sentirse expuesta?", "Hacer gestos pequeños con las manos desde su lugar", "Los gestos con las manos expresan la música sin exponerse.")],
    [ex("Música fuerte: ¿movimiento grande o pequeño?", "Grande", "Fuerte combina con movimientos amplios."), ex("Música suave: ¿movimiento firme o delicado?", "Delicado", "Suave combina con movimientos delicados."), ex("¿Qué debe tener todo movimiento que eliges?", "Una razón basada en lo que oíste", "El movimiento debe poder explicarse con evidencia sonora.")],
    (
        "Una persona de tu casa te da golpecitos con los dedos sobre la mesa: 8 pulsos suaves y lentos (parte A) y 8 pulsos fuertes y rápidos (parte B). Responde con tu cuerpo en un espacio seguro: elige un movimiento para A y otro para B. Dibuja o escribe cuál elegiste para cada parte y explica por qué, con una evidencia sonora.",
        "Para A hice movimientos pequeños y lentos con los brazos porque los golpes eran suaves y lentos. Para B di pasos grandes y rápidos porque los golpes eran fuertes y rápidos.",
        ["elige un movimiento distinto para cada parte", "explica con evidencia sonora", "se mueve con cuidado y respeta su espacio"],
        ["movimiento", "explicación escrita u oral"],
        ["explicar solo con «me gustó»", "moverse sin relación con la intensidad o el tempo"],
        "Reconoce el cuidado al moverse y pregunta qué oyó para elegir cada movimiento; ofrece alternativa de gestos con las manos.",
    ),
    "Mueve solo las manos al ritmo de una música lenta y luego de una rápida que recuerdes. Cuenta cómo cambiaron.",
    "Crea una secuencia de tres movimientos para una música A B A y dibújala con cajas.",
)

# ---------------------------------------------------------------- OA 02 · clase 3
CODG = "Código gráfico acordado: la altura se muestra con la posición (agudo = arriba, grave = abajo); la intensidad con el grosor del trazo (fuerte = grueso, suave = fino); la duración con el largo de la línea (cada ━ = 1 pulso)"

L(
    OA2, 3,
    f"Papel, lápiz y lápices de colores si tienes. {CODG}. Es un acuerdo de esta clase; otras personas pueden usar otros códigos.",
    "Aprenderé a traducir una cualidad del sonido a una imagen con un código acordado. Sirve para dibujar la música y compartirla sin palabras.",
    ["Sé nombrar altura, intensidad y duración.", "Sé que cada línea puede ser larga o corta.", "Sé diferenciar suave y fuerte."],
    [
        f"Una imagen puede mostrar la música si antes acordamos qué significa cada rasgo. {CODG}. Con este código, una línea alta, gruesa y larga muestra un sonido agudo, fuerte y largo. Una línea baja, fina y corta muestra un sonido grave, suave y corto.",
        "Los códigos no son verdades universales: son acuerdos. Por eso, siempre que dibujes la música, escribe al lado una pequeña clave que explique qué significa cada rasgo. Así otra persona puede leer tu dibujo y comprobar si coincide con lo que se oyó.",
        "También las imágenes pueden mostrar sensaciones: usar colores cálidos o fríos, formas redondas o con picos. Esos usos son personales y se explican con evidencia sonora: «dibujé formas con picos porque los sonidos eran fuertes y cortos». Primero la cualidad y después la imagen.",
    ],
    [("código gráfico", "acuerdo que dice qué significa cada rasgo del dibujo"), ("clave", "nota al lado del dibujo que explica el código"), ("trazo", "línea que se dibuja"), ("posición", "qué tan arriba o abajo está el trazo"), ("grosor", "qué tan gruesa o fina es la línea")],
    [
        ("Leer un dibujo", f"{CODG}. Un trazo está arriba, es fino y mide 3 pulsos de largo. ¿Cómo suena el sonido que muestra?", ["Arriba: agudo.", "Fino: suave.", "3 pulsos: dura 3 pulsos."], "Agudo, suave y de 3 pulsos"),
        ("Dibujar un sonido", f"{CODG}. Dibuja con palabras un sonido grave, fuerte y de 2 pulsos.", ["Grave: abajo.", "Fuerte: trazo grueso.", "2 pulsos: dos ━ de largo."], "Un trazo grueso, abajo, de 2 ━"),
    ],
    [
        ("Usar el color para decir fuerte sin avisar que es un acuerdo.", "Otra persona no sabría leerlo.", "Escribe una clave al lado."),
        ("Dibujar un trazo largo para un sonido corto.", "La duración se muestra con el largo de la línea.", "Dibuja el largo según los pulsos."),
    ],
    [
        ex(f"{CODG}. Un trazo grueso significa que el sonido es ¿fuerte o suave?", "Fuerte", "Según el código, el grosor muestra la intensidad."),
        ex(f"{CODG}. Un trazo ubicado muy abajo muestra un sonido ¿agudo o grave?", "Grave", "Según el código, abajo es grave."),
        ex(f"{CODG}. Un trazo de ━━━━ muestra un sonido que dura ¿cuántos pulsos?", "4", "Cada ━ es 1 pulso y hay cuatro."),
    ],
    [
        ex(f"{CODG}. Dibuja con rayas un sonido de 5 pulsos y escribe cuántas rayas usaste.", "5", "Cada pulso se dibuja con una raya."),
        ex(f"{CODG}. Un trazo está arriba, es grueso y mide 1 pulso. ¿Es agudo o grave, fuerte o suave, largo o corto?", "Agudo, fuerte y corto", "Arriba es agudo, grueso es fuerte y 1 pulso es corto."),
        ex(f"{CODG}. Dos trazos tienen igual posición y grosor, pero uno mide 2 pulsos y otro 6. ¿Qué cualidad cambia?", "La duración", "Solo cambia el largo de la línea."),
    ],
    [
        arith(f"{CODG}. Dibujas tres trazos de 2, 3 y 4 pulsos. ¿Cuántos pulsos son en total?", "2+3+4", "Se suman los pulsos de los tres trazos.", " pulsos"),
        ex(f"{CODG}. Quieres mostrar un sonido que sube de grave a agudo poco a poco. ¿Cómo dibujas el trazo?", "Un trazo que sube de abajo hacia arriba", "La posición del trazo muestra la altura, así que sube."),
    ],
    [
        ex("Juan dibujó formas con picos y dijo: «porque los sonidos eran fuertes y cortos». Pedro dibujó círculos y dijo: «porque eran suaves y largos». ¿Alguno se equivoca?", "Ninguno", "Los dos explican su dibujo con rasgos sonoros."),
        ex(f"{CODG}. Dibujo A: trazo arriba, fino, 2 ━. Dibujo B: trazo abajo, grueso, 2 ━. ¿Qué dos cualidades cambian?", "La altura y la intensidad", "Cambian la posición y el grosor; la duración es igual."),
    ],
    [
        ex(f"{CODG}. Un sonido agudo, suave de 2 pulsos y uno grave, fuerte de 3 pulsos. ¿Cuál trazo es más largo y cuál es más grueso?", "El grave y fuerte es más largo y más grueso", "Tiene 3 pulsos contra 2 y es fuerte."),
        arith("Un dibujo tiene 4 trazos y cada uno mide 3 pulsos. ¿Cuántos pulsos en total?", "4*3", "Hay 4 trazos de 3 pulsos cada uno.", " pulsos"),
    ],
    [ex("Dibujas la música de una tormenta: trazos gruesos, abajo y largos. ¿Qué rasgos sonoros muestra?", "Graves, fuertes y largos", "Abajo es grave, grueso es fuerte y largo es de mucha duración.")],
    [ex("¿Qué debes escribir al lado de un dibujo para que otros lo lean?", "Una clave", "La clave explica el código."), ex("En el código de esta clase, ¿qué muestra el grosor?", "La intensidad", "Grueso es fuerte y fino es suave."), ex("¿Qué muestra el largo de la línea?", "La duración", "Cada ━ es un pulso.")],
    (
        "Una persona de tu casa toca con una cuchara sobre una olla: 1 golpe fuerte, 1 golpe suave y 3 golpes suaves seguidos. Dibuja los cinco golpes como trazos usando el código de esta clase (mismo largo para todos, porque son golpes cortos). Escribe una clave al lado y una frase que diga qué cualidad mostraste con cada rasgo.",
        "Clave: grueso es fuerte, fino es suave. Dibujé un trazo grueso y cuatro finos. Con el grosor mostré la intensidad.",
        ["dibuja cinco trazos en orden", "usa el grosor correcto", "escribe una clave y explica"],
        ["dibujo", "clave escrita", "explicación breve"],
        ["no escribir la clave", "usar grosores que no coinciden con lo que sonó"],
        "Reconoce el dibujo con clave y pide que lea su dibujo como si fuera de otra persona.",
    ),
    "Dibuja con un solo trazo un sonido largo y suave y con otro un sonido corto y fuerte.",
    "Inventa tu propio código gráfico de tres reglas y dibuja con él una música de cuatro sonidos.",
)

# ---------------------------------------------------------------- OA 02 · clase 4
RUB = "Nivel 1: solo una opinión («me gustó»). Nivel 2: una evidencia sonora, con o sin opinión, sin llegar al nivel 3. Nivel 3: evidencia sonora, una idea o emoción y además un gesto, un dibujo o un sonido que la muestre"
RESP = {
    "a": "«Me gustó mucho.»",
    "b": "«Me gustó porque sonaba lenta y suave.»",
    "c": "«Sonaba lenta y suave, por eso imaginé un barco que se mece, y lo dibujé con olas largas.»",
    "d": "«Fue entretenida.»",
}

L(
    OA2, 4,
    f"Papel y lápices. Una música descrita por escrito en cada ejercicio. Rúbrica de esta clase: {RUB}.",
    "Aprenderé a construir una respuesta con grados crecientes de elaboración, combinando palabra, gesto, dibujo o sonido. Sirve para decir lo que me sugiere la música con evidencia y con más de un medio.",
    ["Sé separar lo oído de lo imaginado.", "Sé usar «por eso».", "Sé dibujar con un código."],
    [
        f"Una respuesta puede ser más o menos elaborada. {RUB}. Cuanto más elaborada, más claro queda qué oíste y qué te sugirió.",
        f"Veamos ejemplos. {RESP['a']} es nivel 1: solo opinión. {RESP['b']} es nivel 2: da una evidencia sonora. {RESP['c']} es nivel 3: tiene evidencia, una idea y un medio expresivo (el dibujo). Para subir de nivel basta con añadir algo que falta, no hay que escribir mucho.",
        "Los medios expresivos son la palabra (decir o escribir), el cuerpo (gesto o movimiento), la música (tocar o cantar) y lo visual (dibujar). Puedes combinar dos o tres. Elige los medios con los que te sientas cómodo y cuida de no exponer más de lo que quieres.",
    ],
    [("elaboración", "qué tan completa y bien apoyada está una respuesta"), ("medio expresivo", "forma de mostrar lo que sientes: palabra, cuerpo, música o imagen"), ("evidencia sonora", "algo que se oyó"), ("idea", "lo que la música te hace imaginar"), ("opinión", "decir si algo te gustó o no")],
    [
        ("Clasificar un nivel", f"Respuesta: {RESP['b']} ¿Qué nivel tiene según la rúbrica?", ["Tiene opinión: me gustó.", "Tiene evidencia sonora: lenta y suave.", "No tiene idea ni medio expresivo adicional."], "Nivel 2"),
        ("Subir de nivel", f"La respuesta {RESP['d']} es nivel 1. ¿Qué agregarías para que sea nivel 2?", ["Nivel 2 pide una evidencia sonora.", "Digo qué se oyó: por ejemplo, rápida y alegre."], "Una evidencia sonora, por ejemplo que sonó rápida"),
    ],
    [
        ("Pensar que más largo siempre es mejor.", "Lo importante es lo que contiene la respuesta.", "Revisa si hay evidencia, idea y medio expresivo."),
        ("Saltarse la evidencia sonora para llegar a la idea.", "La idea queda sin apoyo.", "Primero di qué oíste y luego lo que imaginaste."),
    ],
    [
        ex(f"Rúbrica: {RUB}. Respuesta: {RESP['a']} ¿Qué nivel tiene?", "Nivel 1", "Es solo una opinión."),
        ex(f"Rúbrica: {RUB}. Respuesta: {RESP['c']} ¿Qué nivel tiene?", "Nivel 3", "Tiene evidencia sonora, una idea y un dibujo."),
        ex("¿Cuáles dos de estas cosas son medios expresivos para responder a la música: palabra, tabla de multiplicar, dibujo, calculadora?", "Palabra y dibujo", "Los medios expresivos son la palabra, el cuerpo, la música y lo visual."),
    ],
    [
        ex(f"Rúbrica: {RUB}. Respuesta: {RESP['d']} ¿Qué nivel tiene?", "Nivel 1", "Es solo una opinión, sin evidencia."),
        ex(f"Rúbrica: {RUB}. Respuesta: «Escuché golpes fuertes y rápidos.» ¿Qué le falta para nivel 3?", "Una idea o emoción y un gesto, un dibujo o un sonido", "Tiene evidencia, pero falta lo demás."),
        ex(f"Rúbrica: {RUB}. Respuesta: «Sonaba suave, por eso sentí calma, y moví los brazos despacio.» ¿Qué nivel tiene?", "Nivel 3", "Tiene evidencia, una emoción y un gesto."),
    ],
    [
        ex(f"Ordena de menor a mayor nivel: (a) {RESP['c']} (b) {RESP['a']} (c) {RESP['b']}", "b, c, a", "La (b) es nivel 1, la (c) es nivel 2 y la (a) es nivel 3."),
        ex("Una música tiene sonidos graves y fuertes. ¿Cuál respuesta llega al nivel 3: (a) «Escuché sonidos graves y fuertes.» (b) «Escuché sonidos graves y fuertes, por eso imaginé un gigante, y caminé con pasos pesados.»?", "b", "La (b) suma una idea y un gesto a la evidencia; la (a) se queda en la evidencia."),
    ],
    [
        ex("Pedro responde: «La música tenía muchos instrumentos y me dio alegría». Lucía dice: «Me dio alegría». ¿Quién tiene mayor elaboración y por qué?", "Pedro, porque dio una evidencia sonora", "Pedro apoya su sensación con algo que se oyó."),
        arith("Mejoras tu respuesta nivel 1 agregando 1 evidencia y 1 idea. Si cada parte tiene 1 oración, ¿cuántas oraciones tiene tu respuesta final?", "1+1+1", "Se suma la opinión, la evidencia y la idea.", " oraciones"),
    ],
    [
        ex("Alguien dice: «Escuché sonidos agudos, me dio alegría y salté contento». ¿Qué nivel tiene?", "Nivel 3", "Tiene evidencia, una emoción y un gesto (el salto)."),
        ex("Alguien dice: «Escuché sonidos agudos y me dio alegría». ¿Qué nivel tiene y qué le falta?", "Nivel 2; le falta un gesto, un dibujo o un sonido", "Tiene evidencia, pero no muestra la idea con otro medio."),
    ],
    [ex("Un niño escucha un tambor lento y grave. Dice: «Escuché un tambor grave y lento, me dio un poco de miedo, y lo dibujé con círculos oscuros». ¿Qué nivel tiene su respuesta?", "Nivel 3", "Tiene evidencia sonora, una emoción y un medio visual.")],
    [ex("¿Qué nivel tiene una respuesta que solo dice «no me gustó»?", "Nivel 1", "Es una opinión sin evidencia."), ex("¿Qué se agrega para pasar de nivel 1 a nivel 2?", "Una evidencia sonora", "Se explica qué se oyó."), ex("¿Qué se agrega para pasar de nivel 2 a nivel 3?", "Una idea o emoción y un gesto, un dibujo o un sonido", "Se suma lo imaginado y una forma de mostrarlo.")],
    (
        "Una persona de tu casa toca 8 golpes suaves y lentos en una mesa y luego 4 golpes fuertes. Escribe una respuesta nivel 3 con: una evidencia sonora, una idea o emoción y un medio expresivo (dibujo, gesto o sonido). Si quieres, muestra el gesto o el dibujo a esa persona y pregúntale qué entendió.",
        "Escuché golpes suaves y lentos, por eso sentí calma, y después cuatro golpes fuertes que me sorprendieron. Hice un dibujo de ondas pequeñas y luego una gran.",
        ["incluye evidencia sonora", "incluye idea o emoción", "usa al menos un medio expresivo y lo explica"],
        ["respuesta escrita", "dibujo o gesto"],
        ["quedarse en la opinión", "olvidar el medio expresivo"],
        "Reconoce el nivel que alcanzó y pregunta por la pieza que falta para el siguiente.",
    ),
    "Escribe una respuesta de nivel 2 sobre un sonido que escuches hoy.",
    "Transforma una respuesta de nivel 1 en una de nivel 3 sobre una música que conozcas, sin copiar su letra.",
)
