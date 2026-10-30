"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF02 (comunicación oral con palabras y expresiones en lengua indígena) y OA LF03 (comprensión de textos
escritos en lengua indígena).

Criterio de autoría: los diálogos, tarjetas, carteles y cartas de práctica son inventados, están escritos en
castellano y se declaran como tales. Las únicas expresiones en lengua indígena son las ya atestiguadas y usadas en
2.º (mari mari, chaltumay en mapuzugun; iorana, maururu en rapa nui; ko, antü, kuyen, ruka, mapu, ñuke) y siempre
vienen con su ficha. No se escribe pronunciación, gramática ni se asegura a quién, cuándo o en qué ceremonias se dice
cada expresión: eso lo explica el educador/a tradicional o la comunidad. No hay ningún texto real en lengua indígena.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LF2, LF3 = "LC03 OA LF02", "LC03 OA LF03"

CONSULT = " Recuerda: la forma tradicional de decir, escribir y usar estas palabras la enseñan el educador o la educadora tradicional y tu comunidad. Consúltales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

FICHA_EXP = "Ficha de expresiones: «mari mari» es un saludo en mapuzugun. «chaltumay» es «gracias» en mapuzugun. «iorana» es un saludo en rapa nui. «maururu» es «gracias» en rapa nui."
DIAL = "Diálogo de práctica (inventado). Ana: «Mari mari». Educadora: «Buenos días, Ana». Ana: «Hoy quiero aprender una palabra». Educadora: «Veamos «ko»; es agua en mapuzugun». Ana: «Chaltumay»."
FICHA_PAL = "Ficha de palabras en mapuzugun: «ko» es agua, «antü» es sol, «kuyen» es luna, «ruka» es casa, «mapu» es tierra, «ñuke» es madre."


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


# =================================================================== LF02 · comunicación oral con expresiones en lengua indígena
L(
    LF2, 1,
    materials="Lápiz y hoja. La ficha de expresiones está escrita en este cuaderno. Las situaciones son inventadas para practicar.",
    use="Aprenderé a mirar la situación y a la persona con quien hablo antes de usar una expresión en lengua indígena. Sirve para comunicarme con respeto.",
    prior=["Conozco las expresiones «mari mari», «chaltumay», «iorana» y «maururu» con su ficha.", "Sé que una fuente es la persona o el material de donde viene un dato."],
    explain=[
        "Una situación es el momento en que hablo: llegar a un lugar, recibir algo o despedirme. El interlocutor es la persona con quien hablo. Antes de decir una expresión me pregunto tres cosas: ¿qué está pasando?, ¿con quién hablo? y ¿qué quiero lograr?",
        "Cada expresión de la ficha sirve para algo. «Mari mari» y «iorana» son saludos. «Chaltumay» y «maururu» quieren decir «gracias». Si quiero saludar, uso un saludo. Si quiero agradecer, uso un «gracias». No las cambio por gusto.",
        "La ficha no dice a quién, cuándo ni de qué manera se usan en cada comunidad. Eso lo explica el educador o la educadora tradicional. Si no tengo una expresión para lo que quiero decir, hablo en castellano y pregunto. No invento palabras.",
    ],
    vocab=[("situación", "el momento en que hablo, como llegar o recibir algo"), ("interlocutor", "la persona con quien hablo"), ("saludo", "expresión para comenzar una conversación"), ("agradecer", "decir gracias por algo recibido"), ("propósito", "lo que quiero lograr al hablar")],
    worked=[
        W("Elegir según la situación", FICHA_EXP + " Situación: te encuentras con la educadora que enseña mapuzugun. ¿Qué expresión de la ficha usas para saludar?", ["Veo que quiero saludar.", "Busco los saludos en mapuzugun: «mari mari».", "Uso «mari mari»."], "«mari mari»"),
        W("Cuando no hay expresión", FICHA_EXP + " Situación: quieres pedirle ayuda a la educadora. ¿Hay una expresión para pedir ayuda en la ficha?", ["Reviso las cuatro expresiones: dos saludos y dos «gracias».", "Ninguna sirve para pedir ayuda.", "Pido ayuda en castellano y pregunto cómo se dice."], "No hay; pido ayuda en castellano y pregunto"),
    ],
    mistakes=[
        M("Usar un saludo para agradecer porque me gusta cómo suena.", "La ficha dice que cada expresión sirve para algo distinto.", "Primero veo qué quiero lograr y elijo la expresión que corresponde."),
        M("Inventar una palabra cuando no tengo una expresión.", "No sé si esa palabra existe.", "Hablo en castellano y pregunto al educador tradicional."),
    ],
    R=[
        ex(FICHA_EXP + " ¿Qué quiere decir «maururu»?", "gracias", "La ficha dice que «maururu» es gracias en rapa nui."),
        ex("El interlocutor es: A) la persona con quien hablo B) el lugar donde estoy.", "A", "Interlocutor es la persona con quien hablo."),
        ex(FICHA_EXP + " ¿Cuál de estas es un saludo en mapuzugun: «mari mari» o «chaltumay»?", "mari mari", "La ficha dice que «mari mari» es un saludo."),
    ],
    C=[
        ex(FICHA_EXP + " La educadora te presta un lápiz. ¿Qué expresión en mapuzugun usas para agradecer?", "chaltumay", "La ficha dice que «chaltumay» es gracias en mapuzugun."),
        ex("Verdadero o falso: puedo usar cualquier expresión de la ficha en cualquier situación.", "Falso", "Cada expresión sirve para algo distinto."),
        ex(FICHA_EXP + " Quieres saludar en rapa nui. ¿Qué expresión usas?", "iorana", "La ficha dice que «iorana» es un saludo en rapa nui."),
    ],
    A=[
        ex(FICHA_EXP + " Une cada situación con su expresión. 1) saludas en mapuzugun 2) agradeces en rapa nui. Escribe las dos expresiones en orden.", "mari mari, maururu", "Un saludo en mapuzugun es «mari mari» y «gracias» en rapa nui es «maururu»."),
        arith("La ficha de expresiones tiene 4 expresiones y 2 son saludos. ¿Cuántas quieren decir «gracias»?", "4 - 2", "Resto los saludos del total."),
        ex("Situación: Ana recibe un lápiz que le presta un compañero. ¿Es una situación de saludo o de agradecimiento?", "de agradecimiento", "Ana recibe algo y quiere dar las gracias."),
    ],
    Z=[
        ex("Pedro dice: «Voy a usar «mari mari» para agradecer porque me gusta cómo suena». ¿Tiene razón? Responde Sí o No.", "No", "La ficha dice que «mari mari» es un saludo."),
        ex("No hay en la ficha una expresión para despedirse. ¿Qué es mejor: inventar una palabra o despedirme en castellano y preguntar?", "despedirme en castellano y preguntar", "No debo inventar palabras."),
    ],
    D=[
        ex("Quieres preguntar cuándo y a quién se dicen estas expresiones en una comunidad. ¿A quién le preguntas primero: a la educadora tradicional o a un compañero que tampoco lo sabe?", "a la educadora tradicional", "Ella puede explicarlo."),
        ex("Ordena una conversación de práctica: B) la educadora responde A) saludo con «mari mari» C) agradezco con «chaltumay». Escribe las letras.", "A, B, C", "Saludo, escucho la respuesta y luego agradezco."),
    ],
    context=[ex(FICHA_EXP + " Llega a tu sala una visita que enseña rapa nui. Quieres saludarla en su lengua. ¿Qué dices: «iorana» o «chaltumay»?", "«iorana»", "«Iorana» es el saludo en rapa nui.")],
    selfcheck=[
        ex("¿Qué nombre tiene la persona con quien hablo?", "interlocutor", "Interlocutor es quien escucha o responde."),
        ex("¿Qué hago si no tengo una expresión para lo que quiero decir?", "hablo en castellano y pregunto", "No invento palabras."),
        ex("¿Quién explica a quién y cuándo se dice una expresión en una comunidad?", "el educador tradicional o la comunidad", "Ellos conocen cómo se usa."),
    ],
    task=T(
        "Usa la ficha de expresiones. Completa una tabla con tres situaciones: A) saludas a la educadora que enseña mapuzugun al llegar a la sala; B) la educadora te muestra cómo se dice una palabra y quieres agradecerle en mapuzugun; C) un compañero te pasa una goma. En A y B escribe la expresión de la ficha. En C explica por qué hablarás en castellano. Después escribe una pregunta para la educadora sobre cuándo se usa cada expresión.",
        "A: «mari mari». B: «chaltumay». C: la ficha no dice si se usa con compañeros, así que hablo en castellano. Pregunta: ¿cuándo se dice «mari mari» en su comunidad?",
        ["elige la expresión correcta en A y B", "explica la decisión en C sin inventar", "escribe una pregunta para el educador/a"],
        ["tabla de tres filas", "pregunta escrita o dicha en voz alta"],
        ["usar un saludo para agradecer", "inventar una palabra"],
        "Valora que eligió según situación e interlocutor; si inventó una palabra, remítelo a preguntar al educador.",
    ),
    reinforce="Mira la ficha y di en voz alta qué expresión usarías para saludar y cuál para agradecer en mapuzugun.",
    extend="Escribe una situación de tu día en que quieras agradecer y otra en que quieras saludar, y decide qué expresión de la ficha usarías en cada una.",
)

L(
    LF2, 2,
    materials="Lápiz y hoja. La ficha de expresiones está en este cuaderno. Para ensayar, una persona de tu casa o de tu curso que te escuche.",
    use="Aprenderé cómo ensayar una expresión con una fuente validada. Sirve para decir las palabras con respeto, sin inventar su forma.",
    prior=["Sé elegir una expresión según la situación.", "Sé que no invento palabras en lengua indígena."],
    explain=[
        "Una expresión validada es una que una fuente confirmó: el educador tradicional, la comunidad o una ficha hecha con ellos. Si no sé quién la confirmó, no la uso como si fuera segura.",
        "Para ensayar sigo cuatro pasos. Uno: escucho a la educadora decir la expresión. Dos: la digo yo. Tres: ella me ayuda a mejorar. Cuatro: la digo de nuevo. Equivocarme al comienzo es parte de aprender, y repetir es lo normal.",
        "No escribo cómo se pronuncia una palabra a partir de lo que imagino. La pronunciación se aprende escuchando a quien conoce la lengua. Tampoco cambio una expresión para que sea más fácil: la digo como me la enseñaron.",
    ],
    vocab=[("validada", "confirmada por el educador, la comunidad o una ficha hecha con ellos"), ("ensayar", "practicar varias veces"), ("pronunciación", "la manera de decir una palabra en voz alta"), ("repetir", "decir otra vez"), ("corregir", "cambiar algo para que quede mejor")],
    worked=[
        W("Los cuatro pasos", "Quieres ensayar «chaltumay» (gracias en mapuzugun). ¿Qué haces después de escuchar a la educadora decirla?", ["El primer paso fue escuchar.", "El segundo paso es decirla yo.", "Después pido ayuda para mejorar."], "Digo la expresión yo"),
        W("Una palabra sin fuente", "Un compañero dice que una palabra que oyó en un video significa «amigo» en mapuzugun. No está en la ficha. ¿Qué haces?", ["Veo que no está validada.", "No la uso como segura.", "Se la pregunto a la educadora tradicional."], "La pregunto a la educadora tradicional"),
    ],
    mistakes=[
        M("Escribir cómo suena una palabra sin haberla escuchado a la educadora.", "Puedo equivocarme y enseñar una forma que no es.", "Escucho primero y repito después."),
        M("Cambiar una expresión para decirla más fácil.", "Dejo de usarla como me la enseñaron.", "La ensayo hasta decirla como la enseñó la educadora."),
    ],
    R=[
        ex("Una expresión validada es: A) la que confirmó la educadora o una ficha hecha con ella B) la que me inventé.", "A", "Validada quiere decir confirmada."),
        ex("Ensayar es: A) practicar varias veces B) decirla una sola vez.", "A", "Ensayar es practicar."),
        ex("¿Quién me muestra cómo se dice una palabra: la educadora o mi imaginación?", "la educadora", "Ella conoce la lengua."),
    ],
    C=[
        ex("Verdadero o falso: puedo escribir la pronunciación de una palabra aunque no la haya escuchado.", "Falso", "La pronunciación se aprende escuchando a quien sabe."),
        ex("Los pasos del ensayo son: escucho, la digo, me ayudan a mejorar y la digo de nuevo. ¿Cuántos pasos son?", "4", "Cuento los cuatro pasos."),
        ex("Si me equivoco al repetir una expresión, ¿es un error grave o parte de aprender?", "parte de aprender", "Equivocarme al comienzo es normal."),
    ],
    A=[
        arith("Ensayas «mari mari» 3 veces y «chaltumay» 3 veces. ¿Cuántas veces ensayas en total?", "3 + 3", "Sumo los dos ensayos."),
        ex("Ordena los pasos: C) ella me ayuda a mejorar A) escucho a la educadora B) la digo yo D) la digo de nuevo. Escribe las letras.", "A, B, C, D", "Escucho, digo, recibo ayuda y vuelvo a decir."),
        ex("Una palabra que no está en la ficha y que oíste en un video. ¿Qué haces: A) la uso igual B) pregunto a la educadora?", "B", "No está validada."),
    ],
    Z=[
        ex("Luis dice: «Mejor digo «mari» solo, porque es más fácil». ¿Tiene razón? Responde Sí o No.", "No", "La expresión se dice como la enseña la educadora."),
        ex("Ana ensayó su expresión y la educadora le dijo cómo mejorar. ¿Qué conviene hacer: ensayar de nuevo o dejar de practicar?", "ensayar de nuevo", "Repetir con ayuda es parte del ensayo."),
    ],
    D=[
        arith("Practicas 2 veces al día durante 4 días. ¿Cuántas veces ensayaste en total?", "2 * 4", "Dos ensayos por cuatro días."),
        ex("Una ficha hecha con la educadora dice que «iorana» es un saludo en rapa nui. Un cartel sin autor dice otra cosa. ¿En cuál confías primero?", "en la ficha hecha con la educadora", "Tiene una fuente validada."),
    ],
    context=[ex("Te toca decir «mari mari» ante tu curso. Te pones nervioso y la dices distinta. ¿Qué haces: pido ayuda y la digo de nuevo o me quedo callado para siempre?", "pido ayuda y la digo de nuevo", "Repetir con ayuda es parte de aprender.")],
    selfcheck=[
        ex("¿Qué significa que una expresión sea validada?", "que una fuente la confirmó", "La confirmó el educador, la comunidad o una ficha hecha con ellos."),
        ex("¿Dónde aprendo la pronunciación de una palabra?", "escuchando a quien conoce la lengua", "No la invento."),
        ex("¿Puedo cambiar una expresión para que sea más fácil?", "No", "La digo como me la enseñaron."),
    ],
    task=T(
        "Elige una de las dos expresiones de la ficha: «mari mari» o «chaltumay» (mapuzugun). Haz un plan de ensayo de cuatro pasos en tu cuaderno: 1) escucho a la educadora; 2) la digo yo; 3) pido ayuda para mejorar; 4) la digo de nuevo. Al lado de cada paso escribe cuándo lo harás (por ejemplo: lunes en la clase). Termina con una pregunta para la educadora sobre cómo se dice bien.",
        "Expresión: «mari mari». 1) Escucho a la educadora el lunes. 2) La digo yo el lunes. 3) Le pido ayuda el martes. 4) La digo de nuevo el miércoles. Pregunta: ¿puede decirla otra vez más despacio?",
        ["elige una expresión de la ficha", "escribe los cuatro pasos", "no escribe una pronunciación inventada", "hace una pregunta a la educadora"],
        ["plan escrito de cuatro pasos", "ensayo en voz alta ante la educadora o un adulto"],
        ["escribir cómo suena sin haberla escuchado", "cambiar la expresión"],
        "Valora que el plan incluye escuchar y pedir ayuda; si inventó una pronunciación, pídele que la borre y espere a escuchar a la educadora.",
    ),
    reinforce="Con la ayuda de alguien que sepa, practica una expresión de la ficha tres veces seguidas.",
    extend="Explica a otra persona los cuatro pasos para ensayar una expresión sin inventarla.",
)

L(
    LF2, 3,
    materials="Lápiz y hoja. El diálogo de práctica está escrito aquí. Es inventado y está en castellano con expresiones de la ficha.",
    use="Aprenderé a mantener un diálogo breve de tres a cinco turnos usando una expresión en lengua indígena. Sirve para conversar con respeto y esperar mi turno.",
    prior=["Sé elegir una expresión según la situación.", "Sé ensayar una expresión con la educadora."],
    explain=[
        "Un diálogo es una conversación entre dos o más personas. Cada vez que alguien habla es un turno. Hablo cuando me toca y escucho cuando le toca a la otra persona. Un diálogo breve puede tener de tres a cinco turnos.",
        "Un buen diálogo tiene un comienzo, una parte del medio y un cierre. Puedo comenzar con un saludo, preguntar o responder algo en castellano y cerrar con un agradecimiento. Las expresiones en lengua indígena aparecen solo donde sirven, como el saludo o el «gracias».",
        "Escucho a la otra persona antes de responder. Miro a quien me habla y espero a que termine. Si no entiendo, pregunto. En una lengua nueva, hablar poco y bien es mejor que hablar mucho e inventar.",
        "Un diálogo se puede actuar con otra persona, cada una con su papel: eso es una dramatización. También puedo contar algo a mi curso hablando yo solo, sin turnos: eso es una exposición breve. En todas estas formas uso solo las expresiones de la ficha.",
    ],
    vocab=[("diálogo", "conversación entre dos o más personas"), ("turno", "cada vez que una persona habla"), ("comienzo", "la primera parte de una conversación"), ("cierre", "la última parte de una conversación"), ("escuchar", "poner atención a lo que dice otra persona")],
    worked=[
        W("Contar los turnos", DIAL + " ¿Cuántos turnos tiene el diálogo?", ["Cuento cada vez que alguien habla.", "Ana habla 3 veces y la educadora 2.", "3 + 2 = 5 turnos."], "5 turnos"),
        W("Comienzo y cierre", DIAL + " ¿Con qué expresión cierra Ana?", ["Miro el último turno.", "Ana dice «Chaltumay».", "Es un agradecimiento."], "«Chaltumay»"),
    ],
    mistakes=[
        M("Hablar mientras la otra persona todavía habla.", "No escucho y se pierde lo que dijo.", "Espero a que termine."),
        M("Llenar el diálogo con palabras inventadas.", "Puedo decir cosas que no existen.", "Uso solo expresiones de la ficha y el resto en castellano."),
    ],
    R=[
        ex("Cada vez que una persona habla en una conversación se llama: A) turno B) cierre.", "A", "Turno es cada vez que alguien habla."),
        ex("Diálogo: Ana: «Mari mari». Educadora: «Buenos días, Ana». ¿Cuántos turnos hay?", "2", "Hablan una vez cada una."),
        ex("Cuando la otra persona habla, ¿espero a que termine o la interrumpo?", "espero a que termine", "Escuchar es parte del diálogo."),
    ],
    C=[
        ex(DIAL + " ¿Cuántos turnos dice Ana?", "3", "Ana habla en el primer, tercer y quinto turno."),
        ex(DIAL + " ¿Qué dice Ana para saludar?", "«Mari mari»", "Su primer turno es el saludo."),
        ex("Verdadero o falso: un buen diálogo usa palabras inventadas en lengua indígena para sonar mejor.", "Falso", "Se usan solo expresiones validadas."),
    ],
    A=[
        ex("Ordena el diálogo: B) la educadora responde A) Ana saluda con «mari mari» C) Ana agradece con «chaltumay». Escribe las letras.", "A, B, C", "Saludo, respuesta y agradecimiento."),
        arith("Un diálogo de práctica tiene 3 turnos de Ana y 2 turnos de la educadora. ¿Cuántos turnos tiene en total?", "3 + 2", "Sumo los turnos de las dos."),
        ex("Diálogo de práctica. Pedro: «Mari mari». Educadora: «Buenos días». Pedro: «¿Me enseña una palabra?». Educadora: «Sí». ¿Quién habla en el último turno?", "la educadora", "El último turno es el «Sí» de la educadora."),
    ],
    Z=[
        ex("Tomás habla encima de la educadora. ¿Qué parte del diálogo cuida más: escuchar o hablar fuerte?", "escuchar", "Un diálogo se construye alternando turnos."),
        ex("Ana quiere despedirse, pero la ficha no tiene una expresión para despedirse. ¿Qué es mejor: A) inventar una palabra B) despedirse en castellano?", "B", "No debo inventar palabras en lengua indígena."),
    ],
    D=[
        ex(DIAL + " Escribe el número del turno donde Ana agradece.", "5", "Es el último turno."),
        arith("Dos amigos dialogan con 2 turnos cada uno. ¿Cuántos turnos tiene el diálogo?", "2 + 2", "Sumo los turnos de cada amigo."),
    ],
    context=[ex("Mañana presentas un diálogo breve ante tu curso. Tu compañero habla demasiado rápido y no te deja responder. ¿Qué le pides: «Espera mi turno, por favor» o «Habla más fuerte»?", "«Espera mi turno, por favor»", "El diálogo se cuida respetando los turnos.")],
    selfcheck=[
        ex("¿Cuántos turnos puede tener un diálogo breve de la clase?", "de tres a cinco", "Es la medida de un diálogo breve."),
        ex("¿Qué debo hacer mientras la otra persona habla?", "escuchar", "Escuchar es parte del diálogo."),
        ex("¿Qué expresión de la ficha puede servir para cerrar agradeciendo en mapuzugun?", "chaltumay", "La ficha dice que es «gracias»."),
    ],
    task=T(
        "Escribe un diálogo de cinco turnos entre una niña llamada Rosa y la educadora tradicional (personajes inventados). Turno 1: Rosa saluda con «mari mari». Turno 2: la educadora responde en castellano. Turno 3: Rosa dice en castellano algo que quiere aprender. Turno 4: la educadora responde en castellano. Turno 5: Rosa agradece con «chaltumay». Escribe los cinco turnos y actúalo leyéndolo con un compañero o un adulto, cada uno con un papel.",
        "Rosa: «Mari mari». Educadora: «Buenos días, Rosa». Rosa: «Quiero aprender una palabra nueva». Educadora: «Muy bien, veamos una». Rosa: «Chaltumay».",
        ["escribe los cinco turnos, alternando a Rosa y la educadora", "usa «mari mari» y «chaltumay» en su lugar", "respeta los turnos al leerlo"],
        ["diálogo escrito", "lectura en voz alta con otra persona"],
        ["inventar palabras en lengua indígena", "saltarse el turno de la otra persona"],
        "Valora que los turnos están claros; si inventó palabras, pide que las reemplace por castellano o por una expresión de la ficha.",
    ),
    reinforce="Lee en voz alta el diálogo de Ana con un adulto, cada uno con un papel.",
    extend="Cambia el diálogo para que Rosa salude con «iorana» a una visita que enseña rapa nui y la agradezca con «maururu».",
)

L(
    LF2, 4,
    materials="Lápiz y hoja. Las fichas con variantes están escritas aquí.",
    use="Aprenderé que una palabra puede decirse o escribirse de más de una manera y cómo comunicarme con respeto ante esas diferencias. Sirve para no corregir a otros sin saber.",
    prior=["Sé ensayar expresiones validadas.", "Sé sostener un diálogo breve."],
    explain=[
        "Una lengua puede tener variantes. Una variante es otra forma de decir o escribir lo mismo. Puede depender del lugar, de la comunidad o de cómo se escribió. Por ejemplo, la casa mapuche se ve escrita «ruka» y «ruca».",
        "Otros ejemplos son «pewen» y «pehuén» para el árbol de los piñones, y «mapuzugun» y «mapudungun» para la lengua mapuche. Son escrituras distintas de lo mismo. Una variante no es un error.",
        "Cuando me encuentro con una variante distinta, no corrijo. Pregunto con respeto: «¿Cómo se dice en su comunidad?». Si dos personas lo dicen distinto, las dos pueden tener razón. La educadora o el educador de mi escuela me dice qué forma usamos allí.",
    ],
    vocab=[("variante", "otra forma de decir o escribir lo mismo"), ("comunidad", "grupo de personas que comparte una cultura"), ("corregir", "cambiar algo porque creo que está mal"), ("respeto", "tratar con cuidado lo que importa a otros"), ("escritura", "la manera de poner una palabra en letras")],
    worked=[
        W("Dos escrituras de una palabra", "Una ficha escribe «ruka» y un libro escribe «ruca» para la casa mapuche. ¿Cuál está mal?", ["Las dos nombran lo mismo.", "Son variantes de escritura.", "Ninguna está mal; pregunto cuál usa la comunidad."], "Ninguna; son variantes"),
        W("Preguntar con respeto", "Un compañero escribe «pehuén» y tú sabías «pewen». ¿Qué le dices?", ["No lo corrijo.", "Pienso en una pregunta amable.", "Digo: «¿Cómo se escribe en su comunidad?»."], "«¿Cómo se escribe en su comunidad?»"),
    ],
    mistakes=[
        M("Corregir a una persona diciendo que su forma está mal.", "Puede ser una variante válida.", "Pregunto cómo se dice en su comunidad."),
        M("Pensar que hay una sola forma correcta en todas partes.", "Las lenguas tienen variantes.", "Anoto las dos formas y la fuente de cada una."),
    ],
    R=[
        ex("Otra forma de decir o escribir lo mismo se llama: A) variante B) error.", "A", "Variante es otra forma válida."),
        ex("«Ruka» y «ruca» nombran la casa mapuche. ¿Son dos escrituras de lo mismo?", "Sí", "Las dos nombran la casa."),
        ex("Si alguien lo dice distinto a mí, ¿lo corrijo o le pregunto con respeto?", "le pregunto con respeto", "Puede ser una variante."),
    ],
    C=[
        ex("Verdadero o falso: «pewen» y «pehuén» son dos escrituras del árbol de los piñones.", "Verdadero", "Son variantes de escritura."),
        ex("Pregunta amable: A) «¿Cómo se dice en su comunidad?» B) «Está mal dicho».", "A", "A pregunta con respeto; B corrige sin saber."),
        ex("«Mapuzugun» y «mapudungun» son dos escrituras de la lengua del pueblo mapuche. ¿Cuántas formas escritas hay?", "2", "Hay dos escrituras."),
    ],
    A=[
        arith("Una ficha trae 3 palabras con 2 escrituras cada una. ¿Cuántas escrituras son en total?", "3 * 2", "Tres palabras por dos escrituras."),
        ex("Dos compañeros escriben «ruka» y «ruca». ¿Qué haces: A) anoto las dos y pregunto cuál usa la comunidad B) borro una?", "A", "Registro las dos y consulto."),
        ex("La educadora de tu escuela usa «pewen». Un libro usa «pehuén». En tu sala, ¿qué forma usas para el cartel: la que usa la educadora o la del libro?", "la que usa la educadora", "Es la forma de la comunidad de tu escuela."),
    ],
    Z=[
        ex("Camila dice: «Mi libro dice «ruca», así que «ruka» está mal». ¿Tiene razón? Responde Sí o No.", "No", "Son variantes de escritura."),
        ex("¿Por qué es mejor preguntar «¿cómo se dice en su comunidad?» que decir «eso no se dice así»?", "porque puede ser una variante válida", "Preguntar respeta lo que sabe la otra persona."),
    ],
    D=[
        ex("Ordena para comunicarte con respeto: C) anoto las dos formas A) escucho cómo lo dice la persona B) pregunto cómo se dice en su comunidad. Escribe las letras.", "A, B, C", "Escucho, pregunto y luego anoto."),
        arith("En la sala hay 5 carteles con la palabra «ruka» y 3 con «ruca». ¿Cuántos carteles hay en total?", "5 + 3", "Sumo los carteles de las dos escrituras."),
    ],
    context=[ex("En el cartel de tu curso, un compañero escribió «mapudungun» y la educadora dijo «mapuzugun». ¿Qué le dices a tu compañero: «Preguntemos qué forma usa la educadora» o «Está mal»?", "«Preguntemos qué forma usa la educadora»", "Pregunto sin corregir y uso la forma de la comunidad.")],
    selfcheck=[
        ex("¿Cómo se llama otra forma válida de decir o escribir lo mismo?", "variante", "Variante es otra forma válida."),
        ex("¿Qué pregunta hago cuando alguien lo dice distinto?", "¿cómo se dice en su comunidad?", "Es una pregunta respetuosa."),
        ex("¿Una variante es un error?", "No", "Puede ser válida."),
    ],
    task=T(
        "Completa una tabla de tres filas con estas palabras y sus variantes, que ya viste en la clase: casa («ruka» / «ruca»), árbol de los piñones («pewen» / «pehuén»), lengua mapuche («mapuzugun» / «mapudungun»). En una columna escribe las dos formas y en otra una pregunta respetuosa para un compañero o una compañera que use la otra forma. Termina con una pregunta para la educadora tradicional sobre qué formas usa su comunidad.",
        "Casa: ruka / ruca. Pregunta: ¿cómo lo escribes en tu comunidad? Árbol: pewen / pehuén. Lengua: mapuzugun / mapudungun. Pregunta a la educadora: ¿qué forma usan ustedes en la escuela?",
        ["anota las dos formas de cada palabra", "no dice que una forma es incorrecta", "escribe una pregunta respetuosa", "pregunta a la educadora"],
        ["tabla escrita", "pregunta dicha en voz alta o escrita"],
        ["tachar una variante", "corregir a un compañero"],
        "Valora que registró las variantes sin juzgar; si tachó una, invítalo a anotar ambas y a preguntar a quien enseña.",
    ),
    reinforce="Escribe «ruka» y «ruca» lado a lado y di con tus palabras por qué ninguna está mal.",
    extend="Busca dos palabras del castellano que se digan distinto en dos familias y anota qué variante usa cada una.",
)

# =================================================================== LF03 · comprensión de textos escritos en lengua indígena
L(
    LF3, 1,
    materials="Lápiz y hoja. El cartel y las fichas están escritos en este cuaderno. Son inventados para practicar y están en castellano, con una expresión de la ficha.",
    use="Aprenderé a pensar qué dirá un texto antes de leerlo, usando pistas como el título, el dibujo y la fuente. Sirve para entrar al texto con calma y comprobar si mi idea era correcta.",
    prior=["Conozco las expresiones «mari mari» y «chaltumay» con su ficha.", "Sé que una fuente es de donde viene un dato."],
    explain=[
        "Anticipar es pensar qué va a decir un texto antes de leerlo. Me ayudan las pistas: el título, el dibujo, quién lo escribió y dónde lo encontré. Con esas pistas hago una idea. Esa idea se llama predicción.",
        "Una predicción no es una verdad. Es una idea que debo comprobar leyendo. Si el texto dice otra cosa, cambio mi idea. No pasa nada: equivocarme al predecir es parte de leer.",
        "También miro la fuente. Si el texto viene de una ficha o de un cartel de mi escuela, anoto de dónde viene. Un texto escrito en lengua indígena no debe separarse de su cultura: no lo leo como si no tuviera dueño ni lugar.",
    ],
    vocab=[("anticipar", "pensar qué dirá un texto antes de leerlo"), ("pista", "dato que me ayuda a pensar o a entender"), ("predicción", "idea que hago sobre lo que dirá un texto"), ("título", "nombre de un texto"), ("comprobar", "revisar si mi idea era cierta")],
    worked=[
        W("Predecir con pistas", "Cartel de práctica (inventado). Título: «Mari mari». Dibujo: dos niños frente a una puerta, uno con la mano levantada. Dónde está: en la puerta de la sala. Fuente: ficha de la clase. ¿Qué predices que dice?", ["Leo el título: «Mari mari».", "La ficha dice que es un saludo en mapuzugun.", "El dibujo muestra a dos niños que se encuentran."], "Un saludo para quien entra a la sala"),
        W("Comprobar la predicción", "Sigues leyendo el cartel y dice: «Mari mari. Bienvenidos a nuestra sala». ¿Tu predicción era correcta?", ["Leo la frase completa.", "Dice «bienvenidos», que es un saludo.", "Mi predicción coincide."], "Sí, era un saludo"),
    ],
    mistakes=[
        M("Creer que mi predicción es segura.", "Todavía no he leído el texto.", "La compruebo leyendo."),
        M("Leer el texto sin mirar quién lo escribió ni dónde está.", "Pierdo pistas de su fuente y su cultura.", "Antes de leer miro título, dibujo, fuente y lugar."),
    ],
    R=[
        ex("Anticipar es: A) pensar qué dirá un texto antes de leerlo B) leer solo el final.", "A", "Anticipar es predecir antes de leer."),
        ex("El título de un texto es: A) su nombre B) su último párrafo.", "A", "El título es el nombre."),
        ex("Una idea que hago antes de leer se llama: A) predicción B) respuesta final.", "A", "Es una idea que debo comprobar."),
    ],
    C=[
        ex("Cartel: título «Mari mari»; dibujo de dos niños que se encuentran. " + "Ficha: «mari mari» es un saludo en mapuzugun. ¿Qué pista del cartel dice que es un saludo?", "el título, según la ficha", "La ficha explica que «mari mari» es un saludo."),
        ex("Verdadero o falso: si el texto dice algo distinto a mi predicción, debo cambiar mi idea.", "Verdadero", "La predicción se corrige con lo que dice el texto."),
        ex("Un texto está pegado en la puerta de la sala. ¿Qué pista es: dónde lo encontré o el color de mi lápiz?", "dónde lo encontré", "El lugar da una pista del propósito del texto."),
    ],
    A=[
        ex("Cartel de práctica. Título: «Chaltumay». Dibujo: una niña entrega una flor a otra. Ficha: «chaltumay» es gracias en mapuzugun. ¿Qué predices que dice el cartel?", "algo de dar las gracias", "El título es gracias y el dibujo muestra un regalo."),
        arith("Un texto tiene 4 pistas: título, dibujo, fuente y lugar. Ya miraste 3. ¿Cuántas te faltan?", "4 - 3", "Resto las pistas que ya miraste."),
        ex("Ordena los pasos: C) compruebo leyendo B) hago una predicción A) miro las pistas. Escribe las letras en orden correcto.", "A, B, C", "Miro, predigo y compruebo."),
    ],
    Z=[
        ex("Pedro dice: «No miro el título porque ya sé lo que dirá». ¿Tiene razón? Responde Sí o No.", "No", "Sin pistas no puedo comprobar mi idea."),
        ex("Una niña ve el título «Mari mari» y dice: «Será una receta de cocina». ¿Qué pista de la ficha contradice su predicción?", "que «mari mari» es un saludo", "La ficha dice que es un saludo, no una receta."),
    ],
    D=[
        ex("Cartel de práctica A: título «Mari mari», dibujo de dos niños. Cartel B: título «Chaltumay», dibujo de un regalo. Con la ficha, ¿cuál predices que habla de agradecer?", "B", "«Chaltumay» es gracias."),
        arith("Tienes 3 carteles y miras 4 pistas en cada uno. ¿Cuántas pistas miras en total?", "3 * 4", "Tres carteles por cuatro pistas."),
    ],
    context=[ex("En el pasillo de tu escuela hay un cartel con el título «Mari mari» y un dibujo de dos niños que se encuentran. Antes de leerlo, ¿qué predices que será: un saludo de bienvenida o una lista de útiles?", "un saludo de bienvenida", "El título, la ficha y el dibujo apuntan a un saludo.")],
    selfcheck=[
        ex("Nombra dos pistas de un texto.", "título y dibujo", "También sirven la fuente y el lugar."),
        ex("¿Debo comprobar mi predicción leyendo?", "Sí", "Una predicción se prueba."),
        ex("¿Está mal equivocarme al predecir?", "No", "Es parte de leer y aprender."),
    ],
    task=T(
        "Lee estas pistas de un cartel de práctica: título «Chaltumay», dibujo de una niña que entrega una hoja de colores a una profesora, lugar: la pared de tu sala, fuente: ficha de la clase (con «chaltumay» es gracias en mapuzugun). Escribe tu predicción de qué dice el cartel y qué pistas usaste. Después escribe una pregunta que le harías a la educadora tradicional sobre cuándo se dice esa palabra.",
        "Predicción: el cartel agradece. Usé el título «Chaltumay», que es gracias, y el dibujo de la entrega. Pregunta: ¿cuándo se dice «chaltumay» en su comunidad?",
        ["escribe una predicción", "nombra al menos dos pistas", "hace una pregunta a la educadora"],
        ["predicción y pistas escritas", "pregunta escrita o dicha en voz alta"],
        ["predecir sin usar pistas", "inventar un significado distinto al de la ficha"],
        "Valora que usó pistas y las nombró; si inventó un significado, remítelo a la ficha.",
    ),
    reinforce="Mira el título y el dibujo de un libro cualquiera de tu casa y di qué crees que dice.",
    extend="Predice qué dirá un cartel con el título «Iorana» y un dibujo de un niño que levanta la mano. Usa la ficha de expresiones.",
)

L(
    LF3, 2,
    materials="Lápiz y hoja. Las tarjetas de práctica y la ficha están escritas aquí. Un adulto lee en voz alta lo que le enseñó el educador o la educadora tradicional, si lo sabe.",
    use="Aprenderé a leer un texto corto usando tres apoyos: lo que oigo, lo que veo y la ficha. Sirve para entender sin adivinar.",
    prior=["Sé anticipar un texto con pistas.", "Sé que las palabras en lengua indígena vienen con su ficha."],
    explain=[
        "Leer un texto corto en una lengua que estoy aprendiendo me resulta más fácil con apoyos. Un apoyo oral es escuchar a alguien que sabe leer la palabra, como el educador o la educadora tradicional. Un apoyo visual es el dibujo. Una ficha me dice el significado.",
        "Con los tres apoyos junto el significado de la palabra. Por ejemplo, la tarjeta con el dibujo de gotas de agua y la palabra «ko» me hace pensar en agua. La ficha lo confirma: «ko» es agua en mapuzugun.",
        "El dibujo ayuda, pero no decide solo. Si el dibujo no coincide con la ficha, no me quedo con lo que me parece: pregunto. La pronunciación la aprendo escuchando a quien conoce la lengua, no la invento mirando las letras.",
    ],
    vocab=[("apoyo oral", "escuchar a alguien que sabe leer la palabra"), ("apoyo visual", "un dibujo que ayuda a entender"), ("tarjeta", "papel pequeño con una palabra y un dibujo"), ("confirmar", "comprobar que algo es cierto"), ("significado", "lo que quiere decir una palabra")],
    worked=[
        W("Leer una tarjeta", FICHA_PAL + " Tarjeta 1 (inventada): dibujo de gotas de agua y la palabra «ko». ¿Qué quiere decir la palabra?", ["Miro el dibujo: gotas de agua.", "Busco «ko» en la ficha: es agua.", "El dibujo y la ficha coinciden."], "agua"),
        W("Leer otra tarjeta", FICHA_PAL + " Tarjeta 2 (inventada): dibujo de una luna y la palabra «kuyen». ¿Qué quiere decir?", ["El dibujo muestra una luna.", "La ficha dice que «kuyen» es luna.", "Coinciden."], "luna"),
    ],
    mistakes=[
        M("Decidir el significado solo por el dibujo.", "El dibujo puede no coincidir con la palabra.", "Reviso también la ficha."),
        M("Inventar cómo se dice la palabra mirando las letras.", "La pronunciación se aprende escuchando.", "Pido a la educadora que la lea."),
    ],
    R=[
        ex(FICHA_PAL + " Tarjeta con dibujo de una casa y la palabra «ruka». ¿Qué quiere decir «ruka»?", "casa", "La ficha dice que «ruka» es casa."),
        ex("Un dibujo que ayuda a entender una palabra se llama apoyo: A) visual B) oral.", "A", "Lo veo con los ojos."),
        ex("Quien me enseña cómo se lee una palabra es un apoyo: A) oral B) visual.", "A", "Lo escucho con los oídos."),
    ],
    C=[
        ex(FICHA_PAL + " Tarjeta: dibujo de un sol y la palabra «antü». ¿Qué apoyo confirma el significado: la ficha o el color de mi lápiz?", "la ficha", "La ficha dice que «antü» es sol."),
        ex("Verdadero o falso: puedo decidir el significado de una palabra solo mirando el dibujo.", "Falso", "Debo confirmar con la ficha."),
        ex(FICHA_PAL + " Tarjeta: dibujo de una mujer con un niño y la palabra «ñuke». ¿Qué significa «ñuke» según la ficha?", "madre", "La ficha dice que «ñuke» es madre."),
    ],
    A=[
        ex(FICHA_PAL + " Une cada tarjeta con su significado. 1) dibujo de un círculo con rayos y la palabra «antü» 2) dibujo de un suelo con pasto y la palabra «mapu». Escribe los dos significados en orden.", "sol, tierra", "La ficha dice que «antü» es sol y «mapu» es tierra."),
        arith("Tienes 6 tarjetas. Ya leíste 4 con ayuda de la ficha. ¿Cuántas faltan?", "6 - 4", "Resto las leídas del total."),
        ex(FICHA_PAL + " La educadora te ayuda a leer la palabra «ko» en voz alta. ¿Qué tipo de apoyo es: oral o visual?", "oral", "Es escuchar a alguien que sabe."),
    ],
    Z=[
        ex(FICHA_PAL + " Tarjeta con dibujo de una luna y la palabra «antü». Luis dice que «antü» es luna por el dibujo. ¿Tiene razón?", "No", "La ficha dice que «antü» es sol."),
        ex("Ana dice: «Ya sé decir bien la palabra porque leí las letras». ¿Qué le falta para saber su pronunciación?", "escuchar a quien conoce la lengua", "La pronunciación se aprende escuchando."),
    ],
    D=[
        ex(FICHA_PAL + " Tarjeta: dibujo de un círculo amarillo y la palabra «antü». Otra tarjeta: dibujo de una luna y «kuyen». ¿Cuál de las dos habla del día?", "antü", "El sol es del día; «antü» es sol."),
        arith("Cada tarjeta tiene 1 dibujo y 1 palabra. Si hay 5 tarjetas, ¿cuántas cosas debes mirar en total?", "5 * 2", "Cinco tarjetas por dos cosas cada una."),
    ],
    context=[ex(FICHA_PAL + " En una pared de tu escuela ves un dibujo de una casa con la palabra «ruka». Un niño dice: «Debe ser una escuela». ¿Qué haces: reviso la ficha o acepto lo que dijo?", "reviso la ficha", "La ficha dice que «ruka» es casa.")],
    selfcheck=[
        ex("¿Qué tres apoyos uso para leer una palabra?", "oral, visual y la ficha", "Los tres juntos ayudan a entender."),
        ex("¿Dónde confirmo el significado de «mapu»?", "en la ficha", "La ficha dice que es tierra."),
        ex("¿Aprendo la pronunciación mirando las letras o escuchando a quien sabe?", "escuchando a quien sabe", "La pronunciación no se adivina."),
    ],
    task=T(
        "Haz tu propia tabla de lectura con tres tarjetas, usando la ficha de palabras. Para cada una dibuja el apoyo visual, escribe la palabra en mapuzugun y el significado que dice la ficha. Por ejemplo, «ko» con gotas de agua. Elige tres entre ko, antü, kuyen, ruka, mapu o ñuke. Después escribe una pregunta para la educadora tradicional sobre cómo se lee una de ellas en voz alta.",
        "Tarjeta 1: gotas de agua, «ko» = agua. Tarjeta 2: sol, «antü» = sol. Tarjeta 3: luna, «kuyen» = luna. Pregunta: ¿puede leer «kuyen» en voz alta para que lo escuche?",
        ["dibuja un apoyo visual claro para cada palabra", "el significado coincide con la ficha", "no inventa pronunciación", "hace una pregunta a la educadora"],
        ["tabla de tres tarjetas con dibujos", "pregunta escrita o dicha en voz alta"],
        ["cambiar el significado de la ficha", "escribir cómo suena la palabra sin haberla escuchado"],
        "Valora que dibujo y ficha coinciden; si el dibujo no coincide con la ficha, pídele que lo ajuste.",
    ),
    reinforce="Mira la ficha de palabras y empareja «ko», «antü» y «kuyen» con un dibujo sencillo para cada una.",
    extend="Cuenta a alguien cómo usaste el dibujo, la ficha y a la educadora para leer una palabra.",
)

L(
    LF3, 3,
    materials="Lápiz y hoja. La nota de práctica está escrita en este cuaderno. Es inventada, está en castellano y trae una palabra de la ficha.",
    use="Aprenderé a separar lo que dice un texto de lo que yo ya sé, y a relacionar las dos cosas. Sirve para comprender mejor sin mezclar mis ideas con el texto.",
    prior=["Sé leer una palabra con ayuda de la ficha.", "Sé que debo separar el dato de la fuente de mi opinión."],
    explain=[
        "Un texto entrega información: datos que están escritos en él. Yo también tengo conocimientos: cosas que aprendí en la escuela, en mi casa o por mi cuenta. Comprender un texto es relacionar las dos cosas sin mezclarlas.",
        "Para no mezclar, uso dos columnas. En una escribo «El texto dice…» y en otra «Yo sé que…». Lo que está en el texto lo subrayo. Lo que sé yo lo escribo aparte. Así veo qué viene del texto y qué viene de mí.",
        "Cuando mi conocimiento ayuda a entender el texto, lo digo con «yo sé que». Si mi conocimiento no coincide con el texto, no lo borro, pero tampoco lo pongo como dato del texto. No atribuyo el texto a un pueblo si no lo dice.",
    ],
    vocab=[("información", "datos que dice un texto"), ("conocimiento", "lo que ya sé por haberlo aprendido"), ("relacionar", "unir dos cosas que tienen que ver"), ("subrayar", "marcar con una línea lo que dice el texto"), ("atribuir", "decir de quién es o de dónde viene algo")],
    worked=[
        W("Separar texto y conocimiento", "Nota de práctica (inventada): «En mi escuela cuidamos el ko. Cerramos la llave cuando terminamos de lavarnos las manos». Ficha: «ko» es agua en mapuzugun. ¿Qué dice el texto que hacen en la escuela?", ["Subrayo lo que dice el texto.", "Dice que cuidan el agua y cierran la llave al terminar.", "Eso es información del texto."], "Cuidan el agua y cierran la llave cuando terminan de lavarse las manos"),
        W("Agregar lo que yo sé", "Sigo con la misma nota. Yo sé que las plantas necesitan agua para crecer. ¿Cómo lo escribo?", ["Esto no está en el texto.", "Es un conocimiento mío.", "Lo escribo con «Yo sé que…»."], "Yo sé que las plantas necesitan agua para crecer"),
    ],
    mistakes=[
        M("Escribir lo que yo sé como si lo dijera el texto.", "Mezclo mi idea con la información.", "Uso las columnas «El texto dice» y «Yo sé que»."),
        M("Decir de qué pueblo es el texto si no lo dice.", "Puedo atribuirlo mal.", "Escribo solo lo que dice y pregunto la procedencia."),
    ],
    R=[
        ex("Lo que está escrito en el texto se llama: A) información del texto B) mi conocimiento.", "A", "La información está en el texto."),
        ex("Lo que yo aprendí antes se llama: A) conocimiento B) título.", "A", "Es lo que ya sé."),
        ex("Para no mezclar, ¿uso una columna para el texto y otra para lo que sé yo?", "Sí", "Así veo qué viene de dónde."),
    ],
    C=[
        ex("Nota de práctica: «Cuidamos el ko. Cerramos la llave al terminar». Ficha: «ko» es agua en mapuzugun. ¿Qué cuidan?", "el agua", "La ficha dice que «ko» es agua."),
        ex("Frase: «Yo sé que las plantas necesitan agua». ¿Es información del texto o un conocimiento mío?", "un conocimiento mío", "Empieza con «yo sé que»."),
        ex("Verdadero o falso: puedo decir de qué pueblo es un texto aunque no lo diga.", "Falso", "No debo atribuirlo si no lo dice."),
    ],
    A=[
        ex("Nota de práctica: «Regamos el patio solo en la mañana». ¿Cuándo riegan, según el texto?", "en la mañana", "El texto lo dice."),
        arith("En la nota hay 3 datos del texto. Yo agrego 2 cosas que sé. ¿Cuántas ideas hay en total en mis dos columnas?", "3 + 2", "Sumo las dos columnas."),
        ex("Clasifica: «Cerramos la llave al terminar» y «Yo sé que el agua es necesaria». ¿Cuál es del texto? Escribe 1 o 2 según el orden.", "1", "La primera frase es la del texto."),
    ],
    Z=[
        ex("Tomás dice: «El texto dice que el agua es necesaria para la vida». El texto no lo dice, es lo que él sabe. ¿Qué debe cambiar?", "decir «Yo sé que…»", "Es un conocimiento suyo, no del texto."),
        ex("Una niña dice: «Ese texto es de un pueblo de la zona norte». El texto no dice nada de eso. ¿Tiene razón? Responde Sí o No.", "No", "No se debe atribuir un texto sin que lo diga."),
    ],
    D=[
        ex("Nota de práctica: «En mi escuela cuidamos el ko». Ficha: «ko» es agua. Une las dos cosas: ¿qué escribes en la columna «El texto dice»?", "que en la escuela cuidan el agua", "Es el dato que entrega el texto con la ficha."),
        arith("Escribes 4 frases en «El texto dice» y 3 en «Yo sé que». ¿Cuántas frases tienes en total?", "4 + 3", "Sumo las dos columnas."),
    ],
    context=[ex("En tu casa o escuela ves una nota que dice: «Cerrar el ko después de usar». Ficha: «ko» es agua. Tu hermano dice que sabe que cerrar la llave ahorra agua. ¿Eso es información de la nota o un conocimiento de tu hermano?", "un conocimiento de tu hermano", "La nota solo dice cerrar el agua.")],
    selfcheck=[
        ex("¿Qué columna uso para lo que dice el texto?", "El texto dice", "Así separo el dato."),
        ex("¿Con qué frase escribo mi conocimiento?", "Yo sé que", "Eso lo distingue del texto."),
        ex("¿Debo atribuir un texto a un pueblo si no lo dice?", "No", "No debo adivinar su procedencia."),
    ],
    task=T(
        "Lee la nota de práctica inventada: «En la escuela, antes de salir a recreo, cerramos la llave del ko y apagamos la luz de la sala». Ficha: «ko» es agua en mapuzugun. Haz una tabla de dos columnas. En «El texto dice» escribe dos datos de la nota. En «Yo sé que» escribe dos cosas que sabes tú sobre el agua o sobre cuidar las cosas. Después escribe una pregunta para la educadora tradicional sobre el agua en su comunidad.",
        "El texto dice: cerramos la llave del agua; apagamos la luz. Yo sé que el agua es necesaria para las plantas; yo sé que la luz gasta energía. Pregunta: ¿cómo cuida el agua su comunidad?",
        ["escribe dos datos del texto", "escribe dos conocimientos propios", "no mezcla ambas columnas", "hace una pregunta a la educadora"],
        ["tabla de dos columnas", "pregunta escrita o dicha en voz alta"],
        ["escribir sus ideas como dato del texto", "atribuir la nota a un pueblo"],
        "Revisa que no mezcló columnas; si lo hizo, ayúdalo a mover cada idea a su lugar.",
    ),
    reinforce="Lee una instrucción corta de tu casa o escuela y di qué dice el texto y qué sabes tú sobre eso.",
    extend="Haz otra tabla con una nota inventada por ti, de tres frases, separando lo que dice y lo que sabes.",
)

L(
    LF3, 4,
    materials="Lápiz y hoja. La carta de práctica está escrita en este cuaderno. Es inventada, está en castellano y trae una expresión de la ficha.",
    use="Aprenderé a responder a un texto diciendo qué sentí y qué límites tengo. Sirve para responder con honestidad sin tener que fingir que sé más.",
    prior=["Sé separar lo que dice el texto de lo que sé yo.", "Sé que algunas cosas las enseña el educador tradicional."],
    explain=[
        "Un texto puede hacerme sentir algo. Puedo sentir alegría, curiosidad, calma o sorpresa. Responder a un texto es decir lo que sentí y por qué. No hay una emoción correcta: cada persona puede sentir distinto.",
        "Cuando respondo, también digo mis límites. Un límite es lo que no sé o no entendí. Por ejemplo: «No sé cómo se dice en otra lengua». Decirlo es honesto y respetuoso. No finjo que sé algo que no sé.",
        "Mi respuesta no debe obligar a nadie a contar cosas de su casa ni de su cultura. Puedo hablar de lo que sentí con un personaje inventado o con lo que vi. Y cuando tenga dudas culturales, las pregunto al educador o a la educadora tradicional.",
    ],
    vocab=[("responder", "decir qué pienso o siento sobre un texto"), ("emoción", "lo que siento, como alegría o curiosidad"), ("límite", "lo que no sé o no entendí"), ("honesto", "que dice la verdad sobre lo que sabe"), ("duda", "algo que no estoy seguro de entender")],
    worked=[
        W("Responder con emoción", "Carta de práctica (inventada): «Querida profesora: hoy aprendí que «chaltumay» es gracias en mapuzugun. Me dio alegría decírselo a una persona de mi casa». ¿Qué emoción dice la carta?", ["Busco la palabra que dice cómo se sintió.", "Dice «me dio alegría».", "La emoción es alegría."], "alegría"),
        W("Decir un límite", "En la misma carta, la niña agrega: «Todavía no sé cómo se dice gracias en otras lenguas». ¿Qué es esa frase: una emoción o un límite?", ["Veo que dice algo que no sabe.", "Lo que no sé es un límite.", "Es un límite."], "un límite"),
    ],
    mistakes=[
        M("Decir una emoción porque creo que es la que corresponde.", "Cada persona siente lo que siente.", "Digo lo que de verdad sentí."),
        M("Fingir que sé algo que no sé.", "Parece que sé más de lo que sé.", "Digo mi límite y pregunto."),
    ],
    R=[
        ex("Carta: «Me dio alegría decirlo». ¿Qué emoción aparece?", "alegría", "La carta nombra alegría."),
        ex("Lo que no sé o no entendí se llama: A) límite B) título.", "A", "Un límite es lo que no sé."),
        ex("Si no sé algo, ¿lo digo con honestidad o finjo?", "lo digo con honestidad", "Decir mi límite es respetuoso."),
    ],
    C=[
        ex("Verdadero o falso: hay una sola emoción correcta para cada texto.", "Falso", "Cada persona puede sentir distinto."),
        ex("Carta de práctica: «Todavía no sé cómo se dice gracias en otras lenguas». ¿Es una emoción o un límite?", "un límite", "Dice algo que la niña no sabe."),
        ex("Frase: «Sentí curiosidad por saber más». ¿Es una emoción o un dato del texto?", "una emoción", "Dice cómo se sintió."),
    ],
    A=[
        ex("Elige la mejor respuesta: A) «Sentí alegría porque aprendí una palabra, pero no sé cuándo se usa.» B) «Todo me da lo mismo.»", "A", "A dice una emoción y un límite."),
        arith("Una respuesta tiene 1 emoción y 2 límites. ¿Cuántas ideas dice mi respuesta?", "1 + 2", "Sumo la emoción y los límites."),
        ex("Elige la mejor pregunta para la educadora: A) «¿Me puede explicar cuándo se usa «chaltumay»?» B) «Ya sé cuándo se usa.»", "A", "A pregunta con respeto lo que no sé."),
    ],
    Z=[
        ex("Rosa dice: «Si digo que no sé algo, mi respuesta vale menos». ¿Tiene razón? Responde Sí o No.", "No", "Decir lo que no sé es honesto."),
        ex("Un compañero pide: «Cuéntanos todo lo que pasa en tu casa cuando usan esa palabra». ¿Qué le respondes: que prefieres no contarlo o que lo cuentas todo?", "que prefieres no contarlo", "Nadie debe contar cosas privadas."),
    ],
    D=[
        ex("Ordena los pasos de una respuesta: C) pregunto lo que no sé A) digo lo que sentí B) digo mi límite. Escribe las letras.", "A, B, C", "Digo emoción, límite y pregunta."),
        arith("Escribes 2 frases sobre lo que sentiste y 3 sobre lo que no sabes. ¿Cuántas frases escribes en total?", "2 + 3", "Sumo ambas partes."),
    ],
    context=[ex("Una compañera lee tu respuesta y dice: «Tienes que sentir alegría, es lo correcto». ¿Qué le dices: «Yo sentí curiosidad» o «Tienes razón, cambiaré lo que sentí»?", "«Yo sentí curiosidad»", "Digo lo que de verdad sentí.")],
    selfcheck=[
        ex("¿Cómo llamo a lo que no sé o no entendí?", "límite", "Es lo que no sé."),
        ex("¿Hay una emoción única correcta ante un texto?", "No", "Cada persona siente distinto."),
        ex("¿A quién pregunto mis dudas culturales?", "al educador tradicional o a la comunidad", "Ellos pueden enseñar."),
    ],
    task=T(
        "Lee la carta inventada: «Querida profesora: hoy leí que «chaltumay» es gracias en mapuzugun. Me dio curiosidad. Aún no sé cuándo se dice». Escribe tu propia respuesta a la carta en tres frases: 1) qué sentiste tú al leerla (la emoción que de verdad sentiste), 2) un límite tuyo, 3) una pregunta para el educador o la educadora tradicional. No cuentes nada privado de tu familia.",
        "Sentí tranquilidad porque la carta es amable. No sé cómo se dice «chaltumay» en voz alta. ¿Puede enseñarme cómo se dice?",
        ["dice una emoción propia", "dice un límite honesto", "hace una pregunta al educador/a", "no cuenta nada privado"],
        ["tres frases escritas", "lectura en voz alta"],
        ["copiar la emoción de la carta sin sentirla", "contar cosas privadas"],
        "Valora la honestidad; si copió la emoción de la carta, pregúntale cómo se sintió él o ella.",
    ),
    reinforce="Di en una frase qué sentiste al leer la carta de práctica.",
    extend="Escribe una respuesta más a otro texto corto que conozcas, con una emoción, un límite y una pregunta.",
)

L(
    LF3, 5,
    materials="Lápiz y hoja. Las tarjetas de práctica y la ficha están en este cuaderno. Son inventadas.",
    use="Aprenderé a comparar dos pistas de un texto y a decidir qué hacer cuando no coinciden. Sirve para comprender con cuidado y no quedarme con lo primero que pienso.",
    prior=["Sé leer una tarjeta con dibujo y ficha.", "Sé que no debo adivinar significados."],
    explain=[
        "Un texto da pistas. Dos pistas pueden coincidir o no. Contrastar es compararlas y ver si dicen lo mismo. Las pistas que uso son el dibujo, la palabra y la ficha. Cuando las tres coinciden, estoy más seguro de lo que entendí.",
        "A veces las pistas no coinciden. Por ejemplo, un dibujo de una luna con la palabra «antü», y la ficha dice que «antü» es sol. Entonces no decido yo. Anoto que las pistas no coinciden y pregunto a la educadora o al educador.",
        "También puedo ver cuál pista es más confiable. Una ficha hecha con la educadora tradicional es más confiable que mi idea. Un dibujo sin autor es una ayuda, pero no una fuente. Así evito errores.",
    ],
    vocab=[("contrastar", "comparar dos cosas para ver si coinciden"), ("coincidir", "decir lo mismo"), ("confiable", "que se puede creer porque viene de una buena fuente"), ("pista", "dato que ayuda a entender"), ("decidir", "elegir una respuesta")],
    worked=[
        W("Pistas que coinciden", FICHA_PAL + " Tarjeta: dibujo de una casa y la palabra «ruka». ¿Las pistas coinciden?", ["El dibujo muestra una casa.", "La ficha dice que «ruka» es casa.", "Las dos pistas coinciden."], "Sí, coinciden"),
        W("Pistas que no coinciden", FICHA_PAL + " Tarjeta: dibujo de una luna y la palabra «antü». ¿Qué hago?", ["El dibujo es una luna.", "La ficha dice que «antü» es sol.", "No coinciden; pregunto a la educadora."], "Las pistas no coinciden; pregunto a la educadora"),
    ],
    mistakes=[
        M("Quedarme con la primera pista que miré.", "Puede estar equivocada.", "Comparo las pistas antes de decidir."),
        M("Decidir yo cuando las pistas no coinciden.", "Puedo equivocarme y enseñar algo falso.", "Anoto que no coinciden y pregunto."),
    ],
    R=[
        ex("Comparar dos cosas para ver si dicen lo mismo se llama: A) contrastar B) borrar.", "A", "Contrastar es comparar."),
        ex("Si el dibujo y la ficha dicen lo mismo, las pistas: A) coinciden B) no coinciden.", "A", "Las dos pistas coinciden."),
        ex("Si dos pistas no coinciden, ¿pregunto o decido yo solo?", "pregunto", "No decido sin saber."),
    ],
    C=[
        ex(FICHA_PAL + " Tarjeta: dibujo de una luna y la palabra «kuyen». ¿Las pistas coinciden?", "Sí", "La ficha dice que «kuyen» es luna."),
        ex(FICHA_PAL + " Tarjeta: dibujo de una casa y la palabra «mapu». ¿Las pistas coinciden?", "No", "La ficha dice que «mapu» es tierra, no casa."),
        ex("Verdadero o falso: una ficha hecha con la educadora tradicional es más confiable que mi idea.", "Verdadero", "Viene de una buena fuente."),
    ],
    A=[
        ex(FICHA_PAL + " Dos tarjetas: A) dibujo de un sol y «antü» B) dibujo de agua y «kuyen». ¿En cuál coinciden las pistas?", "A", "En A, «antü» es sol; en B, «kuyen» no es agua."),
        arith("Revisas 5 tarjetas y 2 tienen pistas que no coinciden. ¿En cuántas coinciden?", "5 - 2", "Resto las que no coinciden."),
        ex(FICHA_PAL + " Tarjeta: dibujo de una madre con su hijo y la palabra «ñuke». ¿Las pistas coinciden?", "Sí", "La ficha dice que «ñuke» es madre."),
    ],
    Z=[
        ex("Luis dice: «El dibujo es una luna, así que «antü» es luna». La ficha dice que «antü» es sol. ¿Qué debe hacer?", "preguntar a la educadora", "Las pistas no coinciden."),
        ex("Ana dice: «Mejor me quedo con la ficha que hizo la educadora que con lo que me imagino». ¿Tiene razón? Responde Sí o No.", "Sí", "La ficha viene de una fuente confiable."),
    ],
    D=[
        ex("¿Qué es más confiable para saber qué dice «ñuke»: A) una idea mía sin fuente B) la ficha hecha con la educadora?", "B", "La ficha viene de una buena fuente."),
        arith("Comparas 3 pistas en cada una de 4 tarjetas. ¿Cuántas pistas comparas en total?", "3 * 4", "Tres pistas por cuatro tarjetas."),
    ],
    context=[ex(FICHA_PAL + " En un cartel de tu escuela ves un dibujo de agua y la palabra «antü». Tu compañero dice: «Está bien». ¿Qué haces: comparo con la ficha y pregunto a la educadora o acepto sin revisar?", "comparo con la ficha y pregunto a la educadora", "La ficha dice que «antü» es sol, no agua.")],
    selfcheck=[
        ex("¿Qué hago cuando dos pistas no coinciden?", "pregunto", "No decido sin saber."),
        ex("¿Qué pista es más confiable: una ficha hecha con la educadora o mi idea?", "la ficha", "Viene de una buena fuente."),
        ex("¿Cómo se llama comparar dos pistas?", "contrastar", "Contrastar es comparar."),
    ],
    task=T(
        "Revisa estas tres tarjetas inventadas con la ficha de palabras: A) dibujo de una casa y «ruka»; B) dibujo de una luna y «antü»; C) dibujo de agua y «ko». En una tabla escribe si en cada una las pistas coinciden o no, y qué haces si no coinciden. Después escribe una pregunta para la educadora tradicional sobre una de las palabras.",
        "A: coinciden (ruka = casa). B: no coinciden (antü = sol, el dibujo es luna); pregunto a la educadora. C: coinciden (ko = agua). Pregunta: ¿cómo se dice «luna» en mapuzugun?",
        ["revisa las tres tarjetas con la ficha", "dice correctamente cuándo coinciden", "pregunta cuando no coinciden", "hace una pregunta a la educadora"],
        ["tabla de tres filas", "pregunta escrita o dicha en voz alta"],
        ["decidir solo cuando no coinciden", "cambiar el significado de la ficha"],
        "Valora que comparó antes de decidir; si decidió sin ficha, pídele que revise y pregunte.",
    ),
    reinforce="Con la ficha, compara dos tarjetas inventadas por ti: una con pistas que coinciden y otra con pistas que no.",
    extend="Inventa una tarjeta con dibujo y palabra de la ficha para que otra persona decida si las pistas coinciden.",
)
