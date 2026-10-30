"""Student material for 4.º básico Inglés (propuesta), EN04 OA 07 (leer sobre temas conocidos o de otras asignaturas).

Todos los textos son originales y están escritos en el enunciado (nada depende de un libro o una tarjeta externa).
Temas: escuela, hogar y muebles, animales salvajes, figuras geométricas, ocupaciones, lugares de la ciudad, comida y Easter.
"""
from __future__ import annotations

from student_content_en4_a import E, lesson, task
from student_lessons import arith

OA7 = "EN04 OA 07"

SCH = "«This is my classroom. There are twenty desks and one board. The library corner is next to the window. My teacher has a green book.»"
HOME = "«My house has a kitchen, a bedroom and a bathroom. In the kitchen there is a table and four chairs. In my bedroom the lamp is on the shelf and the cat is under the bed.»"
EL = "«The elephant is big. It has a long trunk and two big ears. It eats grass and leaves.»"
MON = "«The monkey can climb trees. It has a long tail. It eats fruit.»"
SH = "«A square has four sides. A triangle has three sides. A circle has no sides.»"
REC = "«A rectangle has four sides: two long sides and two short sides.»"
JOBS = "«Ana is a doctor. She works at the hospital. Leo is a baker. He works at the bakery. Mia is a teacher. She works at the school.»"
DIAL = "«A: What does Leo do? B: He is a baker. A: Where does he work? B: At the bakery. A: Where is the bakery? B: It is next to the park.»"
TOWN = "«In my town there is a library, a park and a supermarket. The park is between the library and the supermarket.»"
LUNCH = "«For lunch I eat rice and chicken. I drink water. I eat an apple, too.»"
MENU = "«Menu: soup, rice and chicken, apple. Today there are twelve apples and eight bananas.»"
EAST = "«At Easter, many people decorate eggs. Some people eat chocolate eggs. Mia has a basket with six eggs.»"
DIAL2 = "«A: What do you want? B: I want soup, please. A: Here! B: Thank you.»"
FIRE = "«Eva is a firefighter. She helps people in an emergency. Eva can run fast.»"
NURSE = "«Tom is a nurse. He works at a hospital. Tom helps sick people.»"
ANIM = "«The elephant is big and eats leaves. The zebra has stripes and eats grass. Both animals live in groups.»"

# ---------------------------------------------------------------- clase 1
lesson(
    OA7, 1,
    "Los textos escritos en cada ejercicio; lápiz y papel.",
    "Aprenderé a leer textos sobre la escuela y la casa, y a encontrar cantidades hasta veinte, lugares e instrucciones. Sirve para entender descripciones de espacios que uso todos los días.",
    ["Sé nombrar muebles como table, chair, bed y lamp.", "Sé usar there is, there are, on, under y next to."],
    [
        "En los textos sobre la escuela y la casa aparecen lugares y objetos. En la escuela: classroom (sala de clases), desk (escritorio), board (pizarra), window (ventana) y library corner (rincón de biblioteca). En la casa: kitchen (cocina), bedroom (dormitorio), bathroom (baño), table, chair, lamp y shelf (repisa).",
        "Para leer cantidades usa las palabras de número hasta veinte (twenty) y las expresiones there is (hay uno) y there are (hay varios). Para leer lugares busca on (sobre), under (debajo de) y next to (al lado de). En «The cat is under the bed», el gato está debajo de la cama.",
        "A veces el texto da una instrucción: «Open the window» (abre la ventana) o «Put the book on the table» (pon el libro sobre la mesa). Una instrucción comienza con un verbo. Para entender el texto, busca primero la pregunta y luego la palabra que la responde: un número, un lugar o un objeto.",
    ],
    [("classroom / desk / board", "sala de clases / escritorio / pizarra"), ("window", "ventana"), ("kitchen / bedroom / bathroom", "cocina / dormitorio / baño"), ("there is / there are", "hay (uno) / hay (varios)"), ("on / under / next to", "sobre / debajo de / al lado de"), ("lamp / shelf", "lámpara / repisa"), ("open / put", "abrir / poner")],
    [
        ("Encontrar una cantidad", "Lee: " + SCH + " (desks = escritorios, board = pizarra, window = ventana). ¿Cuántos escritorios hay?", ["Busco desks.", "Antes está twenty.", "Hay veinte."], "20"),
        ("Encontrar un lugar", "Lee: " + HOME + " (kitchen = cocina, bathroom = baño, lamp = lámpara, shelf = repisa). ¿Dónde está el gato?", ["Busco cat.", "Después está under the bed.", "Under significa debajo de."], "Debajo de la cama"),
    ],
    [
        ("Confundir under con on.", "Son palabras de lugar opuestas.", "Under es debajo de y on es sobre; lee cuál aparece."),
        ("Responder con un número que no está en el texto.", "No se busca el dato explícito.", "Busca la palabra de número en la frase que responde a la pregunta."),
    ],
    [
        ("Lee: " + SCH + " ¿Qué hay al lado de la ventana?", "El rincón de la biblioteca", "The library corner is next to the window."),
        ("Lee: " + SCH + " ¿De qué color es el libro de la profesora?", "Verde", "My teacher has a green book."),
        ("Lee: " + HOME + " ¿Cuántas sillas hay en la cocina?", "4", "A table and four chairs."),
    ],
    [
        ("Lee: " + HOME + " ¿Dónde está la lámpara?", "Sobre la repisa", "The lamp is on the shelf."),
        ("¿Qué significa «there are»?", "Hay (varios)", "There are se usa con más de uno."),
        ("Lee: «Open the window. Put the green book on the table.» ¿Qué pones sobre la mesa?", "El libro verde", "Put the green book on the table es la segunda instrucción."),
    ],
    [
        arith("Lee: «There are eleven red desks and nine blue desks.» ¿Cuántos escritorios hay en total?", "11+9", "Se suman los escritorios rojos y los azules."),
        ("Lee: " + HOME + " ¿Cuántos cuartos nombra el texto: kitchen, bedroom y bathroom?", "3", "Son tres cuartos distintos."),
        ("Lee: «Open the window. Put the green book on the table.» ¿Qué tipo de función tiene este texto?", "Dar instrucciones", "Open y put ordenan hacer algo."),
    ],
    [
        ("Lee: " + HOME + " Pedro dice que el gato está sobre la cama. ¿Tiene razón?", "No; el gato está debajo de la cama", "The cat is under the bed."),
        ("Lee: " + HOME + " Ana dice que la casa tiene dos dormitorios. ¿Qué dice el texto?", "Un dormitorio", "El texto dice a bedroom."),
    ],
    [
        arith("Lee: " + HOME + " En la cocina hay una mesa y cuatro sillas. ¿Cuántos muebles hay en la cocina?", "1+4", "Se suman la mesa y las sillas."),
        ("Lee: " + SCH + " ¿Qué objeto del texto es verde y qué está al lado de la ventana?", "El libro de la profesora es verde y el rincón de la biblioteca está al lado de la ventana", "Se combinan dos datos del texto."),
    ],
    [("Ves un cartel en la sala: «Please, open the window.» (please = por favor). ¿Qué haces?", "Abro la ventana", "Open the window significa abre la ventana.")],
    [
        ("¿Qué significa «kitchen»?", "Cocina", "Kitchen es el lugar donde se cocina."),
        ("¿Qué significa «next to»?", "Al lado de", "Next to indica un lugar junto a otro."),
        ("¿Cómo se dice «repisa» en inglés?", "shelf", "Shelf es repisa."),
    ],
    task("Lee: «My bedroom has a bed and a lamp. The lamp is on a small table next to the bed. There are twelve books on the shelf. The cat is under the table.» Dibuja el dormitorio y escribe tres datos con números o lugares que sacaste del texto.", "Cama, lámpara sobre la mesa al lado de la cama, 12 libros en la repisa y gato debajo de la mesa.", ["dibuja la lámpara sobre la mesa", "escribe un número del texto", "escribe un lugar del texto"], ["dibujo del estudiante", "hoja con los datos"], ["poner el gato sobre la mesa", "escribir un número que no está"], "Reconoce lo bien ubicado y vuelve a leer con él la frase donde cambió un lugar."),
    "Lee en voz alta «on, under, next to» y pon un lápiz en cada lugar respecto de un libro.",
    "Escribe un texto de tres frases sobre tu sala de clases con un número y un lugar.",
)

# ---------------------------------------------------------------- clase 2
lesson(
    OA7, 2,
    "Los textos escritos en cada ejercicio; lápiz y papel.",
    "Aprenderé a leer textos sobre animales salvajes y figuras geométricas, y a encontrar sus características. Sirve para unir el inglés con lo que aprendo en Ciencias y en Matemática.",
    ["Sé nombrar animales salvajes y figuras en inglés.", "Sé usar has y can para describir."],
    [
        "Un texto sobre animales describe cómo son y qué hacen. Aparecen partes del cuerpo: trunk (trompa), ears (orejas), tail (cola) y neck (cuello). Aparecen acciones con can, como «The monkey can climb trees» (el mono puede trepar árboles), y comidas, como grass (pasto), leaves (hojas) y fruit (fruta).",
        "Un texto sobre figuras explica sus lados (sides). «A square has four sides» significa «un cuadrado tiene cuatro lados». Un triangle tiene tres lados, un rectangle tiene cuatro lados (dos largos y dos cortos) y un circle no tiene lados. Es información de Matemática dicha en inglés.",
        "Para leer este tipo de texto, busca primero de qué animal o figura trata. Luego busca la característica que te piden: una parte del cuerpo, una comida o un número. Usa solo lo que el texto dice; no agregues datos que no están escritos.",
    ],
    [("trunk / ears / tail", "trompa / orejas / cola"), ("climb", "trepar"), ("fruit", "fruta"), ("grass / leaves", "pasto / hojas"), ("sides", "lados"), ("square / triangle / rectangle / circle", "cuadrado / triángulo / rectángulo / círculo"), ("long / short", "largo / corto")],
    [
        ("Una característica", "Lee: " + EL + " (trunk = trompa, ears = orejas, leaves = hojas). ¿Qué tiene el elefante que es largo?", ["Busco long.", "Oigo long trunk.", "Trunk es trompa."], "La trompa"),
        ("Un dato de Matemática", "Lee: " + SH + " (sides = lados). ¿Cuántos lados tiene un triángulo?", ["Busco triangle.", "Dice three sides.", "Three es tres."], "3"),
    ],
    [
        ("Agregar un dato que no está en el texto, como decir que el elefante es gris.", "El texto no dice el color.", "Responde solo con lo que está escrito."),
        ("Confundir los lados de un cuadrado y de un triángulo.", "Cada figura tiene un número distinto.", "Busca el nombre de la figura y su número."),
    ],
    [
        ("Lee: " + EL + " ¿Cuántas orejas tiene el elefante?", "2", "Two big ears."),
        ("Lee: " + EL + " ¿Qué come el elefante?", "Pasto y hojas", "It eats grass and leaves."),
        ("Lee: " + MON + " (climb = trepar, tail = cola, fruit = fruta). ¿Qué puede hacer el mono?", "Trepar árboles", "The monkey can climb trees."),
    ],
    [
        ("Lee: " + MON + " ¿Cómo es la cola del mono?", "Larga", "It has a long tail."),
        ("Lee: " + SH + " ¿Qué figura no tiene lados?", "El círculo", "A circle has no sides."),
        ("Lee: " + REC + " ¿Cuántos lados largos tiene el rectángulo?", "2", "Two long sides."),
    ],
    [
        arith("Lee: " + SH + " ¿Cuántos lados tienen juntos un cuadrado y un triángulo?", "4+3", "Se suman cuatro lados y tres lados."),
        ("Lee: " + MON + " ¿Qué come el mono?", "Fruta", "It eats fruit."),
        ("Lee: " + REC + " ¿Cuántos lados cortos tiene el rectángulo?", "2", "Two short sides."),
    ],
    [
        ("Lee: " + SH + " Luis dice que el círculo tiene cuatro lados. ¿Tiene razón?", "No; el círculo no tiene lados", "A circle has no sides."),
        ("Lee: " + MON + " Ana dice que el mono come pasto. ¿Qué dice el texto?", "Que come fruta", "It eats fruit."),
    ],
    [
        ("Lee: " + SH + " y " + REC + " ¿Qué tienen en común un cuadrado y un rectángulo?", "Los dos tienen cuatro lados", "Square y rectangle tienen four sides."),
        arith("Lee: «A triangle has three sides.» ¿Cuántos lados tienen tres triángulos en total?", "3*3", "Se multiplica el número de triángulos por sus lados."),
    ],
    [("En la clase de Matemática ves la frase «A square has four sides.» ¿Cuántos lados tiene el cuadrado?", "4", "Four sides son cuatro lados.")],
    [
        ("¿Qué significa «trunk»?", "Trompa", "Trunk es la trompa del elefante."),
        ("¿Qué significa «sides»?", "Lados", "Sides son los lados de una figura."),
        ("¿Se puede agregar un dato que el texto no dice?", "No", "Hay que usar lo que está escrito."),
    ],
    task("Lee: «The giraffe is tall. It has a long neck and two small ears. It eats leaves from tall trees.» (tall = alto). Escribe tres datos de la jirafa que salgan del texto. Luego dibuja un triángulo y escribe debajo «A triangle has three sides».", "Alta, cuello largo, orejas pequeñas, come hojas; triángulo con la frase.", ["escribe tres datos del texto", "dibuja un triángulo", "escribe la frase de los tres lados"], ["hoja con datos y dibujo", "nota del adulto"], ["escribir que la jirafa es verde", "dibujar un cuadrado"], "Reconoce los datos correctos y vuelve a leer con él cada frase."),
    "Lee en voz alta «trunk, ears, tail» y señala esas partes en un dibujo de animal.",
    "Escribe tres frases en inglés sobre un animal salvaje con has y eats.",
)

# ---------------------------------------------------------------- clase 3
lesson(
    OA7, 3,
    "Los textos escritos en cada ejercicio; lápiz y papel.",
    "Aprenderé a leer textos sobre ocupaciones y lugares de la ciudad, y a entender preguntas y respuestas sobre qué hace una persona y dónde está un lugar. Sirve para pedir y dar información en inglés.",
    ["Sé que a doctor es un trabajo.", "Conozco lugares como school, park y library."],
    [
        "Las ocupaciones (jobs) dicen qué trabajo hace una persona: doctor, baker (panadero o panadera), teacher (profesor o profesora), farmer (agricultor) y cook (cocinero). Los lugares de la ciudad (town) son hospital, bakery (panadería), school, library, park y supermarket. Se usa works at para decir dónde trabaja alguien.",
        "Para pedir información se usan preguntas. «What does Leo do?» significa «¿qué hace Leo?» (¿cuál es su trabajo?). «Where does he work?» significa «¿dónde trabaja?». «Where is the bakery?» significa «¿dónde está la panadería?». Las respuestas son «He is a baker», «At the bakery» o «It is next to the park».",
        "Para ubicar un lugar se usan next to (al lado de) y between (entre). En «The park is between the library and the supermarket», el parque queda entre los dos. Para presentarse se dice «I am Eva» (soy Eva) y para presentar a otra persona, «This is my friend Sam» (este es mi amigo Sam). Cualquier persona puede tener cualquier ocupación; el texto dice lo que cada persona hace.",
    ],
    [("job", "ocupación, trabajo"), ("baker / bakery", "panadero / panadería"), ("hospital / supermarket / library", "hospital / supermercado / biblioteca"), ("works at", "trabaja en"), ("What does he do?", "¿qué hace él (de trabajo)?"), ("Where is...?", "¿dónde está...?"), ("between", "entre")],
    [
        ("Ocupación y lugar", "Lee: " + JOBS + " (works = trabaja, baker = panadero, hospital = hospital). ¿Dónde trabaja Ana?", ["Busco Ana.", "Oigo works at the hospital.", "Trabaja en el hospital."], "En el hospital"),
        ("Preguntas y respuestas", "Lee: " + DIAL + " ¿Dónde está la panadería?", ["Busco Where is the bakery?", "La respuesta es next to the park.", "Está al lado del parque."], "Al lado del parque"),
    ],
    [
        ("Pensar que una ocupación es solo para hombres o solo para mujeres.", "Cualquier persona puede tener cualquier trabajo.", "Lee lo que dice el texto de cada persona."),
        ("Responder dónde trabaja alguien con el lugar de otra persona.", "Se mezclan las personas.", "Busca el nombre y la frase works at que le corresponde."),
    ],
    [
        ("Lee: " + JOBS + " ¿Qué es Leo?", "Panadero", "Leo is a baker."),
        ("Lee: " + JOBS + " ¿Quién es profesor o profesora?", "Mia", "Mia is a teacher."),
        ("Lee: " + JOBS + " ¿Dónde trabaja Mia?", "En la escuela", "She works at the school."),
    ],
    [
        ("¿Qué significa «What does Leo do?»", "¿Qué hace Leo (de trabajo)?", "Se usa para preguntar por la ocupación."),
        ("Lee: " + DIAL + " ¿Cuántas preguntas hace A?", "3", "A pregunta qué hace, dónde trabaja y dónde está la panadería."),
        ("Lee: " + DIAL + " ¿Qué responde B a «What does Leo do?»", "He is a baker", "B responde con la ocupación."),
    ],
    [
        ("Lee: " + TOWN + " (between = entre). ¿Qué hay entre la biblioteca y el supermercado?", "El parque", "The park is between them."),
        ("Lee: «Hello! I am Eva. This is my friend Sam. He is a farmer.» (This is my friend = este es mi amigo). ¿Quién es el agricultor?", "Sam", "He is a farmer habla de Sam, a quien Eva presenta."),
        ("Lee: " + JOBS + " ¿Cuántas personas con ocupación nombra el texto?", "3", "Ana, Leo y Mia."),
    ],
    [
        ("Lee: " + JOBS + " Pedro dice que Ana trabaja en la escuela. ¿Tiene razón?", "No; Ana trabaja en el hospital", "She works at the hospital."),
        ("Lee: " + JOBS + " Sofía dice que Mia trabaja en la panadería. ¿Qué dice el texto?", "Que Mia trabaja en la escuela", "Leo trabaja en la panadería."),
    ],
    [
        ("Lee: " + DIAL + " ¿Dónde trabaja Leo y dónde queda ese lugar?", "En la panadería, que queda al lado del parque", "Se combinan dos respuestas del diálogo."),
        ("Lee: " + JOBS + " Une cada lugar con su persona: hospital, bakery, school.", "Hospital-Ana, bakery-Leo, school-Mia", "Cada frase works at indica el lugar."),
    ],
    [("En un cartel de la ciudad lees: «The library is next to the park.» ¿Dónde está la biblioteca?", "Al lado del parque", "Next to the park significa al lado del parque.")],
    [
        ("¿Qué significa «Where is the bakery?»", "¿Dónde está la panadería?", "Where is... pregunta por un lugar."),
        ("¿Cómo se dice «trabaja en» en inglés?", "works at", "Works at une la persona con el lugar."),
        ("¿Una ocupación es solo para hombres o solo para mujeres?", "No, cualquier persona puede tener cualquier ocupación", "Cada texto dice qué hace cada persona."),
    ],
    task("Lee: «Sam is a farmer. He works in the field. Lia is a cook. She works in a restaurant. The restaurant is next to the park.» (field = campo, restaurant = restaurante). Escribe qué es cada persona y dónde trabaja. Luego escribe una pregunta en inglés usando Where is...?", "Sam: farmer, in the field. Lia: cook, in a restaurant. Where is the restaurant?", ["escribe las dos ocupaciones", "escribe los dos lugares", "escribe una pregunta con Where is"], ["hoja con las respuestas", "nota del adulto"], ["mezclar los lugares", "no escribir la pregunta"], "Reconoce lo bien relacionado y vuelve a leer con él cada works."),
    "Lee en voz alta «doctor, baker, teacher» y di dónde trabaja cada uno.",
    "Escribe tres frases sobre ocupaciones de personas que conoces (sin dar nombres completos), con works at.",
)

# ---------------------------------------------------------------- clase 4
lesson(
    OA7, 4,
    "Los textos escritos en cada ejercicio; lápiz y papel.",
    "Aprenderé a leer sobre comida y sobre la celebración de Easter, y a pedir y dar información con What do you want? e I want... Sirve para entender menús, diálogos y descripciones de una celebración.",
    ["Sé nombrar comidas como rice, bread, apple y water.", "Sé usar I want... y Here!."],
    [
        "Los textos sobre comida nombran lo que se come y se bebe: rice (arroz), chicken (pollo), soup (sopa), apple (manzana), banana (plátano) y water (agua). Un menú (menu) es una lista de comidas. Las cantidades hasta veinte aparecen con las palabras de número, como twelve (doce) y eight (ocho).",
        "Easter es una celebración. Muchas personas decoran huevos (eggs) y algunas comen huevos de chocolate. Fíjate en la palabra many (muchas) y some (algunas): no dicen que todas las personas hacen lo mismo. Hay una canasta (basket) para guardar los huevos.",
        "En un diálogo para pedir comida, una persona pregunta «What do you want?» (¿qué quieres?) y otra responde «I want soup, please» (quiero sopa, por favor). Quien entrega dice «Here!». Para decir qué pasa ahora se usa is o are y un verbo con -ing: «Pam is eating soup» (Pam está comiendo sopa). Para decir cómo se siente alguien se usa is o am: «Pam is happy» (Pam está feliz). Para leer bien, busca la pregunta y luego la palabra de comida que la responde.",
    ],
    [("lunch", "almuerzo"), ("menu", "menú: lista de comidas"), ("rice / chicken / soup", "arroz / pollo / sopa"), ("apple / banana", "manzana / plátano"), ("Easter", "Pascua de Resurrección"), ("many / some", "muchas / algunas"), ("What do you want?", "¿qué quieres?")],
    [
        ("Leer una comida", "Lee: " + LUNCH + " (lunch = almuerzo, rice = arroz, chicken = pollo, drink = bebo). ¿Qué bebe la persona?", ["Busco drink.", "Dice I drink water.", "Bebe agua."], "Agua"),
        ("Leer una celebración", "Lee: " + EAST + " (decorate = decorar, eggs = huevos, basket = canasta). ¿Cuántos huevos tiene Mia en la canasta?", ["Busco Mia.", "Dice basket with six eggs.", "Six es seis."], "6"),
    ],
    [
        ("Pensar que todas las personas comen chocolate en Easter.", "El texto dice some people, o sea algunas.", "Lee many y some: no dicen todas."),
        ("Responder con una comida que no está en el texto.", "No se lee con atención.", "Busca la palabra de comida en la frase que responde."),
    ],
    [
        ("Lee: " + LUNCH + " ¿Qué fruta come la persona?", "Una manzana", "I eat an apple, too."),
        ("Lee: " + EAST + " ¿Qué celebración se menciona?", "Easter", "El texto comienza con At Easter."),
        ("Lee: " + EAST + " ¿Qué decoran muchas personas?", "Huevos", "Many people decorate eggs."),
    ],
    [
        ("Lee: " + DIAL2 + " ¿Qué quiere B?", "Sopa", "B dice I want soup."),
        ("Lee: " + DIAL2 + " ¿Quién dice «Here!»?", "A", "A entrega la sopa."),
        ("¿Qué significa «What do you want?»", "¿Qué quieres?", "Se usa para preguntar qué desea alguien."),
    ],
    [
        arith("Lee: " + MENU + " (menu = menú). ¿Cuántas frutas hay en total, contando manzanas y plátanos?", "12+8", "Se suman las manzanas y los plátanos."),
        ("Lee: «Look! Pam is eating soup. Leo is drinking water. Pam is happy.» (look = mira). ¿Qué está haciendo Leo ahora?", "Bebe agua", "Is drinking dice que lo hace ahora."),
        ("Lee: " + EAST + " ¿Cuántas personas comen huevos de chocolate: todas o algunas?", "Algunas", "El texto dice some people."),
    ],
    [
        ("Lee: " + EAST + " Ben dice que en Easter todas las personas comen chocolate. ¿Qué dice el texto?", "Que algunas personas comen huevos de chocolate", "Some people no es todas."),
        ("Lee: " + DIAL2 + " ¿Qué frase pide la sopa?", "I want soup, please", "I want pide algo."),
    ],
    [
        ("Lee los dos textos: " + LUNCH + " y " + MENU + " ¿Qué comidas aparecen en ambos?", "Arroz, pollo y manzana", "Los dos textos nombran rice, chicken y apple."),
        arith("Lee: «Mia has six eggs. She gives two eggs to a friend.» ¿Cuántos huevos le quedan?", "6-2", "Se restan los huevos que regala."),
    ],
    [("En la cafetería de la escuela dicen: «What do you want? I want an apple, please.» ¿Qué quiere quien responde?", "Una manzana", "I want an apple, please.")],
    [
        ("¿Qué significa «many»?", "Muchas o muchos", "Many indica una cantidad grande."),
        ("¿Qué significa «some»?", "Algunas o algunos", "Some no incluye a todos."),
        ("¿Cómo se dice «arroz» en inglés?", "rice", "Rice es arroz."),
    ],
    task("Lee: «For lunch Ana has soup and an apple. She drinks water. On Easter, Ana makes a card with a basket and three eggs.» Escribe qué come y bebe Ana en el almuerzo, cuántos huevos dibuja en la tarjeta y una frase con I want... para pedir algo de comer.", "Sopa, manzana y agua; tres huevos; por ejemplo: I want soup, please.", ["escribe la comida y la bebida", "escribe 3", "escribe una frase con I want"], ["hoja con las respuestas", "nota del adulto"], ["escribir que come chicken", "escribir otro número de huevos"], "Reconoce lo bien leído y vuelve a leer con él la frase del almuerzo."),
    "Lee en voz alta «What do you want? I want rice, please.» con una persona de tu casa.",
    "Escribe un menú de tres comidas en inglés con un número, como «There are ten apples».",
)

# ---------------------------------------------------------------- clase 5
lesson(
    OA7, 5,
    "Los textos escritos en cada ejercicio; lápiz y papel.",
    "Aprenderé a comparar la información de dos textos sin usar estereotipos: veo qué dice cada texto, qué tienen en común y qué cambia. Sirve para leer con justicia y no suponer cosas que el texto no dice.",
    ["Sé leer textos sobre ocupaciones y animales.", "Sé que cualquier persona puede tener cualquier ocupación."],
    [
        "Comparar es buscar qué tienen en común dos cosas y en qué se diferencian. Con dos textos, lee cada uno y anota datos concretos: qué hace, dónde está, cuántos hay, cómo es. Luego usa palabras como both (los dos) y but (pero): «Both animals live in groups, but only the zebra has stripes».",
        "Un estereotipo es una idea simplificada e injusta sobre un grupo de personas, como «solo los hombres pueden ser bomberos». Un texto dice lo que hace una persona concreta, no lo que pueden hacer todas las personas de un grupo. Una frase como «Eva is a firefighter» muestra que una mujer puede serlo.",
        "Para comparar sin estereotipos, usa solo la evidencia del texto y evita frases con «solo» o «siempre» si el texto no las dice. Una buena comparación nombra el dato del texto, no la opinión sobre quién puede o no puede hacer algo.",
    ],
    [("compare", "comparar"), ("both", "los dos"), ("but", "pero"), ("firefighter", "bombero o bombera"), ("nurse", "enfermero o enfermera"), ("emergency", "emergencia"), ("stereotype", "estereotipo: idea simplificada e injusta")],
    [
        ("Comparar datos", "Lee: " + ANIM + " (leaves = hojas, stripes = rayas, groups = grupos). ¿Qué tienen en común el elefante y la cebra?", ["Busco both.", "Dice Both animals live in groups.", "Los dos viven en grupos."], "Los dos viven en grupos"),
        ("Evidencia contra un estereotipo", "Lee: " + FIRE + " (helps = ayuda, emergency = emergencia). Pedro dice que los bomberos son solo hombres. ¿Qué frase del texto lo contradice?", ["Busco la frase que nombra a Eva.", "Dice Eva is a firefighter.", "Eva es una mujer bombera."], "Eva is a firefighter"),
    ],
    [
        ("Generalizar de una persona a todo un grupo.", "El texto habla de una persona concreta.", "Usa solo lo que el texto dice de esa persona."),
        ("Comparar sin dar datos del texto.", "Una opinión no es evidencia.", "Nombra un dato de cada texto."),
    ],
    [
        ("Lee: " + FIRE + " ¿Qué hace Eva?", "Ayuda a personas en una emergencia", "She helps people in an emergency."),
        ("Lee: " + NURSE + " (nurse = enfermero o enfermera, sick = enfermo). ¿Dónde trabaja Tom?", "En un hospital", "He works at a hospital."),
        ("Lee: " + ANIM + " ¿Qué animal tiene rayas?", "La cebra", "The zebra has stripes."),
    ],
    [
        ("Lee: " + ANIM + " ¿Qué animal es grande?", "El elefante", "The elephant is big."),
        ("En Inglés: ¿Qué es un estereotipo?", "Una idea simplificada e injusta sobre un grupo", "Dice que todas las personas de un grupo son iguales."),
        ("Lee: " + FIRE + " Y: " + NURSE + " ¿Qué tienen en común Eva y Tom?", "Los dos ayudan a las personas", "Eva ayuda en una emergencia y Tom ayuda a personas enfermas."),
    ],
    [
        ("Lee: " + NURSE + " ¿Quién trabaja en un hospital: Eva o Tom?", "Tom", "El texto dice que Tom works at a hospital."),
        ("¿Cuál frase es un estereotipo? a) Tom is a nurse. b) Only girls can be nurses.", "b", "La b dice que solo un grupo puede tener un trabajo."),
        ("Lee: " + ANIM + " ¿Qué dos palabras comparan a los animales: both y but?", "Both indica lo común y but indica una diferencia", "Both dice los dos y but dice pero."),
    ],
    [
        ("Lee: " + NURSE + " Ana dice que todas las personas enfermeras son hombres porque Tom es enfermero. ¿Es válido?", "No; el texto habla solo de Tom", "Una persona no representa a todo un grupo."),
        ("Lee: " + FIRE + " Luis dice que Eva no puede correr rápido. ¿Qué frase lo contradice?", "Eva can run fast", "Can run fast dice que corre rápido."),
    ],
    [
        ("Elige la frase que compara sin estereotipos: a) Both Eva and Tom help people. b) Tom is a boy so he cannot cook.", "a", "La a usa datos de los textos; la b supone algo injusto."),
        ("Lee: " + ANIM + " ¿Qué comen ambos animales?", "Plantas: hojas y pasto", "El elefante come hojas y la cebra come pasto."),
    ],
    [("En un cartel de la escuela lees: «Boys and girls can play football.» (football = fútbol). ¿Qué dice el cartel?", "Que niños y niñas pueden jugar fútbol", "Boys and girls can play significa niños y niñas pueden jugar.")],
    [
        ("¿Qué significa «both»?", "Los dos", "Both nombra dos cosas juntas."),
        ("¿Qué significa «but»?", "Pero", "But marca una diferencia."),
        ("¿Qué debes usar para comparar sin estereotipos?", "Datos concretos del texto", "La evidencia viene del texto."),
    ],
    task("Lee: «Sam is a cook. He cooks soup. Pam is a cook, too. She cooks rice. Both Sam and Pam work in a kitchen.» Escribe una frase de comparación con Both y otra con but. No uses ideas sobre quién puede ser cocinero.", "Both Sam and Pam are cooks. Sam cooks soup, but Pam cooks rice.", ["usa Both con un dato del texto", "usa but con una diferencia del texto", "no agrega ideas sobre quién puede ser cocinero"], ["hoja con las dos frases", "nota del adulto"], ["decir que los cocineros son solo hombres", "no usar datos del texto"], "Reconoce los datos del texto y vuelve a leer con él la frase con but."),
    "Lee en voz alta «Both» y «but» y di una frase con cada una usando animales.",
    "Escribe una comparación de dos animales salvajes con Both y but, sin inventar datos.",
)
