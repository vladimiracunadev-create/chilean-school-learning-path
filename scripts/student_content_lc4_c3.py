"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS02 (comunicación oral inicial de ideas y comentarios sobre la cosmovisión, con algunas palabras culturalmente
significativas) y OA LS03 (comprensión de textos breves con palabras o expresiones culturalmente significativas,
planteando y fundamentando opiniones).

Criterio de autoría: todos los textos, fichas, escuelas y personas son inventados solo para practicar y están rotulados
como tales; no se adapta ningún relato tradicional ni se describe ningún rito. Las únicas expresiones en lengua
indígena son saludos y palabras muy atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke). No se
inventa gramática, pronunciación ni significados rituales; nadie debe pronunciar la lengua si no quiere y la forma oral
la enseña el educador/a tradicional. Las ideas sobre cosmovisión se expresan como ideas ficticias de práctica, sin
atribuirlas a ningún pueblo. Cada tarea abierta remite al educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS2, LS3 = "LC04 OA LS02", "LC04 OA LS03"

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
SIT_A = "Situación A: contar en voz baja a una compañera lo que sentiste al escuchar a una visita."
SIT_B = "Situación B: hablar de la familia de otra persona de la sala frente a todo el curso."
SIT_C = "Situación C: conversar en grupo sobre una idea de un cuento inventado por el curso."
SIT_D = "Situación D: obligar a un compañero a pronunciar una palabra de la lengua indígena delante de todos."

L(
    LS2, 1,
    materials="Lápiz y hoja. Las situaciones están escritas aquí; son inventadas para practicar. Nadie tiene que hablar en voz alta si no quiere: puedes responder por escrito o con un dibujo.",
    use="Aprenderé a elegir una situación segura para expresar mis ideas y comentarios, a cuidar a quienes me escuchan y a decidir qué comparto. Sirve para conversar sobre cultura sin presionar a nadie.",
    prior=["Sé escuchar sin interrumpir.", "Sé que no se pregunta a nadie por su origen ni por su familia."],
    explain=[
        "Una situación de comunicación oral es un momento en que hablo y otras personas escuchan: un diálogo de a dos, una conversación en grupo o una exposición breve. Antes de hablar de cultura, elijo una situación segura. Es segura cuando nadie queda expuesto, nadie es presionado y se habla de ideas, no de datos privados.",
        "Para decidir hago tres preguntas. ¿Hablo de mis ideas o sentimientos, o de datos privados de otra persona? ¿Cada persona puede participar como prefiera, hablando, escribiendo o dibujando? ¿Pido que alguien hable en nombre de un pueblo o que pronuncie algo que no quiere? Si la respuesta a la última es sí, la situación no es segura.",
        "Hablar de cosmovisión es compartir ideas sobre cómo se entiende el mundo, como el cuidado del agua o el respeto a la tierra. En esta clase usamos ideas inventadas para practicar, sin atribuirlas a ningún pueblo. Para saber qué piensa un pueblo, escuchamos con respeto al educador o a la educadora tradicional, que representa esa tradición.",
    ],
    vocab=[("diálogo", "conversación entre dos o más personas"), ("exposición", "charla breve para explicar un tema"), ("situación segura", "momento en que nadie queda expuesto ni presionado"), ("cosmovisión", "manera en que un pueblo entiende el mundo"), ("presionar", "obligar a alguien a hacer algo que no quiere")],
    worked=[
        W("Elegir la situación segura", SIT_A + " " + SIT_B + " ¿Cuál es segura?", ["Pienso si alguien queda expuesto.", "En B se habla de la familia de otra persona.", "En A hablo de lo que sentí yo."], "A"),
        W("Detectar la presión", SIT_D + " ¿Es una situación segura? Sí o No.", ["Reviso si se obliga a alguien.", "Se obliga a un compañero a pronunciar delante de todos.", "Eso es presionar."], "No"),
    ],
    mistakes=[
        M("Pedirle a un compañero que hable en nombre de su pueblo.", "Nadie puede representar a todo un pueblo y puede sentirse expuesto.", "Conversamos sobre ideas de un cuento inventado o escuchamos al educador tradicional."),
        M("Creer que si no hablo en voz alta no participo.", "También se participa escuchando, escribiendo o dibujando.", "Elijo la forma en que me siento seguro."),
    ],
    R=[
        ex(SIT_A + " ¿Hablas de lo que sentiste tú o de datos privados de otra persona?", "de lo que sentí yo", "La situación A habla de tu propio sentir."),
        ex("Un diálogo, ¿es una conversación entre dos o más personas o una lectura en silencio?", "una conversación entre dos o más personas", "Diálogo significa conversar."),
        ex("Si no quiero hablar en voz alta, ¿puedo participar escribiendo o dibujando? Sí o No.", "Sí", "Hay varias formas de participar."),
    ],
    C=[
        ex(SIT_B + " ¿Es segura? Sí o No.", "No", "Habla de datos de la familia de otra persona."),
        ex(SIT_C + " ¿Se habla de ideas o de datos privados?", "de ideas", "El cuento es inventado por el curso."),
        ex("Verdadero o falso: puedo pedir a un compañero que hable por todo su pueblo y explique lo que piensa.", "Falso", "Nadie debe hablar en nombre de todo un pueblo."),
    ],
    A=[
        ex("Cuatro situaciones: A, B, C y D de esta clase. ¿Cuáles son seguras? Escribe las letras.", "A y C", "B expone a una familia y D presiona a un compañero."),
        ex("Un niño dice: «Quiero hablar sobre la idea de cuidar el agua en un cuento inventado». ¿Es una situación segura? Sí o No.", "Sí", "Habla de una idea y de un cuento inventado."),
        ex("De las cuatro situaciones A, B, C y D de esta clase, ¿cuántas dejan a alguien expuesto o presionado?", "2", "B expone a una familia y D presiona a un compañero."),
    ],
    Z=[
        ex("Una niña dice: «Si es una actividad del colegio, todos deben hablar delante de todos». ¿Tiene razón? Sí o No.", "No", "Cada persona puede participar como prefiera."),
        ex("Un profesor propone que quien quiera lea su idea, quien prefiera la escriba y quien lo desee la dibuje. ¿Esa situación es más segura que obligar a todos a hablar? Sí o No.", "Sí", "Respeta distintas formas de participar."),
    ],
    D=[
        ex("Ordena los pasos para preparar una conversación segura: A) elijo una idea que no sea privada. B) decido cómo participaré. C) escucho con respeto a los demás. Escribe las letras.", "A, B, C", "Primero la idea, luego la forma y al final la escucha."),
        arith("En un curso de 28 estudiantes, 9 prefieren escribir y 4 prefieren dibujar. ¿Cuántos no prefieren ni escribir ni dibujar?", "28-9-4", "Se restan los que prefieren escribir y dibujar."),
    ],
    context=[ex("En una conversación del curso alguien dice: «Que cuente algo de su familia indígena el que sea de un pueblo». ¿Propones «Hablemos de una idea de un cuento inventado» o «Que levanten la mano»?", "«Hablemos de una idea de un cuento inventado»", "No se pide datos privados ni se expone a nadie.")],
    selfcheck=[
        ex("¿Qué es una situación segura?", "un momento en que nadie queda expuesto ni presionado", "Cuida a todos."),
        ex("¿Puedo participar solo escuchando? Sí o No.", "Sí", "Escuchar es participar."),
        ex("¿Debo hablar en nombre de un pueblo? Sí o No.", "No", "Nadie representa a todo un pueblo."),
    ],
    task=T(
        "Lee estas cuatro situaciones inventadas para practicar. " + SIT_A + " " + SIT_B + " " + SIT_C + " " + SIT_D + " En tu cuaderno escribe: 1) las letras de las situaciones seguras y por qué, 2) cómo participarías tú (hablando, escribiendo o dibujando), 3) una idea de cuidado de la naturaleza para conversar en una situación segura. Termina con una pregunta para el educador o la educadora tradicional.",
        "Seguras: A y C, porque nadie queda expuesto. Participaría escribiendo. Idea: cuidar el agua cuando nos lavamos las manos. Pregunta: ¿cómo cuidan el agua en su comunidad?",
        ["identifica las situaciones seguras", "explica por qué las otras no lo son", "elige cómo participar", "formula una pregunta para el educador/a tradicional"],
        ["tres respuestas escritas", "pregunta escrita o dicha en voz alta"],
        ["pedir que alguien hable por su pueblo", "elegir una situación que presiona a alguien"],
        "Observa que cuide la privacidad y la elección de cada persona; si propuso presionar a alguien, conversa por qué participar es una decisión.",
    ),
    reinforce="Escribe dos situaciones en que conversarías con comodidad y una en que no te sentirías seguro.",
    extend="Explica con tus palabras por qué nadie puede hablar en nombre de todo un pueblo.",
)

# =================================================================== LS02 clase 2 · escuchar palabras y significado
DIALOGO_A = "Diálogo de práctica A (inventado): —Mari mari, buenos días —dijo la visita. —Mari mari —respondió el curso. —Chaltumay por recibirnos —agregó la visita."

L(
    LS2, 2,
    materials="Lápiz y hoja. El diálogo y las fichas están escritos aquí; son inventados para practicar. Nadie está obligado a decir ninguna palabra en voz alta.",
    use="Aprenderé a escuchar un diálogo con palabras de otra lengua, a reconocer qué significan con una ficha y a decir lo que entendí con mis palabras. Sirve para participar con respeto cuando se usan palabras en lengua indígena.",
    prior=["Sé elegir una situación segura para conversar.", "Sé usar una ficha para saber el significado de una palabra."],
    explain=[
        "Escuchar bien es poner atención a quién habla, a qué dice y a cómo lo dice, sin interrumpir. Cuando oigo una palabra en lengua indígena, no trato de adivinar su pronunciación ni su significado. Escucho cómo la dice quien la sabe y la relaciono con la ficha, que me dice qué significa.",
        "En el diálogo de práctica, «mari mari» es un saludo y «chaltumay» quiere decir «gracias» según la ficha. Para entender un diálogo respondo tres preguntas: ¿quién habla?, ¿qué dice? y ¿para qué lo dice? Así sé que la visita saluda y luego agradece, y que el curso responde con el saludo.",
        "Nadie tiene que repetir la palabra en voz alta para aprenderla. Puedo escucharla varias veces, escribirla de la ficha o repetirla en silencio. Si quiero decirla en voz alta, lo hago con calma y le pido al educador o a la educadora tradicional que me enseñe cómo se dice, porque la pronunciación la enseña quien conoce la lengua.",
    ],
    vocab=[("escuchar", "poner atención a lo que otra persona dice"), ("saludo", "palabra o gesto con que se recibe a alguien"), ("agradecer", "decir gracias"), ("pronunciación", "manera de decir una palabra en voz alta"), ("responder", "contestar a lo que otro dijo")],
    worked=[
        W("Entender un diálogo", DIALOGO_A + " " + FICHA_SAL + " ¿Qué hace la visita al final?", ["Busco la última frase de la visita: «Chaltumay por recibirnos».", "La ficha dice que chaltumay es gracias.", "La visita agradece."], "agradece al curso"),
        W("Quién dice qué", DIALOGO_A + " ¿Quién responde «mari mari»?", ["Leo las intervenciones en orden.", "Primero la visita saluda.", "Después responde el curso."], "el curso"),
    ],
    mistakes=[
        M("Inventar cómo se pronuncia una palabra que escuché.", "Solo quien conoce la lengua enseña su pronunciación.", "Pido al educador tradicional que me enseñe cómo se dice."),
        M("Creer que debo repetir la palabra en voz alta para demostrar que aprendí.", "Se puede aprender escuchando y escribiendo.", "Participo escuchando y repitiendo solo si quiero."),
    ],
    R=[
        ex(DIALOGO_A + " ¿Quién dice primero «mari mari»?", "la visita", "Lo dice en la primera frase."),
        ex(FICHA_SAL + " Según la ficha, ¿«mari mari» es un saludo o una despedida?", "un saludo", "La ficha lo dice."),
        ex("Para aprender una palabra, ¿puedo escucharla y escribirla sin decirla en voz alta? Sí o No.", "Sí", "Aprender no obliga a hablar en voz alta."),
    ],
    C=[
        ex(DIALOGO_A + " ¿Cuántas personas o grupos hablan en el diálogo?", "2", "Hablan la visita y el curso."),
        ex("Verdadero o falso: puedo inventar la pronunciación de una palabra que oí si me suena parecida a otra.", "Falso", "La pronunciación la enseña quien conoce la lengua."),
        ex(DIALOGO_A + " ¿Para qué dice la visita «chaltumay»: para agradecer o para pedir ayuda?", "para agradecer", "La ficha dice que significa gracias."),
    ],
    A=[
        ex(DIALOGO_A + " ¿Cuántas veces aparece la expresión «mari mari»?", "2", "La dicen la visita y el curso."),
        ex("Une cada frase con su propósito. Frases: 1) «Mari mari, buenos días». 2) «Chaltumay por recibirnos». Propósitos: a) agradecer. b) saludar. Escribe las parejas.", "1-b, 2-a", "La primera saluda y la segunda agradece."),
        ex("Una niña no quiere repetir en voz alta «chaltumay». ¿Cómo puede participar: A) escribiéndola de la ficha y escuchando. B) obligándose a hablar?", "A", "Hay otras formas de participar."),
    ],
    Z=[
        ex("Un niño dice: «Si no pronuncio «mari mari» igual que la visita, no aprendí». ¿Tiene razón? Sí o No.", "No", "Aprender también es escuchar y entender el sentido."),
        ex("Dos formas de aprender una pronunciación: A) pedirle a la educadora tradicional que la enseñe. B) adivinarla con lo que parece. ¿Cuál es más respetuosa?", "A", "Quien conoce la lengua la enseña."),
    ],
    D=[
        ex("Ordena para entender un diálogo: A) pregunto para qué lo dijo. B) escucho quién habla. C) leo qué dice con ayuda de la ficha. Escribe las letras.", "B, C, A", "Primero quién, luego qué y al final para qué."),
        ex(DIALOGO_A + " Si el curso respondiera «chaltumay» a la visita, ¿cambiaría el sentido de su respuesta: de saludar a agradecer? Sí o No.", "Sí", "«Mari mari» saluda y «chaltumay» agradece."),
    ],
    context=[ex("Una visita te saluda con «mari mari». Tú no quieres decirlo en voz alta. ¿Qué haces: respondes con una sonrisa y escuchas, o te vas?", "respondes con una sonrisa y escuchas", "Se puede responder sin hablar.")],
    selfcheck=[
        ex("¿Dónde veo qué significa una palabra en lengua indígena en estas clases: en la ficha o en mi memoria?", "en la ficha", "La ficha da el significado."),
        ex("¿Debo repetir una palabra en voz alta si no quiero? Sí o No.", "No", "Nadie está obligado."),
        ex("¿Quién enseña la pronunciación: el educador tradicional o mi imaginación?", "el educador tradicional", "Es quien conoce la lengua."),
    ],
    task=T(
        "Lee este diálogo inventado para practicar y su ficha. " + DIALOGO_A + " " + FICHA_SAL + " En tu cuaderno escribe: 1) quién habla en cada línea, 2) lo que significa cada expresión según la ficha, 3) con tus palabras, qué pasó en el diálogo en una oración. No es necesario que digas las palabras en voz alta. Termina con una pregunta para el educador o la educadora tradicional sobre cómo se dice una de ellas.",
        "Habla la visita, responde el curso, la visita vuelve a hablar. «Mari mari» es saludo, «chaltumay» es gracias. La visita saludó y agradeció, y el curso respondió el saludo. Pregunta: ¿cómo se dice «chaltumay»?",
        ["identifica quién habla", "usa la ficha para el significado", "resume con sus palabras", "formula una pregunta para el educador/a tradicional"],
        ["tres respuestas escritas", "pregunta escrita o dicha en voz alta"],
        ["inventar la pronunciación", "decir un significado que la ficha no trae"],
        "Comprueba que el significado venga de la ficha; si inventó una pronunciación, pídele que la cambie por una pregunta al educador tradicional.",
    ),
    reinforce="Relee el diálogo A en silencio y subraya con un color quién saluda y con otro quién agradece.",
    extend="Inventa un diálogo de cuatro líneas que use «mari mari» y «chaltumay» y escribe quién habla en cada una.",
)

# =================================================================== LS02 clase 3 · preparar una idea o sentimiento ficticio
IDEA_A = "Idea ficticia de práctica: «Creo que el agua es importante porque todos la necesitamos. Siento tranquilidad cuando veo el agua limpia.»"

L(
    LS2, 3,
    materials="Lápiz y hoja. Las ideas y los cuadros están escritos aquí; son inventados para practicar. Las ideas son del curso, no de ningún pueblo.",
    use="Aprenderé a preparar una idea y un sentimiento sobre un tema de la cosmovisión, como el cuidado del agua, para comentarlos en una conversación. Sirve para hablar con orden y sin hablar por un pueblo.",
    prior=["Sé que nadie habla en nombre de un pueblo.", "Sé escuchar un diálogo y entender qué significan las palabras de una ficha."],
    explain=[
        "Una idea es lo que pienso sobre algo, y se dice con una razón. «El agua es importante porque todos la necesitamos» es una idea con su porque. Un sentimiento es lo que siento: tranquilidad, alegría, respeto o curiosidad. Puedo decir primero la idea y después el sentimiento, o al revés.",
        "Para preparar una idea sigo cuatro pasos. Elijo un tema, como el agua, el sol o la tierra. Escribo mi idea con una razón. Escribo qué siento. Y escojo una palabra de la ficha, como «ko» (agua), para incluirla con respeto. No invento frases en la lengua: la palabra va dentro de una oración en castellano.",
        "Mi idea o mi sentimiento son míos. No digo «mi pueblo piensa» ni «los indígenas sienten». Digo «yo pienso» o «yo siento». Y para una conversación uso frases cortas, miro a quienes escuchan y dejo que otros respondan. Preparar es practicar en silencio, en papel o frente a una persona de confianza.",
    ],
    vocab=[("idea", "lo que pienso, dicho con una razón"), ("sentimiento", "lo que siento, como alegría o respeto"), ("razón", "motivo que explica por qué pienso algo"), ("tema", "asunto del que se habla"), ("ficticio", "inventado para practicar")],
    worked=[
        W("Separar idea y sentimiento", IDEA_A + " ¿Qué parte es la idea y cuál es el sentimiento?", ["La primera oración da una razón: es la idea.", "La segunda dice cómo se siente: tranquilidad.", "Separo las dos partes."], "idea: el agua es importante porque todos la necesitamos; sentimiento: tranquilidad"),
        W("Incluir una palabra de la ficha", FICHA_PAL + " Escribe una oración con la palabra «antü» y una razón.", ["Elijo el tema: el sol.", "Uso la palabra de la ficha: antü (sol).", "Agrego una razón."], "El sol (antü) es importante porque nos da luz."),
    ],
    mistakes=[
        M("Decir «los indígenas sienten tranquilidad con el agua» después de leer una sola idea.", "No puedo hablar por un pueblo.", "Digo «yo siento tranquilidad»."),
        M("Inventar una frase en lengua indígena para que mi idea suene más cultural.", "Estaría inventando lengua.", "Pongo la palabra de la ficha dentro de una oración en castellano."),
    ],
    R=[
        ex(IDEA_A + " ¿Qué siente la persona del texto?", "tranquilidad", "Lo dice la segunda oración."),
        ex("Una razón de una idea, ¿empieza con «porque» o con «pero»?", "con «porque»", "«Porque» explica el motivo."),
        ex("En mi idea, ¿digo «yo pienso» o «los indígenas piensan»?", "«yo pienso»", "La idea es mía."),
    ],
    C=[
        ex("Verdadero o falso: un sentimiento es lo que siento, como alegría o respeto.", "Verdadero", "Eso es un sentimiento."),
        ex(FICHA_PAL + " ¿Qué palabra de la ficha usarías en una oración sobre la luna?", "kuyen", "La ficha dice que «kuyen» es luna."),
        ex("De estas dos oraciones, ¿cuál tiene una razón? A) «El sol es lindo». B) «El sol es importante porque da luz».", "B", "La B explica con «porque»."),
    ],
    A=[
        ex("Ordena para armar una idea: A) escribo qué siento. B) elijo el tema. C) escribo mi idea con una razón. Escribe las letras.", "B, C, A", "Tema, idea con razón y sentimiento."),
        ex(FICHA_PAL + " Completa con la palabra de la ficha: «La tierra (____) es importante porque en ella crecen las plantas». Elige entre mapu y ko.", "mapu", "«Mapu» es tierra y en ella crecen las plantas."),
        ex("Cuenta las partes de un comentario preparado: tema, idea con razón, sentimiento y palabra de la ficha. ¿Cuántas partes son?", "4", "Son cuatro partes."),
    ],
    Z=[
        ex("Una niña prepara: «Mi pueblo piensa que el agua es importante», sin haberlo conversado con nadie de su comunidad. ¿Qué debe cambiar: «Mi pueblo piensa» por «Yo pienso» o la palabra «agua»?", "«Mi pueblo piensa» por «Yo pienso»", "No puede hablar por un pueblo."),
        ex("Dos comentarios: A) «Yo siento respeto cuando veo el agua limpia». B) «Todos los pueblos sienten respeto por el agua». ¿Cuál es más honesto?", "A", "Habla solo de lo que siente quien lo dice."),
    ],
    D=[
        ex("¿Cuál oración incluye la palabra «ko» y una razón? A) «El ko es bonito.» B) «Hay que cuidar el agua (ko) porque todos la necesitamos.»", "B", "Solo la B trae «ko» con su significado y una razón con «porque»."),
        arith("Un comentario tiene 4 partes y ya escribiste 3. ¿Cuántas faltan?", "4-3", "Se restan las partes ya escritas."),
    ],
    context=[ex("En una conversación del curso te piden comentar la idea de cuidar el agua. Tienes preparado «Yo pienso que el agua (ko) se cuida porque todos la necesitamos». ¿Es adecuada para decirla en voz alta? Sí o No.", "Sí", "Habla desde ti, tiene razón y usa la palabra con respeto.")],
    selfcheck=[
        ex("¿Qué es una razón: lo que explica por qué pienso algo o un dibujo?", "lo que explica por qué pienso algo", "La razón sostiene mi idea."),
        ex("¿Puedo inventar una frase en lengua indígena para mi comentario? Sí o No.", "No", "Solo uso palabras de la ficha."),
        ex("¿Hablo por mí o por todo un pueblo en mi comentario?", "por mí", "Mi idea es mía."),
    ],
    task=T(
        "Prepara en tu cuaderno un comentario corto para una conversación sobre el cuidado del agua. " + FICHA_PAL + " Escribe: 1) una idea con razón que empiece con «Yo pienso que…», 2) un sentimiento que empiece con «Yo siento…», 3) la palabra «ko» dentro de una oración en castellano. Léelo en silencio, luego a una persona de confianza. Termina con una pregunta para el educador o la educadora tradicional sobre el agua.",
        "Yo pienso que el agua (ko) se cuida porque todos la necesitamos. Yo siento tranquilidad cuando el agua está limpia. Pregunta: ¿cómo cuida el agua su comunidad?",
        ["escribe idea con razón", "escribe un sentimiento propio", "incluye una palabra de la ficha en castellano", "formula una pregunta para el educador/a tradicional"],
        ["comentario de tres partes", "pregunta escrita o dicha en voz alta"],
        ["hablar en nombre de un pueblo", "inventar una frase en lengua indígena"],
        "Verifica que hable en primera persona y use solo palabras de la ficha; si habló por un pueblo, ayúdalo a cambiar a «yo pienso».",
    ),
    reinforce="Lee en voz baja tu comentario dos veces y marca con una línea la razón.",
    extend="Prepara un segundo comentario sobre el sol (antü) con una idea, una razón y un sentimiento.",
)

# =================================================================== LS02 clase 4 · dialogar con apoyo
APOYO = "Marco de apoyo (inventado): «Yo pienso que… porque…». «Yo siento…». «¿Tú qué piensas?». «Gracias por escuchar»."

L(
    LS2, 4,
    materials="Lápiz y hoja. El marco de apoyo está escrito aquí. Puedes dialogar de a dos, por escrito o con una persona de confianza.",
    use="Aprenderé a dialogar sobre una idea o un sentimiento con ayuda de frases de apoyo: hablar, escuchar, responder y agradecer. Sirve para conversar con respeto y sin presionar a nadie.",
    prior=["Sé preparar una idea con razón y un sentimiento.", "Sé que nadie habla en nombre de un pueblo."],
    explain=[
        "Dialogar es conversar por turnos. Una persona habla, la otra escucha y luego responde. Un buen diálogo tiene cuatro momentos: saludar, decir mi idea con una razón, escuchar la de la otra persona y despedirme agradeciendo. Puedo usar frases de apoyo para no quedarme en blanco.",
        "El marco de apoyo trae frases como «Yo pienso que… porque…», «Yo siento…», «¿Tú qué piensas?» y «Gracias por escuchar». Las uso para empezar, preguntar y cerrar. Si quiero incluir una palabra de la lengua, uso una de la ficha, como «mari mari» al saludar o «chaltumay» al agradecer, solo si me siento cómodo y entendiendo lo que significan.",
        "En un diálogo respetuoso no interrumpo, no me burlo, no corrijo la manera de hablar de nadie y acepto que otro piense distinto. Si no entiendo algo, pregunto. Si algo es una duda cultural que ninguno sabemos, la anotamos para preguntarla al educador o a la educadora tradicional, en lugar de inventar una respuesta.",
    ],
    vocab=[("turno", "momento que le toca hablar a cada persona"), ("diálogo", "conversación por turnos"), ("apoyo", "ayuda para empezar o seguir"), ("acordar", "ponerse de acuerdo"), ("duda", "algo que no sé y quiero preguntar")],
    worked=[
        W("Ordenar un diálogo", "Cuatro momentos desordenados: a) escucho su idea. b) saludo. c) agradezco. d) digo mi idea con razón. ¿Cuál es el orden?", ["Primero saludo.", "Luego digo mi idea y escucho la de otra persona.", "Al final agradezco."], "b, d, a, c"),
        W("Responder con respeto", "Una compañera dijo: «Yo pienso que el sol es importante porque da luz». Tú piensas que también es importante por el calor. ¿Qué respondes?", ["Escucho su idea completa.", "Uso el marco de apoyo.", "Agrego mi idea sin criticar la suya."], "«Yo también pienso que el sol es importante, además porque nos da calor.»"),
    ],
    mistakes=[
        M("Corregir cómo habla mi compañero.", "El diálogo es para compartir ideas, no para juzgar cómo habla.", "Escucho la idea y respondo a lo que dice."),
        M("Responder una duda cultural inventando una respuesta.", "Puedo equivocarme y faltar el respeto.", "Anoto la duda y la pregunto al educador tradicional."),
    ],
    R=[
        ex(APOYO + " ¿Qué frase del marco usas para preguntar a la otra persona?", "«¿Tú qué piensas?»", "Es la que invita a responder."),
        ex("En un diálogo, ¿hablan por turnos o todos a la vez?", "por turnos", "Dialogar es conversar por turnos."),
        ex("Al terminar un diálogo, ¿qué digo para cerrar con respeto: «gracias por escuchar» o «no me importa»?", "«gracias por escuchar»", "Cierra con respeto."),
    ],
    C=[
        ex("Verdadero o falso: en un diálogo puedo burlarme de cómo habla alguien.", "Falso", "Hay que respetar a quien habla."),
        ex("Si en el diálogo surge una duda cultural que nadie sabe, ¿qué hacemos: la anotamos y preguntamos al educador tradicional o inventamos una respuesta?", "la anotamos y preguntamos al educador tradicional", "No se inventa."),
        ex(APOYO + " ¿Qué frase del marco usas para decir lo que sientes?", "«Yo siento…»", "Esa frase introduce el sentimiento."),
    ],
    A=[
        ex("Ordena estas tres frases de un diálogo: A) «Gracias por escuchar». B) «Mari mari». C) «¿Tú qué piensas?». Escribe las letras en el orden en que las dirías.", "B, C, A", "Saludo, pregunto y agradezco al final."),
        ex("Tu compañera dice: «Yo pienso que la luna es bonita porque brilla de noche». Tú piensas lo mismo. ¿Qué respuesta usa el marco de apoyo? A) «Yo también pienso que la luna es bonita porque brilla de noche». B) «Eso no importa».", "A", "La A responde a su idea con tu opinión y una razón."),
        ex("Un niño dice «mari mari» al saludar y la visita responde igual. ¿Qué momento del diálogo cumplió: saludar o agradecer?", "saludar", "«Mari mari» es un saludo según la ficha."),
    ],
    Z=[
        ex("Una niña dice: «Si mi compañero piensa distinto, tiene que estar equivocado». ¿Tiene razón? Sí o No.", "No", "Se puede pensar distinto con respeto."),
        ex("Dos respuestas a una compañera que dice «Yo siento alegría cuando llueve»: A) «No es cierto». B) «Yo siento tranquilidad cuando llueve. ¿Por qué sientes alegría?». ¿Cuál mantiene el diálogo respetuoso?", "B", "Comparte y pregunta sin negar."),
    ],
    D=[
        ex("Ordena este diálogo de práctica con tres turnos: A) «Yo siento tranquilidad». B) «¿Tú qué piensas?». C) «Yo pienso que el agua se cuida porque todos la necesitamos». Escribe las letras empezando por la idea y terminando con la pregunta.", "C, A, B", "Idea, sentimiento y pregunta."),
        arith("Un diálogo de práctica tiene 4 momentos y cada uno dura 2 minutos. ¿Cuántos minutos dura el diálogo?", "4*2", "Se multiplican los momentos por los minutos de cada uno."),
    ],
    context=[ex("Dialogas con un compañero sobre cuidar el agua. Él dice una idea que no entiendes. ¿Le preguntas «¿Puedes explicarlo de otra forma?» o te quedas callado y finges entender?", "le preguntas «¿Puedes explicarlo de otra forma?»", "Preguntar ayuda a entender y respeta al otro.")],
    selfcheck=[
        ex("¿Cuántos momentos tiene el diálogo del marco: saludar, hablar, escuchar y agradecer?", "4", "Se cuentan cuatro momentos."),
        ex("Si una compañera piensa distinto, ¿la corrijo o la escucho?", "la escucho", "Aceptar ideas distintas es respeto."),
        ex("¿Qué hago ante una duda cultural: pregunto al educador tradicional o invento?", "pregunto al educador tradicional", "No se inventa."),
    ],
    task=T(
        "Escribe en tu cuaderno un diálogo de práctica de seis líneas entre dos personas inventadas, con esta ayuda. " + APOYO + " " + FICHA_SAL + " Debe tener: un saludo (puedes usar «mari mari»), una idea con razón, un sentimiento, una pregunta, una respuesta respetuosa y un agradecimiento (puedes usar «chaltumay»). Ensáyalo con una persona de confianza o léelo en silencio. Termina con una pregunta para el educador o la educadora tradicional.",
        "—Mari mari. —Mari mari. —Yo pienso que el agua se cuida porque todos la necesitamos. Yo siento tranquilidad. ¿Tú qué piensas? —Yo también pienso lo mismo, y siento respeto. —Chaltumay por escuchar. Pregunta: ¿cómo se saluda en su comunidad?",
        ["incluye saludo, idea con razón, sentimiento, pregunta y agradecimiento", "usa solo las palabras de la ficha en lengua indígena", "responde con respeto", "formula una pregunta para el educador/a tradicional"],
        ["diálogo de seis líneas", "pregunta escrita o dicha en voz alta"],
        ["inventar frases en lengua indígena", "corregir al otro"],
        "Comprueba que estén los momentos del diálogo y que no corrija a la otra persona; si inventó frases en la lengua, pide cambiarlas por una pregunta.",
    ),
    reinforce="Con una persona de confianza practica las frases «Yo pienso que… porque…» y «¿Tú qué piensas?».",
    extend="Escribe un diálogo de práctica donde las dos personas piensan distinto y se escuchan con respeto.",
)

# =================================================================== LS03 clase 1 · identificar procedencia
TXT_P = "Texto de práctica A (inventado): «Visita a la Escuela Ejemplo. Una educadora tradicional vino a la sala y escribió «ruka» en la pizarra. Dijo que es la casa mapuche. Después los niños dibujaron una ruka y escribieron «ruka» debajo.»"
FICHA_TXT = "Ficha del texto A (inventada): Título: «Visita a la Escuela Ejemplo». Lo escribió: el curso de la escuela. Fuente de las palabras: la educadora tradicional de la escuela. Permiso: sí, para usar dentro de la sala. Para qué: contar la visita."

L(
    LS3, 1,
    materials="Lápiz y hoja. Los textos y las fichas están escritos aquí; son inventados para practicar y no pertenecen a ninguna escuela ni persona real.",
    use="Aprenderé a identificar la procedencia de un texto breve antes de leerlo: quién lo escribió, de dónde vienen sus palabras y si hay permiso. Sirve para leer con respeto textos que traen palabras de una lengua indígena.",
    prior=["Sé reconocer el título, la imagen y el tema de un texto.", "Sé que las palabras de la lengua indígena las enseña el educador o la educadora tradicional."],
    explain=[
        "La procedencia de un texto es de dónde viene: quién lo escribió, cuándo, para qué y de quién son las palabras que contiene. Antes de leer un texto con palabras en lengua indígena miro su ficha. La ficha me dice la fuente, que es la persona que enseñó las palabras, y el permiso, que es el sí para usarlas.",
        "Para identificar la procedencia busco cinco datos: el título, quién lo escribió, la fuente de las palabras, el permiso y el propósito, es decir, para qué se escribió. Si falta alguno, escribo «no se indica». Un texto con datos que faltan puede leerse, pero no copio ni uso sus palabras hasta tener respuestas.",
        "La procedencia ayuda a leer mejor. Si el texto lo escribió un curso, sé que es una actividad escolar. Si la fuente es una educadora tradicional, sé que las palabras vienen de quien las enseña. Así no confundo el texto con un relato tradicional ni lo atribuyo a un pueblo equivocado. Y si dudo, pregunto.",
    ],
    vocab=[("procedencia", "lugar, persona o grupo de donde viene un texto"), ("fuente", "persona que enseñó las palabras"), ("permiso", "el sí para usar unas palabras"), ("propósito", "para qué se escribió un texto"), ("ficha", "papel con los datos de un texto")],
    worked=[
        W("Leer la ficha de un texto", FICHA_TXT + " ¿Quién enseñó las palabras?", ["Busco la línea «Fuente de las palabras».", "Dice: la educadora tradicional de la escuela.", "Ella las enseñó."], "la educadora tradicional de la escuela"),
        W("Datos que faltan", "Ficha B (inventada): Título: «Una palabra». Lo escribió: no se indica. Fuente: no se indica. Permiso: no se indica. Para qué: no se indica. ¿Cuántos datos faltan?", ["Cuento las líneas con «no se indica».", "Son cuatro."], "4"),
    ],
    mistakes=[
        M("Leer un texto con palabras en lengua indígena sin mirar su ficha.", "No sé quién enseñó las palabras ni si hay permiso.", "Miro primero la ficha."),
        M("Decir que un texto es un relato tradicional porque tiene una palabra en lengua indígena.", "Un texto escolar puede usar palabras sin ser un relato tradicional.", "Leo en la ficha qué tipo de texto es."),
    ],
    R=[
        ex(FICHA_TXT + " ¿Quién escribió el texto A?", "el curso de la escuela", "Lo dice la ficha."),
        ex(TXT_P + " ¿Qué palabra escribió la educadora en la pizarra?", "ruka", "El texto la nombra entre comillas."),
        ex("La procedencia de un texto, ¿dice de dónde viene o cuántas palabras tiene?", "de dónde viene", "Es su origen."),
    ],
    C=[
        ex(FICHA_TXT + " ¿Para qué se escribió el texto A?", "para contar la visita", "El propósito está en la última línea."),
        ex("Verdadero o falso: puedo usar las palabras de un texto aunque su ficha diga «permiso: no se indica».", "Falso", "Sin permiso no las uso."),
        ex(FICHA_TXT + " ¿Hasta dónde llega el permiso: dentro de la sala o en cualquier lugar?", "dentro de la sala", "La ficha lo limita."),
    ],
    A=[
        ex("Cinco datos de procedencia: título, quién lo escribió, fuente, permiso y propósito. En la ficha B faltan todos menos el título. ¿Cuántos faltan?", "4", "5 − 1 = 4."),
        ex(TXT_P + " " + FICHA_TXT + " ¿Qué hicieron los niños con la palabra «ruka»?", "la dibujaron y la escribieron debajo", "Lo dice la última oración."),
        ex("Un texto dice «Escrito por el curso». Otro dice «Escrito por una persona anónima de una pantalla». ¿Cuál tiene mejor procedencia?", "el primero", "Se sabe quién lo escribió."),
    ],
    Z=[
        ex("Un niño dice: «Si un texto tiene una palabra indígena, es un relato tradicional». ¿Tiene razón? Sí o No.", "No", "Hay textos escolares con palabras de la lengua."),
        ex("El texto A tiene permiso «dentro de la sala». ¿Puedes copiar sus palabras en un cartel para la calle? Sí o No.", "No", "El permiso es solo para la sala."),
    ],
    D=[
        ex("Ordena para identificar la procedencia: A) leo el permiso. B) miro el título. C) leo quién lo escribió y la fuente. Escribe las letras en el orden de la ficha del texto A.", "B, C, A", "Título, autor y fuente, y luego permiso."),
        arith("Un curso tiene 5 textos con ficha y 3 de ellos no indican el permiso. ¿Cuántos sí lo indican?", "5-3", "Se restan los textos sin permiso."),
    ],
    context=[ex("Te entregan un texto con la palabra «mapu» y sin ficha. ¿Lo lees y copias sus palabras o pides primero la ficha?", "pides primero la ficha", "Sin ficha no sé la fuente ni el permiso.")],
    selfcheck=[
        ex("¿Qué dato me dice quién enseñó las palabras?", "la fuente", "La fuente es quien las enseñó."),
        ex("¿Qué hago si falta el permiso en la ficha?", "no uso las palabras y pregunto", "Sin permiso no se usan."),
        ex("¿Dice el propósito para qué se escribió un texto? Sí o No.", "Sí", "El propósito es el para qué."),
    ],
    task=T(
        "Lee este texto y su ficha, inventados para practicar. " + TXT_P + " " + FICHA_TXT + " " + FICHA_PAL + " En tu cuaderno escribe: 1) quién escribió el texto, 2) quién enseñó las palabras y hasta dónde llega el permiso, 3) para qué se escribió, 4) qué significa «ruka» según la ficha de palabras. Termina con una pregunta para el educador o la educadora tradicional.",
        "Lo escribió el curso. La fuente es la educadora tradicional y el permiso es solo dentro de la sala. Se escribió para contar la visita. «Ruka» es la casa mapuche. Pregunta: ¿cómo se construye una ruka?",
        ["anota quién escribió y la fuente", "dice hasta dónde llega el permiso", "dice el propósito", "formula una pregunta para el educador/a tradicional"],
        ["cuatro respuestas escritas", "pregunta escrita o dicha en voz alta"],
        ["confundir fuente con propósito", "decir que se puede usar fuera de la sala"],
        "Comprueba que separó fuente, permiso y propósito; si extendió el permiso, vuelve a leer la ficha con él.",
    ),
    reinforce="Lee la ficha del texto A y señala con el dedo cada dato: título, autor, fuente, permiso y propósito.",
    extend="Escribe una ficha de procedencia de cinco líneas para un texto breve inventado por ti.",
)

# =================================================================== LS03 clase 2 · anticipar sin estereotipos
L(
    LS3, 2,
    materials="Lápiz y hoja. Los títulos, los textos y las imágenes descritas están escritos aquí; son inventados para practicar.",
    use="Aprenderé a anticipar de qué trata un texto usando su título, su imagen y su ficha, sin caer en estereotipos sobre los pueblos originarios. Sirve para leer con la mente abierta y sin prejuicios.",
    prior=["Sé identificar la procedencia de un texto.", "Sé que cada pueblo tiene su propia cultura."],
    explain=[
        "Anticipar es pensar, antes de leer, de qué podría tratar el texto. Me ayudan el título, la imagen y la ficha de procedencia. Anticipo con una frase como «Creo que el texto habla de… porque el título dice…». Después leo para comprobar si acerté y, si me equivoqué, corrijo mi idea.",
        "Un estereotipo es una idea simplificada y repetida sobre un grupo, que se aplica a todos sus miembros sin conocerlos. Por ejemplo, «los pueblos originarios viven en el pasado» o «todos se visten igual» son estereotipos. Son falsos porque las personas de los pueblos originarios viven hoy en distintos lugares y de muchas formas.",
        "Para anticipar sin estereotipos me apoyo solo en lo que el texto muestra: su título, su ficha y las palabras escritas. No uso lo que «supongo» de un pueblo. Y cuando una anticipación resulta distinta, no pienso que el texto está mal: pienso que mi idea era muy general y la cambio.",
    ],
    vocab=[("anticipar", "pensar de qué trata un texto antes de leerlo"), ("estereotipo", "idea simplificada que se repite sobre todo un grupo"), ("prejuicio", "opinión formada antes de conocer"), ("comprobar", "verificar si algo es cierto"), ("título", "frase que da nombre a un texto")],
    worked=[
        W("Anticipar con el título", "Título: «Una mañana de lluvia en la escuela». Ficha: lo escribió un curso. ¿De qué podría tratar?", ["Leo el título: lluvia y escuela.", "Pienso en lo que podría contar: una mañana en la escuela con lluvia.", "Anticipo y luego lo compruebo."], "de una mañana de lluvia en la escuela"),
        W("Detectar un estereotipo", "Frases: A) «Los pueblos originarios viven solo en el pasado». B) «El texto cuenta la visita de una educadora a una escuela». ¿Cuál es un estereotipo?", ["Busco una idea que se aplica a todo un grupo.", "La A lo dice de todos los pueblos.", "La B se refiere a un texto."], "A"),
    ],
    mistakes=[
        M("Anticipar que el texto hablará del pasado solo porque tiene una palabra en lengua indígena.", "Es un estereotipo; el texto puede contar algo de hoy.", "Anticipo con el título y la ficha, no con lo que supongo."),
        M("Enojarme porque mi anticipación estaba equivocada.", "Anticipar es una idea para comprobar, no una verdad.", "Cambio mi idea si el texto dice otra cosa."),
    ],
    R=[
        ex("Anticipar, ¿es pensar de qué trata un texto antes de leerlo o resumirlo después?", "pensar de qué trata un texto antes de leerlo", "Es una idea previa."),
        ex("Un estereotipo, ¿es una idea simplificada sobre todo un grupo o un dato comprobado?", "una idea simplificada sobre todo un grupo", "Se aplica a todos sin conocerlos."),
        ex("Para anticipar sin estereotipos, ¿uso el título y la ficha o lo que supongo de un pueblo?", "el título y la ficha", "Son datos del texto."),
    ],
    C=[
        ex("Título: «Mi primer día con el saludo mari mari». ¿De qué crees que trata: de aprender a saludar o de una carrera?", "de aprender a saludar", "El título nombra el saludo."),
        ex("Verdadero o falso: «Todas las personas de los pueblos originarios visten igual» es un estereotipo.", "Verdadero", "Aplica una sola idea a todo un grupo."),
        ex("Si el texto dice algo distinto a lo que anticipé, ¿cambio mi idea o enojo con el texto?", "cambio mi idea", "Anticipar es una hipótesis."),
    ],
    A=[
        ex("Cuatro frases: 1) «Los pueblos originarios nunca usan tecnología». 2) «El texto A cuenta una visita». 3) «Todos los indígenas viven igual». 4) «La ficha dice quién escribió el texto». ¿Cuántas son estereotipos?", "2", "Son la 1 y la 3."),
        ex("Título: «Un dibujo de la ruka del curso». Con la palabra ruka (la casa mapuche, según la ficha), ¿qué anticipas: que habla de un dibujo de una casa o de una montaña?", "de un dibujo de una casa", "El título nombra el dibujo y la ruka."),
        ex("Completa la anticipación: «Creo que el texto habla de la luna porque el título dice «Noche con ____»». Elige entre kuyen y antü.", "kuyen", "«Kuyen» es luna según la ficha."),
    ],
    Z=[
        ex("Una niña dice: «Si un texto tiene una palabra en lengua indígena, seguro que habla de algo muy antiguo». ¿Su anticipación evita estereotipos? Sí o No.", "No", "Supone sin apoyo en el texto."),
        ex("Dos anticipaciones para el título «Mi día en la escuela con una visita»: A) «Habla de una visita a la escuela». B) «Habla de un pueblo que vive en el pasado». ¿Cuál se apoya en el título?", "A", "La B usa un estereotipo."),
    ],
    D=[
        ex("Ordena para anticipar bien: A) comparo con lo que leí. B) leo el título y la ficha. C) escribo qué creo que dirá. Escribe las letras en orden.", "B, C, A", "Primero título y ficha, luego anticipo y al final comparo."),
        ex("Cinco estudiantes anticiparon así: 1) con el título, 2) con un estereotipo, 3) con la ficha, 4) con un estereotipo, 5) con el título y la ficha. ¿Cuántos se apoyaron en datos del texto?", "3", "Son el 1, el 3 y el 5."),
    ],
    context=[ex("Un compañero dice antes de leer: «Ese texto es de gente que no conoce la tecnología». ¿Respondes «Anticipemos solo con el título y la ficha» o «Tienes razón»?", "«Anticipemos solo con el título y la ficha»", "Evita aplicar un estereotipo.")],
    selfcheck=[
        ex("¿Qué dato del texto uso para anticipar: el título o un prejuicio?", "el título", "El título es un dato del texto."),
        ex("¿Cómo corrijo mi anticipación si no coincide con el texto?", "cambio mi idea", "Anticipar es probar una idea."),
        ex("¿Un estereotipo habla de una persona concreta o de todo un grupo?", "de todo un grupo", "Generaliza sobre todo el grupo."),
    ],
    task=T(
        "Lee estos títulos y fichas, inventados para practicar. Título 1: «La mañana en que llegó una visita a la sala». Ficha: lo escribió el curso. Título 2: «Aprendemos a saludar con mari mari». Ficha: lo escribió el curso y la fuente de las palabras es la educadora tradicional. " + FICHA_SAL + " En tu cuaderno escribe: 1) una anticipación para cada título con «Creo que el texto habla de… porque…», 2) un estereotipo que NO usarías para anticipar y por qué, 3) una pregunta para el educador o la educadora tradicional.",
        "Creo que el texto 1 habla de una visita porque el título dice «llegó una visita». Creo que el texto 2 habla de aprender a saludar porque el título nombra mari mari. No usaría «los pueblos viven en el pasado» porque es un estereotipo. Pregunta: ¿cómo se saluda a una visita en su comunidad?",
        ["anticipa con el título y la ficha", "usa «porque» para justificar", "reconoce un estereotipo", "formula una pregunta para el educador/a tradicional"],
        ["dos anticipaciones y un estereotipo", "pregunta escrita o dicha en voz alta"],
        ["anticipar con estereotipos", "no justificar"],
        "Comprueba que sus anticipaciones se apoyen en el título; si usó un estereotipo, pide que lo cambie por un dato del texto.",
    ),
    reinforce="Escribe tres títulos de textos que conozcas y anticipa de qué tratan usando «porque».",
    extend="Explica a una persona de tu casa qué es un estereotipo y da un ejemplo que no ofenda a nadie.",
)

# =================================================================== LS03 clase 3 · localizar palabras y pistas
TXT_Q = "Texto de práctica B (inventado): «Lía llegó a la escuela cuando salía el antü. En la sala, la educadora tradicional mostró una hoja con «ko», «mapu» y «ruka». Lía copió las tres palabras en su cuaderno y dibujó una ruka junto a un río. Antes de irse, dijo «chaltumay» a la educadora.»"

L(
    LS3, 3,
    materials="Lápiz y hoja. El texto y las fichas están escritos aquí; son inventados para practicar.",
    use="Aprenderé a localizar en un texto breve las palabras significativas y las pistas que ayudan a entender su sentido. Sirve para responder con datos del texto y no con suposiciones.",
    prior=["Sé identificar la procedencia de un texto.", "Sé anticipar sin estereotipos."],
    explain=[
        "Una pista es un dato escrito en el texto que me ayuda a entender algo. Puede ser una palabra, una frase o un detalle. Por ejemplo, si el texto dice «cuando salía el antü», la pista «salía» me ayuda a entender que antü es algo que sale por la mañana, y la ficha confirma que es el sol.",
        "Para localizar hago tres pasos. Leo el texto completo. Marco las palabras que van entre comillas o que la ficha explica. Subrayo las pistas que están cerca de cada una, como lo que hace un personaje, el lugar o el momento. Después escribo la palabra, su significado según la ficha y la pista que la apoya.",
        "Una pista debe estar en el texto. Si no la encuentro, no la invento. Y si una palabra tiene un significado que la ficha no trae, no lo adivino: lo anoto como pregunta. Responder con una pista del texto es la mejor forma de mostrar que comprendí lo que leí.",
    ],
    vocab=[("pista", "dato del texto que ayuda a entender algo"), ("localizar", "encontrar algo dentro de un texto"), ("subrayar", "marcar con una línea lo importante"), ("confirmar", "comprobar que algo es cierto"), ("detalle", "dato pequeño del texto")],
    worked=[
        W("Localizar y confirmar", TXT_Q + " " + FICHA_PAL + " ¿Qué dibujó Lía junto a un río?", ["Busco «dibujó» en el texto.", "Dice: una ruka junto a un río.", "La ficha confirma que ruka es la casa mapuche."], "una ruka"),
        W("Usar una pista", TXT_Q + " ¿Cuándo llegó Lía a la escuela?", ["Busco la pista de tiempo.", "Dice «cuando salía el antü».", "Según la ficha, antü es el sol; llegó cuando salía el sol."], "cuando salía el sol (antü)"),
    ],
    mistakes=[
        M("Responder sin buscar la pista en el texto.", "Puedo inventar un dato que no está.", "Marco la pista antes de responder."),
        M("Explicar el significado de una palabra con lo que me parece.", "La ficha es la fuente del significado.", "Busco la palabra en la ficha."),
    ],
    R=[
        ex(TXT_Q + " ¿Qué dijo Lía antes de irse?", "chaltumay", "Lo dice la última oración."),
        ex(TXT_Q + " ¿Cuántas palabras copió Lía en su cuaderno?", "3", "Copió ko, mapu y ruka."),
        ex("Una pista, ¿es un dato del texto que ayuda a entender o una opinión mía sin apoyo?", "un dato del texto que ayuda a entender", "Debe estar escrita en el texto."),
    ],
    C=[
        ex(FICHA_PAL + " Según la ficha, ¿«ko» es agua o tierra?", "agua", "«Ko» es agua y «mapu», tierra."),
        ex(TXT_Q + " ¿Dónde dibujó Lía la ruka: junto a un río o junto a una montaña?", "junto a un río", "Lo dice el texto."),
        ex("Verdadero o falso: si no hay una pista en el texto, debo inventar una para responder.", "Falso", "Sin pista no afirmo."),
    ],
    A=[
        ex(TXT_Q + " Escribe, en el orden del texto, las tres palabras que la educadora mostró en la hoja.", "ko, mapu, ruka", "Aparecen en ese orden."),
        ex(TXT_Q + " " + FICHA_PAL + " ¿Qué palabra de la hoja se relaciona con el río que dibujó Lía?", "ko", "Según la ficha, «ko» es agua y un río es agua."),
        ex("Une cada palabra con su significado según la ficha. Palabras: 1) ko, 2) antü, 3) ruka. Significados: a) sol, b) agua, c) casa mapuche. Escribe las parejas.", "1-b, 2-a, 3-c", "Cada pareja sale de la ficha."),
    ],
    Z=[
        ex("Un niño dice: «Lía llegó de noche porque el texto dice «antü»». ¿Qué pista del texto lo contradice: «cuando salía el antü» o «copió las tres palabras»?", "«cuando salía el antü»", "Según la ficha, antü es el sol que sale por la mañana."),
        ex("Una niña afirma: «La ruka que dibujó Lía es de su familia». ¿El texto lo dice? Sí o No.", "No", "No hay una pista que apoye esa afirmación."),
    ],
    D=[
        ex(TXT_Q + " ¿Cuántas palabras en lengua indígena distintas aparecen en todo el texto?", "5", "Son antü, ko, mapu, ruka y chaltumay."),
        ex("Ordena los pasos para localizar una pista: A) escribo la palabra y su significado. B) subrayo lo que está cerca. C) leo el texto completo. Escribe las letras.", "C, B, A", "Leo, subrayo y escribo."),
    ],
    context=[ex("Alguien te pregunta qué mostró la educadora en la hoja, y tú no recuerdas el texto. ¿Vuelves al texto a buscar la pista o respondes con lo que imaginas?", "vuelves al texto a buscar la pista", "La respuesta se apoya en el texto.")],
    selfcheck=[
        ex("¿Dónde busco el significado de una palabra: en la ficha o en una suposición?", "en la ficha", "La ficha lo da."),
        ex("¿Qué subrayo para entender una palabra: las pistas cercanas o todo el texto?", "las pistas cercanas", "Son los datos que ayudan."),
        ex("Si no hay pista, ¿afirmo igual o pregunto?", "pregunto", "No inventamos datos."),
    ],
    task=T(
        "Lee este texto inventado para practicar. " + TXT_Q + " " + FICHA_PAL + " En tu cuaderno haz una tabla de tres columnas: palabra, significado según la ficha y pista del texto. Completa al menos cuatro filas (por ejemplo antü, ko, mapu y ruka). Termina con una pregunta para el educador o la educadora tradicional sobre una palabra que quieras entender mejor.",
        "antü, sol, «cuando salía el antü». ko, agua, «junto a un río». ruka, casa mapuche, «dibujó una ruka». mapu, tierra, «copió las tres palabras». Pregunta: ¿cómo se cuida la tierra en su comunidad?",
        ["completa cuatro filas", "toma el significado de la ficha", "indica una pista del texto en cada fila", "formula una pregunta para el educador/a tradicional"],
        ["tabla de tres columnas", "pregunta escrita o dicha en voz alta"],
        ["inventar significados", "no citar pistas"],
        "Verifica que cada pista esté en el texto; si usó una que no está, pídele que la cambie por una pregunta.",
    ),
    reinforce="Vuelve a leer el texto B y subraya las pistas que hay junto a la palabra antü.",
    extend="Escribe un texto de tres oraciones con dos palabras de la ficha y subraya las pistas que ayudan a entenderlas.",
)

# =================================================================== LS03 clase 4 · relacionar información y respuesta
TXT_R = "Texto de práctica C (inventado): «El curso preparó una tarjeta para agradecer a la educadora tradicional. Escribió «chaltumay» en grande y dibujó una ruka. Tomás propuso agregar el sol (antü), porque la visita llegó temprano. Ana propuso dibujar un río, porque le gusta el agua (ko). Finalmente el curso dibujó solo el sol, porque cabía mejor en la tarjeta.»"

L(
    LS3, 4,
    materials="Lápiz y hoja. El texto y las fichas están escritos aquí; son inventados para practicar. Las opiniones son tuyas y nadie tiene que contar datos privados.",
    use="Aprenderé a relacionar la información de un texto y a dar una opinión sobre su contenido cultural, apoyándome en lo que dice. Sirve para responder preguntas de comprensión y fundamentar lo que pienso.",
    prior=["Sé localizar palabras y pistas.", "Sé que una opinión se dice con una razón."],
    explain=[
        "Relacionar información es unir datos del mismo texto: quién hizo algo, por qué y qué pasó después. Palabras como «porque», «finalmente» y «propuso» me ayudan. En el texto de la tarjeta, Tomás propuso el sol porque la visita llegó temprano. La causa es que llegó temprano; el efecto es proponer el sol.",
        "Una opinión es lo que yo pienso sobre el texto, y se dice con una razón del texto. «Pienso que la tarjeta es respetuosa porque usa la palabra con su significado» es una opinión fundamentada. «Me gusta» solo no basta: falta el porque. Y una opinión no es una verdad para todos: es mi punto de vista.",
        "Mi opinión sobre el contenido cultural debe ser respetuosa: puedo decir lo que valoro, lo que me llama la atención o lo que me pregunto. No digo que una cultura es mejor ni peor, ni hablo por un pueblo. Y si mi opinión toca algo que no sé, lo planteo como pregunta al educador o a la educadora tradicional.",
    ],
    vocab=[("opinión", "lo que pienso sobre algo, con una razón"), ("fundamentar", "dar razones del texto para apoyar lo que pienso"), ("causa", "lo que hace que algo ocurra"), ("efecto", "lo que ocurre por una causa"), ("punto de vista", "manera personal de ver algo")],
    worked=[
        W("Causa y efecto", TXT_R + " ¿Por qué propuso Tomás agregar el sol (antü)?", ["Busco «Tomás» y «porque».", "Dice «porque la visita llegó temprano».", "Esa es la razón."], "porque la visita llegó temprano"),
        W("Opinión fundamentada", TXT_R + " Opiniones: A) «Me gusta». B) «Pienso que la tarjeta agradece con respeto porque lleva la palabra chaltumay, que significa gracias». ¿Cuál está fundamentada?", ["Busco una razón del texto.", "La B da una razón.", "La A no."], "B"),
    ],
    mistakes=[
        M("Dar una opinión sin ninguna razón del texto.", "Una opinión sin razón no se puede comprobar.", "Agrego «porque» y una pista del texto."),
        M("Decir que la cultura de un pueblo es mejor que otra.", "Falta de respeto; no se comparan así las culturas.", "Digo qué valoro del texto sin comparar."),
    ],
    R=[
        ex(TXT_R + " ¿Qué palabra escribió el curso en grande en la tarjeta?", "chaltumay", "Lo dice la segunda oración."),
        ex(TXT_R + " ¿Qué dibujó finalmente el curso: el sol o un río?", "el sol", "La última oración lo dice."),
        ex("Una opinión fundamentada, ¿tiene una razón del texto o no tiene razón?", "tiene una razón del texto", "Eso la fundamenta."),
    ],
    C=[
        ex(TXT_R + " ¿Por qué propuso Ana dibujar un río?", "porque le gusta el agua", "La razón está en el texto."),
        ex("Verdadero o falso: «Me gusta el texto» es una opinión fundamentada.", "Falso", "No da una razón."),
        ex(TXT_R + " ¿Por qué el curso dibujó solo el sol?", "porque cabía mejor en la tarjeta", "Es la última razón."),
    ],
    A=[
        ex(TXT_R + " Ordena lo que ocurre: A) el curso dibuja solo el sol. B) escribe «chaltumay». C) Tomás propone el sol. Escribe las letras.", "B, C, A", "Primero la palabra, luego la propuesta y al final el dibujo."),
        ex(TXT_R + " " + FICHA_SAL + " ¿Para qué hizo el curso la tarjeta?", "para agradecer a la educadora tradicional", "El texto lo dice y la ficha confirma el sentido de chaltumay."),
        ex(TXT_R + " Tomás y Ana propusieron dibujos distintos. ¿Quién propuso el sol y quién el río? Escribe los nombres en ese orden.", "Tomás y Ana", "Tomás propuso el sol y Ana, el río."),
    ],
    Z=[
        ex("Un niño dice: «La tarjeta está mal hecha porque no dibujaron el río». ¿Es una opinión fundamentada en el texto? Sí o No.", "No", "El texto explica que el sol cabía mejor, y no dice que falte algo."),
        ex("Dos opiniones: A) «Pienso que la tarjeta es respetuosa porque agradece con una palabra de la ficha». B) «Esa cultura es mejor que otras». ¿Cuál es respetuosa y fundamentada?", "A", "La B compara culturas sin razón."),
    ],
    D=[
        ex(TXT_R + " ¿Cuál opinión sobre la propuesta de Tomás está fundamentada? A) «Es buena porque la visita llegó temprano». B) «Es mala porque sí».", "A", "La A da una razón que está en el texto."),
        ex("Ordena para dar una opinión fundamentada: A) leo el texto. B) busco una razón. C) digo «pienso que… porque…». Escribe las letras.", "A, B, C", "Leo, busco una razón y la digo."),
    ],
    context=[ex("Tu compañero dice: «Esa tarjeta es aburrida». Tú quieres dar tu opinión con respeto. ¿Dices «Pienso que es respetuosa porque agradece con chaltumay» o «Tienes razón, es aburrida»?", "«Pienso que es respetuosa porque agradece con chaltumay»", "Das una opinión con una razón del texto.")],
    selfcheck=[
        ex("¿Qué palabra uso para dar la razón de una opinión: «porque» o «también»?", "«porque»", "«Porque» introduce la razón."),
        ex("¿Mi opinión es mi punto de vista o una verdad para todos?", "mi punto de vista", "Es la manera personal de ver."),
        ex("Si mi opinión toca algo que no sé de la cultura, ¿la planteo como pregunta?", "Sí", "Se pregunta al educador tradicional."),
    ],
    task=T(
        "Lee este texto inventado para practicar. " + TXT_R + " " + FICHA_SAL + " En tu cuaderno escribe: 1) una causa y su efecto del texto, 2) una opinión tuya con «Pienso que… porque…» sobre la tarjeta, 3) algo que valoras de la tarjeta y algo que te gustaría preguntar al educador o la educadora tradicional.",
        "Causa: la visita llegó temprano; efecto: Tomás propuso el sol. Pienso que la tarjeta es respetuosa porque agradece con «chaltumay». Valoro que usaron una palabra de la ficha. Pregunta: ¿cuándo se agradece así en su comunidad?",
        ["une una causa con su efecto", "escribe una opinión con «porque»", "valora algo con respeto", "formula una pregunta para el educador/a tradicional"],
        ["tres respuestas escritas", "pregunta escrita o dicha en voz alta"],
        ["opinar sin razón", "comparar culturas"],
        "Comprueba que la opinión tenga una razón del texto; si comparó culturas, conversa por qué se valora sin compararlas.",
    ),
    reinforce="Completa en tu cuaderno tres veces la frase «Pienso que… porque…» sobre el texto C.",
    extend="Escribe una opinión sobre el texto y otra opinión distinta que podría tener un compañero, ambas con razón.",
)

# =================================================================== LS03 clase 5 · explicar con evidencia y límites
TXT_S = "Texto de práctica D (inventado): «Hoy el curso aprendió que «ñuke» es madre y que «kuyen» es luna. La educadora tradicional dijo que hay muchas formas de decir y escribir las palabras, según cada comunidad, y que para saber cuál usar hay que preguntar. Al final, el curso copió las palabras de la ficha y anotó la fuente.»"

L(
    LS3, 5,
    materials="Lápiz y hoja. El texto y las fichas están escritos aquí; son inventados para practicar.",
    use="Aprenderé a explicar lo que comprendí de un texto con evidencia del texto y a decir hasta dónde llega lo que sé. Sirve para opinar con seguridad sin decir más de lo que el texto dice.",
    prior=["Sé localizar pistas y dar una opinión con «porque».", "Sé que una generalización dice que algo vale para todos sin saberlo."],
    explain=[
        "Explicar con evidencia es decir lo que pienso y mostrar la parte del texto que lo apoya. La evidencia es un dato escrito en el texto. Una explicación tiene tres partes: lo que afirmo, la evidencia que lo apoya y la razón que las une. Por ejemplo: «El curso respetó la fuente, porque dice que anotó la fuente».",
        "Los límites son lo que el texto no dice o lo que yo no sé. Un texto breve no me cuenta toda una cultura. Por eso uso frases como «según el texto…», «el texto no dice…» y «para saber más, preguntaría a…». Decir un límite no es un error: es ser honesto y respetuoso con quienes comparten su cultura.",
        "En este texto, la educadora dice que hay muchas formas de decir y escribir las palabras, según cada comunidad. Eso significa que no debo afirmar que una sola escritura es «la correcta» para todos. Mi explicación se queda en lo que el texto dice y dejo las preguntas culturales abiertas para el educador tradicional.",
    ],
    vocab=[("evidencia", "dato del texto que apoya lo que afirmo"), ("explicar", "decir con claridad qué pienso y por qué"), ("límite", "lo que el texto no dice o lo que no sé"), ("según el texto", "frase que muestra de dónde sale una idea"), ("afirmar", "decir que algo es cierto")],
    worked=[
        W("Afirmación, evidencia y razón", TXT_S + " Afirmación: «El curso cuidó la fuente». ¿Cuál es la evidencia?", ["Busco una parte del texto que lo apoye.", "Dice: «anotó la fuente».", "Esa frase es la evidencia."], "«anotó la fuente»"),
        W("Decir un límite", TXT_S + " ¿El texto dice cómo se saluda en cada comunidad? Sí o No.", ["Busco en el texto cómo se saluda.", "No hay nada sobre saludos.", "El texto no lo dice; es un límite."], "No"),
    ],
    mistakes=[
        M("Afirmar algo del texto sin mostrar la evidencia.", "Nadie puede comprobar de dónde lo saqué.", "Agrego «según el texto…» y cito la parte que lo apoya."),
        M("Decir más de lo que el texto cuenta, como si supiera toda la cultura.", "Un texto breve no cuenta toda una cultura.", "Digo «el texto no dice…» y planteo una pregunta."),
    ],
    R=[
        ex(TXT_S + " ¿Qué dijo la educadora que hay muchas?", "formas de decir y escribir las palabras", "Lo dice la segunda oración."),
        ex(TXT_S + " ¿Qué significa «ñuke» según el texto?", "madre", "El texto lo explica en la primera oración."),
        ex("La evidencia, ¿es un dato del texto que apoya lo que afirmo o una idea sin apoyo?", "un dato del texto que apoya lo que afirmo", "Está escrita en el texto."),
    ],
    C=[
        ex(TXT_S + " ¿Qué copió el curso al final?", "las palabras de la ficha", "La última oración lo dice."),
        ex("Verdadero o falso: un texto breve cuenta toda la cultura de un pueblo.", "Falso", "Solo muestra una parte."),
        ex("Frases que ponen un límite: A) «el texto no dice…». B) «todos saben que…». ¿Cuál pone un límite?", "A", "La B generaliza."),
    ],
    A=[
        ex("Une cada afirmación con su evidencia del texto D. Afirmaciones: 1) «El curso aprendió dos palabras». 2) «La educadora pidió preguntar». Evidencias: a) «hay que preguntar». b) ««ñuke» es madre y «kuyen» es luna». Escribe las parejas.", "1-b, 2-a", "Cada evidencia apoya su afirmación."),
        ex(TXT_S + " Escribe las dos palabras en lengua indígena que aparecen entre comillas y su significado.", "ñuke (madre) y kuyen (luna)", "Son las que el texto explica."),
        ex("Completa con un límite: «El texto D no dice ____». Elige: cómo se hace una ruka o que anotaron la fuente.", "cómo se hace una ruka", "El texto no habla de eso, pero sí dice que anotaron la fuente."),
    ],
    Z=[
        ex("Un niño dice: «Según el texto, solo hay una forma correcta de escribir las palabras». ¿Tiene razón? Sí o No.", "No", "El texto dice que hay muchas formas según cada comunidad."),
        ex("Dos explicaciones: A) «El curso respetó la fuente, porque el texto dice que anotó la fuente». B) «El curso respetó la fuente, porque todos lo hacen». ¿Cuál tiene evidencia?", "A", "La B no cita el texto."),
    ],
    D=[
        ex(TXT_S + " ¿Qué evidencia del texto apoya la afirmación «El curso trabajó con cuidado»? A) «copió las palabras de la ficha y anotó la fuente». B) «hay muchas formas de decir y escribir las palabras».", "A", "La A muestra lo que el curso hizo con cuidado."),
        arith("Un curso explicó 6 ideas del texto: 4 con evidencia y las demás sin ella. ¿Cuántas ideas explicó sin evidencia?", "6-4", "Se restan las que tienen evidencia."),
    ],
    context=[ex("Un compañero dice que sabe cómo se hace una ceremonia porque leyó un texto breve que solo explica dos palabras. ¿Le respondes «El texto no dice eso; preguntemos al educador tradicional» o «Tienes razón»?", "«El texto no dice eso; preguntemos al educador tradicional»", "Un texto breve tiene límites.")],
    selfcheck=[
        ex("¿Cuántas partes tiene una explicación con afirmación, evidencia y razón?", "3", "Se cuentan tres partes."),
        ex("¿Qué frase uso para mostrar de dónde sale mi idea: «según el texto» o «todo el mundo sabe»?", "«según el texto»", "Cita la fuente."),
        ex("Si el texto no dice algo, ¿lo invento o digo que no lo dice?", "digo que no lo dice", "Es un límite."),
    ],
    task=T(
        "Lee este texto inventado para practicar. " + TXT_S + " " + FICHA_PAL + " En tu cuaderno escribe: 1) una explicación con tres partes (afirmación, evidencia, razón) sobre cómo trabajó el curso, 2) una cosa que el texto no dice, 3) una pregunta para el educador o la educadora tradicional sobre cómo elegir qué forma de escribir una palabra usar.",
        "Afirmación: el curso trabajó con cuidado. Evidencia: copió las palabras de la ficha y anotó la fuente. Razón: así no inventó nada. El texto no dice cómo se construye una ruka. Pregunta: ¿cómo sé qué forma de escribir una palabra usar en mi comunidad?",
        ["escribe afirmación, evidencia y razón", "cita una parte del texto", "dice algo que el texto no dice", "formula una pregunta para el educador/a tradicional"],
        ["explicación de tres partes", "pregunta escrita o dicha en voz alta"],
        ["afirmar sin evidencia", "decir más de lo que el texto dice"],
        "Comprueba que cite una parte del texto y que reconozca un límite; si afirmó más de lo que el texto dice, vuelve a leer con él la parte relevante.",
    ),
    reinforce="Elige una idea del texto D y escribe, en una tarjeta, la parte del texto que la apoya.",
    extend="Explica por qué un texto breve no puede contarnos toda la cultura de un pueblo.",
)
