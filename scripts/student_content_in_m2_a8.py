"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 08: funciones comunicativas del año al hablar.

Diálogos y presentaciones breves escritos en el enunciado; el estudiante elige o completa lo que diría. Inglés americano
(uso formal moderado). Los títulos de clase del plan son genéricos; aquí se aplican a cantidad y expresiones comunes,
frecuencia, tiempo y acciones que continúan, sugerencias, ofrecimientos y acuerdo, conectores y énfasis, y pasado anterior,
estilo indirecto e hipótesis.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 08"

# ------------------------------------------------------------------ clase 1: cantidad, enumeración y expresiones comunes
WK1 = "«At the school fair, a large number of families came, but only a small number bought tickets for the raffle. There was little time left, and few prizes remained.» (fair = feria, raffle = rifa, prizes = premios, remained = quedaron)"
Q1 = "«Clerk: Welcome to the stationery shop. Student: I'm looking for pens. Do you have a large number of colors? Clerk: Yes, but there are few blue pens today. We have a little black ink left, and there is little red ink. Student: The black pens are cheap enough, and I'll take a few.» (stationery shop = papelería, clerk = vendedora, pens = lápices pasta, ink = tinta, cheap = barato)"
Q2 = "«Nora: Do you like cooking? Leo: Not at all. I hardly ever cook. I'd rather order food online. Nora: I'm pleased that you're honest. I have been looking for a cooking partner for ages.» (cooking = cocinar, order = pedir, online = en línea, honest = sincero, partner = compañero, for ages = hace mucho)"
Q3 = "«Mia: I'm sorry about the delay. Is this your bag? Tom: Yes. Could you look after it while I look for my ticket? Mia: Sure. And you can buy it online next time. It is cheap enough.» (delay = demora, look after = cuidar, look for = buscar, ticket = pasaje, cheap enough = suficientemente barato)"

lesson(
    OA, 1, MAT_R,
    "Aprenderé a expresar cantidad, contar y enumerar (a few, few, little, a large number of), y a usar expresiones comunes como hardly ever, at all, for ages, sorry about, look for y online. Sirve para hablar con precisión y de forma natural.",
    ["Sé usar there is y there are.", "Conozco muchas palabras de uso diario."],
    [
        "Para hablar de cantidad en cosas contables usa a large number of y a small number of: a large number of students. También sirven few (casi no hay) y a few (hay algunos): there are few seats; there are a few seats. Para cosas incontables usa little (casi no hay) y a little (hay un poco): there is little sugar; there is a little sugar. Para enumerar usa first, second, third y finally. Enough va después de un adjetivo: cheap enough; y antes de un sustantivo: enough time.",
        "Hay expresiones comunes que conviene aprender completas: hardly ever (casi nunca), not at all (en absoluto), I'd rather (preferiría), for ages (hace mucho tiempo), I'm pleased (me alegra), sorry about (lamento lo de), look for (buscar), look after (cuidar) y online (en línea). Look for no es lo mismo que look after: look for busca algo; look after cuida algo o a alguien.",
        "Rather, quite y very indican grado: he is rather shy (bastante tímido). Soon significa pronto: Susan will be here soon. Cuando hables, elige la expresión que dice la cantidad exacta. Few y little suenan negativos; a few y a little suenan positivos. Los sinónimos son palabras con significado parecido: cheap e inexpensive. Las palabras compuestas unen dos palabras: notebook, classroom y online.",
    ],
    [("a large / small number of", "una gran / pequeña cantidad de (contables)"), ("few / a few", "pocos / algunos"), ("little / a little", "poco / un poco"), ("enough", "suficiente"), ("hardly ever / not at all", "casi nunca / en absoluto"), ("look for / look after", "buscar / cuidar"), ("synonym / compound word", "sinónimo / palabra compuesta")],
    [
        ("Elegir few o a few", WK1 + " ¿Cuántos premios quedaron y qué suena positivo o negativo?", ["Dice few prizes remained.", "Few suena negativo: casi no quedaron.", "Con a few sería positivo."], "Casi no quedaron premios; few suena negativo"),
        ("Elegir un incontable", WK1 + " ¿Qué significa there was little time left?", ["Time es incontable.", "Little significa casi nada.", "Quedaba muy poco tiempo."], "Quedaba muy poco tiempo"),
    ],
    [
        ("Decir few sugar.", "Sugar es incontable; few va con contables.", "Usa little sugar."),
        ("Confundir look for con look after.", "Uno busca, el otro cuida.", "Look for = buscar; look after = cuidar."),
    ],
    [
        mc("Completa: There are ____ seats left, so hurry.", "a few", ["a little", "much"], "Seats es contable y hay algunos."),
        mc("Completa: There is ____ sugar in the jar, so we need to buy more.", "little", ["few", "many"], "Sugar es incontable y casi no queda."),
        mr(Q2, "¿Qué significa Not at all?", "En absoluto", ["Sí, mucho", "Tal vez"], "Not at all niega por completo."),
    ],
    [
        mr(Q1, "¿Qué dice la vendedora de los lápices azules?", "Que hay pocos hoy", ["Que hay muchos", "Que no hay ninguno"], "Dice there are few blue pens today."),
        mr(Q3, "¿Qué le pide Tom a Mia con look after?", "Que cuide su bolso", ["Que busque su bolso", "Que compre un bolso"], "Look after significa cuidar."),
        mr(Q2, "¿Con qué frecuencia cocina Leo?", "Casi nunca", ["Siempre", "Todos los días"], "Hardly ever significa casi nunca."),
    ],
    [
        mr(Q1, "¿Qué significa cheap enough?", "Suficientemente barato", ["Demasiado caro", "Muy pequeño"], "Enough después del adjetivo indica suficiente."),
        mc("Completa: A ____ number of students joined the club.", "large", ["much", "few"], "Large number of va con contables."),
        mc("Completa para enumerar los pasos: First, we mix the flour. ____, we add the eggs. Finally, we bake the cake.", "Second", ["Two", "Twice"], "Second sigue a first cuando se enumeran pasos."),
    ],
    [
        mr(Q1, "Un compañero dice que a little black ink significa que no queda nada de tinta negra. ¿Qué respuesta es mejor?", "A little significa que queda un poco, no nada", ["Tiene razón: significa nada", "Significa que quedan muchas"], "A little tiene un sentido positivo."),
        mc("¿Qué par de palabras tiene casi el mismo significado?", "cheap e inexpensive", ["cheap y expensive, que se usan para precios", "few y many, que se usan con cosas contables"], "Inexpensive es un sinónimo de cheap."),
    ],
    [
        mr(WK1, "¿Cuál es la oración que dice mejor la situación de la rifa?", "A large number of families came, but few bought tickets", ["A small number of families came, but a lot bought tickets", "No families came to the fair, so nobody bought tickets"], "A large number of families y a small number que compraron."),
        arith("En una feria, 120 familias fueron y solo 30 compraron entradas para la rifa. ¿Cuántas no compraron?", "120-30", "Se resta el grupo que compró del total.", " familias"),
    ],
    [mr(Q3, "Mia dice I'm sorry about the delay. ¿Qué expresa?", "Lamenta la demora", ["Se alegra de la demora", "No le importa"], "Sorry about expresa lamento.")],
    [
        ("En Inglés de 2.º medio (OA 8, clase 1): ¿qué diferencia hay entre few y a few?", "Few es casi ninguno; a few es algunos", "La a cambia el sentido."),
        ("En Inglés de 2.º medio (OA 8, clase 1): ¿qué significa for ages?", "Hace mucho tiempo", "Es una expresión común."),
        ("En Inglés de 2.º medio (OA 8, clase 1): ¿cuándo se usa little?", "Con cosas incontables", "Little sugar, little time."),
    ],
    task("Escribe en inglés un diálogo de seis líneas entre un cliente y un vendedor de una tienda de ropa. Usa a large number of, few, a little o little, enough, look for y online. Léelo con un adulto en voz alta. Sigue este ejemplo.", "Customer: I'm looking for a jacket. Seller: We have a large number of jackets, but few in your size. Customer: Is this one cheap enough? Seller: Yes, and you can buy it online too.", ["usa al menos cinco expresiones de la clase", "las expresiones tienen sentido", "el diálogo se entiende al leerlo"], ["diálogo en la hoja", "nota del adulto"], ["usar few con incontables", "confundir look for con look after"], "Pide que cambie few por a few y explique qué cambió."),
    "Escribe cinco oraciones con a large number of, a small number of, few, little y enough.",
    "Cuenta cuántas veces escuchas hardly ever o not at all en canciones o series durante la semana.",
)

# ------------------------------------------------------------------ clase 2: frecuencia, tiempo y acciones que continúan
H1 = "«Interviewer: How often do you practice swimming? Carla: I usually practice three times a week. Interviewer: How long have you been training? Carla: We have been training for three months. My coach has been working with us all week.» (practice = practicar, training = entrenando, coach = entrenador)"
H2 = "«Sofía: Is Pablo here? Marta: Not yet, but he will be here soon. He has been working during the summer, and he is rather tired.» (not yet = todavía no, soon = pronto, rather = bastante, tired = cansado)"
H3 = "«Neighbor: How often does the bus come? Mrs. Díaz: Every fifteen minutes in the morning, but only once an hour at night. I have been waiting for twenty minutes already.» (neighbor = vecino, only = solo)"
H4 = "«Luis: Have you finished the report? Rosa: Not yet. I have been writing it since lunch. It is rather long.» (report = informe, since = desde, lunch = almuerzo, long = largo)"

lesson(
    OA, 2, MAT_R,
    "Aprenderé a describir frecuencia (usually, often, how often), tiempo (soon, during, since, for) y acciones que empezaron en el pasado y continúan o acaban de terminar (have been + -ing). Sirve para contar hábitos y cuánto tiempo llevas haciendo algo.",
    ["Sé usar el presente simple.", "Conozco los adverbios always, sometimes y never."],
    [
        "Para preguntar por frecuencia usa How often...? y se responde con adverbios (always, usually, often, sometimes, hardly ever, never) o con expresiones (three times a week, once a month, every fifteen minutes). Los adverbios van antes del verbo principal: I usually call her in the morning. Con be, van después: He is often late. El grado se dice con rather, quite o very: he is rather shy.",
        "Para decir que una acción empezó en el pasado y continúa ahora, o acaba de terminar, usa el presente perfecto continuo: have/has been + verbo con -ing. We have been training for three months. She has been working all day. Se usa for con una duración (for three months, for two hours) y since con un punto de partida (since Monday, since lunch). During va con un período: during the summer.",
        "Soon significa pronto y se usa con will: Susan will be here soon. No confundas how often (con qué frecuencia) con how long (cuánto tiempo). How often pide frecuencia; how long pide duración.",
    ],
    [("How often...?", "¿con qué frecuencia...?"), ("usually / often / hardly ever", "usualmente / a menudo / casi nunca"), ("have been + -ing", "llevo haciendo algo"), ("for / since", "durante / desde"), ("during", "durante un período"), ("soon", "pronto")],
    [
        ("Preguntar y responder frecuencia", H1 + " ¿Con qué frecuencia practica Carla?", ["La pregunta es How often.", "La respuesta es three times a week.", "Es la frecuencia."], "Tres veces por semana"),
        ("Duración con presente perfecto continuo", H1 + " ¿Cuánto tiempo llevan entrenando?", ["La pregunta es How long.", "Dice we have been training for three months.", "For marca la duración."], "Tres meses"),
    ],
    [
        ("Decir I am working for three months.", "Para una duración que continúa se usa el presente perfecto continuo.", "Di I have been working for three months."),
        ("Usar for con un punto de partida como Monday.", "For va con duración; since con el punto de partida.", "Di since Monday."),
    ],
    [
        mc("¿Cuál pregunta pide frecuencia?", "How often do you practice?", ["How long have you practiced?", "Where do you practice?"], "How often pide frecuencia."),
        mc("¿Cuál oración está bien escrita?", "I usually call her in the morning", ["I call usually her in the morning", "I am usually call her in the morning"], "El adverbio va antes del verbo principal."),
        mr(H2, "¿Cuándo llegará Pablo?", "Pronto", ["Ayer", "Nunca"], "Dice he will be here soon."),
    ],
    [
        mr(H3, "¿Cada cuánto pasa el bus de noche?", "Una vez por hora", ["Cada quince minutos", "Dos veces por hora"], "Dice only once an hour at night."),
        mr(H4, "¿Desde cuándo escribe Rosa su informe?", "Desde el almuerzo", ["Desde hace una semana", "Desde la noche"], "Dice since lunch."),
        mr(H2, "¿Qué estuvo haciendo Pablo durante el verano?", "Trabajando", ["Estudiando", "Viajando"], "Dice he has been working during the summer."),
    ],
    [
        mc("Completa: We ____ training for three months.", "have been", ["are", "were being"], "Se usa have been + -ing."),
        mc("Completa: She has been working ____ eight o'clock.", "since", ["for", "during"], "Eight o'clock es un punto de partida."),
        mc("Completa: He has been waiting ____ two hours.", "for", ["since", "during"], "Two hours es una duración."),
    ],
    [
        mr(H3, "Mrs. Díaz dice I have been waiting for twenty minutes already. ¿Qué significa?", "Espera desde hace veinte minutos y aún espera", ["Esperó veinte minutos y se fue", "Va a esperar veinte minutos"], "El presente perfecto continuo indica que sigue esperando."),
        mr(H1, "Un compañero dice que My coach has been working with us all week significa que ya terminó de trabajar. ¿Qué respuesta es mejor?", "Trabajó toda la semana y sigue trabajando", ["Significa que terminó de trabajar ayer", "Significa que trabajará toda la semana próxima"], "Has been working indica acción que continúa."),
    ],
    [
        mr(H4, "Rosa dice que el informe es rather long. ¿Qué significa rather?", "Bastante", ["Nada", "Poco"], "Rather indica un grado moderado."),
        arith("Carla practica 3 veces por semana durante 4 semanas. ¿Cuántas veces practica en total?", "3*4", "Se multiplica la frecuencia semanal por las semanas.", " veces"),
    ],
    [mc("Quieres preguntar con qué frecuencia alguien lee. ¿Qué frase eliges?", "How often do you read?", ["How long do you read?", "When do you reading?"], "How often pide la frecuencia.")],
    [
        ("En Inglés de 2.º medio (OA 8, clase 2): ¿qué forma expresa una acción que empezó y continúa?", "Have/has been + -ing", "Es el presente perfecto continuo."),
        ("En Inglés de 2.º medio (OA 8, clase 2): ¿cuándo se usa since?", "Con un punto de partida", "Since Monday, since lunch."),
        ("En Inglés de 2.º medio (OA 8, clase 2): ¿cuál es el significado de hardly ever?", "Casi nunca", "Es frecuencia muy baja."),
    ],
    task("Con un adulto como entrevistador, responde en voz alta: 1) How often do you practice a sport or a hobby? 2) How long have you been doing it? 3) What have you been doing this week? Escribe tus tres respuestas en inglés con un adverbio de frecuencia, for o since y have been + -ing. Sigue este ejemplo.", "1) I usually practice drawing twice a week. 2) I have been drawing for three years. 3) This week I have been practicing portraits.", ["usa un adverbio de frecuencia", "usa for o since correctamente", "usa have been + -ing"], ["tres respuestas en la hoja", "nota del adulto"], ["usar I am doing en lugar de have been", "usar for con un punto de partida"], "Pide que cambie for por since y ajuste la oración."),
    "Escribe cinco oraciones con always, usually, often, sometimes y hardly ever sobre ti.",
    "Pregunta a una persona de tu casa cuánto tiempo lleva en su trabajo o en un hobby y escribe en español su respuesta.",
)

# ------------------------------------------------------------------ clase 3: sugerencias, ofrecimientos, solicitudes y acuerdo
S1 = "«Ben: I'm tired and hungry. Eva: Would you like something to eat? Ben: Yes, please. Eva: Shall I bring you a sandwich? Ben: Thanks. And could you open the window?» (hungry = con hambre, bring = traer, sandwich = sándwich, open = abrir, window = ventana)"
S2 = "«Teo: Tomás is angry with me. Rita: You ought to talk to him. Teo: I don't know how to start. Rita: If I were you, I would say sorry first.» (angry = enojado, ought to = deberías, start = empezar, sorry = perdón)"
S3 = "«Leader: We need a name for our group. Pia: I suggest Blue Team. Lía: I disagree with Blue Team because it is too common. Bruno: I agree with Lía. How about Sunrise?» (leader = líder, name = nombre, group = grupo, suggest = sugerir, common = común, sunrise = amanecer)"
S4 = "«Assistant: Good afternoon. Can I help you? Customer: Yes. Could you tell me where the bank is? Assistant: Of course. Go straight and turn left. Customer: Thank you. Would you mind drawing a map? Assistant: Not at all.» (assistant = encargado, bank = banco, turn left = gira a la izquierda, map = mapa, would you mind = ¿te importaría?)"

lesson(
    OA, 3, MAT_R,
    "Aprenderé a hacer ofrecimientos (Would you like...? Shall I...?), sugerencias (You ought to..., How about...?), solicitudes (Could you...?) y a expresar acuerdo o desacuerdo (I agree/disagree with...). Sirve para conversar con cortesía y llegar a acuerdos.",
    ["Sé usar can y should.", "Conozco please y thank you."],
    [
        "Para ofrecer algo usa Would you like...? o Shall I...?: Would you like something to eat? Shall I bring you a glass of water? Para sugerir usa You ought to + verbo, You should + verbo, How about + -ing o I suggest + sustantivo: You ought to talk to him; How about meeting at six? Para hacer una solicitud cortés usa Could you...? o Would you mind + -ing?: Could you open the window? Would you mind drawing a map?",
        "Para responder a una solicitud usa Sure, Of course o Not at all (si la pregunta es Would you mind...?). Para expresar acuerdo usa I agree with + persona o idea: I agree with Lía. Para desacuerdo usa I disagree with + idea y agrega because: I disagree with Blue Team because it is too common. También puedes proponer otra opción: How about Sunrise?",
        "Elige la forma según la situación. Con amigos, How about...? y Do you want...? son naturales; con adultos, Would you like...? y Could you...? son más corteses. Shall I...? sirve con todos. Termina siempre con una respuesta amable y clara.",
    ],
    [("Would you like...?", "¿te gustaría...? (ofrecer)"), ("Shall I...?", "¿quieres que yo...? (ofrecer)"), ("You ought to / You should", "deberías"), ("How about...?", "¿qué tal si...?"), ("Could you...? / Would you mind...?", "¿podrías...? / ¿te importaría...?"), ("I agree / disagree with", "estoy de acuerdo / en desacuerdo con")],
    [
        ("Ofrecer ayuda", S1 + " ¿Qué ofrece Eva y cómo?", ["Usa Would you like something to eat?", "Luego usa Shall I bring you a sandwich?", "Son dos ofrecimientos."], "Ofrece algo de comer y traer un sándwich"),
        ("Acuerdo y desacuerdo", S3 + " ¿Quién está en desacuerdo y con qué?", ["Lía dice I disagree with Blue Team.", "Su razón es que es demasiado común.", "Bruno está de acuerdo con Lía."], "Lía está en desacuerdo con Blue Team porque es muy común"),
    ],
    [
        ("Usar You must en lugar de You ought to para aconsejar.", "You must es una orden dura.", "Usa You ought to o You should."),
        ("Responder Yes a Would you mind...? queriendo ayudar.", "Yes significa que sí te importa.", "Responde Not at all o Sure."),
    ],
    [
        mc("¿Qué frase ofrece algo de comer?", "Would you like something to eat?", ["Could you eat something?", "You ought to eat"], "Would you like...? ofrece."),
        mc("¿Qué frase pide con cortesía abrir la ventana?", "Could you open the window?", ["Open the window now", "Shall you open the window"], "Could you...? es una solicitud cortés."),
        mr(S2, "¿Qué sugiere Rita?", "Que hable con Tomás", ["Que no le hable", "Que se vaya"], "Dice You ought to talk to him."),
    ],
    [
        mr(S3, "¿Qué nombre propone Bruno?", "Sunrise", ["Blue Team", "Common"], "Bruno dice How about Sunrise?"),
        mr(S4, "¿Qué le pide el cliente al final?", "Que dibuje un mapa", ["Que llame un taxi", "Que cierre el banco"], "Dice Would you mind drawing a map?"),
        mr(S1, "¿Qué solicitud hace Ben?", "Que abra la ventana", ["Que traiga agua", "Que apague la luz"], "Dice could you open the window?"),
    ],
    [
        mc("Alguien pregunta «Would you mind drawing a map?». ¿Qué respuesta es cortés y afirmativa?", "Not at all", ["Yes, I do mind", "No, thanks"], "Not at all significa que no hay problema."),
        mc("Completa: Shall I ____ you a glass of water?", "bring", ["to bring", "bringing"], "Shall I va seguido de verbo sin to."),
        mc("Completa: I ____ with Lía because her idea is original.", "agree", ["am agree", "agreeing"], "Agree no lleva am."),
    ],
    [
        mr(S2, "Un compañero dice que If I were you, I would say sorry first es una orden. ¿Qué respuesta es más acertada?", "Es un consejo, no una orden", ["Es una orden dura", "Es un ofrecimiento"], "If I were you, I would... aconseja."),
        mr(S3, "¿Por qué Pia propone Blue Team y Lía no está de acuerdo?", "Porque Lía piensa que Blue Team es muy común", ["Porque Lía no quiere nombre", "Porque Pia no sabe inglés"], "Lía da su razón con because."),
    ],
    [
        mr(S4, "Un compañero dice que el encargado respondió con descortesía. ¿Qué dato lo contradice?", "Responde Of course y Not at all", ["Da indicaciones: Go straight and turn left", "Menciona el banco y el mapa del lugar"], "Responde con cortesía a las dos solicitudes."),
        mc("Quieres proponer una alternativa a una idea que no te gusta. ¿Qué frase usas?", "I disagree because it is expensive. How about another one?", ["That's silly. Why do you always say such things?", "You must change it, because I don't like your idea"], "Combina desacuerdo con razón y una propuesta."),
    ],
    [mc("Tu amigo está nervioso por un examen. Elige la respuesta que ofrece ayuda y aconseja.", "Would you like help? You ought to review your notes", ["Don't worry about it. You must pass the exam!", "You must pass. Why are you nervous about a test?"], "Ofrece y aconseja con cortesía.")],
    [
        ("En Inglés de 2.º medio (OA 8, clase 3): ¿qué frase sirve para ofrecer ayuda?", "Shall I help you?", "Shall I ofrece una acción."),
        ("En Inglés de 2.º medio (OA 8, clase 3): ¿qué respondes a Would you mind...? si no hay problema?", "Not at all", "Significa que no te importa."),
        ("En Inglés de 2.º medio (OA 8, clase 3): ¿qué se agrega a I disagree para justificarlo?", "Because y una razón", "Una razón apoya el desacuerdo."),
    ],
    task("Con un adulto, practica una conversación de ocho líneas sobre elegir una actividad para el fin de semana. Debes: ofrecer algo (Would you like...?), sugerir (How about...? o You ought to...), hacer una solicitud (Could you...?) y expresar acuerdo y desacuerdo con razón. Escribe el diálogo antes de decirlo en voz alta. Sigue este ejemplo.", "A: Would you like to go out? B: How about the park? A: I disagree with the park because it may rain. How about the movie theater? Could you check the times? B: Sure. I agree with the movie theater.", ["incluye ofrecimiento, sugerencia y solicitud", "expresa acuerdo y desacuerdo con razón", "mantiene la cortesía"], ["diálogo escrito en la hoja", "nota del adulto"], ["decir You must", "dar desacuerdo sin razón"], "Pide que cambie la solicitud por un Would you mind...?"),
    "Escribe cuatro ofrecimientos y cuatro solicitudes cortés en inglés.",
    "Observa cómo se piden cosas en una tienda y anota en español dos frases corteses.",
)

# ------------------------------------------------------------------ clase 4: unir ideas y dar énfasis
U1 = "«Mayra: Neither Pedro nor his sisters are at the party. Dani: Why? Mayra: It's raining today. As a result, the roads are slow. Dani: Pedro looks tough, he is shy, though.» (party = fiesta, roads = caminos, slow = lentos, tough = rudo, shy = tímido)"
U2 = "«Coach: We wouldn't play unless the field was dry. Captain: We can start as soon as it stops raining. Coach: Either we play today or we wait until Saturday.» (field = cancha, dry = seca, stops raining = deja de llover, wait = esperar)"
U3 = "«Sam: Did you make this shelf yourself? Joe: Yes, I made it myself. My sister taught herself to paint, so she painted the shelf herself.» (shelf = repisa, taught herself = aprendió sola, paint = pintar)"
U4 = "«The students organized the fair themselves. The teacher didn't help them. They were proud of themselves.» (organized = organizaron, fair = feria, proud = orgullosos)"

lesson(
    OA, 4, MAT_R,
    "Aprenderé a unir ideas con neither ... nor, either ... or, though, unless, as soon as y as a result, y a dar énfasis a quién realiza la acción con pronombres como myself y themselves. Sirve para hablar con claridad sobre causas, condiciones y quién hizo algo.",
    ["Sé usar and, but, because y so.", "Conozco los pronombres I, you, he y she."],
    [
        "Neither ... nor niega las dos opciones y el verbo concuerda con el sujeto más cercano: Neither Pedro nor his sisters are at the party. Either ... or presenta dos opciones: Either we play today or we wait. Though, al final de la oración, significa sin embargo: he looks tough, he is shy, though. Unless significa a menos que: we wouldn't play unless the field was dry. As soon as significa tan pronto como, y as a result introduce una consecuencia.",
        "Para dar énfasis a quién hace una acción usamos pronombres reflexivos: myself, yourself, himself, herself, itself, ourselves, yourselves, themselves. Did you make it yourself? significa ¿lo hiciste tú solo? She taught herself to paint significa aprendió sola. Los reflexivos también muestran que la persona que hace y la que recibe la acción son la misma: They were proud of themselves.",
        "No olvides la concordancia: yourself es singular y yourselves es plural. Himself y herself dependen de quién hace la acción. Si no hay énfasis, no se necesita el reflexivo. Cuando hables, elige el conector que dice la relación exacta entre tus ideas.",
    ],
    [("neither ... nor / either ... or", "ni ... ni / o ... o"), ("though", "sin embargo (al final)"), ("unless", "a menos que"), ("as soon as", "tan pronto como"), ("myself / yourself / herself", "yo mismo / tú mismo / ella misma"), ("themselves", "ellos mismos")],
    [
        ("Elegir el conector", U2 + " ¿Qué condición pone el entrenador para jugar?", ["Busco unless.", "Dice we wouldn't play unless the field was dry.", "Solo jugarán si la cancha está seca."], "Solo juegan si la cancha está seca"),
        ("Énfasis con un reflexivo", U3 + " ¿Quién hizo la repisa y cómo se enfatiza?", ["Joe dice I made it myself.", "Myself enfatiza que él la hizo solo.", "La pregunta original usaba yourself."], "Joe la hizo solo; se enfatiza con myself"),
    ],
    [
        ("Decir Neither Pedro nor his sisters is at the party.", "El verbo debe concordar con sisters, el sujeto más cercano.", "Di Neither Pedro nor his sisters are at the party."),
        ("Decir He taught him to paint cuando aprendió solo.", "Se necesita el reflexivo para decir que él mismo se enseñó.", "Di He taught himself to paint."),
    ],
    [
        mc("Completa: Neither the coach nor the players ____ ready.", "are", ["is", "be"], "Players es el sujeto más cercano y es plural."),
        mc("Completa: Did you make it ____?", "yourself", ["you", "your"], "Yourself da énfasis."),
        mr(U1, "¿Qué conector marca contraste?", "though", ["so", "neither"], "Though contrasta tough con shy."),
    ],
    [
        mr(U1, "¿Quiénes no están en la fiesta?", "Ni Pedro ni sus hermanas", ["Solo Pedro", "Solo sus hermanas"], "Neither ... nor niega a todos."),
        mr(U2, "¿Qué dos opciones da el entrenador con either ... or?", "Jugar hoy o esperar hasta el sábado", ["Jugar hoy o ir a casa", "Esperar o cancelar"], "Dice either we play today or we wait until Saturday."),
        mr(U4, "¿Quién organizó la feria?", "Los estudiantes solos", ["La profesora", "Los padres"], "Themselves enfatiza que lo hicieron ellos mismos."),
    ],
    [
        mc("Completa: We will not go to the park ____ it stops raining.", "unless", ["as a result", "neither"], "Unless indica la condición: solo si deja de llover."),
        mc("Completa: My sister built the table ____.", "herself", ["himself", "itself"], "Sister es femenino."),
        mc("Completa: I will call you as soon as I ____ home.", "get", ["will get", "am getting"], "Con as soon as se usa el presente simple para un hecho futuro."),
    ],
    [
        mr(U1, "Un compañero dice que as a result introduce la causa de la lluvia. ¿Qué respuesta es más acertada?", "Introduce la consecuencia: caminos lentos", ["Introduce la causa: el hecho de que llueve hoy", "Introduce un contraste entre lluvia y caminos"], "Dice It's raining today. As a result, the roads are slow."),
        mr(U3, "¿Por qué Joe dice «My sister painted the shelf herself» y no «painted it»?", "Para enfatizar que ella lo hizo sin ayuda", ["Porque la repisa es suya", "Porque herself es obligatorio"], "El reflexivo da énfasis."),
    ],
    [
        mc("Une las ideas con unless: «I will go. It does not rain».", "I will go unless it rains", ["I will go unless it does not rain", "I will go unless rain"], "Unless significa if not: voy a menos que llueva."),
        mr(U4, "¿Por qué se usa themselves en They were proud of themselves?", "Porque sujeto y objeto son las mismas personas", ["Se usa por error, porque They ya es el sujeto", "Se debería quitar, porque ya se sabe quiénes son"], "Themselves refleja la acción sobre ellos."),
    ],
    [mr(U1 + " " + U2, "Elige la pareja de oraciones correcta: una con neither ... nor sobre la fiesta y otra con either ... or sobre el partido.", "Neither Pedro nor his sisters are at the party. Either we play today or we wait", ["Neither Pedro nor his sisters is at the party. Either we play today or we wait", "Either Pedro or his sisters are at the party. Neither we play today or we wait"], "Hay que respetar la concordancia.")],
    [
        ("En Inglés de 2.º medio (OA 8, clase 4): ¿con qué sujeto concuerda el verbo en neither ... nor?", "Con el más cercano", "Es la regla de concordancia."),
        ("En Inglés de 2.º medio (OA 8, clase 4): ¿qué significa unless?", "A menos que", "Es una condición negativa."),
        ("En Inglés de 2.º medio (OA 8, clase 4): ¿qué pronombre usas para decir que ella lo hizo sola?", "Herself", "Da énfasis a quien actúa."),
    ],
    task("Con un adulto, practica una conversación corta de seis líneas sobre un proyecto que un grupo hizo solo. Debes usar un conector (neither ... nor, either ... or, though, unless, as soon as o as a result) y dos pronombres con énfasis (myself, yourself, herself, themselves...). Escribe el diálogo y dilo en voz alta. Sigue este ejemplo.", "A: Did you build this model yourself? B: Yes, we built it ourselves. Neither the teacher nor my parents helped us. A: It looks great, though. B: We will finish as soon as we paint it.", ["usa un conector del año", "usa dos pronombres reflexivos con énfasis", "respeta la concordancia"], ["diálogo en la hoja", "nota del adulto"], ["error de concordancia con neither ... nor", "usar el reflexivo equivocado"], "Pide que cambie un conector por otro y ajuste el sentido."),
    "Escribe cinco oraciones con himself, herself, itself, yourselves y themselves.",
    "Escribe en español dos cosas que hiciste tú solo esta semana y dilo con un reflexivo en inglés.",
)

# ------------------------------------------------------------------ clase 5: acciones anteriores, estilo indirecto e hipótesis
R1 = "«Reporter: Why was the shop closed? Neighbor: The owner didn't have money to pay the rent because he had lost his wallet. Then the landlord told him to leave.» (reporter = periodista, closed = cerrada, rent = arriendo, wallet = billetera, landlord = dueño del local, leave = irse)"
R2 = "«Ms. Brown said she had finished the report before the meeting. Mr. Silva told us to wait in the hall. Pablo asked if the director was ready.» (report = informe, meeting = reunión, hall = pasillo, director = director, ready = listo)"
R3 = "«If I were you, I would tell her the truth. He would meet more people if he spoke English. We would arrive earlier if we took the first bus.» (truth = verdad, meet = conocer, earlier = más temprano, first = primero)"
R4 = "«Anna said she was tired. Luis told me he had finished his project. My mother told me to go home.» (tired = cansada, project = proyecto, go home = irme a casa)"

lesson(
    OA, 5, MAT_R,
    "Aprenderé a hablar de acciones que ocurrieron antes de otra en el pasado (had + participio), a informar lo que otros dicen (said, told) y a plantear situaciones hipotéticas y consejos (If I were you, I would...). Sirve para contar hechos en orden, reportar mensajes y dar consejos.",
    ["Sé usar el pasado simple.", "Conozco said y told."],
    [
        "El pasado perfecto (had + participio) se usa cuando una acción pasada ocurrió antes de otra pasada. Siempre hay dos hechos: He didn't have money because he had lost his wallet. Primero perdió la billetera (had lost) y después no tuvo dinero. Sin un segundo hecho pasado, se usa el pasado simple.",
        "En el estilo indirecto (reported speech) contamos lo que otros dijeron y el tiempo retrocede: She said, I am tired se convierte en She said she was tired. He said, I have finished se convierte en He said he had finished. Se usa said sin persona (She said...) y told con persona (She told me...). Las órdenes se reportan con told + persona + to + verbo: She told me to go home. Las preguntas de sí o no se reportan con asked if: Is the director ready? se convierte en Pablo asked if the director was ready.",
        "Para situaciones hipotéticas usamos if + pasado simple, would + verbo: He would meet more people if he spoke English. If I were you, I would tell her the truth. Esa estructura imagina una situación presente o futura que no es real. Se usa were con todas las personas.",
    ],
    [("had + participio", "pasado perfecto: acción anterior"), ("said / told", "dijo / dijo a alguien"), ("reported speech", "estilo indirecto"), ("told someone to + verbo", "dijo a alguien que hiciera"), ("If + past, would + verb", "hipótesis"), ("If I were you...", "si yo fuera tú...")],
    [
        ("Pasado perfecto con dos hechos", R1 + " ¿Qué ocurrió primero: perdió la billetera o no tuvo dinero?", ["Busco had lost.", "Esa acción es anterior a No tuvo dinero.", "Perdió la billetera primero."], "Primero perdió la billetera"),
        ("Estilo indirecto", R4 + " ¿Qué dijo Anna realmente?", ["She said she was tired.", "El tiempo retrocede.", "Anna dijo: I am tired."], "Anna dijo: I am tired"),
    ],
    [
        ("Decir Anna said she is tired cuando habla del pasado.", "El tiempo debe retroceder.", "Di Anna said she was tired."),
        ("Usar had sin un segundo hecho pasado.", "El pasado perfecto necesita dos hechos.", "Usa pasado simple si solo hay uno."),
    ],
    [
        mc("Completa: He didn't have money because he ____ his wallet.", "had lost", ["has lost", "loses"], "Había perdido es anterior a no tener dinero."),
        mc("Completa: She told me ____ home.", "to go", ["go", "going"], "Told + persona + to + verbo."),
        mc("Completa: If I ____ you, I would tell her the truth.", "were", ["was", "am"], "En hipótesis se usa were."),
    ],
    [
        mr(R2, "¿Qué dijo la Sra. Brown?", "Que había terminado el informe antes de la reunión", ["Que terminará el informe", "Que no terminó el informe"], "Ms. Brown said she had finished the report."),
        mr(R2, "¿Qué nos ordenó el Sr. Silva?", "Esperar en el pasillo", ["Salir del pasillo", "Entrar a la reunión"], "Told us to wait in the hall."),
        mr(R3, "¿Qué haría el hombre con inglés?", "Conocería más gente", ["Viajaría menos", "Hablaría menos"], "He would meet more people if he spoke English."),
    ],
    [
        mc("Convierte a estilo indirecto: Luis: «I have finished my project». → Luis said he ____ his project.", "had finished", ["has finished", "finishes"], "El presente perfecto retrocede a had finished."),
        mc("Convierte: Mom: «Go home». → Mom told me ____ home.", "to go", ["go", "that I go"], "Una orden se reporta con to + verbo."),
        mc("Elige la hipótesis correcta:", "We would arrive earlier if we took the first bus", ["We will arrive earlier if we took the first bus", "We would arrive earlier if we take the first bus"], "If + pasado simple, would + verbo."),
    ],
    [
        mr(R1, "Un compañero dice que the landlord told him to leave significa que dijo que se fuera. ¿Es correcto?", "Sí: told him to leave reporta una orden", ["No: significa que lo vio irse del local", "No: significa que él se quedó en el local"], "Told + persona + to + verbo."),
        mr(R4, "¿Qué hace el verbo told de Luis told me he had finished his project?", "Reporta lo que Luis dijo y retrocede el tiempo", ["Cuenta un hecho futuro", "Pregunta algo"], "Told + persona reporta; had finished viene de have finished."),
    ],
    [
        mr(R3, "¿Qué tipo de situación expresa If I were you, I would tell her the truth?", "Un consejo hipotético", ["Una orden", "Un hecho pasado"], "Se imagina la situación del otro."),
        mr(R2, "Pablo preguntó si el director estaba listo. ¿Qué pregunta hizo antes?", "Is the director ready?", ["Was the director ready?", "Will the director be ready?"], "El presente retrocede a pasado en el reporte."),
    ],
    [mr(R1, "Une las ideas: «He lost his wallet» y «He couldn't pay the rent». ¿Qué oración respeta el orden temporal?", "He couldn't pay the rent because he had lost his wallet", ["He couldn't pay the rent because he lost his wallet", "He had lost his wallet because he couldn't pay the rent"], "La acción anterior va con had lost.")],
    [
        ("En Inglés de 2.º medio (OA 8, clase 5): ¿cuándo se usa had + participio?", "Para una acción pasada anterior a otra pasada", "Siempre necesita dos hechos."),
        ("En Inglés de 2.º medio (OA 8, clase 5): ¿qué pasa con el tiempo en el estilo indirecto?", "Retrocede", "Am pasa a was; have finished a had finished."),
        ("En Inglés de 2.º medio (OA 8, clase 5): ¿qué verbo se usa en If I ___ you?", "Were", "Se usa en hipótesis."),
    ],
    task("Con un adulto, practica tres mini-diálogos. 1) Cuenta por qué llegaste tarde con dos acciones (había... antes de...). 2) Reporta lo que un profesor te dijo. 3) Da un consejo con If I were you. Escribe tus tres respuestas y dilas en voz alta. Sigue este ejemplo.", "1) I was late because I had missed the bus. 2) The teacher said she was happy with my work. She told me to sit down. 3) If I were you, I would leave home earlier.", ["usa had + participio con dos hechos", "reporta con retroceso de tiempo", "da un consejo con If I were you"], ["tres respuestas en la hoja", "nota del adulto"], ["usar had sin segundo hecho", "no retroceder el tiempo"], "Pide que cambie el verbo de dicho (said) por told con persona."),
    "Escribe tres oraciones con had + participio y un segundo hecho pasado.",
    "Cuenta a alguien en español lo que otra persona te dijo ayer y marca cómo cambia el tiempo.",
)
