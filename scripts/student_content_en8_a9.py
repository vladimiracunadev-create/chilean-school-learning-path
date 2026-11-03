"""Cuaderno del estudiante, 8.º básico Inglés (propuesta), EN08 OA 09 (estrategias para hablar con claridad y fluidez).

Todos los diálogos, listas y esquemas están escritos en cada ejercicio, con pista en español.
Las clases del plan tienen títulos genéricos; aquí cada clase trabaja un momento (antes, durante o después de hablar) que nombra el OA.
La práctica oral se hace con una persona de la casa; no hay audio.
"""
from __future__ import annotations

from student_content_en8_a import lesson, task
from student_lessons import arith

OA9 = "EN08 OA 09"
READ = "Lee: "

# ---------------------------------------------------------------- clase 1: antes de hablar — practicar, repetir, predecir vocabulario y chunks
CAFE = "Situación: pides algo en una cafetería. Frases fijas (chunks) del tema: «Could I have a sandwich, please?», «I'd like a juice, please.», «How much is it?», «Is it for here or to go?», «Here you are.» (could I have = ¿me podría dar?, I'd like = quisiera, to go = para llevar, here you are = aquí tiene)"

lesson(
    OA9, 1,
    "Las situaciones y las frases escritas en cada ejercicio, lápiz y una persona de la casa para practicar.",
    "Aprenderé a prepararme antes de hablar: practicar la presentación, repetir, predecir el vocabulario clave y usar frases fijas (chunks). Sirve para hablar con más claridad y con menos pausas.",
    ["Sé saludar y pedir cosas simples.", "Conozco palabras de comida y de cortesía."],
    [
        "Antes de hablar (before speaking), prepárate. Practicar (practice) en voz alta ayuda a que las palabras salgan con más facilidad. Repetir (repeat) una frase varias veces la fija en la memoria. Pero no la memorices palabra por palabra: entiende para qué sirve. Practica con una persona de tu casa o frente a un espejo y mide cuánto tardas.",
        "Para predecir el vocabulario clave, pregúntate: ¿qué palabras usaré en esta situación? En una cafetería: sandwich, juice, coffee, price, here, to go. Hacer una lista corta de diez palabras te prepara para hablar sin buscar. Los chunks (expresiones de uso común) son grupos de palabras que se usan siempre juntos, como «Could I have…?», «I'd like…», «How much is it?». Aprender un chunk completo es más rápido que armar la frase palabra por palabra.",
        "Un buen plan de práctica tiene tres pasos: lee la lista de palabras y chunks, di las frases en voz alta tres veces y ensaya un mini diálogo completo con una persona. Si te trabas, repite el chunk desde el principio. No importa que no sea perfecto: la meta es que te entiendan.",
    ],
    [("practice", "practicar"), ("repeat", "repetir"), ("key vocabulary", "vocabulario clave"), ("chunk", "bloque de palabras que se usa junto"), ("Could I have…?", "¿Me podría dar…?"), ("I'd like…", "quisiera…")],
    [
        ("Elegir el chunk", CAFE + " ¿Qué chunk usas para pedir un sándwich de forma educada?", ["Quiero pedir con cortesía.", "El chunk completo es Could I have…?", "Could I have a sandwich, please? es la frase."], "Could I have a sandwich, please?"),
        ("Predecir vocabulario", "Situación: compras un pasaje de bus. ¿Qué palabra esperas usar? Elige: ticket / elephant.", ["Pienso en el tema: bus.", "Para viajar se compra un ticket.", "La palabra es ticket."], "ticket"),
    ],
    [
        ("Memorizar la frase sin saber para qué sirve.", "Se repite sin entender.", "Aprende cuándo usar cada chunk."),
        ("Empezar a hablar sin pensar qué palabras necesitaré.", "No se predice el vocabulario.", "Haz una lista de diez palabras del tema antes de hablar."),
    ],
    [
        # rec
        ("¿Qué significa «I'd like a juice, please»? a) quisiera un jugo, por favor b) tengo un jugo", "a) quisiera un jugo, por favor", "I'd like es una forma cortés de pedir."),
        ("¿Qué significa «to go»? a) para llevar b) para comer aquí", "a) para llevar", "En una cafetería indica un pedido para llevar."),
        ("¿Qué dice la persona al entregarte el pedido? a) Here you are b) How much is it?", "a) Here you are", "Es la frase para entregar algo."),
    ],
    [
        # und
        (CAFE + " ¿Qué chunk usas para preguntar el precio? a) How much is it? b) Here you are", "a) How much is it?", "How much pregunta por el precio."),
        (CAFE + " ¿Qué te preguntan con «Is it for here or to go?»? a) si comes aquí o lo llevas b) si pagas con tarjeta", "a) si comes aquí o lo llevas", "For here significa para comer aquí."),
        ("¿Para qué sirve repetir un chunk varias veces? a) para fijarlo en la memoria b) para cambiar su significado", "a) para fijarlo en la memoria", "La repetición ayuda a recordar."),
    ],
    [
        # app
        ("Situación: preguntas dónde está el baño. ¿Qué chunk eliges? a) Where is the bathroom? b) How much is it?", "a) Where is the bathroom?", "Where pregunta por un lugar."),
        ("Situación: pides ayuda a un profesor. ¿Qué chunk eliges? a) Could you help me, please? b) Here you are", "a) Could you help me, please?", "Es una forma educada de pedir ayuda."),
        arith("Practicas 4 chunks y los dices 3 veces cada uno. ¿Cuántas repeticiones haces en total?", "4*3", "Se multiplican los chunks por las veces."),
    ],
    [
        # rea
        ("Un compañero aprendió «I'd like a juice, please» y en la panadería necesita pedir pan. ¿Qué debe hacer? a) adaptar el chunk: I'd like some bread, please b) repetir exactamente el mismo", "a) adaptar el chunk: I'd like some bread, please", "Un chunk se adapta al nuevo producto."),
        ("Una compañera practica solo en su mente, sin decir las frases. ¿Qué le recomiendas? a) decirlas en voz alta b) no practicar más", "a) decirlas en voz alta", "Hablar en voz alta entrena la pronunciación."),
    ],
    [
        # cha
        ("Completa el chunk: «Could I try this shirt ___?» Elige: on / in.", "on", "Try on significa probarse una prenda."),
        ("¿Qué palabra predices para la situación «en el cine»? Elige: popcorn / saucepan.", "popcorn", "Se relaciona con ir al cine."),
    ],
    [
        # context
        ("Mañana pedirás una pizza por teléfono. ¿Cuál es la mejor preparación? a) practicar I'd like a pizza, please y las palabras size, price y address b) leer sobre la historia de la pizza", "a) practicar I'd like a pizza, please y las palabras size, price y address", "Prepara chunks y vocabulario de la situación.")
    ],
    [
        # selfcheck
        ("¿Qué es un chunk?", "Un grupo de palabras que se usa junto", "Se aprende como unidad."),
        ("¿Cómo practico antes de hablar?", "En voz alta y con repeticiones", "Entrena la pronunciación."),
        ("¿Qué hago para predecir vocabulario?", "Hago una lista de palabras del tema", "Me preparo para la situación."),
    ],
    task("Elige una situación (at the supermarket, at the library o at a bus stop). Escribe una lista de diez palabras clave y cuatro chunks que podrías usar. Luego practica con una persona de tu casa un mini diálogo de seis líneas y anota cuántas veces te trabaste. Si no eliges, usa «at the bus stop».", "Palabras: bus, ticket, stop, driver, seat, street, map, time, fare, school. Chunks: Excuse me, does this bus go to…? How much is the ticket? Thank you. Could you tell me when to get off? Me trabé dos veces.", ["lista diez palabras del tema", "escribe cuatro chunks útiles", "ensaya y registra"], ["hoja con lista y chunks", "nota de la persona"], ["incluir palabras sin relación con la situación", "no practicar en voz alta"], "Reconoce lo que acertó y ayuda a completar la lista con palabras más precisas."),
    "Practica los cinco chunks de la cafetería tres veces seguidas y anota cuál te costó más.",
    "Escribe en español en qué situaciones reales crees que usarías los chunks que aprendiste.",
)

# ---------------------------------------------------------------- clase 2: apoyo organizacional y visual; diagramas
PLAN = "Notas sobre «My ideal weekend»: Saturday morning: soccer; Saturday afternoon: movie with friends; Sunday morning: homework; Sunday afternoon: family lunch."

lesson(
    OA9, 2,
    "Los esquemas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a preparar un apoyo organizacional y visual y a organizar la información clave en diagramas (mapa de ideas, línea de tiempo, tabla). Sirve para hablar con orden y no perder el hilo.",
    ["Sé que una presentación tiene introducción, desarrollo y cierre.", "Conozco palabras clave de un tema."],
    [
        "El apoyo organizacional (organizational support) es una guía breve que te ayuda a ordenar lo que dirás: una lista de ideas, un esquema o un diagrama. El apoyo visual (visual support) es una imagen, un dibujo o una tarjeta con palabras clave. No es un guion para leer: es una ayuda para recordar. Sirve tanto en una presentación como en una conversación.",
        "Un diagrama (diagram) organiza la información. Un mapa de ideas (idea map) pone el tema en el centro y los datos alrededor. Una línea de tiempo (timeline) ordena hechos. Una tabla (table) compara. Elige el diagrama según lo que quieres decir. Por ejemplo, para contar tu fin de semana ideal, una tabla con día, momento y actividad es clara: «Saturday, morning, soccer».",
        "Para usar tu apoyo al hablar, mira solo las palabras clave y explica con tus palabras. Si lees todo el texto, pierdes contacto con quienes te escuchan. Revisa tu diagrama antes de hablar: ¿tiene todas las ideas?, ¿está en orden?, ¿las palabras son claras? Si la respuesta es sí, tu apoyo funciona.",
    ],
    [("organizational support", "apoyo organizacional: guía de ideas"), ("visual support", "apoyo visual: imagen o tarjeta"), ("diagram", "diagrama"), ("idea map", "mapa de ideas"), ("timeline", "línea de tiempo"), ("table", "tabla")],
    [
        ("Elegir el diagrama", "Quieres contar los pasos para hacer un sándwich. ¿Qué diagrama eliges? Elige: una línea de tiempo / un mapa de ideas.", ["Los pasos van en orden.", "La línea de tiempo ordena pasos.", "La línea de tiempo es la mejor opción."], "Una línea de tiempo"),
        ("Completar una tabla", PLAN + " ¿Qué actividad va el domingo en la mañana?", ["Busco Sunday morning.", "Las notas dicen Sunday morning: homework.", "La actividad es la tarea."], "Tarea (homework)"),
    ],
    [
        ("Escribir todo el guion en la tarjeta y leerlo.", "No se usa el apoyo como ayuda.", "Escribe solo palabras clave y explica con tus palabras."),
        ("Usar el mismo diagrama para cualquier tema.", "No se elige según lo que se quiere decir.", "Elige tabla, línea de tiempo o mapa según el tipo de información."),
    ],
    [
        # rec
        (PLAN + " ¿Qué hace el sábado en la mañana? a) fútbol b) cine", "a) fútbol", "Las notas dicen Saturday morning: soccer."),
        (PLAN + " ¿Qué hace el domingo en la tarde? a) almuerzo familiar b) tarea", "a) almuerzo familiar", "Las notas dicen Sunday afternoon: family lunch."),
        ("¿Qué diagrama pone el tema en el centro y los datos alrededor? a) un mapa de ideas b) una línea de tiempo", "a) un mapa de ideas", "El mapa de ideas parte del tema central."),
    ],
    [
        # und
        ("¿Qué es un apoyo visual? a) una imagen o tarjeta con palabras clave b) un libro completo", "a) una imagen o tarjeta con palabras clave", "Ayuda a recordar."),
        (PLAN + " ¿Qué diagrama sirve para comparar días y momentos? a) una tabla b) un mapa de Chile", "a) una tabla", "La tabla organiza filas y columnas."),
        (PLAN + " ¿Cuántas actividades hay en total?", "4", "Hay una por cada momento: dos el sábado y dos el domingo."),
    ],
    [
        # app
        ("Quieres hablar de tu semana escolar. ¿Qué diagrama eliges? a) una tabla con días y asignaturas b) un mapa del colegio", "a) una tabla con días y asignaturas", "Organiza la información por días."),
        ("Quieres presentar una historia de tu vida desde que naciste. ¿Qué diagrama eliges? a) una línea de tiempo b) un gráfico de barras", "a) una línea de tiempo", "Ordena hechos en el tiempo."),
        arith("Tu tabla tiene 5 días y 3 asignaturas por día. ¿Cuántas casillas de asignaturas tiene?", "5*3", "Se multiplican los días por las asignaturas."),
    ],
    [
        # rea
        ("Un compañero escribe 80 palabras en su tarjeta. ¿Qué le recomiendas? a) dejar solo 5 palabras clave b) agregar más palabras", "a) dejar solo 5 palabras clave", "Un apoyo debe ser breve."),
        ("Un compañero usa una línea de tiempo para comparar los precios de tres tiendas. ¿Qué diagrama sería mejor? a) una tabla b) una línea de tiempo", "a) una tabla", "Comparar datos es más claro en una tabla."),
    ],
    [
        # cha
        ("¿Qué palabra clave sirve para un mapa de ideas sobre «my pet»? Elige: name / volcano.", "name", "El nombre es un dato de la mascota."),
        ("¿Qué va en el centro de un mapa de ideas sobre tu familia? Elige: el tema (My family) / un dato menor (el nombre de mi gato).", "El tema (My family)", "El centro lleva el tema general."),
    ],
    [
        # context
        ("Vas a hablar de tu mejor amigo durante un minuto. ¿Qué apoyo preparas? a) un mapa de ideas con name, age, hobby b) un texto de una página para leer", "a) un mapa de ideas con name, age, hobby", "Son palabras clave para hablar con tus palabras.")
    ],
    [
        # selfcheck
        ("¿Qué es un diagrama?", "Un esquema que organiza información", "Ayuda a ordenar ideas."),
        ("¿Cuándo usas una línea de tiempo?", "Cuando hay hechos en orden", "Ordena el tiempo."),
        ("¿Qué escribes en un apoyo?", "Solo palabras clave", "Explicas con tus palabras."),
    ],
    task("Elige un tema (my school day, my favorite food o a trip). Dibuja en tu hoja un diagrama (mapa, línea de tiempo o tabla) con al menos cinco palabras clave y explica en español por qué lo elegiste. Luego habla durante un minuto frente a una persona usando solo tu diagrama. Si no eliges, usa «my school day».", "Tabla: Morning – math, English; Break – sandwich; Afternoon – art, sports. Elegí tabla porque son horarios. Hablé un minuto sin leer.", ["dibuja un diagrama coherente", "usa palabras clave y no oraciones", "justifica su elección"], ["dibujo del diagrama", "nota de la persona"], ["escribir oraciones largas", "elegir un diagrama que no calza con el tema"], "Reconoce el diagrama y ayuda a reducir el texto a palabras clave."),
    "Haz un mapa de ideas sobre tu fin de semana y cuéntaselo a alguien sin leer.",
    "Escribe en español qué diagrama te resulta más fácil y por qué.",
)

# ---------------------------------------------------------------- clase 3: durante el habla — gestos, rellenos y conectores
FILLERS = "Rellenos temporales (fillers): «well…», «you know…», «let me think…», «sure!», «I mean…», «so…». Gestos: señalar con la mano, contar con los dedos, abrir los brazos para decir «big»."

lesson(
    OA9, 3,
    "Las situaciones y listas escritas en cada ejercicio y una persona de la casa para practicar.",
    "Aprenderé a usar gestos y rellenos temporales (you know…, sure!, let me think…) y conectores mientras hablo. Sirve para ganar tiempo para pensar sin quedarme en silencio y para organizar mis ideas.",
    ["Sé usar and, but, so y because.", "Conozco las preguntas de la vida diaria."],
    [
        "Cuando hablas en otro idioma, a veces necesitas tiempo para pensar. Los rellenos temporales (fillers) llenan ese espacio de forma natural: «well…» (bueno…), «you know…» (sabes…), «let me think…» (déjame pensar…), «I mean…» (quiero decir…), «sure!» (¡claro!). Se usan con moderación: un par en una respuesta es natural, diez la hacen confusa.",
        "Los gestos (gestures) ayudan a comunicar cuando faltan palabras. Señalar un objeto, contar con los dedos o mostrar un tamaño con las manos transmite el significado. Combinados con frases simples son muy efectivos. «This big» con los brazos abiertos se entiende aunque no digas una palabra difícil. Los gestos también muestran que escuchas: asentir con la cabeza, sonreír.",
        "Los conectores (connectors) unen tus ideas para que suenen fluidas: and (y), but (pero), so (así que), because (porque), then (luego). «I like soccer, but I don't play every day» es más fluida que dos oraciones sueltas. Al hablar, usa un conector entre ideas y un relleno cuando necesites pensar.",
    ],
    [("filler", "relleno: palabra para ganar tiempo"), ("gesture", "gesto"), ("you know…", "sabes…"), ("let me think…", "déjame pensar…"), ("sure!", "¡claro!"), ("connector", "conector")],
    [
        ("Elegir un relleno", "Alguien te pregunta algo y necesitas pensar. ¿Qué dices? Elige: Let me think… / Goodbye.", ["Necesito tiempo para responder.", "Let me think… es un relleno.", "Es lo que dices."], "Let me think…"),
        ("Elegir un gesto", "Quieres decir «it is very big» sin palabras. ¿Qué gesto haces?", ["Quiero mostrar tamaño.", "Abro los brazos.", "El gesto muestra «big»."], "Abrir los brazos"),
    ],
    [
        ("Quedarse en silencio total cuando no se recuerda una palabra.", "No se conocen los rellenos.", "Di well… o let me think… mientras piensas."),
        ("Usar demasiados rellenos.", "Se cree que más es mejor.", "Usa uno o dos por respuesta."),
    ],
    [
        # rec
        (FILLERS + " ¿Cuál es un relleno? a) well… b) goodbye", "a) well…", "Well… se usa para ganar tiempo."),
        (FILLERS + " ¿Qué significa «sure!»? a) ¡claro! b) ¡adiós!", "a) ¡claro!", "Sure confirma una respuesta."),
        ("¿Qué conector significa «pero»? a) but b) and", "a) but", "But indica contraste."),
    ],
    [
        # und
        (FILLERS + " ¿Para qué sirve un relleno? a) para ganar tiempo al pensar b) para terminar la conversación", "a) para ganar tiempo al pensar", "Evita el silencio incómodo."),
        ("¿Qué gesto sirve para decir «three»? a) mostrar tres dedos b) cerrar los ojos", "a) mostrar tres dedos", "Contar con los dedos aclara la cifra."),
        ("¿Qué conector significa «así que»? a) so b) because", "a) so", "So indica un resultado."),
    ],
    [
        # app
        ("Completa con un conector: «I like tea, ___ I don't like coffee». Elige: but / so.", "but", "Hay un contraste entre gustar y no gustar."),
        ("Completa con un conector: «It was raining, ___ we stayed home». Elige: so / but.", "so", "Quedarse en casa es el resultado."),
        ("Completa con un conector: «I study English ___ I want to travel». Elige: because / so.", "because", "Viajar es la razón."),
    ],
    [
        # rea
        ("En una conversación dices diez veces «you know». ¿Qué pasa? a) la respuesta se vuelve confusa b) hablas con más claridad", "a) la respuesta se vuelve confusa", "El exceso de rellenos distrae."),
        ("No sabes decir «scissors», pero señalas unas tijeras y dices «this». ¿Qué estrategia usas? a) un gesto b) un relleno", "a) un gesto", "Señalar un objeto reemplaza la palabra."),
    ],
    [
        # cha
        ("¿Qué relleno y qué conector completan «___, I like music, ___ I don't play an instrument»? Relleno: Well / Goodbye. Conector: but / so.", "Well y but", "Well gana tiempo y but contrasta las dos ideas."),
        ("Ordena: but / I / like / swimming / I / can't / dive.", "I like swimming but I can't dive", "El conector but va entre las dos ideas."),
    ],
    [
        # context
        ("Un compañero te pregunta cuál es tu comida favorita y no recuerdas la palabra «lasagna». ¿Qué dices primero? a) Well, you know… it's a big pasta b) Silence", "a) Well, you know… it's a big pasta", "Usa un relleno y una descripción.")
    ],
    [
        # selfcheck
        ("¿Qué es un relleno temporal?", "Una palabra para ganar tiempo", "Un ejemplo es well."),
        ("¿Para qué sirve un conector?", "Para unir ideas", "Hace el habla más fluida."),
        ("¿Cuándo uso gestos?", "Cuando falta una palabra o quiero reforzar", "Aclaran el mensaje."),
    ],
    task("Con una persona de tu casa: ella te pregunta «What do you do on weekends?». Tú respondes en inglés con al menos un relleno (well…, you know… o let me think…), dos conectores (and, but, so o because) y un gesto. Escribe lo que dijiste y qué gesto usaste.", "Well, I play soccer on Saturdays, but on Sundays I stay home because I do homework. (Gesto: mostré con los dedos dos días.)", ["usa un relleno", "usa dos conectores", "incluye un gesto y lo describe"], ["hoja con la respuesta", "nota de la persona"], ["no usar ningún conector", "usar un relleno en cada frase"], "Reconoce lo que acertó y ayuda a revisar el uso de los conectores."),
    "Responde a tres preguntas de una persona de tu casa usando un relleno cada vez.",
    "Escribe en español qué relleno o gesto te gustaría usar más cuando te trabas al hablar.",
)

# ---------------------------------------------------------------- clase 4: parafrasear, sinónimos, pedir ayuda y apoyo visual
SYN = "Sinónimos de ejemplo: big = large; small = little; fast = quick; begin = start; happy = glad; easy = simple. Frases para pedir ayuda: «How do you say … in English?», «What's the word for…?», «Could you help me, please?», «Can you repeat that?»"

lesson(
    OA9, 4,
    "Las listas de sinónimos y las frases escritas en cada ejercicio y una persona de la casa para practicar.",
    "Aprenderé a parafrasear, usar sinónimos, solicitar ayuda y usar apoyo visual en distintos formatos mientras hablo. Sirve para seguir comunicando cuando no recuerdo una palabra.",
    ["Sé describir objetos con palabras simples.", "Conozco How do you say…?"],
    [
        "Parafrasear (to paraphrase) es decir lo mismo con otras palabras. Si olvidas «scissors», puedes decir «a tool to cut paper» (una herramienta para cortar papel). Un sinónimo (synonym) es una palabra con significado parecido: big y large, begin y start, fast y quick, happy y glad. Cuando olvidas una palabra, usa un sinónimo que conozcas o describe su función.",
        "También puedes pedir ayuda (ask for help). Frases útiles: «How do you say … in English?», «What's the word for…?», «Could you help me, please?». Pedir ayuda no es un fracaso: es una estrategia de comunicación. Muchas veces la otra persona te dará la palabra y podrás seguir. Si no te entienden, repite con otras palabras.",
        "El apoyo visual puede tener varios formatos: un dibujo, una foto, un objeto real, una tarjeta con palabras clave, una diapositiva. Si no sabes decir «glacier», muestra una foto. Para hablar con fluidez, combina las tres estrategias: describe, usa un sinónimo o muestra una imagen. Así la conversación continúa sin interrupciones.",
    ],
    [("paraphrase", "parafrasear: decirlo con otras palabras"), ("synonym", "sinónimo"), ("ask for help", "pedir ayuda"), ("How do you say…?", "¿Cómo se dice…?"), ("visual support", "apoyo visual"), ("describe", "describir")],
    [
        ("Parafrasear", "No recuerdas la palabra «scissors». ¿Qué dices? Elige: It's a tool to cut paper / It's a fruit.", ["Quiero explicar qué es sin la palabra.", "Describo su función.", "It's a tool to cut paper."], "It's a tool to cut paper"),
        ("Usar un sinónimo", SYN + " Quieres decir «big» pero no la recuerdas. ¿Qué sinónimo usas?", ["Busco la lista de sinónimos.", "Big = large.", "La palabra es large."], "large"),
    ],
    [
        ("Quedarse callado porque no se recuerda una palabra.", "No se usa el parafraseo.", "Describe la palabra con otras que conozcas."),
        ("Pedir ayuda en español sin intentar en inglés.", "Se corta la comunicación.", "Usa How do you say … in English?"),
    ],
    [
        # rec
        (SYN + " ¿Qué sinónimo tiene «begin»? a) start b) finish", "a) start", "Begin y start significan empezar."),
        (SYN + " ¿Qué sinónimo tiene «fast»? a) quick b) slow", "a) quick", "Fast y quick significan rápido."),
        (SYN + " ¿Cuál es una frase para pedir una palabra? a) How do you say … in English? b) Here you are", "a) How do you say … in English?", "Pide una palabra al interlocutor."),
    ],
    [
        # und
        (SYN + " ¿Qué sinónimo tiene «happy»? a) glad b) sad", "a) glad", "Happy y glad significan contento."),
        (SYN + " ¿Qué significa «What's the word for…?»? a) ¿Cuál es la palabra para…? b) ¿Qué hora es?", "a) ¿Cuál es la palabra para…?", "Pide una palabra."),
        ("No sabes decir «bakery». ¿Qué descripción sirve? a) It's a place where you buy bread b) It's a place where you swim", "a) It's a place where you buy bread", "Describe su función."),
    ],
    [
        # app
        ("No recuerdas «umbrella». ¿Qué dices? a) It's a thing you use when it rains b) It's a thing you eat", "a) It's a thing you use when it rains", "Describe para qué se usa."),
        (SYN + " Reemplaza «easy» por un sinónimo: «The test is ___». Elige: simple / difficult.", "simple", "Easy y simple son sinónimos."),
        ("Quieres mostrar tu mascota sin saber el nombre en inglés. ¿Qué apoyo visual usas? a) una foto b) una canción", "a) una foto", "Una foto muestra lo que no puedes decir."),
    ],
    [
        # rea
        ("Un compañero no sabe decir «flashlight» y dice: «a light you hold in your hand». ¿Qué estrategia usa? a) parafrasear b) memorizar", "a) parafrasear", "Describe la palabra con otras."),
        ("¿Por qué conviene pedir ayuda en inglés? a) para practicar y seguir la conversación b) para no hablar", "a) para practicar y seguir la conversación", "Usas el idioma para resolver la duda."),
    ],
    [
        # cha
        ("¿Qué descripción sirve para «bus» sin decir la palabra? a) It's a big vehicle for many people b) It's a small animal", "a) It's a big vehicle for many people", "Describe qué es y para qué sirve."),
        ("¿Cuál sirve para pedir la palabra en inglés de «cuaderno»? a) What's the word for cuaderno in English? b) Here you are", "a) What's the word for cuaderno in English?", "Pide la palabra al interlocutor."),
    ],
    [
        # context
        ("En una conversación olvidas «kitchen». ¿Qué haces? a) digo: the room where we cook b) cambio de tema sin decir nada", "a) digo: the room where we cook", "Parafrasear mantiene la conversación.")
    ],
    [
        # selfcheck
        ("¿Qué es parafrasear?", "Decir lo mismo con otras palabras", "Evita quedarse sin palabras."),
        ("¿Qué es un sinónimo?", "Una palabra con significado parecido", "Ejemplo: big y large."),
        ("¿Cómo pides una palabra en inglés?", "How do you say … in English?", "Es una frase de ayuda."),
    ],
    task("Con una persona de tu casa: ella señala un objeto (por ejemplo, tijeras, un vaso o una llave). Sin decir su nombre en español, describe el objeto en inglés con una frase como It's a thing you use to…. Anota las frases en tu hoja. Si no puedes, usa estos objetos: scissors, glass, key.", "Scissors: It's a tool you use to cut paper. Glass: It's a thing you use to drink water. Key: It's a small metal thing you use to open a door.", ["describe al menos dos objetos", "usa It's a thing/tool you use to…", "no menciona la palabra en español"], ["hoja con las frases", "nota de la persona"], ["decir la palabra en español", "no explicar la función"], "Reconoce lo que acertó y ayuda a completar la frase con la función del objeto."),
    "Escribe tres sinónimos que conozcas y úsalos en oraciones.",
    "Escribe en español cuál de las estrategias (parafrasear, sinónimo, pedir ayuda o apoyo visual) te resulta más útil.",
)

# ---------------------------------------------------------------- clase 5: después de hablar — registrar errores y corregirlos
ERRORS = "Registro de errores de ejemplo: 1) «He go to school» 2) «I have fifteen years» 3) «She don't like pizza» 4) «Yesterday I go to the park» 5) «My brother is more tall than me»"

lesson(
    OA9, 5,
    "El registro de errores escrito en cada ejercicio y lápiz.",
    "Aprenderé a registrar mis errores después de hablar y a corregirlos con ayuda de mi docente y de recursos como un diccionario. Sirve para mejorar con cada intento.",
    ["Sé el presente simple y el pasado simple.", "Conozco los comparativos con -er."],
    [
        "Después de hablar (after speaking), revisa cómo te fue. Un registro de errores (error log) es una tabla donde anotas lo que dijiste mal, la forma correcta y el tipo de error: verbo, orden de palabras, vocabulario o pronunciación. Registrar no es para sentirse mal: es para ver qué patrones se repiten y qué practicar.",
        "Corregir con ayuda significa pedir a tu docente o a otra persona que revise tu registro, y usar recursos como un diccionario o un libro de gramática. Ejemplos de correcciones: «He go to school» → «He goes to school» (con he/she/it el verbo lleva -s); «I have fifteen years» → «I am fifteen years old» (la edad se dice con to be); «She don't like» → «She doesn't like»; «Yesterday I go» → «Yesterday I went» (pasado); «more tall» → «taller».",
        "Para mejorar, elige un error por semana y practícalo en voz alta con ejemplos nuevos. Escribe una meta, como: «This week I will use -s with he/she/it». Al final de la semana, comprueba si volviste a cometer el error. Si disminuyó, ¡es progreso!",
    ],
    [("error log", "registro de errores"), ("correct form", "forma correcta"), ("pattern", "patrón: algo que se repite"), ("dictionary", "diccionario"), ("goal", "meta"), ("feedback", "retroalimentación")],
    [
        ("Corregir un error de verbo", ERRORS + " Corrige el error 1.", ["La frase es He go to school.", "Con he se agrega -s al verbo.", "La forma correcta es He goes to school."], "He goes to school"),
        ("Clasificar un error", ERRORS + " El error 4 («Yesterday I go») ¿es de verbo en pasado o de pronunciación?", ["Yesterday indica pasado.", "El verbo go debe estar en pasado.", "Es un error de verbo en pasado."], "De verbo en pasado"),
    ],
    [
        ("Anotar solo «mal» sin decir cuál es la forma correcta.", "No se corrige.", "Anota siempre la forma correcta."),
        ("Practicar todos los errores a la vez.", "Se pierde el foco.", "Elige un error por semana."),
    ],
    [
        # rec
        (ERRORS + " Corrige el error 2: «I have fifteen years». a) I am fifteen years old b) I has fifteen year", "a) I am fifteen years old", "La edad se dice con to be."),
        (ERRORS + " Corrige el error 3: «She don't like pizza». a) She doesn't like pizza b) She not like pizza", "a) She doesn't like pizza", "Con she se usa doesn't."),
        (ERRORS + " Corrige el error 5: «more tall». a) taller b) tallest", "a) taller", "Los adjetivos cortos usan -er."),
    ],
    [
        # und
        (ERRORS + " ¿Qué tipo de error es «My brother is more tall than me»? a) de comparativo b) de pronunciación", "a) de comparativo", "Se mezcla more con un adjetivo corto."),
        (ERRORS + " Corrige el error 4: «Yesterday I go to the park». a) Yesterday I went to the park b) Yesterday I goed to the park", "a) Yesterday I went to the park", "El pasado de go es went."),
        ("¿Para qué sirve un registro de errores? a) para ver qué debo practicar b) para castigar", "a) para ver qué debo practicar", "Muestra los patrones."),
    ],
    [
        # app
        ("Corrige: «They is happy». a) They are happy b) They am happy", "a) They are happy", "Con they se usa are."),
        ("Corrige: «I no like fish». a) I don't like fish b) I not like fish", "a) I don't like fish", "Con I se usa don't."),
        arith("En tu registro hay 5 errores. Corriges 3 con tu docente. ¿Cuántos faltan por corregir?", "5-3", "Se restan los corregidos del total."),
    ],
    [
        # rea
        (ERRORS + " ¿Qué patrón se repite en los errores 1 y 3? a) la forma del verbo con he o she b) los números", "a) la forma del verbo con he o she", "En ambos, el sujeto es he o she."),
        ("Tu docente te sugiere practicar solo un error por semana. ¿Por qué? a) para enfocarte y avanzar b) para no corregir nada", "a) para enfocarte y avanzar", "Un foco por vez mejora más."),
    ],
    [
        # cha
        ("Escribe tu meta de la semana usando el error 1: «This week I will use ___ with he, she and it».", "-s", "El verbo lleva -s con he, she y it."),
        ("Escribe la forma correcta de «He have a dog».", "He has a dog", "Con he se usa has."),
    ],
    [
        # context
        ("Hablaste con un compañero y dijiste «We was happy». ¿Qué anotas en tu registro? a) «We were happy» como forma correcta b) «mal» sin más", "a) «We were happy» como forma correcta", "Siempre se anota la corrección.")
    ],
    [
        # selfcheck
        ("¿Qué es un registro de errores?", "Una tabla con errores y sus correcciones", "Muestra qué practicar."),
        ("¿Con quién corriges tus errores?", "Con tu docente y con recursos como un diccionario", "Te dan la forma correcta."),
        ("¿Cuántos errores practicas a la vez?", "Uno por semana", "Así te concentras."),
    ],
    task("Con una persona de tu casa: cuéntale en inglés durante un minuto qué hiciste ayer. Pídele que anote dos errores que escuche. Escribe en tu hoja una tabla con tres columnas: lo que dije, la forma correcta y el tipo de error. Luego escribe una meta para la próxima semana. Si no puedes, corrige estos tres errores: «I go yesterday», «She have a cat», «He more big».", "Lo que dije: I go yesterday → I went yesterday (verbo en pasado). She have a cat → She has a cat (verbo con she). He more big → He is bigger (comparativo). Meta: usar el pasado de los verbos irregulares.", ["registra los errores con su forma correcta", "indica el tipo de error", "escribe una meta"], ["tabla con tres columnas", "nota de la persona"], ["no anotar la forma correcta", "escribir una meta vaga"], "Reconoce el registro y ayuda a escribir la forma correcta en cada caso."),
    "Revisa un texto corto que hayas escrito en inglés y registra dos errores con su corrección.",
    "Escribe en español qué error te gustaría eliminar este mes y cómo lo practicarías.",
)
