"""Student material for 4.º básico Inglés (propuesta), EN04 OA 05 (reaccionar a lo escuchado de forma personal y creativa).

Las «escuchas» las lee un adulto en voz alta; el guion va en el enunciado. Las respuestas abiertas (dibujo, mímica,
dramatización, frases) quedan en la tarea final; los ejercicios cerrados comprueban el criterio de cada forma de respuesta.
"""
from __future__ import annotations

from student_content_en4_a import ADULT, E, lesson, task
from student_lessons import arith

OA5 = "EN04 OA 05"

LION = "«A lion is under a tree. Two birds are on the tree. The sun is hot.»"
KIT = "«Lia: Look! A kitten! Tom: Is it lost? Lia: Yes. It is small and scared. Tom: Let's find its home. Lia: Okay!»"

# ---------------------------------------------------------------- clase 1
lesson(
    OA5, 1,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja, lápices de colores o lápiz grafito.",
    "Aprenderé a responder a lo que escucho con un dibujo que incluya lo que dijo el texto y una palabra en inglés. Sirve para mostrar lo que entendí y lo que siento.",
    ["Sé nombrar colores, animales y lugares en inglés.", "Sé usar under, on y next to."],
    [
        "Un dibujo de respuesta (supported response) muestra lo que entendiste de un texto oral. Debe incluir los elementos que el texto menciona: personas, animales, objetos, colores, números y lugares. Si el texto dice que un león está under a tree, dibujas el león debajo del árbol.",
        "Después puedes agregar una palabra o una frase corta en inglés debajo del dibujo, como lion o tree. Eso muestra que sabes cómo se llama cada cosa. También puedes mostrar tu opinión con un símbolo, como una cara contenta, y escribir I like it.",
        "Antes de dibujar escucha dos veces. Anota las palabras clave y comprueba que tu dibujo las incluya todas. No agregues cosas que el texto no dice si cambian lo que se entiende. Puedes agregar detalles propios, pero solo cuando no contradicen el texto.",
    ],
    [("drawing", "dibujo"), ("label", "etiqueta: palabra escrita junto a un dibujo"), ("lion", "león"), ("tree", "árbol"), ("sun", "sol"), ("kite", "volantín"), ("sky", "cielo")],
    [
        ("Un dibujo que coincide", ADULT + LION + " (lion = león, tree = árbol, hot = caluroso). ¿Qué dibujo coincide? a) Un león debajo de un árbol con dos pájaros sobre el árbol b) Un león sobre el árbol con tres pájaros.", ["Busco under a tree: el león está debajo.", "Busco two birds: dos pájaros.", "El dibujo a coincide."], "a"),
        ("Una etiqueta", "En ese dibujo, ¿qué palabra en inglés escribes bajo el animal grande: lion o tree?", ["El animal grande es el león.", "Lion significa león.", "Escribo lion."], "lion"),
    ],
    [
        ("Dibujar algo distinto de lo que dijo el texto, como el león sobre el árbol.", "No se escuchó la palabra de lugar.", "Revisa under, on o next to antes de dibujar."),
        ("Dibujar sin escribir ninguna palabra en inglés.", "El dibujo no muestra el vocabulario aprendido.", "Agrega una etiqueta, como lion o tree."),
    ],
    [
        (ADULT + LION + " ¿Cuántos pájaros dibujas?", "2", "Two birds son dos pájaros."),
        (ADULT + LION + " ¿Dónde dibujas al león?", "Debajo del árbol", "Under a tree significa debajo de un árbol."),
        ("Bajo el árbol de tu dibujo, ¿qué palabra escribes: tree o sun?", "tree", "Tree significa árbol y sun significa sol."),
    ],
    [
        ("¿Por qué se agregan palabras en inglés a un dibujo de respuesta?", "Para mostrar que sé cómo se llama cada cosa", "La etiqueta muestra el vocabulario que entendí."),
        ("Quieres mostrar que el día es caluroso. ¿Qué agregas: un sol o la luna?", "Un sol", "The sun is hot habla del sol."),
        ("¿Qué debe incluir un dibujo de respuesta: elementos del texto o cosas sin relación?", "Elementos del texto", "El dibujo muestra lo que entendí."),
    ],
    [
        (ADULT + "«Mia has a red ball and a blue kite. The kite is in the sky.» (kite = volantín, sky = cielo). ¿De qué color dibujas la pelota?", "Roja", "A red ball significa una pelota roja."),
        (ADULT + "«Mia has a red ball and a blue kite. The kite is in the sky.» ¿Dónde dibujas el volantín?", "En el cielo", "In the sky significa en el cielo."),
        (ADULT + "«Mia has a red ball and a blue kite. The kite is in the sky.» ¿Qué dos objetos dibujas y de qué color es cada uno?", "Una pelota roja y un volantín azul", "El texto dice a red ball y a blue kite."),
    ],
    [
        ("Pedro dibujó el león sobre el árbol. ¿Coincide con el texto «A lion is under a tree»?", "No; el león debe estar debajo del árbol", "Under significa debajo de."),
        ("Ana escucha «Tom is sad» y dibuja una cara con sonrisa. ¿Coincide con el texto?", "No; sad es triste y debe dibujar una cara triste", "El dibujo debe mostrar el sentimiento del texto."),
    ],
    [
        (ADULT + "«Eva paints three eggs: two are blue and one is yellow.» ¿Cuántos huevos azules y cuántos amarillos dibujas?", "2 azules y 1 amarillo", "Two are blue y one is yellow."),
        ("Elige la frase que muestra una respuesta personal: a) The lion is big. b) I like the lion.", "b", "I like the lion expresa lo que yo siento."),
    ],
    [(ADULT + "En la clase de arte escuchas: «Draw a sun in the sky.» (sky = cielo). ¿Dónde dibujas el sol?", "En el cielo", "In the sky significa en el cielo.")],
    [
        ("¿Qué es una etiqueta en un dibujo?", "Una palabra escrita junto al dibujo", "Dice el nombre de lo dibujado."),
        ("¿Cómo se dice «árbol» en inglés?", "tree", "Tree es árbol."),
        ("¿Se puede dibujar algo que contradice el texto?", "No", "El dibujo debe coincidir con lo que dijo el texto."),
    ],
    task("Un adulto lee dos veces: «A girl is in the park. She has a red kite. The kite is in the sky. Two birds are next to the kite. The girl is happy.» Dibuja la escena. Escribe tres etiquetas en inglés, como kite, sky y bird, y una frase con tu opinión, como I like the kite.", "Dibujo de una niña con un volantín rojo en el cielo y dos pájaros al lado, con etiquetas kite, sky, bird y la frase I like the kite.", ["dibuja todos los elementos del texto", "escribe tres etiquetas en inglés", "agrega una frase de opinión"], ["dibujo del estudiante", "nota del adulto"], ["poner el volantín en la mano en lugar del cielo", "no dibujar los dos pájaros"], "Reconoce lo que está bien dibujado y vuelve a escuchar con él la frase que cambió."),
    "Pide a un adulto que diga «sun, tree, lion» y dibuja cada uno con su etiqueta.",
    "Dibuja tu animal salvaje favorito y escribe debajo dos etiquetas y la frase I like it.",
)

# ---------------------------------------------------------------- clase 2
lesson(
    OA5, 2,
    "Un espacio libre y seguro para moverte; los textos escritos en cada ejercicio, que lee un adulto en voz alta.",
    "Aprenderé a responder con mímica y acciones a lo que escucho, para mostrar que entendí verbos y sentimientos. Sirve para participar sin necesidad de hablar mucho en inglés.",
    ["Sé que sleeping es durmiendo y eating es comiendo.", "Conozco los sentimientos happy, sad, tired y scared."],
    [
        "La mímica (mime) es mostrar una idea con el cuerpo, sin palabras. «Show me» significa «muéstrame». Si el adulto dice «Show me: eating», llevas la mano a la boca como si comieras. Para «sleeping» cierras los ojos y apoyas la cabeza en las manos.",
        "También puedes mostrar sentimientos. Para happy sonríes; para sad bajas los hombros y pones cara de pena; para tired bostezas; para scared abres los ojos y te encoges un poco. Otros verbos: flying (volando, mueves los brazos como alas), swimming (nadando) y reading (leyendo un libro imaginario).",
        "Antes de hacer la mímica, escucha bien el verbo. Una buena mímica se parece a lo que hace la persona de verdad y se entiende sin hablar. Hazla en un espacio libre, sin correr ni saltar sobre muebles, y de forma tranquila para cuidar tu cuerpo y el de tus compañeros.",
    ],
    [("mime", "mímica: mostrar con el cuerpo"), ("show me", "muéstrame"), ("flying", "volando"), ("swimming", "nadando"), ("reading", "leyendo"), ("scared", "con miedo"), ("tired", "cansado")],
    [
        ("Mímica de una acción", ADULT + "«Show me: eating.» ¿Qué mímica haces?", ["Escucho el verbo: eating.", "Comer se hace con la mano y la boca.", "Llevo la mano a la boca."], "Llevo la mano a la boca como si comiera"),
        ("Mímica de un sentimiento", ADULT + "«Show me: tired.» ¿Cuál mímica corresponde? a) Bostezar y bajar los hombros b) Saltar con los brazos arriba.", ["Tired es cansado.", "Una persona cansada bosteza.", "Elijo la a."], "a"),
    ],
    [
        ("Hacer la mímica de otro verbo, como comer cuando se dijo reading.", "No se escuchó el verbo.", "Escucha el verbo y recuerda su significado."),
        ("Hacer la mímica corriendo por la sala sin cuidar el espacio.", "Se pone en riesgo a otras personas.", "Hazla en el mismo lugar y con calma."),
    ],
    [
        ("¿Qué significa «Show me»?", "Muéstrame", "Se usa para pedir que muestres algo."),
        ("¿Qué es la mímica?", "Mostrar una idea con el cuerpo sin hablar", "No usa palabras."),
        (ADULT + "«Show me: sleeping.» ¿Qué haces?", "Cierro los ojos y apoyo la cabeza en las manos", "Eso muestra dormir."),
    ],
    [
        ("Alguien mueve los brazos como alas. ¿Qué acción muestra: flying o sleeping?", "flying", "Flying significa volando."),
        ("¿Qué mímica corresponde a «sad»: sonreír o poner cara de pena?", "Poner cara de pena", "Sad significa triste."),
        ("¿Para qué sirve responder con mímica?", "Para mostrar que entendí sin hablar", "La acción muestra la comprensión."),
    ],
    [
        (ADULT + "«The bird is flying. The fish is swimming.» (fish = pez). ¿Qué mímica haces con «swimming»?", "Muevo los brazos como si nadara", "Swimming significa nadando."),
        (ADULT + "«The dog is sleeping. The cat is running.» ¿Qué mímica haces en segundo lugar?", "Corro en el mismo lugar", "The cat is running es la segunda frase."),
        (ADULT + "«Show me: happy, sad, scared.» ¿Cuántos sentimientos tienes que mostrar?", "3", "Happy, sad y scared son tres sentimientos."),
    ],
    [
        ("Luis hizo como si comiera cuando el adulto dijo reading. ¿Qué debió hacer?", "Fingir que lee un libro", "Reading significa leyendo."),
        (ADULT + "«Show me: eating and then sleeping.» ¿Qué mímica haces primero?", "Comer", "And then indica que dormir viene después."),
    ],
    [
        arith(ADULT + "«Show me: jump three times and clap two times.» ¿Cuántos movimientos haces en total?", "3+2", "Se suman los saltos y las palmadas."),
        (ADULT + "«The monkey is eating a banana, then it is sleeping.» ¿Qué haces primero?", "Finjo comer", "Eating viene antes de then."),
    ],
    [(ADULT + "En un juego, tu compañero hace la mímica de beber agua. ¿Qué verbo en inglés dices: drinking o running?", "drinking", "Drinking significa bebiendo.")],
    [
        ("¿Qué significa «flying»?", "Volando", "Flying se muestra con los brazos como alas."),
        ("¿Qué significa «tired»?", "Cansado", "Tired se muestra bostezando."),
        ("¿Dónde haces la mímica?", "En un espacio libre y seguro", "Así cuidas tu cuerpo y el de tus compañeros."),
    ],
    task("En un espacio libre y seguro, un adulto dice dos veces: «Show me: eating. Show me: sleeping. Show me: scared. Show me: happy.» Haz la mímica de cada una, en orden. Después di el nombre en inglés de una mímica que hiciste y nombra el sentimiento que más te gustó mostrar.", "Cuatro mímicas en orden: comer, dormir, miedo y alegría; por ejemplo sleeping y happy.", ["hace las cuatro mímicas en orden", "cada mímica se entiende", "nombra en inglés una acción o sentimiento"], ["nota del adulto", "foto o video con permiso de la familia"], ["cambiar eating por sleeping", "hacer la mímica corriendo por la sala"], "Aplaude la mímica clara y repite con él la palabra del verbo que le costó."),
    "Pide a un adulto que diga «eating, sleeping, reading» y haz la mímica de cada una.",
    "Inventa una mímica de tres acciones y pide a alguien de tu casa que adivine cuáles son.",
)

# ---------------------------------------------------------------- clase 3
lesson(
    OA5, 3,
    "El guion de la escena escrito en el cuaderno; papel y lápiz para hacer objetos de cartulina; un espacio libre y seguro. Todo objeto es de papel o tela, sin partes duras ni puntiagudas.",
    "Aprenderé a dramatizar un momento clave de un texto: elijo qué personaje hago, qué digo y qué acciones muestro. Sirve para representar una historia con voz, gestos y movimiento.",
    ["Sé identificar quién habla en un diálogo.", "Sé hacer mímica de acciones y sentimientos."],
    [
        "Una dramatización (dramatization) es actuar una parte de una historia. El momento clave (key moment) es el momento en que los personajes toman una decisión importante o la historia cambia. Elegir este momento ayuda a que otros entiendan de qué trata la historia.",
        "Para dramatizar necesitas tres cosas. Primero, los personajes y sus líneas (lines), que son lo que cada uno dice. Segundo, las acciones: señalar, mirar o caminar despacio. Tercero, el sentimiento: scared (con miedo), happy (feliz) o sad (triste). La voz y la cara muestran ese sentimiento.",
        "Un personaje puede actuar sin hablar. En la historia de hoy el gatito (kitten) no dice nada: lo muestras con el cuerpo, encogido y tembloroso. Usa objetos seguros, como un peluche o un papel doblado. Nunca uses un animal real que no conoces.",
    ],
    [("dramatization", "dramatización: actuar una parte de una historia"), ("key moment", "momento clave"), ("line", "línea: lo que dice un personaje"), ("kitten", "gatito"), ("lost", "perdido"), ("scared", "con miedo"), ("let's find", "busquemos")],
    [
        ("Quién dice qué", ADULT + KIT + " (kitten = gatito, lost = perdido, scared = con miedo, let's find = busquemos). ¿Quién pregunta «Is it lost?»", ["Busco Is it lost?", "Antes de esa frase está el nombre Tom.", "Tom hace la pregunta."], "Tom"),
        ("El momento clave", "En la misma historia, ¿cuál es el momento clave: «Look! A kitten!» o «Let's find its home»?", ["El momento clave es cuando los personajes deciden algo.", "Tom propone buscar su casa.", "La historia cambia aquí."], "Let's find its home"),
    ],
    [
        ("Dramatizar toda la historia sin elegir un momento.", "Es difícil mostrar claramente la idea.", "Elige un momento clave y actúalo con claridad."),
        ("Usar un animal real desconocido como gatito.", "Puede ser inseguro para ti y para el animal.", "Usa un peluche o un papel doblado."),
    ],
    [
        (ADULT + KIT + " ¿Quién dice «Look! A kitten!»?", "Lia", "Es la primera línea de Lia."),
        (ADULT + KIT + " ¿Cómo está el gatito?", "Pequeño y con miedo", "Lia dice It is small and scared."),
        ("¿Qué significa «Let's find its home»?", "Busquemos su casa", "Let's find es busquemos."),
    ],
    [
        ("El gatito no habla. ¿Cómo muestras que está scared?", "Con el cuerpo, encogido y temblando suavemente", "Se actúa con gestos, no con palabras."),
        ("Lee la escena: «Lia: Look! A kitten! Tom: Is it lost? Lia: Yes. It is small and scared. Tom: Let's find its home. Lia: Okay!» ¿Cuántos personajes necesitas para actuarla, contando el gatito?", "3", "Lia, Tom y el gatito."),
        ("¿Qué es un momento clave?", "El momento en que los personajes toman una decisión o la historia cambia", "Resume lo importante de la historia."),
    ],
    [
        (ADULT + KIT + " ¿Qué dice Tom en el momento clave?", "Let's find its home", "Es su decisión."),
        ("Cuando Lia dice «Look!», ¿qué acción haces para mostrar la línea?", "Señalo con el dedo hacia el gatito", "Look significa mira."),
        ("Lee la escena: «Lia: Look! A kitten! Tom: Is it lost? Lia: Yes. It is small and scared. Tom: Let's find its home. Lia: Okay!» Ordénala: A) Tom pregunta si está perdido. B) Lia ve un gatito. C) Deciden buscar su casa.", "B, A, C", "Primero ve, luego pregunta y al final deciden."),
    ],
    [
        ("Pedro quiere usar algo seguro para el gatito. ¿Cuál elige: a) un peluche o un papel doblado b) un animal que no conoce?", "a", "Un objeto seguro no hace daño a nadie."),
        ("Ana dice que el gatito no puede aparecer porque no habla. ¿Tiene razón?", "No; puede actuar con el cuerpo", "Un personaje puede actuar sin decir nada."),
    ],
    [
        ("Lee la escena: «Lia: Look! A kitten! Tom: Is it lost? Lia: Yes. It is small and scared. Tom: Let's find its home. Lia: Okay!» Lia dice 3 líneas y Tom dice 2. ¿Cuántas líneas hay en total?", "5", "Se suman las líneas de Lia y de Tom."),
        ("¿Qué debes cuidar al actuar el momento clave: la voz y los gestos o solo las palabras?", "La voz, los gestos y las palabras", "Los gestos y la voz muestran el sentimiento."),
    ],
    [(ADULT + "En clase, un grupo actúa el momento clave y dice: «Let's find its home.» (home = casa). ¿Qué decisión toman?", "Buscar la casa del gatito", "Let's find its home significa busquemos su casa.")],
    [
        ("¿Qué es una línea en una dramatización?", "Lo que dice un personaje", "Es cada frase de un personaje."),
        ("¿Cómo se dice «gatito» en inglés?", "kitten", "Kitten es gatito."),
        ("¿Qué objeto usas para el gatito?", "Un peluche o un papel doblado", "Es un objeto seguro para actuar."),
    ],
    task("Con otra persona de tu casa, actúen dos veces este momento clave en un espacio seguro: «Lia: Look! A kitten! Tom: Is it lost? Lia: Yes. It is small and scared. Tom: Let's find its home. Lia: Okay!» Uno hace de Lia y el otro de Tom. Usen un peluche o un papel doblado como gatito. Al final digan en inglés qué personaje hizo cada uno.", "Actuación de la escena con voz clara, gestos y un objeto seguro; cada uno dice «I am Lia» o «I am Tom».", ["dice las líneas en orden", "usa voz y gestos para mostrar el sentimiento", "dice qué personaje hizo"], ["nota del adulto", "foto o video con permiso de la familia"], ["leer sin gestos", "usar un animal real"], "Aplaude la voz clara y repite con él la línea que se olvidó."),
    "Pide a un adulto que lea «Look! A kitten!» y señala con el dedo como lo haría Lia.",
    "Inventa un final de dos líneas para la historia, por ejemplo «Lia: Here is its home! Tom: Hooray!», y actúalo con alguien.",
)

# ---------------------------------------------------------------- clase 4
lesson(
    OA5, 4,
    "Las frases escritas en cada ejercicio, que lee un adulto en voz alta; lápiz y papel.",
    "Aprenderé a decir qué me gusta o qué prefiero y a dar una razón con because. Sirve para expresar mis opiniones en inglés y entender las de otras personas.",
    ["Sé decir I like apples.", "Conozco adjetivos como big, small, red y tall."],
    [
        "Una preferencia (preference) dice lo que te gusta más. Se dice «I like...» (me gusta...) o «My favorite... is...» (mi... favorito es...). Una opinión (opinion) dice lo que piensas. Dos personas pueden tener opiniones distintas y las dos pueden ser válidas.",
        "Para dar una razón se usa because (porque). La estructura es «I like + algo + because + razón». Por ejemplo: «I like giraffes because they are tall» (me gustan las jirafas porque son altas) o «I like apples because they are red» (me gustan las manzanas porque son rojas).",
        "Una buena razón explica la preferencia con una característica: un color, un tamaño o una cualidad como funny (gracioso) o yummy (rico). No basta con repetir lo mismo. «I like pizza because pizza» no tiene una razón. Escucha qué le gusta a cada persona y por qué.",
    ],
    [("preference", "preferencia: lo que me gusta más"), ("opinion", "opinión: lo que pienso"), ("because", "porque"), ("my favorite", "mi favorito"), ("tall", "alto"), ("funny", "gracioso"), ("yummy", "rico")],
    [
        ("Preferencia y razón", ADULT + "«I like apples because they are red.» (apples = manzanas). ¿Qué razón da la persona?", ["Busco because.", "Después de because oigo they are red.", "La razón es el color."], "Son rojas"),
        ("Completar una oración", "Completa: «I like giraffes ___ they are tall.» Elige: because o but.", ["Necesito la palabra que une la preferencia con la razón.", "Because significa porque.", "Elijo because."], "because"),
    ],
    [
        ("Decir una preferencia sin una razón.", "La opinión no queda explicada.", "Agrega because y una característica."),
        ("Pensar que una opinión distinta es un error.", "Cada persona puede pensar diferente.", "Acepta que dos opiniones distintas pueden ser válidas."),
    ],
    [
        ("¿Qué significa «because»?", "Porque", "Because une una preferencia con su razón."),
        (ADULT + "«I like apples because they are red.» ¿Qué le gusta a la persona?", "Las manzanas", "Apples son manzanas."),
        (ADULT + "«I like giraffes because they are tall.» (tall = alto). ¿Cuál es la razón?", "Son altas", "They are tall significa son altas."),
    ],
    [
        ("¿Cuál oración tiene una preferencia y una razón? a) I like bananas. b) I like bananas because they are yellow.", "b", "La b tiene because y una razón."),
        ("¿Qué significa «My favorite animal is the zebra»?", "Mi animal favorito es la cebra", "My favorite es mi favorito."),
        ("¿Pueden ser válidas dos opiniones distintas?", "Sí", "Cada persona puede pensar diferente."),
    ],
    [
        ("Completa: «I like the zoo because the monkeys are ___.» Elige: funny, triangle o under.", "funny", "Funny significa gracioso y es una razón posible."),
        ("Ordena las palabras: because / I like / tall / they are / giraffes", "I like giraffes because they are tall", "La estructura es I like + algo + because + razón."),
        (ADULT + "«I like rice because it is white. I like apples because they are red.» ¿Cuántas razones se dan?", "2", "Una razón por cada preferencia."),
    ],
    [
        ("Ana dice «I like pizza because pizza». ¿Qué le falta?", "Una razón", "Repite lo mismo y no explica nada."),
        ("Ben dice «I like soup because it is hot». Leo dice «I don't like soup». ¿Pueden ser válidas las dos opiniones? (hot = caliente)", "Sí, cada uno piensa distinto", "Una opinión no tiene que coincidir con otra."),
    ],
    [
        ("Elige la mejor razón para «I like Easter because...»: a) we make cards b) the table is under the bed.", "a", "Hacer tarjetas es una característica de la celebración."),
        ("Completa con tu opinión: «I like ___ because ___.» Elige la oración con razón: a) I like dogs because they are friendly. b) I like dogs. (friendly = amistoso)", "a", "La a tiene because y una razón."),
    ],
    [(ADULT + "En el recreo, una niña dice: «I like the park because there are trees.» (trees = árboles). ¿Por qué le gusta el parque?", "Porque hay árboles", "There are trees es la razón.")],
    [
        ("¿Cómo se dice «mi favorito» en inglés?", "My favorite", "My favorite es mi favorito."),
        ("¿Qué significa «opinion»?", "Lo que pienso", "Una opinión es una idea personal."),
        ("¿Qué palabra une una preferencia con su razón?", "because", "Because es porque."),
    ],
    task("Elige una de estas comidas: apples, rice o bread. Di una oración en voz alta y escríbela: «I like ___ because ___.» Usa una razón como red, white, yummy o good. Luego pregunta a una persona de tu casa qué le gusta a ella y por qué, y anota su oración.", "I like apples because they are red.", ["escribe I like + comida", "agrega because y una razón", "anota la oración de la otra persona"], ["hoja con ambas oraciones", "nota del adulto"], ["escribir solo I like apples", "poner una razón sin sentido"], "Reconoce la razón y vuelve a leer con él la estructura I like... because..."),
    "Pide a un adulto que diga «I like red» y responde con otra preferencia propia.",
    "Escribe dos oraciones con I like... because... sobre animales salvajes.",
)

# ---------------------------------------------------------------- clase 5
lesson(
    OA5, 5,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y papel.",
    "Aprenderé a conectar una historia con una experiencia imaginada y segura, usando I imagine, I feel e I would. Sirve para relacionar lo que escucho con mis ideas sin contar datos privados.",
    ["Sé decir cómo se sienten los personajes.", "Sé dar una preferencia con una razón."],
    [
        "Una conexión (connection) une lo que escuchas con tus ideas o con algo que imaginas. Una experiencia ficticia (fictional) es inventada, no real. Para conectar se usan I imagine (imagino), I feel (siento) e I would (yo haría). Por ejemplo: «I imagine I find a kitten» (imagino que encuentro un gatito).",
        "En la historia de hoy, Lia encuentra un gatito perdido. Está feliz, pero el gatito está asustado. Lia llama a un adulto para pedir ayuda: «I would call an adult» (llamaría a un adulto). Es una conexión segura porque pide ayuda y no toca un animal desconocido sin permiso.",
        "Al conectar, cuida tu privacidad. No digas tu dirección, tu teléfono ni nombres completos de otras personas. Una conexión segura usa una situación inventada y un sentimiento. Puedes decir «I imagine a small rabbit in a garden» sin dar ningún dato personal.",
    ],
    [("connection", "conexión: unir el texto con mis ideas"), ("fictional", "ficticio: inventado"), ("I imagine", "yo imagino"), ("I feel", "yo siento"), ("I would", "yo haría"), ("call an adult", "llamar a un adulto"), ("safe", "seguro")],
    [
        ("Conexión segura", "Lia encuentra un gatito perdido. ¿Qué conexión es segura? a) I imagine I call an adult. b) I imagine I touch an unknown animal alone.", ["Busco la que pide ayuda a un adulto.", "La b toca un animal desconocido sin ayuda.", "La a es segura."], "a"),
        ("Qué hace Lia", ADULT + "«Lia finds a kitten. She is happy. The kitten is scared. She calls an adult.» (calls = llama). ¿Qué hace Lia para ayudar?", ["Busco calls.", "Después oigo an adult.", "Lia llama a un adulto."], "Llama a un adulto"),
    ],
    [
        ("Contar tu dirección o teléfono como parte de la conexión.", "Son datos privados.", "Usa una situación imaginada, sin datos personales."),
        ("Imaginar que haces algo inseguro, como tocar un animal desconocido sin ayuda.", "Puede ser peligroso.", "Imagina que pides ayuda a un adulto."),
    ],
    [
        (ADULT + "«Lia finds a kitten. She is happy.» ¿Cómo se siente Lia?", "Feliz", "Happy significa feliz."),
        ("¿Qué significa «I imagine»?", "Yo imagino", "I imagine habla de algo inventado."),
        ("¿Qué significa «fictional»?", "Ficticio, inventado", "Una experiencia ficticia no ocurrió realmente."),
    ],
    [
        ("¿Qué significa «I would call an adult»?", "Yo llamaría a un adulto", "I would es yo haría."),
        ("¿Qué dos cosas une una conexión personal?", "El texto y mis ideas o experiencias imaginadas", "Conectar es unir ambas cosas."),
        ("Lee: «Lia finds a kitten. She is happy. The kitten is scared. She calls an adult.» ¿Qué sentimiento tiene el gatito?", "Miedo", "The kitten is scared."),
    ],
    [
        ("Lee: «Lia finds a kitten. She is happy.» Lia está feliz. Imagino que estoy feliz cuando juego con una pelota. ¿Qué sentimiento comparten?", "Felicidad", "Los dos se sienten happy."),
        ("¿Qué frase conecta con la historia? a) I like pizza. b) I imagine a kitten in my school yard.", "b", "La b une la historia con una situación imaginada."),
        ("Ordena la conexión: A) I would call an adult. B) I imagine I find a kitten. C) I feel happy.", "B, C, A", "Primero imagino, luego siento y al final digo qué haría."),
    ],
    [
        ("Pedro dice «I would take the kitten home without telling anyone». ¿Es una conexión segura?", "No; debe avisar a un adulto", "Avisar a un adulto es la forma segura."),
        ("¿Por qué es mejor llamar a un adulto que actuar solo?", "Porque un adulto puede ayudar de forma segura", "Un adulto sabe qué hacer."),
    ],
    [
        ("¿Cuál conexión protege tu privacidad? a) I imagine a small rabbit in a garden. b) Voy a escribir mi dirección y mi teléfono.", "a", "La a no entrega datos personales."),
        ("Marta escribe: «I imagine I find a puppy. I feel happy. I would call an adult.» ¿Cuántas ideas distintas tiene su conexión?", "3", "Imagina, siente y dice qué haría."),
    ],
    [(ADULT + "En clase, un niño dice: «I imagine I find a bird. I would call an adult.» ¿Qué haría el niño?", "Llamaría a un adulto", "I would call an adult significa llamaría a un adulto.")],
    [
        ("¿Cómo se dice «llamaría a un adulto» en inglés?", "I would call an adult", "I would es yo haría."),
        ("¿Una conexión puede contar datos privados?", "No", "Hay que cuidar la privacidad."),
        ("¿Qué palabra significa «yo siento»?", "I feel", "I feel habla de un sentimiento."),
    ],
    task("Un adulto lee dos veces: «Ben finds a small bird in the yard. The bird is scared. Ben is worried.» (worried = preocupado, bird = pájaro). Escribe tres frases de conexión usando I imagine, I feel e I would. No uses datos privados y propone una acción segura.", "I imagine I find a bird. I feel worried. I would call an adult.", ["usa I imagine, I feel e I would", "la acción propuesta es segura", "no entrega datos privados"], ["hoja con tres frases", "nota del adulto"], ["proponer tocar el pájaro sin ayuda", "escribir una dirección"], "Reconoce la conexión y vuelve a leer con él la acción segura."),
    "Pide a un adulto que diga «I imagine, I feel, I would» y completa una frase con cada una.",
    "Escribe una conexión de tres frases con otra historia que conozcas, sin contar datos privados.",
)
