"""Student material for 3.º básico Inglés (propuesta), EN03 OA 02 (escuchar temas y funciones conocidas).

Las «escuchas» las lee un adulto en voz alta; el guion va en el enunciado. Cada palabra o estructura se explica antes de usarla.
"""
from __future__ import annotations

from student_content_en3_a import ADULT, E, lesson, task
from student_lessons import arith

OA2 = "EN03 OA 02"

lesson(
    OA2, 1,
    "Las instrucciones y presentaciones escritas en cada ejercicio, que lee un adulto en voz alta; un libro o cuaderno, un lápiz y una hoja para tapar el guion.",
    "Aprenderé a seguir instrucciones de la sala de clases y a entender cuando alguien se presenta o presenta a otra persona. Sirve para participar en la clase de inglés.",
    ["Sé que sit down es sentarse y stand up es ponerse de pie.", "Sé decir hello."],
    [
        "Una instrucción dice qué hacer y empieza con la palabra de acción. «Open your book» significa «abre tu libro» y «close your book» significa «cierra tu libro». Otras instrucciones son listen (escucha), look at the board (mira la pizarra) y raise your hand (levanta la mano). Please significa «por favor».",
        "Para presentarse se dice «I'm Ana», que significa «soy Ana». Para presentar a otra persona se dice «This is my friend Leo», que significa «este es mi amigo Leo». La respuesta amable es «Nice to meet you», que significa «mucho gusto». En la mañana se dice «Good morning».",
        "Al escuchar una instrucción, primero busca la palabra de acción y luego el objeto (book, board o hand). Si oyes un nombre, puede ser la persona que habla o la persona presentada. Escucha las palabras I'm y This is para saberlo.",
    ],
    [("open / close", "abrir / cerrar"), ("listen", "escuchar"), ("look at", "mirar a"), ("raise your hand", "levantar la mano"), ("please", "por favor"), ("I'm / This is my friend", "soy / este es mi amigo"), ("Nice to meet you", "mucho gusto"), ("Good morning", "buenos días")],
    [
        ("Seguir una instrucción", ADULT + "«Open your book, please.» (book = libro). ¿Qué haces?", ["Busco la palabra de acción: open.", "Busco el objeto: book.", "Junto las dos pistas."], "Abro mi libro"),
        ("Entender una presentación", ADULT + "«Hello! I'm Mia. This is my friend Tom.» ¿Quién es Tom?", ["Busco I'm: la persona que habla es Mia.", "Busco This is my friend: Tom es presentado.", "Tom es el amigo de Mia."], "El amigo de Mia"),
    ],
    [
        ("Hacer la acción contraria, por ejemplo abrir el libro cuando se dice close.", "No se escuchó la palabra de acción.", "Escucha primero open o close y luego el objeto."),
        ("Pensar que I'm Mia significa que Mia es el amigo de otra persona.", "Se confunde I'm con This is.", "I'm es la persona que habla; This is presenta a otra persona."),
    ],
    [
        (ADULT + "«Open your book.» (open = abrir, book = libro). ¿Qué haces?", "Abro mi libro", "Open significa abrir."),
        (ADULT + "«Close your book, please.» ¿Qué haces?", "Cierro mi libro", "Close significa cerrar."),
        (ADULT + "«I'm Ana.» ¿Qué dice la persona?", "Que se llama Ana", "I'm Ana significa soy Ana."),
    ],
    [
        ("¿Qué significa «raise your hand»?", "Levanta la mano", "Raise es levantar y hand es mano."),
        ("¿Qué significa «Nice to meet you»?", "Mucho gusto", "Es una respuesta amable al conocer a alguien."),
        ("¿Qué palabra de una instrucción te dice qué hacer?", "La palabra de acción, como open o close", "La palabra de acción va al comienzo de la instrucción."),
    ],
    [
        (ADULT + "«Listen. Look at the board. Raise your hand.» (board = pizarra). ¿Qué haces primero?", "Escucho", "Listen es la primera instrucción."),
        (ADULT + "«This is my friend Leo. Nice to meet you, Leo!» ¿Cómo se llama el amigo?", "Leo", "This is my friend Leo presenta al amigo."),
        (ADULT + "«Open your book, please. Look at the board.» ¿Qué debes mirar?", "La pizarra", "Look at the board significa mira la pizarra."),
    ],
    [
        ("Una niña oyó «Please close your book» y abrió su libro. ¿Qué palabra entendió mal?", "Close, que significa cerrar", "Open y close son acciones contrarias."),
        (ADULT + "«I'm Sam. This is my friend Mia.» ¿Quién habla: Sam o Mia?", "Sam", "I'm Sam muestra quién habla."),
    ],
    [
        ("Ordena las instrucciones según el guion (stand up = ponerse de pie, sit down = sentarse): A) Sit down. B) Stand up. C) Look at the board. Guion: «Stand up. Look at the board. Sit down.»", "B, C, A", "El guion dice primero stand up, luego look y al final sit down."),
        (ADULT + "«Hello! I'm Lia. This is my friend Tom. Tom, open your book, please.» ¿Quién debe abrir el libro?", "Tom", "La instrucción llama a Tom con su nombre."),
    ],
    [(ADULT + "En la sala, la profesora dice: «Good morning. Open your book, please. Raise your hand.» Sin contar el saludo, ¿cuántas instrucciones oyes?", "2", "Open your book y raise your hand son dos instrucciones.")],
    [
        ("¿Qué significa «please»?", "Por favor", "Se agrega a una instrucción para pedirla con amabilidad."),
        (ADULT + "«Look at the board.» ¿Qué haces?", "Miro la pizarra", "Look at significa mirar a."),
        ("¿Cómo dices «mucho gusto» en inglés?", "Nice to meet you", "Es la frase que se usa al conocer a alguien."),
    ],
    task("Un adulto da dos veces estas instrucciones: «Stand up. Raise your hand. Sit down.» Hazlas en orden. Luego el adulto dice «Hello! I'm Ana. This is my friend Leo.» y tú respondes en voz alta «Nice to meet you!».", "Se pone de pie, levanta la mano, se sienta y dice Nice to meet you.", ["hace las tres acciones en orden", "responde con Nice to meet you", "mira o saluda a la persona presentada"], ["nota del adulto", "foto o video con permiso de la familia"], ["hacer las acciones en otro orden", "no responder al saludo"], "Reconoce el orden bien hecho y practica de nuevo la frase de saludo con él."),
    "Pide a un adulto que diga «Open, close, listen» y haz cada acción con tu cuaderno.",
    "Preséntate con «I'm ...» y presenta a un amigo o a una persona de tu casa con «This is my friend ...».",
)

lesson(
    OA2, 2,
    "Las descripciones escritas en cada ejercicio, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a entender cuando alguien dice lo que puede o no puede hacer y cómo se siente. Sirve para entender a otras personas cuando hablan de sí mismas.",
    ["Sé que run es correr y jump es saltar.", "Sé decir happy y sad."],
    [
        "Para decir lo que puedes hacer se usa can: «I can swim» significa «sé nadar» o «puedo nadar». Para decir lo que no puedes hacer se usa can't: «I can't jump» significa «no puedo saltar». Can no cambia con los nombres: «Mia can draw» significa «Mia sabe dibujar». Las acciones de hoy son swim (nadar), draw (dibujar), sing (cantar), run y jump.",
        "Para preguntar se dice «Can you swim?» (¿puedes nadar?). Se responde «Yes, I can» (sí puedo) o «No, I can't» (no puedo). Para decir cómo te sientes se usa I'm: happy (feliz), sad (triste), tired (cansado) y hungry (con hambre). Con un nombre se dice «Leo is sad», que significa «Leo está triste».",
        "Al escuchar, fíjate en la palabra can o can't: cambia todo el sentido. Luego escucha la acción o el sentimiento. He significa «él» y she significa «ella». Cuando oyes he o she, la frase habla de otra persona y no de quien habla.",
    ],
    [("can", "poder, saber hacer algo"), ("can't", "no poder"), ("swim / draw / sing", "nadar / dibujar / cantar"), ("happy / sad", "feliz / triste"), ("tired", "cansado"), ("hungry", "con hambre"), ("he / she", "él / ella")],
    [
        ("Can o can't", ADULT + "«I can't jump.» ¿Puede saltar la persona?", ["Busco can o can't.", "Oigo can't.", "Can't significa no puede."], "No"),
        ("Un sentimiento", ADULT + "«Leo is sad.» (Leo es un niño). ¿Cómo está Leo?", ["Busco la palabra del sentimiento.", "Oigo sad.", "Sad significa triste."], "Triste"),
    ],
    [
        ("Entender can't como can.", "No se escucha la parte «t» final.", "Escucha bien: can't significa no puede y cambia el sentido."),
        ("Pensar que «I'm tired» habla de otra persona.", "Se confunde I'm con he o she.", "I'm habla de quien dice la frase; he y she hablan de otra persona."),
    ],
    [
        (ADULT + "«I can swim.» (swim = nadar). ¿Qué puede hacer la persona?", "Nadar", "Can swim significa puede nadar."),
        (ADULT + "«I'm hungry.» (hungry = con hambre). ¿Cómo se siente?", "Con hambre", "Hungry significa con hambre."),
        (ADULT + "«I can't jump.» ¿Puede saltar?", "No", "Can't significa no puede."),
    ],
    [
        ("¿Qué diferencia hay entre can y can't?", "Can es puedo y can't es no puedo", "La pequeña diferencia final cambia el sentido."),
        ("¿Qué significa «Can you sing?»", "¿Puedes cantar?", "Can you pregunta si puedes hacer algo."),
        ("¿Qué significa «Leo is tired»?", "Leo está cansado", "Is tired dice cómo está Leo."),
    ],
    [
        (ADULT + "«Mia can draw. Mia can't swim.» ¿Qué no puede hacer Mia?", "Nadar", "Can't swim significa no puede nadar."),
        (ADULT + "«Leo is sad. Leo is tired.» ¿Cuántos sentimientos nombra el guion?", "2", "Sad y tired son dos sentimientos."),
        (ADULT + "«A: Can you run? B: Yes, I can.» ¿Puede correr la persona B?", "Sí", "Yes, I can significa sí puedo."),
    ],
    [
        ("Pedro oyó «I can't sing» y dijo que la persona canta bien. ¿Qué entendió mal?", "No entendió que can't significa no puede", "Can't dice lo contrario de can."),
        (ADULT + "«Sam is happy. He can jump.» (he = él). ¿Qué sentimiento tiene Sam?", "Feliz", "Happy significa feliz."),
    ],
    [
        (ADULT + "«Lia can sing and draw. She can't swim.» (and = y, she = ella). ¿Cuántas cosas puede hacer Lia?", "2", "Puede cantar y dibujar; nadar no."),
        (ADULT + "«A: Can you jump? B: Yes, I can. A: Can you swim? B: No, I can't.» ¿Qué puede hacer B?", "Saltar, pero no nadar", "Yes, I can es para jump y No, I can't es para swim."),
    ],
    [(ADULT + "En educación física, un niño dice: «Hello! I can run. I can jump. I'm happy!» ¿Cómo se siente?", "Feliz", "I'm happy significa estoy feliz.")],
    [
        ("¿Qué significa «draw»?", "Dibujar", "Draw es hacer un dibujo."),
        (ADULT + "«I'm tired.» ¿Cómo se siente?", "Cansado o cansada", "Tired significa cansado."),
        ("Responde «Can you swim?» diciendo que no puedes, en inglés.", "No, I can't", "No, I can't significa no puedo."),
    ],
    task("Un adulto lee dos veces: «Tom can draw. Tom can't swim. Tom is happy.» Dibuja a Tom haciendo lo que puede hacer y escribe debajo de tu dibujo una palabra: draw. Luego di si Tom está happy o sad.", "Tom dibujando, con la palabra draw y la respuesta happy.", ["dibuja la acción que sí puede hacer", "escribe la palabra draw", "dice que Tom está happy"], ["dibujo", "nota del adulto"], ["dibujar a Tom nadando", "decir que Tom está sad"], "Reconoce lo que acertó y vuelve a leer con él la frase donde aparece can't."),
    "Pide a un adulto que diga «I can sing» y «I can't sing» y muestra con el pulgar arriba o abajo cuál es cuál.",
    "Escribe tres frases con I can y una con I can't sobre lo que haces en el recreo.",
)

lesson(
    OA2, 3,
    "Las descripciones escritas en cada ejercicio, que lee un adulto en voz alta; algunos objetos de la casa y lápiz.",
    "Aprenderé a entender cuántas cosas hay (hasta veinte), de quién son y dónde están. Sirve para entender descripciones de objetos y lugares.",
    ["Sé contar en inglés del uno al diez.", "Sé que book, ball y chair son objetos."],
    [
        "Los números del once al veinte son: eleven (11), twelve (12), thirteen (13), fourteen (14), fifteen (15), sixteen (16), seventeen (17), eighteen (18), nineteen (19) y twenty (20). Escucha bien el final: los números del trece al diecinueve terminan en «-teen».",
        "Para decir lo que tienes se dice I have, que significa «tengo»: «I have fifteen stickers». Con un nombre se dice has: «Mia has nineteen marbles» significa «Mia tiene diecinueve bolitas». Para decir cuántas cosas hay se usa There is (hay uno) y There are (hay varios): «There are twelve pencils».",
        "Para decir dónde está algo se usan in (dentro de), on (sobre) y under (debajo de): «The ball is under the chair» significa «la pelota está debajo de la silla». Primero escucha el número, luego el objeto y por último el lugar.",
    ],
    [("eleven – twenty", "once a veinte"), ("I have / has", "tengo / tiene"), ("There is / There are", "hay (uno) / hay (varios)"), ("in", "dentro de"), ("on", "sobre"), ("under", "debajo de"), ("sticker", "calcomanía")],
    [
        ("Un número y un objeto", ADULT + "«I have fifteen stickers.» ¿Cuántas calcomanías tiene la persona?", ["Busco I have.", "Escucho el número: fifteen.", "Fifteen es 15."], "15"),
        ("Un lugar", ADULT + "«The ball is on the table.» (table = mesa). ¿Dónde está la pelota?", ["Busco el lugar: on.", "On significa sobre.", "La pelota está sobre la mesa."], "Sobre la mesa"),
    ],
    [
        ("Confundir sixteen con seventeen.", "No se escuchó la parte del medio del número.", "Escucha el comienzo: six y seven son distintos; el final «-teen» es igual."),
        ("Pensar que in y on significan lo mismo.", "Se mezcla dentro con sobre.", "In es dentro de algo y on es encima de algo."),
    ],
    [
        (ADULT + "«I have fifteen stickers.» ¿Cuántas calcomanías hay?", "15", "Fifteen significa quince."),
        (ADULT + "«The ball is on the table.» ¿Dónde está la pelota?", "Sobre la mesa", "On significa sobre."),
        (ADULT + "«The book is in the box.» (box = caja). ¿Dónde está el libro?", "Dentro de la caja", "In significa dentro de."),
    ],
    [
        ("¿Qué significa «under»?", "Debajo de", "Under indica un lugar bajo algo."),
        ("¿Qué significa «There are twelve pencils»?", "Hay doce lápices", "There are dice que hay varios."),
        ("¿Qué número es seventeen?", "17", "Seventeen es diecisiete."),
    ],
    [
        (ADULT + "«Mia has nineteen marbles.» (marbles = bolitas). ¿Cuántas bolitas tiene Mia?", "19", "Nineteen significa diecinueve."),
        (ADULT + "«The cat is under the chair.» (cat = gato). ¿Dónde está el gato?", "Debajo de la silla", "Under significa debajo de."),
        (ADULT + "«There are fourteen books on the table.» ¿Cuántos libros hay y dónde?", "14 libros sobre la mesa", "Fourteen es 14 y on the table es sobre la mesa."),
    ],
    [
        ("Leo oyó «sixteen» y escribió 15. ¿Se equivocó?", "Sí, sixteen es 16", "Sixteen es dieciséis, no quince."),
        (ADULT + "«I have twelve pencils. Mia has twenty pencils.» ¿Quién tiene más lápices?", "Mia", "Veinte es mayor que doce."),
    ],
    [
        arith(ADULT + "«Leo has twelve stickers. Mia has seven stickers.» ¿Cuántas calcomanías tienen en total?", "12+7", "Se suman las calcomanías de los dos niños."),
        (ADULT + "«The ball is in the box. The box is under the table.» ¿Dónde está la caja?", "Debajo de la mesa", "The box is under the table dice dónde está la caja."),
    ],
    [(ADULT + "En la sala hay un gato: «There are eighteen chairs. There is a cat under a chair.» ¿Cuántas sillas hay?", "18", "Eighteen significa dieciocho.")],
    [
        ("¿Cómo se dice «veinte» en inglés?", "twenty", "Twenty es el número 20."),
        (ADULT + "«I have thirteen pencils.» ¿Cuántos lápices?", "13", "Thirteen significa trece."),
        ("¿Qué significa «on»?", "Sobre", "On indica un lugar encima de algo."),
    ],
    task("Un adulto lee dos veces: «There are twelve pencils on the table. There is a book in the box. The ball is under the chair.» Dibuja una mesa con 12 lápices, una caja con un libro y una pelota debajo de una silla. Escribe debajo de cada dibujo el lugar: on, in, under.", "Mesa con 12 lápices (on), caja con libro (in) y pelota bajo la silla (under).", ["dibuja 12 lápices sobre la mesa", "pone el libro dentro de la caja", "pone la pelota debajo de la silla"], ["dibujo", "nota del adulto"], ["dibujar menos o más de doce lápices", "intercambiar on con under"], "Reconoce el lugar correcto y vuelve a escuchar solo la parte que no coincide."),
    "Pide a un adulto que diga «eleven, twelve, thirteen» y cuenta con los dedos y los de otra persona.",
    "Escribe en inglés cuántos lápices o cuadernos hay en tu mochila (hasta veinte) y dónde está tu estuche con in, on o under.",
)

lesson(
    OA2, 4,
    "Las escenas escritas en cada ejercicio, que lee un adulto en voz alta; lápiz y espacio para mover el cuerpo.",
    "Aprenderé a entender lo que alguien está haciendo ahora mismo, con verbos que terminan en -ing. Sirve para entender qué pasa en el momento en que se habla.",
    ["Sé que run, jump, eat y read son acciones.", "Sé que Ana y Ben son nombres de personas."],
    [
        "Para decir lo que está pasando ahora se usa am, is o are y un verbo que termina en -ing. «I'm running» significa «estoy corriendo». «Ana is reading» significa «Ana está leyendo». «They are playing» significa «ellos están jugando». Right now significa «ahora mismo».",
        "Verbos de hoy: running (corriendo), jumping (saltando), reading (leyendo), eating (comiendo), drawing (dibujando), swimming (nadando), sleeping (durmiendo) y playing (jugando). Fíjate en que run y swim doblan la última letra: running y swimming.",
        "Para preguntar se dice «What is Ana doing?» (¿qué está haciendo Ana?). Se responde «She is reading» (ella está leyendo). They significa «ellos» o «ellas» y habla de más de una persona. Si no oyes -ing, la frase puede hablar de otra cosa, por ejemplo «I can run» dice lo que puedo hacer y no lo que hago ahora.",
    ],
    [("-ing", "terminación de lo que pasa ahora"), ("running / jumping", "corriendo / saltando"), ("reading / eating", "leyendo / comiendo"), ("drawing / swimming", "dibujando / nadando"), ("sleeping / playing", "durmiendo / jugando"), ("They are", "ellos están"), ("What is Ana doing?", "¿qué está haciendo Ana?")],
    [
        ("Una acción ahora", ADULT + "«I'm running.» ¿Qué hace la persona ahora?", ["Busco la terminación -ing.", "Oigo running.", "Running significa corriendo."], "Corre"),
        ("Pregunta y respuesta", ADULT + "«A: What is Mia doing? B: She is drawing.» (she = ella). ¿Qué hace Mia?", ["La pregunta pregunta por Mia.", "La respuesta dice drawing.", "Drawing significa dibujando."], "Dibuja"),
    ],
    [
        ("Pensar que «I can run» dice lo que hago ahora.", "Se confunde la habilidad con la acción que ocurre en este momento.", "Busca -ing: running es ahora y can run dice lo que sé hacer."),
        ("Decir que «They are playing» habla de una persona.", "No se entiende la palabra they.", "They significa ellos y se usa para más de una persona."),
    ],
    [
        (ADULT + "«I'm running.» ¿Qué hace?", "Corre", "Running es correr ahora."),
        (ADULT + "«Ana is reading.» ¿Qué hace Ana?", "Lee", "Reading significa leyendo."),
        (ADULT + "«Ben is sleeping.» ¿Qué hace Ben?", "Duerme", "Sleeping significa durmiendo."),
    ],
    [
        ("¿Qué indica que un verbo termine en -ing?", "Que la acción ocurre ahora mismo", "El final -ing sirve para lo que está pasando."),
        ("¿Qué significa «What is Ana doing?»", "¿Qué está haciendo Ana?", "What is doing pregunta por una acción ahora."),
        ("¿Cuál frase dice lo que pasa ahora: «I can swim» o «I'm swimming»?", "I'm swimming", "Swimming termina en -ing."),
    ],
    [
        (ADULT + "«Leo is eating an apple.» (apple = manzana). ¿Qué come Leo?", "Una manzana", "Eating an apple significa comiendo una manzana."),
        (ADULT + "«They are playing.» (they = ellos). ¿Habla de una persona o de varias?", "De varias", "They es ellos."),
        (ADULT + "«A: What is Mia doing? B: She is drawing.» ¿Qué hace Mia ahora?", "Dibuja", "Drawing significa dibujando."),
    ],
    [
        ("Pedro oyó «I can run» y dijo que la persona corre ahora. ¿Qué entendió mal?", "Que can run dice lo que puede hacer, no lo que hace ahora", "Para ahora hay que oír running."),
        (ADULT + "«Sam is drawing. Ana is jumping.» ¿Quién salta?", "Ana", "Ana is jumping significa Ana está saltando."),
    ],
    [
        (ADULT + "«Ana is jumping. Ben is reading. Lia is swimming. Tom is sleeping.» ¿Quién está nadando?", "Lia", "Lia is swimming dice que Lia nada."),
        (ADULT + "«What is Lia doing? She is reading. What is Ben doing? He is running.» (she = ella, he = él). ¿Qué dos acciones se dicen?", "Leer y correr", "Reading es leyendo y running es corriendo."),
    ],
    [(ADULT + "En el parque, alguien dice: «Look! Ana is jumping. Ben is running. Lia is eating.» (look = mira) ¿Quién está comiendo?", "Lia", "Lia is eating significa Lia come ahora.")],
    [
        ("¿Qué significa «sleeping»?", "Durmiendo", "Sleeping es la acción de dormir ahora."),
        (ADULT + "«Mia is swimming.» ¿Qué hace Mia?", "Nada", "Swimming es nadar."),
        ("¿Cómo se dice «ahora mismo» en inglés?", "right now", "Right now indica el momento presente."),
    ],
    task("Un adulto lee dos veces: «Ana is jumping. Ben is reading. Lia is eating. Tom is sleeping.» Haz una mímica de cada acción, sin hablar, en un espacio seguro. Luego di en inglés una de las acciones con -ing, por ejemplo jumping.", "Mima saltar, leer, comer y dormir, y dice jumping.", ["hace las cuatro mímicas", "dice una acción con -ing", "relaciona cada acción con el nombre correcto"], ["nota del adulto", "foto o video con permiso de la familia"], ["mimar I can en vez de ahora", "olvidar una de las acciones"], "Reconoce las mímicas correctas y repite despacio, con él, la terminación -ing."),
    "Pide a un adulto que diga «jumping, reading, eating» y haz una mímica de cada una.",
    "Escribe tres frases sobre lo que hacen tres personas ahora, por ejemplo «Ana is reading».",
)

lesson(
    OA2, 5,
    "Seis textos orales cortos escritos en los ejercicios, que lee un adulto en voz alta; lápiz y hoja para tapar el guion.",
    "Aprenderé a reconocer de qué tema habla un texto oral y para qué lo dice la persona. Sirve para entender mejor lo que se escucha.",
    ["Conozco palabras de la escuela y de la casa.", "Sé seguir instrucciones, entender sentimientos y números hasta veinte."],
    [
        "El tema (topic) es de qué se habla. Los temas de esta clase son: la escuela (school), los animales salvajes (wild animals), la casa y los muebles (house), las figuras (shapes), las ocupaciones (jobs), la comida (food) y una celebración (Easter). Easter es la Pascua, una celebración cristiana que no todas las familias celebran. Las figuras son circle (círculo), square (cuadrado) y triangle (triángulo). Los lugares de la ciudad son park (parque) y library (biblioteca).",
        "El propósito (purpose) es para qué habla la persona. Puede dar instrucciones («Open your book»), presentarse («I'm Mr. Rojas»), decir lo que puede hacer o cómo se siente («I'm happy»), decir cuántas cosas hay o dónde están («There are four monkeys in the tree»), o decir lo que pasa ahora («Leo is eating»).",
        "Para reconocer el tema, escucha el objeto o el animal que se nombra (monkeys, egg, ball). Para reconocer el propósito, escucha la estructura: una palabra de acción al principio es una instrucción, I'm o This is es presentarse, There are dice cuántos hay, y -ing dice lo que pasa ahora.",
    ],
    [("topic", "tema"), ("purpose", "propósito"), ("school / jobs", "escuela / ocupaciones"), ("wild animals", "animales salvajes"), ("food", "comida"), ("Easter", "Pascua"), ("monkey / egg / cook", "mono / huevo / cocinero")],
    [
        ("Tema y propósito", ADULT + "«Open your book. Look at the board.» ¿De qué tema habla (escuela o comida) y para qué (dar instrucciones o presentarse)?", ["Veo las palabras book y board: es la escuela.", "Las dos frases empiezan con una acción.", "Eso es dar instrucciones."], "Escuela, para dar instrucciones"),
        ("Cuántos y dónde", ADULT + "«There are four monkeys in the tree.» (monkeys = monos, tree = árbol). ¿Cuál es el propósito?", ["Oigo There are y el número four.", "Oigo in the tree: dice dónde están.", "El propósito es decir cuántos son y dónde están."], "Decir cuántos monos hay y dónde están"),
    ],
    [
        ("Confundir tema con propósito.", "El tema es de qué se habla y el propósito es para qué se habla.", "Pregúntate: ¿de qué cosas habla (tema)? y ¿para qué lo dice (propósito)?"),
        ("Pensar que cualquier texto con un nombre es una presentación.", "Una presentación necesita I'm o This is.", "Busca I'm o This is para saber si alguien se presenta."),
    ],
    [
        (ADULT + "«Open your book. Look at the board.» ¿El tema es la escuela o la comida?", "La escuela", "Book y board son cosas de la escuela."),
        (ADULT + "«There are four monkeys in the tree.» ¿Qué animales aparecen?", "Monos", "Monkeys significa monos."),
        (ADULT + "«The ball is under the chair.» ¿Dónde está la pelota?", "Debajo de la silla", "Under the chair significa debajo de la silla."),
    ],
    [
        ("¿Qué es el tema de un texto oral?", "De qué se habla", "El tema se reconoce por las cosas que se nombran."),
        ("¿Qué es el propósito de un texto oral?", "Para qué habla la persona", "Puede ser instruir, presentarse, describir o contar lo que pasa."),
        ("¿Qué significa «Happy Easter»?", "Feliz Pascua", "Es un saludo para una celebración."),
    ],
    [
        (ADULT + "«Hello! I'm Mr. Rojas. I'm a cook.» (Mr. = señor, cook = cocinero). ¿El propósito es presentarse o dar una instrucción?", "Presentarse", "I'm Mr. Rojas es una presentación."),
        (ADULT + "«Leo is eating bread. Mia is drinking milk.» (bread = pan, drinking = tomando, milk = leche). ¿Dice lo que pasa ahora o lo que alguien puede hacer?", "Lo que pasa ahora", "Eating y drinking terminan en -ing."),
        (ADULT + "«Happy Easter! I have two chocolate eggs.» (eggs = huevos). ¿Qué celebración se menciona?", "Easter (Pascua)", "Se oye Easter en el saludo."),
    ],
    [
        ("Una niña oyó «Look at the board» y dijo que el propósito es presentarse. ¿Tiene razón?", "No; el propósito es dar una instrucción", "Look at empieza con una acción, sin I'm ni This is."),
        (ADULT + "«There are four monkeys in the tree.» ¿El propósito es saludar o decir cuántos hay y dónde están?", "Decir cuántos hay y dónde están", "There are cuatro y in the tree dan esa información."),
    ],
    [
        ("Textos: A «Open your book.» B «I'm Mr. Rojas, I'm a cook.» C «The ball is under the chair.» Temas: 1 la escuela, 2 las ocupaciones, 3 la casa y los muebles. Une cada texto con su tema.", "A1, B2, C3", "Book es escuela, cook es ocupación y chair es mueble."),
        arith(ADULT + "«Mia has four eggs. Leo has three eggs.» (has = tiene). ¿Cuántos huevos hay en total?", "4+3", "Se suman los huevos de Mia y los de Leo."),
    ],
    [(ADULT + "Una niña dice: «Hello! I'm Ana. This is my friend Leo.» ¿Cuál es el propósito de lo que dice?", "Presentarse y presentar a otra persona", "I'm y This is sirven para presentar.")],
    [
        (ADULT + "«The triangle is on the table.» (triangle = triángulo, table = mesa). ¿Qué figura se nombra?", "Un triángulo", "Triangle es la figura de tres lados."),
        (ADULT + "«The library is big.» (library = biblioteca, big = grande). ¿Qué lugar de la ciudad se nombra?", "La biblioteca", "Library es el lugar donde hay libros."),
        (ADULT + "«Close your book.» ¿Es una instrucción o una presentación?", "Una instrucción", "Close es una palabra de acción al principio."),
    ],
    task("Un adulto lee dos veces estos dos textos: A «Open your book, please.» B «There are four monkeys in the tree.» Para cada texto, dibuja una cosa que aparece y escribe en una hoja la letra A o B. Luego di su tema (escuela o animales) y su propósito (dar instrucción o decir cuántos hay).", "A: libro, escuela, instrucción. B: cuatro monos, animales, cuántos hay y dónde.", ["dibuja un libro para A y cuatro monos para B", "dice los temas correctos", "dice los propósitos correctos"], ["dibujos con letras", "nota del adulto"], ["intercambiar los textos A y B", "confundir tema con propósito"], "Reconoce la parte correcta y vuelve a leer con él el texto que confundió."),
    "Pide a un adulto que diga «Close your book» y «I'm Ana» y señala cuál es una instrucción y cuál una presentación.",
    "Escribe un texto corto con un tema (por ejemplo comida) y un propósito (por ejemplo decir cuántas cosas hay).",
)
