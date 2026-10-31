"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF01 (relatos fundacionales en lengua indígena) y OA LF02 (diálogo y exposición en lengua indígena).

Criterio de autoría: las comunidades, las personas, los relatos y los diálogos de práctica son INVENTADOS, están en
castellano y se rotulan como tales; no pertenecen a ningún pueblo. Las únicas expresiones en lengua indígena son las ya
atestiguadas en grados anteriores (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke en mapuzugun; iorana,
maururu en rapa nui) y siempre dentro de una ficha. No se escribe pronunciación, gramática ni uso ceremonial, y no se
afirma a qué pueblo pertenece ningún relato inventado. La forma tradicional de contar, decir y pronunciar la enseñan el
educador/a tradicional y la comunidad; cada tarea abierta lo remite a ellos. Este módulo define los ayudantes y los
textos de práctica que reutilizan los demás módulos lc5_b*.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LF1, LF2 = "LC05 OA LF01", "LC05 OA LF02"

CONSULT = " Recuerda: lo tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Consúltales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No evaluar la identidad ni la fluidez de nadie."


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


MAT = "Lápiz y hojas. Los textos, las fichas y los diálogos están escritos en este cuaderno y son inventados para practicar; no son de ningún pueblo."

FICHA_A = ("Ficha situada (inventada). Comunidad: Bahía Serena (no es un pueblo real). Territorio: una bahía con playa, roqueríos y un río corto. "
           "Fuente y responsable: doña Marta, narradora de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Marta autorizó usar el relato en la escuela. "
           "Límite: la segunda parte del relato no se cuenta fuera de la comunidad.")
FICHA_B = ("Ficha situada (inventada). Comunidad: Cumbre Blanca (no es un pueblo real). Territorio: una cordillera con nieve, pastizales y viento. "
           "Fuente y responsable: don Anselmo, narrador de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: don Anselmo autorizó usar el relato en la escuela. "
           "Límite: no se cuenta el nombre del cerro donde sucede.")
RELATO_A = ("Relato de práctica «La primera gota» (inventado): «Al principio no había mar, ni playa, ni cerros. Solo había silencio y una sombra muy grande. "
            "Un día cayó una gota diminuta y brilló en la sombra. De esa gota nació el primer mar. El mar mojó la arena, la arena sostuvo la primera roca "
            "y de la roca salieron las primeras personas.»")
RELATO_B = ("Relato de práctica «La semilla de luz» (inventado): «Al principio el mundo dormía bajo el hielo. Una semilla de luz bajó del cielo y se hundió en el hielo. "
            "El hielo se quebró y salió el primer pasto. El pasto llamó al viento y el viento llamó a las personas.»")
FICHA_PAL = ("Ficha de palabras (de práctica): en mapuzugun «ko» es agua, «mapu» es tierra, «antü» es sol, «kuyen» es luna, «ruka» es casa y «ñuke» es madre. "
             "«mari mari» es un saludo y «chaltumay» es «gracias» en mapuzugun. «iorana» es un saludo y «maururu» es «gracias» en rapa nui.")

# ============================================================ OA LF01 · relatos fundacionales
L(
    LF1, 1,
    materials=MAT,
    use="Aprenderé a situar un relato fundacional: de qué comunidad es, quién lo cuenta, si hay permiso y qué no se cuenta. Sirve para escuchar relatos con respeto y sin apropiarme de ellos.",
    prior=["Sé que un relato oral se cuenta con la voz y pertenece a una comunidad.", "Sé que no se registra ni se publica lo que no tiene permiso."],
    explain=[
        "Un relato fundacional o cosmogónico es una historia que explica cómo empezó el mundo, un lugar o las personas. Cada pueblo tiene los suyos y los cuida como parte de su cultura. Por eso no es un cuento cualquiera: tiene dueños, que son la comunidad que lo transmite y las personas que lo cuentan.",
        "Antes de leer o escuchar un relato lo situamos con una ficha de seis datos: comunidad, territorio, fuente y responsable, fecha, permiso y límite. El límite dice qué parte no se cuenta fuera de la comunidad. Si falta un dato, la actividad se detiene y se pregunta al educador o educadora tradicional.",
        "En este cuaderno practicamos con relatos inventados, escritos en castellano, que no son de ningún pueblo. Un relato real en lengua indígena lo cuenta una persona de la comunidad, con sus palabras y en su momento. Nosotros aprendemos a escuchar, no a reemplazarla ni a completar lo que ella no cuenta.",
    ],
    vocab=[("relato fundacional", "historia que explica cómo empezó el mundo o un lugar"), ("cosmogónico", "que habla del origen del mundo"), ("fuente", "persona o texto de donde viene el relato"), ("permiso", "autorización para usar un relato"), ("límite", "parte que la comunidad no cuenta fuera de ella")],
    worked=[
        W("Leer una ficha", FICHA_A + " ¿Qué parte del relato no se cuenta fuera de la comunidad?", ["Busco el dato «Límite».", "Dice que es la segunda parte del relato."], "La segunda parte del relato."),
        W("Detectar un dato que falta", "Ficha: «Comunidad: Cumbre Blanca. Territorio: cordillera. Fuente: don Anselmo. Fecha: de ejemplo. Permiso: (sin dato). Límite: (sin dato)». ¿Qué hago?", ["Reviso los seis datos.", "Faltan permiso y límite.", "Sin ellos no se puede usar el relato."], "Detengo la actividad y pregunto al educador tradicional."),
    ],
    mistakes=[
        M("Pensar que un relato fundacional es un cuento sin dueño.", "Pertenece a la comunidad que lo cuida.", "Escribo siempre de qué comunidad viene y quién lo cuenta."),
        M("Completar con mis ideas la parte que la ficha dice que no se cuenta.", "Esa parte la reserva la comunidad.", "La dejo sin escribir y lo anoto como límite."),
    ],
    R=[
        ex("Según la ficha de Bahía Serena, ¿quién es la fuente y responsable del relato?", "Doña Marta", "La ficha la nombra como narradora de la comunidad."),
        ex("Un relato fundacional cuenta: A) cómo empezó el mundo o un lugar B) la lista de útiles escolares", "A", "Los relatos fundacionales hablan de orígenes."),
        ex("En la ficha de Bahía Serena, ¿qué hay en el territorio: una bahía con playa o una cordillera con nieve?", "Una bahía con playa", "Así describe la ficha su territorio."),
    ],
    C=[
        ex("Verdadero o falso: un relato fundacional pertenece a la comunidad que lo cuida.", "Verdadero", "La comunidad lo transmite y decide su uso."),
        ex("¿Para qué sirve el dato «Límite» de una ficha? A) para saber qué parte no se cuenta fuera de la comunidad B) para saber la hora del recreo", "A", "El límite protege lo que la comunidad reserva."),
        ex("Una ficha trae comunidad, territorio, fuente y fecha, pero no dice si hay autorización para usar el relato ni qué parte se reserva. ¿Qué dos datos faltan?", "El permiso y el límite", "Son los dos datos de los seis que no aparecen."),
    ],
    A=[
        ex("Ficha de Cumbre Blanca: «Límite: no se cuenta el nombre del cerro donde sucede». Una compañera quiere escribir el nombre del cerro en su trabajo. ¿Puede? Responde Sí o No.", "No", "El límite lo prohíbe expresamente."),
        ex("Une cada dato con su pregunta. 1) fuente 2) permiso 3) territorio. a) ¿se puede usar? b) ¿dónde vive la comunidad? c) ¿quién lo cuenta?", "1-c, 2-a, 3-b", "Cada dato responde una pregunta distinta."),
        ex("En la ficha de Bahía Serena, ¿cuál de estos datos nombra a una persona: «fuente y responsable» o «territorio»?", "Fuente y responsable", "Nombra a la persona que cuenta el relato."),
    ],
    Z=[
        ex("Pablo dice: «Como el relato de Bahía Serena habla del mar, todos los pueblos de Chile tienen un relato del mar». ¿Qué error comete?", "Generaliza una ficha a todos los pueblos", "Una comunidad no representa a todas."),
        ex("Una niña quiere contar en su exposición la segunda parte del relato de Bahía Serena, que la ficha reserva. ¿Debe contarla? Responde Sí o No.", "No", "Es el límite declarado en la ficha."),
    ],
    D=[
        ex("Ficha 1: fuente doña Marta, permiso «sí». Ficha 2: fuente «no se sabe», permiso «sin dato». ¿Con cuál puedes trabajar?", "Con la ficha 1", "Solo la 1 tiene fuente y permiso."),
        ex("Si falta el permiso, ¿qué haces? A) me detengo y pregunto al educador tradicional B) escribo «sí» para terminar rápido", "A", "No se inventan datos de una ficha."),
    ],
    context=[ex("Una vecina ofrece contar a tu curso el relato de su comunidad y un compañero quiere grabarlo con un celular. ¿Qué haces primero? A) pedir la ficha situada y preguntar si se puede grabar B) grabar sin avisar para no interrumpir", "A", "Primero se sitúa y se pide permiso.")],
    selfcheck=[
        ex("Nombra dos de los seis datos de la ficha situada.", "Dos entre: comunidad, territorio, fuente, fecha, permiso, límite", "Son los datos de la ficha."),
        ex("Verdadero o falso: puedo completar con mis ideas la parte que la comunidad no cuenta.", "Falso", "Lo reservado se respeta."),
        ex("¿Quién enseña la forma tradicional de contar un relato real? A) el educador o educadora tradicional y la comunidad B) cualquier página de internet", "A", "Ellos son la fuente pertinente."),
    ],
    task=T("Lee la ficha de Cumbre Blanca: «" + FICHA_B + "» Haz una tabla de dos columnas: «Lo que la ficha dice» (comunidad, territorio, fuente, permiso, límite) y «Lo que la ficha no dice». Escribe una frase que empiece con «Este relato viene de…» y otra que empiece con «No cuento…». Cierra con una pregunta que le harías al educador tradicional sobre los relatos de tu zona.",
           "Dice: comunidad Cumbre Blanca; cordillera con nieve, pastizales y viento; fuente don Anselmo; permiso sí; límite el nombre del cerro. No dice: la fecha exacta del relato. Este relato viene de Cumbre Blanca, contado por don Anselmo. No cuento el nombre del cerro. Pregunta: ¿qué relatos de nuestra zona se pueden compartir en la escuela?",
           ["completa la tabla con datos de la ficha", "escribe las dos frases pedidas", "formula una pregunta respetuosa"], ["tabla de dos columnas", "dos frases", "pregunta escrita"], ["agregar datos que la ficha no trae", "escribir el nombre del cerro", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea de la ficha está cada dato; valorar que deje en blanco lo no declarado."),
    reinforce="Copia la ficha de Bahía Serena en tu hoja y subraya con un color el permiso y con otro el límite.",
    extend="Escribe cuatro preguntas que harías a una persona de la comunidad antes de usar un relato suyo en la escuela.",
)

L(
    LF1, 2,
    materials=MAT,
    use="Aprenderé a leer o escuchar un relato fundacional comprendiéndolo y declarando sus límites: qué dice, qué no dice y qué la comunidad reserva. Sirve para no confundir lo que cuenta la fuente con lo que yo imagino.",
    prior=["Sé situar un relato con una ficha de seis datos.", "Sé que el límite de la ficha no se rompe."],
    explain=[
        "Comprender un relato es saber qué ocurre y en qué orden: qué había al principio, qué cambió y qué apareció después. Para eso leemos o escuchamos con atención y marcamos cada hecho. Un relato fundacional suele avanzar por pasos, y cada paso nace del anterior. Si cambiamos el orden, cambia el sentido.",
        "Escuchar con límites declarados significa decir en voz alta tres cosas: lo que el relato dice, lo que no dice y lo que la comunidad reserva. Lo que el relato no dice no se completa con la imaginación. Si alguien pregunta algo que la fuente no contó, se responde: «El relato que conozco no cuenta eso».",
        "Los relatos de este cuaderno son inventados. Con ellos practicamos una forma de escuchar que sirve también para los relatos reales, que cuentan las personas de cada comunidad. Cuando ellas se detienen o dicen «esto no lo cuento», eso también es parte del relato y se respeta sin insistir.",
    ],
    vocab=[("orden de los hechos", "qué pasa primero, después y al final"), ("comprender", "saber qué dice un texto y cómo se relacionan sus partes"), ("límite declarado", "lo que se dice abiertamente que no se cuenta"), ("completar", "agregar algo que el texto no dijo"), ("reservar", "guardar algo y no compartirlo con todos")],
    worked=[
        W("Ordenar los hechos", RELATO_A + " ¿Qué nació primero: el mar o las personas?", ["Subrayo cada hecho: gota, mar, arena, roca, personas.", "El mar nace de la gota, antes que todo lo demás."], "Primero nació el mar."),
        W("Responder dentro del límite", RELATO_A + " Alguien pregunta: «¿Cómo se llamaban las primeras personas?». ¿Qué se responde?", ["Busco ese dato en el relato.", "No aparece."], "El relato que conozco no cuenta eso."),
    ],
    mistakes=[
        M("Inventar una respuesta cuando el relato no cuenta algo.", "Se mezcla lo que dice la fuente con lo que imagino.", "Digo que el relato no cuenta eso."),
        M("Cambiar el orden de los hechos al resumir.", "Cada hecho nace del anterior.", "Reviso la secuencia antes de escribir."),
    ],
    R=[
        ex(RELATO_A + " ¿Qué cayó en la sombra?", "Una gota diminuta", "El relato lo dice así."),
        ex(RELATO_A + " ¿De dónde salieron las primeras personas?", "De la roca", "Es lo último que cuenta el relato."),
        ex(RELATO_A + " ¿Qué sostuvo la primera roca: la arena o el silencio?", "La arena", "El relato dice que la arena sostuvo la roca."),
    ],
    C=[
        ex(RELATO_A + " Verdadero o falso: al principio había una sombra muy pequeña.", "Falso", "El relato dice que la sombra era muy grande."),
        ex("¿Qué es un «límite declarado»? A) lo que se dice abiertamente que no se cuenta B) un dibujo del mapa", "A", "Es lo que la fuente avisa que no cuenta."),
        ex("Si el relato no cuenta algo, ¿qué haces: lo completo con mi idea o digo que el relato no lo cuenta?", "Digo que el relato no lo cuenta", "Se respeta lo que la fuente contó."),
    ],
    A=[
        ex("Ordena estos hechos del relato de Bahía Serena: a) las personas salen de la roca b) cae la gota c) nace el mar d) la arena sostiene la roca. Escribe las letras.", "b, c, d, a", "La gota origina el mar, el mar moja la arena y la arena sostiene la roca de la que salen las personas."),
        ex(RELATO_A + " ¿Cuál afirmación está en el relato? A) el mar tenía muchos peces B) la gota brilló en la sombra", "B", "La A agrega algo que no se cuenta."),
        ex(RELATO_B + " ¿Qué se quebró cuando la semilla de luz se hundió?", "El hielo", "El relato lo dice así."),
    ],
    Z=[
        ex("Tomás dice: «La gota del relato era de lluvia». Según el texto de «La primera gota», ¿se puede afirmar eso? Responde Sí o No.", "No", "El relato solo dice que era una gota diminuta que brilló."),
        ex("La ficha de Bahía Serena reserva la segunda parte. Un compañero pregunta qué pasó después con las personas. ¿Qué respuesta respeta el límite? A) «Esa parte no se cuenta fuera de la comunidad» B) «Seguro se fueron a vivir al río»", "A", "La B inventa lo que la comunidad reserva."),
    ],
    D=[
        ex("Camila resume: «De una gota nació el mar y del mar salieron las personas». ¿Qué dos pasos omitió?", "La arena y la roca", "En el relato, el mar moja la arena y la arena sostiene la roca de la que salen las personas."),
        ex("Dos lectores. Lector 1: «El relato dice que el mundo empezó con una gota». Lector 2: «El relato dice que todos los pueblos creen en la gota». ¿Cuál respeta lo que dice la fuente?", "El lector 1", "El lector 2 generaliza a todos los pueblos."),
    ],
    context=[ex("Una vecina cuenta un relato y se detiene antes de la segunda parte: «Eso no lo cuento». Una niña insiste en que lo cuente. ¿Qué debe hacer el curso? A) respetar y no insistir B) pedir que lo cuente para terminar la historia", "A", "El silencio de quien cuenta es un límite que se respeta.")],
    selfcheck=[
        ex("Nombra las tres cosas que se declaran al escuchar con límites.", "Lo que el relato dice, lo que no dice y lo que se reserva", "Son los tres límites de la lectura."),
        ex(RELATO_A + " ¿Qué había al principio: mar o silencio con una sombra grande?", "Silencio con una sombra grande", "Así comienza el relato."),
        ex("Verdadero o falso: puedo responder con mi imaginación lo que el relato no cuenta.", "Falso", "Se avisa que el relato no lo cuenta."),
    ],
    task=T("Lee el relato «La semilla de luz»: «" + RELATO_B.split("«", 2)[2].rstrip("»") + "» Haz una tabla de tres columnas: «El relato dice», «El relato no dice» y «Lo que la comunidad podría reservar». Escribe al menos tres cosas en la primera y dos en la segunda. En la tercera pon una sola frase que empiece con «Preguntaría al educador tradicional si…».",
           "Dice: el mundo dormía bajo el hielo; la semilla de luz bajó del cielo; salió el primer pasto. No dice: de dónde vino la semilla ni cómo se llamaban las personas. Reservado: Preguntaría al educador tradicional si hay una parte del relato que no se cuente fuera de la comunidad.",
           ["registra hechos del texto en el orden correcto", "distingue lo que no dice", "propone una pregunta sin inventar"], ["tabla de tres columnas", "frase de pregunta"], ["agregar hechos que no están", "completar la parte reservada"],
           "Pedir que señale en el texto cada hecho de la primera columna; valorar que escriba «no sé» cuando falta información."),
    reinforce="Escribe en tu hoja los cinco hechos de «La primera gota» en orden, uno por línea.",
    extend="Inventa una pregunta que el relato «La semilla de luz» no responde y escribe cómo responderías con respeto.",
)

L(
    LF1, 3,
    materials=MAT,
    use="Aprenderé a relacionar un relato fundacional con el territorio y con la vida de la comunidad, y a explicar por qué importa a quienes lo cuidan. Sirve para entender que un relato no es solo entretención.",
    prior=["Sé comprender un relato y declarar sus límites.", "Sé que lo que dice una ficha vale para su comunidad."],
    explain=[
        "Un relato fundacional se relaciona con el territorio donde vive la comunidad. En «La primera gota» aparecen el mar, la arena y la roca, que son elementos de una bahía. Esa relación entre el relato y los lugares ayuda a entender por qué la historia importa a quienes viven allí: les habla de su propio entorno.",
        "También se relaciona con la vida de la comunidad: con lo que se cuida, lo que se agradece y cómo se comportan las personas. Esa relación la explican quienes cuentan el relato, con testimonios. Nosotros no la adivinamos: la leemos de la fuente y decimos «según…». Un testimonio inventado de doña Marta nos servirá de ejemplo.",
        "En lengua indígena, algunas palabras claves nombran los elementos del relato. En mapuzugun, «ko» es agua y «mapu» es tierra. Conocer esas palabras ayuda a escuchar el relato de ese pueblo, pero el sentido que el pueblo les da lo explica su comunidad. Una palabra suelta no basta para explicar una cultura.",
    ],
    vocab=[("relación", "vínculo entre dos cosas, como un relato y un lugar"), ("testimonio", "relato de una persona sobre lo que vive o sabe"), ("entorno", "lugares y seres que rodean a una comunidad"), ("palabra clave", "palabra importante para entender un texto o una cultura"), ("según", "palabra que indica de quién viene una idea")],
    worked=[
        W("Relacionar relato y territorio", "Relato «La primera gota» y ficha de Bahía Serena (una bahía con playa, roqueríos y un río corto). ¿Qué elemento del relato aparece también en el territorio?", ["Elementos del relato: mar, arena, roca.", "Territorio: playa y roqueríos, junto al mar."], "El mar, la arena y la roca aparecen en el relato y en la bahía."),
        W("Leer una relación en un testimonio", "Testimonio inventado de doña Marta: «Por este relato, en Bahía Serena no se tira basura al mar y se agradece lo que el mar da». ¿Qué relación hay entre el relato y el cuidado del mar?", ["El relato dice que el mar nació de una gota.", "El testimonio dice que, por eso, se cuida y se agradece."], "Según doña Marta, el relato lleva a cuidar y agradecer al mar."),
    ],
    mistakes=[
        M("Decir que un relato sirve solo para entretener.", "Para la comunidad se relaciona con su territorio y su forma de cuidar.", "Busco qué dice el testimonio sobre su importancia."),
        M("Afirmar el significado de una palabra indígena más allá de la ficha de palabras.", "Una palabra suelta no explica una cultura.", "Uso solo la ficha y pregunto al educador tradicional."),
    ],
    R=[
        ex("Testimonio de doña Marta: «Por este relato, en Bahía Serena no se tira basura al mar y se agradece lo que el mar da». ¿Qué no se hace en el mar?", "No se tira basura", "El testimonio lo dice así."),
        ex("Según el mismo testimonio, ¿qué se agradece: lo que da el mar o lo que da la montaña?", "Lo que da el mar", "El testimonio habla del mar."),
        ex(FICHA_PAL + " ¿Qué significa «ko» en mapuzugun?", "Agua", "La ficha de palabras lo indica."),
    ],
    C=[
        ex("Verdadero o falso: un relato fundacional puede relacionarse con el territorio de la comunidad que lo cuenta.", "Verdadero", "En el ejemplo, el mar y la roca están en la bahía."),
        ex("¿Quién explica por qué un relato importa a una comunidad? A) la comunidad que lo cuenta B) quien lo mira de lejos", "A", "Ella conoce su sentido."),
        ex("Verdadero o falso: con saber que «ko» es agua ya puedo explicar toda la cultura mapuche.", "Falso", "Una palabra suelta no explica una cultura."),
    ],
    A=[
        ex("Une cada elemento con su papel en «La primera gota». 1) mar 2) roca. a) de ella salieron las primeras personas b) nació de la gota", "1-b, 2-a", "El mar nace de la gota; las personas salen de la roca."),
        ex("Testimonio de doña Marta: «Por este relato no se tira basura al mar». Escribe una frase que relacione relato y cuidado, empezando con «Según doña Marta…».", "Según doña Marta, por el relato no se tira basura al mar", "La frase atribuye la relación a la fuente."),
        ex(FICHA_PAL + " ¿Qué dos palabras de la ficha nombran elementos del cielo: «antü» y «kuyen» o «ko» y «mapu»?", "antü y kuyen", "Sol y luna están en el cielo."),
    ],
    Z=[
        ex("Luis afirma: «Como en el relato aparece el mar, en Bahía Serena celebran una fiesta el mismo día cada año». ¿Qué datos inventó?", "La fiesta y la fecha", "El testimonio no habla de fiestas."),
        ex("Un compañero dice: «Como la ficha de palabras trae «ko», el relato de Bahía Serena es mapuche». ¿Qué error comete?", "Mezcla un relato inventado con una ficha de palabras", "El relato es inventado y no es de ningún pueblo."),
    ],
    D=[
        ex("Elige la frase que relaciona bien: A) «Según doña Marta, por el relato no se tira basura al mar» B) «Todos los pueblos cuidan el mar por sus relatos»", "A", "La B generaliza y no atribuye a una fuente."),
        ex("¿Quién puede decir por qué la comunidad de Bahía Serena da importancia al mar? A) la comunidad B) quien lee el relato y lo imagina", "A", "El sentido lo da la comunidad."),
    ],
    context=[ex("Para una exposición, una niña quiere explicar por qué un relato de su zona importa a la comunidad, pero no conoce a nadie que lo cuente. ¿Qué es lo más adecuado? A) preguntar al educador tradicional o a una persona de la comunidad B) explicarlo según lo que le parezca", "A", "La importancia la explica la comunidad.")],
    selfcheck=[
        ex("Escribe una relación que existe entre «La primera gota» y la bahía de la ficha.", "El mar, la arena y la roca aparecen en el relato y en la bahía", "Así el relato se vincula con el territorio."),
        ex("¿Qué palabra usas para indicar de quién viene una idea: «según» o «tal vez»?", "Según", "Indica la fuente de la idea."),
        ex("Verdadero o falso: una palabra de la ficha basta para explicar el pensamiento de un pueblo.", "Falso", "Hace falta la voz de la comunidad."),
    ],
    task=T("Lee el testimonio inventado de don Anselmo, de Cumbre Blanca: «En Cumbre Blanca, cuando llega la primavera, cuidamos el primer pasto que sale. Así recordamos el relato de la semilla de luz.» Haz una tabla con tres columnas: «Elemento del relato», «Elemento del territorio» y «Cómo se cuida». Escribe una frase con «Según don Anselmo…» y otra con «Yo pienso…». No inventes ceremonias ni fechas; usa solo lo que dice el testimonio.",
           "Elemento del relato: el primer pasto. Elemento del territorio: los pastizales. Cómo se cuida: cuidando el primer pasto en primavera. Según don Anselmo, se cuida el primer pasto que sale en primavera. Yo pienso que es una forma de recordar el relato.",
           ["relaciona relato y territorio", "atribuye la relación a la fuente", "separa lo que dice la fuente de lo que piensa"], ["tabla de tres columnas", "dos frases rotuladas"], ["inventar ceremonias o fechas", "generalizar a otros pueblos"],
           "Pedir que señale en qué línea del testimonio está cada dato; valorar que no agregue ritos."),
    reinforce="Dibuja tres elementos del relato «La primera gota» y escribe al lado dónde aparecen en el territorio de Bahía Serena.",
    extend="Escribe por qué la importancia de un relato la explican las comunidades y no quienes lo escuchan de visita.",
)

L(
    LF1, 4,
    materials=MAT,
    use="Aprenderé a construir una respuesta atribuida sobre un relato fundacional: decir qué explica el relato y de quién viene lo que afirmo. Sirve para hablar del origen del mundo sin adueñarme de la voz de nadie.",
    prior=["Sé relacionar un relato con el territorio de la comunidad.", "Sé usar «según» para atribuir una idea."],
    explain=[
        "Una respuesta atribuida es una respuesta que dice de dónde sale cada idea. Para responder «¿qué explica este relato sobre el origen del mundo?» usamos una estructura de tres partes: primero la fuente («Según doña Marta, en el relato de Bahía Serena…»), luego la idea del relato y por último un dato del texto que la apoya.",
        "Una respuesta atribuida también deja ver lo que no sabemos. Si el relato no cuenta algo, escribimos «el relato no dice…». Y cuando damos nuestra opinión, la separamos con «Yo pienso…». Así quien lee distingue la voz de la comunidad de la nuestra y sabe qué puede verificar.",
        "Una respuesta no atribuida suena como si fuera un hecho de todos: «El mundo nació de una gota». Eso mezcla una historia de una comunidad con una afirmación general. Lo correcto es decir: «Según el relato que cuenta doña Marta, el mar nació de una gota». Esa diferencia es pequeña, pero cambia el respeto con que hablamos.",
    ],
    vocab=[("atribuir", "decir de quién viene una idea"), ("apoyar", "mostrar un dato del texto que respalda lo que afirmo"), ("estructura", "orden de las partes de una respuesta"), ("opinión", "lo que yo pienso, separado de lo que dice la fuente"), ("afirmación general", "frase que parece valer para todos")],
    worked=[
        W("Armar una respuesta", RELATO_A + " Responde en una frase: ¿qué explica el relato sobre el origen del mar?", ["Fuente: relato que cuenta doña Marta.", "Idea: el mar nació de una gota.", "Apoyo: la gota cayó y brilló en la sombra."], "Según el relato que cuenta doña Marta, el mar nació de una gota que brilló en la sombra."),
        W("Corregir una respuesta sin fuente", "Respuesta: «El mundo nació de una gota». ¿Qué le falta?", ["No dice de quién viene la idea.", "Parece valer para todos."], "Falta atribuirla: «Según el relato de doña Marta, el mar nació de una gota»."),
    ],
    mistakes=[
        M("Escribir una idea del relato como si fuera un hecho de todos.", "Es una historia de una comunidad.", "Empiezo con «Según…» y nombro la fuente."),
        M("Mezclar mi opinión con lo que dice la fuente.", "El lector no sabe qué viene del relato.", "Separo con «Yo pienso…»."),
    ],
    R=[
        ex("Completa: «Según doña Marta, el mar nació de una ___». Escribe la palabra que falta.", "gota", "El relato lo dice así."),
        ex("¿Cuál frase atribuye la idea? A) «Según don Anselmo, salió el primer pasto» B) «Salió el primer pasto»", "A", "La A nombra la fuente."),
        ex("¿Con qué palabras separo mi opinión de lo que dice la fuente: «Yo pienso…» o «Según…»?", "Yo pienso", "Esas palabras marcan la voz propia."),
    ],
    C=[
        ex("Las tres partes de una respuesta atribuida son: fuente, idea del relato y… A) un dato del texto que la apoya B) un chiste", "A", "El apoyo sale del texto."),
        ex("Verdadero o falso: «El mundo nació de una gota» es una frase bien atribuida.", "Falso", "No dice de quién viene la idea."),
        ex("Si el relato no cuenta un dato, ¿qué escribo: «el relato no dice…» o una idea inventada?", "El relato no dice…", "Así se declara el límite del texto."),
    ],
    A=[
        ex("Ordena para formar una respuesta atribuida: a) porque la gota brilló en la sombra b) el mar nació de una gota c) Según el relato de doña Marta. Escribe las letras.", "c, b, a", "Primero la fuente, luego la idea y al final el apoyo."),
        ex(RELATO_B + " Elige la respuesta atribuida: A) «Según el relato de don Anselmo, el primer pasto salió cuando el hielo se quebró» B) «El pasto salió del hielo en todo el mundo»", "A", "La A nombra la fuente y se apoya en el texto."),
        ex(RELATO_B + " Completa con un dato del texto: «Según don Anselmo, la semilla de luz bajó del ___».", "cielo", "El relato dice que la semilla bajó del cielo."),
    ],
    Z=[
        ex("Rosa escribe: «Según doña Marta, las personas salieron de la roca. Yo creo que doña Marta quiere que cuidemos la bahía». ¿Qué frase es opinión de Rosa?", "Yo creo que doña Marta quiere que cuidemos la bahía", "Es una interpretación que no está en el relato."),
        ex("Dos respuestas a «¿qué explica el relato de Cumbre Blanca?». R1: «Según don Anselmo, el mundo dormía bajo el hielo». R2: «Los pueblos creen que el mundo dormía». ¿Cuál es más respetuosa con la fuente?", "R1", "La R2 generaliza a todos los pueblos."),
    ],
    D=[
        ex("Camilo escribe: «Según doña Marta, el mar nació de una gota, y en la segunda parte las personas hicieron un pueblo». Si la segunda parte no se cuenta fuera de la comunidad, ¿qué error cometió?", "Contó la parte reservada", "Inventó o repitió lo que la ficha reserva."),
        ex("Para responder bien «¿cómo aparecen las personas en el relato de Cumbre Blanca?», ¿qué frase usarías? A) «Según don Anselmo, el pasto llamó al viento y el viento llamó a las personas» B) «Las personas aparecieron por el viento»", "A", "La A cita la fuente y el orden del relato."),
    ],
    context=[ex("En una prueba te preguntan: «¿Qué explica el relato de Bahía Serena?». ¿Qué respuesta pones? A) «Según el relato que cuenta doña Marta, el mar nació de una gota» B) «El mar nació de una gota, todo el mundo lo sabe»", "A", "La A atribuye la idea a la fuente.")],
    selfcheck=[
        ex("Escribe qué palabra al inicio de la respuesta indica de quién viene la idea.", "Según", "Indica la fuente."),
        ex("Verdadero o falso: mi opinión se escribe con «Yo pienso…» y va separada.", "Verdadero", "Así se distingue de la fuente."),
        ex("Verdadero o falso: puedo contar la parte que la ficha reserva si la respuesta lo necesita.", "Falso", "El límite se respeta aunque falte información."),
    ],
    task=T("Responde por escrito: «¿Qué explica el relato “La primera gota” sobre el origen del mar y de las personas?». Usa el relato: «" + RELATO_A.split("«", 2)[2].rstrip("»") + "». Tu respuesta debe tener tres partes: la fuente («Según el relato que cuenta doña Marta…»), la idea y un dato del texto que la apoye. Añade una frase con «El relato no dice…» y otra con «Yo pienso…».",
           "Según el relato que cuenta doña Marta, el mar nació de una gota que brilló en la sombra y las personas salieron de una roca. El relato no dice cómo se llamaban las personas. Yo pienso que el relato explica el origen con elementos de la bahía.",
           ["atribuye la fuente", "incluye un dato del texto", "declara un límite y separa la opinión"], ["respuesta de cuatro frases"], ["escribir una afirmación general", "mezclar opinión y fuente"],
           "Pedir que subraye fuente, idea y apoyo; valorar que no use la parte reservada."),
    reinforce="Reescribe estas dos frases con «Según…»: «El pasto salió del hielo» y «El mar nació de una gota».",
    extend="Escribe una respuesta atribuida sobre «La semilla de luz» con fuente, idea, apoyo y límite.",
)

L(
    LF1, 5,
    materials=MAT,
    use="Aprenderé a comparar dos relatos fundacionales sin decir que uno es mejor o más verdadero. Sirve para respetar las diferentes formas de comprender el origen del mundo.",
    prior=["Sé responder de forma atribuida sobre un relato.", "Sé que cada comunidad cuenta el origen a su manera."],
    explain=[
        "Contrastar es mirar dos cosas y decir en qué se parecen y en qué se diferencian. Dos relatos fundacionales pueden explicar el origen del mundo de maneras distintas: uno parte de una gota y otro de una semilla de luz. Esas diferencias no significan que uno esté bien y el otro mal: cada comunidad entiende el origen desde su territorio y su historia.",
        "Jerarquizar es decir que algo es «mejor», «más verdadero» o «más importante» que otra cosa. Cuando contrastamos relatos no jerarquizamos. Usamos criterios neutros: cómo comienza, qué aparece primero, qué elementos del territorio incluye y cómo llegan las personas. Con esos criterios armamos una tabla y comparamos sin juzgar.",
        "La ciencia también explica el origen del mundo, pero lo hace con evidencia que se puede medir y comprobar. Un relato fundacional responde a otra pregunta: qué sentido tiene el origen para quienes lo cuentan. Son formas distintas de comprender el mundo, y ninguna tiene que borrar a la otra para ser respetada.",
    ],
    vocab=[("contrastar", "decir en qué se parecen y en qué se diferencian dos cosas"), ("jerarquizar", "poner una cosa por encima de otra, como «mejor» o «más verdadera»"), ("criterio", "regla para comparar"), ("evidencia", "dato que se puede medir o comprobar"), ("neutro", "que no favorece a ninguna de las partes")],
    worked=[
        W("Comparar con un criterio", RELATO_A + " " + RELATO_B + " Criterio: cómo empieza cada relato.", ["La primera gota: silencio y una sombra grande.", "La semilla de luz: el mundo dormía bajo el hielo."], "Empiezan distinto: uno con silencio y sombra, otro con el mundo dormido bajo el hielo."),
        W("Evitar jerarquizar", "Una compañera dice: «El relato de la gota es mejor que el de la semilla porque tiene mar». ¿Qué cambia para no jerarquizar?", ["«Mejor» pone un relato sobre otro.", "Puedo decir qué elementos tiene cada uno."], "«El relato de Bahía Serena incluye el mar; el de Cumbre Blanca incluye el hielo y el pasto»."),
    ],
    mistakes=[
        M("Decir que un relato es más verdadero que otro.", "Cada comunidad lo comprende desde su territorio.", "Comparo con criterios como inicio, elementos y llegada de las personas."),
        M("Pensar que el relato y la ciencia se contradicen siempre.", "Responden preguntas de maneras distintas.", "Explico qué responde cada uno sin descalificar a ninguno."),
    ],
    R=[
        ex(RELATO_A + " ¿Qué elemento da origen al mar: una gota o una semilla de luz?", "Una gota", "Así lo cuenta el relato de Bahía Serena."),
        ex(RELATO_B + " ¿Qué sale primero después de que se quiebra el hielo?", "El primer pasto", "El relato lo dice así."),
        ex("Contrastar significa: A) decir en qué se parecen y en qué se diferencian dos cosas B) decidir cuál es mejor", "A", "Contrastar no es jerarquizar."),
    ],
    C=[
        ex("Verdadero o falso: «más verdadero» es una forma de jerarquizar.", "Verdadero", "Pone un relato sobre otro."),
        ex("¿Cuál es un criterio neutro para comparar relatos? A) cómo comienzan B) cuál me gusta más", "A", "El criterio neutro se puede verificar en el texto."),
        ex("Verdadero o falso: dos relatos pueden ser distintos y ambos merecer respeto.", "Verdadero", "Cada uno responde a su comunidad."),
    ],
    A=[
        ex("Compara con el criterio «cómo llegan las personas». En «La primera gota» las personas salen de una roca; en «La semilla de luz» las llama el viento. Escribe la diferencia.", "En uno salen de una roca y en el otro las llama el viento", "La diferencia se ve en el texto de cada relato."),
        ex("¿En cuál de los dos relatos aparece el hielo: «La primera gota» o «La semilla de luz»?", "En La semilla de luz", "El hielo está solo en el relato de Cumbre Blanca."),
        ex("Une cada relato con un elemento propio. 1) La primera gota 2) La semilla de luz. a) pasto b) arena", "1-b, 2-a", "La arena aparece en el primero y el pasto en el segundo."),
    ],
    Z=[
        ex("Pedro escribe: «El relato de Cumbre Blanca está mal porque no tiene mar». ¿Qué error comete?", "Lo juzga con un criterio que no es el suyo", "Cada relato incluye elementos de su territorio."),
        ex("Un compañero dice: «La ciencia dice cuándo se formó el mar y el relato dice que fue una gota, así que el relato es falso». ¿Qué falta aclarar? A) responden preguntas distintas B) uno miente", "A", "El relato da sentido; la ciencia mide evidencia."),
    ],
    D=[
        ex("Hay una semejanza entre ambos relatos. ¿Cuál es? A) algo pequeño inicia el cambio B) todo empieza en el mar", "A", "La gota y la semilla son pequeñas."),
        ex("Elige la frase que contrasta sin jerarquizar: A) «El relato de Bahía Serena parte de una gota y el de Cumbre Blanca de una semilla de luz» B) «El de Cumbre Blanca es más bonito»", "A", "Describe diferencias y no juzga."),
    ],
    context=[ex("En tu curso discuten cuál de dos relatos de origen es «el verdadero». ¿Qué le propones al curso? A) comparar qué incluye cada relato y de qué comunidad viene B) votar el mejor", "A", "Se contrasta y no se vota por jerarquía.")],
    selfcheck=[
        ex("Escribe una palabra que muestre que estoy jerarquizando.", "Mejor, peor o más verdadero", "Esas palabras ponen un relato sobre otro."),
        ex("Nombra un criterio neutro para comparar relatos.", "Cómo comienza, qué aparece primero, qué elementos incluye o cómo llegan las personas", "Se pueden comprobar en el texto."),
        ex("Verdadero o falso: el relato fundacional responde a la pregunta por el sentido del origen, no solo por los datos.", "Verdadero", "Cumple una función cultural."),
    ],
    task=T("Compara los dos relatos de práctica. «La primera gota»: «" + RELATO_A.split("«", 2)[2].rstrip("»") + "». «La semilla de luz»: «" + RELATO_B.split("«", 2)[2].rstrip("»") + "». Haz una tabla con tres criterios: «cómo comienza», «qué aparece primero» y «cómo llegan las personas». Escribe una semejanza y una diferencia. Cierra con una frase que explique por qué no se debe decir cuál es mejor.",
           "Comienza: silencio con una sombra / el mundo dormía bajo el hielo. Aparece primero: el mar / el pasto. Personas: salen de la roca / las llama el viento. Semejanza: algo pequeño inicia el cambio. Diferencia: uno parte del mar y otro del hielo. No se dice cuál es mejor porque cada comunidad entiende el origen desde su territorio.",
           ["usa criterios neutros", "señala una semejanza y una diferencia", "no jerarquiza"], ["tabla de tres criterios", "dos frases de contraste", "frase de cierre"], ["escribir «mejor» o «más verdadero»", "inventar datos que no están en los textos"],
           "Pedir que ubique cada celda en el texto; valorar que cambie los juicios por descripciones."),
    reinforce="Completa en tu hoja una tabla con dos columnas, «La primera gota» y «La semilla de luz», con solo lo que dice cada texto.",
    extend="Explica con tus palabras por qué un relato y una explicación científica del origen del mundo pueden convivir.",
)

L(
    LF1, 6,
    materials=MAT,
    use="Aprenderé a comunicar un relato fundacional y a revisar mi trabajo con validación pertinente. Sirve para compartir lo que aprendí sin adueñarme del relato y para corregir errores antes de entregar.",
    prior=["Sé responder de forma atribuida y contrastar relatos sin jerarquizar.", "Sé que lo tradicional lo valida el educador o la comunidad."],
    explain=[
        "Comunicar un relato fundacional es presentarlo a otras personas. En la escuela lo hacemos con respeto: decimos de qué comunidad viene, quién lo cuenta y qué permiso hay. Contamos solo lo que está autorizado y usamos «según…» para atribuir. No cambiamos el relato ni lo adornamos, porque eso cambiaría su sentido para la comunidad.",
        "Revisar es leer el trabajo con una lista: ¿nombré la fuente? ¿usé solo lo que el relato dice? ¿respeté el límite? ¿evité generalizar? ¿evité jerarquizar? ¿separé mi opinión? Si una respuesta es no, corrijo antes de entregar. Revisar sirve para encontrar errores propios, no para señalar los de otros.",
        "La validación pertinente es la revisión de quien sí puede decir si algo es correcto: el educador o educadora tradicional o una persona de la comunidad. Nosotros podemos revisar la estructura y el respeto, pero no podemos validar el sentido de un relato real. Antes de presentar a otras personas, mostramos el trabajo a quien corresponde.",
    ],
    vocab=[("comunicar", "presentar algo a otras personas"), ("revisar", "leer un trabajo con una lista para corregirlo"), ("validación pertinente", "revisión de quien sabe y corresponde, como el educador tradicional"), ("adornar", "agregar detalles que no están en la fuente"), ("lista de revisión", "preguntas para comprobar un trabajo")],
    worked=[
        W("Revisar un borrador", "Borrador: «Todos los pueblos cuentan que el mundo nació de una gota. Es el mejor relato.» ¿Qué dos errores tiene?", ["«Todos los pueblos» generaliza.", "«El mejor» jerarquiza."], "Generaliza y jerarquiza; falta la fuente."),
        W("Corregirlo", "Corrige el borrador anterior con la fuente doña Marta, de Bahía Serena.", ["Agrego la fuente.", "Quito «todos los pueblos» y «el mejor»."], "Según el relato que cuenta doña Marta, de Bahía Serena, el mar nació de una gota."),
    ],
    mistakes=[
        M("Entregar sin revisar.", "Pueden quedar errores de fuente o de respeto.", "Uso la lista de revisión."),
        M("Presentar el relato real sin mostrarlo antes al educador tradicional.", "Solo la comunidad valida el sentido.", "Pido validación antes de presentar."),
    ],
    R=[
        ex("¿Quién puede validar un relato real: el educador tradicional o cualquier compañero?", "El educador tradicional", "Es quien corresponde."),
        ex("Para comunicar un relato debo decir de qué comunidad viene. Verdadero o falso.", "Verdadero", "Es parte de la atribución."),
        ex("En la lista de revisión, ¿qué pregunta cuida el respeto: «¿respeté el límite?» o «¿me quedó largo?»", "¿Respeté el límite?", "Cuida lo que la comunidad reserva."),
    ],
    C=[
        ex("Revisar sirve para: A) encontrar errores propios antes de entregar B) señalar los errores de otros", "A", "Es una autoevaluación."),
        ex("Verdadero o falso: adornar un relato con detalles propios lo mejora.", "Falso", "Cambia su sentido para la comunidad."),
        ex("¿Qué es la validación pertinente? A) revisión de quien corresponde, como el educador tradicional B) revisión de cualquier persona", "A", "Es quien conoce el relato."),
    ],
    A=[
        ex("Borrador: «Según don Anselmo, el pasto llamó al viento. Es un relato mejor que otros porque tiene viento». ¿Qué frase hay que quitar?", "Es un relato mejor que otros porque tiene viento", "Esa frase jerarquiza un relato sobre otros."),
        ex("Borrador: «El relato cuenta que el mar nació de una gota». ¿Qué falta? A) la fuente B) un adorno", "A", "No dice quién cuenta ni de qué comunidad."),
        ex("Ordena los pasos para presentar: a) presento con «según…» b) pido validación c) reviso con la lista. Escribe las letras.", "c, b, a", "Se revisa, luego se valida y al final se presenta."),
    ],
    Z=[
        ex("Marta revisó su trabajo con la lista y todo está bien. ¿Puede presentarlo como validado? Responde Sí o No.", "No", "La validación la hace el educador o la comunidad."),
        ex("Un compañero propone agregar música y gestos al relato para que sea más entretenido. ¿Qué respondes? A) que primero pregunte al educador tradicional si corresponde B) que lo haga igual", "A", "No se cambia la forma del relato sin quien lo cuida."),
    ],
    D=[
        ex("Borrador: «Los pueblos de Chile creen que el mundo nació de una gota, según yo». ¿Qué problema principal tiene: generaliza y no nombra a la fuente, o está muy corto?", "Generaliza y no nombra a la fuente", "Dice «los pueblos de Chile» y no cita a doña Marta."),
        ex("Si el educador tradicional corrige una parte de tu trabajo, ¿qué haces? A) la cambio y le agradezco B) la defiendo porque yo la escribí", "A", "La validación pertinente se acepta."),
    ],
    context=[ex("Vas a presentar a tu curso lo que aprendiste de un relato. Un compañero dice que no hace falta pedir permiso porque «ya lo sabe todo el mundo». ¿Qué haces? A) pido permiso y valido con el educador B) lo presento igual", "A", "El permiso y la validación son parte de comunicar con respeto.")],
    selfcheck=[
        ex("Escribe una pregunta de la lista de revisión.", "¿Nombré la fuente? o ¿respeté el límite? o ¿separé mi opinión?", "Son preguntas de la lista."),
        ex("Verdadero o falso: yo puedo validar el sentido de un relato real.", "Falso", "Eso lo hace la comunidad."),
        ex("Nombra algo que no se cambia al comunicar un relato.", "El sentido, el orden o el límite del relato", "Cambiar eso lo deforma."),
    ],
    task=T("Escribe un borrador de cinco frases para presentar «La semilla de luz» (relato de práctica de Cumbre Blanca, fuente don Anselmo): «" + RELATO_B.split("«", 2)[2].rstrip("»") + "». Incluye la fuente, dos hechos del relato, un límite («no sé…» o «no cuento…») y una frase con «Yo pienso…». Revísalo con esta lista: fuente, solo lo que dice, límite, sin generalizar, sin jerarquizar, opinión separada. Marca con un visto cada punto que cumpliste.",
           "Según don Anselmo, de Cumbre Blanca, el mundo dormía bajo el hielo. Una semilla de luz bajó del cielo y salió el primer pasto. No sé cómo se llamaban las personas. Yo pienso que el relato habla de la luz y del pasto. Lista: fuente, solo lo que dice, límite, sin generalizar, sin jerarquizar y opinión separada, todo con visto.",
           ["cumple los seis puntos de la lista", "no agrega detalles", "pide validación"], ["borrador de cinco frases", "lista marcada"], ["generalizar a otros pueblos", "adornar el relato"],
           "Pedir que muestre cómo cumplió cada punto de la lista; valorar que escriba qué consultará al educador."),
    reinforce="Revisa con la lista de seis puntos una respuesta tuya de una clase anterior.",
    extend="Escribe una nota de agradecimiento a una persona de la comunidad que cuente un relato en tu escuela, usando «chaltumay» solo como lo dice la ficha de palabras.",
)

# ============================================================ OA LF02 · diálogo y exposición
DIALOGO1 = ("Diálogo de práctica (inventado, en castellano). Lía: Buenas tardes, don Mateo. Quisiera preguntarle por el río de nuestra comunidad. "
            "Don Mateo: Buenas tardes, Lía. Con gusto. El río da agua a las huertas. Lía: ¿Y qué se cuida del río? Don Mateo: Se cuida que el agua esté limpia. Lía: Muchas gracias.")

L(
    LF2, 1,
    materials=MAT,
    use="Aprenderé a situar un diálogo o una exposición sobre mi cultura: quién habla, con quién, sobre qué y con qué permiso. Sirve para preparar una conversación respetuosa.",
    prior=["Sé situar un relato con una ficha.", "Sé que un saludo en lengua indígena lo enseña el educador tradicional."],
    explain=[
        "Un diálogo es una conversación entre dos o más personas que se turnan para hablar. Una exposición es hablar a un grupo sobre un tema, con orden. Ambos pueden tratar sobre un aspecto de la propia cultura: el territorio, los alimentos, los oficios, la familia o los lugares de la comunidad. Cada persona habla de la cultura que vive y conoce.",
        "Antes de dialogar o exponer, situamos la conversación con una ficha: quién habla, con quién, sobre qué tema, en qué lugar y con qué permiso. Si el tema incluye algo de otra persona, como un oficio o una historia familiar, pedimos permiso para contarlo. No contamos datos privados ni lo que la comunidad reserva.",
        "La lengua indígena aparece en el diálogo con vocabulario variado y pertinente, es decir, con palabras que corresponden al tema. La pronunciación adecuada la enseña el educador tradicional o una persona de la comunidad, que dicen la palabra para repetirla. En este cuaderno practicamos con castellano y con unas pocas palabras de las fichas.",
    ],
    vocab=[("diálogo", "conversación entre dos o más personas que se turnan"), ("exposición", "presentación ordenada de un tema ante un grupo"), ("tema", "de qué se habla"), ("turno", "momento en que le toca hablar a cada persona"), ("pertinente", "que corresponde al tema o a la situación")],
    worked=[
        W("Situar un diálogo", DIALOGO1 + " ¿Quién habla con quién y sobre qué tema?", ["Hablan Lía y don Mateo.", "El tema es el río de la comunidad."], "Lía conversa con don Mateo sobre el río de la comunidad."),
        W("Pedir permiso", "Lía quiere contar en su exposición un oficio de don Mateo. ¿Qué hace antes?", ["El oficio es de don Mateo.", "Debe pedirle permiso."], "Pregunta a don Mateo si puede contarlo."),
    ],
    mistakes=[
        M("Hablar de la cultura de otras personas como si fuera la mía.", "Cada persona cuenta lo que vive y conoce.", "Hablo de mi propia cultura y atribuyo lo que me contaron."),
        M("Practicar pronunciación de lengua indígena escribiendo cómo creo que suena.", "La pronunciación la enseñan quienes hablan la lengua.", "Pido al educador tradicional que diga la palabra y la repito."),
    ],
    R=[
        ex("En el diálogo de Lía y don Mateo, ¿sobre qué cosa conversan: el río o el patio?", "El río", "El diálogo es sobre el río de la comunidad."),
        ex("En un diálogo, cada persona espera su: A) turno B) premio", "A", "Los turnos ordenan quién habla."),
        ex("Una exposición es: A) una presentación ordenada ante un grupo B) una conversación sin tema", "A", "Se presenta un tema con orden."),
    ],
    C=[
        ex("Verdadero o falso: puedo contar el oficio de otra persona sin avisarle.", "Falso", "Se pide permiso."),
        ex("¿Qué significa «pertinente»? A) que corresponde al tema B) que es largo", "A", "Pertinente es lo adecuado al tema."),
        ex("¿Quién enseña la pronunciación adecuada de una palabra en lengua indígena: el educador tradicional o un diccionario inventado por mí?", "El educador tradicional", "Es quien habla la lengua o la conoce."),
    ],
    A=[
        ex(DIALOGO1 + " ¿Qué dice don Mateo que da el río?", "Agua a las huertas", "Lo dice en su primer turno."),
        ex("Une cada dato con la ficha de un diálogo. 1) quién habla 2) tema 3) permiso. a) el río b) Lía y don Mateo c) don Mateo autoriza", "1-b, 2-a, 3-c", "Cada dato responde una pregunta de la ficha."),
        ex(DIALOGO1 + " ¿Cuántas veces habla Lía?", "Tres veces", "Lía habla al saludar y preguntar por el río, al preguntar qué se cuida y al agradecer."),
    ],
    Z=[
        ex("Tomás quiere exponer sobre el oficio de su vecina, pero no le preguntó. ¿Qué error comete?", "No pidió permiso", "El oficio es de su vecina."),
        ex("Ana dice que va a mostrar cómo se pronuncia una palabra indígena «como suena». ¿Qué le falta? A) pedir que lo enseñe el educador tradicional B) anotarla de oído", "A", "La pronunciación se aprende de quien habla la lengua."),
    ],
    D=[
        ex("Dos diálogos: en el primero los turnos son ordenados; en el segundo todos hablan a la vez. ¿Cuál permite escuchar bien?", "El primero", "Los turnos ordenados ayudan a entender."),
        ex("Si la comunidad dice que un tema no se cuenta fuera de ella, ¿puedes usarlo en tu exposición? Responde Sí o No.", "No", "Es un límite de la comunidad."),
    ],
    context=[ex("Tu curso invita a una persona de la comunidad a conversar. Antes de empezar, ¿qué preguntas? A) sobre qué temas puede hablar y si se puede anotar B) cuánto cobra", "A", "Sitúa el tema y el permiso.")],
    selfcheck=[
        ex("Nombra dos datos de la ficha de un diálogo.", "Dos entre: quién habla, con quién, tema, lugar, permiso", "Son datos de la ficha."),
        ex("Verdadero o falso: cada persona habla de la cultura que vive y conoce.", "Verdadero", "No se habla por otros."),
        ex("¿Qué haces si no sabes pronunciar una palabra indígena? A) pido al educador tradicional que la diga B) la invento", "A", "Se aprende de quien la habla."),
    ],
    task=T("Lee este diálogo de práctica: «" + DIALOGO1.split("castellano). ", 1)[1] + "» Completa una ficha con: quién habla, con quién, tema, lugar (usa «en la sede de la comunidad») y permiso. Después escribe dos preguntas más que Lía podría hacerle a don Mateo sobre el río y una pregunta que tú harías al educador tradicional.",
           "Quién habla: Lía. Con: don Mateo. Tema: el río de la comunidad. Lugar: en la sede. Permiso: don Mateo autoriza. Preguntas: ¿Qué animales viven en el río? ¿En qué época baja más agua? Mi pregunta: ¿cómo se dice «río» en nuestra lengua?",
           ["completa los cinco datos", "formula preguntas pertinentes", "incluye una consulta al educador"], ["ficha completa", "tres preguntas"], ["inventar palabras en lengua indígena", "hablar por la cultura de otros"],
           "Pedir que muestre en qué parte del diálogo está cada dato; valorar que no invente palabras."),
    reinforce="Copia el diálogo y marca con un color cada turno de Lía y con otro cada turno de don Mateo.",
    extend="Escribe un diálogo de cuatro turnos entre dos estudiantes que conversan sobre un lugar de su comunidad.",
)

DIALOGO2 = ("Diálogo de práctica (inventado, en castellano). Sofía: Mari mari, doña Clara. Doña Clara: Mari mari, Sofía. Sofía: ¿Usted cultiva papas en su huerta? "
            "Doña Clara: Sí, y también habas. Sofía: ¿Cómo sabe cuándo están listas? Doña Clara: Miro las hojas: cuando se ponen amarillas, ya se pueden sacar. Sofía: Chaltumay, doña Clara.")

L(
    LF2, 2,
    materials=MAT + " " + FICHA_PAL,
    use="Aprenderé a escuchar un diálogo con límites declarados: qué dijo cada persona, qué no dijo y qué se reserva. Sirve para participar en una conversación sin inventar lo que otra persona no contó.",
    prior=["Sé situar un diálogo y pedir permiso.", "Sé que «mari mari» es un saludo y «chaltumay» es «gracias» en mapuzugun."],
    explain=[
        "Escuchar bien un diálogo significa seguir quién habla en cada turno, de qué habla y qué responde. Anotamos las ideas principales con palabras propias y nombramos a quién pertenece cada dato: «Doña Clara dice que…». Así nunca atribuimos a una persona lo que dijo otra ni lo que no dijo.",
        "Escuchar con límites declarados quiere decir distinguir tres cosas: lo que se dijo, lo que no se dijo y lo que la persona prefiere reservar. Si alguien responde «eso no lo cuento», se respeta. Si no se contó algo, no se completa con ideas propias. Si no entendemos, pedimos que lo repitan con amabilidad.",
        "En el diálogo de Sofía y doña Clara aparecen saludos y agradecimientos en mapuzugun, como «mari mari» y «chaltumay», que están en la ficha de palabras. La forma de decirlos en cada situación y la pronunciación las enseña el educador tradicional o una persona de la comunidad. Practicar es repetirlas con quien las habla.",
    ],
    vocab=[("idea principal", "lo más importante que dice una persona"), ("turno de habla", "momento en que una persona habla"), ("reservar", "guardar algo y no contarlo"), ("repetir", "volver a decir para entender mejor"), ("saludo", "palabra o frase con la que se empieza una conversación")],
    worked=[
        W("Anotar ideas principales", DIALOGO2 + " ¿Qué dice doña Clara de cómo saber que están listas?", ["Busco su respuesta.", "Dice que mira las hojas y que, si están amarillas, se pueden sacar."], "Doña Clara dice que las papas están listas cuando las hojas se ponen amarillas."),
        W("Distinguir lo que no se dijo", DIALOGO2 + " ¿Dice doña Clara cuándo se siembran las papas?", ["Reviso sus respuestas.", "No habla de la siembra."], "No: ese dato no se dijo."),
    ],
    mistakes=[
        M("Atribuir una respuesta a la persona equivocada.", "Cada turno es de una persona.", "Anoto el nombre al lado de cada idea."),
        M("Completar con mis ideas lo que no se dijo.", "Mezclo mi voz con la de la persona.", "Escribo «no se dijo» y, si quiero saber, pregunto."),
    ],
    R=[
        ex(DIALOGO2 + " ¿Qué cultiva doña Clara además de papas?", "Habas", "Lo dice en su respuesta."),
        ex(DIALOGO2 + " ¿Qué saludo usan al inicio: «mari mari» o «iorana»?", "Mari mari", "Es el saludo que aparece."),
        ex(DIALOGO2 + " ¿Cómo agradece Sofía al final?", "Chaltumay", "Es el agradecimiento que usa."),
    ],
    C=[
        ex(DIALOGO2 + " ¿Por qué sabe doña Clara que las papas están listas: por las hojas o por la fecha?", "Por las hojas", "Dice que mira las hojas."),
        ex("Verdadero o falso: si alguien no contó un dato, lo puedo completar con una idea mía.", "Falso", "Eso mezcla mi voz con la suya."),
        ex("Si no entiendes una respuesta, ¿qué haces: pido que la repita o la invento?", "Pido que la repita", "Se pregunta con respeto."),
    ],
    A=[
        ex(DIALOGO2 + " Une cada dato con quien lo dijo. 1) «las hojas se ponen amarillas» 2) «¿usted cultiva papas?» a) Sofía b) doña Clara", "1-b, 2-a", "Cada turno pertenece a una persona."),
        ex(DIALOGO2 + " ¿Cuántos turnos de habla tiene el diálogo, contando cada cambio de persona?", "Siete turnos", "Sofía habla cuatro veces y doña Clara tres, alternándose: 4 + 3 = 7."),
        ex(DIALOGO2 + " Escribe una idea principal de doña Clara con su nombre al inicio.", "Doña Clara dice que cultiva papas y habas", "La idea nombra a quien la dijo."),
    ],
    Z=[
        ex("Rafael dice: «Doña Clara contó que siembra en octubre». Según el diálogo de práctica, ¿lo dijo? Responde Sí o No.", "No", "No habla de la siembra."),
        ex("Doña Clara responde a otra pregunta: «Eso no lo cuento». ¿Qué hace quien escucha? A) respeta y sigue con otro tema B) insiste hasta que lo diga", "A", "El límite de la persona se respeta."),
    ],
    D=[
        ex("Dos compañeros resumen el diálogo. Uno: «Doña Clara dice que mira las hojas». Otro: «Doña Clara dice que todos los pueblos miran las hojas». ¿Cuál se mantiene en lo que se dijo?", "El primero", "El segundo generaliza a todos los pueblos."),
        ex("En el diálogo hay dos palabras de la ficha de palabras. ¿Cuáles son?", "Mari mari y chaltumay", "Son el saludo y el agradecimiento en mapuzugun."),
    ],
    context=[ex("Una vecina te cuenta cómo cultiva su huerta y de pronto dice «eso último no es para contarlo». Mientras anotas, ¿qué haces? A) borro eso de mis apuntes B) lo dejo por si acaso", "A", "Respeto su límite y no lo registro.")],
    selfcheck=[
        ex("Escribe las tres cosas que se distinguen al escuchar con límites.", "Lo que se dijo, lo que no se dijo y lo que se reserva", "Son los tres límites del diálogo."),
        ex("¿Quién enseña la pronunciación de «mari mari»: el educador tradicional o mi imaginación?", "El educador tradicional", "La pronunciación se aprende de quien habla la lengua."),
        ex("Verdadero o falso: anotar el nombre de quien dijo cada idea evita atribuir mal.", "Verdadero", "Cada idea queda con su voz."),
    ],
    task=T("Lee este diálogo de práctica: «" + DIALOGO2.split("castellano). ", 1)[1] + "» Haz una tabla con tres columnas: «Lo que se dijo» (tres ideas con el nombre de quien las dijo), «Lo que no se dijo» (dos datos que no aparecen) y «Mis preguntas» (dos preguntas que harías). Marca con un círculo las palabras de la ficha de palabras que aparecen.",
           "Se dijo: Doña Clara cultiva papas y habas; mira las hojas para saber si están listas; Sofía agradece con «chaltumay». No se dijo: cuándo se siembra; cuánto rinde la huerta. Preguntas: ¿Cuándo siembra? ¿Qué cuidados necesitan las habas? Palabras: mari mari, chaltumay.",
           ["registra ideas con su autor", "identifica lo que no se dijo", "formula preguntas pertinentes"], ["tabla de tres columnas", "palabras marcadas"], ["atribuir lo dicho a otra persona", "completar con datos propios"],
           "Pedir que señale en el diálogo la línea de cada idea; valorar que no complete con invenciones."),
    reinforce="Escribe tres turnos del diálogo en orden, con el nombre de quien habla.",
    extend="Escribe dos preguntas respetuosas que servirían para saber más sobre la huerta de doña Clara.",
)

L(
    LF2, 3,
    materials=MAT,
    use="Aprenderé a elegir vocabulario variado y pertinente para conversar sobre un aspecto de mi cultura y a reconocer cómo las palabras se relacionan con el tema. Sirve para hablar con precisión y sin repetir siempre las mismas palabras.",
    prior=["Sé escuchar un diálogo con límites declarados.", "Sé que el vocabulario indígena lo enseña quien habla la lengua."],
    explain=[
        "El vocabulario son las palabras que usamos. Un vocabulario variado evita repetir siempre las mismas palabras: en vez de «cosa» o «bonito» decimos una palabra más precisa. Un vocabulario pertinente usa las palabras que corresponden al tema: si hablamos de la pesca en una caleta, usamos «red», «bote» y «marea», y no «semáforo».",
        "Las palabras de un tema se relacionan entre sí. «Siembra», «cosecha», «semilla» y «huerta» pertenecen al tema del cultivo. Agrupar palabras por tema nos ayuda a preparar un diálogo. Si queremos usar una palabra en lengua indígena, la tomamos de una fuente confiable, como el educador tradicional, y no la inventamos ni la traducimos por nuestra cuenta.",
        "Hay palabras que cada comunidad usa de manera especial, y su significado completo lo explican las personas que las usan. Cuando exponemos, decimos «en mi comunidad se usa la palabra…» solo si sabemos con certeza. Si no, preguntamos. En la ficha de palabras tenemos algunas que sí podemos usar: ko, mapu, antü, kuyen, ruka y ñuke en mapuzugun.",
    ],
    vocab=[("vocabulario", "conjunto de palabras que usamos"), ("variado", "que no repite siempre lo mismo"), ("preciso", "que dice justo lo que se quiere decir"), ("campo semántico", "grupo de palabras de un mismo tema"), ("traducir", "pasar una palabra de una lengua a otra")],
    worked=[
        W("Elegir palabras pertinentes", "Tema: la pesca en una caleta. Palabras: red, bote, marea, semáforo. ¿Cuál no corresponde?", ["Pienso en el tema: pesca.", "El semáforo es del tránsito en la ciudad."], "Semáforo no es pertinente."),
        W("Variar el vocabulario", "Texto: «La playa es bonita y el mar es bonito». Cambia una palabra repetida por una más precisa.", ["«Bonito» se repite.", "Elijo otra que diga más: tranquilo, limpio, amplio."], "«La playa es amplia y el mar es tranquilo»."),
    ],
    mistakes=[
        M("Traducir por mi cuenta una palabra de lengua indígena.", "Puedo dar un significado incorrecto.", "Uso la ficha o pregunto al educador tradicional."),
        M("Repetir «cosa» para todo.", "El mensaje queda poco claro.", "Busco una palabra más precisa del tema."),
    ],
    R=[
        ex("Tema: el cultivo. ¿Cuál palabra corresponde: cosecha o semáforo?", "Cosecha", "La cosecha pertenece al cultivo."),
        ex(FICHA_PAL + " ¿Cómo se dice «casa» en mapuzugun, según la ficha?", "ruka", "La ficha de palabras lo indica."),
        ex("Texto: «Me gusta el río. Me gusta el cerro. Me gusta el cielo». ¿Qué expresión se repite al comienzo de las tres frases?", "Me gusta", "Las tres frases empiezan igual."),
    ],
    C=[
        ex("Un vocabulario variado es: A) uno que no repite siempre las mismas palabras B) uno con palabras muy largas", "A", "Variado significa diverso."),
        ex("Verdadero o falso: puedo inventar el significado de una palabra indígena si suena parecido.", "Falso", "El significado lo da quien habla la lengua."),
        ex("Palabras: semilla, siembra, cosecha, red. ¿Cuál no pertenece al tema del cultivo?", "red", "La red es del tema de la pesca."),
    ],
    A=[
        ex("Tema: la pesca en una caleta. Escribe la que no corresponde: bote, red, marea, semáforo, anzuelo.", "semáforo", "No pertenece al tema."),
        ex("¿Cuál frase reemplaza «El agua del río está buena» con una palabra más precisa? A) «El agua del río está limpia» B) «El agua del río está cosa»", "A", "«Limpia» dice cómo es el agua; «cosa» no dice nada."),
        ex(FICHA_PAL + " Une cada palabra con su significado. 1) ko 2) mapu 3) antü. a) tierra b) sol c) agua", "1-c, 2-a, 3-b", "La ficha de palabras lo indica."),
    ],
    Z=[
        ex("Un compañero dice que «ñuke» significa «padre» porque suena parecido a «niño». ¿Qué error comete?", "Inventa el significado por parecido", "En la ficha, «ñuke» es madre."),
        ex("Para presentar el tema «la huerta de la comunidad», ¿qué conjunto de palabras es más pertinente? A) semilla, riego, cosecha, hortaliza B) pelota, cancha, arco, árbitro", "A", "Las del conjunto A pertenecen al cultivo."),
    ],
    D=[
        ex("¿Cuál frase usa palabras pertinentes al tema de la huerta? A) «Con la semilla y el riego llega la cosecha.» B) «Con la semilla y el árbitro llega la cancha.»", "A", "Semilla, riego y cosecha son del cultivo; árbitro y cancha, del deporte."),
        ex("Si quieres usar en tu exposición una palabra de la lengua de tu comunidad y no la conoces con certeza, ¿qué haces? A) pregunto al educador o a una persona de la comunidad B) uso la que me suene mejor", "A", "Solo ellos validan el uso correcto."),
    ],
    context=[ex("En una exposición sobre la pesca en la caleta, un niño dice varias veces «cosa». ¿Qué le sugieres? A) cambiar «cosa» por palabras precisas como red o bote B) hablar más rápido", "A", "La precisión ayuda a entender.")],
    selfcheck=[
        ex("Nombra una palabra pertinente para el tema de la pesca.", "Red, bote, marea o anzuelo", "Pertenecen al tema."),
        ex("Verdadero o falso: «cosa» es una palabra precisa.", "Falso", "Es una palabra muy general."),
        ex("¿Dónde puedo comprobar el significado de una palabra indígena de mi comunidad? A) con el educador tradicional B) adivinando", "A", "Es la fuente adecuada."),
    ],
    task=T("Elige el tema «los lugares de mi comunidad». Escribe una lista de ocho palabras pertinentes en castellano (por ejemplo: plaza, sede, escuela, huerta, río, cerro, caleta, camino). Marca con un círculo dos que usarías en un diálogo. Después escribe un diálogo de cuatro turnos que las use sin repetir «cosa» ni «bonito». Si quieres añadir una palabra de la lengua de tu comunidad, pregunta antes al educador tradicional y anota quién te la enseñó.",
           "Lista: plaza, sede, escuela, huerta, río, cerro, caleta, camino. Círculo: huerta, río. Diálogo: Camilo: ¿Dónde se juntan en la plaza? Rosa: En la plaza nos juntamos después de la escuela. Camilo: ¿Y qué hay cerca? Rosa: Hay un camino hasta la huerta. Palabra añadida: la enseñó el educador tradicional.",
           ["lista pertinente", "diálogo de cuatro turnos", "no repite palabras vacías"], ["lista de ocho palabras", "diálogo", "fuente de la palabra"], ["traducir sin fuente", "palabras que no corresponden al tema"],
           "Pedir que explique por qué cada palabra pertenece al tema; valorar que anote la fuente."),
    reinforce="Escribe tres palabras más para cada tema: cultivo, pesca y reunión de la comunidad.",
    extend="Prepara una mini lista de cinco palabras sobre un tema de tu cultura y subraya las que debes consultar al educador tradicional.",
)

DIALOGO3 = ("Diálogo de práctica (inventado, en castellano). Julián: Quisiera presentar el oficio de tejer que conozco. Marta: Muy bien, ¿qué vas a decir primero? "
            "Julián: Que mi vecina teje con lana de oveja. Marta: ¿Y qué más? Julián: Que ella me autorizó a contarlo. Marta: Excelente, no olvides agradecerle.")

L(
    LF2, 4,
    materials=MAT,
    use="Aprenderé a construir una exposición oral breve sobre un aspecto de mi cultura, atribuyendo las ideas y cuidando la pronunciación. Sirve para presentar con orden lo que sé sin inventar ni hablar por otros.",
    prior=["Sé situar un diálogo, escuchar con límites y elegir vocabulario pertinente.", "Sé que la pronunciación de lengua indígena la enseña quien la habla."],
    explain=[
        "Una exposición breve tiene cuatro partes: saludo, presentación del tema, dos o tres ideas y cierre. En el saludo nombramos a quien escucha. En la presentación decimos de qué vamos a hablar. En las ideas contamos lo que sabemos y de dónde lo sabemos. En el cierre resumimos y agradecemos. Hablamos despacio para que se entienda.",
        "Una exposición atribuida dice quién enseñó cada cosa: «Mi vecina me contó que…» o «Según el educador tradicional…». Si usamos una palabra en lengua indígena, la decimos como la enseñó quien la habla y avisamos que la aprendimos de esa persona. No inventamos cómo se pronuncia ni qué significa. Tampoco hablamos por todo un pueblo.",
        "Para cuidar la pronunciación, antes de exponer practicamos: escuchamos a quien la habla, la repetimos varias veces, y si dudamos, preguntamos. Al hablar, mantenemos un volumen y una velocidad que permitan escuchar. Si cometemos un error, pedimos disculpas y repetimos la palabra. Lo importante es el respeto, no la perfección.",
    ],
    vocab=[("exposición breve", "presentación corta y ordenada de un tema"), ("cierre", "parte final que resume y agradece"), ("atribución", "decir quién enseñó o dijo algo"), ("pronunciación", "manera de decir los sonidos de una palabra"), ("volumen", "qué tan fuerte o suave se habla")],
    worked=[
        W("Ordenar las partes", "Partes: a) Gracias por escuchar b) Buenas tardes, compañeros c) Hoy hablaré del tejido d) Mi vecina teje con lana de oveja. ¿En qué orden va una exposición?", ["Saludo.", "Tema.", "Idea.", "Cierre."], "b, c, d, a"),
        W("Atribuir una idea", "Idea: «El tejido se hace con lana de oveja». ¿Cómo la atribuyes?", ["Pienso en quién me lo contó.", "Escribo su nombre o su rol."], "Mi vecina me contó que el tejido se hace con lana de oveja."),
    ],
    mistakes=[
        M("Saltarme el cierre.", "Termino sin resumir ni agradecer.", "Agrego una frase de cierre y de gracias."),
        M("Hablar rápido para terminar pronto.", "No se escucha.", "Hablo despacio."),
    ],
    R=[
        ex("La primera parte de una exposición es: A) el saludo B) el cierre", "A", "Se empieza saludando."),
        ex("La última parte es: A) el cierre y el agradecimiento B) el tema", "A", "El cierre resume y agradece."),
        ex(DIALOGO3 + " ¿Con qué teje la vecina de Julián?", "Con lana de oveja", "Julián lo dice en su turno."),
    ],
    C=[
        ex("Verdadero o falso: atribuir una idea es decir quién la contó.", "Verdadero", "Atribuir es nombrar la fuente."),
        ex("Si no sé cómo se dice una palabra indígena, ¿qué hago? A) pido al educador tradicional que la diga B) la digo como creo que suena", "A", "La pronunciación se aprende de quien habla."),
        ex("¿Por qué conviene hablar despacio al exponer? A) para que se escuche y se entienda B) para tardar más", "A", "La claridad ayuda a quien escucha."),
    ],
    A=[
        ex("Ordena las partes: a) Muchas gracias b) Buenas tardes c) Hoy hablaré de la huerta d) Mi vecina cultiva papas. Escribe las letras.", "b, c, d, a", "Saludo, tema, idea y cierre."),
        ex(DIALOGO3 + " ¿Qué le recuerda Marta a Julián al final?", "Agradecerle a su vecina", "Marta dice: no olvides agradecerle."),
        ex("Escribe la idea «las papas crecen bajo la tierra» con atribución a una vecina.", "Mi vecina me contó que las papas crecen bajo la tierra", "Se nombra la fuente."),
    ],
    Z=[
        ex("Pablo expone: «Todos los pueblos tejen igual». ¿Qué error comete?", "Habla por todos los pueblos", "Solo puede hablar de lo que conoce y atribuirlo."),
        ex("Una niña se equivoca al decir una palabra indígena y se queda callada. ¿Qué sería mejor? A) pedir disculpas, repetirla y seguir B) callarse y no volver a usarla", "A", "Corregirse con respeto es parte del aprendizaje."),
    ],
    D=[
        ex("Dos exposiciones: la 1 tiene saludo, tema, dos ideas atribuidas y cierre; la 2 solo tiene ideas sin fuente. ¿Cuál es mejor según lo aprendido?", "La 1", "Tiene todas las partes y atribuye."),
        ex("Si tu vecina te pidió que no cuentes una parte de su oficio, ¿qué haces en la exposición? A) no la menciono B) la menciono si es corta", "A", "Su límite se respeta."),
    ],
    context=[ex("Vas a exponer sobre un oficio de tu comunidad y tienes 3 minutos. ¿Qué haces? A) preparo saludo, tema, dos ideas atribuidas y cierre B) improviso sin ordenar", "A", "Una estructura clara cabe en el tiempo.")],
    selfcheck=[
        ex("Nombra las cuatro partes de una exposición breve.", "Saludo, tema, ideas y cierre", "Son las partes de la clase."),
        ex("Verdadero o falso: puedo inventar la pronunciación de una palabra indígena.", "Falso", "Debe enseñarla quien habla la lengua."),
        ex("¿Qué frase atribuye mejor? A) «Mi vecina me contó…» B) «Todos saben que…»", "A", "Nombra la fuente."),
    ],
    task=T("Prepara una exposición de cuatro partes sobre un oficio o actividad de tu comunidad (por ejemplo, tejer, cultivar o pescar). Escribe: saludo, tema, dos ideas con atribución («Mi vecina/vecino me contó que…») y cierre con agradecimiento. Escribe también una frase sobre lo que no cuentas porque no tienes permiso. Ensáyala en voz alta con un compañero o una persona de confianza y anota una cosa para mejorar. Si usas una palabra indígena, apréndela del educador tradicional y escribe quién te la enseñó.",
           "Saludo: Buenas tardes. Tema: hoy hablaré del tejido. Idea 1: mi vecina me contó que teje con lana de oveja. Idea 2: ella dijo que le toma varios días. No cuento: el diseño que ella prefiere guardar. Cierre: gracias por escuchar. Mejorar: hablar más despacio.",
           ["incluye las cuatro partes", "atribuye las ideas", "declara un límite"], ["texto de la exposición", "nota de ensayo"], ["hablar por todo un pueblo", "inventar palabras o pronunciación"],
           "Pedir que lea la exposición y señale cada parte; valorar que declare lo que no cuenta."),
    reinforce="Reordena en tu cuaderno las cuatro partes de una exposición con tus propias frases.",
    extend="Ensaya tu exposición dos veces, una con volumen bajo y otra con volumen adecuado, y anota cuál se escucha mejor.",
)
