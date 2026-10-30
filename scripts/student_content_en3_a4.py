"""Student material for 3.º básico Inglés (propuesta), EN03 OA 04 (estrategias de comprensión oral).

Las «escuchas» las lee un adulto; las imágenes se describen entre corchetes porque el cuaderno no las incluye.
"""
from __future__ import annotations

from student_content_en3_a import ADULT, E, lesson, task
from student_lessons import arith

OA4 = "EN03 OA 04"

lesson(
    OA4, 1,
    "Los títulos, las imágenes descritas y los textos escritos en cada ejercicio, que lee un adulto; lápiz y hoja para tapar el guion.",
    "Aprenderé a predecir de qué trata un texto que voy a escuchar usando pistas como el título, la imagen y las palabras que conozco. Sirve para empezar a escuchar con una idea y entender mejor.",
    ["Sé que un título es el nombre de un texto.", "Conozco palabras como cat, dog, sun y rain."],
    [
        "Predecir (predict) es decir qué creo que va a pasar o de qué trata un texto, antes de escucharlo o mientras lo escucho. Para predecir uso pistas (clues): el título (title), una imagen (image) y las palabras que ya conozco. Puedo decirlo así: «I think the story is about a dog», que significa «creo que el cuento trata de un perro».",
        "Ejemplo: el título es «The Rainy Day» (rainy = lluvioso) y la imagen muestra nubes grises y gotas. Las dos pistas hablan de lluvia, así que predigo que el cuento trata de un día con lluvia. Otra pista es umbrella (paraguas): se usa cuando llueve.",
        "Una predicción no es un hecho: es una idea con pistas. Elige la predicción que use más pistas y que tenga sentido. No es adivinar al azar. Después de escuchar, comprueba si tu idea era correcta.",
    ],
    [("predict", "predecir"), ("clue", "pista"), ("title", "título"), ("I think", "yo creo"), ("rainy", "lluvioso"), ("umbrella", "paraguas")],
    [
        ("Predecir con título e imagen", "Título: «The Rainy Day». Imagen: [nubes grises y gotas de lluvia]. ¿De qué crees que trata: de un día de lluvia o de un día de playa?", ["Leo el título: rainy, lluvioso.", "La imagen muestra nubes y gotas.", "Las dos pistas hablan de lluvia."], "De un día de lluvia"),
        ("Decir la predicción en inglés", "Título: «At the Zoo». Imagen: [un león y un elefante]. Completa: «I think the story is about a lion and an ___.»", ["Miro la imagen: hay un león y un elefante.", "Elephant es elefante.", "Completo con elephant."], "elephant"),
    ],
    [
        ("Predecir sin usar ninguna pista, solo por gusto.", "Se adivina al azar.", "Usa el título, la imagen y las palabras que conoces."),
        ("Pensar que la predicción siempre es verdad.", "Se confunde una idea con un hecho.", "Después de escuchar, comprueba si tu predicción coincide."),
    ],
    [
        ("Título: «The Rainy Day». Imagen: [nubes grises y gotas]. ¿Qué predices: un día de lluvia o un día de calor?", "Un día de lluvia", "Rainy y las gotas hablan de lluvia."),
        ("¿Qué significa «I think»?", "Yo creo", "Se usa para decir una predicción."),
        (ADULT + "«Sam takes an umbrella. The sky is gray.» (takes = toma). ¿Qué predices: llueve o hay mucho sol?", "Llueve", "El paraguas y el cielo gris son pistas de lluvia."),
    ],
    [
        ("¿Qué es predecir?", "Decir qué creo que pasará usando pistas", "La predicción se apoya en pistas."),
        ("¿Cuáles son tres pistas para predecir?", "El título, la imagen y las palabras que conozco", "Son lo primero que puedes usar."),
        ("¿Una predicción siempre es verdad?", "No; hay que comprobar con el texto", "Es una idea, no un hecho."),
    ],
    [
        ("Título: «At the Zoo». Imagen: [un león y un elefante]. ¿Qué predicción usa bien las pistas: a) The story is about a lion and an elephant. b) The story is about a pizza.", "a", "Lion y elephant coinciden con la imagen."),
        ("Título: «My Birthday» (birthday = cumpleaños). Imagen: [un pastel con velas]. ¿Qué predices: a) una fiesta b) un viaje en avión?", "a", "Birthday y el pastel son pistas de una fiesta."),
        ("Completa con una palabra: «I ___ the story is about a dog.»", "think", "I think significa yo creo."),
    ],
    [
        ("Ana ve el título «The Sad Boy» (sad = triste) y predice que el niño se ríe. ¿Qué pista contradice su predicción?", "La palabra sad", "Sad significa triste, no feliz."),
        ("Pedro predice sin mirar el título ni la imagen. ¿Qué debería hacer?", "Mirar el título y la imagen para tener pistas", "Una predicción necesita pistas."),
    ],
    [
        ("Título: «The Cold Day» (cold = frío). Imagen: [un niño con gorro y bufanda]. ¿Qué predicción usa más pistas: a) Today is hot. b) Today is cold.", "b", "Cold, el gorro y la bufanda hablan de frío."),
        ("Título: «The Hungry Cat» (hungry = con hambre, wants = quiere). ¿Qué predicción tiene más sentido: a) The cat wants food. b) The cat is swimming.", "a", "Hungry se relaciona con querer comida."),
    ],
    [("Antes de escuchar un cuento llamado «The Big Elephant», un niño mira el título. ¿De qué animal predice que trata?", "De un elefante grande", "Big es grande y elephant es elefante.")],
    [
        ("¿Qué significa «clue»?", "Pista", "Una clue ayuda a predecir."),
        ("Título: «The Rainy Day». ¿Qué cosa puede aparecer en el cuento: una umbrella o una piscina caliente?", "Una umbrella", "El paraguas se relaciona con la lluvia."),
        ("¿Qué haces después de predecir?", "Escucho y compruebo si coincide", "Una predicción se comprueba."),
    ],
    task("Lee el título «The Hungry Cat» y mira esta imagen descrita: [un gato junto a un plato vacío]. Escribe en una hoja tu predicción completando la frase: «I think the cat wants ___.» Elige entre food (comida) o a bike (bicicleta); wants significa quiere.", "I think the cat wants food.", ["completa con food", "usa el título como pista", "usa la imagen como pista"], ["frase escrita", "nota del adulto"], ["elegir a bike", "no usar el título ni la imagen"], "Reconoce las pistas que usó y vuelve con él sobre la palabra hungry."),
    "Pide a un adulto que diga el título «The Rainy Day» y dibuja lo que crees que verás en el cuento.",
    "Inventa un título para un cuento y escribe tu predicción con «I think...».",
)

lesson(
    OA4, 2,
    "Los textos escritos en cada ejercicio, que lee un adulto; lápiz y hoja para tapar el guion.",
    "Aprenderé a usar lo que ya sé sobre un tema para entender mejor lo que escucho. Sirve para comprender palabras nuevas relacionándolas con cosas conocidas.",
    ["Sé predecir con título e imagen.", "Conozco palabras como Easter, zoo y apple."],
    [
        "Tu conocimiento previo (prior knowledge) es lo que ya sabes sobre un tema. Si escuchas «Tom is hungry. He opens the fridge» (fridge = refrigerador), puedes pensar: «I know that food is in the fridge», que significa «yo sé que la comida está en el refrigerador». Eso te ayuda a entender qué busca Tom.",
        "Conectar es unir lo que escuchas con lo que sabes. Por ejemplo, si el texto habla de Easter (Pascua), puedes recordar que es una celebración y que en muchas casas se regalan huevos de chocolate. Si escuchas big cat (felino grande), puedes pensar en un león, que ya conoces.",
        "Cuidado: lo que sabes ayuda, pero el texto manda. Si piensas que Max es un gato y el texto dice «Max is a dog», debes cambiar tu idea. Pregúntate siempre: ¿qué sé yo? y ¿qué dice el texto?",
    ],
    [("prior knowledge", "conocimiento previo, lo que ya sé"), ("I know", "yo sé"), ("connect", "conectar, unir"), ("fridge", "refrigerador"), ("celebration", "celebración"), ("big cat", "felino grande")],
    [
        ("Conectar con lo que sé", ADULT + "«Tom is hungry. He opens the fridge.» (hungry = con hambre, opens = abre). ¿Qué crees que busca Tom?", ["Sé que la comida está en el refrigerador.", "Tom tiene hambre.", "Conecto las dos ideas."], "Comida"),
        ("El texto manda", "Pablo cree que Max es un gato porque él tiene un gato. El texto dice «Max is a dog». ¿Qué debe hacer?", ["Mi idea previa es útil.", "El texto dice dog.", "Cambio mi idea."], "Seguir el texto: Max es un perro"),
    ],
    [
        ("Usar lo que sé aunque el texto diga otra cosa.", "Se olvida que el texto es la prueba.", "Compara lo que sabes con lo que dice el texto y cambia tu idea si es necesario."),
        ("Pensar que no sé nada sobre el tema.", "No se busca en lo que ya conozco.", "Pregunta: ¿qué conozco sobre este tema?"),
    ],
    [
        ("¿Qué es el conocimiento previo?", "Lo que ya sé sobre un tema", "Prior knowledge es lo que sabes antes de escuchar."),
        (ADULT + "«Tom is hungry. He opens the fridge.» ¿Qué crees que busca Tom?", "Comida", "El refrigerador guarda comida."),
        ("¿Qué significa «I know»?", "Yo sé", "Se usa para decir lo que ya conozco."),
    ],
    [
        ("¿Para qué sirve conectar con lo que ya sé?", "Para entender mejor ideas o palabras nuevas", "Lo conocido da pistas para lo nuevo."),
        ("Si el texto dice algo distinto de lo que pensabas, ¿qué haces?", "Cambio mi idea y sigo lo que dice el texto", "El texto es la evidencia."),
        ("¿Cuál es un ejemplo de conocimiento previo sobre Easter: a) Easter is a celebration b) Easter is a pencil?", "a", "Easter es una celebración."),
    ],
    [
        (ADULT + "«It is Easter. Mia has chocolate eggs.» (Easter = Pascua, eggs = huevos). ¿Qué conocimiento ayuda: a) Easter is a celebration b) Easter is a school subject?", "a", "Easter es una celebración y encaja con los huevos."),
        (ADULT + "«A lion is at the zoo. It is a big cat.» ¿Qué crees que es un big cat: un gato pequeño o un animal grande como el león?", "Un animal grande como el león", "Big cat se relaciona con el león, que es un felino grande."),
        (ADULT + "«Leo has a red apple. He eats it.» (it = lo). ¿Una apple es comida o ropa?", "Comida", "Una manzana se come."),
    ],
    [
        ("Ana oye «The doctor is at the hospital». ¿Qué sabía que le ayuda a entender?", "Que los médicos trabajan en el hospital", "Es una relación que ya conoce."),
        (ADULT + "«Max is a dog. He can run.» Pedro dice que Max es un gato porque él tiene gato. ¿Qué dato del texto prueba que se equivoca?", "Max is a dog", "El texto dice dog, no cat."),
    ],
    [
        ("Mia escuchó que hay huevos en Pascua. ¿Qué frase usa bien su conocimiento y el texto: a) «Yo sé que en Easter hay huevos, y el texto dice que Mia tiene huevos de chocolate.» b) «Yo sé que en Easter hay huevos, así que el texto dice que Mia tiene una bicicleta.»", "a", "La frase a une lo que sabe con lo que dice el texto."),
        (ADULT + "«It is cold. Sam has a hat and gloves.» (cold = frío, gloves = guantes). Usa lo que sabes: ¿para qué usa Sam el gorro y los guantes?", "Para abrigarse del frío", "Con frío nos ponemos gorro y guantes."),
    ],
    [(ADULT + "En clase escuchas: «We are at the zoo. I see a lion.» (we are = estamos, at = en) ¿Qué sabes que te ayuda: que un león es un animal salvaje o que un león es un lápiz?", "Que un león es un animal salvaje", "Eso conecta con lo que ya conoces.")],
    [
        ("¿Cómo se dice «celebración» en inglés?", "celebration", "Celebration es celebración."),
        (ADULT + "«Tom opens the fridge.» ¿Qué cosas esperas encontrar dentro: comida o zapatos?", "Comida", "Un refrigerador guarda comida."),
        ("¿Qué debe mandar si lo que sabes y el texto no coinciden?", "El texto", "El texto es la prueba."),
    ],
    task("Un adulto lee dos veces: «It is Easter. Mia has chocolate eggs. She is happy.» Escribe en una hoja una cosa que sabes sobre Easter (por ejemplo: es una celebración) y una cosa que dice el texto (por ejemplo: Mia has chocolate eggs).", "Sé que Easter es una celebración; el texto dice que Mia tiene huevos de chocolate.", ["escribe algo que ya sabía", "escribe algo que dice el texto", "no mezcla las dos cosas"], ["hoja escrita", "nota del adulto"], ["decir lo que cree y no lo que dice el texto", "no escribir nada propio"], "Reconoce la diferencia entre lo que sabía y lo que dice el texto y pide un ejemplo más."),
    "Pide a un adulto que diga «fridge» y señala dónde está uno en tu casa, si hay.",
    "Escribe una cosa que sabes sobre los leones y una que sabes sobre los elefantes.",
)

lesson(
    OA4, 3,
    "Las imágenes descritas entre corchetes y los textos escritos en cada ejercicio, que lee un adulto; lápiz y hoja para tapar el guion.",
    "Aprenderé a usar una imagen como ayuda al escuchar, pero comprobando siempre con las palabras. Sirve para no confundirme si la imagen no muestra todo.",
    ["Sé predecir con pistas y conectar con lo que ya sé.", "Conozco los colores red, blue y green."],
    [
        "Una imagen (image) te ayuda a entender de qué habla el texto: ves un gato y oyes cat. Puedes mirar la imagen antes de escuchar y relacionar las dos cosas. Una imagen también te ayuda con palabras nuevas, porque ves lo que nombran.",
        "Pero una imagen no dice todo. Puede no mostrar un número exacto, un color si está en blanco y negro o lo que alguien dice. Si la imagen y las palabras no coinciden, las palabras mandan. Por ejemplo, si la imagen muestra un gato sobre una silla y oyes «under the chair», el texto dice que el gato está debajo.",
        "Usa la estrategia en tres pasos: 1) mira la imagen, 2) escucha las palabras clave y 3) comprueba si coinciden. Si no coinciden, confía en las palabras. Así no adivinas solo con la imagen.",
    ],
    [("image", "imagen"), ("match", "coincidir"), ("under", "debajo de"), ("on", "sobre"), ("black and white", "blanco y negro"), ("blue", "azul")],
    [
        ("Imagen y audio coinciden", "Imagen: [un gato negro sobre una silla]. " + ADULT + "«The black cat is on the chair.» ¿La imagen y el audio dicen lo mismo?", ["La imagen muestra un gato sobre la silla.", "El audio dice on the chair.", "Coinciden."], "Sí"),
        ("Imagen y audio no coinciden", "Imagen: [un gato negro sobre una silla]. " + ADULT + "«The cat is under the chair.» ¿Dónde está el gato según el audio?", ["La imagen muestra sobre la silla.", "El audio dice under.", "Las palabras mandan."], "Debajo de la silla"),
    ],
    [
        ("Elegir solo lo que muestra la imagen cuando el audio dice otra cosa.", "Se confía solo en la imagen.", "Si no coinciden, las palabras mandan; vuelve a escuchar."),
        ("Ignorar la imagen y no usarla como ayuda.", "Se pierde una pista útil.", "Mira la imagen antes de escuchar y comprueba con las palabras."),
    ],
    [
        ("Imagen: [un gato negro sobre una silla]. " + ADULT + "«The black cat is on the chair.» ¿Coinciden la imagen y el audio?", "Sí", "Los dos dicen que el gato está sobre la silla."),
        ("Imagen: [un gato negro sobre una silla]. " + ADULT + "«The cat is under the chair.» ¿Coinciden la imagen y el audio?", "No", "La imagen muestra sobre la silla y el audio dice debajo."),
        ("¿Qué significa «image»?", "Imagen", "Es un dibujo o una foto."),
    ],
    [
        ("¿Para qué sirve una imagen cuando escuchas?", "Para entender mejor las palabras y la situación", "La imagen da pistas."),
        ("Si la imagen y las palabras no coinciden, ¿qué debes seguir?", "Las palabras", "Las palabras dicen lo que realmente se cuenta."),
        ("¿La imagen siempre muestra todo?", "No; puede faltar información, como un número", "Por eso hay que escuchar."),
    ],
    [
        ("Imagen: [tres manzanas rojas]. " + ADULT + "«There are four red apples.» (apples = manzanas). ¿Cuántas manzanas dice el audio?", "4", "Four es cuatro."),
        ("Imagen: [un niño con un libro]. " + ADULT + "«The boy is reading a book.» ¿Qué hace el niño?", "Lee", "Reading significa leyendo."),
        ("Imagen: [una niña con una pelota en blanco y negro]. " + ADULT + "«She has a blue ball.» ¿De qué color es la pelota según el audio?", "Azul", "Blue es azul."),
    ],
    [
        ("Luis ve una pelota roja en la imagen y dice «es roja», pero el audio dijo «blue». ¿Qué hizo mal?", "Confió solo en la imagen", "El audio dice que la pelota es azul."),
        ("¿Qué dos fuentes de información debes usar juntas?", "La imagen y las palabras", "Se comprueban entre sí."),
    ],
    [
        ("Tres pares: A [imagen de un perro] y audio «dog». B [imagen de un gato] y audio «bird» (pájaro). C [imagen de un pez] y audio «fish» (pez). ¿En cuántos pares coinciden la imagen y el audio?", "2", "Coinciden A y C; B no."),
        ("Imagen: [un niño con un sombrero, en blanco y negro]. " + ADULT + "«The boy has a green hat.» ¿Qué dato solo te lo da el audio?", "El color verde del sombrero", "La imagen no muestra colores."),
    ],
    [("Ves el dibujo [una niña con un perro, en blanco y negro]. " + ADULT + "«Mia has a dog. The dog is brown.» (brown = café). ¿Qué dato solo te da el audio?", "Que el perro es café", "El dibujo no tiene color.")],
    [
        ("¿Qué significa «black and white»?", "Blanco y negro", "Black es negro y white es blanco."),
        ("Imagen: [un pájaro en un árbol]. " + ADULT + "«The bird is in the tree.» ¿Coinciden?", "Sí", "In the tree es dentro del árbol, igual que la imagen."),
        ("¿Qué haces si dudas entre la imagen y las palabras?", "Vuelvo a escuchar y sigo las palabras", "Las palabras son la prueba."),
    ],
    task("Mira esta imagen descrita: [un perro dentro de una caja]. Un adulto lee dos veces: «The dog is on the box.» Escribe si la imagen y el audio coinciden (sí o no) y luego escribe una frase que describa la imagen usando in the box.", "No coinciden; The dog is in the box.", ["dice que no coinciden", "escribe la frase con in the box", "usa las palabras para decidir"], ["frase escrita", "nota del adulto"], ["decir que coinciden", "no usar in the box"], "Reconoce que revisó imagen y audio y repite con él la diferencia entre in y on."),
    "Pide a un adulto que diga «cat» y muéstrale un dibujo de un gato que hayas hecho.",
    "Dibuja un gato sobre una silla y escribe tres palabras en inglés que lo describan; luego cambia el dibujo para que el gato esté debajo de la silla.",
)

lesson(
    OA4, 4,
    "Los textos y las preguntas escritos en cada ejercicio, que lee un adulto; lápiz y hoja para tapar el guion.",
    "Aprenderé a escuchar las palabras clave de un texto y a anotarlas. Sirve para responder sin necesidad de entender cada palabra.",
    ["Sé que una palabra clave dice una información importante.", "Conozco colores, números y objetos de la sala."],
    [
        "Una palabra clave (key word) es una palabra que lleva la información importante del texto: un objeto (cat, table), un color (red), un número (three) o una acción (eating). Las palabras como the, a y is ayudan a formar la frase, pero casi nunca son las palabras clave.",
        "Mira este ejemplo: «The cat is under the table.» Las palabras clave son cat, under y table. Si anotas esas tres palabras puedes responder «¿dónde está el gato?». También sirve en frases con deseos: «I want a big blue ball, please» (I want = yo quiero). Las palabras clave son big, blue y ball.",
        "No necesitas traducir todo. Mientras escuchas, anota dos o tres palabras clave. Después, usa esas palabras para responder la pregunta. Si te falta una palabra, vuelve a escuchar solo esa parte.",
    ],
    [("key word", "palabra clave"), ("I want", "yo quiero"), ("big", "grande"), ("ball", "pelota"), ("under", "debajo de"), ("in", "dentro de"), ("eating", "comiendo")],
    [
        ("Elegir palabras clave", ADULT + "«Mia has a green ball in the bag.» (bag = mochila). ¿Cuáles son tres palabras clave: a) green, ball, bag o b) has, a, the?", ["Las palabras clave llevan información.", "Green, ball y bag dicen color, objeto y lugar.", "Has, a y the solo forman la frase."], "a"),
        ("Usar las palabras clave", ADULT + "«Tom is eating bread.» (bread = pan). ¿Cuál es la palabra clave de la acción?", ["Busco qué hace Tom.", "Eating es la acción.", "La palabra clave es eating."], "eating"),
    ],
    [
        ("Anotar the, a e is como palabras clave.", "Se anotan palabras que no llevan información.", "Anota objetos, colores, números y acciones."),
        ("Intentar entender cada palabra antes de responder.", "Se pierde el hilo del texto.", "Anota dos o tres palabras clave y úsalas para responder."),
    ],
    [
        ("¿Qué es una palabra clave?", "Una palabra que lleva la información importante", "Dice qué, cuántos, de qué color o dónde."),
        (ADULT + "«The cat is under the table.» ¿Cuáles son dos palabras clave: cat y table o the y is?", "cat y table", "Nombran los objetos importantes."),
        (ADULT + "«Ana has a blue pencil.» ¿Cuál es la palabra clave del color?", "blue", "Blue es el color."),
    ],
    [
        ("¿Cuáles de estas palabras no suelen ser palabras clave: the, a, is, book?", "the, a, is", "Solo ayudan a formar la frase."),
        ("¿Por qué ayudan las palabras clave?", "Porque dicen la información importante", "Con ellas puedes responder."),
        ("¿Tienes que traducir todas las palabras para responder?", "No", "Basta con las palabras clave."),
    ],
    [
        (ADULT + "«Mia has a green ball in the bag.» ¿Cuáles son tres palabras clave: a) green, ball, bag o b) has, a, the?", "a", "Dicen color, objeto y lugar."),
        (ADULT + "«There are five birds in the tree.» (birds = pájaros, tree = árbol). ¿Cuál es la palabra clave del número?", "five", "Five es el número."),
        (ADULT + "«Tom is eating bread.» ¿Cuál es la palabra clave de la acción?", "eating", "Eating es la acción."),
    ],
    [
        ("Sofía anotó «is» y «the» como palabras clave de «The cat is under the table» y no pudo responder dónde está el gato. ¿Qué palabras debió anotar?", "cat, under, table", "Dicen quién y dónde."),
        (ADULT + "«Ben has three red apples.» ¿Cuál palabra clave sirve para responder How many?", "three", "Three es el número."),
    ],
    [
        (ADULT + "«Lia has a yellow bag. Tom has a green bag.» ¿Qué dos palabras clave distinguen las mochilas?", "yellow y green", "Son los colores diferentes."),
        (ADULT + "«Leo is drawing a big red circle.» (circle = círculo). De big, red y circle, ¿cuántas palabras dicen cómo es el círculo?", "2", "Big y red lo describen."),
    ],
    [(ADULT + "En una tienda alguien dice: «I want a big blue ball, please.» (please = por favor). ¿Cuáles son las palabras clave de lo que quiere?", "big, blue, ball", "Dicen tamaño, color y objeto.")],
    [
        ("¿Cómo se dice «palabra clave» en inglés?", "key word", "Key word es palabra clave."),
        (ADULT + "«The ball is on the chair.» ¿Cuáles son tres palabras clave: a) ball, on, chair o b) the, is, the?", "a", "Nombran el objeto, el lugar y la relación."),
        ("¿Cuántas palabras clave anotas mientras escuchas: todas o dos o tres?", "Dos o tres", "Así no pierdes el hilo."),
    ],
    task("Un adulto lee dos veces: «Mia has a green ball in the bag.» Escribe en una hoja las tres palabras clave que escuchaste y luego responde en español: ¿qué color es la pelota?", "green, ball, bag; verde.", ["escribe green, ball y bag", "responde verde", "no anota the ni a ni is"], ["hoja con palabras clave", "nota del adulto"], ["anotar has, a, the", "responder bag"], "Reconoce las palabras clave bien elegidas y repite con él la frase para comprobar."),
    "Pide a un adulto que diga «The cat is under the table» y repite solo las tres palabras clave.",
    "Escribe una frase con una palabra de color y una de objeto, por ejemplo «I want a red pencil».",
)

lesson(
    OA4, 5,
    "Los textos, las predicciones y las preguntas escritos en cada ejercicio, que lee un adulto; lápiz y hoja para tapar el guion.",
    "Aprenderé a comprobar mi predicción con lo que escucho y a cambiarla si el texto dice otra cosa. Sirve para entender de forma flexible.",
    ["Sé predecir con pistas.", "Sé usar palabras clave y comparar la imagen con las palabras."],
    [
        "Los pasos son: 1) predigo con pistas, 2) escucho el texto, 3) comparo mi predicción con lo que dice el texto y 4) mantengo o cambio mi idea. Comprobar (check) es ver si coincide. Revisar (revise) es cambiar mi idea cuando no coincide.",
        "Si coincide, digo «I was right», que significa «tenía razón». Si no coincide, digo «I change my mind. Now I think the story is about a cat», que significa «cambio de opinión. Ahora creo que el cuento trata de un gato». El texto es la prueba, no mi primera idea.",
        "Cambiar una predicción no es un error: significa que escuchaste bien. Por ejemplo, el título «The Big Box» (box = caja) te hace predecir un juguete. Pero si el texto dice «There is a cat in the box!», debes cambiar tu idea. La frase que prueba el cambio es la evidencia.",
    ],
    [("check", "comprobar"), ("revise", "cambiar o corregir"), ("I was right", "tenía razón"), ("I change my mind", "cambio de opinión"), ("Now I think", "ahora creo"), ("box", "caja"), ("in the box", "dentro de la caja")],
    [
        ("La predicción se confirma", "Predicción: «It is raining». " + ADULT + "«The sky is gray. Mia has an umbrella. It is raining.» ¿La predicción coincide con el texto?", ["Mi predicción es lluvia.", "El texto dice It is raining.", "Coincide."], "Sí; I was right"),
        ("La predicción se cambia", "Título: «The Big Box». Predicción: «a toy in the box». " + ADULT + "«Leo opens the big box. There is a cat in the box!» (opens = abre). ¿Coincide?", ["Predije un juguete.", "El texto dice a cat.", "No coincide, así que cambio mi idea."], "No; ahora creo que hay un gato"),
    ],
    [
        ("Mantener la predicción aunque el texto diga otra cosa.", "No se compara con el texto.", "Compara y cambia tu idea si no coincide."),
        ("Pensar que cambiar la predicción es un error.", "Se cree que equivocarse es malo.", "Cambiar tu idea muestra que escuchaste bien."),
    ],
    [
        ("¿Qué significa «check»?", "Comprobar", "Check es ver si algo coincide."),
        ("Predicción: «It is raining». " + ADULT + "«The sky is gray. Mia has an umbrella. It is raining.» ¿Coincide?", "Sí", "El texto confirma la lluvia."),
        ("¿Qué significa «I change my mind»?", "Cambio de opinión", "Se dice cuando el texto no coincide."),
    ],
    [
        ("¿Qué haces después de predecir y escuchar?", "Comparo mi predicción con el texto", "La comparación muestra si debo cambiar."),
        ("Si la predicción no coincide, ¿qué haces?", "La reviso y cambio mi idea", "El texto manda."),
        ("¿Cambiar una predicción es malo?", "No; es parte de entender", "Significa que escuché y comprobé."),
    ],
    [
        ("Título: «The Big Box». Predicción: «a toy in the box». " + ADULT + "«Leo opens the big box. There is a cat in the box!» ¿Coincide con tu predicción?", "No", "El texto dice cat, no toy."),
        ("Completa tu nueva idea: «Now I think the story is about a ___.»", "cat", "Cat es la palabra del texto."),
        ("Predicción: «dog». " + ADULT + "«Max is a dog. He can run.» ¿Mantienes tu predicción?", "Sí", "El texto dice que Max es un perro."),
    ],
    [
        ("Ana mantiene su predicción de que hay un juguete, aunque el texto dice gato. ¿Por qué es un problema?", "Porque el texto es la prueba y manda sobre la predicción", "La predicción debe comprobarse."),
        ("En el texto de la caja, ¿qué frase prueba que debes cambiar tu predicción?", "There is a cat in the box", "Dice qué hay en la caja."),
    ],
    [
        ("Tres predicciones: A «rain» y el texto confirma lluvia. B «toy» y el texto dice gato. C «dog» y el texto dice que Max es un perro. ¿Cuántas predicciones debes cambiar?", "1", "Solo B no coincide."),
        ("Ordena los pasos: A) comparo con el texto B) escucho C) predigo D) mantengo o cambio mi idea.", "C, B, A, D", "Primero predigo, luego escucho, comparo y decido."),
    ],
    [("Antes de escuchar «The Hungry Cat» predices «food». " + ADULT + "«The cat is hungry. Ana gives milk to the cat.» (gives = da, milk = leche). ¿Se confirma tu predicción?", "Sí", "La leche es comida y el gato tiene hambre.")],
    [
        ("¿Qué significa «I was right»?", "Tenía razón", "Se dice cuando la predicción coincide."),
        ("¿Qué significa «Now I think»?", "Ahora creo", "Introduce la nueva idea."),
        ("¿Qué palabra en inglés significa «caja»?", "box", "Box es caja."),
    ],
    task("Título: «The Big Box». Un adulto lee dos veces: «Leo opens the big box. There is a cat in the box!» Escribe tu predicción inicial (por ejemplo «a toy») y luego tu nueva idea completando: «Now I think the story is about a ___.»", "Predicción: un juguete. Nueva idea: Now I think the story is about a cat.", ["escribe una predicción inicial", "completa con cat", "dice que cambió su idea"], ["hoja con ambas frases", "nota del adulto"], ["mantener la predicción del juguete", "completar con toy"], "Reconoce el cambio de idea y repite con él la frase Now I think."),
    "Pide a un adulto que diga «I was right» y «I change my mind» y marca con el pulgar cuál suena a que cambió.",
    "Elige un título, escribe tu predicción y comprueba con otra persona si coincide con una historia corta que ella invente.",
)
