"""Cuaderno del estudiante, 6.º básico Inglés (propuesta), EN06 OA 02 (comprender textos orales de temas variados).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan pista en español. Cada palabra o estructura nueva se explica antes de usarla.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA2 = "EN06 OA 02"
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


# ---------------------------------------------------------------- clase 1: experiencias personales (personas y acciones)
FARM = "«Last summer, I visited my friend Joaquín's farm in Chillán. Joaquín and I planted tomatoes. His mother cooked soup, and I helped her wash the vegetables. In the evening, we watched the stars.» (visited = visité, farm = campo, planted = plantamos, cooked = cocinó, wash = lavar, vegetables = verduras, watched = miramos)"
WEEK = "«My name is Ignacio. On Monday I play football at school. On Wednesday I draw with my friend Pía. On Saturday I help in my neighbour's shop.» (draw = dibujar, neighbour's shop = tienda del vecino)"
BADDAY = "«Yesterday was a bad day for Sofía. In the morning, she missed the bus. At school, she forgot her homework. But in the afternoon, her teacher gave her one more day, and she felt better.» (missed = perdió, forgot = olvidó, gave = dio, felt better = se sintió mejor)"

lesson(
    OA2, 1,
    "Los relatos de experiencias personales escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a distinguir la idea general de la información específica en una experiencia personal contada oralmente: quién, qué hizo, dónde y cuándo. Sirve para entender lo que otras personas cuentan de su vida.",
    ["Sé que yesterday y last summer hablan del pasado.", "Conozco verbos como play, help y draw."],
    [
        "Cuando alguien cuenta una experiencia personal, primero se entiende la idea general (general idea): de qué trata todo el relato. Después se buscan los datos específicos (specific information): personas, acciones, lugares y momentos. Por ejemplo, en un relato sobre un viaje al campo, la idea general es «un verano en el campo» y un dato específico es «plantaron tomates».",
        "Para hablar del pasado, muchos verbos terminan en -ed: visited (visitó), planted (plantó), cooked (cocinó), helped (ayudó), watched (miró). Otros cambian de forma: went (fue), ate (comió), gave (dio), forgot (olvidó). Las palabras de tiempo ayudan: yesterday (ayer), last summer (el verano pasado), in the evening (en la tarde-noche), on Monday (el lunes).",
        "Para escuchar bien, hazte estas preguntas: ¿quién actúa?, ¿qué hace?, ¿dónde? y ¿cuándo? Anota la palabra clave de cada una. Si no entiendes una palabra, mira qué personas y acciones la rodean. No es necesario conocer todas las palabras para captar la idea general.",
    ],
    [("general idea", "idea general"), ("specific information", "información específica"), ("last summer", "el verano pasado"), ("yesterday", "ayer"), ("visited / helped", "visitó / ayudó"), ("went / ate / gave", "fue / comió / dio")],
    [
        ("Idea general y dato específico", ADULT + "«On Sunday, Elena and her father rode bikes along the river. They stopped to eat sandwiches. A duck swam near them. They went home at six.» (rode = anduvieron en, river = río, duck = pato, swam = nadó). ¿Cuál es la idea general y a qué hora volvieron a casa?", ["Todo el relato cuenta un paseo en bicicleta el domingo.", "Busco la hora: They went home at six.", "Separo idea general y dato."], "Idea general: un paseo en bicicleta. Volvieron a las seis"),
        ("Personas y acciones", "En el mismo relato, ¿quiénes son las personas y qué hacen al detenerse?", ["Las personas son Elena y su papá.", "Al detenerse comen sándwiches.", "El pato es un animal, no una persona."], "Elena y su papá comen sándwiches"),
    ],
    [
        ("Responder con la idea general cuando se pide un dato específico.", "No se distingue de qué trata todo el relato de un dato puntual.", "Para un dato, busca la palabra clave: un número, un nombre o un lugar."),
        ("Pensar que un verbo en -ed habla del futuro.", "No se reconoce la terminación del pasado.", "Los verbos en -ed (visited, helped) cuentan hechos que ya ocurrieron."),
    ],
    [
        (ADULT + FARM + " ¿Qué visitó el narrador el verano pasado? a) el campo de un amigo b) un museo c) la casa de su abuela", "a) el campo de un amigo", "Dice I visited my friend Joaquín's farm."),
        (ADULT + FARM + " ¿Qué plantaron Joaquín y el narrador?", "Tomates", "Dice we planted tomatoes."),
        (ADULT + FARM + " ¿Qué hicieron en la tarde-noche? a) miraron las estrellas b) cocinaron sopa", "a) miraron las estrellas", "Dice in the evening, we watched the stars."),
    ],
    [
        (ADULT + FARM + " ¿Cuál es la idea general? a) un verano en el campo con un amigo b) una clase de cocina c) un viaje a la playa", "a) un verano en el campo con un amigo", "Todas las acciones ocurren en la granja del amigo."),
        (ADULT + WEEK + " ¿Qué hace Ignacio los lunes? a) juega fútbol b) dibuja c) ayuda en una tienda", "a) juega fútbol", "Dice On Monday I play football."),
        (ADULT + WEEK + " ¿Con quién dibuja Ignacio?", "Con su amiga Pía", "Dice I draw with my friend Pía."),
    ],
    [
        (ADULT + WEEK + " ¿En cuántos días diferentes de la semana hace actividades Ignacio?", "3", "Hace actividades el lunes, el miércoles y el sábado."),
        (ADULT + WEEK + " ¿Qué día ayuda en una tienda?", "El sábado", "Dice On Saturday I help in my neighbour's shop."),
        (ADULT + BADDAY + " ¿Cuántas cosas malas le pasaron a Sofía antes de la tarde?", "2", "Perdió el bus y olvidó la tarea."),
    ],
    [
        (ADULT + BADDAY + " ¿Qué hizo que Sofía se sintiera mejor? a) su profesora le dio un día más b) su amiga le prestó un lápiz", "a) su profesora le dio un día más", "Dice her teacher gave her one more day."),
        (ADULT + BADDAY + " ¿Cuál es la idea general? a) un mal día que mejoró b) un día de paseo c) un día de campeonato", "a) un mal día que mejoró", "Empieza con problemas y termina con she felt better."),
    ],
    [
        ("Ordena lo que le pasó a Sofía. A) Su profesora le dio un día más. B) Perdió el bus. C) Olvidó su tarea.", "B, C, A", "Primero fue la mañana, luego el colegio y por último la tarde."),
        ("Una compañera dice que Sofía perdió el bus en la tarde. ¿Cuándo lo perdió realmente?", "En la mañana", "Dice in the morning, she missed the bus."),
    ],
    [(ADULT + "Un amigo te deja este mensaje de voz: «Hi! Yesterday I went to the beach with my cousins. We built a sandcastle and ate ice cream. It was fun!» (beach = playa, built = construimos, sandcastle = castillo de arena, ice cream = helado). ¿Qué comieron?", "Helado", "Dice we ate ice cream.")],
    [
        ("¿Qué significa «last summer»?", "El verano pasado", "Indica un tiempo del pasado."),
        ("¿Qué datos específicos buscas en un relato: quién, qué, dónde y cuándo?", "Personas, acciones, lugares y momentos", "Son los datos que responden esas preguntas."),
        ("¿Qué significa «helped»?", "Ayudó", "Es el pasado de help."),
    ],
    task("Un adulto lee dos veces este relato: «Last Friday, my cousin Valeria went to the zoo with her class. She saw two elephants and a lion. At noon, she ate a sandwich near the lake. She took many photos.» (zoo = zoológico, saw = vio, lion = león, noon = mediodía, took = sacó, photos = fotos). Escribe en español: la idea general y cuatro datos específicos (quién, a dónde, qué vio y qué comió).", "Idea general: un paseo al zoológico. Valeria fue al zoológico con su curso, vio dos elefantes y un león y comió un sándwich.", ["escribe la idea general", "anota los cuatro datos específicos", "los datos coinciden con el relato"], ["hoja con respuestas", "nota del adulto"], ["confundir la idea general con un dato", "no anotar cuántos elefantes vio"], "Reconoce lo que acertó y revisa con la persona la diferencia entre idea general y dato específico."),
    "Pide a un adulto que lea el relato de Joaquín y subraya con un lápiz los verbos que terminan en -ed.",
    "Cuenta en tres frases en español un paseo que hiciste, indicando quién, dónde y cuándo.",
)

# ---------------------------------------------------------------- clase 2: temas de otras asignaturas
CYCLE = "«The sun heats the water in the sea. The water goes up as a gas called vapor. High in the sky, the vapor cools and makes clouds. Then rain falls on the land, and the rivers take the water back to the sea.» (heats = calienta, gas, cools = se enfría, clouds = nubes, land = tierra, rivers = ríos)"
GEO = "«Chile is a long and narrow country in South America. The Andes mountains are in the east, and the Pacific Ocean is in the west. In the north there is a big desert. In the south there are glaciers and forests.» (narrow = angosto, east = este, west = oeste, desert = desierto, glaciers = glaciares)"

lesson(
    OA2, 2,
    "Los textos de Ciencias, Geografía y Matemática escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a comprender textos orales de otras asignaturas, como Ciencias, Geografía y Matemática, reconociendo la idea general, el vocabulario del tema y los datos. Sirve para aprender contenidos escolares en inglés.",
    ["Sé que una exposición tiene un tema y datos.", "Conozco palabras como sun, rain, river y country."],
    [
        "En inglés se aprenden también contenidos de otras asignaturas. En Ciencias (Science) se explican procesos, como el ciclo del agua. En Geografía (Geography) se describen lugares y direcciones: north (norte), south (sur), east (este) y west (oeste). En Matemática (Math) se resuelven problemas con números y palabras como each (cada uno), how many (cuántos) y baskets (canastos).",
        "Cada asignatura tiene su vocabulario temático. Aprenderlo en grupos ayuda: sun, vapor, clouds y rain pertenecen a Ciencias; mountains, ocean y desert pertenecen a Geografía. Escucha primero la idea general, por ejemplo «cómo se mueve el agua». Después fíjate en los datos específicos, como qué hace el sol, en qué orden ocurre un proceso o cuántos objetos hay.",
        "En un proceso, el orden importa: then (luego), after that (después) y finally (finalmente) marcan los pasos. En un problema de Matemática, anota los números que oyes y la pregunta que se hace. Si una palabra nueva es parecida al español, como vapor, desert o ocean, es probable que signifique algo parecido.",
    ],
    [("Science / Geography / Math", "Ciencias / Geografía / Matemática"), ("north / south / east / west", "norte / sur / este / oeste"), ("each", "cada uno"), ("how many", "cuántos"), ("then", "luego"), ("vapor / desert / ocean", "vapor / desierto / océano")],
    [
        ("Idea general en Ciencias", ADULT + "«Plants need light, air and water to grow. The leaves take light from the sun. The roots take water from the soil. Without light, a plant becomes weak.» (leaves = hojas, roots = raíces, soil = tierra, weak = débil). ¿De qué trata el texto y cuántas cosas necesitan las plantas?", ["Escucho plants y need: habla de lo que necesitan las plantas.", "Cuento: light, air y water.", "Son tres cosas."], "Trata de lo que necesitan las plantas; necesitan 3 cosas"),
        ("Un dato de Matemática", ADULT + "«Tom has fifteen marbles. He gives five marbles to Lía. How many marbles does Tom have now?» (marbles = bolitas, gives = da, now = ahora).", ["Anoto los números: 15 y 5.", "Gives indica que Tom se queda con menos.", "Calculo 15 − 5 = 10."], "10 bolitas"),
    ],
    [
        ("Confundir east con west al escuchar una dirección.", "No se escucha con atención y se invierte el lado.", "Recuerda: el sol sale por el este (east) y se pone por el oeste (west)."),
        ("Ignorar la pregunta final de un problema de Matemática.", "Se anotan los números, pero no lo que se pide.", "Escucha siempre la pregunta (How many...) y responde esa."),
    ],
    [
        (ADULT + CYCLE + " ¿Qué hace el sol con el agua del mar? a) la calienta b) la congela c) la bebe", "a) la calienta", "Dice the sun heats the water."),
        (ADULT + CYCLE + " ¿Cómo se llama el gas en que se convierte el agua?", "Vapor", "Dice a gas called vapor."),
        (ADULT + CYCLE + " ¿Dónde se forman las nubes? a) en lo alto del cielo b) bajo el mar", "a) en lo alto del cielo", "Dice high in the sky, the vapor makes clouds."),
    ],
    [
        (ADULT + CYCLE + " ¿Cuál es la idea general? a) cómo el agua sube, forma nubes y vuelve como lluvia b) cómo se hace una sopa c) cómo viajan los barcos", "a) cómo el agua sube, forma nubes y vuelve como lluvia", "Todo el texto sigue el recorrido del agua."),
        (ADULT + GEO + " ¿Qué hay al oeste de Chile? a) el océano Pacífico b) la cordillera de los Andes", "a) el océano Pacífico", "Dice the Pacific Ocean is in the west."),
        (ADULT + GEO + " ¿Qué hay en el norte? a) un gran desierto b) glaciares", "a) un gran desierto", "Dice in the north there is a big desert."),
    ],
    [
        (ADULT + "«We have twenty-four apples. We put six apples in each basket. How many baskets do we need?» (apples = manzanas, basket = canasto).", "4", "Se reparten 24 manzanas en grupos de 6.", "24//6"),
        (ADULT + GEO + " ¿Qué dos lugares cita el texto en el sur? a) glaciares y bosques b) desierto y montañas", "a) glaciares y bosques", "Dice in the south there are glaciers and forests."),
        (ADULT + CYCLE + " ¿Qué ocurre después de que se forman las nubes? a) cae lluvia b) el sol calienta el mar", "a) cae lluvia", "Dice then rain falls on the land."),
    ],
    [
        ("Ordena el ciclo del agua. A) Se forman nubes. B) El sol calienta el mar. C) Cae lluvia.", "B, A, C", "Calentamiento, nubes y lluvia es el orden del texto."),
        ("Lee: «There are three rivers and each river has four bridges.» (bridges = puentes). ¿Cuántos puentes hay?", "12", "Hay tres ríos con cuatro puentes cada uno.", "3*4"),
    ],
    [
        ("En Geografía, si tienes el este a tu derecha y miras al norte, ¿qué hay a tu izquierda? Elige: a) el oeste b) el sur", "a) el oeste", "Al mirar al norte, el este queda a la derecha y el oeste a la izquierda."),
        (ADULT + "«Today in Science we study the moon. The moon goes around the Earth in about twenty-eight days. It does not make its own light.» (goes around = gira alrededor, days = días, own = propia). ¿En cuántos días aproximadamente gira alrededor de la Tierra?", "28", "Dice twenty-eight days."),
    ],
    [(ADULT + "En clase de Geografía, un profesor dice: «The Andes are in the east of Chile. If you go west, you arrive at the sea.» (arrive = llegas). Si viajas hacia el oeste, ¿adónde llegas?", "Al mar", "Dice that going west you arrive at the sea.")],
    [
        ("¿Qué significa «each» en un problema de Matemática?", "Cada uno", "Each indica el mismo número para cada grupo."),
        ("¿Cómo se dice «norte» en inglés?", "north", "North es norte."),
        ("¿En qué asignatura aprendes el ciclo del agua?", "Ciencias", "Science estudia procesos de la naturaleza."),
    ],
    task("Un adulto lee dos veces este texto: «In Science, we study the Earth. The Earth has land and water. About seventy percent of its surface is water. The rest is land, with mountains, deserts and forests.» (surface = superficie, rest = resto, percent = por ciento). Escribe en español la idea general y tres datos específicos, y una palabra de Ciencias y otra de Geografía.", "Idea general: cómo es la superficie de la Tierra. Datos: tiene tierra y agua; cerca del 70 % es agua; el resto tiene montañas, desiertos y bosques.", ["escribe la idea general", "anota tres datos específicos", "nombra una palabra de cada asignatura"], ["hoja con respuestas", "nota del adulto"], ["decir que la mayor parte es tierra", "no anotar el porcentaje"], "Reconoce el esfuerzo y repasa con la persona el vocabulario de cada asignatura."),
    "Pide a un adulto que lea el texto del ciclo del agua y señala en un dibujo el sol, las nubes y la lluvia.",
    "Dibuja el ciclo del agua con tres flechas y escribe una palabra en inglés en cada flecha.",
)

# ---------------------------------------------------------------- clase 3: objetos, lugares y tiempo
MUSEUM = "«Welcome to the Science Museum. We open at ten o'clock from Tuesday to Sunday. We are closed on Monday. A ticket costs two thousand pesos for children. The dinosaur room is on the second floor, next to the café.» (welcome = bienvenidos, closed = cerrado, ticket = entrada, floor = piso, next to = al lado de)"
TRIP = "«The school trip is on Friday. The bus leaves at half past eight in the morning. It returns at half past four in the afternoon. Please bring a lunch box and a bottle of water.» (trip = paseo, leaves = sale, returns = vuelve, half past = y media, lunch box = colación, bottle = botella)"
ROOM = "«My room is small. There is a bed under the window. The desk is next to the bed. On the desk there are three books, a lamp and a green cup. The wardrobe is in front of the door.» (bed = cama, desk = escritorio, lamp = lámpara, wardrobe = clóset, in front of = frente a)"

lesson(
    OA2, 3,
    "Los avisos y descripciones escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a identificar objetos, lugares y tiempo en un texto oral: qué hay, dónde está, a qué hora y qué día. Sirve para entender avisos, horarios y descripciones en inglés.",
    ["Sé decir los números hasta cien y los días de la semana.", "Conozco palabras como room, bed y desk."],
    [
        "Muchos textos orales dan información de objetos, lugares y tiempo. Para los objetos oirás nombres como book, lamp o ticket. Para los lugares oirás preposiciones: under (debajo), next to (al lado de), in front of (frente a), on the second floor (en el segundo piso). Para el tiempo oirás días y horas.",
        "Las horas se dicen así: ten o'clock (las diez en punto), half past eight (ocho y media), a quarter past four (cuatro y cuarto). Con in the morning (en la mañana) y in the afternoon (en la tarde) sabes si es antes o después del mediodía. Los números grandes se separan en partes: two thousand (dos mil), eight hundred (ochocientos).",
        "Mientras escuchas, ten lista una tabla mental con tres columnas: objetos, lugares y tiempo. Anota solo una palabra clave en cada una. Después, responde las preguntas buscando esa palabra. Si oyes un precio o una hora, escribe el número de inmediato, porque son datos fáciles de olvidar.",
    ],
    [("next to / under / in front of", "al lado de / debajo de / frente a"), ("o'clock", "en punto"), ("half past eight", "ocho y media"), ("closed", "cerrado"), ("ticket", "entrada"), ("floor", "piso")],
    [
        ("Hora y día", ADULT + "«The library opens at nine o'clock on Monday and Wednesday. On Friday it opens at ten o'clock.» (opens = abre). ¿A qué hora abre la biblioteca el viernes?", ["Busco la palabra Friday.", "Después dice at ten o'clock.", "Diez en punto es las 10:00."], "A las 10:00"),
        ("Lugar de un objeto", "Lee: «The cat is under the table, next to the red ball.» (cat = gato, ball = pelota). ¿Dónde está el gato y qué hay a su lado?", ["Under the table significa debajo de la mesa.", "Next to indica lo que está al lado.", "El objeto es la pelota roja."], "Debajo de la mesa, junto a la pelota roja"),
    ],
    [
        ("Entender half past eight como las nueve y media.", "Se confunde la hora con la siguiente.", "Half past eight es ocho y media: 8:30."),
        ("Responder con el lugar cuando se pregunta por la hora.", "No se escucha la palabra interrogativa.", "Si la pregunta es When o What time, busca días y horas."),
    ],
    [
        (ADULT + MUSEUM + " ¿A qué hora abre el museo? a) a las diez b) a las ocho c) a las doce", "a) a las diez", "Dice we open at ten o'clock."),
        (ADULT + MUSEUM + " ¿Qué día está cerrado el museo?", "El lunes", "Dice we are closed on Monday."),
        (ADULT + MUSEUM + " ¿Dónde está la sala de dinosaurios? a) en el segundo piso, al lado del café b) en el primer piso, frente a la puerta", "a) en el segundo piso, al lado del café", "Dice on the second floor, next to the café."),
    ],
    [
        (ADULT + MUSEUM + " Si van tres niños y cada entrada cuesta 2.000 pesos, ¿cuántos pesos pagan en total?", "6.000", "Cada niño paga 2.000 pesos y son tres.", "2000*3"),
        (ADULT + TRIP + " ¿A qué hora sale el bus? a) a las 8:30 b) a las 9:30", "a) a las 8:30", "Half past eight es las 8:30."),
        (ADULT + TRIP + " ¿Qué dos cosas hay que llevar?", "Una colación y una botella de agua", "Dice a lunch box and a bottle of water."),
    ],
    [
        (ADULT + TRIP + " ¿Cuántas horas dura el paseo desde las 8:30 hasta las 16:30?", "8", "Hay ocho horas entre la salida y el regreso.", "16-8"),
        (ADULT + ROOM + " ¿Qué hay debajo de la ventana?", "Una cama", "Dice there is a bed under the window."),
        (ADULT + ROOM + " ¿Cuántos libros hay sobre el escritorio?", "3", "Dice three books."),
    ],
    [
        (ADULT + ROOM + " Un compañero dice que el clóset está al lado de la cama. ¿Qué dice el texto del clóset?", "Que está frente a la puerta", "Dice the wardrobe is in front of the door."),
        (ADULT + ROOM + " ¿Qué color tiene la taza? a) verde b) azul", "a) verde", "Dice a green cup."),
    ],
    [
        ("Un aviso dice: «The pool is open from Wednesday to Sunday. It is closed on Monday and Tuesday.» (pool = piscina). ¿Cuántos días está abierta la piscina?", "5", "Wednesday, Thursday, Friday, Saturday y Sunday son cinco días."),
        ("Una agenda dice: «Music class at a quarter past four.» (quarter past = y cuarto). ¿A qué hora empieza?", "A las 4:15", "A quarter past four es 4:15."),
    ],
    [(ADULT + "En la estación, el altavoz dice: «The train to Concepción leaves at six o'clock from platform two.» (platform = andén, leaves = sale). ¿Desde qué andén sale?", "Desde el andén 2", "Dice platform two.")],
    [
        ("¿Qué significa «next to»?", "Al lado de", "Indica posición cercana."),
        ("¿A qué hora es «half past three»?", "3:30", "Half past es y media."),
        ("¿Qué significa «closed»?", "Cerrado", "Es lo contrario de open."),
    ],
    task("Un adulto lee dos veces este aviso: «The sports centre is open from Monday to Saturday. It opens at seven o'clock in the morning and closes at nine o'clock at night. The swimming pool is on the first floor, next to the gym. The entrance costs one thousand five hundred pesos.» (sports centre = centro deportivo, swimming pool = piscina, gym = gimnasio, entrance = entrada). Escribe: días, hora de apertura y cierre, ubicación de la piscina y precio.", "Lunes a sábado; abre a las 7:00 y cierra a las 21:00; piscina en el primer piso al lado del gimnasio; cuesta 1.500 pesos.", ["escribe los cuatro datos", "los números son correctos", "no incluye datos que no aparecen"], ["hoja con respuestas", "nota del adulto"], ["confundir la hora de apertura y la de cierre", "poner el domingo como día abierto"], "Reconoce los datos que acertó y repite con la persona la lectura de las horas."),
    "Pide a un adulto que lea el aviso del museo y levanta la mano cada vez que oigas un número.",
    "Describe en cuatro frases en español tu pieza usando debajo de, al lado de y frente a.",
)

# ---------------------------------------------------------------- clase 4: hablantes, pasos y secuencia
RADIO = "«Host: Welcome to School Radio! Today we talk with Camila about her pet. Camila: Hi! I have a rabbit named Nube. Host: What does Nube eat? Camila: Carrots and grass. Host: Thank you, Camila. Camila: Thank you!» (host = presentador, pet = mascota, rabbit = conejo, carrots = zanahorias, grass = pasto)"
CARD = "«How to make a card. First, fold a sheet of paper in half. Then draw a picture on the front. After that, write a message inside. Finally, give the card to your friend.» (card = tarjeta, fold = doblar, message = mensaje, inside = adentro, front = frente)"
TOMAS = "«Before class, Tomás ate breakfast. During recess, he played football. After school, he did his homework. Before bed, he read a book.» (before = antes de, during = durante, after = después de, recess = recreo, bed = cama)"

lesson(
    OA2, 4,
    "Los textos con dos hablantes, instrucciones y secuencias escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a identificar quién habla en un texto oral, cuáles son los pasos de unas instrucciones y en qué orden ocurren los hechos. Sirve para seguir indicaciones y entender relatos ordenados.",
    ["Sé que first, then y finally ordenan los pasos.", "Conozco verbos como draw, write y play."],
    [
        "En un texto oral con varias personas hay hablantes (speakers). Para identificarlos, escucha los nombres, los saludos y los cambios de turno. En una entrevista de radio, el presentador (host) hace las preguntas y la persona invitada responde. Los hablantes pueden ser dos o más.",
        "En unas instrucciones, cada paso empieza con un verbo en orden: fold (dobla), draw (dibuja), write (escribe), give (entrega). Las palabras first, then, after that y finally marcan la secuencia. En una secuencia de eventos, before (antes de), during (durante) y after (después de) dicen cuándo ocurre cada hecho en relación con otro.",
        "Una estrategia útil es numerar mentalmente los pasos: uno, dos, tres. Si faltara uno, el resultado no sale bien. Para una secuencia de eventos, imagina una línea del tiempo con antes, durante y después. Así puedes responder qué ocurrió primero, qué ocurrió en medio y qué ocurrió al final sin confundirte.",
    ],
    [("speaker", "hablante"), ("host", "presentador"), ("before / during / after", "antes de / durante / después de"), ("first, then, after that, finally", "primero, luego, después de eso, finalmente"), ("step", "paso"), ("sequence", "secuencia")],
    [
        ("Identificar hablantes", ADULT + "«Teacher: Open your notebook. Pablo: Which page, please? Teacher: Page twelve. Then copy the title.» (open = abre, page = página, copy = copia, title = título). ¿Cuántos hablantes hay y quién da las instrucciones?", ["Los nombres que anteceden las frases son Teacher y Pablo.", "Son dos hablantes.", "Teacher dice Open, Page twelve y copy: da las órdenes."], "Dos hablantes; da las instrucciones el profesor"),
        ("Pasos en orden", "En el mismo texto, ¿qué debe hacer Pablo después de abrir el cuaderno en la página doce?", ["La profesora dice Then copy the title.", "Then indica el paso siguiente.", "El paso es copiar el título."], "Copiar el título"),
    ],
    [
        ("Contar los pasos de unas instrucciones y olvidar el último.", "Se deja de escuchar antes de que termine el texto.", "Escucha hasta finally o hasta la última orden."),
        ("Confundir before con after.", "Se traducen mal las dos palabras.", "Before es antes de y after es después de."),
    ],
    [
        (ADULT + RADIO + " ¿Cuántos hablantes hay en la entrevista?", "2", "Hablan el presentador y Camila."),
        (ADULT + RADIO + " ¿Qué mascota tiene Camila? a) un conejo b) un perro c) un pez", "a) un conejo", "Dice I have a rabbit named Nube."),
        (ADULT + RADIO + " ¿Qué come Nube? a) zanahorias y pasto b) pan y queso", "a) zanahorias y pasto", "Dice carrots and grass."),
    ],
    [
        (ADULT + CARD + " ¿Qué es lo primero que hay que hacer?", "Doblar una hoja por la mitad", "El primer paso dice first, fold a sheet of paper in half."),
        (ADULT + CARD + " ¿Qué se hace después de dibujar en el frente? a) escribir un mensaje adentro b) entregar la tarjeta", "a) escribir un mensaje adentro", "Dice after that, write a message inside."),
        (ADULT + CARD + " ¿Cuántos pasos tiene, marcados con first, then, after that y finally?", "4", "Son cuatro palabras de secuencia."),
    ],
    [
        (ADULT + TOMAS + " ¿Qué hizo Tomás durante el recreo?", "Jugó fútbol", "Dice during recess, he played football."),
        (ADULT + TOMAS + " ¿Qué hizo después del colegio?", "Hizo su tarea", "Dice after school, he did his homework."),
        (ADULT + TOMAS + " ¿Qué hizo antes de dormir?", "Leyó un libro", "Dice before bed, he read a book."),
    ],
    [
        ("Ordena las actividades de Tomás desde la primera. A) jugó fútbol B) desayunó C) leyó un libro D) hizo la tarea", "B, A, D, C", "Siguen el orden de before class, during recess, after school y before bed."),
        ("Una compañera dice que en la entrevista de radio el presentador responde las preguntas. ¿Qué error comete?", "Es el presentador quien pregunta y Camila quien responde", "El presentador hace las preguntas, por ejemplo What does Nube eat?"),
    ],
    [
        (ADULT + "«Step one: put water in a glass. Step two: add a spoon of salt. Step three: stir. Step four: wait one minute.» (salt = sal, stir = revolver, wait = espera). ¿Cuántos minutos hay que esperar?", "1", "Dice wait one minute."),
        (ADULT + CARD + " ¿Qué paso va justo antes de entregar la tarjeta? a) escribir un mensaje adentro b) dibujar en el frente", "a) escribir un mensaje adentro", "Dice after that, write a message inside, y luego finally, give the card."),
    ],
    [(ADULT + "En clase de Educación Física, la profesora dice: «First, stretch your arms. Then jump ten times. After that, drink some water.» (stretch = estira, arms = brazos, jump = salta, times = veces, drink = toma). ¿Cuántas veces hay que saltar?", "10", "Dice jump ten times.")],
    [
        ("¿Qué significa «after»?", "Después de", "After indica un momento posterior."),
        ("¿Cómo sabes cuántos hablantes hay en un diálogo?", "Contando los nombres distintos", "Cada nombre es una persona."),
        ("¿Qué palabra marca el último paso?", "finally", "Finally significa finalmente."),
    ],
    task("Un adulto lee dos veces este texto: «Radio host: Hello, Daniel! What do you do in the morning? Daniel: First, I wake up at seven. Then I wash my face. After that, I eat bread with butter. Finally, I walk to school. Radio host: Thanks, Daniel!» (wash my face = lavar mi cara, bread = pan, butter = mantequilla, walk = camino). Escribe: cuántos hablantes hay y las cuatro acciones de Daniel en orden.", "Hay 2 hablantes. Se levanta a las siete, se lava la cara, come pan con mantequilla y camina al colegio.", ["dice que hay dos hablantes", "anota las cuatro acciones en orden", "incluye la hora"], ["hoja con respuestas", "nota del adulto"], ["cambiar el orden de las acciones", "no decir quién pregunta"], "Reconoce lo que acertó y repasa con la persona las palabras de secuencia."),
    "Pide a un adulto que lea las instrucciones de la tarjeta y haz cada paso con una hoja de papel.",
    "Escribe en español cuatro pasos de algo que haces cada día, usando first, then, after that y finally en inglés.",
)

# ---------------------------------------------------------------- clase 5: vocabulario, expresiones frecuentes, sonido /r/ y otras culturas
HANAMI = "«In Japan, many families have a picnic in spring under the cherry trees. They sit on blankets and eat rice balls. They enjoy the pink flowers with their friends.» (Japan = Japón, picnic = picnic, cherry trees = cerezos, blankets = mantas, rice balls = bolas de arroz, pink = rosado)"

lesson(
    OA2, 5,
    "Las expresiones, pares de palabras y textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a reconocer palabras de vocabulario, expresiones de uso frecuente y el sonido /r/ del inglés al escuchar textos de otras culturas. Sirve para entender conversaciones cotidianas con más seguridad.",
    ["Sé decir saludos como hello y goodbye.", "Conozco palabras como rain, red y run."],
    [
        "Las expresiones de uso frecuente son frases que se usan todos los días. Excuse me (disculpa) llama la atención. Sorry (perdón) pide disculpas. No problem (no hay problema) responde a un agradecimiento. Of course (por supuesto) acepta. See you later (hasta luego) se dice al despedirse. I don't understand (no entiendo) y Can you repeat, please? (¿puedes repetir, por favor?) ayudan cuando no escuchaste bien.",
        "El sonido inicial /r/ del inglés se oye en ready, run, rain y red. Es distinto del sonido de la r del español. En inglés los labios se redondean un poco y la lengua no toca el paladar ni vibra. Esto importa porque right (derecha o correcto) y light (luz) se parecen y cambian el significado: la /r/ es un sonido que puede interferir con la comprensión.",
        "Escuchar textos de otras culturas también amplía el vocabulario. A veces aparecen palabras menos frecuentes, como picnic, blankets o cherry trees. Para entenderlas, usa el contexto: si los niños se sientan sobre mantas y comen en un parque, picnic es una comida al aire libre. No necesitas conocer cada palabra para entender la idea general del texto.",
    ],
    [("Excuse me / Sorry", "disculpa / perdón"), ("No problem", "no hay problema"), ("Of course", "por supuesto"), ("See you later", "hasta luego"), ("Can you repeat, please?", "¿puedes repetir, por favor?"), ("right / light", "derecha o correcto / luz")],
    [
        ("Elegir la expresión adecuada", "Pisas sin querer el pie de tu amiga. ¿Qué dices? a) Sorry b) See you later c) Of course", ["La situación es un pequeño accidente.", "Sorry pide disculpas.", "See you later se dice al despedirse."], "Sorry"),
        ("Reconocer el sonido /r/", "¿Cuál de estas dos palabras empieza con el sonido /r/: right o light?", ["Right empieza con r.", "Light empieza con l.", "El sonido inicial /r/ está en right."], "right"),
    ],
    [
        ("Pronunciar la /r/ inglesa como la r vibrante del español.", "Se usa el sonido del español, que cambia la palabra.", "Redondea los labios y deja la lengua sin tocar el paladar; no hay vibración."),
        ("Pensar que right y light son la misma palabra.", "Se atiende solo al significado de la oración y no al primer sonido.", "Escucha el primer sonido: /r/ en right y /l/ en light."),
    ],
    [
        ("¿Qué dices si no oíste una palabra? a) Can you repeat, please? b) Of course. c) See you later.", "a) Can you repeat, please?", "Sirve para pedir que repitan."),
        ("¿Qué significa «No problem»?", "No hay problema", "Responde amablemente a un agradecimiento."),
        ("¿Qué palabra empieza con /r/: rain o lane?", "rain", "Rain empieza con el sonido /r/."),
    ],
    [
        (ADULT + HANAMI + " ¿De qué país habla el texto? a) Japón b) Chile c) Perú", "a) Japón", "Dice In Japan."),
        (ADULT + HANAMI + " ¿Dónde se sientan las familias? a) bajo los cerezos b) dentro de un museo", "a) bajo los cerezos", "Dice under the cherry trees."),
        (ADULT + HANAMI + " ¿De qué color son las flores? a) rosado b) azul", "a) rosado", "Dice the pink flowers."),
    ],
    [
        ("Una persona te dice «Thank you». ¿Qué respondes? a) No problem b) Excuse me c) See you later", "a) No problem", "Es la respuesta amable a un agradecimiento."),
        ("¿Qué palabra se diferencia de rock solo porque empieza con /l/ en vez de /r/: lock o sock?", "lock", "Lock cambia solo el sonido inicial; sock empieza con /s/."),
        ("¿Cuál de estas palabras NO empieza con /r/: run, road, lamp, red?", "lamp", "Lamp empieza con /l/."),
    ],
    [
        ("Un compañero dice que road y load suenan iguales. ¿Por qué se equivoca?", "Porque empiezan con sonidos distintos: /r/ y /l/", "Road empieza con /r/ y load con /l/, y significan cosas diferentes."),
        (ADULT + "«Girl: Excuse me, can you help me? Boy: Of course. Girl: Where is the bus stop? Boy: It is on the right.» (bus stop = paradero, on the right = a la derecha). ¿Hacia dónde queda el paradero?", "A la derecha", "Dice on the right."),
    ],
    [
        (ADULT + HANAMI + " ¿Qué comen las familias?", "Bolas de arroz", "Dice they eat rice balls."),
        ("¿Cuántas de estas palabras empiezan con el sonido /r/: ready, lazy, rice, lake, run?", "3", "Ready, rice y run empiezan con /r/; lazy y lake empiezan con /l/."),
    ],
    [(ADULT + "En el aeropuerto, un guía dice: «Excuse me, everyone. Please stay in line and show your passport.» (stay in line = quédense en fila, passport = pasaporte). ¿Qué hay que mostrar?", "El pasaporte", "Dice show your passport.")],
    [
        ("¿Cómo se dice «hasta luego» en inglés?", "See you later", "Es una despedida común."),
        ("¿Qué dos sonidos distinguen right de light?", "/r/ y /l/", "Cada palabra empieza con un sonido distinto."),
        ("¿Qué significa «Of course»?", "Por supuesto", "Se usa para aceptar o confirmar."),
    ],
    task("Un adulto lee dos veces este texto: «In Chile, many families eat bread and drink tea in the afternoon. In England, many people also drink tea and eat biscuits in the afternoon. They sit at the table and talk about their day.» (bread = pan, tea = té, biscuits = galletas, talk = conversan). Escribe: las dos comidas que se mencionan, los dos países y una expresión de uso frecuente que usarías para pedir que repitan el texto.", "Pan con té y té con galletas; Chile e Inglaterra; Can you repeat, please?", ["menciona los dos países", "menciona las comidas", "usa una expresión adecuada"], ["hoja con respuestas", "nota del adulto"], ["confundir los dos países", "usar una expresión que no sirve para pedir repetición"], "Reconoce lo que acertó y practica con la persona las expresiones para pedir ayuda."),
    "Pide a un adulto que diga tres pares: right-light, road-load, rock-lock, y repite el primero de cada par con labios redondeados.",
    "Escribe tres frases cortas en español donde usarías Excuse me, Sorry y No problem.",
)
