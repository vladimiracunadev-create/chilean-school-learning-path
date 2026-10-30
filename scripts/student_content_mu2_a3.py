"""Student material for 2.º básico Música, OA 05 (explorar e improvisar), OA 06 (presentar el trabajo) y OA 07 (experiencias sonoras de la vida)."""
from __future__ import annotations

import re

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA5, OA6, OA7 = "MU02 OA 05", "MU02 OA 06", "MU02 OA 07"

TA, TT, SIL = "TA", "ti-ti", "SIL"
LEY = "TA = 1 sonido en 1 pulso; ti-ti = 2 sonidos rápidos en 1 pulso; SIL = 1 pulso de silencio"
SILABAS = "Las sílabas se cuentan como se escriben, separadas con guiones; cada sílaba es un golpe de palmas."


def P(*tokens: str) -> str:
    return " – ".join(tokens)


def sounds(*tokens: str) -> int:
    return sum({TA: 1, TT: 2, SIL: 0}[t] for t in tokens)


def S(text: str) -> int:
    return len([piece for piece in re.split(r"[-\s]+", text.strip()) if piece])


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- OA 05 · clase 1
CAJA = "Caja de cartón con tapa. Maneras de sonar: (1) yemas de los dedos sobre la tapa: suave y corto; (2) palma abierta sobre la tapa: más fuerte y corto; (3) raspar la tapa con la uña: suave y largo; (4) golpe con una cuchara de madera: fuerte y corto, con timbre distinto."
L(
    OA5, 1,
    f"Una caja de cartón con tapa, una cuchara de madera y tu voz. Nada de vidrio ni objetos que se rompan o lastimen. Tabla de trabajo: {CAJA}",
    "Aprenderé a explorar los sonidos que puede hacer una misma fuente (voz, cuerpo u objeto seguro) usando altura, timbre, intensidad y duración. Sirve para tener más ideas cuando invento música.",
    ["Sé golpear un objeto con suavidad.", "Sé nombrar las cuatro cualidades del sonido."],
    [
        "Explorar es probar, escuchar y descubrir. Con una sola fuente, como una caja de cartón, puedes hacer muchos sonidos distintos: golpear con la yema de los dedos, con la palma, raspar con la uña o golpear con una cuchara de madera. Cada manera cambia una cualidad: la intensidad, la duración o el timbre.",
        "También la voz explora. Puedes hacer un sonido corto como «tic», uno largo como «sssss», uno agudo, con voz fina como de pajarito, o uno grave, con voz honda como de oso. Cuida tu voz: no grites, no hagas ruidos que te duelan la garganta y toma agua. Con el cuerpo puedes usar palmas, chasquidos suaves o pasos.",
        "Para explorar con cuidado, sigue tres reglas. Primero, no dañes el objeto: golpea con suavidad. Segundo, escucha después de cada intento. Tercero, anota o recuerda cada sonido nuevo, para poder usarlo después. Descubrir sonidos es el primer paso para improvisar y crear.",
    ],
    [("explorar", "probar y descubrir sonidos"), ("fuente sonora", "lo que produce el sonido: voz, cuerpo u objeto"), ("posibilidad", "una manera distinta de hacer sonar algo"), ("cualidad", "altura, timbre, intensidad o duración"), ("objeto seguro", "objeto que no se rompe ni lastima al sonar")],
    [
        ("Contar posibilidades", f"{CAJA} ¿Cuántas maneras distintas de sonar tiene la caja?", ["Cuento las maneras numeradas: 1, 2, 3 y 4.", "Hay cuatro maneras distintas."], "4 maneras"),
        ("Elegir por una cualidad", f"{CAJA} Quieres un sonido suave y largo. ¿Cuál manera eliges?", ["Busco una manera que sea suave y también larga.", "La manera 3 es suave y larga."], "La manera 3: raspar con la uña"),
    ],
    [
        ("Golpear muy fuerte para ver cuántos sonidos salen.", "Se puede romper el objeto o lastimar los oídos.", "Explora con suavidad y escucha después de cada intento."),
        ("Quedarse con un solo sonido.", "Se pierden posibilidades.", "Prueba al menos tres maneras distintas con la misma fuente."),
    ],
    [
        ex("Explorar, ¿es probar y descubrir sonidos o repetir siempre el mismo?", "Probar y descubrir sonidos", "Explorar significa buscar diferentes posibilidades."),
        ex("¿Qué fuente sonora no hay que usar: una caja de cartón o un vaso de vidrio?", "Un vaso de vidrio", "El vidrio puede romperse y lastimar."),
        ex("«Tic» es un sonido de voz, ¿corto o largo?", "Corto", "Dura un instante."),
    ],
    [
        ex(f"{CAJA} ¿Cuáles maneras suenan suave?", "Las maneras 1 y 3", "Dedos y uña se describen como suaves."),
        ex(f"{CAJA} ¿Cuáles maneras suenan corto?", "Las maneras 1, 2 y 4", "Solo la 3 es larga."),
        ex("Con la voz, ¿una voz honda como de oso es aguda o grave, y una voz fina como de pajarito es aguda o grave?", "La de oso es grave; la de pajarito es aguda", "Hondo es grave y fino es agudo."),
    ],
    [
        ex(f"{CAJA} Quieres tres sonidos de la caja que cambien el timbre o la intensidad. Elige tres maneras y di qué cambia.", "Por ejemplo: dedos (suave), palma (fuerte) y cuchara (fuerte con otro timbre)", "Cada manera difiere en intensidad o timbre."),
        arith("Haces cada manera de la caja 2 veces. Son 4 maneras. ¿Cuántos sonidos haces?", "4*2", "Cuatro maneras, dos veces cada una.", " sonidos"),
        ex("Quieres un sonido de voz agudo y largo. ¿Qué haces: un «piiiii» fino y sostenido o un «tic» corto?", "Un «piiiii» fino y sostenido", "Fino es agudo y sostenerlo es largo."),
    ],
    [
        ex("Una niña usa solo la palma sobre la caja y dice que ya exploró todo. ¿Por qué no es cierto?", "Porque la caja tiene otras maneras de sonar", "Explorar es probar muchas posibilidades."),
        ex("¿Cambiar solo de dedos a cuchara cambia el timbre? ¿Por qué?", "Sí, porque el material que golpea es distinto", "El timbre depende de lo que produce el sonido."),
    ],
    [
        ex(f"{CAJA} Escribe una secuencia de tres sonidos usando las maneras 1, 3 y 2, en ese orden. ¿Cuál es suave, cuál es largo y cuál es más fuerte?", "1: suave y corto; 3: suave y largo; 2: más fuerte y corto", "Se lee cada manera según la tabla."),
        ex("Descubres 5 sonidos con una olla de plástico y otros 3 con tus manos. ¿Cuántos sonidos nuevos descubriste?", "8", "5 + 3 = 8."),
    ],
    [ex("En tu casa quieres explorar una caja de cartón vacía. Un adulto te dice que no golpees muy fuerte. ¿Por qué es buena idea?", "Para no romper la caja ni lastimar los oídos", "Explorar con cuidado protege los objetos y las personas.")],
    [ex("¿Qué es explorar?", "Probar y descubrir sonidos", "Es buscar posibilidades."), ex("¿Qué regla de seguridad usas al golpear un objeto?", "Golpear con suavidad", "Así no se rompe ni lastima."), ex("Nombra una cualidad del sonido.", "Por ejemplo: la duración", "Altura, timbre, intensidad y duración son las cuatro cualidades.")],
    (
        f"Elige una fuente segura de tu casa (caja de cartón, tarro de plástico, tu voz o tus manos). Descubre al menos tres sonidos distintos. Para cada uno escribe: cómo lo haces, si es agudo o grave, fuerte o suave, y largo o corto. Si usas la caja, puedes partir de esta tabla: {CAJA}",
        "Tres sonidos con la caja: (1) dedos, suave y corto; (2) palma, más fuerte y corto; (3) uña, suave y largo.",
        ["descubre al menos tres sonidos de una fuente", "usa al menos dos cualidades para describirlos", "explora con cuidado"],
        ["demostración de los sonidos", "tabla escrita", "explicación"],
        ["golpear fuerte un objeto frágil", "repetir el mismo sonido tres veces"],
        "Reconoce la variedad de sonidos y pregunta cuál cualidad cambió entre el primero y el segundo.",
    ),
    "Explora con tus manos tres sonidos sobre una mesa y cuéntalos.",
    "Explora una segunda fuente y compara cuál tiene más posibilidades.",
)

# ---------------------------------------------------------------- OA 05 · clase 2
PREG = (TA, TT, TA, SIL)
L(
    OA5, 2,
    f"Lápiz, tus palmas, un tarro o una caja de cartón y una cuchara de madera. Leyenda: {LEY}. Cada pregunta o respuesta dura 4 pulsos.",
    "Aprenderé a improvisar una pregunta musical y una respuesta, como en una conversación. Sirve para inventar música con otra persona, escuchándola.",
    ["Sé tocar un patrón con palmas.", "Sé contar 4 pulsos.", "Sé que SIL es un silencio."],
    [
        "En una conversación musical, una persona hace una pregunta y otra responde. La pregunta es una frase corta de 4 pulsos, y la respuesta también dura 4 pulsos. Se toca sobre un pulso parejo, sin apuro.",
        f"Una respuesta puede ser un eco, que es igual a la pregunta, o una respuesta nueva, que mantiene algo pero cambia otra cosa. Por ejemplo, si la pregunta es {P(*PREG)}, una respuesta nueva podría ser {P(TA, TA, TT, SIL)}. Las dos tienen 4 pulsos. La pregunta deja una idea esperando y la respuesta la contesta.",
        "Improvisar es inventar en el momento. Para hacerlo sin miedo, escucha la pregunta completa, cuenta el pulso y responde con un patrón de 4 pulsos. No hay respuestas «malas» si respetas el pulso y la duración. Solo prueba otra vez.",
    ],
    [("pregunta", "frase musical que deja algo esperando"), ("respuesta", "frase que contesta a la pregunta"), ("eco", "respuesta igual a la pregunta"), ("improvisar", "inventar en el momento"), ("turno", "momento en que le toca tocar a cada persona")],
    [
        ("Medir una respuesta", f"La pregunta es {P(*PREG)}. Un niño responde {P(TA, SIL, TT, TA)}. ¿La respuesta mide lo mismo?", [f"La pregunta tiene {len(PREG)} pulsos.", "La respuesta tiene TA, SIL, ti-ti, TA: 4 pulsos.", "Ambas miden 4 pulsos."], "Sí, 4 pulsos"),
        ("Reconocer un eco", f"Pregunta: {P(*PREG)}. Respuesta: {P(*PREG)}. ¿Es un eco o una respuesta nueva?", ["Comparo símbolo por símbolo.", "Todos coinciden."], "Es un eco"),
    ],
    [
        ("Responder con un patrón de más pulsos que la pregunta.", "La conversación pierde el pulso.", "Cuenta 4 pulsos y deja de tocar."),
        ("Responder antes de que termine la pregunta.", "No se escuchó a la otra persona.", "Espera el final y responde en tu turno."),
    ],
    [
        ex("En una conversación musical, ¿quién toca primero: la pregunta o la respuesta?", "La pregunta", "La respuesta contesta a la pregunta."),
        ex("Una respuesta que repite igual la pregunta se llama...", "Eco", "Eco significa repetir igual."),
        ex("¿Cuántos pulsos dura la pregunta en esta clase?", "4", "La pregunta y la respuesta duran 4 pulsos cada una."),
    ],
    [
        ex(f"Pregunta: {P(*PREG)}. Respuesta: {P(TA, TA, SIL, TA)}. ¿La respuesta es un eco o respuesta nueva?", "Respuesta nueva", "Hay símbolos distintos."),
        ex(f"¿Cuántos sonidos tiene la pregunta {P(*PREG)}?", str(sounds(*PREG)), "1 + 2 + 1 + 0 = 4."),
        ex("Si respondes con 6 pulsos a una pregunta de 4, ¿es correcto?", "No, debe medir 4 pulsos", "La respuesta mide lo mismo que la pregunta."),
    ],
    [
        ex(f"Pregunta: {P(TA, TT, SIL, TA)}. Escribe una respuesta de 4 pulsos con exactamente 2 sonidos.", "Por ejemplo: " + P(TA, SIL, TA, SIL), "Dos TA y dos SIL dan 4 pulsos y 2 sonidos."),
        arith("Se turnan 3 veces: pregunta de 4 pulsos y respuesta de 4 pulsos. ¿Cuántos pulsos hay en total?", "(4+4)*3", "Cada turno completo dura 8 pulsos y son 3 turnos.", " pulsos"),
        ex(f"Pregunta: {P(TA, TA, TA, TA)}. Una respuesta es {P(TA, TA, TA, SIL)}. ¿En qué pulso cambia?", "En el pulso 4", "Los tres primeros son iguales y el cuarto cambia de TA a SIL."),
    ],
    [
        ex("Una niña toca una respuesta distinta cada vez a la misma pregunta. ¿Hace mal por no repetir?", "No; las respuestas pueden variar si mantienen 4 pulsos", "Improvisar permite respuestas distintas."),
        ex("Un niño dice «mi respuesta fue mala porque no sonó como la pregunta». ¿Qué le dices?", "Que una respuesta nueva no tiene por qué sonar igual; solo debe respetar el pulso y la duración", "Una respuesta puede ser distinta sin ser incorrecta."),
    ],
    [
        ex(f"Pregunta: {P(TA, TT, TA, SIL)}. Inventa una respuesta que mantenga el último símbolo (SIL) pero cambie los otros tres.", "Por ejemplo: " + P(TT, TA, TT, SIL), "Termina igual en SIL, y los otros tres símbolos son diferentes a TA, ti-ti, TA."),
        ex("Pregunta y respuesta suman 8 pulsos. Se repiten hasta llegar a 32 pulsos. ¿Cuántas vueltas completas son?", "4", "32 ÷ 8 = 4."),
    ],
    [ex("Dos amigos conversan con palmas. Uno toca 4 pulsos y el otro los repite igual. ¿Qué tipo de respuesta es?", "Un eco", "Repetir igual es un eco.")],
    [ex("¿Cuántos pulsos dura una respuesta?", "4", "Igual que la pregunta."), ex("¿Qué es un eco?", "Una respuesta igual a la pregunta", "Repite sin cambiar."), ex("¿Qué haces mientras el otro toca?", "Escucho en silencio", "Escuchar permite responder bien.")],
    (
        f"Con un compañero de casa o con tus dos manos (mano izquierda pregunta, mano derecha responde), haz una conversación de 3 turnos. La primera pregunta es {P(*PREG)}. Inventa tus propias preguntas y respuestas de 4 pulsos para los otros dos turnos. Escribe con símbolos los 3 turnos y marca cuáles respuestas son eco.",
        f"Turno 1: pregunta {P(*PREG)}, respuesta {P(*PREG)} (eco). Turno 2: pregunta {P(TA, TA, TT, SIL)}, respuesta {P(TA, SIL, TA, TA)}. Turno 3: pregunta {P(TT, TT, TA, SIL)}, respuesta {P(TA, TA, TA, SIL)}.",
        ["cada pregunta y respuesta mide 4 pulsos", "hace 3 turnos con pulso parejo", "marca cuáles respuestas son eco"],
        ["interpretación", "turnos escritos con símbolos", "marca de ecos"],
        ["responder con más o menos de 4 pulsos", "interrumpir"],
        "Reconoce el pulso estable y pregunta qué cambió entre pregunta y respuesta; si hay eco, pide una variante.",
    ),
    "Toca una pregunta de 4 pulsos y pide a alguien que responda con 4 pulsos.",
    "Cambia solo la intensidad de la respuesta y explica cómo suena distinto.",
)

# ---------------------------------------------------------------- OA 05 · clase 3
RULE = "Regla: la creación debe tener 8 pulsos, al menos un SIL y terminar con SIL"
CAND = {
    "X": (TA, TT, TA, SIL, TA, TA, TT, SIL),
    "Y": (TA, TA, TA, TA, TT, TT, TA, TA),
    "Z": (TA, SIL, TA, SIL, TA, SIL, TA),
    "W": (TT, TA, SIL, TA, TT, TA, TA, SIL),
}


def cumple(p):
    return len(p) == 8 and SIL in p and p[-1] == SIL


CAND_TXT = " ".join(f"{k}: {P(*v)}." for k, v in CAND.items())
OK = ", ".join(k for k, v in CAND.items() if cumple(v))
L(
    OA5, 3,
    f"Lápiz, papel y tus palmas o un tarro con cucharas. Leyenda: {LEY}. {RULE}. Creaciones de trabajo: {CAND_TXT}",
    "Aprenderé a crear música siguiendo una regla: usar un límite me ayuda a inventar. Sirve para improvisar con orden y revisar si cumplí.",
    ["Sé contar pulsos y sonidos.", "Sé tocar un patrón con silencios."],
    [
        "Cuando improvisas, a veces es difícil empezar. Una regla ayuda: es un límite que te guía. Por ejemplo: «8 pulsos y terminar con silencio». También puedes usar reglas como «solo sonidos suaves» o «un sonido largo al principio». Con una regla, tu idea tiene forma.",
        f"Para saber si cumpliste una regla, revisas una por una sus partes. Con la regla «{RULE[7:]}», miras: ¿tiene 8 pulsos?, ¿hay al menos un SIL?, ¿el último símbolo es SIL? Si una parte falla, la creación no cumple y se corrige.",
        "Crear con una regla no quita libertad: da un camino. Dentro de la regla puedes elegir muchos sonidos, silencios y fuerza. Al terminar, toca tu creación dos veces, revisa la regla y cuenta tus pulsos.",
    ],
    [("regla", "límite que guía la creación"), ("crear", "inventar algo nuevo"), ("cumplir", "hacer lo que pide la regla"), ("revisar", "comprobar que se cumple cada parte"), ("creación", "música que inventas")],
    [
        ("Revisar una creación", f"{RULE}. Creación X: {P(*CAND['X'])}. ¿Cumple?", ["Cuento los pulsos: son 8.", "Hay un SIL en el pulso 4 y en el 8.", "El último símbolo es SIL."], "Sí, cumple"),
        ("Encontrar la falla", f"{RULE}. Creación Z: {P(*CAND['Z'])}. ¿Cumple?", ["Cuento los pulsos: son 7.", "La regla pide 8."], "No; tiene 7 pulsos en vez de 8 (y además termina en TA)"),
    ],
    [
        ("Revisar solo una parte de la regla.", "Una creación puede fallar en otra parte.", "Revisa todas las partes, una por una."),
        ("Decir que la regla quita la libertad de crear.", "La regla da un camino para inventar.", "Elige sonidos y fuerza dentro de la regla."),
    ],
    [
        ex("Una regla, ¿limita o guía tu creación?", "La guía", "Es un límite que ayuda a empezar."),
        ex(f"{RULE}. ¿Cuántos pulsos debe tener la creación?", "8", "Es la primera parte de la regla."),
        ex(f"{RULE}. ¿Con qué símbolo debe terminar?", "SIL", "Debe terminar con un silencio."),
    ],
    [
        ex(f"{RULE}. Creación Y: {P(*CAND['Y'])}. ¿Cumple? ¿Qué falla?", "No cumple; no tiene ningún SIL y no termina en silencio", "Faltan dos partes de la regla."),
        ex(f"{RULE}. Creación W: {P(*CAND['W'])}. ¿Cumple?", "Sí", "Tiene 8 pulsos, un SIL en el pulso 3 y termina con SIL."),
        ex(f"Cuenta los sonidos de la creación X: {P(*CAND['X'])}.", str(sounds(*CAND['X'])), "1 + 2 + 1 + 0 + 1 + 1 + 2 + 0 = 8."),
    ],
    [
        ex(f"{CAND_TXT} {RULE}. ¿Cuáles cumplen?", OK, "Se revisan las cuatro creaciones con las tres partes de la regla."),
        ex(f"Escribe una creación nueva que cumpla la regla: 8 pulsos, un SIL al menos y SIL al final. Usa solo TA y SIL.", "Por ejemplo: " + P(TA, TA, SIL, TA, TA, TA, SIL, SIL), "Sirve cualquiera con 8 símbolos de TA y SIL, al menos un SIL y SIL al final."),
        ex("Una niña dice «mi creación tiene 8 pulsos, así que cumple». ¿Qué le falta revisar?", "Si hay al menos un SIL y si termina en SIL", "La regla tiene tres partes."),
    ],
    [
        ex("Ana dice: «Con la regla ya no puedo inventar». ¿Qué le dices?", "Que dentro de la regla puede elegir muchos sonidos y silencios", "La regla guía y deja elegir."),
        ex(f"La creación X: {P(*CAND['X'])} se toca dos veces. ¿Cuántos pulsos suenan?", "16", "8 pulsos por vuelta, 2 vueltas."),
    ],
    [
        ex(f"Cambia un solo símbolo de {P(*CAND['Y'])} para que cumpla la regla. ¿Qué cambias?", "El último TA por SIL", "Así queda con 8 pulsos, un SIL y termina con SIL."),
        ex("Inventa otra regla corta que sirva para crear en 4 pulsos.", "Por ejemplo: «4 pulsos, un ti-ti y un silencio»", "Cualquier regla clara que se pueda comprobar sirve."),
    ],
    [arith("Quieres crear 3 piezas de 8 pulsos cada una con la misma regla. ¿Cuántos pulsos crearás en total?", "8*3", "Cada pieza dura 8 pulsos y son 3.", " pulsos")],
    [ex("¿Qué hace una regla en una creación?", "La guía", "Da un camino para inventar."), ex("¿Cuántas partes tiene la regla de hoy?", "Tres", "8 pulsos, al menos un SIL y SIL final."), ex("Si una parte falla, ¿qué haces?", "Corregir la creación", "Debe cumplir todas las partes.")],
    (
        f"Crea una pieza de 8 pulsos con la regla: al menos un SIL y terminar con SIL. Usa TA, ti-ti y SIL. Escríbela con los símbolos, tócala dos veces y revisa tus tres partes de la regla. Si quieres, agrega una segunda regla propia (por ejemplo, «solo sonidos suaves»).",
        f"Mi pieza: {P(TA, TT, SIL, TA, TA, TT, TA, SIL)}. Tiene 8 pulsos, hay SIL en el pulso 3 y termina en SIL.",
        ["cumple las tres partes de la regla", "la escribe con símbolos", "la toca dos veces con pulso parejo"],
        ["pieza escrita", "interpretación", "revisión de la regla"],
        ["escribir 7 o 9 pulsos", "olvidar el SIL final"],
        "Reconoce la revisión de cada parte y pregunta qué sonido le gustó más; si no cumple, pide que cuente los pulsos otra vez.",
    ),
    "Crea con una regla de 4 pulsos y comparte con alguien.",
    "Inventa una regla con dos condiciones y crea una pieza para ella.",
)

# ---------------------------------------------------------------- OA 05 · clase 4
INT = {
    "1": (TA, TT, TA, SIL),
    "2": (TA, TA, TT, SIL),
    "3": (TA, TT, SIL, TA),
    "4": (TA, TA, TA, SIL),
}
CRIT = "Criterios: (a) 4 pulsos; (b) al menos un ti-ti; (c) un SIL"
INT_TXT = " ".join(f"Intento {k}: {P(*v)}." for k, v in INT.items())
L(
    OA5, 4,
    f"Lápiz, papel y tus palmas. Leyenda: {LEY}. {CRIT}. Intentos de trabajo: {INT_TXT}",
    "Aprenderé a elegir la mejor de mis ideas musicales y a recordarla escribiéndola, repitiéndola y poniéndole nombre. Sirve para guardar lo que invento y volver a tocarlo igual.",
    ["Sé tocar un patrón de 4 pulsos.", "Sé escribirlo con símbolos."],
    [
        "Cuando improvisas, se te ocurren muchas ideas. Para guardar la mejor, primero elige con criterios: puedes revisar si tiene la cantidad de pulsos pedida, si usa un ti-ti y si lleva un silencio. Elegir con criterios es más justo que elegir al azar.",
        "Para recordarla, tienes tres ayudas. Escríbela con símbolos, por ejemplo TA – ti-ti – TA – SIL. Repítela tres veces seguidas. Y ponle un nombre fácil, como «gotas rápidas». Así, otro día puedes volver a tocar lo mismo.",
        "Al terminar, toca tu idea elegida dos veces y compara con lo escrito. Si hay una diferencia, corrígela. Una buena idea musical es la que puedes volver a tocar igual y decir por qué la elegiste.",
    ],
    [("seleccionar", "elegir con criterios"), ("recordar", "poder volver a tocar lo mismo"), ("criterio", "regla para elegir"), ("registro", "idea escrita para no olvidarla"), ("nombre", "palabra que ayuda a recordar una idea")],
    [
        ("Elegir con criterios", f"{CRIT}. {INT_TXT} ¿Qué intentos cumplen los tres criterios?", ["Revisa cada intento: pulsos, ti-ti y SIL.", "El 1 tiene 4 pulsos, un ti-ti y un SIL.", "El 2 y el 3 también.", "El 4 tiene 4 pulsos y un SIL, pero ningún ti-ti."], "Cumplen el 1, el 2 y el 3; el 4 no tiene ti-ti"),
        ("Escribir una idea para recordarla", "Tocaste: un sonido, dos sonidos rápidos, un sonido y un silencio. Escríbelo con símbolos.", ["Un sonido es TA.", "Dos sonidos rápidos en un pulso son ti-ti.", "Silencio es SIL."], P(TA, TT, TA, SIL)),
    ],
    [
        ("Elegir solo porque «sonó bonito» sin revisar criterios.", "No se puede comprobar.", "Revisa los criterios antes de decidir."),
        ("Escribir la idea de memoria sin tocarla después.", "Pueden quedar diferencias.", "Toca de nuevo y compara."),
    ],
    [
        ex("Para recordar una idea musical, ¿la escribes o la olvidas?", "La escribo", "Escribir ayuda a volver a tocarla igual."),
        ex("Elegir con criterios, ¿es más justo que elegir al azar?", "Sí", "Los criterios se pueden comprobar."),
        ex("¿Qué ayuda a recordar una idea: ponerle un nombre o no decirle a nadie?", "Ponerle un nombre", "Un nombre sencillo ayuda a la memoria."),
    ],
    [
        ex(f"{CRIT}. Intento 1: {P(*INT['1'])}. ¿Cuántos pulsos tiene?", "4", "Hay 4 símbolos."),
        ex(f"Escribe con símbolos: un sonido, un silencio, dos sonidos rápidos y un sonido.", P(TA, SIL, TT, TA), "TA, SIL, ti-ti, TA en el orden pedido."),
        ex("Repetir tu idea tres veces seguidas, ¿ayuda a recordarla?", "Sí", "Repetir fija la secuencia en la memoria."),
    ],
    [
        ex(f"{INT_TXT} ¿Qué intentos tienen el SIL en el último pulso?", "Los intentos 1, 2 y 4", "Esos terminan con SIL; el 3 termina con TA."),
        ex(f"{INT_TXT} Compara el intento 1 y el intento 4. ¿Cuál tiene más sonidos y cuántos?", f"El intento 1, con {sounds(*INT['1'])} sonidos (el 4 tiene {sounds(*INT['4'])})", "El intento 1 suma 1 + 2 + 1 + 0 = 4; el 4 suma 1 + 1 + 1 + 0 = 3."),
        ex("Tienes un patrón de 4 pulsos con nombre «gotas rápidas». Lo vuelves a tocar una semana después usando solo el nombre y el papel. ¿Qué te ayudó: el papel o el nombre?", "Ambos: el papel guardó los símbolos y el nombre recordó la idea", "Escribir y nombrar son dos ayudas de la memoria."),
    ],
    [
        ex("Leo dice: «Elegí el intento 3 porque sí». ¿Qué mejora su decisión?", "Revisar los criterios y decir cuáles cumple", "Una elección con criterios se puede justificar."),
        ex("Una niña escribió su idea, pero al tocarla no suena igual. ¿Qué debe hacer?", "Comparar lo escrito con lo que tocó y corregir", "El registro debe coincidir con la interpretación."),
    ],
    [
        ex(f"Escribe cómo registrarías tu mejor idea: nombre, símbolos y por qué la elegiste. Usa el intento 2 ({P(*INT['2'])}).", "Por ejemplo: «Paso rápido», " + P(*INT['2']) + ", porque tiene 4 pulsos, un ti-ti y un silencio", "El registro incluye nombre, símbolos y razón."),
        arith("Practicas tu idea 5 veces seguidas. Cada vuelta tiene 4 pulsos. ¿Cuántos pulsos tocas en total?", "4*5", "Cinco vueltas de cuatro pulsos.", " pulsos"),
    ],
    [ex("Improvisaste cinco ideas distintas y quieres guardar solo una. ¿Cómo eliges?", "Reviso criterios como cantidad de pulsos y presencia de silencio, y elijo la que cumple y me gusta", "Se combina criterio y gusto.")],
    [ex("¿Qué ayuda a recordar una idea?", "Escribirla, repetirla y ponerle un nombre", "Son las tres ayudas."), ex("En Música: ¿Qué es un criterio?", "Una regla para elegir", "Permite decidir con razones."), ex("¿Cuántos pulsos tiene una idea de 4 símbolos?", "4", "Un símbolo por pulso.")],
    (
        f"Improvisa tres ideas de 4 pulsos con palmas o un objeto seguro. Escríbelas con símbolos. Usa {CRIT} para elegir la mejor. Ponle un nombre fácil, tócala tres veces seguidas y escribe cómo la elegiste. Si quieres, toma las de ejemplo ({INT_TXT}) para practicar.",
        f"Idea elegida: «gotas rápidas», {P(*INT['1'])}. Cumple los tres criterios y la repetí tres veces.",
        ["escribe tres ideas con símbolos", "elige una usando los criterios", "la toca tres veces y le pone nombre"],
        ["tres ideas escritas", "selección con criterios", "interpretación repetida"],
        ["elegir sin revisar criterios", "no repetir la idea para recordarla"],
        "Reconoce el uso de criterios; pregunta qué ayuda de memoria usó.",
    ),
    "Escribe una idea de 4 pulsos y tócala hoy y mañana.",
    "Elige entre dos ideas con una tabla de criterios y cuéntale a alguien por qué.",
)

# ---------------------------------------------------------------- OA 06 · clase 1
L(
    OA6, 1,
    "Lápiz, papel y colores. Ideas de trabajo para comunicar: (a) «La lluvia empieza suave y se vuelve fuerte»; (b) «Una fiesta alegre»; (c) «Una noche tranquila». Elementos posibles: pulso lento o rápido, sonidos fuertes o suaves, ti-ti rápidos, silencios.",
    "Aprenderé a elegir qué quiero comunicar con mi trabajo musical y a decidir qué sonidos lo muestran. Sirve para presentar mi música a mi curso y a mi comunidad con una idea clara.",
    ["Sé crear un patrón de 4 pulsos.", "Sé describir una música con evidencia."],
    [
        "Presentar es mostrar a otras personas tu trabajo musical. Antes de presentar, decide qué quieres comunicar: una idea, una emoción o una historia corta. Por ejemplo: «la lluvia que empieza suave y se vuelve fuerte». Con esa idea clara, eliges los sonidos.",
        "Los elementos musicales te ayudan a comunicar. Un pulso lento y sonidos suaves dan calma. Un pulso rápido, sonidos fuertes y muchos ti-ti dan energía. Los silencios pueden mostrar espera o sorpresa. Elige pocos elementos y úsalos con intención.",
        "Puedes presentar solo o en grupo. Si es individual, tú decides todo. Si es grupal, conversan y se ponen de acuerdo para que todos entiendan la misma idea. En ambos casos, piensa también en la comunidad que te va a escuchar: tu curso, tu familia o tu escuela.",
    ],
    [("comunicar", "hacer que otros entiendan una idea"), ("presentar", "mostrar un trabajo a otras personas"), ("individual", "una sola persona"), ("grupal", "varias personas juntas"), ("comunidad", "personas con quienes compartimos, como el curso o la familia")],
    [
        ("Elegir elementos", "Quieres comunicar «la lluvia empieza suave y se vuelve fuerte». ¿Cómo cambia la intensidad?", ["Empieza suave.", "Termina fuerte.", "Entonces la intensidad va de suave a fuerte."], "De suave a fuerte"),
        ("Individual o grupal", "Dos amigas quieren presentar juntas. ¿Su presentación es individual o grupal?", ["Hay dos personas.", "Presentan juntas."], "Grupal"),
    ],
    [
        ("Presentar sin decidir qué comunicar.", "La audiencia no entiende qué quiere mostrar.", "Elige una idea y úsala para elegir los sonidos."),
        ("Usar muchos elementos a la vez.", "Se confunde el mensaje.", "Elige pocos elementos y úsalos con intención."),
    ],
    [
        ex("Presentar un trabajo musical, ¿es mostrarlo a otras personas o guardarlo en un cajón?", "Mostrarlo a otras personas", "Presentar significa compartir."),
        ex("Dos amigas presentan juntas. ¿Es una presentación individual o grupal?", "Grupal", "Participan varias personas."),
        ex("«Una noche tranquila», ¿pide pulso lento o rápido?", "Lento", "La calma combina con un pulso lento."),
    ],
    [
        ex("Quieres comunicar «una fiesta alegre». ¿Qué eliges: sonidos suaves y lentos o sonidos rápidos y fuertes?", "Sonidos rápidos y fuertes", "Rápido y fuerte da energía alegre."),
        ex("Un silencio antes del final, ¿puede mostrar sorpresa?", "Sí", "El silencio crea expectativa."),
        ex("¿A quiénes puede presentar su trabajo un estudiante: al curso y a la familia?", "Sí, a ambos", "El curso y la familia forman parte de la comunidad."),
    ],
    [
        ex("Lara quiere comunicar la idea «una noche tranquila» y usa golpes fuertes y rápidos. ¿Su elección combina? ¿Por qué?", "No; lo tranquilo pide sonidos suaves y lentos", "Los elementos deben coincidir con la idea."),
        ex("Elige la idea más clara: (a) «muchas cosas» (b) «la lluvia que empieza suave y se hace fuerte».", "b", "Describe qué sucede y cómo cambia."),
        arith("Un grupo planea 3 secciones de 8 pulsos cada una. ¿Cuántos pulsos dura la presentación?", "8*3", "Tres secciones de 8 pulsos.", " pulsos"),
    ],
    [
        ex("Tomás dice: «Prefiero presentar solo porque en grupo no me escuchan». ¿Qué se puede acordar en el grupo?", "Un acuerdo de turnos y roles para que todos se escuchen", "El acuerdo ayuda a que todos participen."),
        ex("Si tu idea es «la lluvia que se vuelve fuerte», ¿en qué parte de la presentación va el sonido más fuerte: al inicio o al final?", "Al final", "La lluvia aumenta poco a poco."),
    ],
    [
        ex("Quieres comunicar la idea (a). Escribe tres decisiones: pulso, intensidad y un elemento más.", "Por ejemplo: pulso medio, suave que va a fuerte, ti-ti rápidos al final", "Las decisiones muestran el cambio de la lluvia."),
        ex("Si una presentación tiene 3 secciones y quieres un silencio de 2 pulsos entre ellas, ¿cuántos pulsos de silencio hay?", "4", "Hay 2 espacios entre 3 secciones: 2 × 2 = 4."),
    ],
    [ex("En la fiesta de fin de año del curso, un grupo quiere presentar una pieza. ¿Qué deben decidir primero?", "Qué idea quieren comunicar", "Con la idea clara eligen los sonidos.")],
    [ex("¿Qué decides antes de presentar?", "Qué quiero comunicar", "Es la base de la presentación."), ex("¿Puedes presentar en grupo?", "Sí", "Presentar puede ser individual o grupal."), ex("Menciona un elemento musical.", "Por ejemplo: pulso", "Pulso, intensidad y silencio son elementos.")],
    (
        "Elige una de estas tres ideas: (a) la lluvia que empieza suave y se vuelve fuerte, (b) una fiesta alegre, (c) una noche tranquila. Escribe tres decisiones musicales que la muestren (pulso, intensidad y un elemento más). Prueba con tus palmas o un objeto seguro y cuéntale a alguien qué quisiste comunicar.",
        "Idea (a). Pulso medio, intensidad de suave a fuerte, y ti-ti al final. Quise que se sintiera la lluvia aumentando.",
        ["elige una idea de las tres", "escribe tres decisiones musicales", "las prueba y explica qué quiso comunicar"],
        ["decisiones escritas", "demostración", "explicación oral"],
        ["usar elementos que no combinan con la idea", "no explicar el mensaje"],
        "Reconoce la idea clara; pregunta qué elemento fue más importante para mostrarla.",
    ),
    "Cuéntale a alguien de tu casa una idea musical en una frase.",
    "Cambia una decisión y explica cómo cambia el mensaje.",
)

# ---------------------------------------------------------------- OA 06 · clase 2
FR = "ya sue-na la mú-si-ca"
L(
    OA6, 2,
    f"Lápiz, papel y reloj o temporizador. {SILABAS} Frase de trabajo: «{FR}». Ensayo de ejemplo de 20 minutos con tres momentos.",
    "Aprenderé a ensayar con propósito: decidir qué voy a mejorar y trabajar en eso. Sirve para presentar mejor sin cansarme ni repetir sin pensar.",
    ["Sé tocar o cantar una frase corta.", "Sé contar pulsos."],
    [
        "Ensayar con propósito es practicar para mejorar algo concreto. Antes de empezar, decide una meta, por ejemplo «entrar juntos» o «mantener el pulso». Después, divide el tiempo en momentos. Un ensayo de 20 minutos puede tener tres: 5 minutos para calentar la voz y el cuerpo, 10 para repetir la parte difícil y 5 para hacer toda la pieza.",
        f"Repetir sin pensar no sirve. Es mejor repetir una parte difícil de manera lenta, revisar qué pasó y volver a intentar. Con la frase «{FR}», que tiene {S(FR)} sílabas, puedes practicar una palma por sílaba. Si la repites 4 veces, das {S(FR)*4} palmas.",
        "Al terminar el ensayo, di una cosa que mejoró y una que falta mejorar. Un ensayo corto y claro cuida tu voz y tu energía. Si algo duele o te cansa, haz una pausa y toma agua.",
    ],
    [("ensayar", "practicar para mejorar"), ("meta", "lo que quiero lograr en el ensayo"), ("calentar", "preparar la voz y el cuerpo"), ("parte difícil", "sección que cuesta más"), ("pausa", "descanso corto")],
    [
        ("Repartir el tiempo", "Un ensayo dura 20 minutos: 5 de calentamiento, 10 para repetir y el resto para tocar toda la pieza. ¿Cuántos minutos son para la pieza completa?", ["Se suman 5 y 10: 15.", "20 − 15 = 5."], "5 minutos"),
        ("Contar palmas", f"Das una palma por sílaba en «{FR}». ¿Cuántas palmas das si la repites 4 veces?", [f"Una vuelta tiene {S(FR)} sílabas.", f"{S(FR)} × 4 = {S(FR)*4}."], f"{S(FR)*4} palmas"),
    ],
    [
        ("Repetir toda la pieza sin pensar.", "No mejora la parte difícil.", "Elige la parte difícil y repítela lento."),
        ("Ensayar sin pausas hasta cansarse.", "Se cuida mal la voz y el cuerpo.", "Haz pausas cortas y toma agua."),
    ],
    [
        ex("Ensayar con propósito, ¿es repetir sin pensar o mejorar algo concreto?", "Mejorar algo concreto", "El propósito guía el ensayo."),
        ex("¿Qué haces primero en un ensayo: calentar o terminar la pieza?", "Calentar", "Primero se prepara la voz y el cuerpo."),
        ex("Si te cansas, ¿haces una pausa o sigues sin descanso?", "Hago una pausa", "Cuidar tu voz y energía es parte del ensayo."),
    ],
    [
        ex(f"Cuenta las sílabas de «{FR}».", str(S(FR)), "Ya, sue, na, la, mú, si, ca."),
        ex("Un ensayo tiene 5 minutos de calentamiento y 10 de repetir. ¿Cuántos minutos van hasta ahora?", "15", "5 + 10 = 15."),
        ex("«Entrar juntos» ¿es una meta para un ensayo o un adorno?", "Una meta", "Es algo concreto que se puede lograr."),
    ],
    [
        arith(f"Repites la frase «{FR}» 3 veces con una palma por sílaba. ¿Cuántas palmas das?", f"{S(FR)}*3", "Cada vuelta tiene 7 palmas y son 3 vueltas.", " palmas"),
        ex("Quieres repetir una parte difícil de 8 pulsos cinco veces. ¿Cuántos pulsos tocas?", "40", "8 × 5 = 40 pulsos."),
        ex("Ordena el ensayo: (a) hacer toda la pieza, (b) calentar, (c) repetir la parte difícil.", "b, c, a", "Primero se calienta, luego se trabaja lo difícil y al final se toca todo."),
    ],
    [
        ex("Una niña ensayó 15 minutos repitiendo solo lo fácil. ¿Qué podría mejorar?", "Dedicar tiempo a la parte difícil", "Mejorar exige trabajar en lo que cuesta."),
        ex("Un niño dice «ensayé mucho» pero no sabe qué mejoró. ¿Qué le falta?", "Una meta y una revisión al final", "Sin meta no se sabe si mejoró."),
    ],
    [
        ex("Un ensayo de 20 minutos se divide así: 5 de calentamiento, 10 de repetir y el resto de pieza completa. ¿Cuántos ensayos de ese tipo caben en 60 minutos?", "3", "60 ÷ 20 = 3."),
        ex("Quieres elegir una meta para mañana que se pueda comprobar. ¿Cuál sirve: «tocar mejor» o «entrar juntos en el pulso 5»?", "Entrar juntos en el pulso 5", "Se puede observar si ocurrió."),
    ],
    [ex("Tu grupo tiene 20 minutos para ensayar antes de presentar. ¿Cómo reparten el tiempo con los tres momentos?", "5 de calentar, 10 de repetir lo difícil y 5 para la pieza completa", "Es un reparto equilibrado de 20 minutos.")],
    [ex("¿Qué es una meta de ensayo?", "Lo que quiero lograr", "Guía qué practicas."), ex("¿Cuál es la parte que repites más?", "La parte difícil", "Ahí se necesita más práctica."), ex("¿Qué haces si tu voz se cansa?", "Hago una pausa", "Cuidar la voz es parte del ensayo.")],
    (
        f"Planifica un ensayo de 20 minutos con tres momentos y una meta concreta (por ejemplo «entrar juntos»). Usa la frase «{FR}»: practica con una palma por sílaba y repítela 4 veces en la parte «difícil». Anota la meta, el reparto del tiempo y qué mejoró.",
        f"Meta: entrar juntos. 5 min calentar, 10 min repetir {FR}, 5 min pieza completa. Di {S(FR)*4} palmas en las 4 repeticiones. Mejoró la entrada; falta cuidar el final.",
        ["escribe una meta concreta", "reparte el tiempo en 3 momentos que suman 20", "anota qué mejoró y qué falta"],
        ["plan escrito", "ensayo", "revisión final"],
        ["repetir sin una meta", "olvidar las pausas"],
        "Reconoce el plan y pregunta cómo supo que había mejorado; si no hay meta, ayuda a precisarla.",
    ),
    "Practica una parte difícil 3 veces despacio.",
    "Diseña un ensayo de 30 minutos con cuatro momentos.",
)

# ---------------------------------------------------------------- OA 06 · clase 3
ROLES = "Roles posibles: voz, percusión corporal, instrumento, director, presentador y cuidador del tiempo"
L(
    OA6, 3,
    f"Lápiz y papel. {ROLES}. Grupo de trabajo ficticio de 6 estudiantes: Ana, Beto, Carla, Diego, Eva y Fito.",
    "Aprenderé a repartir roles de manera equitativa en un grupo para que todos participen. Sirve para presentar sin que alguien quede fuera ni cargue con todo.",
    ["Sé trabajar en grupo.", "Sé escuchar a otros."],
    [
        "En una presentación grupal, cada persona tiene un rol: puede cantar, tocar un instrumento, hacer percusión corporal, dirigir con señales, presentar la pieza o cuidar el tiempo. Un grupo de 6 personas puede repartir 6 roles, uno por persona.",
        "Un reparto equitativo es justo. Quiere decir que todos tienen un rol importante, que nadie hace todo y que nadie queda sin hacer nada. También se pueden rotar los roles entre varias piezas, para que todos prueben distintas tareas. No importa que algunos roles se vean más; todos son necesarios.",
        "Para decidir, el grupo conversa, escucha y llega a un acuerdo. Si alguien no quiere un rol, se busca otro. Si hay más roles que personas, algunas personas pueden tener dos roles. Si hay menos roles que personas, se agrega un rol de apoyo.",
    ],
    [("rol", "tarea que le toca a cada persona"), ("equitativo", "justo; con partes parecidas para todos"), ("rotar", "cambiar de rol por turnos"), ("acuerdo", "decisión que todos aceptan"), ("apoyo", "ayuda a quien lo necesita")],
    [
        ("Un rol por persona", f"{ROLES}. Hay 6 estudiantes y 6 roles. ¿Cuántos estudiantes quedan sin rol si cada uno recibe uno?", ["6 estudiantes, 6 roles, uno por persona.", "6 − 6 = 0."], "0 estudiantes"),
        ("Rotar roles", "El grupo hará 3 piezas y quiere que todos cambien de rol en cada pieza. ¿Cuántos cambios de rol por persona?", ["Pieza 1: un rol.", "Pieza 2: otro rol.", "Pieza 3: otro rol."], "Cada persona cambia de rol 2 veces"),
    ],
    [
        ("Dejar que una sola persona haga todos los roles.", "No es justo ni equitativo.", "Reparte los roles entre todos."),
        ("Elegir el rol «más visible» para uno mismo sin conversar.", "No hubo acuerdo.", "Conversen y decidan juntos."),
    ],
    [
        ex("Cuando todos tienen un rol justo, el reparto es...", "Equitativo", "Equitativo significa justo."),
        ex("Un grupo de 4 estudiantes y 4 roles. ¿Cuántos estudiantes quedan sin rol si cada uno recibe uno?", "0", "4 − 4 = 0."),
        ex("Si cambias de rol entre piezas, ¿rotas o repites?", "Roto", "Rotar es cambiar por turnos."),
    ],
    [
        ex("Ana es la directora, Beto toca el instrumento y Carla canta. ¿Cuántos roles se repartieron?", "3", "Hay tres personas con tres roles."),
        ex(f"{ROLES}. Hay 5 estudiantes y 6 roles. Si cada estudiante recibe un rol, ¿cuántos roles quedan sin repartir?", "Queda 1 rol sin repartir", "6 − 5 = 1; una persona puede tener dos roles."),
        ex("Hay 7 estudiantes y 6 roles. ¿Qué puede hacer el grupo para que todos participen?", "Agregar un rol de apoyo", "Así el estudiante 7 tiene una tarea."),
    ],
    [
        ex(f"{ROLES}. En un grupo de 6, tres estudiantes ya tienen voz, instrumento y director. ¿Cuántos roles quedan por repartir entre los otros tres?", "3", "Son seis roles en total y ya se repartieron tres."),
        ex("Un grupo reparte así: Ana canta, Beto toca, Carla dirige y Diego presenta. ¿Cuántos estudiantes participan con un rol?", "4", "Cada una de las cuatro personas tiene un rol."),
        ex("Hay 6 estudiantes y 3 piezas. Si en cada pieza cambian todos de rol, ¿cuántos roles distintos prueba cada estudiante?", "3", "Uno por cada pieza."),
    ],
    [
        ex("Eva dice: «Siempre me toca cuidar el tiempo». ¿Qué puede proponer el grupo?", "Rotar los roles entre las piezas", "Rotar da a todos la oportunidad de probar."),
        ex("Un estudiante hace voz, instrumento y dirección, y otros no hacen nada. ¿Es equitativo? ¿Por qué?", "No; algunas personas cargan todo y otras no participan", "El reparto debe ser parecido para todos."),
    ],
    [
        arith("3 piezas, 6 roles distintos y 6 estudiantes. En cada pieza cada estudiante tiene un rol. ¿Cuántas asignaciones de rol hay en total?", "3*6", "En cada pieza hay 6 asignaciones, y son 3 piezas.", " asignaciones"),
        ex("Dos estudiantes quieren el mismo rol. ¿Qué es lo más justo: pelear o conversar y turnarse?", "Conversar y turnarse", "El acuerdo permite que ambos participen."),
    ],
    [ex("Un grupo de 6 se prepara para presentar a su curso. Ana quiere ser directora, Beto presentador, Carla voz, Diego instrumento, Eva percusión corporal y Fito cuidador del tiempo. ¿Está bien repartido?", "Sí; cada una de las 6 personas tiene un rol distinto", "Hay 6 personas y 6 roles diferentes.")],
    [ex("¿Qué es un reparto equitativo?", "Un reparto justo", "Todos reciben un rol importante."), ex("¿Cómo se toma una decisión de grupo?", "Conversando y escuchando", "El acuerdo requiere diálogo."), ex("¿Puede alguien tener dos roles?", "Sí, si hay más roles que personas", "Se reparten para que todo se cumpla.")],
    (
        f"Imagina un grupo de 6 (Ana, Beto, Carla, Diego, Eva y Fito) que preparará una pieza breve. Usa los roles: {ROLES}. Reparte un rol a cada persona. Después, para una segunda pieza, rota los roles para que nadie repita el mismo. Escribe ambas tablas.",
        "Pieza 1: Ana-voz, Beto-percusión, Carla-instrumento, Diego-director, Eva-presentadora, Fito-cuidador del tiempo. Pieza 2: Ana-cuidadora del tiempo, Beto-voz, Carla-percusión, Diego-instrumento, Eva-directora, Fito-presentador.",
        ["asigna un rol distinto a cada persona", "rota los roles en la segunda pieza sin repetir", "escribe ambas tablas con los seis roles"],
        ["dos tablas escritas", "explicación oral del acuerdo"],
        ["repetir roles en la segunda pieza", "dejar a alguien sin rol"],
        "Reconoce el reparto justo y pregunta cómo se pusieron de acuerdo; si hay repeticiones, pide corregirlas.",
    ),
    "Conversa con alguien de tu casa cómo se reparten tareas de manera justa.",
    "Diseña un reparto de roles para un grupo de 8 personas.",
)

# ---------------------------------------------------------------- OA 06 · clase 4
PAUTA = "Pauta de observación: (1) empezaron juntos; (2) mantuvieron el pulso; (3) terminaron juntos"
L(
    OA6, 4,
    f"Lápiz, papel y una pauta de observación. {PAUTA}. Cada criterio se marca con una cruz si se logró. Público ficticio de 12 personas.",
    "Aprenderé a presentar una pieza musical con acuerdos de escucha y a recoger evidencia de cómo resultó. Sirve para mejorar la próxima presentación.",
    ["Sé tocar una pieza breve.", "Sé escuchar en silencio."],
    [
        "Antes de presentar, el grupo acuerda cómo escuchar: silencio mientras suena la música, aplauso al final y atención a quien presenta. El público también tiene un rol. Si vienen familiares o personas de la comunidad, se les invita con respeto. No se graba ni se fotografía a niños sin permiso de un adulto responsable.",
        f"Para saber cómo resultó, recoges evidencia: algo observable. Una pauta con tres criterios ayuda: empezaron juntos, mantuvieron el pulso y terminaron juntos. Cada criterio se marca con una cruz si se logró. Eso se llama pauta de observación.",
        "Las personas del público pueden comentar con la forma «dos estrellas y un deseo»: dos cosas que salieron bien y un deseo para mejorar. Se habla de lo que se oyó, con respeto. Después, el grupo cuenta las cruces y decide qué mejorar.",
    ],
    [("presentación", "momento en que se muestra el trabajo"), ("evidencia", "algo observable que muestra cómo salió"), ("pauta", "lista de criterios para observar"), ("dos estrellas y un deseo", "dos cosas buenas y una por mejorar"), ("acuerdo de escucha", "reglas para escuchar con respeto")],
    [
        ("Contar cruces", f"{PAUTA}. En una presentación se logró el criterio 1 y el criterio 2, pero no el 3. ¿Cuántas cruces hay?", ["Se logró el 1.", "Se logró el 2.", "No se logró el 3."], "2 cruces"),
        ("Leer un comentario", "Un compañero dice: «Me gustó que empezaron juntos y mantuvieron el pulso; quiero que terminen juntos». ¿Cuántas estrellas y cuántos deseos dio?", ["Primero dos cosas buenas: empezar juntos y mantener el pulso.", "Después un deseo: terminar juntos."], "2 estrellas y 1 deseo"),
    ],
    [
        ("Filmar o fotografiar a otros niños sin permiso.", "Se pasa por alto su privacidad.", "Pide permiso a un adulto responsable."),
        ("Comentar diciendo solo «estuvo mal».", "No ayuda a mejorar.", "Di dos cosas buenas y un deseo."),
    ],
    [
        ex("En una presentación, el público escucha en silencio y aplaude al final. ¿Eso es un acuerdo de escucha?", "Sí", "Son reglas para escuchar con respeto."),
        ex("«Dos estrellas y un deseo» son dos cosas buenas y una por mejorar. ¿Verdadero o falso?", "Verdadero", "Eso significa la frase."),
        ex("¿Se puede fotografiar a otros niños sin permiso de un adulto?", "No", "Hay que respetar su privacidad."),
    ],
    [
        ex(f"{PAUTA}. Un grupo logró los tres criterios. ¿Cuántas cruces tiene?", "3", "Uno por cada criterio logrado."),
        ex("Un comentario dice: «Estuvo bonito». ¿Es un comentario con evidencia?", "No", "No dice qué se oyó."),
        ex("Un comentario dice: «Empezaron juntos en el pulso 1». ¿Tiene evidencia?", "Sí", "Dice algo observable."),
    ],
    [
        ex("En una presentación observan 4 grupos. Cada grupo logra 2 criterios. ¿Cuántas cruces hay en total?", "8", "4 × 2 = 8."),
        arith("De 12 personas del público, 9 dicen que el grupo empezó juntos. ¿Cuántas no lo dijeron?", "12-9", "Se restan los 9 del total.", " personas"),
        ex("Una pauta tiene 3 criterios y un grupo logró 2. Escribe cuál puede ser el deseo para mejorar.", "Por ejemplo: terminar juntos", "El deseo se refiere al criterio no logrado."),
    ],
    [
        ex("Un grupo dice: «no hace falta pauta, nos sentimos bien». ¿Qué ventaja da la pauta?", "Muestra evidencia observable de lo logrado", "La pauta permite comprobar lo que se hizo."),
        ex("Un familiar dice que quiere grabar con su celular a todo el curso. ¿Qué debe hacer primero?", "Pedir permiso a los adultos responsables de los niños", "La imagen de los niños requiere permiso."),
    ],
    [
        ex("Un grupo recibió estos comentarios: A «empezaron juntos», B «mantuvieron el pulso», C «terminaron distinto». ¿Cuál criterio hay que mejorar?", "Terminar juntos", "El comentario C señala el criterio no logrado."),
        ex("Un grupo repitió su presentación y subió de 1 cruz a 3. ¿Cuántas cruces ganó?", "2", "3 − 1 = 2."),
    ],
    [ex("Tu curso invita a las familias a una muestra musical. Las personas llegan y quieren entrar a escuchar durante la pieza. ¿Qué acuerdo de escucha ayuda?", "Entrar en silencio entre piezas y escuchar sin interrumpir", "El acuerdo cuida a quienes presentan.")],
    [ex("¿Qué es una pauta de observación?", "Una lista de criterios para observar", "Permite recoger evidencia."), ex("¿Qué dice «dos estrellas y un deseo»?", "Dos cosas buenas y una por mejorar", "Es una manera respetuosa de comentar."), ex("¿Cuántas cruces tiene un grupo que logró los 3 criterios?", "3", "Una por criterio.")],
    (
        f"Presenta una pieza breve a alguien de tu casa. La pieza dura 16 pulsos: 8 palmas suaves (parte A) y luego 8 palmas fuertes (parte B). Pide a una persona que use la pauta: {PAUTA}. Escribe cuántas cruces tuviste y un comentario con «dos estrellas y un deseo». No grabes ni compartas imágenes de otras personas sin permiso.",
        "Tuve 3 cruces: empecé en el pulso 1, mantuve el pulso y terminé en el pulso 16. Dos estrellas: pulso parejo y cambio claro entre suave y fuerte. Un deseo: tocar más fuerte en B.",
        ["presenta la pieza con acuerdos de escucha", "recoge evidencia con la pauta", "escribe dos estrellas y un deseo"],
        ["presentación", "pauta con cruces", "comentario escrito"],
        ["comentar sin evidencia", "grabar sin permiso"],
        "Reconoce la presentación y pregunta qué criterio quiere mejorar; si falta evidencia, pide un ejemplo observable.",
    ),
    "Pide a alguien de tu casa que te cuente una cosa buena y un deseo de tu presentación.",
    "Crea tu propia pauta con tres criterios observables.",
)

# ---------------------------------------------------------------- OA 07 · clase 1
MAPA = "Mapa sonoro (ficticio): Cocina: olla, refrigerador, voces. Patio: pájaros, viento, pelota que bota. Calle: bocina, auto, perro que ladra."
L(
    OA7, 1,
    f"Lápiz y papel. {MAPA} No se necesita grabar ni salir; si quieres, escucha tu propio espacio en silencio por un minuto.",
    "Aprenderé a identificar y describir los sonidos de mis espacios cotidianos. Sirve para notar cuántos sonidos hay a mi alrededor y qué los produce.",
    ["Sé escuchar en silencio.", "Sé describir un sonido con dos cualidades."],
    [
        "Estamos rodeados de sonidos. Un mapa sonoro anota qué sonidos se escuchan en cada lugar, como la cocina, el patio o la calle. Cada sonido tiene una fuente: puede ser natural, como el viento o los pájaros; humana, como una voz o unos pasos; de máquina, como un refrigerador o un auto; o de objetos, como una olla o una pelota que bota.",
        f"Podemos describir cada sonido con sus cualidades: ¿es fuerte o suave?, ¿largo o corto?, ¿agudo o grave? Así, el ladrido de un perro suele sonar fuerte y corto. En el mapa de ejemplo, la cocina tiene olla, refrigerador y voces; el patio, pájaros, viento y una pelota que bota; la calle, bocina, auto y un perro que ladra. Cada lugar tiene tres sonidos.",
        "Para hacer un buen mapa, escucha unos segundos en silencio, anota lo que oyes y clasifícalo. No hay que salir a lugares peligrosos: se puede hacer desde la casa o el patio. Escucha sin tapar tus oídos con auriculares.",
    ],
    [("mapa sonoro", "dibujo o lista de sonidos de un lugar"), ("fuente", "lo que produce un sonido"), ("natural", "sonido de la naturaleza"), ("humano", "sonido hecho por personas"), ("máquina", "sonido hecho por un aparato"), ("objeto", "sonido de algo que golpea o se mueve, como una olla o una pelota")],
    [
        ("Contar sonidos", f"{MAPA} ¿Cuántos sonidos hay en total en el mapa?", ["Cocina tiene 3.", "Patio tiene 3.", "Calle tiene 3.", "3 + 3 + 3 = 9."], "9 sonidos"),
        ("Clasificar por fuente", "El viento, ¿es natural, humano o de máquina?", ["El viento no lo produce una persona ni un aparato.", "Es parte de la naturaleza."], "Natural"),
    ],
    [
        ("Anotar solo sonidos fuertes.", "Se pierden sonidos suaves que también están.", "Escucha en silencio y anota también los suaves."),
        ("Poner auriculares para escuchar mejor el entorno.", "Los auriculares tapan los sonidos de alrededor.", "Escucha sin auriculares."),
    ],
    [
        ex("Un mapa sonoro anota los sonidos de un lugar. ¿Verdadero o falso?", "Verdadero", "Eso es un mapa sonoro."),
        ex("El canto de un pájaro, ¿es natural o de máquina?", "Natural", "Lo hace un animal."),
        ex("Una voz, ¿es humana o natural? Elige la mejor.", "Humana", "La produce una persona."),
    ],
    [
        ex(f"{MAPA} ¿Cuántos sonidos tiene el patio?", "3", "Pájaros, viento y pelota que bota."),
        ex(f"{MAPA} ¿Qué sonidos de la calle son de máquina?", "La bocina y el auto", "Son aparatos; el perro es un animal."),
        ex("El refrigerador suena suave y por mucho rato. ¿Es largo o corto?", "Largo", "Dura mucho tiempo."),
    ],
    [
        ex(f"{MAPA} Clasifica los 9 sonidos: ¿cuántos son de la naturaleza?", "3", "Pájaros, viento y perro; el perro es animal, parte de la naturaleza."),
        ex("Describe el ladrido de un perro con dos cualidades: intensidad y duración.", "Fuerte y corto", "Suele sonar fuerte y breve."),
        arith("Escuchas 1 minuto en cada uno de 3 lugares. ¿Cuántos minutos escuchas?", "1*3", "Un minuto por lugar, tres lugares.", " minutos"),
    ],
    [
        ex("Una niña dice: «En mi casa no hay sonidos porque está en silencio». ¿Qué le dices?", "Que si escucha atenta, siempre hay sonidos suaves", "El silencio total casi no existe."),
        ex("Un niño anota solo «ruido» para todos. ¿Qué le falta?", "Nombrar la fuente y describir el sonido", "Un mapa detalla fuente y cualidades."),
    ],
    [
        ex("Quieres un mapa de 4 lugares con 3 sonidos cada uno. ¿Cuántos sonidos anotas?", "12", "4 × 3 = 12."),
        ex("En tu mapa, 5 sonidos son naturales y 2 son de máquina. ¿Cuántos sonidos hay en total?", "7", "5 + 2 = 7."),
    ],
    [ex("Estás en el patio de la escuela en silencio y oyes: voces de niños, un auto lejano, el viento. ¿Cuántas fuentes hay y de qué tipo son?", "3 fuentes: humana, de máquina y natural", "Cada sonido viene de una fuente distinta.")],
    [ex("¿Qué es un mapa sonoro?", "Una lista o dibujo de los sonidos de un lugar", "Anota lo que se escucha."), ex("¿De qué tipo es el viento?", "Natural", "Lo produce la naturaleza."), ex("¿Cuántas cualidades usas para describir un sonido?", "Cuatro", "Altura, timbre, intensidad y duración.")],
    (
        "Haz un mapa sonoro de un lugar de tu casa o patio. Escucha un minuto en silencio. Anota al menos tres sonidos, di de qué tipo son (natural, humano, de máquina o de objeto) y descríbelos con dos cualidades. Si no puedes escuchar, usa el mapa de ejemplo y elige un lugar.",
        "Patio: pájaros (natural, agudo y corto), viento (natural, suave y largo) y pelota que bota (objeto, fuerte y corto).",
        ["anota al menos tres sonidos", "clasifica su fuente", "describe cada uno con dos cualidades"],
        ["mapa sonoro escrito o dibujado", "explicación oral"],
        ["anotar solo ruidos fuertes", "no nombrar la fuente"],
        "Reconoce los sonidos suaves anotados y pregunta cuál le sorprendió.",
    ),
    "Escucha un minuto en tu pieza y anota tres sonidos.",
    "Compara tu mapa con el de ejemplo y cuenta cuántos sonidos nuevos descubriste.",
)

# ---------------------------------------------------------------- OA 07 · clase 2
L(
    OA7, 2,
    "Lápiz y papel. Funciones de la música: arrullar (dormir), marchar (caminar juntos), celebrar (una fiesta), jugar (ronda) y trabajar (hacer una tarea con ritmo). Descripciones de ejemplo ficticias: A, lenta y suave; B, pulso firme y fuerte; C, alegre y con palmas; D, en círculo con versos rítmicos; E, repetida y pareja.",
    "Aprenderé que la música cumple funciones en la vida: dormir, caminar, celebrar, jugar y trabajar. Sirve para elegir música según el momento y entender por qué existe.",
    ["Sé describir una música con dos rasgos.", "Sé que una canción tiene una letra y un pulso."],
    [
        "La música no solo se escucha por gusto: también cumple una función. Una canción de cuna sirve para arrullar a un bebé: es lenta y suave. Una marcha ayuda a caminar juntos: tiene un pulso firme. Una música de fiesta sirve para celebrar: es alegre y se baila. Una ronda sirve para jugar en círculo.",
        "Las músicas que ayudan a trabajar suelen tener un ritmo parejo y repetido, así las tareas se hacen con más ánimo. En cada función importa un rasgo. Para dormir: lento y suave. Para marchar: pulso firme. Para celebrar: alegre y rápido. Para jugar: versos rítmicos que todos conocen.",
        "Una misma música puede cumplir varias funciones, o cambiar de función con el lugar. Lo importante es notar qué rasgos la hacen útil para ese momento. Cuando elijas música en casa, pregúntate: ¿para qué la necesito ahora?",
    ],
    [("función", "para qué sirve una música"), ("arrullar", "hacer dormir con una canción suave"), ("marcha", "música para caminar juntos"), ("celebrar", "festejar algo especial"), ("ronda", "canto y juego en círculo")],
    [
        ("Emparejar función y rasgo", "Música A: lenta y suave. ¿Para qué función sirve?", ["Lenta y suave da calma.", "Sirve para arrullar."], "Para arrullar o dormir"),
        ("Calcular una marcha", "En una marcha das un paso en cada pulso durante 16 pulsos. ¿Cuántos pasos das?", ["Un paso por pulso.", "16 pulsos son 16 pasos."], "16 pasos"),
    ],
    [
        ("Pensar que cada música sirve para una sola cosa.", "Una música puede cumplir varias funciones.", "Pregúntate para qué la necesitas en ese momento."),
        ("Usar música fuerte y rápida para dormir.", "No combina con la función.", "Elige lenta y suave para dormir."),
    ],
    [
        ex("¿Para qué sirve una canción de cuna?", "Para arrullar a un bebé", "Es lenta y suave."),
        ex("Una marcha, ¿ayuda a caminar juntos o a dormir?", "A caminar juntos", "Tiene un pulso firme."),
        ex("Una ronda se canta y se juega en... ¿círculo o fila?", "Círculo", "Así se juega la ronda."),
    ],
    [
        ex("Descripciones: A, lenta y suave; B, pulso firme y fuerte; C, alegre y con palmas. ¿Cuál es la marcha?", "B", "El pulso firme ayuda a caminar juntos."),
        ex("Descripciones: A, lenta y suave; B, pulso firme y fuerte; C, alegre y con palmas. ¿Cuál es para celebrar?", "C", "Alegre y con palmas anima la fiesta."),
        ex("Descripción D: en círculo con versos rítmicos. ¿Qué función cumple?", "Jugar", "Es una ronda."),
    ],
    [
        ex("Una canción de cuna y una marcha, ¿cuál suele sonar más suave?", "La canción de cuna", "La cuna es lenta y suave; la marcha tiene un pulso firme."),
        arith("Una marcha de 4 pasos por grupo se repite 6 veces. ¿Cuántos pasos das?", "4*6", "Cuatro pasos en cada una de las 6 vueltas.", " pasos"),
        ex("Quieres que un hermano pequeño se duerma. ¿Qué rasgos eliges: lento y suave o rápido y fuerte?", "Lento y suave", "Esos rasgos dan calma."),
    ],
    [
        ex("Ana puso música muy fuerte para que su hermanito se durmiera. ¿Funcionó? ¿Por qué?", "Probablemente no; la música fuerte no calma", "La función de dormir pide suavidad."),
        ex("¿Una misma canción puede cumplir dos funciones? Da un ejemplo.", "Sí; por ejemplo una canción alegre sirve para jugar y para celebrar", "Las funciones no son excluyentes."),
    ],
    [
        ex("Un curso marcha 24 pasos al pulso. Cada 4 pasos hay un golpe de tambor fuerte. ¿Cuántos golpes fuertes hay?", "6", "24 ÷ 4 = 6."),
        ex("Inventa una función nueva para una música y di un rasgo que la haga útil.", "Por ejemplo: música para guardar los juguetes; tiene ritmo parejo", "Una función se apoya en un rasgo audible."),
    ],
    [ex("En el cumpleaños de una amiga, ¿qué función cumple la música y qué rasgo la hace servir para eso?", "Celebrar; es alegre y se puede bailar", "La fiesta pide ánimo y movimiento.")],
    [ex("¿Qué es la función de una música?", "Para qué sirve", "Dormir, marchar, celebrar, jugar o trabajar."), ex("¿Qué rasgo tiene una canción de cuna?", "Lenta y suave", "Da calma al oyente."), ex("¿Qué rasgo tiene una marcha?", "Pulso firme", "Ayuda a caminar juntos.")],
    (
        "Piensa en cuatro momentos de tu día (despertar, jugar, comer, dormir) y elige una función de música para cada uno. Escribe qué rasgos tendría (lenta o rápida, suave o fuerte). Luego marcha 16 pasos al pulso y cuenta cuántos golpes fuertes das si haces uno cada 4 pasos.",
        "Despertar: alegre y medio rápida. Jugar: ronda con versos. Comer: suave y tranquila. Dormir: lenta y suave. En 16 pasos doy 4 golpes fuertes.",
        ["asigna una función a cada momento", "explica los rasgos de cada una", "cuenta 4 golpes fuertes en 16 pasos"],
        ["tabla escrita", "marcha", "conteo"],
        ["elegir música que no combina con el momento", "contar mal los golpes"],
        "Reconoce que los rasgos combinan con el momento; pregunta cuál función le parece más importante.",
    ),
    "Pregunta a alguien de tu casa para qué sirve una canción que conoce.",
    "Elige una música para cinco momentos de un día de campo y explica los rasgos.",
)

# ---------------------------------------------------------------- OA 07 · clase 3
L(
    OA7, 3,
    "Lápiz y papel. Se usa un ejemplo ficticio: una niña llamada Luna recuerda un sonido del patio. Reglas de privacidad: no escribir nombres completos, direcciones ni historias que no quieras compartir.",
    "Aprenderé a describir un recuerdo sonoro propio cuidando mi privacidad. Sirve para contar un sonido que me importa sin compartir más de lo que quiero.",
    ["Sé describir un sonido con cualidades.", "Sé que hay cosas que se pueden contar y otras que no."],
    [
        "Un recuerdo sonoro es un sonido que recordamos: el canto de un pájaro de tu patio, el ruido de la lluvia en el techo, una canción que se escuchaba en un momento. Puedes describirlo con sus cualidades: ¿era fuerte o suave?, ¿largo o corto?, ¿agudo o grave? ¿qué lo producía?",
        "Para compartir con seguridad, cuenta solo lo que tú quieras. No hace falta decir nombres completos, direcciones ni cosas privadas de tu familia. Puedes decir «una persona de mi familia» o «un lugar de mi casa». Si prefieres, imagina un sonido en vez de contar uno real. Nadie debe obligarte a contar un recuerdo.",
        "Una frase para empezar es: «Un sonido que recuerdo es ... Era ... y me hizo sentir ...». Por ejemplo: «Un sonido que recuerdo es la lluvia en el techo. Era suave y largo, y me hizo sentir calma». Esa frase usa dos cualidades y una emoción, sin dar datos privados.",
    ],
    [("recuerdo sonoro", "sonido que recuerdo"), ("privacidad", "lo que decido no compartir"), ("segura", "que no me pone en riesgo"), ("cualidad", "cómo suena: fuerte, suave, largo, corto..."), ("imaginar", "crear en la mente algo que no estoy viendo")],
    [
        ("Armar la frase", "Quieres contar la lluvia en el techo: suave y larga, que te dio calma. Escribe la frase.", ["Empiezo con «Un sonido que recuerdo es ...».", "Agrego «Era suave y largo».", "Termino con la emoción: calma."], "Un sonido que recuerdo es la lluvia en el techo. Era suave y largo, y me hizo sentir calma."),
        ("Cuidar la privacidad", "¿Debes escribir la dirección de tu casa en tu recuerdo sonoro?", ["La dirección es un dato privado.", "No es necesaria para describir un sonido."], "No"),
    ],
    [
        ("Contar un recuerdo que no quieres compartir.", "Nadie debe obligarte a contar algo privado.", "Cuenta solo lo que tú quieras o imagina un sonido."),
        ("Poner nombres completos y direcciones.", "Son datos privados.", "Usa «una persona de mi familia» o «un lugar de mi casa»."),
    ],
    [
        ex("Un recuerdo sonoro, ¿es un sonido que recuerdo o un dibujo que hago?", "Un sonido que recuerdo", "Es memoria de un sonido."),
        ex("Si no quieres contar un recuerdo, ¿qué puedes hacer?", "Imaginar un sonido en vez de contarlo", "Nadie debe obligarte."),
        ex("¿Se pueden decir datos privados como la dirección? Responde sí o no.", "No", "Se protege la privacidad."),
    ],
    [
        ex("Luna dice: «Un sonido que recuerdo es el canto de un pájaro. Era agudo y corto». ¿Qué cualidades usó?", "Altura (agudo) y duración (corto)", "Agudo es altura y corto es duración."),
        ex("¿Cuál frase cuida mejor la privacidad? (a) «Mi tía Rosa Pérez de la calle Larga me cantaba.» (b) «Una persona de mi familia me cantaba.»", "b", "No da nombre completo ni dirección."),
        ex("Completa: «Un sonido que recuerdo es ... Era ... y me hizo sentir ...». ¿Cuántos espacios hay para completar?", "3", "Hay tres espacios: el sonido, cómo era y la emoción."),
    ],
    [
        ex("Luna cuenta: «Un sonido que recuerdo es el viento en las hojas. Era suave y largo». ¿Cuántas cualidades usó?", "2", "Suave es intensidad y largo es duración."),
        ex("¿Qué frase es segura de compartir? (a) «Mi vecina de la casa 12 grita siempre.» (b) «Un sonido que recuerdo es la lluvia, suave y larga.»", "b", "No da datos privados ni nombra personas."),
        ex("Quieres describir el ladrido de un perro en tu recuerdo. ¿Qué cualidades agregas: fuerte o suave y corto o largo?", "Por ejemplo: fuerte y corto", "Se eligen las cualidades que recuerdas."),
    ],
    [
        ex("Pedro dice: «Mi recuerdo es triste y no quiero contarlo». ¿Qué puede hacer?", "Imaginar un sonido o elegir otro recuerdo que sí quiera compartir", "Puede proteger su privacidad."),
        ex("Una compañera cuenta un recuerdo muy privado delante del curso. ¿Qué haces con respeto?", "Escucho con atención y no se lo cuento a otros", "Se respeta la confianza."),
    ],
    [
        ex("Escribe tu recuerdo sonoro con la frase base. Usa el sonido de un timbre de casa que suena corto y agudo y que te hace sentir alegría.", "Un sonido que recuerdo es el timbre de mi casa. Era corto y agudo, y me hizo sentir alegría.", "La frase usa el modelo de tres espacios."),
        ex("Un recuerdo sonoro, ¿puede ser imaginado? Explica.", "Sí; imaginar permite compartir sin contar nada privado", "Es una forma segura de participar."),
    ],
    [ex("En el curso, la profesora pide que compartan un sonido que les guste. Un niño no se anima. ¿Cómo lo apoyas?", "Le recuerdo que puede imaginar un sonido o elegir uno general, como la lluvia", "Así participa sin contar nada privado.")],
    [ex("¿Es obligatorio contar un recuerdo?", "No", "Cada uno decide."), ex("¿Qué cualidades usas para describir?", "Fuerte o suave, largo o corto, agudo o grave", "Son las cualidades del sonido."), ex("¿Qué datos no compartes?", "Nombres completos y direcciones", "Son datos privados.")],
    (
        "Escribe una frase de recuerdo sonoro con el modelo «Un sonido que recuerdo es ... Era ... y me hizo sentir ...». Puede ser real o imaginado. Usa al menos dos cualidades (intensidad, duración o altura). No escribas nombres completos ni direcciones. Si quieres, léela a alguien de confianza.",
        "Un sonido que recuerdo es la lluvia en el techo. Era suave y largo, y me hizo sentir calma.",
        ["usa el modelo de la frase", "incluye al menos dos cualidades", "no da datos privados"],
        ["frase escrita", "lectura voluntaria"],
        ["dar nombres completos o direcciones", "sentirse obligado a contar un recuerdo"],
        "Reconoce el recuerdo; si faltan cualidades, pregunta «¿era fuerte o suave?».",
    ),
    "Imagina un sonido relajante y descríbelo con dos cualidades.",
    "Escribe tres frases con el modelo cambiando el sonido y la emoción.",
)

# ---------------------------------------------------------------- OA 07 · clase 4
PLAN = "Plan: 3 músicas de 3 minutos cada una, con una pausa de 2 minutos entre cada una"
L(
    OA7, 4,
    f"Lápiz y papel. {PLAN}. Reglas de cuidado de los oídos: volumen medio o bajo, nada de sonidos muy fuertes cerca de las orejas y pausas frecuentes.",
    "Aprenderé a cuidar mis oídos y a elegir músicas y sonidos según el momento. Sirve para escuchar sin hacerme daño y para disfrutar mejor.",
    ["Sé que algunos sonidos son muy fuertes.", "Sé nombrar funciones de la música."],
    [
        "Los oídos son delicados. Un sonido muy fuerte, o uno fuerte por mucho tiempo, puede hacer daño. Para cuidarlos: mantén el volumen medio o bajo, no pongas parlantes ni auriculares muy cerca de las orejas, aléjate de sonidos que te duelen y haz pausas. Si algo te molesta, avisa a un adulto.",
        "También se puede elegir. Si necesitas estudiar, escoge sonidos suaves o silencio. Si quieres jugar, una música alegre sirve. Si quieres dormir, algo lento y suave. Elegir bien los sonidos es una forma de cuidar tu ánimo y tu concentración.",
        f"Un buen plan de escucha mezcla músicas y pausas. Por ejemplo: «{PLAN}». En ese plan, escuchas 3 × 3 = 9 minutos de música y descansas 2 pausas de 2 minutos, es decir, 4 minutos. En total son 13 minutos.",
    ],
    [("cuidado", "protegerse del daño"), ("volumen", "qué tan fuerte suena algo"), ("pausa", "descanso entre sonidos"), ("elección", "decidir qué escuchar"), ("concentración", "poner atención a una tarea")],
    [
        ("Calcular el plan", f"{PLAN}. ¿Cuántos minutos de música hay en total?", ["Hay 3 músicas.", "Cada una dura 3 minutos.", "3 × 3 = 9."], "9 minutos"),
        ("Elegir según el momento", "Necesitas concentrarte para hacer una tarea difícil. ¿Eliges música suave o muy fuerte?", ["La música muy fuerte distrae.", "La suave ayuda a concentrarte."], "Suave (o silencio)"),
    ],
    [
        ("Subir el volumen al máximo para sentir más.", "Puede dañar los oídos.", "Mantén el volumen medio o bajo."),
        ("Ignorar un dolor de oídos.", "Puede ser señal de daño.", "Avisa a un adulto y aléjate del sonido."),
    ],
    [
        ex("¿Qué volumen es mejor para cuidar los oídos: medio o muy fuerte?", "Medio", "Un volumen medio no daña."),
        ex("Si un sonido te duele, ¿te alejas y avisas a un adulto o te quedas?", "Me alejo y aviso a un adulto", "Es la forma de cuidarte."),
        ex("¿Para dormir eliges música lenta y suave o rápida y fuerte?", "Lenta y suave", "Da calma al oyente."),
    ],
    [
        ex(f"{PLAN}. ¿Cuántas pausas hay entre 3 músicas?", "2", "Hay una pausa entre la primera y la segunda, y otra entre la segunda y la tercera."),
        ex("Quieres jugar a las rondas. ¿Eliges una música alegre o una de cuna?", "Alegre", "Combina con la función de jugar."),
        ex("Un amigo pone los auriculares muy fuertes. ¿Qué le propones?", "Bajar el volumen y hacer pausas", "Protege sus oídos."),
    ],
    [
        arith(f"{PLAN}. ¿Cuántos minutos de pausa hay en total?", "2*2", "Hay 2 pausas de 2 minutos cada una.", " minutos"),
        arith(f"{PLAN}. ¿Cuántos minutos dura todo el plan?", "3*3+2*2", "Se suman 9 minutos de música y 4 de pausa.", " minutos"),
        ex("Quieres escuchar 4 músicas de 3 minutos con una pausa de 2 minutos entre cada una. ¿Cuántos minutos son en total?", "18", "4 × 3 = 12 de música y 3 pausas de 2 minutos = 6; 12 + 6 = 18."),
    ],
    [
        ex("Leo dice: «Si subo el volumen, se escucha mejor sin riesgo». ¿Qué le respondes?", "Que un volumen muy alto puede dañar los oídos aunque se escuche mejor", "Mejor sonido no significa más seguro."),
        ex("En una fiesta, la música está tan fuerte que te duelen los oídos. ¿Qué puedes decir?", "Pedir bajar el volumen o alejarme", "Cuidar los oídos es más importante."),
    ],
    [
        ex("Un plan de escucha tiene 5 músicas de 2 minutos y 4 pausas de 1 minuto. ¿Cuántos minutos son en total?", "14", "5 × 2 = 10 y 4 × 1 = 4; 10 + 4 = 14."),
        ex("Elige la mejor opción para estudiar: (a) música muy fuerte, (b) música suave o silencio. Justifica.", "b; ayuda a concentrarse", "Lo suave no distrae."),
    ],
    [ex("Tienes una tarea de matemática y tu hermano pone música fuerte. ¿Cómo lo hablan?", "Piden bajar el volumen o usar música suave mientras estudias", "Se resuelve conversando y eligiendo sonidos adecuados.")],
    [ex("¿Qué volumen cuida mejor tus oídos?", "Medio o bajo", "Es lo más seguro."), ex("¿Qué haces si un sonido te duele?", "Me alejo y aviso a un adulto", "Es lo correcto."), ex("En Música: ¿Para qué sirven las pausas?", "Para descansar los oídos", "Evitan el cansancio.")],
    (
        f"Diseña tu plan de escucha: {PLAN}. Cámbialo a tu gusto (por ejemplo, otras duraciones) y calcula el tiempo total. Escribe qué funciones pides a cada música (por ejemplo: calma, jugar, concentrarte) y tres reglas para cuidar tus oídos.",
        "Plan: 3 músicas de 3 minutos con 2 pausas de 2 minutos = 13 minutos. Música 1: calma. Música 2: jugar. Música 3: concentrarme. Reglas: volumen medio, pausas y aviso a un adulto si algo duele.",
        ["calcula el tiempo total correctamente", "asigna una función a cada música", "escribe tres reglas de cuidado"],
        ["plan escrito", "cálculo", "reglas"],
        ["olvidar las pausas en el cálculo", "poner volumen alto como regla"],
        "Reconoce el plan y verifica el cálculo; pregunta qué regla de cuidado es más importante para él o ella.",
    ),
    "Baja el volumen de un parlante y comprueba si se oye bien igual.",
    "Diseña un plan de una hora de escucha con pausas y funciones.",
)
