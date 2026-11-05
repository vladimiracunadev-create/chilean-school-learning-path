"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 01: significado global y explícito en textos orales variados.

Este archivo también define los ayudantes (lesson, mc, MAT_L, MAT_R, ADULT) que importan los demás módulos in_m2_a*.
Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan glosario en español. Los títulos de clase del plan son genéricos (propósito, evidencia,
relaciones, ensayo, producción): aquí se aplican a formatos orales, cantidades y frecuencia, conectores y relato, y respuesta autónoma.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN2M OA 01"
ADULT = "Un adulto lee en voz alta (tapa el guion): "
MAT_L = "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz."
MAT_R = "Los textos escritos en cada ejercicio, lápiz y una hoja para anotar."


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def mc(stem, right, wrongs, why):
    """Alternativas: la correcta se escribe primera; el registro balancea su posición."""
    options = [o.strip().rstrip(".?!,;") for o in [right] + list(wrongs)]
    q = stem + " " + " ".join(f"{'ABC'[i]}) {o}" for i, o in enumerate(options))
    return ex(q, f"A) {right}", why)


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ clase 1: formatos y propósito
SPEECH = "«Good morning, everyone. I am proud to stand here as your new student council president. If we work together, we can make our school more welcoming. I promise to listen to every class. Thank you.» (proud = orgulloso, student council = centro de estudiantes, welcoming = acogedor, promise = prometo, every = cada)"
DEBATE = "«Speaker A: I believe the school should have a debate club, because students learn to listen to other ideas. Speaker B: I disagree. A club needs a teacher, and every teacher already has many classes.» (speaker = hablante, debate club = club de debate, believe = creo, learn = aprenden, listen = escuchar, disagree = no estoy de acuerdo, already = ya)"
CHARGER = "«Is your phone always out of battery? Try our portable charger! It fits in your pocket and charges two phones at once. Buy one this week and get a second one at half price.» (out of battery = sin batería, charger = cargador, fits = cabe, at once = a la vez, half price = a mitad de precio)"
NEWSB = "«Good evening. The city council announced today that a new public library will open next month on Central Avenue. Workers have already painted the reading rooms. The council hopes more students will use it after school.» (city council = municipalidad, announced = anunció, public library = biblioteca pública, painted = pintaron, reading rooms = salas de lectura)"
PLANE = "«To make a paper airplane, first fold the paper in half. Then fold the top corners to the middle. Next, fold each side again. Finally, throw it gently.» (paper airplane = avión de papel, fold = doblar, corners = esquinas, middle = centro, throw = lanzar, gently = con suavidad)"
CAMP = "«Last summer, I went camping with my cousins. On the second night, a storm woke us up, and we had to move the tent. We were wet and tired, but we laughed about it all week.» (camping = acampar, storm = tormenta, woke up = despertó, tent = carpa, wet = mojados, laughed = nos reímos)"
DESCR = "«The old market in my town is always full of color. There are red tomatoes, green peppers and yellow lemons. It smells like fresh bread, and it is very noisy in the morning.» (market = mercado, full of = lleno de, peppers = pimentones, lemons = limones, smells like = huele a, fresh = fresco, noisy = ruidoso)"
CAPT = "«Reporter: You are the captain of the school basketball team. How do you prepare for a big game? Captain: I eat a good breakfast, I warm up, and I stretch for ten minutes. Reporter: How often does the team practice? Captain: Four times a week.» (reporter = periodista, captain = capitán, prepare = prepararse, warm up = calentar, stretch = estirar, practice = entrenar)"

lesson(
    OA, 1, MAT_L,
    "Aprenderé a reconocer, al escuchar, si un texto es una noticia, un discurso, un debate, un aviso, una entrevista, un procedimiento o una anécdota, y a decir su propósito. Sirve para saber qué información buscar antes de entender los detalles.",
    ["Sé que un texto oral puede informar, convencer, enseñar o contar.", "Conozco first, then, last y las preguntas who, what y when."],
    [
        "En 2.º medio escuchas formatos más variados. Un discurso (speech) se dirige a un público y suele terminar con Thank you. Un debate (debate) enfrenta opiniones: cada hablante da su postura con I believe... o I disagree... y una razón con because. Una noticia (news report) informa un hecho reciente. Una descripción (description) dice cómo es un lugar, una persona o una cosa. Una entrevista (interview) tiene preguntas y respuestas por turnos. Un aviso publicitario (advertisement) quiere que compres algo y usa órdenes y ofertas.",
        "Un procedimiento (procedure) enseña pasos con first, then, next y finally. Una anécdota (anecdote) cuenta algo que le pasó al hablante, en pasado: Last summer I went... El propósito (purpose) es la razón por la que se habla: informar, convencer, enseñar o contar. Un buen oyente descubre el propósito con tres pistas: quién habla, el tipo de verbos (órdenes, pasado, preguntas) y las palabras de cierre.",
        "No necesitas entender todas las palabras. Primero decide el formato, luego el propósito y recién después busca la información que la pregunta pide. La idea general (gist) es lo esencial; los detalles (details) son los datos pequeños como números, nombres y horas.",
    ],
    [("speech", "discurso: habla a un público"), ("debate", "debate: opiniones enfrentadas con razones"), ("news report", "noticia: informa un hecho reciente"), ("description", "descripción: cómo es algo o alguien"), ("procedure", "procedimiento: pasos para hacer algo"), ("anecdote", "anécdota: algo que le pasó al hablante"), ("purpose / gist", "propósito / idea general")],
    [
        ("Reconocer un debate", ADULT + DEBATE + " ¿Qué formato es y cómo lo sabes?", ["Hay dos hablantes con posturas distintas.", "Speaker A usa I believe y Speaker B usa I disagree.", "Cada uno agrega una razón con because o if."], "Es un debate: dos personas defienden opiniones opuestas con razones"),
        ("Reconocer el propósito de un procedimiento", ADULT + PLANE + " ¿Cuál es su propósito?", ["Aparecen first, then, next y finally.", "Las oraciones son órdenes: fold, throw.", "Las órdenes ordenadas enseñan a hacer algo."], "Enseñar a hacer un avión de papel"),
    ],
    [
        ("Decir que un aviso es una noticia porque tiene un dato.", "Se mira el dato y no el propósito: un aviso también trae números y ofertas.", "Pregunta si el texto informa un hecho o quiere que hagas algo, como comprar."),
        ("Decir que una entrevista es una anécdota porque alguien habla de sí mismo.", "Se confunde quién habla con el formato: en la entrevista hay preguntas y turnos.", "Busca si una persona pregunta y otra responde."),
    ],
    [
        (ADULT + SPEECH + " ¿Qué formato es? A) un discurso B) una anécdota", "A) un discurso", "Habla a un público, promete cosas y cierra con Thank you."),
        (ADULT + DESCR + " ¿Qué formato es? A) una descripción B) una noticia", "A) una descripción", "Dice cómo es el mercado con colores, olores y ruidos; no cuenta un hecho reciente."),
        (ADULT + CAPT + " ¿Qué pista muestra que es una entrevista? A) un periodista pregunta y el capitán responde B) una persona cuenta lo que le pasó en pasado", "A) un periodista pregunta y el capitán responde", "Las preguntas y respuestas por turnos son la marca de la entrevista."),
    ],
    [
        (ADULT + NEWSB + " ¿Cuál es el propósito? A) informar un hecho reciente de la ciudad B) convencer de comprar libros", "A) informar un hecho reciente de la ciudad", "Cuenta lo que anunció la municipalidad hoy."),
        (ADULT + CAMP + " ¿Cuál es el propósito? A) compartir una experiencia personal B) enseñar a armar una carpa", "A) compartir una experiencia personal", "El hablante cuenta lo que le pasó, en pasado."),
        (ADULT + SPEECH + " ¿Qué quiere lograr el hablante? A) que el público confíe en él y colabore B) que el público compre una entrada o un producto", "A) que el público confíe en él y colabore", "Promete escuchar a cada curso y dice we can make our school more welcoming."),
    ],
    [
        (ADULT + "Tres mensajes. M1: «Hungry? Visit Pizza Sol this Friday! Buy one pizza and get a second one free!» M2: «Last week I found a phone and I gave it to the teacher.» M3: «First, open the puzzle box. Then put the corner pieces together. Finally, add the middle pieces.» (hungry = con hambre, free = gratis, found = encontré, puzzle = rompecabezas, corner = esquina, pieces = piezas, middle = centro). Clasifica cada mensaje: aviso publicitario, anécdota o procedimiento.", "M1 aviso publicitario, M2 anécdota, M3 procedimiento", "M1 ofrece una oferta con órdenes, M2 cuenta algo pasado y M3 ordena pasos."),
        (ADULT + DEBATE + " ¿Cuál es la razón de Speaker B? A) que un club necesita un profesor y todos ya tienen muchas clases B) que los estudiantes aprenden a escuchar otras ideas", "A) que un club necesita un profesor y todos ya tienen muchas clases", "La razón de B viene después de I disagree; la de aprender a escuchar es de A."),
        (ADULT + CHARGER + " ¿Cuál es la idea general? A) invita a comprar un cargador portátil con una oferta B) explica cómo funcionan los teléfonos", "A) invita a comprar un cargador portátil con una oferta", "Lo esencial es el producto y la oferta; los dos teléfonos son un detalle."),
    ],
    [
        ("Un compañero dice que el texto del cargador es una noticia porque trae una oferta con datos. ¿Quién tiene razón? " + ADULT + CHARGER + " A) no: usa preguntas y órdenes (Try, Buy) para convencer B) sí: todo texto con datos informa un hecho", "A) no: usa preguntas y órdenes (Try, Buy) para convencer", "El dato es un apoyo; el propósito es persuadir."),
        (ADULT + CAPT + " Otro oyente dice que es un debate porque el capitán da su opinión sobre cómo prepararse. ¿Cuál es la mejor respuesta? A) es una entrevista: hay preguntas del periodista y respuestas por turnos B) es un debate: se habla de un tema y el capitán da una opinión sobre cómo prepararse", "A) es una entrevista: hay preguntas del periodista y respuestas por turnos", "En un debate hay posturas opuestas; aquí solo hay un invitado que responde."),
    ],
    [
        (ADULT + "«Hello, I am calling about your poster. Is the guitar still for sale? I can come tomorrow at four and pay in cash.» (poster = afiche, still = todavía, for sale = en venta, pay in cash = pagar en efectivo). ¿Cuál es el propósito de quien llama? A) preguntar si un objeto sigue en venta y acordar una visita B) ofrecer una guitarra en venta y pedir que pasen a comprarla hoy", "A) preguntar si un objeto sigue en venta y acordar una visita", "Pregunta por la guitarra y propone una hora para ir."),
        (ADULT + "«First, click File. Next, click Print. Finally, press Enter.» (click = hacer clic, print = imprimir, press = presiona). ¿Qué formato es? A) un procedimiento B) un aviso publicitario", "A) un procedimiento", "First, next y finally ordenan pasos; las órdenes no intentan vender nada."),
    ],
    [(ADULT + "Estás en una estación y escuchas: «Attention, please. Line two is closed between Central Station and Park Station. Please use the buses outside.» (line = línea, closed = cerrada, between = entre, outside = afuera). ¿Cuál es el propósito? A) avisar un cambio y pedir que uses los buses B) invitar a comprar pasajes de bus", "A) avisar un cambio y pedir que uses los buses", "Informa un cierre y pide una acción con Please use.")],
    [
        ("En Inglés de 2.º medio (OA 1, clase 1): ¿qué es el propósito de un texto oral?", "La razón por la que se habla: informar, convencer, enseñar o contar", "Responde para qué se dice el texto."),
        ("En Inglés de 2.º medio (OA 1, clase 1): ¿qué dos expresiones usa un hablante en un debate para dar su postura?", "I believe... y I disagree...", "Muestran una opinión que luego se apoya con because."),
        ("En Inglés de 2.º medio (OA 1, clase 1): ¿qué es el gist de un texto?", "La idea general, sin los detalles", "Es lo esencial que se entiende al escuchar."),
    ],
    task("Un adulto lee dos veces este texto: «Hello, everyone. Today I will explain why reading is important. If you read every day, you learn new words. Please choose a book you like and start today.» (reading = leer, learn = aprendes, choose = elige, start = empieza). Escribe el formato del texto, su propósito y una frase que te lo mostró.", "Es un discurso breve a un público. Su propósito es explicar y convencer de leer a diario. La pista es: Today I will explain why reading is important, y también la orden Please choose a book you like.", ["nombra un formato coherente", "explica el propósito con sus palabras", "cita una frase del texto como pista"], ["hoja con tres respuestas", "nota del adulto"], ["decir que es una entrevista aunque no hay preguntas", "no citar ninguna pista"], "Reconoce lo que acertó y vuelve a escuchar solo la última frase para decidir qué quiere que haga el oyente."),
    "Pide a un adulto que lea el debate y levanta la mano cada vez que oigas una razón con because o if.",
    "Escribe en español tres frases de una anécdota tuya y subraya las palabras que muestran que ya pasó.",
)

# ------------------------------------------------------------------ clase 2: cantidad, frecuencia y datos explícitos
LIB = "«Welcome to the Youth Library. We have a large number of comics and a small number of dictionaries. There are a few computers free today, so please book a time. We open at nine o'clock and close at six. Membership is free for students.» (comics = cómics, dictionaries = diccionarios, a few = unos pocos, free = libre o gratis, book = reserva, membership = socio)"
BAKE = "«In our school craft workshop, there is little glue left, so we cannot build the models today. We have plenty of paper, though. Few students came this week: only six out of thirty. The teacher usually starts at four and often finishes late.» (craft workshop = taller de manualidades, glue = pegamento, left = que queda, build = armar, models = maquetas, little = poco (incontable), plenty of = mucho, though = sin embargo, few = pocos, usually = por lo general, often = a menudo)"
RADIO = "«Hi, this is Tomás from Radio Stars. I hardly ever miss a soccer match, but this week I have been busy. My team has won rather few games, only three out of ten. Our next match is at a quarter past five on Saturday. Tickets cost four thousand pesos.» (hardly ever = casi nunca, miss = perderse, busy = ocupado, rather = bastante, won = ganó, quarter past five = cinco y cuarto, tickets = entradas)"
SURVEY = "«A school survey asked two hundred students how often they read for fun. A large number, one hundred and twenty, said they read every week. Sixty said they read once a month. Only a small number, twenty, said they never read.» (survey = encuesta, for fun = por gusto, every week = cada semana, once a month = una vez al mes, never = nunca)"
TRAIN = "«Passengers, please listen. The train to the coast leaves from platform fifteen at half past eight. There are few seats left, so please hurry. The trip takes about two hours, and tickets cost nine thousand pesos.» (passengers = pasajeros, coast = costa, platform = andén, half past eight = ocho y media, seats left = asientos que quedan, hurry = apúrate, trip = viaje)"

lesson(
    OA, 2, MAT_L,
    "Aprenderé a escuchar cantidades (a few, few, little, a large number), frecuencia (usually, often, hardly ever) y datos como horas y precios, y a anotarlos con exactitud. Sirve para responder cuántos, cuánto, cada cuánto y cuándo sin confundir datos parecidos.",
    ["Sé contar hasta mil y decir las horas.", "Conozco usually, often y never."],
    [
        "La información explícita es la que el texto dice con palabras claras. Lee la pregunta primero y decide qué dato buscas: how many (cuántos), how much (cuánto cuesta o cuánta cantidad), how often (cada cuánto), when (cuándo) o where (dónde). Anota solo palabras clave: números, días, horas y lugares.",
        "Las cantidades tienen matices. A few significa unos pocos, suficientes para algo: there are a few seats. Few significa casi no hay, y suena negativo. Con cosas incontables (sugar, glue), a little es un poco y little es casi nada: there is little glue. Plenty of significa mucho: plenty of paper. A large number of y a small number of se usan con cosas contables: a large number of students. Las horas se dicen así: half past eight es 8:30, a quarter past five es 5:15 y a quarter to six es 5:45.",
        "La frecuencia se dice con adverbios: always (siempre), usually (por lo general), often (a menudo), sometimes (a veces), hardly ever (casi nunca) y never (nunca). También hay once a month (una vez al mes) o every week (cada semana). Antes de responder, comprueba que el dato anotado responde exactamente a lo que se preguntó.",
    ],
    [("a few / few", "unos pocos / casi ninguno"), ("a little / little", "un poco / casi nada (incontable)"), ("a large number of", "una gran cantidad de (contables)"), ("hardly ever", "casi nunca"), ("half past / a quarter past", "y media / y cuarto"), ("how often", "cada cuánto, con qué frecuencia")],
    [
        ("Ubicar una cantidad", ADULT + SURVEY + " ¿Cuántos estudiantes dijeron que leen cada semana?", ["La pregunta pide una cantidad: busco el número junto a every week.", "Dice one hundred and twenty said they read every week.", "One hundred and twenty se escribe 120."], "120 estudiantes"),
        ("Distinguir little y a little", ADULT + BAKE + " ¿Por qué no pueden armar las maquetas hoy?", ["Busco la razón: aparece con so.", "Dice there is little glue left, so we cannot build the models today.", "Little significa casi nada, entonces falta pegamento."], "Porque casi no queda pegamento"),
    ],
    [
        ("Anotar 50 cuando se dijo fifteen.", "Se confunden los números que terminan en -teen con los que terminan en -ty.", "Escucha dónde cae la fuerza: fifTEEN termina fuerte; FIFty empieza fuerte."),
        ("Entender few como unos pocos pero suficientes.", "Se mezclan few y a few; few suena negativo.", "Si no hay a, piensa casi no hay; con a, piensa hay algunos."),
    ],
    [
        (ADULT + LIB + " ¿A qué hora cierra la biblioteca? A) a las 6 B) a las 9", "A) a las 6", "Dice close at six; las nueve es la apertura."),
        (ADULT + TRAIN + " ¿Desde qué andén sale el tren? A) del andén 15 B) del andén 50", "A) del andén 15", "Dice platform fifteen, que se escribe 15."),
        (ADULT + RADIO + " ¿Cuánto cuestan las entradas? A) 4.000 pesos B) 14.000 pesos", "A) 4.000 pesos", "Dice four thousand pesos."),
    ],
    [
        (ADULT + BAKE + " ¿De qué hay mucho en el taller? A) de papel B) de pegamento", "A) de papel", "Dice plenty of paper; del pegamento queda little."),
        (ADULT + LIB + " ¿Qué hay en gran cantidad? A) cómics B) diccionarios", "A) cómics", "A large number of comics; solo a small number of dictionaries."),
        (ADULT + RADIO + " ¿Con qué frecuencia se pierde Tomás un partido de fútbol? A) casi nunca B) siempre", "A) casi nunca", "Hardly ever miss significa casi nunca perderse un partido."),
    ],
    [
        arith(ADULT + SURVEY + " ¿Cuántos de los 200 estudiantes leen cada semana o una vez al mes?", "120+60", "Se suman los dos grupos que dicen leer.", " estudiantes"),
        arith(ADULT + BAKE + " ¿Cuántos estudiantes de los treinta no vinieron esta semana?", "30-6", "Al total se le resta quienes vinieron.", " estudiantes"),
        arith(ADULT + TRAIN + " Un grupo compra tres pasajes. ¿Cuántos pesos pagan en total?", "3*9000", "Tres pasajes de nueve mil pesos cada uno.", " pesos"),
    ],
    [
        (ADULT + SURVEY + " ¿Qué dice el texto sobre quienes nunca leen? A) son una cantidad pequeña, 20 de 200 B) son más de la mitad de los estudiantes", "A) son una cantidad pequeña, 20 de 200", "Only a small number, twenty."),
        (ADULT + BAKE + " ¿Cuál frase resume a los asistentes? A) vinieron pocos estudiantes, seis de treinta B) vinieron casi todos los estudiantes del curso", "A) vinieron pocos estudiantes, seis de treinta", "Few students came: only six out of thirty."),
    ],
    [
        (ADULT + LIB + " ¿Qué debe hacer un estudiante que quiere usar un computador hoy? A) reservar una hora porque quedan unos pocos libres B) esperar porque no queda ninguno", "A) reservar una hora porque quedan unos pocos libres", "A few computers free, so please book a time."),
        (ADULT + RADIO + " ¿A qué hora es el partido del sábado? A) a las 5:15 B) a las 5:45", "A) a las 5:15", "A quarter past five es cinco y cuarto."),
    ],
    [mc(ADULT + TRAIN + " Llegas a las 8:45 al andén. ¿Qué pasa? Elige.", "El tren salió a las 8:30", ["El tren sale en quince minutos", "Quedan asientos de sobra"], "Half past eight es 8:30, antes de tu llegada.")],
    [
        ("En Inglés de 2.º medio (OA 1, clase 2): ¿qué diferencia hay entre a few y few?", "A few significa unos pocos (hay algunos); few significa casi no hay", "La a cambia el sentido de positivo a negativo."),
        ("En Inglés de 2.º medio (OA 1, clase 2): ¿cómo se dice 5:15 en inglés?", "A quarter past five", "Quarter past es y cuarto."),
        ("En Inglés de 2.º medio (OA 1, clase 2): ¿qué significa hardly ever?", "Casi nunca", "Es un adverbio de frecuencia baja."),
    ],
    task("Un adulto lee dos veces este texto: «The youth club needs help. We have one hundred and twenty chairs, but we need two hundred. The party starts at six o'clock. Please bring three thousand pesos to join us.» (youth club = club juvenil, need = necesitamos, party = fiesta, bring = trae). Anota cuántas sillas hay, cuántas se necesitan, cuántas faltan, a qué hora empieza la fiesta y cuánto hay que llevar.", "Hay 120 sillas; se necesitan 200; faltan 80; empieza a las 6; hay que llevar 3.000 pesos.", ["anota los cinco datos", "calcula la diferencia entre 200 y 120", "usa las unidades correctas"], ["hoja con cinco datos", "nota del adulto"], ["anotar 12 en vez de 120", "no calcular cuántas faltan"], "Valida los datos correctos y escucha otra vez solo los números que no coinciden."),
    "Escucha otra vez el aviso de la biblioteca y anota solo los números y las horas, sin escribir las palabras.",
    "Pide a una persona de tu casa que te lea un aviso de tres cantidades de ejemplo y anótalas.",
)

# ------------------------------------------------------------------ clase 3: pasado anterior y lo que otros dicen
ALEX = "«Last Friday Alex missed the bus because he had left his bag at home. He told me to wait, and then he ran back. When he arrived, the bus had already gone. His sister said she would take him to school by car.» (missed = perdió, had left = había dejado, told me to wait = me dijo que esperara, ran back = volvió corriendo, had gone = ya se había ido, sister = hermana, would take = lo llevaría)"
COACH = "«The coach said the team had trained for two hours before the final. Some players were tired, but she told them to rest. After the match, a journalist asked one player how she felt. She said she had never played in a final before.» (coach = entrenadora, trained = entrenó, final = final, rest = descansar, journalist = periodista, felt = se sintió, never ... before = nunca antes)"
FAIRSC = "«Marina told us about the science fair. She said she had built a small wind turbine with her uncle. Before the fair, she had tested it three times. The judges said her project was clear, and they told her to keep going.» (science fair = feria científica, wind turbine = turbina eólica, uncle = tío, tested = probó, judges = jurado, project = proyecto, keep going = seguir)"
MUSEUM = "«Mr. Díaz said the museum had opened a new room. He told the class to arrive early because the guide had planned a special tour. The students were happy, but one boy said he had forgotten his permission form.» (museum = museo, guide = guía, planned = planificó, special = especial, permission form = autorización, forgotten = olvidado)"

lesson(
    OA, 3, MAT_L,
    "Aprenderé a escuchar relatos con acciones que ocurrieron antes que otras (had + participio) y a entender lo que otras personas dijeron (said, told, asked). Sirve para ordenar los hechos y saber quién dijo qué en noticias, anécdotas y entrevistas.",
    ["Sé reconocer el pasado simple, como went y said.", "Conozco las marcas before, after y because."],
    [
        "El pasado perfecto (past perfect) se forma con had + participio. Sirve para hablar de una acción que ocurrió antes que otra acción pasada. En Alex missed the bus because he had left his bag, primero dejó la bolsa (had left) y después perdió el bus (missed). Las marcas before, after, already y because ayudan a ordenar las dos acciones. Already significa ya, y never ... before significa nunca antes.",
        "El estilo indirecto (reported speech) cuenta lo que otra persona dijo. Se usa said (dijo) o told + persona (le dijo a alguien): She said she had finished. Mr. Díaz told us to arrive early. Al contar lo dicho, los tiempos suelen retroceder: lo que alguien dijo con am pasa a was, y con have finished pasa a had finished. Con told + persona + to + verbo se reportan órdenes o consejos: she told them to rest.",
        "Al escuchar, haz dos preguntas: ¿qué pasó primero? y ¿quién lo dijo? Marca en tu hoja una línea de tiempo con dos puntos y el nombre del hablante. Así no confundes lo que dijo la entrenadora con lo que dijo una jugadora.",
    ],
    [("had + participio", "pasado perfecto: acción anterior a otra pasada"), ("already", "ya"), ("never ... before", "nunca antes"), ("said / told", "dijo / le dijo a alguien"), ("reported speech", "estilo indirecto: contar lo que otro dijo"), ("tell someone to", "pedirle a alguien que haga algo")],
    [
        ("Ordenar dos acciones", ADULT + ALEX + " ¿Qué pasó primero: Alex dejó la bolsa o perdió el bus?", ["Busco had + participio: had left his bag.", "Esa acción es anterior a missed the bus.", "Por eso dejó la bolsa primero."], "Primero dejó la bolsa en casa; después perdió el bus"),
        ("Quién dijo qué", ADULT + COACH + " ¿Quién dijo que nunca había jugado en una final?", ["Busco la frase never played in a final before.", "Va después de a journalist asked one player.", "El sujeto de She said es la jugadora."], "Una jugadora, no la entrenadora"),
    ],
    [
        ("Pensar que had left es lo que pasó después.", "Se piensa que el tiempo más largo es el más reciente, pero had marca la acción anterior.", "Pregunta cuál de las dos acciones ocurrió primero: la que lleva had."),
        ("Confundir quién habla cuando aparece said dos veces.", "Se ignora a quién se refiere cada she said.", "Anota el nombre o el cargo del hablante junto a cada frase."),
    ],
    [
        (ADULT + ALEX + " ¿Por qué perdió el bus Alex? A) porque había dejado su bolsa en casa B) porque su hermana lo llevó al colegio", "A) porque había dejado su bolsa en casa", "Dice because he had left his bag at home."),
        (ADULT + MUSEUM + " ¿Qué le dijo el profesor al curso? A) que llegaran temprano B) que llevaran almuerzo", "A) que llegaran temprano", "Dice he told the class to arrive early."),
        (ADULT + FAIRSC + " ¿Con quién construyó Marina la turbina? A) con su tío B) con el jurado", "A) con su tío", "Dice she had built a small wind turbine with her uncle."),
    ],
    [
        (ADULT + COACH + " ¿Qué les dijo la entrenadora a los jugadores cansados? A) que descansaran B) que entrenaran dos horas más", "A) que descansaran", "She told them to rest."),
        (ADULT + FAIRSC + " ¿Cuántas veces había probado Marina la turbina antes de la feria? A) tres veces B) una vez", "A) tres veces", "Dice she had tested it three times."),
        (ADULT + MUSEUM + " ¿Qué dijo un estudiante? A) que había olvidado la autorización B) que había planificado el recorrido", "A) que había olvidado la autorización", "Dice he had forgotten his permission form; la guía planificó el recorrido."),
    ],
    [
        (ADULT + ALEX + " Ordena los hechos con letras. a) el bus se fue b) Alex dejó la bolsa en casa c) Alex volvió corriendo.", "b, c, a", "Dejó la bolsa, volvió corriendo y cuando llegó el bus ya se había ido (had gone)."),
        (ADULT + COACH + " ¿Qué ocurrió antes de la final? A) el equipo entrenó dos horas B) la periodista le preguntó a una jugadora cómo se sentía", "A) el equipo entrenó dos horas", "Dice had trained for two hours before the final."),
        (ADULT + FAIRSC + " ¿Qué dijo el jurado de su proyecto? A) que era claro B) que era demasiado pequeño", "A) que era claro", "Dice the judges said her project was clear."),
    ],
    [
        (ADULT + ALEX + " ¿Por qué Alex le pidió a su compañero que esperara? A) porque pensaba volver por su bolsa B) porque quería ir en auto con su hermana", "A) porque pensaba volver por su bolsa", "He told me to wait, and then he ran back: volvió a casa por la bolsa."),
        (ADULT + MUSEUM + " ¿Por qué se pidió llegar temprano? A) porque la guía había preparado un recorrido especial B) porque el museo cerraba al mediodía", "A) porque la guía había preparado un recorrido especial", "La razón viene con because: the guide had planned a special tour."),
    ],
    [
        (ADULT + "«My brother told me he had lost his keys, so he asked me to open the door. I said I had left mine at school. In the end, our neighbor helped us, and Mom said we should have a spare key.» (brother = hermano, lost = perdió, neighbor = vecina, spare key = llave de repuesto). ¿Quién había perdido las llaves? A) el hermano B) el narrador", "A) el hermano", "Dice my brother told me he had lost his keys; el narrador las dejó en el colegio."),
        (ADULT + COACH + " Si la jugadora dijo she had never played in a final before, ¿qué se entiende? A) que era su primera final B) que ya había jugado muchas finales", "A) que era su primera final", "Never played in a final before significa nunca antes."),
    ],
    [(ADULT + "«Ms. Ríos told the group the bus had left at noon, so they walked to the next stop. A man said he had seen the bus near the bridge.» (noon = mediodía, stop = parada, seen = visto, bridge = puente). ¿Qué ocurrió primero? A) el bus se fue al mediodía B) el grupo caminó a la siguiente parada", "A) el bus se fue al mediodía", "Had left es la acción anterior; después caminaron.")],
    [
        ("En Inglés de 2.º medio (OA 1, clase 3): ¿cómo se forma el pasado perfecto?", "Con had más el participio, como had left", "Had + participio muestra una acción anterior."),
        ("En Inglés de 2.º medio (OA 1, clase 3): ¿qué significa she told them to rest?", "Les dijo que descansaran", "Told + persona + to + verbo reporta una orden o consejo."),
        ("En Inglés de 2.º medio (OA 1, clase 3): ¿qué dos preguntas conviene hacerse al escuchar un relato con said?", "¿Qué pasó primero? y ¿quién lo dijo?", "Ordenan los hechos y los hablantes."),
    ],
    task("Un adulto lee dos veces: «Last Monday I arrived late because I had forgotten my alarm. My teacher said I should buy a clock. Then my friend told me to try a phone alarm.» (arrived = llegué, forgotten = olvidado, alarm = alarma, clock = reloj, should = deberías). Escribe qué ocurrió primero, qué dijo la profesora y qué dijo el amigo.", "Primero olvidé la alarma. La profesora dijo que debía comprar un reloj. El amigo me dijo que probara una alarma en el teléfono.", ["identifica la acción anterior", "distingue qué dijo cada persona", "usa las marcas had, said y told"], ["hoja con tres respuestas", "nota del adulto"], ["intercambiar lo que dijo cada persona", "ordenar mal los hechos"], "Reconoce qué dato acertó y pide escuchar solo la frase que con told para ubicar al amigo."),
    "Escucha otra vez la anécdota de Alex y dibuja una línea de tiempo con tres puntos.",
    "Cuenta en español algo que pasó en tu día y marca cuál acción ocurrió antes de la otra.",
)

# ------------------------------------------------------------------ clase 4: conectores y relaciones
CONN1 = "«Today's weather report. Neither the north nor the south will have sun this weekend. It will either rain or snow in the mountains. The temperature will be mild, though. The wind is strong, so be careful. As a result, the ski center will close early on Saturday.» (neither ... nor = ni ... ni, either ... or = o ... o, snow = nieve, mild = templada, though = sin embargo, as a result = como resultado, ski center = centro de esquí)"
CONN2 = "«Hi, it's Laura. I will call you as soon as I get home. I won't go to the party unless you come too. I wanted to buy a gift, but it was expensive, so I made a card instead.» (as soon as = tan pronto como, unless = a menos que, gift = regalo, expensive = caro, card = tarjeta, instead = en cambio)"
CONN3 = "«Teacher: Neither Ben nor Clara has handed in the project. Either you give it to me on Monday, or I cannot grade it. Ben: I'm sorry, I'll send it as soon as I finish. Clara: I will bring it unless I am sick.» (handed in = entregó, grade = calificar, sick = enferma, send = enviar)"
CONN4 = "«The school choir practiced every day this month. As a result, they won the regional contest. They were nervous, though. The conductor said they would not enter again unless there were more rehearsals.» (choir = coro, practiced = ensayó, regional contest = concurso regional, conductor = director, enter = participar, rehearsals = ensayos)"

lesson(
    OA, 4, MAT_L,
    "Aprenderé a escuchar los conectores neither...nor, either...or, though, unless, as soon as y as a result, y a usarlos para entender cómo se relacionan las ideas. Sirve para saber qué es causa, qué es contraste y qué es condición en un texto oral.",
    ["Sé usar and, but, because y so.", "Conozco first, then y after."],
    [
        "Los conectores (connectors) unen ideas y marcan su relación. Neither ... nor une dos cosas negativas: neither Ben nor Clara significa ni Ben ni Clara. Either ... or presenta dos opciones: you either study or fail (estudias o repruebas). Though significa sin embargo o aunque, y marca un contraste: it was cold, though, so we stayed. Unless significa a menos que: I won't go unless you come.",
        "As soon as significa tan pronto como: I will call as soon as I arrive. As a result significa como resultado y señala una consecuencia: the team practiced every day. As a result, it won. Estos conectores van en frases cortas, por eso conviene oírlos con calma. Tu pista es el sentido: ¿se oponen las ideas (though), se elige entre dos (either...or), una condición (unless), o es una consecuencia (as a result)?",
        "Para responder, busca la idea antes y después del conector. En el informe del tiempo, though marca un contraste (llueve o nieva, pero la temperatura es templada), y as a result anuncia lo que se hará por el viento fuerte. Fijarte en el conector te ayuda a no confundir causa y consecuencia.",
    ],
    [("neither ... nor", "ni ... ni"), ("either ... or", "o ... o"), ("though", "sin embargo, aunque"), ("unless", "a menos que"), ("as soon as", "tan pronto como"), ("as a result", "como resultado")],
    [
        ("Elegir entre dos opciones", ADULT + CONN1 + " ¿Qué tipo de precipitación habrá en las montañas?", ["Busco either ... or.", "Dice it will either rain or snow.", "Es una de las dos, lluvia o nieve."], "Lluvia o nieve, una de las dos"),
        ("Ver una consecuencia", ADULT + CONN4 + " ¿Qué fue el resultado de ensayar todos los días?", ["Busco as a result.", "Dice As a result, they won the regional contest.", "Esa es la consecuencia."], "Ganaron el concurso regional"),
    ],
    [
        ("Entender unless como si o cuando.", "Se traduce por la forma, pero unless es una condición negativa: a menos que.", "Reemplaza unless por if not: I won't go if you don't come."),
        ("Pensar que neither ... nor afirma las dos cosas.", "Se piensa que une dos ideas positivas, pero niega ambas.", "Traduce neither por ni y nor por ni."),
    ],
    [
        (ADULT + CONN1 + " ¿Qué significa neither the north nor the south? A) ni el norte ni el sur B) el norte y el sur", "A) ni el norte ni el sur", "Neither ... nor niega las dos opciones."),
        (ADULT + CONN2 + " ¿Cuándo va a llamar Laura? A) tan pronto como llegue a casa B) a menos que su amiga la llame", "A) tan pronto como llegue a casa", "As soon as significa tan pronto como."),
        (ADULT + CONN4 + " ¿Qué frase muestra un contraste? A) They were nervous, though B) As a result, they won", "A) They were nervous, though", "Though indica que, aunque ganaron, estaban nerviosos."),
    ],
    [
        (ADULT + CONN3 + " ¿Quién entregó el proyecto? A) ninguno de los dos todavía B) solo Clara, y Ben lo hará el lunes", "A) ninguno de los dos todavía", "Neither Ben nor Clara has handed in the project."),
        (ADULT + CONN2 + " ¿Bajo qué condición irá Laura a la fiesta? A) si su amiga también va B) si compra un regalo caro", "A) si su amiga también va", "I won't go to the party unless you come too."),
        (ADULT + CONN1 + " ¿Por qué cerrará temprano el centro de esquí? A) por el viento fuerte B) por falta de nieve", "A) por el viento fuerte", "La consecuencia as a result sigue a The wind is strong."),
    ],
    [
        (ADULT + CONN3 + " ¿Qué opciones le da la profesora? A) entregar el lunes o no tener nota B) entregar el lunes o hacer otro proyecto", "A) entregar el lunes o no tener nota", "Either you give it to me on Monday, or I cannot grade it."),
        (ADULT + CONN4 + " ¿Cuándo volverá a participar el coro? A) solo si hay más ensayos B) siempre que haya concurso", "A) solo si hay más ensayos", "Would not enter again unless there were more rehearsals."),
        (ADULT + CONN2 + " ¿Por qué hizo una tarjeta? A) porque el regalo era caro B) porque no sabía hacer un regalo", "A) porque el regalo era caro", "La razón se dice con so: it was expensive, so I made a card."),
    ],
    [
        (ADULT + "«Mia said she would come to the concert unless it rained. It was sunny, so she came as soon as she finished lunch. She was late, though, because the bus was full.» (lunch = almuerzo, full = lleno, concert = concierto). ¿Vino Mia? ¿Por qué? A) sí, porque no llovió B) no, porque el bus estaba lleno", "A) sí, porque no llovió", "Unless it rained: como no llovió, la condición para no venir no se cumplió."),
        (ADULT + CONN1 + " ¿Cuál frase es la consecuencia de las condiciones del tiempo? A) el centro de esquí cerrará temprano el sábado B) el viento es fuerte en la zona de las montañas", "A) el centro de esquí cerrará temprano el sábado", "As a result introduce la consecuencia."),
    ],
    [
        (ADULT + CONN3 + " ¿Qué dijo Clara sobre el proyecto? A) que lo traerá, a menos que esté enferma B) que no lo traerá porque está enferma", "A) que lo traerá, a menos que esté enferma", "I will bring it unless I am sick: lo trae salvo que se enferme."),
        (ADULT + CONN2 + " ¿Cuál afirmación es falsa? A) Laura irá a la fiesta aunque su amiga no vaya B) Laura hizo una tarjeta en vez de un regalo", "A) Laura irá a la fiesta aunque su amiga no vaya", "Laura dice I won't go unless you come too; por eso es falso que irá aunque su amiga no vaya."),
    ],
    [
        (ADULT + "«Our class has two options for the trip. We can either go to the zoo or visit the science museum. We cannot do both, because the day is short. As a result, we will vote on Friday.» (trip = paseo, zoo = zoológico, vote = votar, both = ambos). ¿Qué ocurrirá el viernes? A) se votará la actividad B) se visitarán ambos lugares", "A) se votará la actividad", "As a result of cannot do both: se vota para elegir uno."),
    ],
    [
        ("En Inglés de 2.º medio (OA 1, clase 4): ¿qué significa unless?", "A menos que", "Es una condición negativa; equivale a if not."),
        ("En Inglés de 2.º medio (OA 1, clase 4): ¿qué conector marca una consecuencia?", "As a result", "Significa como resultado."),
        ("En Inglés de 2.º medio (OA 1, clase 4): ¿qué conector marca un contraste al final de una frase?", "Though", "Equivale a sin embargo."),
    ],
    task("Un adulto lee dos veces: «Hi, it's Sam. I will text you as soon as I get home. I can't go to the movie theater unless my cousin finishes work. We can either meet at six or at eight. It rained. As a result, the match was canceled.» (text = escribir un mensaje, cousin = primo, finish work = terminar de trabajar, canceled = cancelado). Anota qué conector usa para una condición, para dos opciones y para una consecuencia.", "Condición: unless. Dos opciones: either ... or. Consecuencia: as a result.", ["identifica los tres conectores", "asocia cada uno con su función", "cita la frase donde aparece"], ["hoja con tres respuestas", "nota del adulto"], ["confundir unless con as soon as", "no citar la frase"], "Valida el conector acertado y vuelve a escuchar la frase con canceled para la consecuencia."),
    "Escucha otra vez el informe del tiempo y marca con una cruz cada conector que oigas.",
    "Escribe en español una frase tuya con cada una de estas ideas: una condición, un contraste y una consecuencia.",
)

# ------------------------------------------------------------------ clase 5: respuesta independiente
WALKB = "«In the town of Lomas, a group of parents started a walking group: children walk to school together with an adult every morning. Before, many families used to drive, and the streets were crowded. Now there is less traffic, but some parents say it takes more time.» (walking group = grupo que camina, used to drive = antes iban en auto, crowded = congestionadas, traffic = tráfico, takes more time = toma más tiempo)"
PODC = "«Hello and welcome to Teen Voices. Today we talk to Camila, who has studied violin for five years. Camila, what is the hardest part? Camila: Practicing every day, even when I am tired. But I have learned that small steps help. I used to practice for two hours once a week; now I practice thirty minutes every day.» (hardest = más difícil, practicing = practicar, tired = cansada, small steps = pasos pequeños, once a week = una vez a la semana)"
LOST = "«Last Tuesday, I lost my keys on the way home. I looked in my bag, in my pockets and at the bus stop. Then I called the bus company, and a driver had them! I was happy, but I decided to buy a key ring with my name.» (lost = perdí, keys = llaves, pockets = bolsillos, bus stop = paradero, key ring = llavero)"
TALK = "«Today I want to talk about my study notes. At home I used to write everything on loose sheets. Now I use one notebook for each subject. Because of that, I have lost far fewer pages this year.» (study notes = apuntes, loose sheets = hojas sueltas, subject = asignatura, lost = perdido, far fewer = muchas menos, because of that = por eso)"
SONGB = "«Chorus (original): We are walking, we are singing, the sun is up, the day is long. Together, together, together we are strong!» (chorus = coro, sun = sol, long = largo, together = juntos, strong = fuertes)"

lesson(
    OA, 5, MAT_L,
    "Aprenderé a escuchar por mi cuenta textos nuevos (un reportaje, una entrevista, una anécdota, una charla y un coro original) y a responder con idea general, detalles y una opinión apoyada en el texto. Sirve para demostrar todo lo aprendido sin ayuda.",
    ["Sé reconocer formatos y propósitos orales.", "Sé ubicar cantidades, conectores y acciones anteriores."],
    [
        "Responder de forma independiente (independent response) significa usar tú mismo las estrategias: primero ubicas el formato y el propósito, luego la idea general y por último los detalles que la pregunta pide. Si algo no se entiende, usa las palabras que sí entendiste y el contexto. Una palabra repetida, como together en un coro, muestra el tema central.",
        "Para encontrar un detalle, escucha una segunda vez con la pregunta en mente: ¿quién?, ¿cuántos?, ¿cuándo?, ¿por qué? Para una relación entre ideas, fíjate en los conectores: so y as a result para consecuencia, though y but para contraste, unless para condición. Para acciones anteriores, busca had + participio, y para cambios entre antes y ahora, busca used to y now.",
        "Una opinión (opinion) es lo que tú piensas, y debe apoyarse en el texto: I think... because... Usa un dato del texto para justificarla. Por ejemplo, un grupo que va caminando al colegio puede gustarte porque hay menos tráfico, o no gustarte porque toma más tiempo. Ambas son válidas si citas el texto.",
    ],
    [("independent response", "respuesta independiente"), ("opinion", "opinión"), ("I think... because...", "creo que... porque..."), ("main idea", "idea principal"), ("repeated word", "palabra repetida"), ("used to / now", "antes / ahora")],
    [
        ("Idea general de un reportaje", ADULT + WALKB + " ¿Cuál es la idea general?", ["Pregunta clave: ¿qué hacen los apoderados y para qué?", "Organizan un grupo para caminar al colegio.", "Los detalles son el tráfico y el tiempo."], "En Lomas organizaron un grupo para caminar al colegio, con menos tráfico, pero más tiempo"),
        ("Opinión apoyada", ADULT + WALKB + " ¿Es buena idea caminar en grupo? Responde con una razón del texto.", ["Elijo una postura: sí.", "Busco una razón en el texto: hay menos tráfico.", "Escribo: Creo que es buena idea porque hay menos tráfico."], "Sí, porque hay menos tráfico (también es válida otra postura apoyada en el texto)"),
    ],
    [
        ("Dar una opinión sin ninguna razón.", "Se cree que basta con decir me gusta, pero una opinión necesita apoyo.", "Agrega because y un dato del texto."),
        ("Decir que un coro no se puede entender si no se conocen todas las palabras.", "Se olvida que la repetición y las palabras conocidas muestran el tema.", "Busca la palabra repetida y las palabras que sí entiendes."),
    ],
    [
        (ADULT + WALKB + " ¿Qué cambió en las calles? A) hay menos tráfico B) hay más autos", "A) hay menos tráfico", "Dice Now there is less traffic."),
        (ADULT + SONGB + " ¿Cuál es la palabra más repetida? A) together B) singing", "A) together", "Aparece tres veces en la última línea."),
        (ADULT + LOST + " ¿Dónde estaban las llaves? A) las tenía un conductor del bus B) estaban en el bolsillo", "A) las tenía un conductor del bus", "Dice a driver had them."),
    ],
    [
        (ADULT + SONGB + " ¿De qué trata principalmente el coro? A) de caminar juntos y sentirse fuertes B) de lo largo y cansador que es un día", "A) de caminar juntos y sentirse fuertes", "Walking, together y strong dan el tema."),
        (ADULT + LOST + " ¿Qué decidió hacer al final? A) comprar un llavero con su nombre B) llamar otra vez a la empresa de buses", "A) comprar un llavero con su nombre", "Dice I decided to buy a key ring with my name."),
        (ADULT + PODC + " ¿Qué aprendió Camila? A) que los pasos pequeños ayudan B) que practicar dos horas seguidas es mejor", "A) que los pasos pequeños ayudan", "Dice I have learned that small steps help."),
    ],
    [
        (ADULT + PODC + " ¿Cómo practica ahora Camila? A) treinta minutos cada día B) dos horas una vez a la semana", "A) treinta minutos cada día", "Used to practice two hours once a week es el pasado; now habla del presente."),
        (ADULT + LOST + " ¿En qué orden buscó las llaves? a) llamó a la empresa de buses b) miró en su bolso c) miró en el paradero.", "b, c, a", "Primero el bolso y los bolsillos, luego el paradero y por último la llamada con Then."),
        (ADULT + WALKB + " ¿Qué hacían muchas familias antes? A) iban al colegio en auto B) caminaban con sus hijos", "A) iban al colegio en auto", "Dice many families used to drive."),
    ],
    [
        (ADULT + WALKB + " Un apoderado dice que caminar en grupo es mala idea porque toma más tiempo. ¿Su opinión tiene apoyo en el texto? A) sí, porque some parents say it takes more time B) no, porque el texto no habla de tiempo", "A) sí, porque some parents say it takes more time", "La razón aparece en la última frase."),
        (ADULT + PODC + " ¿Cuál es el propósito de la entrevista? A) mostrar cómo una joven mantiene su práctica de violín B) enseñar a tocar violín con pasos", "A) mostrar cómo una joven mantiene su práctica de violín", "Las preguntas y respuestas hablan de su rutina; no hay pasos."),
    ],
    [
        (ADULT + LOST + " ¿Qué enunciado es verdadero? A) perdió las llaves camino a casa y las recuperó B) perdió las llaves en el colegio y no las encontró", "A) perdió las llaves camino a casa y las recuperó", "Dice on the way home y a driver had them."),
        (ADULT + SONGB + " Un oyente dice que el coro es triste. ¿Qué palabras lo contradicen? A) sun is up y we are strong B) the day is long y we are walking", "A) sun is up y we are strong", "El sol arriba y sentirse fuertes muestran un tono alegre."),
    ],
    [mc(ADULT + TALK + " ¿Cuál es la idea principal?", "El hablante cambió un hábito de estudio y ahora pierde menos hojas", ["Los cuadernos cuestan más que las hojas sueltas y por eso conviene no usarlos", "Estudiar es más difícil este año porque hay muchas asignaturas"], "Used to ... now ... y far fewer muestran el cambio.")],
    [
        ("En Inglés de 2.º medio (OA 1, clase 5): ¿cómo se apoya una opinión en un texto oral?", "Con I think... because... y un dato del texto", "La razón debe salir de lo que se escuchó."),
        ("En Inglés de 2.º medio (OA 1, clase 5): ¿qué muestra una palabra repetida en un coro?", "El tema central", "La repetición destaca la idea principal."),
        ("En Inglés de 2.º medio (OA 1, clase 5): ¿en qué orden conviene responder sobre un texto oral?", "Formato y propósito, idea general y por último detalles", "Va de lo general a lo específico."),
    ],
    task("Un adulto lee dos veces: «Last Sunday, my cousin and I tried to make a card for Grandma. We forgot the glue, so the card fell apart. We laughed a lot and made it again, this time with glue. Now it is our Sunday habit.» (card = tarjeta, forgot = olvidamos, glue = pegamento, fell apart = se desarmó, habit = hábito). Responde en español: formato, idea general, un detalle con dato y tu opinión con una razón.", "Es una anécdota. La idea general es que aprendieron de un error y crearon un hábito. Un detalle: olvidaron el pegamento. Mi opinión: es una buena experiencia porque se rieron y lo repitieron.", ["identifica el formato", "resume la idea general", "da un detalle del texto", "apoya su opinión"], ["hoja con cuatro respuestas", "nota del adulto"], ["opinión sin razón", "confundir detalle e idea general"], "Destaca lo acertado y pide una razón sacada del texto para la opinión."),
    "Pide a una persona de tu casa que lea el coro original y marca cada vez que oigas la palabra together.",
    "Escribe en español una opinión sobre la entrevista de Camila y busca el dato del texto que la apoya.",
)
