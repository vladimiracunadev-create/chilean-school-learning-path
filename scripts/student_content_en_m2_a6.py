"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 06: estrategias para apoyar la comprensión de textos leídos.

Textos originales y ficticios, con pista en español; todo texto al que se refiere una pregunta está escrito en el enunciado.
Los títulos de clase del plan son genéricos; aquí cada clase trabaja un grupo de estrategias del OA: antes de leer (propósito,
conocimientos previos, predicción); durante la lectura (lectura rápida y focalizada, elementos del texto); inferir, releer y
plantearse preguntas; después de leer (organizadores gráficos, responder); y recontar, resumir y confirmar información.
"""
from __future__ import annotations

from en_m2_a_common import MAT_READ, arith, lesson, task

OA = "EN2M OA 06"

# ================================================== clase 1: antes de leer
ART1 = "«Electric Scooters in Our City\nSubtitle: Fast, quiet and fun, but are they safe?\nIn the last year, electric scooters have become popular in many cities. People use them to go to school, to work or to a friend’s house. They are cheap and easy to rent with a phone. However, accidents have increased, because some riders do not wear helmets and many use the pavement. Experts suggest special lanes, a speed limit and compulsory helmets.»\n(scooters = monopatines, popular = populares, rent = arrendar, accidents = accidentes, riders = conductores, helmets = cascos, pavement = vereda, experts = expertos, lanes = pistas, speed limit = límite de velocidad, compulsory = obligatorio)"
HEAD2 = "Título de un artículo: «Why Do We Yawn?» Subtítulo: «Science still has no final answer.» Una imagen muestra a tres personas bostezando en una sala. (yawn = bostezar, answer = respuesta)"

lesson(
    OA, 1, MAT_READ,
    "Aprenderé a prepararme antes de leer: decidir un propósito, usar lo que ya sé del tema y predecir el contenido con el título, los subtítulos y las imágenes. Sirve para leer con más atención y comprender más rápido un texto en inglés.",
    ["Sé reconocer el título y el subtítulo de un texto.", "Sé que hay textos para informar, opinar o dar instrucciones."],
    [
        "Antes de leer (pre-reading), haz tres cosas. Primero, decide tu propósito (purpose): ¿buscas una idea general, un dato exacto o una opinión? Segundo, activa tus conocimientos previos (prior knowledge): ¿qué sabes ya del tema? Tercero, haz una predicción (prediction) con el título, el subtítulo y las imágenes: ¿de qué hablará el texto? ¿qué palabras aparecerán?",
        "El título (title) dice el tema; el subtítulo (subtitle) agrega una idea o una pregunta; las imágenes y los diagramas muestran información visual. Por ejemplo, el título Electric Scooters in Our City y el subtítulo Fast, quiet and fun, but are they safe? permiten predecir que el texto hablará de ventajas y de seguridad. Si el texto tiene una pregunta, es probable que la respuesta aparezca en alguna parte.",
        "Las predicciones se confirman o se corrigen durante la lectura. Una predicción incorrecta no es un error: es una pista de que el texto trae información nueva. Antes de leer, escribe dos palabras que esperas encontrar y una pregunta que quieres responder. Así tu lectura tendrá una meta clara y recordarás más.",
    ],
    [("pre-reading", "antes de leer"), ("purpose", "propósito: para qué leo"), ("prior knowledge", "conocimientos previos"), ("prediction", "predicción: idea de lo que leeré"), ("title", "título"), ("subtitle", "subtítulo")],
    [
        ("Predecir con un título", "Un artículo se llama «A Day at the Zoo». ¿Qué palabra esperas encontrar? A) animals B) engines", ["El título habla de un zoológico.", "Un zoológico tiene animales.", "Animals."], "A) animals"),
        ("Elegir un propósito", "Quieres saber a qué hora abre un museo. ¿Qué tipo de lectura necesitas? A) buscar una hora exacta B) leer una opinión", ["Mi propósito es un dato exacto.", "Busco una hora.", "Es buscar un dato exacto."], "A"),
    ],
    [
        ("Empezar a leer sin mirar el título.", "Se pierde el tema y las pistas del texto.", "Lee siempre el título y el subtítulo primero."),
        ("Sentir que la predicción debe ser perfecta.", "Una predicción solo prepara la lectura.", "Compárala con el texto y corrígela si hace falta."),
    ],
    [
        ("Lee: " + ART1 + " ¿Cuál es el título del artículo? A) Electric Scooters in Our City B) Safe Streets", "A", "El título está en la primera línea del texto."),
        ("Lee: " + ART1 + " ¿Qué se pregunta en el subtítulo? A) si los monopatines son seguros B) si son baratos", "A", "El subtítulo dice but are they safe?"),
        ("Lee: " + HEAD2 + " ¿Sobre qué tema se predice que habla el artículo? A) los bostezos B) los viajes", "A", "El título dice Why Do We Yawn?"),
    ],
    [
        ("Lee: " + HEAD2 + " ¿Qué predicción es razonable por el subtítulo? A) que el texto explicará algunas ideas, pero sin una respuesta final B) que dará una receta", "A", "El subtítulo dice Science still has no final answer."),
        ("Lee: " + ART1 + " Antes de leer, tu propósito es saber qué recomiendan los expertos. ¿Qué buscarás? A) experts suggest B) rent with a phone", "A", "Experts suggest introduce las recomendaciones."),
        ("Lee: " + HEAD2 + " ¿Qué conocimiento previo te ayuda a predecir? A) saber que las personas bostezan cuando tienen sueño B) saber cómo se fabrica una cama", "A", "Es un conocimiento relacionado con el tema."),
    ],
    [
        ("Lee: " + ART1 + " ¿Para qué usan los monopatines las personas, según el texto? Elige: A) ir al colegio, al trabajo o a casa de un amigo B) practicar un deporte olímpico", "A", "Dice to go to school, to work or to a friend’s house."),
        ("Lee: " + ART1 + " ¿Qué predijiste con la palabra safe? A) que habría información de seguridad B) que habría una receta", "A", "Safe es una palabra clave y el texto habla de cascos y pistas."),
        ("Lee: «Title: Zoo Visit Rules. Subtitle: Please read before entering.» ¿Qué tipo de texto se predice? A) normas de visita B) un cuento de aventuras", "A", "Rules y Please read indican un texto de normas."),
    ],
    [
        ("Lee: " + ART1 + " La predicción de Pau era que el texto solo hablaría de ventajas. ¿Qué dato la corrige? A) los accidentes han aumentado B) los monopatines son rápidos", "A", "El texto presenta un problema: However, accidents have increased."),
        ("Lee: " + HEAD2 + " Un compañero predice que el artículo dará una respuesta definitiva. ¿Qué pista del texto lo contradice? A) el subtítulo dice que la ciencia aún no tiene una respuesta final B) hay tres personas en la imagen", "A", "El subtítulo anuncia que no hay respuesta definitiva."),
    ],
    [
        ("Ordena los pasos de la rutina antes de leer: a) hacer una predicción con el título b) decidir un propósito c) pensar en lo que ya sé", "b, c, a", "Primero el propósito, luego los conocimientos previos y por último la predicción."),
        ("Lee: " + ART1 + " Un título nuevo dice «Rules for Scooters». ¿Cuál de estas predicciones es más precisa? A) hablará de helmets y speed limit B) hablará de la historia de la bicicleta", "A", "Rules y scooters apuntan a normas de uso."),
    ],
    [("Lee: «Title: A Weekend at the Mountains. Subtitle: Three days, two routes, one tent.» (routes = rutas, tent = carpa). ¿Cuántas rutas hará el viaje?", "Dos", "El subtítulo dice two routes.")],
    [
        ("¿Qué haces antes de leer un texto (en Inglés, 2.º medio)?", "Decido un propósito y hago una predicción", "Así leo con una meta."),
        ("¿Qué aporta el subtítulo?", "Una idea o pregunta adicional sobre el tema", "Complementa el título."),
        ("¿Qué haces si tu predicción no coincide con el texto (en Inglés, 2.º medio)?", "La corrijo", "El texto trae información nueva."),
    ],
    task("Lee estos datos de un artículo ficticio: «Title: The Quiet Library Hour. Subtitle: A new rule for the reading room. Picture: students with headphones reading at long tables.» (headphones = audífonos, reading room = sala de lectura). En tu hoja escribe: tu propósito de lectura, un conocimiento previo, dos palabras que esperas encontrar y una pregunta que quieres responder.", "Propósito: saber qué regla nueva hay. Conocimiento previo: las bibliotecas piden silencio. Palabras: silence, rule, noise. Pregunta: ¿cuándo es la hora de silencio?", ["dice un propósito claro", "usa un conocimiento relacionado con el tema", "escribe dos palabras posibles y una pregunta"], ["hoja con cuatro respuestas"], ["escribir palabras sin relación con el título", "escribir una pregunta que ya está respondida"], "Guarda tu hoja y, si algún día lees el artículo, compara tus predicciones con el texto."),
    "Antes de leer un artículo de noticias, escribe en tu cuaderno tu propósito y tres palabras que esperas ver.",
    "Elige un título de revista que conozcas y escribe una predicción de cuatro líneas con apoyo del subtítulo.",
)

# ================================================== clase 2: lectura rápida y focalizada, elementos del texto
SCHEDULE = "Cartelera de ejemplo de un centro cultural:\nTitle: Spring Workshops\nMonday 5:00 p.m. – Painting (Room 1)\nTuesday 4:30 p.m. – Theatre (Room 3)\nWednesday 6:00 p.m. – Photography (Room 2)\nThursday 5:30 p.m. – Music (Room 4)\nFriday 4:00 p.m. – Dance (Room 1)\nNote: Bring your own materials. Free for students."
GUIDE = "«How to Make a Paper Kite\nWhat you need: paper, two wooden sticks, string, tape.\nStep 1: Cross the sticks in the form of a plus sign and tie them with string.\nStep 2: Place the frame on the paper and draw its shape.\nStep 3: Cut the shape and fold the edges over the sticks.\nStep 4: Tie a long string to the centre and fly it in an open space.»\n(kite = volantín, wooden sticks = varillas de madera, tape = cinta, cross = cruzar, frame = armazón, edges = bordes, open space = espacio abierto)"
DIAG = "Diagrama de ejemplo: «Parts of a bicycle: 1 handlebars, 2 saddle, 3 frame, 4 wheel, 5 pedal, 6 chain.» (handlebars = manubrio, saddle = asiento, chain = cadena)"

lesson(
    OA, 2, MAT_READ,
    "Aprenderé a hacer una lectura rápida (skimming) y una lectura focalizada (scanning) y a usar los elementos organizacionales del texto: título, subtítulo, listas y diagramas. Sirve para encontrar rápidamente la idea general o un dato exacto.",
    ["Sé predecir el contenido con el título.", "Sé los días de la semana y las horas."],
    [
        "La lectura rápida (skimming) sirve para captar la idea general: lees el título, el subtítulo y la primera frase de cada párrafo, sin detenerte en cada palabra. La lectura focalizada (scanning) sirve para encontrar un dato exacto: miras el texto buscando una palabra clave, un número o un nombre, y te detienes solo cuando lo encuentras. Skimming responde de qué trata; scanning responde cuándo, dónde, cuánto o quién.",
        "Los elementos organizacionales (organisational features) te ayudan a moverte. El título dice el tema; los subtítulos separan las partes; las listas ordenan datos; los números indican pasos (Step 1, Step 2); las negritas destacan ideas; y los diagramas (diagrams) muestran las partes de un objeto con nombres o números. Si buscas un horario, mira primero la tabla o la cartelera.",
        "Una buena estrategia es elegir antes de leer: ¿necesito la idea general o un dato exacto? Si necesitas la idea general, haz skimming. Si necesitas un dato, haz scanning con una palabra clave y una pregunta clara. Después, lee con calma solo la frase donde aparece el dato para comprobar que responde lo que preguntas.",
    ],
    [("skimming", "lectura rápida: idea general"), ("scanning", "lectura focalizada: dato exacto"), ("heading", "encabezado o título de una sección"), ("diagram", "diagrama"), ("list", "lista"), ("step", "paso")],
    [
        ("Elegir estrategia", "Quieres saber a qué hora es el taller de baile. ¿Qué estrategia usas? A) scanning B) skimming", ["Necesito un dato exacto.", "Busco la palabra Dance.", "Scanning."], "A) scanning"),
        ("Elegir estrategia", "Quieres saber de qué trata un artículo largo. ¿Qué estrategia usas? A) skimming B) scanning", ["Necesito la idea general.", "Leo título, subtítulo y primeras frases.", "Skimming."], "A) skimming"),
    ],
    [
        ("Leer todo palabra por palabra para encontrar un solo dato.", "Se pierde tiempo y atención.", "Usa scanning con una palabra clave."),
        ("Ignorar los números de pasos en un procedimiento.", "Se cambia el orden de las acciones.", "Sigue los números y los verbos de cada paso."),
    ],
    [
        ("Lee: " + SCHEDULE + " ¿A qué hora es el taller de pintura? A) a las 5:00 p. m. B) a las 4:30 p. m.", "A", "La cartelera dice Monday 5:00 p.m. – Painting."),
        ("Lee: " + SCHEDULE + " ¿En qué sala es el taller de música? A) sala 4 B) sala 2", "A", "Dice Thursday 5:30 p.m. – Music (Room 4)."),
        ("Lee: " + DIAG + " ¿Qué número tiene la cadena? A) 6 B) 3", "A", "El diagrama dice 6 chain."),
    ],
    [
        ("Lee: " + GUIDE + " ¿Para qué sirve el texto? A) para enseñar a hacer un volantín de papel B) para vender volantines", "A", "El título dice How to Make a Paper Kite."),
        ("Lee: " + SCHEDULE + " ¿Qué indica la nota final? A) que los materiales los lleva cada persona y es gratis para estudiantes B) que los talleres son de pago", "A", "Dice Bring your own materials y Free for students."),
        ("Lee: " + GUIDE + " ¿Qué materiales aparecen en What you need? A) papel, varillas, hilo y cinta B) tijeras y pegamento", "A", "Aparecen paper, two wooden sticks, string y tape."),
    ],
    [
        ("Lee: " + GUIDE + " ¿Qué se hace en el paso 3? A) cortar la figura y doblar los bordes sobre las varillas B) atar el hilo largo", "A", "Dice Cut the shape and fold the edges over the sticks."),
        ("Lee: " + SCHEDULE + " ¿Qué días hay talleres en la sala 1? A) lunes y viernes B) martes y jueves", "A", "Painting el lunes y Dance el viernes son en Room 1."),
        arith("Lee: Cada taller de la cartelera dura una hora, y hay cinco talleres en la semana. Una persona se inscribe en todos. ¿Cuántas horas asiste en cuatro semanas?", "5*4", "Se multiplican los talleres por semana por las semanas."),
    ],
    [
        ("Lee: " + GUIDE + " ¿Qué paso va antes de dibujar la forma en el papel? A) cruzar las varillas y atarlas B) cortar el papel", "A", "El paso 1 arma el armazón y el paso 2 lo coloca sobre el papel."),
        ("Lee: " + SCHEDULE + " ¿Por qué conviene usar scanning para saber la hora del taller de fotografía? A) porque busco una palabra exacta, Photography B) porque necesito la idea general", "A", "Con una palabra clave se encuentra el dato directamente."),
    ],
    [
        ("Lee: " + DIAG + " Una persona dice que el número 2 es la rueda. ¿Qué parte es según el diagrama? A) el asiento B) la rueda", "A", "El número 2 corresponde a saddle."),
        ("Lee: " + GUIDE + " Ordena los pasos: a) atar un hilo largo al centro b) cruzar las varillas c) cortar la forma", "b, c, a", "Primero el armazón, luego el corte y al final el hilo."),
    ],
    [("Lee: «Notice: The school gym is closed on Mondays. It opens Tuesday to Friday from 3:00 to 6:00 p.m.» (gym = gimnasio, notice = aviso). ¿A qué hora cierra el gimnasio de martes a viernes?", "A las 6:00 p. m.", "Se usa scanning: from 3:00 to 6:00 p.m.")],
    [
        ("¿Qué es skimming (en Inglés, 2.º medio)?", "Leer rápido para captar la idea general", "No se leen todas las palabras."),
        ("¿Qué es scanning (en Inglés, 2.º medio)?", "Buscar un dato exacto", "Se busca una palabra clave."),
        ("¿Para qué sirven los números de los pasos?", "Para seguir el orden de las acciones", "Marcan la secuencia."),
    ],
    task("Lee este texto ficticio: «Weekend Camp Guide. Title: Choosing a Backpack. Subtitle: Three tips for beginners. Tip 1: Choose a backpack that fits your back. Tip 2: Pack heavy things close to your back. Tip 3: Keep snacks for the way at the top. Picture: a backpack with labels: 1 straps, 2 main pocket, 3 side pocket.» (tips = consejos, fits = se ajusta, pack = poner, straps = correas, side pocket = bolsillo lateral). En tu hoja escribe: una pregunta para skimming, una para scanning y sus respuestas.", "Skimming: ¿De qué trata el texto? De cómo elegir una mochila. Scanning: ¿Qué número tiene el bolsillo lateral en el dibujo? 3.", ["formula una pregunta de idea general", "formula una pregunta de dato exacto", "responde ambas con el texto"], ["hoja con dos preguntas y respuestas"], ["hacer una pregunta de dato como si fuera de idea general", "responder con información que no está en el texto"], "Pide a una persona de tu casa que responda tus dos preguntas con el texto y mide cuánto tarda."),
    "Mira la cartelera de tu colegio o de tu barrio y practica scanning para encontrar tres datos.",
    "Escribe tres preguntas de skimming y tres de scanning sobre un texto de tu libro de inglés.",
)

# ================================================== clase 3: inferir, releer y preguntarse
STORY6 = "«When Camila opened the door, the room was dark and quiet. On the table, there was a cake with half of the candles still lit. A small card said: ‘We waited for you for an hour.’ Camila looked at her phone. She had six missed calls. She sat down and felt a warm, uncomfortable feeling in her chest.»\n(dark = oscura, candles = velas, still lit = aún encendidas, card = tarjeta, waited = esperamos, missed calls = llamadas perdidas, chest = pecho)"
ARTICLE6 = "«The Night Market Is Back. The old night market opened again after two years. Stalls sell handmade bracelets and tea. Some neighbours are worried about noise, though. The council promised to close at ten.»\n(night market = feria nocturna, bracelets = pulseras, neighbours = vecinos, worried = preocupados, noise = ruido, council = municipio, promised = prometió, close = cerrar)"
POEM6 = "«I carry two suitcases to a city I do not know, one full of photos, one full of questions.» (suitcases = maletas, photos = fotos, questions = preguntas)"

lesson(
    OA, 3, MAT_READ,
    "Aprenderé a hacer inferencias al leer, a releer cuando no entiendo y a plantearme preguntas mientras leo. Sirve para entender lo que el texto no dice con palabras y para resolver dudas sin rendirme.",
    ["Sé usar lectura rápida y focalizada.", "Sé reconocer palabras clave."],
    [
        "Una inferencia (inference) es una idea que no está escrita, pero que se deduce de pistas del texto y de lo que ya sabes. Por ejemplo, si una persona llega y encuentra una torta con la mitad de las velas encendidas y una tarjeta que dice We waited for you for an hour, puedes inferir que llegó tarde. La fórmula es: pista del texto + lo que sé = inferencia.",
        "Releer (rereading) significa volver a una frase cuando algo no está claro. No es un fracaso: los buenos lectores lo hacen mucho. Puedes releer una frase, un párrafo o todo el texto. También puedes plantearte preguntas (ask questions) mientras lees: ¿quién habla?, ¿por qué ocurre esto?, ¿qué pasará después? Escribe las preguntas en el margen y busca la respuesta.",
        "Combina las tres estrategias. Primero lee y marca las pistas. Después formula una inferencia con una palabra como probably, maybe o seems. Si dudas, relee la frase clave para comprobar. Una inferencia buena tiene apoyo en el texto; una suposición sin pistas no vale. Si hay varias pistas que apuntan a lo mismo, tu inferencia es más segura.",
    ],
    [("inference", "inferencia: idea que se deduce de pistas"), ("clue", "pista"), ("reread", "releer"), ("ask questions", "plantear preguntas"), ("probably", "probablemente"), ("seems", "parece")],
    [
        ("Inferir con pistas", "Lee: «Luis looked at the clock and ran to the bus stop without breakfast.» ¿Qué infieres? A) que estaba atrasado B) que tenía mucho tiempo", ["Corrió y no desayunó.", "Eso sugiere apuro.", "Estaba atrasado."], "A) que estaba atrasado"),
        ("Plantear preguntas", "Lee: «The door was open, but nobody was inside.» ¿Qué pregunta ayuda a comprender? A) ¿dónde está la gente? B) ¿cuál es el color de la pared?", ["La puerta abierta y nadie dentro genera una duda.", "Quiero saber dónde están las personas.", "Esa pregunta ayuda."], "A"),
    ],
    [
        ("Decir una inferencia sin ninguna pista del texto.", "Es una suposición, no una inferencia.", "Cita la frase que apoya tu idea."),
        ("No releer cuando no se entiende.", "Se sigue leyendo con una duda que crece.", "Vuelve a la frase clave y busca otra pista."),
    ],
    [
        ("Lee: " + STORY6 + " ¿Cómo estaba la habitación cuando entró Camila? A) oscura y silenciosa B) llena de gente", "A", "Dice the room was dark and quiet."),
        ("Lee: " + STORY6 + " ¿Cuántas llamadas perdidas tenía? A) seis B) dos", "A", "Dice six missed calls."),
        ("Lee: " + ARTICLE6 + " ¿Hasta qué hora se comprometió a cerrar el municipio? A) las diez B) las doce", "A", "Dice The council promised to close at ten."),
    ],
    [
        ("Lee: " + STORY6 + " ¿Qué se puede inferir sobre Camila? A) que llegó tarde a la celebración B) que organizó la fiesta", "A", "La tarjeta dice We waited for you for an hour."),
        ("Lee: " + ARTICLE6 + " ¿Qué se puede inferir sobre los vecinos? A) que algunos temen el ruido B) que todos están felices", "A", "Dice Some neighbours are worried about noise."),
        ("Lee: " + POEM6 + " ¿Qué se puede inferir? A) que la persona se muda a una ciudad nueva B) que va de vacaciones a la playa", "A", "La persona carga maletas y dice a city I do not know."),
    ],
    [
        ("Lee: " + STORY6 + " ¿Qué sentimiento expresa la última frase? A) incomodidad B) alegría", "A", "Dice warm, uncomfortable feeling."),
        ("Lee: " + ARTICLE6 + " ¿Qué muestra la palabra though? A) que hay un contraste: la feria vuelve, pero hay preocupación B) que la feria es peligrosa", "A", "Though introduce un contraste con la buena noticia."),
        ("Lee: " + POEM6 + " ¿Qué lleva la persona en la segunda maleta? A) preguntas B) fotos", "A", "Una maleta lleva fotos y la otra, preguntas."),
    ],
    [
        ("Lee: " + STORY6 + " Una compañera infiere que Camila estaba enojada con sus amigos. ¿Qué pista contradice o falta? A) el texto muestra un sentimiento incómodo, no enojo B) hay una torta", "A", "La pista habla de incomodidad, no de enojo."),
        ("Lee: " + ARTICLE6 + " ¿Qué pregunta ayuda a comprender mejor el texto? A) ¿qué hará el municipio para controlar el ruido? B) ¿cuántas pulseras hay?", "A", "Responde a la preocupación que menciona el texto."),
    ],
    [
        ("Lee: " + POEM6 + " ¿Qué dos sentimientos podría tener la persona al llegar? A) curiosidad y nostalgia B) enojo y aburrimiento", "A", "Las fotos sugieren nostalgia y las preguntas, curiosidad."),
        ("Lee: " + STORY6 + " Ordena las pistas: a) Camila mira su teléfono b) Camila abre la puerta c) Camila se sienta", "b, a, c", "El orden del texto es abrir, mirar y sentarse."),
    ],
    [("Lee: «Tomás wrote the date on his hand and looked at it twice before going to bed. He set his alarm for six.» (wrote = escribió, alarm = alarma). ¿Qué pista muestra que le preocupaba olvidar algo importante?", "Escribió la fecha en la mano y la miró dos veces", "El detalle de mirarla dos veces apunta a un recordatorio importante.")],
    [
        ("¿Qué es una inferencia (en estrategias de lectura)?", "Una idea que se deduce de pistas", "No está escrita directamente."),
        ("¿Qué haces cuando algo no está claro?", "Releo la frase o el párrafo", "Volver al texto ayuda."),
        ("¿Qué palabra puede introducir una inferencia?", "Probably", "Muestra que es una deducción."),
    ],
    task("Lee: «Mateo opened his bag in the middle of the class. His face turned red. He looked around and then at the teacher. ‘I think I left my project at home,’ he whispered.» (middle = medio, turned red = se puso rojo, whispered = susurró). En tu hoja escribe: dos pistas, una inferencia con probably y una pregunta que te harías al leer.", "Pistas: su cara se puso roja; miró alrededor y al profesor; susurró. Inferencia: probably siente vergüenza. Pregunta: ¿qué hará el profesor?", ["cita dos pistas del texto", "escribe una inferencia con probably", "formula una pregunta de lectura"], ["hoja con cuatro respuestas"], ["escribir una inferencia sin pistas", "inventar un dato que no está"], "Relee el texto y comprueba que tus dos pistas estén escritas allí."),
    "Lee un cuento breve y marca con un signo de interrogación cada duda que tengas.",
    "Escribe una escena de cuatro líneas sin decir cómo se siente el personaje y pide a otra persona que lo infiera.",
)

# ================================================== clase 4: después de leer, organizadores gráficos
TEXT_A = "«Two Ways to Get to School. Sara goes by bike. It takes fifteen minutes, it is free and she gets exercise. However, on rainy days it is uncomfortable. Pablo takes the bus. It takes thirty minutes, it costs eight hundred pesos and he can read on the way. However, sometimes the bus is full.»\n(by bike = en bicicleta, exercise = ejercicio, uncomfortable = incómodo, full = lleno)"
TEXT_B = "«How a Paper Planet Model is Made (steps). 1) Blow up a balloon. 2) Cover it with strips of paper and paste. 3) Wait one day for it to dry. 4) Paint it and add a ring.»\n(balloon = globo, strips = tiras, paste = engrudo, dry = secarse, paint = pintar, ring = anillo)"
TEXT_C = "«Cause and effect. The school bell was broken, so classes began late. As a result, lunch was shorter, and students were hungry in the afternoon.»\n(bell = timbre, broken = roto, began = empezaron, shorter = más corto, hungry = con hambre)"

lesson(
    OA, 4, MAT_READ,
    "Aprenderé a usar organizadores gráficos para ordenar lo que leí y a responder preguntas planteadas antes de leer. Sirve para comparar, ordenar pasos y relacionar causas y efectos con claridad.",
    ["Sé hacer una predicción antes de leer.", "Sé hacer inferencias al leer."],
    [
        "Después de leer (post-reading), puedes responder las preguntas que te planteaste y usar organizadores gráficos (graphic organisers). Un organizador gráfico es un dibujo simple que ordena ideas. Un diagrama de Venn (Venn diagram) compara dos cosas: en los círculos van las diferencias y en el centro lo que comparten. Una línea de tiempo (timeline) ordena hechos o pasos. Una tabla de causa y efecto (cause and effect) relaciona lo que ocurre con su motivo.",
        "Para elegir el organizador, mira el texto. Si compara dos opciones, usa un diagrama de Venn. Si da pasos con First, then, finally, usa una línea de tiempo o una lista numerada. Si usa so, because o as a result, usa causa y efecto. Si habla de un tema con varias ideas, usa una red de ideas (idea web): el tema al centro y las ideas alrededor.",
        "Al completar un organizador, escribe palabras clave, no frases largas. Revisa que cada dato venga del texto. Después, usa el organizador para responder preguntas o para explicar el texto a otra persona. Si algo no encaja, relee la parte del texto que lo menciona.",
    ],
    [("graphic organiser", "organizador gráfico"), ("Venn diagram", "diagrama de Venn: compara dos cosas"), ("timeline", "línea de tiempo"), ("cause and effect", "causa y efecto"), ("idea web", "red de ideas"), ("post-reading", "después de leer")],
    [
        ("Elegir organizador", "Un texto compara dos celulares: precio, batería y tamaño. ¿Qué organizador conviene? A) diagrama de Venn B) línea de tiempo", ["Hay dos objetos para comparar.", "El diagrama de Venn compara.", "Es el de Venn."], "A) diagrama de Venn"),
        ("Causa y efecto", "Lee: «It rained all night, so the road was muddy.» (muddy = con barro). ¿Cuál es la causa? A) llovió toda la noche B) el camino estaba con barro", ["So introduce la consecuencia.", "Lo que va antes es la causa.", "La causa es la lluvia."], "A"),
    ],
    [
        ("Copiar frases largas en el organizador.", "Se pierde la ventaja de una lectura rápida y clara.", "Escribe solo palabras clave."),
        ("Poner datos que no están en el texto.", "El organizador no representa lo leído.", "Revisa cada casilla con el texto."),
    ],
    [
        ("Lee: " + TEXT_A + " ¿Cuánto tarda Sara en llegar al colegio? A) quince minutos B) treinta minutos", "A", "El texto dice It takes fifteen minutes."),
        ("Lee: " + TEXT_B + " ¿Qué se hace primero? A) inflar un globo B) pintar", "A", "El paso 1 dice Blow up a balloon."),
        ("Lee: " + TEXT_C + " ¿Qué estaba roto? A) el timbre B) el reloj", "A", "Dice The school bell was broken."),
    ],
    [
        ("Lee: " + TEXT_A + " En un diagrama de Venn, ¿qué va en el centro? A) lo que ambos hacen: llegar al colegio B) el costo de Sara", "A", "El centro es lo común a Sara y Pablo."),
        ("Lee: " + TEXT_B + " ¿Qué organizador conviene? A) una línea de tiempo o lista numerada B) un diagrama de Venn", "A", "El texto da pasos ordenados."),
        ("Lee: " + TEXT_C + " ¿Cuál es el efecto de que el timbre estuviera roto? A) las clases empezaron tarde B) se acabó el almuerzo", "A", "Dice so classes began late."),
    ],
    [
        ("Lee: " + TEXT_A + " ¿Qué desventaja tiene la bicicleta en días de lluvia? A) es incómoda B) cuesta dinero", "A", "Dice on rainy days it is uncomfortable."),
        ("Lee: " + TEXT_C + " ¿Qué consecuencia tuvo el almuerzo más corto? A) los estudiantes tuvieron hambre en la tarde B) las clases terminaron antes", "A", "Dice students were hungry in the afternoon."),
        arith("Lee: " + TEXT_A + " Pablo viaja de ida y vuelta en bus todos los días, a 800 pesos cada viaje. ¿Cuántos pesos gasta en cinco días?", "800*2*5", "Se multiplican el pasaje, los dos viajes diarios y los cinco días."),
    ],
    [
        ("Lee: " + TEXT_A + " Completa mentalmente un Venn. ¿Qué característica va solo en Pablo? A) puede leer en el camino B) hace ejercicio", "A", "Pablo puede leer en el bus; el ejercicio es de Sara."),
        ("Lee: " + TEXT_C + " Ordena la cadena de causa y efecto: a) los estudiantes tuvieron hambre b) el timbre se rompió c) el almuerzo fue más corto", "b, c, a", "El timbre roto causó el atraso, luego el almuerzo corto y al final el hambre."),
    ],
    [
        ("Lee: " + TEXT_B + " Ordena los pasos: a) pintar y agregar el anillo b) cubrir el globo con tiras c) inflar el globo d) esperar un día", "c, b, d, a", "El texto numera los pasos de 1 a 4."),
        ("Lee: " + TEXT_A + " ¿Qué es más barato, según el texto? A) la bicicleta, que es gratis B) el bus, que cuesta 800 pesos", "A", "Dice it is free, mientras el bus cuesta."),
    ],
    [("Lee: «Pros of working in teams: you share ideas and finish faster. Cons: some people do not participate.» (pros = ventajas, cons = desventajas, participate = participar). ¿Qué organizador conviene? A) tabla de ventajas y desventajas B) línea de tiempo", "A", "El texto presenta dos grupos: pros y cons.")],
    [
        ("¿Qué compara un diagrama de Venn?", "Dos cosas", "Muestra lo común y lo distinto."),
        ("¿Qué organizador conviene para pasos?", "Una línea de tiempo o lista numerada", "Muestra el orden."),
        ("¿Qué muestra causa y efecto?", "Por qué ocurre algo y qué resultado tuvo", "Une causas y consecuencias."),
    ],
    task("Lee: «Two Sports. Football is played by two teams of eleven players. It needs a big field and a ball. Basketball is played by two teams of five players on a court, with a ball and two baskets. Both sports are team sports and both use a ball.» (field = cancha grande, court = cancha, baskets = canastos). Dibuja un diagrama de Venn y completa: lo exclusivo de cada deporte y lo común.", "Football: 11 jugadores por equipo, cancha grande. Basketball: 5 jugadores, dos canastos. Común: deportes de equipo y usan pelota.", ["incluye los dos deportes y el centro", "cada dato viene del texto", "usa palabras clave"], ["dibujo del diagrama de Venn"], ["poner datos que el texto no da", "mezclar lo exclusivo con lo común"], "Explica tu diagrama a una persona de tu casa usando solo las palabras clave."),
    "Convierte un texto de pasos en una línea de tiempo con tres casillas.",
    "Lee un texto corto de tu libro y elige el organizador que mejor sirva; explica tu elección.",
)

# ================================================== clase 5: recontar, resumir y confirmar
NEWS6 = "«School Mural Day (fictional) Moved to Friday. The art teacher announced that the painting day for the school wall will be moved from Wednesday to Friday because of the rain forecast. Students should bring old clothes and brushes. The activity will start at ten and end at one. Lunch will be provided by the parents’ committee.»\n(announced = anunció, wall = muro, moved = trasladado, forecast = pronóstico, brushes = pinceles, provided = entregado, committee = comité)"
STORY7 = "«A shy boy named Iván wanted to join the school theatre group. Every Tuesday he stood outside the room, but he never entered. One day, the teacher invited him in. Iván read a short line, and everyone clapped. After that, he joined every rehearsal.»\n(shy = tímido, join = unirse, outside = afuera, entered = entró, clapped = aplaudieron, rehearsal = ensayo)"

lesson(
    OA, 5, MAT_READ,
    "Aprenderé a releer, recontar y resumir un texto, y a preguntar para confirmar información. Sirve para comprobar que entendí y para explicar lo leído con mis propias palabras.",
    ["Sé usar organizadores gráficos.", "Sé responder preguntas sobre un texto."],
    [
        "Recontar (retell) es contar un texto con tus propias palabras, en orden: qué pasó primero, qué pasó después y cómo termina. Resumir (summarise) es decir solo lo más importante en pocas frases: la idea principal y los datos necesarios. Un buen resumen no copia el texto, no agrega opiniones y conserva los datos exactos, como fechas, cifras y nombres.",
        "Para resumir, sigue cuatro pasos: 1) relee y subraya las palabras clave; 2) responde who, what, when, where y why; 3) escribe una oración con la idea principal; 4) agrega uno o dos datos que la apoyan. Una oración inicial útil es The text says that… o The article explains that… Si el texto es un cuento, resume el personaje, el problema y la solución.",
        "Para confirmar (confirm) información, haz preguntas: Is it true that…?, Do you mean…?, Did you say…? Puedes preguntar a otra persona o a ti mismo y comprobar con el texto. Si no coincide, relee la frase. Confirmar evita errores cuando hay fechas, números o nombres parecidos. Al terminar, vuelve a tus predicciones y revisa si se confirmaron.",
    ],
    [("retell", "recontar con mis palabras"), ("summarise", "resumir: decir lo importante"), ("main idea", "idea principal"), ("confirm", "confirmar"), ("Is it true that…?", "¿Es verdad que…?"), ("reread", "releer")],
    [
        ("Resumen correcto", "Lee: «The library opens at eight. It has two floors. The first floor has novels and the second has study rooms.» (floors = pisos, novels = novelas, study rooms = salas de estudio). ¿Cuál es un buen resumen? A) The library has two floors: novels and study rooms. B) The library opens at eight.", ["Un resumen reúne la idea principal.", "La opción A incluye lo central.", "La B es un solo detalle."], "A"),
        ("Confirmar con una pregunta", "Una persona dice «The meeting is on the fifteenth». Para confirmar, ¿qué preguntas? A) Did you say the fifteenth? B) Are you tired?", ["Quiero comprobar la fecha.", "Repito el dato y pregunto.", "Did you say the fifteenth?"], "A"),
    ],
    [
        ("Resumir copiando tres párrafos.", "No es un resumen, es una copia.", "Escribe la idea principal con tus palabras."),
        ("Agregar tu opinión al resumen.", "Un resumen informa lo que dice el texto.", "Guarda tu opinión para una respuesta aparte."),
    ],
    [
        ("Lee: " + NEWS6 + " ¿A qué día se traslada la actividad? A) al viernes B) al lunes", "A", "Dice moved from Wednesday to Friday."),
        ("Lee: " + STORY7 + " ¿Cómo se llama el niño? A) Iván B) Tomás", "A", "Dice A shy boy named Iván."),
        ("Lee: " + NEWS6 + " ¿Qué deben llevar los estudiantes? A) ropa vieja y pinceles B) comida", "A", "Dice bring old clothes and brushes."),
    ],
    [
        ("Lee: " + NEWS6 + " ¿Por qué se cambia el día? A) por el pronóstico de lluvia B) por una prueba", "A", "Dice because of the rain forecast."),
        ("Lee: " + STORY7 + " ¿Cuál es el problema de Iván? A) es tímido y no se atreve a entrar B) no tiene tiempo", "A", "Dice he never entered."),
        ("Lee: " + NEWS6 + " ¿Quién entregará el almuerzo? A) el comité de padres B) los profesores", "A", "Dice Lunch will be provided by the parents’ committee."),
    ],
    [
        ("Lee: " + STORY7 + " ¿Cómo se resuelve el problema de Iván? A) la profesora lo invita a entrar y él lee una línea B) cambia de grupo", "A", "Dice the teacher invited him in. Iván read a short line."),
        ("Lee: " + NEWS6 + " ¿Quién anunció el cambio de día? A) la profesora de arte B) el director del colegio", "A", "Dice The art teacher announced."),
        ("Lee: " + NEWS6 + " ¿Cuál es el mejor resumen? A) The painting day was moved to Friday because of rain. B) Students should bring brushes.", "A", "Dice la idea principal; el pincel es un detalle."),
    ],
    [
        ("Lee: " + STORY7 + " ¿Cuál es el mejor resumen en una oración? A) A shy boy joins the theatre group after a teacher invites him. B) Iván claps for everyone.", "A", "Incluye personaje, problema y solución."),
        ("Lee: " + NEWS6 + " Para confirmar que la actividad es el viernes, ¿qué preguntas? A) Is it true that it is on Friday? B) Who is the art teacher?", "A", "Confirma el dato clave."),
    ],
    [
        ("Lee: " + STORY7 + " Recuenta en orden: a) todos aplaudieron b) la profesora lo invitó c) Iván esperaba afuera cada martes", "c, b, a", "El texto sigue ese orden."),
        ("Lee: " + NEWS6 + " Un compañero dice que la actividad dura desde las 10 hasta las 12. ¿Qué dato lo corrige? A) termina a la 1 B) empieza a las 9", "A", "Dice start at ten and end at one."),
    ],
    [("Lee: «The school shop sells notebooks for 1500 pesos and pens for 400 pesos. Today there is a 10% discount on notebooks.» (discount = descuento). Para confirmar el precio de un cuaderno, ¿qué pregunta haces? A) Do you mean fifteen hundred pesos? B) Is the shop open?", "A", "Confirma el precio de los cuadernos.")],
    [
        ("¿Qué es recontar (en Inglés, 2.º medio)?", "Contar un texto con mis palabras, en orden", "Incluye inicio, desarrollo y final."),
        ("¿Qué contiene un buen resumen (en estrategias de lectura)?", "La idea principal y los datos necesarios", "No copia ni opina."),
        ("¿Qué frase sirve para confirmar un dato?", "Did you say…?", "Verifica lo que se entendió."),
    ],
    task("Lee: «Title: A New Skate Rule. The school skate area will be open only after class, from four to six. Students must wear helmets and keep a distance of two metres. The head of sports, Mr. Díaz, said that the rule will start next Monday. ‘Safety comes first,’ he said.» (area = zona, helmets = cascos, distance = distancia, head = jefe, safety = seguridad). En tu hoja escribe: un resumen de dos oraciones y dos preguntas de confirmación.", "Resumen: The skate area will open only from four to six after class. Students must wear helmets and keep two metres, starting next Monday. Preguntas: Did you say from four to six? Is it true that helmets are compulsory?", ["el resumen tiene la idea principal y dos datos", "no copia el texto", "las preguntas confirman datos del texto"], ["hoja con resumen y dos preguntas"], ["copiar una oración completa", "preguntar algo que el texto no menciona"], "Léele tu resumen a una persona de tu casa y comprueba si puede repetir los datos."),
    "Lee un artículo breve en español y resúmelo en tres oraciones; luego escribe un resumen de una oración en inglés con The text says that…",
    "Elige un cuento corto y recuéntalo oralmente a una persona de tu casa con inicio, problema y solución.",
)
