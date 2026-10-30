"""Student material for 4.º básico Música, OA 01 (cualidades del sonido y lenguaje musical) y OA 02 (respuestas elaboradas a la música escuchada)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1, OA2 = "MU04 OA 01", "MU04 OA 02"

TA, TT, TIRI, TAA, SIL = "TA", "ti-ti", "tiri-tiri", "TAA", "SIL"
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


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- OA 01 · clase 1
EV = [(0, 2, "flauta", "aguda", "suave"), (2, 3, "tambor", "grave", "fuerte"), (3, 7, "violonchelo", "grave", "suave"),
      (7, 8, "triángulo", "aguda", "fuerte"), (8, 12, "flauta", "aguda", "fuerte")]
EV_TXT = " ".join(f"Evento {i}: del segundo {a} al {b}, {ins}, altura {alt}, intensidad {inten}." for i, (a, b, ins, alt, inten) in enumerate(EV, 1))
EV_COD = "o = suave, O = fuerte; cada ━ = 1 segundo de duración"

L(
    OA1, 1,
    f"Lápiz y papel. La escucha está descrita por escrito en una línea de tiempo, así que no necesitas audio. Para practicar puedes usar tus palmas, una caja o una olla con una cuchara de madera, a volumen bajo. Código de dibujo: {EV_COD}.",
    "Aprenderé a localizar en una escucha las cuatro cualidades del sonido (altura, timbre, intensidad y duración), diciendo en qué momento ocurre cada una. Sirve para describir con precisión lo que se oyó.",
    ["Sé que un sonido puede ser agudo o grave.", "Sé que un sonido puede ser fuerte o suave.", "Sé qué es un pulso."],
    [
        "Escuchar con atención es poder decir qué cualidad oíste y en qué momento. Para eso se usa una línea de tiempo: una lista de eventos sonoros en el orden en que suenan, con el segundo en que empiezan y terminan. La altura dice si el sonido es agudo (fino) o grave (hondo). La intensidad dice si suena fuerte o suave. El timbre dice qué lo produce. La duración dice cuántos segundos o pulsos suena.",
        f"Cada cualidad responde a su propia pregunta y son independientes. Un triángulo suena agudo y puede sonar fuerte o suave. Un tambor suena grave y también puede sonar fuerte o suave. Por eso agudo no significa fuerte, ni grave significa suave. Para dibujar un evento puedes usar este código: {EV_COD}.",
        "Cuando escuchas no atiendas todo a la vez. En la primera escucha anota solo la altura. En la segunda anota la intensidad. En la tercera mide la duración con los segundos de inicio y término. Así cada dato queda ligado a un momento de la escucha y puedes volver a revisarlo.",
    ],
    [("altura", "qué tan agudo o grave es un sonido"), ("timbre", "el «color» del sonido; dice qué lo produce"), ("intensidad", "qué tan fuerte o suave suena"), ("duración", "cuánto tiempo suena"), ("línea de tiempo", "lista de eventos sonoros en el orden en que suenan")],
    [
        ("Localizar por el segundo", f"{EV_TXT} ¿Qué instrumento suena en el segundo 9?", ["El segundo 9 está entre el 8 y el 12.", "Ese tramo es el evento 5.", "El evento 5 es la flauta."], "La flauta"),
        ("Separar altura de intensidad", f"{EV_TXT} Un niño dice: «el evento 2 es grave, entonces suena suave». ¿Tiene razón?", ["Grave habla de la altura; suave habla de la intensidad.", "El evento 2 es grave y de intensidad fuerte."], "No: es grave pero fuerte; son cualidades distintas"),
    ],
    [
        ("Decir que un sonido es largo porque suena fuerte.", "Se confunden duración e intensidad.", "Mide la duración con los segundos de inicio y término, no con la fuerza."),
        ("Creer que dos sonidos graves suenan iguales.", "Pueden diferir en timbre, intensidad y duración.", "Compara las cuatro cualidades, una por una."),
    ],
    [
        ex(f"{EV_TXT} ¿Qué instrumento suena en el evento 3?", "El violonchelo", "La línea de tiempo anota el violonchelo en el evento 3."),
        ex(f"{EV_TXT} ¿Cuál es la intensidad del evento 4?", "Fuerte", "El evento 4 dice intensidad fuerte."),
        ex("Un trueno lejano se oye hondo. ¿Su altura es aguda o grave?", "Grave", "Un sonido hondo es grave."),
    ],
    [
        ex(f"{EV_TXT} Escribe los números de los eventos con altura aguda.", "1, 4 y 5", "La flauta (1 y 5) y el triángulo (4) son agudos."),
        ex(f"{EV_TXT} ¿Cuántos eventos tienen intensidad fuerte?", "3", "Son fuertes el evento 2, el 4 y el 5."),
        ex(f"{EV_TXT} ¿Cuántos eventos duran exactamente 4 segundos?", "2", "Duran 4 segundos el evento 3 (de 3 a 7) y el 5 (de 8 a 12)."),
    ],
    [
        arith(f"{EV_TXT} ¿Cuántos segundos suena la flauta en total, sumando sus dos eventos?", "(2-0)+(12-8)", "Se suma la duración del evento 1 y la del evento 5.", " segundos"),
        ex(f"{EV_TXT} ¿Qué instrumento suena en el segundo 5?", "El violonchelo", "El segundo 5 está entre el 3 y el 7, que es el evento 3."),
        ex(f"{EV_TXT} ¿Qué número tiene el único evento grave y fuerte a la vez?", "2", "El tambor es grave y fuerte; el violonchelo es grave pero suave."),
    ],
    [
        ex(f"{EV_TXT} Ana dice que el evento 5 es más agudo que el evento 1 porque suena más fuerte. ¿Qué cualidades está confundiendo?", "Altura con intensidad", "Los dos eventos son flauta aguda; solo cambia la intensidad."),
        ex(f"{EV_TXT} La misma flauta suena en los eventos 1 y 5 con la misma altura. ¿Qué dos cualidades cambian entre ambos?", "Intensidad y duración", "Pasa de suave a fuerte y de 2 a 4 segundos."),
    ],
    [
        arith(f"{EV_TXT} ¿Cuántos segundos suenan en total los eventos graves (2 y 3)?", "(3-2)+(7-3)", "Se suman las duraciones de los dos eventos graves.", " segundos"),
        arith(f"{EV_TXT} Si el evento 4 durara 3 segundos desde el segundo 7, ¿en qué segundo terminaría?", "7+3", "Se suma la duración al segundo de inicio.", ""),
    ],
    [ex("En el recreo suena una campana aguda y fuerte durante 3 segundos. Después rebota un balón con un sonido grave y suave durante 5 segundos. ¿Cuál de los dos sonidos dura más y por cuántos segundos?", "El balón, por 2 segundos", "5 segundos menos 3 segundos son 2 segundos más para el balón.")],
    [ex("¿Qué cualidad del sonido dice qué objeto lo produce?", "El timbre", "El timbre es el «color» que distingue una flauta de un tambor."), ex("¿Qué cualidad mide cuánto tiempo suena un sonido?", "La duración", "La duración se mide en segundos o pulsos."), ex("Un susurro y un grito de la misma persona, ¿cambian en altura o en intensidad?", "En intensidad", "Se pasa de suave a fuerte.")],
    (
        f"Haz tu propia línea de tiempo de 3 eventos con objetos seguros de tu casa, por ejemplo golpear una olla con una cuchara de madera, golpear la mesa con la palma o frotar dos hojas de papel. Para cada evento anota el segundo de inicio y de término (puedes contar «mil uno, mil dos…»), el objeto, la altura y la intensidad. Dibuja los tres con el código ({EV_COD}).",
        "Evento 1: del 0 al 2, olla con cuchara, grave, fuerte (O ━━). Evento 2: del 2 al 3, palma en la mesa, grave, suave (o ━). Evento 3: del 3 al 6, papel frotado, agudo, suave (o ━━━).",
        ["anota los tres eventos en orden con inicio y término", "nombra altura e intensidad de cada uno", "dibuja cada evento con el código"],
        ["línea de tiempo escrita", "dibujo con código", "sonidos producidos"],
        ["decir «fuerte» para un sonido agudo sin comprobar", "dibujar una duración distinta de la que anotó"],
        "Reconoce la línea de tiempo clara; si mezcla altura e intensidad, pide volver a escuchar el evento y responder una pregunta por vez.",
    ),
    "Elige dos objetos seguros de tu casa, golpéalos con suavidad y di de cada uno si suena agudo o grave.",
    "Haz una línea de tiempo de cuatro sonidos y pide a una persona de tu casa que los toque sin mirar tus dibujos.",
)

# ---------------------------------------------------------------- OA 01 · clase 2
Q1 = (TA, TT, TIRI, TAA)
Q2 = (TT, TA, SIL, TAA, TA)
Q3 = (TIRI, TIRI, TA, SIL)
Q4 = (TAA, TA, TT, TT)

L(
    OA1, 2,
    f"Lápiz, tus palmas y tus pasos. Leyenda de ritmo: {LEY}. Todos los patrones están escritos en los ejercicios.",
    "Aprenderé a distinguir pulso, acento y patrón, y a calcular cuántos pulsos y cuántos sonidos tiene un patrón. Sirve para tocar con otras personas sin perderse.",
    ["Sé caminar con paso parejo.", "Sé que TA dura un pulso y que ti-ti son dos sonidos rápidos.", "Sé sumar números pequeños."],
    [
        "El pulso es el latido parejo de la música, como tus pasos al caminar. El acento es el pulso que se marca más fuerte y va al comienzo de cada grupo de pulsos. Si cuentas de a 3 dices 1-2-3, 1-2-3, y el acento cae en cada 1. También se puede contar de a 2 y de a 4.",
        f"El patrón es una secuencia de sonidos y silencios que se repite sobre el pulso. Esta vez sumamos tiri-tiri, que son cuatro sonidos muy rápidos dentro de un solo pulso. Leyenda: {LEY}. Para contar pulsos sumamos lo que ocupa cada símbolo. Para contar sonidos sumamos lo que suena. El silencio ocupa un pulso, pero no suena.",
        f"Un ejemplo: {P(*Q1)}. Los pulsos son 1 + 1 + 1 + 2 = {pulses(*Q1)}. Los sonidos son 1 + 2 + 4 + 1 = {sounds(*Q1)}. Ojo: tiri-tiri tiene cuatro sonidos pero ocupa un solo pulso, y TAA tiene un sonido pero ocupa dos pulsos. El pulso se mantiene parejo mientras el patrón cambia.",
    ],
    [("pulso", "latido parejo de la música"), ("acento", "pulso que se marca más fuerte, al inicio de cada grupo"), ("patrón", "secuencia de sonidos y silencios que se repite"), ("tiri-tiri", "cuatro sonidos muy rápidos en un pulso"), ("grupo de pulsos", "pulsos que se cuentan juntos, de a 2, 3 o 4")],
    [
        ("Contar pulsos y sonidos", f"¿Cuántos pulsos y cuántos sonidos tiene {P(*Q2)}?", ["Pulsos: ti-ti 1, TA 1, SIL 1, TAA 2, TA 1.", "1 + 1 + 1 + 2 + 1 = 6 pulsos.", "Sonidos: 2 + 1 + 0 + 1 + 1 = 5 sonidos."], f"{pulses(*Q2)} pulsos y {sounds(*Q2)} sonidos"),
        ("Ubicar los acentos", "Cuento 12 pulsos en grupos de 3, con acento en el primero de cada grupo. ¿En qué números caen los acentos?", ["Los grupos son 1-2-3, 4-5-6, 7-8-9 y 10-11-12.", "El acento va al inicio de cada grupo."], "En los pulsos 1, 4, 7 y 10"),
    ],
    [
        ("Decir que tiri-tiri ocupa cuatro pulsos.", "Se cuentan los sonidos y no los latidos.", "tiri-tiri son cuatro sonidos dentro de un solo pulso."),
        ("Contar TAA como un pulso porque es un solo sonido.", "Se confunden sonidos con pulsos.", "TAA es un sonido que dura 2 pulsos; el segundo pulso sigue sonando."),
    ],
    [
        ex("¿Cuántos pulsos ocupa un TAA?", "2", "Según la leyenda, TAA es un sonido largo que dura 2 pulsos."),
        ex("Cuentas de a 4: 1-2-3-4, 1-2-3-4. Si el acento va en el 1, ¿qué números se dicen suaves?", "2, 3 y 4", "Solo el 1 lleva acento; los otros pulsos van suaves."),
        ex(f"¿Cuántos pulsos tiene el patrón {P(TA, TA, SIL)}?", str(pulses(TA, TA, SIL)), "Cada símbolo ocupa un pulso y el silencio también cuenta."),
    ],
    [
        ex(f"Cuenta los pulsos de este patrón: {P(*Q3)}.", str(pulses(*Q3)), "Cada símbolo ocupa un pulso: 1 + 1 + 1 + 1."),
        ex(f"Cuenta los sonidos de este otro patrón: {P(*Q3)}.", str(sounds(*Q3)), "Suenan 4 + 4 + 1 y el silencio no suena."),
        ex("Cuentas de a 3: 1-2-3, 1-2-3, 1-2-3, con acento en cada 1. ¿Cuántos acentos hay?", "3", "Hay tres grupos y cada grupo tiene un acento."),
    ],
    [
        ex("Escribe los números donde caen los acentos si cuentas 12 pulsos en grupos de 4.", "1, 5 y 9", "Cada grupo parte cuatro números después del anterior."),
        arith("Un patrón de 6 pulsos tiene 1 silencio. ¿Cuántos pulsos suenan?", "6-1", "A los 6 pulsos se les quita el pulso en silencio.", " pulsos"),
        arith("Cuentas 16 pulsos en grupos de 4, con un acento por grupo. ¿Cuántos acentos das?", "16//4", "Cada grupo de 4 pulsos tiene un acento.", " acentos"),
    ],
    [
        ex(f"Luis dice que {P(*Q4)} tiene 4 pulsos porque son 4 símbolos. ¿Cuántos pulsos tiene realmente?", str(pulses(*Q4)), "TAA ocupa 2 y los otros tres ocupan 1 cada uno: 2 + 1 + 1 + 1."),
        ex(f"En {P(*Q4)}, ¿cuántos sonidos hay?", str(sounds(*Q4)), "TAA suena 1, TA suena 1 y cada ti-ti suena 2."),
    ],
    [
        arith(f"El patrón {P(*Q1)} se repite 3 veces. ¿Cuántos sonidos se tocan en total?", f"{sounds(*Q1)}*3", "Cada vuelta tiene 8 sonidos y hay 3 vueltas.", " sonidos"),
        arith(f"Tocas {P(*Q2)} y enseguida {P(*Q1)}. ¿Cuántos pulsos hay entre los dos patrones?", f"{pulses(*Q2)}+{pulses(*Q1)}", "Se suman los pulsos de ambos patrones.", " pulsos"),
    ],
    [ex("En una marcha se cuentan 4 pulsos por grupo y se pisa más fuerte en el primero. Una niña camina 3 grupos completos. ¿Cuántos pasos fuertes y cuántos pasos suaves da?", "3 fuertes y 9 suaves", "Cada grupo tiene 1 pulso fuerte y 3 suaves; en 3 grupos son 3 y 9.")],
    [ex(f"¿Cuántos pulsos tiene {P(SIL, TA, SIL, TA)}?", "4", "Los silencios también ocupan un pulso."), ex(f"¿Cuántos sonidos tiene {P(TA, TA, SIL, SIL)}?", "2", "Solo suenan los dos TA."), ex("¿Qué es un patrón rítmico?", "Una secuencia de sonidos y silencios que se repite", "Un patrón vuelve a sonar sobre el pulso.")],
    (
        f"Camina en tu lugar con paso parejo. Toca con las palmas el patrón {P(TA, TT, TAA, SIL)} cuatro veces seguidas, marcando más fuerte el primer pulso de cada vuelta. Escribe cuántos pulsos y cuántos sonidos tiene el patrón y cuántos pulsos tocaste en total.",
        "El patrón tiene 5 pulsos y 4 sonidos. Lo toqué 4 veces: 20 pulsos en total.",
        ["mantiene el pulso parejo con los pies", "toca el patrón con el silencio en su lugar", "escribe los conteos correctos"],
        ["interpretación", "conteo escrito"],
        ["no contar el silencio como pulso", "contar TAA como un pulso"],
        "Reconoce el pulso estable y pide que marque con el dedo dónde está el silencio y dónde dura 2 pulsos el TAA.",
    ),
    "Camina 16 pasos parejos y aplaude solo en el primer paso de cada grupo de 4. Cuenta cuántos aplausos diste.",
    "Inventa un patrón de 8 pulsos con TA, ti-ti, TAA y SIL, y calcula sus pulsos y sus sonidos.",
)

# ---------------------------------------------------------------- OA 01 · clase 3
F1 = (TA, TT, TA, TAA)
F2 = (TA, TT, TA, TAA)
F3 = (TAA, SIL, TIRI, TIRI)
F4 = (TA, TT, TA, TA)
F5 = (TA, TA, TIRI, TAA)

L(
    OA1, 3,
    f"Lápiz y palmas. Leyenda: {LEY}. Cada frase tiene 4 símbolos y todas están escritas en los ejercicios.",
    "Aprenderé a comparar repetición (reiteración), contraste y variación, y a reconocer la pregunta y respuesta. Sirve para entender cómo está armada una música.",
    ["Sé contar pulsos en un patrón.", "Sé qué es una frase musical corta.", "Sé comparar dos sonidos."],
    [
        "Una música se arma con frases. Si una frase vuelve igual, hay repetición, que también se llama reiteración. Si llega una frase muy distinta, hay contraste. Si vuelve casi igual pero cambia una parte, hay variación. Un contraste puede ser de ritmo, pero también de timbre, de altura o de intensidad.",
        f"Para decidir, compara las frases símbolo por símbolo. Frase 1: {P(*F1)}. Frase 2: {P(*F2)}. No cambia ningún símbolo: es repetición. Frase 3: {P(*F3)}. Cambia todo: es contraste. Frase 4: {P(*F4)}. Cambia solo el último símbolo: es variación.",
        "Otra forma de organizar frases es la pregunta y respuesta. La primera frase queda «abierta», como si preguntara. La segunda frase contesta y da la sensación de cerrar. A veces la respuesta es una variación de la pregunta. Se puede repartir entre dos personas o dos instrumentos, uno pregunta y el otro responde.",
    ],
    [("repetición (reiteración)", "una frase vuelve igual"), ("contraste", "llega algo muy distinto"), ("variación", "vuelve casi igual, con una parte cambiada"), ("pregunta y respuesta", "una frase abierta y otra que contesta"), ("frase", "grupo corto de sonidos que forma una idea musical")],
    [
        ("Clasificar una frase", f"Frase A: {P(*F1)}. Frase B: {P(*F4)}. ¿Es repetición, contraste o variación?", ["Comparo símbolo por símbolo.", "Los tres primeros son iguales y el último cambia de TAA a TA.", "Cambia una sola parte."], "Variación"),
        ("Contar lo que cambia", f"Frase A: {P(*F1)}. Frase C: {P(*F3)}. ¿En cuántos lugares cambian?", ["Posición 1: TA y TAA, cambia.", "Posición 2: ti-ti y SIL, cambia.", "Posición 3: TA y tiri-tiri, cambia.", "Posición 4: TAA y tiri-tiri, cambia."], f"En {diff(F1, F3)} lugares: es un contraste"),
    ],
    [
        ("Llamar variación a una frase donde cambió todo.", "La variación conserva la mayor parte de la frase.", "Si cambió todo es contraste; si cambió una parte es variación."),
        ("Pensar que repetición es que suene parecido.", "En la repetición no cambia nada.", "Si cambia algo, aunque sea pequeño, ya no es repetición."),
    ],
    [
        ex(f"Frase 1: {P(*F1)}. Frase 2: {P(*F2)}. ¿Es repetición, contraste o variación?", "Repetición", "Las dos frases tienen los mismos cuatro símbolos."),
        ex("Suena una frase que queda «abierta» y después otra que la contesta y queda «cerrada». ¿Cuál de las dos es la respuesta: la primera o la segunda?", "La segunda", "La respuesta es la frase que contesta y cierra."),
        ex("Una flauta toca una idea y luego un tambor toca la misma idea, con la misma altura, la misma fuerza y el mismo largo. ¿Qué cualidad cambió: la altura, el timbre o la duración?", "El timbre", "Cambió el instrumento que la produce, o sea, el timbre."),
    ],
    [
        ex(f"Compara {P(*F1)} con {P(*F5)}. ¿En cuántos lugares cambia?", str(diff(F1, F5)), "Cambia la posición 2 (ti-ti por TA) y la posición 3 (TA por tiri-tiri)."),
        ex(f"Compara {P(*F1)} con {P(*F3)}. ¿Es repetición, contraste o variación?", "Contraste", "Cambian los cuatro símbolos: es muy distinta."),
        ex(f"Pregunta: {P(*F1)}. Respuesta: {P(TA, TT, TA, SIL)}. ¿En cuántos lugares cambia la respuesta?", "1", "Solo el último símbolo cambia, de TAA a SIL; la respuesta es una variación."),
    ],
    [
        ex(f"Ordena de menos a más cambio respecto de {P(*F1)}: (a) {P(*F3)}, (b) {P(*F2)}, (c) {P(*F4)}.", "b, c, a", "La b no cambia, la c cambia 1 símbolo y la a cambia 4."),
        ex("Una música tiene las frases A, A, B, A. ¿Cuántas veces se repite la frase A?", "3", "La A aparece en la primera, la segunda y la cuarta posición."),
    ],
    [
        ex(f"Esta pregunta es {P(TA, TA, TT, TAA)}. Su respuesta es una variación que cambia solo el último símbolo por SIL. Escribe la respuesta.", P(TA, TA, TT, SIL), "Se copian los tres primeros símbolos y se cambia el último por SIL."),
        arith(f"La frase {P(*F1)} suena 3 veces seguidas y luego suena {P(*F3)} una vez. ¿Cuántos pulsos son en total?", f"{pulses(*F1)}*3+{pulses(*F3)}", "Se multiplican los pulsos de la primera por 3 y se suman los de la segunda.", " pulsos"),
    ],
    [
        arith(f"La frase {P(*F1)} suena 2 veces y su variación {P(*F4)} suena 2 veces. ¿Cuántos pulsos son en total?", f"{pulses(*F1)}*2+{pulses(*F4)}*2", "Se suman los pulsos de las dos frases, cada una por 2.", " pulsos"),
        ex(f"¿Cuántos sonidos tiene la frase {P(*F3)}?", str(sounds(*F3)), "TAA suena 1, SIL no suena y cada tiri-tiri suena 4."),
    ],
    [ex("En una canción, el mismo estribillo vuelve idéntico después de cada verso. ¿Qué recurso musical es?", "Repetición", "El estribillo vuelve sin cambios.")],
    [ex("Si una frase cambia solo una parte, ¿qué recurso hay?", "Variación", "Es la misma frase con una parte cambiada."), ex("Una frase muy distinta de la anterior, ¿qué recurso es?", "Contraste", "Lo muy distinto es contraste."), ex("¿Cómo se llama la organización en que una frase contesta a otra?", "Pregunta y respuesta", "La segunda frase responde a la primera.")],
    (
        f"Toca con las palmas esta frase base: {P(*F1)}. Después escribe y toca una frase de 4 símbolos que sea una variación (cambia solo uno), otra que sea un contraste (cambian los cuatro) y otra que sea una repetición. Indica cuántos símbolos cambian respecto de la base y toca las tres en orden.",
        f"Base: {P(*F1)}. Variación: {P(TA, TT, TA, SIL)} (cambia 1). Contraste: {P(SIL, TAA, TIRI, TA)} (cambian 4). Repetición: {P(*F1)} (cambian 0).",
        ["escribe tres frases de 4 símbolos", "cuenta correctamente lo que cambia", "toca las frases con pulso parejo"],
        ["frases escritas", "interpretación con palmas"],
        ["llamar variación a un cambio total", "olvidar que la repetición no cambia nada"],
        "Reconoce el conteo de cambios; si duda, pide alinear las frases una bajo otra y comparar símbolo por símbolo.",
    ),
    "Escribe una frase de 4 símbolos y una variación de ella que cambie solo uno.",
    "Crea una pregunta y una respuesta de 4 símbolos cada una y tócalas con una persona de tu casa.",
)

# ---------------------------------------------------------------- OA 01 · clase 4
L(
    OA1, 4,
    "Lápiz, tus palmas y un reloj con segundero, o cuenta «mil uno, mil dos…» como un segundo cada uno. Cuida el volumen: nunca más fuerte que una conversación animada.",
    "Aprenderé a leer y dibujar la dinámica (fuerte, suave y sus cambios) y el tempo (lento, rápido y sus cambios). Sirve para tocar una música con el carácter que pide.",
    ["Sé que fuerte y suave son intensidades.", "Sé qué es un pulso.", "Sé comparar rápido y lento."],
    [
        "La dinámica es cómo cambia la intensidad a lo largo de la música. Se escribe con letras: p significa suave (piano) y f significa fuerte (forte). pp es muy suave y ff es muy fuerte. Una flecha que se abre « < » es crescendo: el sonido sube poco a poco. Una flecha que se cierra « > » es diminuendo: el sonido baja poco a poco.",
        "El tempo es qué tan rápido va el pulso. Un tempo lento tiene pocos pulsos en un tiempo dado, y uno rápido tiene muchos. Si das un pulso por segundo, en 10 segundos das 10 pulsos. Si das el doble de rápido, das 20 en esos mismos 10 segundos. El tempo también puede cambiar poco a poco: acelerando es ir cada vez más rápido y ritardando es ir cada vez más lento.",
        "Dinámica y tempo son distintos. Se puede tocar fuerte y lento, o suave y rápido. Para no confundirlos pregunta primero «¿qué tan fuerte suena?» (dinámica) y después «¿qué tan seguidos van los pulsos?» (tempo). Puedes representarlos con letras, con flechas o con una línea que sube y baja.",
    ],
    [("dinámica", "cambios de intensidad en la música"), ("p (piano) y f (forte)", "suave y fuerte"), ("crescendo ( < )", "sube la intensidad poco a poco"), ("diminuendo ( > )", "baja la intensidad poco a poco"), ("tempo", "qué tan rápido o lento va el pulso"), ("acelerando / ritardando", "cada vez más rápido / cada vez más lento")],
    [
        ("Leer una dinámica", "Una música tiene esta dinámica: p – < – f – > – p. ¿Cómo cambia?", ["Parte suave (p).", "Sube poco a poco ( < ).", "Llega a fuerte (f).", "Baja poco a poco ( > ) y termina suave (p)."], "Suave, sube a fuerte, baja y termina suave"),
        ("Comparar tempos", "Una persona da 10 pulsos en 10 segundos. Otra da 20 pulsos en los mismos 10 segundos. ¿Quién va más rápido?", ["El tiempo es igual: 10 segundos.", "Quien da más pulsos en ese tiempo va más rápido.", "20 es mayor que 10."], "La segunda persona"),
    ],
    [
        ("Decir que crescendo es ir más rápido.", "El crescendo cambia la intensidad, no el tempo.", "Crescendo sube la intensidad; ir más rápido es acelerando."),
        ("Pensar que lento significa suave.", "Se confunden tempo e intensidad.", "Lento habla de los pulsos; suave habla de la intensidad."),
    ],
    [
        ex("¿Qué significa la letra f en una partitura?", "Fuerte", "La letra f viene de forte, que significa fuerte."),
        ex("¿Qué significa la flecha que se abre « < »?", "Crescendo: subir poco a poco", "La flecha abierta indica que la intensidad crece."),
        ex("Una persona da 10 pulsos en 10 segundos y otra da 20 en 10 segundos. ¿Quién va más lento?", "La que da 10 pulsos", "Con el mismo tiempo, menos pulsos es más lento."),
    ],
    [
        ex("Dinámica f – > – p. ¿Cómo cambia la intensidad?", "Parte fuerte y baja hasta suave", "La flecha cerrada baja la intensidad de f a p."),
        ex("Una música va rápida y suave. Otra va lenta y fuerte. ¿Cuál tiene más pulsos en el mismo tiempo?", "La rápida y suave", "Rápida significa más pulsos en el mismo tiempo, sin importar la intensidad."),
        ex("Dibuja con signos una música que parta suave, suba hasta fuerte y se quede fuerte.", "p – < – f", "Suave es p, subir es la flecha abierta y fuerte es f."),
    ],
    [
        arith("Das 1 pulso por segundo durante 30 segundos. ¿Cuántos pulsos das?", "1*30", "Con un pulso por segundo, los pulsos son tantos como segundos.", " pulsos"),
        arith("Das 2 pulsos por segundo durante 10 segundos. ¿Cuántos pulsos das?", "2*10", "Cada segundo tiene 2 pulsos y pasan 10 segundos.", " pulsos"),
        ex("Una música tiene p – < – f – > – p. ¿Cuántas flechas de cambio gradual de intensidad tiene?", "2", "Hay una flecha abierta y una cerrada."),
    ],
    [
        ex("Ana dice: «el crescendo acelera la música». ¿Tiene razón?", "No; el crescendo sube la intensidad, no la velocidad", "Crescendo es sobre la intensidad; el tempo es otro cambio."),
        ex("Una música da 15 pulsos en 10 segundos y otra da 12 pulsos en 10 segundos. ¿Cuál es más lenta?", "La de 12 pulsos", "Con el mismo tiempo, menos pulsos es más lento."),
    ],
    [
        arith("Una música lenta da 1 pulso por segundo y otra más rápida da 2 pulsos por segundo. En 20 segundos, ¿cuántos pulsos más da la rápida?", "2*20-1*20", "Rápida: 2 × 20 = 40; lenta: 1 × 20 = 20; se restan.", " pulsos más"),
        ex("Escribe una dinámica de cinco signos que parta fuerte, baje poco a poco hasta suave y luego vuelva a subir hasta fuerte.", "f – > – p – < – f", "f, flecha cerrada hasta p, flecha abierta hasta f."),
    ],
    [ex("Una persona canta una canción de cuna: va lenta y suave. Otra marcha rápido y fuerte. ¿Qué dinámica y qué tempo tiene cada una?", "Cuna: suave y lenta; marcha: fuerte y rápida", "La cuna va suave y lenta; la marcha va fuerte y rápida.")],
    [ex("¿Qué significa p?", "Suave", "p viene de piano, que significa suave."), ex("¿La flecha cerrada « > » sube o baja la intensidad?", "Baja", "Es el diminuendo."), ex("Más pulsos en el mismo tiempo, ¿es más lento o más rápido?", "Más rápido", "El tempo rápido tiene más pulsos en el mismo tiempo.")],
    (
        "Elige un patrón de palmas de 4 pulsos, por ejemplo TA – TA – TA – SIL. Tócalo 3 veces seguidas: primero suave (p), después con crescendo hasta fuerte (f) y al final con diminuendo hasta suave. Cuida el volumen. Luego toca el mismo patrón en un tempo lento y en uno rápido, contando los pulsos en 10 segundos. Dibuja la dinámica con signos y escribe cuál tempo fue más rápido y por qué.",
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
    "Aprenderé a distinguir las formas A, AB y ABA y a representarlas con letras y cajas. Sirve para ver cómo está construida una música.",
    ["Sé reconocer repetición y contraste.", "Sé contar pulsos.", "Sé comparar suave y fuerte."],
    [
        "Una sección es una parte de la música con un carácter propio. A la primera le ponemos la letra A. Si llega una parte contrastante, es B. Si la música tiene solo A, su forma es A. Si tiene A y luego B, su forma es AB. Si al final vuelve la A, su forma es ABA.",
        f"Un ejemplo de ABA: {SEC_TXT}. Hay tres secciones, pero solo dos distintas: A y B. La A vuelve al final igual que al principio. En total son {SEC_TOTAL} pulsos. Para saber la forma, mira en qué orden aparecen las secciones, no cuánto dura cada una.",
        "Representar una forma es dibujar cajas con letras, una caja por sección, en orden: A | B | A. El largo de la caja puede mostrar cuánto dura. Si la sección vuelve igual se usa la misma letra. Si vuelve un poco cambiada se escribe A', que se lee «A prima». Una sección se reconoce por su carácter: instrumento, intensidad, tempo o altura.",
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
        ex("Una música tiene una parte lenta y suave, y luego una parte rápida y fuerte. No vuelve la primera. ¿Qué forma tiene?", "AB", "Hay dos partes distintas y no vuelve la primera."),
        ex("Si una música tiene una sola sección, ¿qué forma tiene?", "A", "Una sola sección es forma A."),
        ex("En la forma ABA, ¿qué sección vuelve al final?", "La A", "Después de B vuelve la sección A."),
    ],
    [
        ex(f"Una música tiene {SEC_TXT}. ¿Cuántas secciones tiene en total?", "3", "Se cuentan las tres partes aunque dos sean iguales."),
        ex("Una música tiene cuatro partes en este orden: A, B, A, B. ¿Cuántas letras distintas usa?", "2", "Solo se usan A y B."),
        ex("Dibuja con cajas y letras la forma de una música con una parte A, una B y otra vez la A.", "A | B | A", "Se dibuja una caja por sección, en el orden en que suenan."),
    ],
    [
        arith("Una música tiene A de 8 pulsos, B de 4 pulsos y A de 8 pulsos. ¿Cuántos pulsos suenan en total?", "8+4+8", "Se suman los pulsos de las tres secciones.", " pulsos"),
        ex("Una música tiene A de 8 pulsos y B de 8 pulsos. Otra tiene A, B, A con 8 pulsos cada una. ¿Cuántos pulsos más dura la segunda?", "8 pulsos", "La segunda tiene una sección A de 8 pulsos adicional."),
        ex("En una música, A es suave y B es fuerte. Está escrita así: A B A B A. ¿Cuántas veces suena la parte suave?", "3", "La A aparece en las posiciones 1, 3 y 5."),
    ],
    [
        ex("Pedro dice: «si cada sección dura 8 pulsos, la forma AB y la forma ABA duran lo mismo». ¿Tiene razón?", "No; AB dura 16 pulsos y ABA dura 24", "AB tiene dos secciones de 8 pulsos y ABA tiene tres."),
        ex("Una música es A B A', donde A' es la A un poco cambiada. Si A' se considera parte de A, ¿cuántas secciones distintas hay?", "2", "A' sigue siendo la sección A con un cambio; las distintas son A y B."),
    ],
    [
        arith("Una música ABA dura 24 pulsos. La A dura 8 pulsos cada vez que suena. ¿Cuántos pulsos dura la B?", "24-8-8", "Al total se le quitan las dos veces que suena la A.", " pulsos"),
        ex("Escribe una forma de cinco secciones en que la B esté en el lugar 3 y todas las demás sean A.", "A A B A A", "La B va en el centro y las otras cuatro secciones son A."),
    ],
    [ex("En una obra se escucha una melodía tranquila, luego otra con ritmo marcado y al final la tranquila de nuevo. ¿Qué forma tiene?", "ABA", "La primera parte vuelve al final.")],
    [ex("¿Cómo se llama una música con las partes A y luego B?", "AB", "Dos secciones distintas, sin volver a la primera."), ex("En ABA, ¿cuántas letras distintas hay?", "2", "A y B."), ex("¿La forma depende del orden de las secciones o del largo de cada una?", "Del orden", "La forma muestra en qué orden aparecen las secciones.")],
    (
        "Crea una forma ABA con tus palmas: la sección A es suave y de 4 pulsos (por ejemplo TA – TA – TA – SIL), la B es fuerte y de 4 pulsos distintos, y vuelve la A. Dibuja tres cajas con las letras y escribe cuántos pulsos dura en total tu música.",
        "A: TA – TA – TA – SIL (suave); B: TAA – TAA (fuerte); A de nuevo. Forma A | B | A. Total 12 pulsos.",
        ["crea dos secciones con carácter distinto", "vuelve la A igual", "dibuja las cajas y calcula el total"],
        ["interpretación con palmas", "dibujo de cajas", "cálculo escrito"],
        ["que la B suene casi igual que la A", "contar mal los pulsos del total"],
        "Reconoce que la A vuelve igual y pregunta qué hizo distinta a la B; revisa el total sumando.",
    ),
    "Recuerda una canción que conozcas y di si repite una parte. Anótala con letras sin copiar su letra.",
    "Crea una forma ABAB con dos sonidos distintos de tu casa y dibújala con cajas.",
)

# ---------------------------------------------------------------- OA 02 · clase 1
TEXTO = "Una música dura 8 pulsos. Suena una flauta suave, con sonidos agudos y largos, que va lenta. No hay otros instrumentos."

L(
    OA2, 1,
    f"Lápiz. La música que se escucha está descrita por escrito en cada ejercicio, así que no necesitas audio. Texto de trabajo: «{TEXTO}».",
    "Aprenderé a separar lo que se oye (evidencia sonora) de lo que imagino o siento, y a unirlos en una respuesta cada vez más elaborada. Sirve para explicar una música de modo que otros lo puedan comprobar.",
    ["Sé nombrar las cualidades del sonido.", "Sé que cada persona puede sentir algo distinto con la misma música.", "Sé decir «yo escuché»."],
    [
        "Cuando escuchas música puedes decir dos tipos de cosas. Una es lo escuchado: que es lenta, que es suave, que suena una flauta. Eso se puede comprobar volviendo a escuchar. La otra es lo imaginado o sentido: que parece un río, que te dio calma, que te recordó un lugar. Eso es personal y no se comprueba de la misma forma.",
        "Una respuesta puede tener grados de elaboración. En el grado 1 solo opinas: «me gustó». En el grado 2 das evidencia: «escuché una flauta suave y lenta». En el grado 3 unes evidencia e idea con «por eso»: «escuché una flauta suave y lenta, por eso imaginé una mañana tranquila». Mientras más une lo oído con lo imaginado, más elaborada es la respuesta.",
        "Dos personas pueden imaginar cosas distintas con la misma música, y ambas pueden estar bien si explican qué oyeron para pensarlo. Lo que no sirve es decir solo «me gustó» o «parecía un perro» sin decir qué sonido lo mostró.",
    ],
    [("sensación", "lo que sientes al escuchar"), ("emoción", "calma, alegría, miedo, tristeza u otras que sientes"), ("idea", "algo que imaginas al escuchar"), ("evidencia sonora", "lo que se oye y se puede comprobar volviendo a escuchar"), ("elaborada", "que une varias cosas con explicación")],
    [
        ("Clasificar una frase", f"Texto: «{TEXTO}». La frase «Parecía una mañana tranquila en el campo». ¿Es evidencia sonora o es imaginado?", ["Pregunto si se puede comprobar volviendo a escuchar.", "«Mañana tranquila» no se oye, se imagina."], "Imaginado"),
        ("Subir de grado", f"Texto: «{TEXTO}». Una niña dice solo «me gustó». ¿Cómo la subes al grado 3?", ["Agrego lo que se oyó: flauta suave y lenta.", "Agrego una idea y la uno con «por eso»."], "«Escuché una flauta suave y lenta, por eso imaginé un día tranquilo»"),
    ],
    [
        ("Decir solo «me gustó» y no explicar qué se oyó.", "Una opinión sin evidencia no muestra qué escuchaste.", "Agrega algo que oíste: suave, lento, agudo, una flauta."),
        ("Creer que la idea de otra persona está mal porque es distinta.", "La música puede sugerir cosas distintas.", "Pregunta «¿qué oíste para pensar eso?»."),
    ],
    [
        ex(f"Texto: «{TEXTO}». ¿«Suena una flauta» es evidencia sonora o imaginado?", "Evidencia sonora", "Se puede comprobar volviendo a escuchar qué instrumento suena."),
        ex(f"Texto: «{TEXTO}». ¿«Me dio ganas de dormir» es evidencia sonora o sensación personal?", "Sensación personal", "Dormir no se oye; es lo que la persona sintió."),
        ex(f"Texto: «{TEXTO}». ¿Los sonidos de la flauta son agudos o graves?", "Agudos", "El texto dice que la flauta tiene sonidos agudos."),
    ],
    [
        ex(f"Texto: «{TEXTO}». ¿Cuántas frases de la lista son evidencia sonora? (a) es lenta, (b) parecía una nube, (c) es suave, (d) me dio frío.", "2", "Solo (a) y (c) se pueden comprobar; (b) y (d) son imaginados o sentidos."),
        ex("Según la clase, ¿qué palabras unen lo que oíste con lo que sentiste en una respuesta de grado 3?", "Por eso", "«Por eso» conecta la evidencia con la sensación."),
        ex("Dos niños escuchan lo mismo. Uno imagina un río y el otro una lluvia suave. Los dos explican que oyeron sonidos suaves y seguidos. ¿Alguno está equivocado?", "Ninguno", "Los dos dan evidencia sonora y sus ideas son personales."),
    ],
    [
        ex("Ordena de menos a más elaborada: (a) «me gustó», (b) «escuché una flauta suave y por eso sentí calma», (c) «suena una flauta».", "a, c, b", "(a) opina; (c) da evidencia; (b) une evidencia y sensación."),
        ex("Luisa dice: «esta música es triste porque yo lo digo». ¿Qué le falta a su respuesta?", "Evidencia sonora", "Le falta decir qué se oye que la hace pensar eso."),
        ex("Una frase dice solo «la música sonó aguda y suave». ¿Qué grado de elaboración tiene: 1, 2 o 3?", "Grado 2", "Da evidencia sonora, pero no la une con una idea o sensación."),
    ],
    [
        ex("Se escucha una música con tambores fuertes y rápidos. ¿Qué respuesta es de grado 3: (a) «Me gustó.», (b) «Escuché tambores fuertes y rápidos, por eso imaginé una carrera.», (c) «Imaginé una carrera.»?", "b", "La (b) dice qué se oyó y la idea que sugirió; (a) solo opina y (c) no da evidencia."),
        ex("Una persona dice «la música sonó fuerte y rápida». Otra dice «me dio miedo». ¿Cuál frase habla de lo oído y cuál de lo sentido?", "La primera habla de lo oído; la segunda de lo sentido", "Fuerte y rápida se oyen; el miedo es una sensación."),
    ],
    [
        ex("Una niña dice: «Escuché tambores graves y fuertes, por eso me sentí en medio de una tormenta». Nombra la evidencia sonora, la idea y las palabras que las unen.", "Evidencia: tambores graves y fuertes; idea: una tormenta; unen: por eso", "Lo oído son los tambores graves y fuertes; la tormenta es lo imaginado."),
        ex("Una respuesta dice: «Me gustó, es lenta y suena una flauta». ¿Qué le falta para ser de grado 3?", "Unir lo oído con una idea o sensación usando «por eso»", "Tiene opinión y evidencia, pero no las relaciona con lo imaginado."),
    ],
    [ex("Un niño escucha una música lenta y suave, de cuna, y dice: «parece un barco meciéndose». ¿Qué evidencia sonora sostiene su idea: (a) «Suena lenta y suave.» o (b) «Suena fuerte y rápida.»?", "(a)", "Lo lento y suave se parece al balanceo tranquilo de un barco.")],
    [ex("¿«Es lenta» es evidencia sonora o imaginado?", "Evidencia sonora", "El tempo se puede comprobar volviendo a escuchar."), ex("¿«Me recordó mi casa» es evidencia sonora o imaginado?", "Imaginado", "Es un recuerdo personal."), ex("En «Escuché una flauta suave, por eso sentí calma», ¿qué va después de «por eso»?", "La sensación", "Después de «por eso» va lo que se sintió o imaginó.")],
    (
        "Una persona de tu casa golpea una mesa con una cuchara de madera: primero 8 golpes suaves y lentos y después 8 golpes fuertes y rápidos (con cuidado de no dañar la mesa). Escucha cada parte. Para cada una escribe una frase de grado 3: lo que oíste, «por eso» y lo que imaginaste o sentiste.",
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
    "Aprenderé a expresar lo que escucho con el cuerpo y el movimiento, y a explicar por qué elegí ese movimiento. Sirve para mostrar la música sin usar palabras.",
    ["Sé caminar y detenerme.", "Sé qué es una evidencia sonora.", "Sé que lento y rápido son tempos."],
    [
        "El movimiento puede mostrar cualidades de la música. Si la música es lenta, los movimientos pueden ser lentos. Si es fuerte, pueden ser grandes y firmes. Si es suave, pueden ser pequeños y delicados. Si los sonidos son agudos, puedes estirarte hacia arriba; si son graves, hacia abajo.",
        "Un movimiento bien elegido tiene un porqué sonoro. Por ejemplo: «hice movimientos lentos porque los pulsos iban lentos». Así tu movimiento no es solo bonito: está unido a lo que escuchaste. También puedes marcar el pulso con los pies y los acentos con un movimiento más grande.",
        "Para elaborar más tu respuesta, cambia el movimiento cuando cambie la música: si la música pasa de suave a fuerte, tu movimiento pasa de pequeño a grande. Cuida tu cuerpo y el de los demás y mueve solo lo que te acomode. Si no quieres bailar, haz gestos con las manos o la cabeza. No hay un movimiento único correcto, pero cada movimiento debe poder explicarse con algo que se oyó.",
    ],
    [("movimiento", "cambio de posición del cuerpo"), ("gesto", "movimiento pequeño, por ejemplo de las manos"), ("pulso", "latido parejo que puedes marcar con los pies"), ("amplio", "grande, que ocupa mucho espacio"), ("delicado", "pequeño y suave")],
    [
        ("Elegir movimiento para una música", "Música: suave, lenta y grave. ¿Qué movimiento le queda mejor: (a) saltos grandes y rápidos, (b) movimientos pequeños y lentos hacia abajo?", ["La música es suave: movimientos suaves.", "La música es lenta: movimientos lentos.", "Es grave: hacia abajo."], "(b), porque coincide con suave, lenta y grave"),
        ("Contar movimientos", "Marchas 4 pasos al ritmo de la música y repites la marcha 3 veces. ¿Cuántos pasos das?", ["Cada marcha tiene 4 pasos.", "Se repite 3 veces: 4 × 3."], "12 pasos"),
    ],
    [
        ("Hacer un movimiento grande porque «se ve más bonito», sin relación con la música.", "El movimiento debe responder a lo que se escucha.", "Escucha primero y elige un movimiento que coincida con suave, fuerte, lento o rápido."),
        ("Moverse siempre igual aunque la música cambie.", "No muestra el cambio que se oyó.", "Cambia el tamaño o la rapidez de tu movimiento cuando cambie la música."),
    ],
    [
        ex("La música suena fuerte. ¿Qué movimiento elegirías: (a) pequeño y delicado o (b) grande y firme?", "(b)", "Lo fuerte se muestra con un movimiento grande y firme."),
        ex("Si los sonidos suben cada vez más agudos, ¿hacia dónde puedes mover los brazos: hacia arriba o hacia abajo?", "Hacia arriba", "Lo agudo se muestra hacia arriba."),
        ex("¿Qué parte del cuerpo puedes usar para marcar el pulso parejo de la música?", "Los pies", "Los pasos o golpes de pie son parejos como el pulso."),
    ],
    [
        ex("Una música tiene dos partes: la primera lenta y suave, la segunda rápida y fuerte. ¿Qué haces con el movimiento al pasar de la primera a la segunda: lo mantienes igual o lo cambias?", "Lo cambio", "La música cambió, así que el movimiento debe mostrarlo."),
        ex("Dices: «hice pasos cortos porque los sonidos eran suaves». ¿Cuál es la evidencia sonora de esa frase?", "Los sonidos eran suaves", "La frase después de «porque» dice qué se oyó."),
        ex("Una música tiene pulsos con acento cada 4. Si das un salto pequeño en el pulso 1 y pasos normales en los otros, ¿en qué pulsos das pasos normales?", "2, 3 y 4", "El salto marca el acento del 1."),
    ],
    [
        ex("Ana quiere mostrar una música que se va apagando poco a poco. ¿Cómo cambia su movimiento: de grande a pequeño o de pequeño a grande?", "De grande a pequeño", "Apagarse es bajar la intensidad, que se muestra achicando el movimiento."),
        ex("Dos niños muestran la misma música con movimientos distintos y ambos explican qué oyeron para elegirlos. ¿Hay uno solo correcto?", "No", "Ambos tienen una razón sonora; el movimiento puede variar."),
        ex("Una música baja poco a poco de sonidos agudos a sonidos graves. ¿Hacia dónde terminan tus brazos: arriba o abajo?", "Abajo", "Lo grave se muestra hacia abajo."),
    ],
    [
        arith("Una música tiene 2 partes de 8 pulsos cada una y das un paso en cada pulso. ¿Cuántos pasos das en total?", "2*8", "Dos partes de 8 pulsos suman 16 pasos.", " pasos"),
        ex("Una persona mueve los brazos en pequeño en la parte suave y en grande en la parte fuerte. ¿Qué explicación sirve para la parte fuerte: (a) «Hice movimientos grandes porque la música sonaba fuerte.» o (b) «Hice movimientos grandes porque sí.»?", "(a)", "La explicación une el movimiento con la intensidad escuchada."),
    ],
    [
        arith("Una música tiene 3 partes de 4 pulsos. Das un paso por pulso, pero en cada parte hay 1 pulso de silencio en que te quedas quieto. ¿Cuántos pasos das?", "3*(4-1)", "En cada parte das 3 pasos y hay 3 partes.", " pasos"),
        ex("Una niña explica: «hice movimientos grandes porque me gusta». ¿Qué le falta a su explicación?", "La evidencia sonora", "Debe decir qué se oyó que justifica el movimiento."),
    ],
    [ex("Una música de marcha se oye fuerte y con pulso marcado. Una niña la muestra con pasos firmes y parejos. ¿Qué evidencia sonora sostiene su elección: (a) «Se oye fuerte y con pulso marcado.» o (b) «A ella le gusta caminar.»?", "(a)", "Lo fuerte y el pulso marcado se oyen; el gusto no es evidencia sonora.")],
    [ex("¿Qué movimiento muestra un sonido muy suave: grande o pequeño?", "Pequeño", "Lo suave se muestra con un movimiento pequeño."), ex("¿Qué se marca con un movimiento más grande: el acento o el pulso suave?", "El acento", "El acento es el pulso que se marca más fuerte."), ex("¿Para qué sirve decir «porque…» después de tu movimiento?", "Para unirlo con lo que oíste", "Así el movimiento tiene una razón sonora.")],
    (
        "Una persona de tu casa te dice dos músicas descritas: Música 1: suave, lenta y grave. Música 2: fuerte, rápida y aguda. Muestra cada una con un movimiento de cuerpo o de manos. Después escribe una frase por cada música, con «porque», que explique tu movimiento con lo que se oyó. No muevas nada que te incomode.",
        "Música 1: hice movimientos pequeños, lentos y hacia abajo porque la música era suave, lenta y grave. Música 2: hice saltos y brazos hacia arriba porque era fuerte, rápida y aguda.",
        ["elige un movimiento distinto para cada música", "explica cada uno con «porque»", "relaciona el movimiento con al menos dos cualidades"],
        ["movimiento", "frases escritas"],
        ["explicar con «porque me gusta»", "mover igual las dos músicas"],
        "Reconoce la relación entre el movimiento y las cualidades; pregunta «¿qué oíste para elegir ese movimiento?» y acepta variaciones personales.",
    ),
    "Camina lento y suave, y luego rápido y fuerte, como si fueran dos músicas. Di qué cualidad mostró cada movimiento.",
    "Muestra con las manos una música que primero sube y luego baja, y explica cuál es la evidencia sonora.",
)

# ---------------------------------------------------------------- OA 02 · clase 3
L(
    OA2, 3,
    "Papel, lápiz y, si tienes, lápices de colores. Las músicas están descritas por escrito. Código visual de la clase: altura = posición en la hoja (arriba agudo, abajo grave); intensidad = grosor de la línea (gruesa fuerte, delgada suave); duración = largo de la línea.",
    "Aprenderé a traducir las cualidades del sonido a líneas, formas y colores, y a explicar el dibujo con evidencia sonora. Sirve para expresar la música de manera visual.",
    ["Sé nombrar altura, intensidad y duración.", "Sé explicar un movimiento con «porque».", "Sé dibujar líneas."],
    [
        "Se puede dibujar lo que se escucha. Una convención es la regla que todos acordamos para leer un dibujo. En esta clase usaremos esta: la altura se dibuja en la posición vertical, con los sonidos agudos arriba y los graves abajo. La intensidad se dibuja con el grosor: línea gruesa si es fuerte y delgada si es suave. La duración se dibuja con el largo de la línea.",
        "El timbre se puede mostrar con el color o con la textura. Por ejemplo, una flauta puede ser azul y un tambor puede ser rojo. Esa elección es personal, pero debe explicarse y mantenerse en todo el dibujo. Además, se puede decir qué imagen sugiere la música, como un río o una tormenta, siempre que se diga qué se oyó para pensar eso.",
        "Un dibujo bien elaborado se lee de izquierda a derecha, como el tiempo: lo que suena primero va a la izquierda. Después escribes una explicación corta: «dibujé una línea alta, delgada y larga porque la flauta sonaba aguda, suave y larga». Sin explicación, el dibujo no muestra qué evidencia usaste.",
    ],
    [("convención", "regla acordada para leer un dibujo"), ("posición vertical", "arriba o abajo en la hoja"), ("grosor", "qué tan gruesa o delgada es una línea"), ("textura", "cómo se ve o se siente una superficie"), ("de izquierda a derecha", "el orden en que pasa el tiempo en el dibujo")],
    [
        ("Leer un dibujo", "Una línea está arriba, es gruesa y es corta. Con la convención de la clase, ¿qué sonido representa?", ["Arriba es agudo.", "Gruesa es fuerte.", "Corta es de poca duración."], "Un sonido agudo, fuerte y corto"),
        ("Dibujar un sonido", "Un tambor suena grave, suave y largo. ¿Cómo dibujas su línea?", ["Grave: abajo en la hoja.", "Suave: línea delgada.", "Largo: línea larga."], "Una línea abajo, delgada y larga"),
    ],
    [
        ("Poner los sonidos graves arriba porque «se ve mejor».", "Rompe la convención y el dibujo no se podrá leer.", "Respeta la convención: arriba agudo, abajo grave."),
        ("Dibujar sin explicar qué se oyó.", "No se sabe qué evidencia usaste.", "Agrega una frase que una el dibujo con lo escuchado."),
    ],
    [
        ex("Con la convención de la clase, ¿qué cualidad se muestra con el grosor de la línea?", "La intensidad", "Gruesa es fuerte y delgada es suave."),
        ex("Una línea está abajo en la hoja. ¿Representa un sonido agudo o grave?", "Grave", "Abajo es grave en la convención."),
        ex("¿En qué lado de la hoja pones el sonido que suena primero?", "A la izquierda", "El tiempo se lee de izquierda a derecha."),
    ],
    [
        ex("Un sonido es agudo, suave y muy largo. ¿Cómo es su línea: (a) arriba, delgada y larga o (b) abajo, gruesa y corta?", "(a)", "Agudo es arriba, suave es delgada y largo es una línea larga."),
        ex("Dos líneas están a la misma altura. La primera es gruesa y la segunda delgada. ¿En qué cualidad se diferencian?", "En la intensidad", "La altura es igual y cambia el grosor, que muestra la intensidad."),
        ex("Un dibujo tiene una línea larga a la izquierda y una corta a la derecha, las dos a la misma altura. ¿Cuál sonido duró más?", "El primero", "La línea más larga muestra mayor duración."),
    ],
    [
        ex("En un dibujo, una línea sube de abajo hacia arriba mientras se engrosa. ¿Qué cambia en el sonido?", "Se vuelve más agudo y más fuerte", "Subir es más agudo y engrosar es más fuerte."),
        ex("Una niña dibuja la flauta en azul y el tambor en rojo. ¿Qué cualidad muestran los colores?", "El timbre", "El color distingue qué instrumento suena."),
        ex("Una línea delgada, baja y larga, ¿qué sonido representa?", "Grave, suave y largo", "Baja es grave, delgada es suave y larga es de mucha duración."),
    ],
    [
        ex("Una línea gruesa, baja y corta representa un tambor. ¿Qué explicación calza: (a) «porque el tambor sonó fuerte, grave y breve» o (b) «porque el tambor sonó suave, agudo y largo»?", "(a)", "Gruesa es fuerte, baja es grave y corta es breve."),
        ex("Luis dibuja una tormenta y dice «sonó fuerte y grave, por eso usé líneas gruesas y bajas». ¿Cuáles son las dos cualidades que menciona?", "Intensidad y altura", "Fuerte es intensidad y grave es altura."),
    ],
    [
        ex("Tres líneas a la misma altura, de izquierda a derecha, son cada vez más gruesas. ¿Cómo cambia la intensidad de los sonidos?", "Sube: cada vez más fuerte", "El grosor creciente muestra una intensidad creciente."),
        ex("Un sonido agudo, fuerte y corto va seguido de otro grave, suave y largo. Comparada con la primera línea, ¿cómo es la segunda en posición, grosor y largo?", "Más baja, más delgada y más larga", "Grave es más abajo, suave es más delgada y largo es más larga."),
    ],
    [ex("Una música empieza con sonidos graves y suaves y termina con sonidos agudos y fuertes. ¿Cómo cambia el dibujo de izquierda a derecha en altura y en grosor?", "Sube y se engrosa", "Pasa de abajo a arriba y de delgado a grueso.")],
    [ex("¿Qué se dibuja con el largo de una línea?", "La duración", "Más largo significa que suena por más tiempo."), ex("¿Una línea delgada muestra un sonido fuerte o suave?", "Suave", "En la convención, delgada es suave."), ex("¿Cuál cualidad se puede mostrar con el color?", "El timbre", "El color puede señalar qué instrumento suena.")],
    (
        "Dibuja esta música descrita: primero una flauta aguda, suave y larga; después un tambor grave, fuerte y corto; al final la flauta otra vez, aguda, fuerte y corta. Usa la convención de la clase y un color distinto para cada instrumento. Escribe una frase con «porque» para cada parte, que explique tu dibujo con lo que se oyó.",
        "Parte 1: línea alta, delgada y larga, en azul, porque la flauta sonaba aguda, suave y larga. Parte 2: línea baja, gruesa y corta, en rojo, porque el tambor sonaba grave, fuerte y corto. Parte 3: línea alta, gruesa y corta, en azul.",
        ["respeta la convención de altura, grosor y largo", "usa un color distinto para cada instrumento", "explica cada parte con «porque»"],
        ["dibujo", "frases escritas"],
        ["cambiar la convención en medio del dibujo", "olvidar la explicación"],
        "Reconoce que respeta la convención y pide explicar un rasgo; no corrige el estilo del dibujo.",
    ),
    "Dibuja con una línea gruesa y baja un sonido fuerte y grave, y con una línea delgada y alta uno suave y agudo.",
    "Dibuja una música de cuatro sonidos de tu casa con la convención y escribe la explicación.",
)

# ---------------------------------------------------------------- OA 02 · clase 4
L(
    OA2, 4,
    "Papel, lápiz y un espacio seguro para moverte. La música está descrita por escrito en la clase. Si quieres, usa tus palmas y tu voz a volumen bajo.",
    "Aprenderé a construir una respuesta multimodal, que combina varios medios expresivos (verbal, corporal, musical y visual) para una misma música. Sirve para elaborar una respuesta más completa y coherente.",
    ["Sé separar lo oído de lo imaginado.", "Sé explicar un movimiento con «porque».", "Sé dibujar con una convención."],
    [
        "Un medio expresivo es la forma que usas para comunicar: palabras (verbal), movimiento (corporal), sonidos que haces (musical) o dibujo (visual). Una respuesta multimodal usa dos o más medios para la misma música. Lo importante es que todos digan lo mismo: si la música es suave y lenta, tu movimiento, tu dibujo y tu frase deben mostrar suave y lento.",
        "Para construirla sigue tres pasos. Primero anota la evidencia sonora: qué cualidades oíste. Segundo elige dos medios, por ejemplo movimiento y dibujo. Tercero escribe una frase verbal con «por eso», que una la evidencia con lo que imaginaste o sentiste. Así tu respuesta llega a un grado alto de elaboración.",
        "Revisa la coherencia con una pregunta: ¿cada medio muestra las mismas cualidades que anoté? Si en el dibujo la línea es gruesa pero escribiste que la música era suave, hay una contradicción y debes corregir. Una respuesta no es mejor por usar más medios, sino por ser clara y estar respaldada por lo que se oyó.",
    ],
    [("medio expresivo", "forma de comunicar: verbal, corporal, musical o visual"), ("multimodal", "que usa dos o más medios expresivos"), ("coherente", "que todas sus partes dicen lo mismo"), ("contradicción", "dos cosas que no pueden ser ciertas a la vez"), ("grado de elaboración", "qué tan completa y explicada es la respuesta")],
    [
        ("Revisar la coherencia", "Música: fuerte y rápida. Una niña la mostró con saltos grandes, con una línea gruesa y escribió «sonó suave y lenta». ¿Qué medio no es coherente?", ["Saltos grandes y línea gruesa muestran fuerte.", "La frase dice suave y lenta, que es lo contrario."], "La frase escrita"),
        ("Armar una respuesta", "Música oída: flauta aguda y lenta. Medios elegidos: movimiento y palabras. ¿Qué haces en cada medio?", ["Movimiento: gestos lentos con los brazos hacia arriba.", "Palabras: «escuché una flauta aguda y lenta, por eso imaginé un pájaro volando despacio»."], "Gestos lentos hacia arriba y una frase con «por eso»"),
    ],
    [
        ("Usar muchos medios sin que digan lo mismo.", "La respuesta se contradice.", "Revisa que movimiento, dibujo y palabras muestren las mismas cualidades."),
        ("Elegir medios sin anotar antes la evidencia sonora.", "No se sabe qué se debe mostrar.", "Primero anota lo oído y después elige los medios."),
    ],
    [
        ex("¿Cuáles son los cuatro medios expresivos que se nombran en la clase?", "Verbal, corporal, musical y visual", "Son las palabras, el movimiento, el sonido que haces y el dibujo."),
        ex("Una respuesta usa un dibujo y una frase para la misma música. ¿Es multimodal?", "Sí", "Usa dos medios distintos: visual y verbal."),
        ex("¿Cuál es el primer paso para construir una respuesta multimodal?", "Anotar la evidencia sonora", "Se parte de lo que se oyó."),
    ],
    [
        ex("Música: suave y lenta. Un niño la muestra con una línea delgada, con pasos pequeños y escribe «sonó suave y lenta». ¿Es coherente su respuesta?", "Sí", "Los tres medios muestran suave y lento."),
        ex("Música: grave y fuerte. Una niña dibuja una línea alta y delgada. ¿Qué rasgos del dibujo no coinciden con la música?", "La altura y el grosor", "Grave es abajo y fuerte es gruesa; ella dibujó alta y delgada."),
        ex("Una respuesta tiene movimiento, dibujo, palabras y un sonido hecho con la voz. ¿Cuántos medios usa?", "4", "Corporal, visual, verbal y musical."),
    ],
    [
        ex("Pedro dice que su respuesta es mejor porque usa cuatro medios, aunque dos se contradicen. ¿Tiene razón?", "No", "Una respuesta es mejor por ser coherente y respaldada, no por tener más medios."),
        ex("Ordena los pasos: (a) elegir dos medios, (b) anotar la evidencia sonora, (c) escribir la frase con «por eso».", "b, a, c", "Se parte de la evidencia, luego se eligen los medios y al final se escribe la frase."),
        ex("Una respuesta usa solo palabras. ¿Es multimodal?", "No", "Multimodal pide dos o más medios expresivos."),
    ],
    [
        ex("Para una música fuerte, rápida y con tambores, ¿qué frase es de grado alto: (a) «Escuché tambores fuertes y rápidos, por eso imaginé una carrera.» o (b) «Imaginé una carrera.»?", "(a)", "La (a) nombra lo oído y lo une con la idea; la (b) no da evidencia."),
        ex("Una música tiene dos partes: una suave y otra fuerte. Si la muestras con movimiento, ¿cómo cambia tu movimiento entre las partes?", "De pequeño a grande", "El movimiento sigue el cambio de suave a fuerte."),
    ],
    [
        ex("Música: aguda y suave. Dibujo: línea alta y delgada. Movimiento: pasos pesados y firmes. ¿Qué medio contradice a los otros dos?", "El movimiento", "Pasos pesados y firmes muestran fuerte, no suave."),
        ex("Un niño tiene un dibujo y un movimiento coherentes pero no escribió ninguna frase. ¿Qué le falta para una respuesta de grado alto?", "Una frase con «por eso» que una la evidencia con su idea", "La frase verbal explica por qué eligió ese dibujo y ese movimiento."),
    ],
    [ex("Una niña escuchó una música con una melodía aguda y lenta, y la mostró con un dibujo de una línea alta y larga y con gestos lentos de los brazos hacia arriba. ¿Qué frase escrita completa su respuesta de modo coherente: (a) «Sonó grave y rápida.» o (b) «Escuché una melodía aguda y lenta, por eso imaginé un globo subiendo»?", "(b)", "La (b) coincide con aguda y lenta; la (a) dice lo contrario.")],
    [ex("¿Qué significa que una respuesta sea coherente?", "Que todas sus partes dicen lo mismo", "Los medios no se contradicen."), ex("Si el dibujo muestra un sonido fuerte, ¿cómo debe ser el movimiento?", "Grande y firme", "Debe mostrar lo mismo que el dibujo."), ex("¿Qué dos palabras unen la evidencia con la idea en la frase?", "Por eso", "Conectan lo oído con lo imaginado.")],
    (
        "Una persona de tu casa te lee esta descripción de una música: «Empieza con una flauta aguda, suave y lenta. Luego entra un tambor grave y fuerte con pulso rápido. Termina con la flauta otra vez». Construye una respuesta multimodal con dos medios que elijas (movimiento, dibujo, voz o palabras). Primero anota la evidencia sonora de cada parte y al final escribe una frase con «por eso». Revisa que no haya contradicciones.",
        "Evidencia: parte 1 flauta aguda, suave y lenta; parte 2 tambor grave, fuerte y rápido; parte 3 flauta. Medios: movimiento y palabras. Parte 1: brazos arriba, despacio. Parte 2: pasos firmes y rápidos. Frase: «Escuché una flauta suave y un tambor fuerte, por eso imaginé que un pájaro se asustaba con una tormenta».",
        ["anota la evidencia sonora de cada parte", "usa al menos dos medios", "escribe una frase con «por eso»", "revisa la coherencia entre los medios"],
        ["evidencia escrita", "respuesta en dos medios", "frase final"],
        ["que un medio diga lo contrario de otro", "escribir la idea sin la evidencia"],
        "Reconoce la coherencia entre medios; si hay una contradicción, pregunta qué se oyó y pide ajustar solo ese medio.",
    ),
    "Elige una música que conozcas y anota dos cualidades que oyes en ella antes de elegir un medio para mostrarla.",
    "Muestra la misma música de la actividad con un tercer medio y verifica que sigue siendo coherente.",
)
