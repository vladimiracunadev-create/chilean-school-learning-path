"""Cuaderno del estudiante, 1.º medio Inglés (oficial), IN1M OA 07: respuesta personal y discusión apoyadas en evidencia.

Las clases del plan son genéricas; aquí se aplican a: conexiones con otras asignaturas, la vida y otras culturas; relaciones entre
ideas; opiniones y puntos de vista; preguntas e hipótesis; y una discusión independiente. Los textos, encuestas (datos «de
ejemplo») y diálogos van escritos en cada enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN1M OA 07"
MAT = "Los textos, tablas y diálogos escritos en cada ejercicio, lápiz y una hoja para anotar; si quieres, una persona de tu casa para conversar."


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


# ------------------------------------------------------------------ clase 1: hacer conexiones
W_PLASTIC = "«Plastic bottles stay in nature for a very long time. Some cities now collect and recycle them.» (plastic = plástico, bottles = botellas, nature = naturaleza, for a very long time = por mucho tiempo, collect = recolectar)"
BEES = "«Bees are very important for fruit and vegetables because they carry pollen from flower to flower. In some places, the number of bees is falling.» (bees = abejas, pollen = polen, flower = flor, falling = bajando)"
FIESTA = "«In Chile, many families celebrate Fiestas Patrias with traditional food such as empanadas and with dances. Other countries also have national holidays with special food and music.» (celebrate = celebrar, traditional = tradicional, dances = bailes, national holidays = fiestas nacionales)"
SPAIN = "«A teenager in Spain says she walks to school every day because it is only ten minutes from her house. In many cities, students take the bus or the metro.» (teenager = adolescente, walks = camina, take the bus = toma el bus, metro = metro)"

lesson(
    OA, 1, MAT,
    "Aprenderé a reaccionar a un texto conectándolo con otras asignaturas, con mi lengua materna y mi cultura, con la vida cotidiana y con mis experiencias, usando frases como I used to... o I have read... Sirve para dar respuestas personales y bien apoyadas.",
    ["Sé leer o escuchar un texto corto y entender la idea principal.", "Conozco el pasado simple y used to."],
    [
        "Reaccionar a un texto (to respond to a text) es más que decir me gustó. Una buena respuesta conecta lo que leíste o escuchaste con algo que ya sabes. Puedes conectar con otras asignaturas (In Science, we learned that...), con tu lengua materna (Pollen is similar to polen in Spanish), con tu vida cotidiana (At my house...) o con otras culturas (In Chile, ... but in other countries...).",
        "Dos estructuras te ayudan a hablar de experiencias. Used to + verbo cuenta un hábito pasado que ya no existe: I used to throw bottles in any bin, but now I recycle. Have o has + participio cuenta una experiencia hasta hoy sin decir cuándo: I have read a book about bees; she has learned about plants. Con yesterday o last week no se usa have: se usa el pasado, como I visited the beach yesterday.",
        "Una conexión debe relacionarse con el contenido del texto. Si el texto habla de abejas, una respuesta sobre colores no es una buena conexión. Para comprobarlo pregúntate: ¿qué parte del texto me recuerda esto? Si no hay respuesta, busca otra conexión. Mientras más específico sea el dato que conectas, más sólida es tu respuesta.",
    ],
    [("connect", "conectar, relacionar"), ("I used to...", "yo solía..."), ("I have read...", "he leído..."), ("In Science, we learned...", "En Ciencias, aprendimos..."), ("At my house...", "En mi casa..."), ("similar", "parecido")],
    [
        ("Conectar con otra asignatura", W_PLASTIC + " ¿Qué respuesta conecta el texto con Ciencias?  A) In Science, we learned that some materials break down slowly. B) In Art, we painted with watercolours.", ["Busco una idea del texto: el plástico permanece mucho tiempo.", "Pienso en Ciencias: materiales que se degradan lentamente.", "La opción A se relaciona con esa idea."], "A) In Science, we learned that some materials break down slowly."),
        ("Contar un hábito pasado", W_PLASTIC + " Quieres decir que antes botabas botellas y ahora reciclas. ¿Qué frase usas?", ["El hábito ya no existe: uso used to.", "Agrego el contraste con now.", "Digo: I used to throw bottles away, but now I recycle."], "I used to throw bottles away, but now I recycle."),
    ],
    [
        ("Dar una respuesta que no se relaciona con el texto.", "Se cree que cualquier opinión es una conexión.", "Pregúntate qué parte del texto te recuerda lo que dices."),
        ("Usar have con yesterday, como I have visited the beach yesterday.", "Se mezcla la experiencia hasta hoy con una fecha pasada.", "Con yesterday usa el pasado: I visited the beach yesterday."),
    ],
    [
        (BEES + " ¿Qué respuesta conecta con Ciencias? A) In Science, we learned that bees carry pollen. B) In Art, we painted a landscape.", "A) In Science, we learned that bees carry pollen.", "Se relaciona con la idea del texto."),
        (FIESTA + " ¿Qué respuesta conecta con tu vida cotidiana? A) At my house, we also eat special food on holidays. B) The text has two sentences.", "A) At my house, we also eat special food on holidays.", "Une el tema de las fiestas con algo cotidiano."),
        ("¿Qué frase habla de una experiencia hasta hoy? A) I have read a book about bees. B) I have read a book yesterday.", "A) I have read a book about bees.", "Con yesterday no se usa have."),
    ],
    [
        ("Respondes a un texto sobre reciclaje. ¿Qué frase habla de un hábito pasado? A) I used to buy bottled water, but now I use my own bottle. B) I am buying bottled water now.", "A) I used to buy bottled water, but now I use my own bottle.", "Used to + verbo cuenta algo que ya no ocurre."),
        (SPAIN + " ¿Qué respuesta conecta con otra cultura? A) In Chile, many students also walk to school, but others take the bus. B) The girl is ten years old.", "A) In Chile, many students also walk to school, but others take the bus.", "Compara dos lugares."),
        (BEES + " ¿Qué respuesta usa tu lengua materna? A) Pollen is similar to polen in Spanish. B) Pollen is a difficult word.", "A) Pollen is similar to polen in Spanish.", "Relaciona la palabra con el español."),
    ],
    [
        ("Completa: «I ___ seen a documentary about bees.» A) have B) has", "A) have", "Con I se usa have."),
        ("Completa: «She ___ learned about plants in Science.» A) has B) have", "A) has", "Con she se usa has."),
        ("¿Qué frase es correcta? A) I used to collect stamps, but now I don't. B) I use to collect stamps, but now I don't.", "A) I used to collect stamps, but now I don't.", "En pasado se dice used to."),
    ],
    [
        (BEES + " Un compañero responde «I like colours». ¿Por qué no es buena conexión? A) no se relaciona con lo que dice el texto B) no usa have", "A) no se relaciona con lo que dice el texto", "Una conexión parte de una idea del texto."),
        ("Tu compañero dice «I have visited the beach yesterday». ¿Qué problema tiene? A) con yesterday se usa el pasado: I visited the beach yesterday B) falta used to", "A) con yesterday se usa el pasado: I visited the beach yesterday", "Yesterday es una fecha concreta del pasado."),
    ],
    [
        (FIESTA + " ¿Qué respuesta combina cultura propia y comparación? A) In my family, we eat empanadas, and other countries also have special food on holidays. B) Other countries have holidays too.", "A) In my family, we eat empanadas, and other countries also have special food on holidays.", "Une una costumbre propia con la idea del texto."),
        arith(SPAIN + " Tu trayecto al colegio dura 15 minutos y el de la adolescente, 10. ¿Cuántos minutos más dura el tuyo?", "15-10", "Se resta 10 a 15.", " minutos"),
    ],
    [("En clase te preguntan «How does the text about bees connect with your life?». ¿Cuál es la mejor respuesta? A) In Science, we learned that bees help plants, and I have seen bees in my garden. B) I don't know.", "A) In Science, we learned that bees help plants, and I have seen bees in my garden.", "Combina Ciencias y una experiencia personal.")],
    [
        ("En Inglés de 1.º medio (OA 7, clase 1): ¿para qué se usa used to + verbo?", "Para hablar de un hábito pasado que ya no existe", "Contrasta antes y ahora."),
        ("En Inglés de 1.º medio (OA 7, clase 1): ¿qué se usa para una experiencia hasta hoy?", "Have o has + participio, como I have read", "No se dice cuándo ocurrió."),
        ("En Inglés de 1.º medio (OA 7, clase 1): ¿qué debe tener una buena conexión?", "Relación con una idea del texto", "Si no, no apoya la respuesta."),
    ],
    task("Lee este texto: «Many people in the world drink tea every day. In some countries, tea time is a special moment with family or friends.» (drink = toman, tea time = la hora del té, special = especial). Escribe en inglés tres frases que conecten el texto con (a) tu vida cotidiana, (b) un hábito pasado con I used to... y (c) otra cultura o asignatura.", "(a) At my house, we have bread and tea in the afternoon. (b) I used to drink juice every afternoon, but now I drink tea. (c) In Science, we learned that tea comes from a plant.", ["cada frase se relaciona con una idea del texto", "una frase usa used to correctamente", "las frases son distintas entre sí"], ["hoja con tres frases", "lectura en voz alta"], ["escribir una conexión sin relación con el té", "usar used to para algo que sigue ocurriendo"], "Reconoce la mejor conexión y pide que explique qué parte del texto la inspiró."),
    "Elige un texto breve de esta clase y escribe una conexión con tu vida y otra con una asignatura.",
    "Cuenta a otra persona, en español, dos hábitos que tenías antes y ya no tienes, y escríbelos con I used to...",
)

# ------------------------------------------------------------------ clase 2: relaciones entre ideas
W_BUS = "«First, I walk five minutes to the bus stop. Then I ride the bus for ten minutes. Finally, I walk three minutes to school.» (walk = camino, ride = viajo, stop = paradero)"
W_RAIN = "«Although it was raining, we played football. If it rains again tomorrow, we will practise inside.» (although = aunque, practise = practicar, inside = adentro)"

lesson(
    OA, 2, MAT,
    "Aprenderé a explicar la relación entre ideas usando although, but, if y first... then... finally. Sirve para que mis explicaciones sean claras y mis argumentos tengan sentido.",
    ["Conozco conectores como and, but, because y so.", "Sé usar first y then para ordenar acciones."],
    [
        "Las ideas se relacionan de distintas maneras y cada relación tiene sus marcas. La secuencia (sequence) ordena hechos: First, Then, Finally. El contraste (contrast) opone ideas: but y although. La condición (condition) dice qué pasa si ocurre algo: If it rains, we will stay home. La causa y la consecuencia se marcan con because y so.",
        "But va entre dos ideas y significa pero: The park is small, but it is beautiful. Although (aunque) puede ir al inicio o en medio: Although it was raining, we played football. En la frase con If, después de if se usa el presente y en la otra parte will: If we recycle, the city will be cleaner. La secuencia pide un orden lógico: no puede decirse Finally al principio.",
        "Para explicar una relación, pregúntate: ¿Estas ideas se oponen?, ¿una depende de otra?, ¿van en orden? Luego elige el conector. Si cambias el conector, cambia el sentido: Although I am tired, I will study (a pesar del cansancio) no significa lo mismo que Because I am tired, I will study (el cansancio es la razón).",
    ],
    [("although", "aunque"), ("but", "pero"), ("if", "si (condición)"), ("first, then, finally", "primero, luego, finalmente"), ("because / so", "porque / entonces"), ("relationship", "relación")],
    [
        ("Reconocer una secuencia", W_BUS + " ¿Cuántos minutos dura en total el camino al colegio?", ["Identifico los tres pasos: 5, 10 y 3 minutos.", "Los sumo: 5 + 10 + 3.", "El total es 18."], "18 minutos"),
        ("Reconocer contraste y condición", W_RAIN + " ¿Qué conector muestra contraste y cuál muestra condición?", ["Although opone: llovía, pero jugaron.", "If marca una condición futura.", "Contraste: although; condición: if."], "Contraste: although; condición: if"),
    ],
    [
        ("Usar Finally al comienzo de una secuencia.", "Se piensa en la palabra y no en el orden de los hechos.", "Pon First al inicio y Finally al final."),
        ("Cambiar although por because sin notar que cambia el sentido.", "Ambos conectan ideas, pero uno opone y otro explica.", "Pregunta si la segunda idea es una razón o un contraste."),
    ],
    [
        ("«Although it was cheap, I didn't buy it.» ¿Qué relación expresa? A) contraste B) secuencia", "A) contraste", "Although opone dos ideas."),
        ("«First, wash the fruit. Then, cut it.» ¿Qué relación expresa? A) secuencia B) condición", "A) secuencia", "First y Then ordenan los pasos."),
        ("«If it rains, we will stay home.» ¿Qué relación expresa? A) condición B) contraste", "A) condición", "If dice qué ocurre en cierto caso."),
    ],
    [
        ("Completa: «The film was long, ___ it was interesting.» A) but B) if", "A) but", "Se opone long a interesting."),
        ("Completa: «___ you study, you will pass the test.» A) If B) Although", "A) If", "Es una condición."),
        ("Completa: «___ the bus was late, we arrived on time.» A) Although B) If", "A) Although", "Se opone llegar tarde el bus y llegar a tiempo."),
    ],
    [
        ("Ordena con letras los pasos para plantar una semilla: (a) Finally, water it every day. (b) First, put soil in a pot. (c) Then, plant the seed.", "b, c, a", "First, Then y Finally ordenan la secuencia."),
        ("¿Qué oración expresa una condición? A) If we recycle, the city will be cleaner. B) We recycle and the city is clean.", "A) If we recycle, the city will be cleaner.", "Usa If y will."),
        arith("«First, I walk 6 minutes to the bus stop. Then I ride the bus for 14 minutes. Finally, I walk 4 minutes to school.» ¿Cuántos minutos dura en total el camino?", "6+14+4", "Se suman los tres tramos de la secuencia.", " minutos"),
    ],
    [
        ("Compara: «Although I am tired, I will study» y «Because I am tired, I will study». ¿Qué cambia? A) la primera muestra contraste; la segunda, una razón B) la primera muestra una razón; la segunda, un contraste", "A) la primera muestra contraste; la segunda, una razón", "El conector cambia el sentido de la relación."),
        ("Un compañero escribe: «Finally, we met at the cinema. First, we bought tickets.» ¿Qué error tiene? A) el orden de los conectores no coincide con el orden lógico B) falta una coma", "A) el orden de los conectores no coincide con el orden lógico", "First debe ir al inicio y Finally al final."),
    ],
    [
        ("Texto: «First, wash the fruit. Then cut it. Although it is simple, many people forget to wash it. If you wash it, the fruit is safer.» ¿Qué conector muestra contraste? A) Although B) Then", "A) Although", "Opone lo simple con olvidar lavarla."),
        ("Texto: «First, wash the fruit. Then cut it. Although it is simple, many people forget to wash it. If you wash it, the fruit is safer.» ¿Qué conector muestra condición? A) If B) First", "A) If", "Dice qué pasa en el caso de lavarla."),
    ],
    [("Explicas a un compañero por qué recicla tu familia. ¿Qué explicación usa bien un contraste? A) We recycle paper, but it takes time to separate it. B) We recycle paper if it takes time.", "A) We recycle paper, but it takes time to separate it.", "But opone el beneficio y la dificultad.")],
    [
        ("En Inglés de 1.º medio (OA 7, clase 2): ¿qué relación marca if?", "Una condición", "Dice qué pasa en cierto caso."),
        ("En Inglés de 1.º medio (OA 7, clase 2): ¿qué relación marcan first, then y finally?", "Una secuencia u orden", "Ordenan los pasos."),
        ("En Inglés de 1.º medio (OA 7, clase 2): ¿qué relación marcan but y although?", "Un contraste", "Oponen dos ideas."),
    ],
    task("Escribe en inglés cuatro frases sobre cómo llegas al colegio (o a otro lugar que visitas seguido): una con First, Then y Finally para el orden de tu trayecto, una con but, una con although y una con if. Los números o tiempos pueden ser de ejemplo.", "First, I walk five minutes to the bus stop. Then I ride the bus. Finally, I arrive at school. The bus is fast, but it is crowded. Although it is far, I like the trip. If it rains, I take an umbrella.", ["usa First, Then y Finally en orden", "usa but y although con ideas opuestas", "usa if con una condición real"], ["hoja con cuatro frases", "lectura en voz alta"], ["usar although sin contraste", "poner Finally al inicio"], "Reconoce la relación bien expresada y pide revisar el conector cuando las ideas no se oponen."),
    "Subraya los conectores en un texto breve en inglés y escribe qué relación expresa cada uno.",
    "Escribe una frase con although, una con but y una con if sobre tu deporte o pasatiempo favorito.",
)

# ------------------------------------------------------------------ clase 3: opiniones y puntos de vista
SURVEY = "Encuesta de ejemplo a 30 estudiantes: 18 caminan al colegio, 8 usan bus y 4 van en auto."

lesson(
    OA, 3, MAT,
    "Aprenderé a expresar sentimientos, interpretaciones y puntos de vista con frases como In my opinion..., I think... y according to..., y a apoyarlos con razones. Sirve para participar en discusiones con respeto y evidencia.",
    ["Sé conectar un texto con mi vida.", "Conozco because para dar razones."],
    [
        "Una opinión (opinion) es lo que piensas, y se marca con frases como In my opinion..., I think..., I believe... o I feel.... Un hecho (fact) es un dato que se puede comprobar. According to... significa según... y atribuye una información a una fuente: According to the survey, 18 of 30 students walk. Aquí el dato viene de la encuesta; no es tu opinión.",
        "Para dar un buen punto de vista, agrega una razón con because: In my opinion, walking is good because it is free and healthy. Sin razón, tu opinión queda débil. También puedes expresar acuerdo y desacuerdo: I agree with you, I see your point, but I disagree because.... Estas frases son respetuosas y permiten seguir conversando sin atacar a la otra persona.",
        "Los sentimientos se expresan con I feel y adjetivos: I feel proud, I feel worried. Una interpretación (interpretation) es lo que entiendes de un texto: The story shows that friends help each other. Una interpretación necesita apoyo en el texto. Si no hay evidencia, es solo una suposición y conviene decir Maybe....",
    ],
    [("In my opinion", "en mi opinión"), ("I think / I believe", "creo que"), ("According to...", "según..."), ("I agree / I disagree", "estoy de acuerdo / en desacuerdo"), ("I feel", "me siento"), ("I see your point, but...", "entiendo tu punto, pero...")],
    [
        ("Distinguir hecho y fuente", SURVEY + " ¿Qué frase atribuye el dato a la fuente? A) According to the survey, 18 students walk. B) I think 18 students walk.", ["Busco una frase que nombre la fuente.", "According to the survey lo hace.", "I think expresa una opinión."], "A) According to the survey, 18 students walk."),
        ("Apoyar una opinión", "Quieres opinar que caminar al colegio es bueno. ¿Qué frase está mejor apoyada? A) In my opinion, walking is good because it is free and healthy. B) In my opinion, walking is good.", ["Una opinión necesita una razón.", "Because agrega dos razones: gratis y saludable.", "La frase A es más sólida."], "A) In my opinion, walking is good because it is free and healthy."),
    ],
    [
        ("Presentar una opinión como si fuera un hecho.", "Se omite la frase que marca el punto de vista.", "Usa In my opinion o I think antes de la idea."),
        ("Decir You are wrong para desacordar.", "Se ataca a la persona y no la idea.", "Usa I see your point, but I disagree because...."),
    ],
    [
        ("¿Qué significa In my opinion? A) en mi opinión B) según los datos", "A) en mi opinión", "Marca un punto de vista propio."),
        ("¿Cuál es una opinión? A) The gym is beautiful. B) The school has two gyms.", "A) The gym is beautiful.", "Beautiful es un juicio personal; la cantidad se puede comprobar."),
        ("¿Qué significa According to the survey? A) según la encuesta B) en mi opinión", "A) según la encuesta", "Atribuye el dato a una fuente."),
    ],
    [
        ("¿Qué significa I agree? A) estoy de acuerdo B) estoy en desacuerdo", "A) estoy de acuerdo", "Expresa estar de acuerdo."),
        (SURVEY + " ¿Qué frase atribuye el dato a la fuente? A) According to the survey, 4 students go by car. B) I believe 4 students go by car.", "A) According to the survey, 4 students go by car.", "Nombra la encuesta como fuente."),
        ("¿Qué frase expresa un sentimiento? A) I feel proud. B) I read a book.", "A) I feel proud.", "I feel + adjetivo expresa un sentimiento."),
    ],
    [
        arith(SURVEY + " ¿Cuántos estudiantes caminan o usan bus?", "18+8", "Se suman los dos grupos.", " estudiantes"),
        ("Completa con una razón: «In my opinion, walking is good ___ it is healthy.» A) because B) although", "A) because", "Because introduce la razón."),
        ("Quieres discrepar con respeto. ¿Qué frase eliges? A) I see your point, but I disagree because... B) You are wrong.", "A) I see your point, but I disagree because...", "Reconoce la idea del otro y explica tu razón."),
    ],
    [
        ("¿Qué opinión está mejor apoyada? A) In my opinion, a bus is better because it is faster when it rains. B) In my opinion, a bus is better.", "A) In my opinion, a bus is better because it is faster when it rains.", "Incluye una razón."),
        (SURVEY + " «Eighteen of thirty students walk.» ¿Es un hecho o una opinión? A) un hecho de la encuesta B) una opinión", "A) un hecho de la encuesta", "Es un dato de la fuente."),
    ],
    [
        ("¿Qué frase expresa un sentimiento hacia un texto? A) The story made me feel sad because the dog was alone. B) The story has a dog.", "A) The story made me feel sad because the dog was alone.", "Expresa un sentimiento con razón."),
        ("«The bus often arrives late.» Un estudiante dice «Maybe the driver is lazy». ¿Qué problema tiene? A) es una suposición sin evidencia B) es un hecho de la encuesta", "A) es una suposición sin evidencia", "El texto no da razón de la demora."),
    ],
    [("En una discusión sobre si se permiten celulares en clase, ¿qué opinión usa una frase y una razón? A) In my opinion, phones can help because we can look up words, but we should use them only when the teacher asks. B) In my opinion, phones are bad.", "A) In my opinion, phones can help because we can look up words, but we should use them only when the teacher asks.", "Usa una frase de opinión, una razón y un matiz.")],
    [
        ("En Inglés de 1.º medio (OA 7, clase 3): ¿qué significa according to...?", "Según...: atribuye un dato a una fuente", "Distingue un hecho de una opinión."),
        ("En Inglés de 1.º medio (OA 7, clase 3): ¿qué frase usas para discrepar con respeto?", "I see your point, but I disagree because...", "Reconoce al otro y explica tu razón."),
        ("En Inglés de 1.º medio (OA 7, clase 3): ¿cómo se apoya una opinión?", "Con because y una razón", "Sin razón, la opinión queda débil."),
    ],
    task("Lee este texto: «Many schools are changing the start time. Some people say students sleep better if school starts later. Others say families need early schedules.» (start time = hora de inicio, sleep better = duermen mejor, schedules = horarios). Escribe en inglés tres frases: tu opinión con In my opinion... y una razón, una frase con According to... que atribuya la idea a una fuente del texto y una frase de acuerdo o desacuerdo con I agree o I disagree.", "In my opinion, school should start later because teenagers need more sleep. According to the text, some people say students sleep better if school starts later. I agree with them, but I see why families need early schedules.", ["marca una opinión con razón", "atribuye una idea a una fuente", "usa acuerdo o desacuerdo con respeto"], ["hoja con tres frases", "lectura en voz alta"], ["opinión sin razón", "usar According to para una opinión propia"], "Reconoce el uso de cada frase y pide agregar una razón si falta."),
    "Subraya en un texto de esta clase una frase de opinión y una de hecho.",
    "Conversa con una persona de tu casa sobre un tema (por ejemplo, el horario escolar) y registra una opinión y una razón de cada uno.",
)

# ------------------------------------------------------------------ clase 4: preguntas e hipótesis
lesson(
    OA, 4, MAT,
    "Aprenderé a formular preguntas como How long has he...? y Have they...? y a proponer hipótesis apoyadas en pistas. Sirve para conversar, aclarar dudas y explorar ideas con otras personas.",
    ["Sé conectar ideas y dar opiniones.", "Conozco have/has + participio y for/since."],
    [
        "Hacer buenas preguntas es parte de una conversación. Con have o has + participio preguntas por experiencias hasta hoy: Have they finished the project? Has she ever visited a museum? Las respuestas cortas son Yes, they have. o No, they haven't. Con How long has he...? preguntas por la duración: How long has he lived here? y la respuesta usa for o since: He has lived here for three years; He has lived here since 2022.",
        "Una hipótesis (hypothesis) es una explicación posible, que aún no está comprobada. Se apoya en pistas y se dice con Maybe... o I think... because...: Maybe it rained at night, because the streets are wet. Si hay más pistas, puedes confirmar o rechazar la hipótesis. Una buena hipótesis nombra la evidencia.",
        "En una conversación con brecha de información, cada persona sabe una parte. Para completar, haz la pregunta que encaja con el dato que falta. Si la respuesta es un tiempo (for three years), la pregunta es How long...? Si es sí o no, es una pregunta con have o has. Para elegir la pregunta, piensa primero qué clase de respuesta esperas.",
    ],
    [("Have they...?", "¿Han...?"), ("Has she ever...?", "¿Ha ella alguna vez...?"), ("How long has he...?", "¿Hace cuánto tiempo ha...?"), ("for / since", "durante / desde"), ("hypothesis", "hipótesis: explicación posible"), ("Maybe...", "Quizás...")],
    [
        ("Elegir la pregunta para una respuesta", "La respuesta es «Tom has lived in Temuco for three years». ¿Qué pregunta le corresponde? A) How long has Tom lived in Temuco? B) Where does Tom work?", ["La respuesta habla de duración: for three years.", "Para duración se pregunta How long.", "La pregunta es How long has Tom lived in Temuco?"], "A) How long has Tom lived in Temuco?"),
        ("Formular una hipótesis", "Las calles están mojadas y el cielo está oscuro. ¿Qué hipótesis apoya la evidencia? A) Maybe it rained at night, because the streets are wet. B) Maybe it is hot, because the sky is dark.", ["Tomo las pistas: calles mojadas.", "La evidencia sugiere lluvia.", "La hipótesis A es coherente."], "A) Maybe it rained at night, because the streets are wet."),
    ],
    [
        ("Hacer una pregunta con have y responder con for o since.", "No se piensa qué clase de respuesta se espera.", "Piensa primero si esperas sí o no, o un tiempo."),
        ("Presentar una hipótesis como un hecho seguro.", "Se omite Maybe o I think.", "Marca que es una posibilidad y nombra la pista."),
    ],
    [
        ("Para preguntar por la duración usas: A) How long has she lived here? B) Where is she?", "A) How long has she lived here?", "How long pregunta por el tiempo."),
        ("Para preguntar si algo ya se hizo usas: A) Have they finished? B) How long?", "A) Have they finished?", "Es una pregunta de sí o no con have."),
        ("La respuesta «Yes, she has.» corresponde a: A) Has she visited a museum? B) How long has she lived here?", "A) Has she visited a museum?", "Es una pregunta de sí o no con has."),
    ],
    [
        ("«He has lived here since 2022.» ¿Qué pregunta responde? A) How long has he lived here? B) Where does he live?", "A) How long has he lived here?", "Since 2022 es una duración."),
        ("«No, they haven't.» ¿Qué pregunta responde? A) Have they finished the project? B) How long have they worked?", "A) Have they finished the project?", "Es una respuesta corta de sí o no."),
        ("«For two weeks.» ¿Qué pregunta responde? A) How long has she studied English? B) Has she studied English?", "A) How long has she studied English?", "For two weeks es la duración."),
    ],
    [
        ("Completa: «How long ___ she studied English?» A) has B) have", "A) has", "Con she se usa has."),
        ("Completa: «___ they ever seen a whale?» A) Have B) Has", "A) Have", "Con they se usa have."),
        ("Ordena las palabras: lived / has / how long / he / here", "How long has he lived here?", "La estructura es how long + has + sujeto + participio."),
    ],
    [
        ("Compañero A: «Nora has a new pet.» Compañero B: «It is small and sleeps a lot.» ¿Qué hipótesis se apoya en ambas pistas? A) Maybe it is a cat, because it is small and sleeps a lot. B) Maybe it is a fish, because it is small.", "A) Maybe it is a cat, because it is small and sleeps a lot.", "Las pistas apoyan a un gato, no a un caballo."),
        ("A te dice «Nora has had her pet.» y no dice cuánto tiempo. ¿Qué pregunta haces para completar? A) How long has she had it? B) Where is the pet?", "A) How long has she had it?", "Pregunta por la duración."),
    ],
    [
        ("Pistas: hay migas en la mesa y el plato está vacío. ¿Qué hipótesis es mejor? A) Maybe someone ate here, because there are crumbs and an empty plate. B) Maybe someone slept here.", "A) Maybe someone ate here, because there are crumbs and an empty plate.", "Las pistas apoyan que alguien comió."),
        ("A dice «Lucía has played the piano.» B dice «For six years.» ¿Qué pregunta unió ambos datos? A) How long has Lucía played the piano? B) Has Lucía a piano?", "A) How long has Lucía played the piano?", "For six years responde a how long."),
    ],
    [("Entrevistas a un compañero sobre su pasatiempo. ¿Qué dos preguntas son adecuadas? A) Have you ever won a prize? and How long have you played? B) Where you play? and You have play?", "A) Have you ever won a prize? and How long have you played?", "Las dos están formadas correctamente con have.")],
    [
        ("En Inglés de 1.º medio (OA 7, clase 4): ¿qué pregunta busca una duración?", "How long has/have...?", "Se responde con for o since."),
        ("En Inglés de 1.º medio (OA 7, clase 4): ¿qué es una hipótesis?", "Una explicación posible apoyada en pistas, aún sin comprobar", "Se dice con Maybe o I think."),
        ("En Inglés de 1.º medio (OA 7, clase 4): ¿cómo responde un sí corto a Have they...?", "Yes, they have.", "Se repite have."),
    ],
    task("Tu compañero te cuenta (de ejemplo): «My sister has a new hobby. She has learned it for a month. She uses a camera and goes to the park.» (hobby = pasatiempo, learned = aprendió, camera = cámara). Escribe dos preguntas en inglés para saber más (una con How long has... y una con Has/Have... ever...) y una hipótesis con Maybe... because...", "How long has she taken photos? Has she ever shown her photos? Maybe her hobby is photography, because she uses a camera and goes to the park.", ["una pregunta con How long y has/have", "una pregunta de sí o no con has/have", "una hipótesis apoyada en las pistas del texto"], ["hoja con dos preguntas y una hipótesis", "lectura en voz alta"], ["formar la pregunta sin has o have", "hipótesis sin pista"], "Reconoce las preguntas bien formadas y pide nombrar la pista cuando la hipótesis no la tiene."),
    "Escribe cinco preguntas con How long y Have you ever... para hacer a tu familia o a tus amistades.",
    "Observa algo curioso en tu casa o en la calle y escribe una hipótesis con Maybe... because...",
)

# ------------------------------------------------------------------ clase 5: discusión independiente
UNI = "«Some schools require uniforms because they believe students look equal and feel part of a group. Other people say uniforms limit personal style. In a class survey, 12 of 30 students liked uniforms.» (uniforms = uniformes, require = exigen, equal = iguales, group = grupo, limit = limitan, style = estilo, survey = encuesta)"

lesson(
    OA, 5, MAT,
    "Aprenderé a participar por mi cuenta en una discusión: conectar un texto con mi vida, explicar relaciones entre ideas, dar mi opinión con razones y hacer preguntas. Sirve para conversar con confianza y respeto.",
    ["Sé conectar, relacionar ideas, opinar y preguntar.", "Conozco frases como In my opinion y How long...?"],
    [
        "En una discusión grupal (group discussion) combinas todas las habilidades. Primero, entiendes el texto y su idea principal. Luego conectas: In my school, we also.... Después explicas relaciones entre ideas con although, but, if o first-then-finally. Das tu opinión con In my opinion... because.... Y haces preguntas para invitar a otros: What do you think? Have you ever...?",
        "Escuchar al otro es parte de discutir. Puedes responder con I agree with you because..., I see your point, but... o Could you give an example? Cuando dos personas piensan distinto, ambos pueden tener razones válidas. Lo importante es usar evidencia: According to the survey... o In the text, it says.... Evita decir solo Yes o No.",
        "Para planificar tu intervención, escribe una frase de cada tipo: conexión, relación, opinión y pregunta. Luego ensaya en voz alta. Después de la discusión, revisa: ¿apoyé mi opinión?, ¿escuché a los demás?, ¿usé algún dato? Esa revisión te ayuda a mejorar en la próxima conversación.",
    ],
    [("group discussion", "discusión grupal"), ("What do you think?", "¿Qué piensas?"), ("Could you give an example?", "¿Podrías dar un ejemplo?"), ("evidence", "evidencia: datos que apoyan"), ("I agree with you because...", "estoy de acuerdo contigo porque..."), ("In the text, it says...", "En el texto dice...")],
    [
        ("Identificar cada tipo de intervención", "Frases de una discusión: (a) In my school, we have uniforms too. (b) Although uniforms are practical, they limit style. (c) In my opinion, uniforms are fair because everyone looks equal. (d) What do you think? Clasifica cada una: conexión, relación, opinión o pregunta.", ["(a) relaciona el texto con mi colegio.", "(b) opone dos ideas con although.", "(c) da una opinión con razón y (d) invita a otra persona."], "a conexión, b relación, c opinión, d pregunta"),
        ("Usar un dato", UNI + " ¿Cuántos estudiantes de la encuesta no gustaban de los uniformes?", ["Total: 30.", "Les gustaban: 12.", "No les gustaban: 30 − 12 = 18."], "18 estudiantes"),
    ],
    [
        ("Responder solo con Yes o No en una discusión.", "Se cree que basta con tomar una postura.", "Agrega because y una razón o un dato."),
        ("No escuchar y repetir una opinión ya dicha.", "La atención está en el turno propio.", "Responde a lo que dijo la otra persona con I agree o I see your point, but...."),
    ],
    [
        (UNI + " ¿Cuál es la idea principal del texto? A) hay distintas opiniones sobre los uniformes B) los uniformes son obligatorios en todos los colegios", "A) hay distintas opiniones sobre los uniformes", "El texto presenta razones a favor y en contra."),
        (UNI + " ¿Qué razón dan quienes apoyan los uniformes? A) que los estudiantes se ven iguales y sienten que pertenecen al grupo B) que son baratos", "A) que los estudiantes se ven iguales y sienten que pertenecen al grupo", "Dice students look equal and feel part of a group."),
        ("¿Qué pregunta invita a otra persona a opinar? A) What do you think? B) I think.", "A) What do you think?", "Es una pregunta abierta."),
    ],
    [
        (UNI + " ¿Qué respuesta conecta con tu vida? A) In my school, we have a uniform and I feel comfortable with it. B) The survey has thirty students.", "A) In my school, we have a uniform and I feel comfortable with it.", "Relaciona el tema con la vida personal."),
        (UNI + " ¿Qué frase explica una relación de contraste? A) Some people like uniforms, but others say they limit personal style. B) Uniforms and students.", "A) Some people like uniforms, but others say they limit personal style.", "But opone dos posturas."),
        (UNI + " ¿Qué frase atribuye el dato a la fuente? A) According to the class survey, 12 of 30 students liked uniforms. B) I believe 12 students liked uniforms.", "A) According to the class survey, 12 of 30 students liked uniforms.", "Nombra la encuesta como fuente."),
    ],
    [
        (UNI + " ¿Qué dicen quienes critican los uniformes? A) que limitan el estilo personal B) que son más caros", "A) que limitan el estilo personal", "Dice Other people say uniforms limit personal style."),
        ("Un compañero dice «I disagree» sin más. ¿Qué mejora su intervención? A) agregar because y una razón B) hablar más rápido", "A) agregar because y una razón", "Una opinión necesita apoyo."),
        ("Otro compañero responde «I see your point, but in my opinion uniforms are useful because they save time in the morning». ¿Qué estrategias usa? A) reconoce al otro, da opinión y razón B) solo repite lo que dijo el otro", "A) reconoce al otro, da opinión y razón", "Combina I see your point, In my opinion y because."),
    ],
    [
        ("Una intervención dice: «According to the survey, 12 of 30 students liked uniforms, so uniforms are bad.» ¿Qué problema tiene? A) concluye que son malos con un solo dato, que no basta B) usa mal According to", "A) concluye que son malos con un solo dato, que no basta", "Un dato parcial no justifica una conclusión tan fuerte."),
        ("Alguien dice «Uniforms limit style». ¿Qué respuesta es respetuosa y aporta? A) I agree partly, but uniforms also save time. What do you think? B) Wrong.", "A) I agree partly, but uniforms also save time. What do you think?", "Reconoce parte de la idea, agrega un argumento y pregunta."),
    ],
    [
        ("Quieres pedir más información sobre la opinión de alguien. ¿Qué frase usas? A) Could you give an example? B) I do not like it.", "A) Could you give an example?", "Pide una explicación con ejemplo."),
        arith(UNI + " Si en otra encuesta de 40 estudiantes a 15 les gustan los uniformes, ¿cuántos no? ", "40-15", "Se resta 15 al total de 40.", " estudiantes"),
    ],
    [("En tu grupo discuten si el colegio debe tener uniforme. ¿Qué intervención combina opinión, razón y pregunta? A) In my opinion, uniforms are fair because everyone looks equal. What do you think? B) Uniforms. Yes.", "A) In my opinion, uniforms are fair because everyone looks equal. What do you think?", "Incluye opinión, razón y una pregunta al grupo.")],
    [
        ("En Inglés de 1.º medio (OA 7, clase 5): ¿qué tipos de frases usas en una discusión?", "Conexión, relación entre ideas, opinión con razón y pregunta", "Cada tipo cumple una función."),
        ("En Inglés de 1.º medio (OA 7, clase 5): ¿qué dices si no estás de acuerdo con respeto?", "I see your point, but I disagree because...", "Reconoce y explica tu razón."),
        ("En Inglés de 1.º medio (OA 7, clase 5): ¿qué haces después de una discusión?", "Revisas si apoyaste tu opinión y si escuchaste a los demás", "Es la autoevaluación."),
    ],
    task("Lee este texto: «A town has built a new skate park. Young people love it, but some neighbours say it is noisy. The town says it will review the schedule in three months.» (skate park = pista de patinaje, neighbours = vecinos, noisy = ruidoso, schedule = horario, review = revisar). Prepara cuatro frases para una discusión: una conexión, una relación entre ideas con but, although o if, una opinión con In my opinion... because... y una pregunta. Léelas a una persona de tu casa.", "In my town, there is a small skate park too. Although the park is noisy, it keeps young people active. In my opinion, a schedule is a good idea because neighbours need to rest. What do you think about it?", ["la conexión se relaciona con el texto", "la relación entre ideas usa el conector correcto", "la opinión tiene razón", "la pregunta invita a otro"], ["hoja con cuatro frases", "comentario de la persona oyente"], ["opinión sin razón", "conexión sin relación con el texto"], "Reconoce cada intervención lograda y pide que apoye la opinión con un dato si no tiene razón."),
    "Subraya con cuatro colores la conexión, la relación, la opinión y la pregunta en tu intervención.",
    "Conversa con una persona de tu casa sobre otro tema y registra una opinión de cada uno con su razón.",
)
