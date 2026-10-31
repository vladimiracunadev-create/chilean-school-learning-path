"""Cuaderno del estudiante, 6.º básico Inglés (propuesta): EN06 OA 13 (escribir textos con modelo y apoyo visual).

Los textos en inglés son originales, breves y llevan pista en español. Cada palabra o estructura se enseña en la propia clase
antes de usarla. Todos los modelos que una pregunta menciona están escritos dentro del enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA13 = "EN06 OA 13"


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


# ================================================================ OA 13 clase 1: email y postal
lesson(
    OA13, 1,
    "Los modelos de email y postal escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir un email y una postal para contar información de un viaje o una actividad, siguiendo un modelo. Sirve para compartir lo que vivo con personas que están lejos.",
    ["Sé escribir oraciones cortas en inglés.", "Conozco palabras como trip, beach y weather."],
    [
        "Un email (correo electrónico) tiene asunto (Subject), saludo, mensaje y despedida con tu nombre. Una postal (postcard) es una tarjeta breve que se envía desde un lugar de visita. Ambas cuentan información con el propósito de compartir una experiencia: dónde estás, qué haces y cómo es el clima (weather).",
        "Modelo de postal: «Dear Grandma, I am in Valdivia. The river is beautiful. We eat fresh fish and the weather is rainy. See you soon! Love, Camila.» Modelo de email: «Subject: Our school trip. Hi Pedro, Today we visited the museum. It was big and interesting. I took many photos. Best wishes, Rosa.»",
        "Cuando escribes, mira el modelo y sigue el mismo orden: saludo, dos a cuatro oraciones con la información, despedida. El apoyo visual puede ser una foto o un dibujo que acompañe tu mensaje; si no tienes uno, dibuja el lugar. No uses direcciones reales ni datos privados.",
    ],
    [("Dear… / Hi…", "Querido(a)… / Hola…"), ("subject", "asunto"), ("postcard", "postal"), ("weather", "clima"), ("rainy / sunny", "lluvioso / soleado"), ("See you soon!", "¡Hasta pronto!"), ("Love, / Best wishes,", "Con cariño, / Saludos,")],
    [
        ("Identificar el propósito", "Postal: «Dear Grandma, I am at the beach. The sea is warm. We play with a ball. Love, Ana.» ¿Qué comparte Ana?", ["Lee dónde está y qué hace.", "Cuenta su día en la playa.", "El propósito es compartir información de su visita."], "Dónde está y qué hace en la playa"),
        ("Ordenar las partes", "Ordena: a) Love, Ana. b) The sea is warm. c) Dear Grandma, Escribe las letras en orden.", ["Primero va el saludo.", "Luego el mensaje.", "Al final la despedida."], "c, b, a"),
    ],
    [
        ("Escribir la postal sin saludo ni despedida.", "Se cree que basta con el mensaje.", "Sigue el modelo: saludo, mensaje y despedida."),
        ("Poner una dirección real en el texto.", "Se copia un dato personal.", "Usa nombres y lugares inventados o generales."),
    ],
    [
        ("¿Qué es un «postcard»?", "Una postal", "Es una tarjeta breve enviada desde un lugar."),
        ("¿Qué significa «weather»?", "Clima", "Dice si hace sol, frío o lluvia."),
        ("¿Cuál es la despedida: «Dear Grandma,» o «See you soon!»?", "See you soon!", "Dear Grandma abre el texto."),
    ],
    [
        ("En el modelo de email, ¿cuál es el asunto?", "Our school trip", "Después de Subject dice Our school trip."),
        ("En el modelo de postal, ¿cómo está el clima en Valdivia?", "Rainy", "El texto dice the weather is rainy."),
        ("En el modelo de email, ¿qué hizo Rosa hoy?", "Visitó el museo", "Today we visited the museum."),
    ],
    [
        ("Completa la postal: «Dear Tom, I am in the mountains. The air is ___.» Opciones: cold, hot. (Hay nieve en la montaña.)", "cold", "La nieve indica frío."),
        ("Completa la despedida: «See you ___!» Opciones: soon, fish.", "soon", "See you soon es hasta pronto."),
        ("Completa el email: «Subject: ___ ». El mensaje cuenta una fiesta de cumpleaños. Opciones: My party, Rainy.", "My party", "El asunto resume el tema del mensaje."),
    ],
    [
        ("Una postal dice: «The museum is big and interesting.» ¿Es una información o una pregunta?", "Información", "La oración afirma cómo es el museo."),
        ("¿Qué falta en este texto? «Hi Pedro, Today we visited the museum.» Opciones: la despedida, el saludo.", "La despedida", "Tiene saludo pero no cierra con nombre."),
    ],
    [
        ("Conteo: en el modelo de postal («Dear Grandma, I am in Valdivia. The river is beautiful. We eat fresh fish and the weather is rainy. See you soon! Love, Camila.») ¿cuántas oraciones tiene el mensaje, sin contar saludo ni despedida?", "3", "Son I am in Valdivia, The river is beautiful y We eat fresh fish and the weather is rainy."),
        ("En ese modelo, ¿quién escribe la postal?", "Camila", "La firma al final dice Camila."),
    ],
    [("Eres Felipe y visitas un volcán con tu curso. Quieres contárselo a tu abuela en una postal. ¿Qué saludo usas? a) Dear Grandma, b) Subject:", "a", "Dear Grandma abre una postal personal.")],
    [
        ("¿Qué partes tiene un email?", "Asunto, saludo, mensaje y despedida", "Es la estructura del modelo."),
        ("¿Qué significa «Best wishes»?", "Saludos", "Es una despedida amable."),
        ("¿Para qué sirve el apoyo visual?", "Para acompañar el mensaje con una imagen", "Una foto o un dibujo muestran el lugar."),
    ],
    task("Lee estos modelos: «Dear Grandma, I am in Valdivia. The river is beautiful. We eat fresh fish and the weather is rainy. See you soon! Love, Camila.» y «Subject: Our school trip. Hi Pedro, Today we visited the museum. It was big and interesting. I took many photos. Best wishes, Rosa.» Elige uno de estos viajes inventados: un día en el campo, una visita al zoológico o un fin de semana en la playa. Escribe en tu hoja una postal o un email con saludo, tres oraciones y despedida, y dibuja una imagen pequeña del lugar como apoyo visual.", "Subject: My day in the country. Hi Luis, I am in the country. The air is fresh. We see horses. See you soon, Ana. (con dibujo de un caballo)", ["tiene saludo, mensaje de tres oraciones y despedida", "cuenta información coherente con el lugar elegido", "incluye un dibujo como apoyo visual"], ["hoja con texto y dibujo"], ["olvidar la despedida", "poner datos privados"], "Pide que lea el texto en voz alta y diga a quién se lo enviaría."),
    "Copia el modelo de postal y subraya el saludo y la despedida.",
    "Escribe un email de respuesta a Rosa contando un paseo que hiciste con tu curso.",
)

# ================================================================ OA 13 clase 2: agenda e invitación
lesson(
    OA13, 2,
    "Los modelos de agenda e invitación escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a leer y escribir una agenda semanal y una invitación a un evento escolar. Sirve para informar a otras personas qué pasa, cuándo y dónde.",
    ["Conozco los días de la semana en inglés.", "Sé decir la hora con a.m. y p.m."],
    [
        "Una agenda semanal es una lista que ordena actividades por día: «Monday: Math test at 9 a.m.» La invitación avisa de un evento e incluye el qué (event), el cuándo (date y time), el dónde (place) y quién invita. Palabras útiles: You are invited to… (estás invitado a…), Please come! (¡por favor ven!) y RSVP (confirma tu asistencia).",
        "Para localizar información usa palabras clave: What? es el evento, When? es el día y la hora, Where? es el lugar. Modelo: «You are invited to our Science Fair! Date: Friday, May 10. Time: 3 p.m. Place: school gym. Please come! Class 6A.» Aquí What es Science Fair, When es Friday a las 3 p.m. y Where es school gym.",
        "Con los días se usa on (on Friday); con las horas, at (at 3 p.m.); con lugares cerrados, in o at (at the gym). En la agenda no se escriben oraciones largas: basta con el día, la actividad y la hora.",
    ],
    [("agenda", "lista de actividades por día"), ("event", "evento"), ("date / time / place", "fecha / hora / lugar"), ("You are invited to…", "Estás invitado a…"), ("Science Fair", "feria de ciencias"), ("gym", "gimnasio"), ("RSVP", "confirma tu asistencia")],
    [
        ("Localizar el cuándo", "Invitación: «You are invited to our Art Show! Date: Thursday. Time: 11 a.m. Place: school hall. Please come!» ¿Cuándo es el evento?", ["Busco When: día y hora.", "Date dice Thursday.", "Time dice 11 a.m."], "El jueves a las 11 a.m."),
        ("Detectar el dato que falta", "Invitación: «You are invited to our Music Show on Friday at the gym. Please come!» ¿Qué dato falta?", ["Hay evento: Music Show.", "Hay día y lugar.", "No hay hora."], "La hora"),
    ],
    [
        ("Omitir el lugar de la invitación.", "Se cree que quien lee ya lo sabe.", "Revisa What, When y Where antes de enviar."),
        ("Escribir «at Friday».", "Se usa at con un día.", "Con días se usa on."),
    ],
    [
        ("¿Qué significa «place» en una invitación?", "Lugar", "Dice dónde ocurre el evento."),
        ("¿Qué significa «You are invited to…»?", "Estás invitado a…", "Abre una invitación."),
        ("¿Qué día es «Friday»?", "Viernes", "Es el último día de la semana escolar."),
    ],
    [
        ("Agenda: «Monday: Math test at 9 a.m. Wednesday: Art club at 2 p.m. Friday: Science Fair at 3 p.m.» ¿A qué hora es la feria de ciencias?", "3 p.m.", "La línea de Friday dice 3 p.m."),
        ("En esa agenda, ¿qué día es el Art club?", "Wednesday", "La línea de Wednesday menciona el Art club."),
        ("Invitación: «Science Fair. Date: Friday, May 10. Place: school gym.» ¿Dónde es?", "En el gimnasio de la escuela", "Place dice school gym."),
    ],
    [
        ("Completa con on o at: «The show is ___ Thursday.»", "on", "Con días se usa on."),
        ("Completa con on o at: «The show starts ___ 11 a.m.»", "at", "Con horas se usa at."),
        ("Completa: «Please ___!» para pedir que alguien asista. Opciones: come, eat.", "come", "Please come significa por favor ven."),
    ],
    [
        ("Una invitación dice: «You are invited to our Sports Day. Date: Tuesday. Place: school field.» ¿Qué le falta? a) la hora b) el lugar", "a", "Tiene fecha y lugar, pero no hora."),
        ("En una agenda la línea «Tuesday: Library» ¿qué dato no tiene? a) El día b) La hora", "b", "Tiene día y actividad, pero no hora."),
    ],
    [
        ("Una agenda tiene: lunes 9 a.m. Math, martes 10 a.m. Art, viernes 3 p.m. Music. ¿Cuántas actividades tiene la semana?", "3", "Hay una actividad por línea."),
        ("El evento empieza a las 3 p.m. y dura 2 horas. ¿A qué hora termina? Escribe solo el número (p.m.).", "5", "Se suman las horas: 3 + 2 = 5."),
    ],
    [("Tu curso invita a las familias a un desfile (parade) el miércoles a las 10 a.m. en el patio. ¿Cuál es el Where? a) The school yard b) Wednesday", "a", "Where pregunta el lugar, que es el patio (yard).")],
    [
        ("¿Qué tres datos lleva una invitación?", "Fecha, hora y lugar", "Se necesita saber cuándo y dónde."),
        ("¿Qué preposición va con los días?", "on", "Se dice on Monday."),
        ("¿Qué indica «p.m.»?", "Después del mediodía", "Las 3 p.m. son las 3 de la tarde."),
    ],
    task("Lee este modelo: «You are invited to our Science Fair! Date: Friday, May 10. Time: 3 p.m. Place: school gym. Please come! Class 6A.» Escribe en tu hoja una agenda de tres días con actividades escolares y horas, y una invitación a un evento de tu curso (Sports Day, Book Fair o Music Show) con What, When, Where y Please come. Dibuja un pequeño cartel como apoyo visual.", "Agenda: Monday: Math at 9 a.m. Tuesday: Art at 10 a.m. Friday: Book Fair at 3 p.m. Invitación: You are invited to our Book Fair! Date: Friday. Time: 3 p.m. Place: school library. Please come! Class 6B.", ["la agenda tiene día, actividad y hora", "la invitación incluye evento, fecha, hora y lugar", "usa on con días y at con horas"], ["hoja con agenda, invitación y cartel"], ["omitir el lugar o la hora", "usar at con un día"], "Marca con un visto cada dato y pide que complete solo el que falte."),
    "Copia la invitación modelo y subraya el evento, la fecha, la hora y el lugar.",
    "Escribe una invitación para una familia con un evento de tu elección y añade una línea RSVP.",
)

# ================================================================ OA 13 clase 3: noticias
lesson(
    OA13, 3,
    "Los modelos de noticia escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir una noticia breve con titular y datos de qué, quién, dónde y cuándo. Sirve para informar con claridad sobre algo que pasó en mi escuela.",
    ["Sé escribir oraciones en presente y en pasado simple.", "Conozco las preguntas What, Who, Where y When."],
    [
        "Una noticia (news) cuenta un hecho real de forma clara y breve. Empieza con un titular (headline) corto, que resume la noticia. Luego va una primera oración con los datos principales: qué pasó (what), quién participó (who), dónde (where) y cuándo (when). Después se agregan uno o dos detalles.",
        "Modelo: «Headline: Students Collect 200 Bottles. Last Friday, the students of 6B collected 200 plastic bottles in the school yard. They want to recycle them. The teacher says: Great work!» Los hechos pasados se escriben en pasado: collected (recogieron), visited (visitaron), won (ganaron).",
        "El titular no termina con punto, suele omitir palabras pequeñas y suele ir en presente: School Team Wins Chess Tournament. Evita opiniones fuertes y escribe solo datos que puedas comprobar. Apoyo visual: una foto o un dibujo con una frase corta debajo (a caption).",
    ],
    [("news", "noticia"), ("headline", "titular"), ("what / who / where / when", "qué / quién / dónde / cuándo"), ("caption", "pie de foto"), ("collected", "recogieron"), ("recycle", "reciclar"), ("won", "ganó / ganaron")],
    [
        ("Localizar el quién", "Noticia: «Last Monday, the students of 6A planted ten trees in the park.» ¿Quién participó?", ["Busco who.", "La oración empieza con the students of 6A.", "Esos son los participantes."], "Los estudiantes de 6A"),
        ("Elegir un titular", "Noticia: «On Tuesday, our school team won the chess tournament.» ¿Cuál titular sirve? a) School Team Wins Chess Tournament b) Chess is Boring", ["El titular resume el hecho.", "La opción a dice qué pasó.", "La opción b es una opinión."], "a"),
    ],
    [
        ("Escribir un titular largo con punto final.", "Se escribe como una oración común.", "El titular es breve y no lleva punto."),
        ("Agregar opiniones sin datos.", "Se mezclan gustos con hechos.", "Escribe solo qué, quién, dónde y cuándo."),
    ],
    [
        ("¿Qué es un «headline»?", "Un titular", "Resume la noticia en pocas palabras."),
        ("¿Qué significa «where» en una noticia?", "Dónde", "Pregunta el lugar del hecho."),
        ("¿Qué significa «collected»?", "Recogieron", "Es el pasado de collect."),
    ],
    [
        ("Noticia: «Last Friday, the students of 6B collected 200 plastic bottles in the school yard.» ¿Dónde ocurrió?", "En el patio de la escuela", "In the school yard indica el lugar."),
        ("En esa noticia, ¿cuándo ocurrió?", "El viernes pasado", "Last Friday indica el tiempo."),
        ("En esa noticia, ¿cuántas botellas recogieron?", "200", "El número aparece antes de plastic bottles."),
    ],
    [
        ("Completa: «Last Monday, we ___ twelve flowers.» Opciones: planted, plant. (Ocurrió el lunes pasado.)", "planted", "Last Monday pide el pasado, planted."),
        ("Completa el qué: «Headline: Ana ___ the Race.» Opciones: wins, win.", "wins", "El sujeto Ana es una sola persona, así que lleva wins."),
        ("Escribe el dónde: «The students planted trees in the ___.» Opciones: park, Monday.", "park", "Park es un lugar."),
    ],
    [
        ("¿Cuál oración es un dato comprobable? a) The match was great. b) Our team won 3 to 1.", "b", "Un resultado se puede comprobar."),
        ("En «Yesterday our school team won», ¿qué dato entrega la palabra Yesterday? a) cuándo b) dónde", "a", "Yesterday indica el tiempo del hecho."),
    ],
    [
        ("Si 6B recogió 120 botellas el lunes y 80 el martes, ¿cuántas recogió en total? Escribe solo el número.", "200", "Se suman: 120 + 80 = 200."),
        ("Ordena los datos de la noticia: when, headline, what. ¿Cuál va primero en el texto?", "headline", "El titular abre la noticia."),
    ],
    [("Tu curso ganó un partido de básquetbol el sábado pasado en el gimnasio. ¿Cuál es el when? a) Last Saturday b) In the gym", "a", "When pregunta el tiempo.")],
    [
        ("¿Qué cuatro preguntas responde la primera oración de una noticia?", "Qué, quién, dónde y cuándo", "Son los datos principales."),
        ("¿Qué es un pie de foto?", "Una frase corta bajo la imagen", "Se llama caption."),
        ("¿Cómo se dice «ganó» en pasado?", "won", "Won es el pasado de win."),
    ],
    task("Lee este modelo: «Headline: Students Collect 200 Bottles. Last Friday, the students of 6B collected 200 plastic bottles in the school yard. They want to recycle them.» Escribe en tu hoja una noticia inventada con uno de estos hechos: tu curso plantó árboles, ganó un partido o ayudó en un acto. Incluye titular, una oración con qué, quién, dónde y cuándo, y un detalle. Dibuja una imagen con su pie de foto.", "Headline: Class 6A Plants Ten Trees. Last Monday, the students of 6A planted ten trees in the park. They want to help the environment. (Caption: Ten new trees.)", ["titular breve sin punto", "incluye qué, quién, dónde y cuándo", "usa el pasado de un verbo"], ["hoja con noticia y dibujo con pie de foto"], ["escribir opiniones sin datos", "omitir el dónde"], "Pregunta qué dato cambiaría si la noticia fuera de ayer."),
    "Copia el titular modelo y subraya el qué y el quién de la primera oración.",
    "Escribe una noticia de tres oraciones sobre un campeonato deportivo escolar con datos inventados.",
)

# ================================================================ OA 13 clase 4: cuentos y tiras cómicas
lesson(
    OA13, 4,
    "Los modelos de cuento y tira cómica escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir un cuento corto con comienzo, nudo y final, y una tira cómica con diálogos. Sirve para compartir una historia con ideas ordenadas.",
    ["Conozco first, then y finally.", "Sé escribir oraciones simples en pasado."],
    [
        "Un cuento (story) tiene personajes (characters), lugar (setting) y un orden: comienzo, nudo (un problema) y final (la solución). Se ordenan los hechos con first, then, next y finally. Modelo: «First, Lucas lost his hat at the beach. Then he looked behind a rock. Finally, he found it and smiled.»",
        "Una tira cómica (comic strip) cuenta una historia en cuadros. Cada cuadro (panel) tiene un dibujo y globos de diálogo (speech balloons). Se escribe «Panel 1:» y lo que dice cada personaje entre comillas. Modelo: «Panel 1: Mía: I can't find my pencil! Panel 2: Leo: Look, it's under the table! Panel 3: Mía: Thank you!»",
        "Los verbos del pasado: lost (perdió), looked (miró), found (encontró), smiled (sonrió), said (dijo). Lost, found y said son irregulares: no terminan en -ed. El apoyo visual en la tira son los dibujos; en el cuento puede ser un dibujo del problema. No copies un cuento conocido: inventa uno propio.",
    ],
    [("story", "cuento"), ("character", "personaje"), ("panel", "cuadro de una tira"), ("speech balloon", "globo de diálogo"), ("lost / found", "perdió / encontró"), ("first, then, finally", "primero, luego, finalmente"), ("look, it's under the table", "mira, está bajo la mesa")],
    [
        ("Identificar el problema del cuento", "Cuento: «First, Lucas lost his hat at the beach. Then he looked behind a rock. Finally, he found it.» ¿Cuál es el problema?", ["Busco qué sale mal al comienzo.", "Lucas perdió su sombrero.", "Eso es el problema."], "Que Lucas perdió su sombrero"),
        ("Ordenar un cuento", "Ordena: a) Finally, they found a dog. b) First, Ana and Sam walked in the park. c) Then they heard a sound. Escribe las letras en orden.", ["First abre el cuento.", "Then va después del comienzo.", "Finally cierra el cuento."], "b, c, a"),
    ],
    [
        ("Escribir un cuento sin problema ni final.", "Solo se describe sin que ocurra algo.", "Incluye un problema y cómo se resuelve."),
        ("Escribir los diálogos de la tira sin decir quién habla.", "No se indica el personaje.", "Escribe el nombre del personaje antes de cada diálogo."),
    ],
    [
        ("¿Qué significa «finally»?", "Finalmente", "Indica el último hecho."),
        ("¿Qué es un «panel» en una tira cómica?", "Un cuadro de la tira", "Cada cuadro tiene un dibujo y diálogos."),
        ("¿Qué significa «found»?", "Encontró", "Es el pasado de find."),
    ],
    [
        ("Tira: «Panel 1: Mía: I can't find my pencil! Panel 2: Leo: Look, it's under the table! Panel 3: Mía: Thank you!» ¿Qué buscaba Mía?", "Su lápiz", "Mía dice que no encuentra su pencil."),
        ("En esa tira, ¿dónde estaba lo que buscaba?", "Bajo la mesa", "Leo dice under the table."),
        ("En esa tira, ¿en qué panel dice Leo dónde está el lápiz?", "El panel 2", "Leo da la pista en el segundo cuadro."),
    ],
    [
        ("Completa: «First, Ana ___ her book.» Opciones: lost, lose. (Es un hecho pasado.)", "lost", "En el pasado se usa lost."),
        ("Completa: «Finally, Tom ___ his keys.» Opciones: found, finds. (Es un hecho pasado.)", "found", "Found es el pasado de find."),
        ("Completa el globo: «Panel 2: Sam: ___, it's on the chair!» Opciones: Look, Under.", "Look", "Look, it's… sirve para señalar algo."),
    ],
    [
        ("Un cuento termina con «Then she ran away and nothing happened.» ¿Tiene un buen final? Responde sí o no.", "No", "No resuelve el problema."),
        ("¿Cuál va primero en un cuento: first o finally?", "first", "First abre la secuencia."),
    ],
    [
        ("Un cuento tiene cuatro hechos: First, Then, Next y Finally. ¿Cuántos hechos hay antes de Finally?", "3", "First, Then y Next vienen antes."),
        ("Una tira tiene 4 paneles y cada panel tiene 2 diálogos. ¿Cuántos diálogos hay en total? Escribe solo el número.", "8", "Se suman 2 diálogos en cada uno de 4 paneles: 4 × 2 = 8."),
    ],
    [("Escribes una tira sobre un perro perdido. Quieres que un personaje diga «Encuentro mi perro». ¿Qué globo usas? a) Panel 3: Ana: I found my dog! b) Panel 3: Ana: I lost my dog!", "a", "Found significa encontré.")],
    [
        ("¿Qué partes tiene un cuento?", "Comienzo, nudo y final", "Ordenan la historia."),
        ("¿Qué son los speech balloons?", "Globos de diálogo", "Muestran lo que dice cada personaje."),
        ("¿Cómo se dice «perdió» en inglés?", "lost", "Es el pasado de lose."),
    ],
    task("Lee este modelo de cuento: «First, Lucas lost his hat at the beach. Then he looked behind a rock. Finally, he found it and smiled.» y este de tira: «Panel 1: Mía: I can't find my pencil! Panel 2: Leo: Look, it's under the table! Panel 3: Mía: Thank you!» Elige personajes y un problema (perder un balón, perder una llave o perder un gato). Escribe en tu hoja un cuento de tres oraciones y una tira de tres paneles. Dibuja los paneles.", "Cuento: First, Sam lost his ball. Then he looked behind the tree. Finally, he found it. Tira: Panel 1: Sam: I can't find my ball! Panel 2: Ana: Look, it's behind the tree! Panel 3: Sam: Thank you!", ["el cuento tiene comienzo, problema y final con first, then y finally", "la tira tiene tres paneles con diálogos y personajes", "usa pasado en el cuento"], ["hoja con cuento y tira dibujada"], ["no resolver el problema", "no indicar quién habla"], "Pide que lea la tira por turnos con una persona de su casa."),
    "Copia los tres hechos del modelo de cuento y subraya first, then y finally.",
    "Escribe una tira cómica de cuatro paneles con un problema y su solución.",
)

# ================================================================ OA 13 clase 5: rimas y texto independiente
lesson(
    OA13, 5,
    "Los modelos de rima y las opciones de texto escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir una rima y a elegir por mi cuenta el tipo de texto según lo que quiero compartir. Sirve para decidir cómo contar mis ideas.",
    ["Conozco las partes del email, la invitación, la noticia, el cuento y la tira cómica.", "Sé que dos palabras riman cuando terminan con el mismo sonido."],
    [
        "Una rima (rhyme) es un texto corto que repite sonidos al final de las líneas. Hay pares como cat y hat, sun y fun, tree y see. Modelo: «I like my hat. It is very flat. I wear it with my cat. That is that!» (flat y cat riman con hat). Cada línea es corta y tiene ritmo.",
        "Para escribir sin ayuda decide primero tu propósito y a quién va dirigido (audience). Si quieres avisar de un evento, escribe una invitación; si quieres contar un viaje, una postal; si quieres dar un dato real, una noticia; si quieres entretener, un cuento, una rima o una tira.",
        "Después usa el modelo de ese tipo de texto, escribe tu versión, y revisa con una lista: tiene todas sus partes, usa palabras del tema, la ortografía es correcta (I con mayúscula) y se entiende. Pide ayuda del diccionario solo si lo necesitas.",
    ],
    [("rhyme", "rima"), ("cat / hat", "gato / sombrero (riman)"), ("sun / fun", "sol / diversión (riman)"), ("purpose", "propósito: para qué escribo"), ("audience", "destinatario: quién lo lee"), ("checklist", "lista de revisión")],
    [
        ("Encontrar rimas", "Palabras: hat, dog, cat, tree. ¿Cuál rima con «bat»?", ["Bat termina en -at.", "Hat y cat también.", "Pero debo elegir una: hat o cat."], "hat o cat"),
        ("Elegir el tipo de texto", "Quieres avisar a tu curso que el viernes habrá un campeonato de fútbol. ¿Qué texto escribes? Opciones: invitación, rima.", ["Quieres avisar un evento.", "Una invitación lleva cuándo y dónde.", "Eso sirve para avisar."], "Una invitación"),
    ],
    [
        ("Escribir rimas que no suenan igual al final.", "Se confunde la escritura con el sonido.", "Lee en voz alta para comprobar que suenan igual."),
        ("Elegir un tipo de texto sin pensar en el propósito.", "Se escribe lo primero que se ocurre.", "Piensa: ¿qué quiero lograr y para quién escribo?"),
    ],
    [
        ("¿Cuál palabra rima con «sun»? Opciones: fun, dog.", "fun", "Sun y fun terminan en -un."),
        ("¿Qué significa «audience»?", "Destinatario o quien lee", "Es la persona o grupo a quien va el texto."),
        ("¿Qué significa «rhyme»?", "Rima", "Es un texto corto con sonidos finales que se repiten."),
    ],
    [
        ("Quieres contar a tu abuela cómo es tu viaje al sur. ¿Qué texto eliges? a) postal b) invitación", "a", "Una postal comparte la experiencia de un lugar."),
        ("Modelo: «I like my hat. It is very flat. I wear it with my cat.» ¿Qué palabras riman con hat?", "flat y cat", "Terminan igual en -at."),
        ("Quieres informar que tu curso ganó un partido ayer. ¿Qué texto eliges? a) noticia b) rima", "a", "Una noticia informa un hecho real."),
    ],
    [
        ("Completa para rimar: «The sun is hot, we have ___.» Opciones: fun, dog.", "fun", "Sun y fun riman."),
        ("Completa para rimar: «I see a tree, look at ___.» Opciones: me, sun. (me = mí)", "me", "Tree y me riman."),
        ("Elige el propósito: quieres compartir un chiste con tu curso. ¿Qué texto eliges? a) rima o tira cómica b) invitación", "a", "Una rima o una tira entretienen."),
    ],
    [
        ("Alguien escribió: «I love my cat. He sits on a mat.» ¿Riman las líneas? Responde sí o no.", "Sí", "Cat y mat terminan en -at."),
        ("Alguien escribió: «I like to run. It is fun.» ¿Riman las líneas?", "Sí", "Run y fun terminan igual."),
    ],
    [
        ("¿Qué par de palabras rima? a) bee y tree b) bee y bed", "a", "Bee y tree terminan con el mismo sonido."),
        ("Rima: «I see a bee. It sits on a tree. It sings to me.» ¿Cuántas líneas terminan con el sonido -ee? Escribe solo el número.", "3", "Bee, tree y me terminan igual."),
    ],
    [("Tienes que invitar a tu curso a una competencia de ajedrez el jueves a las 3 p.m. en la biblioteca. ¿Qué tipo de texto sirve mejor? a) invitación b) rima", "a", "La invitación lleva fecha, hora y lugar.")],
    [
        ("¿Qué dos cosas decides antes de escribir sin ayuda?", "El propósito y el destinatario", "Así eliges el tipo de texto."),
        ("¿Qué palabra rima con «cat»?", "hat", "Hat y cat terminan en -at."),
        ("¿Qué revisas al final de tu texto?", "Partes, vocabulario y ortografía", "La lista de revisión guía la corrección."),
    ],
    task("Lee este modelo: «I like my hat. It is very flat. I wear it with my cat. That is that!» Elige uno de estos propósitos: 1) invitar a tu curso a un campeonato, 2) contar un paseo a tu abuelo, 3) divertir con una rima. Escribe en tu hoja el texto que corresponda, con las partes de su tipo, y revisa con esta lista: ¿tiene todas sus partes?, ¿usa vocabulario del tema?, ¿escribí I con mayúscula?, ¿se entiende?", "Propósito 3: I see a bee. It sits on a tree. It sings to me. It is free!", ["el tipo de texto calza con el propósito", "tiene todas las partes de ese texto", "revisó con la lista y corrigió"], ["hoja con el texto y la lista marcada"], ["no riman las líneas", "no calza el texto con el propósito"], "Pide que explique por qué eligió ese tipo de texto y no otro."),
    "Escribe cinco pares de palabras que riman, como cat y hat.",
    "Elige un propósito distinto al que usaste y escribe otro texto con el modelo correspondiente.",
)
