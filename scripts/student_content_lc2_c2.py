"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS01 (relatos orales breves y palabras culturalmente significativas) y LS02 (descripción oral del medio natural
y de los mensajes de la naturaleza).

Criterio de autoría: todos los relatos y observaciones son textos de práctica inventados y se declaran como tales;
no se reproduce ni se adapta ningún relato tradicional. Las palabras en lengua indígena se limitan a las muy
atestiguadas (mari mari, chaltumay, ko, antü, kuyen, mapu, lafken, pewen, epew) y a palabras del castellano de origen
indígena (copihue, pudú). No se inventan significados rituales ni espirituales: la lectura de las señales de la
naturaleza y los relatos propios de cada pueblo los explican el educador/a tradicional y la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS1, LS2 = "LC02 OA LS01", "LC02 OA LS02"

CONSULT = " Recuerda: los relatos tradicionales y la forma de leer la naturaleza de cada pueblo los enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

RELATO_EMA = ("Relato de práctica (inventado, no es un relato tradicional): Ema vivía cerca de un bosque. Una mañana encontró un copihue rojo en el suelo. "
              "Se lo llevó a su abuela. La abuela le dijo: «Las flores se cuidan en su lugar». Ema devolvió el copihue al bosque. Después, otras flores se abrieron.")
FICHA_PAL = "Ficha de palabras en mapuzugun: «ko» es agua, «antü» es sol, «kuyen» es luna, «mapu» es tierra, «lafken» es mar, «pewen» es la araucaria."


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


# =================================================================== LS01 · relatos orales breves
L(
    LS1, 1,
    materials="Lápiz, hoja y un adulto que lea en voz alta el relato de práctica escrito aquí. Es un texto inventado para practicar la escucha, no un relato de ningún pueblo.",
    use="Aprenderé a escuchar un relato oral con atención y respeto. Sirve para disfrutar las historias de los pueblos y para recordar qué pasó.",
    prior=["Sé escuchar a otra persona sin interrumpir.", "Sé contestar preguntas sobre quién, dónde y qué pasó."],
    explain=[
        "Un relato oral es una historia que se cuenta con la voz. Muchos pueblos originarios guardan sus historias de esta manera: las personas mayores las cuentan y los niños las escuchan. Por eso saber escuchar es muy importante.",
        "Para escuchar con respeto hago cuatro cosas. Me siento tranquilo. Miro a quien cuenta. No interrumpo ni me río de lo que no entiendo. Y espero al final para preguntar. Si no entiendo algo, lo anoto y lo pregunto después.",
        "Mientras escucho, me hago tres preguntas: ¿quién es el personaje?, ¿dónde ocurre? y ¿qué pasa al final? Si hay una palabra especial, la escribo. Si el relato es de un pueblo, quien lo cuenta es quien conoce y puede compartirlo, y yo lo respeto.",
    ],
    vocab=[("relato oral", "historia que se cuenta con la voz"), ("personaje", "quien participa en la historia"), ("escuchar", "poner atención a lo que otro dice"), ("interrumpir", "hablar cuando otro todavía está hablando"), ("respeto", "tratar con cuidado lo que importa a otros")],
    worked=[
        W("Escuchar y responder", RELATO_EMA + " ¿Quién es el personaje principal?", ["Busco a quién le pasan las cosas.", "Ema encontró el copihue y lo devolvió.", "El personaje principal es Ema."], "Ema"),
        W("Qué hace quien escucha", "Mientras la abuela cuenta un relato, Pedro quiere contar un chiste. ¿Qué hace quien escucha con respeto?", ["Pienso en las cuatro cosas: tranquilo, mirar, no interrumpir, preguntar al final.", "Contar un chiste es interrumpir.", "Espero y pregunto después."], "esperar y preguntar al final"),
    ],
    mistakes=[
        M("Interrumpir para contar otra cosa.", "Pierdo parte del relato y no respeto a quien cuenta.", "Espero al final para preguntar o comentar."),
        M("Reírme cuando no entiendo una palabra.", "La palabra puede ser importante para quien cuenta.", "La anoto y la pregunto con respeto."),
    ],
    R=[
        ex(RELATO_EMA + " ¿Quién encontró el copihue?", "Ema", "El texto dice que Ema lo encontró."),
        ex(RELATO_EMA + " ¿Dónde vivía Ema: cerca de un bosque o cerca del mar?", "cerca de un bosque", "El texto dice «Ema vivía cerca de un bosque»."),
        ex("Cuando alguien cuenta un relato, ¿escucho o interrumpo?", "escucho", "Escuchar es la forma de respetar."),
    ],
    C=[
        ex(RELATO_EMA + " ¿Qué hizo Ema con el copihue al final?", "lo devolvió al bosque", "El texto dice que Ema devolvió el copihue al bosque."),
        ex("Verdadero o falso: puedo reírme de lo que no entiendo mientras alguien cuenta un relato.", "Falso", "Debo escuchar con respeto y preguntar después."),
        ex(RELATO_EMA + " ¿Qué le dijo la abuela a Ema?", "las flores se cuidan en su lugar", "La abuela dijo: «Las flores se cuidan en su lugar»."),
    ],
    A=[
        ex("Ordena lo que hace quien escucha con respeto: A) pregunta al final B) se sienta tranquilo C) mira a quien cuenta. Escribe las letras en orden.", "B, C, A", "Primero se sienta tranquilo, luego mira y al final pregunta."),
        ex(RELATO_EMA + " ¿Qué palabra especial del relato nombra la flor roja?", "copihue", "El texto dice que Ema encontró un copihue rojo."),
        ex(RELATO_EMA + " Ordena los hechos: 1) Ema devuelve el copihue 2) Ema encuentra el copihue 3) otras flores se abren. Escribe los números en orden.", "2, 1, 3", "Primero lo encuentra, luego lo devuelve y después se abren flores."),
    ],
    Z=[
        ex("Beto dice: «Mientras cuentan, yo cuento lo mío para que no se olvide». ¿Es buena idea? Responde Sí o No.", "No", "Interrumpir le quita atención a quien cuenta."),
        ex("En el relato de Ema, ¿por qué crees que la abuela dice que las flores se cuidan en su lugar? Elige: A) para que Ema cuide la naturaleza B) para que Ema se enoje.", "A", "El consejo trata de cuidar la naturaleza, no de enojar."),
    ],
    D=[
        ex("El relato de Ema tiene 6 oraciones. Escuchas 4 y te distraes en las otras. ¿Cuántas oraciones no escuchaste?", "2", "6 − 4 = 2 oraciones."),
        ex(RELATO_EMA + " Si quisieras contárselo a tu familia, ¿qué debes decir primero: «Es mi relato» o «Es un relato de práctica inventado»?", "«Es un relato de práctica inventado»", "El texto dice que es inventado."),
    ],
    context=[ex("Tu abuela empieza a contar una historia familiar mientras cenan. Quieres hacer una pregunta en la mitad. ¿Qué haces: interrumpes ahora o anotas la duda y preguntas al final?", "anoto la duda y pregunto al final", "Así escucho con respeto y no pierdo la pregunta.")],
    selfcheck=[
        ex("¿Qué es un relato oral?", "una historia que se cuenta con la voz", "Se cuenta hablando."),
        ex("¿Cuándo hago mis preguntas: al final o a la mitad?", "al final", "No interrumpo a quien cuenta."),
        ex("Nombra una de las tres preguntas para entender un relato.", "¿quién?, ¿dónde? o ¿qué pasa al final?", "Esas preguntas ayudan a comprender."),
    ],
    task=T(
        "Pide a un adulto que lea en voz alta el relato de práctica de Ema. Escucha sin interrumpir. Después responde en tu cuaderno con dibujos o palabras: ¿Quién es el personaje? ¿Dónde ocurre? ¿Qué pasa al final? Finalmente escribe una cosa que hiciste para escuchar con respeto.",
        "Personaje: Ema. Lugar: cerca de un bosque. Final: devolvió el copihue y las flores se abrieron. Escuché en silencio.",
        ["responde las tres preguntas con el relato", "no inventa hechos", "nombra una forma de escuchar con respeto"],
        ["respuestas en el cuaderno", "dibujo de la escena final"],
        ["inventar partes que no están", "decir que es un relato tradicional"],
        "Valora que escuchó completo; si inventó un hecho, vuelve al texto y pídele que lo compruebe.",
    ),
    reinforce="Cuenta a alguien en una frase quién es Ema y qué hizo con el copihue.",
    extend="Pide a alguien mayor de tu familia que te cuente una historia breve y practica la escucha con las cuatro reglas.",
)

L(
    LS1, 2,
    materials="Lápiz y hoja. Las fichas de fuente están escritas aquí y son inventadas para practicar; en la vida real la fuente es una persona de la comunidad o un material autorizado.",
    use="Aprenderé a reconocer quién cuenta un relato y de qué pueblo viene. Sirve para valorar que cada relato tiene dueños y no se cambia ni se usa de cualquier manera.",
    prior=["Sé escuchar un relato con respeto.", "Sé qué es una fuente."],
    explain=[
        "Los relatos de los pueblos originarios pertenecen a sus comunidades. Los cuentan personas que los han recibido de sus mayores. Por eso, antes de aprender un relato, pregunto cuatro cosas: ¿de qué pueblo es?, ¿quién lo cuenta?, ¿dónde se cuenta? y ¿se puede compartir?",
        "En mapuzugun, la lengua del pueblo mapuche, existe la palabra «epew» para un relato o cuento tradicional. Cada pueblo tiene sus propias palabras y formas de contar. Lo que sé de una cultura no sirve para todas las demás. Los detalles del relato los explica quien lo conoce.",
        "Una ficha de fuente me ayuda a ordenar esas cuatro preguntas. Si falta un dato, no lo invento: lo marco con un signo de pregunta y lo consulto al educador o a la educadora tradicional.",
    ],
    vocab=[("pueblo", "grupo de personas con historia, lengua y cultura propias"), ("narrador", "quien cuenta el relato"), ("tradición", "lo que se transmite de generación en generación"), ("comunidad", "grupo de personas que comparte una cultura"), ("epew", "palabra del mapuzugun para un relato o cuento tradicional")],
    worked=[
        W("Leer la ficha", "Ficha de fuente (inventada): Pueblo: mapuche. Narradora: una educadora tradicional de una escuela. Lugar: la sala. Se puede compartir: sí, en la escuela. ¿Quién cuenta el relato?", ["Busco la palabra «Narradora».", "Leo: una educadora tradicional de una escuela.", "Ella cuenta el relato."], "una educadora tradicional de una escuela"),
        W("Un dato que falta", "Ficha de fuente (inventada): Pueblo: ?. Narrador: un abuelo de la comunidad. Lugar: un patio. ¿Qué dato falta?", ["Reviso los cuatro datos.", "El pueblo tiene un signo de pregunta.", "Falta saber de qué pueblo es."], "falta el pueblo"),
    ],
    mistakes=[
        M("Pensar que un relato puede contarse en cualquier lugar y a cualquiera.", "Algunos relatos se cuentan en ciertas ocasiones y los cuida su comunidad.", "Pregunto si se puede compartir y dónde."),
        M("Inventar el pueblo de un relato.", "Cada relato viene de un pueblo y no puedo suponerlo.", "Marco el dato con «?» y lo consulto."),
    ],
    R=[
        ex("Ficha de fuente: «Pueblo: rapa nui». ¿Qué dato me da: el pueblo o el narrador?", "el pueblo", "La ficha dice de qué pueblo es."),
        ex("¿Cómo se llama quien cuenta un relato: narrador o dibujante?", "narrador", "El narrador es quien cuenta."),
        ex("En mapuzugun, ¿qué palabra se usa para un relato o cuento tradicional: «epew» o «ko»?", "epew", "«Epew» es la palabra para relato; «ko» es agua."),
    ],
    C=[
        ex("Verdadero o falso: todos los pueblos cuentan sus relatos de la misma manera.", "Falso", "Cada pueblo tiene sus propias formas de contar."),
        ex("Ficha: «Narrador: abuelo de la comunidad. Se puede compartir: solo en la escuela». ¿Dónde se puede compartir?", "en la escuela", "La ficha lo dice."),
        ex("Si en la ficha aparece «Pueblo: ?», ¿qué hago: lo invento o lo consulto?", "lo consulto", "No invento datos de otra cultura."),
    ],
    A=[
        ex("Ficha de fuente (inventada): Pueblo: aymara. Narrador: un educador tradicional. Lugar: la biblioteca. Se puede compartir: sí. ¿Cuántos datos tiene la ficha?", "4", "Pueblo, narrador, lugar y si se puede compartir son cuatro datos."),
        ex("Ficha (inventada): Pueblo: mapuche. Narradora: una educadora. Lugar: ?. ¿Qué dato falta?", "el lugar", "El lugar tiene un signo de pregunta."),
        ex("Escribe una pregunta para la ficha que no dice si se puede compartir: A) «¿Se puede compartir este relato en mi curso?» B) «Lo cuento igual».", "A", "A pregunta con respeto."),
    ],
    Z=[
        ex("Marcela dice: «Si me gusta un relato, puedo contarlo en cualquier fiesta». ¿Qué le falta saber?", "si se puede compartir", "Algunos relatos se comparten solo en ciertas ocasiones."),
        ex("¿Por qué importa saber el pueblo de un relato?", "porque cada pueblo tiene sus propios relatos", "No se pueden mezclar los relatos de pueblos distintos."),
    ],
    D=[
        ex("Tienes 3 fichas y cada una tiene 4 datos. ¿Cuántos datos hay en total?", "12", "3 × 4 = 12 datos."),
        ex("Dos fichas dicen: A) «Pueblo: mapuche. Narrador: educadora.» B) «Pueblo: ?. Narrador: ?». ¿Cuál ficha es más completa?", "A", "A tiene pueblo y narrador; B no tiene ninguno."),
    ],
    context=[ex("Tu curso invita a una educadora tradicional a contar un epew. Antes de comenzar, la profesora lee la ficha: «Pueblo: mapuche. Narradora: la educadora. Lugar: la sala. Se puede compartir: sí, en la sala». ¿Pueden contarlo después en el patio de otra escuela?", "No", "La ficha dice que se puede compartir en la sala.")],
    selfcheck=[
        ex("Nombra una de las cuatro preguntas de la ficha de fuente.", "pueblo, narrador, lugar o si se puede compartir", "Esas son las cuatro preguntas."),
        ex("¿Qué hago si falta un dato en la ficha?", "lo consulto", "No lo invento."),
        ex("¿Qué palabra mapuzugun nombra un relato tradicional?", "epew", "«Epew» es la palabra para relato."),
    ],
    task=T(
        "Completa en tu cuaderno esta ficha con datos de práctica inventados: Pueblo: (elige mapuche, aymara o rapa nui). Narrador: (elige un educador o una educadora tradicional, o un abuelo de la comunidad). Lugar: (la sala, la biblioteca o el patio). Se puede compartir: (sí o no, y dónde). Después escribe una pregunta que le harías a esa persona sobre cómo cuidar el relato.",
        "Pueblo: aymara. Narrador: un educador tradicional. Lugar: la biblioteca. Se puede compartir: sí, en la escuela. Pregunta: ¿cómo cuidamos este relato cuando lo contamos en clase?",
        ["completa los cuatro datos con las opciones dadas", "no inventa un relato real", "formula una pregunta de cuidado"],
        ["ficha escrita", "pregunta escrita o dicha"],
        ["dejar datos en blanco", "escribir un relato inventado como si fuera tradicional"],
        "Valora que completó los cuatro datos y preguntó; si inventó un relato real, aclara que eso lo enseña la comunidad.",
    ),
    reinforce="Di en voz alta las cuatro preguntas de la ficha de fuente sin mirar el cuaderno.",
    extend="Pregunta a alguien mayor de tu familia quién le contaba historias cuando era pequeño y anota el nombre de la fuente con su permiso.",
)

L(
    LS1, 3,
    materials="Lápiz y hoja. Los relatos de práctica están escritos aquí; son inventados, no son relatos tradicionales de ningún pueblo.",
    use="Aprenderé a comprender un relato corto y a reconocer sus palabras importantes. Sirve para entender qué pasó y por qué esas palabras importan para un pueblo.",
    prior=["Sé quién cuenta un relato y de qué pueblo es.", "Sé contestar quién, dónde y qué pasa."],
    explain=[
        "Comprender un relato es saber quién actúa, dónde ocurre, qué pasa y cómo termina. También es reconocer las palabras que tienen un significado especial. Una palabra culturalmente significativa es una palabra que importa mucho en la vida de un pueblo, como el nombre de un árbol, de una flor o del agua.",
        "En Chile, el copihue es una flor roja que crece en los bosques del sur y es la flor nacional. La palabra viene del mapuzugun, la lengua del pueblo mapuche. El pewen es la araucaria, un árbol de la cordillera del sur, y sus semillas se llaman piñones. Los pehuenche son una parte del pueblo mapuche cuyo nombre significa «gente del pewen».",
        "Cuando leo un relato, relaciono esas palabras con lo que pasa. Pregunto: ¿por qué aparece este árbol o esta flor?, ¿qué hace el personaje con ellos? No invento un significado sagrado: solo digo lo que el texto dice y lo que sé con certeza.",
    ],
    vocab=[("significativa", "que importa mucho"), ("copihue", "flor roja del sur de Chile; la palabra viene del mapuzugun"), ("pewen", "araucaria, árbol de la cordillera del sur, en mapuzugun"), ("piñón", "semilla de la araucaria"), ("pehuenche", "parte del pueblo mapuche, «gente del pewen»")],
    worked=[
        W("Comprender un relato", "Relato de práctica (inventado): «Con su familia, Tomás fue al bosque en otoño. Bajo un pewen recogió piñones y los llevó a su casa para comer juntos.» ¿Dónde recogió los piñones?", ["Busco dónde ocurre.", "El texto dice: bajo un pewen.", "Los recogió bajo un pewen."], "bajo un pewen"),
        W("Reconocer una palabra especial", "En el relato de Tomás, ¿cuál es la palabra en mapuzugun que nombra un árbol?", ["Busco una palabra que no es castellano.", "Aparece «pewen».", "Un pewen es una araucaria."], "pewen"),
    ],
    mistakes=[
        M("Decir un significado especial que el texto no dice.", "No sé si ese significado existe para el pueblo.", "Solo digo lo que dice el relato y lo que sé con certeza."),
        M("Confundir el relato con una historia real de una persona.", "El texto dice «de práctica (inventado)».", "Leo la nota del relato antes de responder."),
    ],
    R=[
        ex("Relato de práctica (inventado): «Con su familia, Tomás fue al bosque en otoño. Bajo un pewen recogió piñones y los llevó a su casa para comer juntos.» ¿Quién fue al bosque?", "Tomás con su familia", "El texto dice que Tomás fue con su familia."),
        ex("Mismo relato de Tomás. ¿En qué estación del año ocurre?", "en otoño", "El texto dice «en otoño»."),
        ex("¿Qué es el piñón: una semilla de la araucaria o una flor roja?", "una semilla de la araucaria", "El piñón es la semilla del pewen."),
    ],
    C=[
        ex("Verdadero o falso: el copihue es una flor roja del sur de Chile.", "Verdadero", "Es la flor nacional y crece en los bosques del sur."),
        ex("Relato del copihue: «Ema encontró un copihue rojo y lo devolvió al bosque». ¿De qué lengua viene la palabra «copihue»?", "del mapuzugun", "La palabra viene del mapuzugun."),
        ex("Los pehuenche son «gente del pewen». ¿Qué árbol da su nombre a este grupo?", "el pewen", "Pewen es la araucaria."),
    ],
    A=[
        ex("Relato de práctica (inventado): «Lía regó el huerto con ko. Después miró el antü sobre su casa.» " + FICHA_PAL + " ¿Qué palabra del relato quiere decir agua?", "ko", "La ficha dice que «ko» es agua."),
        ex("Mismo relato de Lía y la ficha de palabras. ¿Qué palabra del relato quiere decir sol?", "antü", "La ficha dice que «antü» es sol."),
        ex("Relato de Tomás. Ordena: 1) lleva los piñones a su casa 2) va al bosque con su familia 3) recoge piñones bajo el pewen. Escribe los números en orden.", "2, 3, 1", "Va al bosque, recoge piñones y luego los lleva a la casa."),
    ],
    Z=[
        ex("Rocío dice que el relato de Tomás cuenta una ceremonia secreta con el pewen. ¿El texto lo dice? Responde Sí o No.", "No", "El texto solo cuenta que recogió piñones con su familia."),
        ex("¿Por qué importa la palabra «pewen» para entender el nombre «pehuenche»?", "porque pehuenche significa gente del pewen", "El nombre viene de la palabra pewen."),
    ],
    D=[
        ex("Tomás recogió 12 piñones y su hermana 8. ¿Cuántos piñones recogieron entre los dos?", "20", "12 + 8 = 20 piñones."),
        ex("Relato de Ema y relato de Tomás. ¿En cuál aparece una flor roja?", "en el relato de Ema", "Ema encontró un copihue rojo."),
    ],
    context=[ex("Durante la clase la educadora muestra una foto de un copihue y dice que es la flor nacional. Un compañero pregunta qué quiere decir «nacional». ¿Qué respuesta es correcta: que representa a todo el país o que solo es de un pueblo?", "que representa a todo el país", "Una flor nacional representa al país.")],
    selfcheck=[
        ex("¿Cuál pregunta ayuda a comprender un relato: «¿qué pasa al final?» o «¿cuál es mi color favorito?»", "«¿qué pasa al final?»", "Esa pregunta busca un hecho del relato."),
        ex("¿Qué es una palabra culturalmente significativa?", "una palabra que importa mucho para un pueblo", "Es importante para esa cultura."),
        ex("¿Puedo inventar un significado sagrado para un árbol?", "No", "Solo digo lo que sé con certeza."),
    ],
    task=T(
        "Lee este relato de práctica inventado: «Camila y su abuelo caminaron por el bosque en otoño. Vieron un pewen alto y un río. Camila dijo «chaltumay» al abuelo por mostrarle el bosque.» Fichas: «pewen» es la araucaria; «chaltumay» es gracias en mapuzugun. En tu cuaderno responde: ¿quién camina?, ¿dónde?, ¿qué vieron? y ¿cuál palabra en mapuzugun muestra agradecimiento? Dibuja la escena.",
        "Camila y su abuelo. Por el bosque. Un pewen y un río. «chaltumay» muestra agradecimiento. Dibujo: dos personas, un árbol alto y un río.",
        ["responde las cuatro preguntas con el texto", "reconoce las palabras significativas", "no inventa significados"],
        ["respuestas en el cuaderno", "dibujo de la escena"],
        ["agregar hechos que el relato no dice", "confundir el relato inventado con uno tradicional"],
        "Reconoce que comprendió y que reconoció las palabras; si agregó hechos, invítalo a volver al texto.",
    ),
    reinforce="Dibuja un pewen con sus piñones y escribe su nombre en mapuzugun.",
    extend="Averigua con un adulto si en tu región hay árboles o flores con nombres de origen indígena y anota uno.",
)

L(
    LS1, 4,
    materials="Lápiz y hoja. Las respuestas de ejemplo están escritas aquí.",
    use="Aprenderé a responder a un relato con mis palabras, con dibujos o con un agradecimiento, sin quedarme con él como si fuera mío. Sirve para respetar al pueblo que lo guarda.",
    prior=["Sé contar quién, dónde y qué pasa.", "Sé qué es una fuente."],
    explain=[
        "Después de escuchar un relato puedo responder de varias maneras: dibujar una escena, contar con mis palabras lo que entendí, hacer una pregunta o agradecer. Todas son formas de mostrar que escuché con atención.",
        "Apropiarse es quedarse con algo de otros como si fuera mío. Si cuento un relato de un pueblo y digo «yo lo inventé», me estoy apropiando. Para evitarlo, digo siempre quién me lo contó y de qué pueblo es. También evito cambiar el relato, mezclarlo con otros o usarlo en bromas.",
        "Mi respuesta es mi versión de lo que entendí, no el relato verdadero. Por eso puedo empezar con «Entendí que…». Y cierro agradeciendo, por ejemplo con «chaltumay», que según la ficha es «gracias» en mapuzugun.",
    ],
    vocab=[("responder", "decir o hacer algo después de escuchar"), ("apropiarse", "quedarse con algo de otros como si fuera mío"), ("mi versión", "lo que yo entendí, con mis palabras"), ("agradecer", "decir gracias a quien me compartió algo"), ("mezclar", "juntar cosas que son distintas")],
    worked=[
        W("Responder con mis palabras", RELATO_EMA + " ¿Cómo empiezo mi respuesta?", ["Pienso en lo que entendí.", "Empiezo con «Entendí que…».", "Sigo: Ema devolvió el copihue al bosque."], "Entendí que Ema devolvió el copihue al bosque."),
        W("Evitar apropiarme", "Quiero contar a mi familia un relato que me contó una educadora tradicional. ¿Qué digo primero?", ["Digo quién me lo contó.", "Digo de qué pueblo es.", "Cuento lo que escuché sin cambiarlo."], "digo quién me lo contó y de qué pueblo es"),
    ],
    mistakes=[
        M("Decir «yo inventé este relato» de un relato que me contaron.", "Estoy tomando como mío lo que es de otro.", "Digo quién me lo contó."),
        M("Mezclar dos relatos para que sea más divertido.", "Cambio algo que otros cuidan.", "Cuento solo lo que escuché o cuento mi dibujo."),
    ],
    R=[
        ex("¿Cómo puedo empezar mi respuesta a un relato: «Entendí que…» o «Yo lo inventé…»?", "«Entendí que…»", "Así muestro que es mi versión."),
        ex("Dibujar una escena del relato, ¿es una forma de responder?", "Sí", "Es una manera de mostrar lo que entendí."),
        ex("¿Qué palabra mapuzugun uso para agradecer según la ficha: chaltumay o mapu?", "chaltumay", "Según la ficha, «chaltumay» es gracias."),
    ],
    C=[
        ex("Verdadero o falso: puedo decir que yo inventé un relato que me contó una educadora.", "Falso", "Eso sería apropiarme de algo de otros."),
        ex("¿Qué quiere decir apropiarse?", "quedarse con algo de otros como si fuera mío", "Es tomar lo que es de otros."),
        ex("Si cuento un relato que escuché, ¿qué debo decir además del relato?", "quién me lo contó", "La fuente reconoce a quien lo cuidó."),
    ],
    A=[
        ex("Eliges la respuesta que no se apropia: A) «Esta historia la inventé yo.» B) «Una educadora me contó esta historia y yo la entendí así.»", "B", "B reconoce a la fuente y dice que es mi versión."),
        ex(RELATO_EMA + " Escribe una respuesta que empiece con «Entendí que…» y diga qué hizo Ema. Elige: A) «Entendí que Ema devolvió el copihue al bosque.» B) «Entendí que Ema se lo quedó.»", "A", "A es lo que dice el texto."),
        ex("Termina una respuesta con un agradecimiento. Elige: A) «Chaltumay, gracias por contarnos el relato.» B) «Ya está.»", "A", "A agradece a quien contó."),
    ],
    Z=[
        ex("Claudio dice: «Voy a cambiar el final del relato para que sea más gracioso y lo cuento en la fiesta». ¿Está bien? Responde Sí o No.", "No", "Cambiar un relato que no es mío puede faltarle el respeto al pueblo."),
        ex("¿Por qué es mejor decir «mi versión» que «el relato verdadero»?", "porque yo solo cuento lo que entendí", "Yo no soy quien guarda el relato."),
    ],
    D=[
        ex("Cuentas con tus palabras 3 relatos a la semana por 4 semanas. ¿Cuántos relatos cuentas en total?", "12", "3 × 4 = 12 relatos."),
        ex("Un amigo mezcla el relato de Ema con otro relato sin avisar. ¿Qué le sugieres: contarlo por separado diciendo la fuente o juntarlos?", "contarlo por separado diciendo la fuente", "Así no se confunden ni se cambian."),
    ],
    context=[ex("En el recreo te piden que cuentes el relato que la educadora contó en clase. Tú lo recuerdas a medias. ¿Qué haces: lo inventas completo o dices lo que recuerdas y que le pregunten a la educadora?", "digo lo que recuerdo y que le pregunten a la educadora", "No invento partes de un relato que no es mío.")],
    selfcheck=[
        ex("¿Qué dato digo siempre al contar un relato que me contaron?", "quién me lo contó", "Así reconozco a la fuente."),
        ex("¿Qué frase uso para empezar mi respuesta?", "Entendí que…", "Muestra que es mi versión."),
        ex("¿Puedo mezclar relatos de pueblos distintos?", "No", "Cada relato pertenece a su pueblo."),
    ],
    task=T(
        "Después de escuchar (o leer) el relato de práctica de Ema, haz tres cosas en tu cuaderno: 1) Dibuja una escena. 2) Escribe una frase que empiece con «Entendí que…». 3) Escribe una frase de agradecimiento dirigida a quien lo contó, usando «chaltumay» si quieres (según la ficha es «gracias» en mapuzugun). Escribe al final: «Es un relato de práctica inventado».",
        "Dibujo: Ema y el copihue. Entendí que Ema devolvió el copihue al bosque. Chaltumay por contarnos el relato. Es un relato de práctica inventado.",
        ["dibujo, frase y agradecimiento", "dice que es su versión", "reconoce la fuente"],
        ["dibujo en el cuaderno", "frases escritas"],
        ["cambiar el relato", "decir que el relato es suyo"],
        "Reconoce que respondió desde su versión y agradeció; si dijo que lo inventó, aclara quién es la fuente.",
    ),
    reinforce="Practica en voz alta: «Entendí que… Gracias por contarlo».",
    extend="Elige un cuento corto que te contaron en casa y cuéntalo diciendo primero quién te lo contó.",
)

L(
    LS1, 5,
    materials="Lápiz y hoja. Las afirmaciones para revisar y los carteles de práctica están escritos aquí.",
    use="Aprenderé a revisar un dibujo, un cartel o una dramatización que representa a un pueblo originario, para ver si es respetuoso. Sirve para no repetir estereotipos.",
    prior=["Sé que cada pueblo originario tiene su propia cultura.", "Sé responder sin apropiarme."],
    explain=[
        "Representar es mostrar algo con un dibujo, un cartel o una obra de teatro. Una representación respetuosa muestra a las personas y a los pueblos como son hoy y como son sus culturas, con datos verdaderos. Un estereotipo es una imagen simple y repetida que muestra a todos iguales, y casi siempre es falsa.",
        "Hay errores comunes. Uno es pensar que todos los pueblos viven igual. Otro es pensar que solo existieron en el pasado: hoy los pueblos originarios viven en el campo y en la ciudad. Otro es usar un disfraz como si fuera un juego. Y otro es mezclar objetos de pueblos distintos. Por ejemplo, el tipi es una vivienda de pueblos de Norteamérica, no de Chile.",
        "Para revisar hago tres preguntas: ¿es un dato verdadero?, ¿muestra a un pueblo o a todos como si fueran iguales? y ¿lo aprobó o lo explicó alguien de la comunidad? Si algo no pasa la revisión, lo corrijo con ayuda del educador o la educadora tradicional.",
    ],
    vocab=[("representación", "dibujo, cartel u obra que muestra algo"), ("estereotipo", "imagen simple y repetida que muestra a todos iguales"), ("respetuoso", "que trata con cuidado a las personas y a sus culturas"), ("disfraz", "ropa que se usa para parecer otra cosa"), ("corregir", "cambiar algo para que sea verdadero y respetuoso")],
    worked=[
        W("Revisar un cartel", "Cartel de práctica (inventado): «Los pueblos originarios solo vivieron hace mucho tiempo». ¿Es un dato verdadero?", ["Pienso: ¿hay pueblos originarios hoy?", "Sí, hoy viven personas de pueblos originarios en Chile.", "El cartel es falso y se debe corregir."], "No; hay pueblos originarios hoy"),
        W("Corregir una frase", "Cartel de práctica (inventado): «Todos los pueblos viven igual». ¿Cómo lo corrijo?", ["Veo la palabra «todos» y «igual».", "Cada pueblo tiene su propia cultura.", "Escribo: «Cada pueblo tiene su cultura»."], "Cada pueblo tiene su cultura."),
    ],
    mistakes=[
        M("Pensar que si un dibujo es bonito entonces es respetuoso.", "Un dibujo bonito puede mostrar datos falsos.", "Reviso si es verdadero y si pasó por la comunidad."),
        M("Usar un disfraz de «indígena» en una fiesta como si fuera un chiste.", "Convierte la cultura de un pueblo en un juego.", "Mejor aprendo con el educador cómo se puede representar con respeto."),
    ],
    R=[
        ex("Un estereotipo, ¿es una imagen simple que muestra a todos iguales o una foto?", "una imagen simple que muestra a todos iguales", "Eso es un estereotipo."),
        ex("Verdadero o falso: hoy viven personas de pueblos originarios en Chile.", "Verdadero", "Los pueblos originarios viven hoy en el campo y en la ciudad."),
        ex("El tipi, ¿es una vivienda de pueblos de Norteamérica o de los mapuche de Chile?", "de pueblos de Norteamérica", "La casa mapuche se llama ruka; el tipi es de Norteamérica."),
    ],
    C=[
        ex("Cartel de práctica: «Todos los pueblos originarios hablan la misma lengua». ¿Es verdadero o falso?", "Falso", "Cada pueblo tiene su propia lengua."),
        ex("Dibujo de práctica: una familia mapuche en un tipi. ¿Qué error tiene?", "mezcla un objeto de otro pueblo", "El tipi no es una vivienda mapuche; la casa mapuche se llama ruka."),
        ex("Elige la afirmación respetuosa: A) «Los pueblos originarios son parte del Chile de hoy.» B) «Los pueblos originarios ya no existen.»", "A", "A es verdadera y respetuosa."),
    ],
    A=[
        ex("Cartel de práctica: «Mapuche = flechas y plumas». ¿Qué le falta: datos verdaderos o más colores?", "datos verdaderos", "Es un estereotipo; hace falta preguntar al educador cómo representarlo."),
        ex("Una obra de teatro quiere usar disfraces de pueblos originarios. ¿Qué haces primero: pedir ayuda al educador tradicional o disfrazarte?", "pedir ayuda al educador tradicional", "Primero se consulta a quien conoce la cultura."),
        ex("¿Cuántas preguntas tiene la revisión de esta clase?", "3", "Son datos verdaderos, no mostrar a todos iguales y aprobación de la comunidad."),
    ],
    Z=[
        ex("Pablo dice: «Si me disfrazo con respeto, no hay problema». ¿Qué le falta saber?", "si el educador o la comunidad lo aprueba", "La comunidad decide cómo representar su cultura."),
        ex("Un cartel dice «Los pueblos originarios solo son del pasado». ¿Qué dato lo corrige?", "hoy viven en el campo y en la ciudad", "Muestra que son parte del presente."),
    ],
    D=[
        ex("Revisaste 6 carteles y 2 tenían errores. ¿Cuántos estaban bien?", "4", "6 − 2 = 4 carteles."),
        ex("Un dibujo mezcla una ruka con un moai y una llama. Son de pueblos distintos. ¿Qué mejor haces: dibujar una ruka sola o juntar todo en una escena?", "dibujar una ruka sola", "Así no mezclo elementos de pueblos distintos."),
    ],
    context=[ex("Para el acto de la escuela, un grupo quiere hacer un baile con ropa «de indígena» comprada en una tienda de disfraces. ¿Qué propones: preguntar a la educadora tradicional qué se puede hacer o seguir con los disfraces?", "preguntar a la educadora tradicional qué se puede hacer", "La comunidad dice cómo representar con respeto su cultura.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es un estereotipo?", "una imagen simple que muestra a todos iguales", "Casi siempre es falsa."),
        ex("Verdadero o falso: una de las tres preguntas de la revisión es «¿es un dato verdadero?».", "Verdadero", "Es la primera de las tres preguntas."),
        ex("¿Quién ayuda a corregir una representación?", "el educador tradicional", "Conoce la cultura."),
    ],
    task=T(
        "Revisa estos tres carteles de práctica inventados. A) «Todos los pueblos originarios viven igual.» B) «Hoy hay personas de pueblos originarios en el campo y en la ciudad.» C) «El tipi es la casa de los mapuche.» En tu cuaderno escribe cuáles están bien y cuáles hay que corregir. Para cada uno que corrijas, escribe cómo lo dirías de forma respetuosa. Finalmente escribe una pregunta al educador tradicional.",
        "A: corregir: «Cada pueblo tiene su cultura». B: bien. C: corregir: la casa mapuche se llama ruka; el tipi es de pueblos de Norteamérica. Pregunta: ¿cómo podemos representar su cultura en nuestro acto?",
        ["identifica B como correcta", "corrige A y C", "formula una pregunta para el educador"],
        ["tabla de revisión", "carteles corregidos"],
        ["aceptar el estereotipo", "inventar datos sin fuente"],
        "Valora que revisó con las tres preguntas; si aceptó un estereotipo, vuelve a las preguntas.",
    ),
    reinforce="Escribe una frase que corrija el cartel «Todos los pueblos viven igual».",
    extend="Mira un afiche o un cuento infantil de tu casa y revisa si muestra a las personas de forma respetuosa.",
)

# =================================================================== LS02 · medio natural y mensajes de la naturaleza
L(
    LS2, 1,
    materials="Lápiz, hoja y, si es posible, una ventana o el patio de tu casa. Si no puedes salir, usa la descripción de práctica escrita en este cuaderno.",
    use="Aprenderé a observar el entorno con los sentidos y a decir lo que observo con palabras claras. Sirve para describir la naturaleza antes de interpretar nada.",
    prior=["Sé nombrar elementos de la naturaleza: cielo, árbol, agua, piedra.", "Sé hablar en voz alta con oraciones cortas."],
    explain=[
        "Observar es mirar con atención. Usamos los sentidos: la vista para colores y formas, el oído para sonidos, el olfato para olores y el tacto para sentir si algo está frío, tibio, liso o áspero. No probamos plantas ni cosas desconocidas.",
        "Una descripción oral dice lo que observo con orden. Puedo seguir este orden: dónde estoy, qué veo, qué oigo y qué siento. Uso palabras simples y números cuando puedo, por ejemplo «tres pájaros» o «un árbol alto».",
        "Muchos pueblos originarios han observado la naturaleza durante muchísimo tiempo y conocen su territorio muy bien. Yo comienzo con lo que puedo observar hoy y no digo qué «mensaje» tiene la naturaleza para un pueblo. Eso lo explica la comunidad.",
    ],
    vocab=[("observar", "mirar con atención usando los sentidos"), ("sentido", "vista, oído, olfato, tacto y gusto"), ("descripción", "decir cómo es algo"), ("oral", "dicho con la voz"), ("medio natural", "lo que hay en la naturaleza de un lugar: agua, plantas, animales, cielo")],
    worked=[
        W("Clasificar por sentidos", "Observación de práctica: «Veo un árbol verde. Oigo un pájaro. Siento el viento frío.» ¿Qué sentido usé para «oigo un pájaro»?", ["Pienso con qué parte lo percibo.", "Oigo con los oídos.", "Usé el oído."], "el oído"),
        W("Ordenar una descripción", "Descripción de práctica: «Estoy en el patio. Veo un cielo gris. Oigo la lluvia. Siento el aire frío.» ¿Qué dice primero: dónde estoy o qué veo?", ["Leo la primera oración.", "Dice: «Estoy en el patio».", "Primero dice dónde está."], "dónde estoy"),
    ],
    mistakes=[
        M("Decir una opinión como si fuera una observación, como «el cielo está triste».", "Es una idea mía, no se ve con los ojos.", "Digo lo que veo: «el cielo está gris»."),
        M("Probar una planta para saber cómo es.", "Puede ser peligrosa.", "Uso solo la vista, el oído, el olfato y el tacto con cuidado."),
    ],
    R=[
        ex("¿Con qué sentido veo el color de una hoja: la vista o el oído?", "la vista", "El color se ve."),
        ex("¿Con qué sentido noto si el viento está frío: el tacto o el olfato?", "el tacto", "El frío se siente en la piel."),
        ex("¿Debo probar plantas que no conozco para describirlas? Responde Sí o No.", "No", "Pueden ser peligrosas."),
    ],
    C=[
        ex("Observación de práctica: «Oigo el agua de un río». ¿Qué sentido usé?", "el oído", "El agua se oye."),
        ex("Frase: «El cielo está triste». ¿Es una observación o una idea mía?", "una idea mía", "Triste no se ve con los ojos."),
        ex("Descripción: «Veo tres pájaros en un árbol alto». ¿Cuántos pájaros hay?", "3", "El texto dice tres pájaros."),
    ],
    A=[
        ex("Descripción de práctica: «Hay una piedra lisa y fría. Hay hojas secas. Huele a tierra mojada.» ¿Cuántas cosas distintas se describen?", "3", "La piedra, las hojas secas y el olor a tierra."),
        ex("Observas estos hechos: 1) veo nubes 2) oigo el viento 3) siento calor. ¿Cuál número usa el oído?", "2", "Oír el viento usa el oído."),
        ex("Ordena tu descripción: A) qué oigo B) dónde estoy C) qué veo. Escribe las letras en el orden de esta clase (dónde, qué veo, qué oigo).", "B, C, A", "El orden es dónde estoy, qué veo y qué oigo."),
    ],
    Z=[
        ex("Lucho dice: «El árbol está feliz porque tiene muchas hojas». ¿Es una observación? Responde Sí o No.", "No", "Que el árbol esté feliz es una idea, no algo que se vea."),
        ex("¿Por qué no digo qué mensaje tiene la naturaleza para un pueblo si lo acabo de observar?", "porque eso lo explica la comunidad", "Yo no sé lo que significa para ese pueblo."),
    ],
    D=[
        arith("Contaste 8 hojas verdes y 5 hojas secas. ¿Cuántas hojas contaste en total?", "8+5", "Se suman las hojas verdes y las secas."),
        ex("Describe lo que observas con una frase que use un número: elige la frase correcta para un cielo con 4 nubes. A) «Hay muchas nubes tristes.» B) «Hay 4 nubes en el cielo.»", "B", "B dice lo que se ve y con número."),
    ],
    context=[ex("Estás en tu casa mirando por la ventana. Ves un árbol, oyes un perro y sientes el aire fresco. ¿Con qué sentido sabes que el perro está cerca?", "con el oído", "Lo percibes con el oído.")],
    selfcheck=[
        ex("¿Qué cuatro sentidos uso para observar sin probar?", "vista, oído, olfato y tacto", "Con ellos observo con seguridad."),
        ex("¿Qué dice primero una descripción: dónde estoy o qué siento?", "dónde estoy", "El orden empieza por el lugar."),
        ex("¿Quién explica el mensaje que la naturaleza tiene para un pueblo?", "la comunidad", "Es su saber."),
    ],
    task=T(
        "Mira por la ventana, el patio o el parque con un adulto durante dos minutos. Si no puedes salir, usa esta descripción de práctica: «Estoy en un patio. Veo un árbol alto, tres pájaros y nubes blancas. Oigo el viento. Siento el aire fresco». Cuenta en voz alta lo que observas en cuatro frases: dónde estoy, qué veo, qué oigo y qué siento. Dibuja lo que contaste.",
        "Estoy en el patio. Veo dos árboles y una nube blanca. Oigo un pájaro. Siento el aire fresco. Dibujo: patio con árboles y nube.",
        ["dice las cuatro frases", "usa los sentidos", "no inventa mensajes"],
        ["relato oral", "dibujo"],
        ["decir ideas como observaciones", "probar plantas"],
        "Valora la observación con orden; si dijo «triste» o «feliz», pídele que diga qué ve exactamente.",
    ),
    reinforce="Describe en voz alta lo que ves y oyes en este momento, en dos frases.",
    extend="Cuenta a alguien de tu familia qué ves por tu ventana, con números y colores.",
)

L(
    LS2, 2,
    materials="Lápiz y hoja. Las fichas de territorio están escritas aquí con datos generales y seguros.",
    use="Aprenderé que en distintos territorios de Chile la naturaleza es diferente y que cada pueblo la conoce de forma propia. Sirve para describir un lugar sin mezclar pueblos.",
    prior=["Sé observar con los sentidos.", "Sé nombrar elementos como mar, desierto, volcán, bosque."],
    explain=[
        "Chile tiene paisajes muy distintos. En el norte hay desierto y altiplano. En el centro hay valles. En el sur hay bosques, lagos y volcanes. En los canales del extremo sur hay mar e islas. En el océano Pacífico está Rapa Nui, una isla.",
        "Cada pueblo originario vive en su territorio y conoce su naturaleza. El pueblo aymara vive en el norte, en el altiplano. El pueblo lickanantay vive en el desierto de Atacama. El pueblo mapuche vive sobre todo en el centro y el sur. El pueblo rapa nui vive en la isla de Rapa Nui. El pueblo kawésqar vive en los canales de la Patagonia occidental.",
        "Por eso, para describir la naturaleza de un lugar, primero pregunto de qué pueblo y de qué territorio hablamos. No uso lo que sé de un lugar para otro. Y si no tengo el dato, lo pregunto a una fuente.",
    ],
    vocab=[("territorio", "lugar donde un pueblo vive y que conoce muy bien"), ("altiplano", "zona alta y plana de los Andes"), ("desierto", "lugar con muy poca lluvia"), ("isla", "tierra rodeada de agua"), ("canal", "paso de mar entre islas o tierra")],
    worked=[
        W("Unir pueblo y paisaje", "Ficha: «El pueblo rapa nui vive en una isla del océano Pacífico». ¿Qué paisaje se relaciona con ese pueblo?", ["Leo la ficha.", "Dice isla en el Pacífico.", "El paisaje es una isla."], "una isla en el Pacífico"),
        W("No mezclar territorios", "Un niño dice: «El pueblo aymara vive en un desierto con mar». ¿Qué dice mi ficha del pueblo aymara?", ["Busco aymara: vive en el altiplano del norte.", "No dice que viva junto al mar.", "El niño mezcló datos."], "vive en el altiplano del norte; el niño mezcló"),
    ],
    mistakes=[
        M("Pensar que todos los pueblos viven en el mismo paisaje.", "Chile tiene paisajes muy distintos.", "Pregunto de qué pueblo y territorio hablamos."),
        M("Usar un dato de un territorio para describir otro.", "Cada territorio tiene su propia naturaleza.", "Uso solo los datos de la ficha correcta."),
    ],
    R=[
        ex("Ficha: «El pueblo rapa nui vive en una isla». ¿Dónde vive: en una isla o en un desierto?", "en una isla", "La ficha dice isla."),
        ex("¿Dónde queda el altiplano: en el norte o en el sur?", "en el norte", "El altiplano de Chile está en el norte."),
        ex("¿Qué rodea a una isla: tierra o agua?", "agua", "Una isla está rodeada de agua."),
    ],
    C=[
        ex("Ficha: «El pueblo lickanantay vive en el desierto de Atacama». ¿Es un lugar con mucha o con poca lluvia?", "poca", "Un desierto tiene muy poca lluvia."),
        ex("Verdadero o falso: el pueblo kawésqar vive en el altiplano.", "Falso", "Vive en los canales de la Patagonia occidental."),
        ex("Ficha: «El pueblo mapuche vive sobre todo en el centro y sur de Chile». ¿Vive en el norte desértico?", "No", "La ficha dice centro y sur."),
    ],
    A=[
        ex("Une pueblo y paisaje: 1) aymara 2) rapa nui 3) kawésqar. Paisajes: a) isla b) altiplano c) canales de la Patagonia. Escribe las parejas.", "1-b, 2-a, 3-c", "Aymara: altiplano; rapa nui: isla; kawésqar: canales."),
        ex("Ficha: «En los canales hay mar, islas y mucha lluvia». ¿Cuántos elementos de la naturaleza nombra?", "3", "Mar, islas y lluvia."),
        ex("Describe en una frase al pueblo lickanantay usando la ficha: elige A) «Vive en el desierto de Atacama.» B) «Vive en la isla de Pascua.»", "A", "A coincide con la ficha."),
    ],
    Z=[
        ex("Gabriel dice: «En todos los territorios llueve mucho». ¿Es cierto para el desierto de Atacama? Responde Sí o No.", "No", "En el desierto llueve muy poco."),
        ex("¿Por qué es mejor preguntar de qué pueblo y territorio hablamos antes de describir un lugar?", "porque cada territorio es distinto", "Así uso los datos correctos."),
    ],
    D=[
        ex("Hay 5 pueblos en la explicación del territorio. Si ya describiste 2, ¿cuántos faltan?", "3", "5 − 2 = 3 pueblos."),
        ex("Ficha: «Rapa Nui está en el océano Pacífico; el altiplano está en los Andes». ¿Cuál de los dos está rodeado de agua?", "Rapa Nui", "Una isla está rodeada de agua."),
    ],
    context=[ex("En clase leen sobre un pueblo que vive en el sur con bosques y lagos. Un compañero dice que hay camellos en ese lugar. ¿Qué haces: aceptas o pides una fuente?", "pides una fuente", "Un dato nuevo se revisa con una fuente.")],
    selfcheck=[
        ex("¿Dónde vive el pueblo rapa nui?", "en una isla del océano Pacífico", "La ficha lo dice."),
        ex("¿Qué pregunto antes de describir un lugar?", "de qué pueblo y territorio hablamos", "Cada territorio es distinto."),
        ex("¿Todos los pueblos viven en el mismo paisaje?", "No", "Chile tiene paisajes distintos."),
    ],
    task=T(
        "Elige uno de estos dos territorios: A) El altiplano del pueblo aymara, en el norte, entre cerros y volcanes. B) Los canales de la Patagonia occidental del pueblo kawésqar, con mar, islas y lluvia. En tu cuaderno dibuja el paisaje y escribe tres frases orales que lo describan usando solo los datos dados. Practícalas en voz alta y agrega una pregunta para el educador tradicional.",
        "A: Es el altiplano del norte. Hay cerros y volcanes. El pueblo aymara vive ahí. Pregunta: ¿qué cuidados tienen con los cerros?",
        ["escribe tres frases con datos dados", "dibuja el paisaje", "formula una pregunta"],
        ["dibujo y frases", "frases dichas en voz alta"],
        ["mezclar datos de otro territorio", "inventar mensajes de la naturaleza"],
        "Valora que usó los datos de la ficha; si mezcló territorios, vuelve a la ficha.",
    ),
    reinforce="Une los tres pueblos con su paisaje diciendo una oración para cada uno.",
    extend="Con un adulto, busca en un mapa de Chile dónde queda el altiplano y dónde está Rapa Nui.",
)

L(
    LS2, 3,
    materials="Lápiz y hoja. Las observaciones de práctica están escritas aquí.",
    use="Aprenderé a relacionar lo que observo en la naturaleza con lo que puede pasar después, como las nubes oscuras con la lluvia. Sirve para describir los mensajes que podemos observar y para valorar que cada pueblo los lee a su manera.",
    prior=["Sé observar con los sentidos.", "Sé que hay estaciones del año."],
    explain=[
        "La naturaleza nos muestra señales. Una señal es algo que se observa y que nos avisa de otra cosa. Por ejemplo, si el cielo se llena de nubes oscuras y el viento cambia, puede llover. Si las hojas de los árboles caen y hace más frío, está llegando el otoño.",
        "Para leer una señal, observo primero, luego uno lo que observo con lo que ya sé y digo: «Veo… por eso puede ser que…». Digo «puede ser» porque no estoy seguro. Esta es una manera de describir mensajes de la naturaleza con la ciencia y la experiencia.",
        "Los pueblos originarios tienen su propia manera de leer las señales de su territorio, aprendida por generaciones. Esa lectura la explican sus comunidades y sus educadores tradicionales. Yo no invento qué significa una señal para un pueblo: solo digo lo que observo y pregunto.",
    ],
    vocab=[("señal", "algo que se observa y avisa de otra cosa"), ("estación", "cada época del año: verano, otoño, invierno, primavera"), ("puede ser", "expresión para decir algo que no es seguro"), ("experiencia", "lo que he vivido y aprendido"), ("mensaje de la naturaleza", "señal que la naturaleza nos muestra")],
    worked=[
        W("Leer una señal", "Observo nubes oscuras y el viento fuerte. ¿Qué puede ser que pase?", ["Observo: nubes oscuras y viento.", "Recuerdo que a veces después llueve.", "Digo: puede ser que llueva."], "puede ser que llueva"),
        W("Señal de la estación", "Observo hojas amarillas en el suelo y mañanas más frías. ¿Qué estación puede estar llegando?", ["Observo hojas que caen y más frío.", "Eso pasa a menudo en otoño.", "Puede ser que llegue el otoño."], "el otoño"),
    ],
    mistakes=[
        M("Decir «va a llover seguro» con solo ver una nube.", "No estoy seguro de que pase.", "Uso «puede ser que…»."),
        M("Decir qué significa una señal para un pueblo sin saberlo.", "Esa lectura es de su comunidad.", "Digo lo que observo y pregunto al educador."),
    ],
    R=[
        ex("Nubes oscuras y viento fuerte: ¿qué puede ser que pase?", "que llueva", "Es una señal de lluvia posible."),
        ex("Las hojas caen y hace más frío: ¿qué estación puede estar llegando?", "el otoño", "Esas señales suelen darse en otoño."),
        ex("¿Qué palabra uso cuando no estoy seguro: «seguro» o «puede ser»?", "puede ser", "Marca que es una posibilidad."),
    ],
    C=[
        ex("Verdadero o falso: una señal es algo que se observa y avisa de otra cosa.", "Verdadero", "Eso es una señal."),
        ex("Observo cielo despejado y mucho sol. ¿Qué puede ser que pase con la temperatura?", "que haga calor", "Con mucho sol suele subir la temperatura."),
        ex("¿Quién explica cómo un pueblo lee las señales de su territorio: su comunidad o yo?", "su comunidad", "Es un saber de ese pueblo."),
    ],
    A=[
        ex("Une la señal con lo que puede pasar. 1) Nubes oscuras 2) Mucho sol 3) Hojas amarillas. a) calor b) lluvia c) otoño. Escribe las parejas.", "1-b, 2-a, 3-c", "Nubes: lluvia; sol: calor; hojas amarillas: otoño."),
        ex("Observación: veo charcos en el patio y el suelo mojado. ¿Qué pasó antes: llovió o hubo sol fuerte?", "llovió", "El agua en el suelo muestra que llovió."),
        ex("Completa: «Veo nubes oscuras, por eso ____ que llueva». Elige: A) puede ser B) es seguro.", "A", "No estoy seguro, uso «puede ser»."),
    ],
    Z=[
        ex("Sara dice: «Vi un pájaro volar y eso significa lo mismo para todos los pueblos». ¿Tiene razón? Responde Sí o No.", "No", "Cada pueblo tiene su propia lectura y la explica su comunidad."),
        ex("¿Por qué uso «puede ser» y no «seguro» al leer una señal?", "porque no puedo estar seguro", "Las señales avisan, pero no aseguran."),
    ],
    D=[
        ex("Durante 7 días observas el cielo. En 3 días ves nubes oscuras. ¿En cuántos días no ves nubes oscuras?", "4", "7 − 3 = 4 días."),
        ex("Veo nubes oscuras en la mañana y por la tarde llueve. Al día siguiente veo nubes oscuras y llueve otra vez. ¿Qué puedo decir: «a veces lo he visto» o «siempre pasa»?", "a veces lo he visto", "Con pocos casos no puedo decir siempre."),
    ],
    context=[ex("Tu abuelo mira el cielo y dice: «Hoy habrá lluvia». Tú ves nubes oscuras. ¿Qué dices para unir lo que ves con lo que dijo: «Veo nubes oscuras, por eso puede ser que llueva» o «Tu abuelo siempre acierta»?", "«Veo nubes oscuras, por eso puede ser que llueva»", "Une la observación con la posibilidad.")],
    selfcheck=[
        ex("¿Qué es una señal?", "algo que se observa y avisa de otra cosa", "Eso es una señal."),
        ex("¿Qué dos palabras uso al leer una señal si no estoy seguro?", "puede ser", "Marcan la posibilidad."),
        ex("¿Quién explica la lectura de señales de un pueblo?", "su comunidad", "Es su saber."),
    ],
    task=T(
        "Elige una de estas observaciones de práctica y escribe en tu cuaderno cómo la lees con la frase «Veo…, por eso puede ser que…». A) Nubes oscuras y viento fuerte. B) Hojas amarillas en el suelo y mañanas frías. C) Cielo despejado y mucho sol. Dibuja la señal y lo que puede pasar. Escribe una pregunta al educador tradicional sobre cómo su pueblo observa su territorio.",
        "A: Veo nubes oscuras y viento fuerte, por eso puede ser que llueva. Dibujo: nubes y lluvia. Pregunta: ¿qué señales observan en su territorio?",
        ["usa la frase con «puede ser»", "une señal y posibilidad", "formula una pregunta"],
        ["frase escrita", "dibujo"],
        ["decir que es seguro", "inventar significados"],
        "Valora que usó la posibilidad; si afirmó con seguridad, practica con «puede ser».",
    ),
    reinforce="Mira el cielo hoy y di en voz alta una señal que ves y lo que puede pasar.",
    extend="Pregunta a alguien mayor de tu familia qué señales de la naturaleza observa y anota una.",
)

L(
    LS2, 4,
    materials="Lápiz y hoja. La ficha de palabras y los modelos de descripción están escritos aquí.",
    use="Aprenderé a describir oralmente la naturaleza con algunas palabras en mapuzugun o en castellano que me enseñó una fuente, sin apropiarme. Sirve para hablar con precisión y respeto.",
    prior=["Sé observar y describir con los sentidos.", "Sé que debo nombrar la fuente."],
    explain=[
        "Una descripción oral puede incluir palabras en lengua indígena si una fuente me las enseñó. Por ejemplo, en la ficha de esta clase «ko» es agua, «antü» es sol, «kuyen» es luna, «mapu» es tierra, «lafken» es mar y «pewen» es la araucaria. Las uso con el significado de la ficha y las pronuncio como me enseñe el educador o la educadora.",
        "También puedo usar palabras en castellano que son significativas, como copihue o pudú. El copihue es una flor roja del sur. El pudú es un ciervo muy pequeño que vive en los bosques del sur. Son palabras de origen mapuzugun que hoy usamos en castellano.",
        "Para no apropiarme, empiezo mi descripción diciendo quién me enseñó cada palabra: «Según la ficha…» o «La educadora me enseñó…». No digo que descubrí una palabra ni que inventé un significado. Y al final digo gracias.",
    ],
    vocab=[("describir", "decir cómo es algo"), ("pudú", "ciervo muy pequeño del sur de Chile; la palabra es de origen mapuzugun"), ("copihue", "flor roja del sur de Chile"), ("pronunciar", "decir una palabra con la voz"), ("fuente", "quien me enseñó o escribió el dato")],
    worked=[
        W("Descripción con una palabra", FICHA_PAL + " Quiero decir: «Veo el sol». ¿Qué frase uso con la palabra de la ficha?", ["Busco sol en la ficha.", "Es «antü».", "Digo: «Veo el «antü» en el cielo»."], "Veo el «antü» en el cielo."),
        W("Decir la fuente", "Me enseñó la palabra «ko» la ficha. ¿Cómo lo digo?", ["Empiezo con «Según la ficha».", "Agrego la palabra y el significado.", "Digo: «Según la ficha, «ko» es agua»."], "Según la ficha, «ko» es agua."),
    ],
    mistakes=[
        M("Usar una palabra en lengua indígena con otro significado.", "Quise que sonara bonita.", "Uso el significado de la ficha."),
        M("No decir quién me enseñó la palabra.", "Parece que la inventé yo.", "Empiezo con «Según la ficha…»."),
    ],
    R=[
        ex(FICHA_PAL + " ¿Qué quiere decir «lafken»?", "mar", "La ficha dice que «lafken» es mar."),
        ex(FICHA_PAL + " ¿Qué palabra nombra la luna?", "kuyen", "La ficha dice que «kuyen» es luna."),
        ex("El pudú, ¿es un ciervo muy pequeño o un pájaro grande?", "un ciervo muy pequeño", "El pudú es un ciervo muy pequeño del sur."),
    ],
    C=[
        ex(FICHA_PAL + " Descripción: «Bebo «ko» fresca». ¿Qué es «ko»?", "agua", "La ficha dice que «ko» es agua."),
        ex("Verdadero o falso: puedo decir que yo inventé la palabra «antü».", "Falso", "Es una palabra del mapuzugun que me enseña la ficha."),
        ex("El copihue, ¿qué es: una flor roja del sur o un pez?", "una flor roja del sur", "El copihue es la flor nacional."),
    ],
    A=[
        ex(FICHA_PAL + " Completa la frase: «Camino sobre la «____» y veo un árbol». Elige la palabra que significa tierra.", "mapu", "La ficha dice que «mapu» es tierra."),
        ex(FICHA_PAL + " Describe: «De noche veo la «____» en el cielo». Elige la palabra que significa luna.", "kuyen", "La ficha dice que «kuyen» es luna."),
        ex(FICHA_PAL + " Elige cómo empiezas tu descripción: A) «Según la ficha, el «lafken» es el mar.» B) «Descubrí que el «lafken» es el mar.»", "A", "A reconoce la fuente."),
    ],
    Z=[
        ex("Esteban dice: «El pudú es una planta». ¿Tiene razón? Responde Sí o No.", "No", "El pudú es un ciervo muy pequeño."),
        ex("¿Por qué es importante decir quién me enseñó una palabra?", "para no apropiarme", "Reconozco a la fuente."),
    ],
    D=[
        ex("Quieres describir tu patio con tres palabras de la ficha: «antü», «ko» y «mapu». ¿Cuántas palabras de la ficha usarás?", "3", "Son tres palabras."),
        ex("Descripción: «Veo el «antü» sobre el «lafken»». ¿Qué ves: el sol sobre el mar o la luna sobre la tierra?", "el sol sobre el mar", "«Antü» es sol y «lafken» es mar."),
    ],
    context=[ex("Estás en una playa con tu familia y quieres decir «el mar está tranquilo» usando una palabra de la ficha. ¿Qué palabra usas para mar?", "lafken", "La ficha dice que «lafken» es mar.")],
    selfcheck=[
        ex("¿Qué digo antes de usar una palabra en lengua indígena?", "según la ficha o quién me la enseñó", "Reconozco a la fuente."),
        ex("¿Qué es el copihue?", "una flor roja del sur de Chile", "Es la flor nacional."),
        ex("¿Puedo cambiar el significado de una palabra de la ficha?", "No", "Debo usar el significado que enseña la fuente."),
    ],
    task=T(
        "Usa la ficha de palabras. Elige tres palabras (ko, antü, kuyen, mapu, lafken, pewen) y escribe una descripción oral de tres frases de un paisaje que imagines: cada frase con una palabra de la ficha entre comillas. Empieza con «Según la ficha…». Practícala en voz alta y dibuja el paisaje.",
        "Según la ficha, «ko» es agua. Veo un río con «ko» clara. En el cielo hay «antü». Dibujo: río y sol.",
        ["usa tres palabras de la ficha con su significado", "empieza con «Según la ficha»", "la dice en voz alta"],
        ["frases en el cuaderno", "dibujo del paisaje"],
        ["cambiar el significado", "no decir la fuente"],
        "Valora que usó la ficha y dijo la fuente; si cambió un significado, vuelve a la ficha.",
    ),
    reinforce="Di en voz alta tres frases con «ko», «antü» y «mapu», cada una con su significado.",
    extend="Enséñale a alguien de tu casa dos palabras de la ficha, diciendo que se las enseñó la ficha de la escuela.",
)

L(
    LS2, 5,
    materials="Lápiz y hoja. Las descripciones para revisar están escritas aquí.",
    use="Aprenderé a revisar una descripción oral de la naturaleza para ver si es respetuosa y verdadera. Sirve para mejorar lo que digo antes de compartirlo.",
    prior=["Sé describir con los sentidos.", "Sé usar palabras de la ficha con su fuente."],
    explain=[
        "Revisar es mirar de nuevo para mejorar. Cuando reviso una descripción de la naturaleza hago cuatro preguntas. ¿Digo lo que observo y no lo que imagino? ¿Uso las palabras en lengua indígena con el significado de la fuente? ¿Digo quién me las enseñó? ¿Evito inventar «mensajes» que no sé?",
        "Una buena descripción separa tres cosas: lo que veo («hay nubes»), lo que pienso que puede pasar («puede ser que llueva») y lo que me enseñó una fuente («según la educadora…»). Si mezclo estas tres cosas, parece que todo viene de la fuente y eso no es cierto.",
        "Si encuentro un error, lo corrijo con calma. Puedo borrar una frase, cambiar una palabra o agregar la fuente. Y si hay una duda cultural, la dejo como pregunta para el educador o la educadora tradicional.",
    ],
    vocab=[("revisar", "mirar de nuevo para mejorar"), ("separar", "poner cada cosa en su lugar"), ("corregir", "cambiar para que quede bien"), ("duda", "cuando no estoy seguro de algo"), ("verdadero", "que coincide con lo que realmente es")],
    worked=[
        W("Revisar una frase", "Descripción: «El cielo está enojado y la gente de todos los pueblos sabe que lloverá». ¿Qué parte inventa?", ["Reviso «enojado»: no se ve.", "Reviso «todos los pueblos saben»: no sé eso.", "Las dos partes inventan."], "«enojado» y «todos los pueblos saben»"),
        W("Corregir con la fuente", "Frase: «Descubrí que «ko» es agua». ¿Cómo la corrijo para reconocer la fuente?", ["Veo que dice «descubrí».", "La palabra me la enseñó la ficha.", "Escribo: «Según la ficha, «ko» es agua»."], "Según la ficha, «ko» es agua."),
    ],
    mistakes=[
        M("No separar lo que veo de lo que pienso.", "Parece que todo es un hecho.", "Marco con colores: veo, pienso, me enseñó la fuente."),
        M("Borrar una duda cultural en vez de preguntarla.", "Pierdo la oportunidad de aprender.", "La escribo como pregunta para el educador."),
    ],
    R=[
        ex("Frase: «El cielo está enojado». ¿Dice lo que se ve o lo que se imagina?", "lo que se imagina", "Enojado no se observa."),
        ex("Frase: «Hay tres nubes blancas». ¿Se puede observar?", "Sí", "Se cuentan con la vista."),
        ex("¿Qué hago si tengo una duda cultural: la borro o la pregunto?", "la pregunto", "Preguntar es aprender."),
    ],
    C=[
        ex("Verdadero o falso: en una buena descripción separo lo que veo, lo que pienso y lo que me enseñó una fuente.", "Verdadero", "Separarlo ayuda a no mezclar."),
        ex("Frase: «Según la educadora, «antü» es sol». ¿Qué parte es el dato de la fuente?", "«antü» es sol", "Después de «según» va lo que dice la fuente."),
        ex("Frase: «Puede ser que llueva». ¿Es un hecho seguro o una posibilidad?", "una posibilidad", "«Puede ser» marca posibilidad."),
    ],
    A=[
        ex("Revisa la descripción: «Veo nubes oscuras. Puede ser que llueva. Según la ficha, «ko» es agua». ¿Cuántas de las tres frases vienen de una fuente?", "1", "Solo la tercera dice «según la ficha»."),
        ex("Corrige: «Descubrí que «kuyen» es luna». Elige: A) «Según la ficha, «kuyen» es luna.» B) «Yo sé que «kuyen» es luna.»", "A", "A reconoce la fuente."),
        ex("Una descripción tiene 5 frases y 2 inventan cosas. ¿Cuántas frases quedan bien?", "3", "5 − 2 = 3 frases."),
    ],
    Z=[
        ex("Marina dice: «Si no sé si algo es verdad, lo digo con seguridad igual». ¿Está bien? Responde Sí o No.", "No", "Si no sé, digo «puede ser» o pregunto."),
        ex("¿Por qué es útil separar lo que veo de lo que me enseñó la fuente?", "para saber qué dato viene de quién", "Evita mezclar ideas mías con el saber de la comunidad."),
    ],
    D=[
        ex("Tienes 4 descripciones y revisas 1 por minuto. ¿Cuántos minutos tardas?", "4", "4 ÷ 1 = 4 minutos."),
        ex("Frase: «Según mi abuela, cuando hay niebla puede que haga frío». ¿Es un hecho que ocurre siempre o lo que dijo su abuela?", "lo que dijo su abuela", "Empieza con «según mi abuela»."),
    ],
    context=[ex("Un compañero describe el patio: «El árbol tiene muchas hojas. Los pueblos originarios dicen que el árbol manda mensajes secretos». ¿Qué frase debes revisar con el educador tradicional?", "la de los mensajes secretos", "Eso no se observa y lo explica la comunidad.")],
    selfcheck=[
        ex("¿Cuántas preguntas hago al revisar mi descripción?", "4", "Son las cuatro preguntas."),
        ex("¿Qué hago con una duda cultural?", "la escribo como pregunta", "Así la consulto con el educador."),
        ex("¿Qué palabra marca una posibilidad?", "puede ser", "Dice que no es seguro."),
    ],
    task=T(
        "Revisa esta descripción de práctica inventada: «El bosque está feliz. Veo cuatro árboles altos. Los pueblos originarios dicen que los árboles hablan. Según la ficha, «pewen» es la araucaria». En tu cuaderno subraya con verde lo que se puede observar, con azul lo que viene de una fuente y con rojo lo que hay que revisar. Reescribe la descripción corregida y agrega una pregunta para el educador tradicional.",
        "Verde: veo cuatro árboles altos. Azul: según la ficha, «pewen» es la araucaria. Rojo: el bosque está feliz; los pueblos originarios dicen que los árboles hablan. Corregida: Veo cuatro árboles altos. Según la ficha, «pewen» es la araucaria. Pregunta: ¿cómo cuidan los árboles en su territorio?",
        ["clasifica las frases en tres colores", "corrige la descripción", "formula una pregunta"],
        ["frases subrayadas", "descripción corregida"],
        ["aceptar frases inventadas", "borrar la duda cultural"],
        "Reconoce que separó observación, fuente y duda; si dejó una frase inventada, vuelve a las cuatro preguntas.",
    ),
    reinforce="Revisa una descripción tuya con las cuatro preguntas y corrige una frase.",
    extend="Lee una descripción de un cuento o libro de casa y señala qué parte se puede observar y qué parte es imaginada.",
)
