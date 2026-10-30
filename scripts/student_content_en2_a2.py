"""Student material for 2.º básico Inglés, EN02 OA 03 (evidencia de comprensión oral y sonidos /s/-/z/, /w/-/th/) y OA 04 (estrategias de escucha).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado.
Los sonidos se describen con palabras y con la posición de la boca; no se usa audio externo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA3, OA4 = "EN02 OA 03", "EN02 OA 04"
ADULT = "Un adulto lee en voz alta (el estudiante tapa el guion): "


# ---------------------------------------------------------------- OA 03
register(
    OA3, 1,
    materials="Los textos orales escritos en cada ejercicio, que lee un adulto; lápiz y papel para dibujar.",
    use="Aprenderé a mostrar que entiendo un texto oral identificando a las personas, los animales y los objetos que aparecen. Sirve para comprobar que escuchaste bien lo que dijeron en inglés.",
    prior=["Conozco palabras de la escuela, de animales salvajes y de la casa.", "Sé escuchar buscando palabras clave."],
    explain=[
        "Cuando entiendes un texto oral, puedes decir quién aparece (people), qué animales hay (animals) y qué objetos se nombran (objects). Escucha los nombres de personas, como teacher (profesor), nurse (enfermera) o friend (amigo); los animales, como lion, elephant, giraffe, zebra, monkey y tiger; y los objetos, como table, chair, bed, book y bag.",
        "Una buena forma de mostrar que entiendes es dibujar o señalar. Si el adulto dice «I see a zebra next to a tree», puedes dibujar una cebra y un árbol. También puedes responder a preguntas cortas: Who is it? (¿quién es?) What is it? (¿qué es?) What animal is it? (¿qué animal es?)",
        "No necesitas entender todo el texto. Busca las palabras de personas, animales y objetos. Si oyes una descripción como «It is big and gray. It has a long nose», piensa en el animal que cumple las pistas: es un elefante (elephant). Otras pistas útiles: long neck (cuello largo), black and white lines (rayas blancas y negras), orange and black (naranja y negro), It can run fast (puede correr rápido).",
    ],
    vocab=[("lion", "león"), ("elephant", "elefante"), ("giraffe", "jirafa"), ("zebra", "cebra"), ("monkey", "mono"), ("teacher", "profesor o profesora")],
    worked=[
        {"title": "Identificar un animal", "problem": ADULT + "«It is big and gray. It has a long nose.» ¿Qué animal es?", "steps": ["Oigo big and gray: grande y gris.", "Oigo long nose: nariz larga.", "El animal que cumple las pistas es el elefante."], "answer": "Un elefante (elephant)"},
        {"title": "Identificar un objeto y una persona", "problem": ADULT + "«The teacher has a red book. The book is on the desk.» ¿Quién es la persona y qué objeto aparece?", "steps": ["La persona es the teacher.", "El objeto es a red book.", "El libro está on the desk."], "answer": "La profesora o el profesor; un libro rojo"},
    ],
    mistakes=[
        {"wrong": "Decir lion cuando el texto describe un animal con cuello largo y manchas.", "why": "Se piensa en el primer animal conocido sin comprobar las pistas.", "fix": "Reúne las pistas (cuello largo, manchas) y elige la jirafa (giraffe)."},
        {"wrong": "Responder con el nombre del objeto cuando la pregunta es Who is it?", "why": "Se confunde quién (persona) con qué (objeto).", "fix": "Who pide una persona y what pide un objeto o un animal."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«I see a lion.» ¿Qué animal ve la persona?", "Un león", "Lion es león."),
            ex(ADULT + "«The teacher is in the school.» ¿Quién está en la escuela?", "La profesora o el profesor", "Teacher es profesor o profesora."),
            ex(ADULT + "«I have a book.» ¿Qué objeto tiene?", "Un libro", "Book es libro."),
        ],
        "understand": [
            ex("¿Qué pregunta usas para saber qué es un objeto: Who is it? o What is it?", "What is it?", "What pregunta por cosas o animales; who por personas."),
            ex("¿Cuál de estos es un animal salvaje: zebra, table o book?", "zebra", "Zebra es cebra; table y book son objetos."),
            ex("¿Qué significa «friend»?", "amigo o amiga", "Friend es una persona."),
        ],
        "apply": [
            ex(ADULT + "«It is yellow and brown. It has a very long neck.» ¿Qué animal es?", "Una jirafa", "Neck es cuello y la jirafa lo tiene muy largo."),
            ex(ADULT + "«It has black and white lines. It is next to a tree.» ¿Qué animal es?", "Una cebra", "Black and white lines son rayas blancas y negras."),
            ex(ADULT + "«The girl is on the sofa. She has a bag.» ¿Qué objeto tiene la niña?", "Una mochila o un bolso", "Bag es mochila o bolso."),
        ],
        "reason": [
            ex("Una niña oye «It is orange and black. It can run fast.» y dice que es una cebra. ¿Qué pista contradice su respuesta?", "Orange and black: la cebra es blanca y negra", "Las pistas de color indican un tigre."),
            ex(ADULT + "«A monkey is in the tree. It has a banana.» ¿Qué dos cosas ves en la escena?", "Un mono y un plátano (en un árbol)", "Monkey y banana son el animal y el objeto nombrados."),
        ],
        "challenge": [
            ex(ADULT + "«The doctor is in the hospital. A nurse is next to the doctor. They have a bed.» Responde: ¿cuántas personas hay y qué objeto aparece?", "Dos personas (un médico y una enfermera); una cama", "Doctor y nurse son dos personas, y bed es cama."),
            ex(ADULT + "«I see a big animal. It is gray. It has a long nose. It is in the zoo.» ¿Qué animal es y dónde está?", "Un elefante; en el zoológico", "Long nose es elefante y zoo es zoológico."),
        ],
    },
    context=[ex("En un paseo al zoológico, un guía dice: " + ADULT + "«Look! A lion is under the tree. A monkey is in the tree.» ¿Qué animal está en el árbol?", "El mono", "Monkey is in the tree dice que el mono está en el árbol.")],
    selfcheck=[
        ex("¿Cómo se dice «jirafa» en inglés?", "giraffe", "Giraffe es jirafa."),
        ex(ADULT + "«I see a teacher.» ¿Es una persona o un animal?", "Una persona", "Teacher es profesor o profesora."),
        ex("¿Qué pregunta usas para saber la persona: Who is it? o What is it?", "Who is it?", "Who pregunta por personas."),
    ],
    open_task=task("Un adulto lee dos veces: «I see a zebra and a giraffe. The zebra is next to a tree. The giraffe has a long neck. A teacher has a book.» Dibuja lo que oyes y rotula en inglés: zebra, giraffe, tree, teacher, book. Luego responde en voz alta: What animals can you see? (zebra y giraffe).", "Dibujo con cebra, jirafa, árbol, profesor o profesora con libro; rótulos en inglés.", ["dibuja los dos animales y una persona", "dibuja el árbol y el libro", "rotula con palabras en inglés"], ["dibujo rotulado", "nota del adulto"], ["dibujar un león en lugar de una cebra", "no rotular"], "Compara el dibujo con las palabras clave del texto y pídele que explique qué pista usó."),
    reinforce="Pide a un adulto que diga «zebra, giraffe, lion» y señala los dibujos o juguetes que correspondan.",
    extend="Elige un animal salvaje y escribe en inglés tres pistas, por ejemplo «It is big. It is gray. It has a long nose.»",
)

register(
    OA3, 2,
    materials="Las instrucciones escritas en cada ejercicio, que lee un adulto; papel, lápiz y lápices de colores.",
    use="Aprenderé a seguir instrucciones en orden: primero, luego y al final. Sirve para dibujar, armar y moverme siguiendo lo que dicen en inglés.",
    prior=["Sé seguir instrucciones simples como open, close y stand up.", "Conozco colores y figuras en inglés."],
    explain=[
        "Una instrucción simple tiene un verbo y un objeto: Draw a circle (dibuja un círculo), Color it red (píntalo de rojo), Put the book on the table (pon el libro sobre la mesa). Cuando hay varias instrucciones, el adulto usa palabras de orden: First (primero), Then (luego) y Finally (al final).",
        "Para seguirlas, escucha una instrucción a la vez y hazla antes de pasar a la siguiente. Si las instrucciones son largas, anota una palabra de cada una: por ejemplo, circle, red, line. Así recuerdas el orden aunque se te olvide la frase completa.",
        "Las figuras geométricas que usarás son circle (círculo), square (cuadrado), triangle (triángulo) y rectangle (rectángulo). Los colores son red, blue, yellow y green. Con ellas puedes dibujar lo que se pide y mostrar que entendiste. Palabras de lugar y forma: inside (dentro de), on top of (encima de), under (debajo de), line (línea), roof (techo de una casa).",
    ],
    vocab=[("first", "primero"), ("then", "luego"), ("finally", "al final"), ("draw", "dibujar"), ("color", "pintar, colorear"), ("rectangle", "rectángulo")],
    worked=[
        {"title": "Seguir tres pasos", "problem": ADULT + "«First, draw a circle. Then, color it red. Finally, draw a line under the circle.» ¿Qué dibujas y en qué orden?", "steps": ["First: dibujo un círculo.", "Then: lo pinto de rojo.", "Finally: dibujo una línea debajo del círculo."], "answer": "Un círculo rojo con una línea debajo"},
        {"title": "Palabras de orden", "problem": ADULT + "«First, stand up. Then, touch your nose. Finally, sit down.» ¿Qué haces al final?", "steps": ["Finally significa al final.", "Después de finally oigo sit down."], "answer": "Me siento"},
    ],
    mistakes=[
        {"wrong": "Hacer la última instrucción primero.", "why": "No se escucharon las palabras first, then y finally.", "fix": "Subraya mentalmente first, then y finally para ordenar lo que haces."},
        {"wrong": "Pintar de verde porque se oyó solamente «color».", "why": "Se olvida el color que dice la instrucción.", "fix": "Después de color, escucha la palabra del color: red es rojo y green es verde."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Draw a square.» ¿Qué dibujas?", "Un cuadrado", "Square es cuadrado."),
            ex(ADULT + "«Color it blue.» ¿De qué color lo pintas?", "Azul", "Blue es azul."),
            ex("¿Qué significa «finally»?", "al final", "Finally es la última palabra de orden."),
        ],
        "understand": [
            ex("¿Qué significan first, then y finally?", "primero, luego y al final", "Son palabras que ordenan los pasos."),
            ex("¿Qué haces con una instrucción larga?", "Hago una instrucción a la vez, en orden", "Así no se pierde ningún paso."),
            ex("¿Qué significa «triangle»?", "triángulo", "Triangle es una figura de tres lados."),
        ],
        "apply": [
            ex(ADULT + "«First, draw a triangle. Then, color it yellow.» ¿De qué color es el triángulo?", "Amarillo", "Yellow es amarillo."),
            ex(ADULT + "«First, draw a rectangle. Then, draw a circle inside the rectangle.» ¿Dónde queda el círculo?", "Dentro del rectángulo", "Inside the rectangle es dentro del rectángulo."),
            ex(ADULT + "«First, put your pencil on the table. Then, pick up your book.» ¿Qué tomas al final?", "Mi libro", "Pick up your book es toma tu libro."),
        ],
        "reason": [
            ex("Mateo dibujó primero un cuadrado y después un círculo, pero la instrucción era «First, draw a circle. Then, draw a square.» ¿Qué debió hacer?", "Dibujar primero el círculo y luego el cuadrado", "First marca lo que va primero."),
            ex(ADULT + "«First, color the circle green. Then, color the square red.» ¿De qué color es el cuadrado?", "Rojo", "Red es rojo; el círculo es green."),
        ],
        "challenge": [
            ex(ADULT + "«First, draw a big square. Then, draw a triangle on top of the square. Finally, color the triangle red.» ¿Qué dibujo queda?", "Una casa: un cuadrado con un triángulo rojo arriba", "On top of significa encima de."),
            ex("Ordena los pasos para dibujar una casa: (1) Color the roof red. (2) Draw a square. (3) Draw a triangle on top.", "2, 3, 1", "Primero el cuadrado, luego el triángulo y al final se pinta el techo."),
        ],
    },
    context=[ex("Un profesor da estas instrucciones antes del recreo: " + ADULT + "«First, close your book. Then, put it in your bag. Finally, stand up.» ¿Qué haces después de poner el libro en la mochila?", "Me pongo de pie", "Finally, stand up es la última instrucción.")],
    selfcheck=[
        ex("¿Cómo se dice «luego» en inglés?", "then", "Then es luego."),
        ex(ADULT + "«Draw a circle.» ¿Qué figura dibujas?", "Un círculo", "Circle es círculo."),
        ex("¿Qué haces primero al oír «First, ...»?", "La primera instrucción", "First indica el primer paso."),
    ],
    open_task=task("Un adulto lee dos veces: «First, draw a square. Then, draw a triangle on top of the square. Finally, color the triangle red and the square blue.» Haz el dibujo en tu cuaderno. Después di en voz alta los tres pasos: first, then y finally, con las palabras square, triangle, red y blue.", "Una casa con techo rojo triangular y un cuerpo azul cuadrado.", ["dibuja los pasos en el orden correcto", "usa los colores indicados", "dice first, then y finally"], ["dibujo", "nota del adulto"], ["pintar el triángulo de azul", "cambiar el orden de los pasos"], "Compara el dibujo con las palabras de orden y corrige juntos el paso en que cambió el orden."),
    reinforce="Pide a un adulto que diga «First, stand up. Then, sit down.» y hazlo en ese orden.",
    extend="Escribe tres instrucciones con first, then y finally para dibujar un círculo azul.",
)

register(
    OA3, 3,
    materials="Las frases y diálogos escritos en cada ejercicio, que lee un adulto; lápiz.",
    use="Aprenderé a reconocer frases completas que se usan mucho, como «Thank you» y «Excuse me». Sirve para entender expresiones de todos los días sin traducir palabra por palabra.",
    prior=["Sé decir hello y goodbye.", "Sé que hay frases que se aprenden completas."],
    explain=[
        "Algunas frases en inglés se usan todos los días y conviene aprenderlas completas (chunks). Thank you significa gracias. Please significa por favor. Sorry significa perdón o lo siento. Excuse me se usa para pedir permiso o llamar la atención. Good morning significa buenos días. Happy birthday es feliz cumpleaños y Happy Easter es feliz Pascua. Here you are significa «aquí tienes», It's OK significa «está bien, no importa» y You're welcome significa «de nada». Con Can I ...? se pide permiso: Can I open the window? es «¿puedo abrir la ventana?».",
        "Escucha cada frase como una unidad. Por ejemplo, Excuse me no se traduce palabra por palabra: se usa cuando quieres pasar o preguntar algo. Del mismo modo, Well done significa bien hecho y Me too significa yo también.",
        "Para demostrar que las entiendes, di cuándo se usan. Si alguien te presta un lápiz, dices Thank you. Si empujas sin querer, dices Sorry. Si quieres hablar con la profesora, dices Excuse me.",
    ],
    vocab=[("Thank you.", "Gracias."), ("Sorry.", "Perdón. / Lo siento."), ("Excuse me.", "Disculpe. / Con permiso."), ("Well done!", "¡Bien hecho!"), ("Me too.", "Yo también."), ("Happy Easter!", "¡Feliz Pascua!")],
    worked=[
        {"title": "Expresión de uso frecuente", "problem": ADULT + "«A: Here is your pencil. B: Thank you!» ¿Qué dice B y qué significa?", "steps": ["B dice Thank you.", "Es una frase completa.", "Significa gracias."], "answer": "Thank you significa gracias"},
        {"title": "Cuándo se usa", "problem": ADULT + "«Excuse me, Miss. Can I open the window?» ¿Para qué dice la niña Excuse me?", "steps": ["La niña quiere hablar con la profesora.", "Excuse me sirve para llamar la atención con respeto."], "answer": "Para llamar la atención de la profesora antes de preguntar"},
    ],
    mistakes=[
        {"wrong": "Entender «Excuse me» como «excusa» o «yo» por separado.", "why": "Se traduce palabra por palabra una frase que va completa.", "fix": "Excuse me va junta y significa disculpe o con permiso."},
        {"wrong": "Responder «Sorry» cuando alguien te da algo.", "why": "Se confunde la frase para pedir perdón con la de dar gracias.", "fix": "Si te dan algo, di Thank you; si cometiste un error, di Sorry."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«Thank you!» ¿Qué significa?", "Gracias", "Thank you es gracias."),
            ex(ADULT + "«Happy Easter!» ¿Qué se celebra?", "La Pascua", "Easter es Pascua."),
            ex("¿Qué significa «Sorry»?", "Perdón o lo siento", "Se dice para pedir perdón."),
        ],
        "understand": [
            ex("¿Qué es un chunk?", "Una frase de uso frecuente que se aprende completa", "Por ejemplo Thank you o Excuse me."),
            ex("¿Por qué no conviene traducir Excuse me palabra por palabra?", "Porque la frase completa tiene un significado propio: disculpe", "Excuse me va junta."),
            ex("¿Qué significa «Well done!»", "¡Bien hecho!", "Se dice para felicitar."),
        ],
        "apply": [
            ex(ADULT + "«A: I can swim! B: Me too!» ¿Qué dice B?", "Que también sabe nadar", "Me too significa yo también."),
            ex("Tu amigo te presta un lápiz. ¿Qué frase dices: Thank you o Sorry?", "Thank you", "Se dan las gracias cuando te ayudan."),
            ex("Chocas sin querer con un compañero. ¿Qué dices: Well done o Sorry?", "Sorry", "Sorry pide perdón."),
        ],
        "reason": [
            ex("Un niño quiere preguntarle algo a la profesora que habla con otra persona. ¿Qué frase le sirve para llamarla con respeto?", "Excuse me", "Excuse me llama la atención sin interrumpir mal."),
            ex(ADULT + "«A: Look, I can draw a circle! B: Wow! Well done!» ¿Por qué dice B Well done?", "Porque felicita a A", "Well done se usa para felicitar."),
        ],
        "challenge": [
            ex("Une cada frase con lo que significa: (a) Excuse me (b) Thank you (c) Me too (d) Happy Easter", "a = disculpe, b = gracias, c = yo también, d = feliz Pascua", "Cada chunk tiene un significado propio."),
            ex(ADULT + "«A: Excuse me, can I have a pencil, please? B: Here you are. A: Thank you!» ¿Cuáles son las tres frases de cortesía que usa A?", "Excuse me, please y Thank you", "Son tres frases de uso muy frecuente."),
        ],
    },
    context=[ex("En la entrada de la escuela un niño choca con otro. " + ADULT + "«A: Sorry! B: It's OK.» ¿Qué dice A?", "Que lo siente, pide perdón", "Sorry significa perdón.")],
    selfcheck=[
        ex("¿Cómo dices «gracias» en inglés?", "Thank you", "Thank you es gracias."),
        ex("¿Cómo dices «por favor» en inglés?", "please", "Please es por favor."),
        ex(ADULT + "«Me too.» ¿Qué significa?", "Yo también", "Me too es yo también."),
    ],
    open_task=task("Un adulto representa tres situaciones y tú dices la frase correcta en inglés: (1) te da un lápiz; (2) pisa tu pie sin querer; (3) un compañero arma un rompecabezas y tú lo felicitas. Elige entre Thank you, Sorry y Well done. Después inventa una situación para «Excuse me» y represéntala con el adulto.", "(1) Thank you. (2) Sorry. (3) Well done. (4) Excuse me, can I sit here, please?", ["usa la frase adecuada en cada situación", "habla con voz clara", "inventa una situación con Excuse me"], ["nota del adulto", "dibujo de las tres situaciones"], ["usar Sorry cuando alguien te da algo", "traducir Excuse me palabra por palabra"], "Repasa con él las tres frases y pídele que explique cuándo se usa cada una."),
    reinforce="Pide a un adulto que diga «Thank you» y responde con «You're welcome» (de nada).",
    extend="Escribe un mini diálogo de tres líneas usando Excuse me, please y Thank you.",
)

register(
    OA3, 4,
    materials="Las listas de palabras escritas en cada ejercicio, que lee un adulto; lápiz. Para sentir el sonido: pon los dedos suavemente sobre tu garganta.",
    use="Aprenderé a distinguir los sonidos /s/ y /z/ del inglés. Sirve para no confundir palabras que suenan casi iguales, como sip y zip, y para entender mejor lo que escucho.",
    prior=["Sé que cada palabra tiene sonidos.", "Conozco palabras como sun, zoo y zebra."],
    explain=[
        "En inglés hay dos sonidos que se parecen: /s/ y /z/. El sonido /s/ es como una serpiente: sss. Al decirlo, tu garganta no vibra. El sonido /z/ es como una abeja: zzz. Al decirlo, tu garganta sí vibra. Pon los dedos en tu garganta y compruébalo. Alarga solo el sonido (sss o zzz), porque las vocales siempre vibran y no sirven para la prueba.",
        "Hay pares de palabras que solo cambian por /s/ y /z/: sip (sorbo) y zip (cierre), Sue y zoo, bus y buzz, ice y eyes. Si no distingues el sonido, puedes entender otra palabra. Por ejemplo, zoo es el lugar con animales y Sue es un nombre de niña.",
        "En español, la letra z se dice como /s/, pero en inglés zoo y zebra empiezan con /z/, con la garganta vibrando. Además, la letra s al final también puede sonar /z/ en palabras como is, his y dogs. Y en school, no pongas una «e» antes: se dice sss-cool, sin «es-».",
    ],
    vocab=[("zoo", "zoológico"), ("zebra", "cebra"), ("zip", "cierre, cremallera"), ("buzz", "zumbido"), ("sun", "sol"), ("bus", "bus")],
    worked=[
        {"title": "Contar sonidos /z/", "problem": ADULT + "«sit, zip, sun, zoo» ¿Cuántas palabras empiezan con el sonido /z/?", "steps": ["Sit y sun empiezan con /s/.", "Zip y zoo empiezan con /z/.", "Cuento las dos."], "answer": "2 palabras (zip y zoo)"},
        {"title": "Elegir entre /s/ y /z/", "problem": ADULT + "«bus» y «buzz»: ¿cuál termina con la garganta vibrando?", "steps": ["Bus termina con /s/, sin vibrar.", "Buzz termina con /z/, vibrando como una abeja."], "answer": "buzz"},
    ],
    mistakes=[
        {"wrong": "Decir zoo como «su» o zebra como «sebra», con /s/.", "why": "En español la z suena como s, y se aplica al inglés.", "fix": "Pon los dedos en la garganta: en zoo y zebra debe vibrar, como una abeja."},
        {"wrong": "Decir «eschool» para school.", "why": "En español las palabras no empiezan con s y otra consonante, y se agrega una e al inicio.", "fix": "Empieza con sss y sigue con -cool, sin la e inicial."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«sun» y «zoo». ¿Cuál empieza con /z/?", "zoo", "Zoo empieza con el sonido de la abeja."),
            ex("¿En qué sonido vibra la garganta: /s/ o /z/?", "/z/", "/z/ es el sonido de la abeja y vibra."),
            ex("¿Cuál de estas palabras empieza con /s/: sit o zip?", "sit", "Sit empieza con /s/; zip, con /z/."),
        ],
        "understand": [
            ex("¿Cómo se comparan los sonidos /s/ y /z/ con animales?", "/s/ es como una serpiente y /z/ como una abeja", "Una serpiente hace sss y una abeja hace zzz."),
            ex("¿Por qué sip y zip son una pareja de palabras que conviene practicar?", "Porque cambian solo por el sonido /s/ o /z/", "Un solo sonido cambia el significado."),
            ex("¿Dónde pones los dedos para sentir la diferencia?", "En la garganta", "En /z/ sientes vibración y en /s/ no."),
        ],
        "apply": [
            ex(ADULT + "«sit, zip, zoo, sun» ¿Cuántas palabras tienen /z/ al inicio?", "2", "Zip y zoo empiezan con /z/."),
            ex("Elige la palabra que empieza con /z/: sun, six, zebra.", "zebra", "Zebra es cebra y empieza con /z/."),
            ex("¿Qué palabra termina con /z/: ice o eyes?", "eyes", "Eyes termina como una abeja; ice termina con /s/."),
        ],
        "reason": [
            ex("Un niño oyó «Sue» pero escribió zoo. ¿Qué sonido no distinguió?", "El sonido inicial: /s/ en Sue y /z/ en zoo", "Sue empieza con /s/ y zoo con /z/."),
            ex("¿Por qué en school no se dice una «e» antes de la s?", "Porque en inglés la palabra empieza directamente con el sonido sss", "Agregar e cambia la palabra."),
        ],
        "challenge": [
            ex(ADULT + "«bus, buzz, bus, buzz, bus» ¿Cuántas veces oyes la palabra con /z/?", "2", "Buzz aparece dos veces."),
            ex("Clasifica estas palabras según el sonido final: bus, is, ice, eyes. ¿Cuáles terminan en /s/ y cuáles en /z/?", "/s/: bus, ice; /z/: is, eyes", "Is y eyes terminan con vibración."),
        ],
    },
    context=[ex("En el zoológico, una guía dice: " + ADULT + "«Look at the zebra! It's by the zoo shop.» ¿Qué palabras tienen el sonido /z/ al inicio?", "zebra y zoo", "Las dos empiezan con la letra z, que en inglés suena como abeja.")],
    selfcheck=[
        ex("¿Qué animal te ayuda a recordar el sonido /z/?", "Una abeja", "La abeja hace zzz y la garganta vibra."),
        ex("¿Qué palabra empieza con /z/: zoo o sun?", "zoo", "Zoo empieza con /z/."),
        ex("¿Qué es un «bus» y con qué sonido termina?", "Un bus; con /s/", "Bus termina con el sonido sss."),
    ],
    open_task=task("Con la mano en tu garganta, di cada palabra en voz alta alargando el sonido del inicio (o del final en bus y buzz) y siente si vibra: sun, zoo, sip, zip, bus, buzz. Anota con ✔ las que tienen /z/. Luego léele al adulto estas parejas y pídele que adivine cuál palabra dijiste: sip/zip, Sue/zoo.", "Con /z/ (vibra): zoo, zip, buzz (al final). Con /s/ (no vibra): sun, sip, bus.", ["distingue las palabras con /z/", "marca las palabras en una lista", "dice cada pareja sin confundirlas"], ["lista marcada", "nota del adulto"], ["decir zoo sin vibración", "agregar una e antes de school"], "Repasa con él las parejas más difíciles y haz que sienta la vibración con la mano en la garganta."),
    reinforce="Haz el sonido de la abeja (zzz) con los dedos en la garganta y el de la serpiente (sss) sin vibrar.",
    extend="Busca tres palabras con /z/ de esta clase (zoo, zebra, zip) y dibuja cada una.",
)

register(
    OA3, 5,
    materials="Las listas de palabras escritas en cada ejercicio, que lee un adulto; lápiz y un espejo pequeño si tienes.",
    use="Aprenderé a distinguir los sonidos /w/ y /th/ del inglés. Sirve para decir y entender mejor palabras como we, window, three y thank you.",
    prior=["Conozco palabras como we, one y three.", "Sé que algunas palabras tienen sonidos nuevos."],
    explain=[
        "El sonido /w/ se hace con los labios redondeados, como para decir «u», y luego se pasa rápido a la vocal. Se oye en we, water, window, week y one. No se dice «gu»: no digas «guater», di water.",
        "El sonido /th/ se hace poniendo la punta de la lengua entre los dientes y soplando suave. Se oye en three, thank you, think, thing, this, that, mother y brother. En español no existe este sonido, así que se practica frente a un espejo.",
        "Hay palabras que cambian solo por /w/ y /th/: wing y thing (ala y cosa), wink y think (guiñar y pensar). También conviene no confundir /th/ con /t/: three (tres) no es lo mismo que tree (árbol).",
    ],
    vocab=[("window", "ventana"), ("water", "agua"), ("three", "tres"), ("thank you", "gracias"), ("think", "pensar"), ("tree", "árbol")],
    worked=[
        {"title": "Reconocer /w/", "problem": ADULT + "«we, three, window, thank» ¿Cuántas palabras empiezan con /w/?", "steps": ["We empieza con /w/.", "Window empieza con /w/.", "Three y thank empiezan con /th/."], "answer": "2 palabras (we y window)"},
        {"title": "Diferenciar tree y three", "problem": ADULT + "«tree» y «three». ¿Cuál es el número 3?", "steps": ["Three empieza con /th/, con la lengua entre los dientes.", "Tree empieza con /t/ y es un árbol."], "answer": "three"},
    ],
    mistakes=[
        {"wrong": "Decir «guater» para water.", "why": "En español se suele agregar una g antes de la u.", "fix": "Redondea los labios como para u y pasa de inmediato a la vocal, sin g."},
        {"wrong": "Decir «tree» cuando quieres decir el número tres.", "why": "No se usa la lengua entre los dientes para el sonido /th/.", "fix": "Pon la lengua entre los dientes y sopla suave: three."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«we» y «three». ¿Cuál empieza con /th/?", "three", "Three empieza con la lengua entre los dientes."),
            ex(ADULT + "«water» y «thank». ¿Cuál empieza con /w/?", "water", "Water empieza con los labios redondeados."),
            ex("¿Qué significa «thank you»?", "gracias", "Thank you empieza con /th/."),
        ],
        "understand": [
            ex("¿Cómo haces el sonido /th/?", "Con la punta de la lengua entre los dientes, soplando suave", "Es un sonido que no existe en español."),
            ex("¿Cómo haces el sonido /w/?", "Con los labios redondeados, como para decir u", "Después pasas rápido a la vocal."),
            ex("¿Cuál es la diferencia entre tree y three?", "Tree es árbol, con /t/; three es tres, con /th/", "Un solo sonido cambia el significado."),
        ],
        "apply": [
            ex("Elige la palabra que empieza con /th/: window, three, week.", "three", "Three tiene /th/; window y week tienen /w/."),
            ex("Elige la palabra que empieza con /w/: water, think, this.", "water", "Water empieza con /w/; think y this, con /th/."),
            ex(ADULT + "«we, window, week, three» ¿Cuántas empiezan con /w/?", "3", "We, window y week empiezan con /w/."),
        ],
        "reason": [
            ex("Un niño dice «guindow» para window. ¿Qué error comete y cómo se corrige?", "Agrega una g; debe redondear los labios y decir window sin g", "El sonido /w/ no lleva g."),
            ex("¿Por qué conviene practicar delante de un espejo el sonido /th/?", "Porque así ves la lengua entre los dientes", "El espejo permite comprobar la posición."),
        ],
        "challenge": [
            ex("Clasifica estas palabras: wing, thing, wink, think. ¿Cuáles empiezan con /w/ y cuáles con /th/?", "/w/: wing, wink; /th/: thing, think", "Wing y wink empiezan con labios redondeados."),
            ex(ADULT + "«three trees» ¿Qué palabra tiene /th/ y cuál tiene /t/?", "three tiene /th/; trees tiene /t/", "Three y trees comienzan con sonidos distintos."),
        ],
    },
    context=[ex("En clase de inglés, la profesora lee: " + ADULT + "«Thank you! We have three windows.» ¿Qué palabras empiezan con /th/ y cuáles con /w/?", "Con /th/: thank, three. Con /w/: we, windows", "Thank y three tienen /th/; we y windows tienen /w/.")],
    selfcheck=[
        ex("¿Qué parte de la boca usas para /th/?", "La lengua entre los dientes", "Es la forma del sonido /th/."),
        ex("¿Cómo se dice «agua» en inglés?", "water", "Water empieza con /w/."),
        ex("¿Qué número es three?", "3", "Three es tres."),
    ],
    open_task=task("Frente a un espejo, di cada palabra: we, window, water, three, thank you, think. En una hoja haz dos columnas: /w/ y /th/ y escribe cada palabra en la columna correcta. Luego dile al adulto estas parejas y pide que adivine la palabra: wing/thing, wink/think, tree/three.", "/w/: we, window, water. /th/: three, thank you, think.", ["clasifica las seis palabras", "ve su lengua entre los dientes en /th/", "dice las parejas sin agregar g"], ["hoja con las dos columnas", "nota del adulto"], ["agregar g antes de w", "decir tree en lugar de three"], "Haz que repita despacio las palabras con /th/ viendo el espejo."),
    reinforce="Practica «thank you» tres veces con la lengua entre los dientes.",
    extend="Dibuja tres cosas que empiecen con /w/ y rotula cada una: window, water, week.",
)

# ---------------------------------------------------------------- OA 04
register(
    OA4, 1,
    materials="Los títulos y textos orales escritos en cada ejercicio, que lee un adulto; lápiz.",
    use="Aprenderé a hacer predicciones antes de escuchar y a revisarlas después. Sirve para preparar mi mente y entender mejor un texto en inglés.",
    prior=["Sé que un título da pistas.", "Conozco palabras como egg, bunny y chocolate."],
    explain=[
        "Predecir (predict) es pensar qué va a pasar o de qué va a tratar un texto antes de escucharlo. Para hacerlo, usa un título, una imagen o una palabra. Por ejemplo, si el título es Happy Easter, puedes predecir que se hablará de huevos de Pascua, de un conejo (bunny) o de chocolate.",
        "Una predicción no es una respuesta segura. Es una idea que debes comprobar. Después de escuchar, pregúntate: ¿mi predicción era correcta? Si lo era, aprendiste que tus pistas funcionan. Si no lo era, cambia tu idea con lo que oíste.",
        "Cuida las predicciones: no inventes detalles que no puedes comprobar. Una predicción cuidadosa usa pistas reales, como el título y las imágenes, y se revisa con lo que dice el texto.",
    ],
    vocab=[("predict", "predecir, adivinar con pistas"), ("title", "título"), ("Easter egg", "huevo de Pascua"), ("bunny", "conejito"), ("check", "comprobar"), ("clue", "pista")],
    worked=[
        {"title": "Predecir con el título", "problem": "El título es «At the zoo». ¿Qué animales podrías predecir: lion, monkey o fridge?", "steps": ["Zoo es un lugar con animales.", "Lion y monkey son animales de zoológico.", "Fridge es un refrigerador, no un animal."], "answer": "lion y monkey"},
        {"title": "Comprobar la predicción", "problem": ADULT + "«Tom is at the zoo. He sees a lion and a monkey.» Predije lion y monkey. ¿Estaba bien?", "steps": ["Escucho lion.", "Escucho monkey.", "Mis dos predicciones coinciden con el texto."], "answer": "Sí, mi predicción fue correcta"},
    ],
    mistakes=[
        {"wrong": "Creer que la predicción siempre es correcta y no revisarla.", "why": "Se confunde predecir con saber.", "fix": "Después de escuchar, compara tu idea con lo que dice el texto y corrígela si es necesario."},
        {"wrong": "Predecir algo que no tiene relación con el título.", "why": "No se usa la pista del título.", "fix": "Elige solo ideas que se relacionen con las palabras o imágenes del título."},
    ],
    tiers={
        "recovery": [
            ex("El título es «Happy Easter». ¿Qué predices: eggs o snow?", "eggs", "Easter se asocia con huevos de Pascua."),
            ex("¿Qué significa «predict»?", "Predecir o adivinar con pistas", "Se piensa qué dirá el texto antes de escuchar."),
            ex("El título es «My cat». ¿Qué animal esperas: cat o fish?", "cat", "El título nombra al gato."),
        ],
        "understand": [
            ex("¿Para qué sirve hacer una predicción antes de escuchar?", "Para preparar mi mente y buscar palabras clave", "Predecir ayuda a escuchar con propósito."),
            ex("¿Qué haces después de escuchar con tu predicción?", "La compruebo con lo que oí", "Una predicción se puede confirmar o cambiar."),
            ex("¿Qué pista usas para predecir?", "El título o una imagen", "Son pistas que se ven antes de escuchar."),
        ],
        "apply": [
            ex("El título es «At the park». ¿Qué objetos esperas: ball y tree o bed y fridge?", "ball y tree", "En un parque hay árboles y se juega con una pelota."),
            ex(ADULT + "«Look! A bunny has an Easter egg.» Predije bunny y egg. ¿Qué dos palabras confirma el texto?", "bunny y egg", "Las dos palabras aparecen en el texto."),
            ex("Una imagen muestra un niño con un paraguas. ¿Qué predices: rain o sun?", "rain", "Un paraguas se usa cuando llueve."),
        ],
        "reason": [
            ex("Predije «a lion» para el texto «At the zoo», pero el texto dijo «A monkey is at the zoo». ¿Qué hago?", "Cambio mi predicción: era un mono", "La predicción se corrige con lo que dice el texto."),
            ex("Una niña dice que el título «My school» habla de un gato volador. ¿Es una buena predicción?", "No, porque no hay una pista que la apoye", "Las predicciones deben basarse en pistas reales."),
        ],
        "challenge": [
            ex("Escribe dos predicciones cuidadosas para el título «My house»: elige entre kitchen, bed, lion, window.", "kitchen y bed (o window)", "Son partes y objetos de una casa; lion no se relaciona."),
            ex(ADULT + "«A girl has two Easter eggs. She is happy.» El título era «A happy Easter» y predije eggs y happy. ¿Se cumplió mi predicción?", "Sí; el texto dice Easter eggs y happy", "Las dos pistas están en el texto."),
        ],
    },
    context=[ex("Antes de un cuento, la profesora muestra la imagen de un conejo con una canasta y dice «Happy Easter». ¿Qué predices que dirá el cuento?", "Que habla de huevos de Pascua y un conejo", "Bunny y basket se relacionan con Easter.")],
    selfcheck=[
        ex("¿Cómo se dice «predecir» en inglés?", "predict", "Predict es predecir."),
        ex("¿Qué haces después de predecir y escuchar?", "Compruebo si acerté", "Se compara la predicción con el texto."),
        ex("¿Qué es un «title»?", "Un título", "El title da pistas del texto."),
    ],
    open_task=task("El título de un texto es «At the zoo». Antes de escuchar, escribe o dibuja tres predicciones (por ejemplo lion, monkey, zebra o giraffe). Luego un adulto lee: «Ana is at the zoo. She sees a lion. She sees a monkey. She is happy.» Marca con ✔ las predicciones que el texto confirma y con ✘ las que no.", "Predicciones: lion, monkey, zebra. ✔ lion, ✔ monkey, ✘ zebra.", ["escribe tres predicciones relacionadas con el título", "marca cuáles se confirman", "corrige la que no coincide"], ["lista de predicciones marcada", "nota del adulto"], ["no revisar las predicciones", "marcar ✔ en todas sin escuchar"], "Revisa con él las predicciones y celebra que corrigió una cuando el texto no la confirmó."),
    reinforce="Mira el título «My pet» y predice dos animales posibles. Luego pregunta a un adulto cuál es su mascota.",
    extend="Escribe un título y dos predicciones para un cuento sobre Easter.",
)

register(
    OA4, 2,
    materials="Los textos orales y las situaciones escritas en cada ejercicio, que lee un adulto; lápiz.",
    use="Aprenderé a conectar lo que escucho con lo que ya sé. Sirve para entender mejor un texto en inglés usando mi experiencia y lo que he aprendido en la escuela.",
    prior=["Sé qué hago en el recreo y en mi casa.", "Conozco palabras de animales y de alimentos."],
    explain=[
        "Conectar (connect) es relacionar lo que oyes con lo que ya sabes. Si escuchas «A monkey climbs the tree» y sabes que los monos son buenos para trepar, entiendes mejor el texto. Tus conocimientos previos son tu ayuda.",
        "Tus conocimientos pueden venir de tu casa, de tu escuela o de otras asignaturas. Si sabes que un triángulo tiene tres lados, entiendes «Draw a triangle». Si sabes que un cocinero prepara comida, entiendes «The cook is making a cake».",
        "Una buena conexión usa un dato seguro. Para conectar, pregúntate: ¿qué sé yo de esto? ¿Me ayuda a entender lo que oigo? Si la idea no ayuda, no la uses. Conecta solo con ideas que realmente relacionen.",
    ],
    vocab=[("connect", "conectar, relacionar"), ("know", "saber, conocer"), ("climb", "trepar"), ("cook", "cocinero"), ("cake", "torta"), ("triangle", "triángulo")],
    worked=[
        {"title": "Conectar con lo que sé", "problem": ADULT + "«The cook is making a cake.» ¿Qué sabes de un cocinero que te ayuda a entender?", "steps": ["Sé que un cocinero prepara comida.", "Make significa hacer.", "Cake es torta."], "answer": "Un cocinero prepara comida, así que prepara una torta"},
        {"title": "Usar otra asignatura", "problem": ADULT + "«Draw a triangle.» ¿Qué sabes de matemática que te ayuda?", "steps": ["Sé que un triángulo tiene tres lados.", "Dibujo una figura con tres lados."], "answer": "Dibujo una figura de tres lados"},
    ],
    mistakes=[
        {"wrong": "Conectar con una idea que no tiene relación con el texto.", "why": "Se usa un conocimiento que no ayuda a entender.", "fix": "Pregúntate si lo que sabes ayuda a entender lo que oyes; si no, no la uses."},
        {"wrong": "Pensar que lo que ya sé reemplaza lo que dice el texto.", "why": "Se olvida comprobar con las palabras que se oyen.", "fix": "Usa lo que sabes como ayuda y comprueba con las palabras clave."},
    ],
    tiers={
        "recovery": [
            ex("Sabes que un león es un animal salvaje. ¿Qué entiendes de «A lion is in the zoo»?", "Que hay un león en el zoológico", "Lion y zoo son palabras conocidas."),
            ex("¿Qué significa «connect»?", "Conectar o relacionar", "Se relaciona lo que oyes con lo que sabes."),
            ex("¿Qué sabes de un cocinero (cook)?", "Que prepara comida", "Ese dato ayuda a entender frases sobre cocina."),
        ],
        "understand": [
            ex("¿Para qué sirve conectar lo que escuchas con lo que sabes?", "Para entender mejor el texto", "Los conocimientos previos ayudan a comprender."),
            ex("¿De dónde pueden venir tus conocimientos previos?", "De mi casa, de mi escuela o de otras asignaturas", "Todas esas experiencias son útiles."),
            ex("¿Qué debes hacer si una idea no ayuda a entender el texto?", "No usarla", "Una conexión debe aportar al significado."),
        ],
        "apply": [
            ex(ADULT + "«A monkey climbs the tree.» Sabes que un mono vive en árboles. ¿Qué entiendes de climbs?", "Que el mono sube por el árbol", "Climb significa trepar."),
            ex(ADULT + "«Draw a square.» ¿Qué sabes de matemática que te sirve?", "Que un cuadrado tiene cuatro lados iguales", "El dato matemático ayuda a dibujar la figura."),
            ex(ADULT + "«The nurse is at the hospital.» ¿Qué sabes de una enfermera?", "Que cuida a las personas enfermas", "Ese dato ayuda a entender el lugar y la ocupación."),
        ],
        "reason": [
            ex("El texto dice «The cook has bread». Un niño piensa en un auto. ¿Es una buena conexión?", "No; un cocinero se relaciona con comida, no con autos", "La conexión debe relacionarse con el texto."),
            ex("Una niña sabe que en Pascua se regalan huevos de chocolate. ¿Qué palabras puede predecir en «Happy Easter»?", "Egg y chocolate", "Su conocimiento previo se conecta con Easter."),
        ],
        "challenge": [
            ex(ADULT + "«It is Easter. The bunny has a basket. The basket has eggs.» Escribe dos conocimientos previos que te ayudan.", "Sé que en Pascua se regalan huevos de chocolate y que el conejo es un símbolo de Pascua", "Esas ideas ayudan a entender el texto."),
            ex(ADULT + "«A farmer has a cow and a horse.» Un niño dice: «Un granjero cuida animales». ¿Ayuda esa conexión?", "Sí, porque farmer es granjero y cow y horse son animales", "El conocimiento coincide con las palabras del texto."),
        ],
    },
    context=[ex("Escuchas en inglés: " + ADULT + "«The cook is making rice.» ¿Qué conocimiento tuyo te ayuda a entender?", "Que un cocinero prepara comida, como el arroz que se come en muchas casas", "Rice es arroz y cook es cocinero.")],
    selfcheck=[
        ex("¿Qué es un conocimiento previo?", "Algo que ya sé antes de escuchar", "Previo significa antes."),
        ex(ADULT + "«A bird can fly.» ¿Qué sabes de los pájaros que te ayuda?", "Que vuelan", "Fly es volar."),
        ex("¿Cómo se dice «torta» en inglés?", "cake", "Cake es torta."),
    ],
    open_task=task("Un adulto lee dos veces: «Mia is at the market. She has five apples and three eggs. She is happy.» Antes de escuchar, escribe dos cosas que sabes sobre un mercado (por ejemplo, que se compra comida). Después escucha y marca cuáles de esas ideas te ayudaron.", "Sé que en un mercado se compra fruta. Sé que se compran huevos.", ["escribe dos conocimientos previos", "marca cuáles ayudan", "usa palabras del texto (apples, eggs)"], ["lista de conocimientos previos", "nota del adulto"], ["escribir ideas sin relación con el texto", "olvidar comprobar con lo que oyó"], "Pregúntale qué idea de su casa o de otra asignatura le ayudó más y por qué."),
    reinforce="Cuenta a un adulto qué sabes de los monos y escucha: «A monkey can climb».",
    extend="Elige un animal salvaje y escribe una cosa que sabes de él. Luego busca esa idea en una frase en inglés, por ejemplo «A giraffe has a long neck».",
)

register(
    OA4, 3,
    materials="Las descripciones de imágenes y los textos orales escritos en cada ejercicio, que lee un adulto; lápiz y papel para dibujar.",
    use="Aprenderé a relacionar lo que oigo con una imagen. Sirve para entender un texto en inglés usando lo que veo, aunque no conozca todas las palabras.",
    prior=["Sé que una imagen cuenta cosas.", "Conozco palabras como girl, boy, tree y book."],
    explain=[
        "Una imagen es una ayuda para entender un texto oral. Si ves un dibujo de una niña bajo un árbol y oyes «The girl is under the tree», la imagen y las palabras coinciden. Así sabes que entendiste.",
        "Para relacionar imagen y texto, haz dos pasos. Primero mira la imagen y nombra lo que ves: persona, animal, objeto, lugar. Después escucha y busca las mismas palabras. Si una palabra del texto no está en la imagen, o al revés, revisa de nuevo.",
        "A veces dos imágenes se parecen. Fíjate en los detalles: el color, la cantidad, el lugar. «The cat is under the table» es distinto de «The cat is on the table». La imagen correcta es la que coincide con todas las palabras clave.",
    ],
    vocab=[("picture", "imagen, dibujo"), ("under the tree", "debajo del árbol"), ("on the table", "sobre la mesa"), ("same", "igual"), ("different", "distinto"), ("detail", "detalle")],
    worked=[
        {"title": "Elegir la imagen", "problem": "Imagen A: un gato sobre una mesa. Imagen B: un gato debajo de una mesa. " + ADULT + "«The cat is under the table.» ¿Cuál imagen coincide?", "steps": ["Escucho under, que significa debajo.", "En la imagen B el gato está debajo de la mesa."], "answer": "La imagen B"},
        {"title": "Detalle de color", "problem": "Imagen A: una pelota roja. Imagen B: una pelota azul. " + ADULT + "«I have a blue ball.» ¿Cuál imagen coincide?", "steps": ["Escucho blue, que significa azul.", "La imagen B muestra una pelota azul."], "answer": "La imagen B"},
    ],
    mistakes=[
        {"wrong": "Elegir la imagen solo por un objeto, sin revisar el lugar o el color.", "why": "Se mira un solo detalle.", "fix": "Revisa objeto, color, cantidad y lugar antes de elegir."},
        {"wrong": "Decidir antes de escuchar el texto completo.", "why": "Se elige con la primera palabra.", "fix": "Escucha la frase entera y compara cada palabra clave con la imagen."},
    ],
    tiers={
        "recovery": [
            ex("Imagen: un perro grande. " + ADULT + "«I see a big dog.» ¿Coinciden imagen y texto?", "Sí", "Big dog significa perro grande."),
            ex("Imagen: dos peces. " + ADULT + "«I have one fish.» ¿Coinciden imagen y texto?", "No", "One es uno y la imagen muestra dos."),
            ex("¿Qué significa «picture»?", "Imagen o dibujo", "Una picture ayuda a entender."),
        ],
        "understand": [
            ex("¿Qué haces primero para relacionar una imagen con un texto oral?", "Miro la imagen y nombro lo que veo", "Así sabes qué palabras buscar."),
            ex("¿Por qué conviene escuchar toda la frase antes de elegir una imagen?", "Porque los detalles pueden cambiar la respuesta", "Under y on cambian el significado."),
            ex("¿Qué detalles revisas en una imagen?", "Objeto, color, cantidad y lugar", "Son los detalles que el texto puede nombrar."),
        ],
        "apply": [
            ex("Imagen A: una niña con un libro verde. Imagen B: una niña con un libro rojo. " + ADULT + "«She has a red book.» ¿Cuál imagen es?", "La imagen B", "Red significa rojo."),
            ex("Imagen A: tres manzanas. Imagen B: cinco manzanas. " + ADULT + "«I have five apples.» ¿Cuál imagen es?", "La imagen B", "Five es cinco."),
            ex("Imagen A: un mono en un árbol. Imagen B: un mono debajo de un árbol. " + ADULT + "«The monkey is in the tree.» ¿Cuál imagen es?", "La imagen A", "In the tree es en el árbol."),
        ],
        "reason": [
            ex("Imagen: un gato sobre una silla. Un niño oyó «The cat is under the chair» y dijo que sí coincide. ¿Se equivocó?", "Sí; la imagen muestra el gato sobre la silla y el texto dice debajo", "On y under son opuestos."),
            ex("Imagen A: una niña feliz. Imagen B: una niña triste. " + ADULT + "«She is sad.» ¿Qué imagen coincide y qué palabra lo muestra?", "La imagen B; sad", "Sad significa triste."),
        ],
        "challenge": [
            ex("Imagen: un cocinero con una torta en la cocina. " + ADULT + "«The cook is in the kitchen. He has a cake.» ¿Qué tres cosas coinciden entre imagen y texto?", "el cocinero, la cocina y la torta", "Cook, kitchen y cake."),
            ex("Dibuja en tu cuaderno: " + ADULT + "«A big tree. A bird is on the tree. A cat is under the tree.» ¿Qué animal dibujas debajo del árbol?", "Un gato", "Under the tree es debajo del árbol."),
        ],
    },
    context=[ex("En una tarjeta de Pascua ves un conejo y tres huevos de colores. " + ADULT + "«A bunny has three Easter eggs.» ¿Qué dos detalles coinciden con la imagen?", "El conejo y los tres huevos", "Bunny y three Easter eggs están en la tarjeta.")],
    selfcheck=[
        ex("¿Qué significa «different»?", "distinto", "Different es lo opuesto de same."),
        ex("Imagen: un círculo rojo. " + ADULT + "«A red circle.» ¿Coinciden?", "Sí", "Red circle es círculo rojo."),
        ex("¿Qué detalles revisas al comparar texto e imagen?", "Color, cantidad, objeto y lugar", "Son detalles clave."),
    ],
    open_task=task("Un adulto lee dos veces: «A girl is under a big tree. She has a green book. A bird is on the tree.» Dibuja la escena y rotula en inglés: girl, tree, book, bird. Marca con un círculo el detalle de color (green) y los dos detalles de lugar (under y on).", "Dibujo con una niña bajo un árbol con libro verde y un pájaro sobre el árbol.", ["dibuja los cuatro elementos", "pone el libro verde y lo marca", "ubica a la niña bajo el árbol y al pájaro sobre el árbol"], ["dibujo rotulado", "nota del adulto"], ["poner al pájaro debajo del árbol", "no usar el color verde"], "Compara el dibujo con las palabras clave del texto y corrige juntos los detalles que cambiaron."),
    reinforce="Pide a un adulto que diga «a blue book» y dibuja un libro azul.",
    extend="Dibuja dos escenas casi iguales, una con un gato sobre la mesa y otra con un gato debajo, y escribe una frase en inglés para cada una.",
)

register(
    OA4, 4,
    materials="Los textos orales escritos en cada ejercicio, que lee un adulto dos veces; lápiz.",
    use="Aprenderé a fijarme en las palabras clave y a escuchar otra vez para comprobar. Sirve para entender lo más importante de un texto en inglés sin perderme en las palabras que no conozco.",
    prior=["Sé hacer predicciones y usar imágenes.", "Conozco palabras de la escuela, de animales y de comida."],
    explain=[
        "Las palabras clave (key words) son las que llevan el mensaje más importante: personas, animales, objetos, números, lugares y acciones. En «Tom has five red apples», las palabras clave son Tom, five, red y apples. Las demás palabras ayudan, pero no son necesarias para entender lo esencial.",
        "Para enfocar tu atención, escucha primero buscando una o dos palabras clave. Si no las encuentras, pide escuchar otra vez. En la segunda escucha, busca otras pistas: números, colores, lugares y acciones.",
        "Al final, comprueba (check). Pregúntate: ¿mi respuesta usa palabras que sí oí? ¿Coincide con el texto? Si dudas, escucha de nuevo. Escuchar otra vez es una estrategia de personas que aprenden bien.",
    ],
    vocab=[("key word", "palabra clave"), ("listen again", "escuchar otra vez"), ("check", "comprobar"), ("number", "número"), ("color", "color"), ("place", "lugar")],
    worked=[
        {"title": "Encontrar palabras clave", "problem": ADULT + "«Tom has five red apples.» ¿Cuáles son las palabras clave?", "steps": ["Tom es la persona.", "Five es la cantidad y red es el color.", "Apples es el objeto."], "answer": "Tom, five, red, apples"},
        {"title": "Escuchar otra vez", "problem": ADULT + "«Ana is in the kitchen. She has a cake.» Primero oyes kitchen y pierdes el resto. Escuchas otra vez. ¿Qué descubres?", "steps": ["En la segunda escucha oigo cake.", "Cake es torta.", "Entonces Ana está en la cocina con una torta."], "answer": "Ana tiene una torta en la cocina"},
    ],
    mistakes=[
        {"wrong": "Intentar escribir todo lo que se dice.", "why": "Se pierde la atención en las palabras más importantes.", "fix": "Anota solo una o dos palabras clave en cada escucha."},
        {"wrong": "Responder sin comprobar con una segunda escucha.", "why": "Se confía en lo primero que se entendió.", "fix": "Pide escuchar otra vez y revisa tu respuesta."},
    ],
    tiers={
        "recovery": [
            ex(ADULT + "«I have two cats.» ¿Cuál es la palabra clave de número?", "two", "Two es dos."),
            ex(ADULT + "«The giraffe is in the zoo.» ¿Cuál es la palabra clave de animal?", "giraffe", "Giraffe es jirafa."),
            ex("¿Qué significa «key word»?", "Palabra clave", "Es una palabra importante para entender."),
        ],
        "understand": [
            ex("¿Qué tipo de palabras suelen ser clave?", "Personas, animales, objetos, números, lugares y acciones", "Llevan el significado principal."),
            ex("¿Para qué sirve escuchar otra vez?", "Para encontrar más palabras clave y comprobar mi respuesta", "La segunda escucha confirma lo que entendí."),
            ex("¿Qué haces al terminar de responder?", "Compruebo mi respuesta con lo que oí", "Check significa comprobar."),
        ],
        "apply": [
            ex(ADULT + "«Leo has six blue pencils.» ¿Cuántos lápices tiene Leo y de qué color?", "Seis, azules", "Six es seis y blue es azul."),
            ex(ADULT + "«The lion is under the big tree.» ¿Dónde está el león?", "Debajo del árbol grande", "Under the big tree."),
            ex(ADULT + "«Mum is cooking rice in the kitchen.» ¿Qué cocina mamá y dónde?", "Arroz, en la cocina", "Rice y kitchen son palabras clave."),
        ],
        "reason": [
            ex("Un niño respondió «Ana tiene cinco manzanas». Escuchó otra vez: «Ana has fifteen apples». ¿Qué error tuvo y cómo lo corrigió?", "Confundió five con fifteen; son quince manzanas", "La segunda escucha permitió corregir."),
            ex("¿Por qué es mejor buscar palabras clave que traducir todo?", "Porque con las palabras clave entiendo lo esencial sin perder tiempo", "Traducir todo hace perder el hilo."),
        ],
        "challenge": [
            ex(ADULT + "«A farmer has seven cows. The cows are in the field. One cow is brown.» Escribe tres palabras clave y su significado.", "farmer: granjero; seven: siete; cows: vacas (también brown: café)", "Son personas, número y animal."),
            ex(ADULT + "«Mia has three brown bears. The bears are in the forest.» ¿Cuántos osos hay y de qué color son?", "Tres osos café", "Three es tres y brown es café."),
        ],
    },
    context=[ex("En la sala, la profesora dice una sola vez: " + ADULT + "«Look at the board. Draw a red circle.» Pides que lo repita. ¿Qué palabras clave debes escuchar la segunda vez?", "Board, draw, red y circle", "Son el lugar, la acción, el color y la figura.")],
    selfcheck=[
        ex("¿Cómo se dice «escuchar otra vez» en inglés?", "listen again", "Listen again significa escuchar otra vez."),
        ex(ADULT + "«I see eight birds.» ¿Cuál es la palabra clave de cantidad?", "eight", "Eight es ocho."),
        ex("¿Cuál es una palabra clave: apple o the?", "apple", "Apple es un objeto; the es una palabra pequeña de apoyo."),
    ],
    open_task=task("Un adulto lee dos veces: «Pablo is in the park. He has four red balls. A dog is next to him. The dog is happy.» Primero anota una palabra clave. Escucha de nuevo y anota otras tres. Con las cuatro palabras clave cuenta qué pasa: por ejemplo Pablo, four, balls, dog.", "Palabras clave: Pablo, park, four, balls, dog, happy.", ["anota cuatro palabras clave", "escucha de nuevo", "cuenta lo que pasa con sus palabras"], ["lista de palabras clave", "nota del adulto"], ["anotar frases completas", "no escuchar de nuevo"], "Compara su lista con el texto y celebra las palabras que encontró en la segunda escucha."),
    reinforce="Pide a un adulto que diga «I have five red balls» y repite solo las palabras clave.",
    extend="Escribe una frase en inglés con una persona, un número y un color, y subraya sus palabras clave.",
)
