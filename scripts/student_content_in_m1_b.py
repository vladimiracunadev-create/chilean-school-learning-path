"""Cuaderno del estudiante, 1.º medio Inglés (oficial): IN1M OA 11, comprensión de textos literarios.

Los textos en inglés son originales, breves y llevan glosario en español dentro del enunciado. Cada término se enseña
en la clase antes de usarlo. Sin audio externo: todo lo que hay que leer está escrito en el enunciado.
Los títulos de clase del plan son genéricos (propósito, evidencia, estrategia, brecha de información, respuesta
independiente): aquí se aplican al tipo de texto y tema, personajes y entorno, trama y problema-solución,
trabajo con tarjetas incompletas, y palabras, expresiones idiomáticas y vocabulario temático.
Este módulo define también los ayudantes `lesson` y `mc` que importan los demás módulos in_m1_b*.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "IN1M OA 11"


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def mc(stem, right, wrongs, why):
    """Pregunta de alternativas: la correcta se escribe primera; el registro balancea la posición."""
    options = [o.strip().rstrip(".?!,;") for o in [right] + list(wrongs)]  # sin puntuación final: el balanceo la reubica
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

# ============================================================ clase 1: tipos de texto literario y tema
LH = "«The old lighthouse stands alone / Above the cold and windy sea. / It does not move, it does not moan, / It shows the way for you and me.»"
GLH = "(lighthouse = faro; stands = se levanta; alone = solo; windy = ventoso; moan = quejarse; shows the way = muestra el camino)"
FOXL = "«A small silver fox lived near a lake. Every night it cried because it had no friends. One night a girl heard it and left some bread by the water. After that, the fox stayed near the village and guarded the children when they played near the lake.»"
GFOXL = "(fox = zorro; silver = plateado; cried = lloraba; heard = oyó; left = dejó; guarded = cuidaba; village = aldea)"
RAIN = "«Rain on the roof, rain on the street, / Rain makes the dry earth sweet. / After the storm the flowers grow: / Be patient, and good things show.»"
GRAIN = "(roof = techo; dry = seco; earth = tierra; sweet = dulce; storm = tormenta; flowers = flores; patient = paciente; show = aparecen)"
KITE = "«Panel 1: A boy looks at his broken kite. Boy: It is ruined! Panel 2: His sister brings tape and paper. Sister: Let's fix it together. Panel 3: They fly the kite. Boy: Thanks! It's better than new!»"
GKITE = "(kite = volantín; broken = roto; ruined = arruinado; tape = cinta adhesiva; fix = arreglar; together = juntos; better than new = mejor que nuevo)"
CHESS = "«Mara wanted to win the school chess tournament. She lost her first game and then her second. She almost quit. Then her grandfather said, Every game teaches you a new move. Mara played again. She lost the third game, but she smiled because she learned a new opening. At the end she did not win a trophy, but she felt proud.»"
GCHESS = "(chess = ajedrez; tournament = torneo; lost = perdió; quit = rendirse; teaches = enseña; opening = apertura; trophy = trofeo; proud = orgullosa)"
GIANT = "«Long ago, they say, the mountain was a giant who fell asleep after a long walk. Rain covered his back with grass and trees. Today, when the wind blows, people say he is still breathing in his sleep.»"
GGIANT = "(giant = gigante; fell asleep = se durmió; covered = cubrió; grass = pasto; breathing = respirando)"
DOG = "«Tomas found a lost dog in the park. It had a blue collar and a phone number. Tomas was hungry and late for soccer, but he called the number. Soon a little boy ran to them and hugged the dog. Tomas missed the first ten minutes of the game, and he did not mind.»"
GDOG = "(lost = perdido; collar = collar; hugged = abrazó; missed = se perdió; mind = importar)"
BRIDGE = "«Title: The Bridge. I am only wood and rope, / yet I help you cross the river. / You are on one side, / your friends are on the other. / I carry you, and I stay.»"
GBRIDGE = "(bridge = puente; wood = madera; rope = cuerda; cross = cruzar; river = río; carry = llevar; stay = quedarse)"
ADAPT = "«This adapted version of a classic adventure is for young readers. Ben, a fisherman's son, finds a map in an old bottle. With his best friend Lena, he sails to a hidden island. They find the treasure, but Ben decides to share it with Lena and her family, because they helped him all along.»"
GADAPT = "(adapted version = versión adaptada; map = mapa; bottle = botella; sails = navega; hidden = escondida; treasure = tesoro; share = compartir; helped = ayudaron)"
GARDEN1 = "«The garden was dry. Rafa watered it every day. In April, tomatoes grew.»"
GARDEN2 = "«The garden was dry. Everybody said, It is useless. Rafa watered it every day. In April, tomatoes grew.»"
GGARDEN = "(garden = jardín; dry = seco; watered = regó; useless = inútil; grew = crecieron)"

lesson(
    OA, 1, MAT,
    "Aprenderé a reconocer si un texto es un poema, una tira cómica, un cuento, una leyenda o una novela adaptada, y a decir cuál es su tema. Sirve para saber qué buscar antes de leer los detalles.",
    ["Sé que un texto puede contar, describir o informar.", "Conozco palabras como story, poem y character."],
    [
        "Los textos literarios cuentan o expresan algo con intención artística. Un poema (poem) se escribe en versos, es decir, en líneas cortas, y muchas veces rima. Una tira cómica (comic strip) cuenta una historia en viñetas (panels), con dibujos y globos de diálogo. Un cuento (short story) es un relato breve con personajes. Una leyenda o mito (legend, myth) es un relato antiguo que explica algo de la naturaleza o cuenta hechos extraordinarios. Una novela adaptada (adapted novel) es una novela larga que se acorta y se simplifica para lectores jóvenes.",
        "El tema (theme) es la idea general que el texto quiere comunicar. No es lo mismo que el asunto (topic): el asunto responde «¿de qué trata?» en pocas palabras (ajedrez, un faro, un perro), y el tema es una idea completa que se puede aplicar a la vida real, como «se aprende de las derrotas». Para encontrarlo, pregúntate qué cambia en el personaje al final o qué quiere enseñar el poema.",
        "Sigue tres pasos. Primero, mira la forma del texto: versos, viñetas o párrafos. Segundo, lee y subraya los detalles que se repiten o que producen un cambio. Tercero, escribe el tema en una oración y comprueba que se apoya en esos detalles. Un buen tema es general; un detalle, como el nombre de un personaje, es solo una parte del texto.",
    ],
    [("poem", "poema: versos cortos que a veces riman"), ("comic strip", "tira cómica: historia en viñetas con globos"), ("short story", "cuento: relato breve con personajes"), ("legend", "leyenda: relato antiguo que explica algo o cuenta hechos extraordinarios"), ("theme", "tema: idea general del texto"), ("topic", "asunto: de qué trata, en pocas palabras"), ("panel", "viñeta")],
    [
        ("Reconocer un poema y su tema", f"Texto: {LH} {GLH} ¿Qué tipo de texto es y cuál es su tema?",
         ["Está escrito en versos cortos que riman (sea con me, alone con moan).", "Es un poema. El faro no se mueve ni se queja, y muestra el camino.", "La idea general: alguien constante puede guiar a los demás sin pedir nada."], "Es un poema; su tema es que ser constante y guiar a otros es valioso"),
        ("Reconocer un cuento y su tema", f"Texto: {FOXL} {GFOXL} ¿Qué tipo de texto es y cuál es su tema?",
         ["Es un relato breve con personajes y un cambio: el zorro deja de estar solo.", "Es un cuento breve de animales, con un cambio al final: el zorro ya no está solo.", "El asunto es un zorro; el tema es que un gesto amable puede crear una amistad."], "Es un cuento breve; su tema es que un gesto amable puede crear una amistad"),
    ],
    [
        ("Decir que el tema del cuento del ajedrez es «chess».", "Se confunde el asunto (una palabra) con el tema (una idea completa).", "Escribe una oración: se puede aprender incluso cuando se pierde."),
        ("Elegir como tema un detalle, como «Tomas has a blue collar».", "Un detalle del texto no es una idea general que sirva para otras historias.", "Pregúntate qué quiere enseñar el texto, no qué objetos aparecen."),
    ],
    [
        mc("En Inglés de 1.º medio: ¿cuál de estos textos es un poema?", "«Cold wind, quiet night, / the moon is a silver light.»", ["«Dear Ana, I am writing to tell you about my trip to the south.»"], "Tiene versos cortos que riman (night con light)."),
        mc("¿Cuál de estos textos es una tira cómica?", "«Panel 1: A cat sees a fish. Cat: Mmm! Panel 2: The fish jumps away.»", ["«Ingredients: two eggs, flour and milk.»"], "Tiene viñetas numeradas y diálogo, que es la forma de una tira cómica."),
        mc("En un texto literario en inglés, el tema (theme) es", "la idea general que el texto quiere comunicar", ["el nombre del personaje principal", "la hora en que ocurre la historia"], "El tema es una idea completa; los nombres y la hora son detalles."),
    ],
    [
        mc(f"Lee: {RAIN} {GRAIN} ¿Cuál es el tema del poema?", "Después de una época difícil, la paciencia trae cosas buenas", ["La lluvia es peligrosa para las flores", "En invierno las calles se mojan"], "Los dos últimos versos dicen que, tras la tormenta, crecen las flores y hay que ser paciente."),
        mc(f"Lee la tira cómica: {KITE} {GKITE} ¿Cuál es su tema?", "Trabajar juntos puede arreglar un problema", ["Los volantines son muy caros", "Los niños vuelan volantines los domingos"], "La hermana trae cinta y papel y dice «arreglémoslo juntos»; el volantín queda mejor que nuevo."),
        mc(f"Lee: {CHESS} {GCHESS} ¿Cuál es el tema del cuento?", "Se puede aprender algo valioso al perder", ["Ganar el trofeo es lo único que importa", "El ajedrez es un juego fácil"], "Mara pierde tres partidas, pero aprende una apertura nueva y se siente orgullosa."),
    ],
    [
        mc(f"Lee: {GIANT} {GGIANT} ¿Qué tipo de texto es?", "Una leyenda, porque explica algo de la naturaleza con un hecho extraordinario", ["Una noticia, porque informa lo que pasó ayer", "Una carta personal, porque cuenta algo a alguien"], "Explica por qué la montaña parece respirar, usando un gigante dormido."),
        mc(f"Lee: {RAIN} {GRAIN} ¿Qué pista de forma muestra que es un poema?", "Tiene versos cortos que riman (street con sweet, grow con show)", ["Tiene viñetas con globos de diálogo", "Tiene pasos numerados"], "La rima y los versos son las marcas formales de un poema."),
        mc(f"Lee: {DOG} {GDOG} ¿Cuál es el tema del cuento?", "Hacer lo correcto puede valer más que tus propios planes", ["Es mejor llegar siempre a tiempo al partido que ayudar a otros", "Los perros con collar nunca se pierden"], "Tomas llega tarde al partido, pero no le importa porque ayudó al niño."),
    ],
    [
        mc(f"Lucía lee el cuento del ajedrez: {CHESS} y dice que el tema es «chess». ¿Qué corrección es la mejor?", "Chess es el asunto; el tema es la idea de que se puede aprender al perder", ["Tiene razón, porque el tema siempre es una sola palabra", "El tema es el trofeo"], "El asunto es una palabra; el tema es una idea completa apoyada por el final del cuento."),
        mc(f"Lee la tira cómica: {KITE} ¿Qué detalle muestra mejor que el tema es «trabajar juntos»?", "La hermana dice Let's fix it together", ["El niño dice It is ruined", "En la viñeta 1 el niño mira el volantín"], "Together nombra directamente la idea; los otros detalles muestran el problema."),
    ],
    [
        mc(f"Hay dos versiones de una historia. Versión 1: {GARDEN1} Versión 2: {GARDEN2} {GGARDEN} ¿Qué tema encaja con la versión 2 pero no con la 1?", "Sigue intentando aunque otros duden de ti", ["Los tomates crecen mejor en abril", "Los jardines necesitan muchas personas"], "Solo en la versión 2 hay personas que dicen que es inútil y Rafa igual insiste."),
        mc(f"Lee: {BRIDGE} {GBRIDGE} ¿Qué tema se apoya mejor en el poema?", "Algo sencillo puede unir a las personas", ["Los ríos son peligrosos", "La madera es mejor que la cuerda"], "El puente deja pasar a quien quiere llegar a sus amigos al otro lado."),
    ],
    [mc(f"En la biblioteca del colegio lees la contratapa de un libro: {ADAPT} {GADAPT} ¿Cuál es el tema de la historia?", "Compartir con quienes te ayudan es importante", ["Encontrar un tesoro es fácil", "Las botellas llevan mensajes"], "Ben comparte el tesoro con Lena y su familia porque lo ayudaron.")],
    [
        mc("¿Cuál de estas ideas es un tema y no un detalle?", "La perseverancia ayuda a lograr una meta", ["El abuelo de Mara es mayor", "El torneo es en el colegio"], "Es una idea general; las otras dos son datos de un cuento."),
        mc("¿Qué marca de forma indica que un texto es una tira cómica?", "Viñetas con globos de diálogo", ["Versos que riman"], "Las viñetas y los globos cuentan la historia en una tira cómica."),
        ("Escribe en inglés la palabra que significa «tema» (la idea general de un texto).", "Theme", "Theme es la idea general; topic es solo de qué trata."),
    ],
    task("Lee este poema original: «The little seed is under snow, / It cannot see the sun. / It waits and waits, it does not go, / Until the spring has come.» (seed = semilla; snow = nieve; waits = espera; spring = primavera). En tu hoja anota: tipo de texto, una pista de forma, el asunto en dos palabras y el tema en una oración.",
         "Tipo: poema. Pista: versos cortos que riman (snow con go, sun con come). Asunto: una semilla. Tema: hay que esperar con paciencia el momento adecuado.",
         ["dice el tipo de texto y una pista de forma", "separa asunto (pocas palabras) y tema (una oración)", "el tema no es un nombre ni un objeto"],
         ["ficha de cuatro líneas en la hoja"],
         ["escribir solo «seed» como tema", "no dar ninguna pista del texto"],
         "Pide que cambie la semilla por otro ser vivo y compruebe si su tema sigue sirviendo."),
    "Copia los siete términos del vocabulario y escribe una frase en español con cada uno.",
    "Escribe en español el tema de un cuento o película que conozcas bien, en una oración que no use nombres propios.",
)

# ============================================================ clase 2: personajes, caracterización y entorno
SHEP = "«Long ago, in a village between two hills, lived a shepherd named Teo. He was generous: every winter he gave half of his wool to his neighbors. One cold morning, he found a lost lamb in the snow, and he carried it home on his back.»"
GSHEP = "(shepherd = pastor; hills = cerros; wool = lana; neighbors = vecinos; lamb = cordero; carried = llevó; on his back = en la espalda)"
SOFI = "«Sofia is shy. In class she never raises her hand. But at the end of the day, when her friend Pablo drops his books, she runs to help him before anyone else.»"
GSOFI = "(shy = tímida; raises = levanta; drops = se le caen; runs = corre; anyone else = nadie más)"
LIB = "«It was late evening in a small library on an island. Nora, the librarian, put the last book on the shelf. She was curious about everything, so she opened an old box in the corner. Inside, she found a letter with a drawing of her own village.»"
GLIB = "(librarian = bibliotecaria; shelf = estante; curious = curiosa; corner = rincón; letter = carta; drawing = dibujo)"
IAN = "«I will not wear a coat, said Ian. Even if it is cold! His mother held out the coat again. Ian, it is snowing. I do not care, he said. He walked out with his arms crossed.»"
GIAN = "(coat = abrigo; held out = extendió; snowing = nevando; care = importar; arms crossed = brazos cruzados)"
FARM = "«In the summer of the big drought, Rita lived on a small farm near a dry river. She was honest. When the shop owner gave her too much change, she walked back two kilometers to return it.»"
GFARM = "(drought = sequía; farm = granja; shop owner = dueño de la tienda; change = vuelto; walked back = volvió caminando; return = devolver)"
CAVE = "«Dani and his sister Eli enter the cave. Dani whispers, Maybe we should go back. Eli smiles, takes the flashlight and walks first.»"
GCAVE = "(cave = cueva; whispers = susurra; go back = volver; flashlight = linterna; walks first = camina primero)"
SCARF = "«The streetlights were on. Mia put on her scarf and boots and kicked the snow off the steps of her house. In the window, the lights of the school bus appeared.»"
GSCARF = "(streetlights = luces de la calle; scarf = bufanda; boots = botas; kicked = sacudió con el pie; steps = escalones)"
MARTA = "«One windy dawn on the coast of Chiloé, Marta, the youngest in her family, pushed her small boat into the sea. Everybody said she was too small to fish alone, but she was determined, and she did not turn back.»"
GMARTA = "(dawn = amanecer; windy = ventoso; youngest = la menor; pushed = empujó; determined = decidida; turn back = volver atrás)"
CLARA = "«On Monday morning, in a small school in the Atacama Desert, Clara looked at the empty chair next to hers. Her new classmate was nervous: he did not speak or look at anybody. Clara smiled and said, Do you want to share my book?»"
GCLARA = "(empty = vacía; classmate = compañero; nervous = nervioso; look at = mirar a; anybody = nadie; share = compartir)"

lesson(
    OA, 2, MAT,
    "Aprenderé a describir a un personaje con evidencia del texto y a decir cuándo y dónde ocurre una historia. Sirve para apoyar lo que dices con una frase exacta, y no con una opinión sin pruebas.",
    ["Sé reconocer el tipo de texto y su tema.", "Conozco adjetivos como happy, sad y kind."],
    [
        "Los personajes (characters) son quienes viven la historia. El personaje principal (main character) es el más importante; los demás son personajes secundarios. La caracterización (characterization) es la forma en que el texto muestra cómo es un personaje: por lo que dice, por lo que hace y por lo que otros dicen de él. Los rasgos (traits) se nombran con adjetivos: brave (valiente), shy (tímido), curious (curioso), generous (generoso), stubborn (terco), honest (honesto), lazy (flojo) y kind (amable).",
        "El entorno (setting) tiene dos partes: el tiempo y el lugar. El tiempo dice cuándo ocurre: long ago, last winter, late evening, on Monday morning. El lugar dice dónde: in a village, on an island, in a small school. Estas pistas aparecen casi siempre al comienzo del texto y ayudan a imaginar la escena.",
        "Para describir a un personaje, usa la fórmula «personaje + rasgo + because + acción»: Teo is generous because he gives half of his wool. La palabra because (porque) une el rasgo con la evidencia. Si no encuentras una acción o una frase que apoye el rasgo, cambia el rasgo. A veces un personaje muestra más de un rasgo, y cada uno necesita su propia evidencia.",
    ],
    [("character", "personaje"), ("main character", "personaje principal"), ("trait", "rasgo de carácter"), ("characterization", "caracterización: cómo el texto muestra a un personaje"), ("setting", "entorno: tiempo y lugar"), ("evidence", "evidencia: frase o dato del texto que apoya una idea"), ("because", "porque"), ("brave / shy / curious / generous / stubborn / honest / lazy", "valiente / tímido / curioso / generoso / terco / honesto / flojo")],
    [
        ("Rasgo, evidencia y entorno", f"Texto: {SHEP} {GSHEP} ¿Cómo es Teo, qué lo prueba y cuál es el entorno?",
         ["Teo gives half of his wool every winter and carries the lost lamb home.", "Esas acciones muestran que es generoso: Teo is generous because he gives half of his wool.", "Tiempo: long ago, en invierno y una mañana fría. Lugar: a village between two hills."], "Es generoso (gives half of his wool); ocurre long ago, en una aldea entre dos cerros"),
        ("Más de un rasgo", f"Texto: {SOFI} {GSOFI} ¿Qué rasgos tiene Sofia y qué evidencia hay para cada uno?",
         ["Never raises her hand: es tímida.", "Runs to help Pablo before anyone else: es amable y ayuda sin dudar.", "Cada rasgo se apoya en una acción distinta."], "Es tímida (never raises her hand) y amable (runs to help Pablo)"),
    ],
    [
        ("Decir «Ian is angry» solo porque está afuera en la nieve.", "Estar afuera no prueba un rasgo; falta una frase o acción del texto que lo apoye.", "Busca lo que dice y hace: rechaza el abrigo dos veces, así que es terco."),
        ("Pensar que el entorno es solo el lugar.", "El entorno incluye también el tiempo.", "Anota siempre dos datos: cuándo (tiempo) y dónde (lugar)."),
    ],
    [
        mc("¿Qué dos datos forman el entorno (setting) de una historia?", "El tiempo y el lugar", ["El problema y la solución", "El tema y el título"], "El entorno responde cuándo y dónde ocurre la historia."),
        mc("«Generous» describe a una persona que", "comparte lo que tiene", ["tiene miedo de hablar", "no dice la verdad"], "Generous es generoso; las otras opciones describen timidez y deshonestidad."),
        mc("En la oración «On a farm in the south, Rita fed the hens», ¿cuál es el lugar? (hens = gallinas)", "On a farm in the south", ["Rita", "Fed the hens"], "El lugar dice dónde ocurre la acción; Rita es el personaje y fed the hens es la acción."),
    ],
    [
        mc(f"Lee: {LIB} {GLIB} ¿Cuándo ocurre la escena?", "Late evening", ["In the morning", "Long ago"], "El texto abre con It was late evening."),
        mc(f"Lee: {LIB} {GLIB} ¿Qué acción de Nora muestra su curiosidad?", "She opened an old box in the corner", ["She put the last book on the shelf", "She is a librarian"], "Abrir la caja vieja es la acción que el texto une con su curiosidad (so she opened)."),
        mc(f"Lee: {IAN} {GIAN} ¿Cómo es Ian?", "Stubborn, porque rechaza el abrigo aunque su mamá le avisa que nieva", ["Shy, porque no quiere hablar con su mamá", "Generous, porque su mamá le ofrece un abrigo"], "Dice I will not wear a coat y I do not care, así que no cambia de idea."),
    ],
    [
        mc(f"Lee: {FARM} {GFARM} ¿Dónde vive Rita?", "On a small farm near a dry river", ["In a big city", "In a school"], "El lugar aparece en la primera oración."),
        mc(f"Lee: {FARM} {GFARM} ¿Qué rasgo y qué evidencia describen mejor a Rita?", "Honest, porque camina dos kilómetros para devolver el vuelto de más", ["Generous, porque vive en una granja", "Curious, porque vive cerca de un río"], "El texto dice honest y lo prueba con su acción de devolver el dinero."),
        mc("Lee: «Marco never finished his homework, and he slept in class.» (homework = tarea; slept = durmió) ¿Qué rasgo muestran estas acciones?", "Lazy", ["Brave", "Curious"], "No terminar la tarea y dormir en clase son acciones de una persona floja."),
    ],
    [
        mc(f"Dos lectores leen: {IAN} Lector 1: Ian es valiente porque sale a la nieve. Lector 2: Ian es terco porque rechaza el abrigo aunque le avisan que nieva. ¿Quién usa mejor la evidencia?", "El lector 2, porque se apoya en sus palabras y en su actitud", ["El lector 1, porque la nieve es fría", "Los dos, porque cualquier rasgo se puede defender sin pruebas"], "Lo que Ian dice y hace dos veces apoya mejor terco que valiente."),
        mc(f"Lee: {FARM} Si la historia ocurriera en una primavera lluviosa, en vez de «the summer of the big drought», ¿qué detalle del texto dejaría de calzar?", "A dry river", ["Honest", "Walked back two kilometers"], "En una primavera lluviosa el río no estaría seco; el tiempo explica el río."),
    ],
    [
        mc(f"Lee: {CAVE} {GCAVE} ¿Qué afirmación está apoyada por el texto?", "Eli es más valiente que Dani, porque camina primero", ["Dani es más valiente, porque habla", "Los dos son tímidos"], "Dani propone volver y Eli toma la linterna y avanza."),
        mc(f"Lee: {SCARF} {GSCARF} ¿Qué pistas muestran que es invierno?", "Scarf, boots and snow", ["Streetlights, window and bus", "Steps, house and window"], "La bufanda, las botas y la nieve son pistas de estación."),
    ],
    [mc(f"En el club de lectura completas una ficha sobre este cuento: {MARTA} {GMARTA} ¿Qué rasgo y qué evidencia anotas para Marta?", "Determined, porque sale a pescar aunque todos dicen que es muy pequeña", ["Shy, porque es la menor de su familia", "Lazy, porque sale al amanecer"], "Hace lo que dicen que no puede y no vuelve atrás.")],
    [
        mc("¿Qué es la caracterización (characterization)?", "La forma en que el texto muestra cómo es un personaje, por lo que dice y hace", ["El lugar donde vive un personaje", "La rima de un poema"], "Se trata de cómo el texto muestra a los personajes."),
        ("Escribe en inglés el adjetivo para alguien que no cambia de idea aunque le den buenas razones.", "Stubborn", "Stubborn describe a quien se mantiene terco en su idea."),
        ("En «Late at night, in a tent on a hill, Pia read a comic», escribe en inglés el tiempo de la escena.", "Late at night", "El tiempo responde cuándo; in a tent on a hill es el lugar."),
    ],
    task(f"Lee: {CLARA} {GCLARA} En tu hoja completa una ficha de cuatro líneas: personaje principal, un rasgo con la forma «personaje + rasgo + because + acción», tiempo y lugar.",
         "Main character: Clara. Clara is kind because she smiles and offers to share her book. Time: Monday morning. Place: a small school in the Atacama Desert.",
         ["usa un adjetivo de la lista", "une el rasgo con una acción usando because", "anota el tiempo y el lugar por separado"],
         ["ficha de cuatro líneas en la hoja"],
         ["escribir un rasgo sin acción que lo apoye", "poner el lugar en la línea del tiempo"],
         "Pide que subraye en el texto la frase que apoya su rasgo."),
    "Copia los ocho adjetivos de rasgos y dibuja junto a cada uno una cara que lo represente.",
    "Describe con la forma «personaje + rasgo + because + acción» a un personaje de una serie o libro que conozcas.",
)

# ============================================================ clase 3: trama y problema-solución
LIA = "«In the harbor of Valparaíso, a young painter named Lía had no money for paint. She asked the fishermen for old, unused boat paint. At first they laughed, but she painted a small boat for them. Soon every boat in the harbor wanted a new color, and Lía had work for the whole year.»"
GLIA = "(harbor = puerto; painter = pintora; paint = pintura; fishermen = pescadores; unused = sin usar; laughed = se rieron; color = color; whole year = año completo)"
BUS = "«Elena always took the 7:15 bus to school. One Monday the bus did not come, so she was afraid to be late. She asked a neighbor, and he lent her his bike. She arrived just in time.»"
GBUS = "(neighbor = vecino; lent = prestó; bike = bicicleta; just in time = justo a tiempo; late = tarde)"
WALL = "«The school wall was gray and sad. Students painted a big sea with fish and waves. Now people stop and smile when they pass.»"
GWALL = "(wall = muro; waves = olas; pass = pasar)"
GUIT = "«Tomas wanted to learn the guitar, but he did not have one. He cleaned neighbors' gardens for three Saturdays. Then he bought a second-hand guitar. Now he plays every afternoon.»"
GGUIT = "(guitar = guitarra; cleaned = limpió; gardens = jardines; second-hand = de segunda mano; plays = toca)"
LUNCH = "«Camila forgot her lunch money. A classmate shared her sandwich, but Camila was still hungry. After school she ate a big dinner.»"
GLUNCH = "(forgot = olvidó; lunch money = dinero del almuerzo; shared = compartió; still = todavía; dinner = cena)"
WELL = "«The village well was empty in March. People walked two hours to a river. Finally a boy named Rubén noticed that the water in the old stone channel was not moving. They cleaned the channel and the well filled again.»"
GWELL = "(well = pozo; empty = vacío; channel = canal; noticed = notó; cleaned = limpiaron; filled = se llenó)"
SHOP = "«Joaquín's grandmother had a small shop in Castro. When a big supermarket opened, fewer people came. Joaquín made a simple website with photos of her homemade jam. Soon people from other cities ordered it.»"
GSHOP = "(shop = tienda; fewer = menos; website = sitio web; homemade jam = mermelada casera; ordered = pidieron)"
FRAN = "«Fran is the goalkeeper of her school team, but she is afraid of penalty shots. Before the final, her coach shows her three small exercises. Fran practices them every day for a week. In the final, she stops one penalty and the team wins.»"
GFRAN = "(goalkeeper = arquera; penalty shots = tiros penales; coach = entrenador; stops = ataja; wins = gana)"

lesson(
    OA, 3, MAT,
    "Aprenderé a ordenar una historia en inicio, desarrollo y final, y a encontrar su problema y su solución. Sirve para resumir lo que pasó y explicar cómo se resolvió.",
    ["Sé reconocer personajes y entorno.", "Conozco first, then y finally."],
    [
        "La trama (plot) es la serie de sucesos de una historia, contada en orden. Tiene tres partes: el inicio (beginning) presenta a los personajes, el entorno y, casi siempre, el problema; el desarrollo (development) muestra lo que los personajes hacen para resolverlo; y el final (end) cuenta cómo termina todo. El problema (problem) es lo que impide que el personaje consiga algo. La solución (solution) es lo que lo resuelve.",
        "Hay palabras que ayudan. Para el problema: but (pero), cannot (no puede), no money, afraid (con miedo), did not come. Para el desarrollo y el cambio: so (así que), then (luego), at first (al principio). Para la solución y el final: finally (por fin), soon (pronto), now (ahora), in the end (al final). A veces la solución es parcial (partial solution): resuelve solo una parte, y el personaje sigue con una dificultad.",
        "Para resumir, completa tres frases: al inicio hay este problema; en el desarrollo el personaje hace esto; al final ocurre esto. Pregunta también qué causó la solución: la acción concreta que cambió la situación. Si ordenas las oraciones por tiempo, no mezcles el final con el desarrollo.",
    ],
    [("plot", "trama"), ("beginning", "inicio"), ("development", "desarrollo"), ("end", "final"), ("problem", "problema"), ("solution", "solución"), ("partial solution", "solución parcial"), ("cause", "causa")],
    [
        ("Resumir la trama", f"Texto: {LIA} {GLIA} ¿Cuál es el inicio, el desarrollo y el final?",
         ["Inicio: Lía no tiene dinero para pintura.", "Desarrollo: pide pintura vieja a los pescadores, se ríen, pero ella pinta un bote pequeño.", "Final: todos los botes quieren un color nuevo y tiene trabajo por un año."], "Inicio: sin dinero para pintura. Desarrollo: pinta un bote. Final: tiene trabajo por un año"),
        ("Ordenar tres oraciones", "Ordena según la trama: 1) Everyone clapped. 2) Iván was afraid to sing in front of the class. 3) He took a deep breath and started the song. (clapped = aplaudieron; afraid = con miedo; deep breath = respiración profunda)",
         ["El inicio presenta el problema: el miedo de Iván.", "El desarrollo es lo que hace: respira y empieza la canción.", "El final es el resultado: todos aplauden."], "2, 3, 1"),
    ],
    [
        ("Decir que la solución es el hecho que ocurre al inicio.", "Al inicio suele estar el problema; la solución llega en el desarrollo o el final.", "Busca el cambio que resuelve la dificultad."),
        ("Mezclar la consecuencia del problema con la solución, como «she was late».", "Llegar tarde es lo que pasa si no se resuelve, no lo que lo resuelve.", "Pregunta qué acción arregló la situación."),
    ],
    [
        mc("La trama (plot) es", "la serie de sucesos de la historia, en orden", ["el lugar donde ocurre", "la idea general del texto"], "Plot es el orden de los sucesos."),
        mc("¿En qué parte de la trama suele aparecer la solución?", "En el final", ["En el título", "En la primera oración siempre"], "La solución llega cuando el personaje resuelve el problema, casi siempre hacia el final."),
        mc("En «I wanted to swim, but the pool was closed», la palabra but introduce", "un problema", ["una solución", "un lugar"], "But muestra una dificultad que impide lo que se quería hacer."),
    ],
    [
        mc(f"Lee: {BUS} {GBUS} ¿Cuál es el problema?", "The bus did not come", ["Elena lent her bike", "Elena arrived just in time"], "El problema es que el bus no llegó."),
        mc(f"Lee: {BUS} {GBUS} ¿Cuál es la solución?", "A neighbor lent her his bike", ["Elena took the 7:15 bus", "Elena was afraid"], "La bicicleta prestada resuelve cómo llegar."),
        mc(f"Lee: {BUS} {GBUS} ¿Cuál es el final de la historia?", "She arrived just in time", ["She asked a neighbor", "The bus did not come"], "Es el resultado, la última oración."),
    ],
    [
        mc(f"Lee: {GUIT} {GGUIT} ¿Cuál es el problema?", "Tomas wanted a guitar but did not have one", ["Tomas cleaned gardens", "Tomas plays every afternoon"], "La palabra but anuncia el problema: quiere una guitarra y no la tiene."),
        mc(f"Lee: {GUIT} {GGUIT} ¿Cuál es el desarrollo, lo que hace Tomas para resolverlo?", "He cleaned neighbors' gardens for three Saturdays", ["He bought a second-hand guitar", "He plays every afternoon"], "Limpiar jardines es lo que hace durante el desarrollo para juntar dinero."),
        mc(f"Lee: {GUIT} {GGUIT} ¿Qué palabra marca el paso del esfuerzo a la solución?", "Then", ["But", "Did not"], "Then anuncia el siguiente suceso: compra la guitarra."),
    ],
    [
        mc(f"Pía dice que el cuento de la guitarra termina «cuando Tomas limpia los jardines». ¿Es correcta? {GUIT}", "No: el final es que compra la guitarra y toca todas las tardes", ["Sí, porque limpiar jardines es lo último que se cuenta", "No: el final es que no tenía guitarra"], "Limpiar jardines es el desarrollo; el final muestra el resultado."),
        mc(f"Lee: {LUNCH} {GLUNCH} ¿La solución resuelve todo el problema?", "No: es parcial, porque Camila sigue con hambre", ["Sí, porque Camila olvidó su dinero", "Sí, porque cenó en la tarde"], "Compartir el sándwich ayuda, pero la historia dice que seguía con hambre."),
    ],
    [
        mc(f"Lee: {WELL} {GWELL} ¿Qué acción causó la solución?", "They cleaned the old stone channel", ["People walked two hours to a river", "The well was empty in March"], "Después de limpiar el canal, el pozo se llenó otra vez."),
        mc(f"Lee: {BUS} {GBUS} Elena resume la historia así: «Problem: the bus. End: she is late.» ¿Qué parte de su resumen falla frente al texto?", "El final: llegó justo a tiempo", ["El problema: el bus no vino", "No falla nada"], "El texto termina con She arrived just in time, no tarde."),
    ],
    [mc(f"En el club de lectura debes elegir el mejor resumen de este microcuento: {SHOP} {GSHOP}", "Problema: llegan menos clientes. Solución: vender la mermelada por un sitio web", ["Problema: la abuela vende mermelada. Solución: cerrar la tienda de Castro", "Problema: llegan menos clientes. Solución: abrir otro supermercado en la ciudad"], "El supermercado trajo menos clientes y Joaquín abrió una vía nueva de venta.")],
    [
        mc("¿Qué palabra anuncia una solución?", "Finally", ["Cannot"], "Finally marca que algo se resuelve; cannot muestra un problema."),
        mc("¿Cuál es la palabra que comúnmente anuncia un problema?", "But", ["Soon", "Now"], "But introduce una dificultad."),
        ("¿Cuáles son las tres partes básicas de la trama?", "Inicio, desarrollo y final", "Son beginning, development y end."),
    ],
    task(f"Lee: {FRAN} {GFRAN} En tu hoja escribe tres líneas: inicio, desarrollo y final, y subraya el problema y la solución. Di además si la solución es total o parcial.",
         "Inicio: Fran es arquera y le tiene miedo a los penales. Desarrollo: su entrenador le muestra ejercicios y ella practica una semana. Final: ataja un penal en la final y gana. Solución total.",
         ["escribe las tres partes en orden", "señala claramente el problema y la solución", "justifica si la solución es total o parcial"],
         ["tres líneas y dos subrayados en la hoja"],
         ["mezclar el final con el desarrollo", "decir que el problema es el partido y no el miedo"],
         "Pide que cambie el final para que la solución sea parcial y explique qué cambiaría."),
    "Copia la lista de palabras que anuncian problema y solución y encierra en un color cada grupo.",
    "Cuenta en tres frases en español la trama de una película que conozcas: inicio, desarrollo y final.",
)

# ============================================================ clase 4: brecha de información con tarjetas
POT_A = "«Card A: Long ago, a potter named Inés lived in a village by a river. She made beautiful jars, but every jar broke in the oven.»"
POT_B = "«Card B: An old woman told her, The river clay is too wet. Inés dried the clay in the sun for three days. This time the jars did not break.»"
GPOT = "(potter = alfarera; jars = jarras; broke = se rompían; oven = horno; clay = arcilla; wet = húmeda; dried = secó)"
LEO_A = "«Card A: Leo opened the box and shouted.»"
LEO_B = "«Card B: The box was full of paper birds. Leo smiled.»"
GAP_A = "«Card A: Gaby wanted to join the school choir. At the audition, she forgot the first line of the song and stopped.»"
GAP_B = "«Card B: The teacher said, Start again and look at me. Gaby breathed and sang the whole song. She joined the choir.»"
GGAP = "(choir = coro; audition = audición; forgot = olvidó; line = verso; stopped = se detuvo; breathed = respiró; whole = completa)"
ROB_A = "«Card A: Fabi's science project was a small robot. On the fair day, the robot did not move.»"
ROB_B = "«Card B: Fabi saw that the batteries were upside down. She turned them the right way, and the robot rolled across the table.»"
GROB = "(project = proyecto; fair = feria; batteries = pilas; upside down = al revés; rolled = rodó)"
VALE_A = "«Card A: Vale packs her backpack for the school camp. She cannot find her sleeping bag.»"
VALE_B = "«Card B: Her cousin has two sleeping bags. He gives her the green one.»"
GVALE = "(packs = arma; backpack = mochila; camp = campamento; sleeping bag = saco de dormir; gives = le da)"
LAKE_A = "«Card A: Long ago, the lake had no fish. The people were hungry.»"
LAKE_B = "«Card B: A bird dropped a shining seed into the water. The next morning, there were fish in the lake.»"
GLAKE = "(lake = lago; hungry = con hambre; bird = pájaro; dropped = dejó caer; shining = brillante; seed = semilla)"

lesson(
    OA, 4, MAT,
    "Aprenderé a unir dos tarjetas con partes distintas de una historia y a hacer preguntas para completar lo que falta. Sirve para trabajar en pareja sin inventar datos.",
    ["Sé reconocer problema, desarrollo y solución.", "Conozco preguntas con what, who, where y why."],
    [
        "En una brecha de información (information gap) cada persona tiene una parte de la historia y la otra parte la tiene su compañero (partner). Una tarjeta (card) puede traer el inicio y la otra el final. Para armar la historia completa, lee tu tarjeta, escucha o lee la del compañero y une los datos en orden: problema, intento y solución.",
        "Para pedir lo que falta se usan preguntas. What happened next? es ¿qué pasó después? Why did it happen? es ¿por qué pasó? Where is the story? es ¿dónde ocurre? Who helps? es ¿quién ayuda? Para confirmar, puedes decir: Do you mean that…? (¿quieres decir que…?). Si algo no se entiende, pide que lo repitan con Can you repeat that, please?",
        "Si las dos tarjetas dicen cosas distintas sobre el mismo dato (por ejemplo, un día), hay una contradicción (contradiction): no elijas la que más te gusta. Vuelve a leer, pregunta de nuevo y comprueba cuál calza con el resto de la historia. Si un dato no está en ninguna tarjeta, escribe que no se sabe; no lo inventes.",
    ],
    [("information gap", "brecha de información: cada uno tiene una parte"), ("card", "tarjeta"), ("partner", "compañero o compañera de trabajo"), ("What happened next?", "¿Qué pasó después?"), ("Why did it happen?", "¿Por qué pasó?"), ("contradiction", "contradicción: dos datos que no pueden ser ciertos a la vez"), ("Can you repeat that, please?", "¿Puedes repetirlo, por favor?")],
    [
        ("Unir dos tarjetas", f"Tarjetas: {POT_A} {POT_B} {GPOT} ¿Cuál es el problema y cómo se resuelve?",
         ["La tarjeta A da el problema: las jarras se rompen en el horno.", "La tarjeta B da la causa y la solución: la arcilla estaba húmeda, así que la seca al sol tres días.", "Al unir ambas, el resultado es que las jarras ya no se rompen."], "Problema: las jarras se rompen en el horno. Solución: secar la arcilla al sol tres días"),
        ("Preguntar lo que falta", f"Tienes solo la tarjeta A: {LEO_A} Tu compañero tiene la B. ¿Qué pregunta te sirve para completar el dato que falta?",
         ["La tarjeta A dice que Leo abrió la caja y gritó, pero no dice qué había adentro.", "Lo que falta es el contenido de la caja.", "Pregunto: What was inside the box?"], "What was inside the box? (¿Qué había dentro de la caja?)"),
    ],
    [
        ("Rellenar un dato que ninguna tarjeta trae, como el nombre del colegio.", "Se inventa información que no está en las tarjetas.", "Escribe que no se sabe o pregunta a tu compañero."),
        ("Usar solo tu tarjeta y contar el final sin leer la del compañero.", "Una tarjeta sola no tiene todos los datos.", "Lee las dos y recién entonces escribe la historia."),
    ],
    [
        mc("En una brecha de información (information gap), cada persona tiene", "una parte de los datos", ["todos los datos", "ningún dato"], "Por eso hay que unir las partes."),
        mc("What happened next? significa", "¿Qué pasó después?", ["¿Dónde estás?", "¿Quién lo hizo?"], "What happened next? pide el suceso que sigue."),
        mc("¿Qué pregunta pide el lugar de una historia?", "Where does the story happen?", ["Who is the main character?", "Why did it happen?"], "Where significa dónde."),
    ],
    [
        mc(f"Lee las tarjetas: {GAP_A} {GAP_B} {GGAP} ¿Qué problema muestra la tarjeta A?", "Gaby forgot the first line of the song and stopped", ["Gaby sang the whole song", "Gaby joined the choir"], "El problema está en la audición: olvida el primer verso."),
        mc(f"Lee las tarjetas: {GAP_A} {GAP_B} {GGAP} ¿Qué hace la profesora para ayudarla, según la tarjeta B?", "Le dice que empiece otra vez y la mire", ["Le dice que se vaya", "Canta en su lugar"], "La tarjeta B dice Start again and look at me."),
        mc(f"Lee las tarjetas: {GAP_A} {GAP_B} {GGAP} ¿Cuál de las dos tarjetas contiene el final?", "La tarjeta B, porque Gaby entra al coro", ["La tarjeta A, porque habla del audition", "Ninguna, porque falta el final"], "La última oración de la tarjeta B dice She joined the choir."),
    ],
    [
        mc(f"Tienes solo la tarjeta A: {ROB_A} {GROB} ¿Qué pregunta te ayuda a obtener la causa?", "Why did the robot not move?", ["Where is the fair?", "Who is Fabi?"], "La causa falta en la tarjeta A y se pide con why."),
        mc(f"Lee las tarjetas: {ROB_A} {ROB_B} {GROB} ¿Qué oración une bien las dos tarjetas?", "The robot did not move because the batteries were upside down, so Fabi turned them the right way", ["The robot did not move because the fair was canceled, so Fabi went home", "The robot moved from the beginning, so Fabi won"], "Combina el problema (A) y la solución (B) sin agregar datos."),
        mc(f"Tu compañero dice: «Fabi's robot was broken.» {ROB_A} {ROB_B} ¿Qué dato lo contradice?", "Fabi turned the batteries the right way and the robot rolled", ["The robot was small", "The fair was on a table"], "Si el robot funciona al arreglar las pilas, no estaba roto."),
    ],
    [
        mc(f"Dos resúmenes de las tarjetas: {GAP_A} {GAP_B} Resumen 1: «Gaby joined the choir after trying again.» Resumen 2: «Gaby joined the choir because her friend sang for her.» ¿Cuál tiene evidencia en las tarjetas?", "El resumen 1, porque la profesora le dice que empiece de nuevo y ella canta toda la canción", ["El resumen 2, porque las dos tarjetas hablan de una amiga", "Ninguno, porque falta el final"], "En las tarjetas no hay ninguna amiga; Gaby canta ella misma."),
        mc("La tarjeta A dice que la fiesta es el viernes y la tarjeta B dice que es el sábado. ¿Qué debes hacer?", "Pedir que repitan el dato, releer y ver cuál calza con el resto de la historia", ["Elegir el día que te gusta más", "Ignorar las dos tarjetas"], "Una contradicción se resuelve volviendo a los datos, no eligiendo al azar."),
    ],
    [
        mc(f"Lee: {VALE_A} {VALE_B} {GVALE} ¿Qué dato no aparece en ninguna de las dos tarjetas?", "El nombre del campamento", ["Qué no encuentra Vale", "Quién tiene dos sacos de dormir"], "Ninguna tarjeta nombra el campamento; los otros datos sí están."),
        mc(f"Lee: {VALE_A} {VALE_B} {GVALE} ¿Qué oración une bien las ideas con but y so?", "Vale could not find her sleeping bag, but her cousin had two, so he gave her the green one", ["Vale found her sleeping bag, so her cousin had two, but she lost it", "Vale had two sleeping bags, but her cousin could not find one"], "But presenta el obstáculo y so presenta lo que ocurre como resultado."),
    ],
    [mc(f"En un taller de lectura, tú tienes {LAKE_A} {GLAKE} y tu compañero tiene {LAKE_B} ¿Qué pregunta debes hacerle para saber cómo se solucionó el problema de la gente?", "What solved the people's problem?", ["Where is the bird now?", "Who was hungry long ago?"], "Lo que falta en tu tarjeta es qué resolvió el hambre.")],
    [
        mc("Si un dato no está en ninguna tarjeta, ¿qué haces?", "Escribo que no se sabe", ["Lo invento para completar la historia"], "No se rellenan datos sin evidencia."),
        mc("¿Qué frase sirve para pedir que repitan algo?", "Can you repeat that, please?", ["What happened next?", "Where is the story?"], "Esa frase pide repetir; las otras piden otros datos."),
        ("Escribe en español qué significa «partner» en una actividad de lectura en pareja.", "Compañero o compañera de trabajo", "Partner es quien tiene la otra tarjeta."),
    ],
    task(f"Con tu compañero(a) o con una persona de tu casa, usa estas tarjetas: {LAKE_A} {LAKE_B} {GLAKE} En tu hoja escribe: (1) una pregunta en inglés que haría quien tiene solo la tarjeta A, (2) un resumen de dos líneas que una las tarjetas, (3) un dato que no se sabe.",
         "(1) What happened next? (2) Long ago the lake had no fish and the people were hungry. A bird dropped a shining seed, and the next morning there were fish. (3) No se sabe de qué lugar eran las personas.",
         ["la pregunta es adecuada para obtener lo que falta", "el resumen usa datos de las dos tarjetas", "no inventa el dato que falta"],
         ["tres respuestas escritas en la hoja"],
         ["resumir con datos que no están en las tarjetas", "preguntar algo que ya dice la propia tarjeta"],
         "Pide que subraye en cada tarjeta la frase que usó."),
    "Copia las siete frases del vocabulario y escribe su traducción debajo.",
    "Escribe en español dos tarjetas para una historia de tres líneas: una con el problema y otra con la solución.",
)

# ============================================================ clase 5: palabras clave, expresiones idiomáticas y vocabulario temático
CLIMB = "«At first, the climb was a piece of cake. But after two hours the trail was steep and Marco was out of breath. At last they reached the summit, and the whole valley looked tiny below them.»"
GCLIMB = "(climb = subida; trail = sendero; steep = empinado; out of breath = sin aliento; reached = llegaron a; summit = cima; valley = valle; tiny = diminuto)"
CAMP = "«On the first day of camp nobody talked. Then Rosa told a funny joke to break the ice, and everyone laughed.»"
GCAMP = "(camp = campamento; joke = chiste; laughed = rieron)"
MARKET = "«Sunday in the market of Temuco. At the stall, customers asked for the price of apples. Today is a bargain, said the seller, a kilo for one thousand pesos. Cristina went there once in a blue moon, but today she bought two kilos.»"
GMARKET = "(stall = puesto; customers = clientes; price = precio; bargain = ganga; seller = vendedor; once in a blue moon = muy rara vez)"
TEST = "«Ana felt under the weather on Friday, but she had a test on Monday. She decided to hit the books on Saturday morning. By Monday she was well again.»"
GTEST = "(felt = se sintió; test = prueba; decided = decidió; well = bien)"
PARTY = "«Please do not spill the beans, whispered Tito. It is a surprise party for Leo. I will not tell anybody, said Dani.»"
GPARTY = "(whispered = susurró; surprise party = fiesta sorpresa; anybody = nadie)"
STORM = "«It was raining cats and dogs when the bus stopped. Everybody ran to the shelter and waited ten minutes.»"
GSTORM = "(raining cats and dogs = llueve a cántaros; shelter = refugio)"
MUSEUM = "«School trip to the museum: the tickets do not cost an arm and a leg. They are only two thousand pesos for students.»"
GMUSEUM = "(trip = salida; museum = museo; tickets = entradas; cost an arm and a leg = costar un ojo de la cara)"

lesson(
    OA, 5, MAT,
    "Aprenderé a usar palabras clave, expresiones idiomáticas y vocabulario temático para entender un texto literario sin traducir palabra por palabra. Sirve para leer un cuento por mi cuenta y entender el sentido completo.",
    ["Sé reconocer tema, personajes, entorno y trama.", "Conozco first, then y finally."],
    [
        "Las palabras clave (key words) son las que más ayudan a entender un texto; suelen repetirse o estar relacionadas con el tema. El vocabulario temático (thematic vocabulary) es un grupo de palabras de un mismo campo: climb, trail, steep y summit son del campo «montaña»; stall, customers, price y bargain son del campo «mercado». Si reconoces el campo, puedes deducir el significado de una palabra nueva.",
        "Una expresión idiomática (idiom) es un grupo de palabras cuyo significado no es la suma de cada palabra. A piece of cake no es un trozo de torta, sino algo muy fácil. Break the ice es romper el hielo: hacer que un grupo nervioso se relaje. Otras expresiones frecuentes: under the weather (con mal cuerpo, un poco enfermo), hit the books (ponerse a estudiar), once in a blue moon (muy rara vez), spill the beans (contar un secreto), it is raining cats and dogs (llueve a cántaros) y cost an arm and a leg (costar muchísimo).",
        "Cuando una expresión no tiene sentido literal, no la traduzcas palabra por palabra. Lee la oración completa, mira el contexto (las palabras y hechos alrededor) y pregúntate qué significado calza con la historia. Después comprueba tu idea releyendo: ¿tiene sentido si lo reemplazo por mi significado?",
    ],
    [("key words", "palabras clave"), ("at last", "por fin"), ("thematic vocabulary", "vocabulario temático: palabras de un mismo campo"), ("idiom", "expresión idiomática"), ("a piece of cake", "muy fácil"), ("break the ice", "romper el hielo"), ("under the weather", "con mal cuerpo, un poco enfermo"), ("hit the books", "ponerse a estudiar"), ("once in a blue moon", "muy rara vez"), ("spill the beans", "contar un secreto"), ("cost an arm and a leg", "costar muchísimo"), ("context", "contexto: lo que rodea a una palabra")],
    [
        ("Campo temático y expresión", f"Texto: {CLIMB} {GCLIMB} ¿Qué campo temático forman climb, trail, steep y summit y qué significa «a piece of cake» aquí?",
         ["Climb, trail, steep y summit son palabras de la montaña.", "En At first, the climb was a piece of cake la expresión no habla de comida.", "Por el contexto (después, but ... steep), significa que al principio era muy fácil."], "Campo: montaña. A piece of cake: muy fácil"),
        ("Entender una expresión por contexto", f"Texto: {CAMP} {GCAMP} ¿Qué significa «to break the ice» aquí?",
         ["Nadie hablaba el primer día.", "Rosa cuenta un chiste y todos ríen.", "Entonces romper el hielo es hacer que el grupo se relaje y empiece a hablar."], "Hacer que el grupo se relaje y se comunique"),
    ],
    [
        ("Traducir «once in a blue moon» como «una vez en una luna azul» y quedarse ahí.", "Se traduce palabra por palabra y no se usa el sentido de la expresión.", "Pregunta qué significa en la oración: muy rara vez."),
        ("Pensar que una palabra desconocida impide entender todo el texto.", "No se usa el contexto ni el campo temático.", "Mira las palabras que la rodean y comprueba si calza con la historia."),
    ],
    [
        mc("Las palabras clave (key words) de un texto son", "las que más ayudan a entender el texto", ["las más largas", "las que están al final"], "Se relacionan con el tema y a veces se repiten."),
        mc("Una expresión idiomática (idiom) es un grupo de palabras", "cuyo significado no se obtiene sumando cada palabra", ["que siempre rima", "que es un nombre propio"], "Su sentido es figurado."),
        mc("At last significa", "por fin", ["al principio", "nunca"], "At last marca que algo se logra después de esperar."),
    ],
    [
        mc(f"Lee: {TEST} {GTEST} ¿Qué significa «under the weather» aquí?", "Un poco enferma", ["Bajo la lluvia", "Con mucho trabajo"], "Ana tiene una prueba y el texto dice que el lunes ya estaba bien otra vez."),
        mc(f"Lee: {TEST} {GTEST} ¿Qué significa «hit the books» aquí?", "Estudiar con esfuerzo", ["Golpear los libros", "Comprar libros"], "Tiene una prueba el lunes y estudia el sábado."),
        mc(f"Lee: {PARTY} {GPARTY} ¿Por qué Tito dice «do not spill the beans»?", "Porque quiere que Dani guarde el secreto de la fiesta", ["Porque tiene hambre", "Porque quiere cocinar"], "Se trata de una fiesta sorpresa que no debe contarse."),
    ],
    [
        mc(f"Lee: {MARKET} {GMARKET} ¿A qué campo temático pertenecen stall, customers, price y seller?", "El mercado", ["La escuela", "La montaña"], "Todas son palabras de comprar y vender."),
        mc(f"Lee: {MARKET} {GMARKET} ¿Qué significa «bargain» aquí?", "Un buen precio", ["Un puesto grande", "Un kilo de manzanas"], "El vendedor dice que el kilo cuesta mil pesos y lo llama bargain."),
        mc(f"Lee: {MARKET} {GMARKET} ¿Qué significa «once in a blue moon»?", "Muy rara vez", ["Todas las noches", "Cada fin de semana"], "El contraste es que hoy Cristina sí compró."),
    ],
    [
        mc(f"Un lector traduce «hit the books» de este texto como «golpear los libros»: {TEST} ¿Qué pista del contexto muestra que no es literal?", "Ana tiene una prueba el lunes y lo hace el sábado en la mañana", ["Los libros son pesados", "Ana está en casa"], "La prueba explica que el verbo se refiere a estudiar."),
        mc(f"Lee: {STORM} {GSTORM} Un compañero dice que llovían gatos y perros. ¿Cuál es la mejor corrección?", "Es una expresión: llueve muchísimo", ["Tiene razón, porque hay animales en la calle", "Significa que hay poca lluvia"], "Todos corren al refugio y esperan diez minutos: la lluvia es fuerte."),
    ],
    [
        mc("Completa con la expresión que calza: «I see my cousins ______; they live very far away.»", "once in a blue moon", ["under the weather", "hit the books"], "Si viven lejos, los ve muy rara vez."),
        mc("¿Qué oración usa bien una expresión idiomática?", "It is raining cats and dogs, so take an umbrella", ["It is raining cats and dogs, so we saw many pets in the street", "He spilled the beans, so he cooked dinner"], "En la primera se usa con su sentido: llueve muchísimo."),
    ],
    [mc(f"Te entregan un volante de una salida del colegio: {MUSEUM} {GMUSEUM} ¿Qué dice sobre el precio?", "Que las entradas no son carísimas, pues cuestan solo dos mil pesos para estudiantes", ["Que las entradas son carísimas", "Que las entradas son gratuitas"], "Do not cost an arm and a leg niega que sean muy caras y da el precio.")],
    [
        mc("Si dices «The test was a piece of cake», quieres decir que la prueba fue", "muy fácil", ["muy dulce", "muy larga"], "A piece of cake es una forma de decir que algo es fácil."),
        ("Escribe en inglés la expresión que significa «contar un secreto».", "Spill the beans", "Es la expresión idiomática para revelar un secreto."),
        ("Escribe en español qué es el vocabulario temático (thematic vocabulary).", "Un grupo de palabras de un mismo campo", "Reconocer el campo ayuda a deducir palabras nuevas."),
    ],
    task("Lee este texto: «My cousin Lalo is a clown at birthday parties. He sees me once in a blue moon because he works every weekend. Last Sunday he felt under the weather, but he still came to break the ice at a very shy party.» (clown = payaso; works = trabaja; weekend = fin de semana; shy = tímido). En tu hoja, escribe el significado en español de once in a blue moon, under the weather y break the ice, y subraya una pista de contexto para cada una.",
         "Once in a blue moon: muy rara vez (pista: he works every weekend). Under the weather: un poco enfermo (pista: he still came). Break the ice: hacer que el grupo se relaje (pista: a very shy party).",
         ["da un significado sensato para las tres expresiones", "no traduce palabra por palabra", "subraya una pista de contexto para cada una"],
         ["tres significados y tres subrayados en la hoja"],
         ["traducir literalmente", "dar el mismo significado a dos expresiones distintas"],
         "Pide que explique por qué su significado calza con la historia."),
    "Copia las siete expresiones idiomáticas del vocabulario con su significado y dibuja una escena para tres de ellas.",
    "Escribe en español una situación de tu vida diaria que podrías describir con «a piece of cake» y otra con «under the weather».",
)
