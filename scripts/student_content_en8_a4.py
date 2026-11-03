"""Cuaderno del estudiante, 8.º básico Inglés (propuesta), EN08 OA 04 (lectura de textos literarios y no literarios).

Todos los textos para leer son originales y están escritos en cada ejercicio, con pista en español.
Las clases del plan tienen títulos genéricos; aquí cada clase trabaja un grupo de contenidos que nombra el OA.
Los datos de cuadros y gráficos son de ejemplo.
"""
from __future__ import annotations

from student_content_en8_a import lesson, task
from student_lessons import arith

OA4 = "EN08 OA 04"
READ = "Lee: "

# ---------------------------------------------------------------- clase 1: textos literarios
COMPASS = "«Nico lived in a small village by the sea. One morning, he lost his grandfather's compass on the beach. He looked under the rocks and in the sand, but he did not find it. He felt very sad. His friend Ana said: Let's draw a map and check one area at a time. After two hours, they found the compass near a red boat. Nico smiled and thanked Ana.» (compass = brújula, village = pueblo, rocks = rocas, sand = arena, area = zona, boat = bote, thanked = agradeció)"
RAINPOEM = "«Rain on the window, tap, tap, tap, / Grey clouds sleeping on the map. / Inside my room, a cup of tea, / The rain sings softly just for me.» (window = ventana, clouds = nubes, sleeping = durmiendo, cup of tea = taza de té, softly = suavemente)"
COMIC = "Tira cómica. Cuadro 1, Dani: «Oh no! My phone is dead!». Cuadro 2, su mamá: «You must charge it at night.». Cuadro 3, Dani: «From now on, I will charge it every evening.». (dead = sin batería, charge = cargar, from now on = de ahora en adelante, every evening = todas las tardes)"

lesson(
    OA4, 1,
    "Los textos literarios escritos en cada ejercicio (un cuento, un poema y una tira cómica) y lápiz.",
    "Aprenderé a leer cuentos, poemas y tiras cómicas e identificar el tema, los personajes, el entorno, la trama y el problema y su solución. Sirve para comprender historias en inglés y explicar de qué tratan.",
    ["Sé reconocer verbos en pasado simple como lived, lost y found.", "Conozco palabras como village, sea y beach."],
    [
        "Un texto literario (literary text) tiene un propósito artístico: contar, emocionar o hacer imaginar. Puede ser un cuento (story), un poema (poem) o una tira cómica (comic strip). Los personajes (characters) son quienes participan: Nico y Ana. El entorno (setting) es el lugar y el tiempo: un pueblo junto al mar, una mañana. La caracterización (characterization) muestra cómo es un personaje por lo que dice, hace o siente.",
        "La trama (plot) es lo que pasa en orden: inicio (beginning), desarrollo (middle) y final (end). El problema (problem) es lo que complica la historia: Nico perdió la brújula. La solución (solution) es cómo se resuelve: Ana propuso dibujar un mapa y revisar una zona a la vez. El tema (theme) es la idea general que deja el texto, como «pedir ayuda y trabajar juntos».",
        "Un poema se organiza en versos (lines) que suelen rimar. Su tema puede ser una emoción o una imagen, como un día de lluvia. Una tira cómica cuenta con cuadros: las palabras en globos son lo que dicen los personajes y las imágenes muestran la acción. Para leer bien, pregúntate: ¿quién?, ¿dónde?, ¿qué pasa?, ¿cómo se resuelve? y ¿qué idea deja?",
    ],
    [("character", "personaje"), ("setting", "entorno: lugar y tiempo"), ("plot", "trama: lo que pasa en orden"), ("problem", "problema de la historia"), ("solution", "solución"), ("theme", "tema: idea general del texto")],
    [
        ("Personajes y entorno", READ + COMPASS + " ¿Quiénes son los personajes y dónde ocurre la historia?", ["Busco los nombres: Nico y Ana.", "Busco el lugar: a small village by the sea y the beach.", "Junto los datos."], "Nico y Ana; en un pueblo junto al mar y en la playa"),
        ("Problema y solución", READ + COMPASS + " ¿Cuál es el problema y cómo se resuelve?", ["El problema: Nico perdió la brújula de su abuelo.", "La solución: Ana propuso dibujar un mapa y revisar una zona a la vez.", "Así la encontraron cerca de un bote rojo."], "Nico perdió la brújula; la encontraron al revisar una zona a la vez con un mapa"),
    ],
    [
        ("Decir que el tema es «una brújula roja».", "Se confunde un detalle con el tema.", "El tema es una idea general, como la ayuda de un amigo."),
        ("Confundir el entorno con los personajes.", "Se mezclan quién y dónde.", "El entorno es lugar y tiempo; los personajes son quienes participan."),
    ],
    [
        # rec
        (READ + COMPASS + " ¿Qué perdió Nico? a) la brújula de su abuelo b) su cuaderno", "a) la brújula de su abuelo", "El texto dice he lost his grandfather's compass."),
        (READ + COMPASS + " ¿Dónde la encontraron? a) cerca de un bote rojo b) debajo de una roca", "a) cerca de un bote rojo", "Dice they found the compass near a red boat."),
        (READ + RAINPOEM + " ¿De qué trata el poema? a) de un día de lluvia b) de un día de calor", "a) de un día de lluvia", "Habla de rain, clouds y tea."),
    ],
    [
        # und
        (READ + COMPASS + " ¿Cuál es el tema del cuento? a) la ayuda de una amiga resuelve un problema b) los viajes en barco", "a) la ayuda de una amiga resuelve un problema", "Ana ayuda a Nico a resolver su problema."),
        (READ + RAINPOEM + " ¿Qué palabra rima con «tap»? a) map b) tea", "a) map", "Tap y map terminan con el mismo sonido."),
        (READ + COMIC + " ¿Cuál es el problema de Dani? a) su teléfono no tiene batería b) perdió su mochila", "a) su teléfono no tiene batería", "En el primer cuadro dice my phone is dead."),
    ],
    [
        # app
        (READ + COMIC + " ¿Qué decide hacer Dani al final? a) cargar el teléfono todas las tardes b) comprar otro teléfono", "a) cargar el teléfono todas las tardes", "En el cuadro 3 dice I will charge it every evening."),
        (READ + COMPASS + " ¿Cuánto tiempo pasó hasta que encontraron la brújula?", "Dos horas", "El texto dice After two hours."),
        (READ + RAINPOEM + " ¿Qué hace la lluvia en el último verso? a) canta suavemente b) rompe la ventana", "a) canta suavemente", "El verso dice The rain sings softly just for me."),
    ],
    [
        # rea
        (READ + COMPASS + " Nico se sintió muy triste al comienzo. ¿Qué frase del texto lo muestra? a) He felt very sad b) Nico smiled", "a) He felt very sad", "Esa oración nombra su sentimiento."),
        (READ + COMPASS + " ¿Cuál es la mejor secuencia de la trama? a) pierde la brújula, la busca, recibe una idea, la encuentra b) la encuentra, la pierde, se va", "a) pierde la brújula, la busca, recibe una idea, la encuentra", "Sigue inicio, desarrollo y final."),
    ],
    [
        # cha
        (READ + COMIC + " Una compañera dice que el tema de la tira es «la tecnología es mala». ¿Qué texto corrige su idea? a) Dani aprende a cargar su teléfono para no quedarse sin batería b) El teléfono está roto", "a) Dani aprende a cargar su teléfono para no quedarse sin batería", "El tema es un hábito responsable, no que la tecnología sea mala."),
        (READ + RAINPOEM + " ¿Qué sentimiento transmite el poema? Elige: a) calma b) enojo c) miedo", "a) calma", "Tea, softly y sleeping muestran una escena tranquila."),
    ],
    [
        # context
        (READ + "«Today the school bus was late. Sofía waited at the stop for twenty minutes. At last, her neighbor offered her a ride. Sofía was relieved and said: Thank you so much!» (bus stop = paradero, neighbor = vecino, offered = ofreció, ride = viaje, relieved = aliviada). ¿Cuál es el problema? a) el bus llegó tarde b) Sofía perdió su mochila", "a) el bus llegó tarde", "Dice the school bus was late.")
    ],
    [
        # selfcheck
        ("¿Qué es el entorno de un cuento?", "El lugar y el tiempo", "Es donde y cuándo ocurre la historia."),
        ("¿Qué es la trama?", "Lo que pasa en orden", "Incluye inicio, desarrollo y final."),
        ("¿Cómo se llaman las líneas de un poema?", "Versos", "En inglés, lines."),
    ],
    task("Lee este cuento breve: «Leo lost his school jacket at the park. He asked three people, but nobody saw it. Then his little sister said: Maybe it is under the bench. Leo looked there and found the jacket. He gave her a big hug.» (jacket = chaqueta, bench = banca, maybe = quizás, hug = abrazo). En tu hoja escribe: personajes, entorno, problema, solución y el tema.", "Personajes: Leo y su hermana. Entorno: el parque. Problema: Leo perdió su chaqueta. Solución: su hermana sugirió buscar bajo la banca y la encontró. Tema: la ayuda de la familia.", ["identifica personajes y entorno", "distingue problema y solución", "expresa un tema como idea general"], ["hoja con cinco respuestas", "nota del adulto"], ["decir que el tema es la banca", "confundir el problema con la solución"], "Reconoce lo que acertó y relee con la persona solo el comienzo y el final para separar problema y solución."),
    "Lee de nuevo el poema de la lluvia en voz alta y marca con color las palabras que riman.",
    "Escribe en español el tema de un cuento que conozcas y cuál es su problema y su solución.",
)

# ---------------------------------------------------------------- clase 2: textos no literarios
AD = "«SUNNY BIKES. Rent a bike for just 3.000 pesos per hour! Open every day from 9 a.m. to 6 p.m. Helmets included. Come and ride with us!» (rent = arrendar, per hour = por hora, open = abierto, helmets = cascos, included = incluidos, ride = pasear en bicicleta)"
EMAIL = "«From: Carla Soto. To: Mr. Díaz. Subject: Absence on Monday. Dear Mr. Díaz, I cannot come to school on Monday because I have a dentist appointment at 10 a.m. I will bring a note on Tuesday. Best regards, Carla Soto» (absence = ausencia, dentist = dentista, appointment = hora médica, note = justificativo, best regards = saludos cordiales)"
WEB = "«Youth Library. Opening hours: Monday to Friday, 10:00 to 18:00. Saturday: 10:00 to 14:00. Closed on Sunday. Workshop: Make your own comic, every Wednesday at 16:00. Entrance is free.» (youth = juvenil, opening hours = horario de atención, closed = cerrado, workshop = taller, entrance = entrada)"
GRAPH = "Gráfico de barras de ejemplo, «Books read by 8B». Marzo: 8 libros. Abril: 12 libros. Mayo: 15 libros. Junio: 10 libros. (books read = libros leídos)"

lesson(
    OA4, 2,
    "Los textos no literarios escritos en cada ejercicio (aviso, email, página web y gráfico) y lápiz.",
    "Aprenderé a leer avisos, emails, páginas web y gráficos e identificar su propósito, las ideas generales y la información específica. Sirve para entender textos de la vida real en inglés.",
    ["Sé las horas en inglés y los días de la semana.", "Conozco palabras como open, closed y free."],
    [
        "Un texto no literario (non-literary text) informa, instruye, convence o comunica algo de la vida real. Un aviso publicitario (advertisement) busca que compres o uses algo. Un email (electronic mail) es un mensaje escrito con destinatario (To), remitente (From) y asunto (Subject). Una página web (web page) entrega información con menús y horarios. Un gráfico (graph) muestra datos con barras o líneas.",
        "Para leer cada texto, identifica primero el propósito: ¿quiere vender, pedir algo, informar o mostrar datos? Luego busca la información específica con las preguntas who, what, when, where y how much. En un aviso, mira el precio, el horario y la oferta. En un email, mira para quién es, qué pide y cuándo. En una página web, busca los horarios y los menús. En un gráfico, lee el título y compara los valores.",
        "Las pistas están en el formato. Palabras como «Rent», «Come and» y los signos de exclamación sugieren un aviso que convence. «Dear…» y «Best regards» marcan un email. Los menús como Home o Contact y los horarios en la parte principal marcan una página web. Un título como «Books read by 8B» anuncia un gráfico.",
    ],
    [("advertisement", "aviso publicitario"), ("email", "correo electrónico"), ("web page", "página web"), ("graph", "gráfico"), ("subject", "asunto del email"), ("opening hours", "horario de atención")],
    [
        ("Propósito de un aviso", READ + AD + " ¿Cuál es el propósito del texto?", ["Veo el precio y la invitación Come and ride with us.", "El texto quiere que alguien arriende una bicicleta.", "Es un aviso publicitario."],  "Convencer para arrendar una bicicleta"),
        ("Dato específico en un email", READ + EMAIL + " ¿Por qué Carla no podrá ir el lunes?", ["Busco because.", "Dice because I have a dentist appointment at 10 a.m.", "Esa es la razón."], "Porque tiene una hora con el dentista a las 10"),
    ],
    [
        ("Leer solo el título y contestar sin revisar el texto.", "Se supone la respuesta.", "Busca el dato exacto en el texto antes de contestar."),
        ("Confundir remitente y destinatario en un email.", "No se distingue From de To.", "From es quien escribe y To es quien recibe."),
    ],
    [
        # rec
        (READ + AD + " ¿Cuánto cuesta arrendar una bicicleta por hora? a) 3.000 pesos b) 9.000 pesos", "a) 3.000 pesos", "El aviso dice 3.000 pesos per hour."),
        (READ + EMAIL + " ¿Quién escribe el email? a) Carla Soto b) Mr. Díaz", "a) Carla Soto", "El texto dice From: Carla Soto."),
        (READ + WEB + " ¿Qué día cierra la biblioteca? a) el domingo b) el sábado", "a) el domingo", "La página dice Closed on Sunday."),
    ],
    [
        # und
        (READ + WEB + " ¿Qué se hace en el taller? a) crear un cómic b) aprender a cocinar", "a) crear un cómic", "Dice Make your own comic."),
        (READ + GRAPH + " ¿En qué mes se leyeron más libros?", "Mayo", "El valor 15 es el más alto."),
        (READ + AD + " ¿Hasta qué hora está abierto? a) hasta las 6 p.m. b) hasta las 9 p.m.", "a) hasta las 6 p.m.", "El aviso dice from 9 a.m. to 6 p.m."),
    ],
    [
        # app
        arith(READ + GRAPH + " ¿Cuántos libros más se leyeron en mayo que en marzo?", "15-8", "Se restan los libros de marzo a los de mayo."),
        arith(READ + GRAPH + " ¿Cuántos libros se leyeron en total entre marzo y junio?", "8+12+15+10", "Se suman los cuatro meses."),
        (READ + EMAIL + " ¿Qué traerá Carla el martes? a) un justificativo b) un regalo", "a) un justificativo", "Dice I will bring a note on Tuesday."),
    ],
    [
        # rea
        (READ + WEB + " Un amigo quiere ir el sábado a las 16:00. ¿Podrá entrar? a) no, porque el sábado cierra a las 14:00 b) sí, porque abre todo el día", "a) no, porque el sábado cierra a las 14:00", "El horario del sábado es 10:00 a 14:00."),
        (READ + AD + " ¿Qué palabra del aviso invita a actuar? a) Come b) Helmets", "a) Come", "Come and ride with us es una invitación."),
    ],
    [
        # cha
        (READ + GRAPH + " Un compañero dice que en junio se leyeron más libros que en abril. ¿Qué dato del gráfico lo corrige? a) 10 libros en junio y 12 en abril b) 15 libros en mayo", "a) 10 libros en junio y 12 en abril", "En abril se leyeron más que en junio."),
        ("¿Qué texto de la lista es un email? Elige: a) «Dear Ms. Pino, thank you for your help. Best regards, Luis» b) «Rent a bike now!» c) «Monday to Friday, 9 to 5»", "a) «Dear Ms. Pino, thank you for your help. Best regards, Luis»", "Dear y Best regards son señales de un email."),
    ],
    [
        # context
        (READ + "«Lost: a blue backpack in the gym. Please call the school office or come to room 4. Reward: a chocolate bar.» (lost = perdida, office = oficina, reward = recompensa). ¿Qué se pide? a) que devuelvan una mochila azul b) que compren una mochila", "a) que devuelvan una mochila azul", "El aviso busca recuperar una mochila perdida.")
    ],
    [
        # selfcheck
        ("¿Para qué sirve un aviso publicitario?", "Para convencer de comprar o usar algo", "Es su propósito principal."),
        ("¿Qué parte de un email indica de qué trata?", "El asunto (subject)", "Resume el tema."),
        ("¿Qué muestra un gráfico de barras?", "Datos y su comparación", "Cada barra es un valor."),
    ],
    task("Lee este mensaje: «From: Pedro. To: Ms. Vera. Subject: Homework. Dear Ms. Vera, I am sorry, but I could not finish my science homework because I was sick on Thursday. May I bring it on Monday? Thank you, Pedro» (sorry = lo siento, finish = terminar, sick = enfermo, may I = ¿puedo?). En tu hoja escribe: quién escribe, a quién, el propósito, la razón y qué pide.", "Escribe Pedro a la Sra. Vera. Propósito: pedir más plazo. Razón: estuvo enfermo el jueves. Pide traer la tarea el lunes.", ["identifica remitente y destinatario", "expresa el propósito y la razón", "indica lo que pide"], ["hoja con cinco respuestas", "nota del adulto"], ["confundir From y To", "no decir qué pide"], "Reconoce lo que acertó y relee con la persona Subject, Dear y la última oración."),
    "Busca en tu casa un aviso o folleto en inglés o español y anota su propósito y dos datos específicos.",
    "Escribe en español un email corto a un profesor para pedir una prueba en otra fecha.",
)

# ---------------------------------------------------------------- clase 3: relaciones entre ideas
MATCH = "«Last Friday, the school match was moved to the gym because the field was wet. If the weather is good on Monday, the team will play outside. Many students think the gym is too small, but the coach says it is safer.» (moved = trasladado, field = cancha, wet = mojada, weather = clima, outside = afuera, safer = más seguro, coach = entrenador)"
TRIP = "«First, the class took the bus to the museum. Then the guide showed them an old map. Later, the students drew their own map in a notebook. Finally, they returned to school and shared their work.» (guide = guía, showed = mostró, drew = dibujaron, shared = compartieron)"
NEWS = "«The city will plant two hundred trees in the main avenue. The mayor said that shade will make the street cooler in summer. In my opinion, this is the best project of the year. The work will start on Monday and finish in November.» (plant = plantar, avenue = avenida, mayor = alcalde, shade = sombra, cooler = más fresca, start = comenzar, finish = terminar)"

lesson(
    OA4, 3,
    "Los textos escritos en cada ejercicio (un cuento breve, una noticia y un relato) y lápiz.",
    "Aprenderé a identificar en lo que leo la secuencia, la causa y el efecto, la condición y la diferencia entre hecho y opinión. Sirve para entender por qué pasan las cosas y qué está comprobado.",
    ["Sé because, so, if, first, then y finally.", "Conozco las expresiones I think e in my opinion."],
    [
        "Las ideas de un texto se relacionan de varias formas. La secuencia (sequence) indica el orden: first, then, later, finally. La causa (cause) y el efecto (effect) explican por qué algo ocurre: because presenta la causa y so presenta el efecto. La condición (condition) indica qué debe cumplirse: if + presente, will + verbo.",
        "En «The match was moved to the gym because the field was wet», la causa es que la cancha estaba mojada y el efecto es el cambio de lugar. En «If the weather is good, the team will play outside», la condición es el buen clima. Un hecho (fact) se puede comprobar y una opinión (opinion) expresa lo que alguien piensa: «I think», «in my opinion», «the best», «too small».",
        "Para encontrar cada relación, busca el conector y pregunta: ¿qué pasó?, ¿por qué?, ¿qué pasaría si…?, ¿se puede comprobar? Un texto de noticias suele mezclar hechos y opiniones; sepáralos antes de aceptar una idea. Una cifra o una fecha casi siempre es un hecho; un adjetivo de valoración casi siempre es una opinión.",
    ],
    [("sequence", "secuencia: el orden"), ("cause", "causa"), ("effect", "efecto"), ("condition", "condición"), ("fact", "hecho comprobable"), ("opinion", "opinión")],
    [
        ("Causa y efecto", READ + MATCH + " ¿Por qué se cambió el partido al gimnasio?", ["Busco because.", "Dice because the field was wet.", "La causa es que la cancha estaba mojada."], "Porque la cancha estaba mojada"),
        ("Hecho u opinión", READ + NEWS + " ¿La frase «In my opinion, this is the best project of the year» es un hecho o una opinión?", ["Veo In my opinion.", "También hay un adjetivo de valoración: the best.", "No se puede comprobar."], "Una opinión"),
    ],
    [
        ("Pensar que lo que dice un alcalde siempre es un hecho.", "Se confunde la fuente con la comprobación.", "Una frase es un hecho si se puede comprobar con datos; las valoraciones son opiniones."),
        ("Ignorar la condición y creer que el equipo jugará afuera siempre.", "No se lee el if.", "El equipo jugará afuera solo si el clima es bueno."),
    ],
    [
        # rec
        (READ + MATCH + " ¿Dónde se jugó el partido del viernes? a) en el gimnasio b) en la cancha", "a) en el gimnasio", "El texto dice the school match was moved to the gym."),
        (READ + NEWS + " ¿Cuántos árboles se plantarán?", "200", "El texto dice two hundred trees."),
        (READ + TRIP + " ¿Qué hicieron justo antes de dibujar su propio mapa? a) ver un mapa antiguo b) volver al colegio", "a) ver un mapa antiguo", "La guía mostró un mapa y luego los estudiantes dibujaron."),
    ],
    [
        # und
        (READ + MATCH + " ¿Qué condición debe cumplirse para que el equipo juegue afuera el lunes? a) que el clima sea bueno b) que el entrenador no esté", "a) que el clima sea bueno", "El texto dice If the weather is good on Monday."),
        (READ + NEWS + " ¿Cuál de estas frases es un hecho? a) The work will start on Monday b) This is the best project of the year", "a) The work will start on Monday", "Una fecha de inicio se puede comprobar."),
        (READ + TRIP + " ¿Qué palabra marca el último paso? a) Finally b) Later", "a) Finally", "Finally cierra la secuencia."),
    ],
    [
        # app
        (READ + NEWS + " ¿Por qué plantarán árboles, según el alcalde? a) para dar sombra y refrescar la calle b) para vender madera", "a) para dar sombra y refrescar la calle", "El alcalde dice that shade will make the street cooler."),
        (READ + MATCH + " ¿Qué opinan muchos estudiantes del gimnasio? a) que es muy pequeño b) que es muy grande", "a) que es muy pequeño", "El texto dice Many students think the gym is too small."),
        (READ + TRIP + " Ordena. A) The class drew a map. B) The class took the bus. C) The guide showed an old map. D) They shared their work.", "B, C, A, D", "Siguen first, then, later y finally."),
    ],
    [
        # rea
        (READ + MATCH + " El entrenador dice que el gimnasio es más seguro. ¿Es un hecho o una opinión? a) una opinión b) un hecho", "a) una opinión", "Más seguro es una valoración del entrenador."),
        (READ + NEWS + " ¿Cuál es el efecto de que haya sombra? a) la calle será más fresca en verano b) la calle será más ancha", "a) la calle será más fresca en verano", "La causa es la sombra y el efecto es una calle más fresca."),
    ],
    [
        # cha
        (READ + NEWS + " Escribe la frase del texto que es una opinión.", "In my opinion, this is the best project of the year", "Usa In my opinion y the best, que son señales de opinión."),
        (READ + MATCH + " Completa el efecto: «The field was wet, so the match was ___». Opciones: moved to the gym / played on the field.", "moved to the gym", "El texto dice que el partido se trasladó al gimnasio."),
    ],
    [
        # context
        (READ + "«Because the library is closing for repairs, students can borrow books until Friday. If a book is returned late, the student pays a fine. Many students say the new rule is unfair.» (closing for repairs = cerrando por reparaciones, returned = devuelto, fine = multa, unfair = injusta). ¿Cuál es una opinión? a) the new rule is unfair b) the library is closing for repairs", "a) the new rule is unfair", "Unfair es una valoración de los estudiantes.")
    ],
    [
        # selfcheck
        ("¿Qué conector presenta una causa?", "Because", "Se traduce porque."),
        ("¿Qué conector presenta un efecto?", "So", "Se traduce así que."),
        ("¿Cómo sabes que una frase es una opinión?", "Tiene I think, in my opinion o un adjetivo de valoración", "No se puede comprobar con un dato."),
    ],
    task("Lee este texto: «Last week, our school collected old clothes because many families needed warm jackets. If we collect two hundred jackets, the city will give us a prize. In my opinion, this is a very good idea.» (collected = recolectó, jackets = chaquetas, prize = premio). En tu hoja escribe: la causa, la condición, la meta y la frase que es una opinión.", "Causa: muchas familias necesitaban chaquetas. Condición: recolectar 200 chaquetas. Premio de la ciudad. Opinión: In my opinion, this is a very good idea.", ["identifica causa y condición", "indica la meta con la cifra", "señala la opinión"], ["hoja con cuatro respuestas", "nota del adulto"], ["confundir causa y condición", "poner una cifra distinta"], "Reconoce lo que acertó y relee con la persona because, if e in my opinion para separar cada relación."),
    "Lee de nuevo la noticia de los árboles y subraya con un color los hechos y con otro las opiniones.",
    "Escribe en español dos hechos y dos opiniones sobre tu comuna.",
)

# ---------------------------------------------------------------- clase 4: conectores, palabras clave y derivadas
MAYBE = "«Maybe it will rain tomorrow, so I will take an umbrella. I will wait here until the bus comes. Then I will go to school. The new teacher is taller than the old one, and she is also friendlier.» (maybe = quizás, umbrella = paraguas, wait = esperar, comes = llega, friendlier = más amable, old = antiguo)"
INVITATION = "«Our class decision is to organize a celebration for the end of the year. The invitation has information about the date and the collection of food. The competition will start at noon.» (decision = decisión, celebration = celebración, invitation = invitación, information = información, collection = colecta, competition = competencia)"

lesson(
    OA4, 4,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a reconocer palabras clave y de uso frecuente, los conectores so, then, until, also y maybe, y palabras derivadas con -er en comparaciones y terminación -ion. Sirve para entender mejor un texto y ampliar mi vocabulario.",
    ["Sé que because y so unen causa y efecto.", "Conozco adjetivos como tall, fast y old."],
    [
        "Los conectores (connectors) unen ideas. So indica el resultado (así que). Then indica el orden (luego). Until indica hasta cuándo ocurre algo (hasta que). Also suma una idea (además). Maybe indica posibilidad (quizás). En «Maybe it will rain, so I will take an umbrella», maybe presenta la posibilidad y so, la decisión. En «I will wait until the bus comes», until marca el límite de la espera.",
        "Las palabras derivadas se forman a partir de otras. Para comparar dos cosas, el adjetivo corto lleva -er y se usa than (que): tall → taller than, fast → faster than, old → older than. Si termina en -y, cambia a -ier: friendly → friendlier. Los sustantivos terminados en -ion suelen venir de un verbo: decide → decision, invite → invitation, collect → collection, inform → information, celebrate → celebration, compete → competition.",
        "Muchas palabras en -ion se parecen al español (-ción, -sión): information – información, decision – decisión. Son cognados (cognates) y facilitan la lectura. Cuidado con la ortografía: no siempre se escriben igual. Usa el contexto para comprobar el significado. Las palabras clave y las expresiones de uso frecuente, como every day o at last, aparecen mucho y te ayudan a entender más rápido.",
    ],
    [("connector", "conector: une ideas"), ("until", "hasta que"), ("maybe", "quizás"), ("comparative -er", "forma -er para comparar"), ("-ion", "terminación de sustantivos como information"), ("cognate", "cognado: palabra parecida al español")],
    [
        ("Elegir el conector", "Completa: «I will wait ___ the bus comes». Opciones: until / also.", ["La espera tiene un límite: la llegada del bus.", "Until significa hasta que.", "Until es el conector correcto."], "until"),
        ("Formar el comparativo", "Completa: «My brother is tall, but my father is ___ than him». Opciones: taller / more tall.", ["La frase compara a dos personas y aparece than.", "Tall es un adjetivo corto: se le agrega -er.", "La forma es taller."], "taller"),
    ],
    [
        ("Usar so cuando se quiere sumar una idea.", "Se confunde resultado con adición.", "Si sumas, usa also; si es resultado, usa so."),
        ("Escribir «more tall» en lugar de «taller».", "Se traduce palabra por palabra del español.", "Los adjetivos cortos llevan -er: taller than."),
    ],
    [
        # rec
        ("¿Qué significa «maybe»? a) quizás b) nunca", "a) quizás", "Maybe expresa posibilidad."),
        ("¿Qué comparativo corresponde a tall? a) taller b) more tall", "a) taller", "Taller se usa para comparar dos personas."),
        ("¿Qué sustantivo viene del verbo decide? a) decision b) decider", "a) decision", "Decide cambia a decision."),
    ],
    [
        # und
        (READ + MAYBE + " ¿Qué hará la persona si quizás llueve? a) llevar un paraguas b) quedarse en casa", "a) llevar un paraguas", "El texto dice so I will take an umbrella."),
        (READ + MAYBE + " ¿Hasta cuándo esperará? a) hasta que llegue el bus b) hasta las ocho", "a) hasta que llegue el bus", "El texto dice until the bus comes."),
        (READ + INVITATION + " ¿Qué palabra del texto viene de celebrate? a) celebration b) invitation", "a) celebration", "Celebrate se transforma en celebration."),
    ],
    [
        # app
        (READ + MAYBE + " ¿Qué conector suma la idea de que la profesora nueva también es más amable? a) also b) until", "a) also", "El texto dice she is also friendlier."),
        (READ + INVITATION + " ¿Qué sustantivo del texto significa decisión?", "decision", "Se parece al español y viene de decide."),
        (READ + INVITATION + " ¿A qué hora empieza la competencia?", "Al mediodía", "El texto dice The competition will start at noon."),
    ],
    [
        # rea
        (READ + MAYBE + " Una compañera dice que la profesora nueva es más baja. ¿Qué frase la corrige? a) is taller than the old one b) is also friendlier", "a) is taller than the old one", "Taller than significa más alta que."),
        ("Completa con el comparativo con -er: «My brother is ___ than me» (fast = rápido).", "faster", "Se agrega -er al adjetivo corto."),
    ],
    [
        # cha
        ("Une cada verbo con su sustantivo en -ion. 1) invite 2) collect 3) inform. Sustantivos: a) collection b) information c) invitation", "1-c, 2-a, 3-b", "Invite → invitation, collect → collection, inform → information."),
        ("Completa con el comparativo de easy: «Math is ___ than physics for me». Escribe la palabra.", "easier", "Easy termina en -y y cambia a -ier."),
    ],
    [
        # context
        (READ + "«Maybe I will join the chess club. Then I will invite my friend, and also I will ask my teacher for information about the competition.» (join = unirme, chess = ajedrez, ask = preguntar). ¿Qué conector muestra una posibilidad? a) maybe b) then", "a) maybe", "Maybe expresa algo que quizás ocurra.")
    ],
    [
        # selfcheck
        ("¿Qué significa until?", "Hasta que", "Marca un límite en el tiempo."),
        ("¿Cuál es el comparativo de fast?", "Faster", "Se agrega -er."),
        ("¿Qué terminación tienen information y decision?", "-ion", "Se parecen a las terminaciones -ción y -sión del español."),
    ],
    task("Lee este texto: «My cousin is taller than me. Maybe he will play basketball. Then, he will also join a competition. He is waiting until the new season starts.» (cousin = primo, basketball = básquetbol, season = temporada, join = unirse). En tu hoja escribe el comparativo del texto, un conector de posibilidad, un conector de suma y la palabra en -ion.", "Taller than; maybe; also; competition.", ["encuentra el comparativo en -er", "reconoce maybe y also", "encuentra la palabra en -ion"], ["hoja con cuatro palabras", "nota del adulto"], ["decir que then es de posibilidad", "no encontrar la palabra en -ion"], "Reconoce los conectores correctos y relee con la persona cada frase para revisar el significado."),
    "Lee de nuevo el texto de la invitación y subraya las palabras terminadas en -ion con su verbo.",
    "Escribe en español tres palabras en -ion que conozcas y su verbo en inglés.",
)

# ---------------------------------------------------------------- clase 5: lectura independiente
BIO = "«Ema Ríos was born in a small town in southern Chile. As a child, she loved plants and animals. At fifteen, she started a garden at her school. At twenty-two, she studied biology at the university. Today, she works in a national park and teaches children about trees.» (born = nació, loved = amaba, garden = huerto, studied = estudió, national park = parque nacional, teaches = enseña)"
POEM2 = "«The wind is a painter, he paints the sky, / Blue for the morning, red when day says goodbye. / The wind is a singer, he sings in the trees, / And leaves dance together in the breeze.» (wind = viento, painter = pintor, sky = cielo, goodbye = adiós, sings = canta, leaves = hojas, breeze = brisa)"
NEWS2 = "«The city library opened a new room for teenagers. It has fifty computers and two hundred comics. The room is open from Monday to Saturday. Librarian Paula says: Reading is fun, and now more students come here.» (teenagers = adolescentes, computers = computadores, comics = cómics, librarian = bibliotecaria, fun = entretenido)"

lesson(
    OA4, 5,
    "Los textos escritos en cada ejercicio (una biografía, un poema y una noticia) y lápiz.",
    "Aprenderé a leer por mi cuenta una biografía, un poema y una noticia e identificar propósito, ideas generales, información específica, tema y relaciones. Sirve para comprobar que puedo comprender textos variados sin ayuda.",
    ["Sé reconocer personajes, problema, solución y conectores.", "Distingo hecho y opinión."],
    [
        "En una lectura independiente (independent reading), usas todas las estrategias que ya conoces. Primero identifica el formato: una biografía (biography) cuenta la vida de una persona en orden; un poema usa versos y rimas; una noticia (news) informa algo reciente con datos y citas. Cada formato tiene un propósito diferente: informar, emocionar o dar a conocer.",
        "Para comprender, sigue tres pasos. Uno: lee el título y mira la estructura. Dos: lee el texto completo y subraya nombres, cifras y conectores. Tres: responde las preguntas con el dato exacto. En una biografía, ordena los hechos por edades (at fifteen, at twenty-two). En un poema, busca el tema y las imágenes. En una noticia, separa los hechos de las citas y las opiniones.",
        "Después de responder, vuelve al texto para comprobar. Si una respuesta no aparece en el texto, no la inventes: busca otra vez. Una buena lectura también conecta ideas: ¿qué relación hay entre la infancia de Ema y su trabajo actual? Esa relación es una idea de nivel superior que sale de unir dos datos del texto.",
    ],
    [("biography", "biografía: vida de una persona"), ("news", "noticia"), ("poem", "poema"), ("fact", "hecho"), ("quote", "cita: lo que dice una persona"), ("independent", "independiente: sin ayuda")],
    [
        ("Ordenar hechos de una biografía", READ + BIO + " ¿Qué hizo Ema a los quince años?", ["Busco la edad: fifteen.", "Dice At fifteen, she started a garden at her school.", "Ese es el hecho."], "Empezó un huerto en su colegio"),
        ("Tema de un poema", READ + POEM2 + " ¿A quién compara el poema con un pintor?", ["Busco la palabra painter.", "El primer verso dice The wind is a painter.", "El poema compara al viento con un pintor."], "Al viento"),
    ],
    [
        ("Contestar con información que no aparece en el texto.", "Se usa memoria o imaginación.", "Cada respuesta debe tener una frase del texto como evidencia."),
        ("Confundir la cita de la bibliotecaria con un dato de la noticia.", "No se distingue lo que dice una persona.", "Una cita va entre comillas y expresa lo que alguien opina."),
    ],
    [
        # rec
        (READ + BIO + " ¿Qué estudió Ema en la universidad? a) biología b) medicina", "a) biología", "El texto dice she studied biology."),
        (READ + NEWS2 + " ¿Cuántos computadores tiene la nueva sala?", "50", "El texto dice fifty computers."),
        (READ + POEM2 + " ¿Qué color pinta el viento por la mañana? a) azul b) rojo", "a) azul", "El poema dice Blue for the morning."),
    ],
    [
        # und
        (READ + BIO + " ¿Dónde trabaja hoy Ema? a) en un parque nacional b) en una escuela", "a) en un parque nacional", "El texto dice she works in a national park."),
        (READ + NEWS2 + " ¿Qué días está abierta la sala? a) de lunes a sábado b) de lunes a viernes", "a) de lunes a sábado", "El texto dice from Monday to Saturday."),
        (READ + POEM2 + " ¿Qué hacen las hojas en el último verso? a) bailan b) caen", "a) bailan", "El verso dice leaves dance together."),
    ],
    [
        # app
        arith(READ + BIO + " ¿Cuántos años pasaron entre el huerto de Ema (15 años) y sus estudios en la universidad (22 años)?", "22-15", "Se restan las dos edades."),
        (READ + NEWS2 + " ¿Cuál es la cita de la noticia? a) Reading is fun, and now more students come here b) It has fifty computers", "a) Reading is fun, and now more students come here", "Es lo que dice la bibliotecaria."),
        (READ + POEM2 + " ¿Qué palabra rima con «sky»? a) goodbye b) trees", "a) goodbye", "Sky y goodbye terminan con el mismo sonido."),
    ],
    [
        # rea
        (READ + BIO + " ¿Qué relación hay entre lo que le gustaba de niña y su trabajo actual? a) de niña amaba las plantas y hoy enseña sobre árboles b) de niña amaba los barcos y hoy es capitana", "a) de niña amaba las plantas y hoy enseña sobre árboles", "Une la infancia con el trabajo."),
        (READ + NEWS2 + " ¿Cuál de estas frases es una opinión? a) Reading is fun b) The room is open from Monday to Saturday", "a) Reading is fun", "Fun es una valoración de la bibliotecaria."),
    ],
    [
        # cha
        (READ + NEWS2 + " ¿Cuál es el mejor resumen? a) Una biblioteca abrió una sala para adolescentes, con computadores y cómics b) Una bibliotecaria prefiere los cómics", "a) Una biblioteca abrió una sala para adolescentes, con computadores y cómics", "Reúne quién, qué y para quién."),
        (READ + POEM2 + " ¿Qué dos acciones atribuye el poema al viento? Escribe: pintar y ___.", "cantar", "El poema dice que el viento es un pintor y un cantante (sings)."),
    ],
    [
        # context
        (READ + "«Tomás was born in Punta Arenas. At twelve, he built his first telescope from cardboard tubes. At twenty, he studied physics. Today he teaches astronomy to young students.» (telescope = telescopio, cardboard tubes = tubos de cartón, physics = física, astronomy = astronomía). ¿Qué hizo a los doce años? a) construyó un telescopio de cartón b) estudió física", "a) construyó un telescopio de cartón", "El texto dice At twelve, he built his first telescope.")
    ],
    [
        # selfcheck
        ("¿Qué cuenta una biografía?", "La vida de una persona en orden", "Usa edades y fechas."),
        ("¿Qué es una cita en una noticia?", "Lo que dice una persona", "Va entre comillas."),
        ("¿Qué te ayuda a decidir si una frase es opinión?", "Palabras como fun, best o I think", "Son valoraciones personales."),
    ],
    task("Lee este texto: «Valentina Cruz is a young swimmer from Antofagasta. At nine, she joined a swimming club. At fourteen, she won a regional race. Today she trains five days a week. Her coach says: She is the most disciplined athlete I know.» (swimmer = nadadora, joined = se unió, won = ganó, race = carrera, trains = entrena, athlete = deportista). En tu hoja escribe: el formato, tres hechos con edades o cifras, y la frase que es una cita.", "Formato: biografía. Hechos: a los nueve se unió a un club; a los catorce ganó una carrera regional; entrena cinco días a la semana. Cita: She is the most disciplined athlete I know.", ["reconoce el formato", "escribe tres hechos con su cifra", "identifica la cita"], ["hoja con formato, hechos y cita", "nota del adulto"], ["inventar hechos que no están en el texto", "confundir la cita con un hecho"], "Reconoce lo que acertó y relee con la persona los números para comprobar cada hecho."),
    "Lee en voz alta el poema del viento a una persona de tu casa y explica cuál es su tema.",
    "Escribe en español cuál de los tres formatos (biografía, poema o noticia) te resulta más fácil y por qué.",
)
