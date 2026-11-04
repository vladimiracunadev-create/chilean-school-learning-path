"""Cuaderno del estudiante, 1.º medio Inglés (oficial), IN1M OA 01: significado global y explícito en textos orales variados.

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan pista en español. Todo término nuevo se explica antes de usarlo.
Los títulos de clase del plan son genéricos (propósito, evidencia, estrategia, brecha de información, respuesta independiente):
aquí se aplican a formatos orales, cantidades y horas, idea general y detalle, mensajes incompletos y respuesta autónoma.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN1M OA 01"
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


# ------------------------------------------------------------------ clase 1: formatos y propósito
W_NEWS = "«Good evening. Heavy rain closed two bridges in the town of Valle Claro today. Drivers should take the northern road. The rain will stop tomorrow morning.» (heavy rain = lluvia fuerte, closed = cerró, bridges = puentes, drivers = conductores, northern = del norte, stop = parar)"
W_AD = "«Do you want to learn to play the guitar? Join our music club! Classes start on Monday. Call now and get your first lesson free!» (join = únete a, classes = clases, start = comienzan, call = llama, free = gratis)"
NEWS1 = "«Good morning. The town library opened a new reading room for teenagers yesterday. Mayor Ruiz said it will have forty computers and a quiet corner. Visitors can use it every day until eight in the evening.» (library = biblioteca, reading room = sala de lectura, mayor = alcalde, quiet = tranquilo, corner = rincón, visitors = visitantes)"
AD1 = "«Tired of walking to school? Try the new city bikes! Rent a bike for only five hundred pesos an hour. Download the app and ride today!» (tired of = cansado de, rent = arrendar, only = solo, download = descargar, ride = andar en bicicleta)"
PROC1 = "«To save a document on a computer, first click File. Next, choose Save as. Then write a name for your document. Finally, press Enter.» (save = guardar, choose = elige, name = nombre, press = presiona)"
ANEC1 = "«Last year, I joined the school radio club. On my first day, I was so nervous that I dropped my notes. My friend Paz laughed and helped me pick them up. Now we present the news together every Friday.» (joined = me uní a, nervous = nervioso, dropped = se me cayeron, notes = apuntes, laughed = se rió, pick up = recoger, together = juntos)"
INT1 = "«Presenter: Today we meet Javier, a volunteer at an animal shelter. Javier, why do you volunteer? Javier: Because I love dogs, and they need help. Presenter: How often do you go? Javier: Every Saturday morning.» (presenter = presentador, volunteer = voluntario, shelter = refugio, need = necesitan, often = con qué frecuencia)"
NARR1 = "«Once upon a time a tiny robot lived in an old clock tower. Every night it counted the stars. One night, it counted one star too many, and it found a new comet.» (tiny = diminuto, clock tower = torre del reloj, counted = contaba, stars = estrellas, comet = cometa)"

lesson(
    OA, 1, MAT_L,
    "Aprenderé a reconocer, al escuchar, si un texto es una noticia, un aviso, una entrevista, un procedimiento, una anécdota o una narración, y a decir para qué se dijo. Sirve para saber qué información buscar antes de entender los detalles.",
    ["Sé que un texto oral puede informar, contar o dar instrucciones.", "Conozco palabras como first, then, last, yesterday y every day."],
    [
        "En 1.º medio escuchas textos de muchos formatos. Una noticia (news report) informa un hecho reciente, con lugar y tiempo: yesterday, today, in the town of... Un aviso publicitario (advertisement o ad) quiere convencerte de usar algo, y usa órdenes y preguntas: Try..., Join..., Do you want...? Una entrevista (interview) tiene un presentador que pregunta y una persona que responde por turnos. Una anécdota (anecdote) cuenta algo que le pasó al hablante, en pasado.",
        "Un procedimiento (procedure) enseña pasos con first, next, then y finally. Una narración (narrative) cuenta una historia, real o inventada; muchas empiezan con Once upon a time. Un anuncio o aviso público (announcement) entrega una información breve y útil, como un cambio de horario. Cada formato deja pistas, y la mejor pista es el verbo: pasado en la anécdota, órdenes en el procedimiento y el aviso, preguntas en la entrevista.",
        "El propósito (purpose) es la razón por la que se habla: informar, convencer, enseñar, compartir una experiencia o entretener. La idea general (gist) es lo esencial que entendiste, sin los detalles. No necesitas traducir cada palabra: identifica el formato, deduce el propósito y recién después ubica la información que la pregunta pide.",
    ],
    [("news report", "noticia: informa un hecho reciente"), ("advertisement (ad)", "aviso publicitario: quiere convencer"), ("interview", "entrevista: preguntas y respuestas por turnos"), ("procedure", "procedimiento: pasos para hacer algo"), ("anecdote", "anécdota: algo que le pasó al hablante"), ("purpose / gist", "propósito / idea general")],
    [
        ("Reconocer una noticia", ADULT + W_NEWS + " ¿Qué formato es y cuál es su propósito?", ["Habla de un hecho de hoy, con lugar (Valle Claro) y consecuencias para los conductores.", "No pide comprar ni enseña pasos: entrega información.", "Un texto que informa un hecho reciente es una noticia."], "Es una noticia; su propósito es informar"),
        ("Reconocer un aviso publicitario", ADULT + W_AD + " ¿Qué formato es y cuál es su propósito?", ["Empieza con una pregunta al oyente y usa órdenes: Join, Call.", "Ofrece algo atractivo: la primera clase gratis.", "Quiere que el oyente se inscriba."], "Es un aviso publicitario; su propósito es convencer de unirse al club"),
    ],
    [
        ("Pensar que un texto con precios es una noticia.", "Se mira el dato (un precio) y no el propósito: un aviso también trae números.", "Pregunta si el texto informa un hecho o quiere que el oyente haga algo."),
        ("Decir que una entrevista es una anécdota porque el invitado habla de sí mismo.", "Se confunde quién habla con el formato: la entrevista se reconoce por las preguntas y los turnos.", "Busca si alguien pregunta y otra persona responde."),
    ],
    [
        (ADULT + NEWS1 + " ¿Qué formato es? A) una noticia B) un aviso publicitario", "A) una noticia", "Informa un hecho reciente: la biblioteca abrió una sala ayer."),
        (ADULT + AD1 + " ¿Qué formato es? A) un aviso publicitario B) una entrevista", "A) un aviso publicitario", "Usa preguntas y órdenes (Try, Download) para convencer de usar un servicio."),
        (ADULT + INT1 + " ¿Qué pista muestra que es una entrevista? A) el presentador pregunta y Javier responde B) se explican los pasos de una receta", "A) el presentador pregunta y Javier responde", "Las preguntas y respuestas por turnos son la marca de una entrevista."),
    ],
    [
        (ADULT + PROC1 + " ¿Cuál es el propósito? A) enseñar a guardar un documento B) contar una experiencia", "A) enseñar a guardar un documento", "Usa first, next, then y finally para ordenar los pasos."),
        (ADULT + ANEC1 + " ¿Cuál es el propósito? A) compartir una experiencia personal B) anunciar un servicio", "A) compartir una experiencia personal", "El hablante cuenta lo que le pasó, en pasado."),
        (ADULT + NARR1 + " ¿Por qué es una narración? A) cuenta una historia de ficción y empieza con Once upon a time B) informa un hecho real de hoy", "A) cuenta una historia de ficción y empieza con Once upon a time", "Un robot que cuenta estrellas es ficción, y esa frase abre muchos cuentos."),
    ],
    [
        (ADULT + "Tres mensajes. M1: «Attention, please. The library closes at six today.» M2: «Last week I found a wallet and I returned it to its owner.» M3: «First, add water. Then add the rice. Finally, wait twenty minutes.» (attention = atención, closes = cierra, wallet = billetera, owner = dueño, returned = devolví, add = agrega, wait = espera). Clasifica cada mensaje: aviso público, anécdota o procedimiento.", "M1 aviso público, M2 anécdota, M3 procedimiento", "M1 informa un cierre, M2 cuenta algo pasado y M3 ordena pasos."),
        (ADULT + AD1 + " ¿A quién se dirige principalmente? A) a personas que caminan a la escuela y podrían arrendar una bicicleta B) a conductores de camión", "A) a personas que caminan a la escuela y podrían arrendar una bicicleta", "La pregunta inicial habla de caminar a la escuela."),
        (ADULT + NEWS1 + " ¿Cuál es la idea general? A) la biblioteca abrió una sala de lectura para adolescentes B) el alcalde viajó a otra ciudad", "A) la biblioteca abrió una sala de lectura para adolescentes", "Es lo esencial; los computadores y el horario son detalles."),
    ],
    [
        ("Un amigo dice que el texto de las bicicletas es una noticia porque trae un precio. ¿Quién tiene razón? " + ADULT + AD1 + " A) no: usa órdenes como Try y Download para convencer B) sí: todo texto con precios informa un hecho", "A) no: usa órdenes como Try y Download para convencer", "El precio es un dato de apoyo; el propósito es persuadir."),
        (ADULT + INT1 + " Otro oyente dice que es una anécdota porque Javier habla de sí mismo. ¿Cuál es la mejor respuesta? A) es una entrevista porque un presentador pregunta y Javier responde por turnos B) es una anécdota porque se habla en primera persona", "A) es una entrevista porque un presentador pregunta y Javier responde por turnos", "El formato se decide por la estructura de preguntas y respuestas."),
    ],
    [
        (ADULT + "«Hello, I am calling about your ad. Is the guitar still for sale? I can come tomorrow at four and pay in cash.» (ad = aviso, still = todavía, for sale = en venta, pay in cash = pagar en efectivo). ¿Cuál es el propósito de quien llama? A) preguntar si un objeto sigue en venta y acordar una visita B) informar una noticia de la ciudad", "A) preguntar si un objeto sigue en venta y acordar una visita", "Pregunta por la guitarra y propone una hora para ir."),
        (ADULT + "Un oyente solo entendió las palabras first, next, finally y click. ¿Qué formato podría ser? A) un procedimiento B) una entrevista", "A) un procedimiento", "Esas palabras ordenan pasos y click es una acción."),
    ],
    [(ADULT + "Estás en una estación y escuchas: «Attention, please. Line two is closed between Central Station and Park Station. Please use the buses outside.» (line = línea, closed = cerrada, between = entre, outside = afuera). ¿Cuál es el propósito? A) avisar un cambio y pedir que uses los buses B) contar una anécdota de viaje", "A) avisar un cambio y pedir que uses los buses", "Informa un cierre y pide una acción con Please use.")],
    [
        ("En Inglés de 1.º medio (OA 1, clase 1): ¿qué es el propósito de un texto oral?", "La razón por la que se habla: informar, convencer, enseñar, contar o entretener", "Responde para qué se dice el texto."),
        ("En Inglés de 1.º medio (OA 1, clase 1): ¿qué palabras ordenan los pasos de un procedimiento oral?", "First, next, then y finally", "Marcan el orden de las acciones."),
        ("En Inglés de 1.º medio (OA 1, clase 1): ¿qué es el gist de un texto?", "La idea general, sin los detalles", "Es lo esencial que se entiende al escuchar."),
    ],
    task("Un adulto lee dos veces este texto: «Hello, everyone. Today I will explain why sleep is important. If you sleep well, you can concentrate better at school. Please turn off your phone before bed.» (sleep = dormir, concentrate = concentrarse, turn off = apagar, bed = cama). Escribe el formato del texto, su propósito y una frase que te lo mostró.", "Es una exposición breve. Su propósito es explicar y convencer de dormir bien. La pista es: Today I will explain why sleep is important, y también la orden Please turn off your phone.", ["nombra un formato coherente", "explica el propósito con sus palabras", "cita una frase del texto como pista"], ["hoja con tres respuestas", "nota del adulto"], ["decir que es una entrevista aunque no hay preguntas", "no citar ninguna pista"], "Reconoce lo que acertó y vuelve a escuchar solo la última frase para decidir qué quiere que haga el oyente."),
    "Pide a un adulto que lea el texto de la entrevista y levanta la mano cada vez que oigas una pregunta.",
    "Escribe en español tres frases de una anécdota tuya y subraya las palabras que muestran que ya pasó.",
)

# ------------------------------------------------------------------ clase 2: cantidades, horas y datos explícitos
W_RUN = "«The city marathon had twelve thousand runners this year. The race started at eight o'clock and ended at noon. The winner finished in two hours and ten minutes.» (marathon = maratón, runners = corredores, started = comenzó, ended = terminó, noon = mediodía, winner = ganador, finished = terminó)"
W_STAD = "«The stadium has room for forty thousand people. Last night, thirty-five thousand people came to the concert. Tickets cost nine thousand pesos.» (stadium = estadio, room for = capacidad para, concert = concierto, tickets = entradas)"
FAIR = "«Welcome to the Spring Fair. Tickets cost three thousand pesos for adults and one thousand five hundred pesos for children. The fair has sixty stalls and opens at ten o'clock. There are enough chairs for three hundred people.» (fair = feria, tickets = entradas, adults = adultos, children = niños, stalls = puestos, opens = abre, enough = suficientes, chairs = sillas)"
TREES = "«A small town has planted two hundred thousand trees in five years. Last year, volunteers planted forty thousand trees. The town wants one million trees in ten years. There is not enough water for all of them, so the town will build a new well.» (planted = plantó, trees = árboles, volunteers = voluntarios, wants = quiere, water = agua, well = pozo, build = construir)"
BUS = "«Hi, it's Marta. Two bus tickets cost fourteen thousand pesos in total. We have nine thousand pesos, so we don't have enough money.» (bus ticket = pasaje de bus, in total = en total, enough = suficiente)"
THEATRE = "«The theatre has eight hundred seats. On Friday, six hundred and fifty people came. On Saturday, eight hundred people came, so there were no free seats.» (theatre = teatro, seats = asientos, came = vinieron, free = libres)"
PLAT = "«Please listen. Bus number thirty leaves from platform thirteen at a quarter past seven. Your seat is number forty.» (leaves = sale, platform = andén, a quarter past seven = siete y cuarto, seat = asiento)"
CONC = "«Tickets for the school concert go on sale on Monday at nine. There are two thousand tickets. Each ticket costs eight thousand pesos, but students pay half.» (go on sale = salen a la venta, each = cada, half = la mitad)"

lesson(
    OA, 2, MAT_L,
    "Aprenderé a escuchar cantidades grandes, horas y datos explícitos (los que se dicen con palabras claras) y a anotarlos con exactitud. Sirve para responder cuántos, cuánto cuesta, cuándo y dónde sin confundir datos parecidos.",
    ["Sé contar hasta cien en inglés.", "Conozco los días de la semana y las horas en punto."],
    [
        "La información explícita (explicit information) es la que el texto dice con palabras claras. Para ubicarla, lee primero la pregunta y decide qué dato buscas: how many (cuántos), how much (cuánto cuesta), when (cuándo) o where (dónde). Anota solo palabras clave, no frases enteras: números, días, horas y lugares.",
        "Los números crecen: one hundred es 100, one thousand es 1.000 y one million es 1.000.000. Así, two thousand five hundred es 2.500 y three hundred and forty es 340. Cuidado con los números parecidos: thirteen (13) se acentúa al final y thirty (30) al comienzo; sixteen es 16 y sixty es 60. Enough significa suficiente: There are enough chairs. Not enough significa que falta.",
        "Las horas tienen partes: o'clock es en punto, half past seven es 7:30, a quarter past seven es 7:15 y a quarter to eight es 7:45. Las preposiciones ayudan a ubicar el dato: on con días (on Monday), at con horas (at nine) e in con meses o partes del día (in December). Antes de responder, comprueba que el dato anotado responde exactamente a lo que se preguntó.",
    ],
    [("how many / how much", "cuántos / cuánto cuesta"), ("thousand / million", "mil / millón"), ("enough", "suficiente"), ("half past / a quarter past", "y media / y cuarto"), ("thirteen / thirty", "13 / 30"), ("free", "gratis o libre")],
    [
        ("Ubicar una cantidad", ADULT + W_RUN + " ¿Cuántos corredores hubo?", ["La pregunta pide una cantidad: busco how many o el número junto a runners.", "Dice twelve thousand runners.", "Twelve thousand se escribe 12.000."], "12.000 corredores"),
        ("Comparar con enough", ADULT + W_STAD + " ¿Quedaron asientos libres? ¿Cuántos?", ["La capacidad es forty thousand: 40.000.", "Llegaron thirty-five thousand: 35.000.", "Se resta 40.000 − 35.000 = 5.000."], "Sí, quedaron 5.000 asientos libres"),
    ],
    [
        ("Anotar 30 cuando se dijo thirteen.", "Se confunden thirteen y thirty porque suenan parecidos.", "Escucha dónde cae la fuerza: thirTEEN termina fuerte; THIRty empieza fuerte."),
        ("Responder con un dato de otra pregunta, como la hora de inicio cuando se pregunta el precio.", "Se anota lo primero que se oye y no lo que pide la pregunta.", "Relee la pregunta antes de escribir y marca la palabra que pide el dato."),
    ],
    [
        (ADULT + FAIR + " ¿Cuánto cuesta la entrada de un adulto? A) 3.000 pesos B) 1.500 pesos", "A) 3.000 pesos", "Dice three thousand pesos for adults."),
        (ADULT + FAIR + " ¿Cuántos puestos hay? A) 60 B) 16", "A) 60", "Dice sixty stalls; sixteen sería 16."),
        (ADULT + TREES + " ¿Cuántos árboles quiere tener el pueblo en diez años? A) un millón (1.000.000) B) cuarenta mil (40.000)", "A) un millón (1.000.000)", "Dice one million trees in ten years."),
    ],
    [
        (ADULT + FAIR + " ¿A qué hora abre la feria? A) a las 10 B) a las 3", "A) a las 10", "Dice opens at ten o'clock."),
        (ADULT + TREES + " ¿Cuántos árboles plantaron los voluntarios el año pasado? A) 40.000 B) 14.000", "A) 40.000", "Dice forty thousand trees, no fourteen."),
        (ADULT + BUS + " ¿Tienen suficiente dinero para los pasajes? A) no, el total es 14.000 y tienen 9.000 B) sí, tienen 14.000", "A) no, el total es 14.000 y tienen 9.000", "Marta dice we don't have enough money."),
    ],
    [
        arith(ADULT + FAIR + " Una familia compra 2 entradas de adulto y 1 de niño. ¿Cuántos pesos pagan en total?", "2*3000+1500", "Son dos entradas de 3.000 y una de 1.500.", " pesos"),
        arith(ADULT + BUS + " ¿Cuántos pesos les faltan para comprar los dos pasajes?", "14000-9000", "Al total se le resta lo que tienen.", " pesos"),
        arith(ADULT + TREES + " Si ya hay 200.000 árboles plantados, ¿cuántos faltan para llegar a un millón?", "1000000-200000", "A un millón se le resta lo ya plantado.", " árboles"),
    ],
    [
        (ADULT + FAIR + " Si llegan 350 personas, ¿hay sillas suficientes? A) no: hay para 300 y faltan 50 B) sí: hay para 300, que alcanza", "A) no: hay para 300 y faltan 50", "Hay sillas para 300; 350 − 300 = 50 personas sin silla."),
        (ADULT + TREES + " ¿Por qué construirán un pozo? A) porque no hay suficiente agua para todos los árboles B) porque los voluntarios quieren plantar 40.000 árboles más", "A) porque no hay suficiente agua para todos los árboles", "La razón se dice con so: There is not enough water, so..."),
    ],
    [
        arith(ADULT + THEATRE + " ¿Cuántas personas más fueron el sábado que el viernes?", "800-650", "Al sábado (800) se le resta el viernes (650).", " personas"),
        (ADULT + PLAT + " Anota el número de bus, el andén y el asiento, en ese orden.", "30, 13 y 40", "Bus thirty = 30, platform thirteen = 13, seat forty = 40."),
    ],
    [arith(ADULT + CONC + " ¿Cuántos pesos paga un estudiante por su entrada?", "8000//2", "Los estudiantes pagan la mitad de 8.000.", " pesos")],
    [
        ("En Inglés de 1.º medio (OA 1, clase 2): ¿cómo se dice 2.500 en inglés?", "Two thousand five hundred", "Se dice el miles y luego las centenas."),
        ("En Inglés de 1.º medio (OA 1, clase 2): ¿cómo se diferencian al oído thirteen y thirty?", "En thirteen la fuerza cae al final (13); en thirty cae al comienzo (30)", "El acento marca la diferencia entre 13 y 30."),
        ("En Inglés de 1.º medio (OA 1, clase 2): ¿qué significan how many y how much?", "Cuántos (cosas contables) y cuánto cuesta o cuánta cantidad", "Son las preguntas por cantidad y por precio."),
    ],
    task("Un adulto lee dos veces este texto: «The youth centre needs help. We have one hundred and twenty chairs, but we need two hundred. The party starts at six o'clock. Please bring three thousand pesos to join us.» (youth centre = centro juvenil, need = necesitamos, party = fiesta, bring = trae). Anota en tu hoja cuántas sillas hay, cuántas se necesitan, cuántas faltan, a qué hora empieza y cuánto hay que llevar.", "Hay 120 sillas, se necesitan 200, faltan 80, empieza a las 6 y hay que llevar 3.000 pesos.", ["anota las cinco cantidades o datos", "calcula correctamente las sillas que faltan", "usa el número exacto y no uno parecido"], ["hoja con cinco datos", "nota del adulto"], ["anotar 20 en lugar de 120", "olvidar calcular lo que falta"], "Reconoce los datos exactos y repite la escucha solo en el número que dudó."),
    "Escucha otra vez el aviso de la feria y anota solo los números, sin escribir las palabras.",
    "Inventa un aviso corto en español con tres cantidades (de ejemplo) y pide a una persona de tu casa que las anote al escucharlas.",
)

# ------------------------------------------------------------------ clase 3: idea general primero, detalle después
W_RAFA = "«My name is Rafa. I used to play soccer every day, but now I play the guitar. I have played for two years. Later this year, I want to join a band.» (used to = antes solía, join = unirme a, band = banda)"
W_TOUR = "«Welcome to the museum tour. First, we will see the old photographs. Then we will visit the science room. Later, you can have lunch in the garden. Last, we will return to the bus at three.» (tour = visita guiada, photographs = fotografías, science room = sala de ciencias, lunch = almuerzo, garden = jardín, return = volver)"
ELISA = "«My name is Elisa. I used to live in a small town, but now I live in the capital. I have studied English for six years. Last year I won a school prize, and later this year I want to travel to the south.» (used to = antes solía, capital = capital, have studied = he estudiado, won = gané, prize = premio, travel = viajar, south = sur)"
ROBOT = "«Welcome to the robotics workshop. First, you will build a small robot. Then you will connect the motor. Later, we will test the robots on the table. Last, each group will explain how its robot works.» (robotics = robótica, workshop = taller, build = construir, connect = conectar, motor = motor, test = probar, explain = explicar, works = funciona)"
GRAND = "«My grandfather used to walk ten kilometres to school. Now children take the bus, but he says walking was good exercise.» (grandfather = abuelo, kilometres = kilómetros, take the bus = tomar el bus, exercise = ejercicio)"
MUSIC = "«I have collected stamps for three years. I used to buy them in shops, but now I trade with friends. Last month I found a very old stamp from my grandmother's house. Later I will show it at the school club.» (collected = he coleccionado, stamps = estampillas, trade = intercambiar, shops = tiendas, found = encontré, old = antigua, show = mostrar)"

lesson(
    OA, 3, MAT_L,
    "Aprenderé a escuchar primero la idea general y luego los detalles, apoyándome en palabras clave, marcas de orden (first, then, later, last) y las funciones used to y have + participio. Sirve para no perderme cuando un texto es largo.",
    ["Sé reconocer el formato y el propósito de un texto oral.", "Conozco las marcas first, then y last."],
    [
        "Una estrategia (strategy) es un plan para entender mejor. La más útil es escuchar en dos vueltas. En la primera busca la idea general: quién habla, de qué y para qué. En la segunda busca los detalles que pide la pregunta. No intentes entender todas las palabras: las palabras clave (key words) son los sustantivos, los verbos importantes, los números y los lugares.",
        "Las marcas de orden te dicen la secuencia: first (primero), then (luego), later (más tarde) y last (por último). Dos funciones del año aparecen mucho al hablar de la vida. Used to + verbo habla de un hábito pasado que ya no existe: I used to play soccer (antes jugaba, ahora no). Have + participio con for o since habla de algo que empezó antes y sigue: I have played for two years.",
        "For indica cuánto tiempo (for two years) y since indica desde cuándo (since March). Cuando oigas used to, piensa en un cambio entre antes y ahora. Cuando oigas have played o have studied, piensa en una acción que continúa o en una experiencia hasta hoy. Con esto puedes resumir un texto en una frase.",
    ],
    [("strategy", "estrategia: un plan para entender"), ("key words", "palabras clave"), ("used to", "antes solía (ya no)"), ("have played", "he jugado (hasta hoy)"), ("for / since", "durante / desde"), ("later / last", "más tarde / por último")],
    [
        ("Idea general y detalle", ADULT + W_RAFA + " ¿Cuál es la idea general y cuántos años lleva con la guitarra?", ["Primera vuelta: Rafa habla de un cambio, antes fútbol y ahora guitarra.", "Segunda vuelta: busco el detalle con for.", "Dice I have played for two years."], "Rafa cambió el fútbol por la guitarra; toca hace 2 años"),
        ("Orden de una secuencia", ADULT + W_TOUR + " ¿Qué se hace después de ver las fotografías antiguas?", ["Ubico first: las fotografías.", "La marca siguiente es Then.", "Dice Then we will visit the science room."], "Se visita la sala de ciencias"),
    ],
    [
        ("Confundir used to con una acción que sigue pasando.", "Se piensa que used to describe el presente, pero habla de algo que ya no ocurre.", "Pregunta si el hablante dice que ahora lo hace o que ya no."),
        ("Responder con el primer número que se oyó aunque la pregunta pida otro dato.", "La atención se fija en el primer dato y no en el que pide la pregunta.", "En la segunda vuelta busca solo la palabra de la pregunta."),
    ],
    [
        (ADULT + ELISA + " ¿Dónde vivía Elisa antes? A) en un pueblo pequeño B) en la capital", "A) en un pueblo pequeño", "Used to live in a small town habla del pasado."),
        (ADULT + ELISA + " ¿Desde hace cuánto estudia inglés? A) seis años B) un año", "A) seis años", "Dice have studied English for six years."),
        (ADULT + GRAND + " ¿Qué distancia caminaba el abuelo? A) diez kilómetros B) un kilómetro", "A) diez kilómetros", "Dice used to walk ten kilometres."),
    ],
    [
        (ADULT + ELISA + " ¿Qué quiere hacer Elisa más tarde este año? A) viajar al sur B) ganar un premio escolar", "A) viajar al sur", "Later this year, I want to travel to the south."),
        (ADULT + ROBOT + " ¿Qué se hace al final del taller? A) cada grupo explica cómo funciona su robot B) se construye un robot pequeño", "A) cada grupo explica cómo funciona su robot", "Last marca el último paso."),
        (ADULT + MUSIC + " ¿Cómo consigue ahora las estampillas? A) las intercambia con amigos B) las compra en tiendas", "A) las intercambia con amigos", "Used to buy ... in shops, but now I trade with friends: antes compraba, ahora intercambia."),
    ],
    [
        (ADULT + ROBOT + " Ordena los cuatro pasos del taller con letras. a) probar los robots b) construir un robot c) explicar cómo funciona d) conectar el motor.", "b, d, a, c", "Las marcas first, then, later y last dan el orden."),
        (ADULT + GRAND + " ¿Cuál es la opinión del abuelo? A) que caminar era buen ejercicio B) que el bus es más cómodo", "A) que caminar era buen ejercicio", "Dice he says walking was good exercise."),
        (ADULT + ELISA + " ¿Cuál frase resume mejor el texto? A) Elisa cuenta cambios en su vida y un plan de viaje B) Elisa enseña cómo estudiar inglés", "A) Elisa cuenta cambios en su vida y un plan de viaje", "Mezcla un antes (used to), un hábito de estudio y un plan, sin dar pasos."),
    ],
    [
        (ADULT + MUSIC + " ¿Qué dato es verdadero? A) coleccionar estampillas es algo que hace desde hace tres años B) coleccionó estampillas solo el mes pasado", "A) coleccionar estampillas es algo que hace desde hace tres años", "Dice have collected stamps for three years."),
        (ADULT + MUSIC + " ¿Cuál es la idea general? A) cuenta cómo cambió su forma de conseguir estampillas y qué hará con una antigua B) enseña pasos para pegar una estampilla en una carta", "A) cuenta cómo cambió su forma de conseguir estampillas y qué hará con una antigua", "Mezcla pasado (used to), presente y futuro (later), sin dar pasos."),
    ],
    [
        (ADULT + "«I have lived in Chile for two years, but I used to live in Peru for ten years. Last month I visited my old school there.» (visited = visité, old = antiguo). ¿Cuánto tiempo vivió en Perú? A) diez años B) dos años", "A) diez años", "Used to live in Peru for ten years; los dos años son en Chile."),
        (ADULT + "«I have lived in this neighbourhood since 2018. I used to go to school by bus, but now I ride my bike. Last week, a new bike lane opened.» (neighbourhood = barrio, ride = ando en, bike lane = ciclovía, opened = abrió). ¿Cómo va al colegio ahora? A) en bicicleta B) en bus", "A) en bicicleta", "Used to go by bus es el pasado; hoy dice I ride my bike."),
    ],
    [(ADULT + "«Hello, I am your guide today. First, we will take the lift to the top floor. Then we will walk along the terrace. Later, we will have a snack. Last, we will go down by the stairs.» (guide = guía, lift = ascensor, top floor = último piso, terrace = terraza, snack = colación, stairs = escaleras). ¿Cómo bajan al final? A) por la escalera B) en ascensor", "A) por la escalera", "La marca Last indica el último paso: go down by the stairs.")],
    [
        ("En Inglés de 1.º medio (OA 1, clase 3): ¿qué indica used to + verbo?", "Un hábito del pasado que ya no ocurre", "Contrasta un antes con un ahora."),
        ("En Inglés de 1.º medio (OA 1, clase 3): ¿para qué sirven for y since con have + participio?", "For dice cuánto tiempo y since dice desde cuándo", "Indican la duración de algo que sigue hasta hoy."),
        ("En Inglés de 1.º medio (OA 1, clase 3): ¿qué se busca en la primera vuelta de escucha?", "La idea general: quién habla, de qué y para qué", "Los detalles se dejan para la segunda vuelta."),
    ],
    task("Un adulto lee dos veces este texto: «I have worked at my aunt's bakery for a year. I used to be shy, but now I talk to customers every day. First, I serve the bread. Then I give the change. Last, I clean the table.» (bakery = panadería, shy = tímido, customers = clientes, serve = sirvo, change = vuelto, clean = limpio). Escribe una frase con la idea general y tres detalles.", "La idea general: antes era tímido y ahora habla con clientes en la panadería. Detalles: trabaja ahí hace un año; primero sirve el pan; por último limpia la mesa.", ["escribe una idea general en una frase", "anota tres detalles correctos", "distingue lo pasado (used to) de lo actual"], ["hoja con la idea y los detalles", "nota del adulto"], ["decir que sigue siendo tímido", "confundir el orden de las tareas"], "Reconoce el detalle acertado y vuelve a escuchar las marcas first, then y last para ordenar las tareas."),
    "Escucha otra vez el texto de Elisa y anota solo las palabras clave, no frases completas.",
    "Escribe en español dos cosas que antes hacías y ya no haces, y una que haces desde hace tiempo; sirven para practicar used to y for.",
)

# ------------------------------------------------------------------ clase 4: mensajes incompletos (brecha de información)
W_CLUB = "Persona A: «The English club meets on Wednesdays in room twelve.» Persona B: «It starts at one o'clock. We play word games and watch short videos.» (meets = se reúne, word games = juegos de palabras, short = cortos)"
SCI = "Persona A: «The science fair is on Thursday, and it is in the gym. Entry is free.» Persona B: «It starts at four o'clock and finishes at seven. Bring your student card.» (science fair = feria de ciencias, gym = gimnasio, entry = entrada, finishes = termina, student card = credencial de estudiante)"
BIKE = "Persona A: «We will meet at the park gate on Sunday at nine. The route is twenty kilometres.» Persona B: «Bring water and a helmet. If it rains, we will ride on Monday.» (gate = portón, route = ruta, helmet = casco, rains = llueve, ride = andar en bicicleta)"
BEACH = "Persona A: «The beach clean-up is on Saturday morning. Volunteers get free gloves.» Persona B: «Meet at the pier at eight. Wear old shoes and a hat.» (clean-up = limpieza, volunteers = voluntarios, gloves = guantes, pier = muelle, wear = usa, hat = sombrero)"
COOK = "Persona A: «The cooking class is on Tuesday at five. It costs six thousand pesos.» Persona B: «The class is in the school kitchen. You need an apron and a clean towel.» (cooking class = clase de cocina, costs = cuesta, kitchen = cocina, apron = delantal, towel = toalla)"

lesson(
    OA, 4, MAT_L,
    "Aprenderé a juntar la información que dan dos personas, cada una con una parte del mensaje, y a preguntar lo que falta. Sirve en la vida real: casi nunca una sola persona sabe todo.",
    ["Sé ubicar datos como días, horas y lugares.", "Conozco las preguntas what, where, when y how much."],
    [
        "Una brecha de información (information gap) ocurre cuando cada persona sabe solo una parte del mensaje. Para completar el mensaje, escuchas a las dos y combinas los datos. Primero haz una lista de lo que necesitas saber: qué actividad, qué día, a qué hora, dónde y cuánto cuesta. Luego marca qué dato dio cada persona.",
        "Si falta un dato, pregúntalo. What day is it? pregunta el día. What time does it start? pregunta la hora. Where is it? pregunta el lugar y How much is it? pregunta el precio. Si no entendiste, usa Could you repeat that, please? (¿puedes repetir?) o Do you mean...? (¿quieres decir...?). Pedir ayuda es una estrategia, no una falla.",
        "Cuando combinas datos, cuida que sean coherentes. Por ejemplo, si una persona dice Wednesday y la otra dice one o'clock, el mensaje completo es el miércoles a la una. Mira también las condiciones con if: If it rains, we will ride on Monday significa que el plan cambia solo si llueve.",
    ],
    [("information gap", "brecha de información"), ("What time...?", "¿A qué hora...?"), ("Where is it?", "¿Dónde es?"), ("How much is it?", "¿Cuánto cuesta?"), ("Could you repeat that?", "¿Puedes repetir eso?"), ("if", "si (condición)")],
    [
        ("Combinar dos partes", ADULT + W_CLUB + " ¿Qué día, a qué hora y dónde se reúne el club?", ["Persona A dice el día y el lugar: miércoles, sala doce.", "Persona B dice la hora: one o'clock.", "Se juntan los tres datos."], "Los miércoles, a la una, en la sala 12"),
        ("Preguntar lo que falta", ADULT + W_CLUB + " Solo escuchaste a Persona A. ¿Qué pregunta haces para saber la hora?", ["A no dijo la hora.", "La pregunta por la hora empieza con What time.", "Se pregunta What time does it start?"], "What time does it start?"),
    ],
    [
        ("Dar por completo un mensaje al oír solo a una persona.", "Se olvida que la otra persona tiene datos que la primera no dio.", "Escribe qué datos faltan y espera a escuchar a las dos personas."),
        ("Mezclar el día de una actividad con el de otra.", "Los datos se anotan sin etiqueta y luego se asocian mal.", "Anota cada dato junto a su actividad."),
    ],
    [
        (ADULT + SCI + " ¿Qué día es la feria de ciencias? A) el jueves B) el viernes", "A) el jueves", "Persona A dice on Thursday."),
        (ADULT + SCI + " ¿A qué hora empieza? A) a las cuatro B) a las siete", "A) a las cuatro", "Persona B dice It starts at four o'clock; las siete es la hora de término."),
        (ADULT + BEACH + " ¿Dónde se juntan los voluntarios? A) en el muelle B) en la playa grande", "A) en el muelle", "Persona B dice Meet at the pier."),
    ],
    [
        (ADULT + SCI + " ¿Qué información entrega solo Persona B? A) la hora de inicio y término, y qué llevar B) el día y el lugar", "A) la hora de inicio y término, y qué llevar", "El día y el lugar los dijo Persona A."),
        (ADULT + COOK + " ¿Qué datos tiene solo Persona A? A) el día, la hora y el precio B) el lugar y lo que hay que llevar", "A) el día, la hora y el precio", "Tuesday, five y six thousand pesos son de A; kitchen y apron son de B."),
        (ADULT + BEACH + " ¿Qué se lleva a la limpieza de playa? A) zapatos viejos y sombrero B) guantes", "A) zapatos viejos y sombrero", "Persona B pide old shoes and a hat; los guantes los entregan."),
    ],
    [
        (ADULT + COOK + " Si solo hubieras escuchado a Persona A, ¿qué pregunta harías para saber dónde es la clase? A) Where is the class? B) How much is the class?", "A) Where is the class?", "Where pregunta por el lugar."),
        (ADULT + BIKE + " ¿Qué pasa si llueve el domingo? A) el paseo se hace el lunes B) el paseo se cancela para siempre", "A) el paseo se hace el lunes", "Dice If it rains, we will ride on Monday."),
        arith(ADULT + SCI + " ¿Cuántas horas dura la feria de ciencias?", "7-4", "Empieza a las 4 y termina a las 7.", " horas"),
    ],
    [
        arith(ADULT + COOK + " Tres amigos van a la clase de cocina. ¿Cuántos pesos pagan entre todos?", "3*6000", "Se multiplican tres personas por 6.000 pesos.", " pesos"),
        (ADULT + BIKE + " Un amigo anotó: domingo, nueve de la mañana, portón del parque, veinte kilómetros. ¿Qué dato de Persona B falta en su nota? A) llevar agua y casco B) la hora de llegada", "A) llevar agua y casco", "Su nota solo tiene lo que dijo A."),
    ],
    [
        (ADULT + BEACH + " Alguien que solo escuchó a Persona B cree que la limpieza es en la tarde. ¿Qué dato de Persona A lo corrige? A) que es el sábado en la mañana B) que se entregan guantes gratis", "A) que es el sábado en la mañana", "Persona A dice Saturday morning; los guantes no hablan del horario."),
        (ADULT + "Persona A: «The film club meets on Fridays.» Persona B: «We watch a short film at five o'clock in the library. Entry is two thousand pesos.» (film club = club de cine, short film = cortometraje, library = biblioteca). ¿Cuánto cuestan las entradas de dos amigos? A) 4.000 pesos B) 2.000 pesos", "A) 4.000 pesos", "Cada entrada cuesta 2.000 y son dos amigos: 2 × 2.000."),
    ],
    [arith(ADULT + "Persona A: «The bake sale is on Friday in the school patio.» Persona B: «Every cake costs one thousand pesos, and the money is for a school trip.» (bake sale = venta de pasteles, patio = patio, cake = pastel, trip = paseo). Compras 3 pasteles. ¿Cuántos pesos pagas?", "3*1000", "Cada pastel cuesta 1.000 pesos.", " pesos")],
    [
        ("En Inglés de 1.º medio (OA 1, clase 4): ¿qué es una brecha de información?", "Una situación en que cada persona sabe solo una parte del mensaje", "Hay que combinar lo que dicen ambas."),
        ("En Inglés de 1.º medio (OA 1, clase 4): ¿qué se dice para pedir que repitan?", "Could you repeat that, please?", "Es la frase para pedir repetición."),
        ("En Inglés de 1.º medio (OA 1, clase 4): ¿cómo se pregunta por el precio?", "How much is it?", "How much pregunta cuánto cuesta algo."),
    ],
    task("Un adulto lee este mensaje en dos voces. Voz 1: «The movie night is on Saturday in the community hall.» Voz 2: «It starts at seven. Bring a chair. Tickets are two thousand pesos.» (movie night = noche de cine, community hall = sede vecinal, chair = silla). En tu hoja escribe el mensaje completo en español y una pregunta en inglés que harías si no hubieras oído el precio.", "Noche de cine el sábado a las 7 en la sede vecinal; llevar silla; entradas a 2.000 pesos. Pregunta: How much is it?", ["junta los datos de las dos voces", "no inventa datos nuevos", "escribe una pregunta en inglés correcta"], ["hoja con el mensaje completo", "pregunta escrita"], ["olvidar los datos de una voz", "escribir una pregunta que no pide el dato que falta"], "Reconoce los datos reunidos y revisa cuál faltó; si la pregunta no pide el dato correcto, vuelve a las preguntas what, where, when y how much."),
    "Relee el mensaje de la feria de ciencias y marca con dos colores lo que dijo cada persona.",
    "Pide a una persona de tu casa que te dé la mitad de un mensaje (un día y un lugar) y tú pregunta en inglés la hora y el precio.",
)

# ------------------------------------------------------------------ clase 5: respuesta independiente
WALK = "«In the town of Lomas, a group of parents started a walking bus: children walk to school together with an adult every morning. Before, many families used to drive, and the streets were crowded. Now there is less traffic, but some parents say it takes more time.» (walking bus = bus a pie, parents = apoderados, drive = ir en auto, crowded = llenas, traffic = tráfico, takes more time = toma más tiempo)"
SONG = "«Chorus: We are walking, we are singing, the sun is up, the day is long. Together, together, together we are strong!» (chorus = coro, sun = sol, long = largo, together = juntos, strong = fuertes)"
LOST = "«Last Tuesday, I lost my keys on the way home. I looked in my bag, in my pockets and at the bus stop. Then I called the bus company, and a driver had them! I was happy, but I decided to buy a key ring with my name.» (lost = perdí, keys = llaves, pockets = bolsillos, bus stop = paradero, driver = conductor, key ring = llavero)"
PODCAST = "«Hello and welcome to Teen Voices. Today we talk to Camila, who has studied violin for five years. Camila, what is the hardest part? Camila: Practising every day, even when I am tired. But I have learned that small steps help. I used to practise for two hours once a week; now I practise thirty minutes every day.» (teen voices = voces jóvenes, violin = violín, hardest = lo más difícil, tired = cansada, small steps = pasos pequeños, once a week = una vez por semana)"

lesson(
    OA, 5, MAT_L,
    "Aprenderé a escuchar por mi cuenta textos nuevos (un reportaje, una canción original, una anécdota y una entrevista) y a responder con idea general, detalles y una opinión apoyada en el texto. Sirve para demostrar todo lo aprendido sin ayuda.",
    ["Sé reconocer formatos y propósitos orales.", "Sé ubicar números, horas, orden y datos de dos personas."],
    [
        "Responder de forma independiente (independent response) significa usar tú mismo las estrategias: primero ubicas el formato y el propósito, luego la idea general y por último los detalles que la pregunta pide. Si algo no se entiende, usa las palabras que sí entendiste y el contexto: el tema, los participantes y las pistas del texto.",
        "Las canciones, aunque tengan rima y repitan palabras, también se entienden por la idea general. La repetición de una palabra (together) muestra el tema central. En una entrevista, la pregunta anticipa el tema de la respuesta. En una anécdota, observa el problema, qué hizo la persona y cómo terminó.",
        "Una opinión (opinion) es lo que tú piensas, y debe apoyarse en el texto: I think... because... Usa un dato del texto para justificar. Por ejemplo, la idea de caminar al colegio puede gustarte porque hay menos tráfico, o no gustarte porque toma más tiempo. Ambas son válidas si citas el dato que las apoya.",
    ],
    [("independent response", "respuesta independiente"), ("opinion", "opinión"), ("I think... because...", "creo que... porque..."), ("main idea", "idea principal"), ("repeated word", "palabra repetida"), ("problem / solution", "problema / solución")],
    [
        ("Idea general de un reportaje", ADULT + WALK + " ¿Cuál es la idea general?", ["Pregunta clave: ¿qué hacen los apoderados y para qué?", "Organizan un bus a pie para ir al colegio.", "Los detalles son el tráfico y el tiempo."], "En Lomas organizaron un bus a pie para ir al colegio, con ventajas y una desventaja"),
        ("Opinión apoyada", ADULT + WALK + " ¿Es buena idea el bus a pie? Responde con una razón del texto.", ["Elijo una postura: sí.", "Busco una razón en el texto: hay menos tráfico.", "Escribo: Creo que es buena idea porque hay menos tráfico."], "Sí, porque hay menos tráfico (otra respuesta válida: no, porque toma más tiempo)"),
    ],
    [
        ("Dar una opinión sin ninguna razón.", "Se cree que basta con decir me gusta, pero una opinión necesita apoyo.", "Agrega because y un dato del texto."),
        ("Decir que una canción no se puede entender si no se conocen todas las palabras.", "Se olvida que la repetición y el coro muestran el tema.", "Busca la palabra repetida y las palabras que sí conoces."),
    ],
    [
        (ADULT + WALK + " ¿Qué cambió en las calles? A) hay menos tráfico B) hay más autos", "A) hay menos tráfico", "Dice Now there is less traffic."),
        (ADULT + SONG + " ¿Cuál es la palabra más repetida? A) together B) singing", "A) together", "Aparece tres veces en el último verso."),
        (ADULT + LOST + " ¿Dónde estaban las llaves? A) las tenía un conductor del bus B) estaban en el bolsillo", "A) las tenía un conductor del bus", "Dice a driver had them."),
    ],
    [
        (ADULT + SONG + " ¿De qué trata principalmente la canción? A) de caminar juntos y sentirse fuertes B) de un viaje en avión", "A) de caminar juntos y sentirse fuertes", "Walking, together y strong dan el tema."),
        (ADULT + LOST + " ¿Qué decidió hacer al final? A) comprar un llavero con su nombre B) dejar de usar el bus", "A) comprar un llavero con su nombre", "Dice I decided to buy a key ring with my name."),
        (ADULT + PODCAST + " ¿Qué aprendió Camila? A) que los pasos pequeños ayudan B) que debe practicar solo los fines de semana", "A) que los pasos pequeños ayudan", "Dice I have learned that small steps help."),
    ],
    [
        (ADULT + PODCAST + " ¿Cómo practica ahora Camila? A) treinta minutos cada día B) dos horas una vez a la semana", "A) treinta minutos cada día", "Used to practise two hours once a week es el pasado; now habla del presente."),
        (ADULT + LOST + " ¿En qué orden buscó las llaves? a) llamó a la empresa de buses b) miró en su bolso c) miró en el paradero.", "b, c, a", "Primero el bolso y los bolsillos, luego el paradero y por último la llamada con Then."),
        (ADULT + WALK + " ¿Qué hacían muchas familias antes del bus a pie? A) iban al colegio en auto B) caminaban con sus hijos", "A) iban al colegio en auto", "Dice many families used to drive."),
    ],
    [
        (ADULT + WALK + " Un apoderado dice que el bus a pie es mala idea porque toma más tiempo. ¿Su opinión tiene apoyo en el texto? A) sí, porque some parents say it takes more time B) no, porque el texto no habla de tiempo", "A) sí, porque some parents say it takes more time", "La razón aparece al final del texto."),
        (ADULT + PODCAST + " ¿Cuál es el propósito de la entrevista? A) mostrar cómo una joven mantiene su práctica de violín B) vender clases de violín", "A) mostrar cómo una joven mantiene su práctica de violín", "Las preguntas y respuestas hablan de su rutina, sin invitar a comprar."),
    ],
    [
        (ADULT + LOST + " ¿Qué enunciado es verdadero? A) perdió las llaves camino a casa y las recuperó B) perdió las llaves en el colegio y no las encontró", "A) perdió las llaves camino a casa y las recuperó", "Dice on the way home y a driver had them."),
        (ADULT + SONG + " Un oyente dice que la canción es triste. ¿Qué palabras lo contradicen? A) sun is up y strong B) tired y lost", "A) sun is up y strong", "El sol arriba y sentirse fuertes muestran un tono alegre."),
    ],
    [(ADULT + "«Today I want to talk about plastic bottles. At home we used to throw them away. Now we use one big bottle and refill it. Because of that, we have thrown away fewer bottles this year.» (plastic = plástico, throw away = botar, refill = rellenar, fewer = menos, because of that = por eso). ¿Qué cambió? A) pasaron de botar botellas a rellenar una grande B) compraron más botellas pequeñas", "A) pasaron de botar botellas a rellenar una grande", "Used to throw them away describe el antes; now we use one big bottle, el ahora.")],
    [
        ("En Inglés de 1.º medio (OA 1, clase 5): ¿cómo se apoya una opinión en un texto oral?", "Con I think... because... y un dato del texto", "La razón debe salir de lo que se escuchó."),
        ("En Inglés de 1.º medio (OA 1, clase 5): ¿qué muestra una palabra repetida en una canción?", "El tema central", "La repetición destaca la idea principal."),
        ("En Inglés de 1.º medio (OA 1, clase 5): ¿en qué orden conviene responder sobre un texto oral?", "Formato y propósito, idea general y por último detalles", "Va de lo general a lo específico."),
    ],
    task("Un adulto lee dos veces este texto: «Last Sunday, my cousin and I tried to bake bread. We forgot the salt, so the bread was not tasty. We laughed a lot and baked again, this time with salt. Now it is our Sunday habit.» (bake = hornear, forgot = olvidamos, salt = sal, tasty = rico, habit = costumbre). Escribe el formato, la idea general, dos detalles y tu opinión con I think... because...", "Es una anécdota. Idea general: dos primos se equivocaron al hacer pan y lo repitieron. Detalles: olvidaron la sal; hoy es su costumbre del domingo. Creo que fue divertido porque se rieron mucho.", ["identifica el formato", "resume la idea general en una frase", "anota dos detalles correctos", "da una opinión con una razón del texto"], ["hoja con las cuatro respuestas", "nota del adulto"], ["opinión sin razón", "detalles de otro texto"], "Reconoce lo que ubicó bien y pide que apoye la opinión con un dato; si falla un detalle, vuelve a escuchar solo esa parte."),
    "Pide a una persona de tu casa que lea la canción original y marca cada vez que oigas la palabra together.",
    "Escribe en español una opinión sobre la entrevista de Camila y busca el dato del texto que la apoya.",
)
