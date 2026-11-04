"""Cuaderno del estudiante, 1.º medio Inglés (propuesta), EN1M OA 01 (textos orales en distintos formatos) y OA 02 (propósito, detalle, lenguaje y sonidos al escuchar).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales, con pista en español. Los títulos de las clases del plan son genéricos; aquí cada clase recorre
un grupo de formatos o de contenidos que nombra el OA.
"""
from __future__ import annotations

import re

import student_lessons as sl
from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1, OA2 = "EN1M OA 01", "EN1M OA 02"
ADULT = "Un adulto lee en voz alta (tapa el guion): "


_OPT = re.compile(r"(?:(?<=\s)|^)(\(?)([AaBbCc])(\)|\.)(?=\s)")


def _tidy(item):
    """Quita la puntuación final de las opciones A)/B)/C) para que el balanceo automático no duplique puntos."""
    q = item["q"]
    marks = list(_OPT.finditer(q))
    letters = [m.group(2).upper() for m in marks]
    if letters not in (["A", "B"], ["A", "B", "C"]) or sl._is_matching(q, str(item["a"])):
        return item
    parts = [q[:marks[0].start()]]
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(q)
        seg = re.sub(r"[\s.?!]+$", "", q[m.end():end].strip())
        parts.append(f"{m.group(1)}{m.group(2)}{m.group(3)} {seg}")
    item["q"] = "".join(parts[:1]) + " ".join(parts[1:])
    if re.match(r"^\(?[A-Ca-c][\).]\s", str(item["a"])):
        item["a"] = re.sub(r"[\s.?!]+$", "", item["a"])
    return item


def E(rows):
    return [_tidy(r if isinstance(r, dict) else ex(*r)) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


MAT = "Los guiones escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz."

# ================================================================ OA 01 · clase 1: avisos, anécdotas y descripciones
CAFE = "«Do you want a fresh snack? Come to the school café this week. Every fruit smoothie costs two thousand pesos. We are open from eight to six, Monday to Friday. Bring a friend and you both get a free cookie!» (fresh = fresco, smoothie = batido de frutas, costs = cuesta, open = abierto, free = gratis, cookie = galleta)"
BACKPACK = "«Two years ago, I lost my backpack at the bus terminal. A driver found it and called my mother. Since then, I always write my phone number inside my bags. It was a good lesson.» (lost = perdí, found = encontró, called = llamó, since then = desde entonces, lesson = lección)"
KITCHEN = "«My grandmother's kitchen is small but warm. There is a wooden table in the middle and a blue clock on the wall. It always smells of fresh bread.» (wooden = de madera, in the middle = en el medio, wall = pared, smells of = huele a)"
LIBRARY = "«Attention, please. The school library has a new reading corner. It is open every day after lunch. Silence, please. Thank you.» (reading corner = rincón de lectura, after lunch = después del almuerzo, silence = silencio)"

lesson(
    OA1, 1, MAT,
    "Aprenderé a reconocer el propósito, el público y el contexto de un aviso publicitario, una anécdota y una descripción dichos en voz alta. Sirve para saber qué se espera de ti al escuchar: comprar, aprender algo o imaginar un lugar.",
    ["Sé el presente simple y el pasado simple con verbos comunes.", "Sé usar who, where y when para preguntar."],
    [
        "Todo texto oral tiene un propósito (purpose): la razón por la que alguien habla. Un aviso publicitario (advertisement) busca convencer a un público para que compre o visite algo; por eso usa invitaciones (Come to…, Bring a friend…) y ofertas (free, this week). Una anécdota (anecdote) cuenta un hecho real vivido por quien habla; usa I, my y el pasado simple. Una descripción (description) muestra cómo es una persona o un lugar con adjetivos y la estructura There is…",
        "La audiencia (audience) es el grupo al que se dirige el texto. Se deduce de quién habla, de qué ofrece y del tono. El contexto (context) es la situación: dónde y cuándo se oye. Un aviso con «school café» y «Monday to Friday» se dirige a estudiantes y a su semana de clases. Un aviso de biblioteca que dice Silence, please, quiere que quienes lo oyen cambien su conducta.",
        "Para decidir el propósito, haz dos preguntas mientras escuchas: ¿qué quiere lograr quien habla? y ¿qué pistas lo muestran? Si invita u ofrece algo, convence. Si cuenta lo que vivió y deja una enseñanza, comparte una experiencia. Si muestra cómo es un lugar con adjetivos y There is…, describe. No necesitas entender cada palabra: las pistas bastan.",
    ],
    [("advertisement", "aviso publicitario: busca convencer de comprar o visitar"), ("anecdote", "anécdota: hecho real contado por quien lo vivió"), ("description", "descripción: dice cómo es un lugar o una persona"), ("audience", "audiencia: el grupo al que se habla"), ("purpose", "propósito: lo que el hablante quiere lograr"), ("context", "contexto: dónde, cuándo y en qué situación se oye")],
    [
        ("Propósito de un aviso", ADULT + CAFE + " ¿Para qué se dice este texto?", ["Busco qué quiere lograr quien habla: dice Come to the school café y Bring a friend.", "Ofrece una galleta gratis y un precio: son pistas de publicidad.", "Entonces busca que el público visite y compre."], "Convencer a estudiantes de visitar el café del colegio y comprar un batido"),
        ("Pistas de una anécdota", ADULT + BACKPACK + " ¿Es una anécdota o una descripción? Da una pista.", ["Quien habla usa I y my: cuenta algo propio.", "Usa el pasado: lost, found, called, y una marca de tiempo: two years ago.", "Termina con una enseñanza (a good lesson)."], "Es una anécdota: usa I y el pasado con two years ago y deja una lección"),
    ],
    [
        ("Decidir el propósito solo por el tema (comida = receta).", "Se mira de qué trata y no lo que el hablante quiere lograr.", "Pregunta qué hace el hablante con el tema: invita, cuenta o describe."),
        ("Creer que la audiencia es «todo el mundo».", "No se usan las pistas de lugar, hora o vocabulario.", "Busca la palabra que nombra al público, como school café o shoppers."),
    ],
    [
        (ADULT + CAFE + " ¿Qué frases del guion invitan al público? A) Come to the school café y Bring a friend B) smoothie costs y open from", "A) Come to the school café y Bring a friend", "Come to… y Bring a… son invitaciones; las otras dan datos de precio y horario."),
        (ADULT + CAFE + " ¿Cuánto cuesta cada batido de frutas?", "2.000 pesos", "El guion dice two thousand pesos."),
        (ADULT + KITCHEN + " ¿Qué hace este texto? A) describe un lugar B) da instrucciones", "A) describe un lugar", "Usa There is… y adjetivos como small y warm."),
    ],
    [
        (ADULT + CAFE + " ¿A quién se dirige el aviso? A) a estudiantes del colegio B) a turistas extranjeros", "A) a estudiantes del colegio", "Menciona el school café y el horario de lunes a viernes."),
        (ADULT + BACKPACK + " ¿Qué aprendió quien cuenta la anécdota?", "A escribir su teléfono dentro de sus bolsos", "Dice I always write my phone number inside my bags."),
        ("Une cada fragmento con su formato. 1) «Good evening. Here are today's headlines.» 2) «First, mix the flour and the eggs.» 3) «Last year, I broke my arm playing football.» Formatos: a) anécdota b) noticiero c) procedimiento", "1-b, 2-c, 3-a", "Los titulares son de noticiero, First marca pasos y Last year con I cuenta una vivencia."),
    ],
    [
        (ADULT + KITCHEN + " ¿De qué color es el reloj?", "Azul", "El guion dice a blue clock."),
        (ADULT + CAFE + " ¿Hasta qué hora está abierto el café?", "Hasta las seis", "Dice from eight to six."),
        arith(ADULT + CAFE + " Tres amigos compran un batido cada uno al precio del aviso. ¿Cuántos pesos pagan en total?", "3*2000", "Se multiplican los tres batidos por el precio de cada uno."),
    ],
    [
        (ADULT + CAFE + " Un compañero dice que es una noticia. ¿Qué pista muestra que es publicidad? A) invita a visitar y ofrece una galleta gratis B) informa un hecho reciente del país", "A) invita a visitar y ofrece una galleta gratis", "La invitación y la oferta son marcas de un aviso publicitario."),
        (ADULT + BACKPACK + " ¿Qué pista muestra que la historia es real? A) usa I y my con un hecho personal B) empieza con Once upon a time", "A) usa I y my con un hecho personal", "Once upon a time anuncia un cuento; I y my anuncian vivencia propia."),
    ],
    [
        (ADULT + BACKPACK + " ¿Por qué escribe su teléfono dentro del bolso? A) para que, si lo pierde, puedan llamar a su familia B) para que el conductor del bus sepa su nombre", "A) para que, si lo pierde, puedan llamar a su familia", "Perdió el bolso y un conductor llamó a su madre: ahora se previene."),
        (ADULT + CAFE + " Una amiga dice que la galleta es gratis para quienes llegan solos. ¿Es correcta? A) no, es para quienes van con un amigo B) sí, para todos", "A) no, es para quienes van con un amigo", "El guion dice Bring a friend and you both get a free cookie."),
    ],
    [(ADULT + LIBRARY + " ¿Qué debe hacer quien entra al rincón de lectura?", "Mantener silencio", "El guion dice Silence, please.")],
    [
        ("¿Qué quiere lograr un aviso publicitario?", "Convencer al público de comprar o visitar algo", "Su propósito es persuadir."),
        ("¿Qué palabras del guion de la mochila muestran que quien habla vivió el hecho?", "I y my", "Son pronombres personales de quien cuenta."),
        ("¿Qué es la audiencia de un texto oral?", "El grupo al que se dirige quien habla", "Se deduce de lo que ofrece y de cómo habla."),
    ],
    task("Un adulto lee dos veces este aviso: «Teenagers, fix your bike this Saturday! Our workshop opens at nine. Repairs cost five thousand pesos. Bring your helmet and get a free bottle of water.» (fix = arreglar, workshop = taller, repairs = reparaciones, helmet = casco). En tu hoja escribe: el propósito, la audiencia y dos datos exactos del aviso.", "Propósito: convencer de llevar la bicicleta a reparar. Audiencia: adolescentes. Datos: abre a las nueve; reparar cuesta cinco mil pesos (también: botella de agua gratis con el casco).", ["nombra el propósito de convencer", "indica la audiencia con una pista del guion", "da dos datos exactos y correctos"], ["hoja con tres respuestas", "nota del adulto"], ["decir que es una anécdota", "dar un precio o una hora que no está en el guion"], "Celebra los datos exactos y relee con la persona las palabras Teenagers y Bring para reforzar la audiencia y el propósito."),
    "Pide a un adulto que lea de nuevo el aviso del café y marca en tu hoja la oferta y la invitación.",
    "Escribe en español una anécdota de tres líneas sobre algo que perdiste o encontraste y marca las palabras que irían en pasado en inglés.",
)

# ---------------------------------------------------------------- clase 2: noticiero y descripción con evidencia exacta
NEWS = "«Good evening. This is the eight o'clock news. A new library opened today in the south of the city. It has two floors and room for eighty readers. The mayor said that the library will open from nine to seven. Tomorrow will be sunny, with a high of twenty-six degrees.» (news = noticias, opened = abrió, floors = pisos, room for = capacidad para, mayor = alcalde, sunny = soleado, high = máxima, degrees = grados)"
STREET = "«The street market in my town is open on Sundays. On the left there are fruit and vegetable stands. On the right there are stands with books and old records. At the end of the street there is a small stage where a local band plays at noon.» (street market = feria, stands = puestos, records = discos, stage = escenario, plays = toca, noon = mediodía)"
PHONE = "«Hello, this is the sports center. We have a swimming class on Tuesdays at five thirty and on Thursdays at six. The class lasts forty-five minutes. The teacher is Mrs. Vidal. The price is twelve thousand pesos a month.» (swimming class = clase de natación, lasts = dura, price = precio, a month = al mes)"

lesson(
    OA1, 2, MAT,
    "Aprenderé a ubicar en un noticiero, una descripción y un mensaje telefónico el dato exacto (cifra, lugar, hora, nombre) que responde una pregunta. Sirve para tomar notas fiables al escuchar.",
    ["Sé los números en inglés hasta el millar.", "Sé decir la hora y los días de la semana."],
    [
        "Un noticiero (news broadcast) informa hechos recientes y siempre responde a quién, qué, dónde y cuándo. Una descripción oral presenta un lugar ordenado: izquierda, derecha, fondo. Un mensaje telefónico (phone message) entrega datos prácticos: horarios, precios y nombres. En los tres, la información específica (specific information) es el dato exacto que se pide: una cifra, un lugar, una hora o un nombre.",
        "Para encontrar evidencia precisa, lee o escucha primero la pregunta. Si pide «¿cuántos?», busca un número; si pide «¿dónde?», busca una palabra de lugar como in the south o at the end of; si pide «¿cuándo?», busca un día u hora. Anota solo la palabra clave. Cuidado con los números parecidos: thirteen (13) termina con teen fuerte; thirty (30) lleva la fuerza al principio. Eighty (80) y eighteen (18) también se confunden.",
        "Después de escuchar, contrasta tu nota con otra información del texto. Si dos datos compiten (un horario de martes y otro de jueves), vuelve a la pregunta: ¿cuál pide? Un dato exacto no se cambia por uno aproximado: «alrededor de ochenta» no es lo mismo que «ochenta».",
    ],
    [("news broadcast", "noticiero"), ("specific information", "información específica: dato exacto"), ("floor", "piso de un edificio"), ("stand", "puesto de una feria"), ("lasts", "dura (cuánto tiempo)"), ("high", "temperatura máxima")],
    [
        ("Cifra exacta en un noticiero", ADULT + NEWS + " ¿Cuántos lectores caben en la biblioteca?", ["La pregunta pide una cantidad, busco un número.", "El guion dice room for eighty readers.", "Eighty se escribe 80."], "80 lectores"),
        ("Lugar en una descripción", ADULT + STREET + " ¿Qué se vende a la derecha de la calle?", ["Pide un lugar y qué hay allí: busco On the right.", "Dice stands with books and old records.", "Son puestos con libros y discos antiguos."], "Libros y discos antiguos"),
    ],
    [
        ("Anotar thirteen cuando se dijo thirty.", "Los dos suenan parecidos; cambia la sílaba más fuerte.", "En thirteen se oye fuerte teen al final; en thirty, la primera sílaba."),
        ("Contestar con el dato de otra pregunta.", "Se escucha el texto entero y no la pregunta.", "Lee la pregunta primero y marca la palabra que busca."),
    ],
    [
        (ADULT + NEWS + " ¿Qué tipo de texto es? A) un noticiero B) un mensaje telefónico", "A) un noticiero", "Abre con Good evening y This is the eight o'clock news."),
        (ADULT + STREET + " ¿Qué se vende a la izquierda de la calle?", "Frutas y verduras", "El guion dice On the left there are fruit and vegetable stands."),
        (ADULT + PHONE + " ¿Qué día es la clase de las seis?", "Los jueves", "Dice on Thursdays at six."),
    ],
    [
        (ADULT + NEWS + " ¿Cuántos pisos tiene la biblioteca?", "2", "El guion dice two floors."),
        (ADULT + PHONE + " ¿Cuánto dura cada clase de natación?", "45 minutos", "Dice lasts forty-five minutes."),
        (ADULT + STREET + " ¿Cuándo está abierta la feria? A) los domingos B) los sábados", "A) los domingos", "El guion dice open on Sundays."),
    ],
    [
        (ADULT + NEWS + " ¿Qué temperatura máxima anunciaron para mañana? A) 26 grados B) 16 grados", "A) 26 grados", "Dice a high of twenty-six degrees; sixteen suena parecido pero no se dijo."),
        (ADULT + PHONE + " ¿A qué hora es la clase de los martes?", "A las cinco y media", "El guion dice on Tuesdays at five thirty."),
        arith(ADULT + PHONE + " Una persona paga el precio del mensaje durante tres meses. ¿Cuántos pesos paga en total?", "12000*3", "Se multiplica el precio mensual por tres meses."),
    ],
    [
        (ADULT + STREET + " ¿Dónde toca la banda local? A) en un escenario al final de la calle B) en el puesto de libros", "A) en un escenario al final de la calle", "Dice At the end of the street there is a small stage."),
        (ADULT + NEWS + " ¿Quién anunció el horario de la biblioteca? A) el alcalde B) la directora del colegio", "A) el alcalde", "El guion dice The mayor said."),
    ],
    [
        (ADULT + PHONE + " ¿Cómo se llama la profesora?", "Sra. Vidal", "Dice The teacher is Mrs. Vidal."),
        (ADULT + NEWS + " Un oyente anotó que la biblioteca abre de nueve a cinco. ¿Qué horario dijo en realidad el guion? A) de nueve a siete B) de nueve a cinco", "A) de nueve a siete", "El guion dice from nine to seven; la nota cambió la hora de cierre."),
    ],
    [(ADULT + "«Hi, Marta. It's Tomás. The bus to the lake leaves at seven fifteen from the main square. Bring sunscreen and a hat. The ticket costs eight thousand pesos.» (lake = lago, leaves = sale, sunscreen = bloqueador, ticket = pasaje). ¿Desde dónde sale el bus?", "Desde la plaza principal", "El guion dice from the main square.")],
    [
        ("¿Qué tipo de dato busca la pregunta «¿cuántos?»?", "Un número", "Pide una cantidad exacta."),
        ("¿Qué sílaba lleva la fuerza al final en thirteen?", "teen", "Esa sílaba fuerte la distingue de thirty."),
        ("¿Qué debes hacer primero antes de escuchar un noticiero para responder preguntas?", "Leer las preguntas", "Así sabes qué dato buscar."),
    ],
    task("Un adulto lee dos veces este mensaje: «Hello, Camila. This is Dr. Ibáñez's office. Your dental check-up is on Wednesday at four forty. Please arrive ten minutes early. Bring your school ID. The office is on the third floor.» (dental check-up = control dental, arrive = llegar, early = antes, school ID = credencial escolar, floor = piso). En tu hoja escribe cinco datos exactos del mensaje.", "Control con el Dr. Ibáñez; miércoles; a las cuatro y cuarenta; llegar diez minutos antes con la credencial escolar; consulta en el tercer piso.", ["anota cinco datos distintos", "cada cifra y día coincide con el guion", "no mezcla datos que no se dijeron"], ["hoja con cinco datos", "nota del adulto"], ["confundir four forty con fourteen", "olvidar el piso o el día"], "Reconoce los datos acertados y repasa con la persona cada número dudoso en una segunda lectura."),
    "Pide a un adulto que lea otra vez el noticiero y subraya cada cifra que oigas.",
    "Escribe en español tres datos exactos de tu barrio (horarios o lugares) que podrías dar por teléfono.",
)

# ---------------------------------------------------------------- clase 3: instrucciones y procedimientos
RECIPE = "«Today I will show you how to make a simple fruit salad. First, wash two apples and one banana. Then cut them into small pieces. Next, put the pieces in a bowl and add the juice of one orange. After that, mix everything with a spoon. Finally, wait ten minutes and serve it cold.» (wash = lavar, cut = cortar, pieces = trozos, bowl = bol, add = agregar, juice = jugo, mix = mezclar, spoon = cuchara, serve = servir)"
PHOTO = "«To send a photo from your phone, follow these steps. First, open the photo you want to send. Second, press the share icon. Third, choose the contact. Fourth, check the name again. Last, press send.» (send = enviar, share icon = ícono de compartir, choose = elegir, contact = contacto, check = revisar)"
GAME = "«To play the memory game, you need twelve cards. Put them face down on the table. The first player turns two cards. If the cards match, the player keeps them and plays again. If not, the next player has a turn. The winner has the most pairs.» (face down = boca abajo, turns = da vuelta, match = coinciden, keeps = se queda con, turn = turno, pairs = pares)"

lesson(
    OA1, 3, MAT,
    "Aprenderé una estrategia para entender instrucciones y procedimientos orales: reconocer las palabras de orden (first, then, next, finally) y el verbo de cada paso. Sirve para seguir una receta o un tutorial dichos en inglés.",
    ["Sé que el imperativo usa el verbo sin sujeto (cut, mix).", "Sé contar hasta veinte."],
    [
        "Un procedimiento (procedure) explica cómo hacer algo paso a paso. Se reconoce porque usa verbos de acción al principio de la frase (wash, cut, press) y palabras de orden: first, second, then, next, after that, finally, last. Esas palabras son tus señales: cada una avisa que empieza un paso nuevo. Las instrucciones de un juego (game rules) usan además if… (si…) para explicar qué pasa en cada caso.",
        "La estrategia es escuchar por pasos. Cada vez que oigas una palabra de orden, escribe un número y anota solo el verbo y el objeto: «1 lavar manzanas», «2 cortar». No traduzcas todo. Al terminar, revisa que los números sigan el orden del guion y que no falte ningún paso. Los datos exactos (twelve cards, ten minutes) también se anotan porque cambian el resultado.",
        "Si los pasos se dan desordenados, la palabra de orden manda: finally va al final aunque lo digan antes en otra frase. Verifica con una segunda lectura. Una instrucción es útil solo si alguien puede repetirla en el mismo orden.",
    ],
    [("procedure", "procedimiento: pasos para hacer algo"), ("first / next / finally", "primero / luego / finalmente"), ("step", "paso"), ("match", "coincidir, formar pareja"), ("mix", "mezclar"), ("serve", "servir")],
    [
        ("Ordenar pasos", ADULT + RECIPE + " ¿Qué se hace justo después de cortar la fruta?", ["Busco la palabra de orden de cortar: Then cut them.", "La palabra siguiente es Next, put the pieces in a bowl.", "Entonces el paso que sigue es ponerla en un bol."], "Poner los trozos en un bol y agregar jugo de naranja"),
        ("Dato exacto en un procedimiento", ADULT + GAME + " ¿Cuántas cartas se necesitan?", ["La pregunta pide una cantidad.", "El guion dice you need twelve cards.", "Twelve se escribe 12."], "12 cartas"),
    ],
    [
        ("Escribir los pasos en el orden en que se recuerdan.", "Se ignoran las palabras de orden.", "Numera cada paso al oír first, then, next, finally."),
        ("Anotar solo la palabra de orden y olvidar el verbo.", "Se oye la señal pero no la acción.", "Junto a cada número escribe el verbo y su objeto."),
    ],
    [
        (ADULT + RECIPE + " ¿Cuál es el último paso? A) esperar diez minutos y servir frío B) lavar las manzanas", "A) esperar diez minutos y servir frío", "La palabra Finally marca el último paso."),
        (ADULT + PHOTO + " ¿Qué se hace primero? A) abrir la foto B) enviar", "A) abrir la foto", "El guion dice First, open the photo."),
        (ADULT + GAME + " ¿Dónde se ponen las cartas al empezar? A) boca abajo en la mesa B) boca arriba en la silla", "A) boca abajo en la mesa", "Dice face down on the table."),
    ],
    [
        (ADULT + RECIPE + " Ordena los pasos con letras. A) mix everything B) cut the fruit C) wash the fruit D) serve it cold", "C, B, A, D", "Primero se lava, luego se corta, después se mezcla y al final se sirve."),
        (ADULT + PHOTO + " ¿Qué se revisa antes de enviar? A) el nombre del contacto B) el tamaño de la pantalla", "A) el nombre del contacto", "El cuarto paso dice check the name again."),
        (ADULT + GAME + " ¿Quién gana el juego?", "Quien tiene más pares", "El guion dice The winner has the most pairs."),
    ],
    [
        (ADULT + RECIPE + " ¿Con qué se mezcla todo? A) con una cuchara B) con un tenedor", "A) con una cuchara", "El guion dice mix everything with a spoon."),
        (ADULT + PHOTO + " ¿Qué palabra de orden marca el último paso?", "Last", "El quinto paso empieza con Last, press send."),
        (ADULT + GAME + " ¿Qué hace la jugadora si las dos cartas coinciden? A) se las queda y juega otra vez B) las devuelve y pasa el turno", "A) se las queda y juega otra vez", "El guion dice the player keeps them and plays again."),
    ],
    [
        (ADULT + GAME + " Una jugadora da vuelta dos cartas y no coinciden. ¿Qué pasa? A) juega la siguiente persona B) se queda con las cartas", "A) juega la siguiente persona", "El guion dice If not, the next player has a turn."),
        (ADULT + RECIPE + " Si una persona termina de mezclar la ensalada a las 4:00 de la tarde y sigue el último paso al pie de la letra, ¿a qué hora la sirve?", "A las 4:10 de la tarde", "Finally pide esperar diez minutos y recién entonces servir."),
    ],
    [
        (ADULT + PHOTO + " ¿Cuántos pasos numerados tiene? Cuenta First, Second, Third, Fourth y Last.", "5", "Son cinco palabras de orden, o sea cinco pasos."),
        (ADULT + RECIPE + " Un compañero dice que se mezcla antes de cortar. ¿Qué parte del guion lo corrige? A) After that, mix everything, que viene después de cortar B) Finally, serve it cold", "A) After that, mix everything, que viene después de cortar", "Cortar es el paso Then y mezclar es After that."),
    ],
    [(ADULT + "«To change the password of your school email, follow these steps. First, open the settings. Second, choose Security. Third, type a new password with eight characters. Last, save the change.» (password = contraseña, settings = configuración, type = escribir, characters = caracteres, save = guardar). ¿Cuántos caracteres debe tener la contraseña nueva?", "8", "El guion dice eight characters.")],
    [
        ("¿Qué señalan las palabras first, then, next y finally?", "El orden de los pasos", "Avisan cuándo empieza cada paso."),
        ("¿Qué verbo usa el primer paso de la receta de ensalada de frutas?", "Wash", "El guion dice First, wash two apples."),
        ("¿Para qué sirve escuchar una segunda vez un procedimiento?", "Para revisar que los pasos estén completos y en orden", "Una instrucción solo funciona si se repite en orden."),
    ],
    task("Un adulto lee dos veces estas instrucciones: «To make a paper boat, take one sheet of paper. First, fold it in half. Second, fold the top corners to the center. Third, fold the bottom edges up. Last, open the boat and press the bottom.» (sheet = hoja, fold = doblar, in half = por la mitad, corners = esquinas, center = centro, edges = bordes, press = presionar). En tu hoja anota los cuatro pasos numerados con su verbo.", "1 doblar por la mitad; 2 doblar las esquinas de arriba al centro; 3 doblar los bordes de abajo hacia arriba; 4 abrir el barco y presionar el fondo.", ["cuatro pasos numerados", "cada paso tiene su verbo", "respeta el orden del guion"], ["hoja con cuatro pasos", "nota del adulto"], ["cambiar el orden de los pasos", "olvidar un verbo"], "Reconoce el orden logrado y repasa con la persona las palabras de orden del guion."),
    "Pide a un adulto que lea otra vez las reglas del juego y escribe en español las tres reglas más importantes.",
    "Escribe en español cuatro pasos para algo que sabes hacer (por ejemplo, preparar un té) y subraya las palabras de orden que usarías en inglés.",
)

# ---------------------------------------------------------------- clase 4: entrevistas y conversaciones con vacío de información
INTV = "«Reporter: Tell me about your garden, Ms. Parra. Ms. Parra: It is on the roof of the community center. Reporter: What do you grow? Ms. Parra: Tomatoes, lettuce and herbs. Reporter: Who helps you? Ms. Parra: Twelve neighbors. We meet every Saturday at ten.» (roof = techo, community center = centro comunitario, grow = cultivar, herbs = hierbas, neighbors = vecinos, meet = nos reunimos)"
PLAN = "«Joaquín: Where do you want to go on Friday? Elena: Let's go to the beach. Joaquín: Hmm, I prefer the mountains. Elena: But it is going to rain in the mountains. Joaquín: Really? Then the beach is a better idea. Elena: Great. The bus leaves at eight.» (prefer = prefiero, going to rain = va a llover, Really? = ¿En serio?, better = mejor, leaves = sale)"

lesson(
    OA1, 4, "Los diálogos escritos en cada ejercicio; un adulto los lee en voz alta, cada persona sabe solo una parte de la información; lápiz y hoja.",
    "Aprenderé a completar un dato que me falta preguntando a otra persona (vacío de información). Sirve para entender una conversación o una entrevista cuando cada hablante sabe solo una parte.",
    ["Sé formar preguntas con What, Where, When, Who y How long.", "Sé responder con Yes, I do / No, I don't."],
    [
        "Un vacío de información (information gap) ocurre cuando una persona sabe algo que la otra no sabe. En una entrevista, el entrevistador tiene las preguntas y la persona entrevistada tiene las respuestas. En una conversación, cada hablante aporta un dato y el otro lo completa. Para entenderlas hay que unir las dos partes: lo que dice uno más lo que dice el otro forman el significado completo.",
        "Para llenar el vacío sirven tres movimientos: preguntar (Where do you want to go?), confirmar (Really?, You mean…?) y reformular (So, we go to the beach). La palabra interrogativa te indica qué dato falta: Where pide un lugar, When una hora o un día, Who una persona, What una cosa y How long una duración. Las respuestas completas incluyen el dato exacto (Twelve neighbors, at ten).",
        "Cuando oigas un diálogo, identifica quién tiene qué dato. Marca con las iniciales quién habla y anota cada dato junto a su dueño. Los cambios de opinión son importantes: Joaquín prefería la montaña, pero cambió de opinión al saber de la lluvia. La decisión final es lo último que acuerdan, no lo primero que se propone.",
    ],
    [("information gap", "vacío de información: una persona sabe algo que la otra no"), ("interview", "entrevista"), ("prefer", "preferir"), ("Really?", "¿En serio? Sirve para confirmar"), ("You mean…?", "¿Quieres decir…?"), ("agree", "estar de acuerdo")],
    [
        ("Llenar un vacío en una entrevista", ADULT + INTV + " El reportero no sabe cuántas personas ayudan. ¿Qué dato le da la Sra. Parra?", ["La pregunta que falta es Who helps you?", "La respuesta de Ms. Parra es Twelve neighbors.", "Twelve es 12."], "12 vecinos"),
        ("Decisión final de un diálogo", ADULT + PLAN + " ¿Adónde van finalmente?", ["Elena propone la playa y Joaquín prefiere la montaña.", "Elena dice que va a llover en la montaña.", "Joaquín cambia de opinión y dicen Great."], "A la playa"),
    ],
    [
        ("Quedarse con la primera propuesta del diálogo.", "No se espera la respuesta del otro hablante.", "Escucha hasta el último turno: ahí está el acuerdo."),
        ("Mezclar el dato de un hablante con el del otro.", "No se anota quién habla.", "Marca iniciales y escribe cada dato junto a su hablante."),
    ],
    [
        (ADULT + INTV + " ¿Dónde está la huerta? A) en el techo del centro comunitario B) en el patio de un colegio", "A) en el techo del centro comunitario", "Dice on the roof of the community center."),
        (ADULT + INTV + " ¿Cuándo se reúnen los vecinos?", "Los sábados a las diez", "El guion dice every Saturday at ten."),
        (ADULT + PLAN + " ¿A qué hora sale el bus?", "A las ocho", "Elena dice The bus leaves at eight."),
    ],
    [
        (ADULT + INTV + " ¿Qué cultivan? A) tomates, lechuga y hierbas B) maíz y papas", "A) tomates, lechuga y hierbas", "Ms. Parra responde Tomatoes, lettuce and herbs."),
        (ADULT + PLAN + " ¿Por qué Joaquín cambia de opinión? A) porque va a llover en la montaña B) porque no hay bus", "A) porque va a llover en la montaña", "Elena avisa it is going to rain in the mountains."),
        ("Une cada pregunta con el dato que falta. 1) Who helps you? 2) What do you grow? 3) When do you meet? Datos: a) Tomatoes, lettuce and herbs b) Twelve neighbors c) Every Saturday", "1-b, 2-a, 3-c", "Who pide personas, What pide cosas y When pide un momento."),
    ],
    [
        (ADULT + PLAN + " ¿Qué día quieren salir?", "El viernes", "Joaquín pregunta Where do you want to go on Friday?"),
        arith(ADULT + INTV + " Supón que cada vecino que ayuda lleva tres lechugas a la feria (dato de ejemplo). ¿Cuántas lechugas llevan en total?", "12*3", "Se multiplican los doce vecinos del guion por tres lechugas cada uno."),
        (ADULT + "«Teacher: Please open your books at page twenty. Student: Sorry, twelve? Teacher: No, twenty. Two-zero.» (page = página, books = libros). ¿En qué página deben abrir?", "En la 20", "La profesora corrige twelve y repite twenty, dos-cero."),
    ],
    [
        (ADULT + "«Lucas: Where is the concert? Paula: In the gym. Lucas: And when does it start? Paula: At six.» ¿Qué dato aporta Paula primero? A) el lugar: en el gimnasio B) la hora: a las seis", "A) el lugar: en el gimnasio", "Paula responde primero a Where con In the gym."),
        (ADULT + PLAN + " ¿Qué palabra usa Joaquín para confirmar el aviso de lluvia? A) Really? B) Great", "A) Really?", "Pregunta Really? para confirmar lo que oyó."),
    ],
    [
        (ADULT + INTV + " Un oyente anotó que se reúnen los domingos. ¿Qué día dijo en realidad el guion?", "Los sábados", "El guion dice Saturday, no Sunday."),
        (ADULT + PLAN + " ¿Qué dos lugares se comparan en el diálogo y cuál gana? A) playa y montaña; gana la playa B) playa y piscina; gana la piscina", "A) playa y montaña; gana la playa", "Elena propone beach, Joaquín mountains y al final aceptan the beach."),
    ],
    [(ADULT + "«Customer: How much is a ticket? Clerk: Four thousand pesos for students, six thousand for adults. Customer: I'm a student. Clerk: Then it's four thousand.» (ticket = entrada, clerk = boletero, students = estudiantes, adults = adultos). ¿Cuánto paga el cliente?", "4.000 pesos", "El boletero dice que los estudiantes pagan four thousand y el cliente es estudiante.")],
    [
        ("¿Qué es un vacío de información?", "Cuando una persona sabe algo que la otra no sabe", "Las dos partes se completan al conversar."),
        ("¿Qué palabra interrogativa pide un lugar?", "Where", "Where significa dónde."),
        ("¿Qué palabra sirve para confirmar si entendiste, como «¿en serio?»?", "Really?", "Se usa para verificar lo que se oyó."),
    ],
    task("Un adulto lee dos veces este diálogo: «Sofía: Do you want to study together tomorrow? Daniel: Yes, but I can't in the morning. I have football practice. Sofía: What about the afternoon? Daniel: Good. Can we meet at the library at three? Sofía: Perfect. I'll bring the notes.» (study together = estudiar juntos, practice = entrenamiento, What about…? = ¿Qué tal…?, notes = apuntes). En tu hoja anota: qué proponen, qué dato aporta cada uno (Sofía y Daniel) y en qué acuerdan al final.", "Proponen estudiar juntos mañana. Daniel aporta que en la mañana tiene entrenamiento; Sofía propone la tarde y llevará los apuntes. Acuerdan reunirse en la biblioteca a las tres.", ["identifica la propuesta", "separa lo que aporta cada hablante", "anota el acuerdo final con hora y lugar"], ["hoja con tres respuestas", "nota del adulto"], ["decir que se reúnen en la mañana", "atribuir un dato a la persona equivocada"], "Valida lo que acertó y relee con la persona los turnos de Daniel para separar sus datos."),
    "Pide a un adulto que lea de nuevo el diálogo de Joaquín y Elena y marca cada turno con J o E.",
    "Escribe en español un diálogo de cuatro turnos en que cada persona sabe un dato distinto sobre una salida al cine.",
)

# ---------------------------------------------------------------- clase 5: canción original y respuesta independiente
SONG = "«Verse: Morning light on the window, / The bus is coming down the street. / Hurry up, my friends are waiting, / We are walking to the beat. / Chorus: Together, together, / We walk through the rain. / Together, together, / We sing it again.» (morning light = luz de la mañana, window = ventana, hurry up = apúrate, beat = ritmo, rain = lluvia, sing = cantar)"
ANEC2 = "«Last April, our school team lost the basketball final. We cried a little in the locker room. Then our coach said, We lost the game, but we learned a lot. This year we practiced harder, and we won the cup.» (lost = perdimos, final = final, locker room = camarín, coach = entrenador, practiced harder = practicamos más duro, won = ganamos, cup = copa)"
WEATHER = "«Good morning. Here is the weather. In the north, it will be hot and dry, with thirty-one degrees. In the center, cloudy with some rain in the evening. In the south, it will be cold and windy. Remember to take an umbrella if you are in the center.» (weather = el tiempo, hot = caluroso, dry = seco, cloudy = nublado, windy = ventoso, umbrella = paraguas)"

lesson(
    OA1, 5, MAT,
    "Aprenderé a responder por mi cuenta preguntas sobre una canción, una anécdota y un pronóstico del tiempo, eligiendo el dato o la idea correcta. Sirve para comprobar que ya puedo entender distintos formatos orales sin ayuda.",
    ["Sé reconocer propósito y audiencia.", "Sé buscar datos exactos y seguir pasos."],
    [
        "Una canción (song) combina palabras con ritmo y repetición. Tiene versos (verses) que cuentan o describen y un estribillo (chorus) que se repite. El estribillo suele contener la idea principal: aquí, ir juntos bajo la lluvia. En una canción, las palabras que riman (street / beat) ayudan a recordar, pero el sentido está en las acciones y los sentimientos que nombra.",
        "Un pronóstico del tiempo (weather forecast) es un texto informativo con datos por zonas (north, center, south), temperaturas y recomendaciones. Una anécdota deportiva puede mostrar un cambio: una derrota que termina en aprendizaje. En todos los formatos, usa tu orden de trabajo: leer la pregunta, escuchar buscando esa palabra, anotar el dato, y comprobar con la segunda lectura.",
        "Trabajar de forma independiente significa no depender de que te digan qué hacer. Antes de responder, pregúntate: ¿cuál es el formato?, ¿qué quiere lograr quien habla? y ¿qué pista del guion respalda mi respuesta? Siempre justifica con una palabra o frase del texto.",
    ],
    [("song", "canción"), ("chorus", "estribillo: parte que se repite"), ("verse", "verso, estrofa"), ("weather forecast", "pronóstico del tiempo"), ("rhyme", "rima: sonidos finales parecidos"), ("independent", "independiente: sin ayuda")],
    [
        ("Idea del estribillo", ADULT + SONG + " ¿Qué idea repite el estribillo?", ["Busco la parte que se repite: Together, together.", "Dice We walk through the rain y We sing it again.", "Entonces la idea es ir juntos y cantar a pesar de la lluvia."], "Caminar y cantar juntos aunque llueva"),
        ("Cambio en una anécdota", ADULT + ANEC2 + " ¿Qué pasó después de la derrota?", ["Busco el cambio: Then our coach said…", "El entrenador dijo que aprendieron mucho.", "El año siguiente practicaron más y ganaron la copa."], "Aprendieron, practicaron más y ganaron la copa"),
    ],
    [
        ("Pensar que una canción solo sirve para entretener.", "Se ignora lo que cuenta o expresa.", "Busca qué acción o sentimiento aparece en los versos y en el estribillo."),
        ("Responder sin una pista del guion.", "Se contesta por intuición.", "Cita la palabra o frase que respalda tu respuesta."),
    ],
    [
        (ADULT + SONG + " ¿Qué pasa por la ventana? A) entra luz de la mañana B) llueve fuerte", "A) entra luz de la mañana", "El primer verso dice Morning light on the window."),
        (ADULT + WEATHER + " ¿Cómo estará el sur? A) frío y ventoso B) caluroso y seco", "A) frío y ventoso", "El guion dice In the south, it will be cold and windy."),
        (ADULT + ANEC2 + " ¿En qué deporte perdieron la final?", "Básquetbol", "Dice lost the basketball final."),
    ],
    [
        (ADULT + WEATHER + " ¿Cuántos grados habrá en el norte?", "31", "El guion dice thirty-one degrees."),
        (ADULT + WEATHER + " ¿Quién debe llevar paraguas? A) quien esté en el centro B) quien esté en el norte", "A) quien esté en el centro", "El guion recomienda take an umbrella if you are in the center."),
        (ADULT + SONG + " ¿Qué dos palabras riman al final de los versos 2 y 4? A) street y beat B) window y friends", "A) street y beat", "Street y beat terminan con sonidos parecidos en los versos 2 y 4."),
    ],
    [
        (ADULT + WEATHER + " ¿Cómo estará el centro? A) nublado con algo de lluvia B) soleado y seco", "A) nublado con algo de lluvia", "El guion dice In the center, cloudy with some rain."),
        (ADULT + ANEC2 + " ¿Dónde lloraron un poco? A) en el camarín B) en la cancha", "A) en el camarín", "Dice We cried a little in the locker room."),
        (ADULT + SONG + " ¿Quiénes esperan a quien canta? A) sus amigos B) sus profesores", "A) sus amigos", "El tercer verso dice my friends are waiting."),
    ],
    [
        (ADULT + ANEC2 + " ¿Cuándo perdió el equipo la final? A) el abril pasado B) el marzo pasado", "A) el abril pasado", "El guion dice Last April, our school team lost the basketball final."),
        (ADULT + SONG + " ¿Qué sentimiento transmite el estribillo? A) compañía y alegría B) miedo y soledad", "A) compañía y alegría", "Together y sing it again muestran unión."),
    ],
    [
        (ADULT + WEATHER + " ¿Qué zona tendrá lluvia en la tarde-noche? A) el centro B) el sur", "A) el centro", "El guion dice cloudy with some rain in the evening en el centro."),
        (ADULT + ANEC2 + " Un compañero dice que la historia termina mal. ¿Cuál dato lo contradice? A) we won the cup B) we lost the game", "A) we won the cup", "El final de la anécdota es ganar la copa."),
    ],
    [(ADULT + "«Excuse me, passengers. The train to the capital leaves from platform three at six forty. Please do not leave your bags alone.» (passengers = pasajeros, train = tren, platform = andén, leave your bags alone = dejar los bolsos solos). ¿Desde qué andén sale el tren?", "Andén 3", "El guion dice from platform three.")],
    [
        ("¿Cómo se llama la parte de una canción que se repite?", "Estribillo (chorus)", "Se repite y resume la idea central."),
        ("¿Qué datos entrega un pronóstico del tiempo?", "El clima y la temperatura por zonas", "Es un texto informativo por regiones."),
        ("¿Qué debes hacer antes de dar una respuesta de comprensión oral?", "Buscar una pista en el guion", "La evidencia respalda lo que respondes."),
    ],
    task("Un adulto lee dos veces esta canción original: «Little bird on the roof, / Sing me a song at noon. / The sun is climbing up, / I will see you soon. / Chorus: Fly, fly, fly away, / Come back at the end of the day.» (bird = pájaro, roof = techo, climbing = subiendo, fly = volar, come back = vuelve). En tu hoja escribe: a quién le habla la canción, a qué hora, qué le pide al final y qué sentimiento tiene.", "Le habla a un pájaro pequeño; al mediodía; le pide que vuele pero vuelva al final del día; siente cariño y espera verlo pronto.", ["identifica al destinatario y la hora", "explica el pedido del estribillo", "nombra un sentimiento con una pista"], ["hoja con cuatro respuestas", "nota del adulto"], ["decir que habla a una persona", "ignorar el estribillo"], "Reconoce el acierto y relee con la persona el estribillo para precisar qué se pide al pájaro."),
    "Pide a un adulto que lea otra vez el pronóstico del tiempo y dibuja un mapa simple con el clima de cada zona.",
    "Escribe en español cuatro versos propios con una rima sobre un día de lluvia y marca las palabras que riman.",
)
