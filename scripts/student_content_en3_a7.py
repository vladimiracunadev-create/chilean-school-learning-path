"""Student material for 3.º básico Inglés (propuesta), EN03 OA 07 (leer sobre temas conocidos o de otras asignaturas).

Los textos son originales y breves, con pista en español. Cada estructura se explica antes de usarla.
"""
from __future__ import annotations

from student_content_en3_a import E, lesson, task
from student_lessons import arith

OA7 = "EN03 OA 07"

lesson(
    OA7, 1,
    "Los textos escritos en cada ejercicio y un lápiz.",
    "Aprenderé a leer textos sobre la sala de clases y la casa, y a preguntar y decir dónde está algo. Sirve para entender descripciones de lugares.",
    ["Sé que in, on y under dicen dónde está algo.", "Sé que There is y There are significan hay."],
    [
        "Un texto sobre la sala de clases puede decir: «This is my classroom. There are twelve desks. There is a board. The clock is on the wall.» (classroom = sala de clases, desk = pupitre, board = pizarra, clock = reloj, wall = pared). This is significa «esta es». There are se usa para varios y There is para uno.",
        "Un texto sobre la casa puede decir: «This is my house. There is a kitchen. There is a bedroom. The bed is in the bedroom. The sofa is in the living room.» (kitchen = cocina, bedroom = dormitorio, bed = cama, sofa = sofá, living room = sala de estar). Para preguntar dónde está algo se dice «Where is the bed?» y se responde «It is in the bedroom».",
        "Al leer, busca primero la palabra que preguntas: Where? pide un lugar y How many? pide un número. Luego busca in, on o under, que dicen dónde está algo. Responde con la parte del texto que lo prueba.",
    ],
    [("classroom", "sala de clases"), ("desk", "pupitre"), ("clock", "reloj"), ("kitchen / bedroom", "cocina / dormitorio"), ("bed / sofa", "cama / sofá"), ("Where is...?", "¿dónde está...?"), ("It is in...", "está en...")],
    [
        ("Un número en la sala", "Lee: «This is my classroom. There are twelve desks. There is a board. The clock is on the wall.» ¿Cuántos pupitres hay?", ["Busco desks.", "Antes está twelve.", "Twelve es doce."], "12"),
        ("Un lugar en la casa", "Lee: «This is my house. There is a kitchen. There is a bedroom. The bed is in the bedroom.» ¿Dónde está la cama?", ["Busco bed.", "Después dice in the bedroom.", "In es en o dentro de."], "En el dormitorio"),
    ],
    [
        ("Confundir There is con There are.", "No se mira si es uno o varios.", "There is es para uno y There are para varios."),
        ("Decir que la cama está en la cocina.", "No se busca el lugar en el texto.", "Busca in the bedroom en la frase de la cama."),
    ],
    [
        ("Lee: «This is my classroom. There are twelve desks. There is a board. The clock is on the wall.» ¿Cuántos pupitres hay?", "12", "Twelve es doce."),
        ("Lee: «This is my house. There is a kitchen. There is a bedroom. The bed is in the bedroom.» ¿Dónde está la cama?", "En el dormitorio", "In the bedroom."),
        ("¿Qué significa «Where is the clock?»", "¿Dónde está el reloj?", "Where is pregunta por un lugar."),
    ],
    [
        ("¿Cuál es la diferencia entre There is y There are?", "There is es para uno y There are para varios", "Una se usa en singular y la otra en plural."),
        ("¿Qué significa «This is my house»?", "Esta es mi casa", "This is presenta algo."),
        ("¿Qué palabra de una pregunta pide un lugar?", "Where", "Where significa dónde."),
    ],
    [
        ("Lee: «A: Where is the sofa? B: It is in the living room.» ¿Dónde está el sofá?", "En la sala de estar", "In the living room."),
        ("Lee: «The lamp is on the table.» (lamp = lámpara, table = mesa). ¿Dónde está la lámpara?", "Sobre la mesa", "On the table."),
        ("Completa: «___ is a board in the classroom.»", "There", "There is a board significa hay una pizarra."),
    ],
    [
        ("Ana dice que la cama está en la cocina. ¿Qué frase del texto la corrige?", "The bed is in the bedroom", "In the bedroom es el lugar de la cama."),
        ("Para decir que hay tres sillas, ¿usas There is three chairs o There are three chairs?", "There are three chairs", "Three chairs son varias sillas."),
    ],
    [
        arith("Lee: «In room A there are eight desks. In room B there are four desks.» (room = sala). ¿Cuántos pupitres hay en total?", "8+4", "Se suman los escritorios de las dos salas."),
        ("Lee: «The cat is on the sofa. The sofa is in the living room.» ¿Dónde está el gato?", "Sobre el sofá, en la sala de estar", "El gato está sobre el sofá y el sofá está en la sala de estar."),
    ],
    [("En tu cuaderno encuentras: «This is my classroom. There is a board. The clock is on the wall.» ¿Dónde está el reloj?", "Sobre la pared", "On the wall.")],
    [
        ("¿Cómo se dice «cocina» en inglés?", "kitchen", "Kitchen es cocina."),
        ("¿Qué significa «bedroom»?", "Dormitorio", "Bed es cama y room es habitación."),
        ("Lee: «The lamp is on the table.» ¿Es la lámpara debajo de la mesa?", "No; está sobre la mesa", "On significa sobre."),
    ],
    task("Lee este texto: «This is my house. There is a kitchen. There is a bedroom. The bed is in the bedroom. The sofa is in the living room.» Dibuja un plano sencillo con las tres habitaciones y escribe su nombre en inglés. Pon la cama en el dormitorio y el sofá en la sala de estar.", "Dibujo con kitchen, bedroom (con bed) y living room (con sofa).", ["dibuja las tres habitaciones", "pone la cama en el dormitorio", "pone el sofá en la sala de estar"], ["plano dibujado", "nota del adulto"], ["poner la cama en la cocina", "no escribir los nombres"], "Reconoce los lugares correctos y vuelve a leer con él la frase que no coincide."),
    "Pide a un adulto que lea «Where is the bed?» y señala el dibujo del dormitorio.",
    "Escribe tres frases sobre tu sala de clases con There is, There are y on the wall.",
)

lesson(
    OA7, 2,
    "Los textos escritos en cada ejercicio y un lápiz.",
    "Aprenderé a leer textos sobre animales salvajes y figuras geométricas, y a encontrar datos como cuántos lados tiene una figura. Sirve para aprender datos de otras asignaturas leyendo en inglés.",
    ["Sé que lion, elephant y monkey son animales salvajes.", "Sé que circle, square y triangle son figuras."],
    [
        "Un texto informativo sobre un animal puede decir: «A giraffe is a tall wild animal. It has a long neck. It is yellow and brown.» (giraffe = jirafa, tall = alto, neck = cuello). Has significa «tiene». Otro ejemplo: «An elephant is a big gray wild animal. It has a long trunk.»",
        "Un texto sobre figuras puede decir: «A triangle has three sides. A square has four sides.» (side = lado). También: «The book is a rectangle. It is on the table.» (rectangle = rectángulo). Has se usa para decir cuántos lados o partes tiene algo.",
        "Al leer, busca palabras clave: nombres de animales o figuras, colores, números y partes del cuerpo. Después responde la pregunta con el dato exacto. Si el texto dice three sides, la respuesta es 3, no 4.",
    ],
    [("giraffe", "jirafa"), ("tall", "alto"), ("neck", "cuello"), ("side", "lado"), ("rectangle", "rectángulo"), ("has", "tiene")],
    [
        ("Dato de un animal", "Lee: «A giraffe is a tall wild animal. It has a long neck. It is yellow and brown.» ¿Cómo es el cuello de la jirafa?", ["Busco neck.", "Dice a long neck.", "Long es largo."], "Largo"),
        ("Dato de una figura", "Lee: «A triangle has three sides. A square has four sides.» ¿Cuántos lados tiene un triángulo?", ["Busco triangle.", "Dice three sides.", "Three es tres."], "3"),
    ],
    [
        ("Responder 4 para el triángulo.", "Se confunde la figura con el cuadrado.", "Lee la frase de cada figura: triangle tiene tres lados."),
        ("Pensar que una jirafa es un animal pequeño.", "No se lee la palabra tall.", "Tall significa alto."),
    ],
    [
        ("Lee: «A giraffe is a tall wild animal. It has a long neck. It is yellow and brown.» ¿Cómo es su cuello?", "Largo", "A long neck."),
        ("Lee: «A triangle has three sides. A square has four sides.» ¿Cuántos lados tiene un triángulo?", "3", "El texto dice three sides."),
        ("En el texto de la jirafa, ¿de qué colores es?", "Amarilla y café", "Yellow and brown."),
    ],
    [
        ("¿Qué significa «side»?", "Lado", "Se usa para contar los lados de una figura."),
        ("¿Qué significa «tall»?", "Alto", "Describe algo de gran altura."),
        ("¿Qué significa «has»?", "Tiene", "Has se usa con una figura o un animal."),
    ],
    [
        ("Lee: «A square has four sides.» ¿Cuántos lados tiene un cuadrado?", "4", "El texto dice four sides."),
        ("Lee: «A giraffe is a tall wild animal.» ¿Es una jirafa un animal pequeño?", "No; es un animal alto", "Tall es alto."),
        ("Lee: «The book is a rectangle. It is on the table.» (rectangle = rectángulo). ¿Qué forma tiene el libro?", "Rectángulo", "The book is a rectangle."),
    ],
    [
        ("Un niño dice que el triángulo tiene cuatro lados. ¿Qué frase del texto lo corrige?", "A triangle has three sides", "Three es tres."),
        ("Según el texto de las figuras, ¿cuál tiene más lados: el triángulo o el cuadrado?", "El cuadrado", "Cuatro es mayor que tres."),
    ],
    [
        arith("Lee: «A triangle has three sides. A square has four sides.» ¿Cuántos lados tienen en total las dos figuras juntas?", "3+4", "Se suman los lados de las dos figuras."),
        ("Lee: «An elephant is a big gray wild animal. It has a long trunk.» (trunk = trompa). ¿Qué animal tiene la trompa larga?", "El elefante", "It has a long trunk habla del elefante."),
    ],
    [("En un libro de ciencias lees: «A giraffe is a tall wild animal. It has a long neck.» ¿Qué parte del cuerpo es larga?", "El cuello", "Neck es cuello.")],
    [
        ("¿Cómo se dice «jirafa» en inglés?", "giraffe", "Giraffe es jirafa."),
        ("¿Qué significa «rectangle»?", "Rectángulo", "Es una figura con cuatro lados."),
        ("Lee: «An elephant is a big gray wild animal.» ¿De qué color es?", "Gris", "Gray es gris."),
    ],
    task("Lee: «A triangle has three sides. A square has four sides.» En una hoja dibuja un triángulo y un cuadrado. Cuenta los lados de cada uno y escribe debajo three sides y four sides.", "Un triángulo con three sides y un cuadrado con four sides.", ["dibuja un triángulo con 3 lados", "dibuja un cuadrado con 4 lados", "escribe three sides y four sides"], ["dibujo con etiquetas", "nota del adulto"], ["dibujar un triángulo con 4 lados", "intercambiar las etiquetas"], "Reconoce el número correcto y cuenta con él los lados otra vez."),
    "Pide a un adulto que lea «three sides» y toca los lados de un triángulo.",
    "Escribe una frase sobre otro animal salvaje usando has y un color.",
)

lesson(
    OA7, 3,
    "Los textos y las preguntas escritos en cada ejercicio y un lápiz.",
    "Aprenderé a leer sobre ocupaciones y lugares de una ciudad, a preguntar quién es y dónde está una persona. Sirve para entender textos sobre trabajos y lugares.",
    ["Sé que she significa ella y he significa él.", "Sé que school y park son lugares."],
    [
        "Un texto sobre trabajos puede decir: «Ana is a teacher. She is at school. Sam is a doctor. He is at the hospital. Lia is a cook. She is at the restaurant.» (teacher = profesora, doctor = médico, cook = cocinera, restaurant = restaurante, hospital = hospital). Cada persona está en su lugar de trabajo. Para decir dónde está o trabaja alguien se usa at: «at the hospital» significa «en el hospital» y «at school» significa «en la escuela». Ojo: in the hospital da la idea de estar internado como paciente, por eso aquí se usa at.",
        "Para preguntar por una ocupación se dice «What is your job?» (¿cuál es tu trabajo?) y se responde «I'm a cook». Para preguntar por otra persona se dice «Is she a teacher?» (¿ella es profesora?) y se responde «Yes, she is» (sí) o «No, she isn't» (no). Para preguntar el lugar se dice «Where is Sam?».",
        "Al leer, une el nombre con su trabajo y su lugar. No supongas nada: lee la frase de cada persona. El texto dice quién es cocinero o doctor, y no depende de si es hombre o mujer.",
    ],
    [("job", "trabajo"), ("teacher / doctor / cook", "profesor o profesora / médico o médica / cocinero o cocinera"), ("school / hospital / restaurant", "escuela / hospital / restaurante"), ("Is she...? Yes, she is", "¿ella es...? sí"), ("No, she isn't", "no"), ("Where is...?", "¿dónde está...?")],
    [
        ("Un trabajo", "Lee: «Ana is a teacher. She is at school. Sam is a doctor. He is at the hospital. Lia is a cook. She is at the restaurant.» ¿Cuál es el trabajo de Sam?", ["Busco Sam.", "Dice Sam is a doctor.", "Doctor es médico."], "Médico"),
        ("Un lugar", "En el mismo texto, ¿dónde está Lia?", ["Busco Lia.", "Dice She is at the restaurant.", "Restaurant es restaurante."], "En el restaurante"),
    ],
    [
        ("Poner a Ana en el hospital.", "No se une cada persona con su lugar.", "Lee la frase de cada persona antes de responder."),
        ("Responder Yes, she is cuando el texto dice otro trabajo.", "No se comprueba con el texto.", "Si el texto dice otro trabajo, responde No, she isn't."),
    ],
    [
        ("Lee: «Ana is a teacher. She is at school. Sam is a doctor. He is at the hospital. Lia is a cook. She is at the restaurant.» ¿Dónde está Sam?", "En el hospital", "He is at the hospital."),
        ("En el mismo texto, ¿cuál es el trabajo de Lia?", "Cocinera", "Lia is a cook."),
        ("En el mismo texto, ¿qué trabajo tiene Ana?", "Profesora", "Ana is a teacher."),
    ],
    [
        ("¿Qué significa «What is your job?»", "¿Cuál es tu trabajo?", "Job es trabajo."),
        ("¿Qué significa «No, she isn't»?", "No, ella no lo es", "Se usa para responder que no."),
        ("¿Qué significa «Where is Sam?»", "¿Dónde está Sam?", "Where pregunta por un lugar."),
    ],
    [
        ("Lee: «A: Is Sam a cook? B: No, he isn't. He is a doctor.» ¿Es Sam cocinero?", "No", "No, he isn't."),
        ("Según el texto de Ana, Sam y Lia, ¿dónde trabaja un doctor?", "En el hospital", "Sam is a doctor y está en el hospital."),
        ("Lee: «A: Is Ana a teacher? B: Yes, she is.» ¿Es Ana profesora?", "Sí", "Yes, she is."),
    ],
    [
        ("Pedro dice que Ana es cocinera. ¿Qué frase del texto lo corrige?", "Ana is a teacher", "Ana es profesora."),
        ("Completa: «Where is Lia? She is at the ___.»", "restaurant", "Lia está en el restaurant según el texto."),
    ],
    [
        ("En el texto de Ana, Sam y Lia, ¿cuántos lugares distintos aparecen?", "3", "School, hospital y restaurant."),
        ("¿Quién está en el hospital y qué trabajo tiene?", "Sam, médico", "He is at the hospital y Sam is a doctor."),
    ],
    [("En un cartel lees: «Sam is a doctor. He is at the hospital.» ¿Qué hace falta saber para responder dónde está Sam?", "Leer la frase He is in the hospital", "Esa frase dice el lugar.")],
    [
        ("¿Cómo se dice «trabajo» en inglés?", "job", "Job es trabajo."),
        ("¿Qué significa «cook»?", "Cocinero o cocinera", "Es quien prepara comida."),
        ("¿Qué significa «hospital»?", "Hospital", "Es el lugar donde trabaja un médico."),
    ],
    task("Lee: «Ana is a teacher. She is at school. Sam is a doctor. He is at the hospital. Lia is a cook. She is at the restaurant.» Haz una tabla con tres columnas: nombre, trabajo y lugar. Completa las tres filas.", "Ana - teacher - school; Sam - doctor - hospital; Lia - cook - restaurant.", ["escribe las tres filas", "une cada nombre con su trabajo", "une cada trabajo con su lugar"], ["tabla escrita", "nota del adulto"], ["poner a Sam en la escuela", "mezclar trabajos"], "Reconoce las filas correctas y vuelve con él a la frase de la persona que se equivocó."),
    "Pide a un adulto que diga «doctor» y «hospital» y señala dónde trabaja un doctor.",
    "Escribe tres preguntas con Is she...? o Is he...? sobre los personajes del texto y responde cada una.",
)

lesson(
    OA7, 4,
    "Los textos y diálogos escritos en cada ejercicio y un lápiz.",
    "Aprenderé a leer sobre comida y sobre una celebración, a preguntar qué me gusta y qué quiero, y a responder. Sirve para entender menús, diálogos y textos sobre celebraciones.",
    ["Sé que I like significa me gusta.", "Sé que Here! significa ¡toma!"],
    [
        "Para preguntar si algo te gusta se dice «Do you like fish?» (¿te gusta el pescado?). Se responde «Yes, I do» (sí) o «No, I don't» (no). Para pedir comida se dice «What do you want?» (¿qué quieres?) y se responde «I want rice, please» (quiero arroz, por favor). Palabras de comida: bread (pan), milk (leche), fish (pescado), rice (arroz).",
        "Mira un diálogo: «Ana: What do you want? Tom: I want rice, please. Ana: Here! Tom: Thank you!» Tom pide arroz y Ana se lo da. Easter es la Pascua, una celebración cristiana que no todas las familias celebran. Un texto sobre una celebración puede decir: «Easter is a celebration. People paint eggs. Some people eat chocolate eggs. Happy Easter!» (people = personas, paint = pintan, some = algunas).",
        "Al leer, busca qué pide o qué le gusta a cada persona. Presta atención a Yes o No. Cuando lees una celebración, busca qué hacen las personas y qué cosas aparecen, como eggs. No hace falta que todas las personas hagan lo mismo: el texto dice solo lo que dice.",
    ],
    [("Do you like...?", "¿te gusta...?"), ("Yes, I do / No, I don't", "sí / no"), ("What do you want?", "¿qué quieres?"), ("I want", "yo quiero"), ("bread / milk / fish / rice", "pan / leche / pescado / arroz"), ("Easter", "Pascua"), ("people", "personas")],
    [
        ("Un pedido", "Lee: «Ana: What do you want? Tom: I want rice, please. Ana: Here! Tom: Thank you!» ¿Qué pide Tom?", ["Busco I want.", "Dice rice.", "Rice es arroz."], "Arroz"),
        ("Una celebración", "Lee: «Easter is a celebration. People paint eggs. Some people eat chocolate eggs. Happy Easter!» ¿Qué hacen las personas con los huevos?", ["Busco eggs.", "Dice People paint eggs.", "Paint es pintar."], "Los pintan"),
    ],
    [
        ("Responder Yes, I do a una pregunta cuando no te gusta.", "No se piensa en la respuesta que corresponde.", "Responde No, I don't si no te gusta."),
        ("Pensar que todas las personas comen huevos de chocolate en Easter.", "El texto dice some people, o sea algunas.", "Some significa algunas, no todas."),
    ],
    [
        ("Lee: «Ana: What do you want? Tom: I want rice, please. Ana: Here! Tom: Thank you!» ¿Qué le da Ana a Tom?", "Arroz", "Ana dice Here! después de que Tom pide arroz."),
        ("Lee: «Easter is a celebration. People paint eggs. Some people eat chocolate eggs. Happy Easter!» ¿Qué es Easter?", "Una celebración", "Easter is a celebration."),
        ("¿Qué significa «Do you like fish?»", "¿Te gusta el pescado?", "Do you like pregunta por un gusto."),
    ],
    [
        ("¿Qué significa «What do you want?»", "¿Qué quieres?", "Se usa para pedir algo."),
        ("¿Cómo se responde que sí a «Do you like milk?»", "Yes, I do", "Yes, I do significa sí."),
        ("¿Qué significa «some people»?", "Algunas personas", "Some no es todos."),
    ],
    [
        ("Lee: «A: Do you like fish? B: No, I don't. I like bread.» ¿Le gusta el pescado a B?", "No", "No, I don't."),
        ("En el mismo diálogo, ¿qué le gusta a B?", "El pan", "I like bread."),
        ("Lee: «Easter is a celebration. People paint eggs. Some people eat chocolate eggs.» ¿Todas las personas comen huevos de chocolate?", "No; algunas personas", "Some people dice algunas."),
    ],
    [
        ("Un niño dice que Tom pidió leche. ¿Qué dice el diálogo de Ana y Tom?", "Que pidió arroz (rice)", "I want rice, please."),
        ("Pablo responde «Yes, I do» a «Do you like milk?», pero la persona dice que no le gusta. ¿Qué respuesta le corresponde?", "No, I don't", "Si no le gusta se responde que no."),
    ],
    [
        ("Lee: «A: What do you want? B: I want milk and bread, please.» (and = y) ¿Cuántas comidas pide B?", "2", "Milk y bread."),
        ("Lee: «Easter is a celebration. People paint eggs.» ¿Easter es una comida o una celebración?", "Una celebración", "Easter is a celebration."),
    ],
    [("En un restaurante escuchas: «What do you want? I want fish, please.» ¿Qué pide la persona?", "Pescado", "Fish es pescado.")],
    [
        ("¿Cómo se dice «leche» en inglés?", "milk", "Milk es leche."),
        ("¿Qué significa «please»?", "Por favor", "Se usa al pedir algo."),
        ("¿Qué significa «Happy Easter»?", "Feliz Pascua", "Es un saludo de celebración."),
    ],
    task("Lee: «Ana: What do you want? Tom: I want rice, please. Ana: Here! Tom: Thank you!» Escribe en una hoja qué pide Tom y qué dice Ana cuando le da el plato. Luego escribe tu propia respuesta a «Do you like fish?» con Yes, I do o No, I don't.", "Tom pide arroz; Ana dice Here!; respuesta propia con Yes, I do o No, I don't.", ["escribe rice", "escribe Here!", "responde Yes, I do o No, I don't"], ["hoja con tres respuestas", "nota del adulto"], ["decir que Tom pide milk", "no responder con Yes ni No"], "Reconoce las respuestas correctas y revisa con él la expresión Here!."),
    "Pide a un adulto que diga «I want bread» y respóndele con Here! mientras le muestras un pan dibujado.",
    "Escribe un diálogo de cuatro líneas en que una persona pide comida y la otra se la da.",
)

lesson(
    OA7, 5,
    "Los textos escritos en cada ejercicio y un lápiz.",
    "Aprenderé a comparar información de dos textos sin usar estereotipos. Sirve para entender que cualquier persona puede tener cualquier trabajo y para comparar datos con respeto.",
    ["Sé leer sobre ocupaciones y lugares.", "Sé que she y he significan ella y él."],
    [
        "Comparar es ver qué tienen igual y qué tienen distinto dos cosas o personas. Lee: «Sara is a firefighter. She is strong. Tom is a nurse. He is kind.» (firefighter = bombero o bombera, nurse = enfermero o enfermera, strong = fuerte, kind = amable). Sara y Tom tienen trabajos distintos.",
        "La palabra both significa «los dos» o «las dos». Si el texto dice «Sara is a firefighter. She is kind. Tom is a nurse. He is kind», entonces «Both are kind»: los dos son amables. Para comparar, busca lo que es igual (both) y lo que es diferente.",
        "Un estereotipo es una idea fija que dice que solo cierto tipo de personas puede hacer algo, por ejemplo «solo los hombres pueden ser bomberos». Es falso: cualquier persona puede tener cualquier trabajo. Al leer, usa solo lo que dice el texto y no ideas fijas.",
    ],
    [("compare", "comparar"), ("both", "los dos, las dos"), ("firefighter", "bombero o bombera"), ("nurse", "enfermero o enfermera"), ("strong / kind", "fuerte / amable"), ("stereotype", "idea fija sobre un tipo de personas")],
    [
        ("Comparar dos personas", "Lee: «Sara is a firefighter. She is kind. Tom is a nurse. He is kind.» ¿Qué tienen igual Sara y Tom?", ["Busco lo que repite el texto.", "Los dos son kind.", "Both are kind."], "Los dos son amables"),
        ("Evitar un estereotipo", "Un niño dice que los bomberos solo pueden ser hombres. En el texto, Sara es bombera. ¿Tiene razón?", ["Busco Sara.", "Sara is a firefighter.", "Una mujer es bombera."], "No; Sara es bombera"),
    ],
    [
        ("Decir que solo los hombres pueden ser bomberos.", "Es una idea fija que no está en el texto.", "Usa solo lo que dice el texto: cualquiera puede ser bombero."),
        ("Pensar que both significa uno de los dos.", "Se confunde both con una sola persona.", "Both significa los dos."),
    ],
    [
        ("Lee: «Sara is a firefighter. She is strong. Tom is a nurse. He is kind.» ¿Cuál es el trabajo de Sara?", "Bombera", "Sara is a firefighter."),
        ("En el mismo texto, ¿cuál es el trabajo de Tom?", "Enfermero", "Tom is a nurse."),
        ("En el mismo texto, ¿quién es fuerte?", "Sara", "She is strong habla de Sara."),
    ],
    [
        ("¿Qué significa «both»?", "Los dos", "Both une a dos personas."),
        ("En Inglés: ¿Qué es un estereotipo?", "Una idea fija de que solo cierto tipo de personas puede hacer algo", "Es una idea falsa sobre las personas."),
        ("¿Por qué conviene evitar los estereotipos?", "Porque cualquier persona puede tener cualquier trabajo", "Respetan a todas las personas."),
    ],
    [
        ("Lee: «Lia is a farmer. Ben is a cook. Both are happy.» (farmer = agricultora). ¿Quiénes están felices?", "Los dos", "Both are happy."),
        ("En el mismo texto, ¿qué es diferente entre Lia y Ben?", "Su trabajo", "Lia es farmer y Ben es cook."),
        ("Lee: «Sara is a firefighter. She is kind. Tom is a nurse. He is kind.» ¿Qué tienen en común?", "Los dos son amables", "Both are kind."),
    ],
    [
        ("Una niña dice que solo las mujeres pueden ser enfermeras. En el texto, Tom es enfermero. ¿Qué muestra el texto?", "Que un hombre también puede ser enfermero", "Tom is a nurse."),
        ("Un niño dice que los agricultores son siempre hombres. En el texto «Lia is a farmer. Ben is a cook. Both are happy.», Lia es agricultora. ¿Qué frase del texto lo corrige?", "Lia is a farmer", "Lia es una mujer y es agricultora."),
    ],
    [
        ("¿Qué frase evita un estereotipo: a) Solo las niñas pueden ser enfermeras. b) Tom es enfermero y Sara es bombera: cualquier persona puede tener esos trabajos.", "b", "Dice que cualquiera puede tener esos trabajos."),
        ("Lee: «Lia is a farmer. Ben is a cook. Both are happy.» ¿Cuántas personas son felices?", "2", "Both son dos personas."),
    ],
    [("En tu clase comparan dos textos: Sara bombera y Tom enfermero. Alguien dice que Tom no puede ser enfermero porque es hombre. ¿Qué respondes?", "Que el texto dice que Tom es enfermero y cualquiera puede serlo", "Tom is a nurse es evidencia.")],
    [
        ("¿Cómo se dice «los dos» en inglés?", "both", "Both es los dos."),
        ("¿Qué significa «nurse»?", "Enfermero o enfermera", "Trabaja cuidando personas."),
        ("¿Qué significa «strong»?", "Fuerte", "Describe a alguien con fuerza."),
    ],
    task("Lee: «Sara is a firefighter. She is kind. Tom is a nurse. He is kind.» Escribe en una hoja una cosa igual (Both are kind) y una diferente (sus trabajos). Luego escribe en español una frase que diga que cualquier persona puede tener cualquier trabajo.", "Both are kind. Sara is a firefighter and Tom is a nurse. Cualquier persona puede tener cualquier trabajo.", ["escribe una semejanza", "escribe una diferencia", "no usa estereotipos"], ["hoja con tres frases", "nota del adulto"], ["decir que un trabajo es solo de hombres o solo de mujeres", "no escribir ninguna diferencia"], "Reconoce la comparación y conversa con él sobre por qué los estereotipos no son ciertos."),
    "Pide a un adulto que lea «Both are kind» y apunta a los dos personajes.",
    "Compara dos personas de un texto con both y una diferencia, sin usar ideas fijas.",
)
