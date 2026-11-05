"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 01: textos orales en distintos formatos.

Las «escuchas» las lee una persona adulta en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales, con pista en español. Los títulos de las clases del plan son genéricos; aquí cada clase recorre
un grupo de formatos que nombra el OA (avisos y anécdotas; noticieros y entrevistas; narraciones y canciones;
exposiciones, discursos y debates; conversaciones e instrucciones).
"""
from __future__ import annotations

from en_m2_a_common import ADULT, MAT, arith, lesson, task

OA = "EN2M OA 01"

# ======================================================= clase 1: avisos, anécdotas y descripciones
THEATRE = "«Join the Youth Theatre Club! We meet every Wednesday at four in the school hall. No experience is necessary. This term we are preparing a comedy for the neighborhood. Come to our open day on Friday and try a scene with us. It is free.» (join = unirse, meet = reunirse, hall = salón, term = semestre, comedy = comedia, neighborhood = barrio, scene = escena, free = gratis)"
GUIDE = "«Last summer I worked as a guide at a small museum in my town. On my first day, I got lost inside the building I was supposed to explain! A visitor smiled and asked me for the way to the exit. We both laughed. Since then, I always walk the whole museum before a tour.» (guide = guía, got lost = me perdí, visitor = visitante, exit = salida, tour = visita guiada, since then = desde entonces)"
STUDIO = "«The community radio studio is a tiny room on the second floor. There are two microphones on a round table and a red light above the door. When the light is on, nobody can enter.» (community radio = radio comunitaria, tiny = diminuto, microphone = micrófono, round = redondo, above = sobre, enter = entrar)"
SHOW = "«The school comedy show costs three thousand pesos for adults and one thousand pesos for students.» (adults = adultos, costs = cuesta)"

lesson(
    OA, 1, MAT,
    "Aprenderé a reconocer el propósito, la audiencia y el formato de un aviso publicitario, una anécdota y una descripción dichos en voz alta. Sirve para saber qué se espera de ti al escuchar: participar, aprender algo o imaginar un lugar.",
    ["Sé el presente simple y el pasado simple con verbos comunes.", "Sé usar who, where y when para preguntar."],
    [
        "Todo texto oral tiene un propósito (purpose): la razón por la que alguien habla. Un aviso publicitario (advertisement) busca que el público haga algo, como unirse o visitar; por eso usa órdenes amables (Join…, Come to…) y ofertas (free). Una anécdota (anecdote) cuenta un hecho vivido por quien habla; usa I, my y el pasado simple. Una descripción (description) muestra cómo es un lugar con adjetivos y la estructura There is… o There are…",
        "La audiencia (audience) es el grupo al que se dirige el texto. Se deduce de quién habla, de qué ofrece y del tono. Si el aviso dice No experience is necessary, se dirige también a quienes nunca han actuado. Si un texto dice When the light is on, nobody can enter, quiere que quienes lo oyen cambien su conducta.",
        "Para decidir el propósito, hazte dos preguntas mientras escuchas: ¿qué quiere lograr quien habla? y ¿qué pistas lo muestran? Si invita u ofrece algo, convence. Si cuenta lo que vivió, comparte una experiencia. Si muestra cómo es un lugar con adjetivos y There is…, describe. No necesitas entender cada palabra: las pistas bastan.",
    ],
    [("advertisement", "aviso publicitario: invita o convence al público"), ("anecdote", "anécdota: hecho real contado por quien lo vivió"), ("description", "descripción: dice cómo es un lugar o una persona"), ("audience", "audiencia: el grupo al que se habla"), ("purpose", "propósito: lo que el hablante quiere lograr")],
    [
        ("Propósito de un aviso", ADULT + "«Neighbours, the library book swap is this Sunday at noon in the main square. Bring two books and take two home. Everyone is welcome.» (neighbours = vecinos, swap = intercambio, square = plaza, welcome = bienvenido). ¿Para qué se dice este texto?", ["Busco qué quiere lograr quien habla: dice Bring two books y Everyone is welcome.", "Son invitaciones dirigidas al público.", "Entonces busca que la gente participe en el intercambio."], "Invitar a los vecinos a participar en un intercambio de libros"),
        ("Pistas de una anécdota", ADULT + "«On my birthday last year, my cousin arrived with a cake, but she dropped it at the door. We ate it with spoons from the box and laughed all night.» (dropped = dejó caer, spoons = cucharas). ¿Es una anécdota o un aviso? Da una pista.", ["Quien habla usa my y cuenta algo propio.", "Los verbos están en pasado: arrived, dropped, ate.", "Marca un tiempo pasado con last year."], "Es una anécdota: usa my y el pasado con last year"),
    ],
    [
        ("Decidir el propósito solo por el tema (club = descripción).", "Se mira de qué trata y no lo que el hablante quiere lograr.", "Pregunta qué hace el hablante con el tema: invita, cuenta o describe."),
        ("Creer que la audiencia es «todo el mundo».", "No se usan las pistas de quién habla ni de lo que ofrece.", "Busca la frase que nombra o sugiere al público, como No experience is necessary."),
    ],
    [
        (ADULT + THEATRE + " ¿Qué día se reúne el club?", "Los miércoles", "El guion dice every Wednesday."),
        (ADULT + GUIDE + " ¿Qué es este texto? A) una anécdota B) un aviso", "A) una anécdota", "Cuenta un hecho propio con I y el pasado: Last summer I worked."),
        (ADULT + STUDIO + " ¿Cuántos micrófonos hay en la mesa?", "2", "El guion dice two microphones."),
    ],
    [
        (ADULT + THEATRE + " ¿A quién se dirige el aviso? A) a estudiantes que quieran actuar, aunque no tengan experiencia B) a actores profesionales", "A) a estudiantes que quieran actuar, aunque no tengan experiencia", "El guion dice No experience is necessary."),
        (ADULT + GUIDE + " ¿Qué hace la guía desde entonces antes de cada visita?", "Recorre todo el museo", "Dice I always walk the whole museum before a tour."),
        ("Une cada fragmento con su formato. 1) «Join our club and bring a friend!» 2) «Yesterday I forgot my keys at school.» 3) «The living room has a big window and a green sofa.» Formatos: a) anécdota b) descripción c) aviso", "1-c, 2-a, 3-b", "Join y bring son invitaciones; Yesterday I forgot cuenta lo vivido; has a big window describe un lugar."),
    ],
    [
        (ADULT + THEATRE + " ¿Qué día es la jornada abierta (open day)?", "El viernes", "El guion dice open day on Friday."),
        (ADULT + STUDIO + " ¿Qué significa que la luz roja esté encendida? A) que nadie puede entrar B) que el programa terminó", "A) que nadie puede entrar", "El guion dice When the light is on, nobody can enter."),
        arith(ADULT + SHOW + " Una familia compra entradas para dos adultos y tres estudiantes. ¿Cuántos pesos paga en total?", "2*3000+3*1000", "Se suma el costo de los adultos con el de los estudiantes."),
    ],
    [
        (ADULT + THEATRE + " Un compañero dice que es una anécdota. ¿Qué pista lo contradice? A) usa órdenes al público, como Join y Come to our open day B) cuenta con el pasado lo que le ocurrió a quien habla", "A) usa órdenes al público, como Join y Come to our open day", "Una anécdota narra algo vivido; este texto invita al público y no usa el pasado."),
        (ADULT + GUIDE + " ¿Por qué se rieron la guía y el visitante? A) porque la guía, que debía explicar el edificio, estaba perdida B) porque el visitante ya conocía el museo", "A) porque la guía, que debía explicar el edificio, estaba perdida", "Se infiere del contraste entre explicar el edificio y no encontrar la salida."),
    ],
    [
        (ADULT + "«Listen up, everyone: from Monday the studio door stays closed during recordings. Please wait for the green light.» (recordings = grabaciones, wait = esperar, green light = luz verde). Ana dice que el propósito es informar una norma y pedir una conducta. Beto dice que es vender algo. ¿Quién tiene razón? A) Ana B) Beto", "A) Ana", "No ofrece ni precio ni oferta; dice qué hacer, Please wait."),
        ("Ordena según el orden de los hechos en la anécdota de la guía del museo: a) la guía recorre todo el museo antes de cada visita b) la guía se pierde en su primer día c) un visitante le pregunta por la salida", "b, c, a", "Primero se pierde, luego el visitante pregunta y desde entonces recorre el museo."),
    ],
    [(ADULT + "«Hi, listeners. Tomorrow at six, our community radio has a call-in show about local sports. Call us at the number on the poster. The best question wins a free ticket.» (call-in show = programa con llamadas, poster = afiche, wins = gana). ¿Qué gana la mejor pregunta?", "Una entrada gratis", "El guion dice wins a free ticket.")],
    [
        ("¿Qué es el propósito de un texto oral (en Inglés, 2.º medio)?", "La razón por la que alguien habla, lo que quiere lograr", "Se descubre con las pistas del texto."),
        ("¿Qué tiempo verbal predomina en una anécdota?", "El pasado", "Cuenta hechos que ya ocurrieron."),
        ("¿Qué estructura usan las descripciones de lugares para decir qué hay?", "There is o There are", "Sirve para nombrar lo que hay en un lugar."),
    ],
    task("Una persona adulta lee dos veces este aviso: «Hello, teenagers! Our photography club has two free places. We meet on Thursdays at five. Bring any camera or phone. Come to the first session and take your best picture of the school.» (places = cupos, session = sesión). En tu hoja escribe: el propósito, la audiencia, dos datos exactos y una pista del guion que muestre que es un aviso.", "Propósito: invitar a unirse al club de fotografía. Audiencia: adolescentes. Datos: hay dos cupos; se reúnen los jueves a las cinco (también: llevar cámara o teléfono). Pista: Come to the first session es una invitación.", ["nombra el propósito de invitar", "indica la audiencia con una pista del guion", "da dos datos exactos y correctos", "cita una pista de aviso"], ["hoja con cuatro respuestas", "nota de la persona que leyó"], ["decir que es una anécdota", "dar una hora o una cifra que no está en el guion"], "Celebra los datos exactos y relee con la persona la palabra teenagers y la frase Come to para reforzar la audiencia y el propósito."),
    "Pide que te lean de nuevo el aviso del intercambio de libros y marca en tu hoja la invitación.",
    "Escribe en español una anécdota de tres líneas sobre un olvido o una sorpresa y marca qué verbos irían en pasado en inglés.",
)

# ======================================================= clase 2: noticieros y entrevistas
NEWS = "«Good morning. Here is the local news. A new skate park opened on Saturday near the river. It has three ramps and a wide space for beginners. About two hundred young people visited it on the first day. The council said that the park would be open until nine at night. Tonight will be cloudy, with a low of eleven degrees.» (skate park = pista de skate, ramps = rampas, wide = amplio, beginners = principiantes, council = municipalidad, until = hasta, cloudy = nublado, low = mínima, degrees = grados)"
GOAL = "«Reporter: Welcome, Lucas. You are the youngest goalkeeper in the league. Lucas: Thank you. I am sixteen. I train four times a week, on Monday, Tuesday, Thursday and Saturday. Reporter: What is the hardest part? Lucas: Waiting. A goalkeeper often does nothing for ten minutes and then must act in one second.» (reporter = periodista, goalkeeper = arquero, league = liga, train = entrenar, hardest = lo más difícil, waiting = esperar, act = actuar)"
EXAM = "«Hello, this is the language academy. Your English exam is on Friday at ten fifteen in room fourteen. Please bring a pencil and your ID card. The exam lasts one hour.» (exam = examen, room = sala, ID card = credencial, lasts = dura)"

lesson(
    OA, 2, MAT,
    "Aprenderé a distinguir un noticiero de una entrevista y a ubicar en cada uno el dato exacto (cifra, lugar, hora, nombre) que responde una pregunta. Sirve para tomar notas fiables de lo que oyes.",
    ["Sé los números en inglés hasta el millar.", "Sé decir la hora y los días de la semana."],
    [
        "Un noticiero (news broadcast) informa hechos recientes y responde a quién, qué, dónde y cuándo. Una entrevista (interview) tiene dos voces: quien pregunta (reporter) y quien responde, y muestra opiniones o experiencias. Un mensaje grabado (voice message) entrega datos prácticos: horas, lugares, qué llevar. En los tres formatos buscas información específica (specific information): el dato exacto que se pide.",
        "Para encontrar evidencia precisa, escucha primero la pregunta. Si pide «¿cuántos?», busca un número; si pide «¿dónde?», busca una palabra de lugar como near o in room; si pide «¿cuándo?», busca un día u hora. Anota solo la palabra clave. Cuidado con los números parecidos: thirteen (13) suena fuerte al final con teen; thirty (30) lleva la fuerza al principio. La palabra about avisa que la cifra es aproximada.",
        "Después de escuchar, compara tu nota con el guion. Si dos datos compiten, vuelve a la pregunta y elige el que ella pide. En una entrevista, fíjate también en quién dice cada cosa: la opinión es de la persona entrevistada, no del reportero. Un dato exacto no se cambia por uno aproximado.",
    ],
    [("news broadcast", "noticiero"), ("interview", "entrevista: pregunta y respuesta entre dos personas"), ("reporter", "periodista que pregunta"), ("specific information", "información específica: dato exacto"), ("about", "alrededor de: cifra aproximada")],
    [
        ("Cifra exacta en un noticiero", ADULT + "«Good evening. The new sports hall in the north of the city has two courts and room for eighty spectators. It opens at seven in the morning.» (hall = recinto, courts = canchas, spectators = espectadores). ¿Cuántos espectadores caben?", ["La pregunta pide una cantidad, busco un número.", "El guion dice room for eighty spectators.", "Eighty se escribe 80."], "80 espectadores"),
        ("Quién dice qué", ADULT + "«Reporter: Do you like early training? Anita: Honestly, no. I prefer the afternoon.» (early = temprano, prefer = prefiero). ¿Quién prefiere entrenar en la tarde?", ["Pregunto quién habla cuando dice prefer.", "La frase I prefer la dice Anita.", "La reportera solo pregunta."], "Anita"),
    ],
    [
        ("Anotar thirteen cuando se dijo thirty.", "Los dos suenan parecidos; cambia la sílaba más fuerte.", "En thirteen se oye fuerte teen al final; en thirty, la primera sílaba."),
        ("Atribuir a la reportera la opinión de la persona entrevistada.", "No se fija quién habla en cada turno.", "Marca quién pregunta y quién responde antes de anotar la idea."),
    ],
    [
        (ADULT + GOAL + " ¿Cuántos años tiene Lucas?", "16", "El guion dice I am sixteen."),
        (ADULT + NEWS + " ¿Cuántas rampas tiene la pista de skate?", "3", "El guion dice three ramps."),
        (ADULT + EXAM + " ¿En qué sala es el examen?", "En la sala 14", "El guion dice room fourteen."),
    ],
    [
        (ADULT + NEWS + " ¿Quién dijo que el parque abrirá hasta las nueve de la noche? A) la municipalidad B) los jóvenes que lo visitaron", "A) la municipalidad", "El guion dice The council said."),
        (ADULT + GOAL + " ¿Qué es lo más difícil para Lucas?", "Esperar", "Responde con la palabra Waiting a la pregunta What is the hardest part?"),
        (ADULT + NEWS + " ¿Cuántos jóvenes visitaron el parque el primer día? A) alrededor de 200 B) exactamente 20", "A) alrededor de 200", "El guion dice about two hundred; la palabra about indica una cifra aproximada."),
    ],
    [
        (ADULT + EXAM + " ¿A qué hora empieza el examen?", "A las diez y cuarto", "El guion dice ten fifteen."),
        (ADULT + GOAL + " ¿Qué días entrena Lucas? A) lunes, martes, jueves y sábado B) lunes, miércoles, jueves y domingo", "A) lunes, martes, jueves y sábado", "Dice on Monday, Tuesday, Thursday and Saturday."),
        arith(ADULT + GOAL + " Lucas entrena el número de veces por semana que dijo. ¿Cuántas sesiones hace en seis semanas?", "4*6", "Se multiplica el número de entrenamientos semanales por las semanas."),
    ],
    [
        (ADULT + EXAM + " El examen empieza a las 10:15 y dura el tiempo que dice el guion. ¿A qué hora termina? A) a las 11:15 B) a las 11:00", "A) a las 11:15", "Dura one hour: una hora después de las 10:15."),
        (ADULT + GOAL + " ¿Qué muestra que el texto es una entrevista y no un noticiero? A) hay una persona que pregunta y otra que responde B) un locutor da datos de actualidad", "A) hay una persona que pregunta y otra que responde", "Se alternan Reporter y Lucas."),
    ],
    [
        ("Ordena según el orden en que aparecen en el noticiero de la pista de skate: a) la temperatura mínima de la noche b) cuántos jóvenes la visitaron el primer día c) cuándo se inauguró. Usa el guion: " + NEWS, "c, b, a", "El guion nombra primero la apertura del sábado, luego los visitantes y al final el clima."),
        (ADULT + GOAL + " Lucas dice que a veces el arquero no hace nada diez minutos y luego debe actuar en un segundo. ¿Qué cualidad necesita? A) concentración permanente B) correr distancias largas", "A) concentración permanente", "Se infiere: debe estar atento aunque no pase nada."),
    ],
    [(ADULT + "«Hello, this is Marta from the community radio. The volunteers' meeting is on Thursday at six thirty in the main office. Please bring your notebook.» (volunteers = voluntarios, meeting = reunión, office = oficina). ¿A qué hora es la reunión?", "A las seis y media", "El guion dice six thirty.")],
    [
        ("¿Qué preguntas básicas responde un noticiero?", "Qué pasó, quién, dónde y cuándo", "Informa hechos recientes."),
        ("¿Qué indica la palabra about delante de una cifra?", "Que la cifra es aproximada", "No es un dato exacto."),
        ("¿Qué hace la persona que entrevista?", "Hace preguntas", "La que responde es la persona entrevistada."),
    ],
    task("Una persona adulta lee dos veces: «Good afternoon. Here is the school news. The robotics club won second place in the city contest. Twelve students took part. Their teacher said that the next meeting is on Monday at four. The club needs two new members.» (robotics = robótica, contest = concurso, took part = participaron, members = integrantes). En tu hoja escribe cinco datos exactos.", "Club de robótica; segundo lugar; doce estudiantes; reunión el lunes a las cuatro; necesitan dos integrantes nuevos.", ["anota cinco datos distintos", "cada cifra coincide con el guion", "distingue el dato dicho por la profesora"], ["hoja con cinco datos", "nota de la persona que leyó"], ["anotar 20 en lugar de 12", "olvidar el día de la reunión"], "Compara tus datos con el guion y corrige cada cifra con la palabra exacta que oíste."),
    "Pide que te lean otra vez la entrevista a Lucas y subraya quién dice cada idea.",
    "Escribe en español tres preguntas que harías a un deportista de tu comuna en una entrevista.",
)

# ======================================================= clase 3: narraciones y canciones
BOAT = "«Tomás had a small boat and a big dream: to cross the lake alone. One morning the wind was strong, and his father said, ‘Wait.’ Tomás waited all day. At sunset the lake was calm, and he crossed it slowly. When he arrived, he understood that patience is also a kind of courage.» (boat = bote, dream = sueño, cross = cruzar, alone = solo, wind = viento, sunset = atardecer, calm = calmo, slowly = despacio, patience = paciencia, courage = valentía)"
SONG = "«Walking home when the sun goes down, / the streets are quiet in my town. / Tired feet but a happy heart, / tomorrow is a brand-new start.» (sun goes down = el sol se pone, quiet = silenciosas, tired = cansados, heart = corazón, brand-new start = comienzo nuevo)"
HERON = "«A young heron stood by the river all day and refused every small fish. In the evening, no big fish came. The heron went home hungry.» (heron = garza, refused = rechazó, small = pequeño, hungry = con hambre)"

lesson(
    OA, 3, MAT,
    "Aprenderé a entender una narración y una canción originales dichas en voz alta: personajes, orden de los hechos, tema y ánimo. Sirve para seguir una historia oral y explicar qué idea deja.",
    ["Sé el pasado simple de verbos regulares e irregulares comunes.", "Sé que un texto tiene inicio, desarrollo y final."],
    [
        "Una narración (narrative) cuenta una historia con personajes (characters), un conflicto y un final. Usa el pasado simple y palabras de orden como one morning, at sunset, when. Para entenderla, sigue tres cosas: quién actúa, qué problema enfrenta y cómo termina. El tema (theme) es la idea que deja la historia; casi siempre se dice en pocas palabras, por ejemplo «la paciencia requiere valor».",
        "Una canción (song) se apoya en el ritmo y la rima (rhyme): palabras que terminan con el mismo sonido, como down y town. Su ánimo (mood) se deduce de las palabras: quiet y tired transmiten calma y cansancio; happy heart y brand-new start dan esperanza. En una canción no hace falta entender cada verso: basta captar la imagen y el sentimiento.",
        "Una fábula (fable) es una narración corta con animales que enseña una lección o moraleja (moral). Para distinguir el tema de un hecho, pregúntate: ¿qué enseñanza dejaría esto a otra persona? El hecho dice qué pasó; el tema explica por qué importa.",
    ],
    [("narrative", "narración: historia con personajes y final"), ("theme", "tema: idea principal que deja la historia"), ("rhyme", "rima: final de palabras con el mismo sonido"), ("mood", "ánimo: sentimiento que transmite el texto"), ("moral", "moraleja: lección de una fábula")],
    [
        ("Tema de una narración", ADULT + "«Rita lost her race by two seconds. She cried a little, then thanked the winner and trained again the next week. A month later she won.» (race = carrera, thanked = agradeció, trained = entrenó). ¿Cuál es el tema? A) la perseverancia ayuda a superar una derrota B) las carreras son injustas", ["Veo qué hace Rita ante la derrota: agradece y vuelve a entrenar.", "Al final gana por seguir intentando.", "El tema es perseverar."], "A) la perseverancia ayuda a superar una derrota"),
        ("Ánimo de una canción", ADULT + "«The rain is loud, the night is long, / I hold my coat and hum a song. / The clouds will leave, I know it’s true, / and morning light will find me too.» (rain = lluvia, loud = ruidosa, hold = sujeto, hum = tarareo, light = luz). ¿Qué ánimo transmite? A) esperanza dentro de una noche difícil B) alegría de fiesta", ["Las primeras líneas muestran lluvia y noche larga.", "Las últimas dicen que las nubes se irán y llegará la luz.", "Entonces es esperanza en la dificultad."], "A) esperanza dentro de una noche difícil"),
    ],
    [
        ("Confundir el tema con el hecho («el tema es que Rita ganó»).", "El hecho dice qué pasó; el tema es la idea que deja.", "Pregúntate qué enseñanza deja la historia."),
        ("Creer que debes entender todas las palabras de una canción.", "Se pierde la imagen general por detenerse en cada palabra.", "Capta las palabras que repiten la imagen o el sentimiento."),
    ],
    [
        (ADULT + BOAT + " ¿Qué quería hacer Tomás?", "Cruzar el lago solo", "El guion dice a big dream: to cross the lake alone."),
        (ADULT + SONG + " ¿En qué momento del día se camina a casa?", "Cuando se pone el sol", "El primer verso dice when the sun goes down."),
        (ADULT + HERON + " ¿Qué animal aparece en la fábula?", "Una garza", "El guion dice heron."),
    ],
    [
        (ADULT + BOAT + " ¿Por qué esperó Tomás todo el día? A) porque el viento era fuerte y su padre le dijo que esperara B) porque no tenía bote", "A) porque el viento era fuerte y su padre le dijo que esperara", "El guion dice the wind was strong y his father said, Wait."),
        (ADULT + SONG + " ¿Qué palabra rima con town?", "down", "Las dos terminan con el mismo sonido final (town, down)."),
        (ADULT + HERON + " ¿Qué pasó al anochecer?", "No llegó ningún pez grande", "Dice In the evening, no big fish came."),
    ],
    [
        (ADULT + BOAT + " ¿Cómo estaba el lago al atardecer? A) calmo B) agitado", "A) calmo", "El guion dice At sunset the lake was calm."),
        (ADULT + BOAT + " Ordena: a) Tomás cruzó el lago b) Tomás esperó todo el día c) su padre dijo Wait", "c, b, a", "Primero el padre dijo Wait, luego esperó y al final cruzó."),
        (ADULT + SONG + " ¿Cómo se siente la persona de la canción? A) cansada pero contenta B) enojada y sola", "A) cansada pero contenta", "Los versos nombran tired feet y happy heart."),
    ],
    [
        (ADULT + BOAT + " ¿Cuál es el tema? A) la paciencia también es valentía B) los botes son peligrosos", "A) la paciencia también es valentía", "La última frase lo dice: patience is also a kind of courage."),
        (ADULT + HERON + " ¿Qué enseña la fábula? A) no conviene rechazar pequeñas oportunidades B) hay que pescar solo de noche", "A) no conviene rechazar pequeñas oportunidades", "La garza rechazó los peces pequeños y se quedó sin comer."),
    ],
    [
        (ADULT + SONG + " Ana dice que la canción es triste por la palabra quiet. Luis dice que es tranquila y esperanzada por brand-new start. ¿Quién la interpreta mejor? A) Luis B) Ana", "A) Luis", "Quiet es calma y el último verso mira al mañana con esperanza, no con tristeza."),
        (ADULT + BOAT + " Al final Tomás comprende algo. ¿Qué cambió en él? A) comprendió que esperar también requiere valor B) decidió no volver al lago", "A) comprendió que esperar también requiere valor", "Esperó y luego cruzó: la espera fue parte de su valentía."),
    ],
    [(ADULT + "«Clara found a small key near the bus stop. She gave it to the driver. The next day, an old man thanked her: the key opened his little shop.» (key = llave, bus stop = paradero, driver = conductor, shop = tienda). ¿Dónde encontró Clara la llave?", "Cerca del paradero", "El guion dice near the bus stop.")],
    [
        ("¿Qué es el tema de una narración?", "La idea principal que deja la historia", "Es la enseñanza o idea general."),
        ("¿Qué es la rima (en Inglés, 2.º medio)?", "Palabras que terminan con el mismo sonido", "Por ejemplo, down y town."),
        ("¿Qué es una moraleja (en Inglés, 2.º medio)?", "La lección que enseña una fábula", "Aparece al final de la historia."),
    ],
    task("Una persona adulta lee dos veces: «Mia painted a mural on a grey wall by herself. A boy laughed at her colours, so she stopped for a week. Then a neighbour brought her a brush and said, ‘Your wall is waiting.’ Mia finished the mural, and now people stop to look at it.» (mural = mural, wall = muro, by herself = sola, laughed at = se rió de, brush = pincel, neighbour = vecina). En tu hoja escribe: el personaje, el problema, cómo termina y el tema en una frase.", "Personaje: Mia. Problema: un niño se burló de sus colores y dejó de pintar. Final: terminó el mural y la gente lo mira. Tema: no abandonar lo que hacemos por una burla; el apoyo ayuda a continuar.", ["nombra al personaje", "explica el problema", "dice cómo termina", "formula un tema distinto del hecho"], ["hoja con cuatro respuestas", "nota de la persona que leyó"], ["decir solo que pintó un mural", "dar como tema un detalle como el color gris"], "Compara con la persona que leyó si tu tema explica por qué importa la historia, no solo qué pasó."),
    "Pide que te lean otra vez la canción y dibuja en tu hoja la imagen que más te llegó.",
    "Escribe en español un tema y un personaje para una historia corta que cuentes a una persona de tu casa.",
)

# ======================================================= clase 4: exposiciones, discursos y debates breves
PODCAST = "«Good morning, everyone. Today I will explain how to start a school podcast. First, I will talk about choosing a topic. Second, I will describe the equipment you need. Finally, I will give you three tips for a clear voice. The most important tip is to practise before recording.» (podcast = pódcast, topic = tema, equipment = equipo, tips = consejos, voice = voz, practise = practicar, recording = grabar)"
SPEECH = "«Dear classmates, our school needs a quiet room for reading. We all know that the library is crowded at lunch. If we ask the principal together, we can change this. Let’s raise our voices, politely but with courage. Thank you.» (dear = queridos, quiet = tranquila, crowded = llena, principal = director, raise our voices = alzar la voz, politely = con cortesía)"
DEBATE = "«Speaker A: I think students should wear a uniform because it saves time in the morning. Speaker B: I disagree. A uniform limits our identity, and some families spend a lot on it. Speaker A: But a uniform also avoids pressure about clothes.» (speaker = hablante, uniform = uniforme, saves = ahorra, limits = limita, identity = identidad, spend = gastar, pressure = presión, clothes = ropa)"

lesson(
    OA, 4, MAT,
    "Aprenderé a seguir una exposición oral, un discurso y un debate breve: su organización, su propósito y la postura de cada hablante con sus razones. Sirve para entender qué se defiende y con qué argumentos.",
    ["Sé first, second y finally para ordenar ideas.", "Sé que I think y I disagree expresan una opinión."],
    [
        "Una exposición oral (talk) informa sobre un tema y se organiza en partes: saludo, anuncio del tema, desarrollo y cierre. Las palabras first, second y finally te dicen en qué parte vas. Un discurso (speech) busca convencer a un grupo de actuar o pensar de cierta forma; por eso usa un saludo al público (Dear classmates), una razón y una invitación (Let’s…).",
        "Un debate (debate) enfrenta posturas. Cada hablante da una opinión (I think…), una razón (because…) y a veces responde a otro (I disagree; But…). Para entenderlo, anota dos cosas por hablante: su postura (a favor o en contra) y su razón. No confundas la razón de uno con la del otro: en un debate breve, quien habla cambia en cada turno.",
        "Escucha con una pregunta: ¿qué quiere lograr este texto? La exposición quiere explicar, el discurso quiere persuadir y el debate quiere defender una postura frente a otra. Si reconoces el propósito, es más fácil predecir qué dirá el hablante y encontrar los datos importantes.",
    ],
    [("talk", "exposición oral"), ("speech", "discurso: texto oral que busca persuadir"), ("debate", "debate: enfrentamiento de posturas con razones"), ("because", "porque: introduce una razón"), ("disagree", "no estar de acuerdo")],
    [
        ("Postura y razón", ADULT + "«I believe our town needs a youth centre because teenagers have nowhere to meet in the afternoon.» (believe = creo, youth centre = centro juvenil, nowhere = ningún lugar). ¿Cuál es la razón que da el hablante?", ["La razón va después de because.", "Dice teenagers have nowhere to meet in the afternoon.", "Los adolescentes no tienen lugar para reunirse por la tarde."], "Los adolescentes no tienen dónde reunirse por la tarde"),
        ("Respuesta a una objeción", ADULT + "«Speaker C: Homework should be shorter because we need time to rest. Speaker D: I agree, but it must still be useful.» (homework = tarea, shorter = más corta, rest = descansar, useful = útil). ¿Qué condición agrega D?", ["D empieza con I agree: acepta la idea.", "Después de but agrega una condición.", "La condición es que la tarea sea útil."], "Que la tarea siga siendo útil"),
    ],
    [
        ("Atribuir a un hablante la razón del otro.", "No se anota quién habla en cada turno.", "Escribe una columna por hablante con su postura y su razón."),
        ("Tratar el discurso como una exposición neutral.", "No se reconoce el propósito de persuadir.", "Busca el saludo al público, la razón y la invitación a actuar."),
    ],
    [
        (ADULT + PODCAST + " ¿Sobre qué hablará el expositor?", "Sobre cómo empezar un pódcast escolar", "El guion dice how to start a school podcast."),
        (ADULT + SPEECH + " ¿Qué necesita el colegio, según el discurso?", "Una sala tranquila para leer", "Dice a quiet room for reading."),
        (ADULT + DEBATE + " ¿Qué hablante dice I disagree?", "El hablante B", "Responde con desacuerdo a lo que dijo A."),
    ],
    [
        (ADULT + PODCAST + " ¿Cuál es el consejo más importante?", "Practicar antes de grabar", "El guion dice The most important tip is to practise before recording."),
        (ADULT + SPEECH + " ¿Por qué hace falta esa sala? A) porque la biblioteca está llena a la hora de almuerzo B) porque los libros son caros", "A) porque la biblioteca está llena a la hora de almuerzo", "El guion dice the library is crowded at lunch."),
        (ADULT + DEBATE + " ¿Qué razón da A a favor del uniforme?", "Ahorra tiempo en la mañana", "Dice it saves time in the morning."),
    ],
    [
        (ADULT + PODCAST + " Ordena lo que dice la exposición: a) los consejos para la voz b) cómo elegir el tema c) el equipo que se necesita", "b, c, a", "First es el tema, second el equipo y finally los consejos."),
        (ADULT + DEBATE + " ¿Qué dos razones da B contra el uniforme?", "Limita la identidad y algunas familias gastan mucho", "El guion dice limits our identity y some families spend a lot on it."),
        (ADULT + SPEECH + " ¿Qué propone hacer el discurso?", "Pedir juntos al director", "Dice If we ask the principal together."),
    ],
    [
        (ADULT + SPEECH + " ¿A quién se dirige el discurso? A) a sus compañeros de curso B) a una profesora", "A) a sus compañeros de curso", "Empieza con Dear classmates."),
        (ADULT + DEBATE + " A responde: But a uniform also avoids pressure about clothes. ¿Qué hace con esa frase? A) responde a la objeción de B con otra razón B) acepta que B tiene razón", "A) responde a la objeción de B con otra razón", "La palabra But introduce una razón nueva a favor de su postura."),
    ],
    [
        (ADULT + PODCAST + " Marta anotó que primero se graba y después se practica. ¿Qué dijo el expositor en realidad? A) practicar antes de grabar B) grabar y luego practicar", "A) practicar antes de grabar", "El guion dice practise before recording."),
        (ADULT + SPEECH + " ¿Cuál es el propósito del discurso? A) persuadir para actuar juntos B) informar un horario", "A) persuadir para actuar juntos", "Usa Let’s raise our voices, una invitación a actuar."),
    ],
    [(ADULT + "«Speaker E: Phones should be allowed at breaks because we can talk to our families. Speaker F: I disagree, because we stop talking to each other.» (breaks = recreos, allowed = permitidos, talk to each other = hablar entre nosotros). ¿Qué razón da F?", "Que dejan de hablar entre compañeros", "Dice we stop talking to each other.")],
    [
        ("¿Qué palabra introduce una razón en un debate?", "Because", "Después de because se explica por qué."),
        ("¿Cuál es el propósito de un discurso?", "Persuadir a un grupo", "Busca que el público piense o actúe de cierta manera."),
        ("¿Qué indica la expresión I disagree?", "Que no está de acuerdo", "Expresa una postura contraria."),
    ],
    task("Una persona adulta lee dos veces: «Speaker G: School should start later because teenagers feel tired in the morning. Speaker H: I disagree. If school starts later, it ends later, and many students have training in the afternoon.» (later = más tarde, ends = termina, training = entrenamiento). En tu hoja escribe: la postura de G, su razón, la postura de H y su razón.", "G: a favor de empezar más tarde, porque los adolescentes se sienten cansados en la mañana. H: en contra, porque terminaría más tarde y muchos tienen entrenamiento en la tarde.", ["indica la postura de cada hablante", "da la razón correcta de cada uno", "no mezcla las razones"], ["hoja con cuatro respuestas", "nota de la persona que leyó"], ["dar la razón de H a G", "escribir solo opiniones propias"], "Revisa con la persona que leyó que cada razón esté en la columna del hablante correcto."),
    "Pide que te lean otra vez el discurso y marca la invitación a actuar.",
    "Escribe en español una postura y dos razones sobre un tema de tu liceo para usar en un debate breve.",
)

# ======================================================= clase 5: conversaciones, instrucciones y respuesta propositiva
PAINT = "«Ana: Hi, Pablo. Are you free on Saturday? Pablo: Yes, why? Ana: We need two more people to paint the sports hall wall. Pablo: Sure. What time? Ana: At ten. Bring old clothes. Pablo: OK, I will bring my cousin too.» (free = libre, paint = pintar, wall = muro, old clothes = ropa vieja, cousin = primo)"
VOICE = "«To record a short voice message, follow these steps. First, open the app and press the microphone button. Second, speak for no more than thirty seconds. Third, listen to it again. If it is clear, press send. If not, delete it and start again.» (record = grabar, app = aplicación, speak = hablar, delete = borrar, start again = empezar de nuevo)"
PRINTER = "«Mr. Soto: Excuse me, the printer is not working. Student: Did you check the paper? Mr. Soto: Yes, there is paper. Student: Then maybe the cable is loose. Let me look. Mr. Soto: Thank you.» (printer = impresora, check = revisar, cable = cable, loose = suelto)"

lesson(
    OA, 5, MAT,
    "Aprenderé a entender una conversación y unas instrucciones orales y a elegir una respuesta oral que cumpla lo que se pidió. Sirve para colaborar con otras personas y seguir pasos en inglés.",
    ["Sé preguntar y responder con Are you…? y What time…?", "Sé que first, second y third ordenan pasos."],
    [
        "Una conversación (conversation) tiene turnos: alguien propone y alguien responde. Para entenderla, identifica qué pide cada persona y cómo responde la otra. Sure y OK aceptan; I’m sorry, I can’t rechazan con cortesía. Una buena respuesta cumple el propósito de la pregunta: si piden ayuda a las diez, la respuesta incluye si puedes y qué llevarás.",
        "Las instrucciones (instructions) enumeran pasos con first, second, third, then y finally, y usan verbos en imperativo: open, press, speak, delete. También traen condiciones con If: If it is clear, press send. Si no es claro, hay otro camino. Al escuchar, numera los pasos y anota las cantidades, como thirty seconds, porque cambian el resultado.",
        "Para planear una respuesta oral, haz tres preguntas: ¿qué me pidieron? ¿qué dato necesito dar? ¿cómo suena cortés? Un buen mensaje de respuesta incluye una aceptación o rechazo claro, un dato útil y un detalle práctico. Ensayar la respuesta antes de decirla ayuda a hablar con claridad.",
    ],
    [("conversation", "conversación: turnos entre dos personas"), ("instructions", "instrucciones: pasos para hacer algo"), ("sure", "claro, por supuesto: acepta"), ("step", "paso"), ("if", "si: introduce una condición")],
    [
        ("Seguir un turno", ADULT + "«Tina: Can you help me tomorrow? I need to move two chairs to the hall. Leo: I’m sorry, I can’t. I have a dentist appointment. But I can help on Friday.» (move = mover, dentist appointment = hora al dentista). ¿Acepta Leo ayudar mañana?", ["Leo responde I’m sorry, I can’t.", "Da una razón: tiene hora al dentista.", "Propone otro día, el viernes."], "No; propone ayudar el viernes"),
        ("Seguir instrucciones con condición", ADULT + "«To join the video class, click the link. If the screen is black, refresh the page. If it still does not work, call the teacher.» (join = unirse, click = hacer clic, link = enlace, screen = pantalla, refresh = actualizar). La pantalla está negra. ¿Qué haces primero?", ["Busco la condición que habla de pantalla negra.", "La condición dice If the screen is black, refresh the page.", "Primero se actualiza la página."], "Actualizar la página"),
    ],
    [
        ("Responder con un dato que no se pidió.", "No se identifica qué pidió la otra persona.", "Pregúntate qué pidieron y responde primero eso."),
        ("Olvidar la condición If y seguir todos los pasos.", "Se oyen los pasos pero no se escucha cuándo se aplican.", "Marca cada If y revisa si te corresponde."),
    ],
    [
        (ADULT + PAINT + " ¿Qué día es el trabajo?", "El sábado", "El guion dice free on Saturday."),
        (ADULT + VOICE + " ¿Qué botón se presiona primero?", "El del micrófono", "El guion dice press the microphone button."),
        (ADULT + PRINTER + " ¿Qué aparato no funciona?", "La impresora", "El señor Soto dice the printer is not working."),
    ],
    [
        (ADULT + PAINT + " ¿Para qué necesita Ana a dos personas más?", "Para pintar el muro del gimnasio", "Dice to paint the sports hall wall."),
        (ADULT + VOICE + " ¿Cuánto puede durar el mensaje como máximo?", "30 segundos", "Dice no more than thirty seconds."),
        (ADULT + PRINTER + " ¿Qué problema supone el estudiante?", "Que el cable está suelto", "Dice maybe the cable is loose."),
    ],
    [
        (ADULT + PAINT + " ¿Qué debe llevar Pablo?", "Ropa vieja", "Ana dice Bring old clothes."),
        (ADULT + VOICE + " Si el mensaje no se oye claro, ¿qué se hace?", "Se borra y se empieza de nuevo", "Dice If not, delete it and start again."),
        (ADULT + PAINT + " ¿A quién más llevará Pablo?", "A su primo", "Dice I will bring my cousin too."),
    ],
    [
        (ADULT + VOICE + " ¿Por qué se escucha el mensaje antes de enviarlo? A) para comprobar que es claro B) para cambiar el micrófono", "A) para comprobar que es claro", "El paso siguiente depende de si it is clear."),
        (ADULT + PRINTER + " ¿Para qué sirve la pregunta Did you check the paper? A) para descartar una causa posible B) para dar una orden", "A) para descartar una causa posible", "Pregunta algo que puede explicar el problema."),
    ],
    [
        (ADULT + PAINT + " Ana dijo: We need two more people. ¿Qué respuesta oral cumple mejor lo que pidió? A) «Sure. I can bring my brother and a brush.» B) «I like Saturdays.»", "A) «Sure. I can bring my brother and a brush.»", "Acepta, da cuántas personas llegarán y qué llevan; la otra no responde la petición."),
        (ADULT + VOICE + " Ordena los pasos: a) escuchar el mensaje de nuevo b) hablar máximo treinta segundos c) abrir la aplicación y presionar el botón", "c, b, a", "Es el orden de First, Second y Third en las instrucciones."),
    ],
    [(ADULT + "«Hi, Dani. Can you help me tomorrow? I need to carry two boxes of books to the library. I will be at the gate at four.» (carry = llevar, boxes = cajas, gate = portón). ¿A qué hora y dónde se encuentran?", "A las cuatro, en el portón", "El guion dice at the gate at four.")],
    [
        ("¿Qué palabra usas para aceptar una invitación con cortesía?", "Sure", "Significa claro, por supuesto."),
        ("¿Qué palabra introduce una condición en las instrucciones?", "If", "Indica qué hacer en cierto caso."),
        ("¿Qué debe hacer una buena respuesta oral?", "Responder lo que se pidió con un dato útil", "Así cumple el propósito de la pregunta."),
    ],
    task("Una persona adulta lee dos veces: «Hello! Our school choir needs a volunteer for Friday. Can you come at five and help with the chairs?» (choir = coro, volunteer = voluntario, chairs = sillas). En tu hoja escribe en español la respuesta que dirías en inglés: aceptas o rechazas, dices a qué hora llegarás y ofreces algo más que puedas hacer.", "Acepto ir el viernes; llegaré a las cinco; además puedo llevar una mesa o ayudar a ordenar el salón.", ["responde claramente sí o no", "incluye la hora del guion", "ofrece una ayuda adicional concreta"], ["hoja con la respuesta", "nota de la persona que leyó"], ["responder sin decir si aceptas", "cambiar la hora del aviso"], "Compara con la persona que leyó que tu respuesta incluya los tres elementos pedidos."),
    "Pide que te lean otra vez las instrucciones del mensaje de voz y numera los pasos.",
    "Escribe en español una respuesta cortés a una invitación y marca el dato que ofreces.",
)
