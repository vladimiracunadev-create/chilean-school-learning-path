"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 07: reaccionar a textos con conexiones, evaluación, opinión y preguntas.

Todos los textos a los que se refiere un ejercicio están escritos en el enunciado (ficticios, originales; datos rotulados como de
ejemplo). Inglés americano. Los títulos de clase del plan son genéricos; aquí se aplican a conexiones, evaluar ideas
(true/false because), sentimientos y puntos de vista, consejos y preferencias, y preguntas e hipótesis.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 07"

# ------------------------------------------------------------------ clase 1: conexiones
CA = "«Marta's Stand (fictional). In a small town, a woman opened a stand where she sells empanadas on weekends. At first, only neighbors came. Now people from other towns visit her stand, and she has hired two helpers.» (stand = puesto, sells = vende, neighbors = vecinos, hired = contrató, helpers = ayudantes)"
CB = "«A Useful Triangle (fictional article). In math, we learn that a triangle with sides of 3, 4 and 5 units has a square corner. Builders use this idea to check that walls meet at the right angle.» (triangle = triángulo, sides = lados, units = unidades, square corner = ángulo recto, builders = constructores, walls = muros, right angle = ángulo recto)"
CC = "«A Letter from a Student in Japan (fictional). We start the school year in April, when the cherry trees bloom. Every day we clean our classroom together. We also eat lunch in the classroom.» (letter = carta, school year = año escolar, cherry trees = cerezos, bloom = florecen, clean = limpiamos, together = juntos)"
CD = "«Our Neighborhood Fair (fictional). Every year in September, our neighborhood holds a fair. Families bring food and games, and the old people tell stories.» (fair = feria, holds = realiza, games = juegos, old people = personas mayores, stories = historias)"

lesson(
    OA, 1, MAT_R,
    "Aprenderé a conectar lo que leo o escucho con otras asignaturas, con mi lengua y cultura, con mi vida diaria y con otras culturas, usando frases como I had read..., I learned that... y we usually.... Sirve para dar una reacción personal y apoyada.",
    ["Sé contar experiencias en pasado.", "Conozco usually y often."],
    [
        "Hacer una conexión (connection) es relacionar un texto con algo que ya sabes. Puede ser una conexión con otra asignatura (In math, I learned that...), con tu lengua y tu cultura (In Chile, we usually...), con tu vida diaria (I often...), con una experiencia personal (Last year, I...) o con otra cultura (In Japan, students...). Cada conexión explica qué parte del texto te hace pensar en eso.",
        "Para hablar de algo que ocurrió antes de otra cosa pasada, usa had + participio: Before we studied triangles in math, I had seen the 3-4-5 idea in my uncle's workshop. El pasado perfecto se usa cuando hay dos hechos pasados y uno ocurrió antes. Para costumbres usa usually, often y always: In my town, we usually hold a fair in September.",
        "Una buena conexión tiene tres partes: la idea del texto, lo que ya sabías y la relación entre ambos. Ejemplo: The text says that a woman sells empanadas. In Chile, we usually eat empanadas in September, so it reminds me of my culture.",
    ],
    [("connection", "conexión"), ("In math, I learned that...", "en matemática aprendí que..."), ("we usually / we often", "usualmente / a menudo"), ("I had read / seen / been", "yo había leído / visto / estado"), ("it reminds me of", "me recuerda a"), ("another culture", "otra cultura")],
    [
        ("Conectar con otra asignatura", CB + " ¿Cómo conectas este texto con Matemática?", ["El texto habla de un triángulo de lados 3, 4 y 5.", "En Matemática aprendí el teorema de Pitágoras.", "Puedo decir: In math, I learned that a triangle with sides 3, 4 and 5 has a square corner."], "In math, I learned that a triangle with sides 3, 4 and 5 has a square corner"),
        ("Conectar con la cultura", CA + " ¿Cómo conectas este texto con tu cultura?", ["El texto habla de empanadas.", "En Chile las empanadas son comida frecuente en celebraciones.", "Puedo decir: In Chile, we often eat empanadas at celebrations."], "In Chile, we often eat empanadas at celebrations"),
    ],
    [
        ("Decir una conexión sin explicar qué parte del texto la provoca.", "No se entiende por qué se conecta.", "Cita la idea del texto y luego tu conexión."),
        ("Usar had + participio sin otro hecho pasado.", "El pasado perfecto necesita un segundo hecho al que ser anterior.", "Agrega el segundo hecho: before we studied it."),
    ],
    [
        mc("¿Qué frase introduce una conexión con otra asignatura?", "In math, I learned that...", ["Thank you for coming to my talk today", "If I were you, I would tell her the truth"], "Relaciona el texto con lo aprendido en una asignatura."),
        mr(CD, "¿Qué costumbre cuenta el hablante?", "Su barrio hace una feria cada septiembre", ["Su barrio cierra todos los negocios en septiembre", "Su barrio no hace ninguna actividad en septiembre"], "Dice Every year in September, our neighborhood holds a fair."),
        mr(CC, "¿Qué hacen cada día los estudiantes de Japón del texto?", "Limpian juntos su sala", ["Salen antes de clases para ir a sus casas", "Viajan a otro país durante el mes de abril"], "Dice Every day we clean our classroom together."),
    ],
    [
        mr(CA, "¿Qué conexión personal es adecuada para este texto?", "My uncle also sells food at a market on weekends", ["I like to play soccer with my friends every Sunday", "My dog is small and he sleeps all day on the sofa"], "Se relaciona con vender comida los fines de semana."),
        mr(CC, "¿Qué conexión cultural puedes hacer con el año escolar de Japón?", "En Chile el año escolar suele empezar en marzo", ["En Chile el año escolar empieza en abril, igual que en Japón", "En Chile el año escolar empieza en octubre, al final del año"], "Compara el comienzo del año escolar en ambos países."),
        mr(CB, "¿Qué conexión con la vida diaria sirve para este texto?", "Mi tío revisa que las esquinas queden en ángulo recto al armar un mueble", ["Mi vecina compra pan fresco cada mañana en la panadería de la esquina", "Mi hermana viaja todos los días al colegio en bus con sus amigas"], "Se relaciona con ángulos rectos en construcción."),
    ],
    [
        mc("Completa con la forma correcta: Before we visited the museum, I ____ about it in a magazine.", "had read", ["have read", "was read"], "Had read marca un hecho anterior a la visita."),
        mc("Completa con la forma correcta: In my family, we ____ eat together on Sundays.", "usually", ["usual", "usually are"], "Usually va antes del verbo."),
        mr(CD, "Quieres conectar este texto con tu cultura. ¿Qué frase es más adecuada si en tu barrio también se hace una feria en septiembre?", "In my neighborhood, we also hold a fair in September", ["In my neighborhood, we never hold any kind of activity", "In my neighborhood, nobody brings food or games to a fair"], "Conecta con tu realidad cercana."),
    ],
    [
        mr(CB, "Una compañera dice «In math, I learned that every triangle has a square corner». ¿Qué falla?", "Generaliza: solo algunos triángulos tienen ángulo recto", ["Usa mal la palabra math en una oración con learned", "Olvida mencionar a los constructores del texto del artículo"], "El texto habla de un triángulo en particular, no de todos."),
        mc("Un estudiante dice «Before I visited Japan, I had visited Japan». ¿Qué problema tiene?", "Repite el mismo hecho: no hay un segundo hecho", ["Está perfecta, porque had visited siempre es correcto", "Debe ir en presente, porque Japón existe hoy todavía"], "Había dos hechos distintos: falta uno diferente."),
    ],
    [
        mr(CA + " " + CD, "Compara los dos textos. ¿Qué tienen en común?", "Ambos hablan de actividades de una comunidad con comida o juegos", ["Ambos hablan de triángulos y de cómo los usan los constructores", "Ambos hablan de un viaje de estudiantes a Japón en el mes de abril"], "Los dos muestran actividades comunitarias."),
        mr(CC, "En Japón, el año escolar comienza en abril. ¿Qué conexión hace un estudiante chileno?", "In Chile, we start school in March, after the summer vacation", ["In Chile, we start school in April, just like students do in Japan", "In Chile, we start school in July, after the long winter break"], "Compara el calendario escolar de los dos países."),
    ],
    [mc("Tienes que explicar a un adulto una conexión entre el texto de Marta y tu vida. Elige la mejor frase.", "The text says Marta sells empanadas, and my uncle also has a stand", ["Empanadas are very good food, and I like to eat them on weekends", "The text is about a woman and her stand, and I like it very much"], "Cita el texto y la conexión.")],
    [
        ("En Inglés de 2.º medio (OA 7, clase 1): ¿qué tipos de conexiones puedes hacer?", "Con otras asignaturas, con tu cultura, con tu vida diaria y con otras culturas", "Son los tipos que nombra el OA."),
        ("En Inglés de 2.º medio (OA 7, clase 1): ¿cuándo se usa had + participio?", "Cuando una acción pasada ocurrió antes de otra pasada", "Necesita dos hechos."),
        ("En Inglés de 2.º medio (OA 7, clase 1): ¿cómo se dice usualmente en inglés?", "Usually", "Se coloca antes del verbo."),
    ],
    task("Lee: «A Community Garden (fictional). Our neighborhood has a community garden. Volunteers water the plants every Saturday. Many families say it helps them eat more vegetables.» (community garden = huerto comunitario, volunteers = voluntarios, water = regar, plants = plantas, vegetables = verduras). Escribe tres conexiones en inglés: una con tu vida diaria, una con tu cultura y una con otra asignatura. Léelas a un adulto.", "In my life: I often help my grandmother with her plants. In my culture: in Chile, we usually eat salads with fresh vegetables. In science class: I learned that plants need water and sunlight.", ["escribe tres conexiones distintas", "cada una menciona una idea del texto", "usa frases de la clase"], ["tres frases en la hoja", "nota del adulto"], ["conexiones sin relación con el texto", "olvidar mencionar la idea del texto"], "Pide que explique en una frase cómo cada conexión se vincula con el texto."),
    "Escribe una conexión entre el texto de Japón y tu escuela.",
    "Cuenta a una persona de tu casa algo que leíste hoy y en qué te hizo pensar.",
)

# ------------------------------------------------------------------ clase 2: evaluar ideas e información
FA = "«Fact sheet: Riverside Public Pool (fictional). Open Monday to Saturday, from 8 a.m. to 8 p.m. Entry costs 2,500 pesos for adults and 1,500 pesos for students. Children under 6 swim free with an adult. Swim caps are required.» (fact sheet = ficha de datos, entry = entrada, swim caps = gorros de natación, required = obligatorios, free = gratis)"
FB = "«Survey (example data). Forty students answered. Favorite sport: soccer 18, volleyball 12, swimming 6, tennis 4.» (survey = encuesta, favorite = favorito)"
FC = "«Claim: The town of Alba has the best weather in the country because it is always sunny. Fact: In January, Alba had 28 sunny days and 3 cloudy days.» (claim = afirmación, fact = dato, sunny = soleado, cloudy = nublado)"
FD = "«Review (fictional). The Blue Café is cheap, small and close to the school. I went on Friday, and I waited fifteen minutes for a sandwich. The staff was kind, but the music was too loud.» (review = reseña, cheap = barato, staff = personal, kind = amable, loud = fuerte)"

lesson(
    OA, 2, MAT_R,
    "Aprenderé a evaluar ideas e información de un texto con frases como this is true/correct/false/wrong because... Sirve para decidir si una afirmación coincide con el texto y justificar la decisión con evidencia.",
    ["Sé comparar una afirmación con un texto.", "Conozco because y but."],
    [
        "Evaluar una idea es decidir si es correcta o no y explicar por qué. Para decir que algo coincide con el texto, usa This is true o This is correct y agrega because con una prueba del texto: This is true because the fact sheet says that students pay 1,500 pesos. Para decir que no coincide, usa This is false o This is wrong because...",
        "Hay tres posibles resultados: verdadero (true), falso (false) o no se puede saber (not enough information). Es verdadero si el texto lo dice o permite comprobarlo con un cálculo; es falso si el texto dice lo contrario; y no se puede saber si el texto no da el dato. Una afirmación como always sunny, con solo 28 días de sol en 31, es falsa porque hay 3 nublados. Cuidado con palabras absolutas como always, never, all y nobody: casi nunca son correctas.",
        "También puedes evaluar la calidad de la información: ¿es un dato o una opinión?, ¿hay números?, ¿viene de una fuente? Una reseña mezcla datos (waited fifteen minutes) y opiniones (the music was too loud). Marca cuál es cuál antes de evaluar.",
    ],
    [("true / correct", "verdadero / correcto"), ("false / wrong", "falso / incorrecto"), ("not enough information", "no hay información suficiente"), ("fact / opinion", "dato / opinión"), ("claim", "afirmación"), ("because", "porque, con evidencia")],
    [
        ("Evaluar con un dato", FA + " Evalúa: «Students pay 2,500 pesos.»", ["Busco el precio para estudiantes.", "Dice 1,500 pesos for students.", "Por eso la afirmación es falsa."], "Es falsa, porque los estudiantes pagan 1.500 pesos"),
        ("Detectar una palabra absoluta", FC + " Evalúa: «Alba is always sunny.»", ["Always significa siempre.", "El dato dice 28 días soleados y 3 nublados en enero.", "Hubo días nublados, así que es falso."], "Es falsa, porque en enero hubo 3 días nublados"),
    ],
    [
        ("Decir que una afirmación es verdadera porque suena lógica.", "Se ignora el texto.", "Busca la frase del texto que la confirma o la contradice."),
        ("Confundir una opinión con un dato.", "Too loud es una opinión; fifteen minutes es un dato.", "Pregunta si se puede comprobar con un número o una prueba."),
    ],
    [
        mr(FA, "Evalúa: «The pool opens on Sunday».", "Es falsa: abre de lunes a sábado", ["Es verdadera: abre todos los días", "Es verdadera: abre domingos"], "El texto dice Open Monday to Saturday."),
        mr(FA, "Evalúa: «Swim caps are required».", "Es verdadera: el texto lo dice", ["Es falsa: el texto dice que no son obligatorios", "No se puede saber: el texto no habla de gorros"], "Dice Swim caps are required."),
        mc("¿Qué palabra suele hacer que una afirmación sea falsa?", "always", ["sometimes", "often"], "Always no admite excepciones."),
    ],
    [
        mr(FB, "Evalúa: «Soccer is the most popular sport in the survey».", "Es verdadera: 18 de 40 es el mayor número", ["Es falsa: el vóleibol tiene más votos que el fútbol", "No se puede saber: falta el total de estudiantes"], "Soccer 18 es la cifra mayor."),
        mr(FD, "¿Cuál de estas frases es un dato y no una opinión?", "I waited fifteen minutes", ["The music was too loud for me", "The staff was kind to everyone"], "La espera de quince minutos se puede comprobar."),
        mr(FA, "Evalúa: «Children under 6 pay 1,500 pesos».", "Es falsa: nadan gratis con un adulto", ["Es verdadera: los niños pagan como estudiantes", "No se puede saber: el texto no menciona a niños"], "El texto dice swim free with an adult."),
    ],
    [
        arith("Según la encuesta, 18 estudiantes eligen fútbol y 12 eligen vóleibol. ¿Cuántos estudiantes eligen entre esos dos deportes?", "18+12", "Se suman los dos grupos de la encuesta.", " estudiantes"),
        mr(FB, "Evalúa: «More than half of the students chose soccer».", "Es falsa: 18 es menos que la mitad de 40", ["Es verdadera: 18 estudiantes son más de la mitad", "No se puede saber: no sabemos cuántos respondieron"], "La mitad de 40 es 20 y 18 es menor."),
        mr(FD, "Evalúa: «The Blue Café is close to the school and the music is quiet».", "Es falsa: el texto dice que la música era muy fuerte", ["Es verdadera: el texto dice que el café está cerca del colegio", "No se puede saber: el texto no habla de la música del café"], "El texto dice que the music was too loud, así que no es silenciosa."),
    ],
    [
        mr(FA, "Evalúa: «The pool is open at 9 p.m.». Un compañero dice que es verdadera porque hay luz. ¿Qué respuesta es mejor?", "Es falsa porque cierra a las 8 p.m.", ["Es verdadera porque a las 9 todavía hay gente", "No se puede saber"], "El texto dice from 7 a.m. to 8 p.m."),
        mr(FC, "Un estudiante dice «The fact proves Alba has the best weather in the country». ¿Qué responde alguien que evalúa bien?", "No prueba que sea el mejor: no compara con otros lugares", ["Prueba que es el mejor, porque casi todos los días hubo sol", "El dato es falso, porque en enero hubo tres días nublados"], "Falta comparar con otros lugares."),
    ],
    [
        mr(FB, "Evalúa: «The survey proves that all students like sports».", "No se puede afirmar: solo se preguntó por el deporte favorito", ["Es verdadera: los 40 estudiantes eligieron un deporte favorito", "Es verdadera, porque los 40 estudiantes respondieron la encuesta"], "Los datos no permiten afirmar que a todos les guste el deporte."),
        mr(FD, "Reconoce un dato y una opinión en la reseña y evalúa la afirmación «The staff was kind». ¿Qué corresponde?", "Es una opinión del autor; no se puede comprobar", ["Es un dato comprobable, porque el autor estuvo ahí", "Es falso, porque el personal del café no fue amable"], "Kind es una valoración personal."),
    ],
    [mr(FA, "Un adulto te dice: «Dos adultos y un estudiante van a la piscina. Pagan 5,000 pesos adultos más 1,500 el estudiante, es decir 6,500 pesos». Evalúa la afirmación.", "Es verdadera: 2,500 + 2,500 + 1,500 = 6,500", ["Es falsa: son 7,500 pesos en total, no 6,500", "No se puede saber: falta el precio de los adultos"], "Dos adultos pagan 5.000 y el estudiante 1.500.")],
    [
        ("En Inglés de 2.º medio (OA 7, clase 2): ¿qué frase usas para decir que una afirmación no coincide con el texto?", "This is false because...", "Se agrega la prueba."),
        ("En Inglés de 2.º medio (OA 7, clase 2): ¿qué tres resultados puede tener una evaluación?", "Verdadero, falso o no hay información suficiente", "Depende de lo que dice el texto."),
        ("En Inglés de 2.º medio (OA 7, clase 2): ¿qué palabras hacen sospechosa una afirmación?", "Always, never, all y nobody", "Son palabras absolutas."),
    ],
    task("Lee: «Notice (fictional). The school library will be closed on Thursday and Friday for painting. It will open again on Monday at 8 a.m. Please return books on Wednesday.» (notice = aviso, painting = pintura, return = devolver). Evalúa estas afirmaciones con This is true/false because...: 1) The library is open on Friday. 2) You can return books on Wednesday. 3) The library opens at 7 a.m. on Monday.", "1) This is false because the library is closed on Friday. 2) This is true because the notice says to return books on Wednesday. 3) This is false because it opens at 8 a.m., not at 7.", ["evalúa las tres afirmaciones", "usa because con evidencia", "no usa solo sí o no"], ["tres frases en la hoja", "nota del adulto"], ["decir true sin evidencia", "confundir la hora de apertura"], "Pide que reescriba una afirmación falsa para que sea verdadera."),
    "Escribe dos afirmaciones verdaderas y dos falsas sobre la ficha de la piscina.",
    "Lee una noticia corta en español, anota un dato y una opinión.",
)

# ------------------------------------------------------------------ clase 3: sentimientos, interpretaciones y puntos de vista
OP1 = "«Should movie theaters offer cheaper tickets for students? Tomás: I agree, because students have little money, and movies are a good activity. Dani: I disagree. Movie theaters also have costs, and a lower price for some people means a higher price for others.» (movie theaters = cines, offer = ofrecer, cheaper = más baratas, tickets = entradas, costs = costos, lower = más bajo)"
OP2 = "«Should the school day start with ten minutes of exercise? Pía: I believe in it. After exercise, I feel more awake. Leo: I don't believe that it works for everyone. Some students arrive late, and the time is short.» (exercise = ejercicio, awake = despierto, works = funciona, arrive = llegan, short = corto)"
OP3 = "«Poem (original): The old clock in the square / says it is always late, / but we meet beneath it / because it is our place to wait.» (clock = reloj, square = plaza, late = tarde, beneath = bajo, wait = esperar)"

lesson(
    OA, 3, MAT_R,
    "Aprenderé a expresar sentimientos, interpretaciones y puntos de vista con I agree/disagree because..., I believe that/in... y a apoyar mi opinión con razones del texto. Sirve para participar en discusiones con respeto.",
    ["Sé usar because.", "Conozco I think y in my opinion."],
    [
        "Para expresar un punto de vista (point of view), usa I agree with... because..., I disagree with... because..., I believe that... o I believe in... Después de because, agrega una razón. Una opinión sin razón es débil. También puedes usar In my opinion, To me o I feel that. Para expresar sentimientos usa I feel..., I am pleased, I am sorry about..., I am worried that...",
        "I believe that va seguido de una oración: I believe that exercise helps students. I believe in va seguido de un sustantivo o idea: I believe in respect. Para interpretar (to interpret) un texto, di qué crees que significa y con qué parte lo apoyas: I think the poem says that waiting can be a shared time, because people meet under the clock.",
        "En una discusión, escucha el punto de vista del otro antes de responder. Puedes reconocer lo que dice con I understand your point, but... y luego dar tu razón. Evita descalificar a la persona; discute la idea.",
    ],
    [("I agree / disagree with ... because", "estoy de acuerdo / en desacuerdo con ... porque"), ("I believe that...", "creo que..."), ("I believe in...", "creo en..."), ("point of view", "punto de vista"), ("I am pleased / I am sorry about", "me alegra / lamento"), ("interpret", "interpretar")],
    [
        ("Reconocer acuerdo y desacuerdo", OP1 + " ¿Quién está de acuerdo y por qué?", ["Tomás dice I agree.", "Su razón es que los estudiantes tienen poco dinero.", "Dani dice I disagree."], "Tomás está de acuerdo porque los estudiantes tienen poco dinero; Dani no lo está"),
        ("Interpretar un poema", OP3 + " ¿Qué interpretas del poema?", ["El reloj siempre llega tarde.", "Aun así, la gente se encuentra bajo él.", "Interpreto que esperar puede ser una forma de compartir."], "Que esperar puede ser un tiempo compartido, porque la gente se encuentra bajo el reloj"),
    ],
    [
        ("Decir I agree sin una razón.", "La opinión queda débil.", "Agrega because y una razón."),
        ("Confundir I believe that e I believe in.", "El primero va con una oración y el segundo con un sustantivo.", "Revisa si lo que sigue es una oración o una idea."),
    ],
    [
        mr(OP1, "¿Quién dice I disagree?", "Dani", ["Tomás", "El cine"], "Dani dice I disagree."),
        mc("Completa: I believe ____ exercise helps students.", "that", ["in", "on"], "Después de believe, una oración va con that."),
        mc("Completa: I believe ____ respect.", "in", ["that", "to"], "Believe in va con un sustantivo."),
    ],
    [
        mr(OP2, "¿Por qué Pía cree en la idea del ejercicio?", "Porque después de ejercitarse se siente más despierta", ["Porque suele llegar tarde y no alcanza a entrar a clases", "Porque tiene poco tiempo antes de entrar a clases"], "Dice After exercise, I feel more awake."),
        mr(OP2, "¿Qué duda tiene Leo?", "Que algunos llegan tarde y el tiempo es corto", ["Que nadie hace ejercicio en el colegio por la mañana", "Que el ejercicio es caro y necesita materiales"], "Dice some students arrive late, and the time is short."),
        mr(OP1, "¿Qué razón da Dani?", "Los cines también tienen costos, y un precio más bajo sube otros", ["Los estudiantes tienen mucho dinero para ir al cine", "Las películas del cine son malas para los estudiantes jóvenes"], "La razón viene después de Movie theaters also have costs."),
    ],
    [
        mc("Quieres decir que estás de acuerdo con que los cines ofrezcan entradas más baratas a estudiantes. ¿Qué frase es completa?", "I agree with the idea because students have little money", ["I agree with the idea of cheaper tickets for students", "I agree with the idea of cheaper tickets, because little money"], "Incluye acuerdo, objeto y razón."),
        mc("Quieres decir que estás en desacuerdo con respeto. ¿Qué frase usas?", "I understand your point, but I disagree because costs are high", ["You are wrong, and costs are not important", "That is silly, because nobody should care about movie theater costs"], "Reconoce el punto del otro y da una razón."),
        mc("¿Qué frase expresa un sentimiento?", "I am worried that the time is too short", ["There are twenty students in the class", "The clock is on the square near the school"], "I am worried that expresa preocupación."),
    ],
    [
        mr(OP2, "Un compañero dice «I disagree because I don't like exercise». ¿Por qué esa razón es débil?", "Porque es una preferencia personal y no habla del grupo", ["Porque tiene gramática incorrecta en la palabra because", "Porque no nombra a Pía ni responde a su opinión"], "Una razón más fuerte analiza el efecto en los estudiantes."),
        mr(OP3, "Una compañera dice que el poema trata de comida. ¿Qué respuesta es mejor?", "No: el poema habla de un reloj y de un lugar de encuentro", ["Sí: porque el poema dice square, que es una plaza donde se vende comida", "Sí: porque todo poema habla de comida y de fiestas"], "No se menciona comida; sí un reloj y una plaza."),
    ],
    [
        mr(OP1 + " " + OP2, "¿Qué punto en común tienen los dos debates?", "Una persona está a favor, otra duda, y ambas dan razones", ["Ambos hablan del mismo tema, el precio de las entradas", "Ambos terminan con una votación y un ganador claro"], "Los dos presentan argumentos opuestos."),
        mc("Escribes: «I believe in that students need more time». ¿Qué corrección haces?", "I believe that students need more time", ["I believe in students that need more time", "I believe to students need more time and money"], "Con una oración se usa believe that."),
    ],
    [mr(OP1, "Quieres responder a Dani con respeto. Elige la mejor opción.", "I understand your point, but a student price helps families", ["You don't know anything about movie theaters or about money", "Movie theaters are boring, so nobody should go there"], "Reconoce y responde con una razón.")],
    [
        ("En Inglés de 2.º medio (OA 7, clase 3): ¿qué viene después de because?", "Una razón", "Sin razón, la opinión queda débil."),
        ("En Inglés de 2.º medio (OA 7, clase 3): ¿cuál es la diferencia entre believe that y believe in?", "That va con una oración e in con un sustantivo o idea", "Son estructuras distintas."),
        ("En Inglés de 2.º medio (OA 7, clase 3): ¿qué dices para reconocer el punto de otro antes de responder?", "I understand your point, but...", "Muestra respeto al otro."),
    ],
    task("Lee: «Should students have a day for cleaning the school grounds once a month? Ana: I agree, because it teaches responsibility. Ben: I disagree, because students already have homework.» (cleaning = limpiar, grounds = patios, responsibility = responsabilidad). Escribe en inglés tu propia opinión con I believe that/in... y una razón, y responde a una de las dos personas con I understand your point, but... Preséntalo a un adulto.", "I believe that a cleaning day helps students care for the school, because they use it every day. I understand your point, Ben, but one hour a month is not much.", ["incluye I believe that o in", "da una razón con because", "responde con respeto"], ["tres oraciones en la hoja", "nota del adulto"], ["opinión sin razón", "responder con una descalificación"], "Pide que cambie su opinión por la contraria y busque una razón."),
    "Escribe tres oraciones con I agree, I disagree y I believe sobre otro tema del colegio.",
    "Habla con una persona de tu casa sobre un tema y registra en español dos razones que dio.",
)

# ------------------------------------------------------------------ clase 4: consejos y preferencias
AD1 = "«Dear Sam, I have two invitations on Saturday: my cousin's birthday and a soccer tryout. I don't want to miss either of them. What should I do? — Marco» (invitations = invitaciones, tryout = prueba para el equipo, miss = perderme)"
AD2 = "«Dear Sam, I lost a book that my friend lent me. I feel terrible. She doesn't know yet. — Lía» (lent = prestó, terrible = fatal, yet = todavía)"
AD3 = "«Dear Sam, next week I have to sing in front of the whole school. I am very nervous and my voice shakes. — Gabi» (sing = cantar, nervous = nerviosa, voice = voz, shakes = tiembla)"
PR1 = "«Would you like to see a movie or to go for a walk? I'd rather go for a walk, because the weather is nice.» (go for a walk = dar un paseo, weather = clima)"

lesson(
    OA, 4, MAT_R,
    "Aprenderé a dar consejos con If I were you, I would... y You ought to..., a expresar preferencias con I'd rather... y a ofrecer ayuda con Would you like...? Sirve para responder a problemas de otros con empatía y claridad.",
    ["Sé usar should y can.", "Conozco would you like."],
    [
        "Para aconsejar, usa If I were you, I would + verbo: If I were you, I would tell your friend the truth. Observa que se dice were, no was, aunque sea yo. También sirven You ought to + verbo y You should + verbo. Para ofrecer ayuda usa Would you like some help? o Shall I help you?",
        "Para expresar preferencia usa I'd rather + verbo: I'd rather go for a walk. La contracción I'd significa I would. Para comparar dos opciones puedes agregar than: I'd rather read than watch TV. Cuando respondes a alguien con un problema, comienza con una frase de empatía como I'm sorry to hear that o That sounds difficult, y luego da el consejo.",
        "Un buen consejo es claro, amable y posible de hacer. Explica el porqué con because: If I were you, I would practice every day, because it helps with nerves. Evita las órdenes duras como You must do it.",
    ],
    [("If I were you, I would...", "si yo fuera tú, yo..."), ("You ought to / You should", "deberías"), ("I'd rather", "preferiría"), ("Would you like...?", "¿te gustaría...?"), ("Shall I...?", "¿quieres que yo...? (ofrecer)"), ("I'm sorry to hear that", "lamento oír eso")],
    [
        ("Dar un consejo", AD2 + " ¿Qué consejo darías a Lía?", ["Primero muestro empatía.", "Luego uso If I were you.", "Digo: If I were you, I would tell her the truth and offer to buy another book."], "If I were you, I would tell her the truth and offer to buy another book"),
        ("Expresar preferencia", PR1 + " ¿Qué prefiere el hablante y por qué?", ["Hay dos opciones: película o paseo.", "Dice I'd rather go for a walk.", "La razón: el clima está agradable."], "Prefiere dar un paseo porque el clima está agradable"),
    ],
    [
        ("Decir If I was you.", "En esta estructura se usa were para todas las personas.", "Escribe If I were you."),
        ("Dar una orden dura como consejo.", "Suena poco amable.", "Usa should, ought to o If I were you."),
    ],
    [
        mc("Completa: If I ____ you, I would call him.", "were", ["was", "am"], "Se usa were."),
        mc("¿Qué significa I'd rather read than watch TV?", "Preferiría leer que ver televisión", ["Leí en lugar de ver televisión ayer", "Debo leer antes de ver televisión hoy"], "I'd rather expresa preferencia."),
        mc("¿Qué frase ofrece ayuda?", "Would you like some help?", ["I'd rather sleep all afternoon", "If I were you, I would help"], "Would you like...? ofrece ayuda."),
    ],
    [
        mr(AD3, "¿Qué problema tiene Gabi?", "Debe cantar frente a todo el colegio y está nerviosa", ["No tiene voz porque se quedó sin ánimo para cantar", "No quiere ir al colegio porque no le gustan las clases"], "Dice I am very nervous and my voice shakes."),
        mr(AD1, "¿Qué dilema tiene Marco?", "Tiene dos invitaciones el mismo sábado", ["No tiene invitaciones para el sábado próximo", "Debe elegir un libro para regalar a su primo"], "Dice I have two invitations on Saturday."),
        mr(PR1, "¿Qué le preguntan al hablante?", "Si prefiere ver una película o dar un paseo", ["Si tiene hambre y quiere comer algo ahora mismo", "Qué hora es y cuándo empieza la película"], "Dice Would you like to see a movie or to go for a walk?"),
    ],
    [
        mr(AD3, "¿Cuál es un buen consejo para Gabi?", "If I were you, I would practice with a friend", ["You must be quiet and not move on the stage", "Don't sing, because your voice shakes and it is bad"], "Es un consejo amable y posible."),
        mr(AD1, "¿Qué consejo puedes dar a Marco si la prueba es por la mañana y el cumpleaños es en la tarde?", "If I were you, I would go to the tryout first and the party later", ["If I were you, I would go nowhere on Saturday and stay home", "You must choose only the birthday and forget the tryout"], "Permite asistir a ambos."),
        mc("Quieres decir que prefieres estudiar solo, no en grupo. ¿Qué frase usas?", "I'd rather study alone", ["I would rather to study alone", "I'd rather studying alone"], "Después de I'd rather va el verbo sin to."),
    ],
    [
        mr(AD2, "Un compañero propone para Lía: «You must hide it». ¿Por qué es un mal consejo?", "Porque es una orden dura que no resuelve el problema", ["Porque es muy largo para una respuesta de consejos", "Porque no menciona a Lía ni a su amiga en la frase"], "Un consejo debe ser amable y útil."),
        mc("Un estudiante dice «If I was you, I would study». ¿Qué corriges?", "Was por were", ["Study por studying", "I por me"], "En consejos se usa If I were you."),
    ],
    [
        mr(AD3, "Responde a Gabi con empatía y consejo. Elige la mejor respuesta.", "I'm sorry to hear that. If I were you, I would breathe slowly", ["That's your problem. You ought to quit the school choir", "Don't be nervous. You must sing perfectly in front of everyone"], "Une empatía con un consejo posible."),
        mr(PR1, "Si prefieres quedarte en casa en lugar de dar un paseo, ¿qué respondes?", "I'd rather stay home", ["I'd rather to stay home", "I'd rather staying home"], "I'd rather va seguido de verbo sin to."),
    ],
    [mr(AD1 + " " + AD2, "Marco y Lía tienen problemas distintos. ¿Qué consejo en inglés sirve para los dos casos?", "If I were you, I would be honest and talk to the people involved", ["If I were you, I would ignore the problem and wait", "You must change schools, because nobody will understand you"], "Es un consejo general amable.")],
    [
        ("En Inglés de 2.º medio (OA 7, clase 4): ¿cómo se completa If I ___ you, I would...?", "were", "Siempre se usa were."),
        ("En Inglés de 2.º medio (OA 7, clase 4): ¿cómo se expresa preferencia?", "I'd rather + verbo", "I'd rather go."),
        ("En Inglés de 2.º medio (OA 7, clase 4): ¿qué frase empieza una respuesta empática?", "I'm sorry to hear that", "Muestra comprensión hacia el otro."),
    ],
    task("Lee: «Dear Sam, my friend and I had an argument and now we don't talk. I miss her, but I am shy. — Cata» (argument = discusión, miss = extraño, shy = tímida). Escribe una respuesta de tres oraciones en inglés: empatía, un consejo con If I were you y una preferencia con I'd rather. Léela a un adulto.", "I'm sorry to hear that. If I were you, I would send a short message to your friend. I'd rather talk face to face, but a message is a good first step.", ["incluye empatía", "usa If I were you correctamente", "usa I'd rather"], ["tres oraciones en la hoja", "nota del adulto"], ["decir If I was you", "dar una orden dura"], "Pide que cambie el consejo por otra opción posible."),
    "Escribe dos consejos con If I were you para un amigo que quiere mejorar su inglés.",
    "Escribe en español qué prefieres entre dos actividades de tu semana y por qué, y escribe una oración con I'd rather.",
)

# ------------------------------------------------------------------ clase 5: preguntas e hipótesis
HS1 = "«In the village of Belmar (fictional), the town clock stopped one day and nobody fixed it. People began to arrive late, but they also began to talk more in the street.» (village = aldea, villagers = aldeanos, town clock = reloj del pueblo, stopped = se detuvo, fixed = arregló, arrive = llegar, street = calle)"
HS2 = "«In a small school (fictional), the library had only one computer. Students waited in line every afternoon. Some students began to bring books from home to share.» (computer = computador, line = fila, share = compartir)"
HS3 = "«A river town (fictional) has one bridge. Last winter, the bridge closed for three days. The mayor said, We must prepare a second way to cross.» (river = río, bridge = puente, closed = cerró, mayor = alcalde, cross = cruzar)"

lesson(
    OA, 5, MAT_R,
    "Aprenderé a generar preguntas e hipótesis sobre un texto con What would they...? y What if...?, y a responder con If + pasado, would + verbo. Sirve para pensar más allá de lo que dice el texto.",
    ["Sé hacer preguntas con what y why.", "Conozco If I were you."],
    [
        "Una pregunta hipotética (hypothetical question) imagina una situación que no ocurrió. Se forma con What would...? o What if...?: What would the villagers do if the clock started again? What if the mayor fixed the clock? La respuesta usa If + pasado simple, would + verbo: If the clock started again, people would arrive on time.",
        "Para formular buenas preguntas de comprensión, usa who, what, where, when, why y how sobre el texto. Para formular hipótesis, cambia un dato del texto y piensa en la consecuencia. Una hipótesis es una posible explicación o consecuencia; puede expresarse con probably, maybe o I think that... would.",
        "No hay una única respuesta correcta en una hipótesis, pero sí hay respuestas razonables: deben relacionarse con el texto y mantener la estructura correcta. Si cambias el verbo a futuro o presente, cambia el sentido: If the clock starts, people will arrive on time es un plan real; If the clock started, people would arrive es una imaginación.",
    ],
    [("What would ... do?", "¿qué haría ...?"), ("What if...?", "¿y si...?"), ("If + past, would + verb", "estructura de la hipótesis"), ("hypothesis", "hipótesis"), ("probably / maybe", "probablemente / tal vez"), ("comprehension question", "pregunta de comprensión")],
    [
        ("Formar una pregunta hipotética", HS1 + " Formula una pregunta con What if... sobre el texto.", ["Cambio un dato: el reloj se arregla.", "Uso What if.", "Escribo: What if the mayor fixed the clock?"], "What if the mayor fixed the clock?"),
        ("Responder una hipótesis", HS2 + " Responde: What would students do if there were three computers?", ["Uso If + pasado y would.", "Con tres computadores, la fila sería más corta.", "Respondo: If there were three computers, the line would be shorter."], "If there were three computers, the line would be shorter"),
    ],
    [
        ("Decir If the clock will start, people would arrive.", "No se mezcla will con would en la misma oración.", "Usa If + pasado simple, would + verbo."),
        ("Responder una hipótesis con un dato del texto sin cambiar nada.", "No responde a la situación imaginada.", "Piensa qué cambiaría si el dato fuera distinto."),
    ],
    [
        mc("Completa: What ____ the villagers do if the clock started again?", "would", ["will", "did"], "La hipótesis usa would."),
        mc("Completa: If the clock started again, people ____ arrive on time.", "would", ["will", "are"], "La condición en pasado lleva would."),
        mc("¿Cuál es una pregunta de comprensión (no hipotética)?", "Where is Belmar?", ["What if Belmar had a bigger clock?", "What would happen if the clock started?"], "Se responde con datos del texto."),
    ],
    [
        mr(HS3, "¿Qué pregunta hipotética es adecuada?", "What would the town do if the bridge closed for a month?", ["What did the mayor say about the bridge last winter?", "Where is the bridge that closed for three days last winter?"], "Cambia la duración del cierre para imaginar consecuencias."),
        mr(HS2, "¿Qué dato del texto cambia en la pregunta What if the library had five computers?", "La cantidad de computadores", ["El nombre de la escuela donde ocurre", "El día de la semana en que van"], "Se cambia el número de computadores."),
        mr(HS1, "¿Qué ocurrió con la gente después de que el reloj se detuvo?", "Llegaron tarde y conversaron más en la calle", ["Empezaron a llegar temprano y a hablar menos", "Se fueron del pueblo porque nadie arregló el reloj"], "Dice People began to arrive late, but they also began to talk more."),
    ],
    [
        mr(HS3, "Responde: What would happen if the town had two bridges?", "If the town had two bridges, people could cross when one of them closed", ["If the town has two bridges, people can cross when one of them closes", "If the town would have two bridges, people crossed when one of them closed"], "Usa If + pasado y would o could."),
        mr(HS2, "Responde: What would students do if the library had no computers?", "If the library had no computers, students would use books", ["If the library has no computers, students will use books", "If the library had no computers, students use books at home"], "La hipótesis necesita if + pasado, would + verbo."),
        mc("Elige la oración correcta:", "What if people stopped using phones for a day?", ["What if people stop to use phones for a day?", "What if people will stopped using phones for a day?"], "What if va con pasado simple en una pregunta hipotética."),
    ],
    [
        mr(HS1, "Un compañero responde «If the clock started, people would be happy» y otro «If the clock started, people would arrive on time». ¿Cuál se apoya más en el texto?", "La segunda, porque se relaciona con llegar tarde", ["La primera, porque happy es más positivo", "Ninguna, porque las dos hipótesis dicen lo mismo del texto"], "La hipótesis debe relacionarse con las consecuencias del texto."),
        mc("Una estudiante dice «What if I was the mayor?». ¿Qué corriges?", "Was por were", ["Mayor por mayors", "What por When"], "En hipótesis se usa were."),
    ],
    [
        mr(HS3, "Formula dos preguntas sobre el texto: una de comprensión y una hipotética. ¿Cuáles son adecuadas?", "What did the mayor say? y What would happen without a second bridge?", ["Where is the town? y What if the bridge will close again?", "What is a bridge? y What would happens if there are no bridges?"], "La primera pregunta se responde con el texto; la segunda imagina una situación."),
        mr(HS1, "¿Cuál es una hipótesis razonable sobre el efecto del reloj detenido?", "Maybe people talked more because nobody hurried them", ["Maybe the clock was blue because the village painted it", "Maybe the village was in Japan, because the clock stopped"], "Se relaciona con las consecuencias del texto."),
    ],
    [mc("Lees un cuento en que una niña pierde su mochila y la encuentra un vecino. ¿Qué pregunta hipotética es adecuada?", "What would she do if nobody found her backpack?", ["Who found her backpack at the end of the story?", "Where did she lose her backpack on the way home?"], "La pregunta imagina qué habría pasado en otro caso.")],
    [
        ("En Inglés de 2.º medio (OA 7, clase 5): ¿qué estructura se usa para responder What if...?", "If + pasado simple, would + verbo", "Es la estructura de la hipótesis."),
        ("En Inglés de 2.º medio (OA 7, clase 5): ¿qué palabra expresa posibilidad: probably o never?", "Probably", "Marca una posibilidad."),
        ("En Inglés de 2.º medio (OA 7, clase 5): ¿qué verbo se usa en If I ___ you?", "were", "Se usa were."),
    ],
    task("Lee: «A school (fictional) has only twenty minutes of recess a day. Students say it is too short.» (recess = recreo, too short = demasiado corto). Escribe en inglés una pregunta de comprensión, dos preguntas hipotéticas (What if... y What would...) y una respuesta con If + pasado, would. Léelas a un adulto.", "Question: How long is recess? What if recess were forty minutes? What would students do with extra time? If recess were forty minutes, students would play more games.", ["escribe una pregunta de comprensión", "escribe dos preguntas hipotéticas", "responde con la estructura correcta"], ["cuatro frases en la hoja", "nota del adulto"], ["usar will en la hipótesis", "no relacionar con el texto"], "Pide que cambie un dato y escriba una nueva hipótesis."),
    "Escribe dos preguntas con What if sobre el texto de Belmar.",
    "Piensa en una situación de tu vida y escribe en español una pregunta ¿y si...? con su respuesta.",
)
