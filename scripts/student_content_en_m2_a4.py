"""Cuaderno del estudiante, 2.º medio Inglés (propuesta), EN2M OA 04: lectura y comprensión de textos literarios y no literarios.

Todos los textos son originales, breves y ficticios, con pista en español. Los títulos de clase del plan son genéricos;
aquí cada clase recorre un grupo de textos del OA: poemas y tiras cómicas; cuentos, mitos y obras dramáticas; artículos,
noticias y reseñas; correos, catálogos, gráficos y biografías; y el lenguaje (collocations, conectores, prefijos im-, in-, il-).
Las obras reales quedan para el docente: aquí no se reproduce ninguna. Los datos de gráficos y biografías son «de ejemplo».
"""
from __future__ import annotations

from en_m2_a_common import MAT_READ, arith, lesson, task

OA = "EN2M OA 04"

# ================================================== clase 1: poemas y tiras cómicas
POEM = "«The Last Bus\nThe bus is late, the street is blue,\nthe lamp is tired, and so are you.\nA dog walks by with a sleepy face,\nand the night folds up the day’s last space.\nThen light, then noise, then wheels that sing:\nthe bus is here. What joy it brings!»\n(late = tarde, lamp = farol, tired = cansado, sleepy = soñoliento, folds up = pliega, wheels = ruedas, sing = cantan, joy = alegría)"
COMIC = "Tira cómica (tres cuadros). Cuadro 1: Una chica con una mochila grande dice: «I forgot my homework!» Cuadro 2: Su amigo responde: «Again? What is your excuse today?» Cuadro 3: La chica, sonriendo, saca su cuaderno y dice: «Surprise! I found it.» (homework = tarea, excuse = excusa, surprise = sorpresa, found = encontré)"
POEM2 = "«Morning\nThe kettle sings, the window glows,\nthe cat sleeps on my two warm toes.\nSoon I will run, I will not stay,\nbut for one minute, I will play.»\n(kettle = tetera, glows = brilla, toes = dedos del pie, stay = quedarse)"

lesson(
    OA, 1, MAT_READ,
    "Aprenderé a leer poemas y tiras cómicas y a identificar su tema, su propósito, sus personajes y las palabras clave que lo muestran. Sirve para entender qué siente o qué cuenta un texto literario breve sin traducirlo palabra por palabra.",
    ["Sé reconocer un verso y una estrofa.", "Sé que una tira cómica cuenta una historia en cuadros."],
    [
        "Un poema (poem) se organiza en versos (lines) y a veces en estrofas (stanzas). Muchos poemas usan rima (rhyme): palabras que terminan con sonidos parecidos, como blue y you. El tema (theme) es la idea central, por ejemplo la espera o la alegría. El tono (tone) es la actitud del texto: serio, cansado, alegre o divertido. Las palabras clave son las que repiten o describen esa idea.",
        "Una tira cómica (comic strip) cuenta una historia breve con cuadros, personajes (characters) y diálogos. Su propósito suele ser entretener y mostrar una situación con humor. El humor aparece muchas veces en el último cuadro, donde ocurre una sorpresa. Para entenderla, lee los globos de diálogo en orden y mira cómo cambia la actitud del personaje de un cuadro al siguiente.",
        "Para comprender un texto literario, haz tres preguntas: ¿quién habla o actúa?, ¿qué ocurre o qué se siente? y ¿qué palabras lo muestran? Anota dos palabras clave con su apoyo en el texto. Si una palabra es nueva, usa el contexto y las imágenes. No necesitas traducir todo; basta con entender la idea y el tono.",
    ],
    [("poem", "poema"), ("rhyme", "rima: sonidos finales parecidos"), ("theme", "tema: idea central"), ("tone", "tono: actitud del texto"), ("comic strip", "tira cómica"), ("character", "personaje")],
    [
        ("Rima", "Poema corto: «The kettle sings, the window glows». ¿Qué palabra rima con glows? A) toes B) kettle", ["Busco una palabra que termine con sonido parecido.", "Glows y toes terminan en el mismo sonido.", "Kettle no termina igual."], "A) toes"),
        ("Tono de una tira", COMIC + " ¿Qué tono tiene la tira? A) divertido B) triste", ["Miro el último cuadro.", "La chica encuentra la tarea y dice Surprise!", "El tono es divertido."], "A) divertido"),
    ],
    [
        ("Creer que un poema debe entenderse palabra por palabra.", "Se pierde la idea central y el tono.", "Busca primero el tema y las palabras que se repiten."),
        ("Leer los globos de diálogo en desorden.", "Se cambia la historia de la tira cómica.", "Sigue los cuadros de izquierda a derecha y de arriba abajo."),
    ],
    [
        ("Lee: " + POEM + " ¿Qué palabra rima con blue? A) you B) bus", "A", "Blue y you terminan con el mismo sonido."),
        ("Lee: " + COMIC + " ¿Qué se olvidó la chica? A) su tarea B) su mochila", "A", "Dice I forgot my homework!"),
        ("Lee: " + POEM2 + " ¿Dónde duerme el gato? A) sobre los dedos del pie B) en la ventana", "A", "El poema dice the cat sleeps on my two warm toes."),
    ],
    [
        ("Lee: " + POEM + " ¿Cuál es el tema del poema? A) la espera de un bus en la noche B) un paseo de verano", "A", "Los versos hablan de un bus tarde, de la calle azul y de la espera."),
        ("Lee: " + COMIC + " ¿Qué dice el amigo? A) Again? What is your excuse today? B) Surprise!", "A", "El amigo duda en el segundo cuadro; la sorpresa es de la chica."),
        ("Lee: " + POEM2 + " ¿Qué actitud tiene quien habla al final? A) quiere jugar un minuto antes de salir B) quiere quedarse dormido", "A", "Los versos dicen I will not stay, but for one minute, I will play."),
    ],
    [
        ("Lee: " + POEM + " ¿Qué palabra muestra la alegría del final? A) joy B) late", "A", "La palabra joy aparece cuando llega el bus."),
        ("Lee: " + COMIC + " ¿En qué cuadro aparece la sorpresa? A) en el tercero B) en el primero", "A", "En el tercero la chica saca el cuaderno."),
        ("Lee: " + POEM2 + " ¿Cuántos versos tiene el poema Morning? Cuéntalos sin contar el título.", "4", "Hay cuatro líneas: kettle, cat, soon y but."),
    ],
    [
        ("Lee: " + POEM + " ¿Qué pista muestra que el poema es cansado antes de la llegada del bus? A) the lamp is tired, and so are you B) the bus is here", "A", "La frase describe el cansancio de la noche; la segunda es el final."),
        ("Lee: " + COMIC + " Un compañero dice que la tira es seria. ¿Qué pista lo contradice? A) el último cuadro tiene una sorpresa con una sonrisa B) la chica carga una mochila", "A", "El humor aparece en la sorpresa final."),
    ],
    [
        ("Lee: " + POEM2 + " ¿Qué pareja de palabras NO rima? A) glows y stay B) stay y play", "A", "Stay y play terminan igual; glows y stay no."),
        ("Lee: " + POEM + " Ordena las ideas del poema: a) llega el bus b) un perro pasa c) el bus se atrasa", "c, b, a", "Primero el bus tarda, luego pasa el perro y al final llega el bus."),
    ],
    [("Lee: «Monday: sun. Tuesday: cloud. Wednesday: I forget my umbrella. Thursday: rain!» (cloud = nube, umbrella = paraguas, forget = olvidar). Es un mini poema humorístico. ¿Qué día llueve?", "El jueves", "El último verso dice Thursday: rain!")],
    [
        ("¿Qué es una rima (en Inglés, 2.º medio)?", "Palabras que terminan con sonidos parecidos", "Por ejemplo, blue y you."),
        ("¿Dónde suele estar el humor en una tira cómica?", "En el último cuadro", "Allí ocurre la sorpresa."),
        ("¿Qué es el tono (en Inglés, 2.º medio)?", "La actitud del texto", "Puede ser alegre, serio o divertido."),
    ],
    task("Lee este poema original: «Rainy Day\nThe window drums, the roof is loud,\nI watch a slow, grey, travelling cloud.\nMy tea is warm, my book is near,\nthe rain is here and I am here.» (drums = tamborilea, roof = techo, loud = ruidoso, grey = gris, travelling = viajera, tea = té, near = cerca). En tu hoja escribe: el tema, el tono, una pareja de palabras que rimen y dos palabras clave que apoyen tu respuesta.", "Tema: un día de lluvia en casa. Tono: tranquilo y acogedor. Rimas: loud y cloud, o near y here. Palabras clave: rain, tea, warm, book.", ["dice el tema con una palabra clave", "identifica una rima correcta", "describe el tono con un apoyo del texto"], ["hoja con cuatro respuestas"], ["decir que el tono es triste sin dar una palabra clave", "escribir una rima que no aparece"], "Compara con una persona de tu casa qué palabras sintieron calmadas y cuáles ruidosas."),
    "Vuelve a leer el poema The Last Bus y subraya las dos palabras que muestran cansancio.",
    "Escribe una tira cómica de tres cuadros en español sobre un olvido y marca dónde está el humor.",
)

# ================================================== clase 2: cuentos, mitos y obras dramáticas
STORY = "«Mira and the Silent Lighthouse\nOnce, in a small harbour town, there was a lighthouse that never shone. The people said it was broken. Mira, a young girl who liked to repair clocks, climbed the stairs one winter evening. At the top she found a loose cable. She fixed it, and the light turned on. That night, a fishing boat that was lost in the fog saw the light and came home safely. From then on, the town called her ‘Mira of the light’.»\n(harbour = puerto, lighthouse = faro, shone = brilló, broken = descompuesto, repair = reparar, clocks = relojes, stairs = escaleras, loose cable = cable suelto, fog = niebla, safely = a salvo)"
MYTH = "«The Two Rivers (a short original legend)\nLong ago, two rivers lived on the same mountain. One was fast and loud; the other was slow and quiet. They argued about who was better. A wise bird said: ‘The fast river brings storms to the valley, and the slow river brings food. You both need each other.’ The rivers stopped arguing, and they met at the bottom of the mountain.»\n(rivers = ríos, loud = ruidoso, argued = discutieron, wise = sabio, storms = tormentas, valley = valle, need each other = se necesitan)"
SCENE = "«Scene: a school corridor. Characters: Lola (16) and Mr. Pérez, the teacher.\nLOLA: [nervous] Excuse me, Mr. Pérez, may I speak to you?\nMR. PÉREZ: Of course. What is wrong?\nLOLA: I lost the group’s project folder.\nMR. PÉREZ: [calm] Take a deep breath. When did you last see it?\nLOLA: At lunch, in the library.\nMR. PÉREZ: Then let’s look there together.»\n(corridor = pasillo, nervous = nerviosa, folder = carpeta, calm = tranquilo, deep breath = respiración profunda, lunch = almuerzo)"

lesson(
    OA, 2, MAT_READ,
    "Aprenderé a identificar los personajes, el entorno, la trama (inicio, desarrollo y final) y el conflicto en un cuento, una leyenda breve y una obra dramática adaptada. Sirve para comprender una historia y explicar qué la hace avanzar.",
    ["Sé reconocer el tema y el tono de un texto literario.", "Sé el pasado simple de verbos comunes."],
    [
        "Un cuento (short story) tiene personajes (characters), que son quienes actúan, y un entorno (setting), que es el tiempo y el lugar. La trama (plot) tiene tres partes: inicio (beginning), donde se presenta la situación; desarrollo (middle), donde ocurren los hechos; y final (end), donde se resuelve. El conflicto (conflict) es el problema que mueve la historia: puede ser entre personajes, con la naturaleza o dentro de la persona.",
        "Una leyenda o mito breve explica algo con una historia y suele terminar con una enseñanza (lesson). Una obra dramática (play) se escribe en diálogos: el nombre del personaje va en mayúsculas y las acotaciones, entre corchetes, indican cómo habla o actúa. La escena (scene) dice el lugar y los personajes. En el drama no hay narrador; todo se sabe por lo que dicen y hacen los personajes.",
        "Al leer, marca con un color los personajes y el lugar, con otro el problema y con otro la solución. Pregúntate: ¿qué quiere el personaje?, ¿qué se lo impide? y ¿cómo se resuelve? Usa verbos en pasado (found, fixed, saw) para ordenar los hechos. Las palabras como once, then, that night y from then on te ayudan a ver el orden.",
    ],
    [("character", "personaje"), ("setting", "entorno: lugar y tiempo"), ("plot", "trama: inicio, desarrollo y final"), ("conflict", "conflicto: problema de la historia"), ("lesson", "enseñanza o moraleja"), ("stage direction", "acotación: indicación entre corchetes en una obra de teatro")],
    [
        ("Personaje y problema", "Lee: «Pablo wanted to join the school band, but he was afraid to play in front of people.» (join = unirse, afraid = con miedo). ¿Cuál es el conflicto?", ["El personaje quiere unirse a la banda.", "Pero tiene miedo de tocar frente a otros.", "El miedo es el conflicto."], "El miedo a tocar frente a la gente"),
        ("Entorno", "Lee: «It was a rainy night in a small station.» (rainy = lluvioso, station = estación). ¿Cuál es el entorno?", ["Busco tiempo y lugar.", "El tiempo es una noche de lluvia.", "El lugar es una estación pequeña."], "Una noche lluviosa, en una estación pequeña"),
    ],
    [
        ("Decir que el entorno es solo el lugar.", "El entorno incluye también el tiempo.", "Anota dónde y cuándo ocurre la historia."),
        ("Confundir el final con la última frase que se lee.", "El final es la resolución del conflicto.", "Pregúntate cómo se resuelve el problema."),
    ],
    [
        ("Lee: " + STORY + " ¿Quién es la protagonista? A) Mira B) un pescador", "A", "El cuento se titula Mira and the Silent Lighthouse y ella actúa."),
        ("Lee: " + MYTH + " ¿Qué dos personajes principales tiene la leyenda? A) dos ríos B) dos montañas", "A", "Dice two rivers lived on the same mountain."),
        ("Lee: " + SCENE + " ¿Dónde ocurre la escena? A) en un pasillo del colegio B) en una biblioteca", "A", "Scene: a school corridor."),
    ],
    [
        ("Lee: " + STORY + " ¿Cuál es el conflicto al inicio? A) el faro no funcionaba B) el pueblo no tenía puerto", "A", "Dice there was a lighthouse that never shone."),
        ("Lee: " + MYTH + " ¿Qué problema tienen los ríos? A) discuten sobre cuál es mejor B) no tienen nombre", "A", "Dice They argued about who was better."),
        ("Lee: " + SCENE + " ¿Qué perdió Lola? A) la carpeta del proyecto del grupo B) su mochila", "A", "Dice I lost the group’s project folder."),
    ],
    [
        ("Lee: " + STORY + " ¿Cómo se resuelve el conflicto? A) Mira arregla un cable suelto y el faro se enciende B) los vecinos construyen otro faro", "A", "Dice She fixed it, and the light turned on."),
        ("Lee: " + MYTH + " ¿Qué enseñanza deja el ave sabia? A) que los dos ríos se necesitan B) que el río rápido es mejor", "A", "Dice You both need each other."),
        ("Lee: " + SCENE + " ¿Qué pregunta le hace Mr. Pérez para ayudarla? A) When did you last see it? B) Who took it?", "A", "El profesor pregunta cuándo la vio por última vez."),
    ],
    [
        ("Lee: " + STORY + " ¿Por qué el barco volvió a casa? A) vio la luz del faro en la niebla B) escuchó una campana", "A", "Dice saw the light and came home safely."),
        ("Lee: " + SCENE + " Mr. Pérez dice «Take a deep breath». ¿Qué muestra de su carácter? A) que es calmado B) que está enojado", "A", "La acotación calm y su frase muestran tranquilidad."),
    ],
    [
        ("Lee: " + STORY + " Ordena los hechos: a) Mira repara el cable b) el barco vuelve a casa c) Mira sube las escaleras", "c, a, b", "Primero sube, luego repara y después el barco vuelve."),
        ("Lee: " + MYTH + " ¿Cuál es el final de la leyenda? A) los ríos dejan de discutir y se juntan abajo de la montaña B) el pájaro se va lejos", "A", "Dice The rivers stopped arguing, and they met at the bottom."),
    ],
    [("Lee: «Tomás wanted to give a speech, but he was afraid. He practised in front of the mirror each night. On the big day, he spoke for three minutes and everyone clapped.» (speech = discurso, mirror = espejo, clapped = aplaudió). ¿Cuántos minutos habló Tomás?", "3", "El texto dice for three minutes.")],
    [
        ("¿Qué es el conflicto de una historia (en Inglés, 2.º medio)?", "El problema que mueve la historia", "Es lo que los personajes deben resolver."),
        ("¿Qué indican las acotaciones en una obra de teatro?", "Cómo habla o actúa un personaje", "Van entre corchetes."),
        ("¿Cuáles son las tres partes de la trama?", "Inicio, desarrollo y final", "Se leen en ese orden."),
    ],
    task("Lee esta escena original: «Scene: a bus stop. Characters: Daniel and Elisa.\nDANIEL: [worried] The last bus has gone.\nELISA: [calm] Don’t worry. I have an idea. We can call my brother.\nDANIEL: [relieved] Thank you! I was afraid to walk alone.\nELISA: [smiling] Friends help friends.» (worried = preocupado, relieved = aliviado, alone = solo). En tu hoja escribe: personajes, entorno, conflicto, solución y la enseñanza.", "Personajes: Daniel y Elisa. Entorno: un paradero. Conflicto: se fue el último bus y Daniel teme caminar solo. Solución: llamar al hermano de Elisa. Enseñanza: los amigos se ayudan.", ["nombra personajes y entorno", "dice el conflicto y la solución", "escribe la enseñanza con una pista del texto"], ["hoja con cinco respuestas"], ["decir que el conflicto es la enseñanza", "inventar personajes que no están en la escena"], "Comparte tu respuesta con una persona de tu casa y pregúntale si el conflicto está bien dicho."),
    "Relee el cuento de Mira y escribe en una frase de diez palabras qué problema se resolvió.",
    "Escribe en español el inicio, el desarrollo y el final de una historia breve sobre una ayuda inesperada.",
)

# ================================================== clase 3: artículos, noticias, reseñas
NEWS = "«New Bike Lanes Open in Riverton (fictional)\nThe city of Riverton opened four kilometres of new bike lanes on Friday. The mayor said that the lanes would make streets safer. Last year, there were many accidents near the main square. As a result, the council decided to separate bikes from cars. Cyclists say they feel safer, though some drivers complain about less parking. The council will review the plan in six months.»\n(bike lanes = ciclovías, kilometres = kilómetros, safer = más seguras, accidents = accidentes, council = municipio, separate = separar, cyclists = ciclistas, complain = quejarse, parking = estacionamiento, review = revisar)"
REVIEW = "«Review: The Moonlight Cafe\nI visited this cafe on Saturday. The place is small and quiet, with soft music and good lighting. The hot chocolate was excellent, but the sandwich was cold. The staff were friendly, though the service was slow. I recommend it for reading or studying, not for a quick lunch. My rating: 3 out of 5.»\n(cafe = cafetería, quiet = tranquila, lighting = iluminación, hot chocolate = chocolate caliente, cold = frío, staff = personal, friendly = amable, slow = lento, recommend = recomendar, rating = puntuación)"
PAGE = "«Safe Online Habits: a school web page\nWhy it matters: many students use the internet every day. The main problem is that people share too much personal information. Our advice: use strong passwords, do not share them, and ask an adult if something feels strange. Remember: if a message asks for private data, do not answer.»\n(habits = hábitos, matters = importa, share = compartir, advice = consejo, passwords = contraseñas, strange = extraño, private data = datos privados)"

lesson(
    OA, 3, MAT_READ,
    "Aprenderé a leer artículos, noticias, reseñas y páginas web, e identificar su propósito, la idea principal, los datos específicos, la importancia de las ideas y la relación problema-solución. Sirve para informarme y opinar con evidencia del texto.",
    ["Sé reconocer personajes y trama en un texto literario.", "Sé buscar who, what, where y when en un texto."],
    [
        "Los textos no literarios entregan información real. Una noticia (news article) cuenta un hecho reciente y responde quién, qué, dónde, cuándo y por qué. Una reseña (review) da una opinión sobre algo y suele terminar con una recomendación o puntuación. Una página web (web page) usa títulos y listas para que encuentres información rápido. Cada texto tiene un propósito: informar, opinar o aconsejar.",
        "La idea principal (main idea) es lo más importante que dice el texto; los detalles (details) la apoyan con datos, cifras o ejemplos. Para encontrarla, lee el título y la primera frase de cada párrafo. Las relaciones entre ideas se ven con los conectores: as a result muestra una consecuencia, though marca un contraste y because da una causa. El problema (problem) y la solución (solution) suelen aparecer juntos: Last year there were many accidents… the council decided to separate bikes from cars.",
        "Para resumir, anota la idea principal en una oración y tres detalles con datos. Diferencia un hecho (fact), que se puede comprobar, de una opinión (opinion), que expresa lo que alguien piensa, como The service was slow o I recommend it. Una reseña mezcla hechos y opiniones; una noticia debería dar sobre todo hechos.",
    ],
    [("news article", "noticia"), ("review", "reseña: opinión sobre algo"), ("main idea", "idea principal"), ("fact", "hecho: se puede comprobar"), ("opinion", "opinión: lo que alguien piensa"), ("problem-solution", "relación problema-solución")],
    [
        ("Hecho u opinión", "Frase: «The cafe opens at eight.» ¿Es un hecho o una opinión? A) un hecho B) una opinión", ["Se puede comprobar con un horario.", "No expresa lo que alguien piensa.", "Es un hecho."], "A) un hecho"),
        ("Problema y solución", "Texto: «Many students arrived late, so the school started a breakfast club at seven thirty.» (arrived late = llegaron tarde). ¿Cuál es la solución?", ["El problema es llegar tarde.", "La frase con so dice qué se hizo.", "La solución es el club de desayuno."], "Crear un club de desayuno a las siete y media"),
    ],
    [
        ("Elegir un detalle como idea principal.", "La idea principal resume todo el texto.", "Lee el título y la primera frase de cada párrafo."),
        ("Creer que toda reseña es un hecho.", "Una reseña expresa opiniones.", "Busca palabras como excellent, slow o I recommend."),
    ],
    [
        ("Lee: " + NEWS + " ¿Cuántos kilómetros de ciclovías abrieron? A) cuatro B) seis", "A", "El texto dice four kilometres."),
        ("Lee: " + REVIEW + " ¿Qué puntuación da el autor? A) tres de cinco B) cinco de cinco", "A", "Dice 3 out of 5."),
        ("Lee: " + PAGE + " ¿Qué se debe hacer con las contraseñas? A) no compartirlas B) escribirlas en la pizarra", "A", "El texto dice do not share them."),
    ],
    [
        ("Lee: " + NEWS + " ¿Cuál es el propósito del texto? A) informar un hecho reciente B) vender bicicletas", "A", "Es una noticia sobre ciclovías nuevas."),
        ("Lee: " + REVIEW + " ¿Qué opina el autor del servicio? A) que fue lento B) que fue excelente", "A", "Dice the service was slow."),
        ("Lee: " + PAGE + " ¿Cuál es el problema que menciona? A) que se comparte demasiada información personal B) que el internet es lento", "A", "Dice people share too much personal information."),
    ],
    [
        ("Lee: " + NEWS + " ¿Qué consecuencia tuvieron los accidentes? A) el municipio separó las bicicletas de los autos B) cerraron la plaza", "A", "As a result, the council decided to separate bikes from cars."),
        ("Lee: " + REVIEW + " ¿Para qué actividad recomienda la cafetería? A) leer o estudiar B) almorzar rápido", "A", "Dice I recommend it for reading or studying, not for a quick lunch."),
        ("Lee: " + NEWS + " ¿En cuántos meses revisarán el plan? A) seis B) doce", "A", "El texto dice in six months."),
    ],
    [
        ("Lee: " + NEWS + " ¿Cuál es la idea principal? A) Riverton abrió ciclovías para hacer las calles más seguras B) los conductores no tienen estacionamiento", "A", "Los estacionamientos son un detalle; la idea es la apertura de ciclovías."),
        ("Lee: " + REVIEW + " ¿Qué frase es un hecho? A) The author visited the cafe on Saturday. B) The service was slow.", "A", "La visita en sábado se puede comprobar; slow es una opinión."),
    ],
    [
        ("Lee: " + NEWS + " ¿Qué muestra el conector though? A) un contraste entre ciclistas y conductores B) una causa", "A", "Los ciclistas están más seguros, aunque algunos conductores se quejan."),
        ("Lee: " + PAGE + " Ordena los consejos según el texto: a) preguntar a un adulto b) usar contraseñas fuertes c) no responder si piden datos privados", "b, a, c", "El texto los nombra en ese orden."),
    ],
    [("Lee: «The school library now opens at seven forty-five instead of eight thirty. As a result, students can borrow books before class.» (instead of = en vez de, borrow = pedir prestado). ¿A qué hora abre ahora?", "A las 7:45", "El texto dice opens at seven forty-five.")],
    [
        ("¿Qué diferencia hay entre un hecho y una opinión (en Inglés, 2.º medio)?", "El hecho se puede comprobar; la opinión expresa lo que alguien piensa", "Las reseñas contienen opiniones."),
        ("¿Qué muestra el conector as a result?", "Una consecuencia", "Une la causa con su efecto."),
        ("¿Dónde se busca la idea principal?", "En el título y en la primera frase de cada párrafo", "Resume el texto."),
    ],
    task("Lee esta noticia original (ficticia): «Students Start a Book Exchange. Students of 2nd year at Lomas High School started a book exchange on Monday. Anyone can bring a book and take another one. In two days, students exchanged sixty books. The teacher in charge, Ms. Rojas, said that reading habits can improve. Some students say that the box is too small, though.» (exchange = intercambio, in charge = a cargo, habits = hábitos, improve = mejorar, box = caja). En tu hoja escribe: el propósito, la idea principal, dos datos exactos y una opinión que aparezca.", "Propósito: informar. Idea: los estudiantes de 2.º medio crearon un intercambio de libros. Datos: 60 libros en dos días; empezó el lunes; Ms. Rojas está a cargo. Opinión: la caja es demasiado pequeña.", ["dice un propósito correcto", "escribe la idea principal sin copiar un detalle", "da dos datos exactos y una opinión"], ["hoja con cuatro respuestas"], ["usar un detalle como idea principal", "decir que la caja pequeña es un hecho"], "Marca en el texto con distintos colores la idea principal, los datos y la opinión."),
    "Relee la reseña de la cafetería y subraya tres opiniones.",
    "Escribe una reseña de cinco oraciones de un lugar de tu barrio con una recomendación.",
)

# ================================================== clase 4: correos, catálogos, gráficos, biografías, discursos
EMAIL = "«From: Pia Soto. To: Mr. Vega. Subject: Request: robotics room on Wednesday.\nDear Mr. Vega, I am writing to ask if our club can use the robotics room on Wednesday at four. We need two hours to test our small robot. Could you please let me know by Tuesday? Thank you. Kind regards, Pia»\n(request = solicitud, test = probar)"
CATALOG = "Catálogo de ejemplo. «Backpack A: price 18000 pesos, colour grey, two pockets, 1-year guarantee. Backpack B: price 25000 pesos, colour blue, five pockets, 2-year guarantee. Lunch box: price 6000 pesos, one colour, no guarantee.» (pockets = bolsillos, guarantee = garantía, lunch box = lonchera)"
GRAPH = "Gráfico de ejemplo (cantidad de estudiantes que eligen cada deporte): football 40, volleyball 25, swimming 15, tennis 10. (football = fútbol, volleyball = vóleibol, swimming = natación, tennis = tenis)"
BIO = "Biografía de ejemplo (persona ficticia): «Clara Núñez (born in 1990 in a small town) is an architect. She studied at university for five years. Later, she designed a library with many windows. She says that she wanted people to enjoy reading in natural light. Today she teaches young students.» (architect = arquitecta, designed = diseñó, windows = ventanas, natural light = luz natural, teaches = enseña)"

lesson(
    OA, 4, MAT_READ,
    "Aprenderé a leer correos, catálogos, gráficos, biografías y discursos breves e identificar su propósito, sus datos y las ideas que los unen. Sirve para decidir una compra, entender una cifra o conocer a una persona a partir de un texto.",
    ["Sé reconocer el propósito de un texto.", "Sé leer cifras y tablas simples."],
    [
        "Cada tipo de texto no literario tiene una estructura. Un correo electrónico (email) tiene remitente (From), destinatario (To), asunto (Subject), saludo, cuerpo y cierre; su propósito está en la primera oración del cuerpo. Un catálogo (catalog) lista productos con precio, color y características, y sirve para comparar. Un gráfico (graph) muestra datos con barras o líneas; la cifra más alta señala el mayor valor, y la más baja, el menor.",
        "Una biografía (biography) cuenta la vida de una persona en orden: dónde nació, qué estudió, qué hizo y qué hace hoy. Usa el pasado (studied, designed) y el presente (teaches). Un discurso (speech) busca convencer a un público, con saludo, razones y una invitación a actuar. En todos estos textos, busca primero el propósito, luego la idea principal y al final los datos exactos.",
        "Para comparar datos, usa una tabla corta: escribe los productos en columnas y las características en filas. Para leer un gráfico, mira el título, los nombres de cada barra y las cifras. Para comprender una relación, busca palabras como because, so y as a result. Si dos datos compiten, vuelve a la pregunta y elige el que ella pide.",
    ],
    [("email", "correo electrónico"), ("catalog", "catálogo: lista de productos con características"), ("graph", "gráfico"), ("biography", "biografía: vida de una persona"), ("speech", "discurso"), ("price", "precio")],
    [
        ("Dato de un correo", EMAIL + " ¿Qué día se pide la sala? A) miércoles B) martes", ["Busco el día de la solicitud.", "El asunto dice on Wednesday.", "El martes es el plazo de la respuesta."], "A) miércoles"),
        ("Dato de un gráfico", GRAPH + " ¿Qué deporte elige más gente? A) football B) swimming", ["Busco la cifra más alta.", "Football tiene 40.", "Es el más elegido."], "A) football"),
    ],
    [
        ("Leer una cifra del gráfico sin mirar a qué barra pertenece.", "Se cambia el dato de un deporte por otro.", "Une cada número con el nombre de su barra."),
        ("Pensar que el asunto del correo es el saludo.", "El asunto resume el tema, y el saludo viene después.", "Lee From, To y Subject antes del cuerpo."),
    ],
    [
        (EMAIL + " ¿Quién escribe el correo? A) Pia Soto B) Mr. Vega", "A", "El correo dice From: Pia Soto."),
        (CATALOG + " ¿Cuánto cuesta la lonchera? A) 6.000 pesos B) 18.000 pesos", "A", "El catálogo dice lunch box: price 6000 pesos."),
        (GRAPH + " ¿Cuántos estudiantes eligen tenis? A) 10 B) 15", "A", "El gráfico dice tennis 10."),
    ],
    [
        (EMAIL + " ¿Cuál es el propósito del correo? A) pedir una sala para probar un robot B) invitar a una fiesta", "A", "Dice I am writing to ask if our club can use the robotics room."),
        (CATALOG + " ¿Qué mochila tiene dos años de garantía? A) la B B) la A", "A", "Backpack B tiene 2-year guarantee."),
        (BIO + " ¿Qué profesión tiene Clara Núñez? A) arquitecta B) profesora de inglés", "A", "El texto dice is an architect."),
    ],
    [
        (CATALOG + " Tomás tiene 20.000 pesos. ¿Qué mochila puede comprar? A) la A B) la B", "A", "La A cuesta 18.000 y la B, 25.000."),
        (GRAPH + " ¿Cuántos estudiantes hay en total? Suma las cuatro cifras.", "90", "40 + 25 + 15 + 10 = 90."),
        (BIO + " ¿Por qué diseñó una biblioteca con muchas ventanas? A) para que las personas disfruten leer con luz natural B) para ahorrar dinero", "A", "Dice she wanted people to enjoy reading in natural light."),
    ],
    [
        (CATALOG + " Un compañero quiere la mochila con más bolsillos. ¿Cuál debe elegir y cuánto pagará? A) la B, 25.000 pesos B) la A, 18.000 pesos", "A", "La B tiene cinco bolsillos y cuesta 25.000."),
        (GRAPH + " ¿Qué dos deportes juntos suman la misma cantidad que football? A) volleyball y swimming B) swimming y tennis", "A", "25 + 15 = 40, igual que football; swimming y tennis suman solo 25."),
    ],
    [
        (EMAIL + " ¿Qué tono usa el correo? A) formal B) informal", "A", "Usa Dear Mr. Vega, Could you please y Kind regards."),
        (BIO + " Ordena la vida de Clara según el texto: a) diseñó una biblioteca b) estudió cinco años c) hoy enseña", "b, a, c", "El orden es estudios, trabajo y presente."),
    ],
    [("Lee el siguiente discurso breve: «Dear classmates, our patio is dirty after lunch. Let’s put every wrapper in the bin. A clean school is a better place for everyone.» (dirty = sucio, wrapper = envoltorio, bin = basurero). ¿Cuál es el propósito del discurso? A) persuadir al público de mantener limpio el patio B) informar un horario", "A", "Usa Let’s y una razón final para invitar a actuar.")],
    [
        ("¿Dónde está el propósito de un correo?", "En la primera oración del cuerpo", "Dice por qué se escribe."),
        ("¿Qué muestra la barra más alta de un gráfico?", "El mayor valor", "Es la categoría con más cantidad."),
        ("¿Para qué sirve un catálogo?", "Para comparar productos", "Muestra precio y características."),
    ],
    task("Lee estos datos de ejemplo de un catálogo de zapatillas: «Model Sol: 30000 pesos, grey, light, one-year guarantee. Model Luna: 36000 pesos, black, waterproof, two-year guarantee. Model Mar: 28000 pesos, white, light, no guarantee.» (light = liviana, waterproof = impermeable). Tienes 33000 pesos y quieres una zapatilla con garantía. Escribe en tu hoja: qué modelos puedes comprar, cuál eliges y una razón con datos del texto.", "Puedes comprar Sol (30.000) y Mar (28.000); Luna cuesta 36.000, más de lo que tienes. Con garantía, eliges Sol, porque cuesta 30.000, es liviana y tiene un año de garantía.", ["usa el presupuesto para descartar modelos", "elige uno con garantía", "justifica con datos exactos"], ["hoja con la tabla y la respuesta"], ["elegir Luna sin mirar el precio", "no justificar la elección con datos"], "Muestra a una persona de tu casa tu tabla y pregúntale si está de acuerdo con la razón."),
    "Relee el gráfico de deportes y escribe una frase en español que compare dos barras.",
    "Escribe una biografía de seis líneas de una persona de tu familia que admires, sin datos privados, usando el pasado y el presente.",
)

# ================================================== clase 5: collocations, conectores y prefijos im-, in-, il-
TEXT5 = "«Last week, I made a big decision: I joined a robotics workshop. At first, it seemed impossible, because I had no experience. Neither my cousin nor my friends could join me, so I went alone. Either I would learn or I would give up, I thought. Now I am happy, though the work is not always easy. As soon as the class ends, I save my notes. Unless I practise, I forget the steps. As a result, I study every day.»\n(decision = decisión, impossible = imposible, experience = experiencia, alone = solo, give up = rendirse, notes = apuntes, steps = pasos)"

lesson(
    OA, 5, MAT_READ,
    "Aprenderé a reconocer en un texto combinaciones frecuentes de palabras, expresiones, conectores (neither…nor, either…or, though, unless, as soon as, as a result) y palabras con los prefijos im-, in- e il-. Sirve para entender mejor un texto y adivinar el significado de palabras nuevas.",
    ["Sé que un conector une ideas.", "Sé reconocer palabras clave en un texto."],
    [
        "Las colocaciones (collocations) son combinaciones naturales: make a decision, take notes, give up, join a workshop, heavy rain. Las expresiones de uso frecuente (frequent expressions), como at first (al principio), as soon as (tan pronto como) y so far (hasta ahora), aparecen una y otra vez en los textos. Aprenderlas completas te ayuda a leer más rápido.",
        "Los conectores unen ideas con una relación: neither…nor niega dos cosas (ni… ni); either…or ofrece dos opciones (o… o); though marca un contraste (aunque); unless indica una condición negativa (a menos que); as soon as marca un momento (tan pronto como); y as a result muestra una consecuencia (como resultado). Lee la oración completa y pregúntate qué relación crean antes de buscar la traducción.",
        "Los prefijos im-, in- e il- agregan el sentido de «no» o «lo contrario». Im- se usa antes de b, m y p: impossible, impatient, impolite. Il- se usa antes de l: illegal, illogical. In- se usa en muchos otros casos: incorrect, invisible, informal, incomplete. Si conoces la palabra base (possible, patient, legal), puedes deducir el significado de la derivada.",
    ],
    [("collocation", "combinación natural de palabras"), ("prefix", "prefijo: parte que se agrega al inicio de una palabra"), ("im-", "prefijo de negación antes de b, m, p: impossible"), ("il-", "prefijo de negación antes de l: illegal"), ("in-", "prefijo de negación: incorrect"), ("at first", "al principio")],
    [
        ("Prefijo", "¿Qué significa impatient? A) que no es paciente B) que es muy paciente", ["La palabra base es patient.", "El prefijo im- agrega el sentido de no.", "Entonces es no paciente."], "A) que no es paciente"),
        ("Conector", "En «We stayed home because it was raining», ¿qué relación expresa because? A) una causa B) un contraste", ["Because da la razón.", "La lluvia es la causa de quedarse en casa.", "No es contraste."], "A) una causa"),
    ],
    [
        ("Usar im- antes de una palabra que empieza con l (imlegal).", "La regla pide il- antes de l.", "Escribe illegal con il- ante la l."),
        ("Entender unless como un contraste.", "Unless indica la condición para que algo no ocurra.", "Usa a menos que o si no."),
    ],
    [
        ("Lee: " + TEXT5 + " ¿Qué tomó el hablante la semana pasada? A) una gran decisión B) un autobús", "A", "El texto dice I made a big decision."),
        ("¿Qué prefijo va con la palabra legal para decir lo contrario? A) il- B) im-", "A", "Se usa il- antes de l: illegal."),
        ("Lee: " + TEXT5 + " ¿Qué quiere decir at first? A) al principio B) al final", "A", "At first, it seemed impossible: al principio."),
    ],
    [
        ("Lee: " + TEXT5 + " ¿Qué muestra as a result? A) una consecuencia B) un contraste", "A", "El hablante practica y, como resultado, estudia cada día."),
        ("¿Qué significa incorrect? A) no correcto B) muy correcto", "A", "In- agrega el sentido de no."),
        ("Lee: " + TEXT5 + " ¿Qué muestra though en Now I am happy, though the work is not always easy? A) un contraste B) una causa", "A", "Está feliz, aunque el trabajo no es siempre fácil."),
    ],
    [
        ("Completa con el prefijo correcto: ___possible (no posible). A) im- B) in-", "A", "Antes de p se usa im-: impossible."),
        ("Lee: " + TEXT5 + " ¿Quiénes no pudieron acompañarlo? A) su primo y sus amigos B) su familia", "A", "Neither my cousin nor my friends could join me."),
        ("Lee: " + TEXT5 + " ¿Cuándo guarda sus apuntes? A) tan pronto como la clase termina B) antes de la clase", "A", "As soon as the class ends, I save my notes."),
    ],
    [
        ("Lee: " + TEXT5 + " ¿Qué ocurre si no practica, según el texto? A) se le olvidan los pasos B) se rinde de inmediato", "A", "Dice Unless I practise, I forget the steps."),
        ("Pablo dice que imlegal es correcto. ¿Qué corrección corresponde? A) illegal B) inlegal", "A", "Antes de l se usa il-."),
    ],
    [
        ("Une cada palabra con su significado. 1) invisible 2) impolite 3) illogical. Significados: a) que no se puede ver b) que no tiene lógica c) que no es educado", "1-a, 2-c, 3-b", "Invisible: no visible; impolite: no cortés; illogical: no lógico."),
        ("Lee: «Either we walk, or we take a taxi.» ¿Qué opciones ofrece either…or? A) caminar o tomar un taxi B) caminar y tomar un taxi", "A", "Either…or ofrece dos opciones entre las cuales elegir."),
    ],
    [("Lee: «As soon as the bell rings, the students leave. Neither the teacher nor the director stays in the classroom.» (bell = timbre, rings = suena). ¿Qué ocurre apenas suena el timbre?", "Los estudiantes salen", "As soon as marca el momento en que salen.")],
    [
        ("¿Qué prefijo se usa en impossible?", "im-", "Va antes de p."),
        ("¿Qué significa neither…nor (en lectura de textos)?", "Ni… ni", "Niega dos cosas."),
        ("¿Qué muestra unless?", "Una condición negativa", "Equivale a a menos que."),
    ],
    task("Lee: «It was almost impossible to reach the top of the hill. At first, neither Ana nor Luis wanted to continue. Either they went back or they tried again. As soon as they saw the view, they felt happy. The path was long, though it was not dangerous. As a result, they decided to come back next month.» (reach = llegar, top = cima, continue = continuar, view = vista, path = sendero, dangerous = peligroso). En tu hoja escribe: dos conectores con su relación, una colocación y el significado de impossible.", "Conectores posibles: neither…nor (niega dos personas), either…or (dos opciones), as soon as (momento), though (contraste), as a result (consecuencia). Colocación: reach the top o come back. Impossible: no posible, imposible.", ["identifica dos conectores con su relación", "anota una colocación del texto", "explica el prefijo de impossible"], ["hoja con cuatro respuestas"], ["decir que though es una causa", "inventar un conector que no aparece"], "Subraya cada conector en el texto y escribe al lado su relación."),
    "Escribe diez palabras con im-, in- e il- y agrúpalas según el prefijo.",
    "Escribe un párrafo de cinco oraciones con tres conectores y una colocación de las vistas.",
)
