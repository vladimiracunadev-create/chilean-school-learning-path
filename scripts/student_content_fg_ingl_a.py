"""Cuaderno del estudiante, 3.º medio Inglés (Formación General), OA 01: información central y perspectivas culturales.

Los títulos de clase del plan son genéricos (propósito, pistas, lenguaje útil, postura crítica); aquí se aplican a:
1 propósito y audiencia, 2 idea central y pistas, 3 lenguaje para comparar culturas, 4 postura crítica y respeto.
Todos los textos son originales y breves, llevan glosario en español y están en inglés americano. Las costumbres
descritas son generales y de ejemplo, no afirmaciones sobre un país concreto.
"""
from __future__ import annotations

from fg_ingl_common import ADULT, MAT_L, MAT_R, arith, ex, lesson, mc, ml, mr, task

OA = "FG-INGL-3M-OAC-01"


def sc(n, rows):
    return [(f"En Inglés de 3.º medio (OA 1, clase {n}): {q}", a, w) for q, a, w in rows]


# ------------------------------------------------------------------ clase 1: propósito y audiencia
BLOG = "«Last month I started cycling to school. At first my legs hurt, but now I arrive awake and happy. If you live less than five kilometers away, why not try it? Your city, your health and your wallet will thank you.» (cycling = ir en bicicleta, legs hurt = me dolían las piernas, awake = despierto, wallet = billetera, thank = agradecer)"
NOTICE = "«Notice to students: the school library will close at 4 p.m. on Friday for cleaning. Please return all books before Thursday. Late books will be accepted on Monday.» (notice = aviso, library = biblioteca, close = cerrar, cleaning = limpieza, return = devolver, late = atrasados)"
REVIEW = "«The new documentary about ocean plastic is worth watching. It shows clear facts and real people, though a few scenes feel too long. I recommend it to anyone who wants to understand the problem, not only to experts.» (documentary = documental, worth watching = vale la pena verlo, scenes = escenas, recommend = recomiendo, experts = expertos)"
EXAM = "«Please keep your phone off during the exam. Anyone who breaks this rule will get a zero.» (keep off = mantén apagado, exam = prueba, breaks = infringe, rule = regla, get a zero = recibir un cero)"
RESID = "«Dear residents, from Monday the street cleaning will start at 7 a.m. Please move your cars the night before.» (residents = vecinos, street cleaning = limpieza de la calle, move = mover, the night before = la noche anterior)"
CONV = "«Everyone should learn a second language. It opens doors at work and it helps you understand other people. Start today.» (second language = segundo idioma, opens doors = abre puertas, helps = ayuda)"
BAND = "«Hi everyone! Our school band needs a drummer. Can you play? Come to the music room on Tuesday after class.» (band = banda, drummer = baterista, music room = sala de música)"

lesson(
    OA, 1, MAT_R,
    "Aprenderé a decidir, antes de leer los detalles, para qué se escribió un texto (propósito), a quién se dirige (audiencia) y qué sé ya del tema (conocimiento previo). Sirve para entender la información central de textos de otras culturas sin traducir palabra por palabra.",
    ["Sé reconocer si un texto informa, enseña, convence o cuenta.", "Conozco palabras como please, should, notice y recommend."],
    [
        "El propósito (purpose) es la razón por la que alguien escribe: informar (inform), persuadir (persuade), instruir (instruct), recomendar (recommend), quejarse (complain) o invitar (invite). La audiencia (audience) es el grupo al que se dirige el texto: estudiantes, vecinos, expertos o el público general. Ambos cambian el tipo de texto: un aviso (notice) es breve e impersonal; un blog es personal; una reseña (review) evalúa; un anuncio de invitación llama a participar.",
        "Para descubrir el propósito mira tres pistas. Primera, el título y el formato. Segunda, las formas verbales: las órdenes (Please return...), el should y las preguntas al lector (why not try it?) suelen indicar intención de persuadir o instruir; el pasado personal (Last month I started...) indica relato. Tercera, el vocabulario de evaluación (worth watching, I recommend) indica una reseña. La audiencia se descubre con you o we, con el nivel de formalidad y con el saludo (Dear residents, Hi everyone).",
        "El conocimiento previo (prior knowledge) es lo que ya sabes del tema. Si sabes que el plástico llega al mar, entenderás más rápido un documental sobre eso. Pero cuidado con los falsos amigos: library significa biblioteca, no librería (que se dice bookstore). Un texto con datos puede no ser solo informativo: si además evalúa o pide algo, su propósito principal es recomendar o persuadir.",
    ],
    [("purpose", "propósito: para qué se escribe"), ("audience", "audiencia: a quién se dirige"), ("prior knowledge", "conocimiento previo"), ("inform / persuade", "informar / persuadir"), ("notice", "aviso"), ("review", "reseña")],
    [
        ("Propósito y audiencia de un aviso", NOTICE + " ¿Cuál es el propósito y quién es la audiencia?", ["El texto empieza con Notice to students: se dirige a estudiantes.", "Informa un cierre (will close) y da una orden (Please return).", "El propósito es informar y pedir una acción a quienes tienen libros prestados."], "Informar el cierre y pedir devolver libros; audiencia: estudiantes del colegio"),
        ("Detectar la intención de persuadir", CONV + " ¿Qué palabra y qué orden muestran que el autor quiere persuadir?", ["Busco una palabra de recomendación fuerte: should.", "Busco una orden final: Start today.", "Las dos señalan que el autor quiere que el lector actúe."], "Should y Start today: el autor busca convencer al lector"),
    ],
    [
        ("Decir que un texto con datos es solo informativo.", "Se mira solo que trae datos y no si evalúa o pide algo.", "Pregunta qué quiere el autor que haga o piense el lector."),
        ("Confundir library con librería.", "Es un falso amigo: parece igual en español pero library es biblioteca.", "Comprueba el significado en el glosario o por contexto (books, return)."),
    ],
    [
        mr(BLOG, "¿Cuál es el propósito principal?", "persuadir a los lectores de ir en bicicleta al colegio", ["informar sobre un accidente de tránsito", "explicar cómo funciona una bicicleta"], "El autor cuenta su experiencia y termina con una invitación: why not try it?"),
        mr(NOTICE, "¿A quién se dirige este aviso?", "a estudiantes que tienen libros prestados de la biblioteca", ["a profesores que preparan sus clases en la biblioteca", "a visitantes que quieren comprar libros nuevos"], "Empieza con Notice to students y pide devolver books."),
        mr(REVIEW, "¿Cuál es el propósito principal?", "evaluar un documental y recomendarlo", ["anunciar el precio de las entradas", "enseñar la historia del plástico"], "Usa worth watching e I recommend, palabras de evaluación."),
    ],
    [
        mr(BLOG, "¿Qué frase le habla directamente al lector?", "why not try it?", ["At first my legs hurt", "I started cycling"], "La pregunta y el you invitan al lector, mientras las otras frases cuentan la experiencia propia."),
        mr(NOTICE, "¿Cuál es la información central?", "la biblioteca cierra el viernes y hay que devolver los libros antes del jueves", ["los libros atrasados se aceptan el lunes después de la limpieza", "los estudiantes limpiarán la biblioteca el viernes a las 4"], "Lo esencial es el cierre y la orden de devolver; el lunes es un detalle."),
        mc("Sabes que las botellas plásticas pueden llegar al mar. Vas a leer: " + REVIEW + " ¿Cómo te ayuda ese conocimiento previo?", "puedes anticipar el tema y seguir mejor los datos", ["puedes saltarte la lectura del texto", "puedes asegurar que la reseña es verdadera"], "El conocimiento previo ayuda a predecir y comprender, pero no reemplaza leer ni prueba que el texto sea cierto."),
    ],
    [
        mr(EXAM, "¿Cuál es el propósito?", "instruir y advertir sobre una regla", ["divertir con una historia", "vender un teléfono"], "Usa Please y una consecuencia (will get a zero)."),
        mr(RESID, "¿Quién es la audiencia?", "vecinos que estacionan en la calle", ["turistas de paso por la ciudad", "conductores de buses"], "Dice Dear residents y pide mover los autos."),
        mr(CONV, "¿Qué palabra muestra una opinión y no un hecho?", "should", ["language", "doors"], "Should expresa lo que el autor cree que se debe hacer."),
    ],
    [
        mc("Un compañero dice que la reseña es solo informativa porque trae datos. Texto: " + REVIEW + " ¿Qué le respondes?", "que también evalúa y recomienda, por eso su propósito es recomendar", ["que tiene razón, porque todo texto con datos informa", "que tiene razón, porque es un documental"], "Worth watching e I recommend muestran que el autor valora y aconseja."),
        mc("Compara. Texto 1: " + NOTICE + " Texto 2: " + BLOG + " ¿Cuál es más impersonal y por qué?", "el aviso, porque no cuenta una experiencia personal y da órdenes breves", ["el blog, porque usa I y cuenta una experiencia personal", "los dos, porque ambos usan frases en inglés para informar"], "El aviso no habla de una persona; el blog cuenta una vivencia con I."),
    ],
    [
        mc("Una alumna lee el aviso del texto siguiente y entiende que cerrarán una librería para comprar. Texto: " + NOTICE + " (librería = bookstore). ¿Qué error cometió?", "confundió library con librería, un falso amigo", ["no reconoció el propósito de informar", "pensó que la audiencia eran profesores"], "Library es biblioteca; librería se dice bookstore."),
        mr(BAND, "¿Qué afirmación NO está apoyada por el texto?", "va dirigido a los apoderados de los estudiantes", ["su propósito es invitar a unirse a la banda", "indica un lugar y un día para ir"], "El saludo Hi everyone y la sala de música apuntan a estudiantes, no a apoderados."),
    ],
    [mc("Encuentras en un bus este cartel: «Please give your seat to people who need it.» (give your seat = ceder el asiento). ¿Cuál es el propósito?", "pedir una conducta a los pasajeros", ["contar una anécdota de un viaje en bus", "vender un pasaje a los pasajeros"], "Please y la orden indican que el cartel busca instruir.")],
    sc(1, [
        ("¿Qué es la audiencia de un texto?", "El grupo de personas al que se dirige el texto", "Responde a quién se escribe el texto."),
        ("¿Qué pista de intención de persuadir aparece en un texto con should?", "Que el autor cree que el lector debe actuar", "Should expresa recomendación u obligación."),
        ("¿Cómo se dice biblioteca en inglés?", "Library", "Library es biblioteca; bookstore es librería."),
    ]),
    task("Lee este texto: «Dear neighbors, the community garden needs help this Saturday. We will plant tomatoes and herbs. Bring gloves if you can. All ages are welcome.» (neighbors = vecinos, plant = plantar, herbs = hierbas, gloves = guantes, welcome = bienvenidos). Escribe en español el propósito, la audiencia y dos pistas del texto que lo muestran.", "Propósito: invitar a ayudar con el huerto. Audiencia: vecinos del barrio de todas las edades. Pistas: Dear neighbors y la frase Bring gloves if you can, junto con All ages are welcome.", ["nombra un propósito coherente", "nombra la audiencia", "cita dos pistas del texto"], ["hoja con tres respuestas", "pistas copiadas del texto"], ["decir solo que el texto habla de plantas", "no citar pistas"], "Reconoce lo acertado y vuelve a mirar el saludo y las órdenes para decidir a quién habla y qué pide."),
    "Busca otro aviso breve en inglés de tu casa (un envase o instructivo) y escribe su propósito y audiencia en español.",
    "Escribe dos oraciones en español sobre un tema que conozcas bien y que podría aparecer en un texto de otra cultura.",
)

# ------------------------------------------------------------------ clase 2: idea central y pistas
PARK = "«Urban gardens are becoming popular. A community garden, that is, a piece of land shared by neighbors, gives people fresh vegetables. It also brings neighbors together, since they work side by side. However, some gardens need more volunteers because many people are too busy.» (urban = urbano, shared = compartido, neighbors = vecinos, side by side = lado a lado, volunteers = voluntarios, busy = ocupados)"
TEA = "«In my family, guests always get a hot drink first, such as tea or coffee, and only later a meal. Refusing the drink at once can seem impolite, so I usually accept a small cup. After that, we talk for an hour.» (guests = invitados, hot drink = bebida caliente, refusing = rechazar, at once = de inmediato, accept = aceptar)"
SLEEP = "«Many teenagers sleep less than they need. Experts say that this affects memory, mood and school grades. A simple habit, like turning off screens thirty minutes before bed, can help. Still, changing habits takes time.» (teenagers = adolescentes, experts = expertos, affects = afecta, memory = memoria, mood = ánimo, grades = notas, turning off = apagar, screens = pantallas)"
SHOES = "«At my friend's home, guests take their shoes off at the door and are offered slippers. A guest who keeps shoes on might make the family uncomfortable. Hosts never ask for explanations; it is simply the custom.» (shoes = zapatos, offered = ofrecen, slippers = pantuflas, uncomfortable = incómoda, hosts = anfitriones, custom = costumbre)"

lesson(
    OA, 2, MAT_R,
    "Aprenderé a encontrar la idea central de un texto, a distinguirla de los detalles y a usar pistas del contexto (that is, such as, however, still) para deducir significados. Sirve para entender textos sobre costumbres y temas de interés sin conocer todas las palabras.",
    ["Sé reconocer el propósito y la audiencia de un texto.", "Conozco conectores básicos como but y because."],
    [
        "La idea central (central information, main idea) es lo que el texto quiere comunicar en su totalidad. Los detalles de apoyo (supporting details) son ejemplos, datos o razones que la sostienen. Una buena idea central cubre todo el texto: no es solo la primera frase ni solo la última, ni un dato aislado. Para encontrarla, pregunta: ¿de qué trata todo el párrafo y qué dice sobre eso?",
        "Los conectores son pistas. That is e i.e. introducen una definición: a community garden, that is, a piece of land shared. Such as y for example introducen ejemplos. However, but y still marcan un contraste: lo que sigue limita o corrige la idea anterior. Because, since y so marcan causa o resultado. Cuando aparece una palabra desconocida (habit), busca una definición, un ejemplo o un contraste cerca: en 'a simple habit, like turning off screens' el ejemplo muestra que un habit es una acción que se repite.",
        "Leer con estas pistas te permite entender textos de otras culturas aunque no conozcas cada palabra. Si dos textos tratan costumbres de distintos hogares, la idea central suele ser qué se hace, por qué importa y cómo lo ven los participantes. Evita agregar tu opinión al resumir: el resumen debe decir lo que el texto dice.",
    ],
    [("central information / main idea", "idea central"), ("supporting detail", "detalle de apoyo"), ("that is", "es decir: introduce una definición"), ("such as", "como, por ejemplo: introduce ejemplos"), ("however / still", "sin embargo / aun así: contraste"), ("context clue", "pista del contexto")],
    [
        ("Idea central y detalle", PARK + " ¿Cuál es la idea central?", ["Busco una idea que cubra todo el texto.", "Los huertos dan verduras y unen a los vecinos, pero necesitan voluntarios.", "Los vecinos que trabajan lado a lado son un detalle."], "Los huertos comunitarios dan alimento y unen a los vecinos, pero necesitan voluntarios"),
        ("Deducir una palabra", SLEEP + " ¿Qué significa habit?", ["Veo el ejemplo: turning off screens thirty minutes before bed.", "Después dice changing habits takes time: algo que se repite y cambia con tiempo.", "Habit es una acción que se repite con regularidad."], "Hábito, una acción que se repite con regularidad"),
    ],
    [
        ("Elegir como idea central la última oración.", "Se cree que el final siempre resume, pero a veces es una limitación o un detalle.", "Comprueba que la idea cubra todo el texto."),
        ("Tomar however como una idea que continúa lo anterior.", "However marca contraste: lo que sigue corrige o limita lo anterior.", "Pregunta qué idea se opone a la anterior."),
    ],
    [
        mr(PARK, "¿Qué introduce la expresión that is?", "una definición de community garden", ["un contraste con la idea anterior", "un ejemplo de verduras"], "That is explica el término con otras palabras: a piece of land shared by neighbors."),
        mr(TEA, "¿Cuál es la idea central?", "a los invitados se les ofrece primero una bebida caliente y rechazarla puede parecer descortés", ["en esa familia se almuerza durante una hora completa y después se bebe té o café", "el café es una bebida mejor que el té, y por eso siempre se ofrece primero a los invitados"], "El texto trata de la costumbre de ofrecer bebida y de por qué conviene aceptarla."),
        mr(SLEEP, "¿Qué idea central expresa mejor el texto?", "muchos adolescentes duermen poco, eso los afecta y un hábito simple puede ayudar", ["los expertos prohíben dormir tarde a los adolescentes en todos los países", "las pantallas son peligrosas para los adultos y para los niños pequeños"], "Une el problema, sus efectos y una solución."),
    ],
    [
        mr(TEA, "¿Qué introduce such as?", "ejemplos de bebidas calientes", ["una razón para rechazar", "un contraste con el té"], "Tea or coffee son ejemplos de hot drink."),
        mr(PARK, "¿Qué idea sigue después de However?", "una dificultad: algunos huertos necesitan más voluntarios", ["otra ventaja del huerto: los vecinos trabajan lado a lado", "una definición de la palabra verduras en otras palabras"], "However marca contraste con lo positivo anterior."),
        mr(SLEEP, "¿Qué relación marca Still en la última oración?", "contraste: aunque hay una solución simple, cambiar hábitos toma tiempo", ["causa: por eso los hábitos mejoran al apagar las pantallas", "ejemplo: otro hábito útil para dormir mejor cada noche"], "Still introduce una limitación a la idea positiva anterior."),
    ],
    [
        mr(TEA, "Según las pistas del texto, ¿qué significa impolite? (descortés, divertido o peligroso)", "descortés", ["divertido", "peligroso"], "Si rechazar la bebida puede parecer impolite y por eso la persona la acepta, la palabra tiene sentido negativo social."),
        mr(PARK, "¿Qué título resume mejor el texto?", "Shared gardens grow food and community", ["How to cook vegetables from your own garden", "A guide to buying land for a new garden"], "El título debe cubrir alimento, unión de vecinos y la necesidad de voluntarios."),
        mr(SHOES, "¿Cuál es el mejor resumen?", "los invitados se sacan los zapatos y la familia no pide explicaciones porque es la costumbre", ["los dueños de casa se molestan siempre con los invitados que llegan", "las pantuflas son un regalo caro que la familia da a los invitados"], "El resumen debe decir lo que el texto dice, sin agregar opiniones."),
    ],
    [
        mc("Una compañera dice que la idea central del texto es 'some gardens need more volunteers', porque es la última oración. Texto: " + PARK + " ¿Qué le respondes?", "que es un detalle final, porque la idea central cubre todo el texto", ["que tiene razón, porque lo último siempre es lo central", "que no hay idea central en este texto"], "La idea central abarca los beneficios y la limitación; la última oración solo agrega una dificultad."),
        mr(SLEEP, "¿Qué detalle NO muestra el problema de dormir poco?", "apagar las pantallas treinta minutos antes de dormir", ["afecta las notas escolares de los adolescentes", "afecta la memoria de quienes duermen poco"], "Apagar pantallas es una solución, no un efecto del poco sueño."),
    ],
    [
        mc("Compara. Texto 1: " + TEA + " Texto 2: " + SHOES + " ¿Qué tienen en común?", "en ambos, la conducta del invitado importa para el respeto de la familia anfitriona", ["en ambos se habla de comida que se ofrece a los invitados cuando llegan", "en ambos se prohíbe a los invitados entrar a la casa sin permiso previo"], "Rechazar la bebida o dejarse los zapatos puede parecer una falta de respeto."),
        mc("Texto: " + SHOES + " ¿Qué resumen es mejor?", "los invitados siguen una costumbre del hogar, como sacarse los zapatos", ["las familias son estrictas con los invitados y los retan por sus errores", "solo se habla de las pantuflas que ofrecen a los invitados en la puerta"], "El resumen correcto es completo y fiel; la opción sobre las pantuflas es demasiado estrecha y la de las familias estrictas agrega una opinión que el texto no dice."),
    ],
    [mc("Recibes este mensaje de una familia anfitriona: «When you arrive, please call us from the station, that is, the bus station near the park.» (arrive = llegar, call = llamar). ¿Qué debes hacer al llegar?", "llamar desde la estación de buses cercana al parque", ["llamar desde el parque que queda cerca de la estación", "esperar en casa a que la familia anfitriona llame primero"], "That is aclara que station es la estación de buses cerca del parque.")],
    sc(2, [
        ("¿Para qué sirve la expresión such as?", "Para introducir ejemplos", "Such as precede una lista de casos del tema."),
        ("¿Qué indica however en un texto?", "Un contraste con la idea anterior", "However limita o corrige lo dicho antes."),
        ("¿Cómo se distingue la idea central de un detalle?", "La idea central cubre todo el texto y el detalle solo una parte", "La idea central abarca el texto completo."),
    ]),
    task("Lee: «In my town, neighbors usually greet each other every morning, even if they do not know each other well. For example, they say good morning at the bus stop. However, people in big buildings often do not greet anyone.» (neighbors = vecinos, greet = saludar, bus stop = paradero). Escribe en español la idea central, un detalle de apoyo y qué señala however.", "Idea central: en el pueblo los vecinos suelen saludarse cada mañana. Detalle: saludan en el paradero. However señala un contraste: en edificios grandes muchos no saludan.", ["idea central que abarca el texto", "un detalle que la apoya", "explica la función de however"], ["hoja con tres respuestas"], ["copiar solo la primera oración", "no explicar el contraste"], "Reconoce lo bien hecho y relee la frase con however para ver qué contradice."),
    "Vuelve al texto del huerto comunitario del primer ejemplo resuelto: subraya los conectores (that is, however, since, also) y escribe qué marca cada uno.",
    "Escribe una oración en español con la palabra however que contraste dos costumbres.",
)

# ------------------------------------------------------------------ clase 3: lenguaje para comparar culturas
SCHA = "«At my school, classes start at eight and end at three. We eat lunch in the cafeteria, and we wear a uniform.» (classes = clases, cafeteria = casino, uniform = uniforme)"
SCHB = "«At my cousin's school, classes start at nine and end at four. Students bring their own lunch, and nobody wears a uniform.» (cousin = primo, bring = traen, own = propio, nobody = nadie)"

lesson(
    OA, 3, MAT_R,
    "Aprenderé el lenguaje para comparar costumbres: both, neither, unlike, whereas, similarly y however, y a evitar los estereotipos con expresiones como many o tend to. Sirve para entender textos sobre cómo otras culturas abordan un tema y para hablar de ello con respeto.",
    ["Sé reconocer ideas centrales y conectores de contraste.", "Conozco palabras como but y because."],
    [
        "Para comparar se usan palabras de semejanza y de diferencia. Para semejanzas: both ... and (ambos), similarly (de manera similar), also, like. Para diferencias: whereas y while (mientras que), unlike (a diferencia de), however y on the other hand (por otro lado), but. Neither ... nor significa ni ... ni. Both lleva plural: both schools start early. Neither lleva verbo singular en lenguaje cuidado: neither school has a uniform.",
        "Al comparar, usa datos del texto: horas, cantidades, acciones. Evita afirmar más de lo que dice: si las clases terminan una hora más tarde, no digas que 'el día es más largo' sin calcular la duración. Calcula siempre: de 8 a 15 horas son 7 horas, y de 9 a 16 horas también son 7. Lo que cambia es el horario, no la duración.",
        "Al hablar de otras culturas evita los estereotipos, es decir, ideas simples y fijas sobre un grupo. Usa expresiones que dejan espacio a las excepciones: many people, tend to, in some homes, often. Compara costumbres, no personas, y no digas que una es mejor sin razones. Una buena comparación nombra las dos costumbres, indica semejanzas y diferencias y no juzga.",
    ],
    [("both ... and", "ambos"), ("neither ... nor", "ni ... ni"), ("whereas / while", "mientras que"), ("unlike", "a diferencia de"), ("similarly", "de manera similar"), ("tend to", "tender a: suele")],
    [
        ("Comparar con un conector", SCHA + " " + SCHB + " Completa: 'Students at my school wear a uniform, ___ nobody does at my cousin's school.'", ["Busco una relación de contraste entre las dos escuelas.", "Whereas significa mientras que y marca diferencia.", "So marcaría resultado y also sumaría ideas."], "whereas"),
        ("Duración del día", SCHA + " " + SCHB + " ¿Cuántas horas dura la jornada en cada escuela, del inicio al fin de las clases?", ["Escuela A: de 8 a 15 horas hay 7.", "Escuela B: de 9 a 16 horas hay 7.", "Las dos duran lo mismo; cambia el horario."], "Siete horas en cada una"),
    ],
    [
        ("Decir que una escuela tiene un día más largo porque termina más tarde.", "Se compara el horario de término y no la duración total.", "Calcula la hora de término menos la de inicio."),
        ("Escribir Both school start.", "Both exige plural: both schools start.", "Después de both usa schools y start."),
    ],
    [
        mc(SCHA + " " + SCHB + " ¿Qué afirmación es verdadera?", "en ambas escuelas las clases empiezan en la mañana", ["en ambas escuelas se usa uniforme", "en ambas escuelas se almuerza en el casino"], "Empiezan a las 8 y a las 9; la escuela B no usa uniforme ni casino."),
        mc("Qué indica la palabra unlike en 'Unlike my school, my cousin's school has no uniform'.", "una diferencia entre las escuelas", ["una semejanza entre las escuelas", "una razón de por qué no hay uniforme"], "Unlike significa a diferencia de."),
        mc("Completa: 'Students at my school eat in the cafeteria. ___, students at my cousin's school bring lunch.'", "However", ["Similarly", "Therefore"], "Las dos costumbres son diferentes, así que se necesita un conector de contraste."),
    ],
    [
        mc(SCHA + " " + SCHB + " ¿Cómo se compara el término de las clases?", "las clases terminan una hora más tarde en la escuela de mi primo", ["las clases terminan dos horas más tarde en la escuela de mi primo", "las clases terminan a la misma hora"], "Terminan a las 15 y a las 16: una hora de diferencia."),
        mc(SCHA + " " + SCHB + " ¿Qué duración tiene cada jornada, de inicio a fin?", "las dos duran 7 horas", ["la escuela A dura 8 horas", "la escuela B dura 6 horas"], "De 8 a 15 y de 9 a 16 son 7 horas."),
        mc(SCHA + " " + SCHB + " ¿Qué oración con both es correcta?", "Both schools start before ten o'clock", ["Both school starts before ten o'clock", "Both of school start before ten o'clock"], "Both va con plural, schools start."),
    ],
    [
        mc(SCHA + " " + SCHB + " ¿Qué oración con neither es verdadera?", "Neither school starts classes after nine o'clock", ["Neither school has a uniform", "Neither school begins classes before nine o'clock"], "A empieza a las 8 y B a las 9; la escuela A sí usa uniforme y empieza antes de las 9."),
        mc("¿Cuál es una generalización cuidadosa sobre un grupo?", "Many students in my town tend to bring lunch from home", ["All students in the world hate cafeteria food", "Nobody in my town ever eats lunch at school"], "Many y tend to dejan espacio a las excepciones; all y nobody ever no."),
        mc(SCHA + " " + SCHB + " ¿Qué comparación NO está apoyada por los textos?", "la escuela B tiene una jornada más larga que la escuela A", ["la escuela B empieza más tarde que la escuela A", "la escuela A usa uniforme y la escuela B no"], "Las dos duran 7 horas."),
    ],
    [
        mc("Una alumna escribe: 'Schools in country B are better than in country A because they start later.' ¿Qué problema tiene la oración?", "da un juicio (better) sin evidencia: los textos solo muestran una diferencia", ["usa mal la palabra because en una comparación entre dos escuelas", "habla de dos escuelas en vez de hablar de una sola, como pide el texto"], "Comparar no es lo mismo que juzgar; falta una razón que lo respalde."),
        mc(SCHA + " " + SCHB + " ¿Qué párrafo compara mejor?", "Both schools run seven hours. However, school A starts earlier, whereas school B starts later, and only school A has a uniform.", ["Both schools are similar. School A is stricter than school B because it has a uniform, and that is why it is better", "School A and school B are two schools with students and lunch, and they have classes in the morning"], "El primero usa datos, semejanza y diferencia; los otros juzgan sin datos o no comparan."),
    ],
    [
        mc("Une las ideas con el conector adecuado: 'School A has a cafeteria. School B has none.'", "School A has a cafeteria, whereas school B has none", ["School A has a cafeteria, so school B has none", "School A has a cafeteria, because school B has none"], "Es una diferencia, no un resultado ni una causa."),
        mc("Sobre otra cultura alguien escribe 'Everybody in that country is always late.' ¿Cómo se corrige para evitar el estereotipo?", "In some places, many people tend to arrive later for social events", ["In that country, nobody is ever on time for any event", "In that country, people are rude when they arrive late"], "La frase corregida cuantifica y habla de un contexto, sin juzgar."),
    ],
    [mc("Lees: «My host family has dinner at nine; my family at home has it at seven.» (host family = familia anfitriona, dinner = cena). ¿Qué conector sirve para unir la comparación?", "whereas", ["because", "also"], "Las dos horas son una diferencia entre dos familias.")],
    sc(3, [
        ("¿Qué significa whereas?", "Mientras que, para contrastar", "Whereas une dos ideas distintas."),
        ("¿Cómo se dice ni ... ni en inglés?", "Neither ... nor", "Neither ... nor niega dos cosas a la vez."),
        ("¿Para qué sirve decir many o tend to al hablar de un grupo?", "Para evitar estereotipos y permitir excepciones", "Estas expresiones no afirman que todos sean iguales."),
    ]),
    task("Lee estos datos de ejemplo. Casa 1: «We have tea at five and we eat together at the table.» Casa 2: «We have tea at six, but everybody eats in the living room.» (tea = once, together = juntos, table = mesa, living room = living). Escribe tres oraciones en inglés que comparen las dos casas: una con both o similarly, una con whereas y una con however.", "Both families have tea in the afternoon. In house 1 the tea is at five, whereas in house 2 it is at six. In house 1 they eat at the table; however, in house 2 they eat in the living room.", ["usa los tres conectores", "los datos coinciden con el texto", "no juzga ninguna costumbre"], ["tres oraciones escritas"], ["decir que una casa es mejor", "usar both con singular"], "Valida las oraciones correctas y revisa el uso de cada conector con el glosario."),
    "Compara dos costumbres de tu casa con las de un compañero usando both y whereas, en español, y luego traduce una oración a inglés.",
    "Escribe una generalización cuidadosa sobre un grupo, usando many y tend to.",
)

# ------------------------------------------------------------------ clase 4: postura crítica y respeto
OP1 = "«Some people say school uniforms are old-fashioned. I disagree. In my opinion, a uniform reduces pressure about clothes, and a survey of 100 students at our school showed that 62 agree. Still, I understand that others want to express themselves through clothing.» (uniforms = uniformes, old-fashioned = anticuado, disagree = no estar de acuerdo, pressure = presión, survey = encuesta, agree = están de acuerdo, express themselves = expresarse; los datos son de ejemplo)"
OP2 = "«Everyone knows that homework is useless. Teachers only give it because they have always done it, and no student ever learns anything from it.» (homework = tarea, useless = inútil, only = solo, ever = alguna vez)"
OP3 = "«In my family, we celebrate birthdays with a big lunch at home. A friend told me that in her family, friends go out to a cafe. I used to think my way was the only normal one, but now I see that both ways show love in different forms.» (celebrate = celebrar, lunch = almuerzo, cafe = café, used to think = antes pensaba, show = muestran)"

lesson(
    OA, 4, MAT_R,
    "Aprenderé a identificar la postura (stance) del autor, la evidencia que usa y cómo reconoce otros puntos de vista, y a distinguir hechos de opiniones. Sirve para comprender de forma crítica textos sobre cómo distintas culturas ven un tema y para expresar una postura propia con respeto.",
    ["Sé encontrar la idea central y los conectores de contraste.", "Sé comparar costumbres sin juzgar."],
    [
        "La postura (stance) es la posición del autor frente a un tema: a favor, en contra o neutral. Se marca con expresiones como In my opinion, I believe, I disagree, I am in favor of o I am against. Un hecho (fact) se puede comprobar: A week has seven days. Una opinión (opinion) expresa lo que alguien cree: Mondays are the worst. La evidencia (evidence) son datos, ejemplos o razones que apoyan la postura, como una encuesta (survey).",
        "Un texto crítico bien hecho tiene tres elementos: una postura clara, evidencia suficiente y reconocimiento de otras posturas (concession). Para reconocer otra postura se usa Still, I understand that... o I can see why... Desconfía de las palabras absolutas sin evidencia (everyone, nobody, always, never, useless). Una encuesta de 100 estudiantes de un solo colegio muestra opiniones de ese grupo, no de todos.",
        "Respetar otras posturas no significa cambiar la tuya. Significa criticar ideas y no personas: I disagree with this idea, but I can see why some people like it. En textos de otras culturas, la postura crítica se enriquece al notar que una costumbre propia no es la única 'normal', y que distintas costumbres pueden cumplir la misma función, como demostrar cariño.",
    ],
    [("stance", "postura"), ("evidence", "evidencia"), ("fact / opinion", "hecho / opinión"), ("survey", "encuesta"), ("I disagree", "no estoy de acuerdo"), ("I can see why", "entiendo por qué")],
    [
        ("Postura y evidencia", OP1 + " ¿Cuál es la postura y cuál la evidencia?", ["I disagree con 'uniforms are old-fashioned' muestra que está a favor del uniforme.", "La evidencia es la encuesta de 100 estudiantes, con 62 que están de acuerdo.", "Still, I understand... reconoce otra postura."], "A favor del uniforme; evidencia: encuesta con 62 de 100"),
        ("Detectar una afirmación sin apoyo", OP2 + " ¿Qué le falta?", ["Busco datos o ejemplos: no hay ninguno.", "Everyone, only y no student ever son palabras absolutas.", "La opinión no tiene evidencia y no reconoce otra postura."], "Evidencia y reconocimiento de otras posturas"),
    ],
    [
        ("Pensar que una encuesta de un curso prueba que todos opinan igual.", "Una muestra pequeña de un colegio no representa a todos.", "Indica a quién se encuestó y a quién no."),
        ("Criticar a la persona en vez de la idea.", "Decir que alguien es tonto no argumenta y falta el respeto.", "Critica la idea con una razón: I disagree because..."),
    ],
    [
        mr(OP1, "¿Cuál es la postura del autor sobre los uniformes?", "a favor", ["en contra", "neutral"], "I disagree con la crítica a los uniformes y la defensa que hace muestran apoyo."),
        mr(OP1, "¿Qué frase introduce una opinión?", "In my opinion", ["A survey of 100 students", "Some people say"], "In my opinion presenta lo que el autor cree."),
        mr(OP2, "¿Qué le falta a este texto?", "evidencia como una encuesta o un ejemplo", ["un tema claro sobre el cual opinar", "una opinión clara sobre la tarea escolar"], "Tiene tema y opinión, pero no apoya con datos."),
    ],
    [
        mr(OP1, "¿Cuál es la evidencia del autor?", "una encuesta a 100 estudiantes con 62 que están de acuerdo", ["una entrevista a un profesor y a algunos apoderados", "una carta firmada por los padres del colegio"], "El texto cita la encuesta."),
        mr(OP1, "¿Qué función cumple Still, I understand that others want to express themselves?", "reconoce otro punto de vista", ["entrega una cifra", "cambia el tema"], "Concede que otros piensan distinto sin cambiar su postura."),
        mr(OP1, "¿Qué oración es una opinión del autor?", "a uniform reduces pressure about clothes", ["a survey was done at the school", "62 students agree"], "Reducir la presión es lo que el autor cree; la encuesta y la cifra se informan como datos."),
    ],
    [
        arith("Una encuesta a 100 estudiantes mostró que 62 están de acuerdo con usar uniforme. ¿Cuántos no estaban de acuerdo?", "100-62", "Se resta a los que respondieron los que sí están de acuerdo.", " estudiantes"),
        mc("¿Cuál de estas oraciones es un hecho que se puede comprobar?", "A week has seven days", ["Mondays are the worst day", "Winter is the most beautiful season"], "Los otros dos expresan gustos personales."),
        mc("¿Cuál es una forma respetuosa de expresar desacuerdo?", "I disagree with this idea, but I can see why some people like it", ["You are not smart if you like that idea", "I disagree, and I will not listen to other opinions"], "Critica la idea con cortesía y reconoce otra mirada."),
    ],
    [
        mc("Una compañera dice que la encuesta de este texto prueba que los uniformes son buenos para todos. Texto: " + OP1 + " ¿Qué le respondes?", "que solo muestra la opinión de 100 estudiantes de un colegio", ["que sí, porque 62 es una cifra grande y clara", "que no importa, porque toda encuesta es solo una opinión"], "La muestra es de un solo colegio y no habla de todos los estudiantes."),
        mc("Compara. Texto 1: " + OP1 + " Texto 2: " + OP2 + " ¿Cuál convence más y por qué?", "el primero, porque da razón, evidencia y reconoce otra postura", ["el segundo, porque usa palabras fuertes y seguras", "el primero, porque es más largo que el segundo"], "La fuerza de un argumento está en la evidencia y el respeto, no en el tono ni en el largo."),
    ],
    [
        mr(OP3, "¿Cómo cambió el punto de vista de la autora?", "de creer que su forma era la única normal a aceptar que ambas muestran cariño", ["de preferir celebrar en un café a preferir hacerlo en casa", "de no gustarle los cumpleaños a disfrutar mucho de ellos"], "Dice I used to think my way was the only normal one, but now I see that both ways show love."),
        mr(OP3, "¿Qué oración añadiría una postura crítica y respetuosa al texto?", "I think it is worth asking why each custom matters to the family before judging it", ["I think my way is the correct way and the others are wrong", "I think nobody should go out to a cafe to celebrate birthdays"], "Pide comprender antes de juzgar, sin atacar ninguna costumbre."),
    ],
    [mc("Lees: «Some people think that eating late is unhealthy. I believe it depends on what and how much you eat. In many homes, a late dinner is a social moment.» (late = tarde, unhealthy = poco saludable, depends on = depende de). ¿Cuál es la postura del autor?", "que la respuesta no es tan simple: depende de lo que se coma y cómo se viva", ["que comer tarde siempre es malo para la salud de las personas", "que comer tarde siempre es bueno para la vida social del hogar"], "I believe it depends muestra una postura matizada, no absoluta.")],
    sc(4, [
        ("¿Qué es un hecho (fact)?", "Una afirmación que se puede comprobar", "A diferencia de la opinión, se verifica con datos."),
        ("¿Para qué sirve decir Still, I understand that...?", "Para reconocer otra postura sin cambiar la propia", "Es una concesión respetuosa."),
        ("¿Por qué hay que desconfiar de palabras como everyone o never?", "Porque afirman todo o nada sin evidencia", "Las palabras absolutas rara vez son ciertas."),
    ]),
    task("Lee este tema y elige una postura: «Should students learn about the customs of other countries at school?» (customs = costumbres). Escribe en inglés tres oraciones: tu postura con In my opinion, una razón con because y una oración que reconozca otra postura con Still, I understand that...", "In my opinion, students should learn about other countries' customs. I think so because it helps us understand people better. Still, I understand that some classes have little time for it.", ["postura clara", "una razón", "una concesión respetuosa"], ["tres oraciones en inglés"], ["usar solo palabras absolutas", "no incluir la concesión"], "Marca la postura, la razón y la concesión; si falta una, agrégala con la frase indicada."),
    "Vuelve al texto sobre uniformes del primer ejemplo resuelto: subraya la postura, la evidencia y la concesión con tres colores distintos.",
    "Escribe en español una opinión tuya sobre una costumbre y una frase que reconozca otro punto de vista.",
)

# ================================================================= OA 02: producción de textos breves y claros con postura crítica y respeto
OA2 = "FG-INGL-3M-OAC-02"

# ------------------------------------------------------------------ clase 1: planificar propósito, audiencia y postura
PROMPT = "«Prompt: Should phones be allowed in class? Audience: the school principal. Purpose: persuade.» (prompt = consigna, allowed = permitido, principal = director)"

lesson(
    OA2, 1, MAT_R,
    "Aprenderé a planificar un texto breve: elegir mi postura, el propósito, la audiencia y dos razones antes de escribir. Sirve para producir textos claros que expresen una postura crítica con respeto, sin traducir cada palabra del español.",
    ["Sé reconocer postura, evidencia y opinión en un texto.", "Conozco should, because y I believe."],
    [
        "Un texto claro empieza antes de escribir, con un plan. Primero, el propósito (purpose): persuadir (persuade), informar (inform), quejarse (complain) o proponer (suggest). Segundo, la audiencia (audience): a quién te diriges cambia el saludo y el tono. A una directora le escribes Dear Ms. Rojas, I am writing to suggest...; a compañeros puedes escribir Hi everyone y usar un tono más cercano. Tercero, la postura (stance) en una oración clara.",
        "Para formular la postura usa expresiones como In my opinion, I believe that, I would argue that, From my point of view, I am in favor of... y I am against... Si dudas, puedes marcarlo: I am not convinced that... Una buena postura es específica: 'Social media is bad' es demasiado amplia; 'Spending more than three hours a day on social media can reduce study time' es concreta y se puede defender. Después escribe dos razones (reasons) que apoyen exactamente esa postura.",
        "Al planificar, piensa en inglés desde el principio con frases cortas que ya conoces, en lugar de escribir en español y traducir palabra por palabra. Elige un registro adecuado: formal (Dear..., I would like to...) para autoridades y formularios; neutro o cercano para una publicación entre compañeros. Revisa que cada razón sea sobre el mismo tema que la postura.",
    ],
    [("purpose", "propósito"), ("audience", "audiencia"), ("stance", "postura"), ("reason", "razón"), ("in favor of / against", "a favor de / en contra de"), ("I am not convinced that", "no estoy convencido de que")],
    [
        ("Elegir la postura clara", PROMPT + " ¿Cuál de estas oraciones es una postura clara? A) In my opinion, phones should be allowed in class only for learning tasks. B) Phones are in many classes. C) This text is about phones.", ["Una postura toma posición con In my opinion.", "Dice cuándo sí y cuándo no, así es concreta.", "Las otras dos solo describen o anuncian el tema."], "A) In my opinion, phones should be allowed in class only for learning tasks."),
        ("Elegir el saludo según la audiencia", "Escribes a una directora, Ms. Rojas, para proponer un cambio. ¿Qué inicio es adecuado? A) Dear Ms. Rojas, I am writing to suggest a change. B) Hey! Listen up!", ["Una autoridad merece un registro formal.", "Dear + nombre y I am writing to suggest son formales.", "Hey! Listen up! es demasiado informal."], "A) Dear Ms. Rojas, I am writing to suggest a change."),
    ],
    [
        ("Escribir una postura demasiado amplia.", "Una postura como 'Social media is bad' no se puede defender con dos razones.", "Hazla concreta con cifras o condiciones."),
        ("Escribir razones que no son de la misma postura.", "Se mezcla un tema distinto y el texto pierde claridad.", "Pregunta si cada razón responde a la postura."),
    ],
    [
        mc("¿Cuál de estas oraciones expresa una postura en contra de la tarea diaria?", "I do not think that homework should be given every day", ["Homework is a word that students know very well", "I am in favor of longer breaks for all students"], "Expresa duda sobre la tarea diaria; las otras no hablan de ella con una postura."),
        mc("¿Qué significa I am in favor of longer breaks?", "estoy a favor de recreos más largos", ["estoy en contra de recreos más largos", "prefiero recreos más cortos"], "In favor of significa a favor de."),
        mc("¿Cuál saludo es formal?", "Dear Mr. Vera, I would like to ask about the schedule", ["Hey Vera, what's the schedule for tomorrow, please", "Yo Vera, tell me the schedule right now"], "Dear + apellido y I would like to ask son formales."),
    ],
    [
        mc("Postura: 'The school should start later.' ¿Cuál es una razón que la apoya?", "Teenagers need more sleep to concentrate", ["Cafeterias should sell more fruit", "Many students have phones"], "La razón del sueño se relaciona directamente con el horario."),
        mc("Escribes: 'I am writing to complain about the broken heater in room 12, and I ask you to repair it.' (heater = calefactor, broken = roto, repair = reparar). ¿Cuál es el propósito?", "quejarse y pedir una solución", ["invitar a una fiesta", "contar una anécdota"], "Dice complain y ask you to repair it."),
        mc("Escribes en un blog de compañeros. ¿Qué tono es adecuado?", "cercano y claro, con you y frases cortas", ["muy legal y con palabras complejas", "con órdenes bruscas"], "La audiencia es de pares y el tono debe ser accesible."),
    ],
    [
        mc("¿Cuál postura es más concreta y defendible?", "Spending more than three hours a day on social media can reduce study time", ["Everyone uses social media every single day of the week, even at school", "Social media is bad for teenagers and also for the whole of society"], "La primera incluye una condición y un efecto específico."),
        mc("¿Qué postura deja espacio a otras opiniones?", "I tend to think that school days should be shorter", ["Anyone who disagrees with this idea is simply wrong", "School days must be shorter, and that is final"], "I tend to think suaviza y reconoce que hay otras miradas."),
        mc("Escribes a tu profesora de Inglés para pedir más tiempo para un trabajo. ¿Cuál inicio es mejor?", "Dear Ms. Pérez, I would like to ask for two more days", ["Hey, give me two more days for the assignment", "Teacher, you must extend the deadline for everybody"], "Dear y I would like to ask son formales y corteses."),
    ],
    [
        mc("Postura: 'Schools should have a recycling program.' Una compañera propone la razón 'Recycling is a word in English'. ¿Qué problema tiene?", "no es una razón: no explica por qué conviene hacerlo", ["es una razón válida, pero debería estar en pasado", "es una razón válida, pero falta traducirla al español"], "Una razón debe explicar por qué la postura es buena, no solo nombrar el tema."),
        mc("Quieres que tu texto suene respetuoso con una postura distinta. ¿Qué plan es mejor?", "nombrar la otra postura y explicar por qué piensas diferente", ["ignorar la otra postura para que el texto sea más corto", "decir que quienes sostienen esa postura no piensan bien"], "Reconocer la postura contraria es parte de un texto crítico respetuoso."),
    ],
    [
        mc("Debes persuadir a la directora de cambiar el recreo. Tu borrador empieza: 'Yesterday I played soccer and my friend fell.' ¿Qué es lo más útil para mejorarlo?", "empezar con la postura: I believe that longer breaks help students concentrate", ["agregar más detalles de lo que pasó ayer en el recreo con mis amigos", "traducir el borrador al español palabra por palabra antes de enviarlo"], "El propósito es persuadir; el texto debe comenzar con la postura."),
        mc("Debes explicar a estudiantes de 12 años que saben poco inglés por qué es importante dormir. ¿Qué plan es mejor?", "frases cortas, palabras conocidas y un ejemplo", ["frases largas con términos técnicos", "solo una lista de palabras difíciles"], "El texto debe adaptarse a la audiencia."),
    ],
    [mc("Quieres escribir 'Estoy de acuerdo con eso' en inglés. ¿Cuál es correcto?", "I agree with that", ["I am agree with that", "I have agree with that"], "En inglés se dice I agree, sin am ni have.")],
    [
        ("En Inglés de 3.º medio (OA 2, clase 1): ¿qué es la postura de un texto?", "La posición del autor ante un tema", "Dice si está a favor, en contra o neutral."),
        ("En Inglés de 3.º medio (OA 2, clase 1): ¿cómo se dice no estoy convencido de que?", "I am not convinced that", "Marca una duda sin afirmar todo."),
        ("En Inglés de 3.º medio (OA 2, clase 1): ¿por qué se planifica antes de escribir?", "Para tener claros propósito, audiencia, postura y razones", "El plan evita textos confusos."),
    ],
    task("Elige una de estas consignas: A) «Should school lunches include more vegetables?» o B) «Should students choose some of their class topics?» (lunches = almuerzos, choose = elegir). Escribe en inglés un plan de cuatro líneas: Audience: ..., Stance: ..., Reason 1: ... Reason 2: ...", "Audience: school principal. Stance: In my opinion, school lunches should include more vegetables. Reason 1: Students need healthy food to concentrate. Reason 2: Fresh vegetables are cheap in the area.", ["la postura es clara", "las dos razones apoyan la postura", "la audiencia está indicada"], ["plan con cuatro líneas"], ["postura demasiado amplia", "razones de otro tema"], "Revisa que cada razón responda a la postura y reduce una postura demasiado amplia."),
    "Escribe tres posturas distintas con In my opinion y decide cuál es más concreta.",
    "Escribe en español dos razones para una postura que defiendas y tradúcelas a frases cortas en inglés.",
)

# ------------------------------------------------------------------ clase 2: estructura de un párrafo argumentativo
P1 = "«I believe that schools should offer a cooking class. First, cooking teaches practical skills that students use at home. Second, it can improve healthy habits. For example, students who prepare a salad often want to eat it. As a result, a cooking class would help both learning and health.» (cooking class = taller de cocina, practical = práctico, skills = habilidades, prepare = preparar, as a result = como resultado)"

lesson(
    OA2, 2, MAT_R,
    "Aprenderé a organizar un párrafo argumentativo con postura, razones, ejemplos y cierre, usando conectores como first, second, for example, however y as a result. Sirve para que mis textos breves sean claros y tengan una postura crítica bien apoyada.",
    ["Sé planificar una postura con dos razones.", "Conozco because y for example."],
    [
        "Un párrafo argumentativo tiene cuatro partes. 1) Oración temática (topic sentence) con la postura: I believe that schools should offer a cooking class. 2) Razones (reasons) introducidas con First y Second o con One reason is that... 3) Ejemplo o evidencia (example, evidence) con For example o For instance. 4) Cierre (conclusion) con As a result, Therefore o In conclusion.",
        "Los conectores muestran la relación entre ideas. Para sumar: also, in addition. Para ejemplificar: for example, for instance. Para causa: because, since. Para resultado: so, as a result, therefore. Para contraste: however, but, on the other hand. Para ordenar: first, second, finally. Un conector equivocado cambia el sentido: Because marca causa; however marca contraste. Usa cada razón con una sola idea.",
        "Para cuidar la claridad, escribe oraciones de 10 a 20 palabras, un solo tema por párrafo y evita repetir la misma palabra. No escribas todo en una sola oración larga. Si un ejemplo es tuyo, di que es tuyo: In my school, ... Si lo inventas para practicar, rotúlalo como ejemplo. La conclusión debe repetir la postura con otras palabras, no agregar un tema nuevo.",
    ],
    [("topic sentence", "oración temática: contiene la postura"), ("reason", "razón"), ("for example", "por ejemplo"), ("as a result", "como resultado"), ("first / second / finally", "primero / segundo / finalmente"), ("however", "sin embargo")],
    [
        ("Reconocer la oración temática", P1 + " ¿Cuál es la oración temática?", ["La oración temática expone la postura.", "I believe that schools should offer a cooking class lo hace.", "Las siguientes dan razones, ejemplo y cierre."], "I believe that schools should offer a cooking class."),
        ("Ordenar partes de un párrafo", "Ordena con letras: a) For example, a student who makes a salad may want to eat it. b) I believe that every school should have a library corner. c) A corner with books encourages reading. Escribe las letras en el orden de postura, razón y ejemplo.", ["La postura va primero: b.", "La razón general sigue: c.", "El ejemplo cierra la razón: a."], "b, c, a"),
    ],
    [
        ("Usar however para añadir una razón del mismo lado.", "However marca contraste; para sumar se usa also o in addition.", "Pregunta si la nueva idea suma o se opone."),
        ("Cerrar con un tema nuevo.", "La conclusión debe volver a la postura, no abrir otra discusión.", "Reformula la postura con otras palabras."),
    ],
    [
        mr(P1, "¿Qué conectores ordenan las razones?", "First y Second", ["For example y As a result", "However y Because"], "First y Second numeran las razones."),
        mr(P1, "¿Qué introduce For example?", "un ejemplo que apoya la segunda razón", ["una nueva postura", "un contraste con la primera razón"], "El ejemplo de la ensalada apoya los hábitos saludables."),
        mr(P1, "¿Qué hace la última oración?", "cierra el párrafo con el resultado", ["introduce un contraste", "presenta una duda"], "As a result concluye el argumento."),
    ],
    [
        mc("¿Qué conector completa la oración: 'Bike lanes make streets safer; ___, they encourage people to cycle.'?", "in addition", ["however", "unlike"], "In addition suma una idea del mismo lado; however contrastaría."),
        mc("¿Qué conector completa la oración: 'Public libraries are free; ___, some people do not know about them.'?", "however", ["as a result", "for example"], "La segunda idea se opone a la primera."),
        mc("Elige la oración con la causa: 'The school has a garden ___ students want to learn about plants.'", "because", ["however", "finally"], "Because introduce la razón."),
    ],
    [
        mc("¿Qué oración temática es adecuada para un párrafo sobre bicicletas en la ciudad?", "I believe that cities should build more bike lanes", ["Bike lanes are in some places of the city", "Yesterday I rode my bike along the river"], "La primera toma una posición defendible."),
        mc("Falta el ejemplo: 'Bike lanes make streets safer. ___ a cyclist in a lane rides away from the cars.' Elige.", "For example,", ["In conclusion,", "However,"], "Se necesita introducir un ejemplo."),
        mc("¿Qué cierre es adecuado para el párrafo de la clase de cocina?", "In conclusion, cooking classes would be useful for students", ["However, cooking is difficult for many teenagers", "First, students like salads at lunch time"], "Retoma la postura."),
    ],
    [
        mc("Un párrafo tiene una sola oración larga con cinco ideas unidas por and. ¿Qué es mejor?", "dividirlo en oraciones de 10 a 20 palabras con conectores", ["eliminar la postura para que el texto sea más corto", "añadir más and entre las ideas para unirlas"], "Las oraciones breves y conectadas son más claras."),
        mc("Un alumno escribe 'Also, cooking is difficult' como segunda razón para apoyar una clase de cocina. ¿Qué problema tiene?", "la razón va en contra de la postura", ["usa mal el conector also al comienzo de la oración", "le falta un verbo conjugado para ser una razón"], "Una razón difícil o negativa no apoya la clase."),
    ],
    [
        mc("¿Qué conclusión repite la postura sin introducir un tema nuevo? Postura: more green spaces are needed.", "Therefore, cities need more green spaces", ["Finally, buses are late", "For example, my cousin lives far away"], "Therefore conecta con la postura."),
        mc("Observa: 'Sports teach teamwork. For instance, players must pass the ball. In addition, ___.' ¿Qué cierre es correcto?", "sports also improve health", ["however, I like pizza", "in conclusion, as a result"], "In addition suma una razón del mismo lado."),
    ],
    [mc("Quieres decir 'por esa razón'. ¿Qué conector usas?", "Therefore", ["Unlike", "Whereas"], "Therefore marca resultado.")],
    [
        ("En Inglés de 3.º medio (OA 2, clase 2): ¿qué es la oración temática?", "La oración que expresa la postura del párrafo", "Introduce la idea principal."),
        ("En Inglés de 3.º medio (OA 2, clase 2): ¿para qué sirve for example?", "Para introducir un ejemplo", "Apoya una razón con un caso."),
        ("En Inglés de 3.º medio (OA 2, clase 2): ¿qué conectores indican resultado?", "As a result y therefore", "Ambos marcan una consecuencia."),
    ],
    task("Completa un párrafo de ejemplo con tus propias palabras: «I believe that ___. First, ___. For example, ___. As a result, ___.» Elige el tema: A) schools should have a quiet room, o B) buses should be free for students. (quiet room = sala tranquila)", "I believe that schools should have a quiet room. First, students sometimes need to rest. For example, a student with a headache can sit there. As a result, the classes can continue calmly.", ["usa las cuatro partes", "cada parte coincide con el tema", "usa los conectores indicados"], ["párrafo de cuatro oraciones"], ["razones sin relación", "no usar conectores"], "Revisa que cada oración cumpla su función y reemplaza los conectores equivocados."),
    "Vuelve al párrafo sobre la clase de cocina del primer ejemplo resuelto y marca cada parte con un color diferente.",
    "Escribe tres conectores de la explicación que no hayas usado y una oración con cada uno.",
)

# ------------------------------------------------------------------ clase 3: lenguaje para discrepar con respeto
D1 = "«Mia: I think all students should wear a uniform. Leo: I see your point, but I tend to think that clothes help students feel comfortable. Mia: That is interesting. Could you explain why? Leo: Some students feel more confident in their own clothes.» (point = punto, comfortable = cómodo, explain = explicar, confident = seguro de sí mismo)"

lesson(
    OA2, 3, MAT_R,
    "Aprenderé a discrepar con respeto en inglés usando frases como I see your point, but..., Could you explain...? y expresiones que suavizan (may, might, tend to, some). Sirve para expresar una postura crítica sin ofender a otras personas.",
    ["Sé escribir una postura con una razón.", "Conozco I agree y I disagree."],
    [
        "Discrepar (disagree) con respeto no es no opinar: es criticar la idea y no a la persona. Se usan frases como I see your point, but..., I understand why you think that, however..., I would like to add that..., Could you explain why you think so? y That is interesting. Evita You are wrong o That is stupid: atacan a la persona y no entregan una razón.",
        "Para suavizar una afirmación se usan los verbos modales may y might (puede que), el verbo tend to (suele), cuantificadores como some, many o often en lugar de all o always, y expresiones como it seems that o I am not sure that. Ejemplos: Some students feel more confident in their own clothes. This might help. Con estas palabras el hablante deja claro que habla de una tendencia y no de una verdad absoluta.",
        "Una buena respuesta crítica sigue tres pasos: reconoce lo que el otro dijo (I see your point), expresa tu postura (but I tend to think that...), y da una razón (because...). En el habla, tu tono de voz y tus preguntas también demuestran respeto: Could you explain? invita a seguir conversando. Evita traducir expresiones del español en forma literal: I am agree es un error; se dice I agree.",
    ],
    [("I see your point, but", "entiendo tu punto, pero"), ("Could you explain why?", "¿podrías explicar por qué?"), ("tend to", "suele / tiende a"), ("might / may", "puede que"), ("some / many / often", "algunos / muchos / a menudo"), ("I am not sure that", "no estoy seguro de que")],
    [
        ("Identificar una frase respetuosa", D1 + " ¿Qué frase de Leo reconoce la postura de Mia antes de discrepar?", ["Busco una frase que valide antes de decir pero.", "I see your point, but... reconoce a Mia.", "Después viene su postura con I tend to think that."], "I see your point, but..."),
        ("Suavizar una afirmación", "Convierte 'All teachers give too much homework' en una frase más cuidadosa. Elige: A) Some teachers may give too much homework. B) Teachers are bad.", ["La frase debe hablar de una parte, no de todos.", "Some y may suavizan la afirmación.", "La B juzga a todas las personas."], "A) Some teachers may give too much homework."),
    ],
    [
        ("Decir You are wrong como respuesta crítica.", "Ataca a la persona y no da razón.", "Reconoce y da una razón: I see your point, but I think that..."),
        ("Usar I am agree.", "Es una traducción literal; en inglés agree es un verbo.", "Di I agree."),
    ],
    [
        mr(D1, "¿Qué pregunta hace Mia para invitar a seguir conversando?", "Could you explain why?", ["I think all students should wear a uniform", "That is interesting"], "La pregunta pide una razón y mantiene el diálogo."),
        mc("¿Cuál es una forma respetuosa de discrepar?", "I understand why you think that, but I see it differently", ["You are wrong, and I will not listen to your reasons", "That is a silly idea, and nobody agrees with it"], "Reconoce al otro antes de plantear su diferencia."),
        mc("¿Qué significa tend to?", "suele / tiende a", ["nunca", "es obligatorio"], "Tend to expresa una tendencia."),
    ],
    [
        mr(D1, "¿Qué razón da Leo para su postura?", "algunos estudiantes se sienten más seguros con su ropa", ["los uniformes son caros para muchas familias", "los uniformes no se ven bien en los estudiantes"], "Dice that some students feel more confident in their own clothes."),
        mc("¿Qué palabra suaviza esta afirmación? 'Some students might prefer shorter classes.'", "might", ["students", "classes"], "Might indica posibilidad, no certeza."),
        mc("¿Cuál de estas respuestas incluye una razón?", "I disagree because many students need time to rest", ["I disagree, and that is all I wanted to say", "I disagree, period, with nothing else to add"], "La razón con because da fundamento."),
    ],
    [
        mc("Alguien dijo: 'Social media is useful for school.' Elige una respuesta respetuosa que discrepe parcialmente.", "I see your point, but I think it may also distract students", ["Nobody learns anything from social media at school", "That is false, and you should not say it"], "Reconoce y matiza con may."),
        mc("¿Qué frase pide una aclaración sin sonar brusca?", "Could you say a little more about that?", ["Say it again now, please, so I can write it", "Why would you say something like that"], "Could you es cortés."),
        mc("Corrige: 'Everybody dislikes early classes.' Elige la versión más cuidadosa.", "Many students dislike early classes", ["All students hate early classes", "Nobody likes classes"], "Many evita la generalización total."),
    ],
    [
        mc("Un compañero responde a una opinión con 'You always say silly things.' ¿Qué problema tiene la frase?", "critica a la persona con always y no responde a la idea", ["usa mal el verbo say en presente simple", "es demasiado larga para ser una respuesta cortés"], "Debe criticar la idea con una razón."),
        mc("¿Qué opción reconoce, discrepa y da una razón?", "I understand your point; however, I tend to think that a shorter break is enough because lessons are long", ["I disagree with your point because it is wrong, and I will not change my mind about this", "You are wrong because I said so, and that should be enough of a reason for you"], "Tiene los tres pasos."),
    ],
    [
        mc("Lees: 'Mia: Some people think homework helps. I think it can be too much. Leo: That is a fair point. I tend to think that a little each day works.' (fair = justo). ¿Qué hace Leo?", "reconoce la idea de Mia y propone una variante", ["rechaza la idea de Mia sin dar ninguna razón", "cambia de tema para no hablar de la tarea"], "Reconoce y matiza."),
        mc("¿Qué opción es un error de traducción literal del español?", "I am agree with you", ["I agree with you", "I think so too"], "Se dice I agree, sin am."),
    ],
    [mc("En un chat un compañero escribe: 'Cats are better than dogs. Fact.' Tú no estás de acuerdo. ¿Qué respuesta es respetuosa?", "I see your point, but for me dogs are better because they like to play outdoors", ["That is a stupid opinion and you know nothing about pets", "You know nothing about pets, so your opinion is not valid"], "Reconoce y da una razón, sin atacar.")],
    [
        ("En Inglés de 3.º medio (OA 2, clase 3): ¿para qué sirve I see your point, but?", "Para reconocer lo que dijo el otro antes de discrepar", "Muestra respeto y escucha."),
        ("En Inglés de 3.º medio (OA 2, clase 3): ¿qué verbos modales suavizan una afirmación?", "May y might", "Indican posibilidad y no certeza."),
        ("En Inglés de 3.º medio (OA 2, clase 3): ¿qué error evita decir I agree en lugar de I am agree?", "La traducción literal del español", "Agree ya es un verbo."),
    ],
    task("Lee esta opinión: «Teenagers should have no homework at all.» (teenagers = adolescentes). Escribe en inglés una respuesta de dos o tres oraciones que reconozca la idea, discrepe de forma parcial con una razón y use una palabra que suavice (some, may, might o tend to).", "I see your point, but I tend to think that some homework helps. For example, practice may help students remember things. Maybe a small amount is enough.", ["reconoce la idea", "da una razón", "usa una palabra que suaviza"], ["respuesta en inglés"], ["usar You are wrong", "no dar razón"], "Marca las tres partes y reescribe lo que ataca a la persona."),
    "Practica con una persona de tu casa: ella dice una opinión y tú respondes con I see your point, but...",
    "Escribe tres frases que suavicen una afirmación absoluta con some, many o tend to.",
)

# ------------------------------------------------------------------ clase 4: comunicar una postura oralmente
SPEECH = "«Good afternoon, everyone. Today I want to talk about public libraries. To begin with, they are free, so everybody can use them. Let me give an example: my local library offers computers and quiet rooms. Some people say that books are old-fashioned. I understand that point, but libraries also have films and workshops. In conclusion, public libraries deserve our support. Thank you.» (to begin with = para comenzar, free = gratis, offers = ofrece, quiet rooms = salas silenciosas, workshops = talleres, deserve = merecen, support = apoyo)"

lesson(
    OA2, 4, MAT_L,
    "Aprenderé a presentar mi postura en una intervención oral breve de uno o dos minutos: apertura, dos razones, una concesión y cierre. Sirve para comunicar una postura crítica con claridad y respeto ante un grupo.",
    ["Sé estructurar un párrafo con razones y ejemplos.", "Sé discrepar con respeto."],
    [
        "Una intervención oral breve (short talk) tiene la misma estructura que un párrafo, con marcadores de habla. Apertura: Good afternoon, everyone. Today I want to talk about... Razones: To begin with..., Another reason is that..., Let me give an example. Concesión: Some people say... I understand that point, but... Cierre: In conclusion,... Thank you. Estos marcadores guían al público.",
        "Para que te entiendan, habla con calma, haz pausas al terminar una idea, destaca con la voz las palabras clave (free, example, conclusion) y mira al público. No necesitas un acento perfecto: lo importante es que el mensaje sea claro, con frases cortas y vocabulario que conozcas. Prepara tarjetas con palabras clave y no con el texto completo, así suenas más natural.",
        "Respeta a tu audiencia: usa we y you con cuidado, no ridiculices otras posturas y reconoce los argumentos válidos. Si te equivocas, repara con Sorry, let me say that again. Si no entiendes una pregunta, di Could you repeat that, please? Una buena intervención dura lo que se planificó: 60 a 90 segundos son alrededor de 120 a 180 palabras.",
    ],
    [("to begin with", "para comenzar"), ("let me give an example", "déjame dar un ejemplo"), ("in conclusion", "en conclusión"), ("short talk", "intervención oral breve"), ("key word", "palabra clave"), ("let me say that again", "déjame decirlo de nuevo")],
    [
        ("Reconocer partes de la intervención", "Un adulto o tú lees en voz alta: " + SPEECH + " ¿Qué frase es la concesión?", ["La concesión reconoce otra postura.", "Some people say that books are old-fashioned. I understand that point, but... lo hace.", "Después la autora mantiene su postura."], "Some people say that books are old-fashioned. I understand that point, but libraries also have films and workshops."),
        ("Planificar el tiempo", "Una intervención de 60 segundos con unas 120 palabras. Si tienes 4 partes (apertura, razón 1, razón 2, cierre) y quieres 30 palabras por parte, ¿cuántas palabras escribes en total?", ["Hay 4 partes de 30 palabras.", "4 por 30 son 120.", "Coincide con el tiempo."], "120 palabras"),
    ],
    [
        ("Leer el texto completo sin mirar al público.", "El público pierde contacto y la voz suena monótona.", "Usa tarjetas con palabras clave."),
        ("Decir nada cuando uno se equivoca.", "El error queda sin reparar.", "Usa Sorry, let me say that again."),
    ],
    [
        ml(SPEECH, "¿Cuál es la postura de la hablante?", "las bibliotecas públicas merecen apoyo", ["las bibliotecas son anticuadas", "los libros son caros"], "Dice In conclusion, public libraries deserve our support."),
        ml(SPEECH, "¿Qué razón da para decir que todos pueden usar las bibliotecas?", "son gratis", ["abren de noche", "regalan libros"], "Dice they are free, so everybody can use them."),
        mc("¿Qué frase sirve para comenzar una intervención?", "Good afternoon, everyone. Today I want to talk about...", ["I don't know what to say, so I will just start", "That is all for today. Thank you for listening"], "La apertura saluda y presenta el tema."),
    ],
    [
        ml(SPEECH, "¿Qué ejemplo da la hablante?", "su biblioteca local ofrece computadores y salas silenciosas", ["su biblioteca vende libros usados a precios bajos", "su biblioteca cierra a las seis de la tarde"], "Let me give an example introduce el ejemplo."),
        ml(SPEECH, "¿Qué hace Some people say that books are old-fashioned?", "presenta otra postura que luego reconoce", ["introduce la conclusión de la intervención", "agradece al público por escuchar"], "Es la postura contraria, a la que responde con I understand that point."),
        mc("¿Cuál frase repara un error al hablar?", "Sorry, let me say that again", ["That doesn't matter", "I am agree"], "Es una frase de reparación."),
    ],
    [
        mc("Preparas una intervención de 90 segundos. ¿Qué es mejor usar mientras hablas?", "tarjetas con palabras clave", ["el texto completo para leerlo palabra por palabra", "nada de preparación"], "Las tarjetas ayudan a hablar con naturalidad."),
        mc("¿Qué marcador indica una segunda razón?", "Another reason is that", ["In conclusion", "Good afternoon"], "Another reason is that añade una razón."),
        mc("¿Qué frase de una intervención introduce un ejemplo?", "Let me give an example", ["In conclusion", "Thank you"], "Let me give an example anuncia el ejemplo que apoya la razón."),
    ],
    [
        mc("Un compañero dice que no importa el acento, solo la claridad. Según lo estudiado, ¿qué es correcto?", "lo esencial es que el mensaje sea claro, con frases cortas y vocabulario conocido", ["el acento perfecto es obligatorio para que otras personas te entiendan bien", "hay que hablar rápido y sin pausas para sonar siempre fluido ante el público"], "La claridad es más importante que imitar un acento."),
        ml(SPEECH, "¿Qué opción describe mejor la actitud de la hablante?", "respeta otras posturas y mantiene la suya", ["rechaza las ideas ajenas sin dar razones", "evita decir lo que piensa para no discutir"], "Concede que otros piensan distinto y aun así defiende su postura."),
    ],
    [
        mc("Durante una intervención olvidas una palabra. ¿Qué haces mejor?", "usar otra palabra que conozcas o decir: what I mean is...", ["quedarte callado hasta que recuerdes la palabra exacta", "pasar a otro tema sin avisar a quien te escucha"], "Reformular mantiene la comunicación."),
        mc("¿Qué cierre es adecuado para una intervención sobre bibliotecas?", "In conclusion, I believe that libraries are valuable. Thank you", ["However, I do not know much about libraries or about reading", "First, I would like to begin this talk with a question for all"], "Cierra repitiendo la postura."),
    ],
    [mc("Escuchas una pregunta del público que no entiendes. ¿Qué dices?", "Could you repeat that, please?", ["I don't care about your question", "Stop asking me questions, please"], "Es una forma cortés de pedir repetición.")],
    [
        ("En Inglés de 3.º medio (OA 2, clase 4): ¿qué partes tiene una intervención oral breve?", "Apertura, razones, concesión y cierre", "Es la estructura del párrafo adaptada al habla."),
        ("En Inglés de 3.º medio (OA 2, clase 4): ¿cómo se dice en conclusión?", "In conclusion", "Se usa en el cierre."),
        ("En Inglés de 3.º medio (OA 2, clase 4): ¿para qué sirve Could you repeat that, please?", "Para pedir con cortesía que repitan", "Es una frase de reparación al escuchar."),
    ],
    task("Prepara una intervención de cinco a siete oraciones en inglés sobre uno de estos temas: A) public parks, B) night buses for students. Incluye apertura, una razón, un ejemplo, una concesión con I understand that point, but... y un cierre. (night buses = buses nocturnos)", "Good afternoon, everyone. Today I want to talk about public parks. To begin with, they are free. For example, families can play there. Some people say that parks cost too much. I understand that point, but parks also help people stay healthy. In conclusion, parks deserve our support.", ["tiene las cinco partes", "las oraciones son claras", "mantiene un tono respetuoso"], ["texto de cinco o seis oraciones", "lectura en voz alta con una persona de tu casa"], ["no incluir la concesión", "frases demasiado largas"], "Marca cada parte, acorta las oraciones largas y practica la lectura en voz alta con pausas."),
    "Lee en voz alta tu texto con pausas y marca dónde destacas las palabras clave.",
    "Escribe dos frases de reparación y practícalas en voz alta.",
)

# ------------------------------------------------------------------ clase 5: reparar y revisar el sentido
DRAFT = "«I think that the school are very noisy. Also the students no listen the teacher. In my opinion is necessary a quiet zone, because I have 17 years and I need study.» (noisy = ruidoso, quiet zone = zona tranquila, listen to = escuchar a)"

lesson(
    OA2, 5, MAT_R,
    "Aprenderé a revisar y reparar un texto mío o de un compañero: corregir errores comunes (concordancia, orden, traducción literal), mejorar la claridad y cuidar el tono. Sirve para que mi postura crítica se entienda y se exprese con respeto.",
    ["Sé organizar un párrafo con postura y razones.", "Sé usar frases de discrepancia respetuosa."],
    [
        "Revisar (revise) es leer tu texto como lector: ¿se entiende mi postura?, ¿cada razón apoya la postura?, ¿hay frases demasiado largas?, ¿el tono es respetuoso? Luego se corrige (edit) la gramática. Un buen orden es revisar primero el sentido, después el orden de las ideas y al final la ortografía y los verbos.",
        "Errores frecuentes por transferencia del español: the school are (el verbo debe concordar con el sujeto singular: the school is); the students no listen (la negación en presente es don't: the students don't listen); necessary a quiet zone (el inglés exige sujeto: it is necessary to have a quiet zone o we need a quiet zone); I have 17 years (la edad se dice con be: I am 17 years old); I need study (I need to study); more better (better); depend of (depend on); make homework (do homework); actually no significa actualmente sino en realidad (currently es actualmente).",
        "Para reparar el sentido en la conversación o por escrito, reformula: What I mean is..., In other words..., Let me rephrase that. Si el lector pudo malentender una crítica, agrega una frase que aclare tu intención: I do not mean that all students..., I am only saying that... Una buena revisión conserva la voz del autor, pero hace el texto más claro y respetuoso.",
    ],
    [("revise / edit", "revisar el sentido / corregir la forma"), ("subject-verb agreement", "concordancia sujeto-verbo"), ("don't + verb", "negación en presente"), ("in other words", "en otras palabras"), ("what I mean is", "lo que quiero decir es"), ("false friend", "falso amigo")],
    [
        ("Corregir una concordancia", "Corrige: 'The school are very noisy.' Elige. A) The school is very noisy. B) The school be very noisy.", ["Sujeto singular: the school.", "Con singular se usa is.", "Be sola no se conjuga así en presente."], "A) The school is very noisy."),
        ("Corregir la edad", "Corrige: 'I have 17 years.' Elige. A) I am 17 years old. B) I am 17 years.", ["En inglés la edad se dice con be.", "Se añade years old.", "I am 17 years sin old queda incompleta; se dice I am 17 o I am 17 years old."], "A) I am 17 years old."),
    ],
    [
        ("Corregir solo la ortografía y no revisar el sentido.", "Un texto bien escrito pero confuso no comunica.", "Revisa primero el sentido, luego el orden y por último la forma."),
        ("Pensar que actually significa actualmente.", "Es un falso amigo: significa en realidad.", "Para actualmente usa currently."),
    ],
    [
        mc("¿Cuál es la versión correcta de 'The students no listen the teacher'?", "The students don't listen to the teacher", ["The students no listen to the teacher", "The students not listening the teacher"], "La negación en presente lleva don't y listen se usa con to."),
        mc("¿Qué es lo correcto? 'I ___ to study.'", "need", ["needs", "am need"], "Con I se usa need, seguido de to study."),
        mc("¿Cuál frase es correcta?", "I do my homework every day", ["I make my homework every day", "I does my homework every day"], "Se dice do homework."),
    ],
    [
        mc("Corrige: 'In my opinion is necessary a quiet zone.'", "In my opinion, it is necessary to have a quiet zone", ["In my opinion is necessary to have a quiet zone", "In my opinion, necessary is a quiet zone"], "El inglés necesita un sujeto: it."),
        mc("Corrige 'more better'.", "better", ["more good", "most better"], "Better ya es comparativo."),
        mc("Corrige: 'It depends of the time.'", "It depends on the time", ["It depends at the time", "It depend of time"], "Depend se usa con on."),
    ],
    [
        mc("Una crítica podría malentenderse como un ataque. ¿Qué frase aclara la intención?", "I do not mean that all students make noise; I am only saying that some do", ["Everybody knows I am right about the noise that students make at school", "Students are noisy, period, and that is a fact nobody can deny at all"], "Aclara que no generaliza."),
        mc("Un compañero no entiende tu oración. ¿Qué frase usas para reformular?", "In other words, I think that the school needs a quiet room", ["Whatever, I think the school is fine like this", "That is how it is, and nothing will change"], "Reformular repara la comunicación."),
        mc("¿Qué significa currently?", "actualmente", ["en realidad", "frecuentemente"], "Actually es en realidad y currently es actualmente."),
    ],
    [
        mc("Texto: " + DRAFT + " ¿Qué conviene revisar primero?", "si la postura y las razones se entienden", ["si los verbos concuerdan con el sujeto", "si la ortografía de cada palabra es perfecta"], "Primero se revisa el sentido."),
        mc("Texto: " + DRAFT + " ¿Qué corrección NO es necesaria?", "cambiar noisy por loud", ["cambiar are por is", "cambiar have 17 years por am 17 years old"], "Noisy es correcta y suficiente; las otras dos corrigen errores de concordancia y de edad."),
    ],
    [
        mc("Elige la versión correcta de 'The teachers gives a lot of homework and the students no like it'.", "The teachers give a lot of homework and the students don't like it", ["The teachers gives a lot of homework and the students doesn't like it", "The teachers give a lot of homework and the students no likes it"], "Teachers es plural (give) y la negación en presente lleva don't."),
        mc("¿Cuál es la mejor versión completa de 'In my opinion is necessary a quiet zone, because I have 17 years and I need study'?", "In my opinion, it is necessary to have a quiet zone because I am 17 years old and I need to study", ["In my opinion, necessary a quiet zone because I have 17 years and need study", "In my opinion is necessary a quiet zone, I am 17 and need study"], "Corrige sujeto, edad e infinitivo."),
    ],
    [mc("Quieres decir 'Estoy cansado de esta situación'. ¿Qué versión es correcta?", "I am tired of this situation", ["I have tired of this situation", "I tire of this situation yesterday"], "Se usa be + adjetivo.")],
    [
        ("En Inglés de 3.º medio (OA 2, clase 5): ¿qué se revisa primero en un texto?", "El sentido y la claridad de la postura", "Después se corrigen orden y forma."),
        ("En Inglés de 3.º medio (OA 2, clase 5): ¿cómo se dice tengo 17 años en inglés?", "I am 17 years old", "La edad se dice con be."),
        ("En Inglés de 3.º medio (OA 2, clase 5): ¿qué frase ayuda a reformular?", "In other words, ...", "Dice lo mismo con otras palabras."),
    ],
    task("Corrige este borrador y mejora su claridad: «I think that the cafeteria are too expensive. Many students no buy lunch. In my opinion is necessary lower prices.» (cafeteria = casino, expensive = caro, lower = bajar). Reescríbelo en inglés con tres oraciones correctas y una frase que aclare tu intención.", "I think that the cafeteria is too expensive. Many students don't buy lunch. In my opinion, it is necessary to lower prices. I do not mean that the staff is wrong; I am only saying that prices are high.", ["corrige la concordancia", "corrige la negación", "agrega el sujeto it", "incluye una frase de aclaración"], ["texto revisado"], ["corregir solo una oración", "no aclarar la intención"], "Marca cada error y su corrección y verifica con la tabla de errores frecuentes."),
    "Busca en tu cuaderno de inglés una oración tuya antigua y revisa si tiene alguno de los errores de la clase.",
    "Escribe tres errores típicos del español al inglés y cómo se corrigen.",
)
