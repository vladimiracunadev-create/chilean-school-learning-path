"""Cuaderno del estudiante, 1.º medio Inglés (propuesta), EN1M OA 06 (estrategias de lectura antes, durante y después del texto).

Los textos son originales y están escritos en el enunciado, con pista en español.
"""
from __future__ import annotations

from student_content_en_m1_a import lesson
from student_content_ma01_b import task
from student_lessons import arith

OA6 = "EN1M OA 06"
MATR = "Los textos escritos en cada ejercicio; lápiz, resaltador o lápices de colores y hoja."

# ================================================================ OA 06 · clase 1: antes de leer
BEE = "Título: «Why Dark Skies Matter». Subtítulo: «Seeing the stars in northern Chile». Texto: «In the north of Chile the night sky is very clear and dark. Astronomers use big telescopes there to study stars and planets. Visitors also travel to the desert to look at the stars. Some towns turn off extra lights so that the sky stays dark. Dark skies are in danger because of city lights and the growth of towns.» (dark = oscuro, sky = cielo, astronomers = astrónomos, telescopes = telescopios, study = estudiar, turn off = apagar, extra = sobrantes, danger = peligro, growth = crecimiento)"

lesson(
    OA6, 1, MATR,
    "Aprenderé a prepararme antes de leer: fijar un propósito, hacer predicciones con el título y el subtítulo y usar lo que ya sé. Sirve para leer más rápido y entender mejor un texto en inglés.",
    ["Sé que el título resume el tema.", "Sé leer palabras que se parecen al español."],
    [
        "Leer bien empieza antes de la primera línea. Primero fija un propósito de lectura (reading purpose): ¿para qué leo? Puedes leer para saber por qué algo está en peligro, para hacer una tarea o para elegir un libro. El propósito decide qué buscar: si quieres saber las causas del peligro, buscarás palabras como danger o because.",
        "Luego haz una predicción (prediction): imagina qué tratará el texto usando el título, el subtítulo, las imágenes y los datos de la portada. «Why Dark Skies Matter» sugiere un texto que explica por qué importan los cielos oscuros. «Seeing the stars in northern Chile» precisa el lugar y el tema: observar las estrellas en el norte del país. Tu predicción puede ser parcial o equivocada; lo importante es comprobarla después.",
        "También activa tus conocimientos previos: lo que ya sabes de la noche en el campo o en el desierto (se ven más estrellas lejos de la ciudad) te ayuda a entender el vocabulario. Cuando lees, compara lo que sabías con lo nuevo. Esas tres acciones (propósito, predicción y conocimientos previos) forman la pre lectura (pre-reading).",
    ],
    [("reading purpose", "propósito de lectura: para qué leo"), ("prediction", "predicción: lo que imagino que dirá el texto"), ("prior knowledge", "conocimientos previos"), ("title", "título"), ("subtitle", "subtítulo"), ("pre-reading", "pre lectura: lo que hago antes de leer")],
    [
        ("Predecir con el título", "Lees solo el título «Why Dark Skies Matter» y el subtítulo «Seeing the stars in northern Chile». ¿De qué crees que tratará el texto?", ["El título habla de dark skies y matter (importar).", "El subtítulo habla de ver las estrellas en el norte de Chile.", "Predigo que explica por qué importa mantener oscuro el cielo."], "De por qué importan los cielos oscuros para ver las estrellas en el norte de Chile"),
        ("Propósito de lectura", BEE + " Quieres saber por qué los cielos oscuros están en peligro. ¿Qué palabras buscas?", ["Mi propósito son las causas del peligro.", "Busco danger y because.", "Las encuentro en la última oración."], "Danger, because, city lights y growth of towns"),
    ],
    [
        ("Leer sin fijar un propósito.", "Se lee todo igual, sin saber qué buscar.", "Antes de leer, escribe para qué lees."),
        ("Pensar que una predicción equivocada es un fracaso.", "Se cree que la hipótesis debe ser siempre correcta.", "Una predicción se comprueba y se corrige después de leer."),
    ],
    [
        ("Lees el título «Save the Water» y el subtítulo «Ten ways to use less at home». ¿De qué es más probable que trate? A) de formas de gastar menos agua en casa B) de la historia de los ríos del mundo", "A) de formas de gastar menos agua en casa", "Save the water y use less at home hablan de ahorrar agua en la casa."),
        (BEE + " ¿Qué usan los astrónomos en el norte de Chile para estudiar estrellas y planetas?", "Grandes telescopios", "El texto dice Astronomers use big telescopes there."),
        (BEE + " ¿Cuál es el subtítulo?", "Seeing the stars in northern Chile", "Está después del título."),
    ],
    [
        (BEE + " ¿Cuál es el propósito del texto? A) informar sobre el valor de los cielos oscuros B) vender telescopios", "A) informar sobre el valor de los cielos oscuros", "Explica para qué se usan y qué los amenaza."),
        (BEE + " ¿Qué hacen algunos pueblos para que el cielo siga oscuro?", "Apagan las luces sobrantes", "El texto dice Some towns turn off extra lights."),
        (BEE + " ¿Qué propósito de lectura es adecuado para saber quién usa el cielo del norte? A) buscar las partes con astronomers y visitors B) leer solo el título", "A) buscar las partes con astronomers y visitors", "Esas oraciones nombran a quienes lo usan."),
    ],
    [
        (BEE + " Predijiste que el texto hablaría solo de telescopios. Después de leer, ¿se confirma? A) no del todo: habla también de visitantes, pueblos y peligro B) sí, solo de telescopios", "A) no del todo: habla también de visitantes, pueblos y peligro", "Además de los telescopios hay visitantes, pueblos que apagan luces y una amenaza."),
        (BEE + " ¿Para qué apagan luces algunos pueblos? A) para que el cielo siga oscuro B) para gastar menos en postes", "A) para que el cielo siga oscuro", "Dice so that the sky stays dark."),
        (BEE + " ¿Cuántas amenazas para los cielos oscuros nombra el texto? A) dos B) tres", "A) dos", "Nombra las luces de la ciudad y el crecimiento de los pueblos."),
    ],
    [
        ("Conocimiento previo: sabes que en el campo se ven más estrellas que en la ciudad. ¿Qué dato nuevo agrega el texto? A) que astrónomos y visitantes viajan al norte de Chile por su cielo oscuro B) que en la ciudad se ven menos estrellas", "A) que astrónomos y visitantes viajan al norte de Chile por su cielo oscuro", "Lo de la ciudad ya lo sabías; el texto agrega quiénes viajan y por qué."),
        ("Ana lee «Why Dark Skies Matter» para una tarea de astronomía y Bruno para una receta de pan. ¿Quién tiene un propósito más conectado con el texto? A) Ana B) Bruno", "A) Ana", "El texto habla de estrellas y telescopios."),
    ],
    [
        ("¿Qué predicción es mejor para el subtítulo «Seeing the stars in northern Chile»? A) el texto hablará de observar las estrellas en el norte del país B) el texto hablará de cocinar en el sur", "A) el texto hablará de observar las estrellas en el norte del país", "Stars y northern Chile señalan el tema y el lugar."),
        (BEE + " Un compañero dice que el cielo del norte de Chile está cubierto de luces. ¿Qué dato lo corrige? A) el cielo es muy claro y oscuro B) el cielo es muy brillante de noche", "A) el cielo es muy claro y oscuro", "El texto dice very clear and dark."),
    ],
    [("Un cartel dice: Título: «Beach Clean-up Day». Subtítulo: «Bring gloves and a bag». ¿Qué debes llevar según el subtítulo? (gloves = guantes, bag = bolsa)", "Guantes y una bolsa", "El subtítulo lo dice.")],
    [
        ("¿Qué es un propósito de lectura?", "Saber para qué leo", "Dirige qué busco en el texto."),
        ("¿Qué se usa para hacer una predicción?", "El título, el subtítulo y las imágenes", "Dan pistas del tema."),
        ("¿Qué hago con una predicción después de leer?", "La comparo con el texto", "Se confirma o se corrige."),
    ],
    task("Lee este título y subtítulo originales: «The Night Market. Where food, music and friends meet.» (market = feria, meet = se encuentran). Antes de leer el texto, escribe en tu hoja: tu propósito de lectura, tres palabras que predices, y qué conocimiento previo sobre ferias nocturnas usarías. Después lee el texto y confirma: «The Night Market opens every Friday at six. There are food stands, live music and handmade crafts. Entrance is free.» (opens = abre, stands = puestos, crafts = artesanías).", "Propósito: saber cuándo abre y qué hay. Predicción: food, music, stands. Conocimiento previo: las ferias tienen comida y música. Confirmado: abre los viernes a las seis, hay puestos de comida, música en vivo y artesanías.", ["escribe propósito, predicción y conocimiento previo antes de leer", "confirma con datos del texto", "corrige o ajusta si algo no se cumple"], ["hoja con tres columnas", "nota de confirmación"], ["predecir sin conectar con el texto", "no confirmar después"], "Valora la predicción y ayuda a la persona a confirmar con el texto."),
    "Vuelve a leer el título y subtítulo de «Why Dark Skies Matter» y escribe dos predicciones distintas.",
    "Escribe en español un propósito de lectura para un texto sobre tu deporte preferido.",
)

# ---------------------------------------------------------------- clase 2: lectura rápida y focalizada, elementos organizacionales
FEST = "Título: «Youth Science Festival». Subtítulo: «Three days of experiments». Cuadro del programa: «Day 1 (Friday): chemistry show at 10; robots workshop at 12. Day 2 (Saturday): space talk at 11; planetarium visit at 3. Day 3 (Sunday): family experiments at 10; closing ceremony at 1. Tickets: 3,000 pesos; children under 8 free.» (festival = festival, show = show, workshop = taller, talk = charla, planetarium = planetario, closing = clausura, tickets = entradas)"
CYCLE = "Título: «From Idea to School Magazine». Diagrama con cuatro rótulos numerados: 1 Idea (el equipo elige un tema) → 2 Draft (los estudiantes escriben la primera versión) → 3 Review (una profesora y un compañero la leen y proponen cambios) → 4 Publication (la revista se imprime y se reparte). (idea = idea, draft = borrador, review = revisión, publication = publicación, team = equipo)"

lesson(
    OA6, 2, MATR,
    "Aprenderé a usar la lectura rápida (skimming) y la lectura focalizada (scanning) y a leer los elementos organizacionales (título, subtítulo, diagramas, cuadros). Sirve para encontrar un dato sin leer todo el texto.",
    ["Sé fijar un propósito de lectura.", "Sé qué es un título y un subtítulo."],
    [
        "La lectura rápida (skimming) consiste en mirar con rapidez el título, el subtítulo, el primer párrafo y las palabras destacadas para saber de qué trata el texto. Responde a «¿qué es esto?». La lectura focalizada (scanning) consiste en pasar los ojos buscando una palabra o un número exacto, sin leer todo. Responde a «¿dónde está este dato?». Se usa para horarios, precios y fechas.",
        "Los elementos organizacionales (organizational features) ayudan a ubicarte: el título dice el tema, el subtítulo lo precisa, los cuadros muestran datos ordenados y los diagramas explican procesos con números y flechas. En el programa del festival, el cuadro agrupa los datos por día; en el diagrama de la revista, los números 1 a 4 muestran el orden del proceso. Leerlos primero ahorra tiempo.",
        "Elige la estrategia según tu propósito: si quieres saber de qué trata el texto, hojea (skim); si quieres saber a qué hora es el planetario, rastrea (scan) la palabra planetarium y lee solo esa línea. Después de encontrar el dato, léelo con calma para no confundir horas parecidas.",
    ],
    [("skimming", "lectura rápida: mirar para saber de qué trata"), ("scanning", "lectura focalizada: buscar un dato exacto"), ("organizational feature", "elemento organizacional: título, subtítulo, cuadro, diagrama"), ("diagram", "diagrama"), ("caption", "pie de imagen"), ("keyword", "palabra clave")],
    [
        ("Scanning", FEST + " ¿A qué hora es la visita al planetario?", ["Hago scanning de la palabra planetarium.", "Está en el día 2: planetarium visit at 3.", "La hora es las 3."], "A las 3 (15:00)"),
        ("Orden en un diagrama", CYCLE + " ¿Qué paso va justo después del borrador (draft)?", ["Miro los números del diagrama.", "Draft es el número 2.", "El número 3 es review."], "La revisión (review)"),
    ],
    [
        ("Leer todo el texto para buscar una hora.", "Se pierde tiempo sin necesidad.", "Usa scanning: busca la palabra y mira el número cercano."),
        ("Saltarse el diagrama.", "Se cree que el diagrama no es parte del texto.", "Lee primero los rótulos y números: muestran el orden."),
    ],
    [
        (FEST + " ¿Cuántos días dura el festival?", "Tres días", "El subtítulo dice Three days of experiments."),
        (FEST + " ¿Cuánto cuesta la entrada?", "3.000 pesos", "El cuadro dice Tickets: 3,000 pesos."),
        (CYCLE + " ¿Cuántos pasos tiene el proceso de la revista? A) cuatro B) seis", "A) cuatro", "El diagrama numera del 1 al 4."),
    ],
    [
        (FEST + " ¿Qué estrategia usas para saber de qué trata el texto? A) skimming del título y subtítulo B) leer línea por línea", "A) skimming del título y subtítulo", "El título y el subtítulo resumen el tema."),
        (FEST + " ¿Qué hay el domingo a las diez? A) experimentos en familia B) charla del espacio", "A) experimentos en familia", "El cuadro dice Day 3: family experiments at 10."),
        (CYCLE + " ¿Qué ocurre en la etapa 4? A) la revista se imprime y se reparte B) se elige el tema", "A) la revista se imprime y se reparte", "Publication es el paso final del diagrama."),
    ],
    [
        (FEST + " ¿Qué niños no pagan entrada? A) los menores de ocho años B) los mayores de ocho", "A) los menores de ocho años", "Dice children under 8 free."),
        (CYCLE + " ¿Qué paso explica que otra persona lea el texto y proponga cambios? A) review B) draft", "A) review", "En el paso 3 una profesora y un compañero la leen y proponen cambios."),
        arith(FEST + " Una familia compra 4 entradas para un día. ¿Cuántos pesos paga? (todas pagan entrada completa)", "4*3000", "Se multiplica el valor de cada entrada por cuatro."),
    ],
    [
        (FEST + " ¿Qué dos actividades hay el día 1? A) chemistry show y robots workshop B) planetarium visit y closing ceremony", "A) chemistry show y robots workshop", "El cuadro del día 1 incluye el show de química y el taller de robots."),
        (CYCLE + " ¿Qué paso es el primero del proceso? A) idea B) publication", "A) idea", "El diagrama numera la elección del tema como paso 1."),
    ],
    [
        (FEST + " Un lector dice que la clausura es el sábado. ¿Qué parte lo corrige? A) Day 3 (Sunday): closing ceremony at 1 B) Day 2 (Saturday): space talk", "A) Day 3 (Sunday): closing ceremony at 1", "La clausura figura el día 3, el domingo."),
        (CYCLE + " Un compañero dice que la publicación va antes del borrador. ¿Cómo lo corriges? A) el borrador es 2 y la publicación es 4 B) la publicación es 1", "A) el borrador es 2 y la publicación es 4", "Los números del diagrama marcan el orden."),
    ],
    [("Lee este horario de biblioteca: «Title: Opening hours. Monday to Friday: 9 a.m. to 7 p.m. Saturday: 10 a.m. to 2 p.m. Sunday: closed.» ¿Qué día está cerrada? (opening hours = horario, closed = cerrada)", "El domingo", "La línea del horario dice Sunday: closed.")],
    [
        ("¿Qué respuesta da el skimming?", "De qué trata el texto", "Se hojea para tener la idea general."),
        ("¿Qué busca el scanning?", "Un dato exacto", "Palabra o número específico."),
        ("¿Qué muestran los números de un diagrama?", "El orden del proceso", "Indican el paso."),
    ],
    task("Lee este texto original: Título: «School Lunch Menu». Subtítulo: «Week 1». Cuadro: «Monday: rice and chicken. Tuesday: lentils and salad. Wednesday: pasta with tomato sauce. Thursday: vegetable soup and bread. Friday: fish and potatoes. All lunches include fruit. Vegetarian option every day.» (lentils = lentejas, soup = sopa, fish = pescado, include = incluyen). En tu hoja escribe: de qué trata (skimming), qué se come el miércoles (scanning), qué incluyen todos los almuerzos y si hay opción vegetariana.", "Trata del menú de almuerzos de la semana 1. El miércoles hay pasta con salsa de tomate. Todos incluyen fruta. Sí hay opción vegetariana todos los días.", ["usa skimming para el tema y scanning para el dato", "lee los elementos organizacionales", "responde con datos exactos"], ["hoja con cuatro respuestas", "subrayado de las palabras clave"], ["leer todo el cuadro para un dato", "confundir los días"], "Valora el uso de ambas estrategias y practica con otro dato del cuadro."),
    "Vuelve a mirar el programa del festival y escribe en tu hoja una pregunta que se responda con scanning y otra con skimming.",
    "Escribe en español dos situaciones de tu semana en que usarías scanning (por ejemplo, buscar un horario).",
)

# ---------------------------------------------------------------- clase 3: inferir y releer
UMB = "«Daniel looked at the sky and closed his notebook. He took his umbrella from the bag and put it next to his jacket. Then he ran to the bus stop. Behind him, the street lights were already on.» (looked at the sky = miró el cielo, notebook = cuaderno, umbrella = paraguas, bus stop = paradero, street lights = faroles, already = ya)"
MARA = "«Mara checked her phone again. It was ten past five. The game started at five thirty, and the stadium was thirty minutes away by bus. She grabbed her scarf and ran out without her lunch.» (checked = revisó, stadium = estadio, away = lejos, grabbed = tomó, scarf = bufanda, without = sin)"

lesson(
    OA6, 3, MATR,
    "Aprenderé a hacer inferencias y a releer mientras leo. Sirve para entender lo que el texto sugiere sin decirlo y para corregir una lectura que no calza.",
    ["Sé buscar datos exactos en un texto.", "Sé qué es una inferencia al escuchar."],
    [
        "Una inferencia (inference) es una conclusión que sacas con pistas del texto y lo que ya sabes. En «Daniel looked at the sky and took his umbrella», el texto no dice que va a llover, pero lo infieres: mirar el cielo + llevar paraguas + faroles encendidos sugieren que oscurece y podría llover. Cada inferencia debe apoyarse en pistas del texto, no en lo que se te ocurre.",
        "Releer (reread) es volver a una parte para comprobar un dato o entender mejor. Se relee cuando una respuesta no calza, cuando una palabra confunde o cuando los datos parecen contradecirse. En el texto de Mara, para saber si llegará a tiempo debes releer las horas: son las 5:10, el partido es a las 5:30 y el estadio queda a 30 minutos.",
        "Una estrategia útil es el esquema pista + conocimiento = inferencia. Pista: «ran out without her lunch». Conocimiento: quien corre sin almuerzo tiene apuro. Inferencia: Mara está atrasada. Verifica con otra pista: «checked her phone again». Dos pistas confirman la inferencia.",
    ],
    [("inference", "inferencia: conclusión basada en pistas"), ("clue", "pista"), ("reread", "releer"), ("evidence", "evidencia: la frase que respalda"), ("already", "ya"), ("without", "sin")],
    [
        ("Inferir", UMB + " ¿Qué crees que va a pasar? Da dos pistas.", ["Miro lo que hace: mira el cielo y saca el paraguas.", "Los faroles ya están encendidos: se hace tarde.", "Infiero que va a llover pronto."], "Que va a llover; pistas: miró el cielo y sacó el paraguas"),
        ("Releer para comprobar", MARA + " ¿Llegará al partido a la hora? Relee las horas.", ["Son las 5:10 y el partido es a las 5:30.", "El estadio queda a 30 minutos en bus.", "Necesita 30 minutos pero solo tiene 20: llegará tarde."], "No, llegará tarde porque necesita 30 minutos y solo tiene 20"),
    ],
    [
        ("Dar una inferencia sin pistas del texto.", "La conclusión parece verdadera por intuición.", "Escribe siempre las pistas que la apoyan."),
        ("No releer cuando los datos parecen contradecirse.", "Se confía en la primera lectura.", "Vuelve a la parte dudosa y compara los datos."),
    ],
    [
        (UMB + " ¿Qué lleva Daniel? A) un paraguas B) un abrigo grueso", "A) un paraguas", "El texto dice He took his umbrella."),
        (UMB + " ¿Adónde corre?", "Al paradero de buses", "El texto dice he ran to the bus stop."),
        (MARA + " ¿Qué dejó Mara al salir? A) su almuerzo B) su celular", "A) su almuerzo", "El texto dice without her lunch."),
    ],
    [
        (UMB + " ¿Qué pista indica que oscurece? A) los faroles ya estaban encendidos B) cerró el cuaderno", "A) los faroles ya estaban encendidos", "Se encienden cuando falta luz."),
        (MARA + " ¿Cómo se siente Mara? A) apurada B) aburrida", "A) apurada", "Revisa el celular y corre."),
        (MARA + " ¿A qué hora empieza el partido?", "A las 5:30", "El texto dice The game started at five thirty."),
    ],
    [
        arith(MARA + " Son las 5:10 y el partido es a las 5:30. ¿Cuántos minutos le quedan para llegar?", "30-10", "Se restan los minutos que han pasado de la media hora."),
        (MARA + " Si el viaje dura 30 minutos y le quedan 20, ¿cuántos minutos llegará tarde? A) 10 B) 20", "A) 10", "30 − 20 = 10 minutos."),
        (UMB + " ¿Qué conclusión se apoya en dos pistas? A) va a llover porque miró el cielo y sacó el paraguas B) va a llegar tarde porque corre", "A) va a llover porque miró el cielo y sacó el paraguas", "Las dos pistas apoyan la lluvia."),
    ],
    [
        (MARA + " Una lectora infiere que Mara tiene mucho tiempo. ¿Qué parte del texto la contradice? A) ran out without her lunch B) she grabbed her scarf", "A) ran out without her lunch", "Salir corriendo sin almuerzo muestra apuro."),
        (UMB + " Un lector dice que Daniel va a un partido. ¿Es una inferencia válida? A) no, el texto no da pistas de un partido B) sí, porque corre", "A) no, el texto no da pistas de un partido", "Correr al paradero no indica un partido."),
    ],
    [
        (MARA + " Relee y responde: ¿qué pista de lugar muestra que el estadio está lejos? A) thirty minutes away by bus B) she grabbed her scarf", "A) thirty minutes away by bus", "Esa frase da la distancia en tiempo."),
        ("Lee: «Pablo opened the fridge and sighed. There was only a lemon and a bottle of water. He closed the door and looked for his wallet.» (fridge = refrigerador, sighed = suspiró, wallet = billetera). ¿Qué infieres? A) que Pablo va a salir a comprar comida B) que Pablo cocinará una gran cena", "A) que Pablo va a salir a comprar comida", "El refrigerador casi vacío y la billetera lo sugieren."),
    ],
    [("Lee: «Sofía put on her helmet, checked her bike tires and filled her water bottle.» (helmet = casco, tires = neumáticos, filled = llenó). ¿Qué infieres que hará?", "Un paseo en bicicleta", "El casco, los neumáticos y el agua son pistas.")],
    [
        ("¿Qué necesita una inferencia?", "Pistas del texto", "Si no hay pistas, es una suposición."),
        ("¿Cuándo conviene releer?", "Cuando un dato no calza", "Vuelves a comprobar."),
        ("¿Para qué sirve una segunda pista?", "Para confirmar la inferencia", "Dos pistas hacen más firme la conclusión."),
    ],
    task("Lee este texto original: «Lucas looked at the clock and packed his bag in a hurry. He did not have breakfast. On the street, he saw the bus leaving and ran, but it was too late. He sat on the bench and called his sister.» (packed = guardó, in a hurry = apurado, breakfast = desayuno, leaving = saliendo, too late = demasiado tarde, called = llamó). En tu hoja escribe dos inferencias con sus pistas y una parte que releerías para confirmar.", "Inferencia 1: Lucas está atrasado; pistas: miró el reloj y guardó sus cosas apurado. Inferencia 2: perdió el bus; pistas: vio que salía y era demasiado tarde. Releería la parte del reloj y del bus.", ["escribe dos inferencias válidas", "cita una pista para cada una", "indica qué parte releería"], ["hoja con dos inferencias y pistas", "nota del adulto"], ["inferir sin pistas", "copiar la frase en lugar de inferir"], "Reconoce las pistas y ayuda a unirlas con un conocimiento previo."),
    "Vuelve a leer el texto de Daniel y escribe tres pistas que apoyen que anochece.",
    "Escribe en español una escena de tres líneas donde el lector infiera que alguien está nervioso sin decirlo.",
)

# ---------------------------------------------------------------- clase 4: después de leer: organizadores, resumen y vacío de información
PARTA = "Parte A: «Elisa works in a bakery. She wakes up at four every morning. At five she makes the dough and puts the bread in the oven. At seven the first customers arrive.» (bakery = panadería, wakes up = se levanta, dough = masa, oven = horno, customers = clientes)"
PARTB = "Parte B: «At noon, Elisa sells the last loaf. In the afternoon she cleans the shop and prepares the dough for the next day. She goes home at four and sleeps early.» (sells = vende, loaf = pan, cleans = limpia, prepares = prepara, goes home = vuelve a casa)"

lesson(
    OA6, 4, "Dos mitades de un texto escritas en cada ejercicio (parte A y parte B); lápiz y hoja para armar un organizador gráfico.",
    "Aprenderé a confirmar predicciones, usar organizadores gráficos y resumir después de leer, y a completar un texto uniendo dos partes que leen personas distintas. Sirve para estudiar y para explicar lo leído.",
    ["Sé predecir con el título.", "Sé inferir con pistas."],
    [
        "La pos lectura (post-reading) ocurre después de leer. Primero confirmas tus predicciones: ¿acerté o debo corregir? Luego organizas la información con un organizador gráfico (graphic organizer), como una línea de tiempo, una tabla o un esquema de idea principal y detalles. Un organizador convierte el texto en algo que puedes revisar de un vistazo.",
        "Para resumir, usa tu organizador: escribe quién, qué y cuándo, sin copiar frases. Un buen resumen es más corto que el texto y no agrega datos. Para el texto de Elisa: «Elisa, panadera, se levanta a las cuatro, hace pan, atiende clientes, limpia y se acuesta temprano». Si dos lectores leyeron partes distintas, deben compartir sus datos y completar la línea de tiempo entre los dos.",
        "Otra estrategia de pos lectura es preguntar para confirmar información: «¿A qué hora llegan los primeros clientes?». Si un compañero responde, lo compruebas en el texto. Así evitas errores y completas lo que no leíste.",
    ],
    [("post-reading", "pos lectura: lo que hago después de leer"), ("graphic organizer", "organizador gráfico: tabla, esquema o línea de tiempo"), ("timeline", "línea de tiempo"), ("summary", "resumen"), ("confirm", "confirmar"), ("information gap", "vacío de información")],
    [
        ("Línea de tiempo", PARTA + " " + PARTB + " Ordena de la mañana a la tarde: A) limpiar B) atender a los primeros clientes C) hornear.", ["Hornear ocurre a las 5.", "Los clientes llegan a las 7.", "Limpiar ocurre en la tarde."], "C, B, A"),
        ("Completar con la otra parte", PARTA + " ¿A qué hora vuelve Elisa a casa? Esa información está en la parte B: " + PARTB, ["El dato no está en la parte A.", "La parte B dice She goes home at four.", "Vuelve a las 4 de la tarde."], "A las 4 de la tarde"),
    ],
    [
        ("Resumir copiando el texto completo.", "No se separa lo esencial.", "Escribe quién, qué y cuándo con tus palabras."),
        ("Responder solo con la parte que leíste.", "Se olvida que el compañero tiene otra información.", "Pregunta y completa con la otra parte."),
    ],
    [
        (PARTA + " ¿A qué hora se levanta Elisa?", "A las cuatro", "Dice wakes up at four."),
        (PARTA + " ¿Qué pone en el horno a las cinco?", "El pan", "Dice puts the bread in the oven."),
        (PARTB + " ¿Qué prepara en la tarde?", "La masa del día siguiente", "Dice prepares the dough for the next day."),
    ],
    [
        (PARTA + " " + PARTB + " ¿Qué organizador sirve para ordenar sus actividades? A) una línea de tiempo B) un diagrama de Venn", "A) una línea de tiempo", "Las actividades siguen un orden en el tiempo."),
        (PARTA + " " + PARTB + " ¿A qué hora vende el último pan?", "Al mediodía", "Dice At noon, Elisa sells the last loaf."),
        (PARTA + " " + PARTB + " ¿Qué hace justo antes de volver a casa? A) limpia la tienda y prepara masa B) hornea pan", "A) limpia la tienda y prepara masa", "Son las actividades de la tarde antes de las cuatro."),
    ],
    [
        arith(PARTA + " " + PARTB + " Elisa se levanta a las 4 y vuelve a casa a las 16. ¿Cuántas horas pasan entre ambos momentos?", "16-4", "Se resta la hora de levantarse de la hora de volver."),
        (PARTA + " " + PARTB + " ¿Cuál es el mejor resumen? A) Elisa es panadera: hornea al amanecer, atiende clientes y limpia por la tarde B) Elisa vende pan solo en la tarde", "A) Elisa es panadera: hornea al amanecer, atiende clientes y limpia por la tarde", "Reúne las ideas de ambas partes."),
        (PARTA + " Predijiste que el texto hablaría de un restaurante. Tras leer la parte A, ¿se confirma? A) no, trata de una panadería B) sí", "A) no, trata de una panadería", "El texto dice Elisa works in a bakery."),
    ],
    [
        (PARTA + " " + PARTB + " La lectora de la parte B pregunta: «¿A qué hora llegan los primeros clientes?». ¿Quién tiene el dato? A) la lectora de la parte A B) la lectora de la parte B", "A) la lectora de la parte A", "El dato está en la parte A: At seven."),
        (PARTA + " " + PARTB + " Un compañero dice que Elisa duerme tarde. ¿Qué dato lo corrige? A) sleeps early B) wakes up at four", "A) sleeps early", "La parte B dice que duerme temprano."),
    ],
    [
        ("Completa el organizador. Tema: la jornada de Elisa. Mañana: ____. Tarde: ____. Elige: A) hornear y atender clientes / limpiar y preparar masa B) limpiar / hornear", "A) hornear y atender clientes / limpiar y preparar masa", "El orden sigue los datos de las dos partes."),
        (PARTA + " " + PARTB + " ¿Qué pregunta confirma que entendiste la parte B? A) ¿Qué hace Elisa en la tarde? B) ¿Cuál es su apellido?", "A) ¿Qué hace Elisa en la tarde?", "La parte B habla de la tarde."),
    ],
    [("Lee la parte A: «Marcos works in a bike shop. He opens at nine and fixes flat tires.» (flat tires = neumáticos pinchados). La parte B dice: «He closes at six and counts the money.» ¿A qué hora cierra la tienda? Ese dato está en la parte B.", "A las seis", "La parte B dice He closes at six.")],
    [
        ("¿Qué es un organizador gráfico?", "Un esquema, tabla o línea de tiempo que ordena lo leído", "Resume la información visualmente."),
        ("En Inglés: ¿Qué incluye un buen resumen?", "Quién, qué y cuándo con palabras propias", "Es más corto que el texto."),
        ("¿Qué haces con una predicción después de leer?", "La confirmo o la corrijo", "Compruebas con el texto."),
    ],
    task("Con la parte A de un texto original: «Parte A: Carlos is a lighthouse keeper (fictional). He wakes up at six, checks the lamp and writes the weather in a notebook.» (lighthouse keeper = farero, lamp = lámpara) y la parte B: «Parte B: At night he turns on the light so that ships can see the coast. He drinks hot tea and reads until midnight.» (turns on = enciende, ships = barcos, coast = costa, midnight = medianoche), arma una línea de tiempo con cuatro hechos y escribe un resumen de una frase.", "Línea: 6:00 se levanta; revisa la lámpara y anota el clima; en la noche enciende la luz para los barcos; lee y toma té hasta medianoche. Resumen: Carlos, un farero, revisa la lámpara por la mañana y enciende la luz de noche para guiar a los barcos.", ["ordena cuatro hechos en el orden correcto", "usa datos de ambas partes", "escribe un resumen breve sin copiar"], ["hoja con línea de tiempo y resumen", "nota del adulto"], ["usar solo una de las partes", "copiar frases enteras"], "Reconoce el orden logrado y ayuda a acortar el resumen."),
    "Dibuja una línea de tiempo con las actividades de Elisa y pídele a un adulto que la lea.",
    "Escribe en español un organizador de cuatro pasos para un texto que hayas leído esta semana.",
)

# ---------------------------------------------------------------- clase 5: ciclo completo de lectura estratégica
RECY = "Título: «From Sheep to Sweater». Subtítulo: «How wool becomes clothes». Texto: «Wool becomes clothes in four steps. First, farmers cut the wool from the sheep once a year. Second, workers wash the wool. Third, machines turn it into thread. Last, the thread is knitted into products, such as sweaters, scarves and hats. However, in many places woolen clothes are expensive because the work takes many hours.» (wool = lana, sheep = oveja, farmers = agricultores, thread = hilo, knitted = tejido, sweater = chompa, scarves = bufandas, hats = gorros, expensive = caro)"

lesson(
    OA6, 5, MATR,
    "Aprenderé a combinar las estrategias de antes, durante y después de leer en un solo texto: predecir, hacer lectura rápida y focalizada, inferir, releer, resumir y preguntar para confirmar. Sirve para leer de forma independiente.",
    ["Sé skimming y scanning.", "Sé hacer inferencias y organizadores."],
    [
        "Leer de manera estratégica es un ciclo. Antes de leer: fijas un propósito, predices con el título y activas lo que sabes. Durante la lectura: haces lectura rápida (skimming) para la idea general, lectura focalizada (scanning) para un dato, infieres con pistas y relees las partes confusas. Después de leer: confirmas tus predicciones, completas un organizador, resumes y haces preguntas para comprobar tu comprensión.",
        "En «From Sheep to Sweater», el título y el subtítulo predicen un texto sobre cómo la lana de la oveja se convierte en ropa. Las palabras First, Second, Third y Last señalan una secuencia de cuatro pasos. However marca un problema al final: la ropa de lana es cara porque el trabajo toma muchas horas. Un buen resumen respeta esa estructura: pasos y problema.",
        "Para preguntar y confirmar, formula preguntas que se respondan con datos del texto: «¿Cuántos pasos tiene el proceso?», «¿Qué se hace en el paso tres?». Si alguien responde, comprueba su respuesta en el texto. Así verificas que tu comprensión coincide con la información real.",
    ],
    [("cycle", "ciclo: serie de pasos que se repite"), ("sequence", "secuencia: pasos en orden"), ("thread", "hilo"), ("knit", "tejer"), ("wool", "lana"), ("however", "sin embargo")],
    [
        ("Secuencia", RECY + " ¿Qué ocurre en el paso tres?", ["Busco Third en el texto.", "Dice machines turn it into thread.", "Las máquinas convierten la lana en hilo."], "Las máquinas convierten la lana en hilo"),
        ("Problema final", RECY + " ¿Cuál es el problema que señala el texto y qué palabra lo anuncia?", ["Busco However.", "Dice woolen clothes are expensive because the work takes many hours.", "El problema es el precio alto."], "La ropa de lana es cara porque el trabajo toma muchas horas; lo anuncia However"),
    ],
    [
        ("Saltarse los pasos y leer solo la última parte.", "Se pierde la secuencia.", "Sigue las palabras First, Second, Third y Last."),
        ("No comprobar las respuestas de otros en el texto.", "Se confía sin verificar.", "Pregunta para confirmar y vuelve al texto."),
    ],
    [
        (RECY + " ¿Cuántos pasos tiene el proceso? A) cuatro B) tres", "A) cuatro", "El texto dice in four steps."),
        (RECY + " ¿Qué se hace en el primer paso?", "Los agricultores cortan la lana de la oveja", "Dice First, farmers cut the wool from the sheep."),
        (RECY + " ¿Qué se hace con el hilo al final? A) se teje en chompas, bufandas y gorros B) se lava otra vez y se guarda", "A) se teje en chompas, bufandas y gorros", "Dice the thread is knitted into products."),
    ],
    [
        (RECY + " ¿Qué productos se mencionan? A) chompas, bufandas y gorros B) mantas, zapatos y guantes", "A) chompas, bufandas y gorros", "Dice sweaters, scarves and hats."),
        (RECY + " ¿Qué predicción es más probable con el título «From Sheep to Sweater»? A) la lana de una oveja se convierte en ropa B) una chompa vieja se convierte en lana nueva", "A) la lana de una oveja se convierte en ropa", "From Sheep to Sweater marca el sentido de la transformación."),
        (RECY + " ¿Cuál es el propósito del texto? A) informar sobre un proceso B) convencer de comprar ropa nueva", "A) informar sobre un proceso", "Explica el proceso paso a paso."),
    ],
    [
        (RECY + " Ordena los pasos con letras. A) turn the wool into thread B) wash the wool C) knit the thread D) cut the wool", "D, B, A, C", "Primero se corta, luego se lava, después se hace hilo y al final se teje."),
        (RECY + " Pregunta para confirmar: «¿Quién lava la lana?» ¿Cuál es la respuesta? A) los trabajadores B) las máquinas", "A) los trabajadores", "Dice Second, workers wash the wool."),
        (RECY + " ¿Qué palabra anuncia el problema? A) However B) First", "A) However", "However introduce un contraste con lo anterior."),
    ],
    [
        (RECY + " Un compañero dice que la ropa de lana es barata en todas partes. ¿Qué parte lo corrige? A) in many places woolen clothes are expensive B) farmers cut the wool", "A) in many places woolen clothes are expensive", "El texto dice que en muchos lugares la ropa de lana es cara."),
        (RECY + " Un resumen de una frase. ¿Cuál es el mejor? A) La lana se convierte en ropa en cuatro pasos, pero la ropa de lana suele ser cara porque el trabajo toma muchas horas B) Las ovejas viven en el campo", "A) La lana se convierte en ropa en cuatro pasos, pero la ropa de lana suele ser cara porque el trabajo toma muchas horas", "Incluye los pasos y el problema."),
    ],
    [
        (RECY + " Haz una inferencia: ¿por qué una bufanda tejida a mano puede costar más? A) porque hacerla toma muchas horas de trabajo B) porque se vende solo en invierno", "A) porque hacerla toma muchas horas de trabajo", "El texto da como causa del precio las muchas horas de trabajo."),
        (RECY + " Relee el final: ¿qué palabra explica la causa del precio alto? A) because B) so that", "A) because", "Dice expensive because the work takes many hours."),
    ],
    [("Lee un anuncio: «Title: Library Book Sale. Subtitle: Save up to 70%. Saturday 10 to 4. All proceeds help buy new books.» (sale = venta, proceeds = dinero recaudado). ¿Qué estrategia usas para saber a qué hora es la venta? (skimming o scanning)", "Scanning", "Buscas el dato exacto de la hora.")],
    [
        ("¿Qué tres momentos tiene el ciclo de lectura estratégica?", "Antes, durante y después de leer", "Cada momento tiene estrategias."),
        ("¿Qué se hace al preguntar para confirmar?", "Comprobar la respuesta en el texto", "Verifica la comprensión."),
        ("¿Qué palabra anuncia un problema al final de un texto?", "However", "Introduce un contraste."),
    ],
    task("Lee este texto original: Título: «Learning to Cook». Subtítulo: «Three easy dishes for beginners». Texto: «Pasta with tomato sauce takes twenty minutes. A cheese sandwich takes five minutes. Rice with vegetables takes thirty minutes. However, beginners often forget to wash the vegetables. A simple solution is to wash them first.» (dishes = platos, takes = demora, beginners = principiantes, forget = olvidar, simple solution = solución simple). En tu hoja escribe: tu predicción antes de leer, qué plato demora menos (scanning), el problema y la solución, y una pregunta para confirmar.", "Predicción: recetas fáciles. Demora menos el sándwich de queso (cinco minutos). Problema: los principiantes olvidan lavar las verduras. Solución: lavarlas primero. Pregunta: ¿Cuánto demora el arroz con verduras?", ["escribe una predicción antes de leer", "usa scanning para un dato exacto", "separa problema y solución y formula una pregunta"], ["hoja con cinco respuestas", "subrayado del texto"], ["leer sin predicción", "preguntar algo que no se responde con el texto"], "Valora el uso del ciclo completo y revisa la pregunta con el texto."),
    "Vuelve a leer «From Sheep to Sweater» y escribe tres preguntas que se respondan con el texto.",
    "Escribe en español qué estrategia de lectura usarías para buscar un número de teléfono y cuál para entender de qué trata un artículo.",
)
