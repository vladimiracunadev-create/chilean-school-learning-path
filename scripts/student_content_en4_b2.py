"""Cuaderno del estudiante, 4.º básico Inglés: EN04 OA 11 (interacción breve y presentación) y OA 12 (expresión oral con apoyo).

Los diálogos y tarjetas en inglés son originales y llevan pista en español. Las imágenes se describen entre corchetes.
Los personajes son inventados: nunca se piden ni se dan datos privados. La persona de tu casa lee el otro papel.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_en4_b import lesson
from student_lessons import arith

OA11, OA12 = "EN04 OA 11", "EN04 OA 12"

# ================================================================ OA 11
lesson(
    OA11, 1,
    "Los diálogos escritos en cada ejercicio, un lápiz y una goma, y una persona de tu casa que haga el otro papel.",
    "Aprenderé a hacer y responder pedidos simples de la sala de clases en inglés, con cortesía. Sirve para pedir un objeto o ayuda y responder a quien me lo pide.",
    ["Sé decir hello y thank you.", "Sé nombres de objetos de la sala como pencil, eraser y ruler."],
    [
        "Un pedido (request) es una frase para pedir algo. En la sala de clases se usa «Can I have a pencil, please?» (¿puedo tener un lápiz, por favor?) y «Can you help me, please?» (¿puedes ayudarme, por favor?). La palabra please (por favor) hace el pedido más amable.",
        "Quien recibe el pedido responde. Si dice que sí: «Sure» (claro) o «Yes, here you are» (sí, aquí tienes). Si no puede: «Sorry, I don't have one» (lo siento, no tengo uno). Quien recibe el objeto dice «Thank you» y la otra persona responde «You're welcome» (de nada).",
        "En una conversación se habla por turnos (turns): primero una persona, luego la otra. Un diálogo breve de clase tiene cuatro turnos: pedido, respuesta, agradecimiento y respuesta al agradecimiento. Puedes apoyarte con el objeto y un gesto: por ejemplo, mostrar la mano abierta al pedir un lápiz.",
    ],
    [("request", "pedido"), ("please", "por favor"), ("Can I have...?", "¿puedo tener...?"), ("Here you are.", "aquí tienes"), ("You're welcome.", "de nada"), ("turn", "turno")],
    [
        ("Hacer un pedido", "Necesitas una goma (eraser). ¿Cómo la pides con cortesía?", ["Empiezo con Can I have.", "Digo el objeto: an eraser.", "Termino con please."], "Can I have an eraser, please?"),
        ("Armar un diálogo", "Ordena un diálogo de cuatro turnos con estos papeles: pides una regla (ruler), te la dan, agradeces, responden. ¿Cuáles son las frases?", ["Turno 1: el pedido.", "Turno 2: la respuesta Here you are.", "Turnos 3 y 4: Thank you y You're welcome."], "A: Can I have a ruler, please? B: Here you are. A: Thank you. B: You're welcome."),
    ],
    [
        ("Pedir un objeto sin usar please ni Can I.", "El pedido suena poco amable y confuso.", "Empieza con Can I have y termina con please."),
        ("No responder al agradecimiento.", "La conversación queda incompleta.", "Responde You're welcome cuando te dicen Thank you."),
    ],
    [
        ("¿Qué significa «please»?", "Por favor", "Please hace el pedido más amable."),
        ("¿Qué significa «Here you are»?", "Aquí tienes", "Se dice al entregar algo."),
        ("Te dicen «Thank you». ¿Qué respondes en inglés?", "You're welcome", "You're welcome significa de nada."),
    ],
    [
        ("Elige la frase que es un pedido: (a) «Can I have a pencil, please?» (b) «I have a pencil.»", "a", "Solo (a) pide algo."),
        ("Te preguntan «Can you help me, please?». Elige la mejor respuesta: (a) «Sure.» (b) «Blue.»", "a", "Sure significa claro y acepta ayudar."),
        ("Tu compañero no tiene lápiz extra. Elige lo que dice: (a) «Sorry, I don't have one.» (b) «You're welcome.»", "a", "Sorry, I don't have one explica que no puede."),
    ],
    [
        ("Completa el pedido: «Can I ___ a ruler, please?» (tener)", "have", "Can I have significa puedo tener."),
        ("Completa la entrega: «___ you are.» (aquí)", "Here", "Here you are significa aquí tienes."),
        ("Escribe tu pedido para pedir un lápiz con cortesía. Usa Can I have y please.", "Can I have a pencil, please?", "Un pedido amable lleva Can I have y please."),
    ],
    [
        ("Ana dice «Give me a pencil». ¿Qué falta para que sea un pedido amable? Responde en español.", "Can I have y please", "La frase amable pregunta con Can I have y agrega please."),
        ("Luis recibe una goma y no dice nada. ¿Qué debería decir? Responde en inglés.", "Thank you", "Se agradece después de recibir algo."),
    ],
    [
        ("Ordena las palabras para formar un pedido: please / Can / help / you / me. Escríbelo.", "Can you help me, please?", "El pedido empieza con Can you."),
        ("Ordena los turnos con los números: (1) «Thank you.» (2) «Can I have a pencil, please?» (3) «Here you are.» Escribe los números.", "2, 3, 1", "Primero pides, luego te dan y por último agradeces."),
    ],
    [("Estás en la clase de arte y necesitas el pegamento (glue), pero tu compañero lo está usando. Elige la mejor frase para pedirlo después: (a) «Can I have the glue, please?» (b) «Give glue.»", "a", "La frase (a) es amable y completa.")],
    [
        ("¿Cómo se dice «de nada» en inglés?", "You're welcome", "Se responde a Thank you."),
        ("¿Qué significa «turn» en una conversación?", "Turno", "Se habla por turnos."),
        ("¿Qué significa «Can you help me, please?»", "¿Puedes ayudarme, por favor?", "Es un pedido de ayuda amable."),
    ],
    task("Con una persona de tu casa, representen tres pedidos de sala de clases usando objetos reales: (1) Can I have a pencil, please? (2) Can I have an eraser, please? (3) Can you help me, please? Una persona pide y la otra responde con Sure, Here you are o Sorry, I don't have one. Cada pedido termina con Thank you y You're welcome. Luego cambian de papel.", "A: Can I have a pencil, please? B: Here you are. A: Thank you. B: You're welcome.", ["los tres pedidos usan Can I have/Can you y please", "las respuestas encajan con el pedido", "agradece y responde al agradecimiento", "habla por turnos, sin interrumpir"], ["nota de la persona que hizo el otro papel", "los objetos usados"], ["no usar please", "no responder al agradecimiento"], "La otra persona señala el pedido que sonó más amable y se repite el que costó."),
    "Pide en voz alta un objeto de tu mesa con Can I have y please.",
    "Escribe un diálogo de cuatro turnos para pedir una hoja de papel y practícalo.",
)

lesson(
    OA11, 2,
    "Las dos tarjetas de personajes inventados escritas en esta clase, lápiz y una persona de tu casa que escuche.",
    "Aprenderé a presentar a una persona inventada con frases cortas en inglés, usando He o She. Sirve para hablar de otras personas sin dar datos privados.",
    ["Sé decir My name is... e I like...", "Sé que he es «él» y she es «ella» en inglés."],
    [
        "Cuando presentas a otra persona, dices «This is Ben» (este es Ben). Después usas he (él) para un niño o she (ella) para una niña. Con una tarjeta (card) de datos puedes decir cuatro cosas: nombre, edad, país y un gusto.",
        "Fíjate en los verbos. Con I decimos «I am» o «I like», pero con he o she decimos is y likes: «He is ten», «She is from Peru», «He likes soccer», «She likes painting». También sirve «He can swim» (él sabe nadar): después de can el verbo no cambia.",
        "Presentar a una persona inventada es seguro: usamos solo nombre de pila, edad, país y gustos. Nunca damos dirección, teléfono ni el nombre del colegio de una persona real. Una buena presentación va en orden: This is..., edad, país, gusto y una habilidad. Para preguntar la edad de otra persona: «How old is he?» (¿cuántos años tiene él?) o «How old is she?». Si hablas de ti mismo, usas I'm: «I'm Ben. I'm ten» (soy Ben, tengo diez años).",
    ],
    [("This is...", "este/esta es..."), ("he", "él"), ("she", "ella"), ("He/She is...", "él/ella es o tiene (edad)..."), ("likes", "le gusta"), ("can swim", "sabe nadar")],
    [
        ("Presentar a Ben", "Tarjeta: Ben, 10 años, Chile, le gusta el fútbol (soccer), sabe nadar. ¿Cómo lo presentas en cinco frases?", ["Empiezo con This is Ben.", "Uso he con is para edad y país.", "Uso likes y can para el gusto y la habilidad."], "This is Ben. He is ten. He is from Chile. He likes soccer. He can swim."),
        ("Cambiar a she", "Tarjeta: Ana, 9 años, Perú, le gusta pintar (painting). ¿Cómo dices su edad y su gusto?", ["Es una niña, uso she.", "Para la edad uso is.", "Para el gusto uso likes."], "She is nine. She likes painting."),
    ],
    [
        ("Decir «He like soccer».", "Con he o she el verbo like lleva s.", "Di He likes soccer."),
        ("Usar he para una niña.", "Se confunde el pronombre.", "Usa she para una niña y he para un niño."),
    ],
    [
        ("¿Qué significa «This is Ben»?", "Este es Ben", "This is presenta a una persona."),
        ("¿Qué pronombre usas para Ana, una niña: he o she?", "she", "She es para niñas."),
        ("¿Qué significa «He can swim»?", "Él sabe nadar", "Can swim significa sabe nadar."),
    ],
    [
        ("Tarjeta de Ben: 10 años. ¿Qué oración dice su edad? (a) «He is ten.» (b) «He likes ten.»", "a", "Para la edad se usa is."),
        ("Tarjeta de Ana: Perú. Elige la oración correcta: (a) «She is from Peru.» (b) «He is from Peru.»", "a", "Ana es una niña, entonces se usa she."),
        ("Tarjeta de Ben: soccer. Elige: (a) «He likes soccer.» (b) «He like soccer.»", "a", "Con he el verbo lleva s: likes."),
    ],
    [
        ("Completa: «Ana ___ from Peru.» Opciones: is / like.", "is", "Is se usa con she y con Ana."),
        ("Completa: «Ben ___ soccer.» Opciones: likes / like.", "likes", "Con he el verbo lleva s."),
        ("Tarjeta de Ana: sabe cantar (sing). Escribe la oración en inglés con can.", "She can sing.", "Can va seguido del verbo sin cambios."),
    ],
    [
        ("Tarjeta de Ben: 10 años, Chile. Alguien dice «Ben is nine». ¿Cómo lo corriges? Responde en inglés.", "Ben is ten.", "La tarjeta dice 10 años."),
        ("¿Cuál de estos datos NO es seguro para presentar a una persona? (a) la edad (b) la dirección de su casa", "b", "La dirección es un dato privado."),
    ],
    [
        ("Ordena para formar una oración sobre Ana: from / is / She / Peru. Escríbela.", "She is from Peru.", "Primero va el pronombre y luego is."),
        ("Ben se presenta él mismo ante la clase. Elige lo que dice: (a) «I'm Ben. I'm ten.» (b) «He is Ben. He is ten.»", "a", "Cuando hablas de ti mismo usas I'm."),
    ],
    [("En el club de inglés presentas a un personaje de un libro, Leo, de 8 años, que sabe dibujar (draw). Elige la oración que dice lo que sabe hacer: (a) «He can draw.» (b) «He is draw.»", "a", "Después de can el verbo no cambia.")],
    [
        ("¿Cómo se dice «ella» en inglés?", "she", "She es para niñas y mujeres."),
        ("¿Qué datos son seguros para presentar a alguien?", "Nombre de pila, edad, país y gustos", "No muestran dónde vive."),
        ("¿Cómo se dice «le gusta la música» de Ana?", "She likes music", "Con she el verbo lleva s."),
    ],
    task("Con una persona de tu casa, presenten a dos personajes inventados. Tarjeta 1: Ben, 10 años, Chile, le gusta el fútbol (soccer), sabe nadar (swim). Tarjeta 2: Ana, 9 años, Perú, le gusta pintar (painting), sabe cantar (sing). Cada una de ustedes presenta una tarjeta con cinco frases en inglés, y la otra persona hace una pregunta: «How old is he/she?». Después cambian de tarjeta.", "«This is Ana. She is nine. She is from Peru. She likes painting. She can sing.»", ["empieza con This is...", "usa he o she correctamente", "usa is, likes y can bien", "no inventa datos privados"], ["nota de la persona que escuchó las dos presentaciones"], ["decir He like", "mezclar he y she"], "La otra persona dice qué dato entendió y se repite el que costó."),
    "Di en inglés tres cosas sobre un personaje de dibujos animados, usando he o she.",
    "Inventa una tarjeta de un personaje con nombre, edad, país, gusto y habilidad y preséntalo en cinco frases.",
)

lesson(
    OA11, 3,
    "Las frases escritas en cada ejercicio, lápiz y una persona de tu casa para practicar preguntas y respuestas.",
    "Aprenderé a pedir ayuda cuando no sé una palabra en inglés, con frases como «How do you say...?» y «Can you repeat?». Sirve para seguir conversando sin quedarme en silencio.",
    ["Sé usar please en un pedido.", "Sé el nombre de las letras del abecedario en español."],
    [
        "Nadie conoce todas las palabras de un idioma. Cuando falta una, puedes pedirla. Para saber cómo se dice en inglés una palabra del español, pregunta «How do you say ventana in English?» (¿cómo se dice ventana en inglés?). La respuesta es «Window».",
        "Otras preguntas útiles: «How do you spell it?» (¿cómo se deletrea?), «What does window mean?» (¿qué significa window?) y «Can you repeat, please?» (¿puedes repetir, por favor?). Si no entendiste, di «Sorry, I don't understand» (lo siento, no entiendo). Si no sabes la palabra, di «I don't know the word» (no sé la palabra).",
        "Deletrear (spell) es decir las letras de una palabra una por una. Window se deletrea W-I-N-D-O-W. Para que te entiendan, hazlo despacio y haz una pausa corta entre letras. Estas frases se usan también para hablar de otras asignaturas, por ejemplo de nombres de animales o de lugares. Las letras tienen en inglés nombres distintos de los del español: para decirlas en voz alta con buena pronunciación, aprende el abecedario inglés con tu profesor o con un audio. En este cuaderno practicas escribiendo las letras separadas por guiones.",
    ],
    [("How do you say...?", "¿cómo se dice...?"), ("How do you spell it?", "¿cómo se deletrea?"), ("What does... mean?", "¿qué significa...?"), ("Can you repeat?", "¿puedes repetir?"), ("I don't understand.", "no entiendo"), ("spell", "deletrear")],
    [
        ("Preguntar una palabra", "No sabes decir «silla» en inglés. ¿Qué preguntas?", ["Uso How do you say.", "Digo la palabra en español.", "Termino con in English."], "How do you say silla in English?"),
        ("Pedir ayuda cuando no entiendes", "Una persona te dice una palabra rápido y no la entiendes. ¿Qué dices?", ["Digo Sorry para empezar.", "Pido que repita.", "Agrego please."], "Sorry, can you repeat, please?"),
    ],
    [
        ("Quedarse en silencio cuando no se sabe una palabra.", "La conversación se detiene.", "Pide ayuda con How do you say...?"),
        ("Fingir que se entendió cuando no se entendió.", "Hay más confusión después.", "Di Sorry, I don't understand."),
    ],
    [
        ("¿Qué significa «How do you say...?»", "¿Cómo se dice...?", "Se usa para pedir una palabra en inglés."),
        ("¿Qué significa «Can you repeat, please?»", "¿Puedes repetir, por favor?", "Sirve cuando no entendí."),
        ("¿Qué significa «spell»?", "Deletrear", "Spell es decir las letras una por una."),
    ],
    [
        ("Quieres saber cómo se escribe window letra por letra. Elige la pregunta: (a) «How do you spell window?» (b) «Where is window?»", "a", "How do you spell... pregunta por las letras."),
        ("Alguien dice «Window» y quieres saber qué significa. Elige: (a) «What does window mean?» (b) «Can I have window?»", "a", "What does... mean pregunta el significado."),
        ("No sabes la palabra que necesitas. Elige lo que dices: (a) «I don't know the word.» (b) «You're welcome.»", "a", "I don't know the word explica que falta la palabra."),
    ],
    [
        ("Completa: «How do you ___ ventana in English?» (decir)", "say", "How do you say pregunta cómo se dice."),
        ("Deletrea cat en letras separadas por guiones. Escribe la respuesta con guiones.", "C-A-T", "Cat tiene tres letras: C, A y T."),
        ("Completa: «Sorry, I don't ___.» (entender)", "understand", "I don't understand significa no entiendo."),
    ],
    [
        ("Luis dice solo «Ventana?» y la otra persona no sabe qué quiere. ¿Qué frase debe usar? Responde en inglés.", "How do you say ventana in English?", "La frase completa pregunta por la palabra en inglés."),
        ("Ana dice «Repeat!» con enojo. ¿Qué cambias para que sea amable? Responde en español.", "Digo Can you repeat, please?", "La frase amable lleva Can you y please."),
    ],
    [
        ("Ordena las palabras para formar la pregunta: spell / do / How / you / it. Escríbela.", "How do you spell it?", "La pregunta empieza con How do you."),
        ("Deletrea dog separando las letras con guiones. Escribe la respuesta.", "D-O-G", "Dog tiene D, O y G."),
    ],
    [("En la clase de ciencias quieres decir «hormiga» en inglés, pero no sabes la palabra. Elige tu pregunta: (a) «How do you say hormiga in English?» (b) «What does ant mean?»", "a", "La pregunta (a) pide la palabra en inglés para hormiga.")],
    [
        ("¿Cómo se dice «no entiendo» en inglés?", "I don't understand", "Es la frase para decir que no entendí."),
        ("¿Qué significa «What does window mean?»", "¿Qué significa window?", "Pregunta el significado de una palabra."),
        ("¿Qué hago cuando falta una palabra?", "Pido ayuda con How do you say...?", "Así sigo conversando."),
    ],
    task("Con una persona de tu casa, practiquen este diálogo con las palabras window, door y table. A: «How do you say ventana in English?» B: «Window.» A: «How do you spell it?» B: «W-I-N-D-O-W.» A: «Thank you.» Luego repitan con door (puerta) y table (mesa). Una persona puede decir «Sorry, can you repeat, please?» una vez en cada vuelta y la otra repite más despacio.", "A: How do you say mesa in English? B: Table. A: How do you spell it? B: T-A-B-L-E.", ["usa How do you say...? para pedir cada palabra", "deletrea bien las tres palabras", "pide repetir una vez con cortesía", "habla despacio y por turnos"], ["nota de la persona que deletreó contigo", "las tres palabras con su deletreo escrito"], ["olvidar una letra al deletrear", "pedir repetir sin please"], "La otra persona comprueba el deletreo y se practican de nuevo las letras que costaron."),
    "Pregunta en voz alta cómo se dice «lápiz» en inglés y deletrea la respuesta.",
    "Escribe cinco palabras en español que no sepas en inglés y escribe la pregunta que harías para cada una.",
)

lesson(
    OA11, 4,
    "La tarjeta de datos escrita en esta clase (delfines), papel y lápiz para dibujar un apoyo, y una persona de tu casa como público.",
    "Aprenderé a hacer una presentación breve en inglés, de unos treinta segundos, apoyada en una imagen. Sirve para compartir un tema de otra asignatura, como Ciencias, con frases simples.",
    ["Sé presentar a una persona con This is, He y She.", "Sé preguntar cómo se dice una palabra."],
    [
        "Una presentación breve (brief presentation) tiene partes en orden. Primero un saludo y el tema: «Hello! My topic is dolphins» (hola, mi tema son los delfines). Luego dos o tres datos. Al final, un cierre: «Thank you. Any questions?» (gracias, ¿hay preguntas?).",
        "Datos de la clase de Ciencias sobre delfines (dolphins): «Dolphins live in the sea. They can swim fast. They eat fish.» (sea es mar; fast es rápido; fish es pez o pescado). Con varios animales se usa they (ellos) y se dice live y eat, sin s.",
        "Una imagen te ayuda a recordar: puedes dibujar un delfín en el mar y mostrarlo mientras hablas. También ayudan los gestos: mueve la mano como una ola cuando dices sea. Mira a tu público, habla despacio y practica tres veces antes de presentar. Cada dato debe ser cierto según la tarjeta.",
    ],
    [("presentation", "presentación"), ("dolphins", "delfines"), ("live", "viven"), ("sea", "mar"), ("fast", "rápido"), ("any questions?", "¿hay preguntas?")],
    [
        ("Armar la presentación", "Tarjeta: Dolphins live in the sea. They can swim fast. They eat fish. ¿Cómo empiezas y cómo terminas la presentación?", ["Empiezo con el saludo y el tema.", "Digo los tres datos.", "Cierro con Thank you y Any questions?"], "Hello! My topic is dolphins. ... Thank you. Any questions?"),
        ("Revisar un dato", "Alguien dice «Dolphins live in a tree». ¿Se puede decir en la presentación?", ["Busco el dato en la tarjeta.", "La tarjeta dice live in the sea.", "Corrijo la palabra tree."], "No; se corrige a «Dolphins live in the sea.»"),
    ],
    [
        ("Decir datos que no están en la tarjeta.", "La presentación puede tener errores.", "Usa solo los datos de la tarjeta."),
        ("Leer la tarjeta sin mirar al público.", "La presentación se vuelve difícil de seguir.", "Mira al público y apóyate en tu dibujo."),
    ],
    [
        ("¿Qué significa «dolphins»?", "Delfines", "Dolphins son animales del mar."),
        ("¿Qué significa «Any questions?»", "¿Hay preguntas?", "Se dice al final de la presentación."),
        ("¿Qué significa «fast»?", "Rápido", "Fast describe cómo nadan los delfines."),
    ],
    [
        ("Tarjeta: «Dolphins live in the sea.» ¿Dónde viven los delfines? Responde en español.", "En el mar", "Sea significa mar."),
        ("Ordena las partes de la presentación con los números: (1) datos (2) cierre (3) saludo y tema. Escribe los números en orden.", "3, 1, 2", "Primero saludo y tema, luego datos y al final el cierre."),
        ("Tarjeta: «They eat fish.» ¿Qué comen los delfines? Responde en español.", "Peces", "Fish significa pez o pescado."),
    ],
    [
        ("Completa con live: «Dolphins ___ in the sea.» Opciones: live / lives.", "live", "Con dolphins (varios) el verbo no lleva s."),
        ("Completa el dato: «They can swim ___.» (rápido en inglés)", "fast", "Fast es rápido."),
        ("Escribe en inglés tu saludo para empezar la presentación sobre delfines, de la forma «Hello! My topic is ___.»", "Hello! My topic is dolphins.", "El saludo incluye el tema de la presentación."),
    ],
    [
        ("Leo dice «Dolphins can fly». ¿Qué debe hacer? Responde en español.", "Corregirlo y decir que nadan", "La tarjeta dice que pueden nadar rápido, no volar."),
        ("Ema lee todo sin mirar al público y el público no la sigue. ¿Qué puede cambiar? Responde en español.", "Mirar al público y hablar con apoyo del dibujo", "Mirar y mostrar el dibujo ayuda al público."),
    ],
    [
        ("Elige la presentación completa y en orden: (a) «Hello! My topic is dolphins. Dolphins live in the sea. They eat fish. Thank you.» (b) «Thank you. They eat fish. Hello!»", "a", "La opción (a) tiene saludo, datos y cierre en orden."),
        ("¿Qué dibujo apoya mejor la presentación? Elige: (a) un delfín en el mar (b) un auto en la calle", "a", "El dibujo debe mostrar el tema."),
    ],
    [("En la feria de ciencias de tu curso presentas a los delfines en treinta segundos. Una persona del público quiere saber qué comen. Elige tu dato: (a) «They eat fish.» (b) «They eat grass.» (grass es pasto)", "a", "La tarjeta dice que comen fish.")],
    [
        ("¿Cómo se dice «mar» en inglés?", "sea", "Sea es mar."),
        ("¿Cómo termino una presentación?", "Con Thank you y Any questions?", "Es el cierre."),
        ("¿Qué parte va primero en la presentación?", "El saludo y el tema", "Así el público sabe de qué hablarás."),
    ],
    task("Prepara una presentación de treinta segundos sobre los delfines con esta tarjeta: «Dolphins live in the sea. They can swim fast. They eat fish.» Dibuja un delfín en el mar como apoyo. Practica tres veces. Preséntala a una persona de tu casa con saludo, tres datos y cierre, mostrando tu dibujo. Usa un gesto para sea y mira a tu público.", "«Hello! My topic is dolphins. They live in the sea. They can swim fast. They eat fish. Thank you. Any questions?»", ["tiene saludo, tres datos y cierre", "los datos coinciden con la tarjeta", "muestra el dibujo y usa un gesto", "habla despacio y mira al público"], ["el dibujo de apoyo", "nota del público con los tres datos que recordó"], ["decir un dato que no está en la tarjeta", "leer sin mirar"], "El público dice qué dato recordó y qué parte quedó más clara."),
    "Di en voz alta el saludo y el primer dato de la presentación frente a un espejo.",
    "Prepara con la misma estructura una presentación breve sobre otro animal que conozcas, usando solo datos que sepas con seguridad.",
)

lesson(
    OA11, 5,
    "La tarjeta de delfines de la clase anterior escrita en esta clase, papel y lápiz, y una persona de tu casa que haga preguntas.",
    "Aprenderé a responder preguntas de seguimiento después de una presentación, con frases breves y datos de mi tarjeta. Sirve para conversar con el público y adaptarme a lo que preguntan.",
    ["Sé hacer una presentación breve con apoyo.", "Sé pedir que repitan con Can you repeat, please?"],
    [
        "Después de una presentación, el público puede hacer preguntas de seguimiento (follow-up questions). Escucha la pregunta y responde con una frase breve. Para responder usa los datos de tu tarjeta: «Dolphins live in the sea. They can swim fast. They eat fish.»",
        "Preguntas posibles: «What do dolphins eat?» (¿qué comen?) se responde «They eat fish». «Where do they live?» (¿dónde viven?) se responde «They live in the sea». «Can they swim?» (¿pueden nadar?) se responde «Yes, they can». «Can they fly?» (¿pueden volar?) se responde «No, they can't».",
        "Si no entiendes, pide «Can you repeat the question, please?». Si no sabes la respuesta porque no está en tu tarjeta y no estás seguro, di «I don't know» (no sé) y no inventes. Si estás seguro de un dato simple, como que los delfines nadan y no vuelan, puedes responderlo. Para preguntas con Do they...?, responde «Yes, they do» o «No, they don't»: «Do they live in a tree?» se responde «No, they don't. They live in the sea». Responder con honestidad también es una buena respuesta. Mira a la persona que pregunta y habla con calma.",
    ],
    [("follow-up question", "pregunta de seguimiento"), ("What do they eat?", "¿qué comen?"), ("Where do they live?", "¿dónde viven?"), ("Yes, they can.", "sí, pueden"), ("No, they can't.", "no, no pueden"), ("I don't know.", "no sé")],
    [
        ("Responder con un dato de la tarjeta", "Te preguntan «What do dolphins eat?». ¿Qué respondes?", ["Busco el dato en la tarjeta.", "La tarjeta dice eat fish.", "Respondo con They eat."], "They eat fish."),
        ("Responder cuando el dato no está", "Te preguntan «What color are their babies?» y tu tarjeta no lo dice. ¿Qué dices?", ["Reviso la tarjeta.", "No encuentro el dato.", "Respondo con honestidad."], "I don't know."),
    ],
    [
        ("Inventar una respuesta cuando no se sabe.", "Se entrega información que puede ser falsa.", "Di I don't know si no está en tu tarjeta."),
        ("Responder con una frase que no tiene que ver con la pregunta.", "El público no recibe lo que pidió.", "Escucha la palabra de la pregunta y responde con ella."),
    ],
    [
        ("¿Qué significa «follow-up question»?", "Pregunta de seguimiento", "Es la pregunta que se hace después de una presentación."),
        ("¿Qué significa «I don't know»?", "No sé", "Es una respuesta honesta."),
        ("¿Qué significa «No, they can't»?", "No, no pueden", "Can't es la forma corta de cannot."),
    ],
    [
        ("Te preguntan «Where do they live?». Elige la respuesta de la tarjeta: (a) «They live in the sea.» (b) «They eat fish.»", "a", "Where pregunta por el lugar."),
        ("Te preguntan «Can they swim?». Elige la respuesta de la tarjeta: (a) «Yes, they can.» (b) «No, they can't.»", "a", "La tarjeta dice que nadan rápido."),
        ("¿Qué palabra de la pregunta indica que debes decir un lugar? Responde: What o Where.", "Where", "Where pregunta por el lugar."),
    ],
    [
        ("Completa: «They live ___ the sea.» (en)", "in", "In significa en o dentro de."),
        ("Te preguntan «Can they fly?». Responde con Yes o No y la frase corta completa.", "No, they can't.", "Los delfines nadan en el mar y no vuelan; es un dato seguro."),
        ("Te preguntan «What do they eat?». Escribe tu respuesta en inglés.", "They eat fish.", "La tarjeta dice eat fish."),
    ],
    [
        ("Ana no entendió la pregunta y respondió cualquier cosa. ¿Qué debió decir primero? Responde en inglés.", "Can you repeat the question, please?", "Se pide repetir cuando no se entiende."),
        ("Luis responde «Yes, they can» a la pregunta «Can they fly?». ¿Es correcto? Responde sí o no.", "No", "Los delfines nadan en el mar y no vuelan."),
    ],
    [
        ("Ordena las palabras para responder: eat / They / fish. Escribe la respuesta.", "They eat fish.", "Primero va They y luego el verbo."),
        ("Preguntan: «Do they live in a tree?». Elige tu respuesta correcta según la tarjeta: (a) «No, they live in the sea.» (b) «Yes, they do.»", "a", "La tarjeta dice que viven en el mar."),
    ],
    [("Después de tu presentación en la feria de ciencias, un niño pregunta: «Where do dolphins live?». Elige la mejor respuesta: (a) «They live in the sea.» (b) «They can swim fast.»", "a", "Responde la pregunta sobre el lugar.")],
    [
        ("¿Cómo se dice «¿dónde viven?» en inglés?", "Where do they live?", "Pregunta por el lugar."),
        ("¿Qué hago si no sé la respuesta?", "Digo I don't know", "Es mejor que inventar."),
        ("¿Qué hago si no entendí la pregunta?", "Pido que la repitan", "Así puedo responder bien."),
    ],
    task("Con una persona de tu casa, haz la presentación de los delfines (tarjeta: «Dolphins live in the sea. They can swim fast. They eat fish.») y luego responde estas cuatro preguntas que la persona te hace en cualquier orden: «What do they eat?», «Where do they live?», «Can they fly?» y «How old are they?». Responde con datos de la tarjeta. A la última responde con honestidad. Una vez pide «Can you repeat the question, please?».", "«They eat fish.» «They live in the sea.» «No, they can't.» «I don't know.»", ["responde con datos de la tarjeta", "dice I don't know cuando no está el dato", "pide repetir una vez con cortesía", "habla con calma y mira a la persona"], ["nota de la persona que hizo las preguntas"], ["inventar un dato", "no escuchar la palabra de la pregunta"], "La persona dice qué respuesta fue más clara y comprueban juntos los datos con la tarjeta."),
    "Di en voz alta las respuestas a «What do they eat?» y «Where do they live?».",
    "Escribe tres preguntas de seguimiento que podrían hacerte sobre otra presentación tuya y sus respuestas.",
)

# ================================================================ OA 12
lesson(
    OA12, 1,
    "Las tarjetas de personajes inventados escritas en esta clase y una persona de tu casa para hacer preguntas y respuestas.",
    "Aprenderé a compartir información personal segura en inglés, usando personajes inventados o datos que no revelen dónde vivo. Sirve para presentarme y conocer a otras personas con cuidado.",
    ["Sé decir hello y my name is.", "Sé contar hasta diez en español."],
    [
        "Para compartir información personal en inglés usa frases fijas: «My name is Mateo» (me llamo Mateo), «I'm ten» (tengo diez años), «I'm from Chile» (soy de Chile) y «I like drawing» (me gusta dibujar). También puedes decir «I have a cat» (tengo un gato) o «My favorite food is pasta» (mi comida favorita es la pasta).",
        "Para preguntar a otra persona: «What's your name?» (¿cómo te llamas?), «How old are you?» (¿cuántos años tienes?), «Where are you from?» (¿de dónde eres?), «What do you like?» (¿qué te gusta?) y «Do you have a pet?» (¿tienes una mascota?). Se responde «Yes, I do» (sí) o «No, I don't» (no).",
        "Hay datos privados que no se comparten con personas que no conoces: dirección, teléfono, nombre del colegio y claves. En esta clase usamos personajes inventados y datos seguros: nombre de pila, edad, país, gustos y mascotas. Si alguien te pide un dato privado, no lo des y cuéntaselo a una persona adulta.",
    ],
    [("My name is...", "me llamo..."), ("I'm...", "tengo... años"), ("I'm from...", "soy de..."), ("I have a...", "tengo un/una..."), ("pet", "mascota"), ("favorite", "favorito")],
    [
        ("Presentar a Mateo", "Ficha: Mateo, 10 años, Chile, le gusta dibujar, tiene un gato, comida favorita pasta. Tú eres Mateo. ¿Qué dices en cinco frases?", ["Nombre con My name is.", "Edad con I'm y país con I'm from.", "Gusto, mascota y comida con I like, I have y My favorite food is."], "My name is Mateo. I'm ten. I'm from Chile. I like drawing. I have a cat."),
        ("Responder sobre mascotas", "Eres Mateo. Te preguntan «Do you have a pet?». ¿Qué respondes?", ["Entiendo que preguntan por una mascota.", "Mateo tiene un gato.", "Respondo Yes, I do y el dato."], "Yes, I do. I have a cat."),
    ],
    [
        ("Decir «I have ten years».", "Se traduce palabra por palabra.", "En inglés se dice I'm ten."),
        ("Dar la dirección de la casa al presentarse.", "Es un dato privado.", "Comparte solo nombre de pila, edad, país y gustos."),
    ],
    [
        ("¿Cómo se dice «Me llamo Ana» en inglés?", "My name is Ana", "My name is dice el nombre."),
        ("¿Qué significa «pet»?", "Mascota", "Pet es un animal de compañía."),
        ("¿Qué significa «Yes, I do»?", "Sí", "Es la respuesta corta afirmativa a Do you...?"),
    ],
    [
        ("Ficha de Mateo: 10 años. Te preguntan «How old are you?» y eres Mateo. Elige la respuesta: (a) «I'm ten.» (b) «I have ten.»", "a", "La edad se dice con I'm."),
        ("¿Qué datos son seguros para presentarte? Elige: (a) nombre de pila, edad y gustos (b) dirección y teléfono", "a", "La opción (b) es privada."),
        ("Te preguntan «Where are you from?» y eres Mateo. Elige: (a) «I'm from Chile.» (b) «I like Chile.»", "a", "From indica el país de origen."),
    ],
    [
        ("Completa: «I ___ a cat.» (tengo)", "have", "I have significa tengo."),
        ("Completa la respuesta de Mateo: «My favorite ___ is pasta.» (comida)", "food", "Food es comida."),
        ("Ordena las palabras: from / I'm / Chile. Escribe la oración.", "I'm from Chile", "Primero va I'm y luego from y el país."),
    ],
    [
        ("Una persona que no conoces en un juego en línea te pide tu dirección. ¿Qué haces? Responde en español.", "No la doy y aviso a una persona adulta", "La dirección es un dato privado."),
        ("Ana dice «I have eight years». ¿Cómo se corrige para decir que tiene ocho años? Responde en inglés.", "I'm eight", "En inglés se usa I'm más el número."),
    ],
    [
        ("Te preguntan «Do you have a pet?» y eres Mateo. Escribe la respuesta corta más la frase con el animal.", "Yes, I do. I have a cat.", "Mateo tiene un gato."),
        ("Escribe la pregunta que haces para saber de qué país es una persona.", "Where are you from?", "Where are you from? pregunta el país."),
    ],
    [("Un compañero nuevo de la clase de inglés, personaje inventado, te pregunta «What's your name?». Eres Mateo. Responde con una frase.", "My name is Mateo", "Se usa My name is y el nombre.")],
    [
        ("¿Cómo se dice «¿cuántos años tienes?» en inglés?", "How old are you?", "Es la pregunta por la edad."),
        ("¿Qué significa «What do you like?»", "¿Qué te gusta?", "Pregunta por los gustos."),
        ("¿Cómo se dice «Mi color favorito es el azul»?", "My favorite color is blue", "Favorite es favorito."),
    ],
    task("Con una persona de tu casa, jueguen a conocerse con personajes inventados. Ficha de Mateo: 10 años, Chile, dibujar, un gato, pasta. Ficha de Sofía: 9 años, Perú, bailar (dancing), un perro (dog), arroz (rice). Uno hace de Mateo y el otro de Sofía. Pregunten por turnos: «What's your name?», «How old are you?», «Where are you from?», «What do you like?» y «Do you have a pet?». Respondan solo con los datos de la ficha y cambien de papel.", "A: What's your name? B: My name is Sofía. A: Do you have a pet? B: Yes, I do. I have a dog.", ["pregunta y responde las cinco preguntas", "usa I'm para la edad y I'm from para el país", "responde solo con datos de la ficha", "no da datos privados"], ["nota de la persona con quien practicaste"], ["decir I have ten years", "dar datos privados"], "Repite la pregunta que costó y elogia las respuestas completas."),
    "Di en inglés tu nombre de pila y tu edad frente a un espejo.",
    "Inventa un personaje con nombre, edad, país, gusto y mascota y escribe seis frases para presentarlo.",
)

lesson(
    OA12, 2,
    "Los números escritos en cada ejercicio, lápiz y veinte objetos pequeños de tu casa (lápices, botones, hojas) para contar.",
    "Aprenderé a decir lo que puedo y no puedo hacer, y a decir cantidades hasta veinte en inglés. Sirve para hablar de habilidades y contar cosas con números en inglés.",
    ["Sé contar hasta diez en inglés: one, two, three...", "Sé acciones como swim, jump y run."],
    [
        "Para decir una habilidad usa «I can...» (yo puedo o sé...): «I can swim» (sé nadar). Para decir que no puedes usa «I can't...»: «I can't fly» (no puedo volar). Para preguntar: «Can you ride a bike?» (¿sabes andar en bicicleta?) y se responde «Yes, I can» o «No, I can't». Después de can el verbo no cambia.",
        "Los números del once al veinte en inglés son: 11 eleven, 12 twelve, 13 thirteen, 14 fourteen, 15 fifteen, 16 sixteen, 17 seventeen, 18 eighteen, 19 nineteen y 20 twenty. Del 13 al 19 los números terminan en -teen (thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen). Cuidado: fifteen se escribe con f-i-f, no «fiveteen».",
        "Para decir una cantidad usa «There are» y el número: «There are fifteen books» (hay quince libros). Con una sola cosa se dice «There is one book». Para preguntar la cantidad: «How many books are there?» (¿cuántos libros hay?). Responde con el número y la cosa.",
    ],
    [("I can...", "yo puedo, yo sé..."), ("I can't...", "no puedo, no sé..."), ("eleven", "once"), ("fifteen", "quince"), ("twenty", "veinte"), ("How many...?", "¿cuántos...?")],
    [
        ("Decir una habilidad", "Sabes nadar pero no puedes volar. ¿Cómo lo dices en inglés?", ["Para lo que sé hacer uso I can.", "Para lo que no puedo uso I can't.", "Después de can el verbo no cambia."], "I can swim. I can't fly."),
        ("Decir una cantidad", "Hay 15 libros. ¿Cómo lo dices en inglés?", ["15 en inglés es fifteen.", "Son varios, uso There are.", "Escribo la cosa en plural: books."], "There are fifteen books."),
    ],
    [
        ("Decir «I can swims».", "Después de can el verbo no lleva s.", "Di I can swim."),
        ("Escribir fiveteen en lugar de fifteen.", "Se cambia la ortografía de quince.", "Escribe fifteen: f-i-f-t-e-e-n."),
    ],
    [
        ("¿Cómo se dice «yo puedo nadar» en inglés?", "I can swim", "Can indica habilidad."),
        ("¿Cómo se dice 20 en inglés?", "twenty", "Twenty es veinte."),
        ("¿Qué significa «How many...?»", "¿Cuántos...?", "Se usa para preguntar cantidades."),
    ],
    [
        ("Te preguntan «Can you ride a bike?» y puedes. Elige: (a) «Yes, I can.» (b) «Yes, I do.»", "a", "Una pregunta con Can se responde con can."),
        ("¿Qué número es fifteen? Elige: (a) 5 (b) 15", "b", "Fifteen es 15."),
        ("Elige la oración correcta: (a) «I can't fly.» (b) «I can't flies.»", "a", "Después de can't el verbo no cambia."),
    ],
    [
        arith("Hay dos grupos de ocho lápices. Escribe cuántos lápices hay en total (número).", "8 + 8", "Se suman los dos grupos."),
        ("Escribe en inglés el número 13.", "thirteen", "Thirteen es trece."),
        ("Completa: «There ___ twelve markers.» Opciones: is / are.", "are", "Twelve markers son varios."),
    ],
    [
        ("Ana tenía 18 marcadores y regaló 5. Escribe cuántos le quedan, con número y con palabra en inglés, así: 5 (five).", "13 (thirteen)", "18 menos 5 es 13."),
        ("Luis escribió «There are sixten books» para 16 libros. ¿Cómo se escribe bien 16 en inglés?", "sixteen", "Sixteen es la forma correcta."),
    ],
    [
        arith("Hay tres filas de cinco sillas. Escribe cuántas sillas hay en total (número).", "3 * 5", "Cada fila tiene cinco sillas."),
        ("Escribe la respuesta a «How many fingers are there on two hands?» con la forma «There are ___ fingers». Usa la palabra en inglés.", "There are ten fingers.", "Dos manos tienen diez dedos."),
    ],
    [("En la biblioteca cuentas 14 libros de cuentos. Escribe en inglés cuántos hay con la frase completa.", "There are fourteen books.", "14 se dice fourteen.")],
    [
        ("¿Cómo se dice «once» (11) en inglés?", "eleven", "Eleven es once."),
        ("¿Cómo se dice «No puedo volar» en inglés?", "I can't fly", "I can't indica que no puedo."),
        ("¿Qué número es nineteen?", "19", "Nineteen es diecinueve."),
    ],
    task("Con una persona de tu casa, haz dos juegos. Primero, di en inglés tres cosas que sabes hacer y dos que no con I can y I can't (por ejemplo: I can jump / I can't fly). Segundo, cuenta en voz alta de once a veinte con tus veinte objetos pequeños. Luego tu compañero esconde algunos objetos y tú dices cuántos hay con «There are ___ ...». Intercambien papeles.", "«I can swim. I can jump. I can sing. I can't fly. I can't drive.» «There are fifteen pencils.»", ["dice tres habilidades con I can y dos con I can't", "cuenta de once a veinte sin saltar números", "usa There are con el número en inglés", "el verbo después de can no cambia"], ["nota de la persona que escuchó tus frases y tu conteo"], ["decir I can swims", "escribir fiveteen"], "La otra persona dice qué número costó y se cuenta otra vez ese tramo."),
    "Cuenta en voz alta de once a veinte.",
    "Escribe cinco frases con There are y un número entre 11 y 20 en inglés.",
)

lesson(
    OA12, 3,
    "Las descripciones escritas en cada ejercicio, lápiz y una persona de tu casa para hacer preguntas.",
    "Aprenderé a describir animales, ocupaciones y lugares de la escuela en inglés, y a decir lo que está prohibido hacer en un lugar. Sirve para explicar normas de convivencia y describir lo que veo.",
    ["Sé algunos colores y animales en inglés.", "Sé que It is y She is sirven para describir."],
    [
        "Para describir un animal usa «It is a big, gray elephant» (es un elefante grande y gris). El adjetivo va antes del nombre, nunca después. Para describir una ocupación (occupation) usa «She is a teacher» (ella es profesora), «He is a cook» (él es cocinero) y «He is a doctor» (él es doctor). Un lugar de la escuela es «It is the library» (es la biblioteca).",
        "Lugares de la escuela: library (biblioteca), classroom (sala de clases), gym (gimnasio), playground (patio de juegos) y cafeteria (casino). Para decir lo que está prohibido (prohibition) en inglés usa «Don't» más el verbo: «Don't run in the library» (no corras en la biblioteca), «Don't shout in the classroom» (no grites en la sala), «Don't push on the stairs» (no empujes en la escalera).",
        "También puedes explicar la regla con «You can't...»: «You can't run in the library». Las dos formas dicen lo mismo. Para dar una razón corta puedes agregar «Please be quiet» (por favor, haz silencio). Estas normas ayudan a que todos estemos seguros y a gusto en la escuela.",
    ],
    [("It is a...", "es un/una..."), ("teacher", "profesor/a"), ("library", "biblioteca"), ("Don't run.", "no corras"), ("You can't...", "no puedes..."), ("shout", "gritar")],
    [
        ("Describir un animal", "Imagen: [un elefante grande y gris]. ¿Cómo lo describes en una oración?", ["Empiezo con It is a.", "Pongo los adjetivos antes del nombre.", "Termino con el animal."], "It is a big, gray elephant."),
        ("Decir una prohibición", "Estás en la biblioteca y alguien corre. ¿Qué le dices en inglés?", ["Uso Don't.", "Agrego el verbo run.", "Digo el lugar: in the library."], "Don't run in the library."),
    ],
    [
        ("Decir «a elephant big gray».", "En inglés el adjetivo va antes del nombre.", "Di a big, gray elephant."),
        ("Decir «Not run in the library» para prohibir.", "No se usa Not para empezar la prohibición.", "Usa Don't más el verbo."),
    ],
    [
        ("¿Qué significa «library»?", "Biblioteca", "Library no es librería."),
        ("¿Qué significa «Don't shout»?", "No grites", "Don't prohíbe la acción."),
        ("¿Cómo se dice «profesora» en inglés?", "teacher", "Teacher es profesor o profesora."),
    ],
    [
        ("Imagen: [un perro café pequeño]. Elige la oración correcta: (a) «It is a small, brown dog.» (b) «It is a dog small brown.»", "a", "Los adjetivos van antes del nombre."),
        ("Letrero: [un círculo rojo con un niño corriendo tachado, en la biblioteca]. Elige la frase: (a) «Don't run in the library.» (b) «Run in the library.»", "a", "El letrero prohíbe correr."),
        ("Imagen: [un cocinero con delantal]. Elige: (a) «He is a cook.» (b) «He is a teacher.»", "a", "Cook es cocinero."),
    ],
    [
        ("Completa: «She is a ___.» (doctora en inglés)", "doctor", "Doctor se escribe igual para doctor y doctora."),
        ("Completa la prohibición: «Don't ___ in the classroom.» (gritar)", "shout", "Shout es gritar."),
        ("Escribe la oración con la regla: no puedes correr en el gimnasio mojado (gym). Usa You can't.", "You can't run in the gym.", "You can't indica que está prohibido."),
    ],
    [
        ("Ana dice «Don't running in the library». ¿Cómo se corrige? Responde en inglés.", "Don't run in the library.", "Después de Don't el verbo va sin cambios."),
        ("Leo quiere decir dónde almuerzan los niños en la escuela. ¿Qué palabra del texto de la clase usa? Escríbela.", "cafeteria", "Cafeteria es el casino de la escuela."),
    ],
    [
        ("Ordena las palabras: a / is / It / elephant / big. Escribe la oración.", "It is a big elephant.", "El adjetivo big va antes del nombre."),
        ("Elige la prohibición correcta para el patio de juegos si alguien empuja: (a) «Don't push.» (b) «Don't shout the sun.»", "a", "Don't push significa no empujes."),
    ],
    [("En una visita al museo ves un letrero con una mano que toca un cuadro tachada y las palabras «Don't touch.» (touch es tocar). ¿Qué te dice el letrero? Responde en español.", "No toques", "Don't touch prohíbe tocar.")],
    [
        ("¿Cómo se dice «sala de clases» en inglés?", "classroom", "Classroom es la sala de clases."),
        ("¿Qué palabra uso para prohibir?", "Don't", "Don't significa no."),
        ("¿Cómo se dice «es un pez pequeño y azul»?", "It is a small, blue fish", "El adjetivo va antes del nombre."),
    ],
    task("Con una persona de tu casa, haz tres descripciones y tres prohibiciones. Descripciones: (1) [un elefante grande y gris] (2) [un gato pequeño y negro] (3) [una profesora en una sala de clases]. Prohibiciones: en la library, en la classroom y en las stairs (escalera). Di cada una en inglés y la otra persona te dice si entendió el lugar o el animal.", "«It is a big, gray elephant.» «Don't run in the library.» «Don't shout in the classroom.»", ["describe con adjetivos antes del nombre", "usa Don't con el verbo sin cambios", "nombra bien los lugares", "se entiende lo que dice"], ["nota de la persona que escuchó las seis frases"], ["poner el adjetivo después del nombre", "decir Don't running"], "La otra persona elige la frase que fue más clara y se repite una que costó."),
    "Di en inglés cómo es un animal que veas en una imagen de tu casa.",
    "Inventa tres reglas de tu patio en inglés con Don't y dibuja un letrero para una de ellas.",
)

lesson(
    OA12, 4,
    "Las escenas descritas en cada ejercicio, lápiz y una persona de tu casa para hacer preguntas y respuestas.",
    "Aprenderé a pedir comida y a decir dónde está un objeto en inglés. Sirve para pedir algo en un almuerzo de la escuela o para encontrar mis cosas.",
    ["Sé usar Can I have...? y please.", "Sé palabras de comida como apple, bread y water."],
    [
        "Para pedir comida o bebida usa «Can I have an apple, please?» (¿puedo tener una manzana, por favor?) o «Can I have some water, please?» (¿puedo tener un poco de agua?). Para preguntar si hay: «Do you have milk?» (¿tienes leche?). Respuestas: «Yes, here you are» o «Sorry, we don't have milk». Antes de vocal se dice an (an apple), y antes de consonante se dice a (a banana).",
        "Para preguntar dónde está algo usa «Where is my pencil?» (¿dónde está mi lápiz?). La respuesta usa una palabra de lugar (preposition): on (sobre), in (dentro de), under (debajo de), next to (al lado de). Por ejemplo: «It's on the table» (está sobre la mesa), «It's in the bag» (está dentro de la mochila), «It's under the chair» (está debajo de la silla), «It's next to the book» (está al lado del libro).",
        "Para varias cosas se dice «They are...»: «Where are my shoes?» «They are under the bed» (están debajo de la cama). Para pedir ayuda a encontrar algo, empieza con «Excuse me» (disculpa). Responde siempre con la posición exacta de la escena que ves o lees.",
    ],
    [("Can I have...?", "¿puedo tener...?"), ("Do you have...?", "¿tienes...?"), ("Where is...?", "¿dónde está...?"), ("on / in / under", "sobre / dentro de / debajo de"), ("next to", "al lado de"), ("some", "un poco de, algo de")],
    [
        ("Pedir comida", "Quieres una manzana. ¿Qué pides?", ["Uso Can I have.", "Apple empieza con vocal: an apple.", "Agrego please."], "Can I have an apple, please?"),
        ("Decir dónde está", "Escena: [un lápiz sobre una mesa]. Te preguntan «Where is my pencil?». ¿Qué respondes?", ["Busco dónde está el lápiz.", "Está sobre la mesa.", "Uso on."], "It's on the table."),
    ],
    [
        ("Decir «a apple».", "Apple empieza con vocal y lleva an.", "Di an apple."),
        ("Responder con in cuando algo está encima.", "In significa dentro, on significa sobre.", "Mira la escena y elige on, in o under."),
    ],
    [
        ("¿Qué significa «Where is...?»", "¿Dónde está...?", "Pregunta por la ubicación."),
        ("¿Qué significa «under»?", "Debajo de", "Under indica que algo está abajo."),
        ("¿Qué significa «Do you have milk?»", "¿Tienes leche?", "Do you have... pregunta si hay."),
    ],
    [
        ("Escena: [una pelota dentro de una caja]. Elige: (a) «It's in the box.» (b) «It's on the box.»", "a", "La pelota está dentro."),
        ("Escena: [un gato debajo de una silla]. Elige: (a) «It's under the chair.» (b) «It's next to the chair.»", "a", "El gato está bajo la silla."),
        ("Te sirven un jugo y dices gracias. ¿Cómo respondes a «Here you are»? Elige: (a) «Thank you.» (b) «Sorry.»", "a", "Se agradece cuando te entregan algo."),
    ],
    [
        ("Completa con a o an: «Can I have ___ banana, please?»", "a", "Banana empieza con consonante."),
        ("Completa con a o an: «Can I have ___ egg, please?»", "an", "Egg empieza con vocal."),
        ("Escena: [un libro al lado de una lámpara]. Completa: «It's ___ to the lamp.»", "next", "Next to significa al lado de."),
    ],
    [
        ("Escena: [dos zapatos debajo de la cama]. Te preguntan «Where are my shoes?». Escribe tu respuesta.", "They are under the bed.", "Shoes es plural y están bajo la cama."),
        ("Luis pide leche diciendo «Milk!». ¿Cómo lo dice con cortesía? Responde en inglés.", "Can I have some milk, please?", "Un pedido amable lleva Can I have y please."),
    ],
    [
        ("Ordena las palabras: is / Where / pencil / my. Escribe la pregunta.", "Where is my pencil?", "La pregunta empieza con Where."),
        ("Escena: [un sándwich dentro de una mochila]. Elige la respuesta a «Where is the sandwich?»: (a) «It's in the bag.» (b) «It's under the bag.»", "a", "El sándwich está dentro de la mochila."),
    ],
    [("En el casino de la escuela ves [un vaso de agua sobre la mesa]. Un niño pregunta «Where is the water?». Elige tu respuesta: (a) «It's on the table.» (b) «It's under the table.»", "a", "El vaso está sobre la mesa.")],
    [
        ("¿Cómo se dice «¿puedo tener agua, por favor?»", "Can I have some water, please?", "Es un pedido amable."),
        ("¿Qué significa «next to»?", "Al lado de", "Next to indica que está a un costado."),
        ("¿Cuándo uso an en vez de a?", "Antes de una palabra que empieza con vocal", "Por ejemplo, an apple."),
    ],
    task("Con una persona de tu casa, jueguen a pedir comida y buscar objetos. Pedidos: (1) Can I have an apple, please? (2) Can I have some water, please? (3) Do you have milk? Después miren estas tres escenas: [lápiz sobre la mesa], [pelota dentro de una caja], [gato debajo de la silla]. Una persona pregunta «Where is the ___?» y la otra responde con on, in o under. Cambien de papel.", "A: Where is the pencil? B: It's on the table.", ["hace los tres pedidos con Can I have o Do you have y please", "usa an o a bien", "responde con on, in o under según la escena", "habla por turnos"], ["nota de la persona que hizo el otro papel"], ["decir a apple", "confundir in y on"], "Repite el pedido o la ubicación que costó mirando la escena."),
    "Pide en voz alta una fruta con Can I have y please.",
    "Dibuja una escena con tres objetos y escribe tres oraciones en inglés que digan dónde están.",
)

lesson(
    OA12, 5,
    "Las acciones e imágenes descritas en cada ejercicio, lápiz y una persona de tu casa para hacer mímica.",
    "Aprenderé a decir lo que alguien hace en este momento, usando am, is o are más el verbo con -ing. Sirve para describir lo que pasa ahora, por ejemplo en un video o frente a ti.",
    ["Sé acciones como read, play, draw y eat.", "Sé usar I am, he is y they are."],
    [
        "Para decir lo que pasa ahora usa am, is o are y el verbo con -ing: «I am reading» (estoy leyendo), «She is drawing» (ella está dibujando), «They are playing» (ellos están jugando). Con I usas am, con he, she e it usas is, y con we, you y they usas are.",
        "Para formar el verbo con -ing, casi siempre se agrega ing: read-reading, play-playing, draw-drawing, eat-eating, sing-singing, jump-jumping. Hay casos especiales: run-running y swim-swimming duplican la última letra; write-writing y make-making pierden la e final. Para preguntar usa «What is he doing?» (¿qué está haciendo él?) y responde «He is reading».",
        "Para describir una escena, mira primero quién actúa y cuántas personas son. Una persona usa is; varias usan are. Así evitas errores como «They is playing». Puedes hacer mímica para comprobar: una persona actúa y la otra pregunta «What are you doing?».",
    ],
    [("I am reading.", "estoy leyendo"), ("She is drawing.", "ella está dibujando"), ("They are playing.", "ellos están jugando"), ("What is he doing?", "¿qué está haciendo él?"), ("running", "corriendo"), ("writing", "escribiendo")],
    [
        ("Describir una acción", "Imagen: [una niña sentada que lee un libro]. ¿Qué dices en inglés?", ["Es una niña, uso She is.", "El verbo es read con ing: reading.", "Uno todo."], "She is reading a book."),
        ("Varias personas", "Imagen: [dos niños que juegan]. ¿Qué dices en inglés?", ["Son dos personas: They are.", "El verbo es play con ing: playing.", "Uno todo."], "They are playing."),
    ],
    [
        ("Decir «They is playing».", "They necesita are, no is.", "Di They are playing."),
        ("Decir «He is runing».", "Run duplica la n.", "Escribe running."),
    ],
    [
        ("¿Qué significa «She is drawing»?", "Ella está dibujando", "Is drawing indica una acción ahora."),
        ("¿Cómo se dice «¿qué está haciendo él?» en inglés?", "What is he doing?", "Pregunta por la acción ahora."),
        ("¿Cómo se escribe «corriendo» en inglés?", "running", "Run duplica la n."),
    ],
    [
        ("Imagen: [un niño que come una manzana]. Elige: (a) «He is eating an apple.» (b) «He is eat an apple.»", "a", "Se necesita is y eating."),
        ("Imagen: [tres niños que cantan]. Elige: (a) «They are singing.» (b) «They is singing.»", "a", "They va con are."),
        ("Imagen: [una niña que escribe en su cuaderno]. Elige la forma correcta: (a) writing (b) writeing", "a", "Write pierde la e y queda writing."),
    ],
    [
        ("Completa con am, is o are: «I ___ reading.»", "am", "I va con am."),
        ("Completa con is o are: «The boys ___ jumping.»", "are", "The boys son varios."),
        ("Completa con el verbo swim en -ing: «The girl is ___.»", "swimming", "Swim duplica la m."),
    ],
    [
        ("Luis dice «She are drawing». ¿Cómo se corrige? Responde en inglés.", "She is drawing.", "She va con is."),
        ("Ana describe una escena con un niño que corre y dice «He is run». ¿Cómo debe decirlo? Responde en inglés.", "He is running.", "Run se escribe running."),
    ],
    [
        ("Ordena las palabras: is / She / book / reading / a. Escribe la oración.", "She is reading a book.", "Primero va She is y luego el verbo con -ing."),
        ("Imagen: [una niña que dibuja y un niño que lee]. Elige: (a) «She is drawing and he is reading.» (b) «She is reading and he is drawing.»", "a", "La imagen muestra a la niña dibujando."),
    ],
    [("Una persona de tu casa hace mímica de comer. Preguntas «What are you doing?». Elige la respuesta: (a) «I am eating.» (b) «I am eat.»", "a", "Eating es la forma con -ing.")],
    [
        ("¿Cómo se dice «Estoy leyendo» en inglés?", "I am reading", "Se usa am y reading."),
        ("¿Qué verbo auxiliar va con they?", "are", "They va con are."),
        ("¿Cómo se escribe «escribiendo» en inglés?", "writing", "Write pierde la e."),
    ],
    task("Juega a la mímica con una persona de tu casa. Una persona hace una acción segura (reading, drawing, eating, singing, jumping suave o swimming con los brazos en el aire) y la otra pregunta «What are you doing?». La persona responde con «I am ___ing» y luego la otra describe: «He/She is ___ing». Después hagan una acción juntos y digan «We are ___ing». Hagan al menos cinco acciones.", "A: What are you doing? B: I am drawing. A: She is drawing. Los dos: We are singing.", ["usa am, is o are correctamente", "forma bien el verbo con -ing", "pregunta con What are you doing?", "dice al menos cinco acciones distintas"], ["nota de la persona que hizo la mímica contigo"], ["decir They is", "escribir runing"], "La otra persona comprueba la forma -ing del verbo y se repite una frase."),
    "Di en inglés qué estás haciendo ahora con I am...ing.",
    "Escribe cinco oraciones sobre lo que hacen personas de una imagen y revisa am, is y are.",
)
