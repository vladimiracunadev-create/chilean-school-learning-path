"""Cuaderno del estudiante, 8.º básico Inglés (propuesta): EN08 OA 11, textos breves multimodales para audiencias reales.

Todos los textos en inglés son originales, breves y ficticios, con pista en español. Los modelos y criterios de cada
género están escritos dentro de la propia clase. Sin audio ni material externo. Los títulos de clase del plan son
genéricos (propósito, evidencia, estrategia, brecha de información, respuesta independiente): aquí se aplican a un
género por clase (correo formal, descripción con pie de foto, instrucciones con íconos, noticia, biografía y resumen).
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA11 = "EN08 OA 11"


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ================================================================ clase 1: correo formal
lesson(
    OA11, 1,
    "Los modelos y criterios escritos en cada ejercicio, lápiz y una hoja. Un computador es opcional.",
    "Aprenderé a escribir un correo electrónico formal siguiendo un modelo y cinco criterios. Sirve para pedir información a una persona que no conozco, con respeto y con claridad.",
    ["Sé escribir un correo informal con saludo, mensaje y despedida.", "Conozco Could you…? y I would like to… como formas corteses."],
    [
        "Un correo formal se escribe a alguien que no conoces o a una autoridad: una directora, una bibliotecaria, una oficina. Cambia la audiencia (audience, quién lee) y por eso cambia el tono. No se usan abreviaciones como «u» ni «wanna», y se escribe I am en vez de I'm. Modelo: «Subject: Library card. Dear Ms. Pino, I am a student in 8th grade. I would like to get a library card. Could you tell me which documents I need? Thank you for your help. Best regards, Julián Soto».",
        "Para pedir con cortesía usa Could you + verbo (Could you send me the schedule?) o I would like to + verbo (I would like to book a visit). Una orden directa como «Send me the price» suena brusca. Un correo puede llevar también un recurso multimodal, es decir, algo más que texto: un archivo adjunto (attachment), como una foto o un mapa. Se anuncia así: Please see the attached map.",
        "Criterios para revisar: 1) asunto (subject) concreto, no vago como Hello; 2) saludo formal con título y apellido (Dear Ms. Pino,); 3) el propósito (purpose, para qué escribes) aparece en las primeras oraciones; 4) petición cortés con Could you o I would like to; 5) despedida formal (Best regards,) y tu nombre. Al terminar, revisa tu texto criterio por criterio.",
    ],
    [("subject", "asunto: línea que resume de qué trata el correo"), ("Dear Ms./Mr.", "Estimada/o señora/señor (saludo formal)"), ("Best regards", "Saludos cordiales (despedida formal)"), ("Could you…?", "¿Podría usted…? (petición cortés)"), ("I would like to…", "Me gustaría… (petición cortés)"), ("attachment", "archivo adjunto: foto, mapa o documento que acompaña el correo"), ("purpose", "propósito: para qué escribes"), ("audience", "audiencia: quién va a leer el texto")],
    [
        ("Elegir el saludo para una audiencia formal", "Escribes a una persona que no conoces, el Sr. Vera, que dirige un museo. ¿Qué saludo usas? A) Hey Vera! B) Dear Mr. Vera,", ["La audiencia es una autoridad desconocida.", "Para eso se usa Dear + título + apellido.", "El saludo es Dear Mr. Vera,"], "Dear Mr. Vera,"),
        ("Volver cortés una orden", "Orden: «Send me the schedule.» Reescríbela como petición cortés con Could you.", ["Empieza con Could you.", "Mantén el verbo en forma base: send.", "Cierra con signo de interrogación."], "Could you send me the schedule?"),
    ],
    [
        ("Escribir «Hi!» a la directora de un museo.", "Se usa el saludo informal con una audiencia formal.", "Usa Dear Ms. y el apellido."),
        ("Poner Hello como asunto.", "Un asunto vago no dice de qué trata el correo.", "Usa un asunto concreto: Question about museum prices."),
    ],
    [
        ("En un correo, ¿qué línea resume de qué trata? A) subject B) Best regards", "A", "El subject es el asunto; Best regards es la despedida."),
        ("Para escribirle a una bibliotecaria que no conoces, la Sra. Pino, ¿qué saludo corresponde? A) Hey Pino! B) Dear Ms. Pino,", "B", "Con una persona desconocida se usa un saludo formal con título y apellido."),
        ("¿Qué frase es más formal? A) I would like to know the price. B) I want the price now.", "A", "I would like to suaviza el pedido, mientras que I want ... now suena como una orden."),
    ],
    [
        ("Correo: «Subject: School trip. Dear Ms. Lagos, I would like to book a visit for 25 students. Could you tell me which days are free in May? Best regards, Paz Mora». ¿Cuál es el propósito? A) Reservar una visita para 25 estudiantes B) Agradecer un regalo C) Devolver un libro", "A", "La primera oración pide reservar una visita para 25 estudiantes."),
        ("Mensaje: «Dear Mr. Vera, I am writing about the bus. Send me the bus time. Could you also confirm the price? Thank you, Ana». ¿Qué oración debe cambiarse por ser una orden directa? Copia la oración.", "Send me the bus time.", "Es la única oración sin fórmula cortés; las otras usan Could you o thank you."),
        ("Texto: «Subject: Robotics workshop. Dear Ms. Núñez, I would like to join the workshop. Could you tell me the start date? Thank you.» Se revisan 5 criterios: asunto concreto, saludo formal, propósito, petición cortés, despedida con nombre. ¿Cuántos cumple?", "4", "Cumple asunto, saludo, propósito y petición; falla la despedida con nombre."),
    ],
    [
        ("Elige la versión que cambia «I want a map of the park.» por una fórmula cortés con I would like to. A) I would like to have a map of the park. B) I would like have a map of the park. C) I want to have a map of the park, please.", "A", "I would like to lleva to antes del verbo; la B omite to y la C sigue usando I want."),
        ("Tienes que preguntar si el club de ajedrez del barrio acepta jóvenes. ¿Qué asunto es mejor? A) Hello B) Question about the chess club C) URGENT!!!", "B", "Dice exactamente de qué trata el correo."),
        ("Elige la despedida formal para una persona desconocida: A) See ya! B) Best regards, C) Bye bye", "B", "Best regards es una despedida formal y respetuosa."),
    ],
    [
        ("Versión 1: «Hi! Give me info about the trip.» Versión 2: «Dear Ms. Vera, could you give me information about the trip?» La audiencia es la rectora. ¿Qué versión es mejor? A) Versión 1 B) Versión 2", "B", "Tiene saludo formal y una petición cortés con could you."),
        ("Un estudiante escribe: «Dear Sir, I would like information. Thank you, Eli». ¿Qué dato haría más claro el propósito? A) El precio para 20 estudiantes el viernes B) El clima de hoy C) Su color favorito", "A", "El lector necesita saber qué información se pide, para quiénes y cuándo."),
    ],
    [
        ("Ordena las líneas de un correo formal y escribe las letras en orden. a) Best regards, Tomás Vera b) Subject: Robotics workshop c) I would like to join the workshop. Could you tell me the start date? d) Dear Ms. Núñez,", "b, d, c, a", "El correo va así: asunto, saludo, mensaje y despedida con nombre."),
        ("Correo: «Subject: Hello. Dear Ms. Lagos, I would like to book a visit. Could you tell me the free days? Best regards, Paz Mora». Con los 5 criterios de la clase, ¿cuál es el único que falla? Responde con su número.", "1", "El asunto Hello es vago; los otros cuatro criterios se cumplen."),
    ],
    [("Tu curso necesita permiso para usar el patio del colegio un sábado. Eliges entre dos correos. Texto 1: «Subject: Request to use the yard. Dear Mr. Rojas, I would like to use the yard on Saturday. Could you confirm if it is free? Best regards, Sol». Texto 2: «Subject: yard. Hi. I wanna use the yard. Tell me. Sol». ¿Cuál cumple mejor los criterios? A) Texto 1 B) Texto 2", "A", "Tiene asunto concreto, saludo formal, petición cortés y despedida con nombre.")],
    [
        ("¿Qué expresión sirve para pedir con cortesía una acción a otra persona?", "Could you", "Could you + verbo suaviza la petición."),
        ("¿Qué es un archivo adjunto en un correo?", "Un archivo que acompaña el mensaje", "Una foto o un mapa adjuntos refuerzan el mensaje con otro recurso."),
        ("¿Cuántos criterios usamos para revisar el correo formal?", "5", "Asunto, saludo, propósito, petición cortés y despedida con nombre."),
    ],
    task("Lee este encargo: tu curso quiere visitar un parque nacional y debes escribirle a la oficina del parque, a nombre del Sr. Díaz, para preguntar el horario de los sábados y el precio para 30 estudiantes. Escribe en una hoja un correo formal con asunto, saludo, mensaje y despedida con tu nombre. Revísalo con los cinco criterios y marca cada uno.", "Subject: Saturday visit for a school group. Dear Mr. Díaz, I am a student in 8th grade. I would like to visit the park on a Saturday with 30 students. Could you tell me the opening hours and the price? Please see the attached list of students. Best regards, Ana Rojas.", ["tiene asunto concreto y saludo formal con apellido", "el propósito aparece al comienzo con I would like to o Could you", "tiene despedida formal y nombre"], ["hoja con el correo y los cinco criterios marcados"], ["usar un saludo informal", "olvidar el asunto o el nombre"], "Lee tu correo en voz alta a una persona de tu casa y pregunta si sonaría respetuoso en una oficina."),
    "Reescribe tres órdenes directas como peticiones con Could you.",
    "Escribe un segundo correo, esta vez a un amigo, sobre el mismo tema, y subraya tres cambios de tono.",
)

# ================================================================ clase 2: descripción con pie de foto
lesson(
    OA11, 2,
    "Los textos y datos escritos en cada ejercicio, lápiz y una hoja. Una foto o un dibujo es opcional.",
    "Aprenderé a escribir una descripción de un lugar con detalles precisos y un pie de foto. Sirve para que el lector imagine el lugar y encuentre datos exactos.",
    ["Conozco there is y there are.", "Sé usar adjetivos simples como big, small y green."],
    [
        "Una descripción cuenta cómo es un lugar, una persona o un objeto. Se organiza así: título, una primera oración que dice qué es y dónde está, y luego detalles precisos (precise details): color, tamaño, número o posición. Modelo: «Title: Our school garden. Our school garden is behind the gym. It is small but very green. There are two benches under a big tree and six boxes with tomatoes».",
        "Para dar la posición usa preposiciones de lugar: behind (detrás de), next to (al lado de), under (debajo de), between (entre), in front of (frente a), around (alrededor de). Usa There is con una cosa (There is a clock) y There are con varias (There are six boxes). Un detalle es preciso cuando el lector lo puede comprobar: «six boxes» es preciso; «a nice place» no lo es.",
        "El recurso multimodal de esta clase es el pie de foto (caption): una frase corta bajo la imagen que dice qué se ve y agrega un dato, sin repetir el texto. Criterios: 1) título; 2) primera oración con qué es y dónde está; 3) al menos tres detalles precisos; 4) uso correcto de there is/there are; 5) pie de foto breve con un dato nuevo.",
    ],
    [("caption", "pie de foto: frase corta bajo una imagen"), ("detail", "detalle: dato concreto, como un color o un número"), ("behind", "detrás de"), ("next to", "al lado de"), ("under", "debajo de"), ("between", "entre"), ("in front of", "frente a"), ("around", "alrededor de"), ("There is / There are", "hay (una cosa / varias cosas)")],
    [
        ("Distinguir un detalle preciso", "¿Cuál es un detalle más preciso: «a nice garden» o «six boxes with tomatoes»?", ["Pregunta si el lector puede comprobarlo.", "Six boxes se puede contar.", "A nice garden es solo una opinión."], "six boxes with tomatoes"),
        ("Leer una posición", "Texto: «The bakery is in front of the park.» ¿Dónde está la panadería?", ["Busca la preposición: in front of.", "Significa frente a.", "La panadería está frente al parque."], "Frente al parque"),
    ],
    [
        ("Escribir «There is two trees».", "There is se usa con una sola cosa.", "Con dos árboles corresponde There are."),
        ("Escribir un pie de foto que repite el texto.", "No agrega un dato nuevo.", "Añade quién, cuándo o cuántos."),
    ],
    [
        ("Un caption es A) un texto corto bajo una imagen B) el nombre de quien escribe el correo", "A", "El pie de foto acompaña la imagen y explica qué muestra."),
        ("Completa: «There ___ two benches in the garden.» A) are B) is", "A", "Benches es plural, así que se usa there are."),
        ("¿Cuál es un detalle preciso? A) a nice place B) six boxes with tomatoes", "B", "Six boxes con tomatoes se puede contar y comprobar."),
    ],
    [
        ("Texto: «The library is next to the gym. It is big and bright. There are four long tables and twenty chairs.» ¿Cuál es la oración que dice qué es y dónde está? Copia la oración.", "The library is next to the gym.", "Nombra el lugar y su posición respecto del gimnasio."),
        ("Foto de estudiantes de 8.º regando tomates. ¿Qué pie de foto agrega información? A) A photo of plants B) Eighth graders water the tomatoes every morning", "B", "Dice quiénes lo hacen y cuándo; el otro solo repite que hay plantas."),
        ("En «three red swings», ¿qué dos detalles precisos hay? Responde en español.", "Número y color", "Three es el número y red es el color."),
    ],
    [
        ("Plano: la puerta está a la izquierda, la ventana está frente a la puerta y el escritorio está debajo de la ventana. Completa: «The desk is ___ the window.» Opciones: under / behind.", "under", "El plano dice que el escritorio está debajo de la ventana."),
        ("Ordena las palabras para decir que el jardín está detrás del gimnasio: garden / The / the / is / gym / behind", "The garden is behind the gym.", "La estructura es sujeto, verbo be, preposición y lugar."),
        ("Elige la oración correcta: A) There is five chairs. B) There are five chairs.", "B", "Five chairs es plural y pide there are."),
    ],
    [
        ("Una estudiante escribe: «My room is nice. It is very nice and I like it.» ¿Tiene tres detalles precisos? Responde sí o no.", "No", "Solo dice que es nice, una opinión que no se puede comprobar."),
        ("Texto: «There are six boxes with tomatoes.» ¿Qué pie de foto evita copiar y agrega un dato? A) There are six boxes with tomatoes. B) Tomatoes ready to eat in the school garden.", "B", "Agrega un dato nuevo, que están listos para comer, en vez de repetir el texto."),
    ],
    [
        ("Texto: «The classroom is on the second floor, between the lab and the library. It has a green door, ten tables and a large map of Chile on the back wall.» ¿Dónde está el mapa y cuántas mesas hay? Responde en español.", "En la pared del fondo; 10 mesas", "La oración final da la posición del mapa y el número de mesas."),
        ("Corrige el error: «There is two trees and a red bench in the yard.»", "There are two trees and a red bench in the yard.", "Two trees es plural y necesita there are."),
    ],
    [("Una oficina de turismo pide describir la plaza ficticia Los Olmos. Datos: fuente en el centro, cuatro bancas alrededor y un kiosco en la esquina norte. ¿Qué oración respeta los datos? A) There are four benches around the fountain. B) There are two benches next to the kiosk.", "A", "Coincide con los datos: cuatro bancas alrededor de la fuente.")],
    [
        ("¿Qué preposición significa «debajo de»?", "under", "Under indica que algo está más abajo que otra cosa."),
        ("¿Cuántos detalles precisos pide el criterio 3?", "3", "Al menos tres detalles precisos."),
        ("¿Qué debe agregar el pie de foto respecto del texto?", "Un dato nuevo", "No debe repetir el texto."),
    ],
    task("Lee este encargo: describe un lugar de tu colegio o de tu casa, por ejemplo la sala, el patio o el comedor. Escribe en una hoja un título, una primera oración con qué es y dónde está, tres detalles precisos y un pie de foto para una foto imaginaria. Revísala con los cinco criterios.", "Title: The yard. The yard is behind the school. It is wide and sunny. There are two trees, a red bench and a basketball court. Caption: Students play basketball after class.", ["tiene título y primera oración con lugar", "incluye tres detalles precisos con número, color o posición", "usa there is o there are y un pie de foto con dato nuevo"], ["hoja con la descripción y los criterios marcados"], ["usar solo adjetivos vagos como nice", "repetir el texto en el pie de foto"], "Pide a una persona de tu casa que dibuje lo que describes y compara con el lugar real."),
    "Escribe cinco oraciones con there is o there are sobre tu habitación y subraya la preposición de lugar.",
    "Describe un lugar sin decir su nombre y pide a otra persona que adivine cuál es.",
)

# ================================================================ clase 3: instrucciones con íconos
lesson(
    OA11, 3,
    "Los pasos y listas escritos en cada ejercicio, lápiz y una hoja. Para la tarea abierta basta con papel; no se necesitan materiales especiales.",
    "Aprenderé a escribir instrucciones con una lista de materiales y pasos numerados. Sirve para que otra persona pueda hacer algo sin ayuda, mirando el texto y los dibujos.",
    ["Conozco los verbos de acción como put, add y cover.", "Sé ordenar acciones con first y then."],
    [
        "Las instrucciones (instructions) explican cómo hacer algo. Tienen un título, una lista de materiales y pasos numerados. Los materiales se anuncian con dos puntos: Materials: a cup, soil, one bean, water. Cada paso comienza con un verbo en imperativo, es decir, la forma base sin sujeto: Put soil in the cup. Make a small hole. Add a little water.",
        "Cada paso tiene una sola acción, y se ordenan con palabras de secuencia: First, Next, Then, Finally. Para avisar de un peligro o de un error posible se usa Don't + verbo: Don't pour too much water. El recurso multimodal son los íconos o dibujos: junto a cada paso se pone un dibujo simple, como una gota de agua, que ayuda a entender el texto.",
        "Criterios: 1) título; 2) lista de materiales con dos puntos; 3) cada paso comienza con un verbo en imperativo; 4) pasos en orden, con una sola acción cada uno; 5) un ícono o dibujo por paso. Modelo: «How to plant a bean. Materials: a cup, soil, one bean, water. 1. Put soil in the cup. 2. Make a small hole. 3. Put the bean in the hole. 4. Cover it with soil. 5. Add a little water».",
    ],
    [("instructions", "instrucciones: pasos para hacer algo"), ("step", "paso"), ("materials", "materiales: lo que se necesita"), ("First / Next / Then / Finally", "primero / luego / después / finalmente"), ("Don't + verb", "no hagas… (aviso)"), ("icon", "ícono: dibujo simple que apoya el texto"), ("rinse", "enjuagar"), ("dry", "secar"), ("wet / rub / soap", "mojar / frotar / jabón")],
    [
        ("Contar pasos y materiales", "Texto: «Materials: a cup, soil, one bean, water. 1. Put soil in the cup. 2. Make a small hole. 3. Put the bean in the hole. 4. Cover it. 5. Add a little water.» ¿Cuántos materiales y cuántos pasos hay?", ["Los materiales van después de los dos puntos y se separan con comas.", "Hay cuatro: cup, soil, bean, water.", "Los pasos están numerados del 1 al 5."], "4 materiales y 5 pasos"),
        ("Pasar a imperativo", "Oración: «You put the bean in the hole.» Escríbela como instrucción.", ["Quita el sujeto you.", "Deja el verbo en forma base.", "Queda Put the bean in the hole."], "Put the bean in the hole."),
    ],
    [
        ("Escribir «Then you should maybe think about the bean» como un paso.", "No es una acción clara que el lector pueda hacer.", "Usa un verbo de acción: Put the bean in the hole."),
        ("Poner dos o tres acciones en un solo paso.", "El lector se pierde y no sabe en qué orden hacerlas.", "Un paso, una acción."),
    ],
    [
        ("¿Cuál empieza como una instrucción? A) Put the soil in the cup. B) You are putting soil.", "A", "Una instrucción comienza con el verbo en forma base."),
        ("¿Qué palabra de secuencia sirve para el último paso? A) Finally B) First", "A", "Finally cierra la secuencia."),
        ("«Add a little water» es A) un material B) un paso", "B", "Es una acción que se hace, no un objeto de la lista."),
    ],
    [
        ("Pasos del modelo de la clase: 1. Put soil in the cup. 2. Make a small hole. 3. Put the bean in the hole. 4. Cover it with soil. ¿Qué paso debe ir antes de «Cover it with soil»? A) Put the bean in the hole B) Add water", "A", "Primero se pone el frijol; después se cubre con tierra."),
        ("«Don't pour too much water.» ¿Qué expresa? A) Un aviso de lo que no se debe hacer B) Un material de la lista", "A", "Don't + verbo advierte de un error posible."),
        ("Pasos de lavado de manos: 1. Wet your hands. 2. Rub them with soap for 20 seconds. 3. Rinse them. 4. Dry them with a clean towel. ¿Qué haces justo después de rub?", "Rinse them", "El paso siguiente al 2 es el 3: enjuagar."),
    ],
    [
        ("Ordena los pasos para lavarse las manos y escribe las letras en orden. a) Rinse your hands. b) Dry them with a towel. c) Wet your hands. d) Rub them with soap for 20 seconds.", "c, d, a, b", "Se moja, se frota con jabón, se enjuaga y se seca."),
        ("Completa con First, Next o Finally: «___, wet your hands. ___, rub them with soap. ___, dry them.»", "First, Next, Finally", "First abre la secuencia, Next es el paso intermedio y Finally el último."),
        ("Escribe el paso en imperativo, empezando con el verbo: «You rinse the cup with water.»", "Rinse the cup with water.", "Se quita you y se deja el verbo en forma base."),
    ],
    [
        ("¿Qué paso está mejor escrito? A) Put the soil, the bean and the water and wait. B) Put soil in the cup. Then put the bean in the hole.", "B", "Separa las acciones, con una por paso, y usa secuencia."),
        ("¿Por qué falla el paso «Then you should maybe think about the bean»? A) No es una acción clara B) Tiene tres acciones a la vez", "A", "Un paso debe indicar una acción concreta que se pueda hacer."),
    ],
    [
        ("Pasos: 1. Put soil in the cup. 2. Put the bean in the hole. 3. Cover it with soil. 4. Add a little water. ¿Qué paso falta antes del paso 2? Responde con el paso en inglés.", "Make a small hole.", "El paso 2 habla del hole (hoyo), que aún no se ha hecho."),
        ("Para el paso «Add a little water» necesitas un aviso. ¿Qué aviso calza? A) Don't pour too much water. B) Pour all the water at once.", "A", "El exceso de agua puede dañar la planta; Don't advierte de ello."),
    ],
    [("Hay que elegir un afiche de instrucciones para estudiantes de 5.º básico. ¿Cuál conviene? A) Pasos numerados, cada uno con verbo y un ícono B) Un párrafo largo sin números ni dibujos", "A", "Los pasos numerados con íconos son fáciles de seguir.")],
    [
        ("¿Con qué verbo en forma base comienza cada paso?", "Con un verbo en imperativo", "Put, Add y Cover son ejemplos."),
        ("¿Qué signo se escribe después de Materials?", "Dos puntos", "Los dos puntos anuncian la lista."),
        ("¿Cuántas acciones lleva cada paso?", "Una", "Un paso, una acción."),
    ],
    task("Lee este encargo: elige una de estas dos instrucciones y escríbela en una hoja con título, lista de materiales con dos puntos y de cuatro a seis pasos numerados. Opción 1: cómo preparar tu mochila para mañana. Opción 2: cómo guardar un cuaderno en tu estante. Añade un dibujo simple junto a cada paso y un aviso con Don't. Revísala con los cinco criterios.", "How to pack your backpack. Materials: a backpack, two notebooks, a pencil case, a water bottle. 1. Check your timetable. 2. Put the notebooks in the backpack. 3. Add the pencil case. 4. Don't forget your water bottle. 5. Close the backpack.", ["tiene título y materiales con dos puntos", "cada paso comienza con un verbo en imperativo", "los pasos están en orden, con una acción cada uno y un dibujo por paso"], ["hoja con las instrucciones y los dibujos"], ["escribir pasos con sujeto, como You put", "mezclar dos acciones en un paso"], "Pide a una persona de tu casa que siga tus instrucciones sin ayuda y anota dónde se confundió."),
    "Escribe cinco verbos de acción en forma base y úsalos en pasos de una receta sin fuego ni cuchillos.",
    "Agrega a tus instrucciones dos avisos con Don't y explica por qué cada uno evita un error.",
)
