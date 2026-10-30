"""Student material for 3.º básico Inglés (propuesta), EN03 OA 06 (leer textos literarios y funcionales breves).

Los textos en inglés son originales, muy breves y llevan pista en español. Cada palabra o estructura se explica antes de usarla.
"""
from __future__ import annotations

from student_content_en3_a import E, lesson, task
from student_lessons import arith

OA6 = "EN03 OA 06"

lesson(
    OA6, 1,
    "Los textos cortos escritos en cada ejercicio y un lápiz.",
    "Aprenderé a reconocer qué tipo de texto estoy leyendo: cuento, rima, chant, tarjeta de saludo, instrucciones o texto informativo. Sirve para saber cómo leerlo y qué buscar.",
    ["Sé que una rima repite sonidos al final y un chant tiene acciones.", "Sé que un cuento tiene personajes."],
    [
        "Cada tipo de texto tiene pistas. Una tarjeta de saludo (greeting card) empieza con Dear (querido o querida) y termina con From (de parte de): «Dear Ana, Happy Birthday! From Leo». Las instrucciones (instructions) tienen pasos: «Step 1: Open the box. Step 2: Take the book.» (take = toma).",
        "Un cuento (story) tiene personajes que hacen cosas: «Lola has a cat. The cat is big.» (has = tiene). Una rima (rhyme) repite sonidos al final de las líneas: «Night, night, sleep tight. Stars are shining bright.» Un chant (chant) repite acciones para mover el cuerpo: «Clap, clap, jump!».",
        "Un texto informativo (information text) da datos: «A lion is a big wild animal.» (wild = salvaje). Para reconocer el tipo, mira primero las palabras del comienzo y del final, luego cómo está escrito (pasos, líneas que riman, acciones repetidas) y por último de qué habla.",
    ],
    [("Dear / From", "querido o querida / de parte de"), ("Step 1", "paso 1"), ("greeting card", "tarjeta de saludo"), ("story", "cuento"), ("rhyme", "rima"), ("chant", "chant, texto con acciones"), ("wild animal", "animal salvaje")],
    [
        ("Tarjeta de saludo", "Lee: «Dear Ana, Happy Birthday! From Leo.» (Happy Birthday = feliz cumpleaños). ¿Qué tipo de texto es?", ["Veo Dear al comienzo.", "Veo From al final.", "Son las pistas de una tarjeta."], "Una tarjeta de saludo"),
        ("Instrucciones", "Lee: «Step 1: Open the box. Step 2: Take the book.» (box = caja, book = libro). ¿Qué tipo de texto es?", ["Veo Step 1 y Step 2.", "Cada paso empieza con una acción.", "Son instrucciones."], "Instrucciones"),
    ],
    [
        ("Pensar que cualquier texto con nombres es un cuento.", "Se mira solo los nombres.", "Busca más pistas: Dear y From son de una tarjeta."),
        ("Confundir una rima con un chant.", "No se compara su forma.", "La rima repite sonidos finales; el chant repite acciones."),
    ],
    [
        ("Lee: «Dear Ana, Happy Birthday! From Leo.» ¿Qué tipo de texto es?", "Una tarjeta de saludo", "Dear y From son sus pistas."),
        ("Lee: «Step 1: Open the box. Step 2: Take the book.» ¿Qué tipo de texto es?", "Instrucciones", "Tiene pasos con acciones."),
        ("Lee: «Clap, clap, jump! Clap, clap, jump!» (clap = aplaudir, jump = saltar). ¿Qué tipo de texto es?", "Un chant", "Repite las mismas acciones."),
    ],
    [
        ("¿Qué palabras son pistas de una tarjeta de saludo?", "Dear y From", "Una está al comienzo y la otra al final."),
        ("¿Cómo reconoces unas instrucciones?", "Por los pasos (Step 1, Step 2) y las acciones", "Dicen qué hacer en orden."),
        ("¿Qué diferencia hay entre una rima y un chant?", "La rima repite sonidos finales y el chant repite acciones", "Cada uno tiene su propia pista."),
    ],
    [
        ("Lee: «Lola has a cat. The cat is big. Lola gives water to the cat.» (gives = da, water = agua). ¿Qué tipo de texto es?", "Un cuento", "Tiene personajes y acciones."),
        ("Lee: «A lion is a big wild animal.» ¿Qué tipo de texto es?", "Un texto informativo", "Da un dato sobre un animal."),
        ("Lee: «Night, night, sleep tight. Stars are shining bright.» (sleep tight = duerme bien, stars = estrellas). ¿Qué tipo de texto es?", "Una rima", "Tight y bright repiten un sonido."),
    ],
    [
        ("Ana dice que «Dear Leo, Happy Easter! From Mia» es un cuento porque tiene nombres. ¿Qué palabras muestran que es otra cosa?", "Dear y From; es una tarjeta", "Son las pistas de una tarjeta de saludo."),
        ("Un texto empieza con «Step 1: Take a pencil.» ¿Es un cuento o instrucciones?", "Instrucciones", "Step 1 y la acción take son pistas."),
    ],
    [
        ("Textos: A «Dear Tom, Happy Birthday! From Ana.» B «Step 1: Take a pencil. Step 2: Draw a circle.» C «Max is a dog. Max can run.» Tipos: 1 tarjeta, 2 instrucciones, 3 cuento. Une cada texto con su tipo.", "A1, B2, C3", "Dear y From, Step y acciones, personaje Max."),
        ("Lista de cuatro textos: «Step 1: Open the book.», «Clap, clap, jump!», «Step 1: Take a piece of paper. Step 2: Draw a circle.», «Dear Ana, Happy Birthday! From Leo.» ¿Cuántos son instrucciones?", "2", "Los textos con Step son dos."),
    ],
    [("En la sala encuentras esta hoja: «Step 1: Take a piece of paper. Step 2: Draw a circle.» ¿Qué tipo de texto es?", "Instrucciones", "Tiene pasos y acciones.")],
    [
        ("¿Cómo se dice «tarjeta de saludo» en inglés?", "greeting card", "Es la tarjeta con un saludo."),
        ("¿Qué significa «Dear»?", "Querido o querida", "Se usa al comienzo de una tarjeta."),
        ("Lee: «Max is a dog. Max can run.» ¿Qué tipo de texto es?", "Un cuento", "Tiene un personaje que hace algo."),
    ],
    task("Lee estos tres textos: A «Dear Mia, Happy Easter! From Sam.» B «Step 1: Take a pencil. Step 2: Draw a square.» C «Night, night, sleep tight. Stars are shining bright.» Escribe en una hoja la letra de cada texto y su tipo (tarjeta, instrucciones o rima). Subraya la palabra pista de cada uno.", "A tarjeta (Dear, From); B instrucciones (Step); C rima (tight, bright).", ["identifica los tres tipos", "subraya una pista de cada uno", "no confunde la rima con las instrucciones"], ["hoja con tipos y pistas", "nota del adulto"], ["decir que A es un cuento", "no subrayar pistas"], "Reconoce los tipos bien identificados y repasa con él la pista que le faltó."),
    "Pide a un adulto que lea «Dear» y «From» y mira dónde aparecen en una tarjeta real, si tienes una.",
    "Escribe una tarjeta de saludo de tres líneas con Dear, Happy Birthday y From.",
)

lesson(
    OA6, 2,
    "Los textos escritos en cada ejercicio y un lápiz.",
    "Aprenderé a leer un texto y decir de qué trata en general. Sirve para entender lo principal de un texto sin leer cada palabra con calma.",
    ["Sé reconocer tipos de texto.", "Sé que un detalle es un dato pequeño."],
    [
        "La idea general (general idea) es de qué trata todo el texto. Para encontrarla, lee el título si lo hay, lee todo el texto y pregúntate: ¿quién o qué aparece en todas las frases? Las frases que dan un color, un número o una acción son detalles.",
        "Ejemplo: «Max is a dog. Max is brown. Max can run. Max can jump.» La idea general es el perro Max. En una tarjeta como «Dear Ana, Happy Birthday! I have a gift for you. From Leo» (gift = regalo, for you = para ti), la idea general es que Leo desea feliz cumpleaños a Ana y le tiene un regalo.",
        "También hay textos de pasos: «Step 1: Take a piece of paper. Step 2: Draw a circle. Step 3: Color the circle red.» (piece of paper = hoja de papel, color = pintar). Su idea general es cómo dibujar un círculo rojo. Elige siempre la idea que sirve para todas las frases y no solo para una.",
    ],
    [("general idea", "idea general"), ("detail", "detalle"), ("gift", "regalo"), ("for you", "para ti"), ("piece of paper", "hoja de papel"), ("color", "pintar")],
    [
        ("Idea general de un cuento", "Lee: «Max is a dog. Max is brown. Max can run. Max can jump.» ¿Cuál es la idea general: un perro llamado Max o una pizza?", ["Max aparece en todas las frases.", "Todas hablan de un perro.", "La idea general es Max el perro."], "Un perro llamado Max"),
        ("Idea general de una tarjeta", "Lee: «Dear Ana, Happy Birthday! I have a gift for you. From Leo.» ¿Qué dice Leo a Ana?", ["Busco Happy Birthday.", "Busco I have a gift for you.", "Leo desea feliz cumpleaños y tiene un regalo."], "Que le desea feliz cumpleaños y que tiene un regalo"),
    ],
    [
        ("Elegir un color o un número como idea general.", "Un detalle no resume todo el texto.", "Elige la idea que sirve para todas las frases."),
        ("Leer solo la primera frase.", "No se conoce el resto del texto.", "Lee todo el texto antes de decidir."),
    ],
    [
        ("Lee: «Max is a dog. Max is brown. Max can run. Max can jump.» ¿Cuál es la idea general: un perro llamado Max o una pizza?", "Un perro llamado Max", "Todas las frases hablan de Max."),
        ("Lee: «Dear Ana, Happy Birthday! I have a gift for you. From Leo.» ¿Quién escribe la tarjeta?", "Leo", "From Leo indica quién escribe."),
        ("Lee: «Step 1: Take a piece of paper. Step 2: Draw a circle. Step 3: Color the circle red.» ¿Es una receta, un cuento o instrucciones para dibujar?", "Instrucciones para dibujar", "Tiene pasos con draw y color."),
    ],
    [
        ("¿Qué es la idea general de un texto?", "De qué trata todo el texto", "Resume todas las frases."),
        ("¿Qué es un detalle?", "Un dato pequeño, como un color o una acción", "No resume todo el texto."),
        ("¿Qué haces para encontrar la idea general?", "Leo todo el texto y busco qué aparece en todas las frases", "No basta una frase."),
    ],
    [
        ("Lee: «Step 1: Take a piece of paper. Step 2: Draw a circle. Step 3: Color the circle red.» ¿De qué color es el círculo al final?", "Rojo", "Red es rojo."),
        ("Lee: «Max is a dog. Max is brown. Max can run. Max can jump.» ¿Cuál es un detalle: «Max can jump» o «el texto trata de un perro»?", "Max can jump", "Dice una sola acción."),
        ("Lee: «Dear Ana, Happy Birthday! I have a gift for you. From Leo.» ¿Qué tiene Leo para Ana?", "Un regalo", "Gift es regalo."),
    ],
    [
        ("Pedro dice que la idea general de «Max is a dog. Max is brown. Max can run.» es «Max is brown». ¿Tiene razón?", "No; es un detalle, la idea general es el perro Max", "Brown solo dice el color."),
        ("Elena dice que la tarjeta de Leo trata de un pastel. ¿Tiene razón?", "No; el texto habla de un cumpleaños y un regalo", "No aparece ninguna palabra de pastel."),
    ],
    [
        ("Lee: «A lion is a big wild animal. It is brown. It can run fast.» (wild = salvaje, fast = rápido). Elige el mejor título: a) The Lion b) My Birthday.", "a", "Todas las frases hablan del león."),
        ("Lee: «Step 1: Take a piece of paper. Step 2: Draw a circle. Step 3: Color the circle red.» ¿Cuántos pasos tiene?", "3", "Hay tres pasos numerados."),
    ],
    [("Encuentras en un libro: «A lion is a big wild animal. It is brown. It can run fast.» ¿Cuál es la idea general?", "Cómo es un león", "Todas las frases describen al león.")],
    [
        ("¿Cómo se dice «idea general» en inglés?", "general idea", "General idea es idea general."),
        ("¿Qué significa «gift»?", "Regalo", "Se da en un cumpleaños."),
        ("Lee: «Step 1: Take a piece of paper.» ¿Qué debes tomar?", "Una hoja de papel", "Paper es hoja de papel."),
    ],
    task("Lee este texto: «Max is a dog. Max is brown. Max can run. Max can jump.» Escribe en una hoja un título corto para el texto (por ejemplo My Dog Max) y subraya un detalle del texto.", "My Dog Max; detalle: Max is brown.", ["escribe un título que habla de Max", "subraya un detalle", "no usa un detalle como título"], ["hoja con título y subrayado", "nota del adulto"], ["usar Brown como título", "no subrayar nada"], "Reconoce el título que resume todo y repasa con él cuál era el detalle."),
    "Pide a un adulto que lea «Max is a dog» y dibuja a Max.",
    "Escribe un texto de tres frases sobre un animal y un título que resuma su idea general.",
)

lesson(
    OA6, 3,
    "Los textos escritos en cada ejercicio y un lápiz.",
    "Aprenderé a encontrar los personajes de un texto, qué hace cada uno y a entender las expresiones «I want...» y «Here!». Sirve para seguir quién hace qué en una historia.",
    ["Sé reconocer la idea general.", "Sé leer palabras de acción con -ing."],
    [
        "Los personajes (characters) son las personas, animales o seres que aparecen en una historia. Las acciones (actions) son lo que hacen. En «Mia is jumping. Leo is reading. A dog is running», los personajes son Mia, Leo y el perro, y las acciones son saltar, leer y correr. Un lugar o un objeto no es un personaje.",
        "Dos expresiones frecuentes son I want, que significa «yo quiero», y Here!, que significa «¡toma!» o «¡aquí tienes!». Ejemplo: «Sam is hungry. Sam: I want an apple. Lola: Here!» (hungry = con hambre). Sam quiere una manzana y Lola se la da. Para pedir con amabilidad se agrega please: «I want an apple, please».",
        "Para encontrar personajes y acciones, subraya los nombres de personas o animales y luego la palabra de acción que está cerca de cada uno. Así sabes quién hace qué. Recuerda que is jumping significa «está saltando» y is reading significa «está leyendo».",
    ],
    [("character", "personaje"), ("action", "acción"), ("I want", "yo quiero"), ("Here!", "¡toma!"), ("hungry", "con hambre"), ("park", "parque")],
    [
        ("Quién hace qué", "Lee: «Mia and Leo are in the park. Mia is jumping. Leo is reading. A dog is running.» (and = y, park = parque). ¿Quién está saltando?", ["Busco jumping.", "Antes de is jumping está Mia.", "Mia salta."], "Mia"),
        ("Expresiones frecuentes", "Lee: «Sam is hungry. Sam: I want an apple. Lola: Here!» ¿Quién quiere una manzana?", ["Busco I want.", "Antes de I want está Sam.", "Sam quiere la manzana y Lola la da."], "Sam"),
    ],
    [
        ("Contar el parque o un libro como personajes.", "Se confunden los lugares y objetos con los personajes.", "Los personajes son personas o animales que hacen algo."),
        ("Pensar que Here! significa «aquí vivo».", "No se entiende la expresión.", "Here! dice ¡toma! cuando alguien da algo."),
    ],
    [
        ("Lee: «Mia and Leo are in the park. Mia is jumping. Leo is reading. A dog is running.» ¿Quién está leyendo?", "Leo", "Leo is reading."),
        ("En el mismo texto, ¿qué hace el perro?", "Corre", "Running es correr."),
        ("¿Qué significa «I want»?", "Yo quiero", "Se usa para pedir algo."),
    ],
    [
        ("¿Qué son los personajes de un texto?", "Las personas o animales que aparecen y hacen cosas", "El parque no es personaje."),
        ("¿Qué significa «Here!»?", "¡Toma!", "Se dice al dar algo."),
        ("¿Cómo encuentras quién hace qué?", "Busco los nombres y la acción que está cerca", "Cada nombre va con su acción."),
    ],
    [
        ("Lee: «Mia and Leo are in the park. Mia is jumping. Leo is reading. A dog is running.» ¿Cuántos personajes hay?", "3", "Mia, Leo y el perro."),
        ("Lee: «Sam is hungry. Sam: I want an apple. Lola: Here!» ¿Qué hace Lola?", "Le da una manzana a Sam", "Here! dice que ella se la da."),
        ("Lee: «Tom: I want a pencil. Ana: Here!» ¿Quién da el lápiz?", "Ana", "Ana dice Here!."),
    ],
    [
        ("Pablo dice que el parque es un personaje del texto de Mia y Leo. ¿Tiene razón?", "No; el parque es un lugar", "Los personajes hacen acciones."),
        ("Lee: «Lola has a cat. The cat is big. Lola gives water to the cat. The cat is happy.» (has = tiene, gives = da). ¿Quién da el agua?", "Lola", "Lola gives water to the cat."),
    ],
    [
        ("Lee: «Lola has a cat. The cat is big. Lola gives water to the cat. The cat is happy.» ¿Cuántos personajes hay?", "2", "Lola y el gato."),
        ("Lee: «Ben is eating bread. Ana: I want bread. Ben: Here!» (eating = comiendo, bread = pan). ¿Quién da el pan?", "Ben", "Ben dice Here!."),
    ],
    [("En el recreo, Sam dice: «I want a ball.» y Leo responde: «Here!» ¿Qué hace Leo?", "Le da la pelota a Sam", "Here! se dice al dar algo.")],
    [
        ("¿Cómo se dice «personaje» en inglés?", "character", "Character es personaje."),
        ("Lee: «Ben is sleeping.» ¿Quién es el personaje y qué hace?", "Ben duerme", "Sleeping es durmiendo."),
        ("¿Qué quiere una persona que dice «I want water»?", "Agua", "Water es agua."),
    ],
    task("Lee este texto: «Mia and Leo are in the park. Mia is jumping. Leo is reading. A dog is running.» En una hoja haz una tabla con dos columnas: personaje y acción, y completa tres filas.", "Mia - jumping; Leo - reading; dog - running.", ["escribe los tres personajes", "escribe la acción correcta de cada uno", "no incluye el parque"], ["tabla escrita", "nota del adulto"], ["cambiar las acciones", "agregar park como personaje"], "Reconoce las filas correctas y revisa con él cada acción en el texto."),
    "Pide a un adulto que lea «I want» y «Here!» y representa con las manos pedir y dar algo.",
    "Escribe un diálogo de dos líneas con I want y Here! sobre una fruta.",
)

lesson(
    OA6, 4,
    "Las instrucciones escritas en cada ejercicio; una hoja, un lápiz y lápices de colores o solo lápiz.",
    "Aprenderé a leer instrucciones por pasos y a hacer lo que dicen en orden. Sirve para hacer una actividad siguiendo un texto escrito.",
    ["Sé leer palabras de acción como take y draw.", "Sé los colores red y blue."],
    [
        "Las instrucciones (instructions) son un texto que dice qué hacer, paso a paso. Cada paso (step) empieza con una palabra de acción: take (toma), draw (dibuja), color (pinta). Mira este ejemplo: «Step 1: Take a piece of paper. Step 2: Draw a big circle. Step 3: Color the circle blue. Step 4: Draw two eyes and a mouth.» (piece of paper = hoja de papel, circle = círculo, eyes = ojos, mouth = boca).",
        "Lee un paso a la vez y hazlo antes de leer el siguiente. Fíjate en los números (one, two, three), en los colores (blue) y en los tamaños (big, small). Si saltas un paso, el resultado cambia. Con este texto dibujas una cara azul con dos ojos y una boca.",
        "Para comprobar, lee de nuevo los pasos y pregunta: ¿hice cada acción? ¿usé el color correcto? ¿puse el número correcto de cosas? Si una instrucción dice Step 3, es la tercera acción y no la primera.",
    ],
    [("step", "paso"), ("take", "tomar"), ("draw", "dibujar"), ("color", "pintar"), ("circle", "círculo"), ("eyes / mouth", "ojos / boca")],
    [
        ("Seguir un paso", "Lee: «Step 1: Take a piece of paper. Step 2: Draw a big circle. Step 3: Color the circle blue. Step 4: Draw two eyes and a mouth.» ¿De qué color pintas el círculo?", ["Busco color.", "El Step 3 dice blue.", "Blue es azul."], "Azul"),
        ("Contar lo que dice", "En las mismas instrucciones, ¿cuántos ojos dibujas?", ["Busco eyes.", "El Step 4 dice two eyes.", "Two es dos."], "Dos"),
    ],
    [
        ("Hacer los pasos en otro orden.", "No se respetan los números de los pasos.", "Haz el paso 1, luego el 2 y así hasta el final."),
        ("Dibujar un círculo pequeño cuando dice big.", "No se lee el tamaño.", "Fíjate en palabras como big y small."),
    ],
    [
        ("Lee: «Step 1: Take a piece of paper. Step 2: Draw a big circle. Step 3: Color the circle blue. Step 4: Draw two eyes and a mouth.» ¿Qué haces en el Step 1?", "Tomo una hoja", "Take a piece of paper significa toma una hoja."),
        ("En las mismas instrucciones, ¿qué dibujas en el Step 2?", "Un círculo grande", "Draw a big circle."),
        ("En las mismas instrucciones, ¿qué haces en el Step 4?", "Dibujo dos ojos y una boca", "Draw two eyes and a mouth."),
    ],
    [
        ("¿Qué indica «Step 3»?", "Que es el tercer paso", "Three significa tres."),
        ("¿Qué palabra suele empezar cada paso de unas instrucciones?", "Una palabra de acción", "Take, draw o color dicen qué hacer."),
        ("¿Qué pasa si saltas un paso?", "El resultado cambia", "Los pasos siguen un orden."),
    ],
    [
        ("Lee: «Step 1: Take a piece of paper. Step 2: Draw a big circle. Step 3: Color the circle blue. Step 4: Draw two eyes and a mouth.» ¿Cuántos ojos dibujas?", "2", "Dice two eyes, o sea dos."),
        ("Lee: «Step 1: Take a piece of paper. Step 2: Draw a small square. Step 3: Color the square red.» (square = cuadrado). ¿Qué figura pintas de rojo?", "El cuadrado", "Color the square red."),
        ("Lee: «Step 1: Take a piece of paper. Step 2: Draw a small square. Step 3: Color the square red.» ¿De qué tamaño es la figura?", "Pequeña", "Small es pequeño."),
    ],
    [
        ("Luis dibujó un círculo pequeño, pero el Step 2 dice «a big circle». ¿Qué debe cambiar?", "Dibujar un círculo grande", "Big es grande."),
        ("Ana coloreó primero y dibujó después. ¿Qué paso hizo en un orden incorrecto?", "El color debe hacerse después de dibujar", "Step 2 es dibujar y Step 3 es pintar."),
    ],
    [
        ("Instrucciones: «Step 1: Take a piece of paper. Step 2: Draw a big circle. Step 3: Draw two eyes.» Ordena los pasos: A) Draw two eyes. B) Take a piece of paper. C) Draw a big circle.", "B, C, A", "Primero tomo la hoja, luego dibujo y al final los ojos."),
        arith("Lee: «Step 1: Take a piece of paper. Step 2: Draw three circles. Step 3: Draw two squares.» (circles = círculos, squares = cuadrados). ¿Cuántas figuras dibujas en total?", "3+2", "Se suman los tres círculos y los dos cuadrados."),
    ],
    [("En una hoja tu profesora escribe: «Step 1: Take a piece of paper. Step 2: Draw a small square. Step 3: Color the square red.» ¿Cuántos pasos hay?", "3", "Hay tres pasos numerados.")],
    [
        ("¿Qué significa «mouth»?", "Boca", "Mouth es boca."),
        ("¿Qué significa «color» como acción en un paso?", "Pintar", "Color the circle significa pinta el círculo."),
        ("¿Qué significa «Take a piece of paper»?", "Toma una hoja", "Take es tomar."),
    ],
    task("Lee estas instrucciones: «Step 1: Take a piece of paper. Step 2: Draw a big circle. Step 3: Color the circle blue. Step 4: Draw two eyes and a mouth.» Hazlas en orden. Al terminar, escribe debajo de tu dibujo: blue circle, two eyes, mouth.", "Una cara azul con dos ojos y una boca, con las tres etiquetas.", ["hace los cuatro pasos en orden", "pinta el círculo de azul", "dibuja dos ojos y una boca"], ["dibujo con etiquetas", "nota del adulto"], ["pintar de otro color", "dibujar más de dos ojos"], "Reconoce los pasos bien hechos y repasa con él el paso donde se equivocó."),
    "Pide a un adulto que lea «Take a piece of paper» y toma una hoja.",
    "Escribe tus propias instrucciones de tres pasos para dibujar un sol amarillo.",
)

lesson(
    OA6, 5,
    "Cuatro textos nuevos escritos en cada ejercicio y un lápiz.",
    "Aprenderé a leer un texto nuevo y decir qué tipo es, de qué trata, quiénes aparecen y qué dice. Sirve para usar lo aprendido con textos que no he visto.",
    ["Sé reconocer tipos de texto, la idea general, personajes y acciones.", "Sé seguir instrucciones por pasos."],
    [
        "Cuando lees un texto nuevo, repite estos pasos: 1) mira el tipo de texto con las pistas que aprendiste (Dear y From, Step 1, rimas, acciones, personajes, datos); 2) lee todo el texto y busca la idea general; 3) busca personajes y acciones; 4) usa las palabras que conoces para responder.",
        "Hoy verás cuatro textos: una tarjeta («Dear Mia, Happy Easter! Here is a chocolate egg for you. From Sam» — for you = para ti, here is = aquí tienes), un texto informativo («A zebra is a wild animal. It is black and white. It can run fast.»), instrucciones («Step 1: Take a pencil. Step 2: Draw a square. Step 3: Color it green.») y un cuento («Ben is tired. He is sleeping. A cat is on the bed.»).",
        "No todas las palabras necesitan traducción. Si conoces el tipo de texto, las pistas te ayudan a entender. Responde siempre con una frase o palabra del texto que lo pruebe. Así muestras que leíste con atención.",
    ],
    [("Easter", "Pascua"), ("chocolate egg", "huevo de chocolate"), ("zebra", "cebra"), ("pencil", "lápiz"), ("tired", "cansado"), ("bed", "cama")],
    [
        ("Texto nuevo: tarjeta", "Lee: «Dear Mia, Happy Easter! Here is a chocolate egg for you. From Sam.» (here is = aquí tienes, for you = para ti) ¿Qué tipo de texto es y quién lo escribe?", ["Veo Dear y From.", "From Sam indica quién escribe.", "Es una tarjeta de Sam."], "Una tarjeta; la escribe Sam"),
        ("Texto nuevo: informativo", "Lee: «A zebra is a wild animal. It is black and white. It can run fast.» (wild = salvaje, fast = rápido). ¿De qué trata?", ["Todas las frases hablan de la zebra.", "Dan datos sobre ella.", "Es un texto informativo sobre la cebra."], "De la cebra, un animal salvaje blanco y negro"),
    ],
    [
        ("Leer un texto nuevo sin buscar pistas del tipo de texto.", "No se aprovecha lo que se aprendió.", "Mira primero las pistas: Dear, Step 1, rimas, acciones."),
        ("Responder sin mostrar la frase del texto.", "No se prueba la respuesta.", "Di la palabra o frase del texto que apoya tu respuesta."),
    ],
    [
        ("Lee: «Dear Mia, Happy Easter! Here is a chocolate egg for you. From Sam.» ¿Qué le da Sam a Mia?", "Un huevo de chocolate", "Here is a chocolate egg for you."),
        ("Lee: «A zebra is a wild animal. It is black and white. It can run fast.» ¿De qué colores es la cebra?", "Blanca y negra", "Black and white."),
        ("Lee: «Step 1: Take a pencil. Step 2: Draw a square. Step 3: Color it green.» (it = lo). ¿De qué color pintas el cuadrado?", "Verde", "Green es verde."),
    ],
    [
        ("¿Qué haces primero al leer un texto nuevo?", "Reconozco qué tipo de texto es", "Las pistas del tipo ayudan."),
        ("Lee: «Ben is tired. He is sleeping. A cat is on the bed.» ¿Qué tipo de texto es?", "Un cuento", "Tiene un personaje y acciones."),
        ("¿Para qué sirve decir la frase del texto que apoya tu respuesta?", "Para mostrar que leí con atención", "Es la evidencia."),
    ],
    [
        ("Lee: «Ben is tired. He is sleeping. A cat is on the bed.» (bed = cama). ¿Cómo está Ben?", "Cansado", "Tired es cansado."),
        ("En el mismo texto, ¿dónde está el gato?", "Sobre la cama", "On the bed."),
        ("Lee: «Step 1: Take a pencil. Step 2: Draw a square. Step 3: Color it green.» ¿Qué figura dibujas?", "Un cuadrado", "Square es cuadrado."),
    ],
    [
        ("Un niño dice que la tarjeta de Sam trata de una cebra. ¿Qué palabra del texto no apoya su idea?", "No aparece zebra; el texto dice Easter y chocolate egg", "La idea no coincide con el texto."),
        ("Una niña dice que Ben está feliz porque duerme. ¿Qué dice el texto?", "Ben is tired; está cansado", "Tired es cansado."),
    ],
    [
        ("Textos: A «Dear Mia, Happy Easter! From Sam.» B «Step 1: Take a pencil.» C «Ben is tired. He is sleeping.» Tipos: 1 tarjeta, 2 instrucciones, 3 cuento. Une.", "A1, B2, C3", "Dear y From, Step y personaje."),
        ("En el texto de la zebra, ¿cuántos datos hay (cada frase es un dato): A zebra is a wild animal, It is black and white, It can run fast?", "3", "Hay tres frases con tres datos."),
    ],
    [("En la biblioteca, ves un papel que dice: «Dear Mia, Happy Easter! From Sam.» ¿Qué tipo de texto es?", "Una tarjeta de saludo", "Dear y From son sus pistas.")],
    [
        ("¿Qué significa «zebra»?", "Cebra", "Es un animal salvaje."),
        ("¿Qué significa «Easter»?", "Pascua", "Es una celebración."),
        ("¿Qué significa «Here!»?", "¡Toma!", "Se dice al dar algo."),
    ],
    task("Lee este texto nuevo: «Step 1: Take a pencil. Step 2: Draw a square. Step 3: Color it green.» Escribe en una hoja el tipo de texto y haz el dibujo que pide. Debajo, copia la frase que dice el color.", "Instrucciones; dibuja un cuadrado verde; copia Color it green.", ["identifica instrucciones", "dibuja un cuadrado verde", "copia la frase del color"], ["hoja con tipo, dibujo y frase", "nota del adulto"], ["decir que es un cuento", "pintar de otro color"], "Reconoce las pistas que usó y repasa con él la frase del color."),
    "Pide a un adulto que lea «Happy Easter» y dibuja un huevo.",
    "Escribe tres frases sobre un animal y pide a otra persona que diga qué tipo de texto es.",
)
