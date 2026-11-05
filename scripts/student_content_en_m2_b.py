"""Cuaderno del estudiante, 2.º medio Inglés (propuesta): EN2M OA 11, escritura guiada por modelo y criterios con recursos multimodales.

Todos los textos en inglés son originales, breves y ficticios, con pista en español. Los modelos y criterios de cada
género están escritos dentro de la propia clase. Sin audio ni material externo.
Cobertura del OA 11 (5 clases): este módulo enseña correo electrónico, descripción, cuento, diario personal (journal) y
artículo con gráfico. QUEDAN COMO VACÍO del OA las noticias, los folletos, las biografías, las instrucciones y los
resúmenes (los trabaja el módulo de 1.º medio EN1M OA 11), porque el plan solo tiene 5 clases. Los títulos de clase del
plan son genéricos (propósito, evidencia, inferencia, ensayo, producción): aquí se aplican a un género por clase.
Los datos de gráficos son «de ejemplo».
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA11 = "EN2M OA 11"


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


# ================================================================ clase 1: correo electrónico (propósito y audiencia)
lesson(
    OA11, 1,
    "Los correos y datos escritos en cada ejercicio, lápiz y una hoja. Un computador es opcional.",
    "Aprenderé a escribir un correo electrónico siguiendo un modelo y cinco criterios, y a elegir el tono según quién lo lee. Sirve para pedir algo a un profesor, a una biblioteca o a un compañero y recibir una respuesta clara.",
    ["Sé usar please y thank you.", "Conozco el presente simple y el verbo can."],
    [
        "Un correo electrónico (email) tiene un propósito (purpose, para qué escribes) y una audiencia (audience, quién lo lee). Tiene cinco partes: asunto (subject line), saludo (greeting), cuerpo (body), cierre (closing) y nombre. El asunto resume el tema en pocas palabras: Request for the gym on Friday. La primera oración del cuerpo dice el propósito: I am writing to ask if… Después van los datos: fecha, hora y lugar.",
        "El tono (register) cambia con la audiencia. Con profesores, directivos o instituciones se usa un tono formal: Dear Ms. Soto, Could you please…?, Thank you for your time, Kind regards o Best regards. Con amigos o compañeros se usa un tono informal: Hi Ben, Can you…?, Thanks!, See you! Un archivo que envías junto al correo es un adjunto (attachment): I attached the form significa «adjunté el formulario».",
        "Recurso multimodal: además del texto, el correo usa el asunto, una lista corta con los datos (Date, Time, Place) y la mención de un adjunto, para que el lector entienda de un vistazo. Criterios: 1) asunto específico de ocho palabras o menos; 2) saludo que calza con la audiencia; 3) primera oración con el propósito; 4) datos de fecha, hora y lugar; 5) petición educada, cierre y nombre.",
    ],
    [("subject line", "asunto: título corto del correo"), ("greeting", "saludo: Dear… o Hi…"), ("closing", "cierre: Kind regards, Thanks!"), ("formal", "tono formal, para profesores o instituciones"), ("informal", "tono informal, para amigos"), ("attachment", "adjunto: archivo enviado con el correo (I attached = adjunté)"), ("Could you please…?", "¿Podría… por favor? (petición formal)"), ("purpose", "propósito: para qué escribes")],
    [
        ("Encontrar el propósito", "Correo: «Subject: Request for the science fair schedule. Dear Ms. Soto, I would like to ask for the schedule of the science fair. Could you please send it before Friday? Kind regards, Tomás». ¿Qué oración dice el propósito?", ["El propósito aparece en la primera oración del cuerpo.", "Esa oración es la que sigue al saludo: «I would like to ask for the schedule of the science fair».", "La petición Could you please es el pedido de acción, no el propósito."], "I would like to ask for the schedule of the science fair."),
        ("Pasar de informal a formal", "Mensaje a un profesor: «Hey! Send me the photos from the trip, thanks!». Escríbelo como cuerpo de un correo formal para Mr. Pérez.", ["Cambia el saludo: Dear Mr. Pérez,.", "Cambia la orden por una petición con Could you please.", "Cierra con Thank you y Kind regards."], "Dear Mr. Pérez, Could you please send me the photos from the trip? Thank you. Kind regards, Lía"),
    ],
    [
        ("Escribir «Hey, teacher!» como saludo de un correo al director.", "El saludo informal no calza con la audiencia.", "Con un directivo usa Dear Mr. o Dear Ms. y el apellido."),
        ("Dejar el asunto vacío o escribir solo «Hello».", "El lector no sabe el tema antes de abrir el correo.", "Escribe un asunto específico, como Request: computer room on Monday."),
    ],
    [
        ("¿Qué parte del correo resume el tema antes de abrirlo? A) subject line B) closing", "A", "El asunto es lo primero que ve el lector."),
        ("Para escribir a la directora, Ms. Vega, ¿qué saludo es formal? A) Dear Ms. Vega, B) Hey Vega!", "A", "Dear más el título y el apellido es formal."),
        ("Un correo dice: «I attached the form.» ¿Qué significa attached? A) adjunté B) imprimí", "A", "Attachment es el archivo adjunto; I attached significa adjunté."),
    ],
    [
        ("¿Cuál es el mejor asunto para pedir la sala de computación el lunes? A) Request to use the computer room on Monday B) Computer room C) Important!!!", "A", "Dice el propósito y el día; los otros son vagos o no informan nada."),
        ("Correo: «Hi Sam, can you bring the speaker on Friday? Thanks! Ben». ¿Quién es probablemente el lector? A) un compañero B) la directora", "A", "Hi, can you y Thanks! son informales."),
        ("¿Qué oración dice el propósito de un correo? A) I am writing to ask if the library is open on Saturday. B) Thank you for your time.", "A", "La primera oración del cuerpo dice para qué escribes; Thank you for your time cierra el correo."),
    ],
    [
        ("Escribe como petición formal, empezando con Could you please: «Tell me the time of the meeting.»", "Could you please tell me the time of the meeting?", "Se cambia la orden por una pregunta educada con Could you please."),
        ("Ordena las partes del correo y escribe las letras en orden: a) body b) subject line c) closing and name d) greeting", "b, d, a, c", "El orden es asunto, saludo, cuerpo y cierre con nombre."),
        ("Un correo pide una reunión y solo dice: «Date: Wednesday. Time: 3:30 p.m.». Según el criterio 4, ¿qué dato falta? Responde con una palabra en inglés.", "place", "Faltan fecha, hora y lugar; solo falta el lugar (place)."),
    ],
    [
        ("Correo: «Subject: Request for the gym on Friday. Dear Mr. Rivas, I am writing to ask if class 2A can use the gym on Friday at 10 a.m. Could you please answer by Wednesday? See you! Mia». ¿Qué parte no calza con la audiencia? A) el saludo B) el cierre See you! C) la primera oración", "B", "See you! es informal para un director; el saludo y el propósito sí son formales."),
        ("La misma noticia, que el viaje del viernes se suspendió, va a las familias. ¿Qué inicio calza? A) Dear families, the trip on Friday is cancelled. B) Hey guys, no trip on Friday!", "A", "Las familias son una audiencia formal."),
    ],
    [
        ("Ordena las líneas para formar un correo completo y escribe las letras en orden: a) Kind regards, Pia b) Subject: Request to borrow a projector c) I am writing to ask if we can borrow a projector on Thursday at 11 a.m. d) Dear Ms. Lagos, e) Could you please let me know by Tuesday?", "b, d, c, e, a", "Va asunto, saludo, propósito, petición y cierre con nombre."),
        ("Pasa la petición formal «Could you please send me the notes?» a un amigo, con Can you.", "Can you send me the notes?", "Con un amigo se usa Can you, sin la fórmula formal."),
    ],
    [("Debes escribir a Ms. Rey, coordinadora del colegio, para saber si hay bus el sábado a la salida de curso. ¿Cuál es la mejor primera oración? A) I am writing to ask if there is a bus for the trip on Saturday. B) Hi, I have a question. C) Thank you for reading this email.", "A", "Es la única que dice el propósito concreto; las otras no.")],
    [
        ("¿Qué se escribe en el asunto de un correo?", "El tema o propósito, en pocas palabras", "Resume el correo para el lector."),
        ("Escribe en inglés un cierre formal de dos palabras.", "Kind regards (o Best regards)", "Son los cierres formales de la explicación."),
        ("¿Qué cambia cuando escribes a un amigo en lugar de al director?", "El tono: saludo, petición y cierre", "El registro depende de la audiencia."),
    ],
    task("Lee este encargo: el colegio ficticio Los Aromos organiza una charla. Datos de ejemplo: sábado, 11 a.m., biblioteca; quieres pedir a Ms. Torres, la bibliotecaria, que reserve 20 sillas. Escribe en una hoja el correo con asunto, saludo, propósito, fecha, hora y lugar, petición educada, cierre y tu nombre. Luego escribe un mensaje informal de dos líneas a un compañero con la misma idea. Revisa con los cinco criterios.", "Subject: Request for 20 chairs on Saturday. Dear Ms. Torres, I am writing to ask if you can reserve 20 chairs for a talk. Date: Saturday. Time: 11 a.m. Place: the library. Could you please confirm by Thursday? Kind regards, Álex. Informal: Hi Ben, can you help me with 20 chairs on Saturday at 11? Thanks!", ["asunto específico y saludo formal", "propósito en la primera oración y datos de fecha, hora y lugar", "petición educada, cierre y nombre; versión informal distinta"], ["hoja con los dos mensajes y los criterios marcados"], ["usar un saludo informal con la bibliotecaria", "olvidar el lugar o la hora"], "Lee tu correo a una persona de tu casa y pregunta qué entendió que debía hacer la bibliotecaria."),
    "Escribe tres asuntos de ocho palabras o menos para correos distintos sobre el colegio.",
    "Escribe el mismo pedido en tres tonos: muy formal, formal e informal, y explica en español qué palabra cambió.",
)

# ================================================================ clase 2: descripción con foto y etiquetas
lesson(
    OA11, 2,
    "Las fichas de escena escritas en cada ejercicio, lápiz y una hoja. Para la tarea abierta basta con papel y lápiz.",
    "Aprenderé a escribir una descripción de un lugar con detalles precisos, preposiciones de lugar y etiquetas para una foto. Sirve para que alguien que no conoce el lugar pueda imaginarlo y encontrar cada cosa.",
    ["Sé usar there is y there are.", "Conozco colores, números y adjetivos simples."],
    [
        "Una descripción (description) muestra cómo es un lugar, una persona o un objeto para que el lector lo imagine. Aquí la audiencia (audience) es un visitante que no conoce el lugar. Empieza con una oración general que dice qué lugar es y dónde está: Our school patio is behind the gym. Luego da detalles (details) precisos: color, tamaño, número y material.",
        "Evita palabras vagas como nice o big y usa datos que estén en la imagen: a tall green gate, three wooden benches. Para ubicar usa preposiciones de lugar (prepositions of place): next to (junto a), behind (detrás de), in front of (frente a), between (entre), on the left (a la izquierda) y on the right (a la derecha). Un sonido u olor ayuda al lector: You can hear the fountain.",
        "Recurso multimodal: una foto con etiquetas (labels). Cada etiqueta nombra una parte y dice dónde está: Stone fountain (centre). La evidencia (evidence) manda: cada detalle del texto debe estar en la imagen o en la ficha de escena; no inventes lo que no se ve. Criterios: 1) primera oración con lugar y ubicación; 2) tres detalles precisos; 3) dos preposiciones de lugar; 4) un sonido u olor de la ficha; 5) dos etiquetas para la foto.",
    ],
    [("description", "descripción: texto que muestra cómo es algo"), ("detail", "detalle: dato preciso (color, número, material)"), ("label", "etiqueta: palabra breve junto a una parte de la foto"), ("next to", "junto a"), ("behind", "detrás de"), ("in front of", "frente a"), ("between", "entre"), ("on the left / on the right", "a la izquierda / a la derecha")],
    [
        ("Ubicar con la ficha", "Ficha: «Place: a small library. Left: a red sofa. Centre: a round wooden table with four chairs. Behind the table: tall shelves with 200 books. Sound: pages turning.» Escribe una oración que ubique el sofá.", ["Busca el sofá en la ficha: Left, a red sofa.", "Left se escribe on the left.", "Se agrega el color de la ficha."], "A red sofa is on the left."),
        ("Cambiar una palabra vaga", "Con la misma ficha de la biblioteca, mejora «The table is nice and big.» con datos de la ficha.", ["Nice y big no se pueden comprobar.", "La ficha dice round, wooden y four chairs.", "Se reemplazan por esos datos."], "The table is round and wooden, with four chairs."),
    ],
    [
        ("Escribir «The room is nice and has things».", "No da ningún dato que el lector pueda imaginar.", "Escribe colores, números y materiales: The room has two blue chairs."),
        ("Agregar a la descripción un objeto que la ficha no menciona.", "Se inventa lo que no está en la evidencia.", "Usa solo lo que está en la imagen o la ficha."),
    ],
    [
        ("«The bag is behind the chair.» ¿Dónde está la bolsa respecto de la silla? A) detrás B) frente", "A", "Behind significa detrás de."),
        ("¿Cuál es un detalle más preciso? A) a nice bench B) a green wooden bench", "B", "Green wooden da color y material; nice no se puede comprobar."),
        ("Completa con una de estas palabras (between, behind o next to): «The lamp is ___ the sofa and the window.»", "between", "Between significa entre dos cosas."),
    ],
    [
        ("Ficha: «Place: school patio. Left: a blue basketball hoop. Centre: a stone fountain. Right: two orange benches. Behind the fountain: three tall trees.» ¿Qué oración coincide con la ficha? A) The benches are on the right. B) The trees are in front of the fountain. C) The hoop is on the right.", "A", "B y C invierten la ubicación; los bancos sí están a la derecha."),
        ("¿Cuál es la mejor primera oración de una descripción? A) It is a place. B) Our patio is behind the gym and has a stone fountain. C) I like the patio a lot.", "B", "Dice qué lugar es y dónde está; las otras no."),
        ("Etiqueta de una foto: «Stone fountain (centre)». ¿Qué dos datos da? Responde en español.", "La parte (fuente de piedra) y su lugar (en el centro)", "La etiqueta nombra la parte y la ubica."),
    ],
    [
        ("Ficha: «Centre: a long counter. Behind the counter: an oven.» Completa: «The oven is ___ the counter.»", "behind", "La ficha dice que el horno está detrás del mostrador."),
        ("Ficha: «Beach hut: a yellow door, two blue chairs, one striped umbrella.» Mejora «There are some nice chairs.» con un dato preciso de la ficha.", "There are two blue chairs.", "Se cambia some nice por el número y el color de la ficha."),
        ("Texto: «The bench is next to the lamp. The lamp is behind the bin, and the bin is between two trees.» ¿Cuántas preposiciones de lugar de la lista (next to, behind, between) hay?", "3", "Aparecen next to, behind y between, una vez cada una."),
    ],
    [
        ("Ficha: «Right: two orange benches.» Texto: «On the right there are three orange benches.» ¿Qué falla? A) el número no coincide con la ficha B) falta una preposición C) falta una etiqueta", "A", "La ficha dice two y el texto dice three; el resto está bien."),
        ("Dos textos sobre un mercado. X: «The market is nice and has many things.» Y: «The market has 12 stalls; red tomatoes are next to green peppers.» ¿Cuál cumple mejor el criterio 2? A) Y, porque da números, colores y ubicación B) X, porque es más corto", "A", "El criterio pide detalles precisos y comprobables."),
    ],
    [
        ("Ficha: «Place: computer room next to the library. Left: eight grey computers. Centre: a big white table. Right: a printer. Sound: the air conditioner hums.» Borrador: «The computer room is next to the library. On the left there are eight grey computers. The printer is behind the table.» ¿Qué dato contradice la ficha? A) next to the library B) la posición de la impresora C) la cantidad de computadores", "B", "La ficha ubica la impresora a la derecha, no detrás de la mesa."),
        ("Texto: «Our kitchen is in the yellow house on Mar Street. It has a long wooden table and four chairs. The sink is next to the fridge. You can smell fresh bread.» Criterios: 1) primera oración con lugar y ubicación; 2) tres detalles precisos; 3) dos preposiciones de la lista (next to, behind, in front of, between, on the left, on the right); 4) un sonido u olor. ¿Cuántos criterios cumple?", "3", "Cumple 1, 2 y 4; solo usa next to, así que el criterio 3 falla."),
    ],
    [("El club de fotografía publica la foto de una biblioteca con esta ficha: «Left: three round tables. Right: a green sofa. Sound: low voices.» ¿Qué etiqueta de la foto es correcta? A) Green sofa (on the right) B) Round tables (on the right) C) Green sofa (on the left)", "A", "La ficha pone el sofá verde a la derecha y las mesas a la izquierda.")],
    [
        ("¿Dónde debe estar cada detalle de una descripción?", "En la imagen o en la ficha", "La evidencia manda: no se inventa lo que no se ve."),
        ("¿Cuál es una preposición de lugar? A) between B) because", "A", "Because es un conector de causa; between ubica."),
        ("¿Qué palabras son mejores: vagas o precisas?", "Precisas, con color, número o material", "Permiten imaginar el lugar."),
    ],
    task("Lee este encargo: escribe una descripción de entre cinco y siete oraciones del siguiente lugar y dos etiquetas para su foto. Ficha de ejemplo: «Place: school canteen near the main gate. Left: four long grey tables. Centre: a counter with a blue sign. Right: a mural of ten colorful fish. Sound: spoons and low voices.» Revisa con los cinco criterios y marca cada uno.", "The school canteen is near the main gate. On the left there are four long grey tables. The counter with a blue sign is in the centre. On the right there is a mural of ten colorful fish. You can hear spoons and low voices. Labels: Grey tables (left); Fish mural (right).", ["primera oración con lugar y ubicación", "tres detalles precisos y dos preposiciones de lugar", "un sonido de la ficha y dos etiquetas con la parte y su lugar"], ["hoja con la descripción, las etiquetas y los criterios marcados"], ["usar nice o big sin datos", "inventar objetos que no están en la ficha"], "Pide a una persona de tu casa que dibuje lo que entiende de tu texto y compara con la ficha."),
    "Escribe cinco frases de lugar con next to, behind, between, on the left y on the right sobre un objeto de tu pieza.",
    "Describe el mismo lugar desde otro punto de vista, por ejemplo desde la puerta de entrada, y cambia las preposiciones.",
)

# ================================================================ clase 3: cuento breve con viñetas
lesson(
    OA11, 3,
    "Los textos escritos en cada ejercicio, lápiz y una hoja. Para la tarea abierta basta con papel y lápiz.",
    "Aprenderé a escribir un cuento breve con inicio, problema y final, y a mostrar lo que sienten los personajes con acciones. Sirve para contar una historia a lectores que deben deducir lo que no está dicho.",
    ["Sé usar el pasado simple de verbos regulares e irregulares comunes.", "Conozco palabras como then y after."],
    [
        "Un cuento breve (short story) cuenta hechos con personajes, lugar y un problema. Se escribe en pasado simple y tiene cuatro partes: inicio con el escenario (setting) y el personaje, problema (problem), clímax (el momento más tenso) y final (resolution, cómo se resuelve el problema). Las palabras de tiempo ordenan los hechos: one day, suddenly, after that, in the end.",
        "Los sentimientos se muestran con acciones, y no solo se nombran: Her hands shook sugiere que Ana estaba nerviosa sin decir nervous. Eso es significado implícito (unstated meaning). El lector hace una inferencia (inference): usa pistas del texto para deducir lo que el cuento no dice.",
        "Recurso multimodal: un cómic corto. Cada viñeta (panel) lleva un dibujo y un pie de texto de una o dos oraciones; el diálogo va en un globo (speech balloon) entre comillas. El texto no repite el dibujo: agrega lo que no se ve. Criterios: 1) inicio con personaje y lugar; 2) un problema; 3) verbos en pasado simple; 4) dos palabras de tiempo; 5) un sentimiento mostrado con una acción; 6) un final que resuelve el problema.",
    ],
    [("setting", "escenario: lugar y momento del cuento"), ("problem", "problema: lo que complica la historia"), ("resolution", "final: cómo se resuelve el problema"), ("suddenly", "de pronto"), ("panel", "viñeta: cuadro de un cómic"), ("speech balloon", "globo de diálogo"), ("infer", "inferir: deducir a partir de pistas"), ("unstated meaning", "significado implícito: lo que no se dice pero se entiende")],
    [
        ("Inferir un sentimiento", "Texto: «One day, Lía lost her key. She looked in her bag, and her hands shook. Suddenly, her brother knocked on the door with the key in his hand.» ¿Qué pista muestra que Lía estaba nerviosa?", ["Busca una acción del cuerpo, no un adjetivo.", "La acción es her hands shook.", "El texto no dice nervous: se infiere."], "Her hands shook."),
        ("Mostrar en lugar de decir", "Cambia «Tom was angry.» por una oración que muestre el enojo con acciones.", ["Piensa en lo que hace una persona enojada.", "Elige acciones que se vean.", "Usa el pasado simple."], "Tom closed the book hard and did not look at anyone."),
    ],
    [
        ("Escribir «He is open the door» en lugar de «He opened the door».", "Se mezcla el presente con la forma del verbo y se pierde el pasado.", "Todo el cuento va en pasado simple: opened."),
        ("Escribir solo «She was sad» en cada sentimiento.", "El lector no tiene pistas para inferir.", "Muestra una acción: She sat alone and looked at the floor."),
    ],
    [
        ("¿Qué palabra anuncia un hecho inesperado? A) suddenly B) in the end", "A", "Suddenly significa de pronto; in the end cierra la historia."),
        ("Completa en pasado simple: «Yesterday Eli ___ to the bus stop.» (run)", "ran", "Run es irregular: su pasado es ran."),
        ("«Finally, the team found the missing ball and played again.» ¿Qué parte del cuento es? A) el final B) el escenario", "A", "Resuelve el problema de la pelota perdida."),
    ],
    [
        ("Texto: «Marta's best friend moved to another city on Monday. On Tuesday, Marta stared at the empty seat and did not touch her lunch.» ¿Qué sentimiento sugiere? A) sad B) proud C) surprised", "A", "El asiento vacío y la comida sin tocar son pistas de tristeza."),
        ("¿Qué oración muestra un sentimiento con una acción? A) Leo was scared. B) Leo held the rail and did not look down.", "B", "Describe lo que hace; la otra solo nombra el sentimiento."),
        ("Texto: «One morning, the school bus did not arrive. Aldo and Camila waited for twenty minutes. Then they called the school and a van came.» ¿Cuál es el problema? A) the bus did not arrive B) they called the school C) a van came", "A", "Las otras dos oraciones son pasos para resolver el problema."),
    ],
    [
        ("Completa en pasado simple: «Yesterday, Pia (find) a purse and (give) it to the teacher.» Responde con los dos verbos.", "found, gave", "Find y give son irregulares: found y gave."),
        ("Une cada pista con el sentimiento que sugiere: a) Her hands shook. b) He smiled and ran to the door. c) She sat alone and looked at the floor. Sentimientos: 1) happy 2) nervous 3) lonely", "a-2, b-1, c-3", "Las manos que tiemblan indican nervios; sonreír y correr, alegría; mirar al piso, soledad."),
        ("Completa con one day, suddenly o in the end, una vez cada una y en orden: «___, Rosa found a map. ___, the wind took it. ___, she drew a new one.»", "One day, Suddenly, In the end", "Abren la historia, marcan el problema y cierran con la solución."),
    ],
    [
        ("Dibujo: un niño con paraguas bajo la lluvia. Pie 1: «A boy has an umbrella in the rain.» Pie 2: «The boy walked slowly because the test results were in his bag.» ¿Cuál agrega lo que el dibujo no muestra? A) el pie 1 B) el pie 2", "B", "El pie 2 suma la razón; el pie 1 solo repite lo dibujado."),
        ("Borrador: «One day, Iván lost his phone. He looked in his bag and under the bed. Suddenly, his sister called the number and the phone rang in the kitchen.» ¿Qué criterio no cumple? A) un sentimiento mostrado con una acción B) un problema C) verbos en pasado simple", "A", "No hay ninguna acción que muestre cómo se siente Iván."),
    ],
    [
        ("Ordena el cuento y escribe las letras en orden: a) In the end, Ema's team fixed the net and played. b) One Saturday, Ema's team arrived at the court. c) Suddenly, they saw that the net was broken. d) After that, they looked for a tool in the storage room.", "b, c, d, a", "Las palabras de tiempo marcan inicio, problema, intento y final."),
        ("Cuento: «One day, Rita and Ben walked to the bridge in the park. Suddenly, the wind took Rita's hat into the river. Rita's eyes filled with tears. Then Ben looked at the river and said nothing. The end.» Con los seis criterios de la clase, ¿cuántos cumple?", "5", "Falla el final, porque el problema del sombrero no se resuelve."),
    ],
    [("El club de cómics recibe una viñeta: una niña frente a una mesa con una torta quemada. ¿Qué pie de texto agrega algo que el dibujo no muestra y está en pasado? A) A girl is looking at a cake. B) Sofía smelled smoke and ran to the kitchen, but it was too late. C) Cakes are made with eggs.", "B", "Cuenta lo que pasó antes, en pasado simple; las otras repiten el dibujo o no son parte del cuento.")],
    [
        ("¿En qué tiempo verbal va un cuento breve?", "Pasado simple", "Cuenta hechos que ya ocurrieron."),
        ("¿Qué es el significado implícito?", "Lo que el texto no dice pero se deduce de pistas", "El lector lo infiere de las acciones."),
        ("¿Qué parte del cuento es el clímax?", "El momento más tenso", "Es el punto de mayor tensión antes del final."),
    ],
    task("Lee este encargo: escribe un cuento de cuatro viñetas, cada una con un pie de texto de una o dos oraciones y la descripción del dibujo entre corchetes. Elige un personaje y un problema de esta lista de ejemplo: un paraguas roto antes de una prueba; una bicicleta que se pincha cerca del colegio; un trabajo grupal que se pierde en el computador. Muestra un sentimiento con una acción y resuelve el problema al final. Revisa con los seis criterios.", "Panel 1 [Nina at the bus stop with a broken umbrella]: One rainy morning, Nina stood at the bus stop. Her umbrella was broken. Panel 2 [Nina checks her watch]: Suddenly, she bit her lip and looked at the clock. Panel 3 [A neighbor holds a big umbrella]: After that, a neighbor walked with her to school. Panel 4 [Nina at the door, dry]: In the end, she arrived on time and smiled.", ["inicio con personaje y lugar, y un problema claro", "pasado simple y dos palabras de tiempo", "un sentimiento mostrado con una acción y un final que resuelve"], ["hoja con cuatro viñetas, pies de texto y los criterios marcados"], ["nombrar el sentimiento sin acción", "terminar sin resolver el problema"], "Lee tu cuento sin las descripciones de los dibujos a una persona de tu casa y pregunta cómo cree que se sentía el personaje."),
    "Escribe cinco oraciones que muestren con una acción estos sentimientos: nervioso, contento, cansado, enojado y orgulloso.",
    "Reescribe tu cuento con otro final y explica en español qué pistas cambiaron.",
)

# ================================================================ clase 4: diario personal (journal)
lesson(
    OA11, 4,
    "Los textos escritos en cada ejercicio, lápiz y una hoja. Para la tarea abierta basta con papel y lápiz.",
    "Aprenderé a escribir una entrada de diario personal (journal) con fecha, hechos, sentimientos con because y una reflexión, y a sumar un ícono de ánimo. Sirve para entender mejor una experiencia y decidir qué harás la próxima vez.",
    ["Sé usar el pasado simple y I felt.", "Conozco because y will."],
    [
        "El diario personal (journal) es un texto que escribes sobre una experiencia. Su audiencia (audience) normalmente eres tú, por eso se escribe en primera persona (I), con tono informal y frases cortas. Lleva cuatro partes: la fecha, lo que pasó en pasado simple con dos detalles, cómo te sentiste con because (I felt nervous because…) y una reflexión (reflection): I learned that… o Next time I will…",
        "El recurso multimodal es un ícono de ánimo (mood): una escala de 1 a 5 en la que 1 es un día muy malo y 5 un día muy bueno, o un dibujo breve que acompaña el texto. También puedes hacer una línea de tiempo del día con la hora y el ánimo en cada momento. El propósito (purpose) del diario es comprender tu experiencia, no impresionar a nadie.",
        "Cuidado con las otras personas: no escribas datos privados de compañeros ni de tu familia. Si una entrada habla de algo que te preocupa mucho durante varios días, cuéntaselo a una persona adulta de confianza. Criterios: 1) fecha y primera persona; 2) hechos en pasado simple con dos detalles; 3) un sentimiento con because; 4) una reflexión; 5) ícono de ánimo o dibujo descrito.",
    ],
    [("journal", "diario personal"), ("entry", "entrada: texto de un día del diario"), ("mood", "ánimo: cómo te sientes (escala de 1 a 5)"), ("reflection", "reflexión: lo que aprendes de lo ocurrido"), ("I felt… because…", "me sentí… porque…"), ("Next time I will…", "la próxima vez voy a…"), ("I learned that…", "aprendí que…"), ("first person", "primera persona: escribir con I")],
    [
        ("Encontrar sentimiento y razón", "Entrada de ejemplo: «Tuesday, 5 May (example). Today I joined the school radio club. I read a news item in front of ten people. I felt nervous because my voice was shaking, but I also felt proud. Next time I will breathe slowly before I start. Mood: 3 out of 5.» ¿Qué oración tiene sentimiento con because?", ["Busca I felt.", "Debe tener because.", "La oración es la de nervous."], "I felt nervous because my voice was shaking."),
        ("Convertir notas en entrada", "Notas: «soccer practice; lost 2-1; sad; need to defend more». Escribe una entrada breve de tres oraciones con hecho, sentimiento con because y reflexión.", ["Primero el hecho en pasado.", "Luego I felt + sentimiento + because.", "Termina con Next time I will."], "Today we lost 2-1 at soccer practice. I felt sad because we did not defend well. Next time I will help the defenders more."),
    ],
    [
        ("Escribir una entrada solo con hechos: «I did homework. I ate. I slept.»", "No hay sentimiento ni reflexión, y el diario sirve para comprender la experiencia.", "Agrega I felt… because… y una reflexión."),
        ("Escribir el diario como si fuera un informe para un público: «Dear readers, welcome to my report.»", "El diario es para ti, no para un público formal.", "Usa primera persona e informal: Today I felt tired after practice."),
    ],
    [
        ("¿Para quién se escribe normalmente un diario personal? A) para uno mismo B) para los lectores de un periódico", "A", "El journal es privado y personal."),
        ("Completa con el pasado simple: «Today I ___ to a concert.» (go)", "went", "Go es irregular: su pasado es went."),
        ("¿Qué oración es una reflexión? A) I learned that I need to start earlier. B) I went to the gym at 5 p.m.", "A", "I learned that expresa lo que aprendes; la otra es solo un hecho."),
    ],
    [
        ("¿Qué oración cumple el criterio 3? A) I felt calm because the exam was shorter than I expected. B) I felt calm at school.", "A", "Lleva un sentimiento y su razón con because."),
        ("Escala de ánimo: 1 = día muy malo, 5 = día muy bueno. Entrada: «Today I lost my bus pass and walked home in the rain.» ¿Qué ánimo calza mejor? A) 2 out of 5 B) 5 out of 5", "A", "Perder el pase y mojarse es un día malo, no el mejor."),
        ("¿Qué oración no es adecuada para un diario personal? A) Dear readers, welcome to my official report. B) Today I felt tired after practice.", "A", "Se dirige a un público; el diario habla en primera persona de tu experiencia."),
    ],
    [
        ("Notas: «felt proud; finished my project». Escribe la oración con I felt y because.", "I felt proud because I finished my project.", "Une el sentimiento y la razón con because."),
        ("Notas: «arrived late because the bus was slow; plan: leave home ten minutes earlier». Escribe la reflexión con Next time I will.", "Next time I will leave home ten minutes earlier.", "La reflexión dice qué harás la próxima vez."),
        ("Ordena las líneas de una entrada y escribe las letras en orden: a) Next time I will check the date. b) Today I missed the deadline for the form. c) I felt worried because the form was important. d) Wednesday, 8 October (example).", "d, b, c, a", "Primero la fecha, luego el hecho, el sentimiento y la reflexión."),
    ],
    [
        ("Entrada: «Sunday. I did my homework. I played. I ate. I slept.» ¿Qué le falta? A) un sentimiento con because y una reflexión B) la primera persona", "A", "Está en primera persona, pero solo lista hechos."),
        ("¿Qué entrada protege mejor la privacidad de otra persona? A) Anota el nombre completo de un compañero y su problema personal. B) «A classmate seemed worried, and I felt concerned. Next time I will ask if everything is OK.»", "B", "No da datos privados y se centra en lo que siente quien escribe."),
    ],
    [
        ("Entrada: «Friday, 14 June (example). Today I took part in a science fair. I explained my project to eight visitors. I felt happy. Next time I will practice more. Mood: 4 out of 5.» Con los cinco criterios, ¿cuántos cumple?", "4", "Falla el criterio 3, porque I felt happy no lleva because."),
        ("Línea de tiempo de ejemplo con ánimo del 1 al 5: 10:00, ánimo 4; 12:00, ánimo 2; 16:00, ánimo 5. ¿A qué hora fue más bajo el ánimo?", "12:00", "El número más bajo de la escala es el 2."),
    ],
    [("Raúl, un personaje ficticio, escribe en su diario durante varios días que se siente muy triste y sin ganas. ¿Qué es lo más adecuado además de escribir? A) contárselo a una persona adulta de confianza B) dejar de escribir y no decir nada", "A", "Escribir ayuda a ordenar ideas, pero un adulto de confianza puede acompañarlo.")],
    [
        ("¿Qué dos partes deben aparecer después del hecho en una entrada de diario?", "Un sentimiento con because y una reflexión", "Son los criterios 3 y 4."),
        ("¿Qué significa 1 en una escala de ánimo de 1 a 5?", "Un día muy malo", "El 5 es un día muy bueno."),
        ("Escribe en inglés cómo empieza una reflexión sobre el futuro.", "Next time I will", "Anuncia lo que harás la próxima vez."),
    ],
    task("Lee este encargo: escribe una entrada de diario de cuatro a seis oraciones sobre una de estas experiencias de ejemplo: una prueba que salió mejor de lo esperado; un viaje en bus con retraso; una práctica deportiva. Incluye fecha de ejemplo, dos detalles, un sentimiento con because, una reflexión e ícono de ánimo del 1 al 5. No incluyas datos privados de otras personas. Revisa con los cinco criterios.", "Thursday, 12 June (example). Today the bus arrived twenty minutes late. I waited at the stop with my umbrella. I felt annoyed because I missed the first class. I learned that I should check the schedule. Next time I will leave earlier. Mood: 2 out of 5.", ["fecha y primera persona", "hechos con dos detalles y un sentimiento con because", "una reflexión y un ícono de ánimo"], ["hoja con la entrada y los criterios marcados"], ["listar solo hechos", "escribir datos privados de otras personas"], "Relee tu entrada al día siguiente y anota si el sentimiento y la reflexión siguen siendo verdaderos."),
    "Escribe cuatro oraciones con I felt y because sobre cuatro momentos distintos de un día de ejemplo.",
    "Escribe dos reflexiones distintas, una con I learned that y otra con Next time I will, para la misma experiencia.",
)

# ================================================================ clase 5: artículo con gráfico
lesson(
    OA11, 5,
    "Los datos y textos escritos en cada ejercicio, lápiz y una hoja. Un computador es opcional.",
    "Aprenderé a escribir un artículo breve sobre un tema de interés global usando un gráfico con título, etiquetas y fuente. Sirve para informar a lectores del sitio del colegio con datos que puedan comprobar.",
    ["Sé leer una tabla o un gráfico de barras.", "Conozco porcentajes simples."],
    [
        "Un artículo (article) informa sobre un tema a una audiencia (audience) y se apoya en datos. Tiene cuatro partes: titular (headline), introducción (introduction) con la idea principal, desarrollo (body) con datos y conclusión (conclusion) con una recomendación. Un tema de interés global es uno que afecta a personas de muchos países, como el transporte, el uso de la tecnología o la lectura.",
        "El recurso multimodal es un gráfico (chart). Debe tener un título que diga qué muestra, etiquetas (labels) en cada barra y una fuente (source): Source: class survey (example data). Rotula como «de ejemplo» los datos que no son reales. En el texto, cita al menos dos datos del gráfico sin cambiarlos. Para dar un porcentaje, divide la parte por el total y multiplica por 100: 10 de 50 es 20 %.",
        "El tono es neutro y los datos mandan: usa The largest group… o Only… en vez de opiniones sin respaldo. La conclusión propone una acción: Schools should… Criterios: 1) titular en presente simple; 2) introducción con la idea principal; 3) dos datos del gráfico citados correctamente; 4) conclusión con una recomendación; 5) gráfico con título, etiquetas y fuente.",
    ],
    [("article", "artículo: texto que informa sobre un tema con datos"), ("headline", "titular"), ("introduction", "introducción: presenta la idea principal"), ("conclusion", "conclusión: cierra con una recomendación"), ("chart", "gráfico"), ("source", "fuente: de dónde vienen los datos"), ("percentage", "porcentaje: parte ÷ total × 100"), ("example data", "datos de ejemplo, no reales")],
    [
        ("Citar un dato del gráfico", "Gráfico (datos de ejemplo): «Library cards in a class of 30 students: yes, 21; no, 9.» Escribe una oración de introducción con el total y el dato principal.", ["El total es 30.", "El dato principal es 21 estudiantes con carnet.", "Se escribe en presente simple."], "In our class of 30 students, 21 have a library card."),
        ("Escribir titular y conclusión", "Con el mismo gráfico, escribe un titular y una conclusión con una recomendación.", ["El titular es corto y está en presente simple.", "La conclusión usa Schools should.", "La recomendación sale de que 9 estudiantes no tienen carnet."], "Headline: Most students have library cards. Conclusion: Schools should help every student to get a card."),
    ],
    [
        ("Escribir un titular en pasado, como «Students had library cards».", "Los titulares de este género usan el presente simple.", "Escribe Students have library cards."),
        ("Citar un dato que no está en el gráfico para hacerlo más atractivo.", "Los datos del artículo deben poder comprobarse en el gráfico.", "Usa solo cifras del gráfico y la fuente."),
    ],
    [
        ("¿Qué parte del artículo presenta la idea principal? A) la introducción B) la conclusión", "A", "La introducción abre el artículo con la idea principal."),
        ("¿Qué título de gráfico es mejor? A) Example data: how 40 students travel to school B) Chart", "A", "Dice qué muestra y avisa que son datos de ejemplo."),
        ("«Source: class survey (example data)» dice A) de dónde vienen los datos B) quién escribió el titular", "A", "Una fuente indica el origen de los datos."),
    ],
    [
        ("Gráfico (datos de ejemplo): «How 40 students travel to school: walk, 16; bus, 14; bike, 6; car, 4.» ¿Qué oración es correcta? A) The largest group walks to school. B) Half of the students take the bus. C) Only 4 students walk.", "A", "Caminar es el grupo mayor con 16; 14 de 40 no es la mitad y los que caminan no son solo 4."),
        ("Con el mismo gráfico del transporte, ¿qué titular lo resume bien? A) Walking is the most common way to get to school B) Cars are the most common way to get to school", "A", "Caminar tiene el valor más alto; el auto, el más bajo."),
        arith("Gráfico de transporte de 40 estudiantes: bike, 6; car, 4. ¿Cuántos estudiantes llegan en bicicleta o en auto?", "6+4", "Se suman los dos grupos del gráfico."),
    ],
    [
        arith("En el gráfico del transporte caminan 16 de 40 estudiantes. ¿Qué porcentaje es? Usa parte ÷ total × 100.", "16*100//40", "Se divide la parte por el total y se multiplica por 100.", " %"),
        ("Ordena las partes de un artículo y escribe las letras en orden: a) conclusion b) headline c) body with data d) introduction", "b, d, c, a", "El orden es titular, introducción, desarrollo y conclusión."),
        ("Completa con but o because: «Sixteen students walk, ___ only four come by car.»", "but", "Expresa un contraste entre dos cantidades del gráfico."),
    ],
    [
        ("Borrador: «Half of the students ride the bus.» El gráfico dice que 14 de 40 van en bus. ¿Cuál es la corrección? A) Fourteen of the 40 students ride the bus. B) Fourteen students walk.", "A", "Debe citar el dato exacto; 14 de 40 no es la mitad."),
        ("¿Qué pie del gráfico es mejor? A) Source: class survey of 40 students (example data) B) Source: the internet", "A", "Dice quién produjo los datos y que son de ejemplo."),
    ],
    [
        arith("Otro curso (datos de ejemplo): 20 estudiantes, 5 van en bicicleta. ¿Qué porcentaje es?", "5*100//20", "Parte ÷ total × 100.", " %"),
        ("Borrador con datos del gráfico de transporte: «Headline: Walking leads. Intro: Walking is the most common way to get to school. Body: 16 students walk and 14 take the bus. Conclusion: That is all.» Criterios: 1 titular, 2 introducción, 3 dos datos correctos, 4 conclusión con recomendación, 5 gráfico con fuente. ¿Qué criterio falla en el texto? Responde con el número.", "4", "La conclusión no propone ninguna acción."),
    ],
    [arith("El club de lectura publica un gráfico de libros prestados en una semana (datos de ejemplo): 1.º A, 35; 1.º B, 28; 2.º A, 40; 2.º B, 22. ¿Cuántos libros se prestaron en total?", "35+28+40+22", "Se suman las cuatro barras del gráfico.")],
    [
        ("¿Qué tres elementos debe tener un gráfico?", "Título, etiquetas y fuente", "Son parte del criterio 5."),
        ("¿Cómo se calcula un porcentaje (en Inglés, 2.º medio)?", "Parte ÷ total × 100", "Así 10 de 50 es 20 %."),
        ("¿Cómo se marcan los datos inventados?", "Como datos de ejemplo", "Así el lector no los toma por reales."),
    ],
    task("Lee este encargo: escribe un artículo de cuatro párrafos breves con titular y gráfico para el sitio del colegio. Datos de ejemplo: «Libros prestados de la biblioteca por cuatro cursos en una semana: 1.º A, 12; 1.º B, 9; 2.º A, 15; 2.º B, 8». Dibuja el gráfico con título, etiquetas y fuente, cita dos datos en el desarrollo y termina con una recomendación. Revisa con los cinco criterios.", "Headline: Students borrow books every week. Intro: Four classes borrowed books for one week. Body: Class 2A borrowed 15 books, while class 2B borrowed 8. Conclusion: Schools should keep the library open longer. Chart title: Books borrowed in one week (example data). Source: library record (example data).", ["titular en presente simple e introducción con la idea principal", "dos datos citados sin cambiar y conclusión con recomendación", "gráfico con título, etiquetas y fuente que dice «de ejemplo»"], ["hoja con el artículo, el gráfico y los criterios marcados"], ["citar cifras que no están en el gráfico", "olvidar la fuente o el título del gráfico"], "Muestra el gráfico sin el texto a una persona de tu casa y pregunta qué entiende de los datos."),
    "Escribe tres titulares en presente simple para tres gráficos distintos de tu propia vida cotidiana (datos de ejemplo).",
    "Reescribe el mismo artículo para lectores más pequeños, de 5.º básico, y explica en español qué cambiaste.",
)
