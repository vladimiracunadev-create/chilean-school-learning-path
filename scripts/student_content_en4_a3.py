"""Student material for 4.º básico Inglés (propuesta), EN04 OA 03 (demostrar comprensión de textos orales).

Las «escuchas» las lee un adulto en voz alta; el guion va en el enunciado. Los sonidos /s/-/z/ y /w/-/th/ se trabajan
con preguntas de conocimiento (qué palabra lleva cada sonido), porque el audio lo produce el adulto o el docente.
"""
from __future__ import annotations

from student_content_en4_a import ADULT, E, lesson, task
from student_lessons import arith

OA3 = "EN04 OA 03"

ROOM = "«In the classroom there is a teacher, a girl and a boy. The teacher has a ruler. The girl has a book. The boy has a pencil.»"
ZOO1 = "«In the zoo, I see a lion, a zebra and two monkeys. The lion is big. The monkeys are small.»"
ZOO2 = "«At the zoo there are three elephants, two giraffes and eight monkeys. The elephants are grey. The giraffes are tall. The monkeys are on the trees.»"
MIA = "«Mia likes her school. She has a good teacher. She reads in the library. She plays in the yard with her friends.»"
ZEB = "«The zebra has black and white stripes. It eats grass. It runs fast.»"
EGG = "«First, Eva paints an egg. Then she puts it in a basket. Finally, she gives it to a friend.»"
ZEB2 = "«First, the zebra walks to the river. Then it drinks water. Finally, it runs back to the other zebras.»"
SAND = "«First, Tom takes two slices of bread. Then he puts cheese on the bread. Finally, he eats the sandwich.»"
KIT = "«Tom is in the kitchen. He is cooking rice. He has a red apron. He is happy.»"
LION = "«A lion is sleeping under a tree. The lion is big. It is hot today.»"

# ---------------------------------------------------------------- clase 1
lesson(
    OA3, 1,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a identificar personas, animales y objetos en lo que escucho, y a distinguir los sonidos /s/ y /z/ del inglés. Sirve para no confundir palabras que suenan parecido.",
    ["Sé nombrar objetos de la escuela como ruler, book y pencil.", "Conozco animales salvajes como lion, zebra y monkey."],
    [
        "Cuando escuchas un texto, primero identifica quién o qué aparece: personas (teacher, girl, boy), animales (lion, zebra, monkey) y objetos (ruler, book, pencil). Las palabras clave suelen ser sustantivos. Un sustantivo es una palabra que nombra personas, animales, lugares u objetos.",
        "Hay sonidos del inglés que pueden confundirte. El sonido /s/ es un soplido sin vibración, como en «sip». El sonido /z/ es parecido, pero hace vibrar la garganta, como en «zip». Tócate la garganta y compruébalo. Los pares son sip y zip, bus y buzz, Sue y zoo, ice y eyes, peace y peas.",
        "En español la letra z suena como /s/, por eso muchas personas dicen /s/ en lugar de /z/. Si dices «bus» en lugar de «buzz», cambias la palabra: bus es autobús y buzz es zumbido. Escucha el sonido y pregúntate qué palabra tiene sentido en el texto.",
    ],
    [("teacher / girl / boy", "profesora o profesor / niña / niño"), ("ruler / book / pencil", "regla / libro / lápiz"), ("zoo", "zoológico"), ("monkey", "mono"), ("/s/ y /z/", "dos sonidos: sin vibración y con vibración"), ("bus / buzz", "autobús / zumbido"), ("noun", "sustantivo: nombra personas, animales, lugares u objetos")],
    [
        ("Identificar personas y objetos", ADULT + ROOM + " (classroom = sala de clases). ¿Quién tiene el libro?", ["Busco book.", "Antes oigo the girl has.", "La niña tiene el libro."], "La niña"),
        ("Distinguir /s/ y /z/", "¿Qué palabra tiene el sonido /z/ al final: bus o buzz?", ["Bus termina en /s/.", "Buzz termina en /z/, con vibración.", "Elijo buzz."], "buzz"),
    ],
    [
        ("Decir que bus y buzz son la misma palabra porque se parecen.", "Se ignora la diferencia entre /s/ y /z/.", "Bus es autobús y buzz es zumbido: el sonido final cambia el significado."),
        ("Pensar que en inglés la letra z siempre suena como /s/.", "En español la z suena /s/, pero en inglés suena /z/.", "En inglés z hace vibrar la garganta, como en zoo."),
    ],
    [
        (ADULT + ROOM + " ¿Cuántas personas aparecen en el texto?", "3", "Aparecen la profesora, la niña y el niño."),
        (ADULT + ROOM + " ¿Qué tiene el niño?", "Un lápiz", "The boy has a pencil."),
        (ADULT + ROOM + " ¿Quién tiene la regla?", "La profesora", "The teacher has a ruler."),
    ],
    [
        ("¿Qué sonido hace vibrar la garganta: /s/ o /z/?", "/z/", "El sonido /z/ es el que vibra."),
        ("¿Con qué sonido comienza la palabra zoo?", "/z/", "Zoo comienza con /z/."),
        ("¿Cuál de estas palabras termina con el sonido /z/: bus o buzz?", "buzz", "Buzz termina con /z/ y bus con /s/."),
    ],
    [
        (ADULT + ZOO1 + " (see = ver, big = grande, small = pequeño). ¿Qué animales aparecen?", "Un león, una cebra y dos monos", "Lion, zebra y monkeys son los animales que se nombran."),
        arith(ADULT + ZOO1 + " ¿Cuántos animales hay en total?", "1+1+2", "Se suman todos los animales."),
        ("En «Sue sees a zebra at the zoo», ¿qué dos palabras comienzan con el sonido /z/?", "zebra y zoo", "Zebra y zoo comienzan con /z/; Sue y sees con /s/."),
    ],
    [
        ("Pedro dice que «ice» y «eyes» suenan igual al final. ¿Tiene razón?", "No; ice termina en /s/ y eyes en /z/", "El sonido final es distinto: sin vibración y con vibración."),
        ("Lee: " + ZOO1 + " María dice que el león es pequeño. Según el texto, ¿cómo es el león?", "Grande", "El texto dice The lion is big."),
    ],
    [
        ("¿Cuáles de estas palabras terminan con el sonido /z/: peas, ice, buzz, rice?", "peas y buzz", "Peas y buzz terminan con /z/; ice y rice con /s/."),
        arith(ADULT + "«My school bag has a book, a ruler, three pencils and a box.» (bag = mochila, box = caja). ¿Cuántos objetos hay en la mochila? Cuenta un libro, una regla, tres lápices y una caja.", "1+1+3+1", "Se suman todos los objetos."),
    ],
    [(ADULT + "En el recreo escuchas «Look! A monkey!» (look = mira). ¿Qué animal aparece?", "Un mono", "Monkey significa mono.")],
    [
        ("En Inglés: ¿qué es un sustantivo?", "Una palabra que nombra personas, animales, lugares u objetos", "Teacher, lion y ruler son sustantivos."),
        ("¿Cómo se dice «mono» en inglés?", "monkey", "Monkey es mono."),
        ("¿Qué palabra tiene /z/ al comienzo: Sue o zoo?", "zoo", "Zoo comienza con /z/."),
    ],
    task("Un adulto lee dos veces: «In the zoo, I see a zebra, a lion and three monkeys. The zebra has stripes. The monkeys are on a tree.» Dibuja los tres tipos de animales y escribe debajo cuántos hay de cada uno. Anota las dos palabras que comienzan con /z/.", "Una cebra, un león y tres monos; palabras con /z/: zoo y zebra.", ["dibuja los tres animales", "escribe 1, 1 y 3", "anota zoo y zebra"], ["dibujo del estudiante", "nota del adulto"], ["dibujar dos monos", "anotar sea o sun, que comienzan con /s/"], "Reconoce lo bien identificado y vuelve a escuchar solo la parte donde se equivocó."),
    "Pide a un adulto que diga «zoo, Sue, zip, sip» y levanta la mano solo cuando oigas /z/.",
    "Escribe tres frases con animales del zoo, por ejemplo «I see a zebra at the zoo.»",
)

# ---------------------------------------------------------------- clase 2
lesson(
    OA3, 2,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a elegir la idea general de lo que escucho: de qué trata todo el texto, no solo una parte. Sirve para resumir un texto oral con una frase.",
    ["Sé identificar personas, animales y objetos en un texto.", "Conozco palabras como school, zebra y Easter."],
    [
        "La idea general (main idea) es lo más importante de todo un texto. Responde a la pregunta «¿de qué trata?». Un detalle (detail) es una información pequeña que ayuda a explicar la idea general. Por ejemplo, «Mia reads in the library» es un detalle sobre su escuela.",
        "Para elegir la idea general, escucha todo el texto y pregúntate de qué hablan casi todas las frases. Las frases que hablan de lo mismo apoyan la misma idea. Una buena idea general sirve para todo el texto, no solo para una frase. Un título (title) corto también puede mostrar la idea general.",
        "Ten cuidado con las opciones que nombran solo un detalle. Si el texto habla de la escuela de Mia, la idea no es «Mia lee». Esa frase solo es una parte. También descarta las opciones que dicen algo que el texto no dice.",
    ],
    [("main idea", "idea general: de qué trata todo el texto"), ("detail", "detalle: información pequeña que apoya la idea"), ("title", "título"), ("likes", "le gusta"), ("library", "biblioteca"), ("stripes", "rayas"), ("grass", "pasto")],
    [
        ("Elegir la idea general", ADULT + MIA + " (likes = le gusta, library = biblioteca, yard = patio). Elige la idea general: a) A Mia le gusta su escuela b) Mia está en el zoológico c) Mia no tiene amigos.", ["Las frases hablan de su profesora, la biblioteca y el patio.", "Todas hablan de su escuela.", "La idea general es la a."], "a"),
        ("Distinguir detalle", "En el mismo texto, ¿«Mia reads in the library» es una idea general o un detalle?", ["Esa frase habla de una sola actividad.", "Apoya la idea de que le gusta su escuela.", "Es un detalle."], "Un detalle"),
    ],
    [
        ("Elegir como idea general una frase que solo es un detalle.", "Un detalle solo explica una parte del texto.", "Elige la opción que sirva para todas las frases del texto."),
        ("Elegir una opción porque tiene una palabra conocida, como zoo.", "La palabra aparece, pero el texto no trata de eso.", "Comprueba que la opción describa todo el texto."),
    ],
    [
        (ADULT + ZEB + " (stripes = rayas, grass = pasto, fast = rápido). ¿De qué animal habla el texto?", "De una cebra", "El texto describe a la cebra."),
        ("¿Para qué sirve la idea general?", "Para decir de qué trata todo el texto", "La idea general resume el texto."),
        (ADULT + "«The lion is big. The lion is strong. The lion sleeps under a tree.» (strong = fuerte). ¿De qué animal trata el texto?", "Del león", "Todas las frases hablan del león."),
    ],
    [
        ("«Mia reads in the library». ¿Es una idea general o un dato pequeño?", "Un dato pequeño", "Habla de una sola actividad de Mia."),
        (ADULT + "«It is Easter. Leo and Ana are making cards. Leo draws an egg. Ana draws a basket.» (cards = tarjetas, basket = canasta). ¿Cuál es la idea general? a) Leo y Ana hacen tarjetas de Easter b) Leo come un huevo.", "a", "Todas las frases hablan de hacer tarjetas de Easter."),
        ("Lee: " + ZEB + " ¿Qué título es mejor: The Zebra o The Kitchen?", "The Zebra", "El texto describe a la cebra, no una cocina."),
    ],
    [
        (ADULT + "«I am hungry. I eat rice and chicken. I drink water. Now I am happy.» (chicken = pollo). ¿Cuál es la idea general? a) Una persona almuerza y queda contenta b) Una persona corre en el parque.", "a", "Come, bebe y al final está feliz."),
        (ADULT + "«My house has a kitchen, a bathroom and two bedrooms. The kitchen is big.» (house = casa, bathroom = baño). ¿Cuál es la idea general? a) Cómo es una casa b) Cómo es un zoológico.", "a", "Todas las frases describen partes de una casa."),
        (ADULT + MIA + " Elige el mejor título: a) My School b) A Big Lion c) The Kitchen.", "a", "Todo el texto trata de la escuela de Mia."),
    ],
    [
        ("Lee: " + ZEB + " Ana dice que la idea general es «The zebra runs». ¿Tiene razón?", "No; el texto describe a la cebra y correr es solo un detalle", "La idea general debe servir para todo el texto."),
        ("Lee: " + MIA + " ¿Cuál frase es solo un detalle? a) She plays in the yard. b) Mia likes her school.", "a", "She plays in the yard es una actividad; la b resume el texto."),
    ],
    [
        (ADULT + "«A giraffe is tall. A giraffe has a long neck. A giraffe eats leaves.» (leaves = hojas). ¿Cuál es la idea general? a) A giraffe eats leaves b) El texto describe una jirafa.", "b", "La a es solo un detalle; la b sirve para todo el texto."),
        ("En el texto de Mia hay tres detalles: tiene una buena profesora, lee en la biblioteca y juega en el patio. ¿Cuántos detalles apoyan la idea de que le gusta su escuela?", "3", "Los tres datos apoyan la misma idea."),
    ],
    [(ADULT + "En clase escuchas: «This is my school. I have a teacher. I have a book. I have friends.» ¿Cuál es la idea general? a) Mi escuela b) Mi casa.", "a", "Todas las frases hablan de la escuela.")],
    [
        ("En Inglés: ¿qué es un detalle de un texto oral?", "Una información pequeña que apoya la idea general", "Un detalle explica una parte del texto."),
        ("¿Qué significa «title»?", "Título", "Title es el nombre del texto."),
        ("¿De qué pregunta es respuesta la idea general?", "¿De qué trata el texto?", "Resume el texto completo."),
    ],
    task("Un adulto lee dos veces: «Leo has a cat. The cat is small. The cat has a black tail. Leo gives water to the cat.» (tail = cola, gives = da, water = agua). Escribe la idea general en una frase corta, como «The text is about a cat». Luego escribe un detalle del texto.", "Idea general: el texto trata del gato de Leo. Detalle: el gato tiene una cola negra.", ["escribe una idea general que sirva para todo el texto", "escribe un detalle correcto", "no repite el detalle como idea general"], ["hoja con idea y detalle", "nota del adulto"], ["poner un detalle como idea general", "decir que trata de un perro"], "Reconoce la idea y vuelve a leer con él las frases para comprobar que apoyan la misma idea."),
    "Pide a un adulto que lea «The zebra has stripes» y di de qué animal habla.",
    "Escribe un texto de tres frases sobre tu animal salvaje favorito y subraya la frase que resume el texto.",
)

# ---------------------------------------------------------------- clase 3
lesson(
    OA3, 3,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a encontrar un dato explícito, es decir, dicho directamente en el texto, y a distinguir los sonidos /w/ y /th/ del inglés. Sirve para responder preguntas precisas sobre lo que escucho.",
    ["Sé elegir la idea general de un texto.", "Sé contar hasta veinte en inglés."],
    [
        "Un dato explícito (explicit detail) es una información que el texto dice con claras palabras: un número, un color, un lugar o un nombre. Para encontrarlo, escucha la pregunta, busca la palabra clave en el texto y fíjate en lo que viene alrededor. No hace falta adivinar ni inventar.",
        "Hay dos sonidos del inglés que se confunden. El sonido /w/ se hace redondeando los labios, como en «wing» (ala). El sonido /th/ se hace poniendo la punta de la lengua entre los dientes y soplando, como en «thing» (cosa). Hay pares como wing y thing, wink y think, win y thin.",
        "Si cambias /th/ por /w/, cambias la palabra. «Win» es ganar y «thin» es delgado. «Think» es pensar y «wink» es guiñar un ojo. Escucha el sonido del comienzo de la palabra y revisa si tiene sentido en el texto.",
    ],
    [("explicit detail", "dato dicho directamente en el texto"), ("wing / thing", "ala / cosa"), ("wink / think", "guiñar / pensar"), ("win / thin", "ganar / delgado"), ("elephant / giraffe", "elefante / jirafa"), ("grey", "gris"), ("lunch", "almuerzo")],
    [
        ("Encontrar un número", ADULT + ZOO2 + " (grey = gris, tall = alto, trees = árboles). ¿Cuántas jirafas hay?", ["Busco giraffes.", "Antes oigo two.", "Hay dos jirafas."], "2"),
        ("Distinguir /w/ y /th/", "¿Qué palabra tiene el sonido /th/ al comienzo: wing o thing?", ["Wing comienza con /w/, con los labios redondos.", "Thing comienza con /th/, con la lengua entre los dientes.", "Elijo thing."], "thing"),
    ],
    [
        ("Responder con un dato que no está en el texto, como inventar un color.", "No se busca el dato explícito.", "Busca la palabra clave y usa solo lo que el texto dice."),
        ("Decir que win y thin suenan igual porque empiezan con letras parecidas.", "Se ignora la diferencia entre /w/ y /th/.", "Win comienza con /w/ y thin con /th/; cambian el significado."),
    ],
    [
        (ADULT + ZOO2 + " ¿De qué color son los elefantes?", "Grises", "El texto dice The elephants are grey."),
        (ADULT + ZOO2 + " ¿Dónde están los monos?", "En los árboles", "The monkeys are on the trees."),
        (ADULT + ZOO2 + " ¿Cuántos monos hay?", "8", "Eight monkeys significa ocho monos."),
    ],
    [
        ("¿Qué sonido se hace redondeando los labios: /w/ o /th/?", "/w/", "El sonido /w/ usa los labios redondos."),
        ("En el sonido /th/, ¿dónde pones la punta de la lengua?", "Entre los dientes", "Así se produce el sonido /th/."),
        ("¿Qué significa «thin»?", "Delgado", "Thin es delgado y win es ganar."),
    ],
    [
        arith(ADULT + ZOO2 + " ¿Cuántos animales hay en total?", "3+2+8", "Se suman los animales de cada tipo."),
        (ADULT + "«Leo has lunch. He eats rice, chicken and an apple. He drinks water.» (lunch = almuerzo). ¿Qué bebe Leo?", "Agua", "Drinks water significa bebe agua."),
        ("En «I think it is a thin wing», ¿cuántas palabras tienen el sonido /th/ al comienzo?", "2", "Think y thin comienzan con /th/; wing comienza con /w/."),
    ],
    [
        ("Luis oyó thing pero escribió wing. ¿Qué dos sonidos confundió?", "/th/ con /w/", "Thing comienza con /th/ y wing con /w/."),
        ("Lee: " + ZOO2 + " Ana dice que hay tres jirafas. ¿Qué dato del texto lo contradice?", "El texto dice two giraffes, o sea dos jirafas", "El número explícito es dos."),
    ],
    [
        arith(ADULT + "«At the zoo there are eight monkeys and three elephants.» ¿Cuántos monos más que elefantes hay?", "8-3", "Se resta el número de elefantes al de monos."),
        ("¿Cuál de estas palabras no tiene el sonido /th/: think, thin, win, thing?", "win", "Win comienza con /w/; las otras con /th/."),
    ],
    [(ADULT + "La profesora dice: «The ruler is on the desk. The pencils are in the box. There are fourteen pencils.» (desk = escritorio). ¿Cuántos lápices hay?", "14", "Fourteen significa catorce.")],
    [
        ("En Inglés: ¿qué es un dato explícito?", "Un dato que el texto dice directamente", "No hace falta adivinarlo."),
        ("¿Qué significa «think»?", "Pensar", "Think comienza con /th/."),
        ("¿Qué significa «wink»?", "Guiñar un ojo", "Wink comienza con /w/."),
    ],
    task("Un adulto lee dos veces: «At the zoo there are five giraffes and ten monkeys. The giraffes are tall. The monkeys eat bananas.» Escribe tres datos: cuántas jirafas hay, cuántos monos hay y qué comen los monos. Después escribe una palabra con el sonido /th/ y otra con /w/ de las que aprendiste.", "Cinco jirafas, diez monos, comen bananas; por ejemplo thing y wing.", ["escribe 5, 10 y bananas", "escribe una palabra con /th/", "escribe una palabra con /w/"], ["hoja con los datos", "nota del adulto"], ["decir que comen pasto", "confundir los números"], "Reconoce los datos bien ubicados y vuelve a leer con él la pregunta para buscar la palabra clave."),
    "Pide a un adulto que diga «wing» y «thing» y muestra con los labios y la lengua cuál es cuál.",
    "Escribe cuatro datos de un texto del zoo sobre animales, con números del uno al veinte.",
)

# ---------------------------------------------------------------- clase 4
lesson(
    OA3, 4,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a ordenar tres sucesos de un texto que escucho con first, then y finally. Sirve para contar qué pasó primero, después y al final.",
    ["Sé que first es primero y finally es finalmente.", "Sé ordenar un cuento corto de cuatro pasos."],
    [
        "Muchos textos orales cuentan sucesos (events) en un orden. Para ordenar tres sucesos, busca las palabras first (primero), then (luego) y finally (finalmente). El suceso con first se hace antes y el suceso con finally se hace al final. Then está en medio.",
        "En los textos de hoy hay acciones como paints an egg (pinta un huevo), puts it in a basket (lo pone en una canasta), walks to the river (camina al río), drinks water (bebe agua), takes bread (toma pan) y eats (come). Cada una es un suceso.",
        "Un texto puede decir algo que no es un suceso, como «He likes the library» (le gusta la biblioteca). Eso describe y no ordena. Para ordenar, escribe 1, 2 y 3 junto a los sucesos y comprueba que tengan sentido en la vida real.",
    ],
    [("event", "suceso: algo que pasa"), ("first", "primero"), ("then", "luego"), ("finally", "finalmente"), ("paint", "pintar"), ("river", "río"), ("slice of bread", "rebanada de pan")],
    [
        ("Ordenar sucesos", ADULT + EGG + " (paints = pinta, gives = da, basket = canasta). ¿Qué hace Eva primero?", ["Busco first.", "Después de first oigo paints an egg.", "Eso ocurre primero."], "Pinta un huevo"),
        ("Último suceso", "En el mismo texto, ¿qué hace Eva al final?", ["Busco finally.", "Después de finally oigo gives it to a friend.", "Eso ocurre al final."], "Se lo da a un amigo"),
    ],
    [
        ("Ordenar por lo que parece más importante y no por las palabras de orden.", "Se ignora first, then y finally.", "Usa first, then y finally para numerar los sucesos."),
        ("Contar como suceso una frase que solo describe, como «He likes the library».", "No es una acción que ocurre.", "Cuenta solo las acciones con palabras de orden."),
    ],
    [
        (ADULT + EGG + " ¿Qué palabra significa «luego»?", "then", "Then une el primer suceso con el siguiente."),
        (ADULT + EGG + " ¿Qué hace Eva al final?", "Se lo da a un amigo", "Finally dice she gives it to a friend."),
        ("¿Qué palabra de orden va en medio: first, then o finally?", "then", "Then va entre first y finally."),
    ],
    [
        ("Lee: " + EGG + " ¿Cuántos sucesos hay?", "3", "Pinta, pone en la canasta y entrega: tres sucesos."),
        (ADULT + ZEB2 + " (walks = camina, drinks = bebe, runs back = corre de vuelta). ¿Qué pasa después de que la cebra bebe agua?", "Corre de vuelta con las otras cebras", "Finally dice it runs back to the other zebras."),
        ("Lee: " + ZEB2 + " ¿Qué palabra marca el segundo suceso?", "then", "Then va antes de drinks water."),
    ],
    [
        (ADULT + SAND + " (slice = rebanada, cheese = queso, bread = pan). ¿Qué pone Tom sobre el pan?", "Queso", "Then he puts cheese on the bread."),
        ("Lee: " + SAND + " Ordena: A) Come el sándwich. B) Toma dos rebanadas de pan. C) Pone queso sobre el pan.", "B, C, A", "El texto sigue: toma pan, pone queso, come."),
        ("Lee: " + ZEB2 + " Ordena: A) Corre de vuelta. B) Camina al río. C) Bebe agua.", "B, C, A", "El texto sigue: camina, bebe, corre."),
    ],
    [
        ("Ana dice que Eva da el huevo a su amiga antes de pintarlo. ¿Tiene razón?", "No; primero lo pinta", "Paints an egg viene con first."),
        ("Lee: " + ZEB2 + " ¿Qué hace justo antes de correr de vuelta?", "Bebe agua", "Then drinks water está antes de finally."),
    ],
    [
        (ADULT + "«Leo is at school. First, he reads a book. Then he draws a circle. Finally, he goes home. He likes the library.» (goes home = va a casa). ¿Qué hace Leo después de leer?", "Dibuja un círculo", "Then dice he draws a circle."),
        ("Lee: «Leo is at school. First, he reads a book. Then he draws a circle. Finally, he goes home. He likes the library.» ¿Cuántos sucesos se ordenan, sin contar «He likes the library»?", "3", "Lee, dibuja y va a casa."),
    ],
    [(ADULT + "En clase escuchas: «First, a girl takes a red crayon. Then she draws a circle. Finally, she shows the drawing to the teacher.» (shows = muestra). Ordena: A) Muestra el dibujo. B) Dibuja un círculo. C) Toma un lápiz de cera.", "C, B, A", "El texto sigue: toma, dibuja, muestra.")],
    [
        ("¿Qué significa «finally»?", "Finalmente", "Finally marca el último suceso."),
        ("¿Qué significa «paints an egg»?", "Pinta un huevo", "Paints es pinta y egg es huevo."),
        ("¿Qué suceso va primero: el que tiene first o el que tiene finally?", "El que tiene first", "First significa primero."),
    ],
    task("Un adulto lee dos veces: «First, Ben takes a red crayon. Then he draws an egg. Finally, he gives the egg card to a friend.» (egg card = tarjeta con un huevo). Dibuja tres cuadros numerados 1, 2 y 3, uno por cada suceso. Escribe en cada cuadro first, then o finally.", "1 first (toma un lápiz de cera), 2 then (dibuja un huevo), 3 finally (da la tarjeta).", ["dibuja los tres sucesos en orden", "escribe first, then y finally en el lugar correcto", "el último cuadro muestra la entrega"], ["dibujo del estudiante", "nota del adulto"], ["poner finally en el primer cuadro", "dibujar solo dos sucesos"], "Reconoce el orden correcto y vuelve a leer con él first y finally."),
    "Pide a un adulto que diga «first, then, finally» y muestra con los dedos 1, 2 y 3.",
    "Escribe tres sucesos de tu mañana con first, then y finally, por ejemplo «First, I wake up.»",
)

# ---------------------------------------------------------------- clase 5
lesson(
    OA3, 5,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a mostrar evidencia de una respuesta: digo mi respuesta y señalo la frase del texto que la prueba. Sirve para explicar por qué entendí lo que escuché.",
    ["Sé encontrar la idea general, un dato y el orden de sucesos.", "Sé usar because en español como porque."],
    [
        "La evidencia (evidence) es la parte del texto que prueba tu respuesta. Para mostrarla, di tu respuesta y luego «because I heard...», que significa «porque oí...». Después repite la frase o la palabra clave del texto. Así otra persona puede comprobar que no adivinaste.",
        "Por ejemplo, si el texto dice «Tom is cooking rice» y te preguntan qué hace Tom, tu respuesta es «Tom cocina» y tu evidencia es «Tom is cooking rice». Una evidencia debe estar en el texto: no sirve decir «yo creo» ni inventar un dato.",
        "Cuando una respuesta tiene evidencia, también puedes corregir una idea equivocada. Si alguien dice que Tom está triste, la evidencia «He is happy» muestra que no. Para escoger una buena evidencia, busca la frase que dice exactamente lo mismo que tu respuesta.",
    ],
    [("evidence", "evidencia: la parte del texto que prueba la respuesta"), ("because", "porque"), ("I heard...", "yo oí..."), ("kitchen", "cocina"), ("apron", "delantal"), ("hot", "caluroso, con calor"), ("cooking", "cocinando")],
    [
        ("Respuesta con evidencia", ADULT + KIT + " (kitchen = cocina, apron = delantal). ¿Qué hace Tom y qué frase lo prueba?", ["Busco la acción: cooking rice.", "La respuesta es que cocina arroz.", "La evidencia es «He is cooking rice»."], "Cocina arroz; la frase es «He is cooking rice»"),
        ("Elegir evidencia", "Para probar que Tom está contento, ¿qué frase del texto sirve? a) He has a red apron b) He is happy.", ["Busco una frase sobre cómo se siente.", "La b dice happy.", "La a solo habla de su delantal."], "b"),
    ],
    [
        ("Responder «yo creo que sí» sin señalar ninguna frase del texto.", "No se muestra evidencia.", "Agrega because I heard... y la frase del texto."),
        ("Usar como evidencia una frase que habla de otra cosa.", "La frase no prueba la respuesta.", "Busca la frase que dice lo mismo que tu respuesta."),
    ],
    [
        (ADULT + KIT + " ¿Dónde está Tom?", "En la cocina", "Tom is in the kitchen."),
        (ADULT + KIT + " ¿Qué cocina Tom?", "Arroz", "He is cooking rice."),
        ("¿Qué significa «because»?", "Porque", "Because introduce la razón de una respuesta."),
    ],
    [
        ("¿Qué debes señalar para mostrar evidencia?", "La parte del texto que apoya mi respuesta", "La evidencia viene del texto."),
        ("Elige la mejor respuesta con evidencia: a) Tom cocina. b) Tom cocina porque oí «He is cooking rice».", "b", "La b agrega la frase del texto como evidencia."),
        ("Lee: " + KIT + " ¿Qué frase prueba que usa un delantal rojo?", "He has a red apron", "Apron es delantal y red es rojo."),
    ],
    [
        (ADULT + LION + " (hot = caluroso). ¿Qué hace el león?", "Duerme", "A lion is sleeping under a tree."),
        (ADULT + LION + " ¿Qué frase prueba que el león es grande?", "The lion is big", "Esa frase lo dice directamente."),
        (ADULT + LION + " ¿Dónde duerme el león?", "Debajo de un árbol", "Under a tree significa debajo de un árbol."),
    ],
    [
        ("Lee: " + KIT + " Pedro dice que Tom está triste. ¿Qué frase lo contradice?", "He is happy", "Happy significa feliz."),
        ("Lee: " + LION + " Ana dice que el león corre. ¿Qué frase corrige su idea? a) A lion is sleeping under a tree. b) The lion is big.", "a", "Sleeping muestra que no corre."),
    ],
    [
        arith(ADULT + "«Mia has a school bag. In the bag there are two books, one ruler and three pencils.» ¿Cuántos objetos hay en la mochila?", "2+1+3", "Se suman los libros, la regla y los lápices."),
        ("Lee: «Mia has a school bag. In the bag there are two books, one ruler and three pencils.» Ana dice que hay cuatro lápices. ¿Qué número dice el texto y qué frase lo prueba?", "Tres lápices; la frase es «three pencils»", "El texto dice three pencils."),
    ],
    [("En clase, un niño responde: «Tom está feliz porque oí \"He is happy\".» ¿Qué parte de su respuesta es la evidencia?", "He is happy", "Es la frase del texto que apoya su respuesta.")],
    [
        ("En Inglés: ¿qué es la evidencia de una respuesta?", "La parte del texto que la prueba", "Se toma del texto, no de la imaginación."),
        ("¿Qué significa «I heard...»?", "Yo oí...", "Heard viene de hear, oír."),
        ("¿Sirve decir «yo creo» como evidencia?", "No", "La evidencia debe estar en el texto."),
    ],
    task("Un adulto lee dos veces: «Eva is in the kitchen. She is cooking soup. She has a red apron. She is happy.» (soup = sopa). Escribe una respuesta con evidencia: «Eva ___ because I heard ___.» sobre qué hace Eva. Luego escribe una segunda con evidencia sobre cómo se siente.", "Eva cocina sopa porque oí «She is cooking soup»; Eva está feliz porque oí «She is happy».", ["responde qué hace Eva", "copia o dice la frase como evidencia", "responde cómo se siente con otra evidencia"], ["hoja con las dos respuestas", "nota del adulto"], ["poner una frase de otra cosa como evidencia", "no usar because"], "Reconoce la respuesta con evidencia y vuelve a leer con él la frase que apoya la segunda."),
    "Pide a un adulto que lea «The lion is big» y muestra la palabra clave con un dedo.",
    "Escribe dos respuestas con because sobre un texto corto del zoo, por ejemplo «The zebra has stripes because I heard...».",
)
