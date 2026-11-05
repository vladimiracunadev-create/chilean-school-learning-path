"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 03: propósito, ideas relevantes, detalles y problema-solución al escuchar.

Las «escuchas» las lee un adulto: el guion va escrito en el enunciado. Textos originales (inglés americano, datos ficticios).
Los títulos de clase del plan son genéricos; aquí se aplican a propósito y tema, información específica, importancia y
problema-solución, hablantes y situaciones, y ficha integrada de escucha.
"""
from __future__ import annotations

from in_m2_common import ADULT, MAT_L, arith, lesson, mc, ml, mr, task

OA = "IN2M OA 03"

# ------------------------------------------------------------------ clase 1: propósito, tema e idea general
W1 = "«Good evening. Today I want to tell you about a tool library. In some towns, people can borrow hammers, ladders and drills for free, just like books. This helps families save money, and it keeps many tools from sitting unused in garages.» (tool library = biblioteca de herramientas, borrow = pedir prestado, ladders = escaleras, drills = taladros, unused = sin usar, garages = garajes)"
W2 = "«Do you want to practice English or Spanish? Join our language exchange café every Thursday at seven. Meet people from many countries, enjoy something hot and talk for an hour. The first visit is free.» (language exchange = intercambio de idiomas, enjoy = disfruta, hot = caliente, free = gratis)"
X1 = "«Dear neighbors, thank you for coming. Our building needs a new elevator, and the money is not enough. I ask each family to give a little this month. Together, we can do it.» (neighbors = vecinos, elevator = ascensor, enough = suficiente, give = aportar, together = juntos)"
X2 = "«A small bookstore on Pine Street will close at the end of the month after thirty years. The owner said the rent is too high. Customers are collecting signatures to ask the city for help.» (bookstore = librería, rent = arriendo, customers = clientes, signatures = firmas)"
X3 = "«To send a photo by email, first open a new message. Then click the paperclip and choose the photo. Finally, click send.» (paperclip = clip, choose = elige, send = enviar)"
X4 = "«Last year I joined a swimming team, even though I was afraid of deep water. At first I stayed in the shallow end. Now I swim with the group every Saturday.» (swimming team = equipo de natación, afraid = con miedo, deep = profunda, shallow end = parte baja)"
X5 = "«I believe parks should have free Wi-Fi. Many students need the internet to do homework, and not every family can pay for it. Of course, the cost is high, but libraries already offer a similar service.» (parks = parques, free = gratis, cost = costo, similar = parecido)"
X6 = "«Attention, drivers. Pine Street will be closed tomorrow from eight to noon because workers will fix the road. Please use Oak Avenue instead.» (drivers = conductores, closed = cerrada, noon = mediodía, workers = obreros, fix = arreglar, instead = en su lugar)"
X7 = "«A time bank is a group where people trade help instead of money. For example, you teach guitar for one hour, and later someone helps you with math for one hour. Everyone's hour has the same value.» (trade = intercambian, guitar = guitarra, value = valor)"
X8 = "«Neighbors of Block C: the community room is open on Saturdays from ten to one. Bring your ideas for the summer party. We need volunteers to decorate and to cook. Sign up with Mrs. Lara by Friday.» (community room = sala común, volunteers = voluntarios, decorate = decorar, sign up = inscríbanse)"

lesson(
    OA, 1, MAT_L,
    "Aprenderé a reconocer al escuchar el propósito de un texto, su tema y su idea general, incluso cuando el tema es poco conocido. Sirve para entender lo esencial sin detenerte en cada palabra.",
    ["Sé reconocer formatos orales como avisos y discursos.", "Conozco las preguntas who, what y when."],
    [
        "El propósito (purpose) es la razón por la que alguien habla: informar (to inform), convencer (to persuade), enseñar (to instruct), contar (to tell a story) o invitar (to invite). El tema (topic) es de qué trata el texto, en pocas palabras. La idea principal (main idea) es lo más importante que el hablante dice sobre ese tema. Los detalles (details) son datos que la apoyan, como números, nombres y ejemplos.",
        "Cuando el tema es poco conocido, no necesitas entender todas las palabras. Escucha las palabras que se repiten, los ejemplos y las frases de cierre. Después pregúntate: ¿de qué habla?, ¿qué dice sobre eso? y ¿para qué lo dice? Si tienes dos ideas posibles, elige la que cubre todo el texto, no un solo detalle.",
        "Escribe la idea general con una oración corta: The speaker talks about... and says that... Por ejemplo: The speaker talks about tool libraries and says that people can borrow tools for free.",
    ],
    [("purpose", "propósito: para qué se habla"), ("topic", "tema: de qué trata"), ("main idea", "idea principal"), ("detail", "detalle: dato que apoya la idea"), ("to inform / to persuade", "informar / convencer"), ("to instruct / to invite", "enseñar / invitar")],
    [
        ("Propósito, tema e idea principal", ADULT + W1 + " ¿Cuál es el propósito, el tema y la idea principal?", ["Presenta algo que existe y cómo funciona: informa.", "El tema es la biblioteca de herramientas.", "La idea principal es que prestar herramientas ayuda a ahorrar dinero y evita herramientas sin uso."], "Propósito: informar. Tema: bibliotecas de herramientas. Idea: prestar herramientas ahorra dinero y las aprovecha"),
        ("Un aviso que invita", ADULT + W2 + " ¿Cuál es el propósito y cuál es un detalle?", ["Dice Join our café y The first visit is free: invita.", "El propósito es invitar a asistir.", "Un detalle es que el café funciona los jueves a las siete."], "Invitar a un café de intercambio de idiomas; un detalle es el horario"),
    ],
    [
        ("Elegir como idea principal un detalle, como el precio de la primera visita.", "Un detalle apoya la idea, pero no cubre todo el texto.", "Elige la idea que resume el texto completo."),
        ("Confundir el tema con el propósito.", "El tema dice de qué se habla; el propósito dice para qué.", "Responde primero de qué habla y luego para qué lo dice."),
    ],
    [
        ml(X1, "¿Cuál es el propósito?", "Pedir ayuda a los vecinos para pagar un ascensor", ["Informar a los vecinos sobre un cambio de horario", "Enseñar a los vecinos a usar un ascensor nuevo"], "Dice I ask each family to give a little."),
        ml(X3, "¿Para qué sirve este texto?", "Para enseñar a enviar una foto por correo", ["Para contar una anécdota", "Para vender un teléfono"], "First, Then y Finally ordenan pasos."),
        ml(X2, "¿Cuál es el tema?", "El cierre de una librería", ["La historia de una ciudad", "Un nuevo libro en venta"], "La noticia trata de que la librería cerrará."),
    ],
    [
        ml(X4, "¿Cuál es la idea general?", "Superó el miedo al agua y ahora nada con el equipo", ["Aprendió a nadar rápido en un solo día de práctica", "Dejó el equipo por miedo a la parte profunda"], "Pasó de la parte baja a nadar con el grupo cada sábado."),
        ml(X5, "¿Qué quiere lograr el hablante?", "Convencer de que los parques tengan Wi-Fi gratis", ["Informar el precio de internet", "Contar una experiencia en un parque"], "Dice I believe y da razones."),
        mc("¿Qué es el tema de un texto?", "De qué trata, en pocas palabras", ["Cada dato que se menciona", "La razón por la que el hablante cuenta chistes"], "El tema responde de qué se habla."),
    ],
    [
        ml(X6, "¿Cuál es la idea principal?", "Una calle estará cerrada mañana por la mañana y hay que usar otra", ["Oak Avenue estará cerrada mañana y hay que usar Pine Street", "Los obreros arreglarán dos calles durante toda la tarde y la mañana del día siguiente"], "Informa un cierre y da una alternativa."),
        ml(X2, "¿Qué oración resume mejor la noticia?", "Una librería cerrará después de treinta años y sus clientes piden ayuda", ["El arriendo es alto y los clientes ya no compran libros", "Pine Street tiene muchas librerías que cerrarán este año por el alto arriendo de la zona"], "La idea cubre el cierre y la reacción de los clientes."),
        ml(X4, "¿Qué hacía el hablante al principio?", "Se quedaba en la parte baja de la piscina", ["Nadaba en la parte profunda", "Vivía lejos del equipo"], "At first I stayed in the shallow end."),
    ],
    [
        ml(X5, "Un compañero dice que el propósito es informar el costo del Wi-Fi. ¿Qué respuesta es mejor?", "No: el hablante da una opinión con razones para convencer", ["Sí: menciona que el costo es alto y compara precios", "Sí: usa números para mostrar cuánto cuesta internet y menciona el costo de las bibliotecas"], "I believe y las razones muestran un texto que persuade."),
        ml(X3, "Otra compañera dice que el texto cuenta una experiencia. ¿Tiene razón?", "No: usa First, Then y Finally para enseñar pasos", ["Sí: está en pasado", "Sí: cuenta algo que le pasó al hablante"], "Los pasos ordenados indican un procedimiento."),
    ],
    [
        ml(X7, "¿Cuál es la idea general?", "En un banco de tiempo se intercambia ayuda por horas, no dinero", ["Un banco entrega préstamos de dinero con intereses bajos", "Las personas enseñan guitarra y matemáticas para ganar dinero extra en sus horas libres"], "Dice trade help instead of money y que todas las horas valen lo mismo."),
        mc("Escuchas un texto sobre un tema que casi no conoces y no entiendes algunas palabras. ¿Qué conviene hacer?", "Atender las palabras que se repiten y los ejemplos para sacar la idea general", ["Detenerte en cada palabra desconocida hasta traducirla", "Dejar de escuchar y esperar la siguiente"], "La idea general se saca de lo que se repite y de los ejemplos."),
    ],
    [ml(X8, "¿Cuál es el propósito del aviso?", "Invitar a participar y pedir voluntarios para una fiesta", ["Anunciar que la sala común cerrará los sábados por la tarde", "Contar cómo fue la fiesta de verano del año pasado"], "Pide ideas y voluntarios, y tiene un plazo para inscribirse.")],
    [
        ("En Inglés de 2.º medio (OA 3, clase 1): ¿qué diferencia hay entre el tema y la idea principal?", "El tema dice de qué trata; la idea principal dice lo más importante sobre ese tema", "La idea principal agrega lo que se dice del tema."),
        ("En Inglés de 2.º medio (OA 3, clase 1): ¿cuál es el propósito de un aviso que dice join us?", "Invitar", "Join us es una invitación."),
        ("En Inglés de 2.º medio (OA 3, clase 1): ¿qué se hace cuando el tema es poco conocido?", "Se escuchan las palabras repetidas y los ejemplos", "Eso permite entender lo general sin conocer todas las palabras."),
    ],
    task("Un adulto lee dos veces: «Good morning. Today I will talk about a free tutoring service at the local library. Every Tuesday and Thursday, older students help younger students with math. Many families do not know about it, so please tell your friends.» (tutoring = clases de apoyo, local = del barrio, older = mayores, younger = menores, tell = cuenten). Anota el propósito, el tema, la idea principal y un detalle.", "Propósito: informar e invitar. Tema: clases de apoyo gratis en la biblioteca. Idea principal: hay ayuda gratis de matemáticas y hay que contárselo a otros. Detalle: martes y jueves.", ["indica el propósito con un verbo", "escribe el tema en pocas palabras", "da una idea principal y un detalle"], ["ficha de cuatro líneas en la hoja"], ["elegir un detalle como idea principal", "no escribir el propósito"], "Pide que explique por qué su idea principal cubre más que el detalle que eligió."),
    "Escucha otra vez el texto del banco de tiempo y anota el tema en una frase.",
    "Piensa en un tema poco conocido y escribe en español una oración que diga de qué trata y para qué lo contarías.",
)

# ------------------------------------------------------------------ clase 2: información específica y detalles
D0A = "«Good morning, Mountain View Hotel. Guest: Hello, this is Mr. Lagos. I have a room for two nights, from Friday the ninth. Reception: Yes, room 214. Breakfast is from seven to ten. Guest: Thank you. Could you send a taxi at six on Sunday?» (hotel = hotel, room = habitación, nights = noches, breakfast = desayuno, taxi = taxi)"
D0B = "«Reporter: What do you think about the new bus lane? Mrs. Pérez: I love it. My trip is faster. Mr. Díaz: I don't like it. There is less room for cars, and shops lose customers.» (bus lane = pista solo bus, trip = viaje, room = espacio, lose = pierden, customers = clientes)"
D1 = "«Good morning, runners. The city marathon starts at seven thirty on Sunday at Central Square. Runners must pick up their number on Saturday between ten and five at the sports hall. The finish line is at the river park. The first three runners will get a medal.» (marathon = maratón, pick up = retirar, number = número, finish line = meta, medal = medalla)"
D2 = "«Cinema Lux, good afternoon. Customer: Hi, what time is the comedy tonight? Employee: There are two shows, at six forty-five and at nine ten. Tickets are five thousand five hundred pesos each. Customer: Two tickets for the nine ten, please. I will pay at the door.» (comedy = comedia, shows = funciones, tickets = entradas, each = cada una, door = entrada del cine)"
D3 = "«Teacher: We have three options for the trip: the observatory, the aquarium or the science center. Camila: I prefer the observatory because it opens at night. Joaquín: I would rather go to the aquarium, but it is far. Teacher: Then we will vote on Wednesday.» (observatory = observatorio, aquarium = acuario, science center = centro científico, far = lejos, vote = votar)"
D4 = "«On Saturday morning, Marta went to the vet with her dog. The vet checked the dog's ears and said they were fine. After that, Marta bought a new leash at the pet shop next door and walked home through the park.» (vet = veterinaria, checked = revisó, ears = orejas, leash = correa, pet shop = tienda de mascotas)"
D5 = "«Hi Sofía, it's Gonzalo. The study group is not at my house today. It's at Lucas's place on Maple Street, number 48. We start at four thirty, not four. Bring your math notebook, please.» (study group = grupo de estudio, place = casa, start = empezamos, notebook = cuaderno)"
D6 = "«Look at that: Jorge has run for forty minutes and he isn't tired. Last month he could only run for ten. His coach says he trains every morning at six.» (tired = cansado, last month = el mes pasado, coach = entrenador, trains = entrena)"

lesson(
    OA, 2, MAT_L,
    "Aprenderé a ubicar al escuchar información específica: quién es, qué hace, qué opina, dónde y cuándo ocurre, y quién habla. Sirve para responder preguntas con datos exactos sin confundir personas, lugares ni horas.",
    ["Sé distinguir la idea general de los detalles.", "Sé decir horas, días y números."],
    [
        "La información específica son los datos que responden a preguntas concretas: who (quién), what (qué), where (dónde), when (cuándo), how many o how much (cuántos o cuánto) y why (por qué). Antes de escuchar, lee la pregunta y decide qué tipo de dato buscas. Mientras escuchas, anota solo palabras clave: nombres, números, lugares y verbos.",
        "En los diálogos hay varios hablantes. Anota quién dice cada cosa, por ejemplo C: Camila, J: Joaquín. Las opiniones aparecen con frases como I love it, I don't like it, I prefer y I would rather. Las acciones se reconocen por los verbos, y el tiempo, por palabras como on Saturday, after that o every morning. Cuando dos datos se parecen, como four y fourteen, escucha dónde cae la fuerza de la palabra.",
        "Al terminar, comprueba que tu dato responde exactamente a la pregunta. Si el hablante se corrige, como not four, el dato correcto es el último que dice.",
    ],
    [("who / what / where / when", "quién / qué / dónde / cuándo"), ("how many / how much", "cuántos / cuánto"), ("opinion", "opinión: lo que alguien piensa"), ("I prefer / I would rather", "prefiero"), ("after that", "después de eso"), ("not four", "no a las cuatro: corrección")],
    [
        ("Anotar números y lugares", ADULT + D0A + " ¿Cuántas noches se queda el huésped y en qué habitación?", ["Busco una cantidad: two nights.", "Busco la habitación: 214.", "Respondo con ambos datos."], "Dos noches, habitación 214"),
        ("Atribuir opiniones", ADULT + D0B + " ¿Quién opina qué sobre la pista?", ["La señora Pérez dice I love it y que su viaje es más rápido.", "El señor Díaz dice I don't like it y menciona menos espacio y menos clientes.", "A ella le gusta; a él no."], "La señora Pérez opina a favor; el señor Díaz, en contra"),
    ],
    [
        ("Anotar el primer dato que se dice aunque el hablante se corrija.", "Se ignora la corrección: not four.", "El dato correcto es el que viene después de la corrección."),
        ("Confundir quién dijo una opinión cuando hablan dos personas.", "No se anota el nombre del hablante.", "Marca la inicial del hablante junto a cada dato."),
    ],
    [
        ml(D1, "¿A qué hora empieza la maratón?", "A las 7:30", ["A las 7:00", "A las 10:00"], "Dice starts at seven thirty."),
        ml(D1, "¿Dónde se retira el número?", "En el gimnasio deportivo", ["En la plaza central", "En el parque del río"], "Pick up their number at the sports hall."),
        ml(D5, "¿A qué hora empieza el grupo de estudio?", "A las 4:30", ["A las 4:00", "A las 3:30"], "Dice four thirty, not four."),
    ],
    [
        ml(D3, "¿Quién prefiere el observatorio y por qué?", "Camila, porque abre de noche", ["Joaquín, porque queda lejos", "La profesora, porque cuesta menos"], "Camila dice I prefer the observatory because it opens at night."),
        ml(D4, "¿Qué compró Marta?", "Una correa nueva", ["Comida para el perro", "Un juguete para el perro"], "Bought a new leash."),
        ml(D2, "¿Qué función elige el cliente?", "La de las 9:10", ["La de las 6:45", "La de las 7:15"], "Two tickets for the nine ten."),
    ],
    [
        ml(D5, "¿Dónde se juntará el grupo de estudio?", "En la casa de Lucas, calle Maple 48", ["En la casa de Gonzalo", "En la calle Maple 84"], "It's at Lucas's place on Maple Street, number 48."),
        ml(D3, "¿Por qué Joaquín duda del acuario?", "Porque queda lejos", ["Porque cierra de noche", "Porque es muy caro"], "Dice but it is far."),
        ml(D6, "¿Cuánto tiempo corre Jorge ahora y cuánto corría el mes pasado?", "Cuarenta minutos y diez minutos", ["Diez minutos y cuarenta minutos", "Cuarenta minutos y cuatro minutos"], "Has run for forty minutes; last month he could only run for ten."),
    ],
    [
        ml(D4, "¿Qué hizo Marta inmediatamente después de que la veterinaria revisó las orejas del perro?", "Compró una correa", ["Fue a su casa", "Visitó el parque"], "After that señala lo que sigue: bought a new leash."),
        ml(D1, "¿Quiénes recibirán medalla?", "Los tres primeros corredores", ["Todos los que lleguen a la meta", "Los diez primeros corredores"], "The first three runners will get a medal."),
    ],
    [
        ml(D2, "¿Cuál afirmación es verdadera?", "El cliente comprará dos entradas para la función de las 9:10 y pagará en la puerta", ["El cliente comprará una sola entrada y pagará en la puerta", "El cliente comprará dos entradas para las 6:45 y pagará por internet"], "I will pay at the door."),
        ml(D6, "¿Por qué mejoró Jorge, según el texto?", "Porque entrena todas las mañanas a las seis", ["Porque corre solo los fines de semana", "Porque dejó de entrenar"], "His coach says he trains every morning at six."),
    ],
    [arith(ADULT + D2 + " Un grupo de cuatro personas compra entradas para la función de las 9:10. ¿Cuántos pesos pagan en total?", "4*5500", "Cada entrada cuesta cinco mil quinientos pesos.", " pesos")],
    [
        ("En Inglés de 2.º medio (OA 3, clase 2): ¿qué hace falta anotar al escuchar una opinión en un diálogo?", "Quién la dice", "Hay varios hablantes."),
        ("En Inglés de 2.º medio (OA 3, clase 2): ¿qué dato es correcto si alguien dice four thirty, not four?", "Four thirty", "Se toma el dato corregido."),
        ("En Inglés de 2.º medio (OA 3, clase 2): ¿qué pregunta pide un lugar?", "Where", "Where se traduce dónde."),
    ],
    task("Un adulto lee dos veces: «Hi, this is Dr. Ortiz's office. Your appointment is on Monday at eleven fifteen. Please arrive ten minutes early and bring your ID card. The office is on Elm Street, number 76, on the second floor.» (appointment = hora, early = antes, ID card = cédula, floor = piso). Anota: quién llama, día y hora, calle y número, y qué debes llevar.", "La consulta del Dr. Ortiz; lunes a las 11:15; Elm Street 76; cédula de identidad.", ["anota cuatro datos distintos", "escribe números con cifras", "no confunde hora con número de calle"], ["ficha de cuatro datos en la hoja"], ["escribir 11:50 en lugar de 11:15", "olvidar el piso"], "Pide que lea sus datos al adulto y que compruebe cada uno con el texto."),
    "Escucha otra vez el mensaje de Gonzalo y anota solo números y lugares.",
    "Escribe en español una pregunta con who, where, when y how many sobre algo que te pasó esta semana.",
)

# ------------------------------------------------------------------ clase 3: relaciones de importancia y problema-solución
V1 = "«At our school cafeteria, the main problem is the long line at lunch. Students wait twenty minutes, so they have little time to eat. The solution is simple: open a second counter. As a result, the line now takes ten minutes.» (cafeteria = comedor, line = fila, counter = mesón, wait = esperan, simple = simple)"
V2 = "«When you give a speech, the most important thing is to know your audience. Also, practice with a friend. A small detail, like the color of your shirt, matters less.» (speech = discurso, audience = público, practice = practica, matters = importa)"
I1 = "«A youth orchestra has a problem: there are only two violins, but twelve students want to play. The teacher found a solution. Students will take turns, and the school will borrow six violins from a nearby college.» (orchestra = orquesta, violins = violines, take turns = turnarse, borrow = pedir prestado, nearby college = instituto cercano)"
I2 = "«When you write an email to a teacher, the most important thing is a clear subject. Next, greet politely. Finally, check your spelling. The color of the letters does not matter.» (subject = asunto, greet = saluda, politely = con cortesía, spelling = ortografía, letters = letras)"
I3 = "«The neighborhood bus stop is dark at night, so many people feel unsafe. The neighbors asked for a street lamp, but the city said there was no money. Finally, a local shop agreed to pay for the lamp. Now the stop is bright and people feel safer.» (bus stop = paradero, unsafe = inseguras, street lamp = farol, local shop = tienda del barrio, agreed = aceptó, bright = iluminado)"
I4 = "«Our apartment building has one washing machine for thirty families. The problem is that people use it at the same time. The building council made a schedule, and now each floor has its own day.» (washing machine = lavadora, building council = comité del edificio, schedule = horario, floor = piso)"
I5 = "«There are three reasons to learn a second language. Above all, it opens doors to work. Second, it helps you travel. Finally, it is a nice hobby.» (reasons = razones, above all = sobre todo, opens doors = abre puertas, travel = viajar, hobby = pasatiempo)"
I6 = "«Many students forget their homework. For example, Ana forgets it on the bus, and Ben leaves it on the table. A simple solution is a checklist by the door.» (forget = olvidan, leaves = deja, checklist = lista de verificación, door = puerta)"
I7 = "«The school band cannot practice after four because the music room is used for tutoring. The principal says the band can use the gym on Tuesdays. As a result, the band has two hours of practice each week.» (band = banda, practice = ensayar, tutoring = clases de apoyo, principal = director, gym = gimnasio)"
I8 = "«Our town festival has a problem with parking. About two hundred cars come, but there are only eighty places. The organizers suggest a solution: free buses from the train station every fifteen minutes. As a result, fewer people come by car.» (festival = festival, parking = estacionamiento, places = lugares, organizers = organizadores, suggest = proponen, train station = estación de trenes)"

lesson(
    OA, 3, MAT_L,
    "Aprenderé a reconocer al escuchar qué idea es la más importante y qué problema se plantea y cómo se resuelve. Sirve para entender la estructura de un texto y no quedarse solo con datos sueltos.",
    ["Sé distinguir la idea principal de los detalles.", "Conozco as a result y so."],
    [
        "Las ideas de un texto no tienen el mismo peso. Algunas frases anuncian importancia: the most important thing is, above all, the main problem is, first of all. Otras marcan ideas de apoyo: also, for example, next, finally, second. Una frase que dice matters less o does not matter avisa que esa idea es secundaria. Para ordenar las ideas por importancia, escucha estas señales.",
        "Muchos textos orales tienen una estructura problema-solución. Primero se presenta el problema con frases como the problem is o the main problem is. Luego viene la solución con the solution is, a simple solution is o the teacher found a solution. Al final aparece el resultado, que suele marcarse con as a result o now. Así se responde a tres preguntas: ¿cuál es el problema?, ¿qué se hizo? y ¿qué cambió?",
        "Al escuchar, divide tu hoja en tres columnas: problem, solution y result. Anota palabras clave en cada una. Si falta una columna, vuelve a escuchar buscando la señal que corresponde.",
    ],
    [("the most important thing / above all", "lo más importante / sobre todo"), ("the main problem", "el problema principal"), ("the solution is", "la solución es"), ("for example", "por ejemplo"), ("as a result / now", "como resultado / ahora"), ("matters less", "importa menos")],
    [
        ("Problema, solución y resultado", ADULT + V1 + " ¿Cuál es el problema, la solución y el resultado?", ["The main problem anuncia el problema: la fila larga.", "The solution is anuncia la solución: abrir un segundo mesón.", "As a result anuncia el resultado: ahora la fila dura diez minutos."], "Problema: fila larga. Solución: segundo mesón. Resultado: la fila dura diez minutos"),
        ("Ideas más y menos importantes", ADULT + V2 + " ¿Cuál es la idea más importante y cuál importa menos?", ["The most important thing marca la idea clave: conocer al público.", "Also agrega otra: practicar con un amigo.", "Matters less marca la menos importante: el color de la camisa."], "Lo más importante es conocer al público; importa menos el color de la camisa"),
    ],
    [
        ("Pensar que la primera idea que se oye es siempre la más importante.", "La importancia la marcan frases como the most important thing, no el orden.", "Busca las señales de importancia antes de decidir."),
        ("Confundir el resultado con la solución.", "La solución es lo que se hace; el resultado es lo que cambia después.", "Busca as a result y now para el resultado."),
    ],
    [
        ml(I1, "¿Cuál es el problema?", "Hay solo dos violines y doce estudiantes quieren tocar", ["Los violines están rotos y el colegio no tiene dinero para arreglarlos este año", "El profesor no sabe música y los alumnos tampoco"], "Dice a youth orchestra has a problem."),
        ml(I4, "¿Cuál es la solución?", "Un horario con un día para cada piso", ["Comprar treinta lavadoras", "Cerrar la lavandería"], "The building council made a schedule."),
        ml(I5, "¿Qué razón es la más importante según el hablante?", "Que abre puertas al trabajo", ["Que ayuda a viajar", "Que es un pasatiempo"], "Above all marca la razón más importante."),
    ],
    [
        ml(I3, "¿Qué problema tenía el paradero?", "Estaba oscuro de noche y la gente se sentía insegura", ["Estaba lejos del barrio y casi nadie lo usaba", "Era muy pequeño y la gente no cabía en él cuando llovía en la tarde"], "Dark at night, so many people feel unsafe."),
        ml(I2, "¿Qué es lo más importante en un correo a un profesor?", "Un asunto claro", ["La ortografía", "El color de las letras"], "The most important thing es un asunto claro; la ortografía viene al final."),
        ml(I6, "¿Cuál es la solución propuesta?", "Una lista de verificación junto a la puerta", ["Dejar la tarea en el bus para no olvidarla", "No hacer tarea los días en que hay mucha prisa"], "A simple solution is a checklist by the door."),
    ],
    [
        ml(I1, "¿Qué dos acciones forman la solución?", "Turnarse y pedir prestados seis violines", ["Comprar doce violines y turnarse", "Pedir prestada una sala y cambiar de profesor"], "Dice take turns y borrow six violins."),
        ml(I3, "¿Quién resolvió el problema?", "Una tienda del barrio que pagó el farol", ["La municipalidad", "Los vecinos con su dinero"], "The city said there was no money; a local shop agreed to pay."),
        ml(I4, "¿Qué causaba el problema?", "Que muchas personas usaban la lavadora a la vez", ["Que la lavadora era muy antigua", "Que había pocas familias"], "The problem is that people use it at the same time."),
    ],
    [
        ml(I5, "¿Cuál es la segunda razón para aprender un idioma?", "Ayuda a viajar", ["Abre puertas al trabajo", "Es un pasatiempo"], "Second introduce la segunda razón."),
        ml(I2, "Un oyente dice que el color de las letras es lo más importante. ¿Por qué se equivoca?", "Porque el texto dice que ese detalle no importa", ["Porque el texto dice que lo más importante es la ortografía", "Porque el texto dice que el color importa solo al final"], "The color of the letters does not matter."),
    ],
    [
        ml(I7, "¿Cuál es el resultado de la solución?", "La banda tiene dos horas de ensayo por semana", ["La banda deja de ensayar", "El director cierra el gimnasio"], "As a result señala el resultado."),
        arith(ADULT + I1 + " Con los 2 violines del colegio y los 6 prestados, ¿cuántos de los 12 estudiantes tienen que esperar su turno?", "12-(2+6)", "Se suman los violines disponibles y se restan de los estudiantes.", " estudiantes"),
    ],
    [arith(ADULT + I8 + " ¿Cuántos autos no tienen lugar para estacionar?", "200-80", "Se restan los lugares disponibles de los autos que llegan.", " autos")],
    [
        ("En Inglés de 2.º medio (OA 3, clase 3): ¿qué señal anuncia una solución?", "The solution is", "Es la frase que introduce lo que se hace."),
        ("En Inglés de 2.º medio (OA 3, clase 3): ¿qué significa the most important thing?", "Lo más importante", "Marca la idea de mayor peso."),
        ("En Inglés de 2.º medio (OA 3, clase 3): ¿qué dos columnas, además de result, ayudan a anotar un problema-solución?", "Problem y solution", "Organizan lo que se oye."),
    ],
    task("Un adulto lee dos veces: «Our school trip has a problem. The bus is too small for forty students. Above all, we want everyone to go. The solution is to rent two small buses. As a result, every student can join, and the cost is a little higher.» (trip = paseo, rent = arrendar, join = ir, cost = costo, a little higher = un poco más alto). Completa una tabla con problem, solution y result, y anota qué es lo más importante.", "Problema: el bus es pequeño para cuarenta estudiantes. Solución: arrendar dos buses pequeños. Resultado: todos pueden ir y el costo sube un poco. Lo más importante: que todos vayan.", ["completa las tres columnas", "indica qué es lo más importante", "usa palabras clave del texto"], ["tabla de tres columnas en la hoja"], ["poner el resultado en la columna de solución", "no usar las señales de importancia"], "Pide que explique con qué frase del texto supo qué era lo más importante."),
    "Escucha otra vez el texto del comedor y marca con colores problema, solución y resultado.",
    "Piensa en un problema de tu curso y escribe en español su solución y su posible resultado.",
)

# ------------------------------------------------------------------ clase 4: hablantes, situaciones, opiniones, lugar y tiempo
P1 = "«Host: Today's question is: should cell phones be allowed during recess? Caller 1, Tomás: Yes. Recess is free time, and I use my phone to talk to my cousin in another city. Caller 2, Dani: No. I think students should play together, and phones make them quiet. Host: Thank you both.» (host = conductor, cell phones = celulares, recess = recreo, allowed = permitidos, caller = radioescucha que llama, cousin = primo)"
P2 = "«Agent: Thank you for calling Fast Net. How can I help you? Customer: My internet is very slow since Monday. Agent: I am sorry about that. Is it slow in all rooms? Customer: Yes. Agent: A technician can come on Thursday between two and five. Customer: Thursday is fine.» (agent = ejecutivo, slow = lento, since = desde, technician = técnico, between = entre)"
P3 = "«Mrs. Rojas: The class trip is on the twelfth of May. Mr. Silva: How much will it cost? Mrs. Rojas: Eight thousand pesos per student. Ms. Vega: Can we pay in two parts? Mrs. Rojas: Yes, half this week and half next week.» (class trip = paseo de curso, cost = costar, per = por, pay = pagar, parts = cuotas, half = la mitad)"
P4 = "«Last Friday at the library, Elena met her cousin by chance. They talked for an hour in the reading room, and then they ate lunch together at the corner café.» (library = biblioteca, by chance = por casualidad, reading room = sala de lectura, corner café = cafetería de la esquina)"
P5 = "«Reporter: What do you like about living near the sea? Lucas: I love the mornings; it's calm and I can walk. But in winter it is cold and windy. Reporter: Would you move? Lucas: No, never. I love my town.» (reporter = periodista, sea = mar, calm = tranquilo, windy = con viento, move = mudarte)"

lesson(
    OA, 4, MAT_L,
    "Aprenderé a identificar al escuchar quién habla, qué opina, qué hace, dónde y cuándo ocurre la situación, en diálogos de varios hablantes. Sirve para no mezclar las voces ni los datos de cada persona.",
    ["Sé ubicar información específica.", "Conozco I think, I love y I don't like."],
    [
        "En conversaciones, entrevistas y llamadas hablan varias personas. Cada una tiene un papel (role): el conductor (host), un cliente (customer), un profesor (teacher), un periodista (reporter). Identifica el papel por lo que dice: quien pregunta suele dirigir la conversación, y quien responde da la información o la opinión. Anota la inicial de cada hablante para no confundirlos.",
        "Para reconocer opiniones, busca frases como I think, I believe, I love, I don't like y I prefer. Para reconocer la situación, mira el lugar y el momento: Thank you for calling indica una llamada, the class trip indica una reunión de escuela. Para el tiempo, escucha on Thursday, last Friday, every morning y after that. Los lugares aparecen con in, at y on: at the library, in the reading room.",
        "Una cortesía como I am sorry about that no es una opinión sobre el tema: muestra que el hablante lamenta un problema. Distingue las fórmulas de cortesía de las ideas. Al final, revisa que cada dato esté unido al hablante correcto.",
    ],
    [("host / customer / reporter", "conductor / cliente / periodista"), ("role", "papel de cada hablante"), ("I think / I believe", "creo que"), ("I am sorry about that", "lamento eso: cortesía"), ("by chance", "por casualidad"), ("between two and five", "entre las dos y las cinco")],
    [
        ("Hablantes y opiniones", ADULT + P1 + " ¿Qué postura tiene cada llamado y por qué?", ["Tomás dice Yes: quiere usar el teléfono para hablar con su primo.", "Dani dice No: piensa que los estudiantes deben jugar juntos.", "Cada uno da su razón."], "Tomás está a favor porque habla con su primo; Dani está en contra porque cree que deben jugar juntos"),
        ("Situación, tiempo y lugar", ADULT + P4 + " ¿Dónde y cuándo ocurre la escena?", ["La escena ocurre en la biblioteca.", "Last Friday dice el momento.", "Después van a una cafetería."], "En la biblioteca el viernes pasado"),
    ],
    [
        ("Atribuir a Dani lo que dijo Tomás.", "Se mezclan las voces por no anotar la inicial.", "Marca T o D antes de cada idea."),
        ("Tomar una fórmula de cortesía como opinión.", "I am sorry about that no es una postura sobre el tema.", "Pregunta si la frase da una idea del tema o solo es cortesía."),
    ],
    [
        ml(P1, "¿Quién dice que los estudiantes deben jugar juntos en el recreo?", "Dani", ["Tomás", "El conductor"], "Dani dice I think students should play together."),
        ml(P2, "¿Cuál es el problema del cliente?", "Su internet está lento desde el lunes", ["No tiene internet desde hace una semana", "Se cortó la luz en toda la casa el lunes"], "Dice My internet is very slow since Monday."),
        ml(P3, "¿Cuándo es el paseo?", "El doce de mayo", ["El dos de mayo", "El doce de junio"], "Dice the twelfth of May."),
    ],
    [
        ml(P2, "¿Cuándo irá el técnico?", "El jueves entre las dos y las cinco", ["El lunes por la mañana", "El jueves a las doce"], "Dice on Thursday between two and five."),
        ml(P1, "¿Por qué Tomás quiere usar su teléfono en el recreo?", "Para hablar con su primo de otra ciudad", ["Para jugar con sus compañeros", "Para llamar al conductor"], "Dice I use my phone to talk to my cousin."),
        ml(P5, "¿Qué le gusta a Lucas de las mañanas?", "Que son tranquilas y puede caminar", ["Que son frías y con mucho viento en la playa", "Que hay mucha gente caminando por el pueblo"], "Dice it's calm and I can walk."),
    ],
    [
        ml(P3, "¿Cómo se pagará el paseo?", "La mitad esta semana y la mitad la próxima", ["Todo el dinero el último día antes del paseo", "Solo la mitad del total, sin pagar la otra mitad"], "Dice half this week and half next week."),
        ml(P4, "¿Dónde almorzaron Elena y su primo?", "En la cafetería de la esquina", ["En la sala de lectura", "En la casa de Elena"], "Dice at the corner café."),
        ml(P5, "¿Qué desventaja menciona Lucas?", "Que en invierno hace frío y hay viento", ["Que no puede caminar por la playa en la mañana", "Que hay mucho ruido por los turistas del verano"], "Dice in winter it is cold and windy."),
    ],
    [
        ml(P1, "¿Cuál es la postura de Dani y su razón?", "No: piensa que los estudiantes deben jugar juntos y que los teléfonos los hacen callar", ["Sí: porque los teléfonos son rápidos para hablar con la familia", "No: porque el recreo es muy corto para jugar y para usar teléfonos, y los profesores se enojan"], "Dani dice No y da dos razones."),
        ml(P2, "¿Qué muestra la frase I am sorry about that del agente?", "Que lamenta el problema del cliente", ["Que el servicio ya funciona", "Que el cliente se equivocó"], "Es una fórmula de cortesía ante un problema."),
    ],
    [
        ml(P3, "¿Cuál afirmación es verdadera?", "Una persona pregunta por el costo y otra por pagar en cuotas", ["Todos preguntan por la fecha y nadie por el costo", "Nadie pregunta por el costo ni por las cuotas del pago, solo por la fecha del paseo"], "Mr. Silva pregunta How much; Ms. Vega pregunta Can we pay in two parts."),
        arith(ADULT + P3 + " ¿Cuántos pesos pagará un estudiante esta semana?", "8000//2", "Paga la mitad del costo del paseo.", " pesos"),
    ],
    [ml(P5, "El periodista pregunta si Lucas se mudaría. ¿Qué responde?", "Que no, nunca, porque ama su pueblo", ["Que sí, por el frío", "Que todavía no lo decide"], "Dice No, never. I love my town.")],
    [
        ("En Inglés de 2.º medio (OA 3, clase 4): ¿cómo se identifica a un hablante en un diálogo con varios?", "Por su papel y por lo que dice, anotando su inicial", "Así no se mezclan los datos."),
        ("En Inglés de 2.º medio (OA 3, clase 4): ¿qué expresa I am sorry about that?", "Cortesía: lamenta un problema", "No es una opinión sobre el tema."),
        ("En Inglés de 2.º medio (OA 3, clase 4): ¿qué frase marca un tiempo pasado: last Friday o every morning?", "Last Friday", "Señala un día ya ocurrido."),
    ],
    task("Un adulto lee dos veces: «Interviewer: Why did you join the school newspaper? Pía: Because I like to write. Interviewer: What is difficult? Pía: Deadlines. We must finish on Thursday at noon. Interviewer: And what do you like most? Pía: Seeing my article on the wall on Friday.» (newspaper = diario escolar, deadlines = plazos, finish = terminar, article = artículo, wall = mural). Anota: quién pregunta y quién responde, por qué se unió Pía, qué le cuesta y cuándo ve su artículo.", "Pregunta la entrevistadora y responde Pía. Se unió porque le gusta escribir. Le cuestan los plazos (jueves al mediodía). Ve su artículo el viernes.", ["distingue a los dos hablantes", "anota razón, dificultad y día", "usa palabras clave del texto"], ["ficha de cuatro datos en la hoja"], ["confundir quién pregunta", "mezclar el día del plazo con el día del mural"], "Pide que lea el texto otra vez y marque la frase de cada dato."),
    "Escucha otra vez la llamada al servicio de internet y anota quién dice cada frase.",
    "Escribe en español un diálogo corto de dos personas con una opinión distinta cada una.",
)

# ------------------------------------------------------------------ clase 5: escucha integrada y ficha de notas
L1 = "«Good evening. Here is the local news. The town of Alder Bay has a problem: every summer, thousands of visitors arrive, and the beach parking lot is full by nine in the morning. Residents say the noise and traffic make life difficult. This year, the town council decided to run a free shuttle from the train station every twenty minutes. Visitors can also rent lockers at the station. Mayor Elena Costa said, We want visitors to enjoy our town without causing problems. So far, traffic near the beach has dropped, and residents are happy. However, some shop owners say they sell less because fewer cars stop in the center.» (local news = noticias locales, residents = vecinos, parking lot = estacionamiento, town council = municipalidad, shuttle = bus de acercamiento, lockers = casilleros, mayor = alcaldesa, dropped = bajó, shop owners = dueños de tiendas)"
L2 = "«Good afternoon, friends. I am running for class president because I believe every voice matters. First, I will put an ideas box in the room, and I will read it every Monday. Second, I promise a monthly meeting with the principal. Some people say these things take too much time, but I think they are worth it. Above all, I want everyone to feel heard.» (running for = me presento a, class president = presidenta de curso, voice = voz, matters = importa, ideas box = buzón de ideas, promise = prometo, monthly = mensual, principal = director, worth it = vale la pena, heard = escuchado)"
L3 = "«When I was fifteen, I joined the school choir, but I was nervous because I could not read music. My teacher suggested a simple solution: I listened to each song twice at home and followed the words. Slowly, I learned the notes. Now I sing the second voice and I help new students.» (choir = coro, nervous = nervioso, read music = leer partituras, suggested = sugirió, followed = seguí, notes = notas, second voice = segunda voz)"

lesson(
    OA, 5, MAT_L,
    "Aprenderé a escuchar un texto largo y a completar una ficha con propósito, tema, idea principal, detalles, orden de importancia y problema-solución. Sirve para integrar todo lo aprendido y responder sin ayuda.",
    ["Sé reconocer el propósito, los detalles y el problema-solución.", "Sé anotar quién dice qué."],
    [
        "Una ficha de escucha (listening grid) ordena lo que oyes en filas: purpose, topic, main idea, details, problem, solution y result. En la primera escucha completas lo general: propósito, tema e idea principal. En la segunda, buscas los detalles y las señales de importancia y de problema-solución. En la tercera, solo compruebas los datos dudosos.",
        "Para decidir qué anotar, usa preguntas: ¿para qué habla?, ¿de qué habla?, ¿qué dice sobre eso?, ¿quién lo dice?, ¿qué datos concretos da?, ¿hay un problema?, ¿cómo se resolvió? y ¿qué cambió? Las opiniones se anotan junto al nombre del hablante. Si dos partes de un texto parecen contradecirse, mira conectores como however y but, que muestran que hay otro punto de vista.",
        "En un texto largo no puedes escribir todo. Usa abreviaturas y símbolos, como P para problem y S para solution, o una flecha para el resultado. Revisa al final que tu ficha responda a todas las preguntas con datos del texto.",
    ],
    [("listening grid", "ficha de escucha"), ("problem / solution / result", "problema / solución / resultado"), ("however", "sin embargo: introduce un punto de vista contrario"), ("resident", "vecino, habitante"), ("mayor", "alcalde, alcaldesa"), ("worth it", "que vale la pena")],
    [
        ("Completar la ficha de una noticia", ADULT + L1 + " ¿Cuál es el propósito, el problema y la solución?", ["Es una noticia: informa.", "El problema son los visitantes de verano que llenan el estacionamiento y causan ruido y tráfico.", "La solución es un bus gratuito desde la estación cada veinte minutos."], "Informar; problema: visitantes llenan el estacionamiento; solución: bus gratuito desde la estación cada veinte minutos"),
        ("Detalles y puntos de vista", ADULT + L2 + " ¿Qué dos promesas hace y qué dicen algunos?", ["First y Second marcan dos promesas.", "La primera es un buzón de ideas; la segunda, una reunión mensual con el director.", "Some people say marca el punto de vista contrario: toma demasiado tiempo."], "Promete un buzón de ideas y una reunión mensual con el director; algunos dicen que toma mucho tiempo"),
    ],
    [
        ("Escribir todo el texto en la ficha.", "Se pierde el hilo y no se alcanza a escuchar.", "Anota solo palabras clave y abreviaturas."),
        ("Ignorar however y el punto de vista contrario.", "Se queda con una sola versión de los hechos.", "Busca however y but, que anuncian otra mirada."),
    ],
    [
        ml(L1, "¿Qué hizo la municipalidad para resolver el problema?", "Organizó un bus gratuito desde la estación de trenes", ["Cerró la playa a los visitantes", "Prohibió los autos en todo el pueblo"], "Decided to run a free shuttle."),
        ml(L2, "¿Cuál es el propósito del discurso?", "Convencer a los compañeros de votar por ella", ["Informar de un cambio en las reglas del colegio", "Contar una anécdota de su curso con humor"], "Dice I am running for class president y promete cosas."),
        ml(L3, "¿Qué problema tenía la hablante?", "No sabía leer música y estaba nerviosa en el coro", ["No tenía voz para cantar con el resto del coro y por eso estaba nerviosa", "No tenía profesor de música en el colegio"], "Dice I could not read music."),
    ],
    [
        ml(L1, "¿Cada cuánto tiempo pasa el bus gratuito?", "Cada veinte minutos", ["Cada dos horas", "Cada nueve minutos"], "Dice every twenty minutes."),
        ml(L2, "¿Qué día lee la candidata el buzón de ideas?", "Los lunes", ["Los viernes", "Cada mes"], "Dice I will read it every Monday."),
        ml(L3, "¿Cuál fue la solución que sugirió la profesora?", "Escuchar cada canción dos veces en casa y seguir la letra", ["Cantar sola en el colegio todos los recreos", "Leer un libro sobre notas musicales cada día después de clases en casa"], "Dice I listened to each song twice at home and followed the words."),
    ],
    [
        ml(L1, "¿Quién dijo We want visitors to enjoy our town without causing problems?", "La alcaldesa Elena Costa", ["Un dueño de tienda", "Un vecino"], "El texto dice Mayor Elena Costa said."),
        ml(L1, "¿Qué opinión contraria tienen algunos dueños de tiendas?", "Que venden menos porque se detienen menos autos en el centro", ["Que venden más con el bus gratuito", "Que el pueblo está lleno de turistas"], "However introduce su queja."),
        ml(L3, "¿Cuál fue el resultado en la vida de la hablante?", "Ahora canta la segunda voz y ayuda a estudiantes nuevos", ["Dejó el coro por el nerviosismo", "Aprendió a tocar piano"], "Dice Now I sing the second voice."),
    ],
    [
        ml(L2, "¿Qué frase marca lo más importante para la candidata?", "Above all, I want everyone to feel heard", ["First, I will put an ideas box", "Second, I promise a monthly meeting"], "Above all señala lo más importante."),
        ml(L1, "Un oyente dice que el texto sirve para convencer de visitar Alder Bay. ¿Es correcto?", "No: informa un problema, una solución y opiniones sobre el resultado", ["Sí: dice que es un pueblo hermoso y que vale la pena visitarlo", "Sí: da el precio de los casilleros y dice que el pueblo recibe a miles de turistas"], "Es una noticia: expone hechos y puntos de vista."),
    ],
    [
        ml(L1, "¿Qué relación hay entre el bus gratuito y el tráfico cerca de la playa?", "El bus gratuito logró que el tráfico bajara", ["El bus aumentó el tráfico cerca de la playa", "No hay relación entre el bus y el tráfico"], "Dice So far, traffic near the beach has dropped."),
        ml(L2, "Una compañera dice que la candidata no escucha las críticas. ¿Qué dato del texto muestra lo contrario?", "Menciona lo que dicen algunos y responde que vale la pena", ["Dice que las críticas no merecen respuesta ni cambios", "Cancela la reunión mensual con el director para ahorrar tiempo"], "Some people say ..., but I think they are worth it: reconoce la crítica y responde."),
    ],
    [ml(L3, "Una estudiante nueva no sabe leer música. ¿Qué consejo del texto puede seguir?", "Escuchar cada canción dos veces y seguir la letra", ["Esperar un año completo hasta aprender la música con otra persona", "Cantar muy fuerte para no equivocarse"], "Es la solución que funcionó para la hablante.")],
    [
        ("En Inglés de 2.º medio (OA 3, clase 5): ¿cuántas veces conviene escuchar un texto largo?", "Tres: general, detalles y comprobación", "Cada escucha tiene un propósito."),
        ("En Inglés de 2.º medio (OA 3, clase 5): ¿qué anuncia however en un texto?", "Un punto de vista contrario", "Es un conector de contraste."),
        ("En Inglés de 2.º medio (OA 3, clase 5): ¿qué columnas de problema-solución aparecen en una ficha?", "Problem, solution y result", "Ordenan la estructura del texto."),
    ],
    task("Un adulto lee tres veces: «Good morning. Our community workshop is closing next month because the building will be sold. Members are very sad. The best solution is to find a new place. A school offered a small room, so we can move in April. Above all, we want to keep the community together. We need ten volunteers to help us move.» (community = comunitaria, closing = cerrando, building = edificio, sold = vendido, members = socios, room = sala, move = mudarnos, volunteers = voluntarios). Completa una ficha con propósito, problema, solución, lo más importante y un detalle.", "Propósito: informar y pedir ayuda. Problema: el edificio se vende y el taller cierra. Solución: mudarse a una sala de un colegio en abril. Lo más importante: mantener unida a la comunidad. Detalle: se necesitan diez voluntarios.", ["completa cinco filas de la ficha", "usa palabras clave del texto", "indica lo más importante con la señal above all"], ["ficha de cinco filas en la hoja"], ["confundir problema con solución", "anotar un detalle como lo más importante"], "Pide que explique con una frase por qué eligió esa idea como la más importante."),
    "Escucha otra vez la noticia de Alder Bay y anota con colores el problema, la solución y el resultado.",
    "Escribe en español un resumen de dos líneas de la historia del coro con problema, solución y resultado.",
)
