"""Cuaderno del estudiante, 7.º básico Inglés (oficial), IN07 OA 03 (tema, información específica, pasos, secuencia,
hecho y opinión, causa y efecto en textos escuchados). Las «escuchas» las lee un adulto; los textos son originales.
"""
from __future__ import annotations

from student_content_in7_a import ADULT, arith, lesson, task

OA3 = "IN07 OA 03"
MAT = "Un adulto lee en voz alta cada texto escrito en los ejercicios; una hoja para tapar el guion y lápiz."

DINO = "«Welcome to the dinosaur room. Please stay behind the yellow line. Here you can see a model of a big skeleton, a map of old rivers and some fossils. The guided tour starts in five minutes at the entrance.» (dinosaur = dinosaurio, skeleton = esqueleto, fossils = fósiles, guided tour = visita guiada, entrance = entrada)"
VET = "«Receptionist: Good afternoon. How can I help you? Mr. Pérez: My dog Rocky doesn't eat and he sleeps all day. Receptionist: Take a seat, please. The vet will see you in ten minutes. Mr. Pérez: Thank you.» (receptionist = recepcionista, vet = veterinaria, take a seat = tome asiento)"
SKATE = "«On Sunday, Lucas and his sister Emma go to the skate park near the river. Lucas rides his skateboard, and Emma takes photos with her phone. Their friend Diego brings a small ramp made of wood. At five o'clock, they eat apples under a big tree.» (skate park = pista de skate, skateboard = patineta, takes photos = saca fotos, ramp = rampa, wood = madera, apples = manzanas)"
CHESS = "«Mrs. Alvarez teaches the chess club in room 5 on Mondays at four. Two students, Pía and Joaquín, set up the boards. A new student, Tadeo, learns how the knight moves. Mr. Torres, the principal, visits for ten minutes and says: Good work!» (chess = ajedrez, teaches = enseña, set up = preparan, boards = tableros, knight = caballo, principal = director, visits = visita)"
PICNIC = "«Last Saturday, the school picnic was not outdoors. It rained all morning, so the teachers moved the picnic to the gym. The students were happy because they could play indoor games. The sandwiches were cold, but everybody still enjoyed the party.» (picnic = picnic, outdoors = al aire libre, rained = llovió, gym = gimnasio, indoor = bajo techo, sandwiches = sándwiches, enjoyed = disfrutó)"
BOOKMARK = "«How to make a bookmark. First, take a piece of colored card. Second, ask an adult to cut a long strip. Third, draw a pattern on it. Next, ask an adult to make a small hole at the top. Finally, tie a ribbon through the hole.» (bookmark = marcapáginas, card = cartulina, strip = tira, pattern = diseño, hole = agujero, ribbon = cinta, tie = amarrar)"
JUICE = "«Try Fresh Juice Bar! Our orange juice is the tastiest in the city. It costs only two thousand pesos. We are open every day from eight in the morning to eight at night.» (juice bar = juguería, tastiest = el más rico, costs = cuesta, only = solo, open = abierto)"
LIBRARY = "«I think the new library is wonderful. It has three floors and about ten thousand books. In my opinion, the quiet room is the best place to read. It opens at nine.» (library = biblioteca, floors = pisos, opinion = opinión, quiet = silencioso, opens = abre)"
ADVICE = "«You should drink water before the match. Also, don't eat a big meal just before playing. These tips help you feel good.» (should = deberías, match = partido, meal = comida, tips = consejos)"
HIKE = "«Good morning, hikers. Today's walk is easy, so you do not need special shoes. Take a hat because the sun is strong at noon. We meet at the parking lot at nine and return at two o'clock. Please do not leave rubbish on the trail.» (hikers = excursionistas, hat = sombrero, noon = mediodía, parking lot = estacionamiento, rubbish = basura, trail = sendero)"
NEWKID = "«Teacher: Class, we have a new student today. His name is Kenji, and he is from Japan. He speaks Japanese and a little English. Please be kind and help him find his locker. Student: Can I show him the library, too? Teacher: Yes, thank you, Camila.» (new student = estudiante nuevo, Japan = Japón, kind = amable, locker = casillero)"
CONCERT = "«Reporter: How was the concert? Fan: It was fantastic! The singer arrived on time, the sound was clear, and the lights were beautiful. But the tickets were expensive.» (reporter = reportero, fan = admirador, singer = cantante, sound = sonido, clear = claro, lights = luces, tickets = entradas, expensive = caras)"

# ------------------------------------------------------------------ clase 1
lesson(
    OA3, 1, MAT,
    "Aprenderé a identificar el tema y la situación de un texto oral: de qué se habla, quién habla, dónde y para qué. Sirve para organizar lo que escucho antes de buscar detalles.",
    ["Sé reconocer la idea general de un texto.", "Conozco palabras como museum, dog, ticket y room."],
    [
        "El tema (topic) es de qué trata un texto en una frase corta: una sala de dinosaurios, la salud de una mascota o un partido de fútbol. La situación (situation) es el contexto de la comunicación: quién habla, con quién, dónde y para qué. Un guía de museo que habla con visitantes es una situación; una recepcionista que atiende a un cliente en una clínica veterinaria es otra.",
        "Para identificarlos, escucha la primera parte y busca palabras clave que se repitan o que pertenezcan al mismo campo. Skeleton, fossils y dinosaur apuntan a un museo. Dog, vet y sleeps all day apuntan a la salud de un perro. Luego pregunta: ¿quién habla?, ¿a quién?, ¿en qué lugar? Frases como Welcome to... o How can I help you? suelen mostrar el rol de quien habla.",
        "No confundas el tema con un detalle. En la sala de dinosaurios se nombra un mapa de ríos antiguos, pero el tema no es el río, es la sala y lo que se puede ver en ella. El tema reúne la mayoría de las palabras clave. Un detalle es solo una pieza de esa información.",
    ],
    [("topic", "tema: de qué trata el texto"), ("situation", "situación: quién habla, dónde y para qué"), ("guide", "guía: persona que explica un lugar"), ("vet", "veterinaria o veterinario"), ("key word", "palabra clave"), ("welcome", "bienvenidos")],
    [
        ("Tema y situación", ADULT + DINO + " ¿Cuál es el tema y quién habla?", ["Escucho skeleton, fossils y dinosaur room.", "Welcome to... lo dice alguien que recibe visitantes.", "El tema es la sala de dinosaurios y quien habla es un guía."], "El tema es la sala de dinosaurios de un museo; habla un guía"),
        ("Situación por el lugar", ADULT + VET + " ¿Dónde ocurre la conversación y cuál es el problema?", ["Hay una receptionist y un vet.", "Es la recepción de una clínica veterinaria.", "Rocky no come y duerme todo el día."], "En una clínica veterinaria; el perro no come y duerme todo el día"),
    ],
    [
        ("Elegir como tema un objeto que solo se nombra una vez.", "Se confunde un detalle con el tema.", "Elige el tema que reúne la mayoría de las palabras clave."),
        ("Olvidar quién habla.", "Se escucha el contenido pero no el rol de la persona.", "Pregunta siempre: ¿quién habla y a quién?"),
    ],
    [
        (ADULT + DINO + " ¿Cuál es el tema? a) una sala de dinosaurios en un museo b) un partido de fútbol", "a) una sala de dinosaurios en un museo", "Dice dinosaur room, skeleton y fossils."),
        (ADULT + VET + " ¿Cuál es la situación? a) un perro enfermo en una clínica veterinaria b) una clase de cocina", "a) un perro enfermo en una clínica veterinaria", "Aparecen receptionist, vet y dog."),
        (ADULT + DINO + " ¿Quién habla? a) un guía del museo b) un cocinero", "a) un guía del museo", "Da la bienvenida y avisa de la visita guiada."),
    ],
    [
        (ADULT + DINO + " ¿Cuántos objetos de la sala nombra el guía: un esqueleto, un mapa y unos fósiles?", "3", "Se nombran un modelo de esqueleto, un mapa y unos fósiles."),
        (ADULT + VET + " ¿Dónde ocurre la conversación? a) en una veterinaria b) en un supermercado", "a) en una veterinaria", "La recepcionista habla de the vet."),
        (ADULT + VET + " ¿Cuál es el problema del perro?", "No come y duerme todo el día", "Mr. Pérez dice doesn't eat and sleeps all day."),
    ],
    [
        (ADULT + "«Please fasten your seat belts. We are going to land in twenty minutes.» (fasten = abrochar, seat belts = cinturones, land = aterrizar). ¿Dónde ocurre la situación? a) en un avión b) en una piscina", "a) en un avión", "Land y seat belts son palabras de viaje en avión."),
        (ADULT + DINO + " ¿Dónde empieza la visita guiada?", "En la entrada", "Dice The guided tour starts at the entrance."),
        (ADULT + "«Today I will explain how rain is made. First, the sun heats the sea. Then the water goes up as vapor.» (rain = lluvia, heats = calienta, vapor = vapor). ¿Cuál es el tema? a) cómo se forma la lluvia b) cómo hacer una torta", "a) cómo se forma la lluvia", "Las palabras rain, sun, sea y water son del mismo tema."),
    ],
    [
        ("Ana dice que el tema de la sala de dinosaurios es un río porque se nombra un mapa de ríos. ¿Tiene razón? Responde sí o no.", "No", "El mapa de ríos es un detalle; el tema es la sala y lo que se ve."),
        (ADULT + VET + " ¿Cuál es la mejor descripción del tema? a) la salud de una mascota b) la compra de comida para perros c) un paseo por el parque", "a) la salud de una mascota", "Rocky no come y la recepcionista habla del veterinario."),
    ],
    [
        (ADULT + "«And the striker runs, shoots, and it is a goal! The crowd shouts and the team celebrates.» (striker = delantero, shoots = dispara, crowd = público, celebrates = celebra). ¿Qué situación es? a) una transmisión de un partido b) una clase de matemática", "a) una transmisión de un partido", "Goal, striker y crowd son palabras de fútbol."),
        (ADULT + DINO + " ¿En cuántos minutos empieza la visita guiada?", "5", "Dice starts in five minutes."),
    ],
    [(ADULT + "En el museo, el guía dice: «Please stay behind the yellow line.» (stay = quédense, behind = detrás de, line = línea). Si te acercas a un fósil, ¿qué regla rompes?", "Quedarse detrás de la línea amarilla", "Esa es la regla que da el guía.")],
    [
        ("En Inglés de 7.º (OA 3, clase 1): ¿Qué es el tema de un texto?", "De qué trata el texto", "Reúne la mayoría de las palabras clave."),
        ("¿Qué incluye la situación?", "Quién habla, a quién, dónde y para qué", "Es el contexto de la comunicación."),
        ("En Inglés de 7.º (OA 3, clase 1): ¿Qué es un detalle?", "Un dato que apoya el tema", "No es lo más importante."),
    ],
    task("Un adulto lee dos veces este texto: «Attention, passengers. The bus to La Serena leaves from platform four at six thirty. Please keep your tickets ready. Please put your luggage in the bottom of the bus.» (passengers = pasajeros, platform = andén, tickets = pasajes, luggage = equipaje, put = poner, bottom = parte baja). Escribe en tu hoja el tema, quién habla, dónde y para qué.", "Tema: la salida de un bus. Habla un encargado del terminal, en el terminal de buses, para avisar a los pasajeros.", ["indica un tema", "indica quién habla", "indica lugar y propósito"], ["hoja con cuatro respuestas", "nota del adulto"], ["decir que el tema es el equipaje", "no indicar quién habla"], "Reconoce lo que acertó y repasa con la persona adulta qué palabras clave se repiten en el aviso."),
    "Pide a un adulto que lea el texto de la veterinaria y di en una frase el tema y la situación.",
    "Escribe dos frases en inglés que describan una situación, por ejemplo en una panadería, y di quién habla y dónde.",
)

# ------------------------------------------------------------------ clase 2
lesson(
    OA3, 2, MAT,
    "Aprenderé a ubicar información específica sobre personas, lugares, tiempo y acciones. Sirve para responder preguntas con exactitud: quién, dónde, cuándo y qué hace cada uno.",
    ["Sé reconocer el tema de un texto oral.", "Conozco los días de la semana y las horas en inglés."],
    [
        "La información específica (specific information) es el dato exacto que responde una pregunta. Who pregunta por personas, where por lugares, when por el tiempo y what por acciones o cosas. Antes de escuchar, lee la pregunta y decide cuál dato buscas. Eso enfoca tu atención y evita que te distraigas con otros datos.",
        "Para las personas, atiende a nombres y relaciones: his sister (su hermana), their friend (su amigo), the principal (el director). Para los lugares, atiende a frases como near the river, in room 5 o under a big tree. Para el tiempo, atiende a on Sunday, at five o'clock, on Mondays at four o'clock y for ten minutes. Para las acciones, atiende a los verbos: rides, takes, brings, teaches, learns.",
        "Un truco útil es anotar una tabla con tres columnas: quién, hace qué y dónde o cuándo. Así no mezclas los datos de dos personas. En el skate park, Lucas anda en patineta y Emma saca fotos. Si mezclas las acciones, tu respuesta será incorrecta aunque hayas oído todas las palabras.",
    ],
    [("who", "quién"), ("where", "dónde"), ("when", "cuándo"), ("what", "qué"), ("near", "cerca de"), ("under", "debajo de")],
    [
        ("Persona y acción", ADULT + SKATE + " ¿Quién saca fotos y con qué?", ["La pregunta pide una persona y una cosa.", "Busco takes photos.", "Dice Emma takes photos with her phone."], "Emma, con su teléfono"),
        ("Lugar y tiempo", ADULT + CHESS + " ¿Dónde y cuándo se reúne el club?", ["Busco room y la hora.", "Dice in room 5 on Mondays at four.", "Son lugar y tiempo."], "En la sala 5, los lunes a las 4"),
    ],
    [
        ("Mezclar las acciones de dos personas.", "Se oyen los verbos, pero no se asocian al nombre.", "Anota una tabla con quién, hace qué y dónde."),
        ("Responder con un dato que no corresponde a la pregunta (un lugar cuando piden un tiempo).", "No se lee bien la palabra interrogativa.", "Subraya who, where, when o what antes de escuchar."),
    ],
    [
        (ADULT + SKATE + " ¿Quién saca fotos? a) Emma b) Lucas", "a) Emma", "Dice Emma takes photos with her phone."),
        (ADULT + SKATE + " ¿Dónde está la pista de skate?", "Cerca del río", "Dice near the river."),
        (ADULT + SKATE + " ¿Qué día van? a) el domingo b) el sábado", "a) el domingo", "Dice On Sunday."),
    ],
    [
        (ADULT + CHESS + " ¿Dónde se reúne el club de ajedrez? a) en la sala 5 b) en la sala 4", "a) en la sala 5", "Dice in room 5; four es la hora."),
        (ADULT + CHESS + " ¿Quién aprende cómo se mueve el caballo?", "Tadeo", "Dice A new student, Tadeo, learns how the knight moves."),
        (ADULT + CHESS + " ¿Cuántos minutos visita el director?", "10", "Dice visits for ten minutes."),
    ],
    [
        (ADULT + SKATE + " ¿Dónde comen manzanas? a) debajo de un árbol grande b) sobre la rampa", "a) debajo de un árbol grande", "Dice under a big tree."),
        (ADULT + CHESS + " ¿Cuántos estudiantes se nombran en el texto, sin contar a la profesora ni al director?", "3", "Se nombran Pía, Joaquín y Tadeo."),
        (ADULT + SKATE + " ¿A qué hora comen manzanas? a) a las cinco b) a las seis", "a) a las cinco", "Dice At five o'clock."),
    ],
    [
        (ADULT + SKATE + " Un compañero dice que Diego saca fotos. ¿Qué frase del texto lo contradice?", "Emma takes photos", "Quien saca las fotos es Emma."),
        (ADULT + CHESS + " ¿Qué hace la señora Alvarez? a) enseña ajedrez b) prepara los tableros", "a) enseña ajedrez", "Los tableros los prepara Pía y Joaquín."),
    ],
    [
        (ADULT + SKATE + " ¿Cuántas personas hay en el parque de skate?", "3", "Están Lucas, Emma y Diego."),
        (ADULT + CHESS + " Imagina que el club empieza a las 4:00, que el director llega 20 minutos después y que se queda 10 minutos. ¿A qué hora se va?", "A las 4:30", "4:00 más 20 minutos es 4:20, y más 10 minutos son las 4:30."),
    ],
    [(ADULT + "En el parque de skate, un guardia dice: «The park is open on Saturday and Sunday. Helmets are required. Skaters under ten need an adult with them.» (open = abierto, helmets = cascos, required = obligatorios, skaters = patinadores, need = necesitan). ¿Qué debes usar siempre?", "Un casco", "Dice Helmets are required.")],
    [
        ("¿Qué pregunta se usa para preguntar por personas?", "Who", "Who significa quién."),
        ("¿Qué pregunta se usa para preguntar por lugares?", "Where", "Where significa dónde."),
        ("¿Qué te ayuda a no mezclar datos de dos personas?", "Una tabla de quién, hace qué y dónde", "Organiza los datos por persona."),
    ],
    task("Un adulto lee dos veces este texto: «On Friday, Marta and her brother Sebastián go to the market near the station. Marta buys tomatoes, and Sebastián buys bread. Their neighbor, Mrs. Rojas, sells flowers. At noon, they all have lunch in the square.» (market = feria, station = estación, buys = compra, bread = pan, neighbor = vecina, sells = vende, square = plaza). Haz una tabla con quién, hace qué, dónde y cuándo para cada personaje.", "Marta compra tomates en la feria el viernes. Sebastián compra pan. La señora Rojas vende flores. Al mediodía almuerzan en la plaza.", ["incluye a tres personajes", "une cada acción con su persona", "anota lugares y tiempos"], ["tabla en la hoja", "nota del adulto"], ["decir que Sebastián compra tomates", "olvidar la hora del almuerzo"], "Reconoce lo que acertó y vuelve a escuchar solo el verbo de cada persona."),
    "Pide a un adulto que lea el texto del club de ajedrez y señala en tu tabla quién hace cada acción.",
    "Escribe en inglés tres frases que digan quién hace qué en tu casa, usando nombres inventados y un lugar en cada frase.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA3, 3, MAT,
    "Aprenderé a reconocer causa y efecto, pasos en una secuencia y contrastes en un texto oral. Sirve para entender por qué ocurrió algo, en qué orden y en qué se diferencian dos cosas.",
    ["Sé el significado de first, next, finally, because y but.", "Sé seguir un orden de hechos."],
    [
        "La causa (cause) es la razón por la que algo pasa y el efecto (effect) es lo que pasó. Because (porque) introduce la causa: the students were happy because they could play indoor games. So (por eso) introduce el efecto: it rained all morning, so the teachers moved the picnic. Si preguntas «¿por qué?», la respuesta es la causa.",
        "Una secuencia (sequence) es un orden de pasos o hechos. En instrucciones, los pasos se marcan con first, second, third, next y finally. Para un procedimiento, escucha cuántos pasos hay y qué se hace en cada uno. Si te saltas un paso, el resultado cambia. Además, algunos pasos exigen ayuda de un adulto, como cortar o hacer un agujero.",
        "Un contraste (contrast) muestra una diferencia o algo inesperado. But (pero) es la palabra clave: the sandwiches were cold, but everybody still enjoyed the party. Se dice una idea y luego otra que la corrige o se opone. Presta atención a lo que viene después de but, porque suele ser lo más importante.",
    ],
    [("cause", "causa: la razón"), ("effect", "efecto: lo que pasó"), ("so", "por eso"), ("sequence", "secuencia: orden de pasos"), ("but", "pero: marca contraste"), ("step", "paso")],
    [
        ("Causa y efecto", ADULT + PICNIC + " ¿Por qué se trasladó el picnic al gimnasio?", ["Busco so y because.", "Dice It rained all morning, so the teachers moved the picnic.", "La causa es la lluvia."], "Porque llovió toda la mañana"),
        ("Pasos de un procedimiento", ADULT + BOOKMARK + " ¿Qué se hace en el tercer paso?", ["Cuento los conectores: First, Second, Third.", "Third dice draw a pattern on it.", "Es dibujar un diseño."], "Dibujar un diseño"),
    ],
    [
        ("Poner la causa en el lugar del efecto.", "No se identifica qué viene después de because.", "La causa es lo que viene después de because; el efecto es lo que pasó."),
        ("Olvidar el contraste después de but.", "Se escucha solo la primera idea.", "Atiende a lo que sigue a but."),
    ],
    [
        (ADULT + PICNIC + " ¿Por qué cambió el lugar del picnic? a) porque llovió toda la mañana b) porque faltaban sándwiches", "a) porque llovió toda la mañana", "La causa es It rained all morning."),
        (ADULT + PICNIC + " ¿A dónde se trasladó el picnic?", "Al gimnasio", "Dice moved the picnic to the gym."),
        (ADULT + BOOKMARK + " ¿Qué se hace primero? a) tomar un trozo de cartulina de color b) amarrar una cinta", "a) tomar un trozo de cartulina de color", "First, take a piece of colored card."),
    ],
    [
        (ADULT + PICNIC + " ¿Qué palabra marca el efecto de la lluvia? a) so b) but", "a) so", "So introduce la consecuencia."),
        (ADULT + PICNIC + " ¿Qué palabra marca el contraste entre los sándwiches fríos y la fiesta? a) but b) because", "a) but", "But opone las dos ideas."),
        (ADULT + BOOKMARK + " ¿Qué dos pasos requieren ayuda de un adulto?", "Cortar la tira y hacer el agujero", "Los dos pasos dicen ask an adult."),
    ],
    [
        (ADULT + BOOKMARK + " Ordena los pasos. A) Dibujar el diseño. B) Amarrar la cinta. C) Pedir que corten una tira.", "C, A, B", "El texto sigue el orden second, third y finally."),
        (ADULT + BOOKMARK + " ¿Cuántos pasos tiene el procedimiento?", "5", "Los pasos son first, second, third, next y finally."),
        (ADULT + PICNIC + " ¿Qué efecto tuvo la lluvia en el juego? a) los estudiantes jugaron juegos bajo techo b) se canceló todo", "a) los estudiantes jugaron juegos bajo techo", "Dice they could play indoor games."),
    ],
    [
        (ADULT + "«Pedro likes summer, but Ana prefers winter.» (prefers = prefiere). ¿A quién le gusta más el invierno?", "A Ana", "But marca el contraste y Ana prefiere winter."),
        (ADULT + PICNIC + " Un compañero dice que los sándwiches estaban calientes. ¿Qué frase del texto lo contradice?", "The sandwiches were cold", "El texto dice que estaban fríos."),
    ],
    [
        (ADULT + "«Because Tomás forgot his umbrella, he got wet.» (forgot = olvidó, umbrella = paraguas, got wet = se mojó). ¿Cuál es la causa? a) olvidó su paraguas b) se mojó", "a) olvidó su paraguas", "La causa va después de because; lo que ocurrió es el efecto."),
        (ADULT + "«The bus was late, so I walked.» (late = tarde, walked = caminé). ¿Qué ocurrió primero? a) el bus llegó tarde b) caminé", "a) el bus llegó tarde", "Es la causa; caminar es el efecto."),
    ],
    [(ADULT + "En la cocina, un adulto lee: «First, wash your hands. Next, ask an adult to put the pasta in hot water. Finally, ask an adult to drain it.» (wash = lavar, pasta = pasta, hot water = agua caliente, drain = escurrir). Si alguien se salta el primer paso, ¿qué olvidó hacer?", "Lavarse las manos", "El primer paso es wash your hands.")],
    [
        ("¿Qué introduce la causa?", "Because", "Because significa porque en español."),
        ("¿Qué palabra marca un contraste?", "But", "But significa pero en español."),
        ("¿Qué palabras marcan los pasos de una secuencia?", "First, second, next y finally", "Ordenan las acciones."),
    ],
    task("Un adulto lee dos veces este texto: «Last week, the school match was cancelled because the field was wet. Instead, the students watched a video about football, but they wanted to play. So the next day, the teacher gave them a short indoor game.» (cancelled = suspendido, field = cancha, wet = mojada, instead = en vez de, wanted = querían, short = breve). Escribe una causa, un efecto y un contraste del texto.", "Causa: la cancha estaba mojada. Efecto: se suspendió el partido. Contraste: querían jugar pero vieron un video.", ["identifica una causa", "identifica un efecto", "identifica un contraste"], ["hoja con tres respuestas", "nota del adulto"], ["invertir causa y efecto", "no usar but como pista"], "Reconoce lo que acertó y repasa con la persona adulta qué palabra marca cada relación."),
    "Pide a un adulto que lea el procedimiento del marcapáginas y toca la mesa una vez por cada paso.",
    "Escribe en tu hoja cinco pasos en inglés para preparar una bebida fría, usando first, next y finally.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA3, 4, MAT,
    "Aprenderé a inferir con cuidado el propósito de quien habla y a diferenciar hechos de opiniones. Sirve para no creer todo lo que se dice y entender qué quiere lograr el hablante.",
    ["Sé reconocer el propósito de un texto oral.", "Conozco palabras como think, best y wonderful."],
    [
        "Un hecho (fact) se puede comprobar: it has three floors, it costs two thousand pesos, it opens at nine. Una opinión (opinion) es lo que alguien piensa o siente, y no se puede comprobar de la misma manera: wonderful, tastiest, the best place. Las opiniones suelen llevar adjetivos como wonderful, boring o delicious, y frases como I think... o In my opinion...",
        "El propósito (purpose) es lo que el hablante quiere lograr: informar, convencer, aconsejar o contar. Un anuncio como Try Fresh Juice Bar! busca convencerte de ir. You should drink water busca aconsejar. Para inferir con cuidado (cautiously), usa pistas del texto: verbos como try, you should, don't, y también el tipo de lenguaje. Si no hay suficientes pistas, no afirmes demasiado.",
        "Los anuncios mezclan hechos y opiniones. El precio y el horario son hechos; que el jugo sea el más rico es una opinión de quien lo vende. Aprende a separarlos: cuando oigas un adjetivo muy positivo, pregúntate si se puede medir. Una opinión personal puede ser válida, pero no demuestra que todos piensen igual.",
    ],
    [("fact", "hecho: se puede comprobar"), ("opinion", "opinión: lo que alguien piensa"), ("purpose", "propósito: lo que se quiere lograr"), ("advice", "consejo"), ("should", "deberías"), ("I think", "yo pienso, creo")],
    [
        ("Separar hecho y opinión", ADULT + JUICE + " ¿«It costs only two thousand pesos» es un hecho o una opinión?", ["Me pregunto si se puede comprobar.", "Se puede ver el precio en la lista.", "Es un hecho."], "Un hecho"),
        ("Propósito del anuncio", ADULT + JUICE + " ¿Qué quiere lograr el anuncio?", ["Empieza con Try Fresh Juice Bar!.", "Dice que su jugo es el más rico.", "Quiere convencerte de ir a la juguería."], "Convencer a los oyentes de ir a la juguería"),
    ],
    [
        ("Creer que una opinión es un hecho porque suena segura.", "Las palabras fuertes no hacen que algo sea comprobable.", "Pregunta si se puede medir o comprobar."),
        ("Afirmar el propósito sin pistas.", "Se adivina en vez de usar el texto.", "Apóyate en verbos como try o should."),
    ],
    [
        (ADULT + JUICE + " ¿Cuál es el propósito del anuncio? a) convencer b) contar una historia", "a) convencer", "Usa Try y dice que su jugo es el más rico."),
        (ADULT + JUICE + " ¿«The tastiest in the city» es un hecho o una opinión? a) una opinión b) un hecho", "a) una opinión", "Lo más rico depende del gusto de cada persona."),
        (ADULT + ADVICE + " ¿Cuál es el propósito del texto? a) aconsejar b) vender", "a) aconsejar", "Usa You should y tips."),
    ],
    [
        (ADULT + LIBRARY + " ¿Qué frase avisa que viene una opinión? a) I think b) it has three floors", "a) I think", "I think significa yo pienso."),
        (ADULT + LIBRARY + " ¿Cuántos pisos tiene la biblioteca?", "3", "Es un hecho: three floors."),
        (ADULT + ADVICE + " ¿Qué se aconseja hacer antes del partido?", "Tomar agua", "Dice drink water before the match."),
    ],
    [
        (ADULT + LIBRARY + " Clasifica. A) It has three floors. B) The quiet room is the best place to read. C) It opens at nine. ¿Cuáles son hechos?", "A y C", "Se pueden comprobar; B es una opinión."),
        arith(ADULT + JUICE + " ¿Cuántas horas al día abre la juguería, de ocho de la mañana a ocho de la noche?", "20-8", "Las ocho de la noche son las 20 horas; se resta la hora de apertura.", " horas"),
        (ADULT + ADVICE + " ¿Qué no se debe hacer justo antes de jugar? a) comer mucho b) tomar agua", "a) comer mucho", "Dice don't eat a big meal just before playing."),
    ],
    [
        ("Un compañero dice «I love this song» (me encanta esta canción). ¿Podemos concluir que a todos les gusta? Responde sí o no.", "No", "Es una opinión personal y no prueba lo que piensan los demás."),
        (ADULT + JUICE + " ¿Qué frase muestra que el anuncio quiere que vayas? a) Try Fresh Juice Bar! b) Open every day", "a) Try Fresh Juice Bar!", "Try es una invitación a probar."),
    ],
    [
        (ADULT + "«Honestly, the film was boring, and the seats were uncomfortable.» (honestly = sinceramente, film = película, boring = aburrida, seats = asientos, uncomfortable = incómodos). ¿Cuántas opiniones hay?", "2", "Boring y uncomfortable son opiniones."),
        ("¿«Santiago is the capital of Chile» es un hecho o una opinión? a) un hecho b) una opinión", "a) un hecho", "Se puede comprobar en un mapa."),
    ],
    [(ADULT + "Un amigo dice: «This pizza is delicious. It has cheese, tomato and basil, and it costs five thousand pesos.» (cheese = queso, tomato = tomate, basil = albahaca). Separa en una frase la opinión y el hecho de precio.", "Opinión: es deliciosa; hecho: cuesta 5.000 pesos", "Delicious es lo que opina; el precio se puede comprobar.")],
    [
        ("En Inglés de 7.º (OA 3, clase 4): ¿Qué es un hecho?", "Algo que se puede comprobar", "Un hecho es verificable."),
        ("En Inglés de 7.º (OA 3, clase 4): ¿Qué frase anuncia una opinión?", "I think", "Significa yo pienso."),
        ("¿Para qué sirve «You should»?", "Para dar un consejo", "Should significa deberías."),
    ],
    task("Un adulto lee dos veces este texto: «Visit the Green Park Zoo! It is open from ten to five. Our parrots are the funniest animals in Chile. Tickets cost four thousand pesos. Come this Saturday!» (parrots = loros, funniest = los más divertidos, tickets = entradas). Escribe el propósito, dos hechos y una opinión.", "Propósito: convencer de ir al zoológico. Hechos: abre de 10 a 5; las entradas cuestan 4.000 pesos. Opinión: los loros son los animales más divertidos.", ["indica el propósito", "anota dos hechos", "anota una opinión"], ["hoja con tres respuestas", "nota del adulto"], ["anotar el precio como opinión", "no justificar el propósito"], "Reconoce lo que acertó y revisa con la persona adulta qué se puede comprobar en el texto."),
    "Pide a un adulto que lea otra vez el anuncio de la juguería y levanta la mano cuando oigas una opinión.",
    "Escribe un anuncio de tres frases en inglés para tu colegio, con dos hechos y una opinión.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA3, 5, MAT,
    "Aprenderé a apoyar una respuesta con dos pistas del texto oral. Sirve para demostrar que mi respuesta se basa en lo que escuché.",
    ["Sé ubicar datos específicos y reconocer causas y contrastes.", "Sé distinguir hechos de opiniones."],
    [
        "Una buena respuesta no basta con ser correcta: debe estar respaldada. Una pista (clue) es una palabra o frase del texto que sostiene tu respuesta. Dos pistas hacen la respuesta más sólida. Por ejemplo, para decir que la caminata es fácil puedes citar Today's walk is easy y you do not need special shoes.",
        "Sigue tres pasos. Primero, responde la pregunta. Segundo, busca en tu memoria o en tus apuntes la frase exacta que lo apoya. Tercero, busca una segunda pista que apunte en la misma dirección. Si las dos pistas se contradicen, revisa tu respuesta. Si no encuentras ninguna pista, puede que estés adivinando.",
        "Presta atención a las diferencias entre la información dicha directamente y la que se infiere. Si el texto dice please be kind and help him find his locker, no dice que Kenji esté asustado; eso sería suponer. Cita lo que el texto dice y evita agregar datos propios. Una respuesta con evidencia se escribe así: respuesta, porque dice... y también dice...",
    ],
    [("clue", "pista"), ("evidence", "evidencia"), ("support", "apoyar, respaldar"), ("because it says", "porque dice"), ("also", "también"), ("infer", "inferir: sacar una idea con pistas")],
    [
        ("Dos pistas", ADULT + HIKE + " ¿Es una caminata difícil? Responde con dos pistas.", ["Respondo que no es difícil.", "Primera pista: Today's walk is easy.", "Segunda pista: you do not need special shoes."], "No; pistas: Today's walk is easy y you do not need special shoes"),
        ("Pista que no apoya", ADULT + HIKE + " ¿Qué pista apoya que hace sol fuerte: «take a hat because the sun is strong» o «we meet at the parking lot»?", ["Busco una frase que hable del sol.", "La primera menciona the sun is strong.", "La segunda solo dice dónde se juntan."], "Take a hat because the sun is strong"),
    ],
    [
        ("Citar una pista que no tiene relación con la pregunta.", "Se elige una frase por ser corta o por recordarla.", "Comprueba que la pista hable del mismo tema que la respuesta."),
        ("Agregar datos que el texto no dice.", "Se mezcla lo que se oyó con lo que se imagina.", "Cita solo lo que dice el texto."),
    ],
    [
        (ADULT + HIKE + " ¿Qué debes llevar? a) un sombrero b) botas especiales", "a) un sombrero", "Dice Take a hat."),
        (ADULT + HIKE + " ¿A qué hora se reúnen?", "A las nueve", "Dice We meet at nine."),
        (ADULT + NEWKID + " ¿De dónde es Kenji?", "De Japón", "Dice he is from Japan."),
    ],
    [
        (ADULT + HIKE + " ¿Qué frase respalda la respuesta «la caminata es fácil»? a) Today's walk is easy b) the sun is strong", "a) Today's walk is easy", "Describe el nivel de dificultad."),
        (ADULT + NEWKID + " ¿Qué idiomas habla Kenji?", "Japonés y un poco de inglés", "Dice He speaks Japanese and a little English."),
        (ADULT + HIKE + " ¿Qué se pide que no se deje en el sendero?", "Basura", "Dice do not leave rubbish on the trail."),
    ],
    [
        (ADULT + HIKE + " ¿Se necesitan zapatos especiales? Responde sí o no y escribe la pista.", "No; dice you do not need special shoes", "La frase lo dice directamente."),
        (ADULT + NEWKID + " ¿Quién ofrece mostrarle la biblioteca a Kenji? a) Camila b) la profesora", "a) Camila", "Dice Can I show him the library, too? y la profesora le agradece a Camila."),
        arith(ADULT + HIKE + " ¿Cuántas horas dura la actividad, si empieza a las 9 y termina a las 14 horas?", "14-9", "Se resta la hora de inicio a la de término.", " horas"),
    ],
    [
        (ADULT + NEWKID + " La profesora quiere que traten bien a Kenji. Escribe las dos frases que lo muestran.", "Please be kind; help him find his locker", "Las dos son pedidos de ayuda y amabilidad."),
        (ADULT + HIKE + " Un compañero dice que no hace falta nada para el sol. ¿Qué pista lo contradice?", "Take a hat because the sun is strong at noon", "Pide un sombrero por el sol."),
    ],
    [
        (ADULT + CONCERT + " ¿Cuántos aspectos positivos menciona el admirador?", "3", "Dice que el cantante llegó a tiempo, el sonido fue claro y las luces fueron bonitas."),
        (ADULT + CONCERT + " ¿Qué palabra introduce el problema? a) but b) so", "a) but", "But marca el contraste con lo positivo y presenta el problema de las entradas."),
    ],
    [(ADULT + "Un vecino te pregunta si necesita sombrero en la caminata. Responde con una pista. Texto: " + HIKE, "Sí; dice take a hat because the sun is strong", "El guía lo pide por el sol fuerte.")],
    [
        ("¿Qué es una pista?", "Una palabra o frase del texto que respalda mi respuesta", "Sirve de evidencia."),
        ("¿Qué haces si dos pistas se contradicen?", "Reviso mi respuesta", "Una respuesta con pistas contradictorias puede ser incorrecta."),
        ("¿Qué no debes hacer al responder con evidencia?", "Agregar datos que el texto no dice", "La evidencia debe venir del texto."),
    ],
    task("Un adulto lee dos veces este texto: «Hello, I'm your guide at the botanical garden. The garden is big, so walk slowly. You can touch the leaves, but please do not pick the flowers. The flowers are for everyone to enjoy. The cafe near the exit has hot chocolate and cake.» (botanical garden = jardín botánico, slowly = despacio, leaves = hojas, pick = cortar, enjoy = disfrutar, exit = salida). Responde: ¿se pueden cortar las flores? Escribe tu respuesta y dos pistas que la apoyen.", "No. Pistas: please do not pick the flowers; the flowers are for everyone to enjoy.", ["responde con claridad", "cita dos pistas del texto", "no agrega datos propios"], ["hoja con respuesta y dos pistas", "nota del adulto"], ["citar la cafetería como pista", "no citar ninguna pista"], "Reconoce lo que acertó y revisa con la persona adulta cuál frase habla de las flores."),
    "Pide a un adulto que lea otra vez el texto de la caminata y subraya en tu hoja dos pistas para una de las respuestas.",
    "Escribe tres preguntas sobre el texto del concierto y, para cada una, anota la respuesta y su pista.",
)
