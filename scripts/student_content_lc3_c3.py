"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS02 (comunicación oral inicial de ideas y sentimientos con algunas palabras culturalmente significativas) y
OA LS03 (comprensión de textos breves con algunas palabras culturalmente significativas), contexto de sensibilización.

Criterio de autoría: todos los textos, guiones, diálogos, personajes y escuelas son inventados solo para practicar y
están rotulados como tales; las situaciones de comunicación son ficticias para no exponer vida personal. Las únicas
expresiones en lengua indígena son saludos y palabras muy atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka,
mapu). No se evalúa pronunciación ni se exige repetir sonidos, y no se inventa gramática ni significados. Cada tarea
abierta remite al educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS2, LS3 = "LC03 OA LS02", "LC03 OA LS03"

CONSULT = " Recuerda: la forma tradicional de escribir, decir y usar estas palabras la enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de escritura, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

FICHA_SAL = "Ficha: «mari mari» es un saludo y «chaltumay» quiere decir «gracias», ambas en mapuzugun."
FICHA_PAL = "Ficha de palabras en mapuzugun (de práctica): «ko» es agua, «antü» es sol, «kuyen» es luna, «ruka» es la casa mapuche, «mapu» es tierra, «ñuke» es madre."


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement + CONSULT, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback + FEEDBACK_ADD}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# =================================================================== LS02 clase 1 · elegir una situación segura
L(
    LS2, 1,
    materials="Lápiz y hoja. Las situaciones están escritas en este cuaderno; son inventadas. Nadie tiene que contar su vida personal.",
    use="Aprenderé a elegir una situación segura para comunicar una idea o un sentimiento con respeto. Sirve para hablar en clase sin exponer a nadie ni copiar lo que una comunidad cuida.",
    prior=["Sé que cada persona decide qué cuenta de su vida.", "Sé que «mari mari» es un saludo y «chaltumay» es gracias."],
    explain=[
        "Comunicar oralmente es decir en voz alta una idea o un sentimiento. Puedo hacerlo en un diálogo, en una dramatización, en una conversación o en una exposición. Para empezar elijo una situación de práctica: un momento de la vida de la escuela o de la comunidad, que puede ser inventado.",
        "Una situación es segura cuando cumple cuatro cosas. Es voluntaria: nadie me obliga a hablar. No expone datos privados míos ni de otras personas. No imita ni simula ceremonias ni cantos que una comunidad cuida. Y trata con respeto a todos los que participan.",
        "Algunas situaciones seguras son saludar a una visita, agradecer a la educadora o presentar una palabra de la ficha. Si una persona no quiere hablar en voz alta, puede participar de otra forma, como escuchar, escribir su idea o ayudar con un cartel.",
    ],
    vocab=[("situación segura", "momento de práctica que cuida a las personas y a la cultura"), ("voluntaria", "que se hace porque uno quiere"), ("dramatización", "representar una escena como en una pequeña obra"), ("diálogo", "conversación entre dos o más personas"), ("exposición", "presentar un tema en voz alta")],
    worked=[
        W("Elegir la situación segura", "Opciones para dramatizar: A) una visita llega a la sala y todos la reciben con «mari mari». B) el curso simula una ceremonia. ¿Cuál es segura?", ["La B simula algo que una comunidad cuida.", "La A es un saludo de práctica.", "Elijo la A."], "A"),
        W("Revisar las cuatro condiciones", "Un niño quiere contar en voz alta un problema privado de una persona de su casa. ¿Es segura?", ["Reviso: ¿expone datos privados?", "Sí, cuenta un problema de otra persona.", "No cumple la condición, así que no es segura."], "No"),
    ],
    mistakes=[
        M("Pensar que, si una situación es divertida, ya es segura.", "También debe cuidar la privacidad y el respeto.", "Reviso las cuatro condiciones."),
        M("Obligar a un compañero a actuar.", "La participación debe ser voluntaria.", "Le ofrezco otra forma de participar."),
    ],
    R=[
        ex("Situación: saludar a una visita en la sala. ¿Es segura? Sí o No.", "Sí", "Es un momento de respeto y no expone a nadie."),
        ex("Situación: contar a todo el curso un problema privado de una persona de tu casa. ¿Es segura? Sí o No.", "No", "Expone datos privados."),
        ex("Si no quiero hablar frente al curso, ¿es obligatorio hacerlo? Sí o No.", "No", "La participación es voluntaria."),
    ],
    C=[
        ex("Cuatro situaciones: A) agradecer a la educadora. B) imitar una ceremonia. C) presentar un cartel con «mari mari». D) preguntar a un compañero de qué pueblo es. ¿Cuáles son seguras? Escribe las letras.", "A y C", "B imita algo que se cuida y D pide un dato privado."),
        ex("Verdadero o falso: una situación segura puede ser inventada por el curso.", "Verdadero", "Las situaciones de práctica pueden ser ficticias."),
        ex("Una situación segura es voluntaria, no expone datos privados, trata con respeto y ______. Elige: no imita ceremonias o es secreta.", "no imita ceremonias", "Es la cuarta condición."),
    ],
    A=[
        ex("Elige la situación segura para un diálogo: A) dos amigos se saludan con «mari mari» en el recreo. B) un niño cuenta la enfermedad de un familiar.", "A", "La B expone datos privados."),
        ex("Un niño propone que el curso mime un canto que una comunidad cuida. ¿Cuál de las cuatro condiciones de una situación segura no cumple?", "no imitar ni simular ceremonias ni cantos que una comunidad cuida", "Mimar un canto que se cuida es simularlo."),
        ex("Para una dramatización de práctica puedes elegir A) una visita llega a la sala y es recibida con «mari mari», o B) «una visita hace una ceremonia». ¿Cuál eliges?", "A", "La B simula algo que se cuida."),
    ],
    Z=[
        ex("Sofía dice: «Es segura porque es divertida». ¿Alcanza con ser divertida? Sí o No.", "No", "También debe cuidar a las personas."),
        ex("Un compañero no quiere actuar. ¿Qué haces: A) lo obligo. B) le ofrezco otra forma de participar, como escribir su idea.", "B", "La participación es voluntaria."),
    ],
    D=[
        ex("Ordena: A) reviso si expone datos privados. B) pienso varias situaciones. C) elijo la que cumple las cuatro condiciones. Escribe las letras.", "B, A, C", "Pienso, reviso y recién elijo."),
        ex("Tu situación es voluntaria, no expone datos privados y trata con respeto a todos. ¿Qué condición te falta comprobar?", "que no imite ni simule ceremonias ni cantos que una comunidad cuida", "Son cuatro condiciones y esa es la que no revisaste."),
    ],
    context=[ex("Tu curso prepara una dramatización. ¿Qué eliges: «una visita llega y se la recibe con respeto» o «se actúa una celebración de una comunidad»?", "«una visita llega y se la recibe con respeto»", "La otra imita algo que una comunidad cuida.")],
    selfcheck=[
        ex("¿Una situación segura es voluntaria o forzada?", "voluntaria", "Nadie debe ser obligado."),
        ex("¿Puedo contar datos privados de otra persona en una dramatización? Sí o No.", "No", "Debo cuidar su privacidad."),
        ex("¿Qué puedo hacer si no quiero hablar frente al curso?", "participar de otra forma", "Puedo escuchar o escribir mi idea."),
    ],
    task=T(
        "Elige una situación segura de esta lista: a) recibir a una visita con «mari mari», b) agradecer a la educadora con «chaltumay», c) presentar una palabra de la ficha. " + FICHA_SAL + " En tu cuaderno escribe: 1) la situación que elegiste, 2) por qué cumple las cuatro condiciones (voluntaria, sin datos privados, sin imitar ceremonias, con respeto), 3) una forma de participar para quien no quiera hablar. Termina con una pregunta para la educadora tradicional.",
        "Situación: recibir a una visita con «mari mari». Cumple: es voluntaria; no cuenta datos privados; no imita ceremonias; es respetuosa. Otra forma de participar: ayudar a hacer un cartel. Pregunta: ¿cómo se recibe a una visita en su comunidad?",
        ["elige una situación de la lista", "explica las cuatro condiciones", "propone otra forma de participar", "formula una pregunta para el educador/a tradicional"],
        ["texto escrito en el cuaderno", "pregunta escrita o dicha en voz alta"],
        ["elegir una situación que expone datos privados", "simular una ceremonia"],
        "Verifica que justifique las cuatro condiciones; si eligió una situación que imita algo que se cuida, ayúdalo a cambiarla.",
    ),
    reinforce="Con un adulto, nombra tres situaciones seguras y una que no lo sea.",
    extend="Escribe dos situaciones nuevas, una segura y una no segura, y explica la diferencia.",
)

# =================================================================== LS02 clase 2 · escuchar palabras y significado
GUION_V = "Guion para que una persona adulta lea en voz alta (inventado): «Mari mari, niños. Hoy les muestro una jarra con agua. Ustedes pueden escuchar la palabra «ko» y no tienen que repetirla. Chaltumay por escuchar.»"

L(
    LS2, 2,
    materials="Lápiz y hoja. Una persona adulta lee en voz alta el guion que está escrito en este cuaderno.",
    use="Aprenderé a escuchar palabras en lengua indígena y su significado sin que me exijan repetirlas. Sirve para aprender con respeto y para participar con sentido en una conversación.",
    prior=["Sé que no se evalúa a nadie por cómo pronuncia.", "Sé que la ficha dice qué significa una palabra."],
    explain=[
        "Escuchar bien es poner atención al mensaje y a quien habla. Cuando alguien comparte una palabra de su lengua, escucho primero la palabra, después su significado y luego cuándo se usa. No tengo que repetirla en voz alta si no quiero.",
        "Nadie evalúa mi pronunciación ni la de mis compañeros. La pronunciación de una lengua la enseña quien la habla, con paciencia y en persona. Yo no imito sonidos para hacer reír ni corrijo cómo hablan los demás.",
        "Para no perderme algo, uso tres ayudas. Pido que repitan el texto si no lo entendí. Anoto en la ficha la palabra y su significado. Y escribo preguntas para después. Así mi participación es escuchar con atención y preguntar con respeto.",
    ],
    vocab=[("escuchar", "poner atención a lo que se dice"), ("mensaje", "lo que una persona quiere comunicar"), ("pronunciación", "forma de decir los sonidos de una palabra"), ("paciencia", "calma para esperar y aprender"), ("pregunta", "lo que digo o escribo para saber algo")],
    worked=[
        W("Escuchar el guion", GUION_V + " ¿Qué palabra nueva presenta la visita?", ["Escucho las comillas: «ko».", "La visita dice que pueden escuchar «ko».", "La palabra nueva es «ko»."], "«ko»"),
        W("Qué significa", GUION_V + " " + FICHA_PAL + " ¿Qué significa «ko»?", ["La visita muestra una jarra con agua.", "La ficha dice que «ko» es agua.", "Las dos pistas coinciden."], "agua"),
    ],
    mistakes=[
        M("Pensar que, para participar, tengo que repetir cada palabra en voz alta.", "Escuchar con atención también es participar.", "Escucho, pregunto y anoto."),
        M("Corregirle la pronunciación a un compañero.", "La pronunciación la enseña quien habla la lengua.", "Si quiero saber más, le pregunto al educador tradicional."),
    ],
    R=[
        ex(GUION_V + " ¿Qué muestra la visita?", "una jarra con agua", "Lo dice la segunda oración."),
        ex("En el guion, ¿la visita pide a los niños que repitan la palabra? Sí o No.", "No", "Dice que no tienen que repetirla."),
        ex("En el guion, ¿qué palabra dice la visita para terminar?", "chaltumay", "Es lo último que dice."),
    ],
    C=[
        ex(FICHA_SAL + " En el guion, ¿por qué la visita dice «chaltumay» al final?", "para agradecer que escucharan", "La ficha dice que «chaltumay» es gracias."),
        ex("Verdadero o falso: un compañero que no repite la palabra no participa.", "Falso", "Escuchar con atención es participar."),
        ex("Si no entendí una parte del guion, ¿qué hago: pido que la repitan o la invento?", "pido que la repitan", "Así no invento nada."),
    ],
    A=[
        ex("En el guion se oyen «mari mari», «ko» y «chaltumay». ¿Cuál se dice primero?", "mari mari", "La visita empieza saludando."),
        ex("Une cada expresión con su significado. Expresiones: 1) «mari mari», 2) «ko», 3) «chaltumay». Significados: a) agua, b) saludo, c) gracias. Escribe 1-?, 2-?, 3-?", "1-b, 2-a, 3-c", "Según las fichas, mari mari es saludo, ko es agua y chaltumay es gracias."),
        ex("En el guion, ¿cuántas expresiones distintas en lengua indígena se oyen?", "3", "Son «mari mari», «ko» y «chaltumay»."),
    ],
    Z=[
        ex("Diego dice: «Rodrigo dijo mal «ko», se lo voy a corregir». ¿Qué debería hacer en su lugar: A) preguntarle a la educadora cómo se dice. B) corregirlo delante de todos.", "A", "La pronunciación la enseña quien habla la lengua."),
        ex("¿Es respetuoso reírse cuando alguien intenta decir una palabra nueva? Sí o No.", "No", "La burla daña."),
    ],
    D=[
        ex("Ordena las ayudas para escuchar: A) anoto la palabra y su significado. B) pido que repitan si no entendí. C) escribo una pregunta para después. Escribe las letras.", "B, A, C", "Primero aclaro, luego anoto y al final pregunto."),
        ex("Guion nuevo (inventado): «Mari mari. Hoy conoceremos «antü». Pueden escuchar sin repetir.» " + FICHA_PAL + " ¿Qué palabra conoceremos y qué quiere decir?", "«antü», sol", "La ficha dice que antü es sol."),
    ],
    context=[ex("Una visita comparte la palabra «kuyen» y nadie repite. Un compañero dice que así no aprenden. ¿Qué le respondes: que escuchar y preguntar también es aprender, o que sin repetir no se aprende?", "que escuchar y preguntar también es aprender", "Se aprende con atención y con la guía de quien sabe.")],
    selfcheck=[
        ex("¿Debo repetir una palabra en voz alta si no quiero?", "No", "Puedo participar escuchando."),
        ex("¿Quién enseña la pronunciación de una lengua indígena?", "quien la habla", "El educador tradicional o la comunidad."),
        ex("¿Qué hago si no entendí una parte?", "pido que la repitan", "Preguntar es parte de aprender."),
    ],
    task=T(
        "Pide a un adulto que lea en voz alta este guion de práctica inventado: «Mari mari. Hoy les muestro una luna dibujada y una casa mapuche de papel. Pueden escuchar las palabras «kuyen» y «ruka» sin repetirlas. Chaltumay por escuchar.» " + FICHA_PAL + " " + FICHA_SAL + " Mientras escuchas haz una tabla de dos columnas: palabra y significado. Anota las cuatro expresiones que oíste y su significado según las fichas. Termina con una pregunta que no tenga que ver con la pronunciación para el educador o la educadora tradicional.",
        "mari mari: saludo. kuyen: luna. ruka: casa mapuche. chaltumay: gracias. Pregunta: ¿en qué momentos se usa «ruka» en su comunidad?",
        ["anota las cuatro expresiones", "escribe el significado según las fichas", "no inventa pronunciaciones", "formula una pregunta para el educador/a tradicional"],
        ["tabla de cuatro filas", "pregunta escrita o dicha en voz alta"],
        ["inventar una forma de pronunciar", "corregir a otros"],
        "Verifica que anotó las cuatro expresiones con la ficha; si escribió una pronunciación, pídele que la cambie por una pregunta.",
    ),
    reinforce="Con un adulto, escucha de nuevo el guion y confirma tus anotaciones sin repetir ninguna palabra en voz alta.",
    extend="Escribe dos preguntas que podrías hacerle a una visita sobre el significado de una palabra, sin hablar de su pronunciación.",
)

# =================================================================== LS02 clase 3 · idea o sentimiento ficticio
L(
    LS2, 3,
    materials="Lápiz y hoja. Los personajes son inventados. Hablaré por un personaje, así que no cuento nada de mi vida.",
    use="Aprenderé a preparar una idea o un sentimiento de un personaje inventado para decirlo en voz alta. Sirve para practicar la comunicación oral sin exponer mi vida personal.",
    prior=["Sé elegir una situación segura.", "Sé reconocer algunas emociones."],
    explain=[
        "Un sentimiento es lo que siento por dentro, como alegría, gratitud, curiosidad o nervios. Una idea es lo que pienso sobre algo. Para practicar sin contar mi vida, hablo por un personaje ficticio, que es inventado. Así puedo decir lo que siente sin contar datos míos.",
        "Preparo mi mensaje con una estructura de tres partes: «Soy [personaje]», «Siento [emoción] porque [razón]» y, si quiero, una palabra de la ficha, como «mari mari» o «chaltumay». Por ejemplo: Soy Pía. Siento gratitud porque la visita me enseñó una palabra. Digo «chaltumay».",
        "Antes de hablar practico en voz baja y reviso que mi mensaje sea corto, claro y respetuoso. Marco con una pausa la palabra de la ficha para decirla con calma. Si me trabo, puedo leer mi papel: preparar un apoyo escrito es parte de comunicar bien.",
    ],
    vocab=[("sentimiento", "lo que siento por dentro, como alegría"), ("idea", "lo que pienso sobre algo"), ("personaje ficticio", "personaje inventado que no existe en la vida real"), ("razón", "motivo por el que siento o pienso algo"), ("apoyo escrito", "papel con lo que quiero decir")],
    worked=[
        W("Armar un mensaje", "Personaje: Pía. Emoción: gratitud. Razón: la visita le enseñó una palabra. Palabra: «chaltumay». Escribe el mensaje con la estructura de la clase.", ["Empiezo con el personaje: Soy Pía.", "Sigo con la emoción y la razón: Siento gratitud porque la visita me enseñó una palabra.", "Termino con la palabra: Digo «chaltumay»."], "Soy Pía. Siento gratitud porque la visita me enseñó una palabra. Digo «chaltumay»."),
        W("Reconocer emoción y razón", "Mensaje: «Soy Tomás. Siento curiosidad porque quiero saber qué es «ko»». ¿Cuál es la emoción y cuál la razón?", ["Busco «siento»: curiosidad.", "Busco «porque»: quiere saber qué es «ko».", "Separo las dos partes."], "emoción: curiosidad; razón: quiere saber qué es «ko»"),
    ],
    mistakes=[
        M("Usar datos míos o de mi familia en el mensaje.", "El personaje es inventado para cuidar mi privacidad.", "Hablo por el personaje y uso solo sus datos inventados."),
        M("Escribir un mensaje muy largo.", "Se vuelve difícil de recordar y decir con calma.", "Uso la estructura corta de tres partes."),
    ],
    R=[
        ex("Mensaje: «Soy Pía. Siento alegría porque hay visita». ¿Cuál es el personaje?", "Pía", "Dice «Soy Pía»."),
        ex("En el mensaje anterior, ¿qué emoción siente el personaje?", "alegría", "La dice después de «siento»."),
        ex("En ese mensaje, ¿cuál es la razón de la emoción?", "hay visita", "Viene después de «porque»."),
    ],
    C=[
        ex("Verdadero o falso: para practicar puedo hablar por un personaje inventado y no por mí.", "Verdadero", "Así cuido mi privacidad."),
        ex("Mensaje: «Soy Mateo. Siento nervios porque voy a hablar en clase». ¿Cuál es el sentimiento?", "nervios", "Va después de «siento»."),
        ex("Elige la mejor estructura: A) Soy…, siento… porque…, digo… B) Digo… siento… soy…", "A", "Va de más general a más específico."),
    ],
    A=[
        ex("Une cada parte del mensaje con su inicio. Partes: 1) el personaje, 2) la emoción con su razón, 3) la palabra de la ficha. Inicios: a) «Siento…», b) «Digo…», c) «Soy…». Escribe 1-?, 2-?, 3-?", "1-c, 2-a, 3-b", "El personaje empieza con «Soy», la emoción con «Siento» y la palabra con «Digo»."),
        ex("En «Soy Pía. Siento gratitud porque la visita me enseñó una palabra. Digo «chaltumay»», ¿cuántas oraciones hay?", "3", "Cada oración termina en punto: tres."),
        ex("Tu mensaje ya tiene «Soy Lía.» y «Digo «chaltumay».». ¿Qué parte falta?", "la emoción con su razón", "Falta la oración que empieza con «Siento» y tiene un «porque»."),
    ],
    Z=[
        ex("Ana quiere hablar de un problema de una persona de su casa. ¿Qué le sugieres: hablar por un personaje inventado o contar el problema real?", "hablar por un personaje inventado", "Así no expone a nadie."),
        ex("Un mensaje dice: «Soy Tomás. Siento alegría porque sí». ¿Qué le falta de bueno: una razón clara o más personajes?", "una razón clara", "«Porque sí» no explica la emoción."),
    ],
    D=[
        ex("Ordena el mensaje: A) Digo «chaltumay». B) Soy Pía. C) Siento gratitud porque la visita me enseñó una palabra. Escribe las letras.", "B, C, A", "Primero el personaje, luego la emoción y al final la palabra."),
        ex("Mensaje: «Soy Pía. Siento gratitud porque la visita me enseñó una palabra. Digo «mari mari»». Según la ficha, «mari mari» es un saludo. ¿La palabra final calza con la emoción? Sí o No.", "No", "Para expresar gratitud calza «chaltumay», que es gracias."),
    ],
    context=[ex("Tu curso prepara una dramatización de bienvenida. ¿Qué mensaje preparas para tu personaje: «Soy Pía. Siento alegría porque llegó una visita. Digo «mari mari»» o «Digo mari mari»?", "«Soy Pía. Siento alegría porque llegó una visita. Digo «mari mari»»", "Tiene personaje, emoción, razón y palabra.")],
    selfcheck=[
        ex("¿Hablo por mí o por un personaje inventado en esta práctica?", "por un personaje inventado", "Así cuido mi privacidad."),
        ex("¿Qué palabra uso para decir la razón de una emoción?", "porque", "Une la emoción con su motivo."),
        ex("¿Puedo leer mi papel si me trabo?", "Sí", "El apoyo escrito ayuda a comunicar."),
    ],
    task=T(
        "Prepara un mensaje de 3 oraciones para un personaje inventado por ti. Usa esta estructura: «Soy… Siento… porque… Digo…». Elige la emoción de esta lista: alegría, gratitud, curiosidad, nervios. Elige la palabra de la ficha: " + FICHA_SAL + " Practica en voz baja y marca la pausa antes de la palabra de la ficha. Termina con una pregunta para el educador o la educadora tradicional.",
        "Soy Lía. Siento gratitud porque la visita me enseñó una palabra. Digo «chaltumay». Pregunta: ¿cuándo se agradece así en su comunidad?",
        ["escribe las tres oraciones", "usa un personaje inventado", "explica la razón de la emoción", "formula una pregunta para el educador/a tradicional"],
        ["tres oraciones escritas", "pregunta escrita o dicha en voz alta"],
        ["usar datos personales", "olvidar la razón"],
        "Verifica que hable por el personaje; si usó datos propios, ayúdalo a reescribirlos como datos del personaje inventado.",
    ),
    reinforce="Lee en voz baja tu mensaje dos veces y marca la pausa.",
    extend="Prepara un segundo mensaje para el mismo personaje con otra emoción y otra razón.",
)

# =================================================================== LS02 clase 4 · dialogar con apoyo
DIALOGO = "Diálogo de práctica (inventado): 1) Pía: «Mari mari, Tomás.» 2) Tomás: «Mari mari, Pía. ¿Cómo estás?» 3) Pía: «Estoy contenta. Hoy aprendí una palabra: «ko».» 4) Tomás: «¿Qué significa?» 5) Pía: «Según la ficha, «ko» es agua.» 6) Tomás: «Chaltumay por contarme.»"

L(
    LS2, 4,
    materials="Lápiz y hoja. Un compañero o un adulto puede leer el otro papel del diálogo. El diálogo está escrito en este cuaderno.",
    use="Aprenderé a dialogar con una tarjeta de apoyo: tomar turnos, preguntar, responder y agradecer. Sirve para conversar con respeto usando palabras de la ficha.",
    prior=["Sé preparar un mensaje con un personaje.", "Sé que no se evalúa la pronunciación."],
    explain=[
        "Un diálogo es una conversación entre dos o más personas que se turnan para hablar. Cada intervención se llama turno. En un buen diálogo uno habla y el otro escucha; luego cambian. Si pregunto, espero la respuesta; si me preguntan, respondo con calma.",
        "La tarjeta de apoyo es un papel con las palabras de la ficha y sus significados. Si olvido una palabra, miro la tarjeta. Puedo tener también frases para empezar: «Mari mari», «¿Qué significa?», «Según la ficha…» y «Chaltumay por contarme». La tarjeta me ayuda a hablar sin miedo.",
        "Un diálogo respetuoso no corrige la pronunciación, no se burla y no obliga a nadie a repetir. Si el compañero no sabe qué responder, puede decir «no sé» o «lo preguntamos al educador tradicional», y eso también es una buena respuesta.",
    ],
    vocab=[("turno", "momento en que una persona habla en un diálogo"), ("tarjeta de apoyo", "papel con palabras y frases para ayudar a hablar"), ("responder", "decir algo cuando me preguntan"), ("agradecer", "decir gracias"), ("dialogar", "conversar turnándose")],
    worked=[
        W("Contar turnos", DIALOGO + " ¿Cuántos turnos tiene Pía?", ["Busco los turnos de Pía: 1, 3 y 5.", "Cuento: tres.", "Pía habla tres veces."], "3"),
        W("Quién pregunta", DIALOGO + " ¿Qué pregunta hace Tomás sobre la palabra nueva?", ["Busco el signo de pregunta.", "Tomás pregunta en el turno 4.", "Pregunta: ¿Qué significa?"], "¿Qué significa?"),
    ],
    mistakes=[
        M("Hablar los dos a la vez.", "No se entienden las ideas del otro.", "Respeto el turno: uno habla, el otro escucha."),
        M("Decir una respuesta inventada para no quedar callado.", "Podría dar un dato falso sobre una palabra.", "Digo «no sé» o «lo preguntamos al educador»."),
    ],
    R=[
        ex(DIALOGO + " ¿Quién dice «Mari mari» primero?", "Pía", "Es el turno 1."),
        ex("En el diálogo, ¿cuántos turnos tiene Tomás?", "3", "Son los turnos 2, 4 y 6."),
        ex("¿Cuál es la última frase del diálogo?", "Chaltumay por contarme", "Está en el turno 6."),
    ],
    C=[
        ex("En el diálogo, ¿qué responde Pía cuando Tomás pregunta qué significa «ko»?", "Según la ficha, «ko» es agua", "Es el turno 5."),
        ex("Verdadero o falso: si no sé qué responder, puedo decir «no sé» o «lo preguntamos al educador tradicional».", "Verdadero", "Es una respuesta honesta."),
        ex("En el diálogo, ¿para qué dice Tomás «chaltumay»?", "para agradecer a Pía", "La ficha dice que es gracias."),
    ],
    A=[
        ex("En el diálogo, ¿en qué turno agradece Tomás?", "en el 6", "Tomás dice «Chaltumay por contarme» en el último turno."),
        ex("Ordena para armar un diálogo: A) «Según la ficha, «antü» es sol». B) «Mari mari, Lía». C) «¿Qué significa «antü»?». Escribe las letras en el orden más natural.", "B, C, A", "Saludo, pregunta y respuesta."),
        ex("Tu tarjeta de apoyo dice: «ko» es agua. Te preguntan qué significa «ko». ¿Qué respondes?", "agua", "Según la ficha, «ko» es agua."),
    ],
    Z=[
        ex("Diego se queda callado porque no recuerda qué significa «kuyen». ¿Qué puede hacer: mirar su tarjeta de apoyo o inventar?", "mirar su tarjeta de apoyo", "La tarjeta está para ayudar."),
        ex("Un compañero dice «ko» distinto a como lo dijo la visita. ¿Qué haces: lo corrijo o sigo el diálogo con respeto?", "sigo el diálogo con respeto", "No evalúo la pronunciación."),
    ],
    D=[
        ex("Ordena los turnos: A) Tomás: «Chaltumay por contarme». B) Pía: «Mari mari». C) Tomás: «¿Qué significa?». D) Pía: «Según la ficha, es agua». Escribe las letras.", "B, C, D, A", "Saludo, pregunta, respuesta y agradecimiento."),
        ex("Elige el cierre más respetuoso de un diálogo. A) «Chaltumay por contarme». B) «Lo dijiste mal, otra vez».", "A", "La B corrige y se burla; la A agradece."),
    ],
    context=[ex("En una dramatización un niño pregunta qué es «ruka» y su compañera no lo recuerda. ¿Qué dice ella: «No lo recuerdo, miro mi tarjeta» o «Es una comida»?", "«No lo recuerdo, miro mi tarjeta»", "Es honesto y no inventa.")],
    selfcheck=[
        ex("¿Cómo se llama el momento en que una persona habla en un diálogo?", "turno", "Los turnos se alternan."),
        ex("¿Para qué sirve la tarjeta de apoyo?", "para ayudar a hablar", "Trae palabras y frases de ayuda."),
        ex("¿Puedo corregir la pronunciación de mi compañero?", "No", "Eso lo enseña quien habla la lengua."),
    ],
    task=T(
        "Escribe un diálogo de práctica de 6 turnos entre dos personajes inventados, por ejemplo Lía y Mateo. Debe tener: un saludo con «mari mari», una pregunta sobre qué significa una palabra de la ficha (" + FICHA_PAL + "), una respuesta que empiece con «Según la ficha…» y un agradecimiento con «chaltumay» (" + FICHA_SAL + "). Haz también una tarjeta de apoyo con dos palabras y sus significados. Lee el diálogo con un compañero o un adulto. Termina con una pregunta para el educador tradicional.",
        "1) Lía: «Mari mari, Mateo.» 2) Mateo: «Mari mari, Lía.» 3) Lía: «Hoy aprendí «kuyen».» 4) Mateo: «¿Qué significa?» 5) Lía: «Según la ficha, es luna.» 6) Mateo: «Chaltumay por contarme.» Tarjeta: kuyen = luna; ko = agua. Pregunta: ¿cuándo se dice esta palabra en su comunidad?",
        ["escribe los seis turnos", "incluye saludo, pregunta, respuesta con «según la ficha» y agradecimiento", "hace una tarjeta de apoyo", "formula una pregunta para el educador/a tradicional"],
        ["diálogo escrito", "tarjeta de apoyo y lectura en voz alta"],
        ["inventar un significado", "obligar a un compañero a repetir"],
        "Verifica que todos los significados vengan de la ficha; si inventó uno, pídele que lo reemplace por una pregunta.",
    ),
    reinforce="Lee el diálogo de práctica con un adulto, turnándose, y respeta cada turno.",
    extend="Agrega dos turnos más al diálogo con otra palabra de la ficha y su significado.",
)

# =================================================================== LS02 clase 5 · revisar respeto y contexto
L(
    LS2, 5,
    materials="Lápiz y hoja. Los diálogos son de práctica e inventados.",
    use="Aprenderé a revisar si una conversación fue respetuosa y si las palabras se usaron en el contexto correcto. Sirve para mejorar mi comunicación oral y cuidar a las personas.",
    prior=["Sé dialogar con una tarjeta de apoyo.", "Sé que cada palabra de la ficha tiene un significado."],
    explain=[
        "Revisar es mirar de nuevo lo que hice y ver qué puedo mejorar. Después de un diálogo me hago preguntas con una lista: ¿Hablé por turnos? ¿Obligué a alguien a repetir? ¿Evalué la pronunciación de otra persona? ¿Usé castellano respetuoso? ¿Usé la palabra donde corresponde? ¿Dije de dónde viene la palabra?",
        "El contexto es la situación en que se dice algo. Si la ficha dice que «mari mari» es un saludo, tiene sentido usarla cuando alguien llega, no para decir gracias. Si la ficha dice que «chaltumay» es gracias, la uso para agradecer, no para saludar. Usar una palabra fuera de su contexto la deja sin sentido.",
        "Si encuentro un error, lo cuento con calma: «Me di cuenta de que usé esta palabra donde no correspondía». Corregir un error no me hace menos; muestra que aprendo y respeto a las personas y a la lengua.",
    ],
    vocab=[("revisar", "mirar de nuevo para mejorar"), ("lista de revisión", "preguntas que compruebo una por una"), ("contexto", "situación en que se dice algo"), ("fuera de contexto", "usado donde no corresponde"), ("corregir", "cambiar un error por lo correcto")],
    worked=[
        W("Detectar un uso fuera de contexto", FICHA_SAL + " Un niño dice «chaltumay» cuando llega una visita para saludarla. ¿Está en el contexto correcto?", ["La ficha dice que «chaltumay» es gracias.", "Para saludar la ficha trae «mari mari».", "El uso no coincide con el contexto."], "No: «chaltumay» es gracias, no un saludo"),
        W("Aplicar la lista de revisión", "Diálogo: dos niños se turnaron, nadie fue obligado a repetir y se nombró la ficha, pero uno dijo «mari mari» para dar las gracias. ¿Qué pregunta de la lista no se cumplió?", ["Se turnaron: sí.", "Nadie fue obligado: sí. Se nombró la fuente: sí.", "«Mari mari» es un saludo: no se usó donde corresponde."], "la de usar cada palabra donde corresponde"),
    ],
    mistakes=[
        M("Usar una palabra solo porque suena bonita, sin mirar su significado.", "Puede quedar fuera de contexto.", "Reviso la ficha antes de usarla."),
        M("Esconder un error para no quedar mal.", "Así no puedo mejorar.", "Lo cuento con calma y lo corrijo."),
    ],
    R=[
        ex(FICHA_SAL + " ¿Qué palabra uso para saludar al llegar una visita?", "mari mari", "Según la ficha, es un saludo."),
        ex("¿Qué palabra uso para agradecer?", "chaltumay", "Según la ficha, es gracias."),
        ex("Si me equivoco, ¿lo escondo o lo corrijo con calma?", "lo corrijo con calma", "Así puedo aprender y mejorar."),
    ],
    C=[
        ex("Verdadero o falso: usar una palabra fuera de su contexto puede dejarla sin sentido.", "Verdadero", "El contexto da el sentido."),
        ex("Un niño dice «mari mari» al despedirse para dar las gracias. ¿Coincide con la ficha? Sí o No.", "No", "La ficha dice que «mari mari» es un saludo y no un agradecimiento."),
        ex("¿Qué pregunta de la lista es sobre respeto: «¿Obligué a alguien a repetir?» o «¿Cuántas palabras dije?»", "¿Obligué a alguien a repetir?", "Revisa si respeté la voluntad del otro."),
    ],
    A=[
        ex("En tu diálogo cumpliste todas las preguntas de la lista menos «¿Usé cada palabra donde corresponde?». ¿Qué debes mejorar?", "usar cada palabra donde corresponde", "Es la única pregunta que no cumpliste."),
        ex("Diálogo: A dice «Chaltumay» al llegar. B responde «Mari mari» al recibir un regalo. ¿Cuántos usos están fuera de contexto según la ficha?", "2", "Los dos intercambiaron el sentido de sus palabras."),
        ex("Elige la mejor revisión: A) «Mi diálogo estuvo perfecto, no reviso nada». B) «Me turné, pero usé «mari mari» fuera de contexto; lo corrijo».", "B", "La B revisa con honestidad."),
    ],
    Z=[
        ex("Pedro corrigió la pronunciación de una compañera. En la lista de revisión, ¿qué pregunta no cumplió: la de evaluar la pronunciación o la de turnos?", "evaluar la pronunciación", "No se evalúa la pronunciación de otros."),
        ex("Una niña dice «ko» para hablar del sol. Según la ficha, ¿qué palabra correspondía?", "antü", "«Ko» es agua y «antü» es sol."),
    ],
    D=[
        ex("Ordena: A) corrijo el error con calma. B) reviso mi diálogo con la lista. C) conversé con mi compañero. Escribe las letras.", "C, B, A", "Primero converso, luego reviso y después corrijo."),
        ex("Dos diálogos. A) Se turnaron y dijeron «mari mari» al llegar. B) Se turnaron, pero uno dijo «chaltumay» al llegar para saludar. ¿Cuál cumple mejor la lista de revisión?", "A", "En B una palabra se usó fuera de contexto."),
    ],
    context=[ex("Después de una dramatización, tu profesora te pide que cuentes qué mejorarías. ¿Qué dices: «Mejoraría usar «chaltumay» solo para agradecer» o «No mejoraría nada»?", "«Mejoraría usar «chaltumay» solo para agradecer»", "Reconoce un error de contexto.")],
    selfcheck=[
        ex("¿Qué dos cosas reviso en un diálogo además del respeto?", "el contexto y la fuente", "Son dos preguntas de la lista."),
        ex("¿Una palabra de la ficha se puede usar para cualquier situación?", "No", "Debe coincidir con su significado."),
        ex("¿Corregir un error me hace quedar mal o me ayuda a aprender?", "me ayuda a aprender", "Corregir es parte de mejorar."),
    ],
    task=T(
        "Revisa este diálogo de práctica inventado con una lista de seis preguntas: 1) ¿Hubo turnos? 2) ¿Se obligó a repetir? 3) ¿Se evaluó la pronunciación? 4) ¿Se usó castellano respetuoso? 5) ¿Se usó cada palabra donde corresponde? 6) ¿Se dijo la fuente? Diálogo: «Ana: Mari mari, Tomás. Tomás: Chaltumay, Ana. Ana: Según la ficha, mari mari es un saludo.» " + FICHA_SAL + " Responde sí o no a cada pregunta y explica con una frase la que no se cumple. Termina con una pregunta para el educador tradicional.",
        "1 sí; 2 no; 3 no; 4 sí; 5 no (Tomás dijo «chaltumay» como saludo); 6 sí (Ana dijo según la ficha). Pregunta: ¿cómo responde una persona a un saludo en su comunidad?",
        ["responde las seis preguntas", "explica la que no se cumple", "usa la ficha para el contexto", "formula una pregunta para el educador/a tradicional"],
        ["lista de revisión completada", "pregunta escrita o dicha en voz alta"],
        ["no detectar el uso fuera de contexto", "inventar significados"],
        "Comprueba que detecte el uso de «chaltumay» como saludo; si no lo vio, vuelve con él a la ficha.",
    ),
    reinforce="Lee de nuevo el diálogo y señala con color el turno en que un uso no coincidió con la ficha.",
    extend="Haz tu propia lista de revisión de seis preguntas para un diálogo de tu curso.",
)

# =================================================================== LS03 clase 1 · identificar procedencia
TXT_P = "Texto P (inventado): Título: «La jarra de agua». Imagen: un dibujo de una jarra y un vaso. Texto: «Pía llenó una jarra con agua para la visita. La visita escribió «ko» en la pizarra y dijo que esa palabra nombra el agua. Pía dijo «chaltumay».»"
FICHA_P = "Ficha de procedencia del texto P (inventada): Escrito por: el curso de una Escuela Ejemplo. Fuente de las palabras en lengua indígena: la ficha de palabras de la clase. Permiso: sí, para usar en la sala. Para qué: practicar la lectura."

L(
    LS3, 1,
    materials="Lápiz y hoja. Los textos, las imágenes descritas y las fichas están escritos aquí; son inventados.",
    use="Aprenderé a identificar de dónde viene un texto mirando su título, su imagen y su ficha. Sirve para empezar a leer con respeto antes de interpretar las palabras.",
    prior=["Sé qué es la fuente de una palabra.", "Sé leer un texto breve con expresiones entre comillas."],
    explain=[
        "Antes de leer un texto miro su título, su imagen y su ficha. El título dice de qué trata. La imagen da pistas de lo que ocurre. La ficha dice quién escribió el texto, de dónde vienen las palabras en lengua indígena, si hay permiso y para qué se escribió.",
        "Esos datos forman la procedencia del texto. Con ellos puedo decir si un texto es inventado para practicar, si es de una comunidad o si es de una institución. Y puedo saber si puedo usarlo o si tengo que pedir permiso antes.",
        "Si un texto no trae ficha o la ficha no dice la fuente, me detengo y pregunto. No supongo de qué pueblo es ni invento quién lo escribió. Identificar la procedencia es el primer paso para comprender bien un texto con palabras culturalmente significativas.",
    ],
    vocab=[("título", "nombre de un texto"), ("imagen", "dibujo o foto que acompaña un texto"), ("procedencia", "de dónde viene un texto"), ("ficha", "papel con datos de un texto"), ("tema", "de qué trata un texto")],
    worked=[
        W("Leer título e imagen", TXT_P + " ¿De qué trata probablemente el texto, según su título y su imagen?", ["El título dice «La jarra de agua».", "La imagen muestra una jarra y un vaso.", "Probablemente trata del agua y de una visita."], "del agua y de una visita"),
        W("Leer la procedencia", TXT_P + " " + FICHA_P + " ¿Quién escribió el texto P?", ["Busco «Escrito por» en la ficha.", "Dice: el curso de una Escuela Ejemplo.", "Esa es la procedencia."], "el curso de una Escuela Ejemplo"),
    ],
    mistakes=[
        M("Empezar a leer sin mirar título, imagen ni ficha.", "Se pierden pistas importantes.", "Miro título, imagen y ficha antes del texto."),
        M("Suponer de qué pueblo es un texto sin ficha.", "Puedo equivocarme y atribuir mal.", "Me detengo y pregunto."),
    ],
    R=[
        ex(TXT_P + " ¿Cuál es el título del texto P?", "La jarra de agua", "Está marcado como título."),
        ex("¿Qué muestra la imagen del texto P?", "una jarra y un vaso", "La describe el texto."),
        ex("¿Qué palabra de la lengua indígena escribió la visita en la pizarra?", "ko", "Está en el texto."),
    ],
    C=[
        ex(FICHA_P + " ¿Para qué se escribió el texto P?", "para practicar la lectura", "Lo dice la ficha."),
        ex("Verdadero o falso: el texto P viene de una comunidad indígena real.", "Falso", "La ficha dice que lo escribió el curso de una Escuela Ejemplo."),
        ex("La ficha del texto P, ¿dice si hay permiso para usarlo en la sala? Sí o No.", "Sí", "La línea Permiso dice sí."),
    ],
    A=[
        ex(TXT_P + " Si el título fuera «La luna en la noche» y la imagen fuera un dibujo de una luna, ¿de qué trataría probablemente?", "de la luna", "Título e imagen coinciden."),
        ex("Una ficha completa tiene 4 datos: quién lo escribió, fuente de las palabras, permiso y para qué. Una ficha incompleta solo trae quién lo escribió. ¿Qué tres datos faltan?", "la fuente de las palabras, el permiso y para qué se escribió", "Son los datos que la ficha completa tiene y la incompleta no."),
        ex("Ficha Q (inventada): Escrito por: un niño del curso. Fuente de las palabras: no se indica. Permiso: no se indica. ¿Qué haces: usas las palabras o preguntas a una fuente?", "pregunto a una fuente", "Sin fuente no sé si puedo usar las palabras."),
    ],
    Z=[
        ex("Ana dice: «El texto P es de un pueblo originario porque tiene la palabra «ko»». ¿Tiene razón? Sí o No.", "No", "La ficha dice que lo escribió el curso."),
        ex("Dos pistas para saber de qué trata un texto son el título y la imagen. ¿Cuál es la tercera que me da la ficha: la fuente o el color del papel?", "la fuente", "La ficha trae el origen de las palabras."),
    ],
    D=[
        ex("Ordena los pasos antes de leer: A) leo el texto. B) miro la ficha. C) miro el título y la imagen. Escribe las letras.", "C, B, A", "Primero título e imagen, luego la ficha y después el texto."),
        ex("Un texto trae el título «Gracias a la visita» y no tiene ficha. ¿Qué dato no puedes afirmar: el tema probable o de qué pueblo es?", "de qué pueblo es", "Sin ficha no puedo atribuirlo."),
    ],
    context=[ex("En la biblioteca de tu escuela encuentras un papel con un texto y la palabra «ruka», sin ficha. ¿Qué haces primero: lo copias a un cartel o preguntas a la bibliotecaria de dónde viene?", "preguntas de dónde viene", "Sin procedencia no lo uso.")],
    selfcheck=[
        ex("¿Qué miro antes de leer un texto: título, imagen y ficha, o solo el final?", "título, imagen y ficha", "Dan pistas de qué trata y de dónde viene."),
        ex("¿Qué dato de la ficha dice si puedo usar las palabras?", "el permiso", "Autoriza el uso."),
        ex("¿Qué hago si el texto no trae ficha?", "pregunto", "No debo suponer de dónde viene."),
    ],
    task=T(
        "Lee este texto inventado para practicar. Título: «Una tarde con la educadora». Imagen: un dibujo de niños sentados en círculo. Texto: «Los niños escucharon a la educadora tradicional. Ella dijo «mari mari» y mostró una hoja con la palabra «antü». Dijo que esa palabra nombra el sol.» " + FICHA_SAL + " " + FICHA_PAL + " Escribe en tu cuaderno: 1) el título, 2) lo que muestra la imagen, 3) de qué trata, 4) una pregunta que le harías a la ficha (por ejemplo, quién escribió el texto) y 5) una pregunta para la educadora tradicional.",
        "Título: «Una tarde con la educadora». Imagen: niños sentados en círculo. Trata de una visita que enseña una palabra. Pregunta a la ficha: ¿quién escribió el texto? Pregunta a la educadora: ¿cuándo se usa «antü» en su comunidad?",
        ["identifica título e imagen", "dice de qué trata", "formula una pregunta sobre la ficha", "formula una pregunta para el educador/a tradicional"],
        ["cinco líneas escritas", "pregunta escrita o dicha en voz alta"],
        ["suponer el pueblo del texto", "inventar la fuente"],
        "Observa que usa título, imagen y ficha; si supuso el pueblo, pídele que lo cambie por una pregunta.",
    ),
    reinforce="Lee solo el título y la imagen del texto P y di de qué crees que trata.",
    extend="Crea un título y describe una imagen para un texto de práctica que incluya «chaltumay».",
)

# =================================================================== LS03 clase 2 · anticipar sin estereotipos
L(
    LS3, 2,
    materials="Lápiz y hoja. Los títulos, las imágenes descritas y los textos son inventados.",
    use="Aprenderé a anticipar de qué trata un texto usando pistas y sin caer en estereotipos. Sirve para leer con la mente abierta y comprobar mis ideas con el texto.",
    prior=["Sé identificar título, imagen y procedencia.", "Sé que un estereotipo es una idea fija sobre un grupo."],
    explain=[
        "Anticipar es pensar, antes de leer, de qué podría tratar un texto. Para hacerlo uso solo pistas del título, la imagen y las palabras destacadas. Por ejemplo, el título «Una visita a la sala» me hace pensar en una persona que llega y en niños que la reciben.",
        "Un estereotipo es una idea fija y simple sobre un grupo de personas, como «todos los indígenas viven en el campo» o «siempre usan un mismo tipo de ropa». Los estereotipos son falsos porque cada persona es distinta, y hoy muchas personas de pueblos originarios viven en ciudades y trabajan en todo tipo de oficios.",
        "Por eso mi anticipación debe salir de las pistas, no de ideas fijas. Después de leer, compruebo: ¿mi idea coincidió con el texto? Si no coincidió, la cambio. Equivocarme al anticipar no es un problema; es parte de leer con atención.",
    ],
    vocab=[("anticipar", "pensar de qué trata un texto antes de leerlo"), ("pista", "dato del título o la imagen que ayuda a anticipar"), ("estereotipo", "idea fija y simple sobre un grupo"), ("comprobar", "revisar si una idea coincide con el texto"), ("prejuicio", "idea que se tiene antes de conocer")],
    worked=[
        W("Anticipar con pistas", "Título: «Una tarde de visita». Imagen: una mesa con una jarra y vasos. ¿Qué puedes anticipar: que una visita comparte algo con el curso o que hay una fiesta de disfraces?", ["Miro las pistas: visita, mesa, jarra y vasos.", "Pienso en lo que sale del título y la imagen.", "No hay pistas de disfraces."], "que una visita comparte algo con el curso"),
        W("Detectar un estereotipo", "Un niño dice: «Seguro que el texto habla de personas con plumas, porque son indígenas». ¿Qué error comete?", ["Usa una idea fija sobre un grupo.", "No usa pistas del título ni de la imagen.", "Eso es un estereotipo."], "usa un estereotipo en lugar de pistas"),
    ],
    mistakes=[
        M("Anticipar usando una idea fija sobre un pueblo.", "Es un estereotipo y puede ser falsa.", "Uso solo pistas del título y la imagen."),
        M("Defender mi anticipación aunque el texto diga otra cosa.", "Comprobar es parte de leer.", "Cambio mi idea si el texto no la apoya."),
    ],
    R=[
        ex("Título: «Una visita a la sala». ¿Qué pista da el título: una visita o una carrera?", "una visita", "El título lo dice."),
        ex("Verdadero o falso: un estereotipo es una idea fija y simple sobre un grupo.", "Verdadero", "Esa es su definición."),
        ex("Después de leer, ¿comparo mi anticipación con el texto? Sí o No.", "Sí", "Así compruebo si coincidió."),
    ],
    C=[
        ex("Título: «Gracias, educadora». Imagen: una tarjeta con un corazón. ¿Qué anticipas: que alguien agradece o que alguien se despide para siempre?", "que alguien agradece", "El título lo dice."),
        ex("¿Cuál anticipación usa pistas? A) «Trata de agua, porque la imagen tiene una jarra». B) «Trata de lo que todos los indígenas hacen».", "A", "La B usa un estereotipo."),
        ex("Luis dice: «Seguro que los personajes viven en el campo». ¿Qué le falta a su idea: una pista del texto o más imaginación?", "una pista del texto", "No tiene pista."),
    ],
    A=[
        ex("Cambia el estereotipo por una pregunta: «Todos los indígenas viven en el campo». Elige: A) «¿Dónde ocurre este texto?». B) «Seguro que en el campo».", "A", "La pregunta se responde con el texto."),
        ex("Título: «La luna y la jarra». Imagen: una luna y una jarra con agua. ¿Cuáles dos cosas anticipas que aparecen en el texto?", "la luna y el agua", "Son las pistas de la imagen."),
        ex("Anticipación: «El texto habla de una visita». Al leer, el texto habla de una visita. ¿Tu anticipación coincidió? Sí o No.", "Sí", "El texto confirma tu idea."),
    ],
    Z=[
        ex("Ana dice: «Hoy muchas personas de pueblos originarios viven en ciudades». ¿Esa frase es un estereotipo o desmiente uno?", "desmiente uno", "Muestra que no todos viven en el campo."),
        ex("Pedro anticipó que el texto habla de la luna, pero habla del sol. ¿Qué debe hacer: cambiar su idea o insistir?", "cambiar su idea", "Comprobar es parte de leer."),
    ],
    D=[
        ex("Ordena los pasos: A) leo y comparo con mi anticipación. B) miro el título y la imagen. C) anticipo con pistas. Escribe las letras.", "B, C, A", "Miro, anticipo y comparo."),
        ex("¿Cuál frase reemplaza mejor «Los indígenas siempre usan lo mismo»? A) «Cada persona es distinta». B) «Casi todos usan lo mismo».", "A", "Desmiente el estereotipo sin generalizar."),
    ],
    context=[ex("En tu sala todos anticipan un texto con título «Mari mari, visita». Un niño dice: «Seguro habla de plumas». ¿Qué le propones: mirar el título y la imagen o seguir con su idea?", "mirar el título y la imagen", "Son las pistas reales.")],
    selfcheck=[
        ex("¿De dónde debe salir mi anticipación: de pistas o de ideas fijas?", "de pistas", "Del título, la imagen y las palabras."),
        ex("¿Qué hago si mi anticipación no coincide con el texto?", "cambio mi idea", "Comprobar es parte de leer."),
        ex("¿Cómo se llama la idea fija y simple sobre un grupo?", "estereotipo", "Ignora que cada persona es distinta."),
    ],
    task=T(
        "Lee estos tres títulos de textos de práctica con su imagen descrita: 1) «Una jarra para la visita» (imagen: una jarra con agua), 2) «La luna de la sala» (imagen: una luna dibujada), 3) «Gracias, educadora» (imagen: una tarjeta). Para cada uno escribe una anticipación de una línea que use solo las pistas. Elige un título y escribe una frase que desmienta un estereotipo, por ejemplo con «cada persona es distinta». " + FICHA_PAL + " Termina con una pregunta para la educadora tradicional.",
        "1) Anticipo que habla de agua y de una visita. 2) Anticipo que habla de la luna. 3) Anticipo que alguien agradece. Estereotipo desmentido: cada persona es distinta. Pregunta: ¿qué cuentan de la luna en su comunidad?",
        ["escribe tres anticipaciones con pistas", "no usa estereotipos", "desmiente un estereotipo", "formula una pregunta para el educador/a tradicional"],
        ["tres líneas de anticipación", "pregunta escrita o dicha en voz alta"],
        ["usar una idea fija sobre un pueblo", "inventar significados"],
        "Verifica que cada anticipación nombre una pista; si usó una idea fija, ayúdalo a reformularla como pregunta.",
    ),
    reinforce="Elige un título del cuaderno y di en voz alta tu anticipación usando la frase «Veo en el título que…».",
    extend="Escribe un título y una imagen para un texto de práctica y pide a un compañero que anticipe qué trata.",
)

# =================================================================== LS03 clase 3 · localizar palabras y pistas
TXT_R = "Texto R (inventado): «Pía puso una casita de papel sobre la mesa. Tenía techo y puerta. La visita dijo que la palabra «ruka» nombra la casa mapuche. Pía dibujó el sol sobre el techo y escribió «antü».»"

L(
    LS3, 3,
    materials="Lápiz y hoja. El texto y la ficha están escritos aquí; son inventados.",
    use="Aprenderé a localizar palabras culturalmente significativas y las pistas que ayudan a entender su significado. Sirve para comprender un texto sin inventar ni adivinar lo que dice.",
    prior=["Sé anticipar con pistas.", "Sé que la ficha dice qué significa una palabra."],
    explain=[
        "Una pista es una parte del texto que ayuda a entender algo. Pueden ser palabras cercanas, una descripción o un dibujo. Si el texto dice «una casita con techo y puerta» y luego muestra la palabra «ruka», tengo una pista de que «ruka» se relaciona con una casa.",
        "Para localizar hago tres pasos. Primero subrayo la palabra culturalmente significativa. Segundo busco, alrededor, palabras o descripciones que expliquen. Tercero confirmo con la ficha. Si la pista y la ficha dicen lo mismo, mi comprensión es segura; si no, pregunto.",
        "Una palabra no es decoración. Si la leo, la explico con la ficha y con una pista del texto. Y si el texto no da ninguna pista ni hay ficha, no invento su significado: anoto una pregunta para el educador o la educadora tradicional.",
    ],
    vocab=[("pista", "parte del texto que ayuda a entender algo"), ("localizar", "encontrar algo dentro del texto"), ("confirmar", "comprobar con otra fuente"), ("descripción", "palabras que dicen cómo es algo"), ("subrayar", "marcar con una línea lo importante")],
    worked=[
        W("Pista que explica", TXT_R + " ¿Qué pista del texto ayuda a entender la palabra «ruka»?", ["Busco las palabras cercanas a «ruka».", "El texto dice «una casita con techo y puerta».", "Esa es la pista."], "«una casita con techo y puerta»"),
        W("Confirmar con la ficha", TXT_R + " " + FICHA_PAL + " ¿Qué dice la ficha de «antü»? ¿Coincide con la pista del sol?", ["La ficha dice que «antü» es sol.", "En el texto, Pía dibuja el sol y escribe «antü».", "Coinciden."], "sí; antü es sol"),
    ],
    mistakes=[
        M("Elegir un significado solo porque suena parecido.", "Puede no tener relación con la palabra.", "Busco pistas y confirmo con la ficha."),
        M("Dar por cierto un significado sin pistas ni ficha.", "Estaría inventando.", "Anoto una pregunta para el educador tradicional."),
    ],
    R=[
        ex(TXT_R + " ¿Qué puso Pía sobre la mesa?", "una casita de papel", "Es lo que dice la primera oración."),
        ex("En el texto R, ¿cuántas palabras en lengua indígena aparecen entre comillas?", "2", "Son «ruka» y «antü»."),
        ex("En el texto R, ¿qué dibujó Pía sobre el techo?", "el sol", "Lo dice la última oración."),
    ],
    C=[
        ex(FICHA_PAL + " En el texto R, ¿qué quiere decir «ruka» según la ficha?", "la casa mapuche", "La ficha lo dice."),
        ex("Verdadero o falso: la descripción «con techo y puerta» es una pista de la palabra «ruka» en el texto R.", "Verdadero", "Describe una casita."),
        ex("¿Qué dos cosas uso para entender una palabra: pista del texto y ficha, o solo mi memoria?", "pista del texto y ficha", "Son fuentes comprobables."),
    ],
    A=[
        ex("Texto S (inventado): «La visita llenó un vaso con agua. Dijo que «ko» nombra lo que había en el vaso.» " + FICHA_PAL + " ¿Cuál es la pista que acerca a «ko»?", "el vaso con agua", "El texto muestra el agua."),
        ex("En el texto R, ¿qué dos palabras de lengua indígena se explican con pistas del propio texto?", "ruka y antü", "Se describe una casita con techo y puerta y se dibuja el sol."),
        ex("Texto V (inventado): «Pía dibujó un sol y escribió «antü». Después escribió «mapu» en el borde de la hoja, sin decir nada más.» ¿Para cuál palabra el texto no da ninguna pista?", "mapu", "Para «antü» está el dibujo del sol; para «mapu» no hay nada."),
    ],
    Z=[
        ex("Ana lee «kuyen» en un texto sin pistas ni ficha y dice «seguro es una comida». ¿Qué debería hacer: preguntar o seguir con esa idea?", "preguntar", "Sin pista ni ficha no puede afirmar nada."),
        ex("El texto R dice que Pía dibujó el sol. ¿Esa pista sola basta para estar segura de qué significa «antü», sin mirar la ficha? Sí o No.", "No", "Hay que confirmar con la ficha."),
    ],
    D=[
        ex("Ordena los pasos: A) confirmo con la ficha. B) busco pistas alrededor. C) subrayo la palabra. Escribe las letras.", "C, B, A", "Subrayo, busco y confirmo."),
        ex("Texto T (inventado): «La visita escribió «mapu» y mostró un puñado de tierra. Dijo que esa palabra nombra lo que tenía en la mano.» " + FICHA_PAL + " ¿Qué significa «mapu»?", "tierra", "La pista y la ficha coinciden."),
    ],
    context=[ex("En un cartel dice: «La ruka es acogedora». Al lado hay un dibujo de una casa mapuche. ¿Qué pista dibujada ayuda a entender «ruka»?", "el dibujo de una casa mapuche", "Muestra lo que nombra la palabra.")],
    selfcheck=[
        ex("¿Cómo se llama la parte del texto que ayuda a entender algo?", "pista", "Orienta la comprensión."),
        ex("¿Con qué confirmo lo que creo que significa una palabra?", "con la ficha", "La ficha da el significado."),
        ex("Si no hay pista ni ficha, ¿invento el significado?", "No", "Anoto una pregunta."),
    ],
    task=T(
        "Lee este texto de práctica inventado: «Mateo puso una jarra con agua en la mesa. La visita escribió «ko» y dijo que esa palabra nombra lo que hay en la jarra. Después miró la luna por la ventana y escribió «kuyen».» " + FICHA_PAL + " Haz una tabla de tres columnas: palabra, pista del texto y significado según la ficha. Termina con una pregunta que no esté respondida en el texto para la educadora tradicional.",
        "ko / jarra con agua / agua. kuyen / miró la luna por la ventana / luna. Pregunta: ¿cuándo usan estas palabras en su comunidad?",
        ["localiza las dos palabras", "escribe una pista del texto para cada una", "confirma el significado con la ficha", "formula una pregunta para el educador/a tradicional"],
        ["tabla de tres columnas", "pregunta escrita o dicha en voz alta"],
        ["inventar un significado sin ficha", "dar una pista que el texto no tiene"],
        "Comprueba que cada pista salga del texto; si inventó una pista, pídele que subraye la frase real.",
    ),
    reinforce="Subraya con dos colores la palabra «ruka» y su pista en el texto R.",
    extend="Escribe un texto de tres oraciones con una palabra de la ficha y una pista que ayude a entenderla.",
)

# =================================================================== LS03 clase 4 · relacionar información y respuesta
TXT_U = "Texto U (inventado): «Lía quería agradecer a la visita. Escribió «chaltumay» en una tarjeta y dibujó una jarra con agua. Cuando la visita la leyó, sonrió y dijo «mari mari» a todo el curso.»"

L(
    LS3, 4,
    materials="Lápiz y hoja. El texto está escrito aquí; es inventado.",
    use="Aprenderé a responder preguntas relacionando información del texto con lo que sé y con lo que siento, sin contar datos privados. Sirve para dar respuestas completas y bien apoyadas.",
    prior=["Sé localizar palabras y pistas.", "Sé que nadie está obligado a contar su vida personal."],
    explain=[
        "Una respuesta completa tiene tres partes. Primero, el dato del texto que usa. Segundo, lo que yo sé o lo que siento relacionado con ese dato. Tercero, una razón que une las dos partes. Por ejemplo: «El texto dice que Lía quería agradecer. Yo sé que dar las gracias hace sentir bien. Por eso la visita sonrió».",
        "Para encontrar el dato del texto, leo la pregunta y busco palabras iguales o parecidas en el texto. Para mi parte, uso un conocimiento general, algo que aprendí, algo que imagino o una emoción. No necesito contar cosas privadas de mi casa ni de mi familia.",
        "Cuando mi respuesta usa una palabra en lengua indígena, la explico con la ficha. Y si la pregunta pide algo que el texto no dice, escribo «el texto no lo dice» y añado una pregunta para el educador o la educadora tradicional.",
    ],
    vocab=[("dato del texto", "información que está escrita en el texto"), ("conocimiento", "lo que sé porque lo aprendí"), ("razón", "motivo que une dos ideas"), ("respuesta completa", "respuesta con dato, saber y razón"), ("emoción", "lo que siento, como alegría")],
    worked=[
        W("Responder con las tres partes", TXT_U + " " + FICHA_SAL + " ¿Por qué sonrió la visita?", ["Dato: Lía escribió «chaltumay» en una tarjeta.", "Saber: según la ficha, «chaltumay» es gracias.", "Razón: sonrió porque recibió un agradecimiento."], "Porque Lía le escribió «chaltumay», que es gracias, y recibió un agradecimiento."),
        W("Lo que el texto no dice", TXT_U + " ¿Cuántos años tiene Lía?", ["Busco una edad en el texto.", "No la encuentro.", "Respondo: el texto no lo dice."], "el texto no lo dice"),
    ],
    mistakes=[
        M("Responder solo con mi opinión sin usar el texto.", "No se sabe si la respuesta viene de lo que dice el texto.", "Empiezo con un dato del texto."),
        M("Inventar una respuesta cuando el texto no la trae.", "Estaría afirmando algo que no sé.", "Escribo «el texto no lo dice» y hago una pregunta."),
    ],
    R=[
        ex(TXT_U + " ¿Qué quería hacer Lía?", "agradecer a la visita", "Lo dice la primera oración."),
        ex("En el texto U, ¿qué dibujó Lía en la tarjeta?", "una jarra con agua", "Es lo que dice el texto."),
        ex("En el texto U, ¿qué hizo la visita al leer la tarjeta?", "sonrió", "Es la reacción del texto."),
    ],
    C=[
        ex(FICHA_SAL + " ¿Qué quiere decir la palabra que Lía escribió en la tarjeta?", "gracias", "La ficha dice que chaltumay es gracias."),
        ex("Verdadero o falso: una respuesta completa tiene un dato del texto, un saber mío y una razón.", "Verdadero", "Esas son sus tres partes."),
        ex("Si la pregunta es «¿En qué calle vive Lía?», ¿qué respondo? A) «El texto no lo dice». B) «En una calle larga».", "A", "El texto no da ese dato."),
    ],
    A=[
        ex("Pregunta: ¿Por qué Lía escribió «chaltumay»? Elige la respuesta completa. A) «Porque quería agradecer; y «chaltumay» es gracias según la ficha». B) «Porque sí».", "A", "La A tiene dato, saber y razón."),
        ex("Pregunta: ¿Con qué palabra respondió la visita a todo el curso? Responde con el texto U.", "mari mari", "El texto dice que dijo «mari mari»."),
        ex("En el texto U, ¿qué palabra escribió Lía en la tarjeta y qué palabra dijo la visita en voz alta?", "Lía escribió «chaltumay» y la visita dijo «mari mari»", "Lo dicen la segunda y la tercera oración."),
    ],
    Z=[
        ex("Ana contesta: «Lía quería agradecer porque la visita es amable». ¿Qué le falta a la respuesta: una pista del texto o más adjetivos?", "una pista del texto", "No muestra de dónde sale el dato."),
        ex("Una pregunta pide: «Cuenta qué hace tu familia en las visitas». ¿Es adecuado responder con datos privados? Sí o No.", "No", "Nadie está obligado a contar su vida privada."),
    ],
    D=[
        ex("Ordena para responder: A) explico con una razón. B) busco el dato en el texto. C) añado lo que yo sé. Escribe las letras.", "B, C, A", "Dato, saber y razón."),
        ex("Pregunta: ¿Cómo se sintió la visita? El texto U dice que sonrió al leer la tarjeta. ¿Qué respondes: «No lo dice, pero sonrió; puede haber sentido alegría» o «Se sintió triste»?", "«No lo dice, pero sonrió; puede haber sentido alegría»", "Dice qué falta y deduce con prudencia usando la pista."),
    ],
    context=[ex("En tu control de lectura te preguntan por qué la visita sonrió. ¿Qué respuesta usas: «Porque recibió una tarjeta con «chaltumay», que es gracias» o «Porque sí»?", "«Porque recibió una tarjeta con «chaltumay», que es gracias»", "Usa dato del texto y significado de la ficha.")],
    selfcheck=[
        ex("¿Qué tres partes tiene una respuesta completa?", "dato del texto, saber mío y razón", "Así queda bien apoyada."),
        ex("¿Qué escribo si el texto no dice algo?", "el texto no lo dice", "No debo inventar datos."),
        ex("¿Tengo que contar datos privados para responder?", "No", "Puedo responder con lo que sé o siento."),
    ],
    task=T(
        "Responde dos preguntas sobre este texto de práctica inventado. Texto: «Tomás escribió «mari mari» en un cartel. Lo pegó en la puerta de la sala. Cuando la visita entró, miró el cartel y sonrió.» " + FICHA_SAL + " Preguntas: 1) ¿Por qué Tomás pegó el cartel? 2) ¿Qué sintió la visita? Escribe cada respuesta con las tres partes (dato del texto, saber mío y razón) y marca con una línea cuál es cada parte. Si una pregunta no se puede responder con el texto, escribe «el texto no lo dice» y una pregunta para el educador tradicional.",
        "1) El texto dice que escribió «mari mari» y que la visita entró. Yo sé que un saludo recibe a las personas. Por eso lo pegó, para saludar a la visita. 2) El texto no lo dice con certeza, pero sonrió; puede haber sentido alegría. Pregunta: ¿cómo se recibe a una visita en su comunidad?",
        ["cada respuesta tiene dato, saber y razón", "usa la ficha para «mari mari»", "dice «el texto no lo dice» cuando corresponde", "formula una pregunta para el educador/a tradicional"],
        ["dos respuestas marcadas", "pregunta escrita o dicha en voz alta"],
        ["responder solo con opinión", "inventar datos"],
        "Verifica que cada afirmación tenga apoyo en el texto; si inventó un dato, pídele que escriba «el texto no lo dice».",
    ),
    reinforce="Responde en voz alta una pregunta del texto U usando «El texto dice…, yo sé… por eso…».",
    extend="Escribe una pregunta sobre el texto U que se responda con el texto y otra que no.",
)

# =================================================================== LS03 clase 5 · explicar con evidencia y límites
TXT_V = "Texto W (inventado): «La visita llegó a la sala y dijo «mari mari». Mostró una hoja con la palabra «kuyen». Dijo que esa palabra nombra la luna. Los niños escucharon con atención y luego dijeron «chaltumay».»"

L(
    LS3, 5,
    materials="Lápiz y hoja. El texto y las fichas están escritos aquí; son inventados.",
    use="Aprenderé a explicar lo que comprendí mostrando la evidencia del texto y diciendo hasta dónde puedo afirmar. Sirve para no atribuir significados sin fuente.",
    prior=["Sé responder con dato, saber y razón.", "Sé que no debo inventar significados."],
    explain=[
        "La evidencia es la parte del texto o de la ficha que apoya lo que digo. Cuando explico algo, la cito: «El texto dice…» o «Según la ficha…». Con evidencia, mi explicación no queda en el aire y otra persona puede comprobarla.",
        "Un límite es hasta dónde puedo afirmar. Puedo decir que «kuyen» es luna porque lo dice la ficha. Pero no puedo decir cuándo se usa en una comunidad, qué historias tiene ni qué significa en una ceremonia, porque el texto y la ficha no lo dicen. Eso lo explica el educador o la educadora tradicional.",
        "Mi explicación final tiene tres partes: lo que comprendí con evidencia, lo que no puedo afirmar porque no lo sé y una pregunta para quien sabe. Así uso las palabras con sentido, sin decoración, y con respeto por la fuente.",
    ],
    vocab=[("evidencia", "parte del texto o ficha que apoya lo que digo"), ("límite", "hasta dónde puedo afirmar"), ("citar", "decir exactamente lo que dice una fuente"), ("afirmar", "decir que algo es cierto"), ("comprobar", "revisar con la evidencia")],
    worked=[
        W("Explicar con evidencia", TXT_V + " " + FICHA_PAL + " Explica qué es «kuyen» con evidencia.", ["Evidencia del texto: la visita dijo que nombra la luna.", "Evidencia de la ficha: «kuyen» es luna.", "Concluyo: «kuyen» nombra la luna."], "Según el texto y la ficha, «kuyen» nombra la luna."),
        W("Marcar un límite", TXT_V + " ¿Puedes afirmar cuándo se usa la palabra «kuyen» en una comunidad?", ["Busco ese dato en el texto y en la ficha.", "No aparece.", "No puedo afirmarlo; lo pregunto al educador tradicional."], "No; lo pregunto al educador tradicional"),
    ],
    mistakes=[
        M("Afirmar usos o historias de una palabra sin evidencia.", "No están en el texto ni en la ficha.", "Escribo el límite y una pregunta."),
        M("Citar de memoria y cambiar lo que dice la fuente.", "Puedo alterar el significado.", "Copio la frase tal cual."),
    ],
    R=[
        ex(TXT_V + " ¿Qué palabra mostró la visita en la hoja?", "kuyen", "El texto lo dice."),
        ex("En el texto W, ¿qué nombra la palabra «kuyen»?", "la luna", "La visita lo dijo."),
        ex("En el texto W, ¿qué dijeron los niños al final?", "chaltumay", "Es lo último que ocurre."),
    ],
    C=[
        ex("Verdadero o falso: citar es decir exactamente lo que dice una fuente.", "Verdadero", "Esa es su definición."),
        ex("Elige la frase con evidencia. A) «Según la ficha, «kuyen» es luna». B) «Creo que «kuyen» es algo bonito».", "A", "La A cita la ficha."),
        ex("¿Qué es un límite: hasta dónde puedo afirmar o cuánto puedo escribir?", "hasta dónde puedo afirmar", "Es el alcance de mi evidencia."),
    ],
    A=[
        ex("Pregunta: ¿Se puede afirmar con el texto W cuándo se usa «kuyen» en una comunidad? Sí o No.", "No", "El texto no lo dice."),
        ex("Une cada afirmación con su apoyo. Afirmaciones: 1) la visita saludó. 2) «kuyen» es luna. Apoyos: a) la ficha. b) el texto: dijo «mari mari». Escribe 1-?, 2-?", "1-b, 2-a", "El saludo está en el texto y el significado en la ficha."),
        ex("Tu explicación final ya tiene la evidencia y el límite. ¿Qué parte falta?", "una pregunta para quien sabe", "Son tres partes: evidencia, límite y pregunta."),
    ],
    Z=[
        ex("Camila dice: ««Kuyen» se usa en una ceremonia especial». ¿Tiene evidencia en el texto W o en la ficha? Sí o No.", "No", "Ni el texto ni la ficha lo dicen."),
        ex("Pedro cambió «dijo que nombra la luna» por «dijo que es una fiesta». ¿Qué error cometió al citar?", "alteró lo que dice la fuente", "Cambió el sentido."),
    ],
    D=[
        ex("Ordena la explicación final: A) pregunta para quien sabe. B) lo que comprendí con evidencia. C) lo que no puedo afirmar. Escribe las letras.", "B, C, A", "Evidencia, límite y pregunta."),
        ex("Completa: «Según la ficha, «kuyen» es ____. No puedo afirmar ____». Opciones: luna / cuándo se usa en una comunidad; o sol / el color de la luna.", "luna / cuándo se usa en una comunidad", "La ficha dice luna; el uso no está."),
    ],
    context=[ex("En una exposición te preguntan qué significa «kuyen» en las historias de una comunidad. ¿Qué respondes: «La ficha dice luna; las historias las cuenta la educadora tradicional» o «Tiene un significado ceremonial que ya conozco»?", "«La ficha dice luna; las historias las cuenta la educadora tradicional»", "Marca el límite y remite a quien sabe.")],
    selfcheck=[
        ex("¿Cómo se llama la parte del texto que apoya lo que digo?", "evidencia", "Respalda mi explicación."),
        ex("¿Qué escribo cuando no puedo afirmar algo?", "el límite y una pregunta", "Reconozco lo que no sé."),
        ex("¿Quién explica los usos y las historias de una palabra?", "el educador tradicional o la comunidad", "Es quien conoce y cuida la lengua."),
    ],
    task=T(
        "Escribe una explicación final de 5 líneas sobre este texto de práctica inventado: «La visita escribió «ko» en la pizarra y dijo que nombra el agua. Los niños dijeron «chaltumay».» " + FICHA_PAL + " " + FICHA_SAL + " Línea 1: lo que comprendí (con «Según la ficha…»). Línea 2: la evidencia del texto. Línea 3: lo que dijeron los niños y para qué. Línea 4: un límite (algo que no puedo afirmar). Línea 5: una pregunta para la educadora tradicional.",
        "1) Según la ficha, «ko» es agua. 2) El texto dice que la visita escribió «ko» y que nombra el agua. 3) Los niños dijeron «chaltumay» para agradecer. 4) No puedo afirmar cuándo se usa «ko» en una comunidad. 5) Pregunta: ¿cuándo se usa «ko» en su comunidad?",
        ["escribe las cinco líneas", "cita evidencia del texto y la ficha", "marca un límite claro", "formula una pregunta para el educador/a tradicional"],
        ["explicación de cinco líneas", "pregunta escrita o dicha en voz alta"],
        ["afirmar usos sin evidencia", "alterar lo que dice la fuente"],
        "Revisa que cada afirmación tenga evidencia y que el límite sea honesto; si afirmó un uso sin evidencia, pídele que lo mueva a la pregunta.",
    ),
    reinforce="Subraya en el texto W la frase que apoya cada afirmación de tu explicación.",
    extend="Escribe un límite y una pregunta para el texto U de la clase anterior.",
)
