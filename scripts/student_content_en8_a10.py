"""Cuaderno del estudiante, 8.º básico Inglés (propuesta), EN08 OA 10 (funciones del lenguaje en conversaciones y exposiciones).

Todos los diálogos y situaciones están escritos en cada ejercicio, con pista en español. Las cifras son de ejemplo.
Las clases del plan tienen títulos genéricos; aquí cada clase trabaja un grupo de las funciones que nombra el OA, para usarlas al hablar.
La práctica oral se hace con una persona de la casa; no hay audio.
"""
from __future__ import annotations

from student_content_en8_a import lesson, task
from student_lessons import arith

OA10 = "EN08 OA 10"
READ = "Lee: "

# ---------------------------------------------------------------- clase 1: cantidades, enumerar, identificar y describir
ZOO = "Diálogo. A: «How many people visit the zoo on weekends?» B: «About four thousand. In a whole year there are almost one million visitors.» A: «Is there enough space?» B: «Yes, but there is no parking.» (zoo = zoológico, weekends = fines de semana, holidays = feriados, space = espacio, parking = estacionamiento)"
GUESS = "Juego de adivinar. A: «Who is she?» B: «She is the woman with the long brown hair.» A: «And he?» B: «He is the man in the green jacket. They are Italian.» (hair = pelo, jacket = chaqueta, Italian = italianos)"

lesson(
    OA10, 1,
    "Los diálogos escritos en cada ejercicio, lápiz y una persona de la casa para practicar en voz alta.",
    "Aprenderé a expresar cantidades, contar y enumerar (two thousand, one million, enough, no money), y a identificar y describir personas, objetos y lugares al conversar. Sirve para dar cifras y para decir cómo es algo o quién es alguien.",
    ["Sé los números hasta el cien.", "Conozco is, are y los colores."],
    [
        "Para expresar cantidades en una conversación, se dicen las cifras completas: two thousand (2.000), four thousand (4.000), one million (1.000.000). Thousand y million no llevan -s después de un número: «four thousand people». Para contar, di los números en orden: one, two, three. Para enumerar, usa first, second, third o una lista: «apples, bananas and oranges».",
        "Enough significa suficiente: «There is enough space». No + sustantivo significa ninguno: «no money», «no time», «no parking». Para identificar y describir, usa is y are. «It's a big brown building» (es un edificio grande y café). Para personas: «She is the woman with the long brown hair», «He is the man in the green jacket» (con la ropa con que alguien va vestido se usa in; con rasgos o accesorios, with). Con nacionalidades: «They are French», «We are Chilean».",
        "Al hablar, ordena los adjetivos: tamaño + color + sustantivo (a big brown building). Si te piden una cantidad exacta, pregunta: «How many?» para contables y «How much?» para incontables (water, time, money). Responde con la cifra y la unidad: «About four thousand people». About significa aproximadamente.",
    ],
    [("thousand", "mil"), ("million", "millón"), ("enough", "suficiente"), ("no money", "nada de dinero"), ("the woman with…", "la mujer con…"), ("about", "aproximadamente")],
    [
        ("Decir una cantidad", ZOO + " ¿Cuántas personas visitan el zoológico los fines de semana?", ["Busco How many.", "B responde About four thousand.", "Es aproximadamente 4.000 personas."], "Unas 4.000 personas"),
        ("Describir a una persona", GUESS + " ¿Cómo describe B a la mujer?", ["Busco the woman with.", "B dice the woman with the long brown hair.", "Describe su pelo con with."], "The woman with the long brown hair"),
    ],
    [
        ("Decir «four thousands people».", "Se pluraliza thousand como en español.", "Después de un número, thousand no lleva -s."),
        ("Decir «a brown big building».", "Se invierte el orden de los adjetivos.", "Usa tamaño + color: a big brown building."),
    ],
    [
        # rec
        (ZOO + " ¿Qué falta en el zoológico? a) estacionamiento b) espacio", "a) estacionamiento", "B dice there is no parking."),
        (ZOO + " ¿Hay suficiente espacio? a) sí, hay suficiente b) no hay nada", "a) sí, hay suficiente", "B responde Yes."),
        (GUESS + " ¿De dónde son las dos personas? a) de Italia b) de Francia", "a) de Italia", "B dice They are Italian."),
    ],
    [
        # und
        ("¿Qué significa «no time»? a) nada de tiempo b) mucho tiempo", "a) nada de tiempo", "No + sustantivo significa ninguno."),
        (GUESS + " ¿Quién es el hombre? a) el de la chaqueta verde b) el de la chaqueta azul", "a) el de la chaqueta verde", "B dice the man in the green jacket."),
        ("¿Cómo se dice 1.000.000 en inglés? a) one million b) one thousand", "a) one million", "Million es millón."),
    ],
    [
        # app
        ("Responde a «How many students are there?» (3.000). a) There are three thousand students b) There are three thousands students", "a) There are three thousand students", "Thousand no lleva -s."),
        ("Completa: «It's a ___ building». Elige: big brown / brown big.", "big brown", "Tamaño antes que color."),
        ("Completa: «The girl ___ the long black hair is my cousin». Elige: with / in.", "with", "With se usa con un rasgo, como el pelo."),
    ],
    [
        # rea
        (ZOO + " Un compañero dice que visitan el zoológico un millón de personas cada fin de semana. ¿Qué dato lo corrige? a) about four thousand on weekends b) no parking", "a) about four thousand on weekends", "El millón es la cifra de todo el año."),
        (GUESS + " ¿Por qué se usa «in» en «the man in the green jacket»? a) porque habla de ropa puesta b) porque habla del pelo", "a) porque habla de ropa puesta", "In se usa con ropa."),
    ],
    [
        # cha
        arith("Datos de ejemplo: el zoológico recibe 4.000 visitantes un sábado y 3.000 un domingo. ¿Cuántos visitantes recibe el fin de semana?", "4000+3000", "Se suman los dos días."),
        ("Pregunta correcta para una cantidad de agua: a) How much water is there? b) How many water is there?", "a) How much water is there?", "Water es incontable y usa how much."),
    ],
    [
        # context
        ("En un aeropuerto te preguntan: «How many people are in your group?» (5). ¿Qué respondes? a) There are five of us b) There is five", "a) There are five of us", "Se usa are con una cantidad plural.")
    ],
    [
        # selfcheck
        ("¿Cómo se dice 2.000 en inglés?", "Two thousand", "Thousand no lleva -s."),
        ("¿Qué significa «enough»?", "Suficiente", "Va antes del sustantivo."),
        ("¿Cómo se describe a una mujer con pelo largo?", "The woman with the long hair", "With se usa con rasgos."),
    ],
    task("Con una persona de tu casa: ella te muestra una foto de tres personas (o las describes de un dibujo). Habla durante un minuto en inglés: di cuántas personas hay, describe a una con the woman with… o the man in… y nombra un objeto grande con color. Anota en tu hoja las tres oraciones que dijiste. Si no hay foto, usa este dibujo imaginado: tres amigos junto a un edificio.", "There are three people. The man in the blue jacket is tall. It's a big gray building.", ["dice una cantidad", "describe a una persona con with o in", "describe un objeto con tamaño y color"], ["hoja con tres oraciones", "nota de la persona"], ["invertir el orden color-tamaño", "no incluir la cantidad"], "Reconoce lo que acertó y revisa con la persona el orden de los adjetivos."),
    "Practica en voz alta las cifras two thousand, four thousand y one million, y anota cuál te cuesta más.",
    "Escribe en español la descripción de un amigo con tres rasgos y qué preposición usarías.",
)

# ---------------------------------------------------------------- clase 2: dirección y posesión al conversar
STREET = "Diálogo. A: «Where is Tomás?» B: «He walked from the supermarket to the bank. He went into the bank and came out of it at five. Now he is going to school.» (supermarket = supermercado, bank = banco, came out of = salió de, going to = yendo a)"
BAG = "Diálogo. A: «Whose bag is this?» B: «It belongs to a friend of mine. It's hers.» A: «And which is yours?» B: «The black one is mine. The red one is theirs.» (bag = bolso, belongs to = pertenece a, friend of mine = amigo mío, theirs = de ellos)"

lesson(
    OA10, 2,
    "Los diálogos escritos en cada ejercicio, lápiz y una persona de la casa para practicar.",
    "Aprenderé a expresar dirección (into, out of, from, to) y a solicitar y dar información sobre posesión (Whose…?, belongs to, mine, yours, hers, theirs, a friend of mine). Sirve para decir hacia dónde va alguien y de quién es algo.",
    ["Sé las preposiciones in, on y at.", "Conozco los adjetivos posesivos my, his y her."],
    [
        "Para expresar dirección, usa to (destino), from (origen), into (entrar) y out of (salir). «He walked from the supermarket to the bank.» «He went into the bank and came out of it.» Estas preposiciones van después de verbos de movimiento como go, walk y come. Into implica entrar a un lugar; in solo dice que estás dentro.",
        "Para preguntar por posesión, usa Whose…? «Whose bag is this?» Puedes responder con «It belongs to…» o con pronombres posesivos: mine, yours, his, hers, ours, theirs. «The black one is mine.» «A friend of mine» significa un amigo mío. Para elegir entre varios, usa Which…? «Which is yours?» Los pronombres posesivos no llevan sustantivo detrás: «It's hers», no «It's hers bag».",
        "En una conversación, responde con una frase corta y clara. Si te preguntan de quién es algo, empieza con It's… o It belongs to…. Si te preguntan hacia dónde va alguien, empieza con He is going to… o She went into…. Practica en voz alta con una persona de tu casa preguntando por objetos reales.",
    ],
    [("into", "hacia adentro de"), ("out of", "hacia afuera de"), ("from… to…", "desde… hasta/a…"), ("whose", "de quién"), ("belongs to", "pertenece a"), ("mine, yours, hers, theirs", "pronombres posesivos")],
    [
        ("Responder dónde fue alguien", STREET + " ¿Hacia dónde va Tomás ahora?", ["Busco going to.", "B dice Now he is going to school.", "Va a la escuela."], "A la escuela"),
        ("Responder de quién es algo", BAG + " ¿De quién es el bolso rojo?", ["Busco red.", "B dice The red one is theirs.", "Theirs significa de ellos."], "De ellos"),
    ],
    [
        ("Decir «It's hers bag».", "Se mezcla el pronombre con el adjetivo.", "Di It's hers o It's her bag."),
        ("Usar «in the bank» para decir que entró.", "No se usa into para el movimiento.", "Para entrar a un lugar, usa into."),
    ],
    [
        # rec
        (STREET + " ¿Desde dónde caminó Tomás? a) desde el supermercado b) desde el colegio", "a) desde el supermercado", "B dice from the supermarket."),
        (STREET + " ¿A qué hora salió del banco? a) a las cinco b) a las tres", "a) a las cinco", "B dice came out of it at five."),
        (BAG + " ¿De quién es el bolso negro? a) de B b) de A", "a) de B", "B dice The black one is mine."),
    ],
    [
        # und
        (BAG + " ¿Qué significa «a friend of mine»? a) un amigo mío b) mi amigo favorito", "a) un amigo mío", "Of mine indica pertenencia."),
        (STREET + " ¿Qué palabra usa B para decir entrar al banco? a) into b) from", "a) into", "B dice went into the bank."),
        (BAG + " ¿Qué palabra se usa para elegir entre varios? a) Which b) Whose", "a) Which", "A dice And which is yours?"),
    ],
    [
        # app
        ("Completa: «She walked ___ the library to the park». Elige: from / into.", "from", "From indica el origen."),
        ("Completa: «He came ___ the classroom and went to the yard». Elige: out of / into.", "out of", "Salió de la sala."),
        ("Completa: «This pen is not mine, it's ___» (de ella). Elige: hers / her.", "hers", "El pronombre va solo."),
    ],
    [
        # rea
        (BAG + " Un compañero dice que el bolso rojo es de B. ¿Qué dato lo corrige? a) B dice que es theirs, de otras personas b) B dice que el negro es mine", "a) B dice que es theirs, de otras personas", "Theirs significa de ellos."),
        ("¿Por qué se dice «It's mine» y no «It's my»? a) porque mine reemplaza al sustantivo b) porque es más corto", "a) porque mine reemplaza al sustantivo", "El pronombre va solo."),
    ],
    [
        # cha
        ("Haz una pregunta para saber de quién es una mochila: a) Whose backpack is this? b) Which is the time?", "a) Whose backpack is this?", "Whose pregunta por el dueño."),
        arith("Datos de ejemplo: Tomás camina 400 metros del supermercado al banco y 600 metros del banco al colegio. ¿Cuántos metros camina en total?", "400+600", "Se suman los dos tramos."),
    ],
    [
        # context
        ("En un aeropuerto, una persona pregunta «Whose suitcase is this?» y tú sabes que es de tus padres. ¿Qué respondes? a) It's ours b) It's your", "a) It's ours", "Ours es el pronombre de nosotros.")
    ],
    [
        # selfcheck
        ("¿Qué preposición usas para entrar a un lugar?", "Into", "Indica movimiento hacia adentro."),
        ("¿Qué pregunta usas para saber el dueño?", "Whose…?", "Pregunta por posesión."),
        ("¿Qué pronombre significa «de ellos»?", "Theirs", "Va sin sustantivo."),
    ],
    task("Con una persona de tu casa: ella pone tres objetos sobre la mesa (por ejemplo, un lápiz, un libro y una botella). Pregunta Whose pencil is this? y responde con mine, yours o hers/his. Luego, describe tu camino desde tu cama hasta la cocina con from, to, into u out of. Anota dos diálogos y una frase de camino.", "Whose pencil is this? It's mine. Whose book is this? It's hers. Camino: I walked from my bed to the bathroom, went into the kitchen and came out of it.", ["pregunta con Whose", "responde con un pronombre posesivo", "usa al menos dos preposiciones de dirección"], ["hoja con dos diálogos y una frase", "nota de la persona"], ["poner un sustantivo detrás de mine", "usar in para entrar"], "Reconoce lo que acertó y revisa con la persona dónde usar into y out of."),
    "Describe en voz alta tu camino de la casa al colegio con from y to.",
    "Escribe en español tres objetos de tu casa y de quién son, para practicar mine, yours e hers.",
)

# ---------------------------------------------------------------- clase 3: frecuencia, grado, tiempo y acciones pasadas que continúan
JOB = "Entrevista. A: «How long have you worked here?» B: «I have worked here since 2018.» A: «Have you ever visited Rapa Nui?» B: «No, I have never visited it, but I studied photography five years ago. I have saved money to buy a camera.» (worked = trabajado, since = desde, ever = alguna vez, never = nunca, photography = fotografía, saved = ahorrado)"

lesson(
    OA10, 3,
    "La entrevista escrita en cada ejercicio, lápiz y una persona de la casa para practicar.",
    "Aprenderé a señalar frecuencia, grado y tiempo (since, ago, for, never, ever), y a describir acciones pasadas que continúan en el presente con have/has + participio. Sirve para contar experiencias y preguntar a otros por las suyas.",
    ["Sé el presente simple y el pasado simple.", "Conozco los participios be-been, see-seen y eat-eaten."],
    [
        "El presente perfecto (present perfect) se forma con have o has + participio. Une el pasado con el presente. «I have worked here since 2018» significa que empecé en 2018 y sigo trabajando. Since marca un punto de inicio (since 2018, since Monday). For marca una duración (for three days, for ten years). «I have studied for three days.»",
        "Ever (alguna vez) se usa en preguntas: «Have you ever eaten insects?». Never (nunca) se usa en respuestas: «I have never seen that program». Ago (hace) se usa con el pasado simple, no con el perfecto: «I studied French five years ago». Para frecuencia y grado: always, usually, sometimes, never; very, quite, a little. «I have saved money to buy a bike» muestra una acción que sigue en proceso.",
        "Para formar la pregunta, pon have o has antes del sujeto: «Have you ever…?». Para responder corto: «Yes, I have» o «No, I haven't». Los participios regulares terminan en -ed (worked, studied, saved) y los irregulares hay que aprenderlos: been, seen, eaten, done, written. Practica con una persona de tu casa preguntando «Have you ever…?».",
    ],
    [("since", "desde (punto de inicio)"), ("for", "durante (duración)"), ("ago", "hace (con pasado simple)"), ("ever / never", "alguna vez / nunca"), ("have worked", "he trabajado"), ("participle", "participio: worked, seen, eaten")],
    [
        ("Usar since", JOB + " ¿Desde cuándo trabaja B en ese lugar?", ["Busco since.", "B dice since 2018.", "Empezó en 2018 y sigue allí."], "Desde 2018"),
        ("Responder con ever", JOB + " A pregunta «Have you ever visited Rapa Nui?». ¿Cuál es la respuesta corta?", ["La pregunta usa Have you ever…?", "B responde No, I have never visited it.", "La respuesta corta es No, I haven't."], "No, I haven't"),
    ],
    [
        ("Decir «I have visited it five years ago».", "Se mezcla presente perfecto con ago.", "Con ago usa el pasado simple: I visited it five years ago."),
        ("Decir «I seen that program».", "Se omite el verbo auxiliar have.", "El participio necesita have: I have seen that program."),
    ],
    [
        # rec
        (JOB + " ¿Qué estudió B hace cinco años? a) fotografía b) francés", "a) fotografía", "B dice I studied photography five years ago."),
        (JOB + " ¿Qué quiere comprar B con el dinero ahorrado? a) una cámara b) una bicicleta", "a) una cámara", "B dice I have saved money to buy a camera."),
        (JOB + " ¿Ha visitado B Rapa Nui? a) nunca b) muchas veces", "a) nunca", "B dice I have never visited it."),
    ],
    [
        # und
        ("Completa: «I have worked here ___ 2018». Elige: since / for.", "since", "2018 es un punto de inicio."),
        ("Completa: «She has lived here ___ ten years». Elige: for / since.", "for", "Ten years es una duración."),
        ("¿Cuál es el participio de «eat»? a) eaten b) ate", "a) eaten", "Ate es pasado simple."),
    ],
    [
        # app
        ("Forma la pregunta: «you / ever / eaten / Have / insects». a) Have you ever eaten insects? b) You have eaten ever insects?", "a) Have you ever eaten insects?", "Have va antes del sujeto."),
        ("Completa con ago o since: «I studied French five years ___». Elige: ago / since.", "ago", "Ago va con el pasado simple."),
        ("Completa: «I have ___ that program» (nunca). Elige: never seen / seen never.", "never seen", "Never va entre have y el participio."),
    ],
    [
        # rea
        ("Alguien dice: «I live here since 2020». ¿Cuál es la forma correcta? a) I have lived here since 2020 b) I lived here since 2020", "a) I have lived here since 2020", "Since pide presente perfecto."),
        ("¿Por qué «I have studied for three days» sigue en el presente? a) porque aún estudia b) porque terminó ayer", "a) porque aún estudia", "El presente perfecto une pasado y presente."),
    ],
    [
        # cha
        arith("Datos de ejemplo: B trabaja en el lugar desde 2018. Si hoy fuera 2024, ¿cuántos años llevaría trabajando?", "2024-2018", "Se restan los años."),
        ("Responde corto a «Have you ever been to Valparaíso?» si dices que sí: a) Yes, I have b) Yes, I do", "a) Yes, I have", "Se responde con el auxiliar de la pregunta."),
    ],
    [
        # context
        ("En una entrevista de trabajo te preguntan: «How long have you studied English?» y llevas tres años. ¿Qué respondes? a) I have studied English for three years b) I studied English three years ago", "a) I have studied English for three years", "Sigue estudiando, por eso usas el perfecto y for.")
    ],
    [
        # selfcheck
        ("¿Cómo se forma el presente perfecto?", "Have o has + participio", "Une pasado y presente."),
        ("¿Para qué sirve since?", "Para marcar desde cuándo", "Indica un punto de inicio."),
        ("¿Qué palabra se usa en preguntas con «alguna vez»?", "Ever", "Have you ever…?"),
    ],
    task("Con una persona de tu casa: hazle tres preguntas en inglés con Have you ever…? (por ejemplo, Have you ever eaten sushi?, Have you ever visited the south?, Have you ever seen a volcano?). Anota en tu hoja las respuestas cortas (Yes, I have / No, I haven't) y tu propia respuesta con since o for: I have lived here for … years.", "Have you ever eaten sushi? Yes, I have. Have you ever visited the south? No, I haven't. I have lived here for ten years.", ["formula tres preguntas con Have you ever", "anota respuestas cortas correctas", "usa for o since en su oración"], ["hoja con preguntas y respuestas", "nota de la persona"], ["usar ago con el perfecto", "olvidar el participio"], "Reconoce lo que acertó y revisa con la persona la diferencia entre for y since."),
    "Escribe tres experiencias que has tenido y tres que nunca has tenido, con I have.",
    "Escribe en español qué experiencia te gustaría que alguien te preguntara con Have you ever…?",
)

# ---------------------------------------------------------------- clase 4: conectar ideas e información esencial o adicional
FILM = "Conversación. A: «Why were you late?» B: «The cinema was far, so we took the bus. We saw the film, and then we ate pizza.» A: «Is the cinema the best in town?» B: «Yes, it is. It also has big comfortable seats. I'll wait here until Monday to get the tickets.» (far = lejos, took = tomamos, saw = vimos, comfortable = cómodas, seats = asientos, tickets = entradas)"
RELATIVE = "Presentaciones. «Simon is the boy who lives next door.» «The science book, which I borrowed from the library, is very interesting.» (next door = de al lado, borrowed = pedí prestado, interesting = interesante)"

lesson(
    OA10, 4,
    "Las conversaciones escritas en cada ejercicio, lápiz y una persona de la casa para practicar.",
    "Aprenderé a conectar ideas (and then, so, until, also) y a entregar información esencial o adicional con who y which al hablar. Sirve para hablar con más fluidez y para que mis frases sean más completas.",
    ["Sé because, so y then.", "Conozco who y which como palabras de pregunta."],
    [
        "Los conectores unen ideas para que hables con fluidez. And then indica orden: «We saw the film, and then we ate pizza». So muestra un resultado: «The cinema was far, so we took the bus». Until marca el límite de una espera: «I'll wait until Monday». Also suma una idea: «It also has big seats». Elige el conector según la relación entre tus ideas: orden, resultado, límite o suma.",
        "Who y which dan información sobre un sustantivo. Who se usa con personas y which con cosas. La información esencial identifica de quién o de qué hablas y no lleva comas: «Simon is the boy who lives next door». La información adicional agrega un dato y va entre comas: «The science book, which I borrowed from the library, is very interesting». Si quitas la parte esencial, la oración deja de identificar al sustantivo.",
        "Al conversar, haz pausas en las comas: son una señal de información adicional. Practica con una persona de tu casa: di dos ideas y únelas con un conector. Luego di una frase con who y otra con which. Si no recuerdas el conector, haz dos oraciones cortas; es mejor que quedarse sin hablar.",
    ],
    [("and then", "y luego (orden)"), ("so", "así que (resultado)"), ("until", "hasta que (límite)"), ("also", "además (suma)"), ("who", "que (personas)"), ("which", "que (cosas)")],
    [
        ("Elegir el conector de resultado", FILM + " ¿Qué conector explica por qué tomaron el bus?", ["Busco la razón: el cine estaba lejos.", "La frase dice The cinema was far, so we took the bus.", "El conector es so."], "So"),
        ("Distinguir información esencial", RELATIVE + " «who lives next door», ¿es información esencial o adicional?", ["La frase identifica a Simon.", "Sin ella, no se sabe qué niño es.", "Es esencial y no lleva comas."], "Esencial"),
    ],
    [
        ("Usar which para personas.", "Se confunde who con which.", "Who para personas; which para cosas."),
        ("Poner comas en la información esencial.", "No se distingue de la adicional.", "Solo la información adicional va entre comas."),
    ],
    [
        # rec
        (FILM + " ¿Qué hicieron después de ver la película? a) comieron pizza b) tomaron el bus", "a) comieron pizza", "B dice and then we ate pizza."),
        (FILM + " ¿Hasta cuándo esperará B? a) hasta el lunes b) hasta el viernes", "a) hasta el lunes", "B dice I'll wait here until Monday."),
        (FILM + " ¿Qué conector suma la idea de los asientos cómodos? a) also b) until", "a) also", "B dice It also has big comfortable seats."),
    ],
    [
        # und
        (RELATIVE + " ¿Quién es Simon? a) el niño que vive al lado b) el profesor de ciencias", "a) el niño que vive al lado", "Dice the boy who lives next door."),
        (RELATIVE + " ¿Qué dato adicional se da del libro? a) que lo pidieron prestado de la biblioteca b) que es caro", "a) que lo pidieron prestado de la biblioteca", "Va entre comas con which."),
        (FILM + " ¿Qué dice A para preguntar por la calidad del cine? a) Is the cinema the best in town? b) Where is the bus?", "a) Is the cinema the best in town?", "Usa un superlativo."),
    ],
    [
        # app
        ("Completa con who o which: «The girl ___ sings in the choir is my sister». Elige: who / which.", "who", "The girl es una persona."),
        ("Completa con who o which: «My bike, ___ is red, is very fast». Elige: which / who.", "which", "Bike es una cosa."),
        ("Completa con el conector: «It was late, ___ we took a taxi». Elige: so / until.", "so", "Tomar un taxi es el resultado."),
    ],
    [
        # rea
        ("Una persona dice: «The boy who lives next door is Simon». Otra dice: «Simon, who lives next door, is a boy». ¿Cuál tiene la información esencial? a) la primera b) la segunda", "a) la primera", "La primera identifica a Simon con who lives next door, sin comas."),
        ("Quieres decir que esperarás a tu amigo y que su llegada marca el fin de la espera. ¿Qué conector usas? a) until b) also", "a) until", "Until marca el límite de la espera."),
    ],
    [
        # cha
        ("Une las ideas: «The man is my uncle. He works at the bank». a) The man who works at the bank is my uncle b) The man which works at the bank is my uncle", "a) The man who works at the bank is my uncle", "Who es para personas y es información esencial."),
        ("Une las ideas: «My bike is old. It still works». a) My bike, which is old, still works b) My bike, who is old, still works", "a) My bike, which is old, still works", "Which es para cosas y el dato adicional va entre comas."),
    ],
    [
        # context
        ("En una conversación quieres decir que primero fuiste al parque y después a la biblioteca. ¿Qué conector usas? a) and then b) until", "a) and then", "And then marca el orden.")
    ],
    [
        # selfcheck
        ("¿Qué palabra se usa para personas: who o which?", "Who", "Which es para cosas."),
        ("¿Qué conector marca resultado?", "So", "Presenta la consecuencia."),
        ("¿Qué información va entre comas?", "La adicional", "Agrega un dato."),
    ],
    task("Con una persona de tu casa: dile en inglés dos ideas unidas con and then, otra con so y una persona con who. Por ejemplo: I did my homework, and then I watched TV. It was cold, so I wore a jacket. My friend Ana, who lives near here, is kind. Anota tus tres oraciones y marca cuál tiene información adicional.", "I went to the market, and then I bought fruit. It was late, so I took a taxi. My teacher, who is very kind, helps me. (La información adicional es la tercera oración: va entre comas.)", ["usa and then, so y who", "las oraciones son correctas", "distingue información esencial y adicional"], ["hoja con tres oraciones", "nota de la persona"], ["usar which con una persona", "confundir esencial y adicional"], "Reconoce lo que acertó y revisa con la persona dónde van las comas."),
    "Cuenta a una persona de tu casa qué hiciste ayer usando and then, so y also.",
    "Escribe en español dos frases con conectores sobre tu día.",
)

# ---------------------------------------------------------------- clase 5: procesos y acciones con agente desconocido
FOUND = "Conversación. A: «Where is your wallet?» B: «It was lost yesterday, but it was found on the floor of the bus. The money was not taken.» A: «What happens to lost objects at school?» B: «They are kept in the office, and rooms are cleaned daily.» (wallet = billetera, lost = perdida, found = encontrada, floor = suelo, taken = sacado, kept = guardados, office = oficina)"
OILP = "Exposición. «Plastic is produced from oil. First, the oil is heated. Then it is separated into parts. Finally, the plastic is shaped into bottles.» (heated = calentado, separated = separado, parts = partes, shaped = moldeado)"

lesson(
    OA10, 5,
    "Las conversaciones escritas en cada ejercicio, lápiz y una persona de la casa para practicar.",
    "Aprenderé a describir procesos y acciones en las que el agente es desconocido o no importa, con la voz pasiva (was found, are cleaned, is produced). Sirve para explicar cómo se hace algo y para contar lo que pasó con un objeto sin decir quién lo hizo.",
    ["Sé el participio de verbos como find, clean y produce.", "Conozco is, are, was y were."],
    [
        "La voz pasiva (passive voice) usa to be + participio. En presente: «Rooms are cleaned daily», «Plastic is produced from oil». En pasado: «The money was found on the floor», «The wallet was lost yesterday». Se usa cuando quien hace la acción es desconocido o no importa. En «The money was found on the floor» no sabemos quién lo encontró y no es relevante.",
        "Para describir un proceso, la voz pasiva es muy común, porque interesan los pasos y no quién los hace: «First, the oil is heated. Then it is separated. Finally, the plastic is shaped». Para unir los pasos usa first, then y finally. Si necesitas decir quién, usa by: «The rooms are cleaned by the staff». En una conversación, la pasiva suena más formal que el activo.",
        "Al hablar, elige el tiempo correcto. Is/are + participio para lo habitual o permanente; was/were + participio para el pasado. Los participios regulares terminan en -ed (cleaned, produced, shaped), y algunos irregulares son found, lost, kept, taken. Si dudas, usa la forma activa («Someone found the money») y practica la pasiva después.",
    ],
    [("passive voice", "voz pasiva"), ("agent", "agente: quien hace la acción"), ("was / were + participle", "pasado pasivo"), ("is / are + participle", "presente pasivo"), ("by", "por (agente)"), ("process", "proceso: pasos ordenados")],
    [
        ("Reconocer el pasado pasivo", FOUND + " ¿Dónde fue encontrada la billetera?", ["Busco found.", "B dice it was found on the floor of the bus.", "Fue encontrada en el suelo del bus."], "En el suelo del bus"),
        ("Reconocer un proceso", OILP + " ¿Qué se hace primero con el petróleo?", ["Busco First.", "Dice First, the oil is heated.", "Se calienta."], "Se calienta"),
    ],
    [
        ("Decir «The money found on the floor».", "Falta el verbo to be.", "La pasiva necesita was/were + participio: was found."),
        ("Agregar siempre by + agente.", "Se cree que el agente es obligatorio.", "Se omite si es desconocido o no importa."),
    ],
    [
        # rec
        (FOUND + " ¿Dónde se guardan los objetos perdidos? a) en la oficina b) en la sala", "a) en la oficina", "B dice They are kept in the office."),
        (FOUND + " ¿Qué pasó con el dinero? a) no fue sacado b) fue perdido", "a) no fue sacado", "B dice The money was not taken."),
        (OILP + " ¿Qué se fabrica al final? a) botellas b) combustible", "a) botellas", "Finally, the plastic is shaped into bottles."),
    ],
    [
        # und
        (FOUND + " ¿Cada cuánto se limpian las salas? a) a diario b) una vez al año", "a) a diario", "B dice rooms are cleaned daily."),
        (OILP + " ¿Qué se hace después de calentar el petróleo? a) se separa en partes b) se moldea", "a) se separa en partes", "Dice Then it is separated into parts."),
        ("¿Cuál es el participio de «find»? a) found b) finded", "a) found", "Find es irregular."),
    ],
    [
        # app
        ("Completa: «The windows ___ cleaned every Monday». Elige: are / was.", "are", "Es una acción habitual en presente."),
        ("Completa: «The key ___ found yesterday». Elige: was / is.", "was", "Yesterday indica pasado."),
        ("Pasa a la voz pasiva sin agente: «Someone stole my bike last night». Elige: My bike was stolen last night / My bike stole last night.", "My bike was stolen last night", "Was + participio de steal (stolen)."),
    ],
    [
        # rea
        ("¿Por qué B no dice quién encontró el dinero? a) porque no es relevante b) porque nadie lo encontró", "a) porque no es relevante", "El agente se omite si no importa."),
        ("Un compañero dice «Rooms cleaned daily». ¿Qué falta? a) el verbo are b) el sujeto", "a) el verbo are", "La pasiva necesita to be + participio."),
    ],
    [
        # cha
        ("Escribe la oración en voz pasiva y presente: «Workers make bread every morning». Escribe la versión pasiva sin by.", "Bread is made every morning", "Is + participio de make."),
        ("Ordena el proceso: A) The plastic is shaped. B) The oil is heated. C) The oil is separated.", "B, C, A", "Primero se calienta, luego se separa y después se moldea."),
    ],
    [
        # context
        ("En el colegio dices que las flores se riegan cada día sin decir quién. ¿Qué frase usas? a) The flowers are watered every day b) The flowers water every day", "a) The flowers are watered every day", "Are + participio forma la pasiva.")
    ],
    [
        # selfcheck
        ("¿Cómo se forma la voz pasiva?", "To be + participio", "Es-are/was-were + participio."),
        ("¿Cuándo omites el agente?", "Cuando es desconocido o no importa", "El foco está en la acción."),
        ("¿Qué palabra introduce al agente si lo dices?", "By", "Se usa antes de quien hace la acción."),
    ],
    task("Con una persona de tu casa: explícale en inglés, en tres oraciones, cómo se hace algo en tu casa o colegio usando la voz pasiva, por ejemplo: First, the table is cleaned. Then the plates are put on it. Finally, the food is served. Anota tus tres oraciones. Si no tienes un tema, usa cómo se prepara una ensalada.", "First, the vegetables are washed. Then they are cut. Finally, the salad is served.", ["usa is o are + participio", "ordena los pasos con first, then y finally", "no agrega agentes innecesarios"], ["hoja con tres oraciones", "nota de la persona"], ["omitir to be", "mezclar pasado y presente"], "Reconoce lo que acertó y revisa con la persona los verbos auxiliares."),
    "Describe en voz alta tres cosas que se hacen en tu casa cada semana usando la pasiva.",
    "Escribe en español dos procesos de tu vida diaria que podrías explicar con la voz pasiva.",
)
