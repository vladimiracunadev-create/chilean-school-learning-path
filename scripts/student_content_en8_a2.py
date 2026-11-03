"""Cuaderno del estudiante, 8.º básico Inglés (propuesta), EN08 OA 02 (propósito, detalles y relaciones en textos orales).

Las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan pista en español. Las clases del plan tienen títulos genéricos; aquí cada clase trabaja un grupo de contenidos que nombra el OA.
"""
from __future__ import annotations

from student_content_en8_a import ADULT, lesson, task
from student_lessons import arith

OA2 = "EN08 OA 02"

# ---------------------------------------------------------------- clase 1: propósito, tema e ideas generales
PLASTIC = "«Many cities around the world have a problem: too much plastic. Plastic bags can stay in the ocean for a long time and hurt sea animals. Some cities now ask shoppers to bring their own cloth bags. This simple idea helps the planet.» (ocean = océano, hurt = dañar, sea animals = animales marinos, shoppers = compradores, cloth bags = bolsas de tela, planet = planeta)"
DESERT = "«Last July, my family and I visited the Atacama Desert. It was very dry, and the sky at night was full of stars. My sister took many photos. I learned that some plants can live there even with very little rain.» (desert = desierto, dry = seco, full of = lleno de, stars = estrellas, little rain = poca lluvia)"
RAPA = "«Rapa Nui is an island in the Pacific Ocean. It belongs to Chile. It is famous for its big stone statues called moai. Every year many tourists visit the island.» (island = isla, belongs to = pertenece a, famous = famosa, statues = estatuas, tourists = turistas)"
CLUB = "«Do you want to be a better reader? Join our reading club! We meet every Thursday after school in the library. It is free, and you can bring a friend. Don't miss it!» (better = mejor, join = únete, free = gratis, bring = traer, miss = perderse)"

lesson(
    OA2, 1,
    "Los textos breves escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a identificar el propósito, el tema y las ideas generales de un texto oral, aunque trate de una experiencia personal, de otra asignatura o de un problema global. Sirve para entender de qué trata un mensaje antes de buscar los detalles.",
    ["Sé distinguir una anécdota de un noticiero.", "Conozco palabras como because, so y also."],
    [
        "El propósito (purpose) es lo que quiere lograr quien habla: informar (inform), invitar (invite), convencer (persuade) o contar una experiencia (share an experience). El tema (topic) es de qué se habla, por ejemplo «el plástico» o «un viaje al desierto». Las ideas generales (main ideas) son los mensajes más importantes que dice el texto, y se pueden resumir en una o dos oraciones.",
        "Los temas pueden venir de tu vida (un viaje), de otras asignaturas (geografía, ciencias) o del mundo actual (el plástico en el mar). Las pistas del propósito están en frases típicas: «Join our club!» invita y convence; «Last July, I visited…» comparte una experiencia; «Many cities have a problem» presenta un tema de actualidad. Las palabras repetidas indican el tema: si oyes plastic tres veces, el tema es el plástico.",
        "Para entender el texto global, no trates de traducir cada palabra. Escucha una vez completa, pregunta «¿de qué hablan?» y «¿para qué lo dicen?», y recién después busca los detalles. Un detalle (detail) es un dato menor, como un mes o un color. Un error común es responder con un detalle cuando se pide la idea principal.",
    ],
    [("purpose", "propósito: para qué se habla"), ("topic", "tema: de qué se habla"), ("main idea", "idea principal o general"), ("detail", "detalle: un dato menor"), ("persuade", "convencer"), ("inform", "informar")],
    [
        ("Propósito de un aviso", ADULT + CLUB + " ¿Cuál es el propósito del mensaje?", ["Busco verbos en orden: join y don't miss it.", "Piden que alguien se una a un club.", "Eso es invitar y convencer."], "Invitar y convencer para que se unan al club de lectura"),
        ("Tema de un texto de otra asignatura", ADULT + RAPA + " ¿Cuál es el tema?", ["Busco las palabras que se repiten: island y Rapa Nui.", "Todas las frases hablan de esa isla.", "El tema es la isla y lo que la hace famosa."], "La isla de Rapa Nui y sus estatuas"),
    ],
    [
        ("Responder con un detalle (la fecha) cuando se pide la idea principal.", "Se confunde un dato menor con el mensaje central.", "Pregunta primero de qué habla todo el texto; después revisa los detalles."),
        ("Pensar que un texto con un problema global solo informa.", "No se mira si pide una acción.", "Revisa si el hablante propone una solución o pide algo (Some cities ask…): eso agrega un propósito de persuadir."),
    ],
    [
        (ADULT + PLASTIC + " ¿Cuál es el tema? a) el plástico y el océano b) los animales del desierto", "a) el plástico y el océano", "La palabra plastic aparece varias veces y se habla del ocean."),
        (ADULT + DESERT + " ¿Qué tipo de texto es? a) una experiencia personal b) un aviso para un club", "a) una experiencia personal", "Dice Last July, my family and I visited."),
        (ADULT + CLUB + " ¿Cuándo se reúne el club? a) los jueves después de clases b) los lunes antes de clases", "a) los jueves después de clases", "El guion dice every Thursday after school."),
    ],
    [
        (ADULT + PLASTIC + " ¿Qué solución se menciona? a) usar bolsas de tela b) quemar las bolsas", "a) usar bolsas de tela", "Dice Some cities ask shoppers to bring their own cloth bags."),
        (ADULT + RAPA + " ¿Cuál es la idea general del texto? a) Rapa Nui es una isla chilena famosa por sus moai b) Rapa Nui es una isla del océano Atlántico famosa por sus moai", "a) Rapa Nui es una isla chilena famosa por sus moai", "Resume los datos que se repiten en el texto."),
        (ADULT + DESERT + " ¿Qué aprendió la persona que cuenta? a) que algunas plantas viven con poca lluvia b) que el desierto tiene mucho pasto", "a) que algunas plantas viven con poca lluvia", "Dice I learned that some plants can live there with very little rain."),
    ],
    [
        (ADULT + DESERT + " ¿Dónde estaba la familia en julio? a) en el desierto de Atacama b) en la playa", "a) en el desierto de Atacama", "El guion dice visited the Atacama Desert."),
        (ADULT + RAPA + " ¿A qué país pertenece Rapa Nui?", "A Chile", "El guion dice It belongs to Chile."),
        (ADULT + CLUB + " ¿Qué propósito tiene decir «Don't miss it»? a) animar a asistir b) avisar que el club cerró", "a) animar a asistir", "Don't miss it significa no te lo pierdas."),
    ],
    [
        (ADULT + PLASTIC + " ¿Cuál es el propósito del texto? a) presentar un problema y una solución sencilla b) vender bolsas plásticas", "a) presentar un problema y una solución sencilla", "Parte con un problema y termina con una idea que ayuda al planeta."),
        (ADULT + CLUB + " Una compañera dice que el club cobra una entrada. ¿Qué dato del guion la corrige?", "It is free", "El guion dice que es gratis."),
    ],
    [
        (ADULT + DESERT + " ¿Cuál de estos es un detalle y no la idea principal? a) My sister took many photos b) The family visited the Atacama Desert", "a) My sister took many photos", "Es un dato menor; la idea principal es la visita al desierto."),
        ("Une cada frase con su propósito. 1) «Join our club!» 2) «Last July, I visited the desert.» 3) «Plastic hurts sea animals.» Propósitos: a) informar de un problema b) compartir una experiencia c) invitar", "1-c, 2-b, 3-a", "Join invita, Last July abre una experiencia y hurts sea animals informa un problema."),
    ],
    [(ADULT + "«Good morning, class. Today we will study the water cycle. Water goes up as vapor, forms clouds and comes down as rain. This cycle repeats all the time.» (water cycle = ciclo del agua, vapor = vapor, clouds = nubes, comes down = baja). Un profesor habla en una clase de ciencias. ¿Cuál es su propósito? a) explicar el ciclo del agua b) invitar a un paseo", "a) explicar el ciclo del agua", "Introduce un tema de ciencias y describe sus partes.")],
    [
        ("¿Qué es el tema de un texto?", "De qué se habla", "El tema responde a qué trata el texto."),
        ("¿Qué propósito tiene el aviso «Join our reading club»?", "Invitar", "Pide que alguien se una."),
        ("¿Qué palabra repetida te ayuda a descubrir el tema?", "Plastic, en el texto del plástico", "Lo que más se repite indica el tema."),
    ],
    task("Un adulto lee dos veces este texto: «Hello, everybody. Tomorrow is Earth Day. At eleven o'clock, we will plant ten trees in the school yard. Please bring a bottle of water. We need your help!» (Earth Day = Día de la Tierra, plant = plantar, yard = patio, bottle = botella, help = ayuda). En tu hoja escribe el tema, el propósito y dos detalles del guion.", "Tema: plantar árboles en el Día de la Tierra. Propósito: invitar a ayudar. Detalles: a las once; diez árboles; se debe llevar una botella de agua.", ["identifica el tema", "indica un propósito coherente", "escribe dos detalles exactos"], ["hoja con tema, propósito y detalles", "nota del adulto"], ["escribir un detalle como si fuera el tema", "no anotar ninguna cifra o hora"], "Reconoce lo que acertó y relee con la persona solo la primera y la última oración para decidir tema y propósito."),
    "Pide a un adulto que lea otra vez el texto de Rapa Nui y anota con tus palabras la idea principal y dos detalles.",
    "Escribe en español cómo explicarías a un amigo la diferencia entre el tema y el propósito de un texto.",
)

# ---------------------------------------------------------------- clase 2: información específica y detalles
TRIP = "«Good morning, students. This is Mrs. Lagos. On Friday, October twentieth, we will visit the botanical garden. The bus leaves at eight fifteen from the main gate. Please wear a hat and bring a lunch and a bottle of water. We will return to school at three thirty.» (botanical garden = jardín botánico, leaves = sale, gate = portón, hat = sombrero, lunch = almuerzo, return = volvemos)"
CHAT = "«Matías: Why are you tired, Camila? Camila: Because I helped my uncle in his bakery this morning. We made two hundred rolls. Matías: Wow! Did you eat some? Camila: Of course! But my favorite is the sweet bread with jam.» (tired = cansada, bakery = panadería, rolls = panes, of course = por supuesto, sweet bread = pan dulce, jam = mermelada)"
BIKE = "«On Saturday afternoon, Isabel was riding her bike in the park. A small dog ran in front of her, so she stopped quickly. Then a man called the dog and said sorry. Isabel smiled and continued her ride.» (riding = andando en, ran = corrió, stopped = frenó, called = llamó, said sorry = pidió disculpas, continued = siguió)"

lesson(
    OA2, 2,
    "Los textos breves y diálogos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a ubicar información específica y detalles relevantes: personas y sus acciones, lugares, tiempo, hablantes y situaciones. Sirve para responder preguntas exactas sobre lo que escuché.",
    ["Sé las palabras who, where, when y what.", "Sé los días, los meses y las horas en inglés."],
    [
        "La información específica (specific information) es el dato exacto que responde una pregunta: quién (who) hizo algo, qué (what) hizo, dónde (where), cuándo (when) y cómo (how). Los hablantes (speakers) son las personas que hablan; en un diálogo, cada uno aparece con su nombre antes de hablar. La situación (situation) es el contexto: una reunión, una panadería, un paseo.",
        "Para encontrar un dato, primero lee la pregunta y decide qué tipo de palabra buscas. Un lugar aparece con at, in, near o to (at the main gate). Un tiempo, con on, at y los números (on Friday, at eight fifteen). Una persona, con un nombre o un título (Mrs. Lagos). Una acción, con un verbo (helped, stopped, continued).",
        "Al escuchar un diálogo, anota las iniciales de cada hablante y lo que dice cada uno. Así no confundes quién hizo qué. Cuando una respuesta tiene un número, escríbelo en cifras. Si oyes two hundred, anota 200. Revisa en la segunda escucha: los números y las horas se confunden fácilmente.",
    ],
    [("specific information", "información específica: el dato exacto"), ("speaker", "hablante"), ("situation", "situación: el contexto"), ("detail", "detalle relevante"), ("at the gate", "en el portón"), ("return", "regresar")],
    [
        ("Encontrar un lugar y una hora", ADULT + TRIP + " ¿A qué hora sale el bus y desde dónde?", ["Busco una hora: eight fifteen.", "Busco un lugar con from: from the main gate.", "Uno ambos datos."], "A las 8:15, desde el portón principal"),
        ("Encontrar qué hablante hizo algo", ADULT + CHAT + " ¿Quién ayudó en la panadería y cuántos panes hicieron?", ["La persona es Camila, porque dice I helped my uncle.", "La cifra es two hundred rolls.", "Two hundred se escribe 200."], "Camila ayudó a su tío y hicieron 200 panes"),
    ],
    [
        ("Anotar «eight fifty» cuando el guion dice «eight fifteen».", "Se confunden fifteen y fifty.", "Fifteen termina en -teen con acento al final; fifty, en la primera sílaba. Confirma con el contexto."),
        ("Atribuir a Matías lo que dijo Camila.", "No se marca quién habla.", "Anota la inicial de cada hablante antes de su frase."),
    ],
    [
        (ADULT + TRIP + " ¿Cuándo es la salida? a) el viernes 20 de octubre b) el jueves 2 de octubre", "a) el viernes 20 de octubre", "El guion dice Friday, October twentieth."),
        (ADULT + TRIP + " ¿A qué lugar van los estudiantes? a) al jardín botánico b) a la playa", "a) al jardín botánico", "El guion dice we will visit the botanical garden."),
        (ADULT + BIKE + " ¿Dónde andaba Isabel en bicicleta?", "En el parque", "El guion dice in the park."),
    ],
    [
        (ADULT + TRIP + " ¿Qué deben llevar los estudiantes? a) sombrero, almuerzo y una botella de agua b) un traje de baño y una pelota", "a) sombrero, almuerzo y una botella de agua", "El guion dice wear a hat and bring a lunch and a bottle of water."),
        (ADULT + CHAT + " ¿Cuál es el pan favorito de Camila? a) el pan dulce con mermelada b) el pan integral", "a) el pan dulce con mermelada", "Dice my favorite is the sweet bread with jam."),
        (ADULT + BIKE + " ¿Por qué frenó Isabel?", "Porque un perro pequeño cruzó delante de ella", "Dice A small dog ran in front of her, so she stopped quickly."),
    ],
    [
        (ADULT + CHAT + " ¿Por qué está cansada Camila? a) porque ayudó en la panadería de su tío b) porque estudió toda la noche", "a) porque ayudó en la panadería de su tío", "Dice Because I helped my uncle in his bakery."),
        (ADULT + BIKE + " ¿En qué momento andaba Isabel en bicicleta?", "El sábado en la tarde", "El guion dice On Saturday afternoon."),
        (ADULT + TRIP + " ¿Quién habla en el aviso? a) la Sra. Lagos b) el director", "a) la Sra. Lagos", "Se presenta con This is Mrs. Lagos."),
    ],
    [
        (ADULT + TRIP + " La profesora dice que vuelven a las 3:30. Un estudiante anotó las 3:13. ¿Qué anotó mal? a) confundió thirty con thirteen b) no entendió la palabra bus", "a) confundió thirty con thirteen", "Three thirty es 3:30, no 3:13."),
        (ADULT + CHAT + " ¿Quién pregunta si comió pan: Matías o Camila?", "Matías", "Él dice Did you eat some?"),
    ],
    [
        arith(ADULT + TRIP + " El bus sale a las 8:15. ¿Cuántos minutos faltan desde las 8:15 hasta las 9:00?", "60-15", "De 8:15 a 9:00 faltan 45 minutos; se resta 15 a 60."),
        (ADULT + BIKE + " ¿Qué hizo el hombre después de que Isabel frenó? a) llamó a su perro y pidió disculpas b) se fue sin decir nada", "a) llamó a su perro y pidió disculpas", "El guion dice a man called the dog and said sorry."),
    ],
    [(ADULT + "«Customer: Excuse me, how much is this notebook? Clerk: It costs three thousand five hundred pesos. Customer: And the pencil case? Clerk: Two thousand pesos. Customer: I'll take both.» (notebook = cuaderno, pencil case = estuche, clerk = vendedor, how much is = cuánto cuesta, costs = cuesta, I'll take both = me llevo los dos). ¿Cuánto pagará el cliente por los dos productos en pesos?", "5.500", "Se suman 3.500 y 2.000.")],
    [
        ("¿Qué tipo de palabra buscas si la pregunta es «When…?»?", "Un día o una hora", "When pregunta por el tiempo."),
        ("¿Qué hace cada hablante en un diálogo?", "Habla por turnos", "Por eso se anota quién dijo cada frase."),
        ("¿Cuál es la hora en «eight fifteen»?", "8:15", "Se escribe con cifras para no confundirse."),
    ],
    task("Un adulto lee dos veces este diálogo: «Teacher: Sebastián, where is your science project? Sebastián: I left it at home, but my father is bringing it at twelve fifteen. Teacher: Okay. Please put it on the table near the window. Sebastián: Thank you, miss.» (left = dejé, bringing = trayendo, table = mesa, window = ventana). En tu hoja escribe: quiénes hablan, el problema, la hora y el lugar donde dejarán el proyecto.", "Hablan una profesora y Sebastián. El problema: dejó el proyecto en casa. Hora: 12:15. Lugar: la mesa cerca de la ventana.", ["nombra los dos hablantes", "indica el problema y la hora exacta", "indica el lugar con las dos pistas (table y near the window)"], ["hoja con cuatro datos", "nota del adulto"], ["confundir quién habla", "anotar 12:50 en vez de 12:15"], "Reconoce lo que acertó y relee con la persona solo los números y las preposiciones de lugar para corregir los datos."),
    "Pide a un adulto que lea otra vez la salida al jardín botánico y completa una tabla con día, lugar, hora y objetos.",
    "Escribe en español qué preguntas harías para obtener quién, dónde y cuándo de un aviso del colegio.",
)

# ---------------------------------------------------------------- clase 3: pasos, secuencia y hecho versus opinión
GARDEN = "«How to start a vegetable garden at school. First, choose a sunny place. Then loosen the soil with a small shovel. Next, plant the seeds. Water them until the soil is wet. Finally, put a label with the name of the plant.» (vegetable garden = huerto, sunny = soleado, loosen = remover, soil = tierra, shovel = pala, seeds = semillas, until = hasta que, label = etiqueta)"
OPINIONS = "«Our school has two hundred students. I think English is the most interesting subject. The library opens at eight. In my opinion, the school lunch is delicious. The gym is next to the yard.» (opinion = opinión, interesting = interesante, subject = asignatura, opens = abre, delicious = delicioso, gym = gimnasio)"
RACE = "«First, the runners stood at the starting line. Then the teacher blew the whistle. After that, they ran two laps around the field. Finally, the winner received a medal.» (runners = corredores, starting line = línea de partida, whistle = silbato, laps = vueltas, field = cancha, winner = ganador, medal = medalla)"

lesson(
    OA2, 3,
    "Los textos breves escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a identificar los pasos de instrucciones y procedimientos, la secuencia de eventos y la diferencia entre un hecho y una opinión. Sirve para seguir indicaciones y no confundir lo comprobable con lo que alguien piensa.",
    ["Sé first, second, next, then y finally.", "Conozco I think y in my opinion."],
    [
        "Un procedimiento (procedure) es una serie de pasos. Las palabras first, then, next, after that y finally te dicen el orden. El conector until (hasta que) marca la condición para detener una acción: «Water them until the soil is wet». La secuencia de eventos (sequence) es el orden en que ocurrieron las cosas: primero uno, luego otro. Escucha esas palabras y numera los pasos.",
        "Un hecho (fact) se puede comprobar: contar, medir o buscar. «The library opens at eight» es un hecho. Una opinión (opinion) expresa lo que alguien piensa o siente y no se puede comprobar: «I think English is interesting», «In my opinion, the lunch is delicious». Las señales de opinión son I think, in my opinion, I believe y adjetivos como delicious, boring, best, interesting.",
        "Para no confundirte, haz dos preguntas. Si se trata de pasos, ¿qué palabra marca el orden? Si se trata de una frase, ¿se puede comprobar con un dato, una medida o un documento? Si la respuesta es sí, es un hecho. Si depende de lo que cada persona piensa, es una opinión.",
    ],
    [("fact", "hecho: se puede comprobar"), ("opinion", "opinión: lo que alguien piensa"), ("sequence", "secuencia: el orden de los hechos"), ("until", "hasta que"), ("after that", "después de eso"), ("procedure", "procedimiento: pasos ordenados")],
    [
        ("Seguir el orden de los pasos", ADULT + GARDEN + " ¿Qué se hace justo después de escoger un lugar soleado?", ["El primer paso es choose a sunny place.", "El paso siguiente empieza con Then.", "Then loosen the soil with a small shovel."], "Remover la tierra con una pala pequeña"),
        ("Clasificar una frase", "«The library opens at eight.» ¿Es un hecho o una opinión?", ["Pregunto si se puede comprobar.", "Se puede verificar mirando el horario.", "Entonces es un hecho."], "Un hecho"),
    ],
    [
        ("Clasificar «The school lunch is delicious» como hecho porque suena seguro.", "Se confunde el tono seguro con una verdad comprobable.", "Revisa si hay un adjetivo de valoración, como delicious; esa es una opinión."),
        ("Ignorar until y regar una sola vez.", "No se entiende que until marca una condición.", "Water until the soil is wet significa regar hasta que la tierra esté mojada."),
    ],
    [
        (ADULT + GARDEN + " ¿Qué se hace al final? a) poner una etiqueta con el nombre de la planta b) regar las semillas", "a) poner una etiqueta con el nombre de la planta", "Finally indica el último paso: put a label."),
        (ADULT + OPINIONS + " ¿Cuántos estudiantes tiene el colegio?", "200", "El guion dice two hundred students."),
        (ADULT + RACE + " ¿Qué recibió el ganador? a) una medalla b) un diploma", "a) una medalla", "El guion dice the winner received a medal."),
    ],
    [
        (ADULT + OPINIONS + " ¿Cuál de estas frases es una opinión? a) I think English is the most interesting subject b) The gym is next to the yard", "a) I think English is the most interesting subject", "Lleva I think y el adjetivo interesting."),
        (ADULT + GARDEN + " ¿Hasta cuándo se riegan las semillas? a) hasta que la tierra esté mojada b) hasta que salga el sol", "a) hasta que la tierra esté mojada", "Water them until the soil is wet."),
        (ADULT + RACE + " ¿Qué ocurre justo después de que suena el silbato?", "Los corredores corren dos vueltas", "Después del silbato, dice After that, they ran two laps."),
    ],
    [
        (ADULT + GARDEN + " ¿Qué herramienta se usa para remover la tierra?", "Una pala pequeña", "El guion dice loosen the soil with a small shovel."),
        ("Clasifica la frase «The gym is next to the yard». ¿Es un hecho o una opinión?", "Un hecho", "Se puede comprobar mirando dónde está el gimnasio."),
        (ADULT + RACE + " ¿Cuántas vueltas corrieron?", "2", "El guion dice two laps around the field."),
    ],
    [
        (ADULT + RACE + " Ordena los hechos. A) The winner received a medal. B) The teacher blew the whistle. C) The runners ran two laps. D) The runners stood at the starting line.", "D, B, C, A", "La secuencia es partida, silbato, carrera y premio."),
        (ADULT + OPINIONS + " ¿Qué frase del guion es un hecho que se puede comprobar con un horario? a) The library opens at eight b) The school lunch is delicious", "a) The library opens at eight", "Una hora de apertura se verifica; que algo sea delicioso es una opinión."),
    ],
    [
        ("Clasifica cada frase como hecho (H) u opinión (O). 1) Santiago is the capital of Chile. 2) Summer is the best season. 3) The school has three floors. Responde con tres letras en orden.", "H, O, H", "Las frases 1 y 3 se comprueban; la 2 depende del gusto."),
        (ADULT + GARDEN + " Ordena los pasos. A) Plant the seeds. B) Choose a sunny place. C) Put a label. D) Loosen the soil.", "B, D, A, C", "Siguen first, then, next y finally."),
    ],
    [(ADULT + "«Uniform rules: first, put your name on your jacket. Then hang it in the locker. After that, close the locker. In my opinion, the new lockers are great.» (rules = reglas, jacket = chaqueta, hang = colgar, locker = casillero). ¿Qué parte es una opinión? a) the new lockers are great b) close the locker", "a) the new lockers are great", "Llega después de In my opinion y valora algo.")],
    [
        ("¿Qué significa until?", "Hasta que", "Marca hasta cuándo se hace una acción."),
        ("¿Qué frase introduce una opinión?", "I think o In my opinion", "Anuncian lo que alguien piensa."),
        ("¿Qué palabra marca el último paso?", "Finally", "Cierra la secuencia."),
    ],
    task("Un adulto lee dos veces este texto: «How to make a sandwich. First, put two slices of bread on a plate. Next, spread butter on one slice. Then add cheese and tomato. Finally, put the other slice on top. In my opinion, this is the best snack.» (slices = rebanadas, plate = plato, spread = untar, butter = mantequilla, cheese = queso, top = encima, snack = colación). En tu hoja escribe los cuatro pasos en orden y subraya la frase que es una opinión.", "1. Poner dos rebanadas de pan en un plato. 2. Untar mantequilla en una. 3. Agregar queso y tomate. 4. Poner la otra rebanada encima. Opinión: this is the best snack.", ["escribe los cuatro pasos en orden", "relaciona cada paso con first, next, then o finally", "identifica la frase de opinión"], ["hoja con pasos y opinión subrayada", "nota del adulto"], ["incluir la opinión como un paso", "cambiar el orden de queso y mantequilla"], "Reconoce los pasos correctos y relee con la persona solo las palabras de secuencia para corregir el orden."),
    "Pide a un adulto que lea otra vez el texto del huerto y numera los pasos con first, then, next y finally.",
    "Escribe en español una opinión y un hecho sobre tu colegio.",
)

# ---------------------------------------------------------------- clase 4: causa-efecto, condición y conectores (brecha de información)
RAIN = "Persona A escuchó: «The match was cancelled because it rained all morning.» Persona B escuchó: «The players will play on Saturday if the field is dry.» (match = partido, cancelled = suspendido, rained = llovió, players = jugadores, field = cancha, dry = seca)"
BUS = "«The bus was late, so Tomás missed the first class. He talked to the teacher, and she said: If you bring a note, you will not have a problem. Tomás also promised to wake up earlier.» (late = atrasado, missed = perdió, note = justificativo, wake up = despertar, earlier = más temprano)"
LIBRARY = "«Our library has many books. It also has computers and a quiet room. Students can borrow a book for two weeks. If they keep it longer, they pay a small fine.» (borrow = pedir prestado, quiet = silenciosa, longer = más tiempo, fine = multa)"

lesson(
    OA2, 4,
    "Los textos breves y las frases de dos personas escritos en cada ejercicio; una hoja para tapar el guion y lápiz.",
    "Aprenderé a reconocer causa y efecto, y condición en textos orales, usando los conectores because, so, if y also. Sirve para entender por qué pasan las cosas y qué ocurre si se cumple una condición.",
    ["Sé el pasado simple de verbos como missed y rained.", "Conozco and y but."],
    [
        "La causa (cause) es la razón por la que algo ocurre, y el efecto (effect) es lo que ocurre. Because (porque) presenta la causa: «The match was cancelled because it rained». So (así que) presenta el efecto: «The bus was late, so Tomás missed class». Por eso la causa puede venir antes o después, pero la pista está en el conector. También usamos also (además) para sumar una idea.",
        "La condición (condition) es algo que debe cumplirse para que otra cosa ocurra. If (si) presenta la condición: «If you bring a note, you will not have a problem». Si la condición se cumple, ocurre el resultado. Si no se cumple, no ocurre. Las dos partes están unidas por if y, en la segunda, se usa will (futuro).",
        "En una actividad de brecha de información, cada persona escucha una parte y las dos deben unirlas. Pregunta: Why? (¿por qué?) para hallar la causa y What happens if…? (¿qué ocurre si…?) para la condición. Al juntar las partes comprueba que el conector tiene sentido: la causa explica el efecto, no al revés.",
    ],
    [("cause", "causa: la razón"), ("effect", "efecto: lo que ocurre"), ("because", "porque (presenta la causa)"), ("so", "así que (presenta el efecto)"), ("if", "si (presenta una condición)"), ("also", "además")],
    [
        ("Encontrar la causa", "«The match was cancelled because it rained all morning.» ¿Cuál es la causa?", ["Busco la palabra because.", "Después de because aparece it rained all morning.", "Esa es la razón de la cancelación."], "Que llovió toda la mañana"),
        ("Encontrar la condición", "«The players will play on Saturday if the field is dry.» ¿Qué debe cumplirse para jugar?", ["Busco la palabra if.", "Después de if dice the field is dry.", "Esa es la condición."], "Que la cancha esté seca"),
    ],
    [
        ("Confundir la causa con el efecto en «The bus was late, so Tomás missed class».", "Se cree que lo que viene después de so es la causa.", "So presenta el efecto: perdió la clase porque el bus llegó tarde."),
        ("Pensar que la condición siempre se cumple.", "No se distingue If de When.", "If dice que algo puede pasar solo en ese caso; si no se cumple, no ocurre."),
    ],
    [
        (RAIN + " ¿Cuándo llovió? a) toda la mañana b) toda la tarde", "a) toda la mañana", "La Persona A dice it rained all morning."),
        (ADULT + BUS + " ¿Por qué Tomás perdió la primera clase? a) porque el bus llegó tarde b) porque se enfermó", "a) porque el bus llegó tarde", "El guion dice The bus was late, so Tomás missed the first class."),
        (ADULT + LIBRARY + " ¿Cuántas semanas se puede pedir prestado un libro?", "2", "Dice for two weeks."),
    ],
    [
        (RAIN + " Las dos personas juntan sus datos. ¿Qué día se jugará, si la cancha está seca? a) el sábado b) el domingo", "a) el sábado", "La Persona B dice that the players will play on Saturday."),
        (ADULT + BUS + " ¿Qué pasa si Tomás trae un justificativo? a) no tendrá un problema b) perderá otra clase", "a) no tendrá un problema", "La profesora dice If you bring a note, you will not have a problem."),
        (ADULT + LIBRARY + " ¿Qué ocurre si se guarda un libro más de dos semanas?", "Se paga una multa pequeña", "Dice If they keep it longer, they pay a small fine."),
    ],
    [
        (ADULT + LIBRARY + " ¿Qué tiene la biblioteca además de libros? a) computadores y una sala silenciosa b) una cafetería", "a) computadores y una sala silenciosa", "Dice It also has computers and a quiet room."),
        (ADULT + BUS + " ¿Qué conector presenta el efecto de que el bus llegara tarde? a) so b) because", "a) so", "En The bus was late, so Tomás missed class, so introduce el efecto."),
        ("Completa con because o so: «I took an umbrella ___ it was raining». Opciones: because / so.", "because", "It was raining es la razón de llevar paraguas."),
    ],
    [
        (ADULT + BUS + " ¿Qué prometió Tomás? a) despertarse más temprano b) comprar otro bus", "a) despertarse más temprano", "Dice Tomás also promised to wake up earlier."),
        (ADULT + LIBRARY + " Escribe el conector que suma la idea de los computadores y la sala silenciosa.", "also", "La frase It also has computers agrega información."),
    ],
    [
        ("Una persona escuchó «I stayed home because I was sick». Otra escuchó «I was sick, so I stayed home». ¿Dicen lo mismo? Responde sí o no.", "Sí", "Ambas frases muestran la misma causa (estar enfermo) y el mismo efecto (quedarse en casa)."),
        ("Completa con because o so: «It was cold, ___ I wore a jacket». Opciones: because / so.", "so", "Wore a jacket es el efecto del frío; so presenta el efecto."),
    ],
    [(ADULT + "«If it rains tomorrow, the school trip will be on Wednesday. If it is sunny, we will go on Tuesday. The bus leaves at eight.» (trip = salida, sunny = soleado). Mañana amanece soleado. ¿Qué día es la salida? a) el martes b) el miércoles", "a) el martes", "La condición If it is sunny lleva a Tuesday.")],
    [
        ("¿Qué conector presenta una causa?", "Because", "Se traduce porque."),
        ("¿Qué conector presenta un efecto?", "So", "Se traduce así que."),
        ("¿Qué palabra presenta una condición?", "If", "Se traduce si."),
    ],
    task("Con una persona de tu casa: ella lee la primera mitad, «The picnic was cancelled…», y tú anotas la causa que falta. Después ella lee la segunda mitad: «…because it was very windy. If the wind stops, we will have the picnic on Sunday.» (picnic = picnic, windy = ventoso, wind = viento, stops = para). En tu hoja escribe la causa de la cancelación, la condición para volver a hacerlo y el día.", "Causa: hacía mucho viento. Condición: que el viento pare. Día: el domingo.", ["identifica la causa", "identifica la condición", "indica el día"], ["hoja con causa, condición y día", "nota del adulto"], ["confundir la causa con la condición", "olvidar el día"], "Reconoce lo que acertó y relee con la persona las palabras because e if para distinguir la causa de la condición."),
    "Pide a un adulto que lea otra vez el texto de Tomás y subraya because, so, if y also.",
    "Escribe en español dos oraciones de causa y efecto sobre tu día, usando porque y así que.",
)

# ---------------------------------------------------------------- clase 5: palabras clave, conectores y sonidos
SOUNDS = "Sonidos de la clase: /θ/ es el sonido de «th» sin voz, con la lengua entre los dientes (three, birthday, think, month). /ð/ es el «th» con voz (this, mother, brother, the). /w/ se hace con los labios redondeados (week, water). /r/ se dice sin vibrar la lengua (ready, red, rain). En los verbos regulares en pasado, -ed suena /t/ después de p, k, f, s, sh y ch (helped, looked, washed), /ɪd/ después de t o d (decided, wanted) y /d/ en los demás casos (lived, played)."
ADVERT = "«Hello, I am Lucía. This week I will clean the beach with my friends. First we will walk, then we will collect trash, and also we will plant three small trees. We will work until noon.» (beach = playa, trash = basura, plant = plantar, noon = mediodía)"

lesson(
    OA2, 5,
    "Las listas de palabras y los textos breves escritos en cada ejercicio, que lee un adulto en voz alta; una hoja y lápiz.",
    "Aprenderé a reconocer los sonidos /θ/, /ð/, /w/, /r/ y las terminaciones -ed de verbos regulares en pasado, y a usar palabras clave y los conectores then, also, so y until. Sirve para entender y pronunciar mejor lo que escucho.",
    ["Sé que el pasado de verbos regulares termina en -ed.", "Conozco los conectores then y so."],
    [
        SOUNDS,
        "Las palabras clave (key words) son las que cargan el significado: sustantivos, verbos y números. Los conectores son pequeñas palabras que unen ideas. Then significa luego. Also significa además. So significa así que. Until significa hasta que. «First we will walk, then we will collect trash» muestra el orden; «also we will plant trees» suma una actividad.",
        "Para practicar, repite en voz alta con una persona de tu casa. El sonido /θ/ no existe en el español de Chile, y el /ð/ inglés es más fuerte que la d de «lado»; por eso necesitan práctica. Pon la punta de la lengua entre los dientes: en /θ/ sopla sin voz y en /ð/ haz vibrar la garganta. Si te equivocas, no importa: lo importante es que te entiendan. Las terminaciones -ed también cambian el significado: walk (hoy) y walked (ayer).",
    ],
    [("key word", "palabra clave: lleva el significado"), ("connector", "conector: une ideas"), ("then", "luego"), ("until", "hasta que"), ("-ed ending", "terminación del pasado regular"), ("sound", "sonido")],
    [
        ("Clasificar la terminación -ed", "El verbo «helped» ¿termina con sonido /t/, /d/ o /ɪd/?", ["La letra anterior a -ed es p.", "Después de p, -ed suena /t/.", "Entonces helped suena /helpt/."], "/t/"),
        ("Reconocer el conector de orden", ADULT + ADVERT + " ¿Qué conector muestra el orden entre caminar y recoger basura?", ["Busco el conector entre walk y collect trash.", "Dice First we will walk, then we will collect trash.", "El conector es then."], "Then"),
    ],
    [
        ("Pronunciar siempre -ed como /ɪd/ (walk-ed con una sílaba extra).", "Se lee la letra, no el sonido.", "Después de p, k, f, s, sh y ch, suena /t/; solo después de t o d suena /ɪd/."),
        ("Cambiar /θ/ por /s/ al decir three.", "El español de Chile no tiene /θ/ y se reemplaza.", "Pon la punta de la lengua entre los dientes y sopla sin voz."),
    ],
    [
        ("¿Qué palabra tiene el sonido /θ/ sin voz? a) three b) mother", "a) three", "En three, th es sin voz; en mother, th suena con voz."),
        ("¿Qué palabra tiene el sonido /ð/ con voz? a) this b) birthday", "a) this", "En this, th suena con voz; en birthday suena sin voz."),
        ("¿Con qué sonido empieza «week»? a) /w/ b) /r/", "a) /w/", "Week empieza con w, labios redondeados."),
    ],
    [
        ("¿Qué sonido final tiene «lived»? a) /d/ b) /t/", "a) /d/", "Después de v, -ed suena /d/."),
        ("¿Qué sonido final tiene «decided»? a) /ɪd/ b) /t/", "a) /ɪd/", "Después de d, -ed suena /ɪd/ y forma una sílaba más."),
        ("¿Qué sonido final tiene «washed»? a) /t/ b) /ɪd/", "a) /t/", "Después de sh, -ed suena /t/."),
    ],
    [
        ("¿Qué palabra empieza con el sonido /r/? a) ready b) week", "a) ready", "Ready empieza con r; week empieza con /w/."),
        ("¿Qué palabra empieza con el sonido /θ/ sin voz? a) thank b) the", "a) thank", "En thank, th es sin voz; en the suena con voz."),
        (ADULT + ADVERT + " ¿Cuántos árboles pequeños plantarán?", "3", "El guion dice three small trees."),
    ],
    [
        ("Clasifica por sonido de -ed. Palabras: 1) looked 2) played 3) wanted. Sonidos: a) /t/ b) /d/ c) /ɪd/", "1-a, 2-b, 3-c", "Looked termina en k, played en y y wanted en t."),
        (ADULT + ADVERT + " ¿Hasta cuándo trabajarán Lucía y sus amigos? a) hasta el mediodía b) hasta la noche", "a) hasta el mediodía", "El guion dice We will work until noon."),
    ],
    [
        ("Une cada conector con su significado. 1) then 2) also 3) so 4) until. Significados: a) hasta que b) luego c) además d) así que", "1-b, 2-c, 3-d, 4-a", "Cada conector tiene un significado fijo."),
        (ADULT + ADVERT + " ¿Qué conector usa Lucía para sumar la actividad de plantar árboles? a) also b) until", "a) also", "Dice and also we will plant three small trees."),
    ],
    [(ADULT + "«I studied for my test on Monday, and then I helped my sister with her homework. I also washed the dishes. I worked until nine.» (studied = estudié, test = prueba, dishes = platos, worked = trabajé). ¿Qué terminación -ed suena /ɪd/ en este texto? a) ninguna b) helped", "a) ninguna", "Studied suena /d/, helped suena /t/, washed suena /t/ y worked suena /t/.")],
    [
        ("¿Cómo suena -ed en walked?", "/t/", "Después de k, -ed suena /t/."),
        ("¿Qué palabra significa «además»?", "Also", "Suma una idea a otra."),
        ("¿Qué palabra tiene /θ/: think o brother?", "Think", "En think, th es sin voz."),
    ],
    task("Con una persona de tu casa: léanse en voz alta estas seis palabras, «three, mother, week, ready, helped, wanted», y marca en tu hoja el sonido que tiene cada una al inicio o al final (/θ/, /ð/, /w/, /r/, /t/ o /ɪd/). Después escribe una frase en español que explique cuál fue la más difícil.", "three /θ/, mother /ð/, week /w/, ready /r/, helped /t/, wanted /ɪd/.", ["marca correctamente los seis sonidos", "pronuncia al menos tres palabras con ayuda", "reflexiona sobre la dificultad"], ["hoja con seis sonidos", "nota de la persona que escuchó"], ["marcar /s/ en three", "marcar /ɪd/ en helped"], "Reconoce lo que acertó y practica con la persona solo las dos palabras con th hasta que se escuchen distintas."),
    "Pide a una persona de tu casa que lea las seis palabras en voz alta y repítelas dos veces, mirando cómo se mueve tu lengua.",
    "Escribe en español una estrategia para recordar cuándo -ed suena /t/ y cuándo suena /ɪd/.",
)
