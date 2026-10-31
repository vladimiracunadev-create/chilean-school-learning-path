"""Cuaderno del estudiante, 6.º básico Inglés (propuesta), EN06 OA 10 (expresarse oralmente en diálogos, presentaciones y actividades grupales con apoyo visual o digital).

Sin audio externo: cada ejercicio escribe los diálogos, carteles y esquemas necesarios.
Los textos son originales. Cada palabra o estructura nueva se explica antes de usarla.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA10 = "EN06 OA 10"


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


# ---------------------------------------------------------------- clase 1: diálogos (propósito y contexto)
D1 = "«A: Hi! I'm Elena. What's your name? B: I'm Kai. Nice to meet you. A: Nice to meet you too. What do you do after school? B: I play the guitar. And you? A: I play volleyball on Tuesdays.» (nice to meet you = mucho gusto, after school = después del colegio, guitar = guitarra, volleyball = vóleibol)"
D2 = "«A: What do you eat for breakfast? B: I eat bread and an egg, and I drink milk. A: Do you eat fruit? B: Yes, I do. I eat an apple every day. A: That's healthy!» (breakfast = desayuno, egg = huevo, drink = tomo, healthy = saludable)"

lesson(
    OA10, 1,
    "Los diálogos escritos en cada ejercicio, lápiz y una hoja; una persona de tu casa para practicar en voz alta.",
    "Aprenderé a expresarme oralmente en un diálogo corto: saludar, presentarme, preguntar y responder según el propósito y el contexto. Sirve para conversar en inglés con un compañero.",
    ["Sé decir hello y my name is.", "Conozco How are you? y I'm fine."],
    [
        "Un diálogo (dialogue) tiene un propósito (purpose) y un contexto (context). El propósito puede ser presentarse, conocer a alguien o pedir información. El contexto es dónde y con quién hablas. En un primer encuentro dices Hi! I'm ___ y Nice to meet you (mucho gusto). Con un amigo, puedes decir What do you do after school? (¿qué haces después de clases?).",
        "Para responder, usa la misma estructura de la pregunta. What's your name? se responde con I'm ___ o My name is ___. Do you eat fruit? se responde con Yes, I do o No, I don't. What do you eat for breakfast? se responde con I eat ___. Después de responder, puedes devolver la pregunta con And you? (¿y tú?). Esa pequeña frase mantiene viva la conversación.",
        "Cuando hables, mira a tu compañero, usa voz clara y espera su respuesta. Si no entiendes, pide ayuda: Sorry, can you repeat? Si te equivocas, corrige y sigue. No tienes que hablar perfecto. Lo importante es que se entienda tu mensaje y que escuches al otro. Practica primero con un modelo y luego cambia un detalle, como el deporte o el desayuno.",
    ],
    [("Nice to meet you", "mucho gusto"), ("What's your name?", "¿cómo te llamas?"), ("And you?", "¿y tú?"), ("Yes, I do / No, I don't", "sí / no (en preguntas con do)"), ("after school", "después de clases"), ("healthy", "saludable")],
    [
        ("Elegir una respuesta adecuada", "Te preguntan: «How are you?». ¿Qué respuesta calza con ese propósito? a) I'm fine, thanks. And you? b) My name is Ana.", ["La pregunta es sobre cómo estoy.", "I'm fine responde cómo estoy.", "Agrego And you? para seguir la conversación."], "a) I'm fine, thanks. And you?"),
        ("Responder con do", "Te preguntan: «Do you play football?». Tú juegas. ¿Qué respondes: Yes, I do o Yes, I am?", ["La pregunta usa do.", "Se responde con do.", "Respondo Yes, I do."], "Yes, I do"),
    ],
    [
        ("Responder «Yes, I am» a una pregunta con Do you...?", "Se usa otro verbo auxiliar.", "Responde con el mismo auxiliar: Do you...? → Yes, I do."),
        ("No devolver la pregunta y dejar la conversación en silencio.", "Falta And you?", "Termina tu respuesta con And you?"),
    ],
    [
        ("Lee: " + D1 + " ¿Cómo se llama el segundo hablante? a) Kai b) Elena", "a) Kai", "Dice I'm Kai."),
        ("Lee: " + D1 + " ¿Qué instrumento toca Kai?", "La guitarra", "Dice I play the guitar."),
        ("Lee: " + D1 + " ¿Qué día juega vóleibol Elena? a) los martes b) los viernes", "a) los martes", "Dice on Tuesdays."),
    ],
    [
        ("Lee: " + D2 + " ¿Qué desayuna B? a) pan y huevo b) jugo y galletas", "a) pan y huevo", "Dice I eat bread and an egg."),
        ("Lee: " + D2 + " ¿Qué bebe B en el desayuno?", "Leche", "Dice I drink milk."),
        ("Lee: " + D2 + " ¿Qué dice A al final? a) That's healthy! b) Goodbye!", "a) That's healthy!", "Es su comentario sobre el desayuno."),
    ],
    [
        ("Completa: «A: Do you eat fruit? B: Yes, I ___.» Opciones: do, am.", "do", "La pregunta usa do."),
        ("Completa: «A: What's your name? B: ___ Diego.» Opciones: I'm, It's.", "I'm", "Para presentarte usas I'm."),
        ("Ordena el diálogo. A) Nice to meet you too. B) Hi! I'm Luz. C) I'm Ben. Nice to meet you.", "B, C, A", "Primero saluda, luego responde y por último contesta el gusto."),
    ],
    [
        ("Un compañero responde «My name is fine» a «How are you?». ¿Qué error cometió?", "Respondió con su nombre, no cómo está", "La respuesta no calza con el propósito de la pregunta."),
        ("Lee: " + D1 + " ¿Cuántas preguntas hace Elena en el diálogo?", "2", "Elena hace dos preguntas."),
    ],
    [
        ("Hay un nuevo compañero en tu curso. ¿Qué dos frases dices para iniciar la conversación? a) Hi! I'm Pablo. Nice to meet you. b) Goodbye, see you tomorrow.", "a) Hi! I'm Pablo. Nice to meet you.", "Saluda y se presenta."),
        ("Lee: " + D2 + " ¿Cuántas cosas distintas para comer o beber nombra B en total, contando el desayuno y la fruta?", "4", "Son bread, egg, milk y apple."),
    ],
    [("Estás en el patio y quieres saber qué deporte juega un compañero. ¿Qué preguntas? a) What sport do you play? b) What's your name?", "a) What sport do you play?", "Pregunta por el deporte.")],
    [
        ("¿Cómo se dice «mucho gusto» en inglés?", "Nice to meet you", "Es una frase de presentación."),
        ("¿Qué significa «And you?»", "¿Y tú?", "Devuelve la pregunta."),
        ("¿Cómo respondes a «Do you like pizza?» si te gusta?", "Yes, I do", "Se responde con do."),
    ],
    task("Escribe un diálogo de cinco turnos entre dos estudiantes que se conocen. Debe incluir: saludo, nombres, Nice to meet you, una pregunta sobre qué hacen después de clases y una respuesta con And you? Usa como modelo D1 y cambia nombres y actividades. Luego practícalo con una persona de tu casa.", "A: Hi! I'm Tomás. What's your name? B: I'm Lía. Nice to meet you. A: Nice to meet you too. What do you do after school? B: I draw. And you? A: I play chess.", ["incluye saludo y nombres", "incluye una pregunta con do y una respuesta", "usa And you?"], ["hoja con el diálogo", "nota de quien lo practicó"], ["respuestas que no calzan con la pregunta", "no devolver la pregunta"], "Reconoce el diálogo completo y practica con la persona la pronunciación de Nice to meet you."),
    "Practica con una persona de tu casa el diálogo D1 cambiando el nombre y la actividad.",
    "Escribe un diálogo de cuatro turnos sobre lo que cada uno come en el almuerzo.",
)

# ---------------------------------------------------------------- clase 2: presentación con apoyo visual (palabras y frases clave)
POSTER = "«Poster title: Save Water. Image 1: a dripping tap. Caption: A tap that drips wastes water. Image 2: a child closing the tap while brushing teeth. Caption: Close the tap. Image 3: a bucket with rain water. Caption: Use rain water for plants.» (dripping = goteando, tap = llave, wastes = desperdicia, closing = cerrando, brushing = cepillándose, bucket = balde, plants = plantas)"
TALK = "«Hello, my topic is saving water. Here you can see a tap that drips. It wastes water. Look at this picture: close the tap when you brush your teeth. Finally, we can use rain water for plants. Thank you.» (here you can see = aquí puedes ver, look at = mira, finally = finalmente)"

lesson(
    OA10, 2,
    "Los carteles y presentaciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a presentar un tema con apoyo visual usando palabras y frases clave para señalar imágenes, como Here you can see y Look at this picture. Sirve para exponer en inglés con un cartel o dibujos.",
    ["Sé que una exposición tiene introducción, desarrollo y cierre.", "Conozco palabras como water, plant y tap."],
    [
        "Una presentación con apoyo visual combina lo que dices con imágenes. Cada imagen tiene una leyenda (caption) breve. Para empezar, di Hello, my topic is ___ (hola, mi tema es ___). Para señalar una imagen, usa Here you can see ___ (aquí puedes ver ___) o Look at this picture (mira esta imagen). Para cerrar, di Thank you.",
        "Las palabras y frases clave son las que más importan: tap, wastes, rain water, plants. Anótalas en tu cartel con letra grande. No escribas oraciones largas: la imagen explica parte del mensaje y tu voz explica el resto. Usa conectores como First, Then y Finally para ordenar las ideas, y habla en presente: «A tap that drips wastes water».",
        "Mientras presentas, señala cada imagen con la mano, mira a tu audiencia y habla despacio. Si olvidas una palabra, mira tu cartel y usa la leyenda. Después de presentar, pregunta Do you have any questions? (¿tienen preguntas?). Practica antes frente a una persona de tu casa y mide el tiempo: una presentación breve dura de uno a dos minutos.",
    ],
    [("topic", "tema"), ("Here you can see...", "aquí puedes ver..."), ("Look at this picture", "mira esta imagen"), ("caption", "leyenda"), ("finally", "finalmente"), ("Do you have any questions?", "¿tienen preguntas?")],
    [
        ("Elegir la frase para señalar", "Quieres mostrar una imagen. ¿Qué dices? a) Here you can see a bucket. b) Goodbye, see you.", ["Quiero señalar una imagen.", "Here you can see señala lo que se ve.", "Goodbye es una despedida."], "a) Here you can see a bucket."),
        ("Palabras clave", "En la leyenda «Close the tap», ¿cuáles son las dos palabras clave?", ["Un verbo de acción importante: close.", "Un sustantivo importante: tap.", "The no es clave."], "close y tap"),
    ],
    [
        ("Escribir párrafos largos en el cartel.", "No se aprovecha la imagen.", "Usa palabras clave y leyendas cortas."),
        ("Presentar sin mirar a la audiencia.", "Se lee todo el tiempo del papel.", "Mira a las personas y apóyate en las imágenes."),
    ],
    [
        ("Lee: " + POSTER + " ¿Cuál es el título del cartel? a) Save Water b) Save Light", "a) Save Water", "Es la primera línea."),
        ("Lee: " + POSTER + " ¿Cuántas imágenes tiene el cartel?", "3", "Son tres imágenes con leyenda."),
        ("Lee: " + POSTER + " ¿Qué dice la leyenda de la segunda imagen? a) Close the tap. b) Use rain water.", "a) Close the tap.", "Es la leyenda de Image 2."),
    ],
    [
        ("Lee: " + TALK + " ¿Qué frase usa el expositor para señalar la imagen? a) Look at this picture b) Thank you", "a) Look at this picture", "Dice Look at this picture."),
        ("Lee: " + TALK + " ¿Cómo empieza la presentación? a) Hello, my topic is saving water. b) Finally, we can use rain water.", "a) Hello, my topic is saving water.", "Es la introducción."),
        ("Lee: " + TALK + " ¿Qué palabra de orden usa para la última idea?", "Finally", "Dice Finally, we can use rain water."),
    ],
    [
        ("Lee: " + POSTER + " ¿Cuál leyenda corresponde a un balde con agua de lluvia? a) Use rain water for plants. b) A tap that drips.", "a) Use rain water for plants.", "Es la leyenda de la tercera imagen."),
        ("Lee: " + TALK + " ¿Qué se debe hacer cuando uno se cepilla los dientes? a) cerrar la llave b) abrir la llave", "a) cerrar la llave", "Dice close the tap when you brush your teeth."),
        ("Lee: " + TALK + " ¿Cuántas acciones para ahorrar agua recomienda la presentación?", "2", "Recomienda cerrar la llave y usar agua de lluvia."),
    ],
    [
        ("Un compañero dice en su presentación «I will read my paper» y no mira la audiencia. ¿Qué debe cambiar? a) mirar a las personas y usar las imágenes b) hablar más rápido", "a) mirar a las personas y usar las imágenes", "Así conecta con el público."),
        ("En la presentación, ¿qué frase usa el expositor para mostrar el tema? a) my topic is saving water b) It wastes water", "a) my topic is saving water", "Presenta el tema."),
    ],
    [
        ("Ordena la presentación. A) Thank you. B) Hello, my topic is recycling. C) Here you can see a paper bin.", "B, C, A", "Primero el tema, luego la imagen y por último el cierre."),
        ("Una presentación tiene 3 imágenes y dura 90 segundos. Si dedicas el mismo tiempo a cada imagen, ¿cuántos segundos dedicas a cada una?", "30", "Se reparten 90 segundos entre tres imágenes.", "90//3"),
    ],
    [("En el diario mural del colegio, ves un cartel con una imagen de un contenedor y la leyenda «Put paper here». (paper = papel, put = pon). ¿Qué te indica la leyenda?", "Que ahí se pone el papel", "Es una instrucción simple.")],
    [
        ("¿Qué frase sirve para señalar una imagen?", "Here you can see...", "Presenta lo que se ve."),
        ("¿Qué es una leyenda?", "Una frase corta que explica una imagen", "Acompaña a la imagen."),
        ("¿Qué dices al terminar?", "Thank you", "Es el cierre."),
    ],
    task("Dibuja un cartel con el título «Healthy Food» y tres imágenes: una manzana, un vaso con agua y un plato con verduras. Escribe una leyenda de cuatro palabras como máximo bajo cada imagen. Luego escribe una presentación de cinco oraciones: tema, tres imágenes con Here you can see... y cierre. Practícala en voz alta frente a una persona de tu casa.", "Hello, my topic is healthy food. Here you can see an apple. Here you can see a glass of water. Here you can see vegetables. Thank you.", ["el cartel tiene título y tres imágenes con leyendas cortas", "la presentación tiene tema, tres imágenes y cierre", "habla mirando a la audiencia"], ["hoja con cartel y texto", "nota de quien escuchó"], ["leyendas muy largas", "olvidar el cierre"], "Reconoce el cartel ordenado y practica con la persona la frase Here you can see."),
    "Dibuja tres imágenes de un tema y di una frase con Here you can see... para cada una.",
    "Prepara una presentación de un minuto sobre tu animal favorito con un cartel de tres imágenes.",
)

# ---------------------------------------------------------------- clase 3: actividad grupal
GROUP = "«Task: plan a class garden. Roles: the Leader asks questions, the Secretary writes ideas, the Timekeeper checks the time and the Speaker shares with the class. Leader: What do we need for the garden? Secretary: I will write: soil, seeds and water. Timekeeper: We have five minutes. Speaker: I can present our ideas.» (leader = líder, secretary = secretario, timekeeper = controlador del tiempo, speaker = vocero, soil = tierra, seeds = semillas)"

lesson(
    OA10, 3,
    "Los diálogos de grupo escritos en cada ejercicio, lápiz y una hoja; dos o tres personas de tu casa si quieres practicar.",
    "Aprenderé a participar en una actividad grupal en inglés con roles y frases para turnos, acuerdos y desacuerdos. Sirve para trabajar en equipo y expresar ideas.",
    ["Sé decir I agree y I disagree.", "Conozco palabras como garden, seeds y water."],
    [
        "En una actividad grupal cada persona puede tener un rol (role): leader (líder, hace preguntas y dirige), secretary (secretario, anota las ideas), timekeeper (controla el tiempo) y speaker (vocero, presenta al curso). Los roles ayudan a que todos participen y el trabajo sea ordenado.",
        "Hay frases útiles para trabajar en grupo. What do you think? (¿qué piensas?) pide una opinión. I agree (estoy de acuerdo) y I disagree (no estoy de acuerdo) responden. Can I add something? (¿puedo agregar algo?) pide el turno. It's your turn (es tu turno) da la palabra a otro. Let's vote (votemos) sirve para decidir. Let's start (comencemos) inicia la tarea.",
        "Para hablar bien en grupo, escucha a los demás, no interrumpas y espera tu turno. Cuando no estés de acuerdo, hazlo con respeto: I see your point, but I think... Antes de terminar, el speaker resume las ideas: «We decided to plant flowers and vegetables». Así, todos saben qué se acordó y la actividad termina con un resultado claro.",
    ],
    [("leader / secretary", "líder / secretario"), ("timekeeper / speaker", "controlador del tiempo / vocero"), ("What do you think?", "¿qué piensas?"), ("It's your turn", "es tu turno"), ("Let's vote", "votemos"), ("Can I add something?", "¿puedo agregar algo?")],
    [
        ("Reconocer un rol", "En el grupo, una persona controla que no se pase el tiempo. ¿Qué rol es: Timekeeper o Speaker?", ["Controlar el tiempo es el trabajo del Timekeeper.", "Speaker presenta al curso.", "Elijo Timekeeper."], "Timekeeper"),
        ("Elegir la frase para pedir opinión", "Quieres saber qué piensa tu compañera. ¿Qué dices? a) What do you think? b) It's my turn.", ["Busco una pregunta que pida opinión.", "What do you think? lo hace.", "It's my turn habla de mi turno."], "a) What do you think?"),
    ],
    [
        ("Interrumpir a un compañero.", "Se habla sin esperar el turno.", "Espera y usa Can I add something?"),
        ("Decir «You are wrong» sin explicar.", "Falta respeto y razón.", "Di I see your point, but I think... y explica."),
    ],
    [
        ("Lee: " + GROUP + " ¿Qué quiere planificar el grupo? a) un jardín de curso b) una fiesta", "a) un jardín de curso", "Dice plan a class garden."),
        ("Lee: " + GROUP + " ¿Quién escribe las ideas?", "El secretario", "Dice the Secretary writes ideas."),
        ("Lee: " + GROUP + " ¿Cuántos roles tiene el grupo?", "4", "Son Leader, Secretary, Timekeeper y Speaker."),
    ],
    [
        ("Lee: " + GROUP + " ¿Cuántos minutos tiene el grupo?", "5", "Dice five minutes."),
        ("Lee: " + GROUP + " ¿Qué cosas anota el secretario? a) tierra, semillas y agua b) lápices y cuadernos", "a) tierra, semillas y agua", "Dice soil, seeds and water."),
        ("Lee: " + GROUP + " ¿Quién va a presentar las ideas al curso?", "El vocero", "Dice Speaker: I can present our ideas."),
    ],
    [
        ("Para dar la palabra a un compañero, ¿qué dices? a) It's your turn b) Let's vote", "a) It's your turn", "Da el turno a otra persona."),
        ("Para decidir entre dos ideas, ¿qué dices? a) Let's vote b) It's your turn", "a) Let's vote", "Votar sirve para decidir."),
        ("Para estar de acuerdo con una idea, ¿qué dices? a) I agree b) I disagree", "a) I agree", "I agree significa estoy de acuerdo."),
    ],
    [
        ("Lee este mini diálogo: «Leader: What flowers do we want? Ana: I like roses. Leo: I prefer sunflowers. Leader: Let's vote.» (roses = rosas, sunflowers = girasoles). ¿Cuántos estudiantes dan una opinión?", "2", "Opinan Ana y Leo."),
        ("En el mismo diálogo, ¿qué propone el líder para decidir?", "Votar", "Dice Let's vote."),
    ],
    [
        arith("Cuatro integrantes comparten 20 minutos por igual para exponer sus ideas. ¿Cuántos minutos tiene cada uno?", "20//4", "Se reparten 20 minutos entre 4 personas."),
        ("En una votación sobre tres ideas: 4 votos para roses, 3 para sunflowers y 2 para daisies (margaritas). ¿Cuántos votos hubo?", "9", "Se suman todos los votos.", "4+3+2"),
    ],
    [("En tu grupo, una compañera nunca habla. ¿Qué frase le puedes decir? a) What do you think? b) Be quiet.", "a) What do you think?", "Invita a participar con respeto.")],
    [
        ("¿Qué hace el timekeeper?", "Controla el tiempo", "Es su rol."),
        ("¿Qué significa «It's your turn»?", "Es tu turno", "Da la palabra."),
        ("¿Qué dices para pedir la palabra?", "Can I add something?", "Es una forma cortés."),
    ],
    task("Con dos o tres personas de tu casa, hagan una actividad grupal de cuatro minutos. La tarea es: decidir qué fruta llevar a un picnic entre apples, grapes y pears (grapes = uvas, pears = peras). Reparte los roles: Leader, Secretary, Timekeeper y Speaker (si son menos, una persona hace dos roles). Usa al menos tres frases: What do you think?, I agree o I disagree, y Let's vote. Escribe en tu hoja la decisión final y quién habló.", "Leader: What fruit do we take? Ana: I like apples. Leo: I prefer grapes. Leader: Let's vote. Secretary: Two votes for grapes. Speaker: We decided to take grapes.", ["asigna los cuatro roles", "usa al menos tres frases de grupo", "escribe la decisión final"], ["hoja con roles, frases y decisión", "nota de quien participó"], ["una sola persona habla", "no registra la decisión"], "Reconoce la participación de cada persona y practica la frase Can I add something? en el siguiente turno."),
    "Pide a una persona de tu casa que haga de Leader y responde con I agree o I disagree a tres ideas.",
    "Escribe cuatro frases que usarías para trabajar en equipo.",
)

# ---------------------------------------------------------------- clase 4: apoyo digital o visual (diapositivas)
SLIDES = "«Slide 1: Title: My Healthy Day. Picture: a sun. Slide 2: Breakfast: bread, egg, milk. Picture: a plate. Slide 3: Exercise: football, 30 minutes. Picture: a ball. Slide 4: Sleep: 9 hours. Picture: a moon. Slide 5: Thank you.» (slide = diapositiva, plate = plato, exercise = ejercicio, sleep = dormir, hours = horas)"

lesson(
    OA10, 4,
    "Las diapositivas escritas en cada ejercicio, lápiz y papel (puedes hacer diapositivas en papel si no tienes computador).",
    "Aprenderé a planificar y presentar con diapositivas, digitales o en papel, usando títulos cortos, imágenes y palabras clave. Sirve para exponer en inglés con apoyo visual o digital.",
    ["Sé que una presentación tiene introducción, desarrollo y cierre.", "Conozco palabras como title, picture y hours."],
    [
        "Una diapositiva (slide) tiene un título corto, una imagen y dos o tres palabras clave. No se escriben oraciones largas: la audiencia debe mirar la imagen y escucharte. Las diapositivas se pueden hacer en un programa digital o con hojas de papel. La regla es la misma: poco texto, letra grande y una imagen clara.",
        "Una presentación breve tiene tres partes. La primera diapositiva es el título (Title). Las del medio entregan los datos: una idea por diapositiva. La última dice Thank you. Cuando presentes, di una o dos oraciones por diapositiva: «Slide 3: I play football for thirty minutes every day». Usa palabras de orden como First, Then y Finally.",
        "Antes de presentar, practica con un cronómetro. Si tienes dos minutos y cuatro diapositivas de contenido, hablas treinta segundos en cada una. Revisa con una lista: ¿se lee la letra?, ¿hay una imagen por diapositiva?, ¿digo el número correcto de horas o minutos?, ¿miro al público? Si no tienes computador, pega tus papeles en la pared y señala cada uno.",
    ],
    [("slide", "diapositiva"), ("title", "título"), ("picture", "imagen"), ("key words", "palabras clave"), ("hours / minutes", "horas / minutos"), ("Thank you", "gracias: cierre")],
    [
        ("Contar diapositivas", "Lee una presentación: Slide 1: título. Slide 2: desayuno. Slide 3: ejercicio. Slide 4: dormir. Slide 5: cierre. ¿Cuántas diapositivas tiene?", ["Cuento los números de slide.", "Hay cinco.", "El total es 5."], "5"),
        ("Palabras clave de una diapositiva", "Si la diapositiva es sobre el desayuno y tiene «Breakfast: bread, egg, milk», ¿cuáles son los tres alimentos?", ["Después de los dos puntos hay tres palabras.", "Son bread, egg y milk.", "Esos son los alimentos."], "bread, egg y milk"),
    ],
    [
        ("Llenar la diapositiva con párrafos largos.", "La audiencia lee y no escucha.", "Usa un título, una imagen y dos o tres palabras clave."),
        ("No ensayar el tiempo.", "La presentación se pasa de largo.", "Practica con cronómetro y reparte el tiempo entre diapositivas."),
    ],
    [
        ("Lee: " + SLIDES + " ¿Cuál es el título de la presentación? a) My Healthy Day b) Thank you", "a) My Healthy Day", "Es el título de la primera diapositiva."),
        ("Lee: " + SLIDES + " ¿Cuántas diapositivas tiene?", "5", "Se numeran del 1 al 5."),
        ("Lee: " + SLIDES + " ¿Qué dice la última diapositiva? a) Thank you b) Sleep", "a) Thank you", "Cierra la presentación."),
    ],
    [
        ("Lee: " + SLIDES + " ¿Cuántos minutos hace ejercicio?", "30", "Dice football, 30 minutes."),
        ("Lee: " + SLIDES + " ¿Cuántas horas duerme?", "9", "Dice Sleep: 9 hours."),
        ("Lee: " + SLIDES + " ¿Qué imagen acompaña la diapositiva de dormir? a) una luna b) un sol", "a) una luna", "Dice Picture: a moon."),
    ],
    [
        arith("Lee: " + SLIDES + " Un día tiene 24 horas. Si duerme 9, ¿cuántas horas pasa despierto?", "24-9", "Se resta lo que duerme del total de horas."),
        ("Lee: " + SLIDES + " Presentas las 3 diapositivas de contenido (breakfast, exercise y sleep) en 90 segundos, con el mismo tiempo para cada una. ¿Cuántos segundos hablas en cada una?", "30", "Se reparten 90 segundos entre tres diapositivas.", "90//3"),
        ("Lee: " + SLIDES + " ¿Qué frase dices para la diapositiva de ejercicio? a) I play football for thirty minutes. b) I sleep nine hours.", "a) I play football for thirty minutes.", "Calza con la información de esa diapositiva."),
    ],
    [
        ("Un compañero llenó una diapositiva con diez líneas de texto. ¿Qué debe hacer? a) dejar un título, una imagen y tres palabras clave b) agregar más líneas", "a) dejar un título, una imagen y tres palabras clave", "Es más claro para la audiencia."),
        ("Una diapositiva dice «Exercise: football, 30 minutes» pero el expositor dice «sixty minutes». ¿Qué debe corregir?", "Decir thirty minutes", "Lo que dice debe coincidir con la diapositiva."),
    ],
    [
        ("Ordena las diapositivas de una presentación. A) Thank you B) Title C) Content", "B, C, A", "Primero el título, luego el contenido y al final el cierre."),
        ("Una presentación tiene 1 título, 4 diapositivas de contenido y 1 de cierre. ¿Cuántas diapositivas son?", "6", "Se suman todas las diapositivas.", "1+4+1"),
    ],
    [("En el computador del colegio no hay internet. ¿Qué alternativa tienes para tu presentación? a) hacer diapositivas en hojas de papel b) cancelar la presentación", "a) hacer diapositivas en hojas de papel", "Sirve igual con las mismas reglas.")],
    [
        ("¿Qué lleva una buena diapositiva?", "Título, imagen y palabras clave", "Lleva poco texto."),
        ("¿Qué haces antes de presentar?", "Ensayo con cronómetro", "Así controlo el tiempo."),
        ("¿Cómo se cierra una presentación?", "Con Thank you", "Es una despedida."),
    ],
    task("Planifica una presentación de cinco diapositivas (o cinco hojas de papel) con el título «My Weekend». Slide 1: título e imagen. Slides 2 a 4: tres actividades del fin de semana con una imagen y dos palabras clave cada una (por ejemplo, Saturday: park, football). Slide 5: Thank you. Escribe qué dirás en cada diapositiva con una oración en inglés. Practica con un cronómetro: dos minutos en total.", "Slide 1: My Weekend. Slide 2: Saturday: park, football. I play football in the park. Slide 3: Sunday: lunch, cousins. I eat lunch with my cousins. Slide 4: Sunday: movie. I watch a movie. Slide 5: Thank you.", ["cinco diapositivas ordenadas", "cada diapositiva tiene imagen y palabras clave", "la presentación dura dos minutos"], ["hoja con el plan de diapositivas", "nota de quien escuchó"], ["demasiado texto", "olvidar el cierre"], "Reconoce el plan ordenado y revisa el tiempo con la persona."),
    "Ensaya tu presentación frente a un espejo con un cronómetro y apunta cuánto duró.",
    "Prepara una segunda presentación de tres diapositivas sobre tu deporte favorito.",
)
