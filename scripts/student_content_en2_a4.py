"""Student material for 2.º básico Inglés, EN02 OA 07 (leer textos sobre temas conocidos y funciones del lenguaje).

Todos los textos para leer están escritos completos en el enunciado, con su pista en español.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA7 = "EN02 OA 07"


register(
    OA7, 1,
    materials="Los carteles, listas y textos breves escritos en cada ejercicio; lápiz y papel.",
    use="Aprenderé a leer instrucciones de la escuela y presentaciones de personas, y a actuar o identificar a quién se presenta. Sirve para seguir lo que dicen los carteles y para conocer a otros.",
    prior=["Conozco verbos como open, close, stand up y sit down.", "Sé leer I'm ... y This is ..."],
    explain=[
        "Las instrucciones escritas empiezan con un verbo y dicen qué hacer: Open your book (abre tu libro). Close the door (cierra la puerta). Write your name (escribe tu nombre). Listen, please (escucha, por favor). Clap two times (aplaude dos veces). Muchas veces están en una lista numerada: 1, 2, 3. Se hacen en orden.",
        "En una presentación escrita, una persona dice quién es y puede presentar a otra. «Hello! I'm Pía. I'm seven. This is my friend, Leo. He is eight.» Aquí, Pía se presenta con I'm y presenta a Leo con This is. Para leer bien, busca quién habla y a quién presenta. También se puede presentar a la familia: This is my sister, Ana (esta es mi hermana) y This is my brother, Leo (este es mi hermano).",
        "Puedes mostrar que entendiste actuando o respondiendo. Si lees «Stand up», te pones de pie. Si lees «This is my friend, Leo», sabes que Leo es el amigo. Si dudas, vuelve a leer la frase completa.",
    ],
    vocab=[("write your name", "escribe tu nombre"), ("listen", "escuchar"), ("This is my friend.", "Este es mi amigo / Esta es mi amiga."), ("He is eight.", "Él tiene ocho años."), ("She is seven.", "Ella tiene siete años."), ("please", "por favor")],
    worked=[
        {"title": "Leer una instrucción", "problem": "Lee el cartel: «1. Stand up. 2. Write your name. 3. Sit down.» ¿Qué haces en el paso 2?", "steps": ["Busco el 2.", "Dice Write your name.", "Write es escribir."], "answer": "Escribo mi nombre"},
        {"title": "Leer una presentación", "problem": "Lee: «Hello! I'm Pía. This is my friend, Leo. He is eight.» ¿Quién tiene ocho años?", "steps": ["He is eight habla de un niño.", "Antes se presenta a Leo.", "Entonces Leo tiene ocho años."], "answer": "Leo"},
    ],
    mistakes=[
        {"wrong": "Hacer los pasos de la lista en otro orden.", "why": "No se leyeron los números.", "fix": "Sigue los números 1, 2, 3 en orden."},
        {"wrong": "Pensar que I'm Pía y This is Pía significan lo mismo.", "why": "I'm presenta a quien habla y This is presenta a otra persona.", "fix": "I'm es yo soy; This is es esta es."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «Open your book.» ¿Qué haces?", "Abro mi libro", "Open es abrir."),
            ex("Lee: «I'm Ana.» ¿Quién habla?", "Ana", "I'm Ana significa yo soy Ana."),
            ex("Lee: «This is my friend, Leo.» ¿Quién es Leo?", "El amigo", "This is my friend presenta a un amigo."),
        ],
        "understand": [
            ex("¿Con qué parte de la oración empieza una instrucción?", "Con un verbo", "Open, close y write son verbos."),
            ex("¿Qué diferencia hay entre I'm y This is?", "I'm presenta a quien habla; This is presenta a otra persona", "Sirven para presentar de dos maneras."),
            ex("¿Qué significa «please»?", "por favor", "Please hace la petición amable."),
        ],
        "apply": [
            ex("Lee el cartel: «1. Open your notebook. 2. Write your name. 3. Close your notebook.» ¿Qué haces al final?", "Cierro mi cuaderno", "El paso 3 dice Close your notebook."),
            ex("Lee: «Hello! I'm Mia. I'm seven. This is my friend, Tom. He is eight.» ¿Cuántos años tiene Tom?", "8", "Eight es ocho."),
            ex("Lee: «Stand up, please. Clap two times.» ¿Cuántas veces aplaudes?", "2", "Two times es dos veces."),
        ],
        "reason": [
            ex("Lee: «1. Sit down. 2. Stand up.» Un niño se pone de pie primero. ¿Qué error cometió?", "No siguió el orden: debía sentarse primero", "El número 1 dice sit down."),
            ex("Lee: «Hello! I'm Lía. This is my friend, Dani. She is seven.» ¿Quién tiene siete años: Lía o Dani?", "Dani", "She is seven habla de Dani, la amiga presentada."),
        ],
        "challenge": [
            ex("Lee: «Hello! I'm Sam. This is my sister, Ana. She is nine. This is my brother, Leo. He is ten.» ¿Cuántos años tiene cada hermano?", "Ana: nueve; Leo: diez", "Nine es nueve y ten es diez."),
            ex("Escribe una instrucción en inglés para pedir a un compañero que abra la puerta, con please.", "Open the door, please.", "Open the door, please es la frase."),
        ],
    },
    context=[ex("En la puerta de la sala hay un cartel: «Please close the door. Thank you!» ¿Qué debes hacer?", "Cerrar la puerta", "Close the door significa cerrar la puerta.")],
    selfcheck=[
        ex("¿Cómo se dice «cierra» en inglés?", "close", "Close es cerrar."),
        ex("Lee: «Write your name.» ¿Qué haces?", "Escribo mi nombre", "Write es escribir."),
        ex("Lee: «This is my friend, Pía.» ¿Qué significa?", "Esta es mi amiga Pía", "This is presenta a otra persona."),
    ],
    open_task=task("Lee este cartel de clase y hazlo: «1. Stand up. 2. Touch your nose. 3. Write your name on the paper. 4. Sit down.» Después lee esta presentación y dibuja a las dos personas: «Hello! I'm Noa. I'm seven. This is my friend, Dani. He is eight.» Escribe debajo de cada dibujo el nombre y la edad.", "Dibujo de Noa (7) y Dani (8) con sus nombres y edades.", ["hace los cuatro pasos en orden", "dibuja a Noa y a Dani", "escribe nombre y edad de cada una"], ["foto o nota del adulto", "dibujo rotulado"], ["cambiar el orden de los pasos", "confundir la edad de Noa con la de Dani"], "Revisa con él cada paso del cartel y la edad de cada persona."),
    reinforce="Lee en voz alta «Stand up, sit down» y hazlo.",
    extend="Escribe un cartel de tres pasos para la sala usando los verbos open, write y close.",
)

register(
    OA7, 2,
    materials="Los textos breves escritos en cada ejercicio; lápiz.",
    use="Aprenderé a leer textos que dicen lo que alguien puede hacer, cómo se siente y qué tiene. Sirve para entender notas, cartas y tarjetas, también las de Easter.",
    prior=["Conozco I can, I'm y I have.", "Conozco los números hasta veinte."],
    explain=[
        "Los textos sobre habilidad usan can o can't: «I can swim» (puedo nadar), «She can't fly» (ella no puede volar). Los textos sobre sentimientos usan I'm, He's o She's: «I'm happy», «He's tired», «She's scared». Los textos sobre posesión usan have o has: «I have two pencils», «She has a cat».",
        "Las cantidades llegan hasta veinte: eleven (11), twelve (12), thirteen (13), fourteen (14), fifteen (15), sixteen (16), seventeen (17), eighteen (18), nineteen (19), twenty (20). Para entender un texto, subraya el número y lo que se cuenta: «Ana has fifteen eggs» (Ana tiene quince huevos).",
        "Otras palabras que aparecen: bike (bicicleta), new (nuevo). En una tarjeta de Easter puedes leer: «Dear Mia, Happy Easter! I have twelve eggs. I am happy. From Leo.» En ese texto aparecen un saludo, una posesión y un sentimiento.",
    ],
    vocab=[("can / can't", "puede / no puede"), ("happy / sad / tired", "contento / triste / cansado"), ("have / has", "tengo, tienes / tiene"), ("fifteen", "quince"), ("twenty", "veinte"), ("Easter egg", "huevo de Pascua")],
    worked=[
        {"title": "Habilidad", "problem": "Lee: «Tom can run and jump. He can't swim.» ¿Qué no puede hacer Tom?", "steps": ["Busco can't.", "Después de can't dice swim."], "answer": "Nadar"},
        {"title": "Posesión y cantidad", "problem": "Lee: «Ana has fifteen Easter eggs.» ¿Cuántos huevos tiene Ana?", "steps": ["Busco el número.", "Fifteen es quince."], "answer": "15"},
    ],
    mistakes=[
        {"wrong": "Leer can't como can.", "why": "Se pasa por alto el «-n't».", "fix": "Fíjate en el final: can't niega, can afirma."},
        {"wrong": "Confundir fifteen con fifty.", "why": "Se pierde el final «-teen».", "fix": "Fifteen es quince; fifty es cincuenta y no se usa hasta veinte."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «I can draw.» ¿Qué puede hacer la persona?", "Dibujar", "Draw es dibujar."),
            ex("Lee: «She is happy.» ¿Cómo se siente ella?", "Contenta", "Happy es contento."),
            ex("Lee: «I have a cat.» ¿Qué tiene la persona?", "Un gato", "Cat es gato."),
        ],
        "understand": [
            ex("¿Qué diferencia hay entre can y can't?", "Can significa puede; can't significa no puede", "El final «-n't» indica negación."),
            ex("¿Qué palabras usas para hablar de lo que alguien tiene?", "have o has", "Have con yo y has con él o ella."),
            ex("¿Qué número es «eighteen»?", "18", "Eighteen es dieciocho."),
        ],
        "apply": [
            ex("Lee: «A monkey can climb. A fish can swim.» ¿Qué animal puede nadar?", "El pez", "A fish can swim."),
            ex("Lee: «Leo is sad. He is tired.» ¿Cómo se siente Leo?", "Triste y cansado", "Sad es triste y tired, cansado."),
            ex("Lee: «Mia has sixteen crayons.» ¿Cuántos lápices de cera tiene?", "16", "Sixteen es dieciséis."),
        ],
        "reason": [
            ex("Lee: «A lion can't fly.» Un niño dice que el león vuela. ¿Qué error tiene?", "Entendió can en lugar de can't; el león no puede volar", "Can't significa no puede."),
            ex("Lee: «Pablo has nine stickers. Lía has twelve stickers.» ¿Quién tiene más y cuántos más?", "Lía, tiene 3 más", "Doce menos nueve es tres."),
        ],
        "challenge": [
            ex("Lee la tarjeta: «Dear Mia, Happy Easter! I have twelve Easter eggs. I am happy. From Leo.» ¿Cuántos huevos tiene Leo y cómo se siente?", "12 huevos; contento", "Twelve y happy."),
            ex("Lee: «I have ten pencils and nine pens.» ¿Cuántos son en total?", "19", "Diez más nueve es diecinueve."),
        ],
    },
    context=[ex("En una carta de tu primo lees: «I am Dani. I can swim. I am happy because I have a new bike.» ¿Qué sabe hacer Dani?", "Nadar", "I can swim significa puedo nadar.")],
    selfcheck=[
        ex("¿Cómo se dice «triste» en inglés?", "sad", "Sad es triste."),
        ex("Lee: «She has twenty eggs.» ¿Cuántos huevos tiene?", "20", "Twenty es veinte."),
        ex("¿Qué significa «I can't swim»?", "No puedo nadar", "Can't es no puedo."),
    ],
    open_task=task("Lee esta tarjeta: «Dear Pía, Happy Easter! I have fourteen Easter eggs. I can run and jump. I am happy. From Tom.» Responde por escrito: (1) How many eggs? (2) What can Tom do? (3) How does Tom feel? Después escribe tu propia tarjeta de tres frases con I have, I can y I am.", "(1) 14. (2) run and jump. (3) happy.", ["responde las tres preguntas", "escribe tres frases propias", "usa have, can y am"], ["respuestas escritas", "tarjeta propia"], ["decir catorce como cuarenta", "olvidar la habilidad can"], "Revisa juntos cada respuesta con el texto y celebra la tarjeta propia."),
    reinforce="Lee en voz alta «I can run. I am happy.» y haz la acción.",
    extend="Escribe una nota de cuatro frases a un amigo: dos con I can, una con I am y una con I have.",
)

register(
    OA7, 3,
    materials="Los textos breves escritos en cada ejercicio; lápiz y papel para dibujar.",
    use="Aprenderé a leer descripciones de animales y objetos en un lugar, con figuras geométricas, partes de la casa y muebles. Sirve para entender dónde está algo y cómo es.",
    prior=["Conozco animales salvajes como lion, zebra y giraffe.", "Conozco in, on, under y next to."],
    explain=[
        "Un texto puede describir cómo es un animal o un objeto y dónde está. Para el cómo, usa palabras como big (grande), small (pequeño), tall (alto), long (largo), black (negro) y gray (gris): «The elephant is big and gray». Para el dónde, usa in, on, under o next to: «The cat is under the table».",
        "También hay palabras de figuras geométricas: circle, square, triangle y rectangle. «The window is a square» (la ventana es un cuadrado). «The table is a rectangle» (la mesa es un rectángulo). Y hay partes de la casa y muebles: kitchen, bedroom, bathroom, bed, table, chair, desk (escritorio) y sofa. Otros objetos: door (puerta), clock (reloj).",
        "Lee con calma: primero busca el nombre del animal o del objeto; luego, cómo es; y al final, dónde está. Si dibujas lo que lees, puedes comprobar que entendiste.",
    ],
    vocab=[("tall", "alto"), ("long", "largo"), ("gray", "gris"), ("rectangle", "rectángulo"), ("next to", "al lado de"), ("sofa", "sillón")],
    worked=[
        {"title": "Animal y lugar", "problem": "Lee: «The giraffe is tall. It is next to a tree.» ¿Cómo es la jirafa y dónde está?", "steps": ["Busco cómo es: tall.", "Busco dónde: next to a tree."], "answer": "Alta; al lado de un árbol"},
        {"title": "Objeto y figura", "problem": "Lee: «The window is a square. The table is a rectangle.» ¿Qué figura tiene la mesa?", "steps": ["Busco table.", "Dice a rectangle."], "answer": "Un rectángulo"},
    ],
    mistakes=[
        {"wrong": "Confundir in con on.", "why": "Se parecen en la escritura, pero in es dentro y on es sobre.", "fix": "Piensa en una caja: in the box es dentro; on the box es encima."},
        {"wrong": "Leer solo el animal y no el lugar.", "why": "Se pierde la segunda parte de la frase.", "fix": "Lee la frase completa: qué animal, cómo es y dónde está."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «The cat is on the bed.» ¿Dónde está el gato?", "Sobre la cama", "On the bed es sobre la cama."),
            ex("Lee: «The elephant is big.» ¿Cómo es el elefante?", "Grande", "Big es grande."),
            ex("¿Qué es un «triangle»?", "Un triángulo", "Triangle es triángulo."),
        ],
        "understand": [
            ex("¿Qué dos cosas buscas al leer una descripción?", "Cómo es y dónde está", "La descripción da forma y lugar."),
            ex("¿Qué significa «tall»?", "alto", "Tall se usa para jirafas, árboles o personas."),
            ex("¿Qué diferencia hay entre in y on?", "In es dentro; on es sobre", "Son lugares distintos."),
        ],
        "apply": [
            ex("Lee: «A lion is under the tree.» ¿Dónde está el león?", "Debajo del árbol", "Under es debajo."),
            ex("Lee: «The sofa is in the living room.» ¿Dónde está el sofá?", "En la sala", "Living room es la sala."),
            ex("Lee: «The door is a rectangle. The clock is a circle.» ¿Qué figura tiene el reloj?", "Un círculo", "Circle es círculo."),
        ],
        "reason": [
            ex("Lee: «The monkey is in the tree.» Un niño dice que el mono está debajo del árbol. ¿Por qué se equivoca?", "In significa dentro o en; el mono está en el árbol", "Under sería debajo, pero el texto dice in."),
            ex("Lee: «The zebra is next to the giraffe.» ¿Están juntos o lejos?", "Juntos, uno al lado del otro", "Next to es al lado de."),
        ],
        "challenge": [
            ex("Lee: «My bedroom has a bed and a desk. The bed is next to the window. The window is a square.» Escribe qué hay en el cuarto, dónde está la cama y qué figura tiene la ventana.", "Una cama y un escritorio; la cama está al lado de la ventana; un cuadrado", "Bed, desk, next to y square."),
            ex("Lee: «A big gray elephant is at the zoo. A small monkey is on the elephant.» ¿Qué animal está encima del otro?", "El mono, sobre el elefante", "On the elephant es sobre el elefante."),
        ],
    },
    context=[ex("En un mapa de la casa lees: «The kitchen is next to the bathroom. The table is in the kitchen.» ¿Qué hay dentro de la cocina?", "Una mesa", "The table is in the kitchen.")],
    selfcheck=[
        ex("¿Cómo se dice «debajo de» en inglés?", "under", "Under es debajo de."),
        ex("Lee: «The sofa is gray.» ¿De qué color es el sofá?", "Gris", "Gray es gris."),
        ex("¿Qué figura es «rectangle»?", "Rectángulo", "Rectangle es rectángulo."),
    ],
    open_task=task("Lee esta descripción: «My room has a bed, a desk and a chair. The bed is next to the window. The desk is under the window. The chair is next to the desk. The window is a square.» Dibuja el cuarto y rotula bed, desk, chair, window. Une con una flecha cada rótulo con su mueble.", "Dibujo con cama al lado de la ventana, escritorio debajo de la ventana, silla al lado del escritorio, ventana cuadrada.", ["dibuja los cuatro elementos", "ubica cada mueble correctamente", "rotula en inglés"], ["dibujo rotulado", "nota del adulto"], ["poner la cama debajo de la ventana", "dibujar la ventana redonda"], "Compara el dibujo con el texto y corrige juntos las ubicaciones."),
    reinforce="Lee «The cat is under the table» y dibuja la escena.",
    extend="Describe en inglés tu mueble favorito y dónde está, con una frase como «The chair is next to the table».",
)

register(
    OA7, 4,
    materials="Los textos breves escritos en cada ejercicio; lápiz.",
    use="Aprenderé a leer textos y diálogos que piden y dan información sobre comida, ocupaciones y lugares de la ciudad. Sirve para entender menús, carteles y conversaciones cortas.",
    prior=["Conozco comidas como apple, bread, milk y rice.", "Conozco ocupaciones como teacher, nurse, doctor y cook."],
    explain=[
        "Para pedir información se usan preguntas como What is her job? (¿cuál es su trabajo?), Where is the library? (¿dónde está la biblioteca?) o Do you like rice? (¿te gusta el arroz?). Para dar información, respondes con frases cortas: She is a nurse (ella es enfermera). It is next to the park (está al lado del parque). Yes, I do (sí, me gusta).",
        "Las ocupaciones son teacher, nurse, doctor, cook, farmer y driver. Los lugares de la ciudad (city) son park, school, library, hospital, shop y market. Las comidas son apple, bread, milk, rice, fish, egg y cake.",
        "Cada ocupación se relaciona con un lugar. Una enfermera o un doctor trabajan en un hospital (hospital). Un profesor trabaja en una escuela (school). Un cocinero trabaja en una cocina (kitchen). Un granjero trabaja en el campo (field). Esas relaciones ayudan a entender lo que lees.",
    ],
    vocab=[("job", "trabajo"), ("nurse", "enfermero(a)"), ("driver", "conductor(a)"), ("library", "biblioteca"), ("hospital", "hospital"), ("Do you like ...?", "¿Te gusta ...?")],
    worked=[
        {"title": "Ocupación", "problem": "Lee: «A: What is his job? B: He is a driver.» ¿Cuál es su trabajo?", "steps": ["La pregunta es What is his job.", "La respuesta es He is a driver."], "answer": "Conductor"},
        {"title": "Lugar", "problem": "Lee: «A: Where is the library? B: It is next to the school.» ¿Dónde está la biblioteca?", "steps": ["La respuesta empieza con It is.", "Dice next to the school."], "answer": "Al lado de la escuela"},
    ],
    mistakes=[
        {"wrong": "Responder con el lugar a una pregunta de trabajo.", "why": "No se lee la palabra de la pregunta: job pide una ocupación y where pide un lugar.", "fix": "Lee la palabra de la pregunta antes de buscar la respuesta."},
        {"wrong": "Confundir yes, I do con yes, I can.", "why": "Se mezclan las respuestas de do y de can.", "fix": "Do you like ...? se responde con Yes, I do."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «She is a nurse.» ¿Cuál es su ocupación?", "Enfermera", "Nurse es enfermera."),
            ex("Lee: «I want bread.» ¿Qué comida quiere?", "Pan", "Bread es pan."),
            ex("Lee: «The park is next to the school.» ¿Qué lugar está al lado de la escuela?", "El parque", "Next to the school es al lado de la escuela."),
        ],
        "understand": [
            ex("¿Qué significa «What is her job?»", "¿Cuál es su trabajo?", "Job es trabajo."),
            ex("¿Qué pide la pregunta Where is ...?", "Un lugar", "Where significa dónde."),
            ex("¿Cómo respondes a «Do you like rice?» si te gusta?", "Yes, I do.", "Do se repite en la respuesta."),
        ],
        "apply": [
            ex("Lee: «A: Do you like milk? B: Yes, I do.» ¿Qué le gusta a B?", "La leche", "Milk es leche."),
            ex("Lee: «The doctor is in the hospital.» ¿Dónde está el doctor?", "En el hospital", "Hospital es hospital."),
            ex("Lee: «A: What is her job? B: She is a teacher.» ¿Dónde trabaja probablemente?", "En una escuela", "Un profesor trabaja en una escuela."),
        ],
        "reason": [
            ex("Lee: «A: Where is the market? B: It is next to the library.» Un niño dice que el market es una comida. ¿Qué dice el texto realmente?", "Que el mercado es un lugar al lado de la biblioteca", "Where pide un lugar."),
            ex("Lee: «A: Do you like fish? B: No, I don't.» ¿Le gusta el pescado a B?", "No", "No, I don't significa no me gusta."),
        ],
        "challenge": [
            ex("Lee: «The cook is in the kitchen. He has rice and fish. The farmer has milk and eggs.» Escribe qué tiene cada uno.", "El cocinero tiene arroz y pescado; el granjero tiene leche y huevos", "Rice, fish, milk y eggs."),
            ex("Lee: «A: Where is the hospital? B: It is next to the park. A: Where is the park? B: It is next to the school.» ¿Qué lugar está al lado del hospital y también al lado de la escuela?", "El parque", "El hospital está next to the park y la escuela también está next to the park."),
        ],
    },
    context=[ex("En un cartel de un mercado lees: «Apples, bread, milk, eggs.» ¿Cuántos alimentos distintos se ofrecen?", "4", "Hay cuatro alimentos: apples, bread, milk y eggs.")],
    selfcheck=[
        ex("¿Cómo se dice «trabajo» en inglés?", "job", "Job es trabajo."),
        ex("Lee: «The library is in the city.» ¿Qué lugar es la library?", "La biblioteca", "Library es biblioteca."),
        ex("Lee: «He is a driver.» ¿Cuál es su ocupación?", "Conductor", "Driver es conductor."),
    ],
    open_task=task("Lee este mini diálogo: «A: What is her job? B: She is a cook. A: Where is she? B: She is in the kitchen. She has rice and fish.» Responde: (1) ocupación, (2) lugar, (3) comidas. Después escribe un diálogo parecido de tres líneas con una enfermera (nurse), un hospital y una cama (bed).", "(1) cook; (2) kitchen; (3) rice and fish.", ["responde las tres preguntas", "escribe un diálogo propio", "usa una ocupación y un lugar"], ["respuestas", "diálogo propio"], ["responder con lugar en vez de ocupación", "no usar nurse ni hospital"], "Compara las respuestas con el texto y lee junto a él su diálogo propio."),
    reinforce="Lee «He is a cook» y dibuja a un cocinero.",
    extend="Escribe tres frases sobre tres lugares de la ciudad, por ejemplo «The shop is next to the park».",
)

register(
    OA7, 5,
    materials="Los textos breves escritos en cada ejercicio; lápiz, papel y espacio para actuar.",
    use="Aprenderé a leer textos que dicen qué está pasando ahora mismo, con la forma «is + verbo con -ing». Sirve para entender escenas, tarjetas y descripciones de lo que hacen las personas.",
    prior=["Conozco verbos como run, eat, draw y jump.", "Sé que -ing muestra una acción en este momento."],
    explain=[
        "Para decir qué pasa ahora mismo, se usa is o are más un verbo con -ing. «The boy is running» significa el niño está corriendo. «The children are eating» significa los niños están comiendo. «I am drawing» significa estoy dibujando.",
        "Para leer bien estas frases, busca primero quién hace la acción y luego el verbo con -ing. En «The girl is drinking water», quien actúa es the girl y la acción es drinking. En una escena de Easter puedes leer «The children are looking for eggs» (los niños buscan huevos).",
        "A veces el verbo cambia un poco: run se escribe running (con dos n) y sit se escribe sitting. Si el verbo termina en e, se pierde: write se escribe writing. Otros: play → playing (jugando), read → reading (leyendo), walk → walking (caminando), sleep → sleeping (durmiendo), hold → holding (sosteniendo). Lo importante es reconocer el -ing y que significa ahora.",
    ],
    vocab=[("is running", "está corriendo"), ("are eating", "están comiendo"), ("am drawing", "estoy dibujando"), ("is drinking", "está bebiendo"), ("children", "niños"), ("look for", "buscar")],
    worked=[
        {"title": "Acción ahora", "problem": "Lee: «The boy is running in the park.» ¿Qué hace el niño ahora?", "steps": ["Busco is y la palabra con -ing.", "Running viene de run."], "answer": "Está corriendo en el parque"},
        {"title": "Más de una persona", "problem": "Lee: «The children are looking for Easter eggs.» ¿Qué buscan los niños?", "steps": ["Are looking for significa están buscando.", "Easter eggs son huevos de Pascua."], "answer": "Huevos de Pascua"},
    ],
    mistakes=[
        {"wrong": "Pensar que «is running» significa que corre siempre.", "why": "No se interpreta que -ing es ahora.", "fix": "Is running es está corriendo ahora mismo."},
        {"wrong": "Leer «are» como el verbo ser sin entender la acción.", "why": "Se deja de lado el verbo con -ing.", "fix": "Después de is o are busca el verbo con -ing; ahí está la acción."},
    ],
    tiers={
        "recovery": [
            ex("Lee: «She is eating.» ¿Qué hace ella?", "Está comiendo", "Eating viene de eat."),
            ex("Lee: «The dog is sleeping.» ¿Qué hace el perro?", "Está durmiendo", "Sleeping viene de sleep."),
            ex("¿Qué significa «I am drawing»?", "Estoy dibujando", "Drawing viene de draw."),
        ],
        "understand": [
            ex("¿Qué indica el final -ing?", "Que la acción pasa ahora", "Es una acción en este momento."),
            ex("¿Qué dos palabras acompañan a un verbo con -ing: is y are o can y have?", "is y are", "Is y are + -ing forman la acción en el momento."),
            ex("¿Qué significa «The children are playing»?", "Los niños están jugando", "Playing viene de play."),
        ],
        "apply": [
            ex("Lee: «Mum is cooking rice in the kitchen.» ¿Qué cocina mamá y dónde?", "Arroz, en la cocina", "Rice y kitchen."),
            ex("Lee: «The monkey is climbing the tree.» ¿Qué hace el mono?", "Está trepando el árbol", "Climbing viene de climb."),
            ex("Lee: «The nurse is walking to the hospital.» ¿Hacia dónde camina?", "Hacia el hospital", "Walking to the hospital."),
        ],
        "reason": [
            ex("Lee: «The boy is drinking milk.» Un niño dice que el niño bebe agua. ¿Qué dice el texto?", "Que bebe leche", "Milk es leche."),
            ex("Lee: «The teacher is reading a story.» ¿Por qué sabes que pasa ahora?", "Porque tiene is y reading con -ing", "Is más -ing indica ahora."),
        ],
        "challenge": [
            ex("Lee la escena de Pascua: «It is Easter. The children are in the garden. They are looking for eggs. A girl is holding a basket. A boy is eating chocolate.» ¿Qué hace cada uno?", "Los niños buscan huevos; la niña sostiene una canasta; el niño come chocolate", "Looking for, holding y eating."),
            ex("Ordena para formar una frase: (1) running (2) The (3) is (4) dog.", "2, 4, 3, 1", "The dog is running."),
        ],
    },
    context=[ex("En una postal de Pascua lees: «Dear Mia, I am in the park. I am eating chocolate. The bunny is next to me. From Leo.» ¿Qué hace Leo ahora?", "Come chocolate en el parque", "Eating chocolate significa comiendo chocolate.")],
    selfcheck=[
        ex("¿Cómo se dice «está corriendo» en inglés?", "is running", "Is running es está corriendo."),
        ex("Lee: «She is writing.» ¿Qué hace ella?", "Escribe", "Writing viene de write."),
        ex("¿Qué indica «-ing»?", "Una acción ahora", "-ing es el momento."),
    ],
    open_task=task("Lee estas cinco frases y haz una mímica de cada una: «1. The boy is running. 2. The girl is eating. 3. The dog is sleeping. 4. The cook is cooking. 5. The children are looking for eggs.» Después dibuja una de las escenas y escribe debajo la frase en inglés.", "Dibujo y mímica de las cinco escenas.", ["hace las cinco mímicas", "dibuja una escena", "escribe la frase correcta"], ["foto o video con permiso de la familia", "dibujo con frase"], ["confundir sleeping con eating", "olvidar el is"], "Comparen mímica y frase para ver si coinciden y repasen los verbos."),
    reinforce="Lee en voz alta «The boy is running» y haz la mímica.",
    extend="Escribe cuatro frases con is o are y verbos con -ing sobre lo que pasa en tu casa hoy.",
)
