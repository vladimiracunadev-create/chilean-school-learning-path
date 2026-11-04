"""Cuaderno del estudiante, 1.º medio Inglés (oficial), IN1M OA 10: propósito, estructura y lenguaje en textos no literarios.

Las clases del plan son genéricas; aquí se aplican a: tipos de texto y propósito (descripción, procedimiento, catálogo,
biografía, gráfico, noticia, diálogo); idea principal y detalles; contraste y problema-solución; palabras clave, collocations
y conectores (con dos fragmentos de un texto); y formación de palabras (ir-, dis-, -er, -ist, -ess, -ful) con una lectura
independiente. Todo texto va completo en el enunciado y los datos son «de ejemplo».
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN1M OA 10"
MAT = "Los textos, gráficos y tablas escritos en cada ejercicio, lápiz y una hoja para anotar."


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


# ------------------------------------------------------------------ clase 1: tipos de texto, propósito y estructura
W_STRIP = "«Welcome to Oakfield. It is a small town with green hills and a river. The streets are quiet, and people are friendly.» (town = pueblo, hills = cerros, river = río, friendly = amables)"
W_STEPS = "«How to plant a bean. You need: a cup, soil, a bean and water. Step 1: Fill the cup with soil. Step 2: Put the bean in the soil. Step 3: Water it every day.» (bean = poroto, cup = vaso, soil = tierra, fill = llena, put = pon, water = riega)"
TOWN = "Descripción: «My town is small and quiet. It has a main square with an old fountain, a fair on Saturdays and a library. Around the town there are green hills.» (main square = plaza, fountain = fuente, fair = feria, library = biblioteca)"
PAPER = "Procedimiento: «How to make a paper bookmark. You need: coloured paper, scissors and a ruler. Step 1: Cut a strip of paper. Step 2: Draw a pattern. Step 3: Decorate it with colours.» (bookmark = marcapáginas, scissors = tijeras, ruler = regla, strip = tira, pattern = diseño, decorate = decora)"
CATAL = "Catálogo: «Desk lamp, white, 12,990 pesos. Notebook set (three notebooks), 4,500 pesos. Pencil case, blue, 3,200 pesos.» (catalogue = catálogo, desk lamp = lámpara de escritorio, set = set, pencil case = estuche)"
BIO = "Biografía (datos de ejemplo): «María Gómez was born in a small village in 1990. She studied music and became a pianist. In 2015 she gave her first concert abroad. Today she teaches young musicians.» (biography = biografía, was born = nació, village = aldea, became = se convirtió en, abroad = en el extranjero, teaches = enseña)"
GRAPH = "Gráfico (datos de ejemplo): «Students who read books each month. Grade 7: 12. Grade 8: 15. Grade 9: 18. Grade 10: 20.» (graph = gráfico, grade = curso, each month = cada mes)"
NEWS = "Noticia: «Heavy rain flooded two streets in the south of the city on Tuesday. Firefighters pumped the water out. No one was hurt. The city says it will clean the drains this week.» (flooded = inundó, firefighters = bomberos, pumped out = sacaron con bomba, hurt = herido, drains = desagües)"
DIAL = "Diálogo: «Customer: Excuse me, how much is this jacket? Shop assistant: It's twenty-five thousand pesos. Customer: That is too expensive for me. Do you have a cheaper one?» (customer = cliente, shop assistant = vendedor, jacket = chaqueta, too expensive = demasiado caro, cheaper = más barato)"

lesson(
    OA, 1, MAT,
    "Aprenderé a identificar el propósito y la estructura de textos no literarios: descripciones, procedimientos, catálogos, biografías, gráficos, noticias y diálogos. Sirve para saber qué esperar y cómo buscar la información en cada uno.",
    ["Sé reconocer correos, avisos y páginas web.", "Conozco palabras como step, price y news."],
    [
        "Los textos no literarios (non-literary texts) informan, explican o instruyen, y no cuentan una historia de ficción. Una descripción (description) dice cómo es un lugar o una persona. Un procedimiento (procedure) explica pasos para hacer algo y tiene una lista de materiales (You need) y pasos numerados (Step 1). Un catálogo (catalogue) lista productos con precio. Una biografía (biography) cuenta la vida de una persona con años y hechos.",
        "Una noticia (news report) informa un hecho reciente: dice qué pasó, dónde y cuándo, y suele empezar con lo más importante. Un gráfico (graph) muestra datos con títulos y números por categoría. Un diálogo (dialogue) reproduce una conversación, con turnos y signos como Customer: o Shop assistant:. Cada tipo de texto tiene una estructura (structure) que te ayuda a ubicar la información.",
        "El propósito (purpose) es lo que el texto busca: describir, instruir, vender, informar, comparar datos o contar una vida. Para identificarlo, observa el título, los verbos (Cut, Draw, Decorate indican instrucciones) y las marcas de estructura. Una buena pregunta es: ¿qué tendría que hacer el lector después de leer? Si es seguir pasos, es un procedimiento; si es comprar, un catálogo; si es saber qué ocurrió, una noticia.",
    ],
    [("description", "descripción"), ("procedure", "procedimiento: pasos"), ("catalogue", "catálogo: lista de productos"), ("biography", "biografía"), ("graph", "gráfico"), ("news report", "noticia")],
    [
        ("Reconocer una descripción", W_STRIP + " ¿Qué tipo de texto es y cuál es su propósito?", ["Dice cómo es un lugar: pequeño, con cerros y río.", "No da pasos ni cuenta hechos recientes.", "Su propósito es describir."], "Es una descripción; su propósito es describir un pueblo"),
        ("Reconocer un procedimiento", W_STEPS + " ¿Qué pistas muestran que es un procedimiento?", ["Tiene You need con los materiales.", "Los pasos están numerados (Step 1, 2, 3).", "Los verbos son órdenes: Fill, Put, Water."], "You need, pasos numerados y verbos en orden"),
    ],
    [
        ("Pensar que un texto con años es siempre una biografía.", "Los años aparecen en muchos textos.", "Busca si el texto cuenta la vida de una persona."),
        ("Confundir un catálogo con un procedimiento porque ambos son listas.", "Se mira solo la forma de lista.", "Pregunta si la lista da pasos o productos con precio."),
    ],
    [
        (TOWN + " ¿Qué tipo de texto es? A) una descripción B) un procedimiento", "A) una descripción", "Dice cómo es el pueblo."),
        (PAPER + " ¿Qué tipo de texto es? A) un procedimiento B) un catálogo", "A) un procedimiento", "Tiene materiales y pasos numerados."),
        (CATAL + " ¿Qué tipo de texto es? A) un catálogo B) una biografía", "A) un catálogo", "Lista productos con precios."),
    ],
    [
        (BIO + " ¿Cuál es el propósito? A) contar la vida y la carrera de una persona B) enseñar a tocar piano", "A) contar la vida y la carrera de una persona", "Tiene años y hechos de su vida."),
        (GRAPH + " ¿Qué compara el gráfico? A) cuántos estudiantes leen libros por curso B) cuánto cuestan los libros", "A) cuántos estudiantes leen libros por curso", "Cada curso tiene un número de lectores."),
        (NEWS + " ¿Cuál es el propósito? A) informar un hecho reciente B) convencer de comprar algo", "A) informar un hecho reciente", "Cuenta qué pasó, dónde y cuándo."),
    ],
    [
        arith(CATAL + " Si compras la lámpara, el set de cuadernos y el estuche, ¿cuántos pesos pagas en total?", "12990+4500+3200", "Se suman los tres precios del catálogo.", " pesos"),
        (DIAL + " ¿Qué pide el cliente? A) una chaqueta más barata B) una chaqueta más grande", "A) una chaqueta más barata", "Dice Do you have a cheaper one?"),
        (PAPER + " ¿Qué materiales se necesitan? A) papel de color, tijeras y regla B) pegamento y pinceles", "A) papel de color, tijeras y regla", "Lo dice la línea You need."),
    ],
    [
        (BIO + " Un compañero dice que es una noticia. ¿Qué pista lo contradice? A) cuenta la vida de una persona desde su nacimiento B) tiene un titular", "A) cuenta la vida de una persona desde su nacimiento", "Una biografía sigue la vida; una noticia informa un hecho reciente."),
        (GRAPH + " Un compañero dice que es un procedimiento porque tiene números. ¿Qué respondes? A) no: no da pasos, muestra datos por curso B) sí: los números indican pasos", "A) no: no da pasos, muestra datos por curso", "Los números son cantidades, no pasos."),
    ],
    [
        (NEWS + " ¿Qué dato muestra que la noticia es reciente? A) on Tuesday y this week B) heavy rain", "A) on Tuesday y this week", "Son marcas de tiempo cercanas."),
        (GRAPH + " ¿Qué curso lee más? A) Grade 10 B) Grade 7", "A) Grade 10", "Grade 10 tiene 20, el número más alto."),
    ],
    [(DIAL + " ¿Dónde se escucha un texto así? A) en una tienda B) en una biblioteca", "A) en una tienda", "El cliente pregunta el precio de una chaqueta.")],
    [
        ("En Inglés de 1.º medio (OA 10, clase 1): ¿qué partes tiene un procedimiento?", "Una lista de materiales y pasos numerados", "Se reconoce por You need y Step 1.."),
        ("En Inglés de 1.º medio (OA 10, clase 1): ¿qué hace una biografía?", "Cuenta la vida de una persona con hechos y años", "Sigue el orden de su vida."),
        ("En Inglés de 1.º medio (OA 10, clase 1): ¿para qué sirve un gráfico?", "Para mostrar datos por categoría", "Permite comparar los números."),
    ],
    task("Lee: «Fruit salad. You need: apples, bananas and oranges. Step 1: Wash the fruit. Step 2: Ask an adult to cut it. Step 3: Mix it in a bowl.» (fruit salad = ensalada de frutas, wash = lava, mix = mezcla, bowl = bol). Escribe el tipo de texto, su propósito y dos pistas de estructura que lo muestran.", "Es un procedimiento. Su propósito es enseñar a preparar una ensalada de frutas. Pistas: la lista You need y los pasos Step 1, 2 y 3.", ["identifica el tipo de texto", "explica el propósito", "cita dos pistas de estructura"], ["hoja con tres respuestas", "revisión con el texto"], ["decir que es un catálogo por la lista", "no citar pistas"], "Reconoce lo acertado y pide mostrar con el dedo el You need y los pasos."),
    "Clasifica cinco textos de tu casa (receta, instructivo, boleta, correo) según estos tipos.",
    "Escribe un procedimiento de tres pasos sobre algo que sabes hacer, con You need y Step 1, 2 y 3.",
)

# ------------------------------------------------------------------ clase 2: idea principal, información específica y detalles
W_BIKE = "«Walking is a good way to travel in a city. It is free, it does not pollute and it keeps us active. However, walkers need to be careful with traffic.» (walking = caminar, travel = viajar, free = gratis, pollute = contaminar, active = activos, walkers = peatones, traffic = tráfico)"
GARDEN = "«Urban gardens are becoming popular. They use small spaces such as roofs and balconies. People grow herbs and vegetables for their families. Gardens also help neighbours meet. However, plants need regular care.» (urban = urbano, roofs = techos, balconies = balcones, grow = cultivan, herbs = hierbas, neighbours = vecinos, regular = regular, care = cuidado)"
SLEEP = "«Teenagers need enough sleep. At this age, the body is growing and the brain is learning many things. Many teenagers go to bed late because of phones and homework. Experts suggest a regular bedtime and no screens one hour before sleeping.» (enough = suficiente, brain = cerebro, bedtime = hora de acostarse, experts = expertos, suggest = sugieren, screens = pantallas)"
LANGS = "«Learning a new language has many benefits. It improves memory and helps you meet people from other cultures. Some people learn with apps, others with classes or with friends. The most important thing is to practise a little every day.» (benefits = beneficios, improves = mejora, memory = memoria, cultures = culturas, apps = aplicaciones, practise = practicar)"
MARKET = "«The Sunday book fair opens at ten in the morning. It has used books, comics and maps. Prices are lower than in bookshops, and many sellers accept cards. The fair closes at three.» (book fair = feria del libro, used books = libros usados, comics = cómics, maps = mapas, bookshops = librerías, prices = precios, lower = más bajos, sellers = vendedores, cards = tarjetas)"

lesson(
    OA, 2, MAT,
    "Aprenderé a identificar la idea principal de un texto no literario, la información específica y los detalles que la apoyan. Sirve para resumir y para responder preguntas con precisión.",
    ["Sé reconocer el tipo de texto y su propósito.", "Conozco la lectura de búsqueda (scanning)."],
    [
        "La idea principal (main idea) es lo más importante que dice el texto; todo lo demás la desarrolla. Suele estar en la primera o la última frase de un párrafo, llamada frase temática (topic sentence). Para encontrarla pregunta: ¿de qué habla casi todo el texto? y ¿qué quiere que entienda el autor? Una idea principal no es un dato aislado ni un ejemplo.",
        "Los detalles (details) apoyan la idea principal: ejemplos, datos, razones. La información específica (specific information) es el dato exacto que responde una pregunta: una hora, una cantidad, un nombre. Para encontrarla, usa scanning. Las palabras como for example, such as, also y because anuncian detalles. La palabra however suele anunciar una limitación o un contraste que también forma parte del mensaje.",
        "Para resumir, une la idea principal con los detalles más importantes en una o dos frases, sin copiar. Por ejemplo: Urban gardens are popular because they use small spaces and help neighbours meet, but they need care. Comprueba tu resumen: ¿incluye la idea principal?, ¿no agrega datos que el texto no dijo?",
    ],
    [("main idea", "idea principal"), ("topic sentence", "frase temática"), ("detail", "detalle"), ("specific information", "información específica"), ("such as / for example", "como / por ejemplo"), ("summary", "resumen")],
    [
        ("Encontrar la idea principal", W_BIKE + " ¿Cuál es la idea principal?", ["La primera frase dice el tema: caminar es una buena forma de viajar.", "Los demás datos la apoyan.", "La idea principal es que caminar es bueno para la ciudad."], "Caminar es una buena forma de viajar en la ciudad"),
        ("Distinguir un detalle", W_BIKE + " ¿Es It does not pollute la idea principal o un detalle?", ["Es una razón que apoya la primera frase.", "No resume todo el texto.", "Es un detalle."], "Es un detalle que apoya la idea principal"),
    ],
    [
        ("Elegir como idea principal un ejemplo o un dato.", "Se escoge lo más llamativo.", "Pregunta si la frase resume todo el texto."),
        ("Resumir copiando frases completas.", "Se confunde resumir con copiar.", "Une idea principal y detalles con tus palabras."),
    ],
    [
        (GARDEN + " ¿Cuál es la idea principal? A) los huertos urbanos son cada vez más populares B) los techos son pequeños", "A) los huertos urbanos son cada vez más populares", "Es la primera frase y resume el texto."),
        (SLEEP + " ¿Cuál es la idea principal? A) los adolescentes necesitan dormir lo suficiente B) los teléfonos son malos", "A) los adolescentes necesitan dormir lo suficiente", "Es la frase temática del primer renglón."),
        (LANGS + " ¿Cuál es la idea principal? A) aprender un idioma nuevo tiene muchos beneficios B) las aplicaciones son gratis", "A) aprender un idioma nuevo tiene muchos beneficios", "Resume el texto completo."),
    ],
    [
        (GARDEN + " ¿Qué se cultiva en los huertos urbanos? A) hierbas y verduras B) árboles frutales", "A) hierbas y verduras", "Dice People grow herbs and vegetables."),
        (SLEEP + " ¿Qué sugieren los expertos? A) una hora fija de acostarse y sin pantallas una hora antes B) dormir hasta tarde", "A) una hora fija de acostarse y sin pantallas una hora antes", "Dice a regular bedtime and no screens one hour before sleeping."),
        (MARKET + " ¿A qué hora abre y cierra la feria? A) abre a las diez y cierra a las tres B) abre a las tres y cierra a las diez", "A) abre a las diez y cierra a las tres", "Dice opens at ten and closes at three."),
    ],
    [
        (GARDEN + " ¿Qué ventaja social se menciona? A) ayudan a que los vecinos se conozcan B) bajan los precios de las verduras", "A) ayudan a que los vecinos se conozcan", "Dice Gardens also help neighbours meet."),
        (LANGS + " ¿Cuál es el consejo más importante? A) practicar un poco cada día B) estudiar solo en vacaciones", "A) practicar un poco cada día", "Dice The most important thing is to practise a little every day."),
        (MARKET + " ¿Qué ventaja de precio menciona? A) que son más bajos que en librerías B) que son iguales", "A) que son más bajos que en librerías", "Dice lower than in bookshops."),
    ],
    [
        (GARDEN + " Un compañero dice que el texto solo habla de las ventajas. ¿Qué respondes? A) no: However plants need regular care muestra una dificultad B) sí: todo es positivo", "A) no: However plants need regular care muestra una dificultad", "However anuncia una limitación."),
        (SLEEP + " ¿Qué frase es un detalle y no la idea principal? A) Many teenagers go to bed late because of phones and homework B) Teenagers need enough sleep", "A) Many teenagers go to bed late because of phones and homework", "Explica una causa, no el tema general."),
    ],
    [
        (LANGS + " ¿Cuál es el mejor resumen? A) Aprender un idioma mejora la memoria y permite conocer otras culturas; lo importante es practicar cada día B) Los idiomas se aprenden solo con aplicaciones", "A) Aprender un idioma mejora la memoria y permite conocer otras culturas; lo importante es practicar cada día", "Une la idea principal con los detalles clave."),
        (MARKET + " ¿Qué dato no aparece en el texto? A) el nombre del organizador de la feria B) la hora de cierre", "A) el nombre del organizador de la feria", "El texto no lo menciona."),
    ],
    [(SLEEP + " Quieres dormir mejor. ¿Qué dos consejos aplican según el texto? A) hora regular y sin pantallas una hora antes B) más tareas y más café", "A) hora regular y sin pantallas una hora antes", "Son las sugerencias del texto.")],
    [
        ("En Inglés de 1.º medio (OA 10, clase 2): ¿qué es la idea principal?", "Lo más importante que dice el texto", "Todo lo demás la desarrolla."),
        ("En Inglés de 1.º medio (OA 10, clase 2): ¿qué palabras anuncian ejemplos?", "For example y such as", "Anuncian los detalles."),
        ("En Inglés de 1.º medio (OA 10, clase 2): ¿qué debe tener un resumen?", "La idea principal y los detalles clave, con tus palabras", "No se copia."),
    ],
    task("Lee: «Reading before bed can help you relax. Soft light and a calm story make the body ready for sleep. However, a bright screen can keep you awake. For example, a phone can make it harder to fall asleep.» (relax = relajarte, soft light = luz suave, calm = tranquilo, bright = brillante, awake = despierto, harder = más difícil, fall asleep = quedarte dormido). Escribe la idea principal, dos detalles y un resumen de una frase.", "Idea principal: leer antes de dormir ayuda a relajarse. Detalles: la luz suave y un cuento calmo preparan el cuerpo; una pantalla brillante mantiene despierto. Resumen: leer antes de dormir relaja, pero las pantallas dificultan dormir.", ["identifica la idea principal", "anota dos detalles del texto", "escribe un resumen sin copiar"], ["hoja con tres respuestas", "revisión con el texto"], ["tomar un ejemplo como idea principal", "resumen que copia el texto"], "Reconoce lo logrado y pide comprobar el resumen con la pregunta: ¿incluye la idea principal?"),
    "Elige un texto breve de esta clase y escribe en español su idea principal y dos detalles.",
    "Busca la frase temática en un párrafo de un libro de tu casa y subráyala.",
)

# ------------------------------------------------------------------ clase 3: contraste y problema-solución
W_CITY = "«Living in a big city has advantages and disadvantages. On the one hand, there are many jobs and activities. On the other hand, the traffic is heavy and the air is not clean.» (advantages = ventajas, disadvantages = desventajas, jobs = trabajos, activities = actividades, traffic = tráfico, heavy = pesado, air = aire)"
NOISE = "«The school library has a problem: it is too noisy at lunch time. Students cannot study, so many go home. The librarian made a new rule: lunch time is quiet time, and group work is in the room next door.» (library = biblioteca, noisy = ruidosa, librarian = bibliotecario, rule = regla, quiet = silencio, group work = trabajo en grupo, next door = al lado)"
ONLINE = "«Online shopping is convenient because you can buy at any time. However, you cannot touch the product before buying it. Although some shops offer free returns, the process can take several days.» (convenient = cómodo, product = producto, free returns = devoluciones gratis, process = proceso, several = varios)"
WASTE = "«Our city produces a lot of waste. Many bags end up in landfills. The council started a programme: families separate paper, plastic and glass, and special trucks collect them. Since then, the amount of waste in landfills has fallen.» (waste = basura, landfills = rellenos sanitarios, council = municipalidad, programme = programa, separate = separan, collect = recogen, fallen = bajado)"
BIKES = "«Many students arrive late because the bus is slow. The school asked the council to create a bus lane. Meanwhile, a group of students organised a walking group, so they can arrive together and on time.» (arrive late = llegan tarde, bus lane = pista exclusiva, meanwhile = mientras tanto, organised = organizaron, together = juntos, on time = a tiempo)"
TWINS = "«Ana and Eli are twins, but they are very different. Ana likes to plan everything, while Eli prefers to improvise. Both of them love music, however, and they play in the same band.» (twins = gemelos, plan = planificar, improvise = improvisar, band = banda)"

lesson(
    OA, 3, MAT,
    "Aprenderé a reconocer relaciones de contraste y de problema-solución entre las ideas de un texto no literario. Sirve para entender qué se compara y qué dificultad se resuelve.",
    ["Sé reconocer la idea principal y los detalles.", "Conozco conectores como but, although y so."],
    [
        "El contraste (contrast) opone dos ideas. Las marcas son but, however, although, while, on the one hand... on the other hand, instead of. Por ejemplo: On the one hand, there are many jobs. On the other hand, the traffic is heavy. Aquí se presentan ventajas (advantages) y desventajas (disadvantages) de un mismo tema. Mira ambos lados antes de decidir qué piensa el autor.",
        "La relación problema-solución (problem-solution) tiene cuatro partes: la situación, el problema, la solución y el resultado. El problema se marca con palabras como problem, too noisy, cannot. La solución se introduce con made a rule, started a programme, decided to o organised. El resultado puede aparecer con since then, so o as a result: Since then, the amount of waste has fallen.",
        "Al leer, subraya la marca de cada relación y escribe en el margen qué dos ideas se oponen o cuáles son el problema y la solución. Pregunta si la solución ataca la causa del problema. Por ejemplo, si el problema es el ruido en la biblioteca, una regla de silencio al almuerzo lo resuelve. Si no hay resultado en el texto, dilo: The text does not say.",
    ],
    [("on the one hand / on the other hand", "por un lado / por otro lado"), ("advantage / disadvantage", "ventaja / desventaja"), ("problem / solution", "problema / solución"), ("as a result", "como resultado"), ("since then", "desde entonces"), ("however", "sin embargo")],
    [
        ("Reconocer un contraste", W_CITY + " ¿Qué ventaja y qué desventaja menciona?", ["On the one hand introduce la ventaja: muchos trabajos y actividades.", "On the other hand introduce la desventaja: tráfico y aire poco limpio.", "Los dos lados se oponen."], "Ventaja: muchos trabajos y actividades; desventaja: tráfico y aire poco limpio"),
        ("Reconocer problema y solución", NOISE + " ¿Cuál es el problema y cuál la solución?", ["El problema: la biblioteca es muy ruidosa al almuerzo.", "La solución: una regla de silencio y trabajo en grupo en la sala vecina.", "La solución atiende la causa, el ruido."], "Problema: ruido; solución: una regla de silencio y trabajo en grupo al lado"),
    ],
    [
        ("Leer solo uno de los lados de un contraste.", "Se queda con la primera idea.", "Busca la marca on the other hand o however y lee ambos lados."),
        ("Aceptar cualquier medida como solución.", "No se comprueba si ataca la causa.", "Pregunta si la solución responde al problema."),
    ],
    [
        (ONLINE + " ¿Qué ventaja menciona? A) puedes comprar a cualquier hora B) puedes tocar el producto", "A) puedes comprar a cualquier hora", "Dice because you can buy at any time."),
        (ONLINE + " ¿Qué desventaja menciona? A) no puedes tocar el producto antes de comprarlo B) hay que ir a una tienda", "A) no puedes tocar el producto antes de comprarlo", "Dice However, you cannot touch the product."),
        (WASTE + " ¿Cuál es el problema? A) la ciudad produce mucha basura B) faltan camiones", "A) la ciudad produce mucha basura", "Dice produces a lot of waste."),
    ],
    [
        (WASTE + " ¿Qué solución adoptó la municipalidad? A) las familias separan papel, plástico y vidrio, y camiones especiales los recogen B) cerrar el relleno sanitario", "A) las familias separan papel, plástico y vidrio, y camiones especiales los recogen", "Es el programa que cuenta el texto."),
        (WASTE + " ¿Cuál fue el resultado? A) bajó la cantidad de basura en los rellenos B) aumentó la basura", "A) bajó la cantidad de basura en los rellenos", "Dice has fallen."),
        (TWINS + " ¿Qué palabra señala la diferencia entre Ana y Eli? A) while B) both", "A) while", "While compara a los dos: planifica frente a improvisa."),
    ],
    [
        (TWINS + " ¿Qué tienen en común? A) les encanta la música B) planifican todo", "A) les encanta la música", "Dice Both of them love music, however, y tocan en la misma banda."),
        (BIKES + " ¿Qué problema se menciona? A) los estudiantes llegan tarde porque el bus es lento B) faltan bicicletas", "A) los estudiantes llegan tarde porque el bus es lento", "Dice arrive late because the bus is slow."),
        (BIKES + " ¿Qué solución inmediata tomaron los estudiantes? A) formar un grupo para ir caminando juntos B) esperar la pista exclusiva", "A) formar un grupo para ir caminando juntos", "La pista exclusiva es una petición a futuro."),
    ],
    [
        (W_CITY + " Un compañero dice que la ciudad solo tiene desventajas. ¿Qué dato lo contradice? A) hay muchos trabajos y actividades B) el tráfico es pesado", "A) hay muchos trabajos y actividades", "Es la ventaja del primer lado del contraste."),
        (NOISE + " Un compañero dice que la solución no sirve porque hay otro problema. ¿Cuál es el que atiende la regla? A) el ruido que impide estudiar B) la falta de libros", "A) el ruido que impide estudiar", "La regla de silencio responde al ruido."),
    ],
    [
        (BIKES + " ¿Qué marca introduce lo que pasa mientras tanto? A) Meanwhile B) Because", "A) Meanwhile", "Meanwhile significa mientras tanto."),
        (ONLINE + " ¿Qué muestra Although some shops offer free returns? A) que hay una ventaja, pero el proceso puede demorar B) que las devoluciones son inmediatas", "A) que hay una ventaja, pero el proceso puede demorar", "Although opone la ventaja con la demora."),
    ],
    [("Un texto dice: «Our school has a problem: the patio floods when it rains. The caretaker cleaned the drains, and now the water goes away.» (floods = se inunda, caretaker = auxiliar, cleaned = limpió, drains = desagües). ¿Cuál es la solución? A) limpiar los desagües B) cerrar el patio", "A) limpiar los desagües", "Dice The caretaker cleaned the drains.")],
    [
        ("En Inglés de 1.º medio (OA 10, clase 3): ¿qué marcan on the one hand y on the other hand?", "Dos lados opuestos de un tema", "Presentan ventajas y desventajas."),
        ("En Inglés de 1.º medio (OA 10, clase 3): ¿cuáles son las partes de un texto de problema-solución?", "Situación, problema, solución y resultado", "Ordenan la información."),
        ("En Inglés de 1.º medio (OA 10, clase 3): ¿qué significa since then?", "Desde entonces", "Introduce un resultado."),
    ],
    task("Lee: «Many students use phones in class. On the one hand, phones help them look up words. On the other hand, they can distract students. The teacher made a rule: phones stay in the bag, except for dictionary work. Since then, students pay more attention.» (look up = buscar, distract = distraer, rule = regla, except for = excepto para, pay attention = prestar atención). Escribe la ventaja y la desventaja, el problema, la solución y el resultado.", "Ventaja: ayudan a buscar palabras. Desventaja: pueden distraer. Problema: el uso del teléfono en clase distrae. Solución: los teléfonos quedan en la mochila, excepto para trabajo con diccionario. Resultado: prestan más atención.", ["identifica ventaja y desventaja", "identifica problema, solución y resultado", "usa las marcas del texto"], ["hoja con cinco respuestas", "revisión con el texto"], ["confundir la solución con el problema", "omitir el resultado"], "Reconoce las relaciones ubicadas y pide subrayar la marca de cada una."),
    "Escribe una tabla con las ventajas y desventajas de caminar al colegio.",
    "Describe en cuatro frases un problema de tu curso, su solución y el resultado esperado.",
)

# ------------------------------------------------------------------ clase 4: palabras clave, collocations y conectores (dos fragmentos)
FEST_A = "Fragmento A: «The festival was a big success. Both children and adults enjoyed the music. Although it rained in the morning, the organisers did not cancel the event.» (festival = festival, success = éxito, organisers = organizadores, cancel = cancelar, event = evento)"
FEST_B = "Fragmento B: «Later the sun came out, and thousands of people danced in the park. Last, the band played a famous song, and everyone sang together.» (sun came out = salió el sol, danced = bailaron, band = banda, sang = cantaron)"
TRAFF = "Fragmento A: «Heavy traffic is a common problem in big cities. Many people take part in a campaign to use public transport.» Fragmento B: «The campaign makes progress every year. More people choose the bus so that the streets are less crowded.» (heavy traffic = tráfico pesado, take part in = participar en, campaign = campaña, make progress = avanzar, so that = para que, crowded = llenas)"
RESEARCH = "Fragmento A: «Before the school project, we did research on the topic. First, we made a list of questions.» Fragmento B: «Then we had a look at three websites. Last, we made a decision: we would present a poster.» (research = investigación, topic = tema, have a look = echar un vistazo, make a decision = tomar una decisión, poster = afiche)"
COFFEE = "Fragmento A: «Strong coffee is popular in many countries. Some people eat fast food and drink coffee for breakfast.» Fragmento B: «However, experts say that a healthy breakfast helps you stay alert at school or work.» (strong coffee = café cargado, popular = popular, fast food = comida rápida, breakfast = desayuno, alert = atento)"

lesson(
    OA, 4, MAT,
    "Aprenderé a reconocer palabras y frases clave, combinaciones frecuentes de palabras (collocations) y conectores como later, last, so that, although y both en textos no literarios, juntando fragmentos de un mismo texto. Sirve para entender el hilo del texto y completar la información.",
    ["Sé identificar idea principal y relaciones de contraste.", "Conozco collocations como make a decision."],
    [
        "Las palabras clave (key words) son las que sostienen el sentido: sustantivos, verbos importantes y datos. Las collocations son combinaciones frecuentes: heavy traffic (tráfico pesado), strong coffee (café cargado), fast food, take part in, do research, make progress, have a look, make a decision. Aprenderlas completas ayuda a comprender más rápido y a no traducir palabra por palabra.",
        "Los conectores guían el texto. Later (más tarde) y last (por último) ordenan hechos. So that introduce el propósito: para que. Although introduce un contraste: aunque. Both... and... reúne dos elementos: ambos. En esta clase leerás textos partidos en dos fragmentos: A y B. Cada fragmento tiene una parte de la información; juntos forman el sentido completo.",
        "Para combinar fragmentos, ubica en cada uno qué parte del texto es y qué conectores lo unen. Por ejemplo, Later en el fragmento B indica que continúa el relato del fragmento A. Anota qué dice cada fragmento y verifica que no se contradigan. Si una pregunta depende de ambos fragmentos, busca el dato en cada uno y combínalos.",
    ],
    [("key words", "palabras clave"), ("collocation", "combinación frecuente"), ("take part in", "participar en"), ("make progress", "avanzar, progresar"), ("so that", "para que"), ("both ... and", "ambos ... y")],
    [
        ("Reconocer collocations", "En «Heavy traffic is a common problem», ¿qué collocation aparece y qué significa?", ["Busco dos palabras que van juntas.", "Heavy traffic es una combinación frecuente.", "Significa tráfico pesado o intenso."], "Heavy traffic: tráfico pesado"),
        ("Unir dos fragmentos", FEST_A + " " + FEST_B + " ¿Qué ocurrió a pesar de la lluvia de la mañana?", ["En A dice que llovió en la mañana y no se canceló.", "En B dice que salió el sol y mucha gente bailó.", "A pesar de la lluvia, el festival siguió y la gente bailó."], "El festival siguió y miles de personas bailaron"),
    ],
    [
        ("Traducir una collocation palabra por palabra.", "Se piensa que cada palabra tiene un equivalente único.", "Aprende la combinación completa: heavy traffic."),
        ("Responder con un solo fragmento cuando se necesitan ambos.", "Se ve solo la parte que se leyó primero.", "Busca el dato en A y en B antes de responder."),
    ],
    [
        ("¿Qué collocation significa «tomar una decisión»? A) make a decision B) do a decision", "A) make a decision", "Decision se usa con make."),
        ("¿Qué collocation significa «participar en»? A) take part in B) make part in", "A) take part in", "Take part in es participar en."),
        ("¿Qué significa strong coffee? A) café cargado B) café rápido", "A) café cargado", "Strong con coffee es cargado."),
    ],
    [
        (FEST_A + " ¿Qué significa Both children and adults enjoyed the music? A) disfrutaron los niños y también los adultos B) solo los adultos", "A) disfrutaron los niños y también los adultos", "Both reúne a los dos grupos."),
        (FEST_B + " ¿Qué conector marca la última acción? A) Last B) Later", "A) Last", "Last cierra la secuencia."),
        (TRAFF + " ¿Qué expresa so that? A) el propósito de elegir el bus B) un contraste", "A) el propósito de elegir el bus", "So that dice para qué se elige el bus."),
    ],
    [
        (FEST_A + " " + FEST_B + " ¿Qué ocurrió primero y qué por último? A) llovió por la mañana; por último la banda tocó una canción famosa B) la banda tocó primero y llovió por último", "A) llovió por la mañana; por último la banda tocó una canción famosa", "Later y Last ordenan los hechos."),
        (TRAFF + " ¿Qué avanza cada año? A) la campaña B) el tráfico", "A) la campaña", "Dice makes progress every year."),
        (RESEARCH + " ¿Qué hicieron primero? A) una lista de preguntas B) un afiche", "A) una lista de preguntas", "Dice First, we made a list of questions."),
    ],
    [
        (RESEARCH + " ¿Qué decidieron al final? A) presentar un afiche B) escribir un libro", "A) presentar un afiche", "Dice we would present a poster."),
        (COFFEE + " ¿Qué marca el fragmento B con However? A) una opinión de expertos que contrasta con la costumbre B) una receta", "A) una opinión de expertos que contrasta con la costumbre", "However opone el desayuno saludable con comer comida rápida."),
    ],
    [
        (COFFEE + " ¿Qué recomiendan los expertos? A) un desayuno saludable para mantenerse atento B) café y comida rápida", "A) un desayuno saludable para mantenerse atento", "Lo dice el fragmento B."),
        (TRAFF + " ¿Qué problema se menciona en A y qué propone B? A) tráfico pesado; elegir el bus B) tráfico pesado; no salir de casa", "A) tráfico pesado; elegir el bus", "Cada fragmento aporta una parte."),
    ],
    [(RESEARCH + " ¿Qué collocations aparecen? A) do research, have a look y make a decision B) take a break y pay attention", "A) do research, have a look y make a decision", "Son las combinaciones usadas en el texto.")],
    [
        ("En Inglés de 1.º medio (OA 10, clase 4): ¿qué es una collocation?", "Una combinación frecuente de palabras, como heavy traffic", "Se aprende completa."),
        ("En Inglés de 1.º medio (OA 10, clase 4): ¿qué indica so that?", "Un propósito: para que", "Dice para qué se hace algo."),
        ("En Inglés de 1.º medio (OA 10, clase 4): ¿qué haces si la información está en dos fragmentos?", "Busco el dato en cada uno y los combino", "Así la respuesta es completa."),
    ],
    task("Lee dos fragmentos. A: «Both Luis and Marta joined the school radio. They record a programme every Friday.» B: «Although they were nervous at first, they now make progress every week. Last Friday they interviewed the principal.» (joined = se unieron, record = graban, programme = programa, nervous = nerviosos, interviewed = entrevistaron, principal = director). Escribe en español un resumen con los datos de ambos fragmentos y subraya dos collocations o conectores.", "Luis y Marta se unieron a la radio del colegio y graban un programa cada viernes. Aunque al principio estaban nerviosos, ahora avanzan cada semana. El viernes pasado entrevistaron al director. Conectores: both, although; collocation: make progress.", ["incluye datos de A y de B", "usa los conectores con sentido", "identifica una collocation"], ["hoja con el resumen", "subrayado de dos expresiones"], ["omitir los datos de un fragmento", "traducir make progress palabra por palabra"], "Reconoce los datos reunidos y pide indicar de qué fragmento viene cada uno."),
    "Haz una tarjeta con cada collocation de esta clase y una frase de ejemplo.",
    "Corta un texto corto en dos partes y pide a alguien que lo reconstruya a partir de los conectores.",
)

# ------------------------------------------------------------------ clase 5: formación de palabras y lectura independiente
lesson(
    OA, 5, MAT,
    "Aprenderé a entender palabras derivadas con los prefijos ir- y dis- y los sufijos -er, -ist, -ess y -ful, y a usarlas para leer un texto por mi cuenta. Sirve para descubrir el significado de palabras nuevas a partir de sus partes.",
    ["Sé identificar el tipo de texto y la idea principal.", "Conozco palabras como teacher, helpful y artist."],
    [
        "Muchas palabras se forman agregando prefijos al inicio o sufijos al final. Los prefijos ir- y dis- dan un significado opuesto o negativo. Ir- aparece antes de r: regular se vuelve irregular y responsible se vuelve irresponsible. Dis- aparece antes de muchas palabras: like se vuelve dislike, agree se vuelve disagree, appear se vuelve disappear y honest se vuelve dishonest.",
        "Los sufijos -er, -ist y -ess forman nombres de ocupaciones o personas. -er indica quien hace algo: teach – teacher, sing – singer, farm – farmer. -ist se usa en profesiones: art – artist, piano – pianist, science – scientist, tour – tourist. -ess indica una persona de sexo femenino: act – actress, wait – waitress. Hoy muchas personas prefieren actor o waiter para cualquier género. -ful forma adjetivos y significa lleno de: help – helpful, care – careful, colour – colourful, beauty – beautiful.",
        "Para leer palabras nuevas, separa la raíz del prefijo o sufijo. Si ves irresponsible, quita ir- y queda responsible: no es responsable. Si ves a colourful poster, entiende un afiche lleno de color. Comprueba el resultado con el contexto de la frase. No todas las terminaciones forman palabras: no se dice Careful-er; las combinaciones hay que aprenderlas.",
    ],
    [("ir-, dis-", "prefijos de significado opuesto"), ("-er, -ist, -ess", "sufijos de personas u ocupaciones"), ("-ful", "lleno de"), ("root", "raíz: la palabra base"), ("irregular", "no regular"), ("dishonest", "no honesto")],
    [
        ("Formar palabras con prefijos", "¿Cuál es el opuesto de responsible con el prefijo ir-, y de agree con dis-?", ["Responsible comienza con r, por eso lleva ir-.", "Agree se vuelve disagree.", "Responden irresponsible y disagree."], "irresponsible; disagree"),
        ("Formar ocupaciones", "¿Cómo se llaman la persona que enseña, la que toca el piano y la que trabaja como actriz en inglés?", ["Teach + -er da teacher.", "Piano + -ist da pianist.", "Act + -ess da actress."], "teacher; pianist; actress"),
    ],
    [
        ("Usar dis- antes de una palabra que comienza con r.", "Se aplica un solo prefijo para todo.", "Antes de r se usa ir-: irregular, irresponsible."),
        ("Agregar -ful a cualquier palabra sin comprobar que existe.", "Se supone que siempre funciona.", "Aprende las combinaciones: helpful, careful, colourful."),
    ],
    [
        ("¿Qué palabra significa «no regular»? A) irregular B) disregular", "A) irregular", "Antes de r se usa ir-."),
        ("¿Qué palabra significa «no estar de acuerdo»? A) disagree B) irgree", "A) disagree", "Dis- forma el opuesto de agree."),
        ("¿Qué palabra significa «lleno de color»? A) colourful B) colourous", "A) colourful", "-ful significa lleno de."),
    ],
    [
        ("¿Qué significa singer? A) persona que canta B) canción", "A) persona que canta", "-er indica quien hace la acción."),
        ("¿Qué significa tourist? A) persona que viaja por turismo B) guía de turismo", "A) persona que viaja por turismo", "-ist forma una persona vinculada a la palabra base."),
        ("¿Qué significa careful? A) lleno de cuidado B) sin cuidado", "A) lleno de cuidado", "Care + -ful es cuidadoso."),
    ],
    [
        ("Forma el opuesto de like con dis-.", "dislike", "Dis- + like forma dislike."),
        ("Forma el opuesto de appear con dis-.", "disappear", "Dis- + appear forma disappear."),
        ("Forma una palabra con -ful a partir de help.", "helpful", "Help + -ful es útil o servicial."),
    ],
    [
        ("Completa: «He did not tell the truth. He was ___.» A) dishonest B) irhonest", "A) dishonest", "Dishonest se forma con dis-; ir- se usa solo antes de r."),
        ("¿Qué frase es correcta? A) She is an actress. B) She is an acter.", "A) She is an actress.", "La forma es actress."),
    ],
    [
        ("Un afiche dice: «Join our colourful festival!» ¿Qué tipo de festival promete? A) uno lleno de color B) uno sin color", "A) uno lleno de color", "Colourful significa lleno de color."),
        ("En «The tourist was careful with the map», ¿qué palabras tienen sufijo? A) tourist y careful B) map y with", "A) tourist y careful", "Tourist lleva -ist y careful lleva -ful."),
    ],
    [("Lees en un aviso: «Dear tourists, the history centre has a helpful guide. Please be careful with the old pieces.» (history centre = centro de historia, tourists = turistas, helpful = servicial, careful = cuidadoso, pieces = piezas). ¿Qué piden y qué ofrecen? A) piden cuidado y ofrecen un guía servicial B) piden silencio y ofrecen comida", "A) piden cuidado y ofrecen un guía servicial", "Careful y helpful se explican por -ful.")],
    [
        ("En Inglés de 1.º medio (OA 10, clase 5): ¿qué significa el prefijo dis-?", "Un significado opuesto o negativo", "Por ejemplo, dislike."),
        ("En Inglés de 1.º medio (OA 10, clase 5): ¿cuándo se usa ir-?", "Antes de palabras que empiezan con r, como irregular", "Forma un opuesto."),
        ("En Inglés de 1.º medio (OA 10, clase 5): ¿qué significa -ful?", "Lleno de", "Forma adjetivos como helpful."),
    ],
    task("Lee: «Last summer, a young scientist visited our school. She was a very helpful speaker and an excellent teacher. She explained why it is irresponsible to waste water. Students disagreed on some details, but everybody enjoyed the colourful presentation.» (scientist = científica, speaker = expositora, waste = desperdiciar, details = detalles, enjoyed = disfrutaron). Escribe cuatro palabras derivadas del texto, su raíz y su significado en español.", "scientist (science: persona que se dedica a la ciencia); helpful (help: servicial); irresponsible (responsible: no responsable); colourful (colour: lleno de color). También: teacher (teach), disagreed (agree).", ["identifica cuatro palabras derivadas", "separa la raíz del prefijo o sufijo", "explica el significado"], ["hoja con cuatro palabras", "revisión con el texto"], ["decir que speaker lleva -er sin explicar", "confundir ir- con dis-"], "Reconoce los casos bien analizados y repasa con ella cuándo se usa ir- y dis-."),
    "Haz una tabla con diez palabras derivadas: raíz, prefijo o sufijo y significado.",
    "Busca en un texto cualquiera tres palabras con -er, -ist o -ful y explica su raíz.",
)
