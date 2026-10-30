"""Student material for 4.º básico Inglés (propuesta), EN04 OA 04 (estrategias de comprensión oral).

Las «escuchas» las lee un adulto en voz alta; el guion va en el enunciado. Las imágenes se describen con palabras
(«Imagen (descrita): ...») para que todo ejercicio se pueda resolver solo con lo escrito.
"""
from __future__ import annotations

from student_content_en4_a import ADULT, E, lesson, task
from student_lessons import arith

OA4 = "EN04 OA 04"

BAKE = "«A girl is at the bakery. She wants bread. The baker gives her a loaf. She says: Thank you!»"
PET = "«Tom has a pet. It is small. It has long ears. It eats carrots. It is a rabbit.»"
K1 = "«Hello! I am Sam. Today I am at the park with my friend Leo. We have a red ball and three small cars. Leo is running. I am happy.»"

# ---------------------------------------------------------------- clase 1
lesson(
    OA4, 1,
    "Los títulos, las imágenes descritas y los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a predecir de qué trata un texto antes de escucharlo, usando el título, una imagen o la situación. Sirve para estar listo y entender mejor lo que oigo.",
    ["Sé nombrar animales, muebles, comidas y lugares en inglés.", "Sé que una predicción se comprueba después."],
    [
        "Predecir (predict) es pensar qué palabras o ideas vas a oír antes de escuchar. Las pistas son el título (title), una imagen y la situación. Si el título es «The Zoo», puedes esperar palabras como lion, monkey o giraffe. No esperarías sofa ni bus.",
        "Una predicción no es una respuesta final. Es una idea para comprobar mientras escuchas. Si oyes las palabras que esperabas, tu predicción se cumple. Si no, tienes que cambiarla. Equivocarse en una predicción no es un error grave: ayuda a prestar atención.",
        "Para predecir bien usa lo que ya sabes del tema. En «At the Bakery» (en la panadería) esperas bread (pan) y baker (panadero). En «Easter» esperas egg (huevo) y basket (canasta). Una pista que no sirve es algo sin relación con el texto, como el color de tu lápiz.",
    ],
    [("predict", "predecir: pensar qué vas a oír"), ("title", "título"), ("clue", "pista"), ("bakery / baker", "panadería / panadero"), ("loaf", "pan de molde o hogaza"), ("basket", "canasta"), ("Easter", "Pascua de Resurrección")],
    [
        ("Predecir con el título", "El título es «The Zoo». ¿Qué palabra es menos probable que oigas: lion, monkey o sofa?", ["Un zoo tiene animales.", "Lion y monkey son animales.", "Sofa es un mueble."], "sofa"),
        ("Comprobar", ADULT + BAKE + " (bakery = panadería, loaf = pan, gives = da). El título era «At the Bakery» y predije la palabra bread. ¿Se cumplió mi predicción?", ["Busco bread en el texto.", "Oigo She wants bread.", "La palabra aparece."], "Sí"),
    ],
    [
        ("Pensar que una predicción siempre es correcta.", "Una predicción es una idea que hay que comprobar.", "Escucha y revisa: si no se cumple, la cambias."),
        ("Usar una pista sin relación con el texto, como el color de tu lápiz.", "Esa pista no tiene que ver con el tema.", "Usa el título, la imagen o la situación."),
    ],
    [
        ("El título es «My Bedroom». ¿Qué palabra es menos probable que oigas: bed, lamp o elephant?", "elephant", "Bed y lamp son de un dormitorio; un elefante no."),
        ("Si el título es «Easter», ¿qué palabra esperas más: egg o bus?", "egg", "Los huevos son parte de la celebración de Easter."),
        ("¿Qué significa «predict»?", "Predecir", "Es pensar qué vas a oír antes de escuchar."),
    ],
    [
        ("¿Qué pista no sirve para predecir: el título, un dibujo o el color de mi lápiz?", "El color de mi lápiz", "No tiene relación con el texto."),
        ("¿Una predicción siempre es correcta?", "No, se comprueba mientras escucho", "Puede cumplirse o cambiar."),
        ("El título es «The Doctor». ¿Qué palabra es más probable: hospital o football?", "hospital", "Los doctores trabajan en un hospital."),
    ],
    [
        (ADULT + BAKE + " ¿Qué quiere la niña?", "Pan", "She wants bread."),
        (ADULT + "«Mia is at school. She has a ruler. She has a book. The teacher says: Open your book.» ¿Qué dice la profesora?", "Open your book", "Es lo que dice The teacher."),
        (ADULT + "«A boy is in the park. He is playing with a ball. A dog is running.» (ball = pelota). El título era «The Park». ¿Qué predicción se cumple: ball o bed?", "ball", "El texto dice a ball; no dice bed."),
    ],
    [
        ("Pedro predijo sofa para el título «The Zoo», pero el texto habla de leones. ¿Qué debe hacer?", "Cambiar su predicción por lo que escuchó", "Una predicción se corrige con lo que dice el texto."),
        ("Ana predice lion y Luis predice bed para un texto de título «The Zoo». ¿Cuál predicción es más razonable?", "lion", "Un zoo tiene animales y no camas."),
    ],
    [
        ("Imagen (descrita): un animal muy alto con cuello largo en un zoo. ¿Qué animal esperas oír: giraffe o bear?", "giraffe", "El cuello largo es una pista de la jirafa."),
        (ADULT + "«Ben is at the bakery. He wants two loaves of bread.» (loaves = panes). ¿Cuántos panes quiere Ben?", "2", "Two loaves son dos panes."),
    ],
    [(ADULT + "En clase ves el título «At the Hospital» y oyes: «The doctor helps a boy.» ¿Se cumple la predicción doctor?", "Sí", "La palabra doctor aparece en el texto.")],
    [
        ("¿Qué pista de un texto es el título?", "El nombre del texto", "El título da una pista del tema."),
        ("¿Qué significa «bakery»?", "Panadería", "Bakery es el lugar donde se hace pan."),
        ("¿Qué haces si tu predicción no se cumple?", "La cambio", "Escuchar sirve para corregirla."),
    ],
    task("Un adulto te muestra el título «At the Zoo» y lee dos veces: «A girl is at the zoo. She sees a zebra and a giraffe. She wants a photo.» (photo = foto). Antes de escuchar, escribe tres palabras que esperas oír. Después marca cuáles se cumplieron.", "Palabras posibles: lion, monkey, zebra. Se cumplió zebra.", ["escribe tres palabras relacionadas con el zoo", "marca las que se cumplieron", "no escribe palabras sin relación como sofa"], ["hoja con las predicciones", "nota del adulto"], ["escribir palabras sin relación con el título", "no comprobar con el texto"], "Reconoce las predicciones razonables y vuelve a escuchar con él para marcar las cumplidas."),
    "Pide a un adulto que diga «The Zoo» y di una palabra que esperas oír.",
    "Elige un título, como «At the Bakery», y escribe cinco palabras que esperas oír.",
)

# ---------------------------------------------------------------- clase 2
lesson(
    OA4, 2,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a conectar lo que escucho con lo que ya sé, es decir, mi conocimiento previo. Sirve para entender palabras nuevas y comprobar que el texto tiene sentido.",
    ["Sé predecir con el título.", "Conozco palabras de la escuela, la casa y los lugares de la ciudad."],
    [
        "El conocimiento previo (prior knowledge) es lo que ya sabes antes de escuchar. Si sabes que un doctor trabaja en un hospital y ayuda a personas enfermas, es más fácil entender «Dr. Lia works at the hospital». Conectar es unir lo que oyes con lo que ya sabes.",
        "Puedes conectar con tu escuela, tu casa, tus comidas o tus experiencias. Por ejemplo, si sabes que en una panadería se vende pan, entiendes que «The baker makes bread» habla de pan. Si sabes cómo es una jirafa, entiendes que neck (cuello) es una parte de su cuerpo.",
        "Ten cuidado: lo que sabes ayuda, pero el texto manda. Si el texto dice algo diferente de lo que tú sabías, aceptas lo que dice el texto y lo usas para responder. Pregúntate: ¿qué sé de este tema? y ¿el texto dice lo mismo?",
    ],
    [("prior knowledge", "conocimiento previo: lo que ya sé"), ("connect", "conectar, unir"), ("hospital", "hospital"), ("sick people", "personas enfermas"), ("baker", "panadero"), ("neck", "cuello"), ("chef", "cocinero o cocinera")],
    [
        ("Conectar con lo que sé", ADULT + "«Dr. Lia works at the hospital. She helps sick people.» (Dr. = doctora, works = trabaja, sick = enfermo). ¿Dónde trabaja la doctora Lia?", ["Busco works.", "Después oigo at the hospital.", "Sé que en un hospital se atiende a personas enfermas."], "En el hospital"),
        ("El texto manda", ADULT + "«The monkey eats leaves.» (leaves = hojas). Ana pensaba que los monos solo comen bananas. ¿Qué come el mono según el texto?", ["Lo que sé me ayuda a entender.", "Pero la pregunta es sobre el texto.", "El texto dice leaves."], "Hojas"),
    ],
    [
        ("Responder con lo que yo sé aunque el texto diga otra cosa.", "Se ignora lo que dice el texto.", "Usa lo que sabes como ayuda, pero responde con el texto."),
        ("No conectar con nada y escuchar palabra por palabra.", "Se pierde el sentido general.", "Pregúntate qué sabes del tema antes de escuchar."),
    ],
    [
        ("¿Qué es el conocimiento previo?", "Lo que ya sé antes de escuchar", "Es la información que traigo conmigo."),
        (ADULT + "«Dr. Lia works at the hospital. She helps sick people.» ¿A quién ayuda la doctora?", "A personas enfermas", "Sick people son personas enfermas."),
        ("¿Qué esperas comprar en una panadería: bread o lamp?", "bread", "Sé que en una panadería se vende pan."),
    ],
    [
        ("Si sabes que las jirafas tienen un cuello largo, ¿qué parte del cuerpo es «neck»?", "El cuello", "Neck significa cuello."),
        ("¿Qué palabra esperas oír en un texto sobre Easter: egg o bus?", "egg", "Muchas personas decoran huevos en Easter."),
        ("Si un texto no dice lo mismo que yo sabía, ¿qué uso para responder?", "Lo que dice el texto", "El texto manda."),
    ],
    [
        (ADULT + "«The monkey is hungry. It looks for bananas.» (looks for = busca). ¿Qué busca el mono?", "Bananas", "Looks for bananas significa busca bananas."),
        (ADULT + "«The teacher says: Open your book and read page ten.» (page = página). ¿En qué lugar ocurre esto?", "En la sala de clases", "Una profesora que habla de libros y páginas está en la escuela."),
        (ADULT + "«A baker makes bread every morning.» (every morning = cada mañana). ¿Qué hace el baker?", "Hace pan", "A baker es un panadero."),
    ],
    [
        (ADULT + "«The monkey eats leaves.» Ana dice que no puede ser porque ella pensaba que los monos solo comen bananas. ¿Qué debe hacer?", "Aceptar que el texto dice leaves", "El texto manda, aunque difiera de lo que ella pensaba."),
        ("¿Cuál es una buena conexión? a) Sé que un doctor trabaja en un hospital. b) Sé algo que el texto no dijo y no tiene relación.", "a", "La a une lo que oigo con algo que sé y que tiene relación."),
    ],
    [
        (ADULT + "«The chef cooks soup in a kitchen. He uses a big pot.» (chef = cocinero, pot = olla). ¿Dónde está el chef?", "En una cocina", "In a kitchen significa en una cocina."),
        arith("Ana tiene 6 huevos de Easter. Su amigo le da 4 más. ¿Cuántos huevos tiene ahora?", "6+4", "Se suman los huevos que tenía con los que le dan."),
    ],
    [(ADULT + "En un mercado oyes: «Four apples and two loaves of bread, please.» (please = por favor). Si sabes que un mercado vende comida, ¿qué piden?", "Manzanas y pan", "Apples son manzanas y bread es pan.")],
    [
        ("¿Qué significa «connect»?", "Conectar", "Unir lo que oigo con lo que sé."),
        ("¿Dónde trabaja un doctor?", "En un hospital", "Es lo que se sabe de ese trabajo."),
        ("¿El conocimiento previo reemplaza al texto?", "No, solo ayuda a entenderlo", "El texto es la fuente para responder."),
    ],
    task("Un adulto lee dos veces: «Eva is a baker. She works at the bakery. She makes bread and cakes every morning.» (cakes = queques). Escribe una cosa que ya sabías sobre un panadero y una cosa nueva que dice el texto. Marca si lo que sabías coincide con el texto.", "Sabía: un panadero hace pan. Nueva: Eva hace pan y queques cada mañana. Coincide.", ["escribe un conocimiento previo", "escribe un dato del texto", "indica si coincide"], ["hoja con ambas ideas", "nota del adulto"], ["escribir solo lo que sabía", "inventar un dato que el texto no dice"], "Reconoce la conexión y vuelve a leer con él el dato nuevo."),
    "Pide a un adulto que diga «doctor» y di una cosa que sabes sobre ese trabajo.",
    "Elige un tema como «The Zoo» y escribe tres cosas que ya sabes de él.",
)

# ---------------------------------------------------------------- clase 3
lesson(
    OA4, 3,
    "Las imágenes descritas y los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a usar una imagen como ayuda al escuchar, sin adivinar solo con ella. Sirve para comprobar que lo que veo y lo que oigo coinciden.",
    ["Sé predecir con el título.", "Sé conectar con lo que ya sé."],
    [
        "Una imagen (image) ayuda a entender porque muestra personas, objetos y lugares. Si ves una cocina y una olla, puedes pensar en la palabra soup (sopa). La imagen da pistas, pero no dice todo. Por ejemplo, no te dice el nombre de una persona ni lo que dice.",
        "Para usar bien una imagen, mira primero y luego escucha. Después comprueba si coinciden. Si la imagen muestra tres manzanas y el texto dice cinco, no sigas con la imagen: vuelve a escuchar. Las palabras del texto son las que dan la respuesta final.",
        "En este cuaderno las imágenes están descritas con palabras, por ejemplo «Imagen (descrita): una niña con un libro». Léela como si la vieras. Luego escucha el texto y responde con la información que oyes, usando la imagen solo como ayuda.",
    ],
    [("image", "imagen"), ("describe", "describir: decir cómo es algo"), ("circle", "círculo"), ("square", "cuadrado"), ("triangle", "triángulo"), ("pen", "lápiz de pasta"), ("sitting", "sentado")],
    [
        ("Imagen y texto", "Imagen (descrita): un dibujo con un círculo rojo, un cuadrado azul y dos triángulos amarillos. " + ADULT + "«I see a circle and a square. They are red and blue. And two yellow triangles.» ¿Cuántos triángulos hay?", ["La imagen muestra dos triángulos amarillos.", "El texto dice two yellow triangles.", "Imagen y texto coinciden."], "2"),
        ("Lo que la imagen no dice", "Imagen (descrita): una niña con un libro. " + ADULT + "«Ana has a book.» ¿Cómo se llama la niña?", ["La imagen no dice el nombre.", "El texto dice Ana.", "Respondo con el texto."], "Ana"),
    ],
    [
        ("Adivinar con la imagen y no escuchar el texto.", "La imagen no lo dice todo.", "Escucha el texto y úsalo como respuesta."),
        ("Seguir la imagen cuando no coincide con el texto.", "Se ignora lo que se oyó.", "Vuelve a escuchar y comprueba antes de responder."),
    ],
    [
        ("Imagen (descrita): una niña con un libro. " + ADULT + "«Mia has a book.» ¿Qué tiene Mia?", "Un libro", "Has a book significa tiene un libro."),
        ("¿Para qué sirve mirar una imagen mientras escuchas?", "Para encontrar pistas", "La imagen ayuda a entender el texto."),
        ("Una imagen muestra un león. ¿Qué necesitas para saber qué hace?", "Escuchar el texto", "La imagen sola no dice la acción."),
    ],
    [
        ("Imagen (descrita): tres huevos azules en una canasta. " + ADULT + "«There are three eggs in the basket. They are blue.» ¿De qué color son los huevos?", "Azules", "Blue significa azul."),
        ("Imagen (descrita): una niña. ¿Qué no puedes saber solo con la imagen: su nombre o su cabello?", "Su nombre", "El nombre se dice en el texto."),
        ("¿Cuál palabra de un texto se comprueba mejor con una imagen: triangle o thank you?", "triangle", "Una figura se puede ver en una imagen."),
    ],
    [
        ("Imagen (descrita): un niño sentado en una silla con un lápiz. " + ADULT + "«Leo is sitting on a chair. He is drawing a triangle.» (drawing = dibujando). ¿Qué dibuja Leo?", "Un triángulo", "El texto dice drawing a triangle."),
        ("Imagen (descrita): una cocina con una olla. " + ADULT + "«The cook is making soup.» (soup = sopa). ¿Qué prepara el cocinero?", "Sopa", "Making soup significa preparando sopa."),
        ("Imagen (descrita): una cebra junto a un río. " + ADULT + "«The zebra is drinking water. Two birds are on its back.» (back = lomo). ¿Cuántos pájaros hay?", "2", "Two birds son dos pájaros."),
    ],
    [
        ("Imagen (descrita): una niña con un delantal. Pedro dice que cocina. " + ADULT + "«Eva is painting a picture.» (picture = cuadro). ¿Qué hace Eva?", "Pinta un cuadro", "El texto manda: painting a picture."),
        ("La imagen muestra tres manzanas, pero el adulto dice «There are five apples». ¿Qué debes hacer?", "Volver a escuchar y comprobar", "Imagen y texto no coinciden."),
    ],
    [
        arith("Imagen (descrita): cuatro lápices de pasta rojos. " + ADULT + "«There are four red pens and six blue pens.» ¿Cuántos pens hay en total?", "4+6", "Se suman los pens rojos y los azules."),
        ("Imagen (descrita): un círculo y un cuadrado. " + ADULT + "«There are two circles, three squares and one triangle.» ¿Qué figura aparece en el texto y no en la imagen?", "El triángulo", "La imagen no muestra un triángulo."),
    ],
    [("Imagen (descrita): un parque con un árbol. " + ADULT + "«The dog is sleeping under the tree.» ¿Dónde duerme el perro?", "Debajo del árbol", "Under the tree significa debajo del árbol.")],
    [
        ("¿Qué significa «image»?", "Imagen", "Es un dibujo o una foto."),
        ("¿La imagen puede reemplazar al texto?", "No, ayuda pero no lo reemplaza", "El texto da la información final."),
        ("¿Cómo se dice «círculo» en inglés?", "circle", "Circle es círculo."),
    ],
    task("Imagen (descrita): una canasta con dos huevos rojos. Un adulto lee dos veces: «There are two eggs in the basket. They are red. A girl puts a blue egg in the basket.» Dibuja la canasta como queda al final y escribe cuántos huevos hay y de qué colores.", "Tres huevos: dos rojos y uno azul.", ["dibuja los huevos", "escribe 3", "indica rojo y azul"], ["dibujo del estudiante", "nota del adulto"], ["dibujar solo los dos huevos de la imagen", "olvidar el huevo azul"], "Reconoce el dibujo y vuelve a escuchar con él para añadir lo que dijo el texto."),
    "Pide a un adulto que diga «circle, square, triangle» y dibuja cada figura.",
    "Dibuja una escena y escribe tres frases en inglés que la describan, como «There is a ball.»",
)

# ---------------------------------------------------------------- clase 4
lesson(
    OA4, 4,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a fijarme en las palabras clave de un texto oral y a ignorar las que no ayudan a responder. Sirve para entender un texto largo sin oír cada palabra.",
    ["Sé usar el título, la imagen y lo que sé para predecir.", "Sé buscar un dato explícito en un texto."],
    [
        "Las palabras clave (key words) son las que llevan el significado del mensaje. Suelen ser objetos (ball, books), acciones (running, buying), números (seven, three), colores (red) y lugares (park, shelf). Las palabras pequeñas como a, the o is ayudan a unir la frase, pero casi nunca son la clave.",
        "Para encontrar las palabras clave, escucha la pregunta primero. Si te preguntan cuántos autos hay, escucha un número y la palabra cars. Si te preguntan dónde, escucha un lugar como under the tree. No tienes que recordar todo el texto: solo la parte que contesta la pregunta.",
        "Un texto puede tener frases de saludo o de relleno, como «Hello, hello! It is a nice day.» Esas frases no ayudan a responder la pregunta. Ignóralas y fíjate en la información que importa. Si no estás seguro, pide que lo vuelvan a leer.",
    ],
    [("key word", "palabra clave: lleva el significado"), ("number", "número"), ("color", "color"), ("place", "lugar"), ("action", "acción"), ("shelf", "repisa"), ("nice day", "buen día")],
    [
        ("Palabra clave de un color", ADULT + K1 + " (today = hoy, cars = autos, small = pequeños). ¿De qué color es la pelota?", ["Escucho la pregunta: color.", "Busco ball y oigo red.", "La palabra clave es red."], "Roja"),
        ("Palabras que no son clave", "En «A girl is buying a loaf», ¿qué palabra no es clave: a, buying o loaf?", ["Buying es una acción.", "Loaf es un objeto.", "A solo une la frase."], "a"),
    ],
    [
        ("Pensar que todas las palabras son igual de importantes.", "Se intenta recordar todo el texto.", "Escucha la pregunta y busca solo las palabras clave."),
        ("Elegir como clave una palabra pequeña como the.", "The solo une la frase.", "Elige objetos, acciones, números, colores o lugares."),
    ],
    [
        (ADULT + K1 + " ¿Qué color tiene la pelota?", "Roja", "La frase dice a red ball."),
        ("En «We have a red ball», ¿qué palabra clave responde a la pregunta del color: red o we?", "red", "Red es el color."),
        ("En «Three red cars are in the park», ¿qué palabra clave dice el color?", "red", "Red es el color; the y are solo unen la frase."),
    ],
    [
        (ADULT + K1 + " ¿Qué hace Leo?", "Corre", "Leo is running."),
        ("¿Qué tipo de palabras suelen ser clave: objetos, acciones y números o a y the?", "Objetos, acciones y números", "Esas palabras llevan el significado."),
        ("¿Qué debes escuchar primero para encontrar las palabras clave?", "La pregunta", "La pregunta dice qué buscar."),
    ],
    [
        (ADULT + "«Ana has seven books and two rulers. She puts the books on the shelf.» (shelf = repisa). ¿Cuántos libros tiene?", "7", "Seven books son siete libros."),
        (ADULT + "«Ana has seven books and two rulers. She puts the books on the shelf.» ¿Dónde pone Ana los libros?", "En la repisa", "On the shelf significa en la repisa."),
        arith(ADULT + "«Ana has seven books and two rulers. She puts the books on the shelf.» ¿Cuántos objetos tiene Ana en total entre libros y reglas?", "7+2", "Se suman los libros y las reglas."),
    ],
    [
        ("Luis dice que the es la palabra clave para saber qué hay en la mesa. ¿Tiene razón?", "No; la clave es el objeto, no the", "The solo une la frase."),
        (ADULT + "«The monkey eats a banana under the tree.» ¿Qué dos palabras clave responden dónde come el mono?", "under y tree", "Under the tree indica el lugar."),
    ],
    [
        arith(ADULT + "«Hello, hello! It is a nice day. I am Lia. I am nine. I have two cats and one dog. The cats are black. The dog is white.» ¿Cuántas mascotas tiene Lia?", "2+1", "Se suman los gatos y el perro."),
        (ADULT + "«Hello, hello! It is a nice day. I am Lia. I am nine. I have two cats and one dog. The cats are black. The dog is white.» ¿De qué color es el perro?", "Blanco", "White significa blanco."),
    ],
    [(ADULT + "En la clase escuchas: «Good morning! Today we are in the library. We have ten books.» (library = biblioteca). Si te preguntan cuántos libros hay, ¿qué palabra clave buscas?", "ten", "Ten es el número de libros.")],
    [
        ("¿Qué es una palabra clave?", "Una palabra que lleva el significado del mensaje", "Ayuda a responder la pregunta."),
        ("¿Cómo se dice «repisa» en inglés?", "shelf", "Shelf es repisa."),
        ("¿Las frases de saludo ayudan a responder siempre?", "No, muchas veces son relleno", "Se debe buscar la información que responde la pregunta."),
    ],
    task("Un adulto lee dos veces: «Hello! It is a nice day. I am Pam. I have five red pens and two blue pens. The pens are in my school bag.» Escribe la pregunta «¿Cuántos lápices rojos tiene Pam?» y subraya la palabra clave que la responde. Luego escribe las tres palabras clave que te dijeron cuántos y de qué color.", "Palabras clave: five, red, pens. Respuesta: cinco.", ["responde cinco", "subraya five o five red pens", "no elige hello o nice como clave"], ["hoja con respuesta y palabras clave", "nota del adulto"], ["elegir two blue pens", "subrayar hello"], "Reconoce la clave y vuelve a escuchar con él para encontrar el color."),
    "Pide a un adulto que lea «three red cars» y di cuáles son las palabras clave.",
    "Escribe un texto de tres frases con un número, un color y un lugar, y subraya las palabras clave.",
)

# ---------------------------------------------------------------- clase 5
lesson(
    OA4, 5,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a comprobar mi predicción mientras escucho y a corregirla si hace falta. Sirve para entender mejor, porque cambio mi idea cuando el texto me da nueva información.",
    ["Sé predecir, conectar con lo que sé, usar imágenes y buscar palabras clave.", "Sé que equivocarse en una predicción ayuda a aprender."],
    [
        "Comprobar (check) es escuchar el texto y ver si tu predicción se cumple. Revisar (revise) es cambiar tu idea cuando el texto dice algo distinto. Primero predices, luego escuchas, luego compruebas y, si hace falta, revisas. Así tu comprensión mejora.",
        "Por ejemplo, el título es «The Pet» y piensas que es un perro. Escuchas: «It is small. It has long ears. It eats carrots. It is a rabbit.» Entonces revisas: no es un perro, es un conejo. La evidencia es la frase «It is a rabbit». Cambiar una predicción es una buena estrategia.",
        "Para revisar bien, escribe la nueva idea y la frase que la prueba. Por ejemplo: «It is a rabbit because I heard It is a rabbit.» No cambies tu predicción sin evidencia ni la mantengas aunque el texto diga otra cosa. Escucha con atención las frases finales, que suelen dar la respuesta.",
    ],
    [("check", "comprobar"), ("revise", "revisar, corregir"), ("rabbit", "conejo"), ("carrot", "zanahoria"), ("ears", "orejas"), ("pet", "mascota"), ("evidence", "evidencia")],
    [
        ("Comprobar y revisar", ADULT + PET + " (pet = mascota, ears = orejas, carrots = zanahorias). Predije que era un perro. ¿Qué animal es según el texto?", ["Escucho todo el texto.", "Al final oigo It is a rabbit.", "Mi predicción no se cumple y la reviso."], "Un conejo"),
        ("Evidencia para revisar", "En el mismo texto, ¿qué frase prueba que no es un perro?", ["Busco la frase que nombra al animal.", "Es la última frase.", "It is a rabbit."], "It is a rabbit"),
    ],
    [
        ("Mantener la predicción aunque el texto diga otra cosa.", "Se ignora la evidencia.", "Compara con el texto y cambia la predicción."),
        ("Cambiar la predicción sin explicar con qué frase.", "No se muestra la evidencia.", "Agrega la frase del texto que prueba la nueva idea."),
    ],
    [
        ("¿Qué significa «revise»?", "Revisar o corregir", "Es cambiar una idea cuando el texto dice algo distinto."),
        (ADULT + PET + " ¿Qué animal es?", "Un conejo", "It is a rabbit."),
        ("Si lo que oyes no coincide con tu predicción, ¿qué haces?", "Cambio la predicción", "El texto es la evidencia."),
    ],
    [
        ("Pedro predijo dog. ¿Qué frase prueba que no es un perro: «It is a rabbit» o «Tom has a pet»?", "It is a rabbit", "Nombra el animal exacto."),
        ("¿Es malo equivocarse en una predicción?", "No, se corrige con el texto", "Equivocarse ayuda a escuchar con más atención."),
        ("¿Qué haces después de escuchar el texto: comprobar o predecir?", "Comprobar", "Predices antes y compruebas después."),
    ],
    [
        (ADULT + PET + " ¿Qué come el animal?", "Zanahorias", "It eats carrots."),
        (ADULT + PET + " ¿Cómo es el animal: pequeño o grande?", "Pequeño", "El texto dice It is small."),
        (ADULT + "«It is Easter. There are four eggs in the basket. Two are red and two are blue.» Predije que todos eran rojos. ¿Cuántos son azules?", "2", "Two are blue significa dos son azules."),
    ],
    [
        ("Ana predijo oír sobre un doctor con el título «At the School». El texto dice «Mia has a book and a ruler. The teacher says Hello.» ¿Qué palabra prueba que su predicción no se cumple?", "teacher", "Teacher es una persona de la escuela, no un doctor."),
        ("Lia predijo tres personas. El texto dice «Two girls and one boy are in the yard». ¿Se cumple su predicción?", "Sí", "Dos niñas más un niño suman tres personas."),
    ],
    [
        arith("Un niño predijo 5 monos en el zoo, pero el texto dice «eight monkeys». ¿Cuántos monos más hay que los que predijo?", "8-5", "Se resta lo que predijo a lo que dice el texto."),
        ("Elige la mejor revisión: a) It is a dog. b) It is a rabbit because I heard «It is a rabbit».", "b", "La b cambia la idea y muestra la evidencia."),
    ],
    [(ADULT + "En clase tu predicción es «Es una escena de Easter». Escuchas: «Today there are colorful eggs and a basket.» (colorful = de muchos colores). ¿Se cumplió?", "Sí", "Eggs y basket son pistas de Easter.")],
    [
        ("¿Qué significa «check»?", "Comprobar", "Check es ver si algo es correcto."),
        ("¿Qué necesitas para revisar una predicción?", "Una frase del texto que la pruebe", "La evidencia viene del texto."),
        ("¿Cómo se dice «conejo» en inglés?", "rabbit", "Rabbit es conejo."),
    ],
    task("Un adulto te dice el título «My Pet» y tú predices una palabra y la escribes. Luego lee dos veces: «My pet is small. It has two big ears. It likes carrots. It is not a cat. It is a rabbit.» Escribe tu predicción, escribe lo que el texto dice y si la cambias. Agrega la frase que lo prueba.", "Predicción: dog. Texto: es un rabbit. Reviso porque oí «It is a rabbit».", ["escribe una predicción", "escribe lo que dice el texto", "agrega la frase que lo prueba"], ["hoja con predicción y revisión", "nota del adulto"], ["no cambiar la predicción aunque no coincida", "no mostrar evidencia"], "Reconoce el cambio y vuelve a leer con él la última frase como evidencia."),
    "Pide a un adulto que lea «It is a rabbit» y cambia una predicción que habías escrito.",
    "Elige un título, como «My Pet», haz una predicción y escribe un texto de tres frases que la cambie.",
)
