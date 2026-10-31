"""Cuaderno del estudiante, 7.º básico Inglés (propuesta), EN07 OA 06 (estrategias de lectura con propósito).

Todos los textos son originales y están escritos en el enunciado, con pista en español. Los datos de ejemplo se rotulan como tales.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_en7_a import lesson

OA6 = "EN07 OA 06"

# ---------------------------------------------------------------- clase 1: antes de leer
BAKER = "Portada del texto. Título: «A Day in the Life of a Baker». Subtítulo: «Bread begins at four in the morning». Imagen: panes dorados sobre una mesa de madera. (baker = panadero, bread = pan, golden = dorado)"
BAKERTEXT = "«At four in the morning, the baker gets to the bakery. First, he mixes flour, water, salt and yeast. Then he leaves the dough to rest for an hour. At six, the first loaves go into the oven. By seven, the smell of fresh bread fills the street.» (gets to = llega a, flour = harina, salt = sal, yeast = levadura, dough = masa, rest = reposar, loaves = panes, oven = horno, smell = olor)"
ROBOT = "Portada del texto. Título: «Robots in Our Schools». Subtítulo: «Helping students learn». Imagen: un robot pequeño junto a dos estudiantes que miran una pantalla. (robots = robots, learn = aprender, screen = pantalla)"

lesson(
    OA6, 1,
    "Las portadas de textos y los fragmentos escritos en cada ejercicio y lápiz.",
    "Aprenderé tres estrategias para antes de leer: leer con un propósito, hacer predicciones y usar mis conocimientos previos. Sirve para entender mejor un texto desde el inicio y no perderme al leer en inglés.",
    ["Sé reconocer un título y un subtítulo.", "Conozco palabras como bread, robot y school."],
    [
        "Antes de leer, prepárate (pre-reading). Primero fija un propósito (purpose): ¿para qué leo? Puedo leer para informarme, para encontrar un dato o para disfrutar. El propósito decide cómo lees. Si buscas un horario, no necesitas leer todo; si quieres entender un proceso, lees completo y con calma.",
        "Segundo, haz predicciones (predictions) con el título (title), el subtítulo (subtitle) y la imagen (image). Pregúntate: ¿de qué trata?, ¿qué palabras aparecerán? Por ejemplo, con «A Day in the Life of a Baker» y una imagen de panes, puedes predecir palabras como oven, flour y morning. Una predicción es una idea probable, no una certeza: después se confirma o se corrige.",
        "Tercero, activa tus conocimientos previos (prior knowledge): lo que ya sabes del tema. Si sabes cómo se hace el pan, comprenderás las palabras desconocidas por el contexto. Escribe una frase: «I know that… / I want to learn…» (Sé que… / Quiero aprender…). Estas tres estrategias toman un minuto y mejoran mucho la comprensión.",
    ],
    [("purpose", "propósito: para qué leo"), ("prediction", "predicción: lo que creo que dirá"), ("prior knowledge", "conocimientos previos"), ("title / subtitle", "título / subtítulo"), ("image", "imagen"), ("I know that…", "Sé que…")],
    [
        ("Predecir con portada", BAKER + " ¿Qué palabras puedes predecir? a) oven, flour, morning b) teacher, desk, homework", ["Miro el título: baker.", "La imagen muestra panes.", "Las palabras de la opción a se relacionan con hacer pan."], "a) oven, flour, morning"),
        ("Propósito de lectura", "Quieres saber a qué hora empieza a trabajar el panadero. ¿Cuál es tu propósito de lectura?", ["Mi propósito es un dato específico.", "Busco una hora.", "No necesito leer todo con detalle."], "Encontrar a qué hora empieza a trabajar"),
    ],
    [
        ("Empezar a leer sin mirar el título.", "Se pierde el contexto.", "Lee primero el título, el subtítulo y la imagen."),
        ("Tomar una predicción como si fuera segura.", "No se compara con el texto.", "Confirma o corrige tu predicción al leer."),
    ],
    [
        (ROBOT + " ¿De qué crees que trata el texto? a) de robots que ayudan en el colegio b) de una receta de pan", "a) de robots que ayudan en el colegio", "El título y la imagen muestran robots y estudiantes."),
        (BAKER + " ¿Qué imagen apoya el tema? a) panes sobre una mesa b) un estadio", "a) panes sobre una mesa", "La imagen se relaciona con el panadero."),
        ("Quieres saber el precio de un libro en una librería virtual. ¿Cuál es tu propósito? a) buscar un dato específico b) disfrutar un cuento", "a) buscar un dato específico", "El precio es un dato concreto."),
    ],
    [
        (ROBOT + " ¿Qué predicción es más probable? a) El texto explica cómo un robot ayuda a aprender b) El texto cuenta la historia de un chef", "a) El texto explica cómo un robot ayuda a aprender", "Helping students learn apoya esa idea."),
        (BAKERTEXT + " ¿A qué hora llega el panadero a la panadería?", "A las cuatro de la mañana", "Dice at four in the morning."),
        (BAKERTEXT + " ¿Qué ocurre a las seis? a) los primeros panes entran al horno b) llega la harina", "a) los primeros panes entran al horno", "Dice At six, the first loaves go into the oven."),
    ],
    [
        (BAKER + " Predijiste «oven». Lee: " + BAKERTEXT + " ¿Se confirma la predicción? Responde sí o no.", "Sí", "El texto dice the first loaves go into the oven."),
        (BAKER + " Predijiste «sugar». Lee: " + BAKERTEXT + " ¿Se confirma? Responde sí o no.", "No", "Los ingredientes son flour, water, salt y yeast."),
        (BAKER + " Si tu propósito es conocer el orden de los pasos, ¿qué palabras debes buscar? a) first y then b) oven y bread", "a) first y then", "Marcan la secuencia de pasos."),
    ],
    [
        ("Un compañero dice que no sirve predecir porque se puede equivocar. ¿Qué respuesta es mejor? a) Predecir prepara la lectura y se puede corregir b) Es mejor no pensar antes de leer", "a) Predecir prepara la lectura y se puede corregir", "Una predicción orienta y puede cambiar."),
        (BAKER + " Sabes que el pan se hornea. ¿Qué conocimiento previo te ayuda a entender la palabra «oven»? a) que el pan se cocina en un lugar caliente b) que el pan es redondo", "a) que el pan se cocina en un lugar caliente", "Con ese conocimiento deduces que oven es el horno."),
    ],
    [
        ("Ordena la estrategia. A) Leer el texto. B) Fijar un propósito. C) Hacer predicciones con el título y la imagen.", "B, C, A", "Primero el propósito, luego la predicción y finalmente la lectura."),
        (BAKERTEXT + " Si el panadero llega a las 4:00 y los primeros panes entran al horno a las 6:00, ¿cuántas horas pasan?", "2", "De 4:00 a 6:00 pasan dos horas.", "6-4"),
    ],
    [("Antes de leer una noticia con el título «New Bridge Opens in the City», dices: «I know that bridges help people cross rivers». ¿Qué estrategia usas? a) conocimientos previos b) releer", "a) conocimientos previos", "Dices lo que ya sabes del tema.")],
    [
        ("Antes de leer, ¿qué es el reading purpose?", "Para qué leo", "Decide cómo lees el texto."),
        ("¿Con qué elementos haces una predicción?", "Título, subtítulo e imagen", "Dan pistas del tema."),
        ("¿Cómo se dice «Sé que…» en inglés?", "I know that…", "Es una frase para mostrar lo que ya sabes."),
    ],
    task("Mira esta portada: Título: «Our Class Garden». Subtítulo: «From seeds to flowers». Imagen: unas manos de niños plantando una semilla en una maceta. (garden = jardín, seeds = semillas, flowers = flores). Antes de leer, escribe: tu propósito (por ejemplo, saber cómo se planta), dos palabras que predices y una frase «I know that…» con lo que ya sabes de las plantas.", "Propósito: saber cómo se planta una semilla. Palabras: water y soil. I know that plants need water.", ["escribe un propósito claro", "anota dos predicciones relacionadas con la portada", "escribe una frase I know that… coherente"], ["hoja con respuestas"], ["predecir palabras sin relación con la portada", "escribir el propósito como una predicción"], "Reconoce lo que acertó y relee con la persona el título y la imagen para mejorar las predicciones."),
    "Mira la portada de «Robots in Our Schools» y escribe tres palabras que esperas leer.",
    "Escribe un título de texto y su subtítulo para un tema que te interese, y predice cinco palabras.",
)

# ---------------------------------------------------------------- clase 2: lectura rápida y focalizada
WINTER = "«Winter in the South. In the south of Chile, it rains on most winter days. The temperature is low, and the wind is strong near the coast. Forests stay green all year, and rivers are full of water. Many families wear wool clothes, and they enjoy warm soup. Some tourists visit in winter to see the quiet lakes and the mountains with snow.» (south = sur, temperature = temperatura, wind = viento, coast = costa, wool = lana, soup = sopa, quiet = tranquilos, lakes = lagos, snow = nieve)"
TIMETABLE = "Horario de buses de ejemplo: «Route 12 to the center. Weekdays: 6:15, 7:00, 8:30, 12:00, 17:45, 21:10. Saturdays: 8:00, 12:00, 18:00. Sundays: no service. Ticket: 700 pesos. Students: 350 pesos.» (route = recorrido, weekdays = días de semana, no service = sin servicio, ticket = pasaje)"
SPORT = "«Swimming is a sport for the whole body. Swimmers use their arms and legs, and they control their breathing. There are four main styles: freestyle, backstroke, breaststroke and butterfly. A pool for races is fifty meters long, and swimmers swim one length at a time. Many students start to swim when they are six years old.» (whole body = cuerpo completo, arms = brazos, legs = piernas, breathing = respiración, styles = estilos, length = largo)"

lesson(
    OA6, 2,
    "Los textos y horarios escritos en cada ejercicio y lápiz.",
    "Aprenderé dos formas de leer: la lectura rápida (skimming), para captar la idea general, y la lectura focalizada (scanning), para encontrar un dato exacto. Sirve para ahorrar tiempo cuando leo en inglés.",
    ["Sé fijar un propósito de lectura.", "Conozco palabras como bus, rain y swim."],
    [
        "La lectura rápida (skimming) sirve para saber de qué trata un texto sin leer cada palabra. Mira el título, la primera y la última oración, y las palabras que se repiten. Por ejemplo, en un texto sobre el invierno en el sur, ves rain, cold, wind, snow y entiendes que describe el clima. Skimming responde: ¿de qué trata?",
        "La lectura focalizada (scanning) sirve para encontrar un dato específico, como un número, una hora o un nombre. Tus ojos recorren el texto buscando solo esa palabra o cifra, sin leer todo. Por ejemplo, si buscas el pasaje de estudiante en un horario, recorres hasta ver la palabra students y el número 350. Scanning responde: ¿dónde está este dato?",
        "Elige la estrategia según el propósito. Si quieres saber de qué trata, haz skimming. Si quieres un dato, haz scanning. Después de encontrar la información, lee esa parte con cuidado para estar seguro. Los números, los nombres propios y las palabras en negrita son las mejores pistas para encontrar datos rápido.",
    ],
    [("skimming", "lectura rápida: idea general"), ("scanning", "lectura focalizada: dato específico"), ("main idea", "idea general"), ("specific information", "información específica"), ("key word", "palabra clave"), ("purpose", "propósito")],
    [
        ("Skimming", "Lee rápido: «Penguins are birds that cannot fly. They swim very well. Many penguins live in cold places. They eat fish and small sea animals.» (penguins = pingüinos, fly = volar). ¿De qué trata el texto?", ["Leo la primera oración y las palabras que se repiten.", "Penguins aparece al inicio.", "Todo describe a los pingüinos."], "De los pingüinos"),
        ("Scanning", "Busca el dato: «Library hours: Monday to Friday, 8:00 to 16:00. Saturday, 9:00 to 12:00. Sunday closed.» (closed = cerrada). ¿A qué hora cierra el sábado?", ["Recorro buscando Saturday.", "Después aparece 9:00 to 12:00.", "Cierra a las 12:00."], "A las 12:00"),
    ],
    [
        ("Leer todo el texto con detalle para responder una sola hora.", "Se pierde tiempo cuando basta con scanning.", "Busca la palabra clave y el número."),
        ("Usar solo scanning para entender la idea general.", "Se pierde el sentido global.", "Primero haz skimming para saber de qué trata."),
    ],
    [
        ("Lee: " + WINTER + " Haz skimming. ¿De qué trata el texto? a) del invierno en el sur de Chile b) del verano en el norte de Chile", "a) del invierno en el sur de Chile", "Winter, rain y wind se repiten."),
        ("Lee: " + TIMETABLE + " Haz scanning. ¿Cuánto cuesta el pasaje de un estudiante, en pesos? a) 350 b) 700", "a) 350", "Dice Students: 350 pesos."),
        ("Lee: " + SPORT + " Haz skimming. ¿Cuál es la idea general? a) la natación es un deporte para todo el cuerpo b) las piscinas son profundas", "a) la natación es un deporte para todo el cuerpo", "La primera oración presenta la idea."),
    ],
    [
        ("Lee: " + WINTER + " ¿Qué usan muchas familias? a) ropa de lana b) bloqueador solar", "a) ropa de lana", "Dice many families wear wool clothes."),
        ("Lee: " + TIMETABLE + " ¿Hay servicio los domingos? Responde sí o no.", "No", "Dice Sundays: no service."),
        ("Lee: " + SPORT + " ¿Cuántos estilos principales hay?", "Cuatro", "Dice four main styles."),
    ],
    [
        ("Lee: " + TIMETABLE + " Haz scanning. ¿A qué hora sale el último bus de un día de semana?", "A las 21:10", "Es la última hora de la lista de weekdays."),
        ("Lee: " + TIMETABLE + " ¿Cuántos buses hay los sábados?", "3", "Son 8:00, 12:00 y 18:00."),
        ("Lee: " + SPORT + " Haz scanning. ¿Cuántos metros mide la piscina de la carrera?", "50", "Dice a pool of fifty meters."),
    ],
    [
        ("Lee: " + TIMETABLE + " Dos estudiantes viajan un día de semana. ¿Cuánto pagan en total, en pesos?", "$700", "Cada estudiante paga trescientos cincuenta pesos.", "2*350"),
        ("Lee: " + SPORT + " ¿Por qué se llama «cuerpo completo» al deporte? a) porque se usan brazos y piernas b) porque dura todo el día", "a) porque se usan brazos y piernas", "Dice swimmers use their arms and legs."),
    ],
    [
        ("Lee: " + SPORT + " Una carrera de 200 metros se nada en esa piscina. ¿Cuántos largos hay que nadar? Usa el dato del texto.", "4", "Cada largo mide 50 metros y 200 entre 50 da cuatro largos.", "200//50"),
        ("Lee: " + TIMETABLE + " Quieres tomar el bus de las 12:00 un sábado. ¿Qué estrategia usas: skimming o scanning? Responde con una palabra.", "scanning", "Buscas una hora específica."),
    ],
    [("Quieres saber si la biblioteca abre el domingo. El aviso dice: «Open Monday to Saturday. Closed on Sundays.» Haces scanning. ¿Qué palabra buscas? a) Sundays b) Monday", "a) Sundays", "La palabra clave es el día que preguntas.")],
    [
        ("¿Qué es skimming?", "Leer rápido para captar la idea general", "Se mira el título y las ideas principales."),
        ("¿Para qué sirve el scanning?", "Para encontrar un dato exacto", "Se buscan palabras o números."),
        ("¿Qué pistas ayudan a encontrar datos rápido?", "Números, nombres y palabras clave", "Destacan en el texto."),
    ],
    task("Lee este texto original: «The School Fair. The school fair is on October 25. It begins at 10:00 and finishes at 15:00. There are three stands: food, games and books. Tickets cost 500 pesos. Students from Grade 7 sell the food. The fair is always fun, and families enjoy it.» (fair = feria, stands = puestos, grade = curso, sell = vender, families = familias). Primero haz skimming y escribe de qué trata. Luego haz scanning y anota la fecha, la hora de inicio, el precio y cuántos puestos hay.", "Trata de la feria del colegio. Fecha: 25 de octubre. Inicio: 10:00. Precio: 500 pesos. Puestos: 3.", ["escribe la idea general con skimming", "anota los cuatro datos con scanning", "no inventa datos"], ["hoja con respuestas"], ["anotar la hora de término en lugar de la de inicio", "decir que hay dos puestos"], "Reconoce lo que acertó y repasa con la persona qué datos buscó con el dedo."),
    "Relee el texto del invierno y haz una lista de seis palabras clave sobre el clima.",
    "Escribe una pregunta para cada texto que se pueda responder con scanning.",
)

# ---------------------------------------------------------------- clase 3: elementos del texto y visualizar
SOLAR = "Artículo de ejemplo. Título: «Solar Panels on Our School Roof». Subtítulo: «Clean energy for the whole school». Imagen 1 (pie de foto): «Workers place the panels on the roof.» Imagen 2 (pie de foto): «The screen shows how much energy the panels make.» Encabezado 1: «Why solar?». Texto: «The sun gives free energy. Solar panels change sunlight into electricity.» Encabezado 2: «How does it work?». Texto: «The panels are on the roof. A cable carries the electricity to the school. A screen in the hall shows the numbers.» (panels = paneles, roof = techo, cable = cable, electricity = electricidad, hall = pasillo)"
ZOO = "Página web de ejemplo. Título: «Visit the City Zoo». Subtítulo: «A day with animals». Imagen: una jirafa que come hojas. Pie de foto: «Our giraffe eats leaves from tall trees.» Encabezado: «Opening hours». Texto: «Open every day from 9:00 to 17:00.» Encabezado: «Rules». Texto: «Do not feed the animals.» (giraffe = jirafa, leaves = hojas, feed = alimentar)"
RIVER = "«The river begins in the mountains. At first, it is a thin stream of cold water. The stream goes down between big gray rocks. Later, many small streams join, and the river becomes wide and slow. At the end, the river reaches the sea.» (thin = delgado, stream = arroyo, rocks = rocas, join = se unen, wide = ancho, reaches = llega a)"

lesson(
    OA6, 3,
    "Los artículos y páginas web escritos en cada ejercicio y lápiz.",
    "Aprenderé a usar los elementos organizacionales de un texto (título, subtítulo, imágenes con pie de foto y encabezados) y a visualizar lo que leo. Sirve para entender cómo está organizado un artículo y para imaginarme la información.",
    ["Sé distinguir título y subtítulo.", "Conozco palabras como roof, sun y river."],
    [
        "Los textos tienen elementos organizacionales (organizational elements) que muestran cómo está ordenada la información. El título (title) dice el tema general. El subtítulo (subtitle) lo precisa. Los encabezados (headings) abren secciones, por ejemplo «Why solar?» o «Rules». Las imágenes (images) acompañan al texto y su pie de foto (caption) explica qué se ve. Antes de leer, recorre estos elementos para anticipar el contenido.",
        "Cada elemento aporta información distinta. El título y el subtítulo responden «¿de qué trata?». Los encabezados te permiten ir directo a la sección que necesitas. El pie de foto confirma lo que se dice en el texto: «Workers place the panels on the roof» (Trabajadores ponen los paneles en el techo). Si un pie de foto dice algo que no está en el texto principal, también es información.",
        "Visualizar (visualize) significa crear una imagen mental de lo que lees. Si lees «The river begins in the mountains… a thin stream of cold water… between big gray rocks», puedes imaginar un arroyo delgado que baja por rocas grises. Cuando visualizas, fijas detalles como tamaño, color y lugar, y recuerdas mejor el texto. Puedes incluso dibujar lo que imaginas.",
    ],
    [("organizational elements", "elementos que organizan el texto"), ("heading", "encabezado de una sección"), ("caption", "pie de foto"), ("image", "imagen"), ("visualize", "imaginar lo que se lee"), ("section", "sección")],
    [
        ("Reconocer un elemento", "En «Visit the City Zoo — A day with animals», ¿cuál es el título y cuál el subtítulo?", ["El título nombra el tema general.", "El subtítulo lo precisa.", "El título es Visit the City Zoo."], "Título: Visit the City Zoo. Subtítulo: A day with animals"),
        ("Visualizar", "Lee: «A red kite flies above a green hill.» (kite = volantín, hill = cerro). ¿Qué dibujarías?", ["Imagino un volantín rojo en el cielo.", "Debajo hay un cerro verde.", "Dibujo ambos con sus colores."], "Un volantín rojo sobre un cerro verde"),
    ],
    [
        ("Saltarse el pie de foto porque «no es parte del texto».", "Se pierde información.", "Lee el pie de foto: explica la imagen."),
        ("Pensar que los encabezados son parte de la historia.", "Se confunde una sección con una oración.", "Los encabezados organizan: úsalos para ubicarte."),
    ],
    [
        ("Lee: " + SOLAR + " ¿Cuál es el título? a) Solar Panels on Our School Roof b) Clean energy for the whole school", "a) Solar Panels on Our School Roof", "El otro es el subtítulo."),
        ("Lee: " + ZOO + " ¿Qué muestra la imagen? a) una jirafa que come hojas b) un león durmiendo", "a) una jirafa que come hojas", "El pie de foto lo confirma."),
        ("Lee: " + SOLAR + " ¿Cuántos encabezados hay? a) dos b) cuatro", "a) dos", "Son Why solar? y How does it work?"),
    ],
    [
        ("Lee: " + SOLAR + " ¿Qué muestra la segunda imagen?", "La pantalla que indica la energía que producen los paneles", "El pie de foto lo explica."),
        ("Lee: " + ZOO + " ¿Qué encabezado debes ir a leer para saber el horario?", "Opening hours", "Esa sección tiene el horario."),
        ("Lee: " + RIVER + " ¿Cómo es el arroyo al comienzo? a) delgado y de agua fría b) ancho y lento", "a) delgado y de agua fría", "Dice a thin stream of cold water."),
    ],
    [
        ("Lee: " + SOLAR + " Debajo de «How does it work?», ¿por dónde pasa la electricidad hasta el colegio?", "Por un cable", "Dice a cable carries the electricity."),
        ("Lee: " + ZOO + " ¿Qué regla hay en la sección «Rules»? a) no alimentar a los animales b) no usar celular", "a) no alimentar a los animales", "Dice Do not feed the animals."),
        ("Lee: " + RIVER + " Visualiza. ¿Qué color tienen las rocas? a) grises b) blancas", "a) grises", "Dice big gray rocks."),
    ],
    [
        ("Lee: " + RIVER + " ¿Cuál es la mejor imagen mental del final del río? a) un río ancho y lento que llega al mar b) un arroyo veloz en la montaña", "a) un río ancho y lento que llega al mar", "Dice the river becomes wide and slow and reaches the sea."),
        ("Lee: " + SOLAR + " ¿Qué pie de foto muestra cómo se mide la energía que se produce? a) The screen shows how much energy the panels make b) Workers place the panels on the roof", "a) The screen shows how much energy the panels make", "Muestra qué energía producen los paneles."),
    ],
    [
        ("Lee: " + RIVER + " Ordena las etapas que visualizas. A) El río llega al mar. B) Un arroyo delgado baja por las rocas. C) Muchos arroyos se unen.", "B, C, A", "Del nacimiento en las montañas hasta el mar."),
        ("Lee: " + ZOO + " El zoológico abre de 9:00 a 17:00. ¿Cuántas horas está abierto?", "8", "De 9:00 a 17:00 pasan ocho horas.", "17-9"),
    ],
    [("Lee: «Title: Healthy Breakfast. Subtitle: Start the day with energy. Image: a bowl of fruit and a glass of milk. Caption: Fruit and milk give vitamins and calcium.» (bowl = bol, vitamins = vitaminas, calcium = calcio). ¿Qué puedes predecir antes de leer? a) que explicará qué comer en el desayuno b) que hablará de un viaje al zoológico", "a) que explicará qué comer en el desayuno", "El título, el subtítulo y la imagen hablan de desayuno.")],
    [
        ("¿Qué explica un pie de foto?", "Lo que se ve en la imagen", "Aclara la imagen."),
        ("¿Qué hace un encabezado?", "Abre una sección", "Organiza el texto."),
        ("En una lectura en inglés, ¿qué significa visualize?", "Imaginar lo que se lee", "Crea una imagen mental."),
    ],
    task("Mira este artículo de ejemplo. Título: «Recycling Bins». Subtítulo: «Three colors for a cleaner school». Imagen: tres tarros: azul, amarillo y verde. Pie de foto: «Blue is for paper, yellow for plastic and green for glass.» Encabezado: «Why recycle?» Texto: «Recycling saves energy and reduces waste.» (recycling = reciclaje, energy = energía, reduces = reduce, waste = basura). Escribe: el título, el subtítulo, qué muestra la imagen, el encabezado y un dibujo o una descripción de lo que imaginas.", "Título: Recycling Bins. Subtítulo: Three colors for a cleaner school. Imagen: tres tarros azul, amarillo y verde. Encabezado: Why recycle? Imagino un patio con tres tarros de colores y niños que botan papel, plástico y vidrio.", ["identifica título, subtítulo y encabezado", "describe la imagen con el pie de foto", "visualiza con detalles del texto"], ["hoja con respuestas"], ["confundir título y subtítulo", "inventar colores que no aparecen"], "Reconoce lo que acertó y relee con la persona el pie de foto para completar la descripción de la imagen."),
    "Relee el texto del río y dibuja tres escenas: montaña, valle y mar.",
    "Elige un artículo de una revista o de un sitio web y anota su título, su subtítulo y sus encabezados.",
)

# ---------------------------------------------------------------- clase 4: después de leer
PAPER = "«How paper is recycled. First, old paper is collected. Next, it is mixed with water to make a soft pulp. Then the pulp is cleaned and spread on a screen. Finally, it dries and becomes new paper.» (recycled = reciclado, collected = recolectado, pulp = pulpa, spread = esparcida, screen = malla, dries = se seca)"
SWIM = "«Swimming and running are both good exercise. Swimming is done in water, in a pool or in the sea. Running is done on land, for example in a park. Swimmers use their arms a lot. Runners use their legs a lot. Both sports help the heart.» (exercise = ejercicio, land = tierra, heart = corazón, a lot = mucho)"
SEEDS = "«Seeds travel in different ways. Some seeds, like dandelion seeds, fly with the wind. Other seeds float on water, like coconuts. Some seeds stick to animal fur, and others are eaten by birds. In this way, plants can grow in new places.» (travel = viajan, dandelion = diente de león, float = flotan, coconuts = cocos, stick = se pegan, fur = pelaje, eaten = comidas)"

lesson(
    OA6, 4,
    "Los textos y esquemas escritos en cada ejercicio y lápiz.",
    "Aprenderé estrategias para después de leer: confirmar mis predicciones y usar organizadores gráficos como la secuencia, la comparación y la tabla K-W-L. Sirve para comprobar que entendí y para ordenar la información.",
    ["Sé hacer predicciones antes de leer.", "Conozco palabras como paper, seed y wind."],
    [
        "Después de leer (post-reading), vuelve a tus predicciones (predictions). Si el texto dice lo mismo, se confirma. Si dice algo distinto, se corrige. Anota una palabra o frase del texto que lo pruebe. Así aprendes que no pasa nada si te equivocaste: la corrección enseña.",
        "Un organizador gráfico (graphic organizer) ordena la información. La tabla de secuencia (sequence chart) coloca pasos en orden con first, next, then y finally. El diagrama de Venn compara dos cosas: en el centro van las semejanzas y en los lados las diferencias. La tabla K-W-L tiene tres columnas: Know (lo que sé), Want (lo que quiero saber) y Learned (lo que aprendí). Cada organizador sirve para un tipo de texto.",
        "Elige el organizador según el texto. Un proceso (como el reciclaje del papel) pide una secuencia. Dos temas parecidos (nadar y correr) piden una comparación. Un tema nuevo pide K-W-L. Al completar el organizador, usa palabras clave y no oraciones completas: tres a cinco palabras por casilla bastan.",
    ],
    [("confirm / correct", "confirmar / corregir una predicción"), ("graphic organizer", "organizador gráfico"), ("sequence chart", "tabla de secuencia"), ("Venn diagram", "diagrama de Venn: comparar"), ("K-W-L", "Know, Want, Learned: lo que sé, quiero saber y aprendí"), ("both", "ambos")],
    [
        ("Elegir el organizador", "Vas a leer sobre las semejanzas y diferencias entre gatos y perros. ¿Qué organizador usas: secuencia o diagrama de Venn?", ["Hay dos cosas por comparar.", "Venn muestra semejanzas y diferencias.", "La secuencia sirve para pasos."], "Un diagrama de Venn"),
        ("Confirmar una predicción", "Predicción: «El texto sobre semillas habla de aviones.» El texto dice que las semillas viajan con el viento, el agua o los animales. ¿Qué resultado corresponde?", ["Busco aviones en el texto.", "No aparece.", "La predicción se corrige."], "Se corrige: el texto no habla de aviones"),
    ],
    [
        ("Completar el organizador con oraciones largas.", "No se resumen las ideas.", "Escribe tres a cinco palabras clave por casilla."),
        ("Usar un diagrama de Venn para ordenar pasos.", "No se elige el organizador adecuado.", "Los pasos van en una secuencia."),
    ],
    [
        ("Lee: " + PAPER + " ¿Qué organizador conviene? a) una secuencia b) un diagrama de Venn", "a) una secuencia", "Explica un proceso en pasos."),
        ("Lee: " + SWIM + " ¿Qué organizador conviene? a) un diagrama de Venn b) una secuencia", "a) un diagrama de Venn", "Compara natación y correr."),
        ("Lee: " + SEEDS + " Predijiste que las semillas viajan solo por el viento. ¿Resultado? a) corregida: viajan de varias formas b) confirmada", "a) corregida: viajan de varias formas", "Dice seeds travel in different ways."),
    ],
    [
        ("Lee: " + PAPER + " Completa la secuencia: 1. Se recolecta el papel viejo. 2. Se mezcla con ___. ¿Qué falta?", "Agua", "Dice it is mixed with water."),
        ("Lee: " + SWIM + " En el Venn, ¿qué va en el centro, donde se unen ambos deportes? a) ambos ayudan al corazón b) se hace en el agua", "a) ambos ayudan al corazón", "Dice both sports help the heart."),
        ("Lee: " + SEEDS + " ¿Qué semillas flotan en el agua? a) los cocos b) las de diente de león", "a) los cocos", "Dice float on water, like coconuts."),
    ],
    [
        ("Lee: " + PAPER + " ¿Cuál es el último paso de la secuencia?", "Se seca y se convierte en papel nuevo", "Dice finally, it dries and becomes new paper."),
        ("Lee: " + SWIM + " ¿Qué va solo en el lado de «Swimming»? a) se hace en el agua b) se hace en un parque", "a) se hace en el agua", "Correr es el que ocurre en tierra."),
        ("Lee: " + SEEDS + " ¿Qué dos formas de viaje de las semillas incluye el texto además del viento? a) agua y animales b) lluvia y sol", "a) agua y animales", "También nombra aves, que las comen."),
    ],
    [
        ("Lee: " + SEEDS + " Completa una tabla K-W-L. Columna Learned: ¿qué se aprendió? a) las semillas viajan con el viento, el agua y los animales b) las plantas no necesitan agua", "a) las semillas viajan con el viento, el agua y los animales", "Es lo que el texto enseña."),
        ("Lee: " + PAPER + " Un compañero ordenó: secar, mezclar, recolectar. ¿Está bien? Responde sí o no.", "No", "El orden correcto es recolectar, mezclar y secar."),
    ],
    [
        ("Lee: " + SWIM + " ¿Cuántas semejanzas expresa el texto con la palabra both?", "2", "Dice both good exercise y both sports help the heart."),
        ("Lee: " + PAPER + " Un compañero completó K-W-L. Want: «How does old paper become new paper?». ¿Qué respuesta de Learned responde su duda? a) se mezcla con agua, se limpia la pulpa y se seca b) se corta en trozos pequeños y se guarda en cajas", "a) se mezcla con agua, se limpia la pulpa y se seca", "Es la secuencia que describe el texto."),
    ],
    [("Lee: «Tomorrow I will read about volcanoes. I know that they are mountains. I want to learn how they erupt.» (volcanoes = volcanes, erupt = hacen erupción). ¿Qué parte de la tabla K-W-L corresponde a «I want to learn how they erupt»? a) Want b) Know", "a) Want", "Es lo que quiere saber.")],
    [
        ("¿Qué organizador sirve para comparar dos cosas?", "El diagrama de Venn", "Muestra semejanzas y diferencias."),
        ("¿Qué significa K-W-L?", "Know, Want, Learned", "Lo que sé, quiero saber y aprendí."),
        ("¿Qué haces con una predicción que el texto contradice?", "La corriges", "Anotas la frase que lo prueba."),
    ],
    task("Lee este texto original: «Bats and birds can both fly. Birds have feathers and lay eggs. Bats have fur and have babies that drink milk. Most birds fly during the day, and most bats fly at night.» (bats = murciélagos, feathers = plumas, lay = ponen, fur = pelaje). Haz un diagrama de Venn: pon una semejanza en el centro y dos diferencias en cada lado.", "Centro: ambos pueden volar. Aves: tienen plumas, ponen huevos. Murciélagos: tienen pelaje, sus crías toman leche.", ["escribe la semejanza correcta", "anota dos diferencias de cada animal", "usa palabras clave del texto"], ["diagrama dibujado"], ["poner una diferencia en el centro", "decir que ambos vuelan de día"], "Reconoce lo que acertó y relee con la persona las palabras both y but para ubicar semejanzas y diferencias."),
    "Relee el texto de las semillas y haz una tabla K-W-L con una frase en cada columna.",
    "Haz una secuencia de cinco pasos de una rutina de tu día con first, next, then y finally.",
)

# ---------------------------------------------------------------- clase 5: releer, recontar y preguntar
CAT = "«The Library Cat. In the school library, there was a gray cat called Pepa. She slept on the warm shelf near the window. One day, a student lost a library book. Pepa saw the book under a chair and pushed it with her paw. The librarian found it, smiled and gave Pepa a tasty treat. After that, the students called her the Library Detective.» (library = biblioteca, gray = gris, shelf = estante, window = ventana, lost = perdió, pushed = empujó, paw = pata, librarian = bibliotecaria, treat = premio, detective = detective)"
STAR = "«Stars look small because they are very far away. The Sun is also a star, but it is much closer to us. Because of that, it looks big and bright. A star can shine for millions of years. At night, we see stars only if the sky is clear.» (stars = estrellas, far away = lejos, closer = más cerca, bright = brillante, shine = brillar, millions = millones, clear = despejado)"
BUS2 = "«Mr. Torres drives the school bus. He wakes up at five o'clock and checks the engine. Then he drives to six different neighborhoods. He picks up forty students every morning. In the afternoon, he takes them home. He likes his job because he meets happy children.» (drives = conduce, wakes up = se despierta, engine = motor, neighborhoods = barrios, picks up = recoge, job = trabajo, meets = conoce)"

lesson(
    OA6, 5,
    "Los textos y las listas de palabras clave escritos en cada ejercicio y lápiz.",
    "Aprenderé a releer para aclarar dudas, a recontar un texto con apoyo de palabras clave y a hacer preguntas para confirmar información. Sirve para comprobar si de verdad entendí lo que leí.",
    ["Sé usar organizadores gráficos.", "Conozco preguntas con who, what, where y did."],
    [
        "Releer (reread) es volver a leer una parte del texto cuando algo no quedó claro. No es un fracaso: los buenos lectores releen. Primero identifica qué no entendiste, luego busca esa parte y léela más despacio. Muchas veces el contexto de las oraciones vecinas aclara una palabra desconocida.",
        "Recontar (retell) es decir con tus palabras lo que leíste. Para recontar con apoyo, usa una lista de palabras clave o un organizador: quién, dónde, qué pasó primero, qué pasó después y cómo terminó. Un buen recuento sigue el orden del texto, incluye los datos principales y no copia oraciones enteras. Puedes empezar con «First…, then…, finally…».",
        "Para confirmar información, haz preguntas: Did Pepa find the book? (¿Pepa encontró el libro?), Who found it? (¿quién lo encontró?), Where was the book? (¿dónde estaba?). Contesta mirando el texto. Con las preguntas descubres lo que no recuerdas y vuelves a leer solo esa parte. Así lees con propósito y comprendes mejor.",
    ],
    [("reread", "releer"), ("retell", "recontar con tus palabras"), ("key words", "palabras clave"), ("question", "pregunta"), ("confirm", "confirmar"), ("detail", "detalle")],
    [
        ("Releer para aclarar", "Lees: «The librarian found the book under a chair.» No sabes qué significa librarian. ¿Qué haces? Elige: releer las oraciones vecinas o saltar el texto.", ["Busco pistas en el contexto.", "La palabra aparece con book y library.", "Releer ayuda."], "Releer las oraciones vecinas para encontrar pistas"),
        ("Recontar con apoyo", "Palabras clave: dog – park – ball – friend. Lees: «A dog ran in the park. It found a ball. A boy became its friend.» ¿Cómo recuentas con esas palabras?", ["Uso las palabras en orden.", "Primero el perro y el parque.", "Luego la pelota y el amigo."], "Un perro corrió por el parque, encontró una pelota y un niño se hizo su amigo"),
    ],
    [
        ("Recontar copiando el texto palabra por palabra.", "No se usan palabras propias.", "Usa palabras clave y tu propia frase."),
        ("No releer cuando hay una duda importante.", "La duda se acumula.", "Relee solo la parte que no entendiste."),
    ],
    [
        ("Lee: " + CAT + " ¿Cómo se llama la gata? a) Pepa b) Perla", "a) Pepa", "Dice a gray cat called Pepa."),
        ("Lee: " + STAR + " ¿Por qué las estrellas se ven pequeñas? a) porque están muy lejos b) porque son chicas", "a) porque están muy lejos", "Dice because they are very far away."),
        ("Lee: " + BUS2 + " ¿A qué hora se despierta el Sr. Torres? a) a las cinco b) a las ocho", "a) a las cinco", "Dice he wakes up at five o'clock."),
    ],
    [
        ("Lee: " + CAT + " Responde la pregunta «Where was the book?»", "Debajo de una silla", "Dice Pepa saw the book under a chair."),
        ("Lee: " + STAR + " Responde «Is the Sun a star?»", "Sí", "Dice the Sun is also a star."),
        ("Lee: " + BUS2 + " Responde «How many students does he pick up?»", "Cuarenta", "Dice he picks up forty students."),
    ],
    [
        ("Lee: " + CAT + " Elige las palabras clave para recontar. a) cat, book, chair, librarian b) window, shelf, warm, small", "a) cat, book, chair, librarian", "Resumen quién, qué y dónde."),
        ("Lee: " + STAR + " ¿Cuál es la pregunta correcta para confirmar que el Sol se ve grande? a) «Why does the Sun look big?» b) «Where is the Sun?»", "a) Why does the Sun look big?", "El texto explica la razón: está más cerca."),
        ("Lee: " + BUS2 + " Elige la pregunta que confirma el motivo del Sr. Torres. a) «Why does he like his job?» b) «What time does he sleep?»", "a) Why does he like his job?", "El texto responde: porque conoce niños felices."),
    ],
    [
        ("Lee: " + BUS2 + " Un compañero dice que el Sr. Torres recoge 60 estudiantes. ¿Qué haces? a) releer la parte de picks up y corregir a 40 b) aceptar el dato", "a) releer la parte de picks up y corregir a 40", "El texto dice forty."),
        ("Escribe en inglés la pregunta con Did para comprobar este dato: «Pepa pushed the book». Elige: a) «Did Pepa push the book?» b) «Did Pepa pushed the book?»", "a) Did Pepa push the book?", "Después de did el verbo va en forma base."),
    ],
    [
        ("Lee: " + CAT + " Ordena el recuento. A) La bibliotecaria le da un premio. B) Un estudiante pierde un libro. C) Pepa lo encuentra y lo empuja. D) La llaman la Detective de la Biblioteca.", "B, C, A, D", "Sigue el orden de los hechos."),
        ("Lee: " + BUS2 + " Si recoge 40 estudiantes cada mañana, ¿cuántos recoge en 5 mañanas?", "200", "Se multiplican los estudiantes de una mañana por cinco.", "40*5"),
    ],
    [("Lee: «Last Saturday, Julia baked a cake. It was big, so she shared it with three friends. Everyone ate a slice.» (baked = horneó, shared = compartió, slice = trozo). Te preguntas: «Did Julia eat alone?». Releyendo, ¿cuál es la respuesta? a) No, compartió con tres amigos b) Sí, comió sola", "a) No, compartió con tres amigos", "Dice she shared it with three friends.")],
    [
        ("¿Para qué sirve releer?", "Para aclarar dudas", "Se vuelve a leer la parte confusa."),
        ("Después de leer, ¿qué es retell?", "Decir con tus palabras lo que leíste", "Se usan palabras clave."),
        ("¿Qué pregunta confirma si ocurrió algo en el pasado?", "Did…?", "Se usa did más el verbo base."),
    ],
    task("Lee este texto original: «The Lost Glove. On a cold morning, Marta found a blue glove on the bus stop bench. She looked for the owner, but nobody was there. So she tied the glove to the bus stop sign with a ribbon. In the afternoon, a boy came and said: It is mine! Thank you!» (glove = guante, bench = banca, owner = dueño, tied = amarró, ribbon = cinta). Escribe: cuatro palabras clave, un recuento de tres frases con first, then y finally, y una pregunta con Did para confirmar un dato.", "Palabras: Marta, glove, bench, boy. Recuento: First, Marta found a blue glove on the bench. Then she tied it to the sign. Finally, a boy came and took it. Pregunta: Did Marta find the glove on the bench?", ["elige palabras clave del texto", "recuenta en orden con first, then y finally", "formula una pregunta con Did correcta"], ["hoja con respuestas"], ["escribir «Did Marta found»", "cambiar el color del guante"], "Reconoce lo que acertó y relee con la persona las palabras clave para ordenar el recuento."),
    "Relee el texto de la gata y recuéntalo en voz alta a una persona de tu casa.",
    "Escribe tres preguntas con who, where y why sobre el texto de las estrellas.",
)
