"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS04 (escritura inicial de palabras culturalmente significativas para nombrar y caracterizar) y OA LS05
(creaciones digitales de sensibilización cultural y lingüística), contexto de sensibilización.

Criterio de autoría: todas las fichas, tarjetas, casos, escuelas y personas son inventados solo para practicar y están
rotulados como tales. Las únicas palabras en lengua indígena son muy atestiguadas (mari mari, chaltumay, ko, antü,
kuyen, ruka, mapu, ñuke) y las variantes de escritura ruka/ruca, pewen/pehuén y mapuzugun/mapudungun, presentadas sin
jerarquizar. Las cualidades se escriben en castellano; no se inventa ortografía, símbolo ni gramática. Los recursos
digitales se describen sin marcas ni enlaces y siempre con un adulto. Cada tarea abierta remite al educador/a
tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS4, LS5 = "LC03 OA LS04", "LC03 OA LS05"

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


# =================================================================== LS04 clase 1 · observar modelo y procedencia
MODFICHA = "Ficha de modelos (inventada para practicar): Modelo 1: «ruka», casa mapuche, Fuente: ficha de la clase. Modelo 2: «ñuke», madre, Fuente: ficha de la clase. Modelo 3: «kuyen», luna, Fuente: ficha de la clase."

L(
    LS4, 1,
    materials="Lápiz, hoja y regla. Los modelos están escritos en este cuaderno y siempre quedan a la vista mientras copio.",
    use="Aprenderé a observar un modelo escrito y a anotar de dónde viene antes de copiarlo. Sirve para escribir palabras de una lengua indígena sin inventar letras ni ortografía.",
    prior=["Sé que la ficha dice el significado de una palabra.", "Sé que la ñ y la ü son letras que no se omiten."],
    explain=[
        "Un modelo es una palabra bien escrita, con su significado y su fuente, que dejo a la vista mientras copio. La grafía es la forma en que se escribe una palabra, con sus letras. Para copiar bien, observo el modelo letra por letra y no me fío de mi memoria.",
        "Cada modelo viene de una fuente, que es la ficha, el libro o la persona que lo entregó. Esa procedencia se anota junto a la palabra: «ruka», casa mapuche, Fuente: ficha de la clase. Si no sé de dónde viene una palabra, no la uso como modelo.",
        "Al copiar sigo tres pasos: miro el modelo, escribo una letra tras otra y comparo mi copia con el modelo. No invento letras, signos ni símbolos nuevos, porque no conozco las reglas de escritura de esa lengua. Si me falta una letra, pregunto al educador o a la educadora tradicional.",
    ],
    vocab=[("modelo", "palabra bien escrita que sirve para copiar"), ("grafía", "forma en que se escribe una palabra"), ("procedencia", "de dónde viene una palabra"), ("comparar", "mirar dos cosas para ver si son iguales"), ("copiar", "escribir igual a un modelo")],
    worked=[
        W("Copiar y anotar la fuente", MODFICHA + " Copia el modelo 1 con su significado y su fuente.", ["Miro «ruka» letra por letra: r, u, k, a.", "Escribo la palabra y su significado: casa mapuche.", "Agrego la fuente: ficha de la clase."], "«ruka», casa mapuche, Fuente: ficha de la clase"),
        W("Comparar con el modelo", "Modelo: «ñuke». Mi copia: «nuke». ¿Coincide?", ["Comparo la primera letra.", "El modelo empieza con ñ y mi copia con n.", "No coincide."], "No: falta la ñ"),
    ],
    mistakes=[
        M("Copiar de memoria sin mirar el modelo.", "Puedo cambiar una letra sin darme cuenta.", "Dejo el modelo a la vista y comparo."),
        M("Usar una palabra como modelo sin saber de dónde viene.", "No tengo cómo comprobar su escritura.", "Anoto la fuente o pregunto al educador tradicional."),
    ],
    R=[
        ex(MODFICHA + " ¿Cuál es el significado de «ruka»?", "casa mapuche", "La ficha de modelos lo dice."),
        ex("En la ficha de modelos, ¿cuál es la fuente de «kuyen»?", "la ficha de la clase", "Cada modelo trae su fuente."),
        ex("¿Qué letra especial tiene el modelo 2?", "la ñ", "«Ñuke» empieza con ñ."),
    ],
    C=[
        ex("Verdadero o falso: puedo copiar un modelo de memoria sin mirarlo.", "Falso", "Debo dejarlo a la vista."),
        ex("Modelo: «kuyen». Mi copia: «kuyen». ¿Coincide? Sí o No.", "Sí", "Todas las letras son iguales."),
        ex("¿Qué dos datos anoto junto a un modelo además de la palabra: significado y fuente, o color y tamaño?", "significado y fuente", "Son los datos de la ficha de modelos."),
    ],
    A=[
        ex("¿Cuál es la copia correcta del modelo 3 con su significado y su fuente? A) «kuyen», luna, Fuente: ficha de la clase. B) «kuyen», sol, Fuente: ficha de la clase.", "A", "La ficha dice que «kuyen» es luna."),
        ex("Mira los modelos 1 y 3 de la ficha. ¿Qué palabra tiene más letras: «ruka» o «kuyen»?", "kuyen", "«Kuyen» tiene 5 letras y «ruka» tiene 4."),
        ex("Un compañero copió «ruka» como «ruca». ¿Coincide con el modelo de la ficha? Sí o No.", "No", "La tercera letra es distinta."),
    ],
    Z=[
        ex("Ana encontró «ñuke» en un papel sin fuente. ¿La usa como modelo o primero pregunta de dónde viene?", "pregunta de dónde viene", "Sin fuente no puedo comprobar."),
        ex("Pedro agrega un signo nuevo sobre una letra «para que se vea bien». ¿Es correcto inventar signos? Sí o No.", "No", "No conozco las reglas de escritura de esa lengua."),
    ],
    D=[
        ex("Ordena los pasos para copiar: A) comparo mi copia con el modelo. B) miro el modelo letra por letra. C) escribo una letra tras otra. Escribe las letras.", "B, C, A", "Miro, escribo y comparo."),
        ex("En la ficha de modelos hay 3 palabras y ya copiaste «ruka» y «kuyen». ¿Cuál te falta copiar?", "«ñuke»", "Es el modelo 2."),
    ],
    context=[ex("Tu curso hará una tarjeta con «ruka». Hay una ficha de la clase y un papel suelto sin fuente que dice «rukka». ¿Qué modelo usas?", "el de la ficha de la clase", "Tiene fuente que puedo comprobar.")],
    selfcheck=[
        ex("¿Dónde dejo el modelo mientras copio?", "a la vista", "Así comparo letra por letra."),
        ex("¿Qué dato anoto para saber de dónde viene el modelo?", "la fuente", "Dice la procedencia."),
        ex("¿Puedo inventar un signo si me falta una letra?", "No", "Pregunto al educador tradicional."),
    ],
    task=T(
        "Usa esta ficha de modelos: " + MODFICHA + " En tu cuaderno copia los tres modelos, cada uno en una línea con el formato «palabra, significado, Fuente: ficha de la clase». Compara tu copia con el modelo letra por letra y marca con un visto bueno las que coinciden. Termina con una pregunta para la educadora tradicional sobre una letra o una palabra que quieras entender mejor.",
        "«ruka», casa mapuche, Fuente: ficha de la clase. «ñuke», madre, Fuente: ficha de la clase. «kuyen», luna, Fuente: ficha de la clase. Pregunta: ¿cómo se escribe «casa grande» en su comunidad?",
        ["copia los tres modelos con ñ", "anota significado y fuente", "compara letra por letra", "formula una pregunta para el educador/a tradicional"],
        ["tres líneas copiadas", "pregunta escrita o dicha en voz alta"],
        ["omitir la ñ", "inventar un signo"],
        "Comprueba que la copia coincide letra por letra; si agregó signos nuevos, pídele que los quite y los convierta en pregunta.",
    ),
    reinforce="Copia «kuyen» tres veces mirando el modelo y compara cada copia.",
    extend="Haz tu propia ficha de modelos con tres palabras de la ficha de palabras y anota la fuente de cada una.",
)

# =================================================================== LS04 clase 2 · escribir para nombrar
L(
    LS4, 2,
    materials="Lápiz, hojas y colores. Las tarjetas de nombre se hacen para objetos de práctica dibujados.",
    use="Aprenderé a escribir palabras para nombrar, haciendo tarjetas de nombre para dibujos u objetos. Sirve para presentar palabras de una lengua indígena y también expresiones culturalmente significativas en castellano.",
    prior=["Sé copiar un modelo con su fuente.", "Sé que la ficha dice el significado de cada palabra."],
    explain=[
        "Nombrar es decir cómo se llama algo. Una tarjeta de nombre es un papel pequeño que lleva el nombre de un objeto, un lugar o una persona que cumple un rol, como la educadora tradicional. Para hacerla copio el nombre del modelo y lo pego junto al dibujo.",
        "Puedo nombrar con una palabra de una lengua indígena, como «ko» para el agua. También puedo nombrar con una expresión culturalmente significativa en castellano, como «educadora tradicional», «comunidad» o «territorio». Escribo estas últimas con cuidado y las explico con la ficha del curso.",
        "Mi tarjeta tiene tres líneas: el nombre, para qué cosa es y la fuente. Por ejemplo: «ko» / el agua del vaso / Fuente: ficha de la clase. Si no tengo el nombre de algo en mi ficha, dejo la tarjeta en blanco y pregunto. No invento nombres.",
    ],
    vocab=[("nombrar", "decir cómo se llama algo"), ("tarjeta de nombre", "papel pequeño con el nombre de algo"), ("rol", "función que una persona cumple"), ("expresión en castellano", "palabras en castellano con valor cultural en el texto"), ("en blanco", "sin escribir")],
    worked=[
        W("Hacer una tarjeta", FICHA_PAL + " Dibujo: un sol sobre una casa. Haz la tarjeta del sol.", ["Busco sol en la ficha: «antü».", "Copio la palabra y agrego para qué cosa es: el sol del dibujo.", "Anoto la fuente: ficha de la clase."], "«antü» / el sol del dibujo / Fuente: ficha de la clase"),
        W("Nombrar en castellano", "Ficha: «educadora tradicional» es el nombre en castellano de la persona que enseña la lengua y la cultura de su pueblo en la escuela. Haz la tarjeta de nombre para la persona que visita el curso.", ["Copio el nombre del modelo: educadora tradicional.", "Agrego para qué es: la persona que visita el curso.", "Anoto la fuente: ficha de la clase."], "«educadora tradicional» / la persona que visita el curso / Fuente: ficha de la clase"),
    ],
    mistakes=[
        M("Inventar un nombre cuando la ficha no lo trae.", "Podría estar creando una palabra que no existe.", "Dejo la tarjeta en blanco y pregunto."),
        M("Hacer la tarjeta sin fuente.", "No se sabe de dónde viene el nombre.", "Agrego la tercera línea con la fuente."),
    ],
    R=[
        ex(FICHA_PAL + " Tarjeta para el dibujo de una casa mapuche. ¿Qué palabra copias?", "ruka", "Según la ficha, ruka es la casa mapuche."),
        ex("Tarjeta para el dibujo de la tierra. ¿Qué palabra de la ficha copias?", "mapu", "Mapu es tierra."),
        ex("¿Cuántas líneas tiene una tarjeta de nombre de esta clase?", "3", "Son nombre, para qué cosa es y fuente."),
    ],
    C=[
        ex("Verdadero o falso: puedo nombrar con una palabra indígena o con una expresión culturalmente significativa en castellano.", "Verdadero", "Las dos sirven para nombrar si tienen fuente."),
        ex("¿Cuál tarjeta está completa? A) «ko» / el agua del vaso / Fuente: ficha de la clase. B) «ko».", "A", "La A tiene las tres líneas."),
        ex("La ficha no trae la palabra para el dibujo de un lago. ¿Qué hago con la tarjeta: la dejo en blanco o la invento?", "la dejo en blanco", "No invento nombres."),
    ],
    A=[
        ex("Tres dibujos: sol, luna y agua. Escribe los tres nombres en ese orden con la ficha.", "antü, kuyen, ko", "Sol es antü, luna es kuyen y agua es ko."),
        ex("Una tarjeta de nombre tiene solo el nombre y la fuente. ¿Qué línea le falta?", "para qué cosa es", "Las tres líneas son el nombre, para qué cosa es y la fuente."),
        ex("Ficha del curso: «educadora tradicional» es el nombre en castellano de la persona que enseña la lengua y la cultura de su pueblo en la escuela. Quieres una tarjeta para esa persona. ¿Qué nombre usas?", "educadora tradicional", "Es el nombre de esa persona según la ficha."),
    ],
    Z=[
        ex("Camila escribe «mapu» bajo un dibujo del agua. ¿Cuál es el error?", "usó la palabra de la tierra", "Mapu es tierra y ko es agua."),
        ex("Una tarjeta no dice la fuente. ¿Qué le falta: la tercera línea o más dibujos?", "la tercera línea", "La fuente va en la tercera línea."),
    ],
    D=[
        ex("Ordena los pasos: A) pego la tarjeta junto al dibujo. B) copio el nombre del modelo. C) escribo la fuente. Escribe las letras.", "B, C, A", "Copio, anoto la fuente y pego."),
        ex("Un mural tiene los dibujos del sol, la luna y el agua. Ya hiciste las tarjetas de «antü» y «ko». ¿Qué tarjeta falta y qué palabra lleva?", "la de la luna: «kuyen»", "Sol es antü, agua es ko y luna es kuyen."),
    ],
    context=[ex("Para el diario mural de tu sala haces tarjetas para un dibujo de una casa mapuche, uno del sol y uno del agua. ¿Qué tres palabras escribes en ese orden?", "ruka, antü, ko", "La casa mapuche es ruka, sol es antü y agua es ko.")],
    selfcheck=[
        ex("¿Qué es nombrar?", "decir cómo se llama algo", "Es poner un nombre."),
        ex("¿Qué tres datos lleva mi tarjeta?", "nombre, para qué es y fuente", "Son sus tres líneas."),
        ex("Si la ficha no trae el nombre, ¿qué hago?", "dejo la tarjeta en blanco y pregunto", "No invento nombres."),
    ],
    task=T(
        "Haz tres tarjetas de nombre de práctica usando la ficha: " + FICHA_PAL + " Dibuja un vaso con agua, una luna y una casa mapuche pequeña de papel. Cada tarjeta lleva tres líneas: el nombre copiado, para qué dibujo es y «Fuente: ficha de la clase». Haz una cuarta tarjeta con la expresión en castellano «educadora tradicional» (en la clase, la ficha dice que es el nombre de la persona que enseña la lengua y la cultura de su pueblo) para la persona que visita tu curso. Termina con una pregunta para la educadora tradicional.",
        "«ko» / el agua del vaso / Fuente: ficha de la clase. «kuyen» / la luna dibujada / Fuente: ficha de la clase. «ruka» / la casa mapuche de papel / Fuente: ficha de la clase. «educadora tradicional» / la persona que visita el curso / Fuente: ficha de la clase. Pregunta: ¿cómo se nombra un lago en su comunidad?",
        ["copia bien las tres palabras", "cada tarjeta tiene tres líneas", "incluye la tarjeta en castellano", "formula una pregunta para el educador/a tradicional"],
        ["cuatro tarjetas de nombre", "pregunta escrita o dicha en voz alta"],
        ["inventar un nombre", "olvidar la fuente"],
        "Revisa que cada tarjeta tenga fuente y que las palabras coincidan con la ficha; si inventó un nombre, pídele que lo cambie por una tarjeta en blanco.",
    ),
    reinforce="Escribe tres veces «antü» en una tarjeta mirando el modelo y revisa la ü.",
    extend="Haz una tarjeta más para un objeto de tu sala y deja el nombre en blanco con la frase «por preguntar».",
)

# =================================================================== LS04 clase 3 · escribir para caracterizar
L(
    LS4, 3,
    materials="Lápiz y hoja. Las listas de cualidades están escritas en este cuaderno.",
    use="Aprenderé a escribir cualidades en castellano que digan cómo es lo que nombra una palabra de la ficha. Sirve para describir con cuidado, sin inventar nada sobre la cultura.",
    prior=["Sé hacer tarjetas de nombre.", "Sé que la ficha dice el significado de cada palabra."],
    explain=[
        "Caracterizar es decir cómo es algo. Para hacerlo uso cualidades, que son palabras en castellano como grande, pequeña, clara, fría, cálido o brillante. Una tarjeta de caracterización lleva la palabra de la ficha, su significado y dos cualidades.",
        "Las cualidades salen de lo que puedo observar en un objeto de práctica: el agua de un vaso se ve clara y puede estar fría; el sol en un dibujo es brillante; una casita de papel es pequeña. Elijo cualidades que se puedan observar y que no sean ofensivas ni digan algo que no sé.",
        "No uso cualidades para hablar de las personas ni de su cultura, como «raro» o «antiguo». Y no invento significados culturales: si me preguntan qué significa algo para una comunidad, digo que eso lo explica la educadora tradicional.",
    ],
    vocab=[("caracterizar", "decir cómo es algo"), ("cualidad", "palabra que dice cómo es algo"), ("observar", "mirar con atención para notar detalles"), ("ofensivo", "que puede dañar a otras personas"), ("objeto de práctica", "objeto o dibujo que uso para ejercitar")],
    worked=[
        W("Tarjeta de caracterización", FICHA_PAL + " Objeto de práctica: un vaso con agua clara y fría. Escribe la tarjeta.", ["Palabra de la ficha: «ko».", "Significado: agua.", "Cualidades que observo: clara y fría."], "«ko», agua, cualidades: clara, fría"),
        W("Elegir cualidades observables", "Objeto de práctica: un dibujo del sol. Cualidades posibles: brillante, ruidoso, redondo, triste. ¿Cuáles puedes observar en un dibujo del sol?", ["Un sol dibujado se ve brillante.", "También se ve redondo.", "«Ruidoso» y «triste» no se observan en un dibujo."], "brillante y redondo"),
    ],
    mistakes=[
        M("Usar cualidades que hablan mal de una cultura.", "Pueden ofender y no son datos observables.", "Uso cualidades del objeto de práctica que pueda observar."),
        M("Decir qué significa un objeto para una comunidad.", "No lo sé y no me corresponde afirmarlo.", "Digo que eso lo explica la educadora tradicional."),
    ],
    R=[
        ex("«Clara» y «fría» son cualidades. ¿Describen cómo es algo o cómo se llama?", "cómo es algo", "Una cualidad dice cómo es."),
        ex(FICHA_PAL + " En la tarjeta del vaso con agua, ¿qué palabra de la ficha va primero?", "ko", "El agua es ko."),
        ex("En la tarjeta del sol dibujado, ¿qué cualidad podría ir: brillante o ruidoso?", "brillante", "Un sol dibujado se ve brillante."),
    ],
    C=[
        ex("Verdadero o falso: las cualidades que uso deben poder observarse en el objeto de práctica.", "Verdadero", "Así no invento nada."),
        ex("¿Cuál cualidad describe una casita de papel pequeña: pequeña o profunda?", "pequeña", "Se puede ver su tamaño."),
        ex("Una tarjeta de caracterización lleva palabra, significado y dos cualidades. ¿Cuántos datos lleva en total?", "4", "Son 1 palabra, 1 significado y 2 cualidades."),
    ],
    A=[
        ex("Objeto: una casa mapuche de papel, grande y blanca. ¿Cuál tarjeta está bien hecha? A) «ruka», casa mapuche, cualidades: grande, blanca. B) «ruka», casa mapuche, cualidades: antigua, misteriosa.", "A", "La A usa cualidades que se observan; la B no."),
        ex("Objeto: la luna dibujada, brillante y redonda. ¿Qué palabra de la ficha usas?", "kuyen", "Según la ficha, kuyen es luna."),
        ex("Objeto: una casa mapuche pequeña de papel. Cualidades posibles: pequeña, misteriosa, de papel. ¿Cuáles puedes observar?", "pequeña y de papel", "«Misteriosa» no se puede observar."),
    ],
    Z=[
        ex("Tomás escribe la cualidad «antigua» para describir a una persona de una comunidad. ¿Es adecuado? Sí o No.", "No", "Habla de una persona y puede ofender."),
        ex("Una compañera pregunta qué significa el sol para una comunidad. ¿Qué respondes: que eso lo explica la educadora tradicional o que lo inventas?", "que eso lo explica la educadora tradicional", "No me corresponde afirmarlo."),
    ],
    D=[
        ex("Ordena los pasos: A) escribo el significado de la ficha. B) observo el objeto. C) elijo dos cualidades observables. Escribe las letras.", "B, A, C", "Observo, anoto el significado y elijo cualidades."),
        ex("Objeto: agua en un vaso, clara y fría al tocarla. Cualidades posibles: clara, misteriosa, fría, secreta. ¿Cuáles son observables?", "clara y fría", "«Misteriosa» y «secreta» no se pueden observar."),
    ],
    context=[ex("Para la exposición del curso describes una jarra con agua. ¿Qué tarjeta presentas: «ko», agua, clara y fría; o «ko», agua, misteriosa y secreta?", "«ko», agua, clara y fría", "Usa cualidades observables.")],
    selfcheck=[
        ex("¿Cómo se llama la palabra que dice cómo es algo?", "cualidad", "Las cualidades describen."),
        ex("¿Qué cualidades uso: observables o inventadas?", "observables", "Así no invento nada."),
        ex("¿Quién explica el significado cultural de un objeto?", "la educadora tradicional", "Es quien conoce la cultura."),
    ],
    task=T(
        "Haz tres tarjetas de caracterización de práctica con la ficha: " + FICHA_PAL + " Mira estos objetos de práctica: un vaso con agua clara y fría, un dibujo del sol brillante y una casa mapuche pequeña de papel. Cada tarjeta lleva la palabra de la ficha, su significado y dos cualidades que puedas observar. Termina con una pregunta para la educadora tradicional sobre qué significa algo para su comunidad.",
        "«ko», agua: clara, fría. «antü», sol: brillante, redondo. «ruka», casa mapuche: pequeña, de papel. Pregunta: ¿qué significa el agua para su comunidad?",
        ["usa las palabras de la ficha", "las cualidades son observables", "cada tarjeta tiene palabra, significado y dos cualidades", "formula una pregunta para el educador/a tradicional"],
        ["tres tarjetas", "pregunta escrita o dicha en voz alta"],
        ["usar cualidades ofensivas", "inventar significados culturales"],
        "Verifica que las cualidades sean observables; si inventó un significado cultural, pídele que lo cambie por una pregunta.",
    ),
    reinforce="Observa un objeto de tu casa y escribe dos cualidades en castellano que puedas ver o tocar.",
    extend="Escribe una tarjeta de caracterización para «mapu» con un objeto de práctica de tierra seca en un frasco cerrado dibujado.",
)

# =================================================================== LS04 clase 4 · revisar sin jerarquizar variantes
L(
    LS4, 4,
    materials="Lápiz y hoja. Las variantes están escritas en este cuaderno.",
    use="Aprenderé a revisar mis palabras sin decir que una variante es mejor que otra. Sirve para respetar las distintas formas en que se escribe una lengua y preguntar a quien corresponde.",
    prior=["Sé qué es una variante.", "Sé copiar un modelo y anotar la fuente."],
    explain=[
        "Una variante es otra forma de escribir o decir la misma palabra. Algunas lenguas indígenas se escriben de más de una manera y existen fuentes válidas con grafías distintas. Por ejemplo, la casa mapuche aparece escrita «ruka» o «ruca»; la araucaria, «pewen» o «pehuén»; y la lengua del pueblo mapuche, «mapuzugun» o «mapudungun».",
        "Jerarquizar es poner una forma sobre otra, como decir «esta es la buena y esta es mala». No lo hago. Cuando reviso, comparo con la fuente de mi modelo. Si mi copia no coincide con mi modelo, la corrijo. Pero si dos fuentes escriben distinto, anoto las dos con sus fuentes.",
        "Qué variante usar en un cartel de mi escuela lo decide la comunidad, a través del educador o la educadora tradicional. Yo hago la pregunta: «¿Qué forma usan en su comunidad?». Y mientras tanto, documento ambas.",
    ],
    vocab=[("variante", "otra forma de escribir o decir la misma palabra"), ("jerarquizar", "poner una forma por encima de otra"), ("documentar", "anotar algo con su fuente"), ("fuente válida", "ficha o persona que conoce la lengua y dice de dónde viene su saber"), ("comunidad", "grupo de personas que comparte una cultura")],
    worked=[
        W("Anotar dos variantes", "Libro de la biblioteca: «ruka». Cartel de la escuela: «ruca». Ambos hablan de la casa mapuche. ¿Cómo documentas?", ["Escribo las dos formas.", "Anoto la fuente de cada una.", "No digo cuál es la buena."], "ruka (libro), ruca (cartel); no se jerarquiza"),
        W("Preguntar bien", "Ficha dice «pewen» y un cuento dice «pehuén». ¿Qué pregunta haces: «¿Cuál es la correcta?» o «¿Qué forma usan en su comunidad?»", ["La primera pone una forma sobre otra.", "La segunda respeta las dos.", "Elijo la segunda."], "«¿Qué forma usan en su comunidad?»"),
    ],
    mistakes=[
        M("Tachar una variante diciendo que está mal.", "Puede ser válida en otra fuente.", "Anoto ambas con su fuente."),
        M("Decidir yo cuál variante va en el cartel.", "La decisión corresponde a la comunidad.", "Pregunto al educador tradicional."),
    ],
    R=[
        ex("La casa mapuche se escribe «ruka» o «ruca». ¿Son variantes? Sí o No.", "Sí", "Son dos formas de escribir lo mismo."),
        ex("¿Jerarquizar es poner una forma sobre otra? Sí o No.", "Sí", "Esa es su definición."),
        ex("¿Debo decir que una variante es mala? Sí o No.", "No", "Cada una puede ser válida en su fuente."),
    ],
    C=[
        ex("Verdadero o falso: si mi copia no coincide con mi modelo, la corrijo.", "Verdadero", "Reviso contra mi modelo."),
        ex("Dos fuentes escriben «mapuzugun» y «mapudungun». ¿Qué hago: anoto las dos o elimino una?", "anoto las dos", "No pongo una forma sobre otra."),
        ex("¿Quién decide qué variante va en el cartel de mi escuela: la comunidad o yo solo?", "la comunidad", "Lo decide a través del educador tradicional."),
    ],
    A=[
        ex("Tu libro escribe «ruka» y tu cartel escribe «ruca». ¿Qué anotas junto a cada forma?", "su fuente", "Documentar es anotar cada forma con su fuente."),
        ex("Elige la mejor revisión. A) «Mi cartel dice «ruka» y mi libro, «ruca»; anoto las dos y pregunto». B) ««Ruca» está mal, la borro».", "A", "La A no jerarquiza."),
        ex("Tu copia de «ruka» salió «ruga» y tu modelo dice «ruka». ¿Qué haces: corrijo mi copia o cambio el modelo?", "corrijo mi copia", "Mi copia debe coincidir con mi modelo."),
    ],
    Z=[
        ex("Camila dice: «Una variante es mejor porque la vi primero». ¿Tiene razón? Sí o No.", "No", "Haber visto una primero no la hace mejor."),
        ex("Dos niños discuten qué variante es la correcta. ¿Qué les propones: preguntarle al educador tradicional o votar?", "preguntarle al educador tradicional", "La decisión es de la comunidad."),
    ],
    D=[
        ex("Ordena los pasos: A) pregunto qué forma usa la comunidad. B) anoto las dos formas con su fuente. C) comparo mi copia con mi modelo. Escribe las letras.", "C, B, A", "Comparo, documento y pregunto."),
        ex("En un cartel de tu escuela aparece «pehuén» y en la ficha del curso «pewen». ¿Cuántas formas documentas?", "2", "Una por cada fuente."),
    ],
    context=[ex("El curso hace un cartel y dos niños proponen «ruka» y «ruca». ¿Qué decisión tomas: dejar las dos para preguntar a la educadora o votar cuál es mejor?", "dejar las dos para preguntar a la educadora", "No jerarquizo; consulto.")],
    selfcheck=[
        ex("¿Cómo se llama poner una forma de escribir por encima de otra?", "jerarquizar", "Es lo que no debo hacer."),
        ex("Si dos fuentes escriben distinto, ¿qué hago?", "anoto las dos", "Documentar es respetar."),
        ex("¿A quién pregunto qué variante usar?", "al educador tradicional", "Habla en nombre de la comunidad."),
    ],
    task=T(
        "Revisa este trabajo de práctica. Fichas: libro de la biblioteca «ruka» y «pewen»; cartel de la escuela «ruca» y «pehuén»; ficha del curso «mapuzugun»; texto de un libro «mapudungun». En tu cuaderno haz una tabla de tres filas con las palabras casa mapuche, araucaria y lengua del pueblo mapuche, y escribe en cada fila las formas que viste con su fuente. No marques ninguna como mala. Termina con una pregunta para el educador tradicional sobre qué forma usa su comunidad.",
        "Casa mapuche: ruka (libro), ruca (cartel). Araucaria: pewen (libro), pehuén (cartel). Lengua del pueblo mapuche: mapuzugun (ficha del curso), mapudungun (libro). Pregunta: ¿qué forma usan en su comunidad?",
        ["documenta las dos formas de cada palabra", "anota la fuente de cada una", "no dice que una forma es mala", "formula una pregunta para el educador/a tradicional"],
        ["tabla de tres filas", "pregunta escrita o dicha en voz alta"],
        ["tachar una variante", "olvidar la fuente"],
        "Comprueba que documentó todas las formas sin jerarquizar; si tachó una, ayúdalo a restituirla y a preguntar.",
    ),
    reinforce="Escribe «ruka» y «ruca» juntas con la fuente de cada una.",
    extend="Explica con tus palabras por qué no se debe decir «la variante correcta» entre dos fuentes válidas.",
)

# =================================================================== LS05 clase 1 · propósito de sensibilización
L(
    LS5, 1,
    materials="Lápiz y hoja. Cuando se usen aparatos, siempre con una persona adulta. Los casos de este cuaderno son de práctica.",
    use="Aprenderé a definir para qué quiero hacer un recurso digital que sensibilice a otras personas sobre una cultura y una lengua. Sirve para que mi trabajo tenga un mensaje claro y respetuoso.",
    prior=["Sé que las TIC son aparatos y herramientas para comunicar.", "Sé que las palabras indígenas necesitan fuente y permiso."],
    explain=[
        "Sensibilizar es ayudar a que otras personas conozcan, valoren y respeten algo. Un recurso de sensibilización puede ser un afiche digital, una presentación o un audio corto en castellano que invite a escuchar con respeto a quienes hablan una lengua indígena.",
        "Para definir el propósito respondo tres preguntas. ¿Qué quiero que mi audiencia sepa o sienta? ¿Quiénes son mi audiencia: mi curso, las familias, otro curso? ¿Cuál es mi mensaje central en una sola frase? Por ejemplo: «Escuchar con respeto es una forma de cuidar una lengua».",
        "Un buen propósito no pide imitar ni disfrazarse, no muestra ceremonias y no usa la cultura como un adorno. Se centra en aprender y respetar. Y es corto: si no cabe en una frase, lo simplifico.",
    ],
    vocab=[("sensibilizar", "ayudar a que otros conozcan, valoren y respeten algo"), ("mensaje central", "idea principal del recurso, en una frase"), ("audiencia", "personas que verán o escucharán el recurso"), ("afiche digital", "cartel hecho con un aparato"), ("adorno", "cosa que solo decora y no aporta significado")],
    worked=[
        W("Formular el mensaje central", "Quiero un afiche para otro curso sobre escuchar con respeto. Escribe el mensaje central en una frase.", ["Pienso la idea principal: escuchar con respeto.", "La conecto con el cuidado de la lengua.", "Escribo una sola frase."], "Escuchar con respeto es una forma de cuidar una lengua."),
        W("Definir la audiencia", "El recurso lo verán las familias del curso. ¿Cuál es la audiencia?", ["Leo quiénes lo verán.", "Dice: las familias del curso.", "Esa es la audiencia."], "las familias del curso"),
    ],
    mistakes=[
        M("Poner un propósito que pide disfrazarse o imitar.", "No cuida a la cultura ni a las personas.", "Elijo un propósito de aprender y respetar."),
        M("Escribir un propósito muy largo.", "Se vuelve difícil de recordar.", "Lo resumo en una frase."),
    ],
    R=[
        ex("Sensibilizar es ayudar a conocer, valorar y respetar. ¿Verdadero o falso?", "Verdadero", "Esa es la idea de la clase."),
        ex("El mensaje central, ¿es largo o va en una frase?", "va en una frase", "Es la idea principal."),
        ex("¿Quiénes verán el recurso: la audiencia o los créditos?", "la audiencia", "La audiencia es quien lo ve."),
    ],
    C=[
        ex("Elige el mejor propósito. A) invitar a escuchar con respeto a quienes hablan una lengua indígena. B) disfrazarnos para hacer reír.", "A", "La B usa la cultura como adorno."),
        ex("Mensaje central: «Agradecer es una forma de respeto». ¿Es una frase o varias?", "una frase", "Tiene una sola idea."),
        ex("Si mi audiencia son niños de 6 años, ¿uso frases cortas o muy largas?", "cortas", "Debo adaptarlas a la audiencia."),
    ],
    A=[
        ex("Propósito: sensibilizar a otro curso. Audiencia: otro curso. Mensaje: «Escuchar es participar». ¿Quién verá el recurso?", "otro curso", "Es la audiencia."),
        ex("Para definir el propósito respondes tres preguntas: qué quiero que sepan, quiénes son la audiencia y cuál es el mensaje central. Ya respondiste las dos primeras. ¿Qué te falta?", "el mensaje central", "Es la tercera pregunta."),
        ex("Para sensibilizar con el saludo, ¿qué expresión de la ficha podría ir en un afiche: «mari mari» o «ko»?", "mari mari", "La ficha dice que es un saludo."),
    ],
    Z=[
        ex("Pedro propone que el afiche muestre una ceremonia. ¿Por qué no es un buen propósito: porque expone algo que una comunidad cuida o porque es largo?", "porque expone algo que una comunidad cuida", "Las ceremonias no se muestran."),
        ex("Camila quiere que su afiche «enseñe toda la lengua». ¿Puede en un afiche pequeño? Sí o No.", "No", "Una lengua es enorme y la enseña quien la habla."),
    ],
    D=[
        ex("Ordena para definir el propósito: A) escribo el mensaje central. B) pienso qué quiero que sepan. C) decido la audiencia. Escribe las letras.", "B, C, A", "Pienso, decido y escribo."),
        ex("Elige el mensaje central que respeta esta clase. A) «Escuchemos con respeto». B) «Imitemos todos los sonidos».", "A", "La B invita a imitar."),
    ],
    context=[ex("Tu curso hará un audio de 20 segundos en castellano para otro curso. ¿Qué mensaje central escribes: «Escuchar con respeto cuida una lengua» o «Somos mejores que otros»?", "«Escuchar con respeto cuida una lengua»", "Sensibiliza sin comparar.")],
    selfcheck=[
        ex("¿Qué significa sensibilizar?", "ayudar a conocer, valorar y respetar", "Es el objetivo del recurso."),
        ex("¿En cuántas frases va el mensaje central?", "una", "Debe ser breve."),
        ex("¿Debe un propósito pedir imitar o disfrazarse?", "No", "Eso usa la cultura como adorno."),
    ],
    task=T(
        "Define el propósito de un recurso digital de práctica. Escribe: 1) para qué es (elige: invitar a escuchar con respeto, mostrar un saludo con «mari mari» o agradecer con «chaltumay»), 2) quiénes son tu audiencia (otro curso o las familias del curso), 3) el mensaje central en una frase. " + FICHA_SAL + " Termina con una pregunta para la educadora tradicional sobre si el mensaje es respetuoso.",
        "Propósito: invitar a escuchar con respeto. Audiencia: otro curso. Mensaje: «Escuchar con respeto cuida una lengua». Pregunta: ¿le parece respetuoso este mensaje?",
        ["define propósito, audiencia y mensaje", "el mensaje va en una frase", "no pide imitar ni mostrar ceremonias", "formula una pregunta para el educador/a tradicional"],
        ["tres líneas y una pregunta", "pregunta escrita o dicha en voz alta"],
        ["proponer imitar", "escribir un mensaje muy largo"],
        "Verifica que el mensaje sea una frase y no use la cultura como adorno; si propone imitar, conversen sobre el respeto.",
    ),
    reinforce="Di en voz alta tu mensaje central en menos de diez segundos.",
    extend="Escribe dos mensajes centrales distintos para otras dos audiencias y compáralos.",
)

# =================================================================== LS05 clase 2 · autoría y permiso
L(
    LS5, 2,
    materials="Lápiz y hoja. Los casos de este cuaderno son de práctica; no se descarga ni se publica nada.",
    use="Aprenderé a examinar quién creó cada parte de un recurso y si hay permiso para usarla. Sirve para respetar el trabajo de otras personas y el material que una comunidad cuida.",
    prior=["Sé que un recurso tiene créditos.", "Sé que las palabras necesitan fuente y permiso."],
    explain=[
        "La autoría es saber quién creó algo: un dibujo, una foto, un texto, un audio. Cada creación pertenece a quien la hizo, y para usarla necesito su permiso, que es el sí de esa persona. Mis propios dibujos y textos los puedo usar; los de otros, solo con permiso.",
        "Hay material que además es restringido: una comunidad decide quién puede verlo, escucharlo o copiarlo. Puede ser una grabación, una imagen de un lugar o una práctica que se cuida. Si no tengo certeza de que se puede usar, no lo uso y pregunto al educador o a la educadora tradicional.",
        "Antes de poner algo en mi recurso me hago tres preguntas: ¿Quién lo creó? ¿Tengo su permiso? ¿Es material que una comunidad cuida? Si la respuesta a la segunda es no o a la tercera es sí, lo dejo fuera.",
    ],
    vocab=[("autoría", "saber quién creó algo"), ("permiso", "el sí de quien creó o cuida algo para usarlo"), ("restringido", "que su dueño o su comunidad no permite compartir libremente"), ("créditos", "datos de quién hizo algo"), ("propio", "hecho por mí")],
    worked=[
        W("Examinar cuatro materiales", "Materiales: A) un dibujo hecho por mí. B) una foto que sacó una compañera. C) una grabación de una ceremonia. D) un dibujo de otra escuela. ¿Cuáles puedo usar sin pedir permiso?", ["Mi dibujo lo hice yo.", "Los demás son de otras personas o son material que se cuida.", "Solo A."], "solo A"),
        W("Preguntar por el permiso", "Quiero usar la foto que sacó una compañera. ¿Qué hago?", ["La foto es de ella.", "Necesito su permiso.", "Le pregunto y anoto su nombre en los créditos."], "le pido permiso y la nombro en los créditos"),
    ],
    mistakes=[
        M("Usar una imagen porque la encontré en una pantalla.", "Alguien la creó y puede no permitir su uso.", "Uso mis propios dibujos o pido permiso."),
        M("Usar material de una ceremonia porque es bonito.", "Es material restringido que una comunidad cuida.", "Lo dejo fuera y pregunto."),
    ],
    R=[
        ex("Un dibujo que hice yo, ¿necesita permiso de otra persona? Sí o No.", "No", "Yo soy el autor."),
        ex("Una foto que sacó mi compañera, ¿necesita su permiso? Sí o No.", "Sí", "Ella es la autora."),
        ex("¿Cómo se llama saber quién creó algo: autoría o título?", "autoría", "Es el dato del creador."),
    ],
    C=[
        ex("Verdadero o falso: si encuentro una imagen en una pantalla, puedo usarla sin preguntar.", "Falso", "Alguien la creó."),
        ex("Una grabación de una ceremonia es material restringido. ¿Puedo ponerla en mi recurso? Sí o No.", "No", "Una comunidad decide quién la comparte."),
        ex("Tres preguntas: ¿Quién lo creó?, ¿Tengo permiso?, ¿Es material que una comunidad cuida? Si la segunda respuesta es no, ¿lo uso?", "No", "Sin permiso no lo uso."),
    ],
    A=[
        ex("Tu recurso usa: 1) un texto tuyo, 2) un dibujo tuyo, 3) una foto de una compañera. ¿Qué material necesita permiso antes de usarse?", "la foto de la compañera (el 3)", "Es la única que no hiciste tú."),
        ex("Materiales: A) texto mío. B) dibujo de un compañero con su permiso. C) foto de un lugar sagrado sin permiso. ¿Cuáles puedes usar? Escribe las letras.", "A y B", "La C es material restringido sin permiso."),
        ex("Créditos: «Dibujos: Pía y el curso. Palabras: ficha de la educadora». ¿Se nombran las autorías? Sí o No.", "Sí", "Dice quién hizo cada parte."),
    ],
    Z=[
        ex("Ana dice: «Si es para el colegio, puedo usar cualquier imagen». ¿Tiene razón? Sí o No.", "No", "Aunque sea para el colegio, se pide permiso y se nombra a quien la creó."),
        ex("Un niño no sabe si una grabación se puede usar. ¿Qué hace: la usa igual o pregunta al educador tradicional?", "pregunta al educador tradicional", "En la duda no la uso."),
    ],
    D=[
        ex("Ordena los pasos: A) pido permiso o la dejo fuera. B) veo quién lo creó. C) pienso si es material que se cuida. Escribe las letras.", "B, C, A", "Autoría, restricción y decisión."),
        ex("Tienes 4 materiales: 1) una grabación de una ceremonia, 2) un dibujo tuyo, 3) y 4) dibujos de compañeros que dieron permiso. ¿Cuál dejas fuera?", "el 1: la grabación de la ceremonia", "Es material restringido que una comunidad cuida."),
    ],
    context=[ex("Para un afiche quieres una foto de personas bailando que viste en una pantalla. ¿Qué haces: la usas o usas un dibujo tuyo?", "uso un dibujo mío", "Mis dibujos son propios y no hay riesgo.")],
    selfcheck=[
        ex("¿Quién necesita dar el permiso para usar una foto?", "quien la creó", "Es su autor."),
        ex("¿Qué hago con el material restringido?", "lo dejo fuera", "Una comunidad decide sobre él."),
        ex("¿Puedo usar mis propios dibujos?", "Sí", "Yo soy el autor."),
    ],
    task=T(
        "Examina esta lista de materiales de práctica para un recurso digital: 1) un dibujo tuyo del agua, 2) un dibujo de un compañero (él dice que sí), 3) una foto de un lugar que una comunidad cuida, 4) la palabra «ko» de la ficha. Para cada material escribe quién lo creó, si hay permiso y si lo usarías. " + FICHA_PAL + " Termina con una pregunta para la educadora tradicional sobre qué material no se debería usar.",
        "1) Lo creé yo; no necesita permiso; lo uso. 2) Lo creó mi compañero; tiene permiso; lo uso con crédito. 3) No es mío; es material que se cuida; lo dejo fuera. 4) La ficha; fuente: ficha de la clase; lo uso. Pregunta: ¿qué imágenes no se deben usar?",
        ["responde quién creó cada material", "dice si hay permiso", "deja fuera el material que se cuida", "formula una pregunta para el educador/a tradicional"],
        ["tabla de cuatro materiales", "pregunta escrita o dicha en voz alta"],
        ["usar el material restringido", "olvidar los créditos"],
        "Comprueba que deja fuera el material restringido; si lo usó, conversen sobre quién decide sobre él.",
    ),
    reinforce="Elige un dibujo tuyo para un recurso y escribe «Autor: yo».",
    extend="Haz una lista de tres cosas que pedirías permiso para usar y a quién se lo pedirías.",
)

# =================================================================== LS05 clase 3 · palabras contextualizadas
L(
    LS5, 3,
    materials="Lápiz y hoja. La ficha está escrita en este cuaderno.",
    use="Aprenderé a seleccionar pocas palabras para un recurso y a ponerlas en su contexto, con significado y fuente. Sirve para que las palabras no sean adorno y se entiendan.",
    prior=["Sé examinar autoría y permiso.", "Sé que la ficha da el significado de cada palabra."],
    explain=[
        "Contextualizar una palabra es ponerla donde se entiende: junto a su significado, en una frase y con su fuente. En un recurso no pongo una palabra suelta; la acompaño con una frase como «En mapuzugun, «ko» es agua (Fuente: ficha de la clase)».",
        "Selecciono pocas palabras, dos o tres, que sirvan al mensaje central. Si mi mensaje es agradecer, elijo «chaltumay». Si es saludar, elijo «mari mari». Elegir pocas me permite explicar cada una bien y evita llenar el recurso de palabras sin sentido.",
        "No uso palabras que no estén en mi ficha ni invento frases en lengua indígena. Si quiero una palabra más, la anoto como pregunta para la educadora tradicional y no la pongo en el recurso hasta que ella la revise.",
    ],
    vocab=[("contextualizar", "poner una palabra donde se entienda, con su significado y su fuente"), ("seleccionar", "elegir entre varias cosas"), ("mensaje central", "idea principal del recurso"), ("acompañar", "poner junto a algo"), ("suelta", "sin explicación")],
    worked=[
        W("Elegir según el mensaje", "Mensaje central: agradecer. " + "Ficha: «mari mari» es saludo, «chaltumay» es gracias, «ko» es agua. ¿Qué palabra eliges?", ["El mensaje es agradecer.", "La ficha dice que «chaltumay» es gracias.", "Elijo «chaltumay»."], "«chaltumay»"),
        W("Contextualizar", "Quieres mostrar «ko» en tu recurso. Escribe una línea contextualizada.", ["Escribo la palabra y su lengua.", "Agrego el significado: agua.", "Pongo la fuente."], "En mapuzugun, «ko» es agua (Fuente: ficha de la clase)."),
    ],
    mistakes=[
        M("Poner una palabra sin su significado ni su fuente.", "Queda como adorno.", "La acompaño con una frase y la fuente."),
        M("Poner muchas palabras para que se vea más completo.", "No alcanzo a explicar cada una.", "Elijo dos o tres."),
    ],
    R=[
        ex("Contextualizar es poner una palabra con su significado y su fuente. ¿Verdadero o falso?", "Verdadero", "Así se entiende la palabra."),
        ex("Mensaje central: saludar. " + FICHA_SAL + " ¿Qué palabra eliges?", "mari mari", "Es el saludo."),
        ex("¿Cuántas palabras selecciono para un recurso corto: dos o tres, o treinta?", "dos o tres", "Así puedo explicarlas bien."),
    ],
    C=[
        ex("¿Cuál línea está contextualizada? A) «ko». B) En mapuzugun, «ko» es agua (Fuente: ficha de la clase).", "B", "Tiene lengua, significado y fuente."),
        ex("Verdadero o falso: puedo agregar una palabra que no está en la ficha si me parece bonita.", "Falso", "Debo preguntar primero."),
        ex("Mensaje central: agradecer a la visita. ¿Qué palabra de la ficha de saludos eliges: «mari mari» o «chaltumay»?", "chaltumay", "Según la ficha quiere decir gracias."),
    ],
    A=[
        ex("¿Cuál es la línea contextualizada para «antü» según la ficha? A) En mapuzugun, «antü» es sol (Fuente: ficha de la clase). B) En mapuzugun, «antü» es luna (Fuente: ficha de la clase).", "A", "La ficha dice que «antü» es sol."),
        ex("Tu mensaje central es saludar. Escoges «mari mari» y también agregas «ko» sin relación con el mensaje. ¿Qué problema tiene «ko» en tu recurso?", "no sirve al mensaje central y queda como adorno", "Las palabras se eligen según el mensaje."),
        ex("Mensaje central: cuidar el agua. " + FICHA_PAL + " ¿Qué palabra de la ficha eliges?", "ko", "Ko es agua."),
    ],
    Z=[
        ex("Un compañero pone en su afiche cinco palabras sin significado. ¿Qué problema tiene: son adorno o son pocas?", "son adorno", "Sin significado no se entienden."),
        ex("Lucía quiere inventar una frase en lengua indígena para el afiche. ¿Qué haces: se la cambio por una pregunta para la educadora o la dejo?", "se la cambio por una pregunta para la educadora", "No se inventan frases en lengua indígena."),
    ],
    D=[
        ex("Ordena los pasos: A) escribo la línea contextualizada. B) elijo dos palabras. C) repaso mi mensaje central. Escribe las letras.", "C, B, A", "Repaso, elijo y escribo."),
        ex("Mensaje: saludar y agradecer. Elige las dos palabras: A) «mari mari» y «chaltumay». B) «ko» y «antü».", "A", "Una saluda y la otra agradece."),
    ],
    context=[ex("Preparas un audio en castellano de 20 segundos para otro curso y quieres incluir una palabra. ¿Qué dices: «Según la ficha, «ko» es agua en mapuzugun» o solo «ko»?", "«Según la ficha, «ko» es agua en mapuzugun»", "Contextualiza la palabra.")],
    selfcheck=[
        ex("¿Qué acompaña a una palabra contextualizada: significado y fuente, o un adorno?", "significado y fuente", "Así se entiende."),
        ex("¿Cuántas palabras selecciono: pocas o muchas?", "pocas", "Así las explico bien."),
        ex("¿Puedo inventar frases en lengua indígena?", "No", "Pregunto a la educadora."),
    ],
    task=T(
        "Para el mensaje central «Escuchar con respeto cuida una lengua» selecciona dos palabras de la ficha de saludos o de la ficha de palabras y escribe una línea contextualizada para cada una. " + FICHA_SAL + " " + FICHA_PAL + " Cada línea debe tener la lengua, el significado y la fuente. Escribe también una palabra que te gustaría usar y que no esté en las fichas, como una pregunta para la educadora tradicional.",
        "En mapuzugun, «mari mari» es un saludo (Fuente: ficha de la clase). En mapuzugun, «chaltumay» es gracias (Fuente: ficha de la clase). Pregunta: ¿podríamos usar otra palabra para despedirnos?",
        ["selecciona dos palabras de las fichas", "cada línea tiene lengua, significado y fuente", "no agrega palabras sin ficha", "formula una pregunta para el educador/a tradicional"],
        ["dos líneas contextualizadas", "pregunta escrita o dicha en voz alta"],
        ["poner palabras sueltas", "inventar una frase en lengua indígena"],
        "Verifica que cada línea tenga fuente y significado; si agregó una palabra sin ficha, pídele que la anote como pregunta.",
    ),
    reinforce="Lee en voz alta, con tu voz en castellano, una línea contextualizada de tu tarea.",
    extend="Contextualiza una tercera palabra de la ficha y compara con las dos primeras.",
)

# =================================================================== LS05 clase 4 · crear sin apropiarse
L(
    LS5, 4,
    materials="Lápiz, hojas y colores. Si se usa un aparato, con una persona adulta. Los diseños se hacen con dibujos propios.",
    use="Aprenderé a crear un recurso con mis propias ideas, sin copiar símbolos, diseños, trajes o prácticas de una cultura. Sirve para sensibilizar con respeto y sin apropiarme de lo que no es mío.",
    prior=["Sé examinar autoría y permiso.", "Sé qué es apropiarse."],
    explain=[
        "Crear sin apropiarse es hacer mi recurso con mis ideas, mis dibujos y mis textos, y usar de la cultura solo lo que tengo con fuente y permiso. Apropiarse es tomar como propios símbolos, diseños, trajes, cantos o prácticas de otros, sin permiso ni crédito, o cambiarles el sentido.",
        "Por eso no copio dibujos, símbolos ni diseños de tejidos o de adornos de un pueblo. No me disfrazo ni hago una «ceremonia» para el video. No uso música ni canciones de otros sin permiso. Mis dibujos son sencillos y propios: una jarra, un sol, una casita, con mi estilo.",
        "Lo que sí hago es mostrar mi aprendizaje: una palabra con su significado y su fuente, un saludo de la ficha, un agradecimiento. Y reconozco que esas palabras vienen de personas y comunidades que las cuidan.",
    ],
    vocab=[("apropiarse", "tomar como propio lo de otros sin permiso ni crédito"), ("símbolo", "dibujo o signo que representa una idea"), ("diseño", "forma o dibujo creado por alguien"), ("disfraz", "ropa que imita a otra persona o cultura"), ("propio", "hecho por mí")],
    worked=[
        W("Elegir sin apropiarse", "Para un afiche: A) copiar un diseño de un adorno de un pueblo. B) dibujar una jarra con mi estilo. ¿Cuál es mejor?", ["A copia un diseño creado por otros.", "B es mi creación.", "Elijo B."], "B"),
        W("Reconocer lo que sí puedo hacer", "Quiero mostrar lo aprendido. ¿Qué incluyo: una palabra de la ficha con su fuente o un disfraz?", ["La palabra tiene fuente.", "El disfraz imita a otra cultura.", "Incluyo la palabra con su fuente."], "la palabra de la ficha con su fuente"),
    ],
    mistakes=[
        M("Copiar un diseño porque se ve bonito.", "Es una creación de otros y puede tener sentido que no conozco.", "Dibujo algo mío."),
        M("Disfrazarme para el video.", "Imito a otra cultura y puede ser una burla.", "Muestro mi aprendizaje con mi propia ropa."),
    ],
    R=[
        ex("Dibujar una jarra con mi propio estilo, ¿es apropiarse? Sí o No.", "No", "Es mi creación."),
        ex("Copiar un diseño de un adorno de un pueblo, ¿es una creación propia? Sí o No.", "No", "Lo creó otra persona."),
        ex("Un disfraz que imita a otra cultura, ¿ayuda a sensibilizar o puede ser burla?", "puede ser burla", "Imita sin conocer."),
    ],
    C=[
        ex("Verdadero o falso: puedo usar música de otros en mi recurso si me gusta.", "Falso", "Necesito el permiso de sus autores."),
        ex("Elige lo que sí puedo hacer. A) mostrar una palabra con su significado y fuente. B) copiar un símbolo de un pueblo.", "A", "La B copia lo de otros."),
        ex("¿Cuál recurso respeta esta clase? A) dibujos míos y una palabra con fuente. B) un video con disfraces.", "A", "Usa creaciones propias y fuente."),
    ],
    A=[
        ex("Tu recurso tiene un dibujo propio de un sol y un dibujo copiado de un diseño de tejido de un pueblo. ¿Cuál debes cambiar o dejar fuera?", "el dibujo copiado del diseño de tejido", "Es una creación de otros que no usé con permiso."),
        ex("Materiales: A) mi dibujo de un sol. B) un símbolo de un diseño que vi. C) la palabra «antü» de la ficha. ¿Cuáles puedes usar? Escribe las letras.", "A y C", "El B copia un diseño de otros."),
        ex("Quieres mostrar el saludo. " + FICHA_SAL + " ¿Qué incluyes: «mari mari» con su fuente o una ceremonia actuada?", "«mari mari» con su fuente", "No actúo ceremonias."),
    ],
    Z=[
        ex("Ana dice: «Si copio un símbolo, hago homenaje». ¿Qué le respondes: que copiar sin permiso es apropiarse o que tiene razón?", "que copiar sin permiso es apropiarse", "Un homenaje no reemplaza el permiso."),
        ex("Tomás quiere cantar una canción de una comunidad en su audio sin preguntar. ¿Es adecuado? Sí o No.", "No", "Necesita permiso y fuente."),
    ],
    D=[
        ex("Ordena los pasos: A) uso solo mis dibujos y palabras con fuente. B) pienso qué parte es mía. C) reviso que no copio símbolos ni disfraces. Escribe las letras.", "B, A, C", "Pienso, uso lo mío y reviso."),
        ex("Elige el mejor plan. A) dibujo mío, palabra con fuente, créditos. B) símbolo copiado, canción sin permiso.", "A", "El B se apropia de lo de otros."),
    ],
    context=[ex("Tu curso hará un video para otro curso. Un niño propone usar plumas y pintura en la cara «para que se vea auténtico». ¿Qué propones: usar la ropa de siempre y mostrar una palabra con fuente, o hacer lo que propone?", "usar la ropa de siempre y mostrar una palabra con fuente", "Los disfraces pueden ser burla.")],
    selfcheck=[
        ex("En un recurso digital, ¿qué significa apropiarse de algo?", "tomar como propio lo de otros sin permiso ni crédito", "Es lo que no debo hacer."),
        ex("¿Qué uso en mi recurso: dibujos propios o diseños copiados?", "dibujos propios", "Así creo sin apropiarme."),
        ex("¿Me disfrazo para el video?", "No", "Puede ser una burla."),
    ],
    task=T(
        "Planea en papel tu recurso de sensibilización con estas partes: 1) un dibujo propio y sencillo (por ejemplo, una jarra con agua o un sol), 2) una línea contextualizada con una palabra de la ficha (" + FICHA_PAL + "), 3) los créditos con tu nombre como autor del dibujo y la ficha como fuente de la palabra. Escribe también tres cosas que NO usarás, por ejemplo símbolos copiados, disfraces o música de otros. Termina con una pregunta para la educadora tradicional.",
        "Dibujo: una jarra con agua (autor: yo). Línea: En mapuzugun, «ko» es agua (Fuente: ficha de la clase). No usaré: símbolos copiados, disfraces, música de otros. Pregunta: ¿qué otra cosa no deberíamos usar?",
        ["el dibujo es propio", "la palabra tiene significado y fuente", "escribe tres cosas que no usará", "formula una pregunta para el educador/a tradicional"],
        ["plan en papel", "pregunta escrita o dicha en voz alta"],
        ["copiar un símbolo", "proponer un disfraz"],
        "Verifica que el dibujo sea propio y que la palabra tenga fuente; si propone un disfraz, conversen sobre el respeto.",
    ),
    reinforce="Dibuja en tu cuaderno un sol a tu manera y escribe debajo «Autor: yo».",
    extend="Explica a un adulto por qué un homenaje no reemplaza el permiso.",
)

# =================================================================== LS05 clase 5 · atribución y audiencia
L(
    LS5, 5,
    materials="Lápiz y hoja. Los casos de este cuaderno son de práctica; no se publica nada abiertamente.",
    use="Aprenderé a revisar la atribución y la audiencia de mi recurso antes de mostrarlo. Sirve para dar créditos completos y cuidar quién puede verlo.",
    prior=["Sé examinar autoría y permiso.", "Sé crear sin apropiarme."],
    explain=[
        "Revisar la atribución es comprobar que mis créditos dicen todo: quién hizo los dibujos y textos, de dónde vienen las palabras en lengua indígena y para qué se hizo el recurso. Si falta uno de estos datos, lo agrego antes de mostrar el recurso.",
        "Revisar la audiencia es comprobar que el recurso es adecuado para quienes lo verán. Si lo verán niños pequeños, uso frases cortas. Si lo verán familias, lo aviso antes. Y si lo verá otro curso, lo muestro solo si el permiso lo permite. Un recurso con palabras de una lengua indígena no se publica abierto sin permiso.",
        "Por último, estoy dispuesto a retirar o cambiar el recurso si la educadora o la comunidad lo pide. Cuidar significa también aceptar una corrección sin enojarme. Mostrar el recurso no es el final: es el comienzo de una conversación respetuosa.",
    ],
    vocab=[("atribución", "decir quién hizo cada cosa y de dónde viene"), ("audiencia", "personas que verán o escucharán el recurso"), ("retirar", "sacar algo para que ya no se vea"), ("adecuado", "que es apropiado para quienes lo ven"), ("corrección", "cambio para mejorar algo")],
    worked=[
        W("Revisar créditos", "Créditos: «Dibujos: el curso. Palabras: ficha de la clase. Propósito: sensibilizar a otro curso.» ¿Dicen quién hizo los dibujos, la fuente de las palabras y el propósito?", ["Dibujos: el curso, sí.", "Palabras: ficha de la clase, sí.", "Propósito: sí."], "Sí, los tres datos"),
        W("Aceptar una corrección", "La educadora dice que una palabra del recurso debe quitarse por ahora. ¿Qué haces: la quitas o discutes?", ["Ella es la fuente.", "Retirar la palabra es parte de cuidar.", "La quito y anoto una pregunta."], "la quito y anoto una pregunta"),
    ],
    mistakes=[
        M("Mostrar el recurso sin revisar los créditos.", "Puede faltar la fuente o la autoría.", "Reviso los tres datos antes de mostrar."),
        M("Enojarme si me piden un cambio.", "La corrección ayuda a cuidar la lengua.", "Acepto, cambio y agradezco."),
    ],
    R=[
        ex("Los créditos dicen quién hizo cada cosa y de dónde viene. ¿Es atribución? Sí o No.", "Sí", "Atribuir es dar créditos."),
        ex("Si la educadora pide quitar una palabra, ¿la quito o discuto?", "la quito", "Ella es la fuente."),
        ex("Un recurso con palabras indígenas, ¿se publica abierto sin permiso? Sí o No.", "No", "Se necesita permiso."),
    ],
    C=[
        ex("Verdadero o falso: antes de mostrar mi recurso reviso los créditos y la audiencia.", "Verdadero", "Es el último paso de la revisión."),
        ex("Créditos A: «Dibujos: Pía. Palabras: ficha de la clase.» Créditos B: «Hecho por Pía.» ¿Cuáles dicen la fuente de las palabras?", "A", "El B no menciona la ficha."),
        ex("Si mi audiencia son niños pequeños, ¿uso frases cortas o largas?", "cortas", "Debe ser adecuado."),
    ],
    A=[
        ex("Tu lista de revisión tiene cinco puntos: dibujos, palabras, propósito, audiencia y permiso. Ya revisaste todos menos el permiso. ¿Qué punto falta?", "el permiso", "Es el único punto sin revisar."),
        ex("El permiso dice: «solo para las familias del curso». Quieres mostrarlo a otro curso. ¿Puedes? Sí o No.", "No", "El permiso limita la audiencia."),
        ex("Elige los créditos completos. A) Dibujos: yo; palabra: ficha de la clase; propósito: sensibilizar. B) Dibujos: yo.", "A", "La A tiene los tres datos."),
    ],
    Z=[
        ex("Camila dice: «Ya lo mostré, no hay nada más que revisar». ¿Qué le falta aceptar: que puede haber correcciones o que ya terminó todo?", "que puede haber correcciones", "Mostrar es el comienzo de la conversación."),
        ex("Un niño quiere subir el recurso a un sitio abierto para que más gente lo vea. ¿Qué falta primero: el permiso o más dibujos?", "el permiso", "Sin permiso no se publica."),
    ],
    D=[
        ex("Ordena los pasos: A) muestro el recurso a la audiencia permitida. B) reviso créditos. C) reviso la audiencia y el permiso. Escribe las letras.", "B, C, A", "Reviso todo y luego muestro."),
        ex("La educadora pidió dos correcciones: cambiar una palabra y agregar la fuente en los créditos. Ya cambiaste la palabra. ¿Qué te falta?", "agregar la fuente en los créditos", "Es la segunda corrección pedida."),
    ],
    context=[ex("Terminaste tu afiche de práctica y la educadora te pide cambiar una palabra. Tus compañeros ya lo aplaudieron. ¿Qué haces: lo cambias con gusto o lo dejas porque ya gustó?", "lo cambias con gusto", "Cuidar la lengua es más importante que el aplauso.")],
    selfcheck=[
        ex("¿Qué revisa la atribución?", "que los créditos digan quién hizo cada cosa y de dónde viene", "Es el objetivo de la atribución."),
        ex("¿Qué hago si me piden retirar algo?", "lo retiro", "Cuido la lengua."),
        ex("¿Quién fija la audiencia si hay permiso?", "el permiso", "Dice quiénes pueden verlo."),
    ],
    task=T(
        "Haz una revisión final de práctica de tu recurso con esta lista de cinco puntos: 1) créditos de dibujos, 2) fuente de las palabras, 3) propósito, 4) audiencia, 5) permiso. Escribe sí o no a cada punto y una frase corta de corrección si falta alguno. " + FICHA_SAL + " Escribe unos créditos de dos líneas para tu recurso. Termina con una pregunta para la educadora tradicional sobre si puedes mostrarlo a otro curso.",
        "1 sí; 2 sí; 3 sí; 4 sí (otro curso); 5 no, falta preguntar. Créditos: Dibujos: yo. Palabras: ficha de la clase. Propósito: sensibilizar a otro curso. Pregunta: ¿puedo mostrarlo a otro curso?",
        ["responde los cinco puntos", "escribe créditos completos", "señala lo que falta", "formula una pregunta para el educador/a tradicional"],
        ["lista de revisión y créditos", "pregunta escrita o dicha en voz alta"],
        ["publicar sin permiso", "olvidar la fuente"],
        "Verifica que los créditos incluyan la fuente y que no se publique sin permiso; si falta el permiso, ayúdalo a formular la pregunta.",
    ),
    reinforce="Cuenta a un adulto tus cinco puntos de revisión y marca cuál falta.",
    extend="Escribe una nota de agradecimiento a la educadora por las correcciones a tu recurso.",
)
