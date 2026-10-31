"""Cuaderno del estudiante, 6.º básico Inglés (propuesta), EN06 OA 05 (leer y comprender textos literarios y no literarios).

Todos los textos están escritos en el enunciado y son originales; llevan pista en español.
Cada palabra o estructura nueva se explica antes de usarla. Sin audio externo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA5 = "EN06 OA 05"


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


# ---------------------------------------------------------------- clase 1: cuentos (trama, personajes, entorno, tema)
BOAT = "«Nico is a small boat in a big harbour. Every day, the big ships laugh at him because he is slow. One stormy night, a big ship cannot find the way back. Nico uses his small yellow light to guide the ship. The next morning, everyone thanks Nico.» (harbour = puerto, ships = barcos, laugh at = se ríen de, slow = lento, stormy = tormentoso, guide = guiar)"
HOMEWORK = "«On Monday morning, Elena opens her backpack. Her homework is not there! She remembers that she left it on the kitchen table. She asks her teacher if she can bring it tomorrow. The teacher says yes, but asks her to be more careful. Now Elena makes a list and puts it in her backpack every evening.» (opens = abre, left = dejó, kitchen table = mesa de la cocina, careful = cuidadosa, list = lista)"

lesson(
    OA5, 1,
    "Los cuentos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer un cuento e identificar la trama (inicio, desarrollo y final), los personajes, el entorno y el tema. Sirve para comprender cuentos en inglés y para hablar de ellos.",
    ["Sé que un cuento tiene personajes y un lugar.", "Conozco first, then y finally."],
    [
        "Un cuento (story) tiene personajes (characters), que son quienes actúan, y un entorno (setting), que es el lugar y el tiempo. La trama (plot) es lo que ocurre y tiene tres partes. El inicio (beginning) presenta a los personajes y el problema. El desarrollo (middle) muestra qué pasa para resolverlo. El final (end) dice cómo termina.",
        "El tema (theme) es la idea general que el cuento enseña. No se dice con palabras exactas: se deduce. En el cuento del barco pequeño, el tema es que quienes son pequeños también pueden ser muy útiles. Para encontrar el tema, pregúntate: ¿qué aprende el personaje? y ¿qué quiere decir el autor?",
        "Para leer mejor, subraya los nombres de los personajes y las palabras de lugar y tiempo, como harbour, stormy night o next morning. Luego busca el problema, la solución y el final. Si una palabra es nueva, mira la oración completa: casi siempre da una pista. No necesitas traducir cada palabra para comprender.",
    ],
    [("character", "personaje"), ("setting", "entorno: lugar y tiempo"), ("plot", "trama"), ("beginning / middle / end", "inicio / desarrollo / final"), ("theme", "tema"), ("problem / solution", "problema / solución")],
    [
        ("Personaje y entorno", "Lee: «Max is a young dog who lives on a farm. One sunny morning, he loses his red ball in the tall grass.» (farm = granja, loses = pierde, tall grass = pasto alto). ¿Quién es el personaje y dónde está?", ["El personaje es Max, un perro.", "El lugar es una granja.", "El tiempo es una mañana de sol."], "Max, en una granja"),
        ("Inicio, desarrollo y final", "Sigue con el cuento: «Max looks for the ball for an hour. A bird shows him where it is. Max says thanks and plays all afternoon.» ¿Qué parte es «A bird shows him where it is»?", ["El inicio presenta el problema: perdió la pelota.", "Buscar y encontrar ayuda es el desarrollo.", "Jugar toda la tarde es el final."], "El desarrollo"),
    ],
    [
        ("Decir que el tema es «un barco» porque el cuento habla de uno.", "Se confunde el tema con los personajes.", "El tema es la idea que se aprende, por ejemplo que los pequeños también ayudan."),
        ("Mezclar el inicio con el final.", "No se sigue la secuencia del texto.", "Busca palabras de tiempo como one day, then, the next morning."),
    ],
    [
        ("Lee: " + BOAT + " ¿Quién es el personaje principal? a) Nico b) un barco grande c) una tormenta", "a) Nico", "El cuento comienza con Nico is a small boat."),
        ("Lee: " + BOAT + " ¿Dónde vive Nico?", "En un puerto", "Dice in a big harbour."),
        ("Lee: " + BOAT + " ¿Cuándo ocurre el problema? a) en una noche de tormenta b) en una mañana de sol", "a) en una noche de tormenta", "Dice one stormy night."),
    ],
    [
        ("Lee: " + BOAT + " ¿Por qué los barcos grandes se ríen de Nico?", "Porque es lento", "Dice because he is slow."),
        ("Lee: " + BOAT + " ¿Qué oración muestra el final? a) The next morning, everyone thanks Nico. b) Nico is a small boat.", "a) The next morning, everyone thanks Nico.", "Cierra la historia con el resultado."),
        ("Lee: " + BOAT + " ¿Cuál es el tema? a) los pequeños también pueden ayudar b) los barcos grandes son malos c) hay que evitar las tormentas", "a) los pequeños también pueden ayudar", "Nico es pequeño y salva a un barco grande."),
    ],
    [
        ("Lee: " + HOMEWORK + " ¿Qué problema tiene Elena?", "No encuentra su tarea", "Dice her homework is not there."),
        ("Lee: " + HOMEWORK + " ¿Dónde había dejado la tarea?", "En la mesa de la cocina", "Dice she left it on the kitchen table."),
        ("Lee: " + HOMEWORK + " ¿Cuál es la solución que usa Elena? a) hacer una lista y guardarla en su mochila cada tarde b) comprar otra mochila", "a) hacer una lista y guardarla en su mochila cada tarde", "Dice Elena makes a list."),
    ],
    [
        ("Lee: " + HOMEWORK + " Una compañera dice que la profesora se enoja y le pone una mala nota. ¿Qué dice el texto?", "Que la profesora dice que sí, pero le pide ser más cuidadosa", "No hay mala nota; dice yes and asks her to be more careful."),
        ("Lee: " + HOMEWORK + " ¿Cuál es el tema del cuento? a) ser organizado para no olvidar cosas b) los profesores son estrictos", "a) ser organizado para no olvidar cosas", "Elena aprende a usar una lista."),
    ],
    [
        ("Ordena los hechos del cuento de Elena. A) Hace una lista. B) Abre su mochila y no está la tarea. C) Le pide permiso a su profesora.", "B, C, A", "Primero el problema, luego pide ayuda y finalmente actúa."),
        ("¿Cuántos personajes con nombre o cargo aparecen en el cuento de Elena?", "2", "Aparecen Elena y su profesora."),
    ],
    [("Lee: «Sam left his lunch box on the bus. The driver found it and gave it to the school secretary the next day. Sam was very happy.» (lunch box = lonchera, driver = conductor, secretary = secretaria). ¿Quién encontró la lonchera?", "El conductor", "Dice the driver found it.")],
    [
        ("¿Qué es el entorno (setting) de un cuento?", "El lugar y el tiempo", "Indica dónde y cuándo pasa."),
        ("¿Qué partes tiene la trama?", "Inicio, desarrollo y final", "Estructuran lo que ocurre."),
        ("¿Qué es el tema de un cuento?", "La idea general que enseña", "Se deduce de lo que pasa."),
    ],
    task("Lee este cuento: «Lía is a girl who lives near the sea. She wants to enter the swimming race, but she is afraid of the cold water. Her friend Omar swims with her every afternoon. After two weeks, Lía is not afraid anymore. On the day of the race, she finishes second and smiles.» (race = carrera, afraid = con miedo, anymore = ya no, second = segunda). Escribe en tu hoja: personajes, entorno, problema, solución, final y el tema con tus propias palabras.", "Personajes: Lía y Omar. Entorno: cerca del mar. Problema: miedo al agua fría. Solución: nadar con su amigo cada tarde. Final: termina segunda y sonríe. Tema: con ayuda se supera el miedo.", ["identifica personajes y entorno", "separa problema, solución y final", "formula un tema coherente"], ["hoja con cuadro de la trama", "nota del adulto"], ["confundir la solución con el final", "decir que el tema es «una carrera»"], "Reconoce lo bien identificado y muestra cómo distinguir el problema de la solución con la pregunta ¿qué la ayudó?"),
    "Vuelve a leer el cuento de Nico y subraya con un color el inicio, con otro el desarrollo y con otro el final.",
    "Escribe tres frases en español con el inicio, el desarrollo y el final de un cuento que conozcas.",
)

# ---------------------------------------------------------------- clase 2: poemas y tiras cómicas
SEED = "«The Little Seed. A little seed sleeps in the ground. It does not make a single sound. The rain comes down, the sun shines bright, and now it grows toward the light.» (seed = semilla, ground = suelo, sound = sonido, shines = brilla, grows = crece, toward = hacia)"
COMIC1 = "Tira cómica. Viñeta 1 (una niña con un plato vacío): «I'm hungry!» Viñeta 2 (un niño abre el refrigerador): «There is only one sandwich.» Viñeta 3 (el niño le da la mitad a la niña): «Let's share it!» Viñeta 4 (los dos comen y sonríen): «Thank you! You are a good friend.» (hungry = con hambre, empty = vacío, share = compartir, half = mitad)"
COMIC2 = "Tira cómica. Viñeta 1 (un niño mira un paraguas roto): «Oh no!» Viñeta 2 (empieza a llover): «I will get wet.» Viñeta 3 (una niña llega con un paraguas grande): «Come under mine!» Viñeta 4 (los dos caminan juntos y sonríen). (broken = roto, get wet = mojarse, mine = el mío)"

lesson(
    OA5, 2,
    "Los poemas y tiras cómicas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer un poema y una tira cómica e identificar el tema, las rimas, los personajes, las viñetas y lo que dicen los globos de diálogo. Sirve para comprender textos literarios cortos en inglés.",
    ["Sé que dos palabras riman si terminan igual.", "Conozco palabras como rain, sun y friend."],
    [
        "Un poema (poem) se organiza en versos (lines) que a veces riman. En el poema «The Little Seed», ground rima con sound y bright rima con light. El tema de un poema es la idea central: aquí, cómo una semilla crece con lluvia y sol. Las palabras clave, como seed, rain y sun, te llevan al tema.",
        "Una tira cómica (comic strip) cuenta una historia con dibujos y palabras. Cada cuadro se llama viñeta (panel). Lo que dicen los personajes está en globos de diálogo (speech bubbles). Para comprenderla, lee las viñetas en orden, mira los gestos y busca el problema, la solución y el sentimiento final.",
        "Tanto en el poema como en la tira cómica puedes preguntarte: ¿quién habla o actúa?, ¿qué ocurre? y ¿qué quiere mostrar el texto? En una tira cómica, las expresiones cortas como Oh no! o Thank you! muestran sentimientos. En un poema, las comparaciones y las repeticiones refuerzan una idea.",
    ],
    [("poem / line", "poema / verso"), ("rhyme", "rima"), ("comic strip", "tira cómica"), ("panel", "viñeta"), ("speech bubble", "globo de diálogo"), ("theme", "tema")],
    [
        ("Rima en un poema", "Lee el poema: «A cat sat on a mat. It had a hat. That was that.» (mat = alfombra). ¿Qué palabras riman con cat?", ["Miro el final de cada verso.", "Mat, hat y that terminan con -at.", "Riman con cat."], "mat, hat y that"),
        ("Viñetas y globos", "Lee una tira: Viñeta 1: un niño con una pelota: «Let's play!» Viñeta 2: otro niño: «Okay!» ¿Cuántas personas hablan en la tira y qué proponen?", ["Cada globo es de un personaje distinto.", "Hablan dos personas.", "Proponen jugar."], "Dos personas; proponen jugar"),
    ],
    [
        ("Leer las viñetas en desorden.", "Se pierde la secuencia de la historia.", "Lee de izquierda a derecha y de arriba abajo, viñeta por viñeta."),
        ("Pensar que en un poema siempre riman todos los versos.", "Hay poemas sin rimas.", "Busca el final de cada verso y compara los sonidos."),
    ],
    [
        ("Lee: " + SEED + " ¿Qué palabra rima con bright? a) light b) seed c) rain", "a) light", "Bright y light terminan igual."),
        ("Lee: " + SEED + " ¿Qué necesita la semilla para crecer? a) lluvia y sol b) nieve y viento", "a) lluvia y sol", "Dice the rain comes down, the sun shines bright."),
        ("Lee: " + COMIC1 + " ¿Cuántas viñetas tiene la tira?", "4", "Se indican cuatro viñetas."),
    ],
    [
        ("Lee: " + SEED + " ¿Cuál es el tema del poema? a) cómo crece una semilla b) cómo viaja un avión", "a) cómo crece una semilla", "Habla de una semilla que crece hacia la luz."),
        ("Lee: " + COMIC1 + " ¿Cuál es el problema de la niña? a) tiene hambre y hay un solo sándwich b) perdió su plato", "a) tiene hambre y hay un solo sándwich", "Lo dice la viñeta 1 y la viñeta 2."),
        ("Lee: " + COMIC1 + " ¿Cuál es la solución? a) compartir el sándwich b) comprar otro", "a) compartir el sándwich", "En la viñeta 3 dicen Let's share it!"),
    ],
    [
        ("Lee: " + COMIC2 + " ¿Qué problema tiene el niño? a) su paraguas está roto b) perdió su sombrero", "a) su paraguas está roto", "Lo muestra la viñeta 1."),
        ("Lee: " + COMIC2 + " ¿Quién ayuda al niño?", "Una niña con un paraguas grande", "Dice Come under mine!"),
        ("Lee: " + COMIC2 + " ¿Cuántos personajes aparecen?", "2", "Son el niño y la niña."),
    ],
    [
        ("Un compañero dice que en la tira del sándwich el final es triste. ¿Qué viñeta lo contradice?", "La viñeta 4, donde sonríen", "Ambos comen y sonríen."),
        ("Lee: " + SEED + " ¿Qué palabras muestran la idea del crecimiento? a) grows toward the light b) sleeps in the ground", "a) grows toward the light", "Grows es crece."),
    ],
    [
        ("Lee los versos desordenados: A) And now it grows toward the light. B) A little seed sleeps in the ground. C) The rain comes down, the sun shines bright. Ordénalos como en el poema.", "B, C, A", "El poema empieza con la semilla dormida y termina con su crecimiento."),
        ("Lee: " + COMIC2 + " ¿Qué tema muestra la tira? a) la amistad y la ayuda b) las tormentas", "a) la amistad y la ayuda", "La niña ofrece su paraguas."),
    ],
    [("Lee: «Panel 1: A boy says: I can't find my pencil! Panel 2: A girl says: It's behind your ear! Panel 3: The boy laughs.» (pencil = lápiz, behind = detrás, ear = oreja, laughs = ríe). ¿Dónde estaba el lápiz?", "Detrás de su oreja", "La viñeta 2 lo indica.")],
    [
        ("¿Cómo se llaman los cuadros de una tira cómica?", "Viñetas", "Panel es viñeta."),
        ("¿Dónde está lo que dicen los personajes?", "En los globos de diálogo", "Se llaman speech bubbles."),
        ("¿Riman ground y sound?", "Sí", "Terminan con el mismo sonido."),
    ],
    task("Lee este poema: «The Moon. The moon is high, the moon is white. It watches over us at night. It makes the sea go up and down, and shines upon the sleeping town.» (high = alta, watches over = cuida, sea = mar, shines = ilumina, sleeping = durmiendo). Escribe: el tema, dos pares de palabras que riman y una pregunta que le harías al poema (por ejemplo, empezando con Why o What).", "Tema: la luna de noche. Riman white-night y down-town. Pregunta: Why does the moon shine?", ["escribe un tema coherente", "anota dos pares de rima", "formula una pregunta con una palabra interrogativa"], ["hoja con respuestas", "nota del adulto"], ["decir que riman moon y high", "formular una pregunta sin relación con el texto"], "Reconoce lo que acertó y repasa con la persona los finales de los versos."),
    "Dibuja tu propia tira cómica de tres viñetas con una frase en inglés en cada una.",
    "Escribe un poema de cuatro versos sobre el sol en que rimen dos pares de palabras.",
)

# ---------------------------------------------------------------- clase 3: emails y diálogos
EMAIL1 = "«From: Tomás. To: Rosa. Subject: My birthday. Hi Rosa, my birthday party is on May 10th at 4 p.m. We will play games in the park near the school. Please bring a ball. Can you come? Write back before Wednesday. Bye, Tomás.» (party = fiesta, games = juegos, near = cerca de, bring = trae, write back = responde)"
EMAIL2 = "«From: Rosa. To: Tomás. Subject: Re: My birthday. Hi Tomás! Thank you for the invitation. I can come, but I will arrive at 4:30 because I have a music class. See you there! Rosa.» (invitation = invitación, arrive = llegar, music class = clase de música)"
CHAT = "«Leo: Do you have the Math homework? Sara: Yes, it is on page 24. Leo: Thanks! Which exercises? Sara: Numbers 1 to 6. Leo: Great. Is it for tomorrow? Sara: Yes, it is.» (homework = tarea, page = página, which = cuáles, exercises = ejercicios, for tomorrow = para mañana)"

lesson(
    OA5, 3,
    "Los emails y diálogos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer emails y diálogos e identificar quién escribe, a quién, para qué y los datos de fecha, hora, lugar y qué traer. Sirve para comprender mensajes reales y responderlos.",
    ["Sé leer horas y fechas en inglés.", "Conozco palabras como party, park y bring."],
    [
        "Un email tiene partes fijas: From (de quién), To (para quién), Subject (asunto), el saludo (Hi...), el mensaje y la despedida (Bye, See you). Antes de leer los detalles, mira el asunto y los nombres: te dicen de qué trata y quién habla con quién. Un email de invitación suele incluir fecha, hora, lugar y qué traer.",
        "Las fechas se escriben con mes y número: May 10th se lee «May tenth» (10 de mayo). Las horas llevan a.m. (de la mañana) o p.m. (de la tarde): 4 p.m. son las 16:00. Para pedir una respuesta se usa «Write back» o «Can you come?». Para aceptar: «I can come». Para avisar un cambio: «I will arrive at 4:30».",
        "Un diálogo escrito muestra los turnos con el nombre antes de los dos puntos. Para leerlo, identifica quién pregunta y quién responde. Busca la información específica que se pide: una página, un número, un día. Subraya los datos clave y comprueba que respondiste con la información exacta del texto, no con lo que tú supones.",
    ],
    [("From / To / Subject", "de / para / asunto"), ("invitation", "invitación"), ("a.m. / p.m.", "de la mañana / de la tarde"), ("write back", "responder por escrito"), ("bring", "traer"), ("exercises", "ejercicios")],
    [
        ("Partes de un email", "Lee: «From: Ana. To: Pedro. Subject: Homework help.» ¿Quién escribe, a quién y sobre qué?", ["From dice quién escribe: Ana.", "To dice a quién: Pedro.", "Subject dice el tema: ayuda con la tarea."], "Ana escribe a Pedro sobre ayuda con la tarea"),
        ("Información específica", "Lee: «The class is at 3 p.m. in room 5.» (room = sala). ¿A qué hora y dónde es la clase?", ["Busco la hora: 3 p.m.", "p.m. indica la tarde: las 15:00.", "El lugar es la sala 5."], "A las 3 de la tarde, en la sala 5"),
    ],
    [
        ("Pensar que 4 p.m. es la mañana.", "Se confunde p.m. con a.m.", "A.m. es antes del mediodía; p.m. es después."),
        ("Responder con un supuesto en vez de con el dato del email.", "No se vuelve al texto.", "Busca el dato exacto en el email."),
    ],
    [
        ("Lee: " + EMAIL1 + " ¿Quién escribe el email? a) Tomás b) Rosa", "a) Tomás", "Aparece en la línea From."),
        ("Lee: " + EMAIL1 + " ¿Cuál es el asunto?", "Mi cumpleaños", "Está en la línea Subject."),
        ("Lee: " + EMAIL1 + " ¿Qué hay que traer? a) una pelota b) una torta", "a) una pelota", "Dice Please bring a ball."),
    ],
    [
        ("Lee: " + EMAIL1 + " ¿Qué día es la fiesta?", "El 10 de mayo", "Dice May 10th."),
        ("Lee: " + EMAIL1 + " ¿Dónde será la fiesta? a) en el parque cerca del colegio b) en la casa de Rosa", "a) en el parque cerca del colegio", "Dice the park near the school."),
        ("Lee: " + EMAIL2 + " ¿Por qué llegará Rosa a las 4:30? a) porque tiene clase de música b) porque tiene hambre", "a) porque tiene clase de música", "Dice because I have a music class."),
    ],
    [
        ("Lee: " + CHAT + " ¿Qué página tiene la tarea?", "La 24", "Dice it is on page 24."),
        ("Lee: " + CHAT + " ¿Cuántos ejercicios hay que hacer, del 1 al 6?", "6", "Los números son 1, 2, 3, 4, 5 y 6."),
        ("Lee: " + CHAT + " ¿Para cuándo es la tarea?", "Para mañana", "Dice Is it for tomorrow? Yes, it is."),
    ],
    [
        ("Lee: " + EMAIL2 + " ¿A qué hora llegará Rosa?", "A las 4:30", "Dice I will arrive at 4:30."),
        ("Lee los dos emails. ¿Cuántos minutos después del inicio de la fiesta llegará Rosa?", "30", "La fiesta empieza a las 4:00 p.m. y Rosa llega a las 4:30: hay media hora, 30 minutos."),
    ],
    [
        ("Ordena los mensajes. A) Rosa acepta y avisa que llegará a las 4:30. B) Tomás invita a Rosa. C) Tomás recibe la respuesta.", "B, A, C", "Primero la invitación, luego la respuesta y después se recibe."),
        ("Un compañero cree que la fiesta es en la mañana. ¿Qué dato del email lo corrige?", "4 p.m.", "P.m. indica la tarde."),
    ],
    [("Lee este email: «From: Grandma Julia. To: Camila. Subject: Visit. Hi Camila, I will visit you on Saturday at 11 a.m. I will bring bread. See you soon!» (visit = visitar, bread = pan). ¿A qué hora llega y qué trae?", "A las 11 de la mañana; trae pan", "Dice 11 a.m. y I will bring bread.")],
    [
        ("¿Qué indica «Subject» en un email?", "El asunto o tema", "Dice de qué trata."),
        ("¿Qué indica p.m.?", "Después del mediodía", "Es la tarde o la noche."),
        ("¿Qué significa «write back»?", "Responder por escrito", "Se contesta el mensaje."),
    ],
    task("Lee este email y respóndelo: «From: Diego. To: Valentina. Subject: Science project. Hi Valentina, can we work on the Science project on Thursday at 5 p.m.? We can meet in the library. Please bring the poster. Diego.» (project = proyecto, meet = encontrarnos, poster = cartel). Escribe en inglés una respuesta de tres líneas que confirme el día, la hora y qué llevarás, usando I can come y I will bring.", "Hi Diego! I can come on Thursday at 5 p.m. I will bring the poster. See you in the library. Valentina.", ["confirma día y hora", "usa I will bring con el objeto correcto", "incluye saludo y despedida"], ["hoja con el email", "nota del adulto"], ["cambiar la hora", "olvidar el saludo"], "Reconoce el email completo y revisa que cada dato coincida con el mensaje original."),
    "Relee el email de Tomás y subraya con colores la fecha, la hora, el lugar y qué traer.",
    "Escribe un email corto de invitación a un amigo con fecha, hora y lugar.",
)

# ---------------------------------------------------------------- clase 4: artículos, noticias y biografías
DOLPHIN = "«Dolphins are mammals, not fish. They breathe air through a hole on the top of their heads. They live in groups called pods. Dolphins talk to each other with clicks and whistles.» (mammals = mamíferos, breathe = respiran, hole = orificio, pods = grupos, clicks = chasquidos, whistles = silbidos)"
NEWS = "«Pine Hill School wins a green prize. On May 3rd, the students of Pine Hill School received a prize for their school garden. They planted one hundred and twenty flowers and collected rain water in barrels. The principal said: We are very proud of our students.» (prize = premio, received = recibieron, garden = huerto, planted = plantaron, barrels = barriles, principal = director)"
MISTRAL = "«Gabriela Mistral was born in 1889 in Vicuña, Chile. She was a teacher and a poet. In 1945, she won the Nobel Prize in Literature. She was the first Latin American writer to win this prize. She died in 1957.» (born = nació, teacher = profesora, poet = poeta, won = ganó, prize = premio, died = murió)"

lesson(
    OA5, 4,
    "Los artículos, noticias y biografías escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer artículos informativos, noticias y biografías e identificar la idea general, las fechas, las personas y los lugares. Sirve para informarte en inglés.",
    ["Sé leer años y fechas.", "Conozco palabras como born, teacher y prize."],
    [
        "Un artículo informativo (informative article) explica un tema con datos verdaderos. Su idea general está en la primera oración. Una noticia (news article) cuenta un hecho reciente y responde Who, What, Where y When. Una biografía (biography) cuenta la vida de una persona con fechas: born (nació), studied (estudió), won (ganó) y died (murió).",
        "Para ubicar información específica, usa preguntas: ¿quién?, ¿qué?, ¿cuándo?, ¿dónde? y ¿cuántos? Subraya las fechas y los números. Los años se leen en grupos: 1889 es eighteen eighty-nine y 1945 es nineteen forty-five. También puedes calcular: si alguien nació en 1889 y ganó un premio en 1945, pasaron 56 años.",
        "Cada tipo de texto tiene su función. El artículo informa sobre un tema general; la noticia informa de algo que ocurrió; la biografía narra una vida. Reconocerlo te ayuda a leer con un propósito. Después de leer, comprueba que puedes decir la idea general en una oración y dos datos específicos con números o nombres.",
    ],
    [("article", "artículo"), ("news", "noticia"), ("biography", "biografía"), ("born / died", "nació / murió"), ("won", "ganó"), ("prize", "premio")],
    [
        ("Idea general y dato", "Lee: «The blue whale is the largest animal in the world. It can be thirty metres long.» (whale = ballena, largest = más grande, metres = metros). ¿Cuál es la idea general y cuánto puede medir?", ["La primera oración da la idea general: la ballena azul es el animal más grande.", "El dato específico es thirty metres.", "Thirty es treinta."], "La ballena azul es el animal más grande; puede medir 30 metros"),
        ("Fechas en una biografía", "Lee: «Pablo was born in 1980 and won a prize in 2004.» ¿Cuántos años pasaron entre ambos hechos?", ["Anoto los años: 1980 y 2004.", "Resto: 2004 − 1980.", "Son 24 años."], "24 años"),
    ],
    [
        ("Copiar la fecha sin calcular cuando la pregunta pide cuántos años.", "No se interpreta la pregunta.", "Resta los años cuando la pregunta es How many years."),
        ("Confundir noticia con biografía.", "No se reconoce la función del texto.", "La noticia cuenta un hecho reciente; la biografía, la vida de una persona."),
    ],
    [
        ("Lee: " + DOLPHIN + " ¿Qué tipo de texto es? a) un artículo informativo b) una biografía", "a) un artículo informativo", "Explica datos sobre los delfines."),
        ("Lee: " + DOLPHIN + " ¿Por dónde respiran los delfines?", "Por un orificio en la cabeza", "Dice through a hole on the top of their heads."),
        ("Lee: " + DOLPHIN + " ¿Cómo se llaman los grupos de delfines? a) pods b) herds", "a) pods", "Dice groups called pods."),
    ],
    [
        ("Lee: " + NEWS + " ¿Quién recibió el premio? a) los estudiantes de Pine Hill School b) el director", "a) los estudiantes de Pine Hill School", "Dice the students received a prize."),
        ("Lee: " + NEWS + " ¿Por qué recibieron el premio?", "Por su huerto escolar", "Dice for their school garden."),
        ("Lee: " + NEWS + " ¿Cuándo recibieron el premio?", "El 3 de mayo", "Dice On May 3rd."),
    ],
    [
        ("Lee: " + NEWS + " ¿Cuántas flores plantaron? Responde con el número.", "120", "Dice one hundred and twenty flowers."),
        ("Lee: " + MISTRAL + " ¿Dónde nació Gabriela Mistral?", "En Vicuña, Chile", "Dice born in 1889 in Vicuña, Chile."),
        ("Lee: " + MISTRAL + " ¿Cuántos años pasaron entre su nacimiento y el Premio Nobel?", "56", "Entre 1889 y 1945 pasaron 56 años.", "1945-1889"),
    ],
    [
        ("Lee: " + MISTRAL + " ¿Cuántos años pasaron entre el Premio Nobel y su muerte?", "12", "Entre 1945 y 1957 pasaron 12 años.", "1957-1945"),
        ("Lee: " + MISTRAL + " ¿A qué se dedicaba antes de ganar el premio? a) era profesora y poeta b) era cantante", "a) era profesora y poeta", "Dice she was a teacher and a poet."),
    ],
    [
        ("Lee: " + NEWS + " Un compañero dice que el director no está contento. ¿Qué frase del texto lo contradice?", "We are very proud of our students", "El director dice que está muy orgulloso."),
        ("Ordena los hechos de la vida de Gabriela Mistral según el texto. A) murió B) nació C) ganó el Nobel", "B, C, A", "Primero nació en 1889, luego ganó el premio en 1945 y murió en 1957."),
    ],
    [("Lee esta noticia corta: «Last Saturday, a runner from Chile finished a 10-kilometre race in forty minutes. She was the fastest in her group.» (runner = corredora, race = carrera, fastest = la más rápida). ¿Cuánto tardó?", "40 minutos", "Dice forty minutes.")],
    [
        ("¿Qué contesta una noticia?", "Quién, qué, dónde y cuándo", "Reporta un hecho."),
        ("¿Qué significa «born»?", "Nació", "Se usa en biografías."),
        ("¿Qué cuenta una biografía?", "La vida de una persona", "Incluye fechas y logros."),
    ],
    task("Lee esta biografía corta: «Violeta Parra was born in Chile in 1917. She was a singer, a painter and a collector of folk songs. She travelled around the country to find old songs. She died in 1967.» (singer = cantante, painter = pintora, collector = recopiladora, folk songs = canciones tradicionales, travelled = viajó, old = antiguas). Escribe: el tipo de texto, la idea general, tres datos específicos y cuántos años pasaron entre su nacimiento y su muerte.", "Es una biografía. Trata de la vida de Violeta Parra. Datos: nació en Chile en 1917; fue cantante, pintora y recopiladora; murió en 1967. Pasaron 50 años.", ["identifica que es una biografía", "anota tres datos específicos", "calcula 50 años"], ["hoja con respuestas", "nota del adulto"], ["confundir nacimiento y muerte", "restar mal los años"], "Reconoce los datos bien ubicados y repasa la resta de años con la persona."),
    "Busca en la noticia de Pine Hill School las preguntas Who, What, Where y When y escribe la respuesta de cada una.",
    "Escribe una biografía de cuatro oraciones de una persona de tu familia o de tu curso, con año de nacimiento.",
)

# ---------------------------------------------------------------- clase 5: procedimientos, causa-efecto y problema-solución
BAG = "«How to prepare your school bag. First, look at your timetable. Second, take the books you need. Third, put your pencil case and your notebook in the bag. Finally, add your water bottle and close the bag.» (timetable = horario, books you need = libros que necesitas, pencil case = estuche, add = agregar, close = cerrar)"
RAIN = "«It rained all night. As a result, the river rose and the bridge was closed. Because of that, many students arrived late to school.» (rained = llovió, rose = subió, bridge = puente, as a result = como resultado, because of that = por eso, late = tarde)"
YARD = "«Problem: The school yard is dirty after lunch. Solution: Each class chooses two students to be the Green Team. The Green Team picks up the papers and puts them in the bins. Now the yard is clean every day.» (yard = patio, picks up = recoge, bins = basureros, clean = limpio)"

lesson(
    OA5, 5,
    "Los procedimientos y textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer un procedimiento y a reconocer la secuencia de pasos, las relaciones de causa y efecto y el problema con su solución. Sirve para comprender cómo se hace algo y por qué ocurre algo.",
    ["Sé usar first, second y finally.", "Conozco palabras como rain, bridge y late."],
    [
        "Un procedimiento (procedure) explica cómo hacer algo paso a paso. Usa palabras de secuencia: first, second, third, next, then y finally. Cada paso comienza con un verbo de orden: look, take, put, add, close. Para comprobar que comprendiste, ordena los pasos y explica qué pasa si falta uno.",
        "La relación de causa y efecto (cause and effect) explica por qué ocurre algo. La causa es lo que pasa primero y el efecto es lo que sucede después. Se marca con because (porque), as a result (como resultado) y because of that (por eso). Por ejemplo, la lluvia es la causa, y el puente cerrado es un efecto.",
        "El problema y la solución (problem and solution) es otra estructura. Primero se presenta un problema y luego lo que se hace para resolverlo. Busca las palabras Problem y Solution, o expresiones como the problem is... y to solve it... (para resolverlo...). Tras leer, puedes preguntarte si la solución funciona y por qué.",
    ],
    [("procedure", "procedimiento"), ("cause", "causa"), ("effect", "efecto"), ("as a result", "como resultado"), ("because of that", "por eso"), ("problem / solution", "problema / solución")],
    [
        ("Secuencia de pasos", "Lee: «First, wash the fruit. Second, put it in a bowl. Third, add a little lemon.» (fruit = fruta, bowl = bol, lemon = limón). ¿Qué se hace en el segundo paso?", ["Busco la palabra second.", "Dice put it in a bowl.", "El paso es ponerla en un bol."], "Ponerla en un bol"),
        ("Causa y efecto", "Lee: «It snowed a lot. As a result, the road was closed.» (snowed = nevó, road = camino). ¿Cuál es la causa y cuál el efecto?", ["La causa es lo que pasó primero: nevó mucho.", "As a result marca el efecto.", "El efecto es que el camino se cerró."], "Causa: nevó mucho. Efecto: el camino se cerró"),
    ],
    [
        ("Cambiar el orden de los pasos.", "No se siguen las palabras de secuencia.", "Ordena con first, second, third y finally."),
        ("Confundir la causa con el efecto.", "Se invierte la relación.", "La causa es lo que ocurre antes; el efecto, lo que sucede después."),
    ],
    [
        ("Lee: " + BAG + " ¿Qué se hace primero? a) mirar el horario b) cerrar la mochila", "a) mirar el horario", "Dice First, look at your timetable."),
        ("Lee: " + BAG + " ¿Qué se agrega al final?", "La botella de agua", "Dice Finally, add your water bottle."),
        ("Lee: " + BAG + " ¿Cuántos pasos tiene el procedimiento?", "4", "Son first, second, third y finally."),
    ],
    [
        ("Lee: " + RAIN + " ¿Cuál es la causa de lo que ocurrió? a) llovió toda la noche b) los estudiantes llegaron tarde", "a) llovió toda la noche", "Es lo que pasó primero."),
        ("Lee: " + RAIN + " ¿Qué pasó con el puente?", "Se cerró", "Dice the bridge was closed."),
        ("Lee: " + RAIN + " ¿Cuál fue el efecto final? a) muchos estudiantes llegaron tarde b) el río bajó", "a) muchos estudiantes llegaron tarde", "Dice because of that, many students arrived late."),
    ],
    [
        ("Lee: " + YARD + " ¿Cuál es el problema?", "El patio queda sucio después del almuerzo", "Dice the school yard is dirty after lunch."),
        ("Lee: " + YARD + " ¿Cuántos estudiantes por curso forman el Green Team?", "2", "Dice two students."),
        ("Lee: " + YARD + " ¿Qué hace el equipo con los papeles?", "Los recoge y los pone en los basureros", "Dice picks up the papers and puts them in the bins."),
    ],
    [
        ("Lee: " + YARD + " Si hay 6 cursos y cada uno elige 2 estudiantes, ¿cuántos estudiantes forman el Green Team en total?", "12", "Cada curso elige dos estudiantes y son seis cursos.", "6*2"),
        ("Lee: " + BAG + " Si olvidas el segundo paso, ¿qué te falta en la mochila? a) los libros que necesitas b) la botella de agua", "a) los libros que necesitas", "El segundo paso es take the books you need."),
    ],
    [
        ("Ordena los pasos de un procedimiento de higiene. A) Seca las manos. B) Moja las manos. C) Frota con jabón.", "B, C, A", "El orden es mojar, jabonar y secar."),
        ("Lee: «The bus broke down, so the students walked to school.» (broke down = se descompuso). Elige la causa. a) The bus broke down. b) The students walked to school.", "a) The bus broke down.", "La causa es lo que pasó primero y provocó el otro hecho."),
    ],
    [("Lee: «Problem: The class library has too few books. Solution: Every student brings one book from home to share.» (too few = muy pocos, share = compartir). ¿Cuál es la solución?", "Cada estudiante trae un libro para compartir", "Dice every student brings one book from home to share.")],
    [
        ("¿Qué palabra marca el último paso?", "finally", "Marca el final de la secuencia."),
        ("¿Qué significa «as a result»?", "Como resultado", "Introduce un efecto."),
        ("¿Qué estructura presenta Problem y Solution?", "Problema y solución", "Muestra una dificultad y cómo se resuelve."),
    ],
    task("Lee este texto: «The playground has no shade. Children get very hot at recess. Solution: First, the school plants three trees. Then it puts two benches under them. As a result, the children can rest in the shade.» (shade = sombra, benches = bancas, rest = descansar). Escribe: el problema, la solución, un efecto y la secuencia: ¿qué se hace primero, plantar los árboles o poner las bancas?", "Problema: no hay sombra. Solución: plantar tres árboles y poner dos bancas. Efecto: los niños descansan a la sombra. Primero se plantan los árboles y después se ponen las bancas bajo ellos.", ["identifica el problema", "identifica la solución", "indica un efecto"], ["hoja con respuestas", "nota del adulto"], ["confundir la solución con el efecto", "no mencionar el número de árboles"], "Reconoce lo que identificó y muestra la diferencia entre solución (lo que se hace) y efecto (lo que resulta)."),
    "Relee el texto del puente y subraya la causa con un color y el efecto con otro.",
    "Escribe en español una causa y un efecto de algo que te pasó esta semana.",
)
