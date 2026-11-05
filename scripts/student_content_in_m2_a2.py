"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 02: expresiones clave, collocations, conectores y sonidos.

Las «escuchas» las lee un adulto: el guion va escrito en el enunciado. Inglés americano. El OA escribe «sonido /o/ (usually)»:
el sonido real de usually es /ʒ/ (como en television); se trabaja ese sonido. Los títulos de clase del plan son genéricos;
aquí se aplican a expresiones idiomáticas, collocations y vocabulario temático, conectores, sonidos iniciales y acento.
"""
from __future__ import annotations

from in_m2_common import MAT_L, arith, lesson, mc, ml, mr, task

OA = "IN2M OA 02"

# ------------------------------------------------------------------ clase 1: expresiones idiomáticas y de uso frecuente
W1 = "«Tomorrow is the first day of the pottery workshop, and nobody knows anyone. The teacher tells a joke to break the ice. Soon everyone is laughing.» (pottery workshop = taller de cerámica, nobody = nadie, joke = chiste, laughing = riendo)"
W2 = "«Mateo: How was the history quiz? Elena: It was a piece of cake! I finished in ten minutes.» (quiz = prueba corta, finished = terminé)"
T3 = "«We painted the fence all afternoon. At six o'clock, Dad looked at the sky and said, Let's call it a day. We can finish tomorrow.» (fence = cerca, painted = pintamos, sky = cielo)"
T4 = "«My cousin lives in Canada, so I see him once in a blue moon. The last time was three years ago.» (cousin = primo, last time = la última vez)"
T5 = "«Please keep an eye on my bag while I buy the tickets. I will be back in two minutes.» (bag = bolso, tickets = entradas, back = de vuelta)"
T6 = "«The team had many ideas, so the captain said, Let's make sure we are on the same page before we start.» (team = equipo, captain = capitana, ideas = ideas, before = antes de)"
T7 = "«The new sports hall opens in March. I am looking forward to it because the old one is very small.» (sports hall = gimnasio, opens = abre, small = pequeño)"
T9 = "«Mateo: How was the crossword puzzle? Lucía: It was a piece of cake for my brother, but really hard for me.» (crossword puzzle = crucigrama, hard = difícil)"
T10 = "«Ana: I can't decide between the two jackets. Bea: Take your time, but make up your mind soon. The store closes at eight.» (jackets = chaquetas, take your time = tómate tu tiempo, store = tienda, closes = cierra)"
T11 = "«Diego: Are you going to the school dance? Tina: Maybe. I have to give it a try before I say no.» (dance = baile, maybe = tal vez, say no = decir que no)"
T12 = "«Leo: I am usually shy, but today I broke the ice with a new classmate. Then the teacher said it was time to call it a day, so we left the room.» (shy = tímido, classmate = compañero de curso, left = salimos de)"
T13 = "«Ema: My cousins visit us once in a blue moon, so I am looking forward to this weekend. Mom said we should keep an eye on the little ones, and Dad said, Let's be on the same page: nobody goes near the street.» (cousins = primos, little ones = los pequeños, nobody = nadie, street = calle)"
T14 = "«Coach: Great practice, everyone! We worked hard, so let's call it a day. Next week I am looking forward to seeing you all at the tournament.» (practice = entrenamiento, worked hard = trabajamos duro, tournament = torneo)"

lesson(
    OA, 1, MAT_L,
    "Aprenderé a reconocer al escuchar nueve expresiones frecuentes (por ejemplo break the ice y a piece of cake) y a entender su sentido en el contexto, sin traducirlas palabra por palabra. Sirve para no perder el significado cuando alguien habla de forma natural.",
    ["Sé reconocer frases clave por el contexto.", "Conozco expresiones como hardly ever y a lot of."],
    [
        "Una expresión idiomática (idiom) es un grupo de palabras cuyo significado no sale de traducir cada palabra. Break the ice significa romper el hielo: empezar una conversación entre personas que no se conocen. A piece of cake significa muy fácil. Call it a day significa terminar el trabajo por hoy. Once in a blue moon significa muy rara vez. Keep an eye on es vigilar o cuidar algo. Be on the same page es entender y acordar lo mismo.",
        "Otras tres expresiones frecuentes son look forward to, make up your mind y give it a try. Look forward to significa esperar algo con ganas y va con un sustantivo o con un verbo en -ing: I look forward to the trip. Make up your mind significa decidirse. Give it a try significa intentarlo. Una frase de uso frecuente se aprende como un bloque, igual que Take your time.",
        "Cuando oyes una expresión nueva, no traduzcas cada palabra. Fíjate en la situación, en lo que se dice antes y después, y en el tono de la voz. Pregúntate qué quiere lograr quien habla. Si el significado literal no tiene sentido en la situación, probablemente es una expresión idiomática.",
    ],
    [("break the ice", "romper el hielo"), ("a piece of cake", "muy fácil"), ("call it a day", "terminar por hoy"), ("once in a blue moon", "muy rara vez"), ("keep an eye on", "vigilar"), ("be on the same page", "estar de acuerdo, entender lo mismo"), ("look forward to", "esperar con ganas"), ("make up your mind / give it a try", "decidirse / intentarlo")],
    [
        ("Entender una expresión por el contexto", "Un adulto lee en voz alta (tapa el guion): " + W1 + " ¿Qué hace el profesor al contar un chiste?", ["Nadie se conoce el primer día.", "El profesor cuenta un chiste para break the ice.", "Esa expresión significa empezar la conversación entre personas que no se conocen."], "Rompe el hielo: ayuda a que las personas empiecen a conversar"),
        ("Una expresión sobre dificultad", "Un adulto lee en voz alta (tapa el guion): " + W2 + " ¿Cómo fue la prueba para Elena?", ["Busco la expresión: a piece of cake.", "Significa muy fácil.", "Lo confirma que terminó en diez minutos."], "Muy fácil"),
    ],
    [
        ("Traducir a piece of cake como un trozo de torta y pensar que hablan de comida.", "Se traduce palabra por palabra y no se mira el contexto: están hablando de una prueba.", "Pregúntate si el sentido literal tiene lógica en la situación; si no, es un idiom."),
        ("Pensar que once in a blue moon significa que ocurre cuando la luna es azul.", "Es una expresión fija: no habla de la luna real.", "Aprende el bloque completo: significa muy rara vez."),
    ],
    [
        ml(T3, "¿Qué quiere decir el papá con Let's call it a day?", "Terminar el trabajo por hoy", ["Llamar por teléfono durante el día", "Pintar todo el día siguiente"], "Dice que pueden terminar mañana: se detienen ahora."),
        ml(T4, "¿Cada cuánto ve el hablante a su primo?", "Muy rara vez", ["Cada vez que hay luna llena", "Todos los meses"], "Once in a blue moon es muy rara vez; la última vez fue hace tres años."),
        ml(T5, "¿Qué le pide el hablante a su amigo con keep an eye on?", "Que vigile su bolso", ["Que mire una sola cosa con un ojo", "Que compre las entradas"], "Keep an eye on es vigilar; el hablante va a comprar entradas."),
    ],
    [
        ml(T9, "¿Para quién fue muy fácil el crucigrama y para quién difícil?", "Fácil para su hermano, difícil para Lucía", ["Fácil para Lucía, difícil para su hermano", "Difícil para los dos, aunque se rieron"], "A piece of cake for my brother: fácil para él; really hard for me: difícil para Lucía."),
        mc("Un grupo no se conoce y quiere empezar a conversar. ¿Qué expresión describe el primer paso?", "break the ice", ["call it a day", "once in a blue moon"], "Break the ice es empezar la conversación; las otras dos no sirven para eso."),
        ml(T7, "¿Cómo se siente el hablante sobre el nuevo gimnasio?", "Con ganas de que abra", ["Preocupado porque abre en marzo", "Mirando hacia adelante el frente del gimnasio"], "Looking forward to significa esperar algo con ganas."),
    ],
    [
        ml(T6, "¿Qué quiere lograr la capitana con on the same page?", "Que todos entiendan y acuerden el plan", ["Que todos lean el mismo libro", "Que cada uno trabaje solo"], "Be on the same page es compartir el mismo entendimiento."),
        ml(T10, "Bea dice make up your mind. ¿Qué le pide a Ana?", "Que se decida pronto", ["Que cambie de tienda", "Que pruebe las dos chaquetas más tarde"], "Make up your mind es decidirse; la tienda cierra a las ocho."),
        ml(T11, "¿Qué hará Tina antes de decir que no?", "Intentar ir al baile", ["Pedir permiso para no ir", "Preguntarle a Diego si va"], "Give it a try es intentarlo antes de decir que no."),
    ],
    [
        ml(T12, "¿Qué dos hechos cuenta Leo, en orden?", "Empezó una conversación con alguien nuevo; luego terminaron la clase por hoy", ["Terminó la clase por hoy; luego empezó una conversación con alguien nuevo", "Cambió de sala; luego se quedó solo"], "Broke the ice va primero; call it a day va después con Then."),
        mr("Julia dice: «I see my best friend every day at school, so I see her once in a blue moon.»", "¿Por qué está mal usada la expresión?", "Porque once in a blue moon significa muy rara vez y ella ve a su amiga todos los días", ["Porque once in a blue moon significa todos los días y debería ir en pasado", "Porque en inglés esa expresión no se puede usar con amigos del colegio"], "La frase se contradice: every day y muy rara vez no pueden ir juntos."),
    ],
    [
        ml(T13, "¿Cuál afirmación es verdadera?", "Los primos visitan muy rara vez y la familia acordó una regla de seguridad", ["Los primos visitan todos los fines de semana y nadie cuida a los pequeños", "Los primos viven cerca y la familia no acordó ninguna regla"], "Once in a blue moon indica pocas visitas; keep an eye on y on the same page muestran el cuidado y el acuerdo."),
        ml("«Pablo: Are you going to join the photography club? Eva: I don't know. I never tried before. Pablo: Give it a try, it's free on Monday. Eva: Okay, I will make up my mind after I see the room.» (photography = fotografía, free = gratis, room = sala)", "¿Qué decide Eva por ahora?", "Verá la sala y luego se decidirá", ["Entrar al club sin ver la sala", "No intentar nunca más"], "Make up my mind after significa que se decidirá después de ver la sala."),
    ],
    [ml(T14, "¿Qué hace la entrenadora y qué espera?", "Termina el entrenamiento por hoy y espera con ganas el torneo", ["Empieza el entrenamiento y teme el torneo", "Termina el torneo y espera el próximo entrenamiento"], "Call it a day cierra la sesión y looking forward to muestra ganas del torneo.")],
    [
        ("En Inglés de 2.º medio (OA 2, clase 1): ¿qué significa break the ice?", "Romper el hielo: empezar una conversación", "Es un idiom, no se traduce palabra por palabra."),
        ("En Inglés de 2.º medio (OA 2, clase 1): ¿qué significa call it a day?", "Terminar el trabajo por hoy", "Se usa cuando se deja una tarea para continuar otro día."),
        ("En Inglés de 2.º medio (OA 2, clase 1): ¿cómo conviene entender una expresión nueva al escuchar?", "Usando la situación y lo que se dice antes y después, no palabra por palabra", "El contexto da el sentido de un idiom."),
    ],
    task("Un adulto lee dos veces: «Paula: I want to learn the guitar, but I am afraid. Her friend: Give it a try! It will be a piece of cake after two weeks. Paula: I look forward to my first song. Friend: Let's keep an eye on your progress every Friday.» (guitar = guitarra, afraid = con miedo, progress = progreso, Friday = viernes). Anota tres expresiones que oíste y qué significan.", "Give it a try: intentarlo. A piece of cake: muy fácil. Look forward to: esperar con ganas. Keep an eye on: vigilar o seguir de cerca.", ["anota tres expresiones del texto", "explica cada una en español con sus palabras", "usa el contexto, no la traducción palabra por palabra"], ["hoja con tres expresiones y su significado"], ["traducir palabra por palabra", "anotar palabras sueltas que no son expresiones"], "Pide que explique en una frase qué quiere lograr Paula y que relacione cada expresión con esa meta."),
    "Escucha otra vez el texto del taller de cerámica y anota qué dice el profesor para romper el hielo.",
    "Escribe en español una situación de tu vida donde usarías call it a day y otra donde usarías break the ice.",
)

# ------------------------------------------------------------------ clase 2: collocations y vocabulario temático
C1 = "«At the lake, Amelia took a photo of the mountain. Later, she made a mistake and deleted it by accident.» (lake = lago, deleted = borró, by accident = sin querer)"
C2 = "«Passengers for flight 207, please go to gate twelve. Have your boarding pass and passport ready. The flight has a short delay, and your luggage will arrive later.» (passengers = pasajeros, gate = puerta de embarque, boarding pass = tarjeta de embarque, passport = pasaporte, delay = retraso, luggage = equipaje)"
C3 = "«Pablo: I need to save time this week. Rosa: Then take a break from your phone and do your homework first. Pablo: Good idea, I will make progress faster.» (save = ahorrar, break = descanso, progress = avance)"
C4 = "«Mr. Soto speaks fast, so please pay attention. If you have a question, raise your hand. Now let's have a look at the first page.» (raise = levanta, page = página)"
C5 = "«We ate fast food at the airport because we had a short break between flights. There was heavy traffic on the way, so we were tired.» (airport = aeropuerto, between = entre, traffic = tráfico, tired = cansados)"
C6 = "«Jana had to make a decision: stay home or go to the airport. She did research on the delay and paid attention to the announcements.» (research = investigación, delay = retraso, announcements = avisos por altavoz)"
WA = "«Before we choose a hotel, we must do some research. Then we will make a decision together.» (hotel = hotel, choose = elegir, together = juntos)"
WB = "«The weather report says heavy rain tomorrow, so please pay attention to the signs on the road.» (weather report = pronóstico del tiempo, signs = señales, road = camino)"

lesson(
    OA, 2, MAT_L,
    "Aprenderé a reconocer collocations (combinaciones de palabras que suelen ir juntas, como make a decision) y vocabulario temático del aeropuerto, y a entenderlas al escuchar. Sirve para hablar y escuchar en inglés de forma natural.",
    ["Sé que make y do aparecen en frases cotidianas.", "Conozco palabras de viajes como bus y ticket."],
    [
        "Una collocation es una combinación de palabras que en inglés suenan naturales juntas. Con make se dice make a decision, make a mistake, make progress y make friends. Con do se dice do homework y do research. Con take se dice take a photo, take a break y take a trip. También se dice make a plan. También hay pay attention, have a look, save time, heavy rain, heavy traffic y fast food. En español a veces usamos otro verbo, por eso no conviene traducir palabra por palabra.",
        "El vocabulario temático son las palabras de un tema. En un aeropuerto se oyen flight (vuelo), gate (puerta de embarque), boarding pass (tarjeta de embarque), passport (pasaporte), luggage (equipaje) y delay (retraso). Cuando conoces el tema, anticipas las palabras que van a aparecer y entiendes mejor los avisos.",
        "Al escuchar, atiende al verbo y al sustantivo juntos. Si oyes took a, espera photo, break o trip; si oyes heavy, espera rain o traffic. Anota la combinación completa, no solo una palabra, y apréndela como un bloque.",
    ],
    [("collocation", "combinación frecuente de palabras"), ("make a decision / a mistake", "tomar una decisión / cometer un error"), ("do research / homework", "investigar / hacer la tarea"), ("take a photo / a break", "sacar una foto / descansar"), ("pay attention / have a look", "prestar atención / echar un vistazo"), ("boarding pass / luggage / delay", "tarjeta de embarque / equipaje / retraso")],
    [
        ("Verbo y sustantivo juntos", "Un adulto lee en voz alta (tapa el guion): " + WA + " ¿Qué verbos acompañan a research y a decision?", ["Busco los dos grupos: do some research y make a decision.", "Research se combina con do.", "Decision se combina con make."], "Do research y make a decision"),
        ("Adjetivo y sustantivo juntos", "Un adulto lee en voz alta (tapa el guion): " + WB + " ¿Qué dos collocations aparecen?", ["Busco un adjetivo con sustantivo: heavy rain.", "Busco un verbo con sustantivo: pay attention.", "Las dos se aprenden como bloque."], "Heavy rain y pay attention"),
    ],
    [
        ("Decir do a photo porque en español se dice hacer una foto.", "Se traduce el verbo del español; en inglés se combina take con photo.", "Aprende la combinación completa: take a photo."),
        ("Decir strong rain por lluvia fuerte.", "Rain se combina con heavy; strong va con wind o coffee.", "Memoriza heavy rain como bloque."),
    ],
    [
        ml(C1, "¿Qué verbo se usa con photo en el texto?", "took (took a photo)", ["made (made a photo)", "did (did a photo)"], "En inglés se dice take a photo; make y do no se combinan con photo."),
        mc("¿Qué combinación es natural en inglés?", "make a mistake", ["do a mistake", "take a mistake"], "Con mistake se usa make."),
        mc("¿Qué adjetivo se combina de forma natural con rain?", "heavy", ["big", "high"], "Heavy rain es la combinación fija para lluvia fuerte."),
    ],
    [
        ml(C3, "¿Qué collocation del diálogo significa ahorrar tiempo?", "save time", ["take a break", "make progress"], "Save time es ahorrar tiempo; take a break es descansar."),
        ml(C2, "¿Qué documento se muestra para subir al avión?", "boarding pass", ["luggage", "delay"], "La tarjeta de embarque es boarding pass; luggage es el equipaje."),
        ml(C4, "¿Qué combinación significa echar un vistazo?", "have a look", ["pay attention", "raise your hand"], "Have a look es mirar rápido; pay attention es concentrarse."),
    ],
    [
        mc("Elige el verbo correcto: We must ____ a decision before Friday.", "make", ["do", "put"], "Decision va con make."),
        ml(C5, "¿Qué combinación explica por qué estaban cansados?", "heavy traffic", ["fast food", "short break"], "Heavy traffic aparece con so we were tired."),
        mc("Elige la palabra correcta: My flight leaves in an hour, so I have to go to the ____.", "gate", ["luggage", "passport"], "Se va al gate; el pasaporte y el equipaje no son lugares."),
    ],
    [
        mr("Sam escribe: «I did a decision and I made my homework.»", "¿Qué corrección es la correcta?", "I made a decision and I did my homework", ["I took a decision and I took my homework", "I did a decision and I did my homework"], "Decision va con make y homework con do."),
        mc("Tomás dice: «En inglés se dice do a photo». Julia dice: «Se dice take a photo». ¿Quién tiene razón y por qué?", "Julia, porque la combinación natural es take a photo", ["Tomás, porque do significa hacer siempre", "Ninguno, porque no hay verbo para photo"], "Las collocations no siguen la traducción del español."),
    ],
    [
        ml(C6, "¿Qué dos acciones hizo Jana para decidir?", "Investigó el retraso y prestó atención a los avisos", ["Compró un pasaje nuevo y llamó a su casa", "Sacó fotos del aeropuerto y esperó en la puerta"], "Did research y paid attention son sus dos acciones."),
        mr("Carla escribe: «We had a long delay. We did friends with other passengers and played cards.» (delay = retraso, passengers = pasajeros, cards = cartas)", "¿Qué combinación hay que corregir?", "did friends por made friends", ["long delay por big delay", "played cards por made cards"], "Friends se combina con make."),
    ],
    [ml("«Attention, passengers on flight 305. There is a delay of forty minutes. Please keep your boarding pass and passport with you, and pay attention to the screens. Your luggage will arrive at belt four.» (screens = pantallas, belt = cinta)", "¿Qué debe hacer un pasajero?", "Conservar sus documentos y mirar las pantallas", ["Ir a casa y volver mañana a la misma hora", "Dejar el equipaje en la puerta y esperar sin mirar"], "El aviso pide keep your boarding pass y pay attention to the screens.")],
    [
        ("En Inglés de 2.º medio (OA 2, clase 2): ¿qué es una collocation?", "Una combinación de palabras que suelen ir juntas", "Se aprende como bloque."),
        ("En Inglés de 2.º medio (OA 2, clase 2): ¿qué verbo va con decision: make o do?", "make", "Make a decision es la combinación natural."),
        ("En Inglés de 2.º medio (OA 2, clase 2): ¿cómo se dice ahorrar tiempo en inglés?", "save time", "Es la combinación fija con save."),
    ],
    task("Un adulto lee dos veces: «This weekend I will take a trip to the coast. First, I need to do some research about the bus times. Then I will make a plan and pay attention to the weather.» (trip = viaje, coast = costa, bus times = horarios de bus, plan = plan). Anota cuatro collocations que oíste.", "Take a trip, do research, make a plan, pay attention.", ["anota cuatro combinaciones verbo más sustantivo", "escribe el verbo y el sustantivo juntos", "no repite la misma combinación"], ["hoja con cuatro combinaciones"], ["anotar solo el verbo", "escribir palabras sueltas sin su pareja"], "Pide que invente una oración con una de las combinaciones y la compare con la del texto."),
    "Escucha otra vez el aviso del aeropuerto y anota las palabras del tema que oyes.",
    "Escribe en español tres combinaciones que usas en tu casa y piensa cómo se dirían en inglés con make, do o take.",
)

# ------------------------------------------------------------------ clase 3: conectores
CT1 = "«Neither the rain nor the wind stopped the tennis players. The match was long, though. As a result, the final started late.» (tennis players = tenistas, match = partido, long = largo, final = final)"
CT2 = "«Nico: Which club will you choose? Eva: I will either join the photography club or the choir. I will decide as soon as I see the schedule. I won't join unless the meetings are on Tuesdays.» (choose = elegir, choir = coro, schedule = horario, meetings = reuniones)"
K1 = "«Neither Carla nor her brothers are at home today. They are at the beach, so the house is quiet.» (beach = playa, quiet = silenciosa)"
K2 = "«Neither my sister nor I like loud music, so we either read or draw on Sundays.» (loud = fuerte, read = leemos, draw = dibujamos)"
K3 = "«The planetarium is free on Sundays, though the line is usually long. We will arrive at nine unless the bus is late.» (planetarium = planetario, line = fila, bus = bus)"
K4 = "«It rained all morning. As a result, the soccer field was too muddy, and the game was moved to Saturday. The players were disappointed, though.» (soccer field = cancha de fútbol, muddy = embarrada, moved = cambiado, disappointed = decepcionados)"
K5 = "«Mario: I want to tell the others about the trip. Lía: Please don't, unless the teacher says yes. I will send you the list as soon as she answers.» (trip = paseo, others = los demás, list = lista, answers = responde)"
K6 = "«Tickets for the show are either nine thousand or twelve thousand pesos, depending on the seat. Students pay half the price, unless the seat is in the front row.» (tickets = entradas, depending on = según, seat = asiento, half = la mitad, front row = primera fila)"
K7 = "«Teacher: You can either bring a photo or a drawing. Neither a video nor a song is accepted, though. You will get zero points unless you deliver on Friday.» (drawing = dibujo, accepted = aceptado, deliver = entregar)"
K8 = "«The astronomy night is tomorrow. Neither clouds nor rain is expected, so we will see the stars. The telescope is free, though you must book it. As a result, the club asks you to call as soon as possible.» (astronomy = astronomía, expected = esperado, stars = estrellas, telescope = telescopio, book = reservar)"

lesson(
    OA, 3, MAT_L,
    "Aprenderé a reconocer al escuchar los conectores neither...nor, either...or, though, unless, as soon as y as a result, y a decir qué relación marcan. Sirve para saber qué es una opción, un contraste, una condición o una consecuencia.",
    ["Sé usar and, but, because y so.", "Conozco if y when."],
    [
        "Los conectores unen ideas y muestran su relación. Neither ... nor significa ni ... ni, y niega las dos opciones: neither tea nor coffee. Either ... or presenta dos opciones: either tea or coffee. Though, al final de una frase, significa sin embargo: it is cheap, though. En medio de la frase significa aunque: I will go, though it is late. Unless significa a menos que y equivale a if not. As soon as significa tan pronto como. As a result significa como resultado y marca una consecuencia.",
        "Con neither ... nor, el verbo concuerda con el sujeto que está más cerca. Se dice Neither the girls nor the teacher is ready, porque teacher está más cerca y es singular. Se dice Neither the teacher nor the girls are ready, porque girls está más cerca y es plural. El mismo cuidado se aplica a either ... or.",
        "Para responder, busca la idea antes y después del conector. Neither y nor dicen que ninguno hace algo. Either y or dicen que uno de los dos lo hace. Though introduce un contraste, unless una condición negativa, as soon as el momento y as a result la consecuencia.",
    ],
    [("neither ... nor", "ni ... ni"), ("either ... or", "o ... o"), ("though", "sin embargo"), ("unless", "a menos que (if not)"), ("as soon as", "tan pronto como"), ("as a result", "como resultado")],
    [
        ("Una consecuencia", "Un adulto lee en voz alta (tapa el guion): " + CT1 + " ¿Qué ocurrió como resultado de que el partido fue largo?", ["Busco as a result.", "Dice the final started late.", "Esa es la consecuencia."], "La final empezó tarde"),
        ("Una opción y una condición", "Un adulto lee en voz alta (tapa el guion): " + CT2 + " ¿Qué clubes considera Eva y bajo qué condición no se une?", ["Busco either ... or: photography club o choir.", "Busco unless: las reuniones tienen que ser los martes.", "Si no son los martes, no se une."], "Considera el club de fotografía o el coro; no se une si las reuniones no son los martes"),
    ],
    [
        ("Entender unless como si.", "Se confunden las condiciones: unless es una condición negativa, a menos que.", "Reemplaza unless por if not: I won't join if the meetings are not on Tuesdays."),
        ("Usar are en Neither the players nor the coach are happy.", "El verbo debe concordar con el sujeto más cercano, coach, que es singular.", "Mira el sujeto que va después de nor y haz que el verbo coincida con él."),
    ],
    [
        ml(K1, "¿Qué significa neither Carla nor her brothers?", "Ni Carla ni sus hermanos", ["Carla y sus hermanos", "Carla o sus hermanos"], "Neither ... nor niega a los dos."),
        ml(K3, "¿Qué conector marca un contraste en la primera oración?", "though", ["unless", "as soon as"], "Though dice que es gratis, pero la fila es larga."),
        mc("¿Cuál es la traducción de unless?", "a menos que", ["tan pronto como", "como resultado"], "Unless equivale a if not."),
    ],
    [
        ml(K4, "¿Qué consecuencia tuvo la lluvia?", "El partido se cambió al sábado", ["Los jugadores se pusieron felices", "La cancha quedó seca"], "As a result introduce el cambio al sábado; los jugadores estaban decepcionados."),
        ml(K2, "¿Qué hacen la hermana y el hablante los domingos?", "Leen o dibujan", ["Escuchan música fuerte", "Leen y dibujan a la vez"], "Either read or draw significa una de las dos actividades."),
        ml(K5, "¿Cuándo enviará Lía la lista?", "Tan pronto como la profesora responda", ["Después de contarles a los demás", "Cuando se acabe el paseo"], "As soon as she answers marca el momento."),
    ],
    [
        mc("Elige la forma correcta: Neither the players nor the coach ____ happy about the delay.", "is", ["are", "be"], "El verbo concuerda con coach, el sujeto más cercano, que es singular."),
        mc("Elige la forma correcta: Neither the coach nor the players ____ happy about the delay.", "are", ["is", "was"], "Players es el sujeto más cercano y es plural."),
        mc("Elige el conector que indica el momento exacto: I will call you ____ I arrive at the station.", "as soon as", ["unless", "neither"], "Se pide el momento exacto: tan pronto como llegue."),
    ],
    [
        ml(K7, "¿Qué es verdadero?", "Se acepta una foto o un dibujo, pero no un video ni una canción", ["Se acepta un video o una canción, pero no una foto ni un dibujo", "Se aceptan solo canciones y videos, pero nada de fotos"], "Either a photo or a drawing son las opciones; neither a video nor a song las excluye."),
        mc("Un compañero dice que Neither Ana nor Rosa came significa que vinieron las dos. ¿Es correcto?", "No: significa que no vino ninguna de las dos", ["Sí: neither nor suma a las dos", "Sí: si hay dos nombres, vienen ambas"], "Neither ... nor niega a las dos personas."),
    ],
    [
        ml(K8, "¿Por qué el club pide llamar pronto?", "Porque el telescopio es gratis, pero hay que reservarlo", ["Porque lloverá mañana y hay que cancelar la noche de astronomía", "Porque no habrá estrellas y el telescopio no funcionará"], "As a result viene después de you must book it."),
        mc("¿Qué oración tiene el mismo sentido que I won't go unless you come?", "I won't go if you don't come", ["I will go if you don't come", "I won't go if you come"], "Unless es if not: solo irá si la otra persona va."),
    ],
    [arith("Un adulto lee en voz alta (tapa el guion): " + K6 + " Un estudiante compra un asiento de doce mil pesos que no está en la primera fila. ¿Cuántos pesos paga?", "12000//2", "Los estudiantes pagan la mitad, porque el asiento no está en la primera fila.", " pesos")],
    [
        ("En Inglés de 2.º medio (OA 2, clase 3): ¿qué significa either ... or?", "O ... o: presenta dos opciones", "Se elige una de las dos."),
        ("En Inglés de 2.º medio (OA 2, clase 3): ¿con qué sujeto concuerda el verbo en neither ... nor?", "Con el sujeto más cercano al verbo", "Si el último sujeto es singular, el verbo va en singular."),
        ("En Inglés de 2.º medio (OA 2, clase 3): ¿qué conector marca una consecuencia?", "As a result", "Significa como resultado."),
    ],
    task("Un adulto lee dos veces: «Our trip to the lake depends on the weather. We will either go by bus or by car. As soon as it stops raining, we will leave. Neither Pia nor Leo likes cold water, though.» (depends on = depende de, lake = lago, stops raining = deja de llover, cold = fría). Anota tres conectores que oíste y qué relación marca cada uno.", "Either ... or: dos opciones. As soon as: el momento. Neither ... nor: niega a los dos. Though: contraste.", ["anota tres conectores del texto", "explica la relación de cada uno", "no confunde opción con contraste"], ["hoja con tres conectores y su relación"], ["anotar solo palabras sueltas sin su relación", "confundir though con as a result"], "Pide que cambie un conector por otro y explique cómo cambia el sentido."),
    "Escucha otra vez el texto del partido de tenis y marca el conector que introduce una consecuencia.",
    "Escribe en español dos frases tuyas: una con la idea de a menos que y otra con la idea de tan pronto como.",
)

# ------------------------------------------------------------------ clase 4: sonidos /t/, /d/, /ʒ/, /sp/, /st/
S1 = "«Ten tall students stood on the stage.» (tall = altos, stood = estaban de pie, stage = escenario)"
S2 = "«Dina usually makes a quick decision. Then she shows the pictures on television.» (quick = rápida, pictures = fotos)"
S3 = "«Attention, students. Please stand at the station at ten. The special bus will take ten students down to the town.» (attention = atención, stand = esperen de pie, station = estación, special = especial)"
S4 = "«Speak slowly, please. Stop at the station and study the schedule.» (slowly = despacio, schedule = horario)"
SW1 = "«Tom lives in a small town. Dan walks down the hill.» (small = pequeño, hill = cerro)"
SW2 = "«I usually watch television after making a decision.» (watch = miro, after = después de)"

lesson(
    OA, 4, MAT_L,
    "Aprenderé a distinguir los sonidos iniciales /t/ de to y /d/ de do, el sonido /ʒ/ de usually y las combinaciones /sp/ de special y /st/ de student, y a reconocerlos al escuchar. Sirve para no confundir palabras parecidas, como town y down.",
    ["Conozco los sonidos de las letras t, d, s y p.", "Sé pronunciar palabras como student."],
    [
        "El sonido /t/ al comienzo de una palabra (to, ten, town) es sordo y sale con una pequeña ráfaga de aire: si pones una hoja delante de tu boca, se mueve. El sonido /d/ (do, den, down) es sonoro: la garganta vibra y casi no hay ráfaga. Hay pares de palabras que cambian solo por este sonido: ten y den, town y down, time y dime. Por eso, confundirlos cambia el significado.",
        "El sonido /ʒ/ aparece en usually, television, decision y measure. Se parece a sh de she, pero es sonoro: la garganta vibra. No es el sonido de y ni el de ch. Las combinaciones /sp/ (special, speak) y /st/ (student, study, stop) empiezan con una s seguida directamente de p o t. Muchos hispanohablantes agregan una e inicial, como especial o estudent. En inglés, se empieza con s sin vocal antes.",
        "Al escuchar, atiende a la primera consonante de cada palabra y a si la garganta vibra o no. Si dudas entre dos palabras parecidas, usa el contexto de la oración para decidir cuál tiene sentido.",
    ],
    [("/t/", "sonido sordo de to, ten, town"), ("/d/", "sonido sonoro de do, den, down"), ("/ʒ/", "sonido sonoro de usually y television"), ("/sp/", "combinación inicial de special y speak"), ("/st/", "combinación inicial de student y stop"), ("minimal pair", "par de palabras que cambian por un solo sonido")],
    [
        ("Palabras con /t/ y con /d/", "Un adulto lee en voz alta (tapa el guion): " + SW1 + " ¿Qué palabras empiezan con /t/ y cuáles con /d/?", ["Veo las primeras consonantes: Tom y town.", "Dan y down empiezan con otra consonante.", "Tom y town empiezan con /t/; Dan y down con /d/."], "Con /t/: Tom y town; con /d/: Dan y down"),
        ("Contar el sonido /ʒ/", "Un adulto lee en voz alta (tapa el guion): " + SW2 + " ¿Cuántas palabras tienen el sonido /ʒ/?", ["Busco palabras como usually y television.", "Usually tiene /ʒ/; television también; decision también.", "Hay tres con /ʒ/."], "Tres: usually, television y decision"),
    ],
    [
        ("Decir estudent para student.", "Se agrega una vocal inicial por el español.", "Empieza directamente con /st/ y sin e antes."),
        ("Pensar que town y down suenan igual al empezar.", "Se ignora la vibración de la garganta en /d/.", "Toca tu cuello: en down vibra; en town casi no."),
    ],
    [
        mc("¿Qué par de palabras cambia solo por /t/ y /d/ al comienzo?", "ten – den", ["ten – pen", "tan – ten"], "Ten empieza con /t/ y den con /d/; las otras opciones cambian otros sonidos."),
        mc("¿Qué palabra empieza con el sonido /d/?", "down", ["town", "tie"], "Down empieza con /d/."),
        mc("¿Qué palabra tiene el sonido /ʒ/ como en usually?", "television", ["special", "station"], "Special y station tienen sh, que es sordo; television tiene /ʒ/."),
    ],
    [
        ml(S1, "¿Cuántas palabras empiezan con el sonido /t/?", "Dos: ten y tall", ["Tres: ten, tall y students", "Una: ten"], "Students empieza con /st/, no con /t/."),
        ml(S1, "¿Cuántas palabras empiezan con la combinación /st/?", "Tres: students, stood y stage", ["Dos: students y stage", "Una: students"], "Stood también empieza con /st/."),
        mc("Pones una hoja delante de tu boca y dices ten. ¿Qué debería pasar?", "La hoja se mueve por una pequeña ráfaga de aire", ["La garganta vibra más que con den y la hoja casi no se mueve", "La hoja no se mueve porque no sale aire al decir la t"], "El /t/ inicial lleva ráfaga de aire."),
    ],
    [
        ml(S2, "¿Cuántas palabras tienen /ʒ/?", "Tres: usually, decision y television", ["Dos: usually y decision", "Cuatro: usually, decision, television y pictures"], "Pictures tiene ch, no /ʒ/."),
        mc("Un compañero dice «estudent» y «especial». ¿Qué consejo le das?", "Empezar con /st/ y /sp/ directamente, sin e antes", ["Alargar la e inicial", "Decir la palabra más fuerte"], "En inglés se pronuncia student y special sin vocal inicial."),
        mr("Lee las tres oraciones: 1) Sam will speak slowly. 2) Sam will talk slowly. 3) Sam will tell the story.", "¿Cuál contiene una palabra que empieza con /sp/?", "La oración 1", ["La oración 2", "La oración 3"], "Speak empieza con /sp/; story empieza con /st/."),
    ],
    [
        ml("«Two girls talk. Girl 1: I live in the town. Girl 2: I live down the street.» (street = calle)", "Una oyente anota: «I live in the down». ¿Qué confundió?", "El /t/ de town con el /d/ de down", ["El /ʒ/ de usually con el /sp/ de special", "El /st/ de student con el /d/"], "Town y down cambian solo por el sonido inicial."),
        mc("¿Por qué es importante distinguir /t/ de /d/ en ten y den?", "Porque cambia el significado de la palabra", ["Porque la palabra se vuelve más larga", "Porque cambia la ortografía de la oración"], "Un solo sonido distingue dos palabras distintas."),
    ],
    [
        ml(S4, "¿Cuántas palabras empiezan con /st/?", "Tres: stop, station y study", ["Cuatro: speak, stop, station y study", "Dos: stop y study"], "Speak empieza con /sp/, no con /st/."),
        mc("Marta dice «yusually» con /j/ y «especial». ¿Cuál es la mejor corrección?", "Usar /ʒ/ sonoro como en television y empezar special sin e", ["Hablar más fuerte las dos palabras", "Deletrear las palabras letra por letra"], "Se corrige el sonido /ʒ/ y se quita la vocal inicial."),
    ],
    [ml(S3, "¿Cuántas palabras empiezan con el sonido /t/?", "Cinco: ten, take, ten, to y town", ["Cuatro: ten, take, ten y town", "Seis: ten, take, ten, to, town y the"], "The empieza con otro sonido; to también empieza con /t/.")],
    [
        ("En Inglés de 2.º medio (OA 2, clase 4): ¿qué sonido tiene la garganta vibrando al comienzo de down?", "/d/", "Es el sonido sonoro de do y down."),
        ("En Inglés de 2.º medio (OA 2, clase 4): ¿qué palabra del grupo special, speak y stop empieza con /st/?", "stop", "Special y speak empiezan con /sp/."),
        ("En Inglés de 2.º medio (OA 2, clase 4): ¿en qué palabra aparece el sonido /ʒ/: usually o student?", "usually", "Student empieza con /st/."),
    ],
    task("Con la ayuda de un adulto, lee en voz alta esta oración tres veces: «Dina usually studies at the station.» (studies = estudia, station = estación). Pide al adulto que marque cuando oiga el sonido /ʒ/, /st/ y la ausencia de e inicial, y anota en tu hoja cuántas veces te salió bien.", "Primera lectura: bien /ʒ/, e inicial en studies. Segunda: bien las dos. Tercera: bien las tres.", ["lee la oración tres veces", "registra el sonido /ʒ/, /st/ y la e inicial", "anota qué mejoró"], ["tabla de tres filas en la hoja"], ["agregar e inicial en studies y station", "no registrar qué falló"], "Pide que repita solo la palabra que falló hasta que salga limpia."),
    "Di en voz alta con un adulto los pares ten – den y town – down y anota qué sonido cambia.",
    "Escribe una lista de cinco palabras en español que empiezan con es- y piensa cómo se dirían sin la e inicial en inglés.",
)

# ------------------------------------------------------------------ clase 5: acentuación en palabras y compuestas
lesson(
    OA, 5, MAT_L,
    "Aprenderé a ubicar la sílaba acentuada en palabras de dos o más sílabas y en palabras compuestas, y a notar cómo el acento cambia el sentido. Sirve para que te entiendan y para entender a otros.",
    ["Sé contar sílabas.", "Conozco palabras como teacher, homework y tomorrow."],
    [
        "En inglés, una sílaba de cada palabra se pronuncia más fuerte, más larga y más clara: es la sílaba acentuada. En la mayoría de los sustantivos y adjetivos de dos sílabas el acento cae en la primera: TEAcher, STUdent, TAble, SPEcial. En muchos verbos de dos sílabas cae en la segunda: deCIDE, reLAX, reTURN, enJOY, preSENT. En palabras largas hay que aprenderlas: toMORrow, imPORtant, comPUter y deLIcious llevan acento en la segunda; USually, WONderful y BEAUtiful, en la primera.",
        "En las palabras compuestas, que forman un solo sustantivo, el acento cae en la primera parte: NOTEbook, CLASSroom, HOMEwork, BACKpack, AIRport. En cambio, un adjetivo más un sustantivo suele tener acento en el segundo: green HOUSE es una casa pintada de verde, mientras que GREENhouse es un invernadero. El acento puede cambiar el sentido: un PREsent es un regalo y to preSENT es presentar.",
        "Al escuchar, atiende a la sílaba más fuerte. Si no la entiendes, pide que repitan despacio. Al hablar, marca la sílaba acentuada con más fuerza, más duración y un tono un poco más alto. Practica con mayúsculas en tu cuaderno: reLAX, HOMEwork.",
    ],
    [("stressed syllable", "sílaba acentuada"), ("compound word", "palabra compuesta, como notebook"), ("deCIDE / toMORrow", "acento en la segunda sílaba"), ("TEAcher / HOMEwork", "acento en la primera sílaba"), ("PREsent / preSENT", "regalo / presentar"), ("GREENhouse", "invernadero")],
    [
        ("Acento en un sustantivo de dos sílabas", "Pregunta: ¿dónde cae el acento en teacher?", ["Es un sustantivo de dos sílabas.", "En la mayoría de los casos va en la primera.", "Se dice TEAcher."], "En la primera sílaba: TEAcher"),
        ("Acento en una palabra compuesta", "Pregunta: ¿dónde cae el acento en notebook?", ["Notebook une note y book.", "En un compuesto, el acento va en la primera parte.", "Se dice NOTEbook."], "En la primera parte: NOTEbook"),
    ],
    [
        ("Poner el acento en la última sílaba de toda palabra, como en español.", "Se aplican las reglas del español.", "Aprende palabra por palabra y marca la sílaba fuerte en mayúscula."),
        ("Decir book con más fuerza en notebook.", "En los compuestos el acento va en la primera parte.", "Dilo NOTEbook, con la primera parte fuerte."),
    ],
    [
        mc("¿Dónde cae el acento en student?", "En la primera sílaba", ["En la segunda sílaba", "En las dos por igual"], "Es un sustantivo de dos sílabas: STUdent."),
        mc("¿Dónde cae el acento en repeat?", "En la segunda sílaba", ["En la primera sílaba", "En ninguna"], "Muchos verbos de dos sílabas llevan acento en la segunda: rePEAT."),
        mc("En la palabra compuesta notebook, ¿qué parte lleva más fuerza?", "note", ["book", "las dos por igual"], "En un compuesto, el acento va en la primera parte."),
    ],
    [
        mc("¿Cuál de estas palabras lleva el acento en la segunda sílaba?", "decide", ["table", "teacher"], "Decide es deCIDE; table y teacher llevan el acento en la primera."),
        mr("Lee: «My teacher gave me a present. She will present the prize on Friday.» (present = regalo; prize = premio)", "¿Cuál de los dos present lleva el acento en la segunda sílaba?", "El verbo de la segunda oración", ["El sustantivo de la primera oración", "Los dos por igual"], "El sustantivo es PREsent (regalo) y el verbo es preSENT (presentar)."),
        mc("¿Cuál de estas palabras es compuesta, con acento en la primera parte?", "classroom", ["decide", "enjoy"], "Classroom une class y room: CLASSroom."),
    ],
    [
        mc("¿Dónde cae el acento en important?", "im-POR-tant", ["IM-por-tant", "im-por-TANT"], "Important lleva el acento en la segunda sílaba."),
        mc("¿Dónde cae el acento en tomorrow?", "to-MOR-row", ["TO-mor-row", "to-mor-ROW"], "Tomorrow lleva el acento en la segunda sílaba."),
        mc("Un letrero dice «greenhouse». Si acentúas GREEN-house, ¿qué significa?", "Un invernadero", ["Una casa pintada de verde", "Una casa muy pequeña"], "GREENhouse es invernadero; green HOUSE es una casa verde."),
    ],
    [
        ml("«Dina: I will record the interview tomorrow. Then I will save the record on my computer.» (record = grabar / grabación, interview = entrevista, save = guardar)", "¿Cuál de los dos record lleva el acento en la segunda sílaba?", "El verbo de la primera oración", ["El sustantivo de la segunda oración", "Los dos por igual"], "El verbo es reCORD y el sustantivo es REcord."),
        mc("¿Por qué importa el acento de palabra?", "Porque cambia cómo se entiende la palabra y a veces su significado", ["Porque cambia su ortografía", "Porque la hace más larga"], "Un PREsent no es lo mismo que preSENT."),
    ],
    [
        mc("¿Qué lista tiene solo palabras con acento en la primera sílaba?", "teacher, special, homework", ["decide, enjoy, tomorrow", "prepare, repeat, important"], "Las otras listas incluyen palabras con acento en la segunda."),
        ml("«My teacher gave a speech on the airport project. She asked us to prepare a notebook and a backpack for the trip.» (speech = charla, project = proyecto, trip = viaje)", "¿Qué palabra del texto lleva el acento en la segunda sílaba?", "prepare", ["teacher", "notebook"], "Prepare es prePARE; teacher y notebook llevan el acento en la primera sílaba."),
    ],
    [ml("«Students, please bring your backpack and your notebook to the classroom. Tomorrow we will decide the teams. It is important to be on time.» (bring = traigan, teams = equipos, on time = a la hora)", "¿Cuántas de estas palabras (tomorrow, decide, important) llevan el acento en la segunda sílaba?", "Las tres", ["Solo decide", "Solo tomorrow"], "To-MOR-row, de-CIDE e im-POR-tant tienen el acento en la segunda.")],
    [
        ("En Inglés de 2.º medio (OA 2, clase 5): ¿dónde cae el acento en una palabra compuesta como homework?", "En la primera parte: HOMEwork", "Es la regla de los compuestos."),
        ("En Inglés de 2.º medio (OA 2, clase 5): ¿en qué sílaba cae el acento de decide?", "En la segunda: deCIDE", "Muchos verbos de dos sílabas tienen acento en la segunda."),
        ("En Inglés de 2.º medio (OA 2, clase 5): ¿qué cambia entre PREsent y preSENT?", "El acento y el significado: regalo o presentar", "El acento puede cambiar el sentido."),
    ],
    task("Escribe cada palabra y marca con mayúsculas la sílaba acentuada: homework, decide, teacher, tomorrow, airport, enjoy.", "HOMEwork, deCIDE, TEAcher, toMORrow, AIRport, enJOY.", ["marca una sílaba en cada palabra", "aplica la regla de compuestos", "aplica la regla de verbos de dos sílabas"], ["hoja con seis palabras marcadas"], ["marcar la última sílaba por costumbre del español", "marcar book en notebook"], "Pide que explique qué regla usó en cada palabra."),
    "Di en voz alta cinco palabras de la clase y golpea la mesa en la sílaba acentuada.",
    "Busca en tu casa cuatro objetos con nombre compuesto en inglés (por ejemplo toothbrush) y marca su acento.",
)
