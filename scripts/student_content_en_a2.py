"""Student material for 1.º básico Inglés, EN01 OA 03 (evidencias de comprensión oral) y OA 04 (estrategias de escucha).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado.
El estudiante puede tapar el guion con una hoja mientras el adulto lee.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA3, OA4 = "EN01 OA 03", "EN01 OA 04"
ADULT = "Un adulto lee en voz alta (el estudiante tapa el guion): "


# ---------------------------------------------------------------- OA 03
register(
    OA3, 1,
    materials="Las descripciones escritas en cada ejercicio, que lee un adulto; lápices de colores y papel.",
    use="Aprenderé a mostrar que entendí quién o qué se describe en inglés, señalando o dibujando. Sirve para demostrar comprensión sin tener que hablar mucho.",
    prior=["Sé algunos colores en inglés: red, blue, yellow y green.", "Sé nombrar objetos como ball, cat y book."],
    explain=[
        "Una forma de mostrar que entendiste es señalar, marcar o dibujar lo que oyes. Si el adulto dice «It's a red ball», no necesitas responder con palabras: basta con elegir o dibujar la pelota roja. Eso también es comprensión.",
        "Para identificar un personaje u objeto, escucha tres cosas: el nombre (cat, ball, book), el color (red, blue, green) y el tamaño (big, small). Con esas tres pistas, ya sabes de cuál se habla entre varios.",
        "Si hay dos objetos parecidos, la diferencia está en una palabra: red ball o blue ball, big cat o small cat. Escucha esa palabra con cuidado y elige solo el que coincide con todo lo que oíste.",
    ],
    vocab=[("it's a...", "es un/una..."), ("big", "grande"), ("small", "pequeño"), ("red / blue / green / yellow", "rojo / azul / verde / amarillo"), ("point to", "señalar"), ("choose", "elegir")],
    worked=[
        {"title": "Elegir el objeto", "problem": ADULT + "«It's a small blue ball.» Hay cuatro pelotas: grande roja, pequeña roja, grande azul, pequeña azul. ¿Cuál es?", "steps": ["Small es pequeña.", "Blue es azul.", "Busco la pequeña azul."], "answer": "La pelota pequeña azul"},
        {"title": "Reconocer al personaje", "problem": ADULT + "«It's a big cat. It is black.» Hay un gato grande negro y un perro grande negro. ¿Cuál es?", "steps": ["Escucho cat: gato.", "Big y black coinciden con el gato grande negro."], "answer": "El gato grande negro"},
    ],
    mistakes=[
        {"wrong": "Elegir el objeto que tiene el color correcto pero el nombre equivocado.", "why": "Solo se atiende a una pista.", "fix": "Revisa las tres pistas: nombre, color y tamaño."},
        {"wrong": "No elegir nada porque no entiendo todas las palabras.", "why": "Se piensa que hay que traducir todo.", "fix": "Usa las palabras que sí conoces para descartar opciones."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«It's a cat.» Hay un gato, un perro y un pez. ¿Qué eliges?", "El gato", "Cat es gato."),
            ex(ADULT + "«It's red.» Hay una pelota roja y una azul. ¿Cuál señalas?", "La roja", "Red es rojo."),
            ex(ADULT + "«It's big.» Hay un perro grande y uno pequeño. ¿Cuál eliges?", "El grande", "Big es grande."),
        ],
        "understand": [
            ex("¿Qué tres pistas ayudan a identificar un objeto?", "Nombre, color y tamaño", "Con ellas se elige entre objetos parecidos."),
            ex("¿Qué significa «small»?", "pequeño", "Es lo contrario de big."),
            ex("¿Qué puedes hacer para mostrar que entendiste sin hablar?", "Señalar, marcar o dibujar", "Son formas de mostrar comprensión."),
        ],
        "apply": [
            ex(ADULT + "«It's a green book.» Hay un libro rojo, uno verde y uno azul. ¿Cuál es?", "El verde", "Green es verde."),
            ex(ADULT + "«It's a big yellow fish.» Hay un pez pequeño amarillo, uno grande amarillo y uno grande azul. ¿Cuál es?", "El pez grande amarillo", "Big y yellow coinciden."),
            ex(ADULT + "«It's a small dog.» Hay un perro grande y un perro pequeño. ¿Cuál es?", "El pequeño", "Small es pequeño."),
        ],
        "reason": [
            ex(ADULT + "«It's a red ball.» Hay una pelota roja grande y una pelota roja pequeña. ¿Por qué no puedes elegir solo con esa frase?", "Porque no dice el tamaño y hay dos pelotas rojas", "Falta una pista para decidir."),
            ex("Ana escuchó «blue» y señaló un gato azul, pero el adulto dijo «blue ball». ¿Qué pista olvidó?", "El nombre ball", "Debía elegir una pelota azul."),
        ],
        "challenge": [
            ex(ADULT + "«It's a small green cat on a big yellow chair.» ¿De qué color es la silla?", "Amarilla", "Yellow es amarilla."),
            ex("Escribe en inglés una descripción de una pelota pequeña azul.", "It's a small blue ball", "Se usa tamaño, color y nombre."),
        ],
    },
    context=[ex(ADULT + "«A: Which one is your bag? B: It's the big red bag.» En la entrada del colegio, dos niños buscan una mochila entre una mochila roja grande, una azul grande y una roja pequeña. ¿Cuál es?", "La roja grande", "Big red bag es mochila roja grande.")],
    selfcheck=[
        ex(ADULT + "«It's a dog.» ¿Qué animal es?", "Un perro", "Dog es perro."),
        ex("¿Cómo se dice «verde» en inglés?", "green", "Green es el color verde."),
        ex("¿Qué haces si dos objetos tienen el mismo color?", "Reviso el tamaño y el nombre", "Hay más pistas para decidir."),
    ],
    open_task=task("Un adulto lee: «It's a small red house. It has a big yellow door.» Dibuja lo que oyes y pinta la casa y la puerta con los colores correctos. Luego di en inglés el color de la puerta.", "Dibujo de una casa pequeña roja con una puerta grande amarilla. Dice: «Yellow.»", ["casa pequeña y roja", "puerta grande y amarilla", "dice el color en inglés"], ["dibujo", "nota del adulto"], ["pintar la puerta de rojo", "dibujar una casa grande"], "Compara con él el dibujo con el texto y ayúdale a corregir lo que no coincide."),
    reinforce="Señala en tu casa algo rojo y algo azul diciendo «red» y «blue».",
    extend="Escribe una descripción de tres palabras de un objeto de tu pieza, como «big blue bag».",
)

register(
    OA3, 2,
    materials="Las instrucciones escritas en cada ejercicio, que lee un adulto; hojas, lápices de colores y regla opcional.",
    use="Aprenderé a hacer lo que se pide en una instrucción oral en inglés. Sirve para demostrar que entendí, aunque no hable.",
    prior=["Sé algunos colores en inglés.", "Sé qué significa draw, point y clap."],
    explain=[
        "Seguir una instrucción es la mejor prueba de que entendiste. Si el adulto dice «Draw a blue circle», tú dibujas un círculo azul: acción más objeto más color. No necesitas responder con palabras.",
        "Algunas instrucciones tienen dos pasos: «Draw a circle. Color it red.» Haz el primer paso y luego el segundo. Si te pierdes, pide «Again, please». Las palabras de acción que verás son draw (dibuja), color (pinta), point (señala), touch (toca), clap (aplaude) y jump (salta).",
        "Las formas más comunes son circle (círculo), square (cuadrado), triangle (triángulo) y star (estrella). Si oyes next to (al lado de) o under (debajo de), dibuja la forma en ese lugar.",
    ],
    vocab=[("draw", "dibujar"), ("color", "pintar"), ("circle", "círculo"), ("square", "cuadrado"), ("triangle", "triángulo"), ("star", "estrella")],
    worked=[
        {"title": "Un paso", "problem": ADULT + "«Draw a blue circle.» ¿Qué dibujas?", "steps": ["Draw es dibujar.", "Blue es azul.", "Circle es círculo."], "answer": "Un círculo azul"},
        {"title": "Dos pasos", "problem": ADULT + "«Draw a square. Color it green.» ¿Qué queda en tu hoja?", "steps": ["Primero dibujo un cuadrado.", "Luego lo pinto de verde."], "answer": "Un cuadrado verde"},
    ],
    mistakes=[
        {"wrong": "Hacer solo el segundo paso de la instrucción.", "why": "Se olvida el primero.", "fix": "Haz los pasos en el orden en que los oyes."},
        {"wrong": "Cambiar el color porque no se recuerda.", "why": "Se toma el primero que se tiene a mano.", "fix": "Pide «Again, please» y escucha el color."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Draw a star.» ¿Qué dibujas?", "Una estrella", "Star es estrella."),
            ex(ADULT + "«Touch your head.» ¿Qué haces?", "Me toco la cabeza", "Touch es tocar y head es cabeza."),
            ex(ADULT + "«Color it red.» ¿Con qué color pintas?", "Rojo", "Red es rojo."),
        ],
        "understand": [
            ex("¿Qué significa «triangle»?", "triángulo", "Es la figura con tres lados."),
            ex("¿Qué haces cuando oyes «Draw a circle. Color it yellow.»?", "Dibujo un círculo y lo pinto amarillo", "Son dos pasos seguidos."),
            ex("¿Qué dices si no entiendes una instrucción?", "Again, please", "Es la forma amable de pedir que repitan."),
        ],
        "apply": [
            ex(ADULT + "«Draw a triangle. Color it blue.» ¿Qué figura y color resulta?", "Un triángulo azul", "Se dibuja y luego se pinta."),
            ex(ADULT + "«Draw a big square. Draw a small star next to it.» ¿Dónde queda la estrella?", "Al lado del cuadrado", "Next to es al lado de."),
            ex(ADULT + "«Draw a circle. Draw a star under the circle.» ¿Dónde queda la estrella?", "Debajo del círculo", "Under es debajo."),
        ],
        "reason": [
            ex("Pía dibujó un cuadrado rojo cuando oyó «Draw a red circle». ¿Qué palabra escuchó mal?", "Circle", "Circle es círculo y square es cuadrado."),
            ex("¿Por qué conviene hacer los pasos en orden?", "Porque la instrucción va dando el orden de lo que debo hacer", "El orden cambia el resultado."),
        ],
        "challenge": [
            ex(ADULT + "«Draw a green triangle. Draw a yellow star on top of the triangle. Draw a blue circle next to the triangle.» ¿Cuántas figuras dibujaste en total?", "3", "Triángulo, estrella y círculo."),
            ex("Escribe en inglés la instrucción: dibuja un cuadrado rojo.", "Draw a red square", "Draw más color más figura."),
        ],
    },
    context=[ex(ADULT + "«Open your notebook. Draw a big sun. Color it yellow.» Es la clase de artes. ¿Qué pinta de amarillo?", "El sol", "Sun es sol.")],
    selfcheck=[
        ex("¿Qué significa «draw»?", "dibujar", "Draw es dibujar."),
        ex(ADULT + "«Clap three times.» ¿Cuántas palmadas das?", "3", "Three es tres."),
        ex("¿Cómo se dice «círculo» en inglés?", "circle", "Circle es círculo."),
    ],
    open_task=task("Un adulto da estas instrucciones lentas: «Draw a square. Color it yellow. Draw a blue star under the square. Draw a red circle next to the square.» Hazlas en una hoja. Después di en inglés el color de la estrella.", "Un cuadrado amarillo, una estrella azul debajo y un círculo rojo al lado. Dice: «Blue.»", ["cuadrado amarillo", "estrella azul debajo", "círculo rojo al lado", "dice «Blue»"], ["dibujo", "nota del adulto"], ["estrella arriba", "círculo azul"], "Revisa con él cada paso y pide a quien enseña que repita la instrucción que falló."),
    reinforce="Dibuja un círculo rojo y un cuadrado azul y di sus nombres en inglés.",
    extend="Escribe una instrucción de dos pasos para un compañero, con una figura y un color.",
)

register(
    OA3, 3,
    materials="Los mini diálogos escritos en cada ejercicio, que lee un adulto; lápiz y papel.",
    use="Aprenderé a reconocer expresiones muy usadas, como hello, thank you o sorry, y a saber cuándo se dicen. Sirve para conversar con cortesía en inglés.",
    prior=["Sé decir hello y goodbye.", "Sé que please significa por favor."],
    explain=[
        "Hay expresiones que se oyen todos los días y conviene reconocerlas de inmediato. Good morning (buenos días), Good night (buenas noches), Thank you (gracias), You're welcome (de nada), Sorry (perdón), Please (por favor), Hello (hola) y Goodbye (adiós).",
        "Cada una se usa en un momento. Cuando recibes algo, dices thank you. Cuando alguien te agradece, dices you're welcome. Si chocas con alguien, dices sorry. Si te vas, dices goodbye.",
        "Cuando oigas una de estas expresiones, piensa qué pasó antes. Si alguien dice «Here you are» y te da un lápiz, lo más lógico es contestar thank you. Escuchar la situación ayuda a elegir la expresión.",
    ],
    vocab=[("thank you", "gracias"), ("you're welcome", "de nada"), ("sorry", "perdón, lo siento"), ("please", "por favor"), ("good morning", "buenos días"), ("goodbye", "adiós")],
    worked=[
        {"title": "Qué se dice", "problem": ADULT + "«A: Here you are. B: ...» B recibe un lápiz. ¿Qué dice?", "steps": ["B recibe algo.", "Se agradece con thank you."], "answer": "Thank you"},
        {"title": "Responder a gracias", "problem": ADULT + "«A: Thank you! B: ...» ¿Qué responde B?", "steps": ["A agradece.", "La respuesta de cortesía es you're welcome."], "answer": "You're welcome"},
    ],
    mistakes=[
        {"wrong": "Decir «sorry» cuando alguien te da algo.", "why": "Se confunde la expresión de cortesía.", "fix": "Cuando recibes algo, di thank you."},
        {"wrong": "Responder «thank you» a «thank you».", "why": "Se repite sin pensar.", "fix": "A thank you se responde you're welcome."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Good morning!» ¿Cuándo se dice?", "Por la mañana", "Morning es mañana."),
            ex(ADULT + "«Thank you!» ¿Qué significa?", "Gracias", "Thank you es gracias."),
            ex(ADULT + "«Sorry!» ¿Qué significa?", "Perdón", "Sorry se usa para pedir disculpas."),
        ],
        "understand": [
            ex("¿Qué significa «you're welcome»?", "de nada", "Se responde a thank you."),
            ex("¿Cuándo dices «goodbye»?", "Cuando te vas o termina la conversación", "Es la despedida."),
            ex("¿Qué significa «please»?", "por favor", "Es una palabra de cortesía."),
        ],
        "apply": [
            ex(ADULT + "«A: Can I have a pencil, ...?» ¿Qué palabra de cortesía falta: please o sorry?", "please", "Se pide algo con por favor."),
            ex(ADULT + "«A: Thank you! B: ...» Elige: (a) Goodbye (b) You're welcome.", "b", "A thank you se responde you're welcome."),
            ex(ADULT + "«A: Oh no! I'm so ... I broke your pencil.» ¿Qué falta: sorry o welcome?", "sorry", "Se pide perdón por romper algo."),
        ],
        "reason": [
            ex("Si un compañero te presta un lápiz, ¿dices «sorry» o «thank you»? Explica.", "Thank you, porque recibí un favor", "Se agradece cuando alguien ayuda."),
            ex("¿Por qué «good night» no se dice por la mañana?", "Porque night es noche", "Cada saludo va con su momento del día."),
        ],
        "challenge": [
            ex(ADULT + "«A: Good morning, Ana! B: Good morning! A: Here you are. B: Thank you! A: You're welcome.» ¿Cuántas expresiones de cortesía distintas oíste?", "3", "Good morning, thank you y you're welcome."),
            ex("Escribe en inglés cómo pides un lápiz con cortesía.", "A pencil, please", "Se agrega please."),
        ],
    },
    context=[ex(ADULT + "«A: Oops! Sorry! B: It's OK.» En el patio, una niña choca sin querer con otra. ¿Qué expresión dice la primera?", "Sorry", "Es la disculpa.")],
    selfcheck=[
        ex("¿Qué significa «hello»?", "hola", "Es un saludo."),
        ex(ADULT + "«A: Here is your book. B: Thank you.» ¿Qué recibió B?", "Un libro", "Book es libro."),
        ex("¿Cómo respondes a «Thank you»?", "You're welcome", "Es la respuesta de cortesía."),
    ],
    open_task=task("Un adulto actúa un mini diálogo contigo: te da un lápiz diciendo «Here you are.» Tú respondes con la expresión correcta y luego, cuando él dice «Thank you», contestas con la tuya. Al final se despiden.", "«Thank you.» «You're welcome.» «Goodbye!»", ["dice thank you al recibir", "dice you're welcome al final", "se despide con goodbye"], ["nota del adulto", "audio con permiso de la familia"], ["decir sorry al recibir", "repetir thank you dos veces"], "Cambien de papel y repitan para que practique ambas expresiones."),
    reinforce="Di «thank you» cada vez que alguien te dé algo en tu casa durante un día.",
    extend="Escribe tres situaciones diarias y la expresión en inglés que usarías en cada una.",
)

register(
    OA3, 4,
    materials="Las palabras escritas en cada ejercicio, que lee un adulto una por una; lápiz y una hoja para tapar el guion.",
    use="Aprenderé a distinguir sonidos que se parecen en inglés, como big y pig. Sirve para no confundir palabras al escuchar.",
    prior=["Sé decir palabras cortas como cat y hat.", "Sé que algunos sonidos del inglés no existen en español."],
    explain=[
        "En inglés hay palabras que se escriben distinto y suenan casi igual. Para el oído, big y pig se diferencian solo por el primer sonido. Lo mismo pasa con cat y cap, o pen y pan. Estas parejas se llaman pares mínimos.",
        "Para distinguirlas, escucha una letra a la vez. En cat y cap cambia el sonido final: -t y -p. En pen y pan cambia la vocal del medio: e y a. Si te fijas en el sonido que cambia, no te equivocarás.",
        "Una buena estrategia es pedir que lo repitan despacio y decirlo tú también, mirando la boca de quien habla. No importa tener acento perfecto: lo importante es reconocer cuál palabra oíste.",
    ],
    vocab=[("big / pig", "grande / cerdo"), ("cat / cap", "gato / gorro"), ("pen / pan", "bolígrafo / sartén"), ("hat / hot", "sombrero / caliente"), ("same", "igual"), ("different", "diferente")],
    worked=[
        {"title": "Un par de palabras", "problem": ADULT + "«pig» (el adulto lee solo esa palabra). ¿Oíste big o pig?", "steps": ["Escucho el primer sonido.", "Suena p, no b.", "Es pig."], "answer": "pig"},
        {"title": "Cambia el final", "problem": ADULT + "«cap». ¿Oíste cat o cap?", "steps": ["Escucho el final.", "Termina en p.", "Es cap."], "answer": "cap"},
    ],
    mistakes=[
        {"wrong": "Elegir una palabra por cómo suena en español.", "why": "El oído busca sonidos conocidos.", "fix": "Fíjate en el sonido que cambia y pide que lo repitan."},
        {"wrong": "Mirar solo la letra inicial al escuchar.", "why": "Se olvida que la diferencia puede estar en el medio o el final.", "fix": "Escucha toda la palabra."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«hat». ¿Oíste hat o hot?", "hat", "Tiene la vocal a, como cat."),
            ex(ADULT + "«pen». ¿Oíste pen o pan?", "pen", "Tiene la vocal e."),
            ex(ADULT + "«big». ¿Oíste big o pig?", "big", "Empieza con b."),
        ],
        "understand": [
            ex("¿Qué son los «pares mínimos»?", "Palabras que suenan casi igual y cambian en un solo sonido", "Ejemplo: big y pig."),
            ex("¿En qué se diferencian «cat» y «cap»?", "En el sonido final", "Termina en t o en p."),
            ex("¿Qué haces si no distingues dos palabras?", "Pido que repitan despacio", "Escuchar de nuevo ayuda."),
        ],
        "apply": [
            ex(ADULT + "«hot». ¿Oíste hat o hot?", "hot", "La vocal es o."),
            ex(ADULT + "«pan». ¿Oíste pen o pan?", "pan", "La vocal del medio es a."),
            ex(ADULT + "«cat». ¿Oíste cat o cap?", "cat", "Termina en t."),
        ],
        "reason": [
            ex("Ana escribió «pig» cuando el adulto dijo «big». ¿En qué sonido se equivocó?", "En el primer sonido: p en lugar de b", "Las dos palabras cambian solo la primera letra."),
            ex("¿Por qué es importante distinguir «hat» y «hot»?", "Porque significan cosas distintas: sombrero y caliente", "Un solo sonido cambia el significado."),
        ],
        "challenge": [
            ex(ADULT + "El adulto lee tres palabras: «pig, cap, pan». Escribe cuáles tienen la vocal a.", "cap y pan", "Cap y pan tienen a, pig tiene i."),
            ex("Escribe una palabra que suene casi igual a «bag» y cambie solo el final.", "Por ejemplo: bat", "Bag y bat solo cambian la última letra."),
        ],
    },
    context=[ex(ADULT + "«A: Look! A pig!» En una granja, un niño señala un animal. ¿El animal es big o pig?", "pig", "El adulto dijo pig, que es cerdo.")],
    selfcheck=[
        ex("¿Qué significa «hat»?", "sombrero", "Hat es sombrero."),
        ex(ADULT + "«cap». ¿Oíste cat o cap?", "cap", "Termina en p."),
        ex("¿Qué te ayuda a distinguir dos palabras parecidas?", "Escuchar el sonido que cambia", "Ahí está la diferencia."),
    ],
    open_task=task("Un adulto lee en voz alta, una por una y sin mostrarte: «pig, pan, hat, cap.» Escribe una marca al lado de cada palabra que oigas en esta lista de parejas: big/pig, pen/pan, hat/hot, cat/cap. Después di tú dos de las palabras, una de cada pareja distinta.", "Marca pig, pan, hat y cap. Dice, por ejemplo, «pig» y «hat».", ["marca las cuatro correctas", "dice dos palabras con claridad", "distingue la pareja"], ["lista marcada", "nota del adulto"], ["marcar big en lugar de pig", "confundir pen y pan"], "Repite despacio con él las parejas que falló, mostrando la boca."),
    reinforce="Pide a un adulto que diga «cat» y «cap» y levanta la mano cuando oigas «cap».",
    extend="Escribe dos pares de palabras que suenen casi igual y dibuja cada una.",
)

register(
    OA3, 5,
    materials="Los diálogos y preguntas escritas en cada ejercicio, que lee un adulto; lápiz y papel.",
    use="Aprenderé a mostrar que entendí un texto oral usando varias formas: elegir, dibujar y decir. Sirve para demostrar todo lo que comprendí.",
    prior=["Sé identificar objetos y colores.", "Sé seguir instrucciones y reconocer expresiones de cortesía."],
    explain=[
        "Para mostrar que entendiste un texto oral puedes combinar evidencias: marcar la respuesta, dibujar y decir una frase. Cada una muestra algo distinto. Una sola no siempre es suficiente.",
        "Ejemplo: el adulto lee «Pia has a small red ball. She says: Thank you!». Puedes dibujar la pelota roja pequeña, marcar quién la tiene y decir «Thank you». Con eso muestras objeto, personaje y expresión.",
        "Cuando termines, comprueba: ¿mi dibujo coincide con el texto?, ¿mi respuesta usa las palabras que oí? Pide que lo repitan si dudas. Así tu evidencia es más segura.",
    ],
    vocab=[("evidence", "prueba de que entendiste"), ("draw", "dibujar"), ("choose", "elegir"), ("say", "decir"), ("small red ball", "pelota roja pequeña"), ("check", "revisar")],
    worked=[
        {"title": "Combinar evidencias", "problem": ADULT + "«Pia has a small red ball. She says: Thank you!» ¿Qué dibujas y qué dices?", "steps": ["Dibujo una pelota roja pequeña.", "Marco a Pía como quien la tiene.", "Digo Thank you."], "answer": "Pelota roja pequeña, Pía y la frase Thank you"},
        {"title": "Revisar", "problem": "Dibujé una pelota roja grande. El adulto leyó «small red ball». ¿Qué hago?", "steps": ["Comparo con el texto.", "Small es pequeña.", "Corrijo mi dibujo."], "answer": "Dibujo una pelota roja pequeña"},
    ],
    mistakes=[
        {"wrong": "Dar solo una evidencia, aunque el texto tenga varias ideas.", "why": "Se cree que basta con una.", "fix": "Combina dibujo, elección y frase."},
        {"wrong": "No revisar el dibujo con el texto.", "why": "Se confía en la primera idea.", "fix": "Compara cada detalle con lo que oíste."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Leo has a blue pencil.» ¿Quién tiene el lápiz?", "Leo", "El texto lo dice."),
            ex(ADULT + "«Leo has a blue pencil.» ¿De qué color es el lápiz?", "Azul", "Blue es azul."),
            ex(ADULT + "«Leo says: Thank you!» ¿Qué dice Leo?", "Gracias", "Thank you es gracias."),
        ],
        "understand": [
            ex("¿Qué es una «evidencia» de que entendiste?", "Una prueba, como dibujar, elegir o decir", "Cada evidencia muestra comprensión."),
            ex("¿Por qué conviene dar más de una evidencia?", "Porque cada una muestra una parte distinta de lo que entendí", "Se completa la comprensión."),
            ex("¿Qué haces después de dibujar?", "Reviso mi dibujo con el texto", "Así corrijo errores."),
        ],
        "apply": [
            ex(ADULT + "«Mia has a green book. The book is on the chair.» ¿Dónde está el libro?", "Sobre la silla", "On the chair es sobre la silla."),
            ex(ADULT + "«Mia has a green book. The book is on the chair.» ¿De qué color es el libro?", "Verde", "Green es verde."),
            ex(ADULT + "«A: Good morning! B: Good morning! A: Here you are. B: Thank you!» ¿Quién agradece?", "B", "B dice thank you."),
        ],
        "reason": [
            ex("Un niño dibujó un libro rojo, pero el texto dijo «green book». ¿Qué debe cambiar?", "El color: debe ser verde", "Green significa verde."),
            ex("¿Por qué decir «Thank you» puede ser una evidencia de comprensión en un diálogo?", "Porque muestra que entendí que recibió algo", "Usa la expresión correcta en el momento correcto."),
        ],
        "challenge": [
            ex(ADULT + "«Tom has two small balls. One is red. One is blue. Tom says: Look!» ¿Cuántas pelotas hay y de qué colores?", "2; roja y azul", "Two es dos y se nombran red y blue."),
            ex("Escribe una evidencia posible en español de que entendiste «Pia has a small red ball».", "Dibujo de una pelota roja pequeña con Pía", "Un dibujo coherente prueba comprensión."),
        ],
    },
    context=[ex(ADULT + "«A: Hello! I'm Mia. B: Hello, Mia! I'm Leo. Do you have a pencil? A: Yes. Here you are. B: Thank you!» En clase dos niños se conocen. ¿Qué le presta Mia a Leo?", "Un lápiz", "Pencil es lápiz.")],
    selfcheck=[
        ex(ADULT + "«Ana has a red hat.» ¿De qué color es el sombrero?", "Rojo", "Red es rojo."),
        ex("¿Qué haces para mostrar que seguiste una instrucción?", "La hago con mi cuerpo o con un dibujo", "Actuar es evidencia."),
        ex("¿Qué dices al recibir algo?", "Thank you", "Es la expresión de cortesía."),
    ],
    open_task=task("Un adulto lee dos veces: «Ana has a big yellow star. The star is next to a small blue circle. Ana says: Look!» Muestra que entendiste de tres formas: dibuja, marca quién tiene la estrella (Ana) y di una frase como «Look!».", "Dibujo de una estrella amarilla grande al lado de un círculo azul pequeño, con Ana señalándolos, y dice «Look!».", ["estrella grande y amarilla", "círculo pequeño y azul al lado", "marca a Ana", "dice una frase"], ["dibujo", "nota del adulto"], ["círculo grande", "estrella azul"], "Revisen juntos el dibujo con el texto y repitan la frase que dijo."),
    reinforce="Escucha a un adulto decir «Look!» y señala algo que veas en tu casa.",
    extend="Escribe una descripción de dos líneas de algo de tu pieza y pide a otra persona que la dibuje.",
)

# ---------------------------------------------------------------- OA 04
register(
    OA4, 1,
    materials="Los títulos, descripciones de imágenes y textos escritos en cada ejercicio, que lee un adulto; lápiz.",
    use="Aprenderé a pensar de qué puede tratar un texto antes de escucharlo, usando un título o una imagen, y a cambiar mi idea si el texto dice otra cosa. Sirve para escuchar con más atención.",
    prior=["Sé qué es un título.", "Sé algunas palabras de animales y lugares."],
    explain=[
        "Predecir es pensar de qué puede tratar un texto antes de escucharlo. Si el título es «The Rainy Day» (el día lluvioso), puedes pensar que habla de lluvia, de paraguas o de quedarse en casa. Es una idea que puedes cambiar.",
        "Una predicción no es una respuesta final: es una ayuda. Mientras escuchas, comprueba. Si el texto habla de un paraguas, tu predicción era buena. Si habla de un perro que corre, cambia tu idea sin molestarte.",
        "Para predecir, mira el título y la imagen. Pregúntate: ¿qué veo?, ¿qué personajes hay?, ¿qué puede pasar? Luego escucha y comprueba con las palabras que reconozcas.",
    ],
    vocab=[("predict", "pensar qué pasará o de qué trata"), ("title", "título"), ("rainy day", "día lluvioso"), ("umbrella", "paraguas"), ("check", "comprobar"), ("change", "cambiar")],
    worked=[
        {"title": "Predecir con un título", "problem": "El título es «The Rainy Day». ¿De qué puede tratar?", "steps": ["Rainy significa lluvioso.", "Pienso en lluvia, paraguas, charcos.", "Es una idea que comprobaré."], "answer": "De un día de lluvia"},
        {"title": "Cambiar la predicción", "problem": ADULT + "Pensé que hablaba de lluvia, pero el adulto lee «The sun is hot. Tom and Ana play in the park.» ¿Qué hago con mi predicción?", "steps": ["El texto habla de sol y de parque.", "Mi idea no coincide.", "La cambio."], "answer": "Cambio mi idea: trata de un día de sol"},
    ],
    mistakes=[
        {"wrong": "Quedarse con la primera idea aunque el texto diga otra cosa.", "why": "Se piensa que la predicción es una respuesta.", "fix": "Si lo que oyes es distinto, cambia tu idea."},
        {"wrong": "No predecir nada antes de escuchar.", "why": "Se cree que hay que esperar al texto.", "fix": "Mira el título y piensa una idea corta."},
    ],
    tiers={
        "recovery": [
            ex("Un título dice «My Cat». ¿Sobre qué animal puede tratar?", "Sobre un gato", "Cat es gato."),
            ex("Un título dice «The Big Dog». ¿Qué animal esperas?", "Un perro", "Dog es perro."),
            ex("Un título dice «Happy Birthday». ¿Sobre qué puede tratar?", "Sobre un cumpleaños", "Birthday es cumpleaños."),
        ],
        "understand": [
            ex("¿Qué significa «predecir» un texto?", "Pensar de qué puede tratar antes de escucharlo", "Es una idea previa."),
            ex("¿Por qué una predicción puede cambiar?", "Porque el texto puede decir algo distinto", "Se comprueba al escuchar."),
            ex("¿Qué te ayuda a predecir?", "El título y la imagen", "Dan pistas del tema."),
        ],
        "apply": [
            ex("Un título dice «At the Beach». ¿Qué cosas esperas oír: arena y mar o nieve y esquí?", "Arena y mar", "Beach es playa."),
            ex("Una imagen muestra a un niño con paraguas bajo la lluvia. ¿Qué palabra esperas oír: rain o sun?", "rain", "La imagen muestra lluvia."),
            ex("Un título dice «The Farm». ¿Qué animales esperas: cow, pig o lion?", "cow y pig", "Una granja tiene vacas y cerdos, no leones."),
        ],
        "reason": [
            ex("Pensabas que el texto «The Big Dog» hablaba de un perro, pero el adulto lee «Meow! The big cat sits.» ¿Qué haces?", "Cambio mi idea: habla de un gato", "El texto manda sobre la predicción."),
            ex("¿Por qué no pasa nada malo si tu predicción era distinta al texto?", "Porque predecir es solo una ayuda", "Lo importante es comprobar y corregir."),
        ],
        "challenge": [
            ex("Escribe una predicción en español para el título «The Magic Hat».", "Por ejemplo: habla de un sombrero con magia", "Magic es mágico y hat es sombrero."),
            ex("Dos niños predicen sobre «The Rainy Day»: Ana dice paraguas y Beto dice playa con sol. ¿Quién tiene la mejor predicción?", "Ana", "Rainy se relaciona con lluvia y paraguas."),
        ],
    },
    context=[ex("En la biblioteca ves un libro con el título «My Pet Fish» y un dibujo de una pecera. ¿Sobre qué mascota puede tratar?", "Sobre un pez", "Fish es pez y la pecera lo apoya.")],
    selfcheck=[
        ex("¿Qué significa «title»?", "título", "Es el nombre del texto."),
        ex("Si el texto dice algo distinto, ¿qué haces con tu predicción?", "La cambio", "Se corrige al escuchar."),
        ex("¿Qué palabra esperas en «The Rainy Day»?", "rain", "Rainy se relaciona con lluvia."),
    ],
    open_task=task("Mira estos tres títulos: «The Sunny Day», «My Little Dog» y «Happy Birthday». Para uno de ellos, escribe una predicción corta y dibuja lo que esperas. Luego un adulto lee un texto de dos líneas sobre ese título («My Little Dog: The dog is small. It plays with a ball.») y tú compruebas si tu predicción coincide.", "«My Little Dog»: predigo un perrito pequeño jugando. Compruebo: el texto dice que juega con una pelota; mi idea coincide.", ["predicción escrita", "dibujo relacionado", "comprobación con el texto"], ["predicción y dibujo", "nota del adulto"], ["insistir con la predicción pese al texto", "no justificar"], "Anímalo a decir qué palabra del texto confirmó o cambió su idea."),
    reinforce="Mira la portada de un libro de tu casa y di qué crees que contiene.",
    extend="Escribe títulos de tres cuentos que te gustaría contar y qué esperas que pase en cada uno.",
)

register(
    OA4, 2,
    materials="Los textos y preguntas escritos en cada ejercicio, que lee un adulto; lápiz.",
    use="Aprenderé a usar lo que ya sé del mundo para entender mejor un texto en inglés. Sirve para comprender más aunque haya palabras nuevas.",
    prior=["Sé qué pasa en un cumpleaños.", "Sé qué hacen los animales de una granja."],
    explain=[
        "Tú ya sabes muchas cosas: cómo es un cumpleaños, qué come un perro, qué se hace en la escuela. Esas ideas se llaman conocimientos previos. Úsalas para entender un texto en inglés.",
        "Por ejemplo, si el adulto lee «It's Ana's birthday. Her friends sing and eat cake», aunque no conozcas todas las palabras, sabes que en un cumpleaños hay torta, canciones y amigos. Eso te ayuda a entender birthday, sing y cake.",
        "Antes de escuchar, piensa: ¿qué sé de este tema? Después de escuchar, pregúntate: ¿mi idea ayudó? Los conocimientos previos son una pista, igual que las imágenes y los sonidos.",
    ],
    vocab=[("birthday", "cumpleaños"), ("cake", "torta"), ("farm", "granja"), ("animals", "animales"), ("school", "escuela"), ("I know", "yo sé")],
    worked=[
        {"title": "Usar lo que sé", "problem": ADULT + "«It's Ana's birthday. Her friends sing and eat cake.» ¿Qué palabra entiendes gracias a lo que sabes de un cumpleaños: cake?", "steps": ["Sé que en cumpleaños hay torta.", "Entiendo que cake es torta."], "answer": "cake es torta"},
        {"title": "Predecir con lo que sé", "problem": "Si el texto habla de una granja, ¿qué animales espero?", "steps": ["Pienso en lo que sé de granjas.", "Hay vacas, cerdos y gallinas."], "answer": "Cow, pig y hen"},
    ],
    mistakes=[
        {"wrong": "Pensar que lo que sé no sirve porque el texto está en inglés.", "why": "Se separa el idioma del conocimiento.", "fix": "Piensa en el tema: ya sabes cosas sobre él."},
        {"wrong": "Usar un conocimiento que no tiene que ver con el texto.", "why": "Se mezclan ideas.", "fix": "Verifica que tu idea coincida con las palabras que oyes."},
    ],
    tiers={
        "recovery": [
            ex("En un cumpleaños, ¿qué hay sobre la mesa: cake o book?", "cake", "La torta es típica de cumpleaños."),
            ex("En una granja, ¿hay cow o dolphin?", "cow", "La vaca vive en la granja."),
            ex("En la escuela, ¿usas pencil o spoon para escribir?", "pencil", "El lápiz sirve para escribir."),
        ],
        "understand": [
            ex("¿Qué son los «conocimientos previos»?", "Lo que ya sé sobre un tema", "Ayudan a comprender."),
            ex("¿Cómo te ayudan a entender un texto en inglés?", "Me dan ideas de lo que puede decir", "Se complementan con las palabras que oigo."),
            ex("¿Cuándo conviene pensar en lo que sabes?", "Antes y durante la escucha", "Prepara y ayuda a comprender."),
        ],
        "apply": [
            ex(ADULT + "«On the farm there is a cow. The cow says moo.» ¿Qué sonido hace la vaca?", "Moo", "El texto lo dice y coincide con lo que sé."),
            ex(ADULT + "«At the birthday party, we sing and blow the candles.» ¿En qué ocasión ocurre?", "En un cumpleaños", "Cantar y soplar velas se hace en cumpleaños."),
            ex(ADULT + "«At school I have a book, a pencil and a bag.» ¿Dónde está la persona?", "En la escuela", "School es escuela."),
        ],
        "reason": [
            ex("Ana oyó «farm» y pensó en un tigre. ¿Qué conocimiento previo la ayudaría más?", "Pensar en vacas, cerdos y gallinas", "Esos son animales de granja."),
            ex("¿Por qué conviene comprobar tu idea con las palabras que oyes?", "Porque mi idea puede no coincidir con el texto", "Así se evitan errores."),
        ],
        "challenge": [
            ex("Escribe tres cosas que sabes de un cumpleaños.", "Por ejemplo: torta, regalos y canciones", "Son ideas típicas de ese tema."),
            ex("Escribe una cosa que esperas oír en un texto sobre la playa.", "Por ejemplo: sand, sea o sun", "Son palabras del tema."),
        ],
    },
    context=[ex(ADULT + "«It's my birthday. I have a big cake and many friends.» Cuando tu amiga cuenta esto, ¿qué palabra puedes entender usando lo que sabes: friends o cake?", "cake", "Sé que en cumpleaños hay torta.")],
    selfcheck=[
        ex("¿Qué significa «birthday»?", "cumpleaños", "Es el día en que cumples años."),
        ex("¿Qué animales hay en una granja?", "Por ejemplo: vaca, cerdo y gallina", "Son animales de granja."),
        ex("¿Qué debes hacer con tu idea previa?", "Comprobarla con el texto", "El texto confirma o corrige."),
    ],
    open_task=task("Un adulto lee dos veces: «It's Lola's birthday. Lola has a big cake and three red balloons. Her friends sing.» Antes de que lea, escribe tres cosas que sabes de un cumpleaños. Luego marca cuáles aparecieron en el texto.", "Sé: torta, globos, canciones. Aparecieron las tres: cake, balloons y sing.", ["escribe tres ideas previas", "marca las que aparecen", "explica con una palabra del texto"], ["lista de ideas", "nota del adulto"], ["ideas que no tienen que ver con el tema", "no comprobar con el texto"], "Pídele que diga qué idea suya le ayudó más a entender."),
    reinforce="Piensa qué sabes de las mascotas y di tres palabras en español.",
    extend="Elige un tema (el parque, la escuela o la playa) y escribe cinco palabras que esperarías oír.",
)

register(
    OA4, 3,
    materials="Las descripciones de imágenes escritas en cada ejercicio, que lee un adulto; lápiz.",
    use="Aprenderé a usar imágenes para entender mejor un texto, pero comprobando con las palabras. Sirve para no quedarme solo con lo que adivino.",
    prior=["Sé que una imagen da pistas.", "Sé algunas palabras como cat, dog, sun y rain."],
    explain=[
        "Las imágenes son una gran ayuda para entender. Si ves un dibujo de un gato en un árbol y oyes «cat» y «tree», sabes que hablan de eso. Pero una imagen no dice todo: puede mostrar un gato y el texto hablar de lo que el gato siente.",
        "Por eso se usa la imagen junto con las palabras. Mira la imagen, escucha el texto y comprueba que ambos coincidan. Si no coinciden, confía más en el texto.",
        "Una buena forma de usar una imagen es describirla antes de escuchar: «Veo un niño, una pelota y un parque». Luego escuchas y buscas esas palabras. Si encuentras algo distinto, anótalo.",
    ],
    vocab=[("picture", "imagen"), ("I see", "yo veo"), ("tree", "árbol"), ("sun", "sol"), ("rain", "lluvia"), ("match", "coincidir")],
    worked=[
        {"title": "Imagen y texto coinciden", "problem": "La imagen muestra un gato sobre un árbol. Un adulto lee: «The cat is on the tree.» ¿Coinciden?", "steps": ["Veo un gato y un árbol.", "El texto dice cat y tree.", "Coinciden."], "answer": "Sí, coinciden"},
        {"title": "Imagen y texto no coinciden", "problem": "La imagen muestra un perro. Un adulto lee: «The cat is sleeping.» ¿Qué hago?", "steps": ["Veo un perro.", "El texto dice cat.", "No coinciden, así que me guío por el texto."], "answer": "Confío en el texto: es un gato"},
    ],
    mistakes=[
        {"wrong": "Responder solo mirando la imagen y no escuchando.", "why": "Se piensa que la imagen lo dice todo.", "fix": "Comprueba con las palabras que oyes."},
        {"wrong": "Ignorar la imagen y solo tratar de traducir.", "why": "Se pierde una ayuda.", "fix": "Mira la imagen y descríbela antes de escuchar."},
    ],
    tiers={
        "recovery": [
            ex("La imagen muestra un sol. ¿Qué palabra esperas oír: sun o moon?", "sun", "Sun es sol."),
            ex("La imagen muestra lluvia. ¿Qué palabra esperas: rain o snow?", "rain", "Rain es lluvia."),
            ex("La imagen muestra un perro. ¿Qué palabra esperas: dog o cat?", "dog", "Dog es perro."),
        ],
        "understand": [
            ex("¿Por qué una imagen ayuda a entender?", "Porque muestra lo que el texto puede decir", "Da pistas de lo que dice."),
            ex("¿Qué haces si la imagen y el texto no coinciden?", "Confío más en el texto", "Las palabras dan la información exacta."),
            ex("¿Qué significa «I see»?", "yo veo", "Se usa para describir una imagen."),
        ],
        "apply": [
            ex("La imagen muestra una niña con paraguas. Un adulto lee: «It's rainy. Pia has an umbrella.» ¿Coinciden?", "Sí", "Rainy y umbrella coinciden con la imagen."),
            ex("La imagen muestra un pez. Un adulto lee: «The cat is big.» ¿Coinciden?", "No", "El texto habla de un gato, no de un pez."),
            ex("La imagen muestra a un niño con una pelota roja. Un adulto lee: «Leo has a red ball.» ¿Qué tiene Leo?", "Una pelota roja", "Ambas pistas coinciden."),
        ],
        "reason": [
            ex("¿Por qué no basta con mirar solo la imagen?", "Porque la imagen no dice todo lo que dice el texto", "Las palabras pueden dar más datos."),
            ex("Mia vio un perro en la imagen, pero oyó «cat». ¿Qué debe hacer?", "Preguntar o escuchar de nuevo y cambiar su idea", "El texto corrige la imagen."),
        ],
        "challenge": [
            ex("Describe en español una imagen de un parque con sol y niños jugando.", "Hay un parque soleado donde juegan niños", "Describe objetos y acciones."),
            ex("Escribe una frase en inglés para una imagen de un gato sobre una silla.", "The cat is on the chair", "Usa on para sobre."),
        ],
    },
    context=[ex("En una tarjeta ves un dibujo de una torta con velas y oyes «Happy birthday!». ¿Qué te dice la imagen?", "Que es un cumpleaños", "La imagen y las palabras coinciden.")],
    selfcheck=[
        ex("¿Qué significa «picture»?", "imagen", "Es un dibujo o foto."),
        ex("Si la imagen y el texto no coinciden, ¿en qué confías más?", "En el texto", "Es la información exacta."),
        ex("¿Qué haces antes de escuchar con una imagen?", "La describo", "Así preparo las palabras."),
    ],
    open_task=task("Observa esta escena que describe el adulto: «Un niño con paraguas amarillo, un charco y un gato bajo un árbol». Escríbela o di tres frases de lo que ves («I see a boy», «I see a cat»...). Luego un adulto lee «It's rainy. The boy has an umbrella. The cat is under the tree.» y tú compruebas qué coincide.", "I see a boy. I see a cat. I see a tree. Coinciden: boy, cat, tree, umbrella.", ["tres frases con «I see»", "señala lo que coincide", "dice si algo no coincide"], ["frases", "nota del adulto"], ["describir cosas que no están", "no comprobar con el texto"], "Pídele que señale una palabra del texto que confirma lo que vio."),
    reinforce="Mira una imagen de un libro y di tres cosas que ves en español.",
    extend="Dibuja una escena y escribe tres frases «I see...» para describirla.",
)

register(
    OA4, 4,
    materials="Los textos con palabras clave escritos en cada ejercicio, que lee un adulto; lápices de colores.",
    use="Aprenderé a escuchar solo las palabras importantes (nombres, números, colores) cuando me hacen una pregunta. Sirve para encontrar rápido la respuesta.",
    prior=["Sé algunos colores y números en inglés.", "Sé que las preguntas piden información."],
    explain=[
        "Una palabra clave es una palabra que te da la información importante. Si te preguntan «What color is the ball?», la palabra clave es el color. No necesitas entender cada palabra: solo escuchar la que responde.",
        "Antes de escuchar, lee la pregunta y decide qué buscas: un número, un color, un nombre o un lugar. Si la pregunta es How many?, busca un número. Si es What color?, busca un color. Si es Who?, busca un nombre.",
        "Así escuchas con un objetivo. Cuando oigas la palabra que buscas, tómala. Las otras palabras pueden ayudar, pero no son necesarias para responder.",
    ],
    vocab=[("key word", "palabra clave"), ("how many?", "¿cuántos?"), ("what color?", "¿de qué color?"), ("who?", "¿quién?"), ("where?", "¿dónde?"), ("listen for", "escuchar para encontrar")],
    worked=[
        {"title": "Buscar un color", "problem": ADULT + "«The ball is big and red. It is on the table.» Pregunta: What color is the ball?", "steps": ["La pregunta pide un color.", "Escucho red.", "Es la palabra clave."], "answer": "Rojo"},
        {"title": "Buscar un número", "problem": ADULT + "«Tom has four pencils and two books.» Pregunta: How many pencils?", "steps": ["La pregunta pide un número de lápices.", "Escucho four pencils."], "answer": "4"},
    ],
    mistakes=[
        {"wrong": "Querer entender todas las palabras antes de responder.", "why": "Se cree que hay que comprender todo.", "fix": "Lee la pregunta y escucha solo la palabra clave."},
        {"wrong": "Responder con el número equivocado porque se escuchó otro número.", "why": "Se oye uno y se olvida el objeto.", "fix": "Escucha el número junto al objeto por el que preguntan."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«The cat is black.» ¿De qué color es el gato?", "Negro", "Black es negro."),
            ex(ADULT + "«I have three balls.» ¿Cuántas pelotas hay?", "3", "Three es tres."),
            ex(ADULT + "«Ana is my friend.» ¿Quién es mi amiga?", "Ana", "El nombre es la palabra clave."),
        ],
        "understand": [
            ex("¿Qué es una palabra clave?", "La palabra que da la información importante", "Responde a lo que se pregunta."),
            ex("Si la pregunta es «What color?», ¿qué buscas al escuchar?", "Un color", "Se escucha red, blue, green..."),
            ex("Si la pregunta es «How many?», ¿qué buscas?", "Un número", "Se busca la cantidad."),
        ],
        "apply": [
            ex(ADULT + "«Leo has a blue bag and a red hat.» ¿De qué color es el sombrero?", "Rojo", "Red es rojo."),
            ex(ADULT + "«Mia has two cats and four fish.» ¿Cuántos peces tiene Mia?", "4", "Four fish son cuatro peces."),
            ex(ADULT + "«Pedro is in the park. Ana is at school.» ¿Dónde está Ana?", "En la escuela", "At school es en la escuela."),
        ],
        "reason": [
            ex("Alguien pregunta «How many books?» y el adulto dice «Two books and one pencil». Un niño responde 1. ¿Qué error cometió?", "Escuchó el número del lápiz, no el de los libros", "Debe mirar el objeto por el que preguntan."),
            ex("¿Por qué ayuda leer la pregunta antes de escuchar?", "Porque así sé qué palabra clave buscar", "Escuchas con un objetivo."),
        ],
        "challenge": [
            ex(ADULT + "«Tom has two red balls, one blue ball and three green balls.» ¿Cuántas pelotas verdes hay?", "3", "Three green balls son tres verdes."),
            ex(ADULT + "«Ana's cat is white. Leo's cat is black. Pia's cat is orange.» ¿De quién es el gato negro?", "De Leo", "Black es negro y es el gato de Leo."),
        ],
    },
    context=[ex(ADULT + "«The bus is yellow. It has twenty seats.» Un niño mira un bus escolar con su abuelo, quien describe esto en inglés. ¿De qué color es el bus?", "Amarillo", "Yellow es amarillo.")],
    selfcheck=[
        ex("¿Qué significa «key word»?", "palabra clave", "Es la palabra importante."),
        ex(ADULT + "«I have five pencils.» ¿Cuántos lápices?", "5", "Five es cinco."),
        ex("Si la pregunta es «Who?», ¿qué buscas?", "Un nombre", "Who pide una persona."),
    ],
    open_task=task("Un adulto lee dos veces: «Pia has two small cats. One cat is white and one is black. They are in the garden.» Primero lee la pregunta, luego responde las tres: (1) How many cats? (2) What color is the second cat? (3) Where are the cats?", "(1) Two. (2) Black. (3) In the garden.", ["responde las tres preguntas", "usa palabras clave", "no se confunde de color ni de número"], ["respuestas escritas o dichas", "nota del adulto"], ["decir que los gatos son tres", "decir que ambos son blancos"], "Muéstrale con un dedo la palabra que respondía a cada pregunta y repite el texto."),
    reinforce="Escucha a un adulto decir «I have two books» y levanta dos dedos.",
    extend="Escribe tres preguntas cortas en español sobre un texto de dos líneas y marca la palabra clave de cada una.",
)

register(
    OA4, 5,
    materials="Los textos cortos escritos en cada ejercicio, que lee un adulto dos o tres veces; lápiz.",
    use="Aprenderé a escuchar de nuevo para revisar y mejorar mi respuesta. Sirve para entender más en cada lectura y corregir errores.",
    prior=["Sé predecir y buscar palabras clave.", "Sé que repetir una escucha ayuda a comprender."],
    explain=[
        "Escuchar una sola vez a veces no alcanza. Por eso se escucha de nuevo: la primera vez se capta la idea general, la segunda vez se buscan detalles y la tercera se revisa la respuesta.",
        "Después de escuchar, di tu idea. Luego escucha otra vez con una pregunta nueva, por ejemplo: ¿qué color?, ¿cuántos? Si tu respuesta cambia, corrígela. No es un error cambiar: es mejorar lo que entendiste.",
        "Pide «Again, please» las veces que necesites. Revisa tu respuesta marcando las palabras del texto que la apoyan. Si no encuentras una, vuelve a escuchar.",
    ],
    vocab=[("again, please", "otra vez, por favor"), ("first time", "primera vez"), ("second time", "segunda vez"), ("check", "revisar"), ("change", "cambiar"), ("detail", "detalle")],
    worked=[
        {"title": "Primera y segunda escucha", "problem": ADULT + "«Mia has a small blue bag. The bag is on the chair.» Primera vez: ¿quién tiene algo? Segunda vez: ¿de qué color es la mochila?", "steps": ["Primera vez: Mia tiene una mochila.", "Segunda vez: escucho blue.", "Respondo azul."], "answer": "Mia; azul"},
        {"title": "Corregir una respuesta", "problem": "Pensé que la mochila era roja pero la segunda vez oí «blue». ¿Qué hago?", "steps": ["Mi respuesta no coincide.", "La cambio a azul."], "answer": "Cambio mi respuesta a azul"},
    ],
    mistakes=[
        {"wrong": "No volver a escuchar por miedo a molestar.", "why": "Se cree que hay que entender todo a la primera.", "fix": "Pide «Again, please»; es normal."},
        {"wrong": "Cambiar la respuesta sin escuchar de nuevo.", "why": "Se duda sin evidencia.", "fix": "Cambia solo si el texto lo apoya."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué dices para pedir que repitan?", "Again, please", "Es la frase amable."),
            ex("¿Cuántas veces puedes pedir que repitan un texto?", "Las que necesites", "Escuchar de nuevo ayuda a comprender."),
            ex("En la primera escucha, ¿qué buscas?", "La idea general", "Luego buscas detalles."),
        ],
        "understand": [
            ex("¿Para qué sirve escuchar por segunda vez?", "Para buscar detalles y revisar mi respuesta", "La segunda escucha sirve para precisar."),
            ex("¿Es malo cambiar una respuesta después de escuchar otra vez?", "No, es mejorar mi comprensión", "Corregir es parte de aprender."),
            ex("¿Qué haces para revisar una respuesta?", "Busco la palabra del texto que la apoya", "La evidencia confirma."),
        ],
        "apply": [
            ex(ADULT + "«Tom has two green frogs. One frog is big and one is small.» Primera vez: ¿qué tiene Tom?", "Dos ranas verdes", "Frogs son ranas."),
            ex(ADULT + "«Tom has two green frogs. One frog is big and one is small.» Segunda vez: ¿cuántas ranas son pequeñas?", "1", "One is small."),
            ex(ADULT + "«Pia is in the park. She has a red kite.» Segunda vez: ¿de qué color es la cometa?", "Roja", "Red kite es cometa roja."),
        ],
        "reason": [
            ex("Un niño respondió «dos pelotas» pero al escuchar de nuevo oyó «three balls». ¿Qué debe hacer?", "Cambiar su respuesta a tres", "El texto confirma tres."),
            ex("¿Por qué es mejor escuchar más de una vez?", "Porque cada vez se entiende más", "Se pasa de la idea general al detalle."),
        ],
        "challenge": [
            ex(ADULT + "«Leo has two cats, three dogs and one fish.» ¿Cuántos animales tiene Leo en total?", "6", "Dos más tres más uno son seis."),
            ex("Escribe en español dos preguntas que podrías contestar con una segunda escucha del texto «Mia has a small blue bag».", "Por ejemplo: ¿de qué color es? y ¿cómo es de grande?", "Son detalles que se buscan en la segunda escucha."),
        ],
    },
    context=[ex(ADULT + "«Today is Monday. We have art class at ten.» En la escuela, tu profesora lee el horario en inglés. Si quieres saber a qué hora es arte, ¿qué número buscas?", "Diez", "Ten es diez.")],
    selfcheck=[
        ex("¿Qué significa «again»?", "otra vez", "Se usa para pedir repetir."),
        ex("Si cambias tu respuesta, ¿qué la debe apoyar?", "El texto", "Debe haber una palabra que lo confirme."),
        ex("¿Qué se busca en la primera escucha?", "La idea general", "Es el primer paso."),
    ],
    open_task=task("Un adulto lee tres veces: «Ana has four yellow flowers. Two flowers are small. Two flowers are big.» Primera vez: dibuja las flores. Segunda vez: revisa el color y el tamaño. Tercera vez: corrige lo que no coincide.", "Cuatro flores amarillas, dos pequeñas y dos grandes.", ["dibuja cuatro flores", "las pinta de amarillo", "dos pequeñas y dos grandes", "corrige tras la segunda y tercera escucha"], ["primer y último dibujo", "nota del adulto"], ["dibujar tres flores", "pintarlas de otro color"], "Mira con él qué cambió entre el primer y el último dibujo y celebra la corrección."),
    reinforce="Pide a un adulto que lea «I have three books» dos veces y cuenta tus dedos al oír el número.",
    extend="Escribe un texto de dos líneas en español y pide a alguien que lo lea dos veces para responder tres preguntas.",
)
