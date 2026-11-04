"""Cuaderno del estudiante, 1.º medio Inglés (propuesta), EN1M OA 07 (respuesta personal y crítica a textos leídos o escuchados).

Los textos son originales y están escritos en el enunciado, con pista en español. Los datos numéricos son «de ejemplo».
"""
from __future__ import annotations

from student_content_en_m1_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA7 = "EN1M OA 07"
MATR = "Los textos escritos en cada ejercicio; lápiz y hoja para escribir tus reacciones."

# ================================================================ OA 07 · clase 1: hacer conexiones
KITE = "«Flying kites is a tradition in many countries. In Chile, kites are called volantines, and many families fly them in September. A kite flies because the wind lifts it up and the string keeps it in place.» (kite = volantín, tradition = tradición, wind = viento, lifts = levanta, string = hilo, keeps = mantiene)"

lesson(
    OA7, 1, MATR,
    "Aprenderé a reaccionar a un texto haciendo conexiones con otras asignaturas, con mi cultura, con mi vida y con otras culturas, usando I used to… y I have been/seen/learned/read…. Sirve para mostrar que entendí y para relacionar lo leído con lo que ya sé.",
    ["Sé el pasado simple y el participio de verbos comunes.", "Sé leer un texto breve en inglés."],
    [
        "Reaccionar a un texto es más que repetirlo: es relacionarlo con lo que sabes. Una conexión (connection) puede ser con otra asignatura (el viento que empuja un volantín se relaciona con Ciencias: el viento es aire en movimiento y puede empujar objetos), con tu cultura (en Chile, muchas familias vuelan volantines en septiembre), con la vida cotidiana (mirar el viento antes de secar la ropa), con experiencias personales o con otras culturas (festivales de volantines en otros países).",
        "Para expresar esas conexiones se usan estructuras frecuentes. I used to + verbo cuenta un hábito pasado: I used to fly kites with my cousins. I have + participio cuenta una experiencia hasta ahora: I have seen kites on the beach; I have learned that wind is moving air; I have read about kite festivals. Los participios de algunos verbos son irregulares: see → seen, fly → flown, read → read (se escribe igual).",
        "Una buena conexión es específica y se relaciona con una idea del texto. «I like kites» es una opinión, no una conexión. «I have learned in Science that wind is moving air, so it can push a kite» conecta el texto con lo que aprendiste y explica por qué.",
    ],
    [("connection", "conexión: relación entre el texto y lo que sé"), ("I used to…", "yo solía…; hábito pasado"), ("I have seen / learned / read", "he visto / aprendido / leído"), ("tradition", "tradición"), ("experience", "experiencia"), ("another culture", "otra cultura")],
    [
        ("Conexión personal", KITE + " Escribe una conexión personal con I used to.", ["Pienso en un hábito pasado relacionado con volantines.", "Uso I used to + verbo.", "Escribo: I used to fly kites with my cousins."], "I used to fly kites with my cousins (solía volar volantines con mis primos)"),
        ("Conexión con Ciencias", KITE + " ¿Qué idea de Ciencias conecta con el texto?", ["El texto dice que el viento empuja el volantín.", "En Ciencias, el viento es aire en movimiento y puede empujar objetos.", "Esa idea explica por qué vuela."], "Que el viento es aire en movimiento y puede empujar un objeto"),
    ],
    [
        ("Decir solo «Me gusta» y creer que es una conexión.", "No se relaciona con ninguna idea del texto.", "Explica con una idea del texto o de lo que sabes."),
        ("Usar I have flew en vez de I have flown.", "Se usa el pasado en vez del participio.", "Con have usa el participio: flown, seen, learned."),
    ],
    [
        (KITE + " ¿Cómo se llaman los kites en Chile?", "Volantines", "El texto dice kites are called volantines."),
        (KITE + " ¿En qué mes muchas familias vuelan volantines en Chile?", "Septiembre", "El texto dice in September."),
        (KITE + " ¿Qué empuja al volantín hacia arriba? A) el viento B) el hilo", "A) el viento", "El texto dice the wind lifts it up."),
    ],
    [
        ("Elige la oración que conecta el texto con Ciencias. A) Moving air can push objects, like a kite. B) Kites are sold in many shops.", "A) Moving air can push objects, like a kite.", "Relaciona el texto con una idea científica."),
        ("Elige la oración que conecta con una experiencia personal. A) I used to build paper kites with my sister. B) Kites are made of paper.", "A) I used to build paper kites with my sister.", "Cuenta algo vivido por quien habla."),
        ("Elige la oración que conecta con la cultura de Chile. A) In Chile, flying kites is a family tradition in September. B) Kites have a string.", "A) In Chile, flying kites is a family tradition in September.", "Habla de una tradición del país."),
    ],
    [
        ("Completa: «I ____ to fly kites when I was little, but now I play football.» A) used B) use", "A) used", "Used to + verbo expresa un hábito pasado."),
        ("Completa: «I have ____ about the wind in Science class.» A) learned B) learn", "A) learned", "Have + participio forma el presente perfecto."),
        ("Une cada oración con su conexión. 1) I used to fly kites with my uncle. 2) In other countries, people fly kites at festivals. 3) I have learned that wind is moving air. Conexiones: a) otras culturas b) experiencia personal c) Ciencias", "1-b, 2-a, 3-c", "Cada oración se relaciona con un ámbito distinto."),
    ],
    [
        ("Un compañero escribe «I have flew a kite». ¿Cuál es la forma correcta? A) I have flown a kite. B) I have flew a kite.", "A) I have flown a kite.", "El participio de fly es flown."),
        ("Elige la conexión con la vida cotidiana. A) I check the wind before I hang the laundry. B) Kites are colorful.", "A) I check the wind before I hang the laundry.", "Relaciona el viento con una tarea de la casa."),
    ],
    [
        ("Rosa dice: «I used to fly kites every September, but now I study on holidays». ¿Sigue volando volantines? A) no, used to marca un hábito pasado B) sí, todos los años", "A) no, used to marca un hábito pasado", "But now indica que cambió."),
        (KITE + " ¿Cuál conexión NO se relaciona con el texto? A) I like pizza. B) I have seen kites on the beach.", "A) I like pizza.", "No tiene relación con los volantines."),
    ],
    [("Un diario dice: «I have seen kites on the beach. In Science, I have learned that wind pushes objects.» (beach = playa, objects = objetos). ¿Cuántas conexiones distintas hay? A) dos B) tres", "A) dos", "Una es experiencia personal y otra es Ciencias.")],
    [
        ("¿Qué es una conexión con el texto?", "Una relación entre lo leído y lo que sé", "Explica por qué el texto me importa."),
        ("¿Qué expresa I used to…?", "Un hábito del pasado", "Lo que antes ocurría y ya no."),
        ("¿Cuál es el participio de see?", "Seen", "I have seen."),
    ],
    task("Lee este texto original: «In Chile, many families have a snack called once in the afternoon. It is usually tea or coffee with bread. In other countries, people have afternoon tea or a coffee break.» (snack = merienda, bread = pan, afternoon tea = té de la tarde, coffee break = pausa del café). En tu hoja escribe tres conexiones, una personal con I used to o I have, una con tu cultura y una con otra cultura.", "Personal: I used to have once with my grandmother. Cultura: In Chile, once is a family meal in the afternoon. Otra cultura: In England, people have afternoon tea.", ["escribe tres conexiones distintas", "usa I used to o I have + participio correctamente", "cada conexión se relaciona con el texto"], ["hoja con tres oraciones", "nota del adulto"], ["decir solo «me gusta»", "usar la forma verbal incorrecta"], "Valora las conexiones específicas y corrige solo el participio si es necesario."),
    "Vuelve a leer el texto de los volantines y escribe dos conexiones nuevas, una con Ciencias y otra con tu vida.",
    "Escribe en español dos hábitos que tenías de niño o niña y cómo los dirías con I used to.",
)

# ---------------------------------------------------------------- clase 2: explicar relaciones entre ideas
UNI = "«Longer breaks: yes or no? First, many students say that a longer break helps them relax and talk with friends. Then, teachers say that a longer break leaves less time for classes. For example, ten extra minutes every day add up to fifty minutes a week (example data). Although classes would be shorter, a longer break could help students pay attention. If the school gave fifteen more minutes, more students would feel calm. Finally, the class decided to ask the principal for a trial month.» (break = recreo, relax = relajarse, less time = menos tiempo, add up = sumar, pay attention = poner atención, calm = tranquilos, trial = de prueba, principal = director)"

lesson(
    OA7, 2, MATR,
    "Aprenderé a explicar la relación entre ideas con although, first… then… finally, if, for example y but. Sirve para argumentar y organizar lo que pienso al reaccionar a un texto.",
    ["Sé conectores simples como and y because.", "Sé la estructura de if + pasado, would."],
    [
        "Los conectores explican cómo se relacionan las ideas. First, then y finally ordenan una secuencia: primero una razón, después otra, al final una conclusión. For example introduce un ejemplo que concreta una idea general. But y although marcan contraste: Although classes would be shorter, a longer break could help students pay attention se lee «aunque las clases serían más cortas, un recreo largo podría ayudar a poner atención».",
        "If introduce una condición. En «If the school gave fifteen more minutes, more students would feel calm», la condición (dar quince minutos más) lleva a una consecuencia (más estudiantes tranquilos). La condición es imaginaria; se escribe if + pasado y would + verbo. No necesitas traducir cada palabra: identifica la función del conector y úsalo en tu reacción: «First, I think...; then...; finally...».",
        "Al reaccionar a un texto, explica tus ideas con esta guía: una idea principal, un ejemplo con for example, un contraste con although o but, una condición con if y una conclusión con finally. Así tu respuesta se entiende y se parece a un texto bien organizado.",
    ],
    [("first / then / finally", "primero / luego / por último"), ("for example", "por ejemplo"), ("although", "aunque"), ("but", "pero"), ("if", "si (condición)"), ("conclusion", "conclusión")],
    [
        ("Conector de contraste", UNI + " ¿Qué conector muestra el contraste entre tener clases más cortas y ayudar a poner atención?", ["Busco la idea que se opone.", "Dice Although classes would be shorter, a longer break could help students pay attention.", "El conector es although."], "Although"),
        ("Condición", UNI + " ¿Qué pasaría si el colegio diera quince minutos más?", ["Busco la estructura con if.", "Dice If the school gave fifteen more minutes, more students would feel calm.", "La consecuencia es que más estudiantes se sentirían tranquilos."], "Más estudiantes se sentirían tranquilos"),
    ],
    [
        ("Poner for example sin dar un ejemplo concreto.", "Se usa el conector solo por rellenar.", "Después de for example escribe un caso específico con un dato."),
        ("Usar but y although en la misma oración corta.", "Se duplica el contraste.", "Usa solo uno por oración."),
    ],
    [
        (UNI + " ¿Qué palabra abre la secuencia? A) First B) Finally", "A) First", "First introduce la primera razón."),
        (UNI + " ¿Qué ejemplo da el texto sobre el tiempo extra?", "Diez minutos más cada día suman cincuenta minutos a la semana", "Dice ten extra minutes every day add up to fifty minutes a week."),
        (UNI + " ¿Qué decidió la clase al final? A) pedir un mes de prueba al director B) hacer una encuesta a los profesores", "A) pedir un mes de prueba al director", "Dice Finally, the class decided to ask the principal for a trial month."),
    ],
    [
        (UNI + " ¿Qué ventaja del recreo largo se nombra primero? A) ayuda a relajarse y hablar con amigos B) mejora las notas de inmediato", "A) ayuda a relajarse y hablar con amigos", "Dice First, a longer break helps them relax and talk with friends."),
        (UNI + " ¿Qué relación marca For example? A) un ejemplo de que quita tiempo de clases B) un contraste", "A) un ejemplo de que quita tiempo de clases", "Concreta la idea con un caso."),
        ("Une cada conector con su función. 1) although 2) for example 3) finally Funciones: a) conclusión b) contraste c) ejemplo", "1-b, 2-c, 3-a", "Cada conector organiza ideas de un modo distinto."),
    ],
    [
        ("Completa: «____ I am tired, I will finish my homework.» A) Although B) For example", "A) Although", "Hay un contraste entre cansarse y terminar la tarea."),
        ("Completa: «If I ____ more time, I would read every night.» A) had B) have", "A) had", "Con if + pasado se forma la condición imaginaria."),
        ("Ordena una reacción con letras. A) Finally, I think a longer break is a good idea. B) First, a longer break helps students relax. C) Then, it leaves less time for classes. D) For example, ten extra minutes a day are fifty minutes a week.", "B, C, D, A", "La secuencia va de la razón al ejemplo y a la conclusión."),
    ],
    [
        ("Un estudiante escribe: «Longer breaks leave less time for classes. For example, they help students relax.» ¿Qué conector conviene en lugar de For example? A) But, porque la segunda idea se opone a la primera B) Then, porque ordena una secuencia", "A) But, porque la segunda idea se opone a la primera", "Ayudar a relajarse no es un ejemplo de que quite tiempo de clases: es un contraste."),
        (UNI + " ¿Cuál es la condición en «If the school gave fifteen more minutes…»? A) que el colegio diera quince minutos más B) que más estudiantes se sientan tranquilos", "A) que el colegio diera quince minutos más", "La parte con if es la condición."),
    ],
    [
        (UNI + " Un lector dice que la clase decidió alargar el recreo para siempre. ¿Qué conector del final lo corrige? A) Finally B) Then", "A) Finally", "Finally introduce la decisión: pedir un mes de prueba."),
        (UNI + " ¿Qué función cumple Although en «Although classes would be shorter, a longer break could help students pay attention»? A) mostrar que, aunque hay menos clase, el recreo tiene una ventaja B) repetir que las clases serían más cortas", "A) mostrar que, aunque hay menos clase, el recreo tiene una ventaja", "Introduce un contraste, no una repetición."),
    ],
    [("Lee: «First, I wake up at seven. Then, I have breakfast. Finally, I walk to school.» (breakfast = desayuno). ¿Qué conector marca la última acción?", "Finally", "Indica el último paso de la rutina.")],
    [
        ("¿Qué indica for example?", "Que viene un ejemplo", "Concreta una idea."),
        ("¿Qué indica although?", "Un contraste", "Une dos ideas que se oponen."),
        ("¿Qué estructura usa if para algo imaginario?", "If + pasado, would + verbo", "Condición y consecuencia."),
    ],
    task("Lee este texto original: «Should school start later? First, some students say that they are sleepy at eight. Then, teachers say that a later start would end the day later. For example, classes might finish at five. Although it has disadvantages, a later start could help. If the school started at nine, students would be more awake.» (sleepy = con sueño, later start = comienzo más tarde, disadvantages = desventajas, awake = despierto). En tu hoja escribe tu reacción de cuatro oraciones usando First, For example, Although y If.", "First, I think a later start is good. For example, I would sleep more. Although classes would end later, I would be more awake. If the school started at nine, I would study better.", ["usa los cuatro conectores pedidos", "cada oración se entiende y se relaciona con el texto", "usa if + pasado y would correctamente"], ["hoja con cuatro oraciones", "nota del adulto"], ["usar for example sin ejemplo", "olvidar would en la condición"], "Valora los conectores usados y revisa la condición con if."),
    "Vuelve a leer el texto del recreo largo y encierra todos los conectores con un color.",
    "Escribe en español tres razones para un tema de tu curso y ordénalas con primero, luego y por último.",
)

# ---------------------------------------------------------------- clase 3: opiniones, interpretaciones y puntos de vista
PHONE3 = "«Phones in class: In my opinion, phones are useful if the teacher uses them for a clear task. According to the school survey (example data), 18 of 30 students use their phones to look up words. However, five students say that phones distract them. I think a good rule is to use phones only when the teacher says so.» (phones = celulares, useful = útiles, clear task = tarea clara, survey = encuesta, look up = buscar, distract = distraen, rule = regla)"

lesson(
    OA7, 3, MATR,
    "Aprenderé a expresar sentimientos, interpretaciones y puntos de vista con In my opinion…, I think…, I agree/disagree y according to…. Sirve para opinar con respeto y apoyarme en información.",
    ["Sé distinguir un hecho de una opinión.", "Sé leer datos de ejemplo."],
    [
        "Un hecho (fact) se puede comprobar: «18 of 30 students use their phones to look up words». Una opinión (opinion) es lo que alguien piensa: «phones are useful». Para marcar una opinión se usan frases como In my opinion…, I think…, I believe… (creo que…), I agree with… o I disagree with… (estoy de acuerdo o en desacuerdo con…).",
        "According to… (según…) sirve para indicar la fuente de un dato: According to the survey, 18 of 30 students… Así dejas claro de dónde viene la información y no se confunde con tu opinión. Un buen argumento combina ambas cosas: «According to the survey, 18 of 30 use phones to look up words. In my opinion, that is useful».",
        "También se pueden expresar sentimientos: I feel worried, I am surprised, I am happy. Una interpretación (interpretation) es tu explicación de lo que el texto quiere decir: «I think the text wants us to use phones with rules». Defiende siempre tu punto de vista con una razón.",
    ],
    [("in my opinion", "en mi opinión"), ("I think / I believe", "creo que"), ("I agree / I disagree", "estoy de acuerdo / en desacuerdo"), ("according to", "según"), ("fact", "hecho: se puede comprobar"), ("interpretation", "interpretación: lo que creo que el texto quiere decir")],
    [
        ("Hecho u opinión", PHONE3 + " ¿«18 of 30 students use their phones to look up words» es un hecho o una opinión?", ["Pregunto si se puede comprobar.", "Se puede contar con una encuesta.", "Es un hecho (con datos de ejemplo)."], "Es un hecho, porque es un dato que se puede comprobar"),
        ("Fuente de un dato", PHONE3 + " ¿Qué frase dice de dónde viene el dato de los 18 estudiantes?", ["Busco la palabra según.", "Dice According to the school survey.", "La fuente es la encuesta del colegio."], "According to the school survey"),
    ],
    [
        ("Presentar una opinión como si fuera un hecho.", "No se marca con una frase como in my opinion.", "Antes de una opinión escribe I think o in my opinion."),
        ("Dar un dato sin decir de dónde viene.", "Se olvida la fuente.", "Usa according to… para citar la fuente."),
    ],
    [
        (PHONE3 + " ¿Cuántos estudiantes de 30 usan el celular para buscar palabras?", "18", "El texto dice 18 of 30 students."),
        (PHONE3 + " ¿Qué frase marca la opinión de quien escribe? A) In my opinion B) According to", "A) In my opinion", "Marca un punto de vista personal."),
        (PHONE3 + " ¿Cuál es la regla que propone? A) usar celulares solo cuando el profesor lo indique B) prohibir los celulares", "A) usar celulares solo cuando el profesor lo indique", "Lo dice la última oración."),
    ],
    [
        (PHONE3 + " ¿Cuál oración es un hecho? A) 18 of 30 students use their phones. B) Phones are useful.", "A) 18 of 30 students use their phones.", "Se puede comprobar contando."),
        (PHONE3 + " ¿Qué opinan cinco estudiantes? A) que los celulares los distraen B) que son muy útiles", "A) que los celulares los distraen", "Dice five students say that phones distract them."),
        ("Une cada frase con su función. 1) I disagree with the rule. 2) According to the survey… 3) I think it is useful. Funciones: a) dar una opinión b) citar una fuente c) mostrar desacuerdo", "1-c, 2-b, 3-a", "Cada frase hace algo distinto en un argumento."),
    ],
    [
        arith(PHONE3 + " ¿Cuántos estudiantes de los 30 NO usan el celular para buscar palabras?", "30-18", "Se restan de 30 los 18 que sí lo usan."),
        ("Completa: «____ the survey, most students use phones.» A) According to B) In my opinion", "A) According to", "Se cita la fuente de un dato."),
        ("Quieres decir tu punto de vista personal, sin citar ninguna fuente. ¿Qué frase usas al comenzar? A) In my opinion B) According to", "A) In my opinion", "In my opinion marca un punto de vista propio; according to cita una fuente."),
    ],
    [
        ("Un compañero dice «Phones are bad». ¿Cómo se puede expresar como opinión? A) I think phones are bad B) Phones are bad", "A) I think phones are bad", "La frase I think marca que es su punto de vista."),
        (PHONE3 + " ¿Qué opinión apoya el dato 18 of 30? A) que los celulares son útiles para buscar palabras B) que los celulares distraen a todos", "A) que los celulares son útiles para buscar palabras", "El dato se relaciona con el uso para buscar palabras."),
    ],
    [
        (PHONE3 + " Un lector dice que el texto prohíbe los celulares. ¿Qué frase lo corrige? A) use phones only when the teacher says so B) five students say that phones distract them", "A) use phones only when the teacher says so", "El texto no los prohíbe: propone usarlos con una regla."),
        (PHONE3 + " ¿Con qué conector introduce el texto una crítica? A) However B) According to", "A) However", "However marca un contraste con la opinión anterior."),
    ],
    [("Lee: «I feel worried because the exam is tomorrow. I am happy because I studied.» (exam = prueba, studied = estudié). ¿Qué dos sentimientos expresa quien escribe? A) preocupación y alegría B) tristeza y sorpresa", "A) preocupación y alegría", "Worried es preocupado y happy es contento.")],
    [
        ("En Inglés: ¿Qué diferencia hay entre hecho y opinión?", "El hecho se puede comprobar; la opinión es lo que alguien piensa", "Se escriben con frases distintas."),
        ("¿Para qué sirve according to?", "Para decir la fuente de un dato", "Evita confundirlo con una opinión."),
        ("¿Cómo se dice «estoy en desacuerdo»?", "I disagree", "Es la forma contraria de I agree."),
    ],
    task("Lee este texto original: «Homework on weekends: According to a class vote (example data), 12 of 20 students think there should be no weekend homework. The teacher says that homework helps students remember. However, many students are tired on Monday.» (homework = tarea, vote = votación, remember = recordar, tired = cansados). En tu hoja escribe tres oraciones: un hecho con according to, tu opinión con In my opinion y un desacuerdo o acuerdo con I agree o I disagree.", "According to the vote, 12 of 20 students want no weekend homework. In my opinion, a little homework is fine. I agree with the teacher that homework helps students remember.", ["usa according to con un dato correcto", "marca su opinión con una frase adecuada", "expresa acuerdo o desacuerdo con una razón"], ["hoja con tres oraciones", "nota del adulto"], ["presentar una opinión como hecho", "inventar un dato"], "Reconoce la diferencia entre hecho y opinión y revisa las frases usadas."),
    "Vuelve a leer el texto de los celulares y subraya con un color los hechos y con otro las opiniones.",
    "Escribe en español tu opinión sobre las tareas del fin de semana y una razón.",
)

# ---------------------------------------------------------------- clase 4: resumir y sintetizar
RADIOA = "Fuente A: «A school radio gives students a voice. Students practice speaking and learn to use equipment. They also share news with the school.» (school radio = radio escolar, voice = voz, practice = practicar, equipment = equipos, share = compartir, news = noticias)"
RADIOB = "Fuente B: «A school radio needs a microphone, a quiet room and volunteers. Without a weekly plan, the programs stop. Some schools also need permission from the principal to use the room.» (microphone = micrófono, quiet = tranquila, volunteers = voluntarios, weekly = semanal, stop = se detienen, permission = permiso, principal = director)"

lesson(
    OA7, 4, "Dos fuentes escritas en cada ejercicio (fuente A y fuente B); lápiz y hoja para escribir resúmenes y síntesis.",
    "Aprenderé a resumir y a sintetizar información: reducir un texto a lo esencial y unir las ideas de dos fuentes en una sola idea. Sirve para preparar un informe, una exposición o un trabajo con varios textos.",
    ["Sé encontrar la idea principal.", "Sé conectores como and, but y however."],
    [
        "Resumir (to summarize) es decir con pocas palabras las ideas principales de un solo texto. No se incluyen ejemplos ni detalles menores, y no se agregan datos nuevos. Un resumen de la fuente A: «Una radio escolar da voz a los estudiantes, les enseña a hablar y a usar equipos, y comparte noticias con el colegio».",
        "Sintetizar (to synthesize) es unir las ideas de dos o más fuentes en un solo mensaje coherente. No es copiar una fuente y luego la otra: es relacionar. La síntesis de A y B podría ser: «Una radio escolar da voz a los estudiantes y comparte noticias, pero necesita micrófono, una sala tranquila, voluntarios y a veces permiso de la dirección». Se usan conectores como but y however para unir ventajas y condiciones.",
        "Para resumir y sintetizar: 1) subraya las ideas principales de cada fuente, 2) elimina los ejemplos y los detalles, 3) une las ideas con conectores y 4) revisa que no agregaste datos que no estaban. Si un dato aparece en una fuente y se contradice con la otra, indícalo en tu síntesis.",
    ],
    [("summarize", "resumir: reducir un texto a lo esencial"), ("synthesize", "sintetizar: unir ideas de varias fuentes"), ("source", "fuente: de dónde viene la información"), ("main idea", "idea principal"), ("detail", "detalle"), ("volunteer", "voluntario")],
    [
        ("Resumir una fuente", RADIOA + " Resume la fuente en una frase.", ["Subrayo las ideas principales: voz, práctica y noticias.", "Elimino los detalles.", "Uno las ideas en una frase."], "Una radio escolar da voz a los estudiantes, les enseña a hablar y a usar equipos, y comparte noticias con el colegio"),
        ("Sintetizar", RADIOA + " " + RADIOB + " Escribe una frase que una las dos fuentes.", ["La fuente A da ventajas.", "La fuente B da requisitos.", "Los uno con but."], "Una radio escolar da voz a los estudiantes y comparte noticias, pero necesita micrófono, una sala tranquila y voluntarios"),
    ],
    [
        ("Agregar datos que no estaban en las fuentes.", "Se completa con lo que uno cree.", "Revisa cada dato y comprueba que aparece en alguna fuente."),
        ("Copiar una fuente y luego la otra.", "No se relacionan las ideas.", "Usa conectores como but o and para unirlas."),
    ],
    [
        (RADIOA + " ¿Qué da una radio escolar a los estudiantes? A) una voz para hablar con el colegio B) un sueldo por sus programas", "A) una voz para hablar con el colegio", "La fuente A dice gives students a voice."),
        (RADIOB + " ¿Qué necesita una radio escolar? A) micrófono, sala tranquila y voluntarios B) una antena gigante y un estudio profesional", "A) micrófono, sala tranquila y voluntarios", "La fuente B lo dice en la primera oración."),
        (RADIOB + " ¿Qué pasa sin un plan semanal?", "Los programas se detienen", "La fuente B dice the programs stop."),
    ],
    [
        (RADIOA + " ¿Cuál es el mejor resumen? A) Una radio escolar da voz, enseña a hablar y a usar equipos, y comparte noticias B) Una radio escolar es un aparato con un micrófono", "A) Una radio escolar da voz, enseña a hablar y a usar equipos, y comparte noticias", "Reúne las tres ideas principales."),
        (RADIOB + " ¿Qué permiso puede necesitar una radio escolar? A) del director para usar la sala B) de un banco", "A) de la ciudad para usar el terreno", "La fuente B lo dice."),
        (RADIOA + " ¿Qué practican los estudiantes? A) hablar y usar equipos B) cantar en un coro", "A) hablar y usar equipos", "Dice Students practice speaking and learn to use equipment."),
    ],
    [
        (RADIOA + " " + RADIOB + " ¿Qué conector une mejor las ventajas con los requisitos en una síntesis? A) but B) because", "A) but", "But marca el contraste entre lo bueno y lo que se necesita."),
        (RADIOA + " " + RADIOB + " ¿Qué fuente habla de los problemas o requisitos? A) la fuente B B) la fuente A", "A) la fuente B", "La fuente B menciona micrófono, sala, plan semanal y permiso."),
        ("Une cada tarea con su definición. 1) summarize 2) synthesize 3) detail Definiciones: a) unir ideas de varias fuentes b) dato menor que se omite en el resumen c) reducir un texto a lo esencial", "1-c, 2-a, 3-b", "Cada término describe un paso distinto del trabajo con textos."),
    ],
    [
        (RADIOA + " " + RADIOB + " Una síntesis dice: «Las radios escolares son un negocio rentable». ¿Es correcta? A) no, las fuentes no hablan de dinero B) sí, porque los estudiantes hablan", "A) no, las fuentes no hablan de dinero", "Una síntesis no agrega datos que no están en las fuentes."),
        (RADIOA + " " + RADIOB + " ¿Cuál síntesis es mejor? A) Una radio escolar beneficia al colegio, pero necesita micrófono, sala tranquila y voluntarios B) Una radio escolar necesita un micrófono", "A) Una radio escolar beneficia al colegio, pero necesita micrófono, sala tranquila y voluntarios", "Une ideas de ambas fuentes."),
    ],
    [
        (RADIOA + " ¿Cuántas oraciones tiene la fuente A? A) tres B) dos", "A) tres", "Cada oración aporta una idea: la voz; la práctica y los equipos; las noticias."),
        (RADIOA + " " + RADIOB + " Un compañero dice que la fuente B contradice la fuente A. ¿Es correcto? A) no, completa la información con requisitos B) sí, dice lo opuesto", "A) no, completa la información con requisitos", "La fuente B agrega lo que se necesita; no se opone."),
    ],
    [("Lee: «Fuente 1: Bikes are cheap and good for health. Fuente 2: Bikes need safe lanes. Many roads are dangerous.» (cheap = baratas, lanes = ciclovías, roads = calles). ¿Qué conector usarías para sintetizar las dos fuentes en una frase? (but o because)", "But", "Une la ventaja de la fuente 1 con la condición de la fuente 2.")],
    [
        ("¿Qué se hace al resumir?", "Se reducen las ideas principales de un texto", "Se omiten detalles."),
        ("¿Qué se hace al sintetizar?", "Se unen ideas de dos o más fuentes", "Se relacionan con conectores."),
        ("¿Qué no debe haber en una síntesis?", "Datos que no están en las fuentes", "Se debe respetar lo que dicen."),
    ],
    task("Lee estas dos fuentes originales. Fuente A: «Reading every day improves vocabulary. Students who read more write better.» Fuente B: «Reading takes time. Some students do not have books at home. The school library can help.» (improves = mejora, vocabulary = vocabulario, write = escribir, takes time = toma tiempo, library = biblioteca). En tu hoja escribe un resumen de cada fuente (una frase) y una síntesis de las dos (una frase con but).", "Resumen A: leer cada día mejora el vocabulario y la escritura. Resumen B: leer toma tiempo y no todos tienen libros, pero la biblioteca puede ayudar. Síntesis: leer cada día mejora el vocabulario y la escritura, but necesita tiempo y libros, y la biblioteca del colegio puede ayudar.", ["resume cada fuente sin agregar datos", "une las dos fuentes con un conector", "mantiene el sentido de ambas"], ["hoja con dos resúmenes y una síntesis", "nota del adulto"], ["copiar frases completas", "inventar una causa que no está en las fuentes"], "Valora la síntesis lograda y revisa que cada dato venga de alguna fuente."),
    "Vuelve a leer la fuente B de la radio y subraya solo las ideas principales.",
    "Escribe en español dos fuentes sobre un tema de tu curso y una síntesis de una frase.",
)

# ---------------------------------------------------------------- clase 5: preguntas e hipótesis
PHOTO = "«Photo caption: Two people stand in front of an old blue house. A big brown dog sits near the door. One person holds a key and a box of tools. There is a for sale sign on the fence.» (photo caption = pie de foto, stand = están de pie, old = viejo, holds = sostiene, key = llave, tools = herramientas, for sale sign = letrero de venta, fence = reja)"

lesson(
    OA7, 5, MATR,
    "Aprenderé a generar preguntas y suposiciones (hipótesis) sobre un texto o una imagen, usando How long has he…?, Have they…? e I think they are…. Sirve para investigar y para comprobar lo que entiendo.",
    ["Sé el presente perfecto con have y has.", "Sé formar preguntas con How y Have."],
    [
        "Una pregunta nueva sobre un texto muestra interés y comprensión. Para preguntar por una duración se usa How long has he…? o How long have they…?: «How long has he lived in the house?». Para preguntar si algo ocurrió hasta ahora se usa Have they…? o Has she…?: «Have they bought the house?». Se responde con Yes, they have o No, they haven't.",
        "Una hipótesis (hypothesis) es una suposición que se puede comprobar con más información. Se expresa con I think…, Maybe… o They might…: «I think they are the owners», «Maybe they are workers». No es un hecho: depende de las pistas y puede corregirse si aparece un dato nuevo. Cada hipótesis debe apoyarse en una pista (a key, tools, a for sale sign).",
        "Para formular preguntas e hipótesis sobre un texto o una imagen, sigue esta guía: observa las pistas; haz una hipótesis con I think; formula una pregunta para comprobarla; y revisa si el texto responde o si necesitas buscar más información.",
    ],
    [("hypothesis", "hipótesis: suposición que se puede comprobar"), ("How long has he…?", "¿Cuánto tiempo ha…? (él)"), ("Have they…?", "¿Han ellos…?"), ("I think they are…", "Creo que ellos son…"), ("clue", "pista"), ("maybe", "quizás")],
    [
        ("Formular una hipótesis", PHOTO + " Escribe una hipótesis sobre quiénes son las dos personas y una pista.", ["Observo las pistas: una llave, herramientas y el letrero de venta.", "Hago una hipótesis con I think.", "Escribo: I think they are the owners; the sign says the house is for sale."], "I think they are workers or owners: one holds tools and a key"),
        ("Formular una pregunta", PHOTO + " Escribe una pregunta sobre cuánto tiempo la casa está a la venta.", ["Quiero preguntar por una duración.", "Uso How long + has + participio.", "Escribo: How long has the house been for sale?"], "How long has the house been for sale?"),
    ],
    [
        ("Presentar una hipótesis como un hecho seguro.", "No se marca con I think o maybe.", "Usa I think, maybe o might para marcar que es una suposición."),
        ("Preguntar «How long did the house for sale?» sin has.", "Se olvida el auxiliar y el participio.", "Usa How long has/have + participio."),
    ],
    [
        (PHOTO + " ¿De qué color es la casa? A) azul B) roja", "A) azul", "El pie de foto dice an old blue house."),
        (PHOTO + " ¿Qué sostiene una de las personas?", "Una llave y una caja de herramientas", "El texto dice holds a key and a box of tools."),
        (PHOTO + " ¿Qué dice el letrero de la reja? A) que la casa está en venta B) que hay un perro bravo", "A) que la casa está en venta", "Dice a for sale sign on the fence."),
    ],
    [
        (PHOTO + " ¿Cuál es una hipótesis razonable? A) I think they are looking at the house to buy it. B) I know they are the mayor's children.", "A) I think they are looking at the house to buy it.", "Se apoya en el letrero y la llave; la otra no tiene pistas."),
        (PHOTO + " ¿Cuál es una buena pregunta para saber duración? A) How long has the dog lived there? B) What color is the fence?", "A) How long has the dog lived there?", "How long has… pregunta por duración."),
        (PHOTO + " ¿Cuál pregunta se responde con Yes o No? A) Have they bought the house? B) How long have they been there?", "A) Have they bought the house?", "Have they…? es una pregunta de sí o no."),
    ],
    [
        ("Completa: «____ he lived in the house for a long time?» A) Has B) Have", "A) Has", "Con he se usa has en el presente perfecto."),
        ("Completa: «How long ____ they been friends?» A) have B) has", "A) have", "Con they se usa have."),
        ("Une cada pregunta con su tipo de respuesta. 1) How long has she lived here? 2) Have they finished? 3) I think they are neighbors. Tipos: a) una duración b) Yes o No c) una hipótesis", "1-a, 2-b, 3-c", "Cada oración pide o expresa algo distinto."),
    ],
    [
        (PHOTO + " ¿Qué pista apoya la hipótesis de que van a vender la casa? A) el letrero en la reja B) el color del perro", "A) el letrero en la reja", "El letrero dice que la casa está en venta."),
        (PHOTO + " Un compañero escribe «They are the owners» como un hecho. ¿Cómo mejoras la oración? A) I think they are the owners B) They are the owners, sure", "A) I think they are the owners", "Con I think queda claro que es una hipótesis."),
    ],
    [
        ("Lee: «Luis has been learning the guitar for six months. He has played at two school events.» ¿Qué pregunta de duración haces? A) How long has Luis been learning the guitar? B) Has Luis a guitar?", "A) How long has Luis been learning the guitar?", "La primera pregunta pide la duración y se responde con six months."),
        (PHOTO + " Si preguntas «Have they entered the house?» ¿qué tipo de información buscas? A) si ya entraron B) cuántos años tiene la casa", "A) si ya entraron", "Have they…? pregunta si algo ocurrió hasta ahora."),
    ],
    [("Lees: «The park has a new playground. Three children are playing on it. A woman is taking photos.» (playground = juegos infantiles, photos = fotos). Si piensas que la mujer es la madre de uno de los niños, ¿cómo lo dices? A) I think she is the mother of one of the children. B) I know she is the mayor.", "A) I think she is the mother of one of the children.", "Es una hipótesis con I think.")],
    [
        ("En Inglés: ¿Qué es una hipótesis?", "Una suposición que se puede comprobar", "Se apoya en pistas."),
        ("¿Qué pregunta pide una duración?", "How long has/have…?", "Se responde con for o since."),
        ("¿Con qué palabra marcas que algo es una suposición?", "I think o maybe", "Muestran que no es un hecho."),
    ],
    task("Lee este pie de foto original: «Photo caption: A girl sits on a bench with a violin case. Next to her, a boy reads a music book. There is a school bag on the grass.» (violin case = estuche de violín, music book = libro de música, grass = pasto). En tu hoja escribe: una hipótesis con I think, una pregunta de duración con How long has/have y una pregunta de sí o no con Have/Has.", "I think they are music students. How long has the girl been playing the violin? Has the boy finished the music book?", ["escribe una hipótesis con una pista", "formula una pregunta de duración correcta", "formula una pregunta de sí o no correcta"], ["hoja con tres oraciones", "nota del adulto"], ["presentar la hipótesis como hecho", "olvidar el auxiliar has/have"], "Valora las preguntas bien formadas y revisa has/have con la persona."),
    "Vuelve a leer el pie de foto de la casa y escribe dos preguntas más con Has o Have.",
    "Escribe en español dos hipótesis sobre una imagen cualquiera de tu colegio y una pregunta para comprobarlas.",
)
