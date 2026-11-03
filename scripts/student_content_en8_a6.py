"""Cuaderno del estudiante, 8.º básico Inglés (propuesta), EN08 OA 06 (estrategias de lectura antes, durante y después).

Todos los textos para leer son originales y están escritos en cada ejercicio, con pista en español.
Las clases del plan tienen títulos genéricos; aquí cada clase trabaja una estrategia que nombra el OA.
"""
from __future__ import annotations

from student_content_en8_a import lesson, task
from student_lessons import arith

OA6 = "EN08 OA 06"
READ = "Lee: "

# ---------------------------------------------------------------- clase 1: antes de leer (propósito, predicciones, conocimientos previos)
BEES = "Título: «Busy Bees». Subtítulo: «Why bees matter». Texto: «Bees are small insects that live in groups called colonies. They visit flowers to collect nectar and pollen. When they move from flower to flower, they carry pollen, and this helps plants make fruit and seeds. Without bees, we would have less fruit. Pesticides can harm bee colonies, so many cities now plant flowers without pesticides.» (insects = insectos, colonies = colonias, flowers = flores, nectar = néctar, pollen = polen, seeds = semillas, pesticides = pesticidas, harm = dañar)"

lesson(
    OA6, 1,
    "Los textos con título y subtítulo escritos en cada ejercicio y lápiz.",
    "Aprenderé estrategias para antes de leer: leer con un propósito, hacer predicciones y usar lo que ya sé. Sirve para entrar al texto sabiendo qué busco y qué esperar.",
    ["Sé reconocer el título y el subtítulo de un texto.", "Sé hacer predicciones al escuchar."],
    [
        "Antes de leer (pre-reading), prepara tu mente con tres estrategias. Primera, leer con un propósito (purpose): decide qué quieres averiguar, por ejemplo «¿por qué son importantes las abejas?». Con un propósito, ya sabes qué buscar. Segunda, hacer predicciones (predictions): mira el título, el subtítulo y las imágenes, y piensa qué dirá el texto. Tercera, usar conocimientos previos (prior knowledge): recuerda lo que ya sabes del tema.",
        "Para predecir, usa pistas. Si el título dice «Busy Bees» y el subtítulo dice «Why bees matter», puedes predecir palabras como flowers, honey o plants. Si el texto trata de insectos, probablemente se hable de grupos o de su trabajo. Escribe dos o tres predicciones breves. Después de leer, las comprobarás.",
        "Tu propósito puede cambiar según la tarea: para estudiar, buscas ideas y datos; para disfrutar, buscas la historia; para una tarea, buscas una respuesta concreta. Una buena pregunta antes de leer empieza con why, how o what. Escríbela en una hoja y búscala en el texto. Si no aparece, lee de nuevo con otra pregunta.",
    ],
    [("purpose", "propósito: para qué leo"), ("prediction", "predicción: lo que creo que dirá el texto"), ("prior knowledge", "conocimientos previos"), ("title", "título"), ("subtitle", "subtítulo"), ("pre-reading", "antes de leer")],
    [
        ("Hacer una predicción", "Título: «Busy Bees». Subtítulo: «Why bees matter». ¿Qué palabra esperas encontrar? Elige: flowers / calculator.", ["Miro el título y el subtítulo: hablan de abejas.", "Pienso en lo que sé: las abejas visitan flores.", "La palabra es flowers."], "flowers"),
        ("Escribir un propósito", "Quieres saber por qué son importantes las abejas. ¿Qué pregunta escribes antes de leer? Elige: Why are bees important? / How many pages are there?", ["Mi propósito es saber la importancia de las abejas.", "La pregunta debe empezar con why.", "Why are bees important? sirve para buscar la razón."], "Why are bees important?"),
    ],
    [
        ("Leer sin tener un propósito y quedar sin saber qué buscar.", "Se empieza a leer sin una pregunta.", "Antes de leer escribe una pregunta con why, how o what."),
        ("Predecir con una sola pista y no cambiar la predicción.", "Se mira solo el título.", "Usa título, subtítulo e imagen, y cambia la predicción si el texto dice otra cosa."),
    ],
    [
        # rec
        ("Título: «Bees and flowers». ¿Qué parte del texto miras primero para predecir? a) el título b) la última palabra", "a) el título", "El título resume de qué trata el texto."),
        ("Subtítulo: «Why bees matter». ¿Qué significa matter aquí? a) ser importante b) tener materia", "a) ser importante", "Why bees matter pregunta por qué las abejas son importantes."),
        ("¿Qué estrategia consiste en recordar lo que ya sabes? a) usar conocimientos previos b) releer", "a) usar conocimientos previos", "Los conocimientos previos son lo que ya sabes."),
    ],
    [
        # und
        (READ + BEES + " ¿Se cumple la predicción flowers? a) sí, porque el texto dice que visitan flores b) no, no aparece", "a) sí, porque el texto dice que visitan flores", "El texto dice They visit flowers."),
        (READ + BEES + " ¿Cómo se llama el grupo en que viven las abejas? a) colonia b) bosque", "a) colonia", "El texto dice live in groups called colonies."),
        (READ + BEES + " ¿Qué ayuda a las plantas a producir frutos? a) el polen que llevan las abejas b) el agua de lluvia", "a) el polen que llevan las abejas", "El texto dice they carry pollen, and this helps plants make fruit."),
    ],
    [
        # app
        (READ + BEES + " Tu propósito era saber qué daña a las abejas. ¿Qué palabra del texto responde? a) pesticides b) nectar", "a) pesticides", "El texto dice Pesticides can harm bee colonies."),
        (READ + BEES + " ¿Qué hacen muchas ciudades para ayudar a las abejas? a) plantar flores sin pesticidas b) construir más calles", "a) plantar flores sin pesticidas", "El texto dice many cities now plant flowers without pesticides."),
        ("Antes de leer «Busy Bees», una persona predijo que habría datos de fútbol. ¿Qué debe hacer después de leer? a) corregir su predicción b) decir que el texto está mal", "a) corregir su predicción", "La predicción se cambia con lo que el texto dice."),
    ],
    [
        # rea
        (READ + BEES + " Dos estudiantes tienen propósitos distintos. Ana quiere saber qué comen las abejas y Luis quiere saber por qué son importantes. ¿Qué frase sirve a Luis? a) Without bees, we would have less fruit b) Bees visit flowers", "a) Without bees, we would have less fruit", "Responde por qué importan: sin abejas habría menos fruta."),
        ("Un compañero lee solo el subtítulo «Why bees matter» y concluye que el texto trata de física porque matter significa materia. ¿Qué pista ignoró? a) la palabra bees b) la palabra why", "a) la palabra bees", "Bees es la pista del tema."),
    ],
    [
        # cha
        ("Elige el mejor propósito para estudiar el texto de las abejas con la intención de explicar a un amigo por qué son importantes: a) buscar la razón y un dato b) copiar todo el texto", "a) buscar la razón y un dato", "Un propósito claro limita lo que se busca."),
        ("Escribe una palabra del texto que predijiste y que apareció: flowers, honey o sea.", "flowers", "Flowers aparece varias veces en el texto; honey y sea no aparecen."),
    ],
    [
        # context
        ("Vas a leer un artículo sobre «Cleaning the beach». Tu propósito es saber cuántas personas ayudaron. ¿Qué pregunta escribes? a) How many people helped? b) Where is the bus?", "a) How many people helped?", "How many pregunta por una cantidad.")
    ],
    [
        # selfcheck
        ("En Inglés: ¿Qué es una predicción?", "Una idea de lo que dirá el texto", "Se hace antes de leer."),
        ("¿Qué pistas usas para predecir?", "Título, subtítulo e imágenes", "Dan información sobre el tema."),
        ("¿Para qué sirve leer con un propósito?", "Para saber qué buscar", "Orienta la atención."),
    ],
    task("Observa este título y subtítulo: «Save Energy at School. How to use less electricity». Escribe en tu hoja: tres palabras que predices, una pregunta con why o how, y qué conocimiento previo usaste. Luego lee: «Turn off the lights when you leave the room. Use natural light when possible. Unplug chargers that you are not using.» (turn off = apagar, natural light = luz natural, unplug = desconectar, chargers = cargadores). Marca qué predicción se cumplió.", "Predicciones: lights, electricity, turn off. Pregunta: How can we use less electricity? Conocimiento previo: apagar luces ahorra energía. Se cumplió lights.", ["escribe tres predicciones coherentes", "formula una pregunta de propósito", "marca la que se cumplió"], ["hoja con predicciones y pregunta", "nota del adulto"], ["predecir palabras sin relación con el tema", "escribir una pregunta sin why o how"], "Reconoce las predicciones útiles y revisa con la persona qué parte del título dio cada pista."),
    "Antes de leer otro texto de tu casa, escribe una pregunta de propósito y una predicción.",
    "Escribe en español qué sabes de las abejas y qué quisieras saber antes de leer sobre ellas.",
)

# ---------------------------------------------------------------- clase 2: lectura rápida y focalizada, y elementos organizacionales
CAMP = "Título: «Green Park Summer Camp». Subtítulo 1: «Activities». Texto: «Painting, football and gardening.» Subtítulo 2: «Dates and prices». Texto: «Two weeks, from January 8 to January 21. The price is 45.000 pesos per week.» Subtítulo 3: «Rules». Texto: «Bring a hat, sunscreen and a water bottle. Arrive at nine o'clock.» (camp = campamento, activities = actividades, gardening = jardinería, dates = fechas, price = precio, rules = reglas, bring = traer, sunscreen = bloqueador solar, arrive = llegar)"

lesson(
    OA6, 2,
    "El texto con subtítulos escrito en cada ejercicio y lápiz.",
    "Aprenderé a usar la lectura rápida y la lectura focalizada, y a apoyarme en el título, los subtítulos y las imágenes. Sirve para encontrar información sin leer cada palabra.",
    ["Sé que los textos tienen título y subtítulos.", "Conozco las preguntas who, what, when, where y how much."],
    [
        "La lectura rápida (skimming) consiste en pasar la vista por el texto para entender de qué trata. Se leen el título, los subtítulos, las primeras palabras de cada párrafo y las imágenes. Sirve para saber si un texto sirve para tu propósito. La lectura focalizada (scanning) busca un dato concreto, como un precio, una fecha o un nombre. Se pasa la vista hasta encontrar esa palabra o cifra.",
        "Los elementos organizacionales (organizational elements) guían la lectura: el título (title) dice el tema general, los subtítulos (subtitles) dividen el texto en partes, y las imágenes (images) muestran lo que el texto describe. En el texto del campamento, «Dates and prices» te lleva directo a las fechas y los precios. Si buscas qué traer, el subtítulo útil es «Rules».",
        "Primero usa skimming para ubicar la parte donde está lo que buscas; luego usa scanning para encontrar el dato exacto. No leas todas las palabras: busca números, nombres y las palabras de tu pregunta. Después de encontrar el dato, léelo con calma para comprobar que responde la pregunta.",
    ],
    [("skimming", "lectura rápida: ver de qué trata"), ("scanning", "lectura focalizada: buscar un dato"), ("title", "título"), ("subtitle", "subtítulo"), ("image", "imagen"), ("price", "precio")],
    [
        ("Skimming con subtítulos", READ + CAMP + " ¿Qué subtítulo lees para saber qué traer?", ["Quiero saber qué traer.", "Los subtítulos son Activities, Dates and prices y Rules.", "Rules dice Bring a hat..."], "Rules"),
        ("Scanning de un dato", READ + CAMP + " ¿Cuál es el precio por semana?", ["Busco un número con pesos.", "En Dates and prices dice 45.000 pesos per week.", "El dato es 45.000."], "45.000 pesos por semana"),
    ],
    [
        ("Leer palabra por palabra para encontrar un precio.", "No se usa scanning.", "Pasa la vista hasta ver el número y luego léelo con calma."),
        ("Ignorar los subtítulos y perder tiempo.", "No se aprovecha la organización del texto.", "Los subtítulos te dicen dónde buscar."),
    ],
    [
        # rec
        (READ + CAMP + " ¿Qué actividad aparece primero? a) painting b) swimming", "a) painting", "Dice Painting, football and gardening."),
        (READ + CAMP + " ¿A qué hora hay que llegar? a) a las nueve b) a las diez", "a) a las nueve", "El texto dice Arrive at nine o'clock."),
        (READ + CAMP + " ¿Qué subtítulo habla de las fechas? a) Dates and prices b) Rules", "a) Dates and prices", "Dates significa fechas."),
    ],
    [
        # und
        (READ + CAMP + " ¿Qué técnica usas para saber de qué trata el texto sin leer todo? a) skimming b) scanning", "a) skimming", "Skimming es la lectura rápida."),
        (READ + CAMP + " ¿Qué técnica usas para encontrar el número del precio? a) scanning b) skimming", "a) scanning", "Scanning busca un dato concreto."),
        (READ + CAMP + " ¿Qué dos objetos hay que llevar para el sol? a) sombrero y bloqueador b) bufanda y guantes", "a) sombrero y bloqueador", "Dice Bring a hat, sunscreen and a water bottle."),
    ],
    [
        # app
        arith(READ + CAMP + " ¿Cuánto cuesta el campamento completo de dos semanas, en pesos?", "45000*2", "Se multiplica el precio semanal por las dos semanas."),
        (READ + CAMP + " ¿Cuántos objetos hay que traer según Rules?", "3", "El texto nombra tres objetos."),
        (READ + CAMP + " ¿En qué fecha termina el campamento? a) el 21 de enero b) el 8 de enero", "a) el 21 de enero", "El texto dice to January 21."),
    ],
    [
        # rea
        (READ + CAMP + " Un compañero necesita saber qué deportes se practican. ¿Qué subtítulo debe escanear? a) Activities b) Rules", "a) Activities", "Allí aparece football."),
        (READ + CAMP + " ¿Por qué es útil leer primero los subtítulos? a) porque indican dónde está cada tipo de información b) porque son más largos", "a) porque indican dónde está cada tipo de información", "Dividen el texto en partes."),
    ],
    [
        # cha
        ("Una imagen del campamento muestra niños con sombreros y botellas de agua. ¿Qué parte del texto apoya? a) Rules b) Dates and prices", "a) Rules", "Rules pide sombrero y botella de agua."),
        (READ + CAMP + " Escribe la palabra del texto que significa «reglas».", "Rules", "Es el subtítulo de la tercera parte."),
    ],
    [
        # context
        (READ + "Título: «School Lunch Menu». Monday: rice and chicken. Tuesday: pasta and salad. Wednesday: fish and potatoes. Price: 2.500 pesos. (chicken = pollo, salad = ensalada, fish = pescado, potatoes = papas). Usa scanning: ¿qué se come el miércoles? a) pescado y papas b) pasta y ensalada", "a) pescado y papas", "Busca la palabra Wednesday.")
    ],
    [
        # selfcheck
        ("¿Qué es skimming?", "Leer rápido para ver de qué trata", "Se usan título, subtítulos e imágenes."),
        ("¿Qué es scanning?", "Buscar un dato concreto en el texto", "Se buscan números o nombres."),
        ("¿Para qué sirven los subtítulos?", "Para ubicar cada parte del texto", "Organizan la información."),
    ],
    task("Lee este texto: «Title: Sports Day. Subtitle 1: When? Text: On Friday, October 13, from nine to one. Subtitle 2: What to wear. Text: Sport clothes and white shoes. Subtitle 3: Teams. Text: Red, blue, yellow and green.» (sports day = día del deporte, clothes = ropa, shoes = zapatillas, teams = equipos). Usa skimming para decir de qué trata el texto y scanning para encontrar la fecha, qué ropa llevar y cuántos equipos hay.", "Trata del día del deporte. Fecha: viernes 13 de octubre, de nueve a una. Ropa: ropa deportiva y zapatillas blancas. Hay 4 equipos.", ["usa skimming para el tema", "usa scanning para tres datos exactos", "cuenta correctamente los equipos"], ["hoja con tema y datos", "nota del adulto"], ["decir que hay tres equipos", "confundir la fecha con la hora"], "Reconoce los datos hallados y revisa con la persona qué subtítulo conviene mirar para cada pregunta."),
    "Con una persona de tu casa, haz skimming de un folleto o una página impresa y dile de qué trata en dos oraciones.",
    "Escribe en español cuándo conviene usar skimming y cuándo scanning en una tarea del colegio.",
)

# ---------------------------------------------------------------- clase 3: visualizar y usar organizadores gráficos
HOUSE = "«A small wooden house stands at the top of a green hill. It has a red door and two round windows. A tall tree grows next to it, and a gray cat sleeps under the tree.» (wooden = de madera, stands = se encuentra, hill = cerro, door = puerta, round = redondas, windows = ventanas, grows = crece, sleeps = duerme)"
STEPS = "«How to wash a bike. First, take the bike outside. Then wet it with water. Next, clean it with a sponge and soap. After that, rinse it. Finally, dry it with a cloth.» (wash = lavar, wet = mojar, sponge = esponja, soap = jabón, rinse = enjuagar, dry = secar, cloth = paño)"

lesson(
    OA6, 3,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a visualizar lo que leo, es decir, imaginar una imagen mental, y a usar organizadores gráficos como la secuencia, la red de ideas y la tabla de causa y efecto. Sirve para recordar y ordenar la información.",
    ["Sé leer descripciones breves.", "Conozco first, then y finally."],
    [
        "Visualizar (visualize) significa crear una imagen mental de lo que lees. Si el texto describe una casa pequeña de madera, con puerta roja y dos ventanas redondas, puedes dibujarla en tu mente o en una hoja. Las palabras que más ayudan son adjetivos de color, tamaño y forma, y las preposiciones de lugar (at the top of, next to, under).",
        "Un organizador gráfico (graphic organizer) es un esquema que ordena la información. Una cadena de secuencia (sequence chain) pone los pasos en orden: 1, 2, 3. Una red de ideas (idea web) pone el tema en el centro y los detalles alrededor. Una tabla de causa y efecto (cause-effect table) tiene dos columnas: ¿qué pasó? y ¿por qué?. Cada organizador sirve para un tipo de texto.",
        "Elige el organizador según el texto. Si hay pasos, usa una secuencia. Si hay un tema con varios datos, usa una red. Si hay razones y consecuencias, usa una tabla. Escribe solo palabras clave, no oraciones completas. Después de completarlo, compáralo con el texto: ¿está todo lo importante? ¿sobra algún dato?",
    ],
    [("visualize", "visualizar: imaginar una imagen"), ("graphic organizer", "organizador gráfico"), ("sequence chain", "cadena de secuencia"), ("idea web", "red de ideas"), ("cause-effect table", "tabla de causa y efecto"), ("detail", "detalle")],
    [
        ("Visualizar una descripción", READ + HOUSE + " ¿De qué color es la puerta y cuántas ventanas tiene la casa?", ["Imagino la casa.", "Busco la puerta: a red door.", "Busco las ventanas: two round windows."], "La puerta es roja y tiene dos ventanas redondas"),
        ("Elegir un organizador", READ + STEPS + " ¿Qué organizador sirve mejor para este texto?", ["El texto tiene pasos en orden.", "Los pasos usan first, then, next y finally.", "La cadena de secuencia ordena pasos."], "Una cadena de secuencia"),
    ],
    [
        ("Llenar el organizador con oraciones largas.", "Se copia el texto.", "Usa solo palabras clave."),
        ("Usar una red de ideas para unos pasos.", "No se elige el organizador por el tipo de texto.", "Los pasos van en una cadena de secuencia."),
    ],
    [
        # rec
        (READ + HOUSE + " ¿Dónde está la casa? a) en la cima de un cerro verde b) junto al mar", "a) en la cima de un cerro verde", "Dice at the top of a green hill."),
        (READ + HOUSE + " ¿Qué animal duerme bajo el árbol? a) un gato gris b) un perro negro", "a) un gato gris", "Dice a gray cat sleeps under the tree."),
        (READ + STEPS + " ¿Qué se usa para limpiar la bicicleta? a) una esponja y jabón b) una escoba", "a) una esponja y jabón", "Dice clean it with a sponge and soap."),
    ],
    [
        # und
        (READ + HOUSE + " ¿Cuál de estos dibujos corresponde al texto? a) casa de madera con puerta roja, dos ventanas redondas y un árbol alto al lado b) casa de ladrillo con puerta azul y sin árboles", "a) casa de madera con puerta roja, dos ventanas redondas y un árbol alto al lado", "Coincide con todos los detalles del texto."),
        (READ + STEPS + " ¿Cuál es el tercer paso de la cadena de secuencia? a) limpiar con esponja y jabón b) enjuagar", "a) limpiar con esponja y jabón", "Los pasos son sacar, mojar, limpiar, enjuagar y secar."),
        ("¿Qué organizador usarías para un texto con un tema en el centro y cuatro datos alrededor? a) una red de ideas b) una cadena de secuencia", "a) una red de ideas", "La red pone el tema en el centro."),
    ],
    [
        # app
        (READ + STEPS + " ¿Cuántos pasos tendría la cadena de secuencia?", "5", "Son sacar la bicicleta, mojar, limpiar, enjuagar y secar."),
        (READ + STEPS + " ¿Qué paso va después de enjuagar? a) secar b) mojar", "a) secar", "Finally, dry it with a cloth."),
        (READ + "«Because it rained all night, the river rose. So the road was closed.» (rained = llovió, river = río, rose = subió, road = camino, closed = cerrado). Completa la tabla de causa y efecto: ¿cuál es el efecto final? a) el camino se cerró b) llovió toda la noche", "a) el camino se cerró", "Llover es la causa y cerrar el camino es el efecto."),
    ],
    [
        # rea
        (READ + HOUSE + " Un estudiante dibuja un perro negro bajo el árbol. ¿Qué frase del texto lo corrige? a) a gray cat sleeps under the tree b) a red door and two round windows", "a) a gray cat sleeps under the tree", "El texto dice que bajo el árbol duerme un gato gris."),
        (READ + STEPS + " Un compañero pone «secar» antes de «enjuagar» en su cadena. ¿Qué palabras del texto muestran el error? a) After that, rinse it; Finally, dry it b) First, take the bike outside", "a) After that, rinse it; Finally, dry it", "After that y Finally marcan el orden correcto."),
    ],
    [
        # cha
        (READ + "«The match was cancelled because of the storm. As a result, the students stayed at home.» (cancelled = cancelado, storm = tormenta, because of = a causa de, as a result = como resultado). ¿Qué columna de una tabla de causa y efecto completas con the storm? a) la causa b) el efecto", "a) la causa", "La tormenta explica por qué se canceló."),
        ("Un organizador de tema con un círculo central y cuatro ramas se llama: a) red de ideas b) tabla de causa y efecto", "a) red de ideas", "Pone el tema en el centro."),
    ],
    [
        # context
        (READ + "«My room has a blue bed under the window. A brown desk is next to the bed. A lamp is on the desk, and a poster is above the bed.» (bed = cama, desk = escritorio, lamp = lámpara, poster = afiche, above = encima de). ¿Qué objeto está sobre el escritorio? a) una lámpara b) un afiche", "a) una lámpara", "Dice A lamp is on the desk.")
    ],
    [
        # selfcheck
        ("¿Qué significa visualizar?", "Imaginar una imagen de lo que leo", "Ayuda a comprender y recordar."),
        ("¿Para qué sirve una cadena de secuencia?", "Para ordenar pasos", "Pone cada paso en orden."),
        ("¿Qué escribes en un organizador?", "Palabras clave", "No se copian oraciones completas."),
    ],
    task("Lee este texto: «To make a fruit salad: first, wash the fruit. Second, ask an adult to cut it. Next, put the pieces in a bowl. Then add orange juice. Finally, mix and serve.» (wash = lavar, cut = cortar, pieces = trozos, bowl = bol, serve = servir). En tu hoja dibuja una cadena de secuencia con cinco cuadros y escribe en cada uno una palabra clave. Escribe también por qué elegiste ese organizador.", "Cuadros: 1 lavar fruta; 2 cortar (adulto); 3 poner en bol; 4 agregar jugo; 5 mezclar y servir. Elegí una cadena de secuencia porque el texto tiene pasos en orden.", ["incluye los cinco pasos en orden", "usa palabras clave", "justifica el organizador elegido"], ["dibujo de la cadena", "nota del adulto"], ["poner los pasos en desorden", "copiar oraciones completas"], "Reconoce lo que acertó y relee con la persona first, second, next, then y finally para ordenar."),
    "Dibuja lo que imaginas al leer el texto de la casa y compara con una persona de tu casa.",
    "Escribe en español qué organizador gráfico usarías para estudiar un texto con causas y consecuencias y por qué.",
)

# ---------------------------------------------------------------- clase 4: después de leer — confirmar, releer y preguntar
WATER = "Título: «Save Water at Home». Subtítulo 1: «In the bathroom». Texto: «Close the tap while you brush your teeth. Take showers of five minutes or less.» Subtítulo 2: «In the kitchen». Texto: «Wash vegetables in a bowl, not under running water. Use that water for your plants.» (save = ahorrar, tap = llave, brush = cepillar, showers = duchas, bowl = bol, running = corriendo, plants = plantas)"

lesson(
    OA6, 4,
    "El texto escrito en cada ejercicio y lápiz.",
    "Aprenderé estrategias para después de leer: confirmar mis predicciones, releer cuando tengo una duda y hacer preguntas para comprobar la información. Sirve para asegurarme de que entendí bien el texto.",
    ["Sé hacer predicciones antes de leer.", "Conozco preguntas con what, how y why."],
    [
        "Después de leer (post-reading), comprueba lo que entendiste. Primero, confirma tus predicciones: ¿lo que esperabas apareció? Si sí, la confirmaste. Si no, la corriges y escribes qué aprendiste. Puedes decir: «I predicted… and the text says…». Eso te enseña a predecir mejor la próxima vez.",
        "Segundo, relee (reread) las partes que no entendiste. Volver a leer no es un fracaso: es una estrategia. Relee solo el párrafo o la oración que tiene la duda, con un lápiz en la mano, y subraya las palabras clave. Tercero, haz preguntas para confirmar información (ask questions to confirm): «Does the text say that…?», «Is it true that…?», «Where does it say…?». Responde con una frase del texto.",
        "Un buen cierre de lectura es escribir una oración que diga lo más importante y marcar una duda pendiente. Si la duda no se resuelve releyendo, pregunta a otra persona. En el texto sobre el ahorro de agua, por ejemplo, puedes preguntar: «Is it true that showers should last five minutes or less?». La respuesta está en el texto.",
    ],
    [("post-reading", "después de leer"), ("confirm", "confirmar: comprobar que algo es cierto"), ("reread", "releer"), ("question", "pregunta"), ("evidence", "evidencia: la frase que lo prueba"), ("doubt", "duda")],
    [
        ("Confirmar una predicción", READ + WATER + " Predijiste oír la palabra shower. ¿Se confirmó? ¿Cuántos minutos se recomienda como máximo?", ["Busco shower en el texto.", "Aparece showers of five minutes or less.", "El máximo es cinco minutos."], "Sí, se confirmó; el máximo es 5 minutos"),
        ("Preguntar para confirmar", READ + WATER + " Pregunta: «Is it true that we should wash vegetables under running water?» ¿Cuál es la respuesta con evidencia?", ["Busco wash vegetables.", "Dice in a bowl, not under running water.", "La respuesta es no."], "No: el texto dice que se lavan en un bol, no con agua corriendo"),
    ],
    [
        ("Dar por buena una predicción sin comprobarla.", "No se compara con el texto.", "Busca en el texto una frase que la confirme o la corrija."),
        ("Responder una pregunta sin dar evidencia.", "Se contesta de memoria.", "Cita la frase del texto que lo prueba."),
    ],
    [
        # rec
        (READ + WATER + " ¿Qué hay que hacer mientras te cepillas los dientes? a) cerrar la llave b) dejar correr el agua", "a) cerrar la llave", "El texto dice Close the tap."),
        (READ + WATER + " ¿Qué se hace con el agua del bol? a) se usa para regar las plantas b) se bota por el desagüe", "a) se usa para regar las plantas", "El texto dice Use that water for your plants."),
        (READ + WATER + " ¿Cuántos minutos como máximo debe durar una ducha? a) cinco b) quince", "a) cinco", "Dice of five minutes or less."),
    ],
    [
        # und
        (READ + WATER + " Predijiste que habría un consejo para la cocina. ¿Se cumplió? a) sí, en In the kitchen b) no", "a) sí, en In the kitchen", "El subtítulo In the kitchen lo confirma."),
        (READ + WATER + " ¿Qué pregunta sirve para confirmar un dato del baño? a) Is it true that the tap should be closed? b) Where is the bus stop?", "a) Is it true that the tap should be closed?", "Se relaciona con el texto del baño."),
        (READ + WATER + " ¿Qué parte relees si dudas sobre las verduras? a) In the kitchen b) In the bathroom", "a) In the kitchen", "Es la parte que menciona vegetables."),
    ],
    [
        # app
        (READ + WATER + " ¿Cuál es la respuesta a «Does the text say that we should take long showers»? a) No, it says five minutes or less b) Yes, it says twenty minutes", "a) No, it says five minutes or less", "La evidencia es showers of five minutes or less."),
        (READ + WATER + " Pregunta: «Where does it say to close the tap?» ¿Cuál es la parte del texto? a) In the bathroom b) In the kitchen", "a) In the bathroom", "La frase está bajo ese subtítulo."),
        (READ + WATER + " ¿Cuántos consejos hay en total en el texto?", "4", "Hay cuatro consejos."),
    ],
    [
        # rea
        (READ + WATER + " Un compañero dice que el texto aconseja lavar verduras bajo el agua corriendo. ¿Qué haces? a) relees la sección de la cocina y lo corriges con evidencia b) le crees sin comprobar", "a) relees la sección de la cocina y lo corriges con evidencia", "El texto dice not under running water."),
        (READ + WATER + " Después de leer, anotas «Duda: ¿por qué ahorrar agua?». ¿Qué haces? a) buscas otra fuente o preguntas a alguien b) borras la duda", "a) buscas otra fuente o preguntas a alguien", "El texto no explica el por qué."),
    ],
    [
        # cha
        (READ + WATER + " ¿Qué pregunta de confirmación sirve para el consejo de la cocina? a) Is it true that the water from the bowl can be used for plants? b) Do showers cost five pesos?", "a) Is it true that the water from the bowl can be used for plants?", "Confirma un dato del texto."),
        ("Escribe la frase en inglés que usarías para decir «Predije… y el texto dice…».", "I predicted… and the text says…", "Es la frase para confirmar una predicción."),
    ],
    [
        # context
        (READ + "Antes de leer un afiche de reciclaje, predijiste que hablaría de plástico y papel. El afiche dice: «Put paper in the blue bin and glass in the green bin». ¿Qué parte de tu predicción se cumplió? a) papel b) plástico", "a) papel", "El afiche nombra paper, pero no plástico.")
    ],
    [
        # selfcheck
        ("¿Qué haces con una predicción después de leer?", "La confirmo o la corrijo", "Se compara con el texto."),
        ("¿Qué haces si no entiendes un párrafo?", "Lo releo", "Releer es una estrategia."),
        ("¿Qué es la evidencia?", "La frase del texto que prueba mi respuesta", "Sostiene lo que digo."),
    ],
    task("Lee este texto: «Title: Books at School. The library opens at eight. Students can borrow two books for two weeks. If a book is late, students pay a small fine. Silent reading is every Wednesday.» (borrow = pedir prestado, late = atrasado, fine = multa, silent reading = lectura silenciosa). Antes de leer, escribe una predicción. Después, escribe dos preguntas con Is it true that… para confirmar datos y responde con evidencia.", "Predicción: biblioteca y libros. Pregunta 1: Is it true that students can borrow two books? Sí, two books for two weeks. Pregunta 2: Is it true that silent reading is on Friday? No, es every Wednesday.", ["escribe una predicción", "formula dos preguntas de confirmación", "responde con evidencia"], ["hoja con predicción, preguntas y respuestas", "nota del adulto"], ["no dar evidencia", "preguntar sobre algo que no está en el texto"], "Reconoce lo que acertó y relee con la persona la frase que prueba cada respuesta."),
    "Relee el texto del agua y escribe una pregunta con Is it true that… y su respuesta.",
    "Escribe en español qué haces tú cuando no entiendes una parte de un texto en inglés.",
)

# ---------------------------------------------------------------- clase 5: resumir con apoyo
BEE2 = "«Bees are small insects that live in colonies. They visit flowers to collect nectar and pollen. They carry pollen from flower to flower, and this helps plants make fruit. Without bees, there would be less fruit. Pesticides can harm bees, so some cities plant flowers without them.»"
DIARY = "«Friday, 5 p.m. Today we planted six tomato seeds in the school garden. We watered them and put a sign with our names. Our teacher said that the plants will be ready in three months. I am very excited!» (planted = plantamos, seeds = semillas, watered = regamos, sign = letrero, ready = listas, excited = emocionado)"

lesson(
    OA6, 5,
    "Los textos y los marcos de resumen escritos en cada ejercicio y lápiz.",
    "Aprenderé a resumir un texto con apoyo, usando un marco de frases y organizadores. Sirve para explicar a otra persona, con pocas palabras, lo más importante de lo que leí.",
    ["Sé identificar la idea principal.", "Conozco first, then y in the end."],
    [
        "Un resumen (summary) cuenta la idea principal de un texto con tus palabras, sin copiar frases y sin datos menores. Para hacerlo con apoyo, usa un marco: «The text is about… First, … Then, … In the end, …». También puedes completar un organizador con las palabras clave y luego unirlas en dos o tres oraciones.",
        "Para elegir qué incluir, pregúntate: ¿esta información es esencial? Si la quito y la idea principal sigue clara, no va en el resumen. En el texto de las abejas, «viven en colonias» es un dato de apoyo, mientras que «ayudan a las plantas a producir fruta» es la idea principal. Un resumen suele tener entre dos y tres oraciones.",
        "Después de escribir, relee tu resumen y compáralo con el texto: ¿dice lo mismo en menos palabras? ¿usa tus palabras? ¿mantiene el orden de las ideas? Pide a otra persona que lo lea: si entiende de qué trata el texto, el resumen funciona. Si falta algo importante, agrégalo; si sobra un detalle, quítalo.",
    ],
    [("summary", "resumen"), ("main idea", "idea principal"), ("supporting detail", "detalle de apoyo"), ("frame", "marco de frases"), ("in the end", "al final"), ("own words", "con tus propias palabras")],
    [
        ("Completar un marco de resumen", READ + DIARY + " Completa: «The text is about… First…, in the end…».", ["Tema: plantar tomates en el huerto del colegio.", "Primero plantaron semillas y las regaron.", "Al final pusieron un letrero y esperarán tres meses."], "El texto trata de plantar tomates en el huerto: primero plantaron y regaron las semillas; al final pusieron un letrero y esperarán tres meses"),
        ("Elegir la idea principal", READ + BEE2 + " ¿Cuál es la idea principal? Elige: Bees help plants make fruit / Bees live in colonies.", ["Busco la idea más importante.", "El texto dice que llevan polen y ayudan a las plantas a hacer fruta.", "Vivir en colonias es un dato de apoyo."], "Bees help plants make fruit"),
    ],
    [
        ("Copiar frases enteras del texto.", "Se cree que un resumen es un recorte del original.", "Dilo con tus palabras y quita los detalles menores."),
        ("Incluir todos los detalles.", "No se distingue lo esencial.", "Si sin ese dato la idea es clara, no lo incluyas."),
    ],
    [
        # rec
        (READ + DIARY + " ¿Cuántas semillas plantaron? a) seis b) diez", "a) seis", "Dice six tomato seeds."),
        (READ + BEE2 + " ¿Qué llevan las abejas de flor en flor? a) polen b) agua", "a) polen", "El texto dice They carry pollen."),
        (READ + DIARY + " ¿Cuánto falta para que las plantas estén listas? a) tres meses b) tres días", "a) tres meses", "La profesora dice ready in three months."),
    ],
    [
        # und
        (READ + BEE2 + " ¿Qué dato es un detalle de apoyo? a) Bees live in colonies b) Bees help plants make fruit", "a) Bees live in colonies", "Es información secundaria sobre las abejas."),
        (READ + DIARY + " ¿Cuál es el mejor resumen? a) Plantaron tomates en el huerto y esperan tres meses b) Hoy es viernes a las cinco", "a) Plantaron tomates en el huerto y esperan tres meses", "Contiene lo esencial."),
        (READ + BEE2 + " ¿Qué solución se propone para ayudar a las abejas? a) plantar flores sin pesticidas b) construir colmenas de metal", "a) plantar flores sin pesticidas", "El texto dice some cities plant flowers without them."),
    ],
    [
        # app
        (READ + BEE2 + " Ordena para un resumen. A) Cities plant flowers without pesticides. B) Bees carry pollen. C) Plants make fruit. D) Pesticides can harm bees.", "B, C, D, A", "Primero llevan polen, así las plantas hacen fruta; luego los pesticidas las dañan y las ciudades plantan flores sin ellos."),
        (READ + DIARY + " ¿Qué detalle se puede dejar fuera del resumen? a) que eran las cinco de la tarde b) que plantaron semillas", "a) que eran las cinco de la tarde", "La hora es un detalle menor."),
        (READ + BEE2 + " ¿Cuál es el efecto de que no haya abejas? a) habría menos fruta b) habría más flores", "a) habría menos fruta", "El texto dice Without bees, there would be less fruit."),
    ],
    [
        # rea
        (READ + BEE2 + " Un compañero resume: «Bees are small insects». ¿Qué le falta? a) la idea principal, que ayudan a las plantas b) el nombre del autor", "a) la idea principal, que ayudan a las plantas", "Su resumen es solo un dato inicial."),
        (READ + DIARY + " ¿Qué sentimiento transmite el diario? a) emoción b) tristeza", "a) emoción", "El autor dice I am very excited."),
    ],
    [
        # cha
        (READ + BEE2 + " ¿Cuál es el mejor resumen con las palabras bees, plants y fruit? a) Las abejas ayudan a las plantas a hacer fruta b) Las plantas son verdes", "a) Las abejas ayudan a las plantas a hacer fruta", "Resume la idea principal del texto."),
        (READ + DIARY + " ¿Cuántas oraciones tiene un buen resumen de este texto? a) dos o tres b) diez", "a) dos o tres", "Un resumen es breve."),
    ],
    [
        # context
        (READ + "«Last Saturday, the class painted a mural on the school wall. Twenty students worked for four hours. They used blue, yellow and green paint. The mural shows a big tree with birds.» (mural = mural, wall = muro, paint = pintura, birds = pájaros). ¿Cuál es el mejor resumen? a) La clase pintó un mural de un árbol con pájaros b) El mural usa pintura", "a) La clase pintó un mural de un árbol con pájaros", "Incluye quién y qué hicieron.")
    ],
    [
        # selfcheck
        ("¿Cuánto debe medir un buen resumen?", "Dos o tres oraciones", "Es breve y claro."),
        ("¿Qué marco de resumen empieza con «The text is about»?", "The text is about… First… Then… In the end…", "Ordena las ideas."),
        ("¿Qué haces con un detalle menor?", "Lo dejo fuera del resumen", "No cambia la idea principal."),
    ],
    task("Lee este texto: «The school choir sang at the town square on Sunday. Thirty students performed five songs. Many neighbors came to listen, and the mayor thanked the students. The choir will sing again in December.» (choir = coro, town square = plaza, performed = presentaron, neighbors = vecinos, mayor = alcalde, thanked = agradeció). Escribe un resumen de dos oraciones usando el marco The text is about… First… In the end…", "The text is about the school choir. First, thirty students sang five songs in the square; in the end, the mayor thanked them and they will sing again in December.", ["usa el marco", "incluye la idea principal", "deja fuera detalles menores"], ["hoja con resumen", "nota del adulto"], ["copiar frases enteras", "incluir todos los números"], "Reconoce lo que acertó y relee con la persona qué detalles se pueden quitar sin perder la idea."),
    "Lee de nuevo el texto de las abejas y escribe un resumen de una oración con tus propias palabras.",
    "Escribe en español cuál es la diferencia entre la idea principal y un detalle de apoyo.",
)
