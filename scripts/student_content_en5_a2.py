"""Student material for 5.º básico Inglés (propuesta), EN05 OA 03 (estrategias de escucha) y OA 04 (respuesta tras escuchar).

Las «escuchas» las lee un adulto en voz alta; el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Las imágenes se describen con palabras dentro del enunciado, para que no haga falta ningún dibujo externo.
Todos los textos son originales y cada palabra nueva lleva su pista en español.
"""
from __future__ import annotations

from student_content_en5_a import ADULT, lesson
from student_content_ma01_b import task
from student_lessons import arith

OA3 = "EN05 OA 03"
OA4 = "EN05 OA 04"

FARM = "«A Day at the Farm. Good morning! Today we visit a farm. There are three cows, two horses and ten chickens. The farmer, Mr. Soto, gives food to the animals. The children love to feed the chickens.» (farm = granja, cows = vacas, horses = caballos, chickens = gallinas, farmer = agricultor, feed = dar de comer)"
WATER = "«The sun heats the water in the sea. The water goes up. In the sky it becomes clouds. Then it rains, and the water goes back to the sea.» (heats = calienta, goes up = sube, sky = cielo, becomes = se convierte en, clouds = nubes, rains = llueve, goes back = vuelve)"
PICS = "Imagen A: un niño con paraguas bajo la lluvia. Imagen B: una niña toma un helado bajo el sol. Imagen C: un niño con bufanda y gorro en la nieve."
CLARIFY = "«Ana: The bus leaves at fifteen minutes past eight. Leo: Sorry, did you say fifteen or fifty? Ana: Fifteen. Leo: Okay, thanks.» (leaves = sale, minutes past = minutos después de, sorry = perdón, did you say = ¿dijiste?)"
KEY = "«The Lost Key. Tom comes home from school. He cannot open the door. He looks in his bag, in his pockets and under the mat. At last, he hears his sister inside. She opens the door. The key is in her hand. She says: Tom, you left it in the kitchen!» (key = llave, pockets = bolsillos, mat = felpudo, at last = por fin, inside = adentro, left = dejaste, kitchen = cocina)"

# ================================================================ OA 03
lesson(
    OA3, 1,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a hacer predicciones antes de escuchar y a escuchar con un propósito. Sirve para entender mejor porque sé qué dato busco.",
    ["Conozco palabras como farm, cow, rain y sun.", "Sé que how many es cuántos."],
    [
        "Antes de escuchar, mira el título y las imágenes y haz una predicción (prediction): una idea de lo que crees que vas a oír. Si el título es «A Day at the Farm» (un día en la granja), puedes predecir que oirás animales como cow, horse o chicken. Predecir prepara tu mente.",
        "Escuchar con un propósito (listening for a purpose) significa decidir qué quieres saber antes de escuchar. Por ejemplo: ¿cuántos animales hay? Con ese propósito no te distraes con los detalles que no necesitas. El propósito suele ser una pregunta con who, what, where, when o how many.",
        "Tu predicción puede ser correcta o no, y está bien. Lo importante es comprobarla después. Mientras escuchas, atiende a las palabras que coinciden con tu predicción y a las que no. Anota solo el dato de tu propósito, no todo lo que oyes.",
    ],
    [("prediction", "predicción: idea de lo que oirás"), ("purpose", "propósito: lo que quieres saber"), ("title", "título"), ("how many", "cuántos"), ("farm", "granja"), ("chicken", "gallina")],
    [
        ("Hacer una predicción", "El título de un texto es «A Rainy Day» (un día lluvioso). ¿Qué palabras crees que oirás: umbrella, boots, puddle o beach, sun, ice cream?", ["El título habla de lluvia.", "Con lluvia se usan paraguas y botas, y hay charcos.", "Umbrella, boots y puddle encajan."], "umbrella, boots y puddle"),
        ("Escuchar con propósito", ADULT + FARM + " Tu propósito es saber cuántos animales hay en total (vacas, caballos y gallinas). ¿Cuántos son?", ["Busco los números: three cows, two horses, ten chickens.", "Sumo 3 + 2 + 10.", "El total es 15."], "15"),
    ],
    [
        ("Pensar que una predicción equivocada es un error grave.", "Se cree que una predicción siempre debe ser correcta.", "Una predicción es una idea para comprobar; si falla, la corriges."),
        ("Anotar todo lo que se oye en vez del dato del propósito.", "No se eligió qué buscar antes de escuchar.", "Define tu pregunta antes y anota solo ese dato."),
    ],
    [
        ("Un texto se titula «At the Beach» (en la playa). ¿Qué palabra esperas oír? a) sand b) snow", "a) sand", "Sand es arena y se relaciona con la playa."),
        ("Un texto se titula «My Birthday Party». ¿Qué palabra esperas oír? a) cake b) homework", "a) cake", "En una fiesta de cumpleaños hay torta."),
        ("En Inglés: ¿Qué es una predicción?", "Una idea de lo que se oirá", "Se hace antes de escuchar y luego se comprueba."),
    ],
    [
        (ADULT + FARM + " Tu propósito: saber el nombre del agricultor. ¿Cómo se llama?", "Mr. Soto", "El texto dice The farmer, Mr. Soto."),
        (ADULT + FARM + " Tu propósito: saber qué animal alimentan los niños. ¿Cuál es? a) las gallinas b) las vacas", "a) las gallinas", "Dice the children love to feed the chickens."),
        ("Quieres saber a qué hora empieza una película. ¿Qué palabra de pregunta es tu propósito? a) What time b) Who", "a) What time", "What time se usa para preguntar la hora."),
    ],
    [
        ("Un texto se titula «Healthy Food» (comida saludable). ¿Qué palabras predices? a) fruit, vegetables, water b) race car, bicycle, helmet", "a)", "Las frutas, las verduras y el agua se relacionan con comida saludable."),
        (ADULT + "«We have a picnic in the park. We bring sandwiches, juice and a blanket.» (picnic = picnic, blanket = manta). Tu propósito: saber qué bebida llevan. ¿Cuál es?", "Jugo", "Dice juice entre las cosas que llevan."),
        arith("Tu propósito es saber el total de manzanas. Oyes: «Ana has five apples and Leo has four apples.» ¿Cuántas manzanas hay entre los dos?", "5+4", "Se suman las manzanas de Ana y de Leo."),
    ],
    [
        ("Julia predice que el texto «A Day at the Farm» hablará de un barco. ¿Es una buena predicción? Fundamenta con el título.", "No; el título habla de una granja y no de barcos", "Una predicción debe apoyarse en el título."),
        ("Pablo escucha el texto de la granja con el propósito «cuántos caballos hay». ¿Cuál es el dato?", "2", "Dice two horses."),
    ],
    [
        ("Lee: «Title: The Class Trip. Picture: a bus, children with hats and a zoo gate.» (trip = paseo). ¿Qué predices? a) Los niños van al zoológico en bus b) Los niños duermen", "a)", "El bus, los sombreros y el portón del zoológico dan la pista."),
        arith("Lee: «There are four red balloons and six blue balloons.» (balloons = globos). Tu propósito es saber cuántos globos hay en total. ¿Cuántos son?", "4+6", "Se suman los globos rojos y los azules."),
    ],
    [(ADULT + "En la clase de inglés ven el título «Winter Clothes» (ropa de invierno). ¿Qué palabras predices? a) scarf, coat y gloves (bufanda, abrigo y guantes) b) shorts y sandals (shorts y sandalias)", "a)", "En invierno se usa ropa abrigada.")],
    [
        ("¿Qué haces antes de escuchar: predecir o responder?", "Predecir", "Se predice mirando título e imágenes."),
        ("¿Qué es el propósito al escuchar?", "Lo que quiero saber", "Orienta qué dato buscar."),
        ("¿Qué pregunta usas para buscar una cantidad?", "How many", "How many pregunta por cuántos."),
    ],
    task("Lee el título «A Visit to the Library» (una visita a la biblioteca). Escribe tres palabras en inglés que predices oír y una pregunta de propósito con how many, what time o where. Un adulto lee después: «We go to the library on Monday at ten. We borrow two books each. The library is next to the park.» (each = cada uno, next to = al lado de). Responde tu pregunta y revisa si tus palabras aparecieron.", "Predicción: book, library, read. Propósito: What time? A las diez. Revisión: book y library aparecieron.", ["tres palabras coherentes con el título", "una pregunta de propósito", "responde con el texto y compara"], ["hoja con predicciones y respuesta", "nota del adulto"], ["predecir palabras sin relación con el título", "no comparar al final"], "Reconoce lo bien predicho y repite con él el propósito antes de escuchar de nuevo."),
    "Pide a un adulto que lea solo un título y di en voz alta tres palabras que esperas oír.",
    "Escribe un título inventado en inglés y tres palabras que esperarías oír en ese texto.",
)

lesson(
    OA3, 2,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a usar lo que ya sé y a fijarme en palabras clave para entender un texto. Sirve para seguir lo importante aunque no entienda cada palabra.",
    ["Sé que el sol calienta el agua y que las nubes dan lluvia.", "Conozco palabras como sun, water, sea y rain."],
    [
        "Tus conocimientos previos (prior knowledge) son lo que ya sabes del tema. Si escuchas un texto sobre la lluvia, ya sabes de Ciencias que el sol calienta el agua y que hay nubes. Ese saber te ayuda a entender y a adivinar lo que viene.",
        "Las palabras clave (key words) son las que llevan el mensaje principal: casi siempre son sustantivos, verbos y números. En «The sun heats the water in the sea» las palabras clave son sun, heats, water y sea. Palabras como the o in son pequeñas y no son clave. Las palabras clave suenan más fuerte.",
        "Para usarlas, relaciona lo que oyes con lo que sabes y atiende a las palabras clave. Si oyes sun, water y clouds, puedes pensar en la lluvia. Esto es relacionar con conocimientos previos. Con él entiendes una frase aunque no conozcas una palabra pequeña.",
    ],
    [("prior knowledge", "lo que ya sé"), ("key word", "palabra clave"), ("heats", "calienta"), ("goes up", "sube"), ("clouds", "nubes"), ("rains", "llueve")],
    [
        ("Palabras clave", ADULT + WATER + " ¿Cuáles son las palabras clave de la primera frase? a) sun, heats, water, sea b) the, in, and", ["La primera frase habla del sol, del agua y del mar.", "Esas palabras llevan el mensaje.", "The e in son palabras pequeñas."], "a) sun, heats, water, sea"),
        ("Conocimientos previos", "Ya sabes que las nubes se forman con agua. En el mismo texto, ¿qué viene después de clouds?", ["Busco la palabra después de clouds.", "Dice then it rains.", "Después de las nubes llueve."], "Llueve"),
    ],
    [
        ("Intentar entender cada palabra pequeña y perder el mensaje.", "No se separa lo clave de lo secundario.", "Fíjate en sustantivos, verbos y números: son las palabras clave."),
        ("Ignorar lo que ya sabes del tema.", "Se escucha como si todo fuera nuevo.", "Conecta lo que oyes con lo que ya aprendiste en la escuela."),
    ],
    [
        (ADULT + WATER + " ¿Qué hace el sol con el agua del mar? a) la calienta b) la congela", "a) la calienta", "Dice the sun heats the water."),
        (ADULT + WATER + " ¿En qué se convierte el agua en el cielo? a) en nubes b) en piedras", "a) en nubes", "Dice it becomes clouds."),
        ("En «The water goes up», ¿cuál es la palabra clave del movimiento: goes up o the?", "goes up", "Goes up es subir; the no lleva significado clave."),
    ],
    [
        (ADULT + WATER + " Ordena: A) llueve B) el sol calienta el agua C) se forman nubes.", "B, C, A", "El texto va de calentar, a nubes y a lluvia."),
        (ADULT + WATER + " ¿Adónde vuelve el agua al final? a) al mar b) a una montaña", "a) al mar", "Dice goes back to the sea."),
        ("Ya sabes que las plantas necesitan agua. Si oyes «The plant is dry», ¿qué crees que necesita? a) agua b) un abrigo", "a) agua", "Dry es seco; una planta seca necesita agua."),
    ],
    [
        ("En «The children eat lunch at school», ¿cuál es la palabra clave de la acción: eat o at?", "eat", "Eat es comer y at solo indica lugar."),
        (ADULT + "«Water becomes ice when it is very cold.» (ice = hielo, becomes = se convierte en). Con lo que sabes de Ciencias, ¿cuándo se vuelve hielo el agua?", "Cuando está muy fría", "El texto dice when it is very cold."),
        (ADULT + "«The seeds need water and light to grow.» (seeds = semillas, grow = crecer). ¿Cuántas cosas necesitan las semillas?", "2", "Necesitan agua y luz."),
    ],
    [
        ("Una compañera dice que en «The sun heats the water» la palabra clave es «the». ¿Tiene razón?", "No; sun, heats y water son las clave", "The es una palabra pequeña sin el mensaje principal."),
        (ADULT + "«The bees visit the flowers. They look for nectar.» (bees = abejas, flowers = flores, nectar = néctar). Con lo que sabes de Ciencias, ¿qué crees que son las abejas? a) insectos b) peces", "a) insectos", "Las abejas son insectos."),
    ],
    [
        (ADULT + "«On a sunny day, we play football at the park. We bring water because it is very hot.» (because = porque, hot = caluroso). Elige las tres palabras clave: a) football, park, water b) we, at, is", "a) football, park, water", "Son los sustantivos que llevan el mensaje."),
        ("En el mismo texto, ¿por qué llevan agua? a) porque hace mucho calor b) porque tienen sed siempre", "a) porque hace mucho calor", "Dice because it is very hot."),
    ],
    [(ADULT + "En la clase de Ciencias, el profesor dice: «Plants need light and water.» (plants = plantas, need = necesitan, light = luz). ¿Cuáles son las palabras clave? a) plants, need, light, water b) and", "a)", "Son las palabras que dicen qué necesitan las plantas.")],
    [
        ("¿Qué son los conocimientos previos?", "Lo que ya sé del tema", "Ayudan a entender un texto nuevo."),
        ("¿Qué tipo de palabras suelen ser clave: sustantivos y verbos o palabras pequeñas como the?", "Sustantivos y verbos", "Esas palabras llevan el mensaje."),
        ("¿Qué significa «goes up»?", "Sube", "Go es ir y up es hacia arriba."),
    ],
    task("Un adulto lee dos veces este texto: «A seed needs water, light and warm soil. First, the seed grows roots. Then a small plant comes out of the soil.» (seed = semilla, soil = tierra, roots = raíces, comes out = sale). Escribe cinco palabras clave que oíste y una cosa que ya sabías de Ciencias sobre las plantas.", "Palabras clave: seed, water, light, roots, plant. Ya sabía que las plantas necesitan agua y luz.", ["cinco palabras clave razonables", "relaciona con Ciencias", "no escribe palabras pequeñas como the"], ["hoja con respuestas", "nota del adulto"], ["anotar the, a, and", "no relacionar con lo que ya sabe"], "Reconoce las palabras clave bien elegidas y repite con él el texto, subrayando solo esas."),
    "Pide a un adulto que lea «The sun heats the water» y golpea la mesa solo cuando oigas una palabra clave.",
    "Escribe en español dos cosas que sabes sobre el agua y que te ayudarían a entender un texto en inglés sobre la lluvia.",
)

lesson(
    OA3, 3,
    "Las descripciones de imágenes y los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a relacionar lo que escucho con imágenes. Sirve para comprobar que entendí y para entender mejor palabras nuevas.",
    ["Conozco palabras como rain, sun, snow, umbrella, scarf y ice cream.", "Sé que A, B y C pueden nombrar imágenes."],
    [
        "Una imagen puede ayudar a entender un texto oral. Las imágenes muestran personas, objetos, lugares y acciones. Cuando oyes «The boy has an umbrella», puedes imaginar o buscar una imagen que muestre a un niño con paraguas. Así relacionas lo que oyes con lo que ves.",
        "Para elegir la imagen correcta, escucha las palabras clave y compáralas con cada imagen. Una imagen puede coincidir en una parte (el niño) y no en otra (el paraguas). Elige la que coincide en todo. Descarta primero las que no tienen ningún elemento del texto.",
        "También puedes hacer lo contrario: ver una imagen y predecir qué palabras oirás. Si ves a una niña con helado bajo el sol, esperas oír ice cream, sunny o hot. Usa imágenes para entender palabras desconocidas: si oyes scarf y la imagen muestra una bufanda, ya sabes su significado.",
    ],
    [("picture", "imagen"), ("umbrella", "paraguas"), ("scarf", "bufanda"), ("ice cream", "helado"), ("snow", "nieve"), ("match", "coincidir")],
    [
        ("Elegir la imagen", PICS + " " + ADULT + "«It is a snowy day. The boy wears a hat and a scarf.» (wears = lleva puesto). ¿Qué imagen coincide?", ["Busco snowy, hat y scarf.", "Imagen C tiene nieve, gorro y bufanda.", "A y B no tienen nieve."], "C"),
        ("Descartar", PICS + " Un adulto lee: «The girl eats an ice cream because it is hot.» ¿Qué imágenes descartas?", ["Busco ice cream y hot.", "La imagen B muestra helado y sol.", "A y C no tienen helado."], "A y C"),
    ],
    [
        ("Elegir una imagen solo porque aparece un niño.", "Se compara una sola parte.", "Revisa todos los elementos: niño, objeto, lugar y acción."),
        ("Ignorar la imagen cuando no se entiende una palabra.", "Se pierde una pista visual.", "La imagen ayuda a adivinar el significado de scarf, umbrella u otra palabra."),
    ],
    [
        (PICS + " " + ADULT + "«The boy has an umbrella. It is raining.» ¿Qué imagen coincide?", "A", "Hay paraguas y lluvia en la imagen A."),
        (PICS + " " + ADULT + "«It is a hot day. The girl has an ice cream.» ¿Qué imagen coincide?", "B", "Hay sol y helado en la imagen B."),
        (PICS + " " + ADULT + "«It is cold and snowy. The boy has a hat.» ¿Qué imagen coincide?", "C", "Hay nieve y gorro en la imagen C."),
    ],
    [
        ("Dos imágenes: X muestra a un perro durmiendo en una cama y Y muestra a un perro corriendo en un parque. Un adulto dice: «The dog is running in the park.» (running = corriendo). ¿Qué imagen coincide?", "Y", "Running y park coinciden con la imagen Y."),
        ("Dos imágenes: X muestra a una niña con un libro y Y muestra a una niña con una pelota. Oyes: «She reads a book.» (reads = lee). ¿Qué imagen coincide?", "X", "Book es libro y reads es lee."),
        ("En la imagen A hay un niño con paraguas. ¿Qué palabras predices oír: rain y umbrella o sun y beach?", "rain y umbrella", "El paraguas se usa con la lluvia."),
    ],
    [
        (PICS + " " + ADULT + "«The boy wears a coat, a hat and a scarf.» ¿Cuántas prendas de ropa se nombran?", "3", "Coat, hat y scarf son tres prendas."),
        ("Imagen X: una niña lee un libro bajo un árbol. Imagen Y: una niña juega fútbol en una cancha. Un adulto dice: «She is playing football.» (playing = jugando). ¿Qué imagen coincide?", "Y", "Playing football es jugar fútbol."),
        ("Oyes la palabra «umbrella» y no la conoces. La imagen A muestra un objeto abierto sobre un niño bajo la lluvia. ¿Qué crees que significa? a) paraguas b) zapatos", "a) paraguas", "El objeto que protege de la lluvia en la imagen es un paraguas."),
    ],
    [
        ("Imagen M: dos niños juegan fútbol de día. Imagen N: dos niños juegan fútbol de noche, con una luna. Oyes: «The boys play football at night.» (night = noche). ¿Qué imagen coincide y por qué palabra?", "N; por la palabra night", "Night es noche y N muestra la luna."),
        ("Oyes: «The cat is under the table.» (under = debajo de, table = mesa). Imagen P: gato sobre la mesa. Imagen Q: gato debajo de la mesa. ¿Cuál coincide?", "Q", "Under significa debajo de."),
    ],
    [
        ("Imagen R: cuatro manzanas. Imagen S: seis manzanas. Oyes: «There are six apples on the plate.» (plate = plato). ¿Qué imagen coincide?", "S", "Six es seis."),
        arith("Dos imágenes muestran 3 gatos y 4 gatos. Si juntas las dos imágenes, ¿cuántos gatos hay?", "3+4", "Se suman los gatos de las dos imágenes."),
    ],
    [(PICS + " " + ADULT + "En el recreo alguien dice: «Look at my new scarf! It is very warm.» (warm = abrigada). ¿Qué imagen muestra a alguien que podría tener una bufanda?", "C", "La bufanda se usa en la nieve, imagen C.")],
    [
        ("¿Qué significa «scarf»?", "Bufanda", "Scarf es una prenda para el cuello."),
        ("Si una imagen muestra lluvia y paraguas, ¿qué palabras esperas oír?", "rain y umbrella", "Esas palabras coinciden con la imagen."),
        ("¿Qué haces si una imagen coincide solo en una parte del texto?", "La descarto y busco una que coincida en todo", "Debe coincidir en todos los elementos."),
    ],
    task("Un adulto lee dos veces: «The girl is at the park. She has a red kite. The sun is shining. There is a tree behind her.» (kite = volantín, shining = brilla, behind = detrás de). Dibuja la escena con todos los elementos. Debajo, escribe en español cuatro objetos que dibujaste.", "Dibujo con niña, parque, volantín rojo, sol y árbol detrás. Objetos: niña, volantín, sol, árbol.", ["dibuja los cuatro elementos", "el volantín es rojo", "el árbol queda detrás de ella"], ["dibujo del estudiante", "nota del adulto"], ["olvidar el sol", "poner el árbol delante de la niña"], "Reconoce los elementos correctos y repite con él las palabras behind y red."),
    "Pide a un adulto que diga «umbrella, snow, ice cream» y dibuja un dibujo simple para cada palabra.",
    "Dibuja una escena de tu elección y escribe tres palabras en inglés que un adulto podría decir para describirla.",
)

lesson(
    OA3, 4,
    "Los diálogos escritos en cada ejercicio, que lee un adulto con dos voces; una hoja para tapar el guion y lápiz.",
    "Aprenderé a preguntar para aclarar o comprobar algo que no entendí al escuchar. Sirve para conversar en inglés sin quedarme con dudas.",
    ["Sé decir Sorry y Thank you.", "Reconozco los números de 13 a 19 y de 30 a 90."],
    [
        "A veces no entiendes algo. Para aclarar (clarify) puedes preguntar: «Can you repeat, please?» (¿puedes repetir?), «Sorry, what did you say?» (perdón, ¿qué dijiste?), «What does ___ mean?» (¿qué significa ___?) y «How do you spell it?» (¿cómo se deletrea?). Pedir ayuda es parte de escuchar bien.",
        "Para corroborar (check) algo que crees haber entendido, repites y preguntas: «Do you mean Friday?» (¿te refieres al viernes?), «Did you say fifteen or fifty?» (¿dijiste quince o cincuenta?) o «Is it at eight?» (¿es a las ocho?). La otra persona responde Yes, that's right o No, it's... Con eso confirmas el dato.",
        "Cuidado con los números: thirteen y thirty suenan parecido. En los números de 13 a 19 el acento va en el final (thir-TEEN); en 30, 40, 50 va al comienzo (THIR-ty). Por eso fifteen (15) y fifty (50) se confunden. Cuando dudes de un número, pregunta y escribe el número con cifras.",
    ],
    [("Can you repeat, please?", "¿puedes repetir, por favor?"), ("What does ___ mean?", "¿qué significa ___?"), ("Do you mean...?", "¿te refieres a...?"), ("Did you say...?", "¿dijiste...?"), ("fifteen / fifty", "quince / cincuenta"), ("spell", "deletrear")],
    [
        ("Aclarar", ADULT + CLARIFY + " ¿Qué pregunta hace Leo para asegurarse de la hora?", ["Busco la pregunta de Leo.", "Leo dice: did you say fifteen or fifty?", "Es una pregunta para corroborar."], "Did you say fifteen or fifty?"),
        ("Comprobar el dato", "En el mismo diálogo, ¿qué hora comprende Leo al final?", ["Ana responde Fifteen.", "Fifteen es quince.", "El bus sale a las ocho y quince."], "Las ocho y quince"),
    ],
    [
        ("Quedarse callado cuando no se entiende.", "Se pierde el dato y no se aprende nada.", "Pregunta: Can you repeat, please?"),
        ("Confundir fifteen con fifty.", "El acento cambia: fif-TEEN y FIF-ty.", "Pregunta o pide que escriban el número."),
    ],
    [
        ("Quieres que repitan lo que dijeron. ¿Qué dices? a) Can you repeat, please? b) See you tomorrow.", "a)", "Can you repeat, please? pide repetir."),
        ("No sabes lo que significa «borrow». ¿Qué preguntas? a) What does borrow mean? b) Where is the bus?", "a)", "What does ___ mean? pregunta por un significado."),
        ("¿Qué quiere decir «Do you mean Friday?»", "¿Te refieres al viernes?", "Se usa para corroborar un dato."),
    ],
    [
        ("Oyes un número que suena como «thirteen» o «thirty». ¿Qué preguntas? a) Did you say thirteen or thirty? b) Do you like pizza?", "a)", "Esa pregunta aclara cuál número se dijo."),
        ("Alguien dice: «The party is on Saturday.» Quieres comprobar. ¿Qué dices? a) Do you mean Saturday? b) How do you spell it?", "a) Do you mean Saturday?", "Repite el dato para corroborar."),
        ("Quieres saber cómo se escribe una palabra. ¿Qué preguntas? a) How do you spell it? b) Can I sit here?", "a)", "Spell significa deletrear."),
    ],
    [
        ("Alguien habla muy rápido y no entiendes. ¿Qué le pides? a) Could you speak more slowly, please? (slowly = despacio) b) What is your name?", "a)", "Esa frase pide que hablen más despacio."),
        ("Oyes: «There are sixteen students.» Quieres comprobar el número. ¿Qué preguntas? a) Do you mean sixteen? b) Do you like students?", "a)", "Do you mean...? sirve para comprobar un dato."),
        ("Elige el número 40: a) forty b) fourteen", "a) forty", "Forty es 40 y fourteen es 14."),
    ],
    [
        ("Elige el número 15: a) fifteen b) fifty", "a) fifteen", "Fifteen es 15 y fifty es 50."),
        ("Elige el número 30: a) thirteen b) thirty", "b) thirty", "Thirty es 30 y thirteen es 13."),
    ],
    [
        ("En el diálogo de Ana y Leo, el bus sale a las ocho y quince. Si el bus se atrasa 10 minutos, ¿a qué minutos después de las ocho sale?", "25", "15 + 10 = 25 minutos después de las ocho."),
        ("Un compañero escucha «The pen costs fifty pesos» y anota 15. ¿Qué debió preguntar? a) Did you say fifteen or fifty? b) Where is the pen?", "a)", "Esa pregunta evita confundir los números."),
    ],
    [(ADULT + "En una tienda, un vendedor dice: «The notebook is thirteen thousand pesos.» (thousand = mil). Quieres comprobar el precio. ¿Qué preguntas? a) Did you say thirteen or thirty? b) Thank you, goodbye.", "a)", "Esa pregunta confirma si es 13 o 30.")],
    [
        ("¿Qué significa «Did you say...?»", "¿Dijiste...?", "Sirve para comprobar lo que entendiste."),
        ("¿Qué frase usas para pedir que repitan?", "Can you repeat, please?", "Es una forma cortés."),
        ("¿Es mejor quedarse callado o preguntar cuando no entiendes?", "Preguntar", "Aclarar evita errores."),
    ],
    task("Un adulto lee dos veces: «A: The movie starts at six forty. B: Sorry, did you say six forty or six fourteen? A: Six forty. B: Thanks!» (movie = película, starts = empieza). Escribe la pregunta de B, la hora correcta con cifras y dos frases en inglés que usarías para aclarar algo (por ejemplo, Can you repeat, please?).", "Pregunta de B: did you say six forty or six fourteen? Hora: 6:40. Frases: Can you repeat, please? / What does ___ mean?", ["copia la pregunta", "escribe 6:40", "escribe dos frases para aclarar"], ["hoja con respuestas", "nota del adulto"], ["escribir 6:14", "no escribir frases para aclarar"], "Reconoce la hora correcta y practica con él, en voz alta, dos frases para aclarar."),
    "Pide a un adulto que diga fifteen y fifty y marca con el dedo cuál es cuál; luego pregunta Did you say fifteen or fifty?",
    "Escribe un diálogo de cuatro líneas en que una persona pide repetir un número.",
)

lesson(
    OA3, 5,
    "Los textos y predicciones escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a comprobar si mis predicciones eran correctas después de escuchar y a corregirlas si no. Sirve para entender mejor un texto y aprender de mis ideas.",
    ["Sé hacer una predicción a partir del título.", "Conozco palabras como key, door, bag y kitchen."],
    [
        "Verificar una predicción (to verify a prediction) es comparar lo que pensabas con lo que realmente dice el texto. Antes de escuchar predices. Después de escuchar, te preguntas: ¿mi predicción fue correcta, correcta en parte o equivocada? Si fue equivocada, no pasa nada: corriges y aprendes.",
        "Para verificar, necesitas una evidencia (evidence), que es una frase o palabra del texto que lo confirma. Por ejemplo, si predices que Tom no puede abrir la puerta y el texto dice «He cannot open the door», tu predicción se confirma. Si el texto dice otra cosa, la corriges.",
        "Después de escuchar puedes volver a escuchar una parte para comprobar. Pide al adulto que repita solo la frase que necesitas. Puedes decir: «Can you repeat the last sentence, please?» También puedes escribir la respuesta correcta junto a tu predicción equivocada.",
    ],
    [("verify", "comprobar"), ("evidence", "evidencia: frase del texto que lo prueba"), ("correct / wrong", "correcto / equivocado"), ("key", "llave"), ("door", "puerta"), ("kitchen", "cocina")],
    [
        ("Confirmar una predicción", ADULT + KEY + " Predijiste: «Tom no puede abrir la puerta». ¿Se confirma? ¿Qué frase lo prueba?", ["Busco la parte de la puerta.", "Dice he cannot open the door.", "La predicción se confirma."], "Sí; he cannot open the door"),
        ("Corregir una predicción", "Predijiste: «La llave está en su bolsillo». ¿Se confirma? ¿Dónde estaba la llave?", ["Busco dónde estaba la llave.", "Dice: the key is in her hand; Tom left it in the kitchen.", "La predicción es equivocada."], "No; la llave estaba en la cocina, en la mano de su hermana"),
    ],
    [
        ("Cambiar la predicción sin mirar lo que dice el texto.", "No se usa evidencia del texto.", "Busca la frase que confirma o corrige."),
        ("Sentirse mal por tener una predicción equivocada.", "Se cree que equivocarse es fallar.", "Una predicción equivocada ayuda a aprender más."),
    ],
    [
        ("Predijiste «Tom busca su llave». Se oye: «He looks in his bag, in his pockets and under the mat.» ¿Se confirma?", "Sí", "Looks in his bag, in his pockets and under the mat muestran que busca la llave."),
        ("¿Qué es la evidencia al verificar una predicción?", "Una frase o palabra del texto que la prueba", "Sin evidencia no se puede comprobar."),
        ("Si una predicción es equivocada, ¿qué haces? a) La corrijo con lo que dice el texto b) La dejo igual", "a)", "Se corrige con la evidencia."),
    ],
    [
        (ADULT + KEY + " Predijiste «Tom está contento al comienzo». Dice: «He cannot open the door.» ¿Se confirma?", "No", "No poder abrir la puerta no muestra alegría."),
        (ADULT + KEY + " Predijiste «Su hermana lo ayuda». ¿Se confirma? a) Sí; she opens the door b) No", "a)", "La hermana abre la puerta."),
        (ADULT + KEY + " ¿Quién tenía la llave al final? a) la hermana de Tom b) Tom", "a) la hermana de Tom", "Dice the key is in her hand."),
    ],
    [
        (ADULT + KEY + " Predijiste que la hermana de Tom está dentro de la casa. ¿Se confirma?", "Sí", "Dice he hears his sister inside."),
        (ADULT + KEY + " Predijiste «Tom grita enojado». ¿Se confirma?", "No", "El texto no dice que Tom grite ni que esté enojado."),
        arith("Hiciste 3 predicciones sobre el texto y 2 se confirmaron. ¿Cuántas debes corregir?", "3-2", "Se resta lo confirmado al total."),
    ],
    [
        ("Predicción de Ana: «Tom dejó la llave en el colegio». El texto dice: «You left it in the kitchen.» ¿Qué corrección haces?", "La llave estaba en la cocina", "La evidencia muestra otra ubicación."),
        ("Predicción de Luis: «La historia termina bien». El texto termina con la hermana abriendo la puerta. ¿Qué dices?", "Se confirma", "El problema se resuelve cuando la puerta se abre."),
    ],
    [
        ("Cuenta los lugares donde Tom busca la llave en el texto: bag, pockets, under the mat. ¿Cuántos lugares son?", "3", "Son la mochila, los bolsillos y debajo del felpudo."),
        ("En el texto, ¿qué parte de la predicción «Tom llega a su casa y no puede entrar» se confirma con la frase comes home from school?", "Que llega del colegio", "Esa frase muestra de dónde viene."),
    ],
    [(ADULT + "Predices que en el texto «At the Park» se hablará de columpios. Oyes: «The children play on the swings and the slide.» (swings = columpios, slide = tobogán). ¿Se confirma?", "Sí", "Swings son columpios.")],
    [
        ("¿Qué significa «verify»?", "Comprobar", "Verificar es comparar con el texto."),
        ("¿Qué frase pide repetir la última oración?", "Can you repeat the last sentence, please?", "Se usa para volver a escuchar un dato."),
        ("¿Una predicción equivocada es un fracaso?", "No", "Sirve para aprender."),
    ],
    task("Un adulto lee dos veces: «Title: A Surprise for Mom. Pablo hides a gift in the closet. His brother wants to see it. Pablo says: no! The gift is for Mom's birthday.» (hides = esconde, gift = regalo, closet = clóset, wants = quiere). Antes, escribe dos predicciones. Después, marca cada una como confirmada o corregida y anota la frase del texto que la prueba.", "Predicción 1: hay un regalo (confirmada: hides a gift). Predicción 2: es para el cumpleaños (confirmada: for Mom's birthday).", ["dos predicciones", "marca confirmada o corregida", "cita la evidencia"], ["hoja con predicciones y evidencia", "nota del adulto"], ["no citar evidencia", "cambiar la predicción sin comprobar"], "Aplaude la comparación hecha y repite con él cómo buscar la frase de evidencia."),
    "Pide a un adulto que lea una frase del texto de la llave y di si confirma tu predicción.",
    "Escribe una predicción sobre el título «The Lost Hat» y revisa después con un texto corto de tu invención.",
)

# ================================================================ OA 04
SMILE = "«Hello! My name is Lucía. I love summer because I can swim at the pool. I like ice cream, but I don't like very hot days. I feel happy when my friends come to my house. I am a little scared of storms.» (summer = verano, swim = nadar, pool = piscina, storms = tormentas, a little scared = un poco asustada)"

lesson(
    OA4, 1,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a decir lo que me gusta, lo que no me gusta y cómo me siento sobre algo que escuché. Sirve para reaccionar y compartir mis preferencias y sentimientos en inglés.",
    ["Sé decir I like y I don't like.", "Conozco happy, sad y scared."],
    [
        "Para decir una preferencia (preference) usa I like (me gusta), I love (me encanta), I enjoy (disfruto), I prefer (prefiero) y I don't like (no me gusta). Después de like y love puedes usar una cosa: I love summer, o un verbo con -ing: I like swimming (me gusta nadar).",
        "Para decir un sentimiento (feeling) usa I feel o I am con un adjetivo: happy (contento), sad (triste), excited (entusiasmado), scared (asustado), bored (aburrido), proud (orgulloso). También sirve «I feel happy when...» (me siento contento cuando...). Los sentimientos tienen una causa.",
        "Para dar la razón usa because (porque). «I love summer because I can swim.» La parte con because explica la preferencia o el sentimiento. Para contrastar usa but (pero): «I like ice cream, but I don't like hot days.» Al reaccionar a un texto, di lo que te gustó, cómo te sentiste y por qué.",
    ],
    [("I like / I love", "me gusta / me encanta"), ("I prefer", "prefiero"), ("happy / sad / scared", "contento / triste / asustado"), ("excited / bored / proud", "entusiasmado / aburrido / orgulloso"), ("because", "porque"), ("but", "pero")],
    [
        ("Encontrar una preferencia", ADULT + SMILE + " ¿Qué le encanta a Lucía y por qué?", ["Busco I love.", "Dice I love summer because I can swim at the pool.", "Le encanta el verano porque puede nadar en la piscina."], "El verano, porque puede nadar en la piscina"),
        ("Encontrar un sentimiento", "En el mismo texto, ¿cuándo se siente feliz Lucía?", ["Busco I feel happy.", "Dice when my friends come to my house.", "Se siente feliz cuando sus amigos vienen a su casa."], "Cuando sus amigos vienen a su casa"),
    ],
    [
        ("Decir «I am happy» para algo que no gusta.", "Se confunde el sentimiento con lo contrario.", "Usa I don't like para lo que no gusta y I am sad si te sientes triste."),
        ("Dar la preferencia sin razón.", "No se usa because.", "Agrega because y una razón: I love summer because I can swim."),
    ],
    [
        (ADULT + SMILE + " ¿Qué no le gusta a Lucía? a) los días muy calurosos b) el helado", "a) los días muy calurosos", "Dice I don't like very hot days."),
        (ADULT + SMILE + " ¿Qué le da un poco de miedo a Lucía? a) las tormentas b) la piscina", "a) las tormentas", "Dice a little scared of storms."),
        ("¿Qué significa «I enjoy reading»?", "Disfruto leyendo", "Enjoy es disfrutar."),
    ],
    [
        ("Completa: I love painting ___ it is relaxing. (relaxing = relajante). Elige because o but.", "because", "La segunda parte da la razón."),
        ("Completa: I like soup, ___ I don't like fish. (fish = pescado). Elige because o but.", "but", "La frase contrasta dos ideas."),
        ("Elige la frase que dice que alguien está aburrido: a) I am bored b) I am proud", "a) I am bored", "Bored significa aburrido."),
    ],
    [
        ("Escuchaste: «My team won the game!» (won = ganó). ¿Qué sentimiento es lógico? a) proud b) bored", "a) proud", "Ganar un partido da orgullo."),
        ("Escuchaste: «My dog is lost.» (lost = perdido). ¿Qué sentimiento es lógico? a) sad b) excited", "a) sad", "Perder a una mascota da pena."),
        ("Elige la oración correcta para decir que prefieres el pan al arroz: a) I prefer bread to rice. b) I prefer rice bread.", "a)", "I prefer X to Y compara dos cosas."),
    ],
    [
        ("Pablo dice «I like football because it is fun» (fun = divertido). ¿Qué parte es la razón?", "Because it is fun", "Después de because viene la razón."),
        ("¿Qué frase es una preferencia con razón? a) I love winter because I like snow. b) I love winter.", "a)", "La frase a) tiene because y una razón."),
    ],
    [
        ("Lee: «I like apples. I don't like onions. I love bananas.» (onions = cebollas). ¿Cuántas cosas le gustan o le encantan?", "2", "Le gustan apples y bananas."),
        ("En el texto anterior, ¿qué fruta le encanta? a) bananas b) apples", "a) bananas", "Dice I love bananas."),
    ],
    [(ADULT + "En clase, una niña cuenta: «My brother and I play chess on Sundays. I feel excited when I win.» (chess = ajedrez, win = gano). ¿Cómo se siente cuando gana? a) entusiasmada b) triste", "a) entusiasmada", "Excited es entusiasmado.")],
    [
        ("¿Qué significa «I prefer»?", "Prefiero", "Se usa para elegir una cosa sobre otra."),
        ("¿Qué palabra usas para dar una razón?", "because", "Because significa porque."),
        ("¿Qué significa «proud»?", "Orgulloso", "Proud es sentir orgullo."),
    ],
    task("Un adulto lee dos veces: «My name is Diego. I love the mountains because the air is fresh. I like skiing, but I don't like the cold wind. I am excited when it snows.» (mountains = montañas, air = aire, fresh = fresco, skiing = esquiar, wind = viento, snows = nieva). Escribe tres frases propias: una con I love... because, una con I like..., but I don't like... y una con I feel... when...", "I love music because it is fun. I like tea, but I don't like coffee. I feel happy when I play with my friends.", ["tres frases con la estructura pedida", "usa because y but", "dice un sentimiento"], ["hoja con frases", "nota del adulto"], ["no usar because", "escribir frases que no tienen sentido"], "Reconoce las frases bien armadas y repite con él cada estructura con otros ejemplos."),
    "Pide a un adulto que lea «I love music because it is fun» y repite la frase con otra cosa que te guste.",
    "Escribe tres frases con I like, I don't like y I feel sobre un animal que conoces.",
)

lesson(
    OA4, 2,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a dar una opinión sobre algo que escuché y a decir si estoy de acuerdo o no. Sirve para participar en conversaciones y justificar lo que pienso.",
    ["Sé usar because para dar razones.", "Conozco palabras como good, bad, interesting y boring."],
    [
        "Una opinión (opinion) es lo que piensas sobre algo. Para darla usa I think... (creo que...), In my opinion... (en mi opinión...) o I believe... (creo...). Después agrega una razón con because. Una opinión no es correcta o incorrecta como un dato; pero debe tener una razón.",
        "Para decir si estás de acuerdo usa I agree (estoy de acuerdo) o I disagree (no estoy de acuerdo). Ejemplo: «I agree because the story is exciting» (estoy de acuerdo porque la historia es emocionante). Para dar un adjetivo de opinión usa interesting (interesante), boring (aburrido), funny (divertido), difficult (difícil) o easy (fácil).",
        "Diferencia un hecho (fact) de una opinión. «The story has three characters» es un hecho. «The story is boring» es una opinión. Los hechos se pueden comprobar en el texto; las opiniones, no. Al opinar, sé respetuoso: puedes decir «I see your point, but I think...» (entiendo tu punto, pero creo...).",
    ],
    [("I think", "creo que"), ("In my opinion", "en mi opinión"), ("I agree / I disagree", "estoy de acuerdo / no estoy de acuerdo"), ("fact / opinion", "hecho / opinión"), ("interesting / boring", "interesante / aburrido"), ("difficult / easy", "difícil / fácil")],
    [
        ("Hecho u opinión", "¿«The story has three characters» es un hecho o una opinión?", ["Se puede comprobar contando los personajes.", "No depende de lo que yo piense.", "Es un hecho."], "Hecho"),
        ("Dar una opinión", "Alguien dice: «The video is interesting.» Tú estás de acuerdo porque el video muestra animales. ¿Qué frase dices?", ["Uso I agree.", "Agrego because y la razón.", "Digo: I agree because the video shows animals."], "I agree because the video shows animals"),
    ],
    [
        ("Decir una opinión sin razón: «It is boring.»", "No hay explicación.", "Agrega because: It is boring because nothing happens."),
        ("Presentar una opinión como un hecho.", "Se confunde lo que se piensa con lo que se puede comprobar.", "Usa I think para marcar que es una opinión."),
    ],
    [
        ("«The film lasts one hour.» (lasts = dura). ¿Es hecho u opinión?", "Hecho", "La duración se puede comprobar."),
        ("«The film is fantastic.» ¿Es hecho u opinión?", "Opinión", "Fantastic depende de lo que piense cada persona."),
        ("¿Qué significa «I disagree»?", "No estoy de acuerdo", "Disagree es lo contrario de agree."),
    ],
    [
        ("Completa: I ___ the game is fun because we play together. Elige think o enjoy.", "think", "I think introduce una opinión."),
        ("Elige la oración con razón: a) I like the book because it is funny. b) I like the book.", "a)", "Solo la opción a) tiene because y una razón."),
        ("Alguien dice «I think math is easy». Tú no estás de acuerdo porque a ti te parece difícil. ¿Qué dices? a) I disagree b) I agree", "a) I disagree", "Disagree expresa lo contrario."),
    ],
    [
        ("«I think the book is exciting.» (exciting = emocionante). ¿Es hecho u opinión?", "Opinión", "Empieza con I think y expresa lo que alguien piensa."),
        ("Elige un hecho: a) Santiago is a city. b) Santiago is the most beautiful city.", "a)", "Ser una ciudad se puede comprobar; ser la más linda es opinión."),
        ("Un amigo dice: «Let's go for a walk.» (walk = paseo). Tú quieres ir porque hace buen día. Completa: «I ___ with you because the day is nice.» Elige agree o disagree.", "agree", "Quieres lo mismo que tu amigo, así que estás de acuerdo."),
    ],
    [
        ("Mario dice: «In my opinion, the song is too slow because I want to dance.» ¿Cuál es la razón?", "Quiere bailar", "Después de because viene la razón."),
        ("Elige un hecho: a) The dog has four legs. b) The dog is the best pet. (legs = patas, pet = mascota)", "a)", "Las patas se pueden contar; ser el mejor es una opinión."),
    ],
    [
        ("Lee: «The museum is open from nine to five.» (museum = museo). ¿Es hecho u opinión?", "Hecho", "El horario se puede comprobar."),
        ("Lee: «The museum is boring.» ¿Es hecho u opinión?", "Opinión", "Aburrido depende de cada persona."),
    ],
    [(ADULT + "Un niño dice: «I think the park is the best place because there are many trees.» (best = mejor). ¿Cuál es su razón? a) Hay muchos árboles b) Está cerca", "a)", "Después de because dice many trees.")],
    [
        ("¿Qué significa «In my opinion»?", "En mi opinión", "Introduce lo que pienso."),
        ("¿Qué palabra agrega una razón?", "because", "Because significa porque."),
        ("¿Qué se puede comprobar: un hecho o una opinión?", "Un hecho", "Una opinión no se comprueba."),
    ],
    task("Un adulto lee dos veces: «The new school garden has flowers, vegetables and a small pond. The students water the plants every morning.» (garden = jardín, vegetables = verduras, pond = estanque). Escribe una frase de hecho sobre el texto, una opinión con I think... because... y si estás de acuerdo con I agree o I disagree sobre «The garden is a good idea».", "Hecho: The garden has a pond. Opinión: I think the garden is beautiful because it has flowers. I agree because plants are important.", ["un hecho correcto", "una opinión con because", "usa agree o disagree"], ["hoja con frases", "nota del adulto"], ["decir una opinión como hecho", "no dar razón"], "Reconoce el hecho y la opinión bien separados y repite con él el uso de because."),
    "Pide a un adulto que diga una opinión y respóndele con I agree o I disagree.",
    "Escribe una opinión con I think... because... sobre tu mascota o animal favorito.",
)

lesson(
    OA4, 3,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a relacionar lo que escucho con mi vida y con otras asignaturas como Ciencias, Matemática y Artes. Sirve para entender mejor y compartir lo que sé.",
    ["Sé que las plantas necesitan luz y agua.", "Conozco círculo, cuadrado y triángulo (circle, square, triangle)."],
    [
        "Relacionar (to connect) lo que escuchas con tu vida hace que el texto tenga sentido. Puedes usar frases como «It reminds me of...» (me recuerda a...), «I have the same...» (yo tengo el mismo...) o «In science class we learned...» (en la clase de Ciencias aprendimos...). Así muestras interés por lo escuchado.",
        "Con otras asignaturas, las conexiones son claras. En Ciencias: plants need water and light (las plantas necesitan agua y luz). En Matemática: shapes, como circle (círculo), square (cuadrado) y triangle (triángulo). En Artes: colors, como red, blue y yellow. Si el texto habla de formas, piensa en Matemática.",
        "Para conectar, hazte tres preguntas: ¿esto me pasó a mí?, ¿esto lo aprendí en otra clase? y ¿esto me recuerda a otra cosa? Luego formula una frase corta: «I connect this with science because plants need light». Las conexiones se dicen o escriben con una razón.",
    ],
    [("connect", "relacionar"), ("It reminds me of...", "me recuerda a..."), ("science / math / art", "ciencias / matemática / artes"), ("shape", "forma"), ("circle / square / triangle", "círculo / cuadrado / triángulo"), ("plants need light", "las plantas necesitan luz")],
    [
        ("Conectar con Ciencias", ADULT + "«A plant is in the sun. Its leaves are green and big. It grows near the window.» (leaves = hojas, grows = crece). ¿Con qué asignatura conectas el texto?", ["Hablan de una planta, sol y hojas.", "Eso se estudia en Ciencias.", "Se conecta con Ciencias."], "Ciencias"),
        ("Conectar con Matemática", ADULT + "«The sign has a circle, a square and a triangle.» (sign = letrero). ¿Con qué asignatura conectas el texto?", ["Hablan de formas.", "Las formas se estudian en Matemática.", "Se conecta con Matemática."], "Matemática"),
    ],
    [
        ("Conectar sin explicar por qué.", "La conexión queda sin sentido.", "Agrega una razón: I connect this with science because plants need light."),
        ("Elegir una asignatura al azar.", "No se relaciona con las palabras del texto.", "Busca palabras clave: plants (Ciencias), shapes (Matemática), colors (Artes)."),
    ],
    [
        ("Si oyes «red, blue and yellow», ¿con qué asignatura conectas: Artes o Ciencias?", "Artes", "Los colores se usan en Artes."),
        ("Si oyes «two plus three is five», ¿con qué asignatura conectas?", "Matemática", "Hay una suma."),
        ("¿Qué frase sirve para conectar con una experiencia personal? a) It reminds me of my school b) I disagree", "a)", "It reminds me of... relaciona con algo personal."),
    ],
    [
        (ADULT + "«Water boils when it is very hot.» (boils = hierve). ¿Con qué asignatura conectas? a) Ciencias b) Artes", "a) Ciencias", "El comportamiento del agua es de Ciencias."),
        (ADULT + "«The painter uses green and orange to make a forest.» (painter = pintor, forest = bosque). ¿Con qué asignatura conectas? a) Artes b) Matemática", "a) Artes", "Pintar y colores son Artes."),
        (ADULT + "«We have 12 pencils and 7 are blue.» (pencils = lápices). ¿Con qué asignatura conectas? a) Matemática b) Artes", "a) Matemática", "Hay números y cantidades."),
    ],
    [
        (ADULT + "«The moon moves around the Earth.» (moves = se mueve, Earth = Tierra). ¿Con qué asignatura conectas?", "Ciencias", "El movimiento de la Luna se estudia en Ciencias."),
        (ADULT + "«An artist makes a statue with clay.» (statue = estatua, clay = arcilla). ¿Con qué asignatura conectas?", "Artes", "Hacer una estatua es una actividad de Artes."),
        ("Oyes «cold, snow, winter». Para conectar con tu experiencia, ¿qué frase sirve? a) It reminds me of my winter holidays. b) It is a fact.", "a)", "It reminds me of... relaciona con algo vivido."),
    ],
    [
        ("En el texto de la planta, ¿qué necesita la planta según Ciencias? a) luz y agua b) un abrigo", "a) luz y agua", "Las plantas necesitan luz y agua."),
        arith("En el texto de los lápices hay 12 lápices y 7 son azules. ¿Cuántos no son azules?", "12-7", "Se resta la cantidad de lápices azules al total."),
    ],
    [
        ("Un compañero dice: «El texto de la planta me recuerda a mi casa, donde hay una planta en la ventana». ¿Es una conexión personal o con otra asignatura?", "Personal", "Habla de su propia casa."),
        ("Elige la mejor conexión con Ciencias: a) I connect this with science because plants need light. b) I connect this with science.", "a)", "La opción a) incluye una razón."),
    ],
    [(ADULT + "En el colegio, el profesor lee: «A square has four equal sides.» (equal = iguales, sides = lados). ¿Cuántos lados iguales tiene un cuadrado?", "4", "Four equal sides son cuatro lados iguales.")],
    [
        ("¿Qué significa «It reminds me of...»", "Me recuerda a...", "Conecta el texto con algo personal."),
        ("¿Con qué asignatura conectas la palabra «triangle»?", "Matemática", "Los triángulos se estudian en geometría."),
        ("¿Qué debes agregar a una conexión?", "Una razón", "Explicar por qué evita conexiones sin sentido."),
    ],
    task("Un adulto lee dos veces: «Bees are insects. They visit flowers and make honey. A group of bees lives in a hive.» (bees = abejas, insects = insectos, honey = miel, hive = colmena). Escribe una conexión con Ciencias y una conexión con tu vida. Cada una debe tener una razón con because.", "Con Ciencias: I connect this with science because bees are insects. Con mi vida: It reminds me of my garden because there are flowers.", ["dos conexiones", "ambas tienen because", "una es con Ciencias y otra personal"], ["hoja con frases", "nota del adulto"], ["escribir solo una", "no explicar con because"], "Reconoce las conexiones bien explicadas y repite con él una frase con It reminds me of."),
    "Pide a un adulto que diga una palabra como square, plant o blue y di con qué asignatura la conectas.",
    "Escribe en español una experiencia tuya que se relacione con el texto de las abejas.",
)

lesson(
    OA4, 4,
    "Las descripciones de datos y de imágenes escritas en cada ejercicio, que lee un adulto en voz alta; hoja, lápices de colores y regla.",
    "Aprenderé a mostrar lo que entendí con una ilustración, un esquema o un gráfico. Sirve para responder a un texto oral sin depender solo de las palabras.",
    ["Sé contar de 1 a 10 y sumar números pequeños.", "Conozco los colores red, blue, green y yellow."],
    [
        "Después de escuchar, puedes responder con dibujos o con representaciones (representations). Un dibujo con etiquetas (labels) muestra las partes: dibujas una casa y escribes door, window y roof (puerta, ventana y techo). Una etiqueta es una palabra corta que dice qué es cada parte.",
        "Un esquema (diagram) ordena la información. Un gráfico de barras (bar chart) muestra cantidades con barras de distinta altura. Una línea de tiempo (timeline) muestra el orden de los hechos. Hoy usarás un gráfico de barras: dibujas una barra por cada dato y la altura es el número.",
        "Para hacerlo bien, escucha los datos y anótalos en una tabla. Luego dibuja las barras con una regla. Escribe un título (title) y las etiquetas en cada barra. Revisa que cada barra coincida con el número. Si quieres una maqueta (model), usa objetos seguros de casa, como cajas o papel.",
    ],
    [("label", "etiqueta"), ("diagram", "esquema"), ("bar chart", "gráfico de barras"), ("timeline", "línea de tiempo"), ("model", "maqueta"), ("title", "título")],
    [
        ("Leer los datos", ADULT + "«Four children like pizza, three like pasta and two like soup.» (like = les gusta, pasta = pasta, soup = sopa). ¿Qué altura tiene la barra de pasta?", ["Busco pasta.", "Dice three like pasta.", "La barra de pasta mide tres."], "3"),
        ("Sumar los datos", "En el mismo texto, ¿cuántos niños hay en total?", ["Pizza 4, pasta 3, sopa 2.", "Sumo 4 + 3 + 2.", "El total es 9."], "9"),
    ],
    [
        ("Dibujar las barras sin respetar los números.", "No se mide cada dato.", "Usa una regla y marca una unidad por cada número."),
        ("Olvidar el título y las etiquetas.", "El gráfico no se entiende.", "Escribe un título y rotula cada barra."),
    ],
    [
        (ADULT + "«Four children like pizza, three like pasta and two like soup.» ¿Qué comida tiene la barra más alta?", "Pizza", "El 4 es el número más grande."),
        (ADULT + "«Four children like pizza, three like pasta and two like soup.» ¿Cuántos niños más prefieren pizza que sopa?", "2", "4 − 2 = 2."),
        ("¿Qué es una etiqueta en un dibujo?", "Una palabra que dice qué es cada parte", "Las etiquetas aclaran el dibujo."),
    ],
    [
        ("Dibuja en tu mente un gráfico con barras de 5, 3 y 6 manzanas. ¿Cuál es la barra más baja?", "3", "El 3 es el menor de 5, 3 y 6."),
        arith("Un gráfico muestra 5 rojas, 3 verdes y 6 amarillas. ¿Cuántas manzanas hay en total?", "5+3+6", "Se suman las tres barras."),
        ("Dibujas una casa. ¿Qué etiqueta pones en la parte por donde se entra? a) door b) roof", "a) door", "Door es puerta y roof es techo."),
    ],
    [
        ("En un gráfico las barras miden 4, 7 y 5. ¿Cuánto mide la barra más alta?", "7", "El 7 es el mayor de 4, 7 y 5."),
        arith("En el mismo gráfico las barras miden 4, 7 y 5. ¿Cuánto suman?", "4+7+5", "Se suman las tres barras."),
        ("Quieres rotular un dibujo de una casa con la palabra «ventana» en inglés. ¿Cuál escribes? a) window b) roof", "a) window", "Window es ventana y roof es techo."),
    ],
    [
        ("Un compañero hizo una barra de 8 para un dato que era 5. ¿Cuántas unidades se pasó?", "3", "8 − 5 = 3."),
        ("¿Por qué es útil una línea de tiempo después de escuchar «First... then... finally»? a) Muestra el orden de los hechos b) Muestra los colores", "a)", "La línea de tiempo ordena los hechos."),
    ],
    [
        ("Escuchas: «Mario has two red balls, three blue balls and one green ball.» ¿Cuántas pelotas azules deben tener las barras?", "3", "Three blue balls."),
        arith("Escuchas: «Mario has two red balls, three blue balls and one green ball.» ¿Cuántas pelotas tiene Mario en total?", "2+3+1", "Se suman las pelotas de los tres colores."),
    ],
    [(ADULT + "En el recreo hacen una encuesta: «Five students choose football, four choose basketball and one chooses tennis.» (choose = eligen). ¿Cuántos estudiantes respondieron en total?", "10", "5 + 4 + 1 = 10.")],
    [
        ("¿Qué muestra la altura de una barra en un gráfico?", "La cantidad", "Mientras más alta, mayor es el número."),
        ("¿Qué es un título en un gráfico?", "El nombre que dice de qué trata", "El título ayuda a entenderlo."),
        ("¿Qué significa «label»?", "Etiqueta", "Label es una palabra que identifica algo."),
    ],
    task("Un adulto lee dos veces: «In our class, six children have a cat, eight have a dog and two have a fish.» (cat = gato, dog = perro, fish = pez). Dibuja un gráfico de barras con una barra para cat, otra para dog y otra para fish. Pon título y etiquetas, y escribe cuántos niños hay en total.", "Barras de 6, 8 y 2. Título: Pets in our class. Total: 16.", ["tres barras con alturas 6, 8 y 2", "título y etiquetas", "total 16"], ["dibujo del gráfico", "nota del adulto"], ["alturas que no coinciden", "olvidar el total"], "Reconoce las barras bien dibujadas y revisa con él que cada altura sea igual al número."),
    "Pide a un adulto que lea «three red, two blue» y dibuja dos barras con esos números.",
    "Haz tu propio gráfico con cuántas frutas hay en tu casa: dibuja las barras y pon un título en inglés.",
)

lesson(
    OA4, 5,
    "Los textos y diálogos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a escribir un resumen breve de lo que escuché y a preparar una pequeña dramatización o presentación oral. Sirve para compartir lo que entendí con otras personas.",
    ["Sé usar first, next y finally.", "Sé decir mis preferencias con I like y because."],
    [
        "Un resumen (summary) cuenta lo más importante en pocas frases. Tiene la idea principal y dos o tres datos, en orden. No incluye detalles pequeños ni tu opinión. Para resumir: 1) busca quién y qué; 2) anota los hechos clave; 3) escríbelos con first, next y finally.",
        "Una dramatización (role play) usa personajes y diálogo. Cada actor sabe sus líneas (lines) y las dice con gestos. Una presentación oral (oral presentation) se organiza en tres partes: inicio («Today I'm going to talk about...»), desarrollo (los datos) y cierre («Thank you for listening»).",
        "Cuando preparas tu respuesta, piensa a quién se la vas a mostrar: un compañero o una persona de tu casa. Habla despacio, mira a quien te escucha y usa tus notas. Puedes pedir ayuda con una frase como «Can you help me with this word?». Revisa que tu resumen tenga la idea principal.",
    ],
    [("summary", "resumen"), ("role play", "dramatización"), ("oral presentation", "presentación oral"), ("line", "línea de diálogo"), ("Today I'm going to talk about...", "hoy voy a hablar de..."), ("Thank you for listening", "gracias por escuchar")],
    [
        ("Elegir el mejor resumen", ADULT + "«Rita finds a lost kitten in the park. She gives it water and takes it home. Her mom helps her put up a sign. The next day, the owner calls.» (kitten = gatito, owner = dueño, sign = letrero, calls = llama). ¿Cuál es el mejor resumen? a) Rita encuentra un gatito perdido y su dueño lo recupera. b) Rita va al parque con su mamá.", ["El resumen debe tener la idea principal.", "La idea es el gatito perdido y su dueño.", "La opción a) la tiene."], "a)"),
        ("Ordenar un resumen", "Ordena las ideas: A) El dueño llama. B) Rita encuentra un gatito. C) Rita pone un letrero.", ["Primero lo encuentra.", "Luego pone un letrero.", "Al final el dueño llama."], "B, C, A"),
    ],
    [
        ("Incluir todos los detalles en el resumen.", "Se pierde la idea principal.", "Elige solo los hechos clave."),
        ("Mezclar tu opinión con el resumen.", "El resumen debe contar lo que pasa y no lo que opinas.", "Pon tu opinión en otra frase aparte."),
    ],
    [
        ("¿Qué incluye un resumen? a) la idea principal y hechos clave b) todos los detalles", "a)", "Un resumen es breve."),
        ("¿Con qué frase empiezas una presentación oral? a) Today I'm going to talk about my pet. b) Goodbye.", "a)", "Es una forma común de empezar."),
        ("¿Cómo termina una presentación oral? a) Thank you for listening. b) Today I'm going to talk about...", "a)", "Se agradece a quien escucha."),
    ],
    [
        ("Un resumen del texto de Rita tiene tres frases. ¿Cuál no debe estar? a) Rita encuentra un gatito. b) A mí me gusta mucho el parque. c) El dueño llama.", "b)", "Es una opinión personal."),
        ("En una dramatización del texto de Rita, ¿cuántos personajes mínimos necesitas: Rita, su mamá y el dueño?", "3", "Los personajes nombrados son Rita, su mamá y el dueño."),
        ("¿Qué debe hacer un actor en una dramatización? a) decir sus líneas con gestos b) mirar al suelo", "a)", "Los gestos ayudan a entender."),
    ],
    [
        ("Lee: «Nico loses his lunch box at the park. He asks a woman for help. She sees it near a bench.» (lunch box = lonchera, woman = mujer, bench = banca). Elige el mejor resumen de una frase: a) Nico pierde su lonchera y una mujer lo ayuda a encontrarla. b) Nico come en un parque con una mujer.", "a)", "La opción a) tiene el problema y la solución."),
        ("En una dramatización necesitas ayuda con una palabra. ¿Qué dices? a) Can you help me with this word? b) Thank you for listening.", "a)", "Es una forma de pedir ayuda."),
        arith("Tu presentación tiene 2 minutos de inicio, 3 de desarrollo y 1 de cierre. ¿Cuántos minutos dura en total?", "2+3+1", "Se suman los minutos de cada parte."),
    ],
    [
        ("Un compañero resume así: «Rita va al parque, ve un árbol, toma agua, ve una nube...». ¿Qué le falta?", "La idea principal", "El resumen no dice cuál es el hecho central."),
        ("Para presentar en tres partes, ¿qué parte va después del inicio? a) desarrollo b) cierre", "a) desarrollo", "El orden es inicio, desarrollo y cierre."),
    ],
    [
        ("Escribe el orden correcto de una presentación: A) Thank you for listening B) Today I'm going to talk about my school. C) There are twenty classrooms.", "B, C, A", "Inicio, desarrollo y cierre."),
        arith("La presentación de Ana dura 4 minutos y la de Luis dura 3 minutos. ¿Cuántos minutos duran las dos juntas?", "4+3", "Se suman los minutos de las dos presentaciones."),
    ],
    [(ADULT + "El profesor dice: «First, we meet at the library. Next, we choose a book. Finally, we read together.» (meet = nos juntamos, choose = elegimos). ¿Qué resumen es mejor? a) Se juntan, eligen un libro y leen juntos. b) Leen un libro de matemática.", "a)", "Resume los tres pasos.")],
    [
        ("¿Qué es un resumen?", "Un texto breve con la idea principal y los hechos clave", "Resumir es reducir a lo importante."),
        ("¿Qué significa «Thank you for listening»?", "Gracias por escuchar", "Cierra una presentación."),
        ("¿Qué es una dramatización?", "Una actuación con personajes y diálogo", "Se representa una historia."),
    ],
    task("Un adulto lee dos veces: «Nico loses his lunch box at the park. He asks a woman for help. She sees it near a bench. Nico says thank you and eats lunch.» (lunch box = lonchera, woman = mujer, bench = banca). Escribe un resumen de tres frases en español con first, next y finally. Después prepara una presentación oral de dos líneas empezando con Today I'm going to talk about...", "Primero Nico pierde su lonchera. Luego una mujer la ve cerca de una banca. Al final Nico agradece y almuerza.", ["tres frases en orden", "incluye la idea principal", "inicio de presentación correcto"], ["hoja con resumen", "nota del adulto"], ["incluir opiniones", "no seguir el orden"], "Reconoce el resumen breve y repite con él la presentación en voz alta."),
    "Pide a un adulto que lea un texto corto y cuéntalo en dos frases con first y finally.",
    "Escribe una presentación de tres líneas sobre tu comida favorita, con inicio, desarrollo y cierre.",
)
