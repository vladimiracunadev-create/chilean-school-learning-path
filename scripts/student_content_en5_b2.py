"""Cuaderno del estudiante, 5.º básico Inglés (propuesta): EN05 OA 12 (diálogos sobre habilidad, cantidad, ocupaciones, gustos, hora y acciones).

Los textos en inglés son originales, muy breves y llevan pista en español. Cada palabra o estructura se enseña en la propia
clase antes de usarla. Sin audio externo: todo lo que hay que leer está escrito en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "EN05 OA 12"


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


# ================================================================ OA 12 clase 1: habilidad, inhabilidad y contraste
lesson(
    OA, 1,
    "Los diálogos y los datos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a decir lo que alguien puede y no puede hacer (can y can't) y a contrastar dos ideas con but. Sirve para conversar en inglés sobre habilidades de personas y animales.",
    ["Conozco verbos como swim, run, fly y jump.", "Sé responder preguntas cortas con yes y no."],
    [
        "Para decir lo que alguien puede hacer se usa can, y para decir lo que no puede hacer se usa can't (que es can not). Después de can o can't va el verbo sin cambios: «I can swim», «They can't fly». Lo mismo vale para he, she, it, we, you y they.",
        "Para preguntar se pone can al comienzo: «Can a fish fly?». La respuesta corta es «Yes, it can» o «No, it can't». Observa que en la respuesta corta no se repite el verbo.",
        "Para contrastar dos ideas se usa but (pero): «A penguin can swim but it can't fly». La primera idea es lo que sí puede y la segunda, lo que no. Antes de responder, piensa en el dato real: ¿el animal o la persona puede hacerlo?",
    ],
    [("can", "poder / saber hacer"), ("can't", "no poder / no saber hacer"), ("but", "pero"), ("Can a fish fly?", "¿Puede volar un pez?"), ("Yes, it can. / No, it can't.", "Sí, puede. / No, no puede."), ("swim / fly / run / jump", "nadar / volar / correr / saltar"), ("ride a bike", "andar en bicicleta")],
    [
        ("Responder con una respuesta corta", "«Can a dog fly?» Escribe la respuesta corta.", ["Pienso en el dato real: un perro no vuela.", "La respuesta es negativa: No.", "Uso it can't y no repito el verbo."], "No, it can't"),
        ("Contrastar dos ideas", "Une con but: «A penguin ___ swim» y «it ___ fly». Completa con can o can't.", ["Un pingüino sí nada.", "Un pingüino no vuela.", "La oración queda: A penguin can swim but it can't fly."], "can; can't"),
    ],
    [
        ("Decir «She can swims».", "Se le pone s al verbo después de can.", "Después de can el verbo no cambia: She can swim."),
        ("Responder «No, it can't fly» a la pregunta «Can a dog fly?».", "Se repite el verbo en la respuesta corta.", "La respuesta corta es No, it can't."),
    ],
    [
        ("¿Qué significa «can't»?", "No puedo, no puede", "Can't es la forma negativa de can."),
        ("Completa con can o can't: «A dog ___ fly.»", "can't", "Los perros no vuelan."),
        ("Completa con can o can't: «A fish ___ swim.»", "can", "Los peces nadan."),
    ],
    [
        ("«Can a bee fly? Yes, it ___.» (bee = abeja) Completa con can o can't.", "can", "La respuesta es afirmativa: Yes, it can."),
        ("«Can a dog fly? No, it ___.» Completa con can o can't.", "can't", "La respuesta es negativa: No, it can't."),
        ("¿Qué significa «but» en «It can run but it can't fly»?", "Pero", "But une dos ideas que contrastan."),
    ],
    [
        ("Completa con can o can't: «A penguin ___ swim but it ___ fly.»", "can; can't", "El pingüino nada, pero no vuela."),
        ("En un diálogo: «A: Can you ride a bike? B: No, I ___.» Completa la respuesta de B con can o can't.", "can't", "B responde No, entonces va can't."),
        ("Datos: Leo puede dibujar, no puede cantar, puede nadar. ¿Qué oración es verdadera? a) Leo can sing. b) Leo can't sing.", "b", "En la tabla Leo no puede cantar."),
    ],
    [
        ("Mía dice: «A turtle can swim and it can fly.» (turtle = tortuga). ¿Qué parte es falsa?", "it can fly", "Las tortugas no vuelan."),
        ("¿Cuál oración contrasta bien? a) A cat can climb but it can't fly. b) A cat can climb but it can climb.", "a", "En la a la segunda idea es lo contrario de la primera."),
    ],
    [
        ("Datos: Ana puede nadar y no puede patinar; Pablo no puede nadar y puede patinar. ¿Qué oración es verdadera? a) Ana can skate but Pablo can't. b) Pablo can skate but Ana can't.", "b", "Pablo patina y Ana no."),
        ("Diálogo: «A: Can you swim? B: Yes, I can. A: Can you skate? B: No, I can't.» ¿Cuántas veces aparece la palabra can o can't (sin contar la pregunta)?", "2", "Aparecen en las respuestas: I can y I can't."),
    ],
    [("En la clase de Educación Física, el profesor pregunta a Marcos: «Can you hop on one foot?» (hop = saltar en un pie). Marcos no puede y responde en inglés. ¿Qué dice?", "No, I can't", "Es la respuesta corta negativa.")],
    [
        ("¿Qué significa «can»?", "Poder o saber hacer algo", "Can indica una habilidad."),
        ("¿Cómo respondes «Can a fish fly?»", "No, it can't", "Un pez no vuela."),
        ("¿Qué significa «but»?", "Pero", "But une dos ideas distintas."),
    ],
    task("Lee este modelo: «Lía can run but she can't swim. Tomás can draw but he can't sing.» Escribe en tu hoja tres oraciones sobre ti o sobre un animal con la forma «... can ... but ... can't ...». Luego pregunta a una persona de tu casa «Can you ...?» y anota su respuesta corta.", "A dog can run but it can't fly. I can read but I can't swim. Pregunta: Can you cook? Yes, I can.", ["usa can y can't con el verbo sin cambios", "une las dos ideas con but", "anota una respuesta corta correcta"], ["hoja con tres oraciones y una pregunta"], ["agregar s al verbo", "repetir el verbo en la respuesta corta"], "Pide que lea sus oraciones en voz alta y que diga si cada una es verdadera."),
    "Dibuja un animal y escribe una oración con can y otra con can't sobre él.",
    "Escribe un diálogo de cuatro líneas en que una persona pregunta por tres habilidades y la otra responde con respuestas cortas.",
)

# ================================================================ OA 12 clase 2: cantidades y números hasta mil
lesson(
    OA, 2,
    "Los datos y listas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a decir cuántos hay con a, an, one, many y a lot of, y a leer y escribir números en inglés hasta mil. Sirve para dar y pedir cantidades en un diálogo.",
    ["Conozco los números en inglés hasta cien.", "Sé que las palabras en plural llevan -s, como book y books."],
    [
        "Para hablar de una sola cosa se usa a o an: a ante una consonante (a book) y an ante una vocal (an apple, an egg). Con un solo elemento se dice «There is a…» o «There is one…». Con más de uno se dice «There are…»: «There are two books».",
        "Para cantidades grandes se usan many (muchos) con cosas que se cuentan y a lot of (mucho/muchos) con cualquier cosa: «Many children play» o «A lot of children play». Algunos plurales son especiales: child se convierte en children. Los números llevan guion entre decena y unidad: forty-five (45).",
        "Los números grandes: 100 es one hundred, 200 es two hundred, 300 es three hundred, 350 es three hundred fifty (o three hundred and fifty), y 1.000 es one thousand. No confundas thirteen (13) con thirty (30): el sonido fuerte está en distinto lugar.",
    ],
    [("a / an", "un / una"), ("There is / There are", "hay (uno) / hay (varios)"), ("many", "muchos"), ("a lot of", "mucho, muchos"), ("child / children", "niño / niños"), ("one hundred", "cien (100)"), ("one thousand", "mil (1.000)")],
    [
        ("Elegir a o an", "Completa: «There is ___ egg on the table.»", ["Egg empieza con la vocal e.", "Ante una vocal se usa an.", "La oración es: There is an egg on the table."], "an"),
        ("Escribir un número en letras", "Escribe en inglés el número 350.", ["Primero las centenas: three hundred.", "Luego la decena: fifty.", "Las junto: three hundred fifty."], "three hundred fifty"),
    ],
    [
        ("Decir «There is five children».", "Se usa is con un plural.", "Con varios se usa are: There are five children."),
        ("Confundir thirteen (13) con thirty (30).", "Se oyen casi igual.", "Thirteen termina en -teen (13) y thirty termina en -ty (30); revisa el final."),
    ],
    [
        ("¿Qué va antes de «apple»: a o an?", "an", "Apple empieza con vocal."),
        ("¿Cuál es el plural de «child»?", "children", "Child cambia en vez de agregar s."),
        ("¿Qué significa «a lot of»?", "Mucho o muchos", "Se usa para hablar de cantidades grandes."),
    ],
    [
        ("Completa: «There is ___ umbrella on the chair.» (umbrella = paraguas)", "an", "Umbrella empieza con vocal."),
        ("Completa con is o are: «There ___ many children in the park.»", "are", "Many children es plural."),
        ("¿Cuál número es 13: thirteen o thirty?", "thirteen", "Thirteen termina en -teen."),
    ],
    [
        ("Escribe en inglés el número 45.", "forty-five", "Se junta la decena y la unidad con guion."),
        ("Escribe en inglés el número 300.", "three hundred", "Three es 3 y hundred es 100."),
        {"q": "En un estacionamiento hay 120 autos y 30 motos. ¿Cuántos vehículos hay en total? Escribe el número.", "a": "150", "why": "Se suman los autos y las motos. Cálculo: 120 + 30 = 150.", "calc": "120+30"},
    ],
    [
        ("Marta escribe «There is five children». ¿Cuál es la oración correcta? a) There are five children. b) There is five children.", "a", "Cinco niños son varios, por eso se usa are."),
        ("¿Cuál usa bien many? a) Many children play. b) Many water is cold.", "a", "Many se usa con cosas que se cuentan, como children."),
    ],
    [
        {"q": "Un cartel de la biblioteca dice: «There are 500 books, 250 pens and 100 maps.» ¿Cuántas cosas hay en total? (maps = mapas)", "a": "850", "why": "Se suman las tres cantidades. Cálculo: 500 + 250 + 100 = 850.", "calc": "500+250+100"},
        ("¿Cuál cantidad es mayor: one hundred cars o one thousand cars?", "one thousand cars", "Mil es mayor que cien."),
    ],
    [{"q": "En el curso 5.º A hay 30 children y 12 van a un taller de música. ¿Cuántos NO van al taller?", "a": "18", "why": "Se resta los que van al total. Cálculo: 30 − 12 = 18.", "calc": "30-12"}],
    [
        ("¿Cuál es el plural de child?", "children", "Es un plural especial."),
        ("¿Se dice «There is» o «There are» con 20 cars?", "There are", "Veinte autos es plural."),
        ("¿Cómo se escribe 100 en inglés?", "one hundred", "Cien es one hundred."),
    ],
    task("Lee este modelo: «There are 30 children in the park. There is an apple on the bench. There are a lot of birds.» Escribe en tu hoja tres oraciones sobre tu casa o tu sala de clases: una con there is a/an, una con there are y un número hasta 1.000 escrito en letras (por ejemplo thirty o two hundred), y otra con a lot of.", "There is an egg in the kitchen. There are twenty-five chairs in my classroom. There are a lot of books in the library.", ["usa a o an correctamente", "usa there is con uno y there are con varios", "escribe el número en letras con guion si corresponde"], ["hoja con tres oraciones"], ["usar a ante vocal", "mezclar is con plural"], "Revisa juntos el número: lo lee en voz alta y lo escribe otra vez en cifras."),
    "Cuenta con una persona de tu casa cuántos libros o cuadernos hay en una repisa y escribe «There are ... books».",
    "Escribe en letras los números 17, 70, 99, 150, 600 y 1.000.",
)

# ================================================================ OA 12 clase 3: pedir información, ocupaciones y vestimenta
lesson(
    OA, 3,
    "Los diálogos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a preguntar y responder con how old, what, where, is he y are they, y a hablar de ocupaciones y de la ropa que alguien lleva. Sirve para pedir y dar información sobre personas.",
    ["Conozco las formas de to be: is y are.", "Sé responder yes y no."],
    [
        "Para pedir información se usan preguntas: «How old is Tom?» (¿Cuántos años tiene Tom?), «What is it?» (¿Qué es?), «Where is the nurse?» (¿Dónde está la enfermera?). Con is y are también se hacen preguntas de sí o no: «Is he a doctor?», «Are they vets?».",
        "Las respuestas cortas repiten is o are: «Yes, he is», «No, he isn't», «Yes, they are», «No, they aren't». Isn't es is not y aren't es are not. Las ocupaciones son nurse (enfermero/a), doctor (médico/a), vet (veterinario/a), teacher (profesor/a) y firefighter (bombero/a). Un hospital es donde trabajan médicos y enfermeras.",
        "Para hablar de ropa se pregunta «What's he wearing?» (¿Qué lleva puesto?) y se responde «He's wearing a jacket» (Lleva una chaqueta). También hay uniform (uniforme). Así identificas a una persona por lo que hace y por lo que lleva puesto.",
    ],
    [("How old is…?", "¿Cuántos años tiene…?"), ("Where is…?", "¿Dónde está…?"), ("nurse / doctor / vet", "enfermero(a) / médico(a) / veterinario(a)"), ("teacher / firefighter", "profesor(a) / bombero(a)"), ("hospital", "hospital"), ("What's he wearing?", "¿Qué lleva puesto?"), ("jacket / uniform", "chaqueta / uniforme")],
    [
        ("Responder una pregunta de sí o no", "«Are they vets?» Se sabe que Ana y Leo son veterinarios y que la pregunta es sobre ellos. Escribe la respuesta corta.", ["La pregunta usa Are y they.", "Son vets: la respuesta es positiva.", "Yes, they are."], "Yes, they are"),
        ("Hablar de la ropa", "«What's Sara wearing?» Sara lleva una chaqueta roja. Escribe la respuesta.", ["Se responde con She's wearing.", "El dato es una chaqueta roja.", "Queda: She's wearing a red jacket."], "She's wearing a red jacket"),
    ],
    [
        ("Responder «Yes, he's» a «Is he a doctor?».", "La respuesta corta afirmativa no se contrae.", "Se dice Yes, he is."),
        ("Decir «She wearing a jacket».", "Falta is.", "Se dice She's wearing a jacket (She is wearing)."),
    ],
    [
        ("¿Qué significa «nurse»?", "Enfermero o enfermera", "Nurse cuida a las personas enfermas."),
        ("¿Qué significa «vet»?", "Veterinario o veterinaria", "Vet cuida a los animales."),
        ("¿Qué significa «What's he wearing?»", "¿Qué lleva puesto?", "Wearing es llevar puesto."),
    ],
    [
        ("«A: How old is Tom? B: He is ten.» ¿Qué dato entrega B?", "La edad de Tom", "How old pregunta por la edad."),
        ("«A: Where is the nurse? B: She is at the hospital.» ¿Dónde está la enfermera?", "En el hospital", "At the hospital es en el hospital."),
        ("Completa: «Is he a doctor? Yes, he ___.»", "is", "La respuesta corta repite is."),
    ],
    [
        ("«Are they teachers? No, they ___.» Completa con is, are, isn't o aren't.", "aren't", "La respuesta es negativa y el sujeto es plural."),
        ("Completa: «What's Sara wearing? She's wearing a red ___.» Opciones: jacket, nurse.", "jacket", "Jacket es una prenda de ropa."),
        ("Lee cuida animales enfermos. ¿Cuál es su ocupación: teacher, vet o nurse?", "vet", "Vet es quien cuida animales."),
    ],
    [
        ("Diálogo: «A: Is Ana a nurse? B: Yes, she is. A: Are Ana and Leo nurses? B: No, they aren't.» ¿Qué dato es verdadero? a) Ana is a nurse. b) Ana and Leo are nurses.", "a", "Ana es enfermera, pero Ana y Leo juntos no lo son."),
        ("¿Cuál es la respuesta correcta a «Are they teachers?» cuando sí lo son? a) Yes, they are. b) Yes, they is.", "a", "Con they se usa are."),
    ],
    [
        ("Diálogo: «A: How old is Lucas? B: He's eleven. A: What's he wearing? B: He's wearing a uniform.» ¿Qué edad tiene Lucas y qué lleva puesto?", "11 años y un uniforme", "El diálogo dice eleven y a uniform."),
        ("Ordena para formar una pregunta: wearing / she / What's / ?", "What's she wearing?", "La pregunta comienza con What's y sigue con el sujeto."),
    ],
    [("En el hospital, una enfermera lleva un uniforme blanco. Un niño pregunta: «What's the nurse wearing?» Completa la respuesta: «She's wearing a white ___.»", "uniform", "El texto dice que lleva un uniforme blanco.")],
    [
        ("¿Cómo se pregunta la edad en inglés? Completa: «How ___ is he?»", "old", "How old pregunta por la edad."),
        ("¿Qué significa «uniform»?", "Uniforme", "Es la ropa que se usa para un trabajo o una escuela."),
        ("¿Cómo respondes «Is he a vet?» si es verdad?", "Yes, he is", "La respuesta corta repite is."),
    ],
    task("Lee este modelo: «A: Is she a nurse? B: Yes, she is. A: What's she wearing? B: She's wearing a white uniform.» Con tu hoja, escribe un diálogo de cuatro líneas entre dos personas sobre un vet, un teacher o un firefighter. Incluye una pregunta con Is o Are, una respuesta corta y una pregunta con What's … wearing?", "A: Is he a firefighter? B: Yes, he is. A: What's he wearing? B: He's wearing a red jacket.", ["la pregunta con is/are tiene su respuesta corta", "usa What's … wearing? y She's/He's wearing", "los datos se entienden"], ["hoja con el diálogo de cuatro líneas"], ["decir She wearing sin is", "responder con Yes, he's"], "Pide que lea el diálogo con otra persona y que cambie la ocupación."),
    "Mira a una persona de tu casa y di en inglés qué lleva puesto: «He/She is wearing ...».",
    "Escribe un diálogo en que alguien pregunta cuántos años tiene una persona, dónde trabaja y qué lleva puesto.",
)

# ================================================================ OA 12 clase 4: gustos, personalidad, estados y opiniones
lesson(
    OA, 4,
    "Los diálogos y listas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a decir lo que me gusta y lo que no, a describir cómo es una persona o cómo se siente, y a explicar mi opinión con because. Sirve para conversar sobre gustos y dar razones.",
    ["Conozco la palabra like.", "Sé que is y am se usan para describir."],
    [
        "Para decir un gusto se usa «I like…» y para decir que algo no te gusta, «I don't like…». Para preguntar: «Do you like soccer?» y se responde «Yes, I do» o «No, I don't». Para explicar por qué, se pregunta «Why do you like it?» y se responde con because (porque): «Because it's fun» (porque es entretenido).",
        "Para describir cómo es una persona se usa is con adjetivos: quiet (callado), friendly (amistoso) y funny (divertido): «Pedro is friendly». Para decir cómo te sientes se usa feel: «I feel sad» (triste), «I feel angry» (enojado), «I feel tired» (cansado), «I feel bored» (aburrido).",
        "Cuando das una opinión, la razón (reason) debe tener sentido con lo que dijiste. «I like dogs because they are friendly» es una buena razón. Escucha la pregunta: why pide una razón; do you pide sí o no.",
    ],
    [("I like / I don't like", "me gusta / no me gusta"), ("Why…? Because…", "¿Por qué…? Porque…"), ("fun", "entretenido"), ("quiet / friendly / funny", "callado / amistoso / divertido"), ("sad / angry / tired / bored", "triste / enojado / cansado / aburrido"), ("I feel…", "me siento…")],
    [
        ("Dar una razón", "«Why do you like music?» Completa: «___ it's fun.»", ["Why pide una razón.", "La razón empieza con la palabra porque en inglés.", "Because it's fun."], "Because"),
        ("Describir cómo se siente", "Pablo no durmió bien y bosteza todo el día. Completa: «I feel ___.» Opciones: tired, angry.", ["Mal sueño provoca cansancio.", "Tired es cansado.", "I feel tired."], "tired"),
    ],
    [
        ("Responder «Yes, I like» a «Do you like soccer?».", "La respuesta corta usa do.", "Se dice Yes, I do."),
        ("Responder «Yes, I do» a «Why do you like soccer?».", "Why pide una razón, no sí o no.", "Se dice Because it's fun."),
    ],
    [
        ("¿Qué significa «I don't like»?", "No me gusta", "Don't like es lo contrario de like."),
        ("¿Qué significa «tired»?", "Cansado", "Se siente después de un día largo."),
        ("¿Qué significa «because»?", "Porque", "Se usa para dar una razón."),
    ],
    [
        ("«Do you like soccer? Yes, I ___.» Completa con do o don't.", "do", "La respuesta afirmativa repite do."),
        ("Pedro habla con todos y sonríe siempre. ¿Qué palabra lo describe mejor: friendly o quiet?", "friendly", "Friendly es amistoso."),
        ("Marcos tiene miedo de las arañas y no le gustan. Completa: «I ___ like spiders.» (spiders = arañas)", "don't", "No le gustan, entonces va don't."),
    ],
    [
        ("Hoy no tengo nada que hacer. Completa: «I feel ___.» Opciones: bored, tired.", "bored", "No tener qué hacer produce aburrimiento."),
        ("Completa: «Why do you like painting? ___ it's relaxing.» (relaxing = relajante)", "Because", "Se necesita because para dar la razón."),
        ("Mi equipo perdió el partido. Completa: «I feel ___.» Opciones: sad, funny.", "sad", "Perder un partido puede dar tristeza."),
    ],
    [
        ("«Why do you like pizza?» ¿Qué respuesta da una razón? a) Because it's delicious. b) Yes, I do.", "a", "La a explica por qué; la b responde sí o no."),
        ("Mía dice: «I like dogs because they are friendly.» ¿Qué palabra da la razón?", "friendly", "Es el rasgo que explica por qué le gustan."),
    ],
    [
        ("Ordena las líneas para formar un diálogo: a) Yes, I do. b) Do you like basketball? c) Because it's fun. d) Why? Escribe las letras en orden.", "b, a, d, c", "Primero se pregunta, luego se responde, luego se pide la razón y se da."),
        ("«Leo is quiet. Ana is friendly. Tom is funny.» ¿Cuántas palabras de personalidad hay?", "3", "Son quiet, friendly y funny."),
    ],
    [("Camila dice: «It's raining, I can't go out and I have nothing to do. I feel ___.» Opciones: bored, angry.", "bored", "La pista es que no tiene nada que hacer.")],
    [
        ("¿Qué pide la palabra Why?", "Una razón", "Se responde con because."),
        ("¿Qué significa «friendly»?", "Amistoso", "Describe a una persona agradable con otras."),
        ("¿Cómo se dice «Me siento triste» en inglés?", "I feel sad", "Feel sad es sentirse triste."),
    ],
    task("Lee este modelo: «A: Do you like music? B: Yes, I do. A: Why? B: Because it's fun.» Escribe en tu hoja un diálogo de cuatro líneas sobre algo que te gusta o no te gusta. Incluye una pregunta con Why? y una respuesta con Because. Añade una oración final sobre cómo te sientes, por ejemplo I feel tired.", "A: Do you like soccer? B: No, I don't. A: Why? B: Because I feel tired when I run. I feel bored.", ["responde con do o don't", "la razón empieza con because y tiene sentido", "usa I feel + una palabra de estado"], ["hoja con el diálogo"], ["responder Why con sí o no", "olvidar because"], "Escucha la razón y pregunta si realmente explica el gusto."),
    "Haz una lista de tres cosas que te gustan y tres que no, con I like y I don't like.",
    "Describe a tres personas que conoces con quiet, friendly o funny, y di por qué.",
)

# ================================================================ OA 12 clase 5: la hora, acciones ahora y acciones en el pasado
lesson(
    OA, 5,
    "Los diálogos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a pedir y decir la hora en punto, a preguntar qué está haciendo alguien ahora y a contar qué pasó antes con was, were, made, did y felt. Sirve para mantener diálogos más largos.",
    ["Conozco las formas is y are.", "Sé leer un reloj en punto."],
    [
        "Para preguntar la hora se dice «What time is it?» y se responde «It's four o'clock» (son las cuatro en punto). Para preguntar qué hace alguien ahora se usa is o are y el verbo con -ing: «Is he reading?», «Are they playing?». Las respuestas son «Yes, he is», «No, he isn't», «Yes, they are», «No, they aren't».",
        "Para contar lo que pasó antes se usa el pasado. De be: I was, he was, we were, you were, they were. Algunos verbos cambian: make se convierte en made (hice), do se convierte en did (hice) y feel se convierte en felt (me sentí). «Yesterday I made a cake» significa «Ayer hice una torta».",
        "Para decidir si algo es de ahora o del pasado, busca la pista de tiempo: now (ahora), today (hoy), yesterday (ayer) o last night (anoche). El diálogo mezcla las tres ideas: la hora, lo que pasa ahora y lo que pasó.",
    ],
    [("What time is it?", "¿Qué hora es?"), ("It's … o'clock", "Son las … en punto"), ("reading / playing", "leyendo / jugando"), ("was / were", "estaba, estuve / estaban, estuvieron"), ("made / did / felt", "hice / hice / sentí"), ("now / yesterday", "ahora / ayer")],
    [
        ("Decir la hora", "El reloj marca las 9 en punto. Responde «What time is it?».", ["Uso It's.", "El número es nine.", "Digo o'clock al final."], "It's nine o'clock"),
        ("Elegir presente o pasado", "«Yesterday I ___ a cake.» Opciones: make, made.", ["La pista es yesterday.", "Se necesita pasado.", "El pasado de make es made."], "made"),
    ],
    [
        ("Decir «It's four o'clock» cuando son las cuatro y media.", "o'clock solo sirve para la hora en punto.", "Usa o'clock solo cuando la hora es exacta."),
        ("Decir «Yesterday I make a cake».", "Se usa el presente con una pista de pasado.", "Con yesterday se usa made."),
    ],
    [
        ("¿Qué significa «What time is it?»", "¿Qué hora es?", "Se usa para pedir la hora."),
        ("¿Cómo se dice «Son las 4 en punto»?", "It's four o'clock", "Se usa It's y o'clock."),
        ("¿Qué significa «felt»?", "Sentí (pasado de feel)", "Es el pasado de feel."),
    ],
    [
        ("«Is she reading? No, she ___.» Completa con isn't o aren't.", "isn't", "She va con is."),
        ("«Yesterday I ___ tired.» Opciones: was, were.", "was", "I va con was."),
        ("Completa: «Yesterday I ___ my homework.» Opciones: do, did.", "did", "Yesterday indica pasado."),
    ],
    [
        ("Seis niños patean un balón en una cancha. Responde: «Are they playing soccer?»", "Yes, they are", "La situación muestra que sí juegan."),
        ("La clase empieza a las 8 en punto y son las 7 en punto. Responde en inglés: «Is it late?»", "No, it isn't", "Todavía falta una hora."),
        ("¿Cuál oración habla del pasado? a) I made a cake. b) I make a cake.", "a", "Made es el pasado de make."),
    ],
    [
        ("Pedro dice: «Now I did my homework». ¿Cuál es el error?", "Now indica presente y did es pasado", "La pista de tiempo no coincide con el verbo."),
        ("¿Cuál oración es del presente? a) He is reading now. b) He felt tired yesterday.", "a", "Is reading y now indican presente."),
    ],
    [
        ("Diálogo: «A: Is Ana drawing? B: No, she isn't. She is playing. A: What time is it? B: It's five o'clock.» ¿Qué hace Ana ahora?", "Está jugando", "B dice She is playing."),
        ("En el mismo diálogo, ¿qué hora es?", "Las 5 en punto", "It's five o'clock."),
    ],
    [("Un amigo pregunta por teléfono a Camila: «What time is it? Is Leo sleeping?». Ella mira el reloj, que marca las 6 en punto, y ve que Leo está durmiendo. ¿Qué responde a la segunda pregunta?", "Yes, he is", "La situación muestra que Leo duerme.")],
    [
        ("¿Qué significa «yesterday»?", "Ayer", "Es una pista de pasado."),
        ("¿Cuál es el pasado de be con they?", "were", "They va con were."),
        ("¿Cómo respondes «Are they playing?» si es verdad?", "Yes, they are", "La respuesta repite are."),
    ],
    task("Lee este modelo: «A: What time is it? B: It's three o'clock. A: Is Tom reading? B: Yes, he is. A: Were you tired yesterday? B: Yes, I was. I felt tired.» Escribe en tu hoja un diálogo de seis líneas con una pregunta de la hora, una pregunta con Is o Are y una pregunta sobre ayer, usando was, made, did o felt.", "A: What time is it? B: It's seven o'clock. A: Are they eating? B: No, they aren't. A: Were you at home yesterday? B: Yes, I was. I made a cake.", ["incluye hora en punto", "usa Is o Are con -ing y su respuesta corta", "usa un verbo en pasado con una pista de tiempo"], ["hoja con el diálogo"], ["usar o'clock con medias horas", "mezclar presente con yesterday"], "Marca la pista de tiempo de cada línea y comprueba que el verbo concuerda."),
    "Pregunta a una persona de tu casa «What time is it?» y responde en inglés sin mirar la respuesta escrita.",
    "Escribe cuatro oraciones sobre ayer con was, made, did y felt.",
)
