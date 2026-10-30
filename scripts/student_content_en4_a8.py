"""Student material for 4.º básico Inglés (propuesta), EN04 OA 08 (estrategias de comprensión lectora).

Todos los textos son originales y están escritos en el enunciado. Las imágenes se describen con palabras
(«Imagen (descrita): ...») para que cada ejercicio se resuelva solo con lo escrito.
"""
from __future__ import annotations

from student_content_en4_a import E, lesson, task
from student_lessons import arith

OA8 = "EN04 OA 08"

RAB = "«My pet is a rabbit. It has long ears. It eats carrots every day. I give it fresh water.»"
PEN = "«A penguin is a bird. It cannot fly, but it can swim very well. Many penguins live in cold places.»"
APP = "«There are two red apples and three green apples.»"
LIA = "«Today is Saturday. Lia gets up at eight. She eats bread and milk. Then she goes to the park with her dog. At the park, she meets two friends. They play with a ball for one hour. Finally, they eat apples under a tree.»"
LADY = "«Tom has a ladybug on his hand. The ladybug is small and red with black dots.»"

# ---------------------------------------------------------------- clase 1
lesson(
    OA8, 1,
    "Los títulos, las imágenes descritas y los textos escritos en cada ejercicio; lápiz y papel.",
    "Aprenderé a mirar un texto antes de leerlo (título, imagen y primera frase) y a predecir de qué trata. Sirve para empezar a leer con una idea y comprobarla después.",
    ["Sé predecir con el título al escuchar.", "Sé que una predicción se comprueba."],
    [
        "Antes de leer, haz una vista previa (preview). Mira el título (title), la imagen (image) y la primera frase. Con esas pistas puedes predecir (predict) de qué trata el texto. Si el título es «My Pet Rabbit» y la imagen muestra un conejo con una zanahoria, esperas las palabras rabbit, carrot y eat.",
        "Una predicción es una idea que debes comprobar mientras lees. Si el texto dice lo que esperabas, tu predicción se cumple. Si dice otra cosa, la cambias. Equivocarse no es un error grave: ayuda a leer con más atención y a entender mejor el texto.",
        "Una buena predicción usa pistas del texto. Una mala predicción usa algo sin relación, como el color de la tapa del cuaderno. Después de leer, pregúntate: ¿mi predicción se cumplió? ¿qué palabra del texto me lo muestra? Así practicas leer con evidencia.",
    ],
    [("preview", "vista previa: mirar antes de leer"), ("predict", "predecir"), ("title", "título"), ("image", "imagen"), ("rabbit", "conejo"), ("carrot", "zanahoria"), ("fresh water", "agua fresca")],
    [
        ("Predecir con el título", "El título es «My School». ¿Qué palabra es menos probable que aparezca: desk, ruler o elephant?", ["Una escuela tiene escritorios y reglas.", "Un elefante no es parte de una escuela.", "La menos probable es elephant."], "elephant"),
        ("Comprobar", "Título: «My Pet Rabbit». Imagen (descrita): un conejo comiendo una zanahoria. Predije la palabra carrot. Lee: " + RAB + " (pet = mascota, ears = orejas, fresh = fresca). ¿Se cumplió mi predicción?", ["Busco carrot en el texto.", "Dice It eats carrots every day.", "La palabra aparece."], "Sí"),
    ],
    [
        ("Empezar a leer sin mirar el título ni la imagen.", "Se pierden pistas importantes.", "Haz una vista previa antes de leer."),
        ("Predecir con algo sin relación, como el color de la tapa del cuaderno.", "Esa pista no tiene que ver con el texto.", "Usa el título, la imagen o la primera frase."),
    ],
    [
        ("El título es «The Bakery». ¿Qué palabra es más probable: bread o giraffe?", "bread", "En una panadería se vende pan."),
        ("¿Qué significa «preview»?", "Mirar el título y las imágenes antes de leer", "Es la vista previa de un texto."),
        ("El título es «Easter». ¿Qué palabra es más probable: egg o chair?", "egg", "Los huevos son parte de la celebración."),
    ],
    [
        ("¿Cuál NO es una pista para predecir: el título, una imagen o el color de la tapa del cuaderno?", "El color de la tapa del cuaderno", "No tiene relación con el contenido."),
        ("Título «My Pet Rabbit». Imagen (descrita): un conejo con una zanahoria. ¿Qué comida predices: carrot o pizza?", "carrot", "La imagen muestra una zanahoria."),
        ("¿Cuándo compruebas tu predicción?", "Mientras leo y al terminar", "Comprobar es buscar la evidencia en el texto."),
    ],
    [
        ("Lee: " + RAB + " ¿Qué come el conejo?", "Zanahorias", "It eats carrots every day."),
        ("Lee: " + RAB + " ¿Qué tiene largo el conejo?", "Las orejas", "It has long ears."),
        ("Lee: " + RAB + " ¿Cada cuánto tiempo come zanahorias el conejo?", "Todos los días", "Every day significa todos los días."),
    ],
    [
        ("Pedro predijo la palabra cat para «My Pet Rabbit», pero el texto habla de un conejo. ¿Qué debe hacer?", "Cambiar su predicción", "El texto es la evidencia."),
        ("Título: «Easter Basket». Imagen (descrita): una canasta con tres huevos. Ana predijo three eggs. Lee: «There are three eggs in the basket. They are red, blue and yellow.» ¿Se cumplió?", "Sí", "El texto dice three eggs."),
    ],
    [
        ("Título: «At the Hospital». Imagen (descrita): una doctora y una niña. ¿Cuál predicción es mejor? a) The doctor helps a girl b) The doctor plays soccer on the moon", "a", "La imagen y el título apoyan la a."),
        ("Lee: " + RAB + " ¿Qué frase confirma que el conejo es una mascota?", "My pet is a rabbit", "Pet significa mascota."),
    ],
    [("Antes de leer un cartel de la biblioteca ves el título «Library Rules» (rules = reglas) y una imagen de un niño que dice shhh. ¿Qué predices: silencio o fútbol?", "silencio", "En una biblioteca se pide silencio.")],
    [
        ("¿Qué significa «predict»?", "Predecir", "Es pensar de qué trata antes de leer."),
        ("¿Qué haces si tu predicción no se cumple?", "La cambio", "Leer sirve para corregirla."),
        ("¿Cómo se dice «zanahoria» en inglés?", "carrot", "Carrot es zanahoria."),
    ],
    task("Mira el título «A Day at the Zoo» e imagina una imagen con un león y un mono. Escribe tres palabras que predices. Luego lee: «Today we are at the zoo. We see a lion and two monkeys. The monkeys are funny.» (funny = graciosos). Marca cuáles se cumplieron.", "Predicciones: lion, monkey, zoo. Se cumplieron las tres.", ["escribe tres palabras relacionadas con el zoo", "marca las que se cumplieron", "usa el texto para comprobar"], ["hoja con las predicciones", "nota del adulto"], ["escribir palabras sin relación como bed", "no comprobar con el texto"], "Reconoce las predicciones razonables y vuelve a leer con él para marcar las cumplidas."),
    "Mira el título de un libro en tu casa y di una palabra que esperas leer.",
    "Elige un título, como «My Favorite Animal», y escribe tres palabras que predices.",
)

# ---------------------------------------------------------------- clase 2
lesson(
    OA8, 2,
    "Los textos escritos en cada ejercicio; lápiz y papel.",
    "Aprenderé a conectar lo que leo con lo que ya sé, pero con cuidado: lo que sé ayuda, y el texto decide. Sirve para entender mejor sin cometer errores por suponer.",
    ["Sé predecir con el título y las imágenes.", "Sé que el texto es la evidencia."],
    [
        "El conocimiento previo (prior knowledge) es lo que ya sabes. Ayuda a entender un texto. Por ejemplo, sabes que las aves suelen volar. Pero leer con cuidado significa comprobar que lo que sabes también aparece en el texto. A veces el texto cuenta algo diferente.",
        "Lee este texto: «A penguin is a bird. It cannot fly, but it can swim very well.» La palabra but (pero) marca una diferencia con lo que esperabas: es un ave que no vuela. Si hubieras respondido solo con lo que sabías sobre las aves, habrías cometido un error. Aquí manda el texto.",
        "Para conectar con cuidado haz tres pasos. Uno: pregúntate qué sabes del tema. Dos: lee el texto con atención. Tres: comprueba si coinciden. También cuida las palabras como many (muchos): «Many penguins live in cold places» no dice que todos vivan en lugares fríos.",
    ],
    [("prior knowledge", "conocimiento previo: lo que ya sé"), ("penguin", "pingüino"), ("bird", "ave"), ("cannot fly", "no puede volar"), ("swim", "nadar"), ("many", "muchos"), ("but", "pero")],
    [
        ("Conocimiento previo y texto", "Lee: " + PEN + " (penguin = pingüino, bird = ave, cannot fly = no puede volar). Muchas aves vuelan. ¿Qué dice el texto del pingüino?", ["Sé que muchas aves vuelan.", "Busco cannot fly.", "El texto dice que no puede volar."], "Que no puede volar"),
        ("Dato que dice el texto", "En el mismo texto, ¿qué puede hacer el pingüino muy bien?", ["Busco can.", "Dice it can swim very well.", "Swim es nadar."], "Nadar"),
    ],
    [
        ("Responder solo con lo que sé, como decir que el pingüino vuela.", "Se ignora lo que dice el texto.", "Comprueba con el texto antes de responder."),
        ("Entender many como todos.", "Many no significa todos.", "Lee many como muchos, no todos."),
    ],
    [
        ("¿Qué es el conocimiento previo?", "Lo que ya sé antes de leer", "Es información que traigo conmigo."),
        ("Lee: " + PEN + " ¿Qué puede hacer el pingüino?", "Nadar", "It can swim very well."),
        ("Lee: " + PEN + " ¿Qué palabra marca una diferencia con otras aves?", "but", "But significa pero."),
    ],
    [
        ("¿Por qué hay que comprobar con el texto lo que sé?", "Porque lo que sé puede no ser igual en este caso", "El texto puede contar algo diferente."),
        ("Lee: " + PEN + " Sofía supone que todas las aves vuelan. ¿Esa idea sirve para el pingüino?", "No; el texto dice que el pingüino no vuela", "Cannot fly lo contradice."),
        ("Lee: " + PEN + " ¿Dice el texto que todos los pingüinos viven en lugares fríos?", "No, dice que muchos", "Many significa muchos."),
    ],
    [
        ("Lee: «The cook uses a big pot. He makes soup.» (pot = olla, soup = sopa). Sé que se cocina en una cocina. ¿El texto dice dónde está el cocinero?", "No, lo estoy suponiendo", "El texto no nombra el lugar."),
        ("Elige la conexión cuidadosa con el texto del pingüino: a) Sé que muchos animales nadan; el texto dice que el pingüino nada muy bien. b) Sé que el pingüino vive en mi casa.", "a", "La a une lo que sé con lo que dice el texto."),
        ("Lee: «The dog is sleeping under the table.» Ana sabe que los perros duermen en camas. ¿Dónde duerme el perro según el texto?", "Debajo de la mesa", "Under the table manda sobre lo que ella sabía."),
    ],
    [
        ("Lee: " + PEN + " Luis dice que el pingüino vuela porque es un ave. ¿Qué frase del texto lo contradice?", "It cannot fly", "Cannot fly significa no puede volar."),
        ("Lee: «The cat is sleeping on the sofa.» Pedro dice que los gatos duermen en cajas. ¿Qué debe responder si le preguntan dónde duerme el gato del texto?", "Sobre el sofá", "El texto dice on the sofa."),
    ],
    [
        ("Elige la oración que usa el conocimiento previo con cuidado: a) I know many birds fly, but the text says the penguin cannot fly. b) I know many birds fly, so the penguin flies.", "a", "La a respeta lo que dice el texto."),
        ("Si lo que sabes y lo que dice el texto no coinciden, ¿qué sigues para responder?", "El texto", "El texto es la evidencia."),
    ],
    [("En la clase de ciencias lees: «A whale lives in the sea.» (whale = ballena, sea = mar). ¿Dónde vive la ballena según el texto?", "En el mar", "Lives in the sea significa vive en el mar.")],
    [
        ("¿Qué significa «but»?", "Pero", "Marca una diferencia."),
        ("¿Qué significa «cannot»?", "No puede", "Cannot es la forma negativa de can."),
        ("¿Qué pasos sigues para conectar con cuidado?", "Pensar qué sé, leer y comprobar si coinciden", "Así no se supone de más."),
    ],
    task("Lee: «A bat is an animal that sleeps in the day. It flies at night.» (bat = murciélago, night = noche). Escribe una cosa que ya sabías de los animales y una cosa que el texto dice. Marca con una palabra si coinciden: yes o no.", "Sabía: algunos animales vuelan. El texto: el murciélago vuela de noche. Coinciden: yes.", ["escribe un conocimiento previo", "escribe un dato del texto", "marca yes o no"], ["hoja con las respuestas", "nota del adulto"], ["inventar un dato que el texto no dice", "no comprobar con el texto"], "Reconoce la conexión y vuelve a leer con él el dato del texto."),
    "Lee en voz alta «cannot fly, but can swim» y di de qué animal habla.",
    "Escribe un texto de dos frases con but sobre un animal que no hace lo que otros animales hacen.",
)

# ---------------------------------------------------------------- clase 3
lesson(
    OA8, 3,
    "Las imágenes descritas y los textos escritos en cada ejercicio; lápiz y papel.",
    "Aprenderé a leer las palabras y la imagen juntas y a comprobar que coinciden. Sirve para entender mejor y notar cuando una imagen no dice todo.",
    ["Sé predecir con el título.", "Sé conectar lo que sé con el texto."],
    [
        "Una imagen (image) que acompaña un texto ayuda a entender. Muestra cantidades, colores y lugares. Si la imagen muestra dos manzanas rojas y tres verdes, y el texto dice «two red apples and three green apples», imagen y texto coinciden. Entonces tu comprensión es más segura.",
        "A veces la imagen no muestra todo. Una imagen de un niño sentado bajo un árbol no te dice que está leyendo. Eso lo dice el texto: «He is reading a book». Entonces el texto agrega información. Si la imagen y el texto no coinciden, vuelve a leer la frase y decide con el texto.",
        "Para coordinar palabras e imagen, haz tres pasos. Primero mira la imagen. Segundo lee el texto. Tercero compara: ¿qué dato está en los dos?, ¿qué dato solo está en el texto?, ¿hay algo que no coincide? Este cuaderno describe las imágenes con palabras.",
    ],
    [("image", "imagen"), ("match", "coincidir"), ("red / green", "rojo / verde"), ("apples", "manzanas"), ("sitting", "sentado"), ("under", "debajo de"), ("reading", "leyendo")],
    [
        ("Imagen y texto coinciden", "Imagen (descrita): dos manzanas rojas y tres manzanas verdes. Lee: " + APP + " ¿Cuántas manzanas verdes hay?", ["La imagen muestra tres verdes.", "El texto dice three green apples.", "Coinciden: son tres."], "3"),
        ("El texto agrega información", "Imagen (descrita): un niño sentado bajo un árbol. Lee: «Leo is sitting under a tree. He is reading a book.» ¿Qué hace Leo?", ["La imagen muestra que está sentado.", "No muestra el libro.", "El texto agrega reading a book."], "Lee un libro"),
    ],
    [
        ("Responder solo con la imagen sin leer el texto.", "La imagen no muestra todo.", "Lee el texto para completar la información."),
        ("Ignorar un dato del texto que no coincide con la imagen.", "El texto da la información final.", "Vuelve a leer la frase y decide con el texto."),
    ],
    [
        ("Imagen (descrita): dos manzanas rojas y tres verdes. Lee: " + APP + " ¿Cuántas manzanas rojas hay?", "2", "Two red apples son dos manzanas rojas."),
        ("¿Para qué sirve una imagen que acompaña un texto?", "Para ayudar a entender las palabras", "La imagen da pistas."),
        ("Si imagen y texto no coinciden, ¿con cuál decides?", "Con el texto", "El texto da la información final."),
    ],
    [
        arith("Imagen (descrita): dos manzanas rojas y tres verdes. Lee: " + APP + " ¿Cuántas manzanas hay en total?", "2+3", "Se suman las manzanas de los dos colores."),
        ("Imagen (descrita): una niña con un pincel. Lee: «Eva is painting a picture. She uses red, blue and yellow.» (picture = cuadro). ¿Qué colores usa Eva?", "Rojo, azul y amarillo", "El texto nombra los tres colores."),
        ("Imagen (descrita): un niño sentado bajo un árbol. ¿Qué no puedes saber con solo la imagen: que está sentado o cómo se llama?", "Cómo se llama", "La imagen no dice el nombre; el texto lo diría."),
    ],
    [
        ("Imagen (descrita): una cebra junto a un río. Lee: «The zebra is drinking water. Three birds are near the river.» (near = cerca de, river = río). ¿Cuántos pájaros hay?", "3", "Three birds son tres pájaros."),
        ("Imagen (descrita): cuatro manzanas. Lee: «There are five apples.» ¿Cuántas manzanas dice el texto?", "5", "Las palabras dicen cinco; hay que volver a revisar."),
        ("Imagen (descrita): cuatro manzanas. Lee: «There are five apples.» ¿Qué debes hacer?", "Releer la frase y decidir con el texto", "Imagen y texto no coinciden."),
    ],
    [
        ("Ana dice que la imagen de un niño bajo un árbol muestra que está leyendo. ¿Tiene razón?", "No; la imagen no lo muestra, el texto lo dice", "El texto agrega reading a book."),
        ("Imagen (descrita): una canasta con tres huevos. Lee: «There are three eggs in the basket. They are blue.» ¿Qué dato agrega el texto?", "El color azul", "La imagen descrita no menciona el color."),
    ],
    [
        ("Imagen (descrita): un triángulo y un círculo. Lee: «There is a triangle, a circle and a square.» ¿Qué figura está en el texto y no en la imagen?", "El cuadrado", "La imagen no tiene cuadrado."),
        ("Imagen (descrita): una cocina con una mesa. Lee: «The cook is making soup. The table has four chairs.» ¿Cuántas sillas dice el texto?", "4", "Four chairs son cuatro sillas."),
    ],
    [("Imagen (descrita): una niña con una pelota. Lee: «Ana has a red ball.» (ball = pelota). ¿Qué dato agrega el texto sobre la pelota?", "Que es roja", "El texto dice el color.")],
    [
        ("¿Qué significa «match»?", "Coincidir", "Es que dos cosas dicen lo mismo."),
        ("¿Cómo se dice «manzanas» en inglés?", "apples", "Apples son manzanas."),
        ("¿La imagen reemplaza al texto?", "No, lo acompaña", "El texto da la información final."),
    ],
    task("Imagen (descrita): un parque con un árbol y un perro. Lee: «The dog is sleeping under the tree. Two birds are on the tree. A girl is reading a book.» Escribe qué dato está en la imagen y en el texto, y qué dato solo está en el texto.", "En ambos: perro y árbol. Solo en el texto: dos pájaros y la niña que lee.", ["escribe un dato que está en ambos", "escribe un dato solo del texto", "no agrega datos inventados"], ["hoja con los datos", "nota del adulto"], ["decir que la imagen muestra la niña", "inventar un dato"], "Reconoce lo que coincide y vuelve a leer con él qué agrega el texto."),
    "Lee en voz alta «two red apples» y dibuja lo que dice el texto.",
    "Dibuja una escena y escribe dos frases que coincidan y una que agregue un dato que el dibujo no muestra.",
)

# ---------------------------------------------------------------- clase 4
lesson(
    OA8, 4,
    "El texto escrito en los ejercicios; lápiz y papel.",
    "Aprenderé a releer para responder una pregunta específica: leo la pregunta, busco la palabra clave y vuelvo a la frase correcta. Sirve para no depender de la memoria al responder.",
    ["Sé buscar un dato explícito.", "Sé usar palabras clave."],
    [
        "Releer (reread) es volver a leer una parte del texto. Se hace para responder una pregunta específica. No hace falta leer todo de nuevo. Primero lee la pregunta. Segundo encuentra la palabra clave de la pregunta, por ejemplo friends (amigos) o hour (hora). Tercero busca esa palabra en el texto y relee la frase.",
        "Un texto puede tener muchos datos: horas, comidas, lugares y números. Si la pregunta es «How many friends?» (¿cuántos amigos?), la palabra clave es friends y buscas un número cerca. Si la pregunta es «Where do they eat apples?» (¿dónde comen manzanas?), buscas un lugar cerca de apples.",
        "Después de releer, comprueba tu respuesta con la frase. Si la frase dice lo mismo que tu respuesta, está bien. Si no, vuelve a buscar. Releer con una pregunta clara es más útil que leer sin objetivo.",
    ],
    [("reread", "releer"), ("question", "pregunta"), ("key word", "palabra clave"), ("gets up", "se levanta"), ("meets", "se encuentra con"), ("one hour", "una hora"), ("finally", "finalmente")],
    [
        ("Releer para un número", "Lee: " + LIA + " (gets up = se levanta, meets = se encuentra con, hour = hora). ¿Cuántos amigos encuentra Lia en el parque?", ["La palabra clave es friends.", "Releo At the park, she meets two friends.", "Two es dos."], "2"),
        ("Releer para un lugar", "En el mismo texto, ¿dónde comen manzanas?", ["La palabra clave es apples.", "Releo la última frase.", "Dice under a tree."], "Debajo de un árbol"),
    ],
    [
        ("Responder de memoria sin volver al texto.", "Se puede olvidar o confundir un dato.", "Relee la frase de la palabra clave."),
        ("Leer de nuevo todo el texto sin saber qué se busca.", "Se pierde tiempo.", "Lee primero la pregunta y busca su palabra clave."),
    ],
    [
        ("Lee: " + LIA + " ¿A qué hora se levanta Lia?", "A las ocho", "Lia gets up at eight."),
        ("Lee: " + LIA + " ¿Qué come Lia en el desayuno?", "Pan y leche", "She eats bread and milk."),
        ("Lee: " + LIA + " ¿Con quién va al parque?", "Con su perro", "She goes to the park with her dog."),
    ],
    [
        ("¿Qué haces primero para responder una pregunta específica?", "Leo la pregunta y busco su palabra clave", "Así sé qué frase releer."),
        ("En «How many friends?», ¿cuál es la palabra clave: how o friends?", "friends", "Friends dice de qué se pregunta."),
        ("Lee: " + LIA + " ¿Qué día es?", "Sábado", "Today is Saturday."),
    ],
    [
        ("Lee: " + LIA + " ¿Cuánto tiempo juegan con la pelota?", "Una hora", "They play with a ball for one hour."),
        ("Lee: " + LIA + " ¿Qué hacen al final?", "Comen manzanas", "Finally, they eat apples."),
        ("Lee: " + LIA + " ¿Con qué juegan?", "Con una pelota", "They play with a ball."),
    ],
    [
        ("Lee: " + LIA + " Pedro dice que Lia come manzanas en el desayuno. ¿Qué frase lo contradice?", "She eats bread and milk", "En el desayuno come pan y leche."),
        ("Lee: " + LIA + " Ana respondió que juegan dos horas. ¿Qué frase debe releer y qué dice?", "They play with a ball for one hour; dice una hora", "La respuesta correcta es una hora."),
    ],
    [
        ("Lee: " + LIA + " Ordena: A) Van al parque. B) Comen manzanas. C) Come pan y leche.", "C, A, B", "El texto sigue: desayuna, va al parque, come manzanas."),
        ("Lee: " + LIA + " ¿Cuántos alimentos distintos nombra el texto?", "3", "Bread, milk y apples son tres alimentos."),
    ],
    [("En la escuela te preguntan: «What time does Lia get up?» (what time = a qué hora). Lee el texto: «Lia gets up at eight. She eats bread.» ¿A qué hora se levanta?", "A las ocho", "At eight indica la hora.")],
    [
        ("¿Qué significa «reread»?", "Releer", "Re- indica volver a hacer algo."),
        ("¿Qué significa «gets up»?", "Se levanta", "Gets up es levantarse."),
        ("¿Dónde sacas la respuesta: de la memoria o del texto?", "Del texto", "Hay que volver a la frase."),
    ],
    task("Lee: «On Sunday, Pam goes to the library at ten. She reads two books. Then she writes a card for a friend. Finally, she goes home.» Escribe la pregunta «¿Cuántos libros lee Pam?», subraya la palabra clave y escribe la frase que usaste. Haz lo mismo con «¿Qué hace al final?».", "Dos libros (two books); al final va a casa (she goes home).", ["escribe la palabra clave", "escribe la frase usada", "responde las dos preguntas"], ["hoja con preguntas y frases", "nota del adulto"], ["responder tres libros", "no escribir la frase"], "Reconoce la palabra clave y vuelve a leer con él la frase que contesta."),
    "Lee en voz alta «at eight» y «for one hour» y di qué dato da cada una.",
    "Escribe un texto de cinco frases sobre un día tuyo y dos preguntas para que otra persona relea.",
)

# ---------------------------------------------------------------- clase 5
lesson(
    OA8, 5,
    "Los textos escritos en cada ejercicio; lápiz, papel y lápices de colores.",
    "Aprenderé a elegir y explicar una estrategia cuando no entiendo algo: releer, leer en voz alta, mirar la imagen, dibujar o recontar con ayuda. Sirve para reparar mi comprensión y seguir leyendo.",
    ["Sé predecir, conectar con lo que sé, coordinar imagen y texto y releer.", "Sé decir qué entendí y qué no."],
    [
        "Reparar (repair) la comprensión es arreglar lo que no entendiste. No hay una sola estrategia: depende del problema. Si no conoces una palabra y hay una imagen, mira la imagen y lee la descripción. Si perdiste el orden, relee paso a paso y numera. Si una frase larga te confunde, léela en voz alta (read aloud), despacio.",
        "Otras estrategias son dibujar lo que entendiste y recontar (retell) con ayuda: decir con tus palabras o con tu dibujo qué pasó. Una buena explicación nombra el problema y la estrategia: «No entendí ladybug, miré la imagen y leí small, red, black dots; creo que es un insecto».",
        "Escoge la estrategia que mejor responde a tu problema y explica por qué la elegiste. Saltarte el texto no es una estrategia de reparación. Si después de usar una estrategia todavía dudas, prueba otra o pide ayuda a una persona de tu casa o a tu profesora.",
    ],
    [("repair", "reparar: arreglar lo que no entendí"), ("read aloud", "leer en voz alta"), ("retell", "recontar con mis palabras"), ("draw", "dibujar"), ("ladybug", "chinita"), ("dots", "puntos"), ("strategy", "estrategia")],
    [
        ("Elegir estrategia", "Lee: " + LADY + " (ladybug = chinita, dots = puntos). Imagen (descrita): un insecto pequeño, rojo con puntos negros. No conozco la palabra ladybug. ¿Qué estrategia uso?", ["Hay una imagen y una descripción.", "Mirar la imagen y leer small, red, black dots ayuda.", "Uso la imagen y la descripción."], "Mirar la imagen y leer la descripción"),
        ("Explicar la estrategia", "Lee: «1. Take a pencil. 2. Draw a circle. 3. Color it blue.» Perdí el orden de los pasos. ¿Qué estrategia uso?", ["El problema es el orden.", "Releo paso a paso.", "Numero los pasos."], "Releer paso a paso"),
    ],
    [
        ("Saltarse el texto cuando es difícil.", "No es una estrategia de reparación.", "Elige una estrategia: releer, mirar la imagen, leer en voz alta o dibujar."),
        ("Usar siempre la misma estrategia para todos los problemas.", "Cada problema necesita una estrategia distinta.", "Piensa cuál es el problema y elige la mejor estrategia."),
    ],
    [
        ("¿Qué significa «repair» en la lectura?", "Arreglar lo que no entendí", "Es mejorar mi comprensión."),
        ("Lee: " + LADY + " ¿De qué color es la chinita?", "Roja", "The ladybug is small and red."),
        ("Lee: «1. Take a pencil. 2. Draw a circle. 3. Color it blue.» ¿De qué color pintas el círculo?", "Azul", "Color it blue."),
    ],
    [
        ("Una oración larga me confunde y no sé dónde termina cada idea. ¿Qué estrategia uso: leer en voz alta o dibujar?", "Leer en voz alta", "Leer despacio ayuda a separar las ideas."),
        ("Terminé un cuento pero no recuerdo quién hizo qué. ¿Qué estrategia uso: recontar con ayuda o saltar el texto?", "Recontar con ayuda", "Recontar ayuda a ordenar quién hizo qué."),
        ("¿Qué estrategia sirve si perdí el orden de unos pasos?", "Releer paso a paso", "Así vuelvo a ordenar los pasos."),
    ],
    [
        ("Lee: " + LADY + " ¿Cómo supo alguien qué era un ladybug sin conocer la palabra?", "Con la descripción y la imagen", "Small, red y black dots dan pistas."),
        ("Lee: " + LADY + " ¿Qué tiene la chinita en su cuerpo?", "Puntos negros", "Black dots son puntos negros."),
        ("Lee: " + LADY + " ¿Dónde está la chinita?", "En la mano de Tom", "On his hand."),
    ],
    [
        ("Ana dibuja lo que entendió de «Tom has a ladybug on his hand». ¿Es una buena estrategia?", "Sí; el dibujo muestra lo que entendió", "Dibujar permite comprobar la comprensión."),
        ("Pedro dice que lo mejor es saltarse un texto difícil. ¿Es una estrategia de reparación?", "No; hay que usar una estrategia para entender", "Releer, mirar la imagen o dibujar son estrategias."),
    ],
    [
        ("Elige la mejor explicación: a) No entendí ladybug, miré la imagen y leí small, red, black dots; creo que es un insecto. b) No entendí y no hice nada.", "a", "La a nombra el problema y la estrategia."),
        ("¿Qué problema se repara mirando una imagen? a) No conozco la palabra ladybug y hay una imagen. b) Perdí el orden de los pasos.", "a", "La imagen ayuda con palabras desconocidas; el orden se repara releyendo."),
    ],
    [("Lees una receta: «1. Take bread. 2. Put cheese on the bread.» y no recuerdas qué paso fue primero. ¿Qué estrategia usas?", "Releer los pasos en orden", "El orden de los pasos se recupera releyendo.")],
    [
        ("¿Qué significa «read aloud»?", "Leer en voz alta", "Aloud es en voz alta."),
        ("¿Qué significa «retell»?", "Recontar", "Es decir de nuevo con mis palabras."),
        ("¿Cómo se dice «chinita» en inglés?", "ladybug", "Ladybug es chinita."),
    ],
    task("Lee: «Eva has a hamster. The hamster is small and brown. It eats seeds. Eva gives it water in a small bowl.» (hamster = hámster, seeds = semillas, bowl = recipiente). Imagina que no conoces hamster. Escribe qué estrategia usas, qué pistas del texto te ayudan y qué crees que es un hamster.", "Estrategia: usar la descripción del texto (small, brown, eats seeds). Creo que es un animal pequeño.", ["nombra una estrategia", "usa pistas del texto", "explica qué entendió"], ["hoja con las respuestas", "nota del adulto"], ["no usar ninguna estrategia", "inventar un dato que el texto no dice"], "Reconoce la estrategia y vuelve a leer con él las pistas small, brown y eats seeds."),
    "Lee en voz alta una frase de este cuaderno despacio y di qué entendiste.",
    "Elige un texto de este cuaderno y escribe qué estrategia usarías si no entendieras una palabra.",
)
