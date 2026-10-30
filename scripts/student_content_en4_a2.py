"""Student material for 4.º básico Inglés (propuesta), EN04 OA 02 (comprender textos orales sobre temas y funciones conocidos).

Las «escuchas» las lee un adulto en voz alta; el guion va en el enunciado. Cada palabra o estructura se explica antes de usarla.
Temas: escuela, animales salvajes, casa y muebles, figuras, ocupaciones, ciudad, comida, Easter. Cantidades hasta veinte.
"""
from __future__ import annotations

from student_content_en4_a import ADULT, E, lesson, task
from student_lessons import arith

OA2 = "EN04 OA 02"

# ---------------------------------------------------------------- clase 1
lesson(
    OA2, 1,
    "Las instrucciones y presentaciones escritas en cada ejercicio, que lee un adulto en voz alta; un libro o cuaderno, un lápiz, una hoja y una hoja para tapar el guion.",
    "Aprenderé a seguir instrucciones de la sala de clases y a entender cuando alguien se presenta o presenta a otra persona. Sirve para participar en la clase de inglés.",
    ["Sé que open es abrir y close es cerrar.", "Sé decir hello y I'm Ana."],
    [
        "Una instrucción dice qué hacer y comienza con la palabra de acción: «Take your pencil» (toma tu lápiz), «Put the pencil on the desk» (pon el lápiz sobre el escritorio), «Draw a circle» (dibuja un círculo), «Give me the ruler, please» (dame la regla, por favor) y «Look at the board» (mira la pizarra).",
        "Para presentarse se dice «My name is Sofía» (me llamo Sofía) o «I'm nine» (tengo nueve años). Para presentar a otra persona se dice «This is my friend Leo» (este es mi amigo Leo). Después se usa He is... para un niño (él) y She is... para una niña (ella).",
        "Al escuchar una instrucción busca primero la palabra de acción y luego el objeto o el lugar. Al escuchar una presentación busca quién habla (My name is) y quién es presentado (This is). Con he y she sabes si hablan de un niño o de una niña.",
    ],
    [("take / put", "tomar / poner"), ("draw", "dibujar"), ("give me", "dame"), ("circle / square / triangle", "círculo / cuadrado / triángulo"), ("This is my friend", "este es mi amigo / esta es mi amiga"), ("He is / She is", "él es o está / ella es o está"), ("crayon", "lápiz de cera")],
    [
        ("Seguir una instrucción", ADULT + "«Put the pencil on the desk. Draw a star.» (desk = escritorio, star = estrella). ¿Dónde pones el lápiz?", ["Busco la palabra de acción: put.", "Busco el lugar: on the desk.", "Pongo el lápiz sobre el escritorio."], "Sobre el escritorio"),
        ("Entender una presentación", ADULT + "«Hello! My name is Sofía. This is my friend Leo. He is ten.» ¿Quién tiene diez años?", ["Busco He is ten.", "He se refiere al niño presentado.", "El niño presentado es Leo."], "Leo"),
    ],
    [
        ("Pensar que «He is ten» habla de la persona que se presenta, Sofía.", "He es él; Sofía es una niña.", "Para una niña se dice she; he habla de un niño, aquí Leo."),
        ("Poner el objeto en cualquier lugar sin escuchar on the desk.", "No se escuchó el lugar.", "Después de la acción escucha el lugar o el objeto."),
    ],
    [
        (ADULT + "«Take your pencil.» ¿Qué haces?", "Tomo mi lápiz", "Take significa tomar."),
        (ADULT + "«Draw a circle.» ¿Qué dibujas?", "Un círculo", "Circle significa círculo."),
        (ADULT + "«My name is Sofía.» ¿Qué dice la persona?", "Que se llama Sofía", "My name is significa me llamo."),
    ],
    [
        ("¿Qué significa «Give me the ruler, please»?", "Dame la regla, por favor", "Give me es dame y ruler es regla."),
        ("En «This is my friend Mia. She is nine», ¿qué significa she?", "Ella", "She habla de una niña o mujer."),
        ("¿Qué palabra de una instrucción te dice qué hacer?", "La palabra de acción, como take o draw", "La acción va al comienzo de la instrucción."),
    ],
    [
        (ADULT + "«This is my friend Mia. She is nine.» ¿Quién tiene nueve años?", "Mia", "She is nine habla de Mia."),
        (ADULT + "«Open your book. Look at the board. Close your book.» ¿Qué haces en segundo lugar?", "Miro la pizarra", "Look at the board es la segunda instrucción."),
        (ADULT + "«Draw a circle. Then draw a triangle.» ¿Qué figura dibujas al final?", "Un triángulo", "Then draw a triangle es la última instrucción."),
    ],
    [
        ("Pedro oyó «This is my friend Leo. He is ten» y dice que quien habla tiene diez años. ¿Tiene razón?", "No; el que tiene diez años es Leo", "He is ten habla de Leo, no de quien presenta."),
        ("La profesora dice «Draw a circle. Then draw a triangle». Sofía dibujó primero el triángulo. ¿Qué debió dibujar primero?", "Un círculo", "Then indica que el triángulo va después."),
    ],
    [
        arith(ADULT + "«Take five crayons. Give two crayons to Leo.» (crayon = lápiz de cera). ¿Cuántos crayons te quedan?", "5-2", "Se restan los crayons que le das a Leo."),
        (ADULT + "«Hello! My name is Ana. This is my friend Tom. He is ten. This is my friend Eva. She is nine.» ¿Quién tiene nueve años y a cuántos amigos presenta Ana?", "Eva tiene nueve años y Ana presenta a 2 amigos", "She is nine habla de Eva, y Ana presenta a Tom y a Eva."),
    ],
    [(ADULT + "La profesora dice: «Open your book. Draw a star. Show the star, please.» (show = mostrar). ¿Qué muestras?", "La estrella", "Show the star significa muestra la estrella.")],
    [
        ("¿Qué significa «put»?", "Poner", "Put es poner algo en un lugar."),
        ("¿Qué significa «This is my friend»?", "Este es mi amigo", "Se usa para presentar a otra persona."),
        ("¿Qué usas para hablar de un niño: he o she?", "he", "He es él y she es ella."),
    ],
    task("Un adulto dice dos veces: «Take your pencil. Draw a circle. Draw a triangle next to it. Show it, please.» (next to it = al lado). Haz lo que oyes en una hoja. Después escribe una presentación: «My name is ___. I'm ___.» con tu nombre y tu edad.", "Un círculo y un triángulo dibujados; «My name is Sofía. I'm nine.»", ["dibuja las dos figuras en orden", "muestra el dibujo", "escribe su nombre y edad"], ["dibujo del estudiante", "nota del adulto"], ["dibujar solo una figura", "escribir el nombre en lugar de la edad"], "Reconoce el orden logrado y repite con él, despacio, la palabra de acción que olvidó."),
    "Pide a un adulto que diga «take, put, draw» y haz cada acción con un lápiz.",
    "Escribe tres instrucciones para un compañero, por ejemplo «Open your book. Draw a square. Show it, please.»",
)

# ---------------------------------------------------------------- clase 2
lesson(
    OA2, 2,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a entender lo que alguien puede o no puede hacer y cómo se siente, con can, can't y palabras de sentimientos. Sirve para entender a otras personas al presentarse.",
    ["Sé decir I'm happy.", "Conozco verbos como run, jump y sing."],
    [
        "Para hablar de una habilidad se usa can. «I can swim» significa «puedo nadar» o «sé nadar». Para decir que no puedes se usa can't: «I can't ride a bike» significa «no puedo andar en bicicleta». Para preguntar se dice «Can you jump?» (¿puedes saltar?). Se responde «Yes, I can» o «No, I can't».",
        "Para hablar de sentimientos se usa I'm: I'm happy (estoy feliz), I'm sad (estoy triste), I'm tired (estoy cansado), I'm hungry (tengo hambre) e I'm scared (tengo miedo). La palabra but significa «pero» y une dos ideas distintas, como en «I can run, but I can't jump».",
        "Al escuchar, busca can o can't antes del verbo: te dice si la persona puede hacer algo. Busca también la palabra del sentimiento después de I'm. No te quedes con una sola palabra: oye la frase completa.",
    ],
    [("can", "poder, saber hacer"), ("can't", "no poder"), ("swim / sing / fly", "nadar / cantar / volar"), ("ride a bike", "andar en bicicleta"), ("happy / sad / tired", "feliz / triste / cansado"), ("hungry / scared", "con hambre / con miedo"), ("but", "pero")],
    [
        ("Habilidades", ADULT + "«Hello! I'm Lia. I can swim and I can sing. I can't ride a bike. I'm happy today.» (today = hoy). ¿Qué no puede hacer Lia?", ["Busco can't.", "Después de can't oigo ride a bike.", "No puede andar en bicicleta."], "Andar en bicicleta"),
        ("Sentimientos", "En el mismo texto, ¿cómo se siente Lia?", ["Busco I'm.", "Después de I'm oigo happy.", "Happy significa feliz."], "Feliz"),
    ],
    [
        ("Pensar que Tom puede saltar porque oyó la palabra jump.", "No se escuchó can't antes de jump.", "Escucha can o can't antes del verbo: «I can't jump» significa que no puede."),
        ("Pensar que I'm tired significa que la persona tiene hambre.", "Se confunden palabras de sentimientos.", "Tired es cansado y hungry es con hambre."),
    ],
    [
        ("¿Qué significa «I can swim»?", "Puedo nadar", "Can indica que puedes hacer algo."),
        ("¿Qué significa «I can't ride a bike»?", "No puedo andar en bicicleta", "Can't indica que no puedes."),
        (ADULT + "«I'm Lia. I can swim and I can sing. I'm happy.» ¿Cómo se siente Lia?", "Feliz", "Happy significa feliz."),
    ],
    [
        ("¿Qué significa «sad»?", "Triste", "Sad describe un sentimiento de tristeza."),
        ("¿Qué significa «Can you jump?»", "¿Puedes saltar?", "Can you pregunta si puedes hacer algo."),
        ("¿Qué diferencia hay entre can y can't?", "Can dice que puedes y can't dice que no puedes", "Can't es la forma negativa de can."),
    ],
    [
        (ADULT + "«A bird can fly. A fish can swim. A dog can't fly.» (fly = volar). ¿Qué animal no puede volar según el texto?", "Un perro", "A dog can't fly dice que el perro no vuela."),
        (ADULT + "«I'm Tom. I'm hungry and I'm tired. I can run, but I can't jump.» ¿Qué sentimientos tiene Tom?", "Hambre y cansancio", "Hungry es con hambre y tired es cansado."),
        (ADULT + "«I'm Tom. I'm hungry and I'm tired. I can run, but I can't jump.» ¿Qué no puede hacer Tom?", "Saltar", "I can't jump significa no puedo saltar."),
    ],
    [
        (ADULT + "«I'm Tom. I can run, but I can't jump.» Ana dice que Tom puede saltar porque dijo jump. ¿Tiene razón?", "No; Tom dijo «I can't jump»", "Can't significa que no puede."),
        (ADULT + "«Mia: Can you swim? Leo: Yes, I can. Mia: Can you fly? Leo: No, I can't! Ha, ha!» ¿Qué sí puede hacer Leo?", "Nadar", "Leo responde Yes, I can a la pregunta sobre nadar."),
    ],
    [
        ("Texto: «I'm Max. I can run, jump, swim and sing. I can't fly.» ¿Cuántas cosas puede hacer Max?", "4", "Run, jump, swim y sing son cuatro habilidades; fly no."),
        (ADULT + "«Pam is sad. Pam can't find her ball. Then Ben gives her the ball. Pam is happy.» (find = encontrar, gives = da). ¿Cómo se siente Pam al final y por qué?", "Feliz, porque Ben le da su pelota", "Al final dice Pam is happy y antes Ben gives her the ball."),
    ],
    [(ADULT + "En la clase, una niña dice: «I can draw, but I can't sing.» ¿Qué sabe hacer?", "Dibujar", "I can draw significa puedo dibujar.")],
    [
        ("¿Qué significa «but»?", "Pero", "But une dos ideas distintas."),
        ("¿Qué significa «hungry»?", "Con hambre", "Hungry describe la necesidad de comer."),
        (ADULT + "«Can you sing? Yes, I can.» ¿Puede cantar la persona que responde?", "Sí", "Yes, I can significa sí, puedo."),
    ],
    task("Un adulto lee dos veces: «Hello! I'm Sam. I can swim and I can run. I can't ride a bike. I'm tired today.» Escribe en tu hoja dos cosas que Sam puede hacer, una que no puede hacer y cómo se siente.", "Puede: swim y run. No puede: ride a bike. Se siente: tired.", ["escribe swim y run", "escribe ride a bike", "escribe tired"], ["hoja con lo escrito", "nota del adulto"], ["poner ride a bike entre lo que sí puede", "confundir tired con happy"], "Reconoce lo que ubicó bien y vuelve a escuchar solo la frase con can't."),
    "Pide a un adulto que diga «I can run» y «I can't fly», y haz la acción solo cuando se pueda.",
    "Escribe tres frases sobre ti con I can, I can't y I'm, por ejemplo «I can draw. I can't swim. I'm happy.»",
)

# ---------------------------------------------------------------- clase 3
lesson(
    OA2, 3,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a entender quién tiene qué, cuántas cosas hay (hasta veinte) y dónde están con in, on, under y next to. Sirve para describir objetos y muebles en un lugar.",
    ["Sé contar en inglés hasta veinte.", "Sé decir table, chair y bed."],
    [
        "Para hablar de posesión se usa have o has: «I have two pets» (tengo dos mascotas), «Ben has fifteen stickers» (Ben tiene quince calcomanías). Has se usa con he y she. Para decir cuántas cosas hay se usan números hasta veinte (twenty) y las expresiones there is (hay uno) y there are (hay varios).",
        "Para decir dónde está algo se usan in (en, dentro de), on (sobre), under (debajo de) y next to (al lado de). Algunos muebles son table (mesa), chair (silla), bed (cama), sofa (sofá), lamp (lámpara) y shelf (repisa). Las partes de la casa son bedroom (dormitorio), kitchen (cocina), bathroom (baño) y living room (living o sala de estar).",
        "Al escuchar, busca primero el objeto, luego el número y por último la palabra de lugar. «The cat is under the table» significa que el gato está debajo de la mesa. No confundas under con on: son lugares opuestos.",
    ],
    [("have / has", "tener"), ("there is / there are", "hay (uno) / hay (varios)"), ("in / on / under", "en / sobre / debajo de"), ("next to", "al lado de"), ("table / chair / bed", "mesa / silla / cama"), ("sofa / lamp / shelf", "sofá / lámpara / repisa"), ("bedroom / kitchen", "dormitorio / cocina"), ("bathroom / living room", "baño / living")],
    [
        ("Dónde está el objeto", ADULT + "«Look at my bedroom. There is a bed and there is a lamp. There are two chairs next to the table. My cat is under the table. My books are on the shelf. There are twelve books.» (books = libros). ¿Dónde está el gato?", ["Busco cat.", "Después oigo under the table.", "Under significa debajo de."], "Debajo de la mesa"),
        ("Cuántas cosas hay", "En el mismo texto, ¿cuántos libros hay en la repisa?", ["Busco books y shelf.", "Oigo twelve books.", "Twelve es doce."], "12"),
    ],
    [
        ("Confundir under con on y poner el gato sobre la mesa.", "Son palabras de lugar opuestas.", "Under es debajo de y on es sobre; escucha cuál se dijo."),
        ("Usar there is cuando se habla de muchas cosas.", "There is es para una sola cosa.", "Para varias cosas se usa there are, como en «There are two chairs»."),
    ],
    [
        ("¿Qué significa «under»?", "Debajo de", "Under indica un lugar más abajo."),
        ("¿Qué significa «on the shelf»?", "Sobre la repisa", "On es sobre y shelf es repisa."),
        (ADULT + "«My cat is under the table.» ¿Dónde está el gato?", "Debajo de la mesa", "Under the table significa debajo de la mesa."),
    ],
    [
        ("¿Cuál se usa para una sola cosa: there is o there are?", "there is", "There is habla de una cosa; there are, de varias."),
        ("¿Qué significa «next to»?", "Al lado de", "Next to indica un lugar junto a otro."),
        ("¿Qué palabra se usa con he y she: have o has?", "has", "Has se usa con he y she."),
    ],
    [
        (ADULT + "«Look at my bedroom. There are twelve books on the shelf.» ¿Cuántos libros hay en la repisa?", "12", "Twelve es doce."),
        (ADULT + "«Ben has fifteen stickers. Mia has four stickers.» (stickers = calcomanías). ¿Cuántas calcomanías tiene Mia?", "4", "Mia has four significa Mia tiene cuatro."),
        arith(ADULT + "«Ben has fifteen stickers. Mia has four stickers.» ¿Cuántas calcomanías tienen Ben y Mia juntos?", "15+4", "Se suman las calcomanías de Ben y de Mia."),
    ],
    [
        ("Ana oyó «There is a bed» y dice que hay dos camas. ¿Tiene razón?", "No; there is significa que hay una cama", "There is se usa para una sola cosa."),
        (ADULT + "«The ball is on the sofa. The dog is under the sofa. The cat is next to the sofa.» ¿Qué animal está debajo del sofá?", "El perro", "The dog is under the sofa."),
    ],
    [
        arith(ADULT + "«There are nine red pens and eleven blue pens in a box.» (pens = lápices de pasta). ¿Cuántos pens hay en total?", "9+11", "Se suman los pens rojos y los azules."),
        (ADULT + "«The lamp is on the table. The table is next to the bed. The cat is under the bed.» ¿Qué mueble está al lado de la cama?", "La mesa", "The table is next to the bed."),
    ],
    [(ADULT + "En un juego, preguntan «Where is the ball?» (where = dónde) y responden «It is under the chair.» ¿Dónde está la pelota?", "Debajo de la silla", "Under the chair significa debajo de la silla.")],
    [
        (ADULT + "«The bed is in the bedroom. The sofa is in the living room. The table is in the kitchen.» ¿En qué parte de la casa está el sofá?", "En el living", "The sofa is in the living room."),
        ("¿Qué significa «There are twenty»?", "Hay veinte", "There are indica varios y twenty es veinte."),
        ("¿Qué palabra de lugar significa «sobre»?", "on", "On indica que algo está sobre otra cosa."),
    ],
    task("Un adulto lee dos veces: «My bedroom has a bed and a lamp. The lamp is on the table. My cat is under the bed. There are six books on the shelf.» Dibuja el dormitorio con todo en su lugar y escribe debajo cuántos libros hay.", "Una cama, una lámpara sobre la mesa, un gato debajo de la cama y seis libros en la repisa.", ["dibuja la lámpara sobre la mesa", "dibuja el gato debajo de la cama", "escribe que hay seis libros"], ["dibujo del estudiante", "nota del adulto"], ["poner el gato sobre la cama", "escribir otro número de libros"], "Reconoce lo bien ubicado y vuelve a escuchar solo la frase con la palabra de lugar que cambió."),
    "Pide a un adulto que diga «on, under, next to» y pon un lápiz sobre el libro, debajo de la silla y al lado de la mesa.",
    "Escribe tres frases sobre tu pieza con there is, there are, on, under o next to, por ejemplo «There is a lamp on the table.»",
)

# ---------------------------------------------------------------- clase 4
lesson(
    OA2, 4,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a entender lo que alguien está haciendo ahora mismo, con is, are y un verbo terminado en -ing. Sirve para entender descripciones de lo que pasa en este momento.",
    ["Sé que he es él y she es ella.", "Conozco verbos como run, read, play y sleep."],
    [
        "Para decir lo que alguien está haciendo ahora se usa is o are y un verbo que termina en -ing. «She is running» significa «ella está corriendo». «They are playing» significa «ellos están jugando». Con yo se usa I'm: «I'm drawing» significa «estoy dibujando».",
        "Se usa is con una persona (he, she, Ana) y are con varias (they, two boys). Verbos nuevos: reading (leyendo), sleeping (durmiendo), eating (comiendo), drinking (bebiendo), cooking (cocinando) y painting (pintando). Para preguntar se dice «What is he doing?» (¿qué está haciendo él?).",
        "Al escuchar, busca primero quién hace la acción y luego el verbo con -ing. Si el texto dice «A man is reading», el hombre lee ahora. Si dice «A man can read», habla de una habilidad, no de lo que hace ahora. Escucha is o are y la terminación -ing.",
    ],
    [("is / are + -ing", "está(n) haciendo algo ahora"), ("running", "corriendo"), ("playing", "jugando"), ("reading", "leyendo"), ("sleeping", "durmiendo"), ("eating / drinking", "comiendo / bebiendo"), ("What is he doing?", "¿qué está haciendo él?")],
    [
        ("Qué hace alguien ahora", ADULT + "«Look at the park! A girl is running. Two boys are playing with a ball. A man is reading a book. A dog is sleeping under a tree.» (park = parque). ¿Qué hace el hombre?", ["Busco man.", "Después oigo is reading.", "Reading significa leyendo."], "Lee un libro"),
        ("Cuántas personas", "En el mismo texto, ¿cuántos niños están jugando con una pelota?", ["Busco playing with a ball.", "Antes oigo two boys.", "Two es dos."], "2"),
    ],
    [
        ("Pensar que «A man can read» dice lo que el hombre hace ahora.", "Can read habla de una habilidad.", "Para lo que pasa ahora busca is o are con un verbo terminado en -ing."),
        ("Usar are con una sola persona.", "Are se usa con varias personas.", "Con una persona se usa is: «A girl is running»."),
    ],
    [
        ("¿Qué significa «is running»?", "Está corriendo", "Is running dice que pasa ahora."),
        ("¿Qué significa «are playing»?", "Están jugando", "Are se usa con varias personas."),
        (ADULT + "«A girl is running in the park.» ¿Qué hace la niña?", "Corre", "Running significa corriendo."),
    ],
    [
        ("En «She is reading», ¿qué palabras muestran que la acción pasa ahora?", "is y reading", "Is más un verbo con -ing muestra una acción en este momento."),
        ("¿Se usa is o are con «Two boys»?", "are", "Two boys son varias personas."),
        ("¿Qué significa «What is he doing?»", "¿Qué está haciendo él?", "Doing es haciendo."),
    ],
    [
        (ADULT + "«A dog is sleeping under a tree.» (tree = árbol). ¿Qué hace el perro?", "Duerme", "Sleeping significa durmiendo."),
        (ADULT + "«Two boys are playing with a ball.» ¿Cuántos niños juegan con una pelota?", "2", "Two boys son dos niños."),
        (ADULT + "«A man is reading a book.» ¿Quién lee un libro?", "Un hombre", "A man is reading dice que un hombre lee."),
    ],
    [
        ("Texto: «Look at the park! A girl is running. Two boys are playing with a ball. A man is reading a book. A dog is sleeping under a tree.» Sofía dice que el perro está corriendo. Según el texto, ¿qué hace el perro?", "Está durmiendo bajo un árbol", "El texto dice A dog is sleeping under a tree."),
        (ADULT + "«Mr. Silva is cooking soup. Ana is drinking milk. Leo is eating bread.» (Mr. = señor, soup = sopa, milk = leche, bread = pan). ¿Quién está bebiendo?", "Ana", "Ana is drinking milk."),
    ],
    [
        (ADULT + "«Tom is painting. Eva and Lia are painting, too. Max is sleeping.» (painting = pintando). ¿Cuántas personas están pintando?", "3", "Tom, Eva y Lia están pintando; Max duerme."),
        ("¿Qué frase dice que Leo salta ahora: a) Leo can jump b) Leo is jumping?", "b", "Is jumping muestra una acción en este momento; can jump habla de una habilidad."),
    ],
    [(ADULT + "En un juego de mímica, una niña finge beber de un vaso y dice «I'm drinking.» (I'm = yo estoy). ¿Qué hace?", "Bebe", "Drinking significa bebiendo.")],
    [
        ("¿Qué significa «sleeping»?", "Durmiendo", "Sleeping viene de sleep, dormir."),
        ("¿Con qué palabra se usa is: con una persona o con varias?", "Con una persona", "Is se usa con una persona; are con varias."),
        ("¿Qué significa «I'm drawing»?", "Estoy dibujando", "I'm drawing dice lo que haces ahora."),
    ],
    task("Un adulto lee dos veces: «Look at the school yard! Ana is running. Leo is reading a book. Two girls are playing with a ball. A boy is drinking water.» (yard = patio, water = agua). Dibuja las cuatro escenas y escribe debajo de cada una el verbo con -ing que oíste.", "Cuatro dibujos: running, reading, playing y drinking.", ["dibuja las cuatro acciones", "escribe running, reading, playing y drinking", "dibuja a dos niñas jugando"], ["dibujos del estudiante", "nota del adulto"], ["dibujar a una sola niña jugando", "escribir sleeping en lugar de drinking"], "Reconoce las acciones bien dibujadas y vuelve a escuchar solo la frase donde se equivocó."),
    "Pide a un adulto que diga «running, reading, sleeping» y haz la mímica de cada acción.",
    "Escribe tres frases sobre lo que alguien de tu casa está haciendo ahora, por ejemplo «My friend is reading.»",
)

# ---------------------------------------------------------------- clase 5
lesson(
    OA2, 5,
    "Seis textos cortos escritos en los ejercicios, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a unir el tema de un texto (de qué trata) con su propósito (para qué se dice). Sirve para entender textos orales de la escuela, los animales, la casa, las figuras, las ocupaciones, la ciudad, la comida y Easter.",
    ["Sé seguir instrucciones, presentarme, hablar de habilidades y describir lo que pasa ahora.", "Conozco palabras de la escuela, la casa y la comida."],
    [
        "El tema (topic) es de qué trata el texto: la escuela, animales salvajes, la casa, las figuras, las ocupaciones (jobs), los lugares de la ciudad (town), como library (biblioteca), supermarket (supermercado) y park (parque), la comida o Easter. Easter (Pascua de Resurrección) es una celebración cristiana; en muchos lugares las personas decoran, esconden o regalan huevos, por ejemplo de chocolate. El propósito (purpose) es para qué se dice.",
        "Los propósitos de hoy son cinco: dar instrucciones («Draw a circle»), presentar a alguien («This is my friend...»), decir lo que alguien puede hacer o cómo se siente («I can cook rice»), describir un animal o un objeto («The giraffe has a long neck») y decir qué pasa ahora («A baker is making bread»).",
        "Para unir tema y propósito, escucha las palabras clave. Una palabra como giraffe indica el tema animales. Una frase que empieza con la acción, como draw, indica instrucciones. Una frase con is más -ing dice qué pasa ahora. Responde las dos preguntas: ¿de qué trata? y ¿para qué se dice?",
    ],
    [("topic", "tema: de qué trata un texto"), ("purpose", "propósito: para qué se dice"), ("job", "ocupación, trabajo"), ("town", "ciudad, pueblo"), ("Easter", "Pascua de Resurrección, celebración"), ("long neck", "cuello largo"), ("baker / bakery", "panadero / panadería")],
    [
        ("Tema de un texto", ADULT + "«The giraffe is tall. It has a long neck. It can eat leaves from tall trees.» (tall = alto, leaves = hojas). ¿De qué tema trata el texto?", ["Escucho la palabra giraffe.", "La jirafa es un animal salvaje.", "El tema es animales salvajes."], "Animales salvajes"),
        ("Propósito de un texto", "En el mismo texto, ¿para qué se dice? Elige: dar instrucciones o describir un animal.", ["Busco si hay una orden como draw o open.", "No hay órdenes.", "El texto cuenta cómo es la jirafa."], "Describir un animal"),
    ],
    [
        ("Pensar que un texto es una instrucción solo porque tiene verbos.", "Todos los textos tienen verbos.", "Una instrucción comienza con la acción y ordena algo, como draw o open."),
        ("Decir el tema sin mencionar la palabra que lo muestra.", "No se vuelve al texto para comprobarlo.", "Nombra la palabra clave, como giraffe o eggs, que apoya el tema."),
    ],
    [
        (ADULT + "«Hello. I'm Sam. I'm a cook. This is my friend Eva. She is a doctor.» (cook = cocinero, doctor = doctora). ¿De qué tema trata?", "Ocupaciones", "Cook y doctor son ocupaciones."),
        (ADULT + "«It is Easter. There are six eggs in the basket. The eggs are red, blue and yellow.» (basket = canasta). ¿Qué celebración se menciona?", "Easter", "El texto comienza con It is Easter."),
        (ADULT + "«Draw a circle. Draw a square. Draw a triangle.» ¿De qué tema trata?", "Figuras", "Circle, square y triangle son figuras."),
    ],
    [
        ("En el texto «Draw a circle. Draw a square. Draw a triangle.», ¿para qué se dice?", "Para dar instrucciones", "Draw ordena dibujar algo."),
        ("Lee: «Hello. I'm Sam. I'm a cook. This is my friend Eva. She is a doctor.» ¿Para qué se dice?", "Para presentarse y presentar a otra persona", "Aparecen I'm y This is my friend."),
        (ADULT + "«We are in town. The library is next to the supermarket. The park is near my school.» (near = cerca de). ¿Qué lugar está al lado del supermercado?", "La biblioteca", "The library is next to the supermarket."),
    ],
    [
        (ADULT + "«A baker is making bread. A girl is buying a loaf at the bakery.» (making = haciendo, buying = comprando, loaf = pan, bakery = panadería). ¿Qué hace la niña?", "Compra pan", "A girl is buying a loaf."),
        (ADULT + "«The giraffe is tall. It has a long neck.» ¿Qué tiene la jirafa?", "Un cuello largo", "Has a long neck significa tiene un cuello largo."),
        (ADULT + "«It is Easter. There are six eggs in the basket. The eggs are red, blue and yellow.» ¿De qué colores son los huevos?", "Rojo, azul y amarillo", "El texto nombra red, blue y yellow."),
    ],
    [
        ("Pedro lee «The giraffe is tall. It has a long neck.» y dice que es una instrucción porque tiene verbos. ¿Tiene razón?", "No; describe a un animal y no ordena nada", "No tiene órdenes como draw o open."),
        ("¿Cuál de estas dos frases es una instrucción? A) «Draw a star.» B) «The star is yellow.»", "A", "Draw a star ordena hacer algo; la B describe."),
    ],
    [
        arith(ADULT + "«At Easter, Eva has a basket. There are three red eggs, two blue eggs and four yellow eggs.» ¿Cuántos huevos hay en la canasta?", "3+2+4", "Se suman los huevos de cada color."),
        (ADULT + "«Hello! I'm Ana. I'm a teacher. I'm reading a book now. This is my friend Tom. He is a farmer.» (farmer = agricultor). ¿Qué dos ocupaciones se nombran?", "Teacher y farmer", "Ana es teacher y Tom es farmer."),
    ],
    [(ADULT + "En clase hacen una tarjeta de Easter. La profesora dice: «Draw an egg. Color it blue.» (card = tarjeta, color = pintar). ¿Qué debes dibujar?", "Un huevo", "Draw an egg significa dibuja un huevo.")],
    [
        ("¿Qué es el tema de un texto?", "De qué trata el texto", "El tema responde a la pregunta de qué trata."),
        ("¿Qué es el propósito de un texto?", "Para qué se dice", "El propósito responde a la pregunta para qué."),
        ("¿Qué significa «job»?", "Ocupación o trabajo", "Job es la tarea con que una persona trabaja."),
    ],
    task("Un adulto lee dos veces: «Hello! I'm Sam. I'm a baker. I can make bread. Look! A girl is buying a loaf at my bakery.» Escribe en tu hoja el tema del texto (jobs, food o town) y el propósito (presentarse, decir qué puede hacer, decir qué pasa ahora). Señala dos palabras que te dieron la pista.", "Tema: ocupaciones, comida y ciudad (baker, bread, bakery). Propósitos: presentarse, decir qué puede hacer y decir qué pasa ahora.", ["escribe un tema correcto", "escribe un propósito correcto", "nombra dos palabras clave como baker, bread o buying"], ["hoja con tema y propósito", "nota del adulto"], ["decir un tema sin palabra clave", "decir que es una instrucción"], "Reconoce la parte acertada y vuelve a leer con él las palabras que dan la pista."),
    "Pide a un adulto que diga «giraffe, egg, doctor, circle» y di a qué tema pertenece cada palabra.",
    "Escribe un texto de dos o tres frases sobre un animal salvaje que describas, por ejemplo «The zebra has stripes. It can run.»",
)
