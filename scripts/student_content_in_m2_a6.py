"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 06: estrategias antes, durante y después de hablar.

El estudiante analiza ejemplos escritos y practica con un adulto como interlocutor. Textos originales, inglés americano.
Los títulos de clase del plan son genéricos; aquí se aplican a preparar (práctica, diagramas, conexiones), parafrasear,
sinónimos y chunks, rellenos y conectores, autocorrección y revisión posterior con metas y registro de errores.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 06"

# ------------------------------------------------------------------ clase 1: antes de hablar
DG1 = "Diagrama de ejemplo para hablar de «A place I want to visit» (un lugar que quiero visitar). Centro: Torres del Paine. Ramas: Where = in Chilean Patagonia; When = in summer; What = see mountains and lakes; Why = I like nature."
DG2 = "Diagrama incompleto para «My weekend plan»: Ramas: Place = the park; Time = ?; People = ?; Activity = play basketball."
PRA = "Plan de práctica de una estudiante para una charla de 2 minutos: lunes, escribe las ideas clave; martes, practica sola frente al espejo; miércoles, practica con una amiga; jueves, graba su voz y la escucha; viernes, presenta."

lesson(
    OA, 1, MAT_R,
    "Aprenderé estrategias para prepararme antes de hablar: practicar la presentación, organizar la información clave en un diagrama y hacer conexiones con lo que ya sé. Sirve para hablar con más claridad y seguridad.",
    ["Sé organizar ideas en esquemas.", "Conozco las preguntas who, where, when, what y why."],
    [
        "Antes de hablar, prepárate con tres estrategias. Primero, organiza la información clave en un diagrama (diagram): escribe el tema al centro y agrega ramas con palabras clave para where, when, what y why. Un diagrama no lleva oraciones completas, solo palabras que te recuerdan las ideas.",
        "Segundo, haz conexiones (connections): relaciona el tema con lo que ya sabes, con otras asignaturas, con tus experiencias o con otras culturas. Por ejemplo, para hablar de un lugar de Patagonia puedes conectar con Geografía o con un viaje que hiciste. Tercero, practica (practice): ensaya en voz alta varias veces, con un plan de días, primero solo, luego con alguien y por último grabándote.",
        "Un buen plan de práctica tiene pasos pequeños y fechas. Si te falta una idea, vuelve al diagrama y completa la rama vacía antes de seguir. Practicar no es memorizar: es estar listo para hablar con tus propias palabras.",
    ],
    [("diagram", "diagrama: esquema con palabras clave"), ("key words", "palabras clave"), ("connection", "conexión con lo que ya sabes"), ("practice", "práctica: ensayar en voz alta"), ("plan", "plan"), ("record", "grabar")],
    [
        ("Leer un diagrama", DG1 + " ¿Cómo usarías el diagrama para hablar en una oración?", ["El centro es el lugar: Torres del Paine.", "Las ramas dan Where, When, What y Why.", "Puedo decir: I want to visit Torres del Paine in summer because I like nature."], "I want to visit Torres del Paine in summer because I like nature"),
        ("Completar una rama", DG2 + " ¿Qué ramas faltan y cómo las completarías?", ["Faltan Time y People.", "Time puede ser Saturday morning.", "People puede ser my cousin and two friends."], "Faltan Time y People, por ejemplo Saturday morning y my cousin and two friends"),
    ],
    [
        ("Escribir todo el texto completo antes de hablar y leerlo.", "Se pierde la naturalidad y no se mira a la audiencia.", "Anota solo palabras clave en un diagrama."),
        ("Practicar solo una vez antes de hablar.", "Una práctica no basta para ganar fluidez.", "Practica varias veces en distintos pasos."),
    ],
    [
        mc("¿Qué se escribe en un diagrama para hablar?", "Palabras clave", ["Párrafos completos", "Solo dibujos sin palabras"], "Un diagrama recuerda las ideas con pocas palabras."),
        mr(DG1, "¿Cuál es la rama que responde Why?", "I like nature", ["in summer", "Chilean Patagonia"], "Why pregunta la razón."),
        mc("Hacer conexiones antes de hablar significa", "relacionar el tema con lo que ya sé", ["traducir todo palabra por palabra", "hablar más fuerte"], "Las conexiones activan conocimientos previos."),
    ],
    [
        mr(PRA, "¿Qué hace la estudiante el miércoles?", "Practica con una amiga", ["Presenta ante el curso", "Graba su voz"], "El plan dice miércoles, con una amiga."),
        mr(DG2, "Además de Place, ¿qué rama ya está completa?", "Activity, que dice play basketball", ["Time, que aún tiene un signo de pregunta", "People, que aún tiene un signo de pregunta"], "Place y Activity tienen datos; Time y People tienen signo de pregunta."),
        mc("Quieres hablar de un hobby y lo conectas con Educación Física. ¿Qué haces?", "Relacionas el hobby con esa asignatura", ["Cambias de tema", "Dejas de practicar"], "Es una conexión con otra asignatura."),
    ],
    [
        mr(DG1, "Quieres hablar de la naturaleza de Patagonia. ¿Qué rama usas para decir qué se puede ver?", "What", ["Where", "When"], "What contiene see mountains and lakes."),
        mr(PRA, "¿Qué paso del plan te permite escuchar tu pronunciación?", "Jueves: grabar la voz y escucharla", ["Lunes: escribir ideas clave", "Martes: practicar sola frente al espejo"], "Al grabarte puedes oír cómo suenas."),
        arith("Una estudiante practica 15 minutos al día durante 4 días. ¿Cuántos minutos practica en total?", "15*4", "Se multiplica el tiempo diario por el número de días.", " minutos"),
    ],
    [
        mr(PRA, "Una compañera dice que el plan es malo porque practica varios días seguidos. ¿Qué respuesta es más acertada?", "El plan es bueno porque aumenta la práctica de a poco", ["Tiene razón: conviene practicar todo el mismo día y no antes", "El plan no incluye práctica con otra persona"], "Practicar varias veces y de formas distintas ayuda a la fluidez."),
        mc("Un estudiante escribe todo su texto y lo memoriza palabra por palabra. ¿Qué riesgo corre?", "Quedarse en blanco si olvida una palabra", ["Hablar con demasiada naturalidad", "Practicar demasiado"], "Con un diagrama puede continuar con sus palabras."),
    ],
    [
        mc("Tienes 2 minutos para hablar de una ciudad. ¿Qué diagrama sirve más?", "Centro con ciudad, y ramas where, what to see, food y why", ["Un párrafo de 200 palabras", "Una lista de 40 palabras sueltas"], "Pocas ramas con palabras clave organizan la charla."),
        mr(DG1 + " " + DG2, "Un estudiante copia el diagrama de Torres del Paine para el plan del fin de semana sin cambiar nada. ¿Qué pasa?", "No sirve tal cual: tiene datos de otro tema", ["Sirve igual, porque dice Where y What", "Sirve si cambia el idioma"], "Cada tema necesita su diagrama."),
    ],
    [mc("Vas a hablar de tu mes favorito. Elige la mejor preparación.", "Hacer un diagrama, practicar tres veces y grabarte", ["Leer el calendario sin practicar", "Memorizar un texto largo en una noche"], "Combina diagrama, práctica y revisión.")],
    [
        ("En Inglés de 2.º medio (OA 6, clase 1): ¿qué se escribe en el centro de un diagrama?", "El tema", "Las ramas salen del tema."),
        ("En Inglés de 2.º medio (OA 6, clase 1): ¿qué es hacer una conexión?", "Relacionar el tema con lo que ya sé", "Activa conocimientos previos."),
        ("En Inglés de 2.º medio (OA 6, clase 1): ¿cuál es un paso de un buen plan de práctica?", "Practicar solo, con alguien y grabarse", "Aumentan la fluidez de a poco."),
    ],
    task("Elige un tema: «My favorite season», «A person I admire» o «A skill I want to learn». Dibuja un diagrama con el tema al centro y cuatro ramas (what, why, when, how o who), y escribe un plan de práctica de tres días. Con un adulto, practica diciendo tres oraciones usando el diagrama.", "Tema: My favorite season. Ramas: summer; sun and beach; December to March; with my friends. Plan: lunes ideas, martes sola, miércoles con un adulto. Oraciones: My favorite season is summer because I go to the beach. It lasts from December to March. I like the sun and the beach.", ["diagrama con cuatro ramas de palabras clave", "plan de práctica de tres días", "tres oraciones dichas con el diagrama"], ["diagrama en la hoja", "nota del adulto"], ["escribir oraciones completas en el diagrama", "no planificar días de práctica"], "Pide que explique el tema usando solo el diagrama, sin leer."),
    "Completa el diagrama de ejemplo «My weekend plan» con Time y People.",
    "Dibuja un diagrama en español sobre tu comida favorita y compáralo con uno en inglés.",
)

# ------------------------------------------------------------------ clase 2: parafrasear, sinónimos y chunks
PA1 = "«I forgot the word for the thing you use to open a can. It is a tool, small and metal, and you turn it around the top of the can.» (forgot = olvidé, tool = herramienta, metal = metal, turn = giras, top = parte de arriba)"
PA2 = "«The hall was big and I was glad to be there. The show was nice, and the singers were really good.» (hall = sala, show = espectáculo, singers = cantantes)"
CH1 = "«I'd like to ask a question. As far as I know, the library opens at nine. It depends on the day. What do you think? How about meeting at ten?» (as far as I know = hasta donde sé, it depends on = depende de, How about = qué tal si)"
PA3 = "«Tomás: Where is the place with the machines to wash clothes? Julia: Do you mean the laundromat? Tomás: Yes, that's it!» (machines = máquinas, wash = lavar, clothes = ropa, laundromat = lavandería)"

lesson(
    OA, 2, MAT_R,
    "Aprenderé a parafrasear cuando olvido una palabra, a usar sinónimos y a hablar con expresiones frecuentes (chunks). Sirve para seguir hablando con fluidez sin quedarme en silencio.",
    ["Sé que una palabra puede tener un sinónimo.", "Conozco frases como I'd like to y Could you...?"],
    [
        "Parafrasear (to paraphrase) es decir lo mismo con otras palabras. Si olvidas una palabra, descríbela: the thing you use to open a can, el objeto que se usa para abrir una lata. Di para qué sirve, cómo es o a qué se parece. Así tu interlocutor puede ayudarte con la palabra, como Do you mean the can opener?",
        "Un sinónimo (synonym) es una palabra con significado parecido: big y large, glad y happy, nice y pleasant, begin y start. Usar sinónimos evita repetir y te ayuda cuando una palabra no sale. Cuidado: no todos los sinónimos se usan igual en todos los contextos, por eso conviene verificar en un diccionario.",
        "Los chunks son grupos de palabras que se aprenden y se usan completos: I'd like to..., As far as I know..., It depends on..., What do you think?, How about...?, I'm not sure, but... Los chunks dan fluidez porque no tienes que armar la frase palabra por palabra. Aprende cinco por semana y úsalos en tus conversaciones.",
    ],
    [("paraphrase", "decir lo mismo con otras palabras"), ("synonym", "sinónimo"), ("chunk", "frase frecuente que se usa completa"), ("as far as I know", "hasta donde sé"), ("it depends on", "depende de"), ("How about...?", "¿qué tal si...?")],
    [
        ("Parafrasear una palabra olvidada", PA1 + " ¿Qué hace el hablante para comunicar la idea?", ["No recuerda la palabra.", "La describe: tool, small, metal, turn around the top.", "Eso permite que otro adivine can opener."], "La describe con su función y su forma"),
        ("Cambiar por sinónimos", PA2 + " Mejora la oración con sinónimos de big, glad y nice.", ["Big puede ser large.", "Glad puede ser happy.", "Nice puede ser pleasant."], "The hall was large and I was happy to be there. The show was pleasant"),
    ],
    [
        ("Quedarse en silencio cuando falta una palabra.", "La conversación se detiene.", "Describe la palabra con otras que conozcas."),
        ("Cambiar una palabra por un sinónimo sin comprobar el contexto.", "Algunos sinónimos no sirven en todas las frases.", "Verifica en un diccionario y piensa si suena natural."),
    ],
    [
        mr(PA3, "¿Qué parafrasea Tomás?", "La palabra laundromat", ["La palabra machine", "La palabra Yes"], "Describe un lugar con máquinas para lavar ropa."),
        mc("Un sinónimo de begin es", "start", ["stop", "finish"], "Begin y start significan empezar."),
        mc("¿Cuál de estas es un chunk?", "As far as I know", ["As know I far as", "I far as know as"], "Es una expresión frecuente completa."),
    ],
    [
        mr(CH1, "¿Qué chunk sirve para proponer un plan?", "How about meeting at ten?", ["It depends on the day", "I'd like to ask a question"], "How about...? propone algo."),
        mr(PA1, "¿Para qué sirve el objeto que describe el hablante?", "Para abrir una lata", ["Para cortar papel", "Para medir una lata"], "Se usa the thing you use to open a can."),
        mc("¿Qué chunk sirve para pedir la opinión de alguien?", "What do you think?", ["I'd like to", "It depends on"], "What do you think? pregunta su opinión."),
    ],
    [
        mc("Olvidaste la palabra pencil sharpener (sacapuntas). ¿Qué paráfrasis es mejor?", "A tool you use to make a pencil sharp", ["A big thing in my house that is square", "A long thin thing you write with"], "Describe función y tamaño."),
        mc("Cambia big por un sinónimo en: «We have a big house».", "We have a large house", ["We have a small house", "We have a house big"], "Large es sinónimo de big."),
        mr(CH1, "¿Qué chunk usa el hablante antes de dar el horario de la biblioteca, sin estar totalmente seguro?", "As far as I know", ["How about", "What do you think"], "As far as I know introduce lo que sabe, sin estar totalmente seguro."),
    ],
    [
        mr(PA2, "Una compañera dice que repetir big, nice y really good es suficiente. ¿Qué respuesta es mejor?", "Conviene usar sinónimos para variar", ["Conviene repetir lo mismo", "Conviene dejar de hablar"], "Los sinónimos enriquecen el lenguaje."),
        mc("Un estudiante dice «I am very tired» (tired = cansado) y quiere variar. ¿Cuál sinónimo es adecuado de tired?", "exhausted", ["energetic", "excited"], "Exhausted es muy cansado."),
    ],
    [
        mc("Te piden tu opinión y no estás seguro. ¿Qué chunk usas?", "I'm not sure, but...", ["I'd like to ask a question", "How about meeting at ten"], "Expresa duda antes de opinar."),
        mc("Quieres explicar que tu respuesta cambia según la situación. ¿Qué chunk sirve?", "It depends on...", ["As far as I know", "Do you mean...?"], "It depends on indica dependencia."),
    ],
    [mr(PA3, "En el texto de Tomás y Julia, ¿qué hace Julia para confirmar?", "Pregunta Do you mean the laundromat?", ["Dice Yes", "Repite la palabra machine"], "Do you mean...? propone la palabra que cree que busca.")],
    [
        ("En Inglés de 2.º medio (OA 6, clase 2): ¿qué es parafrasear?", "Decir lo mismo con otras palabras", "Sirve cuando falta una palabra."),
        ("En Inglés de 2.º medio (OA 6, clase 2): ¿qué es un chunk?", "Una expresión frecuente que se usa completa", "Da fluidez al hablar."),
        ("En Inglés de 2.º medio (OA 6, clase 2): ¿cuál es un sinónimo de glad?", "Happy", "Ambas significan contento."),
    ],
    task("Imagina que olvidaste la palabra scissors (tijeras). Escribe una paráfrasis de dos oraciones en inglés que la describa sin decirla, y úsala en un diálogo breve de cuatro líneas con un adulto. Usa dos chunks de la clase. Sigue este ejemplo.", "A: I need the thing that cuts paper. It has two blades. B: Do you mean scissors? A: Yes! How about using them for the project? B: As far as I know, they are in the drawer.", ["la paráfrasis describe función y forma", "usa dos chunks de la clase", "el diálogo suena natural"], ["diálogo en la hoja", "nota del adulto"], ["decir la palabra en español", "no usar ningún chunk"], "Pide que cambie una palabra del diálogo por un sinónimo."),
    "Escribe cinco sinónimos para happy, big y nice.",
    "Elige tres objetos de tu casa y escribe cómo los describirías en inglés sin decir su nombre.",
)

# ------------------------------------------------------------------ clase 3: rellenos temporales y conectores
FI1 = "«Teacher: Why are you late? Student: Well, the bus was late. Of course, I left home on time. Right, so I ran to the gate. Anyway, here I am.» (late = atrasado, on time = a la hora, ran = corrí, gate = portón, here I am = aquí estoy)"
FI2 = "«Sofía: What did you do on Sunday? Bruno: Let me think... Well, I visited my aunt, and then we went to a park. Right, and I also helped my uncle.» (visited = visité, aunt = tía, uncle = tío, helped = ayudé)"
CN1 = "«I will join the choir unless I have a test on Friday. Neither Pia nor Leo can come, though. As a result, we need a new singer.» (choir = coro, test = prueba, singer = cantante)"
CN2 = "«Either we meet at the library or we call each other. As soon as I finish my homework, I will send you a message.» (library = biblioteca, call = llamarnos, finish = termine, send = enviar)"

lesson(
    OA, 3, MAT_R,
    "Aprenderé a usar rellenos temporales (anyway, of course, right, well) para ganar tiempo al hablar y a activar conectores para unir mis ideas. Sirve para que mi conversación suene más natural y organizada.",
    ["Sé usar and, but, because y so.", "Conozco unless, though y as a result."],
    [
        "Los rellenos temporales (fillers) son palabras cortas que usamos para pensar sin quedarnos en silencio: well, let me think, anyway, of course y right. Well y let me think dan tiempo para pensar. Anyway sirve para volver al tema o cerrar una idea. Of course significa por supuesto y confirma algo. Right sirve para pasar a la idea siguiente o confirmar que entendiste.",
        "Los fillers se usan con medida: dos o tres en una respuesta pueden sonar naturales; diez la hacen confusa. Los conectores, en cambio, unen las ideas y muestran su relación: and suma, but contrasta, because da la razón, so da la consecuencia. Los del nivel son neither ... nor, either ... or, though, unless, as soon as y as a result. Elige el conector que corresponde a la relación entre tus dos ideas.",
        "Antes de hablar, prepara un conector para cada idea: primero..., luego..., por eso..., sin embargo... En medio de la conversación, si te quedas sin palabras, usa un filler, respira y sigue con el conector que ya tenías en la cabeza.",
    ],
    [("filler", "relleno: palabra para ganar tiempo"), ("well / let me think", "bueno / déjame pensar"), ("anyway", "en fin, de todos modos"), ("of course", "por supuesto"), ("right", "bien, entonces"), ("connector", "conector: une ideas")],
    [
        ("Reconocer fillers", FI2 + " ¿Qué fillers usa Bruno y para qué?", ["Usa Let me think y Well para pensar.", "Usa Right para pasar a otra idea.", "Los usa en cantidad moderada."], "Let me think, Well y Right: ganar tiempo y pasar a otra idea"),
        ("Elegir un conector", CN1 + " ¿Qué relación marca as a result?", ["Antes dice que Pia y Leo no pueden venir.", "As a result introduce lo que sigue por esa razón.", "Es una consecuencia: necesitan un cantante nuevo."], "Una consecuencia: como no vienen, necesitan un nuevo cantante"),
    ],
    [
        ("Llenar cada pausa con um y uh sin parar.", "El discurso se vuelve confuso.", "Usa fillers con medida y respira."),
        ("Usar but donde corresponde because.", "Se cambia la relación entre las ideas.", "Pregunta si la segunda idea da razón, consecuencia o contraste."),
    ],
    [
        mr(FI1, "¿Qué filler usa el estudiante al comenzar su respuesta?", "Well", ["Never", "Because"], "La respuesta comienza con Well."),
        mc("¿Qué conector da una razón?", "because", ["but", "or"], "Because explica por qué."),
        mc("¿Qué filler se parece a por supuesto?", "of course", ["anyway", "well"], "Of course es por supuesto."),
    ],
    [
        mr(CN2, "¿Qué dos opciones presenta either ... or?", "Juntarse en la biblioteca o llamarse", ["Juntarse en el patio o ir a casa", "Llamarse por teléfono o escribirse un mensaje"], "Dice either we meet at the library or we call each other."),
        mr(FI1, "¿Para qué sirve Right en la última oración?", "Para pasar a la siguiente idea", ["Para decir adiós al terminar la clase", "Para negar lo que se dijo antes"], "Right, so I ran continúa la explicación."),
        mc("¿Qué conector marca contraste?", "though", ["as soon as", "so"], "Though introduce un contraste."),
    ],
    [
        mc("Completa: I will call you ____ I arrive home.", "as soon as", ["unless", "though"], "As soon as marca el momento."),
        mc("Completa: I won't go ____ you come with me.", "unless", ["as a result", "either"], "Unless significa a menos que."),
        mc("Completa: It rained all day. ____, the match was canceled.", "As a result", ["Neither", "Unless"], "As a result introduce la consecuencia."),
    ],
    [
        mr(CN1, "Una estudiante dice que unless I have a test significa si tengo una prueba. ¿Es correcto?", "No: significa a menos que tenga una prueba", ["Sí: significa si tengo una prueba", "Sí: significa cuando tenga una prueba"], "Unless indica una condición negativa."),
        mr(FI2, "¿Qué problema habría si Bruno usara diez fillers en una respuesta?", "Su mensaje sería confuso y lento", ["Su mensaje sería más claro y más corto", "No habría ningún problema"], "El exceso de fillers distrae."),
    ],
    [
        mc("Elige la forma correcta: Neither the girls nor the teacher ____ ready.", "is", ["are", "be"], "El verbo concuerda con teacher, el sujeto más cercano."),
        mr(CN2, "¿Cuándo enviará el mensaje el hablante?", "Tan pronto como termine su tarea", ["Cuando llegue a la biblioteca", "A menos que lo llamen"], "Dice As soon as I finish my homework."),
    ],
    [mc("Te preguntan por qué llegaste tarde y no sabes cómo empezar. ¿Qué respuesta combina filler y conector?", "Well, I missed the bus, so I walked", ["Um, um, er... I don't know why I was late", "Because I was late because the bus was late"], "Well gana tiempo y so da la consecuencia.")],
    [
        ("En Inglés de 2.º medio (OA 6, clase 3): ¿para qué sirven los fillers?", "Para ganar tiempo al hablar", "Evitan el silencio sin información."),
        ("En Inglés de 2.º medio (OA 6, clase 3): ¿qué conector indica consecuencia?", "So o As a result", "Ambos marcan resultado."),
        ("En Inglés de 2.º medio (OA 6, clase 3): ¿qué significa anyway?", "En fin, de todos modos", "Cierra o retoma una idea."),
    ],
    task("Con un adulto, responde en voz alta a la pregunta «What do you usually do on Saturdays?» en cuatro oraciones. Usa dos fillers (por ejemplo well y let me think) y tres conectores (because, so, though, as soon as). Sigue este ejemplo y anota lo que dijiste.", "Well, I usually wake up late because I study hard during the week. Let me think... I help at home, so everything is clean. I play soccer in the afternoon, though. As soon as I finish my homework, I meet my friends.", ["usa dos fillers", "usa tres conectores", "las ideas tienen sentido"], ["cuatro oraciones en la hoja", "nota del adulto"], ["usar demasiados fillers", "elegir un conector que no corresponde"], "Pide que cambie un conector por otro y explique cómo cambia el sentido."),
    "Escribe cuatro oraciones con well, anyway, of course y right.",
    "Escucha una conversación en español y anota los rellenos que usan las personas.",
)

# ------------------------------------------------------------------ clase 4: autocorrección con ayuda
AC1 = "«I go to the beach yesterday... sorry, I went to the beach yesterday. There were two dogs. I mean, there were three dogs.» (beach = playa, dogs = perros, yesterday = ayer)"
AC2 = "«I am agree with you... I mean, I agree with you. It don't matter... sorry, it doesn't matter.» (agree = estar de acuerdo, matter = importar)"
AC3 = "«Student: She have a dog... Teacher: She... Student: She has a dog. Teacher: Good.» (dog = perro)"
AC5 = "«My brother is more tall than me... taller than me. He plays the guitar very good... very well.» (taller = más alto, guitar = guitarra)"

lesson(
    OA, 4, MAT_R,
    "Aprenderé a autocorregirme mientras hablo, con ayuda de quien me escucha, usando frases como I mean y sorry. Sirve para mejorar mi precisión sin detener la conversación.",
    ["Sé distinguir presente y pasado.", "Conozco errores frecuentes como I am agree."],
    [
        "Autocorregirse (to self-correct) es notar un error mientras hablas y arreglarlo. Se hace con frases cortas: sorry, I mean..., let me say that again, no, wait... Las usas, dices la forma correcta y sigues hablando. Por ejemplo: I go to the zoo yesterday... sorry, I went to the zoo yesterday.",
        "Algunos errores frecuentes son I am agree (se dice I agree), it don't matter (it doesn't matter), she have (she has), I have 16 years (I am 16 years old), more tall (taller), very good con un verbo (very well) e I live here since 2020 (I have lived here since 2020). Quien te escucha puede ayudar repitiendo la parte con error con voz de pregunta, como She...?, para que tú la arregles. Eso es una corrección guiada.",
        "Después de la conversación, anota los errores que te corrigieron en tu registro. No te frustres: notar un error ya es un avance. Corrige despacio, repite la oración correcta una vez y sigue con la idea.",
    ],
    [("self-correction", "autocorrección"), ("sorry, I mean...", "perdón, quiero decir..."), ("let me say that again", "déjame decirlo otra vez"), ("I agree", "estoy de acuerdo (sin am)"), ("she has", "ella tiene (no she have)"), ("taller / very well", "más alto / muy bien")],
    [
        ("Autocorregir una forma verbal", AC1 + " ¿Qué corrige el hablante y cómo?", ["Dice I go... yesterday: el pasado no coincide con ayer.", "Usa sorry y dice I went.", "Corrige con una frase corta y sigue."], "Corrige I go por I went con la frase sorry"),
        ("Corrección guiada", AC3 + " ¿Cómo ayuda la profesora?", ["Repite She... con voz de pregunta.", "La estudiante piensa y dice She has a dog.", "No le da la respuesta: la guía."], "Repite She... y la estudiante se corrige sola"),
    ],
    [
        ("Detener toda la conversación para corregir un error pequeño.", "Se pierde el hilo.", "Corrige rápido con una frase corta y sigue."),
        ("Corregir sin decir la forma correcta.", "El interlocutor no sabe qué cambió.", "Di la forma correcta completa."),
    ],
    [
        mr(AC2, "¿Cuál es la forma correcta de I am agree?", "I agree", ["I am agreeing", "I agreeing"], "Agree ya significa estar de acuerdo, sin am."),
        mc("¿Qué frase sirve para corregirse?", "Sorry, I mean...", ["Thank you for coming", "How about you?"], "I mean introduce la forma correcta."),
        mc("¿Cuál es correcta?", "She has a dog", ["She have a dog", "She haves a dog"], "Con she se usa has."),
    ],
    [
        mc("¿Cómo se dice correctamente que tienes 16 años?", "I am 16 years old", ["I have 16 years", "I have 16 years old"], "En inglés la edad se dice con be."),
        mr(AC5, "¿Cuál es la forma correcta de more tall?", "taller", ["more taller", "tallest"], "El comparativo de tall es taller."),
        mr(AC1, "¿Qué corrección hace el hablante sobre los perros?", "Cambia dos por tres", ["Cambia dogs por beach", "Cambia yesterday por today"], "Dice I mean, there were three monkeys."),
    ],
    [
        mc("Corrige: «It don't matter».", "It doesn't matter", ["It not matter", "It don't mattered"], "Con it se usa doesn't."),
        mc("Corrige: «He plays the guitar very good».", "He plays the guitar very well", ["He plays the guitar very goods", "He plays very the guitar good"], "Un adverbio de modo como well modifica el verbo."),
        mc("Corrige: «I live in Valdivia since 2020».", "I have lived in Valdivia since 2020", ["I lived in Valdivia since 2020", "I am living in Valdivia since the year 2020"], "Con since se usa el presente perfecto."),
    ],
    [
        mr(AC3, "Un compañero dice que la profesora debió decir la respuesta correcta de inmediato. ¿Qué respuesta es más adecuada?", "Repetir She... con voz de pregunta ayuda a que el estudiante se corrija solo", ["Es mejor no corregir nunca para no incomodar", "Es mejor decirle la respuesta sin esperar"], "La corrección guiada promueve la autocorrección."),
        mr(AC2, "Un estudiante dice «I am agree... I mean, I agree». ¿Qué hizo bien?", "Notó el error y lo corrigió sin detenerse", ["Cambió de tema", "Repitió el error cinco veces"], "Se autocorrigió con una frase corta."),
    ],
    [
        mc("Escuchas «She have three cats... sorry, she has three cats». ¿Qué estrategia usó la persona?", "Se corrigió sola con sorry", ["Pidió que le repitieran la frase", "Cambió de tema"], "Dijo sorry y la forma correcta."),
        mr(AC5, "Dices «My brother is more tall than me». Un adulto dice «My brother is...?» con voz de pregunta. ¿Qué debes decir?", "taller than me", ["more taller than me", "tallest than me"], "Corrige a la forma correcta del comparativo."),
    ],
    [mr(AC1 + " " + AC2, "¿Qué tipo de errores se corrigen en estos dos textos?", "De formas verbales y estructuras, como I go", ["De ortografía, como beach y dogs mal escritas", "De puntuación, como las comas y los puntos"], "Se corrigen formas como I go por I went e I am agree por I agree; las palabras están bien escritas.")],
    [
        ("En Inglés de 2.º medio (OA 6, clase 4): ¿qué frase corta sirve para autocorregirse?", "Sorry, I mean...", "Introduce la forma correcta."),
        ("En Inglés de 2.º medio (OA 6, clase 4): ¿cómo se dice la edad en inglés: I have 16 years o I am 16 years old?", "I am 16 years old", "Con be, no con have."),
        ("En Inglés de 2.º medio (OA 6, clase 4): ¿cuál es el comparativo de tall?", "Taller", "Los adjetivos cortos agregan -er."),
    ],
    task("Con un adulto, di en voz alta las siguientes oraciones con error y corrígelas con una frase de autocorrección: «She have a bike. I am agree with you. It don't matter. He plays the piano very good». Anota cada corrección. Después el adulto repite cada oración con voz de pregunta para que la corrijas sin ayuda.", "She has a bike. I agree with you. It doesn't matter. He plays the piano very well.", ["corrige las cuatro oraciones", "usa una frase de autocorrección", "se corrige también con la ayuda del adulto"], ["lista de cuatro correcciones", "nota del adulto"], ["dejar el error original", "corregir sin explicar"], "Pide que invente una oración nueva con cada forma correcta."),
    "Escribe una lista de tres errores tuyos que has notado y su corrección.",
    "Escucha a un compañero y anota (en español) dos frases que usa para corregirse.",
)

# ------------------------------------------------------------------ clase 5: después de hablar
LG1 = "Registro de ejemplo de una estudiante: Error 1: «I can to swim» → corrección: I can swim (después de can no va to). Error 2: «The people is nice» → corrección: The people are nice. Error 3: «I went to home» → corrección: I went home. Frecuencia: Error 1 aparece 3 veces; Error 2, 2 veces; Error 3, 1 vez."
MT1 = "Meta de ejemplo: «Para el viernes, voy a usar can sin to en las 10 oraciones que diga en clase y lo voy a revisar con mi registro de errores.»"
MT2 = "Meta de ejemplo (poco clara): «Quiero mejorar mi inglés.»"
FD1 = "Comentarios de un compañero tras una conversación de ejemplo: «Your ideas were clear. You used many connectors. But sometimes you spoke too fast, and you said ‘she have’ twice.»"

lesson(
    OA, 5, MAT_R,
    "Aprenderé a identificar mis debilidades después de hablar, a fijar una meta clara y a registrar y corregir mis errores con ayuda de recursos. Sirve para mejorar de una conversación a la siguiente.",
    ["Sé reconocer mis errores frecuentes.", "Sé usar un diccionario."],
    [
        "Después de hablar, haz una revisión (review). Primero, identifica tus debilidades: ¿qué palabras no encontraste?, ¿qué errores repetiste?, ¿qué sonidos o pausas fallaron? Puedes basarte en lo que recuerdas, en una grabación y en los comentarios de quien te escuchó. Segundo, registra los errores en una tabla con tres columnas: error, corrección y frecuencia.",
        "Tercero, establece metas (goals) claras: una meta buena dice qué harás, cuánto y para cuándo. Por ejemplo: Para el viernes, usaré can sin to en 10 oraciones. Una meta como mejorar mi inglés es demasiado vaga. Cuarto, corrige con recursos: un diccionario en línea, una gramática, una app de práctica o un ejemplo de tu libro. Anota la forma correcta con una oración de ejemplo.",
        "Al final de la semana, revisa tu registro: si un error ya no aparece, táchalo; si aparece de nuevo, vuelve a practicarlo. Mejorar es un ciclo de hablar, revisar, practicar y volver a hablar.",
    ],
    [("weakness", "debilidad: lo que cuesta"), ("error log", "registro de errores"), ("goal", "meta"), ("frequency", "frecuencia: cuántas veces ocurre"), ("feedback", "comentarios sobre lo que hiciste"), ("resource", "recurso: diccionario, gramática")],
    [
        ("Leer un registro de errores", LG1 + " ¿Qué error debe practicar primero y por qué?", ["Comparo la frecuencia de los tres errores.", "El primero aparece 3 veces.", "Debe empezar por el más frecuente."], "I can to swim, porque aparece tres veces"),
        ("Evaluar una meta", MT1 + " " + MT2 + " ¿Cuál meta es mejor?", ["La primera dice qué hacer: usar can sin to.", "Dice cuánto: en 10 oraciones.", "Dice cuándo: para el viernes."], "La primera, porque es concreta: qué, cuánto y cuándo"),
    ],
    [
        ("Fijar una meta como quiero mejorar mi inglés.", "Es demasiado vaga para saber si se cumple.", "Escribe qué, cuánto y para cuándo."),
        ("Anotar el error sin la forma correcta.", "No sabrás qué practicar.", "Escribe error, corrección y una oración de ejemplo."),
    ],
    [
        mr(LG1, "¿Cuántas veces apareció el error The people is nice?", "Dos veces", ["Tres veces", "Una vez"], "El registro dice Error 2, 2 veces."),
        mc("¿Qué columnas tiene un registro de errores?", "Error, corrección y frecuencia", ["Autor, título y año", "Color, tamaño y precio"], "Esas columnas permiten corregir y priorizar."),
        mc("Una meta de aprendizaje debe decir", "qué harás, cuánto y para cuándo", ["solo que quieres mejorar", "solo el nombre del profesor"], "Así puede comprobarse."),
    ],
    [
        mr(LG1, "¿Cuál es la corrección de I went to home?", "I went home", ["I went at home", "I did go to home"], "Con home no se usa to."),
        mr(FD1, "¿Qué debilidad menciona el compañero además de she have?", "A veces hablaba muy rápido", ["No usó conectores", "Sus ideas no eran claras"], "Dice sometimes you spoke too fast."),
        mc("¿Qué recurso sirve para verificar si una palabra se usa así?", "Un diccionario en línea", ["Un mapa de la ciudad donde vives", "Un reloj para medir el tiempo de práctica"], "El diccionario muestra ejemplos de uso."),
    ],
    [
        mr(MT1, "¿Cómo comprobarás esta meta el viernes?", "Contando tus oraciones con can sin to", ["Preguntando qué hora es", "Contando cuántas palabras dijiste en total"], "La meta es medible."),
        mr(FD1, "Con los comentarios del compañero, ¿qué meta clara puedes escribir?", "Para el viernes, diré she has en 5 oraciones y hablaré despacio", ["Este año voy a mejorar todo mi inglés y hablar mejor", "Hablaré más en clase para mejorar mi pronunciación"], "La meta concreta tiene acción, cantidad y plazo."),
        arith("Una estudiante tiene 3 errores del primer tipo, 2 del segundo y 1 del tercero. ¿Cuántos errores registró en total?", "3+2+1", "Se suman las frecuencias.", " errores"),
    ],
    [
        mr(LG1, "Una compañera dice que debe practicar primero I went to home porque es el más fácil. ¿Qué respuesta es más acertada?", "Conviene practicar primero el más frecuente", ["Siempre se practica primero el más fácil", "Conviene ignorar los errores pequeños"], "El error más repetido es el que más afecta la comunicación."),
        mc("Un estudiante graba su conversación y la escucha. ¿Qué gana con eso?", "Puede notar errores que no oye mientras habla", ["Puede memorizar lo que dijo para repetirlo", "No gana nada, porque oírse es incómodo"], "La grabación permite revisar con calma."),
    ],
    [
        mr(FD1, "El compañero dijo que usaste muchos conectores. ¿Cómo usas ese dato?", "Como una fortaleza que debes mantener", ["Como un error que debes corregir pronto", "Como algo sin importancia para la meta"], "Los comentarios también muestran fortalezas."),
        mc("Después de corregir un error, ¿qué conviene anotar en tu registro?", "La forma correcta y un ejemplo", ["Solo el error y cuántas veces lo dijiste", "Solo la fecha y la hora de la conversación"], "Con el ejemplo puedes practicar la forma correcta."),
    ],
    [mc("Tras una conversación, notas que repetiste she have y que hablaste rápido. ¿Cuál es el mejor siguiente paso?", "Registrar ambos, fijar una meta para cada uno y practicar", ["Anotar solo she have, porque lo otro no es un error de inglés", "Esperar a la próxima conversación para ver si pasa de nuevo"], "Se registra, se fija meta y se practica.")],
    [
        ("En Inglés de 2.º medio (OA 6, clase 5): ¿qué tres columnas tiene un registro de errores?", "Error, corrección y frecuencia", "Sirven para priorizar."),
        ("En Inglés de 2.º medio (OA 6, clase 5): ¿qué debe tener una buena meta?", "Qué, cuánto y para cuándo", "Así se puede comprobar."),
        ("En Inglés de 2.º medio (OA 6, clase 5): ¿qué recurso ayuda a verificar la forma correcta?", "Un diccionario o una gramática", "Muestran cómo se usa."),
    ],
    task("Después de la actividad de la clase anterior, escribe un registro con tres errores tuyos o del texto de práctica (error, corrección, frecuencia), una meta clara (qué, cuánto, para cuándo) y el recurso que usarás para comprobar. Entrega la hoja a un adulto y explícasela en inglés con tres oraciones.", "Error: I can to swim. Corrección: I can swim. Frecuencia: 3. Error: The people is nice. Corrección: The people are nice. Frecuencia: 2. Error: I went to home. Corrección: I went home. Frecuencia: 1. Meta: para el viernes, usaré can sin to en 10 oraciones. Recurso: diccionario en línea y ejemplos del libro.", ["registro de tres errores con corrección y frecuencia", "una meta concreta", "indica el recurso"], ["registro en la hoja", "nota del adulto"], ["meta vaga", "no anotar la corrección"], "Pide que reescriba su meta si no dice cuánto o para cuándo."),
    "Completa el registro de errores de ejemplo con una cuarta fila que inventes y su corrección.",
    "Revisa cómo hablaste hoy en español y anota una meta clara de comunicación para mañana.",
)
