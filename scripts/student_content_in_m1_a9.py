"""Cuaderno del estudiante, 1.º medio Inglés (oficial), IN1M OA 09: ideas generales e información explícita en textos impresos y digitales.

Las clases del plan son genéricas; aquí se aplican a: formato y propósito de textos (correos, avisos, páginas web, reseñas),
datos precisos en tablas y notas, estrategias de lectura (skimming, scanning, inferir palabras), dos textos con información
repartida y una lectura independiente. Cada texto va completo en el enunciado, con pista en español.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN1M OA 09"
MAT = "Los textos escritos en cada ejercicio (correos, avisos, páginas web, tablas), lápiz y una hoja para anotar."


def U(texto):
    """Quita la etiqueta de formato («Correo:», «Aviso:»…) para que el estudiante deba reconocerlo."""
    return texto.split(": ", 1)[1]


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


# ------------------------------------------------------------------ clase 1: formato, propósito y contexto
W_MAIL = "Correo: «Subject: Volleyball practice. Hi team, practice is moved to Thursday at 5 pm in the gym. Please bring water. Coach Vera.» (subject = asunto, practice = entrenamiento, moved = cambiado, gym = gimnasio, bring = traigan)"
W_WEB = "Página web: «Home | Courses | Contact. Learn photography online! Join our beginner course. Sign up before May 15 and get a discount.» (courses = cursos, beginner = principiante, sign up = inscríbete, discount = descuento)"
SECRE = "Correo: «Subject: Uniform change. Dear parents, from next Monday, students can wear the school tracksuit on Wednesdays. The change is for the whole term. Best regards, Ms Paredes, secretary.» (parents = apoderados, tracksuit = buzo, whole term = todo el semestre, best regards = saludos cordiales)"
LAB = "Aviso: «NOTICE: The computer lab will be closed on Friday for maintenance. It will open again on Monday at eight. Sorry for the problem.» (notice = aviso, lab = laboratorio, closed = cerrado, maintenance = mantención, sorry = disculpe)"
YAWN = "Artículo de revista: «Why do we yawn? Scientists still do not know exactly. Some think yawning helps us wake up, and others think it cools the brain.» (yawn = bostezar, scientists = científicos, wake up = despertar, cools = enfría, brain = cerebro)"
REVIEW = "Reseña: «The cafeteria's new menu is varied and cheap. However, the lines are long. I give it four stars out of five.» (review = reseña, cafeteria = casino, varied = variado, cheap = barato, lines = filas, stars = estrellas)"
FAIR = "Página web: «School Fair | Home | Schedule | Contact. Join us on Saturday! Games, food and music. Entry is free.» (fair = feria, schedule = programa, games = juegos, entry = entrada, free = gratis)"

lesson(
    OA, 1, MAT,
    "Aprenderé a reconocer el formato, el propósito y el contexto de textos impresos y digitales, como correos, avisos, páginas web, artículos y reseñas. Sirve para saber qué esperar de un texto antes de leerlo en detalle.",
    ["Sé leer textos cortos en inglés con ayuda.", "Conozco palabras como subject, notice y review."],
    [
        "Los textos tienen formatos (formats) con rasgos propios. Un correo (email) tiene asunto (Subject), saludo (Dear / Hi), cuerpo y despedida (Best regards). Un aviso (notice) da información breve y urgente, en mayúsculas o con un título. Una página web (web page) tiene menús como Home, Courses o Contact, y botones o enlaces. Un artículo de revista (magazine article) informa o explica con una pregunta inicial. Una reseña (review) da una opinión con una evaluación.",
        "El propósito (purpose) es lo que quiere lograr el texto: informar (a notice), invitar o convencer (a web page that says Sign up), explicar (an article) o evaluar (a review). El contexto (context) es quién escribe, a quién y dónde se publica: un correo de una secretaria a los apoderados, un aviso en la pared del colegio, una reseña en una página de opiniones. Los dos primeros datos que debes buscar son quién escribe y para qué.",
        "Para identificar el formato mira primero la forma: títulos, menús, saludos, estrellas. Después lee la primera línea. Si ves Dear... y Best regards, es una carta o correo. Si ves Sign up o Join us, el texto quiere que hagas algo. No necesitas entender todas las palabras para decidir el formato y el propósito: las pistas visuales y las frases fijas bastan.",
    ],
    [("email", "correo electrónico"), ("notice", "aviso"), ("web page", "página web"), ("magazine article", "artículo de revista"), ("review", "reseña: opinión con evaluación"), ("purpose", "propósito: para qué se escribe")],
    [
        ("Reconocer un correo", U(W_MAIL) + " ¿Qué formato es y cuál es su propósito?", ["Tiene asunto, saludo y firma: es un correo.", "Avisa un cambio de día y hora de un entrenamiento.", "Su propósito es informar."], "Es un correo; su propósito es informar un cambio de entrenamiento"),
        ("Reconocer una página web", U(W_WEB) + " ¿Qué pistas muestran que es una página web y qué busca?", ["Tiene menús: Home, Courses, Contact.", "Dice Sign up y habla de un descuento.", "Busca que alguien se inscriba."], "Es una página web; busca que la persona se inscriba al curso"),
    ],
    [
        ("Decidir el formato solo por el tema.", "Se mira de qué trata y no cómo se presenta el texto.", "Mira primero títulos, menús, saludos y despedidas."),
        ("Creer que una reseña informa sin opinar.", "Se confunde con una noticia.", "Busca una evaluación, como estrellas o palabras como good o bad."),
    ],
    [
        (U(SECRE) + " ¿Qué formato es? A) un correo B) un aviso de pared", "A) un correo", "Tiene asunto, saludo y despedida."),
        (U(LAB) + " ¿Qué formato es? A) un aviso B) una reseña", "A) un aviso", "Entrega una información breve y urgente."),
        (U(REVIEW) + " ¿Qué formato es? A) una reseña B) un artículo científico", "A) una reseña", "Tiene una evaluación con estrellas."),
    ],
    [
        (U(SECRE) + " ¿Cuál es el propósito? A) informar un cambio de uniforme B) invitar a una fiesta", "A) informar un cambio de uniforme", "Dice que los miércoles se puede usar el buzo."),
        (U(YAWN) + " ¿Cuál es el propósito? A) explicar un tema sin una respuesta única B) vender un producto", "A) explicar un tema sin una respuesta única", "Dice que los científicos no saben con exactitud."),
        (U(FAIR) + " ¿Cuál es el propósito? A) invitar a una feria escolar B) pedir dinero para un viaje", "A) invitar a una feria escolar", "Dice Join us y que la entrada es gratis."),
    ],
    [
        (U(LAB) + " ¿Dónde esperarías leer este texto? A) en un pizarrón o puerta del colegio B) en un libro de cuentos", "A) en un pizarrón o puerta del colegio", "Es un aviso de uso público."),
        (U(REVIEW) + " ¿Quién escribe y para quién? A) una persona que probó el casino, para otros estudiantes B) la directora, para los apoderados", "A) una persona que probó el casino, para otros estudiantes", "Da su opinión con I give it four stars."),
        ("Un texto tiene un menú Home | Courses | Contact y un botón Sign up. ¿Dónde se publica? A) en internet B) en un periódico impreso", "A) en internet", "Los menús y enlaces son propios de las páginas web."),
    ],
    [
        (U(YAWN) + " Un compañero dice que es un aviso. ¿Qué pista lo contradice? A) empieza con una pregunta y explica un tema B) usa mayúsculas y habla de un cierre", "A) empieza con una pregunta y explica un tema", "Un artículo explica; un aviso informa algo urgente."),
        (U(REVIEW) + " Un compañero dice que solo informa que hay un menú. ¿Qué pista muestra que hay opinión? A) I give it four stars out of five B) The cafeteria's new menu", "A) I give it four stars out of five", "Las estrellas son una evaluación personal."),
    ],
    [
        (U(FAIR) + " ¿Qué dato de la página web invita a participar sin pagar? A) Entry is free B) Games, food and music", "A) Entry is free", "Dice que la entrada es gratis."),
        (U(SECRE) + " ¿Hasta cuándo dura el cambio de buzo? A) todo el semestre B) solo un miércoles", "A) todo el semestre", "Dice for the whole term."),
    ],
    [("Recibes en tu correo: «Subject: Library books. Dear students, please return your books before Friday. Thank you. Mrs Soto, librarian.» (return = devuelvan, librarian = bibliotecaria). ¿Cuál es el propósito? A) pedir que se devuelvan los libros B) invitar a una charla", "A) pedir que se devuelvan los libros", "Dice please return your books before Friday.")],
    [
        ("En Inglés de 1.º medio (OA 9, clase 1): ¿qué rasgos tiene un correo?", "Asunto, saludo, cuerpo y despedida", "Son sus partes."),
        ("En Inglés de 1.º medio (OA 9, clase 1): ¿qué es una reseña?", "Un texto que da una opinión con una evaluación", "Por ejemplo, estrellas."),
        ("En Inglés de 1.º medio (OA 9, clase 1): ¿qué datos buscas primero en un texto?", "Quién escribe y para qué", "Definen el contexto y el propósito."),
    ],
    task("Lee este texto: «Subject: Science fair. Hi everyone, the science fair is on Tuesday in the library. Please bring your project at eight. Prizes for the best three. Mr Díaz» (science fair = feria de ciencias, prizes = premios). Escribe en español el formato, el propósito y dos pistas visuales o de lenguaje que lo muestran.", "Es un correo. Su propósito es informar sobre la feria de ciencias y pedir que lleven el proyecto. Pistas: Subject, Hi everyone y la firma Mr Díaz; la frase Please bring your project.", ["identifica el formato", "explica el propósito", "cita dos pistas del texto"], ["hoja con tres respuestas", "revisión con la clave"], ["decir que es un aviso sin justificar", "no citar ninguna pista"], "Reconoce lo acertado y, si no citó pistas, pide que busque el saludo y la firma."),
    "Recorta o copia en tu cuaderno tres textos cortos de tu casa y escribe de qué formato son.",
    "Busca tres tipos de textos en un sitio web (menú, noticia, aviso) y escribe qué propósito tiene cada uno.",
)

# ------------------------------------------------------------------ clase 2: información precisa
W_SHOP = "«Backpack Trek: price 18,990 pesos, weight 700 g, colours: blue, green and black. Free delivery on orders over 25,000 pesos.» (price = precio, weight = peso, colours = colores, free delivery = despacho gratis, orders = compras)"
SCHED = "Programa de talleres (de ejemplo): «Monday 4:00 pm – Drawing, Room 2. Tuesday 4:30 pm – Chess, Library. Wednesday 4:00 pm – Robotics, Lab. Friday 5:00 pm – Theatre, Gym. All workshops are free. Registration closes on March 3.» (workshops = talleres, room = sala, registration = inscripción, closes = cierra)"
LANE = "Noticia: «On 12 June, Mayor Soto opened the new footbridge over the river. The bridge is 120 metres long and has 15 benches. Walkers can use it every day from six in the morning to ten at night.» (mayor = alcalde, footbridge = pasarela, river = río, metres = metros, benches = bancas, walkers = peatones)"
CAMP = "Página web: «Summer Camp 2026 (de ejemplo). Ages 12–15. Dates: 5–14 January. Price: 85,000 pesos for ten days. Includes meals and a T-shirt. Activities: kayaking, hiking and board games. Apply before 20 December.» (camp = campamento, ages = edades, dates = fechas, includes = incluye, meals = comidas, kayaking = kayak, hiking = senderismo, apply = postula)"

lesson(
    OA, 2, MAT,
    "Aprenderé a ubicar información precisa en un texto: nombres, fechas, cantidades, horarios y condiciones. Sirve para responder con exactitud sin leer todo con la misma atención.",
    ["Sé reconocer el formato y el propósito de un texto.", "Conozco números, días y meses en inglés."],
    [
        "La información explícita (explicit information) está dicha con claridad en el texto. Para encontrarla usa la lectura de búsqueda (scanning): lee la pregunta, decide qué palabra o número buscas y recorre el texto solo para ese dato. Fíjate en los números, las fechas, los nombres propios en mayúscula, las horas y las palabras de la pregunta (when, how much, how many, where, who).",
        "Los textos digitales y las tablas ordenan los datos: el programa de talleres tiene día, hora, actividad y lugar. Lee en línea: sigue la fila de la actividad que buscas. En un precio, cuida el separador: en inglés 18,990 se lee como dieciocho mil novecientos noventa; en español se escribe 18.990. Las condiciones usan palabras como before (antes de), over (más de), free (gratis), includes (incluye).",
        "Antes de responder, comprueba que el dato corresponde exactamente a la pregunta: no es lo mismo la fecha en que empieza que la fecha en que cierra la inscripción. Subraya la respuesta en el texto. Si una pregunta pide un cálculo, primero ubica los datos y luego calcula. Evita responder con lo primero que veas.",
    ],
    [("scanning", "lectura de búsqueda de un dato"), ("price / weight", "precio / peso"), ("dates", "fechas"), ("includes", "incluye"), ("free", "gratis"), ("before", "antes de")],
    [
        ("Ubicar un dato en una tabla", SCHED + " ¿Qué día es el taller de robótica y dónde?", ["Busco Robotics en el programa.", "La fila dice Wednesday 4:00 pm – Robotics, Lab.", "El día es miércoles y el lugar, el laboratorio."], "Miércoles, en el laboratorio"),
        ("Ubicar una condición", W_SHOP + " ¿Desde qué monto el despacho es gratis?", ["Busco free delivery.", "Dice on orders over 25,000 pesos.", "Over significa más de."], "Desde compras de más de 25.000 pesos"),
    ],
    [
        ("Responder con el primer número que se ve.", "No se relaciona el número con la pregunta.", "Lee la pregunta y busca la palabra exacta."),
        ("Confundir la fecha de inicio con la de cierre de inscripción.", "Hay varias fechas parecidas en el texto.", "Mira la palabra que acompaña a la fecha, como closes o starts."),
    ],
    [
        (SCHED + " ¿Qué taller es el martes? A) ajedrez B) dibujo", "A) ajedrez", "Dice Tuesday 4:30 pm – Chess."),
        (LANE + " ¿Cuánto mide la pasarela? A) 120 metros B) 15 metros", "A) 120 metros", "Dice 120 metres long; 15 es el número de bancas."),
        (CAMP + " ¿Para qué edades es el campamento? A) de 12 a 15 años B) de 10 a 12 años", "A) de 12 a 15 años", "Dice Ages 12–15."),
    ],
    [
        (SCHED + " ¿Hasta qué fecha se puede inscribir? A) hasta el 3 de marzo B) hasta el 5 de enero", "A) hasta el 3 de marzo", "Dice Registration closes on March 3."),
        (LANE + " ¿Cuántas bancas tiene? A) 15 B) 120", "A) 15", "Dice has 15 benches."),
        (CAMP + " ¿Qué incluye el precio? A) comidas y una polera B) pasajes de avión", "A) comidas y una polera", "Dice Includes meals and a T-shirt."),
    ],
    [
        arith(W_SHOP + " Si compras dos mochilas, ¿cuántos pesos pagas?", "2*18990", "Cada mochila cuesta 18.990 pesos.", " pesos"),
        arith(CAMP + " Si se inscriben tres amigos, ¿cuántos pesos cuesta en total?", "3*85000", "Cada uno paga 85.000 pesos.", " pesos"),
        (LANE + " ¿A qué horas se puede usar la pasarela? A) de seis de la mañana a diez de la noche B) las 24 horas", "A) de seis de la mañana a diez de la noche", "Dice from six in the morning to ten at night."),
    ],
    [
        (SCHED + " Un compañero dice que el teatro es en la biblioteca. ¿Es correcto? A) no: el teatro es el viernes en el gimnasio B) sí: el teatro es en la biblioteca", "A) no: el teatro es el viernes en el gimnasio", "La biblioteca es del ajedrez."),
        (CAMP + " Un compañero dice que el campamento dura un mes. ¿Qué dato lo corrige? A) 5–14 January y ten days B) Apply before 20 December", "A) 5–14 January y ten days", "El texto dice diez días."),
    ],
    [
        (SCHED + " ¿Cuántos minutos más tarde empieza el teatro que el ajedrez?", "30 minutos", "El ajedrez es a las 4:30 y el teatro a las 5:00: pasa media hora, es decir, treinta minutos."),
        (W_SHOP + " ¿Cuántos colores tiene la mochila? A) tres B) dos", "A) tres", "Hay blue, green y black."),
    ],
    [(LANE + " Quieres cruzar la pasarela a las 11 de la noche. ¿Se puede? A) no: cierra a las diez de la noche B) sí: abre las 24 horas", "A) no: cierra a las diez de la noche", "El horario termina a las diez de la noche.")],
    [
        ("En Inglés de 1.º medio (OA 9, clase 2): ¿qué es la lectura de búsqueda (scanning)?", "Leer solo para encontrar un dato concreto", "Se busca una palabra o número."),
        ("En Inglés de 1.º medio (OA 9, clase 2): ¿qué significa over 25,000 pesos?", "Más de 25.000 pesos", "Over indica más de."),
        ("En Inglés de 1.º medio (OA 9, clase 2): ¿qué palabras de la pregunta ayudan a buscar un dato?", "When, how much, how many, where y who", "Indican el tipo de dato."),
    ],
    task("Lee este texto: «Library hours (de ejemplo): Monday to Thursday 9:00 am – 6:00 pm. Friday 9:00 am – 2:00 pm. Closed on Saturday and Sunday. Students can borrow up to three books for ten days.» (hours = horarios, closed = cerrado, borrow = pedir prestado, up to = hasta). Responde en español: ¿a qué hora cierra el viernes?, ¿cuántos libros se pueden pedir? y ¿por cuántos días?", "Cierra a las 2:00 pm el viernes. Se pueden pedir hasta tres libros por diez días.", ["encuentra las tres respuestas exactas", "no confunde el horario del viernes con el de lunes a jueves", "usa números correctos"], ["hoja con tres respuestas", "revisión con el texto"], ["decir que cierra a las 6:00 pm", "confundir libros con días"], "Reconoce los datos bien ubicados y pide subrayar la palabra del texto que lo respalda."),
    "Subraya en un texto de esta clase cada número, fecha y nombre propio.",
    "Busca un horario o una lista de precios real y escribe tres preguntas con respuesta directa.",
)

# ------------------------------------------------------------------ clase 3: estrategias de lectura
W_RING = "Texto: «Recycling is important. People recycle paper, glass and plastic. Information about recycling points is on the city website.» (recycling = reciclaje, glass = vidrio, plastic = plástico)"
SOCCER = "Texto: «Chile's national football team will play two matches next month. The first match is at home and the second is in Lima. The coach says the players are ready.» (national team = selección, matches = partidos, coach = entrenador, ready = listos)"
MUSEUM = "Texto: «The village exhibition shows how people lived long ago. Visitors can touch some objects and listen to stories from guides. Children under six enter free.» (exhibition = exposición, long ago = hace mucho tiempo, objects = objetos, guides = guías, enter = entran)"
FORUM = "Foro digital: «Menu | Search | Log in. Topic: Best apps for learning English? Reply from Tina: I use a vocabulary app and a podcast. It is a practical way to practise every day. Read more.» (log in = iniciar sesión, search = buscar, reply = respuesta, podcast = podcast, practical = práctico, practise = practicar, read more = leer más)"
FRIENDS = "Texto: «My cousin is very sensible. He always thinks before he acts. Actually, he is going to study in a library, not in a bookshop.» (cousin = primo, acts = actúa, bookshop = librería)"

lesson(
    OA, 3, MAT,
    "Aprenderé estrategias para leer mejor: hojear el texto (skimming), buscar datos (scanning), inferir palabras desconocidas por el contexto y usar cognados, imágenes y elementos digitales. Sirve para entender textos aunque no conozca todas las palabras.",
    ["Sé reconocer formato, propósito y datos.", "Conozco algunos cognados, como important e information."],
    [
        "Hojear (skimming) significa leer rápido para captar la idea general: lees el título, los subtítulos y la primera frase de cada párrafo. Buscar (scanning) significa recorrer el texto para encontrar un dato concreto. Usa skimming para saber de qué trata y scanning para responder preguntas específicas. En una página web los elementos digitales ayudan: menús (Menu), buscador (Search), enlaces (Read more) e íconos.",
        "Cuando no conoces una palabra, no te detengas. Mira la palabra de alrededor y su tipo (¿es un verbo, un lugar, un adjetivo?). Los cognados (cognates) son palabras que se parecen al español: important (importante), information (información), recycling (reciclaje), exhibition (exposición), practical (práctico). Pero hay falsos amigos (false friends): library es biblioteca, no librería; actually es en realidad, no actualmente; sensible es sensato; carpet es alfombra, no carpeta.",
        "Para decidir el sentido, prueba: ¿qué significa si lo reemplazo por una palabra que entiendo? ¿encaja con el resto de la frase? Si sigue sin entenderse, anótala, termina el párrafo y vuelve. Las imágenes, los títulos y las listas también dan pistas. Termina siempre con una frase en español que resuma la idea general.",
    ],
    [("skimming", "hojear: leer rápido la idea general"), ("scanning", "buscar un dato concreto"), ("cognate", "cognado: palabra parecida al español"), ("false friend", "falso amigo"), ("context", "contexto: lo que rodea a la palabra"), ("link", "enlace")],
    [
        ("Hojear para la idea general", W_RING + " Hojea el texto y di en español de qué trata.", ["Leo el título y la primera frase.", "El tema es el reciclaje.", "Menciona qué se recicla y dónde buscar información."], "Trata del reciclaje y de dónde encontrar información"),
        ("Inferir una palabra por el contexto", "En «Visitors can touch some objects and listen to stories from guides», ¿qué es guides? A) personas que acompañan y cuentan historias B) objetos de la exposición", ["Veo qué hacen los visitantes: tocan y escuchan.", "Quien cuenta historias es una persona.", "Guides son personas que acompañan."], "A) personas que acompañan y cuentan historias"),
    ],
    [
        ("Traducir library como librería.", "Se confunde un falso amigo por su parecido.", "Library es biblioteca; librería se dice bookshop."),
        ("Leer todo palabra por palabra aunque se busque un dato.", "No se elige entre skimming y scanning.", "Define si necesitas la idea general o un dato."),
    ],
    [
        ("Quieres saber rápido de qué trata un texto. ¿Qué haces? A) hojearlo (skimming) B) buscar solo un número", "A) hojearlo (skimming)", "Skimming da la idea general."),
        ("Quieres saber a qué hora abre una biblioteca. ¿Qué haces? A) buscar el dato (scanning) B) leer palabra por palabra", "A) buscar el dato (scanning)", "Scanning encuentra datos concretos."),
        ("¿Qué palabra de estas es un cognado? A) information B) although", "A) information", "Information se parece a información."),
    ],
    [
        (FRIENDS + " ¿Cómo es el primo? A) sensato B) sensible emocionalmente", "A) sensato", "Sensible es un falso amigo: significa sensato."),
        (FRIENDS + " ¿Dónde va a estudiar? A) en una biblioteca B) en una librería", "A) en una biblioteca", "Library es biblioteca; bookshop es librería."),
        (MUSEUM + " ¿Quiénes entran gratis? A) los niños menores de seis años B) los adultos mayores", "A) los niños menores de seis años", "Dice Children under six enter free."),
    ],
    [
        (SOCCER + " ¿Cuál es la idea general? A) la selección jugará dos partidos el próximo mes B) la selección ganó un campeonato", "A) la selección jugará dos partidos el próximo mes", "Dice will play two matches next month."),
        (FORUM + " ¿Qué elementos digitales aparecen? A) un menú, un buscador y un enlace Read more B) una tabla de precios", "A) un menú, un buscador y un enlace Read more", "Aparecen Menu, Search y Read more."),
        (MUSEUM + " ¿Qué significa exhibition por cognado? A) exposición B) exhibición de comida", "A) exposición", "Se parece a exposición y el contexto confirma que es una muestra."),
    ],
    [
        ("En «I actually like this song», ¿qué significa actually? A) en realidad, de hecho B) actualmente", "A) en realidad, de hecho", "Es un falso amigo: se parece a actualmente, pero significa en realidad."),
        ("En un texto no entiendes la palabra bookshop, pero ves «he is going to study in a library, not in a bookshop». ¿Qué te dice el contexto? A) es un lugar distinto de una biblioteca B) es lo mismo que library", "A) es un lugar distinto de una biblioteca", "Not in a bookshop los separa."),
    ],
    [
        ("Un texto tiene el título «How bees help plants». Haces skimming. ¿Qué esperas leer? A) cómo las abejas ayudan a las plantas B) por qué las abejas pican a las personas", "A) cómo las abejas ayudan a las plantas", "El título anticipa el tema."),
        (FORUM + " ¿Qué recomienda Tina? A) una aplicación de vocabulario y un podcast B) tomar clases presenciales", "A) una aplicación de vocabulario y un podcast", "Dice I use a vocabulary app and a podcast."),
    ],
    [("En una página web para aprender inglés ves los enlaces «Login», «Courses» y «Read more». ¿Para qué sirve Read more? A) para ver más información sobre una noticia o curso B) para cerrar la página", "A) para ver más información sobre una noticia o curso", "Es un enlace que abre más texto.")],
    [
        ("En Inglés de 1.º medio (OA 9, clase 3): ¿qué es el skimming?", "Leer rápido para captar la idea general", "Se mira el título y la primera frase."),
        ("En Inglés de 1.º medio (OA 9, clase 3): ¿qué es un falso amigo?", "Una palabra que se parece al español pero significa otra cosa, como library", "Library no es librería."),
        ("En Inglés de 1.º medio (OA 9, clase 3): ¿cómo infieres una palabra desconocida?", "Con el contexto y el tipo de palabra", "Se prueba si encaja en la frase."),
    ],
    task("Lee: «The city park has a new playground for children. It was built with recycled materials. Before, the park was empty at weekends, but now many families visit it. Admission is free.» (playground = zona de juegos, built = construida, recycled materials = materiales reciclados, weekends = fines de semana, admission = entrada). Haz skimming y escribe la idea general en una frase. Luego haz scanning y anota quién puede entrar gratis o si se paga, y subraya un cognado.", "Idea general: el parque tiene una nueva zona de juegos y ahora lo visitan familias. Entrada: gratis (Admission is free). Cognado: recycled (reciclado).", ["resume la idea general", "responde el dato concreto", "identifica un cognado"], ["hoja con tres respuestas", "revisión con el texto"], ["responder con un dato en vez de la idea general", "no encontrar el dato de la entrada"], "Reconoce el uso de cada estrategia y pide que explique cuál usó para cada pregunta."),
    "Haz una lista de diez cognados y cinco falsos amigos con su significado.",
    "Elige una noticia en inglés y practica skimming por un minuto; escribe en español de qué trata.",
)

# ------------------------------------------------------------------ clase 4: dos textos con información repartida
W_TWO = "Correo: «Hi Sam, join me on Sunday for the beach clean-up! We start at nine.» Página web: «Beach Clean-up: meet at North Pier. Gloves and bags are provided. Bring water.» (beach clean-up = limpieza de playa, pier = muelle, provided = se entregan)"
MAIL = "Correo de Lola a Sam: «Hi Sam, I'm inviting you to my cousin's concert on Saturday. It starts at seven. See you there! Lola.» (inviting = invitando, concert = concierto, cousin = prima o primo)"
CONC = "Página web del concierto: «Spring Concert – Saturday – Town Hall, Park Street. Doors open at six. Tickets: 4,000 pesos each. Children under ten enter free.» (town hall = sala municipal, doors open = abren las puertas, tickets = entradas, each = cada una)"
POST = "Afiche: «Painting Contest for teenagers! Theme: My town. Bring your painting to the library before April 10.» (contest = concurso, painting = pintura, theme = tema, bring = lleva)"
TXT = "Mensaje de texto de Ben: «The painting contest has a prize: a set of art materials for the winner. Entry is free. The winner is announced on April 20.» (prize = premio, set = set, winner = ganador, entry = participación, announced = se anuncia)"

lesson(
    OA, 4, MAT,
    "Aprenderé a combinar la información de dos textos distintos, como un correo y una página web, para obtener un mensaje completo, y a decir qué dato falta o qué pregunta hacer. Sirve para decidir con todos los datos en la mano.",
    ["Sé ubicar datos precisos.", "Sé reconocer formato y propósito."],
    [
        "Muchas veces ningún texto tiene toda la información. Un correo invita a un concierto y dice el día y la hora, pero la dirección y el precio están en la página web. Para tener el mensaje completo, lee los dos textos y combina los datos. Haz una lista de lo que necesitas: qué, cuándo, dónde, cuánto cuesta y qué llevar.",
        "Anota al lado de cada dato de qué texto viene. Así evitas mezclar datos y detectas contradicciones. Si dos textos dicen cosas distintas, busca cuál es más específico o más reciente. Por ejemplo, la página oficial del concierto manda sobre un mensaje informal. Si un dato falta en ambos, formula una pregunta para obtenerlo, como What time does it finish?",
        "La combinación a veces exige un cálculo: si cada entrada cuesta 4,000 pesos y van dos personas, el total es 8,000 pesos. Cuida las condiciones: Children under ten enter free significa que los menores de diez años no pagan. Responde solo con lo que dicen los textos; si no lo dicen, indica que falta información.",
    ],
    [("combine", "combinar"), ("missing information", "información que falta"), ("each", "cada uno"), ("under ten", "menores de diez"), ("before April 10", "antes del 10 de abril"), ("provided", "entregado, incluido")],
    [
        ("Combinar dos textos", W_TWO + " ¿Qué día, a qué hora y dónde es la limpieza?", ["El correo dice domingo a las nueve.", "La página web dice dónde: North Pier.", "Junto: domingo, 9:00, en el muelle norte."], "El domingo a las 9:00 en el muelle norte"),
        ("Detectar lo que falta", W_TWO + " ¿Qué pregunta harías si quieres saber cuánto durará la limpieza?", ["Ninguno de los textos dice cuánto dura.", "Pregunto por la duración.", "How long will it take?"], "How long will it take?"),
    ],
    [
        ("Tomar un dato de un texto y suponer que el otro dice lo mismo.", "No se revisan los dos textos con atención.", "Anota de qué texto viene cada dato."),
        ("Inventar un dato que ninguno de los textos entrega.", "Se llena la falta con suposiciones.", "Si falta, dilo o formula una pregunta."),
    ],
    [
        (MAIL + " " + CONC + " ¿Dónde es el concierto? A) en la sala municipal de Park Street B) en la casa de Lola", "A) en la sala municipal de Park Street", "El correo no dice el lugar; la página dice Town Hall, Park Street."),
        (MAIL + " " + CONC + " ¿A qué hora empieza el concierto? A) a las siete B) a las seis", "A) a las siete", "Lola dice It starts at seven; las seis es la apertura de puertas."),
        (MAIL + " " + CONC + " ¿Cuánto cuesta cada entrada? A) 4.000 pesos B) 7.000 pesos", "A) 4.000 pesos", "La página dice Tickets: 4,000 pesos each."),
    ],
    [
        (POST + " " + TXT + " ¿Qué se debe llevar y adónde? A) una pintura a la biblioteca B) materiales de arte al colegio", "A) una pintura a la biblioteca", "El afiche dice Bring your painting to the library."),
        (POST + " " + TXT + " ¿Cuál es el premio? A) un set de materiales de arte B) dinero", "A) un set de materiales de arte", "El mensaje dice a set of art materials."),
        (POST + " " + TXT + " ¿Cuánto cuesta participar? A) nada B) 4.000 pesos", "A) nada", "El mensaje dice Entry is free."),
    ],
    [
        arith(MAIL + " " + CONC + " ¿Cuántos pesos pagan Lola y Sam juntos por sus entradas?", "2*4000", "Cada entrada cuesta 4.000 pesos y son dos personas.", " pesos"),
        (POST + " " + TXT + " ¿Hasta qué fecha se puede entregar la pintura y cuándo se anuncia el ganador? A) antes del 10 de abril y el 20 de abril B) antes del 20 de abril y el 10 de abril", "A) antes del 10 de abril y el 20 de abril", "Cada fecha viene de un texto distinto."),
        (MAIL + " " + CONC + " Un niño de nueve años va con Lola. ¿Cuánto paga? A) nada B) 4.000 pesos", "A) nada", "Children under ten enter free."),
    ],
    [
        (MAIL + " " + CONC + " Un compañero dice que el concierto empieza a las seis. ¿Qué respondes? A) a las seis solo abren las puertas; empieza a las siete B) tiene razón", "A) a las seis solo abren las puertas; empieza a las siete", "Se combinan los datos de ambos textos."),
        (POST + " " + TXT + " ¿Qué dato no entrega ninguno de los dos textos? A) el tema de la pintura B) cuántas personas participan", "B) cuántas personas participan", "El tema está en el afiche (My town); la cantidad de participantes no aparece."),
    ],
    [
        (POST + " " + TXT + " Si quieres saber en qué sala de la biblioteca se entrega la pintura, ¿qué pregunta harías? A) Which room in the library? B) What is the prize?", "A) Which room in the library?", "El dato falta en ambos textos."),
        (POST + " " + TXT + " Para participar, ¿qué dos condiciones debes cumplir según los textos? A) ser adolescente y entregar antes del 10 de abril B) pagar la participación y entregar el 20 de abril", "A) ser adolescente y entregar antes del 10 de abril", "Teenagers viene del afiche y la fecha, también."),
    ],
    [(MAIL + " " + CONC + " Sam quiere llegar cuando abren las puertas. ¿A qué hora debe llegar? A) a las seis B) a las siete", "A) a las seis", "La página dice Doors open at six.")],
    [
        ("En Inglés de 1.º medio (OA 9, clase 4): ¿qué haces si cada texto tiene una parte de la información?", "Combinas los datos de los dos y anotas de qué texto viene cada uno", "Así se completa el mensaje."),
        ("En Inglés de 1.º medio (OA 9, clase 4): ¿qué haces si falta un dato en ambos textos?", "Lo señalas o formulas una pregunta", "No inventas el dato."),
        ("En Inglés de 1.º medio (OA 9, clase 4): ¿qué significa Children under ten enter free?", "Los menores de diez años entran gratis", "Under indica menos de."),
    ],
    task("Lee dos textos. Mensaje de Ana: «Hi Luis, the book club meets on Thursday. Bring a book you like.» (book club = club de lectura). Página del colegio: «Book Club – Thursdays at 4:15 pm in Room 5. Everyone is welcome. Snacks are provided.» (welcome = bienvenidos, snacks = colaciones). Escribe en español el mensaje completo y una pregunta en inglés para un dato que falte (por ejemplo, la duración).", "El club de lectura es los jueves a las 4:15 en la sala 5. Hay que llevar un libro favorito, todos son bienvenidos y hay colaciones. Pregunta: How long is the meeting?", ["combina los datos de ambos textos", "no inventa datos", "formula una pregunta en inglés para un dato que falta"], ["hoja con el mensaje y la pregunta", "revisión con los textos"], ["omitir el lugar o la hora", "inventar la duración"], "Reconoce los datos reunidos y pide aclarar de qué texto salió cada uno."),
    "Elige dos textos que tengas a mano (por ejemplo, un afiche y un mensaje) y anota qué dato aporta cada uno.",
    "Crea tu propio par de textos de tres líneas cada uno, con información repartida, y pide a alguien que los combine.",
)

# ------------------------------------------------------------------ clase 5: lectura independiente de temas menos conocidos
TOOLS = "Artículo: «Tool libraries: how do they work? In some towns, people can borrow a tool from a library, use it at home, and return it. First, you register at the front desk. Then you choose a tool from the catalogue. The first week is usually free, but longer loans cost a small fee. Although tool libraries are popular, some tools are often out on loan, so users must check the catalogue before they go.» (tool library = biblioteca de herramientas, borrow = pedir prestado, return = devolver, register = registrarse, front desk = recepción, catalogue = catálogo, loan = préstamo, fee = tarifa, out on loan = prestadas, users = usuarios)"
LIGHT = "Artículo: «Lighthouses help ships find their way at night. A strong light turns and sends beams across the sea. In the past, a keeper lived in the lighthouse and kept the light working. Today, most lighthouses are automatic, but some have a small exhibition that visitors can enter.» (lighthouses = faros, ships = barcos, beams = haces de luz, sea = mar, keeper = farero, automatic = automáticos, exhibition = exposición)"
SCHOOLTRIP = "Correo: «Subject: Trip to the science park. Dear parents, we will visit the science park on 14 June. The bus leaves at eight and returns at four. Please send lunch and a water bottle. The cost is six thousand pesos. Payment is due by 7 June. Ms Ríos.» (science park = parque científico, returns = regresa, lunch = almuerzo, water bottle = botella de agua, cost = costo, payment = pago, due by = hasta el)"

lesson(
    OA, 5, MAT,
    "Aprenderé a leer por mi cuenta textos impresos y digitales sobre temas menos conocidos: ideas generales, datos, propósito y opinión. Sirve para enfrentar textos nuevos con confianza.",
    ["Sé hojear, buscar datos y combinar textos.", "Conozco cognados y falsos amigos."],
    [
        "Una lectura independiente (independent reading) usa todas las estrategias en orden. Primero, mira el formato y el título y predice el tema. Segundo, haz skimming para captar la idea general. Tercero, haz scanning para ubicar los datos que piden las preguntas. Cuarto, usa el contexto y los cognados para las palabras nuevas. Quinto, resume en una frase.",
        "En textos de temas menos conocidos, como los faros o las bibliotecas de herramientas, puede haber palabras técnicas. No las busques todas: pregunta si son necesarias para responder. En muchas, la información clave viene después de conectores, como then, first o although. Cuida las ideas con contraste: Although tool libraries are popular, some tools are often out on loan indica que hay un problema.",
        "Al terminar, responde tres cosas: ¿De qué trata?, ¿Cuáles son los datos importantes? y ¿Qué opinas? Tu opinión necesita una razón del texto. Puedes decir In my opinion, a tool library is useful because... Revisa tus respuestas con el texto: si no puedes señalar la frase que las apoya, vuelve a leer.",
    ],
    [("independent reading", "lectura independiente"), ("topic", "tema"), ("detail", "detalle"), ("because", "porque"), ("leaves / returns", "sale / regresa"), ("due by", "plazo hasta")],
    [
        ("Idea general", TOOLS + " ¿De qué trata el texto?", ["El título pregunta cómo funcionan las bibliotecas de herramientas.", "Explica los pasos para usarlas.", "Agrega un problema: herramientas prestadas."], "De cómo funcionan las bibliotecas de herramientas y qué problema pueden tener"),
        ("Ubicar un dato", LIGHT + " ¿Qué hacía el farero en el pasado?", ["Busco keeper.", "Dice a keeper lived in the lighthouse and kept the light working.", "El farero mantenía la luz funcionando."], "Vivía en el faro y mantenía la luz funcionando"),
    ],
    [
        ("Querer entender cada palabra antes de responder.", "Se cree que sin todas las palabras no se entiende el texto.", "Busca la idea general y los datos que pide la pregunta."),
        ("Dar una opinión sin apoyarla en el texto.", "Se olvida la razón.", "Agrega because y una idea del texto."),
    ],
    [
        (TOOLS + " ¿Qué se hace primero? A) registrarse en la recepción B) elegir una herramienta del catálogo", "A) registrarse en la recepción", "Dice First, you register."),
        (LIGHT + " ¿Para qué sirven los faros? A) para ayudar a los barcos a encontrar su camino de noche B) para producir electricidad", "A) para ayudar a los barcos a encontrar su camino de noche", "Dice help ships find their way at night."),
        (SCHOOLTRIP + " ¿Cuándo es la salida? A) el 14 de junio B) el 7 de junio", "A) el 14 de junio", "El 7 de junio es el plazo de pago."),
    ],
    [
        (TOOLS + " ¿Qué problema se menciona? A) algunas herramientas suelen estar prestadas B) las herramientas son muy caras", "A) algunas herramientas suelen estar prestadas", "Dice some tools are often out on loan."),
        (LIGHT + " ¿Cómo son hoy la mayoría de los faros? A) automáticos B) con un farero siempre", "A) automáticos", "Dice most lighthouses are automatic."),
        (SCHOOLTRIP + " ¿A qué hora regresa el bus? A) a las cuatro B) a las ocho", "A) a las cuatro", "Dice returns at four; a las ocho sale."),
    ],
    [
        (TOOLS + " ¿Qué debe hacer el usuario antes de ir? A) revisar el catálogo para ver qué herramientas hay disponibles B) pagar un año completo", "A) revisar el catálogo para ver qué herramientas hay disponibles", "Dice users must check the catalogue before they go."),
        (SCHOOLTRIP + " ¿Qué deben enviar las familias? A) almuerzo y una botella de agua B) dinero en efectivo y celular", "A) almuerzo y una botella de agua", "Dice Please send lunch and a water bottle."),
        (LIGHT + " ¿Qué pueden hacer hoy los visitantes en algunos faros? A) entrar a una pequeña exposición B) encender la luz del faro", "A) entrar a una pequeña exposición", "Dice some have a small exhibition that visitors can enter."),
    ],
    [
        (TOOLS + " Un compañero dice que el texto critica las bibliotecas de herramientas. ¿Qué respondes? A) no: menciona un problema, pero dice que son populares B) sí: dice que nadie las usa", "A) no: menciona un problema, pero dice que son populares", "Although marca un contraste, no una crítica total."),
        (LIGHT + " ¿Qué cambio cuenta el texto entre el pasado y hoy? A) antes vivía un farero y hoy son automáticos B) antes eran automáticos y hoy tienen farero", "A) antes vivía un farero y hoy son automáticos", "In the past y Today marcan el contraste."),
    ],
    [
        arith(SCHOOLTRIP + " El pago vence el 7 de junio y la salida es el 14. ¿Cuántos días antes de la salida vence el pago?", "14-7", "Se restan las fechas del mismo mes.", " días"),
        arith(SCHOOLTRIP + " Si van 3 estudiantes de una misma familia, ¿cuántos pesos pagan en total?", "3*6000", "Cada uno cuesta 6.000 pesos.", " pesos"),
    ],
    [(TOOLS + " ¿Cuál es el mejor resumen? A) una biblioteca de herramientas permite pedir una herramienta prestada y devolverla, aunque algunas suelen estar prestadas B) las herramientas se compran en una web", "A) una biblioteca de herramientas permite pedir una herramienta prestada y devolverla, aunque algunas suelen estar prestadas", "Reúne el proceso y el problema.")],
    [
        ("En Inglés de 1.º medio (OA 9, clase 5): ¿en qué orden se aplican las estrategias de lectura?", "Formato y título, skimming, scanning, contexto y resumen", "Va de lo general a lo específico."),
        ("En Inglés de 1.º medio (OA 9, clase 5): ¿qué marca un contraste en un texto?", "Palabras como although y but", "Muestran una dificultad o una oposición."),
        ("En Inglés de 1.º medio (OA 9, clase 5): ¿cómo apoyas tu opinión sobre un texto?", "Con because y una idea del texto", "La opinión necesita evidencia."),
    ],
    task("Lee: «Many people think that cats are independent, but they also need attention. A cat sleeps up to sixteen hours a day. In the evening, it often plays. Experts say that daily play helps a cat stay healthy and calm.» (independent = independiente, attention = atención, up to = hasta, experts = expertos, healthy = sano, calm = tranquilo). Escribe en español: la idea general, dos datos y tu opinión con una razón del texto.", "Idea general: los gatos parecen independientes, pero necesitan atención. Datos: duermen hasta dieciséis horas al día; el juego diario los mantiene sanos y tranquilos. Opinión: creo que hay que jugar con los gatos porque los expertos dicen que los mantiene sanos.", ["resume la idea general", "anota dos datos del texto", "da una opinión con una razón del texto"], ["hoja con tres respuestas", "revisión con el texto"], ["opinión sin razón", "datos que no están en el texto"], "Reconoce lo logrado y pide subrayar la frase del texto que apoya la opinión."),
    "Elige un artículo corto en inglés, haz skimming y scanning, y resume la idea general en una frase.",
    "Busca un texto en inglés sobre un tema que no conozcas y anota tres palabras que adivinaste por el contexto.",
)
