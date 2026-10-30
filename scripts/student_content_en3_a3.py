"""Student material for 3.º básico Inglés (propuesta), EN03 OA 03 (comprensión detallada de textos orales).

Las «escuchas» las lee un adulto en voz alta; el guion va en el enunciado y el estudiante lo tapa con una hoja.
Incluye los pares de sonidos /s/-/z/ y /w/-/th/ que el OA pide identificar.
"""
from __future__ import annotations

from student_content_en3_a import ADULT, E, lesson, task
from student_lessons import arith

OA3 = "EN03 OA 03"

lesson(
    OA3, 1,
    "Las descripciones y palabras escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a identificar personas, animales y objetos por lo que escucho, y a distinguir sonidos del inglés que se confunden. Sirve para entender bien lo que oigo y no confundir palabras.",
    ["Sé decir en inglés big y small.", "Sé que lion, monkey y book son palabras en inglés."],
    [
        "Al escuchar puedes identificar personas (a teacher, a girl, a boy, a doctor), animales (a lion, a monkey, an elephant) y objetos (a book, a pencil, a table, a chair). A veces el texto describe: «It is big» (es grande), «It is gray» (es gris), «It has a long trunk» (tiene una trompa larga). Escucha la palabra y las pistas.",
        "Gray es gris, yellow es amarillo, black es negro y white es blanco. Para elegir un animal, junta todas las pistas: ser grande, ser gris y tener una trompa larga describen a un elephant (elefante). Una sola pista no siempre basta, porque varios animales pueden ser grandes.",
        "En inglés hay sonidos que se confunden. La /s/ de sip (sorber) es un silbido sin vibración; la /z/ de zip (cierre) hace vibrar la garganta: toca tu cuello y lo sentirás. Otros pares son Sue y zoo, ice (hielo) y eyes (ojos), bus y buzz. También se confunden /w/ de wink (guiñar) y /th/ de think (pensar): para /th/ la lengua queda entre los dientes y para /w/ los labios se redondean.",
    ],
    [("teacher / doctor", "profesor o profesora / médico o médica"), ("lion / elephant / monkey", "león / elefante / mono"), ("It is / It has", "es / tiene"), ("gray", "gris"), ("long trunk", "trompa larga"), ("sip / zip", "sorber / cierre"), ("think / wink", "pensar / guiñar")],
    [
        ("Identificar con pistas", ADULT + "«It is big. It is gray. It has a long trunk.» (long = larga, trunk = trompa). ¿Qué animal es: elephant (elefante), zebra (cebra) o monkey (mono)?", ["Junto las pistas: grande, gris y trompa larga.", "El elefante cumple las tres.", "Los otros animales no tienen trompa larga."], "Un elefante"),
        ("Distinguir sonidos", ADULT + "El adulto dice solo una palabra: «zip». ¿Qué palabra oíste: sip o zip?", ["Escucho el primer sonido.", "Noto la vibración en la garganta.", "Eso es la /z/ de zip."], "zip"),
    ],
    [
        ("Elegir un animal por una sola pista.", "Varios animales pueden ser grandes.", "Junta todas las pistas antes de decidir."),
        ("Pensar que sip y zip suenan igual.", "No se siente la vibración de la /z/.", "Toca tu garganta: en zip vibra y en sip no."),
    ],
    [
        (ADULT + "«It is a lion.» (lion = león). ¿Qué animal es?", "Un león", "Lion es león."),
        (ADULT + "«I see a teacher.» (see = ver). ¿A quién ve?", "A un profesor o profesora", "Teacher es profesor o profesora."),
        (ADULT + "«It is a pencil.» ¿Es una persona, un animal o un objeto?", "Un objeto", "Un lápiz es una cosa, no un ser vivo."),
    ],
    [
        ("¿Qué significa «It has a long trunk»?", "Tiene una trompa larga", "Has es tiene, long es larga y trunk es trompa."),
        ("¿Qué significa «gray»?", "Gris", "Gray es un color."),
        ("¿Qué parte del cuerpo puedes tocar para sentir la vibración de la /z/?", "La garganta", "La /z/ hace vibrar la garganta."),
    ],
    [
        (ADULT + "«I see a girl and a boy.» (girl = niña, boy = niño). ¿Cuántos niños y niñas hay en total?", "2", "Una niña y un niño son dos personas."),
        (ADULT + "El adulto dice solo una palabra: «Sue». ¿Qué palabra oíste: Sue o zoo?", "Sue", "La palabra dicha empieza con el silbido /s/."),
        (ADULT + "«It is a table. It is a chair.» ¿Son personas, animales u objetos?", "Objetos", "Table es mesa y chair es silla."),
    ],
    [
        ("Un niño oyó «ice» y escribió «eyes». ¿Qué par de sonidos confundió?", "El sonido /s/ con el sonido /z/", "Ice termina con /s/ y eyes termina con /z/."),
        ("Una niña oyó el sonido de think y escribió wink. ¿Qué dos sonidos confundió?", "/th/ con /w/", "Think empieza con /th/ y wink con /w/."),
    ],
    [
        (ADULT + "«I see a doctor, a lion and a book.» (doctor = médico o médica). ¿Cuál de las tres cosas es un objeto?", "El libro", "Book es libro y no es un ser vivo."),
        (ADULT + "El adulto dice solo una palabra: «think». ¿Con qué sonido empieza: /th/, con la lengua entre los dientes, o /w/, con los labios redondeados?", "/th/", "Think empieza con /th/."),
    ],
    [(ADULT + "En el zoológico, alguien dice: «I see an elephant at the zoo.» (zoo = zoológico). ¿Qué animal ve?", "Un elefante", "Elephant es elefante.")],
    [
        ("¿Qué significa «lion»?", "León", "Lion es un animal salvaje."),
        ("¿Qué sonido hace vibrar la garganta: el de sip o el de zip?", "El de zip", "La /z/ vibra."),
        (ADULT + "«I see a monkey.» ¿Qué ve?", "Un mono", "Monkey es mono."),
    ],
    task("Un adulto lee dos veces: «It is big. It is gray. It has a long trunk.» Dibuja el animal y escribe su nombre en inglés (elephant). Después, toca tu garganta, di sip y zip, y escribe cuál de las dos palabras hace vibrar tu garganta.", "Dibuja un elefante, escribe elephant y anota que zip hace vibrar la garganta.", ["dibuja un animal con trompa larga", "escribe elephant", "dice que zip vibra"], ["dibujo", "nota del adulto"], ["dibujar un mono o una cebra", "decir que sip vibra"], "Reconoce el dibujo acertado y repite con él sip y zip tocando la garganta."),
    "Pide a un adulto que diga «lion, elephant, monkey» y señala cuál es grande y gris.",
    "Describe un animal con «It is...» e «It has...» y pide a otra persona que adivine cuál es.",
)

lesson(
    OA3, 2,
    "Cinco textos cortos escritos en los ejercicios, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a decir de qué trata en general un texto que escucho. Sirve para entender lo principal aunque no entienda cada palabra.",
    ["Sé reconocer personas, animales y objetos al escuchar.", "Sé que Max es un nombre de perro."],
    [
        "La idea general (main idea) es de qué trata todo el texto. Los detalles (details) son datos pequeños: un color, un número o algo que hace el personaje. Si el texto dice «I have a dog. His name is Max. Max is big. Max can run», la idea general es el perro Max. Que Max pueda correr es un detalle.",
        "Para encontrar la idea general, escucha todo el texto y piensa: ¿de qué hablan todas las frases? No te quedes con una sola frase del medio. Verás las palabras I like (me gusta), hospital (hospital), breakfast (desayuno) y morning (mañana).",
        "Si dudas entre dos ideas, elige la que sirve para todas las frases. Por ejemplo, «I like apples. I like bread. I like cheese» habla de comida que me gusta. «I like bread» es solo un detalle. Un buen título resume la idea general.",
    ],
    [("main idea", "idea general"), ("detail", "detalle"), ("I like", "me gusta"), ("hospital", "hospital"), ("breakfast", "desayuno"), ("morning", "mañana")],
    [
        ("Idea general", ADULT + "«I have a dog. His name is Max. Max is big. Max can run.» (his name = su nombre). ¿Cuál es la idea general: un perro llamado Max o una pizza?", ["Todas las frases hablan del perro.", "La pizza no aparece.", "La idea general es Max, el perro."], "Un perro llamado Max"),
        ("Idea general y detalle", "En el texto de Max, ¿«Max can run» es la idea general o un detalle?", ["La idea general reúne todo el texto.", "Max can run dice una sola cosa.", "Es un dato pequeño."], "Un detalle"),
    ],
    [
        ("Elegir como idea general solo la última frase.", "Una frase no resume todo el texto.", "Elige la idea que sirve para todas las frases."),
        ("Decir que un detalle, como un color, es la idea general.", "Se confunde la parte con el todo.", "Pregunta: ¿esto explica todo el texto o solo una parte?"),
    ],
    [
        (ADULT + "«I have a dog. His name is Max. Max is big. Max can run.» ¿Cuál es la idea general: un perro llamado Max, una pizza o un lápiz?", "Un perro llamado Max", "Todas las frases hablan del perro."),
        (ADULT + "«First, I wake up. Next, I eat breakfast. Last, I go to school.» (wake up = me despierto, breakfast = desayuno). ¿La idea general es la mañana de una persona o un día en el zoológico?", "La mañana de una persona", "Las acciones ocurren al empezar el día."),
        (ADULT + "«It is a circle. It is red. The circle is big.» (circle = círculo). ¿La idea general es un círculo rojo o un cuadrado azul?", "Un círculo rojo", "Todas las frases describen el círculo."),
    ],
    [
        ("¿Qué es la idea general de un texto oral?", "De qué trata todo el texto", "Resume todas las frases."),
        ("¿Qué es un detalle?", "Un dato pequeño del texto, como un color", "Un detalle no explica todo el texto."),
        ("¿Cómo encuentras la idea general?", "Escucho todo el texto y pienso de qué hablan todas las frases", "No basta una sola frase."),
    ],
    [
        (ADULT + "«Mia is a doctor. She is at the hospital. She is happy.» (doctor = médica, she = ella, at = en). ¿Cuál es la idea general: una médica feliz o una niña que come pan?", "Una médica feliz", "Mia, doctor y happy describen a la médica."),
        (ADULT + "«I like apples. I like bread. I like cheese.» (apples = manzanas, cheese = queso). ¿De qué trata: de la comida que me gusta o de la escuela?", "De la comida que me gusta", "Apples, bread y cheese son comidas."),
        ("En el texto de Max, ¿cuál es un detalle: «Max is big» o «el texto trata de un perro»?", "Max is big", "Dice solo una característica de Max."),
    ],
    [
        ("Ana dice que la idea general de «I like apples. I like bread. I like cheese» es «I like bread» porque está en el medio. ¿Tiene razón?", "No; es solo un detalle, la idea general incluye las tres comidas", "La idea general reúne todas las frases."),
        (ADULT + "«Max is a dog. Max is big. Max can run.» Un niño dice que la idea es «Max can run». ¿Es una idea general o un detalle?", "Un detalle", "Habla solo de una acción de Max."),
    ],
    [
        (ADULT + "«I have a cat. It is gray. It is small. It can jump.» (cat = gato). ¿Cuántos detalles dicen un color o un tamaño?", "2", "Gray es el color y small es el tamaño."),
        ("Para el texto «First, I wake up. Next, I eat breakfast. Last, I go to school», elige el mejor título: a) My Morning b) My Dog c) At the Zoo.", "a", "My Morning resume las tres acciones de la mañana."),
    ],
    [(ADULT + "En clase escuchas: «I see a lion. I see an elephant. I see a monkey. I'm at the zoo.» ¿De qué trata en general?", "De animales en el zoológico", "Las frases nombran animales y el zoo.")],
    [
        ("¿Cómo se dice «idea general» en inglés?", "main idea", "Main idea es la idea principal."),
        ("¿Qué significa «I like»?", "Me gusta", "Se usa para decir lo que te gusta."),
        (ADULT + "«It is a circle. It is red. The circle is big.» ¿«It is red» es una idea general o un detalle?", "Un detalle", "Dice solo el color."),
    ],
    task("Un adulto lee dos veces: «I like apples. I like bread. I like cheese.» Escribe en una hoja una de estas dos ideas generales, la que corresponde al texto: a) food I like b) my school. Luego dibuja las tres comidas.", "a) food I like; dibuja manzana, pan y queso.", ["elige la idea general a", "dibuja las tres comidas", "no elige un solo detalle como idea general"], ["hoja con la elección", "dibujo"], ["elegir b", "dibujar solo una comida y decir que ese es el tema"], "Reconoce la idea correcta y vuelve a leer con él las tres frases para mostrar que todas hablan de comida."),
    "Pide a un adulto que lea «I like apples» y dibuja una manzana.",
    "Escribe tres frases con I like sobre lo que más te gusta y un título que resuma la idea general.",
)

lesson(
    OA3, 3,
    "Los textos cortos y las preguntas escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a encontrar un detalle que el texto dice con claridad: un color, un número, un lugar o una persona. Sirve para responder preguntas sobre lo que escucho.",
    ["Sé reconocer la idea general de un texto oral.", "Conozco los colores red y green y los números del uno al diez."],
    [
        "Un detalle explícito (explicit detail) es una información que el texto dice directamente. Para encontrarlo, lee la pregunta antes de escuchar. What color? pregunta por un color. Where? pregunta por un lugar. How many? pregunta por una cantidad. Who? pregunta por una persona.",
        "Mira este texto: «Lia has a red bag. The bag is on the chair. There are three books in the bag.» (bag = mochila). El color es red, el lugar es on the chair y la cantidad es three. Has significa «tiene» y There are significa «hay».",
        "Escucha con una palabra clave en la mente: si buscas un color, ignora los números. También cuida los sonidos que se confunden. En «Sue is at the zoo», Sue es un nombre con /s/ y zoo es un lugar con /z/. Si la respuesta es un número, escríbelo con cifras. En la celebración de Pascua (Easter) se dice «Happy Easter», que significa «feliz Pascua».",
    ],
    [("What color?", "¿de qué color?"), ("Where?", "¿dónde?"), ("How many?", "¿cuántos?"), ("Who?", "¿quién?"), ("bag", "mochila"), ("There are", "hay (varios)"), ("on / under / in", "sobre / debajo de / dentro de")],
    [
        ("Buscar un color", ADULT + "«Lia has a red bag. The bag is on the chair. There are three books in the bag.» ¿De qué color es la mochila?", ["La pregunta pide un color.", "Escucho a red bag.", "Red significa rojo."], "Roja"),
        ("Buscar una cantidad", "En el mismo texto, ¿cuántos libros hay en la mochila?", ["La pregunta es How many?", "Busco un número.", "Escucho three books: tres."], "3"),
    ],
    [
        ("Responder con un número cuando la pregunta pide un color.", "No se identificó qué pide la pregunta.", "Lee la pregunta antes: What color? pide un color."),
        ("Responder con un dato que no está en el texto.", "Se inventa en lugar de buscar.", "Busca la palabra en el texto: el detalle debe estar escrito o dicho."),
    ],
    [
        (ADULT + "«Lia has a red bag. The bag is on the chair. There are three books in the bag.» ¿De qué color es la mochila?", "Roja", "Red es rojo."),
        (ADULT + "En el mismo texto: ¿dónde está la mochila?", "Sobre la silla", "On the chair significa sobre la silla."),
        (ADULT + "En el mismo texto: ¿cuántos libros hay?", "3", "Three es tres."),
    ],
    [
        ("¿Qué significa «How many?»", "¿Cuántos?", "Se usa para preguntar una cantidad."),
        ("¿Qué significa «Where?»", "¿Dónde?", "Se usa para preguntar un lugar."),
        ("Si la pregunta es «What color?», ¿qué detalle buscas?", "Un color", "La pregunta indica qué dato necesitas."),
    ],
    [
        (ADULT + "«Tom has a green ball. The ball is under the table. There are two cats in the room.» (room = habitación). ¿De qué color es la pelota?", "Verde", "Green es verde."),
        (ADULT + "En el texto de Tom: ¿dónde está la pelota?", "Debajo de la mesa", "Under the table significa debajo de la mesa."),
        (ADULT + "En el texto de Tom: ¿cuántos gatos hay?", "2", "Two cats son dos gatos."),
    ],
    [
        ("Pablo respondió «two» a la pregunta «What color is the ball?». ¿Qué hizo mal?", "Buscó un número en vez de un color", "What color? pide un color."),
        (ADULT + "«Ana has a blue pencil. Ben has a yellow pencil.» (yellow = amarillo). ¿Quién tiene el lápiz amarillo?", "Ben", "Ben has a yellow pencil."),
    ],
    [
        arith(ADULT + "«There are twelve chairs and eight tables in the classroom.» (classroom = sala de clases, twelve = 12, eight = 8). ¿Cuántas sillas más que mesas hay?", "12-8", "Se resta la cantidad de mesas a la de sillas."),
        (ADULT + "«Sue is at the zoo.» (Sue es una niña, at = en, zoo = zoológico). ¿Dónde está Sue?", "En el zoológico", "At the zoo es el lugar."),
    ],
    [(ADULT + "En la mochila de un amigo escuchas: «Mia has a yellow pencil and three books.» (and = y) ¿De qué color es el lápiz?", "Amarillo", "Yellow es amarillo.")],
    [
        ("¿Qué significa «bag»?", "Mochila", "Es donde guardas libros y cuadernos."),
        ("¿Qué significa «Who?»", "¿Quién?", "Pregunta por una persona."),
        (ADULT + "«Happy Easter, Ana! Here are three chocolate eggs.» (here are = aquí tienes, eggs = huevos). ¿Cuántos huevos de chocolate hay?", "3", "Three es tres y eggs son huevos."),
    ],
    task("Un adulto lee dos veces: «Tom has a green ball. The ball is under the table. There are two cats in the room.» Responde con una palabra o un número a tres preguntas: What color is the ball? Where is the ball? How many cats? Escribe tus tres respuestas.", "green; under the table; 2.", ["dice green o verde", "dice under the table o debajo de la mesa", "dice 2"], ["respuestas escritas", "nota del adulto"], ["responder two a la pregunta del color", "decir on the table"], "Reconoce cada respuesta correcta y vuelve a leer con él la pregunta que falló."),
    "Pide a un adulto que diga «a red bag» y mira tu mochila para encontrar algo rojo.",
    "Escribe una frase con un color, un lugar y una cantidad sobre tu mochila, usando las palabras de la clase.",
)

lesson(
    OA3, 4,
    "Los textos y las tarjetas de orden escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a ordenar tres sucesos que escucho con first, then y last, incluso cuando el texto los dice en otro orden. Sirve para entender qué pasa primero y qué pasa al final.",
    ["Sé que first es primero y last es al final.", "Sé que then significa luego."],
    [
        "Un texto puede contar tres sucesos (events) en orden: First (primero), Then (luego) y Last (al final). Ejemplo: «First, I open the door. Then, I walk to the table. Last, I sit down.» (door = puerta, walk to = camino hacia). Primero abro, luego camino y al final me siento.",
        "A veces el texto dice las cosas desordenadas: «Last, I go to bed. First, I eat. Then, I brush my teeth.» (go to bed = me acuesto, brush my teeth = me lavo los dientes). El orden de los sucesos no es el orden en que los oyes, sino el que dicen las palabras first, then y last. Aquí es: como, me lavo los dientes y me acuesto.",
        "Para ordenar, busca first, then y last y escribe 1, 2 y 3. Luego revisa si tiene sentido: comer va antes de lavarse los dientes. Con las tarjetas, copia solo la letra de cada suceso en el orden correcto.",
    ],
    [("First", "primero"), ("Then", "luego"), ("Last", "al final"), ("event", "suceso"), ("brush my teeth", "me lavo los dientes"), ("door", "puerta")],
    [
        ("Ordenar tres sucesos", ADULT + "«First, I draw a circle. Then, I draw a square. Last, I draw a triangle.» (draw = dibujo, circle = círculo, square = cuadrado, triangle = triángulo). ¿Qué figura dibujo en segundo lugar?", ["Busco Then.", "Después de Then: a square.", "Es la del medio."], "Un cuadrado"),
        ("Texto desordenado", ADULT + "«Last, I go to bed. First, I eat. Then, I brush my teeth.» ¿Qué hago primero?", ["Busco first, no lo que oigo primero.", "First, I eat.", "Primero como."], "Como"),
    ],
    [
        ("Ordenar por lo que se oye primero y no por first, then y last.", "El texto puede estar desordenado.", "Ordena por las palabras first, then y last."),
        ("Pensar que then es lo último.", "Se confunden then y last.", "Then es el del medio; last es el final."),
    ],
    [
        (ADULT + "«First, I open the door. Then, I walk to the table. Last, I sit down.» ¿Qué hago primero?", "Abro la puerta", "First, I open the door."),
        (ADULT + "En el mismo texto: ¿qué hago al final?", "Me siento", "Last, I sit down."),
        ("¿Qué significa «then»?", "Luego", "Then dice que algo viene después."),
    ],
    [
        ("¿Para qué sirven first, then y last?", "Para decir en qué orden ocurren tres sucesos", "Dan el orden de los sucesos."),
        ("Si oyes «Last» al comienzo de un texto, ¿ese suceso ocurre al final o al principio?", "Al final", "Last siempre marca el final."),
        ("¿Qué significa «I brush my teeth»?", "Me lavo los dientes", "Brush es cepillar y teeth son dientes."),
    ],
    [
        ("Texto: «First, I draw a circle. Then, I draw a square. Last, I draw a triangle.» ¿Qué figura es la segunda?", "El cuadrado", "Then dice square y es la segunda."),
        ("Tarjetas: A) Me acuesto. B) Como. C) Me lavo los dientes. Texto: «First, I eat. Then, I brush my teeth. Last, I go to bed.» (go to bed = me acuesto) Ordénalas.", "B, C, A", "Primero como, luego me lavo los dientes y al final me acuesto."),
        (ADULT + "«First, I open the door. Then, I walk to the table. Last, I sit down.» ¿Qué hago antes de sentarme?", "Camino hacia la mesa", "Then, I walk to the table viene antes de last."),
    ],
    [
        ("Carlos dice que se acuesta primero porque oyó «Last, I go to bed» al comienzo. ¿Tiene razón?", "No; last dice que duerme al final", "El orden lo da la palabra last."),
        (ADULT + "«Last, I draw a triangle. First, I draw a circle. Then, I draw a square.» ¿Qué figura dibujo primero?", "El círculo", "First, I draw a circle."),
    ],
    [
        (ADULT + "«Last, I draw a triangle. First, I draw a circle. Then, I draw a square.» Tarjetas: A) triángulo B) círculo C) cuadrado. Ordénalas.", "B, C, A", "First es el círculo, then el cuadrado y last el triángulo."),
        (ADULT + "«Then, I put the book in the bag. First, I open the bag. Last, I close the bag.» (put = pongo, bag = mochila). Tarjetas: A) Cierro la mochila. B) Pongo el libro. C) Abro la mochila. Ordénalas.", "C, B, A", "First abro, then pongo el libro y last cierro."),
    ],
    [(ADULT + "En la mañana escuchas: «First, I wake up. Then, I eat. Last, I go to school.» (wake up = me despierto). ¿Qué hago al final?", "Voy a la escuela", "Last, I go to school.")],
    [
        ("¿Qué significa «last»?", "Al final", "Last indica el final."),
        (ADULT + "«First, I eat. Then, I brush my teeth. Last, I go to bed.» ¿Qué hago luego de comer?", "Me lavo los dientes", "Then, I brush my teeth."),
        ("¿Qué palabra marca el suceso del medio?", "then", "Then va entre first y last."),
    ],
    task("Un adulto lee dos veces: «Last, I go to bed. First, I eat. Then, I brush my teeth.» (go to bed = me acuesto) Dibuja tres cuadros numerados 1, 2 y 3 y pon en cada uno la acción que corresponde. Debajo escribe first, then y last en el cuadro correcto.", "1 como (first), 2 me lavo los dientes (then), 3 me acuesto (last).", ["dibuja las tres acciones", "las ordena como comer, lavarse los dientes y dormir", "escribe first, then y last en el lugar correcto"], ["dibujo con números", "nota del adulto"], ["poner acostarse primero", "confundir then y last"], "Reconoce el orden bien hecho y repite con él los tres números."),
    "Pide a un adulto que diga «first, then, last» y muestra con tres dedos cuál va primero, cuál al medio y cuál al final.",
    "Escribe tres sucesos de tu día con First, Then y Last, mezcla el orden en que los dices y pide a otra persona que los ordene.",
)

lesson(
    OA3, 5,
    "Los textos, las preguntas y las frases-evidencia escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a mostrar la evidencia de mi respuesta: la palabra o frase que escuché y que prueba lo que digo. Sirve para responder con seguridad y explicar cómo lo sé.",
    ["Sé encontrar detalles como un color, un lugar o una cantidad.", "Sé ordenar sucesos con first, then y last."],
    [
        "La evidencia (evidence) es la palabra o frase del texto que prueba tu respuesta. Si la pregunta es «¿Dónde está el perro?» y respondes «Debajo de la mesa», la evidencia es la frase «It is under the table». Respuesta y evidencia van juntas.",
        "Mira este texto: «Lia has a dog. The dog is brown. It is under the table. It is sleeping.» (brown = café, sleeping = durmiendo). Para el color, la evidencia es «The dog is brown». Para lo que hace, la evidencia es «It is sleeping». Si no hay una frase que apoye tu respuesta, vuelve a escuchar.",
        "Para dar evidencia, sigue tres pasos: 1) responde, 2) busca la frase que lo prueba y 3) dila o márcala. No basta decir «porque sí» o «porque lo sé». Tampoco sirve inventar datos que el texto no dice.",
    ],
    [("evidence", "evidencia: palabra o frase que prueba la respuesta"), ("answer", "respuesta"), ("brown", "café"), ("sleeping", "durmiendo"), ("new", "nuevo"), ("bike", "bicicleta"), ("under / in", "debajo de / dentro de")],
    [
        ("Respuesta con evidencia", ADULT + "«Lia has a dog. The dog is brown. It is under the table. It is sleeping.» ¿De qué color es el perro y qué frase lo prueba?", ["Busco el color: brown.", "La frase es «The dog is brown».", "Respuesta y evidencia juntas."], "Café; «The dog is brown»"),
        ("Elegir la evidencia", "Para la respuesta «El perro duerme», ¿qué frase es la evidencia: a) It is sleeping b) The dog is brown?", ["La respuesta habla de dormir.", "It is sleeping dice sleeping.", "Es la que apoya la respuesta."], "a"),
    ],
    [
        ("Responder «porque sí» sin dar evidencia.", "No se muestra dónde está la respuesta.", "Busca y di la frase del texto que apoya tu respuesta."),
        ("Dar como evidencia una frase que no tiene relación con la pregunta.", "No se relacionó la frase con la respuesta.", "Comprueba que la frase hable de lo mismo que la pregunta."),
    ],
    [
        (ADULT + "«Lia has a dog. The dog is brown. It is under the table. It is sleeping.» ¿Dónde está el perro? ¿Qué frase lo prueba: a) The dog is brown b) It is under the table c) It is sleeping?", "b", "It is under the table dice dónde está el perro."),
        (ADULT + "En el mismo texto: ¿qué hace el perro? ¿Qué frase lo prueba: a) The dog is brown b) It is under the table c) It is sleeping?", "c", "It is sleeping dice que duerme."),
        (ADULT + "En el mismo texto: ¿de qué color es el perro? ¿Qué frase lo prueba: a) The dog is brown b) It is under the table c) It is sleeping?", "a", "The dog is brown dice el color."),
    ],
    [
        ("¿Qué es la evidencia de una respuesta?", "La palabra o frase del texto que prueba lo que respondo", "La evidencia viene del texto."),
        ("¿Por qué no basta decir «porque sí»?", "Porque no muestra dónde lo escuché", "Hay que apoyar la respuesta con el texto."),
        ("Si no encuentras una frase que apoye tu respuesta, ¿qué haces?", "Vuelvo a escuchar el texto", "La evidencia debe estar en lo que se escucha."),
    ],
    [
        (ADULT + "«Ben is happy. He has a new blue bike. He is riding his bike.» (bike = bicicleta, new = nueva, riding = andando en, his = su). ¿Cómo está Ben y qué frase lo prueba?", "Feliz; «Ben is happy»", "Happy significa feliz y esa es la frase."),
        (ADULT + "En el texto de Ben: ¿qué tiene Ben y qué frase lo prueba?", "Una bicicleta azul nueva; «He has a new blue bike»", "Has es tiene."),
        (ADULT + "En el texto de Ben: ¿qué hace Ben ahora y qué frase lo prueba?", "Anda en bicicleta; «He is riding his bike»", "Riding termina en -ing y dice lo que hace."),
    ],
    [
        ("Sofía dice que Ben está triste porque tiene una bicicleta. ¿Qué frase del texto muestra que se equivoca?", "Ben is happy", "Happy es feliz, no triste."),
        ("¿Qué respuesta tiene evidencia en el texto de Ben: «He is riding his bike» o «Creo que Ben está en el parque»?", "He is riding his bike", "Esa frase sí está en el texto."),
    ],
    [
        (ADULT + "«Lia has three red apples. She is at the table.» (at the table = en la mesa). ¿Cuántas manzanas tiene Lia? ¿Qué palabras del texto lo prueban?", "3; «three red apples»", "Three es tres y apples son manzanas."),
        (ADULT + "«There are two cats. One cat is black. One cat is white.» (one = uno, black = negro, white = blanco). ¿Cuántos gatos hay y qué frase lo prueba?", "2; «There are two cats»", "There are two cats dice el número."),
    ],
    [(ADULT + "En clase, la profesora pregunta dónde está el libro. El texto dice: «The book is in the bag.» ¿Qué responde un estudiante y cuál es su evidencia?", "En la mochila; «The book is in the bag»", "In the bag es el lugar y esa es la frase.")],
    [
        ("¿Cómo se dice «evidencia» en inglés?", "evidence", "Evidence es la prueba."),
        ("¿Qué significa «brown»?", "Café", "Brown es un color."),
        (ADULT + "«Ben is happy.» ¿Qué sentimiento tiene Ben?", "Feliz", "Happy es feliz."),
    ],
    task("Un adulto lee dos veces: «Ben is happy. He has a new blue bike. He is riding his bike.» Responde en una hoja: 1) ¿Qué tiene Ben? 2) Escribe la frase del texto que lo prueba (puedes copiarla de esta consigna).", "Una bicicleta azul nueva; He has a new blue bike.", ["responde bicicleta o bike", "copia la frase He has a new blue bike", "no usa una frase que no está en el texto"], ["hoja con respuesta y evidencia", "nota del adulto"], ["dar una respuesta sin frase", "copiar la frase He is riding his bike"], "Reconoce la respuesta y la evidencia correcta y vuelve a leer con él la frase que apoya la respuesta."),
    "Pide a un adulto que lea «The dog is brown» y señala con el dedo qué palabra dice el color.",
    "Escribe una pregunta y una respuesta sobre el texto de Ben, y copia la frase que prueba tu respuesta.",
)
