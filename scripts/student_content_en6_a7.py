"""Cuaderno del estudiante, 6.º básico Inglés (propuesta), EN06 OA 07 (estrategias de comprensión lectora antes, durante y después de leer).

Todos los textos están escritos en el enunciado y son originales; llevan pista en español.
Cada palabra o estructura nueva se explica antes de usarla. Sin audio externo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA7 = "EN06 OA 07"


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- clase 1: antes de leer (propósito, predicción, conocimientos previos)
OCTO = "«An octopus has eight arms and three hearts. It can change colour to hide from its enemies. It lives in the sea and eats crabs and fish.» (octopus = pulpo, arms = brazos, hearts = corazones, colour = color, hide = esconderse, enemies = enemigos, crabs = cangrejos)"
BIKE = "«Title: Bike Safety. Subtitle: Five rules for riding. Rule 1: Always wear a helmet. Rule 2: Stop at red lights. Rule 3: Use hand signals when you turn. Rule 4: Ride on the right side. Rule 5: Do not use your phone while riding.» (rules = reglas, helmet = casco, hand signals = señales con la mano, turn = doblar, ride = andar, while = mientras)"

lesson(
    OA7, 1,
    "Los títulos y textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé tres estrategias para antes de leer: leer con un propósito, hacer predicciones y usar lo que ya sé. Sirve para entrar a un texto en inglés con una idea clara y comprenderlo mejor.",
    ["Sé que el título dice de qué trata un texto.", "Conozco palabras como animals, sea y bike."],
    [
        "Antes de leer conviene prepararse. Primero, define tu propósito (purpose): ¿para qué voy a leer? Puede ser para saber un dato, para aprender un tema o para disfrutar. Segundo, haz una predicción (prediction): mira el título, el subtítulo y las imágenes y piensa de qué trata. Tercero, activa tus conocimientos previos (prior knowledge): ¿qué sé ya de este tema?",
        "Por ejemplo, el título «The Eight-Armed Hunter» y una imagen de un animal marino te hacen predecir que el texto habla de un pulpo. Con tus conocimientos previos, esperas palabras como sea, arms, fish o colour. Una predicción se expresa así: «I think the text is about... because...» (creo que el texto trata de... porque...).",
        "Una predicción puede estar equivocada, y está bien. Lo importante es comparar con el texto después de leer. El propósito también guía la lectura: si solo necesitas saber cuántas reglas hay, no necesitas entender cada palabra. Leer sin estas preguntas previas es como empezar un viaje sin saber a dónde ir.",
    ],
    [("purpose", "propósito: para qué leo"), ("prediction", "predicción: lo que creo que dirá"), ("prior knowledge", "conocimientos previos"), ("title / subtitle", "título / subtítulo"), ("I think... because...", "creo que... porque..."), ("topic", "tema")],
    [
        ("Predecir con el título", "Título: «The Eight-Armed Hunter». Imagen: un animal con ocho brazos nadando en el mar. ¿De qué crees que trata el texto: un pulpo o un caballo?", ["La imagen muestra ocho brazos en el mar.", "Un pulpo tiene ocho brazos.", "Predigo que habla de un pulpo."], "Un pulpo"),
        ("Definir el propósito", "Quieres saber cuántos brazos tiene un pulpo. ¿Qué propósito de lectura escribes: «encontrar un número» o «disfrutar un cuento»?", ["Lo que busco es un dato.", "Los datos numéricos se buscan en el texto.", "Mi propósito es encontrar un número."], "Encontrar un número"),
    ],
    [
        ("Empezar a leer sin mirar el título.", "Se pierde una pista importante.", "Lee primero el título, el subtítulo y las imágenes."),
        ("Pensar que una predicción incorrecta es un error grave.", "Se cree que debe ser siempre acertada.", "Una predicción se corrige al leer."),
    ],
    [
        ("Título: «Bike Safety». ¿Qué palabra esperas encontrar? a) helmet b) volcano c) cake", "a) helmet", "Un cartel de seguridad en bicicleta menciona el casco."),
        ("Subtítulo: «Five rules for riding». ¿Cuántas reglas esperas encontrar?", "5", "Five significa cinco."),
        ("Quieres saber si hay que detenerse en la luz roja. ¿Qué propósito de lectura es adecuado? a) buscar una regla específica b) leer toda la página sin objetivo", "a) buscar una regla específica", "Un propósito claro orienta lo que buscas."),
    ],
    [
        ("Lee: " + OCTO + " ¿Se confirma la predicción «habla de un pulpo»? Responde sí o no.", "Sí", "El texto empieza con An octopus."),
        ("Lee: " + OCTO + " ¿Qué dato sobre los corazones aparece?", "Tiene tres corazones", "Dice three hearts."),
        ("Lee: " + OCTO + " Antes de leer pensaste que el texto diría que el pulpo vive en el desierto. ¿Qué dice el texto?", "Que vive en el mar", "Dice it lives in the sea."),
    ],
    [
        ("Lee: " + BIKE + " Tu propósito es saber qué hay que usar en la cabeza. ¿Qué regla lo responde?", "La regla 1", "Dice Always wear a helmet."),
        ("Lee: " + BIKE + " ¿Qué hay que hacer en una luz roja?", "Detenerse", "Dice Stop at red lights."),
        ("Lee: " + BIKE + " ¿Qué no hay que hacer mientras se anda en bicicleta? a) usar el teléfono b) usar casco", "a) usar el teléfono", "Dice Do not use your phone while riding."),
    ],
    [
        ("Un compañero predijo que «Bike Safety» habla de comida y no cambió su idea después de leer. ¿Qué estrategia olvidó?", "Verificar la predicción con el texto", "Debía compararla con lo que dice."),
        ("Lee: " + OCTO + " ¿Cuál es el mejor propósito para leer este texto? a) aprender datos de un animal b) aprender a jugar fútbol", "a) aprender datos de un animal", "El texto da datos sobre el pulpo."),
    ],
    [
        ("Ordena los pasos antes de leer, como en la explicación. A) Pienso qué sé del tema. B) Defino mi propósito. C) Miro el título y las imágenes para predecir.", "B, C, A", "Primero decides para qué lees, luego observas el título y las imágenes y por último recuerdas lo que sabes."),
        ("Predice. Título: «A Night at the Museum Garden». Imagen: una niña con linterna y estatuas. ¿Qué palabra esperas: statue o submarine?", "statue", "Las estatuas aparecen en la imagen."),
    ],
    [("Vas a leer el horario de un bus con el título «Bus Schedule». Tu propósito es saber a qué hora sale el primero. ¿Qué buscarás en el texto? a) horas b) colores", "a) horas", "Un horario contiene horas.")],
    [
        ("¿Qué es un propósito de lectura?", "Para qué leo", "Orienta lo que busco."),
        ("¿Qué son los conocimientos previos?", "Lo que ya sé del tema", "Ayudan a predecir."),
        ("¿Qué haces con una predicción después de leer?", "La verifico", "Se compara con el texto."),
    ],
    task("Observa este título y subtítulo: «Volcano Explorers. Subtitle: How scientists study volcanoes.» Escribe tu propósito de lectura, una predicción con «I think the text is about... because...» y tres palabras que esperas leer. Después lee: «Scientists study volcanoes to know when they will erupt. They use special tools to measure the heat and the movement of the Earth.» (erupt = hacer erupción, tools = herramientas, measure = medir, heat = calor, movement = movimiento). Verifica tu predicción.", "Propósito: aprender cómo estudian los científicos los volcanes. I think the text is about scientists because of the title. Palabras: scientists, volcano, heat. Se confirmó.", ["escribe un propósito", "escribe una predicción con razón", "verifica con una palabra del texto"], ["hoja con propósito y predicción", "nota del adulto"], ["predicción sin razón", "no verificar con el texto"], "Reconoce el propósito claro y practica a justificar la predicción con una pista del título."),
    "Antes de leer un texto de otra asignatura, escribe tu propósito y una predicción en una frase.",
    "Elige tres títulos que se te ocurran y escribe una predicción para cada uno.",
)

# ---------------------------------------------------------------- clase 2: lectura rápida y lectura focalizada
CAMP = "«Green Valley Summer Camp. For children from 10 to 13 years old. Activities: swimming, hiking and painting. Dates: January 8 to January 19. Price: 85 thousand pesos for the whole camp. Office hours: 9 a.m. to 5 p.m. Call the office to register.» (camp = campamento, hiking = senderismo, whole = completo, office hours = horario de atención, register = inscribirse)"
SCHOOLAD = "«Welcome to Lakeview School! Our school has a large library, a science lab and a sports field. Students learn English, Math, Art and Music. Every Friday we have a reading club in the library. Parents' meetings are on the first Monday of each month.» (welcome = bienvenidos, large = grande, field = cancha, reading club = club de lectura, parents' meetings = reuniones de apoderados, each = cada)"

lesson(
    OA7, 2,
    "Los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a hacer una lectura rápida para captar la idea general y una lectura focalizada para encontrar datos específicos. Sirve para leer avisos y folletos en inglés sin perder tiempo.",
    ["Sé buscar números y nombres en un texto.", "Conozco palabras como camp, school y price."],
    [
        "La lectura rápida (skimming) consiste en pasar la vista por el texto, sin detenerse en cada palabra, para entender de qué trata. Miras el título, la primera oración y las palabras destacadas. Con ella puedes responder: ¿qué tipo de texto es? y ¿cuál es la idea general? Por ejemplo, el aviso de Green Valley es un folleto de un campamento de verano.",
        "La lectura focalizada (scanning) sirve para encontrar un dato específico: una hora, un precio, un nombre. Antes de leer, decide qué buscas, por ejemplo price o dates. Luego recorre el texto con la vista hasta encontrar esa palabra o un número, y lee solo esa parte con atención. No necesitas leer lo demás.",
        "Usa las dos en orden: primero skimming para saber de qué trata; después scanning para encontrar el dato que necesitas. Si la pregunta es «¿de qué trata?», usa lectura rápida. Si la pregunta es «¿cuánto cuesta?» o «¿a qué hora?», usa lectura focalizada. Elegir la estrategia correcta te ahorra tiempo y errores.",
    ],
    [("skimming", "lectura rápida para la idea general"), ("scanning", "lectura focalizada para un dato"), ("general idea", "idea general"), ("specific information", "información específica"), ("price", "precio"), ("dates", "fechas")],
    [
        ("Lectura rápida", "Lee en 10 segundos: «Lost! A small brown dog with a blue collar. His name is Toby. Please call 555-0123 if you see him.» (collar = collar, call = llamar). ¿De qué trata? Usa lectura rápida.", ["Miro la primera palabra: Lost!", "Veo dog y name.", "Es un aviso de un perro perdido."], "Un aviso de un perro perdido"),
        ("Lectura focalizada", "En el mismo aviso, ¿de qué color es el collar? Busca solo la palabra collar.", ["Escaneo hasta collar.", "Antes dice blue.", "El collar es azul."], "Azul"),
    ],
    [
        ("Leer palabra por palabra para encontrar un dato.", "Se pierde tiempo.", "Decide qué buscas y recorre con la vista solo hasta esa palabra o número."),
        ("Usar lectura rápida cuando la pregunta pide un dato exacto.", "No se identifica el tipo de pregunta.", "Si piden un dato, usa lectura focalizada."),
    ],
    [
        ("Lee: " + CAMP + " Con lectura rápida, ¿qué tipo de texto es? a) un folleto de campamento b) un cuento", "a) un folleto de campamento", "El título dice Summer Camp y da información."),
        ("Lee: " + CAMP + " Con lectura focalizada, ¿cuánto cuesta?", "85 mil pesos", "Dice 85 thousand pesos."),
        ("Lee: " + CAMP + " Con lectura focalizada, ¿qué edad tienen los niños del campamento? a) de 10 a 13 años b) de 6 a 8 años", "a) de 10 a 13 años", "Dice from 10 to 13 years old."),
    ],
    [
        ("Lee: " + CAMP + " ¿Qué actividades se mencionan? a) natación, senderismo y pintura b) fútbol y baile", "a) natación, senderismo y pintura", "Dice swimming, hiking and painting."),
        ("Lee: " + CAMP + " ¿Cuántas actividades se enumeran?", "3", "Son swimming, hiking y painting."),
        ("Lee: " + CAMP + " ¿Hasta qué hora atiende la oficina?", "Hasta las 5 de la tarde", "Dice 9 a.m. to 5 p.m."),
    ],
    [
        ("Lee: " + SCHOOLAD + " Con lectura rápida, ¿qué intenta hacer el texto? a) dar la bienvenida y presentar el colegio b) vender un producto", "a) dar la bienvenida y presentar el colegio", "Empieza con Welcome."),
        ("Lee: " + SCHOOLAD + " Con lectura focalizada, ¿qué día es el club de lectura?", "El viernes", "Dice Every Friday we have a reading club."),
        ("Lee: " + SCHOOLAD + " ¿Cuántas asignaturas se mencionan: English, Math, Art y Music?", "4", "Son cuatro nombres de asignaturas."),
    ],
    [
        ("Un compañero, para saber la fecha de las reuniones de apoderados, lee todo el texto lentamente. ¿Qué estrategia es más eficaz? a) lectura focalizada de la palabra meetings b) lectura rápida", "a) lectura focalizada de la palabra meetings", "Busca el dato específico."),
        ("Lee: " + CAMP + " Dos amigos de 9 y 12 años quieren inscribirse. ¿Cuál puede ir al campamento?", "El de 12 años", "El rango es de 10 a 13."),
    ],
    [
        ("Lee: " + CAMP + " Una niña de 13 años y un niño de 14 quieren inscribirse. ¿Quién puede ir?", "La niña de 13 años", "El rango del campamento llega hasta los 13 años."),
        ("Lee: " + SCHOOLAD + " ¿Cuándo son las reuniones de apoderados?", "El primer lunes de cada mes", "Dice on the first Monday of each month."),
    ],
    [("Lees un cartel en un museo: «Open Tuesday to Sunday, 10 a.m. to 6 p.m. Closed on Mondays. Children under six are free.» (free = gratis). Quieres saber si el museo abre los lunes. ¿Qué estrategia usas y cuál es el dato?", "Lectura focalizada; está cerrado los lunes", "Buscas Mondays y encuentras Closed.")],
    [
        ("¿Qué es la lectura rápida?", "Pasar la vista para captar la idea general", "No se leen todas las palabras."),
        ("¿Qué estrategia usas para encontrar un precio?", "Lectura focalizada", "Se busca un dato concreto."),
        ("¿Qué miras primero en la lectura rápida?", "El título y la primera oración", "Dan la idea general."),
    ],
    task("Lee este aviso: «Library News. New books! The library has twenty new English books. Open from Monday to Friday, 8 a.m. to 4 p.m. Children can borrow two books for one week. Silent reading club on Wednesdays at 2 p.m.» (borrow = pedir prestado, silent = silencioso). Primero escribe de qué trata con lectura rápida. Luego escribe cuatro datos con lectura focalizada: cuántos libros nuevos, horario, cuántos libros se pueden pedir y cuándo es el club.", "Trata de novedades de la biblioteca. 20 libros nuevos; de lunes a viernes de 8 a 16; se pueden pedir 2 libros por una semana; el club es los miércoles a las 14:00.", ["escribe la idea general", "anota los cuatro datos con precisión", "diferencia las dos lecturas"], ["hoja con respuestas", "nota del adulto"], ["confundir la hora del club con la de apertura", "olvidar el límite de libros"], "Reconoce los datos bien ubicados y repasa cómo buscar una palabra clave con la vista."),
    "Mira el folleto de un supermercado o un horario de tu casa y encuentra el dato que pide una persona de tu casa sin leer todo.",
    "Escribe dos preguntas de lectura rápida y dos de lectura focalizada sobre el aviso del campamento.",
)

# ---------------------------------------------------------------- clase 3: visualizar y elementos organizacionales
DESERT = "«Title: Life in the Desert. Subtitle: How animals and plants live without much water. Heading 1: The Heat. The desert is very hot in the day and cold at night. Heading 2: The Plants. A cactus stores water in its thick stem. Its spines protect it from animals. [Picture caption: A cactus stores water.] Heading 3: The Animals. Camels can walk for days without drinking water. Many small animals sleep in the day and look for food at night.» (desert = desierto, cactus, stem = tallo, spines = espinas, camels = camellos, look for = buscan)"

lesson(
    OA7, 3,
    "Los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a visualizar lo que leo y a usar los elementos organizacionales del texto: título, subtítulo, encabezados e imágenes. Sirve para entender cómo está organizado un texto y recordar lo que dice.",
    ["Sé que un texto informativo tiene título.", "Conozco palabras como hot, cold y water."],
    [
        "Visualizar (visualize) es formar imágenes en tu mente mientras lees. Si lees «The camel walks slowly across the hot sand», imaginas un camello, arena y calor. Visualizar te ayuda a comprender y a recordar. Después puedes dibujar lo que imaginaste y comprobar si coincide con el texto.",
        "Los elementos organizacionales (text features) muestran cómo está ordenado un texto. El título (title) dice el tema. El subtítulo (subtitle) lo precisa. Los encabezados (headings) separan partes. Las imágenes (pictures) y sus leyendas (captions) ilustran. Las palabras en negrita destacan términos importantes. Al reconocerlos, puedes predecir qué dice cada parte antes de leerla.",
        "Por ejemplo, en «Life in the Desert», el encabezado The Plants anuncia información sobre plantas y la leyenda A cactus stores water apoya esa información. Usa estos elementos como un mapa: miras el título, recorres los encabezados y decides qué parte leer con más detalle según tu propósito.",
    ],
    [("visualize", "formar imágenes mentales"), ("title / subtitle", "título / subtítulo"), ("heading", "encabezado"), ("caption", "leyenda de una imagen"), ("text feature", "elemento organizacional"), ("bold", "negrita")],
    [
        ("Usar un encabezado", "Lee: «Heading: The Animals. Camels can walk for days without drinking water.» ¿Sobre qué trata esta parte?", ["El encabezado dice The Animals.", "La oración habla de camellos.", "Trata de los animales."], "De los animales"),
        ("Visualizar", "Lee: «The cactus has thick green stems and many spines.» (spines = espinas). ¿Qué imagen se forma: una planta con espinas o un pez?", ["Leo cactus, stems y spines.", "Imagino una planta verde con espinas.", "El pez no coincide."], "Una planta con espinas"),
    ],
    [
        ("Saltarse los encabezados.", "Se pierde la organización del texto.", "Léelos primero para saber qué parte tiene cada información."),
        ("Imaginar algo que el texto no dice.", "Se agregan detalles que no están en el texto.", "Visualiza solo lo que el texto describe."),
    ],
    [
        ("Lee: " + DESERT + " ¿Cuál es el título? a) Life in the Desert b) The Heat", "a) Life in the Desert", "Es la primera línea del texto."),
        ("Lee: " + DESERT + " ¿Cuántos encabezados tiene el texto?", "3", "Son The Heat, The Plants y The Animals."),
        ("Lee: " + DESERT + " ¿Qué dice la leyenda de la imagen? a) A cactus stores water. b) Camels sleep.", "a) A cactus stores water.", "Aparece entre corchetes bajo la imagen."),
    ],
    [
        ("Lee: " + DESERT + " ¿Bajo qué encabezado buscarías información sobre los cactus?", "The Plants", "Los cactus son plantas."),
        ("Lee: " + DESERT + " ¿Cómo es el desierto de día y de noche?", "Muy caliente de día y frío de noche", "Dice very hot in the day and cold at night."),
        ("Lee: " + DESERT + " ¿Para qué sirven las espinas del cactus? a) para protegerlo de los animales b) para guardar agua", "a) para protegerlo de los animales", "Dice its spines protect it from animals."),
    ],
    [
        ("Lee: " + DESERT + " ¿Qué almacena el cactus en su tallo grueso? a) agua b) arena", "a) agua", "Dice stores water in its thick stem."),
        ("Lee: " + DESERT + " ¿Qué hacen muchos animales pequeños de día?", "Duermen", "Dice they sleep in the day."),
        ("Lee: " + DESERT + " Quieres saber cómo viven los camellos. ¿Qué encabezado lees primero?", "The Animals", "Los camellos son animales."),
    ],
    [
        ("Lee el texto: «A big orange sun is going down behind a hill. A small boat sails slowly on a calm lake.» (hill = cerro, sails = navega, calm = tranquilo). ¿Qué imagen mental es correcta? a) atardecer con un bote en un lago b) una tormenta en el mar", "a) atardecer con un bote en un lago", "Calm y going down indican tranquilidad."),
        ("Un compañero visualizó que en el desierto hay un río grande. ¿Qué dice el texto del agua?", "Que hay poca agua; los animales y las plantas viven sin mucha agua", "El subtítulo dice without much water."),
    ],
    [
        ("Dibuja un esquema con: Título, Subtítulo, 3 encabezados. ¿Cuántas casillas necesitas en total?", "5", "Una por el título, una por el subtítulo y tres encabezados.", "1+1+3"),
        ("Si el título es «The Animals of the Sea», ¿qué encabezado sería más coherente? a) Whales and Dolphins b) How to Make Bread", "a) Whales and Dolphins", "Es coherente con el tema del título."),
    ],
    [("En la caja de un juego lees: «Title: Space Race. Heading: How to play. Heading: Rules.» Quieres saber cómo se juega. ¿Qué encabezado lees? a) How to play b) Rules", "a) How to play", "Ese encabezado explica cómo se juega.")],
    [
        ("¿Qué es visualizar?", "Formar imágenes mentales del texto", "Ayuda a comprender."),
        ("¿Qué indica un encabezado?", "De qué trata una parte del texto", "Organiza el contenido."),
        ("¿Qué es una leyenda (caption)?", "El texto que explica una imagen", "Acompaña a la imagen."),
    ],
    task("Lee: «Title: Bees at Work. Subtitle: How a hive works. Heading 1: The Queen. The queen lays eggs. Heading 2: The Workers. Worker bees collect nectar and make honey. [Picture caption: Worker bees at the hive.] Heading 3: The Winter. Bees stay inside the hive to keep warm.» (hive = colmena, queen = reina, nectar = néctar, warm = calientes). Dibuja un esquema con el título, el subtítulo y los tres encabezados, y escribe una palabra clave bajo cada uno. Luego dibuja lo que visualizas para la parte The Workers.", "Título: Bees at Work. Subtítulo: How a hive works. Queen: lays eggs. Workers: nectar y honey. Winter: inside, warm. Dibujo: abejas obreras en la colmena.", ["anota título, subtítulo y tres encabezados", "una palabra clave por encabezado", "dibujo coherente con el texto"], ["hoja con esquema y dibujo", "nota del adulto"], ["confundir encabezado con leyenda", "dibujar algo que no dice el texto"], "Reconoce el esquema ordenado y revisa con la persona que el dibujo solo use datos del texto."),
    "Busca en un libro de tu casa un título, un subtítulo y una imagen con leyenda y anótalos.",
    "Escribe un título, un subtítulo y dos encabezados para un texto sobre tu mascota o un animal que te guste.",
)

# ---------------------------------------------------------------- clase 4: después de leer (confirmar predicciones y releer)
BOX = "«On Monday, the class finds a box in the school garden. The students do not know who left it. Inside there are ten new books and a note: For the school library. The students are surprised and happy. Mrs. Silva smiles and says: I think I know who it was, but it is a secret.» (box = caja, garden = jardín, note = nota, surprised = sorprendidos, secret = secreto, I think I know = creo que sé)"

lesson(
    OA7, 4,
    "Los cuentos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a confirmar mis predicciones y a releer para aclarar dudas después de leer. Sirve para comprobar si entendí bien y corregir mis ideas.",
    ["Sé hacer una predicción antes de leer.", "Conozco palabras como box, books y note."],
    [
        "Después de leer (post-reading), lo primero es confirmar tus predicciones (confirm predictions). Compara lo que pensabas con lo que dice el texto. Si coincide, tu predicción se confirma. Si no coincide, la corriges. Por ejemplo, si predijiste que la caja tenía juguetes y el texto dice que tenía books, la predicción no se confirma.",
        "La segunda estrategia es releer (reread). Cuando tienes una duda, vuelve al texto, busca la oración exacta y léela con calma. Releer no es un fracaso: es lo que hacen los buenos lectores. Para responder una pregunta, busca la respuesta en el texto y fíjate en las palabras clave de la pregunta.",
        "Para decir si algo es verdad, falso o no se sabe, comprueba en el texto. Si el texto lo dice, es verdadero. Si el texto dice lo contrario, es falso. Si el texto no lo menciona, no se sabe. Por ejemplo, el texto no dice quién dejó la caja: Mrs. Silva guarda el secreto. Entonces «Mrs. Silva left the box» no se sabe.",
    ],
    [("confirm", "confirmar"), ("reread", "releer"), ("true / false / not stated", "verdadero / falso / no se dice"), ("prediction", "predicción"), ("note", "nota"), ("secret", "secreto")],
    [
        ("Confirmar una predicción", "Predijiste que la caja tenía juguetes. Lee: «Inside the box there are ten new books.» ¿Se confirma tu predicción?", ["Mi idea: juguetes.", "El texto dice books.", "No se confirma; la corrijo: tenía libros."], "No, la caja tenía libros"),
        ("Releer para responder", "Lee: «Rosa has two cats and one rabbit. She feeds them every morning.» (feeds = alimenta). ¿Cuántos animales tiene en total?", ["Releo los números: two y one.", "Sumo 2 + 1.", "Son 3 animales."], "3 animales"),
    ],
    [
        ("Decir «verdadero» porque parece lógico, aunque el texto no lo diga.", "Se confunde lo que se supone con lo que dice el texto.", "Si el texto no lo menciona, la respuesta es no se dice."),
        ("No releer y adivinar la respuesta.", "Se confía solo en la memoria.", "Vuelve al texto y busca la oración."),
    ],
    [
        ("Lee: " + BOX + " ¿Dónde encuentran la caja? a) en el jardín del colegio b) en la biblioteca", "a) en el jardín del colegio", "Dice in the school garden."),
        ("Lee: " + BOX + " ¿Cuántos libros hay en la caja?", "10", "Dice ten new books."),
        ("Lee: " + BOX + " ¿Qué dice la nota? a) For the school library b) Happy birthday", "a) For the school library", "Se lee dentro de la caja."),
    ],
    [
        ("Lee: " + BOX + " Predijiste que los estudiantes estarían tristes. ¿Se confirma? Responde sí o no.", "No", "Dice the students are surprised and happy."),
        ("Lee: " + BOX + " «Mrs. Silva left the box.» ¿Es verdadero, falso o no se dice?", "No se dice", "Ella solo dice que cree saber quién fue."),
        ("Lee: " + BOX + " «The box was in the school garden.» ¿Verdadero, falso o no se dice?", "Verdadero", "Está en la primera oración."),
    ],
    [
        ("Lee: " + BOX + " «The class found the box on Friday.» ¿Verdadero, falso o no se dice?", "Falso", "Dice On Monday."),
        ("Lee: " + BOX + " «The students know who left the box.» ¿Verdadero, falso o no se dice?", "Falso", "Dice the students do not know who left it."),
        ("Lee: " + BOX + " Para responder cuántos libros hay, ¿qué palabras de la pregunta buscas al releer? a) how many b) secret", "a) how many", "Indican que se busca un número."),
    ],
    [
        ("Un compañero predijo que el texto era un poema. Después de leer, ¿se confirma? Responde sí o no.", "No", "Es un cuento con personajes y problema."),
        ("Lee: " + BOX + " ¿Cuál es el sentimiento de los estudiantes al ver los libros? a) sorpresa y alegría b) enojo", "a) sorpresa y alegría", "Dice surprised and happy."),
    ],
    [
        ("Ordena los pasos después de leer. A) Releo para aclarar. B) Confirmo mi predicción. C) Respondo con evidencia.", "B, A, C", "Primero comparas, luego relees y al final respondes con el texto."),
        ("Lee: " + BOX + " ¿Qué evidencia del texto muestra para quién eran los libros?", "La nota que dice For the school library", "La nota indica el destino de los libros."),
    ],
    [("Lees una noticia: «The town park opens on Saturday. There will be games and music.» (opens = abre). Predijiste que abriría el domingo. ¿Se confirma?", "No, abre el sábado", "El texto dice Saturday.")],
    [
        ("¿Qué haces con una predicción después de leer?", "La confirmo o la corrijo", "Se compara con el texto."),
        ("¿Qué significa «reread»?", "Releer", "Volver a leer el texto."),
        ("Si el texto no menciona algo, ¿qué respondes?", "No se dice", "No se puede afirmar."),
    ],
    task("Lee: «On Friday, Tomás takes a mystery package to school. It is wrapped in blue paper and has a ribbon. Everyone wants to know what is inside. At lunch, Tomás opens it. Inside there is a small plant for the class garden.» (package = paquete, wrapped = envuelto, ribbon = cinta, plant = planta). Antes de leer, el título era «The Mystery Package»: escribe qué predijiste. Después escribe si se confirmó, una pista del texto y una afirmación verdadera, una falsa y una que no se diga.", "Predicción: dentro hay un regalo. Se confirmó en parte: era una planta. Pista: Inside there is a small plant. Verdadera: viene en papel azul. Falsa: lo abre el lunes. No se dice: quién lo regaló.", ["escribe una predicción", "verifica con una pista", "clasifica tres afirmaciones"], ["hoja con respuestas", "nota del adulto"], ["marcar como verdadero lo que no se dice", "no releer"], "Reconoce la verificación hecha con evidencia y repasa cómo se decide si algo se dice o no."),
    "Relee el cuento de la caja de libros y encuentra las dos frases que muestran sorpresa.",
    "Escribe tres afirmaciones sobre un cuento que conozcas: una verdadera, una falsa y una que no se diga.",
)

# ---------------------------------------------------------------- clase 5: recontar con apoyo y preguntar para confirmar
MITTEN = "«In winter, Lila finds a red mitten in the snow. She looks around, but nobody is there. She hangs the mitten on a fence. The next day, a small boy takes it and runs home with a big smile.» (mitten = guante, snow = nieve, looks around = mira alrededor, hangs = cuelga, fence = reja, takes = toma)"

lesson(
    OA7, 5,
    "Los cuentos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a recontar un texto con apoyo de palabras clave y a hacer preguntas para confirmar la información. Sirve para comprobar que comprendiste y para dudar de forma ordenada.",
    ["Sé usar first, then y finally.", "Conozco palabras como snow, boy y smile."],
    [
        "Recontar (retell) es contar con tus propias palabras lo que leíste. Para hacerlo con apoyo, escribe cuatro palabras clave en orden: por ejemplo, Lila, mitten, fence, boy. Con ellas puedes decir: «First, Lila finds a mitten. Then she hangs it on a fence. Finally, a boy takes it». No hace falta recordar cada palabra.",
        "También puedes apoyarte en un dibujo con cuatro cuadros. Cada cuadro muestra un hecho. Así recontarás en el orden correcto. Un buen recuento incluye los personajes, el lugar, lo que pasa y cómo termina, pero no copia el texto. Si puedes recontar, es señal de que lo comprendiste.",
        "Para confirmar información, haz preguntas: «Who found the mitten?», «Where did she put it?», «Is it true that the boy was angry?». Luego vuelve al texto y comprueba. Si el texto no lo dice, tu pregunta queda sin respuesta, y eso también es información útil. Preguntar te ayuda a no suponer cosas que no están escritas.",
    ],
    [("retell", "recontar"), ("keyword", "palabra clave"), ("question", "pregunta"), ("first, then, finally", "primero, luego, finalmente"), ("is it true that...?", "¿es verdad que...?"), ("in your own words", "con tus propias palabras")],
    [
        ("Elegir palabras clave", "Lee: «Pedro buys a ticket. He enters the cinema and sits down. He watches a funny film and laughs.» (ticket = entrada, enters = entra, funny = divertida, laughs = se ríe). ¿Cuáles son cuatro palabras clave en orden para recontar?", ["Busco las acciones principales.", "Compra, entra, ve la película, se ríe.", "Elijo ticket, cinema, film, laughs."], "ticket, cinema, film, laughs"),
        ("Hacer una pregunta para confirmar", "Después de leer el texto de Pedro, quieres confirmar si estaba solo. ¿Qué haces? a) busco en el texto si lo dice b) invento una respuesta", "a) busco en el texto si lo dice", "Se confirma con el texto, no con suposiciones."),
    ],
    [
        ("Recontar copiando todas las oraciones.", "No se usan las propias palabras.", "Usa cuatro palabras clave y cuéntalo con tus palabras."),
        ("Responder una pregunta con algo que el texto no dice.", "Se suponen datos.", "Si el texto no lo dice, responde que no se dice."),
    ],
    [
        ("Lee: " + MITTEN + " ¿Qué encuentra Lila? a) un guante rojo b) un gorro azul", "a) un guante rojo", "Dice a red mitten."),
        ("Lee: " + MITTEN + " ¿Dónde lo cuelga?", "En una reja", "Dice she hangs the mitten on a fence."),
        ("Lee: " + MITTEN + " ¿Quién toma el guante al día siguiente? a) un niño pequeño b) una profesora", "a) un niño pequeño", "Dice a small boy takes it."),
    ],
    [
        ("Lee: " + MITTEN + " ¿Cuáles son cuatro palabras clave en orden? a) Lila, mitten, fence, boy b) boy, fence, Lila, snow", "a) Lila, mitten, fence, boy", "Siguen el orden en que ocurren los hechos."),
        ("Lee: " + MITTEN + " ¿Cómo termina el cuento?", "El niño se lleva el guante y corre a casa sonriendo", "Dice runs home with a big smile."),
        ("Lee: " + MITTEN + " ¿En qué estación ocurre? a) en invierno b) en verano", "a) en invierno", "Dice in winter."),
    ],
    [
        ("Lee: " + MITTEN + " Para confirmar, haces la pregunta: «Was Lila alone?». ¿Qué dice el texto? a) nobody is there b) her friend is there", "a) nobody is there", "Cuando mira alrededor, no hay nadie."),
        ("Lee: " + MITTEN + " Preguntas: «What color was the mitten?». ¿Cuál es la respuesta?", "Roja", "Dice red mitten."),
        ("Lee: " + MITTEN + " Preguntas: «How old was the boy?». ¿Qué respondes?", "No se dice", "El texto solo dice small boy, no su edad."),
    ],
    [
        ("Un compañero recontó: «Lila lost her mitten and the boy found it». ¿Qué corrige el texto?", "Lila encontró el guante, no lo perdió", "Dice Lila finds a red mitten."),
        ("Ordena el recuento. A) the boy takes the mitten B) Lila finds a mitten C) she hangs it on a fence", "B, C, A", "Sigue la secuencia del cuento."),
    ],
    [
        ("El recuento «First, Lila finds a mitten. Then she hangs it on a fence. Finally, a boy takes it» cuenta tres hechos. ¿Cuántas palabras de orden usa?", "3", "Usa first, then y finally."),
        ("Elige la mejor pregunta para confirmar quién tomó el guante. a) Who took the mitten? b) Where is the snow?", "a) Who took the mitten?", "Who pregunta por una persona."),
    ],
    [("Alguien te cuenta: «Yesterday I saw a dog in the park. It had a blue ball.» Quieres confirmar de qué color era la pelota. ¿Qué preguntas? a) What colour was the ball? b) Why is the park big?", "a) What colour was the ball?", "La pregunta se enfoca en el dato que quieres confirmar.")],
    [
        ("¿Qué es recontar?", "Contar con tus palabras lo que leíste", "Se hace en orden."),
        ("¿Qué respondes si el texto no dice algo?", "No se dice", "No se debe suponer."),
        ("¿Qué te ayuda a recontar en orden?", "Palabras clave o dibujos", "Marcan los hechos."),
    ],
    task("Lee: «On Saturday, Ema goes to the market with her neighbour. She buys three tomatoes, two apples and a bunch of parsley. On the way home, she meets a friend and gives him one apple. At home, she makes a salad.» (market = feria, neighbour = vecina, bunch = atado, parsley = perejil, meets = encuentra, gives = da, salad = ensalada). Escribe cuatro palabras clave en orden, haz un recuento en tres frases con First, Then y Finally y escribe una pregunta que confirme algo del texto.", "Palabras: market, buys, friend, salad. First, Ema goes to the market and buys tomatoes, apples and parsley. Then she gives an apple to a friend. Finally, she makes a salad. Pregunta: How many tomatoes does she buy?", ["escribe cuatro palabras clave en orden", "recuenta en tres frases con las palabras de orden", "escribe una pregunta con respuesta en el texto"], ["hoja con respuestas", "nota del adulto"], ["copiar el texto", "olvidar que regaló una manzana"], "Reconoce el recuento en orden y practica a responder la pregunta con una oración del texto."),
    "Cuenta a una persona de tu casa el cuento del guante usando solo cuatro palabras clave.",
    "Recuenta con First, Then y Finally algo que hiciste hoy en inglés o español.",
)
