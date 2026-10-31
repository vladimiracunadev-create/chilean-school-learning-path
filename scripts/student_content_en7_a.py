"""Cuaderno del estudiante, 7.º básico Inglés (propuesta), EN07 OA 01 (comprensión global de textos orales).

Todas las «escuchas» las lee un adulto en voz alta: el guion va escrito en el enunciado y el estudiante lo tapa con una hoja.
Los textos son originales y llevan pista en español. Cada palabra o estructura nueva se explica antes de usarla.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "EN07 OA 01"
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


# ---------------------------------------------------------------- clase 1: conversaciones y entrevistas
RADIO = "«Reporter: Welcome to Radio Colegio, Tomás. You are the new captain of the chess club. Tomás: Yes, that's right. Reporter: Why do you like chess? Tomás: Because it makes me think, and I can play with friends. Reporter: When does the club meet? Tomás: On Tuesdays and Thursdays at four o'clock, in room twelve.» (welcome = bienvenido, captain = capitán, chess = ajedrez, makes me think = me hace pensar, meet = reunirse, room = sala)"
PHONE = "«Ana: Hi, Leo. Are you free on Saturday? Leo: Yes, why? Ana: There is a science museum in the city center. The ticket for students costs two thousand five hundred pesos. Leo: Great! What time? Ana: Let's meet at the bus station at ten o'clock. Leo: Perfect. See you on Saturday.» (free = libre, ticket = entrada, costs = cuesta, let's meet = juntémonos)"
SHOP = "«Seller: Can I help you? Customer: Yes, I need running shoes. Seller: These blue shoes cost twenty-five thousand pesos. Customer: Hmm, that is too expensive. Do you have cheaper shoes? Seller: Yes, these gray ones cost eighteen thousand pesos. Customer: Good, I'll take them.» (running shoes = zapatillas para correr, cost = cuestan, too expensive = demasiado caro, cheaper = más baratas, I'll take them = me las llevo)"

lesson(
    OA1, 1,
    "Los guiones de conversaciones y entrevistas escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a reconocer el propósito y el contexto de una conversación o una entrevista: quién habla, con quién, dónde y para qué. Sirve para entender lo esencial de un diálogo en inglés sin traducir cada palabra.",
    ["Sé saludar y hacer preguntas simples con who, where y when.", "Conozco los números y los días de la semana en inglés."],
    [
        "Una conversación (conversation) es un diálogo entre dos o más personas. Una entrevista (interview) es un diálogo especial: una persona, el entrevistador (interviewer o reporter), hace preguntas y otra responde. Antes de entender cada detalle, pregúntate por el propósito (purpose): para qué hablan. Pueden hablar para invitar, comprar, informar o conocer a alguien.",
        "El contexto (context) es la situación: quiénes hablan, dónde están y en qué momento. Las pistas están en frases típicas. «Welcome to…» y «Why do you like…?» aparecen en una entrevista. «Can I help you?» aparece en una tienda. «Are you free on…?» aparece cuando alguien invita. Cada hablante (speaker) tiene un rol, y el rol cambia lo que dice.",
        "Para comprender el texto global, escucha primero una vez y responde tres preguntas: ¿quiénes hablan?, ¿dónde? y ¿para qué? Después escucha otra vez para encontrar datos como la hora, el precio o el lugar. No necesitas entender todas las palabras: las cifras, los nombres y las preguntas ya entregan mucho significado.",
    ],
    [("purpose", "propósito: para qué se habla"), ("context", "contexto: quiénes, dónde y cuándo"), ("interview", "entrevista"), ("speaker", "hablante, la persona que habla"), ("reporter", "reportero, quien hace las preguntas en una entrevista"), ("customer", "cliente")],
    [
        ("Propósito de un aviso", ADULT + "«Good morning, students. Please come to the gym at twelve o'clock. The volleyball team has a short meeting.» (gym = gimnasio, volleyball = vóleibol, meeting = reunión). ¿Quién habla, dónde se oye y para qué?", ["Busco la persona: dice Good morning, students, así que habla alguien del colegio a todo el curso.", "La pista de lugar es the gym, y la de hora es twelve o'clock.", "Please come indica que el propósito es pedir que asistan a una reunión."], "Alguien del colegio habla por altavoz para citar al equipo de vóleibol al gimnasio a las doce"),
        ("Contexto de un diálogo", ADULT + "«Student: Excuse me, can I borrow this book? Librarian: Yes, you can keep it for two weeks.» (borrow = pedir prestado, librarian = bibliotecaria, keep = quedarse con). ¿Dónde ocurre la conversación?", ["Veo la palabra librarian y la acción borrow a book.", "Esas pistas se relacionan con una biblioteca.", "El propósito es pedir un libro prestado."], "En una biblioteca"),
    ],
    [
        ("Pensar que cada diálogo trata de comprar algo porque se oyen precios.", "Se generaliza a partir de una sola palabra.", "Primero identifica quién habla y para qué; el precio puede ser solo un dato."),
        ("Quedarse pensando en una palabra desconocida y perder el resto de la conversación.", "Se intenta traducir todo y se pierde el sentido.", "Sigue escuchando y apóyate en nombres, números y preguntas."),
    ],
    [
        (ADULT + RADIO + " ¿Qué tipo de texto es? a) una entrevista b) un cuento", "a) una entrevista", "Un reportero hace preguntas y Tomás las responde."),
        (ADULT + PHONE + " ¿Para qué hablan Ana y Leo? a) para planear una salida b) para hacer una tarea", "a) para planear una salida", "Ana invita a Leo al museo y acuerdan hora y lugar."),
        (ADULT + SHOP + " ¿Dónde ocurre esta conversación? a) en una tienda de zapatillas b) en una biblioteca", "a) en una tienda de zapatillas", "Hay un vendedor, un cliente, zapatillas y precios."),
    ],
    [
        (ADULT + RADIO + " ¿Cuándo se reúne el club de ajedrez?", "Martes y jueves a las cuatro", "Tomás dice on Tuesdays and Thursdays at four o'clock."),
        (ADULT + RADIO + " ¿Por qué le gusta el ajedrez a Tomás? a) porque lo hace pensar y juega con amigos b) porque puede jugar solo en casa", "a) porque lo hace pensar y juega con amigos", "Su respuesta con because dice it makes me think, and I can play with friends."),
        (ADULT + PHONE + " ¿Dónde y a qué hora se juntan?", "En la estación de buses a las diez", "Ana propone meet at the bus station at ten o'clock."),
    ],
    [
        (ADULT + SHOP + " ¿Por qué el cliente no compra las zapatillas azules?", "Porque son demasiado caras", "Dice that is too expensive y pregunta por otras más baratas."),
        arith(ADULT + PHONE + " Ana y Leo compran una entrada de estudiante cada uno. ¿Cuánto pagan en total, en pesos?", "2*2500", "Cada entrada cuesta dos mil quinientos pesos y son dos personas."),
        arith(ADULT + SHOP + " ¿Cuántos pesos más caras son las zapatillas azules que las grises?", "25000-18000", "Las azules cuestan veinticinco mil y las grises dieciocho mil."),
    ],
    [
        ("Une cada frase con su propósito. 1) «Welcome to Radio Colegio.» 2) «Can I help you?» 3) «Are you free on Saturday?» Propósitos: a) ofrecer ayuda b) saludar al público c) invitar a alguien", "1-b, 2-a, 3-c", "Welcome saluda a quien escucha, Can I help you? ofrece ayuda y Are you free…? invita."),
        ("Una compañera dice: «En la entrevista de la radio, Tomás habla con un amigo en el patio». ¿Qué pista del guion muestra que se equivoca?", "Reporter y Welcome to Radio Colegio", "Esas palabras muestran una entrevista de radio, no una charla de patio."),
    ],
    [
        ("Ordena la conversación de la tienda. A) «Yes, I need running shoes.» B) «Can I help you?» C) «These blue shoes cost twenty-five thousand pesos.» D) «That is too expensive.»", "B, A, C, D", "Primero se ofrece ayuda, luego el cliente pide zapatillas, después se dice el precio y al final el cliente reacciona."),
        (ADULT + RADIO + " ¿Cuántas preguntas hace el reportero? Cuenta solo las oraciones que preguntan.", "2", "Son Why do you like chess? y When does the club meet?"),
    ],
    [(ADULT + "«Attention, please. Tomorrow there is no school bus on route four. Students from route four must take the metro at seven thirty.» (route = recorrido, must take = deben tomar). ¿Cuál es el propósito de este aviso? a) informar un cambio de transporte b) invitar a una fiesta", "a) informar un cambio de transporte", "Dice que no habrá bus y qué hacer en su lugar.")],
    [
        ("¿Quién hace las preguntas en una entrevista?", "El reportero o entrevistador", "Su rol es preguntar para que otra persona responda."),
        ("¿Qué tres preguntas ayudan a entender el contexto?", "Quiénes hablan, dónde y para qué", "Resumen el contexto de la conversación."),
        ("¿Qué frase típica de tienda aparece en el texto de las zapatillas?", "Can I help you?", "El vendedor la usa para ofrecer ayuda."),
    ],
    task("Un adulto lee dos veces este diálogo: «Doctor: Good afternoon, Sofía. What is the problem? Sofía: My throat hurts, and I have a cough. Doctor: Drink warm water and rest at home for two days.» (throat = garganta, hurts = duele, cough = tos, rest = descansar). En tu hoja escribe: quiénes hablan, dónde ocurre, para qué hablan y un dato que sirva de pista.", "Hablan una doctora o un doctor y Sofía. Ocurre en una consulta médica. Hablan para tratar un malestar. Pista: throat hurts y doctor.", ["nombra a los dos hablantes", "indica un lugar coherente con el texto", "escribe un propósito y una pista del guion"], ["hoja con respuestas", "nota del adulto"], ["decir que es una entrevista de radio", "no escribir ninguna pista"], "Reconoce lo que acertó y vuelve a leer con la persona solo los saludos y las preguntas para detectar el lugar y el propósito."),
    "Pide a un adulto que lea la conversación del museo y anota con colores quién habla y qué datos entrega.",
    "Escribe en español qué cambia en una conversación si hablan un cliente y un vendedor, o un reportero y un entrevistado.",
)

# ---------------------------------------------------------------- clase 2: descripciones e instrucciones
DESC = "«My cousin Marta has long black hair and round glasses. She wears a yellow raincoat and carries a green backpack. She is tall and very friendly.» (hair = pelo, glasses = lentes, raincoat = impermeable, carries = lleva, backpack = mochila, tall = alta, friendly = amistosa)"
HAT = "«How to make a paper hat. First, take a rectangular sheet. Second, fold it in half. Next, fold the two top corners to the center. Then fold up the bottom edges, one on each side. Finally, put it on your head.» (sheet = hoja, fold = doblar, half = mitad, corners = esquinas, edges = bordes, head = cabeza)"
ROUTE = "«To get to the library from the school gate, go straight for two blocks. Turn left at the pharmacy. The library is on the right, next to the bakery.» (gate = portón, straight = derecho, block = cuadra, turn left = gira a la izquierda, pharmacy = farmacia, on the right = a la derecha, next to = al lado de, bakery = panadería)"

lesson(
    OA1, 2,
    "Las descripciones e instrucciones escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a encontrar las pistas útiles en descripciones, instrucciones y procedimientos: palabras clave, colores, medidas, direcciones y orden de los pasos. Sirve para seguir indicaciones en inglés.",
    ["Sé los colores y las partes del cuerpo en inglés.", "Conozco first, second y finally."],
    [
        "Una descripción (description) dice cómo es una persona, un objeto o un lugar. Las palabras clave son los adjetivos (long, round, tall) y los sustantivos (hair, glasses). Para no perderte, anota solo dos o tres datos de cada texto. Una instrucción (instruction) dice qué hacer, y un procedimiento (procedure) ordena los pasos de una tarea completa.",
        "Las instrucciones usan verbos en forma de orden: take, fold, turn, go, put. Las palabras de secuencia first, second, next, then y finally marcan el orden de los pasos. En las direcciones, las pistas son turn left (gira a la izquierda), turn right (gira a la derecha), go straight (sigue derecho) y next to (al lado de).",
        "Cuando escuches, haz un dibujo rápido o una lista con números. Si no entiendes una palabra, busca otra pista en la misma oración: por ejemplo, en «a yellow raincoat» el color yellow te ayuda aunque no sepas qué es raincoat. Después de la primera escucha, revisa tus notas con la segunda.",
    ],
    [("description", "descripción"), ("instruction", "instrucción: qué hacer"), ("next / then", "después, luego"), ("turn left / right", "gira a la izquierda / derecha"), ("next to", "al lado de"), ("clue", "pista")],
    [
        ("Pistas en una descripción", ADULT + "«My neighbor Pablo is short and strong. He has curly red hair and a big smile. He always wears a blue cap.» (neighbor = vecino, short = bajo, strong = fuerte, curly = rizado, smile = sonrisa, cap = gorro con visera). ¿Qué dos pistas de color aparecen?", ["Busco los colores: red y blue.", "Red va con hair y blue con cap.", "Las otras palabras describen forma y tamaño."], "Pelo rojo y gorro azul"),
        ("Pasos de una instrucción", ADULT + "«To plant a seed: first, fill a pot with soil. Second, make a small hole. Third, put the seed inside. Finally, cover it and add a little water.» (seed = semilla, pot = maceta, soil = tierra, hole = hoyo, cover = cubrir). ¿Qué se hace en el tercer paso?", ["Busco la palabra third.", "Después de third dice put the seed inside.", "El tercer paso es poner la semilla adentro."], "Poner la semilla en el hoyo"),
    ],
    [
        ("Dibujar el edificio a la derecha cuando el guion dice a la izquierda.", "Se confunden left y right.", "Recuerda: left es izquierda y right es derecha; anótalo con una flecha."),
        ("Saltarse un paso porque no se entendió una palabra.", "Se pierde la secuencia.", "Anota igual el número del paso y completa la palabra en la segunda escucha."),
    ],
    [
        (ADULT + DESC + " ¿De qué color es la mochila de Marta? a) verde b) amarilla", "a) verde", "El guion dice a green backpack."),
        (ADULT + HAT + " ¿Qué palabra marca el último paso? a) finally b) next", "a) finally", "Finally indica que es el último paso."),
        (ADULT + ROUTE + " ¿Qué hay al lado de la biblioteca? a) una panadería b) una farmacia", "a) una panadería", "Dice next to the bakery."),
    ],
    [
        (ADULT + DESC + " ¿Cómo es el pelo de Marta?", "Largo y negro", "Dice long black hair."),
        (ADULT + HAT + " ¿Qué se dobla en el cuarto paso?", "Los bordes de abajo", "Then fold up the bottom edges corresponde al cuarto paso."),
        (ADULT + ROUTE + " ¿Dónde se debe girar a la izquierda?", "En la farmacia", "Dice turn left at the pharmacy."),
    ],
    [
        (ADULT + "«To find the kiosk: leave the gym, go straight for one block and turn right at the corner. The kiosk is between the bank and the florist.» (kiosk = kiosco, corner = esquina, between = entre, florist = florería). Una compañera sale del gimnasio. ¿Qué hace después de caminar una cuadra?", "Gira a la derecha en la esquina", "Dice go straight for one block and turn right at the corner."),
        (ADULT + "«My teacher is a tall woman. She has short gray hair and wears green glasses.» (woman = mujer, gray = gris). ¿Qué rasgos corresponden a esa profesora? a) pelo corto gris y lentes verdes b) pelo largo negro y lentes redondos", "a) pelo corto gris y lentes verdes", "Dice short gray hair y green glasses."),
        (ADULT + "«To make lemonade: first, squeeze two lemons. Second, add a glass of cold water. Third, mix it with a spoon. Finally, add a little sugar.» (lemonade = limonada, squeeze = exprimir, spoon = cuchara, sugar = azúcar). ¿Qué se hace después de agregar el agua?", "Se mezcla con una cuchara", "El tercer paso es mix it with a spoon."),
    ],
    [
        (DESC + " Una compañera dibujó a Marta con pelo corto y mochila roja. ¿Cuántos datos del guion contradice su dibujo?", "2", "Marta tiene pelo largo y mochila verde, no pelo corto ni mochila roja."),
        (ADULT + ROUTE + " Si alguien gira a la derecha en la farmacia, ¿llega a la biblioteca? Responde sí o no.", "No", "El guion dice turn left at the pharmacy, no right."),
    ],
    [
        ("Ordena las acciones de un procedimiento. A) «Finally, close the box.» B) «First, put the cards on the table.» C) «Next, count them.» D) «Then, put them in the box.»", "B, C, D, A", "Siguen la secuencia first, next, then y finally."),
        (ADULT + HAT + " Si solo hicieras los primeros tres pasos, ¿cuántos pasos faltan por hacer? Los pasos son first, second, next, then y finally.", "2", "Faltan then y finally."),
    ],
    [(ADULT + "«Excuse me, where is the swimming pool? Go up the stairs, turn left and walk to the end of the hall. The pool is in front of the changing rooms.» (stairs = escaleras, hall = pasillo, in front of = frente a, changing rooms = camarines). ¿Dónde está la piscina? a) frente a los camarines b) al lado de las escaleras", "a) frente a los camarines", "Dice in front of the changing rooms.")],
    [
        ("¿Qué significa «turn left»?", "Gira a la izquierda", "Left es izquierda."),
        ("¿Qué palabras de secuencia aparecen en las instrucciones del sombrero de papel?", "First, second, next, then y finally", "Marcan el orden de los pasos."),
        ("¿Qué clase de palabras son long, round y tall en una descripción?", "Adjetivos", "Dicen cómo es una persona o una cosa."),
    ],
    task("Un adulto lee dos veces estas instrucciones: «How to make a bookmark. First, cut a strip of paper. Second, write your name on one side. Next, draw a small star at the top. Finally, put the bookmark in your book.» (bookmark = marcapáginas, strip = tira, side = lado, top = parte de arriba). En tu hoja escribe una lista numerada con los cuatro pasos en español y subraya la palabra de secuencia de cada uno.", "1. Cortar una tira de papel (first). 2. Escribir tu nombre en un lado (second). 3. Dibujar una estrella arriba (next). 4. Poner el marcapáginas en el libro (finally).", ["escribe los cuatro pasos en el orden correcto", "relaciona cada paso con su palabra de secuencia", "no omite ningún dato clave"], ["lista numerada", "nota del adulto"], ["invertir el orden de los pasos", "omitir el dibujo de la estrella"], "Reconoce lo que acertó y relee solo las palabras de secuencia con la persona para reconstruir el orden."),
    "Pide a un adulto que lea de nuevo las direcciones de la biblioteca mientras dibujas el recorrido con flechas.",
    "Escribe en español tres pasos de una receta simple que conozcas y márcalos con first, next y finally.",
)

# ---------------------------------------------------------------- clase 3: narraciones y anécdotas
CAMP = "«Last summer, I went camping with my cousins. On the first night, we heard a strange noise near our tent. We were afraid, but my cousin Rafa took a flashlight and looked outside. It was only a small fox looking for food! We laughed and went back to sleep.» (last summer = el verano pasado, went camping = fui de camping, heard = oímos, strange noise = ruido extraño, tent = carpa, afraid = asustados, flashlight = linterna, fox = zorro, laughed = nos reímos)"
BUS = "«On my first day at the new school, I got on the wrong bus. The driver was kind and told me the right bus number. I arrived twenty minutes late, but my teacher smiled and said: Welcome! Today I feel more confident.» (wrong = equivocado, driver = conductor, kind = amable, right = correcto, late = tarde, confident = seguro)"
KITE = "«Last Sunday, Valentina had a problem: her kite was stuck in a tree. She tried to jump, but the tree was too tall. Then she asked the gardener for a long ladder. He helped her, and the kite was free again. Valentina said: Thank you very much!» (kite = volantín, stuck = atascado, gardener = jardinero, ladder = escalera, free = libre)"

lesson(
    OA1, 3,
    "Las anécdotas y narraciones escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé una estrategia para entender anécdotas y narraciones: escuchar la idea principal con las preguntas who, where, when y what happened, y resumirla en una oración. Sirve para contar y entender historias reales o inventadas.",
    ["Sé que first, then y finally ordenan los hechos.", "Reconozco verbos en pasado como went y took."],
    [
        "Una narración (narration) cuenta hechos en orden. Una anécdota (anecdote) es una historia breve y real que alguien cuenta sobre algo que le pasó. Las dos usan el pasado simple (simple past): went (fue), heard (oyó), took (tomó), laughed (rió). Estos verbos te avisan de que los hechos ya ocurrieron.",
        "La estrategia para comprender es preguntar: who (quién), where (dónde), when (cuándo) y what happened (qué pasó). La idea principal (main idea) es lo más importante de la historia y se puede decir en una oración. Los detalles (details) son datos menores, como la hora o los colores. Los sentimientos (feelings) aparecen en palabras como afraid (asustado), kind (amable) o confident (seguro).",
        "Para resumir, une quién + qué pasó + cómo terminó. Por ejemplo: «Rafa descubrió que el ruido era un zorro». No necesitas repetir todos los detalles. Si no entiendes una palabra, usa lo que viene después: cuando oyes «It was only a small fox» entiendes que el ruido no era peligroso.",
    ],
    [("anecdote", "anécdota: historia breve y real"), ("main idea", "idea principal"), ("detail", "detalle"), ("feeling", "sentimiento"), ("simple past", "pasado simple: acciones ya terminadas"), ("what happened", "qué pasó")],
    [
        ("Idea principal", ADULT + "«Yesterday, Joaquín lost his key. He looked in his bag and under his bed. Finally, his friend found it in the kitchen. Joaquín was relieved.» (lost = perdió, found = encontró, relieved = aliviado). ¿Cuál es la idea principal?", ["Pregunto quién: Joaquín.", "Pregunto qué pasó: perdió su llave y su amigo la encontró.", "Uno ambas cosas en una oración."], "Joaquín perdió su llave y su amigo la encontró en la cocina"),
        ("Sentimientos", ADULT + "«Last week, Camila did not get the main part in the school play. She cried in the bathroom. Then her friends gave her a hug.» (main part = papel principal, school play = obra escolar, cried = lloró, hug = abrazo). ¿Cómo se sintió Camila?", ["Busco los verbos: did not get y cried.", "Cried indica tristeza.", "Los abrazos muestran que sus amigos la consolaron."], "Triste"),
    ],
    [
        ("Resumir contando cada detalle en lugar de la idea principal.", "Se confunden los detalles con lo esencial.", "Responde primero quién, qué pasó y cómo terminó."),
        ("Pensar que una historia en pasado ocurre ahora.", "No se reconoce el pasado simple.", "Fíjate en verbos como went, heard y took: las acciones ya pasaron."),
    ],
    [
        (ADULT + CAMP + " ¿Dónde estaba el grupo cuando oyó el ruido? a) cerca de su carpa b) dentro de un auto", "a) cerca de su carpa", "Dice near our tent."),
        (ADULT + BUS + " ¿Cómo se sintió la persona al final? a) más segura b) más asustada", "a) más segura", "Dice Today I feel more confident."),
        (ADULT + KITE + " ¿Cuál es el problema de Valentina? a) su volantín está atascado b) perdió su mochila", "a) su volantín está atascado", "Dice her kite was stuck in a tree."),
    ],
    [
        (ADULT + CAMP + " ¿Quién tomó la linterna?", "Rafa, su primo", "Dice my cousin Rafa took a flashlight."),
        (ADULT + BUS + " ¿Cuántos minutos llegó tarde la persona?", "20", "Dice I arrived twenty minutes late."),
        (ADULT + KITE + " ¿Quién ayuda a Valentina y con qué?", "El jardinero, con una escalera larga", "Dice she asked the gardener for a long ladder."),
    ],
    [
        (ADULT + CAMP + " Elige el resumen correcto. a) Un ruido extraño era un zorro pequeño y todos se rieron b) Un zorro entró a la carpa y se comió la comida.", "a) Un ruido extraño era un zorro pequeño y todos se rieron.", "Dice it was only a small fox y we laughed; el zorro no entra."),
        (ADULT + BUS + " ¿Por qué llegó tarde la persona?", "Porque subió al bus equivocado", "Dice I got on the wrong bus."),
        (ADULT + KITE + " Valentina intentó dos cosas. ¿Cuál probó primero?", "Saltar", "Dice she tried to jump y luego she asked for a ladder."),
    ],
    [
        (ADULT + CAMP + " Una compañera dice: «Todos se asustaron y nadie miró afuera». ¿Qué parte de la anécdota la contradice?", "Rafa tomó una linterna y miró afuera", "Rafa looked outside; por lo tanto, sí alguien miró."),
        (ADULT + BUS + " ¿El conductor fue amable o malhumorado? Responde con una palabra del guion.", "kind", "El guion dice The driver was kind."),
    ],
    [
        ("Ordena las partes de la anécdota del volantín. A) Un jardinero trae una escalera. B) El volantín queda atascado en un árbol. C) El volantín vuelve a estar libre.", "B, A, C", "Primero ocurre el problema, luego llega la ayuda y al final se resuelve."),
        (ADULT + CAMP + " ¿Cuántos verbos en pasado hay en la oración «We laughed and went back to sleep»?", "2", "Son laughed y went."),
    ],
    [(ADULT + "«On Saturday, my cousin and I washed the bikes. It started to rain, so we finished inside. Our hands were cold, but we were happy.» (washed = lavamos, bikes = bicicletas, rain = lluvia, cold = frías). ¿Cuál es la idea principal? a) lavaron las bicicletas aunque llovió b) fueron al cine en bicicleta", "a) lavaron las bicicletas aunque llovió", "Cuenta qué hicieron y cómo siguió pese a la lluvia.")],
    [
        ("En inglés, ¿qué tipo de relato es una anecdote?", "Una historia breve y real", "Cuenta algo que le pasó a alguien."),
        ("¿Qué preguntas ayudan a resumir una historia?", "Quién, dónde, cuándo y qué pasó", "Son las preguntas who, where, when y what happened."),
        ("¿En qué tiempo verbal se cuentan las anécdotas?", "En pasado simple", "Hablan de hechos que ya ocurrieron."),
    ],
    task("Un adulto lee dos veces esta anécdota: «Last Sunday, Mateo made breakfast for his grandmother. He burned the toast, but he made fresh orange juice. She laughed and said: It is the best breakfast!» (breakfast = desayuno, burned = quemó, toast = tostada, fresh = recién hecho, grandmother = abuela). Escribe una oración de resumen con quién, qué pasó y cómo terminó, y un sentimiento de Mateo o de su abuela.", "Mateo preparó el desayuno para su abuela, quemó las tostadas, pero ella se rió y dijo que era el mejor. La abuela se sintió feliz.", ["resume con quién, qué pasó y cómo terminó", "nombra un sentimiento coherente", "no copia el texto entero"], ["hoja con el resumen", "nota del adulto"], ["contar solo un detalle (el jugo)", "decir que el desayuno no le gustó"], "Reconoce lo que acertó y ayuda a la persona a subrayar los tres verbos principales para armar el resumen."),
    "Pide a un adulto que lea la anécdota del bus y marca con una línea qué verbos están en pasado.",
    "Cuenta en español una anécdota breve de tu semana usando el orden: primero, luego, al final.",
)

# ---------------------------------------------------------------- clase 4: exposiciones orales y vacío de información
FAIRA = "Tarjeta A: «Science Fair. Place: the school gym. Day: Friday, the twentieth. Theme: energy.» Tarjeta B: «Time: three thirty in the afternoon. Entrance: free for students. Bring a notebook.» (fair = feria, theme = tema, entrance = entrada, free = gratis, bring = trae)"
BEES = "«Today I will talk about bees. First, bees make honey from flowers. Second, a bee visits many flowers every day and carries pollen. As a result, plants can grow fruit. Finally, bees live together in a hive. In conclusion, bees are small but very important.» (honey = miel, pollen = polen, plants = plantas, fruit = fruta, hive = colmena, in conclusion = en conclusión)"
RECYCLE = "«Good afternoon. My topic is recycling at school. Our school uses three colored bins: blue for paper, yellow for plastic and green for glass. Last month, the students recycled forty kilos of paper. Now, my question is: what can we do to recycle more?» (recycling = reciclaje, bins = basureros, paper = papel, plastic = plástico, glass = vidrio, kilos = kilos)"

lesson(
    OA1, 4,
    "Las exposiciones y tarjetas A y B escritas en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a comprender exposiciones orales y a completar información que me falta usando datos de otra persona (vacío de información). Sirve para escuchar charlas y trabajar en parejas, porque cada uno tiene una parte de los datos.",
    ["Sé hacer preguntas con where, when y what time.", "Conozco palabras como first, finally y because."],
    [
        "Una exposición oral (talk o presentation) es una charla breve para informar a un público. Casi siempre tiene tres partes: introducción (introduction), que dice el tema; desarrollo (body), con las ideas ordenadas con first, second y finally; y conclusión (conclusion), que cierra el tema. Tu trabajo como oyente es detectar el tema y las ideas principales.",
        "Un vacío de información (information gap) ocurre cuando cada persona tiene solo una parte de los datos. Para completar, hay que preguntar y escuchar. Las preguntas útiles son: Where is it?, When is it?, What time does it start? y How much is it? Quien responde debe repetir los datos exactos, y quien pregunta debe anotarlos.",
        "Una buena estrategia es copiar la tabla con espacios vacíos y completarla mientras escuchas. Si no entiendes un dato, pide ayuda con expresiones como «Could you repeat that, please?» (¿puedes repetir?) o «Do you mean…?» (¿quieres decir…?). Al final, revisa si tu tabla quedó completa y si los datos de los dos coinciden.",
    ],
    [("talk", "charla o exposición"), ("introduction", "introducción: presenta el tema"), ("conclusion", "conclusión: cierra el tema"), ("information gap", "vacío de información: cada uno tiene una parte"), ("Could you repeat that?", "¿Puedes repetir eso?"), ("Do you mean…?", "¿Quieres decir…?")],
    [
        ("Completar datos con dos tarjetas", "Tarjeta A: «Pottery workshop. Place: Room 5. Day: Monday.» Tarjeta B: «Time: five o'clock. Price: three thousand pesos. Bring an apron.» (workshop = taller, price = precio, apron = delantal). ¿Dónde y a qué hora es el taller?", ["La tarjeta A tiene el lugar: Room 5.", "La tarjeta B tiene la hora: five o'clock.", "Junto los dos datos."], "En la sala 5 a las cinco"),
        ("Tema de una exposición", ADULT + "«Hello, everyone. Today I will talk about penguins. Penguins cannot fly, but they swim very fast. Some penguins live in cold places. They eat fish.» (penguins = pingüinos, fly = volar, swim = nadar, fish = pescado). ¿Cuál es el tema de la exposición?", ["Busco la frase I will talk about.", "Dice penguins.", "El resto son datos sobre ellos."], "Los pingüinos"),
    ],
    [
        ("Responder con la información de una sola tarjeta.", "Se olvida que cada tarjeta tiene datos distintos.", "Une los datos de A y de B antes de contestar."),
        ("Pensar que la conclusión repite todos los datos.", "No se distingue la función de cada parte.", "La conclusión cierra el tema con una idea breve."),
    ],
    [
        (ADULT + BEES + " ¿Cuál es el tema de la exposición? a) las abejas b) las hormigas", "a) las abejas", "Dice Today I will talk about bees."),
        (ADULT + RECYCLE + " ¿Qué color se usa para el papel? a) azul b) verde", "a) azul", "Dice blue for paper."),
        (FAIRA + " ¿En qué día es la feria? a) el viernes veinte b) el lunes cinco", "a) el viernes veinte", "La tarjeta A dice Friday, the twentieth."),
    ],
    [
        (ADULT + BEES + " ¿Cómo ayudan las abejas a las plantas?", "Llevan polen de flor en flor", "Dice a bee carries pollen and plants can grow fruit."),
        (ADULT + RECYCLE + " ¿Cuántos kilos de papel reciclaron los estudiantes el mes pasado?", "40", "Dice forty kilos of paper."),
        (FAIRA + " ¿Qué debe llevar cada estudiante?", "Un cuaderno", "La tarjeta B dice Bring a notebook."),
    ],
    [
        (FAIRA + " Une los datos de A y B: ¿dónde y a qué hora empieza la feria?", "En el gimnasio del colegio a las tres y media de la tarde", "El lugar viene en A y la hora en B."),
        (FAIRA + " ¿Qué pregunta debe hacer la persona que tiene solo la tarjeta A para saber cuánto cuesta entrar? a) «How much is the entrance?» b) «Where is the gym?»", "a) How much is the entrance?", "La tarjeta B tiene el dato de la entrada; la pregunta pide el precio."),
        (ADULT + BEES + " ¿Qué parte de la exposición comienza con «In conclusion»? a) la conclusión b) la introducción", "a) la conclusión", "Esa expresión cierra el tema."),
    ],
    [
        (ADULT + RECYCLE + " ¿Con qué cierra la exposición? a) con una pregunta para el público b) con un chiste", "a) con una pregunta para el público", "Termina con my question is: what can we do to recycle more?"),
        (FAIRA + " Un compañero dice que la feria cuesta dinero. ¿Tiene razón? Responde sí o no.", "No", "La tarjeta B dice free for students."),
    ],
    [
        (ADULT + RECYCLE + " Si 40 kilos de papel se reparten en 8 cursos por igual, ¿cuántos kilos reciclaría cada curso?", "5", "Se reparte la misma cantidad entre ocho cursos.", "40//8"),
        ("Ordena las partes de la exposición de las abejas. A) Introducción: Today I will talk about bees. B) Conclusión: Bees are small but very important. C) Desarrollo: Bees make honey from flowers.", "A, C, B", "Primero se presenta el tema, luego se desarrolla y al final se cierra."),
    ],
    [(ADULT + "«Good morning. Our class will sell juice at the school party. The juice costs five hundred pesos per glass. We need money for a trip.» (sell = vender, party = fiesta, per glass = por vaso, trip = paseo). ¿Para qué quiere dinero el curso? a) para un paseo b) para comprar libros", "a) para un paseo", "Dice We need money for a trip.")],
    [
        ("Al escuchar una talk en inglés, ¿cuáles son sus tres partes?", "Introducción, desarrollo y conclusión", "Organizan una charla."),
        ("¿Qué se dice para pedir que repitan un dato?", "Could you repeat that, please?", "Es una expresión para clarificar."),
        ("¿Qué es un vacío de información?", "Cuando cada persona tiene solo una parte de los datos", "Hay que preguntar para completarla."),
    ],
    task("Trabaja con una persona de tu casa. Tarjeta A: «Movie night. Place: school library. Day: Thursday.» Tarjeta B: «Time: six o'clock. Bring a cushion. Popcorn is free.» (movie night = noche de cine, cushion = cojín, popcorn = cabritas). Una persona lee solo la tarjeta A y la otra solo la B. Hagan estas preguntas en inglés: Where is it? What time is it? What do I bring? Anota las respuestas en una tabla de tres columnas: lugar, hora y qué llevar.", "Lugar: biblioteca del colegio, el jueves. Hora: seis. Llevar: un cojín. Las cabritas son gratis.", ["hace las preguntas en inglés", "completa la tabla con los tres datos correctos", "pide repetir un dato si no lo entiende"], ["tabla completa", "nota de la persona que ayudó"], ["responder usando solo su tarjeta", "no anotar la hora"], "Reconoce lo que acertó y repasa con la persona qué tarjeta tenía cada dato para volver a hacer las preguntas."),
    "Pide a un adulto que lea de nuevo la exposición de las abejas y marca las tres partes con tres colores.",
    "Escribe en español una exposición de cuatro oraciones sobre un animal, con introducción, desarrollo y conclusión.",
)

# ---------------------------------------------------------------- clase 5: canciones originales y comunicación autónoma
SONG1 = "«Verse: In the morning, I walk to school. The sun is warm and the air is cool. My friends are waiting at the gate. We're early today, we're not late! Chorus: Walk, walk, walk with me, one, two, three. Sing, sing, sing with me, happy as can be!» (walk = caminar, warm = tibio, cool = fresco, waiting = esperando, gate = portón, early = temprano, happy as can be = muy feliz)"
SONG2 = "«Verse: The rain is falling on my window. The street is quiet, the sky is gray. I miss the summer and the beach, I wish tomorrow was a better day. Chorus: Rain, rain, go away, I want to play, I want to play.» (falling = cayendo, quiet = silenciosa, gray = gris, miss = extrañar, beach = playa, wish = desear, better = mejor, go away = vete)"
TALK = "«Hello, I am Rocío. I want to tell you about my dog, Toby. He is a brown dog with short legs. Every day, he waits for me at the door. When I arrive, he jumps and barks happily. I love him because he is loyal.» (tell = contar, short legs = patas cortas, waits = espera, door = puerta, barks = ladra, happily = felizmente, loyal = leal)"

lesson(
    OA1, 5,
    "Las canciones y relatos originales escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a entender una canción y un relato oral por mi cuenta: el tema, el ánimo, las rimas y la estructura (verso y coro). Sirve para disfrutar canciones en inglés y contar con mis palabras de qué se tratan.",
    ["Sé que una canción tiene versos y un coro que se repite.", "Conozco palabras de sentimientos como happy, sad y afraid."],
    [
        "Una canción (song) se divide en versos (verses) y en un coro (chorus). El coro se repite y resume la emoción principal. Para comprender una canción, pregunta por el tema (theme), que es de qué trata, y por el ánimo o estado de ánimo (mood), que es cómo se siente. Las palabras clave dan ese ánimo: happy, early y sing muestran alegría; rain, gray y miss muestran nostalgia.",
        "Para entender por tu cuenta, usa esta rutina: primero escucha entera y piensa en una palabra para el ánimo; después busca dos palabras clave que lo prueben; por último, resume el tema con una oración. Si una palabra no se entiende, apóyate en la rima y en las palabras que se repiten, como «walk» o «rain».",
        "Esta rutina sirve también para un relato (como el de una mascota): escucha quién habla, a quién describe, qué hace cada día y por qué lo quiere. Siempre puedes explicar tu comprensión con una frase corta: «The song is about… because…» (La canción trata de… porque…).",
    ],
    [("song", "canción"), ("verse", "verso: estrofa"), ("chorus", "coro: parte que se repite"), ("theme", "tema: de qué trata"), ("mood", "ánimo: cómo se siente el texto"), ("because", "porque")],
    [
        ("Tema y ánimo", ADULT + "«I plant a tree, I give it water. I watch it grow, taller and taller. One day the birds will come to stay. It is my gift for a better day.» (plant = plantar, grow = crecer, taller = más alto, gift = regalo). ¿De qué trata y cómo se siente?", ["Busco palabras clave: plant, water, grow, gift.", "Todas hablan de cuidar un árbol.", "El ánimo es esperanzador por better day."], "Trata de cuidar un árbol; el ánimo es esperanzado"),
        ("Rima", "En estos versos: «Close the door, don't make a sound. The night is deep and the moon is round.» (door = puerta, round = redonda). ¿Qué palabra rima con sound?", ["Miro las palabras finales de cada verso: sound y round.", "Las dos terminan con el mismo sonido.", "Night y moon no están al final."], "round"),
    ],
    [
        ("Pensar que la canción es alegre solo porque tiene coro.", "El coro no define el ánimo.", "Mira las palabras clave: rain, gray y miss indican nostalgia."),
        ("Traducir palabra por palabra y perder la idea de la canción.", "Se pierde el sentido global.", "Busca el tema con dos palabras clave y el coro."),
    ],
    [
        (ADULT + SONG1 + " ¿Cómo se siente la canción? a) alegre b) triste", "a) alegre", "Happy, early y sing muestran alegría."),
        (ADULT + SONG2 + " ¿Qué clima hay? a) lluvioso b) soleado", "a) lluvioso", "Dice the rain is falling."),
        (ADULT + TALK + " ¿De quién habla Rocío? a) de su perro Toby b) de su gato", "a) de su perro Toby", "Dice my dog, Toby."),
    ],
    [
        (ADULT + SONG1 + " ¿Quién espera en el portón?", "Los amigos", "Dice My friends are waiting at the gate."),
        (ADULT + SONG2 + " ¿Qué extraña quien canta?", "El verano y la playa", "Dice I miss the summer and the beach."),
        (ADULT + TALK + " ¿Qué hace Toby cuando Rocío llega? a) salta y ladra b) duerme", "a) salta y ladra", "Dice he jumps and barks happily."),
    ],
    [
        (ADULT + SONG1 + " ¿Qué palabras del coro se repiten tres veces seguidas? a) walk y sing b) happy y early", "a) walk y sing", "Cada una aparece tres veces en su línea del coro."),
        (ADULT + SONG2 + " ¿Qué dos palabras riman al final de las líneas? a) day y gray b) beach y window", "a) day y gray", "Terminan con el mismo sonido."),
        (ADULT + TALK + " ¿Por qué Rocío quiere a Toby?", "Porque es leal", "Dice I love him because he is loyal."),
    ],
    [
        (ADULT + SONG2 + " ¿Cómo cambia el ánimo si la canción dijera «I wish tomorrow was a better day, and I smile» (smile = sonreír)? Responde con una palabra: más alegre o más triste.", "Más alegre", "Smile agrega una emoción positiva."),
        ("Una amiga dice que la canción de la lluvia es alegre porque tiene un coro. ¿Qué dos palabras del texto muestran que no? a) gray y miss b) play y chorus", "a) gray y miss", "Gray y miss expresan tristeza y nostalgia."),
    ],
    [
        (ADULT + SONG1 + " ¿Cuántas veces aparece la palabra «walk» en el coro?", "3", "El coro dice walk, walk, walk."),
        (SONG1 + " Elige el título que mejor resume esta canción. a) A Happy Walk to School b) Rain on My Window", "a) A Happy Walk to School", "Resume el tema y el ánimo alegre."),
    ],
    [(ADULT + "«Hello, I am Bruno. In my school, we have a music club. We sing songs in English every Wednesday. Last week, we learned a new chorus. I feel proud because I can sing it without the paper.» (club = club, learned = aprendimos, proud = orgulloso, without = sin). ¿Cómo se siente Bruno? a) orgulloso b) enojado", "a) orgulloso", "Dice I feel proud because I can sing it without the paper.")],
    [
        ("En una canción en inglés, ¿qué es el chorus?", "La parte que se repite", "Aparece después de cada verso."),
        ("¿Qué es el ánimo (mood) de una canción?", "Cómo se siente", "Se descubre con palabras clave."),
        ("¿Qué frase sirve para decir de qué trata una canción?", "The song is about…", "Es una fórmula para explicar el tema."),
    ],
    task("Un adulto lee dos veces esta canción original: «Verse: The bus is yellow, the road is long. We laugh and clap and sing a song. Chorus: Hey, hey, we're on our way, it's a beautiful, beautiful day!» (road = camino, laugh = reír, clap = aplaudir, on our way = en camino, beautiful = hermoso). En tu hoja escribe: el tema, el ánimo, dos palabras clave que lo muestran y la rima del primer verso.", "Tema: un viaje en bus. Ánimo: alegre. Palabras clave: laugh y beautiful. Rima: long con song.", ["indica el tema y el ánimo", "escribe dos palabras clave del texto", "encuentra la rima"], ["hoja con respuestas", "nota del adulto"], ["decir que es triste", "usar palabras que no están en el texto"], "Reconoce lo que acertó y vuelve a leer solo las palabras finales de cada verso para encontrar la rima."),
    "Pide a un adulto que lea la canción de la lluvia y escribe una palabra que describa su ánimo.",
    "Escribe en español dos oraciones sobre qué emoción te produce la canción del camino al colegio y por qué.",
)
