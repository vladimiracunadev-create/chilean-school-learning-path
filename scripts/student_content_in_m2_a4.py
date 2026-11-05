"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 04: estrategias de escucha, notas e inferencias con apoyo.

Las «escuchas» las lee un adulto: el guion va escrito en el enunciado; los gestos y la entonación se indican entre corchetes o
con mayúsculas para el énfasis. Textos originales, inglés americano. Los títulos de clase del plan son genéricos; aquí se
aplican a predecir y escuchar con propósito, frases clave y gestos, pedir repetición y confirmar, inferencias y tomar notas.
"""
from __future__ import annotations

from in_m2_common import ADULT, MAT_L, arith, lesson, mc, ml, mr, task

OA = "IN2M OA 04"

# ------------------------------------------------------------------ clase 1: predecir, conocimientos previos y propósito
AQ = "«Welcome to the Bay Aquarium. Our tour starts with the penguins. At eleven o'clock, you can watch the keepers feed them. After that, we visit the jellyfish room, which is dark and quiet. Please do not knock on the tanks.» (aquarium = acuario, tour = visita guiada, penguins = pingüinos, keepers = cuidadores, feed = alimentar, jellyfish = medusas, tanks = peceras grandes)"
MK = "«Welcome to the market. Today the fruit is fresh: apples, pears and grapes. Buy two kilos and get the third kilo at half price.» (market = feria, fresh = fresca, apples = manzanas, pears = peras, grapes = uvas, half price = mitad de precio)"
FM = "«Good evening, fans. The score is two to one. The striker runs, she shoots... and it's a goal!» (fans = hinchas, score = marcador, striker = delantera, shoots = patea)"
FARM = "«Good morning, students. Today we visit Sunny Farm. The bus leaves at nine and returns at three. Wear comfortable shoes and bring a jacket, because the barn is cold. Lunch is at noon.» (farm = granja, returns = regresa, comfortable = cómodos, barn = establo, lunch = almuerzo)"
WA1 = "Situación: escucharás a un guía de planetario. Antes de escuchar, piensa qué palabras esperas oír: stars, telescope, night, show."
WA2 = "Propósito de escucha: «Saber a qué hora alimentan a los pingüinos». Texto: " + AQ

lesson(
    OA, 1, MAT_L,
    "Aprenderé a hacer predicciones antes de escuchar, a usar lo que ya sé del tema y a escuchar con un propósito claro. Sirve para entender más y para comprobar mis predicciones después.",
    ["Sé que el título o la situación dan pistas del tema.", "Conozco palabras de lugares y actividades."],
    [
        "Antes de escuchar, mira el título, el lugar o la situación y haz una predicción (prediction): piensa qué palabras e ideas vas a oír. Para eso usas tus conocimientos previos (prior knowledge): lo que ya sabes de ese tema o de situaciones parecidas. Si vas a oír a un guía de acuario, esperas palabras como fish, tank, feed y tour.",
        "Escuchar con un propósito (listening for a purpose) significa decidir antes qué quieres saber, por ejemplo la hora, el lugar o lo que debes llevar. Con ese propósito, ignoras lo que no necesitas y anotas solo el dato. Durante la escucha comparas lo que oyes con tus predicciones. Después las confirmas (confirm) si el texto las cumple, o las corriges si no.",
        "Una predicción no es una adivinanza: se basa en pistas. Si el audio contradice tu predicción, cambia tu idea y sigue escuchando. Lo importante es que el cambio use lo que oyes.",
    ],
    [("prediction", "predicción: idea de lo que se va a oír"), ("prior knowledge", "conocimientos previos"), ("listening for a purpose", "escuchar con un propósito"), ("confirm", "confirmar"), ("purpose", "propósito"), ("clue", "pista")],
    [
        ("Predecir con una situación", WA1 + " ¿Qué palabras esperas oír y por qué?", ["La situación es un planetario.", "Un planetario muestra cielo y astros.", "Espero stars, telescope, night y show."], "Stars, telescope, night y show, porque un planetario trata del cielo"),
        ("Escuchar con un propósito", WA2 + " ¿Qué dato anotas?", ["Busco una hora relacionada con los pingüinos.", "Dice At eleven o'clock, you can watch the keepers feed them.", "Anoto 11:00 e ignoro el resto."], "11:00"),
    ],
    [
        ("Escribir una predicción sin pista, solo por azar.", "Una predicción necesita apoyarse en el título o en la situación.", "Primero pregunta qué pistas tienes."),
        ("Mantener la predicción aunque el audio la contradiga.", "Se pierde información por defender la idea inicial.", "Cambia la predicción con lo que oyes."),
    ],
    [
        mc("Vas a oír un aviso en una estación de buses. ¿Qué palabra es más probable que oigas? (platform = andén, homework = tarea, sandwich = sándwich)", "platform", ["homework", "sandwich"], "En una estación se habla de andenes."),
        mc("Escuchar con un propósito significa", "decidir antes qué dato quieres encontrar", ["escribir todo lo que se oiga", "esperar hasta el final sin atender"], "Un propósito guía qué anotas."),
        ml(AQ, "Predijiste la palabra penguins. ¿Se confirma tu predicción?", "Sí: la visita empieza con los pingüinos", ["No: la visita empieza con la sala de las medusas", "No: el texto habla de otros animales, no de pingüinos"], "Dice Our tour starts with the penguins."),
    ],
    [
        mc("Vas a oír información sobre una visita al Science Museum. ¿Qué conocimiento previo te ayuda más?", "Que en un museo hay entradas, salas y guías", ["Que los museos siempre cierran de noche", "Que el inglés tiene muchas palabras"], "Ese conocimiento permite predecir palabras de la visita."),
        ml(MK, "Predijiste que se hablaría de precios. ¿Se confirma?", "Sí: dice que hay oferta a mitad de precio", ["No: el texto no menciona ninguna oferta de precios", "No: el audio solo habla de frutas y de verduras"], "Dice the third kilo at half price."),
        ml(FARM, "Tu propósito es saber qué llevar. ¿Qué anotas?", "Zapatos cómodos y una chaqueta", ["Un almuerzo y un balón", "Una linterna y un mapa"], "Dice wear comfortable shoes and bring a jacket."),
    ],
    [
        mc("El título es «Final Match of the City Tennis Cup». ¿Qué grupo de palabras es la mejor predicción? (serve = sacar, score = marcador, winner = ganador)", "serve, score, winner", ["recipe, oven, sugar", "passport, luggage, gate"], "Son palabras de un partido de tenis."),
        mc("Vas a oír un aviso de horarios de tren. ¿Qué propósito de escucha es mejor?", "Anotar la hora y el andén", ["Contar cuántas palabras hay", "Aprender la letra de una canción"], "Es el dato que necesitas para tomar el tren."),
        ml(AQ, "Tu propósito es saber qué no se debe hacer. ¿Qué anotas?", "No golpear las peceras", ["No dar de comer a los peces", "No entrar a la sala oscura"], "Dice Please do not knock on the tanks."),
    ],
    [
        ml(FM, "Un oyente predijo que hablarían de comida, pero el audio habla de un partido. ¿Qué debe hacer?", "Corregir su predicción con lo que oye", ["Seguir con su predicción porque ya la escribió", "Dejar de escuchar"], "Una predicción se ajusta con la evidencia del audio."),
        mc("Leo anota time y place antes de oír un aviso de reunión. Ana no anota nada. ¿Quién escucha con propósito?", "Leo, porque decide qué datos buscar", ["Ana, porque escucha sin distraerse", "Los dos por igual"], "El propósito se define antes de escuchar."),
    ],
    [
        ml(AQ, "Predijiste que la sala de las medusas sería ruidosa. ¿Qué dice el texto?", "Es oscura y tranquila: tu predicción no se confirma", ["Es ruidosa y llena de gente, así que se confirma", "No dice nada de la sala, así que no se puede saber"], "Dice dark and quiet."),
        mc("¿Cuál es el orden correcto de las estrategias?", "Predecir, escuchar con un propósito y confirmar", ["Confirmar, predecir y escuchar", "Escuchar, olvidar y predecir"], "La predicción va antes y la confirmación al final."),
    ],
    [ml(FARM, "Una compañera escucha este aviso y solo anota que el almuerzo es al mediodía. Para llegar y volver, ¿qué otros datos necesita?", "La hora de salida y la de regreso del bus", ["Solo el nombre de la granja", "La hora del almuerzo y los zapatos"], "Dice The bus leaves at nine and returns at three.")],
    [
        ("En Inglés de 2.º medio (OA 4, clase 1): ¿qué es una predicción?", "Una idea de lo que se va a oír, basada en pistas", "No es azar: parte de la situación o del título."),
        ("En Inglés de 2.º medio (OA 4, clase 1): ¿qué haces si el audio contradice tu predicción?", "La corriges con lo que oyes", "La evidencia manda."),
        ("En Inglés de 2.º medio (OA 4, clase 1): ¿para qué sirve decidir un propósito antes de escuchar?", "Para saber qué dato anotar", "Dirige la atención."),
    ],
    task("Lee esta situación: vas a escuchar un aviso en un cine sobre una función especial. Escribe tres palabras que predices y un propósito de escucha. Luego un adulto lee: «Attention, please. Tonight's special show starts at eight thirty, not eight. Tickets cost four thousand pesos. Children under ten are free.» (special show = función especial, tickets = entradas, children = niños, free = gratis). Marca qué predicciones se confirmaron.", "Predicciones: tickets, time, movie. Propósito: anotar la hora y el precio. Se confirman tickets y time; movie no se menciona. Datos: 8:30 y 4.000 pesos.", ["escribe tres predicciones con pista", "define un propósito claro", "marca qué se confirmó y qué no"], ["ficha con predicciones, propósito y datos"], ["predecir sin pista", "anotar todo en vez de un dato"], "Pide que explique por qué su propósito le ayudó a ignorar información."),
    "Lee el título «A Winter Night at the Airport» y escribe tres palabras que esperas oír.",
    "Elige un audio que escuches esta semana (clase, noticia) y escribe antes dos predicciones y un propósito.",
)

# ------------------------------------------------------------------ clase 2: frases clave, gestos y entonación
G1 = "«Remember: the test is on Friday, not Thursday. Don't forget your pencil case. [holds up a pencil] Only pencils, no pens.» (test = prueba, pencil case = estuche, only = solo, pens = lápices pasta)"
G2 = "«You are coming to the party? [rising voice] Great. [falling voice] I will bring the music.» (coming = vienes, party = fiesta, bring = traer, music = música)"
G3 = "«We meet at SIX, not at five. [raises six fingers] Please be on time.» (meet = nos juntamos, on time = a la hora, the capital letters mean strong voice)"
G4 = "«The key thing is to arrive early. Don't forget to bring your ID. In short: be early, bring your ID, and stay calm.» (key thing = lo clave, arrive = llegar, ID = cédula, in short = en resumen, calm = tranquilo)"
G5 = "«[holds hands wide apart] The pizza was this big! [laughs] Okay, maybe not that big, but it was huge.» (pizza = pizza, wide apart = muy separadas, huge = enorme)"
G6 = "«[sighs, slow voice] Great. Another test on Monday.» (sighs = suspira, slow = lenta, another = otra)"
G7 = "«Listen carefully. First, turn left at the bank. Second, walk two blocks. [points ahead] The library is at the corner. Remember: it closes at five.» (turn left = gira a la izquierda, bank = banco, blocks = cuadras, points ahead = señala hacia adelante, corner = esquina, closes = cierra)"
G8 = "«Mr. Díaz: Who finished the project? [pause, looks at the class] Nobody? [raises eyebrows] Then we have a problem.» (project = proyecto, pause = pausa, looks at = mira a, nobody = nadie, raises eyebrows = levanta las cejas)"

lesson(
    OA, 2, MAT_L,
    "Aprenderé a atender frases clave (remember, the key thing is, in short), gestos del hablante y la entonación para entender mejor lo que oigo. Sirve para captar la intención de quien habla aunque no entienda todas las palabras.",
    ["Sé que un hablante puede subir o bajar la voz.", "Conozco first, then y finally."],
    [
        "Las frases clave anuncian lo importante: remember, don't forget, the key thing is, the most important thing is, pay attention to e in short. Después de esas frases suele venir el dato que debes anotar. Los gestos (gestures) también ayudan: señalar con la mano indica un lugar o una dirección; levantar dedos indica un número; abrir los brazos indica algo grande; sacudir la cabeza indica que no.",
        "La entonación (intonation) es la subida y bajada de la voz. En una pregunta que se responde con sí o no, la voz suele subir al final: You are coming? En una afirmación, suele bajar. Cuando el hablante dice una palabra con más fuerza, como SIX en We meet at SIX, not at five, esa palabra es la que corrige o destaca. Una voz lenta con un suspiro puede mostrar cansancio o molestia, aunque la palabra sea positiva, como Great.",
        "Al escuchar, combina tres pistas: palabras clave, gestos y entonación. Si coinciden, tu comprensión es segura. Si no coinciden, como una palabra alegre con una voz triste, piensa en el sentimiento real del hablante.",
    ],
    [("remember / don't forget", "recuerda / no olvides"), ("the key thing is", "lo clave es"), ("in short", "en resumen"), ("gesture", "gesto"), ("intonation", "entonación: subida y bajada de la voz"), ("stress on a word", "énfasis en una palabra")],
    [
        ("Palabras clave y gestos", ADULT + G1 + " ¿Qué datos importantes se subrayan?", ["Remember anuncia un dato: es el viernes y no el jueves.", "Don't forget anuncia otro: llevar estuche.", "El gesto de levantar un lápiz refuerza que son solo lápices."], "La prueba es el viernes, hay que llevar estuche y solo lápices"),
        ("Entonación", ADULT + G2 + " ¿Qué muestra la voz que sube en la primera frase?", ["La voz sube al final de You are coming?", "Eso suele indicar una pregunta.", "Luego Great baja la voz: acepta la respuesta."], "Que es una pregunta"),
    ],
    [
        ("Pensar que Great siempre es alegre.", "El tono y los gestos pueden mostrar lo contrario.", "Escucha cómo suena la voz, no solo la palabra."),
        ("Ignorar una palabra dicha con más fuerza.", "El énfasis suele marcar una corrección o lo más importante.", "Pregúntate por qué el hablante subraya esa palabra."),
    ],
    [
        ml(G1, "¿Qué día es la prueba?", "El viernes", ["El jueves", "El miércoles"], "Dice the test is on Friday, not Thursday."),
        ml(G4, "¿Qué frase anuncia el resumen?", "In short", ["The key thing", "Don't forget"], "In short introduce el resumen."),
        ml(G5, "¿Qué muestran las manos muy separadas?", "Que la pizza era muy grande", ["Que el hablante cuenta cuántas pizzas compró", "Que la pizza era muy pequeña"], "El gesto marca el tamaño que se cuenta."),
    ],
    [
        ml(G3, "¿Qué palabra se dice con más fuerza y qué muestra?", "SIX: corrige la hora de cinco a seis", ["be: da la orden de llegar a la hora justa", "meet: pregunta en qué lugar se juntan"], "El énfasis en SIX corrige el five."),
        ml(G6, "¿Cómo se siente el hablante?", "Molesto o cansado, aunque diga Great", ["Muy contento", "Sorprendido y feliz"], "El suspiro y la voz lenta contradicen la palabra Great."),
        ml(G7, "¿Qué señala el gesto de apuntar hacia adelante?", "Dónde queda la biblioteca", ["Que hay que girar a la derecha", "Que el banco está cerrado"], "Points ahead acompaña The library is at the corner."),
    ],
    [
        ml(G7, "¿A qué hora cierra la biblioteca?", "A las cinco", ["A las seis", "A las cuatro"], "Después de Remember dice it closes at five."),
        ml(G8, "¿Qué muestra la pausa del profesor y mirar al curso?", "Que espera una respuesta de los estudiantes", ["Que quiere terminar la clase", "Que está contando un chiste"], "Pausa y mirada piden que alguien responda."),
        ml(G4, "¿Cuál es lo clave según el hablante?", "Llegar temprano", ["Llevar dinero", "Hablar fuerte"], "The key thing is to arrive early."),
    ],
    [
        ml(G8, "El profesor dice Nobody? con las cejas levantadas. ¿Qué indica?", "Sorpresa o molestia porque nadie terminó", ["Alegría porque todos terminaron", "Que ya nadie tiene dudas"], "Cejas levantadas y entonación ascendente muestran sorpresa."),
        ml(G2, "¿En qué se diferencia You are coming? de You are coming. en la voz?", "La primera sube y pregunta; la segunda baja y afirma", ["La primera baja y pregunta; la segunda sube y afirma", "Solo cambia el volumen, no el sentido de la frase"], "La subida de la voz marca la pregunta."),
    ],
    [
        ml(G1, "Un compañero oyó solo Thursday y se preparó para ese día. ¿Qué pista debió atender para no equivocarse?", "La frase not Thursday", ["El gesto de levantar el lápiz", "La frase Only pencils, no pens"], "Not Thursday corrige el día."),
        ml(G3, "¿Qué muestran los seis dedos levantados?", "Que se refiere a las seis", ["Que son seis personas", "Que hay seis minutos"], "El gesto refuerza el SIX."),
    ],
    [ml(G4, "¿Cuáles son los tres consejos del resumen?", "Llegar temprano, llevar la cédula y mantener la calma", ["Llegar tarde, llevar dinero y hablar poco", "Estudiar, comer y dormir"], "In short enumera be early, bring your ID y stay calm.")],
    [
        ("En Inglés de 2.º medio (OA 4, clase 2): ¿qué suele anunciar remember?", "Un dato importante que no hay que olvidar", "Es una frase clave."),
        ("En Inglés de 2.º medio (OA 4, clase 2): ¿qué suele indicar una voz que sube al final?", "Una pregunta", "La entonación ascendente es típica de las preguntas de sí o no."),
        ("En Inglés de 2.º medio (OA 4, clase 2): ¿qué ayuda a entender el sentimiento real si la palabra y el tono no coinciden?", "El tono, el gesto y la situación", "Son pistas que no se ven en la palabra sola."),
    ],
    task("Un adulto lee dos veces: «Listen, everyone. [claps hands] The most important thing today is safety. Remember: walk, don't run. [points to the door] The exit is that way. [raises one finger] Only one person at a time. In short: stay calm and follow me.» (safety = seguridad, walk = camina, run = corre, exit = salida, one at a time = de uno en uno, follow = sigue). Anota tres frases clave, un gesto y qué te dice.", "Frases clave: the most important thing, remember, in short. Gesto: señala la puerta y dice dónde está la salida. También levanta un dedo: de uno en uno.", ["anota tres frases clave", "describe un gesto y qué indica", "relaciona la pista con el mensaje"], ["hoja con tres frases y un gesto"], ["anotar solo palabras sueltas", "no explicar el gesto"], "Pide que relacione cada frase clave con la instrucción que anuncia."),
    "Escucha otra vez la frase We meet at SIX, not at five y practica dar énfasis a la palabra correcta.",
    "Observa cómo habla alguien en un video sin sonido: describe en español dos gestos y qué crees que quiere decir.",
)

# ------------------------------------------------------------------ clase 3: pedir repetición, clarificar y confirmar
R1 = "«Receptionist: Your session starts at fifteen minutes past four. Student: Sorry, did you say fifteen or fifty? Receptionist: Fifteen. Quarter past four.» (session = sesión, receptionist = recepcionista, fifteen = quince, fifty = cincuenta, quarter past four = cuatro y cuarto)"
R2 = "«Coach: Tomorrow, bring your kit and a towel. Student: Sorry, I didn't catch the last word. Could you repeat it, please? Coach: A towel. For the shower after practice.» (kit = equipo, towel = toalla, catch = entender, shower = ducha)"
R3 = "«Guide: The tour ends at the lookout. Tourist: What does lookout mean? Guide: It is a high place where you can see the city. Tourist: Oh, a viewpoint. Thank you.» (guide = guía, lookout = mirador, viewpoint = mirador, city = ciudad)"
R4 = "«Agent: You need the blue form, on the second floor. Customer: Do you mean the blue form or the green form? Agent: The blue one. The green one is for foreign students.» (agent = funcionaria, form = formulario, foreign = extranjeros)"
R5 = "«Teacher: The assignment is due next Wednesday. Student: So the deadline is the next Wednesday, not this one. Is that right? Teacher: Exactly.» (assignment = tarea, due = para el, deadline = plazo, exactly = exacto)"
R6 = "«Man: The bus leaves from gate seven. Woman: Could you speak more slowly, please? Man: Of course. From... gate... seven. Woman: Thank you.» (gate = puerta, speak slowly = hablar despacio, of course = por supuesto)"

lesson(
    OA, 3, MAT_L,
    "Aprenderé a pedir repetición, a pedir que me expliquen una palabra y a preguntar para confirmar lo que entendí. Sirve para no quedarme con dudas en conversaciones reales.",
    ["Sé hacer preguntas con could y what.", "Conozco please y thank you."],
    [
        "Si no entiendes algo, pídelo con cortesía. Para pedir repetición usa Sorry, could you repeat that, please? o Sorry, I didn't catch the last word. Para pedir que hablen más despacio usa Could you speak more slowly, please? Para pedir el significado de una palabra usa What does lookout mean? Si dudas entre dos opciones, pregunta Did you say fifteen or fifty?",
        "Para confirmar que entendiste, repite con tus palabras y agrega una pregunta: So the deadline is next Wednesday. Is that right? También sirven Do you mean...? y So you are saying that...? Quien responde puede decir Exactly o That's right si es correcto, o corregir con No, I mean... si no lo es.",
        "Pedir clarificación no muestra debilidad: muestra que escuchas con atención. Hazlo en el momento, con una frase corta y una sonrisa, y vuelve a anotar el dato.",
    ],
    [("Could you repeat that, please?", "¿Puede repetir, por favor?"), ("I didn't catch that", "no alcancé a entender"), ("Could you speak more slowly?", "¿Puede hablar más despacio?"), ("What does ... mean?", "¿Qué significa ...?"), ("Do you mean ...?", "¿Quiere decir ...?"), ("Is that right?", "¿Es correcto?")],
    [
        ("Distinguir números parecidos", ADULT + R1 + " ¿Qué pregunta hace el estudiante y a qué hora es la sesión?", ["Pregunta Did you say fifteen or fifty?", "La respuesta es Fifteen. Quarter past four.", "La sesión es a las 4:15."], "Pregunta si dijo quince o cincuenta; la sesión es a las 4:15"),
        ("Confirmar con una pregunta", ADULT + R5 + " ¿Qué hace el estudiante para confirmar?", ["Repite con sus palabras: the deadline is the next Wednesday.", "Agrega la pregunta Is that right?", "La profesora responde Exactly."], "Repite el plazo y pregunta si es correcto; la profesora lo confirma"),
    ],
    [
        ("Quedarse callado cuando no se entiende.", "Se pierde información importante.", "Usa Sorry, could you repeat that, please?"),
        ("Pedir repetición sin decir qué parte no se entendió.", "El hablante repite todo y no soluciona la duda.", "Di qué parte no entendiste: the last word, the time, the number."),
    ],
    [
        ml(R2, "¿Qué frase usa el estudiante para decir que no entendió la última palabra?", "Sorry, I didn't catch the last word", ["What does the last word mean in Spanish?", "Do you mean the last word or the first word?"], "Con ella pide repetir la última palabra."),
        ml(R6, "¿Qué le pide la mujer al hombre?", "Que hable más despacio", ["Que repita todo", "Que cambie de puerta"], "Could you speak more slowly significa más despacio."),
        ml(R3, "¿Qué pregunta el turista?", "Qué significa lookout", ["Dónde queda el hotel", "Cuánto cuesta el tour"], "Dice What does lookout mean?"),
    ],
    [
        ml(R2, "¿Qué debe llevar el estudiante, además del equipo?", "Una toalla", ["Una botella", "Un balón"], "Dice A towel."),
        ml(R4, "¿Qué aclara la pregunta Do you mean the blue form or the green form?", "Cuál de los dos formularios necesita", ["En qué piso queda la oficina", "Cuánto cuesta el trámite"], "La funcionaria aclara que es el azul."),
        ml(R6, "¿De qué puerta sale el bus?", "De la siete", ["De la diecisiete", "De la setenta"], "Dice gate seven."),
    ],
    [
        mc("No sabes si dijeron fifteen o fifty. ¿Qué pregunta te permite distinguirlas?", "Sorry, did you say fifteen or fifty?", ["Sorry, what does fifteen mean?", "Sorry, where is the session?"], "Muestra qué dato dudas y ofrece las dos opciones."),
        mc("Quieres confirmar que la prueba es el lunes. ¿Qué frase sirve?", "So the test is on Monday. Is that right?", ["Could you speak more slowly, please?", "Sorry, could you tell me what test means?"], "Repite el dato y pide confirmación."),
        mc("Te dicen the viewpoint is at the end of the path (path = sendero) y no conoces viewpoint. ¿Qué preguntas?", "What does viewpoint mean?", ["Sorry, did you say the path or the park?", "So the end of the path is far, right?"], "Pides el significado de una palabra."),
    ],
    [
        ml(R1, "¿Por qué la pregunta del estudiante evita un error?", "Porque fifteen y fifty suenan parecido", ["Porque la recepcionista habló en voz baja", "Porque la sesión no existe"], "Distinguir -teen de -ty evita equivocarse con la hora."),
        ml(R4, "Un compañero dice que la funcionaria pidió el formulario verde. ¿Quién tiene razón?", "No: pidió el azul, no el verde", ["Sí: el verde es más importante", "Sí: pidió los dos formularios"], "La funcionaria aclara The blue one."),
    ],
    [
        ml(R5, "La profesora dice Exactly. ¿Qué significa para el estudiante?", "Que entendió correctamente el plazo", ["Que debe entregar hoy", "Que debe repetir la tarea"], "Exactly confirma lo que dijo el estudiante."),
        mc("Un estudiante dice So you are saying that the class is on Tuesday? ¿Qué estrategia usa?", "Confirmar lo que entendió", ["Pedir que hablen más despacio", "Pedir el significado de una palabra"], "Repite con sus palabras y espera confirmación."),
    ],
    [ml("«Clerk: The package arrives in three to four days. Customer: Sorry, did you say three or four? Clerk: Between three and four days, so Thursday or Friday. Customer: So Friday is the latest. Is that right? Clerk: Yes, exactly.» (clerk = empleado, package = paquete, arrives = llega, latest = lo más tarde)", "¿Qué dato confirma el cliente al final?", "Que el viernes es el último día posible", ["Que el paquete llega el jueves", "Que el paquete llegó ayer"], "Friday is the latest, y el empleado dice exactly.")],
    [
        ("En Inglés de 2.º medio (OA 4, clase 3): ¿cómo se pide repetición con cortesía?", "Sorry, could you repeat that, please?", "Es la fórmula más usada."),
        ("En Inglés de 2.º medio (OA 4, clase 3): ¿qué se agrega para confirmar lo que entendiste?", "Una pregunta como Is that right?", "Invita a quien habla a confirmar."),
        ("En Inglés de 2.º medio (OA 4, clase 3): ¿qué dices para saber qué significa una palabra?", "What does ... mean?", "Pide el significado."),
    ],
    task("Imagina esta situación: un adulto te dice «The meeting is at twelve fifteen in room nineteen» y tú no entiendes bien. Escribe tres frases en inglés: una para pedir repetición, una para distinguir dos números parecidos y una para confirmar. Luego el adulto lee tus frases y responde.", "Sorry, could you repeat that, please? Did you say nineteen or ninety? So the meeting is at twelve fifteen in room nineteen. Is that right?", ["usa tres frases de la clase", "distingue dos números parecidos", "confirma con una pregunta"], ["hoja con tres frases en inglés"], ["usar una sola frase para todo", "no repetir el dato al confirmar"], "Pide que lea las frases en voz alta y compruebe que suenan corteses."),
    "Escucha otra vez el diálogo del mirador y anota cómo se explicó la palabra lookout.",
    "Escribe en español tres momentos de tu semana en que te habría servido pedir que repitan algo.",
)

# ------------------------------------------------------------------ clase 4: inferencias con claves de contexto y pistas fonológicas
N1 = "«[Sound of cheering crowd] Number ten has the ball. [Fast, excited voice] She passes... she shoots... Oh, so close!» (cheering = vitoreando, crowd = multitud, passes = pasa, shoots = lanza, so close = por poco)"
N2 = "«[A teacher and a student, in an office] Student: I'm sorry, I didn't finish the report. Teacher: [slowly, low voice] I see. Student: I can bring it tomorrow. Teacher: [sighs] Tomorrow, then.» (report = informe, I see = ya veo, sighs = suspira, tomorrow = mañana)"
N3 = "«[On screen: a map with a red line from the school to a park] Today we walk to the park. [follows the red line with a finger] We go along the red line. It takes twenty minutes.» (on screen = en la pantalla, map = mapa, red line = línea roja, follows = sigue, along = a lo largo de)"
N4 = "«Really? [high voice, rising] You won the prize? That's wonderful! [laughing]» (really = ¿de veras?, won = ganaste, prize = premio, wonderful = maravilloso)"
N5 = "«Gardener: Water the plants once in the morning and once at night. [raises two fingers] Two a day. Not THREE, or the roots will rot.» (gardener = jardinera, water = riega, plants = plantas, roots = raíces, rot = pudrirse, a day = al día)"
N6 = "«Vendor: [in a loud, cheerful voice] Fresh bread! Fresh bread! Still warm! Customer: How much? Vendor: Two for a thousand pesos.» (vendor = vendedor, customer = cliente, fresh = fresco, warm = tibio, how much = cuánto cuesta)"

lesson(
    OA, 4, MAT_L,
    "Aprenderé a hacer inferencias al escuchar: deducir lo que no se dice usando el tema, los participantes, el apoyo visual, la entonación y el acento. Sirve para entender sentimientos, lugares y relaciones entre las personas.",
    ["Sé reconocer gestos y entonación.", "Conozco palabras de emociones como happy y angry."],
    [
        "Una inferencia (inference) es una idea que no se dice con palabras, pero se deduce de pistas. Las claves contextuales son el tema, los participantes (quién habla con quién), el lugar y el apoyo visual, como un mapa o una imagen en pantalla. Un sonido de multitud que aplaude indica un partido; una oficina con un profesor y un estudiante indica una conversación sobre una tarea.",
        "Las pistas fonológicas son la entonación y la acentuación. Una voz alta y rápida muestra emoción; una voz baja y lenta, seriedad o enojo; una voz que sube en una pregunta como Really? muestra sorpresa. La palabra que lleva más fuerza suele ser la importante. Un suspiro antes de Tomorrow, then muestra que el profesor acepta con desagrado.",
        "Para inferir, escribe dos pistas y la idea que deduces: Pista 1 + Pista 2 = inferencia. Comprueba que tu inferencia no contradice ninguna palabra del texto. Si hay dos posibles inferencias, elige la que tiene más pistas.",
    ],
    [("inference", "inferencia: idea deducida de pistas"), ("context clue", "clave del contexto"), ("participants", "participantes: quienes hablan"), ("visual support", "apoyo visual"), ("cheerful / excited", "alegre / emocionado"), ("sigh", "suspiro")],
    [
        ("Inferir el lugar y la situación", ADULT + N1 + " ¿Dónde está el hablante y cómo lo sabes?", ["Hay una multitud que vitorea.", "El hablante dice number ten has the ball y habla rápido.", "Es un partido y el hablante es un comentarista."], "En un partido; el sonido de la multitud y el relato rápido lo muestran"),
        ("Inferir un sentimiento", ADULT + N2 + " ¿Cómo se siente el profesor?", ["Habla despacio y con voz baja.", "Suspira antes de Tomorrow, then.", "Está molesto o decepcionado, aunque acepta la fecha."], "Molesto o decepcionado, aunque acepta la nueva fecha"),
    ],
    [
        ("Inferir algo que contradice las palabras.", "Se inventa una idea sin pistas.", "Escribe las pistas y comprueba que no choquen con el texto."),
        ("Pensar que una pregunta con voz alta siempre es enojo.", "La voz alta en Really? muestra sorpresa, no enojo.", "Junta la entonación con el contexto y las palabras."),
    ],
    [
        ml(N4, "¿Cómo se siente el hablante?", "Sorprendido y contento", ["Enojado y decepcionado por la noticia", "Aburrido y cansado de esperar"], "Really? sube y That's wonderful lo confirman."),
        ml(N6, "¿Dónde ocurre el texto?", "En una feria o mercado", ["En una oficina", "En una biblioteca"], "Un vendedor ofrece pan fresco en voz alta."),
        ml(N3, "¿Qué muestra la línea roja de la pantalla?", "El camino del colegio al parque", ["La hora a la que llegará el curso", "El nombre del parque y de las calles"], "El hablante la sigue con el dedo."),
    ],
    [
        ml(N1, "¿Cómo se sienten las personas de la multitud?", "Emocionadas", ["Aburridas", "Asustadas"], "Cheering y a fast excited voice muestran emoción."),
        ml(N2, "¿Qué relación tienen los dos hablantes?", "Un docente y un estudiante", ["Dos hermanos que hablan de su casa", "Un cliente y un vendedor"], "Hablan de un informe en una oficina."),
        ml(N5, "¿Qué muestra el gesto de levantar dos dedos?", "Que se riega dos veces al día", ["Que se riega tres veces al día", "Que se riega una vez al día"], "Two a day coincide con el gesto."),
    ],
    [
        ml(N5, "¿Qué pista muestra que la jardinera corrige una idea posible?", "Dice Not THREE con énfasis", ["Dice Water the plants en la mañana", "Dice Two a day sin cambiar la voz"], "Not three corrige un posible error."),
        ml(N3, "¿Cuánto durará el recorrido y qué pista del audio lo dice?", "Veinte minutos; lo dice el hablante", ["Diez minutos; lo muestra el mapa", "Una hora; lo muestra la línea roja"], "El dato viene en palabras; el mapa solo muestra el camino."),
        ml(N6, "¿Cuántos panes cuestan mil pesos?", "Dos", ["Uno", "Cuatro"], "Dice two for a thousand pesos."),
    ],
    [
        ml(N2, "Un compañero dice que el profesor está muy contento. ¿Qué pistas lo contradicen?", "La voz baja y lenta, y el suspiro", ["La palabra report", "La palabra tomorrow"], "Esas pistas fonológicas muestran decepción."),
        ml(N6, "Un oyente dice que el vendedor está triste. ¿Qué pistas lo contradicen?", "La voz alegre y fuerte", ["El precio de dos panes por mil pesos", "La palabra warm, que habla de calor"], "La voz cheerful contradice la tristeza."),
    ],
    [
        ml(N1, "¿Qué dos pistas muestran que el partido está cerca de un gol?", "She shoots y Oh, so close, dichas rápido", ["Que hay una multitud que vitorea en el estadio", "Que el número diez tiene la pelota en sus pies"], "Son las palabras y la voz que anuncian un casi gol."),
        ml(N4, "Si en lugar de voz alta el hablante dijera Really? con voz plana y baja, ¿qué inferirías?", "Que no está tan sorprendido; quizá duda", ["Que está todavía más sorprendido que antes", "Que está muy emocionado, aunque hable bajo"], "El tono plano cambia la intención."),
    ],
    [ml("«[At a bus stop] Woman: [looks at her watch, voice tense] Twenty minutes late. [shakes head] Again.» (late = atrasado, watch = reloj, tense = tensa, again = otra vez)", "¿Cómo se siente la mujer y qué pistas lo muestran?", "Molesta: mira el reloj y dice Again", ["Contenta, porque el bus llegó antes de hora", "Tranquila, porque mira el reloj por costumbre"], "Mirar el reloj, voz tensa y Again muestran molestia.")],
    [
        ("En Inglés de 2.º medio (OA 4, clase 4): ¿qué es una inferencia?", "Una idea deducida de pistas, no dicha con palabras", "Se apoya en contexto y voz."),
        ("En Inglés de 2.º medio (OA 4, clase 4): ¿qué pistas del sonido ayudan a inferir sentimientos?", "La entonación y el acento de las palabras", "La voz muestra emociones."),
        ("En Inglés de 2.º medio (OA 4, clase 4): ¿qué apoyo visual puede ayudarte a entender un recorrido?", "Un mapa", "Muestra el camino que se explica."),
    ],
    task("Un adulto lee dos veces: «[In a classroom, noisy] Teacher: [claps twice, loud voice] Quiet, please! [Silence] Thank you. [soft voice] Today we have a visitor. [points to a woman at the door] This is Ms. Prado, a nurse.» (noisy = ruidosa, claps = aplaude, loud = fuerte, silence = silencio, soft = suave, visitor = visita, nurse = enfermera). Anota dos inferencias y las pistas que las apoyan.", "Inferencia 1: la clase estaba desordenada; pistas: noisy y el aplauso con voz fuerte. Inferencia 2: los estudiantes obedecen al profesor; pista: Silence después de Quiet, please.", ["escribe dos inferencias", "cada inferencia lleva una pista del audio", "no contradice el texto"], ["hoja con dos inferencias y pistas"], ["dar una inferencia sin pista", "contradecir lo dicho"], "Pide que cambie una pista y explique cómo cambiaría la inferencia."),
    "Escucha otra vez el audio del partido y anota dos pistas sonoras que muestran emoción.",
    "Observa a alguien en una escena de película sin sonido y escribe qué infieres de sus gestos.",
)

# ------------------------------------------------------------------ clase 5: tomar notas, resumir y preguntar para confirmar
Q1 = "«Good morning. Today I will talk about three ways to study better. First, plan your week: write what you must do each day. Second, take short breaks: study for forty minutes and rest for ten. Third, review at night: read your notes for five minutes before sleeping. In short, plan, rest and review.» (ways = formas, plan = planifica, take short breaks = haz descansos cortos, review = repasa, notes = apuntes, rest = descansar)"
Q2 = "«Our class trip will be on the twenty-second of June. We will go to the science center by train. The train leaves at eight fifteen from Central Station. Please bring lunch, a jacket and a signed permission form. The cost is six thousand pesos.» (class trip = paseo, science center = centro científico, by train = en tren, signed = firmada, permission form = autorización, cost = costo)"
Q3 = "«Hello. I am Nina, and I want to tell you about my summer job. I worked at an ice cream stand near the beach. The hardest part was the long line, because many people came at noon. The best part was meeting people from other countries. Next summer, I will do it again.» (summer job = trabajo de verano, ice cream stand = puesto de helados, hardest = lo más difícil, line = fila, noon = mediodía, again = otra vez)"

lesson(
    OA, 5, MAT_L,
    "Aprenderé a tomar notas de lo que escucho, a resumir algunas ideas con apoyo y a preguntar para confirmar mi comprensión. Sirve para recordar un audio y para comprobar que entendí bien.",
    ["Sé escuchar con un propósito.", "Sé pedir repetición y confirmar."],
    [
        "Tomar notas (note-taking) no es escribir todo: es anotar palabras clave. Usa abreviaturas y símbolos: 1, 2, 3 para pasos, una flecha para consecuencia, una estrella para lo importante y números con cifras. Para el audio de las tres formas de estudiar mejor, las notas podrían ser: 3 ways: 1 plan week, 2 breaks 40/10, 3 review night 5 min. Esas notas tienen pocas palabras y todos los datos.",
        "Un resumen (summary) usa tus notas para decir lo esencial con tus palabras en una o dos oraciones. Con apoyo, puedes usar una plantilla: The speaker explains... First,... Second,... Third,... Evita copiar frases completas y agrega solo las ideas más importantes. Después de resumir, confirma lo que entendiste con preguntas como Did you say forty minutes? o So the third way is to review at night, right?",
        "Para confirmar predicciones, compara tus notas con lo que anticipaste al comienzo. Marca con un tic las que se cumplieron y corrige las que no. Si quedan dudas, pregunta a quien habla o vuelve a escuchar.",
    ],
    [("note-taking", "tomar notas"), ("abbreviation", "abreviatura"), ("summary", "resumen"), ("The speaker explains...", "El hablante explica..."), ("confirm", "confirmar"), ("review", "repasar")],
    [
        ("Notas con palabras clave", ADULT + Q1 + " ¿Cuáles serían unas buenas notas?", ["Busco el número de ideas: 3 ways.", "Anoto cada una con palabra clave: plan week, breaks 40/10, review night 5 min.", "No escribo oraciones completas."], "3 ways: plan week; breaks 40/10; review night 5 min"),
        ("Resumir con apoyo", ADULT + Q2 + " Resume el aviso en dos oraciones con The speaker explains...", ["Tomo los datos de las notas: fecha, medio, hora, qué llevar, costo.", "Uno los datos más importantes en dos oraciones.", "Uso mis palabras."], "The speaker explains that the class trip is on June 22 and the train leaves at 8:15. We must bring lunch, a jacket and a signed form, and it costs 6,000 pesos."),
    ],
    [
        ("Escribir todas las palabras del audio.", "No hay tiempo y se pierde la idea.", "Anota solo palabras clave, números y símbolos."),
        ("Hacer un resumen con todos los detalles.", "Un resumen debe ser corto y esencial.", "Elige solo lo más importante y usa tus palabras."),
    ],
    [
        ml(Q1, "¿Cuántas formas de estudiar mejor explica el hablante?", "Tres", ["Dos", "Cinco"], "Dice three ways."),
        ml(Q2, "¿A qué hora sale el tren?", "A las 8:15", ["A las 8:50", "A las 6:15"], "Dice eight fifteen."),
        mc("En las notas, ¿qué símbolo sirve para marcar lo más importante?", "Una estrella", ["Una flecha, que indica una consecuencia", "Un número, que indica un paso"], "Una estrella resalta sin gastar tiempo."),
    ],
    [
        ml(Q3, "¿Qué fue lo más difícil del trabajo de Nina?", "La fila larga del mediodía", ["Conocer personas de otros países", "El calor de la playa"], "Dice The hardest part was the long line."),
        ml(Q1, "¿Cuánto se debe estudiar y cuánto descansar?", "Cuarenta minutos y diez minutos", ["Diez minutos y cuarenta minutos", "Cuarenta minutos y cuatro minutos"], "Dice study for forty minutes and rest for ten."),
        ml(Q2, "¿Cuál es el costo del paseo?", "6.000 pesos", ["16.000 pesos", "600 pesos"], "Dice six thousand pesos."),
    ],
    [
        ml(Q3, "¿Cuál resume mejor el texto?", "Nina trabajó en un puesto de helados, lo más difícil fue la fila y lo mejor, conocer gente", ["Nina trabajó en un banco cerca de la playa; lo más difícil fue la fila y lo mejor, el sueldo", "Nina trabajó en un puesto de helados; no volverá el próximo verano porque la fila era muy larga"], "El resumen incluye lugar, dificultad y lo mejor."),
        ml(Q1, "Elige las mejores notas para el segundo consejo.", "2 short breaks: 40 min study, 10 rest", ["2 Second, take short breaks and you will feel better with them", "2 plan"], "Son breves y tienen los datos."),
        ml(Q2, "Quieres confirmar la fecha del paseo. ¿Qué pregunta haces?", "So the trip is June twenty-second, right?", ["So the trip is on June twelfth. Is that right?", "Sorry, what does the word trip mean?"], "Repites el dato y pides confirmación."),
    ],
    [
        ml(Q3, "Una compañera anota: «Nina worked at a bank». ¿Qué debe corregir?", "Debe anotar ice cream stand", ["Debe anotar su edad y su apellido", "Debe anotar el nombre de la playa"], "El texto dice ice cream stand."),
        ml(Q1, "Predijiste que el hablante hablaría de comprar libros nuevos. ¿Se confirma?", "No: habla de planificar, descansar y repasar", ["Sí: dice que hay que comprar libros nuevos", "Sí: dice que hay que comprar un cuaderno"], "Las tres formas del texto no incluyen comprar nada."),
    ],
    [
        ml(Q2, "Una familia debe llevar tres cosas. ¿Qué dos faltan si ya compró el almuerzo?", "La chaqueta y la autorización firmada", ["La toalla y el mapa", "El dinero y la linterna"], "El texto pide lunch, jacket y signed permission form."),
        arith(ADULT + Q2 + " Tres estudiantes van al paseo. ¿Cuántos pesos pagan en total?", "3*6000", "Se multiplica el costo de un estudiante por tres.", " pesos"),
    ],
    [ml(Q3, "Escribe en tu resumen una frase sobre el futuro de Nina. ¿Qué dato usas?", "Que el próximo verano lo hará otra vez", ["Que dejará de trabajar", "Que viajará a otro país"], "Dice Next summer, I will do it again.")],
    [
        ("En Inglés de 2.º medio (OA 4, clase 5): ¿qué se anota al tomar notas?", "Palabras clave, números y símbolos", "No se escriben oraciones completas."),
        ("En Inglés de 2.º medio (OA 4, clase 5): ¿qué es un resumen?", "Lo esencial dicho con tus palabras", "Es corto y no copia todo."),
        ("En Inglés de 2.º medio (OA 4, clase 5): ¿qué haces después de resumir para asegurarte?", "Preguntas para confirmar", "Por ejemplo, Is that right?"),
    ],
    task("Un adulto lee dos veces: «Today I will explain how to prepare for an interview. First, learn about the company: read its website. Second, practice three answers aloud. Third, arrive ten minutes early. Finally, send a thank-you message the same day.» (interview = entrevista de trabajo, company = empresa, website = sitio web, aloud = en voz alta, thank-you message = mensaje de agradecimiento). Toma notas con números y palabras clave, y escribe un resumen de dos oraciones.", "Notas: 1 learn company/web; 2 practice 3 answers; 3 arrive 10 min early; 4 thank-you same day. Resumen: The speaker explains how to prepare for an interview. There are four steps: learn about the company, practice answers, arrive early and send a thank-you message.", ["notas con números y palabras clave", "resumen de dos oraciones con sus palabras", "incluye todos los pasos"], ["hoja con notas y resumen"], ["copiar frases completas", "olvidar un paso"], "Pide que cambie un paso por otro y rehaga el resumen en una oración."),
    "Escucha otra vez el texto del estudio y escribe unas notas de cinco palabras.",
    "Elige un video corto en español y toma notas de tres palabras clave con un símbolo cada una.",
)
