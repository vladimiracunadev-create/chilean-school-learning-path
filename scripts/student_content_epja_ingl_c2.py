"""Inglés EPJA Nivel 2, módulo 3 (parte 2): OAD-10, preguntar y contar proyectos personales con las expresiones I want to, I'm going to e I would like to. Todos los textos son inventados."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-10"

F1 = ("Texto de ejemplo, Ana habla de sus planes: «My name is Ana. I want to study nursing. I'm going to buy a book this month. "
      "I would like to visit the south next year.»")

F2 = ("Texto de ejemplo, los planes de Mr. Perez: «I want to open a small shop. I'm going to save money every month. This week I'm going to learn English. "
      "Next year I would like to buy a bike for my son.»")

F3 = ("Diálogo de ejemplo. Mary: What are you going to study? / John: I'm going to study cooking. / Mary: Are you going to work too? / "
      "John: Yes, I am. I'm going to work at night. / Mary: Would you like to open a restaurant? / John: Yes, I would. Someday.")

F4 = (GUION + "Transcripción de un diálogo de ejemplo. Carlos: What are you going to do this weekend, Marta? / Marta: I'm going to visit my mother. "
      "I'm not going to work on Sunday. / Carlos: What do you want to do next year? / Marta: I want to learn computer skills. I would like to find a new job.")

F5 = ("Mensaje de ejemplo de Rosa a un grupo de la comunidad: «Hello, my name is Rosa. I want to sell bread in the neighborhood. "
      "I'm going to buy flour on Monday and I'm going to bake on Tuesday. I'm not going to sell on Sunday. Would you like to help me? Please call me.»")

F6 = ("Texto de repaso, los planes de Pedro: «I want to finish school this year. I'm going to study at night. "
      "I would like to work in an office. I'm not going to travel this summer, because I want to save money.»")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy reconozco frases en inglés para contar lo que quiero hacer y entiendo los planes de una persona en un texto corto.",
    prior=["Cuento mis planes en español: lo que quiero estudiar, comprar o hacer.", "Reconozco palabras de la vida diaria en inglés.", "Sé que una frase en inglés tiene sujeto y verbo."],
    explain=[
        "Todas las personas tienen proyectos: estudiar, ahorrar, abrir un negocio, viajar. En inglés hay tres expresiones muy útiles para contarlos. Aquí las aprenderás completas, sin teoría de tiempos nuevos: I want to… (quiero…), I'm going to… (voy a…) e I would like to… (me gustaría…).",
        "Después de cada una va un verbo simple: «I want to study», «I'm going to buy», «I would like to visit». No se agrega -s ni -ing al verbo. Las tres sirven para hablar del futuro, pero la primera dice un deseo, la segunda un plan decidido y la tercera una forma más amable de decirlo.",
        "Para leer un texto sobre planes, busca estas expresiones: lo que sigue es el proyecto. Ejemplo: «I want to study nursing» quiere decir que la persona quiere estudiar enfermería. Subraya la expresión y el verbo para no perderte.",
    ],
    vocab=[("I want to", "quiero"), ("I'm going to", "voy a"), ("I would like to", "me gustaría"), ("study", "estudiar"), ("buy", "comprar"), ("visit", "visitar"), ("next year", "el próximo año")],
    worked=[
        ("Entender un plan", "Oración de ejemplo: «I want to study nursing.»", ["Subrayo la expresión: I want to (quiero).", "El verbo que sigue es study (estudiar).", "Lo que sigue es nursing (enfermería)."], "Quiero estudiar enfermería"),
        ("Distinguir un plan de un deseo amable", "Oraciones de ejemplo: «I'm going to buy a book» y «I would like to visit the south».", ["La primera es un plan decidido: voy a comprar.", "La segunda es un deseo dicho con amabilidad: me gustaría visitar.", "Ambas hablan del futuro."], "La primera es un plan; la segunda, un deseo amable"),
    ],
    mistakes=[("Escribir «I want study».", "Falta la palabra to entre want y el verbo.", "Escribe «I want to study»."),
              ("Escribir «I'm going to buying a book».", "Después de going to el verbo va simple, sin -ing.", "Escribe «I'm going to buy a book».")],
    T=[
        ("abc", "{F} ¿Qué quiere estudiar Ana?", "Enfermería", "Cocina", "Computación", "Ana dice «I want to study nursing», que es estudiar enfermería."),
        ("ab", "{F} ¿Qué va a comprar Ana este mes?", "Un libro", "Un auto", "Ana dice «I'm going to buy a book this month»."),
        ("abc", "{F} ¿Qué significa «I would like to»?", "me gustaría", "tengo que", "no quiero", "Would like to es una forma amable de decir me gustaría."),
        ("abc", "{F} ¿A dónde le gustaría viajar a Ana el próximo año?", "Al sur", "Al norte", "Al centro", "El texto dice que le gustaría visitar el sur."),
        ("abc", "¿Qué significa «I'm going to study» en un plan de estudio?", "Voy a estudiar", "Estudié", "Me gusta estudiar", "I'm going to más un verbo expresa algo que se va a hacer."),
        ("{F} ¿En qué mes va Ana a comprar el libro? Responde con la expresión en inglés que usa el texto para el tiempo.", "this month", "El texto usa this month, que quiere decir este mes."),
        ("abc", "Completa: I want ___ learn English.", "to", "at", "of", "Después de want se pone to antes del verbo."),
        ("abc", "Elige la oración correcta para decir «Voy a comprar pan».", "I'm going to buy bread.", "I'm going to buying bread.", "I going to buy bread.", "El verbo queda simple y no falta am (I'm)."),
        ("Ordena las palabras: want / to / I / cook.", "I want to cook.", "La estructura es sujeto, want, to y el verbo simple."),
        ("ab", "Una persona dice «I want to travel» y otra «I'm going to travel on Friday». ¿Quién tiene un plan más firme?", "La segunda, con I'm going to", "La primera, con I want to", "I'm going to expresa un plan decidido, no solo un deseo."),
        ("ab", "Verdadero o falso razonado: «I would like to» es una forma más amable que «I want to».", "Verdadero: suena más cortés", "Falso: es más seca", "Would like to se usa para pedir o desear con cortesía."),
        ("abc", "{F} ¿Cuál afirmación es falsa?", "Ana is going to buy a car.", "Ana wants to study nursing.", "Ana would like to visit the south.", "Ana va a comprar un libro, no un auto."),
        ("abc", "¿Cuál oración tiene un error?", "I want study nursing.", "I want to study nursing.", "I would like to study nursing.", "Falta to después de want en la primera."),
    ],
    ctx=("abc", "Un asistente en un centro de capacitación de ejemplo te pregunta tus planes y tú quieres decir con amabilidad que te gustaría aprender inglés. ¿Qué dices?", "I would like to learn English.", "I would like learn English.", "I am going to learned English.", "Would like to más el verbo simple es la forma amable correcta."),
    sc=[("En Inglés: ¿qué significa «I want to»?", "quiero", "I want to introduce un deseo o proyecto."),
        ("En Inglés: ¿cómo se dice «voy a comprar»?", "I'm going to buy", "I'm going to más verbo simple expresa un plan."),
        ("En Inglés: ¿qué falta en «I want ___ study»?", "to", "Entre want y el verbo se pone to.")],
    op=("Con {F} como modelo, escribe o di tres oraciones en inglés sobre proyectos tuyos o inventados: una con I want to, una con I'm going to y una con I would like to.",
        "I want to learn computer skills. I'm going to buy a notebook. I would like to open a small shop.",
        ["usa las tres expresiones", "cada una con verbo simple", "habla de proyectos distintos"],
        ["tres oraciones dichas o escritas"],
        ["olvidar to después de want", "agregar -ing al verbo"],
        "Pregunta: «¿Cuál de los tres proyectos quieres cumplir primero?»"),
    reinforce="Copia las tres expresiones con su significado en una tarjeta y léelas en voz alta cada día.",
    extend="Escribe en inglés dos proyectos reales o inventados de alguien de tu familia y subraya la expresión que usaste.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo palabras para hablar de proyectos y de cuándo se harán.",
    prior=["Reconozco I want to, I'm going to e I would like to.", "Sé decir cuándo haré algo: esta semana, el próximo año.", "Hablo de mis planes en español."],
    explain=[
        "Los proyectos tienen acciones y tiempos. Hoy aprendes verbos de proyectos: open (abrir), save (ahorrar), learn (aprender), buy (comprar), find (encontrar) y finish (terminar).",
        "También necesitas palabras de tiempo: this week (esta semana), this month (este mes), next year (el próximo año), tomorrow (mañana). Se ponen al comienzo o al final de la oración: «This week I'm going to learn English» o «I'm going to learn English this week».",
        "Para leer un texto con planes, busca cada expresión de proyecto, el verbo que le sigue y la palabra de tiempo. Así respondes qué, para qué y cuándo. Recuerda: después de want to, going to y would like to, el verbo va simple.",
    ],
    vocab=[("open", "abrir"), ("save", "ahorrar, guardar"), ("learn", "aprender"), ("find", "encontrar"), ("finish", "terminar"), ("this week", "esta semana"), ("tomorrow", "mañana")],
    worked=[
        ("Leer qué, y cuándo", "Oración de ejemplo: «This week I'm going to learn English.»", ["Busco el tiempo: this week, esta semana.", "Busco la expresión: I'm going to.", "El verbo es learn y el tema es English."], "Esta semana voy a aprender inglés"),
        ("Armar un plan con tiempo", "Dato de ejemplo: abrir un negocio el próximo año.", ["La expresión de deseo: I want to.", "El verbo: open.", "La palabra de tiempo: next year."], "I want to open a business next year"),
    ],
    mistakes=[("Escribir «I want to save the money every month» con artículo de más.", "Se traduce palabra por palabra del español.", "Se dice «I want to save money every month»."),
              ("Confundir learn con teach.", "Se parecen y los dos tienen que ver con aprender.", "Learn es aprender; teach es enseñar.")],
    T=[
        ("abc", "{F} ¿Qué quiere abrir Mr. Perez?", "Una tienda pequeña", "Un taller de autos", "Un banco", "El texto dice «I want to open a small shop»."),
        ("ab", "{F} ¿Qué va a hacer con el dinero cada mes?", "Va a ahorrarlo", "Lo va a gastar", "El texto dice «I'm going to save money every month»."),
        ("abc", "{F} ¿Qué va a aprender esta semana?", "Inglés", "Cocina", "Computación", "El texto dice que esta semana va a aprender inglés."),
        ("abc", "{F} ¿Para quién le gustaría comprar una bicicleta?", "Para su hijo", "Para su esposa", "Para su jefe", "El texto dice «a bike for my son», o sea para su hijo."),
        ("abc", "¿Qué significa «this week»?", "esta semana", "el año pasado", "mañana", "This week es el tiempo de la semana actual."),
        ("{F} ¿Cuándo le gustaría a Mr. Perez comprar la bicicleta? Escribe la expresión en inglés.", "next year", "El texto dice «Next year I would like to buy a bike»."),
        ("abc", "Completa: I'm going to ___ money.", "save", "saves", "saving", "Después de going to el verbo va simple: save."),
        ("abc", "¿Qué oración dice «Mañana voy a terminar»?", "Tomorrow I'm going to finish.", "Tomorrow I finish going.", "I going to finish tomorrow.", "Se usa I'm going to más el verbo simple, y tomorrow al principio."),
        ("Ordena las palabras: to / I / find / a job / want.", "I want to find a job.", "La estructura es sujeto, want to, verbo y el resto."),
        ("ab", "Una persona dice «I want to learn computer skills» y otra dice «I want to teach computer skills». ¿Quién quiere estudiar?", "La primera, con learn", "La segunda, con teach", "Learn es aprender y teach es enseñar."),
        ("ab", "Verdadero o falso razonado: «Next year» y «this week» significan lo mismo.", "Falso: next year es el próximo año y this week es esta semana", "Verdadero: ambos son el futuro", "Next year es el próximo año; this week es esta semana."),
        ("abc", "{F} ¿Cuál afirmación es correcta?", "Mr. Perez wants to open a small shop.", "Mr. Perez wants to close a small shop.", "Mr. Perez is going to sell a bike.", "El texto dice que quiere abrir un negocio pequeño."),
        ("abc", "¿Cuál oración tiene un error?", "I'm going to learning English.", "I'm going to learn English.", "I want to learn English.", "Después de going to el verbo va simple, no con -ing."),
    ],
    ctx=("abc", "En un taller de emprendimiento de ejemplo te piden que escribas qué vas a hacer este mes. Piensas guardar dinero. ¿Qué escribes?", "I'm going to save money this month.", "I'm going to saving money this month.", "I going save money this month.", "Se usa I'm going to más el verbo save, y el tiempo al final."),
    sc=[("En Inglés: ¿qué significa «save»?", "ahorrar, guardar", "Save también se usa para ahorrar dinero."),
        ("En Inglés: ¿cuál palabra significa «el próximo año»?", "next year", "Next year indica el año que viene."),
        ("En Inglés: ¿cómo se dice «abrir»?", "open", "Open es abrir, como un negocio.")],
    op=("Con {F} como modelo, escribe tres oraciones sobre proyectos tuyos o inventados, cada una con una expresión de proyecto, un verbo de la clase y una palabra de tiempo.",
        "I'm going to learn English this month. I want to save money next year. I would like to open a small shop someday.",
        ["usa un verbo de la clase", "usa una palabra de tiempo", "el verbo va simple"],
        ["tres oraciones escritas"],
        ["agregar -ing después de going to", "olvidar la palabra de tiempo"],
        "Pregunta: «¿Qué proyecto necesita más tiempo?»"),
    reinforce="Haz una tabla con los seis verbos y escribe una oración corta con cada uno.",
    extend="Escribe una lista de cinco proyectos de tu comunidad (inventados) con los verbos de la clase.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a preguntar por los planes de otra persona y a responder.",
    prior=["Uso I'm going to, I want to e I would like to.", "Sé que una pregunta cambia el orden de las palabras.", "Entiendo un diálogo corto."],
    explain=[
        "Para preguntar por planes se usa la expresión completa «What are you going to…?», que quiere decir ¿qué vas a…?. Se aprende como una frase útil: «What are you going to study?», «What are you going to buy?».",
        "Para preguntas de sí o no se usa «Are you going to…?». Se responde «Yes, I am» o «No, I'm not». Con he o she: «Is he going to…?» y «Yes, he is». Para una pregunta amable: «Would you like to…?», y se responde «Yes, I would» o «No, I wouldn't».",
        "Paso a paso para preguntar: primero elige la pregunta (What para saber qué, Are para sí o no), pon are y you, agrega going to y termina con el verbo simple. Para responder: usa I'm going to y el verbo simple. No hace falta cambiar nada más.",
    ],
    vocab=[("What are you going to…?", "¿Qué vas a…?"), ("Yes, I am", "Sí, voy a hacerlo"), ("No, I'm not", "No, no voy a hacerlo"), ("Would you like to…?", "¿Te gustaría…?"), ("someday", "algún día"), ("too", "también")],
    worked=[
        ("Armar una pregunta", "Quiero preguntar a Mary qué va a comprar.", ["Empiezo con What.", "Agrego are you going to.", "Termino con el verbo simple: buy."], "What are you going to buy?"),
        ("Responder sí o no", "Pregunta de ejemplo: «Are you going to work at night?» (sí).", ["La pregunta usa are y you.", "Respondo con am porque hablo de mí.", "Si es sí: Yes, I am."], "Yes, I am"),
    ],
    mistakes=[("Responder «Yes, I do» a «Are you going to…?».", "Se mezcla con las preguntas que usan do.", "Con are la respuesta es «Yes, I am»."),
              ("Preguntar «What you are going to study?».", "Se deja el orden de la oración afirmativa.", "En pregunta va primero are: «What are you going to study?».")],
    T=[
        ("abc", "{F} ¿Qué va a estudiar John?", "Cocina", "Enfermería", "Inglés", "John dice «I'm going to study cooking»."),
        ("ab", "{F} ¿John va a trabajar también?", "Sí, de noche", "No, nunca", "John dice «Yes, I am. I'm going to work at night»."),
        ("abc", "{F} ¿Qué le gustaría abrir algún día a John?", "Un restaurante", "Una tienda", "Una escuela", "Mary pregunta por un restaurante y John dice Yes, I would."),
        ("abc", "¿Qué pregunta quiere decir «¿Qué vas a comprar?»?", "What are you going to buy?", "What you are going to buy?", "What do you going to buy?", "En una pregunta va primero are, antes de you."),
        ("abc", "¿Cuál es la respuesta correcta a «Are you going to travel?» si quieres decir sí?", "Yes, I am.", "Yes, I do.", "Yes, I would.", "Con Are you going to… la respuesta corta usa am."),
        ("abc", "¿Cuál es la respuesta correcta a «Would you like to study English?» si quieres decir sí?", "Yes, I would.", "Yes, I am.", "Yes, I do.", "A una pregunta con would you like se responde con would."),
        ("Ordena las palabras para preguntar: are / what / you / going to / do.", "What are you going to do?", "Después de what van are y you, antes de going to."),
        ("abc", "Completa: Are you going ___ study?", "to", "at", "for", "En esta expresión siempre se pone going to antes del verbo."),
        ("abc", "Completa la respuesta negativa: «Are you going to sell?» «No, I'm ___.»", "not", "don't", "isn't", "La respuesta corta negativa de am es No, I'm not."),
        ("ab", "Mary pregunta «Is he going to study?». ¿Qué respuesta corta es correcta si la respuesta es sí?", "Yes, he is", "Yes, he does", "Con is en la pregunta, se responde con is."),
        ("ab", "Verdadero o falso razonado: en «What are you going to study?» el verbo study lleva -s.", "Falso: va simple, sin -s", "Verdadero: siempre lleva -s", "Después de going to el verbo queda en su forma simple."),
        ("abc", "{F} ¿Qué respuesta de John muestra un sueño y no un plan firme?", "Yes, I would. Someday.", "Yes, I am.", "I'm going to study cooking.", "Someday quiere decir algún día, o sea que es un deseo de largo plazo."),
        ("abc", "¿Cuál pregunta tiene un error?", "What you are going to buy?", "What are you going to buy?", "Are you going to buy a bike?", "En la primera, are debe ir antes de you."),
    ],
    ctx=("abc", "Una compañera nueva te cuenta que va a estudiar peluquería y tú quieres preguntarle si también va a trabajar. ¿Qué preguntas?", "Are you going to work too?", "Are you go to work too?", "Do you going to work too?", "Con going to, la pregunta de sí o no empieza con are."),
    sc=[("En Inglés: ¿cómo preguntas «¿Qué vas a estudiar?»?", "What are you going to study?", "What, are you y going to forman la pregunta."),
        ("En Inglés: ¿cómo respondes que no a «Are you going to buy a car?»?", "No, I'm not", "La respuesta negativa corta usa I'm not."),
        ("En Inglés: ¿cómo respondes que sí a «Would you like to travel?»?", "Yes, I would", "Se responde con would, no con do.")],
    op=("Imagina que hablas con una persona de tu curso. Escribe cuatro líneas de un diálogo de ejemplo con {F} como modelo: dos preguntas sobre planes y sus respuestas. Usa datos inventados.",
        "A: What are you going to study? B: I'm going to study English. A: Are you going to work too? B: Yes, I am.",
        ["una pregunta con What", "una pregunta de sí o no", "dos respuestas"],
        ["cuatro líneas de diálogo"],
        ["poner you antes de are", "agregar -s o -ing al verbo"],
        "Pregunta: «¿Se entiende quién pregunta y quién responde?»"),
    reinforce="Escribe cinco preguntas con What are you going to… y respóndelas con datos de ejemplo.",
    extend="Practica el diálogo en voz alta con otra persona, cambiando los datos.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: escucho un diálogo sobre proyectos y respondo preguntas sencillas.",
    prior=["Hago preguntas con What are you going to…?", "Respondo Yes, I am y No, I'm not.", "Sé leer un diálogo corto."],
    explain=[
        "En esta clase practicas la escucha sin audio. Otra persona lee en voz alta el guion, o lo lees tú en voz baja, despacio. En una primera lectura, solo busca de qué trata: ¿qué planes cuentan las personas?",
        "En la segunda lectura, subraya las expresiones de proyecto (I'm going to, I want to, I would like to) y las palabras de tiempo. Hoy aparece la negación «I'm not going to…», que quiere decir no voy a…. Es una frase completa muy útil: «I'm not going to work on Sunday».",
        "Al responder, usa oraciones completas y el verbo simple. Si te piden un dato, cópialo del texto. Así practicas lo que entendiste y el orden de las palabras.",
    ],
    vocab=[("weekend", "fin de semana"), ("I'm not going to", "no voy a"), ("computer skills", "manejo de computador"), ("find a job", "encontrar trabajo"), ("new", "nuevo"), ("mother", "madre")],
    worked=[
        ("Responder con datos del diálogo", "Pregunta de ejemplo: «What is Marta going to do this weekend?»", ["Busco la respuesta en el texto: visit her mother.", "Uso la expresión: is going to.", "Armo la respuesta con she."], "She is going to visit her mother"),
        ("Usar la negación", "Dato de ejemplo: Marta no va a trabajar el domingo.", ["La expresión negativa es is not o isn't.", "Agrego going to.", "El verbo es work."], "She isn't going to work on Sunday"),
    ],
    mistakes=[("Escribir «She going to visit».", "Falta el verbo is entre she y going.", "Escribe «She is going to visit»."),
              ("Decir «I'm not going to working».", "Después de going to el verbo va simple.", "Di «I'm not going to work».")],
    T=[
        ("abc", "{F} ¿A quién va a visitar Marta este fin de semana?", "A su mamá", "A su hermana", "A su jefe", "Marta dice «I'm going to visit my mother»."),
        ("ab", "{F} ¿Marta va a trabajar el domingo?", "No, no va a trabajar", "Sí, va a trabajar", "Marta dice «I'm not going to work on Sunday»."),
        ("abc", "{F} ¿Qué quiere aprender Marta el próximo año?", "Computación", "Cocina", "Inglés", "Marta dice «I want to learn computer skills»."),
        ("abc", "{F} ¿Qué le gustaría encontrar a Marta?", "Un trabajo nuevo", "Una casa nueva", "Un auto nuevo", "Marta dice «I would like to find a new job»."),
        ("abc", "{F} ¿Quién hace las preguntas en el diálogo?", "Carlos", "Marta", "Ana", "Carlos hace las preguntas y Marta responde todas."),
        ("{F} ¿Cuántas cosas dice Marta que quiere o le gustaría hacer el próximo año? Escribe el número.", "2", "Marta dice «I want to learn computer skills» y «I would like to find a new job», o sea dos cosas."),
        ("abc", "Completa: I'm ___ going to work on Sunday.", "not", "no", "don't", "Para negar este plan se dice I'm not going to."),
        ("abc", "Elige la oración correcta.", "She is going to visit her mother.", "She going to visit her mother.", "She is going to visits her mother.", "Con she va is, y el verbo queda simple."),
        ("Ordena las palabras: rest / I'm / to / going.", "I'm going to rest.", "La estructura es I'm going to y el verbo simple."),
        ("ab", "Verdadero o falso: Marta va a trabajar el domingo según {F}", "Falso: dijo que no va a trabajar", "Verdadero: va a trabajar", "El guion dice I'm not going to work on Sunday."),
        ("ab", "Dos frases: «I'm going to visit my mother» y «I would like to visit my mother». ¿Cuál es un plan firme?", "La primera, con I'm going to", "La segunda, con would like to", "I'm going to expresa un plan decidido; would like es un deseo."),
        ("abc", "{F} ¿Qué oración resume lo que Marta quiere hacer en el futuro?", "She wants to learn computer skills and find a new job.", "She wants to sell computers.", "She wants to stop working.", "En el guion dice que quiere aprender computación y encontrar un trabajo."),
        ("abc", "¿Cuál oración tiene un error?", "He going to visit his mother.", "He is going to visit his mother.", "He isn't going to work.", "En la primera falta is entre he y going."),
    ],
    ctx=("abc", "Un amigo te pregunta por mensaje si vas a trabajar el sábado. Tú no vas a trabajar. ¿Qué respondes en inglés?", "No, I'm not going to work.", "No, I don't going to work.", "No, I'm going not to work.", "La negación de este plan es I'm not going to y el verbo."),
    sc=[("En Inglés: ¿cómo dices «no voy a trabajar»?", "I'm not going to work", "La negación es I'm not going to y el verbo simple."),
        ("En Inglés: ¿cómo preguntas «¿Qué vas a hacer?»?", "What are you going to do?", "What are you going to más el verbo do forman la pregunta."),
        ("En Inglés: ¿qué significa «this weekend»?", "este fin de semana", "This weekend es el próximo sábado y domingo.")],
    op=("Pide a otra persona que lea en voz alta {F} Luego escribe tres oraciones de lo que cuenta Marta (una con visit, una con work, una con learn) y una oración tuya inventada.",
        "Marta is going to visit her mother. She isn't going to work on Sunday. She wants to learn computer skills. I want to cook rice.",
        ["tres oraciones sobre Marta", "una propia", "usa is con she"],
        ["cuatro oraciones escritas"],
        ["olvidar is con she", "agregar -ing al verbo"],
        "Pregunta: «¿Qué plan de Marta te gustó más?»"),
    reinforce="Vuelve a leer el guion en voz alta y subraya cada expresión de proyecto.",
    extend="Inventa un diálogo de cuatro líneas sobre los planes del fin de semana de dos personas.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico los proyectos personales a una situación de la comunidad: un mensaje para organizar un pequeño negocio.",
    prior=["Uso I want to, I'm going to e I'm not going to.", "Pregunto con Would you like to…?", "Leo un mensaje corto."],
    explain=[
        "Los proyectos personales también sirven en el barrio y en el trabajo: vender pan, organizar un taller, buscar ayuda. En inglés un mensaje breve y claro tiene un saludo, el proyecto y una petición educada.",
        "Un mensaje de ejemplo se organiza así: «Hello, my name is…», luego «I want to…», después los pasos con «I'm going to…» y al final «Would you like to help me?». La palabra please suaviza la petición: «Please call me».",
        "Al leer un mensaje de otra persona, subraya el proyecto, los pasos y la petición. Después contesta con una oración completa, por ejemplo «Yes, I would» o «Sorry, I can't». Can't es la forma corta de «no puedo»; úsala como una expresión completa.",
    ],
    vocab=[("sell", "vender"), ("bake", "hornear"), ("flour", "harina"), ("neighborhood", "barrio"), ("help", "ayudar"), ("please", "por favor"), ("Sorry, I can't", "Perdón, no puedo")],
    worked=[
        ("Encontrar los pasos de un plan", "Mensaje de ejemplo: «I'm going to buy flour on Monday and I'm going to bake on Tuesday.»", ["Subrayo I'm going to y su verbo.", "Paso 1: buy flour on Monday.", "Paso 2: bake on Tuesday."], "Compra harina el lunes y hornea el martes"),
        ("Contestar una invitación", "Pregunta de ejemplo: «Would you like to help me?» (sí).", ["La pregunta usa would you like to.", "Respondo con would.", "Respuesta corta afirmativa."], "Yes, I would"),
    ],
    mistakes=[("Escribir «I'm going to sell in Sunday».", "Para los días se usa on, no in.", "Escribe «on Sunday»."),
              ("Contestar «Yes, I am» a «Would you like to help me?».", "Se mezcla con la pregunta de going to.", "A would you like se responde con would: «Yes, I would».")],
    T=[
        ("abc", "{F} ¿Qué quiere vender Rosa?", "Pan", "Verduras", "Ropa", "Rosa dice «I want to sell bread in the neighborhood»."),
        ("ab", "{F} ¿Qué va a hacer Rosa el lunes?", "Va a comprar harina", "Va a hornear pan", "Rosa dice «I'm going to buy flour on Monday»."),
        ("abc", "{F} ¿Qué va a hacer Rosa el martes?", "Hornear", "Vender", "Descansar", "El texto dice que el martes va a hornear (bake)."),
        ("abc", "{F} ¿Qué día no va a vender Rosa?", "El domingo", "El lunes", "El martes", "El texto dice «I'm not going to sell on Sunday»."),
        ("abc", "{F} ¿Qué le pide Rosa a las personas del grupo?", "Que la ayuden", "Que le compren pan", "Que le presten dinero", "Rosa pregunta «Would you like to help me?», o sea si la quieren ayudar."),
        ("{F} ¿Qué debe hacer una persona que quiere ayudar? Responde con el verbo en inglés que usa Rosa.", "call", "El texto dice «Please call me»."),
        ("abc", "Completa: I'm going to bake ___ Tuesday.", "on", "in", "at", "Para los días de la semana se usa on."),
        ("abc", "Elige la respuesta educada a una invitación que no puedes aceptar.", "Sorry, I can't.", "No, never.", "I'm not going.", "Sorry, I can't es una forma amable de decir que no puedes."),
        ("Ordena las palabras: want / I / bread / sell / to.", "I want to sell bread.", "La estructura es I want to y el verbo simple sell."),
        ("ab", "Verdadero o falso: Rosa va a vender pan el domingo.", "Falso: dice que no va a vender el domingo", "Verdadero: dice que sí", "El texto dice I'm not going to sell on Sunday."),
        ("ab", "Una persona escribe «Please help me» y otra «Help me». ¿Cuál es más cortés?", "Please help me", "Help me", "La palabra please suaviza la petición y la hace más amable."),
        ("abc", "{F} ¿Qué oración es verdadera?", "Rosa is going to bake on Tuesday.", "Rosa is going to bake on Sunday.", "Rosa isn't going to buy flour.", "El martes va a hornear según el mensaje."),
        ("abc", "¿Cuál oración tiene un error?", "I'm going to sell in Sunday.", "I'm going to sell on Sunday.", "I want to sell bread.", "Con los días de la semana se usa on, no in."),
    ],
    ctx=("abc", "En la junta de vecinos de ejemplo te invitan a ayudar a organizar una feria de libros. Quieres decir que sí con amabilidad. ¿Qué respondes?", "Yes, I would.", "Yes, I am.", "Yes, I do.", "A una pregunta con would you like se responde con would."),
    sc=[("En Inglés: ¿qué significa «please»?", "por favor", "Please se usa para pedir con cortesía."),
        ("En Inglés: ¿cómo se dice «vender»?", "sell", "Sell es el verbo para vender."),
        ("En Inglés: ¿cómo dices que no puedes aceptar una invitación?", "Sorry, I can't", "Es la forma amable y completa de decir no.")],
    op=("Escribe un mensaje corto en inglés, con datos inventados, como el de {F} para organizar un proyecto pequeño en tu barrio. Incluye saludo, proyecto, dos pasos y una invitación.",
        "Hello, my name is Pedro. I want to open a small garden. I'm going to buy seeds on Friday and I'm going to plant on Saturday. Would you like to help me? Please call me.",
        ["tiene saludo", "tiene proyecto y dos pasos", "tiene invitación con please"],
        ["un mensaje de cuatro a seis oraciones"],
        ["olvidar los pasos", "agregar -ing al verbo"],
        "Pregunta: «¿Se entiende qué vas a hacer y qué pides?»"),
    reinforce="Escribe el mensaje otra vez cambiando el proyecto y los días.",
    extend="Lee tu mensaje en voz alta a otra persona y pídele que te diga qué entendió.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado sobre proyectos personales, me autoevalúo y decido qué seguir practicando.",
    prior=["Uso I want to, I'm going to e I would like to.", "Pregunto y respondo sobre planes.", "Leo mensajes y diálogos cortos."],
    explain=[
        "En este desempeño aprendiste a contar tus proyectos con tres expresiones completas, a preguntar con What are you going to…? y Are you going to…?, a negar con I'm not going to y a responder con Yes, I am, No, I'm not o Yes, I would.",
        "También aprendiste vocabulario de proyectos (open, save, learn, buy, find, finish) y palabras de tiempo (this week, next year, tomorrow). Todos los verbos van simples después de las expresiones.",
        "Para decidir qué practicar, revisa tus errores: ¿olvidas to?, ¿agregas -ing?, ¿dices «Yes, I do» en vez de «Yes, I am»? Elige uno y practícalo en voz alta unos minutos cada día. Cuenta tus proyectos a otra persona: hablar de lo que quieres hacer ayuda a cumplirlo.",
    ],
    vocab=[("finish school", "terminar el colegio"), ("office", "oficina"), ("summer", "verano"), ("at night", "de noche"), ("because", "porque"), ("travel", "viajar")],
    worked=[
        ("Revisar una oración", "Oración de ejemplo: «I want study at night».", ["Veo want y el verbo study.", "Falta to después de want.", "Corrijo."], "I want to study at night"),
        ("Contar un plan con razón", "Dato de ejemplo: no vas a viajar porque vas a ahorrar.", ["La negación: I'm not going to travel.", "La razón: because.", "El plan que explica: I want to save money."], "I'm not going to travel, because I want to save money"),
    ],
    mistakes=[("Responder «Yes, I do» a «Are you going to study?».", "Se mezcla do con are.", "Con are la respuesta es «Yes, I am»."),
              ("Decir «I'm going to buying».", "Después de going to el verbo va simple.", "Di «I'm going to buy».")],
    T=[
        ("abc", "{F} ¿Qué quiere terminar Pedro este año?", "El colegio", "El trabajo", "Un curso de cocina", "Pedro dice «I want to finish school this year»."),
        ("ab", "{F} ¿Cuándo va a estudiar Pedro?", "De noche", "En la mañana", "Pedro dice «I'm going to study at night»."),
        ("abc", "{F} ¿Dónde le gustaría trabajar a Pedro?", "En una oficina", "En una tienda", "En un taller", "El texto dice que le gustaría trabajar en una oficina."),
        ("abc", "{F} ¿Por qué Pedro no va a viajar este verano?", "Porque quiere ahorrar dinero", "Porque no tiene tiempo", "Porque está enfermo", "El texto dice «because I want to save money»."),
        ("abc", "{F} ¿Qué expresión usa Pedro para decir que no va a viajar?", "I'm not going to", "I don't want to", "I would like to", "El texto dice I'm not going to travel."),
        ("{F} ¿Qué estación del año nombra Pedro? Escribe la palabra en inglés.", "summer", "Pedro dice «this summer», o sea este verano."),
        ("abc", "Completa: I want ___ finish school.", "to", "of", "for", "Después de want va to antes del verbo."),
        ("abc", "Elige la oración correcta.", "I would like to work in an office.", "I would like work in an office.", "I would like to working in an office.", "Would like to lleva el verbo simple."),
        ("Ordena las palabras: study / going / I'm / to / at night.", "I'm going to study at night.", "La estructura es I'm going to y el verbo simple."),
        ("ab", "Una persona dice «Yes, I am» y otra «Yes, I do». ¿Quién responde bien a «Are you going to work?»?", "La que dice Yes, I am", "La que dice Yes, I do", "Con are se responde con am."),
        ("ab", "Verdadero o falso razonado: «I want to saving money» está bien escrita.", "Falso: el verbo va simple, save", "Verdadero: así se escribe", "Después de want to el verbo no lleva -ing."),
        ("abc", "{F} ¿Cuál afirmación es falsa?", "Pedro is going to travel this summer.", "Pedro wants to finish school.", "Pedro is going to study at night.", "El texto dice que no va a viajar este verano."),
        ("abc", "¿Cuál oración tiene dos errores?", "I going to buying a bike.", "I'm going to buy a bike.", "I want to buy a bike.", "Falta I'm y buying debe ser buy."),
    ],
    ctx=("abc", "En un taller de orientación de ejemplo te piden que escribas un proyecto con una razón. Imagina que vas a estudiar de noche porque trabajas de día. ¿Cuál es mejor?", "I'm going to study at night, because I work during the day.", "I'm going to studying at night, because I work.", "I going study at night.", "La oración usa I'm going to, verbo simple y because para la razón."),
    sc=[("En Inglés: ¿cómo cuentas un plan firme?", "I'm going to + verbo simple", "I'm going to más verbo simple expresa un plan decidido."),
        ("En Inglés: ¿cómo dices que te gustaría algo?", "I would like to + verbo simple", "Would like to es la forma amable del deseo."),
        ("En Inglés: ¿cómo preguntas «¿Qué vas a comprar?»?", "What are you going to buy?", "What, are you y going to forman la pregunta.")],
    op=("Autoevaluación oral o escrita. Con {F} como modelo, cuenta tres proyectos tuyos o inventados (uno con cada expresión) y escribe una frase sobre qué vas a practicar después.",
        "I want to learn computer skills. I'm going to save money. I would like to open a shop. Next, I'm going to practice questions with What.",
        ["usa las tres expresiones", "cada una con verbo simple", "dice qué practicar"],
        ["tres oraciones y una frase de siguiente paso"],
        ["olvidar to después de want", "no decir qué practicar"],
        "Pregunta: «¿Cuál de tus tres proyectos te entusiasma más?»"),
    reinforce="Elige el error que más repites y escribe tres oraciones correctas sobre él.",
    extend="Cuenta tus proyectos en inglés a una persona cercana y pregúntale qué quiere hacer ella, con What are you going to…?",
)
