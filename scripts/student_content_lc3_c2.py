"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR05 (creaciones digitales para la revitalización lingüística) y OA LS01 (textos orales breves y palabras
culturalmente significativas, contexto de sensibilización).

Criterio de autoría: todos los relatos, fichas, listas y personas son inventados solo para practicar y están rotulados
como tales; no se adapta ni se reproduce ningún relato tradicional. Las únicas expresiones en lengua indígena son
saludos y palabras muy atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu). Los recursos digitales se
describen sin marcas ni enlaces y siempre con un adulto. Cada tarea abierta remite al educador/a tradicional o a la
comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LR5, LS1 = "LC03 OA LR05", "LC03 OA LS01"

CONSULT = " Recuerda: la forma tradicional de escribir, decir y usar estas palabras la enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de escritura, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

FICHA_SAL = "Ficha: «mari mari» es un saludo y «chaltumay» quiere decir «gracias», ambas en mapuzugun."
FICHA_PAL = "Ficha de palabras en mapuzugun (de práctica): «ko» es agua, «antü» es sol, «kuyen» es luna, «ruka» es la casa mapuche, «mapu» es tierra, «ñuke» es madre."
LISTA_AUT = "Lista autorizada de práctica (inventada): la educadora tradicional de una Escuela Ejemplo autoriza usar en el recurso del curso «mari mari» (saludo), «chaltumay» (gracias) y «ko» (agua), todas en mapuzugun. Las demás palabras no están autorizadas hasta que ella las revise."


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


# =================================================================== LR05 clase 1 · propósito y límites
L(
    LR5, 1,
    materials="Lápiz y hoja. Cuando se usen aparatos (computador, tableta, grabadora), siempre con una persona adulta presente. Los acuerdos de este cuaderno son de práctica.",
    use="Aprenderé a acordar con mi curso para qué haremos un recurso digital y qué límites vamos a respetar. Sirve para crear algo útil para cuidar una lengua sin hacer daño a nadie.",
    prior=["Sé que las palabras indígenas se usan con fuente y permiso.", "Sé que no se pide a nadie datos privados."],
    explain=[
        "Las TIC son las tecnologías de la información y la comunicación: computadores, tabletas, teléfonos, cámaras y grabadoras. Con ellas puedo crear recursos escritos o audiovisuales, como un afiche digital, una presentación o un audio, para expresar ideas y sentimientos sobre una cultura.",
        "Antes de crear, el curso acuerda tres cosas. El propósito: qué queremos lograr, por ejemplo agradecer o saludar con una palabra autorizada. La audiencia: quién lo verá, por ejemplo las familias del curso. Los límites: lo que no haremos, aunque se pueda hacer con el aparato.",
        "Los límites protegen a las personas y a la lengua. No grabamos a nadie sin su permiso. No mostramos ceremonias ni lugares que una comunidad cuida. No usamos palabras sin fuente. No ponemos datos personales. Si alguien no quiere salir en el recurso, lo respetamos.",
    ],
    vocab=[("TIC", "tecnologías de la información y la comunicación"), ("recurso digital", "trabajo hecho con un aparato, como un afiche o un audio"), ("propósito", "lo que queremos lograr"), ("audiencia", "las personas que verán o escucharán el recurso"), ("límite", "algo que acordamos no hacer")],
    worked=[
        W("Propósito, audiencia y límite", "Un curso quiere hacer una presentación para agradecer a la educadora tradicional con la palabra autorizada «chaltumay». Dice: «La verán las familias del curso. No pondremos rostros». Nombra el propósito, la audiencia y el límite.", ["Propósito: agradecer a la educadora.", "Audiencia: las familias del curso.", "Límite: no poner rostros."], "propósito: agradecer; audiencia: las familias; límite: no poner rostros"),
        W("Elegir lo que respeta límites", "Ideas: A) mostrar una ceremonia grabada. B) agradecer con la palabra «chaltumay» autorizada. C) grabar a una compañera sin avisarle. ¿Cuál respeta los límites?", ["A muestra algo que una comunidad cuida.", "C graba sin permiso.", "B usa una palabra autorizada."], "B"),
    ],
    mistakes=[
        M("Pensar que, si el aparato permite grabar, ya puedo grabar a cualquiera.", "Que se pueda hacer no significa que esté permitido.", "Pido permiso antes de grabar y respeto un no."),
        M("Crear el recurso sin acordar el propósito.", "No sé para qué sirve ni a quién le sirve.", "Primero escribo el propósito y la audiencia."),
    ],
    R=[
        ex("TIC significa tecnologías de la información y la comunicación. ¿Un computador es una TIC? Sí o No.", "Sí", "Es un aparato que sirve para comunicar y crear."),
        ex("Un curso quiere hacer un video para agradecer a la educadora. ¿Eso es un propósito o un límite?", "un propósito", "Dice lo que el curso quiere lograr."),
        ex("¿Cuál es un límite: «no grabar a nadie sin permiso» o «hacer el video más largo»?", "no grabar a nadie sin permiso", "Un límite dice lo que no haremos."),
    ],
    C=[
        ex("Acuerdo de práctica: propósito, saludar a las familias; audiencia, las familias del curso; límite, no mostrar rostros. ¿Quiénes verán el recurso?", "las familias del curso", "La audiencia es quien lo verá."),
        ex("Cuáles son TIC: A) lápiz, B) tableta, C) grabadora de voz, D) cuaderno. Escribe las letras.", "B, C", "La tableta y la grabadora son tecnologías."),
        ex("Verdadero o falso: basta con que yo quiera grabar a otra persona para tener su permiso.", "Falso", "El permiso lo da la otra persona."),
    ],
    A=[
        ex("Un curso escribió el propósito y los límites de su recurso, pero no dijo quiénes lo verán. ¿Qué parte del acuerdo le falta?", "la audiencia", "La audiencia es quien verá el recurso."),
        ex("Propósito: enseñar a saludar con «mari mari». ¿Qué límite es mejor? A) usar solo la palabra que autorizó la educadora. B) usar todas las palabras que encuentre.", "A", "El límite A protege la lengua y la fuente."),
        ex("¿Cuáles son límites? 1) no grabar sin permiso. 2) usar muchos colores. 3) no poner datos personales. 4) no mostrar ceremonias. Escribe los números.", "1, 3 y 4", "Los límites dicen lo que no haremos; los colores son una decisión de diseño."),
    ],
    Z=[
        ex("Una niña quiere grabar la voz de una persona invitada. ¿Qué debe hacer primero: pedirle permiso y explicarle el propósito, o grabar rápido?", "pedirle permiso y explicarle el propósito", "La persona debe saber para qué se usará su voz."),
        ex("Pedro dice: «Si el recurso es para cuidar una lengua, no necesito límites». ¿Tiene razón?", "No", "Los límites protegen a las personas aunque el propósito sea bueno."),
    ],
    D=[
        ex("Ordena el acuerdo: A) decido qué no haremos. B) defino el propósito. C) pienso quién lo verá. Escribe las letras en el orden de esta clase.", "B, C, A", "Primero el propósito, luego la audiencia y al final los límites."),
        ex("Un compañero no quiere salir en el recurso. ¿Qué haces: lo incluyo igual o respeto su decisión?", "respeto su decisión", "Cada persona decide si aparece."),
    ],
    context=[ex("Tu curso hará una presentación digital para dar la bienvenida a una visita. ¿Qué escribes como propósito: «dar la bienvenida con una palabra autorizada» o «mostrar fotos de todos»?", "dar la bienvenida con una palabra autorizada", "Es un propósito claro y no expone a nadie.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué significa la sigla TIC?", "tecnologías de la información y la comunicación", "Es el nombre de esos aparatos y herramientas."),
        ex("¿Quién decide si su voz o su imagen aparecen en un recurso?", "la propia persona", "Nadie puede decidirlo por otra."),
        ex("¿Qué dos cosas debo acordar además de los límites?", "el propósito y la audiencia", "Son las tres partes del acuerdo."),
    ],
    task=T(
        "Completa un acuerdo de práctica para un recurso digital de tu curso. Elige un propósito de esta lista: a) saludar a las familias con «mari mari», b) agradecer a la educadora con «chaltumay». Elige una audiencia: las familias del curso o el resto de la escuela. Escribe tres límites tomados de esta lista: no grabar sin permiso, no mostrar ceremonias, no usar palabras sin fuente, no poner datos personales, no mostrar rostros. " + FICHA_SAL + " Termina con una pregunta para la educadora tradicional.",
        "Propósito: agradecer con «chaltumay». Audiencia: las familias del curso. Límites: no grabar sin permiso; no usar palabras sin fuente; no mostrar rostros. Pregunta: ¿qué otra palabra podríamos usar con su permiso?",
        ["escribe propósito, audiencia y tres límites", "los límites protegen a las personas y a la lengua", "usa solo las palabras de la ficha", "formula una pregunta para el educador/a tradicional"],
        ["acuerdo escrito en el cuaderno", "pregunta escrita o dicha en voz alta"],
        ["no escribir límites", "usar una palabra que la ficha no trae"],
        "Verifica que los límites protejan a personas y lengua; si agregó una palabra que no está en la ficha, pídele que la cambie por una pregunta.",
    ),
    reinforce="Explica a un adulto, con tus palabras, qué son el propósito, la audiencia y los límites de un recurso.",
    extend="Escribe dos límites más que pondrías para un audio de tu curso y di por qué los pondrías.",
)

# =================================================================== LR05 clase 2 · expresiones autorizadas
L(
    LR5, 2,
    materials="Lápiz y hoja. La lista autorizada está escrita en este cuaderno; es inventada para practicar.",
    use="Aprenderé a elegir, para un recurso digital, solo las expresiones que tienen fuente y autorización. Sirve para que el recurso cuide la lengua y no repita palabras sin saber de dónde vienen.",
    prior=["Sé qué es el propósito de un recurso.", "Sé que una palabra necesita fuente y permiso."],
    explain=[
        "Una expresión autorizada es la que su fuente permite usar. En la vida real la autoriza una persona que conoce y cuida la lengua, como el educador o la educadora tradicional, y lo hace para un uso concreto. Que una palabra aparezca en muchos lugares no la hace autorizada.",
        "Para seleccionar, sigo tres pasos. Pienso el propósito: qué quiero decir. Reviso la lista autorizada y escojo solo lo que sirve para ese propósito. Anoto para cada palabra su significado y su fuente. Así el recurso no queda con palabras sueltas, como decoración.",
        "Si una palabra me gusta pero no está en la lista, no la uso. La anoto como una pregunta para la educadora. Y si la lista la autoriza para saludar, no la uso para otra cosa, como un juego o una burla. El permiso tiene un uso claro.",
    ],
    vocab=[("autorizada", "que su fuente permite usar"), ("seleccionar", "elegir entre varias cosas"), ("lista", "serie de datos ordenados"), ("decoración", "adorno que no aporta significado"), ("uso", "para qué se emplea una palabra")],
    worked=[
        W("Elegir por propósito", LISTA_AUT + " Propósito: agradecer a la visita. ¿Qué expresión eliges?", ["Pienso: agradecer es dar las gracias.", "En la lista, «chaltumay» es gracias.", "Elijo «chaltumay»."], "«chaltumay»"),
        W("Palabra fuera de la lista", LISTA_AUT + " Un compañero propone la palabra «antü», que le gusta mucho. ¿Qué hacemos?", ["Reviso la lista: «antü» no está.", "No la usamos todavía.", "La anotamos como pregunta para la educadora."], "no la usamos; la anotamos como pregunta"),
    ],
    mistakes=[
        M("Usar una palabra porque aparece en muchos lugares.", "Que sea frecuente no significa que esté autorizada para mi recurso.", "Uso solo lo que dice la lista autorizada."),
        M("Poner palabras solo para que el afiche se vea bonito.", "Sin significado ni fuente son una decoración.", "Escribo el significado y la fuente de cada palabra."),
    ],
    R=[
        ex(LISTA_AUT + " ¿Cuál de estas palabras está en la lista: «ko» o «antü»?", "ko", "La lista autoriza «ko»."),
        ex(LISTA_AUT + " Para saludar, ¿qué expresión autorizada usas?", "mari mari", "La lista la presenta como saludo."),
        ex("Para dar las gracias con la lista autorizada, ¿qué expresión sirve?", "chaltumay", "Es la que quiere decir gracias."),
    ],
    C=[
        ex("Una palabra no está en la lista pero me gusta. ¿Puedo usarla en el recurso? Sí o No.", "No", "Solo se usa lo autorizado."),
        ex("Propósito: hablar del agua. La lista autoriza «mari mari», «chaltumay» y «ko». ¿Cuál sirve?", "ko", "«Ko» es agua."),
        ex("Mi recurso usa «ko» y «chaltumay». La lista autoriza «mari mari», «chaltumay» y «ko». ¿Cuál expresión autorizada no usé?", "mari mari", "Es la que está en la lista y no aparece en el recurso."),
    ],
    A=[
        ex("Un recurso de «saludo y gracias» necesita dos expresiones de la lista autorizada. ¿Cuáles son?", "mari mari y chaltumay", "Una saluda y la otra agradece."),
        ex("Candidatas: 1) «chaltumay», que está en la lista. 2) una palabra escuchada en un video, sin fuente. 3) «ko», que está en la lista. ¿Cuáles puedes usar? Escribe los números.", "1 y 3", "La 2 no tiene fuente ni autorización."),
        ex("¿Qué anotación es completa? A) «ko»: agua (Fuente: lista autorizada de la Escuela Ejemplo). B) «ko».", "A", "La A trae significado y fuente."),
    ],
    Z=[
        ex("Camila dice: «Si una palabra aparece en muchos sitios de internet, ya está autorizada». ¿Tiene razón?", "No", "La autorización la da quien cuida la lengua."),
        ex("La lista autoriza «mari mari» para saludar. Un grupo quiere usarla en un juego para burlarse. ¿Se puede?", "No", "El permiso es para saludar, no para burlarse."),
    ],
    D=[
        ex("Ordena los pasos: A) anoto significado y fuente. B) reviso la lista autorizada. C) pienso el propósito. Escribe las letras.", "C, B, A", "Primero el propósito, luego la lista y al final la anotación."),
        ex("Tu curso quería cinco palabras en el recurso, pero la lista autoriza solo tres. ¿Qué haces con las otras dos: las uso igual o las anoto como preguntas para la educadora?", "las anoto como preguntas para la educadora", "Una palabra que no está en la lista no se usa hasta que se autorice."),
    ],
    context=[ex("Preparan un cartel digital para dar las gracias a una visita. Con la lista autorizada, ¿qué expresión ponen: «chaltumay» o «mari mari»?", "chaltumay", "Quiere decir gracias.")],
    selfcheck=[
        ex("¿Quién autoriza en la vida real el uso de una palabra de una lengua?", "quien la conoce y la cuida", "Puede ser el educador tradicional o la comunidad."),
        ex("Si una palabra me gusta pero no está en la lista, ¿qué hago?", "la anoto como pregunta", "No la uso hasta que se autorice."),
        ex("¿Qué dos datos anoto junto a cada palabra del recurso?", "el significado y la fuente", "Así no es una decoración."),
    ],
    task=T(
        "Usa esta lista de práctica: " + LISTA_AUT + " Elige uno de estos propósitos: a) un cartel de bienvenida, b) una tarjeta de agradecimiento. Selecciona de la lista la expresión que sirve para ese propósito y anota su significado y la fuente («lista autorizada de la Escuela Ejemplo»). Después escribe una palabra que te gustaría usar y que no está en la lista, como una pregunta para la educadora tradicional.",
        "Bienvenida: «mari mari» = saludo (Fuente: lista autorizada de la Escuela Ejemplo). Pregunta: ¿podríamos usar también otra palabra para el sol?",
        ["elige solo expresiones de la lista", "anota significado y fuente de la expresión", "no usa palabras que no están autorizadas", "formula una pregunta para el educador/a tradicional"],
        ["expresión elegida con significado y fuente", "pregunta escrita o dicha en voz alta"],
        ["agregar palabras sin autorización", "olvidar la fuente"],
        "Comprueba que cada palabra tenga significado y fuente; si agregó una palabra no autorizada, pídele que la cambie por una pregunta.",
    ),
    reinforce="Con un adulto, repasa la lista autorizada y di para qué sirve cada expresión.",
    extend="Explica con tus palabras por qué una palabra autorizada para saludar no se usa para burlarse.",
)

# =================================================================== LR05 clase 3 · diseñar un recurso pequeño
L(
    LR5, 3,
    materials="Lápiz, hojas y colores. El diseño se hace primero en papel. Los aparatos, si se usan, siempre con una persona adulta.",
    use="Aprenderé a planear un recurso digital pequeño en papel antes de crearlo. Sirve para que el trabajo tenga orden, incluya la fuente y no se llene de cosas que no corresponden.",
    prior=["Sé acordar propósito, audiencia y límites.", "Sé elegir expresiones autorizadas."],
    explain=[
        "Un recurso pequeño puede ser un afiche digital, una presentación de tres diapositivas o un audio corto en castellano. Antes de usar el aparato, hago un boceto: un dibujo rápido en papel que muestra qué va en cada parte. Así descubro los errores sin gastar tiempo.",
        "Mi plan dice: el formato, las partes en orden y lo que lleva cada una. Por ejemplo, en una presentación de tres diapositivas, la primera lleva el título, la segunda una palabra autorizada con su significado y un dibujo propio, y la tercera los créditos con la fuente.",
        "Pienso también cuánto cabe. Un afiche pequeño no puede llevar muchas palabras: mejor pocas y bien explicadas. Un audio corto se entiende mejor si cada parte tiene una sola idea. Cada parte tiene una razón; si no la tiene, la saco.",
    ],
    vocab=[("boceto", "dibujo rápido que planea cómo será algo"), ("formato", "tipo de recurso, como afiche, presentación o audio"), ("diapositiva", "una pantalla de una presentación"), ("créditos", "datos de quién hizo algo y de dónde vienen las fuentes"), ("plan", "pasos y partes ordenados antes de hacer algo")],
    worked=[
        W("Planear tres diapositivas", "Plan: diapositiva 1, título «Gracias»; diapositiva 2, la palabra «chaltumay» con su significado y un dibujo propio; diapositiva 3, créditos. ¿En qué diapositiva va la fuente?", ["Los créditos llevan la fuente.", "Los créditos están en la diapositiva 3.", "Entonces la fuente va ahí."], "en la diapositiva 3"),
        W("Sacar lo que no tiene razón", "Plan de 4 diapositivas: 1) título «Gracias». 2) la palabra «chaltumay» con su significado. 3) una foto de un cantante famoso que no tiene relación con el propósito. 4) créditos. ¿Qué diapositiva sacas?", ["Pregunto cuál razón tiene cada diapositiva.", "La 1, la 2 y la 4 tienen una razón.", "La 3 no se relaciona con el propósito."], "la 3"),
    ],
    mistakes=[
        M("Empezar a crear con el aparato sin hacer un plan.", "Se pierde tiempo y se olvidan la fuente y los créditos.", "Primero hago el boceto en papel."),
        M("Llenar el afiche con muchas palabras.", "No cabe el significado ni la fuente de cada una.", "Elijo pocas palabras y las explico bien."),
    ],
    R=[
        ex("Antes de crear un recurso digital, ¿hago un plan o empiezo sin pensar?", "hago un plan", "El plan ordena el trabajo."),
        ex("Una presentación de 3 diapositivas, ¿cuántas pantallas tiene?", "3", "Cada diapositiva es una pantalla."),
        ex("¿Cuál formato es solo sonido: afiche, presentación o audio?", "audio", "El audio se escucha y no se ve."),
    ],
    C=[
        ex("Plan: diapositiva 1, título; diapositiva 2, la palabra «ko» con su significado; diapositiva 3, créditos. ¿En qué diapositiva aparece el significado de «ko»?", "en la 2", "La 2 lleva la palabra y su significado."),
        ex("¿Qué dos datos debe llevar cada palabra de mi recurso: el significado según la ficha y la fuente, o un efecto sonoro?", "el significado según la ficha y la fuente", "Así la palabra no es solo decoración."),
        ex("Verdadero o falso: puedo usar en mi recurso la imagen de otra persona sin permiso, porque es tarea.", "Falso", "Las imágenes de otros necesitan permiso."),
    ],
    A=[
        ex("Ordena las partes de una presentación de tres diapositivas: A) créditos con la fuente. B) palabra autorizada con su significado y un dibujo propio. C) título. Escribe las letras en orden.", "C, B, A", "Primero el título, luego la palabra y al final los créditos."),
        ex("Plan A: título «Gracias», palabra «chaltumay», significado, dibujo propio y créditos con la fuente. Plan B: título y la palabra sin significado ni fuente. ¿Cuál plan está completo?", "A", "El A trae significado, fuente y créditos."),
        ex("Una presentación tiene 4 diapositivas: título, saludo, agradecimiento y créditos. Solo el saludo y el agradecimiento llevan una expresión autorizada. ¿Qué diapositivas no la llevan?", "el título y los créditos", "Son las dos que no llevan una expresión."),
    ],
    Z=[
        ex("Ana quiere poner 12 palabras en un afiche pequeño y no queda espacio para la fuente. ¿Es un buen diseño? Sí o No.", "No", "Sin fuente no puedo explicar de dónde vienen."),
        ex("Elige el mejor orden de lectura. A) título, palabra, significado, créditos. B) créditos, significado, título.", "A", "El A se entiende de principio a fin."),
    ],
    D=[
        ex("Ordena los pasos: A) hago el boceto. B) elijo palabras de la lista autorizada. C) decido el propósito. D) creo el recurso con el aparato. Escribe las letras.", "C, B, A, D", "Pienso, elijo, planeo y recién creo."),
        ex("Un video tiene tres escenas: la 1 con «mari mari», la 2 con «chaltumay» y la 3 con una palabra que no está en la lista autorizada. ¿Qué haces con la escena 3?", "saco la palabra y la anoto como pregunta para la educadora", "Una palabra sin autorización no se usa."),
    ],
    context=[ex("Tu curso hará un afiche digital para agradecer a la educadora. ¿Qué es mejor poner: título «Gracias», «chaltumay» con su significado, dibujo propio y créditos, o solo una foto de ella sin permiso?", "título «Gracias», «chaltumay» con su significado, dibujo propio y créditos", "Cuida la fuente, el permiso y la autoría.")],
    selfcheck=[
        ex("¿Cómo se llama el dibujo rápido que planea cómo será un recurso?", "boceto", "Es el primer plano en papel."),
        ex("¿Qué parte del recurso dice quién hizo cada cosa y de dónde vienen las fuentes?", "los créditos", "Ahí se anotan autoría y fuentes."),
        ex("¿Las imágenes de mi recurso deben ser propias o tener permiso?", "propias o con permiso", "No se toma una imagen sin permiso."),
    ],
    task=T(
        "Planea en papel un recurso de tres diapositivas con la lista autorizada: " + LISTA_AUT + " Dibuja tres rectángulos. En el primero escribe el título y el propósito. En el segundo escribe una expresión de la lista con su significado e indica qué dibujo propio la acompañará. En el tercero escribe los créditos: «Palabra: lista autorizada de la Escuela Ejemplo. Dibujos: del curso.» Escribe en una línea la razón de cada diapositiva. Termina con una pregunta para la educadora tradicional.",
        "Diapositiva 1: «Gracias» (propósito: agradecer). Diapositiva 2: «chaltumay» = gracias; dibujo propio: una tarjeta. Diapositiva 3: créditos. Razones: el título dice el propósito, la palabra agradece y los créditos nombran la fuente. Pregunta: ¿está bien cómo presentamos la palabra?",
        ["tres diapositivas con su contenido", "la expresión es de la lista y tiene significado", "los créditos nombran la fuente", "formula una pregunta para el educador/a tradicional"],
        ["boceto en papel con tres rectángulos y una razón por diapositiva", "pregunta escrita o dicha en voz alta"],
        ["olvidar los créditos", "usar una imagen ajena"],
        "Revisa que cada parte tenga una razón y que haya créditos; si usó una imagen ajena, pídele que dibuje la suya.",
    ),
    reinforce="Haz un boceto de un afiche con título, una palabra autorizada y créditos, usando solo papel y lápiz.",
    extend="Cambia tu plan de tres diapositivas a un audio de tres partes y escribe qué idea dice cada parte.",
)

# =================================================================== LR05 clase 4 · crear sin reemplazar voces
L(
    LR5, 4,
    materials="Lápiz, hojas y, si hay, un aparato con una persona adulta presente. Los casos de este cuaderno son de práctica.",
    use="Aprenderé a crear mi recurso sin reemplazar las voces de las personas que hablan la lengua. Sirve para que la tecnología ayude a la lengua y no la imite ni la deje sin hablantes.",
    prior=["Sé planear un recurso pequeño.", "Sé que la voz de una persona necesita su permiso."],
    explain=[
        "Revitalizar una lengua es ayudar a que más personas la usen y a que sus hablantes sigan hablándola. Un recurso digital puede ayudar, pero no reemplaza a quienes hablan la lengua. Mi recurso no puede fingir que habla por ellos ni imitar su voz.",
        "Por eso, en mi recurso uso mi voz solo para leer en castellano. No imito el acento de nadie ni uso una voz hecha por computador para decir palabras de una lengua indígena, porque podría equivocarme y pasar por hablante. Si quiero que se escuche una palabra, invito a la educadora a grabarla, con su permiso y para el uso que ella diga.",
        "Si no es posible grabar, escribo la palabra con su fuente y dejo un espacio para que el educador o la educadora la diga en persona cuando presentemos el trabajo. Mis dibujos y mis textos en castellano son la base. La lengua indígena la ponen quienes la hablan.",
    ],
    vocab=[("hablante", "persona que habla una lengua"), ("reemplazar", "ocupar el lugar de otro"), ("imitar", "copiar la voz o la forma de hablar de alguien"), ("grabación", "registro de un sonido en un aparato"), ("presentar", "mostrar un trabajo a otras personas")],
    worked=[
        W("Elegir cómo incluir una palabra", "Quieres que el recurso suene. Opciones: A) imitar con mi voz el acento de la visita. B) invitar a la educadora a grabar «mari mari» con su permiso. C) usar una voz de computador. ¿Cuál es mejor?", ["A imita a una persona y puede ser burla.", "C reemplazaría a un hablante.", "B deja que hable quien sabe, con permiso."], "B"),
        W("Qué hago con mi voz", "Voy a grabar un audio para mi recurso. ¿En qué lengua uso mi voz?", ["Mi voz puede leer lo que sé bien.", "Mi texto del recurso está en castellano.", "Uso mi voz para leer en castellano."], "en castellano"),
    ],
    mistakes=[
        M("Usar una voz de computador para decir palabras de una lengua indígena.", "Puede equivocarse y reemplaza a las personas que sí la hablan.", "Escribo la palabra con su fuente o invito al educador a grabarla."),
        M("Imitar el acento de una visita para que el audio suene más «auténtico».", "Es una imitación y puede sentirse como burla.", "Leo en castellano con mi propia voz."),
    ],
    R=[
        ex("¿Una voz hecha por computador puede reemplazar a una persona que habla una lengua indígena? Sí o No.", "No", "No es una persona hablante."),
        ex("¿Quién puede grabar una palabra indígena para mi recurso, con su permiso: la educadora tradicional o yo imitándola?", "la educadora tradicional", "Ella conoce la lengua."),
        ex("¿En qué lengua puedo usar mi voz para leer mi texto: en castellano o imitando un acento?", "en castellano", "Es la lengua que yo uso de verdad."),
    ],
    C=[
        ex("Verdadero o falso: imitar el acento de una visita es una forma de respeto.", "Falso", "Una imitación puede sentirse como burla."),
        ex("Para que la palabra «ko» se escuche en mi audio, ¿qué necesito primero: el permiso de quien la graba o un efecto de sonido?", "el permiso de quien la graba", "La voz de una persona necesita su permiso."),
        ex("Si no se puede grabar, ¿qué hago con la palabra: la escribo con su fuente o la invento?", "la escribo con su fuente", "No invento una forma de decirla."),
    ],
    A=[
        ex("Tres ideas: 1) escribir «chaltumay» con su fuente. 2) hacer que una voz de computador diga «chaltumay». 3) dibujar una tarjeta de agradecimiento. ¿Cuáles respetan esta clase? Escribe los números.", "1 y 3", "La 2 reemplaza a un hablante."),
        ex("Tu audio tiene tu voz leyendo en castellano. La palabra indígena la dirá la educadora cuando presenten el trabajo. ¿Reemplazas a la educadora?", "No", "Su voz se deja para ella."),
        ex("Tu audio tiene tres partes. 1) Tu voz lee en castellano: «Hoy aprendimos a agradecer». 2) Un espacio para que la educadora diga la palabra. 3) Tu voz lee: «Gracias por enseñarnos». ¿Qué parte no lees tú?", "la 2", "Esa parte se deja para la voz de la educadora."),
    ],
    Z=[
        ex("Valentina dice: «Si el computador dice la palabra, se escucha igual y no necesito molestar a la educadora». ¿Qué le respondes: que puede equivocarse y no es una persona hablante, o que tiene razón?", "que puede equivocarse y no es una persona hablante", "Una voz hecha por computador puede cometer errores."),
        ex("Un grupo quiere imitar la forma de hablar de una visita en un video para una obra. ¿Es respetuoso? Sí o No.", "No", "Puede resultar una burla."),
    ],
    D=[
        ex("Ordena para incluir una palabra con respeto: A) la educadora la graba o la dice en persona. B) pregunto si lo puede hacer y para qué uso. C) yo preparo el espacio en mi recurso. Escribe las letras.", "B, C, A", "Pregunto, preparo y ella participa."),
        ex("¿Cuál recurso es mejor para revitalizar? A) uno que muestra las palabras con fuente y deja que hablen quienes saben. B) uno que imita las voces de los hablantes.", "A", "El A no reemplaza a nadie."),
    ],
    context=[ex("Para la presentación del curso, un niño propone que un programa haga «hablar» a un personaje en lengua indígena. ¿Qué propones tú: invitar a la educadora a decir la palabra o aceptar su idea?", "invitar a la educadora a decir la palabra", "Así se escucha la voz de quien sabe.")],
    selfcheck=[
        ex("¿Qué es una persona hablante?", "alguien que habla una lengua", "Es quien usa la lengua al comunicarse."),
        ex("¿Uso mi voz para imitar acentos?", "No", "Imitar puede ser burla."),
        ex("¿Quién da la voz a las palabras indígenas en mi presentación?", "quien las habla, con su permiso", "La lengua la ponen sus hablantes."),
    ],
    task=T(
        "Escribe un guion de práctica de un audio de 20 segundos en castellano para agradecer a la educadora: «Hoy aprendimos palabras con ayuda de la educadora tradicional de la Escuela Ejemplo. Gracias por enseñarnos.» " + FICHA_SAL + " Marca con una línea el espacio donde la educadora diría ella misma «chaltumay», si lo autoriza. Escribe qué no harás (por ejemplo, no imitar acentos ni usar una voz de computador) y una pregunta para la educadora sobre cómo prefiere participar.",
        "Guion: Hoy aprendimos palabras con ayuda de la educadora tradicional. [Espacio para que ella diga «chaltumay»]. Gracias por enseñarnos. No haré: imitar acentos. Pregunta: ¿prefiere decirlo en persona o que escribamos la palabra?",
        ["el texto está en castellano y leído con voz propia", "deja un espacio para la voz de quien sabe", "escribe al menos un «no haré»", "formula una pregunta para el educador/a tradicional"],
        ["guion con el espacio marcado", "pregunta escrita o dicha en voz alta"],
        ["escribir cómo se dice la palabra", "usar una voz imitada"],
        "Comprueba que el guion esté en castellano y que no reemplace voces; si el estudiante escribió una pronunciación, pídele que la cambie por una pregunta.",
    ),
    reinforce="Lee en voz alta, con tu propia voz y en castellano, el guion de la clase.",
    extend="Escribe dos razones por las que una voz de computador no debe reemplazar a un hablante.",
)

# =================================================================== LR05 clase 5 · devolver, atribuir, controlar acceso
L(
    LR5, 5,
    materials="Lápiz y hoja. Los casos de este cuaderno son de práctica; no se publica nada en internet.",
    use="Aprenderé a mostrar mi recurso primero a quien lo ayudó, a anotar los créditos y a decidir quién puede verlo. Sirve para cuidar a las personas y a la lengua después de crear.",
    prior=["Sé planear un recurso con créditos.", "Sé que no se reemplazan las voces de los hablantes."],
    explain=[
        "Devolver es mostrar el recurso, antes que a nadie, a la educadora o al educador tradicional que ayudó, para que lo revise. Si encuentra un error, lo corregimos. Si pide que no se comparta algo, lo respetamos. Así el trabajo vuelve a la comunidad que enseñó.",
        "Atribuir es anotar quién hizo cada cosa: la fuente de las palabras, quiénes del curso crearon el recurso y para qué se hizo. Controlar el acceso es decidir quién puede verlo: solo el curso, las familias con aviso, o nadie más. Un recurso no se publica abierto en internet sin permiso.",
        "Publicar no siempre ayuda a revitalizar. Si la palabra está mal escrita, si falta permiso o si se usa sin respeto, el recurso puede hacer daño. Cuidar quién lo ve es parte de revitalizar con respeto.",
    ],
    vocab=[("devolver", "mostrar el trabajo a quien enseñó para que lo revise"), ("atribuir", "anotar quién hizo cada cosa y de dónde viene"), ("acceso", "quiénes pueden ver o escuchar el recurso"), ("publicar", "hacer que cualquiera pueda ver algo"), ("aviso", "información dada antes para que alguien pueda decidir")],
    worked=[
        W("Ordenar los pasos finales", "Pasos: A) crear el recurso. B) devolverlo a la educadora para que lo revise. C) corregir lo que ella indique. D) mostrarlo al público acordado. ¿En qué orden?", ["Primero creo.", "Luego devuelvo y corrijo.", "Al final muestro a quien se acordó."], "A, B, C, D"),
        W("Escoger el acceso", "El permiso de la educadora dice: solo para mostrar a las familias del curso. ¿Puedes subir el recurso a un sitio abierto de internet?", ["Leo el permiso: familias del curso.", "Un sitio abierto lo vería cualquiera.", "No cumpliría con el permiso."], "No"),
    ],
    mistakes=[
        M("Pensar que publicar siempre ayuda a que la lengua viva.", "Un recurso con errores o sin permiso puede hacer daño.", "Primero devuelvo, corrijo y controlo el acceso."),
        M("Poner créditos solo con mi nombre.", "Se olvida a quien enseñó las palabras.", "Agrego la fuente de las palabras y quiénes ayudaron."),
    ],
    R=[
        ex("Antes de compartir, ¿a quién le muestro primero el recurso: a la educadora que ayudó o a cualquiera?", "a la educadora que ayudó", "Ella puede revisarlo."),
        ex("Anotar quién hizo cada cosa se llama atribuir. ¿Es verdadero o falso?", "Verdadero", "Atribuir es dar créditos."),
        ex("Controlar el acceso es decidir quién puede ver el recurso. ¿Verdadero o falso?", "Verdadero", "Es elegir la audiencia con cuidado."),
    ],
    C=[
        ex("Créditos A: «Hecho por el curso. Palabras: lista autorizada de la educadora.» Créditos B: «Hecho por mí.» ¿Cuáles nombran la fuente?", "A", "El B no menciona de dónde vienen las palabras."),
        ex("El permiso dice: «solo para mostrar en la sala». ¿Quiénes pueden verlo: los del curso o todo el mundo?", "los del curso", "El permiso limita el acceso a la sala."),
        ex("Verdadero o falso: si el recurso se publica abierto en internet, ayuda siempre a revitalizar una lengua.", "Falso", "Puede dañar si hay errores o falta permiso."),
    ],
    A=[
        ex("Ordena: A) corrijo lo que dice la educadora. B) le devuelvo el recurso. C) decido quién lo ve, según su permiso. Escribe las letras.", "B, A, C", "Devuelvo, corrijo y luego decido el acceso."),
        ex("El permiso dice: «para el curso y para las familias con aviso». 1) una compañera del curso. 2) una familia que recibió el aviso. 3) una persona desconocida de internet. ¿Quiénes pueden verlo? Escribe los números.", "1 y 2", "La 3 no está dentro del permiso."),
        ex("La educadora revisó el recurso y dijo que no se mostrara a otros cursos. ¿Qué haces con el recurso?", "lo muestro solo a quien ella permitió", "Su indicación manda sobre el acceso."),
    ],
    Z=[
        ex("Un niño dice: «Mejor lo subo abierto a internet; así más gente aprende». ¿Qué falta revisar primero?", "el permiso y la revisión de la educadora", "Sin eso podría haber errores o usos no permitidos."),
        ex("Una niña quiere borrar el nombre de la educadora de los créditos para que se vea más ordenado. ¿Es buena idea? Sí o No.", "No", "La fuente debe estar nombrada."),
    ],
    D=[
        ex("Créditos completos: A) fuente de las palabras, quiénes hicieron el recurso y para qué. B) solo el título. ¿Cuál escribes?", "A", "Atribuye y explica el propósito."),
        ex("Tres decisiones de acceso: 1) solo el curso. 2) las familias con aviso. 3) abierto a todo internet sin permiso. ¿Cuál no corresponde si no hay permiso?", "3", "Abrir a todos sin permiso no se debe hacer."),
    ],
    context=[ex("Tu curso terminó un afiche digital con la palabra «ko». La educadora aún no lo ha revisado. ¿Qué haces: mostrarlo a otro curso hoy o primero devolvérselo a ella?", "devolvérselo a ella", "Debe revisarlo antes de compartirlo.")],
    selfcheck=[
        ex("¿Cómo se llama mostrar el trabajo a quien enseñó para que lo revise?", "devolver", "Es el primer paso después de crear."),
        ex("¿Qué debo anotar para dar créditos a las palabras?", "la fuente", "Dice de dónde vienen."),
        ex("¿Quién decide el acceso a un recurso hecho con palabras autorizadas?", "quien dio el permiso", "Su permiso fija los límites."),
    ],
    task=T(
        "Completa una ficha de cierre de práctica para el recurso «Gracias» de tu curso. Escribe: 1) a quién se lo devolverás primero, 2) los créditos en dos líneas (la fuente de las palabras y quiénes lo hicieron), 3) quién podrá verlo, eligiendo entre «solo el curso», «las familias con aviso» o «nadie más». " + FICHA_SAL + " Termina con una pregunta para la educadora tradicional sobre si el recurso puede mostrarse a otros.",
        "Devolver a: la educadora tradicional de la Escuela Ejemplo. Créditos: Palabras de la lista autorizada de la educadora. Hecho por el curso. Acceso: solo el curso. Pregunta: ¿podemos mostrarlo a las familias?",
        ["elige a quién devolver primero", "escribe créditos que nombran la fuente", "decide un acceso limitado", "formula una pregunta para el educador/a tradicional"],
        ["ficha escrita", "pregunta escrita o dicha en voz alta"],
        ["publicar abierto sin permiso", "omitir la fuente en los créditos"],
        "Revisa que los créditos nombren la fuente y que el acceso sea limitado; si propuso publicar abierto, recuérdale que falta permiso.",
    ),
    reinforce="Cuenta a un adulto los tres pasos finales: devolver, atribuir y controlar el acceso.",
    extend="Escribe una frase de créditos para un cartel de tu curso que nombre la fuente de las palabras y a quienes lo hicieron.",
)

# =================================================================== LS01 clase 1 · acercarse sin apropiarse
L(
    LS1, 1,
    materials="Lápiz y hoja. Las situaciones están escritas en este cuaderno; son inventadas para practicar.",
    use="Aprenderé a escuchar con respeto textos orales y palabras de otra cultura sin imitarlos ni tomarlos como míos. Sirve para acercarme a otras culturas sin hacer daño.",
    prior=["Sé escuchar sin interrumpir.", "Sé que el educador tradicional enseña la lengua y la cultura de su pueblo."],
    explain=[
        "Un texto oral es lo que se dice en voz alta, como un relato, un saludo o una explicación. Cuando una visita habla, yo escucho con atención. Escuchar ya es participar. Nadie tiene que repetir sonidos si no quiere, y nadie debe imitar para hacer reír.",
        "Hay cuatro formas de acercarme a lo de otra cultura. Aprender es escuchar y entender con quien sabe. Reproducir es repetir tal cual algo que me dieron permiso de repetir. Recrear es hacer algo nuevo inspirado, con respeto y avisando. Apropiarme es tomar como mío lo de otros, sin permiso ni crédito, y eso no se hace.",
        "Las palabras, relatos, cantos y bailes que cuida una comunidad son parte de su historia. Me acerco con preguntas: ¿quién lo cuenta?, ¿puedo compartirlo?, ¿cómo lo nombro? Y no copio algo que una comunidad cuida solo porque me gustó.",
    ],
    vocab=[("texto oral", "lo que se dice en voz alta y se escucha"), ("aprender", "escuchar y entender con quien sabe"), ("reproducir", "repetir tal cual algo con permiso"), ("recrear", "hacer algo nuevo inspirado, con respeto y avisando"), ("apropiarse", "tomar como propio lo de otros sin permiso ni crédito")],
    worked=[
        W("Clasificar una acción", "Una niña escucha un relato de la educadora y luego dice que ella lo inventó. ¿Aprende o se apropia?", ["Escuchó el relato, eso está bien.", "Pero dice que es suyo.", "Tomó como propio lo de otra persona."], "se apropia"),
        W("Elegir la respuesta respetuosa", "Un compañero imita los sonidos de una visita para hacer reír. ¿Qué le dices? A) «Escuchemos con respeto». B) «Hazlo más fuerte».", ["La imitación puede ser una burla.", "La A invita a escuchar.", "Elijo A."], "A"),
    ],
    mistakes=[
        M("Creer que debo repetir los sonidos para participar.", "Escuchar con atención ya es participar.", "Escucho y pregunto si quiero saber más."),
        M("Copiar un canto o baile que una comunidad cuida para una obra del colegio.", "Puede ser algo que solo se comparte de cierta forma.", "Pregunto a la educadora qué se puede compartir."),
    ],
    R=[
        ex("Una visita dice una palabra de su lengua. ¿Qué hago primero: escucho con atención o me río?", "escucho con atención", "La atención muestra respeto."),
        ex("¿Debo repetir una palabra si no quiero hacerlo? Sí o No.", "No", "Escuchar ya es una forma de participar."),
        ex("Escuchar con respeto, ¿es una forma de participar? Sí o No.", "Sí", "Quien escucha también aprende."),
    ],
    C=[
        ex("Une: 1) tomar como propio lo de otros sin permiso ni crédito. 2) escuchar y entender con quien sabe. Escribe la palabra de cada una.", "apropiarse, aprender", "La 1 es apropiarse y la 2, aprender."),
        ex("Verdadero o falso: imitar con burla los sonidos de una lengua es una forma de respeto.", "Falso", "La burla daña."),
        ex("Escuché un relato de la educadora y digo que yo lo inventé. ¿Estoy aprendiendo o apropiándome?", "apropiándome", "Lo digo como mío sin crédito."),
    ],
    A=[
        ex("Acciones: A) escuchar sin interrumpir. B) imitar el acento para hacer reír. C) preguntar con respeto. D) decir que el relato es mío. ¿Cuáles son respetuosas? Escribe las letras.", "A y C", "B y D no respetan a quien lo cuenta."),
        ex("La visita no pide que nadie repita sus palabras. ¿Puede el curso participar escuchando y preguntando? Sí o No.", "Sí", "Escuchar y preguntar es participar."),
        ex("Una niña propone que todos repitan una palabra en coro, aunque algunos no quieren. ¿Qué propones: A) obligar a todos. B) invitar a repetir a quien quiera y dejar que los demás escuchen.", "B", "Nadie debe ser obligado a repetir."),
    ],
    Z=[
        ex("Un niño dice: «Si repito los sonidos igual que la visita, ya aprendí su lengua». ¿Qué falta: la guía de quien enseña o más volumen?", "la guía de quien enseña", "Aprender una lengua requiere a quien la sabe."),
        ex("Copiar un baile o un canto que cuida una comunidad, sin permiso, para una obra del colegio. ¿Es respetuoso? Sí o No.", "No", "Se toma algo de otros sin permiso."),
    ],
    D=[
        ex("Tres acciones: 1) copiar una historia diciendo que es tuya. 2) escuchar la historia y preguntar de qué fuente viene. 3) contar la historia nombrando a quien te la contó, con su permiso. ¿Cuál es una apropiación? Escribe el número.", "1", "Es la que la presenta como propia."),
        ex("Ordena: A) pregunto si puedo compartirlo. B) escucho con atención. C) lo comparto nombrando la fuente. Escribe las letras.", "B, A, C", "Escucho, pido permiso y recién comparto."),
    ],
    context=[ex("Una visita termina de saludar con «mari mari». Un compañero quiere hacer un chiste con esa expresión. ¿Qué le dices: «Mejor preguntemos qué significa» o «Dilo más fuerte»?", "«Mejor preguntemos qué significa»", "Preguntar muestra respeto.")],
    selfcheck=[
        ex("¿Qué significa apropiarse de algo de otros?", "tomarlo como mío sin permiso ni crédito", "Es lo contrario de aprender con respeto."),
        ex("Si no quiero repetir una palabra, ¿cómo participo?", "escuchando y preguntando", "Escuchar es participar."),
        ex("¿A quién le pregunto si puedo compartir un relato que cuenta una comunidad?", "al educador tradicional o a la comunidad", "Ellos lo cuidan."),
    ],
    task=T(
        "Lee esta situación inventada para practicar: «Una visita contó que en su comunidad se saluda con «mari mari». Dos niños dijeron cosas diferentes. Un niño: «Mejor escuchemos y preguntemos». Otro: «Digamos que yo lo inventé». » " + "Ficha: «mari mari» es un saludo en mapuzugun. En tu cuaderno escribe: 1) cuál niño aprende y cuál se apropia, 2) una pregunta respetuosa para la visita, 3) qué haces tú si no quieres repetir una palabra.",
        "Aprende el primer niño. Se apropia el segundo. Pregunta: ¿cuándo se dice «mari mari» en su comunidad? Si no quiero repetir, escucho con atención.",
        ["distingue aprender y apropiarse", "escribe una pregunta respetuosa", "explica cómo participar escuchando", "no inventa significados"],
        ["tres respuestas escritas", "pregunta escrita o dicha en voz alta"],
        ["confundir aprender con apropiarse", "obligar a repetir"],
        "Valora que reconoce la apropiación y propone escuchar; si imitó o se burló, conversa sobre el respeto sin humillar.",
    ),
    reinforce="Dibuja una escena donde alguien escucha con atención a una visita y escribe una frase que diga cómo participa.",
    extend="Explica con tus palabras la diferencia entre aprender y apropiarse con un ejemplo de tu curso.",
)

# =================================================================== LS01 clase 2 · situar relato y fuente
FICHA_REL = "Ficha oral A (inventada para practicar): Relato: «Luz y la vecina». Lo cuenta: el profesor del curso, que lo inventó para practicar. Pueblo: no corresponde, no es un relato de ningún pueblo. Territorio: no corresponde. Permiso: es del curso. Para qué: practicar la escucha."

L(
    LS1, 2,
    materials="Lápiz y hoja. Un adulto lee en voz alta los relatos de práctica. Todos son inventados y no pertenecen a ningún pueblo.",
    use="Aprenderé a situar un relato oral: saber quién lo cuenta, de qué pueblo y territorio viene, si hay permiso y para qué se cuenta. Sirve para no mezclar relatos ni atribuirlos a quien no corresponde.",
    prior=["Sé la diferencia entre aprender y apropiarme.", "Sé que una fuente es quien sabe y comparte algo."],
    explain=[
        "Situar un relato es ubicarlo: decir quién lo cuenta, de qué pueblo y territorio viene, si hay permiso para compartirlo y para qué se cuenta. Esos datos se anotan en una ficha oral, igual que la ficha de procedencia de un texto escrito.",
        "En esta clase todos los relatos son de práctica, inventados por el curso. Por eso la ficha dice «no corresponde» en pueblo y territorio. Un relato inventado no se atribuye a ningún pueblo. En la vida real, quien cuenta un relato tradicional dice a qué pueblo pertenece y qué se puede compartir.",
        "Cuando escucho un relato de verdad hago cuatro preguntas: ¿quién lo cuenta?, ¿de qué pueblo y territorio es?, ¿puedo compartirlo?, ¿para qué se cuenta? Si no me responden, no lo atribuyo a ningún pueblo ni lo cuento como si lo supiera.",
    ],
    vocab=[("relato", "texto oral que cuenta algo"), ("situar", "ubicar quién, de dónde y para qué"), ("ficha oral", "papel que anota datos de un relato escuchado"), ("pueblo", "grupo con una historia, una cultura y una lengua propias"), ("territorio", "lugar donde vive y se cuida una comunidad")],
    worked=[
        W("Leer una ficha oral", FICHA_REL + " ¿Quién cuenta el relato?", ["Busco la línea «Lo cuenta».", "Dice: el profesor del curso.", "Es el narrador."], "el profesor del curso"),
        W("Qué hago sin datos", "Escuché un relato en una reunión. Nadie dijo quién lo contó ni de qué pueblo es. ¿Puedo decir a mis amigos que es un relato de un pueblo en particular?", ["Reviso los datos que tengo.", "No sé quién lo cuenta ni de dónde es.", "No debo atribuirlo a ningún pueblo."], "No"),
    ],
    mistakes=[
        M("Decir que un relato de práctica es de un pueblo originario.", "Fue inventado por el curso.", "Digo «relato de práctica inventado» y no lo atribuyo a ningún pueblo."),
        M("Contar un relato sin decir quién lo contó.", "La fuente queda olvidada.", "Digo siempre «lo escuché de…»."),
    ],
    R=[
        ex(FICHA_REL + " ¿Quién cuenta el relato «Luz y la vecina»?", "el profesor del curso", "Lo dice la ficha."),
        ex("En la ficha A, ¿el relato pertenece a un pueblo originario? Sí o No.", "No", "La ficha dice que no corresponde."),
        ex("En la ficha A, ¿para qué se cuenta el relato?", "para practicar la escucha", "Ese es su propósito."),
    ],
    C=[
        ex("Relato de práctica: «Luz saludó a su vecina con un «mari mari». Su vecina sonrió.» ¿A qué pueblo atribuyes este relato inventado?", "a ninguno", "Es un relato inventado por el curso."),
        ex("Ficha oral B (inventada): Relato: «La visita». Lo cuenta: una persona de la comunidad. Pueblo: por preguntar. Territorio: por preguntar. Permiso: por preguntar. ¿Qué datos faltan antes de compartir el relato?", "pueblo, territorio y permiso", "La ficha dice «por preguntar» en esas líneas."),
        ex("Verdadero o falso: si no sé de qué pueblo es un relato, puedo inventar el dato para completar la ficha.", "Falso", "No debo inventar datos."),
    ],
    A=[
        ex("Cuatro preguntas para situar un relato: ¿quién lo cuenta?, ¿de qué pueblo y territorio?, ¿puedo compartirlo?, ¿para qué se cuenta? Quieres saber si el relato se puede contar a otros. ¿Cuál pregunta te lo dice?", "¿puedo compartirlo?", "Esa pregunta trata del permiso."),
        ex("Ficha oral C (inventada): Relato: «Gracias». Lo cuenta: la educadora tradicional de la Escuela Ejemplo. Permiso: solo dentro de la sala. Para qué: enseñar una palabra. ¿Puedes contarlo en una radio abierta? Sí o No.", "No", "El permiso es solo dentro de la sala."),
        ex("¿Qué frase es mejor al contar un relato de práctica? A) «Lo escuché de mi profesor, que lo inventó». B) «Es un relato de un pueblo antiguo».", "A", "La A dice la fuente real."),
    ],
    Z=[
        ex("Pedro dice: «Todos los relatos que escucho en clase son de un pueblo originario». ¿Tiene razón?", "No", "Algunos son inventados para practicar."),
        ex("Un relato de práctica menciona «mari mari». ¿Eso lo convierte en un relato de ese pueblo? Sí o No.", "No", "Usar una expresión no cambia que el relato fue inventado."),
    ],
    D=[
        ex("Ordena los pasos: A) anoto en la ficha lo que me responden. B) pregunto quién lo cuenta. C) escucho el relato. Escribe las letras.", "C, B, A", "Escucho, pregunto y anoto."),
        ex("Ficha oral D (inventada): Relato: «El camino». Lo cuenta: un invitado. Pueblo: no se indica. Permiso: no se indica. ¿Qué haces: lo cuentas como relato de un pueblo o pides los datos que faltan?", "pido los datos que faltan", "Sin pueblo ni permiso no puedo atribuirlo."),
    ],
    context=[ex("Tu amiga te cuenta un relato y dice: «Es de un pueblo, pero no sé cuál». ¿Qué le sugieres: preguntar a la educadora tradicional o decir que es de cualquier pueblo?", "preguntar a la educadora tradicional", "Ella puede ayudar a situar el relato.")],
    selfcheck=[
        ex("¿Cómo se llama el papel que anota quién cuenta un relato, de dónde es y para qué?", "ficha oral", "Es la ficha de un relato escuchado."),
        ex("Si un relato es inventado por el curso, ¿qué pongo en pueblo y territorio?", "no corresponde", "No pertenece a ningún pueblo."),
        ex("¿Qué hago si no sé a qué pueblo pertenece un relato?", "pregunto", "No lo atribuyo sin saber."),
    ],
    task=T(
        "Lee en voz alta, o pide a un adulto que lea, este relato de práctica inventado: «Luz vivía cerca de un río. Cada mañana saludaba a su vecina con un «mari mari». Una tarde llevó agua a su vecina y ella le dijo «chaltumay». Luz sonrió y volvió a casa.» " + FICHA_SAL + " Completa una ficha oral con estas líneas: Relato, Lo cuenta, Pueblo, Territorio, Permiso, Para qué. Escribe «no corresponde» donde sea un relato inventado. Termina con una pregunta que le harías a la educadora tradicional sobre un relato de su comunidad.",
        "Relato: «Luz y el río». Lo cuenta: el curso (inventado). Pueblo: no corresponde. Territorio: no corresponde. Permiso: es del curso. Para qué: practicar la escucha. Pregunta: ¿qué relatos se pueden compartir?",
        ["completa las seis líneas", "no atribuye el relato a ningún pueblo", "formula una pregunta para el educador/a tradicional", "no inventa datos"],
        ["ficha oral escrita", "pregunta escrita o dicha en voz alta"],
        ["atribuir el relato a un pueblo", "inventar un permiso"],
        "Observa que distingue relato inventado de relato tradicional; si atribuyó el relato a un pueblo, explícale que fue inventado para practicar.",
    ),
    reinforce="Explica a un adulto cuáles son las cuatro preguntas para situar un relato.",
    extend="Inventa un relato de tres oraciones, escribe su ficha oral y marca «no corresponde» en pueblo y territorio.",
)

# =================================================================== LS01 clase 3 · reconocer palabras significativas
GUION_A = "Guion para que una persona adulta lea en voz alta (relato de práctica inventado, no es de ningún pueblo): «Luz vivía cerca de un río. Cada mañana saludaba a su vecina con un «mari mari». Una tarde llevó agua en un balde y su vecina le dijo «chaltumay». Al día siguiente Luz volvió a decir «mari mari» y las dos sonrieron.»"

L(
    LS1, 3,
    materials="Lápiz y hoja. Un adulto lee el guion en voz alta. El guion está escrito en este cuaderno y es inventado.",
    use="Aprenderé a reconocer, cuando escucho un relato, las palabras que tienen significado cultural. Sirve para entender mejor lo que se cuenta y para llevar la cuenta de cada palabra.",
    prior=["Sé situar un relato con una ficha oral.", "Sé que «mari mari» es un saludo y «chaltumay» es gracias."],
    explain=[
        "Una palabra significativa es una palabra que tiene un valor especial en el relato, como «mari mari» cuando alguien saluda. Cuando escucho, pongo atención a esas palabras y las anoto. Puedo hacer una marca cada vez que la oigo.",
        "Escuchar un relato exige otra técnica que leer. No puedo volver atrás con la vista. Por eso, mientras la persona lee, hago una tabla simple: una columna para la palabra y otra para cuántas veces la oí. Después reviso con la ficha qué significa cada una.",
        "No imito el sonido ni la dicción. Solo reconozco las palabras por lo que significan en el guion. Si alguna no la entiendo, pido que la lean de nuevo o la anoto como pregunta para el educador o la educadora tradicional.",
    ],
    vocab=[("palabra significativa", "palabra con valor especial en el relato"), ("guion", "texto escrito para que alguien lo lea en voz alta"), ("marca", "señal que hago para contar algo"), ("tabla", "lista en columnas para ordenar datos"), ("repetir", "volver a leer o decir algo")],
    worked=[
        W("Contar con marcas", GUION_A + " ¿Cuántas veces se dice «mari mari»?", ["Escucho y hago una marca cada vez.", "La primera vez: «saludaba… con un «mari mari»».", "La segunda: «volvió a decir «mari mari»». Son dos marcas."], "2"),
        W("Qué dice la ficha", FICHA_SAL + " En el guion, ¿qué quiere decir la palabra que dijo la vecina?", ["La vecina dijo «chaltumay».", "La ficha dice que es gracias.", "La vecina agradeció."], "gracias"),
    ],
    mistakes=[
        M("Contar solo una vez una palabra que se repite.", "Perdería la cuenta de cuántas veces aparece.", "Hago una marca por cada vez que la oigo."),
        M("Anotar una palabra que no se dijo porque me parece importante.", "Estaría inventando algo del relato.", "Anoto solo las que escucho."),
    ],
    R=[
        ex(GUION_A + " ¿Qué palabra dijo Luz cada mañana al saludar a su vecina?", "mari mari", "Lo dice la segunda oración."),
        ex("En el guion, ¿qué palabra dijo la vecina después de recibir el agua?", "chaltumay", "La vecina agradeció."),
        ex("En el guion, ¿cerca de qué lugar vivía Luz?", "cerca de un río", "Es lo que dice la primera oración."),
    ],
    C=[
        ex("En el guion, ¿cuántas veces se oye «mari mari»?", "2", "Una al saludar cada mañana y otra al día siguiente."),
        ex(FICHA_SAL + " En el guion, ¿por qué la vecina dijo «chaltumay»?", "porque recibió agua de Luz", "Le agradeció el agua."),
        ex("Verdadero o falso: en el guion Luz dijo «chaltumay».", "Falso", "Lo dijo la vecina y Luz dijo «mari mari»."),
    ],
    A=[
        ex("En el guion, ¿cuál de las dos expresiones se oye más veces: «mari mari» o «chaltumay»?", "mari mari", "«Mari mari» se oye dos veces y «chaltumay» una."),
        ex("Completa la tabla: palabra «mari mari», marcas: __. Palabra «chaltumay», marcas: __.", "2 y 1", "Una marca por cada vez que se oye."),
        ex("En el guion, ¿quién sonrió al final?", "las dos", "El guion dice «las dos sonrieron»."),
    ],
    Z=[
        ex("Un niño anotó que en el guion se dijo «antü». ¿Tiene razón? Sí o No.", "No", "El guion no menciona «antü»."),
        ex("Si no entiendo una palabra que oí, ¿qué hago: pido que la lean de nuevo o la invento?", "pido que la lean de nuevo", "No debo inventar."),
    ],
    D=[
        ex("Ordena los hechos del guion: A) la vecina agradeció. B) Luz llevó agua. C) Luz saludó cada mañana. D) Al día siguiente las dos sonrieron. Escribe las letras.", "C, B, A, D", "Es el orden en que se cuentan."),
        ex("Guion nuevo (inventado): «Tomás dijo «mari mari» a su profesora. Ella respondió «mari mari» y Tomás dijo «chaltumay». Ella sonrió.» ¿Cuántas veces se oye «mari mari»?", "2", "Una vez Tomás y otra vez la profesora."),
    ],
    context=[ex("Un adulto lee: «El director dijo «mari mari» y luego «chaltumay» a las familias». Con la ficha de saludos, ¿qué hizo el director primero?", "saludó", "«Mari mari» es un saludo.")],
    selfcheck=[
        ex("¿Qué hago cada vez que oigo una palabra significativa?", "hago una marca", "Así llevo la cuenta."),
        ex("¿Dónde veo qué quiere decir la palabra que oí?", "en la ficha", "La ficha da el significado."),
        ex("¿Puedo anotar una palabra que no oí?", "No", "Anoto solo lo que escucho."),
    ],
    task=T(
        "Pide a un adulto que lea en voz alta este relato de práctica inventado: «En la escuela, la profesora dijo «mari mari» a una visita. La visita respondió «mari mari». Después el curso dijo «chaltumay» y todos aplaudieron.» " + FICHA_SAL + " Mientras escuchas haz una tabla con dos columnas: palabra y marcas. Luego escribe qué significa cada palabra según la ficha y una pregunta para el educador o la educadora tradicional.",
        "mari mari: 2 marcas (saludo). chaltumay: 1 marca (gracias). Pregunta: ¿cuándo se usan estas palabras en su comunidad?",
        ["anota las dos palabras con sus marcas", "cuenta bien las veces", "escribe el significado según la ficha", "formula una pregunta para el educador/a tradicional"],
        ["tabla con marcas", "pregunta escrita o dicha en voz alta"],
        ["anotar una palabra que no se dijo", "inventar un significado"],
        "Comprueba el conteo: «mari mari» dos veces y «chaltumay» una. Si inventó un significado, pídele que use la ficha.",
    ),
    reinforce="Pide que te lean de nuevo el guion y confirma tus marcas.",
    extend="Escribe un guion de tres oraciones con dos expresiones de la ficha y pide a un adulto que lo lea para que tú las cuentes.",
)

# =================================================================== LS01 clase 4 · relacionar saberes sin generalizar
L(
    LS1, 4,
    materials="Lápiz y hoja. Los casos son inventados para practicar.",
    use="Aprenderé a relacionar lo que escucho con lo que sé yo y con lo que saben otras personas, sin decir que todas las personas de un pueblo piensan o hacen lo mismo. Sirve para evitar estereotipos.",
    prior=["Sé reconocer palabras significativas en un relato oral.", "Sé que cada persona decide qué cuenta de su vida."],
    explain=[
        "Relacionar saberes es unir lo que escucho con lo que yo sé y con lo que saben otras personas. Puedo decir: «Yo sé que el agua es necesaria» y «Mi compañera dice que le gusta escuchar relatos». Cada saber lo atribuyo a quien lo dijo.",
        "Generalizar es decir que todas las personas de un grupo son o hacen lo mismo. Una frase como «todas las personas de un pueblo hacen tal cosa» es una generalización. Es una mala idea porque cada pueblo y cada persona son distintos. Mejor digo: «en este relato de práctica…» o «según la educadora…».",
        "Para no generalizar uso palabras que limitan: «en este relato», «según esta persona», «en esta comunidad», «algunas personas». Y evito «todos», «siempre» y «nunca» cuando hablo de un pueblo. Si no sé, pregunto.",
    ],
    vocab=[("saber", "lo que una persona conoce"), ("generalizar", "decir que todos los de un grupo son o hacen lo mismo"), ("estereotipo", "idea fija y simple sobre un grupo"), ("limitar", "decir hasta dónde vale algo"), ("atribuir", "decir quién dijo o hizo algo")],
    worked=[
        W("Detectar una generalización", "Frases: 1) «En este relato de práctica, Luz saluda cada mañana». 2) «Todos los pueblos originarios saludan cada mañana». ¿Cuál generaliza?", ["La 1 habla de un relato.", "La 2 dice «todos los pueblos».", "La 2 generaliza."], "la 2"),
        W("Reescribir sin generalizar", "Reescribe «Las personas de un pueblo siempre dicen mari mari» para que no generalice.", ["Quito «siempre» y «las personas de un pueblo».", "Pongo la fuente: según la ficha.", "Escribo: según la ficha, «mari mari» es un saludo en mapuzugun."], "Según la ficha, «mari mari» es un saludo en mapuzugun."),
    ],
    mistakes=[
        M("Usar «todos» o «siempre» para hablar de un pueblo.", "Cada persona y cada comunidad es distinta.", "Uso «en este relato» o «según la educadora»."),
        M("Contar lo que sabe mi compañero como si lo hubiera dicho el pueblo entero.", "Es solo su saber.", "Digo «mi compañero dice»."),
    ],
    R=[
        ex("¿Cuál frase generaliza: «En este relato, Luz saluda» o «Todos los pueblos saludan igual»?", "«Todos los pueblos saludan igual»", "Habla de todos."),
        ex("La palabra «todos» al hablar de un pueblo, ¿limita o generaliza?", "generaliza", "Incluye a todas las personas."),
        ex("La frase «según la educadora» ¿limita o generaliza?", "limita", "Dice de quién es el dato."),
    ],
    C=[
        ex("Verdadero o falso: una idea fija y simple sobre un grupo se llama estereotipo.", "Verdadero", "Esa es su definición."),
        ex("Elige la frase que limita: A) «Siempre se hace así». B) «En este relato de práctica, se hace así».", "B", "La B dice hasta dónde vale."),
        ex("Lucía dice: «Yo sé que el agua es necesaria». ¿De quién es ese saber?", "de Lucía", "Lo atribuyo a quien lo dijo."),
    ],
    A=[
        ex("Reescribe para no generalizar: «Todos los pueblos originarios hacen lo mismo en las visitas». Elige: A) «Según la educadora, en su comunidad se saluda al llegar». B) «Todos saludan al llegar».", "A", "La A usa fuente y comunidad."),
        ex("Une cada saber con quien lo dijo. 1) «El agua es necesaria». 2) «Me gusta escuchar relatos». Dijeron: Lucía y Diego, respectivamente. ¿Quién dijo la 2?", "Diego", "Se atribuye en el orden dado."),
        ex("Marta dijo que quiere saber más sobre el río del relato. ¿Qué frase atribuye bien ese saber? A) «Marta quiere saber más sobre el río». B) «Todos queremos saber más sobre el río».", "A", "La A dice quién lo dijo; la B lo atribuye a todos."),
    ],
    Z=[
        ex("Camila dice: «Mi vecino es de un pueblo, así que sé todo sobre su pueblo». ¿Tiene razón? Sí o No.", "No", "Una persona no habla por todo su pueblo."),
        ex("Un compañero dice: «Todos los niños indígenas viven en el campo». ¿Es cierto o es un estereotipo?", "es un estereotipo", "Hay personas indígenas en muchos lugares, también en las ciudades."),
    ],
    D=[
        ex("Ordena para relacionar saberes: A) escucho el relato. B) digo lo que yo sé. C) digo lo que dice otra persona y lo atribuyo. Escribe las letras.", "A, B, C", "Escucho, aporto mi saber y luego atribuyo el de otros."),
        ex("Elige la mejor frase para el diario mural: A) «En el relato de práctica, Luz agradece con «chaltumay»; la ficha dice que es gracias». B) «Todos los pueblos agradecen con «chaltumay»».", "A", "La A usa fuente y limita."),
    ],
    context=[ex("En clase alguien dice: «Los pueblos originarios siempre hacen ceremonias». ¿Qué responde alguien que no generaliza: «No sé de todos, pero podemos preguntarle a la educadora» o «Sí, es verdad»?", "«No sé de todos, pero podemos preguntarle a la educadora»", "No afirma lo que no sabe.")],
    selfcheck=[
        ex("¿Qué palabras debo evitar al hablar de un pueblo: todos y siempre o en este relato?", "todos y siempre", "Esas palabras generalizan a todo un grupo."),
        ex("¿Cómo se llama una idea fija y simple sobre un grupo?", "estereotipo", "Ignora lo distintos que son."),
        ex("¿A quién atribuyo un saber que dice un compañero?", "a mi compañero", "Digo quién lo dijo."),
    ],
    task=T(
        "Lee este relato de práctica inventado: «Luz saludó a su vecina con un «mari mari». La vecina agradeció con un «chaltumay». Las dos se despidieron con una sonrisa.» " + FICHA_SAL + " Escribe tres frases: una que empiece con «Yo sé que…» (algo tuyo), una que empiece con «Según la ficha…» (con un dato de la ficha) y una que empiece con «En este relato de práctica…». Evita las palabras «todos», «siempre» y «nunca». Termina con una pregunta para la educadora tradicional.",
        "Yo sé que saludar con amabilidad hace sentir bien. Según la ficha, «chaltumay» es gracias en mapuzugun. En este relato de práctica, las dos se despiden con una sonrisa. Pregunta: ¿cómo se saluda en su comunidad?",
        ["escribe las tres frases pedidas", "no generaliza", "usa un dato de la ficha", "formula una pregunta para el educador/a tradicional"],
        ["tres frases escritas", "pregunta escrita o dicha en voz alta"],
        ["usar todos o siempre al hablar de un pueblo", "inventar un dato"],
        "Revisa que las frases limiten; si generalizó, conversa con el estudiante y reformulen con «en este relato» o «según la educadora».",
    ),
    reinforce="Cambia una frase que diga «todos hacen…» por otra que diga «en este caso…».",
    extend="Escribe una frase con «todos» sobre un grupo cualquiera, como los hinchas de un equipo, y cámbiala usando «algunas personas» o «según esta persona».",
)

# =================================================================== LS01 clase 5 · comunicar con atribución
L(
    LS1, 5,
    materials="Lápiz y hoja. Los casos son inventados. Nadie tiene que hablar de su familia ni de su pueblo.",
    use="Aprenderé a contar lo que aprendí diciendo de quién lo aprendí. Sirve para compartir saberes con respeto y para no mezclar lo que sé con lo que dijo otra persona.",
    prior=["Sé situar un relato y reconocer palabras significativas.", "Sé que no se generaliza sobre un pueblo."],
    explain=[
        "Comunicar lo aprendido es contarlo a otras personas con mis palabras. Para hacerlo bien tengo que atribuir: decir quién me lo enseñó. Puedo usar la frase: «Aprendí con… que…». Así reconozco a quien sabe.",
        "Una buena comunicación tiene tres partes. Lo que aprendí y de quién lo aprendí. Lo que yo pienso, que marco con «yo pienso que». Y lo que no sé o quiero preguntar, que marco con «quisiera saber». Así separo claramente lo que es dato de lo que es opinión.",
        "También cuido lo que no me corresponde contar. No cuento detalles que me pidieron guardar, ni hablo por una comunidad. Si dudo, digo: «eso lo explica la educadora tradicional».",
    ],
    vocab=[("comunicar", "contar algo a otras personas"), ("atribución", "decir quién enseñó o dijo algo"), ("opinión", "lo que yo pienso"), ("guardar", "no contar algo que me pidieron cuidar"), ("explicar", "decir con claridad algo")],
    worked=[
        W("Usar «aprendí con»", "Aprendiste con la educadora tradicional de la Escuela Ejemplo que «mari mari» es un saludo en mapuzugun. Escribe una frase de atribución.", ["Empiezo con «Aprendí con…».", "Nombro a la fuente: la educadora tradicional.", "Sigo con lo que aprendí."], "Aprendí con la educadora tradicional que «mari mari» es un saludo en mapuzugun."),
        W("Separar dato y opinión", "Frase: «Aprendí con la educadora que «chaltumay» es gracias. Yo pienso que es una palabra amable». ¿Cuál parte es opinión?", ["La primera parte dice «aprendí con».", "La segunda dice «yo pienso que».", "La opinión es la segunda parte."], "«yo pienso que es una palabra amable»"),
    ],
    mistakes=[
        M("Contar lo que aprendí sin decir de quién.", "Parece que lo inventé yo y la fuente queda olvidada.", "Uso «aprendí con…»."),
        M("Contar algo que me pidieron guardar.", "No me corresponde compartirlo.", "Digo «eso lo explica la educadora tradicional»."),
    ],
    R=[
        ex("¿Qué frase empieza una atribución: «Aprendí con…» o «Siempre se hace…»?", "«Aprendí con…»", "Nombra a quien me enseñó."),
        ex("En «Yo pienso que es amable», ¿qué marco: un dato o una opinión?", "una opinión", "«Yo pienso» marca mi idea."),
        ex("Si me pidieron guardar algo, ¿lo cuento o lo guardo?", "lo guardo", "No me corresponde compartirlo."),
    ],
    C=[
        ex("Elige la frase con atribución: A) «Aprendí con la educadora que «ko» es agua». B) ««Ko» es agua».", "A", "La A dice de quién aprendí."),
        ex("Verdadero o falso: puedo hablar en nombre de toda una comunidad después de una visita.", "Falso", "Solo cuento lo que escuché y de quién."),
        ex("En «Quisiera saber cuándo se dice «mari mari»», ¿qué expresa la frase: un dato o una pregunta?", "una pregunta", "«Quisiera saber» marca lo que no sé."),
    ],
    A=[
        ex("Une la parte con su marca. Partes: 1) lo que aprendí. 2) lo que pienso. 3) lo que quiero saber. Marcas: a) «yo pienso que», b) «quisiera saber», c) «aprendí con». Escribe 1-?, 2-?, 3-?", "1-c, 2-a, 3-b", "Cada parte tiene su marca."),
        ex("Ordena para formar una frase de atribución: la educadora / Aprendí con / que «chaltumay» es gracias.", "Aprendí con la educadora que «chaltumay» es gracias.", "Primero va «Aprendí con», luego la fuente y al final el dato."),
        ex("Tu exposición ya tiene «lo que aprendí» y «lo que pienso». ¿Qué parte falta?", "lo que quiero saber", "Son tres partes y esa es la que no está escrita."),
    ],
    Z=[
        ex("Diego cuenta: «Los pueblos hacen siempre lo mismo y yo lo aprendí solo». ¿Qué dos errores tiene: generalizar y no atribuir, o ser breve?", "generalizar y no atribuir", "Usa «siempre» y no nombra la fuente."),
        ex("¿Qué es mejor para una exposición: «según la ficha» o «me parece que alguien dijo»?", "«según la ficha»", "Es más claro quién dio el dato."),
    ],
    D=[
        ex("Ordena una exposición breve: A) lo que quisiera saber. B) lo que aprendí con atribución. C) lo que pienso. Escribe las letras.", "B, C, A", "Primero el dato, luego mi opinión y al final mi pregunta."),
        ex("Completa: «Aprendí con ____ que «mari mari» es un saludo». Opciones: la educadora de la Escuela Ejemplo o nadie en particular.", "la educadora de la Escuela Ejemplo", "Se nombra a la fuente."),
    ],
    context=[ex("Al cierre de la unidad cuentas lo aprendido a otro curso. ¿Qué frase usas para empezar: «Aprendí con la educadora que…» o «Todo el mundo sabe que…»?", "«Aprendí con la educadora que…»", "Nombra a la fuente.")],
    selfcheck=[
        ex("¿Cómo se llama decir quién me enseñó algo?", "atribución", "Es dar crédito a la fuente."),
        ex("¿Qué frase marca mi opinión?", "«yo pienso que»", "Separa mi idea del dato."),
        ex("¿Qué digo si no me corresponde contar algo?", "eso lo explica la educadora tradicional", "Remito a quien sabe."),
    ],
    task=T(
        "Prepara una exposición de 40 segundos para tu curso con estas tres partes: 1) «Aprendí con… que…» (usa la ficha: " + FICHA_SAL + "), 2) «Yo pienso que…» y 3) «Quisiera saber…». Escribe cada parte en una línea y practica leerla en voz alta. Al final escribe algo que no vas a contar porque no te corresponde, por ejemplo un detalle privado de otra persona.",
        "Aprendí con la ficha de la clase que «chaltumay» es gracias. Yo pienso que es una palabra amable. Quisiera saber cuándo se usa. No contaré: detalles privados de otras personas.",
        ["escribe las tres partes", "nombra a la fuente", "separa dato y opinión", "indica algo que no corresponde contar"],
        ["tres líneas escritas", "lectura en voz alta"],
        ["no atribuir", "generalizar sobre un pueblo"],
        "Comprueba que atribuya y que separe dato y opinión; si generalizó, ayúdalo a reescribir con «según la educadora».",
    ),
    reinforce="Lee en voz alta tus tres líneas y marca con colores las tres partes.",
    extend="Explica a un adulto, en tres oraciones, algo que aprendiste en esta unidad diciendo de quién lo aprendiste.",
)
