"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 10: conocimiento y uso del lenguaje en conversaciones,
discusiones y exposiciones (funciones del año).

Diálogos y textos originales y ficticios, con pista en español; todo lo que una pregunta nombra está escrito en el enunciado.
Los títulos de clase del plan son genéricos; aquí cada clase trabaja un grupo de funciones del OA: expresiones de uso común,
sinónimos y palabras compuestas; frecuencia, tiempo y grado (incluido has been working); acciones anteriores en el pasado y
descripción de lugares y personas; confirmar, sugerir, ofrecer y opinar; y conectar ideas, enfatizar e informar lo que otros dicen.
La producción oral real se evalúa con las tareas abiertas y una persona que escucha.
"""
from __future__ import annotations

from en_m2_a_common import MAT_SPEAK, arith, lesson, task

OA = "EN2M OA 10"

# ================================================== clase 1: expresiones comunes, sinónimos y compuestas
D1 = "«Nico: Have you seen Marta lately? Rita: Hardly ever. I have known her for ages, but she is busy. Nico: Is she looking for a job? Rita: Not at all. She is looking after her little brother this month. Nico: I’m pleased to hear that. Sorry about the noise, by the way. Rita: No problem. I’d rather study at home than go to the library. Nico: The new notebook is cheap enough. I bought it online.»\n(lately = últimamente, for ages = desde hace mucho, looking for = buscando, not at all = para nada, looking after = cuidando, pleased = contento, noise = ruido, cheap = barato, bought = compré, online = en línea)"
D2 = "«Ana: What do you do on Sundays? Leo: I usually stay at home. I do not go out much. I hardly ever watch television. Ana: Sorry about last week! I could not come. Leo: Don’t worry. I’m pleased that you called. Ana: I’d rather meet on Saturday. It is a good day. We can have a snack in the school playground.»\n(stay = quedarse, go out = salir, television = televisión, could not = no pude, called = llamaste, snack = merienda, playground = patio)"

lesson(
    OA, 1, MAT_SPEAK,
    "Aprenderé a expresarme con claridad usando palabras y expresiones de uso común (hardly ever, at all, I’d rather, for ages, I’m pleased, sorry about, look for, look after, cheap enough, online), sinónimos y palabras compuestas. Sirve para sonar natural en una conversación y en una discusión.",
    ["Sé el presente simple y los adverbios de frecuencia.", "Sé que una palabra puede tener un sinónimo."],
    [
        "Muchas expresiones comunes se aprenden como una unidad. Hardly ever significa casi nunca; not at all significa para nada; for ages significa desde hace mucho; I’m pleased significa me alegra; Sorry about… significa lamento lo de…; I’d rather… significa prefiero… Los verbos con preposición cambian el sentido: look for es buscar, look after es cuidar. Cheap enough es lo bastante barato, y online significa en línea.",
        "Los sinónimos (synonyms) te ayudan a no repetir palabras: pleased y happy, cheap y inexpensive, hardly ever y rarely, big y large. Las palabras compuestas (compound words) unen dos palabras: notebook, playground, classmate, homework, online. El significado de la compuesta suele salir de sus partes: play + ground, a place to play. Acentúa la primera parte: PLAYground.",
        "Para expresarte con claridad, usa frases cortas y seguras. Primero elige la expresión adecuada a la situación: para disculparte (Sorry about…), para preferir (I’d rather…), para agradecer o alegrarte (I’m pleased…). Después agrega tu información. Si no recuerdas una palabra, usa un sinónimo o explica con otras palabras.",
    ],
    [("hardly ever", "casi nunca"), ("not at all", "para nada"), ("for ages", "desde hace mucho"), ("I’m pleased", "me alegra"), ("look for / look after", "buscar / cuidar"), ("cheap enough", "lo bastante barato")],
    [
        ("Elegir expresión", "Quieres decir «casi nunca voy al cine». ¿Qué frase usas? A) I hardly ever go to the cinema. B) I always go to the cinema.", ["Hardly ever es casi nunca.", "La A.", "La B es lo contrario."], "A"),
        ("Verbo con preposición", "¿Qué significa look after? A) cuidar B) buscar", ["Look after es cuidar.", "Look for es buscar.", "La A."], "A"),
    ],
    [
        ("Traducir hardly ever como mucho.", "Hardly significa poco, no mucho.", "Recuerda que hardly ever es casi nunca."),
        ("Confundir look for con look after.", "Cambia el sentido del verbo.", "For se relaciona con buscar y after con cuidar."),
    ],
    [
        ("Lee: " + D1 + " ¿Con qué frecuencia ve Nico a Marta? A) casi nunca B) todos los días", "A", "Rita responde Hardly ever."),
        ("Lee: " + D1 + " ¿A quién cuida Marta este mes? A) a su hermano pequeño B) a su abuela", "A", "Dice looking after her little brother."),
        ("Lee: " + D1 + " ¿Cómo compró Nico el cuaderno? A) en línea B) en una tienda", "A", "Dice I bought it online."),
    ],
    [
        ("Lee: " + D1 + " ¿Qué significa Not at all? A) para nada B) por supuesto", "A", "Rita responde que Marta no busca trabajo."),
        ("Lee: " + D2 + " ¿Qué prefiere Ana? A) juntarse el sábado B) juntarse el domingo", "A", "Dice I’d rather meet on Saturday."),
        ("Lee: " + D2 + " ¿De qué se disculpa Ana? A) de no haber podido venir la semana pasada B) de haber llegado tarde hoy", "A", "Dice Sorry about last week! I could not come."),
    ],
    [
        ("Lee: " + D1 + " ¿Qué significa cheap enough? A) lo bastante barato B) demasiado caro", "A", "Enough indica suficiente."),
        ("Lee: " + D2 + " ¿Con qué frecuencia mira televisión Leo? A) casi nunca B) a menudo", "A", "Dice I hardly ever watch television."),
        ("Lee: " + D1 + " ¿Desde hace cuánto conoce Rita a Marta? A) desde hace mucho tiempo B) desde ayer", "A", "Dice I have known her for ages."),
    ],
    [
        ("Lee: " + D1 + " ¿Qué prefiere hacer Rita? A) estudiar en casa en vez de ir a la biblioteca B) ir a la biblioteca", "A", "Dice I’d rather study at home than go to the library."),
        ("Lee: " + D2 + " Un compañero dice que a Leo le gusta salir mucho. ¿Qué lo corrige? A) dice I do not go out much B) dice I stay at home", "A", "Do not go out much indica que sale poco."),
    ],
    [
        ("Une la palabra compuesta con su significado. 1) classmate 2) homework 3) playground. Significados: a) tarea para la casa b) patio de juegos c) compañero de clase", "1-c, 2-a, 3-b", "Cada compuesta combina dos palabras."),
        ("Elige el sinónimo de pleased: A) happy B) angry", "A", "Pleased y happy son parecidas."),
    ],
    [("Lee: «Lía: My grandmother lives far away, so I call her every week. I’m pleased when she answers. I look after her cat when she travels.» ¿Qué cuida Lía cuando su abuela viaja?", "Al gato de su abuela", "Dice I look after her cat.")],
    [
        ("¿Qué significa hardly ever?", "Casi nunca", "Expresa una frecuencia baja."),
        ("¿Cómo se dice «prefiero» en inglés?", "I’d rather", "Se usa con un verbo simple."),
        ("¿Qué significa online?", "En línea", "Es una palabra de uso común."),
    ],
    task("Escribe cinco oraciones sobre ti usando cinco de estas expresiones: hardly ever, not at all, for ages, I’m pleased, sorry about, I’d rather, look for, look after, cheap enough, online. Luego dilas en voz alta a una persona de tu casa como en una conversación.", "Ejemplo: I hardly ever eat late. I have known my best friend for ages. I’d rather watch a film than play a game. I’m pleased that it is Friday. I buy books online.", ["usa cinco expresiones correctas", "cada oración se entiende", "las lee con claridad"], ["hoja con cinco oraciones", "comentario de la persona que escuchó"], ["confundir look for con look after", "usar hardly ever como mucho"], "Pide a la persona que cuente cuántas expresiones reconoció."),
    "Escribe diez palabras compuestas que conozcas y su significado.",
    "Escribe un diálogo de cuatro líneas con tres de las expresiones de la clase.",
)

# ================================================== clase 2: frecuencia, tiempo y grado
INT1 = "«Interviewer: How often do you practise sports? Hana: I usually practise three times a week, but I sometimes miss a session. Interviewer: How long have you been playing volleyball? Hana: I have been playing for two years. Interviewer: Is it difficult? Hana: It is rather hard in the first weeks, but I am pretty good now. Interviewer: When is your next match? Hana: Soon. We play next Saturday.»\n(practise = practicar, miss = faltar, session = sesión, rather = bastante, pretty = bastante, match = partido)"
INT2 = "«Interviewer: Have you been working this summer? Matías: Yes, I have been working at a bakery since December. I usually start at six and finish at noon. Interviewer: How often do you work? Matías: Five days a week. Interviewer: Do you like it? Matías: I like it very much, though it is quite tiring. Interviewer: Will you continue in March? Matías: I will decide soon.»\n(summer = verano, bakery = panadería, since = desde, start = empezar, finish = terminar, tiring = cansador, continue = continuar, decide = decidir)"

lesson(
    OA, 2, MAT_SPEAK,
    "Aprenderé a preguntar y describir la frecuencia, el tiempo y el grado de las acciones, incluyendo el presente perfecto continuo (has been working). Sirve para conversar sobre rutinas, trabajos y actividades que duran un tiempo.",
    ["Sé los adverbios de frecuencia.", "Sé el presente continuo."],
    [
        "Para preguntar por la frecuencia se usa How often…? How often do you practise sports? Se responde con adverbios (always, usually, often, sometimes, rarely, never) o con expresiones como three times a week. Los adverbios suelen ir antes del verbo principal (I usually practise) y después de to be (She is often late). Para preguntar por la duración se usa How long…? How long have you been playing volleyball?",
        "El presente perfecto continuo (present perfect continuous) se forma con have/has + been + verbo con -ing. Se usa para una acción que empezó en el pasado y continúa hasta ahora: He has been working during the summer. I have been playing for two years. Se usa for con una duración (for two years) y since con el momento de inicio (since December).",
        "Para decir el grado (degree) se usan palabras como very, quite, rather y pretty: It is rather hard. Para el tiempo, soon, next Saturday y this month. Al conversar, escucha la pregunta y responde con la estructura correcta. Si te preguntan How often?, responde con una frecuencia; si te preguntan How long?, responde con for o since.",
    ],
    [("How often…?", "¿Con qué frecuencia…?"), ("How long…?", "¿Desde hace cuánto…?"), ("have been playing", "he estado jugando"), ("for", "durante (una duración)"), ("since", "desde (un momento)"), ("rather", "bastante")],
    [
        ("Pregunta", "Quieres saber cada cuánto va alguien al gimnasio. ¿Qué preguntas? A) How often do you go to the gym? B) How long is the gym?", ["Busco la frecuencia.", "How often pregunta cada cuánto.", "La A."], "A"),
        ("for o since", "Completa: «I have been studying English ___ 2022.» A) since B) for", ["2022 es un momento de inicio.", "Se usa since.", "La A."], "A"),
    ],
    [
        ("Usar for con un momento de inicio (for December).", "For se usa con duraciones y since con puntos de inicio.", "Escribe since December o for six months."),
        ("Olvidar been en el presente perfecto continuo.", "La estructura necesita have/has + been + -ing.", "Escribe have been working."),
    ],
    [
        ("Lee: " + INT1 + " ¿Con qué frecuencia practica Hana? A) tres veces por semana B) todos los días", "A", "Dice three times a week."),
        ("Lee: " + INT2 + " ¿Desde cuándo trabaja Matías en la panadería? A) desde diciembre B) desde marzo", "A", "Dice since December."),
        ("Lee: " + INT1 + " ¿Cuándo es su próximo partido? A) el próximo sábado B) mañana", "A", "Dice We play next Saturday."),
    ],
    [
        ("Lee: " + INT1 + " ¿Desde hace cuánto juega vóleibol? A) dos años B) dos meses", "A", "Dice for two years."),
        ("Lee: " + INT2 + " ¿Cuántos días a la semana trabaja? A) cinco B) siete", "A", "Dice Five days a week."),
        ("Lee: " + INT2 + " ¿Qué opina del trabajo? A) que le gusta, aunque es cansador B) que no le gusta", "A", "Dice I like it very much, though it is quite tiring."),
    ],
    [
        ("Lee: " + INT1 + " ¿Qué dice Hana sobre las primeras semanas? A) que fue bastante difícil B) que fue fácil", "A", "Dice It is rather hard in the first weeks."),
        ("Lee: " + INT2 + " ¿A qué hora termina de trabajar? A) al mediodía B) a las seis", "A", "Dice finish at noon."),
        ("Lee: " + INT1 + " ¿Qué estructura usa Hana para decir que sigue jugando desde hace dos años? A) I have been playing B) I played", "A", "El presente perfecto continuo muestra una acción que continúa."),
    ],
    [
        ("Lee: " + INT1 + " ¿Cuál es la pregunta que se responde con for two years? A) How long have you been playing? B) How often do you play?", "A", "Una duración se responde con for."),
        ("Lee: " + INT2 + " ¿Qué dice que hará pronto? A) decidir si continúa B) cambiar de trabajo", "A", "Dice I will decide soon."),
    ],
    [
        ("Completa: «She ___ been reading since breakfast.» A) has B) have", "A", "Con she se usa has."),
        ("Ordena de menos a más frecuente: a) never b) sometimes c) usually", "a, b, c", "Never es 0, sometimes es de vez en cuando y usually es lo habitual."),
    ],
    [arith("Teo ha estado aprendiendo piano desde marzo y practica cada día 20 minutos. ¿Cuántos minutos practica en una semana de siete días?", "20*7", "Se multiplican los minutos diarios por los siete días.")],
    [
        ("¿Cómo se forma el presente perfecto continuo (en Inglés, 2.º medio)?", "Have/has + been + verbo con -ing", "Muestra una acción que continúa."),
        ("¿Cuándo se usa since?", "Con el momento de inicio", "Por ejemplo, since December."),
        ("¿Cómo se pregunta por la frecuencia?", "How often…?", "Se responde con adverbios."),
    ],
    task("Entrevista a una persona de tu casa (o imagina las respuestas) con tres preguntas: una con How often, una con How long y una con grado (¿es difícil?). Escribe las preguntas y las respuestas en inglés, usando since o for, un adverbio de frecuencia y rather o quite.", "Ejemplo: How often do you cook? I usually cook on Sundays. How long have you been living here? I have been living here for ten years. Is it difficult? It is quite easy.", ["tres preguntas correctas", "usa for o since y un adverbio", "respuestas coherentes con la pregunta"], ["hoja con las preguntas y respuestas"], ["usar since con una duración", "responder How often con una duración"], "Haz la entrevista en voz alta y pide que te respondan sin ver tu hoja."),
    "Escribe cinco oraciones con have been + -ing sobre actividades de tu semana.",
    "Escribe un diálogo de seis líneas con How often y How long.",
)

# ================================================== clase 3: acciones anteriores y descripción de lugares y personas
D3 = "«Reporter: Why were you late yesterday? Student: I missed the bus. I had forgotten my wallet at home, so I had to go back. Reporter: Had you checked the schedule? Student: Yes, but the bus had left before I arrived. Reporter: And how was the market? Student: It was very busy and crowded. There was a basketball court near the entrance. A lady, who is a very organized person, was selling bread.»\n(reporter = periodista, wallet = billetera, schedule = horario, entrance = entrada, lady = señora, organized = organizada)"
D4 = "«Guide: This is a hospital. It is interesting for visitors because of the old building. Doctor Ruiz is a good surgeon. She is very good at staying calm. Nurse Ana is interested in helping children. The cafe is quiet at noon but crowded at six.»\n(guide = guía, hospital = hospital, surgeon = cirujana, calm = tranquila, nurse = enfermera, children = niños)"

lesson(
    OA, 3, MAT_SPEAK,
    "Aprenderé a describir acciones que ocurrieron antes de otra en el pasado (past perfect) y a identificar y describir lugares, ocupaciones y personas (cualidades) en una conversación. Sirve para contar qué pasó antes y describir con precisión.",
    ["Sé el pasado simple.", "Sé adjetivos como busy y quiet."],
    [
        "El pasado perfecto (past perfect) se forma con had + participio y muestra la acción que ocurrió antes de otra del pasado: He didn’t have money because he had lost his wallet. Primero perdió la billetera; después no tuvo dinero. En preguntas se invierte: Had you checked the schedule? Se responde: Yes, I had o No, I hadn’t. Palabras clave: before, after, already, by the time.",
        "Para describir lugares se usan adjetivos como busy, crowded, quiet y noisy, y sustantivos compuestos como basketball court. Para describir personas y oficios se usa be + adjetivo (a very organized person), good at + sustantivo o -ing (good at staying calm) y interested in + sustantivo o -ing (interested in helping children). Interested describe a quien siente, y interesting describe lo que produce interés.",
        "En una conversación, organiza lo que cuentas: primero la acción anterior (había olvidado, había perdido) y luego el hecho posterior. Para describir, elige dos o tres adjetivos que expliquen cómo es el lugar o la persona y agrega un dato. Practica con una pregunta y su respuesta completa: Why was she late? Because she had missed the bus.",
    ],
    [("past perfect", "pasado perfecto: had + participio"), ("had lost", "había perdido"), ("crowded", "lleno de gente"), ("good at", "bueno para"), ("interested in", "interesado en"), ("organized", "organizado")],
    [
        ("Past perfect", "Completa: «When I arrived, the film ___.» A) had started B) starts", ["La película empezó antes de que llegara.", "Se usa had started.", "La A."], "A"),
        ("Descripción", "¿Qué frase describe una cualidad? A) She is a very organized person. B) She is on the bus.", ["Organized es una cualidad.", "La B es un lugar.", "La A."], "A"),
    ],
    [
        ("Decir I had lose.", "Después de had va el participio.", "Escribe had lost."),
        ("Usar interesting para una persona que siente interés.", "Interesting describe lo que produce interés.", "Usa I am interested in…"),
    ],
    [
        ("Lee: " + D3 + " ¿Qué había olvidado el estudiante? A) su billetera B) su mochila", "A", "Dice I had forgotten my wallet at home."),
        ("Lee: " + D4 + " ¿Qué oficio tiene la doctora Ruiz? A) cirujana B) enfermera", "A", "Dice Doctor Ruiz is a good surgeon."),
        ("Lee: " + D3 + " ¿Cómo era el mercado? A) muy concurrido y lleno de gente B) vacío", "A", "Dice very busy and crowded."),
    ],
    [
        ("Lee: " + D3 + " ¿Qué había pasado con el bus cuando llegó? A) ya había salido B) llegó atrasado", "A", "Dice the bus had left before I arrived."),
        ("Lee: " + D4 + " ¿En qué es buena la doctora Ruiz? A) en mantener la calma B) en cocinar", "A", "Dice good at staying calm."),
        ("Lee: " + D4 + " ¿Qué le interesa a la enfermera Ana? A) ayudar a niños B) viajar", "A", "Dice interested in helping children."),
    ],
    [
        ("Lee: " + D3 + " ¿Por qué tuvo que volver a casa? A) porque había olvidado su billetera B) porque se perdió", "A", "Dice so I had to go back."),
        ("Lee: " + D4 + " ¿Cuándo está llena de gente la cafetería? A) a las seis B) al mediodía", "A", "Dice crowded at six."),
        ("Lee: " + D3 + " ¿Cómo describe a la señora? A) como una persona muy organizada B) como una persona nerviosa", "A", "Dice a very organized person."),
    ],
    [
        ("Lee: " + D3 + " Un compañero entiende que el estudiante olvidó la billetera después de llegar tarde. ¿Qué lo corrige? A) la olvidó antes: had forgotten B) la olvidó en el bus", "A", "Had forgotten indica una acción anterior."),
        ("Lee: " + D4 + " ¿Por qué el hospital es interesante para los visitantes? A) por su edificio antiguo B) por sus precios", "A", "Dice because of the old building."),
    ],
    [
        ("Ordena: a) llegó a la parada b) olvidó la billetera c) el bus salió", "b, c, a", "Olvidó la billetera, el bus salió antes (had left before I arrived) y después él llegó."),
        ("Une cada frase con su tipo. 1) He had already left. 2) She is good at drawing. 3) It is a basketball court. Tipos: a) habilidad b) lugar c) acción anterior", "1-c, 2-a, 3-b", "Had left es anterior, good at es habilidad y court es un lugar."),
    ],
    [("Lee: «By the time we got to the cinema, the film had already started. We had bought the tickets online, so we entered quickly.» (got to = llegamos a, entered = entramos). ¿Cómo habían comprado las entradas?", "En línea", "Dice we had bought the tickets online.")],
    [
        ("¿Cómo se forma el pasado perfecto (en conversación)?", "Had + participio", "Muestra la acción anterior."),
        ("¿Qué preposición va con good (en conversación)?", "At", "Good at staying calm."),
        ("¿Qué diferencia hay entre interested e interesting (en conversación)?", "Interested siente; interesting produce interés", "Se usan en distintos sujetos."),
    ],
    task("Cuenta en voz alta, a una persona de tu casa, un hecho pasado con una causa anterior (por ejemplo, por qué llegaste tarde o no pudiste hacer algo) usando dos frases con had + participio. Luego describe un lugar y una persona de tu barrio con dos adjetivos y good at o interested in. Antes escribe tus frases en una hoja.", "Ejemplo: I was late because I had missed the bus. I hadn’t finished my homework because I had lost my notebook. The market is busy and crowded. My neighbour is good at fixing bikes.", ["usa dos frases con had + participio", "describe un lugar y una persona", "usa good at o interested in"], ["hoja con las frases", "comentario de la persona que escuchó"], ["usar el pasado simple en lugar del pasado perfecto", "decir interesting para una persona que siente interés"], "Pregunta a la persona qué acción ocurrió primero."),
    "Escribe cinco oraciones con had + participio sobre un día especial.",
    "Escribe una descripción de tres oraciones de un oficio que te interese.",
)

# ================================================== clase 4: confirmar, sugerir, ofrecer y acuerdo
D5 = "«Cami: It’s a lovely park, isn’t it? Tomás: Yes, it is. You like running, don’t you? Cami: Yes, I do. Your brother wasn’t at school today, was he? Tomás: No, he wasn’t. He is ill. Cami: Would you like something to drink? Tomás: Yes, please. Cami: Shall I bring you a hot chocolate? Tomás: That would be great. You ought to try the new cafe by the gate.»\n(lovely = lindo, running = correr, ill = enfermo, drink = beber, hot chocolate = chocolate caliente, gate = portón)"
D6 = "«Dani: I think we should have a school radio. Pia: I agree with you. It would be fun, wouldn’t it? Dani: Yes, and we could play music. Pia: I’d like to talk about sports as well. Dani: I disagree with the sports idea, because we already have a newsletter. Pia: OK, shall I ask the principal if we can start in March? Dani: Good idea. Could you also ask for a room?»\n(radio = radio, fun = entretenido, newsletter = boletín, principal = director, room = sala)"

lesson(
    OA, 4, MAT_SPEAK,
    "Aprenderé a confirmar información con tag questions, a hacer sugerencias, ofrecimientos y solicitudes y a expresar acuerdo o desacuerdo en una discusión. Sirve para conversar con cortesía y llegar a acuerdos.",
    ["Sé el verbo to be y el presente simple.", "Sé frases como I think y I like."],
    [
        "Las preguntas de cola (tag questions) confirman información. Una frase afirmativa lleva cola negativa: It’s a lovely park, isn’t it? Una frase negativa lleva cola afirmativa: Your brother wasn’t at school, was he? Se repite el auxiliar de la frase: You like running, don’t you? She will come, won’t she? Se responde con Yes o No y el auxiliar.",
        "Para ofrecer se usa Would you like…? y Shall I…?: Would you like something to eat? Shall I bring you a cup of tea? Para sugerir se usa You ought to… (deberías) o We could… (podríamos). Para hacer una solicitud se usa Could you…? Could you also ask for a room? Para acuerdo y desacuerdo, usa I agree with… e I disagree with…, y completa con because.",
        "En una discusión, escucha al otro antes de responder. Reconoce su idea antes de decir que no estás de acuerdo: I see your point, but I disagree because… Mantén un tono amable y usa please. Después de una oferta, responde con Yes, please o No, thank you. Practica con roles: una persona ofrece, la otra acepta o rechaza con cortesía.",
    ],
    [("tag question", "pregunta de cola"), ("Would you like…?", "¿Te gustaría…?"), ("Shall I…?", "¿Quieres que yo…?"), ("You ought to", "deberías"), ("Could you…?", "¿Podrías…?"), ("I disagree with", "no estoy de acuerdo con")],
    [
        ("Cola", "Completa: «You play the guitar, ___?» A) don’t you B) do you", ["La frase es afirmativa.", "La cola es negativa.", "La A."], "A"),
        ("Respuesta cortés", "Te ofrecen: «Would you like some tea?» ¿Qué respondes si aceptas? A) Yes, please. B) No, I am.", ["Respondo con cortesía.", "Yes, please acepta.", "La A."], "A"),
    ],
    [
        ("Usar una cola afirmativa después de una frase afirmativa.", "La cola debe ser opuesta a la frase.", "Cambia la polaridad."),
        ("Responder a Would you like con Yes, I would like not.", "La respuesta no es natural.", "Responde Yes, please o No, thank you."),
    ],
    [
        ("Lee: " + D5 + " ¿Qué le gusta hacer a Cami? A) correr B) nadar", "A", "Dice You like running."),
        ("Lee: " + D5 + " ¿Qué ofrece Cami? A) un chocolate caliente B) un pastel", "A", "Dice Shall I bring you a hot chocolate?"),
        ("Lee: " + D6 + " ¿Qué quiere crear Dani? A) una radio escolar B) un equipo", "A", "Dice I think we should have a school radio."),
    ],
    [
        ("Lee: " + D5 + " ¿Por qué no fue su hermano al colegio? A) porque está enfermo B) porque tiene prueba", "A", "Tomás responde He is ill."),
        ("Lee: " + D6 + " ¿Con qué idea está en desacuerdo Dani? A) hablar de deportes B) poner música", "A", "Dice I disagree with the sports idea."),
        ("Lee: " + D5 + " ¿Qué le sugiere Tomás? A) probar la nueva cafetería junto al portón B) irse a casa", "A", "Dice You ought to try the new cafe by the gate."),
    ],
    [
        ("Lee: " + D6 + " ¿Qué razón da Dani contra el tema de deportes? A) ya tienen un boletín B) no hay sala", "A", "Dice because we already have a newsletter."),
        ("Lee: " + D6 + " ¿Qué ofrece hacer Pia? A) preguntar al director si pueden empezar en marzo B) comprar el equipo", "A", "Dice shall I ask the principal if we can start in March?"),
        ("Lee: " + D5 + " Cami dice It’s a lovely park, isn’t it? ¿Qué espera? A) que Tomás confirme B) que Tomás se despida", "A", "La cola busca confirmación."),
    ],
    [
        ("Lee: " + D6 + " ¿Qué solicitud hace Dani al final? A) pedir una sala B) pedir permiso para salir", "A", "Dice Could you also ask for a room?"),
        ("Lee: " + D5 + " ¿Qué cola va después de Your brother wasn’t at school? A) was he B) wasn’t he", "A", "La frase es negativa y la cola, afirmativa."),
    ],
    [
        ("Completa con la cola: «It will rain tomorrow, ___?» A) won’t it B) will it", "A", "La frase es afirmativa y la cola, negativa."),
        ("Une cada frase con su función. 1) Shall I carry your bag? 2) You ought to rest. 3) I disagree with you. Funciones: a) sugerencia b) desacuerdo c) ofrecimiento", "1-c, 2-a, 3-b", "Shall I ofrece; ought to sugiere; disagree opina en contra."),
    ],
    [("Lee: «Sam: You don’t eat fish, do you? Luis: No, I don’t. Sam: Would you like some pasta? Luis: Yes, please.» ¿Qué le ofrece Sam?", "Pasta", "Dice Would you like some pasta?")],
    [
        ("¿Cómo se forma una cola si la frase es negativa?", "Con el auxiliar en forma afirmativa", "She isn’t here, is she?"),
        ("¿Qué expresa Shall I?", "Un ofrecimiento", "Pregunta si puedo hacer algo."),
        ("¿Cómo se acepta una oferta con cortesía?", "Yes, please", "Se acepta con cortesía."),
    ],
    task("Con una persona de tu casa, actúen un diálogo de ocho líneas sobre un plan para el fin de semana. Debe tener: una tag question, un ofrecimiento con Would you like o Shall I, una sugerencia con You ought to o We could, una solicitud con Could you y un acuerdo o desacuerdo con razón. Escribe primero el guion.", "Ejemplo: A: It’s a good day for a picnic, isn’t it? B: Yes. Shall I bring the sandwiches? A: Great. We could invite Lia. B: I disagree, because she is busy. A: OK. Could you send a message to Ben?", ["incluye las cinco funciones", "las frases son correctas", "se representa con cortesía"], ["guion escrito", "comentario de la persona que actuó"], ["usar una cola afirmativa después de una frase afirmativa", "no dar razón en el desacuerdo"], "Pide a la persona que marque en el guion cada función que oyó."),
    "Escribe diez colas con distintos auxiliares y revísalas.",
    "Escribe un diálogo de diez líneas entre dos personas que no están de acuerdo pero se respetan.",
)

# ================================================== clase 5: conectar ideas, enfatizar e informar
D7 = "«Reporter: What did the coach say? Luz: She said that neither the goalkeeper nor the captain could play on Saturday, so she told us to change the plan. Reporter: Did you do it yourself? Luz: Yes, we planned the new team ourselves. We will play on Sunday as soon as the field is free, unless it rains. Reporter: And what did your friend say? Luz: He said that he had taught himself to play the drums, though he is not a professional.»\n(coach = entrenadora, goalkeeper = arquero, captain = capitán, plan = plan, field = cancha, drums = batería, professional = profesional, taught = enseñó)"
D8 = "«Teacher: Neither Ana nor Ben handed in the project. Student: Either they forgot or they had problems with the internet. Teacher: They told me to wait. As a result, I will give them one more day. Student: That’s fair, though some students finished on time. Teacher: Unless they miss the new date, there will be no problem.»\n(handed in = entregaron, forgot = olvidaron, fair = justo, on time = a tiempo, miss = perder)"

lesson(
    OA, 5, MAT_SPEAK,
    "Aprenderé a conectar ideas con neither…nor, either…or, though, as a result, as soon as y unless, a enfatizar quién realiza la acción con pronombres reflexivos y a informar lo que otros dicen. Sirve para contar lo que pasó y lo que se dijo con claridad y precisión.",
    ["Sé conectores simples como and, but y because.", "Sé el pasado simple."],
    [
        "Los conectores unen ideas: neither…nor (ni… ni), either…or (o… o), though (aunque), as a result (como resultado), as soon as (tan pronto como) y unless (a menos que). Neither John nor Susan is in the office significa que ninguno está. We wouldn’t use gas unless it was cheap significa que solo lo usarían si fuera barato. Elige el conector según la relación: contraste, consecuencia, condición, tiempo u opciones.",
        "Los pronombres reflexivos (myself, yourself, himself, herself, itself, ourselves, themselves) enfatizan quién realiza la acción: Did you make it yourself? We planned the team ourselves. También indican que el sujeto y el objeto son la misma persona: he taught himself. Para informar lo que otros dicen (reported speech) se usa said (that) o told + persona + to: Mr. Brown said he had finished the report; she told me to go home.",
        "En el estilo indirecto, el tiempo verbal retrocede: «I am tired» pasa a She said she was tired; «I finished» pasa a He said he had finished. Los pronombres también cambian: «I» pasa a he o she. Al conversar, di primero quién habló, luego lo que dijo, y agrega un conector si necesitas contrastar o explicar.",
    ],
    [("neither…nor", "ni… ni"), ("either…or", "o… o"), ("unless", "a menos que"), ("as a result", "como resultado"), ("reflexive pronoun", "pronombre reflexivo"), ("told me to", "me dijo que (hiciera algo)")],
    [
        ("Reflexivo", "Completa: «They painted the room ___.» A) themselves B) theirs", ["Se enfatiza que lo hicieron ellos mismos.", "Themselves.", "La A."], "A"),
        ("Estilo indirecto", "Ana dice: «I am hungry.» ¿Cómo lo reportas? A) Ana said she was hungry. B) Ana said she is hungry yesterday.", ["Retrocede el tiempo.", "Am pasa a was.", "La A."], "A"),
    ],
    [
        ("Confundir neither…nor con either…or.", "Una niega las dos opciones y la otra ofrece una de ellas.", "Neither: ninguna; either: una de las dos."),
        ("Reportar sin cambiar el pronombre.", "Se confunde quién habla.", "Cambia I por he o she."),
    ],
    [
        ("Lee: " + D7 + " ¿Qué dijo la entrenadora? A) que el arquero y el capitán no podían jugar B) que el campo estaba cerrado", "A", "Dice neither the goalkeeper nor the captain could play on Saturday."),
        ("Lee: " + D7 + " ¿Quién planificó el nuevo equipo? A) ellos mismos B) la entrenadora", "A", "Dice we planned the new team ourselves."),
        ("Lee: " + D8 + " ¿Quiénes no entregaron el proyecto? A) Ana y Ben B) todos", "A", "Dice Neither Ana nor Ben handed in the project."),
    ],
    [
        ("Lee: " + D7 + " ¿Cuándo jugarán? A) el domingo, apenas la cancha esté libre B) el sábado", "A", "Dice We will play on Sunday as soon as the field is free."),
        ("Lee: " + D8 + " ¿Qué hipótesis da el estudiante? A) olvidaron o tuvieron problemas con internet B) estaban enfermos", "A", "Dice Either they forgot or they had problems with the internet."),
        ("Lee: " + D7 + " ¿Cómo aprendió su amigo a tocar la batería? A) solo, por sí mismo B) con un profesor", "A", "Dice he had taught himself."),
    ],
    [
        ("Lee: " + D8 + " ¿Qué consecuencia tuvo? A) el profesor dará un día más B) cancelará la tarea", "A", "Dice As a result, I will give them one more day."),
        ("Lee: " + D7 + " ¿Qué condición puede cambiar el partido del domingo? A) que llueva B) que no haya árbitro", "A", "Dice unless it rains."),
        ("Lee: " + D8 + " ¿Qué muestra though? A) un contraste: algunos sí entregaron a tiempo B) una causa", "A", "Dice though some students finished on time."),
    ],
    [
        ("Lee: " + D7 + " La entrenadora dijo que cambiaran el plan. ¿Cómo lo reporta Luz? A) she told us to change the plan B) she said us the plan", "A", "Told + persona + to + verbo."),
        ("Lee: " + D8 + " ¿Qué condición evita problemas? A) que no pierdan la nueva fecha B) que entreguen hoy", "A", "Dice Unless they miss the new date, there will be no problem."),
    ],
    [
        ("Une cada frase con su función. 1) Neither John nor Susan is here. 2) She told me to wait. 3) We built it ourselves. Funciones: a) enfatizar quién actúa b) informar lo que dice otra persona c) negar dos cosas", "1-c, 2-b, 3-a", "Neither niega, told reporta y ourselves enfatiza."),
        ("Reporta: «I will call you tomorrow», dijo Teo. A) Teo said he would call me the next day. B) Teo said I call you tomorrow.", "A", "Will pasa a would y tomorrow pasa a the next day."),
    ],
    [("Lee: «Marco said that he had finished the report. His teacher told him to send it by Friday.» (report = informe, send = enviar). ¿Qué le dijo la profesora?", "Que lo enviara el viernes", "Told him to send it by Friday.")],
    [
        ("¿Qué significa unless (en conversación)?", "A menos que", "Expresa una condición."),
        ("¿Qué pronombre reflexivo corresponde a we?", "Ourselves", "Enfatiza quién actúa."),
        ("¿Qué estructura se usa con told (en conversación)?", "Told + persona + to + verbo", "She told me to go."),
    ],
    task("Conversa con una persona de tu casa durante un minuto: cuéntale qué dijo una profesora o un amigo (usa said y told), usa un conector de la clase y un pronombre reflexivo. Escribe antes cuatro frases de apoyo.", "Ejemplo: My teacher said that the test was easy. She told us to study. Neither my friend nor I studied much. We prepared the notes ourselves, though it was hard. As a result, we did well.", ["usa said y told", "incluye un conector y un reflexivo", "las frases se entienden"], ["hoja con cuatro frases", "comentario de la persona que escuchó"], ["no cambiar el pronombre al reportar", "usar either…or como si fuera una negación"], "Pide a la persona que repita lo que dijo la profesora para comprobar que entendió."),
    "Escribe cinco frases con said o told sobre lo que dijo alguien hoy.",
    "Escribe un diálogo de seis líneas con neither…nor, unless y un reflexivo.",
)
