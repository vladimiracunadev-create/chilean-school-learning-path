"""Cuaderno del estudiante, 8.º básico Inglés (oficial): IN08 OA 15, escribir para informar, opinar y narrar.

Los textos en inglés son originales y breves, con glosario en español dentro del enunciado. Los conectores, la ortografía
de palabras frecuentes y la puntuación (dos puntos) se enseñan en la clase antes de usarse en un ejercicio. Los títulos de
clase del plan son genéricos: aquí cada clase trabaja un propósito (informar, opinar, narrar), los dos puntos y la
ortografía con una escritura independiente.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "IN08 OA 15"


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


# ============================================================ clase 1: escribir para informar
PEN1 = "Humboldt penguins are birds that cannot fly. They live on the coasts of Chile and Peru. They swim very well and eat small fish. They also rest on rocks near the sea."
G_PEN1 = "(penguins = pingüinos; coasts = costas; swim = nadan; small fish = peces pequeños; rest = descansan; rocks = rocas)"
SCH1 = "Our school library is a quiet place where students read and borrow books. It has a reading corner, a computer table and a shelf of comics. It is open on weekdays, but it is closed on weekends."
G_SCH1 = "(quiet = silencioso; borrow = pedir prestado; corner = rincón; shelf = estante; comics = historietas; weekends = fines de semana; weekdays = días de semana)"

lesson(
    OA, 1,
    "Los textos y las oraciones escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir un párrafo para informar con una oración principal, datos en presente simple y conectores como and, also y but. Sirve para explicar un tema de forma clara y ordenada.",
    ["Conozco el presente simple con he, she, it y they.", "Sé usar and y but."],
    [
        "Un texto para informar (to inform) presenta datos verdaderos sobre un tema. Tiene tres partes: una oración principal (topic sentence) que dice de qué trata el párrafo; varias oraciones de apoyo (supporting sentences) con datos; y una oración final (closing sentence) que cierra. Los datos se pueden comprobar: es un hecho (fact). Una opinión (opinion) dice lo que alguien piensa y no se puede comprobar: «Penguins are cute».",
        "Para informar se usa sobre todo el presente simple: «Penguins swim». Con he, she, it y con un solo animal, el verbo lleva -s: «A penguin eats fish. It lives on the coast». Con they no lleva -s: «They swim». Para unir datos usa and (y), also (también) y but (pero): «They swim very well and eat small fish. They also rest on rocks. Penguins cannot fly, but they swim».",
        "Antes de escribir, anota tres datos que sepas con seguridad y deja fuera los que no. Escribe primero la oración principal, luego los datos en orden lógico (qué es, dónde vive, qué hace) y por último la oración final. Después lee tu párrafo y comprueba que cada oración se refiera al tema. Si una oración habla de otra cosa, quítala.",
    ],
    [("inform", "informar"), ("topic sentence", "oración principal"), ("supporting sentence", "oración de apoyo"), ("fact", "hecho: se puede comprobar"), ("opinion", "opinión: lo que alguien piensa"), ("also", "también"), ("closing sentence", "oración final")],
    [
        ("Reconocer la oración principal", "Párrafo: «Our school has a garden. Students plant lettuce there. They also water the plants every day.» (garden = huerto; plant = plantan; water = riegan) ¿Cuál es la oración principal?",
         ["La oración principal presenta el tema general.", "La primera dice que el colegio tiene un huerto.", "Las otras dan datos de apoyo."], "Our school has a garden."),
        ("Separar hecho y opinión", "Oraciones: 1) «Condors live in the Andes.» 2) «Condors are the most beautiful birds.» (condors = cóndores; the most beautiful = los más hermosos) ¿Cuál es un hecho?",
         ["Un hecho se puede comprobar.", "Dónde viven los cóndores se puede comprobar.", "Más hermosas es una opinión."], "La oración 1."),
    ],
    [
        ("Escribir «A penguin eat fish».", "Con un solo animal (it) falta la -s del verbo.", "Escribe A penguin eats fish."),
        ("Mezclar opiniones en un texto informativo.", "Una opinión no se puede comprobar.", "Usa solo datos verdaderos y comprobables."),
    ],
    [
        ("La oración principal (topic sentence) dice: a) de qué trata el párrafo b) cómo termina", "a", "Presenta el tema del párrafo."),
        ("«Fact» significa: a) un hecho comprobable b) una opinión", "a", "Un hecho se puede verificar."),
        ("Elige el verbo correcto: «A penguin ___ fish.» a) eats b) eat", "a", "A penguin es singular y el verbo lleva -s."),
    ],
    [
        (f"Lee: «{PEN1}» {G_PEN1} ¿Cuál es la oración principal? a) Humboldt penguins are birds that cannot fly b) They also rest on rocks near the sea", "a", "La primera oración presenta el tema; la otra es un dato de apoyo."),
        (f"Lee: «{PEN1}» {G_PEN1} ¿Dónde viven los pingüinos de Humboldt? a) On the coasts of Chile and Peru b) In the Andes mountains", "a", "El texto dice on the coasts of Chile and Peru."),
        (f"Lee: «{PEN1}» {G_PEN1} ¿Qué conector se usa para sumar un dato en la última oración? a) also b) but", "a", "Also significa también."),
    ],
    [
        (f"Lee: «{SCH1}» {G_SCH1} Completa: «It is open on weekdays, ___ it is closed on weekends.» Opciones: but, and.", "but", "La segunda parte contrasta con la primera."),
        (f"Lee: «{SCH1}» {G_SCH1} ¿Qué oración es una opinión? a) The library is the best place in the world b) It has a computer table", "a", "The best place in the world no se puede comprobar."),
        (f"Lee: «{SCH1}» {G_SCH1} Ordena: x) It has a reading corner. y) Our school library is a quiet place. z) It is closed on weekends. Escribe las letras en el orden del párrafo.", "y, x, z", "Va primero la oración principal, luego un dato y al final el cierre."),
    ],
    [
        (f"Lee: «{PEN1}» {G_PEN1} Un compañero agrega «Penguins are cute». ¿Por qué no sirve en un texto informativo? a) Es una opinión y no se puede comprobar b) Es muy corta", "a", "Un texto informativo usa hechos comprobables."),
        (f"Lee: «{SCH1}» {G_SCH1} Se agrega «My cousin plays football on Sundays». ¿Qué problema tiene? a) No se relaciona con el tema de la biblioteca b) Le falta la -s al verbo", "a", "Las oraciones de apoyo deben hablar del tema."),
    ],
    [
        ("Un párrafo informa sobre el huemul, un ciervo de Chile: «The huemul is a deer from Chile. It lives in the mountains of the south. It eats grass and plants.» (deer = ciervo; grass = pasto) Elige la oración final que cierra bien. a) The huemul is an important animal for the country b) I have a red bike", "a", "Cierra el tema sin salirse de él."),
        ("Quieres informar sobre las abejas: «Bees live in hives. A bee ___ nectar from flowers.» Opciones: collects, collect. (hives = colmenas; nectar = néctar)", "collects", "A bee es singular y lleva -s."),
    ],
    [("La revista del colegio pide un párrafo informativo sobre el reciclaje. Un estudiante escribe cuatro oraciones: 1) We recycle paper and plastic. 2) We have blue bins in the yard. 3) Recycling is boring. 4) Students put paper in the bins every day. (bins = basureros; boring = aburrido) ¿Qué oración quitas por no ser un hecho? Escribe el número.", "3", "Is boring es una opinión; las demás son hechos.")],
    [
        ("¿Qué tres partes tiene un párrafo informativo?", "Oración principal, apoyo y cierre", "Ordenan el texto."),
        ("¿Qué conector sirve para agregar un dato: also o but?", "Also", "Also significa también."),
        ("¿Un hecho se puede comprobar? Responde sí o no.", "Sí", "Un hecho se puede verificar."),
    ],
    task("Escribe un párrafo de cuatro oraciones para informar sobre el tema «Our classroom». Datos que puedes usar: tiene una pizarra, treinta sillas (o las que tenga tu sala) y una ventana grande. Incluye una oración principal, dos datos con and o also, y una oración final. Evita opiniones. (board = pizarra; window = ventana)", "Our classroom is a bright place to learn. It has a board and many chairs. It also has a big window. We study there every day.", ["tiene oración principal y oración final", "los datos son verdaderos", "usa and o also"], ["párrafo de cuatro oraciones en la hoja"], ["escribir opiniones como si fueran hechos", "olvidar la -s en un verbo con it"], "Pide que cambie un dato por otro del mismo tema y explique por qué sigue siendo un hecho."),
    "Copia el vocabulario y escribe un hecho y una opinión sobre tu colegio.",
    "Escribe tres hechos sobre un animal de Chile que conozcas bien, con presente simple.",
)

# ============================================================ clase 2: escribir para expresar opiniones
OP2 = "In my opinion, more students should cycle to school. First, cycling is good for health because it is exercise. Also, it is fast, so students arrive on time. However, some roads are not safe, so students need a helmet and a safe route. For these reasons, I think cycling is a good idea."
G_OP2 = "(cycle = ir en bicicleta; health = salud; exercise = ejercicio; arrive on time = llegar a tiempo; roads = calles; safe = seguro; helmet = casco; route = ruta)"
OP2B = "I think students should have a reading hour every day. For example, a reading hour helps students learn new words. It also helps them relax after class. Some people say there is no time, but a short hour is enough."
G_OP2B = "(reading hour = hora de lectura; relax = relajarse; enough = suficiente)"

lesson(
    OA, 2,
    "Los textos de opinión escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir una opinión con razones, usando I think, in my opinion, because, so, also, however y for example. Sirve para defender una idea de forma clara y respetuosa.",
    ["Sé usar because, and y but.", "Conozco should para dar un consejo."],
    [
        "Una opinión (opinion) dice lo que piensas y por qué. Se introduce con expresiones como I think (creo), I believe (creo, estoy convencido), in my opinion (en mi opinión), I agree (estoy de acuerdo) y I disagree (no estoy de acuerdo). Una opinión sin razón no convence. Por eso agrega siempre una razón con because (porque) y un ejemplo con for example (por ejemplo).",
        "Un párrafo de opinión tiene tres partes: tu opinión al comienzo; dos razones, unidas con conectores como first, also, because y so (así que); y una conclusión (for these reasons…). Si quieres mostrar otro punto de vista, usa however (sin embargo) o but: «However, some roads are not safe». Esto muestra que consideras otras ideas y hace tu texto más justo.",
        "Escribe con respeto: habla de ideas y no de personas. Usa should (debería) para recomendar: «Students should wear a helmet». Prefiere I think en lugar de afirmaciones absolutas como «Everybody hates homework». Antes de entregar, comprueba que cada razón apoya tu opinión y que la conclusión repite la idea con otras palabras.",
    ],
    [("I think / I believe", "creo / creo firmemente"), ("in my opinion", "en mi opinión"), ("I agree / I disagree", "estoy de acuerdo / en desacuerdo"), ("reason", "razón"), ("for example", "por ejemplo"), ("however", "sin embargo"), ("so", "así que"), ("should", "debería")],
    [
        ("Ubicar la opinión y la razón", "Párrafo: «I think school lunches should include fruit because fruit is healthy.» (lunches = almuerzos; fruit = fruta; healthy = saludable) ¿Cuál es la opinión y cuál la razón?",
         ["La opinión viene después de I think: should include fruit.", "La razón viene después de because.", "La razón es que la fruta es saludable."], "Opinión: los almuerzos deben incluir fruta. Razón: la fruta es saludable."),
        ("Elegir el conector", "Completa: «It is cold today, ___ I wear a jacket.» Opciones: so, however. (jacket = chaqueta)",
         ["La segunda parte es el resultado de la primera.", "So introduce una consecuencia.", "However introduce un contraste."], "so"),
    ],
    [
        ("Escribir «Everybody hates homework».", "Es una generalización que no se puede probar.", "Escribe I think homework should be short."),
        ("Dar una opinión sin razón.", "No convence a quien lee.", "Agrega because y una razón."),
    ],
    [
        ("«In my opinion» significa: a) en mi opinión b) por ejemplo", "a", "Introduce lo que piensa quien escribe."),
        ("«However» se usa para: a) mostrar un contraste b) sumar un dato", "a", "However significa sin embargo."),
        ("Elige la oración con razón: a) I like winter because I can play in the snow b) I like winter", "a", "La primera da una razón con because."),
    ],
    [
        (f"Lee: «{OP2}» {G_OP2} ¿Cuál es la opinión? a) More students should cycle to school b) Roads are dangerous", "a", "El texto comienza con in my opinion para la idea principal."),
        (f"Lee: «{OP2}» {G_OP2} ¿Qué razón da para que andar en bicicleta sea bueno para la salud? a) It is exercise b) It is expensive", "a", "El texto dice because it is exercise."),
        (f"Lee: «{OP2}» {G_OP2} ¿Qué conector introduce el otro punto de vista? a) However b) Also", "a", "However muestra el contraste sobre las calles no seguras."),
    ],
    [
        (f"Lee: «{OP2B}» {G_OP2B} Completa: «___, a reading hour helps students learn new words.» Opciones: For example, However.", "For example", "La oración da un ejemplo de los beneficios."),
        (f"Lee: «{OP2B}» {G_OP2B} ¿Qué frase introduce la opinión? a) I think b) Some people say", "a", "I think presenta la idea de quien escribe."),
        (f"Lee: «{OP2B}» {G_OP2B} ¿Qué razón da el texto para que la hora de lectura sea buena? a) It helps students relax after class b) It makes classes shorter", "a", "El texto dice It also helps them relax after class."),
    ],
    [
        ("Una compañera escribe: «I disagree with long homework because students need time to rest.» ¿Está en contra o a favor de las tareas largas? Escribe en contra o a favor. (rest = descansar)", "En contra", "I disagree significa que no está de acuerdo."),
        (f"Lee: «{OP2B}» {G_OP2B} Un compañero quiere agregar «Cars are fast». ¿Por qué no sirve? a) No apoya la opinión sobre la lectura b) Es una oración muy corta", "a", "Cada razón debe apoyar la opinión principal."),
    ],
    [
        ("Compara dos oraciones. 1) «I think the park should have more trees because trees give shade.» 2) «Trees are nice and everybody likes them.» (shade = sombra) ¿Cuál es una opinión mejor escrita? Escribe 1 o 2.", "1", "La primera tiene opinión, razón con because y evita generalizar."),
        ("Texto: «I believe recess should be longer. ___, students can play and talk with friends.» ¿Qué completa mejor? a) For example b) However c) Never (recess = recreo)", "a", "Después de la opinión sigue un ejemplo con for example."),
    ],
    [("En el centro de alumnos se debate si el casino debe vender más fruta. Un estudiante escribe: «I think the school should sell more fruit because many students want a healthy snack.» (snack = colación) Otro responde: «I disagree because fruit is expensive.» ¿Qué estudiante está a favor de vender más fruta? Escribe el número: 1 para el primero, 2 para el segundo.", "1", "El primero propone vender más fruta; el segundo no está de acuerdo.")],
    [
        ("¿Qué palabra usas para introducir una razón?", "Because", "Because significa porque."),
        ("¿Qué palabra muestra un contraste: so o however?", "However", "However significa sin embargo."),
        ("¿Se debe escribir una opinión con respeto hacia las personas? Responde sí o no.", "Sí", "Se discuten las ideas, no a las personas."),
    ],
    task("Escribe un párrafo de opinión de cuatro oraciones sobre este tema: «Should students wear sports shoes to school?» (sports shoes = zapatillas deportivas). Elige tu opinión, escribe una razón con because, un ejemplo con for example y una conclusión con For these reasons.", "In my opinion, students should wear sports shoes on some days because they are comfortable. For example, they help students run in Physical Education. However, formal shoes are better for ceremonies. For these reasons, I think students need both.", ["la opinión es clara", "incluye razón con because y un ejemplo", "tiene una conclusión"], ["párrafo de cuatro oraciones en la hoja"], ["opinión sin razón", "usar generalizaciones como everybody"], "Pide que escriba una frase con However para mostrar otro punto de vista."),
    "Copia los conectores de opinión y escribe una frase con cada uno.",
    "Escribe una opinión de dos oraciones sobre el uso de la bicicleta en tu comuna, con because.",
)

# ============================================================ clase 3: escribir para narrar
NA3 = "Last Sunday, Fabian and his sister went to the market. First, they bought some fruit. Then it started to rain, so they ran to a bus stop. After that, an old man shared his umbrella. Finally, they arrived home happy."
G_NA3 = "(market = feria; fruit = fruta; started = empezó; ran = corrieron; bus stop = paradero; shared = compartió; umbrella = paraguas; arrived = llegaron)"
NB3 = "Yesterday Tomas took his dog to the park. Suddenly, the dog saw a cat and ran away. Tomas looked for him for twenty minutes. At last he found the dog under a bench."
G_NB3 = "(took = llevó; suddenly = de pronto; ran away = salió corriendo; looked for = buscó; at last = por fin; found = encontró; bench = banca)"

lesson(
    OA, 3,
    "Los textos narrativos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir una historia corta en pasado con conectores de secuencia como first, then, after that, suddenly y finally. Sirve para contar lo que pasó de forma ordenada y entretenida.",
    ["Conozco el pasado simple de verbos como went y bought.", "Sé usar first, then y finally."],
    [
        "Narrar (to narrate) es contar qué pasó. Una narración tiene personajes, un lugar y un tiempo, y los hechos en orden. Se escribe en pasado simple. Los verbos regulares terminan en -ed (started, arrived, looked). Los irregulares cambian: go → went, buy → bought, run → ran, take → took, see → saw, find → found. No son regulares, hay que aprenderlos.",
        "Para ordenar los hechos usa conectores de secuencia: first (primero), then (luego), next (después), after that (después de eso), suddenly (de pronto), at last o finally (por fin, al final). Para dar razones o resultados usa because (porque), so (así que) y but (pero): «It started to rain, so they ran». Después de first o then se suele poner coma: «First, they bought fruit».",
        "Una buena narración tiene un inicio (quién, dónde, cuándo), un desarrollo (qué pasó) y un final (cómo terminó). Antes de escribir anota los hechos en orden con palabras clave. Luego redacta cada hecho en una oración con su conector. Al terminar, lee para ver si todos los verbos están en pasado y si el orden de los hechos es lógico.",
    ],
    [("narrate", "narrar"), ("past simple", "pasado simple"), ("first / then / next", "primero / luego / después"), ("after that", "después de eso"), ("suddenly", "de pronto"), ("at last / finally", "por fin / al final"), ("went / bought / ran / took / saw / found", "fui / compré / corrí / tomé / vi / encontré")],
    [
        ("Poner los verbos en pasado", "Completa: «Yesterday I ___ (go) to the library and ___ (buy) a notebook.» Escribe los dos verbos en pasado.",
         ["Yesterday indica pasado.", "El pasado de go es went.", "El pasado de buy es bought."], "went, bought"),
        ("Ordenar con conectores", "Hechos: a) They arrived home. b) They went to the market. c) It started to rain. Usa First, Then, Finally para ordenar las letras.",
         ["Primero fueron a la feria: b.", "Luego empezó a llover: c.", "Al final llegaron a casa: a."], "b, c, a"),
    ],
    [
        ("Mezclar presente y pasado: «Yesterday Ana go to school and saw a friend».", "Yesterday pide el pasado y go queda en presente.", "Escribe Yesterday Ana went to school and saw a friend."),
        ("Usar el mismo conector en todas las oraciones.", "El texto se vuelve monótono.", "Alterna first, then, after that, suddenly y finally."),
    ],
    [
        ("Elige el pasado de «run»: a) ran b) runned", "a", "Run es irregular y cambia a ran."),
        ("Elige el pasado de «buy»: a) bought b) buyed", "a", "El pasado de buy es bought."),
        ("«Suddenly» significa: a) de pronto b) al final", "a", "Marca algo inesperado."),
    ],
    [
        (f"Lee: «{NA3}» {G_NA3} ¿Qué hicieron primero Fabian y su hermana? a) They bought some fruit b) They ran to a bus stop", "a", "La palabra First marca el primer hecho."),
        (f"Lee: «{NA3}» {G_NA3} ¿Qué pasó después de que empezó a llover? a) They ran to a bus stop b) They arrived home", "a", "Because of the rain, they ran to a bus stop."),
        (f"Lee: «{NA3}» {G_NA3} ¿Qué conector marca el último hecho? a) Finally b) First", "a", "Finally indica el final de la secuencia."),
    ],
    [
        (f"Lee: «{NB3}» {G_NB3} Completa: «The dog ___ a cat and ran away.» Opciones: saw, see.", "saw", "La acción ocurrió ayer y el pasado de see es saw."),
        (f"Lee: «{NB3}» {G_NB3} ¿Qué conector introduce un hecho inesperado? a) Suddenly b) At last", "a", "Suddenly presenta algo que pasa de repente."),
        (f"Lee: «{NB3}» {G_NB3} ¿Dónde encontró Tomas a su perro? a) Under a bench b) In a market", "a", "El texto termina con at last he found the dog under a bench."),
    ],
    [
        (f"Lee: «{NB3}» {G_NB3} Un compañero cambia el primer verbo a «takes». ¿Qué corrección haces? a) took, porque el relato está en pasado b) takes está bien", "a", "Yesterday indica pasado y el pasado de take es took."),
        (f"Lee: «{NA3}» {G_NA3} Un compañero dice que la oración «It started to rain, so they ran» da una razón. ¿Qué expresa so? a) El resultado de la lluvia b) El inicio de la historia", "a", "So une una causa con su consecuencia."),
    ],
    [
        ("Escribe en orden con conectores estas oraciones: x) He ate lunch. y) He woke up at seven. z) He went to school. ¿Qué orden usarías para First, Then, Finally? Escribe las letras en orden.", "y, z, x", "Despertar, ir al colegio y almorzar tiene una secuencia lógica."),
        ("Mini relato de ejemplo: «Last Friday, Camila ___ (see) a rainbow on her way home. She ___ (take) a photo and ___ (run) to show it to her mother.» Escribe los tres verbos en pasado, en orden. (rainbow = arcoíris)", "saw, took, ran", "Los tres verbos son irregulares y el relato es del pasado."),
    ],
    [("En un concurso de relatos del colegio, una compañera empieza así: «Last winter, my grandfather ___ (take) me to the lake. First, we ___ (find) a small boat.» (lake = lago; boat = bote) Escribe los dos verbos en pasado, en orden, para completar el comienzo.", "took, found", "Take pasa a took y find pasa a found.")],
    [
        ("¿Qué tiempo verbal se usa para narrar hechos terminados?", "Pasado simple", "Narrar cuenta hechos que ya ocurrieron."),
        ("En Inglés (oficial): ¿Cuál es el pasado de «go»?", "Went", "Es un verbo irregular y cambia por completo."),
        ("¿Qué conector sirve para cerrar una historia: finally o first?", "Finally", "Finally marca el último hecho."),
    ],
    task("Escribe una historia de cinco oraciones usando este plan: Personaje: Daniela. Lugar: la plaza de tu barrio. Hechos: perdió su bufanda, la buscó y un vecino la encontró. Usa First, Then, Suddenly, After that y Finally, y verbos en pasado. (bufanda = scarf; vecino = neighbour)", "First, Daniela went to the square with her friends. Then she lost her scarf. Suddenly, she looked on the bench and could not find it. After that, a neighbour asked about it. Finally, the neighbour found the scarf near the fountain.", ["usa los cinco conectores", "todos los verbos están en pasado", "la secuencia es lógica"], ["historia de cinco oraciones en la hoja"], ["mezclar presente y pasado", "repetir el mismo conector"], "Pide que cambie el final por otro y que ajuste el conector si hace falta."),
    "Copia los verbos irregulares de la clase en una tabla con su pasado.",
    "Cuenta en cuatro oraciones lo que hiciste ayer, con First, Then y Finally.",
)

# ============================================================ clase 4: dos puntos y puntuación (brecha de información)
CA4 = "Tarjeta A. Ema packs three things for her hike: a jacket, a bottle of water and sandwiches."
CB4 = "Tarjeta B. Ema visits the hills of her town on Saturday at 9:30."
G_CAB4 = "(packs = guarda en la mochila; hike = caminata; hills = cerros; town = pueblo)"
RL4 = "There is one rule in our class: be kind to each other."

lesson(
    OA, 4,
    "Las oraciones y las tarjetas escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a usar los dos puntos (:) para introducir una lista o una explicación y para escribir la hora, y a repasar la puntuación básica. Sirve para escribir textos claros y bien presentados.",
    ["Sé usar punto, coma y signo de interrogación.", "Sé decir la hora en inglés."],
    [
        "Los dos puntos (colon, :) se usan en inglés en tres casos. Uno: antes de una lista, después de una oración completa. «Ema packs three things: a jacket, a bottle and sandwiches.» Dos: antes de una explicación o un ejemplo, también después de una oración completa. «There is one rule: be kind.» Tres: entre la hora y los minutos. «The class starts at 9:30.»",
        "Después de los dos puntos de una lista, los elementos se separan con comas y el último se une con and: «a jacket, a bottle of water and sandwiches». No se escriben dos puntos justo después de un verbo como is, are o need, ni después de such as. Mal: «My favourite colours are: red and blue». Bien: «My favourite colours are red and blue» o «I have two favourite colours: red and blue».",
        "Repasa la otra puntuación. El punto (.) cierra una oración. La coma (,) separa los elementos de una lista y va después de First o Then. El signo de interrogación (?) cierra una pregunta. El signo de exclamación (!) muestra sorpresa o fuerza. En inglés no se usan signos de apertura (¿ ¡). Cada oración empieza con mayúscula.",
    ],
    [("colon", "dos puntos (:)"), ("comma", "coma (,)"), ("full stop", "punto (.)"), ("question mark", "signo de interrogación"), ("exclamation mark", "signo de exclamación"), ("list", "lista"), ("rule", "regla")],
    [
        ("Poner los dos puntos antes de una lista", "Oración sin puntuación: «Ana buys three fruits apples pears and grapes». Escribe la oración con los dos puntos y las comas. (grapes = uvas; pears = peras)",
         ["Primero va una oración completa: Ana buys three fruits.", "Luego los dos puntos y la lista.", "Los elementos se separan con comas; and va antes del último."], "Ana buys three fruits: apples, pears and grapes."),
        ("Escribir la hora", "Quieres escribir que la clase de Inglés empieza a las nueve y media. ¿Cómo escribes la hora con dígitos?",
         ["La hora y los minutos se separan con dos puntos.", "Nueve y media son 9 y 30 minutos.", "Se escribe 9:30."], "9:30"),
    ],
    [
        ("Escribir «My favourite colours are: red and blue».", "No se ponen dos puntos justo después de are.", "Escribe My favourite colours are red and blue."),
        ("Escribir la hora con coma o punto: «at 9,30».", "En inglés se usan los dos puntos para la hora.", "Escribe at 9:30."),
    ],
    [
        ("Los dos puntos en inglés se llaman: a) colon b) comma", "a", "Colon es el nombre de los dos puntos."),
        ("Elige la hora bien escrita: a) 4:15 b) 4,15", "a", "La hora usa dos puntos."),
        ("En inglés, ¿cómo se abre una pregunta? a) Solo se cierra con ? b) Con ¿ al inicio", "a", "El inglés no usa el signo de apertura."),
    ],
    [
        (f"Lee: {RL4} ¿Qué introducen los dos puntos en esta oración? a) Una explicación de la regla b) Una hora", "a", "Después de los dos puntos viene la explicación: be kind to each other."),
        (f"Lee: {CA4} {G_CAB4} ¿Qué se enumera después de los dos puntos? a) The things Ema packs b) The hills", "a", "La lista es la de lo que Ema guarda en la mochila."),
        (f"Lee: {CB4} {G_CAB4} ¿A qué hora visita los cerros? a) 9:30 b) 9:03", "a", "La tarjeta dice 9:30."),
    ],
    [
        ("Elige la oración con dos puntos bien usados: a) We need three things: paper, glue and pencils b) We need: three things paper glue and pencils", "a", "Los dos puntos van después de una oración completa."),
        ("Elige la oración correcta: a) My favourite fruits are mango and kiwi b) My favourite fruits are: mango and kiwi", "a", "No se escriben dos puntos justo después de are."),
        ("Completa con la puntuación correcta: «The bus arrives at 7___45» Opciones: :, ,", ":", "La hora usa dos puntos entre horas y minutos."),
    ],
    [
        (f"{CA4} {CB4} {G_CAB4} Une las dos tarjetas. ¿Qué oración es correcta? a) Ema visits the hills on Saturday at 9:30 and packs three things: a jacket, a bottle of water and sandwiches b) Ema visits the hills on Saturday at 9,30 and packs: three things a jacket a bottle of water sandwiches", "a", "Usa 9:30 y dos puntos después de una oración completa."),
        ("Un compañero escribió: «We need: paper, glue and scissors.» ¿Qué corrección haces? a) We need paper, glue and scissors (sin dos puntos después de need) b) We need: paper, glue and scissors (sin cambios)", "a", "No se ponen dos puntos justo después de un verbo como need."),
    ],
    [
        (f"{CA4} {CB4} {G_CAB4} Tu compañero A tiene la tarjeta A y tú la B. Él pregunta: ¿cuándo va Ema a los cerros? ¿Qué respondes, con la puntuación correcta? a) On Saturday at 9:30 b) On Sunday at 3:30", "a", "La tarjeta B dice Saturday at 9:30."),
        ("Escribe la puntuación correcta en esta oración: «First put the paper on the table then draw a border» ¿Qué cambio es necesario? a) Una coma después de First b) Dos puntos después de First", "a", "Después de First se escribe coma."),
    ],
    [("Un cartel del casino dice: «Remember the three rules wash your hands eat sitting down and clean your table». (wash = lava; clean = limpia) ¿Dónde va el signo de dos puntos? a) Después de rules b) Después de table", "a", "Va después de la oración completa que introduce la lista.")],
    [
        ("¿Cómo se escribe en inglés cuatro y quince: 4,15 o 4:15?", "4:15", "La hora usa dos puntos."),
        ("¿Se puede escribir dos puntos justo después de are?", "No", "Los dos puntos van después de una oración completa."),
        ("¿Qué signo cierra una pregunta en inglés: ? o ¿?", "?", "No se usa signo de apertura."),
    ],
    task("Escribe en tu hoja tres oraciones usando dos puntos: una con una lista de tres cosas que llevas al colegio, una con una explicación (por ejemplo, una regla de tu sala) y una con una hora de actividad (por ejemplo, 8:15). Revisa que después de los dos puntos de la lista haya comas y and.", "I bring three things to school: a notebook, a pencil case and a bottle. We have one rule: listen to each other. The first class starts at 8:15.", ["la oración de lista y la de explicación llevan dos puntos después de una oración completa", "la hora usa dos puntos", "la lista tiene comas y and"], ["tres oraciones en la hoja"], ["poner dos puntos justo después de un verbo", "escribir la hora con coma"], "Pide que intercambie sus oraciones con otra persona para detectar un error de puntuación."),
    "Copia los usos de los dos puntos y escribe un ejemplo con cada uno.",
    "Escribe la hora de tres actividades de tu día en inglés, con dos puntos.",
)

# ============================================================ clase 5: ortografía de palabras frecuentes y escritura independiente
SP5 = "Yesterday my freind and I wen to the park. We saw a beautifull bird. There was many peple. Tomorow we will go again becuase it was fun."
G_SP5 = "(friend = amigo; beautiful = hermoso; people = personas; tomorrow = mañana; because = porque)"

lesson(
    OA, 5,
    "El texto y la lista de palabras escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir bien palabras muy frecuentes y a escribir un texto por mi cuenta para informar, opinar o narrar. Sirve para cuidar la ortografía y mostrar lo que sé.",
    ["Conozco los conectores because, so, but y also.", "Sé usar dos puntos y comas."],
    [
        "La ortografía (spelling) es escribir las palabras correctamente. Hay palabras muy frecuentes que conviene memorizar: because, friend, people, beautiful, different, tomorrow, usually, which. Una regla útil: i antes de e, salvo después de c (friend, receive). Tiene excepciones, como their y neighbour: apréndelas de memoria. Algunas palabras tienen letras que no se pronuncian, como people o friend. Copia la palabra, tápala y escríbela de memoria varias veces.",
        "Hay palabras que suenan parecido y se escriben distinto (homófonos). Their (de ellos) y there (allí, y en there is / there are) no son iguales: «Their house is big. There is a dog in the garden». To (hacia), too (también, demasiado) y two (dos) tampoco: «I want to go too. We have two tickets». El corrector del procesador de textos no detecta estos errores: debes revisarlos tú. También cuida el apóstrofo: it's significa it is.",
        "Para escribir de forma independiente, elige un propósito: informar (hechos en presente), opinar (I think… because…) o narrar (pasado y conectores de secuencia). Planifica, escribe, revisa y edita con tu lista: oración principal, conectores, verbos, dos puntos, mayúsculas y ortografía. Si dudas de una palabra, búscala en un diccionario o pregunta. Un texto correcto es un texto que revisaste.",
    ],
    [("spelling", "ortografía"), ("because", "porque"), ("friend", "amigo"), ("people", "personas"), ("beautiful", "hermoso"), ("tomorrow", "mañana"), ("their / there", "de ellos / allí"), ("to / too / two", "hacia / también / dos")],
    [
        ("Corregir una palabra mal escrita", "Palabra: «freind». Escríbela bien.",
         ["La regla dice i antes de e.", "No viene después de c.", "Se escribe friend."], "friend"),
        ("Elegir entre their y there", "Completa: «___ is a cat on the roof.» Opciones: There, Their. (roof = techo)",
         ["Es una oración con la estructura there is.", "Their significa de ellos y no cabe.", "Se usa There."], "There"),
    ],
    [
        ("Escribir «becuase» o «peple».", "Se omite o se cambia una letra.", "Escribe because y people, copiándolas de memoria varias veces."),
        ("Confiar solo en el corrector para their y there.", "El corrector no sabe cuál significado quieres.", "Revisa tú el sentido de la oración."),
    ],
    [
        ("Elige la palabra bien escrita: a) beautiful b) beautifull", "a", "Beautiful termina en -ful con una sola l."),
        ("Elige la palabra bien escrita: a) people b) peple", "a", "People lleva una o antes de la p."),
        ("«Two» significa: a) dos b) también", "a", "Two es el número 2; too significa también."),
    ],
    [
        (f"Lee: «{SP5}» {G_SP5} ¿Cómo se escribe bien «tomorow»? a) tomorrow b) tomorow", "a", "Tomorrow se escribe con dos r."),
        (f"Lee: «{SP5}» {G_SP5} ¿Cómo se escribe bien «becuase»? a) because b) becuase", "a", "Because comienza con be y sigue con cause."),
        (f"Lee: «{SP5}» {G_SP5} ¿Qué palabra está mal escrita en la primera oración? a) freind b) park", "a", "Friend se escribe con ie."),
    ],
    [
        ("Completa: «I want to go ___.» Opciones: too, two. (también)", "too", "Too significa también."),
        ("Completa: «We have ___ tickets.» Opciones: two, too.", "two", "Es el número 2."),
        ("Completa: «The students put ___ books on the shelf.» Opciones: their, there.", "their", "Los libros pertenecen a los estudiantes."),
    ],
    [
        (f"Lee: «{SP5}» {G_SP5} El corrector subraya «peple». ¿Qué corrección aceptas? a) people b) pople", "a", "People es la forma correcta."),
        ("Un corrector básico no subraya nada en «Its a nice day.», pero hay un error. ¿Cuál? a) Falta el apóstrofo: It's b) Falta un punto", "a", "It's significa it is."),
    ],
    [
        ("Mini texto de opinión de ejemplo: «I think we should recycle becuase it helps the planet.» ¿Qué palabra corriges? a) because b) planet", "a", "Becuase es un error de ortografía; la forma correcta es because."),
        ("Mini texto de narración: «Yesterday I wen to school. Then I saw my friend.» (went) ¿Qué palabra corriges y cómo queda? Escribe la palabra corregida.", "went", "Wen está incompleto; el pasado de go es went."),
    ],
    [("Un grupo del curso escribe en el diario mural: «Thier favourite game is football becuase it is fun.» Hay dos errores de ortografía de palabras frecuentes. ¿Cuántos errores hay en total entre thier y becuase? Escribe el número.", "2", "Thier debe ser their y becuase debe ser because.")],
    [
        ("¿Qué regla ayuda a escribir friend y receive?", "I antes de e, salvo después de c", "Resume una regla frecuente."),
        ("¿Cuál se usa con there is: there o their?", "There", "There is significa hay."),
        ("¿Quién revisa los homófonos como their y there: el corrector o tú?", "Tú", "El corrector no detecta ese tipo de error."),
    ],
    task("Elige un propósito (informar, opinar o narrar) y escribe en tu hoja un texto de cinco oraciones sobre «My weekend» (mi fin de semana). Usa al menos dos conectores, una oración con dos puntos y cinco palabras frecuentes bien escritas de la lista: because, friend, people, beautiful, tomorrow, different. Revisa con una lista de ortografía.", "Last Saturday I went to the park with my friend. First, we saw many people: families, dogs and children. Then we ate a sandwich because we were hungry. After that, we looked at a beautiful tree. Finally, we went home at 6:30, and tomorrow we will play a different game.", ["elige un propósito y lo cumple", "usa conectores y dos puntos", "cinco palabras frecuentes bien escritas"], ["texto de cinco oraciones revisado en la hoja"], ["olvidar el pasado en una narración", "escribir mal because o people"], "Pide que subraye cada palabra de la lista y compruebe su ortografía con un diccionario."),
    "Copia las ocho palabras del vocabulario cuatro veces cada una: mira, tapa, escribe y compara.",
    "Escribe tres oraciones con their, there y too, sin repetir las del cuaderno.",
)
