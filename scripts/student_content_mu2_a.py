"""Student material for 2.º básico Música, OA 01 (cualidades y estructuras) y OA 02 (sensaciones e ideas)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1, OA2 = "MU02 OA 01", "MU02 OA 02"

TA, TT, SIL = "TA", "ti-ti", "SIL"
LEY = "TA = 1 sonido en 1 pulso; ti-ti = 2 sonidos rápidos en 1 pulso; SIL = 1 pulso de silencio"
CODIGO = "o = sonido suave, O = sonido fuerte, cada ━ = 1 pulso de duración"


def P(*tokens: str) -> str:
    return " – ".join(tokens)


def pulses(*tokens: str) -> int:
    return len(tokens)


def sounds(*tokens: str) -> int:
    return sum({TA: 1, TT: 2, SIL: 0}[t] for t in tokens)


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- OA 01 · clase 1
L(
    OA1, 1,
    f"Lápiz, papel, una olla o un tarro con una cuchara de madera y tus palmas. Código para dibujar sonidos: {CODIGO}. Todo lo que se escucha en los ejercicios está descrito por escrito.",
    "Aprenderé a describir un sonido con cuatro cualidades: altura, timbre, intensidad y duración, y a dibujarlas. Sirve para hablar de la música con palabras exactas.",
    ["Sé que un sonido puede ser fuerte o suave.", "Sé que un sonido puede ser largo o corto.", "Sé distinguir un sonido fino de uno hondo."],
    [
        "Todo sonido tiene cuatro cualidades. La altura dice si el sonido es agudo (fino, como un pajarito) o grave (hondo, como un tambor grande). La intensidad dice si suena fuerte o suave. La duración dice cuánto tiempo suena: largo o corto. El timbre es el color del sonido y dice quién suena: una voz, una cuchara o una campana.",
        f"Las cualidades son independientes: un sonido puede ser agudo y suave, o grave y fuerte. Por eso las preguntamos una por una. También podemos dibujarlas. Usamos este código: {CODIGO}. Así, «O ━━━» es un sonido fuerte que dura 3 pulsos, y «o ━» es un sonido suave que dura 1 pulso.",
        "Para describir un sonido hazte cuatro preguntas: ¿es agudo o grave?, ¿es fuerte o suave?, ¿es largo o corto?, ¿qué lo produce? Escucha dos veces: la primera para sentirlo y la segunda para responder con una pista que realmente oíste.",
    ],
    [("agudo", "sonido fino, de tono alto"), ("grave", "sonido hondo, de tono bajo"), ("intensidad", "qué tan fuerte o suave suena"), ("duración", "cuánto tiempo suena"), ("timbre", "el color del sonido; dice quién suena")],
    [
        ("Describir y dibujar un cascabel", "Un cascabel suena fino, flojito, y se apaga rápido (1 pulso). Descríbelo y dibújalo con el código.", ["Altura: suena fino, así que es agudo.", "Intensidad: suena flojito, así que es suave.", "Duración: se apaga rápido, 1 pulso, así que es corto.", "Dibujo con el código: o ━."], "Agudo, suave, corto; se dibuja «o ━»"),
        ("Separar altura de intensidad", "Una niña dice: «el silbido de papá es agudo, entonces es fuerte». ¿Tiene razón?", ["Agudo habla de la altura; fuerte habla de la intensidad.", "Un silbido puede ser agudo y a la vez muy suave, si se silba bajito."], "No necesariamente: son dos cualidades distintas"),
    ],
    [
        ("Decir que todo sonido agudo es fuerte.", "Se mezclan la altura y la intensidad.", "Pregunta primero «¿fino u hondo?» y después «¿fuerte o suave?»."),
        ("Decir que un sonido es largo porque parte con un golpe fuerte.", "Se confunden duración e intensidad.", "Cuenta cuánto tiempo se oye el sonido, no qué tan fuerte parte."),
    ],
    [
        ex("Una gota cae en un vaso y hace un «tic» muy breve. ¿El sonido es largo o corto?", "Corto", "El «tic» se acaba casi al instante, así que su duración es corta."),
        ex("Un tambor grande hace un «bum» hondo. ¿Su altura es aguda o grave?", "Grave", "Un sonido hondo y de tono bajo es grave."),
        ex("¿Cómo se llama la cualidad que dice quién suena: una flauta, una cuchara o una voz?", "El timbre", "El timbre es el color del sonido y nos dice qué lo produce."),
    ],
    [
        ex("Dices «sol» muy bajito y después muy fuerte, con el mismo tono de voz. ¿Qué cualidad cambió?", "La intensidad", "Cambió qué tan fuerte suena, y eso es la intensidad."),
        ex(f"Observa el código ({CODIGO}). El sonido A es «o ━» y el sonido B es «O ━━━━». ¿B es más fuerte o más suave que A, y más largo o más corto?", "Más fuerte y más largo", "O mayúscula es fuerte y cuatro rayas duran más que una."),
        ex("Ordena de menor a mayor duración: (a) ━━━, (b) ━, (c) ━━━━━.", "b, a, c", "Tienen 1, 3 y 5 pulsos de duración; se ordenan de 1 a 5."),
    ],
    [
        ex(f"Escribe con el código ({CODIGO}) un sonido fuerte que dure 3 pulsos.", "O ━━━", "O mayúscula indica fuerte y tres rayas indican 3 pulsos."),
        arith(f"Un patrón dibujado es: o ━, O ━━, o ━━━. Con el código ({CODIGO}), ¿cuántos pulsos suenan en total?", "1+2+3", "Se suman las rayas de cada sonido: 1, 2 y 3.", " pulsos"),
        ex("Escribe A (aguda) o G (grave) para cada sonido: (a) chiflido de un pájaro, (b) bocina de un barco grande, (c) zumbido de un mosquito.", "a A, b G, c A", "El pájaro y el mosquito suenan finos; la bocina grande suena hondo."),
    ],
    [
        ex("Dos tambores se golpean con la misma fuerza durante el mismo tiempo, pero uno es de lata y otro es de madera, y suenan distinto. ¿Qué cualidad explica la diferencia y por qué no es la intensidad?", "El timbre, porque la fuerza fue la misma", "Si la fuerza es igual, lo distinto es el material que suena: el timbre."),
        ex("Sonido A: grave, suave y largo. Sonido B: agudo, suave y largo. ¿Qué cualidad es la única diferente?", "La altura", "Los dos son suaves y largos; solo cambia agudo contra grave."),
    ],
    [
        arith("El sonido B dura 3 pulsos. Quieres que el sonido A dure 2 pulsos más que B. ¿Cuántos pulsos debe durar A?", "3+2", "Se agregan 2 pulsos a los 3 de B.", " pulsos"),
        ex(f"Con el código ({CODIGO}), escribe dos sonidos seguidos que cambien SOLO la intensidad. El primero es suave y dura 2 pulsos.", "o ━━ y luego O ━━", "El segundo debe durar igual (2 pulsos) y ser fuerte para que solo cambie la intensidad."),
    ],
    [ex("En el recreo, la campana suena fuerte y por mucho rato; una pelota que bota hace un «pof» suave y breve. Di la intensidad y la duración de cada una.", "Campana: fuerte y larga; pelota: suave y corta", "La campana se oye fuerte y dura; el «pof» es flojo y se acaba rápido.")],
    [ex("¿Qué cualidad cambia cuando pasas de un susurro a un grito?", "La intensidad", "Se pasa de suave a fuerte."), ex("Un trueno lejano, ¿es agudo o grave?", "Grave", "El trueno suena hondo."), ex("Nombra las cuatro cualidades del sonido.", "Altura, timbre, intensidad y duración", "Son las cuatro preguntas para describir cualquier sonido.")],
    (
        f"Golpea una olla (o la mesa) con una cuchara de madera. Haz tres sonidos: uno suave y corto, uno fuerte y corto, y uno fuerte y largo (déjalo sonar apagando con la mano al final). Dibújalos con el código ({CODIGO}) y escribe qué cualidad cambió entre el primero y el segundo, y entre el segundo y el tercero.",
        "Dibujé: o ━, O ━, O ━━━. Del primero al segundo cambió la intensidad. Del segundo al tercero cambió la duración.",
        ["produce los tres sonidos pedidos", "dibuja cada sonido con el código", "nombra la cualidad que cambió en cada paso"],
        ["interpretación con objeto", "dibujo con código", "explicación oral o escrita"],
        ["decir que cambió la altura cuando solo cambió la fuerza", "dibujar la duración sin relación con lo que sonó"],
        "Reconoce el dibujo claro y pregunta qué pista audible mostró cada cambio; si dice «me gustó», pide que diga si sonó fuerte o suave, largo o corto.",
    ),
    "Elige tres objetos de tu casa seguros para golpear. Golpéalos suavemente y di de cada uno si suena agudo o grave.",
    "Busca un sonido agudo y largo y otro grave y corto. Dibújalos con el código y explica por qué cada uno cumple.",
)

# ---------------------------------------------------------------- OA 01 · clase 2
L(
    OA1, 2,
    f"Lápiz, tus palmas y tus pasos. Leyenda: {LEY}. Todos los patrones están escritos en cada ejercicio.",
    "Aprenderé a distinguir pulso, acento y patrón, y a contar pulsos en grupos de 2, 3 y 4. Sirve para marchar, bailar y tocar con otras personas sin perderse.",
    ["Sé caminar al mismo paso varias veces.", "Sé contar hasta 20.", "Sé lo que son TA, ti-ti y SIL."],
    [
        "El pulso es el latido de la música. Es parejo, como tus pasos al caminar. Podemos contarlo: 1, 2, 3, 4. El acento es el pulso que se marca más fuerte. Si cuentas 1, 2, 3, 4 y dices el 1 con más fuerza, el acento cae en el 1 y se repite cada 4 pulsos.",
        f"Los pulsos se agrupan de a 2, de a 3 o de a 4, y el acento va al comienzo de cada grupo. En grupos de 3 se cuenta 1-2-3, 1-2-3. El patrón es una secuencia de sonidos que se repite sobre el pulso. Por ejemplo, {P(TA, TT, TA, SIL)}. Aquí hay 4 pulsos, y el silencio también cuenta.",
        "No confundas pulso con ritmo. El pulso se mantiene parejo. El ritmo es lo que suena sobre el pulso, y puede tener sonidos rápidos, lentos y silencios. Camina el pulso con los pies y toca el patrón con las palmas para sentir la diferencia.",
    ],
    [("pulso", "latido parejo de la música"), ("acento", "pulso que se marca más fuerte"), ("patrón", "secuencia de sonidos que se repite"), ("ritmo", "lo que suena sobre el pulso"), ("grupo de pulsos", "pulsos que se cuentan juntos, con el acento al inicio")],
    [
        ("Contar pulsos y sonidos", f"¿Cuántos pulsos y cuántos sonidos tiene {P(TA, TT, TA, SIL)}?", ["Cada símbolo ocupa un pulso: TA, ti-ti, TA, SIL. Son 4 pulsos.", "Sonidos: TA suena 1, ti-ti suena 2, TA suena 1 y SIL no suena: 1 + 2 + 1 = 4."], f"{pulses(TA, TT, TA, SIL)} pulsos y {sounds(TA, TT, TA, SIL)} sonidos"),
        ("Ubicar los acentos", "Cuento 12 pulsos en grupos de 3, con acento en el primero de cada grupo. ¿En qué números caen los acentos?", ["Los grupos son 1-2-3, 4-5-6, 7-8-9 y 10-11-12.", "El acento va al inicio de cada grupo."], "En los pulsos 1, 4, 7 y 10"),
    ],
    [
        ("Decir que ti-ti son dos pulsos.", "Se cuentan los sonidos y no los latidos.", "ti-ti son dos sonidos rápidos dentro de un solo pulso."),
        ("Saltarse el silencio al contar los pulsos.", "Se piensa que si no suena nada, no cuenta.", "El silencio ocupa un pulso; cuéntalo en voz baja."),
    ],
    [
        arith("Caminas diciendo 1-2-3-4 y 1-2-3-4. ¿Cuántos pulsos dices en total?", "4+4", "Cada grupo tiene 4 pulsos y hay dos grupos.", " pulsos"),
        ex("En 1-2-3-4 el acento va en el 1. ¿Qué números se dicen suaves?", "2, 3 y 4", "Solo el 1 lleva acento; los otros pulsos van suaves."),
        ex("¿Qué se mantiene parejo mientras cambia la melodía: el pulso o el acento?", "El pulso", "El pulso es el latido que no cambia aunque cambie lo que suena."),
    ],
    [
        ex("Cuentas de a 3: 1-2-3, 1-2-3, 1-2-3, con acento en cada 1. ¿Cuántos acentos hay?", "3", "Hay tres grupos y cada grupo tiene un acento."),
        ex(f"Cuenta los pulsos de este patrón (el silencio cuenta): {P(TA, TA, TT, TA, SIL, TA)}.", str(pulses(TA, TA, TT, TA, SIL, TA)), "Hay seis símbolos y cada uno ocupa un pulso."),
        ex("Un ti-ti, ¿ocupa 1 pulso o 2 pulsos?", "1 pulso", "Sus dos sonidos rápidos caben en un solo pulso."),
    ],
    [
        ex("Cuenta 12 pulsos en grupos de 3 con el acento en el primero de cada grupo. Escribe los números donde caen los acentos.", "1, 4, 7 y 10", "Cada grupo parte tres números después del anterior: 1, 4, 7, 10."),
        ex(f"Cuenta los sonidos de este patrón de 8 pulsos: {P(TA, TA, TT, SIL, TT, TT, TA, SIL)}.", str(sounds(TA, TA, TT, SIL, TT, TT, TA, SIL)), "Suman 1 + 1 + 2 + 0 + 2 + 2 + 1 + 0, porque el silencio no suena."),
        arith("Un patrón de 8 pulsos tiene 3 silencios. ¿Cuántos pulsos suenan?", "8-3", "A los 8 pulsos se les quitan los 3 que están en silencio.", " pulsos"),
    ],
    [
        ex("Luis dice: «si toco más rápido, el pulso cambió a ti-ti». ¿Tiene razón?", "No; ti-ti son dos sonidos en un mismo pulso y el pulso sigue igual", "Un ti-ti divide un pulso en dos sonidos, pero el latido no cambia."),
        ex("En una marcha el acento va cada 2 pasos (1-2, 1-2...). En 8 pasos, ¿cuántos acentos hay?", "4", "Con grupos de 2, 8 pasos forman 4 grupos y cada uno lleva un acento."),
    ],
    [
        ex("Quieres un acento cada 4 pulsos durante 16 pulsos. ¿En qué números caen los acentos?", "1, 5, 9 y 13", "Cada grupo de 4 empieza 4 números después del anterior."),
        ex("Un grupo de 3 pulsos con acento al inicio se repite 5 veces. ¿Cuántos pulsos y cuántos acentos hay en total?", "15 pulsos y 5 acentos", "Hay 5 grupos de 3 pulsos y cada grupo tiene un acento: 3 × 5 = 15."),
    ],
    [arith("En un baile se da un paso en cada pulso y un golpe de pie más fuerte cada 4 pasos. En 20 pasos, ¿cuántos golpes fuertes se dan?", "20//4", "Se reparten 20 pasos en grupos de 4; cada grupo tiene un golpe fuerte.", " golpes")],
    [ex(f"¿Cuántos pulsos tiene {P(SIL, TA, SIL, TA)}?", "4", "Los silencios también ocupan un pulso."), ex(f"¿Cuántos sonidos tiene {P(TA, TA, SIL, SIL)}?", "2", "Solo suenan los dos TA."), ex("En una canción, ¿qué es un patrón de ritmo?", "Una secuencia de sonidos que se repite", "Un patrón es una secuencia que vuelve a sonar sobre el pulso.")],
    (
        f"Camina en tu lugar con paso parejo. Toca con las palmas el patrón {P(TA, TA, TT, SIL)} cuatro veces seguidas y marca más fuerte el primer pulso de cada vuelta. Escribe cuántos pulsos y cuántos sonidos tiene el patrón y cuántos pulsos tocaste en total.",
        "Toqué el patrón cuatro veces. Cada vez tiene 4 pulsos y 4 sonidos (1 + 1 + 2 + 0). En total toqué 16 pulsos. El acento fue el primer TA de cada vuelta.",
        ["mantiene el pulso parejo con los pies", "toca el patrón con el silencio en su lugar", "escribe 4 pulsos, 4 sonidos y 16 pulsos en total"],
        ["interpretación", "conteo escrito", "explicación oral del acento"],
        ["no contar el silencio como pulso", "acelerar en el ti-ti"],
        "Reconoce el pulso estable y pide que muestre con el dedo dónde está el silencio; si cuenta 5 pulsos, repite despacio con una palabra por pulso.",
    ),
    "Camina 16 pasos parejos y aplaude solo en cada cuarto paso. Cuenta cuántos aplausos diste.",
    "Prueba un acento cada 3 pasos en lugar de cada 4 y cuenta cuántos acentos caben en 12 pasos.",
)

# ---------------------------------------------------------------- OA 01 · clase 3
PAT = (TA, TT, TA, SIL)
L(
    OA1, 3,
    f"Lápiz, tus palmas y un cuaderno para anotar. Leyenda: {LEY}. Los patrones están escritos en cada ejercicio.",
    "Aprenderé a reconocer un patrón que regresa, a contarlo cuando se repite y a encontrar dónde cambia. Sirve para tocar acompañamientos y no perderme.",
    ["Sé contar pulsos y sonidos de un patrón.", "Sé que el silencio ocupa un pulso."],
    [
        f"Un patrón que regresa se llama ostinato. Es una secuencia corta que se repite una y otra vez, como una huella que vuelve a aparecer. Por ejemplo, {P(*PAT)} se puede tocar tres veces seguidas. Cada vuelta dura 4 pulsos, así que tres vueltas duran 12 pulsos.",
        "Para decidir si un patrón regresó igual, compara vuelta por vuelta y pulso por pulso. Si todos los símbolos coinciden, es el mismo patrón. Si cambia un símbolo, aunque sea uno, ya es una variación: un patrón parecido pero no igual.",
        "Un patrón que se repite ayuda a la música. Da seguridad a quien toca, y deja que otra persona cante o improvise encima. Para anotar cuántas veces suena, usa palitos: | | | significa tres vueltas.",
    ],
    [("patrón", "secuencia corta de sonidos y silencios"), ("ostinato", "patrón que se repite varias veces"), ("vuelta", "una vez que suena el patrón completo"), ("variación", "patrón parecido pero con algo cambiado"), ("repetir", "tocar otra vez lo mismo")],
    [
        ("Contar tres vueltas", f"El patrón {P(*PAT)} se toca 3 veces. ¿Cuántos pulsos y cuántos sonidos suenan?", [f"Una vuelta tiene {pulses(*PAT)} pulsos y {sounds(*PAT)} sonidos.", f"Tres vueltas: {pulses(*PAT)} × 3 = {pulses(*PAT)*3} pulsos y {sounds(*PAT)} × 3 = {sounds(*PAT)*3} sonidos."], f"{pulses(*PAT)*3} pulsos y {sounds(*PAT)*3} sonidos"),
        ("Encontrar la variación", f"Vuelta 1: {P(TA, TT, TA, SIL)}. Vuelta 2: {P(TA, TT, SIL, TA)}. ¿Regresó igual?", ["Comparo pulso por pulso.", "Los pulsos 1 y 2 coinciden.", "En el pulso 3, la vuelta 1 tiene TA y la vuelta 2 tiene SIL; en el pulso 4 pasa al revés."], "No; cambian los pulsos 3 y 4"),
    ],
    [
        ("Decir que un patrón es igual solo porque tiene los mismos símbolos.", "El orden también importa.", "Compara pulso por pulso, en el mismo lugar."),
        ("Dejar de contar la vuelta en que hay silencio.", "Se olvida que el silencio ocupa un pulso.", "Cuenta en voz baja el pulso del silencio."),
    ],
    [
        ex("¿Cómo se llama un patrón corto que se repite muchas veces?", "Ostinato", "Un ostinato es un patrón que regresa una y otra vez."),
        ex(f"El patrón {P(TA, SIL, TA, SIL)} se toca una sola vez. ¿Cuántos pulsos dura?", "4", "Cuatro símbolos ocupan cuatro pulsos, aunque haya silencios."),
        ex("Marcas | | | | en tu cuaderno cuando suena un patrón. ¿Cuántas vueltas tocaste?", "4", "Hay un palito por vuelta y dibujaste cuatro."),
    ],
    [
        ex(f"Compara {P(TA, TT, TA, SIL)} con {P(TA, TT, TA, SIL)}. ¿Es el mismo patrón?", "Sí", "Los cuatro símbolos coinciden uno a uno."),
        ex(f"¿Cuántos silencios hay en {P(TA, SIL, TT, SIL)}?", "2", "Se cuentan los SIL que aparecen: uno en el pulso 2 y otro en el pulso 4."),
        ex("¿Cuál es el patrón que se repite en TA – SIL – TA – SIL – TA – SIL – TA – SIL: «TA – SIL» o «TA – TA»?", "TA – SIL", "Cada dos pulsos aparece un TA seguido de un SIL."),
    ],
    [
        ex(f"El patrón {P(TA, TA, SIL, TA)} se repite 2 veces. Escribe cómo queda completo.", P(TA, TA, SIL, TA, TA, TA, SIL, TA), "Se copia el patrón dos veces seguidas, símbolo por símbolo."),
        arith("Un patrón de 4 pulsos se toca 5 veces. ¿Cuántos pulsos suenan en total?", "4*5", "Se repiten 4 pulsos cinco veces.", " pulsos"),
        ex(f"Cuenta cuántos sonidos hay en dos vueltas de {P(TT, TA, SIL, TA)}.", str(2 * sounds(TT, TA, SIL, TA)), "Una vuelta tiene 2 + 1 + 0 + 1 = 4 sonidos; dos vueltas, 8."),
    ],
    [
        ex(f"Vuelta 1: {P(TA, TT, SIL, TA)}. Vuelta 2: {P(TA, TT, SIL, TA)}. Vuelta 3: {P(TA, TT, TA, TA)}. ¿En qué vuelta y en qué pulso cambió el patrón?", "En la vuelta 3, en el pulso 3", "Las vueltas 1 y 2 tienen SIL en el pulso 3; la vuelta 3 tiene TA."),
        ex(f"Ana toca {P(TT, TA, TT, SIL)} y Beto toca {P(TA, TT, TT, SIL)}. Los dos tienen 4 pulsos. ¿Tienen la misma cantidad de sonidos?", f"Sí: Ana {sounds(TT, TA, TT, SIL)} y Beto {sounds(TA, TT, TT, SIL)}", "Ambos suman 2 + 1 + 2 = 5 sonidos aunque el orden sea distinto."),
    ],
    [
        ex("Un patrón de 4 pulsos tiene 3 sonidos y se repite hasta que suenan 12 sonidos en total. ¿Cuántas vueltas se tocaron?", "4", "Cada vuelta tiene 3 sonidos; 12 sonidos son 4 vueltas de 3."),
        ex(f"Inventa una variación de {P(*PAT)} que cambie un solo símbolo. Escríbela.", f"Por ejemplo: {P(TA, TT, TA, TA)}", "Basta cambiar un símbolo, por ejemplo el último SIL por TA, y dejar los otros tres."),
    ],
    [arith("En una canción, la caja toca el mismo patrón de 4 pulsos durante 6 vueltas. ¿Cuántos pulsos toca en total?", "4*6", "Se repiten 4 pulsos en cada una de las 6 vueltas.", " pulsos")],
    [ex(f"¿Cuántos sonidos tiene una vuelta de {P(*PAT)}?", str(sounds(*PAT)), "Suena 1 + 2 + 1 y el silencio no suena."), ex("Si cambia un símbolo del patrón, ¿sigue siendo exactamente igual?", "No, ahora es una variación", "Un patrón es igual solo si todos los símbolos coinciden."), ex("¿Qué cuentas para saber cuántas veces sonó un patrón?", "Las vueltas", "Cada vez que suena completo es una vuelta.")],
    (
        f"Toca con las palmas el patrón {P(*PAT)} tres veces seguidas. En la cuarta vuelta cambia un solo símbolo a tu elección (por ejemplo, el último SIL por TA). Escribe tus 4 vueltas con los símbolos, di en qué pulso cambió y cuántos pulsos tocaste.",
        f"Vueltas 1 a 3: {P(*PAT)}. Vuelta 4: {P(TA, TT, TA, TA)}. Cambió el pulso 4. Toqué 16 pulsos.",
        ["toca tres vueltas iguales", "cambia exactamente un símbolo en la cuarta", "escribe las cuatro vueltas y el pulso del cambio"],
        ["interpretación con palmas", "patrón escrito", "explicación del cambio"],
        ["cambiar dos símbolos y creer que cambió uno", "perder el pulso cuando llega el silencio"],
        "Reconoce el pulso estable; pide que compare su vuelta 3 y su vuelta 4 en voz alta, símbolo por símbolo.",
    ),
    "Toca el patrón dos veces y pide a alguien que cuente en voz alta las vueltas que escuchó.",
    "Cambia dos símbolos y explica cuántos pulsos quedaron iguales y cuántos distintos.",
)

# ---------------------------------------------------------------- OA 01 · clase 4
L(
    OA1, 4,
    "Lápiz, papel y colores. Letras para anotar: A = una sección, B = una sección distinta. Las músicas están descritas por escrito; un adulto puede interpretarlas con la voz y las palmas.",
    "Aprenderé a reconocer las secciones de una música, a anotarlas con letras y a dibujarlas. Sirve para entender cómo está armada una pieza.",
    ["Sé distinguir lento de rápido y fuerte de suave.", "Sé contar pulsos."],
    [
        "Una música se arma con partes llamadas secciones. Si una sección vuelve a sonar igual, hay repetición. Si llega una sección diferente, hay contraste. Para anotarlas usamos letras: A es la primera sección y B es una sección distinta de A.",
        "Un orden muy común es A – B – A: suena A, aparece B con otro carácter y luego regresa A. También existen A – B, A – A – B o A – B – A – B. Cuando una letra vuelve, la sección es la misma que antes.",
        "Para encontrar las secciones, busca un cambio claro: más rápido o más lento, más fuerte o más suave, otro instrumento o una altura distinta. Cuando oigas un cambio, escribe una letra nueva; cuando regrese algo conocido, repite la letra. Puedes dibujar cada sección con un color.",
    ],
    [("sección", "parte de una música"), ("repetición", "una parte que vuelve a sonar igual"), ("contraste", "una parte distinta de la anterior"), ("A y B", "letras para anotar secciones distintas"), ("forma", "el orden de las secciones, como A – B – A")],
    [
        ("Anotar la forma", "Suena primero una parte lenta y suave. Luego una parte rápida y fuerte. Al final regresa la parte lenta y suave. ¿Cuál es la forma?", ["La parte lenta y suave es A.", "La parte rápida y fuerte es distinta, así que es B.", "Al final regresa la parte A."], "A – B – A"),
        ("Contar pulsos de la forma", "En una pieza, cada sección dura 8 pulsos. La forma es A – B – A. ¿Cuántos pulsos dura en total?", ["Hay tres secciones.", "Cada una dura 8 pulsos: 8 + 8 + 8 = 24."], "24 pulsos"),
    ],
    [
        ("Poner una letra nueva cada vez que cambia la música.", "Se olvida que una sección conocida que regresa lleva su misma letra.", "Si lo que suena ya apareció, repite esa letra."),
        ("Pensar que A siempre es más lenta.", "Las letras solo nombran partes; no dicen cómo suenan.", "A es la primera sección, sea como sea."),
    ],
    [
        ex("Una canción tiene estrofa, estribillo, estrofa y estribillo. Si la estrofa es A y el estribillo es B, ¿qué forma tiene?", "A – B – A – B", "Se anotan las secciones en el orden en que suenan."),
        ex("¿Qué letra se usa para una sección distinta de A?", "B", "La segunda sección distinta recibe la letra B."),
        ex("En A – B – A, ¿cuántas veces suena la sección A?", "2", "A está al principio y vuelve al final."),
    ],
    [
        ex("Una pieza suena así: parte suave, parte suave igual, parte fuerte. ¿Qué forma tiene?", "A – A – B", "Las dos primeras son iguales y la tercera es distinta."),
        ex("En A – B – A – B – A, ¿cuántas secciones hay en total?", "5", "Se cuentan todas las letras: A, B, A, B, A."),
        ex("Pintas la sección A de azul y la B de rojo. Para A – B – A, ¿qué colores usas, en orden?", "Azul, rojo, azul", "Cada letra lleva siempre su color."),
    ],
    [
        ex("Una música tiene cuatro secciones: la primera y la tercera son iguales; la segunda y la cuarta son iguales entre sí, pero distintas de la primera. Escribe su forma.", "A – B – A – B", "Las secciones iguales llevan la misma letra, y las distintas, otra."),
        ex("Una pieza tiene la forma A – A – B – A. ¿Cuántas veces suena la sección A?", "3", "A aparece en el primer, el segundo y el cuarto lugar."),
        ex("Quieres una forma de tres secciones donde las dos de los lados son iguales entre sí y la del medio es distinta. ¿Qué letras usas?", "A – B – A", "Los lados repiten la misma letra y el medio lleva otra."),
    ],
    [
        ex("Luisa dice: «A – B – A tiene tres partes distintas». ¿Qué corrige?", "Tiene tres secciones, pero solo dos son distintas: A y B", "A regresa, y lo que regresa no es una sección nueva."),
        ex("Una pieza tiene la forma A – B. Cada sección dura 6 pulsos. Si se agrega una A al final, ¿cuántos pulsos más dura?", "6", "La nueva A vuelve a durar lo mismo que la primera A: 6 pulsos."),
    ],
    [
        arith("La sección A dura 8 pulsos y la sección B dura 4 pulsos. En la forma A – B – A – B, ¿cuántos pulsos dura la pieza?", "8+4+8+4", "Se suman las duraciones en el orden en que suenan.", " pulsos"),
        ex("Una pieza de 24 pulsos tiene tres secciones del mismo largo. ¿Cuántos pulsos dura cada una?", "8", "24 pulsos repartidos en 3 secciones iguales dan 8 pulsos cada una."),
    ],
    [ex("Observa este dibujo de una pieza: sol grande, luna pequeña, sol grande. El sol representa A. ¿Qué forma muestra?", "A – B – A", "El sol vuelve y la luna es la parte distinta.")],
    [ex("¿Qué es una sección?", "Una parte de una música", "Las músicas se arman con partes que llamamos secciones."), ex("Si la letra A vuelve a aparecer, ¿la sección es nueva o la misma?", "La misma", "Una letra repetida indica una sección que regresó."), ex("¿Cómo anotas con color una sección?", "Con el mismo color para la misma letra", "Cada letra lleva siempre un mismo color para reconocerla.")],
    (
        "Esta pieza está descrita así: primero suenan 8 pulsos lentos y suaves (palmas suaves), luego 8 pulsos rápidos y fuertes (palmas fuertes) y al final vuelven los 8 pulsos lentos y suaves. Interprétala con las palmas, escribe su forma con letras y dibújala con dos colores. Anota cuántos pulsos dura en total.",
        "La forma es A – B – A. Pinté A de azul y B de rojo. Dura 24 pulsos (8 + 8 + 8).",
        ["interpreta los tres bloques en orden", "escribe la forma A – B – A", "usa un color por sección y anota 24 pulsos"],
        ["interpretación", "dibujo con colores", "forma y total escritos"],
        ["poner una C al final porque «suena distinto» (es la A que regresa)", "no mantener el pulso al cambiar a la sección B"],
        "Reconoce la forma correcta y pregunta qué cambio audible le avisó de la sección B; si duda, pídele repetir la sección A y comparar.",
    ),
    "Inventa con tus palmas una forma A – B – A y pide a alguien de tu casa que diga cuándo cambió la música.",
    "Crea una forma A – B – A – B y calcula cuántos pulsos dura si cada sección dura 4 pulsos.",
)

# ---------------------------------------------------------------- OA 02 · clase 1
L(
    OA2, 1,
    "Lápiz y papel. Las músicas están descritas por escrito con sus rasgos audibles; un adulto puede interpretarlas con la voz o las palmas.",
    "Aprenderé a decir qué me hace sentir o imaginar una música y a justificarlo con algo que realmente se oye. Sirve para hablar de la música sin decir solo «me gustó».",
    ["Sé decir si algo es rápido o lento.", "Sé decir si algo es fuerte o suave.", "Sé nombrar emociones como alegría, calma o susto."],
    [
        "Una música puede hacerte sentir calma, alegría o susto, o hacerte imaginar un lugar. Eso es una impresión. Una impresión es personal, pero para compartirla bien hay que añadir una evidencia: algo que se oye en la música y que explica lo que sentiste.",
        "Una buena frase tiene dos partes: «Me parece ... porque ...». Por ejemplo, «Me parece tranquila porque va lenta y suave». La parte «porque» nombra un rasgo audible: rápido o lento, fuerte o suave, agudo o grave, largo o corto, qué instrumento suena.",
        "Frases como «me gustó» o «es linda» dicen cómo te sentiste, pero no dicen qué oíste. Nadie puede comprobarlas. En cambio, «suena rápida y con sonidos cortos» se puede verificar escuchando otra vez.",
    ],
    [("impresión", "lo que siento o imagino al escuchar"), ("evidencia", "un rasgo que realmente se oye"), ("rasgo audible", "algo que se puede oír, como lento, fuerte o agudo"), ("emoción", "lo que siento, como calma o alegría"), ("porque", "palabra que une mi impresión con la evidencia")],
    [
        ("Armar la frase completa", "Escuchas una música muy lenta, suave y con sonidos largos. Te parece tranquila. Escribe la frase con evidencia.", ["La impresión es: tranquila.", "Los rasgos audibles son: lenta, suave y de sonidos largos.", "Se unen con la palabra «porque»."], "Me parece tranquila porque va lenta y suave"),
        ("Distinguir evidencia", "Dos niños escuchan lo mismo. Pía dice: «es linda». Nico dice: «es linda porque los sonidos son agudos y suaves». ¿Quién dio evidencia?", ["Pía solo dijo que le gustó.", "Nico nombró dos rasgos que se pueden oír: agudos y suaves."], "Nico"),
    ],
    [
        ("Decir solo «me gustó» o «es linda».", "No se sabe qué se oyó.", "Agrega «porque» y nombra un rasgo audible."),
        ("Poner como evidencia algo que no se oye, como «porque la hizo mi abuela».", "Eso es una historia, no un rasgo del sonido.", "Elige algo que puedas volver a oír: rápido, fuerte, agudo..."),
    ],
    [
        ex("Una música va muy rápida y con golpes fuertes. ¿Cuál es un rasgo audible: «rápida» o «me da vergüenza»?", "Rápida", "Rápida se puede oír; la vergüenza es lo que siente una persona."),
        ex("Completa: «Me parece alegre porque suena ____». Elige: rápida y con sonidos agudos / sin ningún sonido.", "Rápida y con sonidos agudos", "Son rasgos que se oyen y que combinan con la alegría."),
        ex("¿Qué palabra une tu impresión con la evidencia: «me gustó» o «porque»?", "Porque", "«Porque» introduce la razón audible."),
    ],
    [
        ex("¿Cuál frase da una evidencia? (a) «Es bonita.» (b) «Suena grave y lenta.»", "b", "Grave y lenta se pueden oír y comprobar; bonita no."),
        ex("Una música tiene sonidos cortos, agudos y rápidos. Escribe una frase «Me parece ... porque ...» con la impresión «juguetona».", "Me parece juguetona porque suena rápida y con sonidos cortos y agudos", "Se une la impresión con rasgos que se oyen."),
        ex("Une cada impresión con la evidencia que más combina. Impresiones: calma y susto. Evidencias: sonidos fuertes y bruscos; sonidos suaves y largos.", "Calma con sonidos suaves y largos; susto con sonidos fuertes y bruscos", "Lo suave y largo da calma; lo fuerte y brusco sobresalta."),
    ],
    [
        ex("Una música es rápida, fuerte y de sonidos agudos. Elige la impresión que mejor combina con esos rasgos: «dormir» o «correr en una fiesta».", "Correr en una fiesta", "Rápida, fuerte y aguda da energía; dormir pide calma."),
        ex("Lee la frase: «Me parece misteriosa porque suena lenta, grave y suave». ¿Cuántos rasgos audibles nombra?", "3", "Los rasgos son lenta, grave y suave."),
        ex("En la frase «Me parece alegre porque suena rápida», escribe solo la evidencia.", "Suena rápida", "Lo que va después de «porque» es la evidencia."),
    ],
    [
        ex("Ema dice: «es triste porque yo estaba triste hoy». ¿Qué le falta a su frase?", "Un rasgo audible de la música", "Lo que explica la música es lo que se oye en ella, no el día de Ema."),
        ex("Dos personas escuchan una música lenta y suave. Una siente calma y la otra sueño. ¿Pueden tener razón las dos?", "Sí, si ambas nombran rasgos audibles de esa música", "Las impresiones pueden variar mientras se apoyen en lo que se oye."),
    ],
    [
        ex("Una música tiene tres rasgos: lenta, grave y fuerte. Escribe una frase con una impresión y dos de esos rasgos como evidencia.", "Por ejemplo: «Me parece pesada porque suena lenta y grave»", "La frase usa «porque» y dos rasgos de los tres escritos."),
        ex("Se cambian los rasgos de la misma música: ahora es rápida, aguda y suave. ¿Cambia la impresión posible? Explica con un rasgo.", "Sí; por ejemplo, ahora parece ligera porque es rápida y aguda", "Al cambiar los rasgos audibles también puede cambiar lo que se siente."),
    ],
    [ex("En una película, la música se hace de pronto lenta y grave cuando aparece el villano. Di qué impresión da y con qué evidencia.", "Da misterio o miedo porque suena lenta y grave", "Lo lento y grave suele sentirse oscuro, y se apoya en rasgos que se oyen.")],
    [ex("¿Qué es una evidencia en música?", "Un rasgo que se oye", "La evidencia es algo que puedo volver a escuchar."), ex("¿Basta decir «me gustó»?", "No, hay que decir qué se oyó", "Falta una razón audible."), ex("Nombra dos rasgos audibles.", "Por ejemplo: rápido y fuerte", "Rápido, lento, fuerte, suave, agudo o grave se pueden oír.")],
    (
        "Canta con tu familia, en voz baja, una canción corta que ya conozcas. Si prefieres, usa esta descripción: una música lenta, suave y con sonidos largos. Escribe o di una frase «Me parece ... porque ...» con tu impresión y al menos dos rasgos audibles.",
        "Me parece tranquila porque va lenta y suave, y los sonidos son largos.",
        ["nombra una impresión", "usa «porque»", "da al menos dos rasgos audibles"],
        ["frase oral o escrita", "dibujo opcional"],
        ["decir solo «me gustó»", "dar como evidencia un recuerdo"],
        "Reconoce la impresión y pregunta «¿qué oíste que te hizo sentir eso?»; si la respuesta es vaga, pide un rasgo de la lista.",
    ),
    "Di en voz alta tres frases «Me parece ... porque ...» sobre tres sonidos de tu casa.",
    "Cambia la evidencia de una frase por su contraria y di cómo cambia la impresión.",
)

# ---------------------------------------------------------------- OA 02 · clase 2
L(
    OA2, 2,
    "Un espacio libre de muebles y objetos, calcetines o zapatos que no resbalen, y papel. Las músicas están descritas por escrito; un adulto puede marcar el pulso con las palmas. Movimientos sin empujar ni saltos altos.",
    "Aprenderé a responder a la música con el cuerpo: elegir un movimiento que combine con lo que oigo. Sirve para expresar ideas sin usar palabras.",
    ["Sé caminar al pulso.", "Sé distinguir lento de rápido y fuerte de suave."],
    [
        "El cuerpo puede decir lo que sientes de una música. Para que el movimiento responda a lo que suena, haz coincidir el movimiento con un rasgo audible. Si la música es lenta, mueve el cuerpo lento. Si es suave, haz movimientos pequeños. Si es fuerte, movimientos grandes.",
        "Los sonidos largos piden movimientos que se estiran o se deslizan, como mover un brazo despacio. Los sonidos cortos piden movimientos breves, como golpecitos o saltitos pequeños. Los sonidos agudos pueden hacerse arriba, en puntillas; los graves, abajo, con los pies firmes.",
        "Un movimiento que responde cambia cuando la música cambia. Si la sección A es lenta y la sección B es rápida, tu movimiento también cambia en B. Cuenta los pulsos para saber cuándo cambiar.",
    ],
    [("movimiento", "lo que hago con mi cuerpo para responder a la música"), ("lento", "poco a poco, con calma"), ("pequeño", "movimiento que ocupa poco espacio"), ("deslizar", "mover el cuerpo sin cortar el movimiento"), ("cambio", "cuando la música o el movimiento pasan a otra cosa")],
    [
        ("Elegir un movimiento", "Una música es lenta, suave y de sonidos largos. ¿Qué movimiento combina: golpecitos rápidos o balancear un brazo despacio?", ["Lenta pide movimiento lento.", "Sonidos largos piden movimientos que se estiran.", "Balancear despacio cumple las dos cosas."], "Balancear un brazo despacio"),
        ("Contar el cambio", "Una música tiene 4 pulsos de sección A y 4 pulsos de sección B. Das un paso por pulso y cambias de movimiento en B. ¿En qué paso empieza el cambio?", ["A ocupa los pulsos 1, 2, 3 y 4.", "B empieza en el pulso siguiente."], "En el paso 5"),
    ],
    [
        ("Moverse siempre igual aunque cambie la música.", "El movimiento no responde a lo que suena.", "Cambia el movimiento cuando cambie un rasgo audible."),
        ("Mover el cuerpo muy fuerte para una música suave.", "El movimiento no coincide con la intensidad.", "Hazlo pequeño y suave."),
    ],
    [
        ex("La música va muy lenta. ¿Tu movimiento debe ser lento o rápido?", "Lento", "El movimiento responde a la velocidad que se oye."),
        ex("Suenan golpecitos muy cortos y suaves. ¿Haces saltitos pequeños o un estirón largo?", "Saltitos pequeños", "Sonidos cortos y suaves piden movimientos breves y pequeños."),
        ex("¿Cuándo debe cambiar tu movimiento: cuando cambia la música o cuando te aburres?", "Cuando cambia la música", "El movimiento responde a lo que se oye."),
    ],
    [
        ex("Una música es fuerte. ¿Qué tamaño de movimiento combina: grande o pequeño?", "Grande", "Un sonido fuerte se acompaña con un movimiento grande."),
        ex("Una música tiene sonidos largos y suaves. ¿Qué movimiento combina: deslizar una mano despacio o dar golpes secos con el pie?", "Deslizar una mano despacio", "Largo pide deslizar y suave pide gesto tranquilo."),
        ex("Das un paso en cada pulso y la música tiene 8 pulsos. ¿Cuántos pasos das?", "8", "Un paso por pulso: 8 pulsos son 8 pasos."),
    ],
    [
        ex("Une cada rasgo con un movimiento. Rasgos: fuerte y suave. Movimientos: manos pequeñas y brazos grandes.", "Fuerte con brazos grandes; suave con manos pequeñas", "La fuerza del sonido se refleja en el tamaño del movimiento."),
        ex("Suena un sonido agudo muy largo. ¿Qué movimiento combina: estirarte despacio hacia arriba o agacharte rápido?", "Estirarte despacio hacia arriba", "Agudo se hace arriba y largo se estira."),
        arith("Das un paso en cada pulso. La sección A dura 8 pulsos y la B dura 4. ¿Cuántos pasos das en total?", "8+4", "Un paso por pulso: 8 pasos en A y 4 pasos en B.", " pasos"),
    ],
    [
        ex("Mara se mueve igual en la sección rápida que en la lenta. ¿Qué le falta a su movimiento?", "Cambiar cuando cambia la velocidad de la música", "Un movimiento que responde cambia con lo que se oye."),
        ex("Una música es grave y fuerte. Tomás hace movimientos pequeños y en puntillas. ¿Combina? ¿Por qué?", "No; grave y fuerte piden movimientos grandes y firmes, abajo", "Lo grave se hace abajo y lo fuerte se hace grande."),
    ],
    [
        ex("La forma de la música es A – B – A: A lenta, B rápida. Escribe qué movimiento haces en cada letra.", "A: movimiento lento; B: movimiento rápido; A: lento otra vez", "El movimiento acompaña cada cambio y regresa con A."),
        ex("Quieres moverte 12 pulsos: 4 lentos, 4 rápidos y el resto de nuevo lentos. ¿Cuántos pulsos lentos al final?", "4", "12 pulsos menos los 4 lentos y los 4 rápidos dejan 4 pulsos lentos."),
    ],
    [ex("En una fiesta, la música pasa de lenta y suave a rápida y fuerte. ¿Qué cambia en el baile?", "El baile se vuelve rápido y grande", "El cuerpo sigue la velocidad y la intensidad del sonido.")],
    [ex("¿Qué haces con el cuerpo si la música es suave?", "Movimientos pequeños", "La intensidad suave se refleja en gestos pequeños."), ex("Si los sonidos son cortos, ¿haces golpecitos o estiras el brazo?", "Golpecitos", "Lo corto es breve."), ex("¿Cuándo cambias de movimiento?", "Cuando cambia un rasgo de la música", "El movimiento responde a la música.")],
    (
        "Haz esta danza de 12 pulsos en un espacio libre, marcando el pulso con palmas. Pulsos 1 a 4: movimientos lentos y grandes. Pulsos 5 a 8: golpecitos rápidos y pequeños. Pulsos 9 a 12: otra vez lentos y grandes. Cuéntala en voz baja y dibuja con tres figuras (grande, pequeña, grande) lo que hiciste.",
        "Hice 4 pulsos lentos y grandes, 4 de golpecitos pequeños y 4 lentos y grandes. Dibujé: círculo grande, círculo pequeño, círculo grande.",
        ["hace tres bloques de 4 pulsos", "cambia el movimiento exactamente en los pulsos 5 y 9", "mantiene el pulso parejo"],
        ["demostración de movimiento", "dibujo de tres figuras", "conteo en voz baja"],
        ["cambiar de movimiento en el pulso equivocado", "usar espacio con objetos o empujar a otros"],
        "Reconoce el cambio justo en el pulso 5; pregunta qué rasgo de la música eligió representar con el tamaño del movimiento.",
    ),
    "Camina por tu pieza al pulso: 8 pasos lentos, 8 pasos rápidos. Cuenta en voz alta.",
    "Inventa un movimiento para un sonido agudo y corto, y otro para uno grave y largo. Explícalos.",
)

# ---------------------------------------------------------------- OA 02 · clase 3
L(
    OA2, 3,
    "Papel, lápices de colores y regla. Código gráfico: punto ● = sonido corto; línea ━━ = sonido largo; arriba = agudo; abajo = grave; trazo grueso = fuerte; trazo fino = suave. Las músicas están descritas por escrito.",
    "Aprenderé a dibujar lo que me sugiere una música, usando líneas y colores que representen lo que oigo. Sirve para expresar una idea sin palabras y para que otros la entiendan.",
    ["Sé dibujar puntos y líneas.", "Sé que agudo es fino y grave es hondo."],
    [
        "Un dibujo puede mostrar lo que sugiere una música. Podemos usar un código: un punto es un sonido corto y una línea larga es un sonido largo. Si el sonido es agudo, se dibuja arriba; si es grave, abajo. Si es fuerte, el trazo es grueso; si es suave, el trazo es fino.",
        "Los colores pueden expresar lo que sentiste. Por ejemplo, azul para calma o rojo para energía. Pero los colores son una elección personal. Si usas un color, explica por qué lo eliges. Lo que sí se puede comprobar es el código del dibujo: puntos, líneas y posición.",
        "Un buen dibujo musical se puede «leer»: otra persona puede seguirlo con el dedo de izquierda a derecha y decir qué suena primero, qué suena después, si es largo o corto, agudo o grave.",
    ],
    [("dibujo musical", "dibujo que muestra los sonidos con puntos, líneas y colores"), ("código", "regla que dice qué significa cada símbolo"), ("de izquierda a derecha", "orden en que se lee el dibujo"), ("trazo", "línea que dibujas"), ("color expresivo", "color que elijo para mostrar lo que siento")],
    [
        ("Leer un dibujo", "Un dibujo, de izquierda a derecha, tiene: 3 puntos arriba y 1 línea larga abajo. ¿Qué suena?", ["Los puntos son sonidos cortos y arriba son agudos.", "La línea larga abajo es un sonido largo y grave."], "Tres sonidos cortos y agudos, y luego uno largo y grave"),
        ("Dibujar un sonido", "Quieres dibujar un sonido corto, fuerte y grave. ¿Cómo lo dibujas?", ["Corto: un punto.", "Fuerte: trazo grueso.", "Grave: abajo."], "Un punto grueso, abajo"),
    ],
    [
        ("Dibujar solo una historia sin mostrar lo que suena.", "Los demás no pueden saber qué oíste.", "Agrega puntos, líneas y posición según el código."),
        ("Usar el código sin decirlo.", "Quien mira no sabe qué significa cada símbolo.", "Escribe una pequeña leyenda."),
    ],
    [
        ex("En el código, ¿un punto representa un sonido largo o corto?", "Corto", "Un punto es breve, igual que un sonido corto."),
        ex("Un sonido grave, ¿se dibuja arriba o abajo?", "Abajo", "Grave es hondo, y se dibuja abajo."),
        ex("Un trazo grueso representa un sonido ¿fuerte o suave?", "Fuerte", "El trazo grueso muestra mucha intensidad."),
    ],
    [
        ex("Un sonido suave, ¿se dibuja con trazo fino o con trazo grueso?", "Trazo fino", "El trazo fino muestra poca intensidad."),
        ex("Dibujas dos puntos arriba. ¿Qué sonidos representan, en altura y duración?", "Sonidos agudos y cortos", "Los puntos son cortos y arriba es agudo."),
        ex("¿Qué cualidad del sonido muestras con la posición arriba o abajo?", "La altura", "Arriba es agudo y abajo es grave."),
    ],
    [
        ex("Un dibujo tiene 5 puntos y 2 líneas largas. ¿Cuántos sonidos cortos y cuántos largos representa?", "5 cortos y 2 largos", "Cada punto es un sonido corto y cada línea larga es uno largo."),
        arith("Otro dibujo tiene 6 puntos y 3 líneas largas. ¿Cuántos sonidos representa en total?", "6+3", "Se suma un sonido por cada punto y por cada línea.", " sonidos"),
        ex("Quieres dibujar un sonido largo, agudo y suave. ¿Cómo es tu trazo y dónde lo pones?", "Una línea larga y fina, arriba", "Largo es línea larga, suave es trazo fino y agudo es arriba."),
    ],
    [
        ex("Dos dibujos: A tiene 4 puntos finos arriba. B tiene 4 puntos gruesos abajo. ¿En qué cualidades se diferencian los sonidos?", "En la altura (arriba/abajo) y la intensidad (fino/grueso)", "Cambia la posición y el grosor, pero la duración es la misma."),
        ex("Una niña pintó una línea larga, azul y suave para una música. ¿Qué se puede comprobar con el código y qué es personal?", "Se comprueba que es larga y suave; el azul es una elección personal", "La duración y el grosor siguen el código, el color expresa lo que sintió."),
    ],
    [
        ex("Describe con palabras, de izquierda a derecha, el dibujo de esta música: dos sonidos cortos y agudos, y después uno largo y grave.", "Dos puntos arriba y una línea larga abajo", "Se dibujan en el orden en que suenan, siguiendo el código."),
        ex("Un dibujo tiene en orden: línea larga, punto, punto, línea larga. ¿Cuántos sonidos largos y cuántos cortos tiene?", "2 largos y 2 cortos", "Hay dos líneas largas y dos puntos."),
    ],
    [ex("Quieres mostrar a tu curso la música de una tormenta que empieza suave y termina fuerte. ¿Cómo cambia el grosor del trazo?", "Parte fino y termina grueso", "La intensidad pasa de suave a fuerte, y se dibuja así.")],
    [ex("¿Dónde se dibuja un sonido agudo?", "Arriba", "Agudo es fino y alto."), ex("¿Qué significa una línea larga?", "Un sonido largo", "Línea larga indica duración larga."), ex("¿Qué debes escribir para que otros entiendan tu dibujo?", "Una leyenda con el código", "La leyenda explica los símbolos.")],
    (
        "Esta música se describe así: primero tres sonidos cortos y suaves, agudos; luego un sonido largo y fuerte, grave; y por último dos sonidos cortos y suaves, agudos. Dibújala de izquierda a derecha con el código (punto = corto, línea = largo, arriba = agudo, abajo = grave, trazo fino = suave, trazo grueso = fuerte). Escribe una leyenda y elige un color para toda la obra, explicando por qué.",
        "Dibujé 3 puntos finos arriba, una línea larga y gruesa abajo, y 2 puntos finos arriba. Elegí azul porque la música me dio calma. Leyenda: punto = corto, línea = larga...",
        ["dibuja los seis sonidos en el orden pedido", "usa posición y grosor según el código", "escribe una leyenda y explica el color"],
        ["dibujo musical", "leyenda", "explicación del color"],
        ["cambiar el orden de los sonidos", "usar color sin explicar"],
        "Reconoce el dibujo legible; pide que otra persona lo «lea» con el dedo y diga lo que suena.",
    ),
    "Dibuja con puntos y líneas el sonido de tres golpes cortos y uno largo. Escribe la leyenda.",
    "Dibuja la misma música, pero cambiando solo la altura. Explica qué cambió en el dibujo.",
)

# ---------------------------------------------------------------- OA 02 · clase 4
L(
    OA2, 4,
    "Lápiz y papel. Dos niños ficticios, Sofía y Tomás, escuchan una misma música descrita por escrito: sonidos cortos, suaves, repetidos y bastante lentos. Un adulto puede interpretarla dando golpecitos suaves sobre la mesa.",
    "Aprenderé que una misma música puede sugerir ideas distintas y que todas valen si se apoyan en lo que se oye. Sirve para escuchar con respeto a mis compañeros.",
    ["Sé decir una impresión con evidencia.", "Sé escuchar a otros sin interrumpir."],
    [
        "Una misma música puede sugerir ideas distintas a distintas personas. Una escucha lluvia y otra, pasos de un gigante. Las dos pueden tener razón si cada una explica su idea con algo que realmente se oye, como «golpes cortos y suaves que se repiten».",
        "Una idea es válida cuando se apoya en un rasgo audible. Si alguien dice una idea que no tiene relación con lo que suena, o dice que otra persona «se equivoca», falta respeto o falta evidencia. En cambio, podemos preguntar: «¿Qué oíste para pensar eso?». Una idea también se puede mostrar con sonidos: para la lluvia, unos golpecitos suaves y cortos sobre la mesa.",
        "Escuchar a otros nos ayuda a notar rasgos que no habíamos notado. Para conversar con respeto: espera tu turno, di «yo escuché ... porque ...» y agradece la idea del otro. Si tu idea cambia después de escuchar, también está bien.",
    ],
    [("idea", "lo que imagino al escuchar"), ("respeto", "escuchar y valorar a los demás"), ("turno", "momento en que me toca hablar"), ("rasgo audible", "algo que realmente se oye"), ("acuerdo", "regla que todos aceptan para conversar")],
    [
        ("Dos ideas válidas", "Sofía dice: «es lluvia porque los sonidos son cortos, suaves y repetidos». Tomás dice: «son pasos de gigante porque son lentos y repetidos». ¿Pueden tener razón los dos?", ["Los dos nombran rasgos audibles: repetidos, y suaves o lentos.", "La música tiene esos rasgos, así que ambas ideas se apoyan en lo que suena."], "Sí, los dos"),
        ("Contar las ideas del curso", "En un curso de 12 estudiantes, 5 imaginaron lluvia, 4 imaginaron pasos y los demás imaginaron otra cosa. ¿Cuántos imaginaron otra cosa?", ["Se suman los que imaginaron lluvia y pasos: 5 + 4 = 9.", "Se restan de 12: 12 − 9 = 3."], "3 estudiantes"),
    ],
    [
        ("Decir «tu idea está mal» solo porque es distinta.", "Una idea puede ser diferente y estar bien apoyada.", "Pregunta «¿qué oíste para pensar eso?»."),
        ("Cambiar de idea solo para ser igual al resto.", "Tu idea puede valer aunque sea distinta.", "Si no te convence otra idea, explica la tuya."),
    ],
    [
        ex("Varios niños escuchan la misma música y cada uno imagina algo distinto. ¿Es posible?", "Sí", "Cada persona puede imaginar distinto mientras se apoye en lo que suena."),
        ex("¿Qué pregunta ayuda a entender la idea de otro: «¿qué oíste?» o «¿por qué piensas algo tan raro?»", "¿Qué oíste?", "Pregunta con curiosidad y no juzga."),
        ex("Si cuentas la idea que te sugirió una música, ¿qué debes agregar para que sea completa?", "La evidencia, lo que oíste", "Una idea completa dice qué se oyó para pensarla."),
    ],
    [
        ex("Una niña dice «es lluvia» y no explica por qué. ¿Qué le falta?", "La evidencia, lo que oyó", "Una idea necesita un rasgo audible que la apoye."),
        ex("Mateo escucha golpes fuertes y lentos y dice «es un tambor gigante». ¿Qué rasgos usó como evidencia?", "Fuertes y lentos", "Son los rasgos audibles que nombró."),
        ex("Cuando un compañero dice una idea distinta, ¿esperas tu turno o interrumpes?", "Espero mi turno", "Esperar el turno es una forma de respeto."),
    ],
    [
        ex("Una música suena fuerte, rápida y con sonidos agudos. Ana dice «es una fiesta» y Beto dice «es un susto». ¿Qué evidencia puede dar cada uno?", "Ana: es rápida y de sonidos agudos; Beto: es fuerte", "Cada idea puede apoyarse en rasgos distintos de los mismos sonidos."),
        arith("En un curso de 20 niños, 9 imaginaron mar, 6 imaginaron viento y el resto imaginó otra cosa. ¿Cuántos imaginaron otra cosa?", "20-9-6", "Se restan del total los que imaginaron mar y viento.", " niños"),
        ex("Dos amigos escuchan una música lenta y suave. ¿Qué idea se apoya en la evidencia: «es una carrera de autos» o «es un barco que se mece»?", "Un barco que se mece", "Lento y suave combina con un balanceo; una carrera es rápida."),
    ],
    [
        ex("Pía dice: «Tomás se equivoca, es lluvia, no pasos». ¿Qué podría decir con respeto?", "Yo escuché lluvia porque los golpes son cortos y suaves; ¿qué oíste tú?", "Habla de lo que oyó y pregunta a Tomás, sin decir que se equivoca."),
        ex("Quieres mostrar con sonidos tu idea de «lluvia» golpeando una mesa con los dedos. ¿Cómo tocas: golpecitos suaves y cortos o golpes fuertes y largos?", "Golpecitos suaves y cortos", "La lluvia fina se representa con sonidos suaves y cortos."),
    ],
    [
        ex("Una música es lenta, suave y grave. Escribe dos ideas distintas que se apoyen en esos rasgos.", "Por ejemplo: un oso caminando y un barco grande a lo lejos", "Ambas ideas se apoyan en rasgos que se oyen: lento, suave y grave."),
        ex("Si cambias la misma música a rápida y aguda, ¿tu idea puede seguir siendo la misma? ¿Por qué?", "Probablemente no, porque cambian los rasgos que la apoyaban", "La idea nacía de rasgos audibles; si estos cambian, la idea también."),
    ],
    [ex("En una clase, la profesora hace sonar golpes lentos y suaves. Un niño dice «sueño» y otra niña dice «un bosque en calma». ¿Cómo valoran las dos ideas?", "Las dos son válidas si cada una explica con lo que oyó", "Dos ideas distintas pueden vivir juntas con evidencia.")],
    [ex("¿Pueden dos personas imaginar cosas distintas con la misma música?", "Sí", "Cada persona oye y siente a su modo."), ex("¿Qué hace válida una idea?", "Que se apoye en un rasgo audible", "La evidencia es lo que se oye."), ex("Menciona una frase respetuosa para conversar.", "Yo escuché ... porque ...", "Es una frase que comparte sin juzgar.")],
    (
        "Escucha esta música (un adulto da golpecitos suaves y lentos, repetidos, sobre una mesa durante 8 pulsos). Escribe tu idea con «Yo escuché ... porque ...» y completa: «Otra persona pudo imaginar ... porque ...». Comparte con alguien de tu casa y pídele que diga su idea con evidencia.",
        "Yo escuché pasos de un gigante porque los golpes eran lentos, suaves y repetidos. Otra persona pudo imaginar lluvia porque los golpes eran suaves y repetidos.",
        ["escribe su idea con evidencia audible", "propone otra idea posible con evidencia", "escucha la idea del otro sin decir que está mal"],
        ["frase escrita u oral", "conversación con respeto"],
        ["decir que una idea distinta es incorrecta", "no dar evidencia audible"],
        "Reconoce la idea con evidencia; si hay desacuerdo, modela la pregunta «¿qué oíste?» y pide repetir la audición.",
    ),
    "Cuenta a alguien de tu familia una idea que te sugirió un sonido de tu casa y qué oíste para pensarla.",
    "Escribe tres reglas de respeto para conversar sobre lo que escuchamos.",
)
