"""Cuaderno del estudiante, 8.º básico Inglés (oficial), IN08 OA 09 (textos impresos y digitales) y OA 10 (lectura crítica de textos no literarios funcionales).

Todos los textos son originales, breves y vienen escritos en el enunciado con su pista en español.
Los datos de gráficos, personas y direcciones son de ejemplo.
"""
from __future__ import annotations

from student_content_in8_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA9 = "IN08 OA 09"
OA10 = "IN08 OA 10"
MAT = "Los textos escritos en cada ejercicio, lápiz y una hoja para anotar."

EMAIL = "«From: Ms. Vera. To: Class 8B. Subject: Science project. Hello, 8B. Please bring a plastic bottle and a ruler on Monday. We will build a rain gauge. Best wishes, Ms. Vera.» (project = proyecto, bring = traer, ruler = regla, rain gauge = pluviómetro, best wishes = saludos)"
WEB = "«Home | Events | Contact. Events: Beach Clean-up. Saturday, 9:00. Meet at the pier. Bring gloves and a bag. Free for everyone.» (events = actividades, clean-up = limpieza, pier = muelle, gloves = guantes, bag = bolsa, free = gratis)"
CHAT = "«Lía: Are you coming to the match? Tomás: Yes! What time? Lía: 4:30 at the field. Tomás: Great, see you!» (match = partido, field = cancha, see you = nos vemos)"
YAWN = "«Why do we yawn? Scientists are still studying this question. Yawning often happens when we are tired or bored. It also seems to be contagious: when one person yawns, others often do too.» (yawn = bostezar, still = todavía, bored = aburrido, contagious = contagioso)"

# ================================================================== OA 9, clase 1
lesson(
    OA9, 1, MAT,
    "Aprenderé a reconocer el tipo de texto impreso o digital (correo, página web, chat, artículo) y su propósito. Sirve para saber qué buscar antes de leer los detalles.",
    ["Sé reconocer anécdotas, entrevistas y exposiciones al escuchar.", "Conozco palabras como bring, free y subject."],
    [
        "Los textos impresos (en papel) y digitales (en pantalla) tienen formatos distintos. Un correo electrónico (email) tiene From, To y Subject, un saludo y una despedida como Best wishes. Una página web (web page) tiene un menú, por ejemplo Home | Events | Contact, y títulos. Un chat (chat) tiene mensajes cortos por turnos con nombres. Un artículo de revista (magazine article) tiene un título que presenta un tema y párrafos que lo explican.",
        "El propósito (purpose) es la razón del texto: pedir algo, informar de una actividad, coordinar un plan o explicar un tema. En el correo de la profesora, el propósito es pedir que traigan materiales. En la página web de eventos, es informar de una actividad. En el chat, es coordinar un partido. En el artículo del bostezo, es informar sobre un tema de ciencia.",
        "Antes de leer en detalle, mira el formato y los títulos: te dicen qué tipo de texto es y qué datos puedes esperar. En una página de eventos esperas fecha, hora y lugar; en un artículo, una explicación; en un chat, preguntas y respuestas rápidas. Así lees con un propósito y encuentras la información más rápido.",
    ],
    [("email", "correo electrónico"), ("web page", "página web"), ("chat", "chat: mensajes cortos por turnos"), ("article", "artículo"), ("subject", "asunto del correo"), ("purpose", "propósito: para qué se escribe un texto")],
    [
        ("Reconocer el formato", EMAIL + " ¿Qué tipo de texto es y qué pistas lo muestran?", ["Tiene From, To y Subject.", "Tiene saludo y despedida.", "Son pistas de un correo electrónico."], "Un correo electrónico: tiene From, To, Subject, saludo y despedida"),
        ("Reconocer el propósito", WEB + " ¿Para qué sirve este texto?", ["Es una página de actividades.", "Dice día, hora, lugar y qué llevar.", "Sirve para informar de una actividad."], "Informar de una limpieza de playa"),
    ],
    [
        ("Decir que un chat es un artículo porque habla de un partido.", "El tema no define el tipo de texto; el formato sí.", "Mira si hay mensajes por turnos con nombres."),
        ("Pensar que una página web siempre cuenta una historia.", "Muchas páginas informan sobre horarios, lugares o precios.", "Revisa el menú y los títulos."),
    ],
    [
        (EMAIL + " ¿Qué tipo de texto es? a) un correo electrónico b) un artículo de revista", "a) un correo electrónico", "Tiene From, To y Subject."),
        (WEB + " ¿Qué pista muestra que es una página web? a) el menú Home | Events | Contact b) la firma Best wishes", "a) el menú Home | Events | Contact", "Un menú de navegación es propio de una página web."),
        (CHAT + " ¿Cuántas personas hablan?", "2", "Hablan Lía y Tomás."),
    ],
    [
        (EMAIL + " ¿Cuál es el propósito? a) pedir que traigan materiales para un proyecto b) invitar a una fiesta c) vender una botella", "a) pedir que traigan materiales para un proyecto", "Dice Please bring a plastic bottle and a ruler."),
        (YAWN + " ¿Cuál es el propósito? a) informar sobre un tema de ciencia b) pedir permiso para salir", "a) informar sobre un tema de ciencia", "Presenta una pregunta científica y datos."),
        (WEB + " ¿Qué datos puedes esperar de esta página? a) día, hora y lugar de una actividad b) una receta", "a) día, hora y lugar de una actividad", "Es una página de actividades."),
    ],
    [
        (EMAIL + " ¿Qué deben traer? a) una botella de plástico y una regla b) una botella de vidrio y un cuaderno", "a) una botella de plástico y una regla", "Dice a plastic bottle and a ruler."),
        (CHAT + " ¿A qué hora es el partido? a) a las 4:30 b) a las 4:00", "a) a las 4:30", "Lía escribe 4:30 at the field."),
        (WEB + " ¿Cuánto cuesta participar? a) es gratis b) 3.000 pesos", "a) es gratis", "Dice Free for everyone."),
    ],
    [
        ("Pedro dice que el texto de Lía y Tomás es un artículo porque habla de un partido. ¿Qué pista de formato muestra su error? a) los nombres con mensajes por turnos b) la palabra match", "a) los nombres con mensajes por turnos", "Un chat se reconoce por los turnos."),
        (YAWN + " ¿Qué frase muestra que los científicos aún no saben todo? a) Scientists are still studying this question. b) It often happens when we are tired.", "a) Scientists are still studying this question.", "Still studying dice que la investigación continúa."),
    ],
    [
        ("Un texto tiene un título grande, una foto y tres párrafos que explican por qué bostezamos. ¿Qué tipo de texto es? a) un artículo de revista b) un chat", "a) un artículo de revista", "Un título, una foto y párrafos explicativos son propios de un artículo."),
        ("Necesitas saber rápido la hora y el lugar de una actividad. ¿Qué texto conviene leer? a) la página web de actividades b) el artículo sobre el bostezo", "a) la página web de actividades", "Es la que entrega horario y lugar."),
    ],
    [("En la pantalla de tu celular aparece: «Reminder: your library book is due on Friday. Please return it or renew it online.» (reminder = recordatorio, due = vence, return = devolver, renew = renovar). ¿Cuál es el propósito? a) recordar una fecha de devolución b) invitar a una fiesta", "a) recordar una fecha de devolución", "Dice que el libro vence el viernes y pide devolverlo o renovarlo.")],
    [
        ("En Inglés de 8.º (OA 9, clase 1): ¿Qué pistas tiene un correo?", "From, To, Subject, saludo y despedida", "Son partes propias del formato."),
        ("¿Qué muestra el menú Home | Events | Contact?", "Que es una página web", "Es un menú de navegación."),
        ("¿Para qué sirve reconocer el propósito antes de leer?", "Para saber qué buscar", "Orienta la lectura."),
    ],
    task("Lee estos dos textos de ejemplo. Texto 1: «From: Mr. Díaz. Subject: Change of room. Dear students, tomorrow the English class is in room 4. Kind regards, Mr. Díaz.» (change = cambio, room = sala, dear = estimados, kind regards = atentos saludos). Texto 2: «Home | Library | News. New books this month: 40 comics and 25 novels.» (comics = historietas, novels = novelas). Escribe el tipo y el propósito de cada texto, y una pista de formato.", "Texto 1: correo; avisa un cambio de sala; From, Subject y la despedida. Texto 2: página web; informa de libros nuevos; menú Home | Library | News.", ["nombra el tipo de cada texto", "dice el propósito", "cita una pista de formato"], ["hoja con tres datos por texto", "nota de una persona de tu casa"], ["decir que ambos son chats", "no citar una pista"], "Reconoce lo que acertó y vuelve a mirar el encabezado y el menú para decidir el tipo."),
    "Mira un correo o una página real en tu casa y di qué partes tiene: encabezado, saludo, menú o título.",
    "Escribe un mensaje de chat de cuatro líneas en inglés para coordinar un plan e indica su propósito.",
)

# ------------------------------------------------------------------ OA 9, clase 2
SCHED = "«Library Summer Workshops. Monday: Drawing, 10:00-11:30, Room 3. Wednesday: Robotics, 14:00-15:30, Room 5. Friday: Storytelling, 11:00-12:00, Room 3. All workshops are free. Maximum 20 children per workshop. Sign up at the front desk.» (workshops = talleres, drawing = dibujo, robotics = robótica, storytelling = cuentacuentos, room = sala, free = gratis, maximum = máximo, sign up = inscribirse, front desk = mesón de entrada)"

lesson(
    OA9, 2, MAT,
    "Aprenderé a ubicar información exacta en un texto impreso o digital (horarios, salas, precios, cupos) y a citar la frase que lo prueba. Sirve para responder con evidencia.",
    ["Sé reconocer el tipo de texto.", "Conozco las horas y los días en inglés."],
    [
        "La información explícita (explicit information) es la que el texto escribe con claridad. Para ubicarla, lee primero la pregunta y subraya la palabra que pide el dato: when (cuándo), where (dónde), how many (cuántos), how much (cuánto cuesta), which (cuál). Luego busca en el texto esa palabra o una parecida.",
        "En un horario o una lista, cada línea tiene el mismo orden de datos: día, actividad, hora y sala. Lee de izquierda a derecha y no mezcles líneas. Para las horas, calcula la duración restando la hora de inicio a la hora de término: de 10:00 a 11:30 son una hora y treinta minutos, es decir, 90 minutos. En los cupos, usa los números tal como están escritos.",
        "Para justificar una respuesta, cita la evidencia (evidence), es decir, la frase del texto que la prueba. Por ejemplo: la respuesta es «gratis» porque el texto dice All workshops are free. Citar la evidencia te permite comprobar que no adivinaste.",
    ],
    [("explicit", "explícito: escrito con claridad"), ("evidence", "evidencia: frase del texto que prueba la respuesta"), ("schedule", "horario"), ("sign up", "inscribirse"), ("maximum", "máximo"), ("duration", "duración")],
    [
        ("Ubicar una hora", SCHED + " ¿A qué hora empieza el taller de robótica y qué frase lo prueba?", ["Busco Robotics en el horario.", "Dice Wednesday: Robotics, 14:00-15:30.", "Empieza a las 14:00."], "A las 14:00; la frase es Wednesday: Robotics, 14:00-15:30"),
        ("Ubicar un cupo", SCHED + " ¿Cuántos niños como máximo hay por taller?", ["Busco Maximum.", "Dice Maximum 20 children per workshop.", "El máximo es 20."], "20 niños"),
    ],
    [
        ("Mezclar los datos de dos líneas del horario.", "Cada línea tiene sus propios datos.", "Lee una línea completa antes de pasar a la siguiente."),
        ("Responder sin citar de dónde viene el dato.", "No se puede comprobar si se adivinó.", "Escribe la frase del texto que lo prueba."),
    ],
    [
        (SCHED + " ¿Qué día es el taller de dibujo? a) el lunes b) el viernes", "a) el lunes", "Dice Monday: Drawing."),
        (SCHED + " ¿En qué sala es el taller de robótica? a) en la sala 5 b) en la sala 3", "a) en la sala 5", "Dice Robotics, 14:00-15:30, Room 5."),
        (SCHED + " ¿Cuánto cuestan los talleres? a) son gratis b) cuestan 2.000 pesos", "a) son gratis", "Dice All workshops are free."),
    ],
    [
        (SCHED + " ¿Cuántos talleres hay en el horario?", "3", "Hay dibujo, robótica y cuentacuentos."),
        (SCHED + " ¿Qué día es el cuentacuentos? a) el viernes b) el miércoles", "a) el viernes", "Dice Friday: Storytelling."),
        (SCHED + " ¿Dónde hay que inscribirse? a) en el mesón de entrada b) en la sala 3", "a) en el mesón de entrada", "Dice Sign up at the front desk."),
    ],
    [
        arith(SCHED + " ¿Cuántos minutos dura el taller de dibujo (de 10:00 a 11:30)?", "60+30", "Una hora son 60 minutos.", " minutos"),
        arith(SCHED + " Si los tres talleres tienen el cupo máximo, ¿cuántos niños participan en total?", "20*3", "Cada taller admite 20 niños.", " niños"),
        (SCHED + " ¿Qué taller dura exactamente una hora? a) cuentacuentos b) robótica", "a) cuentacuentos", "De 11:00 a 12:00 es una hora."),
    ],
    [
        (SCHED + " ¿Qué frase del texto prueba que no hay que pagar? a) All workshops are free. b) Sign up at the front desk.", "a) All workshops are free.", "Free significa gratis."),
        (SCHED + " Un lector dice que robótica es en la sala 3. ¿Qué dato lo corrige? a) Robotics, 14:00-15:30, Room 5 b) Drawing, 10:00-11:30, Room 3", "a) Robotics, 14:00-15:30, Room 5", "Robótica es en la sala 5."),
    ],
    [
        (SCHED + " ¿Qué dos talleres comparten la misma sala? a) dibujo y cuentacuentos b) robótica y dibujo", "a) dibujo y cuentacuentos", "Ambos son en la sala 3."),
        arith(SCHED + " El taller de robótica dura 90 minutos y el de cuentacuentos 60. ¿Cuántos minutos más dura robótica?", "90-60", "Se resta la menor duración a la mayor.", " minutos"),
    ],
    [("Quieres ir a un taller en la tarde, después del almuerzo. Según el horario, ¿cuál eliges? a) robótica, a las 14:00 b) dibujo, a las 10:00", "a) robótica, a las 14:00", "Es el único que empieza en la tarde.")],
    [
        ("¿Cómo calculas la duración entre 10:00 y 11:30?", "Restando la hora de inicio a la de término", "Son 90 minutos."),
        ("En Inglés de 8.º (OA 9, clase 2): ¿Qué es la evidencia?", "La frase del texto que prueba la respuesta", "Permite comprobar que no adivinaste."),
        ("¿Qué palabra pregunta por una cantidad contable?", "How many", "Por ejemplo, How many children?"),
    ],
    task("Lee esta ficha de ejemplo: «Science Fair, Friday 15 November. Opens at 9:00 and closes at 12:00. Place: school gym. Entry: 1,000 pesos for visitors, free for students. 18 projects. Prize: a telescope kit.» (science fair = feria científica, opens = abre, closes = cierra, entry = entrada, visitors = visitas, projects = proyectos, prize = premio). Escribe cuánto dura la feria, cuánto paga una visita, cuántos proyectos hay y la frase que prueba el precio para estudiantes.", "Dura 3 horas; una visita paga 1.000 pesos; hay 18 proyectos; la frase es free for students.", ["calcula la duración", "anota precio y proyectos", "cita la frase que prueba el precio para estudiantes"], ["hoja con cuatro respuestas", "nota de una persona de tu casa"], ["decir 12 horas de duración", "no citar una frase"], "Reconoce los datos bien ubicados y repasa el cálculo de la duración."),
    "Elige un horario real de tu casa o curso y subraya día, hora y lugar de una actividad.",
    "Escribe una ficha de tres líneas en inglés con día, hora y lugar, y pide a otra persona que escriba tres preguntas sobre ella.",
)

# ------------------------------------------------------------------ OA 9, clase 3
COMPOST = "«Our School Compost Project. Turning leftovers into soil. In September, Class 8A started a compost bin behind the gym. Students put fruit peels, dry leaves and eggshells in the bin. After three months, the bin produces dark soil. The soil is used in the school garden.» (compost = compostaje, leftovers = restos, soil = tierra, bin = contenedor, gym = gimnasio, peels = cáscaras, dry leaves = hojas secas, eggshells = cáscaras de huevo, produces = produce, dark = oscura)"

lesson(
    OA9, 3, MAT,
    "Aprenderé a usar estrategias de lectura: hojear (skim) para ver el tema, buscar datos (scan), usar el contexto y las palabras parecidas al español. Sirve para entender textos aunque tengan palabras desconocidas.",
    ["Sé identificar el tipo de texto y ubicar datos.", "Conozco palabras parecidas al español como project y information."],
    [
        "Hojear (to skim) es leer rápido el título, el subtítulo y la primera línea para saber de qué trata el texto. Buscar un dato (to scan) es mover los ojos por el texto buscando una palabra o un número concreto, sin leer todo. En el texto del compost, el título y el subtítulo dicen que se trata de convertir restos en tierra; para buscar cuántos meses, escaneas el número three months.",
        "Hay palabras que se parecen al español, llamadas cognados (cognates): project (proyecto), compost (compostaje), produce (producir), information (información). Te ayudan a entender sin diccionario. Pero hay que cuidar los falsos amigos: library es biblioteca, no librería.",
        "Si no conoces una palabra, usa el contexto (context clues): las palabras de alrededor. En Students put fruit peels, dry leaves and eggshells in the bin, peels aparece en una lista de restos de comida y plantas, así que probablemente significa cáscaras. No hace falta entender todas las palabras; lo importante es entender la idea y los datos que buscas.",
    ],
    [("skim", "hojear: leer rápido para ver el tema"), ("scan", "buscar un dato concreto"), ("context clue", "pista del contexto"), ("cognate", "palabra parecida al español"), ("title / subtitle", "título / subtítulo"), ("leftovers", "restos, sobras")],
    [
        ("Hojear con el título", COMPOST + " Mirando solo el título y el subtítulo, ¿de qué crees que trata?", ["El título dice Our School Compost Project.", "El subtítulo dice Turning leftovers into soil.", "Trata de convertir restos en tierra en el colegio."], "De convertir restos en tierra en el colegio"),
        ("Buscar un dato", COMPOST + " Escanea el texto: ¿cuántos meses pasan hasta que el contenedor produce tierra oscura?", ["Busco un número con months.", "Dice After three months.", "Son tres meses."], "Tres meses"),
    ],
    [
        ("Leer palabra por palabra y detenerse en cada palabra difícil.", "Se pierde el hilo y se tarda mucho.", "Hojea primero y escanea el dato que buscas."),
        ("Creer que library significa «librería».", "Library es biblioteca; librería es bookshop.", "Cuida los falsos amigos."),
    ],
    [
        (COMPOST + " ¿Cuántos meses tarda el contenedor en producir tierra oscura? a) 3 b) 6", "a) 3", "Dice After three months."),
        (COMPOST + " ¿Dónde está el contenedor? a) detrás del gimnasio b) en la biblioteca", "a) detrás del gimnasio", "Dice behind the gym."),
        (COMPOST + " ¿Qué palabra se parece a «producir»? a) produces b) soil", "a) produces", "Es un cognado."),
    ],
    [
        (COMPOST + " En la lista «fruit peels, dry leaves and eggshells», ¿qué significa probablemente «peels»? a) cáscaras de fruta b) jugos", "a) cáscaras de fruta", "Está en una lista de restos de fruta y plantas."),
        (COMPOST + " ¿Qué se hace con la tierra oscura? a) se usa en el huerto escolar b) se vende en una feria", "a) se usa en el huerto escolar", "Dice The soil is used in the school garden."),
        (COMPOST + " El subtítulo sugiere que el texto trata de... a) convertir restos en tierra b) comprar tierra en una tienda", "a) convertir restos en tierra", "Turning leftovers into soil significa convertir restos en tierra."),
    ],
    [
        (COMPOST + " ¿Qué curso comenzó el contenedor? a) 8A b) 8B", "a) 8A", "Dice Class 8A."),
        (COMPOST + " ¿En qué mes comenzó el proyecto? a) en septiembre b) en diciembre", "a) en septiembre", "Dice In September."),
        (COMPOST + " ¿Cuántos tipos de restos se nombran: cáscaras de fruta, hojas secas y cáscaras de huevo?", "3", "Son tres elementos distintos."),
    ],
    [
        (COMPOST + " Si el contenedor se empezó en septiembre y necesita tres meses, ¿en qué mes tiene tierra oscura? a) en diciembre b) en octubre", "a) en diciembre", "Septiembre más tres meses es diciembre."),
        (COMPOST + " ¿Qué significa probablemente «leftovers» según el subtítulo y el texto? a) restos de comida y plantas b) juguetes viejos", "a) restos de comida y plantas", "El texto menciona cáscaras, hojas y huevo."),
    ],
    [
        (COMPOST + " Pedro dice que la tierra se produce en una semana. ¿Qué parte del texto lo corrige? a) After three months b) behind the gym", "a) After three months", "Dice tres meses, no una semana."),
        ("Quieres saber cuánto cuesta un libro y el texto tiene diez párrafos. ¿Qué estrategia usas? a) escanear buscando un número con pesos b) leer cada palabra en orden", "a) escanear buscando un número con pesos", "Scan busca un dato concreto sin leer todo."),
    ],
    [("Ves un cartel en el patio: «Recycling Corner: paper, plastic, glass, batteries». (batteries = pilas). Quieres saber dónde dejar el plástico. ¿Qué estrategia usas? a) escanear buscando la palabra plastic b) leer cada palabra con un diccionario", "a) escanear buscando la palabra plastic", "Scan sirve para buscar una palabra concreta.")],
    [
        ("¿Qué es hojear un texto?", "Leer rápido el título y la primera línea para ver el tema", "Se hace antes de leer en detalle."),
        ("En Inglés de 8.º (OA 9, clase 3): ¿Qué es un cognado?", "Una palabra parecida al español", "Por ejemplo, project y proyecto."),
        ("¿Qué haces si no conoces una palabra?", "Usar las palabras de alrededor como pista", "El contexto ayuda a deducir el significado."),
    ],
    task("Lee este texto de ejemplo: «School Radio Club. Join our team! We record a news program every Thursday. You can be a reporter, an editor or a sound technician. Meetings are in room 6 at one o'clock.» (join = únete, record = grabamos, news = noticias, reporter = reportero, editor = editor, technician = técnico, meetings = reuniones). Primero hojea el título y escribe de qué trata. Luego escanea para encontrar el día, la sala y los tres cargos.", "Trata de un club de radio escolar. Día: jueves (para grabar); sala 6, a la una; cargos: reportero, editor y técnico de sonido.", ["dice el tema con el título", "ubica día, sala y hora", "nombra los tres cargos"], ["hoja con tema y datos", "nota de una persona de tu casa"], ["leer todo sin estrategia", "confundir el día de grabación con la sala"], "Reconoce los datos que ubicó y repasa cómo escanear un número o una palabra concreta."),
    "Elige un texto breve en inglés (un envase, un aviso) y hojea el título para decir de qué trata.",
    "Busca cinco cognados en un texto en inglés y escribe su significado en español.",
)

# ------------------------------------------------------------------ OA 9, clase 4
TXT_A = "Texto A (correo): «Subject: Chess Club Trip. Hi, the trip to the chess tournament is on 14 November. We leave at 7:30 from the main gate.» (chess = ajedrez, tournament = torneo, leave = salimos, main gate = portón principal)"
TXT_B = "Texto B (página web): «Chess Tournament, Regional Hall. Entry: 3,000 pesos. Bring your own board and a lunch box. The tournament ends at 5:00.» (entry = entrada, bring = traer, board = tablero, lunch box = vianda, ends = termina)"

lesson(
    OA9, 4, MAT,
    "Aprenderé a juntar la información de dos textos que se complementan y a formular una pregunta para el dato que falta. Sirve para organizar una actividad cuando cada texto entrega solo una parte.",
    ["Sé ubicar datos exactos en un texto.", "Conozco preguntas como What time...? y Where...?"],
    [
        "A veces la información completa está repartida entre dos textos, por ejemplo, un correo y una página web. Para unirla, lee cada texto y anota sus datos en una tabla con columnas como date (fecha), time (hora), place (lugar), price (precio) y bring (qué llevar). Escribe junto a cada dato de qué texto viene.",
        "Cuando termines, revisa qué casillas quedan vacías. Esa es la brecha de información (information gap). Para completarla, escribe una pregunta corta y específica: What time do we come back to school? o Is lunch included? Una buena pregunta pide solo lo que falta y se puede responder con una frase breve.",
        "Si dos textos dan datos distintos para lo mismo, como dos horas de salida, no elijas tú: pregunta a la persona que organiza o revisa la fecha del texto más reciente. Combinar textos es una forma de comprensión: reúnes datos, los comparas y decides qué hacer con ellos.",
    ],
    [("information gap", "brecha de información: dato que falta"), ("table", "tabla"), ("combine", "combinar"), ("Is lunch included?", "¿Está incluido el almuerzo?"), ("What time do we come back?", "¿A qué hora volvemos?"), ("source", "fuente: texto del que viene un dato")],
    [
        ("Juntar datos", TXT_A + " " + TXT_B + " ¿Cuál es la fecha, la hora de salida y el precio de la entrada?", ["La fecha y la hora de salida están en el texto A.", "El precio está en el texto B.", "Junto los tres datos."], "14 de noviembre; salida a las 7:30; entrada de 3.000 pesos"),
        ("Preguntar lo que falta", TXT_A + " " + TXT_B + " ¿Qué dato no dicen los textos sobre el regreso? Escribe una pregunta en inglés.", ["Ningún texto dice a qué hora vuelven al colegio.", "Una pregunta puede ser What time do we come back to school?", "La pregunta es corta y específica."], "No dicen la hora de regreso; What time do we come back to school?"),
    ],
    [
        ("Mezclar de qué texto viene cada dato.", "Se anotan datos sin saber su fuente y no se puede comprobar.", "Escribe A o B junto a cada dato."),
        ("Preguntar por algo que ya está en los textos.", "Se pierde tiempo y se parece no haber leído.", "Mira primero qué casillas quedan vacías."),
    ],
    [
        (TXT_A + " " + TXT_B + " ¿Qué día es el viaje? a) el 14 de noviembre b) el 5 de noviembre", "a) el 14 de noviembre", "El texto A dice 14 November."),
        (TXT_A + " " + TXT_B + " ¿Cuánto cuesta la entrada? a) 3.000 pesos b) 7.300 pesos", "a) 3.000 pesos", "El texto B dice Entry: 3,000 pesos."),
        (TXT_A + " " + TXT_B + " ¿A qué hora salen? a) a las 7:30 b) a las 5:00", "a) a las 7:30", "El texto A dice We leave at 7:30."),
    ],
    [
        (TXT_A + " " + TXT_B + " ¿Dónde es el torneo? a) en Regional Hall b) en el portón principal", "a) en Regional Hall", "El texto B nombra Regional Hall."),
        (TXT_A + " " + TXT_B + " ¿Qué deben llevar? a) su tablero y una vianda b) solo dinero", "a) su tablero y una vianda", "El texto B dice Bring your own board and a lunch box."),
        (TXT_A + " " + TXT_B + " ¿A qué hora termina el torneo? a) a las 5:00 b) a las 7:30", "a) a las 5:00", "El texto B dice The tournament ends at 5:00."),
    ],
    [
        (TXT_A + " " + TXT_B + " ¿Qué texto dice desde dónde salen? a) el texto A: desde el portón principal b) el texto B: desde Regional Hall", "a) el texto A: desde el portón principal", "Solo el texto A dice from the main gate."),
        ("Resume en una línea los datos de ambos textos: fecha, salida, precio y qué llevar, separados por punto y coma.", "14 de noviembre; salida 7:30; 3.000 pesos; tablero y vianda", "Reúne los datos de A y B."),
        arith(TXT_B + " Si van 4 estudiantes y cada uno paga la entrada, ¿cuántos pesos pagan en total?", "4*3000", "Cada entrada cuesta 3.000 pesos.", " pesos"),
    ],
    [
        ("Los textos no dicen cuándo vuelven. ¿Qué pregunta haces? a) What time do we come back to school? b) Where is the board?", "a) What time do we come back to school?", "Pregunta por el dato que falta."),
        ("Un tercer texto dice que salen a las 8:30. ¿Qué haces? a) preguntar a la persona que organiza cuál es la hora correcta b) elegir la hora que te conviene", "a) preguntar a la persona que organiza cuál es la hora correcta", "Hay datos que se contradicen."),
    ],
    [
        ("¿Cuántos datos del plan aparecen solo en el texto B: nombre del lugar, precio, qué llevar y hora de término?", "4", "El texto B entrega los cuatro."),
        (TXT_A + " ¿Qué tipo de texto es el texto A? a) un correo b) un artículo", "a) un correo", "Tiene Subject y un saludo."),
    ],
    [("Ves un afiche: «Bake Sale, Friday, 3:00, school yard». Tu profesora escribe en un correo: «Please bring 12 cookies each». (bake sale = venta de pasteles, cookies = galletas). ¿Qué debes llevar y a dónde? a) 12 galletas, al patio b) 3 galletas, al gimnasio", "a) 12 galletas, al patio", "El afiche dice school yard y el correo dice 12 cookies.")],
    [
        ("En Inglés de 8.º (OA 9, clase 4): ¿cómo se completa un dato que falta entre dos textos?", "Con una pregunta corta y específica", "Se completa con una pregunta."),
        ("En Inglés de 8.º (OA 9, clase 4): ¿Qué anotas junto a cada dato?", "De qué texto viene", "La fuente permite comprobarlo."),
        ("¿Cómo es una buena pregunta para un dato que falta?", "Corta y específica", "Pide solo lo que falta."),
    ],
    task("Lee estos dos textos de ejemplo. Texto A (correo): «Hi, the beach trip is on Saturday. We meet at the bus stop at 8:00.» Texto B (afiche): «Beach Day. Bring sun cream and a towel. The bus costs 2,500 pesos. We return at 6:00.» (beach = playa, sun cream = bloqueador, towel = toalla, return = volvemos). Escribe una tabla con día, lugar de encuentro, hora de encuentro, precio, qué llevar y hora de regreso, y una pregunta en inglés para el dato que no se dice (qué ropa usar).", "Sábado; paradero; 8:00; 2.500 pesos; bloqueador y toalla; 6:00. Pregunta: What should we wear?", ["completa seis datos", "indica la fuente de cada dato", "formula una pregunta en inglés"], ["tabla de seis datos", "pregunta escrita"], ["mezclar el precio con la hora", "preguntar algo que ya se dijo"], "Reconoce los datos que anotó bien y repasa dónde está cada dato en cada texto."),
    "Con dos avisos de tu curso, escribe una tabla con los datos que entrega cada uno.",
    "Escribe dos mensajes breves en inglés que se complementen, y una pregunta que complete la información.",
)

# ------------------------------------------------------------------ OA 9, clase 5
BLOG = "«My first month as a cyclist. By Valentina. Last month I started to cycle to school. At first it was hard because the road has many hills. Now it takes me only 20 minutes. I also save 1,200 pesos a week because I do not take the bus. My advice: wear a helmet and check your brakes every week.» Comentarios: «Nico: Great post! I want to start too. Which bike do you use? Valentina: A second-hand blue bike. I bought it for 45,000 pesos.» (cyclist = ciclista, cycle = andar en bicicleta, hills = cerros, takes me = me demora, save = ahorro, advice = consejo, helmet = casco, brakes = frenos, second-hand = usada)"

lesson(
    OA9, 5, MAT,
    "Aprenderé a leer por mi cuenta un texto digital (una entrada de blog con comentarios) y a mostrar la idea general, datos exactos y una conclusión con evidencia. Sirve para demostrar que puedo comprender un texto nuevo.",
    ["Sé hojear y escanear.", "Conozco conectores como because y so."],
    [
        "Un blog es una página digital en que una persona publica textos con su nombre y sus experiencias. Después del texto suele haber comentarios (comments), mensajes de otros lectores con preguntas y respuestas. Para leerlo bien, identifica quién escribe, de qué trata y para qué: contar una experiencia, informar o dar consejos.",
        "Lee en tres pasos. Primero, hojea el título y las primeras líneas para ver el tema. Segundo, lee completo y subraya datos exactos: números, tiempo, precio y consejos. Tercero, revisa los comentarios: ¿qué pregunta hace alguien y qué responde la autora? Un comentario puede agregar un dato nuevo, como el precio de la bicicleta.",
        "Para concluir, usa solo lo que dice el texto. Si ahorra dinero porque no toma el bus, esa es la razón explícita. Si el texto dice It was hard at first, puedes concluir que ahora es más fácil porque ahora le toma solo 20 minutos, pero lo cuentas con tus palabras y apoyas tu respuesta con una frase del texto.",
    ],
    [("blog post", "entrada de blog: texto publicado en línea"), ("comment", "comentario de un lector"), ("advice", "consejo"), ("second-hand", "usado"), ("save", "ahorrar"), ("conclusion", "conclusión: idea que sacas del texto")],
    [
        ("Idea general", BLOG + " ¿Cuál es la idea general de la entrada?", ["Valentina cuenta su primer mes yendo en bicicleta al colegio.", "Explica lo difícil al comienzo y lo que ganó.", "Termina con consejos."], "Cuenta cómo le fue en su primer mes yendo en bicicleta y da consejos"),
        ("Dato de los comentarios", BLOG + " ¿Qué bicicleta usa y cuánto pagó por ella?", ["Nico pregunta por la bicicleta.", "Valentina responde en un comentario.", "Es una bicicleta azul usada que costó 45.000 pesos."], "Una bicicleta azul usada, 45.000 pesos"),
    ],
    [
        ("Leer solo la entrada y olvidar los comentarios.", "Los comentarios pueden dar datos nuevos.", "Revisa también las preguntas y las respuestas."),
        ("Sacar una conclusión que el texto no apoya.", "Se pierde la evidencia.", "Cita la frase del texto que apoya tu conclusión."),
    ],
    [
        (BLOG + " ¿Quién escribe la entrada? a) Valentina b) Nico", "a) Valentina", "Dice By Valentina."),
        (BLOG + " ¿Cuánto demora ahora en llegar al colegio? a) 20 minutos b) 45 minutos", "a) 20 minutos", "Dice Now it takes me only 20 minutes."),
        (BLOG + " ¿De qué trata la entrada? a) de su primer mes andando en bicicleta al colegio b) de un viaje a la playa", "a) de su primer mes andando en bicicleta al colegio", "El título y el primer párrafo lo dicen."),
    ],
    [
        (BLOG + " ¿Por qué fue difícil al comienzo? a) porque el camino tiene muchos cerros b) porque no tenía casco", "a) porque el camino tiene muchos cerros", "Dice because the road has many hills."),
        (BLOG + " ¿Cuántos pesos ahorra por semana? a) 1.200 b) 45.000", "a) 1.200", "Dice I also save 1,200 pesos a week."),
        (BLOG + " ¿Qué consejos da? a) usar casco y revisar los frenos cada semana b) comprar una bicicleta nueva", "a) usar casco y revisar los frenos cada semana", "Dice wear a helmet and check your brakes every week."),
    ],
    [
        arith(BLOG + " Si ahorra 1.200 pesos por semana, ¿cuántos pesos ahorra en 4 semanas?", "1200*4", "Se multiplica el ahorro semanal por 4.", " pesos"),
        (BLOG + " Nico pregunta qué bicicleta usa. ¿Dónde está la respuesta? a) en el comentario de Valentina b) en el consejo final", "a) en el comentario de Valentina", "Valentina responde A second-hand blue bike."),
        (BLOG + " ¿Qué quiere hacer Nico? a) empezar a andar en bicicleta b) comprar un bus", "a) empezar a andar en bicicleta", "Dice I want to start too."),
    ],
    [
        (BLOG + " ¿Por qué ahorra dinero Valentina? a) porque no toma el bus b) porque la bicicleta es gratis", "a) porque no toma el bus", "Dice because I do not take the bus."),
        (BLOG + " ¿Cuál frase es un hecho? a) I bought it for 45,000 pesos. b) Great post!", "a) I bought it for 45,000 pesos.", "El precio se puede comprobar; Great post! es una opinión de Nico."),
    ],
    [
        (BLOG + " ¿Qué conclusión se apoya en el texto? a) Andar en bicicleta le resultó más fácil con el tiempo, porque ahora demora solo 20 minutos. b) Andar en bicicleta cuesta más que tomar el bus.", "a) Andar en bicicleta le resultó más fácil con el tiempo, porque ahora demora solo 20 minutos.", "El texto dice que fue difícil al comienzo y que ahora tarda poco."),
        (BLOG + " Un lector dice que Valentina pagó 120.000 pesos por la bicicleta. ¿Qué frase lo corrige? a) I bought it for 45,000 pesos b) I also save 1,200 pesos a week", "a) I bought it for 45,000 pesos", "El precio es 45.000 pesos."),
    ],
    [arith("En un blog escolar lees: «Our school garden has 15 tomato plants. Last week, we picked 30 tomatoes. Please water the plants on Fridays.» (plants = plantas, picked = recogimos, water = regar). Si cada planta dio el mismo número de tomates, ¿cuántos tomates dio cada planta?", "30//15", "Se reparten los tomates entre las plantas.", " tomates")],
    [
        ("¿Dónde puede estar un dato nuevo en un blog?", "En los comentarios", "Los lectores y la autora agregan información."),
        ("En Inglés de 8.º (OA 9, clase 5): ¿Cómo apoyas una conclusión?", "Con una frase del texto", "La evidencia respalda lo que dices."),
        ("¿Qué pasos sigues al leer un texto nuevo?", "Hojear, leer subrayando datos y revisar los comentarios", "Son tres pasos de lectura."),
    ],
    task("Lee esta entrada de blog de ejemplo: «My book club. By Camilo. We meet every Tuesday at 4:30 in the school library. This month we read an adventure story with 12 chapters. We finish three chapters each week. Join us! Comment: Sofía: How many people are in the club? Camilo: Nine.» (book club = club de lectura, chapters = capítulos, finish = terminamos, join = únete). Escribe la idea general, cuántas semanas se necesitan para terminar el libro y cuántas personas hay en el club.", "Idea general: Camilo presenta su club de lectura y lo que leen. El libro se termina en 4 semanas (12 ÷ 3). Hay 9 personas.", ["dice la idea general", "calcula las semanas con los datos", "usa el comentario para el número de personas"], ["hoja con tres respuestas", "nota de una persona de tu casa"], ["decir 12 semanas", "no mirar el comentario"], "Reconoce el cálculo correcto y revisa el comentario para el dato de las personas."),
    "Lee en voz alta el blog de Valentina y escribe en tu cuaderno tres datos con números.",
    "Escribe un comentario en inglés de dos líneas para el blog de Valentina con una pregunta nueva.",
)

# ================================================================== OA 10, clase 1
AD = "«NEW Fresh Bakery! Try our warm bread every morning from 7:00. Buy two loaves and get one free this week. Visit us at 45 Elm Street!» (bakery = panadería, warm = tibio, loaves = panes, free = gratis, visit = visítanos)"
BIO = "«Rosa Lagos (persona de ejemplo) was born in a small coastal village. As a child, she repaired radios for her neighbours. Later, she studied engineering and built a solar charger for rural schools. Because of her work, ten schools now have light in the evening. Today, she teaches students to build their own devices.» (coastal = costera, repaired = reparaba, neighbours = vecinos, engineering = ingeniería, solar charger = cargador solar, rural = rural, devices = aparatos)"
DESCR = "«The Old Market is a covered building with a red roof and twelve stalls. It smells of bread and flowers. On Saturdays, it is full of people.» (market = mercado, covered = cubierto, roof = techo, stalls = puestos, smells of = huele a, full of = lleno de)"

lesson(
    OA10, 1, MAT,
    "Aprenderé a reconocer el propósito y las ideas generales de textos no literarios funcionales: avisos publicitarios, biografías y descripciones. Sirve para entender para qué se escribió un texto y qué dice.",
    ["Sé reconocer correos, páginas web y artículos.", "Conozco palabras como free, born y studied."],
    [
        "Los textos no literarios funcionales sirven para algo concreto: informar, instruir, convencer o describir. Un aviso publicitario (advertisement) busca convencer de comprar o visitar algo. Una biografía (biography) cuenta la vida de una persona en orden. Una descripción (description) dice cómo es un lugar o una cosa. También hay artículos, instrucciones, correos, diálogos, páginas web y gráficos.",
        "El propósito (purpose) responde a ¿para qué se escribió? En el aviso de la panadería, el propósito es convencer de visitarla: usa palabras llamativas como NEW, warm y free. En la biografía de Rosa, es informar sobre su vida y su trabajo. En la descripción del mercado, es mostrar cómo es: red roof, twelve stalls, full of people.",
        "Las ideas generales son lo más importante: en el aviso, una oferta de dos panes más uno gratis; en la biografía, una mujer que reparó radios, estudió ingeniería y hoy enseña. Los detalles son datos como 7:00, 45 Elm Street o ten schools. Para entender un texto, primero identifica el propósito y la idea general, y luego busca los detalles.",
    ],
    [("advertisement", "aviso publicitario"), ("biography", "biografía: vida de una persona"), ("description", "descripción: cómo es algo"), ("purpose", "propósito"), ("main idea", "idea general"), ("detail", "detalle")],
    [
        ("Propósito de un aviso", AD + " ¿Cuál es el propósito de este aviso?", ["Usa palabras llamativas: NEW, warm, free.", "Da una oferta y una dirección.", "Quiere convencer de visitar la panadería."], "Convencer de visitar la panadería"),
        ("Idea general de una biografía", BIO + " ¿Cuál es la idea general?", ["Cuenta la vida de Rosa en orden.", "Pasó de reparar radios a estudiar ingeniería y enseñar.", "Su trabajo ayuda a escuelas rurales."], "Rosa pasó de reparar radios a crear un cargador solar para escuelas rurales y hoy enseña"),
    ],
    [
        ("Pensar que un aviso publicitario solo informa.", "Su propósito principal es convencer.", "Fíjate en palabras llamativas y ofertas."),
        ("Confundir un detalle con la idea general.", "Un número o una dirección son detalles.", "Pregunta qué quiere decir el texto en conjunto."),
    ],
    [
        (AD + " ¿Qué tipo de texto es? a) un aviso publicitario b) una biografía", "a) un aviso publicitario", "Ofrece un producto y una oferta."),
        (BIO + " ¿Qué tipo de texto es? a) una biografía b) un aviso publicitario", "a) una biografía", "Cuenta la vida de una persona en orden."),
        (DESCR + " ¿Qué tipo de texto es? a) una descripción b) una receta", "a) una descripción", "Dice cómo es un lugar."),
    ],
    [
        (AD + " ¿Cuál es la oferta de esta semana? a) comprar dos panes y llevar uno gratis b) pagar solo la mitad", "a) comprar dos panes y llevar uno gratis", "Dice Buy two loaves and get one free."),
        (BIO + " ¿Qué construyó Rosa? a) un cargador solar para escuelas rurales b) una radio gigante", "a) un cargador solar para escuelas rurales", "Dice built a solar charger for rural schools."),
        (DESCR + " ¿Qué idea general tiene la descripción? a) el mercado es un edificio con techo rojo, puestos y mucha gente los sábados b) el mercado cierra los domingos", "a) el mercado es un edificio con techo rojo, puestos y mucha gente los sábados", "Resume cómo es el lugar."),
    ],
    [
        (AD + " ¿Qué palabra del aviso llama la atención de una novedad? a) NEW b) bread", "a) NEW", "NEW (nuevo) sirve para atraer a los lectores."),
        (BIO + " ¿Qué hizo Rosa de niña? a) reparaba radios de sus vecinos b) enseñaba ingeniería", "a) reparaba radios de sus vecinos", "Dice As a child, she repaired radios for her neighbours."),
        (DESCR + " ¿Cuántos puestos tiene el mercado?", "12", "Dice twelve stalls."),
    ],
    [
        (BIO + " Pablo dice que el propósito de la biografía es vender cargadores solares. ¿Qué respondes? a) que no: su propósito es informar sobre la vida y el trabajo de Rosa b) que sí, porque lo nombra", "a) que no: su propósito es informar sobre la vida y el trabajo de Rosa", "El texto cuenta la vida de Rosa, no ofrece un producto."),
        (AD + " Ema dice que la idea general es la dirección. ¿Qué error comete? a) confunde un detalle con la idea general b) lee mal el precio", "a) confunde un detalle con la idea general", "La dirección es un dato; la idea general es la oferta."),
    ],
    [
        (BIO + " ¿Cuántas escuelas tienen luz en la noche gracias al trabajo de Rosa? a) 10 b) 100", "a) 10", "Dice ten schools."),
        (AD + " ¿Qué tipo de palabras usa el aviso para convencer? a) palabras llamativas como NEW, warm y free b) datos científicos", "a) palabras llamativas como NEW, warm y free", "Son propias de un aviso."),
    ],
    [("Ves un afiche: «Join the school choir! Everyone is welcome. Practices on Wednesdays at 4:00. Come and sing with us!» (choir = coro, welcome = bienvenidos, practices = ensayos, sing = cantar). ¿Cuál es el propósito? a) invitar a unirse al coro b) contar la vida de un músico", "a) invitar a unirse al coro", "Usa Join, Come y datos de ensayos.")],
    [
        ("En Inglés de 8.º (OA 10, clase 1): ¿qué propósito principal tiene un aviso publicitario?", "Convencer", "Usa palabras llamativas."),
        ("En Inglés de 8.º (OA 10, clase 1): ¿Qué cuenta una biografía?", "La vida de una persona", "En orden y con datos."),
        ("¿Qué es una descripción?", "Un texto que dice cómo es algo", "Muestra rasgos del lugar o cosa."),
    ],
    task("Lee estos dos textos de ejemplo. Texto 1: «Fresh Juice Bar! Try our new orange and carrot juice. Only 2,000 pesos today. Don't miss it!» (juice = jugo, carrot = zanahoria, don't miss it = no te lo pierdas). Texto 2: «Leo Paz (persona de ejemplo) was born in a mountain town. He learned to paint with his grandfather. Today he paints murals for schools.» (mural = mural). Escribe el tipo de texto, el propósito y la idea general de cada uno.", "Texto 1: aviso publicitario; convencer de probar un jugo; hay un jugo nuevo a 2.000 pesos. Texto 2: biografía; informar sobre la vida de Leo; aprendió a pintar con su abuelo y hoy pinta murales.", ["nombra el tipo de texto", "dice el propósito", "resume la idea general"], ["hoja con tres respuestas por texto", "nota de una persona de tu casa"], ["decir que el aviso solo informa", "confundir el precio con la idea general"], "Reconoce el propósito de cada texto y repasa la diferencia entre idea general y detalle."),
    "Busca un aviso de una caja o revista en tu casa y di para qué sirve.",
    "Escribe un aviso breve en inglés de cuatro líneas para invitar a tu curso a una actividad.",
)

# ------------------------------------------------------------------ OA 10, clase 2
PLANT = "«How to take care of a plant. First, put it near a window. Then water it when the soil is dry. If the leaves turn yellow, give it less water. Because plants need light, do not keep them in a dark room. Finally, turn the pot a little every week so all sides get light.» (take care of = cuidar, pot = maceta, soil = tierra, dry = seca, leaves = hojas, yellow = amarillas, less = menos, dark = oscura, turn = girar, sides = lados)"
SEA = "«Why is the sea salty? Rivers carry small amounts of salt from rocks to the sea. When the sun heats the sea, water evaporates but the salt stays. Over a very long time, the sea becomes salty.» (salty = salado, rivers = ríos, carry = llevan, rocks = rocas, heats = calienta, evaporates = se evapora, stays = queda)"

lesson(
    OA10, 2, MAT,
    "Aprenderé a identificar la secuencia, la causa y el efecto, y la condición en instrucciones y explicaciones leídas. Sirve para seguir pasos y entender por qué ocurren las cosas.",
    ["Sé reconocer first, then y finally.", "Conozco because, so e if."],
    [
        "En unas instrucciones, los pasos tienen secuencia (sequence): first, then, next, finally. En How to take care of a plant, el primer paso es poner la planta cerca de una ventana y el último es girar la maceta cada semana. Respetar el orden es importante: si cambias un paso, el resultado puede ser distinto.",
        "La causa y el efecto explican por qué ocurre algo. Because introduce la causa: Because plants need light, do not keep them in a dark room (la causa es que las plantas necesitan luz; el efecto es que no hay que dejarlas en un cuarto oscuro). En el texto del mar, la causa es que los ríos llevan sal y el agua se evapora; el efecto es que el mar se vuelve salado.",
        "La condición (condition) dice qué hacer si algo ocurre: If the leaves turn yellow, give it less water. Si las hojas no están amarillas, no hace falta dar menos agua. Para leer un texto con pasos, causas y condiciones, subraya con tres colores: un color para las palabras de secuencia, otro para because y so, y otro para if.",
    ],
    [("sequence", "secuencia: orden de los pasos"), ("cause", "causa: lo que provoca algo"), ("effect", "efecto: lo que resulta"), ("condition", "condición: lo que debe ocurrir"), ("if", "si"), ("less", "menos")],
    [
        ("Condición y consecuencia", PLANT + " ¿Qué haces si las hojas de la planta se vuelven amarillas?", ["Busco la palabra If.", "Dice If the leaves turn yellow, give it less water.", "La acción es dar menos agua."], "Darle menos agua"),
        ("Causa y efecto", SEA + " ¿Cuál es la causa de que el mar sea salado?", ["La causa está en cómo llega la sal.", "Los ríos llevan sal desde las rocas.", "El agua se evapora pero la sal queda."], "Los ríos llevan sal desde las rocas y, al evaporarse el agua, la sal queda"),
    ],
    [
        ("Cambiar el orden de los pasos.", "Cada paso depende del anterior.", "Subraya first, then, next y finally."),
        ("Aplicar una condición cuando no se cumple.", "Si las hojas no están amarillas, no hay que darle menos agua.", "Lee primero la parte con if."),
    ],
    [
        (PLANT + " ¿Qué se hace primero? a) poner la planta cerca de una ventana b) girar la maceta", "a) poner la planta cerca de una ventana", "Dice First, put it near a window."),
        (PLANT + " ¿Cuándo se riega la planta? a) cuando la tierra está seca b) todos los días a la misma hora", "a) cuando la tierra está seca", "Dice water it when the soil is dry."),
        (SEA + " ¿Qué se evapora cuando el sol calienta el mar? a) el agua b) la sal", "a) el agua", "Dice water evaporates but the salt stays."),
    ],
    [
        (PLANT + " ¿Por qué no hay que dejar las plantas en un cuarto oscuro? a) porque necesitan luz b) porque se enfrían", "a) porque necesitan luz", "Dice Because plants need light."),
        (PLANT + " ¿Qué se hace al final? a) girar un poco la maceta cada semana b) poner la planta en la ventana", "a) girar un poco la maceta cada semana", "Dice Finally, turn the pot a little every week."),
        (SEA + " ¿Qué ocurre después de mucho tiempo? a) el mar se vuelve salado b) el mar se seca", "a) el mar se vuelve salado", "Dice Over a very long time, the sea becomes salty."),
    ],
    [
        (PLANT + " Las hojas están verdes. ¿Debes darle menos agua? a) no, porque la condición se cumple solo si las hojas se vuelven amarillas b) sí, siempre", "a) no, porque la condición se cumple solo si las hojas se vuelven amarillas", "La instrucción depende de la condición."),
        (PLANT + " ¿Para qué sirve girar la maceta cada semana? a) para que todos los lados reciban luz b) para regar más", "a) para que todos los lados reciban luz", "Dice so all sides get light."),
        (SEA + " ¿Qué se queda en el mar cuando el agua se evapora? a) la sal b) las rocas", "a) la sal", "Dice the salt stays."),
    ],
    [
        (PLANT + " Pedro puso la planta en un cuarto oscuro. ¿Qué paso del texto no cumplió y por qué importa? a) el que pide no dejarla en la oscuridad, porque necesita luz b) el de regar cuando la tierra está seca", "a) el que pide no dejarla en la oscuridad, porque necesita luz", "Because plants need light."),
        (SEA + " Ana dice que el mar es salado porque la gente le echa sal. ¿Qué dice el texto? a) que la sal viene de las rocas, llevada por los ríos b) que la sal la ponen los barcos", "a) que la sal viene de las rocas, llevada por los ríos", "Rivers carry small amounts of salt from rocks."),
    ],
    [
        (PLANT + " Ordena con números: (1) girar la maceta, (2) regar cuando la tierra esté seca, (3) poner la planta cerca de una ventana.", "3, 2, 1", "Siguen el orden del texto: first, then y finally."),
        (SEA + " ¿Qué palabra introduce el momento en que ocurre la evaporación? a) When b) Over", "a) When", "When introduce el momento en que ocurre el proceso."),
    ],
    [("Tu profesora entrega una ficha: «How to keep a classroom plant healthy. First, put it near a window. If the soil is dry, add water. If the leaves turn brown, tell the teacher.» (healthy = sana, brown = café). Tu planta tiene la tierra húmeda y hojas verdes. ¿Qué debes hacer? a) no regarla y seguir mirando b) regarla igual", "a) no regarla y seguir mirando", "Ninguna de las dos condiciones se cumple.")],
    [
        ("En Inglés de 8.º (OA 10, clase 2): ¿qué palabra introduce el último paso de unas instrucciones?", "Finally", "Finally significa finalmente."),
        ("En Inglés de 8.º (OA 10, clase 2): ¿Qué palabra introduce una condición?", "If", "If significa si."),
        ("¿Qué palabra introduce una causa?", "Because", "Because significa porque."),
    ],
    task("Lee este texto de ejemplo: «How to make a paper airplane. First, take a sheet of paper. Next, fold it in half and open it. Then fold the top corners to the middle line. Finally, fold the sides again. If the airplane falls too fast, bend the back edge up a little.» (airplane = avioncito, sheet = hoja, corners = esquinas, line = línea, falls = cae, bend = doblar, edge = borde). Escribe los pasos en orden y qué haces si el avión cae muy rápido.", "1) Tomar una hoja. 2) Doblarla por la mitad y abrirla. 3) Doblar las esquinas de arriba hacia la línea del medio. 4) Doblar los lados otra vez. Si cae muy rápido, doblar un poco hacia arriba el borde de atrás.", ["anota cuatro pasos en orden", "dice la condición con su consecuencia", "no inventa pasos"], ["hoja con pasos numerados", "nota de una persona de tu casa"], ["cambiar el orden de los pasos", "ignorar la condición"], "Reconoce los pasos que ordenó bien y revisa la parte con if."),
    "Lee en voz alta las instrucciones de la planta y marca con color las palabras first, then y finally.",
    "Escribe en inglés unas instrucciones de cuatro pasos para algo que sepas hacer y una condición con if.",
)

# ------------------------------------------------------------------ OA 10, clase 3
PUB = "«The Super Notebook! It has 100 pages and a hard cover. It is the best notebook in the world and it costs 1,800 pesos. Buy it today or you will lose the chance of your life!» (pages = hojas, hard cover = tapa dura, costs = cuesta, only = solo, lose = perder, chance = oportunidad)"
REV = "«I bought the notebook last week. The pages are thin, and the pen goes through them. In my opinion, it is too expensive for that quality. But the cover is strong, and the size is perfect for my bag.» (thin = delgadas, goes through = traspasa, quality = calidad, strong = resistente, size = tamaño, perfect = perfecto)"

lesson(
    OA10, 3, MAT,
    "Aprenderé a distinguir hechos de opiniones en avisos publicitarios y reseñas leídas. Sirve para no creer todo lo que dice un anuncio y para comparar opiniones.",
    ["Sé distinguir hechos y opiniones al escuchar.", "Conozco adjetivos como best, strong y expensive."],
    [
        "Un hecho (fact) se puede comprobar: It has 100 pages; It costs 1,800 pesos; The cover is hard. Una opinión (opinion) es un juicio de quien escribe: It is the best notebook in the world; It is too expensive; The size is perfect. En los avisos publicitarios, muchas frases son opiniones que buscan convencer, aunque suenen muy seguras.",
        "Hay pistas de opinión: palabras como best, perfect, amazing, too y frases como in my opinion o I think. También las frases con fuerza, como Buy it today or you will lose the chance of your life, quieren apurar al lector. Las pistas de hecho son números, medidas, materiales y datos comprobables.",
        "Una reseña (review) es un texto en que una persona da su opinión sobre algo que compró. Puede incluir hechos (the pages are thin) y opiniones (it is too expensive). Para leer con sentido crítico, separa los hechos de las opiniones y compara: el aviso quiere vender; la reseña cuenta una experiencia personal. Ambos pueden ser útiles si distingues cada parte.",
    ],
    [("fact", "hecho: se puede comprobar"), ("opinion", "opinión: lo que alguien piensa"), ("review", "reseña: opinión sobre algo comprado"), ("the best", "el mejor"), ("too expensive", "demasiado caro"), ("perfect", "perfecto")],
    [
        ("Separar hechos del aviso", PUB + " Escribe dos hechos que se pueden comprobar.", ["Busco números y características.", "It has 100 pages y It costs 1,800 pesos son datos comprobables.", "Tiene una tapa dura."], "Tiene 100 hojas y cuesta 1.800 pesos (también: tiene tapa dura)"),
        ("Reconocer una opinión en el aviso", PUB + " ¿«It is the best notebook in the world» es hecho u opinión?", ["No se puede medir cuál es el mejor del mundo.", "Es un juicio de quien vende.", "Es una opinión."], "Es una opinión"),
    ],
    [
        ("Creer que todo lo que dice un aviso es un hecho.", "Muchas frases son opiniones para vender.", "Separa las frases con números de las que usan best o perfect."),
        ("Creer que toda reseña es solo una opinión.", "Una reseña puede incluir hechos, como las hojas delgadas.", "Busca datos comprobables dentro de la reseña."),
    ],
    [
        (PUB + " ¿«It has 100 pages» es hecho u opinión? a) un hecho b) una opinión", "a) un hecho", "Las hojas se pueden contar."),
        (PUB + " ¿«It costs 1,800 pesos» es hecho u opinión? a) un hecho b) una opinión", "a) un hecho", "El precio se puede comprobar."),
        (REV + " ¿«In my opinion, it is too expensive» es hecho u opinión? a) una opinión b) un hecho", "a) una opinión", "Too expensive y in my opinion son un juicio."),
    ],
    [
        (REV + " ¿Qué frase es un hecho? a) The pages are thin. b) The size is perfect.", "a) The pages are thin.", "Se puede comprobar mirando las hojas."),
        (PUB + " ¿Qué frase es una opinión? a) It is the best notebook in the world. b) It has a hard cover.", "a) It is the best notebook in the world.", "Best es un juicio."),
        (REV + " ¿Qué palabra avisa que viene una opinión? a) opinion b) bought", "a) opinion", "In my opinion introduce lo que piensa quien escribe."),
    ],
    [
        (PUB + " Clasifica como hecho (H) u opinión (O): 1) It has 100 pages. 2) It is the best notebook in the world. 3) It costs 1,800 pesos. Escribe H u O.", "1 H, 2 O, 3 H", "Las frases 1 y 3 se pueden comprobar; la 2 es un juicio."),
        (REV + " ¿Qué hecho de la reseña contradice «The pages are great»? a) The pen goes through them. b) The cover is strong.", "a) The pen goes through them.", "Muestra un problema de las hojas."),
        (PUB + " ¿Qué frase busca apurar al lector? a) Buy it today or you will lose the chance of your life! b) It has 100 pages.", "a) Buy it today or you will lose the chance of your life!", "Usa presión para convencer."),
    ],
    [
        (PUB + " Marta dice que el aviso prueba que es el mejor cuaderno del mundo. ¿Qué le respondes? a) que es una opinión de quien vende y no se puede comprobar b) que tiene razón porque lo dice el aviso", "a) que es una opinión de quien vende y no se puede comprobar", "Best es un juicio."),
        (REV + " La reseña dice «too expensive» y el aviso dice «the best notebook in the world». ¿Qué tipo de frases son? a) opiniones, que no se pueden comprobar b) hechos, que se pueden comprobar", "a) opiniones, que no se pueden comprobar", "Too expensive y best son juicios de quien escribe."),
    ],
    [
        ("Un aviso dice: «The Mega Backpack has 3 pockets and it is the most amazing backpack ever». (pockets = bolsillos, amazing = increíble). ¿Qué parte es un hecho? a) it has 3 pockets b) it is the most amazing backpack ever", "a) it has 3 pockets", "El número de bolsillos se puede comprobar."),
        ("Una reseña dice: «The backpack broke after two weeks. I think the zip is too weak.» (broke = se rompió, zip = cierre, weak = débil). ¿Cuál es el hecho? a) The backpack broke after two weeks. b) I think the zip is too weak.", "a) The backpack broke after two weeks.", "El tiempo y la rotura se pueden comprobar; la otra frase es opinión."),
    ],
    [("Quieres comprar un cuaderno y lees el aviso y la reseña. ¿Qué haces para decidir con mejor criterio? a) separar los hechos de las opiniones y comparar ambos textos b) creer solo la frase más llamativa del aviso", "a) separar los hechos de las opiniones y comparar ambos textos", "Los hechos te ayudan a decidir y las opiniones te muestran puntos de vista.")],
    [
        ("En Inglés de 8.º (OA 10, clase 3): ¿cómo reconoces un hecho en un aviso?", "Porque se puede comprobar, como un número o una medida", "Por ejemplo, un número o una medida."),
        ("En Inglés de 8.º (OA 10, clase 3): ¿Qué pistas avisan que viene una opinión?", "Palabras como best, perfect, too e in my opinion", "Expresan un juicio."),
        ("En Inglés de 8.º (OA 10, clase 3): ¿qué intenta lograr quien escribe un aviso con opiniones?", "Convencer de comprar", "Usa opiniones y presión."),
    ],
    task("Lee este aviso de ejemplo: «The Magic Bottle! It holds 750 ml and keeps drinks cold for 12 hours. It is the coolest bottle you will ever see. Get yours now!» (bottle = botella, holds = guarda, keeps = mantiene, cold = frío, coolest = la más genial). Escribe dos hechos, dos opiniones y qué frase te apura a comprar.", "Hechos: guarda 750 ml; mantiene el frío 12 horas. Opiniones: it is the coolest bottle you will ever see; (Get yours now! presiona). Frase de apuro: Get yours now!", ["anota dos hechos", "anota al menos una opinión", "identifica la frase que apura"], ["hoja con tres respuestas", "nota de una persona de tu casa"], ["poner coolest como hecho", "no ubicar la frase que presiona"], "Reconoce los hechos con números y repasa las palabras como coolest."),
    "Busca un aviso real y marca con color los hechos y las opiniones.",
    "Escribe una reseña de cuatro líneas en inglés de un objeto de tu casa, con dos hechos y dos opiniones.",
)

# ------------------------------------------------------------------ OA 10, clase 4
INFO = "«The school library has a new collection of comics. First, students fill in a form. Then the librarian checks the information. You can borrow a comic until Friday, so read it quickly. The library also has a game room. Maybe it will open longer next month.» (collection = colección, comics = historietas, fill in = completar, form = formulario, librarian = bibliotecaria, borrow = pedir prestado, until = hasta, game room = sala de juegos, longer = más tiempo)"

lesson(
    OA10, 4, MAT,
    "Aprenderé a reconocer palabras derivadas con los sufijos -er (en comparaciones) y -ion, y a entender los conectores so, then, until, also y maybe en textos leídos. Sirve para deducir significados y seguir el hilo de un texto.",
    ["Sé que -er se usa para comparar.", "Conozco conectores como because y first."],
    [
        "El sufijo -ion forma sustantivos a partir de verbos y se parece al -ción del español. Algunos solo agregan -ion: act, action; collect, collection; connect, connection; discuss, discussion; protect, protection. Otros cambian el final: create, creation; decorate, decoration; invite, invitation; inform, information; educate, education; pollute, pollution. Si conoces el verbo, puedes deducir el sustantivo.",
        "El sufijo -er en comparaciones se agrega a adjetivos cortos: fast, faster; cheap, cheaper; small, smaller. Si el adjetivo termina en y, cambia a ier: easy, easier. Si termina en una vocal y una consonante, se duplica la consonante: big, bigger. Con adjetivos largos se usa more y no -er: more expensive.",
        "Los conectores ayudan a leer: so (por eso, resultado), then (después), until (hasta que), also (además) y maybe (quizás, posibilidad). En el texto de la biblioteca, First, students fill in a form. Then the librarian checks... muestra orden; You can borrow a comic until Friday, so read it quickly muestra límite y resultado; Maybe it will open longer next month muestra una posibilidad.",
    ],
    [("-ion", "sufijo de sustantivos: -ción"), ("collect → collection", "colectar → colección"), ("faster / easier", "más rápido / más fácil"), ("so / then / until", "así que / después / hasta"), ("also", "además"), ("maybe", "quizás")],
    [
        ("Derivar con -ion", "El verbo es «decorate». ¿Cuál es el sustantivo con -ion y qué significa?", ["Decorate termina en e.", "Se quita la e y se agrega -ation o -ion: decoration.", "Significa decoración."], "Decoration: decoración"),
        ("Derivar con -er", "El adjetivo es «easy». ¿Cuál es su comparativo?", ["Easy termina en y.", "La y cambia a ier.", "Easier."], "Easier"),
    ],
    [
        ("Escribir «invition» en vez de invitation.", "El sustantivo de invite cambia a invitation.", "Aprende el patrón: invite, invitation."),
        ("Decir «more fast» en vez de faster.", "Fast es corto y lleva -er.", "Di faster than."),
    ],
    [
        ("¿Cuál es el sustantivo de «collect»? a) collection b) collecter", "a) collection", "El sufijo -ion forma el sustantivo."),
        ("¿Cuál es el sustantivo de «inform»? a) information b) informer", "a) information", "Inform forma information."),
        ("¿Cuál es el comparativo de «fast»? a) faster b) more fast", "a) faster", "Fast es un adjetivo corto."),
    ],
    [
        ("¿Cuál es el sustantivo de «create»? a) creation b) createion", "a) creation", "Se quita la e y se agrega -ion."),
        ("¿Cuál es el comparativo de «big»? a) bigger b) biger", "a) bigger", "Se duplica la consonante."),
        (INFO + " ¿Qué significa «also» en «The library also has a game room»? a) además b) hasta", "a) además", "Also agrega una idea más."),
    ],
    [
        (INFO + " ¿Qué conector del texto muestra el orden entre completar el formulario y revisar la información? a) Then b) until", "a) Then", "Then significa después."),
        (INFO + " ¿Hasta cuándo puedes pedir prestada la historieta? a) hasta el viernes b) hasta el lunes", "a) hasta el viernes", "Dice until Friday."),
        (INFO + " ¿Qué indica «Maybe it will open longer next month»? a) que es una posibilidad, no una certeza b) que ya abrió", "a) que es una posibilidad, no una certeza", "Maybe significa quizás."),
    ],
    [
        ("Completa con el sustantivo con -ion de «discuss»: «We had a long ___ about the project.» a) discussion b) discuss", "a) discussion", "Se necesita un sustantivo después de long."),
        ("¿Qué verbo da el sustantivo «protection»? a) protect b) protein", "a) protect", "Protection viene de protect."),
    ],
    [
        ("Completa con el comparativo: «The new bus is ___ than the old bus» (quiet). a) quieter b) more quiet", "a) quieter", "Quiet es corto y lleva -er."),
        (INFO + " ¿Qué conector une «You can borrow a comic until Friday» con «read it quickly»? a) so b) maybe", "a) so", "So muestra el resultado: leerla rápido."),
    ],
    [("Lees en un cartel: «Invitation to the school art exhibition. Come and see the new collection of paintings. Maybe you will find your favourite artist!» (invitation = invitación, exhibition = exposición, paintings = pinturas, favourite = favorito). ¿Qué verbo da la palabra «invitation»? a) invite b) invent", "a) invite", "Invitation viene de invite.")],
    [
        ("¿Qué sufijo forma sustantivos como action y collection?", "-ion", "Se parece a -ción."),
        ("En Inglés de 8.º (OA 10, clase 4): ¿Cuál es el comparativo de easy?", "Easier", "La y cambia a ier."),
        ("¿Qué indica maybe?", "Una posibilidad", "Maybe significa quizás y no una certeza."),
    ],
    task("Con esta lista de verbos de ejemplo: decorate, collect, connect, create, inform. Escribe el sustantivo con -ion de cada uno y su significado en español. Luego escribe una oración con easy y el comparativo easier y otra con maybe.", "Decoration (decoración), collection (colección), connection (conexión), creation (creación), information (información). The test is easier than the last one. Maybe we can finish today.", ["escribe cinco sustantivos con -ion", "escribe una oración con easier", "escribe una oración con maybe"], ["lista de cinco palabras", "dos oraciones"], ["escribir invition", "decir more easy"], "Reconoce los sustantivos bien formados y repasa el patrón de los verbos que terminan en e."),
    "Elige tres sustantivos con -ion y busca el verbo del que vienen.",
    "Escribe cinco comparativos de adjetivos que conozcas y úsalos en oraciones con than.",
)

# ------------------------------------------------------------------ OA 10, clase 5
DATA = "«Books borrowed from the school library (datos de ejemplo): March 120; April 150; May 90; June 180.»"
BIO2 = "«Rosa Lagos (persona de ejemplo) was born in a small coastal village. As a child, she repaired radios for her neighbours. Then she studied engineering and built a solar charger for rural schools. Because of her work, ten schools now have light in the evening. Today, she teaches students to build their own devices.» (coastal = costera, repaired = reparaba, neighbours = vecinos, engineering = ingeniería, solar charger = cargador solar, rural = rural, devices = aparatos)"

lesson(
    OA10, 5, MAT,
    "Aprenderé a leer por mi cuenta un gráfico de datos y una biografía breve: identificar el propósito, ideas, secuencia, causa-efecto y la diferencia hecho-opinión. Sirve para demostrar que entiendo textos no literarios nuevos.",
    ["Sé reconocer el propósito de un texto.", "Sé leer datos en una lista o en un gráfico."],
    [
        "Un gráfico (graph) muestra datos con barras, líneas o números. Para leerlo, identifica el título (qué mide), las categorías (por ejemplo, los meses) y los valores (cuánto). Compara los valores: el más alto, el más bajo y la diferencia entre ellos. En una lista de datos, como March 120; April 150, cada mes va con su número.",
        "Una biografía cuenta la vida de una persona y suele seguir un orden: infancia, estudios y trabajo actual. Marcas como as a child, then, because of her work y today señalan la secuencia y la causa. Busca los hechos que se pueden comprobar, como ten schools, y las opiniones, que no se pueden comprobar.",
        "Al leer solo, usa una rutina: 1) lee el título y el propósito, 2) identifica la idea general, 3) ubica los datos que piden las preguntas, 4) ordena los hechos y 5) separa los hechos de las opiniones. Justifica cada respuesta con una frase o un dato del texto.",
    ],
    [("graph", "gráfico"), ("data", "datos"), ("borrowed", "prestados"), ("highest / lowest", "más alto / más bajo"), ("difference", "diferencia"), ("because of", "debido a")],
    [
        ("Leer un gráfico", DATA + " ¿En qué mes se prestaron más libros y cuántos?", ["Comparo los cuatro valores.", "180 es el mayor.", "Junio, con 180 libros."], "Junio, con 180 libros"),
        ("Secuencia y causa", BIO2 + " ¿Qué consecuencia tuvo el trabajo de Rosa?", ["Busco la expresión Because of her work.", "Dice ten schools now have light in the evening.", "La consecuencia es que diez escuelas tienen luz de noche."], "Diez escuelas tienen luz en la noche"),
    ],
    [
        ("Tomar el primer número del gráfico como el mayor.", "Hay que comparar todos los valores.", "Lee todos los datos antes de decidir."),
        ("Confundir la secuencia de la vida con el orden del texto.", "Marcas como as a child y today indican cuándo ocurrió cada cosa.", "Subraya las marcas de tiempo."),
    ],
    [
        (DATA + " ¿En qué mes se prestaron menos libros? a) en mayo b) en marzo", "a) en mayo", "Mayo tiene 90."),
        (DATA + " ¿Cuántos libros se prestaron en abril? a) 150 b) 180", "a) 150", "El dato de abril es 150."),
        (BIO2 + " ¿Cuál es el propósito de la biografía? a) informar sobre la vida y el trabajo de Rosa b) vender un cargador", "a) informar sobre la vida y el trabajo de Rosa", "Cuenta su vida en orden."),
    ],
    [
        arith(DATA + " ¿Cuántos libros se prestaron en total en los cuatro meses?", "120+150+90+180", "Se suman los cuatro datos.", " libros"),
        arith(DATA + " ¿Cuántos libros más se prestaron en junio que en mayo?", "180-90", "Se resta el valor menor al mayor.", " libros"),
        (BIO2 + " ¿Qué hizo Rosa de niña? a) reparaba radios b) estudiaba ingeniería", "a) reparaba radios", "Dice As a child, she repaired radios."),
    ],
    [
        (BIO2 + " Ordena con números: (1) estudió ingeniería, (2) reparaba radios de niña, (3) hoy enseña a estudiantes.", "2, 1, 3", "Sigue la secuencia: as a child, then, today."),
        (DATA + " ¿Cuál es la tendencia de marzo a abril? a) subió b) bajó", "a) subió", "Pasó de 120 a 150."),
        (BIO2 + " ¿Qué conector del texto muestra la consecuencia de su trabajo? a) Because of b) Then", "a) Because of", "Because of her work introduce la consecuencia."),
    ],
    [
        (DATA + " Un lector dice: «Los préstamos bajaron de abril a mayo y subieron en junio». ¿Es correcto? a) sí, porque pasaron de 150 a 90 y luego a 180 b) no, porque siempre subieron", "a) sí, porque pasaron de 150 a 90 y luego a 180", "Los datos muestran bajada y subida."),
        (BIO2 + " ¿Cuál de estas frases es un hecho del texto? a) Ten schools now have light in the evening. b) Rosa is the best engineer ever.", "a) Ten schools now have light in the evening.", "Se puede comprobar; la otra es una opinión que el texto no dice."),
    ],
    [
        arith(DATA + " Si en julio se prestaran 30 libros más que en junio (dato de ejemplo), ¿cuántos libros serían?", "180+30", "Se suman los 30 libros a los de junio.", " libros"),
        (BIO2 + " Pedro dice que Rosa enseña a construir aparatos porque fue una niña famosa. ¿Qué dice realmente el texto? a) que enseña hoy a construir aparatos, sin hablar de fama b) que fue famosa de niña", "a) que enseña hoy a construir aparatos, sin hablar de fama", "El texto no menciona fama."),
    ],
    [("Lees en un informe de ejemplo: «Bottles recycled in our school: Monday 40; Tuesday 55; Wednesday 35. The recycling bin was full on Tuesday, so the caretaker emptied it.» (bottles = botellas, recycled = recicladas, bin = contenedor, full = lleno, caretaker = auxiliar, emptied = vació). ¿Qué día se recicló más y por qué vació el contenedor el auxiliar? a) el martes; porque estaba lleno b) el miércoles; porque estaba vacío", "a) el martes; porque estaba lleno", "Martes tiene 55 y dice so the caretaker emptied it.")],
    [
        ("¿Qué datos buscas primero en un gráfico?", "El título, las categorías y los valores", "Dicen qué mide y cuánto."),
        ("En Inglés de 8.º (OA 10, clase 5): ¿Qué expresión muestra una causa en una biografía?", "Because of", "Introduce la razón de algo."),
        ("¿Qué haces para justificar una respuesta?", "Cito una frase o un dato del texto", "Es la evidencia."),
    ],
    task("Lee estos textos de ejemplo. Gráfico: «Students who walk to school: Monday 30; Tuesday 45; Wednesday 38; Thursday 27.» Biografía breve: «Tomás Vera (persona de ejemplo) loved birds as a child. Then he studied biology and wrote a guide of local birds. Because of his guide, many families now count birds in their gardens.» (walk = caminan, birds = aves, biology = biología, guide = guía, local = locales, count = cuentan). Escribe el día con más estudiantes, el total de la semana y la consecuencia del trabajo de Tomás.", "Martes (45); total 140 (30+45+38+27); consecuencia: muchas familias cuentan aves en sus jardines.", ["ubica el valor más alto", "suma los cuatro datos", "cita la consecuencia"], ["hoja con tres respuestas", "nota de una persona de tu casa"], ["no sumar los cuatro valores", "confundir causa y consecuencia"], "Reconoce los datos bien ubicados y revisa la suma con una calculadora o a mano."),
    "Haz un gráfico de barras con los datos de los libros prestados y marca el mes más alto.",
    "Escribe una biografía de ejemplo de cuatro frases sobre una persona inventada, con as a child, then y because of.",
)
