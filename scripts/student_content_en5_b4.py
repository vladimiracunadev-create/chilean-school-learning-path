"""Cuaderno del estudiante, 5.º básico Inglés (propuesta): EN05 OA 14 (escritura de las funciones del nivel).

Los textos en inglés son originales, muy breves y llevan pista en español. Cada palabra o estructura se enseña en la propia
clase antes de usarla. Sin audio externo: todo lo que hay que leer está escrito en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "EN05 OA 14"


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


# ================================================================ OA 14 clase 1: escribir habilidad, inhabilidad y cantidades
lesson(
    OA, 1,
    "Las oraciones y tablas escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir bien oraciones con can y can't, con there is y there are, y con números hasta mil. Sirve para dar información escrita clara y sin errores.",
    ["Conozco can, can't y los números hasta cien.", "Sé que una oración empieza con mayúscula y termina con punto."],
    [
        "Al escribir hay que cuidar tres cosas. Primero, el apóstrofo: can't lleva apóstrofo en el lugar de la o de not («They can't fly»). Segundo, la forma del verbo: después de can el verbo no cambia («She can swim»). Tercero, cada oración comienza con mayúscula y termina con punto.",
        "Para decir cuántos hay, escribe a o an con uno solo («a bus», «an egg») y there is. Con varios escribe there are, y recuerda que child cambia a children. Con many o a lot of, el sustantivo va en plural: «many cars», «a lot of children».",
        "Los números se escriben con guion entre decena y unidad (twenty-one, seventy-two). Las centenas se escriben como three hundred, five hundred. Mil es one thousand. Para estar seguro, lee en voz alta el número que escribiste y compáralo con la cifra.",
    ],
    [("can't", "no puede (can not)"), ("There is a / an", "Hay un / una"), ("There are", "Hay (varios)"), ("many / a lot of", "muchos / muchos"), ("twenty-one", "veintiuno"), ("one hundred", "cien"), ("one thousand", "mil")],
    [
        ("Escribir una inhabilidad", "Escribe una oración con estos datos: Tomás — nadar: no puede.", ["El sujeto es Tomás.", "Va can't y el verbo swim sin cambios.", "Empiezo con mayúscula y termino con punto."], "Tomás can't swim."),
        ("Corregir una oración", "Corrige: «there is ten children.» Escribe la oración bien escrita.", ["Ten children es plural.", "Con plural se usa there are.", "Agrego mayúscula inicial y punto."], "There are ten children."),
    ],
    [
        ("Escribir «cant» sin apóstrofo.", "Se olvida la contracción.", "Escribe can't con apóstrofo."),
        ("Escribir «thirtythree» todo junto.", "Falta el guion entre decena y unidad.", "Escribe thirty-three."),
    ],
    [
        ("¿Cuál está bien escrito: cant, can't o ca'nt?", "can't", "El apóstrofo reemplaza la o de not."),
        ("¿Cómo se escribe en cifras «sixteen»?", "16", "Sixteen es dieciséis."),
        ("¿Cuál es el plural de child?", "children", "Es un plural especial."),
    ],
    [
        ("Elige la oración bien escrita: a) They can't fly. b) They cant fly.", "a", "La a lleva el apóstrofo."),
        ("Completa con a o an: «There is ___ orange on the table.»", "an", "Orange empieza con vocal."),
        ("Escribe en letras el número 72.", "seventy-two", "Se une la decena y la unidad con guion."),
    ],
    [
        ("Pablo puede saltar y no puede nadar. Elige la oración correcta: a) Pablo can jump but he can swim. b) Pablo can jump but he can't swim.", "b", "La segunda idea contrasta con la primera."),
        {"q": "En una escuela hay 480 niños y 320 niñas. ¿Cuántos estudiantes hay en total? Escribe el número en cifras.", "a": "800", "why": "Se suman las dos cantidades. Cálculo: 480 + 320 = 800.", "calc": "480+320"},
        ("Escribe en letras el número 800.", "eight hundred", "Eight es ocho y hundred es cien."),
    ],
    [
        ("Ana escribe «I can't swim but I can float». ¿Qué palabra une las dos ideas?", "but", "But une una idea con su contraste."),
        ("¿Cuál está bien escrito: thirty-three o thirtythree?", "thirty-three", "Los números compuestos llevan guion."),
    ],
    [
        ("Una profesora escribe en la pizarra: «There are a lot of children.» ¿Qué número de niños puede ser? a) 1 b) 25", "b", "Con a lot of children son muchos."),
        ("Escribe en letras el número 1.000.", "one thousand", "Mil es one thousand."),
    ],
    [("En el cartel de la biblioteca hay 600 libros. Escribe una oración que diga «hay seiscientos libros» con there are.", "There are six hundred books.", "Se usa there are con plural y el número en letras.")],
    [
        ("¿Qué reemplaza el apóstrofo en can't?", "La o de not", "Can't es can not."),
        ("¿Cómo se escribe «cuarenta y cinco» en inglés?", "forty-five", "Decena y unidad se unen con guion."),
        ("¿Con qué letra empieza cada oración?", "Con mayúscula", "Es una regla de escritura."),
    ],
    task("Lee este modelo: «I can run but I can't swim. There are twenty-five chairs in my room. There is an egg in the kitchen.» Escribe en tu hoja cuatro oraciones: una con can y can't, una con there is a/an, una con there are y un número hasta 1.000 en letras, y una con many o a lot of. Revisa el apóstrofo, las mayúsculas, los puntos y los guiones.", "I can read but I can't sing. There is an apple on the table. There are fifty students in my school. There are a lot of trees in the park.", ["usa can y can't con el verbo sin cambios", "usa a/an y is/are correctos", "escribe el número en letras con guion", "revisa mayúsculas, apóstrofos y puntos"], ["hoja con cuatro oraciones"], ["olvidar el apóstrofo", "escribir el número sin guion"], "Subraya con un color cada error corregido para ver cómo mejoró el texto."),
    "Escribe tres oraciones con can't sobre animales (por ejemplo, A fish can't walk).",
    "Escribe un párrafo de cinco oraciones sobre tu sala de clases con cantidades y números.",
)

# ================================================================ OA 14 clase 2: ocupaciones, vestimenta y gustos
lesson(
    OA, 2,
    "Las oraciones y listas escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir sobre ocupaciones, la ropa que lleva alguien y lo que me gusta o no. Sirve para describir personas y expresar mis preferencias por escrito.",
    ["Conozco nurse, vet, doctor y teacher.", "Sé que like significa gustar."],
    [
        "Para escribir una ocupación se usa is o are y a o an: «She is a nurse», «He is an artist», «They are vets». Con varias personas, la ocupación va en plural con -s. Se escribe a ante consonante y an ante vocal. Algunas ocupaciones son nurse, doctor, vet, teacher y firefighter.",
        "Para describir la ropa se escribe «He is wearing a jacket» o «She's wearing a uniform». Cuando varias personas llevan lo mismo, se escribe «They are wearing uniforms». La palabra wearing lleva -ing, siempre después de is o are.",
        "Para escribir un gusto se usa like y para lo contrario don't like: «I like apples. I don't like onions.» Con él o ella el verbo cambia: «He likes apples» y «She doesn't like onions». Revisa las mayúsculas y los puntos.",
    ],
    [("She is a nurse.", "Ella es enfermera."), ("an artist", "un artista"), ("They are vets.", "Ellos son veterinarios."), ("He is wearing a jacket.", "Lleva puesta una chaqueta."), ("I don't like…", "No me gusta…"), ("He likes / She doesn't like", "A él le gusta / A ella no le gusta")],
    [
        ("Escribir una ocupación", "Escribe una oración: Ana — enfermera.", ["Sujeto Ana, verbo is.", "Nurse empieza con consonante, entonces a.", "Con mayúscula y punto."], "Ana is a nurse."),
        ("Escribir la ropa", "Escribe una oración: Pedro lleva puesto un uniforme.", ["Sujeto Pedro, verbo is.", "Wearing lleva -ing.", "Un uniforme es a uniform."], "Pedro is wearing a uniform."),
    ],
    [
        ("Escribir «She is nurse» sin a.", "Falta el artículo antes de la ocupación.", "Escribe She is a nurse."),
        ("Escribir «He like apples».", "Con he, like cambia.", "Escribe He likes apples."),
    ],
    [
        ("¿Cómo se escribe «enfermera» en inglés?", "nurse", "Nurse es enfermera o enfermero."),
        ("¿Qué significa «jacket»?", "Chaqueta", "Es una prenda de ropa."),
        ("¿Cuál es el plural de vet?", "vets", "Se agrega s."),
    ],
    [
        ("Completa: «She is ___ artist.» Opciones: a, an.", "an", "Artist empieza con vocal."),
        ("Completa: «They ___ vets.» Opciones: is, are.", "are", "They es plural."),
        ("Completa: «He ___ wearing a uniform.» Opciones: is, are.", "is", "He va con is."),
    ],
    [
        ("Escribe una oración que comience con Sofía y que diga que Sofía y Leo son veterinarios.", "Sofía and Leo are vets.", "Dos personas llevan are y la ocupación en plural."),
        ("Corrige: «I no like fish». Escribe la oración bien escrita.", "I don't like fish.", "La negación se forma con don't."),
        ("Escribe una oración: María lleva puesta una chaqueta roja.", "María is wearing a red jacket.", "Se usa is wearing y el color va antes del sustantivo."),
    ],
    [
        ("Pedro escribe «Leo and Mia are vet». ¿Cuál es el error?", "Vet debe ir en plural: vets", "Hay dos personas."),
        ("¿Cuál está bien escrito? a) He likes music. b) He like music.", "a", "Con he, like pasa a likes."),
    ],
    [
        ("Elige el orden correcto para empezar un párrafo: a) She works in a hospital. b) Ms. Rojas is a nurse.", "b", "Primero se presenta a la persona y luego se dan datos."),
        ("«I like apples. I don't like onions. I like pears.» ¿Cuántas oraciones dicen lo que le gusta?", "2", "Son I like apples y I like pears."),
    ],
    [("En el cartel de la «Semana de los oficios» dice: «Mr. Díaz is a firefighter. He is wearing a red jacket.» (firefighter = bombero). Escribe lo que lleva puesto Mr. Díaz.", "A red jacket", "El cartel dice He is wearing a red jacket.")],
    [
        ("¿Qué palabra falta: «He ___ wearing»?", "is", "Después de he va is."),
        ("¿Cómo se escribe «No me gusta» en inglés?", "I don't like", "Don't like es no gustar."),
        ("¿Qué artículo va antes de «uniform»: a o an?", "a", "Uniform se pronuncia con sonido de consonante (yu), así que lleva a."),
    ],
    task("Lee este modelo: «Ms. Rojas is a nurse. She works in a hospital. She is wearing a white uniform. She likes her job.» Escribe en tu hoja un párrafo de cuatro oraciones sobre una persona que trabaja (puede ser inventada): quién es, qué ocupación tiene, qué lleva puesto y qué le gusta de su trabajo. Revisa a/an, is/are, el verbo con -s y los puntos.", "Mr. Silva is a firefighter. He works at the fire station. He is wearing a red helmet. He likes helping people.", ["dice la ocupación con a/an", "describe qué lleva puesto con is wearing", "usa likes con he o she"], ["hoja con un párrafo de cuatro oraciones"], ["omitir a/an", "escribir like en vez de likes"], "Lee el texto con la persona y verifica que cada oración tenga sentido."),
    "Escribe tres oraciones: dos con I like y una con I don't like.",
    "Describe en cuatro oraciones a dos personas que trabajan juntas, usando they are.",
)

# ================================================================ OA 14 clase 3: personalidad, estados, hora y opinión
lesson(
    OA, 3,
    "Las oraciones y textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir cómo es una persona, cómo se siente, qué hora es y por qué me gusta algo. Sirve para escribir notas, mensajes y opiniones con razones.",
    ["Conozco quiet, friendly, sad, tired y bored.", "Sé escribir la hora en punto."],
    [
        "Para describir cómo es alguien se escribe is más un adjetivo: «Mia is friendly», «Leo is quiet». Para decir cómo te sientes se escribe feel: «I feel tired», «I feel angry». Para escribir la hora en punto se usa «It's four o'clock», con apóstrofo en It's y con o'clock.",
        "Los números de la hora se escriben en letras en un texto: one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve. Se usa o'clock solo cuando la hora es exacta. No sirve para las 5:30.",
        "Para justificar una opinión se escribe la opinión y luego because con la razón: «I like swimming because it's fun». No olvides la mayúscula inicial y el punto final, y revisa la ortografía de because (b-e-c-a-u-s-e) y de friendly (f-r-i-e-n-d-l-y).",
    ],
    [("Mia is friendly.", "Mia es amistosa."), ("I feel tired.", "Me siento cansado."), ("It's four o'clock.", "Son las cuatro en punto."), ("because", "porque"), ("fun", "entretenido"), ("o'clock", "en punto")],
    [
        ("Escribir la hora", "Escribe la hora: 7:00.", ["La hora es en punto.", "Empiezo con It's y el número en letras.", "Termino con o'clock."], "It's seven o'clock."),
        ("Justificar una opinión", "Escribe: Me gusta nadar porque es entretenido.", ["Escribo la opinión: I like swimming.", "Agrego because y la razón.", "La razón es it's fun."], "I like swimming because it's fun."),
    ],
    [
        ("Escribir «becouse» o «becuse».", "Se escribe de oído.", "La ortografía correcta es because."),
        ("Escribir «It's five o'clock» cuando son las 5:30.", "O'clock solo se usa en punto.", "Solo se usa o'clock en las horas exactas."),
    ],
    [
        ("¿Cómo se escribe «siete en punto»?", "It's seven o'clock", "Se usa o'clock para la hora exacta."),
        ("¿Cuál está bien escrito: becouse o because?", "because", "Es la palabra para dar una razón."),
        ("¿Qué significa «I feel sad»?", "Me siento triste", "Feel sad es sentirse triste."),
    ],
    [
        ("Completa: «Pedro is ___.» (Pedro habla poco.) Opciones: quiet, funny.", "quiet", "Quiet es callado."),
        ("Completa: «I ___ tired.» Opciones: feel, feels.", "feel", "Con I se usa feel."),
        ("Completa: «It's ___ o'clock.» (Son las diez.)", "ten", "Ten es diez."),
    ],
    [
        ("Corrige la ortografía: «frendly». Escribe la palabra bien.", "friendly", "La palabra tiene una i antes de n."),
        ("Completa: «I like painting ___ it is relaxing.»", "because", "Se necesita because para dar la razón."),
        ("Escribe la hora: 12:00.", "It's twelve o'clock.", "La hora exacta se escribe con o'clock."),
    ],
    [
        ("Elige la oración que justifica la opinión: a) I like soccer because it's fun. b) I like soccer and it's fun.", "a", "Because introduce la razón."),
        ("Mía escribe «It's 5 o'clock» cuando son las 5:30. ¿Qué está mal?", "O'clock solo se usa para la hora en punto", "Las 5:30 no son en punto."),
    ],
    [
        ("Cuenta los errores de «i feel sad becouse my team lost» (mayúsculas, ortografía y puntuación). ¿Cuántos errores hay?", "3", "Faltan mayúscula en I, la corrección de because y el punto."),
        ("Escribe corregida la oración «i feel sad becouse my team lost».", "I feel sad because my team lost.", "Se corrigen I, because y el punto."),
    ],
    [("Camila escribe una nota para su amiga Ana: «It's late. I feel tired. I go to bed.» ¿Qué dos palabras dicen cómo se siente?", "feel tired", "I feel tired dice cómo se siente.")],
    [
        ("¿Para qué sirve la palabra because?", "Para dar una razón", "Es una conjunción que explica por qué."),
        ("¿Cuándo se usa o'clock?", "Solo con horas en punto", "Las otras horas llevan otra forma."),
        ("¿Cómo se escribe «Ella es amistosa» en inglés?", "She is friendly", "Is friendly describe a una persona."),
    ],
    task("Lee este modelo: «Mia is friendly. It's four o'clock. I feel tired. I like Music because it's fun.» Escribe en tu hoja un texto de cuatro oraciones: una que describa cómo es una persona, otra con cómo te sientes, otra con una hora en punto y otra con una opinión con because. Revisa mayúsculas, apóstrofos, la ortografía de because y los puntos.", "Leo is quiet. I feel bored. It's three o'clock. I like reading because it's relaxing.", ["describe a una persona con is + adjetivo", "usa I feel + estado", "escribe la hora con o'clock", "justifica con because y buena ortografía"], ["hoja con cuatro oraciones"], ["escribir becouse", "usar o'clock con 5:30"], "Lee las oraciones con la persona y marca una mejora por cada corrección."),
    "Escribe una nota de tres oraciones a una persona de tu casa: la hora que es y cómo te sientes.",
    "Escribe tres opiniones con because sobre una comida, una asignatura y un deporte.",
)

# ================================================================ OA 14 clase 4: acciones en el momento
lesson(
    OA, 4,
    "Las oraciones y preguntas escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir lo que alguien está haciendo ahora, con preguntas y respuestas, usando is o are y el verbo con -ing. Sirve para describir una escena y preguntar por ella.",
    ["Conozco los verbos read, play, run, make y swim.", "Sé que is va con he y she, y are con they."],
    [
        "Para escribir una acción que ocurre ahora se usa is o are y el verbo con -ing: «He is reading», «They are playing». Si la acción es negativa se escribe isn't o aren't: «He isn't reading». Para preguntar, is o are va primero: «Is he reading?» y «Are they playing?».",
        "Las respuestas cortas repiten is o are: «Yes, he is», «No, he isn't», «Yes, they are», «No, they aren't». Escribe las respuestas cortas sin repetir el verbo. Con -ing hay que cuidar la ortografía: play pasa a playing, read pasa a reading, run pasa a running (se repite la n), make pasa a making (se quita la e) y swim pasa a swimming (se repite la m).",
        "Para escribir una escena, mira primero qué hace cada persona y luego escribe una oración por persona. Verifica que cada oración tenga is o are, el verbo con -ing y el punto o el signo de pregunta.",
    ],
    [("He is reading.", "Él está leyendo."), ("They aren't playing.", "Ellos no están jugando."), ("Is he reading?", "¿Está leyendo?"), ("Yes, he is. / No, he isn't.", "Sí, lo está. / No, no lo está."), ("running / making / swimming", "corriendo / haciendo / nadando"), ("-ing", "terminación del verbo para acciones que ocurren ahora")],
    [
        ("Escribir una acción en el momento", "Escribe la oración: Ana — dibujar (ahora).", ["Sujeto Ana, verbo is.", "Draw pasa a drawing.", "Con mayúscula y punto."], "Ana is drawing."),
        ("Escribir una pregunta y su respuesta", "Pregunta: ¿Está durmiendo Leo? (Leo duerme.) Escribe la pregunta y la respuesta corta.", ["La pregunta empieza con Is.", "Sleep pasa a sleeping.", "La respuesta es afirmativa."], "Is Leo sleeping? Yes, he is."),
    ],
    [
        ("Escribir «Is she read?».", "Falta -ing en el verbo.", "Escribe Is she reading?"),
        ("Escribir «runing».", "No se repite la n.", "Run pasa a running."),
    ],
    [
        ("¿Cómo se escribe «play» con -ing?", "playing", "Se agrega -ing sin cambios."),
        ("¿Cómo se escribe «read» con -ing?", "reading", "Se agrega -ing."),
        ("¿Qué significa «Is he reading?»", "¿Está leyendo?", "Pregunta por una acción ahora."),
    ],
    [
        ("¿Cómo se escribe «run» con -ing?", "running", "Se repite la n."),
        ("¿Cómo se escribe «make» con -ing?", "making", "Se quita la e antes de -ing."),
        ("¿Cómo se escribe «swim» con -ing?", "swimming", "Se repite la m."),
    ],
    [
        ("Completa: «___ they playing soccer? No, they aren't.» Opciones: Is, Are.", "Are", "They va con are."),
        ("Escribe la pregunta con estas palabras: he / sleeping / Is", "Is he sleeping?", "En la pregunta, is va primero."),
        ("Completa: «Mia is ___.» (dibujar, ahora). Escribe el verbo con -ing.", "drawing", "Draw pasa a drawing."),
    ],
    [
        ("Pedro escribe «Is she read?». ¿Qué le falta?", "El -ing en read: Is she reading?", "Después de is va el verbo con -ing."),
        ("Elige la respuesta corta correcta a «Are they playing?» si no juegan: a) No, they aren't. b) No, they isn't.", "a", "They va con aren't."),
    ],
    [
        ("Texto: «Tom is running. Mia is reading. Leo and Ana are playing.» ¿Cuántas personas aparecen?", "4", "Son Tom, Mia, Leo y Ana."),
        ("En el mismo texto, responde por escrito: Are Leo and Ana reading?", "No, they aren't.", "Ellos están jugando, no leyendo."),
    ],
    [("En el patio, una niña observa: «Tom is running. Mia is reading.» Alguien le pregunta «Is Mia running?». ¿Qué responde por escrito?", "No, she isn't.", "Mia lee, no corre.")],
    [
        ("¿Dónde va is en una pregunta: al comienzo o al final?", "Al comienzo", "Is he reading?"),
        ("¿Cómo se escribe la respuesta corta si sí lo hace con they?", "Yes, they are.", "La respuesta repite are."),
        ("¿Qué le agregas al verbo para una acción ahora?", "-ing", "Es la terminación característica."),
    ],
    task("Lee este modelo: «Tom is running. Mia is reading. Is Leo playing? No, he isn't. He is sleeping.» Escribe en tu hoja una escena de cinco oraciones sobre lo que hacen cuatro personas en una plaza (pueden ser inventadas). Incluye una pregunta con Is o Are y su respuesta corta. Revisa el -ing y los signos.", "Sara is swimming. Pedro and Ana are playing. Is Leo running? Yes, he is. Mia is making a sandcastle.", ["usa is o are con el verbo en -ing", "la pregunta lleva Is/Are al comienzo y signo de pregunta", "la respuesta corta es correcta", "revisa running, making y swimming"], ["hoja con la escena"], ["omitir -ing", "no repetir la consonante"], "Pide que lea cada oración y diga a quién describe."),
    "Escribe tres oraciones sobre lo que hacen tres personas de tu casa en este momento.",
    "Escribe un diálogo con cuatro preguntas Is/Are y sus respuestas cortas sobre una escena.",
)

# ================================================================ OA 14 clase 5: acciones en el pasado y párrafo propio
lesson(
    OA, 5,
    "Las oraciones y textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir lo que pasó antes con was, were, made, did y felt y a unir varias funciones en un párrafo corto. Sirve para contar mi día de ayer por escrito.",
    ["Conozco is y are, y las pistas yesterday y last night.", "Sé escribir oraciones con can, con there is y con like."],
    [
        "Para escribir lo que pasó antes, cambia el verbo. Be pasa a was con I, he, she e it, y a were con we, you y they. Algunos verbos cambian de forma: make pasa a made, do pasa a did y feel pasa a felt. Las pistas de tiempo son yesterday (ayer), last night (anoche) y last weekend (el fin de semana pasado).",
        "Ejemplos: «Yesterday I was at home», «We were happy», «I made a cake», «I did my homework», «I felt tired». Revisa que la pista de tiempo y el verbo estén en pasado. No mezcles «Yesterday I make a cake».",
        "Un párrafo breve junta varias funciones: puede decir dónde estabas, qué hiciste, cómo te sentiste y por qué. Usa una oración por idea, ordénalas con first, then y finally, y termina con una opinión o un sentimiento. Al final, revisa mayúsculas, puntos y ortografía.",
    ],
    [("was / were", "estaba, estuve / estaban, estuvieron"), ("made", "hice (pasado de make)"), ("did", "hice (pasado de do)"), ("felt", "sentí (pasado de feel)"), ("yesterday", "ayer"), ("last night", "anoche")],
    [
        ("Pasar una oración al pasado", "Cambia al pasado: «I feel tired.» Usa yesterday al comienzo.", ["Feel pasa a felt.", "Agrego la pista Yesterday.", "Cuido mayúscula y punto."], "Yesterday I felt tired."),
        ("Elegir was o were", "Completa: «We ___ at the park last weekend.»", ["El sujeto es We.", "We va con were.", "La pista last weekend indica pasado."], "were"),
    ],
    [
        ("Escribir «Yesterday I make a cake».", "El verbo no está en pasado.", "Escribe Yesterday I made a cake."),
        ("Escribir «We was happy».", "We no va con was.", "Escribe We were happy."),
    ],
    [
        ("¿Cuál es el pasado de make?", "made", "Es un verbo que cambia de forma."),
        ("¿Cuál es el pasado de feel?", "felt", "Es un verbo que cambia de forma."),
        ("¿Cuál es el pasado de do?", "did", "Es un verbo que cambia de forma."),
    ],
    [
        ("Completa: «Yesterday I ___ at home.» Opciones: was, were.", "was", "I va con was."),
        ("Completa: «They ___ happy.» Opciones: was, were.", "were", "They va con were."),
        ("Completa: «Last night I ___ my homework.» Opciones: do, did.", "did", "Last night indica pasado."),
    ],
    [
        ("Escribe en pasado con yesterday: «I make a sandwich.»", "Yesterday I made a sandwich.", "Make pasa a made."),
        ("Ordena para formar una oración que empiece con Yesterday: felt / I / happy / Yesterday", "Yesterday I felt happy.", "La pista va al comienzo y luego el sujeto y el verbo."),
        ("Completa: «She ___ my friend last year.» Opciones: was, were.", "was", "She va con was."),
    ],
    [
        ("¿Cuál tiene un error? a) She was tired. b) We was tired.", "b", "We va con were."),
        ("¿Cuál oración habla del pasado? a) I do my homework now. b) I did my homework yesterday.", "b", "Did y yesterday indican pasado."),
    ],
    [
        ("Texto: «Yesterday I was at home. I did my homework. I made a sandwich. I felt happy.» ¿Cuántos verbos en pasado hay?", "4", "Son was, did, made y felt."),
        ("En ese texto, ¿qué oración dice cómo se sintió?", "I felt happy.", "Felt es la forma del verbo de sentir."),
    ],
    [("Ana escribe a su amiga Julia: «Yesterday I was at the park. We were happy. I made a drawing.» (drawing = dibujo). ¿Con qué palabra marca que habla del pasado?", "Yesterday", "Es la pista de tiempo.")],
    [
        ("¿Cuál es el pasado de be con you?", "were", "You va con were."),
        ("¿Qué significa «last night»?", "Anoche", "Es una pista de pasado."),
        ("¿Cómo se escribe «Ayer me sentí cansado» en inglés?", "Yesterday I felt tired", "Felt es el pasado de feel."),
    ],
    task("Lee este modelo: «Yesterday I was at home. I did my homework. Then I made a sandwich. Finally, I felt happy because it was a good day.» Escribe en tu hoja un párrafo de cinco oraciones sobre tu día de ayer o de un día inventado. Usa was o were, y al menos dos de made, did y felt. Une las ideas con first, then y finally, y termina con una opinión con because.", "Yesterday I was at school. First, I did my Math homework. Then I made a card for my friend. Finally, I felt happy because it was fun.", ["usa was o were bien conjugado", "usa dos de made, did, felt", "usa first/then/finally", "termina con because"], ["hoja con un párrafo de cinco oraciones"], ["mezclar yesterday con presente", "escribir we was"], "Pide que relea y subraye cada verbo en pasado."),
    "Escribe tres oraciones con yesterday, last night y last weekend.",
    "Escribe un párrafo que junte una hora, un sentimiento y una acción en el pasado.",
)
