"""Cuaderno del estudiante, 8.º básico Inglés (oficial): IN08 OA 11, comprensión de textos literarios.

Los textos en inglés son originales, breves y llevan glosario en español dentro del enunciado. Cada término se enseña
en la clase antes de usarlo. Sin audio externo: todo lo que hay que leer está escrito en el enunciado.
Los títulos de clase del plan son genéricos (propósito, evidencia, estrategia, brecha de información, respuesta
independiente): aquí se aplican al tema, los personajes, el entorno y la trama, el problema y su solución, y las
palabras y expresiones clave.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "IN08 OA 11"


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


# ============================================================ clase 1: tipos de texto literario y tema
T1 = "Tomas is the new student at a school in Valdivia. At break he sits alone. A girl named Ema offers him half of her sandwich and asks him to play. Soon Tomas has three new friends. He smiles all day."
G_T1 = "(break = recreo; offers = ofrece; half = mitad; soon = pronto)"
P1 = "Drop after drop falls on the stone. / The stone is hard, the drop is small. / Day after day, the drop keeps going, / And one day, the stone has a hole."
G_P1 = "(drop = gota; hard = duro; keeps going = sigue; hole = hoyo)"
C1 = "Panel 1: Gaby looks at her broken pencil case. Panel 2: Her classmate Rolo says, 'Take mine. I have two.' Panel 3: Gaby smiles and says, 'Thanks! Tomorrow I will bring you a sweet.'"
G_C1 = "(broken = roto; take = toma; sweet = dulce)"
N1 = "Captain Rey sails on the ship Albatross for ninety days. Food is low and the crew is angry. The captain shares his own bread and talks with each sailor. The crew trusts him again."
G_N1 = "(sails = navega; crew = tripulación; low = escasa; shares = comparte; trusts = confía en)"

lesson(
    OA, 1,
    "Los textos, el poema y la tira cómica escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a reconocer qué tipo de texto literario leo y a decir cuál es su tema, es decir, su idea general. Sirve para entender qué quiere comunicar un poema, una tira cómica o un cuento en inglés.",
    ["Sé leer textos breves en inglés con ayuda de un glosario.", "Conozco palabras como character, setting y plot."],
    [
        "Un texto literario cuenta o imagina algo. Hay cuatro tipos frecuentes: el poema o la canción (poem, song), con versos y a veces rima; la tira cómica (comic strip), con viñetas (panels); el cuento breve (short story); y la novela adaptada (adapted novel), una novela larga reescrita con lenguaje más simple. Fíjate en el formato: versos, viñetas o párrafos.",
        "El asunto (topic) es de qué trata el texto, en una o dos palabras: friendship, the sea, school. El tema (theme) es la idea general o el mensaje: una oración completa que sirve para muchas historias, como «Sharing makes life better». Un detalle (detail) es un dato pequeño, como el nombre de una calle. El tema no es un detalle ni solo el asunto.",
        "Para encontrar el tema, mira tres pistas: el título, lo que se repite y cómo termina el texto. Pregunta: ¿qué aprende el personaje? ¿qué pasa gracias a lo que hace? Después escribe una oración que no dependa de los nombres propios. Si tu oración solo funciona para ese cuento (por ejemplo «Tomas is new»), todavía es un detalle y no un tema.",
    ],
    [("poem / song", "poema / canción"), ("comic strip", "tira cómica"), ("panel", "viñeta"), ("short story", "cuento breve"), ("adapted novel", "novela adaptada"), ("topic", "asunto: de qué trata, en pocas palabras"), ("theme", "tema: idea general o mensaje"), ("detail", "detalle")],
    [
        ("Encontrar el tema de un cuento breve", "Texto: «Every morning, old Don Hugo feeds the street dogs near the market in Talca. 'They have no home, but they have me,' he says. Soon children bring water and blankets too.» (feeds = da de comer; street dogs = perros callejeros; blankets = frazadas) ¿Cuál es el asunto y cuál el tema?",
         ["Asunto: de qué trata en pocas palabras. Trata de ayudar a perros callejeros.", "Mira cómo termina: los niños también ayudan.", "El tema es una idea general: una acción amable puede inspirar a otros."], "Asunto: ayudar a perros callejeros. Tema: una acción amable puede inspirar a otros."),
        ("Reconocer el tipo de texto", "Texto: «Windy day, windy day, / my kite goes up and away. / I hold the string, I hold it tight, / and the sky is my delight.» (kite = volantín; string = hilo; tight = firme; delight = alegría) ¿Qué tipo de texto es?",
         ["Mira el formato: son cuatro versos cortos, no párrafos.", "Las palabras day y away riman, y tight y delight también.", "Los versos con rima forman un poema."], "Es un poema, con versos que riman."),
    ],
    [
        ("Decir que el tema es solo una palabra, como «friendship».", "Se confunde el asunto con el tema.", "Escribe una oración completa con una idea: «A kind gesture can start a friendship»."),
        ("Poner como tema un dato del texto, como «Tomas is the new student».", "Un detalle solo sirve para ese cuento.", "Pregúntate qué mensaje quedaría si cambiaras los nombres y el lugar."),
    ],
    [
        ("¿Cuál es un texto literario? a) A short story about a lost dog b) A school notice about a trip", "a", "El cuento imagina una historia; el aviso solo informa."),
        ("Un «comic strip» es un texto que se organiza en: a) viñetas b) estrofas", "a", "Comic strip es la tira cómica y cada cuadro es una viñeta (panel)."),
        ("En un texto, el «theme» es: a) la idea general o mensaje b) el nombre del personaje principal", "a", "El tema responde qué quiere comunicar el texto; el nombre es un detalle."),
    ],
    [
        (f"Lee: «{T1}» {G_T1} ¿Cuál es el asunto (topic) del texto? a) Friendship at a new school b) A school trip to the lake", "a", "Trata de un estudiante nuevo que hace amigos; no hay ningún paseo."),
        (f"Lee: «{T1}» {G_T1} ¿Qué oración expresa mejor el tema? a) A kind gesture can start a friendship b) Tomas is a new student", "a", "El tema es el mensaje general; la segunda opción es solo un detalle."),
        (f"Lee: «{P1}» {G_P1} ¿Qué tipo de texto es? a) A poem b) A news report", "a", "Tiene cuatro versos cortos y repite palabras como drop y day."),
    ],
    [
        (f"Lee: «{P1}» {G_P1} ¿Qué tema expresa mejor? a) Small steady efforts can achieve big changes b) Hard things never change c) Water is always cold", "a", "La gota pequeña sigue cayendo y al final abre un hoyo en la piedra dura."),
        (f"Lee la tira: «{C1}» {G_C1} ¿Cuál es el tema? a) Sharing is a way to help others b) Pencil cases are expensive c) You should never ask for help", "a", "Rolo comparte su estuche y Gaby promete devolver el gesto."),
        (f"Lee: «{N1}» {G_N1} ¿Qué oración es la mejor pista para el tema «A good leader shares and listens»? a) Captain Rey sails for ninety days b) The captain shares his own bread and talks with each sailor", "b", "Esa oración muestra cómo actúa el líder y por qué la tripulación vuelve a confiar."),
    ],
    [
        ("Texto: «Ana lives on one side of a river and Ben on the other. They cannot visit each other. One day each of them builds half of a wooden bridge. The halves meet in the middle.» (bridge = puente; wooden = de madera; halves = mitades; meet = se encuentran) ¿Qué tema encaja mejor? a) Working together can solve a problem b) Friends must live far away from each other", "a", "Cada uno construye su mitad y así resuelven un problema que solos no podían."),
        (f"Un compañero dice que el poema «{P1}» tiene como tema «rain is wet». ¿Qué pista del poema muestra que esa idea es débil? a) The last line says that one day the stone has a hole b) The first line has the word drop", "a", "El final muestra el resultado de la constancia, que es el mensaje central."),
    ],
    [
        (f"Compara los dos textos. Texto 1: «{T1}» Texto 2: «{C1}» {G_T1} {G_C1} ¿Qué tema comparten? a) Small acts of kindness matter b) You must be strong to make friends", "a", "En ambos un gesto amable (compartir comida o un estuche) cambia la situación."),
        ("Mini cuento: «Ema loses the school race. She is sad, but she trains again and next year she wins.» (race = carrera; trains = entrena) ¿Qué tema expresa? a) Failure can lead to success if you keep trying b) Winning is the only important thing c) Training is boring", "a", "Perder la lleva a entrenar de nuevo y después gana."),
    ],
    [("Tu curso prepara una «Kindness Week». La profesora pide un texto cuyo tema sea «Small acts of kindness matter». Resumen 1: «A boy finds a coin and buys candy only for himself.» Resumen 2: «A girl gives her umbrella to a neighbour in the rain, and the neighbour thanks her with a smile.» (coin = moneda; neighbour = vecina) ¿Cuál resumen sirve? Escribe 1 o 2.", "2", "El segundo resumen muestra un gesto amable pequeño con efecto positivo.")],
    [
        ("En inglés, ¿cómo se llama cada cuadro de una tira cómica?", "Panel", "Panel es la viñeta."),
        ("Para encontrar el tema, ¿qué tres pistas se usan? Escribe: título, lo que se repite y ___.", "El final", "Cómo termina el texto muestra lo que aprendió el personaje."),
        ("¿Qué es mejor para un tema: una palabra o una oración completa?", "Una oración completa", "El tema es una idea o mensaje y necesita una oración."),
    ],
    task("Lee este mini cuento: «Pablo fixes bikes for free on Saturdays in his neighbourhood in Concepcion. One day a girl brings a broken bike. Pablo fixes it, and she brings him a sandwich. Next Saturday, five neighbours come to help him.» (fixes = arregla; for free = gratis; neighbourhood = barrio; neighbours = vecinos) En tu hoja anota: tipo de texto, asunto en dos palabras, tema en una oración y una oración del texto que lo apoye.", "Tipo: cuento breve. Asunto: arreglar bicicletas. Tema: ayudar sin esperar nada puede unir a una comunidad. Pista: «Next Saturday, five neighbours come to help him».", ["identifica el tipo de texto", "separa asunto (pocas palabras) de tema (oración)", "cita una pista exacta del texto"], ["ficha de cuatro líneas en la hoja"], ["escribir un nombre propio como tema", "escribir solo una palabra como tema"], "Pide que cambie los nombres y el lugar y compruebe que su tema sigue sirviendo."),
    "Copia la tabla de vocabulario y escribe un ejemplo de cada tipo de texto.",
    "Escribe en español el tema de un cuento que conozcas bien, en una oración que no use nombres propios.",
)

# ============================================================ clase 2: personajes, acciones y características
W2A = "Fabi is the goalkeeper of her team. Her team is losing 0-2. She does not give up: she shouts to her friends and stops two penalties. The match ends 2-2."
GW2A = "(goalkeeper = arquera; losing = perdiendo; give up = rendirse; shouts = grita; stops = ataja; penalties = penales)"
W2B = "Diego always arrives late, loses his keys and forgets his homework. But he laughs at his own mistakes and helps everyone clean the classroom."
GW2B = "(arrives = llega; late = tarde; keys = llaves; forgets = olvida; mistakes = errores; clean = limpiar)"
X2A = "Camila is the oldest sister. When her little brother cries at night, she tells him a story and gives him her blanket. In the morning she is tired, but she does not complain."
GX2A = "(oldest = mayor; cries = llora; blanket = frazada; complain = quejarse)"
X2B = "Jorge finds a wallet with money on the bus. Inside there is a card with a phone number. He calls the owner and returns the wallet."
GX2B = "(wallet = billetera; owner = dueño; returns = devuelve)"
X2C = "I am the cat that sleeps all day. / I do not run, I do not play. / If someone calls, I turn away. / Tomorrow? Maybe. Not today."
GX2C = "(sleeps = duerme; turn away = me doy vuelta; maybe = quizás)"
X2D = "Panel 1: Nico says, 'I know the answer!' Panel 2: He shouts it before the teacher finishes the question. Panel 3: It is wrong. Everybody laughs and Nico blushes."
GX2D = "(shouts = grita; finishes = termina; wrong = incorrecta; blushes = se sonroja)"

lesson(
    OA, 2,
    "Los textos, el poema y la tira cómica escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a describir a un personaje por lo que hace y por cómo es, y a señalar la evidencia en el texto. Sirve para entender por qué actúa así y para defender mi opinión con una oración del propio texto.",
    ["Sé reconocer personajes y entorno en un texto breve.", "Conozco adjetivos como happy, sad y kind."],
    [
        "Los personajes (characters) son quienes actúan en la historia. El personaje principal (main character) es el más importante; los personajes secundarios (secondary characters) lo acompañan. Para describirlos usa dos cosas: sus acciones (lo que hacen) y sus características (cómo son), que se dicen con adjetivos: brave (valiente), shy (tímido), generous (generoso), honest (honesto), lazy (flojo), caring (cariñoso), impatient (impaciente), determined (decidido, no se rinde), patient (paciente).",
        "Pocas veces el texto dice cómo es el personaje. Casi siempre debes deducirlo de sus acciones. Si alguien devuelve una billetera con dinero, es honest. Si alguien no abandona un objetivo difícil, es determined. Esto se llama inferir: usar las pistas del texto y lo que ya sabes para llegar a una idea que no está escrita con esas palabras.",
        "Una buena respuesta tiene tres partes: el personaje, la característica y la evidencia. Por ejemplo: «Rosa is generous because she gives her lunch to a friend». Usa because (porque) para unir la característica con la acción. La evidencia debe estar en el texto; si no hay ninguna pista, no puedes afirmarlo.",
    ],
    [("main character", "personaje principal"), ("secondary character", "personaje secundario"), ("trait", "característica del personaje"), ("brave", "valiente"), ("honest", "honesto"), ("lazy", "flojo, perezoso"), ("determined", "decidido, que no se rinde"), ("impatient", "impaciente"), ("caring", "cariñoso, que cuida a otros"), ("evidence", "evidencia: pista del texto")],
    [
        ("Deducir una característica desde una acción", f"Texto: «{W2A}» {GW2A} ¿Cómo es Fabi y qué evidencia lo muestra?",
         ["Mira sus acciones: grita a sus amigas y ataja dos penales.", "La frase clave es «She does not give up».", "Una persona que no se rinde cuando pierde es determined."], "Fabi es determined (decidida) porque no se rinde aunque va perdiendo."),
        ("Dos características en un mismo personaje", f"Texto: «{W2B}» {GW2B} Diego tiene un lado negativo y uno positivo. ¿Cuáles?",
         ["Lado negativo: llega tarde, pierde las llaves y olvida la tarea (disorganized, desordenado).", "Lado positivo: se ríe de sus errores y ayuda a limpiar.", "Es cheerful (alegre) y helpful (servicial)."], "Es desordenado, pero alegre y servicial."),
    ],
    [
        ("Decir «Camila is tired» como característica del personaje.", "Estar cansada es un estado de un momento; no muestra cómo es ella.", "Busca acciones repetidas o decisiones: ella cuida a su hermano sin quejarse."),
        ("Afirmar «Jorge is rich» porque encuentra dinero.", "El dinero que encuentra no es suyo; no hay pista de que sea rico.", "Usa la acción que sí aparece: devuelve la billetera, así que es honest."),
    ],
    [
        ("«Honest» significa: a) honesto b) flojo", "a", "Honest es la persona que dice la verdad y devuelve lo ajeno."),
        ("Elige la oración con evidencia: a) Rosa is generous because she gives her lunch to a friend b) Rosa is generous", "a", "La primera oración une la característica con una acción."),
        ("El personaje que más importa en una historia es el: a) main character b) secondary character", "a", "Main character es el principal."),
    ],
    [
        (f"Lee: «{X2A}» {GX2A} ¿Qué característica muestra que Camila no se queja pese al cansancio? a) She is patient b) She is selfish", "a", "Sigue tranquila y no se queja aunque está cansada."),
        (f"Lee: «{X2B}» {GX2B} Escribe en inglés una característica de Jorge que se deduzca de su acción: honest o lazy.", "honest", "Llama al dueño y le devuelve la billetera con el dinero."),
        (f"Lee el poema: «{X2C}» {GX2C} ¿Qué característica tiene el gato? a) Lazy b) Determined", "a", "Duerme todo el día, no corre ni juega y deja todo para mañana."),
    ],
    [
        (f"Lee la tira: «{X2D}» {GX2D} ¿Qué característica muestra Nico? a) Impatient b) Shy c) Caring", "a", "Responde antes de que la profesora termine la pregunta."),
        (f"Lee: «{X2A}» {GX2A} ¿Cuál es la mejor evidencia de que Camila es caring? a) She tells him a story and gives him her blanket b) She is the oldest sister", "a", "Esas acciones muestran cuidado; ser la mayor es solo un dato."),
        (f"Lee: «{X2B}» {GX2B} ¿Quién es el personaje principal de la historia? a) Jorge b) The owner of the wallet", "a", "Jorge hace todas las acciones; el dueño solo recibe la billetera y es secundario."),
    ],
    [
        ("Un compañero dice: «Fabi is shy because she shouts to her friends.» ¿Qué corrección es mejor? a) Gritar a sus amigas no muestra timidez, muestra que se anima y lidera b) Está bien, porque Fabi es la arquera", "a", "La acción contradice la característica que propone."),
        (f"Lee: «{W2B}» {GW2B} Un compañero afirma que Diego es lazy. ¿Qué dato del texto muestra lo contrario? a) He helps everyone clean the classroom b) He loses his keys", "a", "Ayuda a limpiar, una acción que no hace una persona floja."),
    ],
    [
        (f"Compara a Fabi con el gato del poema: «{W2A}» frente a «{X2C}» {GW2A} {GX2C} ¿Qué diferencia muestran? a) Fabi actúa para cambiar el resultado y el gato evita actuar b) Los dos son igual de decididos", "a", "Ella grita y ataja penales; el gato deja todo para mañana."),
        ("Tres textos: 1) «Lia returns a lost phone», 2) «Marco copies from a friend», 3) «Sofi tells the truth about a broken glass». (phone = teléfono; copies = copia; truth = verdad; glass = vaso) ¿En cuáles personajes se ve honestidad? Escribe los números en orden.", "1, 3", "Devolver lo ajeno y decir la verdad son acciones honestas; copiar no lo es."),
    ],
    [("En una exposición, una compañera presenta al personaje de una historia: «Lena is brave because she walks alone to get help when her brother is hurt.» (get help = buscar ayuda; hurt = herido) Tu profesora pide revisar si tiene las tres partes: personaje, característica y evidencia. ¿Las tiene? Responde sí o no.", "Sí", "Nombra a Lena, dice brave y usa una acción con because.")],
    [
        ("¿Cómo se dice «valiente» en inglés?", "Brave", "Es un adjetivo para describir un personaje."),
        ("En una descripción de personaje, ¿qué palabra une la característica con la acción?", "Because", "Because significa porque y justifica la característica."),
        ("Si el texto no da ninguna pista, ¿puedes afirmar una característica? Responde sí o no.", "No", "Sin evidencia la afirmación sería una invención."),
    ],
    task("Lee: «Mr. Salas is a bus driver in Santiago. Every morning he waits for an old woman who walks slowly. One rainy day he gets out of the bus and opens his umbrella for her. The passengers wait quietly and nobody complains.» (waits for = espera a; passengers = pasajeros; quietly = en silencio) Describe en tu hoja al señor Salas con la forma «character + trait + because + action» y agrega una segunda característica de otro personaje.", "Mr. Salas is caring because he opens his umbrella for the old woman. The passengers are patient because nobody complains.", ["usa un adjetivo de la lista", "une característica y acción con because", "describe también a otro personaje"], ["dos oraciones completas en la hoja"], ["escribir una característica sin acción que la apoye", "usar un adjetivo que el texto contradice"], "Pide que busque en el texto la frase exacta que apoya cada oración."),
    "Copia los ocho adjetivos de personajes de la tabla y dibuja al lado de cada uno una cara que lo represente.",
    "Describe con la forma «character + trait + because + action» a un personaje de un cuento o película que conozcas.",
)

# ============================================================ clase 3: entorno y trama
W3A = "In a small village in the Atacama desert, a boy named Ivo wants to see the stars. In the evening the sky is cloudy. He waits on the roof all night. At four in the morning the clouds go away and the stars appear."
GW3A = "(village = pueblo; desert = desierto; cloudy = nublado; roof = techo; clouds = nubes)"
W3B = "In the morning, Sofi is at home in Valparaiso. She packs a bag. In the afternoon she is at the bus station. At night she arrives at her grandmother's house by the sea."
GW3B = "(packs = arma; bus station = terminal; arrives = llega; by the sea = junto al mar)"
X3A = "On a stormy Friday in Chiloe, Marta and her father repair a small fishing boat. The wind is strong. First they fix the sail. Then they paint the name Esperanza on the side. In the end the boat is ready for Saturday."
GX3A = "(stormy = tormentoso; repair = reparan; fishing boat = bote de pesca; sail = vela; paint = pintan; ready = lista)"
X3B = "Panel 1: It is Monday in the school library. Lucas wants a book about volcanoes. Panel 2: The book is not on the shelf. Panel 3: The librarian finds it in the returns box. Lucas reads it happily."
GX3B = "(volcanoes = volcanes; shelf = estante; librarian = bibliotecaria; returns box = caja de devoluciones; happily = contento)"
X3C = "The sun comes up, the city wakes. / The market opens, the baker bakes. / At noon the park is full of fun. / At night the streets are quiet, the day is done."
GX3C = "(comes up = sale; wakes = despierta; bakes = hornea; noon = mediodía; fun = diversión; done = terminado)"

lesson(
    OA, 3,
    "Los textos, el poema y la tira cómica escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a ubicar el entorno (tiempo y lugar) y a ordenar la trama en inicio, desarrollo y final usando palabras de secuencia. Sirve para resumir una historia en inglés sin perder el orden de los hechos.",
    ["Reconozco el tema y las características de un personaje.", "Conozco palabras de tiempo como morning, afternoon y night."],
    [
        "El entorno (setting) tiene dos partes: el lugar (place) y el tiempo (time). El tiempo puede ser un momento del día (in the morning, at night), un día (on Friday) o una época (in winter). Busca expresiones con in, on y at y nombres de lugares: village, library, bus station. En una misma historia el entorno puede cambiar, como en el viaje de Sofi.",
        "La trama (plot) es la cadena de hechos. Tiene un inicio (beginning), que presenta personajes y lugar; un desarrollo (middle), donde ocurre la acción principal; y un final (end), que muestra cómo termina. Para ordenarla usa palabras de secuencia (sequence words): first (primero), then (luego), after that (después de eso), finally o in the end (al final).",
        "Un buen resumen usa una oración por parte y respeta ese orden: «At the beginning…, in the middle…, in the end…». No cuentes todos los detalles, solo los hechos que cambian la historia. Si una oración dice cómo es el clima, es entorno; si dice qué hace alguien, es parte de la trama.",
    ],
    [("setting", "entorno: lugar y tiempo"), ("place / time", "lugar / tiempo"), ("plot", "trama"), ("beginning / middle / end", "inicio / desarrollo / final"), ("first / then", "primero / luego"), ("after that", "después de eso"), ("finally / in the end", "finalmente / al final")],
    [
        ("Identificar el entorno", f"Texto: «{W3A}» {GW3A} ¿Cuál es el entorno?",
         ["Lugar: un pueblo del desierto de Atacama y el techo.", "Tiempo: la noche, hasta las cuatro de la mañana.", "Se escribe lugar y tiempo juntos."], "Lugar: un pueblo del desierto de Atacama. Tiempo: de noche, hasta las cuatro de la mañana."),
        ("Ver cómo cambia el entorno", f"Texto: «{W3B}» {GW3B} Ordena los lugares y momentos en que está Sofi.",
         ["Mañana: en su casa en Valparaíso.", "Tarde: en el terminal de buses.", "Noche: en la casa de su abuela, junto al mar."], "Casa en la mañana, terminal en la tarde, casa de la abuela en la noche."),
    ],
    [
        ("Poner en el desarrollo el hecho que solo presenta a los personajes.", "Se confunde la presentación con la acción principal.", "El inicio presenta; el desarrollo trae el problema o la acción importante."),
        ("Usar «finally» en la primera oración de un resumen.", "Esa palabra solo sirve para el último hecho.", "Empieza con first o at the beginning."),
    ],
    [
        ("«In the afternoon» indica: a) tiempo b) lugar", "a", "Afternoon es un momento del día."),
        ("Una palabra de secuencia que se usa para cerrar un resumen es: a) finally b) first", "a", "Finally significa finalmente y cierra la secuencia."),
        ("«Bus station» es: a) un lugar b) un personaje", "a", "Es el terminal de buses, un lugar del entorno."),
    ],
    [
        (f"Lee: «{X3A}» {GX3A} ¿Dónde y cuándo ocurre? a) In Chiloe, on a stormy Friday b) In Santiago, on a sunny Sunday", "a", "El texto dice On a stormy Friday in Chiloe."),
        (f"Lee: «{X3A}» {GX3A} ¿Qué hacen primero Marta y su padre? a) They fix the sail b) They paint the name", "a", "La palabra First marca el primer paso."),
        (f"Lee: «{X3A}» {GX3A} ¿Qué palabra marca el último hecho? a) In the end b) Then", "a", "In the end indica el final de la trama."),
    ],
    [
        (f"Lee la tira: «{X3B}» {GX3B} ¿Qué viñeta presenta el problema? a) Panel 2 b) Panel 3", "a", "En la viñeta 2 el libro no está en el estante."),
        (f"Lee la tira: «{X3B}» {GX3B} ¿Qué viñeta es el final? a) Panel 3 b) Panel 1", "a", "En la viñeta 3 la bibliotecaria lo encuentra y Lucas lo lee."),
        (f"Lee el poema: «{X3C}» {GX3C} ¿Qué tres momentos del día aparecen, en orden? a) Morning, noon, night b) Noon, morning, night", "a", "Primero el sol sale y la ciudad despierta (mañana), luego es mediodía y al final es de noche."),
    ],
    [
        (f"Lee: «{X3A}» {GX3A} Un compañero dice que la oración «The wind is strong» es parte de la trama. ¿Es correcto? a) No, describe el entorno b) Sí, es una acción de Marta", "a", "Dice cómo está el clima; no cuenta una acción de un personaje."),
        (f"Lee: «{X3B}» {GX3B} Ordena los hechos con letras: x) The librarian finds the book. y) Lucas wants a book. z) The book is not on the shelf. Escribe las tres letras en orden.", "y, z, x", "Primero quiere el libro, luego no está y al final lo encuentran."),
    ],
    [
        (f"Texto: «{W3A}» {GW3A} Resume el desarrollo. ¿Qué opción corresponde al desarrollo y no al inicio? a) He waits on the roof all night b) A boy named Ivo wants to see the stars", "a", "Esperar toda la noche es la acción principal; querer ver estrellas presenta la meta."),
        (f"Texto: «{X3A}» {GX3A} Un resumen dice: «Finally, the boat is ready. First, Marta and her father repair a boat.» ¿Qué error tiene? a) El orden de las palabras de secuencia está invertido b) Falta un personaje", "a", "Finally debe ir al final y First al inicio."),
    ],
    [("Tu curso de Inglés hace una cartelera con resúmenes de un cuento sobre el desierto. Tu compañero escribió: «At the beginning, a boy named Ivo wants to see the stars. In the middle, he waits all night on the roof. In the end, the stars appear.» (stars = estrellas; roof = techo) ¿Respeta inicio, desarrollo y final? Responde sí o no.", "Sí", "Cada oración corresponde a una parte y el orden es el de la historia.")],
    [
        ("¿Cuáles son las dos partes del entorno?", "Lugar y tiempo", "El entorno responde dónde y cuándo."),
        ("¿Qué significa «first» en una secuencia?", "Primero", "Marca el primer hecho."),
        ("Si una oración dice «It is a cold night», ¿qué parte de la historia es: entorno o acción?", "Entorno", "Describe el tiempo y el clima, no lo que hace un personaje."),
    ],
    task("Lee este cuento: «In winter, Tania lives in a small town in the south of Chile. She wants to ride her bike, but the road is full of snow. She asks her uncle for help. First they clear the snow from the road. Then they ride slowly to the school. Finally Tania arrives on time.» (winter = invierno; snow = nieve; clear = despejan; road = camino; on time = a tiempo) En tu hoja escribe un resumen con tres oraciones: At the beginning…, In the middle…, In the end…, y anota el entorno.", "Entorno: invierno, un pueblo del sur de Chile. At the beginning, Tania wants to ride her bike but there is snow. In the middle, she and her uncle clear the snow from the road. In the end, she arrives at school on time.", ["resume tres partes en orden", "usa las expresiones de secuencia", "anota lugar y tiempo del entorno"], ["resumen de tres oraciones y entorno en la hoja"], ["contar detalles sin importancia", "mezclar el orden de los hechos"], "Pide que subraye en el cuento la palabra que le indicó cada parte."),
    "Copia las palabras de secuencia de la tabla y ordénalas de la primera a la última.",
    "Escribe tres oraciones en inglés con first, then y finally sobre algo que haces antes de ir al colegio.",
)

# ============================================================ clase 4: problema y solución (brecha de información)
TA = "Tarjeta A. Beginning: Nora wants to take photos of birds at the lake, but her camera has no battery. Middle: She asks her cousin for a charger."
TB = "Tarjeta B. Middle: Her cousin has a charger, but it does not fit the camera. End: Nora takes a picture with her cousin's phone and the photos are great."
GTAB = "(camera = cámara; battery = batería; charger = cargador; fit = calzar; phone = teléfono)"
W4A = "The school garden has no water because the tap is broken. The students cannot water the plants. Mateo has an idea: they collect rain water in buckets. After two days, the plants are green again."
GW4A = "(garden = huerto; tap = llave; water = regar; buckets = baldes; green = verdes)"
W4B = "Isa is afraid to speak in English class. She practises in front of the mirror and then with a friend. On the day of the presentation she is still nervous, but she finishes it."
GW4B = "(afraid = con miedo; mirror = espejo; presentation = presentación; nervous = nerviosa; finishes = termina)"
X4A = "Leo's bike has a flat tyre on the way to the match. He has no repair kit. A neighbour lends him a pump and Leo arrives ten minutes late, but he still plays."
GX4A = "(flat tyre = rueda pinchada; repair kit = kit de reparación; lends = presta; pump = bomba de aire; late = tarde)"
X4B = "Panel 1: Pia's little dog hides under the bed every time it thunders. Panel 2: Pia tries to pull him out, but he is afraid. Panel 3: She sits quietly beside the bed and reads a book. Panel 4: The dog comes out and sleeps on her feet."
GX4B = "(hides = se esconde; thunders = truena; pull out = sacar; afraid = asustado; feet = pies)"
X4C = "Two friends want the same seat on the bus. They argue for a minute. Then Gaspar says, 'You sit now, I sit on the way back.' Bruna agrees."
GX4C = "(seat = asiento; argue = discuten; way back = vuelta; agrees = acepta)"

lesson(
    OA, 4,
    "Las tarjetas, los textos y la tira cómica escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a encontrar el problema de una historia y su solución, aunque la información venga repartida en dos partes. Sirve para completar una historia con los datos de dos compañeros y para explicar cómo se resolvió algo.",
    ["Sé ordenar inicio, desarrollo y final.", "Conozco but, so y because."],
    [
        "El problema (problem) es lo que impide que el personaje consiga algo. La solución (solution) es lo que hace o lo que ocurre para resolverlo. Palabras que anuncian un problema: but (pero), cannot (no puede), no (sin), afraid (con miedo), broken (roto). Palabras que ayudan a ver la solución: so (así que), then (luego), idea, help, finally, in the end.",
        "A veces la solución no resuelve todo: el personaje consigue una parte (partial solution, solución parcial). Leo llega diez minutos tarde, pero juega. Por eso debes leer el final con cuidado. Una buena pregunta es: ¿qué cambió entre el problema y el final? Esa diferencia es la solución, y la causa (cause) es la acción que la produce.",
        "Con una brecha de información (information gap), cada persona tiene una parte de la historia y la otra parte falta. Para completarla, une los datos: lee la tarjeta A, luego la B, y construye la cadena Problem → Attempt (intento) → Solution. Si dos datos no calzan, vuelve a leer, pregunta o pide aclarar, pero no inventes la parte que falta.",
    ],
    [("problem", "problema"), ("solution", "solución"), ("partial solution", "solución parcial"), ("attempt", "intento"), ("cause", "causa"), ("information gap", "brecha de información: cada uno tiene una parte"), ("idea", "idea")],
    [
        ("Hallar problema y solución", f"Texto: «{W4A}» {GW4A} ¿Cuál es el problema y cuál la solución?",
         ["Problema: la llave está rota y no hay agua para regar.", "La idea de Mateo es recoger agua de lluvia en baldes.", "El resultado: después de dos días las plantas están verdes."], "Problema: sin agua porque la llave está rota. Solución: recoger agua de lluvia en baldes."),
        ("Reconocer una solución parcial", f"Texto: «{W4B}» {GW4B} ¿Isa resuelve por completo su problema?",
         ["Su problema es el miedo a hablar en inglés.", "Practica, pero el día de la presentación sigue nerviosa.", "Termina la presentación: avanzó, pero el miedo no desapareció."], "No del todo: es una solución parcial, porque termina pero sigue nerviosa."),
    ],
    [
        ("Decir que la solución de Leo es «arrive ten minutes late».", "Llegar tarde es la consecuencia del problema, no su solución.", "La solución es que un vecino le presta una bomba de aire."),
        ("Completar una tarjeta con datos inventados cuando falta información.", "Se rellena la brecha sin evidencia.", "Usa solo lo que dicen las dos tarjetas o pide más datos."),
    ],
    [
        ("«Broken» (roto) es una palabra que suele anunciar: a) un problema b) una solución", "a", "Algo roto impide hacer algo."),
        ("«Solution» significa: a) solución b) personaje", "a", "Es lo que resuelve el problema."),
        ("En una brecha de información, cada persona tiene: a) una parte de los datos b) todos los datos", "a", "Por eso hay que unir las partes."),
    ],
    [
        (f"Lee: «{X4A}» {GX4A} ¿Cuál es el problema de Leo? a) A flat tyre on the way to the match b) A broken pump", "a", "El texto dice que la rueda se pincha camino al partido."),
        (f"Lee: «{X4A}» {GX4A} ¿Quién ayuda a Leo? a) A neighbour b) A coach", "a", "Un vecino le presta una bomba de aire."),
        (f"Lee: «{X4A}» {GX4A} ¿Resuelve del todo el problema? a) Partly: he plays, but he arrives late b) Completely: he arrives on time", "a", "Llega diez minutos tarde, pero igual juega: es una solución parcial."),
    ],
    [
        (f"Lee las tarjetas. {TA} {TB} {GTAB} ¿Qué problema nuevo aparece en la tarjeta B? a) The charger does not fit the camera b) Nora has no cousin", "a", "El cargador del primo no calza con la cámara."),
        (f"Lee las tarjetas. {TA} {TB} {GTAB} ¿Cuál es la solución final? a) Nora uses her cousin's phone b) Nora buys a new camera", "a", "Toma las fotos con el teléfono de su primo."),
        (f"Lee la tira: «{X4B}» {GX4B} ¿Qué viñeta muestra lo que hace Pia para resolver el problema? a) Panel 3 b) Panel 1", "a", "En la viñeta 3 Pia se sienta tranquila y lee, lo que calma al perro."),
    ],
    [
        (f"Lee la tira: «{X4B}» {GX4B} En la viñeta 2, Pia intenta sacar al perro. ¿Cómo se llama esto en la cadena de la historia? a) Attempt (un intento que no funciona) b) Solution", "a", "No resuelve el problema, porque el perro sigue asustado."),
        (f"Lee: «{X4C}» {GX4C} ¿Cuál es la solución al conflicto de Gaspar y Bruna? a) They take turns b) They both stand", "a", "Se turnan: ahora una persona se sienta y a la vuelta la otra."),
    ],
    [
        (f"Lee las tarjetas. {TA} {TB} {GTAB} Un compañero dice: «Nora's cousin has no charger.» ¿Qué dato de la tarjeta B lo contradice? a) Her cousin has a charger b) The photos are great", "a", "La tarjeta B dice que su primo sí tiene un cargador."),
        ("Tarjeta A: «Hugo cannot find his glasses before the exam.» Tarjeta B: «His sister finds them in his jacket.» (glasses = lentes; exam = prueba; jacket = chaqueta) ¿Qué conectan las dos tarjetas? a) Problema y solución b) Dos finales distintos", "a", "La tarjeta A tiene el problema y la B la solución."),
    ],
    [("En una actividad de clase, dos compañeros leen dos tarjetas distintas sobre una misma historia. Tarjeta 1: «A bakery in Osorno has no flour on Monday.» Tarjeta 2: «The baker buys flour from a friend and sells bread on Tuesday.» (flour = harina; bakery = panadería; sells = vende) Al unirlas, ¿qué se sabe? a) Hay un problema el lunes y una solución el martes b) El pan se acaba para siempre", "a", "El lunes falta harina y el martes ya se vende pan.")],
    [
        ("¿Qué palabra anuncia un problema: but o so?", "But", "But muestra una dificultad."),
        ("¿Qué es una solución parcial?", "Una solución que resuelve solo una parte", "El personaje avanza, pero el problema no desaparece del todo."),
        ("Si falta un dato en una brecha de información, ¿qué debes hacer: inventarlo o volver a leer y preguntar?", "Volver a leer y preguntar", "Así no inventas información."),
    ],
    task("Estas son las dos tarjetas de una historia. Tarjeta A: «Rocio loses her bus card on the way to school. She has no money, so she asks the bus driver to let her enter.» Tarjeta B: «The driver says yes, and she gives him a thank-you note the next day.» (bus card = tarjeta de transporte; asks = pide; lets her enter = la deja subir; thank-you note = nota de agradecimiento) Une las tarjetas y completa en tu hoja una cadena Problem → Attempt → Solution y escribe si la solución es total o parcial.", "Problem: Rocio loses her bus card and has no money. Attempt: she asks the bus driver to let her enter. Solution: the driver says yes. Es una solución total, porque puede viajar al colegio.", ["une los datos de las dos tarjetas", "separa problema, intento y solución", "decide con una razón si es total o parcial"], ["cadena de tres casillas en la hoja"], ["inventar datos que no están en las tarjetas", "poner el problema en el lugar de la solución"], "Pide que cuente la historia en voz alta con las palabras but, so y finally."),
    "Copia el vocabulario y escribe junto a cada palabra si se relaciona con el problema o con la solución.",
    "Escribe tres oraciones en inglés que cuenten un problema cotidiano de tu colegio y cómo se resolvió, con but y so.",
)

# ============================================================ clase 5: palabras clave, expresiones frecuentes y vocabulario temático
W5A = "Once upon a time, a fisherman lived in a small port. One day, all of a sudden, the sea became very calm. Little by little, a huge wave grew behind the boat. The fisherman rowed fast to the shore and saved his friends."
GW5A = "(fisherman = pescador; port = puerto; calm = calmo; huge = enorme; wave = ola; rowed = remó; shore = orilla; saved = salvó)"
W5B = "Max wants to bake a cake. First he mixes flour, eggs and sugar. Then he puts the cake in the oven. After thirty minutes the kitchen smells great. He is hungry!"
GW5B = "(bake = hornear; mixes = mezcla; flour = harina; eggs = huevos; sugar = azúcar; oven = horno; smells = huele)"
Z5 = "Once upon a time, a girl named Alba lived in a house at the end of a long road in the south. Every evening she watered a small tree, but the tree never grew. All of a sudden, one spring morning, she saw a tiny green leaf. Little by little, the tree became strong and gave shade to the whole street. Alba learned that patience and care can change a place."
GZ5 = "(watered = regaba; never grew = nunca crecía; leaf = hoja; shade = sombra; whole = toda; care = cuidado)"

lesson(
    OA, 5,
    "El cuento y los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a usar palabras clave, expresiones frecuentes y vocabulario temático para entender un texto literario, y haré una lectura completa por mi cuenta. Sirve para comprender un cuento sin traducir palabra por palabra.",
    ["Sé reconocer tema, personajes, entorno y trama.", "Conozco first, then y finally."],
    [
        "Las palabras clave (key words) son las que más ayudan a entender el texto: casi siempre se repiten o se relacionan con el tema. El vocabulario temático (thematic vocabulary) es un grupo de palabras de un mismo campo: sea, fisherman, wave, boat, shore son del mar; flour, sugar, oven, bake son de cocinar. Si reconoces el campo, puedes deducir el significado de palabras nuevas.",
        "Las expresiones de uso frecuente (frequent expressions) aparecen en muchos cuentos: once upon a time (érase una vez), one day (un día), all of a sudden (de repente), little by little (poco a poco), in the end (al final). No se traducen palabra por palabra: se aprende su sentido completo. Marcan cuándo ocurre algo o cómo cambia la historia.",
        "Para leer sin traducir todo, sigue tres pasos. Uno: lee entero el párrafo y busca las palabras que ya conoces. Dos: mira la palabra desconocida junto a su campo temático y a las otras palabras de la oración (contexto). Tres: comprueba que el significado calza con la historia. Esto se llama deducir el significado por el contexto.",
    ],
    [("key words", "palabras clave"), ("thematic vocabulary", "vocabulario temático"), ("once upon a time", "érase una vez"), ("all of a sudden", "de repente"), ("little by little", "poco a poco"), ("one day", "un día"), ("context", "contexto: palabras alrededor")],
    [
        ("Reconocer el campo temático", f"Texto: «{W5B}» {GW5B} ¿Qué campo temático forman flour, eggs, sugar y oven?",
         ["Todas son palabras de la cocina.", "Max hornea una torta.", "El campo es cooking (cocinar)."], "Forman el campo de la cocina, o cooking."),
        ("Entender una expresión frecuente", f"Texto: «{W5A}» {GW5A} ¿Qué significa «all of a sudden» en este cuento?",
         ["No se traduce palabra por palabra.", "Aparece cuando el mar cambia de repente.", "Significa de repente."], "De repente."),
    ],
    [
        ("Traducir «little by little» como «pequeño por pequeño».", "Se traduce palabra por palabra y se pierde el sentido.", "La expresión completa significa poco a poco."),
        ("Pensar que una palabra desconocida impide entender todo el texto.", "No se usa el contexto ni el campo temático.", "Mira las palabras que la rodean y comprueba si calza con la historia."),
    ],
    [
        ("«Once upon a time» se usa para: a) empezar un cuento b) cerrar una carta", "a", "Es la fórmula tradicional de inicio: érase una vez."),
        ("«Little by little» significa: a) poco a poco b) de repente", "a", "Marca un cambio lento."),
        ("«Wave, boat, shore» son palabras del campo: a) del mar b) de la cocina", "a", "Forman un campo temático sobre el mar."),
    ],
    [
        (f"Lee: «{W5A}» {GW5A} ¿Qué palabra de vocabulario temático del mar aparece en la primera oración? a) port b) oven", "a", "Port es el puerto; oven es del campo de la cocina."),
        (f"Lee: «{W5B}» {GW5B} ¿Qué palabra marca la secuencia al inicio del texto? a) First b) Little by little", "a", "First indica el primer paso."),
        (f"Lee: «{W5A}» {GW5A} ¿Qué expresión muestra que algo ocurre un día determinado? a) One day b) Little by little", "a", "One day marca el momento en que cambia la historia."),
    ],
    [
        ("Texto: «The fisherman puts the net into the water. Many fish swim into it.» (puts = pone; fish = peces; swim = nadan) Si no sabes qué es «net», ¿qué ayuda más a deducirlo? a) La palabra fish y la acción de ponerla en el agua b) La primera letra de la palabra", "a", "El contexto sugiere un objeto para pescar: una red."),
        (f"Lee: «{W5A}» {GW5A} ¿Qué significa «rowed fast to the shore»? a) Remó rápido hacia la orilla b) Nadó lejos de la orilla", "a", "Rowed es remó y shore es orilla."),
        (f"Lee: «{W5B}» {GW5B} ¿Qué campo temático explica la palabra «oven»? a) Cooking b) Sailing", "a", "El horno se relaciona con hornear la torta."),
    ],
    [
        (f"Lee: «{Z5}» {GZ5} ¿Cuál es el entorno? a) A house at the end of a long road in the south, in spring b) A big city in winter", "a", "El texto dice at the end of a long road in the south y one spring morning."),
        (f"Lee: «{Z5}» {GZ5} ¿Cuál es el problema de Alba? a) The tree never grows b) She has no water", "a", "Riega el árbol cada tarde, pero nunca crecía."),
    ],
    [
        (f"Lee: «{Z5}» {GZ5} ¿Qué expresión señala el momento en que cambia la historia? a) All of a sudden b) Once upon a time", "a", "Introduce la aparición de la hoja verde y rompe la situación inicial."),
        (f"Lee: «{Z5}» {GZ5} ¿Cuál es el tema? a) Patience and care can change a place b) Trees give shade only in summer c) Girls like long roads", "a", "Alba aprende eso al ver que el árbol crece y da sombra a toda la calle."),
    ],
    [(f"Tu curso presenta cuentos en una feria del libro. Una compañera resume el cuento de Alba así: «At the beginning, Alba waters a small tree. In the middle, a leaf appears. In the end, the tree gives shade, and the theme is patience and care.» {GZ5} ¿Cuántas partes de la trama menciona? Escribe el número.", "3", "Menciona inicio, desarrollo y final, y además el tema.")],
    [
        ("¿Qué significa «all of a sudden»?", "De repente", "Marca un cambio rápido."),
        ("¿Qué campo temático forman sugar, flour y oven?", "Cocina", "Son palabras relacionadas con cocinar."),
        ("Para deducir una palabra nueva, ¿qué miras primero: el contexto o el diccionario?", "El contexto", "Primero usas las palabras que la rodean y el campo temático."),
    ],
    task("Lee: «Once upon a time, a boy named Nico lived in a village by a lake in the south. Every summer he made a small paper boat. All of a sudden, one day, a strong wind took the boat to the middle of the lake. Little by little, the wind stopped and a fisherman brought the boat back. Nico learned to say thank you.» (village = pueblo; lake = lago; paper boat = barquito de papel; wind = viento; brought back = devolvió) En tu hoja anota: dos expresiones frecuentes, tres palabras del campo del agua, el problema, la solución y el tema.", "Expresiones: once upon a time, all of a sudden. Agua: lake, boat, fisherman. Problema: el viento se lleva el barco. Solución: un pescador lo devuelve. Tema: dar las gracias y valorar la ayuda.", ["encuentra dos expresiones frecuentes", "anota tres palabras del mismo campo", "identifica problema, solución y tema con una oración"], ["ficha de cinco líneas en la hoja"], ["poner palabras de otros campos", "escribir el tema como una sola palabra"], "Pide que explique cómo dedujo el significado de una palabra nueva usando el contexto."),
    "Copia las expresiones frecuentes de la tabla y escribe su significado completo, sin traducir palabra por palabra.",
    "Escribe un inicio de cuento de tres oraciones con once upon a time, one day y all of a sudden.",
)
