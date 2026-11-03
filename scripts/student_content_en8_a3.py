"""Cuaderno del estudiante, 8.º básico Inglés (propuesta), EN08 OA 03 (estrategias para escuchar y aclarar).

Las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan pista en español. Las clases del plan tienen títulos genéricos; aquí cada clase trabaja una estrategia que nombra el OA.
"""
from __future__ import annotations

from student_content_en8_a import ADULT, lesson, task
from student_lessons import arith

OA3 = "EN08 OA 03"

# ---------------------------------------------------------------- clase 1: hacer predicciones
MARKET = "«Saturday is market day in my town. My mother and I walk to the fair at nine o'clock. We buy tomatoes, lettuce and a kilo of apples. The seller always gives me an extra apple. Then we carry the bags home.» (market = feria, lettuce = lechuga, seller = vendedor, extra = una más, carry = llevar)"
DRILL = "«Attention, please. This is an earthquake drill. When the alarm sounds, stay calm. Get under your desk, cover your head and hold on. When it stops, walk to the yard with your teacher. Do not run.» (earthquake drill = simulacro de sismo, alarm = alarma, stay calm = mantén la calma, cover = cubrir, hold on = sostenerte, walk = caminar)"
BAKERY = "«Welcome to the cooking class. Today we will make bread rolls. First, mix flour, water and a little salt. Then knead the dough for ten minutes. Finally, an adult will put the rolls in the oven.» (cooking class = clase de cocina, flour = harina, salt = sal, knead = amasar, dough = masa, oven = horno)"

lesson(
    OA3, 1,
    "Las descripciones de título e imagen y los guiones escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a hacer predicciones antes de escuchar, usando el título, una imagen y lo que ya sé. Sirve para entender mejor porque sé qué palabras esperar.",
    ["Sé que market, drill y class son tipos de situaciones.", "Conozco vocabulario de comida y del colegio."],
    [
        "Una predicción (prediction) es una idea sobre lo que vas a oír antes de escuchar. Se apoya en pistas: el título (title), una imagen (picture), el lugar y lo que ya sabes del tema. Si el título es «Market day» y la imagen muestra personas con canastos de frutas, puedes predecir palabras como apples, tomatoes, price y buy.",
        "Predecir no es adivinar: es preparar la mente. Escribe dos o tres palabras que esperas oír. Mientras escuchas, comprueba si aparecieron. Si no aparecieron, cambia tu predicción: eso también es aprender. Un error común es predecir con una sola pista y no mirar las demás.",
        "Los conocimientos previos (prior knowledge) también ayudan. Si ya has participado en un simulacro de sismo, esperas oír palabras como alarm, calm y yard. Una predicción útil responde a tres preguntas: ¿de qué trata?, ¿quién habla? y ¿qué palabras oiré? Con ellas, el texto es más fácil de seguir.",
    ],
    [("prediction", "predicción: lo que creo que oiré"), ("title", "título"), ("picture", "imagen"), ("prior knowledge", "conocimiento previo"), ("confirm", "confirmar: comprobar que algo es cierto"), ("clue", "pista")],
    [
        ("Predecir con un título y una imagen", "Título: «Market day». Imagen: personas con canastos de frutas y verduras. ¿Qué palabra esperas oír? Elige: apples, whistle o homework.", ["Miro el título y la imagen: son sobre una feria.", "Pienso en lo que se vende en una feria: frutas y verduras.", "La palabra que encaja es apples."], "apples"),
        ("Confirmar una predicción", ADULT + MARKET + " Predijiste que oirías apples. ¿Se cumplió? ¿Cuántos kilos?", ["Escucho el guion y busco apples.", "Aparece a kilo of apples.", "La predicción se cumple y el dato es un kilo."], "Sí, se cumplió: un kilo de manzanas"),
    ],
    [
        ("Predecir con una sola pista y no mirar el resto.", "Se ve solo la imagen o solo el título.", "Usa las tres fuentes: título, imagen y lo que sabes del tema."),
        ("Aferrarse a la predicción cuando el texto dice otra cosa.", "Se cree que la predicción debe ser correcta.", "Cámbiala si el texto no la confirma: corregir es parte de la estrategia."),
    ],
    [
        ("Título: «An earthquake drill at school». ¿Qué palabra predices oír? a) alarm b) birthday", "a) alarm", "Un simulacro de sismo se relaciona con una alarma."),
        ("Título: «Cooking class». ¿Qué palabra predices oír? a) flour b) volleyball", "a) flour", "En una clase de cocina se usa harina."),
        (ADULT + DRILL + " ¿Qué hay que hacer cuando suena la alarma? a) mantener la calma b) correr al patio", "a) mantener la calma", "El guion dice stay calm; no se debe correr."),
    ],
    [
        (ADULT + BAKERY + " Predijiste oír «flour». ¿Qué ingrediente seco aparece primero en el guion?", "Harina (flour)", "Dice mix flour, water and a little salt."),
        (ADULT + MARKET + " ¿A qué hora van a la feria? a) a las nueve b) a las diez", "a) a las nueve", "El guion dice at nine o'clock."),
        ("Tienes la imagen de una persona con casco, bicicleta y semáforo. ¿Cuál es la mejor predicción? a) hablarán de seguridad en la calle b) hablarán de una receta", "a) hablarán de seguridad en la calle", "Casco, bicicleta y semáforo son pistas de tránsito."),
    ],
    [
        (ADULT + DRILL + " Predijiste oír running. ¿Qué dice el texto sobre correr? a) que no se debe correr b) que se debe correr", "a) que no se debe correr", "Dice Do not run."),
        (ADULT + BAKERY + " ¿Cuántos minutos se amasa la masa?", "10", "El guion dice ten minutes."),
        (ADULT + MARKET + " ¿Qué les da siempre el vendedor? a) una manzana extra b) una lechuga extra", "a) una manzana extra", "El guion dice The seller always gives me an extra apple."),
    ],
    [
        ("Un compañero predijo sobre «Market day» que oirá la palabra soccer. En el guion la palabra no aparece. ¿Qué debe hacer? a) corregir su predicción con lo que oye b) ignorar el guion", "a) corregir su predicción con lo que oye", "Una predicción puede cambiar cuando aparece nueva información."),
        (ADULT + DRILL + " ¿Por qué es útil predecir antes de este aviso? a) porque reconoces alarm y calm más rápido b) porque ya no necesitas escuchar", "a) porque reconoces alarm y calm más rápido", "La predicción prepara el vocabulario, pero igual hay que escuchar."),
    ],
    [
        ("Predice. El título es «Birthday party» y la imagen muestra globos, pastel y velas. ¿Qué palabra predices oír? Elige: cake / hammer.", "cake", "El pastel se relaciona con un cumpleaños."),
        ("Una persona predice que en «Cooking class» se hablará de salir al patio. ¿Por qué es una mala predicción?", "Porque cooking class se relaciona con cocinar y no con salir al patio", "La predicción debe apoyarse en el título."),
    ],
    [(ADULT + "«Good morning, listeners. Today the weather will be sunny and warm. The highest temperature will be twenty-eight degrees. Remember to wear sunscreen and drink water.» (listeners = oyentes, warm = cálido, highest = más alta, sunscreen = bloqueador). Si el título es «Weather report», ¿qué predicción se cumple? a) que se hablará del clima b) que se hablará de una receta", "a) que se hablará del clima", "El guion habla de sunny, warm y temperature.")],
    [
        ("En Inglés: ¿Qué es una predicción?", "Una idea de lo que voy a oír", "Se hace antes de escuchar con pistas."),
        ("¿Qué tres fuentes ayudan a predecir?", "Título, imagen y conocimientos previos", "Dan pistas sobre el tema y las palabras."),
        ("¿Qué haces si el texto no confirma tu predicción?", "La cambio", "Se corrige con lo que se oye."),
    ],
    task("Observa este título e imagen: «A day at the beach». Imagen: una familia con toallas, sombrilla y pelota junto al mar. En tu hoja escribe tres palabras que esperas oír y explica en español una pista que usaste. Luego pide a un adulto que lea esta frase: «Today we are at the beach. The sea is calm, and the children are playing with a ball under the umbrella.» (sea = mar, calm = tranquilo, umbrella = sombrilla). Marca cuál de tus palabras apareció.", "Palabras: sea, ball, umbrella. Pista: la imagen muestra mar, pelota y sombrilla. Aparecieron sea, ball y umbrella.", ["escribe tres palabras coherentes con título e imagen", "explica una pista", "marca las que se confirmaron"], ["hoja con predicciones", "hoja con las palabras confirmadas"], ["predecir palabras sin relación con el tema", "no marcar lo que se confirmó"], "Reconoce las predicciones útiles y revisa con la persona qué pista del título o la imagen no se usó."),
    "Pide a un adulto que lea de nuevo el simulacro de sismo y subraya las palabras que habías predicho.",
    "Escribe en español qué palabras esperarías oír en un reportaje sobre un partido de fútbol escolar y por qué.",
)

# ---------------------------------------------------------------- clase 2: escuchar con un propósito y usar conocimientos previos
FAIR = "«Radio Escuela here. The science fair is next Thursday. Students will show twenty-four projects about energy, water and space. Parents can visit from three to five. Entrance is free.» (science fair = feria científica, projects = proyectos, energy = energía, space = espacio, parents = apoderados, entrance = entrada, free = gratis)"
SLEEP = "«Teenagers need between eight and ten hours of sleep every night. Sleeping well helps memory and mood. To sleep better, turn off your phone one hour before bed, and keep your room quiet and dark.» (teenagers = adolescentes, sleep = dormir, memory = memoria, mood = ánimo, turn off = apagar, quiet = silenciosa, dark = oscura)"
POOL = "«Rules for the school pool. Walk, don't run. Shower before you enter. Only enter with a teacher. Wear a swimming cap. Leave your bag in the locker.» (pool = piscina, shower = ducharse, swimming cap = gorro de baño, locker = casillero)"

lesson(
    OA3, 2,
    "Los guiones y las preguntas previas escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a escuchar con un propósito, es decir, leer la pregunta antes de oír el texto, y a usar lo que ya sé para entender. Sirve para buscar el dato correcto sin perderme en el resto.",
    ["Sé hacer predicciones con el título.", "Conozco números hasta cien y horas en inglés."],
    [
        "Escuchar con un propósito (purpose) significa decidir qué buscas antes de oír. Si la pregunta es «¿cuántos proyectos?», solo necesitas un número. Si es «¿a qué hora?», solo necesitas una hora. Así tu atención se concentra en un dato y no en todo el texto. Lee las preguntas, marca la palabra clave de cada una y luego escucha.",
        "Los conocimientos previos (prior knowledge) son lo que ya sabes. Si sabes que una feria científica muestra proyectos, o que una piscina escolar tiene normas, entiendes más rápido. También sirven para detectar errores: si oyes «only enter with a teacher», sabes que es una regla de seguridad porque has visto normas parecidas.",
        "Combina las dos ideas. Antes de escuchar, pregúntate qué sabes del tema y qué dato buscas. Durante la escucha, anota solo ese dato. Después, comprueba tu respuesta con otra escucha. Si la pregunta pide una opinión o una razón, escucha palabras como because, so o good.",
    ],
    [("purpose", "propósito: lo que busco al escuchar"), ("prior knowledge", "conocimientos previos: lo que ya sé"), ("keyword", "palabra clave de la pregunta"), ("rule", "regla o norma"), ("advice", "consejo"), ("check", "comprobar")],
    [
        ("Escuchar con un propósito", "Pregunta previa: ¿cuántos proyectos habrá? " + ADULT + FAIR + " Responde.", ["La palabra clave es cuántos, o sea, un número.", "Escucho y busco un número: twenty-four projects.", "Veinticuatro se escribe 24."], "24 proyectos"),
        ("Usar conocimientos previos", ADULT + POOL + " Sabes que en una piscina hay normas de seguridad. ¿Por qué crees que dicen Walk, don't run?", ["Pienso en lo que sé: el suelo mojado resbala.", "Walk, don't run pide caminar para evitar caídas.", "La regla se relaciona con la seguridad."], "Porque el suelo mojado resbala y se evitan caídas"),
    ],
    [
        ("Escuchar todo el texto sin saber qué buscar.", "No se lee la pregunta antes.", "Lee la pregunta primero y marca la palabra clave."),
        ("Responder con lo que se sabe del tema, sin comprobar con el texto.", "Se confunde conocimiento previo con la respuesta.", "Los conocimientos ayudan a entender, pero la respuesta sale del texto."),
    ],
    [
        ("Pregunta previa: ¿a qué hora pueden visitar los apoderados? " + ADULT + FAIR + " Elige: a) de tres a cinco b) de dos a cuatro", "a) de tres a cinco", "El guion dice from three to five."),
        ("Pregunta previa: ¿cuánto cuesta la entrada? " + ADULT + FAIR + " Responde.", "Es gratis", "El guion dice Entrance is free."),
        ("Pregunta previa: ¿cuántas horas de sueño necesitan los adolescentes? " + ADULT + SLEEP + " Elige: a) de ocho a diez b) de cuatro a seis", "a) de ocho a diez", "El guion dice between eight and ten hours."),
    ],
    [
        ("Pregunta previa: ¿cuándo se debe apagar el teléfono? " + ADULT + SLEEP + " Responde.", "Una hora antes de dormir", "Dice turn off your phone one hour before bed."),
        ("Pregunta previa: ¿qué debe llevar la persona en la cabeza? " + ADULT + POOL + " Elige: a) un gorro de baño b) un casco", "a) un gorro de baño", "El guion dice Wear a swimming cap."),
        ("Pregunta previa: ¿con quién se puede entrar a la piscina? " + ADULT + POOL + " Responde.", "Con un profesor o profesora", "Dice Only enter with a teacher."),
    ],
    [
        ("Pregunta previa: ¿cómo se llama la radio que da el aviso? " + ADULT + FAIR + " Responde.", "Radio Escuela", "El guion empieza con Radio Escuela here."),
        ("Pregunta previa: ¿qué se debe hacer antes de entrar a la piscina? " + ADULT + POOL + " Elige: a) ducharse b) comer algo", "a) ducharse", "El guion dice Shower before you enter."),
        ("Pregunta previa: ¿qué pide la primera regla de la piscina? " + ADULT + POOL + " Elige: a) caminar b) correr", "a) caminar", "La regla dice Walk, don't run."),
    ],
    [
        (ADULT + FAIR + " ¿Sobre qué temas son los proyectos? Nombra los tres temas.", "Energía, agua y espacio", "El guion dice about energy, water and space."),
        (ADULT + SLEEP + " ¿Qué ayuda a dormir mejor, según el texto? a) mantener el cuarto silencioso y oscuro b) dejar la música fuerte", "a) mantener el cuarto silencioso y oscuro", "El guion dice keep your room quiet and dark."),
    ],
    [
        (ADULT + POOL + " ¿Dónde se deja la mochila? a) en el casillero b) en el borde de la piscina", "a) en el casillero", "El guion dice Leave your bag in the locker."),
        (ADULT + SLEEP + " ¿Qué dos cosas mejora dormir bien? Escribe las dos.", "La memoria y el ánimo", "El guion dice helps memory and mood."),
    ],
    [(ADULT + "«Welcome, visitors. The museum opens at ten and closes at five. Groups need a reservation. Photos without flash are allowed.» (visitors = visitantes, opens = abre, closes = cierra, reservation = reserva, flash = flash). Pregunta previa: ¿cuántas horas está abierto el museo? Responde con un número.", "7", "De 10 a 17 horas son siete horas.")],
    [
        ("¿Qué haces antes de escuchar si quieres un dato exacto?", "Leo la pregunta y marco la palabra clave", "Así sé qué buscar."),
        ("¿Qué son los conocimientos previos?", "Lo que ya sé del tema", "Ayudan a entender el texto."),
        ("Si la pregunta es «¿a qué hora?», ¿qué buscas?", "Una hora", "La palabra clave pide un tiempo."),
    ],
    task("Lee estas dos preguntas antes de escuchar: 1) ¿Qué día es la salida? 2) ¿Qué se debe llevar? Un adulto lee dos veces: «Good morning. The field trip is on Wednesday. Please bring a jacket, a water bottle and a notebook. The bus leaves at eight thirty.» (field trip = salida pedagógica, jacket = chaqueta, water bottle = botella de agua, notebook = cuaderno). Escribe las respuestas y tacha una palabra del texto que no necesitaste para responder.", "1) Miércoles. 2) Una chaqueta, una botella de agua y un cuaderno. Palabra no necesitada: bus o eight thirty.", ["responde con datos exactos", "usa las preguntas para filtrar", "indica una palabra que no usó"], ["hoja con respuestas", "nota del adulto"], ["anotar la hora como respuesta a la pregunta 1", "olvidar un objeto de la lista"], "Reconoce los datos correctos y vuelve a leer con la persona las palabras clave de cada pregunta para filtrar mejor."),
    "Escribe dos preguntas antes de que un adulto lea el aviso de la piscina y marca las palabras clave.",
    "Escribe en español qué sabes del tema «feria científica» y qué palabras en inglés esperarías oír.",
)

# ---------------------------------------------------------------- clase 3: palabras clave, apoyos visuales, gestos y entonación
GESTURE = "«(The teacher points to the board.) Please write your name here, at the top. (She points to the shelf.) And put your book over there.» (points to = señala, board = pizarra, shelf = estante, over there = allá)"
STRESS = "«No, no. I said the BLUE bag, not the red one. The blue bag is on the chair. The red bag is on the floor.» (La voz sube y se vuelve más fuerte en BLUE.) (bag = bolso, chair = silla, floor = suelo)"
TONE = "«(Voz sube al final.) You are coming to the party? (Voz baja al final.) You are coming to the party. (Voz muy alegre.) You are coming to the party!» (party = fiesta, coming = viniendo)"

lesson(
    OA3, 3,
    "Los guiones con indicaciones de gestos y entonación escritos en cada ejercicio, que lee un adulto en voz alta; una hoja y lápiz.",
    "Aprenderé a centrarme en palabras y expresiones clave y a usar apoyos como imágenes, gestos y entonación del hablante. Sirve para entender aunque no conozca todas las palabras.",
    ["Sé preguntar y responder con there is y it is.", "Conozco adjetivos de color y objetos del colegio."],
    [
        "Las palabras clave (key words) son las que llevan el significado: sustantivos, verbos principales, números y adjetivos importantes. Las expresiones clave son frases fijas, como «over there» (allá), «at the top» (arriba), «I said…» (yo dije…). Cuando las reconoces, entiendes la idea aunque no conozcas todas las demás palabras.",
        "Los apoyos (supports) ayudan a entender. Una imagen muestra el lugar o el objeto. Los gestos (gestures) del hablante, como señalar con la mano, indican dónde está algo. La entonación (intonation) es cómo sube y baja la voz: si sube al final, suele ser una pregunta; si baja, una afirmación; si es muy alegre, una emoción. La palabra con más fuerza (stress) suele ser la más importante.",
        "Para usar estos apoyos, mira al hablante, repara en su mano y su cara, y escucha cómo cambia su voz. Si dice «I said the BLUE bag, not the red one», la fuerza en BLUE te indica que el color es el dato clave. Anota la palabra marcada y descarta la otra.",
    ],
    [("key word", "palabra clave"), ("gesture", "gesto: movimiento de manos o cara"), ("intonation", "entonación: subida y bajada de la voz"), ("stress", "énfasis: fuerza en una palabra"), ("over there", "allá"), ("point", "señalar")],
    [
        ("Usar un gesto como apoyo", ADULT + GESTURE + " ¿Dónde debe poner el libro el estudiante?", ["El gesto: la profesora señala el estante.", "La frase dice over there, o sea, allá.", "Juntos indican el estante."], "En el estante"),
        ("Usar la entonación", ADULT + STRESS + " ¿Qué bolso quiere la persona?", ["La voz sube en BLUE.", "La persona dice I said the BLUE bag, not the red one.", "El bolso importante es el azul."], "El bolso azul"),
    ],
    [
        ("Ignorar el gesto y quedarse solo con las palabras.", "Se escucha pero no se observa.", "Mira hacia dónde señala el hablante y anótalo."),
        ("Pensar que la subida de voz siempre es enojo.", "Se confunde entonación con emoción.", "Si la voz sube al final, suele ser una pregunta; si sube con fuerza en una palabra, esa es la palabra importante."),
    ],
    [
        (ADULT + GESTURE + " ¿Dónde debe escribir el estudiante su nombre? a) arriba, en la pizarra b) al final del cuaderno", "a) arriba, en la pizarra", "El guion dice write your name here, at the top, y señala la pizarra."),
        (ADULT + STRESS + " ¿Dónde está el bolso azul? a) en la silla b) en el suelo", "a) en la silla", "El guion dice The blue bag is on the chair."),
        (ADULT + TONE + " ¿Cuál es la frase en que la voz sube al final? a) You are coming to the party? b) You are coming to the party.", "a) You are coming to the party?", "La voz que sube al final marca una pregunta."),
    ],
    [
        (ADULT + TONE + " ¿Cuál de las tres frases muestra más emoción? a) la tercera, con voz alegre b) la segunda, con voz baja", "a) la tercera, con voz alegre", "Se dice con voz muy alegre y signo de exclamación."),
        (ADULT + GESTURE + " ¿Qué palabra del guion indica un lugar alejado del hablante? a) over there b) at the top", "a) over there", "Over there significa allá."),
        (ADULT + STRESS + " ¿Qué color se dice con más fuerza? a) azul b) rojo", "a) azul", "La voz sube en BLUE."),
    ],
    [
        (ADULT + GESTURE + " ¿Qué señala la profesora cuando dice «And put your book over there»? a) un estante b) la puerta", "a) un estante", "El guion indica que señala el estante."),
        (ADULT + STRESS + " ¿Dónde está el bolso rojo?", "En el suelo", "El guion dice The red bag is on the floor."),
        ("¿Qué apoyo te muestra que alguien hace una pregunta aunque no entiendas todas las palabras? a) la entonación que sube al final b) el color de su ropa", "a) la entonación que sube al final", "La voz que sube al final marca la pregunta."),
    ],
    [
        ("Una persona señala la puerta y dice «The exit is over there». ¿Qué apoyo te muestra dónde está la salida? a) el gesto de señalar b) el título", "a) el gesto de señalar", "El gesto se combina con over there."),
        (ADULT + STRESS + " ¿Por qué es importante la fuerza en BLUE? a) porque marca la diferencia con el bolso rojo b) porque es una pregunta", "a) porque marca la diferencia con el bolso rojo", "La palabra con más fuerza contrasta con la otra."),
    ],
    [
        ("Une cada apoyo con lo que ayuda a entender. 1) imagen 2) gesto 3) entonación. Ayudas: a) cómo suena una pregunta b) hacia dónde señala quien habla c) cómo es un lugar o un objeto", "1-c, 2-b, 3-a", "La imagen muestra cómo es algo, el gesto señala y la entonación marca la pregunta."),
        ("Una profesora dice «Put the notebooks over there» y señala una caja. Un estudiante deja los cuadernos en la mesa. ¿Qué apoyo no usó? a) el gesto de la profesora b) la palabra notebooks", "a) el gesto de la profesora", "El gesto indicaba la caja."),
    ],
    [(ADULT + "«(The guide points to a map.) We are here, in the plaza. (He points to the right.) The market is over there. Is that clear?» (guide = guía, map = mapa, plaza = plaza, right = derecha, clear = claro). ¿En qué dirección está el mercado? a) a la derecha b) a la izquierda", "a) a la derecha", "El guía señala a la derecha y dice over there.")],
    [
        ("¿Qué es la entonación?", "Cómo sube y baja la voz", "Ayuda a distinguir preguntas y emociones."),
        ("¿Qué hace un gesto al hablar?", "Ayuda a entender dónde o qué es algo", "Complementa las palabras."),
        ("¿Qué palabra suele tener más fuerza en una frase?", "La más importante", "Es la palabra clave."),
    ],
    task("Con una persona de tu casa: ella lee esta frase cambiando la fuerza de la voz, «I want the GREEN pencil, not the yellow one», y señala un lápiz verde. Después la lee con fuerza en PENCIL: «I want the green PENCIL, not the pen». (pencil = lápiz, pen = lapicera, want = quiero). En tu hoja escribe qué palabra tenía más fuerza cada vez y qué dato cambió.", "Primera vez: GREEN, el dato es el color. Segunda vez: PENCIL, el dato es el objeto (lápiz, no lapicera).", ["identifica la palabra con más fuerza en cada lectura", "explica qué dato cambió", "usa el gesto como apoyo"], ["hoja con dos palabras y explicación", "nota de la persona que leyó"], ["decir que la frase tiene el mismo énfasis", "confundir pencil con pen"], "Reconoce la palabra con énfasis y repite la frase con la persona exagerando la fuerza hasta distinguir el cambio."),
    "Pide a un adulto que lea otra vez los guiones con gestos y marca con una flecha hacia dónde señala.",
    "Escribe en español cómo usas tu cara y tus manos para que te entiendan cuando preguntas dónde está algo.",
)

# ---------------------------------------------------------------- clase 4: preguntar para aclarar (brecha de información)
TIME = "A: «The meeting is at four fifteen, in room twelve.» B: «Sorry, did you say four fifty?» A: «No, four fifteen, in room twelve.» (meeting = reunión, room = sala)"
PRICE = "A: «The ticket costs thirty thousand pesos... I mean, thirteen thousand pesos.» B: «Could you repeat that, please? Thirteen thousand?» A: «Yes, thirteen thousand.» (ticket = entrada, costs = cuesta, I mean = quiero decir)"
HOMEWORK = "«For homework, read pages twenty to twenty-five. Then write five sentences. The test is next Tuesday.» (homework = tarea, pages = páginas, sentences = oraciones, test = prueba)"

lesson(
    OA3, 4,
    "Los diálogos y las frases de dos personas escritos en cada ejercicio; una hoja y lápiz.",
    "Aprenderé a preguntar para aclarar y confirmar información en una conversación, con frases como Could you repeat that? y Did you say…? Sirve para no quedarme con dudas y comprobar un dato.",
    ["Sé preguntar con what, where y when.", "Conozco números hasta cien y las horas."],
    [
        "Cuando no entiendes algo en una conversación, puedes preguntar para aclarar (to clarify). Algunas frases útiles son: «Could you repeat that, please?» (¿puedes repetir eso?), «Sorry, I didn't catch that» (perdón, no lo capté), «Do you mean…?» (¿quieres decir…?), «Did you say fifteen or fifty?» (¿dijiste quince o cincuenta?) y «What does … mean?» (¿qué significa…?). Son frases muy comunes y nunca son una falta de educación.",
        "Para corroborar (to confirm) un dato, repítelo con voz de pregunta: «Four fifteen?». Si es correcto, la otra persona responde «Yes, that's right». Si no lo es, te corrige. Confirmar es útil con números, horas, precios y nombres, porque son datos fáciles de confundir.",
        "En una actividad de brecha de información, cada persona tiene una parte del dato y debe pedir la que le falta con preguntas claras. Una pregunta corta basta: «What time is the test?», «How many pages?», «Which pages do I read?» (¿qué páginas leo?). Usa un tono amable y espera la respuesta antes de seguir.",
    ],
    [("clarify", "aclarar: hacer más claro algo"), ("confirm", "corroborar, confirmar"), ("Could you repeat that?", "¿Puedes repetir eso?"), ("Do you mean…?", "¿Quieres decir…?"), ("I didn't catch that", "no lo capté"), ("That's right", "es correcto")],
    [
        ("Elegir la frase para aclarar", "Un compañero dice algo muy rápido y no lo entendiste. ¿Qué frase usas? Elige: Could you repeat that, please? / Thank you very much.", ["No entendí lo que dijo.", "Necesito que lo diga otra vez.", "La frase que pide repetir es Could you repeat that, please?"], "Could you repeat that, please?"),
        ("Corroborar un dato", ADULT + TIME + " ¿A qué hora es la reunión y en qué sala?", ["A dice four fifteen, in room twelve.", "B duda y pregunta si es four fifty.", "A corrige y confirma four fifteen."], "A las 4:15, en la sala 12"),
    ],
    [
        ("Quedarse callado cuando no se entiende.", "Se cree que preguntar es mostrar debilidad.", "Usa una frase corta de aclaración y confirma el dato."),
        ("Preguntar «What?» de manera brusca.", "No se conoce una forma educada.", "Di Sorry, could you repeat that, please?"),
    ],
    [
        (ADULT + PRICE + " ¿Cuánto cuesta la entrada? a) trece mil pesos b) treinta mil pesos", "a) trece mil pesos", "A corrige: I mean, thirteen thousand pesos."),
        ("Quieres saber si alguien dijo quince o cincuenta. ¿Qué pregunta usas? a) Did you say fifteen or fifty? b) Can you open the window?", "a) Did you say fifteen or fifty?", "Esa pregunta confirma exactamente el dato dudoso."),
        (ADULT + HOMEWORK + " ¿Cuántas oraciones hay que escribir?", "5", "El guion dice write five sentences."),
    ],
    [
        (ADULT + HOMEWORK + " Alguien no entendió las páginas. ¿Qué pregunta ayuda? a) Which pages do I read? b) Where is the library?", "a) Which pages do I read?", "Pide justo el dato que falta."),
        (ADULT + HOMEWORK + " ¿Para cuándo es la prueba? a) para el próximo martes b) para mañana", "a) para el próximo martes", "El guion dice The test is next Tuesday."),
        (ADULT + TIME + " ¿Qué palabra usa B para confirmar la hora? a) Sorry, did you say… b) Good morning", "a) Sorry, did you say…", "Con esa pregunta B corrobora el dato."),
    ],
    [
        (ADULT + PRICE + " ¿Qué cifra dijo A primero, antes de corregirse? a) thirty thousand pesos b) thirteen thousand pesos", "a) thirty thousand pesos", "A dice The ticket costs thirty thousand pesos... I mean thirteen thousand."),
        (ADULT + HOMEWORK + " ¿Qué páginas hay que leer? a) de la 20 a la 25 b) de la 2 a la 5", "a) de la 20 a la 25", "El guion dice pages twenty to twenty-five."),
        arith(ADULT + HOMEWORK + " ¿Cuántas páginas hay que leer, contando la 20 y la 25?", "25-20+1", "Se cuentan ambos extremos."),
    ],
    [
        ("Persona A escuchó «The bus leaves at eight fifteen». Persona B escuchó «The bus leaves from gate four». (leaves = sale, gate = puerta) Juntan los datos. ¿Cuál es la información completa? a) El bus sale a las 8:15 desde la puerta 4 b) El bus sale a las 4:15 desde la puerta 8", "a) El bus sale a las 8:15 desde la puerta 4", "A aporta la hora (eight fifteen) y B aporta el lugar (gate four)."),
        (ADULT + PRICE + " ¿Por qué B pidió repetir? a) porque dudó entre treinta mil y trece mil b) porque no hablaba inglés", "a) porque dudó entre treinta mil y trece mil", "Escuchó dos cifras distintas y quiso confirmar."),
    ],
    [
        (ADULT + "«A: The test is on October thirteenth. B: Sorry, thirteenth or thirtieth? A: Thirteenth.» (test = prueba) ¿Qué fecha corresponde? a) el 13 de octubre b) el 30 de octubre", "a) el 13 de octubre", "Thirteenth es el 13 y thirtieth es el 30; A confirma el 13."),
        ("Dos estudiantes tienen datos distintos: uno escuchó «Room 12» y otro «Room 20». ¿Qué pregunta les ayuda a decidir? a) Did you say twelve or twenty? b) Where is the bus?", "a) Did you say twelve or twenty?", "Es la pregunta que compara los dos números."),
    ],
    [(ADULT + "«Teacher: Please open your books on page forty-five. Student: Excuse me, miss. Did you say forty-five or fifty-four? Teacher: Forty-five.» (open = abrir, page = página). ¿Qué página debe abrir el estudiante?", "45", "La profesora confirma forty-five.")],
    [
        ("¿Qué significa «Could you repeat that, please?»?", "¿Puedes repetir eso, por favor?", "Se usa para pedir que repitan."),
        ("¿Qué pregunta confirma un número dudoso?", "Did you say fifteen or fifty?", "Compara las dos opciones."),
        ("¿Preguntar para aclarar es una falta de educación?", "No", "Es una forma amable de entender mejor."),
    ],
    task("Con una persona de tu casa: ella lee una frase con un dato que debes confirmar. Lee: «The concert is on Saturday at six thirty in the gym.» (concert = concierto, gym = gimnasio). Tú no lo captas y debes formular dos preguntas en inglés para aclarar. Escribe tus dos preguntas y la respuesta que recibirías.", "Preguntas: Could you repeat that, please? / Did you say six thirty? Respuesta: Yes, six thirty, on Saturday in the gym.", ["usa una frase de aclaración", "confirma un dato con Did you say…?", "escribe la respuesta esperada"], ["hoja con dos preguntas y respuesta", "nota de la persona"], ["preguntar sin confirmar el dato", "usar una pregunta de otra situación"], "Reconoce las frases correctas y practica con la persona la entonación de una pregunta educada."),
    "Pide a un adulto que lea de nuevo el diálogo de la hora y marca las frases que sirven para aclarar.",
    "Escribe en español cuándo es útil confirmar un dato y qué datos confundes con más frecuencia.",
)

# ---------------------------------------------------------------- clase 5: confirmar predicciones y resumir una idea con apoyo
PARK = "«Last weekend, our class cleaned a small park near the school. We collected twelve bags of leaves and eight bags of trash. A neighbor gave us juice. In the end, the park looked clean, and we felt proud.» (cleaned = limpió, park = parque, leaves = hojas, trash = basura, neighbor = vecina, proud = orgullosos)"
STORM = "«Chile is a long country, so its weather changes a lot. In the north there is a desert with little rain. In the center the summers are dry and warm. In the south there is a lot of rain and green forest. This is why people wear different clothes in each zone.» (weather = clima, long = largo, forest = bosque, zone = zona, clothes = ropa)"

lesson(
    OA3, 5,
    "Los textos breves y los marcos de resumen escritos en cada ejercicio, que lee un adulto en voz alta; una hoja y lápiz.",
    "Aprenderé a confirmar mis predicciones después de escuchar y a resumir una idea con un marco de apoyo. Sirve para recordar y contar a otra persona lo esencial de lo que oí.",
    ["Sé hacer predicciones y escuchar con un propósito.", "Conozco first, then y finally."],
    [
        "Después de escuchar, confirma tu predicción: ¿lo que esperabas apareció? Si sí, la confirmaste. Si no, la corriges. Esta comprobación te ayuda a recordar y a aprender cómo predecir mejor la próxima vez. Puedes decir: «I predicted… and the text said…» (Predije… y el texto dijo…).",
        "Un resumen (summary) cuenta la idea principal con pocas palabras y sin detalles menores. Para hacerlo con apoyo, usa un marco como: «The text is about… First…, then… In the end…». Puedes empezar con quién o qué, seguir con lo que pasó o lo que se explica y terminar con el resultado. Un resumen no copia frases enteras: las dice con tus palabras.",
        "Un buen resumen tiene dos o tres oraciones. Si tienes más, estás agregando detalles. Para elegir qué incluir, pregúntate: ¿esta información es esencial para entender la idea principal? Si la quitas y la idea sigue clara, no la incluyas. Pide a una persona que lea tu resumen y vea si puede entender el texto sin escucharlo.",
    ],
    [("confirm", "confirmar: comprobar que se cumplió"), ("summary", "resumen: la idea principal en pocas palabras"), ("main idea", "idea principal"), ("in the end", "al final"), ("prediction", "predicción"), ("detail", "detalle menor")],
    [
        ("Confirmar una predicción", "Título: «Cleaning the park». Predijiste oír las palabras leaves y trash. " + ADULT + PARK + " ¿Se confirmaron las dos?", ["Escucho y busco leaves: aparece twelve bags of leaves.", "Busco trash: aparece eight bags of trash.", "Ambas palabras aparecen."], "Sí, las dos se confirmaron"),
        ("Resumir con un marco", ADULT + PARK + " Completa: «The text is about… First…, then… In the end…».", ["Tema: la limpieza de un parque.", "Primero recolectaron hojas y basura.", "Al final el parque quedó limpio."], "El texto trata de una clase que limpió un parque: primero recolectó hojas y basura y al final el parque quedó limpio"),
    ],
    [
        ("Resumir copiando todas las frases del texto.", "Se cree que más palabras es mejor resumen.", "Usa el marco y deja solo la idea principal."),
        ("Resumir con un dato menor, como el jugo del vecino.", "Se confunde un detalle con la idea central.", "Pregunta si, sin ese dato, la idea sigue clara."),
    ],
    [
        (ADULT + STORM + " ¿Qué zona de Chile tiene poca lluvia? a) el norte b) el sur", "a) el norte", "El guion dice in the north there is a desert with little rain."),
        (ADULT + PARK + " ¿Cuántas bolsas de hojas recolectaron?", "12", "El guion dice twelve bags of leaves."),
        (ADULT + STORM + " ¿Qué zona tiene bosque verde y mucha lluvia? a) el sur b) el centro", "a) el sur", "El guion dice In the south there is a lot of rain and green forest."),
    ],
    [
        arith(ADULT + PARK + " ¿Cuántas bolsas recolectaron en total entre hojas y basura?", "12+8", "Se suman las bolsas de hojas y las de basura."),
        (ADULT + STORM + " ¿Por qué la gente usa ropa distinta en cada zona? a) porque el clima cambia mucho b) porque hay más tiendas", "a) porque el clima cambia mucho", "Dice that Chile is long, so its weather changes a lot."),
        ("Predijiste que un texto sobre el clima hablaría de nieve. El texto habló de desierto, centro y sur. ¿Qué haces? a) reviso mi predicción y la corrijo b) digo que el texto está mal", "a) reviso mi predicción y la corrijo", "Corregir la predicción con lo escuchado es parte de la estrategia."),
    ],
    [
        (ADULT + STORM + " ¿Cómo es el verano en el centro del país? a) seco y cálido b) frío y lluvioso", "a) seco y cálido", "El guion dice In the center the summers are dry and warm."),
        (ADULT + PARK + " ¿Cómo se sintieron los estudiantes al final?", "Orgullosos", "El guion dice we felt proud."),
        (ADULT + PARK + " ¿Qué hizo una vecina? a) les dio jugo b) les prestó una escoba", "a) les dio jugo", "El guion dice A neighbor gave us juice."),
    ],
    [
        (ADULT + STORM + " ¿Cuál es el mejor resumen? a) Chile es largo y su clima cambia en el norte, el centro y el sur b) Chile tiene un desierto con poca lluvia", "a) Chile es largo y su clima cambia en el norte, el centro y el sur", "Incluye la idea principal; la otra opción es solo un detalle."),
        (ADULT + PARK + " ¿Cuál de estos es un detalle que se puede dejar fuera del resumen? a) que una vecina dio jugo b) que limpiaron el parque", "a) que una vecina dio jugo", "No cambia la idea principal."),
    ],
    [
        (ADULT + PARK + " Ordena los hechos para un resumen. A) The park looked clean. B) The class collected bags. C) The class cleaned the park. D) They felt proud.", "C, B, A, D", "Primero limpiaron, recolectaron bolsas y al final el parque quedó limpio y se sintieron orgullosos."),
        (ADULT + STORM + " Escribe en una oración corta el resumen del texto, usando las palabras north, center y south.", "El clima de Chile cambia entre el norte, el centro y el sur", "Resume la idea principal con las tres zonas."),
    ],
    [(ADULT + "«Last Friday, our school had a book fair. Students sold used books for one thousand pesos each. We collected forty thousand pesos. With that money, we will buy new books for the library.» (book fair = feria del libro, used = usados, each = cada uno, money = dinero). ¿Cuál es el mejor resumen? a) El colegio vendió libros usados para comprar libros nuevos para la biblioteca b) El colegio vendió libros por mil pesos", "a) El colegio vendió libros usados para comprar libros nuevos para la biblioteca", "Incluye qué hicieron y para qué; la otra opción es solo un dato.")],
    [
        ("¿Qué es un resumen?", "La idea principal en pocas palabras", "No incluye los detalles menores."),
        ("¿Qué haces después de escuchar para comprobar tu predicción?", "Reviso si lo que esperaba apareció", "Así confirmo o corrijo."),
        ("¿Qué marco puedes usar para resumir?", "The text is about…, first…, then…, in the end…", "Ordena las ideas."),
    ],
    task("Un adulto lee dos veces este texto: «Last Sunday, my family went to the lake. We rented a small boat, and my brother rowed for an hour. We saw ducks and a heron. At six o'clock, we ate sandwiches on the shore and went home tired but happy.» (lake = lago, rented = arrendamos, rowed = remó, ducks = patos, heron = garza, shore = orilla). Primero escribe una predicción a partir del título «A day at the lake». Después escribe un resumen de dos oraciones con el marco The text is about…, First…, In the end…", "Predicción: boat, water, ducks. Resumen: The text is about a family trip to the lake. First, they rented a boat and saw birds; in the end, they ate sandwiches and went home happy.", ["escribe una predicción con tres palabras", "confirma o corrige", "resume con el marco en dos oraciones"], ["hoja con predicción y resumen", "nota del adulto"], ["resumir con demasiados detalles", "copiar frases enteras"], "Reconoce el resumen y revisa con la persona qué detalles se pueden quitar sin perder la idea."),
    "Pide a un adulto que lea de nuevo el texto del parque y escribe dos resúmenes: uno de una oración y otro de tres.",
    "Escribe en español qué estrategia de escucha te ayuda más: predecir, escuchar con propósito, usar gestos o preguntar.",
)
