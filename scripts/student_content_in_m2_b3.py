"""Cuaderno del estudiante, 2.º medio Inglés (oficial), IN2M OA 12: estrategias de lectura antes, durante y después.

Todos los textos están escritos en el enunciado (originales; temas de ciencias y seguridad escolar con datos generales).
Inglés americano. Los títulos de clase del plan son genéricos; aquí se aplican a prelectura (propósito, conocimientos
previos), lectura rápida y focalizada con elementos del texto, inferir, releer y preguntarse, postlectura con
organizadores gráficos, y recontar, resumir y preguntar para confirmar.
"""
from __future__ import annotations

from in_m2_common import MAT_R, arith, lesson, mc, mr, task

OA = "IN2M OA 12"

# ------------------------------------------------------------------ clase 1: antes de leer
V0 = "Título: «Why Do Volcanoes Erupt?» Subtítulo: «A short guide for students». Imagen: un dibujo de un volcán con humo. Primera oración: «A volcano is an opening in the Earth's surface where hot rock, ash and gases can come out.» (erupt = hacer erupción, guide = guía, opening = abertura, surface = superficie, hot rock = roca caliente, ash = ceniza, gases = gases)"
V1 = "Título: «How to Prepare for a School Trip». Imagen: una mochila abierta. Primera oración: «Before a trip, make a list of what to bring and check the weather.» (prepare = prepararse, school trip = paseo de curso, bring = llevar, weather = clima)"
V2 = "Título: «Meet Our New Student Council». Imagen: cinco jóvenes sonriendo en el patio. Primera oración: «This year, five students were elected to lead the council.» (council = centro de estudiantes, elected = elegidos, lead = dirigir)"
V3 = "Título: «The Price of Comfort» (un artículo de revista). Imagen: un sillón. Primera oración: «Many people buy expensive furniture, but few ask how long it will last.» (price = precio, comfort = comodidad, furniture = muebles, last = durar)"

lesson(
    OA, 1, MAT_R,
    "Aprenderé estrategias de prelectura: leer con un propósito y activar mis conocimientos previos mirando título, subtítulo, imágenes y primera oración. Sirve para entender mejor un texto antes de leerlo completo.",
    ["Sé leer títulos y subtítulos.", "Sé hacer predicciones."],
    [
        "La prelectura (pre-reading) son las acciones que haces antes de leer. Primero, define un propósito (purpose): ¿para qué leo? Puede ser aprender un dato, seguir instrucciones, disfrutar o preparar una opinión. El propósito decide cómo leerás: rápido para tener la idea general, o despacio para buscar un dato.",
        "Segundo, activa tus conocimientos previos (prior knowledge): ¿qué sé de este tema? Mira el título, el subtítulo, las imágenes y la primera oración. Con eso haz predicciones: ¿de qué tratará?, ¿qué palabras aparecerán?, ¿qué quiero saber? Una forma útil es la tabla K-W-L: lo que sé (Know), lo que quiero saber (Want) y lo que aprendí (Learned), que se completa después.",
        "Una buena prelectura toma dos minutos y ahorra tiempo después. Si el título es una pregunta, como Why Do Volcanoes Erupt?, tu propósito puede ser encontrar la respuesta. Escribe una pregunta propia antes de leer y busca su respuesta mientras lees.",
    ],
    [("purpose", "propósito de lectura"), ("prior knowledge", "conocimientos previos"), ("pre-reading", "prelectura"), ("prediction", "predicción"), ("title / subtitle", "título / subtítulo"), ("K-W-L chart", "tabla: sé, quiero saber, aprendí")],
    [
        ("Predecir con el título y la imagen", V0 + " ¿Qué predices que dirá el texto y qué quieres saber?", ["El título pregunta por qué los volcanes hacen erupción.", "Predigo que explicará las causas y las partes.", "Quiero saber qué sale del volcán."], "Que explicará por qué hacen erupción y qué sale de un volcán"),
        ("Elegir un propósito", V1 + " ¿Qué propósito de lectura es adecuado?", ["El texto es una guía para prepararse.", "Quiero saber qué llevar.", "Mi propósito: encontrar qué debo llevar y qué revisar."], "Encontrar qué debo llevar y qué revisar antes del paseo"),
    ],
    [
        ("Empezar a leer sin mirar el título ni las imágenes.", "Se pierden pistas del tema.", "Dedica dos minutos a título, subtítulo e imágenes."),
        ("Hacer predicciones que no tienen relación con las pistas.", "Una predicción debe apoyarse en lo que ves.", "Basa tu predicción en una pista concreta."),
    ],
    [
        mr(V0, "¿Qué pista del texto muestra que habla de ciencia?", "El título y el dibujo de un volcán", ["La fecha de publicación", "El tamaño de la letra"], "El título y la imagen dicen el tema."),
        mc("¿Para qué sirve tener un propósito de lectura?", "Para decidir cómo voy a leer", ["Para saltarse el título", "Para leer más rápido"], "El propósito guía la lectura."),
        mr(V1, "¿Qué esperas leer en este texto?", "Una lista de cosas para llevar", ["Un cuento de misterio sobre un paseo", "Una noticia sobre el clima de la semana"], "El título habla de prepararse."),
    ],
    [
        mr(V2, "¿Cuál es una predicción adecuada a partir del título y la imagen?", "Presentará a los cinco integrantes del centro", ["Explicará cómo se forman las capas", "Enseñará la receta de un pastel"], "El título dice Meet y la imagen muestra cinco jóvenes."),
        mr(V3, "¿Qué conocimiento previo te ayuda con este texto?", "Que los muebles caros no siempre duran más", ["Que los sillones se usan principalmente para dormir", "Que las revistas se imprimen en papel brillante"], "Se relaciona con el tema del precio y la duración."),
        mc("En una tabla K-W-L, ¿qué se escribe en la columna W?", "Lo que quiero saber", ["Lo que aprendí en el texto", "Lo que ya sé"], "W es Want to know."),
    ],
    [
        mr(V0, "Completa la tabla K-W-L antes de leer: K: un volcán saca cosas calientes. ¿Cuál es una buena W?", "¿Qué hay dentro del volcán?", ["Los volcanes sacan cosas muy calientes", "Un volcán es grande"], "W es una pregunta que quieres responder; las otras opciones son cosas que ya sabes."),
        mr(V3, "Predice qué dirá el texto con la primera oración. ¿Cuál es la mejor predicción?", "Que explicará cuánto duran los muebles caros", ["Que contará un viaje en tren", "Que dará una receta de cocina"], "La primera oración habla de durar."),
        arith("Antes de leer, una estudiante dedica 2 minutos a la prelectura de cada uno de 4 textos. ¿Cuántos minutos en total?", "2*4", "Se multiplica el tiempo por el número de textos.", " minutos"),
    ],
    [
        mr(V2, "Un compañero dice que no sirve mirar la imagen porque no tiene letras. ¿Qué respuesta es mejor?", "La imagen da pistas del tema y ayuda a predecir", ["Tiene razón: solo importan las letras", "Las imágenes se miran al final"], "Las imágenes son pistas."),
        mr(V1, "Si tu propósito es saber qué llevar, ¿cómo lees?", "Busco la lista y la palabra bring", ["Leo palabra por palabra sin saltar nada", "Salto el texto"], "Un propósito de datos pide leer con foco."),
    ],
    [
        mr(V0 + " " + V3, "Lees dos textos con propósitos distintos. ¿Cuál requiere una lectura que busque la explicación de una causa?", "El texto de los volcanes", ["El texto de los muebles", "Ninguno de los dos"], "El título pregunta por qué."),
        mc("Un estudiante lee el título, mira la imagen y escribe una pregunta propia. ¿Qué estrategia usó?", "Prelectura con propósito", ["Resumen del texto ya leído", "Edición del texto"], "Es lo que se hace antes de leer."),
    ],
    [mr(V2, "Antes de leer este texto, ¿cuál es una pregunta propia adecuada?", "Who are the five students?", ["How is a volcano formed?", "What is a good recipe for bread?"], "La pregunta se relaciona con el título y la imagen.")],
    [
        ("En Inglés de 2.º medio (OA 12, clase 1): ¿qué haces en la prelectura?", "Defino un propósito y activo conocimientos previos con título, imágenes y primera oración", "Prepara la lectura."),
        ("En Inglés de 2.º medio (OA 12, clase 1): ¿qué significa la columna L en una tabla K-W-L?", "Lo que aprendí", "Se completa después de leer."),
        ("En Inglés de 2.º medio (OA 12, clase 1): ¿qué es una predicción en la lectura?", "Una idea de lo que dirá el texto, basada en pistas", "No es una adivinanza."),
    ],
    task("Lee estas pistas. Título: «The Secret Life of Trees». Imagen: un bosque con una persona abrazando un tronco. Primera oración: «Trees can share food and information through their roots.» (secret = secreto, trees = árboles, share = compartir, information = información, roots = raíces). Escribe: tu propósito de lectura, lo que ya sabes, dos predicciones y una pregunta propia.", "Propósito: aprender cómo se comunican los árboles. Ya sé: tienen raíces. Predicciones: explicará cómo comparten comida; usará palabras como roots y forest. Pregunta: How do trees share food?", ["escribe un propósito claro", "da dos predicciones con pistas", "formula una pregunta propia"], ["hoja con cuatro respuestas"], ["predecir sin apoyarse en pistas", "no escribir una pregunta"], "Pide que lea el texto después y compruebe cuántas predicciones se confirmaron."),
    "Elige un texto en inglés de tu clase y haz solo la prelectura: título, imagen y primera oración.",
    "Haz una tabla K-W-L en español con un tema que te interese.",
)

# ------------------------------------------------------------------ clase 2: lectura rápida, focalizada y elementos del texto
EQ = "Título: «Earthquake Safety at School». Subtítulo: «What to do before, during and after». Sección 1, Before: «Know the safe places in your classroom, such as under a strong desk. Keep your exit path clear.» Sección 2, During: «Drop, cover and hold on. Stay away from windows. Do not run outside.» Sección 3, After: «Follow your teacher. Move calmly to the safe zone. Wait for instructions.» (earthquake = sismo, safety = seguridad, before = antes, during = durante, after = después, strong = firme, desk = pupitre, exit path = vía de salida, clear = despejada, drop = agáchate, cover = cúbrete, hold on = sujétate, windows = ventanas, safe zone = zona segura, wait = espera)"
DG = "Diagrama del texto: «Parts of a Volcano». Tiene flechas y palabras: crater (cráter) en la cima, vent (conducto) en el centro, magma chamber (cámara de magma) abajo, ash cloud (nube de ceniza) arriba."
TX = "«A museum guide says: The art museum opens at 10 a.m. and closes at 6 p.m. Tickets cost 4,000 pesos for adults and 2,000 pesos for students. The new room about modern art is on the second floor. Free tours start at noon every day.» (museum = museo, opens = abre, closes = cierra, tickets = entradas, modern art = arte moderno, floor = piso, tours = visitas guiadas, noon = mediodía)"

lesson(
    OA, 2, MAT_R,
    "Aprenderé a leer rápido para captar la idea general (skimming), a leer focalizado para buscar un dato (scanning) y a usar títulos, subtítulos y diagramas para organizar la lectura. Sirve para encontrar información sin leerlo todo.",
    ["Sé hacer prelectura con título e imágenes.", "Sé reconocer idea principal y detalles."],
    [
        "La lectura rápida (skimming) sirve para captar la idea general: lees el título, el subtítulo, la primera oración de cada sección y la última, sin detenerte en cada palabra. La lectura focalizada (scanning) sirve para encontrar un dato exacto: miras el texto buscando una palabra clave, un número o una palabra con mayúscula, y cuando la encuentras, lees solo esa parte con cuidado.",
        "Los elementos organizacionales (organizational elements) ayudan a ubicarse: el título dice el tema; el subtítulo precisa; los encabezados de sección dividen el texto (Before, During, After); las listas ordenan pasos; los diagramas muestran partes, procesos o relaciones con flechas y etiquetas. Un diagrama rotulado se lee mirando cada etiqueta y su flecha.",
        "Elige la estrategia según tu propósito. Para saber de qué trata, usa skimming; para saber a qué hora abre un museo, usa scanning en la palabra opens. También puedes plantearte preguntas mientras lees: ¿qué parte falta?, ¿qué significa esta palabra en el contexto?",
    ],
    [("skimming", "lectura rápida para la idea general"), ("scanning", "lectura focalizada para un dato"), ("heading / section", "encabezado / sección"), ("diagram / label", "diagrama / etiqueta"), ("keyword", "palabra clave"), ("organizational element", "elemento que organiza el texto")],
    [
        ("Skimming con títulos", EQ + " ¿De qué trata el texto, usando solo título, subtítulo y encabezados?", ["El título dice que habla de seguridad ante sismos en el colegio.", "Los encabezados son Before, During y After.", "Trata de qué hacer en cada momento."], "Trata de qué hacer antes, durante y después de un sismo en el colegio"),
        ("Scanning de un dato", TX + " ¿A qué hora abre el museo?", ["Busco la palabra opens.", "Dice opens at 10 a.m.", "Respondo con esa hora."], "A las 10 a.m."),
    ],
    [
        ("Leer todo el texto palabra por palabra para encontrar una hora.", "Se pierde tiempo.", "Busca la palabra clave y lee solo esa parte."),
        ("Ignorar los encabezados.", "Se pierden pistas de organización.", "Úsalos para ubicarte antes de leer."),
    ],
    [
        mr(EQ, "¿Cuántas secciones tiene el texto?", "Tres", ["Dos", "Cinco"], "Son Before, During y After."),
        mr(TX, "¿Cuánto cuesta una entrada de estudiante?", "2.000 pesos", ["4.000 pesos", "6.000 pesos"], "Dice 2,000 pesos for students."),
        mr(DG, "¿Qué hay en la cima del volcán según el diagrama?", "El cráter (crater)", ["La cámara de magma (magma chamber)", "El conducto"], "El crater está en la cima."),
    ],
    [
        mr(EQ, "¿Qué hacer durante el sismo según el texto?", "Agacharse, cubrirse y sujetarse", ["Correr afuera lo más rápido posible", "Acercarse a las ventanas"], "Dice Drop, cover and hold on."),
        mr(DG, "¿Qué hay abajo del volcán según el diagrama?", "La cámara de magma", ["La nube de ceniza y humo", "El cráter"], "Magma chamber está abajo."),
        mr(TX, "¿Dónde está la nueva sala de arte moderno?", "En el segundo piso", ["En el primer piso", "En la entrada"], "Dice on the second floor."),
    ],
    [
        mr(TX, "Quieres saber si hay una visita guiada a las 3 p.m. Para encontrarlo, ¿qué palabra buscas?", "tours", ["tickets", "closes"], "Tours se refiere a visitas guiadas."),
        mr(EQ, "¿Qué sección usas para saber qué hacer después del sismo?", "After", ["Before", "During"], "After trata de lo que sigue."),
        arith("Entrada de adulto: 4.000 pesos. Entrada de estudiante: 2.000 pesos. Un grupo de 2 adultos y 3 estudiantes visita el museo. ¿Cuántos pesos pagan en total?", "2*4000+3*2000", "Se suman los adultos y los estudiantes.", " pesos"),
    ],
    [
        mr(EQ, "Un compañero dice que en un sismo hay que salir corriendo del colegio. ¿Qué respuesta es más acertada?", "El texto dice Do not run outside", ["Tiene razón: hay que salir corriendo", "El texto no habla de salir"], "La instrucción es no correr afuera."),
        mr(DG, "Un lector dice que el diagrama rotula cinco partes del volcán. ¿Cuántas partes rotula en realidad?", "Cuatro etiquetas en total", ["Cinco, contando también las flechas", "Tres, sin la nube"], "Se cuentan las etiquetas una por una: crater, vent, magma chamber y ash cloud."),
    ],
    [
        mr(EQ, "Quieres encontrar solo lo que debes hacer antes. ¿Qué estrategia usas?", "Scanning de la sección Before", ["Skimming de todo el texto del cartel", "Leer solo el título"], "Se busca una parte específica."),
        mr(TX, "Quieres saber de qué trata el texto del museo. ¿Qué estrategia usas?", "Skimming del título y el inicio", ["Scanning de la palabra tours", "Leer el último número"], "Se busca la idea general."),
    ],
    [mr(DG + " " + EQ, "Un diagrama y un texto con secciones tienen la misma función de organizar. ¿Cuál es esa función?", "Ayudar a ubicar la información", ["Hacer el texto más largo", "Evitar leer el texto"], "Ambos organizan la información.")],
    [
        ("En Inglés de 2.º medio (OA 12, clase 2): ¿qué es skimming?", "Leer rápido para captar la idea general", "No se leen todas las palabras."),
        ("En Inglés de 2.º medio (OA 12, clase 2): ¿qué es scanning?", "Buscar un dato específico", "Se busca una palabra clave."),
        ("En Inglés de 2.º medio (OA 12, clase 2): ¿para qué sirven los encabezados?", "Para ubicarse y dividir el texto", "Muestran las secciones."),
    ],
    task("Lee: Título: «Welcome to Pine Park». Subtítulo: «Rules and Opening Hours». Sección 1, Hours: «Open every day from 8 a.m. to 7 p.m.». Sección 2, Rules: «Keep dogs on a leash. Do not pick flowers. Use the trash cans for trash.» Sección 3, Events: «Free yoga class on Saturdays at 9 a.m.» (hours = horarios, leash = correa, pick = cortar, trash cans = papeleros, trash = basura, yoga = yoga). Escribe tu propósito, qué estrategia usas para saber de qué trata (skimming) y cómo encuentras la hora de la clase de yoga (scanning).", "Propósito: saber qué se puede hacer en el parque. Skimming: título, subtítulo y encabezados Hours, Rules y Events. Scanning: busco yoga y encuentro Saturdays at 9 a.m.", ["explica el skimming con los elementos del texto", "explica el scanning con una palabra clave", "responde con datos exactos"], ["hoja con tres respuestas"], ["leer todo para encontrar un dato", "no usar los encabezados"], "Pide que busque con scanning otro dato del mismo texto."),
    "Elige una página de un libro de otra asignatura y haz skimming de títulos y subtítulos.",
    "Busca en una noticia en español un diagrama o encabezado y explica para qué sirve.",
)

# ------------------------------------------------------------------ clase 3: inferir, releer y preguntarse
IF1 = "«Tomás arrived at the station with a suitcase. The board said Train 417: CANCELED. He looked at his watch, sighed and began to call a taxi.» (suitcase = maleta, board = panel, canceled = cancelado, sighed = suspiró, call = llamar)"
IF2 = "«Laura opened her bag at the exam and found only a pencil case. She looked at her classmate, who was already writing. She raised her hand and said quietly, I forgot my calculator.» (exam = examen, pencil case = estuche, classmate = compañero, quietly = en voz baja, forgot = olvidé, calculator = calculadora)"
IF3 = "«The bakery on the corner was always full on Sundays. Yesterday, a sign hung on the door: Closed until further notice. People stood outside and looked at each other. One woman said, What are we going to do without our bread?» (bakery = panadería, sign = cartel, hung = colgaba, closed = cerrado, until further notice = hasta nuevo aviso, bread = pan)"
IF4 = "Texto sobre un parque de un pueblo de Chile: «In January, the town park was crowded. By June, the paths were empty and the fountain was covered with leaves. In September, buds appeared on the trees.» (crowded = repleto, paths = senderos, fountain = fuente, covered = cubierta, leaves = hojas, buds = brotes)"

lesson(
    OA, 3, MAT_R,
    "Aprenderé a hacer inferencias al leer, a releer los pasajes difíciles y a plantearme preguntas mientras leo. Sirve para entender lo que el texto sugiere sin decirlo y para resolver dudas.",
    ["Sé localizar información explícita.", "Sé usar el contexto para entender palabras."],
    [
        "Una inferencia (inference) es una conclusión que sacas con pistas del texto y lo que ya sabes. La fórmula es: pista del texto + conocimiento previo = inferencia. En Tomás looked at his watch, sighed and began to call a taxi, las pistas son el tren cancelado, mirar el reloj, suspirar y llamar un taxi. Con lo que sabes sobre trenes, infieres que necesita otra forma de llegar.",
        "Releer (rereading) es volver a un pasaje cuando no entiendes. Puedes releer una oración, un párrafo o todo el texto. Antes de releer, di qué no entendiste: ¿una palabra, un conector, una relación entre ideas? Al releer, busca esa parte. Preguntarte mientras lees (asking questions) mantiene tu atención: ¿qué pasó antes?, ¿por qué el personaje hace esto?, ¿qué quiere decir esta palabra?",
        "Una inferencia buena es posible, tiene pistas y no contradice el texto. Evita las inferencias sin pistas o que cambian los hechos. Si una inferencia no tiene dos pistas, busca más.",
    ],
    [("inference", "inferencia"), ("clue", "pista"), ("reread", "releer"), ("ask questions", "plantearse preguntas"), ("evidence", "evidencia"), ("It seems that", "parece que")],
    [
        ("Inferir con pistas", IF1 + " ¿Qué infieres que hará Tomás y por qué?", ["Pistas: Train 417: CANCELED, mirar el reloj, suspirar, llamar un taxi.", "Conocimiento previo: si el tren se cancela, hay que buscar otro medio.", "Infiero que irá en taxi."], "Que irá en taxi, porque su tren fue cancelado"),
        ("Releer para entender", IF2 + " ¿Por qué Laura levanta la mano?", ["Veo que abrió el bolso y solo había un estuche.", "Dice I forgot my calculator.", "Necesita ayuda con la calculadora."], "Porque olvidó su calculadora y necesita ayuda"),
    ],
    [
        ("Hacer una inferencia sin ninguna pista del texto.", "Una inferencia sin pista es una suposición.", "Busca al menos una pista en el texto."),
        ("Seguir leyendo sin entender y no releer.", "Se acumulan las dudas.", "Detente y relee la parte que falló."),
    ],
    [
        mr(IF3, "¿Qué pista muestra que la panadería cerró?", "El cartel de la puerta: Closed", ["La panadería estaba llena los domingos", "La gente conversaba"], "El cartel lo dice."),
        mr(IF4, "¿Qué infieres de que en junio los senderos estaban vacíos?", "Que era invierno y salía menos gente", ["Que el parque cerró para siempre en junio", "Que era verano"], "En junio es invierno en Chile y hay menos visitantes."),
        mc("¿Qué dos cosas se usan para hacer una inferencia?", "Pistas del texto y conocimientos previos", ["Solo la imaginación del lector", "Solo el título del texto"], "Es la fórmula de la inferencia."),
    ],
    [
        mr(IF3, "¿Cómo se sienten las personas que miran el cartel?", "Preocupadas o sorprendidas", ["Muy contentas", "Aburridas y sin interés"], "People stood outside and looked at each other, y la mujer pregunta qué harán sin pan: hay preocupación."),
        mr(IF2, "¿Cómo se sintió Laura al hablar?", "Con vergüenza o preocupación", ["Con mucha alegría", "Con enojo"], "Said quietly (en voz baja) y no tener su calculadora sugieren vergüenza o preocupación."),
        mr(IF4, "¿Qué estación del año sugiere que aparezcan brotes en septiembre?", "La primavera en Chile", ["El otoño, cuando caen las hojas", "El verano"], "En Chile, septiembre es primavera."),
    ],
    [
        mr(IF1, "Haz una pregunta mientras lees: ¿cuál aclara una duda que el texto no responde?", "Why was the train canceled?", ["What did the board say?", "Did he arrive?"], "El texto no dice por qué se canceló el tren; las otras preguntas ya tienen respuesta en el texto."),
        mr(IF2, "Relee la oración She looked at her classmate, who was already writing. ¿Qué infieres?", "Que su compañero ya empezó el examen", ["Que el examen es muy fácil para todos", "Que su compañero copia"], "Already writing muestra que el compañero ya había empezado."),
        mr(IF3, "¿Qué pregunta aclara una duda que el texto NO responde?", "Why is the bakery closed?", ["What did the sign say?", "Was it full on Sundays?"], "El texto no explica el motivo del cierre; las otras ya tienen respuesta."),
    ],
    [
        mr(IF1, "Un lector dice que Tomás cancela su viaje porque odia los trenes. ¿Qué responde alguien que lee con cuidado?", "No hay pistas de que odie los trenes", ["Tiene razón: odia los trenes", "El texto no habla de trenes"], "La inferencia debe tener pistas: el texto solo muestra que busca un taxi."),
        mr(IF4, "Un lector dice que el parque estaba lleno de hojas en enero. ¿Qué responde alguien que lee con cuidado?", "No: en enero estaba repleto de personas", ["Sí: estaba lleno de hojas", "No: nunca hubo hojas"], "Relee: crowded en enero y covered with leaves en junio."),
    ],
    [
        mr(IF3, "¿Qué infieres que hará la gente que compraba pan allí? Apóyate en dos pistas.", "Buscar otra panadería, porque el cartel dice cerrado", ["Esperar en la puerta hasta el domingo, porque abrirá pronto", "Comprar el doble de pan"], "Hay dos pistas en el texto: el cartel dice Closed y la mujer pregunta qué harán sin pan."),
        mr(IF1 + " " + IF2, "En ambos textos hay un problema inesperado. ¿Qué tienen en común sus protagonistas?", "Intentan resolver el problema", ["Se rinden y esperan sin hacer nada", "Se enojan con todos"], "Tomás llama un taxi y Laura pide ayuda."),
    ],
    [mr(IF2, "Relee y responde: ¿qué pregunta te ayuda a entender el final del texto?", "¿Qué necesita Laura para el examen?", ["¿De qué color es la calculadora de Laura?", "¿Cuántos años tiene el profesor?"], "Aclara el problema.")],
    [
        ("En Inglés de 2.º medio (OA 12, clase 3): ¿qué fórmula usas para hacer una inferencia?", "Pista del texto más conocimiento previo", "Así se llega a una conclusión."),
        ("En Inglés de 2.º medio (OA 12, clase 3): ¿qué haces antes de releer?", "Decir qué no entendí", "Así sabes qué buscar."),
        ("En Inglés de 2.º medio (OA 12, clase 3): ¿qué es una buena pregunta mientras lees?", "Una que se relaciona con el texto y aclara una duda", "Mantiene la atención."),
    ],
    task("Lee: «Ema stood in the hall with her ticket in her hand. The line was long and her friends were already inside. She looked at the clock: seven fifty-five. The doors close at eight, she whispered. She began to run.» (ticket = entrada, hall = vestíbulo, line = fila, inside = adentro, clock = reloj, doors = puertas, whispered = susurró, run = correr). Escribe dos inferencias con dos pistas cada una y una pregunta que te harías mientras lees.", "Inferencia 1: Ema teme llegar tarde; pistas: the doors close at eight, looked at the clock. Inferencia 2: Ema va a entrar a un evento; pistas: ticket, doors. Pregunta: Will she arrive in time?", ["escribe dos inferencias", "cada una tiene dos pistas", "formula una pregunta"], ["hoja con tres respuestas"], ["inferir sin pistas", "contradecir el texto"], "Pide que relea la última oración y diga qué cambia si Ema llega a tiempo."),
    "Relee un texto difícil y subraya la parte que no entendiste.",
    "Elige una escena de una serie y escribe en español una inferencia con dos pistas.",
)

# ------------------------------------------------------------------ clase 4: después de leer y organizadores gráficos
OR1 = "«Two Ways to Learn English (fictional). Apps are cheap and flexible: you can practice any time. Classes cost more and have a fixed schedule, but you get a teacher's feedback. Both need regular practice to work well.» (apps = aplicaciones, cheap = barata, flexible = flexible, fixed = fijo, feedback = comentarios, regular = regular, work = funcionar)"
OR2 = "«How a Letter Travels (fictional). First, you write the letter and put it in an envelope. Second, you take it to the post office. Third, workers sort it. Fourth, a truck takes it to another city. Finally, a mail carrier delivers it.» (envelope = sobre, post office = oficina de correos, sort = clasificar, mail carrier = cartero, delivers = entrega)"
OR3 = "«Why Plants Need Light (fictional). Plants use light to make their food. If a plant gets little light, it grows slowly and its leaves turn pale. As a result, a plant near a window is often greener than one in a dark corner.» (plants = plantas, light = luz, food = alimento, grows = crece, slowly = lentamente, pale = pálidas, greener = más verde)"
OR4 = "«Camila's Report (fictional). Last month, our class collected money for a school trip. Week 1: we made a plan. Week 2: we sold sandwiches. Week 3: we made a poster. Week 4: we counted the money.» (collected = juntó, plan = plan, sold = vendimos, counted = contamos)"

lesson(
    OA, 4, MAT_R,
    "Aprenderé estrategias de postlectura: responder las preguntas que me planteé, usar organizadores gráficos (diagrama de Venn, línea de tiempo, causa y efecto) y releer para comprobar. Sirve para ordenar lo que leí y recordarlo.",
    ["Sé hacer prelectura y inferencias.", "Conozco first, second y finally."],
    [
        "Después de leer, vuelve a tus preguntas del comienzo: ¿las respondiste? Si no, relee la parte que corresponde. Luego usa un organizador gráfico (graphic organizer) para ordenar las ideas. Un diagrama de Venn compara dos cosas: lo que tienen solo A, lo que tienen solo B y lo que comparten. Una línea de tiempo (timeline) ordena hechos por fecha o paso. Un cuadro de causa y efecto (cause and effect) muestra qué ocurrió y por qué.",
        "Elige el organizador según el texto. Si el texto compara apps y clases, usa Venn. Si cuenta los pasos de una carta, usa una línea de tiempo con first, second, third. Si explica por qué las plantas necesitan luz, usa causa y efecto con la palabra as a result. Completa el organizador con palabras clave, no oraciones completas.",
        "Al terminar, relee el organizador y compáralo con el texto. Comprueba que cada dato aparece en el texto y que no falta ninguna idea importante. Un organizador bien hecho te permite explicar el texto sin mirarlo.",
    ],
    [("graphic organizer", "organizador gráfico"), ("Venn diagram", "diagrama de Venn: compara dos cosas"), ("timeline", "línea de tiempo"), ("cause and effect", "causa y efecto"), ("answer the questions", "responder las preguntas"), ("reread", "releer")],
    [
        ("Completar un Venn", OR1 + " ¿Qué va en cada parte de un diagrama de Venn de apps y clases?", ["Solo apps: barata y flexible.", "Solo clases: más caras, horario fijo y comentarios del profesor.", "Ambas: necesitan práctica regular."], "Apps: baratas y flexibles. Clases: más caras, horario fijo y comentarios del profesor. Ambas: práctica regular"),
        ("Causa y efecto", OR3 + " ¿Cuál es la causa y cuál el efecto?", ["Causa: la planta recibe poca luz.", "Efecto: crece lentamente y sus hojas se ponen pálidas.", "As a result lo confirma."], "Causa: poca luz; efecto: crece lento y sus hojas se ponen pálidas"),
    ],
    [
        ("Copiar el texto completo en el organizador.", "Un organizador usa palabras clave.", "Anota solo lo esencial."),
        ("Usar una línea de tiempo para comparar dos cosas.", "Una línea de tiempo ordena pasos; para comparar se usa un Venn.", "Elige el organizador según la relación."),
    ],
    [
        mc("¿Qué organizador sirve para comparar dos cosas?", "Un diagrama de Venn", ["Una línea de tiempo", "Un cuadro de causa y efecto"], "El Venn muestra diferencias y semejanzas."),
        mc("¿Qué organizador sirve para ordenar los pasos de una carta?", "Una línea de tiempo", ["Un diagrama de Venn", "Un cuadro de causa y efecto"], "Los pasos tienen orden."),
        mr(OR2, "¿Cuál es el último paso?", "El cartero entrega la carta", ["Se escribe la carta", "Se clasifica la carta en la oficina"], "Finally, a mail carrier delivers it."),
    ],
    [
        mr(OR2, "¿Cuál es el segundo paso?", "Llevarla a la oficina de correos", ["Escribirla y ponerla en un sobre", "Clasificarla"], "Second, you take it to the post office."),
        mr(OR1, "¿Qué comparten las apps y las clases?", "Necesitan práctica regular", ["Cuestan lo mismo", "Tienen horario fijo"], "Dice Both need regular practice."),
        mr(OR3, "¿Dónde crece más verde una planta?", "Cerca de una ventana", ["En un rincón oscuro", "Bajo la tierra"], "Dice a plant near a window is often greener."),
    ],
    [
        mr(OR4, "En una línea de tiempo con las semanas, ¿qué ocurre en la semana 3?", "Se hizo un afiche", ["Se vendieron sándwiches", "Se contó dinero"], "Week 3: we made a poster."),
        mr(OR1, "¿Qué cuadro de causa y efecto sirve para explicar que las clases cuestan más?", "Causa: hay profesor y comentarios; efecto: cuestan más", ["Causa: son baratas y flexibles; efecto: se usan más que las clases", "Causa: son apps; efecto: son flexibles y baratas"], "El texto relaciona costo y servicio."),
        arith("En un diagrama de Venn de las apps y las clases pones 2 palabras clave en la zona «solo apps», 3 en «solo clases» y 1 en «ambas». ¿Cuántas palabras clave escribes en total?", "2+3+1", "Se suman las palabras de las tres zonas.", " palabras"),
    ],
    [
        mr(OR3, "Un lector dice que la causa es que la planta está en la ventana. ¿Qué responde alguien que lee con cuidado?", "La causa es la poca luz, no la ventana", ["Tiene razón: la ventana la pone pálida", "Las hojas no cambian"], "La poca luz es la causa de las hojas pálidas."),
        mr(OR1, "Un lector dice que las apps son mejores porque son baratas. ¿Qué dato del texto es más completo?", "Cada una tiene ventajas distintas", ["Las apps ofrecen comentarios del profesor", "Las clases son peores"], "El texto compara y no dice cuál es mejor: las clases dan comentarios del profesor."),
    ],
    [
        mr(OR2 + " " + OR4, "Los dos textos usan secuencia. ¿Qué organizador sirve para ambos?", "Una línea de tiempo", ["Un Venn", "Un cuadro de causa y efecto"], "Ambos ordenan pasos."),
        mc("Antes de leer te preguntaste «How does a letter travel?». Después de leer, ¿qué haces?", "Compruebo si respondí mi pregunta", ["Olvido la pregunta", "Escribo otra pregunta"], "Cierra el ciclo: comprueba y, si falta, relee."),
    ],
    [mr(OR3, "Completa un organizador de causa y efecto con una cadena: poca luz → ¿? → ¿?", "Poca luz → crece lento → hojas pálidas", ["Poca luz → crece rápido → hojas verdes", "Poca luz → no pasa nada → nada"], "Sigue los hechos del texto.")],
    [
        ("En Inglés de 2.º medio (OA 12, clase 4): ¿qué organizador compara dos cosas?", "Un diagrama de Venn", "Muestra lo que tienen en común y lo distinto."),
        ("En Inglés de 2.º medio (OA 12, clase 4): ¿qué organizador ordena pasos?", "Una línea de tiempo", "Marca el orden."),
        ("En Inglés de 2.º medio (OA 12, clase 4): ¿qué se escribe en un organizador?", "Palabras clave", "No se copia el texto."),
    ],
    task("Lee: «Two Neighborhood Parks (fictional). Park Norte has a playground and a track. Park Sur has a playground and a lake. Both have benches and trees, but Park Sur has fewer trees.» (playground = patio de juegos, track = pista, lake = laguna, benches = bancas). Haz un diagrama de Venn con las dos zonas y escribe dos frases que expliquen lo que aprendiste.", "Solo Norte: pista. Solo Sur: laguna y menos árboles. Ambos: patio de juegos, bancas y árboles. Frases: Both parks have a playground. Park Sur has a lake.", ["completa las tres partes del Venn", "usa palabras clave", "escribe dos frases"], ["Venn en la hoja", "dos frases en la hoja"], ["poner un dato en la zona equivocada", "copiar oraciones completas"], "Pide que explique qué zona del Venn cambió si Park Norte tuviera también una laguna."),
    "Lee un texto de otra asignatura y haz un organizador con palabras clave.",
    "Dibuja una línea de tiempo en español con los pasos de tu mañana.",
)

# ------------------------------------------------------------------ clase 5: recontar, resumir y preguntar para confirmar
RS1 = "«The Library Cat (original). In the town of Brightfield, a gray cat named Pepper began to visit the library every morning. Readers petted him, and children read aloud to him. When the library closed for repairs, Pepper waited at the door for two weeks. When it reopened, he walked in as if nothing had happened, and the librarian gave him a warm cushion.» (library = biblioteca, gray = gris, petted = acariciaban, read aloud = leían en voz alta, repairs = reparaciones, waited = esperó, reopened = reabrió, as if = como si, cushion = cojín)"
RS3 = "«A New Rule for Phones (fictional). The school decided that phones must stay in lockers during lessons. Students may use them at lunch and after school. Most teachers like the rule, but some students say it is unfair. The principal will review the rule in June.» (rule = regla, lockers = casilleros, lessons = clases, unfair = injusta, review = revisar, principal = director)"

lesson(
    OA, 5, MAT_R,
    "Aprenderé a recontar un texto con mis palabras, a resumirlo y a preguntar para confirmar información. Sirve para comprobar que entendí y para explicar lo leído a otras personas.",
    ["Sé usar organizadores gráficos.", "Sé releer y plantearme preguntas."],
    [
        "Recontar (retelling) es contar con tus propias palabras lo que pasó o lo que dice el texto, en orden. Usa first, then, after that y finally, y mantén los personajes y hechos principales. Resumir (summarizing) es decir solo lo esencial en pocas oraciones: quién, qué, cuándo, dónde y por qué, sin detalles pequeños ni opiniones propias. Un resumen suele tener dos o tres oraciones.",
        "Para resumir, sigue tres pasos. Primero, subraya las ideas principales. Segundo, tacha los detalles que no cambian el sentido. Tercero, escribe con tus palabras, con conectores simples. Por ejemplo: Pepper, a cat, visited the Brightfield library every morning. When it closed, he waited at the door, and when it reopened, he returned.",
        "Para confirmar información, pregunta y comprueba en el texto: Did Pepper wait at the door for two weeks? Who gave him a cushion? Is it true that the rule is for the whole school? Responde Yes o No y señala la frase del texto que lo prueba. Si no está en el texto, la respuesta es: the text doesn't say.",
    ],
    [("retell", "recontar"), ("summarize", "resumir"), ("main idea", "idea principal"), ("confirm", "confirmar"), ("the text doesn't say", "el texto no lo dice"), ("in my own words", "con mis propias palabras")],
    [
        ("Resumir en dos oraciones", RS1 + " Resume el texto en dos oraciones.", ["Subrayo: Pepper, visits the library, waits during repairs, returns.", "Quito detalles como el cojín.", "Escribo: A cat named Pepper visited the Brightfield library every day. When it closed, he waited, and he returned when it reopened."], "A cat named Pepper visited the Brightfield library every day. When it closed, he waited, and he returned when it reopened"),
        ("Preguntar para confirmar", RS3 + " ¿Es verdad que los estudiantes pueden usar el teléfono en el almuerzo?", ["Busco la parte del almuerzo.", "Dice may use them at lunch and after school.", "Respondo Yes y cito la frase."], "Yes: dice that students may use them at lunch and after school"),
    ],
    [
        ("Incluir opiniones propias en el resumen.", "Un resumen dice lo que el texto dice, no lo que tú piensas.", "Escribe solo las ideas principales del texto."),
        ("Responder Yes sin comprobar en el texto.", "Puede ser algo que no dice.", "Busca la frase que lo confirma o responde the text doesn't say."),
    ],
    [
        mr(RS1, "¿Cuántas semanas esperó Pepper en la puerta?", "Dos semanas", ["Una semana entera", "Un mes"], "Dice waited at the door for two weeks."),
        mr(RS3, "¿Quién revisará la regla en junio?", "El director", ["Los profesores", "Los padres"], "Dice The principal will review the rule in June."),
        mc("¿Qué debe hacer un resumen?", "Decir solo lo esencial con tus palabras", ["Copiar frases del texto", "Agregar tu opinión"], "Resume sin detalles pequeños ni opinión."),
    ],
    [
        mr(RS1, "¿Qué hicieron los niños con Pepper?", "Le leían en voz alta", ["Le daban de comer en la puerta", "Lo llevaban a casa"], "Dice children read aloud to him."),
        mr(RS3, "¿Qué piensan algunos estudiantes de la regla?", "Que es injusta", ["Que es perfecta y no hay que cambiarla", "Que es corta"], "Dice some students say it is unfair."),
        mr(RS1, "¿Qué recibió Pepper al final?", "Un cojín cálido", ["Un hueso de juguete", "Un libro nuevo"], "Dice the librarian gave him a warm cushion."),
    ],
    [
        mr(RS1, "Elige el mejor recuento en orden: ¿cuál es?", "First, Pepper visited the library. Then it closed and he waited. Finally, it reopened.", ["First, Pepper waited at the door. Then he visited the library. Finally, the library closed.", "Pepper liked cushions and children."], "Respeta el orden de los hechos."),
        mr(RS3, "Elige el mejor resumen: ¿cuál es?", "Phones must stay in lockers during lessons, but may be used at lunch.", ["The school decided that students may use phones all day, but only in lockers.", "Most students are happy with the rule."], "Resume la regla con las excepciones."),
        mr(RS3, "Confirma: Did the principal change the rule in May? ¿Cuál es la respuesta?", "The text doesn't say", ["Yes, the principal changed it in May", "No, never"], "El texto solo dice que la revisará en junio; no habla de mayo."),
    ],
    [
        mr(RS1, "Un compañero resume: «Pepper is a dog that lived in the library». ¿Qué corriges?", "Pepper es un gato, no un perro", ["Nada: el resumen es correcto", "Pepper vivía en la escuela"], "El texto dice a gray cat named Pepper."),
        mr(RS3, "Otro compañero resume: «Everyone likes the rule». ¿Qué corriges?", "No todos están de acuerdo: algunos estudiantes la critican", ["Nada: todos los estudiantes y profesores están de acuerdo", "Nadie conoce la regla"], "Most teachers like the rule, but some students say it is unfair."),
    ],
    [
        mr(RS1, "Confirma: Is it true that Pepper wanted to leave the town? ¿Cuál es la respuesta?", "The text doesn't say about that", ["Yes, he wanted to leave", "No, he never wanted to go"], "No hay pistas de que quiera irse."),
        mr(RS3, "¿Cuál es una pregunta de confirmación que se puede comprobar en el texto?", "Do students use phones at lunch?", ["Why do students love phones so much?", "Will phones be banned?"], "Se responde con una frase del texto: may use them at lunch."),
    ],
    [arith("Pepper esperó en la puerta dos semanas mientras la biblioteca estaba cerrada, y cada semana tiene 7 días. ¿Cuántos días esperó?", "2*7", "Se multiplican las semanas por los días de cada semana.", " días")],
    [
        ("En Inglés de 2.º medio (OA 12, clase 5): ¿qué diferencia hay entre recontar y resumir?", "Recontar cuenta todo en orden con tus palabras; resumir dice solo lo esencial", "El resumen es más corto."),
        ("En Inglés de 2.º medio (OA 12, clase 5): ¿qué respondes si el texto no da el dato?", "The text doesn't say", "Así no inventas."),
        ("En Inglés de 2.º medio (OA 12, clase 5): ¿qué incluye un resumen?", "Quién, qué, cuándo, dónde y por qué", "Son las ideas esenciales."),
    ],
    task("Lee: «The Seed Fair (fictional). Every autumn, the town of Valle holds a fair in the main square. Local farmers sell seeds, school groups plant small gardens and children paint flower pots with bright colors. The mayor says the fair brings visitors from other towns, and shops report more sales.» (fair = feria, farmers = agricultores, seeds = semillas, square = plaza, gardens = jardines, flower pots = macetas, mayor = alcalde, shops = tiendas, sales = ventas). Haz tres cosas: recuenta en tres oraciones, resume en una oración y formula una pregunta para confirmar un dato.", "Recuento: Every autumn, Valle holds a fair in the main square. Farmers sell seeds. School groups plant gardens and children paint flower pots. Resumen: Valle holds an autumn fair that brings visitors and more sales. Pregunta: Do children paint flower pots?", ["recuenta con tus palabras y en orden", "resume en una oración", "formula una pregunta de confirmación"], ["hoja con tres respuestas"], ["incluir opiniones propias", "copiar frases del texto"], "Pide que cambie un dato del texto y compruebe si la pregunta de confirmación cambia."),
    "Resume un cuento que leíste en una oración con quién, qué y por qué.",
    "Pide a una persona de tu casa que te cuente algo que leyó y haz dos preguntas para confirmar.",
)
