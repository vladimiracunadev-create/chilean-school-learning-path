"""Cuaderno del estudiante, 6.º básico Inglés (propuesta): EN06 OA 11 (vocabulario y expresiones) y OA 12 (diálogos orales).

Los textos en inglés son originales, breves y llevan pista en español. Cada palabra o estructura se enseña en la propia clase
antes de usarla. Sin audio externo: todo lo que hay que leer o decir está escrito en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA11 = "EN06 OA 11"
OA12 = "EN06 OA 12"


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


# ================================================================ OA 11 clase 1: propósito y contexto
lesson(
    OA11, 1,
    "Las listas de palabras y situaciones escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a elegir la palabra o la expresión que sirve para cada situación. Sirve para hablar y escribir en inglés con las palabras justas.",
    ["Conozco palabras básicas en inglés como cat, book y school.", "Sé saludar y despedirme en inglés."],
    [
        "El vocabulario temático son las palabras que pertenecen a un mismo tema. Por ejemplo, el tema deportes y pasatiempos incluye swimming (nadar), skating (patinar), chess (ajedrez) y cycling (andar en bicicleta). El tema lugares incluye library (biblioteca), bakery (panadería) y hospital (hospital).",
        "Las expresiones de uso común son frases hechas que se usan siempre igual: That's cool! (¡Qué genial!), Great! (¡Genial!), Well done! (¡Bien hecho!), Good idea! (¡Buena idea!), Thanks a lot! (¡Muchas gracias!), No problem. (No hay problema), Sorry! (¡Perdón!) y Excuse me. (Disculpa, con permiso).",
        "Para elegir bien piensa en el propósito (para qué hablas) y en el contexto (con quién y dónde estás). Si alguien logra algo, felicitas con Well done! Si pasas entre dos personas, dices Excuse me. Si alguien te ayuda, dices Thanks a lot!",
    ],
    [("vocabulary", "vocabulario: las palabras de un tema"), ("purpose", "propósito: para qué hablas"), ("context", "contexto: dónde y con quién estás"), ("That's cool!", "¡Qué genial!"), ("Well done!", "¡Bien hecho!"), ("Excuse me.", "Disculpa, con permiso"), ("Sorry!", "¡Perdón!")],
    [
        ("Elegir la expresión", "Un amigo te muestra su bicicleta nueva. ¿Qué dices? Opciones: That's cool! / Sorry! / Excuse me.", ["Mira la situación: tu amigo te muestra algo que le gusta.", "Quieres mostrar que te parece genial.", "La expresión para eso es That's cool!"], "That's cool!"),
        ("Encontrar la palabra que no es del tema", "Tema deportes. Palabras: swimming, skating, tennis, bakery. ¿Cuál no pertenece?", ["Swimming, skating y tennis son deportes.", "Bakery es un lugar donde se vende pan.", "No es un deporte."], "bakery"),
    ],
    [
        ("Usar Sorry! para felicitar.", "Sorry sirve para pedir perdón, no para celebrar.", "Mira el propósito: si celebras, usa Great! o Well done!"),
        ("Mezclar palabras de otro tema en una lista.", "No se mira a qué tema pertenece cada palabra.", "Pregunta: ¿esta palabra va con las demás del tema?"),
    ],
    [
        ("¿Qué significa «Well done!»?", "¡Bien hecho!", "Se dice para felicitar un logro."),
        ("Palabras: cat, dog, rabbit, library. ¿Cuál no es un animal?", "library", "Library es un lugar, no un animal."),
        ("Completa: «Thanks a lot! — No ___.» Opciones: problem, cool.", "problem", "No problem es la respuesta común a un agradecimiento."),
    ],
    [
        ("Tu compañera te presta un lápiz. ¿Qué dices tú? a) Thanks a lot! b) No problem.", "a", "Quien recibe la ayuda agradece; No problem lo dice quien ayudó."),
        ("Palabras: swimming, skating, chess, cycling. ¿Qué tema las reúne? a) sports and hobbies b) food c) weather", "a", "Son deportes y pasatiempos."),
        ("¿Para qué sirve «Excuse me.»? a) Pedir paso o atención con cortesía b) Felicitar a alguien", "a", "Excuse me abre una petición educada."),
    ],
    [
        ("Un amigo ganó una carrera. Completa: «You won? ___!» Opciones: Great, Sorry.", "Great", "Great expresa alegría por su logro."),
        ("Completa: «You buy bread at the ___.» Opciones: bakery, library.", "bakery", "El pan se compra en una panadería."),
        ("Chocas sin querer con alguien en el pasillo. ¿Qué dices? Opciones: Sorry!, Great!", "Sorry!", "Pides perdón por el choque."),
    ],
    [
        ("Alguien dice: «I have a new puppy!» ¿Qué respuesta encaja? a) That's cool! b) Excuse me.", "a", "That's cool! muestra interés y alegría; Excuse me pide paso."),
        ("Una compañera se cayó en el recreo. ¿Encaja decirle «Well done!»? Responde sí o no.", "No", "Well done felicita un logro y una caída no lo es."),
    ],
    [
        ("Lista: skating (deporte), library (lugar), chess (pasatiempo), bakery (lugar), swimming (deporte). ¿Cuántas de estas palabras son del tema lugares?", "2", "Library y bakery son los lugares."),
        ("Mini diálogo: A: «I made a cake!» B: «___» Opciones: a) Well done! b) Excuse me. c) Sorry!", "a", "Hacer un pastel es un logro que se felicita."),
    ],
    [("Estás en la biblioteca (library) y quieres pasar entre dos personas sentadas. ¿Qué dices? a) Excuse me. b) That's cool!", "a", "Excuse me pide paso con cortesía.")],
    [
        ("¿Qué es el vocabulario temático?", "Las palabras de un mismo tema", "Agrupa palabras que van juntas, como deportes."),
        ("¿Qué significa «Good idea!»?", "¡Buena idea!", "Se usa para aprobar una propuesta."),
        ("¿Qué dos cosas miras para elegir una expresión?", "El propósito y el contexto", "Primero para qué hablas y luego dónde y con quién."),
    ],
    task("Lee estas tres situaciones: 1) Una compañera te muestra su dibujo nuevo. 2) Una persona te ayuda a llevar tu mochila. 3) Quieres pasar entre dos personas. Escribe en tu hoja la expresión en inglés que usarías en cada una, eligiendo entre: That's cool!, Thanks a lot!, Excuse me., Sorry!, Well done! Después escribe con tus palabras por qué elegiste cada una.", "1) That's cool! porque quiero mostrar que me gusta. 2) Thanks a lot! porque me ayudaron. 3) Excuse me. porque pido paso con cortesía.", ["las tres expresiones calzan con la situación", "explica el propósito de cada una", "escribe las expresiones en inglés sin cambiarlas"], ["hoja con tres expresiones y razones"], ["usar Sorry! para felicitar", "no explicar la elección"], "Pregunta qué cambiaría si la situación 1 fuera que su dibujo se rompió."),
    "Escribe en una hoja las seis expresiones de la explicación con su significado en español.",
    "Escribe una lista de cinco palabras del tema lugares de tu barrio, con su significado.",
)

# ================================================================ OA 11 clase 2: palabras clave y pistas
lesson(
    OA11, 2,
    "Los textos breves y listas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a usar palabras clave y pistas del texto para entender y completar vocabulario. Sirve para descubrir una palabra aunque no la recuerde.",
    ["Conozco expresiones como Great! y Thanks a lot!", "Sé qué es un tema de vocabulario."],
    [
        "Una palabra clave (key word) es la palabra que lleva el sentido de una oración. Las otras palabras de la oración dan pistas (clues) para saber de qué se habla. En «Mia has a racket and a ball. She plays ___», las palabras racket y ball son pistas: la palabra que falta es tennis.",
        "También hay palabras de uso frecuente, que aparecen casi en todo texto: and (y), but (pero), because (porque), very (muy), with (con), today (hoy), now (ahora), so (así que). Aunque son pequeñas, ordenan las ideas: because explica una razón, but muestra una diferencia y so muestra un resultado.",
        "Para completar una oración sigue estos pasos: 1) lee toda la oración, 2) busca las palabras clave, 3) elige la palabra que calza con las pistas, 4) vuelve a leer para comprobar que tiene sentido. Si dudas entre dos, prueba cuál encaja mejor con el tema.",
    ],
    [("key word", "palabra clave"), ("clue", "pista"), ("because", "porque"), ("but", "pero"), ("and", "y"), ("very", "muy"), ("with", "con"), ("so", "así que")],
    [
        ("Completar con pistas", "«Leo wears goggles and a swimming cap. He is in the pool. He is ___.» Opciones: swimming, cooking. (goggles = antiparras; pool = piscina)", ["Las pistas son goggles, swimming cap y pool.", "Todas hablan de nadar.", "Calza swimming."], "swimming"),
        ("Elegir la palabra de unión", "«I like pasta ___ it is tasty.» Opciones: because, but. (tasty = rico)", ["La segunda parte da una razón.", "Una razón se une con because.", "Como a mí me gusta, la razón es que es rico."], "because"),
    ],
    [
        ("Elegir una palabra sin mirar las pistas.", "Se adivina y la oración pierde sentido.", "Subraya las pistas antes de elegir."),
        ("Confundir because con but.", "Se mira solo que son palabras pequeñas.", "Because da una razón; but muestra una diferencia."),
    ],
    [
        ("¿Qué significa «because»?", "Porque", "Introduce una razón."),
        ("Pistas: ball, racket. ¿Qué palabra falta? «She plays ___.» Opciones: tennis, chess.", "tennis", "Racket y ball se usan en tennis."),
        ("¿Qué significa «very»?", "Muy", "Very refuerza una cualidad, como very big."),
    ],
    [
        ("«The bakery is closed today, ___ I buy bread at the market.» Opciones: so, but. (so = así que) ¿Qué palabra señala el resultado?", "so", "Como la panadería está cerrada, el resultado es comprar en otro lugar."),
        ("«Ana likes soccer ___ Tom likes chess.» Opciones: but, because. (Muestran gustos distintos.)", "but", "But marca la diferencia entre dos gustos."),
        ("En «Pablo has a helmet and a bike. He goes ___.» ¿Qué palabra falta? Opciones: cycling, reading.", "cycling", "Helmet y bike son pistas de andar en bicicleta."),
    ],
    [
        ("Texto: «Sofía is in the library. She has a book and a pencil. She is very quiet.» (quiet = callada) ¿Qué palabra clave dice dónde está Sofía?", "library", "La oración dice in the library."),
        ("Completa: «I am tired ___ I ran a lot.» Opciones: because, but.", "because", "Correr mucho es la razón del cansancio."),
        ("Completa: «Today is sunny ___ warm.» Opciones: and, but. (sunny = soleado; warm = cálido)", "and", "Las dos ideas son buenas y se suman, no se oponen."),
    ],
    [
        ("Texto: «Rosa is at the hospital. She is a doctor.» Una persona dice que Rosa trabaja en una panadería. ¿Tiene razón? Responde sí o no.", "No", "Las pistas hospital y doctor muestran otro lugar de trabajo."),
        ("«Max is very hungry. He eats a ___.» Opciones: sandwich, helmet. ¿Qué pista decide la respuesta?", "hungry", "Hungry (con hambre) lleva a elegir una comida."),
    ],
    [
        ("Pistas: bat, glove, field (campo). ¿Qué deporte es? Opciones: baseball, swimming.", "baseball", "Bat y glove se usan en baseball."),
        ("«I like the park ___ it has big trees.» Opciones: because, but. ¿Qué palabra falta?", "because", "Los árboles grandes explican por qué le gusta."),
    ],
    [("Lee el aviso: «Library open today. Please be very quiet.» ¿Qué piden en el aviso? a) Hablar fuerte b) Estar en silencio", "b", "Very quiet significa muy callado.")],
    [
        ("¿Qué es una palabra clave?", "La que lleva el sentido de la oración", "Las demás palabras dan pistas a su alrededor."),
        ("¿Qué significa «but»?", "Pero", "But muestra una diferencia."),
        ("¿Qué haces después de elegir una palabra?", "Releer la oración para comprobar que tiene sentido", "Así compruebas que la elección calza."),
    ],
    task("Lee este texto: «Tomás is at the park with a ball and his friends. He plays soccer because it is fun. Today is sunny but windy.» Escribe en tu hoja: a) las palabras clave del texto, b) la pista que muestra el deporte, c) una oración nueva con because sobre algo que te gusta hacer.", "a) park, ball, soccer, sunny, windy. b) ball and friends. c) I like swimming because it is fun.", ["identifica al menos tres palabras clave", "señala la pista del deporte", "su oración nueva usa because con una razón"], ["hoja con respuestas a), b) y c)"], ["escribir una oración sin razón después de because", "no justificar con una pista"], "Pide que señale con el dedo en el texto cada pista que usó."),
    "Escribe tres oraciones con and, but y because sobre tu comida favorita.",
    "Escribe un mini texto de tres líneas con pistas para que otra persona adivine tu deporte favorito sin nombrarlo.",
)

# ================================================================ OA 11 clase 3: estrategia comunicativa
lesson(
    OA11, 3,
    "Las listas de verbos y frases escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé una estrategia para aprender vocabulario en bloques (chunks) y otra para pedir ayuda cuando no sé una palabra. Sirve para hablar con más seguridad.",
    ["Conozco palabras de deportes y pasatiempos.", "Sé que algunas palabras van siempre juntas."],
    [
        "Un chunk es un bloque de palabras que se aprende junto. En inglés cada pasatiempo va con su verbo: play soccer, play chess (jugar), go swimming, go skating (ir a nadar, ir a patinar), do homework (hacer la tarea), make a sandwich (preparar un sándwich). No se dice «do soccer» ni «make homework».",
        "Si no sabes una palabra, puedes pedir ayuda con frases completas: How do you say «patinar» in English? (¿Cómo se dice «patinar» en inglés?), What does «chess» mean? (¿Qué significa «chess»?), Can you repeat, please? (¿Puedes repetir, por favor?) y I don't know the word. (No sé la palabra).",
        "Otra estrategia es describir la palabra que no sabes: It's a thing for writing. (Es una cosa para escribir.), It's a place for books. (Es un lugar para libros.). Así la otra persona te ayuda a encontrar pencil o library sin que te quedes en silencio.",
    ],
    [("chunk", "bloque de palabras que se aprende junto"), ("play + juego", "jugar a algo: play chess"), ("go + -ing", "ir a hacer algo: go swimming"), ("do / make", "hacer: do homework, make a cake"), ("How do you say…?", "¿Cómo se dice…?"), ("What does… mean?", "¿Qué significa…?"), ("Can you repeat, please?", "¿Puedes repetir, por favor?")],
    [
        ("Elegir el verbo del bloque", "Completa: «I ___ homework after school.» Opciones: do, make, play.", ["Se dice do homework.", "Do va con tareas y trabajos.", "Los otros no forman el bloque."], "do"),
        ("Pedir ayuda con una frase", "No recuerdas cómo se dice «patinar». ¿Qué le preguntas a tu profesor? Opciones: How do you say «patinar» in English? / Excuse me, sorry.", ["Necesitas una palabra en inglés.", "La pregunta para eso es How do you say…?", "La otra opción no pide nada."], "How do you say «patinar» in English?"),
    ],
    [
        ("Decir «do soccer».", "Se traduce palabra por palabra.", "Con juegos y deportes de equipo se usa play: play soccer."),
        ("Quedarse callado cuando falta una palabra.", "Se cree que hay que saberlo todo.", "Usa una frase de ayuda o describe lo que quieres decir."),
    ],
    [
        ("Completa: «We ___ chess on Fridays.» Opciones: play, go.", "play", "Los juegos como el ajedrez van con play."),
        ("¿Cuál es el bloque correcto? a) go swimming b) do swimming", "a", "Las actividades con -ing usan go."),
        ("¿Qué significa «Can you repeat, please?»", "¿Puedes repetir, por favor?", "Se usa cuando no entendiste."),
    ],
    [
        ("Une el verbo con el bloque: a) play b) go c) make. Bloques: 1) a sandwich 2) skating 3) tennis. Escribe tres pares como a1.", "a3, b2, c1", "Play va con tennis, go con skating y make con a sandwich."),
        ("Quieres saber el significado de «bakery». ¿Qué preguntas? a) What does «bakery» mean? b) Where is the bakery?", "a", "What does… mean? pide el significado."),
        ("Quieres describir un lápiz sin saber la palabra. ¿Cuál frase sirve? a) It's a thing for writing. b) It's a place for books.", "a", "Describe para qué sirve un lápiz."),
    ],
    [
        ("Completa: «I ___ my homework before dinner.» Opciones: do, play.", "do", "Do homework es el bloque correcto."),
        ("Completa: «My brother and I ___ skating on Saturdays.» Opciones: go, make.", "go", "Go skating usa go más -ing."),
        ("Quieres preguntar cómo se dice «bicicleta» en inglés. Escribe la pregunta completando: «How do you ___ «bicicleta» in English?»", "say", "How do you say… pide la palabra en inglés."),
    ],
    [
        ("En «I ___ a cake for my mom's birthday», ¿cuál verbo va? Opciones: make, do, go. (mom = mamá)", "make", "Make a cake es el bloque correcto."),
        ("Una compañera dice un bloque incorrecto: «I go chess.» ¿Cómo se corrige?", "I play chess.", "El ajedrez se juega, así que lleva play."),
    ],
    [
        ("Palabras: tennis, skating, chess, swimming. Con go se pueden decir dos de ellas (go ___). ¿Cuáles? (Escribe las dos palabras en el orden de la lista.)", "skating, swimming", "Go skating y go swimming son los bloques con -ing."),
        ("Cuentas los bloques: play soccer, go skating, do homework, make a cake, play chess. ¿Cuántos usan play?", "2", "Play soccer y play chess."),
    ],
    [("En una conversación no entiendes una frase que dijo tu compañero. ¿Qué dices? a) Can you repeat, please? b) That's cool!", "a", "Pides que repita lo que no entendiste.")],
    [
        ("¿Qué es un chunk?", "Un bloque de palabras que se aprende junto", "Aprender en bloques ayuda a no equivocar el verbo."),
        ("¿Qué verbo va con homework?", "do", "Se dice do homework."),
        ("¿Qué puedes hacer si no sabes una palabra?", "Preguntar o describirla", "Así sigues comunicando."),
    ],
    task("Lee esta lista de bloques: play chess, play soccer, go swimming, go skating, do homework, make a sandwich. Escribe en tu hoja cinco oraciones sobre tu semana, cada una con un bloque distinto (por ejemplo, I play soccer on Monday). Después escribe las dos frases que usarías para pedir ayuda si no recuerdas una palabra.", "I play chess on Monday. I go swimming on Wednesday. I do homework at home. I make a sandwich after school. I play soccer on Saturday. Frases: How do you say…? / What does… mean?", ["usa cinco bloques distintos bien formados", "cada oración tiene sujeto y verbo", "escribe dos frases de ayuda correctas"], ["hoja con cinco oraciones y dos frases de ayuda"], ["decir do soccer", "escribir un bloque incompleto"], "Subraya los bloques y pregunta por qué cada verbo es el correcto."),
    "Copia los seis bloques de la lista y escribe su significado en español.",
    "Inventa un bloque nuevo con go y -ing que no aparezca en la lista, como go cycling, y úsalo en una oración.",
)

# ================================================================ OA 11 clase 4: interactuar con apoyo
lesson(
    OA11, 4,
    "Los diálogos y bancos de palabras escritos en cada ejercicio, lápiz, una hoja y una persona para practicar.",
    "Aprenderé a usar vocabulario y expresiones en diálogos cortos con apoyo de un banco de palabras. Sirve para conversar sobre mis gustos y reaccionar con naturalidad.",
    ["Conozco expresiones como That's cool! y Thanks a lot!", "Sé usar play, go y do en bloques."],
    [
        "En un diálogo cada persona habla por turnos. Para que suene natural, une tres cosas: una pregunta, una respuesta con palabras del tema y una reacción con una expresión común. Ejemplo: A: «What sport do you like?» B: «I like swimming.» A: «That's cool!»",
        "Un banco de palabras (word bank) es una lista de ayuda con las palabras que puedes usar. Antes de hablar, léelo y elige las que calzan. Si olvidas una, mira el banco o usa una frase de ayuda como How do you say…?",
        "Al terminar, revisa dos cosas: ¿usé palabras del tema?, ¿mi reacción calza con lo que dijo la otra persona? Si te dicen «I won a medal!», lo natural es Great! o Well done!, no Sorry! Si alguien cuenta un problema, dices Sorry to hear that. (Lamento oír eso.)",
    ],
    [("turn", "turno"), ("word bank", "banco de palabras: lista de ayuda"), ("What sport do you like?", "¿Qué deporte te gusta?"), ("I like…", "Me gusta…"), ("medal", "medalla"), ("Me too.", "Yo también.")],
    [
        ("Completar un diálogo", "A: «What sport do you like?» B: «I like ___.» A: «That's cool!» Banco: skating, bakery, library. ¿Qué palabra elige B?", ["La pregunta es por un deporte.", "Solo skating es un deporte del banco.", "B responde I like skating."], "skating"),
        ("Elegir la reacción", "A: «I won a medal!» B: ___ Opciones: Well done! / Excuse me.", ["A cuenta un logro.", "Un logro se felicita.", "La reacción es Well done!"], "Well done!"),
    ],
    [
        ("Responder con una palabra que no es del tema.", "No se lee la pregunta completa.", "Lee la pregunta y elige del banco una palabra del tema que pide."),
        ("Reaccionar con una expresión que no calza.", "Se repite una frase sin pensar en el contexto.", "Antes de reaccionar, piensa qué contó la otra persona."),
    ],
    [
        ("¿Qué significa «What sport do you like?»", "¿Qué deporte te gusta?", "Pregunta por un gusto en deportes."),
        ("A: «I like chess.» B: «___» Opciones: That's cool!, Sorry!", "That's cool!", "Muestra interés por el gusto de A."),
        ("¿Qué significa «Me too.»?", "Yo también", "Se usa para decir que también te pasa o te gusta."),
    ],
    [
        ("A: «Do you play tennis?» B: «Yes, I ___.» Opciones: do, am. ¿Cuál completa?", "do", "La pregunta empieza con Do, así que se responde Yes, I do."),
        ("Ordena el diálogo: a) That's cool! b) I like cycling. c) What do you like? Escribe las letras en orden.", "c, b, a", "Primero va la pregunta, luego la respuesta y al final la reacción."),
        ("Banco: library, bakery, hospital. A: «Where do you buy bread?» B: «At the ___.» ¿Qué palabra elige B?", "bakery", "El pan se compra en la panadería."),
    ],
    [
        ("Completa el diálogo: A: «Do you like cycling?» B: «No, I ___.» Opciones: don't, am.", "don't", "La pregunta empieza con Do, así que se responde No, I don't."),
        ("A: «I love reading.» B: «Me ___!» Opciones: too, cool. B quiere decir que a B también le gusta leer.", "too", "Me too significa yo también."),
        ("Banco: swimming, chess, library. A: «What do you do on Sundays?» B: «I go ___.» ¿Qué palabra del banco completa el bloque con go?", "swimming", "Go swimming es un bloque; chess lleva play y library es un lugar."),
    ],
    [
        ("A: «I made a chocolate cake.» ¿Cuál es mejor respuesta de B? a) Great! b) Sorry!", "a", "Great! celebra algo que A hizo bien."),
        ("A: «My bike is broken.» B: «Sorry to hear that.» (broken = rota; Sorry to hear that = Lamento oír eso) ¿B reacciona bien? Responde sí o no.", "Sí", "Sorry to hear that muestra pena por un problema."),
    ],
    [
        ("Banco: skating, cycling, chess. Completa: «I go ___ on Sundays.» Hay dos posibles; escribe una de ellas.", "skating o cycling", "Go acepta actividades con -ing, y chess lleva play."),
        ("En «A: I love music. B: Me too!» ¿Qué dice B?", "Que a B también le gusta la música", "Me too es yo también."),
    ],
    [("Dos amigos hablan. A: «I have a new skateboard.» B: «___ Can I try it?» Opciones: a) That's cool! b) Excuse me! ¿Cuál completa mejor?", "a", "That's cool! reacciona al nuevo skateboard antes de pedir probarlo.")],
    [
        ("¿Qué tres partes tiene un buen turno de diálogo?", "Pregunta, respuesta y reacción", "Así la conversación fluye."),
        ("¿Para qué sirve un banco de palabras?", "Para elegir palabras de ayuda", "Es una lista con vocabulario útil."),
        ("¿Qué dices si alguien te cuenta un logro?", "Well done! o Great!", "Son expresiones para felicitar."),
    ],
    task("Practica con una persona de tu casa este diálogo: A: «What sport do you like?» B: «I like ___.» A: «That's cool! Do you play it on weekends?» B: «Yes, I do. / No, I don't.» Banco de palabras: swimming, skating, tennis, chess, cycling. Escribe tu versión completa del diálogo en la hoja, usando dos palabras del banco y una expresión (That's cool!, Great! o Well done!). Luego léelo en voz alta con la otra persona, cada uno su turno.", "A: What sport do you like? B: I like tennis. A: That's cool! Do you play it on weekends? B: Yes, I do. Great!", ["usa palabras del banco que calzan con la pregunta", "incluye una expresión común adecuada", "lo lee por turnos con claridad"], ["hoja con el diálogo escrito y lectura en voz alta"], ["responder con una palabra fuera del tema", "reaccionar sin calzar con lo dicho"], "Pide que cambie la reacción por otra que también calce y explique por qué."),
    "Escribe el diálogo del ejemplo cambiando el deporte y la expresión final.",
    "Escribe un diálogo de seis turnos sobre pasatiempos entre dos amigos, con tres expresiones comunes distintas.",
)

# ================================================================ OA 12 clase 1: preguntas y respuestas
lesson(
    OA12, 1,
    "Los diálogos y tarjetas de preguntas escritos en cada ejercicio, lápiz, una hoja y una persona para practicar.",
    "Aprenderé a hacer y responder preguntas con Who, How much, How many, Can y Where. Sirve para conversar con mis compañeros y profesores.",
    ["Sé decir mi nombre y qué me gusta.", "Conozco números hasta 100 en inglés."],
    [
        "Cada pregunta pide un tipo de dato. Who…? (¿Quién?) pide una persona: «Who is your teacher?» — «Ms. Rojas is my teacher.» How much…? (¿Cuánto?) pide un precio o una cantidad que no se cuenta: «How much is the pen?» — «It's 500 pesos.» How many…? (¿Cuántos?) pide algo que se cuenta: «How many books do you have?» — «I have four.»",
        "Can…? (¿Puedes…?) pide si alguien es capaz de algo o tiene permiso. Se responde corto: «Can you swim?» — «Yes, I can.» o «No, I can't.» Where…? (¿Dónde?) pide un lugar: «Where is the library?» — «It's next to the gym.»",
        "Para responder bien, escucha la primera palabra de la pregunta: dice qué dato debes dar. Responde con una oración completa o con la respuesta corta. Si no entiendes, usa Can you repeat, please?",
    ],
    [("Who…?", "¿Quién…?"), ("How much…?", "¿Cuánto…? (precio o cantidad que no se cuenta)"), ("How many…?", "¿Cuántos…? (cosas que se cuentan)"), ("Can…?", "¿Puedes…?"), ("Where…?", "¿Dónde…?"), ("Yes, I can. / No, I can't.", "Sí puedo. / No puedo.")],
    [
        ("Elegir la respuesta", "Pregunta: «Where is the bakery?» Opciones: a) It's near the school. b) I have three. c) Ms. Rojas.", ["Where pide un lugar.", "Near the school es un lugar.", "Las otras respuestas dan una cantidad y una persona."], "a"),
        ("Responder con respuesta corta", "Pregunta: «Can you ride a bike?» Respondes que sí. ¿Qué dices?", ["Can se responde con Can o can't.", "La respuesta afirmativa es Yes, I can.", "No hace falta repetir toda la oración."], "Yes, I can."),
    ],
    [
        ("Responder «Where is it?» con un número.", "No se mira la primera palabra de la pregunta.", "Where pide un lugar, no una cantidad."),
        ("Usar How many con cosas que no se cuentan, como agua.", "Se confunde con How much.", "Con cosas que se cuentan usa How many; con precio o líquidos, How much."),
    ],
    [
        ("¿Qué significa «Who is your teacher?»", "¿Quién es tu profesor o profesora?", "Who pregunta por una persona."),
        ("«How many pencils do you have?» ¿Qué dato pide? a) Un lugar b) Una cantidad que se cuenta", "b", "How many pide un número de cosas contables."),
        ("¿Cómo respondes «No» a «Can you swim?»", "No, I can't.", "Can't es la forma corta de cannot."),
    ],
    [
        ("«How much is the notebook?» Opciones: a) It's 800 pesos. b) I have two. (notebook = cuaderno)", "a", "How much pide el precio."),
        ("«Who is Tom?» Opciones: a) He's my cousin. b) It's at home.", "a", "Who pide una persona, y he's my cousin la describe."),
        ("Completa la pregunta: «___ many books are on the desk?» Opciones: How, Who.", "How", "La pregunta es How many…?"),
    ],
    [
        ("Completa: «___ is your best friend?» La respuesta es «Sofía is my best friend.» Opciones: Who, Where.", "Who", "La respuesta nombra a una persona, así que la pregunta es Who."),
        ("Completa: «___ you play the guitar?» La respuesta es «Yes, I can.» Opciones: Can, Where.", "Can", "La respuesta corta con can corresponde a una pregunta con Can."),
        ("Completa: «How ___ is the bus ticket?» La respuesta es «It's 700 pesos.» Opciones: much, many.", "much", "El precio se pregunta con How much."),
    ],
    [
        ("Escribe la pregunta para esta respuesta: «It's in front of the school.» Opciones: a) Where is the park? b) How many parks?", "a", "La respuesta indica un lugar."),
        ("Pregunta: «How much water is in the bottle?» (bottle = botella) ¿Por qué se usa How much y no How many?", "Porque el agua no se cuenta", "El agua es una cantidad que no se cuenta en unidades."),
    ],
    [
        ("Sara dice: «There are twelve students.» (students = estudiantes) ¿Qué pregunta responde? a) How many students are there? b) Who is the teacher?", "a", "La respuesta es una cantidad contable."),
        ("Diálogo: A: «Can I use your pen?» B: «Yes, you can.» ¿A pide permiso o pregunta un precio?", "Pide permiso", "Can I… pide permiso."),
    ],
    [("En la tienda de la escuela preguntas por el precio de un jugo. ¿Qué pregunta usas? a) How much is the juice? b) Where is the juice?", "a", "Para saber el precio se usa How much.")],
    [
        ("¿Qué pregunta pide un lugar?", "Where…?", "Where significa dónde."),
        ("¿Qué pregunta usas para contar objetos?", "How many…?", "Se usa con cosas que se cuentan."),
        ("¿Cómo respondes afirmativamente a «Can you sing?»", "Yes, I can.", "Es la respuesta corta con can."),
    ],
    task("Lee esta tarjeta de preguntas: 1) Who is your teacher? 2) How many books do you have? 3) How much is a pen? 4) Can you play chess? 5) Where is your school? Practica con una persona de tu casa: una persona pregunta, la otra responde con una oración completa o respuesta corta. Escribe en tu hoja tus cinco respuestas y practícalas en voz alta, luego cambien de rol.", "1) Ms. Rojas is my teacher. 2) I have six books. 3) A pen is 500 pesos. 4) Yes, I can. 5) My school is near my house.", ["cada respuesta da el tipo de dato que pide la pregunta", "usa respuestas cortas o completas bien formadas", "lo practica oralmente por turnos"], ["hoja con cinco respuestas y práctica oral"], ["responder con un dato que no corresponde a la pregunta", "no usar can o can't en la 4"], "Pide que cambie la pregunta 3 por otra con How much y la responda."),
    "Copia las cinco palabras interrogativas de la explicación con su significado.",
    "Escribe cuatro preguntas nuevas, una con Who, otra con Where, otra con How many y otra con Can, sobre tu curso.",
)

# ================================================================ OA 12 clase 2: acciones, posición y objetos
lesson(
    OA12, 2,
    "Las escenas y listas escritas en cada ejercicio, lápiz, una hoja y objetos de la casa para practicar.",
    "Aprenderé a describir cómo se hace una acción, dónde está un objeto y cómo es. Sirve para dar indicaciones y describir cosas en una conversación.",
    ["Conozco verbos como run, read y play.", "Conozco palabras como bottle, car y table."],
    [
        "Para decir cómo se hace una acción se usa un adverbio después del verbo: «He reads fast.» (Lee rápido.), «She reads very slowly.» (Lee muy despacio.), «Tom plays well.» (Juega bien.), «Ana writes carefully.» (Escribe con cuidado.) Very antes del adverbio lo hace más fuerte: very slowly.",
        "Para decir dónde está un objeto se usan: next to (al lado de), beside (junto a), in front of (delante de) y behind (detrás de). Ejemplo: «The ball is behind the chair.» (La pelota está detrás de la silla.) «The lamp is next to the bed.» (La lámpara está al lado de la cama.)",
        "Para identificar objetos: these (estos) se usa para varios objetos cercanos y those (esos) para varios objetos lejanos: «These cars are fast.» «Those bikes are red.» Para el material se usa It's a… : «It's a plastic bottle.» (Es una botella de plástico.) «It's a wooden table.» (Es una mesa de madera.)",
    ],
    [("fast / slowly", "rápido / despacio"), ("well", "bien"), ("next to / beside", "al lado de / junto a"), ("in front of", "delante de"), ("behind", "detrás de"), ("these / those", "estos (cerca) / esos (lejos)"), ("plastic / wooden", "de plástico / de madera")],
    [
        ("Describir cómo hace una acción", "Mateo corre más lento que todos. ¿Cuál oración lo describe? a) Mateo runs very slowly. b) Mateo runs very fast.", ["Corre más lento que todos.", "Se necesita slowly.", "La opción a lo dice."], "a"),
        ("Decir dónde está un objeto", "La escena: la mochila está detrás del sillón. Completa: «The backpack is ___ the sofa.» Opciones: behind, in front of.", ["Detrás es behind.", "Delante sería in front of.", "La escena dice detrás."], "behind"),
    ],
    [
        ("Decir «She reads slow» sin la terminación.", "Se usa el adjetivo en lugar del adverbio.", "Con slowly se escribe la terminación -ly."),
        ("Usar these para objetos lejanos.", "Se confunde cerca con lejos.", "These son los cercanos y those los lejanos."),
    ],
    [
        ("¿Qué significa «in front of»?", "Delante de", "Describe una posición."),
        ("¿Qué significa «very slowly»?", "Muy despacio", "Very refuerza slowly."),
        ("¿Qué palabra se usa para varias cosas lejanas? Opciones: these, those.", "those", "Those señala varias cosas lejos."),
    ],
    [
        ("Escena: la lámpara está al lado de la cama. ¿Qué oración es correcta? a) The lamp is next to the bed. b) The lamp is behind the bed.", "a", "Next to significa al lado de."),
        ("«___ cars are fast.» Hablas de dos autos que están lejos de ti. Opciones: These, Those.", "Those", "Se usa those para objetos lejanos."),
        ("«It's a ___ bottle.» La botella es de plástico. Opciones: plastic, wooden.", "plastic", "Plastic es el material de la botella."),
    ],
    [
        ("Escena: el gato está sentado delante de la puerta. Escribe la oración completando: «The cat is ___ the door.»", "in front of", "In front of significa delante de."),
        ("Ana lee tres páginas en un minuto y Luis lee diez. ¿Qué oración describe a Luis? a) Luis reads fast. b) Luis reads slowly.", "a", "Luis lee más páginas, entonces lee rápido."),
        ("Escena: dos globos junto a la ventana. Completa: «The balloons are ___ the window.» Opciones: beside, behind.", "beside", "Junto a se dice beside."),
    ],
    [
        ("Escena: una taza, un plato y una jarra están en una fila. La taza está next to el plato y la jarra está next to el plato por el otro lado. ¿Qué objeto está al lado de los otros dos?", "El plato", "El plato queda en el medio, con la taza a un lado y la jarra al otro."),
        ("En «The table is wooden and the bottle is plastic», ¿qué objeto es de madera?", "La mesa", "Wooden significa de madera y se dice de table."),
    ],
    [
        ("Escena: arriba de la mesa hay un vaso. Al lado del vaso hay un plato y detrás del plato hay una jarra. ¿Qué objeto está detrás del plato?", "La jarra", "La jarra se ubica detrás del plato."),
        ("Texto: «Pedro writes carefully. Lucía writes quickly.» (quickly = rápido) ¿Quién escribe con más cuidado?", "Pedro", "Carefully significa con cuidado y se dice de Pedro."),
    ],
    [("Una compañera te pregunta dónde dejaste tu botella de plástico. Está junto a tu mochila. ¿Qué respondes? a) It's beside my backpack. b) It's very slowly.", "a", "Beside my backpack dice dónde está.")],
    [
        ("¿Qué significa «behind»?", "Detrás de", "Indica una posición, atrás de otro objeto."),
        ("¿Cómo se dice «Lee muy despacio» en inglés?", "He reads very slowly.", "Se usa very slowly para despacio."),
        ("¿Qué palabra señala varias cosas cerca?", "these", "These son las cosas cercanas."),
    ],
    task("Lee este modelo: «The lamp is next to the bed. The bag is behind the chair. These books are on the desk. It's a plastic bottle.» Elige cuatro objetos de tu casa y escribe una oración sobre dónde está cada uno (usa next to, beside, in front of o behind), una oración con these o those y una oración con plastic o wooden. Luego descríbele la escena en inglés a una persona de tu casa mientras ella la mira.", "The cup is beside the book. The shoes are behind the door. These pencils are on the table. It's a wooden box.", ["usa al menos tres expresiones de posición distintas", "incluye these o those correctamente", "describe un material con plastic o wooden"], ["hoja con seis oraciones y descripción oral"], ["confundir these con those", "no escribir la expresión de posición completa"], "Pide que cambie un objeto de lugar y diga la nueva oración."),
    "Escribe las cuatro expresiones de posición con su significado.",
    "Escribe cuatro oraciones sobre tu familia o tu curso con very fast, very slowly, well y carefully.",
)

# ================================================================ OA 12 clase 3: estados de ánimo, actividades y gustos
lesson(
    OA12, 3,
    "Los diálogos y listas escritos en cada ejercicio, lápiz, una hoja y una persona para practicar.",
    "Aprenderé a decir cómo se ve alguien, qué opino de una actividad y qué me gusta o no. Sirve para conversar sobre emociones y gustos.",
    ["Conozco palabras como tired, hungry y happy.", "Sé que like significa me gusta."],
    [
        "Para describir el estado de ánimo se usa looks + adjetivo: «He looks tired.» (Se ve cansado.), «She looks hungry.» (Se ve con hambre.), «You look nervous.» (Te ves nervioso.), «They look good.» (Se ven bien.) Con I y you se escribe look sin -s; con he, she o it se escribe looks.",
        "Para opinar sobre una actividad se usa el verbo con -ing: «Skating is cool.» (Patinar es genial.), «Riding a bike is boring.» (Andar en bicicleta es aburrido, según quien lo opina.) Cool es positivo y boring es negativo.",
        "Para gustos: I love… (me encanta), I like… (me gusta), I don't mind… (no me molesta, me da lo mismo) e I hate… (odio, no me gusta nada). Después de estos verbos se usa -ing: «I love playing baseball.» «I don't mind washing dishes.» «I hate waiting.»",
    ],
    [("looks tired / hungry / nervous", "se ve cansado / con hambre / nervioso"), ("cool / boring", "genial / aburrido"), ("I love…", "me encanta…"), ("I like…", "me gusta…"), ("I don't mind…", "no me molesta…"), ("I hate…", "no soporto…")],
    [
        ("Describir el estado de ánimo", "Pablo bosteza (yawns) y se frota los ojos. Completa: «Pablo looks ___.» Opciones: tired, nervous.", ["Bostezar y frotarse los ojos indica sueño.", "Tired significa cansado.", "La respuesta es tired."], "tired"),
        ("Expresar un gusto", "A Rosa le encanta jugar baseball. Escribe su oración con I love.", ["Después de love se usa -ing.", "Playing baseball es jugar baseball.", "Se escribe I love playing baseball."], "I love playing baseball."),
    ],
    [
        ("Escribir «He look tired».", "Se olvida la -s con he.", "Con he, she o it se escribe looks."),
        ("Decir «I like play chess».", "No se usa -ing después de like.", "Escribe I like playing chess."),
    ],
    [
        ("¿Qué significa «I hate…»?", "No soporto… o odio…", "Es el gusto más negativo."),
        ("¿Qué significa «boring»?", "Aburrido", "Es una opinión negativa."),
        ("Completa: «She ___ hungry.» Opciones: looks, look.", "looks", "Con she se agrega la -s."),
    ],
    [
        ("Ordena de más a menos gusto: I hate, I love, I like. Escribe las tres expresiones separadas por comas.", "I love, I like, I hate", "Love es lo más fuerte, luego like y hate es lo contrario."),
        ("«___ is cool.» Opciones: Skating, Skate. Opinas sobre la actividad.", "Skating", "Para una actividad como sujeto se usa -ing."),
        ("Mateo no tiene problema en lavar los platos, tampoco le encanta. ¿Qué expresión usa? a) I don't mind washing dishes. b) I hate washing dishes.", "a", "I don't mind significa que no le molesta."),
    ],
    [
        ("Lucía tiembla (trembles) antes de cantar en el escenario. Completa: «Lucía looks ___.» Opciones: nervous, hungry.", "nervous", "Temblar antes de actuar muestra nervios."),
        ("A Tom le encanta andar en bicicleta. Escribe: «I ___ cycling.» con la expresión de gusto fuerte.", "love", "Love expresa un gusto muy fuerte."),
        ("Opinas que ver una película larga es aburrido. Completa: «Watching long movies is ___.» Opciones: boring, cool.", "boring", "Aburrido se dice boring."),
    ],
    [
        ("Texto: «Ana looks tired. She loves helping at home.» ¿Cómo se ve Ana?", "Cansada", "Looks tired significa se ve cansada."),
        ("«I don't mind walking.» ¿A quién le parece mal caminar: a la persona que habla o a nadie?", "A nadie", "Don't mind significa que no le molesta."),
    ],
    [
        ("Ordena las palabras: tired / looks / Sam. Escribe la oración completa.", "Sam looks tired.", "El sujeto va primero y luego looks tired."),
        ("Un compañero dice: «Chess is cool, but waiting is boring.» ¿Qué actividad le parece aburrida?", "Waiting", "Boring se dice de waiting."),
    ],
    [("Tu amigo llega a clases bostezando y frotándose los ojos. Quieres decir cómo lo ves. ¿Qué dices? a) You look tired. b) You love tired.", "a", "You look tired describe el estado de ánimo.")],
    [
        ("¿Cómo se dice «Se ve nervioso» en inglés?", "He looks nervous.", "Looks + adjetivo describe el ánimo."),
        ("¿Qué significa «I don't mind»?", "No me molesta", "No es ni un gusto fuerte ni un rechazo."),
        ("¿Qué forma del verbo sigue a «I love»?", "La forma con -ing", "Se dice I love dancing."),
    ],
    task("Lee este modelo de diálogo: A: «You look tired.» B: «Yes, I played soccer. I love playing soccer, but I don't mind resting.» A: «Skating is cool, too!» Elige tu estado de ánimo (tired, hungry, nervous o good) y tres gustos: uno con I love, otro con I like y otro con I hate o I don't mind. Escribe un diálogo de cuatro turnos en tu hoja y léelo en voz alta con una persona de tu casa.", "A: You look hungry. B: Yes, I am. I love eating fruit. I like playing chess. I don't mind washing dishes. A: That's cool!", ["usa looks con un estado de ánimo adecuado", "incluye tres expresiones de gusto con -ing", "lee el diálogo con turnos claros"], ["hoja con diálogo de cuatro turnos y lectura en voz alta"], ["olvidar la -s en looks", "no usar -ing después del verbo de gusto"], "Pide que cambie un gusto fuerte por uno suave y cuente cómo cambia el mensaje."),
    "Escribe tres oraciones con I love, I like y I hate sobre comidas o deportes.",
    "Escribe un diálogo de seis turnos en el que una persona se ve nerviosa antes de un examen y la otra la anima.",
)

# ================================================================ OA 12 clase 4: pasado, intenciones y futuro
lesson(
    OA12, 4,
    "Los diálogos y calendarios escritos en cada ejercicio, lápiz, una hoja y una persona para practicar.",
    "Aprenderé a hablar del pasado, de lo que necesito o quiero y de lo que haré. Sirve para conversar sobre planes y recuerdos.",
    ["Conozco los días de la semana y los meses.", "Sé que I play y I played hablan de tiempos distintos."],
    [
        "Para hablar del pasado se usan expresiones de tiempo: yesterday (ayer), last week (la semana pasada), last month (el mes pasado), last year (el año pasado). Después se usa el verbo en pasado: «Yesterday I played soccer.» (Ayer jugué fútbol.) «Last week we visited my aunt.» (La semana pasada visitamos a mi tía.) Algunos verbos cambian por completo: go → went (fue), eat → ate (comió), see → saw (vio), have → had (tuvo).",
        "Para intenciones y necesidades se usa we need to / want to / forget to: «We need to study.» (Necesitamos estudiar.) «I want to learn chess.» (Quiero aprender ajedrez.) «Don't forget to bring your book.» (No olvides traer tu libro.)",
        "Para planes del futuro hay tres formas: I'm going to + verbo para un plan: «I'm going to visit my cousin.» (Voy a visitar a mi primo.), y también «I'm going to Easter Island.» (Voy a Isla de Pascua.); el presente con una hora o día cercano: «She's arriving tomorrow.» (Llega mañana.); y will para una predicción: «Man will land on Mars.» (El ser humano llegará a Marte.)",
    ],
    [("yesterday", "ayer"), ("last week / month / year", "la semana / el mes / el año pasado"), ("we need to…", "necesitamos…"), ("I want to…", "quiero…"), ("don't forget to…", "no olvides…"), ("I'm going to…", "voy a…"), ("tomorrow", "mañana"), ("will", "indica una predicción o promesa"), ("went / ate / saw / had", "fue / comió / vio / tuvo")],
    [
        ("Elegir la expresión de tiempo", "«___ I visited my grandmother.» Hablas del día anterior. Opciones: Yesterday, Tomorrow.", ["El día anterior es ayer.", "Visited está en pasado.", "Yesterday calza con pasado."], "Yesterday"),
        ("Distinguir plan y predicción", "«I'm going to visit my aunt in July.» ¿Es un plan o una predicción?", ["I'm going to + verbo indica un plan que ya está decidido.", "Una predicción usa will.", "Es un plan."], "Un plan"),
    ],
    [
        ("Decir «Yesterday I play soccer».", "Se usa el verbo en presente con una expresión del pasado.", "Con yesterday usa el verbo en pasado: played."),
        ("Escribir «I need study».", "Falta to después de need.", "Se escribe I need to study."),
    ],
    [
        ("¿Qué significa «last month»?", "El mes pasado", "Se refiere a un tiempo anterior."),
        ("¿Qué significa «We need to study»?", "Necesitamos estudiar", "Need to expresa necesidad."),
        ("¿Qué expresión es del pasado? Opciones: tomorrow, yesterday.", "yesterday", "Yesterday indica un día anterior."),
    ],
    [
        ("Completa: «___ week we went to the beach.» Opciones: Last, Next. Ocurrió la semana anterior.", "Last", "Last week significa la semana pasada."),
        ("Completa: «I ___ to learn chess.» Opciones: want, wants. (Habla yo.)", "want", "Con I se usa want."),
        ("«She's arriving tomorrow.» ¿Cuándo llega?", "Mañana", "Tomorrow significa mañana."),
    ],
    [
        ("Completa con la expresión para un plan: «I'm ___ to visit my cousin.» Opciones: going, will.", "going", "I'm going to expresa un plan."),
        ("Completa con una predicción: «People ___ travel to Mars one day.» Opciones: will, went.", "will", "Will se usa para predecir."),
        ("Le dices a un compañero que no olvide traer su cuaderno. Completa: «Don't ___ to bring your notebook.»", "forget", "Don't forget to… es no olvides…"),
    ],
    [
        ("Un amigo dice «Last year I traveled to Santiago.» ¿Sobre qué tiempo habla?", "El pasado", "Last year es el año pasado."),
        ("Diálogo: A: «What did you do yesterday?» (= ¿Qué hiciste ayer?) B: «I played chess.» ¿B habló del pasado o del futuro?", "Del pasado", "Yesterday y played muestran tiempo pasado."),
    ],
    [
        ("Ordena la oración: going / I'm / swim / to. Escribe la oración completa.", "I'm going to swim.", "Se forma con I'm going to + verbo."),
        ("Lista: yesterday, tomorrow, last week, next week (= la próxima semana). ¿Cuántas expresiones hablan del pasado?", "2", "Son yesterday y last week."),
    ],
    [("Una amiga pregunta qué hiciste el sábado pasado. Respondes: «Last Saturday I ___ soccer.» Opciones: played, play.", "played", "Con last Saturday se usa el verbo en pasado.")],
    [
        ("¿Cómo se dice «mañana» en inglés?", "Tomorrow", "Es una expresión de futuro."),
        ("¿Qué significa «I'm going to…»?", "Voy a…", "Indica un plan."),
        ("¿Qué expresión de pasado significa «ayer»?", "Yesterday", "Se usa para el día anterior."),
    ],
    task("Lee este modelo: A: «What did you do yesterday?» B: «I played chess. Last week I visited my aunt.» A: «What are you going to do tomorrow?» B: «I'm going to study. We need to bring our books.» Escribe un diálogo de cuatro turnos con una expresión de pasado, un plan con I'm going to y una necesidad con need to. Léelo en voz alta con una persona de tu casa.", "A: What did you do last weekend? B: I played soccer. A: What are you going to do tomorrow? B: I'm going to study. I need to finish my homework.", ["usa una expresión de tiempo pasado con verbo en pasado", "incluye I'm going to y need to bien formados", "lo lee con turnos claros"], ["hoja con el diálogo y lectura en voz alta"], ["decir yesterday con un verbo en presente", "olvidar to después de need"], "Pide que cuente qué cambia si en lugar de tomorrow usa last week."),
    "Escribe cuatro expresiones de tiempo con su significado.",
    "Escribe una predicción con will sobre cómo será el colegio en veinte años.",
)

# ================================================================ OA 12 clase 5: cantidades, orden y comparaciones
lesson(
    OA12, 5,
    "Las tablas y diálogos escritos en cada ejercicio, lápiz, una hoja y una persona para practicar.",
    "Aprenderé a decir cantidades, dar el lugar de alguien en una lista y comparar. Sirve para conversar de carreras, estaturas y juegos.",
    ["Conozco los números hasta cincuenta en inglés.", "Sé comparar usando más y menos."],
    [
        "Los números grandes se dicen así: sixty (60), seventy (70), eighty (80), ninety (90), one hundred (100), two hundred (200). Para el orden se usan first (primero), second (segundo), third (tercero) y fourth (cuarto). Ejemplo: «I am second in the race.» (Voy segundo en la carrera.)",
        "Para comparar dos cosas se agrega -er al adjetivo y se usa than: tall → taller («Tom is taller than Ana.»), fast → faster («My bike is faster than yours.»). Si el adjetivo termina en -y, la y cambia a i: easy → easier → the easiest. Si termina en vocal y consonante, se duplica la consonante: big → bigger → the biggest. Para decir que algo es el más de todos se usa the + -est: the tallest, the easiest.",
        "Con adjetivos largos como difficult no se agrega -er: se usa more difficult than y the most difficult. Ejemplo: «This game is the most difficult of all.» (Este juego es el más difícil de todos.) Compara siempre con dos cosas (than) o con un grupo (of all).",
    ],
    [("first / second / third / fourth", "primero / segundo / tercero / cuarto"), ("sixty / eighty / two hundred", "sesenta / ochenta / doscientos"), ("taller than", "más alto que"), ("faster than", "más rápido que"), ("the easiest", "el más fácil"), ("the most difficult of all", "el más difícil de todos")],
    [
        ("Usar un comparativo", "Tom mide 150 cm y Ana mide 140 cm. Completa: «Tom is ___ than Ana.» Opciones: taller, tallest.", ["Se comparan dos personas.", "Para dos personas se usa -er + than.", "La respuesta es taller."], "taller"),
        ("Usar un superlativo", "En un juego de tres pruebas, la prueba A es fácil, la B más fácil y la C la más fácil de las tres. Completa: «C is the ___ test.» Opciones: easiest, easier.", ["Se compara con las tres pruebas.", "Para el grupo se usa the -est.", "La respuesta es easiest."], "easiest"),
    ],
    [
        ("Decir «more tall than».", "Se aplica la regla de los adjetivos largos a uno corto.", "Con adjetivos cortos se agrega -er: taller than."),
        ("Decir «the most easiest».", "Se mezclan dos formas del superlativo.", "Usa the easiest o the most difficult, nunca las dos."),
    ],
    [
        ("¿Cómo se dice 80 en inglés?", "Eighty", "Es el número ochenta."),
        ("¿Qué significa «second»?", "Segundo", "Es el segundo lugar en una lista."),
        ("¿Qué significa «taller than»?", "Más alto que", "Compara dos personas."),
    ],
    [
        ("Completa: «My bike is ___ than yours.» Opciones: faster, fastest. Se comparan dos bicicletas.", "faster", "Entre dos cosas se usa -er más than."),
        ("Completa: «This puzzle is the ___ of all.» Opciones: most difficult, difficulter.", "most difficult", "Con difficult se usa the most."),
        ("Resultados de una carrera: Ana llegó primera, Leo segunda y Mía tercera. Completa: «Leo is ___.» Opciones: second, third.", "second", "Leo llegó en el segundo lugar."),
    ],
    [
        ("Escribe en inglés con letras el número 60.", "sixty", "El número sesenta se dice sixty."),
        ("Datos: Pedro mide 148 cm y Julia 152 cm. Escribe la oración con taller than sobre Julia.", "Julia is taller than Pedro.", "Julia mide más centímetros que Pedro."),
        ("Tres libros: A tiene 20 páginas, B 30 y C 45. Completa: «C is the ___ book.» Opciones: biggest, smallest. (big = grande)", "biggest", "El que tiene más páginas es el más grande."),
    ],
    [
        ("Un gato es más rápido que una tortuga. ¿Qué oración es correcta? a) The cat is faster than the turtle. b) The turtle is faster than the cat.", "a", "La oración a coincide con el dato dado."),
        ("¿Cómo se dice 200 en inglés? Opciones: two hundred, two thousand.", "two hundred", "200 se dice two hundred."),
    ],
    [
        ("Tres personas: Ana (140 cm), Beto (150 cm) y Carla (155 cm). Escribe la oración con the tallest sobre quien mide más.", "Carla is the tallest.", "Carla mide 155 cm, más que los otros."),
        ("Competencia: Leo 8 puntos, Mía 5 puntos, Sam 7 puntos. ¿Quién llegó tercero?", "Mía", "Ordenados de mayor a menor son Leo 8, Sam 7 y Mía 5, así que Mía queda tercera."),
    ],
    [("En el club de ajedrez, Pablo ganó 4 partidas, Sofía 7 y Tomás 5. Completa: «Sofía is ___.» Opciones: first, second.", "first", "Con 7 partidas ganadas Sofía tiene el mayor número.")],
    [
        ("¿Cómo se dice «el más difícil de todos»?", "The most difficult of all", "Se usa the most con adjetivos largos."),
        ("¿Qué palabra va con taller al comparar dos personas?", "than", "Taller than compara dos."),
        ("¿Cómo se dice 200?", "Two hundred", "Es la forma en inglés de doscientos."),
    ],
    task("Lee esta tabla de una carrera: Ana 12 segundos, Leo 14 segundos, Mía 11 segundos, Sam 13 segundos. Escribe en tu hoja: a) quién fue first, second, third y fourth, b) dos oraciones con faster than comparando a dos niños, c) una oración con the fastest. Después dile el resultado en voz alta a una persona de tu casa.", "Mía was first, Ana second, Sam third, Leo fourth. Mía is faster than Ana. Ana is faster than Leo. Mía is the fastest.", ["ordena correctamente los lugares", "usa faster than con los niños correctos", "usa the fastest bien formado"], ["hoja con resultados y oraciones, y lectura en voz alta"], ["decir the most fast", "invertir los resultados"], "Pide que cambie el tiempo de Mía a 15 segundos y que diga quién sería el más rápido."),
    "Escribe los números 60, 80 y 200 en inglés y practícalos en voz alta.",
    "Escribe cuatro oraciones comparando objetos de tu casa con taller than, bigger than, faster than y the easiest.",
)
