"""Cuaderno del estudiante, 3.º básico Lenguaje y Comunicación: OA 27 (convenciones sociales) y OA 28 (exposición oral)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA27, OA28 = "LE03 OA 27", "LE03 OA 28"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, ctx, sc, open_args, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=sc, open_task=task(*open_args), reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 27 · clase 1
reg(
    OA27, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar presentaciones.",
    "Aprenderé a presentarme y a presentar a otras personas según la situación. Sirve para comenzar bien una conversación en el colegio, en el barrio o con personas adultas.",
    ["Sé decir mi nombre.", "Sé saludar."],
    [
        "Presentarse es decir quién eres cuando conoces a alguien. Una presentación sencilla tiene tu nombre y algo más que sea útil, como tu curso o algo que te gusta. No es necesario decir datos privados, como dónde vives o tu número de teléfono. Con un niño o una niña de tu edad puedes decir: «Hola, soy Camila, voy en tercero y me gusta dibujar».",
        "También podemos presentar a otras personas. Presentar es decir quién es alguien ante otra persona. Una fórmula muy usada es: «Te presento a Mateo, mi compañero de curso». Antes de presentar a alguien conviene mirar a ambos y decir primero el nombre de la persona a quien se le debe más respeto, por ejemplo una persona adulta.",
        "La manera de presentarse cambia según el contexto, que es la situación en que estamos. Con una persona adulta que no conocemos decimos: «Mucho gusto, soy Camila». A una persona adulta le hablamos de «usted»: «Le presento a Mateo». Con compañeros podemos decir «Hola, soy Camila». Después de la presentación, respondemos con una frase amable: «Mucho gusto» o «Encantado, encantada».",
    ],
    [("presentarse", "decir quién soy cuando conozco a alguien"), ("presentar", "decir quién es una persona a otra persona"), ("contexto", "situación en que estamos y personas con quienes hablamos"), ("dato privado", "información personal que no debemos dar a desconocidos"), ("mucho gusto", "fórmula amable al conocer a alguien")],
    [
        ("Presentarse a un compañero", "Llega Pablo, un niño nuevo, y quieres presentarte. Eres Camila, vas en tercero y te gusta dibujar. ¿Qué dices?", ["Digo hola y mi nombre.", "Agrego mi curso.", "Agrego algo que me gusta, sin datos privados."], "«Hola, soy Camila, voy en tercero y me gusta dibujar.»"),
        ("Presentar a dos personas", "Estás con tu compañero Mateo y llega tu profesora Rosa. ¿Cómo los presentas?", ["Miro a ambos.", "Nombro primero a la profesora.", "Digo quiénes son."], "«Profesora Rosa, le presento a Mateo, mi compañero de curso.»"),
    ],
    [("Dar tu dirección o tu teléfono al presentarte.", "Son datos privados.", "Di solo tu nombre y algo sobre ti, como tu curso."), ("Presentarse con un adulto exactamente como con los amigos.", "El contexto pide más cuidado.", "Con adultos usa «Mucho gusto» y habla con respeto.")],
    [
        E("¿Qué debe tener una presentación sencilla: tu nombre o tu dirección?", "Tu nombre", "La dirección es un dato privado."),
        E("Presentar a alguien es decir quién es esa persona a otra. ¿Es verdadero o falso?", "Verdadero", "Es la definición de presentar."),
        E("Responder «Mucho gusto» después de que te presenten, ¿es amable o descortés?", "Amable", "Es una fórmula de cortesía."),
    ],
    [
        E("¿Por qué no se dice la dirección al presentarse?", "Porque es un dato privado", "Puede poner en riesgo a la persona."),
        E("¿Qué es el contexto en una presentación?", "La situación en que estamos y con quién hablamos", "Cambia cómo hablamos."),
        E("Con una persona adulta desconocida, ¿qué se adapta mejor: «Mucho gusto, soy Camila» o «Ey, soy la Cami»?", "Mucho gusto, soy Camila", "Es más cuidadosa con una persona adulta."),
    ],
    [
        E("Pía va en tercero y le gusta correr. ¿Qué presentación tiene nombre, curso y gusto: a) «Hola, soy Pía, voy en tercero y me gusta correr.» b) «Hola, soy Pía y vivo en la calle Los Olmos.»", "a", "La b da un dato privado y no dice curso ni gusto."),
        E("Estás con tu amiga Lía y llega la señora Rosa, una vecina mayor. Elige cómo presentarlas: a) «Señora Rosa, le presento a Lía, mi amiga.» b) «Señora Rosa, esta es una persona.»", "a", "Dice nombres y relación, y trata de «usted» a la persona adulta."),
        E("Un niño nuevo dice: «Soy Toño». ¿Qué respondes con cortesía: «Mucho gusto, Toño» o «No me importa»?", "Mucho gusto, Toño", "Es la respuesta cortés."),
    ],
    [
        E("Pedro se presenta: «Soy Pedro, vivo en la calle Los Olmos 123, mi teléfono es…». ¿Qué datos no debería dar?", "La dirección y el teléfono", "Son datos privados."),
        E("Ana presenta a Eli, su vecina de 80 años, con su compañero Tomás: «Tomás, esta es Eli». ¿A quién conviene nombrar primero para mostrar respeto?", "A Eli", "Es una persona mayor."),
    ],
    [
        E("Estás en una reunión con una persona adulta que no conoces y un compañero. Presenta de manera cortés a tu compañero Hugo. Elige: a) «Le presento a Hugo, mi compañero.» b) «Este es Hugo.»", "a", "Es más completa y respetuosa."),
        E("Un niño no quiere decir su número de teléfono a alguien que acaba de conocer. ¿Está bien?", "Sí", "Es un dato privado y puede reservarlo."),
    ],
    [E("En una actividad, el curso conoce a un invitado, el señor Rojas. La profesora te pide que lo presentes a tu compañera Isa. ¿Qué parte nombras primero: «Señor Rojas» o «Isa»?", "Señor Rojas", "Se nombra primero a la persona adulta.")],
    [
        E("¿Puedo contar mi dirección a una persona que acabo de conocer?", "No", "Es un dato privado."),
        E("¿Se puede presentar a dos personas diciendo sus nombres?", "Sí", "Es la forma básica de presentar."),
        E("¿Cambia la presentación según el contexto?", "Sí", "Con adultos o amigos usamos formas distintas."),
    ],
    ("Practica presentaciones. Imagina tres situaciones: 1) conoces a una compañera nueva llamada Valentina, 2) tu profesora Rosa llega mientras estás con tu amigo Mateo, 3) un vecino adulto, el señor Rojas, llega a tu casa. Escribe qué dices en cada una. No escribas dirección ni teléfono.",
     "1) Hola, soy Camila. Mucho gusto. 2) Profesora Rosa, le presento a Mateo, mi amigo. 3) Mucho gusto, señor Rojas, soy Camila.",
     ["se presenta o presenta con nombres", "adapta el lenguaje a quien escucha", "no da datos privados"], ["hoja con tres presentaciones o práctica oral"], ["dar dirección o teléfono", "usar el mismo tono con todas las personas"],
     "Si usa datos privados, pregunta qué pasaría si un desconocido los oyera."),
    "Practica con una persona de tu casa cómo presentar a dos personas de tu familia que no se conocen.",
    "Escribe tres presentaciones distintas para el mismo niño: con un compañero, con un profesor y con un invitado.",
)

# ================================================================ OA 27 · clase 2
reg(
    OA27, 2,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a saludar y despedirme de forma distinta según la hora, la persona y el lugar. Sirve para convivir con respeto en el colegio, en la calle y en casa.",
    ["Sé presentarme.", "Sé decir hola y chao."],
    [
        "Saludar es mostrar que vemos a una persona y que nos importa. La manera de saludar cambia según el momento del día, la persona y el lugar. Por la mañana decimos «buenos días», después del almuerzo «buenas tardes» y al anochecer «buenas noches». Es un saludo de contexto, es decir, que se ajusta al momento.",
        "También cambia el registro, que es la forma de hablar según con quién hablamos. Con amigos usamos un registro informal y decimos «hola, ¿cómo estás?». Con una persona adulta, como una profesora o un vecino, usamos un registro más formal y decimos «buenos días, ¿cómo está?». Usamos «usted» con personas mayores o que no conocemos, y «tú» con amigos o con quien nos pide que lo tratemos de «tú».",
        "Además, cada persona tiene su forma de saludar: algunos prefieren un saludo con la mano, otros un abrazo o un beso y otros solo una sonrisa. Si alguien no quiere contacto físico, respetamos y saludamos con palabras. Si alguien insiste en un contacto que a ti no te gusta, puedes decir que no y contárselo a una persona adulta de confianza. Al despedirnos usamos «chao», «hasta mañana» o «que le vaya bien».",
    ],
    [("saludo", "palabra o gesto con que mostramos que vemos a alguien"), ("registro", "forma de hablar según con quién hablamos"), ("usted", "forma de hablar con respeto a una persona mayor o poco conocida"), ("despedida", "palabras con que nos separamos de alguien"), ("contacto físico", "tocar a alguien, como abrazo o beso")],
    [
        ("Elegir el saludo según la hora", "Son las 8 de la mañana y encuentras a tu vecina Eli en la entrada. ¿Cómo la saludas?", ["La hora es la mañana.", "Eli es una persona adulta.", "Uso «buenos días» y trato amable."], "«Buenos días, señora Eli, ¿cómo está?»"),
        ("Respetar la preferencia", "Tu amigo Leo extiende la mano y no quiere abrazos. ¿Cómo lo saludas?", ["Veo que prefiere la mano.", "Respeto su forma.", "Uso palabras amables."], "Le doy la mano o lo saludo con palabras: «Hola, Leo»."),
    ],
    [("Usar siempre «hola» con todo el mundo.", "Con personas mayores o en situaciones formales no siempre es lo más adecuado.", "Elige el saludo según hora y persona."), ("Obligar a alguien a dar un abrazo o un beso.", "Cada persona decide sobre su cuerpo.", "Saluda con palabras si no quiere contacto.")],
    [
        E("Por la mañana, ¿qué saludo corresponde: buenos días o buenas noches?", "Buenos días", "Se usa en la mañana."),
        E("Con amigos puedes decir «hola, ¿cómo estás?». ¿Es registro informal o formal?", "Informal", "Es la forma entre amigos."),
        E("Al despedirte de alguien, ¿puedes decir «hasta mañana»?", "Sí", "Es una despedida cortés."),
    ],
    [
        E("¿Qué es el registro?", "La forma de hablar según con quién hablamos", "Cambia entre amigos y adultos."),
        E("¿Por qué no se debe obligar a alguien a dar un abrazo?", "Porque cada persona decide sobre su cuerpo", "El respeto incluye el contacto físico."),
        E("A las 21:00 ya es de noche. ¿Qué saludo sería adecuado: buenas noches o buenos días?", "Buenas noches", "Es el saludo para el anochecer."),
    ],
    [
        E("Llegas a tu sala a las 8:15 y saludas a tu profesora. Elige: a) «Buenos días, profesora.» b) «Qué onda, profe.»", "a", "Es una forma más cuidadosa con una persona adulta."),
        E("Un niño no quiere un beso al saludar. ¿Cuál es una respuesta respetuosa: «Hola» con una sonrisa o insistir en el beso?", "Hola con una sonrisa", "Respeta su decisión."),
        E("Te despides de tu vecino mayor que va al médico. Elige la mejor: a) «Que le vaya bien.» b) «Ya, chao nomás.»", "a", "Es cortés y cuidadosa."),
    ],
    [
        E("Luis dice a una vecina mayor: «Buenas, ¿qué hay?». Ana dice: «Buenos días, señora, ¿cómo amaneció?». ¿Quién ajusta mejor su registro?", "Ana", "Usa un saludo más cuidado para una persona mayor."),
        E("Una compañera te dice «chao» a las 8 de la mañana al entrar al colegio. ¿Es el saludo adecuado?", "No", "Chao es una despedida, no un saludo de llegada."),
    ],
    [
        E("Llegas a una tienda a las 15:00. ¿Cuál es el saludo mejor: a) «Buenas tardes.» b) «Buenos días.»", "a", "A esa hora corresponde buenas tardes."),
        E("Un compañero te saluda con una pequeña reverencia, como se acostumbra en su familia, y no con la mano. ¿Qué conviene hacer: a) respetar su forma y saludar con palabras b) pedirle que lo haga como tú?", "a", "Respetar es aceptar las formas distintas."),
    ],
    [E("Mañana verás a tu profesora a las 8:30, a un amigo a las 13:30 y a una vecina mayor a las 22:00. ¿Cuántos saludos distintos necesitas: buenos días, buenas tardes y buenas noches?", "Tres", "Cada hora pide un saludo diferente.")],
    [
        E("¿Buenos días se usa en la mañana?", "Sí", "Es el saludo de ese momento."),
        E("¿Puedo cambiar mi saludo según con quién hablo?", "Sí", "Se llama cambiar el registro."),
        E("¿Debo respetar si alguien no quiere abrazos?", "Sí", "Cada persona decide sobre su cuerpo."),
    ],
    ("Elige tus saludos. Escribe cómo saludas y cómo te despides en tres situaciones: 1) a las 8:00 con tu profesora, 2) a las 14:00 con un amigo que prefiere dar la mano, 3) a las 21:00 con una vecina mayor. Usa el saludo según la hora, el registro adecuado y menciona una forma de respetar lo que cada persona prefiere.",
     "1) Buenos días, profesora; hasta mañana. 2) Hola, Leo; le doy la mano; chao. 3) Buenas noches, señora; que descanse.",
     ["usa la hora correcta", "adapta el registro", "respeta la preferencia de la persona"], ["hoja con tres saludos y despedidas"], ["usar el mismo saludo siempre", "no respetar una preferencia"],
     "Si repite el saludo, pregunta qué cambia según la hora o la persona."),
    "Observa durante un día cuántos saludos distintos dicen las personas de tu casa y anótalos.",
    "Escribe un diálogo de saludo entre un niño y un vecino mayor, usando «usted».",
)

# ================================================================ OA 27 · clase 3
reg(
    OA27, 3,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a preguntar y a pedir permiso con las fórmulas de cortesía por favor, gracias, permiso y perdón. Sirve para pedir cosas y pasar por lugares sin molestar a nadie.",
    ["Sé saludar y presentarme.", "Sé esperar una respuesta."],
    [
        "Pedir algo con cortesía significa usar palabras amables y un tono tranquilo. Las fórmulas de cortesía más usadas son «por favor», «gracias», «permiso» y «perdón». Se usan para pedir ayuda, agradecer, pasar por un lugar o disculparse. No son palabras mágicas: sirven cuando las decimos de verdad.",
        "Para preguntar algo a una persona podemos usar: «¿Me puedes decir…?», «¿Podría ayudarme con…?». Para pedir un permiso usamos: «¿Puedo salir al baño, por favor?» o «Con permiso, necesito pasar». Esperamos la respuesta. Si la respuesta es «no», aceptamos con calma y podemos preguntar por qué o cuándo sí se podrá.",
        "Una pregunta bien formada dice qué necesito y a quién se lo pido. Por ejemplo: «Profesora, ¿puede explicarme otra vez el ejercicio dos, por favor?». Es mejor que decir «No entiendo nada». Elegimos el momento para preguntar sin interrumpir a quien está hablando con otra persona.",
    ],
    [("cortesía", "manera amable de tratar a los demás"), ("permiso", "autorización para hacer algo"), ("fórmula de cortesía", "frase como por favor o gracias"), ("pedir", "decir lo que necesito a otra persona"), ("interrumpir", "hablar cuando otra persona está hablando")],
    [
        ("Pedir ayuda con cortesía", "Necesitas que tu compañero Hugo te preste su regla. Escribe cómo lo pides.", ["Digo su nombre.", "Pido con «podrías» o «puedes».", "Agrego «por favor»."], "«Hugo, ¿me prestas tu regla, por favor?»"),
        ("Pedir permiso para pasar", "Estás en el pasillo y hay personas conversando que bloquean el paso. ¿Qué dices?", ["Digo una fórmula de permiso.", "Hablo con tono tranquilo.", "Espero que se muevan."], "«Con permiso, necesito pasar.»"),
    ],
    [("Decir «Dame el lápiz» sin saludo ni cortesía.", "Parece una orden, no un pedido.", "Di: «¿Me prestas el lápiz, por favor?»"), ("Insistir cuando la respuesta es «no».", "No se respeta la decisión del otro.", "Acepta con calma y pregunta cuándo sí se podrá.")],
    [
        E("¿Qué fórmula usas para pedir pasar por un pasillo: con permiso o dame eso?", "Con permiso", "Es una fórmula de cortesía."),
        E("Para pedir un lápiz, ¿qué palabra agregas: por favor o ahora?", "Por favor", "Es una fórmula de cortesía."),
        E("Si te dicen «no», ¿qué haces: aceptar con calma o enojarte?", "Aceptar con calma", "Se respeta la decisión del otro."),
    ],
    [
        E("¿Qué es una fórmula de cortesía?", "Una frase amable como por favor o gracias", "Se usa para tratar bien a los demás."),
        E("¿Por qué conviene esperar la respuesta cuando pides permiso?", "Porque el permiso lo da la otra persona", "Hay que esperar su decisión."),
        E("Elige la pregunta más cortés: a) «¿Puedo salir al baño, por favor?» b) «Voy al baño.»", "a", "Pide permiso con cortesía."),
    ],
    [
        E("Necesitas la goma de un compañero solo un ratito y después se la devolverás. ¿Qué pides: «¿Me prestas tu goma, por favor?» o «¿Me regalas tu goma, por favor?»", "¿Me prestas tu goma, por favor?", "Se presta algo para devolverlo."),
        E("Tu profesora habla con un apoderado. Necesitas hacer una pregunta importante. ¿Qué haces primero: esperar una pausa o interrumpirlos?", "Esperar una pausa", "Así no interrumpes la conversación."),
        E("Se te cayó el cuaderno de una compañera al pasar. ¿Qué dices para disculparte: «Perdón, no fue mi intención» o «Fue tu culpa»?", "Perdón, no fue mi intención", "Es una disculpa cortés."),
    ],
    [
        E("Camila pide: «Dame el lápiz». Bea pide: «¿Me prestas el lápiz, por favor?». ¿Quién pide con más cortesía?", "Bea", "Usa pregunta y por favor."),
        E("Luis pidió permiso para salir y la profesora dijo que después. Luis dijo «Entonces me voy igual». ¿Respetó la respuesta?", "No", "Pidió permiso pero no aceptó la decisión."),
    ],
    [
        E("Quieres preguntar a la bibliotecaria dónde están los libros de animales. Elige la mejor pregunta: a) «Disculpe, ¿me podría decir dónde están los libros de animales, por favor?» b) «¿Dónde están?»", "a", "Es clara y cortés."),
        E("Una pregunta como «¿Qué hora es?» a un desconocido se mejora con: a) «Disculpe, ¿sabe qué hora es?» b) «Hora.»", "a", "Es cortés y clara."),
    ],
    [E("Estás en la fila del comedor y necesitas pasar entre dos compañeros. Piensa: ¿qué fórmula usas primero, «permiso» o «gracias»? Después de que te dejan pasar, ¿qué dices?", "Permiso; después gracias", "Primero pides pasar y luego agradeces.")],
    [
        E("¿Gracias es una fórmula de cortesía?", "Sí", "Se usa para agradecer."),
        E("¿Debo esperar la respuesta cuando pido permiso?", "Sí", "La otra persona decide."),
        E("¿Insistir tras un «no» es cortés?", "No", "No se respeta la decisión."),
    ],
    ("Pide con cortesía. Escribe qué dices en cada situación: 1) pedir a un compañero que te preste un sacapuntas, 2) pedir permiso a la profesora para ir al baño, 3) preguntar a una persona adulta del colegio, que no conoces, dónde queda la biblioteca, 4) pasar entre dos personas en un pasillo. Usa por favor, permiso, gracias o perdón, según corresponda.",
     "1) ¿Me prestas tu sacapuntas, por favor? 2) Profesora, ¿puedo ir al baño, por favor? 3) Disculpe, ¿me puede decir dónde queda la biblioteca? 4) Con permiso.",
     ["usa fórmulas de cortesía", "formula preguntas claras", "usa tono respetuoso"], ["hoja con cuatro frases o práctica oral"], ["ordenar en lugar de pedir", "no usar ninguna fórmula"],
     "Si la frase es una orden, pregunta cómo se diría como pregunta amable."),
    "Practica con una persona de tu casa tres veces cómo pedir algo con por favor y gracias.",
    "Inventa un diálogo corto entre un niño que pide permiso y un adulto que responde que no.",
)

# ================================================================ OA 27 · clase 4
reg(
    OA27, 4,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a expresar opiniones, sentimientos e ideas con respeto, sin gritar ni ofender. Sirve para decir lo que pienso y siento y que los demás me escuchen.",
    ["Sé pedir con cortesía.", "Sé reconocer emociones simples."],
    [
        "Cuando algo nos molesta o nos alegra, podemos decirlo. Expresar un sentimiento es contar lo que sentimos, como alegría, enojo, miedo o pena. Expresar una opinión es decir lo que pensamos. Una buena manera es usar mensajes con «yo»: «Yo me siento triste cuando no me dejan jugar» o «Yo pienso que podemos turnarnos».",
        "Para hablar con respeto cuidamos tres cosas. Primero, el tono: hablamos con voz tranquila, sin gritar. Segundo, las palabras: no usamos insultos ni burlas. Tercero, el momento: elegimos un momento en que la otra persona pueda escuchar. Si estamos muy enojados, respiramos y esperamos un poco antes de hablar.",
        "Un mensaje con «tú» suele sonar a acusación: «Tú siempre lo echas a perder». Un mensaje con «yo» habla de lo que siento: «Yo me puse triste cuando se rompió mi dibujo». También conviene decir qué necesito: «Me gustaría que me avisaran antes de usar mis cosas». Así los demás entienden y pueden ayudar.",
    ],
    [("sentimiento", "lo que sentimos por dentro, como alegría o enojo"), ("opinión", "lo que pensamos sobre algo"), ("mensaje con yo", "frase que habla de lo que yo siento o necesito"), ("tono", "manera en que suena la voz"), ("respetar", "tratar bien a los demás aunque pensemos distinto")],
    [
        ("Cambiar un mensaje de «tú» a «yo»", "Tu compañero usó tu estuche sin pedir permiso. Quieres decir «Tú siempre agarras mis cosas». Cámbialo a un mensaje con «yo».", ["Pienso qué siento.", "Digo lo que me pasó.", "Pido lo que necesito."], "«Yo me molesto cuando usan mis cosas sin avisar. Me gustaría que me pidieran permiso.»"),
        ("Expresar una opinión con respeto", "Tu grupo quiere hacer un afiche de color rojo y tú prefieres azul. ¿Qué dices?", ["Digo lo que pienso con «yo».", "Doy una razón.", "No ataco la idea de otros."], "«Yo prefiero el azul, porque se ve mejor con las letras blancas. ¿Qué piensan?»"),
    ],
    [("Gritar para que me escuchen.", "Los demás se asustan o se enojan y no entienden.", "Usa voz tranquila y mensaje con «yo»."), ("Decir «tú siempre…» o «tú nunca…».", "Acusa y no deja espacio para escuchar.", "Habla de lo que sientes y pide lo que necesitas.")],
    [
        E("Un mensaje con «yo» habla de lo que yo siento o necesito. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        E("¿Cuál es un sentimiento: alegría o escuela?", "Alegría", "Es algo que se siente por dentro."),
        E("¿Cuál tono es mejor para expresar un enojo: voz tranquila o gritos?", "Voz tranquila", "Se escucha mejor."),
    ],
    [
        E("¿Por qué los mensajes con «tú siempre…» suelen funcionar peor?", "Porque acusan y la otra persona se defiende", "No ayudan a escuchar."),
        E("¿Para qué sirve decir «Me gustaría que…»?", "Para decir qué necesito", "Ayuda a que los demás sepan qué puede mejorar."),
        E("Si estás muy enojado, ¿qué conviene hacer: respirar y esperar un poco o insultar enseguida?", "Respirar y esperar un poco", "Ayuda a hablar con calma."),
    ],
    [
        E("Elige el mensaje con «yo»: a) «Tú nunca me esperas.» b) «Yo me siento solo cuando no me esperan.»", "b", "Habla de lo que siento."),
        E("Tu amigo se ríe cuando te equivocas. Escribe qué sientes. Usa «Yo me siento… cuando…»; la emoción puede ser tristeza.", "Yo me siento triste cuando se ríen de mí", "Expresa el sentimiento con «yo»."),
        E("Quieres pedir que bajen la voz en la sala. ¿Cuál es respetuosa: «Yo necesito silencio para concentrarme, ¿pueden hablar más bajito?» o «¡Cállense!»?", "Yo necesito silencio para concentrarme, ¿pueden hablar más bajito?", "Dice lo que necesitas con respeto."),
    ],
    [
        E("Ana dice: «Tú arruinas todo». Bea dice: «Yo me enojo cuando se pierde nuestro trabajo». ¿Quién expresa mejor su sentimiento?", "Bea", "Habla de lo que ella siente."),
        E("Un niño dice: «No quiero jugar a eso, porque me da miedo». ¿Está bien expresar miedo?", "Sí", "Los sentimientos se pueden decir con respeto."),
    ],
    [
        E("Tu compañero opina que el recreo es corto. Tú piensas que está bien. ¿Cuál es respetuosa: «Yo pienso distinto: creo que alcanza para jugar» o «Qué tontería»?", "Yo pienso distinto: creo que alcanza para jugar", "Opina sin descalificar."),
        E("Si algo te hizo feliz, ¿también puedes expresarlo con un mensaje con «yo»?", "Sí", "Los sentimientos positivos también se comunican."),
    ],
    [E("En el grupo, Joaquín grita: «¡Tú no entiendes nada!». Camila le responde: «Yo me siento confundida. ¿Me lo explicas más despacio?». ¿Quién habló con respeto?", "Camila", "Habló tranquila, dijo cómo se sentía y pidió ayuda.")],
    [
        E("¿Puedo decir lo que siento sin insultar?", "Sí", "Un mensaje con «yo» lo permite."),
        E("¿Gritar ayuda a que me entiendan?", "No", "Los demás se asustan o se defienden."),
        E("¿Puedo pedir lo que necesito con «Me gustaría que…»?", "Sí", "Es una forma clara y respetuosa."),
    ],
    ("Expresa con respeto. Escribe qué dirías en cada situación con un mensaje con «yo»: 1) un compañero se llevó tu cuaderno sin avisar y estás molesto, 2) tu equipo ganó el juego y estás contento, 3) tu grupo quiere decorar con globos y tú prefieres flores. Di tu sentimiento u opinión, y lo que necesitas o piensas.",
     "1) Yo me molesto cuando me sacan el cuaderno sin avisar. Me gustaría que me pidieran permiso. 2) Yo me siento feliz de que ganamos. 3) Yo prefiero las flores, porque son más bonitas. ¿Qué piensan?",
     ["usa mensajes con «yo»", "expresa el sentimiento o la opinión", "no ofende ni acusa"], ["hoja con tres mensajes"], ["usar «tú siempre»", "insultar o burlarse"],
     "Si el mensaje acusa, pregunta cómo se diría hablando de lo que siente."),
    "Dile a una persona de tu casa algo que te alegró hoy usando «Yo me siento…».",
    "Escribe un mensaje con «yo» para pedir ayuda a un profesor en un trabajo difícil.",
)

# ================================================================ OA 27 · clase 5
reg(
    OA27, 5,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a agradecer, a pedir disculpas y a reparar el daño que causamos. Sirve para cuidar las relaciones con los demás y hacernos cargo de lo que hacemos.",
    ["Sé usar por favor y permiso.", "Sé expresar sentimientos con «yo»."],
    [
        "Agradecer es decir gracias cuando alguien nos ayuda o nos da algo. Un buen agradecimiento dice por qué agradecemos: «Gracias por prestarme el lápiz; me sirvió mucho». Disculparse es reconocer que hicimos algo que molestó o dañó a otra persona y decir «perdón» o «lo siento».",
        "Una disculpa sincera tiene tres partes: reconocer lo que hice («Rompí tu lápiz»), decir perdón («Perdón») y ofrecer algo para reparar. Reparar significa hacer algo para arreglar el daño, como reponer con un lápiz nuevo, ayudar a limpiar o volver a hacer una tarea. Reparar muestra que nos importa la otra persona.",
        "No sirve decir «perdón, pero tú también…» porque culpa al otro y no repara. Tampoco sirve exigir que el otro nos perdone enseguida: a veces necesita tiempo. Si nos perdonan, agradecemos. Si no, respetamos y cuidamos el trato. Podemos también agradecer ayudas pequeñas, como que nos guarden el puesto.",
    ],
    [("agradecer", "decir gracias por algo que alguien hizo o dio"), ("disculpa", "palabras con que reconocemos un error y decimos perdón"), ("reparar", "hacer algo para arreglar un daño"), ("sincera", "que se dice de verdad"), ("perdonar", "aceptar la disculpa de alguien")],
    [
        ("Armar una disculpa con reparación", "Sin querer, manchaste con pintura el dibujo de tu compañera Nina. Escribe una disculpa con las tres partes.", ["Digo lo que hice.", "Digo perdón.", "Ofrezco reparar."], "«Manché tu dibujo. Perdón. ¿Quieres que te ayude a hacerlo de nuevo?»"),
        ("Agradecer diciendo por qué", "Tu amigo Tomás te guardó el puesto en la fila del comedor. ¿Cómo agradeces?", ["Digo gracias.", "Digo qué hizo.", "Digo cómo me ayudó."], "«Gracias por guardarme el puesto; así no me quedé al final.»"),
    ],
    [("Decir «perdón, pero tú también…».", "Culpa al otro y no repara.", "Reconoce tu parte y di perdón; el resto puede hablarse después."), ("Esperar que me perdonen enseguida.", "La otra persona puede necesitar tiempo.", "Ofrece reparar y respeta su tiempo.")],
    [
        E("¿Qué palabra usas para agradecer: gracias o permiso?", "Gracias", "Es la fórmula de agradecimiento."),
        E("¿Qué significa reparar: arreglar un daño o ignorar lo que pasó?", "Arreglar un daño", "Es hacerse cargo."),
        E("Una disculpa sincera, ¿dice «perdón» y reconoce lo que pasó?", "Sí", "Son partes de la disculpa."),
    ],
    [
        E("¿Cuáles son las tres partes de una disculpa sincera?", "Reconocer lo que hice, decir perdón y ofrecer reparar", "Así la disculpa es completa."),
        E("¿Por qué «perdón, pero tú también…» no es buena disculpa?", "Porque culpa al otro", "No reconoce mi parte ni repara."),
        E("Rompiste el borrador de Ema. ¿Qué es reparar: reponerlo con otro igual, o decir solo «perdón»?", "Reponerlo con otro igual", "Reparar es arreglar el daño."),
    ],
    [
        E("Llegaste tarde a una reunión del grupo. Elige la disculpa con reparación: a) «Llegué tarde. Perdón. Ayudo a terminar la parte que falta.» b) «No fue mi culpa.»", "a", "Reconoce, pide perdón y repara."),
        E("Una compañera te prestó su goma. Elige el agradecimiento que dice por qué: a) «Gracias por la goma, pude borrar el error.» b) «Ya.»", "a", "Dice gracias y por qué."),
        E("Tiraste un vaso de agua en la mesa de un compañero. ¿Qué reparación ayuda: limpiar la mesa o irte?", "Limpiar la mesa", "Arregla el daño causado."),
    ],
    [
        E("Teo dice: «Perdón, pero tú me empujaste primero». Pía dice: «Te empujé sin querer. Perdón. ¿Estás bien?». ¿Quién hizo una mejor disculpa?", "Pía", "Reconoce, pide perdón y se preocupa por el otro."),
        E("Después de tu disculpa, el compañero dice que necesita tiempo. ¿Qué haces: respetar o insistir hasta que te perdone?", "Respetar", "El perdón no se puede exigir."),
    ],
    [
        E("Tomás agradeció a Luis: «Gracias por ayudarme con la mochila, pesaba mucho». ¿Dijo qué hizo y por qué agradece?", "Sí", "Nombra la ayuda y su razón."),
        E("¿Se puede agradecer una ayuda pequeña, como que te presten un lápiz?", "Sí", "Agradecer cuida las relaciones incluso en cosas pequeñas."),
    ],
    [E("Sin querer, rompiste el cartel que preparó un compañero para exponer. Tienes 20 minutos antes de la exposición y alcanza para hacer otro cartel. Elige la mejor: a) «Rompí tu cartel. Perdón. Te ayudo a hacer otro ahora.» b) «Fue un accidente, no pasa nada.»", "a", "Reconoce, pide perdón y repara.")],
    [
        E("¿Una disculpa sincera necesita decir perdón?", "Sí", "Es una de sus partes."),
        E("¿Reparar significa arreglar el daño?", "Sí", "Es hacerse cargo."),
        E("¿Puedo exigir que me perdonen enseguida?", "No", "Cada persona necesita su tiempo."),
    ],
    ("Agradece, discúlpate y repara. Escribe una frase para cada situación: 1) un compañero te ayudó a recoger tus cuadernos, 2) sin querer pisaste el trabajo de una compañera y lo ensuciaste, 3) llegaste tarde a un acuerdo del grupo. En las situaciones 2 y 3 usa las tres partes: reconocer, perdón y reparar.",
     "1) Gracias por ayudarme a recoger los cuadernos; me ahorraste tiempo. 2) Pisé tu trabajo. Perdón. Te ayudo a limpiarlo o a repetirlo. 3) Llegué tarde. Perdón. Hago ahora la parte que faltó.",
     ["agradece diciendo por qué", "disculpa con las tres partes", "propone una reparación posible"], ["hoja con tres frases"], ["decir perdón pero culpar al otro", "no ofrecer reparación"],
     "Si falta la reparación, pregunta qué podría hacer para arreglar el problema."),
    "Escribe una nota de agradecimiento para alguien que te ayudó esta semana.",
    "Inventa una escena en que un niño se disculpa y repara un daño, y represéntala con una persona de tu casa.",
)

# ================================================================ OA 28 · clase 1
reg(
    OA28, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa que haga de público.",
    "Aprenderé a elegir la idea central de una exposición y a pensar en quién la escuchará. Sirve para hablar con claridad sobre un tema que me interesa y para que me entiendan.",
    ["Sé contar algo que me gusta.", "Sé hablar frente a un grupo pequeño."],
    [
        "Exponer es contar un tema a otras personas de forma ordenada. Antes de hablar, conviene decidir cuál es la idea central, que es lo más importante que quiero que las personas entiendan. La idea central se puede decir en una sola oración. Por ejemplo: «Las plantas necesitan luz, agua y tierra para crecer».",
        "También pensamos en la audiencia, que son las personas que me escucharán. No es lo mismo exponer ante compañeros de tu edad que ante niños más pequeños o ante personas adultas. Si la audiencia es más pequeña, uso palabras más simples y ejemplos más cortos. Si ya conoce el tema, puedo agregar datos nuevos.",
        "Una exposición clara tiene un tema, una idea central y un público. Un tema es de qué hablo; la idea central es lo que quiero que entiendan sobre ese tema. «Las plantas» es un tema. «Las plantas necesitan luz, agua y tierra» es una idea central. Con la idea central clara, elegimos qué ejemplos y datos incluir.",
    ],
    [("exponer", "contar un tema a otras personas de forma ordenada"), ("tema", "asunto del que hablo"), ("idea central", "lo más importante que quiero que entiendan"), ("audiencia", "personas que me escuchan"), ("oración", "conjunto de palabras con sentido completo")],
    [
        ("Distinguir tema e idea central", "¿Cuál es el tema y cuál la idea central? a) «Los gatos» b) «Los gatos duermen muchas horas al día y necesitan cariño».", ["Veo cuál es corta y amplia.", "«Los gatos» solo nombra el asunto.", "La b dice lo que quiero que entiendan."], "El tema es «Los gatos» (a) y la idea central es la b."),
        ("Pensar en la audiencia", "Vas a exponer sobre cómo cuidar una planta ante niños de primero básico. ¿Qué cambias respecto de exponer ante tu curso?", ["Pienso en su edad.", "Uso palabras simples.", "Uso ejemplos cortos."], "Uso palabras más simples y ejemplos más cortos."),
    ],
    [("Hablar de un tema muy amplio sin una idea central.", "La audiencia no sabe qué debe entender.", "Escribe una oración que diga lo más importante."), ("Usar palabras difíciles con niños más pequeños.", "No entienden.", "Cambia por palabras simples y da un ejemplo.")],
    [
        E("¿«Los perros» es un tema o una idea central?", "Un tema", "Solo nombra el asunto."),
        E("¿La audiencia son las personas que escuchan?", "Sí", "Es el público de la exposición."),
        E("¿Qué es la idea central: lo más importante que quiero que entiendan o el título?", "Lo más importante que quiero que entiendan", "Resume el mensaje principal."),
    ],
    [
        E("¿Por qué conviene pensar en la audiencia antes de exponer?", "Para elegir palabras y ejemplos que entiendan", "Cambia según quienes escuchan."),
        E("Una idea central puede decirse en una oración. ¿Verdadero o falso?", "Verdadero", "Resume lo central en pocas palabras."),
        E("Para niños de primero, ¿qué conviene usar: palabras simples o palabras muy técnicas?", "Palabras simples", "Así entienden mejor."),
    ],
    [
        E("Elige la idea central: a) «Las plantas» b) «Las plantas necesitan luz, agua y tierra para crecer».", "b", "Dice lo que quiero que entiendan."),
        E("Tema: «El reciclaje». Elige la idea central: a) «El reciclaje» b) «Reciclar el papel y el plástico ayuda a cuidar el planeta».", "b", "Es una oración con idea completa; la a solo nombra el tema."),
        E("Vas a exponer ante niños de primero. ¿Qué conviene cambiar: tus palabras y ejemplos o nada?", "Mis palabras y ejemplos", "La audiencia influye en cómo hablo."),
    ],
    [
        E("Luis expone: «Hoy voy a hablar de animales». Ema expone: «Hoy voy a mostrar que los gatos necesitan agua fresca, comida y cariño». ¿Quién tiene idea central más clara?", "Ema", "Dice lo que quiere que entiendan."),
        E("Un niño dice: «Mi idea central es el sol, la luna, las estrellas, el mar y los árboles». ¿Es una sola idea central clara?", "No", "Mezcla muchos temas sin una idea que los una."),
    ],
    [
        E("Expones a niños de 5 años. ¿Qué ejemplo conviene: «El agua sube desde la raíz» o «La planta toma agua como tú con un sorbete»?", "La planta toma agua como tú con un sorbete", "Compara con algo que conocen."),
        E("Tienes dos temas: «las plantas» y «cómo cuidar una planta». ¿Cuál se acerca más a una idea central útil?", "Cómo cuidar una planta", "Orienta lo que dirás."),
    ],
    [E("Ana dice: «Mi tema es los juegos». Leo dice: «Mi idea central es que el luche se salta en un pie y se juega con una piedra». ¿Quién dijo una idea central?", "Leo", "Dice en una oración lo que quiere que entiendan.")],
    [
        E("¿El tema y la idea central son lo mismo?", "No", "El tema es de qué hablo; la idea central es lo que quiero que entiendan."),
        E("¿Pienso en la audiencia antes de exponer?", "Sí", "Para elegir palabras y ejemplos."),
        E("¿La idea central puede decirse en una oración?", "Sí", "Resume el mensaje."),
    ],
    ("Prepara tu idea central. Elige uno de estos temas: «las plantas», «el reciclaje» o «un juego que me gusta». Escribe: 1) el tema, 2) una oración con la idea central, 3) a qué audiencia le hablarás (compañeros, niños más pequeños o personas adultas) y una cosa que cambiarás para esa audiencia.",
     "1) Las plantas. 2) Las plantas necesitan luz, agua y tierra para crecer. 3) Niños más pequeños: usaré palabras simples y un ejemplo con regar una macetita.",
     ["distingue tema e idea central", "escribe una oración completa", "adapta la exposición a la audiencia"], ["hoja con tres respuestas o explicación oral"], ["idea central que es solo un título", "no pensar en la audiencia"],
     "Si la idea es solo una palabra, pide que diga qué quiere que entiendan."),
    "Cuenta a una persona de tu casa tu idea central en una sola oración.",
    "Prepara dos ideas centrales distintas para el mismo tema, para dos audiencias distintas.",
)

# ================================================================ OA 28 · clase 2
reg(
    OA28, 2,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a ordenar mi exposición en introducción, desarrollo y cierre. Sirve para que quienes escuchan sigan mis ideas y sepan cuándo empiezo y cuándo termino.",
    ["Sé decir una idea central.", "Sé usar primero, luego y finalmente."],
    [
        "Una exposición tiene partes. La introducción es el comienzo: saludamos, decimos el tema y la idea central, y contamos qué vamos a explicar. El desarrollo es la parte principal: ahí explicamos las ideas una tras otra, en un orden claro. El cierre recuerda la idea central y agradece a quienes escucharon.",
        "En el desarrollo conviene ordenar las ideas con palabras como «primero», «luego», «además» y «por último». Por ejemplo, si hablamos de cómo cuidar una planta: primero la luz, luego el agua, por último la tierra. Cada idea tiene una explicación breve y, si se puede, un ejemplo.",
        "La introducción no debe ser muy larga: dos o tres oraciones bastan. Una introducción puede ser: «Hola, soy Ana. Hoy les contaré cómo cuidar una planta. Veremos la luz, el agua y la tierra». Así quienes escuchan saben qué sigue y pueden prestar más atención.",
    ],
    [("introducción", "comienzo de la exposición donde presento el tema"), ("desarrollo", "parte principal donde explico las ideas"), ("cierre", "final donde recuerdo la idea central y agradezco"), ("orden", "forma de colocar las ideas una después de otra"), ("conector", "palabra que une ideas, como primero o luego")],
    [
        ("Ordenar una exposición", "Ordena estas partes de una exposición: a) «Gracias por escuchar.» b) «Primero, la luz.» c) «Hola, hoy les cuento cómo cuidar una planta.»", ["Busco el comienzo con saludo y tema.", "Sigue la explicación.", "Termina con agradecimiento."], "c, b, a."),
        ("Reconocer una introducción", "¿Cuál es una buena introducción? a) «Primero, el agua.» b) «Hola, soy Leo. Hoy les explico cómo hacer un barco de papel.»", ["Busco saludo, tema y qué haré.", "La b presenta el tema.", "La a ya está en el desarrollo."], "La b."),
    ],
    [("Empezar la exposición sin decir de qué se hablará.", "La audiencia se pierde.", "Di tu nombre, el tema y lo que explicarás."), ("Terminar de golpe sin cierre.", "No queda claro qué se debía recordar.", "Repite la idea central y agradece.")],
    [
        E("¿Qué parte de la exposición va primero: introducción o cierre?", "Introducción", "Presenta el tema antes de explicar."),
        E("¿En qué parte explicamos las ideas: en la introducción o en el desarrollo?", "En el desarrollo", "Es la parte principal."),
        E("¿Qué palabra ordena ideas: primero o nunca?", "Primero", "Es un conector de orden."),
    ],
    [
        E("¿Qué se dice en el cierre?", "La idea central y un agradecimiento", "Recuerda lo importante y despide."),
        E("¿Por qué es útil decir qué vas a explicar en la introducción?", "Para que el público sepa qué sigue", "Ayuda a seguir la explicación."),
        E("Ordena: a) luego el agua b) primero la luz c) por último la tierra. Escribe las letras en orden.", "b, a, c", "Siguen primero, luego y por último."),
    ],
    [
        E("Elige la mejor introducción para el tema «cómo hacer un barco de papel»: a) «Hola, hoy les muestro cómo hacer un barco de papel, doblando la hoja en tres pasos.» b) «Barco.»", "a", "Tiene saludo, tema y plan."),
        E("Completa con un conector: «___ pintamos el fondo; luego pegamos los dibujos». ¿Cuál falta: primero o jamás?", "Primero", "Marca el inicio del orden."),
        E("Ordenas tres ideas con «primero», «luego» y «por último»: la luz, el agua y la tierra. ¿Qué conector va con la tierra, si es la última idea?", "Por último", "La última idea lleva «por último»."),
    ],
    [
        E("Carla empieza: «Voy a hablar de cosas». Pía empieza: «Hola, soy Pía. Hoy les contaré cómo se juega al luche». ¿Quién tiene mejor introducción?", "Pía", "Dice quién es, el tema y lo que hará."),
        E("Una exposición termina diciendo «Eso es todo». ¿Tiene un cierre completo?", "No", "No repite la idea central ni agradece."),
    ],
    [
        E("Ordena los pasos de una exposición completa: a) agradecer b) explicar tres ideas c) presentar el tema d) repetir la idea central. Escribe las letras.", "c, b, d, a", "Introducción, desarrollo, cierre con idea y agradecimiento."),
        E("¿Cuántas partes principales tiene una exposición: introducción, desarrollo y cierre?", "Tres", "Esas son las partes."),
    ],
    [E("Una exposición sobre el reciclaje comienza con «Hola, soy Bruno; hoy les cuento tres formas de reciclar», explica papel, vidrio y plástico, y termina con «Reciclar ayuda al planeta; gracias por escuchar». ¿Cuántas formas de reciclar explica en el desarrollo?", "Tres", "Papel, vidrio y plástico.")],
    [
        E("¿El cierre agradece a la audiencia?", "Sí", "Es una buena forma de terminar."),
        E("¿El desarrollo es la parte principal?", "Sí", "Ahí se explican las ideas."),
        E("¿Los conectores ayudan a ordenar las ideas?", "Sí", "Marcan el orden."),
    ],
    ("Ordena tu exposición. Elige el tema «cómo cuidar una planta» o «cómo jugar al luche». Escribe: 1) una introducción de dos o tres oraciones con saludo, tema y qué explicarás, 2) tres ideas del desarrollo con los conectores primero, luego y por último, 3) un cierre con la idea central y agradecimiento. Léelo en voz alta a una persona de tu casa.",
     "1) Hola, soy Ana. Hoy les cuento cómo cuidar una planta. Veremos luz, agua y tierra. 2) Primero, la luz; luego, el agua; por último, la tierra. 3) Para crecer, una planta necesita luz, agua y tierra. Gracias por escuchar.",
     ["la introducción tiene saludo, tema y plan", "el desarrollo usa conectores", "el cierre recuerda la idea central y agradece"], ["texto escrito y lectura en voz alta"], ["omitir la introducción", "terminar sin cierre"],
     "Si falta el cierre, pregunta qué quieres que la audiencia recuerde."),
    "Cuenta a una persona de tu casa los pasos de una receta simple usando primero, luego y por último.",
    "Prepara la misma exposición con un cierre distinto: una pregunta para el público.",
)

# ================================================================ OA 28 · clase 3
reg(
    OA28, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: un objeto pequeño de tu casa para describir.",
    "Aprenderé a incluir descripciones y ejemplos para ilustrar mis ideas en una exposición. Sirve para que quienes escuchan imaginen lo que digo y comprendan mejor.",
    ["Sé ordenar una exposición.", "Sé decir cómo es algo."],
    [
        "Una idea suelta se entiende mejor cuando la acompañamos con una descripción y un ejemplo. Describir es decir cómo es algo: su forma, color, tamaño, sonido, textura o para qué sirve. Un ejemplo es un caso concreto que muestra la idea. Si digo «Las frutas son sanas», puedo dar el ejemplo «Una manzana tiene vitaminas».",
        "Para describir usamos palabras que dicen cómo es algo: «redonda», «roja», «suave», «pequeña». Para dar un ejemplo usamos «por ejemplo», «como» o «es el caso de». Una descripción y un ejemplo no deben ser muy largos: una o dos oraciones. Se colocan justo después de la idea que explican.",
        "Elegimos ejemplos que la audiencia conozca. Si hablo de animales domésticos ante niños, un ejemplo posible es el perro o el gato. Un ejemplo inventado que no tiene que ver con la idea confunde. La descripción y el ejemplo deben ayudar a entender, no a llenar tiempo.",
    ],
    [("descripción", "palabras que dicen cómo es algo"), ("ejemplo", "caso concreto que muestra una idea"), ("detalle", "dato pequeño que ayuda a imaginar"), ("ilustrar", "aclarar una idea con ejemplos o imágenes"), ("concreto", "que se puede ver, tocar o imaginar con claridad")],
    [
        ("Agregar una descripción", "Idea: «Mi mascota es tranquila». Agrega una descripción: ¿cómo es o qué hace?", ["Pienso en lo que se ve.", "Digo cómo se mueve o cómo se ve.", "Lo uno a la idea."], "«Mi mascota es tranquila: duerme casi todo el día en su cama.»"),
        ("Agregar un ejemplo", "Idea: «Hay frutas que son rojas». Agrega un ejemplo.", ["Pienso en una fruta roja.", "Uso «por ejemplo».", "Lo uno a la idea."], "«Hay frutas rojas; por ejemplo, la frutilla.»"),
    ],
    [("Dar ejemplos que no tienen relación con la idea.", "Confunden a quienes escuchan.", "Elige un ejemplo que muestre exactamente la idea."), ("Hacer descripciones muy largas.", "La audiencia pierde el hilo.", "Usa una o dos oraciones por descripción.")],
    [
        E("Describir es decir cómo es algo. ¿Verdadero o falso?", "Verdadero", "Es la definición de describir."),
        E("Un ejemplo es un caso concreto. ¿Verdadero o falso?", "Verdadero", "Muestra la idea con un caso."),
        E("¿Cuál es una descripción: «redonda y roja» o «ayer fui al parque»?", "Redonda y roja", "Dice cómo es algo."),
    ],
    [
        E("¿Por qué una descripción ayuda a quienes escuchan?", "Porque les permite imaginar lo que digo", "Hace la idea más clara."),
        E("Idea: «Los animales de la granja dan alimento». Ejemplo posible: ¿la vaca da leche o el sol da luz?", "La vaca da leche", "Es un animal de granja que da alimento."),
        E("¿Qué palabras anuncian un ejemplo: por ejemplo o sin embargo?", "Por ejemplo", "Anuncia un caso."),
    ],
    [
        E("Idea: «Mi pelota es especial». Elige una descripción: a) «Es azul, blanda y tiene una estrella.» b) «La compré ayer.»", "a", "Dice cómo es."),
        E("Idea: «Hay deportes que se juegan en equipo». Elige un ejemplo: a) el fútbol b) la lectura silenciosa.", "a", "El fútbol se juega en equipo."),
        E("Idea: «Mi lugar favorito es la ventana». ¿Cuál es una descripción del lugar: a) «Tiene mucha luz y vista a un árbol.» b) «Ayer fui con mi amigo.»", "a", "Dice cómo es el lugar; la b habla de otro día."),
    ],
    [
        E("Ana dice: «Mi gato es suave y gris, y duerme en una caja». Bea dice: «Mi gato es lindo». ¿Quién ilustra mejor?", "Ana", "Da detalles de cómo es y qué hace."),
        E("Luis explica «Los árboles dan sombra» y el ejemplo: «Mi primo tiene un auto rojo». ¿El ejemplo ayuda?", "No", "No se relaciona con la idea."),
    ],
    [
        E("Idea: «Mi comida favorita es fácil de preparar». Elige la que mejor ilustra: a) «Solo se mezcla pan con queso y se calienta con ayuda de un adulto.» b) «Me gusta mucho.»", "a", "Da un ejemplo concreto de cómo se prepara."),
        E("Idea: «En el patio hay cosas para jugar». Elige el ejemplo con «por ejemplo»: a) «Por ejemplo, el columpio.» b) «Por ejemplo, la estrella.»", "a", "El columpio es algo para jugar."),
    ],
    [E("Estás explicando que algunos animales viven en el mar. Un compañero dice: «Por ejemplo, los delfines». Otro dice: «Por ejemplo, los caballos». ¿Cuál ejemplo es correcto?", "Los delfines", "Viven en el mar; los caballos no.")],
    [
        E("¿Una descripción dice cómo es algo?", "Sí", "Ayuda a imaginarlo."),
        E("¿Puedo usar «por ejemplo» para dar un caso?", "Sí", "Anuncia el ejemplo."),
        E("¿Los ejemplos deben tener relación con la idea?", "Sí", "Si no, confunden."),
    ],
    ("Ilustra tus ideas. Elige una de estas ideas: «Mi mascota o animal favorito es especial», «Mi lugar favorito es especial» o «Mi juego favorito es entretenido». Escribe: la idea, dos oraciones de descripción y un ejemplo con «por ejemplo». Luego léelo a una persona de tu casa.",
     "Mi lugar favorito es especial. Es la ventana de mi pieza y tiene mucha luz. Desde ahí se ve un árbol grande con hojas verdes. Por ejemplo, ahí leo mis cuentos por la tarde.",
     ["incluye la idea", "agrega dos oraciones de descripción", "usa un ejemplo relacionado"], ["texto escrito y lectura en voz alta"], ["ejemplo sin relación", "descripción muy general"],
     "Si la descripción es general, pregunta qué se ve, se oye o se siente."),
    "Describe a una persona de tu casa un objeto sin decir su nombre, para que lo adivine.",
    "Escribe un ejemplo y una descripción para cada una de tres ideas distintas.",
)

# ================================================================ OA 28 · clase 4
reg(
    OA28, 4,
    "Este cuaderno, lápiz y una hoja.",
    "Aprenderé a decir con precisión de quién o de qué hablo, y a variar el vocabulario. Sirve para que nadie se confunda y para que mi exposición suene clara y variada.",
    ["Sé describir y dar ejemplos.", "Sé qué son los pronombres (él, ella, eso)."],
    [
        "Los pronombres, como «él», «ella», «eso» o «lo», reemplazan palabras para no repetirlas. Pero a veces confunden. Si digo «Ana habló con Bea y ella se rió», no se sabe quién se rió. El referente es la persona o cosa a la que se refiere un pronombre. Cuando hay dudas, conviene decir el nombre: «Ana habló con Bea y Bea se rió».",
        "En una exposición, hablamos ante personas que no pueden preguntar enseguida. Por eso es mejor explicitar el referente: nombrar con claridad de qué o de quién hablamos. Cambiamos «eso es importante» por «cuidar el agua es importante». Así la audiencia no tiene que adivinar.",
        "También conviene usar un vocabulario variado. Si repetimos «cosa» o «muy bueno» muchas veces, el texto se vuelve pobre. Podemos cambiar «cosa» por «objeto», «herramienta» o «juguete», según el caso, y «muy bueno» por «excelente» o «útil». El vocabulario variado hace más rica la exposición, pero debe ser exacto.",
    ],
    [("pronombre", "palabra que reemplaza a otra, como él, ella o eso"), ("referente", "persona o cosa de la que habla un pronombre"), ("explicitar", "decir con claridad lo que antes era dudoso"), ("vocabulario", "conjunto de palabras que uso"), ("sinónimo", "palabra con significado parecido a otra")],
    [
        ("Aclarar un pronombre", "Frase: «Ana habló con Bea y ella se rió». ¿Cómo aclaras quién se rió si fue Bea?", ["Veo que «ella» puede ser Ana o Bea.", "Cambio el pronombre por el nombre.", "Escribo la frase de nuevo."], "«Ana habló con Bea y Bea se rió.»"),
        ("Cambiar una palabra repetida", "Frase: «El juego es muy bueno, y el libro es muy bueno». ¿Cómo la mejoras sin repetir?", ["Veo que «muy bueno» se repite.", "Busco otra palabra exacta.", "Cambio una de las dos."], "«El juego es muy bueno y el libro es excelente.»"),
    ],
    [("Usar «eso» o «lo» sin decir a qué se refiere.", "La audiencia no sabe de qué hablas.", "Nombra el tema: «el reciclaje», «la planta»."), ("Cambiar una palabra por otra que significa algo distinto.", "Se pierde la exactitud.", "Usa palabras que signifiquen casi lo mismo y que encajen.")],
    [
        E("¿«Ella» es un pronombre?", "Sí", "Reemplaza a una persona."),
        E("En «Tomás y Lucas jugaron y él ganó», ¿se sabe quién ganó?", "No", "«Él» puede ser Tomás o Lucas."),
        E("Para aclarar, ¿debo cambiar el pronombre por el nombre?", "Sí", "Así queda claro el referente."),
    ],
    [
        E("¿Qué es el referente de un pronombre?", "La persona o cosa a la que se refiere", "Es lo que el pronombre reemplaza."),
        E("¿Por qué conviene explicitar el referente en una exposición?", "Porque la audiencia no puede preguntar enseguida", "Así nadie se confunde."),
        E("¿Por qué conviene variar el vocabulario?", "Para que el texto sea más rico y no repetitivo", "Evita repetir las mismas palabras."),
    ],
    [
        E("Cambia «eso es importante» por una frase clara sobre cuidar el agua. Elige: a) «Cuidar el agua es importante.» b) «Eso es importante, pues sí.»", "a", "Explicita el referente."),
        E("En «Max le prestó el lápiz a Leo y él lo perdió», ¿a qué se refiere «lo»?", "Al lápiz", "«Lo» reemplaza a «el lápiz»."),
        E("Cambia «cosa» por una palabra más precisa en: «Una cosa para escribir». Elige: a) lápiz b) lluvia", "a", "El lápiz es una herramienta para escribir."),
    ],
    [
        E("Luis dice: «Pedro llamó a Tomás y él vino». Ana dice: «Pedro llamó a Tomás y Tomás vino». ¿Quién explicitó el referente?", "Ana", "Dijo el nombre en vez del pronombre."),
        E("«Excelente» es un sinónimo posible de «muy bueno». ¿Cambia el significado de forma importante?", "No", "Significan casi lo mismo."),
    ],
    [
        E("Mejora esta frase para una exposición: «Ellos lo pusieron allí». Elige la versión que aclara: a) «Los niños pusieron el libro sobre la mesa.» b) «Ellos lo pusieron aquí.»", "a", "Nombra quiénes, qué y dónde."),
        E("Una exposición dice cuatro veces «cosa». ¿Qué conviene hacer: cambiar por palabras exactas o repetir más?", "Cambiar por palabras exactas", "Se enriquece el vocabulario."),
    ],
    [E("En una exposición escuchas: «Cuidar el agua es importante. Eso ayuda a las plantas. Eso también ayuda a los animales». ¿Qué conviene explicitar en la segunda y tercera oración: «Cuidar el agua» o «mañana»?", "Cuidar el agua", "Es lo que ayuda a plantas y animales.")],
    [
        E("¿Un pronombre puede ser confuso?", "Sí", "Si no está claro a quién se refiere."),
        E("¿Cambiar «cosa» por «objeto» puede dar más precisión?", "Sí", "Es más específico según el caso."),
        E("¿Debo nombrar el referente si hay dudas?", "Sí", "Aclara de qué hablo."),
    ],
    ("Aclara y varía. Reescribe estas frases para una exposición: 1) «Tomás y Max jugaron y él ganó» (ganó Max), 2) «Eso es importante» (se habla de leer cada día), 3) «Mi cuaderno es muy bueno y mi lápiz es muy bueno». Usa el nombre o el tema y cambia una palabra repetida.",
     "1) Tomás y Max jugaron y Max ganó. 2) Leer cada día es importante. 3) Mi cuaderno es muy bueno y mi lápiz es excelente.",
     ["explicita el referente", "evita repetir palabras", "mantiene el sentido"], ["hoja con tres frases"], ["dejar «él» o «eso» sin aclarar", "cambiar el sentido"],
     "Si se mantiene el pronombre, pregunta quién o qué es."),
    "Lee un párrafo de un cuento y busca los pronombres que podrían confundir.",
    "Escribe dos frases con un pronombre confuso y corrígelas.",
)

# ================================================================ OA 28 · clase 5
reg(
    OA28, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: un objeto de tu casa y una hoja grande para hacer un papelógrafo.",
    "Aprenderé a ensayar la voz, la postura y el apoyo visual de una exposición. Sirve para hablar con seguridad y para que mi mensaje se vea y se escuche bien.",
    ["Sé ordenar una exposición.", "Sé explicar con claridad."],
    [
        "Cuando exponemos, el cuerpo y la voz comunican. La voz debe ser clara y con volumen suficiente para que todos oigan. El ritmo no debe ser muy rápido: hacemos pausas entre ideas. La postura es la forma de colocar el cuerpo: de pie, con la espalda recta, mirando al público y con las manos tranquilas.",
        "Los gestos ayudan cuando acompañan lo que decimos: señalar un dibujo, mostrar el tamaño con las manos. Pero no deben distraer. Mirar a distintas personas del público muestra interés. No miramos solo el papel ni el suelo. Si me equivoco, respiro, sigo y digo la frase de nuevo.",
        "El material de apoyo es algo que ayuda a explicar, como un papelógrafo (una hoja grande con dibujos y pocas palabras), un objeto o una lámina. Conviene que tenga letra grande, pocas palabras y dibujos claros. Un objeto debe ser seguro y fácil de mostrar: no usamos objetos cortantes ni frágiles. También puede ser una presentación en computador, como PowerPoint: cada diapositiva (cada pantalla) lleva una sola idea, pocas palabras, letra grande y una imagen clara. Si no hay computador, dibujamos cada diapositiva en una hoja. No siempre hace falta material: lo usamos solo si ayuda. No lo leemos entero: lo usamos para mostrar. Ensayar antes, aunque sea frente a un espejo o a una persona de la casa, da seguridad.",
    ],
    [("volumen", "qué tan fuerte suena la voz"), ("ritmo", "rapidez al hablar"), ("postura", "forma de colocar el cuerpo"), ("papelógrafo", "hoja grande con dibujos y pocas palabras"), ("material de apoyo", "objeto, lámina o presentación que ayuda a explicar"), ("diapositiva", "cada pantalla de una presentación en computador, con una sola idea")],
    [
        ("Elegir una buena postura", "Vas a exponer. ¿Qué postura elegirías: a) de pie, espalda recta, mirando al público b) de espaldas al público leyendo?", ["Pienso en el público.", "Veo cuál permite verte y oírte.", "Elijo la que mira al público."], "La a."),
        ("Mejorar un papelógrafo", "Un papelógrafo tiene tres párrafos largos en letra chica. ¿Qué cambias?", ["Reduzco las palabras.", "Aumento el tamaño de la letra.", "Agrego un dibujo."], "Pongo pocas palabras en letra grande y un dibujo claro."),
        ("Una idea por diapositiva", "Una diapositiva de PowerPoint dice: «Las plantas necesitan luz, agua, tierra, aire, abono, espacio, cuidado y tiempo», con dos imágenes diminutas. ¿Qué cambias?", ["Veo que hay muchas ideas juntas.", "Dejo una idea por diapositiva.", "Uso pocas palabras y una imagen clara."], "Hago una diapositiva con «La planta necesita luz» y un dibujo grande del sol."),
    ],
    [("Leer todo el papel mirando al suelo.", "El público no te ve ni te siente.", "Mira a las personas y usa el papel solo como guía."), ("Hablar muy rápido por los nervios.", "No se entiende.", "Respira, haz pausas y baja el ritmo."), ("Llenar la diapositiva o el papelógrafo de texto y leerlo entero.", "El público lee en vez de escucharte.", "Deja pocas palabras y explica con tu voz.")],
    [
        E("¿Qué es el volumen de la voz: qué tan fuerte suena o qué tan rápido?", "Qué tan fuerte suena", "El ritmo es la rapidez."),
        E("¿Qué es un papelógrafo: una hoja grande con dibujos y pocas palabras o un cuaderno pequeño?", "Una hoja grande con dibujos y pocas palabras", "Sirve para mostrar ideas."),
        E("Al exponer, ¿miro al público o solo al suelo?", "Al público", "Muestra interés y seguridad."),
    ],
    [
        E("¿Por qué conviene hacer pausas al exponer?", "Porque ayudan a que el público entienda", "Permiten pensar las ideas."),
        E("¿Qué conviene en cada diapositiva de una presentación: una idea con pocas palabras o un párrafo largo?", "Una idea con pocas palabras", "Así se lee desde lejos y se escucha tu explicación."),
        E("¿Por qué conviene ensayar antes?", "Para tener más seguridad", "Ayuda a corregir y recordar."),
    ],
    [
        E("Un papelógrafo debe tener: a) pocas palabras y letra grande b) un texto muy largo. ¿Cuál es correcta?", "a", "Se debe leer desde lejos."),
        E("Si me equivoco al decir una frase, ¿qué hago: respiro, sigo y la repito, o me quedo callado y me voy?", "Respiro, sigo y la repito", "Un error se corrige y se sigue."),
        E("Una diapositiva tiene seis frases largas y tres imágenes diminutas. ¿Qué conviene: a) dejar una idea, pocas palabras y una imagen clara b) agregar más texto?", "a", "Una idea clara se ve y se entiende mejor."),
    ],
    [
        E("Ana habla bajito y rápido, mirando al piso. Beto habla claro, con pausas y mira al público. ¿Quién comunica mejor?", "Beto", "Su voz y su mirada ayudan."),
        E("Un niño lee las 10 líneas de su papelógrafo en voz alta. ¿Es buen uso del apoyo?", "No", "Se lee todo en lugar de explicar."),
    ],
    [
        arith("Tu exposición dura 3 minutos. La introducción y el cierre ocupan 1 minuto. ¿Cuántos minutos quedan para el desarrollo?", "3-1", "Se restan los minutos ocupados.", " minutos"),
        E("Para ensayar sin público, ¿qué puedes hacer: hablar frente a un espejo o no ensayar?", "Hablar frente a un espejo", "Ayuda a ver tu postura y gestos."),
    ],
    [E("Mañana expones sobre los perros. Tienes una lámina con un dibujo y un objeto, como una correa. ¿Qué es mejor para el apoyo: mostrar la lámina y la correa o solo leer el cuaderno?", "Mostrar la lámina y la correa", "Apoyan lo que explicas.")],
    [
        E("¿Mirar al público es parte de una buena exposición?", "Sí", "Muestra interés y seguridad."),
        E("¿El material de apoyo se lee completo?", "No", "Solo se muestra o se usa de guía."),
        E("¿Respirar ayuda a tener ritmo calmado?", "Sí", "Ayuda a hablar más despacio."),
    ],
    ("Ensaya tu exposición. Elige uno de estos temas: «cómo cuidar una planta» o «cómo jugar al luche». Prepara un apoyo a tu elección: un papelógrafo con pocas palabras y un dibujo, un objeto seguro de tu casa, o tres diapositivas dibujadas en hojas (o hechas en un computador, si tienes uno). Ensaya tres veces tu exposición frente a un espejo o a una persona de tu casa. Marca después tres cosas: tu volumen, tu ritmo y si miraste al público.",
     "Material: un dibujo de una planta con tres palabras: luz, agua, tierra. Ensayo: hablé fuerte, a un ritmo calmado y miré a mi público.",
     ["usa apoyo con pocas palabras", "ensaya voz, ritmo y mirada", "evalúa cómo le salió"], ["papelógrafo u objeto y autoevaluación escrita"], ["leer todo sin mirar", "apoyo con exceso de texto"],
     "Si lee todo el apoyo, pide que lo use solo para mostrar."),
    "Ensaya tu exposición frente a una persona de tu casa y pide un comentario amable sobre tu voz.",
    "Haz un segundo papelógrafo con otro tema y compara cuál comunica mejor.",
)
