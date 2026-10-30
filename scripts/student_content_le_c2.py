"""Cuaderno del estudiante, 1.º básico Lenguaje y Comunicación: OA 21 (conversaciones grupales) y OA 22 (cortesía y convenciones sociales)."""
from __future__ import annotations

from student_lessons import ex, register

OA21, OA22 = "LE01 OA 21", "LE01 OA 22"
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


# ================================================================ OA 21
reg(
    OA21, 1,
    "Los diálogos escritos en este cuaderno, lápiz y hoja. Para practicar se necesitan dos o tres personas de la casa, o muñecos que hagan de participantes.",
    "Aprenderé que en una conversación cada persona habla en su turno y que lo que dice una conecta con lo que dijo la anterior. Sirve para conversar con mi curso y mi familia.",
    ["Sé hablar con otra persona.", "Sé escuchar sin interrumpir por un momento."],
    [
        "Una conversación es cuando dos o más personas hablan sobre un tema. Todas aportan ideas, y por eso es como tejer una tela: cada voz es un hilo que se une a los otros. Para que la conversación funcione, hay que respetar los turnos. Un turno es el momento en que habla una persona.",
        "Mientras otra persona habla, yo escucho con atención y no hablo al mismo tiempo. Cuando termina, puedo hablar yo. Es mejor que mi idea tenga relación con el tema. Por ejemplo, si hablamos de juegos del recreo, no cuento de repente qué comí en la mañana.",
        "Una buena forma de conectar es usar la idea de la otra persona. Puedo decir: «Yo también juego a la pelota» o «Yo prefiero la cuerda». Así los demás notan que escuché y la conversación sigue unida.",
    ],
    [("conversación", "hablar entre varias personas sobre un tema"), ("turno", "momento en que habla una persona"), ("tema", "de qué se está hablando"), ("aportar", "agregar una idea"), ("interrumpir", "hablar cuando otro está hablando")],
    [
        ("Respetar el turno", "Ana cuenta que le gusta saltar la cuerda. Beto la interrumpe para hablar de su perro. ¿Qué debió hacer Beto?", ["Ana todavía estaba hablando.", "Beto debe esperar a que termine.", "Después puede decir su idea."], "Beto debe esperar su turno."),
        ("Conectar con el tema", "El tema es «juegos del recreo». Ana dice: «Me gusta la cuerda». ¿Qué puede decir Beto para conectar su idea?", ["Escucha lo que dijo Ana.", "Piensa en un juego del recreo.", "Lo dice con relación al tema."], "Beto puede decir: «A mí me gusta la pelota»."),
    ],
    [("Hablar todos al mismo tiempo.", "Hay muchas ganas de contar algo.", "Levanta la mano o espera a que el otro termine."), ("Cambiar el tema de repente.", "Se olvida de qué se habla.", "Agrega una idea relacionada con el tema.")],
    [
        E("Diálogo: Ana: «Me gusta la cuerda». Beto: «A mí, la pelota». ¿Quién habló primero?", "Ana", "Ana abre la conversación."),
        E("¿Hablo mientras otra persona está hablando?", "No", "Debo esperar mi turno."),
        E("Tema: mascotas. ¿Una idea relacionada es «Mi gato duerme mucho» o «Hoy llueve»?", "Mi gato duerme mucho", "Habla de una mascota, el mismo tema."),
    ],
    [
        E("¿Qué es un turno de habla?", "El momento en que habla una persona", "Cada persona tiene el suyo."),
        E("¿Por qué conviene respetar los turnos?", "Para que todos se escuchen", "Si hablan juntos nadie entiende."),
        E("¿Qué significa aportar una idea?", "Agregar algo que pienso al tema", "Así se construye la conversación."),
    ],
    [
        E("Tema: frutas. Luz dice: «Me gusta la sandía». Escribe una frase que conecte con Luz.", "Por ejemplo: A mí también me gusta la sandía", "Habla del mismo tema y de lo dicho por Luz."),
        E("Tema: el recreo. Pedro dice: «Jugamos a la escondida». Escribe una idea relacionada.", "Por ejemplo: Yo me escondí detrás del árbol", "Está relacionada con el juego."),
        E("Tres niños hablan por turnos: Ana, Beto y Carla. ¿Cuántos turnos hay en total si cada uno habla una vez?", "3", "Cada niño tiene un turno."),
    ],
    [
        E("Diálogo: Tema «animales». Ana: «Me gustan los perros». Beto: «Ayer comí pizza». ¿Beto conectó con el tema?", "No", "Habló de comida, no de animales."),
        E("En una conversación, dos niños hablan juntos y no se entiende nada. ¿Qué regla no respetaron?", "Los turnos", "Debieron hablar uno a la vez."),
    ],
    [
        E("Tema: juegos. Ana: «Me gusta saltar». Beto: «A mí me gusta pintar». Carla: «A mí también saltar, Ana». ¿Quién conectó directamente con otra persona?", "Carla", "Mencionó la idea de Ana."),
        E("Diálogo: Luz: «Mi abuela hace pan». Mateo: «Qué rico, mi abuelo también cocina». ¿Mateo conectó?", "Sí", "Usó la idea de Luz y agregó la suya."),
    ],
    [E("En el recreo, tu grupo habla de qué jugar. Luz dice «A la pelota». Tú prefieres la cuerda. ¿Qué puedes decir sin interrumpir y conectando?", "Por ejemplo: Yo prefiero la cuerda; podemos jugar las dos", "Respeta el turno y se relaciona con el tema.")],
    [
        E("¿Qué hago mientras otro habla?", "Escucho en silencio", "Así respeto su turno."),
        E("Si quiero hablar, ¿qué hago: levanto la mano o grito?", "Levanto la mano", "Es una forma respetuosa."),
        E("Tema: colores. ¿Qué frase conecta: «Mi color es el verde» o «Tengo hambre»?", "Mi color es el verde", "Habla del tema colores."),
    ],
    ("Conversa en voz alta con dos personas de tu casa sobre este tema: «¿Qué juego nos gusta?». Cada uno habla una vez por turno. Tú dices tu idea y luego conectas con la de una persona usando la frase «Yo también…» o «Yo prefiero…». Al final, pide a una persona que te diga si respetaste los turnos.",
     "Mamá dijo: me gusta el dominó. Papá dijo: a mí, las cartas. Yo dije: a mí me gusta la cuerda. Luego dije: yo también juego dominó, mamá. Esperé mi turno y no interrumpí.",
     ["espera su turno", "dice una idea sobre el tema", "conecta con la idea de otra persona"], ["adulto observa los turnos y anota si conectó"], ["interrumpir", "hablar de otro tema"],
     "Si interrumpió, vuelve a practicar con una señal: tocar el hombro del que habla significa esperar."),
    "Cuenta a un adulto cuántas veces esperaste tu turno hoy.",
    "Conversa con un adulto sobre «mi comida favorita» y conecta tres veces con lo que dice.",
)

reg(
    OA21, 2,
    "Las frases modelo de este cuaderno, lápiz y hoja. Se puede practicar con un adulto o frente a un espejo.",
    "Aprenderé a dar mi opinión y a explicarla con una razón. Sirve para que los demás entiendan por qué pienso así.",
    ["Sé respetar turnos.", "Sé decir lo que me gusta."],
    [
        "Cuando das una opinión, dices lo que piensas o prefieres. Por ejemplo: «Yo prefiero jugar a la pelota». Pero para que los demás entiendan, conviene agregar una razón. La razón dice por qué piensas así, y se une con la palabra «porque».",
        "Una frase con razón se arma en dos partes. Primero va lo que creo: «Prefiero la cuerda». Después va la razón: «porque puedo saltar con mis amigas». Quedaría: «Prefiero la cuerda porque puedo saltar con mis amigas». La razón debe tener relación con la opinión.",
        "También puedes usar otras palabras, como «creo que» o «me parece que». Por ejemplo: «Creo que debemos jugar a las escondidas porque participan todos». Con una razón clara, tu idea se entiende mejor y los demás pueden contestarte.",
    ],
    [("opinión", "lo que pienso o prefiero"), ("razón", "el motivo de mi opinión"), ("porque", "palabra que une opinión y razón"), ("creo que", "forma de empezar una opinión"), ("explicar", "decir por qué")],
    [
        ("Armar una frase con razón", "Opinión: «Prefiero el helado de frutilla». Razón: «es dulce y fresco». Júntalas.", ["Escribo la opinión.", "Agrego «porque».", "Escribo la razón."], "Prefiero el helado de frutilla porque es dulce y fresco."),
        ("Reconocer la razón", "En «Creo que debemos reciclar porque cuidamos el planeta», ¿cuál es la razón?", ["Busco la palabra «porque».", "La razón va después.", "Es «cuidamos el planeta»."], "La razón es «cuidamos el planeta»."),
    ],
    [("Dar la opinión sin razón.", "Se cree que basta con decir lo que gusta.", "Agrega «porque» y un motivo."), ("Dar una razón que no tiene relación.", "Se dice lo primero que se ocurre.", "Piensa si la razón explica de verdad la opinión.")],
    [
        E("En «Prefiero la cuerda porque puedo saltar», ¿cuál es la opinión?", "Prefiero la cuerda", "Es lo que la persona piensa o prefiere."),
        E("En «Prefiero la cuerda porque puedo saltar», ¿cuál es la razón?", "Puedo saltar", "Va después de «porque»."),
        E("¿Qué palabra une la opinión con su razón?", "Porque", "Introduce el motivo."),
    ],
    [
        E("¿Para qué sirve dar una razón?", "Para que los demás entiendan por qué pienso así", "La razón explica la opinión."),
        E("¿La frase «Me gusta el verano porque hace calor» tiene razón?", "Sí", "Después de «porque» está el motivo."),
        E("¿Es mejor decir «No quiero» o «No quiero porque tengo frío»?", "No quiero porque tengo frío", "La segunda explica el motivo."),
    ],
    [
        E("Completa: «Prefiero el parque porque ___». Escribe una razón.", "Por ejemplo: hay columpios", "Es un motivo coherente con el parque."),
        E("Une: opinión «Quiero jugar a las escondidas» y razón «participan todos».", "Quiero jugar a las escondidas porque participan todos", "Se unen con «porque»."),
        E("Escribe una opinión con razón sobre tu animal favorito.", "Por ejemplo: Mi animal favorito es el perro porque me cuida", "Tiene opinión y razón."),
    ],
    [
        E("Ana dice: «Hay que ordenar la sala porque está limpia». ¿La razón explica la opinión?", "No", "Si ya está limpia, no hay motivo para ordenarla."),
        E("Beto dice: «Quiero la fruta porque me gusta y es sana». ¿Cuántas razones dio?", "2", "Son dos: le gusta y es sana."),
    ],
    [
        E("Elige la mejor razón para «Debemos lavarnos las manos»: a) porque es lunes, b) porque así quedan limpias.", "b", "La razón b explica el motivo de lavarse."),
        E("Luz dice: «Creo que debemos caminar en la fila porque así nadie se golpea». Escribe su opinión.", "Debemos caminar en la fila", "Es lo que piensa antes de «porque»."),
    ],
    [E("Tu grupo debe decidir qué cuento leer: «el zorro» o «la tortuga». Tú prefieres «la tortuga». Di tu opinión con razón.", "Por ejemplo: Prefiero el de la tortuga porque es corto", "Tiene opinión y razón coherente.")],
    [
        E("¿Una opinión puede ir con «porque»?", "Sí", "Se usa para dar la razón."),
        E("Completa: «Me gusta leer porque ___».", "Por ejemplo: aprendo cosas nuevas", "La razón explica el gusto."),
        E("¿Qué va después de «porque»?", "La razón", "Es el motivo de lo que pienso."),
    ],
    ("Escribe y di en voz alta tres frases con «porque». Frase 1: sobre qué juego prefieres entre pelota, cuerda y escondidas. Frase 2: sobre qué fruta prefieres entre manzana, plátano y naranja. Frase 3: sobre qué cuento quieres escuchar esta noche entre «el zorro» y «la tortuga». Cada frase lleva tu opinión y una razón.",
     "1) Prefiero la cuerda porque puedo saltar con mis amigas. 2) Prefiero el plátano porque es suave y dulce. 3) Quiero el cuento de la tortuga porque es corto y me gusta el final.",
     ["cada frase tiene opinión y razón", "usa «porque»", "la razón explica la opinión"], ["tres frases dichas en voz alta y escritas"], ["razón sin relación", "frase sin porque"],
     "Si falta razón, pregunta: ¿por qué? y pide que la agregue después de «porque»."),
    "Dile a un adulto una opinión con «porque» sobre tu comida favorita.",
    "Da dos razones distintas para la misma opinión.",
)

reg(
    OA21, 3,
    "Los diálogos escritos en este cuaderno, lápiz y hoja. Para practicar se necesita un adulto o un compañero que hable y otro que escuche.",
    "Aprenderé a mostrar que escuché lo que dijo otra persona. Sirve para que la persona se sienta escuchada y para continuar bien la conversación.",
    ["Sé respetar turnos.", "Sé dar una opinión con razón."],
    [
        "Escuchar bien no es solo callarse. También es mostrar que entendí. Puedo mirar a la persona, hacer un gesto con la cabeza y repetir con mis palabras lo que dijo. Por ejemplo, si Ana dice «Me gusta jugar en el patio porque hay espacio», yo puedo decir: «Tú dijiste que te gusta el patio porque hay espacio».",
        "Decir lo que escuché con mis palabras sirve para comprobar si entendí bien. Si me equivoco, la persona me corrige. Después de mostrar que escuché, puedo agregar mi idea o hacer una pregunta sobre lo que dijo.",
        "Hay frases que ayudan: «Tú dijiste que…», «Entiendo que…», «¿Quieres decir que…?». Usarlas hace que la conversación sea más amable y que nadie quede sin ser escuchado.",
    ],
    [("escuchar", "poner atención a lo que otro dice"), ("decir con mis palabras", "contar lo que alguien dijo, usando mis propias palabras"), ("comprobar", "revisar si entendí bien"), ("pregunta", "lo que digo para saber más"), ("gesto", "movimiento que muestra que escucho")],
    [
        ("Decir con mis palabras", "Ana: «Me gusta el patio porque hay espacio para correr.» ¿Cómo muestra Beto que escuchó?", ["Mira a Ana.", "Repite con sus palabras.", "Usa «Tú dijiste que…»."], "Tú dijiste que te gusta el patio porque puedes correr."),
        ("Comprobar con una pregunta", "Luz: «Mi gato duerme todo el día.» ¿Qué pregunta muestra que escuché?", ["Pienso en lo que dijo Luz.", "Hago una pregunta sobre eso.", "Uso «¿Quieres decir que…?»."], "¿Quieres decir que tu gato duerme casi todo el día?"),
    ],
    [("Mirar para otro lado mientras alguien habla.", "Se pierde la atención.", "Mira a la persona y muestra interés."), ("Repetir mal lo que dijo.", "No se prestó atención.", "Escucha con calma y repite solo lo que dijo.")],
    [
        E("Ana dijo: «Me gusta el patio». ¿Qué frase muestra que escuché: «Tú dijiste que te gusta el patio» o «Yo tengo un perro»?", "Tú dijiste que te gusta el patio", "Repite lo que dijo Ana."),
        E("¿Qué hago con mi mirada cuando alguien habla?", "Lo miro", "Mirar muestra atención."),
        E("¿Decir con mis palabras lo que dijo otra persona muestra que escuché?", "Sí", "Así se ve que entendí."),
    ],
    [
        E("¿Por qué conviene mostrar que escuché?", "Para que la persona se sienta escuchada", "Mostrar atención es respeto."),
        E("¿Qué hago si no estoy seguro de haber entendido?", "Pregunto: ¿Quieres decir que…?", "Así compruebo lo entendido."),
        E("¿Callarme es suficiente para mostrar que escuché?", "No", "También debo mostrar que entendí."),
    ],
    [
        E("Beto dijo: «Mi hermano juega fútbol». Escribe una frase que empiece con «Tú dijiste que…».", "Tú dijiste que tu hermano juega fútbol", "Repite lo dicho."),
        E("Carla dijo: «Me asusta la tormenta porque suena muy fuerte». Escribe una pregunta con «¿Quieres decir que…?».", "¿Quieres decir que la tormenta te asusta por lo fuerte que suena?", "Comprueba lo entendido."),
        E("Luis dijo: «Mi abuela me enseñó a tejer». Escribe cómo mostrarías que escuchaste.", "Por ejemplo: Tú dijiste que tu abuela te enseñó a tejer", "Repite el mensaje."),
    ],
    [
        E("Diálogo: Ana: «Me gusta leer porque aprendo cosas». Beto: «Yo tengo una bicicleta roja». ¿Beto mostró que escuchó?", "No", "No habló de lo que dijo Ana."),
        E("Diálogo: Mía: «Hoy no jugué porque me dolía la pierna». Pedro: «Tú dijiste que no jugaste porque te dolía la pierna». ¿Cómo lo hizo Pedro?", "Bien, porque repitió lo que dijo Mía", "Pedro dijo con sus palabras lo que dijo Mía."),
    ],
    [
        E("Eva dice «Mi hermano tiene ocho años». Teo repite «Tu hermano tiene dos años». ¿Qué falló?", "No escuchó bien el dato", "Cambió el número ocho por dos."),
        E("Rosa quiere saber si entendió «Mañana vamos al parque a las tres». Escribe una pregunta de comprobación.", "Por ejemplo: ¿Quieres decir que vamos mañana a las tres al parque?", "Comprueba el dato."),
    ],
    [E("En la clase, tu compañero dice: «Me gustó el cuento porque el perro era valiente». Quieres mostrar que escuchaste y agregar tu idea. ¿Qué dices?", "Por ejemplo: Tú dijiste que te gustó porque el perro era valiente; yo pienso que el final fue lindo", "Primero dice con sus palabras lo que escuchó y luego agrega su idea.")],
    [
        E("¿Qué palabra uso para empezar a repetir lo que dijo otro: «Tú dijiste que…» o «Me da lo mismo»?", "Tú dijiste que…", "Repite lo que dijo."),
        E("¿Qué muestra que escucho: mirar, hacer un gesto con la cabeza o decir con mis palabras lo que oí?", "Todas", "Las tres muestran atención."),
        E("Si me equivoco al repetir, ¿qué puede hacer la otra persona?", "Corregirme", "Así aclaramos el mensaje."),
    ],
    ("Lee el diálogo con un adulto: Persona A: «Me gusta la plaza porque hay columpios y mi tía me lleva». Persona B: «…» Escribe y di lo que respondería B para mostrar que escuchó (usa «Tú dijiste que…») y agrega una pregunta. Luego representa el diálogo con tu adulto cambiando de papel.",
     "B: Tú dijiste que te gusta la plaza porque hay columpios y tu tía te lleva. ¿Qué columpio te gusta más? Practiqué mirando a A y asintiendo.",
     ["repite lo dicho con sus palabras", "agrega una pregunta", "mira a la persona"], ["frase escrita y dicha en voz alta"], ["cambiar los datos", "no hacer pregunta"],
     "Si cambió algún dato, relee el diálogo y corrige solo ese dato."),
    "Repite hoy con tus palabras algo que alguien te haya dicho.",
    "Di con tus palabras dos veces seguidas lo que dice un adulto y pide que te diga si lo entendiste bien.",
)

reg(
    OA21, 4,
    "Los diálogos escritos en este cuaderno, lápiz y hoja. Para practicar, un adulto o compañero puede hacer de otro participante.",
    "Aprenderé a decir que pienso distinto y a hacer preguntas, siempre con respeto. Sirve para conversar sin pelear cuando no estamos de acuerdo.",
    ["Sé dar una opinión con razón.", "Sé mostrar que escuché."],
    [
        "No siempre pensamos igual que los demás. Eso es normal y puede ser interesante. Disentir significa decir que pienso diferente. Se puede hacer con respeto si primero escucho y después explico mi idea con una razón. Por ejemplo: «Yo pienso distinto porque a mí me gusta más la cuerda».",
        "Una forma amable de disentir empieza con «Entiendo que…» o «Puede ser, pero yo pienso…». Nunca digo «eso es tonto» ni me burlo. Digo lo que pienso y por qué. Así la otra persona puede escucharme sin molestarse.",
        "Preguntar también ayuda a entender a los demás. Puedo preguntar: «¿Por qué piensas eso?» o «¿Me explicas?». Las preguntas muestran curiosidad y respeto. Si alguien tiene una razón distinta a la mía, quizás aprendo algo nuevo.",
    ],
    [("disentir", "decir que pienso diferente"), ("respeto", "tratar bien a los demás aunque piensen distinto"), ("preguntar", "pedir que me expliquen"), ("burla", "reírse de lo que otro dice"), ("acuerdo", "cuando dos personas piensan igual")],
    [
        ("Disentir con respeto", "Ana dice: «Debemos jugar a la pelota». Beto prefiere la cuerda. ¿Cómo puede decirlo con respeto?", ["Escucha a Ana.", "Empieza con «Entiendo que…».", "Da su razón."], "Entiendo que quieres pelota, pero yo prefiero cuerda porque podemos saltar todos."),
        ("Preguntar para entender", "Luz dice: «No me gustan los payasos.» ¿Qué puede preguntar Teo con respeto?", ["Quiere saber más.", "Usa una pregunta abierta.", "No se burla."], "¿Por qué no te gustan los payasos?"),
    ],
    [("Decir «eso es tonto».", "Se piensa que la otra idea no sirve.", "Di «yo pienso distinto porque…»."), ("No dejar hablar al que piensa distinto.", "Se quiere ganar la conversación.", "Escucha y pregunta con curiosidad.")],
    [
        E("¿Es respetuoso decir «eso es tonto» cuando alguien piensa distinto?", "No", "Es una burla, no una razón."),
        E("¿Cuál frase es respetuosa: «Yo pienso distinto porque…» o «Qué mala idea»?", "Yo pienso distinto porque…", "Explica sin ofender."),
        E("Para entender mejor a alguien, ¿qué puedo hacer?", "Preguntar por qué piensa eso", "La pregunta muestra interés."),
    ],
    [
        E("¿Qué significa disentir?", "Decir que pienso diferente", "No se está de acuerdo."),
        E("¿Por qué conviene dar una razón al disentir?", "Para que el otro entienda mi idea", "La razón explica por qué pienso distinto."),
        E("¿Disentir significa pelear?", "No", "Se puede pensar distinto sin pelear."),
    ],
    [
        E("Ana dice «Hoy debemos leer». Tú quieres dibujar. Escribe una frase que empiece con «Entiendo que…».", "Por ejemplo: Entiendo que quieres leer, pero yo prefiero dibujar porque hoy estoy cansado", "Disiente con respeto y razón."),
        E("Beto dice «El verano es mejor que el invierno». Escribe una pregunta para entender por qué.", "Por ejemplo: ¿Por qué piensas que el verano es mejor?", "Pide la razón."),
        E("Luis dice «Los gatos son mejores que los perros». Tú piensas distinto. Escribe cómo lo dices con respeto.", "Por ejemplo: Yo pienso distinto porque los perros juegan conmigo", "Disiente y da razón."),
    ],
    [
        E("Diálogo: Ana: «Prefiero la sopa». Beto: «Qué asco la sopa». ¿Beto fue respetuoso?", "No", "Se burló de la idea de Ana."),
        E("Diálogo: Mía: «No me gusta correr». Teo: «¿Por qué no te gusta?». ¿Qué hizo Teo?", "Preguntó con interés", "Quiso entender la razón de Mía."),
    ],
    [
        E("Dos niñas piensan distinto sobre el color del dibujo: Ana lo quiere azul y Eva rojo. Escribe una solución donde ambas queden contentas.", "Por ejemplo: Usar azul y rojo juntos", "Ambas ideas se incluyen."),
        E("Teo dice: «Eso no me gusta». Escribe cómo preguntarle de manera amable por qué.", "Por ejemplo: ¿Me cuentas por qué no te gusta?", "La pregunta invita a explicar."),
    ],
    [E("En tu grupo, Eva dice «Vamos al columpio». Pedro dice «Mejor al balancín». Tú quieres el resbalín. ¿Qué dices con respeto?", "Por ejemplo: Entiendo, pero yo prefiero el resbalín porque es más rápido; podemos ir a los tres", "Disiente con razón y propone.")],
    [
        E("¿Digo «tu idea es mala»?", "No", "Debo decir por qué pienso distinto."),
        E("¿Qué frase uso al preguntar: «¿Por qué piensas eso?» o «Cállate»?", "¿Por qué piensas eso?", "Es una pregunta respetuosa."),
        E("Si dos personas piensan distinto, ¿pueden conversar?", "Sí", "Se puede conversar con respeto."),
    ],
    ("Lee la situación y escribe qué dirías tú. Situación: tu familia habla de qué comer en el almuerzo. Papá dice: «Hagamos pizza». Tú prefieres arroz con pollo. Escribe: 1) una frase para decir que piensas distinto (empieza con «Entiendo que…»), 2) una razón con «porque» y 3) una pregunta para saber la razón de papá. Luego dilo en voz alta a un adulto.",
     "1) Entiendo que quieres pizza, pero yo prefiero arroz con pollo. 2) Porque me gusta cómo lo prepara la abuela. 3) ¿Por qué quieres pizza hoy?",
     ["dice que piensa distinto con respeto", "da una razón", "hace una pregunta"], ["tres frases escritas y dichas"], ["burlarse de la idea", "no dar razón"],
     "Si usó una frase que ofende, pide que la cambie por «Yo pienso distinto porque…»."),
    "Practica en casa decir «yo pienso distinto porque…» sin enojarte.",
    "Escribe cómo resolverías un desacuerdo entre dos amigos que quieren juegos distintos.",
)

reg(
    OA21, 5,
    "Las pautas escritas en este cuaderno, lápiz y hoja. Se conversa con dos o tres personas de la casa, o con tres muñecos si nadie está disponible.",
    "Aprenderé a mantener una conversación breve sin que un adulto me guíe en cada paso. Sirve para conversar con confianza en la escuela y en casa.",
    ["Sé respetar turnos, dar razones, mostrar que escucho y disentir con respeto."],
    [
        "Una conversación autónoma es la que llevamos entre nosotros sin que alguien nos diga qué hacer en cada momento. Para lograrla recuerda cuatro cosas: esperar el turno, decir una idea con razón, mostrar que escuchaste y preguntar o disentir con respeto.",
        "Antes de conversar, mira la pauta: ¿hablé en mi turno? ¿di una razón con «porque»? ¿repetí o pregunté sobre lo que dijeron? ¿fui respetuoso con ideas distintas? Si puedes responder sí a las cuatro, tu conversación fue buena.",
        "Es normal olvidar alguna. Si te equivocas, puedes decir: «Perdón, me tocaba a ti». Después de conversar, revisa qué hiciste bien y qué quieres mejorar la próxima vez.",
    ],
    [("autónomo", "que lo hago por mí mismo"), ("pauta", "lista para revisar cómo lo hice"), ("turno", "momento en que hablo"), ("respeto", "buen trato a todos"), ("mejorar", "hacerlo mejor la próxima vez")],
    [
        ("Revisar con la pauta", "Ana habló en su turno, dio una razón, repitió lo que dijo Beto y no se burló de Carla. ¿Cuántos puntos de la pauta cumplió?", ["La pauta tiene cuatro puntos.", "Cumplió turno, razón, escucha y respeto.", "Son cuatro puntos."], "Cumplió los 4 puntos."),
        ("Reparar un error", "Beto interrumpió a Luz. ¿Qué puede decir?", ["Se da cuenta.", "Pide perdón.", "Deja hablar a Luz."], "Perdón, me tocaba a ti; sigue Luz."),
    ],
    [("Esperar que el adulto guíe cada paso.", "Falta confianza.", "Recuerda la pauta de cuatro puntos."), ("No revisar lo que hice.", "Se termina y se olvida.", "Usa la pauta al terminar.")],
    [
        E("¿Cuántos puntos tiene la pauta de conversación: turno, razón, escucha y respeto?", "4", "Son cuatro puntos."),
        E("Si interrumpo sin querer, ¿qué digo?", "Perdón, sigue tú", "Reparar un error muestra respeto."),
        E("¿Qué punto de la pauta es «esperar a que otro termine»?", "El turno", "Hablar por turnos es esperar."),
    ],
    [
        E("¿Qué significa conversar de manera autónoma?", "Conversar sin que alguien me diga cada paso", "Es llevar la conversación yo mismo."),
        E("¿Para qué sirve la pauta al final?", "Para ver qué hice bien y qué puedo mejorar", "Permite revisar la conversación."),
        E("¿Por qué conviene dar razones en una conversación?", "Porque ayudan a entender mi idea", "La razón explica la opinión."),
    ],
    [
        E("Diálogo: Ana: «Quiero leer el libro del oso porque tiene dibujos». Beto: «Tú dijiste que quieres el del oso. Yo prefiero el del tren porque es más corto». ¿Qué hizo Beto primero: repetir lo que dijo Ana o pensar distinto?", "Repetir lo que dijo Ana", "Primero repitió lo de Ana."),
        E("En ese mismo diálogo, ¿Beto dio una razón para su preferencia?", "Sí, que es más corto", "Dijo «porque es más corto»."),
        E("Ana ahora quiere seguir la conversación. Escribe una pregunta para Beto.", "Por ejemplo: ¿Qué hay en el libro del tren?", "Eso muestra interés."),
    ],
    [
        E("Dos niños hablan a la vez durante toda la charla y nadie escucha. ¿Qué punto de la pauta no cumplen?", "El turno", "No esperan que el otro termine."),
        E("Luz hizo bien tres puntos de la pauta. ¿Cumplió todos?", "No, le falta uno", "Hay cuatro puntos y cumplió tres."),
    ],
    [
        E("Tema: «¿Qué haremos en el recreo?». Ana: «Saltar la cuerda porque es divertido». Beto: «Yo prefiero la pelota porque corro». Escribe una frase para que Carla muestre que escuchó a ambos y proponga algo.", "Por ejemplo: Ana quiere cuerda y Beto pelota; podemos jugar primero uno y después el otro", "Muestra escucha y propone."),
        E("Eva quiere mejorar su conversación. Marca una cosa que puede practicar: a) hablar más fuerte que todos, b) esperar el turno.", "b", "Esperar el turno mejora la conversación."),
    ],
    [E("En tu casa, la familia conversa sobre dónde pasear el domingo: playa, parque o cerro. Todos dan su opinión. Escribe tu aporte con una razón y una frase que conecte con alguien.", "Por ejemplo: Prefiero el parque porque hay columpios; mamá, tú dijiste que el cerro cansa, ¿por eso prefieres parque?", "Incluye razón y conexión.")],
    [
        E("¿Cuál es el primer punto de la pauta: esperar el turno?", "Sí", "Primero se escucha y se espera."),
        E("¿Pedir perdón si interrumpo es un buen gesto?", "Sí", "Eso muestra respeto."),
        E("¿Qué hago al terminar una conversación?", "Reviso con la pauta", "Veo qué hice bien."),
    ],
    ("Conversa 3 minutos con dos personas de tu casa sobre este tema: «¿Qué haremos el fin de semana?». Antes de empezar lee la pauta: 1) espero mi turno, 2) digo mi idea con «porque», 3) muestro que escuché, 4) soy respetuoso. Al terminar, marca qué puntos cumpliste y escribe uno que quieras mejorar.",
     "Conversé con mamá y mi hermano. Esperé mi turno. Dije: quiero ir a la plaza porque hay columpios. Dije: tú dijiste que prefieres el cine. Fui respetuoso. Quiero mejorar: no interrumpir a mi hermano.",
     ["cumple los cuatro puntos o dice cuáles no", "marca un punto a mejorar"], ["pauta marcada", "adulto confirma lo observado"], ["no revisar la pauta", "no decir qué mejorar"],
     "Si marcó todo sin pensar, pide un ejemplo concreto de una frase suya que muestre el punto."),
    "Hoy conversa en la cena con la pauta de cuatro puntos en mente.",
    "Conversa con un compañero distinto al de siempre y cuéntale algo nuevo de ti.",
)

# ================================================================ OA 22
reg(
    OA22, 1,
    "Las frases modelo de este cuaderno, lápiz y hoja. Para practicar se necesita un adulto o un muñeco.",
    "Aprenderé a presentarme y a presentar a otra persona de forma amable. Sirve para conocer gente nueva y hacer amigos.",
    ["Sé decir mi nombre.", "Sé saludar."],
    [
        "Presentarse es decir quién soy. Se dice el nombre y, si se quiere, algo que a uno le gusta. Por ejemplo: «Hola, me llamo Ana y me gusta dibujar». Se dice con voz clara y mirando a la persona. No hace falta decir datos privados como la dirección o el teléfono.",
        "Presentar a otra persona es decirle a alguien quién es esa persona. Por ejemplo: «Te presento a mi amigo Beto». Se nombra primero a la persona mayor y luego a la otra. Después ambas pueden saludarse: «Mucho gusto» o «Encantado».",
        "Cuando alguien se presenta contigo, responde con tu nombre y una frase amable, como «Mucho gusto» o «Qué bueno conocerte». Así la conversación empieza bien. Si no oíste el nombre, puedes decir «¿Me lo repites, por favor?».",
    ],
    [("presentarse", "decir quién soy"), ("presentar", "decir quién es otra persona"), ("mucho gusto", "frase para saludar a alguien que conozco hoy"), ("nombre", "cómo me llaman"), ("datos privados", "información que no se comparte con extraños")],
    [
        ("Presentarme", "Ana quiere presentarse en un curso nuevo. ¿Qué dice?", ["Saluda.", "Dice su nombre.", "Agrega algo que le gusta."], "Hola, me llamo Ana y me gusta dibujar."),
        ("Presentar a un amigo", "Beto llega con Luz y quiere presentarla a su abuela. ¿Qué dice?", ["Primero nombra a la abuela.", "Después nombra a Luz.", "Usa «Te presento a…»."], "Abuela, te presento a mi amiga Luz."),
    ],
    [("Hablar bajito y sin mirar.", "Da vergüenza.", "Di tu nombre con voz clara y mirando."), ("Dar datos privados como la dirección.", "No se sabe qué cuidar.", "Di solo tu nombre y un gusto.")],
    [
        E("¿Cuál es una buena presentación: «Me llamo Ana» o «Ana vive en la calle…»?", "Me llamo Ana", "No hay que dar la dirección."),
        E("Para presentar a mi amigo Beto, digo: «Te ___ a mi amigo Beto». ¿Qué palabra falta: presento o llevo?", "presento", "Presentar a alguien es decir quién es."),
        E("Cuando alguien me presenta, ¿qué puedo decir: «Mucho gusto» o «No me importa»?", "Mucho gusto", "Es una frase amable."),
    ],
    [
        E("¿Qué se dice al presentarse?", "El nombre y algo que me gusta", "Con eso otros me conocen."),
        E("¿Por qué no hay que dar datos privados a extraños?", "Para cuidarse y estar seguro", "La dirección o el teléfono son privados."),
        E("¿Cómo puedo pedir que me repitan un nombre?", "¿Me lo repites, por favor?", "Se pide con cortesía."),
    ],
    [
        E("Escribe una frase para presentarte a un niño nuevo. Usa el nombre «Mateo» como ejemplo.", "Hola, me llamo Mateo y me gusta jugar a la pelota", "Incluye saludo, nombre y un gusto."),
        E("Escribe cómo presentarías a tu amiga Rosa a tu profesora.", "Profesora, le presento a mi amiga Rosa", "Primero se nombra a la persona mayor."),
        E("Escribe cómo responder cuando alguien te dice «Hola, me llamo Eva».", "Hola Eva, mucho gusto, me llamo…", "Se responde con nombre y cortesía."),
    ],
    [
        E("Sol se presenta así: «Me llamo Sol y vivo en la calle Los Olmos 123». ¿Qué dato no conviene decir?", "La dirección", "Es un dato privado."),
        E("Teo presenta a su papá y a su amigo Iván. Dice: «Papá, te presento a mi amigo Iván». ¿Está bien?", "Sí", "Nombra primero a su papá, que es la persona mayor."),
    ],
    [
        E("Ordena para presentarte: a) Mucho gusto, b) Hola, c) Me llamo Ana. Escribe las letras en orden.", "b, c, a", "Primero saludo, luego nombre, después cortesía."),
        E("Un niño nuevo llega al curso, nadie sabe su nombre. ¿Qué puede decir la profesora?", "Les presento a nuestro nuevo compañero", "Introduce al niño al grupo."),
    ],
    [E("En el primer día de clases, un niño se acerca a ti en el recreo. Escribe cómo te presentarías y qué le preguntarías.", "Por ejemplo: Hola, me llamo Luis y me gusta pintar. ¿Cómo te llamas tú?", "Incluye nombre, gusto y pregunta.")],
    [
        E("¿Digo mi nombre con voz clara?", "Sí", "Así me entienden."),
        E("Al presentar a una abuela y a una amiga, ¿a quién nombro primero?", "A la abuela", "Se nombra primero a la persona mayor."),
        E("¿Qué palabra amable digo cuando me presentan a alguien?", "Mucho gusto", "Es una fórmula de cortesía."),
    ],
    ("Prepara una presentación de tres frases: 1) saludo, 2) tu nombre y 3) algo que te gusta (por ejemplo: dibujar, jugar a la pelota, cantar, leer). Luego presenta a un muñeco o a un adulto con la frase «Te presento a…». Ensaya frente a un adulto con voz clara.",
     "Hola. Me llamo Ana. Me gusta dibujar. Te presento a mi muñeco Pancho.",
     ["saluda", "dice su nombre", "dice un gusto", "presenta a otra persona"], ["adulto observa la presentación"], ["decir datos privados", "voz muy baja"],
     "Si habló bajito, repite con la voz un poco más fuerte: clara pero amable."),
    "Presenta a un familiar a otro familiar con la frase «Te presento a…».",
    "Escribe cómo presentarías a dos amigos que no se conocen.",
)

reg(
    OA22, 2,
    "Las situaciones escritas en este cuaderno, lápiz y hoja. No se necesitan materiales especiales.",
    "Aprenderé a saludar y despedirme de forma distinta según la hora y la persona. Sirve para ser amable en la escuela y en la calle.",
    ["Sé decir hola y chao.", "Sé que hay mañana, tarde y noche."],
    [
        "Saludar es decir algo amable cuando nos encontramos con alguien. No siempre se saluda igual. A un amigo puedes decirle «hola». A un adulto, como una profesora o un vecino, es mejor decir «buenos días», «buenas tardes» o «buenas noches», según la hora.",
        "Se dice «buenos días» en la mañana, «buenas tardes» después del almuerzo y «buenas noches» cuando ya oscureció. Al despedirse se dice «adiós», «hasta luego» o «chao». A un adulto puedes decirle «hasta luego» o «que le vaya bien».",
        "Al saludar es bueno mirar a la persona, sonreír y hablar con voz suave. También se puede agregar el nombre, por ejemplo: «Buenos días, señora Rosa». Un saludo amable hace sentir bien al otro.",
    ],
    [("saludar", "decir algo amable al encontrarse"), ("despedirse", "decir algo amable al irse"), ("buenos días", "saludo de la mañana"), ("buenas tardes", "saludo de después del almuerzo"), ("buenas noches", "saludo o despedida cuando es de noche")],
    [
        ("Elegir el saludo", "Son las 9 de la mañana y encuentras a tu profesora. ¿Cómo la saludas?", ["Es de mañana.", "Es una persona adulta.", "Uso «buenos días»."], "Buenos días, profesora."),
        ("Despedirse de un amigo", "Se acaba el recreo y te despides de tu compañero Beto. ¿Qué le dices?", ["Es un amigo.", "Puedo usar una forma cercana.", "Digo «chao»."], "Chao, Beto, nos vemos."),
    ],
    [("Decir «buenos días» en la noche.", "No se piensa en la hora.", "Mira la hora o el cielo."), ("Saludar a un adulto como a un amigo.", "Se usa siempre «hola».", "Usa «buenos días» o «buenas tardes».")],
    [
        E("A las 8 de la mañana, ¿digo «buenos días» o «buenas noches»?", "Buenos días", "Es de mañana."),
        E("Después del almuerzo, ¿qué saludo uso: «buenas tardes» o «buenos días»?", "Buenas tardes", "Ya pasó el mediodía."),
        E("A un amigo en el recreo puedo decirle «hola». ¿Verdadero o falso?", "Verdadero", "Con amigos es normal."),
    ],
    [
        E("¿Qué saludo uso cuando es de noche?", "Buenas noches", "Se dice de noche."),
        E("¿Por qué saludamos distinto a un amigo y a una profesora?", "Porque con adultos usamos un trato más respetuoso", "El saludo cambia según la persona."),
        E("¿Qué hago con mi cara al saludar?", "Miro y sonrío", "Hace más amable el saludo."),
    ],
    [
        E("Es la 1 de la tarde (ya almorzaste) y ves a la señora Rosa, vecina. Escribe cómo la saludas.", "Buenas tardes, señora Rosa", "Después del almuerzo se dice buenas tardes."),
        E("Sales de la escuela a las 4 de la tarde. Escribe cómo te despides de la profesora.", "Hasta mañana, profesora", "Es una despedida amable."),
        E("Escribe cómo saludarías a tu abuelo cuando lo ves al amanecer.", "Buenos días, abuelo", "Es de mañana."),
    ],
    [
        E("Teo saluda a la directora diciendo «¡Ey, hola!». ¿Es lo más adecuado?", "No, es mejor «buenos días»", "A una autoridad se le saluda con respeto."),
        E("Luis dice «Buenas noches» a su profesora a las 10 de la mañana. ¿Se equivocó?", "Sí", "A esa hora corresponde «buenos días»."),
    ],
    [
        E("Una familia sale de una tienda a las 9 de la noche. ¿Qué dicen al despedirse: «buenas noches» o «buenos días»?", "Buenas noches", "Ya es de noche."),
        E("¿Cuántos saludos distintos hay en este texto: buenos días, buenas tardes, buenas noches?", "3", "Se cuentan tres."),
    ],
    [E("En el patio, un compañero nuevo te dice «hola». Detrás viene su mamá. ¿Cómo saludas a cada uno?", "Al niño: hola; a su mamá: buenas tardes, señora", "Al niño con cercanía y a la adulta con respeto.")],
    [
        E("Si me despido de un adulto, ¿digo «hasta luego» o «¡chao, flojo!»?", "Hasta luego", "Es una despedida respetuosa."),
        E("¿Cuándo digo «buenos días»?", "En la mañana", "Es el saludo de la mañana."),
        E("¿Saludar con una sonrisa es amable?", "Sí", "Hace sentir bien al otro."),
    ],
    ("Mira estas cuatro situaciones y escribe cómo saludarías o te despedirías en cada una. A) 8:00 de la mañana, llegas a la escuela y ves a la profesora. B) 3:00 de la tarde, llegas a la casa de tu abuela. C) 8:00 de la noche, te vas a dormir y te despides de tu papá. D) Recreo, ves a tu mejor amigo Beto.",
     "A) Buenos días, profesora. B) Buenas tardes, abuela. C) Buenas noches, papá. D) Hola, Beto.",
     ["elige el saludo según la hora", "usa trato respetuoso con adultos", "usa trato cercano con amigos"], ["cuatro saludos escritos o dichos"], ["buenos días en la noche", "decir «hola» a todos igual"],
     "Pide que mire la hora de cada situación y luego cambie el saludo si hace falta."),
    "Saluda a tres personas distintas hoy con el saludo que corresponde.",
    "Escribe una despedida distinta para un amigo, un vecino y un profesor.",
)

reg(
    OA22, 3,
    "Las situaciones y frases modelo de este cuaderno, lápiz y hoja. No se necesitan otros materiales.",
    "Aprenderé a preguntar y a pedir permiso con cortesía. Sirve para pedir cosas sin molestar y para que me digan que sí.",
    ["Sé decir «por favor» y «gracias».", "Sé hacer preguntas."],
    [
        "Cuando necesito algo, puedo pedirlo con cortesía. Pedir permiso es preguntar si puedo hacer algo. Se usa «¿puedo…?» o «¿me permites…?» y la palabra mágica «por favor». Por ejemplo: «¿Puedo ir al baño, por favor?».",
        "Si quiero algo que es de otra persona, no lo tomo: lo pido. Digo «¿Me prestas tu lápiz, por favor?». Si la persona dice que sí, digo «gracias». Si dice que no, respondo «está bien» y no me enojo. Una respuesta de no también se respeta.",
        "Para preguntar algo que no sé, puedo empezar con «disculpa» o «perdón». Por ejemplo: «Disculpa, ¿dónde está la biblioteca?». Esa palabra capta la atención con amabilidad. Hablar con un tono suave y mirar a la persona ayuda a que me respondan bien.",
    ],
    [("permiso", "autorización para hacer algo"), ("por favor", "palabra que hace amable una petición"), ("disculpa", "palabra para llamar la atención con cortesía"), ("prestar", "dejar algo por un rato"), ("petición", "cuando pido algo")],
    [
        ("Pedir permiso", "Necesitas ir al baño durante la clase. ¿Qué dices?", ["Levanto la mano.", "Uso «¿puedo…?».", "Agrego «por favor»."], "Profesora, ¿puedo ir al baño, por favor?"),
        ("Pedir algo prestado", "Quieres usar el lápiz azul de Beto. ¿Qué dices?", ["No lo tomo sin avisar.", "Pregunto.", "Uso «por favor»."], "Beto, ¿me prestas tu lápiz azul, por favor?"),
    ],
    [("Tomar las cosas sin pedir.", "Se cree que es rápido o gracioso.", "Pregunta antes con «¿me prestas…?»."), ("Enojarse si dicen que no.", "Cuesta aceptar un no.", "Di «está bien» y busca otra opción.")],
    [
        E("Para ir al baño en clase, ¿pido permiso o salgo sin avisar?", "Pido permiso", "Debo avisar y preguntar."),
        E("¿Qué palabra hace amable una petición?", "Por favor", "Muestra buena educación."),
        E("¿Qué digo si me prestan un lápiz?", "Gracias", "Agradezco el favor."),
    ],
    [
        E("¿Qué es pedir permiso?", "Preguntar si puedo hacer algo", "Se espera una respuesta."),
        E("¿Por qué no debo tomar el lápiz de otro sin preguntar?", "Porque es de otra persona", "Debo respetar lo que no es mío."),
        E("Si alguien me dice que no a un préstamo, ¿qué respondo?", "Está bien", "Respeto su decisión."),
    ],
    [
        E("Quieres salir al patio durante la clase. Escribe cómo pides permiso a la profesora.", "Por ejemplo: Profesora, ¿puedo salir al patio, por favor?", "Usa ¿puedo? y por favor."),
        E("Quieres jugar con la pelota de Luz. Escribe cómo la pides.", "Por ejemplo: Luz, ¿me prestas la pelota, por favor?", "Pide prestado con cortesía."),
        E("No sabes dónde está el baño. Escribe cómo preguntas a un adulto.", "Por ejemplo: Disculpa, ¿dónde está el baño?", "Usa disculpa y una pregunta clara."),
    ],
    [
        E("Teo dice a un compañero: «Dame tu goma». ¿Está pidiendo con cortesía?", "No", "No usa pregunta ni por favor."),
        E("Eva dice: «¿Me prestas tu cuaderno, por favor?». Carla responde: «No, lo estoy usando». ¿Qué responde bien Eva?", "Está bien, gracias", "Respeta el no."),
    ],
    [
        E("Ordena para pedir bien: a) por favor, b) ¿me prestas tu lápiz, c) gracias. Escribe las letras en el orden: pedir con cortesía.", "b, a, c", "Pido, digo por favor y agradezco."),
        E("Ana llega tarde a clase y la profesora está explicando. Escribe cómo pide permiso para entrar.", "Por ejemplo: Disculpe, profesora, ¿puedo pasar?", "Pide permiso sin interrumpir."),
    ],
    [E("En una tienda del barrio quieres ver un cuaderno que está en un estante alto. Escribe cómo se lo pides al vendedor.", "Por ejemplo: Disculpe, ¿me puede mostrar ese cuaderno, por favor?", "Es una petición cortés.")],
    [
        E("¿Qué palabra uso para llamar la atención con cortesía: «disculpa» o «oye»?", "Disculpa", "Es más amable."),
        E("¿Pido permiso para tomar cosas de otra persona?", "Sí", "Así respeto lo ajeno."),
        E("¿Cómo termino cuando me prestan algo?", "Digo gracias", "Agradezco el favor."),
    ],
    ("Escribe y di en voz alta cuatro peticiones con cortesía: 1) pedir permiso para ir al baño, 2) pedir prestada una goma, 3) preguntar la hora a tu profesora o a un adulto de tu familia, 4) pedir que te ayuden a abrir un frasco. Cada una debe llevar «por favor» o «disculpa».",
     "1) Profesora, ¿puedo ir al baño, por favor? 2) Beto, ¿me prestas tu goma, por favor? 3) Disculpa, ¿qué hora es? 4) ¿Me ayudas a abrir el frasco, por favor?",
     ["cuatro peticiones", "usa por favor o disculpa", "usa tono amable"], ["cuatro frases escritas y dichas"], ["dar órdenes", "no agradecer"],
     "Si dio una orden, pide que la cambie a pregunta con «¿puedes…?» o «¿me prestas…?»."),
    "Pide hoy un favor con «por favor» y agradece después.",
    "Escribe una petición cortés y una respuesta cortés para cuando te digan que no.",
)

reg(
    OA22, 4,
    "Las situaciones escritas en este cuaderno, lápiz y hoja. No se necesitan otros materiales.",
    "Aprenderé a decir lo que pienso y lo que siento con respeto. Sirve para que los demás me entiendan sin enojarse ni herirse.",
    ["Sé nombrar emociones como alegre, triste y enojado.", "Sé que puedo decir lo que siento."],
    [
        "Todos sentimos emociones: alegría, tristeza, enojo, miedo. Es bueno decirlas con palabras. Una forma respetuosa es usar «Me siento… porque…». Por ejemplo: «Me siento triste porque no me invitaron a jugar». Así explico lo que me pasa sin culpar ni gritar.",
        "Hay frases que ayudan a decir lo que quiero: «Me gustaría que…», «Necesito que…», «Prefiero que…». Por ejemplo: «Me gustaría que me esperaran para jugar». Se dicen con voz tranquila. Evita palabras que hieren, como «eres malo» o «no te quiero».",
        "También puedo contar una idea con cortesía: «Creo que…» o «Me parece que…». Así los demás saben qué pienso y pueden responder. Y cuando otro dice cómo se siente, escucho con atención y trato bien lo que dice.",
    ],
    [("emoción", "lo que siento, como alegría o tristeza"), ("expresar", "decir con palabras lo que pienso o siento"), ("me siento", "frase para decir cómo estoy"), ("herir", "hacer daño con lo que digo"), ("tranquilo", "sin gritar ni enojarme")],
    [
        ("Decir una emoción", "Nadie te invitó a jugar y te sientes triste. ¿Qué dices?", ["Pienso cómo me siento.", "Uso «Me siento…».", "Agrego «porque…»."], "Me siento triste porque no me invitaron a jugar."),
        ("Pedir lo que quiero", "Un compañero te quita el lápiz. Estás molesto. ¿Qué dices con respeto?", ["Digo cómo me siento.", "Digo lo que quiero.", "Uso voz tranquila."], "Me siento molesto porque me quitaste el lápiz; me gustaría que me lo devolvieras."),
    ],
    [("Gritar o insultar cuando uno está enojado.", "Se piensa que así me escuchan.", "Di «me siento… porque…» con voz tranquila."), ("Guardarse todo lo que se siente.", "Da vergüenza decirlo.", "Cuéntalo a un adulto o amigo.")],
    [
        E("¿Cuál frase dice cómo me siento: «Me siento contento» o «Eres malo»?", "Me siento contento", "Habla de mi emoción, no ofende."),
        E("«Me siento ___ porque perdí mi juguete». ¿Qué palabra es probable: triste o dormido?", "triste", "Perder algo causa tristeza."),
        E("¿Puedo contar lo que siento con voz tranquila?", "Sí", "Se entiende mejor."),
    ],
    [
        E("¿Para qué sirve decir «me siento… porque…»?", "Para explicar lo que me pasa sin ofender", "Muestra mi emoción y su causa."),
        E("¿Por qué conviene evitar «eres malo»?", "Porque hiere a la otra persona", "Es una palabra que daña."),
        E("¿Qué significa «expresar» una idea?", "Decirla con palabras", "Es comunicar lo que pienso."),
    ],
    [
        E("Escribe cómo dirías que estás contento porque tu amigo te ayudó.", "Me siento contento porque mi amigo me ayudó", "Dice emoción y causa."),
        E("Un niño no te dejó jugar y te molestó. Escribe una frase con «Me gustaría que…».", "Me gustaría que me dejaran jugar", "Dice lo que quiero con respeto."),
        E("Escribe una idea con «Creo que…» sobre cuál es el mejor juego del patio.", "Por ejemplo: Creo que la escondida es el mejor juego del patio", "Usa «Creo que…» para opinar."),
    ],
    [
        E("Teo grita «¡Eres un tonto!» porque Eva rompió su dibujo. ¿Qué podría decir sin ofender?", "Me siento triste porque rompiste mi dibujo", "Habla de su emoción."),
        E("Luz dice: «Me siento sola porque nadie juega conmigo». ¿Qué emoción nombra?", "Soledad", "Siente que está sola."),
    ],
    [
        E("Ordena para decir bien tu emoción: a) porque no me esperaron, b) me siento triste. Escribe las letras en orden.", "b, a", "Primero la emoción y luego la causa."),
        E("Mía dice: «Me siento feliz cuando mi mamá me lee un cuento». ¿Cuál es la causa de su alegría?", "Que su mamá le lee un cuento", "La causa va después de «cuando»."),
    ],
    [E("Tu compañero se burló de tu dibujo. Dices una frase para decirle cómo te sientes y qué quieres, con voz tranquila.", "Por ejemplo: Me siento triste porque te reíste de mi dibujo; me gustaría que me lo dijeras con respeto", "Incluye emoción, causa y petición.")],
    [
        E("¿Qué empiezo a decir para contar una emoción: «Me siento…» o «Tú eres…»?", "Me siento…", "Habla de mí, no acusa."),
        E("¿Un grito ayuda a que me escuchen mejor?", "No", "Gritar asusta o enoja."),
        E("¿Es bueno contar lo que siento a un adulto de confianza?", "Sí", "Un adulto me puede ayudar."),
    ],
    ("Lee cuatro situaciones y escribe qué dirías, con «Me siento… porque…». A) Tu amigo te regaló un dibujo. B) Alguien rompió tu torre de bloques. C) No te dejaron jugar a la pelota. D) Ganaste un premio en el curso. En una de ellas agrega «Me gustaría que…».",
     "A) Me siento contento porque mi amigo me regaló un dibujo. B) Me siento molesto porque rompieron mi torre; me gustaría que me pidieran permiso. C) Me siento triste porque no me dejaron jugar. D) Me siento orgulloso porque gané un premio.",
     ["dice la emoción", "dice la causa", "usa voz tranquila"], ["cuatro frases escritas y dichas en voz alta"], ["decir solo «me enojé» sin causa", "insultar"],
     "Si falta la causa, pregunta: ¿qué pasó para que te sintieras así?"),
    "Cuenta a un adulto cómo te sentiste hoy con «Me siento… porque…».",
    "Escribe cómo reaccionarías si un amigo te dice «Me siento triste porque no jugaste conmigo».",
)

reg(
    OA22, 5,
    "Las situaciones escritas en este cuaderno, lápiz y hoja. No se necesitan otros materiales.",
    "Aprenderé a dar las gracias, a reparar un error y a pedir perdón con sinceridad. Sirve para cuidar a mis amigos y a mi familia.",
    ["Sé decir gracias.", "Sé que a veces cometo errores."],
    [
        "Dar las gracias es reconocer que alguien nos ayudó o nos dio algo. Se dice «gracias» y, si quieres, por qué: «Gracias por prestarme tu lápiz». El agradecimiento hace sentir bien a quien ayudó. Se dice mirando a la persona.",
        "A veces cometemos errores y molestamos a alguien sin querer. Entonces se pide perdón. Un buen perdón tiene tres partes: digo qué hice («Rompí tu torre»), digo que lo siento («Lo siento mucho») y ofrezco reparar («¿Te ayudo a armarla otra vez?»). Pedir perdón no es perder: es cuidar a la otra persona.",
        "Cuando alguien te pide perdón, puedes responder «Está bien» o «Te perdono» si de verdad lo sientes. También puedes decir «Gracias por decírmelo». Si todavía estás molesto, puedes decir: «Necesito un momento». Todos tenemos derecho a sentir y a esperar.",
    ],
    [("agradecer", "decir gracias por algo recibido"), ("perdón", "palabra para reparar un error"), ("reparar", "arreglar lo que dañé"), ("sincero", "que dice la verdad de lo que siente"), ("perdonar", "aceptar el perdón de alguien")],
    [
        ("Agradecer", "Luz te ayudó a recoger tus lápices. ¿Qué le dices?", ["Pienso en lo que hizo.", "Digo gracias.", "Agrego por qué."], "Gracias, Luz, por ayudarme a recoger mis lápices."),
        ("Pedir perdón", "Sin querer, pisaste el dibujo de Beto. ¿Cómo pides perdón?", ["Digo qué pasó.", "Digo que lo siento.", "Ofrezco ayudar."], "Pisé tu dibujo, lo siento mucho; ¿te ayudo a pintar uno nuevo?"),
    ],
    [("Decir «perdón» pero seguir molestando.", "Se dice para que lo dejen en paz.", "Cambia lo que hiciste y repara."), ("Obligar a perdonar enseguida.", "Se quiere cerrar rápido.", "Respeta que el otro necesite tiempo.")],
    [
        E("Alguien me presta su lápiz. ¿Qué digo: «Gracias» o «Dame más»?", "Gracias", "Agradezco el favor."),
        E("Si sin querer rompo la torre de bloques de un amigo, ¿qué digo primero?", "Lo siento", "Reconozco el error."),
        E("Pedir perdón, ¿es perder?", "No", "Es cuidar a la otra persona."),
    ],
    [
        E("¿Cuáles son las tres partes de un buen perdón?", "Decir qué hice, decir que lo siento y ofrecer reparar", "Así el perdón es completo."),
        E("¿Por qué conviene agregar «por qué» al agradecer?", "Para que la persona sepa lo que valoré", "Hace el gracias más claro."),
        E("¿Qué hago si todavía estoy molesto cuando me piden perdón?", "Digo que necesito un momento", "Puedo esperar a sentirme mejor."),
    ],
    [
        E("Escribe un agradecimiento para tu abuela, que te preparó una sopa.", "Gracias, abuela, por prepararme la sopa", "Nombra el favor."),
        E("Rompiste sin querer el lápiz de Teo. Escribe un perdón con las tres partes.", "Rompí tu lápiz, lo siento mucho; ¿te regalo uno mío?", "Incluye qué hice, lo siento y reparar."),
        E("Un amigo te pidió perdón y lo sientes sincero. Escribe qué le respondes.", "Por ejemplo: Está bien, gracias por decírmelo", "Acepta con cortesía."),
    ],
    [
        E("Beto dice «Perdón» y se ríe. ¿Es un perdón sincero?", "No", "Falta sentirlo de verdad."),
        E("Eva dice: «Perdón, lo hice sin querer; te ayudo a limpiar». ¿Qué parte de reparar incluyó?", "Ofrecer ayuda", "Dijo que ayudará a limpiar."),
    ],
    [
        E("Una niña dice «gracias» sin mirar, mientras mira su celular. ¿Qué podría mejorar?", "Mirar a la persona al agradecer", "Mirar muestra sinceridad."),
        E("Ordena: a) Lo siento, b) Rompí tu torre, c) ¿Te ayudo a armarla? Escribe las letras en el orden recomendado.", "b, a, c", "Qué hice, lo siento, reparar."),
    ],
    [E("Estás jugando y sin querer golpeas a tu compañero con la pelota. ¿Qué dices y haces?", "Por ejemplo: Te di con la pelota, lo siento; ¿estás bien? ¿te ayudo?", "Reconoce, pide perdón y ayuda.")],
    [
        E("¿Qué palabra digo cuando recibo ayuda?", "Gracias", "Reconozco lo que hicieron por mí."),
        E("¿Pedir perdón arregla todo sin hacer nada más?", "No, también hay que reparar", "El perdón incluye arreglar el daño."),
        E("Si me piden perdón, ¿estoy obligado a decir «te perdono» enseguida?", "No", "Puedo tomarme un momento."),
    ],
    ("Escribe y di en voz alta: 1) un agradecimiento a alguien de tu casa por una ayuda concreta; 2) un perdón con las tres partes para esta situación: sin querer ensuciaste el cuaderno de tu hermana con pintura; 3) una respuesta amable si tu hermana te perdona.",
     "1) Gracias, mamá, por leerme el cuento. 2) Ensucié tu cuaderno con pintura, lo siento mucho; ¿te ayudo a limpiarlo? 3) Gracias por ayudarme a limpiarlo.",
     ["agradece con motivo", "pide perdón con tres partes", "responde con cortesía"], ["tres frases escritas y dichas"], ["perdón sin reparar", "gracias sin decir por qué"],
     "Si falta una parte, pide que la agregue y vuelva a decir el perdón completo."),
    "Agradece hoy a tres personas diciendo por qué.",
    "Escribe un perdón para un hermano y para un amigo.",
)

reg(
    OA22, 6,
    "Las situaciones escritas en este cuaderno, lápiz y hoja. No se necesitan otros materiales.",
    "Aprenderé a elegir la respuesta social más adecuada en situaciones distintas. Sirve para convivir bien en la escuela, en casa y en la calle.",
    ["Sé saludar, pedir permiso, agradecer y pedir perdón."],
    [
        "En cada situación hay una respuesta social que ayuda a convivir. Antes de hablar, piensa tres cosas: ¿con quién hablo?, ¿dónde estoy? y ¿qué necesito? Con esas respuestas eliges las palabras: saludar, pedir permiso, agradecer, pedir perdón o decir cómo me siento.",
        "Por ejemplo, si llegas a la escuela, saludas. Si quieres salir de la sala, pides permiso. Si alguien te ayudó, agradeces. Si molestaste sin querer, pides perdón. Si un compañero está triste, dices algo amable. Cada situación pide una palabra distinta.",
        "Para elegir bien, usa la regla: lo que dices debe ser amable, claro y respetuoso. Si dudas, imagina cómo te gustaría que te hablaran a ti. Con práctica, elegirás cada vez mejor.",
    ],
    [("situación", "momento en que estoy con otros"), ("convivir", "llevarse bien con los demás"), ("respuesta social", "lo que digo o hago con los demás"), ("adecuado", "que sirve para la situación"), ("regla", "guía para actuar")],
    [
        ("Elegir la respuesta", "Llegas a la escuela y ves a tu profesora. ¿Saludas o pides permiso?", ["Llego a un lugar.", "Veo a una persona mayor.", "Corresponde saludar ahí."], "Saludo: «Buenos días, profesora»."),
        ("Elegir otra respuesta", "Derramaste agua en la mesa de Luz sin querer. ¿Qué dices?", ["Cometí un error.", "Molesté a Luz.", "Corresponde pedir perdón."], "Lo siento, derramé agua; te ayudo a secar."),
    ],
    [("Usar siempre la misma frase.", "Se cree que sirve para todo.", "Piensa quién, dónde y qué necesito."), ("Hablar sin pensar.", "Se actúa rápido.", "Respira y piensa antes de hablar.")],
    [
        E("Llego a clases y veo a mi profesora. ¿Qué digo?", "Buenos días, profesora", "Corresponde saludar ahí."),
        E("Mi amigo me prestó su cuaderno. ¿Qué digo?", "Gracias", "Agradezco el préstamo."),
        E("Quiero salir de la sala. ¿Qué hago?", "Pido permiso", "Debo avisar y preguntar."),
    ],
    [
        E("¿Qué tres preguntas me hago antes de hablar?", "Con quién hablo, dónde estoy y qué necesito", "Me ayudan a elegir las palabras."),
        E("¿Por qué no sirve usar siempre la misma frase?", "Porque cada situación necesita una respuesta distinta", "No es lo mismo saludar que pedir perdón."),
        E("¿Lo que digo debe ser amable, claro y respetuoso?", "Sí", "Esa es la regla."),
    ],
    [
        E("Un niño nuevo está solo en el recreo. Escribe una frase amable para invitarlo a jugar.", "Por ejemplo: Hola, ¿quieres jugar con nosotros?", "Incluye a la otra persona."),
        E("Tu compañero se cayó. Escribe qué le dices.", "Por ejemplo: ¿Estás bien? ¿Te ayudo?", "Eso muestra cuidado."),
        E("Quieres un vaso de agua en casa de tu tía. Escribe cómo lo pides.", "Por ejemplo: Tía, ¿me das un vaso de agua, por favor?", "Pide con cortesía."),
    ],
    [
        E("Luis llega tarde y entra gritando: «¡Hola a todos!». ¿Qué debería hacer en vez?", "Entrar en silencio, saludar y pedir permiso", "Respeta la clase."),
        E("Mía recibe un regalo y no dice nada. ¿Qué le falta?", "Agradecer", "Debe decir gracias."),
    ],
    [
        E("Elige la respuesta más adecuada si tu amigo está triste porque se le perdió su juguete: a) «¡Qué bobo!», b) «Siento que lo hayas perdido; ¿te ayudo a buscarlo?».", "b", "La b es amable y ayuda."),
        E("En el comedor, el niño de al lado tiene tu cuchara. Escribe cómo se la pides.", "Por ejemplo: Disculpa, ¿me pasas la cuchara, por favor?", "Pide con cortesía."),
    ],
    [E("Un vecino mayor sostiene la puerta para que entres. Escribe qué le dices.", "Gracias, buenas tardes", "Agradece y saluda.")],
    [
        E("Si pisé sin querer a un compañero, ¿qué digo?", "Lo siento", "Así pido perdón."),
        E("Si encuentro a mi abuela por la mañana, ¿qué digo?", "Buenos días, abuela", "Saludo con respeto."),
        E("¿Puedo gritar para que me escuchen mejor?", "No", "Debo hablar con respeto."),
    ],
    ("Lee cuatro situaciones y escribe la respuesta social adecuada, diciendo en voz alta tu frase. A) A las 4 de la tarde llegas a la casa de un compañero y su mamá abre la puerta. B) Quieres tomar prestada la pelota de Eva. C) Un compañero te ayudó a abrir tu mochila. D) Sin querer, golpeaste a Teo con tu codo.",
     "A) Buenas tardes, señora. B) Eva, ¿me prestas la pelota, por favor? C) Gracias por ayudarme. D) Lo siento, te golpeé sin querer; ¿estás bien?",
     ["elige una respuesta para cada situación", "usa palabras amables y claras", "adapta la frase a la persona"], ["cuatro frases"], ["usar la misma frase en todas", "no usar cortesía"],
     "Si repitió la misma frase, vuelve a la tabla de quién, dónde y qué necesito."),
    "Usa hoy cuatro fórmulas de cortesía: hola, por favor, gracias y perdón.",
    "Escribe un pequeño diálogo con saludo, petición, agradecimiento y despedida.",
)
