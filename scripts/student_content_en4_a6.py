"""Student material for 4.º básico Inglés (propuesta), EN04 OA 06 (leer textos literarios y funcionales breves).

Todos los textos son originales y están escritos en el enunciado. Cada palabra nueva se explica en la clase o lleva su pista en español.
"""
from __future__ import annotations

from student_content_en4_a import E, lesson, task
from student_lessons import arith

OA6 = "EN04 OA 06"

CARD = "«Dear Ana, Happy Easter! I hope you have many eggs. From Leo»"
INSTR = "«1. Take a paper. 2. Draw a circle. 3. Color it red.»"
INFO = "«The giraffe is a tall animal. It has a long neck. It eats leaves.»"
STORY = "«Tom has a red kite. The wind takes the kite. Tom runs. He finds the kite in a tree.»"
CHANT = "«Clap, clap, stamp, stamp! Jump, jump, stop!»"
RHYME = "«I see a bee. It sees me.»"
G1 = "«The zebra has black and white stripes. It eats grass. It lives with other zebras.»"
G2 = "«Dear Max, Happy Easter! I hope you have a nice day. From Eva»"
G3 = "«How to make a card: 1. Take a paper. 2. Fold it in half. 3. Draw an egg. 4. Write: Happy Easter!»"
G4 = "«Lia is sad. She cannot find her red ball. Ben looks under the table. Ben finds the ball. Lia is happy.»"
S1 = "«Sam is hungry. He sees a banana. Sam says: I want a banana, please. Lia says: Here! Sam eats the banana. He says: Thank you!»"
S2 = "«Eva wants a blue crayon. Tom has a blue crayon. Tom says: Here! Eva draws a blue egg.»"
I1 = "«How to draw a house: 1. Draw a square. 2. Draw a triangle on the square. 3. Draw a small rectangle in the square. 4. Color the triangle red.»"
I2 = "«How to make a basket card: 1. Take a paper. 2. Draw a basket. 3. Draw three eggs in the basket. 4. Color the eggs blue.»"
I3 = "«1. Open your book. 2. Look at page five. 3. Close your book.»"

# ---------------------------------------------------------------- clase 1
lesson(
    OA6, 1,
    "Los textos escritos en cada ejercicio; lápiz y papel.",
    "Aprenderé a reconocer qué tipo de texto estoy leyendo: cuento, rima, chant, tarjeta de saludo, instrucciones o texto informativo. Sirve para saber qué buscar al leer.",
    ["Sé que un texto puede ser un cuento, una rima o un chant.", "Conozco palabras como card, draw y animal."],
    [
        "Cada tipo de texto tiene pistas. Una tarjeta de saludo (greeting card) comienza con Dear (querida o querido) y termina con From (de parte de) y un nombre. Unas instrucciones (instructions) tienen pasos numerados y verbos como take, draw o color. Un texto informativo (information) da datos sobre algo.",
        "Un cuento (story) tiene personajes y cuenta lo que les pasa. Una rima (rhyme) tiene líneas cortas que terminan con sonidos parecidos, como bee y me. Un chant tiene palabras repetidas y acciones para decir con ritmo, como clap, stamp o jump.",
        "Para reconocer el tipo de texto, mira primero cómo empieza, cómo termina y cómo está escrito. Luego pregúntate: ¿tiene números de paso?, ¿tiene personajes?, ¿da datos?, ¿saluda a alguien? Una sola pista no basta: conviene encontrar dos.",
    ],
    [("greeting card", "tarjeta de saludo"), ("Dear... / From...", "querido o querida... / de parte de..."), ("instructions", "instrucciones: pasos para hacer algo"), ("information", "información: datos"), ("story", "cuento"), ("rhyme", "rima"), ("chant", "texto con ritmo y acciones")],
    [
        ("Reconocer una tarjeta", "Lee: " + CARD + " (hope = espero, many = muchos). ¿Qué tipo de texto es?", ["Comienza con Dear Ana.", "Termina con From Leo.", "Es una tarjeta de saludo."], "Una tarjeta de saludo"),
        ("Reconocer instrucciones", "Lee: " + INSTR + " (take = toma, paper = papel, color = pinta). ¿Qué tipo de texto es?", ["Tiene pasos con números.", "Cada paso empieza con un verbo: take, draw, color.", "Son instrucciones."], "Instrucciones"),
    ],
    [
        ("Pensar que un texto con un animal es siempre un cuento.", "Un texto informativo también puede hablar de un animal.", "Busca personajes y sucesos para un cuento; busca datos para un texto informativo."),
        ("Decidir el tipo de texto con una sola pista.", "Una pista puede engañar.", "Busca dos pistas, como cómo empieza y cómo termina."),
    ],
    [
        ("Lee: " + CARD + " ¿Qué tipo de texto es?", "Una tarjeta de saludo", "Tiene Dear al comienzo y From al final."),
        ("Lee: " + INFO + " (tall = alto, neck = cuello, leaves = hojas). ¿Qué tipo de texto es?", "Un texto informativo", "Da datos sobre la jirafa."),
        ("Lee: " + CHANT + " ¿Qué tipo de texto es?", "Un chant", "Tiene palabras repetidas y acciones."),
    ],
    [
        ("¿Qué palabra al comienzo es pista de una tarjeta: Dear o Draw?", "Dear", "Dear se usa al saludar a alguien."),
        ("¿Qué muestra que unas instrucciones son instrucciones: pasos numerados con verbos o un saludo?", "Pasos numerados con verbos", "Las instrucciones dicen qué hacer en orden."),
        ("Lee: " + STORY + " (wind = viento, kite = volantín, finds = encuentra). ¿Qué tipo de texto es?", "Un cuento", "Tiene un personaje y sucesos."),
    ],
    [
        ("Lee: " + RHYME + " ¿Qué tipo de texto es?", "Una rima", "Bee y me tienen el mismo sonido final."),
        ("Lee: " + INSTR + " ¿Cuántos pasos tiene?", "3", "Los números 1, 2 y 3 indican tres pasos."),
        ("Lee: " + CARD + " ¿Quién escribe la tarjeta?", "Leo", "From Leo indica quién la envía."),
    ],
    [
        ("Lee: " + INFO + " Pedro dice que es un cuento porque tiene un animal. ¿Tiene razón?", "No; es informativo porque da datos y no cuenta sucesos", "No tiene personajes que hagan cosas en orden."),
        ("Lee: " + CARD + " ¿Para quién es la tarjeta?", "Para Ana", "Dear Ana nombra a quien la recibe."),
    ],
    [
        ("Lee los textos: A «Take a paper. Draw a star.» B «Dear Eva, Happy Easter! From Tom» C «The zebra has stripes.» D «Bee and tree, you and me.» ¿Qué tipo es cada uno, en orden A, B, C y D?", "Instrucciones, tarjeta, informativo, rima", "Cada texto tiene sus pistas propias."),
        ("Lee: A «Take a paper. Draw a star.» B «Dear Eva, Happy Easter! From Tom» C «The zebra has stripes.» D «Bee and tree, you and me.» ¿Cuál tiene un mensaje para una persona en particular?", "B", "Dear Eva nombra a la persona que recibe."),
    ],
    [("En la sala ves el cartel «1. Open your book. 2. Look at page five.» (page = página). ¿Qué tipo de texto es?", "Instrucciones", "Tiene pasos numerados con verbos.")],
    [
        ("¿Qué significa «Dear»?", "Querido o querida", "Se usa para saludar al comienzo de una tarjeta."),
        ("¿Qué significa «instructions»?", "Instrucciones", "Son pasos para hacer algo."),
        ("¿Cuántas pistas conviene buscar para reconocer un tipo de texto?", "Dos o más", "Una pista sola puede engañar."),
    ],
    task("Lee estos tres textos: A «Dear Mia, Happy Easter! From Sam» B «1. Take a pencil. 2. Draw a square.» C «The lion is big. It eats meat.» (meat = carne). Escribe qué tipo es cada uno y una pista de cómo lo reconociste.", "A: tarjeta (Dear, From); B: instrucciones (números y verbos); C: informativo (da datos).", ["nombra bien los tres tipos", "da una pista distinta para cada uno", "usa palabras como Dear, números o datos"], ["hoja con los tres tipos", "nota del adulto"], ["decir que C es un cuento", "no dar ninguna pista"], "Reconoce el tipo acertado y vuelve a leer con él la pista que lo muestra."),
    "Lee en voz alta «Dear» y «From» y busca cuál texto de la clase los tiene.",
    "Escribe una tarjeta corta que comience con Dear y termine con From.",
)

# ---------------------------------------------------------------- clase 2
lesson(
    OA6, 2,
    "Los textos escritos en cada ejercicio; lápiz y papel.",
    "Aprenderé a identificar la idea general de un texto escrito: de qué trata en total. Sirve para resumir lo que leo con una frase.",
    ["Sé reconocer el tipo de texto.", "Sé que un detalle es un dato pequeño."],
    [
        "La idea general (main idea) de un texto escrito responde a «¿de qué trata?». En un texto informativo es el tema que se explica. En una tarjeta es el mensaje que quiere dar. En unas instrucciones es lo que se logra al terminar los pasos. En un cuento es lo que les pasa a los personajes.",
        "Los detalles apoyan la idea general. En «The zebra has black and white stripes. It eats grass. It lives with other zebras», los tres datos hablan de la cebra. Por eso la idea es que el texto describe a la cebra. «It eats grass» es solo un detalle.",
        "Para encontrar la idea general, lee todo el texto, subraya las palabras que se repiten y elige una frase que sirva para todas las oraciones. Si una opción solo sirve para una oración, es un detalle. Un buen título también puede resumir el texto.",
    ],
    [("main idea", "idea general"), ("detail", "detalle"), ("zebra", "cebra"), ("stripes", "rayas"), ("fold", "doblar"), ("half", "mitad"), ("cannot find", "no puede encontrar")],
    [
        ("Idea general de un texto informativo", "Lee: " + G1 + " (stripes = rayas, grass = pasto, lives = vive). ¿Cuál es la idea general? a) El texto describe a la cebra b) El texto habla de cómo se hace un pastel.", ["Todas las frases hablan de la cebra.", "La a sirve para todo el texto.", "La b no tiene relación."], "a"),
        ("Idea general de unas instrucciones", "Lee: " + G3 + " (fold = doblar, half = mitad). ¿Para qué sirven los pasos?", ["Los pasos hablan de papel, un huevo y Happy Easter.", "Al terminar queda una tarjeta.", "Sirven para hacer una tarjeta."], "Para hacer una tarjeta"),
    ],
    [
        ("Elegir un detalle como idea general, como «eats grass».", "Un detalle solo sirve para una oración.", "Elige la idea que sirva para todas las oraciones."),
        ("Elegir la idea porque contiene una palabra conocida.", "La palabra puede aparecer sin ser el tema.", "Comprueba que la idea resuma todo el texto."),
    ],
    [
        ("Lee: " + G1 + " ¿De qué animal trata el texto?", "De la cebra", "Todas las oraciones hablan de la cebra."),
        ("Lee: " + G2 + " (hope = espero, nice = lindo). ¿Para qué se escribió la tarjeta?", "Para saludar en Easter", "Dice Happy Easter."),
        ("Lee: " + G3 + " ¿Para qué sirve el texto?", "Para hacer una tarjeta", "Son pasos para hacer una tarjeta."),
    ],
    [
        ("Lee: " + G4 + " (cannot find = no puede encontrar, looks = mira). ¿Cuál es la idea general? a) Ben ayuda a Lia a encontrar su pelota b) Lia compra pan.", "a", "El texto cuenta cómo Ben encuentra la pelota."),
        ("Lee: " + G4 + " ¿«Ben looks under the table» es una idea general o un detalle?", "Un detalle", "Es una parte pequeña del cuento."),
        ("Lee: " + G4 + " Elige un buen título: The Red Ball o The Zoo.", "The Red Ball", "El cuento trata de una pelota roja."),
    ],
    [
        ("Lee: " + G3 + " ¿Cuántos pasos tiene?", "4", "Los números 1, 2, 3 y 4 indican cuatro pasos."),
        ("Lee: " + G2 + " ¿Quién escribe la tarjeta?", "Eva", "From Eva indica quién la envía."),
        ("Lee: " + G4 + " ¿Dónde mira Ben?", "Debajo de la mesa", "Under the table significa debajo de la mesa."),
    ],
    [
        ("Lee: " + G1 + " Luis dice que la idea general es «grass» porque aparece esa palabra. ¿Tiene razón?", "No; grass es un detalle y el texto describe a la cebra", "La idea general debe servir para todo el texto."),
        ("Lee: " + G4 + " Ana dice que el texto trata solo de «Lia is sad». ¿Tiene razón?", "No; solo es el comienzo y falta que encuentran la pelota", "La idea general incluye lo que pasa en todo el cuento."),
    ],
    [
        ("Lee: " + G1 + " ¿Cuál frase resume mejor el texto? a) Zebras are animals with stripes that eat grass b) Zebras are green.", "a", "La a coincide con lo que dice el texto."),
        ("Lee: A " + G1 + " B " + G2 + " C " + G3 + " D " + G4 + " ¿Cuál habla de personajes que sienten algo?", "D, el cuento de Lia y Ben", "Lia está triste y luego feliz."),
    ],
    [("En el cuaderno de inglés de tu compañero ves el texto «The lion is big. The lion is strong. The lion sleeps.» (strong = fuerte). ¿De qué trata?", "Del león", "Todas las oraciones hablan del león.")],
    [
        ("¿Qué es la idea general?", "De qué trata todo el texto", "Resume el texto."),
        ("¿Qué es un detalle?", "Un dato pequeño que apoya la idea", "Explica una parte."),
        ("¿Cómo se dice «cebra» en inglés?", "zebra", "Zebra es cebra."),
    ],
    task("Lee: «Dear Pam, Happy Easter! I made a card for you. It has a blue egg and a yellow basket. From Ben» (made = hice). Escribe la idea general en una frase corta, como «Ben sends an Easter card to Pam». Luego escribe dos detalles del texto.", "Idea: Ben envía una tarjeta de Easter a Pam. Detalles: tiene un huevo azul; tiene una canasta amarilla.", ["escribe una idea que sirva para todo el texto", "escribe dos detalles correctos", "no repite un detalle como idea"], ["hoja con idea y detalles", "nota del adulto"], ["poner un detalle como idea general", "inventar un dato que el texto no dice"], "Reconoce la idea y vuelve a leer con él cada detalle para comprobar."),
    "Lee en voz alta «The zebra has stripes» y di de qué animal habla.",
    "Escribe un texto de tres oraciones sobre un animal salvaje y subraya la oración que resume el texto.",
)

# ---------------------------------------------------------------- clase 3
lesson(
    OA6, 3,
    "Los textos escritos en cada ejercicio; lápiz y papel.",
    "Aprenderé a encontrar quiénes son los personajes de un cuento y qué hace cada uno, incluyendo las expresiones I want... y Here!. Sirve para entender quién hace qué en una historia escrita.",
    ["Sé que una historia tiene personajes y acciones.", "Conozco I want... y Here! en un diálogo."],
    [
        "Los personajes (characters) son las personas o los animales de una historia. Las acciones (actions) son lo que hacen: eats (come), draws (dibuja), says (dice), gives (da) o runs (corre). Para encontrarlos, busca los nombres y los verbos que van con ellos.",
        "Dos expresiones muy frecuentes son «I want...», que significa «yo quiero...», y «Here!», que significa «¡toma!» o «¡aquí está!». Quien dice I want pide algo. Quien dice Here! lo entrega. También verás wants, que es la forma para él o ella: «Eva wants a crayon» significa «Eva quiere un lápiz de cera».",
        "Para saber quién hace cada acción, mira quién va antes del verbo. En «Tom says: Here!», el personaje es Tom y la acción es decir Here!. Después comprueba si el personaje que pide es distinto del que entrega. Eso evita mezclar a los personajes.",
    ],
    [("character", "personaje"), ("action", "acción"), ("I want...", "yo quiero..."), ("Here!", "¡toma! / ¡aquí está!"), ("wants", "quiere (él o ella)"), ("says", "dice"), ("gives", "da")],
    [
        ("Quién pide", "Lee: " + S1 + " (hungry = con hambre, banana = plátano). ¿Quién dice «I want a banana, please»?", ["Busco I want.", "Antes está Sam says.", "Sam pide el plátano."], "Sam"),
        ("Quién entrega", "En el mismo texto, ¿quién dice «Here!»?", ["Busco Here!", "Antes está Lia says.", "Lia entrega el plátano."], "Lia"),
    ],
    [
        ("Mezclar quién pide y quién entrega.", "Los dos personajes hacen acciones distintas.", "I want pide algo y Here! lo entrega."),
        ("Confundir wants con want.", "Wants se usa con él o ella.", "Con un nombre propio se usa wants, como en «Eva wants a crayon»."),
    ],
    [
        ("Lee: " + S1 + " ¿Quién tiene hambre?", "Sam", "El texto dice Sam is hungry."),
        ("Lee: " + S1 + " ¿Qué dice Lia?", "Here!", "Lia entrega el plátano con Here!"),
        ("¿Qué significa «I want a banana, please»?", "Quiero un plátano, por favor", "I want es yo quiero."),
    ],
    [
        ("¿Qué significa «Here!» cuando alguien da algo?", "¡Toma! o ¡aquí está!", "Se dice al entregar un objeto."),
        ("Lee: " + S1 + " ¿Quién come el plátano?", "Sam", "Sam eats the banana."),
        ("Lee: " + S1 + " ¿Cuántos personajes hay?", "2", "Hay dos nombres: Sam y Lia."),
    ],
    [
        ("Lee: " + S2 + " (wants = quiere, crayon = lápiz de cera). ¿Qué quiere Eva?", "Un lápiz de cera azul", "Eva wants a blue crayon."),
        ("Lee: " + S2 + " ¿Quién dice «Here!»?", "Tom", "Tom entrega el lápiz de cera."),
        ("Lee: " + S2 + " ¿Qué dibuja Eva?", "Un huevo azul", "Eva draws a blue egg."),
    ],
    [
        ("Pedro dice que Lia quiere el plátano porque dice «Here!». ¿Tiene razón?", "No; Sam es quien lo quiere y Lia lo entrega", "I want lo dice Sam."),
        ("Lee: " + S1 + " Ordena las acciones: A) Sam come el plátano. B) Lia dice Here! C) Sam dice I want a banana.", "C, B, A", "Pide, recibe y come."),
    ],
    [
        ("Lee: «Max and Pam are at the park. Max has a ball. Pam wants the ball. Max says: Here! They play together. Both are happy.» (together = juntos). ¿Qué palabra muestra que Pam desea algo: wants o plays?", "wants", "Wants indica que Pam quiere algo."),
        ("Lee: «Max and Pam are at the park. Max has a ball. Pam wants the ball. Max says: Here! They play together. Both are happy.» ¿Quiénes están felices?", "Max y Pam", "Both are happy significa los dos están felices."),
    ],
    [("Lees una nota en la clase: «Mia: I want a pencil, please. Leo: Here!» (pencil = lápiz). ¿Quién da el lápiz?", "Leo", "Leo dice Here! al entregarlo.")],
    [
        ("¿Qué significa «wants»?", "Quiere", "Wants se usa con él o ella."),
        ("¿Qué es un personaje?", "Una persona o un animal de la historia", "Son quienes hacen las acciones."),
        ("¿Cómo se dice «dice» en inglés?", "says", "Says es dice."),
    ],
    task("Lee: «Ben is thirsty. He sees a glass of water. Ben says: I want water, please. Ana says: Here! Ben drinks the water.» (thirsty = con sed, glass = vaso). Escribe los dos personajes, qué hace cada uno y la expresión I want... que aparece. Luego escribe la expresión que significa ¡toma!", "Personajes: Ben (quiere agua y la bebe) y Ana (la entrega). I want water, please. Here!", ["nombra Ben y Ana", "dice qué hace cada uno", "escribe I want water y Here!"], ["hoja con personajes y acciones", "nota del adulto"], ["decir que Ana quiere agua", "no escribir Here!"], "Reconoce los personajes y vuelve a leer con él quién dice cada frase."),
    "Lee en voz alta «I want a pencil, please» y «Here!» con dos voces.",
    "Escribe un texto de cuatro líneas con I want... y Here! entre dos personajes.",
)

# ---------------------------------------------------------------- clase 4
lesson(
    OA6, 4,
    "Las instrucciones escritas en cada ejercicio; lápiz, papel y lápices de colores.",
    "Aprenderé a seguir instrucciones escritas paso a paso y a comprobar el resultado. Sirve para hacer un dibujo o una tarea siguiendo un texto en inglés.",
    ["Sé reconocer unas instrucciones.", "Conozco verbos como draw, color, take y open."],
    [
        "Las instrucciones escritas tienen pasos numerados (1, 2, 3). Cada paso empieza con un verbo de acción: take (toma), draw (dibuja), color (pinta), write (escribe), open (abre) y close (cierra). El orden de los pasos importa: si cambias el orden, el resultado cambia.",
        "Algunas palabras indican dónde hacer algo: on (sobre), in (dentro de) y under (debajo de). También indican con qué color: red (rojo), blue (azul) y yellow (amarillo). En «Draw a triangle on the square», el triángulo va sobre el cuadrado, como el techo de una casa.",
        "Para seguir unas instrucciones, lee un paso, hazlo y luego lee el siguiente. Al final, compara tu resultado con todos los pasos y revisa números, colores y lugares. Si algo no coincide, vuelve a leer el paso donde te equivocaste.",
    ],
    [("step", "paso"), ("draw / color", "dibujar / pintar"), ("on / in / under", "sobre / dentro de / debajo de"), ("square / triangle / rectangle", "cuadrado / triángulo / rectángulo"), ("house", "casa"), ("basket", "canasta"), ("page", "página")],
    [
        ("Seguir un paso", "Lee: " + I1 + " (house = casa, small = pequeño). ¿Qué figura dibujas primero?", ["Busco el paso 1.", "Dice Draw a square.", "Dibujo un cuadrado."], "Un cuadrado"),
        ("Revisar el resultado", "En las mismas instrucciones, ¿de qué color pintas el triángulo?", ["Busco Color.", "Dice Color the triangle red.", "El triángulo es rojo."], "Rojo"),
    ],
    [
        ("Hacer los pasos en otro orden.", "El resultado puede quedar mal.", "Sigue los pasos en el orden de los números."),
        ("Pintar la figura equivocada, como el cuadrado en lugar del triángulo.", "No se leyó qué figura pintar.", "Lee el paso completo antes de pintar."),
    ],
    [
        ("Lee: " + I1 + " ¿Dónde dibujas el triángulo?", "Sobre el cuadrado", "On the square significa sobre el cuadrado."),
        ("Lee: " + I1 + " ¿Dónde dibujas el rectángulo?", "Dentro del cuadrado", "In the square significa dentro del cuadrado."),
        ("¿Qué significa «Color it red»?", "Píntalo de rojo", "Color es pintar y red es rojo."),
    ],
    [
        ("¿Por qué importa el orden de los pasos?", "Porque cambia el resultado", "Cada paso depende del anterior."),
        ("Lee: " + I1 + " ¿Cuántos pasos tiene?", "4", "Los números van del 1 al 4."),
        ("Lee: " + I3 + " (page = página). ¿Qué haces en el paso 2?", "Miro la página cinco", "Look at page five es el paso 2."),
    ],
    [
        ("Lee: " + I2 + " (basket = canasta, eggs = huevos). ¿Cuántos huevos dibujas?", "3", "Three eggs son tres huevos."),
        ("Lee: " + I2 + " ¿De qué color pintas los huevos?", "Azul", "Color the eggs blue."),
        ("Lee: " + I3 + " ¿Qué haces al final?", "Cierro mi libro", "Close your book es el paso 3."),
    ],
    [
        ("Lee: " + I1 + " Luis pintó el cuadrado de rojo. ¿Qué paso no siguió bien?", "El paso 4, que dice pintar el triángulo", "El paso 4 pide pintar el triángulo."),
        ("Lee: " + I1 + " Si haces el paso 2 antes del paso 1, ¿qué problema tienes?", "No hay un cuadrado donde poner el triángulo", "El triángulo va sobre el cuadrado."),
    ],
    [
        arith("Las instrucciones de la casa tienen 4 pasos, las de la canasta 4 pasos y las del libro 3 pasos. ¿Cuántos pasos hay en total?", "4+4+3", "Se suman los pasos de los tres textos."),
        ("Lee: " + I1 + " Al terminar, ¿cuántas figuras distintas tiene tu dibujo?", "3", "Son tres figuras distintas."),
    ],
    [("En la clase hay un cartel: " + I3 + " ¿Qué haces primero?", "Abro mi libro", "Open your book es el paso 1.")],
    [
        ("¿Qué significa «step»?", "Paso", "Cada número de las instrucciones es un paso."),
        ("¿Qué significa «on the square»?", "Sobre el cuadrado", "On es sobre."),
        ("¿Cómo se dice «rectángulo» en inglés?", "rectangle", "Rectangle es rectángulo."),
    ],
    task("Lee: «How to draw a flag: 1. Draw a rectangle. 2. Draw a circle in the rectangle. 3. Color the circle yellow. 4. Color the rectangle blue.» (flag = bandera). Haz el dibujo siguiendo los pasos. Después escribe cuántos pasos tiene el texto y de qué color es el círculo.", "Una bandera con rectángulo azul y círculo amarillo; 4 pasos; el círculo es amarillo.", ["sigue los pasos en orden", "el círculo está dentro del rectángulo", "escribe 4 pasos y amarillo"], ["dibujo del estudiante", "nota del adulto"], ["pintar el círculo de azul", "dibujar el círculo fuera del rectángulo"], "Reconoce lo que siguió bien y vuelve a leer con él el paso que cambió el resultado."),
    "Lee en voz alta «Draw a square. Color it red.» y haz el dibujo.",
    "Escribe unas instrucciones de tres pasos para dibujar una casa con figuras, y pide a alguien que las siga.",
)

# ---------------------------------------------------------------- clase 5
lesson(
    OA6, 5,
    "Cuatro textos nuevos escritos en los ejercicios; lápiz y papel.",
    "Aprenderé a leer un texto nuevo y a usar lo que ya sé: reconozco el tipo de texto, la idea general, los personajes y las palabras clave. Sirve para entender textos que no he visto antes.",
    ["Sé reconocer el tipo de texto, la idea general, los personajes y las instrucciones.", "Sé usar I want... y Here!."],
    [
        "Cuando lees un texto nuevo, usa cuatro pasos. Primero, reconoce el tipo de texto con sus pistas. Segundo, lee todo y piensa en la idea general. Tercero, busca personajes, acciones o pasos. Cuarto, subraya las palabras que no conoces y usa las que sí conoces para entender.",
        "Hoy verás una tarjeta, un cuento, unas instrucciones y un texto informativo nuevos. Aparecen palabras como hat (sombrero), box (caja), bakery (panadería), baker (panadero), face (cara) y eyes (ojos). Si no conoces una palabra, lee la frase completa y busca pistas.",
        "Al terminar, comprueba tu comprensión con una pregunta: ¿puedo decir de qué trata el texto con una frase y mostrar dos palabras que lo prueban? Si es así, entendiste lo importante, aunque no conozcas cada palabra.",
    ],
    [("hat", "sombrero"), ("box", "caja"), ("bakery", "panadería"), ("baker", "panadero"), ("face", "cara"), ("eyes", "ojos"), ("transfer", "usar lo aprendido en algo nuevo")],
    [
        ("Texto nuevo: tarjeta", "Lee: «Dear Ben, Happy Easter! Here is a card for you. From Pam.» ¿Quién recibe la tarjeta?", ["Busco Dear.", "Dice Dear Ben.", "Ben recibe la tarjeta."], "Ben"),
        ("Texto nuevo: instrucciones", "Lee: «1. Take a pencil. 2. Draw a circle. 3. Draw two eyes.» (eyes = ojos). ¿Qué dibujas al final?", ["Tiene tres pasos.", "El paso 3 dice Draw two eyes.", "Dibujo dos ojos."], "Dos ojos"),
    ],
    [
        ("Saltar la lectura del tipo de texto y responder al azar.", "No se usan las pistas.", "Reconoce primero el tipo de texto."),
        ("Detenerse por una palabra desconocida.", "Se pierde el hilo.", "Lee la frase completa y busca pistas."),
    ],
    [
        ("Lee: «A boy wants a hat. The hat is in a box. He opens the box. Here is the hat!» (hat = sombrero). ¿Qué tipo de texto es?", "Un cuento", "Tiene un personaje y sucesos."),
        ("Lee: «A boy wants a hat. The hat is in a box. He opens the box. Here is the hat!» ¿Qué quiere el niño?", "Un sombrero", "A boy wants a hat."),
        ("Lee: «A boy wants a hat. The hat is in a box. He opens the box. Here is the hat!» ¿Dónde está el sombrero?", "En una caja", "The hat is in a box."),
    ],
    [
        ("Lee: «A bakery is a place in a town. A baker makes bread. People buy bread there.» ¿Qué tipo de texto es?", "Un texto informativo", "Da datos sobre una panadería."),
        ("Lee: «A bakery is a place in a town. A baker makes bread. People buy bread there.» ¿Quién hace el pan?", "El panadero", "A baker makes bread."),
        ("¿Qué haces primero ante un texto nuevo?", "Reconozco el tipo de texto", "Así sé qué pistas buscar."),
    ],
    [
        ("Lee: «1. Take a pencil. 2. Draw a circle. 3. Draw two eyes.» ¿Qué dibujas con esos tres pasos?", "Una cara", "Un círculo con dos ojos forma una cara."),
        ("Lee: «Dear Ben, Happy Easter! Here is a card for you. From Pam.» ¿Quién escribe la tarjeta?", "Pam", "From Pam indica quién la escribe."),
        ("Lee: «A boy wants a hat. The hat is in a box. He opens the box. Here is the hat!» ¿Qué abre el niño?", "La caja", "He opens the box."),
    ],
    [
        ("Lee: «A bakery is a place in a town. A baker makes bread. People buy bread there.» Ana no conoce la palabra «baker». ¿Qué puede hacer?", "Leer la frase completa y usar las palabras que conoce", "Bread y bakery dan pistas."),
        ("Lee: «A boy wants a hat. The hat is in a box. He opens the box. Here is the hat!» Dos niños lo leen. Uno dice que es un cuento y otro que es una tarjeta. ¿Quién tiene razón?", "El que dice que es un cuento", "No empieza con Dear ni termina con From y tiene sucesos."),
    ],
    [
        arith("Lee: «Max has three eggs. He says: Here is an egg for you.» Max le da un huevo a Ana. ¿Cuántos huevos le quedan a Max?", "3-1", "Se resta el huevo que entrega a los tres que tenía."),
        ("Lee: «A boy wants a hat. The hat is in a box. He opens the box. Here is the hat!» Elige la frase que prueba que el cuento termina bien: a) Here is the hat! b) A boy wants a hat.", "a", "Here is the hat! muestra que el niño encuentra el sombrero."),
    ],
    [("En el recreo ves un cartel: «Dear friends, Happy Easter! From the school.» ¿Qué tipo de texto es?", "Una tarjeta de saludo", "Comienza con Dear y termina con From.")],
    [
        ("¿Cuál es el primer paso para leer un texto nuevo?", "Reconocer el tipo de texto", "Las pistas dicen qué buscar."),
        ("¿Qué significa «box»?", "Caja", "Box es caja."),
        ("¿Se necesita conocer todas las palabras para entender lo importante?", "No, basta con las palabras conocidas y las pistas", "El contexto ayuda."),
    ],
    task("Lee este texto nuevo: «Dear Ana, Happy Easter! I have a basket with three eggs. Here is an egg for you. From Max.» Escribe qué tipo de texto es, quién lo escribe, quién lo recibe y cuántos huevos dice el texto que hay en la canasta.", "Es una tarjeta; lo escribe Max, lo recibe Ana; hay tres huevos.", ["reconoce la tarjeta", "nombra a Max y a Ana", "escribe tres huevos"], ["hoja con las cuatro respuestas", "nota del adulto"], ["decir que Ana escribe", "no contar bien los huevos"], "Reconoce lo que acertó y vuelve a leer con él Dear y From."),
    "Lee en voz alta «Dear Ana, From Max» y di quién escribe y quién recibe.",
    "Escribe un texto corto nuevo de cualquier tipo y pide a alguien que descubra qué tipo es.",
)
