"""Cuaderno del estudiante, 2.º medio Inglés (oficial): IN2M OA 11, comprensión de textos literarios.

Textos originales, breves y con glosario en español dentro del enunciado; todo término usado en un ejercicio se
enseña antes en la explicación o el vocabulario de esa clase. Sin audio externo.
Los títulos de clase del plan son genéricos (propósito, evidencia, relaciones, ensayo, producción): aquí se aplican a
género y tema, personajes y entorno, trama y conflicto, expresiones idiomáticas y vocabulario temático con respuesta.
Este módulo define también los ayudantes `lesson` y `mc` que importan los demás módulos in_m2_b*.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "IN2M OA 11"


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def mc(stem, right, wrongs, why):
    """Pregunta de alternativas: la correcta se escribe primera; el registro balancea la posición."""
    options = [o.strip().rstrip(".?!,;") for o in [right] + list(wrongs)]
    letters = "ABC"
    q = stem + " " + " ".join(f"{letters[i]}) {o}" for i, o in enumerate(options))
    return ex(q, f"A) {right}", why)


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


MAT = "Los textos escritos en cada ejercicio, lápiz y una hoja para anotar."

# ============================================================ clase 1: géneros literarios y tema
SONG = "«Verse: The bus is late, the rain is cold, / but I have you, and that is gold. Chorus: We walk, we walk, we do not mind, / the road is long, but we are kind.»"
GSONG = "(late = atrasado; rain = lluvia; gold = oro; walk = caminamos; mind = importar; road = camino; kind = amables)"
PLAYA = "«Scene 1. A kitchen at night. (Ana enters, holding a phone. She looks nervous.) ANA: (whispering) I broke the screen. (Her brother Luis looks up from his book.) LUIS: Tell Dad before he sees it.»"
GPLAYA = "(scene = escena; kitchen = cocina; holding = sosteniendo; nervous = nerviosa; whispering = susurrando; broke = rompí; screen = pantalla; looks up = levanta la vista)"
TREE = "«The old tree gives its shade to all, / the child, the bird, the tired man. / It never asks, it answers every call, / and gives as much as a tree can.»"
GTREE = "(tree = árbol; shade = sombra; tired = cansado; asks = pide; answers = responde; call = llamado)"
MYTH = "«They say the first rain fell because the Sun and the Moon argued. The Sun was angry that the Moon had the night. The Moon cried, and her tears became rain. Since then, they take turns, and rain reminds people that anger can end in tears.»"
GMYTH = "(argued = discutieron; angry = enojado; cried = lloró; tears = lágrimas; take turns = se turnan; reminds = recuerda; anger = enojo)"
WALLET = "«Eli found a wallet with money in the school yard. Nobody was looking. He thought about the new shoes he wanted, but he gave the wallet to the teacher. Later, the owner, a first-year student, thanked him with a big smile. Eli felt light, as if he had put down a heavy bag.»"
GWALLET = "(wallet = billetera; yard = patio; nobody = nadie; thought about = pensó en; owner = dueño; thanked = agradeció; light = liviano; heavy bag = bolso pesado)"
SKATE = "«Panel 1: A girl throws a ball at a hoop and misses. Girl: Oh no! Panel 2: She practices every afternoon. Panel 3: A month later, the ball goes in. Girl: I did it!»"
GSKATE = "(throws = lanza; hoop = aro; misses = falla; practices = practica; goes in = entra)"
GYM = "«Scene 2. The school gym. (Mia stands alone with a trophy in her hand. Her coach enters.) COACH: You won! Why are you not smiling? MIA: (looking down) My team helped me, but they are not here.»"
GGYM = "(gym = gimnasio; alone = sola; trophy = trofeo; coach = entrenador; won = ganaste; looking down = mirando hacia abajo; helped = ayudó)"
HOME = "«Verse 1: Five o'clock, the day is done, / the sky is orange, the streets are loud. Chorus: Home, home, take me home, / where the lights are warm. Verse 2: Six o'clock, the stars come out. Chorus: Home, home, take me home, / where the lights are warm.»"
GHOME = "(done = terminado; sky = cielo; loud = ruidosas; lights = luces; warm = cálidas; stars = estrellas; come out = salen)"
WIND = "«Hector told the truth about the broken window, even though he could have stayed silent. His dad was angry for a minute and then proud.»"
WIND2 = "«I could say it was not me, / the window broken, plain to see. / But truth is light, though hard to say, / and silence weighs more every day.»"
GWIND = "(window = ventana; truth = verdad; silent = callado; proud = orgulloso; plain to see = a la vista; light = luz; weighs = pesa; silence = silencio)"
STAGE = "«Act 1. (The stage is dark.) NARRATOR: Once there was a village without a river.»"
GSTAGE = "(act = acto; stage = escenario; dark = oscuro; narrator = narrador; village = aldea; river = río)"

lesson(
    OA, 1, MAT,
    "Aprenderé a distinguir canciones, poemas, tiras cómicas, cuentos, obras de teatro y mitos o leyendas, y a formular su tema con dos pistas del texto. Sirve para saber qué buscar al leer y para explicar con evidencia de qué trata realmente un texto.",
    ["Sé que un texto literario tiene personajes, entorno y trama.", "En 1.º medio distinguí tema de asunto en poemas y cuentos."],
    [
        "Los textos literarios se reconocen por su forma. Una canción (song) se organiza en estrofas (verses) y un estribillo (chorus), que es la parte que se repite. Un poema (poem) usa versos y a veces rima. Una tira cómica (comic strip) usa viñetas (panels). Una obra de teatro (play) se divide en actos (acts) y escenas (scenes); cada personaje habla en su turno y las acotaciones (stage directions), entre paréntesis, indican cómo actuar. Un mito o leyenda (myth, legend) es un relato antiguo con hechos extraordinarios que explica algo del mundo. Una novela (novel) es un relato largo dividido en capítulos; en el colegio se leen versiones adaptadas.",
        "El tema (theme) es una idea general sobre la vida que se puede aplicar a otras historias. El asunto (topic) dice solo de qué trata: una lluvia, un partido. Un tema se escribe como oración completa: «La honestidad da tranquilidad». En 2.º medio se pide además que sustentes el tema con evidencia, es decir, con dos pistas del texto: una palabra, un verso, una acción o una acotación.",
        "Sigue tres pasos. Primero, observa la forma del texto y nombra el género. Segundo, subraya lo que se repite, lo que cambia o lo que los personajes aprenden. Tercero, escribe el tema en una oración y agrega dos pistas con la estructura «The text shows this because...». Si una pista no se relaciona con tu oración, cámbiala.",
    ],
    [("verse", "estrofa"), ("chorus", "estribillo: parte que se repite"), ("play", "obra de teatro"), ("act / scene", "acto / escena"), ("stage directions", "acotaciones: indicaciones para actuar, entre paréntesis"), ("myth / legend", "mito / leyenda: relato antiguo con hechos extraordinarios"), ("novel", "novela: relato largo en capítulos"), ("theme", "tema: idea general que el texto comunica"), ("topic", "asunto: de qué trata, en pocas palabras")],
    [
        ("Género y tema de una canción", f"Texto: {SONG} {GSONG} ¿Qué género es y cuál es su tema?",
         ["Tiene estrofa (verse) y estribillo (chorus), y los versos riman (cold con gold).", "Es una canción. Aunque el bus llega tarde y llueve, el hablante tiene a alguien a su lado y eso vale como oro.", "Tema: la compañía hace más llevaderos los momentos difíciles."], "Es una canción; su tema es que la compañía hace más llevaderos los momentos difíciles"),
        ("Las acotaciones en una obra de teatro", f"Texto: {PLAYA} {GPLAYA} ¿Qué género es y qué aportan las acotaciones?",
         ["Hay escena, nombres de personajes antes de cada línea y paréntesis: es una obra de teatro.", "Los paréntesis dicen que Ana entra con el teléfono, que está nerviosa y que habla en susurros.", "Esas acotaciones muestran emociones y acciones que los diálogos no dicen."], "Es una obra de teatro; las acotaciones muestran que Ana está nerviosa"),
    ],
    [
        ("Decir que el tema de la canción es «the bus».", "Se confunde el asunto (un objeto) con el tema (una idea completa).", "Escribe una oración sobre la vida: la compañía ayuda en los momentos difíciles."),
        ("Pensar que las acotaciones son parte de lo que dice el personaje.", "Están entre paréntesis y no se pronuncian: orientan a quien actúa.", "Lee los diálogos con el nombre del personaje y las acotaciones solo como instrucciones."),
    ],
    [
        mc("En una obra de teatro en inglés, las acotaciones (stage directions) son", "las indicaciones entre paréntesis sobre cómo actuar o qué ocurre", ["las líneas que cada personaje dice en voz alta ante el público", "el título de la obra y el nombre de quien la escribió"], "Se escriben entre paréntesis para orientar la actuación y no se pronuncian."),
        mc("El estribillo (chorus) de una canción es", "la parte que se repite entre las estrofas", ["la estrofa más larga y más importante de la canción", "el primer verso de todo el texto"], "Su rasgo es la repetición, no el largo ni la posición."),
        mc("¿Cuál de estas frases expresa un tema y no solo un asunto?", "El éxito de un equipo depende de todos sus integrantes", ["Un partido de básquetbol entre dos colegios", "La entrenadora y las jugadoras del equipo de básquetbol del colegio"], "Una idea completa sobre la vida es un tema; las otras dos son asuntos."),
    ],
    [
        mc(f"Lee: {MYTH} {GMYTH} ¿Por qué es un mito o leyenda?", "Explica con hechos extraordinarios por qué llueve en el mundo", ["Da pasos para hacer algo en orden, como una receta", "Está dividido en escenas con acotaciones"], "El Sol y la Luna discuten y sus lágrimas explican el origen de la lluvia."),
        mc(f"Lee: {GYM} {GGYM} En la acotación «(looking down)», ¿qué información se da sobre Mia?", "Que habla con tristeza y soledad, sin mirar a su entrenador", ["Que está presumiendo su trofeo con orgullo ante todos", "Que está enojada con su entrenador"], "Mirar hacia abajo, más sus palabras sobre su equipo ausente, muestra tristeza."),
        mc(f"Lee: {HOME} {GHOME} ¿Qué muestra que Chorus es un estribillo?", "Sus versos se repiten iguales tras cada una de las estrofas", ["Tiene más palabras que cualquier otra parte del texto", "Es la única parte que rima"], "El texto repite Home, home, take me home después de las dos estrofas."),
    ],
    [
        mc(f"Lee: {TREE} {GTREE} ¿Cuál es el tema del poema?", "Dar sin esperar nada a cambio es valioso", ["Los árboles viejos crecen mejor que los jóvenes", "La sombra es más fresca en verano"], "El árbol da sombra a todos y nunca pide nada."),
        mc(f"Lee: {WALLET} {GWALLET} ¿Cuál es el tema del cuento?", "Actuar con honestidad da tranquilidad a quien actúa así", ["Las billeteras se pierden con facilidad en los patios", "Los zapatos nuevos son muy caros"], "Eli devuelve la billetera y se siente liviano."),
        mc(f"Lee: {SKATE} {GSKATE} ¿Cuál es el tema de la tira cómica?", "Insistir después de fracasar lleva al progreso", ["Los aros de básquetbol están demasiado altos para jugar", "Las tardes son mejores para entrenar"], "La niña falla, practica cada tarde y al mes logra encestar."),
    ],
    [
        mc(f"Lee: {WALLET} Dos estudiantes escriben el tema. Lía: «Eli». Mateo: «Ser honesto puede dar paz, porque Eli se siente liviano tras devolver la billetera». ¿Quién formula bien un tema con evidencia?", "Mateo, porque escribe una idea completa y la apoya", ["Lía, porque un solo nombre resume todo el cuento", "Ninguno, porque los temas no necesitan evidencia del texto"], "Un tema es una oración sobre la vida apoyada en una pista del texto."),
        mc(f"Lee: {TREE} ¿Qué verso muestra mejor que el árbol da sin esperar nada a cambio?", "It never asks, it answers every call", ["the child, the bird, the tired man", "and gives as much as a tree can"], "Never asks dice directamente que no pide nada a cambio; los otros versos solo nombran a quienes reciben o la cantidad."),
    ],
    [
        mc(f"Compara dos textos. Texto A: {WIND} Texto B: {WIND2} {GWIND} ¿Qué tema comparten?", "Decir la verdad cuesta, pero pesa menos que callar y ocultar", ["Las ventanas rotas se arreglan fácilmente con ayuda", "Los adultos siempre se enojan al principio"], "En ambos, decir la verdad cuesta, pero el resultado es mejor que el silencio."),
        mc("Alba quiere convertir un cuento en una obra de teatro. ¿Qué cambio es necesario?", "Escribir diálogos con nombres de personajes y acotaciones", ["Hacer que todos los versos rimen entre sí", "Dibujar viñetas con globos de diálogo para cada escena nueva"], "El teatro se escribe en diálogos con nombres y acotaciones; la rima y las viñetas son de otros géneros."),
    ],
    [mc(f"En el club de inglés debes rotular tres textos con estas etiquetas: Songs, Plays, Comics. Lee el comienzo de uno: {STAGE} {GSTAGE} ¿Qué etiqueta le corresponde?", "Plays", ["Songs", "Comics"], "Tiene acto, escenario, narrador y acotación, rasgos del teatro.")],
    [
        ("Escribe en inglés la palabra que significa «acotaciones» en la expresión «stage ____».", "directions", "Stage directions son las indicaciones entre paréntesis en una obra de teatro."),
        mc("Una obra de teatro se divide en actos y estos, a su vez, en", "escenas (scenes)", ["estribillos (choruses)", "viñetas (panels)"], "Las partes de un acto se llaman escenas."),
        mc("Un tema se escribe mejor como", "una oración completa sobre la vida", ["una sola palabra que nombra un objeto del cuento", "el nombre del personaje principal"], "El tema es una idea general que puede aplicarse a otros casos."),
    ],
    task("Lee este texto original: «Panel 1: A girl hides a note in her bag. Panel 2: She reads it again and again, but she does not send it. Panel 3: She finally gives it to her friend. Friend: Thank you for telling me!» (note = nota; hides = esconde; bag = mochila; again and again = una y otra vez; finally = por fin; gives = entrega). En tu hoja anota: género, dos pistas de forma, tema en una oración y una pista del texto que lo apoye.",
         "Género: tira cómica. Pistas: viñetas numeradas y un diálogo. Tema: expresar lo que sentimos fortalece las amistades. Pista: finally gives it to her friend y ella responde Thank you.",
         ["nombra el género con dos pistas de forma", "escribe el tema como oración completa", "apoya el tema con una pista del texto"],
         ["ficha de cuatro líneas en la hoja"],
         ["escribir solo «note» o «friend» como tema", "dar una pista que no se relaciona con el tema"],
         "Pide que cambie la pista por otra del mismo texto y compruebe si el tema se mantiene."),
    "Copia los ocho términos del vocabulario y escribe un ejemplo en español de cada uno.",
    "Elige una canción que conozcas y escribe su tema en una oración, sin copiar su letra.",
)

# ============================================================ clase 2: personajes, caracterización y entorno
GRAN = "«Rafael was selfish. He never shared his sandwiches, and he always took the best seat on the bus.»"
GGRAN = "(selfish = egoísta; shared = compartió; seat = asiento)"
SIMON = "«Nadia arrived early and prepared the whole presentation alone. When her partner forgot the slides, she smiled and said, No problem, I have a copy. She never mentioned it again.»"
GSIMON = "(arrived = llegó; prepared = preparó; whole = completa; alone = sola; partner = compañero; forgot = olvidó; slides = diapositivas; copy = copia; mentioned = mencionó)"
STORM = "«The sky was black and the wind hit the windows. In the old house, the clock sounded loudly, and Claudia felt that something was waiting for her at the top of the stairs.»"
GSTORM = "(sky = cielo; hit = golpeaba; windows = ventanas; clock = reloj; sounded = sonaba; loudly = fuerte; waiting = esperando; stairs = escaleras)"
BEACH = "«The beach was full of children and laughter. The sun was warm and the music from the café made everyone want to dance.»"
GBEACH = "(beach = playa; laughter = risas; warm = cálido; café = cafetería; dance = bailar)"
ROD = "«Rodrigo accepted every challenge without thinking. He signed up for the long race without training. His friends warned him, but he laughed and said, Nothing can happen to me!»"
GROD = "(accepted = aceptó; challenge = desafío; signed up = se inscribió; race = carrera; training = entrenar; warned = advirtieron; laughed = se rio; nothing can happen = no puede pasarme nada)"
LENA = "«At the start of the term, Lena refused to speak in class because she was afraid of making mistakes. By December, she was asking questions and leading group discussions.»"
GLENA = "(term = semestre; refused = se negó; afraid = con miedo; mistakes = errores; leading = dirigiendo; discussions = discusiones)"
ISA = "«Isa took a job at a fruit stand because her family needed extra money. Every morning at six o'clock she opened the stand and sold fruit before school.»"
GISA = "(job = trabajo; fruit stand = puesto de fruta; extra = adicional; opened = abría; sold = vendía; fruit = fruta)"
OLGA = "«My mother is the most generous person I know, said Pablo. She works two jobs, but she always has time to cook for our neighbor when he is sick.»"
GOLGA = "(generous = generosa; works = trabaja; jobs = trabajos; cook = cocinar; neighbor = vecino; sick = enfermo)"
TOMAS = "«Tomás was the best student in the class and he knew it. He rolled his eyes when others asked questions, and he said, Everyone should be as smart as me.»"
GTOMAS = "(knew = sabía; rolled his eyes = puso los ojos en blanco; others = otros; smart = inteligente)"
CLIMB = "«At the base of the cliff, Camilo felt his hands shake because of his fear of heights. He took a deep breath, checked his rope twice and began to climb slowly with his guide beside him.»"
GCLIMB = "(base = base; cliff = acantilado; shake = temblar; fear of heights = miedo a las alturas; deep breath = respiración profunda; rope = cuerda; climb = escalar; slowly = lentamente; guide = guía)"
MARIA = "«Maria wanted to be the first in her family to go to university. She studied every night, even when she was tired, because that was her dream.»"
GMARIA = "(university = universidad; studied = estudiaba; tired = cansada; dream = sueño)"
SARA = "«Sara checked the map twice before choosing a path. She carried extra snacks and a warm jacket and asked her group to wait at every fork.»"
GSARA = "(map = mapa; path = sendero; carried = llevaba; extra = adicional; snacks = colaciones; warm jacket = chaqueta abrigada; wait = esperar; fork = bifurcación)"
LONELY = "«It was winter in the north. The streets were empty, the shop windows were dark, and a cold fog covered the town square.»"
GLONELY = "(empty = vacías; shop windows = vitrinas; dark = oscuras; fog = niebla; covered = cubría; town square = plaza)"

lesson(
    OA, 2, MAT,
    "Aprenderé a describir a un personaje de dos formas, explicando por qué actúa y cómo cambia, y a ver cómo el entorno crea un ambiente. Sirve para apoyar con evidencia lo que dices de un personaje, en vez de dar solo una opinión.",
    ["Sé que los personajes tienen rasgos y que el entorno tiene tiempo y lugar.", "Conozco adjetivos como brave, shy, curious, generous y stubborn."],
    [
        "La caracterización (characterization) puede ser directa o indirecta. Es directa cuando el narrador dice cómo es el personaje: «Rafael was selfish». Es indirecta cuando lo muestran sus acciones, sus palabras, sus pensamientos o lo que otros dicen de él. También usarás responsible (responsable), determined (decidido) y lazy (flojo). Ocho rasgos nuevos: loyal (leal), selfish (egoísta), reckless (imprudente), cautious (cuidadoso), humble (humilde), anxious (ansioso), ambitious (con grandes metas) y arrogant (arrogante).",
        "La motivación (motivation) es la razón por la que un personaje actúa. La encuentras con la pregunta «¿Por qué lo hace?». Un personaje también puede cambiar: compara cómo es al comienzo con cómo es al final. El entorno (setting) incluye tiempo y lugar, pero además crea un ambiente (mood), que es el sentimiento que produce el texto: miedo, calma, alegría. Para saberlo, mira palabras como black, empty, warm o laughter.",
        "Para analizar a un personaje, usa la estructura «Personaje + rasgo + evidence + motivation». Por ejemplo: «Isa is responsible because she opens the stand every morning; she works because her family needs money». Una buena respuesta cita una acción o una frase del texto. Si la evidencia no se relaciona con el rasgo, o si el rasgo no encaja, cambia uno de los dos.",
    ],
    [("direct characterization", "caracterización directa: el narrador dice cómo es"), ("indirect characterization", "caracterización indirecta: se deduce de acciones, palabras o pensamientos"), ("motivation", "motivación: razón por la que actúa"), ("mood", "ambiente: sentimiento que produce el texto"), ("loyal / selfish / reckless / cautious", "leal / egoísta / imprudente / cuidadoso"), ("humble / anxious / ambitious / arrogant", "humilde / ansioso / ambicioso / arrogante")],
    [
        ("Caracterización directa e indirecta", f"Texto A: {GRAN} {GGRAN} Texto B: {SIMON} {GSIMON} ¿Cuál usa caracterización directa y cuál indirecta?",
         ["El texto A dice el rasgo con una palabra: selfish.", "El texto B no nombra ningún rasgo, pero Nadia prepara todo, sonríe y no menciona el error de su compañero.", "A es directa; B es indirecta y muestra a una persona responsable y generosa."], "A es directa (selfish); B es indirecta (sus acciones muestran responsabilidad)"),
        ("Ambiente del entorno", f"Texto: {STORM} {GSTORM} ¿Qué ambiente crea el entorno y qué palabras lo muestran?",
         ["Busca palabras de lugar y tiempo: black sky, wind, old house, clock sounded loudly.", "Esas palabras producen miedo o tensión.", "Además, Claudia siente que algo la espera arriba, y eso refuerza el ambiente."], "Ambiente de miedo o suspenso, mostrado por black, wind, old house y loudly"),
    ],
    [
        ("Decir que un personaje es «lazy» solo porque el texto menciona que está en un dormitorio.", "Un lugar no prueba un rasgo: falta una acción o una frase que lo apoye.", "Busca qué hace, qué dice y por qué: esa es la evidencia."),
        ("Confundir el ambiente (mood) con el lugar.", "El lugar es dónde ocurre; el ambiente es el sentimiento que producen las palabras.", "Pregunta qué siente quien lee: calma, miedo o alegría."),
    ],
    [
        mc("En la caracterización directa, el rasgo del personaje", "lo dice explícitamente el narrador", ["se descubre solo por el título del texto", "se deduce del color de la portada"], "Directa significa que el texto nombra el rasgo con palabras como selfish o brave."),
        mc("«Loyal» describe a una persona que", "permanece fiel a sus amigos aunque sea difícil y no los abandona", ["siempre piensa solo en sí misma y en lo que le conviene", "actúa sin pensar en los riesgos"], "Loyal es leal; las otras opciones describen egoísmo e imprudencia."),
        mc("En un texto, el ambiente (mood) es", "el sentimiento que producen las palabras", ["el nombre del autor y el año del texto", "la cantidad de personajes que aparecen en la historia"], "El ambiente se siente con palabras como dark, warm o quiet."),
    ],
    [
        mc(f"Lee: {ROD} {GROD} ¿Qué rasgo muestran sus acciones?", "Reckless", ["Cautious", "Humble"], "Se inscribe sin entrenar y rechaza las advertencias: es imprudente."),
        mc(f"Lee: {MARIA} {GMARIA} ¿Por qué estudia María cada noche (motivación)?", "Porque quiere ser la primera de su familia en la universidad", ["Porque le gusta quedarse despierta hasta muy tarde cada noche de la semana", "Porque su familia la obliga a estudiar todas las noches"], "El texto da la razón con wanted to be the first in her family."),
        mc(f"Lee: {BEACH} {GBEACH} ¿Qué ambiente crea la descripción?", "Alegre y festivo", ["Misterioso y tenso", "Triste y solitario"], "Children, laughter, warm y dance producen alegría."),
    ],
    [
        mc(f"Lee: {TOMAS} {GTOMAS} ¿Qué rasgo tiene Tomás y cuál es la evidencia?", "Arrogant: pone los ojos en blanco y dice que todos deberían ser tan inteligentes como él", ["Humble: sabe que es el mejor estudiante, pero no lo dice y escucha a todos", "Anxious: hace preguntas en clase porque está nervioso"], "Sus palabras y su gesto muestran que se siente superior."),
        mc(f"Lee: {CLIMB} {GCLIMB} ¿Qué rasgo muestran sus acciones al escalar?", "Cautious: revisa dos veces su cuerda y avanza despacio", ["Reckless, porque escala un acantilado alto", "Arrogant, porque se cree mejor que su guía"], "Respira hondo, revisa la cuerda y sube con cuidado pese a su miedo."),
        mc(f"Lee: {LONELY} {GLONELY} ¿Qué pistas crean un ambiente de soledad?", "Empty streets, dark shop windows and cold fog", ["The north, a winter day, shop windows and the town square", "The shop windows, the town and the square"], "Empty, dark y cold producen sensación de vacío; las otras opciones solo nombran lugares."),
    ],
    [
        mc(f"Lee: {LENA} {GLENA} ¿Cómo cambia Lena y qué evidencia lo muestra?", "Del miedo a hablar a dirigir discusiones (refused to speak, leading group discussions)", ["De dirigir discusiones a quedarse callada (leading, refused to speak)", "No cambia, porque siempre habla en clase"], "Se comparan el comienzo (refused) con el final (leading)."),
        mc(f"Lee: {OLGA} {GOLGA} Pablo dice que su madre es generosa. Este es un ejemplo de", "caracterización indirecta, porque habla otro personaje", ["caracterización directa, porque el narrador dice cómo es ella", "un cambio de personaje que ocurre al final"], "Habla un personaje (Pablo), no el narrador, así que la caracterización es indirecta."),
    ],
    [
        mc(f"Lee: {ISA} {GISA} ¿Qué descripción de Isa tiene rasgo, evidencia y motivación?", "Responsible: opens the stand daily; her family needs money", ["Responsible: she is a girl who works at a fruit stand near her school", "Lazy: she sells fruit before school"], "Une el rasgo con una acción del texto y la razón que da el texto."),
        mc("Un lector dice: «Daniela es leal, porque se llama Daniela». ¿Qué falta en su respuesta?", "Evidencia: una acción o frase del texto que pruebe el rasgo", ["Un adjetivo en inglés más difícil y más largo", "El nombre del narrador"], "Un rasgo sin evidencia es una opinión; falta citar el texto."),
    ],
    [mc(f"En el club de lectura alguien escribe que Sara es cautious. Lee: {SARA} {GSARA} ¿Qué detalle del texto apoya ese rasgo?", "She checked the map twice before choosing a path", ["She is part of a group of hikers", "She chose a path in the forest"], "Revisar el mapa dos veces antes de decidir es una acción prudente; las otras opciones no prueban el rasgo.")],
    [
        ("Escribe en inglés el adjetivo para alguien que actúa sin pensar en los riesgos.", "Reckless", "Reckless describe a quien se arriesga sin pensar."),
        mc("«Mood» en un texto literario significa", "el sentimiento que produce el texto", ["el tiempo exacto en que ocurre la historia", "la rima de los versos"], "El ambiente no es el tiempo ni la rima, sino lo que se siente al leer."),
        mc("La motivación de un personaje responde a la pregunta", "¿Por qué actúa así?", ["¿Cuántos años tiene?", "¿Dónde vive?"], "La motivación es la razón de sus acciones."),
    ],
    task("Lee: «Gabriel never missed a training session, even when it was raining. When his teammate was injured, he carried his bag and stayed with him until the doctor arrived. Gabriel was never the best player, but the team trusted him.» (training session = entrenamiento; teammate = compañero de equipo; injured = lesionado; carried = llevó; trusted = confiaba en). En tu hoja escribe: un rasgo, dos pistas de evidencia, su motivación probable y si la caracterización es directa o indirecta.",
         "Rasgo: loyal. Evidencia: stayed with his injured teammate and never missed training. Motivación probable: quiere apoyar a su equipo. Caracterización: indirecta, porque el narrador no nombra el rasgo.",
         ["usa un rasgo del vocabulario", "cita dos acciones del texto", "explica la motivación y el tipo de caracterización"],
         ["ficha de cuatro líneas en la hoja"],
         ["dar el rasgo sin evidencia", "decir directa cuando el narrador no nombra el rasgo"],
         "Pide que explique por qué su rasgo es mejor que otro posible, usando la misma evidencia."),
    "Escribe una oración con cada uno de los ocho rasgos nuevos usando un personaje inventado.",
    "Describe a un personaje de una película que conozcas con rasgo, evidencia y motivación, sin copiar diálogos.",
)
