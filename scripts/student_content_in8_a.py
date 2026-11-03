"""Cuaderno del estudiante, 8.º básico Inglés (oficial), IN08 OA 01 y OA 02 (comprensión oral y lenguaje clave/sonidos).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan pista en español. Todo término nuevo se explica antes de usarlo.
Este módulo define también el ayudante `lesson` que importan los demás módulos in8_*.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "IN08 OA 01"
OA2 = "IN08 OA 02"
ADULT = "Un adulto lee en voz alta (tapa el guion): "
MAT_L = "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz."
MAT_R = "Los textos escritos en cada ejercicio, lápiz y una hoja para anotar."


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


# ------------------------------------------------------------------ textos OA 1, clase 1
INTV = "«Reporter: Welcome, Camila. You are the youngest skater in the regional championship. How often do you practise? Camila: I practise four days a week, usually after school. Reporter: What is the hardest part? Camila: Falling! But I always stand up and try again.» (reporter = periodista, youngest = la más joven, skater = patinadora, practise = practicar, usually = normalmente, hardest = lo más difícil, falling = caerse, stand up = levantarse)"
ANEC = "«Last summer, I went to the market with my uncle. I wanted to buy peaches, but I forgot my wallet. The seller smiled and said: Pay me tomorrow. The next day, I took the money and a drawing for her. She put it on her stall. I was so proud!» (peaches = duraznos, wallet = billetera, seller = vendedora, smiled = sonrió, pay = paga, drawing = dibujo, stall = puesto, proud = orgulloso)"
EXPO = "«Good afternoon, everyone. Today I will talk about the Atacama Desert. It is one of the driest places in the world. It is in the north of Chile. Some parts get almost no rain in a whole year. But animals and plants live there, and at night the sky is full of stars.» (desert = desierto, driest = más seco, get = recibir, whole = entero, plants = plantas, full of = lleno de, stars = estrellas)"
PROC = "«To make a bookmark, first take a strip of thick paper. Next, draw a pattern on it. Then colour it with pencils. Finally, tie a ribbon at the top.» (bookmark = marcapáginas, strip = tira, thick = grueso, pattern = diseño, colour = colorear, ribbon = cinta)"

lesson(
    OA1, 1, MAT_L,
    "Aprenderé a reconocer entrevistas, anécdotas, exposiciones y procedimientos al escucharlos, y a decir para qué se dicen. Sirve para saber qué buscar antes de entender los detalles.",
    ["Sé que un texto oral puede informar, contar o dar instrucciones.", "Conozco palabras como first, then, last y yesterday."],
    [
        "En 8.º escuchas textos más variados. Una entrevista (interview) tiene un periodista que pregunta y una persona que responde por turnos. Una anécdota (anecdote) es un relato breve de algo que le pasó al hablante, casi siempre en pasado. Una exposición (talk) es un texto en que una persona presenta un tema a una audiencia. Un procedimiento (procedure) explica cómo hacer algo paso a paso.",
        "Cada tipo deja pistas. En la entrevista hay preguntas, como How often do you practise?, y respuestas con I. En la anécdota aparecen verbos en pasado, como went, wanted y forgot, y marcas como Last summer o The next day. La exposición comienza con un saludo a todos, como Good afternoon, everyone, y anuncia el tema con Today I will talk about. El procedimiento ordena los pasos con first, next, then y finally.",
        "El propósito (purpose) es la razón por la que se habla: conocer a una persona, compartir una experiencia, informar sobre un tema o enseñar a hacer algo. Si identificas el tipo y el propósito, sabes qué escuchar: en una entrevista, qué dice la persona; en una anécdota, qué pasó y cómo termina; en un procedimiento, el orden de los pasos.",
    ],
    [("interview", "entrevista: preguntas y respuestas por turnos"), ("anecdote", "anécdota: relato breve de algo que le pasó a alguien"), ("talk", "exposición: una persona presenta un tema"), ("procedure", "procedimiento: pasos para hacer algo"), ("purpose", "propósito: para qué se dice un texto"), ("audience", "audiencia: personas que escuchan")],
    [
        ("Reconocer una entrevista", ADULT + INTV + " ¿Qué tipo de texto es y cuál es la pista?", ["Hay un reportero y una deportista que hablan por turnos.", "El reportero hace preguntas y Camila las responde.", "Esa estructura de pregunta y respuesta es la de una entrevista."], "Es una entrevista: el periodista pregunta y Camila responde"),
        ("Reconocer el propósito de una anécdota", ADULT + ANEC + " ¿Cuál es el propósito del texto?", ["Verbos como went, wanted y forgot están en pasado.", "El hablante cuenta algo que le ocurrió, con un final emotivo (I was so proud).", "No enseña pasos ni presenta un tema general."], "Compartir una experiencia personal"),
    ],
    [
        ("Pensar que un texto con muchos datos es una entrevista.", "Se confunde el tipo de texto con la cantidad de datos; una entrevista exige preguntas y respuestas.", "Busca si hay dos hablantes que se turnan con preguntas."),
        ("Decir que una anécdota enseña a hacer algo.", "Se confunde el propósito: la anécdota cuenta una vivencia, no entrega pasos.", "Pregunta si el hablante cuenta lo que le pasó o si da pasos para seguir."),
    ],
    [
        (ADULT + INTV + " ¿Qué tipo de texto es? a) una entrevista b) un aviso de colegio", "a) una entrevista", "Un periodista hace preguntas y Camila responde por turnos."),
        (ADULT + ANEC + " ¿Qué tipo de texto es? a) una anécdota b) unas instrucciones", "a) una anécdota", "Cuenta algo que le pasó al hablante en el pasado."),
        (ADULT + EXPO + " ¿Qué tipo de texto es? a) una exposición b) una conversación entre amigos", "a) una exposición", "Una persona presenta un tema y saluda a todos."),
    ],
    [
        (ADULT + INTV + " ¿Para qué se hizo esta entrevista? a) para conocer cómo entrena una patinadora b) para vender patines c) para anunciar un campeonato nuevo", "a) para conocer cómo entrena una patinadora", "Las preguntas son sobre cuántos días practica y qué le cuesta más."),
        (ADULT + PROC + " ¿Qué pista muestra que son instrucciones? a) first, next, then y finally ordenan los pasos b) hay dos hablantes que se turnan c) aparece la frase Last summer", "a) first, next, then y finally ordenan los pasos", "Esas palabras marcan el orden de los pasos de un procedimiento."),
        (ADULT + EXPO + " ¿Cuál es el tema? a) el desierto de Atacama b) la lluvia en Santiago c) los animales del mar", "a) el desierto de Atacama", "El hablante anuncia: Today I will talk about the Atacama Desert."),
    ],
    [
        (ADULT + "Tres mensajes. Mensaje A: «Welcome back, everyone. Today we will learn how plants make food.» Mensaje B: «Yesterday I missed the bus, so I ran to school and arrived five minutes late.» Mensaje C: «Reporter: Where do you train? Nora: In the park near my house.» (plants = plantas, missed = perdí, ran = corrí, arrived = llegué, late = tarde, train = entrenar). Clasifica cada mensaje: exposición, anécdota o entrevista.", "A exposición, B anécdota, C entrevista", "A presenta un tema a todos, B cuenta algo pasado y C tiene pregunta y respuesta."),
        (ADULT + ANEC + " ¿Qué quiere lograr quien cuenta? a) compartir una vivencia con un final emotivo b) enseñar a comprar duraznos", "a) compartir una vivencia con un final emotivo", "Cuenta lo que le pasó y termina con I was so proud."),
        (ADULT + EXPO + " ¿A quién le habla la persona? a) a una audiencia que escucha una charla b) a un amigo por teléfono", "a) a una audiencia que escucha una charla", "Good afternoon, everyone saluda a todos los presentes."),
    ],
    [
        ("Tomás dice que el texto del desierto es una entrevista porque tiene muchos datos. ¿Cuál es la respuesta correcta? a) No, porque una sola persona presenta y no hay preguntas ni respuestas b) Sí, porque los datos siempre indican una entrevista", "a) No, porque una sola persona presenta y no hay preguntas ni respuestas", "La entrevista exige preguntas y respuestas por turnos."),
        (ADULT + ANEC + " ¿Qué grupo de palabras muestra que lo contado ya pasó? a) went, wanted, forgot b) buy, pay, take", "a) went, wanted, forgot", "Son verbos en pasado: ir, querer y olvidar."),
    ],
    [
        (ADULT + PROC + " Un oyente solo entendió las palabras draw, colour y ribbon. ¿Qué tipo de texto podría ser? a) instrucciones para hacer una manualidad b) una entrevista deportiva", "a) instrucciones para hacer una manualidad", "Dibujar, colorear y cinta son acciones y materiales de una manualidad."),
        (ADULT + INTV + " Un oyente dice que el propósito es entretener con un cuento. Otro dice que es informar sobre la rutina de una deportista. ¿Quién tiene mejor evidencia? a) el segundo, por las preguntas sobre días de práctica y dificultad b) el primero, porque Camila habla de caerse", "a) el segundo, por las preguntas sobre días de práctica y dificultad", "Las preguntas piden información sobre su rutina, no cuentan un cuento."),
    ],
    [(ADULT + "Recibes un mensaje de voz: «Hi Lola, it's Dani. I'm at the station. The train is late, so I will arrive at a quarter past six. Please wait for me at the cafe.» (station = estación, late = atrasado, arrive = llegar, wait = esperar, cafe = cafetería). ¿Cuál es el propósito? a) avisar un atraso y pedir que la esperen b) contar una anécdota de viaje", "a) avisar un atraso y pedir que la esperen", "Dani explica el atraso con so y pide Please wait for me.")],
    [
        ("En Inglés de 8.º (OA 1, clase 1): ¿Qué es una anécdota?", "Un relato breve de algo que le pasó a alguien", "Cuenta una vivencia, normalmente en pasado."),
        ("En Inglés de 8.º (OA 1, clase 1): ¿qué palabras te avisan el orden de las acciones de un procedimiento?", "First, next, then y finally", "Marcan el orden de las acciones."),
        ("¿Qué tipo de texto tiene preguntas de un periodista y respuestas de otra persona?", "Una entrevista", "Se turnan preguntas y respuestas."),
    ],
    task("Un adulto lee dos veces este texto: «Hello, everyone. Today I want to talk about recycling paper. In our school, we use a lot of paper every week. If we use both sides of a page, we use less. Please put used paper in the blue box.» (recycling = reciclar, paper = papel, both sides = ambos lados, less = menos, used = usado, box = caja). Escribe en tu hoja el tipo de texto, su propósito y una frase que te lo mostró.", "Es una exposición. Su propósito es convencer de reciclar papel. La pista es Hello, everyone. Today I want to talk about…", ["nombra un tipo de texto coherente", "explica el propósito con sus palabras", "cita una frase del texto como pista"], ["hoja con tres respuestas", "nota del adulto"], ["decir que es una entrevista sin haber preguntas", "no citar ninguna pista"], "Reconoce lo que acertó y vuelve a escuchar solo la última frase para decidir qué quiere que haga la audiencia."),
    "Pide a un adulto que lea el texto de la entrevista y levanta la mano cada vez que oigas una pregunta.",
    "Escribe en español tres frases de una anécdota tuya y subraya las palabras que muestran que ya pasó.",
)

# ------------------------------------------------------------------ OA 1, clase 2
FAIR = "«Good morning. The school book fair opens on Tuesday in the library. There are two hundred and fifty books. Entry is free for students and two thousand five hundred pesos for visitors. The first one hundred visitors get a free poster. The fair closes on Friday at five thirty.» (book fair = feria del libro, opens = abre, entry = entrada, free = gratis, visitors = visitas, poster = afiche, closes = cierra)"
RACE = "«The school race has six runners. Ema is first, Bruno is second and Clara is third. Dario arrived fourth. The winner receives a medal.» (race = carrera, runners = corredores, arrived = llegó, winner = ganador, receives = recibe, medal = medalla)"
SHOP = "«Good morning. Today at the market, tomatoes are one thousand eight hundred pesos a kilo, lemons are one thousand two hundred, and onions are nine hundred. We have three hundred and forty kilos of potatoes. We open at nine in the morning and close at two in the afternoon.» (market = feria, lemons = limones, onions = cebollas, potatoes = papas, open = abrimos, close = cerramos)"
CHOIR = "«The choir practises on Thursday at half past four in the music room. The concert is in December, at seven in the evening. There are thirteen singers and three guitar players. The first song is a surprise.» (choir = coro, music room = sala de música, concert = concierto, singers = cantantes, guitar players = guitarristas, surprise = sorpresa)"

lesson(
    OA1, 2, MAT_L,
    "Aprenderé a escuchar números grandes, ordinales y horas para ubicar información exacta. Sirve para responder con precisión: cuántos, cuándo y en qué lugar.",
    ["Sé contar hasta cien en inglés.", "Conozco los días y los meses en inglés."],
    [
        "La información explícita (explicit information) es la que el texto dice con palabras claras. Para ubicarla, lee primero la pregunta y decide qué dato buscas: how many (cuántos), when (cuándo), where (dónde) o how much (cuánto cuesta). Anota solo palabras clave, no frases enteras: números, días, meses y lugares.",
        "En 8.º los números crecen: one hundred es 100, two hundred and fifty es 250 y one thousand two hundred es 1.200. Los ordinales indican la posición: first (1.º), second (2.º), third (3.º), fourth (4.º). Cuidado con los números que suenan parecido: thirteen (13) se acentúa al final y thirty (30) se acentúa al comienzo. También hay horas con partes: half past four es 4:30, a quarter past six es 6:15 y a quarter to six es 5:45.",
        "Las preposiciones de tiempo te ayudan: on se usa con días (on Tuesday), at con horas (at five thirty) e in con meses y partes del día (in December, in the afternoon). Antes de responder, comprueba que el dato que anotaste responde exactamente a la pregunta, no a otra parecida.",
    ],
    [("how many", "cuántos"), ("how much", "cuánto"), ("first, second, third", "primero, segundo, tercero"), ("half past", "y media"), ("a quarter past / to", "y cuarto / menos cuarto"), ("on / at / in", "con días / con horas / con meses")],
    [
        ("Ubicar un número", ADULT + FAIR + " ¿Cuántos libros hay?", ["La pregunta pide una cantidad: busco how many o el número junto a books.", "Dice two hundred and fifty books.", "Two hundred and fifty se escribe 250."], "250 libros"),
        ("Ubicar un ordinal", ADULT + RACE + " ¿Quién llegó segundo?", ["La pregunta pide una posición: busco second.", "Dice Bruno is second.", "Ema es primera y Clara tercera."], "Bruno"),
    ],
    [
        ("Anotar 30 cuando se dijo thirteen.", "Se confunden thirteen y thirty porque suenan parecidos.", "Escucha dónde cae la fuerza: thirTEEN termina fuerte; THIRty empieza fuerte."),
        ("Responder con un dato de otra pregunta, como el día de cierre cuando se pregunta la hora.", "Se anota lo primero que se oye y no lo que pide la pregunta.", "Relee la pregunta antes de escribir y marca la palabra clave que pide."),
    ],
    [
        (ADULT + SHOP + " ¿Cuánto cuesta un kilo de limones? a) 1.200 pesos b) 900 pesos", "a) 1.200 pesos", "Dice lemons are one thousand two hundred."),
        (ADULT + CHOIR + " ¿Qué día practica el coro? a) el jueves b) el martes", "a) el jueves", "Dice on Thursday."),
        (ADULT + CHOIR + " ¿En qué mes es el concierto? a) en diciembre b) en julio", "a) en diciembre", "Dice in December."),
    ],
    [
        (ADULT + SHOP + " ¿Cuántos kilos de papas hay? a) 340 b) 430 c) 304", "a) 340", "Three hundred and forty es 300 + 40."),
        (ADULT + CHOIR + " ¿Cuántos cantantes hay? a) 13 b) 30", "a) 13", "Dice thirteen singers; thirty sería 30."),
        (ADULT + SHOP + " ¿A qué hora cierra la feria? a) a las 2 de la tarde b) a las 9 de la mañana", "a) a las 2 de la tarde", "Dice close at two in the afternoon."),
    ],
    [
        arith(ADULT + SHOP + " Si compras 2 kilos de tomates, ¿cuántos pesos pagas?", "2*1800", "Un kilo cuesta 1.800 pesos.", " pesos"),
        arith(ADULT + SHOP + " ¿Cuántos pesos cuestan juntos un kilo de tomates y un kilo de limones?", "1800+1200", "Se suman 1.800 y 1.200.", " pesos"),
        arith(ADULT + CHOIR + " ¿Cuántos músicos hay en total, sumando cantantes y guitarristas?", "13+3", "Hay 13 cantantes y 3 guitarristas.", " personas"),
    ],
    [
        ("Mía anotó «30 cantantes» al escuchar el texto del coro. ¿Qué palabra oyó mal? a) thirteen, que es 13 b) three, que es 3", "a) thirteen, que es 13", "Confundió thirteen con thirty."),
        (ADULT + SHOP + " ¿Cuál de los tres productos con precio es el más barato por kilo? a) las cebollas b) los limones", "a) las cebollas", "Cuestan 900 pesos, menos que 1.200 y 1.800."),
    ],
    [
        (ADULT + "«Practice starts at a quarter to six.» (practice = práctica). ¿A qué hora empieza? a) a las 5:45 b) a las 6:15", "a) a las 5:45", "A quarter to six es un cuarto antes de las seis."),
        arith(ADULT + SHOP + " ¿Cuántas horas está abierta la feria, de las 9 de la mañana a las 2 de la tarde (14 horas en reloj de 24)?", "14-9", "Se resta la hora de apertura a la de cierre.", " horas"),
    ],
    [arith(ADULT + "En el terminal oyes: «The bus to Chillán leaves from platform twelve at eight forty. Tickets cost eight thousand five hundred pesos each.» (platform = andén, leaves = sale, tickets = pasajes, each = cada uno). ¿Cuántos pesos pagan tres personas por sus pasajes?", "3*8500", "Cada pasaje cuesta 8.500 pesos.", " pesos")],
    [
        ("¿Dónde se acentúa thirteen?", "En el final, -teen", "Thirteen termina fuerte; thirty empieza fuerte."),
        ("¿Cómo se dice «y cuarto» al dar la hora en inglés?", "Quarter past", "Quarter past six es 6:15."),
        ("¿Qué número es «two hundred and fifty»?", "250", "Son 200 más 50."),
    ],
    task("Un adulto lee dos veces este mensaje: «Welcome to the science fair. It is on Friday from nine to twelve in the gym. There are twelve projects. The prize is a book. Visitors enter by the blue door.» (science fair = feria científica, gym = gimnasio, project = proyecto, prize = premio, visitors = visitas, enter = entrar). Escribe en tu hoja el día, el lugar, cuántos proyectos hay y cuál es el premio.", "Viernes; en el gimnasio; 12 proyectos; un libro.", ["anota los cuatro datos", "usa solo lo que dice el texto", "escribe en español o en inglés"], ["hoja con cuatro datos", "nota del adulto"], ["anotar 20 proyectos en vez de 12", "anotar la puerta azul como si fuera el lugar"], "Reconoce los datos que acertó y repasa la diferencia entre twelve (12) y twenty (20) con la persona adulta."),
    "Pide a un adulto que lea de nuevo el texto del coro y anota solo las palabras clave: día, hora, mes y números.",
    "Escribe un aviso de seis líneas con día, hora, lugar y dos números grandes, y pide a otra persona que anote los datos al escucharlo.",
)

# ------------------------------------------------------------------ OA 1, clase 3
BIKES = "«I need a bike for school. Bike one is cheaper than bike two, but bike two is lighter and faster. Bike two has gears; bike one does not. In my opinion, bike two is the best choice, so I will save money for two months.» (cheaper = más barata, lighter = más liviana, faster = más rápida, gears = cambios, opinion = opinión, choice = elección, save = ahorrar)"
ROOMS = "«Our school has four rooms for clubs. The gym is bigger than the library, but the library is quieter. The art room is the smallest, and it is the brightest room because it has four big windows. The music room is the noisiest.» (rooms = salas, bigger = más grande, quieter = más silenciosa, smallest = la más pequeña, brightest = la más luminosa, windows = ventanas, noisiest = la más ruidosa)"
PETS = "«My neighbour has a dog and a cat. The dog is older than the cat, and it is also friendlier. The cat is more independent than the dog. In the evening, the dog sleeps by the door, and the cat sleeps on the sofa.» (neighbour = vecino, older = mayor, friendlier = más amistoso, independent = independiente, than = que, door = puerta, sofa = sofá)"

lesson(
    OA1, 3, MAT_L,
    "Aprenderé a usar la estrategia de escuchar con un propósito y a reconocer comparaciones (-er than, the -est). Sirve para entender textos que comparan personas, lugares o cosas.",
    ["Sé reconocer el tipo de texto y ubicar datos exactos.", "Conozco adjetivos como big, small, old y fast."],
    [
        "Una estrategia (strategy) es un plan para entender mejor. Una buena estrategia al escuchar es fijar un propósito antes de empezar: decidir qué quieres saber. Si la pregunta es «cuál es mejor», escucha las comparaciones. Después de escuchar, resume en una frase lo que entendiste.",
        "Comparar (to compare) es decir en qué se parecen o se diferencian dos cosas. Con dos cosas, el adjetivo corto lleva -er y luego than: cheaper than (más barata que), bigger than (más grande que). Con adjetivos largos se usa more: more independent (más independiente). Con tres o más cosas se usa the + -est o the most: the smallest (la más pequeña), the noisiest (la más ruidosa).",
        "Algunas palabras cambian al comparar: big pasa a bigger, y noisy pasa a noisier y noisiest. También existen formas irregulares: good, better, the best. Al escuchar, anota el adjetivo y de qué objeto se dice. Así evitas decir que la bicicleta más barata es también la más liviana.",
    ],
    [("strategy", "estrategia: plan para entender mejor"), ("compare", "comparar: ver parecidos y diferencias"), ("cheaper than", "más barata que"), ("the smallest", "la más pequeña"), ("the best", "el mejor"), ("more ... than", "más ... que")],
    [
        ("Comparación entre dos", ADULT + BIKES + " ¿Qué bicicleta es más barata?", ["Busco la palabra cheaper y than.", "Dice Bike one is cheaper than bike two.", "Cheaper significa más barata."], "La bicicleta uno"),
        ("Superlativo entre tres", ADULT + ROOMS + " ¿Cuál es la sala más pequeña?", ["Busco smallest, que es el superlativo de small.", "Dice The art room is the smallest.", "Es la sala de arte."], "La sala de arte"),
    ],
    [
        ("Pensar que cheaper quiere decir «mejor».", "Se confunde barata con buena; el hablante prefiere la más cara.", "Anota el adjetivo exacto de cada comparación."),
        ("Responder con la sala equivocada porque se nombró más veces.", "Se elige el objeto que más suena, no el que cumple el adjetivo.", "Pregúntate: ¿qué adjetivo pide la pregunta y a qué objeto se aplica?"),
    ],
    [
        (ADULT + BIKES + " ¿Qué bicicleta es más liviana? a) la dos b) la uno", "a) la dos", "Dice bike two is lighter."),
        (ADULT + ROOMS + " ¿Cuál sala es la más ruidosa? a) la sala de música b) la biblioteca", "a) la sala de música", "Dice The music room is the noisiest."),
        (ADULT + PETS + " ¿Quién es mayor? a) el perro b) el gato", "a) el perro", "Dice The dog is older than the cat."),
    ],
    [
        (ADULT + BIKES + " ¿Qué hará la persona para comprar la bicicleta que prefiere? a) ahorrar dinero por dos meses b) pedir una prestada", "a) ahorrar dinero por dos meses", "Dice I will save money for two months."),
        (ADULT + ROOMS + " ¿Por qué la sala de arte es la más luminosa? a) porque tiene cuatro ventanas grandes b) porque es la más grande", "a) porque tiene cuatro ventanas grandes", "Dice it has four big windows; además es la más pequeña."),
        (ADULT + PETS + " ¿Cuál animal es más amistoso? a) el perro b) el gato c) los dos por igual", "a) el perro", "Dice it is also friendlier."),
    ],
    [
        (ADULT + BIKES + " ¿Cuál es la idea general? a) la persona compara dos bicicletas y prefiere la más liviana y rápida b) la persona vende una bicicleta barata c) la persona repara los cambios", "a) la persona compara dos bicicletas y prefiere la más liviana y rápida", "Resume la comparación y la elección final."),
        (ADULT + PETS + " ¿Dónde duerme el gato? a) en el sofá b) junto a la puerta", "a) en el sofá", "Dice the cat sleeps on the sofa; el perro duerme junto a la puerta."),
        (ADULT + ROOMS + " Entre el gimnasio y la biblioteca, ¿cuál es más silenciosa? a) la biblioteca b) el gimnasio", "a) la biblioteca", "Dice the library is quieter."),
    ],
    [
        (ADULT + BIKES + " Valentina dice que la persona prefiere la bicicleta más barata. ¿Qué frase del texto la contradice? a) bike two is the best choice b) bike one is cheaper than bike two", "a) bike two is the best choice", "Elige la dos, que es más cara pero más liviana y rápida."),
        (ADULT + ROOMS + " Si solo oyeras «the biggest» y «the smallest», ¿cuántas salas se comparan como mínimo? a) tres b) dos", "a) tres", "El superlativo compara tres o más cosas."),
    ],
    [
        (ADULT + "«Our class has three plants. The fern is taller than the cactus, but the cactus is the oldest. The basil is the smallest, and it needs more water than the other two.» (plants = plantas, fern = helecho, taller = más alta, cactus = cactus, oldest = la más vieja, basil = albahaca, needs = necesita). ¿Qué planta es la más vieja? a) el cactus b) el helecho", "a) el cactus", "Dice the cactus is the oldest."),
        (ADULT + "«Our class has three plants. The fern is taller than the cactus, but the cactus is the oldest. The basil is the smallest, and it needs more water than the other two.» (taller = más alta, smallest = la más pequeña, needs = necesita, water = agua). ¿Qué planta necesita más agua? a) la albahaca b) el cactus", "a) la albahaca", "Dice the basil needs more water than the other two."),
    ],
    [(ADULT + "Tu curso escucha una opinión: «Of the two buses, the express bus is faster than the local bus, but the local bus is cheaper. I think the express bus is better because I have little time.» (express = directo, local = local, little time = poco tiempo). ¿Qué bus elige la persona y por qué? Responde en español.", "El directo, porque es más rápido y tiene poco tiempo", "Elige el express por la rapidez, aunque cueste más.")],
    [
        ("En Inglés de 8.º (OA 1, clase 3): ¿Qué es una estrategia de escucha?", "Un plan para entender mejor lo que se escucha", "Por ejemplo, fijar un propósito antes de escuchar."),
        ("¿Cómo se forma la comparación de «cheap» entre dos cosas?", "Cheaper than", "Se agrega -er y se usa than."),
        ("¿Qué significa «the smallest»?", "La más pequeña", "Es el superlativo de small."),
    ],
    task("Un adulto lee dos veces este texto: «We have two ways to school. The path through the park is longer than the street, but it is quieter and safer. The street is the fastest way, so I use it when I am late.» (path = camino, park = parque, longer = más largo, safer = más seguro, fastest = el más rápido, late = atrasado). Escribe en tu hoja qué camino es más largo, cuál es el más rápido y cuándo se usa cada uno.", "El camino por el parque es más largo y más seguro; la calle es el camino más rápido y se usa cuando va atrasado.", ["identifica el camino más largo", "identifica el más rápido", "dice cuándo se usa la calle"], ["hoja con tres respuestas", "nota del adulto"], ["mezclar longer con fastest", "no decir cuándo usa la calle"], "Reconoce lo que acertó y pide volver a escuchar solo las dos comparaciones para ubicarlas."),
    "Pide a un adulto que lea el texto de las bicicletas y subraya cada comparación que oigas.",
    "Escribe dos frases en inglés que comparen tu mochila con la de otra persona usando bigger than y lighter than.",
)

# ------------------------------------------------------------------ OA 1, clase 4
M_SOL = "Mensaje de Sol: «Hi, it's Sol. The cinema trip is on Saturday. We meet at the bus stop at two o'clock.»"
M_MARCO = "Mensaje de Marco: «Hi, it's Marco. The ticket costs three thousand pesos. We come back at six.»"
M_NORA = "Mensaje de Nora: «Hello, team. Sports day is next Friday. There are four teams: red, blue, green and yellow. The first game starts at ten o'clock.»"
M_ABEL = "Mensaje de Abel: «Hi, it's Abel. Please bring a hat and a bottle of water. Our team colour is green. We play on the big field.»"

lesson(
    OA1, 4, MAT_L,
    "Aprenderé a juntar los datos de dos mensajes orales para completar la información y a preguntar lo que falta. Sirve para organizar una actividad cuando cada persona sabe solo una parte.",
    ["Sé ubicar datos exactos como día, hora, precio y lugar.", "Conozco preguntas como When is...? y What time...?"],
    [
        "A veces la información está repartida: cada persona sabe solo una parte. A eso se le llama una brecha de información (information gap). Para cerrarla, escuchas con cuidado a cada hablante, anotas sus datos en una tabla y juntas las partes. Una tabla simple tiene columnas como day (día), place (lugar), time (hora), price (precio) y bring (qué llevar).",
        "Si falta un dato, haces una pregunta. Las preguntas más útiles empiezan con What (qué), Where (dónde), When (cuándo), Which (cuál) y How much (cuánto cuesta). What time is the game? pregunta la hora. Which cinema is it? pregunta cuál cine. Could you repeat that, please? pide que repitan. Una buena pregunta es corta, usa una palabra clave y pregunta solo por lo que falta.",
        "Antes de responder, revisa que los datos de los dos mensajes no se contradigan. Si uno dice two o'clock y el otro dice four o'clock, también debes preguntar para confirmar. Así evitas organizar un plan con datos que no coinciden.",
    ],
    [("information gap", "brecha de información: falta un dato que otra persona tiene"), ("table", "tabla: filas y columnas con datos"), ("ticket", "entrada o pasaje"), ("What time...?", "¿A qué hora...?"), ("Which...?", "¿Cuál...?"), ("Could you repeat that?", "¿Podría repetir eso?")],
    [
        ("Juntar dos mensajes", ADULT + M_SOL + " " + M_MARCO + " ¿Cuánto cuesta la entrada y a qué hora se reúnen?", ["El precio está en el mensaje de Marco: three thousand pesos.", "La hora de reunión está en el mensaje de Sol: two o'clock.", "Junto los dos datos."], "La entrada cuesta 3.000 pesos y se reúnen a las 2"),
        ("Preguntar lo que falta", ADULT + M_SOL + " " + M_MARCO + " ¿Qué dato no dicen ninguno de los dos? Escribe una pregunta en inglés para pedirlo.", ["Sol dice día, lugar de encuentro y hora; Marco dice precio y regreso.", "Ninguno dice cuál cine es.", "Una pregunta es Which cinema is it?"], "El nombre o cuál es el cine; Which cinema is it?"),
    ],
    [
        ("Anotar el dato de un mensaje como si fuera del otro.", "Se mezclan las fuentes y la tabla queda con datos equivocados.", "Escribe junto a cada dato el nombre de quien lo dijo."),
        ("Preguntar por algo que ya se dijo.", "No se revisó la tabla antes de preguntar.", "Mira primero qué casilla está vacía y pregunta solo por esa."),
    ],
    [
        (ADULT + M_SOL + " " + M_MARCO + " ¿A qué hora vuelven? a) a las 6 b) a las 2", "a) a las 6", "Marco dice We come back at six."),
        (ADULT + M_SOL + " " + M_MARCO + " ¿Qué día es la salida al cine? a) el sábado b) el viernes", "a) el sábado", "Sol dice The cinema trip is on Saturday."),
        (ADULT + M_NORA + " " + M_ABEL + " ¿De qué color es el equipo de Abel? a) verde b) rojo", "a) verde", "Abel dice Our team colour is green."),
    ],
    [
        (ADULT + M_NORA + " " + M_ABEL + " ¿Qué dos cosas deben llevar? a) un sombrero y una botella de agua b) una polera roja y una pelota c) dinero y una mochila", "a) un sombrero y una botella de agua", "Abel dice bring a hat and a bottle of water."),
        (ADULT + M_NORA + " " + M_ABEL + " ¿Cuántos equipos hay? a) 4 b) 6", "a) 4", "Nora nombra cuatro colores: red, blue, green and yellow."),
        (ADULT + M_NORA + " " + M_ABEL + " Si no hubieras oído la hora del primer partido, ¿qué pregunta la averigua? a) What time is the first game? b) Where is the big field?", "a) What time is the first game?", "What time pregunta por la hora."),
    ],
    [
        (ADULT + M_NORA + " " + M_ABEL + " Completa la tabla con una frase: día, color del equipo de Abel, hora del primer partido y qué llevar.", "Viernes próximo; verde; a las 10; un sombrero y agua", "El día y la hora los dice Nora; el color y lo que se lleva, Abel."),
        (ADULT + M_NORA + " " + M_ABEL + " ¿Quién dice dónde juegan? a) Abel b) Nora", "a) Abel", "Abel dice We play on the big field; Nora no nombra el lugar."),
        (ADULT + M_SOL + " " + M_MARCO + " Si un amigo pregunta «Where do we meet?», ¿quién tiene la respuesta? a) Sol: en el paradero b) Marco: en el cine", "a) Sol: en el paradero", "Sol dice We meet at the bus stop."),
    ],
    [
        (ADULT + M_SOL + " " + M_MARCO + " Daniel anotó «Nos juntamos a las 6». ¿Qué dato mezcló? a) la hora de regreso con la hora de reunión b) el precio con el día", "a) la hora de regreso con la hora de reunión", "Las 6 es la vuelta; la reunión es a las 2."),
        (ADULT + M_NORA + " " + M_ABEL + " Nadie dice cuántos jugadores tiene cada equipo. ¿Qué pregunta lo averigua? a) How many players are in each team? b) What colour is the team?", "a) How many players are in each team?", "How many pregunta por una cantidad."),
    ],
    [
        arith(ADULT + "Dos mensajes. Rita: «The art workshop is on Wednesday at four. It is in room twelve.» Pedro: «The workshop costs five thousand pesos, and we bring our own brushes.» (workshop = taller, room = sala, costs = cuesta, brushes = pinceles). ¿Cuántos pesos pagarían tres amigos por el taller?", "3*5000", "Cada persona paga 5.000 pesos.", " pesos"),
        (ADULT + "Dos mensajes. Rita: «The art workshop is on Wednesday at four. It is in room twelve.» Pedro: «The workshop costs five thousand pesos, and we bring our own brushes.» (room = sala, brushes = pinceles). ¿Qué debe llevar cada persona y en qué sala es? a) pinceles propios y sala 12 b) pintura y sala 5", "a) pinceles propios y sala 12", "Pedro dice los pinceles; Rita dice la sala."),
    ],
    [(ADULT + "Tu amigo Cris dice: «The match is on Sunday. I don't know the time.» Tu amiga Ema dice: «The match starts at eleven thirty, but I don't know the place.» (match = partido, place = lugar). ¿Qué dos datos tienes completos y cuál falta? Responde en español.", "Día domingo y hora 11:30; falta el lugar", "Cris da el día, Ema da la hora y nadie dice el lugar.")],
    [
        ("En Inglés de 8.º (OA 1, clase 4): ¿qué significa que hay una brecha de información entre dos mensajes?", "Que falta un dato que otra persona tiene", "Se cierra escuchando y preguntando."),
        ("¿Cómo preguntas en inglés a qué hora es algo?", "What time is it?", "What time pregunta por la hora."),
        ("¿Qué haces si dos mensajes dan horas distintas?", "Preguntar para confirmar cuál es la correcta", "Evita planes con datos que no coinciden."),
    ],
    task("Un adulto lee dos veces dos mensajes. Elisa: «The beach clean-up is on Sunday in the morning. We meet at the pier.» Joaquín: «Bring gloves and a bag. The clean-up finishes at twelve o'clock.» (clean-up = limpieza, pier = muelle, gloves = guantes, bag = bolsa, finishes = termina). Escribe una tabla con día, lugar, qué llevar y hora de término. Luego escribe una pregunta en inglés para el dato que no se dice (la hora de inicio).", "Domingo; el muelle; guantes y una bolsa; 12:00. Pregunta: What time does it start?", ["completa los cuatro datos", "indica que falta la hora de inicio", "escribe una pregunta con What time"], ["tabla de cuatro datos", "pregunta escrita"], ["mezclar quién dijo cada dato", "preguntar algo que ya se dijo"], "Reconoce qué casillas llenó bien y repasa What time para preguntar la hora."),
    "Pide a un adulto que lea los mensajes del cine y dibuja una tabla con día, lugar, hora y precio.",
    "Escribe dos mensajes breves de dos amigos que organizan una salida y deja un dato sin decir; luego escribe la pregunta que lo pediría.",
)

# ------------------------------------------------------------------ OA 1, clase 5
RHYME = "«A cat in a hat sat on a mat. It had a chat with a fat grey rat.» (cat = gato, hat = sombrero, sat = se sentó, mat = alfombra, chat = conversación, fat = gordo, rat = rata)"
RIDDLE = "«I have keys, but I have no doors. I have a screen, but I am not a television. You type on me. What am I?» (keys = teclas, doors = puertas, screen = pantalla, television = televisor, type = escribir a máquina)"
SONG = "«Monday, Tuesday, I walk to school. Wednesday, Thursday, I follow the rule. Friday comes and I feel free. Saturday is for you and me.» (walk = camino, follow = sigo, rule = regla, feel free = me siento libre)"
STORY8 = "«Mr. Vera is a baker. Every morning he gets up at four. He makes bread for the whole street. Last week, the oven stopped working. He called a technician, but the technician came late. So Mr. Vera made flatbread on a pan, and all his customers said it was delicious.» (baker = panadero, gets up = se levanta, oven = horno, technician = técnico, flatbread = pan plano, pan = sartén, customers = clientes, delicious = delicioso)"

lesson(
    OA1, 5, MAT_L,
    "Aprenderé a entender sola o solo rimas, adivinanzas, canciones y relatos breves originales, mostrando la idea general y un dato exacto. Sirve para demostrar que puedes escuchar de forma independiente.",
    ["Sé reconocer tipos de texto, ubicar datos y comparar.", "Conozco palabras de uso diario como morning, school y bread."],
    [
        "Los textos orales también pueden jugar con el sonido. Una rima (rhyme) tiene palabras que terminan con el mismo sonido, como cat, hat y mat. Un juego de palabras (wordplay) usa sonidos parecidos o pistas para que adivines algo. Una adivinanza (riddle) da pistas y termina con una pregunta. Una canción (song) tiene versos con ritmo y, a veces, rima.",
        "Con estos textos, escucha primero la idea general: de qué trata y cómo suena. Luego escucha una segunda vez para detalles exactos. En un relato breve, como el del panadero, busca quién (Mr. Vera), qué problema tuvo (the oven stopped working), qué hizo para solucionarlo (made flatbread on a pan) y cómo terminó (all his customers said it was delicious).",
        "Para trabajar de forma independiente, sigue tres pasos: escucha para la idea general, escucha para un dato exacto y revisa tu respuesta con una frase del texto. No necesitas entender todas las palabras; necesitas encontrar las pistas. Si dudas, vuelve a escuchar solo la parte donde estaba el dato.",
    ],
    [("rhyme", "rima: palabras con el mismo sonido final"), ("wordplay", "juego de palabras"), ("riddle", "adivinanza"), ("song", "canción"), ("problem", "problema"), ("solution", "solución")],
    [
        ("Rima", ADULT + RHYME + " ¿Qué dos palabras riman con cat y empiezan con h y m?", ["Una rima repite el sonido final: -at.", "Hat y mat terminan en -at igual que cat.", "Sat, chat, fat y rat también riman."], "Hat y mat"),
        ("Idea general de un relato", ADULT + STORY8 + " ¿Cuál es el problema y cuál la solución?", ["El problema es que el horno dejó de funcionar y el técnico llegó tarde.", "Mr. Vera hizo pan plano en una sartén.", "Los clientes dijeron que estaba delicioso."], "El horno falló; hizo pan plano en una sartén"),
    ],
    [
        ("Pensar que una rima rima por la letra inicial.", "La rima depende del sonido final, no de la primera letra.", "Compara cómo terminan las palabras al decirlas en voz alta."),
        ("Responder la adivinanza con la última cosa que se nombró.", "No se usan todas las pistas juntas.", "Reúne las pistas: teclas, pantalla y escribir."),
    ],
    [
        (ADULT + RIDDLE + " ¿Qué es? a) un teclado de computador b) una puerta", "a) un teclado de computador", "Tiene teclas y pantalla, y se escribe en él."),
        (ADULT + STORY8 + " ¿A qué hora se levanta Mr. Vera? a) a las 4 b) a las 8", "a) a las 4", "Dice he gets up at four."),
        (ADULT + SONG + " ¿Qué día se siente libre la persona? a) el viernes b) el lunes", "a) el viernes", "Dice Friday comes and I feel free."),
    ],
    [
        (ADULT + STORY8 + " ¿Qué dejó de funcionar la semana pasada? a) el horno b) la sartén c) el reloj", "a) el horno", "Dice the oven stopped working."),
        (ADULT + RHYME + " ¿Con quién conversó el gato? a) con una rata gris y gorda b) con un perro negro", "a) con una rata gris y gorda", "Dice it had a chat with a fat grey rat."),
        (ADULT + SONG + " ¿Con quién es el sábado? a) con otra persona (you and me) b) solo con la persona que canta", "a) con otra persona (you and me)", "Dice Saturday is for you and me."),
    ],
    [
        (ADULT + STORY8 + " ¿Cuál es la idea general? a) un panadero resolvió un problema del horno y a sus clientes les gustó b) un técnico arregló un horno c) una calle quedó sin pan", "a) un panadero resolvió un problema del horno y a sus clientes les gustó", "Resume problema, solución y final."),
        (ADULT + SONG + " ¿Cuál es la idea general? a) la semana va de caminar a la escuela a sentirse libre el fin de semana b) una carrera de caminata", "a) la semana va de caminar a la escuela a sentirse libre el fin de semana", "Los versos recorren los días de la semana."),
        (ADULT + RHYME + " ¿Cuál palabra NO rima con cat? a) grey b) rat", "a) grey", "Grey termina en otro sonido; rat termina en -at."),
    ],
    [
        (ADULT + STORY8 + " Ana dice que el técnico arregló el horno a tiempo. ¿Qué frase del texto lo contradice? a) the technician came late b) he makes bread for the whole street", "a) the technician came late", "Dice que el técnico llegó tarde."),
        (ADULT + RIDDLE + " ¿Qué pista de la adivinanza descarta que sea un televisor? a) I am not a television b) You type on me", "a) I am not a television", "El texto lo niega de forma directa."),
    ],
    [
        (ADULT + "«I have hands, but I cannot clap. I have a face, but I cannot smile. What am I?» (hands = manos, clap = aplaudir, face = cara, smile = sonreír). ¿Qué es? a) un reloj b) una persona", "a) un reloj", "Un reloj tiene manecillas (hands) y esfera (face)."),
        (ADULT + "«Last Monday, Tomás lost his umbrella on the bus. He told the driver. On Tuesday, the driver found it under a seat and called the school. Tomás thanked him with a card.» (lost = perdió, umbrella = paraguas, driver = conductor, found = encontró, seat = asiento, card = tarjeta). ¿Cómo terminó la historia? a) Tomás recuperó su paraguas y agradeció b) Tomás compró otro paraguas", "a) Tomás recuperó su paraguas y agradeció", "El conductor lo encontró y Tomás lo agradeció con una tarjeta."),
    ],
    [(ADULT + "Escuchas una canción original en una radio escolar: «Rain on the roof, rain on the street, / splash in my shoes and splash on my feet. / I jump in the puddles and laugh at the sky, / and I wave to the clouds as they travel by.» (rain = lluvia, roof = techo, splash = chapotear, puddles = charcos, laugh = reírse, wave = saludar, clouds = nubes). ¿Cuál es el tema de la canción? a) divertirse bajo la lluvia b) quejarse del frío", "a) divertirse bajo la lluvia", "La persona salta en los charcos y se ríe.")],
    [
        ("En Inglés de 8.º (OA 1, clase 5): ¿qué tienen en común las palabras que riman?", "Que terminan con el mismo sonido", "Por ejemplo cat, hat y mat."),
        ("¿Qué haces primero al escuchar de forma independiente?", "Escuchar la idea general", "Luego buscas un dato exacto."),
        ("¿Cómo compruebas tu respuesta?", "Con una frase del texto", "La evidencia respalda la respuesta."),
    ],
    task("Un adulto lee dos veces este relato original: «Two months ago, Marta planted five tomato seeds in a box. Every day she gave them water. After two weeks, three plants appeared. Marta was happy, so she took a photo and sent it to her cousin.» (ago = hace, planted = plantó, seeds = semillas, box = cajón, gave = dio, appeared = aparecieron, photo = foto, sent = envió, cousin = prima). Escribe en tu hoja la idea general y dos datos exactos.", "Idea general: Marta plantó semillas y logró que crecieran plantas. Datos: cinco semillas; tres plantas después de dos semanas.", ["escribe la idea general en una frase", "anota dos datos exactos del texto", "no inventa datos"], ["hoja con tres respuestas", "nota del adulto"], ["decir que aparecieron cinco plantas", "no mencionar el tiempo transcurrido"], "Reconoce lo que acertó y compara cuántas semillas y cuántas plantas aparecieron."),
    "Pide a un adulto que lea la rima del gato y escribe tres palabras que terminen igual.",
    "Escribe una rima de dos versos en inglés con las palabras sun y fun y comprueba que terminen con el mismo sonido.",
)
