"""Cuaderno del estudiante, 1.º medio Inglés (oficial), IN1M OA 04: estrategias de escucha, inferencia con apoyo y clarificación.

Las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado. Lo que el hablante hace (gestos, tono) se
describe entre paréntesis y las flechas ↗ ↘ marcan si la voz sube o baja. Los textos son originales y llevan pista en español.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN1M OA 04"
ADULT = "Un adulto lee en voz alta (tapa el guion): "
MAT_L = "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz."


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ clase 1: predecir y escuchar con un propósito
W_LOST = "Título: «At the lost-and-found office». Guion: «Excuse me, I lost my umbrella yesterday. It is green with white dots. I think I left it on bus number twelve.» (lost-and-found = objetos perdidos, umbrella = paraguas, dots = lunares, left = dejé)"
W_TRIP = "Título: «Plan for the school trip». Guion: «Hello, class. We will visit the planetarium on Friday. The bus leaves at nine. Please bring five thousand pesos for the ticket.» (planetarium = planetario, leaves = sale, ticket = entrada)"
CAFE = "Título: «Student Café menu». Guion: «Welcome to the Student Café. Today's special is vegetable soup with bread, three thousand five hundred pesos. Dessert is free if you bring your own spoon.» (special = plato del día, vegetable = de verduras, dessert = postre, free = gratis, spoon = cuchara)"
MUSEUM = "Título: «Tomorrow's aquarium visit». Guion: «Hi, everybody. Tomorrow we are going to the aquarium. Please bring a notebook, a pencil and lunch. We leave at eight o'clock sharp. Don't forget your permission note.» (aquarium = acuario, notebook = cuaderno, sharp = en punto, forget = olvides, permission note = autorización firmada)"
SCORES = "Título: «Sports results». Guion: «Here are the results. The red team won with twenty-one points. The blue team scored eighteen. The green team came third with fifteen points.» (results = resultados, won = ganó, scored = anotó, came third = quedó tercero)"
CONTEST = "Título: «School contest». Guion: «Next week, our class will have a recycling contest. Every group collects paper, plastic and cans. The group with the most weight wins a trip to the botanical garden. The contest starts on Monday and ends on Friday.» (contest = concurso, recycling = reciclaje, cans = latas, weight = peso, wins = gana, botanical garden = jardín botánico, ends = termina)"

lesson(
    OA, 1, MAT_L,
    "Aprenderé a predecir de qué hablará un texto y a escuchar con un propósito claro, usando lo que ya sé. Sirve para entender más y para saber qué dato buscar.",
    ["Sé reconocer el formato y el tema de un texto oral.", "Conozco palabras como title, price y time."],
    [
        "Predecir (to predict) es imaginar de qué hablará un texto antes de escucharlo, usando el título, el formato o una imagen. Si el título es Student Café menu, esperas palabras como soup, price y dessert. Usar conocimientos previos (prior knowledge) significa recordar lo que ya sabes del tema: en una cafetería hay precios, platos y horarios.",
        "Escuchar con un propósito (listening for a purpose) significa decidir qué buscas antes de escuchar. Si el propósito es saber cuánto cuesta, atiendes los números y la palabra pesos. Si es saber cuándo, atiendes horas y días. Un propósito claro evita que te pierdas en lo que no necesitas.",
        "Después de escuchar, confirma tu predicción (confirm your prediction): ¿lo que oíste coincide con lo que esperabas? Si no coincide, corrígela. Predecir no es adivinar sin base: es una hipótesis que se prueba. Anota dos o tres palabras esperadas antes de escuchar y marca las que aparecen.",
    ],
    [("predict", "predecir: imaginar qué dirá el texto"), ("prior knowledge", "conocimientos previos"), ("purpose for listening", "propósito de escucha: qué busco"), ("confirm", "confirmar: comprobar si era cierto"), ("title", "título"), ("special", "plato del día")],
    [
        ("Predecir con el título", W_LOST.split(". Guion")[0] + ". ¿Qué palabras esperas oír? A) lost, color, bus B) recipe, oven, flour", ["El título habla de objetos perdidos.", "En ese lugar se describe lo perdido y dónde se perdió.", "Las palabras esperables son lost, color y bus."], "A) lost, color, bus"),
        ("Escuchar con un propósito", ADULT + W_TRIP + " Escuchas para saber cuánto dinero llevar. ¿Qué dato buscas?", ["El propósito es saber un monto.", "Busco un número junto a pesos.", "Dice five thousand pesos."], "5.000 pesos"),
    ],
    [
        ("Predecir sin ninguna base y no revisar después.", "Se imagina algo sin mirar el título ni el formato y no se compara con lo que se oye.", "Usa el título y confirma cada predicción al terminar."),
        ("Escuchar todo con la misma atención aunque se busque un dato.", "No se decidió el propósito antes de escuchar.", "Define qué dato buscas y atiéndelo."),
    ],
    [
        ("Título: «A day at the beach». ¿Qué palabras esperas oír? A) sand, waves, sunscreen B) keyboard, printer, screen", "A) sand, waves, sunscreen", "Son palabras del tema playa: arena, olas y bloqueador."),
        ("Vas a escuchar un menú. ¿En qué debes fijarte si quieres saber cuánto gastarás? A) números y precios B) colores y formas", "A) números y precios", "El propósito es el costo."),
        ("Antes de escuchar el menú de la cafetería, ¿qué pregunta te ayuda a escuchar con propósito? A) ¿Cuánto cuesta el plato del día? B) ¿Quién ganó el partido?", "A) ¿Cuánto cuesta el plato del día?", "Es una pregunta relacionada con el título del texto."),
    ],
    [
        (ADULT + CAFE + " ¿Cuánto cuesta el plato del día? A) 3.500 pesos B) 5.300 pesos", "A) 3.500 pesos", "Dice three thousand five hundred pesos."),
        (ADULT + CAFE + " ¿Cuándo el postre es gratis? A) si llevas tu propia cuchara B) si pides sopa", "A) si llevas tu propia cuchara", "Dice Dessert is free if you bring your own spoon."),
        (ADULT + MUSEUM + " ¿Qué se debe llevar? A) cuaderno, lápiz y almuerzo B) bloqueador y gorro", "A) cuaderno, lápiz y almuerzo", "Dice Please bring a notebook, a pencil and lunch."),
    ],
    [
        (ADULT + MUSEUM + " ¿A qué hora salen? A) a las ocho en punto B) a las diez", "A) a las ocho en punto", "Dice eight o'clock sharp."),
        arith(ADULT + SCORES + " ¿Cuántos puntos de diferencia hay entre el equipo rojo y el azul?", "21-18", "El rojo tiene 21 y el azul 18.", " puntos"),
        (ADULT + SCORES + " ¿Qué equipo quedó tercero? A) el verde B) el azul", "A) el verde", "Dice The green team came third."),
    ],
    [
        ("Predijiste para «Winter clothes sale» las palabras discounts, jackets y scarves. Oyes: «Everything is half price this weekend: coats, gloves and scarves.» (half price = mitad de precio, coats = abrigos, gloves = guantes). ¿Se confirma tu predicción? A) sí, en lo central: ofertas de ropa de invierno B) no, habla de ropa de verano", "A) sí, en lo central: ofertas de ropa de invierno", "Half price equivale a discounts y coats, gloves y scarves son ropa de invierno."),
        ("Sabes que en una biblioteca se pide silencio. ¿Qué frase esperas oír de la bibliotecaria? A) Please speak quietly. B) Please sing louder.", "A) Please speak quietly.", "Tus conocimientos previos de una biblioteca anticipan esa norma."),
    ],
    [
        (ADULT + CONTEST + " ¿Qué grupo gana el viaje? A) el que reúne más peso B) el que termina primero", "A) el que reúne más peso", "Dice The group with the most weight wins."),
        (ADULT + CONTEST + " ¿Cuántos días dura el concurso, contando lunes y viernes? A) 5 B) 4", "A) 5", "Lunes, martes, miércoles, jueves y viernes son cinco días."),
    ],
    [(ADULT + "Estás en la estación y oyes: «Passengers for Valdivia, your bus leaves from platform four at ten past nine.» (passengers = pasajeros, platform = andén, ten past nine = nueve y diez). Tu propósito es saber la hora de salida. ¿A qué hora sale? A) 9:10 B) 10:09", "A) 9:10", "Ten past nine significa nueve y diez.")],
    [
        ("En Inglés de 1.º medio (OA 4, clase 1): ¿qué es predecir antes de escuchar?", "Imaginar de qué hablará el texto usando el título, el formato o una imagen", "Es una hipótesis que se confirma después."),
        ("En Inglés de 1.º medio (OA 4, clase 1): ¿qué es escuchar con un propósito?", "Decidir qué dato buscas antes de escuchar", "Así atiendes lo que necesitas."),
        ("En Inglés de 1.º medio (OA 4, clase 1): ¿qué haces después de escuchar con tu predicción?", "La confirmas o la corriges", "Se compara con lo que se oyó."),
    ],
    task("Mira este título: «Problem at the bus stop». Escribe tres palabras que esperas oír. Luego un adulto lee: «Excuse me, the bus is late again. We have waited for twenty minutes. Let's call the bus company.» (late = atrasado, waited = esperamos, minutes = minutos, bus company = empresa de buses). Marca cuáles de tus palabras aparecieron y corrige las que no.", "Predije: bus, late, wait. Aparecieron bus y late, y waited. Corrijo: escribí wait y el texto dice waited, es el pasado de wait.", ["anota tres palabras coherentes con el título", "marca las que aparecen", "corrige una predicción si no coincide"], ["hoja con predicción y confirmación", "nota del adulto"], ["predecir palabras sin relación con el título", "no revisar después de escuchar"], "Reconoce las predicciones acertadas y pide corregir una: ¿qué dato nuevo te dio el texto?"),
    "Antes de leer un afiche o un aviso, anota tres palabras que esperas ver y luego márcalas.",
    "Elige un texto que oirás hoy (noticias o un video) y escribe una predicción y un propósito de escucha antes de empezar.",
)

# ------------------------------------------------------------------ clase 2: inferencia con claves contextuales y fonológicas
W_WAITER = "«(A waiter holds a menu and smiles.) Waiter: Are you ready to order? Customer: Yes, I'd like the fish, please.» (waiter = garzón, menu = carta, order = pedir, fish = pescado)"
W_SHIRT = "«Maria: Did you buy the green T-shirt? Pablo: No, I bought the BLUE one.» (la palabra con mayúsculas se dice con más fuerza)"
COURT = "«(Two people carry rackets and sports bags.) Lena: The court is free now. Ready? Marco: Let's go!» (rackets = raquetas, sports bags = bolsos deportivos, court = cancha, free = libre)"
PARTY = "«Luis: You are coming to the party ↗? Ana: Yes, I am ↘.» (↗ = la voz sube al final, ↘ = la voz baja al final; party = fiesta)"
PASTA = "«Dad: Mum said you wanted pizza. Teo: No, I wanted PASTA.» (la palabra con mayúsculas se dice con más fuerza; wanted = quería)"
TIRED = "«Beto: I didn't say she was late. I said she was TIRED.» (la palabra con mayúsculas se dice con más fuerza; late = atrasada, tired = cansada)"
PRESENT = "Frase 1: «Can you preSENT the results to the class?» Frase 2: «I have a PREsent for you.» (la sílaba con mayúsculas se dice con más fuerza; present = presentar o regalo, results = resultados)"
RIBS = "«(The speaker wears a white coat and points to a skeleton model.) Teacher: These are the ribs. They protect the lungs.» (white coat = delantal blanco, skeleton = esqueleto, ribs = costillas, protect = protegen, lungs = pulmones)"
TEST = "«Great, another test on Monday.» (la voz es baja y lenta, y la persona suspira; test = prueba)"

lesson(
    OA, 2, MAT_L,
    "Aprenderé a hacer inferencias al escuchar, usando el tema, los participantes, el apoyo visual y pistas del sonido como la entonación y el acento. Sirve para entender lo que no se dice con palabras.",
    ["Sé escuchar con un propósito.", "Conozco las preguntas who, where y why."],
    [
        "Hacer una inferencia (inference) es deducir algo que el texto no dice con claridad, usando pistas. Las pistas contextuales (context clues) son el tema, quiénes hablan (los participantes) y lo que se ve, como un gesto o un objeto. Si un garzón sostiene una carta y pregunta Are you ready to order?, puedes inferir que están en un restaurante aunque no lo digan.",
        "Las pistas fonológicas (phonological clues) vienen del sonido. La entonación (intonation) es cómo sube o baja la voz: si sube al final, suele ser una pregunta o una duda (You are coming ↗?); si baja, suele ser una afirmación o una respuesta (Yes, I am ↘). El acento (stress) es la palabra o sílaba que se dice con más fuerza. En No, I bought the BLUE one, el acento en BLUE muestra un contraste con otra cosa.",
        "El acento también cambia el significado de palabras: present con fuerza en la primera sílaba (PREsent) es un regalo; con fuerza en la segunda (preSENT) es presentar. El tono de voz comunica sentimientos: una voz baja y lenta puede mostrar cansancio o molestia. Para inferir, junta dos o tres pistas y comprueba que no contradigan el texto.",
    ],
    [("inference", "inferencia: deducir con pistas"), ("context clue", "pista del contexto"), ("intonation", "entonación: cómo sube o baja la voz"), ("stress", "acento: lo que se dice con más fuerza"), ("participants", "participantes: quienes hablan"), ("tone", "tono de voz")],
    [
        ("Inferir el lugar", ADULT + W_WAITER + " ¿Dónde ocurre la escena?", ["Hay una persona con una carta y un cliente.", "Se pregunta si están listos para pedir.", "Eso ocurre en un restaurante."], "En un restaurante"),
        ("Inferir por el acento", ADULT + W_SHIRT + " ¿Qué muestra el acento en BLUE?", ["Maria pregunta por la polera verde.", "Pablo responde con acento en BLUE.", "El acento marca un contraste: no verde, azul."], "Que compró la azul, no la verde"),
    ],
    [
        ("Pensar que si la voz sube siempre se enoja.", "Se interpreta la entonación como un sentimiento y no como una pregunta o duda.", "Revisa si la frase es pregunta y qué dice el contexto."),
        ("Ignorar las pistas visuales cuando se infiere.", "Se atiende solo a las palabras.", "Revisa gestos y objetos descritos entre paréntesis."),
    ],
    [
        (ADULT + COURT + " ¿Dónde están? A) en un recinto deportivo B) en una biblioteca", "A) en un recinto deportivo", "Llevan raquetas y bolsos y hablan de una cancha libre."),
        (ADULT + PARTY + " ¿Qué función tiene la voz que sube en la pregunta de Luis? A) pide confirmar algo B) da una orden", "A) pide confirmar algo", "La entonación ascendente marca una pregunta de confirmación."),
        (ADULT + PASTA + " ¿Qué palabra tiene acento? A) PASTA B) wanted", "A) PASTA", "Se dice con más fuerza para contrastar con pizza."),
    ],
    [
        (ADULT + PASTA + " ¿Qué quería realmente Teo? A) pasta B) pizza", "A) pasta", "El acento en PASTA corrige lo que dijo su mamá."),
        (ADULT + TIRED + " ¿Qué dijo Beto de ella? A) que estaba cansada, no atrasada B) que llegó tarde", "A) que estaba cansada, no atrasada", "El acento en TIRED corrige late."),
        (ADULT + RIBS + " ¿Qué clase es? A) una clase de ciencias del cuerpo humano B) una clase de música", "A) una clase de ciencias del cuerpo humano", "Hay delantal blanco, un esqueleto y costillas."),
    ],
    [
        (ADULT + PRESENT + " ¿En qué frase present significa regalo? A) en la frase 2, porque la fuerza está en la primera sílaba B) en la frase 1, porque la fuerza está en la segunda sílaba", "A) en la frase 2, porque la fuerza está en la primera sílaba", "PREsent con fuerza inicial es el sustantivo regalo."),
        (ADULT + TEST + " ¿Cómo se siente la persona? A) molesta o cansada de otra prueba B) feliz por la prueba", "A) molesta o cansada de otra prueba", "La voz baja y el suspiro contradicen las palabras Great."),
        (ADULT + PARTY + " ¿Qué contesta Ana con la voz que baja? A) confirma que va B) duda de ir", "A) confirma que va", "Yes, I am ↘ es una respuesta firme."),
    ],
    [
        (ADULT + PASTA + " Un oyente entendió que Teo no quería comer nada. ¿Qué pista de acento lo corrige? A) el acento en PASTA muestra lo que sí quería B) la voz sube al final", "A) el acento en PASTA muestra lo que sí quería", "El acento marca la alternativa que sí quería."),
        (ADULT + RIBS + " ¿Qué pista visual apoya que habla sobre el cuerpo humano? A) el modelo de esqueleto B) el delantal blanco solamente", "A) el modelo de esqueleto", "Un esqueleto se relaciona con costillas y pulmones; un delantal solo no define el tema."),
    ],
    [
        (ADULT + "«Teacher: Good job, Tom ↗?» (La profesora levanta las cejas.) (good job = buen trabajo, eyebrows = cejas). ¿Qué puedes inferir? A) que muestra duda o sorpresa B) que lo felicita sin dudas", "A) que muestra duda o sorpresa", "La voz que sube y las cejas levantadas indican duda; una felicitación firme baja la voz."),
        (ADULT + "«(A woman looks at the sky and takes out an umbrella.) Woman: Hmm... it looks dark.» (sky = cielo, takes out = saca, umbrella = paraguas, dark = oscuro). ¿Qué puedes inferir? A) que cree que va a llover B) que hará calor", "A) que cree que va a llover", "El cielo oscuro y el paraguas son pistas de lluvia."),
    ],
    [(ADULT + "«(A boy looks at his phone, then at the clock, and runs.) Boy: Oh no, the bus!» (looks at = mira, clock = reloj, runs = corre). ¿Qué puedes inferir? A) que se le hace tarde para tomar el bus B) que tiene mucho tiempo", "A) que se le hace tarde para tomar el bus", "Mira el reloj, corre y menciona el bus.")],
    [
        ("En Inglés de 1.º medio (OA 4, clase 2): ¿qué es una inferencia?", "Deducir algo que no se dice con claridad usando pistas", "Se apoya en el contexto y en el sonido."),
        ("En Inglés de 1.º medio (OA 4, clase 2): ¿qué suele indicar la entonación que sube al final?", "Una pregunta o una duda", "Marca que se pide confirmación o información."),
        ("En Inglés de 1.º medio (OA 4, clase 2): ¿qué muestra una palabra dicha con más fuerza?", "Lo importante o un contraste", "El acento resalta la idea clave."),
    ],
    task("Un adulto lee dos veces este mensaje, diciendo la palabra en mayúsculas con más fuerza: «I didn't ask for tea. I asked for COFFEE.» (asked for = pedí). Escribe qué quería realmente la persona, qué pista del sonido lo muestra y una pregunta con la voz que sube, por ejemplo Are you coming ↗?", "Quería café. La pista es el acento en COFFEE, que contrasta con tea. Pregunta: Are you ready ↗?", ["dice qué quería la persona", "nombra la pista de acento", "escribe una pregunta e indica que la voz sube"], ["hoja con tres respuestas", "nota del adulto"], ["no relacionar el acento con un contraste", "decir que la voz baja en una pregunta de confirmación"], "Reconoce la inferencia correcta y repasa con ella la regla: acento = contraste, voz que sube = pregunta."),
    "Lee en voz alta «I didn't say she was late» cambiando el acento en cada palabra y anota cómo cambia el sentido.",
    "Mira una escena de un video sin sonido y escribe tres inferencias apoyadas en lo que se ve.",
)

# ------------------------------------------------------------------ clase 3: frases clave y apoyo del hablante
W_LIB = "«(The speaker points to the left.) The post office is over there. (She points to the right.) And the pharmacy is over there.» (points to = señala, left = izquierda, right = derecha, post office = correo, pharmacy = farmacia)"
W_ARR = "«The most important thing is to arrive early. For example, the bus leaves at seven thirty.» (arrive early = llegar temprano, for example = por ejemplo)"
RULES = "«First of all, thank you for coming. The most important rule is to keep the room tidy. For example, put your bags under the table. In conclusion, if we all help, we will finish quickly.» (rule = regla, tidy = ordenada, bags = mochilas, in conclusion = en conclusión, finish = terminar)"
STOPS = "«(The guide holds up three fingers.) We have three stops today: the tower, the fountain and the park.» (guide = guía, holds up = levanta, fingers = dedos, stops = paradas, tower = torre, fountain = fuente)"
FOLDER = "«(The speaker shakes her head and points to the blue folder.) No, not that one. This one, the blue one.» (shakes her head = mueve la cabeza, folder = carpeta, blue = azul)"
RECIPE = "«The recipe is simple. In other words, you only need three ingredients.» (recipe = receta, in other words = en otras palabras, ingredients = ingredientes)"
WON = "«(The speaker jumps and smiles.) We won! We really won!» (jumps = salta, smiles = sonríe, won = ganamos)"
DIR = "«(The speaker points to the left, then straight ahead.) Turn left at the corner, then go straight for two blocks.» (corner = esquina, straight = derecho, blocks = cuadras)"

lesson(
    OA, 3, MAT_L,
    "Aprenderé a reconocer frases clave que anuncian ideas importantes y a usar los gestos y el tono del hablante como apoyo. Sirve para entender qué es lo principal sin entender cada palabra.",
    ["Sé hacer inferencias con pistas.", "Conozco frases como for example y first."],
    [
        "Algunas frases clave (key phrases) anuncian el tipo de idea que viene. First of all abre la presentación. The most important thing is... anuncia la idea principal. For example introduce un ejemplo. In other words reformula con palabras más simples. In conclusion cierra el texto. Si las reconoces, puedes seguir la estructura aunque haya palabras desconocidas.",
        "El hablante también ayuda con apoyos (supports): gestos, miradas y objetos. Señalar con la mano indica lugar (over there). Mostrar tres dedos indica una cantidad. Mover la cabeza de lado a lado suele ser no. Saltar y sonreír muestra alegría. Cuando un gesto y una palabra coinciden, la información es más fuerte; si no coinciden, hay una pista de que el hablante bromea o duda.",
        "La entonación también ayuda: una voz más fuerte y aguda marca emoción, y una voz que baja al final marca que la idea terminó. Para usar estos apoyos, enfoca la atención en las frases clave y observa el gesto en el momento exacto. Luego pregunta: ¿esta idea es principal, un ejemplo o una conclusión?",
    ],
    [("key phrase", "frase clave: anuncia un tipo de idea"), ("for example", "por ejemplo"), ("in other words", "en otras palabras"), ("in conclusion", "en conclusión"), ("gesture", "gesto: movimiento que ayuda a entender"), ("over there", "allá")],
    [
        ("Seguir un gesto", ADULT + W_LIB + " ¿Dónde está la farmacia?", ["El correo se señala hacia la izquierda.", "La farmacia se señala hacia la derecha.", "Over there, con el gesto, indica el lado."], "A la derecha"),
        ("Reconocer la idea principal", ADULT + W_ARR + " ¿Qué es lo más importante y qué es el ejemplo?", ["The most important thing anuncia la idea principal: llegar temprano.", "For example introduce un ejemplo.", "El ejemplo es la salida del bus a las 7:30."], "Lo importante es llegar temprano; el ejemplo es el bus que sale a las 7:30"),
    ],
    [
        ("Pensar que una frase con for example es la idea principal.", "Se confunde el ejemplo con la idea que ilustra.", "Busca la frase The most important... para la idea principal."),
        ("Ignorar el gesto del hablante.", "Se atiende solo a las palabras y se pierde el apoyo visual.", "Observa dónde señala o qué cuenta con los dedos."),
    ],
    [
        (ADULT + RULES + " ¿Qué frase anuncia la regla más importante? A) The most important rule B) First of all", "A) The most important rule", "Es la frase clave que presenta la idea principal."),
        (ADULT + RULES + " ¿Qué frase cierra el texto? A) In conclusion B) For example", "A) In conclusion", "In conclusion introduce la idea final."),
        (ADULT + RECIPE + " ¿Qué hace in other words? A) explica con palabras más simples B) cuenta algo del pasado", "A) explica con palabras más simples", "Reformula: la receta es simple porque solo requiere tres ingredientes."),
    ],
    [
        (ADULT + STOPS + " ¿Cuántas paradas hay? A) tres B) dos", "A) tres", "Dice three stops y levanta tres dedos."),
        (ADULT + FOLDER + " ¿Qué carpeta pide la persona? A) la azul B) la roja", "A) la azul", "Dice the blue one y la señala."),
        (ADULT + WON + " ¿Cómo se siente el hablante? A) muy contento B) enojado", "A) muy contento", "Salta, sonríe y repite We won."),
    ],
    [
        (ADULT + RULES + " ¿Qué ejemplo da para mantener ordenada la sala? A) poner las mochilas bajo la mesa B) cerrar las ventanas", "A) poner las mochilas bajo la mesa", "For example introduce ese ejemplo."),
        (ADULT + DIR + " ¿Qué hay que hacer después de girar a la izquierda? A) seguir derecho dos cuadras B) girar a la derecha", "A) seguir derecho dos cuadras", "Dice go straight for two blocks."),
        (ADULT + RECIPE + " ¿Cuántos ingredientes necesita la receta? A) tres B) dos", "A) tres", "In other words la receta solo necesita three ingredients."),
    ],
    [
        (ADULT + FOLDER + " Un oyente solo entendió «not that one». ¿Qué gesto le ayuda a saber cuál sí? A) señalar la carpeta azul B) mover la cabeza solamente", "A) señalar la carpeta azul", "El gesto de señalar indica la elegida."),
        (ADULT + RULES + " Un oyente dice que la regla más importante es poner las mochilas bajo la mesa. ¿Qué respondes? A) no: es un ejemplo de mantener la sala ordenada B) sí: es la idea principal", "A) no: es un ejemplo de mantener la sala ordenada", "For example introduce un ejemplo, no la regla."),
    ],
    [
        (ADULT + "«First of all, I want to say hello to everyone. The most important thing about this park is that it is free. For example, anybody can play football there. In conclusion, it is a place for all.» (anybody = cualquiera, football = fútbol, free = gratuito, hello = saludo). ¿Cuál es la idea principal? A) que el parque es gratuito B) que se juega fútbol", "A) que el parque es gratuito", "Se anuncia con The most important thing."),
        (ADULT + "«(The speaker puts a finger over her lips.) Shh! Please be quiet. The baby is sleeping.» (finger = dedo, lips = labios, quiet = silencio, baby = bebé, sleeping = durmiendo). ¿Qué pide el gesto? A) silencio B) más ruido", "A) silencio", "El dedo sobre los labios y Shh piden silencio."),
    ],
    [(ADULT + "«(The speaker counts on her fingers.) First, the invitation. Second, the music. Third, the food.» (invitation = invitación, music = música, food = comida). ¿Cuántas cosas hay en la lista? A) tres B) cuatro", "A) tres", "Cuenta con los dedos y dice First, Second, Third.")],
    [
        ("En Inglés de 1.º medio (OA 4, clase 3): ¿qué anuncia The most important thing is...?", "La idea principal", "Es una frase clave."),
        ("En Inglés de 1.º medio (OA 4, clase 3): ¿para qué sirve in other words?", "Para decir lo mismo con palabras más simples", "Reformula una idea."),
        ("En Inglés de 1.º medio (OA 4, clase 3): ¿qué apoyo da señalar con la mano?", "Indica el lugar o el objeto del que se habla", "Es un apoyo visual."),
    ],
    task("Un adulto lee dos veces este texto y hace los gestos entre paréntesis: «First of all, welcome. (The speaker holds up two fingers.) There are two rules. The most important thing is to arrive on time. For example, class starts at eight. In conclusion, be on time and be kind.» (welcome = bienvenidos, rules = reglas, on time = a tiempo, kind = amable). Anota cuántas reglas hay, la idea principal, el ejemplo y la conclusión.", "Hay dos reglas. Idea principal: llegar a tiempo. Ejemplo: la clase empieza a las ocho. Conclusión: ser puntual y amable.", ["anota el número de reglas apoyado en el gesto", "identifica idea principal, ejemplo y conclusión", "usa las frases clave como guía"], ["hoja con cuatro respuestas", "nota del adulto"], ["decir que el ejemplo es la idea principal", "ignorar los dedos levantados"], "Reconoce las frases clave bien ubicadas y repasa con ella cuál introduce el ejemplo y cuál la conclusión."),
    "Escucha un noticiero y anota solo las frases que anuncian ideas, como first, for example o in conclusion.",
    "Escribe una explicación de tres frases en español usando primero, por ejemplo y en conclusión, y tradúcelas a las frases clave en inglés.",
)

# ------------------------------------------------------------------ clase 4: pedir repetición, clarificar y confirmar
W_MEET = "«Clara: The meeting is at half past ten. Dani: Sorry, could you repeat that? Clara: Half past ten, in room four. Dani: So, ten thirty in room four. Clara: Exactly!» (meeting = reunión, half past = y media, repeat = repetir, exactly = exacto)"
W_SUB = "«Teacher: Please submit the report by Thursday. Student: What does submit mean? Teacher: Submit means to give it to me. Student: Oh, deliver it. Thank you!» (submit = entregar, report = informe, deliver = entregar, mean = significar)"
STREET = "«Ben: Take the second street on the right. Nora: Sorry, did you say second or third? Ben: Second. Nora: Thanks! So, second on the right.» (take = toma, street = calle, right = derecha, second = segunda, third = tercera)"
APPLES = "«Sofía: We need two kilos of apples and one of pears. Leo: Could you speak more slowly, please? Sofía: Two kilos of apples, and one kilo of pears.» (apples = manzanas, pears = peras, slowly = más despacio)"
DEAD = "«Mr Ruiz: The deadline is tomorrow at noon. Tina: Do you mean tomorrow at midday, not at midnight? Mr Ruiz: Yes, midday.» (deadline = fecha límite, noon, midday = mediodía, midnight = medianoche)"
GYM = "«Gabriel: I will meet you at the gym at six. Isa: At six in the morning or in the evening? Gabriel: In the evening.» (gym = gimnasio, morning = mañana, evening = tarde-noche)"
HELMET = "«Guide: You must wear a helmet, gloves and shoes. Tourist: So I need three things: a helmet, gloves and shoes. Did I understand correctly? Guide: Yes, that is right.» (guide = guía, must = debes, helmet = casco, gloves = guantes, correctly = correctamente)"

lesson(
    OA, 4, MAT_L,
    "Aprenderé a pedir repetición o aclaración y a confirmar lo que entendí cuando converso con alguien. Sirve para no quedarme con dudas y para evitar malentendidos.",
    ["Sé hacer preguntas simples en inglés.", "Conozco la frase Sorry?"],
    [
        "Cuando no entiendes algo, pedirlo es una estrategia, no una debilidad. Para pedir repetición usa Sorry, could you repeat that, please? Si habla muy rápido, di Could you speak more slowly, please? Para preguntar por una palabra, usa What does ___ mean? Para elegir entre dos datos parecidos, di Did you say second or third?",
        "Para aclarar (to clarify) puedes preguntar Do you mean...? y ofrecer tu interpretación: Do you mean tomorrow at midday? Para confirmar lo que entendiste, repite con tus palabras: So, you want me to... o So I need three things... Termina con Did I understand correctly? o Is that right? y espera que la otra persona diga Yes, that's right o corrija.",
        "En una brecha de información, cada persona sabe una parte. Para completar la información, pregunta lo que falta y confirma lo que recibiste. Una buena secuencia es: escuchar, preguntar lo que falta, repetir con tus palabras y confirmar. Así reduces errores en datos importantes, como horas, lugares y cantidades.",
    ],
    [("Could you repeat that?", "¿Podrías repetir eso?"), ("More slowly, please", "Más despacio, por favor"), ("What does ___ mean?", "¿Qué significa ___?"), ("Do you mean...?", "¿Quieres decir...?"), ("So, you want me to...", "Entonces, quieres que..."), ("Did I understand correctly?", "¿Entendí bien?")],
    [
        ("Pedir repetición y confirmar", ADULT + W_MEET + " ¿Qué dato se repitió y cómo lo confirmó Dani?", ["Dani no entendió la hora y pidió repetir.", "Clara repitió: half past ten, in room four.", "Dani confirmó con So, ten thirty in room four."], "Se repitió la hora y la sala; Dani confirmó con So,..."),
        ("Preguntar por una palabra", ADULT + W_SUB + " ¿Qué pregunta hizo la estudiante y qué significa la palabra?", ["Preguntó What does submit mean?", "La profesora explicó: give it to me.", "Submit significa entregar."], "What does submit mean?; significa entregar"),
    ],
    [
        ("Quedarse callado cuando no se entendió.", "Se cree que preguntar muestra debilidad.", "Usa Could you repeat that, please? como estrategia."),
        ("Repetir lo entendido sin pedir confirmación.", "Se asume que la interpretación es correcta.", "Termina con Did I understand correctly? o Is that right?"),
    ],
    [
        ("No entendiste lo que dijo tu compañero porque habló rápido. ¿Qué dices? A) Could you speak more slowly, please? B) Where is the bus?", "A) Could you speak more slowly, please?", "Pide hablar más despacio."),
        ("Quieres saber el significado de una palabra nueva. ¿Qué preguntas? A) What does this word mean? B) How old are you?", "A) What does this word mean?", "Es la frase para preguntar el significado."),
        ("Quieres confirmar lo que entendiste. ¿Cómo terminas? A) Did I understand correctly? B) See you tomorrow.", "A) Did I understand correctly?", "Pide confirmar lo entendido."),
    ],
    [
        (ADULT + STREET + " ¿Qué dudó Nora? A) si era la segunda o la tercera calle B) si era a la izquierda", "A) si era la segunda o la tercera calle", "Preguntó second or third."),
        (ADULT + APPLES + " ¿Qué pidió Leo? A) que hablara más despacio B) que repitiera el precio", "A) que hablara más despacio", "Dice Could you speak more slowly, please?"),
        (ADULT + DEAD + " ¿Qué aclaró Tina? A) que era mediodía y no medianoche B) que la fecha era hoy", "A) que era mediodía y no medianoche", "Preguntó Do you mean tomorrow at midday, not at midnight?"),
    ],
    [
        (ADULT + GYM + " ¿Qué pregunta aclaró la hora? A) At six in the morning or in the evening? B) Where is the gym?", "A) At six in the morning or in the evening?", "Pregunta cuál de las dos opciones es."),
        (ADULT + HELMET + " ¿Cuántas cosas dijo el turista que necesitaba? A) tres B) dos", "A) tres", "Dice So I need three things."),
        (ADULT + STREET + " ¿Cómo confirmó Nora? A) repitiendo: second on the right B) preguntando otra vez por la tercera", "A) repitiendo: second on the right", "Repetir con palabras propias confirma lo entendido."),
    ],
    [
        (ADULT + APPLES + " Un amigo dice que Leo necesita dos kilos de peras. ¿Qué datos aclara Sofía? A) dos kilos de manzanas y uno de peras B) uno de manzanas y dos de peras", "A) dos kilos de manzanas y uno de peras", "Lo repite despacio al final del diálogo."),
        (ADULT + HELMET + " Un oyente dice que el turista no entendió bien. ¿Qué dato lo contradice? A) el guía responde Yes, that is right B) el guía repite la lista", "A) el guía responde Yes, that is right", "Confirma que la interpretación fue correcta."),
    ],
    [
        (ADULT + "«Ema: The concert starts at seven. Fer: Sorry, did you say seven or eleven? Ema: Seven. Fer: So, seven in the evening. Is that right? Ema: Yes, that is right.» (concert = concierto, starts = empieza, evening = tarde-noche). ¿Qué dato aclaró Fer? A) la hora, siete u once B) el lugar del concierto", "A) la hora, siete u once", "Preguntó seven or eleven para no confundir los números parecidos."),
        (ADULT + "«Sam: Please bring a spare charger. Mika: What does spare mean? Sam: Extra. One you don't use every day.» (spare = de repuesto, charger = cargador, extra = adicional). ¿Qué significa spare? A) de repuesto, adicional B) caro", "A) de repuesto, adicional", "Sam lo explica con extra."),
    ],
    [(ADULT + "«Coach: Practice moves to Wednesday at five. Player: Sorry, do you mean this Wednesday, not next? Coach: Yes, this Wednesday.» (practice = entrenamiento, moves = se cambia, this = este, next = próximo). ¿Qué dato se aclara? A) el miércoles de esta semana B) el miércoles de la próxima semana", "A) el miércoles de esta semana", "El entrenador confirma this Wednesday, not next.")],
    [
        ("En Inglés de 1.º medio (OA 4, clase 4): ¿cómo se pide que repitan?", "Could you repeat that, please?", "Es la frase para pedir repetición."),
        ("En Inglés de 1.º medio (OA 4, clase 4): ¿cómo se confirma lo entendido?", "Repitiéndolo con tus palabras y preguntando Did I understand correctly?", "Se pide confirmación."),
        ("En Inglés de 1.º medio (OA 4, clase 4): ¿cómo se pregunta el significado de una palabra?", "What does ___ mean?", "Pregunta por el significado."),
    ],
    task("Un adulto lee una sola vez, bastante rápido: «The workshop is on Tuesday at a quarter past four in room nine. Bring a notebook and a pen.» (workshop = taller, a quarter past four = cuatro y cuarto, notebook = cuaderno, pen = lápiz de pasta). Escribe en inglés dos preguntas para pedir repetición o aclaración (por ejemplo, la hora) y una frase para confirmar lo que entendiste.", "Preguntas: Sorry, could you repeat the time, please? Do you mean room nine? Confirmación: So, Tuesday at 4:15 in room nine. Did I understand correctly?", ["escribe dos preguntas de clarificación", "escribe una frase de confirmación", "usa las frases aprendidas sin inventar datos"], ["hoja con tres frases", "nota del adulto"], ["preguntar algo que no aparece en el texto", "no pedir confirmación"], "Reconoce las frases útiles y pide que revise si sus preguntas apuntan a un dato real del texto."),
    "Memoriza tres frases para pedir ayuda al conversar y úsalas en voz alta con una persona de tu casa.",
    "Pide a una persona de tu casa que te dé una instrucción de tres pasos, pide repetición de uno y confírmalos con So...",
)

# ------------------------------------------------------------------ clase 5: confirmar predicciones y resumir con apoyo
DANI = "«Hi, I'm Daniela. I moved to Concepción last month. At first I felt lonely, but my teacher introduced me to the drama club. Now I have new friends, and next month we will perform a play.» (moved = me mudé, lonely = sola, introduced = presentó, drama club = taller de teatro, perform = presentar, play = obra de teatro)"
VOLC = "«Welcome, visitors. The volcano trail takes about two hours. It is steep at the beginning, but easier after the first bridge. Wear strong shoes and bring water. Do not leave the path.» (trail = sendero, steep = empinado, bridge = puente, strong shoes = zapatos resistentes, path = camino)"
MARKET = "«Dear readers, the public library will close for repairs next Monday. Instead, you can borrow books at the tables in the square. Thank you for your patience.» (readers = lectores, public library = biblioteca pública, repairs = reparaciones, borrow = pedir prestado, square = plaza, patience = paciencia)"
RADIO = "«Good morning, listeners. Today we talk about volunteering. A group of teenagers cleans the river every month. They say it is hard work, but it is also fun. If you want to join, call the number on our website.» (listeners = oyentes, volunteering = voluntariado, teenagers = adolescentes, river = río, join = unirse, website = sitio web)"

lesson(
    OA, 5, MAT_L,
    "Aprenderé a usar por mi cuenta todas las estrategias: predecir, escuchar con propósito, inferir, confirmar y resumir algunas ideas con apoyo. Sirve para entender un texto nuevo y comprobar si lo entendí bien.",
    ["Sé predecir y escuchar con un propósito.", "Sé pedir repetición y confirmar lo entendido."],
    [
        "En una escucha independiente (independent listening) combinas las estrategias en orden. Antes de escuchar: lees el título, predices y decides tu propósito. Mientras escuchas: atiendes frases clave, números, tono y gestos. Después de escuchar: confirmas tus predicciones, resumes y compruebas tu comprensión con una pregunta si es necesario.",
        "Resumir (to summarize) es decir lo esencial con pocas palabras, sin detalles menores. Un buen resumen responde quién, qué y para qué, y usa tus palabras. Para apoyar el resumen, conserva dos o tres palabras clave del texto. Por ejemplo: Daniela se mudó, se sintió sola, entró al teatro y ahora tiene amigos.",
        "Para confirmar tu comprensión puedes preguntar Did I understand correctly that...? y decir tu resumen. Si la otra persona corrige, ajusta tus ideas. Recuerda que una inferencia debe apoyarse en una pista: no inventes información que el texto no entregó. Si no lo dice, puedes decir The text doesn't say.",
    ],
    [("summarize", "resumir"), ("confirm a prediction", "confirmar una predicción"), ("main points", "ideas principales"), ("The text doesn't say.", "El texto no lo dice."), ("support", "apoyo: pista o dato que respalda"), ("check understanding", "comprobar la comprensión")],
    [
        ("Confirmar una predicción", "Título: «A new student». Predices: new school, friends, feelings. " + ADULT + DANI + " ¿Qué predicción se confirma más claramente?", ["El texto habla de mudarse y de sentirse sola.", "También de nuevos amigos.", "Por eso se confirman new school, friends y feelings."], "Las tres: nuevo lugar, amigos y sentimientos"),
        ("Resumir", ADULT + DANI + " Resume el texto en una frase.", ["Quién: Daniela.", "Qué: se mudó, se sintió sola, entró al club de teatro.", "Para qué: hoy tiene amigos y prepara una obra."], "Daniela se mudó, se sintió sola, entró al teatro y ahora tiene amigos"),
    ],
    [
        ("Resumir copiando todos los detalles.", "No se distingue lo esencial de lo secundario.", "Responde quién, qué y para qué en una frase."),
        ("Agregar información que el texto no dio.", "Se mezclan inferencias con datos inventados.", "Si no lo dice, responde The text doesn't say."),
    ],
    [
        (ADULT + VOLC + " ¿Cuánto dura el sendero? A) unas dos horas B) unas doce horas", "A) unas dos horas", "Dice about two hours."),
        (ADULT + MARKET + " ¿Dónde se podrán pedir libros prestados el lunes? A) en las mesas de la plaza B) en la biblioteca", "A) en las mesas de la plaza", "Instead, you can borrow books at the tables in the square."),
        (ADULT + RADIO + " ¿Cuál es el tema? A) el voluntariado de adolescentes que limpian un río B) la historia de un río", "A) el voluntariado de adolescentes que limpian un río", "Dice Today we talk about volunteering."),
    ],
    [
        (ADULT + VOLC + " ¿Qué se recomienda llevar? A) zapatos resistentes y agua B) un paraguas", "A) zapatos resistentes y agua", "Dice Wear strong shoes and bring water."),
        (ADULT + MARKET + " ¿Por qué cerrará la biblioteca? A) por reparaciones B) por un feriado", "A) por reparaciones", "Dice will close for repairs."),
        (ADULT + RADIO + " ¿Qué opinan los adolescentes del trabajo? A) que es difícil, pero entretenido B) que es aburrido", "A) que es difícil, pero entretenido", "Dice hard work, but it is also fun."),
    ],
    [
        (ADULT + VOLC + " ¿Cuál es el resumen más fiel? A) el sendero dura unas dos horas, empieza empinado y exige zapatos resistentes B) el sendero es plano y no necesita preparación", "A) el sendero dura unas dos horas, empieza empinado y exige zapatos resistentes", "Reúne los datos principales del texto."),
        (ADULT + MARKET + " ¿Qué solución se ofrece? A) pedir libros en las mesas de la plaza B) esperar en casa", "A) pedir libros en las mesas de la plaza", "Es la solución al cierre por reparaciones."),
        (ADULT + RADIO + " ¿Qué debe hacer quien quiera unirse? A) llamar al número del sitio web B) ir al río el lunes", "A) llamar al número del sitio web", "Dice call the number on our website."),
    ],
    [
        (ADULT + RADIO + " Un compañero dice que el texto no explica cuándo limpian el río. ¿Es cierto? A) no: dice every month, cada mes B) sí: no hay ningún dato de tiempo", "A) no: dice every month, cada mes", "Hay un dato de frecuencia."),
        (ADULT + DANI + " Un compañero dice que Daniela vive en Santiago. ¿Qué respondes? A) el texto dice Concepción, no Santiago B) sí, por la ciudad grande", "A) el texto dice Concepción, no Santiago", "No se debe agregar información que no aparece."),
    ],
    [
        (ADULT + DANI + " ¿Cuál es el mejor resumen? A) Daniela se mudó, se sintió sola, entró al teatro y ahora tiene amigos B) Daniela vive en Concepción y estudia teatro desde niña", "A) Daniela se mudó, se sintió sola, entró al teatro y ahora tiene amigos", "El resumen sigue lo que dice el texto; la otra opción agrega datos que no aparecen."),
        (ADULT + VOLC + " Un compañero dice que el texto no avisa si el sendero es difícil. ¿Qué respondes? A) sí avisa: es empinado al inicio y más fácil después del primer puente B) no dice nada sobre la dificultad", "A) sí avisa: es empinado al inicio y más fácil después del primer puente", "Dice steep at the beginning, but easier after the first bridge."),
    ],
    [(ADULT + "«Title: Fun Run Day. Attention, runners. This Saturday, the city closes Main Street to cars from nine to one. Bring a water bottle. A first-aid stand will help with small problems.» (runners = corredores, Main Street = calle principal, first-aid stand = puesto de primeros auxilios). Predijiste horarios y reglas. ¿Qué dato confirma esa predicción? A) la calle se cierra a los autos de nueve a una B) habrá un partido de fútbol", "A) la calle se cierra a los autos de nueve a una", "Es un horario y una regla del día.")],
    [
        ("En Inglés de 1.º medio (OA 4, clase 5): ¿qué responde un buen resumen?", "Quién, qué y para qué, con pocas palabras", "Reúne lo esencial."),
        ("En Inglés de 1.º medio (OA 4, clase 5): ¿qué dices si el texto no da un dato?", "The text doesn't say.", "No se inventa información."),
        ("En Inglés de 1.º medio (OA 4, clase 5): ¿cómo compruebas tu comprensión con otra persona?", "Preguntando Did I understand correctly that...? y diciendo tu resumen", "Esperas su confirmación."),
    ],
    task("Lee el título «Garden Club» y escribe tres palabras que esperas oír. Un adulto lee dos veces: «Welcome to the Garden Club. Every Wednesday, students plant flowers and vegetables. The most important rule is to water the plants gently. In conclusion, we learn and have fun.» (club = club, plant = plantar, flowers = flores, water = regar, gently = con suavidad). Confirma tus predicciones, resume en una frase y escribe una pregunta para comprobar tu comprensión.", "Predije: plants, flowers, water. Se confirman las tres. Resumen: el club planta flores y verduras los miércoles y enseña a regar con cuidado. Pregunta: Did I understand correctly that the club meets on Wednesdays?", ["escribe tres predicciones coherentes y las confirma", "resume sin detalles menores", "formula una pregunta de comprensión en inglés"], ["hoja con predicción, confirmación, resumen y pregunta", "nota del adulto"], ["agregar datos que el texto no dijo", "no confirmar las predicciones"], "Reconoce lo logrado y revisa con ella si el resumen respondió quién, qué y para qué."),
    "Resume en una frase en español el último video que viste, usando quién, qué y para qué.",
    "Escribe un resumen de una frase de cada texto de esta clase y compáralo con el de otra persona.",
)
