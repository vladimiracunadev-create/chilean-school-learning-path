"""Cuaderno del estudiante, 7.º básico Inglés (propuesta), EN07 OA 04 (comprensión de textos literarios y no literarios).

Todos los textos son originales y están escritos en el enunciado, con pista en español. Las personas y los datos de las noticias
y las biografías son inventados («de ejemplo»). El texto real del plan lector lo elige el docente.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_en7_a import lesson

OA4 = "EN07 OA 04"

# ---------------------------------------------------------------- clase 1: poemas y tiras cómicas
BAG = "«My backpack is heavy, my backpack is blue. It carries my books and my lunch box too. On Monday it holds my notebook and pen. On Friday it's empty, I fill it again.» (backpack = mochila, heavy = pesada, carries = lleva, lunch box = lonchera, holds = guarda, empty = vacía, fill = llenar)"
WINTER = "«Cold winter morning, the window is white. The street is so quiet, there is frost in the light. I wear my red scarf and my woolly hat. Hot chocolate waits, and that is that.» (frost = escarcha, scarf = bufanda, woolly = de lana, waits = espera)"
RAINC = "Tira cómica en cuatro viñetas. Viñeta 1: Leo mira el cielo gris y dice: «It is going to rain!» Viñeta 2: Mia mira hacia arriba y dice: «No, it isn't. Look, there is some sun!» Viñeta 3: empieza a llover y Mia queda mojada. Viñeta 4: Leo abre su paraguas y dice: «Told you!» (told you = te lo dije, wet = mojada, umbrella = paraguas)"
PENCIL = "Tira cómica en cuatro viñetas. Viñeta 1: Ana revuelve su mochila y dice: «Where is my pencil case?» Viñeta 2: Teo sonríe y dice: «Is this it?» Viñeta 3: Ana dice: «Yes! Thank you!» Viñeta 4: Teo dice: «It was under your chair!» (pencil case = estuche, is this it? = ¿es este?, under = debajo de, chair = silla)"

lesson(
    OA4, 1,
    "Los poemas y las tiras cómicas escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer poemas y tiras cómicas e identificar el tema, los personajes, las rimas y lo que pasa en cada viñeta. Sirve para entender textos literarios cortos en inglés y explicar de qué tratan.",
    ["Sé que los versos riman si terminan con el mismo sonido.", "Conozco palabras como backpack, rain y sun."],
    [
        "Un poema (poem) se escribe en versos (lines) agrupados en estrofas (stanzas). Muchas veces los versos riman (rhyme): blue rima con too, hat rima con that. El tema (theme) es la idea general del poema: de qué trata en el fondo. Para encontrarlo, busca las palabras que se repiten o que describen un mismo tema, por ejemplo backpack, books y notebook en un poema sobre la rutina escolar.",
        "Una tira cómica (comic strip) cuenta una historia breve con dibujos en recuadros llamados viñetas (panels). Los personajes (characters) hablan con globos de diálogo (speech bubbles). Para comprenderla, lee las viñetas en orden, de izquierda a derecha, y pregúntate: ¿quién habla?, ¿qué quiere?, ¿qué pasa al final? A veces la gracia (the joke) está en la última viñeta.",
        "En ambos textos, las palabras importantes (key words) y las expresiones frecuentes ayudan a comprender. «Told you!» es una expresión que significa «te lo dije». En un poema, el ánimo (mood) se descubre con adjetivos como quiet, cold, heavy o happy. Siempre apoya tu respuesta con una palabra del texto.",
    ],
    [("poem / lines / stanza", "poema / versos / estrofa"), ("rhyme", "rima: sonido final igual"), ("theme", "tema: idea general"), ("comic strip / panel", "tira cómica / viñeta"), ("speech bubble", "globo de diálogo"), ("mood", "ánimo del texto")],
    [
        ("Rimas de un poema", "Lee: «The sun is high, the sky is blue. I run and jump, and so do you.» (high = alto, jump = saltar). ¿Qué dos palabras riman?", ["Miro las palabras al final de los versos: blue y you.", "Las dos terminan con el mismo sonido.", "High y sky también riman, pero están dentro del mismo verso y no al final de dos versos."], "blue y you"),
        ("Leer una tira cómica", "Tira cómica. Viñeta 1: Pablo dice: «I'm hungry!» Viñeta 2: Sara le da una manzana. Viñeta 3: Pablo dice: «Thanks!» ¿Qué problema tiene Pablo y cómo se resuelve? (hungry = con hambre, apple = manzana)", ["En la viñeta 1 dice I'm hungry: tiene hambre.", "En la viñeta 2 Sara le da una manzana.", "El problema se resuelve con la manzana."], "Pablo tiene hambre y Sara le da una manzana"),
    ],
    [
        ("Pensar que el tema es lo mismo que una palabra suelta, como «blue».", "El tema es la idea general, no un detalle.", "Pregúntate de qué trata todo el poema."),
        ("Leer las viñetas en desorden.", "Se pierde la secuencia y la gracia.", "Lee de la primera a la última, siguiendo la numeración."),
    ],
    [
        ("Lee: " + BAG + " ¿De qué color es la mochila? a) azul b) roja", "a) azul", "El poema dice my backpack is blue."),
        ("Lee: " + WINTER + " ¿Qué palabra rima con white? a) light b) hat", "a) light", "White y light terminan con el mismo sonido."),
        ("Lee: " + RAINC + " ¿Quién dice «It is going to rain!»? a) Leo b) Mia", "a) Leo", "Lo dice Leo en la viñeta 1."),
    ],
    [
        ("Lee: " + BAG + " ¿Qué lleva la mochila el lunes?", "El cuaderno y el lápiz", "Dice on Monday it holds my notebook and pen."),
        ("Lee: " + WINTER + " ¿Qué espera a la persona del poema?", "Un chocolate caliente", "Dice hot chocolate waits."),
        ("Lee: " + PENCIL + " ¿Dónde estaba el estuche?", "Debajo de la silla de Ana", "Teo lo dice en la viñeta 4: it was under your chair."),
    ],
    [
        ("Lee: " + BAG + " ¿Cuál es el tema del poema? a) la rutina de la mochila durante la semana b) un viaje a la playa", "a) la rutina de la mochila durante la semana", "Habla de lo que lleva el lunes y de cómo queda el viernes."),
        ("Lee: " + WINTER + " ¿Cómo es el ánimo del poema? a) tranquilo y acogedor b) triste y asustado", "a) tranquilo y acogedor", "Quiet, scarf y hot chocolate muestran calma."),
        ("Lee: " + RAINC + " ¿Qué demuestra la viñeta 3? a) que Leo tenía razón b) que Mia tenía razón", "a) que Leo tenía razón", "Llueve, como Leo dijo."),
    ],
    [
        ("Lee: " + WINTER + " Una compañera dice que el poema trata de un día de verano. ¿Qué palabra del texto la contradice?", "winter", "El título y el primer verso dicen cold winter morning."),
        ("Lee: " + PENCIL + " ¿Por qué Teo muestra que el estuche estaba bajo la silla en la última viñeta? a) para revelar dónde estaba y cerrar la historia b) para pedir otro estuche", "a) para revelar dónde estaba y cerrar la historia", "La viñeta final resuelve el problema inicial de Ana."),
    ],
    [
        ("Lee: " + WINTER + " ¿Cuántos pares de palabras riman al final de los versos?", "2", "Son dos pares: white con light y hat con that."),
        ("Lee: " + RAINC + " Ordena las acciones. A) Leo abre su paraguas. B) Mia ve algo de sol. C) Empieza a llover. D) Leo ve el cielo gris.", "D, B, C, A", "Sigue las viñetas del 1 al 4."),
    ],
    [("Lee esta tira cómica. Viñeta 1: Una niña dice: «My bike is broken!» Viñeta 2: Un niño le trae una llave de tuercas. Viñeta 3: Ella dice: «Great! Now it works!» (broken = rota, wrench = llave de tuercas, works = funciona). ¿Qué problema se resuelve en la tira? a) una bicicleta rota b) un libro perdido", "a) una bicicleta rota", "Dice my bike is broken y luego it works.")],
    [
        ("En una comic strip, ¿qué es un panel?", "Un recuadro de una tira cómica", "Cada viñeta muestra una escena."),
        ("¿Qué es el tema de un poema?", "La idea general", "Es de qué trata en el fondo."),
        ("¿Qué significa «Told you!»?", "¡Te lo dije!", "Es una expresión común."),
    ],
    task("Lee este poema original: «The moon is a boat on the dark blue sea. The stars are the fish that swim by me. I close my eyes, and the boat floats on. I wake up, and the night is gone.» (boat = bote, fish = peces, floats = flota, gone = se fue). Escribe: el tema, dos rimas y dos palabras que muestren el ánimo.", "Tema: la noche y los sueños. Rimas: sea-me y on-gone. Ánimo: calmado; floats y close my eyes lo muestran.", ["escribe un tema coherente con el poema", "anota dos rimas correctas", "señala dos palabras del texto que justifican el ánimo"], ["hoja con respuestas"], ["decir que el tema es «fish»", "anotar rimas que no están en el texto"], "Reconoce lo que acertó y vuelve con la persona a los finales de cada verso para encontrar las rimas."),
    "Relee el poema de la mochila y subraya con azul las palabras de objetos escolares.",
    "Dibuja una tira cómica de cuatro viñetas sobre un problema en el patio y escribe un globo de diálogo en inglés en cada una.",
)

# ---------------------------------------------------------------- clase 2: cuentos y novelas adaptadas
BOAT = "«The Blue Boat. In a small village by the sea, there lived a boy called Tomás. Every morning he looked at the old blue boat of Mr. Díaz. One day Mr. Díaz said: Today you can help me, but only if the sea is calm. At noon the wind grew strong and the sky turned gray. Mr. Díaz decided to return to the coast. They arrived safely, wet but happy. That night Tomás wrote in his diary: The sea is beautiful, but we must respect it.» (village = pueblo, calm = en calma, wind = viento, coast = costa, safely = a salvo, diary = diario, respect = respetar)"
ROBOT = "«The Robot Club. On Tuesday afternoon, the robotics club had a problem: the robot could not move. Camila checked the batteries, but they were full. Then Iván looked at the wheel and found a small stone. He removed it, and the robot moved again. The members clapped. Camila said: Teamwork solves problems.» (robot = robot, batteries = pilas, full = llenas, wheel = rueda, stone = piedra, removed = sacó, clapped = aplaudieron, teamwork = trabajo en equipo)"
HOUSE = "«Chapter 1: The New House. Lucía opened the door of the old house at the end of Pine Street. The air smelled like wood and dust. In the living room, there was a large clock that did not work. Strange, she whispered. Behind the clock, she saw a small key.» (chapter = capítulo, dust = polvo, living room = sala, clock = reloj, whispered = susurró, key = llave)"

lesson(
    OA4, 2,
    "Los cuentos y el capítulo adaptado escritos en cada ejercicio y lápiz.",
    "Aprenderé a identificar en un cuento o en una novela adaptada el tema, los personajes y sus acciones, el entorno (tiempo y lugar) y la trama (inicio, desarrollo y final). Sirve para comprender historias en inglés y contarlas en orden.",
    ["Sé que un cuento tiene personajes, lugar y tiempo.", "Conozco verbos en pasado como looked, found y arrived."],
    [
        "Un cuento (story) y una novela adaptada (adapted novel) tienen elementos que conviene identificar. Los personajes (characters) son quienes actúan. El entorno o escenario (setting) es el lugar y el tiempo donde ocurre: a small village by the sea, Tuesday afternoon. La trama (plot) es el orden de los hechos: inicio (beginning), desarrollo (middle) y final (ending).",
        "El inicio presenta a los personajes y el lugar. En el desarrollo aparece un problema o un cambio: el robot no se mueve; el viento se hace fuerte. En el final se resuelve o termina la historia. El tema (theme) es la idea general o la enseñanza: por ejemplo, que hay que respetar el mar o que el trabajo en equipo resuelve problemas.",
        "Los verbos en pasado simple (looked, found, arrived, wrote) te dicen qué hicieron los personajes. Lee con las preguntas who, where, when y what happened. Para el tema, pregunta por qué pasan los hechos y qué aprende el personaje. Apoya siempre tu respuesta con una frase del texto.",
    ],
    [("character", "personaje"), ("setting", "entorno: lugar y tiempo"), ("plot", "trama: orden de los hechos"), ("beginning / middle / ending", "inicio / desarrollo / final"), ("theme", "tema o enseñanza"), ("chapter", "capítulo")],
    [
        ("Personajes y entorno", "Lee: «On a rainy Saturday, Nico and his sister baked bread in the kitchen.» (rainy = lluvioso, baked = hornearon, bread = pan). ¿Quiénes son los personajes y cuál es el entorno?", ["Busco los nombres: Nico y su hermana.", "El tiempo es a rainy Saturday.", "El lugar es the kitchen."], "Personajes: Nico y su hermana. Entorno: un sábado lluvioso en la cocina"),
        ("Inicio, desarrollo y final", "Lee: «Rita lost her hat in the wind. She ran after it across the park. Finally, a boy caught it and gave it back.» (lost = perdió, ran = corrió, caught = atrapó, gave back = devolvió). ¿Cuál es el final?", ["Busco las palabras finally y gave it back.", "Un niño atrapa el sombrero.", "El final es que se lo devuelve."], "Un niño atrapa el sombrero y se lo devuelve a Rita"),
    ],
    [
        ("Confundir el entorno con los personajes.", "Se mezclan quién actúa y dónde ocurre.", "Los personajes son quienes actúan; el entorno es el lugar y el tiempo."),
        ("Contar el final antes del problema.", "No se respeta la trama.", "Ordena los hechos por inicio, desarrollo y final."),
    ],
    [
        ("Lee: " + BOAT + " ¿Dónde ocurre la historia? a) en un pueblo junto al mar b) en una ciudad grande", "a) en un pueblo junto al mar", "Dice in a small village by the sea."),
        ("Lee: " + ROBOT + " ¿Quién encontró la piedra en la rueda? a) Iván b) Camila", "a) Iván", "Dice Iván looked at the wheel and found a small stone."),
        ("Lee: " + HOUSE + " ¿Qué vio Lucía detrás del reloj? a) una llave pequeña b) una carta", "a) una llave pequeña", "Dice she saw a small key."),
    ],
    [
        ("Lee: " + BOAT + " ¿Cuál es el problema en el desarrollo?", "El viento se hizo fuerte y el cielo se puso gris", "Dice the wind grew strong and the sky turned gray."),
        ("Lee: " + ROBOT + " ¿Cuál es el problema del club al inicio?", "El robot no podía moverse", "Dice the robot could not move."),
        ("Lee: " + HOUSE + " ¿Qué le pasa al reloj? a) no funciona b) suena fuerte", "a) no funciona", "Dice a large clock that did not work."),
    ],
    [
        ("Lee: " + BOAT + " ¿Cómo termina la historia? a) llegan a salvo, mojados pero felices b) el bote se hunde", "a) llegan a salvo, mojados pero felices", "Dice they arrived safely, wet but happy."),
        ("Lee: " + ROBOT + " ¿Qué solucionó el problema?", "Sacar la piedra de la rueda", "Dice he removed it, and the robot moved again."),
        ("Lee: " + HOUSE + " ¿Qué hay en el aire de la casa vieja?", "Olor a madera y a polvo", "Dice the air smelled like wood and dust."),
    ],
    [
        ("Lee: " + BOAT + " ¿Cuál es el tema? a) hay que respetar el mar b) los viajes largos son aburridos", "a) hay que respetar el mar", "Tomás lo escribe en su diario: we must respect it."),
        ("Lee: " + ROBOT + " ¿Cuál es el tema? a) el trabajo en equipo resuelve problemas b) los robots son caros", "a) el trabajo en equipo resuelve problemas", "Camila lo dice al final."),
    ],
    [
        ("Lee: " + BOAT + " Ordena los hechos. A) Llegan a la costa. B) Tomás mira el bote. C) El viento se hace fuerte.", "B, C, A", "Primero admira el bote, luego cambia el clima y al final regresan."),
        ("Lee: " + HOUSE + " ¿Qué pregunta de misterio queda sin responder al final del capítulo? a) para qué sirve la llave b) cómo se llama la calle", "a) para qué sirve la llave", "El texto nombra Pine Street, pero no explica la llave."),
    ],
    [("Lee: «On Sunday morning, Julia and her cousin went to the river. They saw a small boat without a person. Julia called the police station, and an officer took the boat.» (boat = bote, police station = comisaría, officer = oficial). ¿Cuándo ocurre la historia? a) el domingo en la mañana b) el sábado en la noche", "a) el domingo en la mañana", "Dice on Sunday morning.")],
    [
        ("¿Qué es el entorno de un cuento?", "El lugar y el tiempo donde ocurre", "Responde a where y when."),
        ("¿Qué son el inicio, el desarrollo y el final?", "Las partes de la trama", "Ordenan los hechos."),
        ("¿Qué pregunta ayuda a encontrar el tema?", "Qué aprende el personaje", "El tema es la idea o enseñanza."),
    ],
    task("Lee este cuento original: «The Lost Dog. On Friday afternoon, Marcos found a small brown dog near the bus stop. The dog was cold and hungry. Marcos took it to the school, and the teacher called the owner. The next day, a girl came for the dog. She said: Thank you, you are very kind!» (found = encontró, owner = dueño, hungry = hambriento, kind = amable). Escribe: el entorno, los personajes, el problema, el final y el tema.", "Entorno: viernes en la tarde cerca de un paradero. Personajes: Marcos, el perro, la profesora y la niña. Problema: el perro estaba perdido, con frío y hambre. Final: la niña vuelve por su perro. Tema: ayudar a otros.", ["identifica el entorno y los personajes", "describe el problema y el final con datos del texto", "propone un tema coherente"], ["hoja con respuestas"], ["omitir al dueño o a la profesora", "decir que el tema es «brown dog»"], "Reconoce lo que acertó y ayuda a la persona a ordenar los hechos con first, then y finally."),
    "Relee el cuento del robot y subraya con rojo el problema y con verde la solución.",
    "Escribe en español un final distinto para el capítulo de la casa nueva.",
)

# ---------------------------------------------------------------- clase 3: correos, avisos y páginas web
EMAIL = "De: Carla. Para: Rodrigo. Asunto: School trip. «Hi Rodrigo, I have news about the trip to the science museum. We leave on Thursday at 8:30 from the school gate. Please bring a lunch, a water bottle and the signed permission form. The bus returns at 3:00. Write to me if you have questions. Best wishes, Carla» (news = noticias, leave = salimos, gate = portón, signed = firmada, permission form = autorización, returns = vuelve, questions = preguntas)"
BIKE = "Aviso: «BIKE SALE at Bike World! Mountain bikes for teenagers. Colors: red and blue. Helmet included. Special price: 120,000 pesos. Only until Saturday. Visit us at 25 Main Street.» (sale = venta, helmet = casco, included = incluido, special price = precio especial, only until = solo hasta)"
WEBMUS = "Página web: «Science Museum. Opening hours: Tuesday to Sunday, 10:00 to 17:00. Closed on Mondays. Tickets: adults 6,000 pesos, students 3,000 pesos, children under five free. Rules: Do not touch the exhibits. Photos are allowed without flash.» (opening hours = horario, closed = cerrado, tickets = entradas, exhibits = piezas, allowed = permitidas, flash = flash)"

lesson(
    OA4, 3,
    "Los correos, avisos y páginas web escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer correos, avisos publicitarios y páginas web, y a encontrar la información específica: quién escribe, qué ofrece, cuándo, cuánto y qué se debe hacer. Sirve para entender mensajes reales en inglés.",
    ["Sé leer horas, precios y días.", "Conozco palabras como bring, price y open."],
    [
        "Un correo electrónico (email) tiene partes: De (From), Para (To), Asunto (Subject), saludo (greeting), mensaje (message) y despedida (closing). El asunto resume el tema. En el mensaje busca quién escribe, qué quiere decir, cuándo, dónde y qué debe hacer la persona que lee. Palabras como please y bring indican una petición.",
        "Un aviso publicitario (advertisement) quiere convencer de comprar algo. Muestra qué se vende, el precio (price), un beneficio (benefit) y un límite de tiempo (only until Saturday). Una página web (web page) informa con títulos, horarios (opening hours), precios y reglas (rules). En todos estos textos, los números y las palabras en mayúscula entregan información específica.",
        "Para leer rápido, primero mira el título o el asunto, luego recorre el texto buscando la información que necesitas (por ejemplo, un precio). Después lee esa parte con cuidado. Recuerda que en inglés los miles se escriben con coma: 6,000 es seis mil. Si hay una lista de reglas, lee cada una: lo que está permitido (allowed) y lo que no.",
    ],
    [("email / subject", "correo / asunto"), ("advertisement", "aviso publicitario"), ("price", "precio"), ("opening hours", "horario de atención"), ("rules", "reglas"), ("allowed", "permitido")],
    [
        ("Leer un correo", "Lee: «Subject: Football practice. Hi team, practice is on Wednesday at 5:00 in the school yard. Bring your boots.» (practice = entrenamiento, boots = zapatos de fútbol). ¿Qué debe llevar el equipo?", ["Busco la palabra bring.", "Dice bring your boots.", "La respuesta es sus zapatos de fútbol."], "Sus zapatos de fútbol"),
        ("Leer un aviso", "Lee: «Pizza Night! Two pizzas for 9,000 pesos. Only on Friday.» (night = noche). ¿Hasta cuándo es la oferta?", ["Busco la limitación de tiempo.", "Dice only on Friday.", "La oferta es solo el viernes."], "Solo el viernes"),
    ],
    [
        ("Leer los números con coma como si fueran decimales.", "En inglés la coma separa los miles.", "6,000 pesos son seis mil pesos."),
        ("Responder sin mirar el asunto o el título.", "Se pierde el tema general.", "Lee primero el asunto o el título."),
    ],
    [
        ("Lee: " + EMAIL + " ¿Qué actividad se anuncia? a) una visita al museo de ciencias b) una fiesta", "a) una visita al museo de ciencias", "Dice the trip to the science museum."),
        ("Lee: " + BIKE + " ¿Qué incluye el precio? a) un casco b) una mochila", "a) un casco", "Dice helmet included."),
        ("Lee: " + WEBMUS + " ¿Qué día está cerrado el museo? a) el lunes b) el domingo", "a) el lunes", "Dice closed on Mondays."),
    ],
    [
        ("Lee: " + EMAIL + " ¿A qué hora salen del colegio?", "A las 8:30", "Dice we leave on Thursday at 8:30."),
        ("Lee: " + BIKE + " ¿Qué colores tienen las bicicletas?", "Rojo y azul", "Dice red and blue."),
        ("Lee: " + WEBMUS + " ¿Cuánto cuesta la entrada de un estudiante, en pesos?", "$3.000", "Dice students 3,000 pesos."),
    ],
    [
        ("Lee: " + EMAIL + " Rodrigo va a la visita. ¿Qué tres cosas lleva? a) almuerzo, botella de agua y autorización firmada b) mochila, balón y casco", "a) almuerzo, botella de agua y autorización firmada", "Son las tres cosas que pide Carla."),
        ("Lee: " + WEBMUS + " Un grupo de 4 estudiantes compra entradas. ¿Cuánto pagan en total, en pesos?", "$12.000", "Cada estudiante paga tres mil pesos.", "4*3000"),
        ("Lee: " + BIKE + " Una bicicleta cuesta 120,000 pesos. Con 20,000 pesos ya ahorrados, ¿cuánto falta para comprarla?", "$100.000", "Se resta lo ahorrado al precio.", "120000-20000"),
    ],
    [
        ("Lee: " + EMAIL + " ¿Cuál es el propósito del correo? a) informar y pedir que lleven cosas b) vender entradas", "a) informar y pedir que lleven cosas", "Informa la salida y dice please bring."),
        ("Lee: " + WEBMUS + " Un visitante lleva una cámara con flash. ¿Qué regla no cumple? a) las fotos se permiten sin flash b) no se debe correr", "a) las fotos se permiten sin flash", "Dice photos are allowed without flash."),
    ],
    [
        ("Lee: " + WEBMUS + " Un niño de cuatro años y su hermana de catorce años (estudiante) van al museo. ¿Cuánto pagan en total, en pesos?", "$3.000", "El niño menor de cinco años entra gratis y la estudiante paga 3.000."),
        ("Lee: " + EMAIL + " Si el bus sale a las 8:30 y vuelve a las 3:00 de la tarde, ¿cuánto dura la actividad?", "6 horas y media", "De 8:30 a 15:00 pasan seis horas y media."),
    ],
    [("Lee: «Subject: Library book. Hi Lucas, your book is ready at the library. Please pick it up before Friday. Best, the librarian» (pick up = retirar, before = antes de). ¿Cuándo debe retirar el libro? a) antes del viernes b) después del viernes", "a) antes del viernes", "Dice before Friday.")],
    [
        ("¿Qué indica el asunto de un correo?", "El tema del mensaje", "Resume de qué trata."),
        ("¿Qué quiere lograr un aviso publicitario?", "Convencer de comprar", "Muestra qué se vende y a qué precio."),
        ("¿Cómo se lee 6,000 en inglés?", "Seis mil", "La coma separa los miles."),
    ],
    task("Lee este correo original: «From: Mrs. Vera. To: all students. Subject: Art class. Hello, everybody. Tomorrow we will paint with watercolors. Please bring a small brush, a jar and an old shirt. The class begins at 11:00. Do not forget your sketchbook.» (watercolors = acuarelas, brush = pincel, jar = frasco, old shirt = camisa vieja, sketchbook = croquera). Escribe: quién escribe, el asunto, a qué hora empieza y los cuatro objetos que hay que llevar.", "Escribe la Sra. Vera. Asunto: Art class. Empieza a las 11:00. Objetos: pincel, frasco, camisa vieja y croquera.", ["identifica a quien escribe y el asunto", "anota la hora exacta", "lista los cuatro objetos"], ["hoja con respuestas"], ["omitir la croquera", "anotar una hora distinta de las 11:00"], "Reconoce lo que acertó y relee con la persona las frases con bring y don't forget."),
    "Relee el aviso de la bicicleta y subraya con una línea el precio y con dos líneas el límite de tiempo.",
    "Escribe en inglés un correo breve de tres líneas para invitar a un amigo a tu casa con día y hora.",
)

# ---------------------------------------------------------------- clase 4: procedimientos, noticias y biografías
SENDMAIL = "«How to send a good email. First, write a clear subject. Second, start with Hello and the name of the person. Next, write your message in short sentences. If you attach a file, say it in the text. Finally, read it again before you send it.» (clear = claro, attach = adjuntar, file = archivo, again = otra vez, send = enviar)"
NEWS = "Noticia de ejemplo: «Students plant 200 trees. Last Saturday, 50 students from Pine School planted 200 trees in the city park. The mayor said it was a great idea. Because the park lost many trees in a storm, the students decided to help. If the trees grow well, the park will have more shade next summer.» (plant = plantar, mayor = alcalde, storm = tormenta, shade = sombra)"
BIO = "Biografía de una persona inventada, de ejemplo: «Marta Rivas was born in a small town in 1980. As a child, she loved the stars. She studied physics at university and, after that, she worked at an observatory. In 2015, she discovered a new comet. Many people think she is the best scientist in her town.» (born = nació, stars = estrellas, studied = estudió, observatory = observatorio, discovered = descubrió, comet = cometa)"

lesson(
    OA4, 4,
    "Los procedimientos, noticias y biografías escritos en cada ejercicio y lápiz.",
    "Aprenderé a leer procedimientos, noticias y biografías, y a reconocer la secuencia, la diferencia entre hecho y opinión, la condición con if y la causa y el efecto con because. Sirve para entender textos informativos y saber qué datos comprobar.",
    ["Sé que first, then y finally ordenan los pasos.", "Conozco la diferencia entre un hecho y una opinión."],
    [
        "Un procedimiento (procedure) ordena pasos con first, second, next y finally. Una noticia (news) cuenta un hecho reciente y responde quién, qué, dónde y cuándo. Una biografía (biography) cuenta la vida de una persona en orden de tiempo: born in 1980 (nació en 1980), studied (estudió), worked (trabajó), discovered (descubrió). Todos estos textos usan palabras de orden, de tiempo y de causa.",
        "Reconoce las relaciones entre ideas. La secuencia usa first, next, after that y finally. La causa y el efecto usan because (porque). La condición usa if (si): «If the trees grow well, the park will have more shade» (si los árboles crecen bien, el parque tendrá más sombra). Una condición dice qué pasa solo cuando algo ocurre. Recuerda que el verbo después de if va en presente; si habla de algo que puede ocurrir mañana, el resultado usa will (If it rains, we will stay inside). Si siempre ocurre, el resultado también va en presente (If you press the button, the door opens).",
        "También distingue hechos de opiniones. Un hecho se puede comprobar: 50 students planted 200 trees. Una opinión expresa lo que alguien piensa: it was a great idea, she is the best scientist. En una noticia o biografía, fíjate en quién dice la opinión, por ejemplo the mayor o many people think. Así sabes si es un dato o un juicio.",
    ],
    [("procedure", "procedimiento"), ("news", "noticia"), ("biography", "biografía"), ("if", "si: introduce una condición"), ("because", "porque"), ("opinion / fact", "opinión / hecho")],
    [
        ("Condición con if", "Lee: «If you press the green button, the door opens.» (press = presionar, button = botón, opens = se abre). ¿Qué pasa si se presiona el botón verde?", ["Busco la palabra if.", "Después de if está la condición: presionar el botón verde.", "El resultado es que la puerta se abre."], "La puerta se abre"),
        ("Hecho y opinión", "Lee: «The school has 20 classrooms. It is the best school in the city.» (classrooms = salas). ¿Cuál es el hecho?", ["Un hecho se puede comprobar contando.", "Veinte salas se puede contar.", "The best school es una opinión."], "The school has 20 classrooms"),
    ],
    [
        ("Pensar que una frase con un número siempre es un hecho.", "No se revisa quién lo afirma ni si se puede comprobar.", "Comprueba si el dato se puede verificar."),
        ("Usar will después de if en la condición.", "Se confunde cuál verbo va en presente.", "If + presente, y el resultado lleva will."),
    ],
    [
        ("Lee: " + SENDMAIL + " ¿Qué se hace en el primer paso? a) escribir un asunto claro b) leer otra vez el correo", "a) escribir un asunto claro", "Dice First, write a clear subject."),
        ("Lee: " + NEWS + " ¿Dónde plantaron los árboles? a) en el parque de la ciudad b) en el patio del colegio", "a) en el parque de la ciudad", "Dice in the city park."),
        ("Lee: " + BIO + " ¿Qué estudió Marta Rivas? a) física b) arte", "a) física", "Dice she studied physics at university."),
    ],
    [
        ("Lee: " + SENDMAIL + " ¿Qué se debe hacer si se adjunta un archivo?", "Decirlo en el texto del correo", "Dice if you attach a file, say it in the text."),
        ("Lee: " + NEWS + " ¿Por qué decidieron ayudar los estudiantes?", "Porque el parque perdió muchos árboles en una tormenta", "Dice because the park lost many trees in a storm."),
        ("Lee: " + BIO + " ¿Qué descubrió en 2015?", "Un cometa nuevo", "Dice she discovered a new comet."),
    ],
    [
        ("Lee: " + NEWS + " ¿Qué ocurrirá si los árboles crecen bien? a) el parque tendrá más sombra b) el parque se cerrará", "a) el parque tendrá más sombra", "Dice if the trees grow well, the park will have more shade."),
        ("Lee: " + NEWS + " ¿Qué frase es una opinión? a) it was a great idea b) 50 students planted 200 trees", "a) it was a great idea", "Great expresa un juicio del alcalde."),
        ("Lee: " + BIO + " ¿Qué frase es una opinión? a) many people think she is the best scientist b) she was born in 1980", "a) many people think she is the best scientist", "Best expresa un juicio y no se puede medir."),
    ],
    [
        ("Lee: " + BIO + " Ordena la vida de Marta. A) Trabajó en un observatorio. B) Estudió física. C) Amaba las estrellas de niña. D) Descubrió un cometa.", "C, B, A, D", "Sigue el orden del texto."),
        ("Lee: " + SENDMAIL + " Si un correo no tiene asunto claro, ¿qué paso no se cumplió? a) el primero b) el último", "a) el primero", "El primer paso es escribir un asunto claro."),
    ],
    [
        ("Lee: " + NEWS + " Si 50 estudiantes plantaron 200 árboles por igual, ¿cuántos árboles plantó cada uno?", "4", "Se reparten los árboles entre los estudiantes.", "200//50"),
        ("Lee: " + BIO + " Marta nació en 1980 y descubrió el cometa en 2015. ¿Cuántos años pasaron entre su nacimiento y el descubrimiento?", "35", "Se resta el año de nacimiento al año del descubrimiento.", "2015-1980"),
    ],
    [("Lee: «If it rains tomorrow, we will have the match inside the gym because the field will be wet.» (match = partido, field = cancha, wet = mojada). ¿Dónde será el partido si llueve? a) dentro del gimnasio b) en la cancha", "a) dentro del gimnasio", "La condición if it rains lleva a have the match inside the gym.")],
    [
        ("En un texto leído, ¿qué palabra señala que viene una condición?", "if", "If significa si y abre la condición."),
        ("¿Cómo se ordena una biografía?", "En orden de tiempo", "Va de los primeros años hacia los últimos."),
        ("¿Una opinión se puede medir?", "No", "Depende de quién la diga."),
    ],
    task("Lee esta noticia de ejemplo: «Pine Library has a new rule. Because many students talk loudly, the library now has a quiet room. If you want to talk, you must use the group room. Many students think the new rule is excellent.» (rule = regla, loudly = fuerte, quiet = silenciosa, group room = sala grupal, excellent = excelente). Escribe: un hecho, una opinión, una causa con because y una condición con if.", "Hecho: la biblioteca tiene una sala silenciosa. Opinión: la regla es excelente. Causa: muchos estudiantes hablan fuerte. Condición: si quieres hablar, usa la sala grupal.", ["escribe un hecho comprobable", "identifica una opinión", "escribe una causa y una condición con datos del texto"], ["hoja con respuestas"], ["poner la opinión como hecho", "mezclar causa y condición"], "Reconoce lo que acertó y subraya con la persona because en un color y if en otro."),
    "Relee la biografía de Marta y dibuja una línea de tiempo con tres fechas o etapas.",
    "Escribe en inglés una condición con if sobre el tiempo de mañana.",
)

# ---------------------------------------------------------------- clase 5: palabras derivadas y conectores
UNTEXT = "«Sofía was unhappy because her bike was old and slow. Her friend Tomás said: Do not worry, I will unlock the garage and we will repair it. They worked slowly and carefully. Soon the bike looked new again.» (unhappy = infeliz, worry = preocuparse, unlock = abrir con llave, garage = garaje, repair = reparar, slowly = despacio, carefully = con cuidado, quickly = rápidamente)"
CONN = "«First, Ema opens the book. Second, she reads the title. Next, she looks at the pictures. Finally, she writes a question. Before she reads, she thinks about the topic. While she reads, she takes notes. After she reads, she shares ideas. Ema likes poems, and her brother likes poems too. She reads in the library or at home.» (opens = abre, pictures = imágenes, topic = tema, takes notes = toma notas, shares = comparte)"

lesson(
    OA4, 5,
    "Los textos escritos en cada ejercicio y lápiz.",
    "Aprenderé a formar palabras con el prefijo un- y los sufijos -ing y -ly, y a reconocer conectores como first, second, next, finally, or, when, while, before, after, too y because. Sirve para entender palabras nuevas y cómo se unen las ideas de un texto.",
    ["Sé que un adjetivo describe cómo es algo.", "Conozco palabras como happy, slow y quick."],
    [
        "Las palabras derivadas (derived words) se forman a partir de otra palabra. El prefijo un- va al inicio y significa no o lo contrario: happy → unhappy (infeliz), fair → unfair (injusto), kind → unkind (poco amable). Con algunos verbos, un- indica deshacer la acción: lock → unlock (abrir con llave). El sufijo -ing va al final de un verbo: read → reading, play → playing. Indica una acción en curso o forma sustantivos: swimming (nadar), a swimming pool (una piscina para nadar).",
        "El sufijo -ly convierte un adjetivo en un adverbio de modo, que dice cómo se hace algo: slow → slowly (despacio), quick → quickly (rápidamente), careful → carefully (con cuidado). Si el adjetivo termina en -y, cambia a -ily: happy → happily (felizmente). Para comprender una palabra nueva, quita el prefijo o el sufijo y busca la palabra base: unfair = un- + fair.",
        "Los conectores (connectors) unen ideas y muestran su relación. First, second, next y finally ordenan los pasos. Or ofrece opciones. Too significa también. When y while indican tiempo (cuando y mientras). Before y after indican antes y después. Because explica una causa. Al leer, subraya los conectores para ver cómo se organiza el texto.",
    ],
    [("un-", "prefijo: no o lo contrario"), ("-ing", "sufijo: acción en curso o nombre de actividad"), ("-ly", "sufijo: dice cómo se hace algo"), ("base word", "palabra base"), ("connector", "conector"), ("derived word", "palabra derivada")],
    [
        ("Prefijo un-", "Forma la palabra contraria de «kind» (amable) con un-. ¿Qué significa?", ["Agrego un- al inicio de kind.", "La palabra es unkind.", "Significa poco amable."], "unkind: poco amable"),
        ("Sufijo -ly", "Forma el adverbio de «quiet» (silencioso) y completa: «She speaks ___.»", ["Agrego -ly a la palabra base.", "La palabra es quietly.", "Dice cómo habla ella."], "quietly"),
    ],
    [
        ("Agregar un- a cualquier palabra para decir lo contrario.", "No todas las palabras aceptan un-.", "Comprueba que la palabra exista, por ejemplo unhappy, unfair, unlock."),
        ("Escribir happyly en lugar de happily.", "No se cambia la y por i.", "Si termina en -y, cambia a -ily."),
    ],
    [
        ("¿Cuál es la palabra base de «unhappy»? a) happy b) hap", "a) happy", "Se quita el prefijo un-."),
        ("¿Qué significa «slowly»? a) despacio b) rápido", "a) despacio", "Es el adverbio de slow."),
        ("¿Qué palabra tiene el sufijo -ing? a) reading b) reader", "a) reading", "Termina en -ing."),
    ],
    [
        ("Lee: " + UNTEXT + " ¿Por qué estaba Sofía infeliz? a) su bicicleta era vieja y lenta b) perdió su casco", "a) su bicicleta era vieja y lenta", "Dice it was old and slow."),
        ("Lee: " + UNTEXT + " ¿Qué abrió Tomás? a) el garaje b) la ventana", "a) el garaje", "Dice I will unlock the garage."),
        ("Lee: " + UNTEXT + " ¿Cómo trabajaron los amigos?", "Despacio y con cuidado", "Dice they worked slowly and carefully."),
    ],
    [
        ("Completa con un adverbio con -ly: «The turtle walks very ___.» (slow). ¿Qué palabra falta?", "slowly", "Se agrega -ly a la palabra base slow."),
        ("¿Cuál es el adverbio de «happy»? a) happily b) happyly", "a) happily", "Si termina en -y, cambia a -ily."),
        ("¿Qué verbo significa abrir con llave, lo contrario de «lock» (cerrar con llave)? a) unlock b) block", "a) unlock", "Un- indica deshacer la acción."),
    ],
    [
        ("Lee: " + CONN + " ¿Qué conector indica que Ema hace algo antes de leer? a) before b) while", "a) before", "Dice before she reads, she thinks about the topic."),
        ("Lee: " + CONN + " ¿Qué conector muestra que a su hermano también le gustan los poemas? a) too b) or", "a) too", "Dice and her brother likes poems too."),
    ],
    [
        ("Lee: " + CONN + " Ordena los pasos de Ema según las palabras de secuencia. A) Escribe una pregunta. B) Lee el título. C) Mira las imágenes. D) Abre el libro.", "D, B, C, A", "First, second, next y finally ordenan los pasos."),
        ("Lee: " + CONN + " ¿Cuántas palabras de secuencia aparecen en las primeras cuatro oraciones del texto?", "4", "First, second, next y finally."),
    ],
    [("Lee: «Pablo was unhappy because the game was unfair. The referee decided quickly, and the players listened carefully.» (referee = árbitro, players = jugadores, listened = escucharon). ¿Qué dos adverbios con -ly aparecen? a) quickly y carefully b) unhappy y unfair", "a) quickly y carefully", "Son adverbios que dicen cómo se decidió y cómo escucharon.")],
    [
        ("¿Qué significa el prefijo un-?", "No o lo contrario", "Cambia el significado de la palabra base."),
        ("¿Qué dice un adverbio terminado en -ly?", "Cómo se hace algo", "Describe el modo de la acción."),
        ("¿Qué conector explica una causa?", "because", "Because significa porque y da el motivo."),
    ],
    task("Lee este texto original: «Yesterday, Luisa felt unlucky because she lost her keys. She searched quickly in her bag, but the keys were not there. While she was looking, her friend helped her carefully. Finally, they found the keys in the kitchen. Luisa was happy, and her friend was happy too.» (unlucky = sin suerte, lost = perdió, searched = buscó, found = encontraron). Escribe: una palabra con un-, dos adverbios con -ly que digan cómo se hizo algo (sin contar finally) y los conectores while, finally y too con la frase en que aparecen.", "Con un-: unlucky. Con -ly: quickly y carefully (finally es el conector). While: while she was looking. Finally: finally, they found the keys. Too: and her friend was happy too.", ["identifica la palabra con un-", "escribe dos adverbios con -ly", "relaciona cada conector con su frase"], ["hoja con respuestas"], ["anotar happy como palabra con un-", "olvidar la frase de too"], "Reconoce lo que acertó y subraya con la persona los prefijos y sufijos que encontró."),
    "Escribe tres palabras con un-: unhappy, unfair y unkind, y una oración con cada una.",
    "Busca en el texto de Sofía todas las palabras que terminan en -ly.",
)
