"""Cuaderno del estudiante, 1.º medio Inglés (propuesta), EN1M OA 02 (propósito, detalle, lenguaje y sonidos al escuchar).

Las «escuchas» las lee un adulto en voz alta con el guion escrito en el enunciado. En la clase de sonidos el adulto lee las palabras
de cada par; no hay audio externo. Textos originales con pista en español.
"""
from __future__ import annotations

from student_content_en_m1_a import ADULT, MAT, lesson
from student_content_ma01_b import task
from student_lessons import arith

OA2 = "EN1M OA 02"

# ================================================================ OA 02 · clase 1: propósito, tema e idea general
DESERT = "«The flowering desert is a natural event in northern Chile. It happens in some years, when there is more rain than usual. Seeds under the sand wake up, and the desert fills with flowers. Many tourists visit it, so visitors must walk only on the paths to protect the flowers.» (flowering = florido, event = fenómeno, seeds = semillas, sand = arena, wake up = despiertan, paths = senderos, protect = proteger)"
PODCAST = "«Welcome to Teen Voices. Today I want to talk about sleep. Some students sleep only six hours on school days, but teenagers need between eight and ten hours. Sleep helps memory and mood. So tonight, put your phone away thirty minutes before bed.» (sleep = dormir, memory = memoria, mood = ánimo, put away = guardar, before bed = antes de dormir)"
BIKE = "«Why are more people using bicycles in the city? Cyclists say that it is cheap, fast and good for health. However, they also say that there are not enough safe lanes. The city plans to build new lanes next year.» (cheap = barato, health = salud, however = sin embargo, lanes = ciclovías, plans = planea, build = construir)"
SWAP = "«Hello, listeners. Today's topic is old clothes. Instead of throwing clothes away, you can bring them to a swap fair. This Saturday, the neighborhood swap fair opens at eleven.» (throwing away = botar, swap fair = feria de intercambio, neighborhood = barrio)"

lesson(
    OA2, 1, MAT,
    "Aprenderé a identificar el propósito, el tema y las ideas relevantes de un texto oral sobre un tema poco conocido. Sirve para entender de qué trata una charla o un podcast sin necesitar cada palabra.",
    ["Sé reconocer si un texto informa, convence o cuenta.", "Sé usar so y however en español: «por eso» y «sin embargo»."],
    [
        "El tema (topic) es de qué trata el texto, y se dice en pocas palabras: «el desierto florido», «el sueño de los adolescentes». El propósito (purpose) es lo que el hablante quiere lograr: informar (inform), convencer (persuade) o entretener (entertain). La idea general (gist) une el tema con lo más importante que se dice sobre él. Las ideas relevantes (main ideas) son las pocas que sostienen esa idea general; los ejemplos son detalles.",
        "Cuando el tema es poco conocido, no te frenes en las palabras nuevas. Escucha el inicio (suele presentar el tema), las palabras que se repiten (flowers, sleep, lanes) y las palabras que anuncian consecuencias o recomendaciones: so (por eso), however (sin embargo), must (debe). Un hablante que dice «tonight, put your phone away» quiere convencer; uno que explica cómo ocurre un fenómeno quiere informar.",
        "Para resumir la idea general usa esta fórmula: tema + lo más importante. Por ejemplo: «El desierto de Chile florece cuando llueve más y hay que cuidarlo». Si tu resumen incluye muchos números o nombres, es un detalle y no una idea general.",
    ],
    [("topic", "tema: de qué trata el texto"), ("gist", "idea general del texto"), ("main idea", "idea relevante"), ("persuade", "convencer"), ("so", "por eso, de modo que"), ("however", "sin embargo")],
    [
        ("Tema y propósito", ADULT + DESERT + " ¿Cuál es el tema y para qué se dice?", ["El inicio presenta el tema: the flowering desert.", "Explica cuándo ocurre y pide caminar por los senderos.", "Informa y además pide cuidar el lugar."], "Tema: el desierto florido del norte de Chile. Propósito: informar y pedir que lo cuiden"),
        ("Idea general", ADULT + BIKE + " ¿Cuál es la idea general?", ["Veo lo que se repite: bicycles y lanes.", "Las ventajas de la bicicleta aparecen antes de However.", "Después de However aparece el problema: faltan ciclovías seguras."], "Más gente usa bicicleta, pero faltan ciclovías seguras y la ciudad planea construirlas"),
    ],
    [
        ("Resumir con un detalle (un número) y no con la idea general.", "Se recuerda un dato suelto y no el mensaje.", "Resume con tema + lo más importante, sin cifras."),
        ("Pensar que, si no entiendo una palabra, no entiendo el texto.", "Se traduce palabra por palabra.", "Apóyate en el inicio, las palabras repetidas y las señales como so y however."),
    ],
    [
        (ADULT + DESERT + " ¿Qué ocurre con las semillas bajo la arena cuando llueve más que de costumbre? A) despiertan y el desierto se llena de flores B) se secan y quedan bajo la arena", "A) despiertan y el desierto se llena de flores", "El guion dice Seeds under the sand wake up."),
        (ADULT + DESERT + " ¿Qué hace que florezca el desierto?", "Que llueva más que de costumbre", "El guion dice when there is more rain than usual."),
        (ADULT + BIKE + " ¿Qué medio de transporte se menciona?", "La bicicleta", "El texto empieza con Why are more people using bicycles?"),
    ],
    [
        (ADULT + PODCAST + " ¿Cuál es el propósito principal? A) convencer de dormir más B) entretener con una historia sobre un teléfono perdido", "A) convencer de dormir más", "Termina con una recomendación: put your phone away before bed."),
        (ADULT + DESERT + " ¿Para qué piden caminar solo por los senderos?", "Para proteger las flores", "El guion dice walk only on the paths to protect the flowers."),
        (ADULT + BIKE + " ¿Qué plan anuncia la ciudad? A) construir nuevas ciclovías el próximo año B) prohibir las bicicletas en el centro", "A) construir nuevas ciclovías el próximo año", "El guion dice The city plans to build new lanes next year."),
    ],
    [
        (ADULT + PODCAST + " ¿Cuántas horas de sueño necesita un adolescente según el guion?", "Entre 8 y 10 horas", "Dice between eight and ten hours."),
        arith(ADULT + PODCAST + " Una estudiante duerme seis horas y necesita al menos ocho. ¿Cuántas horas le faltan?", "8-6", "Se resta lo que duerme de lo que necesita."),
        (ADULT + BIKE + " ¿Qué razones dan los ciclistas para usar la bicicleta? Escribe cuántas razones dan.", "3", "Dicen que es barata, rápida y buena para la salud."),
    ],
    [
        (ADULT + DESERT + " ¿Qué palabra introduce la consecuencia en «Many tourists visit it, so visitors must walk only on the paths»? A) so B) many", "A) so", "So significa por eso: muestra la consecuencia de que lleguen muchos turistas."),
        (ADULT + PODCAST + " Un compañero dice que el podcast pide dormir con el teléfono al lado. ¿Es correcto? A) no, pide guardarlo treinta minutos antes de dormir B) sí, lo recomienda", "A) no, pide guardarlo treinta minutos antes de dormir", "El guion dice put your phone away thirty minutes before bed."),
    ],
    [
        (ADULT + BIKE + " However introduce un contraste. ¿Qué dos ideas contrasta? A) las ventajas de la bicicleta y la falta de ciclovías seguras B) la bicicleta y el tren", "A) las ventajas de la bicicleta y la falta de ciclovías seguras", "Antes de however hay ventajas y después una falta."),
        (ADULT + DESERT + " ¿Qué dos ideas relevantes tiene el texto? A) el desierto florece con más lluvia y los visitantes deben cuidar las flores B) el desierto florece todos los años y los turistas pueden caminar donde quieran", "A) el desierto florece con más lluvia y los visitantes deben cuidar las flores", "Son las ideas que sostienen el mensaje; el resto no se dice."),
    ],
    [(ADULT + SWAP + " ¿Qué pueden hacer con la ropa que ya no usan?", "Llevarla a la feria de intercambio del barrio", "El guion dice bring them to a swap fair.")],
    [
        ("¿Qué es la idea general de un texto?", "El tema junto con lo más importante que se dice de él", "No es un detalle suelto."),
        ("¿Qué significa so en una frase como «so visitors must…»?", "Por eso", "Introduce una consecuencia."),
        ("¿Qué propósito tiene un texto que termina con una recomendación como «put your phone away»?", "Convencer", "Una recomendación busca cambiar la conducta."),
    ],
    task("Un adulto lee dos veces este texto original: «Humboldt penguins live on the coast of Chile and Peru. They eat small fish. Fishing boats and pollution are problems for them, so some groups protect their nesting places.» (penguins = pingüinos, coast = costa, fish = peces, pollution = contaminación, nesting places = lugares de anidación). En tu hoja escribe: el tema, el propósito y dos ideas relevantes.", "Tema: los pingüinos de Humboldt. Propósito: informar. Ideas: viven en la costa de Chile y Perú y comen peces pequeños; los barcos de pesca y la contaminación los afectan, por eso hay grupos que protegen sus lugares de anidación.", ["nombra el tema con precisión", "indica un propósito coherente", "da dos ideas relevantes y no solo cifras"], ["hoja con tres respuestas", "nota del adulto"], ["decir que el propósito es vender", "responder solo con un detalle como small fish"], "Valora la idea relevante y repasa con la persona la señal so para encontrar la consecuencia."),
    "Pide a un adulto que lea otra vez el podcast sobre el sueño y escribe una frase de idea general.",
    "Escribe en español el tema, el propósito y la idea general de una charla que hayas escuchado en el colegio.",
)

# ---------------------------------------------------------------- clase 2: detalles, opiniones y problema-solución
GARDEN = "«At our school, snails were eating the lettuce in the garden. This was a big problem for the first-year class. The students tried watering at night, but it made things worse. Then they collected the snails by hand every morning and took them to a far corner of the yard. Rocío said, It is boring, but it works. After two weeks, the lettuce grew well.» (snails = caracoles, lettuce = lechuga, watering = regar, worse = peor, collected = recogieron, far corner = rincón lejano, grew = creció)"
OPIN = "«Tomás: I love football. It is exciting. Marina: I prefer chess. It is calm, and you have to think. Tomás: But chess is slow! Marina: Slow, yes, but I never get hurt!» (exciting = emocionante, calm = tranquilo, slow = lento, get hurt = lastimarse)"
FAIR = "«The science fair is on Wednesday at ten in the gym. Ms. Rivas will give the opening speech. Students from the first year will present their experiments in room three, and students from the second year in room four.» (science fair = feria científica, opening speech = discurso de apertura, experiments = experimentos, room = sala)"
BUSLATE = "«Attention, passengers. The bus to the airport is late because of the rain. The new departure time is ten past six. Please wait in the main hall.» (late = atrasado, because of = a causa de, departure = salida, main hall = sala principal)"

lesson(
    OA2, 2, MAT,
    "Aprenderé a encontrar información específica (personas, acciones, opiniones, lugares y tiempo) y las relaciones de contraste y problema-solución en un texto oral. Sirve para responder preguntas de detalle sin perder la idea del texto.",
    ["Sé reconocer la idea general de un texto oral.", "Sé que but significa «pero»."],
    [
        "Los detalles clave (key details) responden quién, qué hizo, dónde, cuándo y qué opina. En el texto del huerto: quiénes (the first-year class), qué hicieron (collected the snails), dónde (a far corner of the yard) y cuándo (every morning, after two weeks). Una opinión (opinion) dice lo que alguien piensa y suele traer adjetivos: exciting, calm, slow, boring.",
        "Las relaciones entre ideas se anuncian con palabras señal. But, however y although marcan contraste: la segunda parte se opone a la primera. En un esquema problema-solución (problem-solution) primero aparece una dificultad (snails were eating the lettuce), luego intentos (watering at night, que empeoró las cosas), después la solución (collected the snails by hand) y al final el resultado (the lettuce grew well).",
        "Para no equivocarte, contesta con la palabra exacta: si preguntan «¿cuándo?», da un tiempo; si preguntan «¿quién opina?», nombra a la persona. Cuando haya varias opiniones, asigna cada una a su hablante con una pista: Tomás dice I love football; Marina dice I prefer chess.",
    ],
    [("key detail", "detalle clave"), ("opinion", "opinión: lo que alguien piensa"), ("problem-solution", "problema-solución: primero una dificultad y luego cómo se resolvió"), ("contrast", "contraste: dos ideas que se oponen"), ("but", "pero"), ("result", "resultado")],
    [
        ("Problema y solución", ADULT + GARDEN + " ¿Cuál era el problema y cuál fue la solución que funcionó?", ["El problema aparece al inicio: snails were eating the lettuce.", "El primer intento, regar de noche, empeoró las cosas.", "La solución fue recoger los caracoles a mano cada mañana y llevarlos lejos."], "Problema: caracoles comían la lechuga. Solución: recogerlos a mano cada mañana y llevarlos a un rincón lejano"),
        ("Contraste de opiniones", ADULT + OPIN + " ¿Qué opina cada uno del juego que prefiere?", ["Tomás dice que el fútbol es emocionante.", "Marina dice que el ajedrez es tranquilo y hay que pensar.", "But marca el contraste: Tomás lo encuentra lento."], "Tomás: el fútbol es emocionante. Marina: el ajedrez es tranquilo"),
    ],
    [
        ("Atribuir una opinión a la persona equivocada.", "No se anota quién habla.", "Junto a cada opinión escribe la inicial del hablante."),
        ("Creer que lo primero que se intentó resolvió el problema.", "Se ignoran palabras como but y worse.", "Sigue el orden: problema, intentos, solución, resultado."),
    ],
    [
        (ADULT + GARDEN + " ¿Qué comían los caracoles?", "La lechuga del huerto", "El guion dice snails were eating the lettuce."),
        (ADULT + FAIR + " ¿Qué día es la feria científica?", "El miércoles a las diez", "Dice on Wednesday at ten."),
        (ADULT + OPIN + " ¿Qué juego prefiere Marina?", "El ajedrez", "Ella dice I prefer chess."),
    ],
    [
        (ADULT + GARDEN + " ¿Adónde llevaron los caracoles? A) a un rincón lejano del patio B) a la sala del primer año", "A) a un rincón lejano del patio", "El guion dice took them to a far corner of the yard."),
        (ADULT + FAIR + " ¿Dónde presentan sus experimentos los estudiantes de primer año? A) en la sala tres B) en la sala cuatro", "A) en la sala tres", "El guion dice first year… in room three."),
        (ADULT + OPIN + " ¿Qué opina Tomás del ajedrez? A) que es lento B) que es tranquilo", "A) que es lento", "Tomás dice But chess is slow."),
    ],
    [
        (ADULT + GARDEN + " ¿Qué resultado se vio después de dos semanas de recoger los caracoles?", "La lechuga creció bien", "El guion cierra con After two weeks, the lettuce grew well."),
        (ADULT + FAIR + " ¿Quién da el discurso de apertura?", "La Sra. Rivas", "Dice Ms. Rivas will give the opening speech."),
        (ADULT + BUSLATE + " ¿Por qué se atrasa el bus?", "A causa de la lluvia", "El guion dice because of the rain."),
    ],
    [
        (ADULT + OPIN + " ¿Qué palabra marca el contraste en «Slow, yes, but I never get hurt»? A) but B) never", "A) but", "But opone la lentitud con la ventaja de no lastimarse."),
        (ADULT + GARDEN + " Rocío dice «It is boring, but it works». ¿Qué opina? A) que es aburrido pero funciona B) que no funciona", "A) que es aburrido pero funciona", "La primera parte critica y but introduce el valor."),
    ],
    [
        (ADULT + GARDEN + " Un compañero dice que regar de noche resolvió el problema. ¿Qué dato del guion lo corrige? A) it made things worse B) the lettuce grew well", "A) it made things worse", "Regar de noche empeoró las cosas; lo que funcionó fue recoger los caracoles."),
        (ADULT + FAIR + " ¿Qué cursos presentan experimentos? A) primer y segundo año B) segundo y tercer año", "A) primer y segundo año", "El guion nombra first year y second year."),
    ],
    [(ADULT + BUSLATE + " ¿A qué hora es la nueva salida? A) a las seis y diez B) a las diez para las seis", "A) a las seis y diez", "Ten past six significa seis y diez.")],
    [
        ("¿Qué orden sigue un texto de problema-solución?", "Problema, intentos, solución y resultado", "Así se organizan las ideas."),
        ("¿Qué indican palabras como but y however?", "Un contraste", "La segunda idea se opone a la primera."),
        ("¿Para qué sirve anotar la inicial de cada hablante?", "Para no atribuir una opinión a la persona equivocada", "Así se separan las voces."),
    ],
    task("Un adulto lee dos veces este texto original: «Last week, our class had a problem. The computer room was noisy and nobody could finish the test. Ms. Soto asked us to use quiet voices, but the room was still noisy. Then Camilo suggested a signal: a green card means quiet. After that, everyone finished the test.» (noisy = ruidoso, finish = terminar, suggested = sugirió, signal = señal, card = tarjeta). En tu hoja escribe: el problema, el intento que no funcionó, la solución y el resultado.", "Problema: la sala de computación estaba ruidosa y nadie terminaba la prueba. Intento: pedir voces bajas, pero siguió el ruido. Solución: Camilo propuso una tarjeta verde que significa silencio. Resultado: todos terminaron la prueba.", ["separa las cuatro partes", "cita al menos un detalle del guion", "mantiene el orden del texto"], ["hoja con cuatro respuestas", "nota del adulto"], ["decir que la solución fue pedir voces bajas", "omitir el resultado"], "Reconoce lo bien ubicado y relee con la persona las palabras but y Then para separar intento y solución."),
    "Pide a un adulto que lea otra vez el diálogo de Tomás y Marina y escribe una opinión propia sobre el deporte que prefieres.",
    "Escribe en español un problema pequeño de tu colegio y dos formas de resolverlo.",
)

# ---------------------------------------------------------------- clase 3: conectores, colocaciones y modismos
CHORE = "«Last Saturday I wanted to find my old guitar, so I decided to clean my room. First, I made my bed. Later, I took a break and had lunch. Although I was tired, I did my homework, too. Both my brother and my sister helped me so that I could finish before dinner. Last, I found the guitar. It was a piece of cake!» (made my bed = tendí la cama, took a break = hice una pausa, had lunch = almorcé, did my homework = hice la tarea, finish = terminar, dinner = cena, piece of cake = muy fácil)"

lesson(
    OA2, 3, MAT,
    "Aprenderé a reconocer conectores (later, last, so that, although, both), combinaciones frecuentes de palabras (collocations) y modismos al escuchar. Sirve para entender cómo se relacionan las ideas y no traducir palabra por palabra.",
    ["Sé first, then, but y because.", "Sé el pasado simple de verbos comunes (made, took, had, did)."],
    [
        "Los conectores (connectors) unen ideas. Later (más tarde) y last (por último) ordenan acciones en el tiempo, igual que first. So that (para que) indica propósito: «I could finish before dinner». Although (aunque) introduce un contraste: «Although I was tired, I did my homework». Both (los dos) se usa para hablar de dos personas a la vez: «Both my brother and my sister helped me».",
        "Las combinaciones frecuentes (collocations) son palabras que casi siempre van juntas. En inglés se hace la cama (make a bed), se hace una pausa (take a break), se almuerza (have lunch) y se hace la tarea (do homework). Si dices «do a break» o «make homework», suena extraño aunque se entienda. Aprenderlas como bloque es más útil que traducir cada palabra.",
        "Un modismo (idiom) es una expresión cuyo sentido no se saca de las palabras sueltas. A piece of cake no habla de pastel: significa que algo fue muy fácil. Cuando oigas una expresión extraña, pregúntate si el sentido literal encaja con la situación. Aquí la persona encontró la guitarra y estaba contenta, así que «muy fácil» tiene sentido.",
    ],
    [("connector", "conector: palabra que une ideas"), ("although", "aunque"), ("so that", "para que"), ("both", "los dos"), ("collocation", "combinación frecuente: make a bed, take a break"), ("idiom", "modismo: expresión con sentido figurado")],
    [
        ("Reconocer el conector", ADULT + CHORE + " ¿Qué conector muestra el contraste «estaba cansado, pero hizo la tarea»?", ["Busco la idea que se opone: tired y did my homework.", "La frase dice Although I was tired.", "Although introduce el contraste."], "Although"),
        ("Colocaciones", ADULT + CHORE + " ¿Qué verbo va con break en el guion?", ["Busco la palabra break.", "El guion dice took a break.", "La colocación es take a break."], "Took (take a break)"),
    ],
    [
        ("Traducir a piece of cake como «un pedazo de pastel».", "Se interpreta el modismo de forma literal.", "Revisa si el sentido literal encaja; si no, busca un sentido figurado como «muy fácil»."),
        ("Decir make homework en lugar de do homework.", "Se traduce hacer siempre con make.", "Aprende la colocación completa: do homework, make a bed."),
    ],
    [
        (ADULT + CHORE + " ¿Qué quería encontrar la persona? A) su guitarra vieja B) su cuaderno", "A) su guitarra vieja", "El guion dice I wanted to find my old guitar."),
        (ADULT + CHORE + " ¿Qué hizo primero? A) tendió su cama B) almorzó", "A) tendió su cama", "La palabra First introduce I made my bed."),
        (ADULT + CHORE + " ¿Qué verbo va con lunch en el guion?", "Had (have lunch)", "El guion dice had lunch."),
    ],
    [
        (ADULT + CHORE + " ¿Qué conector expresa propósito, «para que pudiera terminar antes de la cena»? A) so that B) although", "A) so that", "So that introduce para qué ayudaron los hermanos."),
        (ADULT + CHORE + " ¿Qué significa both en «Both my brother and my sister helped me»? A) los dos B) ninguno de los dos", "A) los dos", "Both se usa para hablar de dos personas a la vez."),
        (ADULT + CHORE + " ¿Qué quiere decir que fue a piece of cake?", "Que fue muy fácil", "Es un modismo para algo sencillo."),
    ],
    [
        ("Une cada conector con su función. 1) later 2) although 3) so that Funciones: a) contraste b) propósito c) orden en el tiempo", "1-c, 2-a, 3-b", "Later ordena, although opone ideas y so that explica para qué."),
        (ADULT + CHORE + " ¿Qué conector usa la persona para presentar el último paso? A) Last B) Later", "A) Last", "El guion dice Last, I found the guitar."),
        (ADULT + CHORE + " ¿Qué hizo después del almuerzo? A) tarea B) tendió la cama", "A) tarea", "Tras Later y lunch viene Although… I did my homework."),
    ],
    [
        ("Completa con la colocación correcta: «Every morning I ____ my bed.» A) make B) do", "A) make", "En inglés se dice make the bed, no do the bed."),
        (ADULT + CHORE + " ¿Qué dos personas ayudaron? A) su hermano y su hermana B) su madre y su padre", "A) su hermano y su hermana", "El guion dice Both my brother and my sister."),
    ],
    [
        ("Elige el modismo que significa «muy fácil»: A) a piece of cake B) a piece of pie", "A) a piece of cake", "Solo la primera se usa con ese sentido figurado."),
        ("Completa: «____ it was raining, we played football.» A) Although B) So that", "A) Although", "Hay un contraste entre la lluvia y jugar; so that no tiene sentido."),
    ],
    [(ADULT + "«Last night my cousins arrived from Osorno. Both Emilia and Joaquín brought gifts. We cooked dinner together so that everyone could rest early. Although it was late, we talked for an hour.» (cousins = primos, brought = trajeron, gifts = regalos, rest = descansar, late = tarde). ¿Para qué cocinaron juntos?", "Para que todos descansaran temprano", "So that introduce el propósito.")],
    [
        ("¿Qué indica el conector although?", "Un contraste", "Une dos ideas que se oponen."),
        ("¿Qué es una colocación?", "Una combinación de palabras que suelen ir juntas", "Por ejemplo, take a break."),
        ("¿Por qué no se traduce un modismo palabra por palabra?", "Porque su sentido es figurado", "El sentido no sale de las palabras sueltas."),
    ],
    task("Un adulto lee dos veces este texto original: «Last Sunday, my aunt and I baked bread. First, we made the dough. Later, we took a break and drank tea. Although the oven was hot, we opened it to check the bread. Both of us loved the smell. It was a piece of cake!» (baked = horneamos, dough = masa, oven = horno, check = revisar, smell = olor). En tu hoja escribe: dos conectores que oíste y para qué sirven, una colocación y el significado del modismo.", "Conectores: Later (orden en el tiempo) y Although (contraste); también Both (los dos). Colocación: took a break / made the dough. Modismo: a piece of cake significa que fue muy fácil.", ["identifica dos conectores y su función", "nombra una colocación del guion", "explica el modismo con su sentido figurado"], ["hoja con cuatro respuestas", "nota del adulto"], ["traducir el modismo literalmente", "confundir although con so that"], "Reconoce los conectores acertados y repasa con la persona qué tipo de relación marca cada uno."),
    "Pide a un adulto que lea otra vez el texto de la guitarra y subraya todos los conectores.",
    "Escribe en español tres colocaciones de tu rutina (por ejemplo, hacer la tarea) y cómo las dirías en inglés.",
)

# ---------------------------------------------------------------- clase 4: sonidos
lesson(
    OA2, 4, "Las listas de palabras escritas en cada ejercicio; un adulto las lee en voz alta (o las dices tú mismo/a y te grabas); lápiz y hoja.",
    "Aprenderé a distinguir los sonidos vocales largos y cortos (feet/fit), las combinaciones tr y dr, el sonido inicial /j/ (year, yes) y el final -tion (vacation). Sirve para entender y pronunciar palabras que se parecen pero significan cosas distintas.",
    ["Sé que las vocales del inglés tienen más sonidos que las del español.", "Conozco las letras del abecedario inglés."],
    [
        "En inglés, la vocal larga /iː/ (feet, sheep, seat) dura más y se pronuncia con la boca estirada. La vocal corta /ɪ/ (fit, ship, sit) es breve y relajada. Cambiar de vocal cambia la palabra: sheep es «oveja» y ship es «barco». Los hispanohablantes tienden a decir las dos como la «i» del español, y por eso se confunden. Una pista: las letras ee y ea suelen dar el sonido largo; una i sola entre consonantes suele dar el corto.",
        "Al comienzo de palabra, tr suena como «chr» (tree, train, try) y dr como «jr» (dress, drain, dry). No separes la t o la d de la r. El sonido inicial /j/ de year y yes se parece a la «y» de «yo», pero más suave; no es el sonido de jet, que empieza con /dʒ/. Por eso year no se pronuncia como «jir». Compara yet (todavía) con jet (avión a reacción).",
        "El final -tion suena «shən»: vacation, station, information, invitation. Nunca se dice «tion» con t. Para entenderlo al escuchar, no busques la t: busca el sonido «sh» seguido de una vocal breve. Practica en voz alta con un adulto: dilo despacio, después rápido y escucha si puedes oír la diferencia entre cada par.",
    ],
    [("long vowel", "vocal larga /iː/: feet, sheep"), ("short vowel", "vocal corta /ɪ/: fit, ship"), ("tr / dr", "tree suena como «chri»; dress suena como «jres»"), ("/j/", "sonido de year y yes, como la y de «yo»"), ("-tion", "terminación que suena «shən»: vacation"), ("minimal pair", "par de palabras que cambian por un solo sonido")],
    [
        ("Vocal larga o corta", "El adulto lee las dos palabras en voz alta: «seat» y «sit». ¿Cuál tiene la vocal más larga?", ["Seat lleva ea, que suele dar el sonido largo /iː/.", "Sit lleva una i sola entre consonantes: sonido corto /ɪ/.", "Por eso la vocal larga está en seat."], "Seat"),
        ("Terminación -tion", "Un adulto lee: «vacation, station, information». ¿Cómo suena el final de las tres palabras?", ["Las tres terminan en -tion.", "La t se une a la i y suena sh.", "El final es shən."], "Como «shən»"),
    ],
    [
        ("Pronunciar year como «jir».", "Se confunde el sonido /j/ con /dʒ/.", "Empieza la palabra con la y de «yo», sin presionar la lengua."),
        ("Pronunciar tion con t.", "Se lee como en español.", "Recuerda que -tion suena shən."),
    ],
    [
        ("Clasifica por la vocal: seat, sit, sheep, ship. Escribe cuáles tienen vocal larga y cuáles corta.", "Largas: seat, sheep. Cortas: sit, ship", "Ea y ee dan el sonido largo; la i sola entre consonantes da el corto."),
        ("¿Cuál palabra significa «barco»? A) sheep B) ship", "B) ship", "Sheep es oveja; ship tiene vocal corta y es barco."),
        ("¿Cuál de estas palabras termina con el sonido «shən»? A) vacation B) vacant", "A) vacation", "Vacation termina en -tion; vacant termina en -ant."),
    ],
    [
        ("Un adulto lee en voz alta «dry» y «try». ¿Cómo suenan las consonantes iniciales?  A) dry como «jrai» y try como «chrai» B) las dos como «trai»", "A) dry como «jrai» y try como «chrai»", "Dr se acerca a «jr» y tr a «chr»."),
        ("¿Cuál de estas palabras empieza con el sonido /j/ de yo? A) year B) jet", "A) year", "Year empieza con /j/; jet empieza con /dʒ/."),
        ("Un adulto lee dos palabras: «feet» y «fit». Feet significa «pies». ¿Cuál es la de vocal más larga?", "Feet", "Feet lleva ee y fit lleva una i breve."),
    ],
    [
        ("¿Cuál palabra termina con el sonido «sh» más una vocal breve? A) station B) stand", "A) station", "Station termina en -tion, que suena shən."),
        ("El adulto lee «leave» y «live». Leave significa «irse». ¿Cuál tiene la vocal larga? A) leave B) live", "A) leave", "Leave lleva ea y su vocal es larga; live tiene la i corta."),
        ("¿Cómo suena la combinación inicial de «tree»? A) como «chri» B) como «dri»", "A) como «chri»", "Tr suena parecido a chr; dr suena parecido a jr."),
    ],
    [
        ("Une las palabras con su par que cambia solo la vocal. 1) bean 2) cheap 3) heel Pares: a) hill b) bin c) chip", "1-b, 2-c, 3-a", "Bean/bin, cheap/chip y heel/hill cambian vocal larga por corta."),
        ("La profesora dice: «The ____ is in the harbor.» La palabra es la que significa «barco». ¿Cuál escribes? A) ship B) sheep", "A) ship", "En el puerto hay un barco; ship es la de vocal corta."),
    ],
    [
        ("Clasifica según el comienzo: tree, dress, train, drain. Escribe cuáles empiezan con tr y cuáles con dr.", "tr: tree, train. dr: dress, drain", "Se miran las dos primeras letras de cada palabra."),
        ("Una persona dice «yet» y otra dice «jet». ¿Qué palabra significa «todavía»? A) yet B) jet", "A) yet", "Yet empieza con /j/ y significa todavía; jet es un avión."),
    ],
    [("Un adulto lee: «We are on vacation at the train station.» ¿Qué dos palabras terminan con el sonido «shən»?", "Vacation y station", "Las dos terminan en -tion.")],
    [
        ("¿Cómo suena la vocal de feet?", "Larga (/iː/)", "Se escribe ee y dura más."),
        ("¿Qué sonido tiene la terminación -tion?", "«shən»", "Se dice como en vacation."),
        ("¿Con qué sonido empieza year?", "/j/, como la y de «yo»", "No es jet."),
    ],
    task("Con un adulto, lee en voz alta estas ocho palabras y graba o anota si dijiste bien cada sonido: sheep, ship, tree, dress, year, yes, vacation, station. En tu hoja escribe: cuáles tienen vocal larga, cuáles empiezan con tr o dr, cuáles con /j/ y cuáles terminan en -tion.", "Vocal larga: sheep. Vocal corta: ship. tr: tree. dr: dress. /j/: year, yes. -tion: vacation, station.", ["clasifica las ocho palabras sin dejar ninguna fuera", "pronuncia -tion como shən", "diferencia vocal larga y corta con un adulto"], ["hoja con la clasificación", "grabación o nota del adulto"], ["decir year como jir", "pronunciar tion con t"], "Valida los sonidos bien pronunciados y repite con la persona solo los pares que se confundieron."),
    "Lee en voz alta cinco veces la lista bean, bin, cheap, chip, heel, hill con un adulto y marca las que sonaron igual.",
    "Escribe en español una frase breve para recordar cómo suena -tion y léela a una persona.",
)

# ---------------------------------------------------------------- clase 5: respuesta independiente
DIALOG = "«Teacher: Good morning, everyone. Today we will talk about our trip to the museum. Student 1: When do we go? Teacher: On Friday, at eight. We will take the bus from the school. Student 2: What should we bring? Teacher: Bring a notebook and a pencil, and wear comfortable shoes. Student 3: Is it free? Teacher: The tickets cost two thousand pesos, but the school pays for half. Student 1: So we pay one thousand? Teacher: Exactly.» (museum = museo, trip = salida, should = deberíamos, comfortable = cómodos, tickets = entradas, pays for half = paga la mitad)"
TALK2 = "«Hello. I want to tell you about my grandfather. He was a fisherman in Chiloé for forty years. He woke up at four every morning. Although the work was hard, he loved the sea. Later, he taught me to repair nets. Now I want to be a fisherman too.» (fisherman = pescador, Chiloé = isla del sur de Chile, hard = duro, sea = mar, taught = enseñó, repair nets = reparar redes)"

lesson(
    OA2, 5, MAT,
    "Aprenderé a responder por mi cuenta preguntas sobre un diálogo y una charla, combinando propósito, detalles, conectores y sonidos. Sirve para comprobar que ya entiendo textos orales de varios temas sin ayuda.",
    ["Sé buscar tema, propósito y detalles.", "Sé reconocer los conectores although, so that, later, both."],
    [
        "Responder de forma independiente significa tomar tú las decisiones de escucha: leer las preguntas antes, escuchar buscando la pista y comprobar con una segunda lectura. Un diálogo con varios hablantes (teacher, student 1, student 2) entrega datos repartidos: la hora la dice la profesora, pero la pregunta la hace un estudiante. Marca quién dice qué.",
        "En una charla personal, el propósito suele ser compartir una experiencia y las ideas relevantes se apoyan en detalles: cuántos años, qué hacía, qué aprendió. Los conectores guían el orden: later introduce algo que ocurrió después y although muestra que, a pesar de lo difícil, el abuelo amaba el mar. Los cálculos simples también forman parte de la comprensión: si las entradas cuestan dos mil pesos y la escuela paga la mitad, cada estudiante paga mil.",
        "Antes de entregar tu respuesta, revísala con tres preguntas: ¿responde justo lo que pregunta?, ¿la respalda una pista del guion? y ¿los números coinciden con lo que dijeron? Si una respuesta no pasa el control, vuelve a escuchar solo esa parte.",
    ],
    [("trip", "salida, viaje corto"), ("should", "deber, convenir"), ("half", "la mitad"), ("fisherman", "pescador"), ("later", "más tarde, después"), ("clue", "pista que respalda una respuesta")],
    [
        ("Dato de un diálogo", ADULT + DIALOG + " ¿Cuánto paga cada estudiante por la entrada?", ["La entrada cuesta dos mil pesos.", "La escuela paga la mitad.", "La mitad de 2.000 es 1.000."], "1.000 pesos"),
        ("Idea de una charla", ADULT + TALK2 + " ¿Por qué el nieto quiere ser pescador?", ["Busco una razón en el guion.", "El abuelo amaba el mar y le enseñó a reparar redes.", "Ahora el nieto quiere ser pescador también."], "Porque admira a su abuelo y aprendió de él"),
    ],
    [
        ("No leer las preguntas antes de escuchar.", "Se escucha sin saber qué buscar.", "Lee las preguntas y marca la palabra que pide cada una."),
        ("Responder sin comprobar los números.", "Se confía en la memoria.", "Haz el cálculo con los datos del guion y compara."),
    ],
    [
        (ADULT + DIALOG + " ¿A qué hora salen? A) a las ocho B) a las nueve", "A) a las ocho", "La profesora dice On Friday, at eight."),
        (ADULT + TALK2 + " ¿Dónde trabajaba el abuelo? A) en Chiloé B) en Valdivia", "A) en Chiloé", "El guion dice a fisherman in Chiloé."),
        (ADULT + DIALOG + " ¿Qué deben llevar los estudiantes?", "Un cuaderno y un lápiz", "La profesora dice Bring a notebook and a pencil."),
    ],
    [
        (ADULT + TALK2 + " ¿Cuántos años fue pescador el abuelo?", "40", "Dice for forty years."),
        (ADULT + DIALOG + " ¿Cómo viajan al museo? A) en bus desde el colegio B) a pie", "A) en bus desde el colegio", "El guion dice We will take the bus from the school."),
        arith(ADULT + DIALOG + " Un curso de 30 estudiantes paga mil pesos cada uno. ¿Cuántos pesos reúnen en total?", "30*1000", "Se multiplican los estudiantes por lo que paga cada uno."),
    ],
    [
        (ADULT + DIALOG + " ¿Qué día es la salida?", "El viernes", "La profesora dice On Friday."),
        (ADULT + TALK2 + " ¿A qué hora se levantaba el abuelo?", "A las cuatro", "El guion dice He woke up at four every morning."),
        (ADULT + DIALOG + " ¿Qué deben usar en los pies? A) zapatos cómodos B) botas de goma", "A) zapatos cómodos", "La profesora dice wear comfortable shoes."),
    ],
    [
        (ADULT + TALK2 + " ¿Qué conector muestra que, aunque el trabajo era duro, el abuelo amaba el mar? A) although B) later", "A) although", "Although introduce el contraste entre lo duro y lo querido."),
        (ADULT + DIALOG + " Un estudiante dice que la entrada completa cuesta mil pesos. ¿Qué corrige el guion? A) cuesta dos mil, pero la escuela paga la mitad B) cuesta cinco mil", "A) cuesta dos mil, pero la escuela paga la mitad", "La profesora explica el precio completo y el aporte del colegio."),
    ],
    [
        (ADULT + TALK2 + " ¿Qué palabra marca lo que ocurrió después, cuando el abuelo enseñó a reparar redes? A) Later B) Although", "A) Later", "Later ordena la acción en el tiempo."),
        ("Una persona lee estas palabras: «ship, sheep, vacation». ¿Cuál tiene la vocal corta y cuál termina en shən? A) ship y vacation B) sheep y ship", "A) ship y vacation", "Ship tiene vocal corta y vacation termina en -tion."),
    ],
    [(ADULT + "«Hi, this is Fernanda. I'm calling about the guitar class. Although it starts at five, I can arrive at five fifteen. Both my cousin and I want to join. Can you save two places?» (guitar class = clase de guitarra, arrive = llegar, join = unirse, save = guardar, places = cupos). ¿Cuántos cupos pide guardar?", "2", "Fernanda y su prima quieren unirse: two places.")],
    [
        ("¿Qué haces antes de escuchar para saber qué buscar?", "Leer las preguntas", "Te dice qué dato buscar."),
        ("¿Qué indica although en una charla?", "Que hay un contraste", "Une dos ideas que se oponen."),
        ("¿Cómo puedes comprobar un cálculo de un diálogo?", "Con los datos del guion", "Los números del texto sirven de prueba."),
    ],
    task("Un adulto lee dos veces este texto original: «Hi. My name is Valentina and I want to tell you about my neighbor. Don Lucho repairs bicycles for free every Sunday. Although he is seventy, he works for four hours. Both children and adults visit him. Later, he teaches them to fix a flat tire so that they can help themselves.» (neighbor = vecino, repairs = repara, for free = gratis, flat tire = neumático pinchado, help themselves = ayudarse solos). En tu hoja escribe: el propósito, tres datos exactos, el conector de contraste y el conector de propósito.", "Propósito: compartir y admirar lo que hace un vecino. Datos: arregla bicicletas gratis los domingos; tiene setenta años; trabaja cuatro horas. Contraste: although. Propósito: so that.", ["indica un propósito coherente", "da tres datos exactos", "identifica although y so that con su función"], ["hoja con cinco respuestas", "nota del adulto"], ["confundir although con so that", "dar un dato inventado"], "Reconoce los datos acertados y repasa con la persona las dos palabras señal."),
    "Pide a un adulto que lea otra vez el diálogo del museo y calcula cuánto paga un curso de 20 estudiantes.",
    "Escribe en español tres preguntas que podrías hacerle a Don Lucho sobre su trabajo.",
)
