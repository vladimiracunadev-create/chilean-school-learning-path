"""Student material for 1.º básico Inglés, EN01 OA 07 (leer textos sobre temas y funciones conocidas).

Los textos están escritos completos en cada ejercicio; un adulto puede leerlos en voz alta si hace falta.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA7 = "EN01 OA 07"


register(
    OA7, 1,
    materials="Las instrucciones y presentaciones escritas en cada ejercicio; lápiz y papel.",
    use="Aprenderé a leer instrucciones y presentaciones simples en inglés, como «Open your book» o «My name is Ana». Sirve para saber qué hacer y quién es una persona.",
    prior=["Sé qué significan stand up, sit down y open.", "Sé decir hello y mi nombre."],
    explain=[
        "Una instrucción empieza con un verbo de acción: Open your book (abre tu libro), Close the door (cierra la puerta), Write your name (escribe tu nombre). Al leerla, primero reconoce la acción y luego lo que debes tocar o usar.",
        "Una presentación dice quién eres. Se usan frases como «My name is Ana» (me llamo Ana), «I'm seven» (tengo siete años) y «I'm from Chile» (soy de Chile). Con ellas puedes leer cómo se presenta alguien más.",
        "Si no conoces una palabra, mira las que sí conoces. En «Write your name on the page», conoces write, your name y page; con eso entiendes qué hacer. Después haz lo que dice para comprobar.",
    ],
    vocab=[("open / close", "abrir / cerrar"), ("write", "escribir"), ("my name is...", "me llamo..."), ("I'm seven", "tengo siete años"), ("your", "tu"), ("page", "página")],
    worked=[
        {"title": "Leer una instrucción", "problem": "Lee: «Write your name on the page.» ¿Qué haces?", "steps": ["Write es escribir.", "Your name es tu nombre.", "On the page es en la página."], "answer": "Escribo mi nombre en la página"},
        {"title": "Leer una presentación", "problem": "Lee: «Hello! My name is Leo. I'm seven.» ¿Cómo se llama y cuántos años tiene?", "steps": ["My name is Leo: se llama Leo.", "I'm seven: tiene siete años."], "answer": "Leo; siete años"},
    ],
    mistakes=[
        {"wrong": "Leer «Close» y abrir el libro.", "why": "Se confunden open y close.", "fix": "Close es cerrar y open es abrir."},
        {"wrong": "Entender «I'm seven» como un nombre.", "why": "No se reconoce el patrón.", "fix": "Después de «I'm» puede venir una edad, un lugar o una emoción."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «Open your book.» ¿Qué haces?", "Abro mi libro", "Open es abrir."),
            ex("Lee: «My name is Ana.» ¿Cómo se llama la persona?", "Ana", "My name is indica el nombre."),
            ex("Lee: «Close the door.» ¿Qué haces?", "Cierro la puerta", "Close es cerrar y door es puerta."),
        ],
        "understand": [
            ex("¿Con qué empieza casi siempre una instrucción?", "Con un verbo de acción", "Dice qué hacer."),
            ex("¿Qué significa «My name is...»?", "Me llamo...", "Se usa para presentarse."),
            ex("¿Qué significa «I'm seven»?", "Tengo siete años", "Seven es siete."),
        ],
        "apply": [
            ex("Lee: «Hello! I'm Tom. I'm six.» ¿Cuántos años tiene Tom?", "Seis", "Six es seis."),
            ex("Lee: «Write your name. Draw a star.» ¿Qué haces primero?", "Escribo mi nombre", "Write your name va primero."),
            ex("Lee: «Look at the board.» ¿Qué miras?", "La pizarra", "Board es pizarra."),
        ],
        "reason": [
            ex("Un niño leyó «Close your book» y abrió su libro. ¿Qué palabra confundió?", "Close con open", "Close es cerrar."),
            ex("¿Por qué conviene hacer lo que dice una instrucción?", "Para comprobar que la entendí", "La acción muestra comprensión."),
        ],
        "challenge": [
            ex("Ordena las instrucciones como si fueras a escribir: (a) Write your name. (b) Open your notebook. (c) Close your notebook.", "b, a, c", "Primero se abre, luego se escribe y al final se cierra."),
            ex("Escribe en inglés una presentación con tu nombre inventado, por ejemplo Pedro.", "Hello! My name is Pedro", "My name is más el nombre."),
        ],
    },
    context=[ex("En la puerta de la sala hay un cartel: «Open the door, please.» ¿Qué pide el cartel?", "Que abras la puerta", "Open the door es abre la puerta.")],
    selfcheck=[
        ex("¿Qué significa «write»?", "escribir", "Write es escribir."),
        ex("Lee: «I'm eight.» ¿Qué dice?", "Que tiene ocho años", "Eight es ocho."),
        ex("¿Qué haces si no conoces una palabra de la instrucción?", "Uso las palabras que conozco", "El resto ayuda a entender."),
    ],
    open_task=task("Lee estas tres instrucciones: «1. Open your notebook. 2. Write your name. 3. Draw a blue star.» Hazlas en orden. Luego escribe tu presentación completando: «Hello! My name is ___. I'm ___.» con tu nombre y tu edad.", "Cuaderno abierto, nombre escrito, estrella azul dibujada. «Hello! My name is Pedro. I'm seven.»", ["hace las tres instrucciones en orden", "completa su presentación", "usa My name is e I'm"], ["cuaderno con la actividad"], ["dibujar una estrella roja", "escribir I'm seven sin nombre"], "Lee con él cada instrucción y revisa en el cuaderno que coincida."),
    reinforce="Lee en voz alta «Open your book» y hazlo.",
    extend="Escribe tres instrucciones de la sala de clases en inglés.",
)

register(
    OA7, 2,
    materials="Los textos con habilidades, emociones y posesión escritos en cada ejercicio; lápiz.",
    use="Aprenderé a leer frases que dicen qué puede hacer alguien, cómo se siente y qué tiene. Sirve para conocer a otros por escrito.",
    prior=["Sé qué significan can, I'm y have.", "Sé leer palabras como happy y dog."],
    explain=[
        "Al leer, encontrarás tres tipos de frases muy comunes. Con «can» se dice lo que alguien sabe hacer: She can sing. Con «I'm» o «He is» se dice cómo está: I'm happy. Con «have» o «has» se dice lo que tiene: He has a dog.",
        "Reconócelas por su palabra clave. Si ves can, piensa en una habilidad. Si ves happy, sad o tired, piensa en una emoción. Si ves have o has, piensa en algo que alguien posee.",
        "Una carta sencilla puede juntarlas: «Hello! I'm Mia. I can run. I have a cat. I'm happy.» Léela frase por frase y pregúntate de cada una: ¿qué puede hacer?, ¿cómo está?, ¿qué tiene?",
    ],
    vocab=[("can", "puede, sabe hacer"), ("has", "tiene"), ("happy", "contento"), ("sad", "triste"), ("tired", "cansado"), ("cat", "gato")],
    worked=[
        {"title": "Tres tipos de frases", "problem": "Lee: «I'm Mia. I can run. I have a cat. I'm happy.» ¿Qué puede hacer Mia?", "steps": ["Busco can.", "I can run: puede correr."], "answer": "Correr"},
        {"title": "Qué tiene", "problem": "Con el mismo texto, ¿qué tiene Mia?", "steps": ["Busco have.", "I have a cat: tiene un gato."], "answer": "Un gato"},
    ],
    mistakes=[
        {"wrong": "Confundir «I have» con «I can».", "why": "Las dos empiezan con I.", "fix": "Mira la segunda palabra: have es tener y can es poder."},
        {"wrong": "Leer «I'm sad» como un nombre.", "why": "No se reconoce la emoción.", "fix": "Después de I'm puede venir una emoción como sad."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «She can sing.» ¿Qué sabe hacer ella?", "Cantar", "Sing es cantar."),
            ex("Lee: «He has a dog.» ¿Qué tiene él?", "Un perro", "Has a dog es tiene un perro."),
            ex("Lee: «I'm tired.» ¿Cómo está la persona?", "Cansada", "Tired es cansado."),
        ],
        "understand": [
            ex("¿Qué indica la palabra «can» en una frase?", "Lo que alguien puede o sabe hacer", "Muestra lo que alguien puede hacer."),
            ex("¿Cuándo se usa «has»?", "Con he, she o un nombre para decir lo que alguien tiene", "Es la forma de have."),
            ex("¿Qué palabras muestran una emoción?", "Happy, sad y tired", "Describen cómo se siente alguien."),
        ],
        "apply": [
            ex("Lee: «Leo can swim. Leo has a boat. Leo is happy.» ¿Qué sabe hacer Leo?", "Nadar", "Swim es nadar."),
            ex("Lee: «Ana has a new ball. She is happy.» ¿Cómo está Ana?", "Contenta", "Happy es contento."),
            ex("Lee: «Pia has two cats. They can jump.» ¿Qué pueden hacer los gatos?", "Saltar", "Jump es saltar."),
        ],
        "reason": [
            ex("Un niño leyó «I have a dog» y dijo «puedo un perro». ¿Qué confundió?", "Have con can", "Have es tener."),
            ex("En «Tom is tired. He can't run.», ¿qué relación hay entre estar cansado y no poder correr?", "Está cansado y por eso no puede correr", "La emoción explica la capacidad."),
        ],
        "challenge": [
            ex("Lee: «I'm Mia. I can draw. I have a red bag. I'm happy.» Escribe cuántas frases hay de cada tipo: habilidad, tener y emoción.", "1 de cada tipo", "Hay una con can, una con have y una con happy."),
            ex("Escribe en inglés una frase que diga que una niña tiene un gato.", "She has a cat", "She has más cat."),
        ],
    },
    context=[ex("En una carta de una amiga lees: «I'm Lia. I can dance. I have a new doll.» ¿Qué tiene Lía?", "Una muñeca nueva", "Doll es muñeca.")],
    selfcheck=[
        ex("¿Qué significa «sad»?", "triste", "Es una emoción."),
        ex("Lee: «He can run.» ¿Qué hace él?", "Corre", "Run es correr."),
        ex("¿Qué palabra indica que alguien tiene algo?", "have o has", "Son las formas de tener."),
    ],
    open_task=task("Lee la carta de Leo: «Hello! I'm Leo. I can swim. I have a green kite. I'm happy.» Responde por escrito: (1) ¿Qué puede hacer? (2) ¿Qué tiene? (3) ¿Cómo está? Luego escribe tu propia carta de tres frases con I can, I have e I'm.", "(1) Nadar. (2) Una cometa verde. (3) Contento. Mi carta: I can run. I have a ball. I'm happy.", ["tres respuestas correctas", "carta con las tres estructuras", "frases completas"], ["respuestas", "carta"], ["decir que Leo tiene una pelota", "carta sin I'm"], "Subraya con él can, have e I'm en la carta para ver cada tipo."),
    reinforce="Lee «I can run» y haz el movimiento.",
    extend="Escribe una carta de cuatro frases sobre una mascota inventada.",
)

register(
    OA7, 3,
    materials="Las descripciones escritas en cada ejercicio; lápices de colores.",
    use="Aprenderé a leer descripciones con números, colores y tamaños, como «three big red balls». Sirve para entender cuántos son y cómo son los objetos.",
    prior=["Sé los números del 1 al 10 en inglés.", "Sé los colores y big / small."],
    explain=[
        "Una descripción dice cuántos objetos hay y cómo son. En inglés el orden es: número, tamaño, color, objeto. Por ejemplo: three big red balls significa tres pelotas rojas grandes.",
        "Al leer, busca primero el objeto (balls) y luego mira las palabras antes: red es el color, big es el tamaño y three es la cantidad. Cuando hay más de uno, el objeto termina en s: one ball, two balls.",
        "Puedes dibujar lo que lees para comprobar. Si lees «two small blue fish», dibujas dos peces pequeños azules. Si tu dibujo coincide con cada palabra, entendiste la descripción.",
    ],
    vocab=[("one, two, three...", "uno, dos, tres..."), ("big / small", "grande / pequeño"), ("red / blue / green", "rojo / azul / verde"), ("balls", "pelotas"), ("fish", "pez, peces"), ("how many?", "¿cuántos?")],
    worked=[
        {"title": "Leer una descripción", "problem": "Lee: «three big red balls». ¿Cuántas hay y cómo son?", "steps": ["Three: tres.", "Big: grandes.", "Red: rojas.", "Balls: pelotas."], "answer": "Tres pelotas rojas grandes"},
        {"title": "Comparar", "problem": "Lee: «two small blue fish» y «one big blue fish». ¿Cuántos peces hay en total?", "steps": ["Dos peces pequeños azules.", "Un pez grande azul.", "2 + 1 = 3."], "answer": "3 peces"},
    ],
    mistakes=[
        {"wrong": "Dibujar una pelota roja en lugar de tres.", "why": "Se salta el número.", "fix": "Lee el número antes que el objeto."},
        {"wrong": "Cambiar el orden: leer red three balls.", "why": "No se respeta el patrón.", "fix": "El orden es número, tamaño, color, objeto."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «two cats». ¿Cuántos gatos?", "2", "Two es dos."),
            ex("Lee: «a red ball». ¿De qué color es la pelota?", "Roja", "Red es rojo."),
            ex("Lee: «a big dog». ¿Cómo es el perro?", "Grande", "Big es grande."),
        ],
        "understand": [
            ex("En «three big red balls», ¿qué palabra es el número, cuál el tamaño y cuál el color?", "three es el número, big el tamaño y red el color", "Ese es el orden: número, tamaño, color y objeto."),
            ex("¿Qué indica la «s» al final de balls?", "Que hay más de una", "Es el plural."),
            ex("¿Qué significa «small»?", "pequeño", "Es lo contrario de big."),
        ],
        "apply": [
            ex("Lee: «four small green frogs». ¿Cuántas ranas hay y de qué color son?", "4 ranas verdes", "Four es cuatro y green es verde."),
            ex("Lee: «one big yellow sun». ¿Cómo es el sol?", "Grande y amarillo", "Big es grande y yellow es amarillo."),
            ex("Lee: «two blue pencils and three red pencils». ¿Cuántos lápices hay en total?", "5", "Dos más tres son cinco."),
        ],
        "reason": [
            ex("Un niño dibujó dos pelotas cuando el texto decía «three balls». ¿Qué número leyó mal?", "Three", "Three es tres."),
            ex("¿Por qué «a big dog» y «a small dog» son descripciones distintas?", "Porque cambia el tamaño", "Big y small son opuestos."),
        ],
        "challenge": [
            ex("Lee: «five small red flowers and two big yellow flowers». ¿Cuántas flores amarillas hay?", "2", "Two big yellow flowers."),
            ex("Escribe en inglés: tres gatos pequeños negros.", "three small black cats", "Número, tamaño, color, objeto."),
        ],
    },
    context=[ex("En una lista de compras de una tienda de útiles lees: «two blue pens, three red pencils and one big notebook». ¿Cuántos lápices rojos hay?", "3", "Three red pencils son tres lápices rojos.")],
    selfcheck=[
        ex("¿Qué significa «three»?", "tres", "Es el número 3."),
        ex("Lee: «a small cat». ¿Cómo es el gato?", "Pequeño", "Small es pequeño."),
        ex("¿Qué haces para comprobar una descripción?", "La dibujo", "El dibujo debe coincidir con cada palabra."),
    ],
    open_task=task("Lee esta descripción: «I have two big red apples, three small yellow bananas and one green pear.» Dibuja la fruta y escribe el número bajo cada grupo. Luego escribe tu propia descripción de tres objetos con número, tamaño y color.", "Dibujo: 2 manzanas rojas grandes, 3 plátanos amarillos pequeños, 1 pera verde; números 2, 3, 1. Mi descripción: I have two big blue balls.", ["cantidades correctas", "colores y tamaños correctos", "descripción propia con el orden correcto"], ["dibujo", "descripción escrita"], ["dibujar tres manzanas", "cambiar los colores"], "Contrasta cada grupo del dibujo con el texto, palabra por palabra."),
    reinforce="Lee «two red balls» y dibuja las dos pelotas.",
    extend="Escribe una descripción de cinco objetos de tu pieza con número, tamaño y color.",
)

register(
    OA7, 4,
    materials="Las preguntas y los textos escritos en cada ejercicio; lápiz.",
    use="Aprenderé a leer preguntas con Where, What y Who y sus respuestas. Sirve para encontrar información en un texto y responder.",
    prior=["Sé qué significan in, on y under.", "Sé leer palabras como cat, bag y book."],
    explain=[
        "Las preguntas con Where, What y Who piden información distinta. Where is the cat? (¿dónde está el gato?) pide un lugar. What is this? (¿qué es esto?) pide un nombre de objeto. Who is she? (¿quién es ella?) pide una persona.",
        "La respuesta repite parte de la pregunta: Where is the cat? It's on the chair. What is this? It's a book. Who is she? She is Ana. Fíjate en la primera palabra de la pregunta para saber qué buscar en el texto.",
        "Al leer una pregunta, primero decide qué buscas: un lugar, un objeto o una persona. Luego encuentra esa palabra en el texto y responde con ella. Si buscas un lugar, busca in, on, under o next to.",
    ],
    vocab=[("where?", "¿dónde?"), ("what?", "¿qué?"), ("who?", "¿quién?"), ("on / in / under", "sobre / dentro / debajo"), ("it's", "es / está"), ("chair", "silla")],
    worked=[
        {"title": "Pregunta de lugar", "problem": "Lee: «The cat is on the chair.» Pregunta: Where is the cat?", "steps": ["Where pide un lugar.", "Busco on the chair."], "answer": "On the chair (sobre la silla)"},
        {"title": "Pregunta de persona", "problem": "Lee: «This is Ana. She is my friend.» Pregunta: Who is she?", "steps": ["Who pide una persona.", "Busco el nombre: Ana."], "answer": "Ana"},
    ],
    mistakes=[
        {"wrong": "Responder un nombre a una pregunta con Where.", "why": "Se confunde Where con Who.", "fix": "Where pide un lugar."},
        {"wrong": "Responder sin buscar la palabra en el texto.", "why": "Se adivina.", "fix": "Busca in, on o under."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué pide la pregunta «Where is the ball?»", "Un lugar", "Where es dónde."),
            ex("¿Qué pide la pregunta «Who is she?»", "Una persona", "Who es quién."),
            ex("¿Qué pide la pregunta «What is this?»", "El nombre de un objeto", "What es qué."),
        ],
        "understand": [
            ex("¿Qué significa «Where is the book?»", "¿Dónde está el libro?", "Where es dónde."),
            ex("¿Qué palabras te ayudan a responder una pregunta con Where?", "In, on, under y next to", "Estas palabras indican el lugar."),
            ex("¿Qué haces primero al leer una pregunta?", "Decido qué tipo de dato busco", "Así encuentro la respuesta."),
        ],
        "apply": [
            ex("Lee: «The ball is under the table.» Pregunta: Where is the ball?", "Under the table", "Under es debajo."),
            ex("Lee: «This is a pencil.» Pregunta: What is this?", "A pencil", "Pencil es lápiz."),
            ex("Lee: «He is Tom. He is my brother.» Pregunta: Who is he?", "Tom", "El nombre es la respuesta."),
        ],
        "reason": [
            ex("Un niño respondió «Ana» a «Where is the cat?». ¿Qué error cometió?", "Respondió con una persona en lugar de un lugar", "Where pide un lugar."),
            ex("¿Por qué es útil la primera palabra de una pregunta?", "Porque dice qué tipo de dato debo buscar", "Cada una pide algo distinto."),
        ],
        "challenge": [
            ex("Lee: «The book is in the bag. The bag is next to the chair.» ¿Dónde está la mochila?", "Next to the chair", "Next to es al lado de."),
            ex("Escribe una pregunta en inglés para saber dónde está el gato.", "Where is the cat?", "Where pregunta por un lugar."),
        ],
    },
    context=[ex("En una nota en la cocina lees: «The apples are in the box. The box is on the table.» ¿Dónde está la caja?", "Sobre la mesa", "On the table es sobre la mesa.")],
    selfcheck=[
        ex("¿Cómo se dice «¿quién?» en inglés?", "who", "Who es quién."),
        ex("Lee: «The dog is in the garden.» ¿Dónde está el perro?", "En el jardín", "In the garden."),
        ex("¿Qué significa «What is this?»", "¿Qué es esto?", "What pide un nombre."),
    ],
    open_task=task("Lee este texto: «This is Lia. She is my sister. The bag is on the chair. The pencil is in the bag.» Responde: (1) Who is she? (2) Where is the bag? (3) Where is the pencil? Luego escribe una pregunta propia con Where sobre un objeto de tu pieza.", "(1) Lia, mi hermana. (2) On the chair. (3) In the bag. Pregunta: Where is my book?", ["tres respuestas correctas", "usa palabras de lugar", "una pregunta con Where"], ["respuestas", "pregunta"], ["responder un nombre a Where", "pregunta sin Where"], "Subraya con él Who, Where y las respuestas del texto."),
    reinforce="Lee «Where is the ball?» y señala un lugar de tu casa.",
    extend="Escribe tres preguntas con Where, What y Who sobre tu familia o tu sala de clases.",
)

register(
    OA7, 5,
    materials="Los textos con acciones escritos en cada ejercicio; lápiz y papel.",
    use="Aprenderé a leer frases que dicen lo que alguien está haciendo ahora, como «She is reading». Sirve para entender lo que pasa en un texto o una imagen.",
    prior=["Sé qué significan run, eat y read.", "Sé qué significa is y are."],
    explain=[
        "Las acciones que ocurren ahora se escriben con am, is o are y un verbo terminado en -ing: I am reading, He is eating, They are playing. El -ing te dice que la acción está pasando en este momento.",
        "Para entender quién lo hace, mira la palabra antes de is o are: She is reading (ella), The boys are playing (los niños). Para entender qué hace, mira la palabra con -ing: reading, eating, playing.",
        "Una pregunta común es «What is he doing?» (¿qué está haciendo él?). Se responde con He is y la acción. Lee el texto, busca la palabra con -ing y responde.",
    ],
    vocab=[("is / are", "está / están"), ("reading", "leyendo"), ("eating", "comiendo"), ("playing", "jugando"), ("sleeping", "durmiendo"), ("What is he doing?", "¿qué está haciendo él?")],
    worked=[
        {"title": "Qué hace ahora", "problem": "Lee: «Ana is reading a book.» ¿Qué hace Ana?", "steps": ["Busco la palabra con -ing.", "Reading es leyendo."], "answer": "Está leyendo un libro"},
        {"title": "Quiénes", "problem": "Lee: «The boys are playing football.» ¿Quiénes juegan?", "steps": ["Antes de are: the boys.", "Son los niños."], "answer": "Los niños"},
    ],
    mistakes=[
        {"wrong": "Leer «is reading» como «lee» siempre.", "why": "No se nota el -ing.", "fix": "El -ing indica que la acción pasa ahora."},
        {"wrong": "Confundir quién hace la acción.", "why": "Se salta la palabra antes de is.", "fix": "Lee quién va antes de is o are."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «He is eating.» ¿Qué hace él?", "Está comiendo", "Eating es comiendo."),
            ex("Lee: «She is sleeping.» ¿Qué hace ella?", "Está durmiendo", "Sleeping es durmiendo."),
            ex("Lee: «They are playing.» ¿Qué hacen ellos?", "Están jugando", "Playing es jugando."),
        ],
        "understand": [
            ex("¿Qué indica la terminación -ing?", "Que la acción ocurre ahora", "Es lo que pasa en este momento."),
            ex("¿Qué significa «What is he doing?»", "¿Qué está haciendo él?", "Pregunta por la acción actual."),
            ex("¿Qué palabra va con «they»: is o are?", "are", "They are es la forma correcta."),
        ],
        "apply": [
            ex("Lee: «Mia is drawing a flower.» ¿Qué dibuja Mía?", "Una flor", "Flower es flor."),
            ex("Lee: «Leo and Tom are running in the park.» ¿Dónde corren?", "En el parque", "In the park."),
            ex("Lee: «The cat is sleeping on the chair.» ¿Dónde duerme el gato?", "Sobre la silla", "On the chair."),
        ],
        "reason": [
            ex("Lee: «Ana is eating and Beto is reading.» ¿Cuál es la diferencia entre ellos?", "Ana come y Beto lee", "Cada uno hace una acción."),
            ex("Un niño leyó «She is sleeping» como «ella duerme siempre». ¿Qué pasó por alto?", "El -ing, que indica que ocurre ahora", "Is sleeping es está durmiendo."),
        ],
        "challenge": [
            ex("Lee: «Look! Pia is singing, Leo is jumping and Ana is drawing.» ¿Quién está saltando?", "Leo", "Leo is jumping."),
            ex("Escribe en inglés qué está haciendo un niño que come una manzana.", "He is eating an apple", "He is más eating."),
        ],
    },
    context=[ex("En una foto de la plaza lees: «A girl is running. A boy is eating. A dog is sleeping.» ¿Quién duerme?", "El perro", "A dog is sleeping.")],
    selfcheck=[
        ex("¿Cómo se dice «leyendo» en inglés?", "reading", "Reading es leyendo."),
        ex("Lee: «She is playing.» ¿Qué hace ella?", "Juega", "Playing es jugando."),
        ex("¿Qué palabra va con «I»: am, is o are?", "am", "I am es la forma correcta."),
    ],
    open_task=task("Lee estas frases: «Mia is reading. Leo is drawing. The dog is sleeping. The children are playing.» Dibuja cuatro escenas pequeñas, una por frase, y escribe debajo de cada una la palabra con -ing. Luego escribe qué estás haciendo tú ahora: «I am ...».", "Cuatro dibujos con reading, drawing, sleeping, playing. Mi frase: I am writing.", ["cuatro escenas correctas", "rótulos con -ing", "una frase propia con I am"], ["dibujos", "frase"], ["dibujar a Leo leyendo", "escribir I writing"], "Compara con él cada dibujo con su frase y revisa el -ing."),
    reinforce="Lee «He is eating» y haz el gesto de comer.",
    extend="Escribe cinco frases con is o are y -ing sobre lo que ves por la ventana.",
)
