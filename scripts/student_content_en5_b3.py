"""Cuaderno del estudiante, 5.º básico Inglés (propuesta): EN05 OA 13 (textos literarios y funcionales con modelo).

Los textos en inglés son originales, muy breves y llevan pista en español. Cada palabra o estructura se enseña en la propia
clase antes de usarla. Sin audio externo: todo lo que hay que leer está escrito en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA = "EN05 OA 13"


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


# ================================================================ OA 13 clase 1: email y postal
lesson(
    OA, 1,
    "Los modelos de texto escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé las partes de un email y de una postal (saludo, mensaje y despedida) y a escribir uno siguiendo un modelo. Sirve para compartir información con una persona lejana.",
    ["Sé escribir oraciones cortas en inglés.", "Conozco palabras como school, Art, Music y sunny."],
    [
        "Un email es un mensaje escrito que se envía por internet. Tiene un destinatario (To), un asunto (Subject) que dice de qué trata, un saludo (Hi Ana, o Dear Ana), el mensaje y una despedida con tu nombre (Best wishes, Tomás). Una postal (postcard) es una tarjeta corta que se envía desde un lugar y sigue la misma idea con menos espacio.",
        "Modelo de email: «To: Ana. Subject: My new school. Hi Ana, I am in a new school. I like Art and Music. My teacher is friendly. Please write to me. Best wishes, Tomás.» Las oraciones son cortas, comienzan con mayúscula y terminan en punto.",
        "Para escribir tu propio texto copia la estructura del modelo y cambia los datos. No uses direcciones de correo reales ni datos privados: usa nombres inventados. Algunas despedidas útiles son Best wishes, See you soon y Love (con mucho cariño).",
    ],
    [("email", "correo electrónico"), ("subject", "asunto: de qué trata el mensaje"), ("Hi / Dear", "Hola / Querido(a)"), ("Best wishes / See you soon", "Saludos / Hasta pronto"), ("postcard", "postal"), ("please write to me", "por favor escríbeme")],
    [
        ("Encontrar las partes del email", "En el modelo, ¿qué línea dice de qué trata el mensaje?", ["Busco la palabra Subject.", "Después de Subject dice My new school.", "Esa línea resume el tema."], "Subject: My new school"),
        ("Ordenar las partes", "Ordena: a) Best wishes, Tomás b) Hi Ana, c) I am in a new school. Escribe las letras en orden.", ["Primero va el saludo.", "Luego el mensaje.", "Al final la despedida."], "b, c, a"),
    ],
    [
        ("Escribir el email sin saludo ni despedida.", "Se pierde la estructura del texto.", "Escribe siempre saludo, mensaje y despedida."),
        ("Escribir una dirección real de correo en el modelo.", "Es un dato privado.", "Usa nombres inventados y no escribas datos privados."),
    ],
    [
        ("¿Qué significa «subject» en un email?", "Asunto", "Dice de qué trata el mensaje."),
        ("¿Cuál es el saludo: «Hi Ana,» o «Best wishes,»?", "Hi Ana,", "Hi Ana abre el mensaje."),
        ("¿Qué es una «postcard»?", "Una postal", "Es una tarjeta corta que se envía desde un lugar."),
    ],
    [
        ("En el modelo, ¿quién escribe el email?", "Tomás", "Tomás firma la despedida."),
        ("En el modelo, ¿qué asignaturas le gustan a Tomás?", "Art y Music", "El mensaje dice I like Art and Music."),
        ("¿Cómo es su profesora o profesor según el modelo?", "Friendly", "El modelo dice My teacher is friendly."),
    ],
    [
        ("Completa el saludo: «___ Ana,» Opciones: Hi, Bye.", "Hi", "Hi es un saludo al comienzo."),
        ("Escribe la despedida del modelo con tu nombre inventado Sofía: Best wishes, ___", "Sofía", "La despedida termina con el nombre de quien escribe."),
        ("Completa la postal: «Hi Sara! I am at the ___. It is very hot.» Opciones: beach, snow.", "beach", "Hot (calor) calza con la playa."),
    ],
    [
        ("¿Cuál tiene saludo, mensaje y despedida? a) Hi Pablo! I am at the beach. See you soon, Ana. b) I am at the beach.", "a", "La b no tiene saludo ni despedida."),
        ("Un email sin Subject. ¿Qué problema tiene? a) Quien lo recibe no sabe de qué trata antes de abrirlo. b) No se puede escribir.", "a", "El asunto avisa el tema."),
    ],
    [
        ("Mensaje: «Hi Leo, Today I am at the park with my dog. It's sunny. See you tomorrow, Marta.» ¿Cuántas oraciones tiene el mensaje sin contar saludo ni despedida? (sunny = soleado)", "2", "Las oraciones son Today I am at the park with my dog e It's sunny."),
        ("En ese mensaje, ¿quién recibe el email?", "Leo", "El saludo dice Hi Leo."),
    ],
    [("Luisa escribe un email a su amiga Rosa para contarle que celebró su cumpleaños. ¿Qué asunto es mejor? a) My birthday party b) Hi", "a", "El asunto debe resumir el tema.")],
    [
        ("¿Qué significa «Best wishes»?", "Saludos", "Es una despedida amable."),
        ("¿Dónde va el nombre de quien escribe?", "Al final, en la despedida", "Así se sabe quién escribió."),
        ("¿Qué datos no debes escribir en un email de práctica?", "Datos privados como direcciones reales", "Se protege la privacidad."),
    ],
    task("Lee este modelo: «To: Ana. Subject: My new school. Hi Ana, I am in a new school. I like Art and Music. My teacher is friendly. Please write to me. Best wishes, Tomás.» Escribe en tu hoja un email corto o una postal (inventando nombres) a un amigo, con: To, Subject, saludo, tres oraciones y despedida. Cambia el tema: por ejemplo, un viaje a la playa o tu nueva mascota.", "To: Leo. Subject: My holiday. Hi Leo, I am at the beach. The water is cold. I play with my cousin. See you soon, Sofía.", ["incluye To, Subject, saludo y despedida", "tres oraciones con mayúscula y punto", "el mensaje cuenta información coherente con el asunto"], ["hoja con el email o la postal"], ["olvidar el asunto", "poner datos privados"], "Pide que explique para qué sirve cada parte que escribió."),
    "Escribe una postal de dos oraciones a una persona de tu casa contando algo del día.",
    "Escribe un email de respuesta a Tomás contando de tu escuela, con las mismas partes del modelo.",
)

# ================================================================ OA 13 clase 2: agenda e invitación
lesson(
    OA, 2,
    "Los modelos de agenda e invitación escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir una agenda y una invitación con el día, la hora y el lugar. Sirve para informar a otras personas cuándo y dónde pasa algo.",
    ["Conozco los días de la semana en inglés.", "Sé leer horas como 3 p.m."],
    [
        "Una agenda (agenda) es una lista de actividades por día. Lleva el día, la actividad y la hora: «Tuesday: Art club at 3 p.m.». Los días son Monday, Tuesday, Wednesday, Thursday, Friday, Saturday y Sunday. Con la hora se usa a.m. antes del mediodía y p.m. después.",
        "Una invitación (invitation) avisa de un evento. Lleva a quién se invita, de qué es, la fecha o el día (date), la hora (time) y el lugar (place), y una petición educada: «Please come!». Modelo: «Hi Sam! You are invited to my birthday party. Date: Saturday. Time: 4 p.m. Place: my house. Please come! Ana.»",
        "Antes de escribir, revisa que no falte ningún dato: sin la hora o el lugar, la persona no sabe cuándo ni a dónde ir. Usa on con los días (on Friday), at con las horas (at 4 p.m.) y at o in con los lugares (at the school library).",
    ],
    [("agenda", "lista de actividades por día"), ("invitation", "invitación"), ("You are invited to…", "Estás invitado(a) a…"), ("date / time / place", "fecha / hora / lugar"), ("Please come!", "¡Por favor ven!"), ("a.m. / p.m.", "antes del mediodía / después del mediodía"), ("on Friday / at 4 p.m.", "el viernes / a las 4 de la tarde")],
    [
        ("Leer una agenda", "Agenda: «Monday: Math test. Tuesday: Art club at 3 p.m. Wednesday: Library. Friday: Birthday party.» (test = prueba). ¿Qué hay el martes?", ["Busco Tuesday.", "Después dice Art club at 3 p.m.", "Esa es la actividad."], "Art club a las 3 p.m."),
        ("Revisar los datos de una invitación", "«Hi Sam! You are invited to my party on Saturday at the park. Please come!» ¿Qué dato falta?", ["Hay día: Saturday.", "Hay lugar: the park.", "No hay hora."], "La hora"),
    ],
    [
        ("Escribir una invitación sin hora ni lugar.", "La persona no sabe cuándo ni a dónde ir.", "Incluye siempre date, time y place."),
        ("Escribir «at Friday» para el día.", "Se usa at con un día.", "Con días se usa on: on Friday."),
    ],
    [
        ("¿Qué significa «invitation»?", "Invitación", "Avisa de un evento."),
        ("¿Qué día es «Tuesday»?", "Martes", "Tuesday es el día entre Monday y Wednesday."),
        ("¿Qué indica «p.m.» en «3 p.m.»?", "Después del mediodía", "Las 3 p.m. son las 3 de la tarde."),
    ],
    [
        ("Agenda: «Monday: Math test. Tuesday: Art club at 3 p.m. Wednesday: Library. Friday: Birthday party.» ¿Qué día es la fiesta (party)?", "Friday", "La línea de Friday dice Birthday party."),
        ("En la misma agenda, ¿a qué hora es el Art club?", "3 p.m.", "La línea de Tuesday indica la hora."),
        ("Invitación: «You are invited to my birthday party. Date: Saturday. Time: 4 p.m. Place: my house.» ¿Cuál es la hora?", "4 p.m.", "El dato Time dice 4 p.m."),
    ],
    [
        ("Completa: «You are ___ to my party.» Opciones: invited, wearing.", "invited", "You are invited es estás invitado."),
        ("Ordena los días de la agenda: Friday, Monday, Wednesday.", "Monday, Wednesday, Friday", "Es el orden de la semana."),
        ("Completa con on o at: «The party is ___ Saturday.»", "on", "Con los días se usa on."),
    ],
    [
        ("«Please come at 4 p.m. on Saturday.» ¿Qué dato falta para saber a dónde ir?", "El lugar", "No dice dónde."),
        ("¿Qué línea de agenda tiene día y hora? a) Thursday: Soccer at 5 p.m. b) Soccer.", "a", "La b no tiene día ni hora."),
    ],
    [
        {"q": "La clase de Music empieza a las 2 p.m. y dura 2 horas. ¿A qué hora (p.m.) termina? Escribe solo el número.", "a": "4", "why": "Se suman las horas de duración a la hora de inicio. Cálculo: 2 + 2 = 4.", "calc": "2+2"},
        ("Agenda: «Monday: Math. Tuesday: Art. Thursday: Music. Friday: Party.» ¿Qué día entre lunes y viernes no tiene actividad?", "Wednesday", "Falta el día que está entre Tuesday y Thursday."),
    ],
    [("La profesora escribe: «You are invited to our class show on Thursday at 11 a.m. in the school hall.» (hall = salón grande). ¿Dónde es el evento?", "En el salón de la escuela", "In the school hall indica el lugar.")],
    [
        ("¿Qué tres datos lleva una invitación?", "Fecha, hora y lugar", "Date, time y place."),
        ("¿Qué significa «Please come!»?", "¡Por favor ven!", "Es una petición educada."),
        ("¿Qué significa «a.m.»?", "Antes del mediodía", "Las 9 a.m. son las 9 de la mañana."),
    ],
    task("Lee este modelo: «Hi Sam! You are invited to my birthday party. Date: Saturday. Time: 4 p.m. Place: my house. Please come! Ana.» Primero escribe una agenda de tres días con una actividad y hora en cada uno (por ejemplo, Monday: Math at 9 a.m.). Después escribe una invitación a una fiesta o juego en la escuela con date, time, place y Please come!", "Agenda: Monday: Art at 9 a.m. Tuesday: Library at 2 p.m. Thursday: Soccer at 4 p.m. Invitación: Hi Leo! You are invited to a game. Date: Friday. Time: 3 p.m. Place: the school yard. Please come! Ana.", ["la agenda tiene día, actividad y hora", "la invitación incluye date, time, place y Please come", "usa on con días y at con horas"], ["hoja con agenda e invitación"], ["omitir la hora o el lugar", "usar at con un día"], "Marca con un visto cada dato y pide que corrija solo lo que falte."),
    "Escribe en una hoja la agenda de tus tres actividades de mañana con su hora.",
    "Escribe una invitación para una reunión con tu curso en la que no falte ningún dato.",
)

# ================================================================ OA 13 clase 3: cuentos y rimas
lesson(
    OA, 3,
    "Los cuentos y rimas modelo escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir un cuento corto con comienzo, desarrollo y final, y una rima de dos pares usando un modelo. Sirve para compartir ideas e historias en inglés.",
    ["Conozco las palabras first, then y finally.", "Sé que dos palabras riman cuando sus finales suenan igual."],
    [
        "Un cuento (story) tiene personajes (characters), un lugar (place) y un orden: comienzo, desarrollo y final. Para ordenar los hechos se usan las palabras first (primero), then (luego), next (después) y finally (finalmente). Modelo: «First, Lia finds a small cat. Then she gives it milk. Next, she calls her friend. Finally, the cat has a new home.»",
        "Una rima (rhyme) usa palabras que terminan con el mismo sonido, por ejemplo cat y mat, o sun y fun. Modelo: «I have a cat. It sits on a mat. I see the sun. We have fun.» Las dos primeras líneas riman entre sí, y las dos últimas también.",
        "Para escribir, copia la estructura del modelo y cambia los personajes, el lugar o los hechos. Después revisa que el orden de los hechos tenga sentido y que las palabras de la rima suenen igual al final.",
    ],
    [("story", "cuento"), ("characters / place", "personajes / lugar"), ("first / then / next / finally", "primero / luego / después / finalmente"), ("rhyme", "rima"), ("small cat", "gato pequeño"), ("new home", "hogar nuevo")],
    [
        ("Ordenar un cuento", "Ordena con las palabras de orden: a) Finally, the cat has a new home. b) First, Lia finds a small cat. c) Then she gives it milk.", ["El comienzo usa First.", "Luego sigue then.", "El final usa Finally."], "b, c, a"),
        ("Completar una rima", "Completa para que rime: «I have a cat. It sits on a ___.» Opciones: mat, tree.", ["Cat termina en -at.", "Mat termina en -at.", "Tree no rima."], "mat"),
    ],
    [
        ("Contar los hechos sin orden claro.", "No se usan palabras de orden.", "Usa first, then, next y finally."),
        ("Terminar una rima con palabras que suenan distinto, como cat y tree.", "No se escucha el final de la palabra.", "Elige palabras con el mismo final, como cat y mat."),
    ],
    [
        ("¿Qué significa «finally»?", "Finalmente", "Se usa para el último hecho."),
        ("¿Qué palabra de orden usas al comienzo de un cuento: first o finally?", "first", "First es primero."),
        ("¿Riman «sun» y «fun»?", "Sí", "Ambas terminan con el mismo sonido."),
    ],
    [
        ("Lee el modelo del cuento: ¿qué encuentra Lia primero?", "Un gato pequeño", "La primera oración dice Lia finds a small cat."),
        ("¿Qué le da Lia al gato?", "Leche", "Then she gives it milk."),
        ("¿Cómo termina el cuento del modelo?", "El gato tiene un hogar nuevo", "Finally, the cat has a new home."),
    ],
    [
        ("Completa para que rime: «Look at my kite. It is red and ___.» Opciones: bright, tree.", "bright", "Kite y bright terminan igual."),
        ("Completa con una palabra de orden: «___, Lia finds a small cat.»", "First", "Es el comienzo del cuento."),
        ("¿Cuál palabra rima con «mat»: hat o dog?", "hat", "Mat y hat terminan en -at."),
    ],
    [
        ("Pedro escribe: «First, the cat has a new home. Finally, Lia finds the cat.» ¿Qué error hay?", "El orden de los hechos no tiene sentido", "No se puede tener un hogar antes de encontrar al gato."),
        ("¿Cuáles son dos líneas que riman? a) I see the sun. We have fun. b) I see the sun. We eat a cake.", "a", "Sun y fun riman; sun y cake no."),
    ],
    [
        ("Cuento corto: «First, Omar sees a bird. Then it flies. Next, it sits on a tree. Finally, it sings.» ¿Cuántos hechos tiene el cuento?", "4", "Hay cuatro hechos, uno por cada palabra de orden."),
        ("Rima: «I like to read. I plant a seed.» ¿Cuáles son las palabras que riman?", "read y seed", "Terminan con el mismo sonido."),
    ],
    [("Una profesora pide un cuento de tres hechos sobre un perro. Un niño escribe: «First, a dog runs. Then it jumps. Finally, it sleeps.» ¿Qué hace el perro justo antes de dormir?", "Salta", "Then it jumps viene antes de finally.")],
    [
        ("¿Cuántas partes principales tiene un cuento (comienzo, desarrollo y final)?", "3", "Son comienzo, desarrollo y final."),
        ("¿Cuál palabra rima con «cat»: mat o dog?", "mat", "Cat y mat terminan igual."),
        ("¿Qué significa «characters»?", "Personajes", "Son quienes participan en el cuento."),
    ],
    task("Lee este modelo: «First, Lia finds a small cat. Then she gives it milk. Next, she calls her friend. Finally, the cat has a new home.» Escribe en tu hoja un cuento de cuatro oraciones con First, Then, Next y Finally sobre otro personaje (por ejemplo, un niño y un pájaro). Luego escribe una rima de dos líneas, por ejemplo «I see a bee. It sits on a tree.»", "First, Omar finds a small bird. Then he gives it water. Next, he calls his teacher. Finally, the bird flies home. Rima: I see a bee. It sits on a tree.", ["usa las cuatro palabras de orden", "los hechos tienen un orden con sentido", "la rima tiene dos palabras que suenan igual al final"], ["hoja con el cuento y la rima"], ["desordenar los hechos", "rimar palabras con finales distintos"], "Lee con la persona el cuento en voz alta para comprobar el orden."),
    "Pide a una persona de tu casa que te diga tres hechos de su día y ordénalos con first, then y finally.",
    "Escribe dos rimas de dos líneas cada una, con los pares moon-spoon y day-play.",
)

# ================================================================ OA 13 clase 4: tiras cómicas
lesson(
    OA, 4,
    "Las tiras cómicas descritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir los diálogos de una tira cómica corta, con viñetas y globos de diálogo. Sirve para contar una situación con pocas palabras y con ayuda del dibujo.",
    ["Conozco expresiones como Hello, Let's go y I'm hungry.", "Sé que dos personajes pueden hablar por turnos."],
    [
        "Una tira cómica (comic strip) cuenta una historia corta en cuadros llamados viñetas (panels). En cada viñeta hay personajes y, a veces, un globo de diálogo (speech bubble) con lo que dicen. Las viñetas se leen en orden, de izquierda a derecha.",
        "Aquí cada viñeta se describe con texto, para que puedas trabajar sin dibujos. Modelo: «Panel 1: Cat: I'm hungry! Panel 2: Dog: Me too! Panel 3: Cat and Dog: Let's eat!» (hungry = con hambre, me too = yo también, let's eat = comamos).",
        "Para escribir tu propia tira, decide los personajes, el problema y el final. Los globos tienen frases muy cortas. El dibujo muestra la acción; el texto agrega solo lo necesario. Usa signos de exclamación (!) o de pregunta (?) para dar la emoción.",
    ],
    [("comic strip", "tira cómica"), ("panel", "viñeta"), ("speech bubble", "globo de diálogo"), ("I'm hungry!", "¡Tengo hambre!"), ("Me too!", "¡Yo también!"), ("Let's eat!", "¡Comamos!")],
    [
        ("Saber quién habla", "Mira el modelo. ¿Quién dice «Me too!»?", ["Busco la viñeta 2.", "Después de Panel 2 dice Dog.", "Dog es quien habla."], "Dog"),
        ("Ordenar las viñetas", "Ordena: a) Cat and Dog: Let's eat! b) Cat: I'm hungry! c) Dog: Me too! Escribe las letras en orden.", ["Primero se dice el problema.", "Luego la reacción.", "Al final la solución."], "b, c, a"),
    ],
    [
        ("Escribir globos con mucho texto.", "El globo es pequeño y el lector se pierde.", "Usa frases muy cortas."),
        ("Mezclar el orden de las viñetas.", "La historia pierde sentido.", "Lee de izquierda a derecha y ordena los hechos."),
    ],
    [
        ("¿Qué es una «panel»?", "Una viñeta", "Es cada cuadro de la tira cómica."),
        ("¿Qué es un «speech bubble»?", "Un globo de diálogo", "Contiene lo que dice un personaje."),
        ("¿Qué significa «I'm hungry!»?", "¡Tengo hambre!", "Hungry es hambriento."),
    ],
    [
        ("En el modelo, ¿quién tiene hambre al principio?", "Cat", "En el panel 1 Cat dice I'm hungry."),
        ("En el modelo, ¿cuántas viñetas hay?", "3", "Son los paneles 1, 2 y 3."),
        ("¿Qué dicen Cat y Dog juntos al final?", "Let's eat!", "Es la frase de la viñeta 3."),
    ],
    [
        ("Lee la tira: «Panel 1: Bird: I'm cold! Panel 2: Sun: Come here!» ¿Qué estaba sintiendo el pájaro? (cold = frío)", "Frío", "I'm cold significa tengo frío."),
        ("Completa el globo del perro que quiere jugar: «Panel 1: Dog: Let's ___!» Opciones: play, sleep.", "play", "El perro quiere jugar."),
        ("Panel: «Teacher: Open your books!» ¿Qué le pide el profesor? (open = abrir)", "Que abran sus libros", "Open your books es abre tus libros."),
    ],
    [
        ("Tira: «Panel 1: Mouse: Where's my cheese? Panel 2: Cat: I don't know. Panel 3: Mouse: Here it is!» ¿Qué problema aparece en la viñeta 1? (cheese = queso)", "El ratón no encuentra su queso", "Where's my cheese? es dónde está mi queso."),
        ("¿Cuál globo es más adecuado en una tira cómica? a) Hi! b) Hi! I am very happy to see you because we have not seen each other for many days and I want to tell you many things.", "a", "Los globos deben ser cortos."),
    ],
    [
        ("Tira: «Panel 1: Girl: I'm tired. Panel 2: Boy: Sit down. Panel 3: Girl: Thank you!» ¿Cuántas veces habla la niña?", "2", "Habla en las viñetas 1 y 3."),
        ("En esa tira, ¿qué le sugiere el niño a la niña?", "Que se siente", "Sit down es siéntate."),
    ],
    [("Una amiga dibuja una tira con tres viñetas y escribe en la última: «Cat and Dog: See you tomorrow!» ¿Qué sentido tiene la viñeta?", "Es la despedida final", "See you tomorrow cierra la historia.")],
    [
        ("¿En qué orden se leen las viñetas?", "De izquierda a derecha", "Así se sigue la historia."),
        ("¿Qué significa «Me too»?", "Yo también", "Se usa para estar de acuerdo."),
        ("¿Qué signo se usa para dar emoción en un globo?", "El signo de exclamación", "Se escribe ! al final."),
    ],
    task("Lee este modelo: «Panel 1: Cat: I'm hungry! Panel 2: Dog: Me too! Panel 3: Cat and Dog: Let's eat!» Escribe en tu hoja una tira cómica de tres viñetas con dos personajes. Cada viñeta tiene una frase corta. Puedes dibujar los personajes al lado o dejar solo el texto. Ideas: un problema (I'm cold, I'm lost), una reacción y una solución.", "Panel 1: Bird: I'm cold! Panel 2: Sun: Come here! Panel 3: Bird: Thank you!", ["tiene tres viñetas en orden", "las frases son cortas y se entienden", "hay un problema y un final"], ["hoja con la tira cómica"], ["globos largos", "no tener final"], "Lee la tira en voz alta con la persona; pregunta qué problema se resolvió."),
    "Dibuja tres cuadros y escribe en cada uno una frase del modelo del gato y el perro.",
    "Escribe una segunda tira cómica de cuatro viñetas con un final divertido.",
)
