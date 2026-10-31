"""Cuaderno del estudiante, 6.º básico Inglés (propuesta), EN06 OA 04 (reaccionar ante lo escuchado: preferencias, sentimientos y opiniones).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan pista en español. Cada palabra o estructura nueva se explica antes de usarla.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA4 = "EN06 OA 04"
ADULT = "Un adulto lee en voz alta (tapa el guion): "


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


# ---------------------------------------------------------------- clase 1: preferencias y organizador gráfico
SPORTS = "«Sofía: I love swimming because it is relaxing. Diego: I prefer basketball. I like playing with a team. Sofía: I don't like running. It makes me tired. Diego: Me neither. I only run in games.» (relaxing = relajante, prefer = prefiero, team = equipo, makes me tired = me cansa, me neither = yo tampoco)"
SURVEY = "«We asked ten students: Which sport do you like? Six students like football, three like swimming and one likes tennis.» (asked = preguntamos, students = estudiantes)"
FOODS = "«Hello! I'm Valentina. I love pizza and I like salad. I don't like fish. I prefer juice to milk. For dessert, I like fruit better than ice cream.» (dessert = postre, fruit = fruta, better than = más que, juice = jugo)"

lesson(
    OA4, 1,
    "Los diálogos y encuestas escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a expresar preferencias sobre lo que escucho, como I like, I love, I don't like y I prefer, y a mostrarlas en un esquema. Sirve para reaccionar a un texto y decir qué te gusta más.",
    ["Sé decir I like y I don't like.", "Conozco nombres de deportes y comidas."],
    [
        "Para expresar una preferencia (preference) usas verbos que muestran cuánto te gusta algo. I love ___ (me encanta), I like ___ (me gusta), I don't like ___ (no me gusta) y I prefer ___ to ___ (prefiero ___ a ___). Después del verbo va un sustantivo o un verbo con -ing: I like swimming. Para dar una razón, agrega because: I like swimming because it is relaxing.",
        "También puedes reaccionar a lo que dice otra persona. Me too (yo también) coincide con una preferencia positiva: «I like pizza.» – «Me too.» Me neither (yo tampoco) coincide con una preferencia negativa: «I don't like fish.» – «Me neither.» Si no coincides, usas I don't (yo no) o I do (yo sí).",
        "Las preferencias se pueden representar con un esquema (diagram) o un gráfico (chart). En una encuesta con diez estudiantes, puedes dibujar una barra para cada deporte: la más alta muestra la preferencia mayoritaria. Un esquema te permite comparar resultados de un vistazo, sin repetir todas las palabras.",
    ],
    [("I love / I like", "me encanta / me gusta"), ("I don't like", "no me gusta"), ("I prefer ___ to ___", "prefiero ___ a ___"), ("Me too / Me neither", "yo también / yo tampoco"), ("because", "porque"), ("diagram / chart", "esquema / gráfico")],
    [
        ("Reaccionar a una preferencia", "Un amigo dice: «I don't like tomatoes.» (tomatoes = tomates). Tú piensas lo mismo que él. ¿Qué respondes: Me too o Me neither?", ["Su frase es negativa: I don't like.", "Yo coincido con él.", "Para coincidir con una frase negativa se usa Me neither."], "Me neither"),
        ("Dar una preferencia con razón", "Completa: «I prefer cats to dogs ___ they are quiet.» (cats = gatos, quiet = tranquilos). Opciones: because, but, and.", ["Falta la razón de la preferencia.", "Because introduce la razón.", "Lo coloco en el espacio."], "because"),
    ],
    [
        ("Decir «Me too» después de una frase negativa.", "Se confunden las dos respuestas.", "Después de I don't like, usa Me neither."),
        ("Olvidar la -ing después de like.", "Se dice I like swim.", "Con un verbo, usa -ing: I like swimming."),
    ],
    [
        (ADULT + SPORTS + " ¿Qué le encanta a Sofía? a) nadar b) correr c) jugar básquetbol", "a) nadar", "Dice I love swimming."),
        (ADULT + SPORTS + " ¿Qué prefiere Diego? a) el básquetbol b) la natación", "a) el básquetbol", "Dice I prefer basketball."),
        (ADULT + SPORTS + " ¿Qué no le gusta a Sofía? a) correr b) nadar", "a) correr", "Dice I don't like running."),
    ],
    [
        (ADULT + FOODS + " ¿Qué prefiere Valentina: jugo o leche?", "Jugo", "Dice I prefer juice to milk."),
        (ADULT + FOODS + " ¿Qué comida no le gusta?", "El pescado", "Dice I don't like fish."),
        (ADULT + SPORTS + " ¿Por qué le gusta nadar a Sofía?", "Porque es relajante", "Dice because it is relaxing."),
    ],
    [
        (ADULT + SURVEY + " ¿Cuántos estudiantes respondieron en total?", "10", "Seis más tres más uno suman diez.", "6+3+1"),
        (ADULT + SURVEY + " ¿Cuántos más prefieren fútbol que natación?", "3", "Seis menos tres da la diferencia.", "6-3"),
        (ADULT + SURVEY + " Si dibujas una barra para cada deporte, ¿cuál es la más alta? a) fútbol b) tenis", "a) fútbol", "Seis es el número mayor."),
    ],
    [
        ("Una persona dice: «I don't like cold weather.» (weather = clima). Tú sientes lo mismo. ¿Qué respondes: Me too o Me neither?", "Me neither", "Me neither coincide con una frase negativa."),
        ("Un compañero dijo «I prefer swimming to running» y la razón fue «it is relaxing». ¿Qué palabra introdujo la razón?", "because", "Con because se justifica una preferencia."),
    ],
    [
        ("Dibuja un gráfico de barras con la encuesta del texto: ¿qué altura (en número de estudiantes) tiene la barra de tenis?", "1", "Un estudiante prefiere tenis."),
        ("En la misma encuesta, ¿qué fracción de los 10 estudiantes prefiere natación: 3 de 10 o 6 de 10?", "3 de 10", "Tres estudiantes eligieron natación."),
    ],
    [(ADULT + "En la cafetería del colegio, una niña dice: «I love apples, but I don't like bananas.» (apples = manzanas, bananas = plátanos). ¿Qué fruta no le gusta?", "Los plátanos", "Dice I don't like bananas.")],
    [
        ("¿Qué significa «I prefer ___ to ___»?", "Prefiero una cosa a otra", "Compara dos opciones."),
        ("¿Qué respuesta usas para coincidir con «I like pizza»?", "Me too", "Coincide con una preferencia positiva."),
        ("En Inglés: ¿Qué palabra introduce una razón?", "because", "Because significa porque."),
    ],
    task("Lee esta encuesta: «We asked eight students: Which fruit do you like? Four like apples, three like grapes and one likes pears.» (grapes = uvas, pears = peras). Dibuja un gráfico de barras con las tres frutas. Luego escribe en inglés dos frases: una con I prefer ___ to ___ y otra con I don't like ___ because ___ , sobre tus propias preferencias.", "Barras: manzanas 4, uvas 3, peras 1. I prefer apples to pears. I don't like grapes because they are sour.", ["dibuja las tres barras con los valores correctos", "escribe una frase con I prefer ___ to ___", "escribe una frase con because"], ["hoja con el gráfico y las frases", "nota del adulto"], ["cambiar los números del gráfico", "olvidar el because"], "Reconoce el gráfico completado y ayuda a revisar que la suma de las barras sea 8."),
    "Pide a una persona de tu casa que te diga tres cosas que le gustan y responde con Me too o I don't.",
    "Haz una encuesta de cinco personas sobre su comida favorita y dibuja un gráfico.",
)

# ---------------------------------------------------------------- clase 2: sentimientos y experiencias, dramatización
LOSTCAT = "«Last night, I heard a story about a boy who lost his cat. It reminded me of my friend Pedro, who lost his cat last year. I felt sad at first, but I felt happy when the cat came back.» (heard = escuché, lost = perdió, reminded me of = me recordó, felt = sentí, at first = al comienzo)"
THANKS = "«In the United States, many families eat a big dinner on Thanksgiving Day in November. They say thanks for the good things in their lives. Many people eat turkey with their families.» (Thanksgiving Day = Día de Acción de Gracias, thanks = gracias, turkey = pavo)"
FIESTAS = "«In Chile, on September eighteenth, many people celebrate the national holidays. They eat empanadas, they dance cueca and they fly kites.» (celebrate = celebran, national holidays = fiestas patrias, fly kites = elevan volantines)"

lesson(
    OA4, 2,
    "Los textos y diálogos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a decir cómo me siento ante lo que escucho y a relacionarlo con mis experiencias y con mi propia cultura, y a representarlo con una dramatización. Sirve para conectar un texto con tu vida.",
    ["Sé decir happy, sad y tired.", "Conozco las palabras story, friend y cat."],
    [
        "Para decir cómo te sientes usa I feel ___ o I'm ___: happy (feliz), sad (triste), surprised (sorprendido), worried (preocupado), proud (orgulloso), excited (entusiasmado). Para relacionar lo que oyes con tu vida, usa frases como «It reminds me of...» (me recuerda a...), «The same happened to me...» (a mí me pasó lo mismo) o «In Chile, we...» (en Chile, nosotros...).",
        "Relacionar el texto con tu propia cultura significa comparar. Si oyes que en otro país una familia celebra con una gran comida, piensas en qué hacen tú y tus cercanos en una fiesta en Chile. Puedes decir «In my country, we eat empanadas». Así notas parecidos y diferencias sin juzgar lo que es distinto.",
        "Una dramatización (role play) es representar con el cuerpo y la voz lo escuchado. Cuando dramatizas, el tono y la cara deben coincidir con el sentimiento: I'm so happy! se dice con una sonrisa y voz alegre. I'm worried se dice con voz suave y cejas hacia arriba. Dramatizar es una forma de demostrar que entendiste cómo se sentía el personaje.",
    ],
    [("I feel ___", "me siento ___"), ("happy / sad / worried / proud / excited", "feliz / triste / preocupado / orgulloso / entusiasmado"), ("It reminds me of...", "me recuerda a..."), ("In Chile, we...", "en Chile, nosotros..."), ("role play", "dramatización"), ("the same", "lo mismo")],
    [
        ("Decir cómo me siento", ADULT + "«Tomorrow is my first day at a new school. I don't know anyone there.» (new = nuevo, anyone = a nadie). ¿Cómo se siente probablemente quien habla: worried o proud?", ["Es su primer día y no conoce a nadie.", "Esa situación causa preocupación.", "Proud sería si hubiera ganado algo."], "worried"),
        ("Relacionar con mi cultura", ADULT + FIESTAS + " ¿Qué frase relaciona el texto con la propia cultura: «In Chile, we eat empanadas on September eighteenth» o «The sky is blue»?", ["Busco una frase que hable de Chile y de la fiesta.", "La primera usa In Chile, we...", "La segunda no se relaciona con el texto."], "In Chile, we eat empanadas on September eighteenth"),
    ],
    [
        ("Pensar que si algo es diferente a mi cultura, está mal.", "Se juzga en vez de comparar.", "Observa parecidos y diferencias sin juzgar."),
        ("Dramatizar «I'm so happy» con voz triste.", "El tono no coincide con el sentimiento.", "Usa una sonrisa y una voz alegre."),
    ],
    [
        (ADULT + LOSTCAT + " ¿A quién le recordó la historia al narrador? a) a su amigo Pedro b) a su profesora", "a) a su amigo Pedro", "Dice it reminded me of my friend Pedro."),
        (ADULT + LOSTCAT + " ¿Cómo se sintió primero? a) triste b) enojado", "a) triste", "Dice I felt sad at first."),
        (ADULT + LOSTCAT + " ¿Cómo se sintió al final? a) feliz b) preocupado", "a) feliz", "Dice I felt happy when the cat came back."),
    ],
    [
        (ADULT + THANKS + " ¿Qué hacen muchas familias ese día? a) una gran cena b) un desfile de bicicletas", "a) una gran cena", "Dice a big dinner on Thanksgiving Day."),
        (ADULT + THANKS + " ¿Para qué dicen gracias las familias?", "Por las cosas buenas de su vida", "Dice they say thanks for the good things."),
        (ADULT + FIESTAS + " ¿Qué baile se menciona?", "La cueca", "Dice they dance cueca."),
    ],
    [
        ("Completa para comparar con tu cultura: «In the United States, they eat turkey. In Chile, on September eighteenth, we eat ___.» Opciones: empanadas, sushi.", "empanadas", "El texto sobre Chile menciona las empanadas."),
        ("Dramatización: la línea es «I'm so excited!» (excited = entusiasmado). ¿Qué tono usas? a) voz fuerte y sonrisa b) voz baja y triste", "a) voz fuerte y sonrisa", "Excited es un sentimiento positivo."),
        ("Dramatización: la línea es «I'm worried about the test.» (test = prueba). ¿Qué gesto usas? a) cejas hacia arriba y voz suave b) saltar de alegría", "a) cejas hacia arriba y voz suave", "El gesto coincide con preocupación."),
    ],
    [
        ("Un compañero dice sobre el texto de Acción de Gracias: «Qué raro, eso está mal». ¿Qué falta en su reacción: comparar o juzgar?", "Comparar", "Debería decir qué hacemos en Chile en vez de juzgar."),
        ("Elige una buena reacción: a) It reminds me of the national holidays in Chile. b) I don't care.", "a) It reminds me of the national holidays in Chile.", "Relaciona el texto con una experiencia propia."),
    ],
    [
        ("Ordena una mini dramatización. A) My dog is found! B) My dog is lost! C) I feel so happy!", "B, A, C", "Primero el problema, luego la solución y al final el sentimiento."),
        ("En el texto del gato, ¿cuántos sentimientos distintos se mencionan?", "2", "Se mencionan sad y happy."),
    ],
    [(ADULT + "En una conversación, tu amiga dice: «I lost my pencil case today. I feel really sad.» (pencil case = estuche, really = muy). ¿Qué respuesta muestra interés? a) Oh, no! That's sad. Can I help? b) I don't care.", "a) Oh, no! That's sad. Can I help?", "Muestra empatía y ofrece ayuda.")],
    [
        ("¿Cómo se dice «me siento feliz» en inglés?", "I feel happy", "Feel es sentir y happy es feliz."),
        ("¿Qué significa «It reminds me of...»?", "Me recuerda a...", "Conecta el texto con mi experiencia."),
        ("¿Qué es una dramatización?", "Representar con voz y cuerpo lo escuchado", "Muestra el sentimiento del personaje."),
    ],
    task("Un adulto lee dos veces este texto: «At the school party, Lucía danced with her friends. Then the music stopped, and she lost her shoe. Everyone laughed, but Lucía laughed too. In the end, she felt proud because she did not get angry.» (party = fiesta, lost = perdió, shoe = zapato, laughed = se rieron, angry = enojada). En tu hoja escribe dos frases en inglés: una con I feel ___ sobre cómo te sentirías tú, y otra con It reminds me of... Luego practica con una persona la dramatización de la frase «I feel proud».", "I feel surprised. It reminds me of a party at my school.", ["escribe una frase con I feel", "escribe una frase con It reminds me of", "dramatiza con tono acorde"], ["hoja con frases", "nota del adulto sobre la dramatización"], ["usar un sentimiento que no calza con la historia", "dramatizar con tono que no coincide"], "Reconoce la frase más cercana al texto y practica con la persona el tono de voz del sentimiento."),
    "Pide a una persona de tu casa que lea «I feel proud» de tres maneras distintas y elige cuál coincide con el sentimiento.",
    "Escribe tres frases comparando una fiesta de otro país con una de Chile, usando In Chile, we...",
)

# ---------------------------------------------------------------- clase 3: opiniones
RECESS = "«Ana: I think students need more recess because they need to play. Pablo: I disagree. Recess is long enough. Ana: Why? Pablo: Because we also need time to learn. Ana: That's true, but playing helps us learn too.» (recess = recreo, disagree = no estoy de acuerdo, long enough = suficientemente largo, true = verdad)"
ZOO = "«Mr. Reyes: In my opinion, children should read every day. Reading helps us imagine new things. Carla: I agree. I also think that reading is fun. Mr. Reyes: And it helps us write better.» (opinion = opinión, should = deberían, imagine = imaginar, helps = ayuda, better = mejor)"

lesson(
    OA4, 3,
    "Los diálogos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a expresar mi opinión sobre lo que escucho con I think..., In my opinion... y because, y a decir si estoy de acuerdo. Sirve para participar en una conversación o presentar una postura de forma ordenada.",
    ["Sé decir I like y I don't like.", "Conozco because y but."],
    [
        "Una opinión (opinion) es lo que piensas sobre algo; no es un hecho. Se introduce con I think... (creo que...), In my opinion,... (en mi opinión,...) o I believe... (creo que...). Para justificarla usa because (porque): «I think reading is important because it helps us learn». Una opinión sin razón es poco convincente.",
        "Para reaccionar a la opinión de otra persona, usa I agree (estoy de acuerdo) o I disagree (no estoy de acuerdo). También puedes decir That's true, but... (es verdad, pero...) para reconocer algo y agregar otra idea. Cuando no estés de acuerdo, hazlo con respeto: «I see your point, but I think...» (entiendo tu punto, pero creo que...).",
        "Una buena presentación oral de una opinión tiene tres partes: la opinión, la razón y un ejemplo. Por ejemplo: «In my opinion, recess is important because we need to play. For example, we run and talk with friends». Así tu audiencia entiende qué piensas y por qué lo piensas.",
    ],
    [("I think... / In my opinion...", "creo que... / en mi opinión..."), ("I agree", "estoy de acuerdo"), ("I disagree", "no estoy de acuerdo"), ("That's true, but...", "es verdad, pero..."), ("for example", "por ejemplo"), ("should", "debería")],
    [
        ("Encontrar la opinión y la razón", ADULT + "«Luis: I think summer is the best season because we can swim.» (season = estación, swim = nadar). ¿Cuál es la opinión y cuál la razón?", ["Busco I think: la opinión es que el verano es la mejor estación.", "La razón viene después de because.", "La razón es que se puede nadar."], "Opinión: el verano es la mejor estación. Razón: se puede nadar"),
        ("Estar de acuerdo o no", "Marta dice: «Dogs are better pets than fish.» (pets = mascotas, fish = peces). Tú piensas lo mismo. ¿Qué dices: I agree o I disagree?", ["Pienso lo mismo que Marta.", "Estar de acuerdo se dice I agree.", "I disagree sería lo contrario."], "I agree"),
    ],
    [
        ("Decir una opinión sin razón.", "Se olvida justificar con because.", "Agrega una razón: I think... because..."),
        ("Responder «I disagree» de forma brusca.", "Falta cortesía.", "Usa That's true, but... o I see your point, but..."),
    ],
    [
        (ADULT + RECESS + " ¿Qué opina Ana? a) que se necesita más recreo b) que no hay que jugar", "a) que se necesita más recreo", "Dice students need more recess."),
        (ADULT + RECESS + " ¿Por qué Ana quiere más recreo?", "Porque los estudiantes necesitan jugar", "Dice because they need to play."),
        (ADULT + RECESS + " ¿Qué frase usa Pablo para no estar de acuerdo? a) I disagree b) I agree", "a) I disagree", "Dice I disagree."),
    ],
    [
        (ADULT + ZOO + " ¿Qué opina el señor Reyes? a) que los niños deben leer cada día b) que los niños deben dormir más", "a) que los niños deben leer cada día", "Dice children should read every day."),
        (ADULT + ZOO + " ¿Está Carla de acuerdo con él? Responde sí o no.", "Sí", "Dice I agree."),
        (ADULT + ZOO + " ¿Qué otra razón da el señor Reyes? a) leer ayuda a escribir mejor b) leer es caro", "a) leer ayuda a escribir mejor", "Dice and it helps us write better."),
    ],
    [
        ("Completa: «I think English is useful ___ I can talk with people from other countries.» Opciones: because, but, so.", "because", "Introduce la razón de la opinión."),
        ("Ordena la presentación de una opinión. A) For example, we run with friends. B) In my opinion, recess is important. C) Because we need to play.", "B, C, A", "Va primero la opinión, luego la razón y después el ejemplo."),
        ("Una compañera dice: «I think homework is useless.» (useless = inútil). Tú no estás de acuerdo. ¿Qué respuesta es respetuosa? a) I see your point, but I think homework helps us. b) You are wrong.", "a) I see your point, but I think homework helps us.", "Reconoce la idea y expresa otra opinión."),
    ],
    [
        (ADULT + RECESS + " ¿Cuál es la última frase de Ana? a) That's true, but playing helps us learn too. b) I disagree.", "a) That's true, but playing helps us learn too.", "Reconoce el punto de Pablo y agrega otra idea."),
        ("Dos personas opinan sobre las estaciones: Camilo dice que el verano es mejor porque hay vacaciones, y Julia dice que el invierno es mejor porque hay lluvia para saltar en charcos. ¿Cuántas razones distintas hay?", "2", "Cada persona da una razón diferente."),
    ],
    [
        ("Un compañero dice: «Football is the best sport.» ¿Es un hecho o una opinión?", "Una opinión", "La mejor es una valoración personal."),
        ("Otro dice: «A football team has eleven players.» ¿Es un hecho o una opinión?", "Un hecho", "Se puede comprobar contando."),
    ],
    [(ADULT + "En un debate en clase, el profesor pregunta: «Should we have a uniform at school?» (uniform = uniforme). Un estudiante responde: «I think we should, because it is simple and we look the same.» ¿Cuál es su razón?", "Que es simple y todos se ven iguales", "La razón viene después de because.")],
    [
        ("¿Qué significa «In my opinion»?", "En mi opinión", "Introduce lo que pienso."),
        ("¿Qué dices si piensas lo mismo que otra persona?", "I agree", "Expresa que coincides con alguien."),
        ("¿Qué palabra agrega una razón?", "because", "Because significa porque."),
    ],
    task("Lee esta pregunta: «Is it better to study in the morning or in the afternoon?» (better = mejor). Prepara una mini presentación oral de 30 segundos con tres partes: una opinión (I think...), una razón (because...) y un ejemplo (for example...). Escríbela en tu hoja y luego dila en voz alta a una persona de tu casa.", "I think it is better to study in the morning because I feel fresh. For example, I understand Math faster.", ["usa I think... y una razón con because", "agrega un ejemplo con for example", "se entiende y está en orden"], ["hoja con el texto", "nota de quien escuchó"], ["no dar ninguna razón", "olvidar el ejemplo"], "Reconoce la opinión clara y ayuda a agregar la razón o el ejemplo que falte."),
    "Pide a un adulto que lea el debate del recreo y escribe si estás de acuerdo con Ana o con Pablo, con una razón.",
    "Escribe una opinión sobre tu comida favorita y justifícala con because.",
)

# ---------------------------------------------------------------- clase 4: párrafo y resumen breve
SCHOOLTRIP = "«Last Friday, Class 6A visited the science museum. First, they saw a big dinosaur skeleton. Then they did an experiment about magnets. Finally, they ate lunch in the garden. The students loved the experiment and wanted to go back.» (skeleton = esqueleto, experiment = experimento, magnets = imanes, garden = jardín, wanted = quisieron)"
VOLCANO = "«A volcano is a mountain with a hole at the top. Inside the Earth, there is very hot rock called magma. When the pressure is too high, the magma comes out through the hole. Then it is called lava. Lava is very hot, but it cools and becomes new rock.» (hole = hoyo, magma, pressure = presión, comes out = sale, lava, cools = se enfría)"

lesson(
    OA4, 4,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a escribir un párrafo o un resumen breve de lo que escucho, con la idea principal y tres datos en orden. Sirve para recordar y compartir lo que entendiste.",
    ["Sé usar first, then y finally.", "Conozco palabras como museum, lunch y lava."],
    [
        "Un resumen (summary) es una versión corta de un texto. Dice la idea principal (main idea) y algunos datos importantes, sin detalles pequeños. No incluye tu opinión; cuenta lo que dice el texto. Un párrafo (paragraph) tiene una oración principal y dos o tres oraciones de apoyo.",
        "Para escribir un resumen, sigue tres pasos. Primero, escucha y anota palabras clave. Segundo, escribe la idea principal en una oración: «Class 6A visited the science museum». Tercero, agrega dos o tres datos con palabras de orden: First, Then, Finally. Un buen resumen tiene entre tres y cuatro oraciones y puede incluir una frase de reacción al final, como «I think it was fun».",
        "Evita copiar el texto original palabra por palabra. Usa tus propias palabras y las palabras clave. Si hay números o nombres importantes, inclúyelos con exactitud. Para revisar tu resumen pregúntate: ¿dice de qué trata?, ¿incluye los datos más importantes?, ¿está en orden? Si respondes sí a las tres, está listo.",
    ],
    [("summary", "resumen"), ("main idea", "idea principal"), ("paragraph", "párrafo"), ("detail", "detalle"), ("first, then, finally", "primero, luego, finalmente"), ("in your own words", "con tus propias palabras")],
    [
        ("Idea principal", ADULT + "«Many penguins live in cold places. They have thick feathers to stay warm. They swim to find fish. Their babies stay in a group to keep safe.» (thick = gruesas, feathers = plumas, babies = crías, keep safe = mantenerse seguros). ¿Cuál es la idea principal?", ["Cada oración habla de los pingüinos.", "La primera dice dónde viven y las otras explican cómo viven.", "La idea principal: cómo viven los pingüinos."], "Cómo viven los pingüinos en lugares fríos"),
        ("Resumir con orden", "Resume el texto de los pingüinos en una oración con tus palabras: «Many penguins ___ in cold places and ___ to find fish.» Opciones: live, swim.", ["Primero el verbo para vivir: live.", "Segundo el verbo para buscar peces: swim.", "Completo el resumen."], "live ... swim"),
    ],
    [
        ("Copiar el texto casi completo en el resumen.", "No se selecciona lo importante.", "Escribe solo la idea principal y dos o tres datos."),
        ("Agregar la opinión propia como si el texto la dijera.", "Se mezcla lo que dice el texto con lo que pienso.", "Separa el resumen de tu reacción."),
    ],
    [
        (ADULT + SCHOOLTRIP + " ¿Qué visitó la clase 6A? a) el museo de ciencias b) un zoológico", "a) el museo de ciencias", "Dice visited the science museum."),
        (ADULT + SCHOOLTRIP + " ¿Qué vieron primero?", "Un esqueleto de dinosaurio", "Dice First, they saw a big dinosaur skeleton."),
        (ADULT + SCHOOLTRIP + " ¿Qué hicieron al final? a) almorzaron en el jardín b) volvieron al colegio", "a) almorzaron en el jardín", "Dice Finally, they ate lunch in the garden."),
    ],
    [
        (ADULT + SCHOOLTRIP + " ¿Cuál es el mejor resumen? a) La clase visitó un museo, vio un esqueleto, hizo un experimento y almorzó. b) La clase comió almuerzo.", "a) La clase visitó un museo, vio un esqueleto, hizo un experimento y almorzó.", "Incluye la idea principal y los datos en orden."),
        (ADULT + VOLCANO + " ¿Qué es el magma? a) roca muy caliente dentro de la Tierra b) agua muy fría", "a) roca muy caliente dentro de la Tierra", "Dice very hot rock called magma."),
        (ADULT + VOLCANO + " ¿Cómo se llama el magma cuando sale por el hoyo?", "Lava", "Dice then it is called lava."),
    ],
    [
        (ADULT + VOLCANO + " Completa el resumen: «A volcano is a mountain with a hole. Hot ___ comes out when the pressure is high.» Opciones: magma, snow.", "magma", "El magma sale cuando la presión es alta."),
        (ADULT + VOLCANO + " ¿Qué pasa con el magma cuando la presión es muy alta? a) sale por el hoyo b) se queda adentro", "a) sale por el hoyo", "Dice when the pressure is too high, the magma comes out."),
        (ADULT + VOLCANO + " ¿Qué ocurre con la lava al final? a) se enfría y se vuelve roca nueva b) desaparece", "a) se enfría y se vuelve roca nueva", "Dice it cools and becomes new rock."),
    ],
    [
        ("Un compañero escribe de la excursión: «I think the museum was boring.» ¿Es un resumen o una opinión?", "Una opinión", "El resumen cuenta hechos; este texto da su valoración."),
        ("Ordena el resumen de la excursión. A) Finally, they ate lunch. B) Class 6A visited the science museum. C) Then they did an experiment.", "B, C, A", "La idea principal va primero y los datos siguen el orden de los hechos."),
    ],
    [
        (ADULT + VOLCANO + " ¿Cuál es un buen resumen en una oración? a) A volcano is a mountain where hot magma comes out as lava and becomes new rock. b) Volcanoes are beautiful and I love them.", "a) A volcano is a mountain where hot magma comes out as lava and becomes new rock.", "Reúne la idea principal y la secuencia sin dar opinión."),
        (ADULT + VOLCANO + " ¿Cuántas oraciones tiene el texto?", "5", "Se cuentan cinco puntos finales en el texto."),
    ],
    [(ADULT + "En la clase de Historia, una profesora dice: «Long ago, people sent messages by horse. Later, they used the telegraph. Today we use phones and email.» (horse = caballo, later = más tarde, telegraph = telégrafo). ¿Cuál es la mejor idea principal? a) cómo han cambiado las formas de enviar mensajes b) cómo montar a caballo", "a) cómo han cambiado las formas de enviar mensajes", "Describe la secuencia de tres épocas.")],
    [
        ("¿Qué incluye un resumen?", "La idea principal y los datos más importantes", "Es una versión corta del texto."),
        ("¿Incluye un resumen tu opinión?", "No", "Un resumen cuenta lo que dice el texto."),
        ("¿Qué palabras ayudan a ordenar los datos?", "first, then y finally", "Marcan el orden."),
    ],
    task("Un adulto lee dos veces este texto: «Honey bees live in a hive. The queen bee lays eggs. Worker bees collect nectar from flowers and make honey. In winter, they stay inside the hive to keep warm.» (hive = colmena, queen = reina, lays eggs = pone huevos, worker = obrera, nectar = néctar, warm = calientes). Escribe un párrafo de tres oraciones en inglés o en español con la idea principal y dos datos, y una frase de reacción que empiece con I think...", "Honey bees live in a hive. The queen lays eggs and workers make honey. In winter, they stay inside. I think bees are amazing.", ["escribe la idea principal", "incluye dos datos del texto", "agrega una reacción con I think"], ["párrafo escrito", "nota del adulto"], ["copiar el texto completo", "mezclar la opinión con los datos"], "Reconoce el dato mejor escogido y ayuda a reducir una oración larga a las palabras clave."),
    "Pide a un adulto que lea el texto del volcán y escribe una oración de resumen sin mirar el texto.",
    "Resume en tres oraciones una escucha de otra asignatura, por ejemplo una explicación de tu profesor.",
)

# ---------------------------------------------------------------- clase 5: preguntas sobre el tema
BEES = "«Today I listened to a talk about honey bees. Bees live in hives. A queen bee lays eggs. Worker bees collect nectar from flowers. They make honey.» (talk = charla, hives = colmenas, queen = reina, nectar = néctar)"
SPACE = "«The Moon is about four hundred thousand kilometres from the Earth. Astronauts went there in a rocket. They walked on the Moon and took rocks back to the Earth.» (astronauts = astronautas, rocket = cohete, walked = caminaron, rocks = rocas, took back = trajeron)"

lesson(
    OA4, 5,
    "Los textos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a hacer preguntas sobre el tema que escuché con Who, What, Where, When, Why y How, y a organizar las ideas en un esquema. Sirve para demostrar interés y comprender mejor.",
    ["Sé usar What y Where.", "Conozco palabras como bees, queen y Moon."],
    [
        "Hacer preguntas es una forma de reaccionar a un texto y demostrar interés. Las palabras interrogativas son: Who (¿quién?), What (¿qué?), Where (¿dónde?), When (¿cuándo?), Why (¿por qué?) y How (¿cómo?). How many pregunta cuántos y How long pregunta cuánto dura o cuánto mide algo. Cada una pide un tipo de información distinto.",
        "Para formar una pregunta, pon la palabra interrogativa al inicio y sigue con un verbo auxiliar: What do bees eat? Where do bees live? Who lays the eggs? Fíjate en que cuando la pregunta es sobre la persona que hace la acción (Who lays eggs?), no necesitas do. Una buena pregunta se puede responder con lo que dice el texto, o te lleva a buscar más información.",
        "También puedes representar el tema con un esquema o mapa de ideas: escribe el tema en el centro y dibuja cuatro ramas con las ideas principales, por ejemplo Where, Who, What, Product (producto). En cada rama anota una palabra clave. Después, formula una pregunta por rama. El esquema te muestra qué sabes y qué te falta saber.",
    ],
    [("Who / What / Where", "quién / qué / dónde"), ("When / Why / How", "cuándo / por qué / cómo"), ("How many / How long", "cuántos / cuánto tiempo o cuánto mide"), ("question", "pregunta"), ("mind map", "mapa de ideas"), ("branch", "rama")],
    [
        ("Elegir la pregunta correcta", "La respuesta es «Worker bees collect nectar». ¿Qué pregunta le corresponde? a) What do worker bees collect? b) Where do worker bees live?", ["La respuesta habla de qué recolectan las abejas obreras.", "Esa información la pide What do... collect?", "Where preguntaría por un lugar."], "a) What do worker bees collect?"),
        ("Formar una pregunta sobre el tema", "Escribe una pregunta con Where para la oración «Bees live in hives».", ["La respuesta es un lugar: in hives.", "Uso Where al inicio.", "Pregunta: Where do bees live?"], "Where do bees live?"),
    ],
    [
        ("Usar Where cuando la respuesta es una persona.", "No se piensa en el tipo de dato que se pide.", "Who pregunta por personas; Where por lugares."),
        ("Preguntar algo que el texto no puede responder y que no lleva a buscar nada.", "Falta relación con el tema.", "Formula preguntas que se conecten con la información."),
    ],
    [
        (ADULT + BEES + " ¿Qué palabra interrogativa usarías para preguntar por un lugar? a) Where b) Who c) How many", "a) Where", "Where significa dónde."),
        (ADULT + BEES + " ¿Quién pone los huevos en la colmena? a) la reina b) las obreras", "a) la reina", "Dice a queen bee lays eggs."),
        (ADULT + BEES + " ¿Qué hacen las abejas obreras con el néctar?", "Hacen miel", "Dice they make honey."),
    ],
    [
        (ADULT + SPACE + " ¿Qué pregunta tiene como respuesta «in a rocket»? a) How did the astronauts go to the Moon? b) Who lives on the Moon?", "a) How did the astronauts go to the Moon?", "La respuesta indica el medio con el que fueron."),
        (ADULT + SPACE + " ¿Qué trajeron los astronautas de vuelta a la Tierra?", "Rocas", "Dice took rocks back to the Earth."),
        (ADULT + SPACE + " ¿A cuántos kilómetros aproximados está la Luna de la Tierra?", "400.000", "Dice about four hundred thousand kilometres."),
    ],
    [
        ("Completa la pregunta: «___ do bees live?» para la respuesta in hives. Opciones: Where, Who, Why.", "Where", "La respuesta es un lugar."),
        ("Completa la pregunta: «___ lays the eggs?» para la respuesta the queen bee. Opciones: Who, Where, When.", "Who", "La respuesta es una persona o un ser."),
        ("Completa la pregunta: «___ kilometres is the Moon from the Earth?» (kilometres = kilómetros). Opciones: How many, Where.", "How many", "Se pregunta por una cantidad."),
    ],
    [
        ("Una compañera pregunta: «Why bees make honey?». ¿Qué error tiene la pregunta? Responde con la forma correcta.", "Why do bees make honey?", "Falta el auxiliar do después de Why."),
        ("Esquema: en el centro dice «Bees» y las ramas dicen Hive, Queen, Workers, Honey. ¿Cuántas ramas tiene el esquema?", "4", "Se nombran cuatro ramas."),
    ],
    [
        ("¿Cuál es la pregunta correcta para la respuesta «Two legs» sobre un pingüino? (legs = patas) a) How many legs does a penguin have? b) How many does a penguin legs?", "a) How many legs does a penguin have?", "How many va con un sustantivo y el auxiliar does."),
        ("¿Cuál pregunta pide una razón sobre el texto «The Moon changes shape in the sky»? a) Why does the Moon change shape? b) Where does the Moon change shape?", "a) Why does the Moon change shape?", "Why pide una razón."),
    ],
    [(ADULT + "Un compañero presenta un tema: «Today I will talk about turtles. Some turtles live in the sea and some live on land. They have hard shells.» (turtles = tortugas, shells = caparazones, hard = duro). Después de su charla, quieres saber dónde viven. ¿Qué preguntas? a) Where do turtles live? b) How many shells?", "a) Where do turtles live?", "Where pregunta por el lugar.")],
    [
        ("¿Qué palabra interrogativa pide una razón?", "Why", "Why significa por qué."),
        ("¿Qué pregunta pide una cantidad?", "How many", "Se usa con cosas que se pueden contar."),
        ("¿Qué es un mapa de ideas?", "Un esquema con el tema al centro y ramas de ideas", "Organiza el tema."),
    ],
    task("Un adulto lee dos veces este texto: «Today I will talk about elephants. Elephants live in Africa and Asia. They eat grass, leaves and fruit. A baby elephant drinks milk from its mother.» (elephants = elefantes, leaves = hojas, baby = cría). Dibuja un mapa de ideas con el tema al centro y tres ramas: Where, What they eat y Baby. Luego escribe tres preguntas en inglés, una por rama.", "Where do elephants live? What do elephants eat? What does a baby elephant drink?", ["dibuja un mapa con tres ramas", "escribe tres preguntas correctas", "cada pregunta calza con su rama"], ["hoja con el mapa y las preguntas", "nota del adulto"], ["usar Where para preguntar qué comen", "olvidar el signo de interrogación"], "Reconoce las preguntas bien formadas y revisa con la persona la palabra interrogativa de cada una."),
    "Pide a un adulto que lea el texto de las abejas y formula una pregunta con cada palabra interrogativa.",
    "Escribe cinco preguntas sobre un tema que te interese, una con Who, What, Where, Why y How.",
)
