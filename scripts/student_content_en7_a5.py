"""Cuaderno del estudiante, 7.º básico Inglés (propuesta), EN07 OA 05 (lectura de temas cercanos, actuales e interculturales).

Todos los textos son originales y están escritos en el enunciado, con pista en español. Las funciones del lenguaje del OA se
reparten en las cinco clases: posesión y descripción, tiempo-grado-modo, causa y condición, rutinas y pasado, permiso y consejo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_en7_a import lesson

OA5 = "EN07 OA 05"

# ---------------------------------------------------------------- clase 1: posesión y descripción de objetos
LOST = "Aviso de objetos perdidos: «We found a small red backpack near the gym. It is Marta's, because her name is on the label. We also found a big green umbrella: it belongs to the students' club. Whose is the old leather wallet? Please ask at the office.» (found = encontramos, label = etiqueta, belongs to = pertenece a, whose = de quién, leather = cuero, wallet = billetera, office = oficina)"
GUITAR = "«Ben's guitar is an old wooden instrument with six strings. It has a shiny red finish and a small round hole. Ben's cousin has a new plastic guitar, but Ben says his is better. The band's drummer says: The guitar on the left is mine, and the one on the right is yours.» (strings = cuerdas, shiny = brillante, finish = acabado, hole = agujero, plastic = plástico, drummer = baterista, left = izquierda, right = derecha)"
BOX = "«The science club has a box of materials. The big blue box is ours. The small yellow box is theirs. The teachers' room has a new white shelf. It is the teachers', not the students'. This clear plastic bottle is hers, and that metal compass is his.» (materials = materiales, shelf = estante, clear = transparente, metal = metal, compass = brújula)"

lesson(
    OA5, 1,
    "Los avisos y textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer textos que muestran posesión (Marta's, the students', mine, yours, whose) y que describen objetos en detalle (tamaño, edad, color, material). Sirve para entender de quién es algo y cómo es un objeto.",
    ["Sé los colores y los tamaños en inglés.", "Conozco palabras como bag, book y guitar."],
    [
        "Para mostrar que algo pertenece a alguien, en inglés se usa 's después del nombre: Marta's backpack (la mochila de Marta). Con un plural regular que termina en -s, se agrega solo el apóstrofo: the students' club (el club de los estudiantes). Con un plural irregular, como children, se agrega 's: the children's room. Para preguntar por el dueño se usa whose: Whose is this wallet? (¿de quién es esta billetera?).",
        "Los pronombres posesivos reemplazan al sustantivo: mine (mío), yours (tuyo), his (de él), hers (de ella), ours (nuestro) y theirs (de ellos). Se usan sin sustantivo: The guitar on the left is mine. Antes del sustantivo se usan my, your, his, her, our y their: my guitar. No confundas hers con her: her bag, pero The bag is hers.",
        "Para describir un objeto en detalle, los adjetivos van antes del sustantivo y suelen seguir este orden: tamaño (size), edad (age), color (color) y material (material): a small red backpack, an old wooden instrument, a new plastic guitar. Por ejemplo, an old wooden instrument se entiende como instrumento viejo de madera. Cuando leas, subraya cada adjetivo para imaginar el objeto completo.",
    ],
    [("'s / s'", "marca de posesión: de alguien / de varios"), ("whose", "de quién"), ("mine, yours, hers", "pronombres: mío, tuyo, de ella"), ("ours, theirs", "nuestro, de ellos"), ("size, age, color, material", "tamaño, edad, color, material"), ("belongs to", "pertenece a")],
    [
        ("Posesión con 's", "Lee: «This is Sofía's notebook. These are the boys' pencils.» (boys = niños). ¿De quién es el cuaderno y de quiénes los lápices?", ["Busco las marcas de posesión: Sofía's y boys'.", "El cuaderno es de Sofía.", "Los lápices son de los niños."], "El cuaderno es de Sofía y los lápices son de los niños"),
        ("Orden de adjetivos", "Escribe en inglés «una mochila pequeña roja» usando el orden tamaño y color: a ___ ___ backpack.", ["El tamaño va primero: small.", "El color va después: red.", "Queda a small red backpack."], "a small red backpack"),
    ],
    [
        ("Escribir «the students club» sin apóstrofo.", "Se olvida la marca de posesión.", "Con plural en -s se escribe the students' club."),
        ("Usar hers antes de un sustantivo: «hers bag».", "Se confunde el pronombre con el adjetivo.", "Antes del sustantivo se usa her: her bag."),
    ],
    [
        ("Lee: " + LOST + " ¿De quién es la mochila roja? a) de Marta b) del club de estudiantes", "a) de Marta", "Dice It is Marta's."),
        ("Lee: " + GUITAR + " ¿De qué material es la guitarra de Ben? a) madera b) plástico", "a) madera", "Dice an old wooden instrument."),
        ("Lee: " + BOX + " ¿Qué caja pertenece al club de ciencias? a) la azul grande b) la amarilla pequeña", "a) la azul grande", "Dice The big blue box is ours."),
    ],
    [
        ("Lee: " + LOST + " ¿A quién pertenece el paraguas verde?", "Al club de estudiantes", "Dice it belongs to the students' club."),
        ("Lee: " + GUITAR + " ¿Cuántas cuerdas tiene la guitarra de Ben?", "6", "Dice six strings."),
        ("Lee: " + BOX + " ¿Quién usa el estante blanco nuevo? a) los profesores b) los estudiantes", "a) los profesores", "Dice It is the teachers', not the students'."),
    ],
    [
        ("Lee: " + LOST + " ¿Quién todavía no tiene dueño conocido? a) la billetera b) el paraguas", "a) la billetera", "Dice Whose is the old leather wallet?"),
        ("Lee: " + GUITAR + " ¿Qué acabado tiene la guitarra de Ben? a) rojo brillante b) azul opaco", "a) rojo brillante", "Dice a shiny red finish."),
        ("Lee: " + BOX + " Describe el material de la botella. ¿Qué dice el texto?", "De plástico transparente", "Dice this clear plastic bottle."),
    ],
    [
        ("Lee: " + GUITAR + " ¿Cuál es la guitarra nueva? a) la del primo de Ben b) la de Ben", "a) la del primo de Ben", "Dice Ben's cousin has a new plastic guitar."),
        ("Lee: " + BOX + " Una compañera dice que la brújula es de ella. ¿Qué dice el texto? a) es de él b) es de ella", "a) es de él", "Dice that metal compass is his."),
    ],
    [
        ("Ordena las palabras para describir un objeto en el orden correcto: wooden / a / table / big / brown", "a big brown wooden table", "El orden es tamaño, color y material antes del sustantivo."),
        ("Lee: " + BOX + " Completa con el pronombre: The big blue box is ___ (de nosotros). The clear plastic bottle is ___ (de ella).", "ours; hers", "Ours es de nosotros y hers es de ella."),
    ],
    [("Lee: «Look at this poster. The big white dog is Lucas's. The small black dog is Ana's. The brown one is the neighbors'.» (neighbors = vecinos). ¿De quién es el perro blanco grande? a) de Lucas b) de Ana", "a) de Lucas", "Dice The big white dog is Lucas's.")],
    [
        ("En el aviso de objetos perdidos, ¿qué significa la palabra whose?", "De quién", "Se usa para preguntar por el dueño."),
        ("¿Cómo se escribe «el club de los estudiantes»?", "the students' club", "Plural regular con apóstrofo final."),
        ("¿Qué orden siguen los adjetivos de una descripción?", "Tamaño, edad, color y material", "Es el orden usual en inglés."),
    ],
    task("Lee este aviso original: «Lost: a medium blue bag with a silver zipper. It is Pedro's, but he lost it near the library. It has an old yellow notebook, a small metal ruler and his sister's sunglasses. Please ask at the office.» (medium = mediano, zipper = cierre, ruler = regla, sunglasses = lentes de sol). Escribe: de quién es la bolsa, qué tiene dentro y cómo es cada objeto según el texto (tamaño, edad, color o material).", "La bolsa es de Pedro. Dentro hay un cuaderno amarillo viejo, una regla pequeña de metal y los lentes de sol de su hermana. La bolsa es mediana, azul y tiene cierre plateado.", ["indica el dueño de la bolsa", "enumera los tres objetos con sus rasgos", "usa el orden de los adjetivos"], ["hoja con respuestas"], ["decir que los lentes son de Pedro", "olvidar el material de la regla"], "Reconoce lo que acertó y subraya con la persona las marcas 's y los adjetivos."),
    "Relee el texto de la guitarra y subraya con rojo los adjetivos y con azul los posesivos.",
    "Escribe tres oraciones en inglés sobre objetos de tu mochila usando 's y mine.",
)

# ---------------------------------------------------------------- clase 2: tiempo, grado y modo
SPORTS = "Afiche: «Sports Week. The opening is on Monday at 9:00 in the yard. Swimming is on Tuesday. The relay race is always at the end of the week, on Friday, and it is very exciting. The prizes are on Friday at 12:30. Teams usually train quietly in the morning, and sometimes they train at night. Next week there is no school on Monday.» (opening = apertura, relay race = carrera de relevos, prizes = premios, train = entrenar, quietly = en silencio, exciting = emocionante)"
CHOIR = "«Our choir practice is on Mondays at 4:00. In December, we have a concert on the 14th at 7:00 in the town hall. Sara sings quite well, and Pedro sings a bit loudly. We always warm up before we start. We never sing without water. We practice a little every day.» (choir = coro, concert = concierto, town hall = municipalidad, quite well = bastante bien, a bit = un poco, loudly = fuerte, warm up = calentar la voz)"
FAIR = "«The science fair is next week, on Thursday, from 10:00 to 13:00. It is in December, near the end of the school year. Students speak very clearly and answer questions politely. The visitors usually arrive early. Yesterday, the winners were announced. Tomorrow we will paint the posters.» (fair = feria, clearly = con claridad, politely = con cortesía, early = temprano, winners = ganadores, announced = anunciados)"

lesson(
    OA5, 2,
    "Los afiches y textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer textos que indican el tiempo, el grado y el modo en que ocurren las acciones (on Monday, always, very, quietly) y que dan y piden información sobre el tiempo. Sirve para entender horarios, afiches y rutinas.",
    ["Sé los días de la semana y los meses.", "Conozco las horas en inglés."],
    [
        "Para decir cuándo ocurre algo se usan preposiciones. On va con los días (on Monday, on the 14th), at con las horas (at 4:00), in con los meses y las estaciones (in December, in summer), y las expresiones next week (la próxima semana), yesterday (ayer) y tomorrow (mañana) no llevan preposición. Para preguntar: When is the party? (¿cuándo es la fiesta?) y What time is it? (¿qué hora es?).",
        "Los adverbios de frecuencia (frequency adverbs) dicen cada cuánto ocurre algo: always (siempre), usually (por lo general), sometimes (a veces), never (nunca). Los adverbios de grado (degree) dicen cuánto: very (muy), quite (bastante), a bit y a little (un poco). Los adverbios de modo (manner) dicen cómo se hace algo: quietly (en silencio), clearly (con claridad), well (bien), fast (rápido). Los de modo suelen ir después del verbo: she sings well. Los de frecuencia van antes del verbo principal (she always sings) y después de to be (she is always late).",
        "Para leer, subraya los adverbios y pregúntate qué información agregan: cada cuánto, cuánto o cómo. No cambian el hecho central, pero cambian el significado. «Teams train quietly» dice cómo entrenan; «teams sometimes train at night» dice con qué frecuencia. Si tienes dudas, lee la oración sin el adverbio y luego con él.",
    ],
    [("on / at / in", "con días / con horas / con meses"), ("always, usually, sometimes, never", "siempre, por lo general, a veces, nunca"), ("very, quite, a bit", "muy, bastante, un poco"), ("quietly, clearly, well", "en silencio, con claridad, bien"), ("next week", "la próxima semana"), ("When is…?", "¿Cuándo es…?")],
    [
        ("Elegir la preposición", "Completa con on, at o in: «The meeting is ___ Tuesday ___ 3:30.»", ["Los días llevan on.", "Las horas llevan at.", "Queda on Tuesday at 3:30."], "on Tuesday at 3:30"),
        ("Clasificar un adverbio", "En «Ana speaks clearly», ¿qué dice clearly: cada cuánto, cuánto o cómo?", ["Clearly viene de clear y termina en -ly.", "Dice de qué manera habla Ana.", "Es un adverbio de modo."], "Cómo habla: adverbio de modo"),
    ],
    [
        ("Escribir «She always is late».", "Se pone el adverbio antes de to be.", "Con to be el adverbio va después: She is always late."),
        ("Usar in con los días: «in Monday».", "Se confunden las preposiciones de tiempo.", "Con los días se usa on Monday."),
    ],
    [
        ("Lee: " + SPORTS + " ¿A qué hora son los premios? a) a las 12:30 b) a las 9:00", "a) a las 12:30", "Dice The prizes are on Friday at 12:30."),
        ("Lee: " + CHOIR + " ¿Cuándo es el concierto? a) el 14 de diciembre a las 7:00 b) el lunes a las 4:00", "a) el 14 de diciembre a las 7:00", "Dice in December, concert on the 14th at 7:00."),
        ("Lee: " + FAIR + " ¿Cuándo es la feria de ciencias? a) la próxima semana, el jueves b) ayer", "a) la próxima semana, el jueves", "Dice next week, on Thursday."),
    ],
    [
        ("Lee: " + SPORTS + " ¿Qué día es la carrera de relevos?", "El viernes", "Dice on Friday."),
        ("Lee: " + CHOIR + " ¿Quién canta bastante bien?", "Sara", "Dice Sara sings quite well."),
        ("Lee: " + FAIR + " ¿Cómo responden las preguntas los estudiantes?", "Con cortesía", "Dice answer questions politely."),
    ],
    [
        ("Lee: " + SPORTS + " ¿Con qué frecuencia entrenan los equipos de noche? a) a veces b) siempre", "a) a veces", "Dice sometimes they train at night."),
        ("Lee: " + CHOIR + " ¿Qué nunca hace el coro? a) cantar sin agua b) calentar la voz", "a) cantar sin agua", "Dice We never sing without water."),
        ("Lee: " + FAIR + " ¿Cuándo llegan los visitantes? a) temprano, por lo general b) tarde, siempre", "a) temprano, por lo general", "Dice usually arrive early."),
    ],
    [
        ("Lee: " + CHOIR + " ¿Quién canta un poco fuerte? a) Pedro b) Sara", "a) Pedro", "Dice Pedro sings a bit loudly."),
        ("Lee: " + SPORTS + " ¿Qué adverbio muestra que la carrera de relevos es siempre al final de la semana? a) always b) quietly", "a) always", "Always indica que ocurre cada vez."),
    ],
    [
        ("Lee: " + SPORTS + " Si hoy es miércoles y la apertura fue el lunes, ¿cuántos días faltan para el viernes?", "2", "De miércoles a viernes hay dos días.", "5-3"),
        ("Lee: " + FAIR + " La feria dura desde las 10:00 hasta las 13:00. ¿Cuántas horas dura?", "3", "De 10 a 13 pasan tres horas.", "13-10"),
    ],
    [("Lee: «My cousin always wakes up early on Saturdays. He usually plays football at 9:00, and sometimes he reads a book in the afternoon. He never eats breakfast quickly.» (wakes up = se despierta, plays = juega, quickly = rápido). ¿Qué hace a veces en la tarde? a) lee un libro b) juega fútbol", "a) lee un libro", "Dice sometimes he reads a book in the afternoon.")],
    [
        ("¿Qué preposición va con las horas?", "at", "Se dice at 4:00."),
        ("¿Qué adverbio significa «nunca»?", "never", "Es el adverbio de frecuencia opuesto a always."),
        ("¿Qué indican los adverbios de modo?", "Cómo se hace algo", "Describen la manera de la acción."),
    ],
    task("Lee este afiche original: «Reading Club. We meet every Wednesday at 5:00 in the library. In June, we always read a poem. Students usually bring a snack. We read quietly for ten minutes, and then we talk a little. On the last day, the winner gets a book.» (snack = colación, talk = conversar, last day = último día, winner = ganador). Escribe: el día y la hora de reunión, qué siempre ocurre en junio, qué hacen en silencio y cuántos minutos.", "Se reúnen los miércoles a las 5:00. En junio siempre leen un poema. Leen en silencio diez minutos.", ["indica día y hora correctos", "usa los adverbios para responder", "anota los diez minutos"], ["hoja con respuestas"], ["decir que se reúnen los jueves", "no escribir la acción de junio"], "Reconoce lo que acertó y subraya con la persona on, at, in y los adverbios."),
    "Relee el afiche de la semana deportiva y subraya con tres colores los días, las horas y los adverbios.",
    "Escribe tu horario de una mañana usando at, on y dos adverbios de frecuencia.",
)

# ---------------------------------------------------------------- clase 3: causa, efecto y condición
ICE = "«Ice and heat. An ice cream melts if you heat it. If you leave ice in the sun, it turns into water. Water boils at one hundred degrees Celsius, so we never touch a boiling pot. Plants grow well because they receive light and water.» (melts = se derrite, heat = calentar, turns into = se convierte en, boils = hierve, degrees Celsius = grados Celsius, pot = olla, receive = reciben)"
TRAFFIC = "«Traffic rules. If the light is red, stop. If the light is green, look left and right, and then you can go. We cross at the crosswalk because it is safer. If a car comes, wait on the sidewalk.» (traffic = tráfico, crosswalk = paso de cebra, safer = más seguro, sidewalk = vereda)"
DIARY = "«Teacher's note. Our class garden has many problems. If we do not water the plants, they will die. If we use too much water, the soil will be muddy. The plants are small because they have little sun. So we will move the pots to the yard, and if it works, we will have flowers in spring.» (garden = huerto, will die = morirán, muddy = barroso, soil = tierra, pots = macetas, spring = primavera)"

lesson(
    OA5, 3,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer textos que explican causa y efecto (because, so) y que expresan condiciones con If you…, I will… (por ejemplo, If you cook, I'll help you). Sirve para entender explicaciones científicas, reglas y planes.",
    ["Sé que because significa porque.", "Conozco el verbo will en frases como I will help."],
    [
        "La causa y el efecto (cause and effect) explican por qué ocurre algo. Because (porque) introduce la causa: Plants grow well because they receive light. So (por eso, así que) introduce el efecto: Water boils at 100 degrees, so we never touch a boiling pot. Por eso, because se lee con la causa y so con el resultado.",
        "Una condición (condition) dice qué pasa si ocurre algo. Se forma con if (si): If you heat ice cream, it melts. Para hablar de algo posible en el futuro se usa if + presente, y el resultado lleva will + verbo: If you cook, I will help you (Si cocinas, te ayudaré). La contracción de I will es I'll. Si el resultado va primero, no se usa coma: I will help you if you cook.",
        "Para leer con atención, busca la palabra if y marca la condición y su resultado. Pregúntate: ¿qué debe pasar primero?, ¿qué ocurre entonces? Las reglas y las advertencias usan if con frecuencia: If the light is red, stop. Una condición no dice que ocurrirá siempre: dice que ocurrirá solo si se cumple lo que sigue a if.",
    ],
    [("because", "porque: introduce la causa"), ("so", "por eso: introduce el efecto"), ("if", "si: introduce una condición"), ("will", "futuro: ocurrirá"), ("I'll", "contracción de I will"), ("condition", "condición")],
    [
        ("Causa con because", "Lee: «The match is cancelled because it is raining.» (cancelled = suspendido, match = partido). ¿Cuál es la causa?", ["Busco la palabra because.", "Después viene it is raining.", "La lluvia es la causa."], "Que está lloviendo"),
        ("Condición con if", "Lee: «If you study, you will pass the test.» (pass = aprobar). ¿Qué pasará si se estudia?", ["La condición va después de if: study.", "El resultado lleva will.", "El resultado es aprobar la prueba."], "Se aprobará la prueba"),
    ],
    [
        ("Poner will después de if: «If you will cook, I help you».", "Se invierten los tiempos verbales.", "If + presente; el resultado lleva will."),
        ("Confundir so con because.", "No se identifica qué parte es la causa.", "Because lleva la causa; so lleva el efecto."),
    ],
    [
        ("Lee: " + ICE + " ¿Qué pasa con el hielo al sol? a) se convierte en agua b) se congela más", "a) se convierte en agua", "Dice it turns into water."),
        ("Lee: " + TRAFFIC + " ¿Qué se hace si la luz está roja? a) detenerse b) cruzar rápido", "a) detenerse", "Dice if the light is red, stop."),
        ("Lee: " + DIARY + " ¿Por qué las plantas son pequeñas? a) porque tienen poco sol b) porque tienen mucha agua", "a) porque tienen poco sol", "Dice because they have little sun."),
    ],
    [
        ("Lee: " + ICE + " ¿A cuántos grados hierve el agua según el texto?", "A 100 grados Celsius", "Dice one hundred degrees Celsius."),
        ("Lee: " + TRAFFIC + " ¿Por qué se cruza en el paso de cebra?", "Porque es más seguro", "Dice because it is safer."),
        ("Lee: " + DIARY + " ¿Qué pasa si se usa demasiada agua?", "La tierra se pone barrosa", "Dice the soil will be muddy."),
    ],
    [
        ("Lee: " + ICE + " ¿Cuál es el efecto de que el agua hierva a 100 grados? a) nunca se toca una olla hirviendo b) las plantas crecen", "a) nunca se toca una olla hirviendo", "Dice so we never touch a boiling pot."),
        ("Lee: " + TRAFFIC + " Si viene un auto, ¿qué se hace? a) esperar en la vereda b) cruzar", "a) esperar en la vereda", "Dice if a car comes, wait on the sidewalk."),
        ("Lee: " + DIARY + " ¿Qué se hará con las macetas? a) se llevarán al patio b) se regarán menos", "a) se llevarán al patio", "Dice we will move the pots to the yard."),
    ],
    [
        ("Lee: " + DIARY + " ¿Qué ocurrirá en primavera si el cambio funciona?", "Habrá flores", "Dice if it works, we will have flowers in spring."),
        ("Lee: " + ICE + " Un compañero dice que los helados se derriten si se enfrían. ¿Es correcto? Responde sí o no.", "No", "El texto dice que se derriten si se calientan."),
    ],
    [
        ("Lee: " + DIARY + " Ordena la lógica del plan. A) Mover las macetas al patio. B) Plantas pequeñas por poco sol. C) Posibles flores en primavera.", "B, A, C", "Primero el problema, luego la acción y después el resultado esperado."),
        ("Lee: " + TRAFFIC + " Escribe cuántas reglas del texto usan if.", "3", "Son la luz roja, la luz verde y el auto que se acerca."),
    ],
    [("Lee: «If you recycle paper, the school will save trees. We recycle because it helps the planet.» (recycle = reciclar, save = salvar, planet = planeta). ¿Por qué se recicla? a) porque ayuda al planeta b) porque es obligatorio", "a) porque ayuda al planeta", "Dice because it helps the planet.")],
    [
        ("En un aviso, ¿qué palabra abre una condición con resultado en will?", "if", "Se traduce como si."),
        ("¿Qué palabra introduce el efecto en «…, so we never touch…»?", "so", "So significa por eso."),
        ("¿Cómo se contrae I will?", "I'll", "Es la contracción habitual."),
    ],
    task("Lee este aviso original: «Library rule. If you borrow a book, return it in two weeks. If you lose a book, you will pay for it. Students read in silence because other students are studying. So please speak quietly.» (borrow = pedir prestado, return = devolver, lose = perder, pay = pagar). Escribe: una condición con su resultado, una causa con because y un efecto con so.", "Condición: si pierdes un libro, lo pagarás. Causa: se lee en silencio porque otros estudian. Efecto: por eso se habla en voz baja.", ["escribe una condición con resultado", "identifica una causa con because", "identifica un efecto con so"], ["hoja con respuestas"], ["invertir la causa y el efecto", "usar will después de if"], "Reconoce lo que acertó y subraya con la persona la parte de if y la parte con will."),
    "Relee las reglas de tránsito y dibuja un semáforo con la regla de cada luz.",
    "Escribe en inglés una condición con If y un resultado con will sobre tu fin de semana.",
)

# ---------------------------------------------------------------- clase 4: rutinas, pasado y acciones simultáneas
TRIP2 = "«Wednesday, 8 p.m. Today I was walking home when it started to rain. While I was running, my friend Elena was waiting at the bus stop with an umbrella. We usually take the bus at five, but today the bus was late. We talked and laughed. Last year I did not like rain, and now I do. What time does the school bus come in your town? Does it come early?» (walking = caminando, started = empezó, running = corriendo, waiting = esperando, late = atrasado, laughed = nos reímos)"
MORNING2 = "«My routine. I get up at 6:30 and have breakfast. I walk to school with my neighbor. Yesterday, I got up late, so I missed the bus. When I arrived, the class was starting. The teacher was writing on the board while the students were opening their books. Did I arrive late? Yes, I did.» (get up = levantarse, missed = perdí, was starting = estaba empezando, board = pizarra, were opening = estaban abriendo)"
PARK = "«Last Sunday, Julia was riding her bike in the park when she saw a small dog. The dog was running behind a ball. While Julia was stopping, the dog's owner was shouting its name. Does the dog live in the park? No, it doesn't. It lives in the next street. Did Julia help? Yes, she did. She gave the ball back.» (riding = andando, ball = pelota, owner = dueño, shouting = gritando, nearby = cerca, next street = calle siguiente, gave back = devolvió)"

lesson(
    OA5, 4,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer textos que hablan de rutinas y acciones presentes y pasadas, y que describen acciones que ocurren al mismo tiempo o que interrumpen a otras en el pasado (when, while). Sirve para entender diarios, relatos de la semana y preguntas con do, does y did.",
    ["Sé el presente simple (I get up) y el pasado simple (I got up).", "Conozco el verbo to be en pasado: was y were."],
    [
        "El presente simple (present simple) cuenta rutinas y datos habituales: I get up at 6:30. Para preguntar se usa do o does: What time does the bus come? Para responder: Yes, it does / No, it doesn't. El pasado simple (past simple) cuenta acciones terminadas: Yesterday, I got up late. Para preguntar se usa did: Did I arrive late? Yes, I did / No, I didn't. Después de did el verbo vuelve a su forma base.",
        "El pasado continuo (past continuous) usa was o were + verbo con -ing para describir una acción en desarrollo en el pasado: She was walking (estaba caminando). Con while se muestran dos acciones simultáneas: While I was running, Elena was waiting. Con when se muestra una acción que interrumpe a otra más larga: I was walking home when it started to rain. La acción larga va en pasado continuo y la que interrumpe, en pasado simple.",
        "Al leer, identifica qué acciones son rutinas (usually, every day), cuáles son del pasado terminado (yesterday, last year) y cuáles estaban en desarrollo. Pregúntate: ¿cuál es la acción larga? ¿Cuál la interrumpe? Así entiendes el orden de los hechos aunque el texto cambie de tiempo verbal.",
    ],
    [("present simple", "presente simple: rutinas"), ("past simple", "pasado simple: acciones terminadas"), ("past continuous", "pasado continuo: estaba haciendo"), ("while", "mientras: acciones simultáneas"), ("when", "cuando: una acción interrumpe a otra"), ("did / does", "auxiliares para preguntar en pasado / presente")],
    [
        ("Acciones simultáneas", "Lee: «While Marco was cooking, his sister was setting the table.» (setting the table = poniendo la mesa). ¿Qué ocurría al mismo tiempo?", ["La palabra while une dos acciones.", "Marco cocinaba.", "Su hermana ponía la mesa."], "Marco cocinaba y su hermana ponía la mesa"),
        ("Acción interrumpida", "Lee: «I was reading when the phone rang.» (rang = sonó). ¿Qué acción interrumpió a la otra?", ["La acción larga es was reading.", "La acción que interrumpe va en pasado simple.", "Fue el sonido del teléfono."], "El sonido del teléfono"),
    ],
    [
        ("Usar el pasado continuo para una acción terminada y breve.", "Se confunde la acción en desarrollo con la acción puntual.", "Usa el pasado simple para la acción que interrumpe."),
        ("Decir «Did she arrived?».", "Se conjuga el verbo principal después de did.", "Después de did el verbo va en forma base: Did she arrive?"),
    ],
    [
        ("Lee: " + TRIP2 + " ¿Qué hacía la persona cuando empezó a llover? a) caminaba a casa b) tomaba el bus", "a) caminaba a casa", "Dice I was walking home when it started to rain."),
        ("Lee: " + MORNING2 + " ¿Por qué perdió el bus? a) porque se levantó tarde b) porque llovía", "a) porque se levantó tarde", "Dice I got up late, so I missed the bus."),
        ("Lee: " + PARK + " ¿Qué hacía Julia cuando vio al perro? a) andaba en bicicleta b) leía un libro", "a) andaba en bicicleta", "Dice Julia was riding her bike when she saw a small dog."),
    ],
    [
        ("Lee: " + TRIP2 + " ¿Qué hacía Elena mientras la persona corría?", "Esperaba en el paradero con un paraguas", "Dice Elena was waiting at the bus stop with an umbrella."),
        ("Lee: " + MORNING2 + " ¿Qué hacía la profesora cuando llegó la persona?", "Escribía en la pizarra", "Dice The teacher was writing on the board."),
        ("Lee: " + PARK + " ¿Qué hacía el dueño del perro mientras Julia se detenía?", "Gritaba el nombre del perro", "Dice the dog's owner was shouting its name."),
    ],
    [
        ("Lee: " + TRIP2 + " ¿A qué hora toman normalmente el bus? a) a las cinco b) a las ocho", "a) a las cinco", "Dice We usually take the bus at five."),
        ("Lee: " + MORNING2 + " ¿A qué hora se levanta normalmente?", "A las 6:30", "Dice I get up at 6:30."),
        ("Lee: " + PARK + " ¿Julia ayudó al perro? a) sí, devolvió la pelota b) no", "a) sí, devolvió la pelota", "Dice Did Julia help? Yes, she did. She gave the ball back."),
    ],
    [
        ("Lee: " + PARK + " ¿El perro vive en el parque? ¿Dónde vive?", "Vive en la calle siguiente", "Dice it lives in the next street."),
        ("Lee: " + MORNING2 + " Ordena. A) Llegó con la clase empezando. B) Se levantó tarde. C) Perdió el bus.", "B, C, A", "Primero se levantó tarde, luego perdió el bus y después llegó."),
    ],
    [
        ("Una persona se levanta a las 6:30 y sale de su casa a las 8:00. ¿Cuántos minutos hay entre las dos horas?", "90", "Una hora y media son 90 minutos.", "60+30"),
        ("Lee: " + MORNING2 + " Elige el verbo correcto en la pregunta «Did she ___ late?» a) arrive b) arrived", "a) arrive", "Después de did el verbo va en forma base."),
    ],
    [("Lee: «Last Friday, Tomás was painting a poster when his brush fell. He was painting the sky while his friend was drawing the sun. Did they finish? Yes, they did.» (brush = pincel, fell = cayó, drawing = dibujando, finish = terminar). ¿Qué hacía el amigo mientras Tomás pintaba el cielo? a) dibujaba el sol b) pintaba el mar", "a) dibujaba el sol", "Dice his friend was drawing the sun.")],
    [
        ("¿Qué forma verbal usa «was walking»?", "Pasado continuo", "Se forma con was o were y -ing."),
        ("¿Qué palabra une dos acciones simultáneas?", "while", "While significa mientras y une dos acciones simultáneas."),
        ("¿Qué verbo se usa para preguntar en pasado?", "did", "Se usa antes del verbo base."),
    ],
    task("Lee este diario original: «Thursday. This morning I was making breakfast when the lights went out. While I was looking for a candle, my neighbor was knocking on the door. We usually have electricity in the morning, but today the power was off. Did the lights come back? Yes, they did, at 8:30.» (lights went out = se cortó la luz, candle = vela, knocking = golpeando, power = electricidad). Escribe: qué hacía la persona cuando se cortó la luz, qué hacía el vecino mientras tanto y a qué hora volvió la luz.", "Hacía el desayuno cuando se cortó la luz. El vecino golpeaba la puerta mientras ella buscaba una vela. La luz volvió a las 8:30.", ["distingue la acción larga y la que interrumpe", "relaciona las dos acciones simultáneas", "anota la hora exacta"], ["hoja con respuestas"], ["decir que la luz volvió a las 8:00", "confundir quién golpeaba la puerta"], "Reconoce lo que acertó y subraya con la persona when y while para ver qué acciones ocurren a la vez."),
    "Relee el texto de la mañana y subraya con rojo las rutinas y con verde las acciones del pasado.",
    "Escribe en inglés una oración con when y otra con while sobre algo que pasó esta semana.",
)

# ---------------------------------------------------------------- clase 5: permiso y consejo en textos digitales
CHAT = "Chat de curso: «Lea: Can I use your pen, please? Max: Sure, you can. Lea: Thanks! Should I write in blue or black? Max: You should write in black, and you shouldn't use pencil in the test. Lea: Can I use a calculator? Max: No, you can't. The teacher said it is not allowed. Lea: OK. Thanks for the advice!» (use = usar, should = debería, test = prueba, calculator = calculadora, allowed = permitido, advice = consejo)"
HEALTH = "Página web: «Healthy habits for students. You should drink water every day. You shouldn't eat too many sweets. You can ask the teacher for permission to go to the bathroom. May I leave the classroom? Yes, you may, but come back quickly. It is a good idea to sleep nine hours.» (habits = hábitos, sweets = dulces, permission = permiso, bathroom = baño, leave = salir, come back = volver)"
EVENT = "Mensaje de grupo: «Hi, everyone! The school trip is on Friday. Can we take a camera? Yes, you can. Can we take a ball? No, you can't. You should wear comfortable shoes and take a jacket. You shouldn't bring valuable things, because they can get lost. Can I invite my friend? Please ask the teacher first.» (camera = cámara, comfortable = cómodos, jacket = chaqueta, valuable = de valor, invite = invitar)"

lesson(
    OA5, 5,
    "Los chats y páginas escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer textos digitales (chats, mensajes y páginas web) que piden y dan permiso (Can I…?, You can / can't) y dan consejos (You should / shouldn't). Sirve para entender reglas y recomendaciones en inglés.",
    ["Sé que can significa poder.", "Conozco palabras como allowed, test y habit."],
    [
        "Para pedir permiso (permission) se usa Can I…? o la forma más formal May I…?: Can I use your pen? Para dar permiso se responde Yes, you can o Sure. Para negarlo se usa No, you can't o You can't do that. También puedes oír: It is not allowed (no está permitido). Después de can y may, el verbo va en forma base: Can I go?",
        "Para dar consejo (advice) se usa should (debería) y should not o shouldn't (no debería): You should drink water; you shouldn't eat too many sweets. Un consejo no es una obligación: es una recomendación. La forma It is a good idea to… también da consejos. Después de should, el verbo también va en forma base.",
        "Los textos digitales como chats y páginas web usan frases cortas, abreviaturas y respuestas rápidas: Sure, OK, Thanks. Para leerlos, identifica quién pregunta, qué pide (permiso o consejo) y qué respuesta recibe. En una página de consejos, fíjate en si cada frase usa should o shouldn't: así sabes qué es recomendable y qué no.",
    ],
    [("Can I…?", "¿Puedo…?"), ("May I…?", "¿Puedo…? (más formal)"), ("should / shouldn't", "debería / no debería"), ("advice", "consejo"), ("not allowed", "no permitido"), ("permission", "permiso")],
    [
        ("Pedir y dar permiso", "Lee: «Can I open the window? Yes, you can.» (window = ventana). ¿Qué permiso se pide y cuál es la respuesta?", ["La pregunta usa Can I…?", "Pide abrir la ventana.", "La respuesta es Yes, you can: sí se puede."], "Pide abrir la ventana y le dicen que sí"),
        ("Dar consejo", "Lee: «You shouldn't run in the corridor.» (corridor = pasillo). ¿Es un consejo de hacer algo o de no hacerlo?", ["Veo la palabra shouldn't.", "Significa no deberías.", "Aconseja no correr."], "Aconseja no correr en el pasillo"),
    ],
    [
        ("Pensar que should es una orden obligatoria.", "Se confunde consejo con obligación.", "Should da un consejo; It is not allowed señala una regla."),
        ("Decir «Can I to go?».", "Se agrega to por traducción literal.", "Después de can el verbo va sin to: Can I go?"),
    ],
    [
        ("Lee: " + CHAT + " ¿Qué le pide Lea a Max al comienzo? a) un lápiz pasta b) una calculadora", "a) un lápiz pasta", "Dice Can I use your pen, please?"),
        ("Lee: " + HEALTH + " ¿Qué se debería hacer todos los días? a) beber agua b) comer dulces", "a) beber agua", "Dice you should drink water every day."),
        ("Lee: " + EVENT + " ¿Se puede llevar una cámara? a) sí b) no", "a) sí", "Dice Can we take a camera? Yes, you can."),
    ],
    [
        ("Lee: " + CHAT + " ¿En qué color aconseja Max escribir?", "En negro", "Dice you should write in black."),
        ("Lee: " + HEALTH + " ¿Cuántas horas aconseja dormir?", "Nueve", "Dice sleep nine hours."),
        ("Lee: " + EVENT + " ¿Qué se debe llevar según el consejo?", "Zapatos cómodos y una chaqueta", "Dice wear comfortable shoes and take a jacket."),
    ],
    [
        ("Lee: " + CHAT + " ¿Se puede usar calculadora en la prueba? a) no b) sí", "a) no", "Max dice No, you can't."),
        ("Lee: " + HEALTH + " ¿Qué se debe hacer para salir de la sala según la página? a) pedir permiso b) salir sin avisar", "a) pedir permiso", "Dice May I leave the classroom? Yes, you may."),
        ("Lee: " + EVENT + " ¿Se puede llevar una pelota? a) no b) sí", "a) no", "Dice Can we take a ball? No, you can't."),
    ],
    [
        ("Lee: " + EVENT + " ¿Por qué no se deben llevar cosas de valor?", "Porque se pueden perder", "Dice because they can get lost."),
        ("Lee: " + CHAT + " Un compañero dice que Max aconseja escribir con lápiz grafito en la prueba. ¿Tiene razón? Responde sí o no.", "No", "Max dice you shouldn't use pencil in the test."),
    ],
    [
        ("Lee: " + EVENT + " ¿Qué debe hacer alguien que quiere invitar a un amigo? a) preguntar primero a la profesora b) invitarlo sin decir nada", "a) preguntar primero a la profesora", "Dice please ask the teacher first."),
        ("Lee: " + HEALTH + " ¿Cuántas oraciones del texto usan should o shouldn't?", "2", "Dice you should drink water y you shouldn't eat too many sweets."),
    ],
    [("Lee: «Student: May I borrow your ruler? Friend: Of course, you can. But you should give it back before the next class.» (borrow = pedir prestado, ruler = regla, give back = devolver). ¿Qué consejo da el amigo? a) devolverla antes de la próxima clase b) quedársela", "a) devolverla antes de la próxima clase", "Dice you should give it back before the next class.")],
    [
        ("Al leer un chat, ¿qué dos formas ves para pedir permiso?", "Can I…? o May I…?", "Son las dos formas habituales."),
        ("¿Qué significa «shouldn't»?", "No deberías", "Es un consejo negativo."),
        ("¿Qué va después de can o should?", "El verbo en forma base", "No se agrega to."),
    ],
    task("Lee este chat original: «Eva: Can I sit here? Nico: Yes, you can. Eva: Should I use my red pen or my black pen? Nico: You should use the black pen. You shouldn't write with a marker. Eva: Can I take a photo of the board? Nico: No, you can't. The teacher will send it by email.» (sit = sentarse, marker = marcador, board = pizarra, send = enviar). Escribe: dos permisos que se piden, la respuesta a cada uno y dos consejos.", "Permisos: sentarse (sí) y sacar foto de la pizarra (no). Consejos: usar el lápiz negro y no escribir con marcador.", ["anota dos permisos con su respuesta", "anota dos consejos", "usa los datos correctos"], ["hoja con respuestas"], ["decir que sí puede sacar la foto", "confundir el color del lápiz"], "Reconoce lo que acertó y subraya con la persona can, can't, should y shouldn't."),
    "Relee el chat de Lea y Max y marca con una flecha los permisos y con una estrella los consejos.",
    "Escribe dos consejos en inglés para un compañero que llega nuevo al colegio.",
)
