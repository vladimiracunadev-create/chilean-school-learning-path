"""Cuaderno del estudiante, 7.º básico Inglés (oficial), IN07 OA 04 (estrategias para comprender textos escuchados:
predecir, escuchar con un propósito, palabras clave, apoyos visuales y gestuales, preguntar, confirmar y resumir).
Las imágenes se describen con palabras dentro de cada enunciado; el adulto lee los guiones.
"""
from __future__ import annotations

from student_content_in7_a import ADULT, arith, lesson, task

OA4 = "IN07 OA 04"
MAT = "Un adulto lee en voz alta cada texto escrito en los ejercicios; una hoja para tapar el guion y lápiz."

BLACKOUT = "Título: «The Night the Lights Went Out». Guion: «Last night, there was a storm. Suddenly, all the lights went out. We found a flashlight and played a card game in the living room. When the lights came back, we were all laughing.» (storm = tormenta, suddenly = de pronto, lights = luces, flashlight = linterna, living room = living, laughing = riéndonos)"
BIKELOCK = "Título: «How to Keep Your Bike Safe». Guion: «First, always use a strong lock. Second, park your bike in a bright place with other bikes. Third, write down the serial number of your bike, because the police can use it if the bike is lost.» (lock = candado, park = estacionar, bright = iluminado, serial number = número de serie, police = policía, lost = perdida)"
CORRIDOR = "«It's a busy morning in the school corridor. Students run to their classes, lockers close with a bang, and a teacher says: Walk, please! The bell rings, and soon the corridor is empty and quiet.» (corridor = pasillo, lockers = casilleros, bang = golpe, bell = timbre, empty = vacío, quiet = silencioso)"
FARM = "«My uncle has a small farm in the south. He has twenty cows and fifty chickens. Every day, he gets up at five to milk the cows. He says the work is hard, but he loves the animals and the green fields.» (farm = campo, cows = vacas, chickens = gallinas, milk = ordeñar, hard = duro, fields = potreros)"
MENU = "«Today's school menu: for lunch we have chicken with rice and a green salad. For dessert, there is fruit or yogurt. On Fridays, the cafeteria also sells sandwiches for two thousand pesos.» (menu = menú, chicken = pollo, rice = arroz, salad = ensalada, dessert = postre, yogurt = yogur, sells = vende)"
ROUTE = "«To get to the library, go straight along this corridor. Turn left at the water fountain. The library is the second door on the right.» (go straight = siga derecho, turn left = gire a la izquierda, water fountain = bebedero, second = segunda, right = derecha)"
CROSSING = "Imagen descrita: una persona con casco y chaleco amarillo está de pie junto a una bicicleta; detrás hay un paso de peatones. Guion: «Today I'll show you how to cross the street safely with your bike. First, stop at the corner. Look left, look right and look left again. Then walk with your bike across the crossing.» (cross = cruzar, safely = con seguridad, corner = esquina, crossing = paso de peatones)"
MUSIC = "«Welcome to the music workshop. Today we will use three instruments: the guitar, the drums and the piano. Please sit in a circle. I will give each of you a small percussion instrument.» (workshop = taller, instruments = instrumentos, drums = batería, circle = círculo, percussion = percusión)"
NOISE = "Título: «The Strange Noise». Guion: «Last weekend, Sara and her dad were camping near a lake. At night, Sara heard a strange noise outside the tent. She was nervous. Her dad took the flashlight and looked outside. It was a small fox looking for food! They laughed and put the food bag in the car.» (camping = acampando, lake = lago, tent = carpa, nervous = nerviosa, fox = zorro, bag = bolsa)"

# ------------------------------------------------------------------ clase 1
lesson(
    OA4, 1, MAT,
    "Aprenderé a predecir de qué trata un texto oral a partir de su título y de su contexto. Sirve para activar las palabras que ya conozco y entender mejor lo que escucho.",
    ["Sé que un título anticipa el tema del texto.", "Conozco palabras como storm, bike y beach."],
    [
        "Predecir (to predict) es pensar, antes de escuchar, qué se va a decir. Para eso usas dos fuentes: el título (title) y el contexto (context), que es la situación en que escuchas: una clase de Ciencias, un programa de radio, un aviso en un terminal. También usas tus conocimientos previos (background knowledge), es decir, lo que ya sabes del tema.",
        "Con el título The Night the Lights Went Out puedes predecir palabras como storm, dark, flashlight y candle. Con How to Keep Your Bike Safe puedes predecir que serán consejos o instrucciones y que aparecerán palabras como lock y helmet. Una predicción no es una certeza: es una hipótesis que luego comprobarás al escuchar.",
        "Predecir ayuda a escuchar con un propósito (purpose): sabes qué buscar. Anota dos o tres palabras o ideas antes de escuchar. Después, mientras oyes, marca cuáles se cumplieron. Si un título dice A Rainy Day, es razonable esperar umbrella y boots, pero sería poco razonable esperar sunscreen o desert.",
    ],
    [("predict", "predecir: pensar antes lo que se va a decir"), ("title", "título"), ("context", "contexto: la situación en que escuchas"), ("background knowledge", "conocimientos previos"), ("purpose", "propósito: lo que busco al escuchar"), ("guess", "suposición")],
    [
        ("Predecir por el título", BLACKOUT.split(" Guion")[0] + " ¿Qué palabras esperarías oír?", ["Pienso en una noche sin luz.", "Se me ocurren storm, dark y flashlight.", "Las anoto para comprobarlas."], "Palabras como storm, dark y flashlight"),
        ("Tipo de texto por el título", BIKELOCK.split(" Guion")[0] + " ¿Qué tipo de texto esperas?", ["Miro How to Keep... Safe.", "Eso suena a consejos o instrucciones.", "Espero verbos como use, park y write."], "Consejos o instrucciones para cuidar una bicicleta"),
    ],
    [
        ("Predecir algo que no tiene relación con el título.", "No se piensa en el tema ni en el contexto.", "Antes de predecir, lee el título y pregúntate de qué podría tratar."),
        ("Creer que la predicción debe cumplirse siempre.", "Una predicción es una hipótesis, no una certeza.", "Compara con el texto y corrige si hace falta."),
    ],
    [
        ("Título: «The Night the Lights Went Out». ¿Qué palabras probablemente oirás? a) storm, dark, flashlight b) beach, sand, towel", "a) storm, dark, flashlight", "Una noche sin luz se relaciona con tormenta, oscuridad y linterna."),
        ("Título: «How to Keep Your Bike Safe». ¿Qué tipo de texto esperas? a) consejos o instrucciones b) un cuento de terror", "a) consejos o instrucciones", "How to indica pasos o consejos."),
        ("Título: «A Day at the Beach». ¿Qué palabra esperas oír? a) sand b) snow", "a) sand", "Sand es arena y se relaciona con la playa."),
    ],
    [
        ("Estás en la clase de Ciencias y el título es «The Water Cycle» (ciclo del agua). ¿De qué esperas que hable? a) rain, sun, clouds b) goal, referee, medal", "a) rain, sun, clouds", "El ciclo del agua usa lluvia, sol y nubes."),
        ("Imagen descrita: un niño sentado en una habitación oscura sostiene una linterna. ¿Qué problema crees que tendrá la historia? a) se cortó la luz b) hay una fiesta de cumpleaños", "a) se cortó la luz", "La habitación oscura y la linterna son pistas."),
        ("Título: «A Surprise Party for Grandma». ¿Qué personajes esperas? a) familia y amigos b) pasajeros de un avión", "a) familia y amigos", "Una fiesta para la abuela reúne a personas cercanas."),
    ],
    [
        (ADULT + BLACKOUT + " Predijiste: «se cortó la luz». ¿Se cumplió? Responde sí o no.", "Sí", "Dice all the lights went out."),
        (ADULT + BIKELOCK + " ¿Cuál de las palabras que predijiste aparece: lock o oven? Responde con la que aparece.", "lock", "El primer consejo habla de a strong lock."),
        ("Elige el título más adecuado para este texto: «First, wash the fruit. Next, cut it. Finally, add juice.» a) Fruit Salad Recipe b) The Football Final", "a) Fruit Salad Recipe", "El texto da pasos para preparar fruta."),
    ],
    [
        ("Un compañero predijo que «How to Keep Your Bike Safe» trata de carreras de bicicleta. ¿Qué parte del título lo contradice?", "Keep Your Bike Safe", "Habla de cuidar la bicicleta, no de competir."),
        ("¿Por qué conviene predecir antes de escuchar? a) porque activa el vocabulario y ayuda a entender b) porque da la respuesta correcta", "a) porque activa el vocabulario y ayuda a entender", "Predecir no da respuestas, prepara la comprensión."),
    ],
    [
        ("Título: «A Rainy Day». ¿Cuántas de estas palabras son razonables? umbrella (paraguas), desert (desierto), puddle (charco), boots (botas), sunscreen (bloqueador)", "3", "Umbrella, puddle y boots calzan con un día de lluvia."),
        ("Título: «My First Day at a New School». ¿Cuál no es una predicción razonable? a) nervous feelings (nervios) b) a volcano erupting (un volcán en erupción) c) new friends (amigos nuevos)", "b) a volcano erupting (un volcán en erupción)", "Las otras dos se relacionan con un primer día de clases."),
    ],
    [("Un programa de radio se llama «Weather for the Weekend» (clima del fin de semana). ¿Qué datos esperas oír?", "Temperaturas y si lloverá o habrá sol", "El título habla del clima.")],
    [
        ("¿En qué dos cosas te apoyas para predecir?", "En el título y en el contexto", "Ambos entregan pistas del tema."),
        ("¿Una predicción es una certeza?", "No", "Es una hipótesis que luego se comprueba."),
        ("¿Para qué sirve anotar palabras esperadas antes de escuchar?", "Para saber qué buscar y comprobarlas después", "Da un propósito a la escucha."),
    ],
    task("Lee estos tres títulos: «The Lost Wallet», «How to Plant a Tree», «A Trip to the Zoo». Para cada uno escribe en tu hoja el tipo de texto que esperas (cuento, instrucciones o descripción) y tres palabras que crees que oirás. Un adulto puede leer luego un texto breve para comprobar.", "The Lost Wallet: cuento; wallet, police, find. How to Plant a Tree: instrucciones; seed, water, dig. A Trip to the Zoo: relato o descripción; animals, tickets, lion.", ["indica el tipo de texto de cada título", "anota tres palabras por título", "las palabras tienen relación con el título"], ["hoja con tres predicciones", "nota del adulto"], ["anotar palabras que no se relacionan", "no indicar el tipo de texto"], "Reconoce las predicciones razonables y repasa con la persona adulta cómo el título sugiere el tema."),
    "Pide a un adulto que lea el guion de la noche sin luz y marca en tu hoja cuáles de tus palabras predichas se cumplieron.",
    "Escribe un título en inglés para un texto sobre una excursión y tres palabras que predices.",
)

# ------------------------------------------------------------------ clase 2
lesson(
    OA4, 2, MAT,
    "Aprenderé a escuchar una primera vez para captar la idea general (gist) sin detenerme en cada palabra. Sirve para entender de qué trata un texto aunque no conozca todo el vocabulario.",
    ["Sé que la idea general es lo más importante de un texto.", "Conozco palabras como busy, quiet, farm y hard."],
    [
        "La primera escucha tiene un solo propósito: captar el gist, es decir, la idea general. Pregúntate: ¿de qué trata?, ¿quién habla? y ¿cómo termina? No intentes anotar números ni nombres; eso se hace en una segunda escucha, con una pregunta concreta. Escuchar para el gist es como mirar un paisaje completo antes de fijarte en una hoja.",
        "Si aparece una palabra desconocida, no te detengas. Sigue escuchando y apóyate en las palabras que sí conoces, en el tono y en la situación. Por ejemplo, aunque no sepas milk, si oyes cows y farm entiendes que se trata de trabajo con animales. Una sola palabra rara no arruina la comprensión.",
        "Un buen gist cabe en una frase corta y no incluye detalles pequeños. Del texto del pasillo, el gist es: la mañana empieza ruidosa y el pasillo queda en silencio cuando suena el timbre. Que un profesor diga Walk, please! es un detalle que apoya esa idea. Si tu frase es demasiado pequeña o demasiado general, ajústala.",
    ],
    [("gist", "idea general del texto"), ("detail", "detalle: dato pequeño"), ("first listening", "primera escucha"), ("unknown word", "palabra desconocida"), ("tone", "tono de voz"), ("busy", "ocupado, con mucho movimiento")],
    [
        ("Gist de una escena", ADULT + CORRIDOR + " ¿Cuál es el gist?", ["Escucho busy, run, bang y luego bell, empty, quiet.", "Primero hay ruido y después silencio.", "El gist es el paso del ruido al silencio."], "La mañana pasa del ruido en el pasillo al silencio cuando suena el timbre"),
        ("Gist con una palabra desconocida", ADULT + FARM + " Si no conoces milk, ¿entiendes de qué trata?", ["Sigo escuchando.", "Oigo uncle, farm, cows y animals.", "Trata del trabajo de un tío con animales en un campo."], "Sí: trata del campo y del trabajo de un tío con animales"),
    ],
    [
        ("Detenerse en una palabra que no se entiende.", "Se pierde el hilo del texto.", "Sigue escuchando y usa las demás palabras."),
        ("Dar como gist un detalle pequeño.", "Se confunde un dato con la idea completa.", "Resume en una frase de qué trata todo el texto."),
    ],
    [
        (ADULT + CORRIDOR + " ¿Cuál es el gist? a) la mañana pasa del ruido al silencio b) los estudiantes organizan una fiesta", "a) la mañana pasa del ruido al silencio", "Empieza busy y termina quiet."),
        (ADULT + FARM + " ¿De quién se habla? a) del tío del hablante y su campo b) de una profesora", "a) del tío del hablante y su campo", "Dice My uncle has a small farm."),
        ("¿Cuál de estas preguntas busca el gist? a) What is the text about? b) How many cows are there?", "a) What is the text about?", "La primera pregunta pide el tema general; la segunda pide un número."),
    ],
    [
        (ADULT + FARM + " ¿Cómo se siente el tío con su trabajo? a) lo ama aunque es duro b) lo odia", "a) lo ama aunque es duro", "Dice the work is hard, but he loves the animals."),
        (ADULT + CORRIDOR + " ¿Cuál es solo un detalle? a) a teacher says Walk, please b) el pasillo pasa de ruidoso a silencioso", "a) a teacher says Walk, please", "Es un dato pequeño; la idea general es el cambio de ruido a silencio."),
        (ADULT + FARM + " Si no entiendes la palabra milk, ¿qué haces? a) sigo escuchando y uso el resto b) me detengo hasta traducirla", "a) sigo escuchando y uso el resto", "El contexto aclara el sentido sin detener la escucha."),
    ],
    [
        (ADULT + "«Our school has a big project: we want to plant fifty trees in the park. Students, teachers and parents will work together on Saturday.» (plant = plantar, together = juntos). ¿Cuál es el gist? a) plantar árboles entre todos b) comprar un parque", "a) plantar árboles entre todos", "Todas las ideas giran en torno a plantar árboles."),
        (ADULT + CORRIDOR + " ¿Qué cambio ocurre entre el comienzo y el final del texto?", "Del ruido al silencio", "Empieza busy y termina empty and quiet."),
        (ADULT + "«I never eat breakfast at home. I have a snack at school, and I am hungry in the morning.» (never = nunca, snack = colación, hungry = con hambre). ¿Cuál es el gist? a) no desayuna en casa y tiene hambre en la mañana b) le gusta mucho desayunar", "a) no desayuna en casa y tiene hambre en la mañana", "Dice never eat breakfast y I am hungry."),
    ],
    [
        ("Lucas solo escuchó la palabra «cows» y dice que el texto trata de las vacas en general. ¿Qué error comete? a) confunde una palabra con el gist b) no oyó nada", "a) confunde una palabra con el gist", "El texto trata del trabajo del tío en el campo."),
        (ADULT + FARM + " ¿Qué frase muestra que el trabajo es duro?", "The work is hard", "Hard significa duro."),
    ],
    [
        arith(ADULT + FARM + " ¿Cuántos animales hay entre vacas y gallinas, si el tío tiene veinte vacas y cincuenta gallinas?", "20+50", "Se suman las vacas y las gallinas.", " animales"),
        (ADULT + CORRIDOR + " ¿Cuál es el mejor resumen? a) el pasillo pasa de ser ruidoso a quedar en silencio b) un profesor castiga a un estudiante", "a) el pasillo pasa de ser ruidoso a quedar en silencio", "El texto no habla de castigo."),
    ],
    [(ADULT + "Recibes este mensaje de voz: «Hi, it's Sofi. I'm late because of traffic, but I will arrive at six. Please wait for me at the bus stop.» (traffic = tráfico, arrive = llegar, wait = esperar, bus stop = paradero). ¿Cuál es el gist?", "Sofi llegará tarde, a las seis, y pide esperarla en el paradero", "Resume el mensaje completo.")],
    [
        ("¿Qué buscas en la primera escucha?", "La idea general", "Los detalles se buscan después."),
        ("¿Qué haces ante una palabra desconocida?", "Sigo escuchando y uso el contexto", "No conviene detenerse."),
        ("¿Cuánto debe medir un buen gist?", "Una frase corta", "Resume sin detalles pequeños."),
    ],
    task("Un adulto lee una sola vez este texto: «Every Saturday, Valentina helps in the community garden. She waters the plants and talks with her neighbors. Last week, a boy gave her a small lemon tree. She says that the garden makes her happy.» (community garden = huerto comunitario, waters = riega, neighbors = vecinos, lemon tree = limonero, makes her happy = la hace feliz). Escribe en tu hoja el gist en una sola frase.", "Valentina ayuda en el huerto comunitario y eso la hace feliz.", ["escribe una sola frase", "no incluye detalles pequeños", "la frase refleja todo el texto"], ["hoja con una frase", "nota del adulto"], ["escribir solo el regalo del limonero", "copiar el texto"], "Reconoce lo que acertó y pregunta qué idea une todas las frases del texto."),
    "Pide a un adulto que lea el texto del campo una vez y di el gist en voz alta antes de volver a escuchar.",
    "Escribe en español el gist de tu día de ayer en una sola frase.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA4, 3, MAT,
    "Aprenderé a escuchar por segunda vez con una pregunta concreta en mente, para encontrar un dato específico. Sirve para responder con exactitud sin tener que recordar todo el texto.",
    ["Sé obtener la idea general en una primera escucha.", "Conozco palabras como left, right, lunch y price."],
    [
        "En la segunda escucha tu propósito cambia: ya no buscas el tema, sino la respuesta a una pregunta. Lee la pregunta antes de escuchar y subraya la palabra interrogativa: what, where, when, who, how many o how much. Luego decide qué tipo de dato buscas: un número, un lugar, una persona o una acción.",
        "Mientras escuchas, enfoca tu atención en las palabras clave que se relacionan con la pregunta. Si preguntan por el postre, busca dessert. Si preguntan cómo llegar a la biblioteca, busca palabras de dirección: go straight, turn left, second door. Ignora lo que no responde la pregunta; no hace falta recordar todo.",
        "Por último, comprueba tu respuesta con el texto. ¿La palabra clave que escuchaste está junto a tu dato? Si una pregunta se puede responder de varias maneras, elige la que el texto dice con más claridad. Con práctica, una segunda escucha de unos segundos basta para ubicar el dato. En una conversación real también puedes preguntar para aclarar o confirmar: Sorry? o Could you repeat that, please? (¿puede repetir?) y Do you mean...? o Is that right? (¿quiere decir...?, ¿es correcto?).",
    ],
    [("question word", "palabra interrogativa: what, where, when..."), ("second listening", "segunda escucha"), ("turn left / right", "gira a la izquierda / derecha"), ("go straight", "sigue derecho"), ("dessert", "postre"), ("how much", "cuánto"), ("Could you repeat that, please?", "¿Puede repetir, por favor?"), ("Is that right?", "¿Es correcto?")],
    [
        ("Escuchar con una pregunta", ADULT + MENU + " Pregunta: ¿qué hay de plato principal?", ["Leo la pregunta: plato principal es lunch.", "Escucho la palabra lunch.", "Dice chicken with rice and a green salad."], "Pollo con arroz y ensalada verde"),
        ("Direcciones", ADULT + ROUTE + " Pregunta: ¿qué debes hacer en el bebedero?", ["Busco water fountain.", "Antes dice Turn left.", "Debo girar a la izquierda."], "Girar a la izquierda"),
    ],
    [
        ("Escuchar la segunda vez sin saber qué se busca.", "No se leyó la pregunta antes.", "Lee la pregunta y subraya la palabra interrogativa."),
        ("Confundir left (izquierda) con right (derecha).", "Se oye el final de la frase, pero no la dirección.", "Anota la dirección apenas la oigas."),
    ],
    [
        (ADULT + MENU + " ¿Qué hay de postre? a) fruta o yogur b) torta o helado", "a) fruta o yogur", "Dice dessert, there is fruit or yogurt."),
        (ADULT + MENU + " ¿Qué vende además la cafetería los viernes?", "Sándwiches", "Dice On Fridays, the cafeteria also sells sandwiches."),
        (ADULT + ROUTE + " ¿Hacia dónde se gira en el bebedero? a) a la izquierda b) a la derecha", "a) a la izquierda", "Dice Turn left."),
    ],
    [
        ("Antes de la segunda escucha lees: «¿Qué hay de almuerzo?». ¿Qué palabras buscas? a) chicken, rice, salad b) bell, locker", "a) chicken, rice, salad", "Son palabras de comida."),
        (ADULT + ROUTE + " ¿Qué puerta es la biblioteca?", "La segunda de la derecha", "Dice the second door on the right."),
        (ADULT + MENU + " ¿Qué día se venden sándwiches?", "El viernes", "Dice On Fridays."),
    ],
    [
        (ADULT + ROUTE + " Ordena. A) Girar a la izquierda en el bebedero. B) Seguir derecho por el pasillo. C) Entrar por la segunda puerta a la derecha.", "B, A, C", "Es el orden en que se dan las indicaciones."),
        (ADULT + MENU + " ¿Cuántas opciones de postre hay?", "2", "Hay fruta o yogur."),
        (ADULT + MENU + " ¿Qué acompaña al pollo? a) arroz y ensalada verde b) fideos y puré", "a) arroz y ensalada verde", "Dice chicken with rice and a green salad."),
    ],
    [
        (ADULT + MENU + " Sara dice que el postre es torta. ¿Qué dos opciones dice realmente el aviso?", "Fruta o yogur", "Dessert es postre y dice fruit or yogurt."),
        ("No alcanzaste a oír la hora de un aviso. ¿Qué dices en inglés? a) Could you repeat the time, please? b) Thank you, goodbye.", "a) Could you repeat the time, please?", "Sirve para pedir que repitan lo que no entendiste."),
    ],
    [
        arith(ADULT + MENU + " Si compras tres sándwiches el viernes, ¿cuántos pesos pagas en total?", "3*2000", "Cada sándwich cuesta 2.000 pesos.", " pesos"),
        (ADULT + ROUTE + " Para confirmar que entendiste «la segunda puerta a la derecha», ¿qué preguntas en inglés? a) Is that right? The second door on the right? b) How much is it?", "a) Is that right? The second door on the right?", "Is that right? sirve para corroborar lo que entendiste."),
    ],
    [(ADULT + "Un compañero nuevo te pregunta cómo llegar a la biblioteca. Usa este texto: " + ROUTE + " Dile la ruta en español.", "Seguir derecho, girar a la izquierda en el bebedero y entrar por la segunda puerta a la derecha", "Reúne las tres indicaciones del texto en orden.")],
    [
        ("¿Qué haces antes de la segunda escucha?", "Leo la pregunta y decido qué dato busco", "Así enfoco mi atención."),
        ("En Inglés de 7.º (OA 4, clase 3): ¿Qué significa «turn left»?", "Gira a la izquierda", "Left es izquierda."),
        ("¿Qué palabra interrogativa pregunta por un lugar?", "Where", "Where significa dónde."),
    ],
    task("Lee esta pregunta antes de escuchar: «¿A qué hora empieza la película y cuánto cuesta la entrada?». Un adulto lee dos veces: «The movie club meets on Friday. The film starts at six thirty, and the ticket costs three thousand pesos. After the film, we have a short discussion.» (movie club = club de cine, film = película, ticket = entrada, discussion = conversación). Escribe tus respuestas y la palabra clave que escuchaste para cada una.", "La película empieza a las 6:30 (clave: starts at six thirty). La entrada cuesta 3.000 pesos (clave: ticket costs).", ["responde las dos partes de la pregunta", "anota una palabra clave por respuesta", "usa solo datos del texto"], ["hoja con dos respuestas y dos claves", "nota del adulto"], ["confundir la hora con el precio", "anotar la conversación posterior como hora"], "Reconoce lo que acertó y repasa con la persona adulta qué palabra clave anuncia hora y cuál anuncia precio."),
    "Pide a un adulto que lea el menú otra vez y responde por escrito dos preguntas: qué hay de postre y qué se vende los viernes.",
    "Escribe tres preguntas en español que se puedan responder con el texto de las indicaciones de la biblioteca.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA4, 4, MAT,
    "Aprenderé a usar apoyos visuales, gestos, tono de voz y palabras que se parecen al español para comprender un texto oral. Sirve para entender mensajes aunque no conozca todas las palabras.",
    ["Sé que las imágenes y los gestos ayudan a entender.", "Conozco palabras como instrument, circle y piano."],
    [
        "Cuando escuchas, no solo oyes palabras. También ves imágenes, gestos y el entorno. Si el hablante señala una puerta y dice that door, entiendes cuál puerta. Si una imagen muestra una persona con casco y un paso de peatones, ya sabes que el tema es la seguridad en la calle. Estas son pistas visuales (visual clues).",
        "También hay pistas del propio lenguaje (linguistic clues). Los cognados (cognates) son palabras que se parecen al español y significan lo mismo: guitar (guitarra), instrument (instrumento), circle (círculo), important (importante). La repetición y el tono de voz también informan: Careful, careful! dicho en voz alta y rápida muestra urgencia o peligro.",
        "Usar estos apoyos no es hacer trampa: es una estrategia de comprensión. Los buenos oyentes combinan tres cosas: lo que oyen, lo que ven y lo que saben. Eso sí, hay que comprobar. Algunas palabras se parecen al español pero significan otra cosa: library es biblioteca, no «librería». Si el sentido no calza con el contexto, busca otra pista.",
    ],
    [("visual clue", "pista visual: imagen, gesto"), ("gesture", "gesto: movimiento de manos o cuerpo"), ("cognate", "cognado: palabra parecida al español"), ("tone", "tono de voz"), ("repetition", "repetición"), ("careful", "ten cuidado")],
    [
        ("Pista visual", CROSSING + " ¿Qué pistas visuales apoyan que el tema es la seguridad en la calle?", ["Miro la imagen descrita.", "Hay casco, chaleco amarillo y paso de peatones.", "Todo indica seguridad vial."], "El casco, el chaleco y el paso de peatones"),
        ("Cognados", ADULT + MUSIC + " ¿Qué palabras se parecen al español y ayudan a entender?", ["Busco guitar, piano, instruments, circle y percussion.", "Se parecen a guitarra, piano, instrumentos, círculo y percusión.", "Con ellas entiendo que es un taller de música."], "Guitar, piano, instruments, circle y percussion"),
    ],
    [
        ("Asumir que toda palabra parecida al español significa lo mismo.", "Hay falsos amigos que se parecen pero cambian de sentido.", "Comprueba con el contexto y con la imagen."),
        ("Ignorar el gesto del hablante.", "Se escucha solo la palabra y se pierde la pista visual.", "Mira a quien habla y a lo que señala."),
    ],
    [
        ("¿Cuál de estas palabras se parece al español y te ayuda a entender? a) important b) shelf", "a) important", "Important se parece a importante."),
        (CROSSING + " ¿Qué hace la persona de la imagen, según el dibujo descrito? a) está parada junto a su bicicleta b) corre por la playa", "a) está parada junto a su bicicleta", "La imagen describe una persona junto a una bicicleta."),
        ("El hablante señala una puerta y dice: «Please go through that door». ¿Qué apoya la comprensión? a) el gesto de señalar b) el volumen", "a) el gesto de señalar", "El gesto indica cuál puerta."),
    ],
    [
        (ADULT + MUSIC + " De las palabras guitar, drums, piano, instruments y circle, ¿cuántas se parecen a una palabra en español?", "4", "Guitar, piano, instruments y circle; drums no se parece."),
        (ADULT + CROSSING + " ¿Qué hay que hacer antes de cruzar?", "Detenerse en la esquina", "Dice First, stop at the corner."),
        (ADULT + MUSIC + " ¿Cuántos instrumentos nombra el profesor?", "3", "Nombra la guitarra, la batería y el piano."),
    ],
    [
        ("Imagen descrita: un reloj marca las 3. El hablante dice: «The meeting is at this time». ¿A qué hora es la reunión?", "A las 3", "La imagen entrega la hora."),
        ("El hablante dice en voz alta y rápido: «Careful, careful!». ¿Qué pistas muestran urgencia? a) la repetición y el tono b) el tamaño de la letra", "a) la repetición y el tono", "Repetir y subir la voz indican urgencia."),
        (ADULT + CROSSING + " ¿Cuántas veces hay que mirar a los lados antes de cruzar, según el guion?", "3", "Se mira izquierda, derecha y de nuevo izquierda."),
    ],
    [
        ("¿Por qué usar imágenes y gestos no es trampa? a) porque apoyan la comprensión del mensaje b) porque reemplazan escuchar", "a) porque apoyan la comprensión del mensaje", "Son estrategias que se combinan con la escucha."),
        ("El hablante dice «Pass me the red one» y señala una caja roja y otra azul. ¿Cuál caja debes pasar?", "La caja roja", "Red es rojo y el gesto lo confirma."),
    ],
    [
        ("Imagen descrita: un gráfico de barras con tres barras. Lunes 4, martes 6, miércoles 2. El audio dice: «The highest bar is Tuesday». ¿Cuántas unidades tiene la barra más alta?", "6", "Martes es la barra más alta y tiene 6."),
        ("El hablante señala un reloj, dice «late» con voz preocupada y se lleva las manos a la cabeza. ¿Qué crees que siente? a) preocupación b) alegría", "a) preocupación", "El tono y el gesto muestran angustia."),
    ],
    [("En la clase de música el profesor sostiene una guitarra sobre su pierna y dice «Hold it like this». ¿Qué pista te ayuda a saber qué hacer?", "Ver cómo la sostiene", "El gesto muestra la posición.")],
    [
        ("¿Qué es un cognado?", "Una palabra que se parece al español y significa lo mismo", "Ayuda a entender."),
        ("¿Qué pistas visuales puedes usar?", "Imágenes y gestos", "Apoyan lo que oyes."),
        ("¿Qué haces si una palabra se parece al español pero no calza con el contexto?", "Busco otra pista", "Puede ser un falso amigo."),
    ],
    task("Un adulto lee este texto y hace los gestos de dibujar y de mostrar: «Please draw a circle and a triangle on the paper. Then show the paper to the group.» (draw = dibujar, paper = papel, show = mostrar). Haz lo que dice el texto y luego escribe qué pistas visuales te ayudaron y qué cognados escuchaste.", "Pistas: el gesto de dibujar y el de mostrar la hoja. Cognados: circle (círculo), triangle (triángulo) y group (grupo).", ["hace las acciones del texto", "nombra una pista visual", "explica con un ejemplo"], ["hoja con pistas y acciones", "nota del adulto"], ["no mencionar ninguna pista visual", "creer que todas las palabras se parecen al español"], "Reconoce las pistas acertadas y repasa con la persona adulta cuándo un gesto aclara una palabra."),
    "Pide a un adulto que lea el texto del taller de música señalando objetos reales de la casa y observa cuántas palabras entiendes por el gesto.",
    "Haz una lista de seis cognados entre inglés y español, y revisa si en tu lista hay alguno que no signifique lo mismo.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA4, 5, MAT,
    "Aprenderé a comprobar mis predicciones, corregirlas con evidencia y resumir lo que escuché con apoyo. Sirve para aprender de mis errores y confiar en mi comprensión.",
    ["Sé predecir con el título y escuchar para el gist.", "Conozco palabras como fox, tent, lake y laugh."],
    [
        "Después de escuchar, vuelve a tu predicción y compárala con el texto. Si coincide, la confirmas (confirm). Si no coincide, la corriges (revise). Corregir no es un fracaso: es la parte más importante del proceso. Buenos oyentes cambian su idea cuando la evidencia lo exige.",
        "En el texto The Strange Noise, tal vez predijiste que Sara se encontró con un monstruo o que se fue corriendo. El texto dice otra cosa: era un zorro pequeño que buscaba comida. Entonces corriges: no era un monstruo y no huyeron; se rieron y guardaron la comida en el auto. Anota la evidencia, es decir, la frase del texto que te hizo cambiar de idea.",
        "Para cerrar, haz un resumen (summary) de dos o tres ideas con apoyo de tus notas. Un buen resumen dice quién, qué pasó y cómo terminó, sin detalles pequeños. Una secuencia útil es predecir, escuchar, comprobar y corregir. Si sigues estos pasos, tu comprensión mejora con cada texto.",
    ],
    [("confirm", "confirmar: comprobar que algo es cierto"), ("revise", "corregir, revisar"), ("evidence", "evidencia: frase del texto que respalda"), ("summary", "resumen"), ("fox", "zorro"), ("tent", "carpa")],
    [
        ("Descartar una predicción", ADULT + NOISE + " Predijiste: «Era un monstruo». ¿Se confirma o se descarta?", ["Busco qué hizo ruido.", "Dice It was a small fox.", "El monstruo no existe: se descarta."], "Se descarta; era un zorro pequeño"),
        ("Corregir con evidencia", ADULT + NOISE + " Predijiste que acampaban en la playa. Corrígelo.", ["Busco el lugar.", "Dice camping near a lake.", "Acampaban cerca de un lago."], "Acampaban cerca de un lago"),
    ],
    [
        ("Mantener la predicción aunque el texto la contradiga.", "Se prefiere la idea propia al texto.", "Corrige con la evidencia del texto."),
        ("Hacer un resumen con todos los detalles.", "Un resumen largo pierde la idea central.", "Incluye quién, qué pasó y cómo terminó."),
    ],
    [
        (ADULT + NOISE + " ¿Cómo se sentía Sara? a) nerviosa b) aburrida", "a) nerviosa", "Dice She was nervous."),
        (ADULT + NOISE + " ¿Dónde acampaban? a) cerca de un lago b) en el desierto", "a) cerca de un lago", "Dice camping near a lake."),
        (ADULT + NOISE + " ¿Qué hizo el papá de Sara?", "Tomó la linterna y miró afuera", "Dice took the flashlight and looked outside."),
    ],
    [
        (ADULT + NOISE + " Predijiste que Sara se fue corriendo. ¿Qué hizo su papá en realidad? a) tomó la linterna y miró afuera b) volvió a dormir", "a) tomó la linterna y miró afuera", "Eso contradice la predicción de huir."),
        (ADULT + NOISE + " ¿Qué palabra cambia tu predicción de miedo a risa? a) fox b) night", "a) fox", "El ruido era un zorro pequeño y por eso se rieron."),
        (ADULT + NOISE + " ¿Qué hicieron al final? a) rieron y guardaron la bolsa de comida en el auto b) cambiaron de lago", "a) rieron y guardaron la bolsa de comida en el auto", "Dice They laughed and put the food bag in the car."),
    ],
    [
        (ADULT + NOISE + " Ordena. A) El papá mira afuera. B) Sara escucha un ruido. C) Guardan la bolsa de comida en el auto.", "B, A, C", "El texto sigue ese orden."),
        (ADULT + NOISE + " ¿Por qué guardaron la comida en el auto? a) porque el zorro buscaba comida b) porque tenían frío", "a) porque el zorro buscaba comida", "Buscaba comida cerca de la carpa, así que la guardan para que no vuelva."),
        ("Ordena el proceso de un buen oyente. A) Corregir lo que no coincidió. B) Predecir con el título. C) Comprobar con el texto.", "B, C, A", "Primero predice, luego comprueba y corrige."),
    ],
    [
        ("Una compañera mantiene su predicción aunque el texto la contradiga. ¿Qué debería hacer? a) corregirla con la evidencia b) ignorar el texto", "a) corregirla con la evidencia", "Corregir es parte de comprender."),
        (ADULT + NOISE + " Un amigo predijo que el final sería triste. ¿Qué parte del final muestra que no?", "They laughed", "Reírse indica que terminó bien."),
    ],
    [
        (ADULT + NOISE + " ¿Cuál es el mejor resumen? a) Sara oyó un ruido en la noche, pero era un zorro pequeño que buscaba comida b) Sara tuvo miedo y se fue a casa", "a) Sara oyó un ruido en la noche, pero era un zorro pequeño que buscaba comida", "Incluye quién, qué pasó y cómo terminó."),
        ("¿Cuántos personajes humanos se nombran en el texto del zorro, contando a Sara y a su papá?", "2", "Son Sara y su papá; el zorro es un animal."),
    ],
    [(ADULT + "Título: «A Visit to the Dentist». Guion: «Don't worry, it was easy. I only had a check-up, and the dentist said my teeth are healthy.» (dentist = dentista, check-up = control, teeth = dientes, healthy = sanos). Si predijiste «fue muy doloroso», ¿cómo corriges?", "No fue doloroso: fue fácil, solo un control", "Dice it was easy y que fue un check-up.")],
    [
        ("En Inglés de 7.º (OA 4, clase 5): ¿Qué haces si tu predicción no coincide con el texto?", "La corrijo con la evidencia", "Corregir mejora la comprensión."),
        ("¿Qué debe incluir un buen resumen?", "Quién, qué pasó y cómo terminó", "Resume sin detalles pequeños."),
        ("¿Qué significa «confirm»?", "Confirmar", "Es comprobar que algo es cierto."),
    ],
    task("Lee el título «The Missing Cake» y escribe una predicción. Luego un adulto lee dos veces: «On Sunday, Lucía put a lemon cake on the table. When she came back, the cake was gone. She looked under the table and found her little dog with cream on his nose. She laughed and hid the next cake in the cupboard.» (missing = perdida, gone = desaparecida, cream = crema, nose = hocico, hid = escondió, cupboard = alacena). Escribe si tu predicción se confirmó o se corrigió, con la evidencia, y un resumen de dos frases.", "Predicción: alguien se llevó la torta. Se corrigió: la comió el perrito (evidencia: cream on his nose). Resumen: la torta desapareció, la encontró en el perrito y la próxima la escondió.", ["escribe una predicción antes de escuchar", "compara con la evidencia del texto", "resume en dos frases"], ["hoja con predicción, evidencia y resumen", "nota del adulto"], ["no comparar con el texto", "resumen con demasiados detalles"], "Reconoce lo que acertó y revisa con la persona adulta si el resumen responde quién, qué pasó y cómo terminó."),
    "Pide a un adulto que lea el texto del zorro otra vez y marca con una cruz las palabras que corrigieron tu primera idea.",
    "Elige un título de una película o un libro que conozcas, escribe tres predicciones y marca después cuáles se cumplieron.",
)
