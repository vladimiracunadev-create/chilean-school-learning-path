"""Cuaderno del estudiante, 1.º medio Inglés (oficial): IN1M OA 12, estrategias de lectura.

Prelectura (propósito, predicciones, conocimientos previos), lectura (lectura rápida y focalizada, elementos
organizacionales, inferencias, relectura) y poslectura (confirmar predicciones, organizadores gráficos, recontar,
resumir, preguntar). Textos originales con glosario en español dentro del enunciado.
"""
from __future__ import annotations

from student_content_in_m1_b import MAT, lesson, mc, task
from student_lessons import arith, ex

OA = "IN1M OA 12"

# ============================================================ clase 1: prelectura
TSU = "«Title: Tsunami Safety in a Coastal Town. Subtitle: What to do when the alarm sounds. Image: a street sign with an arrow and the words Safe Zone.»"
GTSU = "(safety = seguridad; coastal = costero; alarm = alarma; sounds = suena; sign = letrero; arrow = flecha)"
BEES = "«Title: The Secret Life of Bees. Subtitle: How a hive works together. Image: a close photo of bees on a honeycomb.»"
GBEES = "(bees = abejas; secret = secreto; hive = colmena; honeycomb = panal)"
PODC = "«Title: How to Start a Class Podcast. Subtitle: Five steps for beginners. Image: a student speaking into a microphone next to a numbered list.»"
GPODC = "(podcast = programa grabado de audio; microphone = micrófono; steps = pasos; beginners = principiantes; numbered list = lista numerada)"
STARS = "«Title: Atacama Stars: Astronomy for Beginners. Subtitle: Why the northern desert has some of the clearest skies. Image: a telescope under a night sky.»"
GSTARS = "(clearest = más despejados; skies = cielos; telescope = telescopio; night sky = cielo nocturno)"
HERO = "«Title: Hidden Heroes: People Who Keep the City Clean. Subtitle: A day with the night crew. Image: a worker in a bright jacket sweeping a street at dawn.»"
GHERO = "(hidden = ocultos; keep = mantienen; crew = equipo de trabajo; bright = brillante; sweeping = barriendo; dawn = amanecer)"
COV1 = "Portada 1: «Title: Secrets of the Old Lighthouse. Subtitle: A mystery for brave readers. Image: three kids with a lantern.»"
COV2 = "Portada 2: «Title: My First Vegetable Garden. Subtitle: Easy steps with seeds, soil and water. Image: hands planting a seed.»"
GCOV = "(lighthouse = faro; lantern = linterna; vegetable garden = huerta; seeds = semillas; soil = tierra; planting = plantando)"

lesson(
    OA, 1, MAT,
    "Aprenderé a prepararme antes de leer: decidir para qué leo, hacer predicciones con el título y las imágenes, y usar lo que ya sé. Sirve para leer con más rapidez y menos dudas.",
    ["Sé reconocer el título y las imágenes de un texto.", "Conozco palabras como topic, text y reader."],
    [
        "Antes de leer (pre-reading) hay tres estrategias. La primera es leer con un propósito (reading purpose): decidir para qué leo. Puedo leer para encontrar un dato concreto, para entender las ideas principales, para aprender cómo se hace algo o para disfrutar. El propósito cambia cómo leo: no se lee igual un horario que un cuento.",
        "La segunda estrategia es hacer predicciones (predictions): ideas sobre lo que el texto dirá, apoyadas en pistas como el título (title), el subtítulo (subtitle) y las imágenes (images). Una buena predicción se puede decir así: I think the text will explain… because the title says… La tercera estrategia es usar los conocimientos previos (prior knowledge): lo que ya sé del tema, por ejemplo que las abejas viven en grupo.",
        "Durante la lectura se comprueba cada predicción. Si el texto muestra algo distinto, no te quedes con la idea antigua: cámbiala con la nueva evidencia (evidence). Predecir bien no significa acertar siempre, sino usar pistas y revisarlas. Una predicción sin pista es solo una adivinanza.",
    ],
    [("reading purpose", "propósito de lectura: para qué leo"), ("prediction", "predicción: idea de lo que dirá el texto"), ("prior knowledge", "conocimientos previos: lo que ya sé"), ("title / subtitle", "título / subtítulo"), ("image", "imagen"), ("evidence", "evidencia: pista del texto que apoya una idea"), ("I think the text will…", "creo que el texto…")],
    [
        ("Predecir con título, subtítulo e imagen", f"Antes de leer ves: {TSU} {GTSU} ¿Qué predicción haces y qué conocimiento previo usas?",
         ["El título y el subtítulo hablan de seguridad ante una alarma de tsunami.", "La imagen muestra un letrero con una flecha y Safe Zone.", "Predicción: el texto explicará cómo llegar a un lugar seguro siguiendo letreros. Conocimiento previo: las ciudades costeras tienen señales para evacuar."], "Predicción: explicará cómo llegar a una zona segura; conocimiento previo: existen señales de evacuación"),
        ("Elegir un propósito de lectura", "Necesitas saber a qué hora cierra el gimnasio del colegio y tienes un horario. ¿Qué propósito de lectura tienes y cómo lees?",
         ["No necesitas entender todo el horario.", "Tu propósito es encontrar un solo dato: la hora de cierre.", "Entonces buscas rápido la palabra closes y el número cercano."], "Propósito: encontrar un dato; busco directamente la hora de cierre"),
    ],
    [
        ("Hacer una predicción sin ninguna pista del título ni de la imagen.", "Una predicción sin pistas es una adivinanza.", "Apóyate en el título, el subtítulo o la imagen."),
        ("Mantener la predicción aunque el primer párrafo muestre otra cosa.", "No se revisa la predicción con la nueva evidencia.", "Cambia tu predicción cuando el texto la contradiga."),
    ],
    [
        mc("Leer con un propósito (reading purpose) significa", "decidir para qué voy a leer antes de empezar", ["leer solo en voz alta", "leer sin mirar el título"], "El propósito guía cómo leo."),
        mc("Una predicción (prediction) es", "una idea de lo que dirá el texto, basada en pistas", ["un resumen del final", "una palabra desconocida"], "Se hace antes de leer, con título e imágenes."),
        mc("Los conocimientos previos (prior knowledge) son", "lo que ya sé sobre el tema", ["lo que aprenderé después de leer", "las preguntas del profesor"], "Son lo que ya tengo antes de empezar."),
    ],
    [
        mc(f"Ves: {BEES} {GBEES} ¿Qué predicción tiene más apoyo?", "The text will explain how bees live and work as a group", ["The text will tell a story about a lost dog", "The text will give a recipe for honey cake"], "El subtítulo habla de una colmena que trabaja junta y la imagen muestra abejas."),
        mc(f"Ves: {BEES} {GBEES} ¿Qué parte del texto apoya mejor la idea de que las abejas trabajan en grupo?", "El subtítulo: How a hive works together", ["La palabra Secret", "La palabra Life"], "Together significa juntos y hive es la colmena."),
        mc(f"Vas a leer: {BEES} ¿Qué conocimiento previo te ayuda?", "Las abejas hacen miel y viven en grupos", ["Las hormigas viven bajo la tierra", "Los zorros viven en madrigueras"], "Se relaciona con el tema del texto."),
    ],
    [
        mc(f"Vas a grabar un podcast con tu curso y ves: {PODC} {GPODC} ¿Cuál es tu propósito de lectura?", "Aprender los pasos y seguirlos", ["Disfrutar un poema", "Buscar un teléfono"], "El subtítulo promete pasos para principiantes."),
        mc(f"Ves: {PODC} {GPODC} ¿Qué predicción apoya el subtítulo Five steps for beginners?", "El texto traerá cinco pasos explicados de forma sencilla", ["El texto será una novela larga", "El texto tratará de astronomía"], "Five steps y beginners anuncian una guía corta para empezar."),
        mc(f"El texto {PODC} tiene una sección llamada What you need. Solo quieres saber qué equipo comprar. ¿Qué propósito y qué estrategia eliges?", "Encontrar un dato: ir directo a la sección What you need", ["Leer cada palabra desde el inicio sin saltar", "Leer solo la última línea"], "Solo necesitas un dato, así que vas a la sección que lo contiene."),
    ],
    [
        mc(f"Ves: {STARS} {GSTARS} Luis predice: «The text will teach how to cook beans.» Ema predice: «The text will explain why the desert sky is clear for watching stars.» ¿Quién tiene más apoyo en las pistas?", "Ema, porque el título, el subtítulo y la imagen hablan de estrellas y de un cielo despejado", ["Luis, porque en el norte se cocinan muchos porotos", "Ninguno, porque no se puede predecir"], "Las pistas del texto apoyan el tema del cielo."),
        mc(f"Predijiste que el texto {STARS} hablaría de telescopios muy caros. El primer párrafo dice que se puede mirar el cielo sin telescopio. ¿Qué haces?", "Cambio mi predicción con la nueva evidencia", ["Mantengo mi predicción igual", "Dejo de leer"], "La estrategia exige revisar la predicción cuando el texto la contradice."),
    ],
    [
        mc("Tres tareas: (1) preparar una charla de dos minutos sobre abejas; (2) saber el horario de un museo; (3) disfrutar un cuento. ¿Qué propósito corresponde a cada una?", "1 leer con cuidado para entender las ideas; 2 buscar un dato; 3 leer por placer", ["1 buscar un dato; 2 leer por placer; 3 leer para entender las ideas"], "Una charla pide comprender ideas, un horario pide un dato y un cuento se disfruta."),
        mc("Crees que los delfines son peces y ves este título: «Dolphins Are Mammals». (dolphins = delfines; mammals = mamíferos) ¿Qué haces?", "Reviso mi conocimiento previo, porque el título lo contradice", ["Ignoro el título", "Cambio el título"], "Un conocimiento previo se puede corregir con nueva información."),
    ],
    [mc(f"En la biblioteca quieres un libro para aprender a hacer una huerta. {COV1} {COV2} {GCOV} ¿Cuál eliges?", "La portada 2, porque el subtítulo habla de pasos con semillas, tierra y agua", ["La portada 1, porque tiene una linterna", "Las dos sirven igual"], "El título y el subtítulo de la portada 2 calzan con tu propósito.")],
    [
        mc("¿Cuándo se hacen las predicciones?", "Antes de leer, con el título y las imágenes", ["Solo al terminar el texto"], "Pre-reading es la fase anterior a la lectura."),
        mc("¿Qué pistas ayudan a predecir el tema de una portada?", "El título, el subtítulo y la imagen", ["El número de página"], "Son pistas visibles antes de leer."),
        ("Escribe en inglés la palabra que significa «predicción».", "Prediction", "Prediction es la idea de lo que dirá el texto."),
    ],
    task(f"Antes de leer ves esta portada: {HERO} {GHERO} En tu hoja escribe: (1) tu propósito de lectura, (2) una predicción con la pista que la apoya, (3) un conocimiento previo que te ayuda.",
         "(1) Quiero entender qué trabajo hace el equipo de limpieza de noche. (2) I think the text will describe a worker's night because the subtitle says A day with the night crew. (3) Sé que en las ciudades la basura se recoge muy temprano.",
         ["el propósito dice para qué leo", "la predicción cita una pista del título, subtítulo o imagen", "el conocimiento previo se relaciona con el tema"],
         ["tres respuestas cortas en la hoja"],
         ["una predicción sin pista", "un conocimiento previo sin relación con el tema"],
         "Pide que cambie el subtítulo por otro y vea si cambia su predicción."),
    "Copia las siete palabras del vocabulario y dibuja un símbolo para cada una.",
    "Elige un libro de tu casa, mira solo la portada y escribe en español tu propósito y una predicción con su pista.",
)

# ============================================================ clase 2: lectura rápida, focalizada y elementos del texto
GREEN = "«Title: A Greener School. Subtitle: How Class 1B reduced paper waste. The Problem: Every day the school threw away about 40 kilos of paper. The Plan: Students placed blue boxes in each classroom and held a weekly contest. The Result: After one term, paper waste fell by 15 kilos a day. Caption under the photo: Students count the paper in the blue box.»"
GGREEN = "(greener = más verde; waste = desperdicio; threw away = botaba; kilos = kilos; placed = pusieron; contest = concurso; term = semestre; fell = bajó; caption = pie de foto)"
CLUB = "«Title: Chess Club Rules. Subtitle: Read before you play. Heading Time: Each player has ten minutes. Heading Respect: Shake hands before and after the game. Heading Silence: Do not talk while the game is on. Caption under the photo: Two members play in the library.»"
GCLUB = "(rules = reglas; shake hands = dar la mano; silence = silencio; while = mientras; members = socios)"
FAIR = "«Title: School Science Fair. Subtitle: Friday program. 9:00 Opening. 9:30 Robots. 10:30 Break. 11:00 Plants. 12:00 Prizes. Note: bring your project box. Entry is free.»"
GFAIR = "(fair = feria; program = programa; break = recreo; plants = plantas; prizes = premios; entry = entrada; free = gratis)"
CYCLE = "«Diagram: The Water Cycle. Label 1: The sun heats the water. Label 2: Water vapor rises. Label 3: Clouds form. Label 4: Rain falls. Caption: Water moves from the sea to the sky and back.»"
GCYCLE = "(cycle = ciclo; heats = calienta; vapor = vapor; rises = sube; clouds = nubes; form = se forman; falls = cae)"
TRAIL = "«Title: Trail Safety. Heading Water: Carry two liters of water per person. Heading Time: Start at 10:00 and be back by 16:00. Heading Group: Walk with an adult and stay together.»"
GTRAIL = "(trail = sendero; liters = litros; per person = por persona; back = de vuelta; stay together = quédense juntos)"
BOOKF = "«Title: Book Fair Week. Monday: Opening in the hall at 10:00. Wednesday: Author talk in the library at 15:30. Friday: Used-book sale in the yard at 12:00.»"
GBOOKF = "(book fair = feria del libro; hall = salón; author talk = charla con un autor; used-book sale = venta de libros usados; yard = patio)"
NIGHT = "«Title: Night Market. Subtitle: Food, crafts and music. Heading Where: Plaza Norte. Heading When: Saturdays, 18:00 to 22:00. Heading Rules: Bring a bag. Caption: A stall sells handmade candles.»"
GNIGHT = "(crafts = artesanías; square = plaza; bag = bolsa; stall = puesto; handmade = hecho a mano; candles = velas)"

lesson(
    OA, 2, MAT,
    "Aprenderé a leer rápido para captar la idea general y a leer de forma focalizada para encontrar un dato, usando el título, los subtítulos, los diagramas y los pies de foto. Sirve para encontrar información sin leer todo palabra por palabra.",
    ["Sé hacer predicciones con el título y las imágenes.", "Conozco los números y las horas en inglés."],
    [
        "Hay dos formas de leer con rapidez. La lectura rápida (skimming) consiste en recorrer el texto con la vista para captar la idea general: miras el título, el subtítulo, los encabezados y la primera oración de cada párrafo. La lectura focalizada (scanning) consiste en buscar un dato concreto, como un número, una hora o un nombre, saltándote lo demás. Para hacer scanning, primero decide qué palabra o número buscas.",
        "Los elementos organizacionales (organizational elements) del texto ayudan a ubicarte. El título (title) dice de qué trata. El subtítulo (subtitle) agrega información. Los encabezados (headings) separan las partes. Un diagrama (diagram) muestra un proceso con etiquetas (labels). El pie de foto (caption) es un texto breve junto a una imagen que la explica.",
        "Elige la estrategia según tu pregunta. Si preguntan de qué trata el texto, haz skimming con el título, el subtítulo y los encabezados. Si preguntan cuántos, cuándo o quién, haz scanning: busca la palabra clave o el número y lee solo la oración cercana. Siempre comprueba que el dato que encontraste responde exactamente a la pregunta.",
    ],
    [("skimming", "lectura rápida para captar la idea general"), ("scanning", "lectura focalizada para buscar un dato"), ("heading", "encabezado: título de una parte"), ("diagram", "diagrama"), ("label", "etiqueta de un diagrama"), ("caption", "pie de foto"), ("subtitle", "subtítulo")],
    [
        ("Scanning para un número", f"Texto: {GREEN} {GGREEN} ¿Cuántos kilos bajó el desperdicio de papel cada día?",
         ["Pregunta por una cantidad: busco un número cerca de fell.", "Hago scanning hasta The Result: paper waste fell by 15 kilos a day.", "El dato que responde es 15."], "15 kilos al día"),
        ("Skimming para la idea general", f"Texto: {GREEN} ¿De qué trata el texto, mirando solo el título, el subtítulo y los encabezados?",
         ["El título es A Greener School y el subtítulo habla de reducir el desperdicio de papel.", "Los encabezados son The Problem, The Plan y The Result.", "Entonces trata de cómo un curso redujo el papel que botaba el colegio."], "Cómo un curso redujo el desperdicio de papel del colegio"),
    ],
    [
        ("Leer todo el texto palabra por palabra para encontrar una hora.", "Es lento y no hace falta: el dato está en una oración.", "Haz scanning: busca el número o la palabra clave."),
        ("Responder con un número cercano, pero de otra pregunta.", "Se toma el primer número visto sin comprobar qué pregunta responde.", "Relee la pregunta y comprueba que tu dato calza."),
    ],
    [
        mc("La lectura rápida (skimming) sirve para", "captar la idea general del texto", ["buscar un número exacto", "aprender cada palabra"], "Se recorre el texto mirando título y encabezados."),
        mc("La lectura focalizada (scanning) sirve para", "buscar un dato concreto, como una hora o un número", ["entender la idea general sin mirar nada", "leer solo el título"], "Se busca una palabra o un número."),
        mc("Un pie de foto (caption) es", "un texto breve junto a una imagen que la explica", ["el título del libro", "una pregunta de examen"], "Caption va al lado de la foto o del dibujo."),
    ],
    [
        mc(f"Lee: {CLUB} {GCLUB} ¿Bajo qué encabezado está la regla de dar la mano?", "Respect", ["Time", "Silence"], "Shake hands está bajo Respect."),
        mc(f"Lee: {CLUB} {GCLUB} ¿Cuánto tiempo tiene cada jugador?", "Ten minutes", ["Two members", "Before and after"], "Bajo Time dice Each player has ten minutes."),
        mc(f"Lee: {CLUB} {GCLUB} ¿Dónde juegan los dos socios de la foto, según el pie de foto?", "In the library", ["In the yard", "In the classroom"], "El pie de foto dice Two members play in the library."),
    ],
    [
        mc(f"Lee: {FAIR} {GFAIR} ¿A qué hora son las plantas (Plants)?", "11:00", ["9:30", "12:00"], "Plants aparece junto a 11:00."),
        mc(f"Lee: {FAIR} {GFAIR} ¿Qué ocurre a las 12:00?", "Prizes", ["Robots", "Break"], "A las 12:00 se entregan los premios."),
        mc(f"Lee: {FAIR} {GFAIR} ¿Qué debes llevar?", "Your project box", ["A bag of plants", "Money for the entry"], "La nota dice bring your project box y la entrada es gratis."),
    ],
    [
        mc("Quieres saber a qué hora empieza una charla en un programa de feria. ¿Qué estrategia es más eficiente?", "Scanning: buscar la palabra charla y el número cercano", ["Skimming de todo el programa para la idea general", "Leer el título solamente"], "Necesitas un dato exacto, así que buscas ese dato."),
        mc(f"Lee: {CYCLE} {GCYCLE} ¿Qué pregunta NO se puede responder con el diagrama?", "How many liters of rain fall in a year?", ["What forms after vapor rises?", "What does the sun do?"], "El diagrama no trae cantidades de lluvia."),
    ],
    [
        arith(f"Lee: {TRAIL} {GTRAIL} Un grupo de 4 personas hace la caminata. ¿Cuántos litros de agua llevan en total, según el texto?", "4*2", "Cada persona lleva dos litros.", " litros"),
        arith(f"Lee: {TRAIL} Si el grupo parte a las 10:00 y vuelve a las 16:00, ¿cuántas horas dura la caminata?", "16-10", "Se resta la hora de salida a la de regreso.", " horas"),
    ],
    [mc(f"Recibes este afiche del colegio: {BOOKF} {GBOOKF} ¿Dónde y a qué hora es la charla con un autor?", "En la biblioteca, a las 15:30", ["En el salón, a las 10:00", "En el patio, a las 12:00"], "Author talk aparece el miércoles en la biblioteca.")],
    [
        mc("Para encontrar un número exacto en un texto, haces", "scanning", ["skimming"], "Scanning busca un dato concreto."),
        mc("Un diagrama muestra", "un proceso o una idea con etiquetas", ["solo un poema"], "Los labels explican las partes."),
        ("Escribe en inglés la palabra que significa «pie de foto».", "Caption", "Caption es el texto junto a una imagen."),
    ],
    task(f"Lee: {NIGHT} {GNIGHT} En tu hoja escribe: (1) la idea general en una oración (skimming), (2) el lugar, el horario y lo que se debe llevar (scanning), (3) dos elementos organizacionales que viste.",
         "(1) El texto presenta un mercado nocturno con comida, artesanías y música. (2) Plaza Norte; sábados de 18:00 a 22:00; hay que llevar una bolsa. (3) Título y encabezados (Where, When, Rules) o pie de foto.",
         ["la idea general no copia una sola línea del texto", "los tres datos son exactos", "nombra dos elementos organizacionales"],
         ["tres respuestas en la hoja"],
         ["confundir el horario con la regla", "olvidar un dato de los tres"],
         "Pide que explique qué estrategia usó para cada parte."),
    "Copia los siete términos del vocabulario y escribe un ejemplo de cada uno que veas en un libro de tu casa.",
    "Elige una página con título y subtítulo de un libro y escribe en español de qué crees que trata solo con skimming.",
)

# ============================================================ clase 3: inferencias y relectura
UMB = "«Marcos looked at the sky, took his umbrella and put on his rain jacket before leaving. His little sister laughed: You look like a duck!»"
GUMB = "(umbrella = paraguas; rain jacket = chaqueta de lluvia; leaving = salir; laughed = rio; duck = pato)"
ENV = "«Lola opened the envelope and read the first line. She froze. Then she laughed and hugged her sister. The letter said: Dear Lola, you won the school drawing contest!»"
GENV = "(envelope = sobre; froze = se quedó inmóvil; hugged = abrazó; won = ganaste; contest = concurso)"
REST = "«The restaurant was almost empty at lunch time. The waiter kept looking at the door and checking his watch. The cook came out of the kitchen with a tray of fresh bread, put it on a table and sighed.»"
GREST = "(restaurant = restaurante; waiter = garzón; checking = revisando; watch = reloj; cook = cocinero; tray = bandeja; sighed = suspiró)"
LIST = "«Gonzalo's hands were shaking. He read the list on the wall three times, then smiled and shouted: Yes! He ran to call his mother.»"
GLIST = "(shaking = temblando; list = lista; wall = muro; shouted = gritó; ran = corrió)"
SWIM = "«Camila's room was full of medals and photos of swimming pools. A towel was still wet on the chair.»"
GSWIM = "(medals = medallas; swimming pools = piscinas; towel = toalla; wet = mojada)"
FILM = "«Carlos was holding two tickets and checking the clock. His friend arrived and said, Sorry I am late. Carlos sighed: The movie started ten minutes ago.»"
GFILM = "(tickets = entradas; clock = reloj de pared; movie = película; started = empezó; ago = hace)"
GATE = "«Notice: the school bus will leave from the north gate today because the main gate is closed for repairs. Please bring your card.»"
GGATE = "(notice = aviso; gate = portón; closed = cerrado; repairs = reparaciones; card = tarjeta)"
KITCH = "«Julia walked into the kitchen. The oven was on, the table had flour on it, and her grandfather was wearing an apron. Julia smiled and said, It smells wonderful.»"
GKITCH = "(oven = horno; flour = harina; apron = delantal; smells = huele)"

lesson(
    OA, 3, MAT,
    "Aprenderé a hacer inferencias con pistas del texto y a releer para comprobar lo que entendí. Sirve para entender lo que el texto no dice con todas las letras.",
    ["Sé hacer scanning y skimming.", "Conozco palabras como because, probably y maybe."],
    [
        "Una inferencia (inference) es una idea que no está escrita, pero que se deduce con pistas del texto y con lo que ya sabes. Fórmula: pista del texto + conocimiento previo = inferencia. Por ejemplo, si Marcos lleva paraguas y chaqueta de lluvia, y sabes que la gente los usa cuando llueve, infieres que llueve o que va a llover. Una inferencia no se inventa: siempre debe tener evidencia.",
        "En inglés se expresa con palabras de probabilidad: probably (probablemente), maybe (quizás), must be (debe de ser), it seems that (parece que) y I think… because… (creo… porque…). Ejemplo: He is probably nervous because his hands are shaking. Usa probably cuando tengas buenas pistas, y evita decirlo como un hecho seguro si el texto no lo afirma.",
        "Relee (reread) cuando una parte no calza o cuando una primera lectura te dio una idea que quieres comprobar. Relee la oración que contiene la pista, y la anterior y la siguiente, para ver el contexto. También sirve para confirmar que una inferencia sigue valiendo hasta el final del texto.",
    ],
    [("inference", "inferencia: idea deducida con pistas"), ("clue", "pista"), ("probably", "probablemente"), ("maybe", "quizás"), ("must be", "debe de ser"), ("it seems that", "parece que"), ("reread", "releer")],
    [
        ("Hacer una inferencia con evidencia", f"Texto: {UMB} {GUMB} ¿Qué puedes inferir sobre el clima y cómo lo dices en inglés?",
         ["Pistas: mira al cielo, toma paraguas y chaqueta de lluvia.", "Conocimiento previo: la gente usa esas cosas cuando llueve.", "Inferencia: It is probably raining, because he took his umbrella."], "It is probably raining, because he took his umbrella (probablemente llueve)"),
        ("Releer para comprobar", f"Texto: {ENV} {GENV} En la primera lectura parece que Lola se asusta. ¿Por qué se ríe y se abraza con su hermana?",
         ["She froze se puede leer como susto.", "Releo hasta la última oración: la carta dice que ganó el concurso de dibujo.", "Entonces se quedó inmóvil por la sorpresa y se ríe de alegría."], "Porque ganó el concurso de dibujo"),
    ],
    [
        ("Decir como hecho seguro algo que el texto no dice, como «Lola is afraid of letters».", "Se salta la evidencia y se presenta una idea inventada como cierta.", "Usa probably y una pista del texto."),
        ("No releer cuando una parte contradice lo que entendí.", "Se mantiene una idea errada.", "Relee la oración con la pista y corrige tu idea."),
    ],
    [
        mc("Una inferencia (inference) es", "una idea que deduzco con pistas del texto y lo que ya sé", ["una frase copiada del texto", "un error de lectura"], "La inferencia no está escrita pero se apoya en evidencia."),
        mc("Relear (reread) sirve para", "comprobar o corregir lo que entendí", ["cambiar el final del texto", "saltarme las oraciones difíciles"], "Releer ayuda a comprender mejor."),
        mc("Probably significa", "probablemente", ["rápidamente", "nunca"], "Probably expresa una inferencia con buenas pistas."),
    ],
    [
        mc(f"Lee: {REST} {GREST} ¿Qué se puede inferir del restaurante?", "Probablemente han llegado pocos clientes", ["El restaurante está cerrado para siempre", "El cocinero está enojado con el garzón"], "Está casi vacío, el garzón mira la puerta y el cocinero suspira."),
        mc(f"Lee: {REST} {GREST} ¿Qué pista apoya mejor la inferencia de que hay pocos clientes?", "The restaurant was almost empty at lunch time", ["The cook came out of the kitchen", "The tray had fresh bread"], "Casi vacío a la hora del almuerzo es la pista más directa."),
        mc(f"Lee: {REST} {GREST} ¿Qué oración expresa la inferencia con evidencia?", "The restaurant is probably quiet today, because it is almost empty", ["The restaurant is a big building", "The cook is always sad"], "Une probably con la pista del texto."),
    ],
    [
        mc(f"Lee: {LIST} {GLIST} ¿Cuál es la mejor inferencia?", "Su nombre aparece en la lista", ["Perdió su teléfono", "Su mamá está enojada"], "Sonríe y grita Yes! después de leer la lista."),
        mc(f"Lee: {LIST} {GLIST} ¿Qué pista muestra que Gonzalo estaba nervioso antes de leer?", "His hands were shaking", ["He ran to call his mother", "He read the list on the wall"], "Las manos temblando son una pista de nervios."),
        mc(f"Lee: {LIST} {GLIST} ¿Qué crees que hará después? Elige la inferencia más razonable.", "Probablemente contará la noticia a su familia", ["Probablemente romperá la lista", "Probablemente se irá al cine"], "Corre a llamar a su mamá."),
    ],
    [
        mc(f"Lee: {SWIM} {GSWIM} ¿Cuál inferencia tiene mejor apoyo?", "Camila probablemente nada, porque hay medallas y fotos de piscinas", ["Camila odia el agua", "Camila es profesora"], "Las medallas y las piscinas apoyan la idea de que nada."),
        mc(f"Dos lectores leen: {SWIM} Lector 1: «Camila probably swam today, because the towel is still wet.» Lector 2: «Camila swam last week.» ¿Quién tiene mejor apoyo?", "El lector 1, porque una toalla todavía mojada indica algo reciente", ["El lector 2, porque hay medallas", "Ninguno, porque el texto no lo dice"], "Una toalla mojada se seca con rapidez, así que lo ocurrido es reciente."),
    ],
    [
        mc(f"Lee: {FILM} {GFILM} ¿Qué se puede inferir?", "Probablemente ya se perdieron el comienzo de la película", ["La película ya terminó", "Carlos está enojado con las entradas"], "La película empezó hace diez minutos y recién llegó el amigo."),
        mc(f"En el texto {REST} alguien infiere que el cocinero está triste porque el restaurante está vacío. ¿Por qué esa inferencia es más débil que «hay pocos clientes»?", "Porque el texto solo dice que suspiró, no por qué", ["Porque los cocineros nunca se ponen tristes", "Porque suspirar es algo alegre"], "El texto no explica el motivo del suspiro."),
    ],
    [mc(f"Ves este aviso en el colegio: {GATE} {GGATE} ¿Qué debes inferir que harás hoy?", "Esperar el bus en el portón norte", ["Esperar en el portón principal", "Quedarte en casa"], "El portón principal está cerrado por reparaciones.")],
    [
        mc("¿Cuál de estas palabras expresa que estás deduciendo algo con buenas pistas?", "Probably", ["Never"], "Probably expresa probabilidad."),
        mc("¿Qué se une para hacer una inferencia?", "Una pista del texto y un conocimiento previo", ["Dos adivinanzas"], "Sin pista no hay inferencia."),
        ("Escribe en inglés la palabra que significa «releer».", "Reread", "Reread es leer otra vez para comprobar."),
    ],
    task(f"Lee: {KITCH} {GKITCH} En tu hoja escribe dos inferencias en inglés con probably y because. Cada una debe nombrar una pista distinta.",
         "Her grandfather is probably baking, because the oven is on and there is flour on the table. Julia probably likes the smell, because she smiles and says it smells wonderful.",
         ["usa probably y because", "cada inferencia tiene una pista diferente del texto", "no afirma algo que el texto contradice"],
         ["dos oraciones completas en la hoja"],
         ["inferir sin pista", "repetir la misma pista en las dos oraciones"],
         "Pide que subraye en el texto la pista de cada oración."),
    "Copia las siete palabras del vocabulario y escribe una oración en español con cada una.",
    "Observa a una persona de tu casa de lejos, sin hablar, y escribe una inferencia con probably sobre lo que está haciendo.",
)

# ============================================================ clase 4: poslectura con brecha de información
SGAR_A = "«Card A: The school garden opened in March. It has 12 beds of vegetables.»"
SGAR_B = "«Card B: Students sell tomatoes every Friday. The money buys new tools.»"
GSGAR = "(garden = huerta; beds = camas de cultivo; vegetables = verduras; sell = venden; tools = herramientas)"
PURR = "«Title: Why Do Cats Purr? ... Cats purr when they feel calm, but they can also purr when they are scared or in pain, as a way to calm themselves.»"
GPURR = "(purr = ronronear; calm = tranquilo; scared = asustado; pain = dolor; calm themselves = calmarse a sí mismos)"
LANE_A = "«Card A: The council built a bike lane on Avenida Central last month. It is 2 kilometers long and has green paint so drivers can see it.»"
LANE_B = "«Card B: Many students now ride to school. The lane is safe and quiet. Next year the council wants to add a second lane near the park.»"
GLANE = "(council = municipalidad; bike lane = ciclovía; paint = pintura; drivers = conductores; ride = andar en bicicleta; add = agregar)"
RAD_A = "«Card A: The school radio starts on Monday. It will broadcast at 13:00 for fifteen minutes.»"
RAD_B = "«Card B: Students from every grade present news and music. The first topic is the recycling contest.»"
GRAD = "(broadcast = transmitir; present = presentar; news = noticias; grade = curso; topic = tema; recycling = reciclaje)"
PLAY_A = "«Card A: A new playground opened in Villa Verde. It has two slides and a climbing wall.»"
PLAY_B = "«Card B: Parents and teachers built it in six weekends. It is open every day until sunset.»"
GPLAY = "(playground = plaza de juegos; slides = toboganes; climbing wall = muro de escalada; built = construyeron; weekends = fines de semana; sunset = puesta de sol)"

lesson(
    OA, 4, MAT,
    "Aprenderé a completar un organizador gráfico con dos tarjetas distintas, a recontar y resumir, y a preguntar para confirmar datos. Sirve para estudiar un texto después de leerlo y trabajar en pareja.",
    ["Sé hacer predicciones, scanning y skimming.", "Conozco las preguntas what, where, who y when."],
    [
        "Después de leer (post-reading) se revisa lo que se entendió. Primero se confirman las predicciones (confirm predictions): compara lo que pensabas con lo que dijo el texto. Si coincide, dices The prediction was confirmed. Si no coincide, lo corriges: The text says something different. A veces la predicción se confirma solo en parte.",
        "Un organizador gráfico (graphic organizer) ordena la información en una tabla, un mapa o un esquema. Una tabla simple tiene columnas como What?, Where?, When? y Who? Recontar (retell) es contar con tus propias palabras lo importante en orden; resumir (summarize) es decir solo las ideas principales en pocas oraciones, sin copiar el texto entero ni agregar datos nuevos.",
        "Con una brecha de información, cada compañero tiene una tarjeta (card). Para confirmar un dato, pregunta: Did you say that…? (¿dijiste que…?) o Can you repeat the number, please? (¿puedes repetir el número?). Para completar lo que falta, usa preguntas con what, where, when y who. Si un dato aparece distinto en las dos tarjetas, vuelve a leer y pregunta; no lo elijas al azar.",
    ],
    [("confirm a prediction", "confirmar una predicción"), ("graphic organizer", "organizador gráfico: tabla o esquema"), ("retell", "recontar con mis palabras"), ("summarize", "resumir: ideas principales, pocas oraciones"), ("Did you say that…?", "¿dijiste que…?"), ("card", "tarjeta"), ("partner", "compañero")],
    [
        ("Completar un organizador con dos tarjetas", f"Tarjetas: {SGAR_A} {SGAR_B} {GSGAR} Completa: What? When? How many beds? What do they do with the money?",
         ["La tarjeta A dice qué es y cuándo abrió: una huerta escolar, en marzo, con 12 camas.", "La tarjeta B dice qué hacen: venden tomates los viernes y compran herramientas.", "Se juntan los datos de las dos tarjetas en las cuatro columnas."], "What: school garden. When: March. How many beds: 12. Money: buys new tools"),
        ("Confirmar una predicción", f"Predicción: «The text will say cats purr only when they are happy.» Texto: {PURR} {GPURR} ¿Se confirmó la predicción?",
         ["El texto dice que ronronean cuando están tranquilos.", "Pero también dice que pueden ronronear cuando están asustados o con dolor.", "La predicción se confirma solo en parte y hay que corregirla."], "Se confirmó solo en parte: también ronronean asustados o con dolor"),
    ],
    [
        ("Copiar casi todo el texto y llamarlo resumen.", "Un resumen debe ser corto y decir solo las ideas principales.", "Escribe una o dos oraciones con lo más importante."),
        ("Agregar a un resumen un dato que no está en las tarjetas.", "Se inventa información que nadie dijo.", "Usa solo lo que dicen las tarjetas o pregunta."),
    ],
    [
        mc("Un organizador gráfico (graphic organizer) sirve para", "ordenar la información en una tabla o esquema", ["decorar el cuaderno", "traducir cada palabra"], "Ordena los datos para estudiarlos."),
        mc("Resumir (summarize) es", "decir las ideas principales en pocas oraciones", ["copiar el texto completo", "leer más rápido"], "El resumen es corto y fiel al texto."),
        mc("Did you say that…? sirve para", "confirmar un dato con tu compañero", ["despedirte", "pedir permiso"], "Es una pregunta para confirmar."),
    ],
    [
        mc(f"Lee las tarjetas: {LANE_A} {LANE_B} {GLANE} ¿Dónde está la ciclovía?", "On Avenida Central", ["Near the park", "In the school"], "La tarjeta A da el lugar."),
        mc(f"Lee las tarjetas: {LANE_A} {LANE_B} {GLANE} ¿Qué largo tiene la ciclovía?", "2 kilometers", ["1 kilometer", "A second lane"], "Está en la tarjeta A."),
        mc(f"Lee las tarjetas: {LANE_A} {LANE_B} {GLANE} Tu compañero tiene la otra tarjeta. ¿Qué pregunta le haces para saber qué planea la municipalidad?", "What does the council want to do next year?", ["How long is the lane?", "Where is Avenida Central?"], "Ese dato está solo en la tarjeta B."),
    ],
    [
        mc(f"Lee las tarjetas: {RAD_A} {RAD_B} {GRAD} ¿Cuántos minutos dura cada transmisión?", "Fifteen minutes", ["Thirteen minutes", "Five minutes"], "La tarjeta A dice for fifteen minutes."),
        mc(f"Lee las tarjetas: {RAD_A} {RAD_B} {GRAD} ¿Quiénes presentan las noticias y la música?", "Students from every grade", ["Teachers from the school", "Parents from the council"], "La tarjeta B dice Students from every grade."),
        mc(f"Lee las tarjetas: {RAD_A} {RAD_B} {GRAD} ¿Cuál es el primer tema?", "The recycling contest", ["The music contest", "The soccer game"], "La tarjeta B lo nombra."),
    ],
    [
        mc(f"Compara dos resúmenes de las tarjetas: {LANE_A} {LANE_B} Resumen 1: copia todas las oraciones completas. Resumen 2: «The council built a green 2-kilometer bike lane on Avenida Central; students use it and a second lane is planned.» ¿Cuál es mejor resumen?", "El 2, porque es corto y conserva las ideas principales", ["El 1, porque tiene todas las palabras", "Ninguno, porque falta el nombre del alcalde"], "Un resumen es breve y fiel; el nombre del alcalde no está en las tarjetas."),
        mc(f"Predijiste que el texto diría que la ciclovía es peligrosa. Lees: {LANE_A} {LANE_B} ¿Qué pasó con tu predicción?", "No se confirmó, porque la tarjeta B dice que es segura y tranquila", ["Se confirmó, porque hay conductores", "Se confirmó, porque es verde"], "El texto dice lo contrario de la predicción."),
    ],
    [
        mc("Tu tarjeta dice que son 2 kilómetros y tu compañero dice «3 kilómetros». ¿Qué haces?", "Releo, pregunto Can you repeat the number, please? y comparo con la tarjeta", ["Elijo el número que me gusta", "Escribo 5 para promediar"], "Una contradicción se resuelve volviendo a la fuente."),
        mc(f"Solo tienes la tarjeta B: {LANE_B} ¿Qué pregunta te sirve para saber la longitud de la ciclovía?", "How long is the lane?", ["Who rides to school?", "When will the second lane be built?"], "El largo está en la tarjeta que tu compañero tiene."),
    ],
    [mc("Tu compañero te lee: «The museum opens at ten on Saturdays and the guided tour starts at eleven.» Tú anotaste que el tour parte a las doce. ¿Qué frase usas para confirmar?", "Did you say the tour starts at eleven?", ["Where is the museum?", "I like Saturdays."], "Le preguntas directamente por el dato que dudas.")],
    [
        mc("Después de leer, ¿qué se hace con una predicción?", "Se compara con lo que dijo el texto", ["Se olvida"], "Así se confirma o se corrige."),
        mc("Recontar (retell) es", "contar con mis palabras lo importante en orden", ["copiar el título"], "Se cuenta en el mismo orden del texto."),
        ("Escribe en inglés la palabra que significa «tarjeta».", "Card", "Card es la tarjeta con la parte del texto."),
    ],
    task(f"Con tu compañero(a) o con una persona de tu casa, lean las dos tarjetas: {PLAY_A} {PLAY_B} {GPLAY} En tu hoja haz: (1) un organizador con What?, Where?, Who built it? y When is it open?; (2) un resumen de dos oraciones; (3) una pregunta en inglés para confirmar un dato.",
         "(1) What: a playground with two slides and a climbing wall. Where: Villa Verde. Who built it: parents and teachers in six weekends. When is it open: every day until sunset. (2) A new playground opened in Villa Verde. Parents and teachers built it in six weekends. (3) Did you say it is open until sunset?",
         ["el organizador usa datos de las dos tarjetas", "el resumen tiene dos oraciones y no agrega datos", "la pregunta es correcta en inglés"],
         ["organizador, resumen y pregunta escritos en la hoja"],
         ["agregar datos que no están en las tarjetas", "hacer un resumen más largo que el texto"],
         "Pide que marque en cada tarjeta lo que usó en cada columna."),
    "Copia las siete frases del vocabulario y escribe su traducción debajo.",
    "Haz un organizador de cuatro columnas sobre una noticia que hayas escuchado esta semana.",
)

# ============================================================ clase 5: lectura independiente completa
LIBW = "«Title: A Library on Wheels. Subtitle: How an old bus brings books to the hills. Paragraph 1: In the hills above Coquimbo, many families live far from a library. Mr. Soto, a retired teacher, turned an old bus into a mobile library. Paragraph 2: Every Saturday the bus visits six villages. Children borrow up to three books and return them the next week. Paragraph 3: At first only ten children came. Now eighty visit each week, and volunteers read stories aloud. (Texto de ejemplo.)»"
GLIBW = "(wheels = ruedas; hills = cerros; retired = jubilado; mobile = móvil; villages = aldeas; borrow = pedir prestado; return = devolver; volunteers = voluntarios; aloud = en voz alta)"
MUR = "«Title: Murals of Valparaíso. Subtitle: Art on the hills. Paragraph 1: Many walls on the hills of Valparaíso are covered with colorful murals. Paragraph 2: Local artists paint them with the permission of the owners. Some murals show the sea; others show faces of neighbors. Paragraph 3: Visitors can follow a map and walk the mural route in about two hours. (Texto de ejemplo.)»"
GMUR = "(murals = murales; covered = cubiertas; colorful = coloridos; local = de la zona; permission = permiso; owners = dueños; route = ruta; map = mapa)"

lesson(
    OA, 5, MAT,
    "Aprenderé a usar todas las estrategias en un solo texto: predecir, leer rápido y focalizado, inferir, recontar, resumir y preguntar. Sirve para leer un artículo completo por mi cuenta.",
    ["Sé predecir, hacer skimming y scanning, inferir y completar un organizador."],
    [
        "Para leer un artículo por tu cuenta, combina las estrategias en tres momentos. Antes: mira el título, el subtítulo y la imagen, decide tu propósito y haz una predicción con una pista. Durante: haz skimming para la idea general, scanning para datos exactos y relee lo que no entiendas. Después: confirma tu predicción, completa un organizador, y recuenta o resume lo más importante.",
        "Recuerda que un resumen conserva las ideas principales y no agrega información que no está en el texto. Una buena pregunta para confirmar empieza con what, who, where, when o how many y se puede responder con el texto. Si el texto no da la respuesta, di que no está escrito.",
        "Cuando termines, comprueba tu trabajo: ¿mi predicción tuvo una pista?, ¿mis datos están en el texto?, ¿mi resumen es breve?, ¿mis inferencias llevan probably y una evidencia? Eso te permite leer cada texto con más seguridad.",
    ],
    [("pre-reading", "antes de leer"), ("during reading", "mientras se lee"), ("post-reading", "después de leer"), ("main idea", "idea principal"), ("summary", "resumen"), ("question", "pregunta")],
    [
        ("Antes, durante y después", f"Texto: {LIBW} {GLIBW} Antes de leer ves solo el título y el subtítulo. ¿Qué predicción es razonable y qué dato obtienes con scanning sobre las aldeas?",
         ["Título y subtítulo: A Library on Wheels, un bus viejo lleva libros a los cerros.", "Predicción: el texto contará cómo un bus lleva libros a lugares lejanos.", "Scanning del párrafo 2: visits six villages, así que son seis aldeas."], "Predicción: un bus lleva libros a lugares lejanos. Aldeas: seis"),
        ("Resumir con ideas principales", f"Texto: {LIBW} Elige la idea central de los tres párrafos y resúmela en una oración.",
         ["El párrafo 1 presenta a Mr. Soto y su biblioteca móvil.", "El párrafo 2 dice cuándo visita las aldeas y cuántos libros prestan.", "Una oración: Mr. Soto turned an old bus into a library that visits six villages and now serves many children."], "Un jubilado convirtió un bus en una biblioteca móvil que visita seis aldeas y sirve a muchos niños"),
    ],
    [
        ("Hacer una predicción solo después de leer.", "Una predicción se hace antes, con el título y las imágenes.", "Antes de leer, mira título, subtítulo e imagen."),
        ("Resumir con un dato que no está en el texto.", "Se agrega información inventada.", "Comprueba cada dato del resumen en el texto."),
    ],
    [
        mc("Ves solo esto: «Title: A Library on Wheels. Subtitle: How an old bus brings books to the hills.» (wheels = ruedas; hills = cerros) ¿Qué predicción tiene apoyo?", "Un bus trae libros a lugares lejanos", ["Una receta de pan", "Un partido de fútbol"], "Wheels y bus son pistas."),
        mc(f"Lee: {LIBW} {GLIBW} ¿Quién convirtió el bus en biblioteca?", "Mr. Soto, a retired teacher", ["A volunteer", "A child from the hills"], "Aparece en el párrafo 1."),
        mc(f"Lee: {LIBW} {GLIBW} ¿Cuántos libros como máximo pueden pedir prestados los niños?", "Three", ["Six", "Eighty"], "Dice up to three books."),
    ],
    [
        mc(f"Haz skimming sobre {LIBW} ¿Cuál es la idea principal?", "Un bus lleva libros a familias que viven lejos de una biblioteca", ["Las aldeas tienen seis escuelas", "Un profesor compró libros nuevos"], "El título y el párrafo 1 dan el tema."),
        mc(f"Lee: {LIBW} {GLIBW} ¿Cuántos niños visitan el bus cada semana ahora?", "Eighty", ["Ten", "Three"], "El párrafo 3 compara ten al inicio con eighty ahora."),
        mc(f"Lee: {LIBW} {GLIBW} ¿Cuándo visita el bus las aldeas?", "Every Saturday", ["Every Monday", "Every day"], "Está en el párrafo 2."),
    ],
    [
        mc(f"Lee: {LIBW} {GLIBW} ¿Qué inferencia tiene mejor apoyo sobre por qué aumentó el número de niños?", "Probablemente el servicio es útil y los niños lo disfrutan", ["El bus se hizo más grande", "Hay menos aldeas"], "Subió de diez a ochenta y hay voluntarios que leen cuentos."),
        mc(f"Un compañero resume {LIBW} así: «Mr. Soto has a restaurant in Coquimbo.» ¿Qué corrección haces?", "Mr. Soto es un profesor jubilado que tiene una biblioteca móvil", ["Está bien, porque Coquimbo es una ciudad", "Mr. Soto vive en Valparaíso"], "El restaurante no aparece en el texto."),
        mc(f"Lee: {LIBW} {GLIBW} ¿Qué ocurrió primero, según el párrafo 3?", "Al comienzo llegaron solo diez niños", ["Ahora ochenta niños visitan el bus cada semana", "Los voluntarios leen cuentos en voz alta"], "El párrafo 3 usa At first para el comienzo (diez niños) y Now para lo de hoy (ochenta niños)."),
    ],
    [
        arith(f"Lee: {LIBW} Si ahora son 80 niños por semana y al comienzo eran 10, ¿cuántos niños más llegan ahora?", "80-10", "Se resta la cantidad inicial a la actual.", " niños"),
        mc(f"Predijiste que el texto diría que la biblioteca móvil cierra por falta de niños. Lees {LIBW} ¿Qué pasó con tu predicción?", "No se confirmó, porque cada vez van más niños", ["Se confirmó, porque al inicio fueron pocos", "Se confirmó, porque el bus es viejo"], "El texto cuenta que el número creció."),
    ],
    [
        mc(f"Dos resúmenes de {LIBW} Resumen 1: «A retired teacher made a mobile library that visits six villages every Saturday.» Resumen 2: «A bus visits villages and children can borrow thirty books each.» ¿Cuál es mejor?", "El 1, porque todos sus datos están en el texto", ["El 2, porque tiene más cifras", "Los dos son iguales de buenos"], "El resumen 2 inventa treinta libros; el texto dice up to three."),
        mc(f"Lee: {LIBW} Un lector dice: «The text does not say what the bus looks like.» ¿Es correcto?", "Sí, el texto solo dice que es an old bus, sin más detalles", ["No, el texto dice que es amarillo", "No, el texto trae una foto con todos los colores"], "Old bus es todo lo que se dice del bus."),
    ],
    [mc(f"En tu curso te piden preguntar algo que se pueda contestar con el texto {LIBW} ¿Cuál es una buena pregunta?", "How many villages does the bus visit?", ["What is Mr. Soto's favorite color?", "Why is the bus yellow?"], "La respuesta, six, está escrita en el texto.")],
    [
        mc("¿Qué pasa con un resumen que incluye un dato que no está en el texto?", "Es incorrecto, porque agrega información inventada", ["Es correcto si suena bien"], "Un resumen debe ser fiel."),
        mc("¿Cuál es el orden correcto de las fases de lectura?", "Antes, durante y después de leer", ["Después, antes y durante"], "Pre-reading, during reading y post-reading."),
        ("Escribe en inglés «idea principal».", "Main idea", "Main idea es lo más importante del texto."),
    ],
    task(f"Lee este texto y trabaja solo: {MUR} {GMUR} En tu hoja escribe: (1) una predicción hecha solo con el título y el subtítulo, (2) un dato con scanning sobre la duración de la ruta, (3) un resumen de una oración, (4) una pregunta en inglés que se pueda contestar con el texto.",
         "(1) I think the text will explain how paintings decorate the hills of Valparaíso. (2) The mural route takes about two hours. (3) Local artists paint colorful murals on the hills of Valparaíso, and visitors can walk a route to see them. (4) How long is the mural route?",
         ["la predicción usa el título y el subtítulo", "el dato es exacto", "el resumen es breve y fiel", "la pregunta se contesta con el texto"],
         ["cuatro respuestas en la hoja"],
         ["agregar datos que no están en el texto", "hacer una pregunta que el texto no responde"],
         "Pide que subraye en el texto dónde está la respuesta de su pregunta."),
    "Copia las seis palabras del vocabulario y escribe una acción de lectura para cada una.",
    "Lee un artículo breve de un diario con una persona de tu casa y usa las tres fases: antes, durante y después.",
)
