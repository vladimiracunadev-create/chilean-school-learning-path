"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 02: comprensión de textos orales (propósito, tema, detalles,
relaciones entre ideas, vocabulario, conectores y sonidos).

Las «escuchas» las lee una persona adulta en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Todos los textos son originales, con pista en español. Los títulos de clase del plan son genéricos; aquí cada clase trabaja
un grupo de contenidos del OA: propósito e idea general; información específica; relaciones y conectores; palabras clave,
modismos y collocations; sonidos y cualidades de la voz. Los nombres de lugares y personas son ficticios.
"""
from __future__ import annotations

from en_m2_a_common import ADULT, MAT, arith, lesson, task

OA = "EN2M OA 02"

# ================================================== clase 1: propósito, tema e idea general
BRIDGE = "«Good morning, school. This is the Science Club. Today we want to explain why bridges often use triangle shapes. A triangle does not change its shape when you push it, so it is strong. Engineers use triangles in bridges, towers and even bicycle frames.» (bridges = puentes, triangle = triángulo, push = empujar, strong = fuerte, engineers = ingenieros, towers = torres, frames = cuadros)"
BAKE = "«Hi, everyone! Our class is saving money for the end-of-year trip. Come to our bake sale on Thursday at the break. Bring some coins!» (saving = ahorrando, bake sale = venta de pasteles, break = recreo, coins = monedas)"
MARLOW = "«In the fictional town of Marlow, people hold a lantern night every spring. Families walk along the old bridge with paper lanterns, and the town band plays slow music. The mayor says the night is a way to welcome the new season.» (fictional = ficticio, lantern = farol, band = banda, mayor = alcalde, welcome = dar la bienvenida, season = estación)"
BUS = "«Attention, passengers. The eight-twenty bus to the city centre is delayed by ten minutes. Please wait at stop four.» (passengers = pasajeros, delayed = retrasado, stop = paradero)"

lesson(
    OA, 1, MAT,
    "Aprenderé a reconocer el propósito, el tema y las ideas relevantes de un texto oral, incluso cuando el tema me es poco conocido. Sirve para entender lo esencial de un aviso, un mensaje o una explicación sin traducir cada palabra.",
    ["Sé reconocer si un hablante informa, invita o cuenta algo.", "Sé usar las preguntas who, what, where y when."],
    [
        "El propósito (purpose) es lo que el hablante quiere lograr: informar o explicar, invitar o persuadir, advertir o contar. El tema (topic) es de qué trata el texto, y la idea general (main idea) es lo más importante que se dice sobre ese tema. Un detalle (detail) es un dato que apoya la idea, como una hora o un lugar.",
        "Cuando el tema es poco conocido, no necesitas entender todas las palabras. Escucha las primeras frases, que suelen anunciar el tema, y las últimas, que suelen cerrar la idea. Las palabras que se repiten o se explican con otras (por ejemplo, strong después de triangle) son pistas de la idea general. Las palabras parecidas al español, como engineers o triangle, también ayudan.",
        "Para separar la idea general de los detalles, hazte la pregunta: ¿qué se pierde si borro esta frase? Si el texto sigue teniendo sentido, era un detalle. Si el texto deja de tener sentido, era una idea relevante. Verbos como explain, come to y please wait te muestran el propósito: explicar, invitar y pedir.",
    ],
    [("purpose", "propósito: lo que el hablante quiere lograr"), ("topic", "tema: de qué trata el texto"), ("main idea", "idea general: lo más importante que se dice del tema"), ("detail", "detalle: dato que apoya la idea"), ("explain", "explicar"), ("delayed", "retrasado")],
    [
        ("Idea general y detalle", ADULT + "«Welcome to the school library. Please keep your voice low, because many students are studying. You can borrow up to three books for two weeks.» (voice low = voz baja, borrow = pedir prestado). ¿Cuál es la idea general?", ["Busco qué pide el hablante en la primera frase.", "Se dice Please keep your voice low y se da una razón.", "Los datos de los libros son detalles."], "Pedir silencio en la biblioteca porque otros estudian"),
        ("Propósito de un mensaje", ADULT + "«Hello, neighbours. The street fair is cancelled this Saturday because of the strong wind. We will tell you the new date soon.» (cancelled = cancelada, wind = viento). ¿Para qué se dice este mensaje?", ["Veo qué hace el hablante: da una noticia.", "Anuncia que la feria se cancela y que habrá otra fecha.", "Es informar."], "Informar que se cancela la feria"),
    ],
    [
        ("Decidir la idea general con el primer dato que se oye (la hora) y no con lo que se explica.", "Un detalle se confunde con la idea relevante.", "Pregunta qué se pierde si borras la frase; si todo sigue claro, era un detalle."),
        ("Pensar que, si no entiendo una palabra, no puedo entender el propósito.", "El propósito se deduce de verbos y frases como explain, come to o please wait.", "Busca palabras conocidas y las que se repiten antes de rendirte."),
    ],
    [
        (ADULT + BRIDGE + " ¿Qué forma hace que un puente sea fuerte?", "El triángulo", "El guion dice A triangle does not change its shape, so it is strong."),
        (ADULT + BRIDGE + " ¿Quién habla en este mensaje? A) el Science Club B) la dirección", "A", "El guion empieza con This is the Science Club."),
        (ADULT + BAKE + " ¿Cuándo es la venta de pasteles? A) el jueves, en el recreo B) el viernes, en la tarde", "A", "El guion dice on Thursday at the break."),
    ],
    [
        (ADULT + BRIDGE + " ¿Cuál es el propósito del mensaje? A) explicar por qué los puentes usan triángulos B) invitar a un campeonato", "A", "El guion dice we want to explain why bridges often use triangle shapes."),
        (ADULT + BAKE + " ¿Para qué se hace la venta de pasteles? A) para ahorrar dinero para el paseo B) para comprar útiles", "A", "Dice saving money for the end-of-year trip."),
        (ADULT + MARLOW + " ¿Cuál es el tema general del texto? A) una fiesta de faroles en primavera B) un concurso de música", "A", "La frase inicial dice lantern night every spring; la banda es un detalle."),
    ],
    [
        (ADULT + BAKE + " ¿Qué se pide llevar? A) monedas B) pasteles", "A", "El guion dice Bring some coins."),
        (ADULT + MARLOW + " ¿Qué dice el alcalde sobre la noche de faroles? A) que sirve para dar la bienvenida a la nueva estación B) que el puente es muy antiguo", "A", "Dice a way to welcome the new season."),
        arith("En la venta de pasteles, cada trozo cuesta 600 pesos y cada jugo cuesta 500 pesos. Dani compra 3 trozos y 2 jugos. ¿Cuántos pesos paga?", "3*600+2*500", "Se suma el costo de los trozos con el costo de los jugos."),
    ],
    [
        (ADULT + BRIDGE + " Pau dice que el propósito es informar. Teo dice que es invitar a una actividad. ¿Quién tiene razón? A) Pau, porque explica un hecho y no pide actuar B) Teo, porque dice This is the Science Club", "A", "El texto explica por qué el triángulo es fuerte y no invita a nada."),
        (ADULT + BAKE + " ¿Qué frase muestra que el hablante quiere que el público actúe? A) Come to our bake sale B) We are saving money", "A", "Come to es una invitación; saving money explica la razón."),
    ],
    [
        (ADULT + MARLOW + " Un compañero dice que el texto trata de un puente. ¿Qué es en realidad el puente? A) un lugar donde ocurre la fiesta B) el tema principal", "A", "El tema es la noche de faroles; el puente solo es el lugar donde caminan."),
        (ADULT + BRIDGE + " Ordena las ideas como aparecen: a) dónde usan triángulos los ingenieros b) el triángulo no cambia de forma al empujarlo c) la pregunta de por qué los puentes usan triángulos", "c, b, a", "Primero se anuncia el tema, luego la razón y al final los usos."),
    ],
    [(ADULT + BUS + " ¿A qué hora saldrá ahora el bus de las ocho y veinte?", "A las 8:30", "El bus se retrasa diez minutos: 8:20 más 10 minutos son las 8:30.")],
    [
        ("¿Qué es el propósito de un texto oral (en comprensión oral)?", "Lo que el hablante quiere lograr", "Puede ser informar, invitar o advertir."),
        ("¿Qué pregunta ayuda a separar un detalle de la idea general?", "¿Qué se pierde si borro esta frase?", "Si el texto sigue claro, era un detalle."),
        ("¿Dónde suelen aparecer el tema y el cierre de la idea?", "En las primeras y las últimas frases", "Ayudan cuando hay palabras desconocidas."),
    ],
    task("Una persona adulta lee dos veces: «Hello, music fans. The school radio will play songs chosen by students every Friday at lunch. If you want to suggest a song, put your name and the title in the red box by the office. Please choose songs without bad words.» (suggest = sugerir, title = título, box = caja, office = oficina, bad words = groserías). En tu hoja escribe: el propósito, el tema, una idea relevante y un detalle.", "Propósito: invitar a sugerir canciones. Tema: la radio del colegio. Idea relevante: se tocan canciones elegidas por estudiantes los viernes. Detalle: la caja roja junto a la oficina (o: sin groserías).", ["dice el propósito con una pista del guion", "separa una idea relevante de un detalle", "no inventa datos que no están en el guion"], ["hoja con cuatro respuestas", "nota de la persona que leyó"], ["decir que el propósito es describir un lugar", "escribir una cifra que el guion no dice"], "Marca con otro color la frase que usaste para el propósito y revisa si es una invitación."),
    "Pide que te lean otra vez el aviso del bus y marca la frase que pide una acción.",
    "Escucha un aviso corto (por ejemplo, del colegio o del transporte) y escribe en español su propósito y un detalle.",
)

# ================================================== clase 2: información específica y detalles
MATCH = "«Ana: Are you coming to the basketball match tomorrow? Beto: I would like to, but I have a dentist appointment at five. Ana: What a pity! The match starts at six at the Central Gym. Beto: Maybe I can arrive late, at about six thirty. Ana: Great. I think our team is very fast this year. Beto: You always say that!» (match = partido, dentist appointment = hora al dentista, pity = pena, late = tarde, fast = rápido)"
JACKET = "«Hello, this is Rosa from the lost property office. We found your blue jacket on the bus. It was under a seat near the back door. You can collect it in room twelve from nine to twelve, Monday to Friday. Please bring your student card.» (lost property = objetos perdidos, found = encontramos, seat = asiento, collect = retirar, student card = credencial)"
OPINIONS = "«Speaker 1: I love the new school app because it shows my timetable. Speaker 2: I like it too, but it is slow in the morning. Speaker 3: I do not use it. I prefer paper because I never lose it.» (app = aplicación, timetable = horario, slow = lenta, paper = papel, never = nunca)"

lesson(
    OA, 2, MAT,
    "Aprenderé a encontrar información específica en un texto oral: personas, acciones, opiniones, lugares, tiempos y situaciones. Sirve para anotar datos exactos de un mensaje o de una conversación sin confundir quién dijo qué.",
    ["Sé escuchar para identificar el propósito de un texto.", "Sé los números y las horas en inglés."],
    [
        "La información específica (specific information) es un dato exacto: una hora, un lugar, una cifra, un nombre. Los detalles clave (key details) responden preguntas como who, what, where, when y why. Cada pregunta busca un tipo de palabra: who busca personas, where busca lugares como near, in room o at the gym, y when busca días, horas o frases como at five.",
        "En una conversación hay varios hablantes (speakers). Antes de anotar un dato, pregúntate quién lo dijo. Las opiniones se reconocen por verbos como love, like, prefer o think. Los conectores but, too y also avisan que aparece un contraste o una suma. Si un hablante dice I like it too, su opinión se parece a la de la persona anterior, pero no es una opinión nueva.",
        "Anota solo palabras clave, no frases completas, y escribe junto a cada dato el nombre del hablante o la letra de la pregunta. Cuando dos horas o dos lugares compiten, vuelve a la pregunta y elige el que ella pide. Las cifras con about (alrededor de) son aproximadas, y las que llevan exactly son exactas.",
    ],
    [("specific information", "información específica: dato exacto"), ("key details", "detalles clave"), ("speaker", "hablante"), ("opinion", "opinión: lo que alguien piensa o siente"), ("prefer", "preferir"), ("appointment", "hora o cita acordada")],
    [
        ("Distinguir dos horas", ADULT + "«The film club meets at four. The film starts at four thirty and finishes at six. After that, we talk about it until six forty-five.» (film = película, finishes = termina, until = hasta). ¿A qué hora termina la película?", ["La pregunta pide cuándo termina la película.", "El guion dice finishes at six.", "Las otras horas son de otras acciones."], "A las seis"),
        ("Quién dijo qué", ADULT + "«Luis: I think the ending was sad. Marta: Really? I thought it was funny.» (ending = final, sad = triste, funny = divertido). ¿Quién piensa que el final fue triste?", ["Busco el verbo think y la palabra sad.", "La frase I think the ending was sad la dice Luis.", "Marta tiene la opinión contraria."], "Luis"),
    ],
    [
        ("Anotar la hora del compromiso de otro hablante (el dentista) como la hora del partido.", "Se mezclan los datos de dos acciones distintas.", "Escribe junto a cada hora la acción que ella nombra."),
        ("Creer que I like it too es una opinión distinta.", "El conector too muestra que la opinión coincide con la anterior.", "Marca los conectores but, too y also antes de anotar opiniones."),
    ],
    [
        (ADULT + MATCH + " ¿Dónde es el partido? A) en el Central Gym B) en la escuela", "A", "El guion dice at the Central Gym."),
        (ADULT + JACKET + " ¿De qué color es la chaqueta?", "Azul", "El guion dice blue jacket."),
        (ADULT + OPINIONS + " ¿Qué cosa le gusta al hablante 1 de la aplicación? A) que muestra su horario B) que es rápida", "A", "Dice it shows my timetable."),
    ],
    [
        (ADULT + MATCH + " ¿A qué hora empieza el partido? A) a las seis B) a las cinco", "A", "El guion dice starts at six; las cinco es la hora del dentista."),
        (ADULT + JACKET + " ¿Dónde estaba la chaqueta? A) bajo un asiento, cerca de la puerta de atrás B) en la sala doce", "A", "Dice under a seat near the back door; la sala doce es el lugar para retirarla."),
        (ADULT + OPINIONS + " ¿Qué problema menciona el hablante 2? A) la aplicación es lenta por la mañana B) la aplicación no tiene horario", "A", "Dice but it is slow in the morning."),
    ],
    [
        (ADULT + MATCH + " ¿A qué hora piensa llegar Beto?", "Alrededor de las seis y media", "Dice at about six thirty; about indica una hora aproximada."),
        (ADULT + JACKET + " ¿Cuántas horas al día se puede retirar la chaqueta, de nueve a doce?", "3", "De nueve a doce hay tres horas."),
        (ADULT + OPINIONS + " ¿Quién prefiere el papel y por qué?", "El hablante 3, porque nunca lo pierde", "Dice I prefer paper because I never lose it."),
    ],
    [
        (ADULT + MATCH + " Beto no puede llegar a la hora de inicio. ¿Por qué? A) tiene una hora al dentista a las cinco B) vive lejos del gimnasio", "A", "Dice dentist appointment at five y Maybe I can arrive late."),
        (ADULT + OPINIONS + " ¿Qué dos hablantes tienen una opinión positiva, aunque uno la matiza? A) 1 y 2 B) 2 y 3", "A", "El 1 dice I love it y el 2 dice I like it too, but it is slow."),
    ],
    [
        (ADULT + JACKET + " Un compañero entiende que puede retirar la chaqueta los sábados en la sala nueve. ¿Qué dos datos corrige el guion? A) los días son de lunes a viernes y la sala es la doce B) los días son de martes a sábado y la sala es la doce", "A", "El guion dice room twelve y Monday to Friday; los sábados no está."),
        (ADULT + MATCH + " ¿Cuál es la opinión de Ana sobre su equipo? A) que es muy rápido B) que juega lento", "A", "Dice our team is very fast this year."),
    ],
    [(ADULT + "«Hi, this is Dan. I am at the station. The train to the coast leaves at seven fifteen from platform two, but I will wait for you near the ticket machine.» (station = estación, platform = andén, ticket machine = máquina de boletos). ¿Desde qué andén sale el tren?", "Desde el andén dos", "El guion dice from platform two.")],
    [
        ("¿Qué palabra de pregunta busca un lugar?", "Where", "Where pregunta por lugares."),
        ("¿Qué indica la palabra about delante de una hora?", "Que la hora es aproximada", "No es un dato exacto."),
        ("¿Qué debo anotar junto a cada dato en una conversación?", "Quién lo dijo", "Evita confundir a los hablantes."),
    ],
    task("Una persona adulta lee dos veces: «Hello, this is Camila from the youth centre. The chess workshop starts next Tuesday at five in the blue room, on the first floor. The teacher is Mr. Salas. The workshop is free, but you need to bring your own chess set, if you have one.» (workshop = taller, floor = piso, own = propio, set = juego). En tu hoja escribe cinco datos: día, hora, lugar, profesor y una condición.", "Martes (próximo); cinco; sala azul del primer piso; Mr. Salas; es gratis y se lleva un juego de ajedrez propio, si se tiene.", ["anota cinco datos distintos", "cada dato coincide con el guion", "indica quién dice cada información"], ["hoja con cinco datos", "nota de la persona que leyó"], ["anotar la hora con cinco y media", "olvidar el piso o el nombre del profesor"], "Compara tu nota con el guion y subraya el dato que cambiaste al escribir."),
    "Pide que te lean otra vez la conversación del partido y escribe quién dice cada hora.",
    "Escribe en español qué dato exacto buscarías si te preguntan where, when y who en un mensaje de bus.",
)

# ================================================== clase 3: relaciones entre ideas y conectores
POOL = "«The sports club has a problem: the gym is too small for forty players. As a result, the coach can only take twenty players on Tuesdays. To solve it, the club will use the school patio on Thursdays, unless it rains. As soon as the new schedule is ready, the coach will send it to everyone.» (problem = problema, coach = entrenador, solve = resolver, patio = patio, rains = llueve, schedule = horario)"
BAND = "«Neither Lola nor Hugo can play on Saturday, so the band needs a new drummer. Either Mia or Otto can help, but Otto is busy. The band will practise on Friday, though the room is small.» (drummer = baterista, busy = ocupado, practise = ensayar, small = pequeña)"
WALK = "«Please read this carefully. Our hiking group will leave at seven in the morning. As soon as we reach the top, we will have lunch. We will not go if the forecast says storm, unless the guide decides the path is safe. The path is long, though the view is worth it.» (hiking = senderismo, top = cima, forecast = pronóstico, storm = tormenta, guide = guía, path = sendero, view = vista, worth it = vale la pena)"

lesson(
    OA, 3, MAT,
    "Aprenderé a reconocer relaciones entre ideas en un texto oral: importancia, problema y solución, y los conectores neither…nor, either…or, though, unless, as soon as y as a result. Sirve para entender por qué ocurre algo y qué condición lo cambia.",
    ["Sé usar and, but, so y because.", "Sé distinguir el tema y los detalles de un texto oral."],
    [
        "Muchos textos orales presentan un problema (problem) y una solución (solution). El problema dice qué sale mal; la solución dice qué se hará. Las ideas también se ordenan por importancia: la más importante se repite, se dice con énfasis o aparece después de frases como the main thing is… Reconocer esta relación te ayuda a resumir.",
        "Los conectores muestran cómo se unen las ideas. Neither…nor significa «ni… ni», y niega las dos opciones. Either…or significa «o… o», y ofrece dos opciones. Though se usa para contrastar, como «aunque» o «sin embargo». Unless significa «a menos que» o «si no». As soon as significa «tan pronto como», y marca un momento. As a result significa «como resultado» e indica una consecuencia.",
        "Al escuchar, marca mentalmente el conector y pregúntate qué relación crea: contraste, condición, tiempo, consecuencia u opción. Después anota las dos ideas que une. Por ejemplo, en «We will go unless it rains» la condición para no ir es la lluvia. En «Neither Lola nor Hugo can come» ninguna de las dos personas viene.",
    ],
    [("problem", "problema: lo que sale mal"), ("solution", "solución: lo que se hará"), ("neither…nor", "ni… ni"), ("either…or", "o… o"), ("though", "aunque; sin embargo"), ("unless", "a menos que; si no"), ("as soon as", "tan pronto como"), ("as a result", "como resultado")],
    [
        ("Conector de condición", ADULT + "«We will have the concert outside unless the weather is bad.» (concert = concierto, weather = clima). ¿Cuándo no será afuera?", ["Unless significa a menos que.", "La condición es que el clima sea malo.", "Entonces no será afuera si el clima es malo."], "Si el clima es malo"),
        ("Problema y consecuencia", ADULT + "«The bus was late. As a result, we missed the first class.» (missed = perdimos). ¿Cuál es la consecuencia?", ["As a result introduce una consecuencia.", "Lo que viene después es missed the first class.", "El bus atrasado es la causa."], "Perdieron la primera clase"),
    ],
    [
        ("Confundir either…or con neither…nor y entender que las dos personas ayudarán.", "Se pierde que neither…nor niega las dos opciones.", "Neither…nor suma dos negativos: ninguna de las dos."),
        ("Entender though como porque.", "Though marca contraste, no causa.", "Usa aunque o sin embargo y comprueba que las dos ideas se oponen."),
    ],
    [
        (ADULT + POOL + " ¿Cuál es el problema del club? A) el gimnasio es muy pequeño para cuarenta jugadores B) el entrenador no tiene horario", "A", "El guion dice the gym is too small for forty players."),
        (ADULT + BAND + " ¿Quién puede ayudar al grupo, pero está ocupado? A) Otto B) Hugo", "A", "El guion dice Either Mia or Otto can help, but Otto is busy."),
        (ADULT + WALK + " ¿A qué hora sale el grupo? A) a las siete de la mañana B) a las siete de la tarde", "A", "El guion dice at seven in the morning."),
    ],
    [
        (ADULT + POOL + " ¿Cuál es la solución que propone el club? A) usar el patio los jueves B) cerrar el club", "A", "Dice the club will use the school patio on Thursdays."),
        (ADULT + BAND + " ¿Quiénes no pueden tocar el sábado? A) Lola y Hugo B) Mia y Otto", "A", "Neither Lola nor Hugo can play on Saturday: ninguno de los dos puede."),
        (ADULT + WALK + " ¿Qué harán al llegar a la cima? A) almorzar B) volver", "A", "As soon as we reach the top, we will have lunch."),
    ],
    [
        (ADULT + POOL + " ¿Qué relación crea As a result? A) muestra una consecuencia del gimnasio chico B) muestra una condición", "A", "La consecuencia es que el entrenador solo puede llevar veinte jugadores."),
        (ADULT + POOL + " El entrenador recibe cuarenta jugadores, pero puede llevar veinte los martes. ¿Cuántos jugadores no entran ese día?", "20", "40 menos 20 son 20."),
        (ADULT + WALK + " ¿Cuándo sí irán, aunque el pronóstico diga tormenta? A) si la guía decide que el sendero es seguro B) si el grupo llega temprano", "A", "Dice unless the guide decides the path is safe."),
    ],
    [
        (ADULT + WALK + " ¿Qué contraste expresa la frase The path is long, though the view is worth it? A) el sendero es largo, pero la vista lo compensa B) el sendero es largo, por eso es seguro", "A", "Though marca contraste entre largo y vale la pena."),
        (ADULT + BAND + " ¿Por qué el grupo busca baterista? A) porque Lola y Hugo no pueden tocar el sábado B) porque el cuarto es pequeño", "A", "La consecuencia aparece con so: Neither Lola nor Hugo can play on Saturday, so the band needs a new drummer."),
    ],
    [
        (ADULT + POOL + " Ordena las ideas en el orden en que aparecen: a) el nuevo horario llegará a todos b) el club usará el patio c) el gimnasio es pequeño", "c, b, a", "Primero el problema, luego la solución y al final el aviso del horario."),
        (ADULT + WALK + " Si el pronóstico dice tormenta y la guía considera inseguro el sendero, ¿qué ocurre? A) no salen B) salen igual", "A", "Unless significa a menos que; si el sendero no es seguro, la condición no se cumple."),
    ],
    [(ADULT + "«Neither the museum nor the park is open on Mondays. Either the cinema or the library is a good plan, but the library closes early.» (museum = museo, closes = cierra, early = temprano). ¿Qué lugar cierra temprano?", "La biblioteca", "El guion dice the library closes early.")],
    [
        ("¿Qué significa unless?", "A menos que; si no", "Introduce una condición."),
        ("¿Qué relación muestra as a result?", "Una consecuencia", "Une una causa con su resultado."),
        ("¿Qué significa neither…nor?", "Ni… ni", "Niega las dos opciones."),
    ],
    task("Una persona adulta lee dos veces: «The school choir has a problem: only six students come to practice. As a result, the group sounds weak. The teacher will invite more students as soon as the new term starts. Either Anita or Ben will make the poster, but neither of them has the paint yet. The choir will sing at the end of the year, unless the room is closed.» (choir = coro, weak = débil, term = semestre, poster = afiche, paint = pintura). En tu hoja escribe: el problema, la consecuencia, la solución y una condición.", "Problema: solo seis estudiantes van a los ensayos. Consecuencia: el grupo suena débil. Solución: la profesora invitará a más estudiantes cuando empiece el semestre. Condición: cantarán a fin de año, a menos que la sala esté cerrada.", ["nombra el problema y la solución", "usa unless o as soon as en una condición", "no mezcla datos de otras ideas"], ["hoja con cuatro respuestas", "nota de la persona que leyó"], ["decir que la solución es el afiche", "confundir neither con either"], "Subraya en la hoja el conector de cada respuesta y comprueba que muestra la relación correcta."),
    "Pide que te lean otra vez el guion del grupo musical y marca los conectores.",
    "Escribe en español dos situaciones de tu vida diaria y une cada una con un conector como unless o as a result.",
)

# ================================================== clase 4: palabras clave, modismos y collocations
CAMP = "«Last weekend my friends and I decided to take a trip to the coast. We caught an early bus, but there was heavy traffic, so we arrived late. It was a piece of cake to find the hostel because the street was very clear. In the evening, we made a plan: we would take photos, have a picnic and keep in touch with our families.» (coast = costa, caught = tomamos, heavy traffic = mucho tráfico, hostel = hostal, clear = clara, picnic = picnic)"
TEST = "«I felt under the weather on Monday, so I stayed home. Now I have to hit the books because the exam is next week. My brother says it is not difficult, but it will not be a piece of cake for me. I pay attention in class, and I take notes, so I hope it goes well.» (under the weather = indispuesto, hit the books = ponerse a estudiar, exam = prueba, difficult = difícil, notes = apuntes)"
CLUB = "«Our robotics club is a team of twelve students. We make a decision together before each project. Then we do our research, give a short presentation and save time with a shared plan. Once in a blue moon, we do not agree, but we always find a solution.» (robotics = robótica, project = proyecto, research = investigación, presentation = presentación, shared = compartido, agree = estar de acuerdo, solution = solución)"

lesson(
    OA, 4, MAT,
    "Aprenderé a reconocer palabras y frases clave, modismos de uso frecuente y combinaciones habituales de palabras (collocations) en un texto oral. Sirve para entender una idea aunque no conozca cada palabra y para usar frases naturales.",
    ["Sé verbos comunes como make, take, have y do.", "Sé identificar el tema de un texto."],
    [
        "Las palabras clave (key words) son las que sostienen el mensaje; si las quitas, el texto pierde sentido. Muchas veces se repiten o se dicen más fuerte. Una expresión idiomática (idiom) es una frase cuyo significado no se obtiene palabra por palabra: a piece of cake significa «algo muy fácil», y under the weather significa «sentirse indispuesto», no «bajo el clima».",
        "Una colocación (collocation) es una combinación de palabras que suenan naturales juntas. En inglés decimos make a decision y no do a decision; take a photo y no make a photo; heavy traffic y no strong traffic; pay attention; take notes; have a picnic; have breakfast; take a rest; give a presentation; catch a bus; keep in touch (seguir en contacto) y save time (ahorrar tiempo). Aprender el verbo con su pareja es más útil que aprenderlo suelto.",
        "El vocabulario temático (thematic vocabulary) son las palabras de un mismo tema: viaje (bus, hostel, coast, traffic), estudio (exam, notes, books) o trabajo en equipo (project, presentation, decision). Si identificas el tema, puedes predecir palabras y entender mejor un modismo por el contexto. Cuando no sepas una palabra, escucha lo que rodea al modismo: en it will not be a piece of cake for me, la frase but ayuda a ver que es difícil.",
    ],
    [("key words", "palabras clave"), ("idiom", "modismo: frase de sentido no literal"), ("collocation", "combinación natural de palabras"), ("piece of cake", "muy fácil"), ("under the weather", "indispuesto, no muy bien de salud"), ("hit the books", "ponerse a estudiar"), ("keep in touch", "seguir en contacto"), ("once in a blue moon", "muy rara vez"), ("thematic vocabulary", "vocabulario de un mismo tema")],
    [
        ("Collocation de un verbo", ADULT + "«We need to make a decision about the school trip.» (decision = decisión). ¿Qué verbo va con decision? A) make B) do", ["Pienso en la combinación natural.", "En inglés se dice make a decision.", "Do a decision no es natural."], "A"),
        ("Modismo por contexto", ADULT + "«The test was a piece of cake. I finished it in ten minutes.» (test = prueba, finished = terminé). ¿Qué significa a piece of cake aquí?", ["La segunda frase da una pista: terminó en diez minutos.", "Entonces la prueba fue fácil.", "No se habla de comida."], "Muy fácil"),
    ],
    [
        ("Traducir under the weather como «bajo el clima».", "Un modismo no se interpreta palabra por palabra.", "Busca la pista del contexto: el hablante se quedó en casa."),
        ("Decir do a decision o strong traffic.", "Se usa el verbo o el adjetivo que no suele acompañar a la palabra.", "Aprende make a decision y heavy traffic como una sola pieza."),
    ],
    [
        (ADULT + CAMP + " ¿A dónde viajaron los amigos? A) a la costa B) a la montaña", "A", "El guion dice a trip to the coast."),
        (ADULT + CAMP + " ¿Por qué llegaron tarde? A) por mucho tráfico B) porque perdieron el bus", "A", "El guion dice heavy traffic, so we arrived late."),
        (ADULT + TEST + " ¿Qué tiene que hacer el hablante porque la prueba es la próxima semana?", "Ponerse a estudiar", "Dice I have to hit the books."),
    ],
    [
        (ADULT + CAMP + " ¿Qué significa It was a piece of cake to find the hostel? A) fue muy fácil B) fue una comida", "A", "El hostal estaba en una calle muy clara."),
        (ADULT + CLUB + " ¿Qué hace el club antes de cada proyecto? A) toma una decisión juntos B) hace una fiesta", "A", "Dice we make a decision together before each project."),
        (ADULT + TEST + " ¿Qué significa under the weather? A) sentirse indispuesto B) estar en la lluvia", "A", "El hablante se quedó en casa el lunes; es una expresión para sentirse mal."),
    ],
    [
        (ADULT + CAMP + " ¿Qué tres cosas planearon para la noche? A) sacar fotos, hacer un picnic y mantenerse en contacto B) dormir, leer y cocinar", "A", "El guion dice take photos, have a picnic and keep in touch."),
        (ADULT + TEST + " ¿Qué hace el hablante en clase? A) presta atención y toma apuntes B) llega tarde", "A", "Dice I pay attention in class, and I take notes."),
        (ADULT + CLUB + " ¿Qué pasa once in a blue moon? A) muy rara vez no están de acuerdo B) siempre discuten", "A", "Once in a blue moon significa muy rara vez; luego dice we always find a solution."),
    ],
    [
        (ADULT + TEST + " El hermano dice que no es difícil. ¿Qué conector muestra que el hablante piensa distinto? A) but B) so", "A", "But introduce el contraste: it will not be a piece of cake for me."),
        (ADULT + CAMP + " ¿Qué frase del guion pertenece al vocabulario de viaje? A) caught an early bus B) hit the books", "A", "Caught an early bus habla de transporte; hit the books es de estudio."),
    ],
    [
        (ADULT + CLUB + " Marca la colocación incorrecta según el guion: A) do a presentation B) give a presentation", "A", "El guion usa give a presentation; do a presentation no es natural."),
        (ADULT + CAMP + " Un compañero dice que keep in touch significa guardar un objeto. ¿Qué significa en el guion? A) mantener contacto con la familia B) tocar el celular", "A", "El texto dice keep in touch with our families."),
    ],
    [(ADULT + "«It was a rainy day, so we stayed at home. I took a photo of the window and I sent it to my cousin. We decided to keep in touch every week.» (rainy = lluvioso, window = ventana, cousin = primo). ¿Con qué frecuencia decidieron mantener contacto?", "Cada semana", "El guion dice every week.")],
    [
        ("¿Qué es una colocación (collocation)?", "Una combinación de palabras que suena natural", "Por ejemplo, make a decision."),
        ("¿Qué significa a piece of cake?", "Algo muy fácil", "Es un modismo."),
        ("¿Cómo se dice en inglés «tomar apuntes»?", "Take notes", "Se usa take con notes."),
    ],
    task("Una persona adulta lee dos veces: «Yesterday was a busy day. I got up early, had breakfast and caught the bus. At school we gave a short presentation about our city. It was not a piece of cake, but my group made a good decision: we practised twice. After class, I felt under the weather, so I went home and took a rest.» (busy = ocupado, gave a presentation = hicimos una presentación, practised = practicamos, rest = descanso). En tu hoja escribe: tres collocations del guion, dos modismos y qué significa cada uno en español.", "Collocations: had breakfast, caught the bus, gave a presentation, made a decision, took a rest (cualquiera de tres). Modismos: not a piece of cake (no fue fácil) y under the weather (indispuesto).", ["anota tres collocations que sí aparecen", "anota los dos modismos del guion", "explica cada significado en español"], ["hoja con cinco expresiones", "nota de la persona que leyó"], ["inventar una expresión que no está en el guion", "traducir palabra por palabra"], "Revisa en el guion que cada expresión esté completa, con el verbo y su pareja."),
    "Pide que te lean otra vez el texto del club de robótica y subraya las collocations.",
    "Escribe cinco collocations con make y take, y una oración con cada una.",
)

# ================================================== clase 5: sonidos y cualidades de la voz
SOUNDS = "«Usually, the student takes two photos of the special display at the station.» (display = exhibición, station = estación)"

lesson(
    OA, 5, MAT,
    "Aprenderé a reconocer en un texto oral los sonidos /t/, /d/, /ʒ/, los grupos iniciales /sp/ y /st/ y la acentuación de palabras largas y compuestas. Sirve para entender mejor lo que oigo y para que me entiendan cuando hablo.",
    ["Sé leer palabras comunes en inglés.", "Sé que cada palabra tiene sílabas."],
    [
        "El sonido /t/ de to y el sonido /d/ de do son parecidos, pero se diferencian por la voz. Al decir /d/ hacen vibrar la garganta, y al decir /t/ inicial se suelta un poquito de aire. En inglés, la lengua toca la parte de arriba de la boca, detrás de los dientes. Dos palabras que cambian el sentido solo por /t/ o /d/ son tie y die, o town y down.",
        "El sonido /ʒ/ aparece en palabras como usually, television, decision y measure. Es un sonido suave, como una /sh/ con la garganta vibrando. Los grupos iniciales /sp/ y /st/ (special, student, speak, study) se dicen directamente: en español solemos agregar una e antes, pero en inglés no se dice «espesial» ni «estudent». Las dos consonantes se pronuncian juntas desde el inicio.",
        "La acentuación (stress) es la sílaba que suena más fuerte. En las palabras de dos o más sílabas hay una sílaba más fuerte: table (TA-ble), decide (de-CIDE), computer (com-PU-ter). En las palabras compuestas (compound words), el acento suele ir en la primera parte: BLACKboard, NOTEbook, CLASSroom. La entonación (intonation) y la fuerza de la voz muestran qué es importante en el mensaje.",
    ],
    [("stress", "acento: sílaba que suena más fuerte"), ("compound word", "palabra compuesta: dos palabras unidas"), ("/ʒ/", "sonido suave de usually y television"), ("/sp/, /st/", "grupos iniciales de special y student"), ("intonation", "entonación: subida y bajada de la voz")],
    [
        ("Sonido /ʒ/", "¿Cuál de estas palabras contiene el sonido /ʒ/? A) vision B) station", ["Pienso en el sonido suave del medio de vision.", "En vision se escucha /ʒ/, y en station se escucha /ʃ/ (sh).", "Entonces la respuesta es vision."], "A) vision"),
        ("Acento en palabra compuesta", "¿Dónde suena más fuerte la palabra compuesta notebook? A) en note B) en book", ["Las palabras compuestas suelen tener el acento al inicio.", "Se dice NOTEbook.", "El acento va en note."], "A) en note"),
    ],
    [
        ("Decir «estudent» o «espeak» al empezar una palabra.", "En español se agrega una e antes de s + consonante.", "Pronuncia /st/ y /sp/ juntos, sin vocal inicial."),
        ("Acentuar la segunda parte de una palabra compuesta.", "No se aplica la regla de las compuestas.", "Marca el acento en la primera parte: BLACKboard."),
    ],
    [
        (SOUNDS + " ¿Qué palabra de la oración contiene el sonido /ʒ/? A) usually B) display", "A", "Usually tiene /ʒ/ en la sílaba -su-."),
        (SOUNDS + " ¿Qué palabra comienza con el grupo /st/? A) student B) display", "A", "Student empieza con st; display empieza con /d/."),
        ("¿Qué palabra comienza con el grupo /sp/? A) special B) station", "A", "Special empieza con sp; station empieza con st."),
    ],
    [
        ("¿Cuál es la sílaba más fuerte en decide? A) la segunda: de-CIDE B) la primera: DE-cide", "A", "En decide el acento va en la segunda sílaba."),
        ("¿Cuál es la sílaba más fuerte en teacher? A) la primera: TEA-cher B) la segunda: tea-CHER", "A", "En teacher el acento va en la primera sílaba."),
        ("Un compañero dice «espesial» en vez de special. ¿Qué corrección corresponde? A) decirla sin e inicial B) agregar otra e", "A", "En inglés /sp/ se pronuncia junta, sin vocal antes."),
    ],
    [
        ("En la oración «The student does his homework», ¿qué palabra comienza con /d/? A) does B) homework", "A", "Does comienza con /d/; homework comienza con /h/."),
        ("¿Cuál de estas palabras compuestas lleva el acento en la primera parte? A) CLASSroom B) class-ROOM", "A", "La compuesta suena con acento en class."),
        ("Marca la palabra con sonido /ʒ/ en «Today I watch television at home»: A) television B) watch", "A", "Television contiene /ʒ/ en -vi-."),
    ],
    [
        ("Pablo dice que tie y die suenan igual. ¿Qué diferencia hay? A) tie empieza con /t/ y die con /d/; cambia el significado B) no hay diferencia", "A", "El sonido inicial cambia el significado: corbata y morir."),
        ("En un aviso se dice con mucha fuerza la palabra NOW: «Come NOW!». ¿Qué comunica la fuerza de la voz? A) que es urgente B) que es una pregunta", "A", "El énfasis marca la palabra importante, now, y señala urgencia."),
    ],
    [
        ("Une cada palabra con su acento: 1) computer 2) tomorrow 3) classroom. Acentos: a) com-PU-ter b) to-MOR-row c) CLASS-room", "1-a, 2-b, 3-c", "Computer y tomorrow suenan fuerte en la segunda sílaba; classroom, en la primera."),
        ("¿Qué palabra tiene el sonido /ʒ/: «measure» o «music»? Escribe la que lo tiene.", "measure", "En measure el medio suena /ʒ/; en music, no."),
    ],
    [("Una guía de museo dice: «Today we have a special exhibition for students.» ¿Cuáles son las dos palabras que comienzan con /sp/ o /st/? Escríbelas.", "special y students", "Special empieza con sp y students con st.")],
    [
        ("¿Qué letra no se agrega antes de /sp/ o /st/ en inglés?", "La e", "En español se agrega, pero en inglés no."),
        ("¿Dónde va el acento en una palabra compuesta como notebook?", "En la primera parte", "Se dice NOTEbook."),
        ("¿Qué sonido tiene usually en el medio?", "/ʒ/", "Es un sonido suave con la garganta vibrando."),
    ],
    task("Una persona adulta lee en voz alta, dos veces, esta frase: «Usually, the student studies in the classroom after the special lesson.» En tu hoja haz tres cosas: 1) escribe las palabras que comienzan con /st/ o /sp/; 2) escribe la palabra con /ʒ/; 3) escribe la palabra compuesta y marca en mayúsculas su sílaba más fuerte. Luego léela tú en voz alta.", "1) student, studies, special. 2) usually. 3) classroom: CLASSroom.", ["escribe las tres palabras con /st/ o /sp/", "identifica la palabra con /ʒ/", "marca el acento de la palabra compuesta"], ["hoja con tres respuestas", "nota de la persona que escuchó"], ["agregar una e inicial al leer student", "acentuar room en vez de class"], "Pide a la persona que escuche tu lectura y te diga si pronunciaste student sin e.")
    ,
    "Repite en voz alta diez veces special, student, speak y study sin agregar una e al principio.",
    "Busca en un texto corto cinco palabras de dos sílabas y marca en cada una la sílaba más fuerte.",
)
