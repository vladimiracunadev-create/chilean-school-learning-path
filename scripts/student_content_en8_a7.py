"""Cuaderno del estudiante, 8.º básico Inglés (propuesta), EN08 OA 07 (reacción a textos leídos o escuchados, con apoyo).

Todos los textos son originales y están escritos en cada ejercicio, con pista en español.
Las clases del plan tienen títulos genéricos; aquí cada clase trabaja un tipo de reacción que nombra el OA.
Los datos numéricos son de ejemplo.
"""
from __future__ import annotations

from student_content_en8_a import lesson, task
from student_lessons import arith

OA7 = "EN08 OA 07"
READ = "Lee: "

# ---------------------------------------------------------------- clase 1: hacer conexiones
EARTH = "«Chile is a long country with many volcanoes and earthquakes. The ground moves because the Earth has big pieces, called plates, that push each other. People in Chile practice earthquake drills at school and at work. After a strong earthquake, families check their emergency bag.» (volcanoes = volcanes, earthquakes = terremotos, ground = suelo, plates = placas, push = empujar, drills = simulacros, emergency bag = mochila de emergencia)"
FOOD = "«In many countries, families eat together on Sundays. In Japan, people often eat rice with fish. In Peru, many families prepare ceviche. In Chile, some families eat empanadas on special days. Food helps people share their culture.» (families = familias, rice = arroz, fish = pescado, prepare = preparar, special = especial, share = compartir)"

lesson(
    OA7, 1,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a reaccionar a un texto haciendo conexiones con otras asignaturas, con mi cultura, con mi vida diaria y con otras culturas, usando frases como I know about this because… e I remember that…. Sirve para comprender mejor y hablar de lo que leo.",
    ["Sé leer textos breves y reconocer el tema.", "Conozco la palabra because."],
    [
        "Hacer una conexión (connection) significa unir lo que lees con algo que ya sabes. Puede ser con otra asignatura (en Ciencias, las placas de la Tierra), con tu lengua materna y tu cultura (en Chile se hacen simulacros de sismo), con tu vida cotidiana (revisar la mochila de emergencia) o con otras culturas (qué comen las familias en otros países).",
        "Para expresarlo, usa frases de apoyo. «I know about this because…» (Sé de esto porque…) introduce lo que sabes: «I know about this because I studied plates in science class». «I remember that…» (Recuerdo que…) introduce un recuerdo: «I remember that we practiced a drill last year». Estas frases hacen que tu respuesta sea clara y ordenada.",
        "Una buena conexión siempre tiene dos partes: el dato del texto y la experiencia o idea tuya. Por ejemplo: «The text says that the Earth has plates. I know about this because we studied them in science». Si solo repites el texto, no hay conexión. Si solo hablas de ti, tampoco: une las dos partes.",
    ],
    [("connection", "conexión: unir el texto con algo que sé"), ("I know about this because…", "sé de esto porque…"), ("I remember that…", "recuerdo que…"), ("culture", "cultura"), ("daily life", "vida cotidiana"), ("subject", "asignatura")],
    [
        ("Conexión con otra asignatura", READ + EARTH + " ¿Con qué asignatura conectas la idea de las placas de la Tierra?", ["El texto habla de plates y de cómo se mueve el suelo.", "Eso se estudia en Ciencias Naturales.", "La conexión es con Ciencias."], "Con Ciencias Naturales"),
        ("Conexión con la vida diaria", READ + EARTH + " Escribe una conexión con tu vida usando I remember that…: has practicado un simulacro.", ["Tomo el dato del texto: drills at school.", "Agrego mi recuerdo: practicamos un simulacro.", "Uso la frase I remember that…"], "I remember that we practiced an earthquake drill at school"),
    ],
    [
        ("Repetir el texto sin agregar nada personal.", "Se cree que conectar es resumir.", "Une el dato del texto con algo que sabes o recuerdas."),
        ("Hablar de uno mismo sin mencionar el texto.", "Se pierde la relación con el texto.", "Empieza con el dato del texto y luego agrega tu conocimiento."),
    ],
    [
        # rec
        (READ + EARTH + " ¿Qué practican las personas en Chile? a) simulacros de sismo b) carreras de autos", "a) simulacros de sismo", "El texto dice People in Chile practice earthquake drills."),
        (READ + FOOD + " ¿Qué comen a menudo en Japón? a) arroz con pescado b) pasta con carne", "a) arroz con pescado", "El texto dice In Japan, people often eat rice with fish."),
        ("¿Qué frase introduce lo que sabes de un tema? a) I know about this because… b) What time is it?", "a) I know about this because…", "Introduce un conocimiento previo."),
    ],
    [
        # und
        (READ + EARTH + " ¿Con qué asignatura conecta «The Earth has big pieces called plates»? a) Ciencias Naturales b) Artes Visuales", "a) Ciencias Naturales", "Las placas se estudian en Ciencias."),
        (READ + FOOD + " ¿Con qué cultura conectas «ceviche»? a) la peruana b) la japonesa", "a) la peruana", "El texto dice In Peru, many families prepare ceviche."),
        (READ + EARTH + " ¿Qué revisan las familias después de un terremoto fuerte? a) la mochila de emergencia b) la televisión", "a) la mochila de emergencia", "El texto dice families check their emergency bag."),
    ],
    [
        # app
        (READ + FOOD + " Completa la conexión con tu cultura: «In Chile, some families eat ___ on special days». Elige: empanadas / ramen.", "empanadas", "El texto dice In Chile, some families eat empanadas."),
        (READ + EARTH + " Elige la mejor conexión: a) I know about this because we studied plates in science b) I like pizza", "a) I know about this because we studied plates in science", "Une el dato del texto con un conocimiento."),
        (READ + FOOD + " ¿Qué idea del texto conectas con tu vida si comes en familia los domingos? a) families eat together on Sundays b) people eat rice", "a) families eat together on Sundays", "Es el dato que se relaciona con esa experiencia."),
    ],
    [
        # rea
        (READ + EARTH + " Una compañera dice «I remember that I like football» después de leer. ¿Qué falta? a) relación con el texto b) más palabras", "a) relación con el texto", "No conecta ninguna idea del texto."),
        (READ + FOOD + " ¿Por qué el texto dice que la comida ayuda a compartir la cultura? a) porque cada país tiene platos especiales b) porque todos comen igual", "a) porque cada país tiene platos especiales", "Los ejemplos muestran platos distintos."),
    ],
    [
        # cha
        (READ + EARTH + " Escribe una conexión con Ciencias usando I know about this because… y la palabra plates.", "I know about this because I studied plates in science class", "Une el dato con lo aprendido."),
        (READ + FOOD + " Une cada país con su plato. 1) Japón 2) Perú 3) Chile. Platos: a) ceviche b) empanadas c) arroz con pescado", "1-c, 2-a, 3-b", "El texto da un plato por país."),
    ],
    [
        # context
        (READ + "«Last week, the city celebrated a cultural festival. People wore traditional clothes and sang folk songs. I remember that my grandmother made a traditional dessert.» (festival = fiesta cultural, wore = vestían, traditional = tradicional, folk songs = canciones folclóricas, dessert = postre). ¿Qué recuerda la persona? a) que su abuela hizo un postre tradicional b) que compró ropa", "a) que su abuela hizo un postre tradicional", "Después de I remember that aparece su recuerdo.")
    ],
    [
        # selfcheck
        ("¿Qué significa «I know about this because…»?", "Sé de esto porque…", "Introduce un conocimiento previo."),
        ("¿Con qué cuatro cosas puedes conectar un texto?", "Otras asignaturas, mi cultura, mi vida y otras culturas", "Son las conexiones del OA."),
        ("¿Qué dos partes tiene una buena conexión?", "El dato del texto y mi experiencia", "Une el texto con lo que sé."),
    ],
    task("Lee este texto: «Every year, around March 21, many countries celebrate the first day of spring in the north. In Chile, spring starts in September. Students plant flowers and draw pictures of nature.» (spring = primavera, plant = plantar, flowers = flores, pictures = dibujos, nature = naturaleza). Escribe en tu hoja una conexión con Ciencias, una con tu vida y una con tu cultura, usando I know about this because… e I remember that…", "Ciencias: I know about this because the seasons change due to the Earth's tilt. Vida: I remember that we planted flowers in spring. Cultura: In Chile, spring starts in September.", ["escribe tres conexiones", "usa las dos frases de apoyo", "cada conexión se relaciona con el texto"], ["hoja con tres conexiones", "nota del adulto"], ["conectar sin relación con el texto", "escribir datos científicos incorrectos"], "Reconoce las conexiones logradas y ayuda a unir cada una con una frase del texto."),
    "Lee de nuevo el texto de los terremotos y escribe dos conexiones propias con I know about this because….",
    "Escribe en español una conexión entre una idea de Historia o Ciencias y algo de tu vida diaria.",
)

# ---------------------------------------------------------------- clase 2: opiniones y justificación
PHONES = "«Some schools want students to leave their phones in lockers during class. Teachers say students pay more attention. Students say they need phones for emergencies. In my opinion, phones should stay in lockers during lessons, because students will listen better. I think there will be fewer distractions, and I know that exams are easier to prepare.» (leave = dejar, lockers = casilleros, pay attention = poner atención, emergencies = emergencias, distractions = distracciones, exams = pruebas)"

lesson(
    OA7, 2,
    "El texto escrito en cada ejercicio y lápiz.",
    "Aprenderé a expresar opiniones y a justificarlas con frases como there will be… because…, you should/shouldn't… because…, I know/find… e I think there will…. Sirve para decir lo que pienso y dar una razón.",
    ["Sé usar because para dar una razón.", "Conozco should y shouldn't."],
    [
        "Una opinión (opinion) dice lo que piensas. Para que sea fuerte, debe tener una justificación (justification), es decir, una razón. Se usa because: «You should leave your phone in the locker because you will listen better». Should significa debería; shouldn't, no debería. Se usa con el verbo en forma simple: you should read, you shouldn't run.",
        "Otras frases de apoyo ayudan a dar la opinión. «I think there will be…» (creo que habrá…) expresa una predicción: «I think there will be fewer distractions». «I know that…» (sé que…) o «I find it…» (me parece…) presentan una creencia o evaluación: «I find it difficult to study with a phone on the desk». «There will be…because…» (habrá… porque…) une una predicción con su razón.",
        "Para evaluar una opinión, pregunta: ¿tiene una razón?, ¿la razón se relaciona con la opinión?, ¿es un hecho o una impresión? Una justificación débil es «because I like it». Una justificación mejor es «because students will listen better». Escribe tu opinión con la estructura: opinión + because + razón. Si hay dos razones, agrega also (además).",
    ],
    [("opinion", "opinión"), ("justification", "justificación: la razón"), ("should", "debería"), ("I think there will be…", "creo que habrá…"), ("I find it…", "me parece…"), ("because", "porque")],
    [
        ("Identificar la opinión y la razón", READ + PHONES + " ¿Cuál es la opinión de la persona y su razón?", ["Busco In my opinion.", "La opinión: los celulares deben quedar en los casilleros.", "La razón viene después de because: students will listen better."], "Opina que los celulares deben quedar en los casilleros porque los estudiantes escucharán mejor"),
        ("Dar una predicción con razón", READ + PHONES + " Completa: «I think there will be fewer distractions ___ phones will stay in lockers». Opciones: because / but.", ["La oración da una razón.", "Because presenta la razón.", "La palabra es because."], "because"),
    ],
    [
        ("Dar una opinión sin razón.", "Se cree que la opinión es suficiente.", "Agrega because y una razón."),
        ("Usar «should» con el verbo en pasado.", "Se mezcla con el pasado.", "Después de should va el verbo simple: you should read."),
    ],
    [
        # rec
        (READ + PHONES + " ¿Dónde propone dejar los celulares? a) en los casilleros b) en la sala de profesores", "a) en los casilleros", "El texto dice leave their phones in lockers."),
        (READ + PHONES + " ¿Qué dicen los profesores? a) que los estudiantes ponen más atención b) que los celulares son caros", "a) que los estudiantes ponen más atención", "El texto dice students pay more attention."),
        (READ + PHONES + " ¿Para qué dicen los estudiantes que necesitan el celular? a) para emergencias b) para jugar", "a) para emergencias", "El texto dice they need phones for emergencies."),
    ],
    [
        # und
        ("¿Cuál es la opinión con razón? a) You should sleep early because you will have more energy b) You should sleep early", "a) You should sleep early because you will have more energy", "Incluye la razón con because."),
        ("¿Qué significa «shouldn't»? a) no debería b) no puede", "a) no debería", "Shouldn't es la forma negativa de should."),
        (READ + PHONES + " ¿Qué predicción hace la persona? a) habrá menos distracciones b) habrá más tarea", "a) habrá menos distracciones", "El texto dice there will be fewer distractions."),
    ],
    [
        # app
        ("Completa con should o shouldn't: «You ___ run in the pool because the floor is wet». Elige: shouldn't / should.", "shouldn't", "Correr en el piso mojado es peligroso."),
        ("Completa con la razón: «You should drink water because ___» (health = salud). Elige: it is good for your health / it is blue.", "it is good for your health", "La razón se relaciona con la opinión."),
        ("Completa con el conector que une la opinión y la razón: «We should recycle ___ it protects the planet». Elige: because / but.", "because", "La segunda parte explica la razón de la opinión."),
    ],
    [
        # rea
        (READ + PHONES + " Una compañera dice: «Phones are bad because I don't like them». ¿Qué le falta a su justificación? a) una razón relacionada con la situación b) más palabras", "a) una razón relacionada con la situación", "«No me gustan» es una razón personal débil."),
        (READ + PHONES + " ¿Qué razón comparten los profesores y quien opina? a) que los estudiantes escucharán mejor b) que los celulares son caros", "a) que los estudiantes escucharán mejor", "Ambos hablan de atención."),
    ],
    [
        # cha
        ("Ordena las palabras para formar una opinión: exercise / because / you / should / keeps / it / you / healthy.", "You should exercise because it keeps you healthy", "El orden es opinión con should + because + razón."),
        ("Ordena las palabras: because / should / you / read / learn / more / you.", "You should read because you learn more", "El orden es opinión + because + razón."),
    ],
    [
        # context
        (READ + "«I find it hard to study at night because the street is noisy. I think there will be less noise if the neighbors close their windows.» (hard = difícil, noisy = ruidosa, neighbors = vecinos). ¿Qué razón se da para estudiar mal de noche? a) que la calle es ruidosa b) que hay poca luz", "a) que la calle es ruidosa", "Se explica con because the street is noisy.")
    ],
    [
        # selfcheck
        ("En Inglés: ¿Qué palabra introduce una razón?", "Because", "Une la opinión con su razón."),
        ("¿Cómo se dice «creo que habrá…»?", "I think there will be…", "Expresa una predicción."),
        ("¿Qué significa «you should»?", "Tú deberías", "Da un consejo."),
    ],
    task("Lee este texto: «My school wants to start at eight thirty instead of eight. Many students think they will sleep more. Some parents say the school day will end late.» (instead of = en vez de, sleep = dormir, end = terminar). Escribe en tu hoja dos oraciones: una con You should… because… y otra con I think there will be… because…", "You should start at eight thirty because students will sleep more. I think there will be more traffic in the afternoon because the school day will end late.", ["escribe una opinión con should", "escribe una predicción con there will be", "agrega una razón con because"], ["hoja con dos oraciones", "nota del adulto"], ["no dar ninguna razón", "usar should con verbo en pasado"], "Reconoce lo que acertó y ayuda a unir cada opinión con una razón del texto."),
    "Lee de nuevo el texto de los celulares y escribe tu propia opinión con because.",
    "Escribe en español una opinión sobre un tema del colegio y dos razones que la apoyen.",
)

# ---------------------------------------------------------------- clase 3: comparaciones y su justificación
HEIGHT = "Datos de ejemplo. Alturas: Ana mide 150 centímetros, Leo mide 163 centímetros y Pía mide 158 centímetros. (tall = alto, taller = más alto/a, the tallest = el/la más alto/a)"
TREES = "Datos de ejemplo. Edades de tres árboles de un parque: el roble tiene 80 años, el ciprés tiene 120 años y la araucaria tiene 200 años. (oak = roble, cypress = ciprés, araucaria = araucaria, old = viejo, older = más viejo, the oldest = el más viejo)"

lesson(
    OA7, 3,
    "Los datos y textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a comparar y justificar con taller than, more important than y the oldest… because…. Sirve para decir qué es más grande, más importante o más antiguo, y dar una razón.",
    ["Sé el comparativo con -er y than.", "Conozco more y most."],
    [
        "Para comparar dos cosas con adjetivos cortos se usa -er + than: tall → taller than, old → older than. Con adjetivos largos se usa more + adjetivo + than: more important than, more interesting than. Para destacar el que más tiene una cualidad entre tres o más, se usa the + -est: the tallest, the oldest, o the most + adjetivo largo: the most important.",
        "Una comparación se justifica con because. «The cypress is older than the oak because it is 120 years old and the oak is 80». También se puede comparar con How much…? (¿cuánto más…?): «How much taller is Leo than Ana?» Se responde restando: 163 − 150 = 13 centímetros. Así se compara con un dato concreto. Para contar cosas se usa How many more…? (¿cuántos más…?): «How many more students does 8A have than 8B?». Los adjetivos que terminan en -e solo agregan -r o -st: larger, the largest.",
        "Cuando compares, comprueba que ambos elementos tienen el dato. No digas que algo es el más viejo si solo conoces dos edades. Usa the oldest solo con tres o más elementos. Después de than, usa el segundo elemento de la comparación: «taller than Ana». Una buena comparación nombra los dos elementos, el adjetivo y el dato que la apoya.",
    ],
    [("taller than", "más alto que"), ("more important than", "más importante que"), ("the oldest", "el más viejo"), ("the most", "el que más"), ("how much taller", "cuánto más alto"), ("because", "porque")],
    [
        ("Comparar dos datos", HEIGHT + " ¿Quién es más alto, Leo o Ana?", ["Leo mide 163 y Ana 150.", "163 es mayor que 150.", "Leo es taller than Ana."], "Leo es más alto que Ana"),
        ("Superlativo", TREES + " ¿Cuál es el árbol más viejo?", ["Comparo 80, 120 y 200 años.", "El mayor es 200.", "La araucaria es the oldest."], "La araucaria"),
    ],
    [
        ("Decir «more taller».", "Se mezcla more con -er.", "Los adjetivos cortos llevan -er: taller than."),
        ("Usar the oldest con solo dos elementos.", "Se confunde comparativo y superlativo.", "Con dos elementos usa older than; con tres o más, the oldest."),
    ],
    [
        # rec
        (HEIGHT + " ¿Quién mide 158 centímetros? a) Pía b) Ana", "a) Pía", "Los datos dicen que Pía mide 158."),
        (TREES + " ¿Cuántos años tiene el roble?", "80", "El dato dice que el roble tiene 80 años."),
        (HEIGHT + " ¿Qué palabra significa «más alto que»? a) taller than b) tallest", "a) taller than", "Taller than compara dos."),
    ],
    [
        # und
        (HEIGHT + " ¿Quién es the tallest? a) Leo b) Pía", "a) Leo", "Mide 163 cm, la mayor altura."),
        (TREES + " ¿Cuál es más viejo, el roble o el ciprés? a) el ciprés b) el roble", "a) el ciprés", "120 años es más que 80."),
        ("¿Qué comparativo corresponde a «important»? a) more important b) importanter", "a) more important", "Los adjetivos largos usan more."),
    ],
    [
        # app
        arith(HEIGHT + " ¿Cuántos centímetros más alto es Leo que Ana?", "163-150", "How much taller se responde restando las alturas."),
        arith(TREES + " ¿Cuántos años más tiene la araucaria que el ciprés?", "200-120", "Se restan las edades."),
        arith(HEIGHT + " ¿Cuántos centímetros más alta es Pía que Ana?", "158-150", "Se restan las alturas."),
    ],
    [
        # rea
        (TREES + " Justifica: «The araucaria is older than the cypress because ___». Elige: it is 200 years old and the cypress is 120 / it is green.", "it is 200 years old and the cypress is 120", "La razón usa un dato de comparación."),
        (HEIGHT + " Un compañero dice que Pía es the tallest. ¿Por qué se equivoca? a) porque Leo mide más b) porque Ana es más alta", "a) porque Leo mide más", "Leo mide 163, más que 158."),
    ],
    [
        # cha
        ("Completa con la forma correcta: «Math is ___ than history for me» (interesting).", "more interesting", "Interesting es largo y usa more."),
        ("Completa con la forma correcta: «Leo is the ___ of the three» (tall).", "tallest", "Con tres personas se usa the -est."),
    ],
    [
        # context
        (TREES + " ¿Qué frase es correcta? a) The oak is younger than the cypress b) The oak is older than the araucaria", "a) The oak is younger than the cypress", "El roble tiene 80 años y el ciprés 120.")
    ],
    [
        # selfcheck
        ("¿Cómo se forma el comparativo de tall?", "Taller", "Se agrega -er."),
        ("¿Qué palabra se usa con el comparativo?", "Than", "Se traduce que."),
        ("¿Cuándo se usa the oldest?", "Con tres o más elementos", "Se destaca el que más tiene la cualidad."),
    ],
    task("Con estos datos de ejemplo: el curso 8A tiene 36 estudiantes, el 8B tiene 30 y el 8C tiene 33. Escribe tres oraciones en inglés: una con more than, una con the largest y una con How many more…? y su respuesta, justificando con un dato. (students = estudiantes, class = curso)", "8A has more students than 8B because it has 36 and 8B has 30. 8A is the largest class. How many more students does 8A have than 8B? Six.", ["usa una comparación con more than", "usa the largest", "calcula la diferencia correctamente"], ["hoja con tres oraciones", "nota del adulto"], ["comparar el curso con un número que no corresponde", "restar mal"], "Reconoce la comparación bien armada y revisa con la persona cada resta."),
    "Mide a dos personas de tu casa con una huincha y escribe una comparación con taller than y la diferencia.",
    "Escribe en español dos cosas de tu colegio que comparas y por qué una es más importante que la otra.",
)

# ---------------------------------------------------------------- clase 4: resumir y sintetizar con oraciones simples
RADIO = "«The school radio started three years ago. Now it has twelve students who work as presenters and technicians. They broadcast every Friday at noon. The programs include music, news and interviews with teachers. Next month, the radio will start a new program about sports.» (radio = radio, presenters = locutores, technicians = técnicos, broadcast = transmitir, programs = programas, include = incluyen, interviews = entrevistas)"

lesson(
    OA7, 4,
    "El texto escrito en cada ejercicio y lápiz.",
    "Aprenderé a resumir y sintetizar información usando oraciones simples y descripciones breves, y a presentarla en un esquema. Sirve para explicar un texto de manera clara y corta.",
    ["Sé identificar la idea principal de un texto.", "Conozco oraciones simples con sujeto y verbo."],
    [
        "Resumir (to summarize) es decir lo más importante con pocas palabras. Sintetizar (to synthesize) es unir ideas de varias partes en una sola idea breve. Para hacerlo, usa oraciones simples (simple sentences): sujeto + verbo + complemento. «The radio started three years ago.» «Twelve students work on it.» Cada oración dice una idea.",
        "Una descripción breve (short description) dice cómo es algo con pocos adjetivos y datos: «The school radio has twelve students and broadcasts every Friday». Para organizar tus ideas, puedes usar un esquema (outline) con título, tres ideas y un cierre: Topic → Idea 1 → Idea 2 → Idea 3. El esquema es la base del resumen.",
        "Pasos para sintetizar: subraya las palabras clave, descarta los detalles menores, une las ideas en dos o tres oraciones y revisa que no cambies el sentido. No copies las frases del texto: reescríbelas con tus propias palabras. Si usas cifras (twelve students, every Friday), verifica que coincidan con el texto.",
    ],
    [("summarize", "resumir"), ("synthesize", "sintetizar: unir ideas en una"), ("simple sentence", "oración simple"), ("outline", "esquema"), ("short description", "descripción breve"), ("detail", "detalle")],
    [
        ("Escribir una oración simple", READ + RADIO + " Escribe una oración simple sobre cuántos estudiantes trabajan en la radio.", ["Busco el número: twelve students.", "Armo sujeto + verbo: Twelve students work on the radio.", "La oración es simple y tiene una idea."], "Twelve students work on the school radio"),
        ("Elegir el esquema", READ + RADIO + " ¿Cuál es el tema del esquema? Elige: The school radio / A football match.", ["El texto habla de la radio del colegio.", "El tema es lo que se repite.", "El tema es The school radio."], "The school radio"),
    ],
    [
        ("Copiar el texto completo como resumen.", "Se cree que resumir es copiar.", "Reescribe con oraciones simples y tus palabras."),
        ("Incluir todos los números.", "No se distingue lo esencial.", "Usa solo los datos necesarios."),
    ],
    [
        # rec
        (READ + RADIO + " ¿Cuándo transmite la radio? a) los viernes al mediodía b) los lunes por la tarde", "a) los viernes al mediodía", "El texto dice every Friday at noon."),
        (READ + RADIO + " ¿Cuántos estudiantes trabajan en la radio? a) 12 b) 20", "a) 12", "El texto dice twelve students."),
        (READ + RADIO + " ¿Hace cuántos años empezó la radio? a) tres b) cinco", "a) tres", "El texto dice started three years ago."),
    ],
    [
        # und
        (READ + RADIO + " ¿Qué programas incluye? a) música, noticias y entrevistas b) deportes y cocina", "a) música, noticias y entrevistas", "El texto dice include music, news and interviews."),
        (READ + RADIO + " ¿Cuál es una oración simple? a) The radio broadcasts on Fridays. b) Because of the programs, which include music.", "a) The radio broadcasts on Fridays.", "Tiene sujeto, verbo y una idea."),
        (READ + RADIO + " ¿Qué programa nuevo habrá? a) uno de deportes b) uno de ciencias", "a) uno de deportes", "El texto dice a new program about sports."),
    ],
    [
        # app
        (READ + RADIO + " Elige el mejor resumen: a) The school radio has twelve students and broadcasts music, news and interviews every Friday. b) The radio is new.", "a) The school radio has twelve students and broadcasts music, news and interviews every Friday.", "Incluye las ideas principales."),
        (READ + RADIO + " Ordena el esquema: A) program about sports B) started three years ago C) twelve students D) broadcasts every Friday.", "B, C, D, A", "Sigue el orden del texto."),
        (READ + RADIO + " ¿Qué detalle se puede dejar fuera de un resumen de una oración? a) que habrá un programa nuevo el próximo mes b) que es la radio del colegio", "a) que habrá un programa nuevo el próximo mes", "Es un dato futuro menos esencial."),
    ],
    [
        # rea
        (READ + RADIO + " Un compañero resume: «The radio is good». ¿Por qué no es un buen resumen? a) no da datos del texto b) usa pocas palabras", "a) no da datos del texto", "Es una opinión sin datos."),
        (READ + RADIO + " ¿Cuántas ideas principales tiene un buen resumen de este texto? a) dos o tres b) diez", "a) dos o tres", "Un resumen breve incluye lo esencial."),
    ],
    [
        # cha
        (READ + RADIO + " ¿Qué oración sintetiza el texto con las palabras radio, students y Friday? a) The school radio has students who broadcast on Friday b) The students have a football match on Friday", "a) The school radio has students who broadcast on Friday", "Une las tres palabras en una idea que coincide con el texto."),
        ("Completa un esquema sobre el texto: Tema: The school radio. Idea 1: twelve students. Idea 2: ___. Elige: broadcasts every Friday / has a big stadium.", "broadcasts every Friday", "El texto da ese dato."),
    ],
    [
        # context
        (READ + "«The class garden has fifteen tomato plants. Students water them every Monday and Thursday. Last week, they harvested five kilos of tomatoes.» (garden = huerto, water = regar, harvested = cosecharon). ¿Cuál es el mejor resumen? a) The class garden has fifteen plants and gave five kilos of tomatoes b) Students like tomatoes", "a) The class garden has fifteen plants and gave five kilos of tomatoes", "Une las cifras esenciales.")
    ],
    [
        # selfcheck
        ("¿Qué es sintetizar?", "Unir ideas en una idea breve", "Reduce el texto sin cambiar el sentido."),
        ("¿Qué es una oración simple?", "Una oración con sujeto y verbo que dice una idea", "Es clara y corta."),
        ("¿Para qué sirve un esquema?", "Para ordenar las ideas antes de resumir", "Muestra tema e ideas."),
    ],
    task("Lee este texto: «The school library has three computers, two thousand books and a quiet room. Students can borrow books for two weeks. The librarian says that the best time to visit is in the morning.» (librarian = bibliotecaria, borrow = pedir prestado). Escribe un esquema con tema y tres ideas, y luego un resumen de dos oraciones simples.", "Tema: the school library. Ideas: three computers; two thousand books; borrow for two weeks. Resumen: The school library has computers and books. Students can borrow books for two weeks.", ["escribe el esquema con tema y tres ideas", "resume en dos oraciones simples", "no copia el texto"], ["hoja con esquema y resumen", "nota del adulto"], ["incluir opiniones", "copiar todo"], "Reconoce el esquema y ayuda a reducir el resumen a las ideas esenciales."),
    "Subraya las palabras clave del texto de la radio y escribe una oración simple con cada una.",
    "Escribe en español cómo resumirías en tres oraciones simples un reportaje que hayas visto.",
)

# ---------------------------------------------------------------- clase 5: generar preguntas y responder de forma independiente
JACKETS = "«In the gym there are three jackets. Ana says: Whose jackets are these? Leo: The blue one is mine. Pía: The gray one is Mateo's. The red one is ours; it belongs to the twins. Mateo is two years older than his sister.» (jackets = chaquetas, mine = mía, Mateo's = de Mateo, ours = nuestra, twins = gemelos, older = mayor)"

lesson(
    OA7, 5,
    "El diálogo y los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a generar preguntas sobre un texto (Whose… are these?, How much taller…?, When…?) y a reaccionar con una respuesta independiente: una pregunta, una opinión y un resumen. Sirve para comprobar lo que entendí y para conversar.",
    ["Sé usar who, what, where y when.", "Conozco whose y how much."],
    [
        "Generar preguntas (generate questions) sobre un texto ayuda a comprender y a conversar. Whose…? pregunta por el dueño: «Whose jackets are these?» (¿de quién son estas chaquetas?). How much taller…? pregunta por una diferencia: «How much taller is Leo than Ana?». When…? pregunta por el tiempo: «When did the radio start?». Cada palabra pide un tipo de dato.",
        "Para formar una pregunta con When, Where o How much, usa un verbo auxiliar: do, does o did en el presente y pasado simples. «When did it start?» (no «When it started?»). Con whose, el sustantivo va después: Whose book is this? Para elegir la pregunta correcta, mira la respuesta: si es un dueño, usa whose; si es un tiempo, when; si es una cantidad, how much o how many.",
        "Una respuesta independiente combina tres partes: una pregunta propia, una opinión con because y un resumen de una oración. Por ejemplo: «Whose jacket is the gray one? In my opinion, Mateo should take it because it is his. The text is about three jackets in the gym». Así demuestras que entendiste, opinas y resumes.",
    ],
    [("whose", "de quién"), ("how much", "cuánto"), ("when", "cuándo"), ("auxiliary verb", "verbo auxiliar: do, does, did"), ("belongs to", "pertenece a"), ("mine / ours", "mío / nuestro")],
    [
        ("Elegir la pregunta correcta", READ + JACKETS + " Respuesta: «It belongs to the twins». ¿Qué pregunta la genera? Elige: Whose jacket is the red one? / When did they arrive?", ["La respuesta indica un dueño.", "Para un dueño se usa whose.", "La pregunta es Whose jacket is the red one?"], "Whose jacket is the red one?"),
        ("Preguntar por una diferencia", "Datos de ejemplo: Ana tiene 14 años y su hermano Mateo tiene 16. ¿Qué pregunta hace falta para obtener la diferencia? Elige: How much older is Mateo than Ana? / Whose is Mateo?", ["Se busca una diferencia de edad.", "How much older pregunta por la diferencia.", "La pregunta es How much older is Mateo than Ana?"], "How much older is Mateo than Ana?"),
    ],
    [
        ("Decir «When it started?».", "Se omite el verbo auxiliar.", "En el pasado se dice When did it start?"),
        ("Hacer una pregunta cuya respuesta no está en el texto.", "No se revisa el texto.", "Comprueba que la respuesta aparece en el texto."),
    ],
    [
        # rec
        (READ + JACKETS + " ¿De quién es la chaqueta azul? a) de Leo b) de Pía", "a) de Leo", "Leo dice The blue one is mine."),
        (READ + JACKETS + " ¿De quién es la chaqueta gris? a) de Mateo b) de Ana", "a) de Mateo", "Pía dice The gray one is Mateo's."),
        (READ + JACKETS + " ¿Cuántas chaquetas hay en el gimnasio?", "3", "El texto dice three jackets."),
    ],
    [
        # und
        ("¿Qué pregunta sirve para saber el dueño de un objeto? a) Whose bag is this? b) How much is the bag?", "a) Whose bag is this?", "Whose pregunta por el dueño."),
        ("¿Qué pregunta sirve para saber el momento? a) When did the match start? b) Whose match is it?", "a) When did the match start?", "When pregunta por el tiempo."),
        (READ + JACKETS + " ¿Qué significa «ours» en la oración sobre la chaqueta roja? a) nuestra b) tuya", "a) nuestra", "Ours es el pronombre de nosotros."),
    ],
    [
        # app
        (READ + JACKETS + " Respuesta: «Two years». ¿Qué pregunta la genera? a) How much older is Mateo than his sister? b) Whose jacket is red?", "a) How much older is Mateo than his sister?", "La respuesta es una diferencia de edad."),
        ("Completa con did: «When ___ the class start?». Elige: did / does.", "did", "Para el pasado se usa did."),
        (READ + JACKETS + " ¿A quiénes pertenece la chaqueta roja? a) a los gemelos b) a Leo", "a) a los gemelos", "El texto dice it belongs to the twins."),
    ],
    [
        # rea
        (READ + JACKETS + " ¿Cuál es una buena opinión con razón sobre la chaqueta gris? a) Mateo should take it because it is his b) The jacket is nice", "a) Mateo should take it because it is his", "Tiene opinión y razón."),
        ("Un compañero pregunta «How much old is Mateo?». ¿Cuál es la forma correcta? a) How old is Mateo? b) How many old is Mateo?", "a) How old is Mateo?", "How old pregunta por la edad."),
    ],
    [
        # cha
        (READ + JACKETS + " ¿Qué pregunta sirve para saber de quién es la chaqueta azul? a) Whose jacket is the blue one? b) How much is the jacket?", "a) Whose jacket is the blue one?", "Whose pregunta por el dueño."),
        (READ + JACKETS + " ¿Cuál es el mejor resumen del texto? a) There are three jackets in the gym, and each has an owner b) The gym is big", "a) There are three jackets in the gym, and each has an owner", "Resume la idea central del diálogo."),
    ],
    [
        # context
        ("En un dramatizado, una persona pregunta: «Whose phone is this?». ¿Qué respuesta es correcta? a) It's mine b) It starts at six", "a) It's mine", "Mine responde con un dueño.")
    ],
    [
        # selfcheck
        ("¿Qué pregunta usas para saber el dueño?", "Whose…?", "Pregunta por la posesión."),
        ("¿Qué verbo auxiliar usas en When… en pasado?", "Did", "When did it start?"),
        ("¿Qué tres partes tiene una respuesta independiente?", "Pregunta, opinión con because y resumen", "Muestra que comprendiste el texto."),
    ],
    task("Lee este texto: «The school theater club performed a play last Saturday. Twenty students acted and ten worked backstage. Tickets cost two thousand pesos. The play was about a lost dog.» (theater = teatro, performed = presentó, acted = actuaron, backstage = detrás de escena, tickets = entradas). Escribe una pregunta con When, una con How much, una opinión con because y un resumen de una oración.", "When did the club perform the play? How much were the tickets? I think the play was good because many students worked together. The theater club performed a play about a lost dog.", ["escribe dos preguntas correctas", "escribe una opinión con razón", "escribe un resumen de una oración"], ["hoja con cuatro respuestas", "nota del adulto"], ["omitir el verbo auxiliar", "dar una opinión sin because"], "Reconoce las preguntas bien formadas y ayuda a agregar la razón de la opinión."),
    "Escribe con una persona de tu casa un diálogo de cuatro líneas con Whose…? y Which is yours?",
    "Escribe en español una pregunta que te gustaría hacer sobre un texto y cómo responderías.",
)
