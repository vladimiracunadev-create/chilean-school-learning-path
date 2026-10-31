"""Cuaderno del estudiante, 7.º básico Inglés (propuesta): EN07 OA 11, escritura breve según género, modelo y criterio.

Todos los textos en inglés son originales y breves, con pista en español. El modelo y los criterios de cada género están
escritos dentro de la propia clase. Sin audio ni material externo. Los títulos de clase del plan son genéricos
(propósito, pistas, estrategia, brecha de información, comunicación independiente): aquí se aplican a la escritura de un
género por clase (correo, descripción, tira cómica, folleto y noticia, rima y cuento).
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA11 = "EN07 OA 11"


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


# ================================================================ OA 11 clase 1: propósito, audiencia y modelo (correo electrónico)
lesson(
    OA11, 1,
    "Los modelos y listas de criterios escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir un correo electrónico corto siguiendo un modelo y una lista de criterios. Sirve para que un mensaje en inglés se entienda y sea adecuado para quien lo lee.",
    ["Sé escribir oraciones simples en inglés, como I can come on Monday.", "Conozco because (porque) y can (poder)."],
    [
        "Un correo electrónico (email) tiene partes fijas: el asunto (subject, lo que dice de qué trata), el saludo (greeting), el mensaje (body) y la despedida (closing) con tu nombre. Modelo: «Subject: Party. Hi Tom, thanks for your message. I can come on Saturday at 4 p.m. Can I bring a cake? See you soon, Ana».",
        "Antes de escribir, piensa en el propósito (purpose, para qué escribes: invitar, pedir, agradecer, disculparte) y en la audiencia (audience, quién lo va a leer). A un amigo le escribes Hi Tom, y cierras con See you soon. A una profesora le escribes Dear Ms. Rojas, y cierras con Best wishes o Thank you.",
        "Un criterio de evaluación (criterion) es una condición que tu texto debe cumplir. Para un correo corto usaremos tres: 1) saludo que calza con la audiencia, 2) un propósito claro con los datos que el lector necesita (día, hora, lugar), 3) despedida y nombre. Al terminar, revisa tu texto contra cada criterio, uno por uno.",
    ],
    [("email", "correo electrónico"), ("subject", "asunto: de qué trata el correo"), ("greeting", "saludo: Hi Tom, / Dear Ms. Rojas,"), ("closing", "despedida: See you soon, / Best wishes,"), ("purpose", "propósito: para qué escribes"), ("audience", "audiencia: quién lee tu texto"), ("criterion", "criterio: condición que el texto debe cumplir"), ("Dear", "Estimado/a (saludo más formal)")],
    [
        ("Reconocer las partes del modelo", "Texto: «Subject: Party. Hi Tom, thanks for your message. I can come on Saturday at 4 p.m. Can I bring a cake? See you soon, Ana». ¿Cuál es la despedida?", ["Busca la línea final, antes del nombre.", "La despedida es la frase que cierra el mensaje.", "Esa frase es See you soon."], "See you soon"),
        ("Elegir un saludo según la audiencia", "Vas a escribirle a tu profesor de Música, el Sr. Vera, para pedir una partitura. ¿Qué saludo usas? Opciones: Dear Mr. Vera, / Hi buddy,", ["La audiencia es un profesor.", "A un profesor se le escribe con un saludo más formal.", "El saludo adecuado es Dear Mr. Vera,"], "Dear Mr. Vera,"),
    ],
    [
        ("Escribir Hi buddy, a una persona adulta que no es de confianza.", "Se usa el mismo saludo para todos.", "Mira la audiencia: con adultos o autoridades usa Dear y el apellido."),
        ("Escribir «Come to my party» sin día ni hora.", "Se olvida que el lector necesita los datos para responder.", "Revisa el criterio 2: agrega día, hora y lugar."),
    ],
    [
        ("¿Qué significa «subject» en un correo electrónico?", "Asunto", "Es la línea que dice de qué trata el correo."),
        ("Correo: «Hi Mia, I can't come on Friday because I have a cold. Best wishes, Leo». ¿Cuál es el saludo?", "Hi Mia,", "El saludo es la primera línea, antes del mensaje."),
        ("¿Cuál de estas es una despedida? a) Best wishes, b) Dear Ms. Rojas,", "a", "Best wishes cierra el correo; Dear Ms. Rojas abre el correo como saludo."),
    ],
    [
        ("Ordena las líneas de un correo. a) Best wishes, Lena b) Hi Pablo, c) I can help you on Tuesday. Escribe las letras en orden.", "b, c, a", "Primero va el saludo, luego el mensaje y al final la despedida con el nombre."),
        ("Correo: «Dear Mr. Silva, can I borrow the book until Monday? Thank you, Paula». ¿Cuál es el propósito? a) Pedir un libro prestado b) Disculparse por llegar tarde", "a", "Paula pregunta si puede pedir prestado el libro hasta el lunes."),
        ("Criterios: 1) saludo, 2) propósito con datos, 3) despedida y nombre. Texto: «Hi Tom, I can come on Saturday at 4 p.m.». ¿Qué criterio no se cumple?", "3", "No tiene frase de despedida ni nombre."),
    ],
    [
        ("Completa la despedida: «Thanks for your help. ___, Leo». Opciones: Best wishes / Dear.", "Best wishes", "Dear se usa al comenzar; Best wishes sirve para cerrar."),
        ("Completa con una razón: «I can't go to the park ___ I have a cold.» Opciones: because / but.", "because", "La segunda parte explica la razón por la que no puede ir."),
        ("Escribirás una invitación a tu mejor amigo. ¿Qué primera oración calza con la audiencia? a) Do you want to come to my house on Sunday? b) I am writing to inform you about a formal meeting.", "a", "Es una pregunta cercana y simple, adecuada para un amigo."),
    ],
    [
        ("Correo a la directora: «Hey! Can I use the gym on Friday at 4 p.m.? Thanks, Leo». Criterios: 1) saludo que calza con la audiencia, 2) propósito claro con datos, 3) despedida y nombre. ¿Qué criterio no se cumple?", "1", "El propósito tiene día y hora y la despedida tiene nombre, pero Hey! no es un saludo adecuado para una directora."),
        ("La invitación de Ana dice: «Party on Saturday at 5 p.m.». Tom quiere llegar justo al comienzo. ¿Qué hora debe escribir Tom en su respuesta?", "5 p.m.", "La invitación fija el comienzo a las 5 p.m."),
    ],
    [
        ("Ordena las partes de este correo. a) Best wishes, Mia b) Subject: Science project c) Dear Mr. Vega, d) Can we meet on Tuesday at 10 a.m.? Escribe las letras en orden.", "b, c, d, a", "Va primero el asunto, luego el saludo, el mensaje y la despedida con el nombre."),
        ("Mensaje: «Hi Leo, my party is at my house. Can you come?». ¿Qué dos datos necesita Leo para poder responder? (Escribe los dos en el orden en que aparecen en el modelo de la clase.)", "día y hora", "El mensaje no dice cuándo es la fiesta ni a qué hora empieza."),
    ],
    [("Tu curso arma un club de reciclaje. Le escribes a la profesora Reyes para pedir una reunión. ¿Qué texto cumple mejor los tres criterios? a) «Dear Ms. Reyes, can we meet on Monday at 2 p.m. to plan the recycling club? Thank you, Sofia» b) «Ms. Reyes, I want a meeting. Sofia»", "a", "Tiene saludo formal, propósito con día y hora, y despedida con nombre.")],
    [
        ("¿Qué es la audiencia de un texto?", "Quién lo va a leer", "Define el tono del saludo y de la despedida."),
        ("¿Qué significa «Dear» al comienzo de un correo?", "Estimado/a", "Es un saludo más formal."),
        ("¿Cuántos criterios usamos para revisar el correo corto?", "3", "Saludo, propósito claro con datos y despedida con nombre."),
    ],
    task("Lee este encargo: tu amigo Max te invitó a su cumpleaños el sábado 14 a las 3 p.m. en su casa, y tú sí puedes ir. Escribe en una hoja un correo de respuesta con asunto, saludo, mensaje y despedida con tu nombre. Revisa tu correo con los tres criterios de la clase y marca cada uno con una cruz.", "Subject: Your birthday. Hi Max, thanks for the invitation. I can come on Saturday 14 at 3 p.m. Can I bring a game? See you soon, Nico.", ["tiene asunto, saludo, mensaje y despedida con nombre", "el saludo calza con un amigo", "confirma día y hora con datos correctos"], ["hoja con el correo y los tres criterios marcados"], ["omitir la despedida", "olvidar el día o la hora"], "Pide que cambie el correo para la profesora jefe en vez de Max y que diga qué partes cambió y por qué."),
    "Copia el modelo de correo de la explicación y subraya con un color el saludo, el mensaje y la despedida.",
    "Escribe dos versiones de un mismo mensaje de agradecimiento: una para un amigo y otra para una profesora.",
)

# ================================================================ OA 11 clase 2: pistas del modelo (descripción)
lesson(
    OA11, 2,
    "Las descripciones modelo y las listas de criterios escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir una descripción corta de una persona usando un modelo y criterios. Sirve para que otra persona pueda imaginar a quien describo.",
    ["Conozco adjetivos como tall, short, funny y kind.", "Sé que en inglés se dice He is… y He has…"],
    [
        "Una descripción cuenta cómo es una persona, un lugar o un objeto. Un modelo ayuda a ver su orden. Modelo: «My cousin Nico is 13. He is tall and thin. He has short black hair and brown eyes. He is funny and kind». Primero va quién es y su edad, luego el aspecto físico y al final la personalidad.",
        "Fíjate en las pistas de lenguaje del modelo. Para estado y cualidades se usa is (He is tall). Para lo que se tiene se usa has (He has short hair). Con I, you, we y they se usa have: I have brown eyes. Los adjetivos (tall, thin, funny) describen y van después de is.",
        "Los criterios de esta descripción son cuatro: 1) dice quién es y su edad, 2) da al menos dos datos del aspecto (pelo, ojos, estatura), 3) incluye al menos una cualidad de personalidad, 4) usa bien is y has. Con ellos puedes revisar tu texto o el de otra persona y decir con claridad qué falta.",
    ],
    [("description", "descripción"), ("tall / short", "alto / bajo"), ("thin", "delgado"), ("hair", "pelo"), ("eyes", "ojos"), ("funny", "divertido"), ("kind", "amable"), ("has / have", "tiene / tengo, tienen"), ("friendly / shy / generous", "amistosa / tímida / generosa")],
    [
        ("Reconocer las pistas del modelo", "Modelo: «My cousin Nico is 13. He is tall and thin. He has short black hair and brown eyes. He is funny and kind». ¿Qué dato de aspecto dice sobre su pelo?", ["Busca la oración con hair.", "Dice He has short black hair.", "El pelo es corto y negro."], "short black hair"),
        ("Corregir con el criterio 4", "Una compañera escribió «My friend Eva have long hair». ¿Cómo se corrige?", ["El sujeto es My friend, que equivale a she.", "Con she se usa has, no have.", "Queda: My friend Eva has long hair."], "My friend Eva has long hair."),
    ],
    [
        ("Escribir «She have brown eyes».", "Se usa have con todos los sujetos.", "Con he, she e it se usa has: She has brown eyes."),
        ("Describir solo el aspecto físico.", "Se olvida que el criterio 3 pide una cualidad de personalidad.", "Agrega una oración con is, por ejemplo She is kind."),
    ],
    [
        ("¿Qué significa «kind»?", "Amable", "Describe a una persona que trata bien a los demás."),
        ("Completa: «He ___ short hair.» Opciones: has / is.", "has", "Lo que se tiene (pelo) va con has."),
        ("Completa: «My teacher ___ tall.» Opciones: is / has.", "is", "Una cualidad como tall va con is."),
    ],
    [
        ("Descripción: «Lucy is 11. She has long red hair and green eyes. She is shy». ¿Cuál es la cualidad de personalidad? (shy = tímida)", "shy", "Es la única palabra que habla de cómo es ella y no de su aspecto."),
        ("Descripción: «Pedro is 12. He is short. He has curly hair». Criterio 3: ¿la descripción cumple con él? Responde sí o no. (curly = rizado)", "No", "Todas las oraciones hablan del aspecto y no hay una cualidad de personalidad."),
        ("Une: Lucy ___ a good friend. / Lucy ___ blue eyes. Opciones para completar en orden: a) is, has b) has, is", "a", "Una cualidad lleva is y lo que se tiene lleva has."),
    ],
    [
        ("Completa: «I ___ brown eyes.» Opciones: have / has.", "have", "Con I se usa have."),
        ("Completa: «My sister ___ funny.» Opciones: is / has.", "is", "Funny es una cualidad y lleva is."),
        ("Escribe una oración de aspecto sobre Ana usando has y estos datos: long black hair. (Escribe la oración completa.)", "Ana has long black hair.", "Con Ana (she) se usa has y después los datos del pelo."),
    ],
    [
        ("Descripción: «Omar is 12. He is tall. He has short hair and glasses. He is funny». Se usan cuatro criterios. ¿Cuántos cumple? (glasses = lentes)", "4", "Dice quién es y su edad, da aspecto, incluye una cualidad y usa bien is y has."),
        ("Una compañera dice que «Tom has kind» está correcta. ¿Tiene razón? Responde sí o no.", "No", "Kind es una cualidad y lleva is: Tom is kind."),
    ],
    [
        ("Descripción: «Mia is 12. She is tall. She has two long braids». ¿Qué criterio falta? (braids = trenzas) a) criterio 1, quién es y su edad b) criterio 3, una cualidad de personalidad", "b", "Sí dice quién es y su edad, pero ninguna oración habla de su personalidad."),
        ("Ordena el texto. a) She is friendly. b) Rita is 12. c) She has short brown hair. Escribe las letras en orden.", "b, c, a", "Primero va quién es, luego el aspecto y al final la personalidad."),
    ],
    [("Tu curso arma un cartel para buscar al «mejor compañero del mes» y tienes que describir a Daniela, de 13 años, que es alta, tiene pelo largo y es generosa. ¿Qué descripción cumple los cuatro criterios? a) «Daniela is 13. She is tall. She has long hair. She is generous.» b) «Daniela is nice. She tall. She have long hair.»", "a", "La primera dice la edad, el aspecto, la personalidad y usa bien is y has.")],
    [
        ("¿En qué orden va una descripción modelo?", "Quién es, aspecto y personalidad", "Así el lector imagina a la persona de lo general a lo particular."),
        ("Quieres decir que ella tiene pelo largo: She ___ long hair. ¿Qué verbo va en el espacio? Opciones: has / have.", "has", "Para tener se usa has con he, she o it."),
        ("¿Cuántos criterios se usan para esta descripción?", "4", "Quién es, aspecto, personalidad y uso de is y has."),
    ],
    task("Lee este encargo: describe a un compañero o a una persona famosa que conozcas (sin escribir apellidos ni datos privados). Escribe en tu hoja una descripción de cuatro a seis oraciones. Usa el modelo de la clase y marca en tu texto, con una cruz, cada uno de los cuatro criterios.", "Sara is 13. She is short and thin. She has long brown hair. She is funny and kind.", ["dice quién es y su edad", "incluye al menos dos datos de aspecto", "incluye al menos una cualidad de personalidad", "usa bien is y has"], ["hoja con la descripción y los cuatro criterios marcados"], ["usar have con she o he", "olvidar la personalidad"], "Pide que cambie un adjetivo del aspecto por otro más preciso y que explique si el texto sigue cumpliendo los criterios."),
    "Copia el modelo de Nico y reemplaza cada adjetivo por otro de la lista de palabras importantes.",
    "Escribe una descripción de tu habitación en cinco oraciones usando is y has, y revísala con los criterios.",
)

# ================================================================ OA 11 clase 3: estrategia con recursos multimodales (tira cómica)
lesson(
    OA11, 3,
    "Las descripciones de viñetas y los globos de diálogo escritos en cada ejercicio, lápiz, una hoja y colores.",
    "Aprenderé a escribir una tira cómica corta combinando imagen y texto. Sirve para contar algo de forma creativa con pocas palabras.",
    ["Sé escribir oraciones cortas en inglés.", "Conozco signos como ? y !."],
    [
        "Una tira cómica (comic strip) cuenta una historia en varias viñetas (panels). Cada viñeta tiene una imagen y un texto corto. El texto puede estar en un globo de diálogo (speech bubble), que muestra lo que dice un personaje, o en un cuadro de texto (caption), que cuenta lo que pasa. Un recurso multimodal es cualquier medio que apoya el mensaje además de las palabras: dibujo, color, tamaño de letra.",
        "Una buena estrategia es que la imagen muestre y el texto agregue. Si el dibujo ya muestra lluvia, el globo no necesita decir solo It is rain; puede decir It's raining! Where is my umbrella? También hay palabras de sonido (sound words), como Splash! (salpicadura), Boom! (explosión) y Ring! (timbre). Se escriben con letras grandes para que se «oigan».",
        "Los criterios de esta tira son: 1) tres viñetas con una idea cada una, 2) no más de ocho palabras por globo, 3) al menos una palabra de sonido, 4) los signos ? o ! donde corresponden. Planifica primero qué muestra cada dibujo y después escribe el texto.",
    ],
    [("comic strip", "tira cómica"), ("panel", "viñeta"), ("speech bubble", "globo de diálogo: lo que dice un personaje"), ("caption", "cuadro de texto que cuenta lo que pasa"), ("sound word", "palabra de sonido: Splash!, Boom!"), ("It's raining!", "¡Está lloviendo!"), ("umbrella", "paraguas")],
    [
        ("Elegir el texto que agrega información", "Viñeta: dibujo de una niña con un paraguas bajo la lluvia. ¿Qué globo agrega más? Opciones: «It's raining! Where is my hat?» / «A girl and an umbrella».", ["El dibujo ya muestra la lluvia y el paraguas.", "El texto debe aportar algo nuevo.", "El primer globo agrega que busca su gorro."], "It's raining! Where is my hat?"),
        ("Revisar con el criterio 3", "Una tira de tres viñetas tiene los textos «Hello!», «Look at that!» y «Goodbye!». ¿Cumple el criterio 3, una palabra de sonido? ", ["Busca palabras como Splash!, Boom! o Ring!", "Ninguno de los tres textos es un sonido.", "No cumple."], "No"),
    ],
    [
        ("Escribir en el globo lo que ya muestra el dibujo.", "Se piensa que el texto debe repetir la imagen.", "Deja que la imagen muestre y que el texto agregue un dato nuevo."),
        ("Poner párrafos largos en cada globo.", "Se escribe como en una redacción.", "Escribe ocho palabras o menos y una sola idea por viñeta."),
    ],
    [
        ("¿Qué es un globo de diálogo (speech bubble)?", "El lugar donde se escribe lo que dice un personaje", "Muestra la voz del personaje."),
        ("¿Cuál de estas es una palabra de sonido? Opciones: Splash! / Umbrella", "Splash!", "Imita un ruido, en este caso el agua."),
        ("¿Cuántas viñetas pide el criterio 1?", "3", "Cada viñeta tiene una idea y son tres en total."),
    ],
    [
        ("Viñeta 1: un niño mira el cielo gris. ¿Qué globo agrega más? a) «Oh no! We can't play outside!» b) «A boy looks at the sky.»", "a", "El globo agrega un dato nuevo (no podrán jugar afuera); b solo repite el dibujo."),
        ("Globo: «Where is my phone?!». ¿Qué cuadro de texto lo acompañaría? a) caption: «Ana looks in her bag.» b) caption: «Ana sleeps.»", "a", "Buscar el teléfono calza con mirar en la mochila."),
        ("Texto: «Can we go to the park today with the dog and my sister?» ¿Cumple el criterio 2, ocho palabras o menos? Responde sí o no.", "No", "Tiene 13 palabras, más que el límite de ocho."),
    ],
    [
        ("Viñeta: dibujo de un perro que salta a un charco. Escribe la palabra de sonido que usarías. Opciones: Splash! / Ring!", "Splash!", "Un salto en agua se imita con Splash!"),
        ("Completa el globo de una persona que se asusta: «Look out___» Elige el signo. Opciones: ! / ?", "!", "El signo ! muestra una advertencia o una emoción fuerte."),
        ("Completa el globo con signo correcto: «Do you have an umbrella___» Opciones: ? / !", "?", "Es una pregunta, así que lleva ?"),
    ],
    [
        ("Tira de tres viñetas: 1) «Boom!» 2) «Wow, that was loud!» 3) «Is everyone OK?» ¿Cuántos criterios cumple de estos: tres viñetas, ocho palabras o menos por globo, una palabra de sonido, ? o ! donde corresponde?", "4", "Cumple los cuatro: hay tres viñetas, ninguno pasa de ocho palabras, Boom! es un sonido y hay ! y ?"),
        ("Un compañero dice que repetir con palabras lo que ya muestra el dibujo es lo ideal. ¿Tiene razón? Responde sí o no.", "No", "El texto debe agregar información que el dibujo no muestra."),
    ],
    [
        ("Ordena una mini historia en tres viñetas. a) «Ring!» (suena el timbre) b) «Lunch time!» (los niños salen) c) «I am hungry!» (un niño mira su reloj) Escribe las letras en orden lógico.", "c, a, b", "Primero siente hambre, luego suena el timbre y al final salen a almorzar."),
        ("Viñeta: un niño con una pelota rota. ¿Qué texto agrega un problema sin repetir el dibujo? a) «Oh no! Now we can't play!» b) «A boy with a ball.»", "a", "El globo cuenta cómo se siente y qué problema nuevo aparece."),
    ],
    [("Te piden una tira de tres viñetas para el diario mural sobre cuidar el agua. Viñeta 1: un grifo gotea. Viñeta 2: una niña lo cierra. Viñeta 3: la niña sonríe. ¿Qué texto del primer globo cumple los criterios? a) «Drip, drip! Water is on!» b) «There is a tap that is leaking water in the school kitchen every day.»", "a", "Tiene una palabra de sonido, es corto y apoya el dibujo.")],
    [
        ("¿Qué es un recurso multimodal?", "Cualquier medio que apoya el mensaje además de las palabras", "Por ejemplo el dibujo, el color o el tamaño de letra."),
        ("¿Cuántas palabras como máximo debe tener un globo en esta tira?", "8", "Es el límite del criterio 2."),
        ("¿Qué signo lleva una pregunta?", "?", "Las preguntas terminan con signo de interrogación."),
    ],
    task("Lee este encargo: dibuja una tira cómica de tres viñetas en tu hoja con esta historia: 1) Dos niños esperan el bus bajo la lluvia. 2) El bus pasa y salpica un charco. 3) Los niños quedan mojados y se ríen. Escribe en cada viñeta un globo o un cuadro de texto en inglés. Revisa tu tira con los cuatro criterios de la clase.", "Panel 1: «Where is the bus?» Panel 2: «Splash!» Panel 3: «We are wet! Ha, ha!»", ["tres viñetas con una idea cada una", "máximo ocho palabras por globo", "usa una palabra de sonido", "usa ? y ! donde corresponde"], ["hoja con tres viñetas dibujadas y escritas"], ["repetir con palabras el dibujo", "globos demasiado largos"], "Pregunta qué dato nuevo agrega cada texto que el dibujo no muestra."),
    "Copia la tira del criterio y subraya la palabra de sonido y los signos ? y !.",
    "Crea una cuarta viñeta que cierre la historia con un giro divertido y úsala con una caption.",
)

# ================================================================ OA 11 clase 4: brecha de información (folleto y noticia)
lesson(
    OA11, 4,
    "El folleto modelo, la noticia modelo y las listas de criterios escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir un folleto breve y una noticia corta con los datos que el lector necesita. Sirve para informar de forma clara y ordenada.",
    ["Sé escribir fechas y horas en inglés, como Saturday at 3 p.m.", "Conozco palabras como free, price y place."],
    [
        "Un folleto (brochure) invita a participar en una actividad. Tiene título (title), un eslogan corto (slogan), los datos clave (when, where, price) y una invitación con un verbo de orden: Join us! (¡Únete!), Visit… (Visita…), Come… (Ven…). Modelo: «Book Fair! Read, swap and enjoy. When: Friday, 10 a.m. Where: school library. Price: free. Join us!».",
        "Una noticia (news report) cuenta un hecho que ya pasó. Tiene un titular (headline), una primera oración que responde Who? What? Where? When? y un detalle. Suele usar pasado: won (ganó), opened (abrió), visited (visitó). Modelo: «School team wins match. The school team won the match on Friday. The score was 3 to 1».",
        "Hay una brecha de información (information gap) cuando el lector no tiene un dato que tú sí tienes. Para llenarla, piensa qué preguntas haría el lector: ¿cuándo?, ¿dónde?, ¿cuánto cuesta? Criterios del folleto: 1) título, 2) when, where y price, 3) una invitación. Criterios de la noticia: 1) titular, 2) quién, qué, dónde y cuándo, 3) un detalle.",
    ],
    [("brochure", "folleto"), ("slogan", "eslogan"), ("headline", "titular de una noticia"), ("When / Where / Price", "Cuándo / Dónde / Precio"), ("Join us!", "¡Únete a nosotros!"), ("free", "gratis"), ("won", "ganó")],
    [
        ("Encontrar el dato que falta", "Folleto: «Science Day! Learn with experiments. Where: school yard. Price: free. Join us!». ¿Qué dato clave no aparece? (Revisa when, where y price.)", ["When pide el día y la hora.", "Where está: school yard. Price está: free.", "Falta When."], "When"),
        ("Revisar una noticia con las preguntas del lector", "Texto: «Chess club wins. The chess club won the game on Saturday». ¿Qué pregunta del lector queda sin responder: Who, What, Where o When?", ["Who: the chess club. What: won the game. When: on Saturday.", "No dice dónde fue.", "Falta Where."], "Where"),
    ],
    [
        ("Poner solo el título y la invitación en un folleto.", "Se cree que con llamar la atención basta.", "Agrega when, where y price para que el lector pueda ir."),
        ("Escribir la noticia sin fecha ni lugar.", "Se olvida la brecha de información del lector.", "Responde Who?, What?, Where? y When? en la primera oración."),
    ],
    [
        ("¿Qué significa «Join us!»?", "¡Únete a nosotros!", "Es una invitación a participar."),
        ("Folleto: «Where: library. When: Monday, 4 p.m. Price: free». ¿Cuánto cuesta ir?", "Nada, es gratis", "Price: free significa que es gratis."),
        ("¿Qué es el titular (headline) de una noticia?", "El título que resume el hecho", "Va primero y atrae la atención del lector."),
    ],
    [
        ("Folleto: «Craft Fair! Make and sell. When: Sunday, 11 a.m. Where: Town square. Price: 2.000 pesos». ¿Dónde ocurre la actividad?", "En Town square", "Where indica el lugar: Town square."),
        ("Noticia: «Girls team wins. The girls team won the race on Tuesday at the park». ¿Cuándo ocurrió el hecho?", "El martes", "On Tuesday indica el día."),
        ("Un folleto tiene tres criterios: título, datos when/where/price e invitación. Texto: «Join us!». ¿Cuántos criterios cumple?", "1", "Solo cumple el de la invitación."),
    ],
    [
        ("Completa el folleto: «Movie Night! When: Friday, 7 p.m. Where: school gym. Price: free. ___ us!» Opciones: Join / Won.", "Join", "Join us! es la invitación del folleto."),
        arith("Folleto: «Concert! Price: 3.000 pesos per ticket». Una familia compra 3 entradas. ¿Cuántos pesos paga en total?", "3 * 3000", "Cada entrada cuesta lo mismo, así que se multiplica por el número de entradas.", " pesos"),
        ("Completa la primera oración de la noticia: «Class 7A ___ the quiz on Monday.» Opciones: won / win.", "won", "On Monday ya pasó, así que se usa won, el pasado de win."),
    ],
    [
        ("Un compañero escribió el folleto «Game Day! When: Friday. Where: yard. Price: free». ¿Cumple el criterio 2 (when, where y price)? Responde sí o no.", "Sí", "Los tres datos aparecen: When es Friday, Where es yard y Price es free."),
        ("Noticia: «Robot club opens. The robot club opened a new room at school». ¿Qué pregunta del lector queda sin responder, When o Who?", "When", "No dice cuándo se abrió, pero sí dice quién (robot club)."),
    ],
    [
        ("Ordena el folleto. a) Join us! b) Art Show! c) Where: school hall. When: Thursday, 5 p.m. Escribe las letras en orden.", "b, c, a", "Va primero el título, luego los datos y al final la invitación."),
        ("Titular: «Library opens new section». ¿Qué texto es mejor primera oración? a) The library opened a new section on Monday. b) Something happened at school.", "a", "Responde Who, What y When con datos claros."),
    ],
    [("Tu curso organiza una venta de pasteles el viernes a las 12 h en el patio para juntar plata para el paseo, con precio de 500 pesos cada uno. ¿Qué folleto cumple los criterios? a) «Cake Sale! When: Friday, 12 p.m. Where: school yard. Price: 500 pesos. Join us!» b) «We sell cakes. Come when you can. It is cheap.»", "a", "Da título, when, where, price e invitación; el segundo no da datos precisos.")],
    [
        ("¿Qué quiere decir «brecha de información»?", "Un dato que el lector no tiene", "Tú lo sabes y el lector lo necesita para actuar."),
        ("¿A cuáles cuatro preguntas responde la primera oración de una noticia?", "Who, What, Where y When", "Son quién, qué, dónde y cuándo."),
        ("¿Qué verbo de orden aparece en el folleto modelo para invitar?", "Join", "Join us! invita a participar."),
    ],
    task("Lee este encargo: tu curso organiza una «Feria de juegos de mesa» el jueves 12 a las 3 p.m. en la sala 5, con entrada gratis. Escribe en tu hoja: a) un folleto con título, when, where, price e invitación; b) una noticia de dos oraciones sobre la feria como si ya hubiera pasado (usa Who, What, Where y When). Marca los criterios de cada texto.", "a) Game Fair! Play and learn. When: Thursday 12, 3 p.m. Where: Room 5. Price: free. Join us! b) Board Game Fair! Class 7B had a board game fair. The fair was in Room 5 on Thursday at 3 p.m.", ["folleto con título, when, where, price e invitación", "noticia con titular y quién, qué, dónde y cuándo", "los datos coinciden con el encargo"], ["hoja con folleto y noticia"], ["olvidar un dato clave", "mezclar datos del folleto con los de la noticia"], "Pide que borre un dato y explique qué pregunta del lector queda sin responder."),
    "Copia el folleto modelo y subraya el título, los datos y la invitación con tres colores.",
    "Escribe un titular y una primera oración para una noticia sobre un partido de tu curso, con los cuatro datos.",
)

# ================================================================ OA 11 clase 5: comunicar de forma independiente (rima y cuento breve)
lesson(
    OA11, 5,
    "Los modelos de rima y cuento y las listas de criterios escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir una rima y un cuento breve siguiendo un modelo y criterios. Sirve para contar y jugar con el inglés de forma creativa.",
    ["Sé que una oración empieza con mayúscula y termina con punto.", "Conozco palabras como first, then y finally."],
    [
        "Una rima (rhyme) es un texto corto cuyos finales de verso suenan igual: cat y hat, night y light, day y play. Importa el sonido, no la escritura. Por eso home y come no riman: se escriben parecido, pero suenan distinto. Modelo de rima original: «I have a cat, / she wears a hat. / We play all day, / and then we say: hooray!».",
        "Un cuento breve (short story) tiene tres partes: comienzo (personaje y lugar), problema y final (solución). Para ordenar las ideas se usan first, then y finally. Modelo: «Last Saturday, Mia found a small box in the park. First, she opened it. Then she saw a note. Finally, she gave the box to the teacher». Los cuentos suelen estar en pasado: found (encontró), opened (abrió), saw (vio), gave (dio).",
        "Criterios de la rima: 1) cuatro versos, 2) al menos dos pares que riman por sonido, 3) tema claro. Criterios del cuento: 1) personaje y lugar, 2) un problema o suceso, 3) al menos dos conectores (first, then, finally), 4) un final. Trabaja de forma independiente: planifica, escribe y revisa sin copiar el modelo.",
    ],
    [("rhyme", "rima"), ("verse", "verso: una línea de la rima"), ("story", "cuento"), ("character", "personaje"), ("first / then / finally", "primero / luego / finalmente"), ("found", "encontró"), ("saw", "vio"), ("gave", "dio")],
    [
        ("Detectar rimas por sonido", "Pares: night–light, home–come, day–play. ¿Cuál par no rima aunque se escriba parecido?", ["Lee los sonidos en voz alta.", "Night y light riman; day y play riman.", "Home y come no riman."], "home–come"),
        ("Revisar un cuento con los criterios", "Cuento: «Last Sunday, Leo lost his bike key at the park. First, he looked in his bag. Then he asked a friend. Finally, he found it under a bench». ¿Cuál es el problema?", ["Busca qué le pasa al personaje.", "Perdió la llave de su bicicleta.", "Eso es lo que debe resolver."], "Leo lost his bike key"),
    ],
    [
        ("Pensar que riman las palabras que se escriben parecido.", "Se mira la escritura y no el sonido.", "Lee las dos palabras en voz alta: si el final suena igual, riman."),
        ("Escribir un cuento sin final.", "Se detiene cuando aparece el problema.", "Cierra con una oración que diga cómo se resuelve."),
    ],
    [
        ("¿Qué significa «finally»?", "Finalmente", "Marca la última parte del cuento."),
        ("¿Riman star y far? Responde sí o no.", "Sí", "Terminan en el mismo sonido."),
        ("¿Cuáles son las tres partes de un cuento breve?", "Comienzo, problema y final", "Así se ordena lo que ocurre."),
    ],
    [
        ("Une los pares que riman. Palabras: sea, tree, sun, run. Escribe los dos pares.", "sea–tree y sun–run", "Los finales suenan igual en cada par."),
        ("Cuento: «Emma lost her ticket at the zoo. First, she looked in her bag. Then she asked a guard». ¿Qué criterio falta? a) un final b) personaje y lugar", "a", "Hay personaje y lugar, pero no hay una oración de cierre."),
        ("Rima: «The sun is hot, / so we run a lot; / the sea is blue, / so we swim too». ¿Cuántos pares de versos riman por sonido?", "2", "Hot–lot y blue–too."),
    ],
    [
        ("Completa para que rime con light: «We sleep at ___.» Opciones: night / moon.", "night", "Night y light terminan con el mismo sonido."),
        ("Completa con conector: «First, he opened the door. ___, he saw a dog.» Opciones: Then / Because.", "Then", "Then marca el segundo paso de la secuencia."),
        ("Completa el pasado: «Yesterday, Nina ___ a coin on the street.» Opciones: found / find.", "found", "El cuento está en pasado y el pasado de find es found."),
    ],
    [
        ("Un compañero dice que book y look no riman porque empiezan con letras distintas. ¿Tiene razón? Responde sí o no.", "No", "Riman por sonido: terminan igual en -ook, aunque la letra inicial cambie."),
        ("Cuento: «Gabo was at the beach. First, he made a sandcastle. Finally, a wave destroyed it (destruyó). He laughed and built (construyó) a new one». Se piden 4 criterios. ¿Cuántos cumple?", "4", "Tiene personaje y lugar, un problema, dos conectores y un final."),
    ],
    [
        ("Ordena el cuento. a) Finally, he gave it to the guard. b) Last week, Dan found a wallet at school. c) First, he looked for a name inside it. Escribe las letras en orden.", "b, c, a", "Primero se presenta lo ocurrido, luego el primer paso y al final la solución."),
        ("Rima de tres versos: «I see a bee / up in a tree / and it looks at ___». Elige la palabra que cierra el verso con rima. Opciones: me / dog.", "me", "Bee, tree y me terminan con el mismo sonido."),
    ],
    [("En la hora de lectura debes escribir un cuento de tres líneas para tus compañeros menores. ¿Cuál cumple mejor los criterios? a) «Last Friday, Tina lost her scarf at school. First, she asked her teacher. Finally, a boy found it in the yard.» b) «Tina lost her scarf at school. She looked for it. Tina is sad.»", "a", "Tiene personaje y lugar, un problema, conectores y un final; b no tiene conectores ni final.")],
    [
        ("¿Se mira el sonido o la escritura para saber si dos palabras riman?", "El sonido", "Home y come se escriben parecido, pero no riman."),
        ("¿Qué conector sirve para el último paso de un cuento?", "Finally", "Cierra la secuencia."),
        ("¿Cuántos versos tiene la rima modelo de los criterios?", "4", "El criterio 1 pide cuatro versos."),
    ],
    task("Lee este encargo: elige uno de estos dos temas: A) rima sobre tu mascota favorita o una inventada, B) cuento sobre un objeto perdido en la escuela. Si eliges A: cuatro versos con dos pares que riman. Si eliges B: tres o cuatro oraciones con personaje, lugar, problema, final y dos conectores. Escríbelo en tu hoja y revísalo con los criterios de la clase.", "A) I have a frog, / he sits on a log. / He likes to hop, / he will not stop! B) Last Monday, Pablo lost his pencil case at school. First, he looked in the classroom. Then he asked the teacher. Finally, he found it in the library.", ["cumple todos los criterios del género elegido", "las rimas coinciden en sonido o el cuento tiene un final", "usa palabras que conoce, sin copiar el modelo"], ["hoja con el texto y los criterios marcados"], ["rimar solo por escritura", "dejar el cuento sin final"], "Pide que lea la rima en voz alta o cuente el cuento a una persona y explique qué cambió al revisarlo."),
    "Escribe diez pares de palabras y marca con una cruz los que riman por sonido.",
    "Escribe un cuento de cinco oraciones con tres conectores distintos y un final sorprendente.",
)
