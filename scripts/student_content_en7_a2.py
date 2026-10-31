"""Cuaderno del estudiante, 7.º básico Inglés (propuesta), EN07 OA 02 (información explícita y relaciones en textos orales).

Las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan pista en español.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_en7_a import ADULT, lesson

OA2 = "EN07 OA 02"

# ---------------------------------------------------------------- clase 1: tema e ideas generales
WATER = "«When the sun heats the sea, the water goes up into the air as vapor. In the sky, the vapor gets cold and forms clouds. Then the water falls to the ground as rain or snow. This movement of water is called the water cycle.» (heats = calienta, vapor = vapor, clouds = nubes, falls = cae, ground = suelo, cycle = ciclo)"
JAPAN = "«In Japan, people take off their shoes before they enter a house. They leave the shoes near the door and put on soft slippers. This keeps the floor clean and shows respect for the home.» (take off = sacarse, enter = entrar, slippers = pantuflas, floor = piso, respect = respeto, home = hogar)"
ICE = "«Iceland is a cold island, but many houses are warm. The reason is simple: hot water comes out of the ground in many places. People use it to heat their homes and to keep the sidewalks free of ice. It is a clean source of energy.» (island = isla, reason = razón, comes out = sale, heat = calentar, sidewalks = veredas, source = fuente)"

lesson(
    OA2, 1,
    "Los textos orales escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a identificar el tema y las ideas generales de un texto oral sobre ciencias, otras culturas o el mundo actual. Sirve para entender de qué habla una charla sin quedarme en los detalles.",
    ["Sé reconocer palabras clave en una escucha.", "Conozco palabras como water, rain, house y energy."],
    [
        "El tema (topic) de un texto oral es de qué trata en una palabra o en una frase corta. Las ideas generales (main ideas) son los mensajes más importantes; los detalles (details) son datos menores. Los textos de otras asignaturas, de otras culturas o de interés global tienen palabras temáticas: water y rain en ciencias; shoes y respect en cultura; energy en medio ambiente.",
        "Para encontrar el tema, escucha una vez sin anotar y pregúntate: ¿qué palabra se repite o qué idea domina? En el texto del ciclo del agua, water aparece muchas veces. Después, elige un título (title) que sirva para todo el texto, ni demasiado pequeño ni demasiado grande: «The Water Cycle» sirve; «Rain» queda corto porque no incluye vapor y nubes.",
        "La idea general se puede decir en una oración corta: «El texto explica que el agua sube, forma nubes y cae». Si una opción de respuesta habla de un solo detalle, probablemente no es la idea general. Usa palabras como «explains» (explica) y «describes» (describe) para decir tu idea en inglés: The text explains how…",
    ],
    [("topic", "tema: de qué trata"), ("main idea", "idea general"), ("detail", "detalle"), ("title", "título"), ("explains", "explica"), ("describes", "describe")],
    [
        ("Tema de un texto de ciencias", ADULT + "«Plants need light to grow. Their leaves take light from the sun and use it to make food. Without light, plants turn pale and weak.» (leaves = hojas, pale = pálidas, weak = débiles). ¿Cuál es el tema?", ["Busco la palabra que se repite: plants y light.", "Todo el texto explica por qué las plantas necesitan luz.", "El tema es la luz y las plantas."], "Por qué las plantas necesitan luz"),
        ("Idea general y detalle", ADULT + "«In many countries, children wear uniforms at school. Uniforms help students feel equal. In some schools, they are blue; in others, gray.» (uniforms = uniformes, equal = iguales). ¿Cuál es un detalle y no la idea general?", ["La idea general es que los uniformes ayudan a sentirse iguales.", "El color azul o gris es un dato menor.", "Por eso el color es un detalle."], "El color de los uniformes (azul o gris)"),
    ],
    [
        ("Elegir como tema el primer dato que se oye.", "Se confunde un detalle con el tema.", "Busca la palabra que se repite y la idea que une todo el texto."),
        ("Decir que el texto trata de «rain» solo porque aparece rain.", "Se elige una palabra y no la idea completa.", "Elige el tema que incluye todas las ideas del texto."),
    ],
    [
        (ADULT + WATER + " ¿Cuál es el tema? a) el ciclo del agua b) cómo se fabrica un paraguas", "a) el ciclo del agua", "El texto termina diciendo this movement of water is called the water cycle."),
        (ADULT + JAPAN + " ¿Cuál es el tema? a) una costumbre al entrar en una casa b) un deporte tradicional", "a) una costumbre al entrar en una casa", "Todo el texto habla de sacarse los zapatos antes de entrar."),
        (ADULT + ICE + " ¿Qué fuente de calor se usa en Islandia? a) agua caliente del suelo b) leña", "a) agua caliente del suelo", "Dice hot water comes out of the ground."),
    ],
    [
        (ADULT + WATER + " ¿Qué pasa con el vapor en el cielo?", "Se enfría y forma nubes", "Dice the vapor gets cold and forms clouds."),
        (ADULT + JAPAN + " ¿Por qué se dejan los zapatos cerca de la puerta?", "Para mantener el piso limpio y mostrar respeto", "Dice this keeps the floor clean and shows respect."),
        (ADULT + ICE + " ¿Para qué usan el agua caliente además de calentar casas?", "Para mantener las veredas libres de hielo", "Dice to keep the sidewalks free of ice."),
    ],
    [
        (ADULT + WATER + " Elige el mejor título. a) The Water Cycle b) A Rainy Day", "a) The Water Cycle", "Incluye vapor, nubes y lluvia; el otro título solo cubre la lluvia."),
        (ADULT + JAPAN + " Elige la idea general. a) Entrar sin zapatos mantiene limpio y muestra respeto b) Las pantuflas son suaves", "a) Entrar sin zapatos mantiene limpio y muestra respeto", "La otra opción es solo un detalle."),
        (ADULT + ICE + " Elige la idea general. a) El agua caliente natural ayuda a Islandia con energía limpia b) Islandia es una isla", "a) El agua caliente natural ayuda a Islandia con energía limpia", "Resume las dos ideas del texto; la otra es un dato menor."),
    ],
    [
        (ADULT + ICE + " Una compañera dice que el texto trata de países cálidos. ¿Qué dato del texto lo contradice?", "Iceland is a cold island", "El texto dice que la isla es fría."),
        (ADULT + WATER + " Un compañero dice que del cielo solo cae lluvia en este texto. ¿Es correcto? Responde sí o no.", "No", "El texto menciona rain y también snow."),
    ],
    [
        (ADULT + WATER + " Ordena según el texto. A) Se forman nubes. B) Sube el vapor. C) Cae lluvia o nieve.", "B, A, C", "Primero el sol calienta el mar y sube el vapor, luego se forman nubes y al final cae el agua."),
        (ADULT + ICE + " ¿Cuántos usos del agua caliente menciona el texto? Cuenta calentar casas y mantener las veredas libres de hielo.", "2", "El texto nombra dos usos: calentar los hogares y despejar las veredas."),
    ],
    [(ADULT + "«Many animals confuse plastic with food. Sea turtles eat plastic bags because they look like jellyfish. This can make the turtles very sick. We can help by using fewer plastic bags.» (confuse = confunden, turtles = tortugas, jellyfish = medusas, sick = enfermas, fewer = menos). ¿Cuál es la idea general? a) el plástico daña a los animales marinos b) las tortugas son rápidas", "a) el plástico daña a los animales marinos", "El texto explica el daño y sugiere una solución.")],
    [
        ("Al escuchar en inglés, ¿qué es el topic?", "De qué trata el texto", "Resume lo más importante."),
        ("¿Qué frase sirve para decir la idea general?", "The text explains how…", "Explains introduce la idea."),
        ("¿Un color o una cifra suelen ser idea general o detalle?", "Detalle", "Son datos menores."),
    ],
    task("Un adulto lee dos veces este texto: «In Chile, many schools have a school garden. Students plant lettuce, carrots and herbs. They water the plants and take care of the soil. In the end, they eat what they grow.» (lettuce = lechuga, carrots = zanahorias, herbs = hierbas, take care of = cuidar, soil = tierra, grow = cultivar). En tu hoja escribe: el tema, la idea general en una oración y dos detalles.", "Tema: los huertos escolares. Idea general: los estudiantes cultivan y cuidan plantas que luego comen. Detalles: plantan lechuga y zanahorias; riegan las plantas.", ["indica el tema", "escribe una idea general que incluye el texto completo", "anota dos detalles que sí aparecen"], ["hoja con respuestas", "nota del adulto"], ["decir solo «lettuce» como tema", "poner como idea general un solo detalle"], "Reconoce lo que acertó y aclara la diferencia entre tema, idea general y detalle con tres colores."),
    "Pide a un adulto que lea el texto de Islandia y escribe un título distinto de tres a cinco palabras en inglés.",
    "Escribe en español de qué crees que trata un texto que dice: «Bees fly from flower to flower» y justifica con una palabra clave.",
)

# ---------------------------------------------------------------- clase 2: información específica y detalles
MATCH = "«Good evening. This is Radio Sur with the sports news. At the city stadium, the local team, Los Pumas, played against Atlético Norte. The match started at seven o'clock. Los Pumas scored two goals, and Atlético Norte scored one. Eight thousand fans watched the game.» (stadium = estadio, scored = anotó, goals = goles, fans = hinchas, watched = vieron)"
FRIENDS = "«Nico: I want pizza for the party. Ema: I prefer pasta because it is easy to share. Lía: I like both, but I am vegetarian, so no meat, please. Nico: OK, pizza with cheese and tomato, then. Ema: Fine, and I bring the drinks.» (party = fiesta, prefer = prefiero, share = compartir, vegetarian = vegetariana, meat = carne, cheese = queso, drinks = bebidas)"
TOUR = "«Welcome to the Natural History Museum. The tour begins at ten thirty in the main hall. First, we visit the dinosaur room on the second floor. Then, we go to the minerals room, which is next to the cafeteria. The tour ends at noon. Please do not touch the exhibits.» (tour = visita guiada, hall = vestíbulo, dinosaur = dinosaurio, floor = piso, minerals = minerales, exhibits = piezas exhibidas)"

lesson(
    OA2, 2,
    "Los textos orales escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a encontrar información específica y detalles: quién, qué hace, dónde, cuándo y quién habla. Sirve para anotar los datos importantes de una noticia, una conversación o una visita guiada.",
    ["Sé las preguntas who, where, when y how many.", "Conozco los números hasta 10.000 en inglés."],
    [
        "La información específica (specific information) es el dato exacto que se pide: un nombre, una hora, un lugar, una cantidad. Los detalles relevantes (relevant details) se asocian a las personas y sus acciones (who does what), a los lugares (where), al tiempo (when) y a los hablantes (speakers). Cada pregunta busca un tipo de dato distinto.",
        "Cuando escuchas, prepara una tabla con cuatro columnas: who, what, where y when. Mientras escuchas, escribe solo la palabra clave, no la oración completa: por ejemplo, «7:00», «stadium», «2 goals». En una conversación con varios hablantes, anota quién dice cada cosa: las marcas Nico, Ema o Lía te ayudan a no confundirlos.",
        "Presta atención a los números y a las horas: seven o'clock es 7:00 y seven thirty es 7:30. En las cantidades, eight thousand es 8.000. Si la pregunta usa how many (cuántos), busca un número; si usa what time (a qué hora), busca una hora; si usa where, busca un lugar.",
    ],
    [("specific information", "información específica: dato exacto"), ("detail", "detalle"), ("speaker", "hablante"), ("what time", "a qué hora"), ("how many", "cuántos"), ("o'clock", "en punto")],
    [
        ("Hora y lugar", ADULT + "«The school choir has a concert on Friday at six forty-five in the library. Tickets are free.» (choir = coro, concert = concierto, tickets = entradas). ¿Dónde y a qué hora es el concierto?", ["Pregunta where: busco un lugar, la library.", "Pregunta what time: busco una hora, six forty-five.", "Six forty-five es 6:45."], "En la biblioteca a las 6:45"),
        ("Quién dice qué", ADULT + "«Paula: I want to play basketball. Hugo: I prefer swimming. Paula: But the pool is closed today.» (prefer = prefiero, pool = piscina, closed = cerrada). ¿Quién prefiere nadar?", ["Busco la palabra swimming.", "La frase I prefer swimming la dice Hugo.", "Paula quiere jugar básquetbol."], "Hugo"),
    ],
    [
        ("Anotar números sin fijarse en cuál dato pide la pregunta.", "Se mezclan las horas con las cantidades.", "Lee primero la pregunta: what time pide la hora y how many pide una cantidad."),
        ("Atribuir la frase de un hablante a otro.", "No se anotó quién habló.", "Marca el nombre de cada hablante al lado de su idea."),
    ],
    [
        (ADULT + MATCH + " ¿Dónde se jugó el partido? a) en el estadio de la ciudad b) en el colegio", "a) en el estadio de la ciudad", "Dice at the city stadium."),
        (ADULT + FRIENDS + " ¿Quién es vegetariana? a) Lía b) Ema", "a) Lía", "Ella dice I am vegetarian."),
        (ADULT + TOUR + " ¿Dónde está la sala de dinosaurios? a) en el segundo piso b) al lado de la cafetería", "a) en el segundo piso", "Dice the dinosaur room on the second floor."),
    ],
    [
        (ADULT + MATCH + " ¿A qué hora empezó el partido?", "A las siete", "Dice started at seven o'clock."),
        (ADULT + FRIENDS + " ¿Qué lleva Ema a la fiesta?", "Las bebidas", "Dice I bring the drinks."),
        (ADULT + TOUR + " ¿A qué hora termina la visita guiada?", "Al mediodía", "Dice the tour ends at noon."),
    ],
    [
        (ADULT + MATCH + " ¿Cuántos goles se anotaron en total?", "3", "Los Pumas anotaron dos y Atlético Norte uno.", "2+1"),
        (ADULT + MATCH + " ¿Qué equipo ganó el partido?", "Los Pumas", "Anotó dos goles y el otro equipo solo uno."),
        (ADULT + FRIENDS + " ¿Qué ingredientes tendrá la pizza?", "Queso y tomate", "Nico dice pizza with cheese and tomato."),
    ],
    [
        (ADULT + TOUR + " ¿Qué sala se visita primero? a) la de dinosaurios b) la de minerales", "a) la de dinosaurios", "La visita dice First, we visit the dinosaur room."),
        (ADULT + TOUR + " ¿Qué prohíbe el guía? a) tocar las piezas b) sacar fotos", "a) tocar las piezas", "Dice do not touch the exhibits."),
    ],
    [
        (ADULT + TOUR + " La visita empieza a las 10:30 y termina a las 12:00. ¿Cuántos minutos dura?", "90", "De 10:30 a 12:00 pasan una hora y media, es decir, 90 minutos.", "60+30"),
        (ADULT + MATCH + " Si de los ocho mil hinchas tres mil eran niños (dato de ejemplo), ¿cuántos eran adultos?", "5.000", "Se restan los niños del total de hinchas.", "8000-3000"),
    ],
    [(ADULT + "«Hello, this is Clara. I'm at the bus station. My bus to the beach leaves at nine fifteen from platform four. The ticket costs six thousand pesos.» (platform = andén, leaves = sale, beach = playa, costs = cuesta). ¿De qué andén sale el bus? a) del cuatro b) del cinco", "a) del cuatro", "Dice from platform four.")],
    [
        ("¿Qué pregunta pide una hora?", "What time…?", "Se responde con una hora."),
        ("¿Cómo se dice 7:30 en inglés?", "Seven thirty", "Se dicen la hora y los minutos."),
        ("¿Qué conviene anotar de cada hablante?", "Su nombre y su palabra clave", "Así no se confunden."),
    ],
    task("Un adulto lee dos veces este mensaje de voz: «Hi, this is Mr. Soto from the swimming club. Tomorrow's class is at eight a.m. (de la mañana) in the municipal pool, not in the school pool. Bring a towel and a bathing cap. The class lasts one hour.» (towel = toalla, bathing cap = gorro de baño, lasts = dura). Completa una tabla con: quién llama, a qué hora, dónde, qué llevar y cuánto dura.", "Llama el Sr. Soto del club de natación. A las ocho de la mañana, en la piscina municipal. Llevar toalla y gorro de baño. Dura una hora.", ["identifica a quien habla", "anota hora, lugar y duración correctos", "anota los dos objetos que hay que llevar"], ["tabla completa", "nota del adulto"], ["decir que es en la piscina del colegio", "olvidar el gorro de baño"], "Reconoce lo que acertó y relee con la persona solo la oración con not para corregir el lugar."),
    "Pide a un adulto que lea de nuevo la visita guiada del museo y marca cada número que oigas.",
    "Escribe una tabla con who, what, where y when de una noticia breve que hayas visto esta semana.",
)

# ---------------------------------------------------------------- clase 3: pasos y secuencia
MORNING = "«Before school, Andrés feeds his dog. After breakfast, he walks to the bus stop. While he waits, he reads a comic. When the bus arrives, he sits near the window. Finally, he gets to school at eight.» (feeds = alimenta, comic = historieta, near the window = cerca de la ventana)"
POSTER = "«How to make a poster. First, choose a topic. Second, write a big title. Next, add two pictures. Then color the letters. Finally, show the poster to the class.» (poster = afiche, topic = tema, pictures = imágenes, letters = letras)"
ROBOT = "«A robot arm builds a toy car. Step one, it takes a metal base. Step two, it puts four wheels on the base. Step three, it adds the body. After that, a person checks the car. Before the car goes to the shop, it gets a label.» (robot arm = brazo robótico, wheels = ruedas, body = carrocería, checks = revisa, label = etiqueta, shop = tienda)"

lesson(
    OA2, 3,
    "Los textos orales escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a identificar los pasos de una instrucción y la secuencia de eventos con first, second, next, then, finally, before, after y while. Sirve para seguir procedimientos y contar en orden lo que ocurrió.",
    ["Sé que first, then y finally ordenan los pasos.", "Conozco verbos como choose, add y show."],
    [
        "Una secuencia (sequence) es el orden en que ocurren las cosas. Las palabras de secuencia son first, second, third, next, then, after that y finally. Before significa antes de y after significa después de. While y when conectan dos acciones que ocurren a la vez o una tras otra: while he waits (mientras espera), when the bus arrives (cuando llega el bus).",
        "En un procedimiento, cada paso (step) comienza con un verbo: choose, write, add, color, show. Para comprender, numera los pasos mientras escuchas: 1, 2, 3. Así detectas cuál va antes y cuál después. Si no oyes una palabra de secuencia, el orden de las oraciones también te da la pista.",
        "Cuidado con before y after: «Before school, he feeds his dog» significa que lo hace antes de ir al colegio. «After breakfast, he walks» significa que camina después del desayuno. Si cambias el orden de las acciones, cambias el significado. Para comprobar, cuenta tus pasos y revisa que no falte ninguno.",
    ],
    [("sequence", "secuencia"), ("step", "paso"), ("before", "antes de"), ("after", "después de"), ("while", "mientras"), ("when", "cuando")],
    [
        ("Ordenar pasos", ADULT + "«First, wash the apples. Second, cut them into slices. Next, put them in a bowl. Finally, add a spoon of honey.» (apples = manzanas, slices = rebanadas, bowl = bol, honey = miel). ¿Qué se hace después de cortar las manzanas?", ["Busco la palabra cut: es el segundo paso.", "El paso siguiente está marcado con next.", "Dice put them in a bowl."], "Ponerlas en un bol"),
        ("Antes y después", ADULT + "«Before dinner, Sara sets the table. After dinner, she washes the plates.» (sets the table = pone la mesa, plates = platos). ¿Cuándo lava los platos?", ["Busco la palabra washes.", "La frase empieza con After dinner.", "Entonces lo hace después de la cena."], "Después de la cena"),
    ],
    [
        ("Ordenar los pasos como se oyen en la lista y no según la palabra de secuencia.", "Se ignoran first, next y finally.", "Numera los pasos con las palabras de secuencia."),
        ("Pensar que before y after significan lo mismo.", "Se confunden las dos palabras.", "Before va primero en el tiempo; after va después."),
    ],
    [
        (ADULT + MORNING + " ¿Qué hace Andrés antes de ir al colegio? a) alimenta a su perro b) lee una historieta", "a) alimenta a su perro", "Dice Before school, Andrés feeds his dog."),
        (ADULT + POSTER + " ¿Qué se hace en el primer paso? a) elegir un tema b) mostrar el afiche", "a) elegir un tema", "Dice First, choose a topic."),
        (ADULT + ROBOT + " ¿Qué recibe el auto antes de ir a la tienda? a) una etiqueta b) un motor", "a) una etiqueta", "Dice before the car goes to the shop, it gets a label."),
    ],
    [
        (ADULT + MORNING + " ¿Qué hace Andrés mientras espera el bus?", "Lee una historieta", "Dice while he waits, he reads a comic."),
        (ADULT + POSTER + " ¿Qué se colorea?", "Las letras", "Dice color the letters."),
        (ADULT + ROBOT + " ¿Cuántas ruedas pone el brazo robótico?", "4", "Dice four wheels."),
    ],
    [
        (ADULT + MORNING + " Ordena las acciones de Andrés. A) Camina al paradero. B) Llega al colegio. C) Alimenta a su perro. D) Se sienta cerca de la ventana.", "C, A, D, B", "Sigue el orden del texto: before school, after breakfast, when the bus arrives, finally."),
        (ADULT + POSTER + " ¿Qué paso va justo antes de mostrar el afiche a la clase?", "Colorear las letras", "El paso then va antes de finally."),
        (ADULT + ROBOT + " ¿Quién revisa el auto después de la carrocería?", "Una persona", "Dice After that, a person checks the car."),
    ],
    [
        (ADULT + POSTER + " Un compañero hizo el afiche así: título, tema, imágenes, mostrar. ¿Qué pasos están en el orden equivocado? a) elegir el tema y escribir el título b) agregar imágenes y mostrar", "a) elegir el tema y escribir el título", "Primero se elige el tema y después se escribe el título."),
        (ADULT + MORNING + " ¿Qué pasa cuando llega el bus?", "Andrés se sienta cerca de la ventana", "Dice when the bus arrives, he sits near the window."),
    ],
    [
        (ADULT + POSTER + " Si cada afiche lleva 2 imágenes y hay 7 afiches, ¿cuántas imágenes se necesitan?", "14", "Se multiplican las imágenes de cada afiche por el número de afiches.", "2*7"),
        (ADULT + ROBOT + " El robot arma 5 autos y cada uno lleva 4 ruedas. ¿Cuántas ruedas usa en total?", "20", "Cada auto lleva cuatro ruedas.", "5*4"),
    ],
    [(ADULT + "«Before you swim in the pool, take a shower. While you swim, stay in your lane. After you swim, dry your hair.» (take a shower = ducharse, lane = carril, dry = secar). ¿Cuándo debes ducharte? a) antes de nadar b) después de nadar", "a) antes de nadar", "Dice Before you swim, take a shower.")],
    [
        ("En una secuencia oral, ¿qué indica la palabra after?", "Después de", "Indica lo que ocurre más tarde."),
        ("En una instrucción oral, ¿qué palabra de secuencia cierra los pasos?", "finally", "Cierra la secuencia."),
        ("¿Qué conviene hacer mientras escuchas un procedimiento?", "Numerar los pasos", "Así se mantiene el orden."),
    ],
    task("Un adulto lee dos veces estas instrucciones: «How to prepare a class timetable. First, write the days of the week. Second, write the hours in the first column. Next, write the subjects in the boxes. Then use a different color for each subject. Finally, hang the timetable above your desk.» (timetable = horario, boxes = casillas, subjects = asignaturas, hang = colgar, above = sobre). Numera los cinco pasos en español y marca con una flecha cuál va antes y cuál después de «use a different color».", "1. Escribir los días. 2. Escribir las horas. 3. Escribir las asignaturas. 4. Usar un color para cada asignatura. 5. Colgar el horario. Antes del color va escribir las asignaturas; después va colgar.", ["numera los cinco pasos en el orden correcto", "señala el paso anterior y el siguiente", "usa las palabras de secuencia"], ["lista numerada", "nota del adulto"], ["poner colgar el horario antes del color", "no escribir las horas"], "Reconoce lo que acertó y subraya con la persona las palabras de secuencia para reconstruir el orden."),
    "Pide a un adulto que lea de nuevo la rutina de Andrés y dibuja tres escenas en orden.",
    "Escribe tu rutina de la mañana usando before, after y finally.",
)

# ---------------------------------------------------------------- clase 4: hecho/opinión y causa-efecto
GARDEN = "«Our school garden has twelve tomato plants. I think the garden is beautiful. The tomatoes are red because they are ripe. In my opinion, they taste better than store tomatoes. Plants need water, so we water them every morning.» (tomato plants = plantas de tomate, ripe = maduros, taste = saben, store = tienda, water = regar)"
CITY = "«The new library opened last Monday. It has four floors and a big reading room. Some people say it is the best building in the city. The library is crowded because many students need a quiet place to study. I believe more libraries are important.» (opened = abrió, reading room = sala de lectura, crowded = llena de gente, quiet = silencioso)"
GAME = "«Our team lost the match because two players were sick. The coach was sad, so he gave a short speech. He said: We played badly, but the next game will be great. I think he is a good coach.» (lost = perdió, players = jugadores, sick = enfermos, coach = entrenador, speech = discurso)"

lesson(
    OA2, 4,
    "Los textos orales escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a diferenciar un hecho de una opinión y a reconocer relaciones de causa y efecto con because y so. Sirve para saber qué datos se pueden comprobar y qué es solo lo que alguien piensa.",
    ["Sé que because significa porque.", "Conozco verbos como think, believe y need."],
    [
        "Un hecho (fact) es un dato que se puede comprobar: «The garden has twelve tomato plants». Una opinión (opinion) es lo que una persona piensa o siente y no se puede medir: «The garden is beautiful». Las opiniones suelen llevar frases como I think, I believe, in my opinion y palabras como best, beautiful, better o important.",
        "La relación de causa y efecto (cause and effect) explica por qué pasa algo. La causa es el motivo; el efecto es el resultado. Because (porque) va antes de la causa: «The tomatoes are red because they are ripe». So (por eso, así que) va antes del efecto: «Plants need water, so we water them». Si lees dos oraciones con because y so, identifica cuál es la causa y cuál es el efecto.",
        "Para decidir si algo es hecho u opinión, pregúntate: ¿puedo comprobarlo contando, midiendo o buscando una prueba? Si la respuesta es sí, es un hecho. Si depende de quién lo diga, es una opinión. Una opinión puede ser razonable, pero no es un dato que se compruebe.",
    ],
    [("fact", "hecho: dato comprobable"), ("opinion", "opinión: lo que alguien piensa"), ("cause", "causa: el motivo"), ("effect", "efecto: el resultado"), ("because", "porque"), ("so", "por eso, así que")],
    [
        ("Hecho u opinión", ADULT + "«The museum has three floors. I think the museum is boring.» (floors = pisos, boring = aburrido). ¿Cuál es el hecho y cuál la opinión?", ["Pregunto si puedo comprobar cada oración.", "Puedo contar los pisos: es un hecho.", "Boring depende de quién lo diga: es una opinión."], "Hecho: tiene tres pisos. Opinión: es aburrido"),
        ("Causa y efecto", ADULT + "«The bus was late because it rained. As a result, we arrived at nine.» (late = tarde, rained = llovió). ¿Cuál es la causa de que el bus llegara tarde?", ["Busco la palabra because.", "Después de because dice it rained.", "La lluvia es la causa."], "Que llovió"),
    ],
    [
        ("Creer que toda oración con un número es un hecho.", "No se verifica si la información se puede comprobar.", "Comprueba si el dato se puede contar o medir."),
        ("Poner el efecto después de because.", "Se confunden causa y efecto.", "Después de because va la causa."),
    ],
    [
        (ADULT + GARDEN + " ¿Cuál es un hecho? a) El huerto tiene doce plantas de tomate b) El huerto es hermoso", "a) El huerto tiene doce plantas de tomate", "Se puede contar; hermoso es una opinión."),
        (ADULT + CITY + " ¿Cuál es una opinión? a) La nueva biblioteca es el mejor edificio de la ciudad b) La biblioteca tiene cuatro pisos", "a) La nueva biblioteca es el mejor edificio de la ciudad", "Best depende de quién lo diga."),
        (ADULT + GAME + " ¿Por qué perdió el equipo? a) porque dos jugadores estaban enfermos b) porque llovió", "a) porque dos jugadores estaban enfermos", "Dice because two players were sick."),
    ],
    [
        (ADULT + GARDEN + " ¿Por qué los tomates son rojos?", "Porque están maduros", "Dice they are ripe."),
        (ADULT + CITY + " ¿Por qué la biblioteca está llena de gente?", "Porque muchos estudiantes necesitan un lugar silencioso para estudiar", "Dice many students need a quiet place to study."),
        (ADULT + GAME + " ¿Qué hizo el entrenador porque estaba triste?", "Dio un discurso corto", "Dice The coach was sad, so he gave a short speech."),
    ],
    [
        (ADULT + GARDEN + " Marca las dos opiniones. A) I think the garden is beautiful. B) The tomatoes are red. C) In my opinion, they taste better than store tomatoes. D) We water them every morning.", "A y C", "Beautiful y better son juicios personales."),
        (ADULT + CITY + " ¿Qué frase del texto introduce una opinión? a) I believe b) opened last Monday", "a) I believe", "I believe expresa lo que piensa quien habla."),
        (ADULT + GAME + " ¿Cuál es el efecto de que dos jugadores estuvieran enfermos?", "El equipo perdió", "La causa es que estaban enfermos y el efecto es la derrota."),
    ],
    [
        (ADULT + GARDEN + " En «Plants need water, so we water them», ¿cuál es la causa? a) las plantas necesitan agua b) las regamos todas las mañanas", "a) las plantas necesitan agua", "So va antes del efecto; la causa es lo primero."),
        (ADULT + CITY + " Un compañero dice que es un hecho que la biblioteca es el mejor edificio. ¿Tiene razón? Responde sí o no.", "No", "Es una opinión que dicen algunas personas y no se puede comprobar."),
    ],
    [
        (ADULT + GARDEN + " Supón que cada planta necesita 3 litros de agua por semana (dato de ejemplo). Con 12 plantas, ¿cuántos litros se necesitan por semana?", "36", "Se multiplica el agua de cada planta por el número de plantas.", "3*12"),
        (ADULT + CITY + " Supón que la biblioteca tiene 4 pisos y que cada piso tiene 25 mesas (dato de ejemplo). ¿Cuántas mesas hay en total?", "100", "Se multiplica el número de mesas por el de pisos.", "4*25"),
    ],
    [(ADULT + "«The park is closed today because it is windy. Many people think the park is the best place in town. The park has a pond and two playgrounds.» (windy = ventoso, pond = estanque, playgrounds = áreas de juego). ¿Cuál es el motivo del cierre? a) hace mucho viento b) hay una reparación", "a) hace mucho viento", "Dice it is closed because it is windy.")],
    [
        ("Al escuchar a alguien, ¿se puede comprobar una opinión como «it is boring»?", "No", "Depende de quién la diga."),
        ("¿Qué palabra introduce la causa?", "because", "Va antes del motivo."),
        ("¿Qué expresión en inglés anuncia que alguien da su opinión?", "I think", "Muestra lo que alguien piensa."),
    ],
    task("Un adulto lee dos veces este texto: «The school pool has six lanes and is twenty-five meters long. I think swimming is the most fun sport. The pool is closed on Mondays because the water needs cleaning. So the swimming club trains on Tuesdays.» (lanes = carriles, meters = metros, trains = entrena, cleaning = limpieza). Escribe en tu hoja: dos hechos, una opinión y una relación de causa y efecto con la palabra because o so.", "Hechos: tiene seis carriles; mide 25 metros. Opinión: nadar es el deporte más divertido. Causa y efecto: la piscina cierra los lunes porque el agua necesita limpieza.", ["escribe dos hechos comprobables", "identifica una opinión", "escribe una causa y su efecto"], ["hoja con respuestas", "nota del adulto"], ["poner una opinión como hecho", "invertir la causa y el efecto"], "Reconoce lo que acertó y pide a la persona que compruebe cada oración preguntando si se puede medir."),
    "Pide a un adulto que lea el partido perdido y subraya con dos colores la causa y el efecto.",
    "Escribe en español dos hechos y dos opiniones sobre tu colegio.",
)

# ---------------------------------------------------------------- clase 5: conectores y sonidos /z/, /s/ y /h/
BELL = "«When the bell rings, we go to the yard. Do you want tea or juice? I like music too. While I cook, my brother sets the table.» (bell = timbre, rings = suena, yard = patio, tea = té, cook = cocinar, sets the table = pone la mesa)"
TIMETABLE = "«Hello, students. This week we have two tests. The science test is on Tuesday, and the English test is on Thursday. You can bring a pen or a pencil. After the test, we will watch a short film.» (tests = pruebas, bring = traer, pen = lápiz pasta, pencil = lápiz grafito, film = película)"
POOL = "«Today I will talk about my hobby. I like swimming because it is relaxing. When I swim, I forget my problems. I swim every Saturday, and my sister swims too. After the lesson, we eat fruit or a sandwich.» (hobby = pasatiempo, relaxing = relajante, forget = olvido, lesson = clase)"

lesson(
    OA2, 5,
    "Los textos orales y las listas de palabras escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a reconocer los conectores or, too, when y while en textos orales, y a distinguir los sonidos /z/, /s/ y /h/. Sirve para entender cómo se unen las ideas y pronunciar mejor palabras como zoo, sad, hot y hour.",
    ["Sé que and une ideas.", "Conozco palabras como zoo, bus, house y hour."],
    [
        "Los conectores (connectors) unen ideas. Or ofrece una opción: tea or juice. Too significa también y va al final: I like music too. When significa cuando y while significa mientras: while I cook (mientras cocino) indica dos acciones a la vez. Before y after indican orden (antes y después), y because indica causa.",
        "Los sonidos también ayudan a comprender. El sonido /s/ es como la s de «sad» o «bus». El sonido /z/ vibra como una abeja: zoo, rose, dogs. La terminación -s suena /z/ después de sonidos con voz (dogs, bags, pens) y suena /s/ después de sonidos sin voz (cats, books, cups). Toca tu garganta: si vibra, es /z/. (Después de s, z, sh o ch, como en buses o watches, la terminación se dice /iz/, con una sílaba más.)",
        "El sonido /h/ al inicio se pronuncia con un soplo, como en hot, house o hat. Pero hay palabras con h muda (silent h): hour se pronuncia como «our» y honest como «onest». Por eso se dice «an hour» y no «a hour». Cuando oigas un par parecido, como sip/zip o ice/eyes, fíjate en la vibración de tu garganta y en el soplo de la h.",
    ],
    [("or", "o: ofrece una opción"), ("too", "también (al final)"), ("while", "mientras"), ("/s/ y /z/", "sonidos de sad (sin vibración) y zoo (con vibración)"), ("/h/", "soplo inicial como en hot"), ("silent h", "h muda: hour, honest")],
    [
        ("Conector or", ADULT + "«Would you like a bus or a taxi? A bus is cheaper.» (cheaper = más barato). ¿Qué dos opciones se ofrecen?", ["Busco la palabra or.", "Une a bus y a taxi.", "Son las dos opciones."], "Un bus y un taxi"),
        ("Sonido de la -s", "¿Qué sonido tiene la -s final de «dogs» y qué sonido tiene la de «cats»?", ["Dogs termina en g, un sonido con voz: la -s suena /z/.", "Cats termina en t, un sonido sin voz: la -s suena /s/.", "Compruébalo tocando tu garganta."], "dogs termina con /z/ y cats termina con /s/"),
    ],
    [
        ("Decir «a hour» porque la palabra empieza con h.", "No se reconoce la h muda.", "Hour suena como «our»: se dice an hour."),
        ("Pronunciar siempre la -s plural como /s/.", "No se distingue la vibración.", "Después de sonidos con voz, como dogs o bags, suena /z/."),
    ],
    [
        (ADULT + BELL + " ¿Qué hacemos cuando suena el timbre? a) vamos al patio b) cocinamos", "a) vamos al patio", "Dice when the bell rings, we go to the yard."),
        (ADULT + TIMETABLE + " ¿Qué se puede traer a la prueba? a) un lápiz pasta o un lápiz grafito b) solo un libro", "a) un lápiz pasta o un lápiz grafito", "Dice You can bring a pen or a pencil."),
        ("¿Qué palabra tiene el sonido /z/ al inicio? a) zoo b) sad", "a) zoo", "Zoo empieza con /z/ y sad empieza con /s/."),
    ],
    [
        (ADULT + BELL + " ¿Qué hace el hermano mientras la persona cocina?", "Pone la mesa", "Dice while I cook, my brother sets the table."),
        (ADULT + TIMETABLE + " ¿Qué prueba es el jueves?", "La de inglés", "Dice the English test is on Thursday."),
        ("¿Cuál de estas palabras empieza con el sonido /h/? a) house b) hour", "a) house", "En house se pronuncia la h y en hour la h es muda."),
    ],
    [
        (ADULT + POOL + " ¿Quién nada también los sábados?", "La hermana", "Dice my sister swims too."),
        (ADULT + POOL + " ¿Qué comen después de la clase?", "Fruta o un sándwich", "Dice we eat fruit or a sandwich."),
        ("Elige la palabra con el sonido /s/ final. a) bus b) buzz", "a) bus", "Bus termina con /s/ y buzz con /z/."),
    ],
    [
        ("¿Qué plural termina con /z/? a) bags b) books", "a) bags", "Bags termina en g, un sonido con voz; books termina en k, sin voz."),
        (ADULT + BELL + " Un compañero dice que «too» significa «muy» en «I like music too». ¿Qué significa en esa oración?", "También", "Too al final significa también."),
    ],
    [
        ("Cuenta cuántas palabras de esta lista terminan con el sonido /z/: dogs, cats, bags, cups, pens.", "3", "Dogs, bags y pens terminan con /z/; cats y cups terminan con /s/."),
        ("Cuenta cuántas palabras de esta lista tienen h muda: hour, house, honest, hat, hot.", "2", "Hour y honest tienen h muda; las otras tres tienen /h/."),
    ],
    [(ADULT + "«Do you want to go to the zoo on Saturday or on Sunday? I can go on Sunday, and my cousin can too.» (cousin = primo). ¿Qué día pueden ir las dos personas? a) el domingo b) el sábado", "a) el domingo", "Dice I can go on Sunday, and my cousin can too.")],
    [
        ("¿Qué conector significa «también»?", "too", "Va al final de la oración."),
        ("¿Cómo se pronuncia hour?", "Como our", "La h es muda."),
        ("¿Qué conector indica dos acciones a la vez?", "while", "While significa mientras y une dos acciones simultáneas."),
    ],
    task("Un adulto lee dos veces: «On Friday, I walk to school when it is sunny. While I walk, I listen to music. At noon, I have soup or salad. My friend has salad too.» (sunny = soleado, soup = sopa, salad = ensalada). Escribe en tu hoja: qué hace la persona mientras camina, qué opciones tiene a mediodía y cuál es su condición para ir caminando. Después lee en voz alta estas palabras y marca las que tienen /z/ al final: bags, cats, pens, cups.", "Mientras camina, escucha música. A mediodía hay sopa o ensalada. Camina cuando está soleado. Con /z/: bags y pens.", ["responde con los conectores while, or y when", "identifica las dos palabras con /z/", "no inventa datos"], ["hoja con respuestas", "nota del adulto"], ["decir que camina cuando llueve", "marcar cats como /z/"], "Reconoce lo que acertó y practica con la persona tocar la garganta para sentir la vibración de /z/."),
    "Pide a un adulto que lea las palabras zoo, sad, hot y hour sin mostrarte el papel; escríbelas y revisa.",
    "Escribe dos oraciones en inglés con or y too, usando comida que te gusta.",
)
