"""Cuaderno del estudiante, 7.º básico Inglés (oficial), IN07 OA 07 (reaccionar a textos leídos o escuchados en exposiciones
y conversaciones: conexiones, opiniones y sentimientos justificados, resúmenes y preguntas). Los textos son originales
y están escritos en cada enunciado; los casos son ficticios para no pedir datos personales.
"""
from __future__ import annotations

from student_content_in7_a import lesson, task
from student_lessons import arith

OA7 = "IN07 OA 07"
MAT = "Los textos y diálogos escritos en cada ejercicio, lápiz y, para practicar en voz alta, una persona de tu casa que te escuche."

ROBOT = "«At Villa Verde School, a robot helps in the library. It can find books, say the title and give a short summary. Students like the robot because it never gets tired. Some teachers worry that students may stop asking people for help. The librarian says: The robot is a tool, not a replacement.» (robot = robot, tool = herramienta, replacement = reemplazo, worry = preocuparse, never = nunca, tired = cansado)"
BOX = "«On Pine Street, neighbors built a small wooden box and put it near the bus stop. Inside, there are books for children and adults. The rule is simple: take a book, leave a book. Mrs. Lara reads there every Friday, and her grandson Mateo says it is his favorite place in the neighborhood.» (neighbors = vecinos, wooden = de madera, rule = regla, grandson = nieto, neighborhood = barrio)"
FIC = "«Ana's neighborhood has a small garden where children plant flowers. At first, nobody takes care of it, so the flowers die. Then Ana makes a schedule, and every child waters the garden once a week. After a month, the garden is full of color.» (garden = jardín, schedule = calendario, waters = riega, once a week = una vez por semana, full of color = lleno de color)"
DEBATE = "«Class 7B talks about homework. Luis: I think we need less homework because we are tired in the evening. Carla: I do not agree. I think homework helps us practice. Julián: I see both points. Maybe we need less homework on Fridays. Teacher: Why do you think that, Julián? Julián: Because many students have sports on Friday afternoon.» (homework = tarea, tired = cansados, agree = estar de acuerdo, practice = practicar, both = ambos, maybe = quizás)"
VOL = "«A volunteer group cleans a river park every Saturday. Last month, they collected sixty bags of rubbish. They also planted twenty small trees. Many families joined them, and the park looks better now.» (volunteer = voluntario, collected = recogieron, bags = bolsas, rubbish = basura, planted = plantaron, joined = se unieron, looks better = se ve mejor)"

# ------------------------------------------------------------------ clase 1
lesson(
    OA7, 1, MAT,
    "Aprenderé a seleccionar una idea significativa de un texto para comentarla y a conectarla con otra asignatura, con una experiencia o con mi cultura usando I learned/read about... in... Sirve para reaccionar a lo que leo o escucho con ideas propias.",
    ["Sé encontrar la idea general de un texto.", "Conozco learned, read y about."],
    [
        "Cuando reaccionas a un texto, no repites todo: eliges una idea significativa (meaningful idea), es decir, una que te hace pensar, sentir o preguntar. En el texto del robot de la biblioteca, una idea significativa es que algunos profesores temen que los estudiantes dejen de pedir ayuda a las personas. En el de la caja de libros, es que los vecinos comparten libros con una regla simple.",
        "Luego conecta esa idea con otras asignaturas, con tu vida cotidiana o con otra cultura. Para eso usa frases como I learned about robots in Technology class (aprendí sobre robots en Tecnología) o I read about a street library in a newspaper (leí sobre una biblioteca callejera en un diario). El tiempo pasado learned y read muestra que lo aprendiste antes. In indica dónde y when indica cuándo.",
        "Escoge una idea que te permita decir algo más: una opinión, un ejemplo o una pregunta. Evita detalles menores, como el material de la caja. Un buen comienzo es: The most interesting idea is... because... Con esa frase ya tienes un tema, una razón y un camino para seguir conversando.",
    ],
    [("meaningful idea", "idea significativa: una que me hace pensar"), ("I learned about...", "aprendí sobre..."), ("I read about...", "leí sobre..."), ("in / when", "en / cuando"), ("tool", "herramienta"), ("neighborhood", "barrio")],
    [
        ("Elegir una idea significativa", BOX + " ¿Qué idea es más significativa para comentar: que los vecinos comparten libros o que la caja es de madera?", ["Pienso qué idea me hace pensar.", "Compartir libros me lleva a hablar de comunidad.", "La madera es un detalle."], "Que los vecinos comparten libros"),
        ("Conectar con una asignatura", "Completa: «I learned about robots ___ Technology class.» (in / on)", ["Hablo de una clase.", "Para decir dónde lo aprendí uso in.", "I learned about robots in Technology class."], "in"),
    ],
    [
        ("Comentar un detalle sin importancia.", "No lleva a una opinión ni a una conversación.", "Elige una idea que te haga pensar."),
        ("Usar el presente para algo que ya aprendiste.", "Se mezcla learn con learned.", "Usa learned o read para hablar del pasado."),
    ],
    [
        (ROBOT + " ¿Cuál es la idea principal? a) un robot ayuda en la biblioteca de una escuela b) un robot cocina", "a) un robot ayuda en la biblioteca de una escuela", "El texto describe un robot en la biblioteca."),
        (BOX + " ¿Cuál es la regla de la caja?", "Take a book, leave a book", "Dice The rule is simple."),
        (ROBOT + " ¿Por qué les gusta el robot a los estudiantes?", "Porque nunca se cansa", "Dice because it never gets tired."),
    ],
    [
        (BOX + " ¿Cuál idea es más significativa para comentar? a) los vecinos comparten libros b) la caja es de madera", "a) los vecinos comparten libros", "Lleva a hablar de comunidad; la madera es un detalle."),
        (ROBOT + " ¿Qué preocupa a algunos profesores?", "Que los estudiantes dejen de pedir ayuda a las personas", "Dice may stop asking people for help."),
        (ROBOT + " ¿Con qué asignatura conectas mejor el texto del robot? a) Tecnología b) Educación Física", "a) Tecnología", "Un robot es una herramienta tecnológica."),
    ],
    [
        ("Elige la frase que conecta una idea con otra asignatura. a) I learned about neighbors and rules in Social Studies. b) I learned about neighbors yesterday.", "a) I learned about neighbors and rules in Social Studies.", "Nombra el tema y la asignatura."),
        ("¿Qué frase usa bien el pasado? a) I learned about sharing in school. b) I learn about sharing yesterday.", "a) I learned about sharing in school.", "Learned es el pasado de learn."),
        ("Completa con el pasado de read (se escribe igual): «I ___ about a street library in a newspaper.»", "read", "El pasado de read se escribe read."),
    ],
    [
        ("¿Por qué conviene elegir una idea antes de comentar? a) porque tu opinión se concentra y tiene ejemplos b) para hablar más tiempo", "a) porque tu opinión se concentra y tiene ejemplos", "Una idea clara permite argumentar."),
        (ROBOT + " Para discutir si el robot puede reemplazar a las personas, ¿qué frase del texto elegirías? a) The robot is a tool, not a replacement. b) It can find books.", "a) The robot is a tool, not a replacement.", "Habla directamente de reemplazo."),
    ],
    [
        (BOX + " ¿Cuántas personas con nombre se nombran en el texto?", "2", "Se nombran la señora Lara y Mateo."),
        ("Elige la frase que presenta una idea y dónde la aprendiste. a) I read about a street library in a text. b) I read in about street library.", "a) I read about a street library in a text.", "El orden de las palabras es correcto."),
    ],
    [(BOX + " En clase de Lenguaje comentan este texto. ¿Qué idea elegirías para comentar? a) compartir libros fortalece el barrio b) el color de la caja", "a) compartir libros fortalece el barrio", "Es una idea que se puede opinar y ejemplificar.")],
    [
        ("¿Qué es una idea significativa?", "Una idea que me hace pensar o sentir", "Sirve para reaccionar a un texto."),
        ("¿Cuál es el pasado de learn?", "learned", "Se forma con -ed."),
        ("¿Para qué sirve conectar con otra asignatura?", "Para relacionar lo que leo con lo que sé", "Da más sentido al comentario."),
    ],
    task("Lee este texto: «A school in the south of Chile has a weather station. Students measure the rain every day and write the numbers in a table. They use the data in Mathematics and Science.» (weather station = estación meteorológica, measure = miden, rain = lluvia, table = tabla, data = datos). Elige una idea significativa y escribe dos frases en inglés: una que empiece con I learned about... in... y otra con The most interesting idea is... because...", "I learned about tables in Mathematics. The most interesting idea is the weather station because students use real data.", ["elige una idea significativa", "usa I learned about... in...", "agrega una razón con because"], ["hoja con dos frases", "nota de la persona que leyó"], ["elegir un detalle sin importancia", "no agregar razón"], "Reconoce la idea elegida y pregunta qué otra asignatura podría conectarse."),
    "Lee en voz alta el texto del robot y di cuál idea te hizo pensar más.",
    "Escribe tres frases con I learned about... in... sobre tres asignaturas distintas.",
)

# ------------------------------------------------------------------ clase 2
lesson(
    OA7, 2, MAT,
    "Aprenderé a expresar preferencias, sentimientos y opiniones y a justificarlos de manera simple con I like... because..., I feel... y I think that... Sirve para reaccionar a lo que leo o escucho y explicar por qué.",
    ["Sé usar because para dar una razón.", "Conozco happy, sad y tired."],
    [
        "Para dar una preferencia (preference) usa I like... because... y agrega la razón: I like skating because it is fun. Para decir lo que sientes usa I feel... o I am...: I feel happy, I feel angry, I feel afraid, I feel nervous. Con algunas emociones hay preposiciones: afraid of (miedo a), angry about (enojado por algo) y angry with (enojado con alguien).",
        "Para dar una opinión usa I think that...: I think that the robot is useful because it finds books fast. Una opinión es válida cuando tiene una razón. Después de because escribe un hecho o una explicación, no repitas la misma idea. For example (por ejemplo) introduce una muestra concreta: I like sports. For example, swimming and basketball.",
        "Presta atención a la forma. Después de I like usa un sustantivo o un verbo con -ing (I like music, I like drawing). Después de because va una oración completa con sujeto y verbo (because it is relaxing). Si tu razón es débil, agrega un ejemplo para apoyarla.",
    ],
    [("preference", "preferencia"), ("I feel...", "me siento..."), ("I think that...", "yo pienso que..."), ("afraid of", "con miedo a"), ("angry about / with", "enojado por algo / con alguien"), ("for example", "por ejemplo")],
    [
        ("Preferencia con razón", "Completa: «I like drawing ___ it is relaxing.» (because / but)", ["Después del espacio hay una razón.", "Because introduce la razón.", "I like drawing because it is relaxing."], "because"),
        ("Sentimiento", "María perdió su cuaderno y dice «I feel sad». ¿Cómo se siente?", ["Sad significa triste.", "Perdió algo importante.", "Se siente triste."], "Triste"),
    ],
    [
        ("Repetir la idea como razón: «I like chess because I like chess».", "La razón no explica nada.", "Da una razón distinta: because it makes me think."),
        ("Usar afraid with en vez de afraid of.", "Se traduce la preposición del español.", "Aprende la combinación: afraid of."),
    ],
    [
        ("¿Qué significa «I feel afraid»?", "Tengo miedo", "Afraid es asustado."),
        ("¿Qué significa «I think that...»?", "Yo pienso que...", "Introduce una opinión."),
        ("Completa con una razón: «I like board games because ___». a) they are fun with friends b) yesterday", "a) they are fun with friends", "Después de because va una razón completa."),
    ],
    [
        ("Perdiste un partido importante. ¿Cómo te sientes más probablemente? a) sad b) excited", "a) sad", "Perder un partido suele dar tristeza."),
        ("Completa con la preposición: «I am angry ___ the noise.» (about / with). Escribe la que se usa con un ruido.", "about", "Se usa about con cosas y with con personas."),
        ("¿Qué frase expresa una opinión y no un hecho? a) I think that the film is boring. b) The film lasts two hours.", "a) I think that the film is boring.", "Boring es una valoración personal."),
    ],
    [
        ("Completa: «Mateo is angry ___ his brother because he broke his toy.» (about / with)", "with", "Se usa with con una persona."),
        ("Mañana tienes un examen y sientes preocupación. ¿Qué palabra completa «I feel ___»? a) nervous b) hungry", "a) nervous", "Nervous es nervioso."),
        ("En «I think that the robot is useful because it finds books fast», ¿cuál es la razón?", "it finds books fast", "Va después de because."),
    ],
    [
        ("Tomás dice «I like chess because I like chess». ¿Qué le falta? a) una razón distinta b) una palabra más larga", "a) una razón distinta", "Repetir la idea no explica."),
        ("Ordena las palabras para formar una frase: because / I / music / like / relaxing / is / it", "I like music because it is relaxing.", "Sujeto y verbo, luego because y la razón."),
    ],
    [
        ("¿Qué expresión introduce un ejemplo?", "For example", "Significa por ejemplo."),
        ("En «I like sports. For example, swimming and basketball», ¿cuántos deportes se nombran?", "2", "Se nombran natación y básquetbol."),
    ],
    [("Tu amigo pregunta «Do you like cooking?». ¿Qué respuesta tiene opinión y razón? a) Yes, I do, because it is creative. b) Yes, because yesterday.", "a) Yes, I do, because it is creative.", "Tiene una razón completa.")],
    [
        ("¿Qué frase uso para dar una opinión?", "I think that...", "Introduce lo que pienso."),
        ("En Inglés de 7.º (OA 7, clase 2): ¿Qué va después de because?", "Una razón completa", "Con sujeto y verbo."),
        ("¿Qué preposición usa afraid?", "Of", "Se dice afraid of."),
    ],
    task("Escribe tres frases en inglés sobre estas ideas: tu actividad favorita (con I like... because...), una emoción que sentiste hoy (con I feel...) y una opinión sobre el texto del robot (con I think that...). Léelas en voz alta a una persona de tu casa.", "I like drawing because it is relaxing. I feel happy today. I think that the robot is useful because it finds books fast.", ["escribe las tres frases pedidas", "cada razón es distinta de la idea", "las lee en voz alta"], ["hoja con tres frases", "nota de la persona que escuchó"], ["razón repetida", "usar la preposición equivocada"], "Reconoce las frases correctas y ayuda a mejorar la razón si es débil."),
    "Dile a una persona de tu casa tres cosas que te gustan y por qué, siempre con because.",
    "Escribe un párrafo de cuatro frases sobre un deporte, con I like, I feel, I think that y for example.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA7, 3, MAT,
    "Aprenderé a conectar un texto con otro texto, con mi vida diaria o con mi cultura, usando casos ficticios o ejemplos seguros. Sirve para dar sentido a lo que leo sin compartir datos personales.",
    ["Sé elegir una idea significativa.", "Conozco similar, remind y because."],
    [
        "Conectar es relacionar lo que lees con algo que ya conoces. Puedes conectar con otro texto: This story is similar to the street library because both are about neighbors who work together. Con una experiencia de vida cotidiana: It reminds me of a school clean-up day. Con otra asignatura: In Science I learned that plants need water. O con tu cultura: In Chile, many neighborhoods have a neighbors' association.",
        "Para hacerlo de forma segura (safely), no necesitas contar cosas privadas. Puedes usar un caso ficticio, como Imagine a student called Ana who..., o hablar de hechos generales de tu colegio. Evita nombres, direcciones o problemas familiares: tu conexión debe respetar tu privacidad y la de otras personas. Una buena conexión nombra qué se parece y por qué.",
        "Las frases útiles son: It reminds me of... (me recuerda a...), This is similar to... (esto se parece a...) y Both... (ambos...). También usa because para explicar la semejanza. Recuerda que parecerse no es ser idéntico: el huerto y la caja de libros son distintos, pero ambos muestran vecinos que cooperan.",
    ],
    [("connect", "conectar, relacionar"), ("similar to", "parecido a"), ("It reminds me of...", "me recuerda a..."), ("both", "ambos"), ("safely", "de forma segura"), ("schedule", "calendario, horario")],
    [
        ("Encontrar lo común", FIC + " ¿Qué tienen en común este texto y la caja de libros de la calle Pine?", ["Pienso en las personas del texto.", "En los dos, los vecinos trabajan juntos.", "Esa es la semejanza."], "En ambos, los vecinos cooperan por su barrio"),
        ("Conectar de forma segura", "Elige la conexión más segura: a) It reminds me of a school clean-up day. b) It reminds me of a secret problem of my neighbor.", ["Una conexión no debe contar cosas privadas.", "El día de limpieza del colegio es una experiencia general.", "La opción a es segura."], "a) It reminds me of a school clean-up day."),
    ],
    [
        ("Contar un problema privado como conexión.", "No se cuida la privacidad.", "Usa un caso ficticio o un hecho general."),
        ("Decir que dos textos son lo mismo.", "Se exagera la semejanza.", "Di en qué se parecen y en qué se diferencian."),
    ],
    [
        (FIC + " ¿Qué hizo Ana para cuidar el huerto?", "Hizo un calendario de riego", "Dice Ana makes a schedule."),
        (FIC + " ¿Cuántas veces a la semana riega cada niño?", "1", "Dice once a week."),
        ("En Inglés de 7.º (OA 7, clase 3): ¿Qué significa «It reminds me of»?", "Me recuerda a", "Introduce una conexión."),
    ],
    [
        (FIC + " ¿Qué pasó al principio con el huerto? a) nadie lo cuidaba y las flores murieron b) estaba lleno de color", "a) nadie lo cuidaba y las flores murieron", "Dice nobody takes care of it, so the flowers die."),
        ("¿Qué conexión es más segura? a) It reminds me of a school clean-up day. b) It reminds me of a secret problem of my neighbor.", "a) It reminds me of a school clean-up day.", "No cuenta cosas privadas."),
        (FIC + " ¿Cómo está el huerto después de un mes? a) lleno de color b) vacío", "a) lleno de color", "Dice full of color."),
    ],
    [
        ("Completa: «This story is similar to the street library ___ both are about neighbors.» (because / but)", "because", "Because introduce el motivo de la semejanza."),
        ("¿Qué frase conecta con Ciencias? a) In Science I learned that plants need water. b) In Science I learned that plants do not need water.", "a) In Science I learned that plants need water.", "Es un hecho correcto de Ciencias."),
        arith(FIC + " Si hay 4 semanas en un mes y cada niño riega una vez por semana, ¿cuántas veces riega cada niño en un mes?", "1*4", "Una vez por semana durante 4 semanas.", " veces"),
    ],
    [
        ("¿Por qué usar un caso ficticio como Ana para conectar? a) para no compartir datos personales o privados b) para inventar mentiras", "a) para no compartir datos personales o privados", "Cuida la privacidad."),
        ("Mateo dice que el huerto y la caja de libros son lo mismo. ¿Tiene razón? Responde sí o no.", "No", "Se parecen en la cooperación, pero son proyectos distintos."),
    ],
    [
        (BOX + " ¿Qué día lee la señora Lara en la caja de libros?", "El viernes", "Dice Mrs. Lara reads there every Friday."),
        ("¿Qué palabra de la conexión significa «ambos»?", "Both", "Both se usa para dos cosas."),
    ],
    [("En tu barrio quieren juntar libros para compartir. Conecta con la caja de la calle Pine. ¿Qué frase escribes? a) This is similar to the street library because neighbors share books. b) This is similar to a football match because it is long.", "a) This is similar to the street library because neighbors share books.", "Explica qué se parece y por qué.")],
    [
        ("¿Con qué puedo conectar un texto?", "Con otro texto, la vida diaria, otras asignaturas o mi cultura", "Así le doy sentido."),
        ("¿Qué debo cuidar al conectar?", "La privacidad", "No cuento datos personales ni privados."),
        ("En Inglés de 7.º (OA 7, clase 3): ¿Qué significa «both»?", "Ambos", "Se usa para dos cosas o personas."),
    ],
    task("Lee este texto: «At a school in Valdivia, students plant a vegetable bed. Each class takes care of one row. In summer, they cook a soup with the vegetables and share it with the whole school.» (vegetable bed = cama de cultivo, row = hilera, cook = cocinar, soup = sopa, share = compartir). Escribe tres frases de conexión: una con otro texto de esta clase, una con una asignatura y una con tu vida diaria (sin datos privados).", "This is similar to the garden of Ana because children take care of plants. In Science I learned that plants need sun and water. It reminds me of a school clean-up day.", ["escribe tres conexiones", "usa similar to o reminds me", "no cuenta datos privados"], ["hoja con tres frases", "nota de la persona que leyó"], ["contar problemas privados", "no explicar la semejanza"], "Reconoce las conexiones acertadas y revisa que cada una diga por qué se parece."),
    "Lee en voz alta el texto del huerto de Ana y di en qué se parece a algo que hiciste en el colegio.",
    "Escribe una conexión entre el texto del robot y un texto que hayas leído en otra asignatura.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA7, 4, MAT,
    "Aprenderé a conversar con personas que opinan distinto, a hacer preguntas con do, does y did y a responder con respeto. Sirve para discutir ideas sin pelear.",
    ["Sé dar una opinión con I think that... because...", "Conozco agree, maybe y why."],
    [
        "Cuando varias personas opinan distinto, la conversación mejora si hay respeto. Para estar de acuerdo usa I agree o Me too. Para no estarlo, di I do not agree o I see your point, but... (entiendo tu punto, pero...), y agrega tu razón. Para pedir razones, pregunta Why do you think that? Evita frases que ataquen a la persona, como «that's stupid».",
        "Las preguntas con do, does y did sirven para averiguar más. Con I, you, we o they usa do: Do you like sports? Con he, she o it usa does: Does Carla think homework helps? Para el pasado usa did con todos: Did Carla finish her homework yesterday? Después de do, does o did el verbo queda en forma simple: Does she think..., Did she finish... Para preguntar la razón agrega why: Why does Luis feel tired?",
        "También puedes proponer un acuerdo intermedio: Maybe we need less homework on Fridays. Los desacuerdos son parte de aprender: lo importante es escuchar, preguntar y justificar. Al terminar, resume lo que dijo cada persona con tus palabras, para comprobar que entendiste: Luis thinks..., Carla thinks...",
    ],
    [("I agree / I do not agree", "estoy de acuerdo / no estoy de acuerdo"), ("I see your point, but...", "entiendo tu punto, pero..."), ("Why do you think that?", "¿Por qué piensas eso?"), ("do / does / did", "auxiliares de pregunta (presente / pasado)"), ("maybe", "quizás"), ("respect", "respeto")],
    [
        ("Quién opina qué", DEBATE + " ¿Qué opina Carla de la tarea?", ["Busco el nombre Carla.", "Dice I think homework helps us practice.", "Carla piensa que la tarea ayuda a practicar."], "Que la tarea ayuda a practicar"),
        ("Una pregunta con does", "Completa: «___ does Carla think homework helps?» (Why / Where)", ["Se pregunta la razón.", "Why significa por qué.", "La palabra es Why."], "Why"),
    ],
    [
        ("Usar do con she, he o it.", "Se olvida que con tercera persona va does.", "Usa does con he, she o it."),
        ("Atacar a la persona en vez de responder a su idea.", "Se pierde el respeto.", "Usa I see your point, but... y da una razón."),
    ],
    [
        (DEBATE + " ¿Qué opina Luis? a) que necesitan menos tarea b) que necesitan más tarea", "a) que necesitan menos tarea", "Dice we need less homework."),
        (DEBATE + " ¿Qué opina Carla?", "Que la tarea ayuda a practicar", "Dice homework helps us practice."),
        (DEBATE + " ¿Qué propone Julián?", "Menos tarea los viernes", "Dice Maybe we need less homework on Fridays."),
    ],
    [
        ("¿Qué significa «I do not agree»?", "No estoy de acuerdo", "Expresa un desacuerdo con respeto."),
        (DEBATE + " Cuando la profesora pregunta «Why do you think that?», ¿qué pide a Julián? a) una razón b) una fecha", "a) una razón", "Why pregunta por la razón."),
        ("¿Qué frase muestra respeto antes de dar tu opinión? a) I see your point, but... b) You are wrong.", "a) I see your point, but...", "Reconoce la idea del otro."),
    ],
    [
        ("Completa con do o does: «___ Luis like homework?»", "Does", "Luis equivale a he, y con he se usa does."),
        ("Completa la pregunta en pasado: «___ Carla finish her homework yesterday?» (Did / Does)", "Did", "Yesterday indica el pasado."),
        ("Completa con do o does: «___ you like sports on Friday?»", "Do", "Con you se usa do."),
    ],
    [
        ("¿Cuál es una respuesta respetuosa a una opinión distinta? a) I see your point, but I think we need practice. b) That is silly.", "a) I see your point, but I think we need practice.", "Reconoce la idea y da una razón."),
        (DEBATE + " ¿Quién propone una solución intermedia?", "Julián", "Dice Maybe we need less homework on Fridays."),
    ],
    [
        arith("En una encuesta, 12 estudiantes quieren menos tarea, 8 no quieren cambios y 5 no están seguros. ¿Cuántos estudiantes respondieron?", "12+8+5", "Se suman las tres respuestas.", " estudiantes"),
        ("Ordena las palabras para formar una pregunta: Julián / why / think / does / that", "Why does Julián think that?", "Why va primero y does va antes del sujeto."),
    ],
    [("Tu amigo dice que prefiere el invierno, y tú prefieres el verano. ¿Qué respondes con respeto? a) I see your point, but I prefer summer because it is warm. b) You are wrong.", "a) I see your point, but I prefer summer because it is warm.", "Respeta la idea del amigo y da una razón.")],
    [
        ("¿Qué auxiliar se usa con she en una pregunta en presente?", "Does", "Does va con he, she o it."),
        ("En Inglés de 7.º (OA 7, clase 4): ¿Qué auxiliar se usa en preguntas en pasado?", "Did", "Se usa con todas las personas."),
        ("¿Qué frase muestra que entiendes al otro antes de responder?", "I see your point, but...", "Reconoce su idea."),
    ],
    task("Con una persona de tu casa, haz esta práctica: ella dice una opinión («I think the school day is too long») y tú respondes con respeto usando I see your point, but... y una razón. Luego escribe tres preguntas en inglés para saber más: una con Why does..., una con Do you... y una con Did you...", "I see your point, but I think the day is not too long because we have recess. Why does she think so? Do you like recess? Did you finish your homework?", ["responde con respeto y razón", "escribe las tres preguntas con el auxiliar correcto", "las dice en voz alta"], ["hoja con respuesta y preguntas", "nota de la persona que participó"], ["usar do con she", "no dar razón"], "Reconoce las preguntas bien formadas y revisa los auxiliares con la persona de tu casa."),
    "Practica decir tres veces I see your point, but... con razones distintas.",
    "Escribe un diálogo de seis líneas entre dos estudiantes que opinan distinto sobre el uso del celular en el colegio.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA7, 5, MAT,
    "Aprenderé a respaldar mi reacción con evidencia del texto, a resumir con apoyo y a generar preguntas. Sirve para que mi opinión se base en lo que dice el texto.",
    ["Sé expresar una opinión con una razón.", "Sé hacer preguntas con do, does y did."],
    [
        "Una reacción con evidencia tiene tres partes: tu idea, la evidencia (evidence) del texto y una explicación. Por ejemplo: I think the group is useful because they collected sixty bags of rubbish. Aquí la idea es que el grupo es útil, y la evidencia es el dato de las sesenta bolsas. Sin evidencia, una opinión suena débil: I think it is good no dice por qué.",
        "Para encontrar evidencia, busca datos concretos del texto: números, acciones y resultados. Evidencia puede ser They planted twenty small trees o The park looks better now. Los datos se pueden comprobar y las opiniones no. Usa for example para presentar un dato como ejemplo: For example, many families joined them.",
        "Luego resume con apoyo (summarize): una o dos frases con las ideas principales. Un buen resumen del texto es: A group cleans a river park, collects rubbish and plants trees with the help of families. Por último, genera preguntas: Did the volunteers plant trees? Do many families help? Con ellas profundizas lo que leíste y abres la conversación.",
    ],
    [("evidence", "evidencia: dato del texto"), ("summarize", "resumir"), ("question", "pregunta"), ("for example", "por ejemplo"), ("volunteer", "voluntario"), ("collect", "recoger")],
    [
        ("Respaldar una opinión", VOL + " Opinión: «The group is useful». ¿Qué dato del texto la respalda?", ["Busco un dato que muestre utilidad.", "Recogieron sesenta bolsas de basura.", "Ese número es evidencia."], "Collected sixty bags of rubbish"),
        ("Generar una pregunta", "Forma una pregunta con did sobre «The volunteers planted trees».", ["Para el pasado uso did.", "Después de did el verbo va simple: plant.", "Did the volunteers plant trees?"], "Did the volunteers plant trees?"),
    ],
    [
        ("Dar una opinión sin evidencia.", "No se explica por qué se piensa así.", "Agrega un dato del texto con because."),
        ("Resumir con todos los detalles.", "Se pierde la idea central.", "Usa una o dos frases con las ideas principales."),
    ],
    [
        (VOL + " ¿Cuántas bolsas de basura recogieron?", "60", "Dice sixty bags."),
        (VOL + " ¿Cuántos árboles plantaron?", "20", "Dice twenty small trees."),
        (VOL + " ¿Cuándo limpian el parque? a) cada sábado b) cada lunes", "a) cada sábado", "Dice every Saturday."),
    ],
    [
        (VOL + " ¿Qué frase respalda la reacción «the group is useful»? a) They collected sixty bags of rubbish. b) The park is near a river.", "a) They collected sixty bags of rubbish.", "Muestra un resultado concreto."),
        ("¿Qué expresión introduce un ejemplo en inglés?", "For example", "Presenta un caso concreto."),
        (VOL + " Reacción: «People care about the park». ¿Qué dato respalda esa idea? a) Many families joined them. b) They plant trees.", "a) Many families joined them.", "Muestra que las personas participan."),
    ],
    [
        arith(VOL + " Si recogen 60 bolsas en un mes con 4 sábados, ¿cuántas bolsas recogen por sábado en promedio?", "60//4", "Se reparten las 60 bolsas entre los 4 sábados.", " bolsas"),
        (VOL + " ¿Cuál es el mejor resumen? a) A group cleans a river park, collects rubbish and plants trees with families. b) A group sells trees.", "a) A group cleans a river park, collects rubbish and plants trees with families.", "Resume las ideas principales."),
        ("¿Qué pregunta está bien formada? a) Did the volunteers plant trees? b) Do the volunteers planted trees?", "a) Did the volunteers plant trees?", "Después de did el verbo va simple."),
    ],
    [
        ("Una reacción dice «I think it is good» y no agrega más. ¿Qué le falta? a) una razón o ejemplo del texto b) otro saludo", "a) una razón o ejemplo del texto", "La evidencia hace sólida la opinión."),
        (VOL + " ¿«They planted twenty small trees» es un hecho o una opinión? a) un hecho b) una opinión", "a) un hecho", "Se puede comprobar con el texto."),
    ],
    [
        ("Completa la reacción: «I think the group is useful because ___». Usa como evidencia el dato de las bolsas de basura del texto de los voluntarios.", "they collected sixty bags of rubbish", "Es el dato de las bolsas del texto."),
        arith("Si cada mes plantan 20 árboles, ¿cuántos plantan en 3 meses?", "20*3", "Se multiplican los árboles por mes por los meses.", " árboles"),
    ],
    [("Una amiga pregunta «Why do you like the volunteers?». ¿Qué respuesta usa evidencia? a) I like them because they planted twenty small trees. b) I like them because yes.", "a) I like them because they planted twenty small trees.", "Usa un dato del texto.")],
    [
        ("¿Qué tres partes tiene una reacción con evidencia?", "Idea, evidencia y explicación", "Así se sostiene la opinión."),
        ("¿Qué incluye un buen resumen?", "Las ideas principales", "Sin detalles pequeños."),
        ("En Inglés de 7.º (OA 7, clase 5): ¿Qué auxiliar se usa en preguntas en pasado?", "Did", "Se usa con todas las personas."),
    ],
    task("Lee este texto: «The school choir sings every Thursday. Last week, it sang for the people of a nursing home. The visitors clapped and some of them sang too. The choir wants to visit another home next month.» (choir = coro, nursing home = hogar de ancianos, visitors = visitas, clapped = aplaudieron). Escribe una reacción con I think... because... y una evidencia, un resumen de una frase y una pregunta con did.", "I think the choir is kind because it sang for the people of a nursing home. Resumen: the choir sings for others. Did the visitors sing too?", ["reacción con razón y evidencia", "resumen en una frase", "pregunta bien formada"], ["hoja con tres respuestas", "nota de la persona que leyó"], ["opinión sin evidencia", "pregunta con did y verbo en pasado"], "Reconoce lo que acertó y revisa que la evidencia sea un dato del texto."),
    "Escribe una pregunta con do, otra con does y otra con did sobre el texto de los voluntarios.",
    "Escribe una reacción de cuatro frases a un texto que hayas leído en el colegio, con una evidencia y una pregunta.",
)
