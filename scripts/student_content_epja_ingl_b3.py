"""Inglés EPJA Nivel 2, módulo 2 (OAD-07): conversar sobre el transporte de la comunidad y dar instrucciones para llegar del hogar al establecimiento. Textos inventados."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-07"

F1 = ("Dialogue (example): Ana: How do you get to work? Carlos: I take the bus. It's number 12. Ana: How long is the trip? Carlos: It's 40 minutes. "
      "Ana: And your wife? Carlos: She walks to work. Her job is near our house.")

F2 = ("Bus schedule (example), Route 12: The bus leaves Central Station at 6:30, 7:00, 7:30 and 8:00 a.m. It arrives at the school 25 minutes later: 6:55, 7:25, 7:55 and 8:25 a.m. "
      "The last bus leaves at 10:00 p.m. No buses on Sunday.")

F3 = ("Directions card (example): Go straight. Turn left. Turn right. Cross the street. Don't turn right. "
      "Map text: From the bus stop, go straight two blocks. Turn left at the corner. The school is next to the library. The pharmacy is inside the market.")

F4 = ("Dialogue (example): Marta: Excuse me, where is the health center? Mr. Lopez: Go straight on Main Street for two blocks. Turn right at the bakery. "
      "The health center is next to the park, on the left. Marta: Thank you! Mr. Lopez: You're welcome.")

F5 = ("Instructions (example) from Ana's house to the adult school: 1. Leave your house and turn left on Pine Street. 2. Walk three blocks. "
      "3. At the corner of Pine Street and Oak Avenue, take bus 12. 4. Get off at the park. 5. The school is on Oak Avenue, next to the library. Class starts at 7:00.")

F6 = ("Message (example) from Mr. Lopez: Hi Ana. My bus is late today. I'm going to school by subway. Take Line 1 too. Get off at Central Station. "
      "Then go straight one block. Turn right at the corner. Don't be late! Class starts at 7:00.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de cómo me muevo cada día y reconozco las palabras de transporte de mi comunidad en una conversación escrita.",
    prior=["Sé cómo me muevo por mi barrio y cómo se llaman en español los medios de transporte.", "Sé responder preguntas con How y What.", "Conozco el presente simple con he y she."],
    explain=[
        "Todas las personas se mueven por la ciudad de alguna manera: micro, metro, colectivo, bicicleta o a pie. Hoy ponemos esas formas en inglés.",
        "Para decir cómo vas a un lugar puedes usar go con by: I go by bus, We go by subway, She goes by taxi. Para caminar lo más natural es el verbo walk: I walk to work, She walks to work. También existe on foot (a pie), por ejemplo I go on foot, que se entiende bien pero se usa menos.",
        "También se usa el verbo take con el vehículo: I take the bus, He takes the subway. Es la forma más común en inglés estadounidense. Con he o she, take lleva -s: takes.",
        "Para preguntar cómo se va, lo natural es How do you get to work? (get to = llegar a). Para preguntar cuánto demora, usa How long is the trip? La respuesta puede ser: It's 40 minutes.",
    ],
    vocab=[("bus", "micro, bus"), ("subway", "metro"), ("taxi", "taxi"), ("bike", "bicicleta"), ("walk", "caminar"), ("on foot", "a pie"), ("trip", "viaje, trayecto"), ("near", "cerca de")],
    worked=[
        ("Decir cómo voy", "Quieres decir: «Voy al trabajo en metro».", ["Voy: I go.", "En metro: by subway.", "Uno las partes: I go to work by subway."], "I go to work by subway."),
        ("Hablar de otra persona", "Quieres decir: «La vecina toma la micro».", ["La vecina es she.", "Take con she lleva -s: takes.", "Escribo: My neighbor takes the bus."], "My neighbor takes the bus."),
    ],
    mistakes=[("Escribir «She walk to work».", "Con he, she e it el verbo del presente simple lleva -s.", "Escribe She walks to work."),
              ("Decir «I go in bus» para viajar en micro.", "Con vehículos públicos se usa by: by bus, by subway.", "Escribe I go by bus o, mejor, I take the bus.")],
    T=[
        ("abc", "{F} How does Carlos go to work?", "By bus", "On foot", "By taxi", "Carlos dice «I take the bus»."),
        ("{F} What is the bus number? Escribe solo el número.", "12", "Carlos dice «It's number 12»; el 40 es la duración del viaje, no el número del bus."),
        ("{F} How many minutes is Carlos's trip? Escribe solo el número.", "40", "A la pregunta How long, Carlos responde «It's 40 minutes», es decir, la duración del viaje."),
        ("ab", "{F} How does Carlos's wife get to work?", "She walks.", "She takes a taxi.", "El texto dice «She walks to work»; no menciona ningún taxi."),
        ("abc", "{F} Why does she walk to work?", "Her job is near their house", "She has a bike", "The bus is expensive", "El texto dice «Her job is near our house»."),
        ("abc", "La expresión «on foot» significa:", "A pie", "En bicicleta", "En taxi", "On foot es ir caminando, con los pies, y equivale al verbo walk."),
        ("abc", "Dices en inglés: «Yo voy al trabajo en metro». ¿Cuál es la oración correcta?", "I go to work by subway.", "I go to work for subway.", "I am subway to work.", "Con vehículos se usa go by y el nombre del vehículo."),
        ("ab", "Elige la oración correcta.", "She walks to work.", "She walk to work.", "Con she, el verbo walk lleva -s en el presente simple."),
        ("abc", "«How do you go to work?» significa:", "¿Cómo vas al trabajo?", "¿Dónde trabajas?", "¿Cuánto cuesta el trabajo?", "How do you go pregunta por la manera de ir a un lugar."),
        ("abc", "Completa: My brother ___ the bus to school.", "takes", "take", "taking", "My brother es he y con he el verbo lleva -s."),
        ("abc", "Completa: We ___ to work by taxi.", "go", "goes", "going", "Con we el verbo del presente simple queda sin -s."),
        ("ab", "Alguien pregunta: «Does Carlos take a taxi?» Elige la respuesta corta correcta.", "No, he doesn't.", "No, he don't.", "Carlos toma el bus y con he se usa doesn't."),
        ("abc", "¿Cuál de estas palabras es un vehículo de dos ruedas para una persona?", "Bike", "Bus", "Subway", "Una bike es una bicicleta, con dos ruedas."),
    ],
    ctx=("abc", "En tu barrio (ejemplo) una vecina te pregunta en inglés: «How do you get to the market?» Tú vas caminando. ¿Qué respondes?", "I walk.", "I go for foot.", "I am foot.", "Para ir caminando se usa el verbo walk: I walk."),
    sc=[("¿Cómo digo «a pie» en inglés?", "On foot", "On foot es la expresión para caminar."),
        ("Completa: She ___ the subway.", "takes", "She es tercera persona singular, y el verbo take del presente simple lleva -s."),
        ("¿Qué pregunta uso para saber cuánto demora un trayecto?", "How long is the trip?", "How long pregunta por la duración.")],
    op=("Lee el diálogo: {F} Escribe en tu cuaderno tres oraciones sobre cómo te mueves tú y cómo se mueve una persona cercana (datos de ejemplo): usa go by, take o on foot.",
        "I go to work by bus. My sister takes the subway. My neighbor goes on foot.",
        ["escribe tres oraciones", "usa by, take u on foot", "usa -s con he o she"],
        ["tres oraciones sobre transporte"],
        ["escribir «She go»", "decir «in bus» en vez de by bus"],
        "Pregunta: «¿Cuánto demora ese trayecto?»."),
    reinforce="Escribe cómo vas tú a tres lugares distintos (trabajo, feria, consultorio) con by o on foot.",
    extend="Pregunta a otra persona «How do you go to work?» y anota su respuesta en inglés.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy reconozco el vocabulario de horarios de transporte y aprendo a preguntar y decir a qué hora sale y llega un bus.",
    prior=["Sé decir el transporte que uso.", "Leo horas como 7:30.", "Uso What time con el presente simple."],
    explain=[
        "Un horario de transporte (schedule) dice a qué hora sale (leaves) y a qué hora llega (arrives) un bus. Con los números y esas dos palabras ya entiendes casi todo.",
        "Para preguntar la hora usa What time: What time does the bus leave? What time does it arrive? Con he, she e it, la pregunta lleva does y el verbo queda sin -s.",
        "Para responder, usa at más la hora: The bus leaves at 7:00. It arrives at 7:25. Las siglas a.m. significan antes del mediodía y p.m. después del mediodía.",
        "También hay palabras de orden: first (primero), next (siguiente), last (último). The last bus leaves at 10:00 p.m.",
    ],
    vocab=[("schedule", "horario"), ("leaves", "sale"), ("arrives", "llega"), ("station", "estación"), ("first", "primero"), ("next", "siguiente"), ("last", "último")],
    worked=[
        ("Leer un horario", "Schedule (example): «The bus leaves at 7:00. It arrives at 7:25.»", ["Sale a las 7:00.", "Llega a las 7:25.", "La diferencia es de 25 minutos."], "El viaje dura 25 minutos"),
        ("Preguntar la hora", "Quieres preguntar a qué hora sale el bus.", ["Uso What time.", "Con the bus (it) uso does.", "El verbo queda sin -s: leave."], "What time does the bus leave?"),
    ],
    mistakes=[("Escribir «What time does the bus leaves?».", "Después de does el verbo vuelve a su forma base, sin -s.", "Escribe What time does the bus leave?"),
              ("Confundir leaves con arrives.", "Una palabra es salida y la otra es llegada.", "Leaves = sale, arrives = llega.")],
    T=[
        ("abc", "{F} Where does the bus leave from?", "Central Station", "The school", "The market", "El texto dice «leaves Central Station»."),
        ("abc", "{F} What time does the first bus leave?", "6:30", "7:00", "10:00", "La primera hora de salida es 6:30."),
        ("{F} What time does the 7:00 bus arrive? Escribe solo la hora, por ejemplo 9:00.", "7:25", "El horario dice que cada bus llega 25 minutos después de salir, así que el de las 7:00 llega a las 7:25."),
        ("ab", "{F} Is there a bus on Sunday?", "No, there isn't.", "Yes, there is.", "El texto dice «No buses on Sunday»."),
        ("abc", "{F} What time does the last bus leave?", "10:00 p.m.", "8:00 a.m.", "6:30 p.m.", "El texto dice «The last bus leaves at 10:00 p.m.»."),
        ("abc", "En un horario, «arrives» significa:", "Llega", "Sale", "Espera", "Arrives indica la llegada del bus."),
        ("ab", "En un horario, «leaves» significa:", "Sale", "Llega", "Leaves indica la hora en que el bus parte."),
        ("abc", "Completa la pregunta: What time ___ the bus leave?", "does", "do", "is", "Con the bus (it) se usa does y el verbo queda sin -s."),
        ("abc", "Traduce: «El bus llega a las 8:25».", "The bus arrives at 8:25.", "The bus arrive at 8:25.", "The bus leaves at 8:25.", "Con the bus (it) el verbo lleva -s: arrives."),
        ("{F} How many a.m. departures from Central Station are listed? Escribe el número.", "4", "Las salidas a.m. son 6:30, 7:00, 7:30 y 8:00, o sea, cuatro; el bus de las 10:00 p.m. es el último de la noche."),
        ("{F} You arrive at the station at 7:10. What time does the next bus leave? Escribe solo la hora, por ejemplo 9:00.", "7:30", "A las 7:10 el bus de las 7:00 ya salió, entonces el próximo sale a las 7:30."),
        ("ab", "¿Qué significa «p.m.»?", "Después del mediodía", "Antes del mediodía", "p.m. se usa para las horas de la tarde y la noche."),
        ("{F} How many minutes does the trip take? Escribe solo el número.", "25", "De 6:30 a 6:55 pasan 25 minutos."),
    ],
    ctx=("abc", "Estás en una estación (ejemplo) y alguien te pregunta en inglés: «What time does the last bus leave?» El último sale a las 10:00 p.m. ¿Qué respondes?", "At 10:00 p.m.", "At 10:00 a.m.", "At 8:00 p.m.", "Se responde con at más la hora correcta."),
    sc=[("¿Qué significa «schedule»?", "Horario", "Schedule es el cuadro de horas del transporte."),
        ("Completa: The bus ___ at 7:00.", "leaves", "Con the bus (it) el verbo lleva -s."),
        ("¿Cómo pregunto la hora de llegada de un bus?", "What time does the bus arrive?", "Con does, el verbo queda sin -s.")],
    op=("Lee el horario: {F} Escribe en tu cuaderno cuatro oraciones sobre el horario de un transporte que usas (datos de ejemplo): cuándo sale, cuándo llega y cuál es el último.",
        "The bus leaves at 7:00. It arrives at 7:30. The first bus leaves at 6:00. The last bus leaves at 10:00 p.m.",
        ["escribe cuatro oraciones", "usa leaves y arrives", "usa at con cada hora"],
        ["cuatro oraciones con horas"],
        ["escribir «does leaves»", "olvidar at antes de la hora"],
        "Pregunta: «¿Cuánto demora el viaje?»."),
    reinforce="Mira el horario de un bus de tu barrio y escribe tres horas en inglés con at.",
    extend="Haz dos preguntas con What time does...? sobre un horario y pide a otra persona que las responda.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a dar instrucciones para llegar a un lugar con las palabras go straight, turn left, turn right y next to.",
    prior=["Sé las palabras izquierda y derecha en español.", "Conozco algunos lugares de la ciudad.", "Puedo leer una oración corta en inglés."],
    explain=[
        "Para dar direcciones usamos órdenes cortas: go straight (sigue derecho), turn left (gira a la izquierda), turn right (gira a la derecha), cross the street (cruza la calle). En esta clase las presentamos como expresiones completas, sin teoría nueva.",
        "Para decir dónde está algo usamos preposiciones de lugar: next to (al lado de), at the corner (en la esquina), inside (dentro de), on (en, sobre una calle). Ejemplo: The school is next to the library.",
        "Para decir cuántas cuadras, usa un número y blocks: go straight two blocks. Si es una sola, se dice one block.",
        "Para decir que no hagas algo, se usa Don't antes de la orden: Don't turn right. Es otra expresión útil y se aprende completa.",
    ],
    vocab=[("go straight", "sigue derecho"), ("turn left", "gira a la izquierda"), ("turn right", "gira a la derecha"), ("next to", "al lado de"), ("corner", "esquina"), ("block", "cuadra"), ("inside", "dentro de")],
    worked=[
        ("Seguir una dirección", "Map text (example): «Go straight two blocks. Turn left at the corner.»", ["Primero: sigue derecho dos cuadras.", "Segundo: en la esquina, gira a la izquierda."], "Dos cuadras derecho y luego izquierda"),
        ("Decir dónde está un lugar", "Quieres decir: «La escuela está al lado de la biblioteca».", ["La escuela: the school.", "Está: is.", "Al lado de: next to."], "The school is next to the library."),
    ],
    mistakes=[("Escribir «two block».", "Con dos o más, block lleva -s: blocks.", "Escribe two blocks."),
              ("Confundir left con right.", "Giras al lado equivocado.", "Dibuja un mapa corto y marca L y R antes de decir la dirección.")],
    T=[
        ("abc", "{F} En las direcciones, «go straight» significa:", "Sigue derecho", "Gira a la izquierda", "Cruza la calle", "Go straight es seguir sin girar."),
        ("abc", "{F} En las direcciones, «turn left» significa:", "Gira a la izquierda", "Gira a la derecha", "Sigue derecho", "Left significa izquierda, y turn left es girar hacia ese lado."),
        ("abc", "{F} En las direcciones, «turn right» significa:", "Gira a la derecha", "Gira a la izquierda", "Cruza la calle", "Right significa derecha, y turn right es girar hacia ese lado; no es lo mismo que left."),
        ("ab", "{F} «Next to» significa:", "Al lado de", "Lejos de", "Next to indica que dos cosas están una junto a la otra."),
        ("abc", "{F} Completa: The school is ___ the library.", "next to", "go straight", "turn left", "Para decir dónde está algo usamos next to."),
        ("abc", "{F} «At the corner» significa:", "En la esquina", "En la mitad de la calle", "Dentro del mercado", "Corner es la esquina, el punto donde se juntan dos calles."),
        ("Ordena las palabras: Turn / left / at / the / corner. Escribe la oración.", "Turn left at the corner.", "La orden empieza con turn y luego la dirección y el lugar."),
        ("abc", "Traduce: «Cruza la calle».", "Cross the street.", "Turn the street.", "Go the street left.", "Cross significa cruzar, y se usa con the street sin otra palabra en medio."),
        ("abc", "{F} Where is the school?", "Next to the library", "Inside the market", "Next to the pharmacy", "El texto dice «The school is next to the library»."),
        ("ab", "Elige la oración correcta.", "Go straight two blocks.", "Go straight two block.", "Con dos o más, block lleva -s."),
        ("abc", "«Don't turn right» significa:", "No gires a la derecha", "Gira a la derecha", "Sigue derecho", "Don't antes de la orden indica que no se debe hacer."),
        ("{F} How many blocks do you go straight in the map text? Escribe el número.", "2", "El texto dice «go straight two blocks»."),
        ("ab", "{F} «The pharmacy is inside the market» significa:", "La farmacia está dentro del mercado", "La farmacia está al lado del mercado", "Inside quiere decir dentro de algo."),
    ],
    ctx=("abc", "Una vecina (ejemplo) te pregunta en inglés cómo llegar a la plaza. La plaza está a dos cuadras derecho y luego a la izquierda. ¿Qué respondes?", "Go straight two blocks. Turn left.", "Turn left two blocks. Go straight.", "Cross two blocks. Next to left.", "Primero se indica seguir derecho y luego girar."),
    sc=[("¿Cómo digo «gira a la izquierda»?", "Turn left", "Left es izquierda y turn es girar."),
        ("Si en un mapa de ejemplo lees «The bank is next to the park», ¿qué significa next to?", "Al lado de", "Next to indica que un lugar está justo al lado de otro, sin nada entre los dos."),
        ("¿Cómo digo «dos cuadras»?", "Two blocks", "Con dos o más, el sustantivo block va en plural, con -s.")],
    op=("Revisa la tarjeta de direcciones: {F} Escribe en tu cuaderno tres pasos para llegar de la parada de bus a un lugar de tu barrio (datos de ejemplo): usa go straight, turn left o right y next to.",
        "Go straight two blocks. Turn right at the corner. The pharmacy is next to the bakery.",
        ["escribe tres pasos", "usa go straight y turn", "usa next to o at the corner"],
        ["tres oraciones de instrucción"],
        ["confundir izquierda con derecha", "escribir «two block»"],
        "Pregunta: «¿Cuántas cuadras hay y dónde se gira?»."),
    reinforce="Elige un lugar de tu barrio y escribe dos direcciones para llegar con turn y go straight.",
    extend="Dibuja un mapa pequeño de tu barrio y escribe tres frases con next to.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo un diálogo para preguntar y dar direcciones, y respondo preguntas sobre lo que dice cada persona.",
    prior=["Sé decir go straight, turn left y turn right.", "Conozco next to y at the corner.", "Sé responder preguntas con where."],
    explain=[
        "Para pedir ayuda a una persona desconocida, empieza con Excuse me (disculpe). Luego pregunta: Where is the health center? (¿Dónde está el centro de salud?). Con una cosa se dice is.",
        "Quien responde da pasos en orden: primero seguir derecho, luego girar, al final decir dónde queda el lugar. Para decir de qué lado queda, usa on the left o on the right.",
        "Las cortesías son parte de comunicarse: Thank you (gracias) y You're welcome (de nada). Usarlas hace la conversación más amable, aunque tengas poco vocabulario.",
        "Practica en parejas: una persona lee la pregunta, la otra busca la respuesta en el texto, y después cambian.",
    ],
    vocab=[("excuse me", "disculpe"), ("health center", "centro de salud"), ("bakery", "panadería"), ("park", "parque"), ("on the left", "a la izquierda"), ("on the right", "a la derecha"), ("you're welcome", "de nada")],
    worked=[
        ("Preguntar por un lugar", "Quieres preguntar dónde está la panadería.", ["Empiezo con Excuse me.", "Pregunto: Where is the bakery?"], "Excuse me, where is the bakery?"),
        ("Seguir las instrucciones", "Instrucciones: «Go straight for two blocks. Turn right at the bakery.»", ["Primero: dos cuadras derecho.", "Después: en la panadería, a la derecha."], "Dos cuadras derecho y luego derecha en la panadería"),
    ],
    mistakes=[("Preguntar «Where are the health center?».", "Health center es una sola cosa y lleva is.", "Escribe Where is the health center?"),
              ("Olvidar saludar con cortesía.", "Una pregunta sin saludo o gracias suena seca.", "Empieza con Excuse me y termina con Thank you.")],
    T=[
        ("abc", "{F} What is Marta looking for?", "The health center", "The bakery", "The park", "Marta pregunta «Where is the health center?»."),
        ("abc", "{F} Where does Marta turn right?", "At the bakery", "At the park", "At the corner of Main Street", "El señor dice «Turn right at the bakery»."),
        ("{F} How many blocks does Marta go straight? Escribe solo el número.", "2", "El señor dice «for two blocks»."),
        ("ab", "{F} Where is the health center?", "Next to the park", "Next to the bakery", "El señor dice «next to the park»."),
        ("abc", "{F} Is the health center on the left or on the right?", "On the left", "On the right", "Inside the park", "La última indicación dice «on the left»."),
        ("abc", "{F} Who asks the question?", "Marta", "Mr. Lopez", "The baker", "Marta empieza el diálogo con «Excuse me»."),
        ("abc", "«Excuse me» se usa para:", "Llamar la atención con cortesía", "Despedirse", "Pedir comida", "Excuse me sirve para empezar a hablar con una persona."),
        ("abc", "«You're welcome» es la respuesta a:", "Thank you", "Excuse me", "Good morning", "You're welcome es la forma de decir «de nada» cuando alguien da las gracias."),
        ("abc", "{F} Completa lo que dice el señor: Go ___ on Main Street for two blocks.", "straight", "left", "corner", "El diálogo dice «Go straight on Main Street»: primero se sigue derecho y recién después se gira."),
        ("abc", "{F} Completa lo que dice el señor: Turn ___ at the bakery.", "right", "straight", "next", "El señor dice «Turn right at the bakery»; turn straight y turn next no existen como instrucción."),
        ("ab", "{F} ¿Cuál es el segundo paso?", "Turn right at the bakery", "Go straight on Main Street", "El primer paso es seguir derecho y el segundo girar."),
        ("ab", "Elige la pregunta correcta.", "Where is the health center?", "Where are the health center?", "Health center es singular y lleva is."),
        ("abc", "{F} «The health center is on the left» significa:", "El centro de salud está a la izquierda", "El centro de salud está a la derecha", "El centro de salud está lejos", "On the left indica el lado izquierdo; nada en la frase dice que esté lejos."),
    ],
    ctx=("abc", "Tomas micro en una ciudad que no conoces (ejemplo) y quieres preguntar a una persona dónde está el mercado. ¿Qué dices?", "Excuse me, where is the market?", "Excuse me, where are market?", "Where is you the market?", "Se empieza con cortesía y se usa Where is para un lugar."),
    sc=[("¿Cómo pido ayuda con cortesía para llegar a un lugar?", "Excuse me, where is...?", "Excuse me abre la conversación y Where is pregunta el lugar."),
        ("¿Qué significa «on the right»?", "A la derecha", "On the right indica el lado derecho, al contrario de on the left."),
        ("¿Qué contesto a «Thank you»?", "You're welcome", "Es la respuesta cortés a un agradecimiento.")],
    op=("Lee el diálogo: {F} Escribe en tu cuaderno un diálogo de seis líneas entre dos personas: una pregunta dónde queda un lugar (datos de ejemplo) y la otra da dos instrucciones y dice de qué lado queda.",
        "A: Excuse me, where is the bank? B: Go straight one block. Turn left at the corner. The bank is on the right. A: Thank you! B: You're welcome.",
        ["escribe un diálogo de seis líneas", "usa Excuse me y Where is", "da dos instrucciones y un lado"],
        ["un diálogo corto"],
        ["olvidar Excuse me", "no decir de qué lado queda el lugar"],
        "Pregunta: «¿Cómo suena el diálogo si lo lees en voz alta con otra persona?»."),
    reinforce="Lee el diálogo en voz alta con otra persona, una lee la pregunta y la otra la respuesta.",
    extend="Escribe cómo llegar de tu casa a una panadería cercana en tres pasos.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a una situación real: leo y escribo instrucciones para llegar de mi casa al establecimiento donde estudio.",
    prior=["Sé dar direcciones con go straight y turn.", "Conozco los números y ordinales básicos.", "Sé nombrar el transporte que uso."],
    explain=[
        "Dar instrucciones para llegar al establecimiento es una situación real: puede ser para una compañera nueva o un familiar. Se escriben en pasos numerados y en orden.",
        "Los números ordinales ayudan a ordenar: first (primero), second (segundo), third (tercero), fourth (cuarto), fifth (quinto). En la lista se usan números simples: 1, 2, 3.",
        "Usa verbos de acción en forma de orden: Leave your house, Walk three blocks, Take bus 12, Get off at the park. Son expresiones completas que sirven en la vida diaria.",
        "No pongas tu dirección real. Usa calles de ejemplo, como Pine Street y Oak Avenue, para practicar sin datos personales.",
    ],
    vocab=[("leave", "salir de"), ("walk", "caminar"), ("get off", "bajarse"), ("street", "calle"), ("avenue", "avenida"), ("library", "biblioteca"), ("class", "clase")],
    worked=[
        ("Leer los pasos en orden", "Instructions (example): «1. Leave your house. 2. Walk three blocks.»", ["Paso 1: sales de tu casa.", "Paso 2: caminas tres cuadras."], "Salir de la casa y caminar tres cuadras"),
        ("Escribir un paso", "Quieres escribir el paso: «Camina cuatro cuadras».", ["Camina: Walk.", "Cuatro cuadras: four blocks.", "Uno las partes."], "Walk four blocks."),
    ],
    mistakes=[("Mezclar el orden de los pasos.", "La persona se pierde si los pasos no siguen el camino real.", "Numera los pasos y recorre el camino en tu mente de principio a fin."),
              ("Escribir «Get of at the park».", "La expresión correcta es get off, con dos f.", "Escribe Get off at the park.")],
    T=[
        ("{F} How many blocks do you walk? Escribe solo el número.", "3", "El segundo paso dice «Walk three blocks»."),
        ("abc", "{F} Which street do you turn left onto?", "Pine Street", "Oak Avenue", "Main Street", "El primer paso dice «turn left on Pine Street»."),
        ("{F} Which bus do you take? Escribe solo el número.", "12", "El tercer paso dice «take bus 12»."),
        ("abc", "{F} Where do you get off?", "At the park", "At the library", "At the corner of Pine Street", "El cuarto paso dice «Get off at the park»."),
        ("abc", "{F} Where is the school?", "On Oak Avenue, next to the library", "On Pine Street, inside the park", "At the corner of Main Street", "El paso 5 dice «The school is on Oak Avenue, next to the library»."),
        ("ab", "{F} ¿Cuál es el segundo paso?", "Walk three blocks.", "Take bus 12.", "El segundo paso es caminar tres cuadras."),
        ("abc", "«Third» significa:", "Tercero", "Cuarto", "Segundo", "Third es el ordinal de tres."),
        ("{F} What time does class start? Escribe solo la hora, por ejemplo 9:00.", "7:00", "El texto termina con «Class starts at 7:00»."),
        ("ab", "En las instrucciones, «get off» significa:", "Bajarse", "Subirse", "Get off es bajar de un vehículo."),
        ("abc", "Traduce: «Camina tres cuadras».", "Walk three blocks.", "Walks three block.", "Walk three blocking.", "Con una orden el verbo va en forma base y blocks lleva -s."),
        ("abc", "Escribe el paso 4 de otra ruta (ejemplo): «Bájate en la plaza».", "Get off at the square.", "Get of at the square.", "Gets off the square.", "La expresión es get off, con dos f."),
        ("abc", "«Turn right on Pine Street» significa:", "Gira a la derecha en la calle Pine", "Sigue derecho por la calle Pine", "Cruza la calle Pine", "Turn right es girar a la derecha."),
        ("abc", "Completa: The school is ___ the library.", "next to", "get off", "walk", "Next to indica que están uno al lado del otro."),
    ],
    ctx=("abc", "Una compañera nueva (ejemplo) te pregunta cómo llegar a tu centro de estudios desde la plaza. Debes dar dos pasos. ¿Cuál es una buena respuesta?", "First, go straight two blocks. Second, turn left at the corner.", "First, left. Second, block.", "Go left two blocks. Next to straight.", "Los pasos usan first y second y verbos de acción en orden."),
    sc=[("¿Cuál es el ordinal de 1?", "First", "First es el ordinal de uno; second es el de dos y third el de tres."),
        ("¿Cómo digo «bájate en el parque»?", "Get off at the park.", "Get off es bajar de un vehículo."),
        ("Completa: Walk two ___.", "blocks", "Con dos, block va en plural.")],
    op=("Revisa las instrucciones de Ana: {F} Escribe en tu cuaderno cinco pasos para llegar de una casa de ejemplo a tu centro de estudios (calles de ejemplo, no reales). Después léelos en voz alta a otra persona.",
        "1. Leave your house and turn right on Elm Street. 2. Walk two blocks. 3. Take bus 15. 4. Get off at the square. 5. The school is next to the bank.",
        ["escribe cinco pasos en orden", "usa verbos como leave, walk, take o get off", "usa next to o on"],
        ["cinco pasos numerados"],
        ["usar la dirección real", "desordenar los pasos"],
        "Pregunta: «¿En cuántos pasos llegas al establecimiento?»."),
    reinforce="Lee las instrucciones de Ana y marca el verbo de cada paso.",
    extend="Explica a otra persona, de palabra, cómo llegar a tu lugar de trabajo desde la plaza más cercana.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado sobre transporte, horarios y direcciones, me autoevalúo y decido qué practicar después.",
    prior=["Hablé de cómo me muevo.", "Leí horarios y di direcciones.", "Escribí instrucciones para llegar a un lugar."],
    explain=[
        "Revisar lo logrado es mirar qué ahora puedes hacer en inglés: decir cómo vas a un lugar, leer un horario, dar direcciones y escribir instrucciones en pasos.",
        "Para revisar tus instrucciones comprueba cuatro cosas: ¿van en orden?, ¿usé turn left o right sin confundir?, ¿usé blocks con -s?, ¿usé next to o at the corner para el lugar?",
        "En este mensaje hay un cambio: el bus de Mr. Lopez llega tarde y usa otro transporte. Eso pasa en la vida real, y por eso conviene saber varias rutas.",
        "Sin audio no puedes comprobar la pronunciación. Pide a otra persona que lea las instrucciones en voz alta y repite las partes más difíciles.",
    ],
    vocab=[("late", "tarde, atrasado"), ("line", "línea"), ("today", "hoy"), ("too", "también"), ("then", "luego"), ("don't be late", "no llegues tarde")],
    worked=[
        ("Seguir una ruta nueva", "Message (example): «Take Line 1. Get off at Central Station. Then go straight one block.»", ["Primero: toma la línea 1.", "Segundo: bájate en la estación central.", "Tercero: sigue derecho una cuadra."], "Tres pasos en orden"),
        ("Corregir una instrucción", "Alguien escribe: «Go straight two block.»", ["Veo el número dos: hay más de una cuadra.", "Con dos o más, block va en plural y lleva -s.", "Corrijo: Go straight two blocks."], "Go straight two blocks."),
    ],
    mistakes=[("Olvidar el orden de las instrucciones.", "La ruta no funciona si los pasos están desordenados.", "Usa then, first o second para marcar el orden."),
              ("Confundir «I'm going» con «I go».", "El primero indica lo que ocurre hoy y el segundo un hábito.", "Para hoy usa I'm going; para todos los días usa I go.")],
    T=[
        ("abc", "{F} Why does Mr. Lopez change his transport?", "His bus is late", "His bike is broken", "It is Sunday", "El texto dice «My bus is late today»."),
        ("abc", "{F} How does Mr. Lopez go to school today?", "By subway", "By taxi", "On foot", "Dice «I'm going to school by subway»."),
        ("abc", "{F} Where does Ana get off?", "At Central Station", "At the park", "At the library", "El mensaje dice «Get off at Central Station»."),
        ("{F} How many blocks do you go straight after the station? Escribe el número.", "1", "El mensaje dice «go straight one block»."),
        ("ab", "{F} Where do you turn right?", "At the corner", "At the bakery", "El mensaje dice «Turn right at the corner»."),
        ("{F} What time does class start? Escribe solo la hora, por ejemplo 9:00.", "7:00", "El mensaje dice «Class starts at 7:00»."),
        ("ab", "{F} «Don't be late!» significa:", "No llegues tarde", "Llega tarde", "Don't indica que no debes hacer algo."),
        ("abc", "Traduce: «Hoy voy a la escuela en metro».", "I'm going to school by subway today.", "I go to school for subway today.", "I'm subway to school today.", "Para hoy se usa I'm going y el vehículo con by."),
        ("abc", "Completa: Take Line 1 ___.", "too", "block", "left", "Too significa también y va al final de la oración."),
        ("ab", "Corrige: «Turn to right at the corner».", "Turn right at the corner.", "Turn right at the corners.", "Con turn se usa directamente right, sin to."),
        ("abc", "Ordena la ruta: Get off, take Line 1, go straight. ¿Cuál es el orden correcto?", "Take Line 1, get off, go straight", "Go straight, take Line 1, get off", "Get off, go straight, take Line 1", "Primero subes, luego bajas y después caminas."),
        ("abc", "¿Qué oración tiene un error?", "She take the bus.", "She takes the bus.", "He goes on foot.", "Con she, take debe llevar -s."),
        ("abc", "Un vecino (ejemplo) dice «The bank is next to the pharmacy». ¿Qué significa?", "El banco está al lado de la farmacia", "El banco está dentro de la farmacia", "El banco está lejos de la farmacia", "Next to es al lado de."),
    ],
    ctx=("abc", "Un compañero (ejemplo) te escribe: «My bus is late. How do I get to school?» (get to = llegar a). Tú sabes que el metro llega a una estación cerca. ¿Qué respondes?", "Take the subway. Get off at Central Station.", "Take the school. Get off the subway.", "Go the subway. Get on Central.", "La respuesta usa take y get off con el lugar."),
    sc=[("¿Cómo escribo el orden de una ruta?", "Con pasos numerados o con first, second y then", "Los pasos en orden evitan confusiones."),
        ("Completa: He ___ on foot.", "goes", "Con he el verbo lleva -es."),
        ("¿Qué quiero practicar la próxima semana?", "Elijo una parte y la anoto", "Una meta propia ayuda a avanzar.")],
    op=("Haz la revisión final: {F} Escribe en tu cuaderno un mensaje de seis oraciones a una compañera: dice cómo vas tú al establecimiento, qué horario usas y tres pasos de dirección. Después anota un logro y un paso siguiente.",
        "I go to school by bus. The bus leaves at 6:30. First, leave your house. Second, take bus 12. Third, get off at the park. Achieved: directions. Next: more verbs.",
        ["escribe seis oraciones", "incluye transporte, hora y tres pasos", "anota un logro y un paso siguiente"],
        ["un mensaje y dos frases de autoevaluación"],
        ["no ordenar los pasos", "olvidar la hora"],
        "Pregunta: «¿Qué paso te costó más escribir?»."),
    reinforce="Repasa la tarjeta de direcciones de la clase 3 y escribe cuatro pasos nuevos.",
    extend="Prepara una ruta de ejemplo de tu casa a un lugar de la comunidad y léela a otra persona.",
)
