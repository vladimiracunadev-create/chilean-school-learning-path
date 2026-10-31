"""Cuaderno del estudiante, 7.º básico Inglés (oficial), IN07 OA 01 (comprensión general y explícita de textos orales).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan pista en español. Todo término nuevo se explica antes de usarlo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "IN07 OA 01"
ADULT = "Un adulto lee en voz alta (tapa el guion): "


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


# ------------------------------------------------------------------ textos de OA 1
ANN = "«Good morning, students. This is the school radio. Tomorrow is Thursday, and the robotics club meets in room 12 at four o'clock. Please bring a notebook and a pencil. New members are welcome.» (robotics club = taller de robótica, meets = se reúne, room = sala, bring = traer, welcome = bienvenidos)"
CONV = "«Tomás: Hi, Elena! Are you coming to the beekeeping workshop? Elena: Yes, I am, but I don't have a hat. Tomás: Don't worry. The teacher has extra hats. Elena: Great! See you at the garden.» (beekeeping = apicultura, workshop = taller, hat = sombrero, extra = de repuesto, garden = huerto)"
DESC = "«My town has a small museum near the river. It has a big blue door and two tall windows. Inside, there are old maps and a model of a ship. It is open from Tuesday to Sunday.» (museum = museo, river = río, door = puerta, maps = mapas, ship = barco, open = abierto)"
STORY = "«Last Friday, Ana's radio stopped working. She opened the back and saw that the battery was empty. She bought a new battery at the corner shop, and the radio worked again. She danced happily.» (stopped working = dejó de funcionar, battery = pila, empty = vacía, bought = compró, corner shop = almacén de la esquina)"
BOTTLES = "«Today I want to talk about plastic bottles. Every year, many bottles end up in the sea. Birds and fish can be hurt. But we can help. We can use a metal bottle, we can recycle, and we can join a beach clean-up.» (end up = terminan, sea = mar, hurt = dañados, recycle = reciclar, join = unirse a, beach clean-up = limpieza de playa)"
CATS = "«Many people think cats sleep too much. In fact, a cat sleeps about fourteen hours a day. This is normal. In the wild, cats save energy for hunting. So a sleepy cat is not lazy; it is just a good hunter.» (in fact = de hecho, hours = horas, in the wild = en estado salvaje, save = ahorrar, hunting = cazar, lazy = flojo)"
TRIP = "«Mr. Soto: Class, our trip is next Wednesday. We leave at eight fifteen and come back at one o'clock. Valeria: Do we need money? Mr. Soto: No, but bring a lunch box and a water bottle. Pablo: Where are we going? Mr. Soto: To the science museum in the city center.» (trip = salida pedagógica, leave = salimos, come back = volvemos, lunch box = vianda, water bottle = botella de agua, science = ciencias)"
BUS = "«Late at night, at a bus stop, Lucía speaks to a bus driver. Lucía: Excuse me, does this bus go to the hospital? Driver: No, you need the number 14. It stops across the street. Lucía: Thank you. Is it late? Driver: Not at all. Number 14 comes every ten minutes.» (bus stop = paradero, hospital = hospital, across the street = al otro lado de la calle, not at all = para nada, every = cada)"
SOUP = "«In the school kitchen, Chef Mara and two students, Iván and Rosa, make soup. Iván peels the carrots. Rosa washes the potatoes. Chef Mara tastes the soup and says: It needs more salt. Iván adds a little salt.» (chef = cocinera, peels = pela, washes = lava, tastes = prueba, needs = necesita, salt = sal)"
VOICE = "«Hi Diego, it's Sofía. The football match is not on Saturday now. It's on Sunday at eleven because it is raining on Saturday. Please tell the team. Bring your blue shirt. Bye!» (match = partido, now = ahora, raining = lloviendo, team = equipo, shirt = polera)"
WEATHER = "«Good evening. Here is the weather for tomorrow. In the north, it will be sunny and hot, thirty-two degrees. In the center, cloudy with light rain in the afternoon, eighteen degrees. In the south, windy and cold, nine degrees.» (weather = clima, sunny = soleado, cloudy = nublado, light rain = lluvia ligera, windy = ventoso, degrees = grados)"

# ------------------------------------------------------------------ clase 1
lesson(
    OA1, 1,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a reconocer qué tipo de texto oral escucho (aviso, conversación, descripción o cuento) y para qué se dijo. Sirve para decidir qué buscar antes de entender los detalles.",
    ["Sé que un texto puede informar, describir o contar algo.", "Conozco palabras como today, tomorrow, bring y open."],
    [
        "Un texto oral tiene un tipo (text type) y un propósito (purpose). El tipo es la forma del texto: un aviso (announcement) habla a muchas personas e informa; una conversación (conversation) tiene dos o más hablantes que se turnan; una descripción (description) dice cómo es algo; un cuento (story) cuenta hechos pasados en orden; unas instrucciones (instructions) dicen qué pasos seguir.",
        "Para reconocer el tipo, escucha las primeras frases y busca pistas. Good morning, students sugiere un aviso. Los nombres seguidos de dos puntos, como Tomás: y Elena:, indican una conversación. Las frases con is, has y there are suelen describir. Last Friday, bought y worked suelen contar una historia pasada. Palabras como first, then y wash o cut (verbos que mandan hacer algo) suelen marcar instrucciones.",
        "El propósito responde a la pregunta «¿para qué lo dicen?»: informar, invitar, pedir ayuda, avisar una regla, describir o entretener. No hace falta entender cada palabra. Con el tipo y el propósito ya sabes qué debes buscar: en un aviso, qué, cuándo y dónde; en un cuento, quién y qué le pasó.",
    ],
    [("announcement", "aviso: mensaje para muchas personas"), ("conversation", "conversación entre dos o más personas"), ("description", "descripción: dice cómo es algo"), ("story", "cuento: hechos pasados en orden"), ("instructions", "instrucciones: pasos que hay que seguir"), ("purpose", "propósito: para qué se dice un texto"), ("clue", "pista: palabra que ayuda a entender")],
    [
        ("Reconocer el tipo", ADULT + DESC + " ¿Qué tipo de texto es y qué pista lo muestra?", ["Escucho el comienzo: My town has a small museum.", "No hay turnos de hablantes ni hechos en orden; hay frases como it has y there are.", "Esas frases dicen cómo es el museo."], "Es una descripción: las frases it has y there are dicen cómo es el museo"),
        ("Reconocer el propósito", ADULT + ANN + " ¿Para qué se dice este texto?", ["Es un aviso de la radio del colegio.", "Dice el día, la sala y la hora de una reunión.", "El propósito es informar de la reunión e invitar a socios nuevos."], "Informar de una reunión del club de robótica e invitar a nuevos miembros"),
    ],
    [
        ("Pensar que cualquier texto con nombres de personas es un cuento.", "Se olvida que una conversación también nombra personas, pero estas hablan por turnos.", "Fíjate en si los hablantes se turnan o en si alguien cuenta hechos pasados."),
        ("Decir que un aviso solo sirve para entretener.", "Se confunde el propósito: un aviso sirve para dar información útil.", "Busca qué dato necesita el oyente: día, hora, lugar o regla."),
    ],
    [
        (ADULT + ANN + " ¿Qué tipo de texto es? a) un aviso b) un cuento", "a) un aviso", "Habla a todos los estudiantes y da información de una reunión."),
        (ADULT + CONV + " ¿Qué tipo de texto es? a) una conversación entre dos personas b) la descripción de un lugar", "a) una conversación entre dos personas", "Tomás y Elena hablan por turnos."),
        (ADULT + DESC + " ¿Para qué se dice este texto? a) para describir un lugar b) para invitar a un taller", "a) para describir un lugar", "Dice cómo es el museo: puerta azul, ventanas, mapas."),
    ],
    [
        (ADULT + ANN + " ¿Para qué sirve este aviso? a) informar de una reunión b) enseñar a armar un robot c) vender entradas", "a) informar de una reunión", "Dice el día, la hora y la sala del club."),
        (ADULT + STORY + " ¿Qué expresión muestra que el texto cuenta algo que ya pasó? a) Last Friday b) corner shop", "a) Last Friday", "Last Friday indica un tiempo pasado; corner shop es solo un lugar."),
        (ADULT + CONV + " ¿Cuántas personas hablan en este texto?", "2", "Hablan Tomás y Elena."),
    ],
    [
        (ADULT + "Tres mensajes breves. A) «Attention, passengers: the bus to Rancagua leaves at six.» B) «First, wash the carrots. Then cut them.» C) «My dog is small, brown and very fast.» (attention = atención, passengers = pasajeros, leaves = sale, wash = lavar, cut = cortar). Escribe el tipo de cada uno: aviso, instrucciones o descripción.", "A aviso, B instrucciones, C descripción", "A informa a pasajeros, B da pasos con first y then, C dice cómo es un perro."),
        (ADULT + ANN + " ¿A quién se dirige el aviso? a) a los estudiantes del colegio b) a una sola amiga", "a) a los estudiantes del colegio", "Comienza con Good morning, students."),
        (ADULT + STORY + " ¿Cuál es el propósito del texto? a) contar lo que le pasó a Ana con su radio b) pedir una pila prestada", "a) contar lo que le pasó a Ana con su radio", "Narra hechos pasados en orden: se apagó, vio la pila, compró otra."),
    ],
    [
        ("Marta dice: «El texto del museo es un cuento porque tiene un río». ¿Tiene razón? Responde sí o no.", "No", "Describe un lugar; no hay personajes ni hechos pasados en orden, y el río es solo un dato del lugar."),
        (ADULT + "«Please walk, don't run, near the pool.» (walk = caminar, run = correr, pool = piscina). ¿Cuál es el propósito? a) dar una regla de seguridad b) contar una historia", "a) dar una regla de seguridad", "Pide una conducta concreta junto a la piscina."),
    ],
    [
        (ADULT + ANN + " ¿Qué frase muestra que pueden llegar personas que aún no están en el club? a) New members are welcome. b) Please bring a notebook.", "a) New members are welcome.", "New members son los miembros nuevos y welcome significa bienvenidos."),
        (ADULT + "«Flight 20 to Punta Arenas is delayed by one hour.» (flight = vuelo, delayed = atrasado). ¿Qué hace este texto? a) informa un cambio b) cuenta una anécdota", "a) informa un cambio", "Avisa un atraso a los pasajeros, sin contar una historia."),
    ],
    [(ADULT + "En la radio del colegio suena: «Lost: a green water bottle. Please ask in the office.» (lost = perdido, ask = preguntar, office = oficina). Si la botella es tuya, ¿qué debes hacer?", "Preguntar en la oficina", "El aviso dice Please ask in the office.")],
    [
        ("¿Qué tipo de texto tiene hablantes que se turnan?", "Una conversación", "Los nombres y los turnos de habla indican una conversación."),
        ("¿Qué pregunta responde el propósito de un texto?", "Para qué lo dicen", "El propósito es la razón por la que se dice el texto."),
        ("¿Qué tipo de texto dice cómo es un lugar o un objeto?", "Una descripción", "La descripción entrega rasgos de lo descrito."),
    ],
    task("Un adulto lee dos veces este mensaje: «Hello, everyone. The school garden is open on Friday at three o'clock. We need ten students to plant tomatoes. Please wear old shoes.» (garden = huerto, plant = plantar, wear = usar, old shoes = zapatos viejos). Escribe en tu hoja: el tipo de texto, su propósito y una palabra o frase que te lo mostró.", "Es un aviso. Sirve para invitar a plantar tomates el viernes. La pista es: We need ten students.", ["escribe un tipo de texto coherente", "explica el propósito con sus palabras", "cita una pista del texto"], ["hoja con tres respuestas", "nota del adulto"], ["decir que es un cuento", "no citar ninguna pista"], "Reconoce lo que acertó y vuelve a escuchar solo la primera frase para decidir a quién le habla el mensaje."),
    "Pide a un adulto que lea el aviso del club de robótica y levanta la mano cada vez que oigas un dato de día, hora o lugar.",
    "Escribe en español un aviso de tres frases para tu curso y explica qué pistas lo harían reconocible como aviso.",
)

# ------------------------------------------------------------------ clase 2
lesson(
    OA1, 2,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a encontrar la idea general (gist) de un texto oral, es decir, de qué trata en conjunto. Sirve para entender lo principal aunque no conozcas todas las palabras.",
    ["Sé reconocer el tipo de texto y su propósito.", "Conozco palabras como because, help, cats y bottles."],
    [
        "La idea general (main idea) es lo más importante que dice un texto, dicho en una sola frase. Responde a la pregunta «¿de qué trata todo el texto y qué quiere decir?». Los detalles (details) son datos que apoyan esa idea, como números, nombres o ejemplos.",
        "Para encontrarla, escucha primero sin anotar detalles. Fíjate en las palabras que se repiten: si oyes bottles, sea y recycle varias veces, el tema son las botellas y el mar. Fíjate también en el comienzo, que suele presentar el tema, y en el final, que suele dar la conclusión. Palabras como but, so y in fact marcan un cambio o una conclusión.",
        "Una buena idea general no es demasiado pequeña ni demasiado grande. Un solo dato, como fourteen hours, es un detalle. Decir solo «animales» es demasiado general. La idea general de un texto sobre gatos que duermen mucho es: los gatos duermen muchas horas porque ahorran energía para cazar.",
    ],
    [("main idea / gist", "idea general: lo más importante del texto"), ("detail", "detalle: dato que apoya la idea"), ("topic", "tema: de qué se habla"), ("in fact", "de hecho: introduce un dato que aclara"), ("but", "pero: marca un cambio"), ("so", "entonces / por eso: marca una conclusión")],
    [
        ("Tema e idea general", ADULT + BOTTLES + " ¿Cuál es el tema y cuál la idea general?", ["Se repiten bottles, sea y help.", "El tema son las botellas de plástico y el mar.", "Después de But we can help aparecen las acciones: la idea es que botellas dañan animales y podemos ayudar."], "Las botellas de plástico dañan a los animales del mar, pero podemos ayudar"),
        ("Idea general frente a detalle", ADULT + CATS + " ¿Fourteen hours es la idea general o un detalle?", ["Fourteen hours es un número.", "Un número apoya la idea, pero no es lo más importante.", "La idea general explica por qué duermen tanto."], "Es un detalle"),
    ],
    [
        ("Escoger como idea general el primer dato que se oye.", "Se confunde un detalle con la idea general.", "Escucha el texto completo y pregunta qué quiere decir en conjunto."),
        ("Decir una idea tan amplia que sirve para cualquier texto, como «se habla de animales».", "La idea general debe decir algo específico del texto.", "Agrega qué se dice sobre el tema: «los gatos duermen mucho porque ahorran energía»."),
    ],
    [
        (ADULT + BOTTLES + " ¿De qué trata el texto? a) de botellas de plástico y el mar b) de un campeonato de natación", "a) de botellas de plástico y el mar", "Se repiten bottles y sea."),
        (ADULT + CATS + " ¿De qué animal habla el texto? a) del gato b) del perro", "a) del gato", "Cats y cat se repiten durante todo el texto."),
        (ADULT + BOTTLES + " ¿Qué palabra marca el cambio hacia las soluciones? a) but b) every", "a) but", "But we can help abre la parte de las acciones posibles."),
    ],
    [
        (ADULT + CATS + " ¿Cuál es la idea general? a) los gatos duermen muchas horas porque ahorran energía para cazar b) los gatos son flojos y no cazan c) los gatos comen catorce veces al día", "a) los gatos duermen muchas horas porque ahorran energía para cazar", "Resume el tema y la razón que da el texto."),
        (ADULT + BOTTLES + " ¿Qué quiere lograr quien habla? a) que los oyentes ayuden con acciones concretas b) que compren botellas nuevas", "a) que los oyentes ayuden con acciones concretas", "Menciona metal bottle, recycle y beach clean-up como ayudas."),
        (ADULT + CATS + " ¿Qué palabra introduce un dato que corrige una creencia? a) in fact b) so", "a) in fact", "In fact (de hecho) aclara lo que se cree."),
    ],
    [
        (ADULT + "«Our school has a new rule for the break. Students can use the football field on Monday and Wednesday. Students in sixth grade use it on Tuesday and Thursday. On Friday, everyone plays together.» (break = recreo, field = cancha, rule = regla, together = juntos). ¿Cuál es la idea general? a) hay un horario nuevo para usar la cancha b) hay un partido el viernes en otro colegio", "a) hay un horario nuevo para usar la cancha", "Todo el texto reparte los días de uso de la cancha."),
        (ADULT + "«Last summer I visited my grandparents' farm. I fed the hens, picked plums and rode a horse. It was the best holiday of my life.» (farm = campo, fed = alimenté, hens = gallinas, picked = recogí, plums = ciruelas, holiday = vacaciones). ¿Qué idea resume mejor el texto? a) fueron unas vacaciones muy buenas en el campo b) hubo un problema con los caballos", "a) fueron unas vacaciones muy buenas en el campo", "Las acciones y la última frase muestran que lo pasó muy bien."),
        (ADULT + BOTTLES + " ¿Cuál de estas frases es un detalle y no la idea general? a) We can join a beach clean-up. b) Plastic is a problem for the sea.", "a) We can join a beach clean-up.", "Es una acción concreta que apoya la idea de ayudar."),
    ],
    [
        ("Mateo dice: «La idea general del texto de los gatos es fourteen hours». ¿Qué le responderías? a) que es un detalle y la idea explica el porqué b) que tiene toda la razón", "a) que es un detalle y la idea explica el porqué", "El número apoya la idea general, no la reemplaza."),
        (ADULT + CATS + " ¿Qué dato del texto explica por qué un gato que duerme mucho no es flojo? a) que ahorra energía para cazar b) que come catorce veces al día", "a) que ahorra energía para cazar", "Dice In the wild, cats save energy for hunting."),
    ],
    [
        (ADULT + "«At lunchtime, the cafeteria is very noisy. Students shout, chairs move, and trays fall. A teacher says: Please speak quietly. Everyone wants to eat in peace.» (cafeteria = casino, noisy = ruidoso, shout = gritan, trays = bandejas, quietly = en voz baja, in peace = tranquilos). ¿Cuál es la idea general? a) en el casino hay mucho ruido y se pide hablar en voz baja b) el casino cerró por falta de sillas", "a) en el casino hay mucho ruido y se pide hablar en voz baja", "Describe el ruido y termina con la petición de la profesora."),
        (ADULT + BOTTLES + " Si la persona agregara una frase final, ¿cuál repetiría la idea general? a) Small actions help the sea. b) Many birds live near the sea.", "a) Small actions help the sea.", "Resume lo que dice el texto: las acciones pequeñas ayudan al mar."),
    ],
    [(ADULT + "En una charla de ciencias oyes: «Bees are important. They carry pollen from flower to flower, and this helps plants make fruit. Without bees, we would have fewer apples and almonds.» (bees = abejas, pollen = polen, flower = flor, fruit = fruta, without = sin, fewer = menos). ¿Cuál es la idea general?", "Las abejas son importantes porque ayudan a las plantas a dar fruta", "Todo el texto explica por qué las abejas son importantes.")],
    [
        ("En Inglés de 7.º (OA 1, clase 2): ¿Qué es la idea general de un texto?", "Lo más importante que dice, en una sola frase", "Resume el texto completo."),
        ("¿Un número, un nombre o una fecha es idea general o detalle?", "Un detalle", "Son datos que apoyan la idea."),
        ("¿Qué significa «in fact»?", "De hecho", "In fact introduce un dato que aclara o corrige."),
    ],
    task("Un adulto lee dos veces este texto: «Many students walk to school. Walking is good for your body and it is free. It also helps the air because there are fewer cars. So try to walk on Fridays.» (body = cuerpo, free = gratis, air = aire, cars = autos, try = intenta). Escribe en tu hoja la idea general en una frase, y dos detalles que la apoyan.", "Idea general: caminar al colegio es bueno para ti y para el aire. Detalles: es gratis; hay menos autos.", ["escribe una frase única de idea general", "anota dos detalles del texto", "no copia el texto entero"], ["hoja con tres respuestas", "nota del adulto"], ["anotar solo un detalle como idea general", "inventar datos que el texto no dice"], "Reconoce lo que acertó y vuelve a preguntar «¿para qué quieren que camine?» para ubicar la conclusión."),
    "Pide a un adulto que lea el texto de las abejas y di en voz alta la idea general en una sola frase.",
    "Escribe dos frases cortas en inglés sobre las abejas y subraya cuál es la idea general y cuál el detalle.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA1, 3,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a ubicar información explícita, es decir, datos que el texto dice directamente: días, horas, lugares, números y objetos. Sirve para responder con precisión lo que se escucha.",
    ["Sé decir la hora en inglés (eight fifteen, one o'clock).", "Conozco los días de la semana en inglés."],
    [
        "La información explícita (explicit information) es la que el texto dice con palabras claras. No hay que adivinarla. Responde preguntas como who (quién), what (qué), where (dónde), when (cuándo), how many (cuántos) y which (cuál). Para ubicarla, primero lee la pregunta y decide qué dato buscas.",
        "En una escucha, anota solo palabras clave: números, días, lugares y objetos. En la salida pedagógica del texto, las claves son next Wednesday (día), eight fifteen (hora de salida), one o'clock (hora de regreso), lunch box y water bottle (cosas que traer) y science museum (lugar). No necesitas escribir frases completas.",
        "Cuidado con las negaciones y los contrastes. Si oyes «No, but bring a lunch box», la respuesta a «¿necesitan dinero?» es no. Cuidado también con números parecidos: fifteen (15) y fifty (50) suenan casi igual; fifteen acentúa el final y fifty la primera parte. Si dudas, escucha de nuevo y compara con el contexto.",
    ],
    [("explicit", "explícito: dicho directamente en el texto"), ("where", "dónde"), ("when", "cuándo"), ("how many", "cuántos"), ("bring", "traer"), ("come back", "volver, regresar")],
    [
        ("Ubicar un dato de hora", ADULT + TRIP + " ¿A qué hora salen?", ["La pregunta pide una hora de salida: busco leave.", "Dice We leave at eight fifteen.", "Eight fifteen es ocho y cuarto."], "A las 8:15"),
        ("Ubicar un dato con negación", ADULT + TRIP + " ¿Necesitan llevar dinero?", ["Busco la pregunta Do we need money?", "La respuesta empieza con No.", "Pide otras cosas: vianda y botella."], "No"),
    ],
    [
        ("Confundir fifteen con fifty.", "Los dos números suenan parecidos y se mira solo el comienzo.", "Atiende a cuál sílaba se acentúa y comprueba con el contexto (una hora no puede ser las cincuenta)."),
        ("Responder con un dato que el texto no dice, como «van en bus».", "Se adivina en vez de ubicar lo explícito.", "Responde solo con lo que el texto dice con palabras claras."),
    ],
    [
        (ADULT + TRIP + " ¿Cuándo es la salida? a) el próximo miércoles b) el próximo jueves", "a) el próximo miércoles", "Dice next Wednesday."),
        (ADULT + TRIP + " ¿A dónde van? a) al museo de ciencias b) a la playa", "a) al museo de ciencias", "Dice to the science museum."),
        (ADULT + TRIP + " ¿A qué hora vuelven? a) a la una b) a las ocho", "a) a la una", "Dice come back at one o'clock."),
    ],
    [
        (ADULT + TRIP + " ¿Qué dos cosas deben llevar? a) una vianda y una botella de agua b) dinero y una mochila", "a) una vianda y una botella de agua", "Dice bring a lunch box and a water bottle."),
        (ADULT + TRIP + " ¿Qué estudiante pregunta por el dinero? a) Valeria b) Pablo", "a) Valeria", "Valeria dice Do we need money?; Pablo pregunta el lugar."),
        (ADULT + TRIP + " ¿Cuántos estudiantes hacen preguntas?", "2", "Preguntan Valeria y Pablo."),
    ],
    [
        (ADULT + "«The cooking class is on Monday at ten past four, in the school kitchen. Each student brings two eggs and one apple. The teacher gives the flour, the milk and the sugar.» (cooking class = clase de cocina, eggs = huevos, flour = harina, milk = leche, sugar = azúcar). ¿Cuántas cosas trae cada estudiante en total, contando cada huevo y cada manzana?", "3", "Trae dos huevos y una manzana: 2 + 1 = 3."),
        (ADULT + "«The cooking class is on Monday at ten past four, in the school kitchen. Each student brings two eggs and one apple. The teacher gives the flour, the milk and the sugar.» (cooking class = clase de cocina, eggs = huevos). ¿Quién trae la harina? a) el profesor o la profesora b) cada estudiante", "a) el profesor o la profesora", "Dice The teacher gives the flour."),
        (ADULT + "«The cooking class is on Monday at ten past four, in the school kitchen. Each student brings two eggs and one apple.» (ten past four = cuatro y diez, kitchen = cocina). ¿A qué hora empieza la clase? a) a las 4:10 b) a las 10:04", "a) a las 4:10", "Ten past four significa diez minutos después de las cuatro."),
    ],
    [
        (ADULT + TRIP + " Un compañero dice que el regreso es a las 3. ¿Qué dato del texto lo contradice?", "Come back at one o'clock", "El texto dice que vuelven a la una, no a las tres."),
        (ADULT + TRIP + " Si salen a las 8:15 y vuelven a la 1:00 de la tarde, ¿cuánto dura la salida en horas y minutos? a) 4 horas 45 minutos b) 5 horas 15 minutos", "a) 4 horas 45 minutos", "De 8:15 a 12:15 son 4 horas, y de 12:15 a 13:00 son 45 minutos."),
    ],
    [
        (ADULT + "«The bakery opens at seven thirty. Bread costs two thousand pesos per kilo, and a cake costs eight thousand pesos. On Sunday, the bakery closes at one o'clock.» (bakery = panadería, opens = abre, costs = cuesta, per kilo = el kilo, closes = cierra). ¿Cuántos pesos cuestan juntos un kilo de pan y una torta?", "10.000 pesos", "Se suman los dos precios: 2.000 + 8.000 = 10.000 pesos."),
        (ADULT + "«The bakery opens at seven thirty. On Sunday, the bakery closes at one o'clock.» (opens = abre, closes = cierra). ¿A qué hora cierra el domingo? a) a la una b) a las siete y media", "a) a la una", "Dice On Sunday, the bakery closes at one o'clock."),
    ],
    [(ADULT + "Escuchas un mensaje del club de ciclismo: «The ride is on Saturday at nine. We start at the lake and finish at the park. Bring a helmet, water and a snack.» (ride = paseo en bicicleta, lake = lago, finish = terminar, helmet = casco, snack = colación). ¿Qué tres cosas debes llevar?", "Un casco, agua y una colación", "Dice bring a helmet, water and a snack.")],
    [
        ("En Inglés de 7.º (OA 1, clase 3): ¿Qué es información explícita?", "La que el texto dice directamente", "No hay que adivinarla."),
        ("¿Qué pregunta en inglés pide una hora o un día?", "When", "When significa cuándo."),
        ("En Inglés de 7.º (OA 1, clase 3): ¿Qué significa «how many»?", "Cuántos", "How many pregunta por una cantidad."),
    ],
    task("Un adulto lee dos veces este mensaje: «Welcome to the Science Fair. It is on Friday from nine to twelve in the gym. There are twelve projects. The prize is a book. Visitors should enter by the blue door.» (science fair = feria científica, gym = gimnasio, prize = premio, visitors = visitas, enter = entrar). Escribe en tu hoja el día, el lugar, cuántos proyectos hay y cuál es el premio.", "Friday (viernes); en el gimnasio; 12 proyectos; un libro.", ["anota los cuatro datos", "usa solo lo que dice el texto", "escribe en español o en inglés"], ["hoja con cuatro datos", "nota del adulto"], ["decir que son 20 proyectos (por twelve/twenty)", "anotar la puerta como si fuera el lugar"], "Reconoce los datos que acertó y repasa la diferencia entre twelve (12) y twenty (20) con la persona adulta."),
    "Pide a un adulto que lea de nuevo el texto de la salida y escribe solo las palabras clave en tu hoja.",
    "Inventa un aviso de salida con día, hora, lugar y dos cosas que traer, y pide a otra persona que anote los datos.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA1, 4,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a relacionar quién habla, qué acciones realiza cada persona y dónde ocurre la situación. Sirve para entender escenas con varios personajes.",
    ["Sé reconocer la idea general de un texto oral.", "Conozco verbos como peel, wash, ask y add."],
    [
        "En un texto oral con varias personas conviene preguntar tres cosas: quién habla (speaker), qué hace cada uno (action) y dónde ocurre todo (setting). Los nombres propios, los títulos como Chef o Driver y los pronombres he (él) y she (ella) te dicen quién actúa.",
        "Los verbos en tercera persona del presente terminan en -s, como peels, washes, tastes y adds. Ese -s indica que habla de una sola persona (he, she, Rosa). Si oyes dos nombres y dos verbos distintos, asocia cada acción con su persona: Iván peels the carrots y Rosa washes the potatoes. Así evitas mezclar quién hizo qué.",
        "El lugar y el momento aparecen en frases como in the school kitchen, at a bus stop, late at night o across the street. A veces el lugar no se nombra, pero las palabras lo sugieren: soup, carrots y chef hablan de una cocina. En las conversaciones, escucha también quién pregunta y quién responde.",
    ],
    [("speaker", "hablante: quien habla"), ("action", "acción: lo que alguien hace"), ("setting", "lugar y momento donde ocurre algo"), ("he / she", "él / ella"), ("peels / washes / adds", "pela / lava / agrega (una sola persona)"), ("across the street", "al otro lado de la calle")],
    [
        ("Acción de cada persona", ADULT + SOUP + " ¿Qué hace Rosa?", ["Busco el nombre Rosa.", "La oración dice Rosa washes the potatoes.", "Washes es lava."], "Lava las papas"),
        ("Quién pregunta y quién responde", ADULT + BUS + " ¿Quién pregunta si el bus va al hospital?", ["Busco la pregunta: does this bus go to the hospital?", "Quien la dice es Lucía.", "El conductor responde que necesita el número 14."], "Lucía"),
    ],
    [
        ("Asignar la acción de una persona a otra, por ejemplo decir que Rosa pela las zanahorias.", "Se escucha el verbo, pero no se asocia con el nombre.", "Cada vez que oigas un verbo con -s, busca el nombre que lo acompaña."),
        ("Decir que la escena ocurre en el hospital porque se nombra el hospital.", "Se confunde el destino que se menciona con el lugar donde están los hablantes.", "Fíjate en frases como at a bus stop, que dicen dónde están."),
    ],
    [
        (ADULT + SOUP + " ¿Dónde ocurre la escena? a) en la cocina del colegio b) en un parque", "a) en la cocina del colegio", "Dice in the school kitchen."),
        (ADULT + SOUP + " ¿Quién pela las zanahorias? a) Iván b) Rosa", "a) Iván", "Dice Iván peels the carrots."),
        (ADULT + BUS + " ¿Dónde está Lucía? a) en un paradero de bus b) dentro del hospital", "a) en un paradero de bus", "Dice at a bus stop; el hospital es su destino."),
    ],
    [
        (ADULT + SOUP + " ¿Quién prueba la sopa? a) la cocinera Mara b) Rosa c) Iván", "a) la cocinera Mara", "Dice Chef Mara tastes the soup."),
        (ADULT + BUS + " ¿Qué número de bus necesita Lucía?", "14", "El conductor dice you need the number 14."),
        (ADULT + BUS + " ¿Cuántos minutos pasan entre un bus 14 y el siguiente?", "10", "Dice every ten minutes."),
    ],
    [
        (ADULT + SOUP + " ¿Qué hace Iván al final? a) agrega un poco de sal b) lava las papas", "a) agrega un poco de sal", "Chef Mara dice que falta sal e Iván adds a little salt."),
        (ADULT + SOUP + " ¿Cuántas personas hay en la cocina?", "3", "Hay una cocinera, Mara, y dos estudiantes, Iván y Rosa."),
        (ADULT + BUS + " ¿Dónde se detiene el bus 14? a) al otro lado de la calle b) en la puerta del hospital", "a) al otro lado de la calle", "Dice It stops across the street."),
    ],
    [
        (ADULT + SOUP + " Daniel dice: «Rosa le agrega la sal a la sopa». ¿Qué parte del texto muestra que se equivoca?", "Iván adds a little salt", "Quien agrega la sal es Iván, no Rosa."),
        (ADULT + BUS + " Con las pistas del texto, ¿a qué hora del día ocurre la escena? a) de noche b) de mañana", "a) de noche", "Dice Late at night."),
    ],
    [
        (ADULT + SOUP + " Si Chef Mara dijera «It needs more pepper», ¿qué haría falta en la sopa? (pepper = pimienta)", "Pimienta", "Needs more indica lo que falta; pepper es pimienta."),
        (ADULT + "«In the library, Pablo reads a comic and Nora writes a poem. The librarian, Mr. Ríos, stamps the books. Pablo asks him: Can I borrow this comic? Mr. Ríos says: Yes, for two weeks.» (comic = historieta, writes = escribe, poem = poema, stamps = timbra, borrow = pedir prestado, weeks = semanas). ¿Por cuánto tiempo puede llevarse Pablo el cómic?", "Dos semanas", "Mr. Ríos responde for two weeks."),
    ],
    [(ADULT + "«On a rainy afternoon at the bus terminal, a grandmother asks a young man for help with her bag. He carries the bag to platform 5. She says thank you and gives him a mandarin.» (rainy = lluviosa, terminal = terminal, bag = bolso, carries = lleva, platform = andén, mandarin = mandarina). ¿Qué hace el joven y a dónde va?", "Lleva el bolso de la abuela al andén 5", "Dice He carries the bag to platform 5.")],
    [
        ("¿Qué indica el -s final en «washes»?", "Que habla de una sola persona", "Es el presente de he, she o un nombre."),
        ("¿Qué significa «across the street»?", "Al otro lado de la calle", "Es una frase de lugar."),
        ("¿Para qué sirve preguntar «who, what, where»?", "Para relacionar quién hace qué y dónde", "Organiza la información de la escena."),
    ],
    task("Un adulto lee dos veces esta escena: «On Saturday morning at the farmers' market, Gabriela sells tomatoes. Her cousin Leo packs the bags. A customer asks: How much are the tomatoes? Gabriela says: Two thousand pesos a kilo.» (farmers' market = feria, sells = vende, packs = embolsa, customer = cliente, how much = cuánto cuestan). Haz una tabla con tres columnas: quién, qué hace, dónde. Completa una fila por cada personaje.", "Gabriela, vende tomates, en la feria. Leo, embolsa, en la feria. El cliente, pregunta el precio, en la feria.", ["incluye a tres personajes", "une cada acción con la persona correcta", "indica el lugar"], ["tabla en la hoja", "nota del adulto"], ["asignar la venta a Leo", "olvidar al cliente"], "Reconoce las filas que acertó y vuelve a escuchar solo el verbo de cada persona."),
    "Pide a un adulto que lea la escena de la cocina y señala con el dedo a la persona que realiza cada acción.",
    "Cambia los nombres y las acciones de la escena de la cocina para escribir una escena nueva de tres frases.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA1, 5,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a responder sobre un texto oral y a mostrar la pista que respalda mi respuesta. Sirve para demostrar que entendí y para corregirme cuando me equivoco.",
    ["Sé ubicar datos explícitos y la idea general.", "Sé relacionar quién hace qué y dónde."],
    [
        "Mostrar comprensión no es solo responder: es justificar. Una buena respuesta tiene dos partes: la respuesta (answer) y la evidencia (evidence), que es la palabra o frase del texto que la respalda. Por ejemplo: «El partido es el domingo, porque dicen It's on Sunday at eleven».",
        "Sigue tres pasos. Primero, lee la pregunta y decide qué buscas. Segundo, escucha otra vez con ese propósito. Tercero, elige una respuesta y cita la pista. Si la pista no calza con tu respuesta, cámbiala. Esto se llama revisar una predicción: pensabas una cosa, el texto dice otra, y corriges.",
        "Cuidado con los cambios. En el mensaje de voz, el partido estaba planeado para el sábado, pero cambió al domingo por la lluvia. Palabras como not, now y because avisan un cambio y su razón. Responde siempre con la información más reciente, no con la primera que oíste.",
    ],
    [("answer", "respuesta"), ("evidence", "evidencia: frase del texto que respalda"), ("check", "revisar, comprobar"), ("change", "cambio"), ("because", "porque"), ("not... now", "ya no... ahora")],
    [
        ("Responder con evidencia", ADULT + VOICE + " ¿Cuándo es el partido? Responde y cita la pista.", ["Pienso que dice Saturday, pero escucho con cuidado.", "Dice It's on Sunday at eleven.", "Corrijo mi predicción: el partido es el domingo a las 11."], "El domingo a las 11; pista: It's on Sunday at eleven"),
        ("Revisar una predicción", ADULT + WEATHER + " Alguien predice: «En el sur hará calor». ¿Qué dice el texto?", ["Busco south en el texto.", "Dice windy and cold, nine degrees.", "La predicción no calza: hace frío y viento."], "Hace frío y viento, nueve grados"),
    ],
    [
        ("Responder con la primera información (sábado) y no con el cambio.", "No se escucha la parte que corrige lo anterior.", "Atiende a palabras como not y now, y responde con lo más reciente."),
        ("Dar una respuesta sin decir qué frase del texto la apoya.", "Parece correcta, pero no demuestra que se entendió.", "Agrega siempre la pista: «porque dicen...»."),
    ],
    [
        (ADULT + VOICE + " ¿Por qué cambió el día del partido? a) porque llueve el sábado b) porque falta una polera", "a) porque llueve el sábado", "Dice because it is raining on Saturday."),
        (ADULT + VOICE + " ¿A quién deja el mensaje Sofía? a) a Diego b) al entrenador", "a) a Diego", "Comienza con Hi Diego."),
        (ADULT + VOICE + " ¿Qué debe llevar el equipo? a) la polera azul b) la pelota", "a) la polera azul", "Dice Bring your blue shirt."),
    ],
    [
        (ADULT + WEATHER + " ¿Cuántos grados harán en el norte?", "32", "Dice thirty-two degrees."),
        (ADULT + WEATHER + " ¿Cómo estará el centro? a) nublado, con lluvia ligera en la tarde b) soleado y caluroso", "a) nublado, con lluvia ligera en la tarde", "Dice cloudy with light rain in the afternoon."),
        (ADULT + WEATHER + " ¿Qué frase del texto respalda que hará frío en el sur? a) windy and cold b) sunny and hot", "a) windy and cold", "Cold significa frío; sunny and hot corresponde al norte."),
    ],
    [
        arith(ADULT + WEATHER + " ¿Cuántos grados más hará en el norte que en el sur?", "32-9", "Se resta la temperatura del sur a la del norte.", " grados"),
        (ADULT + VOICE + " Una persona escribe: «El partido es el sábado». ¿Qué frase del mensaje la contradice?", "The football match is not on Saturday now", "El mensaje dice que ya no es el sábado."),
        (ADULT + WEATHER + " ¿En cuál zona conviene llevar paraguas? a) en el centro b) en el norte", "a) en el centro", "Solo en el centro dice light rain."),
    ],
    [
        (ADULT + "«The talent show is on Friday at six. First, Class 7A sings. Second, Class 7B dances. Finally, Class 7C plays the guitar. After the show, everyone eats pizza.» (talent show = show de talentos, sings = canta, dances = baila, plays = toca, guitar = guitarra, pizza = pizza). ¿Qué curso baila? a) 7B b) 7C", "a) 7B", "Second, Class 7B dances."),
        (ADULT + "«The talent show is on Friday at six. First, Class 7A sings. Second, Class 7B dances. Finally, Class 7C plays the guitar. After the show, everyone eats pizza.» (finally = finalmente). ¿Qué curso cierra el show?", "7C", "Finally, Class 7C plays the guitar marca el último número."),
    ],
    [
        (ADULT + "«Mrs. Vega says: The recycling day was Monday, but it is Wednesday this week. Please put the paper in the blue bin and the plastic in the yellow bin. Glass goes to the green container outside the gate.» (recycling = reciclaje, bin = contenedor, glass = vidrio, gate = portón). ¿Qué día es el reciclaje esta semana? a) el miércoles b) el lunes", "a) el miércoles", "El texto corrige el día habitual con but it is Wednesday this week."),
        (ADULT + "«Mrs. Vega says: The recycling day was Monday, but it is Wednesday this week. Please put the paper in the blue bin and the plastic in the yellow bin. Glass goes to the green container outside the gate.» (paper = papel, plastic = plástico). ¿En qué contenedor va el plástico? a) en el amarillo b) en el azul", "a) en el amarillo", "Dice the plastic in the yellow bin."),
    ],
    [(ADULT + "Un compañero deja este mensaje: «I cannot come to the study group today. My little sister has a cold, so I have to stay home. Can you send me the homework for English?» (study group = grupo de estudio, cold = resfrío, stay = quedarse, send = enviar). ¿Por qué no puede ir al grupo y qué pide?", "Porque su hermana tiene resfrío y debe quedarse en casa; pide la tarea de inglés", "Dice so I have to stay home y Can you send me the homework for English?")],
    [
        ("En Inglés de 7.º (OA 1, clase 5): ¿Qué dos partes tiene una buena respuesta?", "La respuesta y la evidencia", "La evidencia es la pista del texto."),
        ("En Inglés de 7.º (OA 1, clase 5): ¿Qué significa «because»?", "Porque", "Because introduce una razón."),
        ("¿Qué haces si tu predicción no calza con el texto?", "La corrijo", "Revisar la predicción es parte de comprender."),
    ],
    task("Un adulto lee dos veces este mensaje: «Hello, I'm calling about the art class. It is not on Tuesday now. It is on Thursday at five because the teacher is sick on Tuesday. Please bring paper and paint.» (calling = llamando, art class = clase de arte, sick = enfermo, paper = papel, paint = pintura). Escribe tres respuestas con su evidencia: 1) cuándo es la clase, 2) por qué cambió, 3) qué hay que llevar.", "1) El jueves a las 5, pista: It is on Thursday at five. 2) Porque el profesor está enfermo, pista: the teacher is sick. 3) Papel y pintura, pista: bring paper and paint.", ["responde las tres preguntas", "incluye una pista del texto en cada una", "usa la información más reciente"], ["hoja con tres respuestas y tres pistas", "nota del adulto"], ["responder martes", "no citar la pista"], "Reconoce las respuestas correctas y repasa con la persona dónde estaba la palabra not."),
    "Pide a un adulto que lea de nuevo el mensaje del partido y subraya en tu hoja la palabra que avisa el cambio.",
    "Escribe en inglés un mensaje de voz de tres frases con un cambio de plan y su razón, usando not, now y because.",
)
