"""Cuaderno del estudiante, 1.º medio Inglés (oficial): IN1M OA 13, historias e información con recursos multimodales.

Los recursos visuales se describen con palabras dentro del enunciado («Image description: ...») y los datos de
gráficos son «de ejemplo». Todo texto en inglés es original y lleva glosario en español.
"""
from __future__ import annotations

from student_content_in_m1_b import MAT, lesson, mc, task
from student_lessons import arith, ex

OA = "IN1M OA 13"

# ============================================================ clase 1: propósito, audiencia y recursos
POST1 = "«Poster A: Headline: Walk to school! Image: a group of students crossing a street under a smiling sun. Small text: Healthy, free and fun.»"
GPOST1 = "(walk = caminar; crossing = cruzando; smiling = sonriente; healthy = saludable; free = gratis)"
SLIDES = "«Digital story. Slide 1: a photo of an empty chair with the text Nico's first day. Slide 2: a photo of two hands shaking with the text A new friend.»"
GSLIDES = "(empty = vacía; shaking = estrechándose; hands = manos; friend = amigo)"
BOOK = "«Poster B: Headline: Book swap! Image: a pile of books with a heart. Text: Bring one book, take one book. Friday, 13:00, library.»"
GBOOK = "(swap = intercambio; pile = pila; heart = corazón; bring = trae; take = lleva)"

lesson(
    OA, 1, MAT,
    "Aprenderé a reconocer qué recursos usa un texto multimodal (palabras, imágenes, colores, letras) y para quién y para qué sirve cada uno. Sirve para escribir historias e información que se vean atractivas y se entiendan rápido.",
    ["Sé escribir oraciones simples en inglés.", "Conozco palabras como poster, picture y title."],
    [
        "Un texto multimodal (multimodal text) combina palabras con otros recursos (resources): imágenes, fotos, colores, tipos de letra, gráficos, íconos, la manera de ordenar todo en la página (layout) y, en pantalla, también sonido o video. Los recursos no son adornos: cada uno debe apoyar el mensaje (message), que es la idea principal que quieres comunicar.",
        "Antes de escribir, decide el propósito (purpose) y la audiencia (audience). El propósito puede ser contar una historia (narrate), informar (inform) o convencer (persuade). La audiencia es la persona que leerá o verá el texto: niños pequeños, compañeros, familias. Para escribir con ideas claras, puedes partir de temas como experiencias personales, contenidos de otras asignaturas, asuntos de interés global, la cultura de otros países o textos que leíste.",
        "Un buen texto multimodal tiene un titular (headline) corto, una imagen que muestra lo mismo que dicen las palabras, letras grandes y de buen contraste, pocos colores y un orden claro. Si un recurso no ayuda al mensaje, quítalo. Si la imagen dice una cosa y el texto otra, el lector se confunde.",
    ],
    [("multimodal text", "texto que combina palabras con imágenes u otros recursos"), ("resource", "recurso: imagen, color, letra, gráfico"), ("message", "mensaje: idea principal"), ("purpose", "propósito: para qué se escribe"), ("audience", "audiencia: quién lee o ve"), ("headline", "titular"), ("layout", "diseño u orden en la página")],
    [
        ("Recurso que apoya el mensaje", "Afiche: «Headline: Close the tap! Image: a tap with water drops falling. Small text: Save water at school.» (tap = llave; drops = gotas; save = ahorrar) ¿Cuál es el mensaje y qué recurso lo apoya?",
         ["El titular es una orden corta: Close the tap!", "La imagen muestra una llave que gotea, o sea, agua que se desperdicia.", "El texto pequeño dice la acción: Save water at school."], "Mensaje: ahorrar agua en el colegio; la imagen de la llave que gotea apoya el mensaje"),
        ("Elegir recursos según la audiencia", "Debes crear una historia sobre un conejo para niños de 6 años. ¿Qué recursos eliges?",
         ["La audiencia son niños pequeños que leen poco.", "Necesitan dibujos grandes y de colores.", "También oraciones muy cortas con letras grandes."], "Dibujos grandes y de colores, oraciones cortas y letras grandes"),
    ],
    [
        ("Poner muchas imágenes y colores sin pensar si apoyan el mensaje.", "Los recursos que no ayudan al mensaje distraen.", "Deja solo los que refuerzan la idea principal."),
        ("Escribir un texto largo sin pensar en quién lo leerá.", "No se adapta a la audiencia.", "Decide antes quién leerá y cuánto tiempo tendrá."),
    ],
    [
        mc("Un texto multimodal (multimodal text) es un texto que", "combina palabras con imágenes u otros recursos", ["solo tiene palabras", "solo se escucha"], "Multi indica varios recursos."),
        mc("El mensaje (message) de un texto es", "la idea principal que quieres comunicar", ["el color del fondo", "el número de página"], "Todos los recursos deben apoyarlo."),
        mc("La audiencia (audience) es", "la persona que leerá o verá tu texto", ["la persona que lo imprime", "el lugar donde se cuelga"], "Se decide pensando en quién lo recibe."),
    ],
    [
        mc(f"Lee: {POST1} {GPOST1} ¿Cuál es el mensaje del afiche?", "Ir caminando al colegio es una buena idea", ["Los cruces de calle son peligrosos", "Los colegios son gratis"], "El titular dice Walk to school! y el texto agrega sus ventajas."),
        mc(f"Lee: {POST1} {GPOST1} ¿Cuál es el propósito del afiche?", "Convencer a los estudiantes de caminar al colegio", ["Contar una historia de un niño", "Explicar cómo funciona un semáforo"], "Usa una orden y ventajas para persuadir."),
        mc(f"Lee: {SLIDES} {GSLIDES} ¿Qué propósito tiene esta historia digital?", "Contar una experiencia personal de un niño que conoce a un amigo nuevo", ["Dar el horario del colegio", "Vender sillas"], "Las diapositivas muestran una secuencia: primer día y nuevo amigo."),
    ],
    [
        mc("Haces un afiche sobre cuidar el agua para niños de 7 años. ¿Qué conjunto de recursos es mejor?", "Un dibujo grande de una gota y una frase corta con letras grandes", ["Un párrafo de ochenta palabras con letras pequeñas", "Una tabla con muchos números"], "Los niños pequeños necesitan imágenes claras y poco texto."),
        mc("Un afiche se verá desde tres metros de distancia. ¿Qué combinación de letras es más legible?", "Letras grandes y oscuras sobre fondo claro", ["Letras pequeñas amarillo claro sobre fondo blanco", "Letras medianas rojas sobre fondo naranja"], "El buen contraste y el tamaño ayudan a leer de lejos."),
        mc("Un texto sobre el plástico en el mar trata un tema de", "interés global", ["una experiencia personal únicamente", "la cultura de otro país únicamente"], "El plástico en el mar es un asunto que afecta a muchos países."),
    ],
    [
        mc("Un afiche tiene el titular «Join our soccer team!» pero la imagen muestra una cancha vacía y nublada sin personas. ¿Qué problema tiene?", "La imagen no refuerza el mensaje de invitar a jugar", ["El titular es demasiado corto", "El titular no puede llevar un verbo"], "El mensaje invita a unirse, pero la imagen no muestra personas ni energía."),
        mc("Para el pasillo de un colegio hay dos afiches sobre reciclar papel. El 1 tiene 80 palabras y ninguna imagen. El 2 tiene un titular de tres palabras, un ícono de reciclaje y una frase. ¿Cuál es mejor?", "El 2, porque se entiende en segundos para quien pasa caminando", ["El 1, porque explica más", "Los dos, porque nadie lee afiches"], "En un pasillo la gente mira pocos segundos."),
    ],
    [
        mc("Una diapositiva tiene cuatro imágenes, tres tipos de letra, cinco colores y una oración corta. ¿Qué cambio la mejora más?", "Dejar una sola letra y dos imágenes que apoyen el mensaje", ["Agregar dos colores más", "Hacer la oración más pequeña"], "Pocos recursos coherentes se leen mejor."),
        mc("Debes adaptar un afiche para vecinos que lo verán desde un paradero, mientras esperan la micro. ¿Qué cambio conviene?", "Titular grande y una sola idea con una imagen clara", ["Un texto largo con letras chicas", "Muchas fotos pequeñas"], "Es poco tiempo de lectura: conviene un mensaje rápido."),
    ],
    [mc(f"El colegio hace un intercambio de libros. Revisa este afiche: {BOOK} {GBOOK} ¿Cuándo y dónde es?", "El viernes a las 13:00, en la biblioteca", ["El jueves a las 13:00, en el patio", "El viernes a las 10:00, en la biblioteca"], "El texto pequeño da día, hora y lugar.")],
    [
        mc("¿Qué es un titular (headline)?", "El título corto y llamativo del texto", ["El último párrafo"], "Atrae la mirada y resume el mensaje."),
        mc("¿Cuál de estos propósitos es persuadir?", "Convencer a alguien de hacer algo", ["Contar una anécdota sin pedir nada"], "Persuadir busca que el lector actúe."),
        ("Escribe en inglés la palabra que significa «mensaje».", "Message", "Message es la idea principal."),
    ],
    task(f"Debes diseñar en papel un afiche para invitar a un intercambio de libros del colegio con estos datos: «Book swap, Friday, 13:00, library, bring one book and take one book.» En tu hoja escribe: (1) un titular de hasta cinco palabras, (2) la imagen que dibujarías, (3) dos datos que irían en letra pequeña, (4) a qué audiencia se dirige.",
         "(1) Swap a book! (2) Dibujo de dos manos intercambiando un libro. (3) Friday, 13:00 / Bring one book, take one book. (4) A estudiantes del colegio.",
         ["el titular es corto y claro", "la imagen apoya el mensaje", "los datos son exactos y suficientes", "nombra la audiencia"],
         ["cuatro respuestas y un dibujo en la hoja"],
         ["omitir el día o el lugar", "elegir una imagen que no se relaciona con el mensaje"],
         "Pide que muestre el afiche a otra persona y compruebe si entiende el mensaje en cinco segundos."),
    "Copia los siete términos del vocabulario y dibuja un ejemplo de tres de ellos.",
    "Observa un afiche de tu calle y escribe en español su mensaje, su propósito y su audiencia.",
)

# ============================================================ clase 2: evidencia precisa entre imagen, texto y gráfico
CH2 = "«Chart (de ejemplo): Books read by Class 1A in a month. Week 1: 12. Week 2: 18. Week 3: 9. Week 4: 21.»"
GCH2 = "(chart = gráfico; books = libros; read = leídos; week = semana)"
IMG2 = "«Image description: Two girls wear helmets and ride bikes along a river path.»"
GIMG2 = "(helmets = cascos; ride = andan; river = río; path = sendero)"
SEEDP = "«Image description: Three students plant a small tree in the school yard.»"
GSEEDP = "(plant = plantan; yard = patio)"
BOT = "«Chart (de ejemplo): Plastic bottles collected. Monday: 20. Tuesday: 35. Wednesday: 15.»"
GBOT = "(plastic bottles = botellas plásticas; collected = recolectadas)"

lesson(
    OA, 2, MAT,
    "Aprenderé a comprobar que las palabras que escribo calzan exactamente con una imagen o un gráfico. Sirve para escribir pies de foto y datos que no confundan ni exageren.",
    ["Sé reconocer el mensaje, el propósito y la audiencia de un texto multimodal.", "Conozco los números y los días de la semana en inglés."],
    [
        "Cuando una imagen o un gráfico acompaña un texto, las palabras deben coincidir con la evidencia (evidence) visible. Un pie de foto (caption) describe con exactitud lo que se ve: quiénes, qué hacen y dónde. Si la imagen muestra a tres estudiantes plantando un árbol, el pie de foto no puede decir que limpian un río.",
        "Un gráfico de barras (bar chart) muestra cantidades por categoría; la barra más alta es el valor mayor. Para escribir una oración sobre un gráfico, primero lee los números y compáralos: the most (el mayor), the fewest (el menor), more than (más que), fewer than (menos que). Después comprueba que tu oración sea verdadera según los datos. Los datos de los gráficos de este cuaderno son de ejemplo.",
        "Regla de coherencia: cada oración de un texto multimodal debe tener su evidencia. Si un compañero escribe un número o un dato que no está en el gráfico o la imagen, hay que corregirlo. También puedes sumar o restar datos del gráfico si necesitas un total o una diferencia, y escribirlos en una oración clara.",
    ],
    [("caption", "pie de foto"), ("bar chart", "gráfico de barras"), ("the most / the fewest", "el mayor / el menor"), ("more than / fewer than", "más que / menos que"), ("evidence", "evidencia: dato visible que apoya una oración"), ("total", "total")],
    [
        ("Elegir el pie de foto exacto", f"{SEEDP} {GSEEDP} ¿Qué pie de foto corresponde: «Students plant a tree in the school yard» o «Students clean a river»?",
         ["La imagen muestra tres estudiantes, un árbol pequeño y un patio.", "Students plant a tree in the school yard describe exactamente eso.", "Clean a river no aparece en la imagen."], "Students plant a tree in the school yard"),
        ("Comprobar una oración con un gráfico", f"{BOT} {GBOT} ¿Es verdadera la oración «We collected the most bottles on Tuesday»?",
         ["Lunes: 20; martes: 35; miércoles: 15.", "El valor mayor es 35, del martes.", "La oración es verdadera."], "Sí, es verdadera: el martes tiene el valor mayor (35)"),
    ],
    [
        ("Escribir un pie de foto con un detalle que la imagen no muestra, como «in winter».", "Se agrega información que no se ve y que podría ser falsa.", "Describe solo lo que se ve o añade datos que conozcas con certeza."),
        ("Leer mal una barra y decir que el menor valor es el mayor.", "Se comparan mal los números del gráfico.", "Ordena los números antes de escribir the most o the fewest."),
    ],
    [
        mc("Un pie de foto (caption) bueno", "describe con exactitud lo que se ve en la imagen", ["cuenta una historia distinta", "no se relaciona con la imagen"], "El pie de foto sirve para explicar la imagen."),
        mc("En un gráfico de barras, la barra más alta indica", "el valor mayor", ["el valor menor", "el título"], "A mayor altura, mayor cantidad."),
        mc("«The fewest» significa", "el menor", ["el mayor", "el primero"], "The fewest es la cantidad más pequeña."),
    ],
    [
        mc(f"{IMG2} {GIMG2} ¿Qué pie de foto corresponde mejor?", "Two girls ride bikes along a river path", ["Two girls fish in the river", "Two boys play soccer"], "Los cascos, las bicicletas y el sendero junto al río están en la descripción."),
        mc(f"{CH2} {GCH2} ¿En qué semana leyó menos libros el curso?", "Week 3", ["Week 1", "Week 4"], "Week 3 tiene 9, el menor valor."),
        mc(f"{IMG2} {GIMG2} ¿Cuál oración está apoyada por la imagen?", "The girls wear helmets", ["The girls carry umbrellas", "The girls ride horses"], "La descripción dice que llevan casco."),
    ],
    [
        mc(f"{CH2} {GCH2} ¿Qué oración es verdadera según el gráfico?", "Week 2 had more books than Week 1", ["Week 3 had more books than Week 4", "Week 1 had the most books"], "Week 2 tiene 18 y Week 1 tiene 12."),
        arith(f"{CH2} ¿Cuántos libros leyó el curso en las cuatro semanas?", "12+18+9+21", "Se suman los cuatro valores del gráfico.", " libros"),
        arith(f"{CH2} ¿Cuántos libros más leyó el curso en Week 4 que en Week 3?", "21-9", "Se restan los valores de las dos semanas.", " libros"),
    ],
    [
        mc(f"Un compañero escribe este pie de foto para {IMG2}: «Two girls fish in the river.» ¿Qué está mal?", "La imagen muestra a dos niñas en bicicleta, no pescando", ["Falta el nombre de la ciudad", "Está demasiado corto"], "El pie de foto debe coincidir con la imagen."),
        mc(f"Un compañero escribe: «The class read 70 books this month.» Revisa {CH2} ¿Qué corrección haces?", "Son 60 libros en total, según el gráfico", ["Está bien", "Son 52 libros en total"], "12 + 18 + 9 + 21 = 60."),
    ],
    [
        mc(f"{CH2} Elige el mejor titular para este gráfico.", "Week 4 is our reading record!", ["Reading goes down every week", "Nobody reads in Week 3"], "Week 4 tiene el valor mayor; las otras opciones son falsas."),
        arith(f"{CH2} La meta del curso era leer 70 libros. ¿Cuántos libros faltaron?", "70-60", "La meta menos el total leído.", " libros"),
    ],
    [mc("En el diario mural te piden escribir el pie de una foto de la feria de ciencias. «Image description: A boy shows a small volcano model to two visitors.» (volcano = volcán; model = maqueta; visitors = visitantes) ¿Cuál escribes?", "A student shows his volcano model to visitors", ["Visitors cook at the science fair", "A girl measures the rain"], "Describe lo que se ve con las palabras clave de la imagen.")],
    [
        mc("¿Qué oración sobre un gráfico necesita revisar números?", "The most and the fewest", ["Hello and goodbye"], "Los superlativos dependen de los valores."),
        mc("Si un dato no está en la imagen ni en el gráfico, debes", "no escribirlo o buscar otra evidencia", ["escribirlo igual"], "Las oraciones deben tener evidencia."),
        ("Escribe en inglés la palabra que significa «gráfico de barras».", "Bar chart", "Bar chart muestra cantidades con barras."),
    ],
    task(f"Mira esta información: {BOT} Image description: «Four students carry two big bags of bottles to a recycling bin.» (bags = bolsas; recycling bin = contenedor de reciclaje; carry = llevan). En tu hoja escribe: (1) un pie de foto de la imagen, (2) dos oraciones verdaderas sobre el gráfico con most, fewest, more than o fewer than, (3) el total de botellas.",
         "(1) Four students carry two big bags of bottles to a recycling bin. (2) Tuesday had the most bottles. Wednesday had fewer bottles than Monday. (3) 70 botellas.",
         ["el pie de foto describe lo que se ve", "las dos oraciones son verdaderas según el gráfico", "el total es 70"],
         ["tres respuestas escritas en la hoja"],
         ["agregar datos que la imagen no muestra", "calcular mal el total"],
         "Pide que marque en el gráfico los números que usó en cada oración."),
    "Copia los seis términos del vocabulario y dibuja un gráfico de barras con tres barras de ejemplo.",
    "Escribe un pie de foto en español para una foto de tu calle y revisa que diga solo lo que se ve.",
)

# ============================================================ clase 3: narrar con pasado simple y conectores
PAN = "«Image 1: a boy at a bus stop in the rain. Image 2: a bus arrives and it is full of people. Image 3: a woman gives him her seat.»"
GPAN = "(bus stop = paradero; full of = lleno de; gives = le da; seat = asiento)"
BOTL = "«Nico went to the beach with his cousin. He saw a green bottle. He opened it and found a small map. Finally, he showed the map to his teacher.»"
GBOTL = "(beach = playa; cousin = primo; bottle = botella; opened = abrió; map = mapa; showed = mostró)"

lesson(
    OA, 3, MAT,
    "Aprenderé a escribir una historia corta con pasado simple, conectores de orden y un guion de viñetas (storyboard). Sirve para contar una experiencia con imágenes y frases claras.",
    ["Sé que la historia tiene inicio, desarrollo y final.", "Conozco went, saw y found."],
    [
        "Una historia multimodal se planifica con un guion de viñetas (storyboard): una serie de cuadros en los que cada uno tiene una imagen y una oración (caption). Cada viñeta debe mostrar una sola idea. La primera presenta el personaje y el lugar; las siguientes muestran lo que ocurre; la última cierra la historia.",
        "Para narrar hechos terminados se usa el pasado simple (past simple). Los verbos regulares terminan en -ed: opened, showed, walked. Muchos verbos frecuentes son irregulares y cambian: go-went, see-saw, find-found, take-took, have-had, make-made, buy-bought, run-ran. No se agrega -ed a los irregulares: taked y goed son errores.",
        "Los conectores de orden (sequence words) ayudan a seguir la historia: first (primero), then (luego), after that (después de eso), finally (por fin). Para hacer más atractiva la historia, agrega adjetivos y detalles: the enormous black dog ran across the empty square es más vivo que the dog ran. Mantén todo el relato en el mismo tiempo verbal.",
    ],
    [("storyboard", "guion en viñetas"), ("caption", "oración que acompaña una viñeta"), ("past simple", "pasado simple"), ("irregular verb", "verbo irregular"), ("first / then / after that / finally", "primero / luego / después de eso / por fin"), ("detail", "detalle")],
    [
        ("Poner verbos en pasado", "Escribe en pasado simple los verbos go, see y find para completar: «Yesterday Nico ___ to the beach, ___ a bottle and ___ a map.»",
         ["Los tres son verbos irregulares.", "Go cambia a went, see a saw y find a found.", "Se escribe: went, saw, found."], "went, saw, found"),
        ("Planificar un storyboard", f"Texto: {BOTL} {GBOTL} ¿Qué conector de orden aparece en la última viñeta y qué muestra?",
         ["Busco la palabra que cierra la historia.", "Finally introduce la última acción.", "La última viñeta muestra que Nico le muestra el mapa a su profesor."], "Finally: Nico le muestra el mapa a su profesor"),
    ],
    [
        ("Escribir «taked» en vez de «took».", "Se usa la terminación -ed en un verbo irregular.", "Aprende las formas irregulares: take-took."),
        ("Cambiar de tiempo en medio de la historia: «He went to the park and sees a dog».", "Se mezclan pasado y presente.", "Mantén todo en pasado: he saw a dog."),
    ],
    [
        mc("El pasado simple de go es", "went", ["goed", "gone"], "Go es irregular: went."),
        mc("¿Qué conector sirve para empezar la historia?", "First", ["Finally"], "First es el primer paso del relato."),
        mc("Un storyboard (guion en viñetas) es", "una serie de cuadros con imagen y oración", ["una lista de verbos", "una receta"], "Cada cuadro cuenta una parte de la historia."),
    ],
    [
        mc("Completa: «Yesterday Luisa ___ a photo of the sunset.»", "took", ["taked", "taken"], "Take es irregular: took."),
        mc("Completa: «She ___ a lost cat near the market.» (cat = gato)", "saw", ["seen", "seed"], "See cambia a saw en pasado."),
        mc("Completa: «First, Martina bought a ticket. ___, she got on the train.»", "Then", ["Because", "But"], "Then indica lo que ocurre a continuación."),
    ],
    [
        mc(f"Escribes el pie de la imagen 1: {PAN} {GPAN} ¿Qué oración corresponde?", "First, the boy waited at the bus stop in the rain", ["First, the boy wait at the bus stop in the rain", "First, the boy sleeps at the bus stop"], "Va en pasado y coincide con la imagen."),
        mc(f"Escribes el pie de la imagen 2: {PAN} {GPAN} ¿Qué oración corresponde?", "Then the bus arrived, but it was full", ["Then the bus leaved, and it was empty", "Then the bus is arriving full"], "Arrived está en pasado y full coincide con la imagen."),
        mc(f"Escribes el pie de la imagen 3: {PAN} {GPAN} ¿Qué oración corresponde?", "Finally, a woman gave him her seat", ["Finally, a woman give him her seat", "Finally, the bus broke"], "Gave es el pasado de give y la acción se ve en la imagen."),
    ],
    [
        mc("¿Qué versión es más atractiva para una historia? Versión 1: «The dog was big.» Versión 2: «The enormous black dog ran across the empty square.» (enormous = enorme; square = plaza)", "La versión 2, porque agrega detalles y una acción", ["La versión 1, porque es más corta", "Las dos son iguales"], "Los adjetivos y la acción hacen la imagen mental más clara."),
        mc("Observa: «Image: a girl in red boots jumps in a puddle.» (boots = botas; puddle = charco) ¿Qué texto agrega información que la imagen no puede mostrar?", "The rain stopped and she felt happy", ["A girl in red boots jumped in a puddle", "A girl wears boots"], "Los sentimientos y el tiempo atmosférico completan a la imagen."),
    ],
    [
        mc("¿Qué oración está bien escrita en una historia en pasado?", "Yesterday we went to the museum", ["Yesterday we go to the museum", "Yesterday we goes to the museum"], "Went es el pasado de go."),
        mc("¿Cuál de estas secuencias usa los conectores en un orden lógico?", "First, Ana made a list. Then she bought apples. After that, she cooked. Finally, she ate", ["Finally, Ana made a list. Then she ate. First, she cooked"], "Los conectores siguen el orden real de las acciones."),
    ],
    [mc("Debes escribir el pie de la última viñeta de una historia sobre un gato perdido. «Image: a girl gives the cat to a smiling family.» (smiling = sonriente) ¿Cuál escribes?", "Finally, she gave the cat to a smiling family", ["Finally, she give the cat to a smiling family", "First, she gave a cat"], "Gave es el pasado de give y finally cierra la historia.")],
    [
        mc("¿Cuál es el pasado de find?", "Found", ["Finded"], "Find es irregular: found."),
        mc("Los conectores first, then y finally sirven para", "ordenar las acciones", ["traducir palabras"], "Marcan la secuencia."),
        ("Escribe el pasado simple del verbo «make».", "Made", "Make es irregular: made."),
    ],
    task("Mira estas imágenes de una historia y escribe cuatro oraciones con first, then, after that y finally: Image 1: a girl walks to a market. Image 2: she sees a small lost cat. Image 3: she takes the cat to a shop owner. Image 4: the owner finds a poster with the cat's picture. Usa los verbos walk, see, take y find en pasado. (market = feria; shop owner = dueño de una tienda; poster = afiche; picture = foto)",
         "First, a girl walked to the market. Then she saw a small lost cat. After that, she took the cat to a shop owner. Finally, the owner found a poster with the cat's picture.",
         ["usa los cuatro conectores en orden", "los cuatro verbos están en pasado", "cada oración corresponde a una imagen"],
         ["cuatro oraciones en la hoja"],
         ["usar taked o finded", "no seguir el orden de las imágenes"],
         "Pide que dibuje un cuadro simple para cada oración y compruebe que coinciden."),
    "Copia los cuatro conectores y los ocho verbos irregulares con su pasado y dibuja un símbolo para cada uno.",
    "Cuenta con cuatro oraciones en español una salida que hiciste y subraya los conectores que podrías pasar a inglés.",
)

# ============================================================ clase 4: brecha de información para armar un afiche
HAN_A = "«Card A (images): Image 1: people sitting under cherry trees with food.»"
HAN_B = "«Card B (facts): In Japan, families and friends have picnics under cherry trees in spring. This is called hanami.»"
GHAN = "(cherry trees = cerezos; picnics = picnics; spring = primavera; called = llamado)"
WAT_A = "«Card A (images): Image 1: a full glass of water. Image 2: a dripping tap. Image 3: a bucket under the tap.»"
WAT_B = "«Card B (messages): Message 1: Water is precious. Message 2: A dripping tap wastes water. Message 3: Collect it and use it for plants.»"
GWAT = "(glass = vaso; dripping = goteando; tap = llave; bucket = balde; precious = valiosa; wastes = desperdicia; collect = junta; plants = plantas)"
CAR_A = "«Card A (images): Image 1: dancers in colorful costumes in a street parade.»"
CAR_B = "«Card B (facts): Carnival is a big festival in Brazil. It has music, dance and parades in the streets.»"
GCAR = "(dancers = bailarines; costumes = trajes; parade = desfile; festival = fiesta; music = música)"
BIKE_A = "«Card A (images): Image 1: a bicycle. Image 2: a bus. Image 3: a group of friends walking.»"
BIKE_B = "«Card B (messages): Message 1: Bikes do not make smoke. Message 2: A bus carries many people. Message 3: Walking is free and healthy.»"
GBIKE = "(smoke = humo; carries = lleva; healthy = saludable; walking = caminando)"
PLNT_A = "«Card A (images): Image 1: a seed. Image 2: a small plant. Image 3: a flower.»"
PLNT_B = "«Card B (facts): A seed needs water and light to grow. Then a small plant grows leaves. Later, the plant makes flowers.»"
GPLNT = "(seed = semilla; light = luz; grow = crecer; leaves = hojas; flowers = flores)"

lesson(
    OA, 4, MAT,
    "Aprenderé a unir una tarjeta con imágenes y otra con datos para escribir pies de foto y armar un afiche o infografía, y a pedir lo que falta. Sirve para trabajar en pareja con información repartida.",
    ["Sé escribir pies de foto exactos.", "Conozco las preguntas what, which y how many."],
    [
        "En una brecha de información (information gap) cada compañero tiene una parte: por ejemplo, uno tiene la tarjeta con las imágenes (images) y el otro la tarjeta con los datos (facts) o los mensajes (messages). Para armar el texto, hay que emparejar cada imagen con el dato que la explica, sin inventar. Puedes usar frases como: My card says… (mi tarjeta dice…), I have a picture of… (tengo una imagen de…), Which fact goes with image 2? (¿qué dato va con la imagen 2?) y Can you read the first fact, please? (¿puedes leer el primer dato, por favor?).",
        "Una infografía (infographic) o un afiche (poster) tiene partes que se ordenan: titular (headline), imagen, pie de foto (caption) y, a veces, una invitación a actuar (call to action), como Save water! o Join us! El orden de lectura va de arriba hacia abajo y de izquierda a derecha, y cada pie de foto debe estar cerca de su imagen.",
        "Cuando unes dos tarjetas, revisa dos cosas. Primero, la coherencia: el dato debe describir lo que muestra la imagen. Segundo, la fidelidad: no agregues cifras, nombres ni fechas que no aparecen en ninguna tarjeta. Si algo falta, pregúntalo a tu compañero.",
    ],
    [("information gap", "brecha de información"), ("facts", "datos"), ("message", "mensaje"), ("infographic", "infografía: imágenes y datos ordenados"), ("call to action", "invitación a actuar"), ("My card says…", "mi tarjeta dice…"), ("Which fact goes with image 2?", "¿qué dato va con la imagen 2?")],
    [
        ("Unir imagen y dato", f"Tarjetas: {HAN_A} {HAN_B} {GHAN} Escribe un pie de foto que una ambas tarjetas.",
         ["La tarjeta A muestra personas bajo cerezos con comida.", "La tarjeta B explica que en Japón se hace un picnic bajo los cerezos en primavera y se llama hanami.", "Pie de foto: Hanami: people have a picnic under cherry trees in spring."], "Hanami: people have a picnic under cherry trees in spring"),
        ("Ordenar tres imágenes con tres datos", f"Tarjetas: {PLNT_A} {PLNT_B} {GPLNT} ¿Qué dato va con la imagen 2?",
         ["Las imágenes siguen el orden: semilla, planta pequeña, flor.", "Los datos siguen el mismo orden: semilla, planta pequeña, flores.", "La imagen 2 es la planta pequeña, y su dato es Then a small plant grows leaves."], "Then a small plant grows leaves"),
    ],
    [
        ("Agregar a un pie de foto una fecha o una cifra que no está en ninguna tarjeta.", "Se inventa información.", "Usa solo los datos de las tarjetas o pregunta a tu compañero."),
        ("Emparejar el mensaje 3 con la imagen 1 solo porque está primero.", "Se empareja por posición y no por significado.", "Relaciona cada dato con lo que muestra la imagen."),
    ],
    [
        mc("My card says… significa", "mi tarjeta dice…", ["mi tarjeta es azul", "mi tarjeta no está"], "Sirve para leer tu parte de la información."),
        mc("En una infografía, el pie de foto debe estar", "cerca de su imagen", ["en otra página", "al final del cuaderno"], "Así el lector ve la relación."),
        mc("Un call to action es", "una invitación a hacer algo", ["un título en español", "una imagen sin texto"], "Por ejemplo, Save water!"),
    ],
    [
        mc(f"Tarjetas: {WAT_A} {WAT_B} {GWAT} ¿Qué mensaje va con la imagen 2?", "A dripping tap wastes water", ["Water is precious", "Collect it and use it for plants"], "El mensaje 2 habla de una llave que gotea, como muestra la imagen 2."),
        mc(f"Tarjetas: {WAT_A} {WAT_B} {GWAT} ¿Qué imagen va con «Collect it and use it for plants»?", "El balde bajo la llave", ["El vaso lleno", "La llave que gotea sola"], "El balde recoge el agua que cae."),
        mc(f"Tarjetas: {WAT_A} {WAT_B} {GWAT} ¿Qué titular une bien las tres imágenes y mensajes?", "Every drop counts!", ["Dance in the street!", "Plant a seed!"], "Los tres mensajes hablan del valor del agua."),
    ],
    [
        mc(f"Tarjetas: {CAR_A} {CAR_B} {GCAR} ¿Qué pie de foto combina las dos tarjetas?", "Carnival in Brazil: music, dance and parades in the streets", ["Carnival in Brazil: quiet walks in the forest", "Parade in Japan: cherry trees"], "Une la imagen del desfile con los datos de la tarjeta B."),
        mc(f"Solo tienes la tarjeta A: {CAR_A} ¿Qué pregunta le haces a tu compañero para saber en qué país ocurre?", "Which country is it?", ["What color is the costume?", "Who are the dancers?"], "El país está en la tarjeta B."),
        mc(f"Tu compañero dice que en la tarjeta B hay datos sobre invierno. Revisa {CAR_B} ¿Qué respondes?", "No, no menciona invierno: dice música, baile y desfiles", ["Sí, hay datos de invierno", "No hay ningún dato"], "Los datos verificables están en la tarjeta."),
    ],
    [
        mc(f"Tarjetas: {BIKE_A} {BIKE_B} {GBIKE} Un compañero empareja la imagen 3 con «Bikes do not make smoke». ¿Qué corrección haces?", "La imagen 3 (amigos caminando) va con «Walking is free and healthy»", ["Está bien", "La imagen 3 va con A bus carries many people"], "Hay que unir por significado."),
        mc(f"Tarjetas: {BIKE_A} {BIKE_B} El pie de foto de la imagen 2 dice: «A bus carries 80 people.» ¿Qué problema tiene?", "El 80 no aparece en ninguna tarjeta", ["Está demasiado corto", "Mezcla bus con bicicleta"], "Solo se pueden usar los datos de las tarjetas."),
    ],
    [
        mc(f"Tarjetas: {BIKE_A} {BIKE_B} Ordenas el afiche de arriba hacia abajo. ¿Qué orden es más lógico?", "Titular, tres imágenes con sus pies de foto y una invitación final", ["Una invitación, tres pies de foto sin imágenes y un titular", "Solo las imágenes sin palabras"], "Un afiche claro empieza con un titular y termina con una acción."),
        mc(f"Tarjetas: {PLNT_A} {PLNT_B} Escribe una sola oración que une las tres imágenes con los datos. ¿Cuál es correcta?", "A seed needs water and light, then it grows leaves and later makes flowers", ["A flower makes a seed with water and then it becomes a leaf and a tree", "A seed grows because it is very big and it makes smoke"], "Sigue el orden y los datos de la tarjeta B."),
    ],
    [mc(f"En una actividad de ciencias tienes {PLNT_A} y tu compañero tiene la parte con los datos. ¿Qué dices para pedir el primero?", "Can you read the first fact, please?", ["I have a picture of a bus", "Which country is it?"], "Pide el primer dato de su tarjeta.")],
    [
        mc("¿Qué haces si falta un dato en ambas tarjetas?", "Lo pregunto o escribo que no se sabe", ["Lo invento"], "No se inventa información."),
        mc("¿Qué frase pide que una persona lea su tarjeta?", "Can you read the first fact, please?", ["I have a picture of a bike."], "Es una petición educada."),
        ("Escribe en inglés la palabra que significa «afiche».", "Poster", "Poster es un cartel con imagen y texto."),
    ],
    task(f"Con tu compañero(a) o con una persona de tu casa, usen las tarjetas: {BIKE_A} {BIKE_B} {GBIKE} En tu hoja escribe: (1) un titular, (2) un pie de foto para cada imagen, (3) una invitación final (call to action).",
         "(1) Move your way! (2) Image 1: Bikes do not make smoke. Image 2: A bus carries many people. Image 3: Walking is free and healthy. (3) Choose how you go to school!",
         ["el titular es corto", "cada pie de foto usa un mensaje que corresponde a su imagen", "la invitación final pide una acción"],
         ["cinco líneas escritas en la hoja"],
         ["emparejar al revés", "agregar datos que no están en las tarjetas"],
         "Pide que dibuje el afiche con tres cuadros y compruebe que cada imagen tiene su pie."),
    "Copia las frases útiles del vocabulario y escribe su traducción debajo.",
    "Haz dos tarjetas de tres líneas sobre un tema de tu casa: una con imágenes y otra con mensajes, y pide a alguien que las una.",
)

# ============================================================ clase 5: producción independiente
DRAFT = "«Digital story draft (de ejemplo). Slide 1: Image: a river in the morning. Text: Our class visited the river. Slide 2: Image: students with gloves collecting plastic bottles. Text: We collected 48 bottles. Slide 3: Image: a bar chart with Group A: 20 and Group B: 28. Text: Group B collected more bottles than the other group. Slide 4: Image: a clean river bank. Text: Please keep our river clean!»"
GDRAFT = "(draft = borrador; gloves = guantes; collecting = recolectando; bank = orilla; keep = mantén)"
SPORT = "«Sports Day. Next Friday at 10:00 in the school yard. Races, tug of war and a relay.»"
GSPORT = "(sports day = día del deporte; races = carreras; tug of war = cuerda de tracción; relay = posta)"

lesson(
    OA, 5, MAT,
    "Aprenderé a revisar y crear por mi cuenta una historia o información con imágenes, pie de foto y datos. Sirve para que mis textos multimodales sean claros y atractivos.",
    ["Sé elegir recursos, escribir pies de foto, narrar en pasado y unir información de dos tarjetas."],
    [
        "Para crear un texto multimodal por tu cuenta, sigue cinco pasos. Uno: decide el mensaje, el propósito y la audiencia. Dos: elige un titular corto. Tres: escoge imágenes que muestren lo mismo que dicen las palabras. Cuatro: escribe pies de foto exactos, en pasado si cuentas lo que pasó y en presente si informas un dato. Cinco: revisa que los números coincidan con el gráfico.",
        "Cuando revises el trabajo de otra persona, usa tres preguntas. ¿Mensaje claro? ¿Cada imagen apoya una oración? ¿Hay algún dato sin evidencia? Si encuentras un error, escribe la corrección y explica por qué. Un buen borrador (draft) puede mejorar muchas veces.",
        "Para cerrar un texto que invita a actuar, usa una orden amable y corta: Please keep our river clean! Please recycle paper! Join us on Friday! Estas invitaciones (calls to action) funcionan mejor cuando son concretas y se relacionan con el mensaje.",
    ],
    [("draft", "borrador"), ("headline", "titular"), ("caption", "pie de foto"), ("evidence", "evidencia"), ("call to action", "invitación a actuar"), ("revise", "revisar y mejorar")],
    [
        ("Revisar una diapositiva", f"Borrador: {DRAFT} {GDRAFT} ¿La diapositiva 3 es coherente con su gráfico?",
         ["El gráfico muestra A: 20 y B: 28.", "El texto dice que el grupo B recolectó más.", "28 es mayor que 20, así que es coherente."], "Sí, es coherente: 28 es mayor que 20"),
        ("Comprobar un total", f"Borrador: {DRAFT} ¿Coincide el total de la diapositiva 2 con los grupos del gráfico?",
         ["La diapositiva 2 dice 48 botellas.", "El gráfico da 20 y 28.", "20 + 28 = 48, así que coincide."], "Sí: 20 + 28 = 48"),
    ],
    [
        ("Terminar la historia sin invitación ni mensaje claro.", "El lector no sabe qué hacer ni qué idea llevarse.", "Cierra con una invitación corta, concreta y relacionada con el mensaje."),
        ("Cambiar de tiempo verbal entre diapositivas sin motivo.", "Se mezcla pasado y presente.", "Si cuentas lo que pasó, usa pasado en todas las diapositivas."),
    ],
    [
        mc(f"Lee: {DRAFT} {GDRAFT} ¿Cuál es la invitación a actuar (call to action)?", "Please keep our river clean!", ["We collected 48 bottles", "Our class visited the river"], "Es la orden amable que pide hacer algo."),
        mc(f"Lee: {DRAFT} {GDRAFT} ¿Cuántas botellas recolectó el grupo B?", "28", ["20", "48"], "El gráfico de la diapositiva 3 dice Group B: 28."),
        mc(f"Lee: {DRAFT} {GDRAFT} ¿Qué diapositiva muestra el resultado final del trabajo?", "La 4, con la orilla limpia", ["La 1, con el río en la mañana", "La 2, con los guantes"], "Una orilla limpia es el resultado."),
    ],
    [
        mc(f"Lee: {DRAFT} {GDRAFT} ¿Qué titular conviene para toda la historia?", "A Clean River Starts With Us", ["A Soccer Match", "Plastic Is Cheap"], "Resume el mensaje: actuar para mantener limpio el río."),
        mc(f"Lee: {DRAFT} ¿Qué tiempo verbal se usa para contar las diapositivas 1 y 2?", "Pasado simple", ["Presente simple", "Futuro"], "Visited y collected están en pasado."),
        mc(f"Lee: {DRAFT} Un compañero cambia la diapositiva 3 a «Group A collected more bottles than Group B». ¿Es correcto?", "No, porque el gráfico dice que el grupo B recolectó 28 y el grupo A 20", ["Sí, porque A viene primero", "Sí, porque el total es 48"], "El texto debe seguir los datos del gráfico."),
    ],
    [
        mc(f"Revisa esta diapositiva nueva: «Image: a bar chart with Group A: 20 and Group B: 28. Text: We collected 60 bottles.» ¿Qué corriges?", "El total debe ser 48, no 60", ["El color del gráfico", "Las barras deben ser rojas"], "20 + 28 = 48."),
        mc(f"Lee: {DRAFT} Tu profesor pide agregar una diapositiva con una fecha exacta de la visita. ¿Qué haces?", "Preguntar la fecha, porque no aparece en el borrador", ["Inventar una fecha que suene bien", "Copiar la fecha de otro afiche"], "Los datos deben tener evidencia."),
        mc(f"Lee: {DRAFT} Quieres un pie de foto para la diapositiva 1 que coincida con la imagen. ¿Cuál eliges?", "A river in the morning, before the clean-up", ["A big soccer stadium at night", "A kitchen with plastic bottles"], "La imagen es un río en la mañana."),
    ],
    [
        mc("Un compañero escribe para una foto de estudiantes ordenando una biblioteca: «Students clean a beach.» ¿Cuál es el problema principal?", "El texto no coincide con la imagen", ["Falta un verbo", "No tiene titular"], "La imagen y las palabras deben decir lo mismo."),
        arith(f"Lee: {DRAFT} ¿Cuántas botellas más recolectó el grupo B que el grupo A?", "28-20", "Se resta lo del grupo A a lo del grupo B.", " botellas"),
    ],
    [
        mc(f"Lee: {DRAFT} Un lector dice que la diapositiva 4 podría ser un buen primer cuadro. ¿Qué respondes?", "No, porque muestra el resultado y la historia empieza con la visita al río", ["Sí, porque el final siempre va primero", "Sí, porque tiene signo de exclamación"], "El orden de una historia sigue la secuencia: visita, trabajo, gráfico y resultado."),
        mc("Tres mejoras posibles para un borrador de afiche: (1) agregar tres fuentes nuevas, (2) cambiar el titular por uno más corto, (3) añadir un párrafo de 100 palabras. ¿Cuál mejora más la claridad?", "Cambiar el titular por uno más corto", ["Agregar tres fuentes nuevas", "Añadir un párrafo de 100 palabras"], "Un titular corto se lee en pocos segundos."),
    ],
    [mc(f"Tienes que anunciar el día del deporte con estos datos: {SPORT} {GSPORT} ¿Qué titular y pie de foto escribes?", "Titular: Sports Day is coming! Pie de foto: Next Friday at 10:00 in the school yard", ["Titular: Sports Day was yesterday! Pie de foto: Next Monday at 8:00 in the gym", "Titular: Cooking Day! Pie de foto: Friday at midnight"], "Usa los datos de la tarjeta sin cambiarlos.")],
    [
        mc("¿Cuál es un buen cierre para una historia sobre reciclar?", "Please recycle paper!", ["Paper is made from trees"], "Es una invitación breve y concreta."),
        mc("Para revisar, debes preguntar si cada imagen", "apoya una oración", ["tiene muchos colores"], "La coherencia entre imagen y texto es la clave."),
        ("Escribe en inglés la palabra que significa «borrador».", "Draft", "Draft es la primera versión que se puede mejorar."),
    ],
    task(f"Crea en tu hoja un afiche con estos datos: {SPORT} {GSPORT} Escribe: (1) un titular, (2) tres pies de foto en inglés para tres imágenes (races, tug of war, relay), (3) una invitación final, (4) la audiencia a la que va dirigido.",
         "(1) Sports Day is coming! (2) Students run a race. Two teams pull the rope. Four friends pass the baton in a relay. (3) Join us next Friday at 10:00! (4) Estudiantes del colegio.",
         ["el titular es corto y llamativo", "cada pie de foto coincide con una imagen", "la invitación usa los datos del enunciado", "nombra la audiencia"],
         ["afiche con titular, tres imágenes y pies de foto, invitación y audiencia"],
         ["cambiar el día o la hora", "escribir pies de foto que no coinciden con las imágenes"],
         "Pide que muestre el afiche a una persona y que esta diga cuál es el mensaje."),
    "Copia las seis palabras del vocabulario y dibuja un ejemplo de titular, imagen y pie de foto.",
    "Crea un afiche para invitar a tu familia a ver una película en casa, con titular, imagen y pie de foto en inglés.",
)
