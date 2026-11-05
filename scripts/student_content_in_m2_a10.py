"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 10: textos no literarios, propósito, estructura y lenguaje.

Todos los textos están escritos en el enunciado (originales, ficticios; los datos se rotulan «de ejemplo»). Inglés americano.
Los títulos de clase del plan son genéricos; aquí se aplican a formatos y propósito, idea principal y detalles, relaciones de
importancia y problema-solución, palabras clave, expresiones, collocations y conectores, y prefijos im-, in-, il-.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 10"

# ------------------------------------------------------------------ clase 1: formatos y propósito
F_AD = "«Swim Smart! Lessons for ages 12 to 17. Learn four strokes in eight weeks. Small groups, kind teachers and a free trial class. Sign up today and get 10% off.» (lessons = clases, ages = edades, strokes = estilos de nado, small groups = grupos pequeños, free trial = prueba gratis, off = de descuento)"
F_EM = "«From: Pia Soto. To: Mr. Vega. Subject: Change of meeting. Dear Mr. Vega, the science club meeting has moved to Thursday at 4:00 p.m. in room 12. Please tell the other members. Best regards, Pia.» (subject = asunto, change = cambio, moved = se cambió, members = integrantes, best regards = saludos)"
F_CAT = "«Catalog (example). Headphones A: 15,000 pesos, black, wired, 1-year guarantee. Headphones B: 28,000 pesos, white, wireless, 2-year guarantee.» (catalog = catálogo, headphones = audífonos, wired = con cable, wireless = inalámbricos, guarantee = garantía)"
F_BIO = "«Rosa Meyer (biography, fictional). Rosa Meyer was born in a small town and became a nurse at the age of twenty-two. She worked for thirty years in a children's hospital. She taught young nurses and helped start a school for caregivers.» (biography = biografía, born = nació, nurse = enfermera, taught = enseñó, caregivers = cuidadores)"
F_PR = "«How to Save a File. First, click the File menu. Second, choose Save As. Third, type a name. Finally, click Save.» (file = archivo, menu = menú, choose = elige, type = escribe, name = nombre)"
F_RV = "«Review: The Silver Key (fictional book). I liked the main character because she is brave and funny. The story moves fast, but the ending is a little predictable. I give it four stars out of five.» (review = reseña, key = llave, brave = valiente, ending = final, predictable = predecible, stars = estrellas)"
F_DL = "«Dialogue (fictional). Ana: Excuse me, how do I get to the library? Leo: Go straight for two blocks and turn left. Ana: Is it far? Leo: No, it is five minutes on foot.» (excuse me = disculpa, straight = derecho, block = cuadra, turn left = dobla a la izquierda, far = lejos, on foot = a pie)"
F_SP = "«Dear graduates, today you finish a stage. Thank you to your families and teachers. Remember: you are ready for the next step. Never stop learning!» (graduates = egresados, stage = etapa, ready = listos, step = paso, never stop = nunca dejes de)"
F_GR = "«Graph (example data): Hours of exercise per week. Ages 12-13: 5 hours. Ages 14-15: 4 hours. Ages 16-17: 3 hours.» (graph = gráfico, hours = horas, exercise = ejercicio, ages = edades)"

lesson(
    OA, 1, MAT_R,
    "Aprenderé a reconocer el formato y el propósito de textos no literarios como avisos, correos, catálogos, biografías, procedimientos, reseñas, discursos y gráficos. Sirve para saber qué buscar y cómo leer cada tipo de texto.",
    ["Sé que un texto puede informar, convencer o enseñar.", "Conozco palabras como price, guarantee y subject."],
    [
        "Los textos no literarios entregan información del mundo real. Cada formato tiene una forma y un propósito. Un aviso publicitario (advertisement) quiere convencer de comprar y usa órdenes y ofertas. Un correo electrónico (email) comunica un mensaje a alguien y tiene asunto, saludo y despedida. Un catálogo (catalog) lista productos con precios y características. Una biografía (biography) cuenta la vida de una persona.",
        "Un procedimiento (procedure) enseña pasos en orden con first, second y finally. Una reseña (review) da una opinión sobre un libro o un producto. Un discurso (speech) se dirige a un público para motivar o agradecer. Un gráfico (graph) muestra datos con barras o líneas. Un diálogo (dialogue) reproduce la conversación entre dos personas y se reconoce por los turnos de cada hablante. Las noticias informan hechos recientes. Una descripción detalla cómo es algo.",
        "Para reconocer el propósito, mira tres pistas: la forma (pasos, columnas, saludo), el lenguaje (órdenes, opiniones, datos, fechas) y el cierre (Sign up today, Thank you, I give it four stars). Pregúntate: ¿quiere informar, convencer, enseñar, comunicar, opinar o motivar?",
    ],
    [("advertisement", "aviso publicitario: convencer"), ("email", "correo electrónico: comunicar"), ("catalog", "catálogo: listar productos"), ("procedure", "procedimiento: pasos"), ("review", "reseña: opinión"), ("graph", "gráfico: datos"), ("dialogue", "diálogo: conversación por turnos")],
    [
        ("Reconocer el propósito de un aviso", F_AD + " ¿Qué formato es y cuál es su propósito?", ["Tiene una oferta y una invitación: Sign up today.", "Es un aviso publicitario.", "Su propósito es convencer de inscribirse."], "Es un aviso; quiere convencer de inscribirse en clases de natación"),
        ("Reconocer un procedimiento", F_PR + " ¿Qué formato es y cómo lo sabes?", ["Hay First, Second, Third y Finally.", "Las oraciones son órdenes.", "Enseña a hacer algo."], "Es un procedimiento: enseña pasos con First, Second, Third y Finally"),
    ],
    [
        ("Pensar que un catálogo quiere convencer de comprar por su tono.", "Un catálogo lista productos y datos; la publicidad usa ofertas y órdenes.", "Mira si hay columnas de precios y características."),
        ("Confundir una reseña con una noticia.", "La reseña da una opinión; la noticia informa hechos.", "Busca frases como I liked y I give it four stars."),
    ],
    [
        mr(F_EM, "¿Cuál es el propósito del correo?", "Avisar a los integrantes un cambio de reunión", ["Convencer de comprar una entrada", "Contar una anécdota de la reunión"], "Dice the meeting has moved y Please tell the other members."),
        mr(F_CAT, "¿Qué formato es?", "Un catálogo", ["Una reseña", "Un discurso"], "Lista productos con precios y características."),
        mr(F_RV, "¿Qué formato es?", "Una reseña", ["Una noticia", "Un catálogo"], "Dice I liked y I give it four stars."),
    ],
    [
        mr(F_BIO, "¿Qué cuenta este texto?", "La vida de una persona", ["Pasos para hacer algo", "Una oferta de productos"], "Es una biografía."),
        mr(F_SP, "¿Qué quiere lograr el hablante?", "Agradecer y motivar a los egresados y sus familias", ["Vender un producto a las familias", "Enseñar cómo se organiza una ceremonia"], "Dice Thank you y Never stop learning."),
        mr(F_GR, "¿Qué muestra el gráfico?", "Las horas de ejercicio por edad", ["El precio de audífonos", "Los pasos para guardar un archivo"], "Dice Hours of exercise per week."),
    ],
    [
        mr(F_AD, "¿Qué oferta hace el aviso?", "Un 10% de descuento al inscribirse hoy", ["Un 10% más de clases si se inscribe hoy", "Clases gratis durante todo el año"], "Dice Sign up today and get 10% off."),
        mr(F_CAT, "¿Cuál audífono tiene mayor garantía?", "El B, con dos años", ["El A, con tres años", "Los dos tienen la misma"], "Headphones B tiene 2-year guarantee."),
        arith("En el catálogo, los audífonos A cuestan 15.000 pesos y los B 28.000 pesos. ¿Cuántos pesos más cuestan los B?", "28000-15000", "Se resta el precio menor del mayor.", " pesos"),
    ],
    [
        mr(F_RV, "Una compañera dice que la reseña es una noticia porque da una calificación. ¿Qué respuesta es más acertada?", "Es una reseña porque da una opinión personal y una calificación con estrellas", ["Es una noticia porque da una calificación con números y estrellas", "Es un correo porque habla de un libro y da una calificación"], "Las opiniones y estrellas son propias de la reseña."),
        mr(F_BIO, "¿Qué detalle muestra que el texto es una biografía?", "Cuenta etapas de la vida: nacimiento, trabajo y enseñanza", ["Da pasos ordenados para hacer algo con First y Finally", "Presenta datos en columnas con precios y características del producto"], "La biografía narra la vida en orden."),
    ],
    [
        mr(F_PR + " " + F_AD, "Dos textos usan órdenes. ¿En qué se diferencian los propósitos?", "El procedimiento enseña pasos y el aviso busca convencer de inscribirse en las clases", ["Los dos quieren vender, pero el aviso lo hace con ofertas y el otro con pasos", "Los dos cuentan una historia, pero uno lo hace con pasos numerados"], "El mismo recurso (órdenes) sirve para propósitos distintos."),
        mr(F_EM, "Un estudiante dice que el correo busca convencer. ¿Qué dato lo contradice?", "No ofrece nada ni pide comprar: informa un cambio de reunión", ["Tiene un saludo al comienzo y una despedida al final", "Tiene un asunto escrito en la parte de arriba"], "El correo informa y pide avisar a otros."),
    ],
    [mr(F_DL, "Este texto tiene turnos de dos personas que hablan. ¿Qué formato es y para qué sirve?", "Un diálogo, que sirve para pedir y dar una indicación de camino", ["Un procedimiento, que enseña pasos escritos para hacer algo", "Una noticia, que informa un hecho reciente de la ciudad"], "Los turnos de Ana y Leo muestran un diálogo; la pregunta y la respuesta dan una indicación.")],
    [
        ("En Inglés de 2.º medio (OA 10, clase 1): ¿qué formato tiene pasos con first, second y finally?", "Un procedimiento", "Enseña a hacer algo."),
        ("En Inglés de 2.º medio (OA 10, clase 1): ¿qué formato quiere convencer de comprar?", "Un aviso publicitario", "Usa ofertas y órdenes."),
        ("En Inglés de 2.º medio (OA 10, clase 1): ¿qué formato da una opinión sobre un libro?", "Una reseña", "Incluye opiniones y calificación."),
    ],
    task("Lee: «Notice (fictional). The school choir will hold a bake sale on Friday from 3 to 5 p.m. in the gym. Come and buy a cake to help us pay for new uniforms. Everyone is welcome!» (choir = coro, bake sale = venta de pasteles, gym = gimnasio, uniforms = uniformes, welcome = bienvenido). Escribe el formato, el propósito, dos pistas del texto y una pregunta que el lector puede contestar con él.", "Formato: aviso. Propósito: invitar a una venta de pasteles del coro. Pistas: Come and buy a cake y Everyone is welcome. Pregunta: ¿Dónde es la venta?", ["identifica el formato", "explica el propósito", "da dos pistas y una pregunta"], ["hoja con cuatro respuestas"], ["confundir aviso con noticia", "dar pistas sin conexión con el propósito"], "Pide que explique por qué este texto no es un procedimiento."),
    "Clasifica en una tabla, con formato y propósito, los ocho textos de la clase: aviso, correo, catálogo, biografía, procedimiento, reseña, discurso y gráfico.",
    "Busca en tu casa un papel con información (boleta, afiche, folleto) y anota su formato y propósito.",
)

# ------------------------------------------------------------------ clase 2: idea principal, información específica y detalles
MG = "«Magazine article (fictional): Why Walk More? Many people spend most of the day sitting. Experts say that a short walk after lunch can help us feel more awake. A group of office workers tried it for a month. A large number of them reported more energy in the afternoon, and few felt tired.» (magazine article = artículo de revista, experts = especialistas, sitting = sentadas, awake = despiertos, office workers = oficinistas, reported = dijeron tener, energy = energía)"
WP = "«Web page (fictional): Youth Orchestra Auditions. Who can join? Students aged 12 to 18. When? Saturday, March 9, at 10 a.m. Where? Room 4 of the music school. What to bring? Your instrument and a short piece. How long? About ten minutes per student.» (web page = página web, auditions = audiciones, aged = de edades, instrument = instrumento, piece = pieza)"
GP = "«Graph (example data): Students' favorite lunch. Pasta: 12. Chicken and rice: 9. Salad: 6. Sandwich: 3.» (favorite = favorito, chicken = pollo, rice = arroz)"
DS = "«Description (fictional): The Old Market. The market has narrow streets and colorful stalls. In the morning, it smells of fresh bread and fruit. People greet each other, and the sellers shout the day's prices.» (narrow = angostas, stalls = puestos, smells = huele, greet = saludan, sellers = vendedores, shout = gritan)"

lesson(
    OA, 2, MAT_R,
    "Aprenderé a identificar la idea principal, la información específica y los detalles en textos no literarios como artículos, páginas web, gráficos y descripciones. Sirve para entender un texto informativo y responder con datos exactos.",
    ["Sé identificar el propósito de un texto.", "Sé leer datos y gráficos."],
    [
        "La idea principal (main idea) de un texto no literario suele estar en el título y en la primera o la última oración. Pregunta: ¿qué quiere decir el autor sobre el tema? La información específica (specific information) es el dato que responde una pregunta concreta: who, when, where, how many. Los detalles (supporting details) son datos y ejemplos que apoyan la idea principal.",
        "En un artículo de revista, la idea principal puede formularse como una pregunta o afirmación en el título (Why Walk More?). En una página web, los subtítulos y las preguntas (Who can join? When?) organizan los datos. En un gráfico, el título dice el tema y las cifras comparan. En una descripción, los adjetivos y los verbos de sentidos (smells of, looks like) muestran cómo es el lugar.",
        "Para responder con datos, regresa al texto y localiza la palabra clave de la pregunta (scanning). Lee el pasaje completo y comprueba que el dato responde la pregunta, no una parecida. Si se pide una idea principal, no escojas un detalle ni una opinión aislada.",
    ],
    [("main idea", "idea principal"), ("specific information", "información específica"), ("supporting detail", "detalle que apoya"), ("subheading", "subtítulo"), ("scanning", "buscar un dato puntual"), ("graph title", "título del gráfico")],
    [
        ("Idea principal y detalle", MG + " ¿Cuál es la idea principal y cuál es un detalle?", ["El título pregunta Why Walk More?", "La idea es que una caminata corta después del almuerzo puede dar más energía.", "Un detalle es que un grupo de oficinistas lo probó un mes."], "Idea: caminar un poco después del almuerzo da energía. Detalle: un grupo de oficinistas lo probó por un mes"),
        ("Ubicar datos en una página web", WP + " ¿Cuándo y dónde son las audiciones?", ["Busco When? y Where?", "Dice Saturday, March 9, at 10 a.m.", "Dice Room 4 of the music school."], "El sábado 9 de marzo a las 10 a.m., en la sala 4 de la escuela de música"),
    ],
    [
        ("Elegir un detalle como idea principal.", "Un detalle apoya la idea, pero no resume el texto.", "Pregunta si la idea cubre todo el texto."),
        ("Responder con un dato parecido a lo que se pide.", "Se pierde la precisión del texto.", "Relee la pregunta y busca la palabra clave exacta."),
    ],
    [
        mr(WP, "¿Qué debe llevar un estudiante a la audición?", "Su instrumento y una pieza corta", ["Un libro de partituras y su cuaderno", "Una autorización firmada por un adulto"], "Dice Your instrument and a short piece."),
        mr(GP, "¿Cuál es el almuerzo favorito de más estudiantes?", "Pasta", ["Ensalada", "Sándwich"], "Pasta tiene 12, el mayor número."),
        mr(DS, "¿Qué huele en la mañana en el mercado?", "Pan fresco y fruta", ["Pescado fresco y sal de mar", "Flores y café recién hecho"], "Dice smells of fresh bread and fruit."),
    ],
    [
        mr(MG, "¿Qué dijeron muchas personas del grupo que probó la caminata?", "Que tenían más energía en la tarde y pocos se sentían cansados", ["Que se sentían más cansadas después de caminar", "Que preferían sentarse después del almuerzo"], "Dice A large number ... reported more energy."),
        mr(WP, "¿Cuánto dura cada audición?", "Unos diez minutos", ["Cerca de una hora por grupo", "Todo un sábado completo"], "Dice About ten minutes per student."),
        mr(DS, "¿Cómo son las calles del mercado?", "Angostas", ["Anchas y vacías por la mañana", "Silenciosas y sin gente"], "Dice narrow streets."),
    ],
    [
        arith("Según el gráfico, 12 estudiantes eligen pasta y 9 eligen pollo con arroz. ¿Cuántos estudiantes eligen alguna de las dos?", "12+9", "Se suman las dos columnas del gráfico.", " estudiantes"),
        mr(WP, "¿Quiénes pueden ingresar a la orquesta?", "Estudiantes de 12 a 18 años", ["Cualquier adulto que toque un instrumento", "Solo niños de 5 a 11 años de la escuela"], "Dice Students aged 12 to 18."),
        mr(DS, "¿Qué hace la gente en el mercado?", "Se saluda entre sí", ["Duerme mientras vende", "Corre por las calles"], "Dice People greet each other."),
    ],
    [
        mr(GP, "Un compañero dice que más de la mitad prefiere pasta. ¿Qué respuesta es más acertada?", "No: 12 de 30 es menos que la mitad", ["Sí: 12 es el número más alto del gráfico", "Sí: casi todos eligieron pasta"], "La mitad de 30 es 15 y 12 es menor."),
        mr(MG, "Un lector dice que el texto prueba que caminar cura cualquier cosa. ¿Qué responde alguien que lee con cuidado?", "No: solo dice que algunos sintieron más energía después de caminar", ["Sí: el texto prueba que caminar cura cualquier enfermedad", "No: el texto no habla de caminar ni de energía"], "El texto no afirma tanto."),
    ],
    [
        mr(WP, "¿Cuál es la idea principal de la página web?", "Informar cómo y cuándo participar en las audiciones de la orquesta", ["Contar la historia de la orquesta juvenil y sus músicos", "Vender instrumentos y partituras a los estudiantes"], "Resume los datos de participación."),
        mr(DS, "¿Cuál es la idea principal de la descripción?", "Mostrar cómo es un mercado con sus colores, olores y gente", ["Contar un viaje que alguien hizo a un mercado antiguo", "Enseñar a comprar frutas y pan al mejor precio"], "Los detalles describen el lugar."),
    ],
    [arith("En el gráfico, 12 estudiantes eligen pasta, 9 pollo con arroz, 6 ensalada y 3 sándwich. ¿Cuántos estudiantes respondieron en total?", "12+9+6+3", "Se suman las cuatro columnas del gráfico.", " estudiantes")],
    [
        ("En Inglés de 2.º medio (OA 10, clase 2): ¿dónde suele estar la idea principal?", "En el título y en la primera o última oración", "Ahí el autor resume el tema."),
        ("En Inglés de 2.º medio (OA 10, clase 2): ¿qué es un detalle?", "Un dato o ejemplo que apoya la idea principal", "No resume todo el texto."),
        ("En Inglés de 2.º medio (OA 10, clase 2): ¿qué hace el título de un gráfico?", "Dice qué tema muestran los datos", "Sin título no se entiende."),
    ],
    task("Lee: «Web page (fictional): Reading Club. What is it? A weekly club for students who like books. When? Every Wednesday at 4:30 p.m. Where? Library, second floor. How much? It is free. Bring a book you want to share.» (weekly = semanal, share = compartir, floor = piso). Escribe la idea principal, tres datos específicos y una pregunta que se pueda responder con el texto.", "Idea principal: un club de lectura semanal. Datos: miércoles 4:30 p.m.; biblioteca, segundo piso; es gratis. Pregunta: ¿Cuánto cuesta?", ["escribe la idea principal", "da tres datos específicos", "formula una pregunta respondible"], ["hoja con cinco respuestas"], ["elegir un detalle como idea principal", "inventar datos"], "Pide que cambie la pregunta por otra que use when."),
    "Lee de nuevo el gráfico y escribe dos preguntas con how many.",
    "Elige un afiche y escribe su idea principal y tres datos.",
)

# ------------------------------------------------------------------ clase 3: relaciones de importancia y problema-solución
NW = "«News (fictional): Library Opens a Game Room. The Central Library has opened a game room for students. The problem was that many teenagers did not have a quiet place to spend time after school. Now they can play board games and read from Monday to Friday. The librarian said the room is already full by four o'clock.» (news = noticia, game room = sala de juegos, teenagers = adolescentes, board games = juegos de mesa, librarian = bibliotecaria, full = llena)"
RV = "«Review (fictional): The Quiet Café. The café is small and calm, so it is perfect for studying. The most important thing for me is the Wi-Fi, which works well. However, the chairs are not comfortable, and the prices are rather high. I would go again, unless I need to stay for hours.» (calm = tranquilo, perfect = perfecto, works well = funciona bien, however = sin embargo, comfortable = cómodas, prices = precios)"
AR = "«Article (fictional): Fewer Cars, More Space. A town had a problem: the main street was crowded with cars, and families could not walk safely. The council decided to close the street to cars on Sundays. As a result, many families now walk and shop there, and sales in small shops have grown.» (crowded = repleta, safely = con seguridad, council = municipalidad, close = cerrar, sales = ventas, shops = tiendas, grown = aumentado)"
SP = "«Speech (fictional): To Our Volunteers. Above all, I want to thank you. First, you gave your time. Second, you taught the younger children. Finally, you made friends. A small detail, like the color of the T-shirt, is not important.» (volunteers = voluntarios, gave = dieron, taught = enseñaron, younger = menores, T-shirt = polera)"

lesson(
    OA, 3, MAT_R,
    "Aprenderé a reconocer en textos no literarios qué ideas son más importantes y cuál es el problema y su solución. Sirve para entender la estructura de noticias, reseñas, artículos y discursos.",
    ["Sé identificar la idea principal.", "Conozco as a result y however."],
    [
        "Las ideas de un texto no tienen el mismo peso. Las señales de importancia son the most important thing, above all, first of all, mainly. Las ideas de apoyo se marcan con also, for example, second y finally. Las ideas menos importantes se marcan con a small detail o is not important. Estas señales ayudan a ordenar la información.",
        "Muchos textos informativos presentan un problema y una solución. El problema se marca con the problem was, many people could not, there was no... La solución, con decided to, now, The council closed the street. El resultado, con as a result, so y now. Las reseñas usan however y but para contrastar lo bueno con lo malo.",
        "Para analizar, divide tu hoja en tres columnas: problem, solution y result. Si el texto es una reseña, usa pro y con. Después subraya la frase que marca la idea más importante y comprueba que no es solo un detalle.",
    ],
    [("the most important thing / above all", "lo más importante / sobre todo"), ("problem / solution / result", "problema / solución / resultado"), ("however / but", "sin embargo / pero"), ("as a result", "como resultado"), ("now", "ahora"), ("unless", "a menos que")],
    [
        ("Problema, solución y resultado", NW + " ¿Cuál es el problema, la solución y el resultado?", ["El problema: no tenían un lugar tranquilo después del colegio.", "La solución: una sala de juegos en la biblioteca.", "El resultado: la sala ya está llena a las cuatro."], "Problema: no había lugar tranquilo; solución: sala de juegos; resultado: la sala se llena a las cuatro"),
        ("Importancia en un discurso", SP + " ¿Cuál es la idea más importante y cuál es un detalle sin importancia?", ["Above all marca la idea más importante: agradecer.", "First, Second y Finally dan razones.", "El color de la polera se marca como no importante."], "Lo más importante es agradecer; el color de la polera no es importante"),
    ],
    [
        ("Pensar que la última idea de una lista es siempre la más importante.", "La importancia la dicen las señales, no la posición.", "Busca above all o the most important thing."),
        ("Poner el resultado como si fuera el problema.", "Se pierde el orden causal.", "Busca decided to para la solución y as a result para el resultado."),
    ],
    [
        mr(AR, "¿Cuál es el problema?", "La calle estaba repleta de autos y las familias no podían caminar con seguridad", ["Que había pocas tiendas en la calle principal y las ventas eran bajas", "Que nadie vivía en la ciudad y las calles estaban vacías"], "Dice A town had a problem."),
        mr(AR, "¿Cuál es la solución?", "Cerrar la calle a los autos los domingos", ["Construir más estacionamientos en la calle principal", "Prohibir las tiendas de la calle los domingos"], "Dice The council decided to close the street."),
        mr(RV, "¿Qué es lo más importante para quien escribe la reseña?", "El Wi-Fi", ["Las sillas", "Los precios"], "Dice The most important thing for me is the Wi-Fi."),
    ],
    [
        mr(AR, "¿Qué resultado produjo la solución?", "Más familias caminan y compran allí, y las ventas de las tiendas subieron", ["Las tiendas cerraron porque ya no llegaban autos", "Hay más autos y la calle sigue repleta de gente y ruido"], "As a result, many families now walk and shop there."),
        mr(RV, "¿Qué aspecto negativo menciona la reseña?", "Las sillas incómodas y los precios altos", ["El Wi-Fi, que funciona mal y se corta seguido", "La calma, que molesta a quien quiere conversar"], "Dice However, the chairs are not comfortable and the prices are rather high."),
        mr(NW, "¿Qué dice la bibliotecaria?", "Que la sala ya está llena a las cuatro", ["Que la sala cerrará pronto por falta de espacio", "Que no hay juegos para todos los estudiantes"], "Dice the room is already full by four o'clock."),
    ],
    [
        mr(RV, "¿Cuándo no volvería al café quien escribe la reseña?", "Si necesita quedarse por horas", ["Si necesita conectarse al Wi-Fi para estudiar", "Si el café está tranquilo y vacío"], "Dice I would go again, unless I need to stay for hours."),
        mr(SP, "¿Cuántas razones de agradecimiento da con First, Second y Finally?", "Tres", ["Dos", "Cuatro"], "Se enumeran tres: dieron su tiempo, enseñaron y hicieron amigos."),
        arith("En una encuesta de ejemplo, antes del cierre 60 familias caminaban cada domingo por la calle; después, 150 familias lo hacen. ¿Cuántas familias más caminan?", "150-60", "Se resta la cantidad anterior de la actual.", " familias"),
    ],
    [
        mr(NW, "Un lector dice que la solución fue cerrar la biblioteca. ¿Qué responde alguien que lee con cuidado?", "No: la solución fue abrir una sala de juegos para estudiantes", ["Sí: el problema era que la biblioteca estaba abierta", "No: el texto no menciona ninguna solución"], "El texto dice The Central Library has opened a game room."),
        mr(RV, "Un lector dice que la reseña es totalmente positiva. ¿Qué palabra lo contradice?", "However, que introduce lo negativo", ["Perfect, que describe el lugar con exageración", "Calm, que describe cómo se siente el lugar"], "However introduce lo negativo."),
    ],
    [
        mr(AR + " " + NW, "Los dos textos presentan un problema y una solución. ¿Qué tienen en común?", "Una solución que cambia el uso de un espacio para las personas", ["Un problema de tránsito en una calle principal", "Una crítica a un café por sus precios"], "Ambas cambian un espacio público."),
        mr(SP, "¿Qué idea del discurso se considera de menor importancia?", "El color de la polera", ["Agradecer", "Enseñar a los menores"], "Dice a small detail ... is not important."),
    ],
    [mr(RV, "Resume la reseña con pro y con. ¿Qué opción es correcta?", "Pro: calma y buen Wi-Fi; con: sillas incómodas y precios altos", ["Pro: calma y precios altos; con: Wi-Fi y sillas incómodas", "Pro: sillas cómodas y precios bajos; con: poca calma y mal Wi-Fi"], "Resume lo bueno y lo malo que dice el texto.")],
    [
        ("En Inglés de 2.º medio (OA 10, clase 3): ¿qué palabras marcan la idea más importante?", "Above all y the most important thing", "Son señales de importancia."),
        ("En Inglés de 2.º medio (OA 10, clase 3): ¿qué conector marca el resultado?", "As a result", "Introduce la consecuencia."),
        ("En Inglés de 2.º medio (OA 10, clase 3): ¿qué conector introduce un aspecto negativo en una reseña?", "However", "Marca un contraste."),
    ],
    task("Lee: «News (fictional): Neighborhood Fixes a Dark Corner. A dark corner near the school made many students feel unsafe. The neighbors asked the city for a streetlight, and the city installed one last week. As a result, students now walk home with more confidence.» (corner = esquina, unsafe = inseguros, streetlight = farol, installed = instaló, confidence = confianza). Completa una tabla con problem, solution y result, y escribe cuál es la idea más importante.", "Problema: una esquina oscura hacía sentir inseguros a los estudiantes. Solución: la ciudad instaló un farol. Resultado: ahora caminan con más confianza. Idea más importante: pedir un farol resolvió el problema.", ["completa las tres columnas", "indica la idea más importante", "usa datos del texto"], ["tabla de tres columnas en la hoja"], ["poner el resultado en la columna de solución", "no justificar la idea más importante"], "Pide que explique con qué conector supo cuál era el resultado."),
    "Busca en una noticia en español el problema, la solución y el resultado.",
    "Escribe una reseña de tres líneas de algo que usas con una frase con however.",
)

# ------------------------------------------------------------------ clase 4: palabras clave, expresiones, collocations y conectores
K1 = "«Notice (fictional): Student Council Elections. Candidates must hand in their form before Friday. Voting will take place on Tuesday. Neither the principal nor the teachers can vote for the council, but they will help count the votes. If you cannot vote on Tuesday, you can either vote early on Monday or vote in the library on Wednesday. As soon as the results are ready, we will post them on the board.» (elections = elecciones, principal = director, candidates = candidatos, hand in = entregar, form = formulario, voting = votación, vote = votar, council = centro de estudiantes, count = contar, results = resultados, board = panel)"
K2 = "«Tips (fictional): How to Prepare for an Interview. Do some research about the company. Make a good first impression by arriving early. Pay attention to the questions and take your time before answering. Even if you are nervous, try to smile. Break the ice with a short greeting. It will be a piece of cake if you practice.» (tips = consejos, interview = entrevista, research = investigación, impression = impresión, nervous = nervioso, smile = sonreír, greeting = saludo)"
K3 = "«Report (fictional): Student Survey. A large number of students said they arrive late because of traffic. Others said they hardly ever arrive late. Although the bus is cheap, it is slow. As a result, the school will consider a later start time.» (report = informe, survey = encuesta, traffic = tránsito, consider = evaluar, start time = hora de inicio)"

lesson(
    OA, 4, MAT_R,
    "Aprenderé a identificar palabras clave, expresiones idiomáticas, collocations y conectores en textos no literarios. Sirve para entender cómo se relacionan las ideas y cuáles son las palabras que más importan.",
    ["Sé reconocer conectores como and, but y because.", "Conozco collocations como make a decision y pay attention."],
    [
        "Las palabras clave (key words) son las que más se repiten o las que contienen el tema: voting, candidates, council. El vocabulario temático es el conjunto de palabras de un mismo tema (en el aviso de elecciones: candidates, voting, results). Las expresiones idiomáticas (idioms) tienen un sentido que no sale de traducir palabra por palabra: break the ice, a piece of cake. Las collocations son combinaciones frecuentes: hand in a form, make a good impression, pay attention, do research, take your time.",
        "Los conectores muestran relaciones. Neither ... nor niega las dos opciones; either ... or presenta dos opciones; though o although contrasta; unless es una condición negativa; as soon as marca el momento; as a result marca la consecuencia. En los informes aparecen también hardly ever (casi nunca) y a large number of (muchos). Los conectores del año anterior siguen siendo útiles: and, but, because, so, when, if, then, after, before. Con neither ... nor, el verbo concuerda con el sujeto más cercano.",
        "Al leer, subraya con un color las palabras clave, con otro los conectores y encierra las collocations. Si no conoces una palabra, usa el contexto. Pregúntate qué relación marca cada conector y cómo cambiaría el sentido sin él.",
    ],
    [("key words", "palabras clave"), ("idiom", "expresión idiomática"), ("collocation", "combinación frecuente"), ("neither ... nor / either ... or", "ni ... ni / o ... o"), ("although / though", "aunque / sin embargo"), ("as soon as / as a result", "tan pronto como / como resultado"), ("hardly ever / a large number of", "casi nunca / muchos")],
    [
        ("Reconocer collocations", K2 + " ¿Qué collocations aparecen?", ["Busco verbo y sustantivo juntos.", "Do some research y make a good impression.", "También pay attention."], "Do research, make a good impression y pay attention"),
        ("Interpretar conectores", K1 + " ¿Qué opciones tiene quien no puede votar el martes?", ["Busco either ... or.", "Dice vote early on Monday or vote in the library on Wednesday.", "Esas son las dos opciones."], "Votar antes, el lunes, o votar en la biblioteca el miércoles"),
    ],
    [
        ("Traducir break the ice como romper hielo en el sentido literal.", "Es una expresión que significa empezar la conversación.", "Usa el contexto: greeting indica una conversación."),
        ("Usar are en Neither the principal nor the teacher are present.", "El verbo concuerda con el sujeto más cercano, teacher.", "Di Neither the principal nor the teacher is present."),
    ],
    [
        mr(K1, "¿Qué palabra clave aparece más en el aviso?", "vote / voting", ["form / board", "teachers / principal"], "Es el tema del aviso."),
        mr(K2, "¿Qué expresión idiomática del texto significa «muy fácil»?", "a piece of cake", ["break the ice", "make a good impression"], "A piece of cake significa muy fácil."),
        mr(K3, "¿Qué conector marca una consecuencia?", "As a result", ["Although", "Hardly ever"], "As a result introduce la consecuencia."),
    ],
    [
        mr(K1, "¿Quiénes no pueden votar por el centro de estudiantes?", "Ni el director ni los profesores", ["Solo el director del colegio, no los profesores", "Todos los estudiantes que no sean candidatos"], "Dice Neither the principal nor the teachers can vote."),
        mr(K1, "¿Cuándo se publicarán los resultados?", "Tan pronto como estén listos", ["Antes de que empiece la votación del martes", "El lunes, cuando se entreguen los formularios"], "Dice As soon as the results are ready."),
        mr(K3, "¿Qué relación marca although en Although the bus is cheap, it is slow?", "Contraste", ["Causa", "Condición"], "Although contrasta cheap con slow."),
    ],
    [
        mc("Completa en presente: Neither the teacher nor the students ____ ready.", "are", ["is", "was"], "El verbo concuerda con students, el sujeto más cercano."),
        mc("Completa: I will not go ____ you come with me.", "unless", ["as a result", "although"], "Unless significa a menos que."),
        mc("Completa con la collocation correcta: She wants to ____ a good impression.", "make", ["do", "take"], "Se dice make a good impression."),
    ],
    [
        mr(K2, "Un lector dice que break the ice significa romper un hielo de verdad. ¿Qué respuesta es más acertada?", "No: significa empezar la conversación con un saludo amable", ["Sí: significa romper un hielo de verdad antes de saludar", "No: significa cortar el saludo para empezar a trabajar"], "El texto dice Break the ice with a short greeting."),
        mr(K3, "Un lector dice que hardly ever significa casi siempre. ¿Qué respuesta es mejor?", "No: significa casi nunca", ["Sí: significa casi siempre", "Sí: significa nunca"], "Others said they hardly ever arrive late."),
    ],
    [
        mr(K1, "Une las ideas del texto con el conector correcto: si no puedes votar el martes, puedes votar el lunes o votar el miércoles. ¿Qué conectores se usan?", "If y either ... or, que presenta dos opciones", ["Unless y neither ... nor", "Although y as a result"], "El texto usa If y either ... or."),
        mr(K3, "¿Qué conectores aparecen en el texto del informe?", "Although y as a result", ["Neither ... nor y either ... or", "Unless y as soon as"], "Aparecen en la tercera y cuarta oración."),
    ],
    [mr(K2, "Elige las tres mejores palabras clave del texto de entrevistas.", "interview, research, impression", ["bicycle, window, bread", "company, music, door"], "Son las que resumen el tema.")],
    [
        ("En Inglés de 2.º medio (OA 10, clase 4): ¿qué es una collocation?", "Una combinación frecuente de palabras", "Se aprende como bloque."),
        ("En Inglés de 2.º medio (OA 10, clase 4): ¿qué significa unless?", "A menos que", "Es condición negativa."),
        ("En Inglés de 2.º medio (OA 10, clase 4): ¿qué marcan las palabras clave?", "El tema del texto", "Se repiten o lo contienen."),
    ],
    task("Lee: «Notice (fictional): Park Cleanup Day. Neither rain nor wind will cancel the event, so come ready. You can either bring your own gloves or borrow a pair. As soon as the cleanup is done, we will have juice and sandwiches for everyone. Come and make a difference in our park!» (cleanup = limpieza, event = actividad, gloves = guantes, borrow = pedir prestado, juice = jugo, make a difference = marcar una diferencia). Subraya dos conectores de la lista de la clase, una collocation y escribe la idea del aviso.", "Conectores: neither ... nor, either ... or, as soon as. Collocation: make a difference. Idea: se invita a una limpieza del parque que se hará con lluvia o viento, y habrá jugo al final.", ["subraya dos conectores", "identifica una collocation", "escribe la idea del aviso"], ["hoja con tres respuestas"], ["confundir neither con either", "no ver la relación de cada conector"], "Pide que cambie un conector por otro y explique cómo cambia el sentido."),
    "Subraya con colores las palabras clave y los conectores del aviso de elecciones, y anota qué relación marca cada conector.",
    "Busca un aviso en inglés en internet y anota una collocation y un conector.",
)

# ------------------------------------------------------------------ clase 5: prefijos im-, in-, il-
PF1 = "«Review (fictional): Yesterday the bus was impossible: it was late, and the driver was impolite. I was impatient, but I stayed calm. The schedule is incomplete, and the sign was illegible. It is illegal to park there, and it is illogical to wait there.» (impossible = imposible, impolite = descortés, impatient = impaciente, schedule = horario, incomplete = incompleto, sign = letrero, illegible = ilegible, illegal = ilegal, illogical = ilógico, park = estacionar)"
PF2 = "«Notice (fictional): This form is incomplete. The information is incorrect in two places. The name is invisible because the ink is light. Please write in a formal way, not an informal way.» (form = formulario, information = información, incorrect = incorrecto, ink = tinta, light = clara, formal = formal)"
PF3 = "«The machine is inactive today. The weather is imperfect for a trip, but the plan is not impossible. It is inexpensive, and the instructions are not illegible.» (inactive = inactivo, imperfect = imperfecto, inexpensive = barato, instructions = instrucciones)"

lesson(
    OA, 5, MAT_R,
    "Aprenderé a formar y entender palabras derivadas con los prefijos im-, in- e il- (impossible, incomplete, illegal), que dan el sentido contrario. Sirve para entender palabras nuevas y escribir sus formas correctas.",
    ["Sé que un prefijo cambia el sentido de una palabra.", "Conozco unhappy y disagree."],
    [
        "Un prefijo es una parte que se agrega al comienzo de una palabra para cambiar su significado. Los prefijos im-, in- e il- suelen significar no o lo contrario. Se usan con adjetivos: possible → impossible, polite → impolite, patient → impatient, complete → incomplete, correct → incorrect, formal → informal, legal → illegal, logical → illogical, legible → illegible.",
        "Hay una regla de ortografía. Se usa im- delante de las letras b, m y p: impossible, impolite, imperfect, immature. Se usa il- delante de l: illegal, illogical, illegible. En los demás casos se usa in-: incomplete, incorrect, inactive, informal, invisible, inexpensive. Para saber si una palabra tiene este prefijo, quítaselo: si queda otra palabra con sentido opuesto, es un prefijo. Impossible → possible, informal → formal. En cambio important, interesting y inside no son derivadas, porque al quitar im- o in- no queda una palabra con el sentido contrario.",
        "Usa estas formas para entender textos más rápido. Si lees illegible y sabes que legible es posible de leer, entiendes que illegible es lo que no se puede leer. En un texto, pregunta si el sentido negativo encaja con el contexto.",
    ],
    [("im- (b, m, p)", "no, lo contrario: impossible, impolite"), ("il- (l)", "no, lo contrario: illegal, illogical"), ("in- (otros)", "no, lo contrario: incomplete, informal"), ("prefix", "prefijo"), ("derived word", "palabra derivada"), ("opposite", "opuesto")],
    [
        ("Formar con el prefijo correcto", "Forma el contrario de polite, legal y complete.", ["Polite empieza con p: se usa im-.", "Legal empieza con l: se usa il-.", "Complete empieza con c: se usa in-."], "Impolite, illegal e incomplete"),
        ("Comprobar la derivación", PF2 + " ¿Qué significa informal en el texto y cuál es su palabra base?", ["Informal es el contrario de formal.", "Quito in- y queda formal.", "Informal significa no formal."], "Significa no formal; su palabra base es formal"),
    ],
    [
        ("Escribir inpossible o imlegal.", "Se confunde la regla: im- va antes de b, m, p; il- antes de l.", "Escribe impossible e illegal."),
        ("Pensar que important es el contrario de portant.", "Quitando im- no queda una palabra con el sentido contrario.", "Aplica la prueba de quitar el prefijo."),
    ],
    [
        mc("¿Cuál es el contrario de possible?", "impossible", ["inpossible", "ilpossible"], "Delante de p se usa im-."),
        mc("¿Cuál es el contrario de legal?", "illegal", ["imlegal", "inlegal"], "Delante de l se usa il-."),
        mc("¿Cuál es el contrario de complete?", "incomplete", ["imcomplete", "ilcomplete"], "Delante de c se usa in-."),
    ],
    [
        mr(PF1, "¿Qué significa impolite en el texto?", "Descortés", ["Muy cortés", "Rápido"], "El prefijo im- da el sentido contrario de polite."),
        mr(PF2, "¿Qué significa incorrect?", "Que no es correcto", ["Que es muy correcto", "Que está escrito con mucho cuidado"], "In- da el sentido contrario."),
        mr(PF3, "¿Qué significa inactive?", "Que no está activo", ["Que está activo", "Que está roto para siempre"], "In- da el sentido contrario de active."),
    ],
    [
        mc("Completa con la forma correcta: The letter is ____ (not legible). I cannot read it.", "illegible", ["imlegible", "inlegible"], "Delante de l se usa il-."),
        mc("Completa con la forma correcta: It is ____ (not possible) to finish today.", "impossible", ["inpossible", "illpossible"], "Delante de p se usa im-."),
        mc("Completa con la forma correcta: The form is ____ (not complete).", "incomplete", ["imcomplete", "ilcomplete"], "Delante de c se usa in-."),
    ],
    [
        mr(PF1, "Un lector dice que illogical es lo que tiene sentido. ¿Qué respuesta es más acertada?", "No: illogical es lo que no es lógico ni tiene sentido", ["Sí: illogical es lo que tiene mucho sentido", "Sí: significa muy rápido"], "Il- da el sentido contrario de logical."),
        mc("Un estudiante dice que important es el contrario de portant. ¿Qué respuesta es mejor?", "No: sin im- no queda una palabra con sentido contrario (portant)", ["Sí: portant es la palabra base y im- la vuelve contraria", "Sí: im- siempre cambia el sentido a lo contrario"], "No toda palabra que empieza por im- es derivada."),
    ],
    [
        mr(PF3, "¿Qué significa inexpensive?", "Barato, no caro", ["Muy caro y de lujo", "Gratis para todos"], "In- da el sentido contrario de expensive."),
        mr(PF3, "Un lector dice que the plan is not impossible significa que el plan es imposible. ¿Qué respuesta es mejor?", "No: no + impossible se cancelan, así que el plan es posible", ["Sí: significa que el plan es imposible de hacer", "Sí: significa muy difícil"], "No + impossible se cancelan."),
    ],
    [mr(PF1 + " " + PF2, "Clasifica estas palabras por prefijo: impossible, illegal, incomplete, impolite. ¿Qué agrupación es correcta?", "im-: impossible, impolite; il-: illegal; in-: incomplete", ["im-: illegal, impolite; il-: impossible; in-: incomplete", "im-: incomplete; il-: illegal; in-: impossible"], "La regla depende de la letra que sigue.")],
    [
        ("En Inglés de 2.º medio (OA 10, clase 5): ¿qué prefijo va antes de la letra l?", "il-", "Se usa en illegal e illogical."),
        ("En Inglés de 2.º medio (OA 10, clase 5): ¿qué prefijo va antes de p y m?", "im-", "Se usa en impossible e immature."),
        ("En Inglés de 2.º medio (OA 10, clase 5): ¿qué prueba muestra si una palabra es derivada?", "Quitar el prefijo y ver si queda una palabra con el sentido contrario", "Así se distingue de important."),
    ],
    task("Lee: «This is impossible!» said Leo. «The map is incomplete, the signs are illegible, and the instructions are incorrect.» (map = mapa, signs = letreros, instructions = instrucciones). Escribe la palabra base de cada palabra con prefijo, su significado, y una oración tuya con una palabra derivada nueva (por ejemplo impatient o informal).", "Impossible → possible; incomplete → complete; illegible → legible; incorrect → correct. Oración: My brother is impatient when he waits.", ["escribe la base de cuatro palabras", "explica su significado", "forma una oración con una palabra nueva"], ["hoja con cuatro bases y una oración"], ["usar el prefijo equivocado", "no explicar el significado"], "Pide que aplique la prueba de quitar el prefijo a important."),
    "Escribe diez adjetivos con im-, in- e il- y sus bases.",
    "Busca en un texto en inglés tres palabras con im-, in- o il- y comprueba si son derivadas.",
)
