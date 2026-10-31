"""Student material for 5.º básico Inglés (propuesta), EN05 OA 07 (estrategias de lectura) y OA 08 (respuesta a lo leído).

Todos los textos de lectura son originales y están escritos en el propio enunciado. Cada palabra nueva lleva su pista en español.
Las respuestas multimodales (dibujo, organizador, dramatización, exposición, párrafo) se practican con textos y plantillas escritos aquí.
"""
from __future__ import annotations

from student_content_en5_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA7 = "EN05 OA 07"
OA8 = "EN05 OA 08"

TREE = "Título: «Why Do Some Trees Lose Their Leaves?». Imagen: un árbol con hojas rojas y amarillas junto a otro árbol sin hojas."
BAKER = "«Mr. Torres is a baker. He gets up at four in the morning. He makes bread, buns and cakes in his small shop. At seven, the first customers arrive. At noon he closes the shop and goes home to rest.» (baker = panadero, gets up = se levanta, buns = bollos, customers = clientes, noon = mediodía, rest = descansar)"
POOL = "«Sunny Pool. Opening hours: Monday to Friday, 9:00 to 18:00. Saturday and Sunday, 10:00 to 16:00. Prices: adults, 3.000 pesos; children from 5 to 12 years, 1.500 pesos; children under 5, free. Swimming lessons: Tuesday and Thursday at 17:00.» (opening hours = horario, prices = precios, adults = adultos, under = menores de, free = gratis, lessons = clases)"
ROOM = "«My room is small. A red chair is next to the window. A lamp is on the table. A cat sleeps under the table. Two pictures are on the wall above my bed.» (lamp = lámpara, under = debajo de, above = sobre, wall = pared, bed = cama)"
BOX = "«Lucas has a magic box. It is old and blue. First, he puts a coin in the box. Then he says: abracadabra! After that, the box shows a surprise: three paper birds fly out. The children clap and shout: again!» (magic = mágica, coin = moneda, surprise = sorpresa, paper = de papel, fly out = salen volando, clap = aplauden, again = otra vez)"
KITE = "«The Kite Contest. Every year, the town of Valle Alto has a kite contest. This year, Rita makes a big yellow kite with a long tail. She is nervous because the wind is weak. At first, her kite does not fly. Then the wind grows stronger and the kite goes up high. Rita wins the prize for the highest kite.» (contest = concurso, tail = cola, nervous = nerviosa, weak = débil, grows stronger = se hace más fuerte, goes up high = sube alto, prize = premio, highest = más alto)"
MARIO = "«Mario loves animals. Last Sunday, he saw a lost puppy near the school. The puppy was cold and hungry. Mario gave it water and some bread. Then he took it to a vet. The vet found the owner. Mario felt very happy.» (puppy = cachorro, vet = veterinario, found = encontró, owner = dueño, felt = se sintió)"

MOON = "«The Moon. The Moon goes around the Earth. It shines at night because it reflects the light of the Sun. People can see its changes: new moon, half moon and full moon.» (goes around = gira alrededor de, reflects = refleja, changes = cambios)"
SCHED = "«Class schedule. Monday: Math 8:30, English 10:00. Tuesday: Art 9:00, Science 11:00. Wednesday: English 9:00, PE 12:00.» (schedule = horario, PE = educación física)"
KITCHEN = "«The kitchen is bright. There is a round table in the center. Three chairs are around the table. A fruit bowl is on the table. A clock is on the wall.» (bright = luminosa, round = redonda, center = centro, fruit bowl = frutero, clock = reloj)"
GARDEN = "«The class plants a garden. On Monday, they buy seeds. On Tuesday, they dig the soil. On Wednesday, they plant the seeds and water them.» (plants = planta, seeds = semillas, dig = cavan, soil = tierra, water = riegan)"

# ================================================================ OA 07
lesson(
    OA7, 1,
    "Los títulos, imágenes y textos descritos en cada ejercicio, y lápiz.",
    "Aprenderé a prepararme antes de leer: fijar un propósito, hacer predicciones y usar lo que ya sé. Sirve para leer con más atención y entender mejor.",
    ["Sé que el título y las imágenes dan pistas.", "Conozco palabras como tree, leaves, red y yellow."],
    [
        "Antes de leer (pre-reading) puedes hacer tres cosas. Primera, leer con un propósito (purpose): decidir qué quieres saber, por ejemplo «quiero saber por qué algunos árboles pierden sus hojas». Segunda, hacer predicciones (predictions): imaginar de qué hablará el texto a partir del título y la imagen. Tercera, recordar lo que ya sabes (prior knowledge).",
        "Mira el título «Why Do Some Trees Lose Their Leaves?» (¿por qué algunos árboles pierden sus hojas?) y la imagen de árboles con hojas rojas y amarillas. Puedes predecir que el texto hablará del otoño y del frío. Tu conocimiento previo de Ciencias dice que en otoño las hojas cambian de color y caen. Con esto, tu lectura será más activa.",
        "Escribe tu propósito como una pregunta con why, what, how o when. Una buena pregunta es corta y se puede responder con el texto. Después de leer, compararás: ¿mi predicción fue correcta? Si no, la corriges. Hacer esto antes de leer no toma más de un minuto.",
    ],
    [("pre-reading", "antes de leer"), ("purpose", "propósito"), ("prediction", "predicción"), ("prior knowledge", "lo que ya sé"), ("autumn", "otoño"), ("leaves", "hojas")],
    [
        ("Predecir", TREE + " ¿De qué estación del año crees que hablará el texto?", ["Miro la imagen: hojas rojas y amarillas.", "Recuerdo que las hojas cambian de color en otoño.", "Predigo que habla del otoño."], "Del otoño"),
        ("Propósito", "Para el mismo texto, ¿cuál es una buena pregunta de propósito? a) Why do some trees lose their leaves? b) What is your name?", ["El propósito se relaciona con el título.", "La opción a) usa las palabras del título.", "La b) no se relaciona."], "a)"),
    ],
    [
        ("Empezar a leer sin pensar en el título.", "Se pierde una pista importante.", "Lee el título y mira las imágenes antes de leer."),
        ("Predecir algo que no se relaciona con el título.", "La predicción no se apoya en pistas.", "Una predicción debe tener una razón, como una palabra del título."),
    ],
    [
        ("Título: «A Day at the Zoo». Imagen: una jirafa y un elefante. ¿Qué predices? a) animales b) autos", "a) animales", "La imagen muestra animales."),
        ("¿Qué es el propósito de lectura?", "Lo que quiero saber al leer", "El propósito guía la lectura."),
        ("Título: «How to Make Pancakes». ¿Qué tipo de texto predices? a) instrucciones b) un poema", "a) instrucciones", "How to... anuncia pasos."),
    ],
    [
        ("Antes de leer «How Do Bees Make Honey?» (¿cómo hacen miel las abejas?), elige un conocimiento previo útil: a) Las abejas visitan flores b) La luna es redonda", "a)", "Las abejas y las flores se relacionan con la miel."),
        ("Título: «The Biggest Fish». ¿Qué pregunta de propósito sirve? a) How big is the biggest fish? b) Where is my pencil?", "a)", "La pregunta se relaciona con el título."),
        ("Predijiste que el texto «Winter Games» (juegos de invierno) habla de nieve. ¿En qué te apoyas?", "En la palabra winter", "Winter indica la estación fría."),
    ],
    [
        ("Título: «Penguins in the Snow». Imagen: pingüinos en el hielo. ¿Qué conocimiento previo te ayuda? a) Muchos pingüinos viven cerca de mares fríos b) Los pingüinos viven en la selva", "a)", "Se relaciona con la nieve y el hielo de la imagen."),
        ("Título: «How to Build a Sandcastle» (castillo de arena). ¿Qué propósito de lectura es adecuado? a) Learn the steps to build it b) Find a phone number", "a)", "El título anuncia instrucciones."),
        ("Antes de leer «A Rainy Day», ¿qué predicción es razonable? a) Habrá paraguas y charcos b) Habrá playa y calor", "a)", "Rainy se relaciona con lluvia."),
    ],
    [
        ("Un compañero predice que «Soccer Day» (día de fútbol) habla de un viaje en barco. ¿Es una buena predicción? ¿Por qué?", "No; soccer es fútbol y no se relaciona con barcos", "Una predicción debe apoyarse en el título."),
        ("Antes de leer «The Water Cycle» (el ciclo del agua), ¿qué sabes por Ciencias? a) El agua sube, forma nubes y cae como lluvia b) El agua no cambia", "a)", "Ese es el conocimiento previo correcto."),
    ],
    [
        ("Título: «The Rainforest». Escribe una pregunta de propósito con what: a) What animals live in the rainforest? b) What time is it? (rainforest = selva)", "a)", "La pregunta se relaciona con el título."),
        ("Predices que el texto «The Space Trip» (el viaje al espacio) hablará de cohetes. ¿Qué palabra en inglés puede aparecer? a) rocket b) kitchen", "a) rocket", "Rocket es cohete y se relaciona con el espacio."),
    ],
    [("Antes de leer una noticia con el titular «New Park Opens in Town» (abre un nuevo parque en el pueblo), ¿qué predices? a) habla de un parque nuevo b) habla de una película", "a)", "El titular nombra un parque nuevo.")],
    [
        ("¿Qué tres cosas haces antes de leer?", "Fijar un propósito, predecir y recordar lo que sé", "Preparan la lectura."),
        ("¿Qué significa «prior knowledge»?", "Lo que ya sé", "Es el conocimiento anterior."),
        ("¿Qué miras para predecir?", "El título y las imágenes", "Dan pistas del tema."),
    ],
    task("Mira este título e imagen: «A Visit to the Farm». Imagen: un granero rojo, tres vacas y un tractor. Escribe tu propósito como pregunta en inglés (con what, how many o where), tres palabras que predices encontrar y una cosa que ya sabes sobre las granjas.", "Propósito: How many cows are there? Predicción: cow, farmer, tractor. Ya sé que en las granjas hay animales.", ["pregunta en inglés", "tres palabras coherentes", "un conocimiento previo"], ["hoja con respuestas", "nota del adulto"], ["predecir palabras que no se relacionan", "olvidar el propósito"], "Reconoce lo bien hecho y relee con él el título para mejorar la predicción."),
    "Mira la portada de un libro que tengas en casa, lee su título y di en voz alta de qué crees que trata.",
    "Elige un título de un libro que conozcas y escribe una predicción y una pregunta de propósito.",
)

lesson(
    OA7, 2,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a hacer una lectura rápida (skimming) para saber de qué trata un texto sin leerlo todo. Sirve para decidir si un texto me sirve y entender la idea general.",
    ["Sé identificar el título y la primera oración.", "Conozco palabras como baker, bread y shop."],
    [
        "La lectura rápida (skimming) significa pasar la vista por el texto para captar la idea general. No leas cada palabra. Mira primero el título, la primera oración y la última, y las palabras que se repiten o destacan. Con eso sabes de qué trata el texto en menos de un minuto.",
        "Practica con el texto del panadero. El título habla de un panadero; la primera oración dice «Mr. Torres is a baker». Las palabras bread, buns, cakes y shop destacan y muestran el tema. Con este vistazo ya sabes que el texto cuenta el trabajo de un panadero. No necesitas saber a qué hora llegan los clientes.",
        "La lectura rápida responde a: ¿de qué trata? y ¿qué tipo de texto es? Es útil para elegir un libro, para buscar un texto en un tema o para saber si un artículo tiene la información que necesitas. Después, si el texto te sirve, lo lees con más calma.",
    ],
    [("skimming", "lectura rápida"), ("main idea", "idea general"), ("first sentence", "primera oración"), ("repeated words", "palabras repetidas"), ("baker", "panadero"), ("shop", "tienda")],
    [
        ("Idea general con skimming", "Hojea este texto: " + BAKER + " ¿De qué trata en general?", ["Miro la primera oración: Mr. Torres is a baker.", "Veo bread, buns y cakes juntos.", "Trata del trabajo de un panadero."], "Del trabajo de un panadero"),
        ("Palabras del mismo tema", "En el mismo texto, ¿qué palabras de comida aparecen? ¿Cuántas?", ["Busco bread, buns y cakes.", "Son tres.", "El texto habla de tres productos de panadería."], "3: bread, buns y cakes"),
    ],
    [
        ("Leer palabra por palabra cuando solo se quiere la idea general.", "Se pierde tiempo y se pierde la visión del conjunto.", "En skimming mira título, primera oración y palabras repetidas."),
        ("Usar skimming para buscar la hora exacta de un dato.", "Para un dato específico se necesita otra estrategia.", "Para un dato concreto usa la lectura focalizada (scanning)."),
    ],
    [
        ("¿Qué miras primero en la lectura rápida?", "El título y la primera oración", "Dan la idea general."),
        ("Lee solo el título: «Pets at Home». ¿De qué crees que trata? a) de mascotas b) de autos", "a) de mascotas", "Pets son mascotas."),
        ("¿Para qué sirve el skimming? a) Para saber de qué trata un texto b) Para encontrar la hora exacta", "a)", "Skimming da la idea general."),
    ],
    [
        ("Hojea: «My Pets. These are my pets. I have a dog, a cat and two rabbits. They live in a house near the park.» (rabbits = conejos, house = casa). ¿De qué trata?", "De sus mascotas", "El título y la primera oración lo dicen."),
        ("Hojea: «The Planets. There are eight planets in our solar system. The Earth is the third planet from the Sun. Jupiter is the biggest.» (solar system = sistema solar). ¿Qué tema común hay en las oraciones?", "Los planetas", "Todas nombran planetas."),
        ("Hojea: «Mr. Torres is a baker. He gets up at four.» ¿Qué tipo de trabajo tiene? a) hace pan b) arregla autos", "a)", "Baker es panadero."),
    ],
    [
        ("Hojea: " + MOON + " ¿Cuál es la idea general?", "La Luna y sus cambios", "El título y las oraciones hablan de la Luna."),
        ("En el texto de la Luna, ¿qué palabra se repite más? a) Moon b) Sun", "a) Moon", "Moon aparece en el título y en varias oraciones."),
        ("Hojea: «Sports Day. Today is Sports Day at our school. There are races, jumping games and a football match.» (races = carreras). ¿De qué trata?", "Del día de deportes del colegio", "Título y primera oración lo dicen."),
    ],
    [
        ("Un compañero dice que para saber de qué trata el texto del panadero debe leer cada palabra. ¿Es verdad?", "No; basta mirar el título, la primera oración y las palabras repetidas", "Eso es skimming."),
        ("Para el texto del panadero, ¿qué dato NO necesitas para la idea general? a) la hora a la que llegan los clientes b) que es panadero", "a)", "Es un detalle que no cambia la idea general."),
    ],
    [
        ("Hojea: «School Rules. Rule 1: Arrive on time. Rule 2: Wear your uniform. Rule 3: Be kind.» (rules = reglas, uniform = uniforme, kind = amable). ¿Cuántas reglas aparecen?", "3", "Hay Rule 1, Rule 2 y Rule 3."),
        ("¿De qué trata el texto «School Rules»? a) de las normas de un colegio b) de un partido", "a)", "Rules son normas y school es colegio."),
    ],
    [("Quieres un texto sobre dinosaurios. Ves dos títulos: «Dinosaur Facts» y «Cooking Pasta». ¿Cuál eliges?", "Dinosaur Facts", "El título anuncia el tema que buscas.")],
    [
        ("¿Qué significa «skimming»?", "Lectura rápida", "Es leer para captar la idea general."),
        ("¿Qué palabras ayudan a captar la idea general?", "Las que se repiten", "Revelan el tema."),
        ("¿Qué lees primero en un texto?", "El título", "Orienta la lectura."),
    ],
    task("Hojea este texto durante un minuto: «The Library. Our school library has many books. There are books about animals, sports and space. Students can borrow two books each week. The library is a quiet place.» (borrow = pedir prestado, quiet = silencioso). Escribe de qué trata, qué palabras se repiten y qué tipo de texto crees que es.", "Trata de la biblioteca del colegio; se repite books; es un texto informativo.", ["idea general", "una palabra repetida", "tipo de texto"], ["hoja con respuestas", "nota del adulto"], ["leer sin parar para encontrar datos", "decir que es un cuento"], "Reconoce lo bien captado y practica con él mirando solo el título y la primera oración."),
    "Elige un libro que tengas, lee solo la portada y la primera frase y di de qué trata.",
    "Hojea el texto del panadero y escribe una frase en español con la idea general.",
)

lesson(
    OA7, 3,
    "El folleto escrito en cada ejercicio y lápiz.",
    "Aprenderé a hacer una lectura focalizada (scanning) para encontrar un dato específico, como una hora, un precio o un nombre. Sirve para encontrar rápido lo que necesito.",
    ["Sé leer horas como 9:00 y 17:00.", "Conozco palabras como prices, adults, children y free."],
    [
        "La lectura focalizada (scanning) es buscar un dato concreto con la vista, sin leer todo. Primero decide qué buscas: un número, un nombre o una palabra. Luego pasa la vista por el texto hasta encontrarlo. Es lo que haces cuando buscas un número en una lista de teléfonos.",
        "Los folletos, los horarios y las listas son ideales para scanning. En el folleto de la piscina, si buscas el precio para un niño de 8 años, busca la palabra children y fíjate en el número. Los datos suelen estar en números, nombres con mayúscula o palabras clave como prices, hours y lessons.",
        "Para no equivocarte, repite en tu mente lo que buscas. Cuando lo encuentres, lee la frase completa para confirmar. Por ejemplo, children from 5 to 12 years son 1.500 pesos, pero children under 5 es gratis. Una palabra pequeña, como under, cambia la respuesta.",
    ],
    [("scanning", "lectura focalizada"), ("opening hours", "horario de apertura"), ("prices", "precios"), ("adults / children", "adultos / niños"), ("under", "menores de"), ("free", "gratis")],
    [
        ("Encontrar un precio", "Lee: " + POOL + " ¿Cuánto paga un niño de 8 años?", ["Busco children from 5 to 12 years.", "8 está entre 5 y 12.", "Paga 1.500 pesos."], "1.500 pesos"),
        ("Encontrar un horario", "En el mismo folleto, ¿a qué hora abre el sábado?", ["Busco Saturday.", "Dice Saturday and Sunday, 10:00 to 16:00.", "Abre a las 10:00."], "A las 10:00"),
    ],
    [
        ("Leer todo el folleto para encontrar un dato.", "Se pierde tiempo.", "Decide el dato que buscas y pasa la vista hasta encontrarlo."),
        ("Ignorar la palabra under y decir que los niños de 4 años pagan 1.500 pesos.", "Se lee solo una parte.", "Under 5 significa menores de 5 y es gratis."),
    ],
    [
        ("Lee: " + POOL + " ¿A qué hora cierra el lunes?", "A las 18:00", "Dice Monday to Friday, 9:00 to 18:00."),
        ("Lee: " + POOL + " ¿Cuánto paga un adulto?", "3.000 pesos", "Dice adults, 3.000 pesos."),
        ("Lee: " + POOL + " ¿Qué días hay clases de natación? a) martes y jueves b) lunes y viernes", "a)", "Dice Tuesday and Thursday at 17:00."),
    ],
    [
        ("Lee: " + POOL + " ¿Cuánto paga un niño de 3 años?", "Nada; es gratis", "Under 5 es gratis."),
        arith("Lee: " + POOL + " Una familia con 2 adultos y 1 niño de 10 años quiere ir. ¿Cuánto pagan en total, en pesos?", "2*3000+1500", "Dos entradas de adulto más una de niño."),
        ("Lee: " + POOL + " ¿A qué hora empiezan las clases de natación?", "A las 17:00", "Dice lessons at 17:00."),
    ],
    [
        ("Lee: " + SCHED + " ¿A qué hora es la clase de Art?", "A las 9:00", "Dice Tuesday: Art 9:00."),
        ("En el horario, ¿qué día hay Science?", "El martes", "Dice Tuesday: Science 11:00."),
        ("En el horario, ¿cuántas clases de English hay en total?", "2", "Una el lunes a las 10:00 y otra el miércoles a las 9:00."),
    ],
    [
        ("Lee: " + POOL + " Una persona llega el domingo a las 17:00. ¿Está abierta la piscina?", "No", "El domingo cierra a las 16:00."),
        arith("Lee: " + POOL + " ¿Cuántas horas está abierta la piscina el sábado, de 10:00 a 16:00?", "16-10", "Se resta la hora de apertura a la de cierre."),
    ],
    [
        ("Lee: «Bus 12: 7:30, 8:15, 9:00. Bus 20: 7:45, 8:30, 9:15.» ¿A qué hora sale el primer Bus 20?", "7:45", "Es el primer horario de Bus 20."),
        ("En el mismo horario, ¿cuántos buses hay en total en la lista?", "6", "Hay tres horarios de Bus 12 y tres de Bus 20."),
    ],
    [("Buscas el teléfono de Ana en esta lista: «Ana: 5551, Beto: 5552, Carla: 5553.» ¿Cuál es?", "5551", "En la lista, Ana tiene el 5551.")],
    [
        ("¿Qué significa «scanning»?", "Lectura focalizada para encontrar un dato", "Busca un dato concreto."),
        ("¿Qué tipos de texto sirven para scanning?", "Folletos, horarios y listas", "Tienen datos concretos."),
        ("¿Qué haces cuando encuentras el dato?", "Leo la frase completa para confirmar", "Así evitas errores."),
    ],
    task("Lee este horario: «Zoo Tour. Tuesday: 10:00 and 14:00. Thursday: 10:00. Saturday: 11:00, 13:00 and 15:00. Price: 2.000 pesos per child.» (tour = visita guiada, per = por). Escribe a qué hora hay visitas el jueves, cuántas hay el sábado y cuánto pagan 3 niños.", "Jueves 10:00; el sábado hay 3 visitas; 3 niños pagan 6.000 pesos.", ["hora del jueves", "cantidad de visitas del sábado", "cálculo correcto"], ["hoja con respuestas", "nota del adulto"], ["confundir los días", "calcular mal el total"], "Reconoce los datos hallados y practica con él el cálculo de 3 por 2.000."),
    "Busca en una lista de tu casa, como un calendario, un dato específico, como el día de un cumpleaños, sin leer todo.",
    "Escribe un pequeño horario con tres datos y pídele a alguien que busque uno.",
)

lesson(
    OA7, 4,
    "El texto descrito en cada ejercicio, lápiz y hoja para dibujar.",
    "Aprenderé a visualizar lo que leo, es decir, a formar una imagen mental, y a releer cuando tengo dudas. Sirve para entender detalles de ubicación y descripciones.",
    ["Sé que next to es al lado de y under es debajo de.", "Conozco chair, table, lamp y window."],
    [
        "Visualizar (to visualize) es crear una imagen en tu mente a partir de las palabras. Cuando lees «A red chair is next to the window», imaginas una silla roja cerca de una ventana. Es más fácil si dibujas lo que lees en una hoja, como un croquis simple.",
        "Las palabras de lugar te ayudan: next to (al lado de), on (sobre), under (debajo de), above (sobre, más arriba) y between (entre). Marca cada objeto y su lugar. Si no recuerdas dónde está un objeto, no adivines: relee (reread) la frase donde se menciona.",
        "Releer es una estrategia muy útil. Si no entendiste una parte, vuelve a la oración y léela con calma. Busca la palabra de lugar y la cosa. También puedes releer para comprobar tu dibujo o tu predicción. Un buen lector relee las veces que haga falta.",
    ],
    [("visualize", "formar una imagen mental"), ("reread", "releer"), ("next to", "al lado de"), ("under", "debajo de"), ("above", "sobre, más arriba"), ("wall", "pared")],
    [
        ("Visualizar un objeto", "Lee: " + ROOM + " ¿Dónde está la lámpara?", ["Busco lamp.", "Dice A lamp is on the table.", "Está sobre la mesa."], "Sobre la mesa"),
        ("Releer para aclarar", "En el mismo texto, ¿dónde duerme el gato?", ["No recuerdo; releo.", "Dice A cat sleeps under the table.", "Duerme debajo de la mesa."], "Debajo de la mesa"),
    ],
    [
        ("Dibujar la silla debajo de la ventana.", "Se confunde next to con under.", "Next to es al lado de y under es debajo de."),
        ("Adivinar un dato que no recuerdas.", "No se relee el texto.", "Vuelve a leer la frase que menciona el objeto."),
    ],
    [
        ("Lee: " + ROOM + " ¿De qué color es la silla?", "Roja", "Dice a red chair."),
        ("Lee: " + ROOM + " ¿Dónde están las dos imágenes (pictures)? a) en la pared sobre la cama b) debajo de la mesa", "a)", "Dice on the wall above my bed."),
        ("¿Qué significa «reread»?", "Releer", "Re- indica volver a hacer una acción."),
    ],
    [
        ("Lee: " + ROOM + " ¿Cuántas imágenes hay en la pared?", "2", "Dice Two pictures."),
        ("Lee: " + ROOM + " ¿Qué objeto está al lado de la ventana? a) la silla roja b) la lámpara", "a)", "Dice A red chair is next to the window."),
        ("Lee: " + ROOM + " ¿Qué hay debajo de la mesa? a) un gato b) una silla", "a) un gato", "Dice a cat sleeps under the table."),
    ],
    [
        ("Lee: " + KITCHEN + " ¿Qué forma tiene la mesa?", "Redonda", "Dice a round table."),
        ("En la cocina, ¿cuántas sillas hay alrededor de la mesa?", "3", "Dice Three chairs."),
        ("En la cocina, ¿qué está sobre la mesa? a) un frutero b) un reloj", "a) un frutero", "El reloj está en la pared."),
    ],
    [
        ("Si dibujas el cuarto, ¿qué dibujas sobre la mesa? a) una lámpara b) un gato", "a) una lámpara", "El gato está debajo de la mesa."),
        ("Lee: «The ball is between the box and the chair.» (between = entre). ¿Qué dos objetos tiene a los lados?", "La caja y la silla", "Between indica que está en medio de ellos."),
    ],
    [
        ("Lee: «A boy is on a bench. A bird is on his hat. A dog is under the bench.» (bench = banca). ¿Qué está debajo de la banca?", "Un perro", "Dice a dog is under the bench."),
        ("En el texto anterior, ¿qué está sobre el sombrero? a) un pájaro b) el perro", "a) un pájaro", "Dice a bird is on his hat."),
    ],
    [("Lee: «There are three books on the shelf. One is red, one is blue and one is green.» (shelf = repisa). ¿Cuántos libros hay sobre la repisa?", "3", "Dice three books.")],
    [
        ("¿Qué significa «visualize»?", "Formar una imagen en mi mente", "Es imaginar lo que se lee."),
        ("¿Qué haces si no recuerdas un dato?", "Releo la frase", "Releer evita adivinar."),
        ("¿Qué significa «above»?", "Sobre o más arriba", "Above indica una posición más alta."),
    ],
    task("Lee este texto: «In the park, there is a big tree. A bench is under the tree. A girl sits on the bench. Her dog is next to her. Two birds are above the tree.» (sits = se sienta). Dibuja la escena en tu hoja con todos los elementos en su lugar. Escribe debajo cuántos animales hay.", "Dibujo con árbol, banca debajo, niña sobre la banca, perro al lado y dos pájaros arriba. Hay 3 animales.", ["dibuja la banca debajo del árbol", "perro al lado de la niña", "escribe 3 animales"], ["dibujo del estudiante", "nota del adulto"], ["poner la banca sobre el árbol", "olvidar los pájaros"], "Reconoce el dibujo logrado y relee con él las palabras de lugar."),
    "Relee la descripción del cuarto del texto y dibuja un croquis con los muebles.",
    "Describe en tres oraciones en inglés dónde están tres objetos de tu cuarto y pide a otra persona que los dibuje.",
)

lesson(
    OA7, 5,
    "El cuento escrito en cada ejercicio y lápiz.",
    "Aprenderé a confirmar mis predicciones después de leer, a contar de nuevo con ayuda de palabras clave y a hacer preguntas para comprobar información. Sirve para comprender y recordar un texto.",
    ["Sé hacer predicciones antes de leer.", "Conozco who, what, where, when y why."],
    [
        "Después de leer (post-reading) haces tres cosas. Primera, confirmar tus predicciones (confirm predictions): comparar lo que pensabas con lo que dice el texto. Segunda, releer las partes que no están claras. Tercera, volver a contar (retell) lo que leíste con ayuda de palabras clave o de dibujos.",
        "Para volver a contar con apoyo, escribe las palabras clave en orden: «Lucas - magic box - coin - abracadabra - paper birds». Con esas palabras cuentas la historia con first, then y finally. No necesitas memorizar el texto, solo recordar lo importante.",
        "También puedes hacer preguntas para confirmar información: «What does Lucas put in the box?» (¿qué pone Lucas en la caja?), «Who claps?» (¿quién aplaude?), «Where do the birds come from?» (¿de dónde salen los pájaros?). Las preguntas usan who, what, where, when, why o how. La respuesta está en el texto.",
    ],
    [("confirm", "confirmar"), ("retell", "volver a contar"), ("key words", "palabras clave"), ("question", "pregunta"), ("claps", "aplaude"), ("coin", "moneda")],
    [
        ("Confirmar una predicción", "Lee: " + BOX + " Predijiste «la caja mágica mostrará una sorpresa». ¿Se confirma?", ["Busco la sorpresa.", "Dice the box shows a surprise.", "La predicción se confirma."], "Sí; the box shows a surprise"),
        ("Hacer una pregunta", "Con el mismo texto, escribe la pregunta cuya respuesta es «three paper birds». a) What flies out of the box? b) Who is Lucas?", ["La respuesta nombra cosas que salen volando.", "La pregunta a) coincide.", "La b) pregunta por Lucas."], "a)"),
    ],
    [
        ("Contar de nuevo agregando cosas que no están en el texto.", "Se cuenta lo que se imagina y no lo leído.", "Usa las palabras clave del texto, en orden."),
        ("Hacer una pregunta cuya respuesta no está en el texto.", "No sirve para confirmar información.", "Pregunta algo que se pueda responder con una frase del texto."),
    ],
    [
        ("Lee: " + BOX + " ¿De qué color es la caja?", "Azul", "Dice It is old and blue."),
        ("Lee: " + BOX + " ¿Qué pone Lucas primero en la caja?", "Una moneda", "Dice First, he puts a coin."),
        ("Lee: " + BOX + " ¿Cuántos pájaros salen de la caja?", "3", "Dice three paper birds."),
    ],
    [
        ("Lee: " + BOX + " Ordena con las palabras clave: A) pájaros de papel B) moneda C) abracadabra.", "B, C, A", "Primero la moneda, luego la palabra mágica y después los pájaros."),
        ("Lee: " + BOX + " ¿Qué hacen los niños al final? a) aplauden y piden otra vez b) se van", "a)", "Dice clap and shout: again!"),
        ("Elige una pregunta con who: a) Who has a magic box? b) What is blue?", "a)", "Who pregunta por una persona."),
    ],
    [
        ("Lee: " + BOX + " ¿Qué palabra mágica dice Lucas?", "abracadabra", "Dice Then he says: abracadabra!"),
        ("Para el texto de Lucas, elige una pregunta con how many: a) How many paper birds fly out? b) Who is Lucas?", "a)", "How many pregunta por una cantidad."),
        ("Lee: " + BOX + " ¿Quiénes aplauden al final? a) los niños b) Lucas", "a) los niños", "Dice The children clap."),
    ],
    [
        ("Lee: " + BOX + " Un compañero dice que los pájaros son de plástico. ¿Cómo lo compruebas?", "Releyendo: dice paper birds, pájaros de papel", "La evidencia está en el texto."),
        ("Escribe una pregunta con where sobre el texto de Lucas. Elige: a) Where do the birds come from? b) When is the party?", "a)", "La respuesta está en el texto: salen de la caja."),
    ],
    [
        ("Ordena las palabras clave según aparecen en el texto de Lucas: A) pájaros B) moneda C) caja.", "C, B, A", "Primero aparece la caja, luego la moneda y al final los pájaros."),
        ("Una palabra clave del texto de Lucas NO aparece en él. ¿Cuál? a) abracadabra b) bicycle", "b) bicycle", "Abracadabra es lo que dice Lucas, pero no hay ninguna bicicleta."),
    ],
    [("Lees el título «Surprise in the Garden» y predices que hay una flor nueva. Al terminar el texto ves que había un cachorro. ¿Qué haces con tu predicción?", "La corrijo", "La evidencia del texto muestra otra cosa.")],
    [
        ("¿Qué significa «retell»?", "Volver a contar", "Se cuenta de nuevo con apoyo."),
        ("¿Qué haces después de leer para confirmar?", "Comparo mi predicción con el texto", "Así sabes si acertaste."),
        ("¿Qué palabra usas para preguntar por una persona?", "Who", "Who significa quién."),
    ],
    task("Lee este cuento: «Pablo finds a small key in the garden. He tries it on the garden door, but it does not open. Then he tries it on an old box in the shed. The box opens and inside there are ten colorful marbles.» (finds = encuentra, tries = prueba, shed = cobertizo, marbles = bolitas). Escribe tres palabras clave en orden, una predicción que hiciste antes (con el título «The Mystery Key») y si se confirmó, y dos preguntas con who y what.", "Palabras clave: key, door, box. Predicción: abre algo; se confirmó. Preguntas: Who finds the key? What is inside the box?", ["tres palabras clave en orden", "predicción comparada", "dos preguntas con respuesta en el texto"], ["hoja con respuestas", "nota del adulto"], ["hacer preguntas sin respuesta en el texto", "no comparar la predicción"], "Reconoce lo bien hecho y relee con él las preguntas para comprobar sus respuestas."),
    "Cuenta a una persona de tu casa un cuento corto usando solo tres palabras clave anotadas.",
    "Escribe tres preguntas (who, what, where) sobre el texto del panadero.",
)

# ================================================================ OA 08
lesson(
    OA8, 1,
    "El texto escrito en cada ejercicio y lápiz.",
    "Aprenderé a expresar lo que me gustó, lo que sentí y mi opinión sobre lo que leí. Sirve para reaccionar a un texto con razones.",
    ["Sé usar I like, I feel y because.", "Conozco happy, sad y proud."],
    [
        "Después de leer, puedes reaccionar al texto. Di si te gustó o no con I liked it (me gustó) o I didn't like it (no me gustó). Agrega por qué con because: «I liked the story because it was funny». También puedes decir cómo te sentiste: «I felt happy» (me sentí feliz) o «I felt sad» (me sentí triste).",
        "Cuando das una opinión, usa I think... (creo que...) y una razón. «I think Mario is kind because he helped the puppy.» (creo que Mario es amable porque ayudó al cachorro). Las razones deben apoyarse en el texto: una acción, una frase o un dato.",
        "Mario es un buen personaje para practicar. Algunas palabras de sentimiento son: happy (feliz), sad (triste), proud (orgulloso), surprised (sorprendido) y worried (preocupado). Elige la que mejor muestre cómo te sentiste tú, no cómo se sintió el personaje, y explícalo.",
    ],
    [("I liked it", "me gustó"), ("I didn't like it", "no me gustó"), ("I felt", "me sentí"), ("I think", "creo que"), ("proud / surprised / worried", "orgulloso / sorprendido / preocupado"), ("because", "porque")],
    [
        ("Dar una opinión con razón", "Lee: " + MARIO + " Completa: «I think Mario is kind because...» Elige la mejor razón: a) he helped the puppy b) he has a vet", ["La razón debe mostrar que es amable.", "Ayudar al cachorro es amable.", "La opción a) es la razón."], "a)"),
        ("Un sentimiento", "En el mismo texto, ¿cómo se sintió Mario al final?", ["Busco felt.", "Dice Mario felt very happy.", "Se sintió muy feliz."], "Muy feliz"),
    ],
    [
        ("Decir «I liked it» sin razón.", "Falta explicar.", "Agrega because y una razón del texto."),
        ("Confundir cómo se siente el personaje con cómo me siento yo.", "Son dos cosas distintas.", "Di I felt para tus sentimientos y He felt para los de otro."),
    ],
    [
        ("Lee: " + MARIO + " ¿Qué le dio Mario al cachorro? a) agua y pan b) un hueso", "a)", "Dice gave it water and some bread."),
        ("Lee: " + MARIO + " ¿Qué significa «I felt happy»?", "Me sentí feliz", "Felt es el pasado de feel."),
        ("¿Qué significa «I didn't like it»?", "No me gustó", "Didn't like es negación en pasado."),
    ],
    [
        ("Completa: I liked the story ___ it was exciting. Elige because o but.", "because", "La segunda parte da la razón."),
        ("Lee: " + MARIO + " Para decir que te sentiste orgulloso de Mario, ¿qué frase usas? a) I felt proud of Mario b) I felt hungry", "a)", "Proud es orgulloso."),
        ("Elige la reacción con razón: a) I liked the story because Mario helped the puppy. b) I liked the story.", "a)", "Solo a) da una razón."),
    ],
    [
        ("Completa: I felt ___ because the puppy was cold. Elige worried o proud.", "worried", "Un cachorro con frío preocupa."),
        ("Quieres decir «me gustó el cuento». ¿Qué frase usas? a) I liked the story. b) I didn't like the story.", "a)", "I liked it significa me gustó."),
        ("Un compañero dice: «I didn't like the story because it was too short.» ¿Cuál es su razón?", "Era muy corta", "Después de because dice too short."),
    ],
    [
        ("Lee: " + MARIO + " Un compañero dice «I think Mario is brave because he found a dragon». ¿Se apoya en el texto?", "No; el texto no menciona ningún dragón", "Una opinión debe apoyarse en hechos que están en el texto."),
        ("En el texto, ¿qué acción de Mario muestra que se preocupa por los animales? a) darle agua y llevarlo al veterinario b) vivir cerca de la escuela", "a)", "Esas acciones muestran cuidado."),
    ],
    [
        ("Lee: «Pedro lost his hat, but a girl found it.» ¿Cómo te sentirías tú si pierdes algo? Elige una palabra para I felt ___: a) worried b) proud", "a) worried", "Perder algo puede preocupar."),
        ("Lee: «Pedro lost his hat, but a girl found it.» ¿Qué sentimiento tendría Pedro al final? a) happy b) angry", "a) happy", "Recuperar el sombrero es motivo de alegría."),
    ],
    [("Lee: «The dog wagged its tail when it saw the boy.» (wagged = movió, saw = vio). ¿Cómo crees que se sintió el perro? a) contento b) triste", "a) contento", "Mover la cola muestra alegría.")],
    [
        ("¿Qué significa «proud»?", "Orgulloso", "Se siente por algo bien hecho."),
        ("¿Qué significa «I think»?", "Creo que", "Introduce una opinión."),
        ("¿Qué debe tener una reacción?", "Una razón", "Así se entiende por qué."),
    ],
    task("Lee este texto: «Elena trains every day for the race. On the day of the race, she falls. She gets up and finishes last, but she smiles. Her friends cheer for her.» (trains = entrena, falls = se cae, finishes = termina, last = último, cheer = animan). Escribe tres frases en inglés: una con I liked/didn't like y because, una con I felt y una con I think.", "I liked the story because Elena did not give up. I felt proud. I think Elena is brave.", ["tres frases", "usa because", "usa I felt e I think"], ["hoja con frases", "nota del adulto"], ["no dar razón", "no usar los tres modelos"], "Reconoce las reacciones con razón y practica con él cambiar el sentimiento."),
    "Lee en voz alta una oración sobre el texto de Mario con I liked o I didn't like y because.",
    "Escribe tres frases en inglés sobre un libro o una película que conozcas: una con liked, una con felt y una con think.",
)

lesson(
    OA8, 2,
    "El cuento escrito en cada ejercicio, lápiz y regla.",
    "Aprenderé a mostrar lo que entendí con un organizador gráfico: un mapa del cuento y una tabla. Sirve para ordenar la información de un texto de forma visual.",
    ["Sé identificar personajes, lugar y problema.", "Conozco beginning, middle y end."],
    [
        "Una ilustración (illustration) es un dibujo de una escena del texto: incluye solo lo que el texto dice y lleva una frase corta como título. Un organizador gráfico (graphic organizer) es un esquema para ordenar ideas. El mapa del cuento (story map) tiene cuatro cajas: Characters (personajes), Setting (lugar y momento), Problem (problema) y Solution (solución). Se completa con palabras o frases cortas sacadas del texto.",
        "Otro organizador es la tabla de causa y efecto: a la izquierda va lo que pasó (cause) y a la derecha, el resultado (effect). Una línea de tiempo (timeline) muestra los hechos en orden con first, next y finally. Elige el organizador según la pregunta: ¿quiénes?, ¿por qué?, ¿en qué orden?",
        "Para completar un organizador, relee el texto con un lápiz y subraya los datos. Escribe palabras cortas, no oraciones largas. Revisa que cada caja tenga información del texto y no de tu imaginación. Un buen organizador te permite contar el cuento sin volver a leerlo.",
    ],
    [("graphic organizer", "organizador gráfico"), ("story map", "mapa del cuento"), ("characters", "personajes"), ("setting", "lugar y momento"), ("problem / solution", "problema / solución"), ("timeline", "línea de tiempo")],
    [
        ("Completar el mapa del cuento", "Lee: " + KITE + " ¿Quién es el personaje principal y cuál es el lugar?", ["Busco el nombre: Rita.", "Busco el lugar: the town of Valle Alto.", "Personaje: Rita. Lugar: Valle Alto."], "Rita; el pueblo de Valle Alto"),
        ("Problema y solución", "En el mismo texto, ¿cuál es el problema y cuál la solución?", ["Problema: the wind is weak and the kite does not fly.", "Solución: the wind grows stronger.", "El viento fuerte hace subir el volantín."], "El viento es débil y el volantín no vuela; el viento se hace más fuerte"),
    ],
    [
        ("Escribir oraciones largas en cada caja.", "El organizador pierde su función.", "Escribe palabras o frases cortas."),
        ("Poner el problema en la caja de solución.", "Se confunden las cajas.", "Problem es lo difícil y Solution es lo que lo resuelve."),
    ],
    [
        ("Lee: " + KITE + " ¿De qué color es el volantín? a) amarillo b) rojo", "a) amarillo", "Dice a big yellow kite."),
        ("Lee: " + KITE + " ¿Cómo se siente Rita al comienzo? a) nerviosa b) enojada", "a) nerviosa", "Dice she is nervous."),
        ("Lee: " + KITE + " ¿Qué gana Rita? a) el premio al volantín más alto b) un libro", "a)", "Dice the prize for the highest kite."),
    ],
    [
        ("Lee: " + KITE + " En un organizador de causa y efecto: causa «the wind is weak». ¿Cuál es el efecto? a) el volantín no vuela al principio b) Rita gana", "a)", "Dice at first, her kite does not fly."),
        ("Lee: " + KITE + " En la línea de tiempo, ¿qué va después de que el viento se hace más fuerte? a) el volantín sube alto b) Rita llega al concurso", "a)", "Dice the kite goes up high."),
        ("Lee: " + KITE + " Completa el mapa: Setting (momento). ¿Cuándo es el concurso? a) cada año b) cada día", "a)", "Dice Every year."),
    ],
    [
        ("Según el texto del volantín, si la línea de tiempo anota: el volantín no vuela, viento fuerte, el volantín sube, Rita gana, ¿cuántos hechos tiene?", "4", "Son cuatro hechos."),
        ("Para el mapa del cuento de Rita, ¿qué va en la caja Setting? a) Valle Alto, cada año b) Rita es nerviosa", "a)", "Setting es lugar y momento."),
        ("Quieres ilustrar la escena final del texto del volantín. ¿Qué debe incluir el dibujo según el texto? a) Rita, el volantín amarillo alto y el premio b) un perro y un barco", "a)", "Una ilustración muestra solo lo que dice el texto: Rita, el volantín y el premio."),
    ],
    [
        ("Ordena la línea de tiempo: A) Rita gana el premio B) el viento es débil C) el viento se hace más fuerte D) el volantín no vuela.", "B, D, C, A", "El texto sigue ese orden."),
        ("Un compañero llenó la caja Characters con «Valle Alto». ¿Qué error cometió?", "Puso un lugar en vez de un personaje", "Valle Alto es un lugar."),
    ],
    [
        ("Lee: «Tomás has a blue bike. He rides it to school. One day, the bike has a flat tire. He walks. The next day, his dad fixes it.» (flat tire = neumático pinchado). ¿Cuál es el problema para el mapa?", "La bicicleta tiene un neumático pinchado", "Es lo que dificulta a Tomás."),
        ("En el texto de Tomás, ¿cuál es la solución?", "Su papá arregla la bicicleta", "Dice his dad fixes it."),
    ],
    [("Un organizador de causa y efecto tiene causa: «It is raining» y efecto: «We stay inside». ¿Qué conector usarías en inglés para unirlos? a) so b) but", "a) so", "So une causa con efecto.")],
    [
        ("¿Qué cajas tiene un mapa del cuento?", "Personajes, lugar, problema y solución", "Characters, Setting, Problem y Solution."),
        ("¿Qué escribes en las cajas: oraciones largas o palabras cortas?", "Palabras cortas", "Un organizador es breve."),
        ("¿Qué muestra una línea de tiempo?", "El orden de los hechos", "Usa first, next y finally."),
    ],
    task("Lee este texto: «Nora wants to bake bread for her family. In her kitchen, she mixes the flour, the water and the yeast. She waits two hours. The bread is soft and smells delicious. Her family eats all of it.» (bake = hornear, flour = harina, yeast = levadura, soft = blando, smells = huele, kitchen = cocina). Dibuja un mapa del cuento con cuatro cajas (Characters, Setting, Problem y Solution) y completa cada una con palabras cortas. Luego dibuja una línea de tiempo con tres hechos.", "Characters: Nora y su familia. Setting: la cocina de Nora. Problem: quiere hacer pan para su familia. Solution: mezcla los ingredientes y espera dos horas. Línea: mezcla, espera, come.", ["cuatro cajas completas", "palabras cortas", "línea de tiempo de tres hechos"], ["dibujo del organizador", "nota del adulto"], ["escribir oraciones largas", "poner los hechos en desorden"], "Reconoce las cajas bien llenadas y relee con él para mejorar las que faltan."),
    "Dibuja un mapa del cuento con cuatro cajas para el texto del volantín de Rita y completa solo dos cajas.",
    "Haz una tabla de causa y efecto con dos filas sobre un texto que hayas leído en esta unidad.",
)

lesson(
    OA8, 3,
    "El texto escrito en cada ejercicio y lápiz.",
    "Aprenderé a relacionar un texto con mis experiencias y con otras asignaturas, y a dar mi opinión con razones. Sirve para mostrar que entendí y que el texto me importa.",
    ["Sé que las plantas necesitan agua y luz.", "Sé decir I think y because."],
    [
        "Cuando lees, puedes relacionar el texto con tu vida: «This reminds me of my neighbor's garden» (esto me recuerda al jardín de mi vecino). También con otras asignaturas: Ciencias, Matemática, Artes o Historia. Así el texto cobra sentido y es más fácil recordarlo.",
        "Usa frases como «I connect this with science because...» (lo relaciono con ciencias porque...), «In math class we learned...» (en la clase de matemática aprendimos...) y «I agree/disagree because...» (estoy de acuerdo/no estoy de acuerdo porque...). La razón debe venir del texto y de lo que sabes.",
        "Por ejemplo, el texto «Plants grow when they get water, light and warm soil» se conecta con Ciencias, porque las plantas necesitan esas cosas. Se conecta con tu vida si tú has plantado algo. Dar tu opinión también es una forma de respuesta: «I think we should water plants every day because they need water».",
    ],
    [("It reminds me of...", "me recuerda a..."), ("I connect this with...", "lo relaciono con..."), ("In science class", "en la clase de ciencias"), ("I agree / I disagree", "estoy de acuerdo / no estoy de acuerdo"), ("should", "debería"), ("soil", "tierra")],
    [
        ("Conectar con Ciencias", "Lee: «Plants grow when they get water, light and warm soil.» (grow = crecen, soil = tierra). ¿Con qué asignatura lo conectas y por qué?", ["Habla de plantas.", "Las plantas se estudian en Ciencias.", "Se conecta con Ciencias porque habla de lo que necesitan las plantas."], "Con Ciencias, porque habla de lo que necesitan las plantas"),
        ("Conectar con tu vida", "Un niño dice: «It reminds me of the tomato plant at home». ¿Qué tipo de conexión es?", ["Habla de su casa.", "Es una experiencia personal.", "Es una conexión con su vida."], "Con su vida personal"),
    ],
    [
        ("Conectar sin dar razón.", "No se explica la relación.", "Agrega because y una razón."),
        ("Dar una opinión que no se relaciona con el texto.", "La opinión no se apoya en lo leído.", "Usa datos o frases del texto para opinar."),
    ],
    [
        ("Lee: «A triangle has three sides.» (sides = lados). ¿Con qué asignatura lo conectas?", "Matemática", "Las figuras se estudian en Matemática."),
        ("Lee: «Pablo Neruda was a Chilean poet.» (poet = poeta). ¿Con qué asignatura lo conectas? a) Lenguaje b) Matemática", "a) Lenguaje", "Los poetas y la poesía se estudian en Lenguaje."),
        ("Lee: «The artist mixes blue and yellow to make green.» (mixes = mezcla). ¿Con qué asignatura lo conectas?", "Artes", "Mezclar colores se hace en Artes."),
    ],
    [
        ("Un compañero dice: «Plants need light.» Tú sabes que es verdad. Completa: «I ___ with you because plants need light.» Elige agree o disagree.", "agree", "Estás de acuerdo porque lo que dijo es verdad."),
        ("Elige la frase que relaciona con tu vida: a) It reminds me of my school b) A triangle has three sides", "a)", "It reminds me of... es personal."),
        ("Lee: «Water boils at 100 degrees Celsius.» (boils = hierve, degrees Celsius = grados Celsius). ¿Con qué asignatura lo conectas?", "Ciencias", "Los cambios del agua se estudian en Ciencias."),
    ],
    [
        ("Lee: «Rain falls from clouds.» (falls = cae). ¿Con qué asignatura lo conectas?", "Ciencias", "La lluvia y las nubes se estudian en Ciencias."),
        ("Lee: «Long ago, people sailed in big wooden ships.» (sailed = navegaban, ships = barcos). ¿Con qué asignatura lo conectas?", "Historia", "Habla de un tiempo del pasado."),
        ("Alguien dice: «I think reading every day is important because it helps me learn.» ¿Es hecho u opinión?", "Opinión", "Empieza con I think y da una razón."),
    ],
    [
        ("Un compañero dice «I think we should drink more water». ¿Qué parte es la opinión?", "We should drink more water", "I think introduce la opinión."),
        ("Para opinar sobre el texto de las plantas, ¿cuál es una buena razón? a) because they need water b) because it is Monday", "a)", "La razón debe relacionarse con el texto."),
    ],
    [
        arith("En una clase de Matemática: «A garden has 4 rows with 6 plants each.» ¿Cuántas plantas hay?", "4*6", "Se multiplican las filas por las plantas de cada fila."),
        ("Para el texto anterior, ¿con qué dos asignaturas puedes conectar: a) Matemática y Ciencias b) Artes y Música?", "a)", "Hay cálculo de plantas y se habla de plantas."),
    ],
    [("Lee: «A week has seven days.» ¿Con qué asignatura lo conectas? a) Matemática b) Educación Física", "a) Matemática", "Los días y los números se usan en Matemática.")],
    [
        ("¿Qué significa «It reminds me of»?", "Me recuerda a", "Conecta con algo vivido."),
        ("¿Qué debe llevar una conexión?", "Una razón", "Sin razón no se entiende la relación."),
        ("¿Qué significa «I disagree»?", "No estoy de acuerdo", "Es lo opuesto a agree."),
    ],
    task("Lee este texto: «Honeybees fly from flower to flower. They collect nectar to make honey. When they visit flowers, they also help plants make fruit.» (collect = recolectan, nectar = néctar, honey = miel, fruit = fruta). Escribe dos conexiones: una con Ciencias y una con tu vida o experiencia. Termina con una opinión con I think... because...", "Con Ciencias: I connect this with science because bees help plants. Con mi vida: It reminds me of my garden. Opinión: I think bees are important because they help plants.", ["conexión con Ciencias", "conexión personal", "opinión con razón"], ["hoja con frases", "nota del adulto"], ["no dar razón", "opinar sin relación con el texto"], "Reconoce las conexiones bien explicadas y practica con él una frase con because."),
    "Lee el texto de las abejas y dile a otra persona con qué asignatura lo relacionas.",
    "Escribe en español tres conexiones entre un texto de esta unidad y tu vida diaria.",
)

lesson(
    OA8, 4,
    "El texto escrito en cada ejercicio y lápiz.",
    "Aprenderé a escribir un párrafo o resumen breve de lo que leí, con una idea principal y dos o tres datos en orden. Sirve para compartir lo que entendí por escrito.",
    ["Sé usar first, next y finally.", "Sé identificar la idea principal."],
    [
        "Un resumen o párrafo breve (summary) cuenta lo más importante de un texto en tres o cuatro frases. Tiene una frase de inicio con la idea principal (topic sentence), dos o tres datos en orden y, si quieres, una frase final. No copia todo el texto: usa tus palabras y deja los detalles pequeños.",
        "Para escribirlo: 1) subraya las ideas clave; 2) escribe la idea principal en una frase; 3) agrega los hechos con first, then y finally; 4) revisa mayúsculas, puntos y que los hechos estén en orden. Evita agregar tu opinión dentro del resumen; si quieres opinar, hazlo en una frase aparte que empiece con I think.",
        "Un ejemplo sobre el texto de Mario: «Mario found a lost puppy. First, he gave it water and bread. Then he took it to a vet. Finally, the vet found the owner.» Tiene la idea principal y tres datos en orden. Compara con tu texto: si alguno de los hechos no está en el texto, no debe estar en el resumen.",
    ],
    [("summary", "resumen"), ("topic sentence", "frase con la idea principal"), ("first / then / finally", "primero / luego / finalmente"), ("detail", "detalle"), ("capital letter", "mayúscula"), ("full stop", "punto")],
    [
        ("Elegir la mejor frase de inicio", "Lee: " + MARIO + " ¿Cuál es la mejor frase de inicio para un resumen? a) Mario found a lost puppy. b) Mario likes bread.", ["La frase de inicio da la idea principal.", "La idea principal es que encontró un cachorro perdido.", "La opción a) la tiene."], "a)"),
        ("Ordenar un resumen", "Ordena las frases: A) Finally, the vet found the owner. B) Mario found a lost puppy. C) Then he took it to a vet. D) First, he gave it water and bread.", ["Primero la idea principal.", "Luego los hechos en orden.", "El orden es B, D, C, A."], "B, D, C, A"),
    ],
    [
        ("Copiar el texto completo en el resumen.", "Un resumen es breve.", "Escribe solo la idea principal y los hechos clave."),
        ("Poner los hechos en desorden.", "Se pierde la secuencia.", "Usa first, then y finally para ordenar."),
    ],
    [
        ("¿Cuántas frases tiene un resumen breve?", "Tres o cuatro", "Un resumen es corto, de tres o cuatro frases."),
        ("¿Qué contiene la frase de inicio?", "La idea principal", "Es el topic sentence."),
        ("¿Con qué palabra marcas el último hecho? a) finally b) first", "a) finally", "Finally indica el final."),
    ],
    [
        ("Lee: " + KITE + " Elige la idea principal para un resumen: a) Rita wins a prize with her kite. b) Rita likes yellow.", "a)", "Es el hecho central del texto."),
        ("Lee: " + KITE + " Elige el hecho que NO va en el resumen: a) Rita is nervous b) the kite has a long tail", "b)", "La cola larga es un detalle menor."),
        ("¿Qué corrección necesita esta frase: «first mario found a puppy»?", "Mayúscula en First y en Mario, y punto al final", "Las oraciones empiezan con mayúscula y terminan con punto."),
    ],
    [
        ("Lee: " + GARDEN + " ¿Cuál es la idea principal para el resumen? a) The class plants a garden b) The class likes Monday", "a)", "Es el hecho central."),
        ("Lee: " + GARDEN + " ¿Qué hacen el miércoles?", "Plantan las semillas y las riegan", "Dice On Wednesday, they plant the seeds and water them."),
        ("Lee: " + GARDEN + " ¿Qué día cavan la tierra?", "El martes", "Dice On Tuesday, they dig the soil."),
    ],
    [
        ("Un compañero escribió un resumen con su opinión: «I love the story». ¿Dónde debe ir esa frase?", "Aparte del resumen", "El resumen cuenta hechos, no opiniones."),
        ("Lee: " + MARIO + " Elige el resumen mejor: a) Mario saw a lost puppy, gave it water and took it to a vet. b) Mario went to school and ate bread.", "a)", "La opción a) tiene los hechos centrales."),
    ],
    [
        ("Completa el resumen con el conector: «Rita makes a kite. ___, the wind grows stronger.» Elige Then o Why.", "Then", "Then indica lo que pasa después."),
        ("Lee: " + KITE + " Ordena: A) Rita wins B) The wind grows stronger C) Rita's kite does not fly.", "C, B, A", "Es el orden del texto."),
    ],
    [("Lee: «Maya paints a picture. First, she draws a tree. Then she colors it green. Finally, she signs her name.» (paints = pinta, signs = firma). ¿Cuántos pasos hay en el resumen sin contar la idea principal?", "3", "First, then y finally marcan tres pasos.")],
    [
        ("¿Qué es un resumen?", "Un texto breve con la idea principal y los hechos clave", "Resumir es reducir a lo importante."),
        ("¿Qué letra va al comienzo de una oración?", "Mayúscula", "Las oraciones empiezan con mayúscula."),
        ("¿Qué palabra marca el primer hecho?", "First", "First significa primero."),
    ],
    task("Lee este texto: «A new bus line starts in our town on Monday. It goes from the school to the market. The bus comes every ten minutes. It costs five hundred pesos.» (line = línea, market = feria, costs = cuesta). Escribe un resumen de tres frases en inglés o español con una idea principal y dos datos. Marca con subrayado la idea principal.", "A new bus line starts on Monday. It goes from the school to the market. It costs five hundred pesos.", ["idea principal", "dos datos del texto", "orden lógico"], ["hoja con el resumen", "nota del adulto"], ["agregar información que no está", "no usar punto"], "Reconoce el resumen breve y relee con él para comprobar que los datos están en el texto."),
    "Escribe una frase con la idea principal de un cuento que conozcas y léela en voz alta.",
    "Escribe un resumen de cuatro frases del texto de Mario con tus palabras.",
)

lesson(
    OA8, 5,
    "Los guiones y esquemas escritos en cada ejercicio y lápiz.",
    "Aprenderé a preparar una dramatización y una pequeña exposición oral sobre lo que leí. Sirve para compartir un texto con otras personas de forma clara y entretenida.",
    ["Sé que una dramatización tiene personajes y diálogo.", "Sé decir Today I'm going to talk about..."],
    [
        "Una dramatización (role play) cuenta una historia con actores. Cada actor tiene un personaje (role) y dice sus líneas (lines). Un guion (script) escribe quién habla: «Mario: Look, a puppy!». Entre paréntesis se anotan los gestos: (kneels) = se arrodilla. Cada actor usa la voz y el cuerpo según su personaje.",
        "Una exposición oral (oral presentation) tiene tres partes. Inicio: Today I'm going to talk about... (hoy voy a hablar de...). Desarrollo: los hechos más importantes, en orden, con first, then y finally. Cierre: Thank you for listening (gracias por escuchar). Puedes usar un dibujo o un cartel como apoyo visual.",
        "Para hablar bien: mira a quien te escucha, habla despacio y con voz clara, y usa tus notas solo como ayuda. Ensaya dos veces antes. En grupo, repartan los papeles y revisen el tiempo. Si te equivocas, respira y sigue; lo importante es transmitir las ideas.",
    ],
    [("role play", "dramatización"), ("script", "guion"), ("lines", "líneas del personaje"), ("oral presentation", "exposición oral"), ("Thank you for listening", "gracias por escuchar"), ("rehearse", "ensayar")],
    [
        ("Armar una línea", "Lee: " + MARIO + " En una dramatización, ¿quién diría «I found the owner!»? a) Mario b) El veterinario", ["Busco quién encontró al dueño.", "El texto dice The vet found the owner.", "Lo diría el veterinario."], "b) El veterinario"),
        ("Organizar la exposición", "Ordena las tres partes de una exposición: A) Thank you for listening B) Today I'm going to talk about a lost puppy C) First, Mario gave it water.", ["El inicio presenta el tema.", "El desarrollo cuenta los hechos.", "El cierre agradece."], "B, C, A"),
    ],
    [
        ("Leer el guion sin gestos ni voz.", "El personaje no se nota.", "Usa voz y cuerpo según el personaje."),
        ("Hablar muy rápido en la exposición.", "Quien escucha no entiende.", "Habla despacio y con voz clara."),
    ],
    [
        ("¿Qué es un guion?", "El texto que dice quién habla y qué dice", "Script es guion."),
        ("¿Con qué frase empiezas una exposición oral? a) Today I'm going to talk about... b) Goodbye", "a)", "Es la frase de inicio."),
        ("¿Qué significa «Thank you for listening»?", "Gracias por escuchar", "Cierra la exposición."),
    ],
    [
        ("En el guion «Vet: (smiles) I found the owner!», ¿qué indica «(smiles)»?", "Un gesto", "Lo que va entre paréntesis es una acción."),
        arith("Un grupo tiene 4 personajes: Mario, el veterinario, el cachorro y el dueño. Si cada uno dice 2 líneas, ¿cuántas líneas hay?", "4*2", "Se multiplican los personajes por las líneas de cada uno."),
        ("Elige el apoyo visual adecuado para la exposición sobre Mario: a) un dibujo del cachorro b) una foto del patio", "a)", "Se relaciona con el tema."),
    ],
    [
        ("En el guion, la línea es «I am so happy!». ¿Qué gesto es adecuado? a) sonreír y levantar los brazos b) bajar la cabeza triste", "a)", "El gesto debe coincidir con el sentimiento."),
        arith("Un guion de 12 líneas se reparte por igual entre 3 actores. ¿Cuántas líneas dice cada actor?", "12//3", "Se divide el total entre los actores."),
        ("En la exposición, ¿cuál es la mejor manera de usar el cartel? a) Señalar las partes mientras explicas b) Leerlo sin mirar a nadie", "a)", "El apoyo visual ayuda cuando se usa para explicar."),
    ],
    [
        ("Un compañero quiere leer el guion con voz baja y sin mirar a nadie. ¿Qué le recomiendas?", "Mirar al público y hablar más fuerte", "Una dramatización necesita voz y contacto visual."),
        ("En el cierre de la exposición, ¿qué es mejor decir? a) Thank you for listening b) I don't know", "a)", "El cierre agradece."),
    ],
    [
        arith("Una exposición dura 5 minutos: 1 de inicio, 3 de desarrollo y el resto de cierre. ¿Cuántos minutos dura el cierre?", "5-1-3", "Se resta inicio y desarrollo al total."),
        arith("Ensayaron dos veces y cada ensayo duró 6 minutos. ¿Cuántos minutos ensayaron en total?", "6+6", "Se suman los minutos de los dos ensayos."),
    ],
    [("Antes de la exposición, tu grupo debe repartir los papeles. ¿Cuál sería un buen reparto para el texto de Mario? a) un actor para Mario y uno para el veterinario b) todos hacen de Mario", "a)", "Cada personaje tiene su actor.")],
    [
        ("¿Qué significa «rehearse»?", "Ensayar", "Rehearse es practicar antes."),
        ("¿Cuántas partes tiene una exposición oral?", "Tres", "Inicio, desarrollo y cierre."),
        ("¿Qué va entre paréntesis en un guion?", "Los gestos o acciones", "Indican cómo actuar."),
    ],
    task("Con el texto de Mario y el cachorro que leíste arriba, escribe un guion de seis líneas para dos actores (Mario y el veterinario). Incluye al menos un gesto entre paréntesis. Luego escribe en inglés la frase de inicio y la de cierre para una exposición sobre el mismo texto.", "Mario: Look, a lost puppy! Vet: (smiles) Let's look for the owner. Inicio: Today I'm going to talk about a lost puppy. Cierre: Thank you for listening.", ["seis líneas de guion", "al menos un gesto", "frases de inicio y cierre"], ["hoja con guion", "nota del adulto"], ["no incluir gestos", "olvidar el cierre"], "Reconoce el guion claro y ensaya con él en voz alta, mirando a quien escucha."),
    "Ensaya en voz alta con una persona de tu casa dos líneas del guion de Mario.",
    "Prepara una exposición de tres partes sobre un cuento de esta unidad, con un dibujo de apoyo.",
)
