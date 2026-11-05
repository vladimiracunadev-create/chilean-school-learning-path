"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 16: funciones comunicativas del año en textos escritos.

Correos, boletines, reseñas y diarios breves escritos en el enunciado; el estudiante elige, corrige o completa formas.
Textos originales, inglés americano. Concordancia de neither ... nor con el sujeto más cercano; pasado perfecto solo con un
segundo hecho pasado; estilo indirecto con retroceso de tiempo. Los títulos de clase del plan son genéricos; aquí se
aplican a cantidad y frecuencia, descripción y expresiones comunes, acciones que continúan y opinión, conectores,
énfasis y reporte, y pasado anterior e hipótesis.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 16"

# ------------------------------------------------------------------ clase 1: cantidad, enumeración, frecuencia, tiempo y grado
N1 = "Boletín del club de ajedrez (borrador): «A large number of members came to the first meeting. There are few boards, so we share them. We have a little time before the next game. I usually play on Saturdays, and I often watch games on Sundays. Our teacher is rather strict, but she will be here soon.» (chess = ajedrez, members = socios, meeting = reunión, boards = tableros, share = compartir, strict = exigente)"
N2 = "Correo de ejemplo: «Hi Lía, there are a few seats left for the workshop, but there is little time to sign up. Please send your details this week. First, write your name. Second, write your school. Third, write your phone.» (seats = cupos, workshop = taller, sign up = inscribirse)"
N3 = "Mensaje de un club: «How often do you practice? I practice twice a week. My brother hardly ever practices. We usually meet at five.»"

lesson(
    OA, 1, MAT_R,
    "Aprenderé a escribir cantidades, enumeraciones, frecuencia, tiempo y grado (a few, few, little, a large number of, usually, often, rather, soon) en textos escritos. Sirve para informar con precisión por escrito.",
    ["Sé usar there is y there are.", "Conozco los adverbios de frecuencia."],
    [
        "Para escribir cantidades usa a large number of o a small number of con sustantivos contables; few y a few con contables; little y a little con incontables. A few y a little son positivos (hay algunos, hay un poco); few y little son negativos (casi no hay). Para contar y enumerar, usa first, second, third y finally, o las listas con viñetas.",
        "Para escribir frecuencia usa always, usually, often, sometimes, hardly ever y never. Van antes del verbo principal (I usually play chess) y después de be (She is often late). También se escribe con expresiones como twice a week o once a month. Para preguntar por frecuencia: How often do you practice? Para el tiempo, usa soon, now, later y during. Para el grado, usa rather, quite y very: she is rather strict.",
        "Al escribir, no repitas el mismo adverbio. Cuida la concordancia de there are con plural y there is con incontables. Revisa que few y little no se usen con el sustantivo equivocado.",
    ],
    [("a large / small number of", "una gran / pequeña cantidad (contables)"), ("few / a few", "pocos / unos pocos (contables)"), ("little / a little", "poco / un poco (incontables)"), ("How often...?", "¿con qué frecuencia?"), ("twice a week / once a month", "dos veces por semana / una vez al mes"), ("rather / soon", "bastante / pronto")],
    [
        ("Elegir la cantidad", N2 + " ¿Qué quedan pocos y qué hay poco?", ["Busco a few y little.", "A few seats left: unos pocos asientos.", "Little time: casi no queda tiempo."], "Quedan unos pocos asientos y casi no queda tiempo"),
        ("Ubicar la frecuencia", N1 + " ¿Con qué frecuencia juega y ve partidas?", ["Busco usually y often.", "Usually play on Saturdays.", "Often watch games on Sundays."], "Juega los sábados por lo general y ve partidas los domingos a menudo"),
    ],
    [
        ("Escribir few time.", "Time es incontable; few va con contables.", "Escribe little time."),
        ("Poner el adverbio de frecuencia después del verbo principal.", "Debe ir antes: I usually play chess.", "Colócalo antes del verbo, o después de be."),
    ],
    [
        mr(N1, "¿Qué dice sobre los tableros?", "Hay pocos, por eso se comparten", ["Hay muchos y sobran en el club", "No hay ninguno, así que no juegan"], "Dice there are few boards, so we share them."),
        mc("Completa: There is ____ sugar left.", "little", ["few", "many"], "Sugar es incontable."),
        mc("Completa: There are ____ chairs left.", "a few", ["a little", "much"], "Chairs es contable."),
    ],
    [
        mr(N3, "¿Con qué frecuencia practica el autor?", "Dos veces por semana", ["Una vez al mes", "Todos los días"], "Dice twice a week."),
        mr(N3, "¿Con qué frecuencia practica su hermano?", "Casi nunca", ["A menudo", "Siempre"], "Dice hardly ever."),
        mr(N1, "¿Cómo es la profesora?", "Bastante exigente", ["Muy simpática y relajada", "Nada exigente con los socios"], "Dice rather strict."),
    ],
    [
        mc("Escribe correctamente (el adverbio va antes del verbo principal):", "I usually play chess on Saturdays", ["I play usually chess on Saturdays", "I play chess on usually Saturdays"], "El adverbio va antes del verbo principal."),
        mc("Con el verbo be, el adverbio de frecuencia va después de be. Elige:", "She is often late", ["She often is late", "She is late often"], "Después de be va el adverbio."),
        arith("En el club hay 40 socios. Una gran cantidad, 28, vino a la primera reunión. ¿Cuántos no vinieron?", "40-28", "Se resta quienes vinieron de los socios totales.", " socios"),
    ],
    [
        mr(N1, "Un compañero escribe a large number of boards. ¿Qué dice el texto?", "Dice few boards, es decir, pocos tableros", ["Dice a large number, igual que el compañero", "No dice nada sobre los tableros"], "Few indica una cantidad pequeña."),
        mc("Una compañera escribe «There is a few seats left». ¿Qué corriges?", "There are a few seats", ["There is a few seat", "There is few seats"], "Seats es plural; se usa there are."),
    ],
    [
        mc("Escribes tres pasos para inscribirte. ¿Cuál enumeración usa bien las palabras de orden?", "First, write your name. Second, write your school. Third, write your phone", ["First, write your name. Second, write your school. First, write your phone", "First, write your name. Third, write your school. Second, write your phone"], "La enumeración usa las palabras de orden en secuencia."),
        mc("Escribe la pregunta para obtener la frecuencia con que alguien lee: ¿cuál es?", "How often do you read?", ["How long do you read?", "How many read?"], "How often pide la frecuencia."),
    ],
    [mc("Escribes un mensaje para un compañero. ¿Qué oración dice mejor que casi nunca llega tarde?", "He hardly ever arrives late", ["He hardly arrives never late", "He ever hardly arrives late"], "Hardly ever va antes del verbo.")],
    [
        ("En Inglés de 2.º medio (OA 16, clase 1): ¿qué diferencia hay entre few y a few?", "Few: casi ninguno; a few: unos pocos", "Cambia el sentido."),
        ("En Inglés de 2.º medio (OA 16, clase 1): ¿dónde va usually en I take photos?", "Antes del verbo: I usually take photos", "Es la regla."),
        ("En Inglés de 2.º medio (OA 16, clase 1): ¿con qué sustantivos se usa little?", "Con incontables", "Little time, little sugar."),
    ],
    task("Escribe un boletín de seis a ocho oraciones sobre un club o una actividad de tu curso. Usa a large number of, few o a few, little o a little, usually u often, twice a week, rather y soon. Incluye una enumeración con First, Second y Third. Sigue este ejemplo.", "A large number of students joined the reading club. There are few copies of the book, so we share. We have a little time before the next meeting. I usually read on Fridays. The teacher is rather kind. First, bring a book. Second, bring a pen. Third, arrive on time.", ["usa al menos seis funciones", "las funciones son correctas", "incluye una enumeración"], ["boletín en la hoja"], ["usar few con incontables", "poner el adverbio después del verbo principal"], "Pide que subraye cada función y diga cuál es."),
    "Escribe cinco oraciones con few, a few, little, a little y a large number of.",
    "Cuenta en tu casa cuántas veces por semana haces una actividad y escríbelo en inglés.",
)

# ------------------------------------------------------------------ clase 2: describir personas y situaciones, y expresiones comunes
P1 = "Descripción en un correo: «My new neighbor is polite and kind, but her brother is impolite. Yesterday, the form was incomplete, so I had to look for the missing page online. It is illegal to park in front of the door, and it is illogical to leave your car there.» (neighbor = vecina, polite = cortés, form = formulario, missing = que falta, online = en línea, illegal = ilegal, illogical = ilógico)"
P2 = "Mensaje: «Sorry about the mess. Is this bag yours? It belongs to Marta, I think. Can you look after it? I will look for my keys. We have enough time, and the bus ticket is cheap enough.» (mess = desorden, belongs to = pertenece a, look after = cuidar, look for = buscar, enough = suficiente, ticket = pasaje)"
P3 = "Anuncio: «Lost: a blue folder. It belongs to Pablo. It contains an incomplete report and some old photos. If you find it, please contact us online. We are sorry about the trouble.» (folder = carpeta, contains = contiene, report = informe, contact = contactar, trouble = molestia)"

lesson(
    OA, 2, MAT_R,
    "Aprenderé a describir personas y situaciones con adjetivos como polite/impolite, complete/incomplete y legal/illegal, y a escribir expresiones comunes (enough time, sorry about, belong to, look for, look after, online) y palabras compuestas. Sirve para escribir con claridad y precisión.",
    ["Sé usar adjetivos para describir.", "Conozco los prefijos im-, in- e il-."],
    [
        "Para describir personas y situaciones usa adjetivos y sus opuestos con los prefijos im-, in- e il-: polite → impolite, patient → impatient, complete → incomplete, correct → incorrect, legal → illegal, logical → illogical. Recuerda la regla general: im- antes de b, m, p; il- antes de l; in- en la mayoría de los demás casos. Hay excepciones (irregular, unhappy): consulta un diccionario. Un adjetivo describe a una persona (He is polite) o una situación (It was incomplete).",
        "Para escribir con claridad y de forma natural, usa expresiones comunes: enough time (tiempo suficiente), cheap enough (suficientemente barato), sorry about (lamento lo de), belong to (pertenecer a), look for (buscar), look after (cuidar) y online (en línea). Enough va antes del sustantivo (enough time) y después del adjetivo (cheap enough). Belong to se usa con la persona dueña: It belongs to Marta.",
        "También hay palabras compuestas, como online, classroom, homework y notebook. Se escriben juntas, con un guion o separadas, según la palabra. Si dudas, consulta un diccionario. Evita repetir la misma palabra: usa sinónimos y expresiones.",
    ],
    [("polite / impolite", "cortés / descortés"), ("complete / incomplete", "completo / incompleto"), ("legal / illegal", "legal / ilegal"), ("enough time / cheap enough", "tiempo suficiente / suficientemente barato"), ("belong to / look for / look after", "pertenecer a / buscar / cuidar"), ("sorry about / online", "lamento lo de / en línea")],
    [
        ("Elegir el adjetivo contrario", P1 + " ¿Qué adjetivo describe al hermano de la vecina y cuál es su contrario?", ["Busco el adjetivo del hermano.", "Es impolite.", "Su contrario es polite."], "Impolite (descortés); su contrario es polite"),
        ("Distinguir look for y look after", P2 + " ¿Qué busca el autor y qué le pide cuidar?", ["Busca sus llaves: look for.", "Pide cuidar la bolsa: look after.", "Son dos acciones distintas."], "Busca sus llaves y le pide cuidar la bolsa"),
    ],
    [
        ("Decir It is inlegal.", "Antes de l se usa il-.", "Escribe illegal."),
        ("Escribir enough cheap.", "Enough va después del adjetivo.", "Escribe cheap enough."),
    ],
    [
        mc("¿Cuál es el contrario de polite?", "impolite", ["inpolite", "ilpolite"], "Delante de p se usa im-."),
        mc("¿Cuál es el contrario de legal?", "illegal", ["imlegal", "inlegal"], "Delante de l se usa il-."),
        mc("¿Cuál es el contrario de complete?", "incomplete", ["imcomplete", "ilcomplete"], "Delante de c se usa in-."),
    ],
    [
        mr(P2, "¿A quién pertenece la bolsa según el autor?", "A Marta, según cree el autor", ["Al autor del mensaje", "A su hermano, según dice el mensaje"], "Dice It belongs to Marta, I think."),
        mr(P3, "¿Qué hay dentro de la carpeta?", "Un informe incompleto y algunas fotos viejas", ["Un informe terminado y algunas fotos nuevas", "Un cuaderno incompleto y algunas fotos viejas"], "Dice an incomplete report and some old photos."),
        mr(P3, "¿Cómo se contacta al autor?", "En línea", ["Por carta", "En persona"], "Dice contact us online."),
    ],
    [
        mc("Completa (tiempo suficiente): We have ____ to finish the project.", "enough time", ["enough times", "enough of time"], "Enough va antes del sustantivo incontable."),
        mc("Completa con la expresión de la clase (lamento lo del error): I am ____ about the mistake.", "sorry", ["sorrow", "sadly"], "Sorry about expresa lamento."),
        mc("Completa: The tickets are ____. We can buy two.", "cheap enough", ["enough cheap", "cheaply enough"], "Enough va después del adjetivo."),
    ],
    [
        mr(P1, "Un compañero dice que illogical significa lógico. ¿Qué respuesta es más acertada?", "No: illogical significa que no es lógico", ["Sí: il- agrega énfasis, así que significa muy lógico", "Sí: significa ilegal porque lleva il-"], "Il- da el sentido contrario."),
        mr(P3, "Otro compañero escribe: «The folder belongs of Pablo». ¿Qué corriges?", "The folder belongs to Pablo", ["The folder belongs on Pablo", "The folder belongs Pablo"], "Belong va con to."),
    ],
    [
        mc("Reescribe: «We have time enough». ¿Cuál es la forma correcta?", "We have enough time", ["We have enough times", "We time have enough"], "Enough va antes del sustantivo."),
        mr(P1, "El formulario no está completo. ¿Qué oración lo dice bien?", "The form is incomplete", ["The form is not incomplete", "The form is incompleted"], "Incomplete es un adjetivo correcto; not incomplete diría lo contrario."),
    ],
    [mc("Escribes un mensaje: tu amigo perdió su billetera. ¿Qué oración usa bien look for y sorry about?", "I am sorry about your wallet. I will look for it online", ["I am sorry about your wallet. I will look after it online", "I am sorry about your wallet. I will look it for online"], "Look for it va junto; look after significa cuidar, no buscar.")],
    [
        ("En Inglés de 2.º medio (OA 16, clase 2): ¿qué prefijo va delante de la letra l?", "il-", "Se usa en illegal e illogical."),
        ("En Inglés de 2.º medio (OA 16, clase 2): ¿qué significa belong to?", "Pertenecer a", "Se usa con el dueño."),
        ("En Inglés de 2.º medio (OA 16, clase 2): ¿dónde va enough con un adjetivo?", "Después: cheap enough", "Con sustantivo va antes."),
    ],
    task("Escribe un correo de cinco o seis oraciones a un amigo sobre una situación en que perdiste algo o hubo un malentendido. Usa dos adjetivos con prefijo (impolite, incomplete, illegal...), enough time o cheap enough, sorry about, look for o look after, belong to y online. Sigue este ejemplo.", "Hi Tomás, sorry about the mess yesterday. I lost a notebook that belongs to my sister. I will look for it, but I do not have enough time today. The list I made was incomplete, so I asked online. I hope it is not impossible to find.", ["usa dos adjetivos con prefijo", "usa tres expresiones comunes", "las formas son correctas"], ["correo en la hoja"], ["usar el prefijo equivocado", "poner enough después del sustantivo"], "Pide que cambie un adjetivo por su contrario y ajuste el sentido."),
    "Escribe los contrarios de diez adjetivos con im-, in- e il-.",
    "Describe en español tres cosas de tu casa y piensa un adjetivo con prefijo para cada una en inglés.",
)

# ------------------------------------------------------------------ clase 3: acciones continuas, acuerdo, opinión, posesión y tiempo
PC1 = "Diario: «For two months, I have been learning to swim. My teacher has been helping me every Tuesday, and I have been practicing my breathing at home. I was left without my goggles last week, so I borrowed my brother's. During the summer, I will keep training.» (swim = nadar, breathing = respiración, goggles = antiparras, borrowed = pedí prestadas, keep training = seguir entrenando)"
PC2 = "Foro: «I agree with Laura about the school trip. I believe in short trips because they cost less. I disagree with Tomás: he says the bus is expensive, but the price has been the same since March. In my opinion, this plan is good for everyone.» (trip = paseo, cost = costar, price = precio, since = desde, plan = plan)"
PC3 = "Carta: «Ms. Díaz has been working all day. Since Monday, she has been preparing a report for her job. This desk is hers. That chair is mine, and the lamp is yours if you need it tomorrow.» (report = informe, job = trabajo, desk = escritorio, chair = silla, lamp = lámpara)"

lesson(
    OA, 3, MAT_R,
    "Aprenderé a escribir acciones que empezaron en el pasado y continúan (have been + -ing), a expresar acuerdo, desacuerdo y opinión, y a indicar posesión y tiempo (I was left without..., during, since, for). Sirve para escribir diarios, foros y cartas con precisión.",
    ["Sé usar el presente simple y el pasado simple.", "Conozco I agree, I disagree y I believe."],
    [
        "El presente perfecto continuo (have/has been + verbo con -ing) describe una acción que empezó en el pasado y todavía continúa o acaba de terminar: I have been learning to swim for two months. She has been working all day. Se usa for con una duración (for two months) y since con un punto de partida (since Monday). Con during se indica un período: during the summer.",
        "Para expresar acuerdo y desacuerdo, escribe I agree with + persona o idea, y I disagree with + persona o idea, seguido de because. Para opinar, escribe I believe that + oración o I believe in + sustantivo, y In my opinion... Para decir que algo es de alguien, usa posesivos y expresiones: This is mine, that is yours, it belongs to Marta. Para decir que te quedaste sin algo, usa I was left without my goggles.",
        "Cuida el tiempo: yesterday pide pasado simple; for y since con una acción que continúa piden presente perfecto continuo. Con be, el presente perfecto simple (has been) también se usa con since: The price has been the same since March. Antes de entregar, comprueba que cada for y since tenga la duración o el punto de partida correctos.",
    ],
    [("have been + -ing", "acción que empezó y continúa"), ("for / since / during", "durante / desde / durante un período"), ("I agree / disagree with", "estoy de acuerdo / en desacuerdo con"), ("I believe that / in", "creo que / en"), ("mine / yours / belongs to", "mío / tuyo / pertenece a"), ("I was left without", "me quedé sin")],
    [
        ("Elegir for o since", PC1 + " ¿Desde cuándo aprende a nadar?", ["La frase For two months muestra una duración.", "Aprende desde hace dos meses.", "Se usa for para la duración."], "Desde hace dos meses"),
        ("Acuerdo y desacuerdo", PC2 + " ¿Con quién está de acuerdo y con quién no el autor?", ["I agree with Laura.", "I disagree with Tomás.", "Cada postura tiene una razón."], "Está de acuerdo con Laura y en desacuerdo con Tomás"),
    ],
    [
        ("Decir I am learning to swim for two months.", "Para una duración que continúa se usa have been + -ing.", "Escribe I have been learning for two months."),
        ("Usar for con un punto de partida como Monday.", "For va con duración y since con punto de partida.", "Escribe since Monday."),
    ],
    [
        mr(PC1, "¿Qué le pasó al autor la semana pasada?", "Se quedó sin sus antiparras", ["Perdió su mochila en la piscina", "Cambió de profesora de natación"], "Dice I was left without my goggles."),
        mc("Completa: She has been working ____ eight o'clock.", "since", ["for", "during"], "Eight o'clock es un punto de partida."),
        mc("Completa: My cousin has been living here ____ last year.", "since", ["for", "during"], "Last year es un punto de partida."),
    ],
    [
        mr(PC2, "¿Qué cree el autor de los paseos cortos?", "Que cuestan menos", ["Que son aburridos", "Que son caros"], "Dice I believe in short trips because they cost less."),
        mr(PC3, "¿Desde cuándo prepara la señora Díaz el informe?", "Desde el lunes", ["Desde hace una hora", "Desde el domingo"], "Dice Since Monday."),
        mr(PC3, "¿Qué objeto se ofrece al lector si lo necesita mañana?", "La lámpara", ["La silla", "El escritorio"], "Dice the lamp is yours if you need it tomorrow."),
    ],
    [
        mc("Completa: I have been studying English ____ three years.", "for", ["since", "during"], "Three years es una duración."),
        mc("Completa: This notebook ____ to Marta.", "belongs", ["belong", "belonging"], "Con it se usa belongs."),
        mc("Completa con el tiempo correcto: He ____ for an hour.", "has been waiting", ["is waiting", "waits"], "La espera empezó antes y continúa."),
    ],
    [
        mr(PC2, "Un compañero dice que el precio subió. ¿Qué dato del foro lo contradice?", "Que el precio es el mismo desde marzo", ["Que Tomás dice que el bus es caro", "Que Laura piensa que el paseo es una buena idea"], "Dice the price has been the same since March."),
        mc("Otro compañero escribe: «This desk is she». ¿Qué corriges?", "This desk is hers", ["This desk is her", "This desk is herself"], "Hers es el posesivo que se usa solo."),
    ],
    [
        mr(PC1, "Reescribe: «I learn to swim two months ago». ¿Cuál es correcta?", "I started learning to swim two months ago", ["I have been learning to swim two months ago", "I am learning to swim since two months"], "Se usa pasado simple con ago."),
        arith("El autor lleva 2 meses aprendiendo a nadar y entrena 4 veces por semana durante 8 semanas. ¿Cuántas sesiones de entrenamiento hizo?", "4*8", "Se multiplica las sesiones semanales por las semanas.", " sesiones"),
    ],
    [mc("Quieres escribir que estás en desacuerdo con una idea y explicar por qué. ¿Qué oración es correcta?", "I disagree with the idea because it costs too much", ["I disagree the idea because it costs too much", "I am disagree with the idea because it costs too much"], "Disagree with + idea + because; sin with o con am la oración es incorrecta.")],
    [
        ("En Inglés de 2.º medio (OA 16, clase 3): ¿cómo se forma el presente perfecto continuo?", "Have o has been más verbo con -ing", "Muestra una acción que continúa."),
        ("En Inglés de 2.º medio (OA 16, clase 3): ¿qué usas con un punto de partida: for o since?", "Since", "Since Monday, since lunch."),
        ("En Inglés de 2.º medio (OA 16, clase 3): ¿cómo dices que estás de acuerdo con alguien?", "I agree with + persona", "No lleva am."),
    ],
    task("Escribe una entrada de diario de seis a ocho oraciones sobre algo que has estado haciendo últimamente (por ejemplo un hobby o un proyecto). Usa have been + -ing con for y since, I was left without, I believe that o in, I agree o disagree with y una expresión de posesión (belong to, mine, yours). Sigue este ejemplo.", "I have been drawing for two years. Since September, I have been practicing portraits. Last week, I was left without my pencils, so I borrowed my sister's. I believe in practicing every day. I agree with my teacher about patience. This sketchbook belongs to me.", ["usa have been + -ing con for y since", "usa acuerdo u opinión", "usa una expresión de posesión"], ["diario en la hoja"], ["usar for con un punto de partida", "I am agree"], "Pide que cambie for por since y ajuste la oración."),
    "Escribe cuatro oraciones con for y cuatro con since sobre actividades tuyas.",
    "Cuenta en español desde cuándo haces algo y cómo se diría en inglés.",
)

# ------------------------------------------------------------------ clase 4: unir ideas, énfasis y reporte
LK1 = "Correo: «Neither Pablo nor his friends are coming to the match, though they love soccer. Either we play at five or we cancel. I will call you as soon as I know. We will not play unless the field is dry. As a result, we need a plan B.» (match = partido, cancel = cancelar, field = cancha, dry = seca, plan B = plan alternativo)"
LK2 = "Carta: «My sister built the shelf herself. She did not ask for help, and she taught herself how to paint it. I told her that I was proud of her.» (shelf = repisa, built = construyó, ask for help = pedir ayuda, taught herself = aprendió sola, proud = orgulloso)"
LK3 = "Reporte: «Mr. Brown said he had finished the report. The coach told us to arrive early. Ana said she was tired. My mother told me to go home.» (report = informe, coach = entrenador, arrive = llegar, tired = cansada)"

lesson(
    OA, 4, MAT_R,
    "Aprenderé a escribir ideas unidas con neither ... nor, either ... or, though, unless, as soon as y as a result; a dar énfasis a quien realiza la acción con himself, herself y themselves; y a informar lo que otros dicen con said y told. Sirve para escribir textos claros y precisos.",
    ["Sé usar and, but, because y so.", "Conozco los pronombres reflexivos."],
    [
        "Los conectores unen ideas con una relación precisa. Neither ... nor niega las dos opciones; el verbo concuerda con el sujeto más cercano: Neither Pablo nor his friends are coming. Either ... or presenta dos opciones: Either we play at five or we cancel. Though, al final de una oración, es sin embargo. Unless es a menos que. As soon as es tan pronto como. As a result marca una consecuencia.",
        "Los pronombres reflexivos (myself, yourself, himself, herself, itself, ourselves, yourselves, themselves) dan énfasis a quien realiza la acción: My sister built the shelf herself. También indican que quien hace y quien recibe la acción son la misma persona: I am proud of myself. En el estilo indirecto (reported speech), cuentas lo que otros dijeron y el tiempo retrocede: Ana said she was tired (de I am tired). Mr. Brown said he had finished (de I have finished). Para órdenes usa told + persona + to + verbo: My mother told me to go home.",
        "Al escribir, elige un conector que diga la relación exacta. Revisa la concordancia con neither ... nor. Para el reporte, usa said sin persona y told con persona: She said she was tired; She told me she was tired.",
    ],
    [("neither ... nor / either ... or", "ni ... ni / o ... o"), ("though / unless", "sin embargo / a menos que"), ("as soon as / as a result", "tan pronto como / como resultado"), ("herself / themselves", "ella misma / ellos mismos"), ("said / told", "dijo / dijo a alguien"), ("reported speech", "estilo indirecto")],
    [
        ("Elegir el conector", LK1 + " ¿Qué condición se pone para jugar?", ["Busco unless.", "We will not play unless the field is dry.", "Solo se juega si la cancha está seca."], "Solo jugarán si la cancha está seca"),
        ("Reportar lo que dijo otra persona", LK3 + " ¿Qué dijo Ana realmente?", ["She said she was tired.", "El tiempo retrocede.", "Ana dijo: I am tired."], "Ana dijo: I am tired"),
    ],
    [
        ("Escribir She said me that she was tired.", "Con persona se usa told: She told me.", "Escribe She told me that she was tired o She said she was tired."),
        ("Escribir She built it itself.", "El reflexivo debe coincidir con el sujeto.", "Escribe She built it herself."),
    ],
    [
        mc("Completa: Neither the teacher nor the students ____ ready.", "are", ["is", "be"], "El verbo concuerda con students, el sujeto más cercano."),
        mc("Completa: My sister painted the room ____.", "herself", ["himself", "itself"], "Sister es ella."),
        mc("Completa: We cannot start ____ the field is dry.", "unless", ["as soon as", "though"], "Unless es a menos que."),
    ],
    [
        mr(LK1, "¿Qué opciones presenta either ... or?", "Jugar a las cinco o cancelar", ["Jugar a las cinco o a las seis", "Cancelar el partido o llamar a Pablo"], "Dice Either we play at five or we cancel."),
        mr(LK3, "¿Qué dijo el entrenador?", "Que llegáramos temprano", ["Que nos fuéramos a casa", "Que trajéramos agua al partido"], "The coach told us to arrive early."),
        mr(LK2, "¿Quién construyó la repisa?", "Su hermana, sola", ["El autor, con ayuda de su hermana", "Un carpintero que contrató su hermana"], "Herself da énfasis a que la hizo ella."),
    ],
    [
        mc("Convierte a estilo indirecto: «I am tired», said Ana. → Ana said she ____ tired.", "was", ["is", "has been"], "El presente retrocede a pasado."),
        mc("Convierte: «I have finished», said Mr. Brown. → Mr. Brown said he ____ finished.", "had", ["has", "was"], "Have finished retrocede a had finished."),
        mc("Convierte: Mom: «Go home». → Mom ____ me to go home.", "told", ["said", "tells"], "Told + persona + to + verbo."),
    ],
    [
        mr(LK1, "Un compañero escribe: «Neither Pablo nor his friends is coming». ¿Qué corriges?", "Is por are: friends es plural y está más cerca", ["Neither por either, porque hay dos opciones", "Friends por friend, porque Pablo es un solo nombre"], "Concordancia con el sujeto más cercano."),
        mr(LK3, "Otro compañero escribe: «Ana said me she was tired». ¿Qué corriges?", "Ana told me she was tired", ["Ana told to me she was tired", "Ana said me she is tired"], "Said no lleva persona directa; con persona se usa told."),
    ],
    [
        mr(LK2, "Reescribe con énfasis: «Ana made the cake». ¿Cuál es correcta?", "Ana made the cake herself", ["Ana made the cake herselves", "Ana made the cake himself"], "Herself enfatiza que lo hizo sola."),
        mc("Elige la oración con though al final con el sentido «sin embargo»:", "He looks tough. He is shy, though", ["He looks tough. He is shy, as a result", "He looks tough. He is shy, unless"], "Though al final de la oración significa sin embargo."),
    ],
    [mc("Escribes: Ms. Soto said, “I am proud of you.” ¿Cómo lo reportas?", "Ms. Soto said she was proud of us", ["Ms. Soto said she is proud of us", "Ms. Soto said she was proud of you"], "El tiempo retrocede y el pronombre cambia.")],
    [
        ("En Inglés de 2.º medio (OA 16, clase 4): ¿con qué sujeto concuerda el verbo en neither ... nor?", "Con el más cercano", "Es la regla de concordancia."),
        ("En Inglés de 2.º medio (OA 16, clase 4): ¿qué pronombre indica que ella lo hizo sola?", "Herself", "Da énfasis a quien actúa."),
        ("En Inglés de 2.º medio (OA 16, clase 4): ¿qué pasa con el tiempo en el estilo indirecto?", "Retrocede", "Am pasa a was."),
    ],
    task("Escribe un correo de siete a nueve oraciones a un compañero sobre un evento que se complicó. Usa neither ... nor (con la concordancia correcta), either ... or, unless, as soon as, as a result, un reflexivo con énfasis y dos oraciones en estilo indirecto. Sigue este ejemplo.", "Neither the coach nor the players are ready. Either we start at four or we move the game. We cannot start unless the field is dry. As soon as it dries, I will call you. Ana said she was tired. Our teacher told us to wait. We organized the day ourselves. As a result, we are very proud.", ["usa cinco conectores", "usa un reflexivo con énfasis", "reporta dos mensajes con retroceso de tiempo"], ["correo en la hoja"], ["error de concordancia con neither ... nor", "no retroceder el tiempo"], "Pide que cambie un conector por otro y explique cómo cambia el sentido."),
    "Escribe diez oraciones en estilo indirecto a partir de diez frases directas.",
    "Cuenta en español lo que alguien te dijo hoy y marca cómo cambiaría el tiempo en inglés.",
)

# ------------------------------------------------------------------ clase 5: pasado anterior, hipótesis y consejos
PH1 = "Mensaje a un amigo: «Yesterday I was late for school because I had missed the bus. First I ran to the station, but the next bus had already left. The driver said I should have left home earlier. If I were you, I would set two alarms.» (late = tarde, missed = perdí, ran = corrí, station = terminal, set = programar, alarms = alarmas)"
PH2 = "Carta de consejos: «Dear Sam, thanks for your letter. You said your friend has not spoken to you since your argument. If I were you, I would write her a short letter. By the way, my cousin is shy. He would meet more people if he spoke more English.» (argument = discusión, letter = carta, meet = conocer, shy = tímido)"
PH3 = "Relato: «Tomás did not have his ticket because he had left it at home. His brother told him to go back and look for it. At the station, an officer said the train had already left.» (ticket = pasaje, left = dejó, officer = funcionario, station = estación)"

lesson(
    OA, 5, MAT_R,
    "Aprenderé a escribir acciones que ocurrieron antes de otra en el pasado (had + participio), situaciones hipotéticas (If I were you, I would...; he would meet more people if he spoke English) y consejos. Sirve para contar hechos en orden y dar recomendaciones por escrito.",
    ["Sé usar el pasado simple.", "Conozco should y If I were you."],
    [
        "El pasado perfecto (had + participio) se usa cuando una acción pasada ocurrió antes de otra acción pasada. Siempre hay dos hechos: I was late because I had missed the bus. Primero perdí el bus (had missed) y después llegué tarde (was late). Sin un segundo hecho pasado, se usa el pasado simple. Las palabras already, before y by the time ayudan a mostrar el orden.",
        "Las situaciones hipotéticas se escriben con if + pasado simple, would + verbo: He would meet more people if he spoke English; We would arrive earlier if we took the first train. Expresan algo que no ocurre ahora o es poco probable. Para dar consejos usa If I were you, I would + verbo, y You should + verbo. Se usa were con todas las personas en esta estructura.",
        "Al contar lo que otros dijeron, el tiempo retrocede: An officer said the train had already left (de «The train has already left»). Should have + participio da un consejo sobre el pasado: I should have left earlier. Antes de entregar, revisa que cada had tenga su segundo hecho y que cada if lleve el verbo en pasado y would en la otra parte.",
    ],
    [("had + participio", "pasado perfecto: acción anterior"), ("already / before / by the time", "ya / antes / para cuando"), ("If + past, would + verb", "hipótesis"), ("If I were you, I would...", "consejo"), ("should have + participio", "debería haber"), ("said / told", "dijo / dijo a alguien")],
    [
        ("Orden de hechos", PH1 + " ¿Qué ocurrió primero: perdió el bus o llegó tarde?", ["Busco had missed.", "Esa acción es anterior a was late.", "Primero perdió el bus."], "Primero perdió el bus"),
        ("Consejo", PH1 + " ¿Qué consejo da el autor y con qué estructura?", ["Es un consejo hipotético.", "Usa If I were you, I would set two alarms.", "Recomienda programar dos alarmas."], "Programar dos alarmas, con If I were you, I would"),
    ],
    [
        ("Decir If I was you, I will write her.", "En consejos se usa were y would.", "Escribe If I were you, I would write her."),
        ("Usar had sin segundo hecho pasado.", "El pasado perfecto necesita dos hechos.", "Si solo hay un hecho, usa el pasado simple."),
    ],
    [
        mr(PH3, "¿Por qué Tomás no tenía su pasaje?", "Porque lo había dejado en casa", ["Porque no tenía dinero para comprarlo", "Porque lo había perdido en el tren"], "Dice because he had left it at home."),
        mr(PH3, "¿Qué dijo el funcionario?", "Que el tren ya había salido", ["Que el tren estaba por salir", "Que el pasaje era falso"], "Dice an officer said the train had already left."),
        mc("Completa: If I ____ you, I would call her.", "were", ["was", "am"], "En consejos se usa were."),
    ],
    [
        mr(PH2, "¿Qué consejo recibe Sam?", "Escribirle una carta corta a su amiga", ["Olvidar la discusión y no hablar más con ella", "Hablar con el profesor sobre la discusión"], "Dice I would write her a short letter."),
        mr(PH2, "¿Qué haría el primo si hablara más inglés?", "Conocería a más gente", ["Viajaría menos por la ciudad", "Hablaría menos con sus amigos"], "Dice he would meet more people if he spoke more English."),
        mr(PH1, "¿Qué ya había hecho el siguiente bus cuando el autor llegó al terminal?", "Ya había salido", ["Acababa de llegar al terminal", "Nunca llegó a pasar por ahí"], "Dice had already left."),
    ],
    [
        mc("Completa: Tomás did not have a ticket because he ____ it at home.", "had left", ["has left", "leaves"], "Dejar el pasaje ocurrió antes."),
        mc("Completa: We would arrive earlier if we ____ the first train.", "took", ["take", "will take"], "If + pasado simple."),
        mc("Completa: When we arrived at the cinema, the movie ____ already started.", "had", ["has", "was"], "Empezar ocurrió antes de llegar: had + participio."),
    ],
    [
        mr(PH1, "Un compañero dice que had missed significa que perderá el bus. ¿Qué respuesta es más acertada?", "No: significa que ya lo había perdido antes de llegar tarde", ["Sí: significa que lo perderá mañana, igual que will miss", "No: significa que lo pierde ahora mismo"], "Had + participio marca una acción anterior."),
        mc("Otro compañero escribe: «We would arrive earlier if we take the first train». ¿Qué corriges?", "Take por took, porque la condición va en pasado", ["Would por will, porque se habla del futuro", "Earlier por later, porque la hipótesis es sobre llegar tarde"], "La hipótesis necesita pasado en la condición."),
    ],
    [
        mr(PH3, "Une las ideas con pasado perfecto: «Tomás left his ticket at home. He did not have a ticket». ¿Cuál es correcta?", "Tomás did not have a ticket because he had left it at home", ["Tomás did not have a ticket because he has left it at home", "Tomás did not have a ticket because he leaves it at home"], "La acción anterior va con had left."),
        mr(PH2, "Escribe un consejo con la estructura de la clase para quien tiene un problema con un amigo. ¿Cuál es el mejor?", "If I were you, I would talk to him calmly", ["If I was you, I would to talk to him calmly", "If I were you, I will talk to him calmly"], "Usa If I were you, I would + verbo."),
    ],
    [mc("Escribes: «The coach said I ____ more water». ¿Qué forma está bien en estilo indirecto?", "should drink", ["should to drink", "have drunk"], "Should va con verbo sin to.")],
    [
        ("En Inglés de 2.º medio (OA 16, clase 5): ¿qué necesita el pasado perfecto para usarse?", "Dos hechos pasados, uno anterior al otro", "Marca el orden."),
        ("En Inglés de 2.º medio (OA 16, clase 5): ¿cómo se forma una hipótesis?", "If + pasado simple, would + verbo", "Expresa algo imaginario."),
        ("En Inglés de 2.º medio (OA 16, clase 5): ¿qué forma de be usa If I ___ you?", "Were", "Se usa en consejos."),
    ],
    task("Escribe un texto de siete a nueve oraciones con tres partes: 1) un relato breve con pasado perfecto y un segundo hecho pasado (por ejemplo por qué llegaste tarde o perdiste algo); 2) un consejo con If I were you, I would; 3) una hipótesis con if + pasado, would. Sigue este ejemplo.", "Last Friday I could not call my friend because I had left my phone at school. I walked back, but the building was already closed. I waited at the gate for twenty minutes. If I were you, I would check my bag before leaving. You should always keep a note with phone numbers. If I had a second phone, I would not worry. In the end, the guard let me use his phone.", ["usa had + participio con un segundo hecho", "escribe un consejo con If I were you", "escribe una hipótesis con if + pasado"], ["texto en la hoja"], ["usar had sin segundo hecho", "decir If I was"], "Pide que cambie el consejo por otra opción posible."),
    "Escribe cinco oraciones con had + participio y su segundo hecho pasado.",
    "Piensa en un problema de un amigo y escribe en español un consejo que luego traducirás con If I were you.",
)
