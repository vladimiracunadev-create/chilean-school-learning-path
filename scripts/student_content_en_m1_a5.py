"""Cuaderno del estudiante, 1.º medio Inglés (propuesta), EN1M OA 05 (lectura e interpretación de funciones del lenguaje).

Los textos son originales, están escritos en el enunciado y llevan pista en español. Los datos numéricos son «de ejemplo».
"""
from __future__ import annotations

from student_content_en_m1_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA5 = "EN1M OA 05"
MATR = "Los textos escritos en cada ejercicio; lápiz y hoja para subrayar y anotar."

# ================================================================ OA 05 · clase 1: cantidad, frecuencia y grado
SURVEY = "«Report of a class survey (example data). In 1°B there are 40 students. A large number of students, 28, walk to school. A few students, 7, come by bus. Few students, 2, ride a bike, because there is little space to leave bicycles at school. Three students are driven by a family member. Most students visit the library once a week, but Daniel goes only once a month. Camila is really talkative, and Daniel is quite shy.» (survey = encuesta, walk = caminar, ride a bike = andar en bicicleta, space = espacio, driven = llevados en auto, once a week = una vez por semana, talkative = conversadora, shy = tímido)"
RECIPE2 = "«Recipe note: Use a little salt and a few olives. There is little time, so bake for only fifteen minutes.» (olives = aceitunas, bake = hornear)"

lesson(
    OA5, 1, MATR,
    "Aprenderé a interpretar al leer las palabras que expresan cantidad (a large number of, a few, few, a little, little), frecuencia (once a week) y grado (quite, really). Sirve para entender datos, encuestas y recetas con precisión.",
    ["Sé contar y leer cifras.", "Sé qué son los sustantivos contables (students) e incontables (time)."],
    [
        "Para hablar de cantidad en inglés se elige la palabra según el sustantivo. Con contables en plural se usa a large number of (una gran cantidad), a small number of (una cantidad pequeña), a few (unos pocos, suficientes) y few (muy pocos, casi no hay). Con incontables se usa a little (un poco, algo) y little (muy poco, casi nada). La diferencia es de sentido: A few students come by bus es neutral; Few students ride a bike dice que casi nadie lo hace, con sentido negativo.",
        "La frecuencia (frequency) dice cuántas veces ocurre algo: once a week (una vez por semana), twice a month (dos veces al mes), three times a year (tres veces al año). El grado (degree) dice la intensidad de una cualidad: quite shy (bastante tímido), really talkative (muy conversadora). Los adverbios como really y quite modifican al adjetivo que sigue.",
        "Al leer, lee los números primero y luego las palabras de cantidad; comprueba que sumen o que coincidan. En la encuesta, 28 + 7 + 2 + 3 = 40. Si una frase dice few, espera una cifra muy baja; si dice a large number of, una cifra alta.",
    ],
    [("a large number of", "una gran cantidad de (contables)"), ("a few / few", "unos pocos / muy pocos"), ("a little / little", "un poco / muy poco (incontables)"), ("once a week", "una vez por semana"), ("quite", "bastante"), ("really", "muy, realmente")],
    [
        ("Cantidad en una encuesta", SURVEY + " ¿Cuántos estudiantes caminan a la escuela?", ["Busco la expresión a large number of students.", "El número que sigue es 28.", "Eso responde la pregunta."], "28 estudiantes"),
        ("Grado y frecuencia", SURVEY + " ¿Cómo describe el texto a Daniel y cada cuánto va a la biblioteca?", ["Busco quite shy para el grado.", "Busco once a month para la frecuencia.", "Une las dos pistas."], "Es bastante tímido y va una vez al mes"),
    ],
    [
        ("Traducir few como «unos pocos» sin ver el sentido.", "Se ignora que few (sin a) indica casi ninguno.", "A few = unos pocos, algunos; few = muy pocos."),
        ("Usar few con sustantivos incontables (few time).", "Se olvida que time es incontable.", "Con incontables se usa little: little time."),
    ],
    [
        (SURVEY + " ¿Cuántos estudiantes van en bus?", "7", "El texto dice A few students, 7."),
        (SURVEY + " ¿Por qué pocos estudiantes van en bicicleta?", "Porque hay poco espacio para dejar bicicletas", "Dice because there is little space."),
        (SURVEY + " ¿Qué significa once a month? A) una vez al mes B) una vez al año", "A) una vez al mes", "Month es mes y once es una vez."),
    ],
    [
        (SURVEY + " ¿Quién es quite shy? A) Daniel B) Camila", "A) Daniel", "El texto lo dice de Daniel."),
        arith(SURVEY + " ¿Cuántos estudiantes son llevados por un familiar? Calcula 40 − 28 − 7 − 2.", "40-28-7-2", "Se restan del total los que caminan, van en bus y en bicicleta."),
        (SURVEY + " ¿Qué visita la mayoría una vez por semana? A) la biblioteca B) el gimnasio", "A) la biblioteca", "Dice Most students visit the library once a week."),
    ],
    [
        (SURVEY + " ¿Cuántos estudiantes hay en 1°B?", "40", "El texto dice In 1°B there are 40 students."),
        (SURVEY + " ¿Qué significa really talkative? A) muy conversadora B) poco conversadora", "A) muy conversadora", "Really intensifica el adjetivo talkative."),
        (SURVEY + " ¿Cuántos estudiantes van en bicicleta?", "2", "El texto dice Few students, 2, ride a bike."),
    ],
    [
        (SURVEY + " ¿Qué diferencia hay entre «A few students come by bus» y «Few students ride a bike»? A) a few es neutral y few indica muy pocos B) son idénticas", "A) a few es neutral y few indica muy pocos", "La a cambia el sentido de «algunos» a «casi nadie»."),
        ("Con el sustantivo incontable «time», ¿qué palabra usas para decir «muy poco»? A) little B) few", "A) little", "Little acompaña a incontables como time."),
    ],
    [
        (SURVEY + " Un lector dice que la mayoría llega en bus. ¿Qué dato lo corrige? A) 28 de 40 caminan B) 7 van en bus", "A) 28 de 40 caminan", "La mayor cantidad pertenece a quienes caminan."),
        (SURVEY + " ¿Qué frase prueba que Daniel va menos que los demás a la biblioteca? A) Daniel goes only once a month B) Camila is really talkative", "A) Daniel goes only once a month", "Compara con once a week de la mayoría."),
    ],
    [(RECIPE2 + " ¿Cuántas aceitunas usa la receta? A) unas pocas B) ninguna", "A) unas pocas", "Dice a few olives.")],
    [
        ("¿Qué expresa a small number of?", "Una cantidad pequeña de contables", "Se usa con sustantivos plurales."),
        ("¿Qué modifican quite y really?", "El adjetivo que viene después", "Marcan el grado."),
        ("¿Qué significa twice a month?", "Dos veces al mes", "Es una expresión de frecuencia."),
    ],
    task("Lee este texto original: «Notice from the school gym (example data). A large number of students, 120, use the gym. A few teachers, 6, come after school. Few students, 3, stay after six o'clock because the gym closes then. Mr. Lagos goes to the gym three times a week. Camila is quite athletic, and Pablo is really tired after practice.» (athletic = deportista, closes = cierra, tired = cansado). En tu hoja escribe: quién usa el gimnasio en mayor cantidad, cuántos profesores lo usan, cuál es la frecuencia del Sr. Lagos y cómo se describe a Camila.", "Lo usan en mayor cantidad los estudiantes (120). Lo usan 6 profesores. El Sr. Lagos va tres veces a la semana. Camila es bastante deportista.", ["usa las cifras exactas", "interpreta bien las palabras de cantidad", "traduce la frecuencia y el grado"], ["hoja con cuatro respuestas", "subrayado del texto"], ["confundir few con a few", "no traducir el grado de quite"], "Valora las cifras y vuelve a las palabras de cantidad para afinar el sentido."),
    "Vuelve a leer la encuesta y subraya con un color las palabras de cantidad y con otro las de frecuencia.",
    "Escribe en español cuatro datos de tu curso que podrías expresar con a large number of, a few, little y once a week.",
)

# ---------------------------------------------------------------- clase 2: acciones que continúan, duración y hábitos pasados
SWIM = "«Profile (fictional). Lucas has been swimming for three years. He has been training every day since March. He is tired now because he has been practicing for two hours. His sister Marta used to play volleyball, but now she plays tennis. Lucas and his friend Gaspar have been friends for eight years. Their coach has just announced a new schedule.» (swimming = nadando, training = entrenando, since = desde, practicing = practicando, used to = solía, friends = amigos, coach = entrenador, has just announced = acaba de anunciar, schedule = horario)"

lesson(
    OA5, 2, MATR,
    "Aprenderé a interpretar al leer acciones que empezaron en el pasado y continúan o acaban de terminar (have been + -ing), la duración (for, since) y los hábitos pasados (used to). Sirve para entender perfiles, biografías y relatos con tiempo.",
    ["Sé el presente continuo (is swimming).", "Sé el pasado simple."],
    [
        "El presente perfecto continuo (have/has been + verbo -ing) describe una acción que empezó en el pasado y sigue ahora, o que acaba de terminar y se nota el resultado. «Lucas has been swimming for three years» significa que nada hace tres años y todavía lo hace. «He is tired because he has been practicing for two hours» muestra una acción que acaba de terminar y explica su cansancio. Se pregunta con How long: How long have you been friends?",
        "Para la duración se usan for y since. For + un período (for three years, for eight years, for two hours) dice cuánto dura. Since + un punto del tiempo (since March, since primary school) dice cuándo empezó. Se puede responder la misma pregunta con las dos formas. Has just announced significa «acaba de anunciar»: una acción terminada hace muy poco.",
        "Los hábitos pasados se expresan con used to + verbo: Marta used to play volleyball significa que antes jugaba, pero ya no lo hace. Fíjate en la palabra now: «but now she plays tennis». Si el texto contrasta antes y ahora con used to y now, el cambio es el centro del mensaje.",
    ],
    [("have been + -ing", "acción que empezó antes y continúa o acaba de terminar"), ("for", "durante (un período)"), ("since", "desde (un punto del tiempo)"), ("used to", "solía; hábito del pasado que ya no ocurre"), ("just", "recién, acaba de"), ("How long…?", "¿Cuánto tiempo…?")],
    [
        ("For y since", SWIM + " ¿Desde cuándo entrena Lucas cada día?", ["Busco since en el texto.", "El texto dice since March.", "Es un punto en el tiempo."], "Desde marzo"),
        ("Hábito pasado", SWIM + " ¿Marta todavía juega vóleibol? Explica con una pista.", ["Busco used to play volleyball.", "Used to indica un hábito del pasado.", "Luego aparece but now she plays tennis."], "No, antes jugaba pero ahora juega tenis"),
    ],
    [
        ("Pensar que used to significa que la acción continúa.", "Se confunde con el presente.", "Used to habla de un hábito pasado que ya no ocurre."),
        ("Usar for con un punto en el tiempo (for March).", "Se olvida la diferencia entre período y punto.", "For va con un período; since va con un punto de inicio."),
    ],
    [
        (SWIM + " ¿Cuánto tiempo lleva nadando Lucas?", "Tres años", "El texto dice for three years."),
        (SWIM + " ¿Qué practica Marta ahora? A) tenis B) vóleibol", "A) tenis", "Dice but now she plays tennis."),
        (SWIM + " ¿Desde hace cuánto son amigos Lucas y Gaspar?", "Ocho años", "Dice for eight years."),
    ],
    [
        (SWIM + " ¿Por qué está cansado Lucas? A) porque ha estado practicando dos horas B) porque no durmió", "A) porque ha estado practicando dos horas", "El texto dice he has been practicing for two hours."),
        (SWIM + " ¿Qué significa has just announced? A) acaba de anunciar B) anunciará mañana", "A) acaba de anunciar", "Just señala una acción muy reciente."),
        (SWIM + " ¿Qué anunció el entrenador?", "Un nuevo horario", "Dice a new schedule."),
    ],
    [
        arith(SWIM + " Lucas lleva tres años nadando. Si cada año tiene 12 meses, ¿cuántos meses lleva nadando?", "3*12", "Se multiplican los años por los meses de cada año."),
        (SWIM + " ¿Qué forma indica que la acción empezó y continúa? A) has been swimming B) used to play", "A) has been swimming", "Have been + -ing une pasado y presente."),
        (SWIM + " ¿Cuál es la mejor traducción de «used to play volleyball»? A) solía jugar vóleibol B) juega vóleibol ahora", "A) solía jugar vóleibol", "Used to habla de un hábito pasado."),
    ],
    [
        (SWIM + " ¿Cuál frase usa since correctamente? A) He has been training since March B) He has been training since three years", "A) He has been training since March", "Since va con un punto en el tiempo, no con un período."),
        (SWIM + " ¿Cuál frase usa for correctamente? A) for eight years B) for primary school", "A) for eight years", "For va con un período."),
    ],
    [
        (SWIM + " Un lector dice que Marta juega vóleibol hoy. ¿Qué parte lo corrige? A) used to play volleyball, but now she plays tennis B) has been swimming", "A) used to play volleyball, but now she plays tennis", "Used to y now muestran un cambio."),
        (SWIM + " Un lector dice que Lucas empezó a nadar hace un año. ¿Qué dato lo corrige? A) he has been swimming for three years B) he has just announced", "A) he has been swimming for three years", "El texto da tres años, no uno."),
    ],
    [("Lee: «Ana has been learning the guitar since January. She used to play the piano, but she stopped. How long has she been learning the guitar?» (stopped = dejó). ¿Desde cuándo aprende la guitarra?", "Desde enero", "Dice since January.")],
    [
        ("¿Qué pregunta se usa para preguntar duración?", "How long…?", "Pide un período o inicio."),
        ("¿Qué significa «I have been waiting for an hour»?", "Llevo una hora esperando", "Acción que empezó y continúa."),
        ("¿Qué expresa used to?", "Un hábito del pasado que ya no ocurre", "Contrasta antes y ahora."),
    ],
    task("Lee este texto original: «Profile (fictional). Emilia has been learning chess for two years. She has been playing in the school team since last April. Her brother used to play chess, but now he paints. Emilia has just won a regional game. How long has she been in the team? Since April.» (chess = ajedrez, team = equipo, won = ganó, regional = regional, paints = pinta). En tu hoja escribe: cuánto lleva aprendiendo, desde cuándo está en el equipo, qué hacía su hermano antes y qué acaba de pasar.", "Lleva dos años aprendiendo. Está en el equipo desde abril pasado. Su hermano jugaba ajedrez antes y ahora pinta. Acaba de ganar un juego regional.", ["usa for y since correctamente", "interpreta used to como hábito pasado", "traduce has just won como acción reciente"], ["hoja con cuatro respuestas", "subrayado de las formas verbales"], ["confundir for con since", "decir que el hermano juega ajedrez ahora"], "Reconoce las formas bien interpretadas y repasa la diferencia entre período y punto de inicio."),
    "Vuelve a leer el perfil de Lucas y subraya las formas have been + -ing con un color y used to con otro.",
    "Escribe en español tres cosas que llevas haciendo un tiempo y dos hábitos que tenías antes y ya no tienes.",
)

# ---------------------------------------------------------------- clase 3: predicciones, necesidad, promesas y posibilidades
PLAN2 = "«Message from the coach (example). Tomorrow it will probably rain in the afternoon, so we might move the match to Sunday. You needn't bring a ball: the school has many. I promise I will send the new schedule tonight. Shall we meet at the gym at ten? Remember that Mr. Lagos shall be here at nine to open the doors.» (probably = probablemente, might = podría, move = cambiar, needn't = no necesitas, promise = prometo, shall = verbo modal formal para futuro u ofrecimiento, meet = juntarnos, open = abrir)"

lesson(
    OA5, 3, MATR,
    "Aprenderé a interpretar al leer verbos modales y expresiones que indican predicciones, necesidades, promesas y posibilidades (will probably, might, needn't, I promise, shall). Sirve para entender mensajes sobre planes y saber qué es seguro, qué es posible y qué es obligatorio.",
    ["Sé will para el futuro.", "Sé que can y must son verbos modales."],
    [
        "Los verbos modales son auxiliares que añaden un matiz de certeza, necesidad o permiso. Will probably expresa una predicción muy probable (casi segura). Might expresa una posibilidad: puede pasar o no. La diferencia es de grado: en «it will probably rain», hay mucha probabilidad; en «we might move the match», hay una posibilidad. Si se compara, will probably es más seguro que might.",
        "Needn't (o don't need to) significa que algo no es necesario: «You needn't bring a ball» quiere decir que no hace falta llevar pelota. No es una prohibición: es la ausencia de obligación. Una promesa (promise) se hace con I promise I will…: compromete a quien habla. Shall es un modal formal: Shall we meet…? es una sugerencia o invitación, y «Mr. Lagos shall be here» es un uso formal que expresa una promesa o una decisión firme: se asegura de que él estará ahí.",
        "Al leer un mensaje de planes, subraya los modales y clasifícalos: seguro (will), muy probable (will probably), posible (might), no necesario (needn't), compromiso (I promise), sugerencia (Shall we…?). Eso te dice qué debes preparar y qué debes esperar.",
    ],
    [("will probably", "probablemente; casi seguro"), ("might", "podría; es posible"), ("needn't", "no hace falta, no es necesario"), ("promise", "promesa"), ("shall", "modal formal; Shall we…? = ¿Y si…?"), ("possibility", "posibilidad")],
    [
        ("Grado de certeza", PLAN2 + " ¿Qué es más probable: la lluvia o el cambio de partido al domingo?", ["La lluvia usa will probably.", "El cambio usa might.", "Will probably es más seguro que might."], "La lluvia, porque dice will probably; el cambio solo es posible (might)"),
        ("No necesidad", PLAN2 + " ¿Hay que llevar pelota?", ["Busco needn't bring a ball.", "Needn't indica que no hace falta.", "El colegio tiene muchas."], "No, porque el colegio tiene muchas"),
    ],
    [
        ("Entender needn't como una prohibición.", "Se confunde con must not.", "Needn't = no hace falta; must not = está prohibido."),
        ("Entender might como «seguro».", "No se ve el grado de posibilidad.", "Might es solo una posibilidad."),
    ],
    [
        (PLAN2 + " ¿Qué promete la persona que escribe? A) enviar el nuevo horario esta noche B) llevar una pelota", "A) enviar el nuevo horario esta noche", "Dice I promise I will send the new schedule tonight."),
        (PLAN2 + " ¿A qué hora llegará el Sr. Lagos?", "A las nueve", "Dice shall be here at nine."),
        (PLAN2 + " ¿Qué sugiere con Shall we meet at the gym at ten? A) juntarse en el gimnasio a las diez B) cerrar el gimnasio", "A) juntarse en el gimnasio a las diez", "Shall we…? propone un plan."),
    ],
    [
        (PLAN2 + " ¿Qué podría hacer el equipo con el partido? A) cambiarlo al domingo B) cancelarlo para siempre", "A) cambiarlo al domingo", "Dice we might move the match to Sunday."),
        (PLAN2 + " ¿Cuándo es probable que llueva?", "En la tarde de mañana", "Dice Tomorrow it will probably rain in the afternoon."),
        (PLAN2 + " ¿Qué abre el Sr. Lagos? A) las puertas B) las ventanas", "A) las puertas", "Dice to open the doors."),
    ],
    [
        ("Une cada frase con su significado. 1) It might snow. 2) You needn't hurry. 3) I promise I will call. Significados: a) no es necesario apurarse b) puede que nieve c) me comprometo a llamar", "1-b, 2-a, 3-c", "Might = posible, needn't = no hace falta y promise = compromiso."),
        ("Lee: «He will probably win, but she might win too.» ¿Quién tiene más probabilidad? A) él B) ella", "A) él", "Will probably es más seguro que might."),
        ("Lee: «You needn't wear a coat; it is warm.» ¿Qué se entiende? A) que no hace falta abrigo B) que el abrigo está prohibido", "A) que no hace falta abrigo", "Needn't indica ausencia de necesidad, no prohibición."),
    ],
    [
        ("Lee: «You must not touch the paint. You needn't clean the brushes.» ¿Qué se puede hacer sin limpiar? A) no limpiar los pinceles B) tocar la pintura", "A) no limpiar los pinceles", "Needn't indica que no hace falta; must not prohíbe tocar."),
        ("Lee: «I promise I will come early. It might be difficult because of the traffic.» ¿Qué es seguro y qué es posible? A) seguro: la promesa; posible: la dificultad B) seguro: el tráfico; posible: la promesa", "A) seguro: la promesa; posible: la dificultad", "I promise compromete y might solo es posibilidad."),
    ],
    [
        (PLAN2 + " Un compañero entendió que es obligatorio llevar pelota. ¿Qué frase lo corrige? A) You needn't bring a ball B) Tomorrow it will probably rain", "A) You needn't bring a ball", "Needn't significa que no es necesario."),
        (PLAN2 + " Un compañero dice que seguro habrá partido el sábado. ¿Qué frase muestra duda? A) we might move the match B) the school has many", "A) we might move the match", "Might expresa posibilidad."),
    ],
    [("Lee: «The bus might be late. It will probably arrive at five. I promise I will wait for you.» ¿Qué hace quien escribe? A) promete esperar B) llega tarde", "A) promete esperar", "Dice I promise I will wait.")],
    [
        ("¿Cuál es más seguro: will probably o might?", "Will probably", "Might indica solo posibilidad."),
        ("¿Qué significa needn't?", "No hace falta", "No es una prohibición."),
        ("¿Qué expresa I promise I will…?", "Un compromiso de quien habla", "Es una promesa."),
    ],
    task("Lee este mensaje original: «Hi team. The trip to the museum might be on Friday, but it will probably be on Thursday because of the weather forecast. You needn't bring lunch: the school will give you sandwiches. I promise I will confirm the day by tonight. Shall we meet at the gate at eight?» (trip = salida, weather forecast = pronóstico, gate = portón, confirm = confirmar, lunch = almuerzo). En tu hoja escribe: qué día es más probable, qué es posible, qué no es necesario, qué se promete y qué se sugiere.", "Es más probable el jueves; es posible el viernes; no hace falta llevar almuerzo; se promete confirmar el día esta noche; se sugiere juntarse en el portón a las ocho.", ["clasifica correctamente will probably y might", "interpreta needn't como no necesario", "identifica promesa y sugerencia"], ["hoja con cinco respuestas", "subrayado de los modales"], ["cambiar jueves y viernes", "tomar needn't como prohibición"], "Reconoce los modales bien clasificados y revisa con la persona las pistas de cada uno."),
    "Vuelve a leer el mensaje del entrenador y subraya cada modal con un color distinto según su función.",
    "Escribe en español tres planes tuyos para el fin de semana, uno seguro, uno probable y uno solo posible.",
)

# ---------------------------------------------------------------- clase 4: conectar ideas
TRIP3 = "«Last summer, Andrea and her cousin both wanted to visit the coast. First, they saved money so that they could buy the bus tickets. Although the tickets were expensive, they bought them. Later, they packed light bags. Both girls wore hats because the sun was strong. Last, they sent a postcard to their grandmother.» (saved = ahorraron, tickets = pasajes, packed = empacaron, light = livianas, wore = usaron, strong = fuerte, sent = enviaron, postcard = postal, grandmother = abuela)"
NOTEA = "Mensaje de Andrea: «I have the tickets for Saturday at seven. The bus leaves from the main terminal.» (leaves = sale)"
NOTEB = "Mensaje de su prima: «I have the address of the hostel, but I don't know the bus time. I will bring both backpacks.» (address = dirección, hostel = hostal, backpacks = mochilas)"

lesson(
    OA5, 4, "Dos mensajes que se complementan, escritos en cada ejercicio; cada mensaje tiene un dato que el otro no tiene; lápiz y hoja.",
    "Aprenderé a entender cómo se conectan las ideas con although, both, so that, later y last, y a completar información que falta uniendo dos mensajes. Sirve para seguir el hilo de un relato y de una conversación escrita.",
    ["Sé first, then y because.", "Sé but y so."],
    [
        "Los conectores unen ideas y muestran su relación. Both… and… une a dos personas o cosas (Both girls). So that indica el propósito de una acción (they saved money so that they could buy tickets). Although introduce un contraste (aunque los pasajes eran caros, los compraron). Later y last ordenan los hechos en el tiempo: later es «más tarde» y last es «por último». Because explica la causa.",
        "Para leer un relato, subraya cada conector y pregúntate qué relación marca: ¿orden?, ¿causa?, ¿propósito?, ¿contraste?, ¿suma? Así reconstruyes la historia sin traducir todo. Si un conector introduce una idea que parece contradictoria, probablemente es un contraste.",
        "En una conversación escrita con vacío de información, cada mensaje aporta una pieza: Andrea tiene los pasajes y la hora del bus; la prima tiene la dirección del hostal. Para el plan completo debes unir ambos datos. Anota el dato de cada autor y busca qué falta para llegar al hostal el sábado.",
    ],
    [("although", "aunque: contraste"), ("so that", "para que: propósito"), ("both … and", "tanto … como; los dos"), ("later", "más tarde, después"), ("last", "por último"), ("because", "porque: causa")],
    [
        ("Conector de contraste", TRIP3 + " ¿Qué conector muestra que, a pesar del precio, compraron los pasajes?", ["Busco la idea que se opone: eran caros, pero compraron.", "La frase dice Although the tickets were expensive.", "Although marca el contraste."], "Although"),
        ("Propósito", TRIP3 + " ¿Para qué ahorraron dinero?", ["Busco so that.", "El texto dice they saved money so that they could buy the bus tickets.", "El propósito es comprar los pasajes."], "Para poder comprar los pasajes de bus"),
    ],
    [
        ("Pensar que although introduce una causa.", "Se confunde con because.", "Although = aunque (contraste); because = porque (causa)."),
        ("Leer solo un mensaje de la conversación.", "Se olvida que la información está repartida.", "Subraya el dato que aporta cada autor."),
    ],
    [
        (TRIP3 + " ¿Qué conector señala el último paso? A) Last B) Later", "A) Last", "Last significa por último."),
        (TRIP3 + " ¿Por qué usaron sombrero las dos? A) porque el sol estaba fuerte B) porque llovía", "A) porque el sol estaba fuerte", "Dice because the sun was strong."),
        (TRIP3 + " ¿Qué enviaron a su abuela?", "Una postal", "Dice they sent a postcard."),
    ],
    [
        (TRIP3 + " ¿Qué indica both en «Both girls wore hats»? A) que las dos usaron sombrero B) que ninguna lo usó", "A) que las dos usaron sombrero", "Both se refiere a las dos."),
        (TRIP3 + " ¿Qué hicieron después de comprar los pasajes? A) empacaron bolsos livianos B) enviaron la postal", "A) empacaron bolsos livianos", "Later marca lo siguiente: packed light bags."),
        (NOTEA + " ¿A qué hora sale el bus?", "A las siete", "Dice at seven."),
    ],
    [
        (NOTEA + " " + NOTEB + " ¿Qué dato tiene Andrea que no tiene su prima? A) la hora del bus B) la dirección del hostal", "A) la hora del bus", "La prima dice que no conoce la hora."),
        (NOTEA + " " + NOTEB + " ¿Qué dato tiene la prima que no tiene Andrea? A) la dirección del hostal B) los pasajes", "A) la dirección del hostal", "Andrea no menciona la dirección."),
        (NOTEA + " " + NOTEB + " ¿Qué necesitan juntar para viajar el sábado? A) pasajes y dirección B) solo la dirección del hostal", "A) pasajes y dirección", "Los pasajes con el horario y la dirección completan el plan."),
    ],
    [
        ("Une cada conector con su relación. 1) although 2) so that 3) later Relaciones: a) propósito b) orden en el tiempo c) contraste", "1-c, 2-a, 3-b", "Although opone, so that explica para qué y later ordena."),
        (NOTEB + " ¿Qué lleva la prima? A) las dos mochilas B) los pasajes", "A) las dos mochilas", "Dice I will bring both backpacks."),
    ],
    [
        (TRIP3 + " Un lector dice que no compraron los pasajes porque eran caros. ¿Qué conector lo corrige? A) Although B) Because", "A) Although", "Although muestra que los compraron a pesar del precio."),
        (NOTEA + " " + NOTEB + " Un compañero dice que ya tienen todo para viajar. ¿Qué sigue faltando? A) ningún dato, porque suman los dos mensajes B) la hora del bus, que nadie tiene", "A) ningún dato, porque suman los dos mensajes", "Los pasajes y la hora, más la dirección, completan el plan."),
    ],
    [("Lee: «Both Elisa and Mateo like pizza, but Elisa prefers vegetables. Although the restaurant was full, they found a table.» (full = lleno, found = encontraron). ¿Qué muestra although? A) un contraste B) una causa", "A) un contraste", "Aunque estaba lleno, encontraron mesa.")],
    [
        ("¿Qué relación marca so that?", "Propósito", "Dice para qué se hace algo."),
        ("¿Qué significa both?", "Los dos", "Se refiere a dos personas o cosas."),
        ("¿Qué conector ordena el último hecho?", "Last", "Significa por último."),
    ],
    task("Lee estos dos mensajes. Mensaje de Pedro: «I have the paint for the wall. I don't have brushes.» (paint = pintura, wall = pared, brushes = pinceles). Mensaje de Valeria: «I have two brushes, although they are old. Both Pedro and I will paint on Saturday so that we finish before lunch.» (old = viejos, finish = terminar). En tu hoja escribe: qué tiene cada uno, qué conectores se usan y qué día pintan.", "Pedro tiene pintura y Valeria dos pinceles viejos. Conectores: although (contraste), both (los dos), so that (propósito). Pintan el sábado.", ["asigna cada dato al autor correcto", "identifica al menos dos conectores y su función", "indica el día correcto"], ["hoja con cuatro respuestas", "subrayado de los conectores"], ["atribuir los pinceles a Pedro", "confundir although con because"], "Valora el reparto de datos y repasa la función de cada conector."),
    "Vuelve a leer el relato de Andrea y numera los hechos con first, later y last.",
    "Escribe en español dos oraciones con although y so that sobre algo de tu semana.",
)

# ---------------------------------------------------------------- clase 5: situaciones hipotéticas y consejos
ADV = "«Dear Alex, I am always nervous before tests. I study a lot, but I forget everything. What should I do? — Nervous in Osorno. Reply: Dear Nervous, if I were you, I would sleep eight hours and I would take short breaks while studying. You would feel calmer if you practiced with old tests. If you were less afraid of mistakes, you would learn faster. Good luck!» (nervous = nervioso, forget = olvidar, calmer = más tranquilo, practiced = practicaras, afraid = con miedo, mistakes = errores, faster = más rápido)"
ENG = "«My neighbor Tomás is shy. He would meet more people if he spoke English at the school club. If I were Tomás, I would go to the club on Friday. Also, if he joined, he would make new friends.» (neighbor = vecino, club = taller, joined = se uniera, make friends = hacer amigos)"

lesson(
    OA5, 5, MATR,
    "Aprenderé a interpretar al leer situaciones hipotéticas o imaginarias y consejos con if + pasado y would. Sirve para entender cartas de consejos, opiniones y planes que dependen de una condición.",
    ["Sé el pasado simple.", "Sé should para dar consejo."],
    [
        "Una situación hipotética es algo imaginario o poco probable en el presente. Se construye con if + pasado simple, y el resultado con would + verbo: If he spoke English, he would meet more people. Aunque el verbo esté en pasado, el sentido es presente o futuro: no habla del pasado, habla de una posibilidad imaginada. En esta estructura, con if se usa were para todas las personas: if I were, if he were.",
        "El consejo (advice) más frecuente es If I were you, I would…: «si yo fuera tú, yo haría…». Quien lo dice se pone en el lugar del otro y recomienda. Otras fórmulas son You should… y Why don't you…? Cuando leas una carta de consejos, identifica el problema, el consejo y el resultado que se imagina: sleep eight hours → feel calmer.",
        "Para no confundirte, separa cada oración en dos partes: la condición (if…) y la consecuencia (would…). «If you practiced with old tests, you would feel calmer». La condición es lo que se propone hacer; la consecuencia es lo que pasaría. Ninguna de las dos es un hecho: son imaginadas.",
    ],
    [("if I were you, I would…", "si yo fuera tú, yo haría… (consejo)"), ("if + pasado, would + verbo", "estructura de una situación imaginaria"), ("hypothetical", "hipotético: imaginario o poco probable"), ("advice", "consejo"), ("condition", "condición: la parte con if"), ("result", "resultado: la parte con would")],
    [
        ("Consejo", ADV + " ¿Qué consejo le dan a la persona nerviosa?", ["Busco If I were you, I would.", "Le dicen que duerma ocho horas y haga pausas cortas.", "También sugieren practicar con pruebas antiguas."], "Dormir ocho horas, hacer pausas cortas y practicar con pruebas antiguas"),
        ("Condición y resultado", ENG + " ¿Cuál es la condición y cuál el resultado de «He would meet more people if he spoke English»?", ["La condición es if he spoke English.", "El resultado es he would meet more people.", "Ninguna de las dos ocurre todavía: es imaginario."], "Condición: hablar inglés en el taller. Resultado: conocería a más gente"),
    ],
    [
        ("Pensar que if + pasado habla del pasado.", "Se traduce el verbo literalmente.", "Con would indica una situación imaginaria del presente o futuro."),
        ("Creer que would expresa un hecho seguro.", "Se olvida la condición.", "El resultado depende de la parte con if."),
    ],
    [
        (ADV + " ¿Qué problema cuenta la persona? A) se pone nerviosa antes de las pruebas B) no tiene tiempo", "A) se pone nerviosa antes de las pruebas", "Dice I am always nervous before tests."),
        (ADV + " ¿Cuántas horas recomienda dormir?", "Ocho", "Dice sleep eight hours."),
        (ENG + " ¿Quién es tímido? A) Tomás B) el vecino de Tomás", "A) Tomás", "El texto dice Tomás is shy."),
    ],
    [
        (ADV + " ¿Qué pasaría si practicara con pruebas antiguas? A) se sentiría más tranquilo B) se sentiría más cansado", "A) se sentiría más tranquilo", "Dice You would feel calmer."),
        (ENG + " ¿Qué haría quien escribe si fuera Tomás? A) iría al taller el viernes B) cambiaría de colegio", "A) iría al taller el viernes", "Dice If I were Tomás, I would go to the club on Friday."),
        (ENG + " ¿Qué lograría Tomás si se uniera al taller? A) haría nuevos amigos B) perdería amigos", "A) haría nuevos amigos", "Dice he would make new friends."),
    ],
    [
        (ADV + " ¿Qué ocurriría si la persona tuviera menos miedo a los errores? A) aprendería más rápido B) olvidaría todo", "A) aprendería más rápido", "Dice you would learn faster."),
        (ENG + " ¿Qué significa «He would meet more people»? A) conocería a más gente B) conoció a más gente ayer", "A) conocería a más gente", "Would + verbo expresa una consecuencia imaginaria."),
        ("Une cada expresión con su función. 1) If I were you, I would… 2) You should… 3) Why don't you…? Funciones: a) sugerencia en forma de pregunta b) consejo desde el lugar del otro c) consejo directo", "1-b, 2-c, 3-a", "Cada fórmula da el consejo de modo distinto."),
    ],
    [
        (ADV + " ¿Cuál es la condición en «If you practiced with old tests, you would feel calmer»? A) practicar con pruebas antiguas B) sentirse más tranquilo", "A) practicar con pruebas antiguas", "La parte con if es la condición."),
        (ENG + " ¿Por qué se usa were en «If I were Tomás»? A) porque con if se usa were para todas las personas B) porque Tomás es plural", "A) porque con if se usa were para todas las personas", "Es una regla de la estructura hipotética."),
    ],
    [
        (ADV + " Un lector dice que la persona sí estudia poco. ¿Qué dato lo corrige? A) I study a lot B) Good luck", "A) I study a lot", "La persona dice que estudia mucho pero olvida todo."),
        (ENG + " Un lector dice que Tomás ya habla inglés en el taller. ¿Qué parte muestra que es solo una posibilidad? A) would meet more people if he spoke English B) My neighbor", "A) would meet more people if he spoke English", "If + pasado y would indican algo imaginario."),
    ],
    [("Lee: «If I were you, I would call your grandmother tonight. She would be happy to hear from you.» (hear from you = saber de ti). ¿Qué consejo da quien escribe?", "Llamar a la abuela esta noche", "Dice I would call your grandmother tonight.")],
    [
        ("¿Qué estructura expresa una situación imaginaria?", "If + pasado simple, would + verbo", "Une condición y resultado."),
        ("¿Qué expresa If I were you, I would…?", "Un consejo", "Se pone en el lugar del otro."),
        ("¿Qué verbo se usa con if para todas las personas?", "Were", "If I were, if he were."),
    ],
    task("Lee esta carta original: «Dear Sam, I never have time to read. I get home late and I am tired. What can I do? — Busy in Temuco. Reply: Dear Busy, if I were you, I would read ten minutes before bed. You would finish a book in a month if you read every night. If you turned off your phone, you would feel more relaxed. Good luck!» (get home = llego a casa, tired = cansado, finish = terminar, turned off = apagaras, relaxed = relajado). En tu hoja escribe el problema, dos consejos y un resultado que se imagina.", "Problema: no tiene tiempo para leer porque llega tarde y cansado. Consejos: leer diez minutos antes de dormir; apagar el celular. Resultado: terminaría un libro en un mes o se sentiría más relajado.", ["identifica el problema", "escribe dos consejos con la estructura", "indica un resultado imaginario"], ["hoja con tres respuestas", "subrayado de condición y resultado"], ["confundir el consejo con un hecho", "olvidar la condición"], "Reconoce los consejos y revisa la condición y el resultado de cada oración."),
    "Vuelve a leer la carta de consejos y subraya las condiciones con un color y los resultados con otro.",
    "Escribe en español un problema pequeño tuyo y un consejo con «si yo fuera tú…».",
)
