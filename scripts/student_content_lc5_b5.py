"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR03 (lectura de textos de la realidad familiar, local y territorial, reconociendo palabras y expresiones
culturalmente significativas) y OA LR04 (escritura de mensajes con frases y oraciones breves).

Criterio de autoría: los textos, las personas, las comunidades y los mensajes de práctica son INVENTADOS, están en
castellano y se rotulan como tales; no pertenecen a ningún pueblo. Las únicas palabras en lengua indígena son las ya
atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke en mapuzugun; iorana, maururu en rapa nui), siempre
dentro de una ficha. No se inventa lengua, pronunciación ni sentido espiritual de ninguna expresión. Los mensajes de
LR04 son frases breves en castellano, con a lo más un saludo o agradecimiento de la ficha de palabras; las frases
completas en lengua indígena las enseña el educador/a tradicional. Cada tarea abierta remite al educador/a tradicional
o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LR3, LR4 = "LC05 OA LR03", "LC05 OA LR04"

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


MAT = "Lápiz y hojas. Los textos, las fichas y los mensajes están escritos en este cuaderno y son inventados para practicar; no son de ningún pueblo."

FICHA_PAL = ("Ficha de palabras (de práctica): en mapuzugun «ko» es agua, «mapu» es tierra, «antü» es sol, «kuyen» es luna, «ruka» es casa y «ñuke» es madre. "
             "«mari mari» es un saludo y «chaltumay» es «gracias» en mapuzugun. «iorana» es un saludo y «maururu» es «gracias» en rapa nui.")
CAMINO = ("Texto de práctica «El camino a la escuela» (inventado): «Cada mañana, Lucas y sus vecinos caminan juntos por el camino de la quebrada. "
          "En el camino saludan con un «mari mari» a las personas mayores. En invierno, cuando el río crece, los vecinos avisan en la sede si el camino está cerrado. "
          "Después de la lluvia, todos limpian el camino con palas y rastrillos.»")
TEJEDORA = ("Texto de práctica «Las manos de la tejedora» (inventado): «Doña Berta teje con lana de oveja en el patio de su casa. Primero lava la lana, después la hila y por último teje. "
            "Mientras trabaja, conversa con las niñas del barrio. Ella dice que tejer es cuidar el hilo entre todas.»")
COSECHA = ("Texto de práctica «Después de la cosecha» (inventado): «Cuando termina la cosecha de papas, la comunidad se junta en la sede. Cada familia trae un canasto y lo comparte. "
           "Don Aníbal da las gracias a los vecinos por su trabajo. Los niños ayudan a repartir.»")
FICHA_T2 = ("Ficha de texto (inventada). Tipo: descripción. Autor: Lucas, estudiante. Tema: el camino a la escuela de su comunidad. "
            "Permiso: Lucas autorizó usar el texto en la escuela. Límite: no se publica el nombre de la quebrada.")

# ============================================================ OA LR03 · lectura cultural con palabras significativas
L(
    LR3, 1,
    materials=MAT,
    use="Aprenderé a situar un texto sobre la familia, el lugar o el territorio y a reconocer qué palabras y expresiones pueden ser significativas para la comunidad. Sirve para leer textos de la cultura con respeto.",
    prior=["Sé situar un texto con una ficha.", "Sé qué es una expresión culturalmente significativa."],
    explain=[
        "Los textos sobre la realidad familiar, local y territorial cuentan cómo se vive en un lugar: cómo se llega a la escuela, qué oficios hay, qué se cultiva o cómo se ayudan los vecinos. Pueden estar escritos en castellano o en lengua indígena. En ambos casos, algunas palabras y frases tienen un sentido especial para la comunidad.",
        "Antes de leer, situamos el texto con una ficha: tipo de texto, autor o autora, tema, permiso y límite. Luego leemos buscando las palabras y expresiones que parecen significativas: nombres de lugares, saludos, oficios, formas de ayudarse y frases que se repiten. Las subrayamos, pero no explicamos su sentido sin una fuente.",
        "Una palabra puede ser significativa aunque sea muy simple, como «sede» o «camino», porque nombra un lugar importante para la comunidad. Y una palabra en lengua indígena, como «mari mari», es un saludo que está en nuestra ficha de palabras. Todo lo demás, el sentido profundo y su uso en cada situación, lo explica la comunidad.",
    ],
    vocab=[("texto de la realidad local", "texto que cuenta cómo se vive en un lugar"), ("palabra significativa", "palabra con valor especial para la comunidad"), ("expresión", "palabra o frase que dice algo con sentido"), ("subrayar", "marcar una palabra o frase"), ("saludo", "palabra con que se comienza una conversación")],
    worked=[
        W("Leer la ficha", FICHA_T2 + " ¿Quién escribió el texto y de qué trata?", ["Busco autor y tema.", "Lucas; el camino a la escuela."], "Lo escribió Lucas y trata del camino a la escuela de su comunidad."),
        W("Subrayar palabras significativas", CAMINO + " Subraya dos palabras o expresiones que parezcan significativas.", ["Busco lugares y saludos.", "Aparecen «sede» y «mari mari»."], "«Sede» y «mari mari»."),
    ],
    mistakes=[
        M("Explicar el sentido profundo de una palabra sin fuente.", "Invento un significado.", "La subrayo y pregunto."),
        M("Leer sin mirar la ficha.", "No sé quién escribió ni qué se puede usar.", "Leo primero la ficha."),
    ],
    R=[
        ex(FICHA_T2 + " ¿Quién es el autor del texto?", "Lucas", "La ficha lo indica."),
        ex(CAMINO + " ¿Con qué saludo saludan a las personas mayores?", "Mari mari", "Aparece entre comillas en el texto."),
        ex(CAMINO + " ¿Dónde avisan si el camino está cerrado?", "En la sede", "El texto lo dice."),
    ],
    C=[
        ex("Verdadero o falso: una palabra muy simple puede ser significativa para una comunidad.", "Verdadero", "Por ejemplo, «sede»."),
        ex(FICHA_PAL + " ¿Qué es «mari mari» según la ficha de palabras?", "Un saludo", "Lo dice la ficha."),
        ex("Verdadero o falso: puedo explicar el sentido profundo de una palabra sin preguntar.", "Falso", "Lo explica la comunidad."),
    ],
    A=[
        ex(FICHA_T2 + " ¿Se puede publicar el nombre de la quebrada? Responde Sí o No.", "No", "El límite lo prohíbe."),
        ex("Une cada palabra del texto con su tipo. 1) sede 2) mari mari 3) palas y rastrillos. a) herramientas b) saludo c) lugar", "1-c, 2-b, 3-a", "Cada palabra pertenece a un tipo distinto."),
        ex(CAMINO + " ¿Qué frase del texto muestra cooperación? A) «Todos limpian el camino con palas y rastrillos» B) «El río crece en invierno»", "A", "Todos trabajan juntos; la B solo cuenta lo que pasa con el río."),
    ],
    Z=[
        ex("Tomás dice: «Como el texto usa “mari mari”, el texto es de un pueblo real». ¿Qué error comete?", "El texto es inventado", "Solo usa una palabra de la ficha."),
        ex("Una niña dice que «sede» es una palabra sagrada. El texto no lo dice. ¿Qué falla?", "Inventa un sentido", "El texto solo nombra la sede como lugar."),
    ],
    D=[
        ex("Dos fichas: F1 con autor y permiso; F2 sin autor. ¿Con cuál puedes trabajar?", "Con la F1", "La F2 no tiene autoría."),
        ex("Si no entiendes una palabra del texto, ¿qué haces? A) la subrayo y pregunto B) invento su sentido", "A", "No se inventa."),
    ],
    context=[ex("Un vecino te muestra un texto escrito por una persona de su comunidad que tiene palabras que no conoces. ¿Qué haces primero? A) pedir la ficha y preguntar qué significan B) explicarlas yo", "A", "Primero ficha y fuente.")],
    selfcheck=[
        ex("Nombra tres datos de la ficha de un texto.", "Tres entre: tipo, autor, tema, permiso, límite", "Son datos de la ficha."),
        ex("Verdadero o falso: puedo subrayar palabras significativas sin explicarlas.", "Verdadero", "Subrayar es un primer paso."),
        ex(CAMINO + " ¿Qué usan los vecinos para limpiar el camino?", "Palas y rastrillos", "El texto lo dice."),
    ],
    task=T("Lee la ficha y el texto: «" + FICHA_T2 + "» «" + CAMINO.split("«", 2)[2].rstrip("»") + "» Haz una tabla de tres columnas: «Datos de la ficha» (tipo, autor, permiso, límite), «Palabras o expresiones que subrayé» (al menos cuatro) y «Lo que no sé de ellas». Escribe una pregunta para el educador tradicional sobre algún saludo de la lengua de tu comunidad.",
           "Datos: descripción; Lucas; permiso sí; límite el nombre de la quebrada. Subrayé: sede, mari mari, camino, palas y rastrillos. No sé: por qué avisan en la sede. Pregunta: ¿cómo se saluda a una persona mayor en nuestra lengua?",
           ["completa la ficha", "subraya palabras del texto", "declara lo que no sabe"], ["tabla de tres columnas", "pregunta escrita"], ["explicar sentidos sin fuente", "escribir el nombre reservado"],
           "Pedir que ubique cada palabra en el texto; valorar que no explique sentidos."),
    reinforce="Copia el texto y subraya con un color los lugares y con otro los saludos.",
    extend="Escribe cuatro palabras de tu comunidad que podrían ser significativas y a quién consultarías.",
)

L(
    LR3, 2,
    materials=MAT,
    use="Aprenderé a leer un texto de la vida local comprendiéndolo y declarando sus límites, y a reconocer las palabras significativas sin explicar lo que el texto no dice. Sirve para leer con respeto y precisión.",
    prior=["Sé situar un texto y subrayar palabras significativas.", "Sé distinguir lo que dice un texto de lo que imagino."],
    explain=[
        "Comprender es saber quién hace qué, dónde y cuándo. En «El camino a la escuela» buscamos los hechos: quiénes caminan, por dónde, qué hacen en invierno y qué hacen después de la lluvia. Los marcamos y luego los resumimos con nuestras palabras. Si una palabra no la entendemos, la anotamos para preguntarla.",
        "Leer con límites es decir qué dice el texto, qué no dice y qué está reservado. El texto dice que los vecinos avisan en la sede si el camino está cerrado, pero no dice a quién le avisan ni cuántos son. Eso no lo completamos. Y el nombre de la quebrada, que la ficha reserva, no lo escribimos.",
        "Las palabras significativas se reconocen por lo que el texto muestra de ellas. El «mari mari» es un saludo que usan los vecinos con las personas mayores; el texto no explica por qué ni en qué situaciones. Nosotros decimos lo que el texto dice y dejamos lo demás como pregunta para la comunidad.",
    ],
    vocab=[("comprender", "entender lo que dice un texto"), ("hecho", "algo que ocurre en el texto"), ("límite del texto", "lo que el texto no dice"), ("resumir", "decir con pocas palabras lo más importante"), ("reservado", "guardado y no compartido con todos")],
    worked=[
        W("Marcar hechos", CAMINO + " ¿Qué hacen los vecinos después de la lluvia?", ["Busco «después de la lluvia».", "Dice que limpian el camino."], "Limpian el camino con palas y rastrillos."),
        W("Lo que el texto no dice", CAMINO + " ¿Dice cuántos vecinos caminan con Lucas?", ["Reviso el texto.", "Solo dice «sus vecinos»."], "No, el texto no lo dice."),
    ],
    mistakes=[
        M("Responder con lo que imagino y no con lo que dice el texto.", "Atribuyo al texto algo que no contó.", "Vuelvo al texto y busco la frase."),
        M("Explicar por qué se usa un saludo sin que el texto lo diga.", "Invento un sentido.", "Escribo que el texto no lo explica."),
    ],
    R=[
        ex(CAMINO + " ¿Con quién camina Lucas cada mañana?", "Con sus vecinos", "El texto lo dice."),
        ex(CAMINO + " ¿Por dónde caminan: por el camino de la quebrada o por la playa?", "Por el camino de la quebrada", "El texto lo dice."),
        ex(CAMINO + " ¿En qué estación del año crece el río?", "En invierno", "El texto lo menciona."),
    ],
    C=[
        ex(CAMINO + " Verdadero o falso: el texto dice cuántos vecinos caminan con Lucas.", "Falso", "Solo dice «sus vecinos»."),
        ex("Si el texto no explica por qué se usa un saludo, ¿qué escribo? A) “el texto no lo explica” B) una razón probable", "A", "Se declara el límite."),
        ex(CAMINO + " ¿Qué avisan los vecinos en la sede: si el camino está cerrado o si hay fiesta?", "Si el camino está cerrado", "Es lo que dice el texto."),
    ],
    A=[
        ex(CAMINO + " Ordena: a) limpian el camino b) el río crece c) avisan en la sede. Escribe las letras.", "b, c, a", "Primero el río crece, luego avisan y después de la lluvia limpian."),
        ex(CAMINO + " ¿Cuál afirmación está en el texto? A) saludan con un mari mari a las personas mayores B) usan lanchas para cruzar", "A", "La B no aparece."),
        ex(CAMINO + " ¿Qué resumen es fiel al texto? A) Lucas y sus vecinos caminan juntos, avisan en la sede si el camino está cerrado y lo limpian después de la lluvia B) Lucas camina solo y nadie limpia el camino", "A", "La B cambia lo que dice el texto."),
    ],
    Z=[
        ex("Pedro dice: «En el texto se ve que los vecinos hacen una ceremonia con el saludo». ¿Está en el texto? Responde Sí o No.", "No", "El texto solo dice que saludan."),
        ex("La ficha reserva el nombre de la quebrada. Alguien pregunta cómo se llama. ¿Qué respuesta respeta el límite? A) «Ese dato no se publica» B) «Seguro es Quebrada Seca»", "A", "La B inventa un nombre."),
    ],
    D=[
        ex("Dos resúmenes. R1: «Los vecinos limpian el camino después de la lluvia». R2: «Los vecinos limpian el camino todos los domingos». ¿Cuál es fiel al texto?", "R1", "La R2 agrega una frecuencia."),
        ex("¿Qué dos herramientas nombra el texto?", "Palas y rastrillos", "El texto las menciona."),
    ],
    context=[ex("Alguien te pregunta por qué los vecinos de un texto usan un saludo especial con las personas mayores, y el texto no lo dice. ¿Qué respondes? A) “el texto no lo dice; se puede preguntar a la comunidad” B) una razón que te parece posible", "A", "Se respeta el límite.")],
    selfcheck=[
        ex("Nombra las tres cosas que se declaran al leer con límites.", "Lo que el texto dice, lo que no dice y lo reservado", "Son los límites de la lectura."),
        ex(CAMINO + " ¿Qué saludo usan los vecinos?", "Mari mari", "Aparece en el texto."),
        ex("Verdadero o falso: puedo completar con mi imaginación lo que el texto no dice.", "Falso", "Se declara que no lo dice."),
    ],
    task=T("Lee el texto: «" + CAMINO.split("«", 2)[2].rstrip("»") + "» Haz una tabla de tres columnas: «El texto dice» (cuatro datos), «El texto no dice» (dos datos) y «Palabras significativas» (dos, con la frase del texto donde aparecen). Escribe un resumen de dos frases con tus palabras.",
           "Dice: Lucas camina con sus vecinos; saludan con mari mari; avisan en la sede si el camino está cerrado; limpian el camino con palas y rastrillos. No dice: cuántos vecinos son; a quién le avisan. Palabras: sede (avisan en la sede), mari mari (saludan con un mari mari). Resumen: Lucas y sus vecinos caminan juntos a la escuela. Se avisan en la sede si el camino está cerrado y lo limpian después de la lluvia.",
           ["registra datos del texto", "reconoce lo que no dice", "resume con palabras propias"], ["tabla de tres columnas", "resumen de dos frases"], ["agregar datos", "explicar sentidos sin fuente"],
           "Pedir que ubique cada dato; valorar que reconozca lo que no se dice."),
    reinforce="Subraya en el texto los verbos que dicen qué hacen los vecinos.",
    extend="Escribe tres preguntas que el texto no responde y cómo las harías.",
)

L(
    LR3, 3,
    materials=MAT,
    use="Aprenderé a analizar las palabras y expresiones significativas de un texto de la vida local: qué muestran del oficio, del lugar y de la forma de ayudarse. Sirve para valorar la cultura sin inventar significados.",
    prior=["Sé leer un texto con límites.", "Sé que el sentido profundo lo explica la comunidad."],
    explain=[
        "Analizar es explicar qué muestra cada palabra o expresión significativa, sin pasar de lo que dice el texto. En «Las manos de la tejedora», «teje con lana de oveja» muestra un oficio, «en el patio de su casa» muestra un lugar y «cuidar el hilo entre todas» muestra una forma de trabajar juntas.",
        "Podemos ordenar las palabras en una tabla de cuatro columnas: lugares, oficios, materiales y formas de ayudarse. Así vemos de un vistazo qué muestra el texto de la vida de doña Berta. Para cada una, escribimos una frase con «el texto muestra que…». Si falta información, escribimos «el texto no dice».",
        "Valorar es reconocer la importancia de algo con respeto. Podemos valorar que doña Berta enseñe a las niñas, pero no decimos que sea una tradición de un pueblo ni que tenga un valor sagrado, porque el texto no lo dice. Si queremos saber más, preguntamos a la comunidad o al educador tradicional.",
    ],
    vocab=[("analizar", "explicar qué muestra cada parte de un texto"), ("oficio", "trabajo que una persona sabe hacer"), ("material", "cosa con que se hace algo, como la lana"), ("valorar", "reconocer la importancia de algo con respeto"), ("forma de ayudarse", "manera en que las personas cooperan")],
    worked=[
        W("Clasificar", TEJEDORA + " Clasifica: el patio, la lana, tejer, cuidar el hilo entre todas.", ["El patio es un lugar.", "La lana es un material.", "Tejer es un oficio.", "Cuidar el hilo entre todas es una forma de ayudarse."], "Patio: lugar. Lana: material. Tejer: oficio. Cuidar el hilo entre todas: forma de ayudarse."),
        W("Analizar sin inventar", TEJEDORA + " ¿Qué muestra que doña Berta converse con las niñas mientras trabaja?", ["El texto dice que conversa con las niñas del barrio.", "Eso muestra que comparte su trabajo."], "Que comparte su trabajo con las niñas; el texto no dice por qué."),
    ],
    mistakes=[
        M("Decir que una práctica es una tradición de un pueblo sin que el texto lo diga.", "Invento un origen.", "Digo solo lo que el texto muestra."),
        M("Clasificar sin volver al texto.", "Puedo equivocarme de categoría.", "Busco la frase que lo justifica."),
    ],
    R=[
        ex(TEJEDORA + " ¿Con qué teje doña Berta?", "Con lana de oveja", "El texto lo dice."),
        ex(TEJEDORA + " ¿Dónde teje: en el patio de su casa o en la sede?", "En el patio de su casa", "El texto lo dice."),
        ex(TEJEDORA + " ¿Qué hace primero doña Berta: lava la lana o teje?", "Lava la lana", "El texto da ese orden."),
    ],
    C=[
        ex("Un material es: A) una cosa con que se hace algo B) un lugar", "A", "Por ejemplo, la lana."),
        ex("Verdadero o falso: puedo decir que tejer es una tradición de un pueblo si el texto no lo dice.", "Falso", "Eso lo diría la comunidad."),
        ex(TEJEDORA + " ¿Qué dice doña Berta que es tejer: cuidar el hilo entre todas o ganar dinero?", "Cuidar el hilo entre todas", "El texto lo dice."),
    ],
    A=[
        ex("Une cada palabra con su categoría. 1) el patio 2) la lana 3) tejer. a) material b) oficio c) lugar", "1-c, 2-a, 3-b", "Cada palabra corresponde a una categoría."),
        ex(TEJEDORA + " Ordena los pasos: a) teje b) lava la lana c) hila. Escribe las letras.", "b, c, a", "El texto dice: primero lava, después hila y por último teje."),
        ex(TEJEDORA + " ¿Cuál frase con «El texto muestra que…» se apoya en el texto? A) «El texto muestra que doña Berta conversa con las niñas del barrio mientras trabaja» B) «El texto muestra que doña Berta es famosa en todo el país»", "A", "La B agrega un dato que el texto no dice."),
    ],
    Z=[
        ex("Ana dice: «Doña Berta teje así porque lo aprendió de sus antepasados». ¿Está en el texto? Responde Sí o No.", "No", "El texto no dice cómo aprendió."),
        ex("Luis dice: «Todas las tejedoras trabajan entre todas». ¿Qué error comete?", "Generaliza a todas las tejedoras", "El texto habla de doña Berta."),
    ],
    D=[
        ex("Elige la frase que analiza sin inventar: A) «El texto muestra que doña Berta comparte su oficio con las niñas» B) «El texto muestra que el tejido es un rito»", "A", "La B inventa."),
        ex(TEJEDORA + " ¿Qué tres pasos del trabajo menciona el texto?", "Lavar, hilar y tejer", "Son los que cuenta."),
    ],
    context=[ex("Una niña dice en clases que «cuidar el hilo entre todas» es una creencia antigua. No tiene fuente. ¿Qué le propones? A) preguntar a una persona que teje B) aceptarlo", "A", "Una fuente puede explicar el sentido.")],
    selfcheck=[
        ex("Nombra las cuatro columnas de la tabla de análisis.", "Lugares, oficios, materiales y formas de ayudarse", "Son las categorías de la clase."),
        ex("Verdadero o falso: valorar es reconocer la importancia de algo con respeto.", "Verdadero", "Es su definición."),
        ex("¿Qué escribo si falta información? A) “el texto no dice” B) lo que supongo", "A", "Se declara el límite."),
    ],
    task=T("Lee «Después de la cosecha»: «" + COSECHA.split("«", 2)[2].rstrip("»") + "» Haz una tabla de cuatro columnas: lugares, oficios o actividades, alimentos y formas de ayudarse, con al menos un dato en cada una. Escribe una frase con «El texto muestra que…» y una con «Me gustaría preguntar a la comunidad…». No expliques significados que el texto no da.",
           "Lugares: la sede. Actividades: cosechar, repartir. Alimentos: papas. Formas de ayudarse: cada familia comparte un canasto; los niños ayudan a repartir. El texto muestra que la comunidad se junta y comparte después de la cosecha. Me gustaría preguntar a la comunidad cómo se organizan para repartir los canastos.",
           ["completa cuatro columnas con datos del texto", "analiza sin inventar", "formula una pregunta respetuosa"], ["tabla de cuatro columnas", "dos frases"], ["inventar significados", "generalizar"],
           "Pedir que indique la frase del texto de cada dato; valorar que no agregue ritos."),
    reinforce="Haz la misma tabla con «Las manos de la tejedora».",
    extend="Escribe qué expresión de «Después de la cosecha» te parece significativa y qué preguntarías sobre ella.",
)

L(
    LR3, 4,
    materials=MAT,
    use="Aprenderé a construir una respuesta atribuida sobre un texto de la vida local, usando una palabra o expresión significativa y una frase del texto como evidencia. Sirve para responder con claridad y respeto.",
    prior=["Sé analizar palabras y expresiones significativas.", "Sé usar «según» para atribuir."],
    explain=[
        "Una respuesta atribuida tiene cinco partes. Primero, la fuente: «Según el texto “Después de la cosecha”…». Segundo, la palabra o expresión que elegimos. Tercero, lo que el texto muestra de ella. Cuarto, una frase del texto como evidencia. Quinto, un límite: «el texto no explica…». Con estas partes, quien lee sabe de dónde sale cada afirmación.",
        "Elegir bien la evidencia es clave. La evidencia es una frase del texto que podemos señalar con el dedo. Si afirmamos que la comunidad comparte, la evidencia es «Cada familia trae un canasto y lo comparte». Si no hay una frase que lo apoye, no hacemos la afirmación. La evidencia no es una opinión ni algo que recordamos de otro lugar.",
        "Una respuesta bien atribuida no usa «todos», «siempre» ni «los pueblos». Habla del texto y de la comunidad de práctica. Cuando damos nuestra opinión, la separamos con «Yo pienso…». Y cuando se trata de una palabra de lengua indígena, usamos solo lo que dice la ficha de palabras o lo que enseña el educador tradicional.",
    ],
    vocab=[("respuesta atribuida", "respuesta que dice de dónde viene cada dato"), ("evidencia", "frase del texto que apoya lo que afirmo"), ("expresión elegida", "palabra o frase significativa sobre la que escribo"), ("límite", "aclaración de lo que el texto no dice"), ("opinión", "lo que yo pienso, separado de lo que dice el texto")],
    worked=[
        W("Armar la respuesta", COSECHA + " Pregunta: ¿qué muestra la expresión «da las gracias a los vecinos»?", ["Fuente: el texto «Después de la cosecha».", "Muestra que don Aníbal agradece el trabajo de los vecinos.", "Evidencia: «Don Aníbal da las gracias a los vecinos por su trabajo»."], "Según el texto, don Aníbal da las gracias a los vecinos: «Don Aníbal da las gracias a los vecinos por su trabajo». El texto no explica por qué."),
        W("Corregir una respuesta", "Respuesta: «Todos los pueblos agradecen a la tierra después de la cosecha». ¿Qué error tiene?", ["Dice «todos los pueblos».", "El texto habla de una comunidad."], "Generaliza; debe hablar de la comunidad del texto."),
    ],
    mistakes=[
        M("Afirmar algo sin evidencia.", "No se puede comprobar.", "Busco una frase del texto."),
        M("Usar «todos» o «siempre».", "El texto cuenta un caso.", "Nombro la comunidad o el texto."),
    ],
    R=[
        ex("Completa: «Según el texto “Después de la ___”, la comunidad se junta en la sede».", "cosecha", "Es el título."),
        ex(COSECHA + " ¿Qué trae cada familia?", "Un canasto", "El texto lo dice."),
        ex("La evidencia es: A) una frase del texto que apoya lo que afirmo B) mi opinión", "A", "Se encuentra en el texto."),
    ],
    C=[
        ex("Verdadero o falso: puedo usar «los pueblos» para hablar de lo que cuenta un texto.", "Falso", "El texto habla de una comunidad."),
        ex("Las cinco partes son fuente, expresión, lo que muestra, evidencia y… A) límite B) chiste", "A", "El límite declara lo que no sabemos."),
        ex("¿Cómo separo mi opinión? A) con “Yo pienso…” B) sin avisar", "A", "Marca la voz propia."),
    ],
    A=[
        ex("Ordena: a) “Cada familia trae un canasto y lo comparte” b) Según el texto c) la comunidad comparte lo cosechado. Escribe las letras.", "b, c, a", "Fuente, idea y evidencia."),
        ex(COSECHA + " Elige la evidencia que apoya que los niños ayudan: A) “Los niños ayudan a repartir” B) “La comunidad se junta en la sede”", "A", "La A muestra la ayuda."),
        ex(TEJEDORA + " Completa: «Según el texto, doña Berta dice que tejer es cuidar el ___ entre todas».", "hilo", "El texto lo dice."),
    ],
    Z=[
        ex("Rosa escribe: «Según el texto, don Aníbal es el líder de la comunidad». ¿Qué error comete?", "Agrega un dato que el texto no dice", "El texto solo dice que agradece."),
        ex("Luis escribe: «El texto no explica por qué don Aníbal da las gracias a los vecinos». ¿Es una respuesta válida? Responde Sí o No.", "Sí", "Declara un límite del texto."),
    ],
    D=[
        ex("Dos respuestas. R1: «Según el texto, la comunidad comparte: “Cada familia trae un canasto y lo comparte”». R2: «Las comunidades siempre comparten». ¿Cuál tiene evidencia?", "R1", "La R2 generaliza sin evidencia."),
        ex("Si la ficha reserva un dato del texto, ¿lo usas como evidencia? A) no B) sí", "A", "El límite se respeta."),
    ],
    context=[ex("En una prueba te piden explicar qué muestra una expresión de un texto. ¿Qué haces? A) escribo fuente, expresión, lo que muestra, evidencia y límite B) escribo lo que sé de otros textos", "A", "Se responde con el texto.")],
    selfcheck=[
        ex("Nombra las cinco partes de la respuesta atribuida.", "Fuente, expresión, lo que muestra, evidencia y límite", "Son las partes de la clase."),
        ex("Verdadero o falso: una evidencia puede ser una opinión mía.", "Falso", "Sale del texto."),
        ex("Verdadero o falso: puedo decir «el texto no explica…».", "Verdadero", "Declara el límite."),
    ],
    task=T("Responde por escrito: «¿Qué muestra la expresión “cuidar el hilo entre todas” en el texto “Las manos de la tejedora”?». Usa el texto: «" + TEJEDORA.split("«", 2)[2].rstrip("»") + "». Tu respuesta debe tener la fuente, la expresión, lo que muestra, una frase del texto como evidencia y un límite («El texto no explica…»). Añade una frase con «Yo pienso…».",
           "Según el texto «Las manos de la tejedora», la expresión «cuidar el hilo entre todas» muestra que doña Berta ve el tejido como un trabajo compartido. La evidencia es que «conversa con las niñas del barrio». El texto no explica qué significa exactamente «el hilo» para ella. Yo pienso que habla de cuidar el trabajo juntas.",
           ["incluye las cinco partes", "usa evidencia del texto", "separa la opinión"], ["respuesta de cinco frases"], ["afirmar sin evidencia", "generalizar"],
           "Pedir que muestre la evidencia en el texto; valorar el límite."),
    reinforce="Escribe una evidencia de «El camino a la escuela» que apoye: los vecinos cooperan.",
    extend="Escribe una respuesta atribuida sobre «El camino a la escuela» con las cinco partes.",
)

L(
    LR3, 5,
    materials=MAT,
    use="Aprenderé a comparar dos textos de la vida local y sus palabras significativas sin decir que uno es mejor. Sirve para ver cómo cada texto muestra una manera de vivir un lugar.",
    prior=["Sé responder de forma atribuida con evidencia.", "Sé que contrastar es distinto de jerarquizar."],
    explain=[
        "Contrastar dos textos es mirar en qué se parecen y en qué se diferencian. «Las manos de la tejedora» y «Después de la cosecha» hablan de oficios y lugares distintos, pero en ambos aparecen personas que comparten: doña Berta con las niñas y la comunidad con sus canastos. Para comparar, usamos criterios neutros y una tabla.",
        "Los criterios pueden ser: el lugar, la actividad, los materiales o alimentos, las palabras o expresiones significativas y la forma de compartir. Escribimos lo que dice cada texto y, si un criterio no aparece, anotamos «no se menciona». No decimos que uno de los textos sea más importante, más cultural o mejor. Ambos muestran un aspecto de la vida de una comunidad.",
        "También evitamos concluir que los textos muestran cómo viven todas las comunidades. Son textos de práctica y cada uno habla de una comunidad. Si queremos comparar con la realidad de nuestra comunidad, preguntamos a las personas que la conocen y atribuimos lo que nos cuenten.",
    ],
    vocab=[("contrastar", "decir en qué se parecen y en qué se diferencian dos cosas"), ("criterio", "regla para comparar"), ("no se menciona", "el texto no dice nada sobre eso"), ("semejanza", "algo en lo que dos cosas se parecen"), ("diferencia", "algo en lo que dos cosas no se parecen")],
    worked=[
        W("Comparar con un criterio", TEJEDORA + " " + COSECHA + " Criterio: el lugar.", ["En el primero, el patio de la casa de doña Berta.", "En el segundo, la sede."], "Un texto ocurre en un patio y el otro en la sede."),
        W("Una semejanza", "Criterio: forma de compartir. Doña Berta conversa con las niñas; la comunidad comparte canastos.", ["Doña Berta conversa con las niñas.", "La comunidad comparte canastos."], "Ambos textos muestran personas que comparten con otras."),
    ],
    mistakes=[
        M("Decir que un texto es más cultural que otro.", "Jerarquiza.", "Comparo con criterios neutros."),
        M("Llenar la tabla con datos que no están.", "Inventa información.", "Escribo «no se menciona»."),
    ],
    R=[
        ex(TEJEDORA + " ¿Qué oficio muestra «Las manos de la tejedora»?", "Tejer", "Es el oficio de doña Berta."),
        ex(COSECHA + " ¿Qué alimento se cosecha en «Después de la cosecha»?", "Papas", "El texto lo dice."),
        ex("Contrastar es: A) ver semejanzas y diferencias B) elegir el mejor", "A", "Contrastar no pone un texto sobre otro."),
    ],
    C=[
        ex("Verdadero o falso: «es más cultural» es una forma de jerarquizar.", "Verdadero", "Pone un texto sobre otro."),
        ex("Si un criterio no aparece en un texto, ¿qué escribo? A) no se menciona B) lo que supongo", "A", "No se inventa."),
        ex("Verdadero o falso: dos textos pueden ser distintos y tener una semejanza.", "Verdadero", "Por ejemplo, ambos muestran que se comparte."),
    ],
    A=[
        ex("Criterio «lugar». Tejedora: el patio de la casa. Cosecha: la sede. ¿Cuál es la diferencia? A) uno ocurre en un patio y el otro en la sede B) los dos ocurren en la sede", "A", "Se comparan los lugares."),
        ex("Une cada texto con su dato. 1) Las manos de la tejedora 2) Después de la cosecha. a) cada familia trae un canasto b) lava, hila y teje", "1-b, 2-a", "Cada texto tiene su dato."),
        ex("Criterio «niñas o niños que participan». ¿Cuál es una semejanza entre los dos textos? A) en ambos participan niñas o niños B) en ambos se cosechan papas", "A", "Doña Berta conversa con niñas y los niños ayudan a repartir; solo un texto habla de cosecha."),
    ],
    Z=[
        ex("Marta dice: «El texto de la cosecha es mejor porque participa toda la comunidad». ¿Qué error comete?", "Jerarquiza con un criterio ajeno", "Cada texto muestra una forma de compartir."),
        ex("Pedro dice: «Estos dos textos muestran cómo viven todas las comunidades». ¿Qué falla? A) generaliza dos textos de práctica B) nada", "A", "Son dos textos inventados."),
    ],
    D=[
        ex("Elige la comparación respetuosa: A) «En el primer texto el oficio es tejer; en el segundo, cosechar y compartir» B) «Tejer es menos importante que cosechar»", "A", "La A describe."),
        ex("¿Qué criterio no aparece en «Las manos de la tejedora»: los materiales o los alimentos cosechados?", "Los alimentos cosechados", "El texto menciona lana, no cosecha."),
    ],
    context=[ex("Dos estudiantes presentan textos de comunidades distintas y discuten cuál muestra mejor la cultura. ¿Qué propones? A) comparar qué muestra cada uno B) votar", "A", "Se contrasta sin jerarquizar.")],
    selfcheck=[
        ex("Nombra dos criterios neutros para comparar textos.", "Dos entre: lugar, actividad, materiales o alimentos, expresiones, forma de compartir", "Son criterios de la clase."),
        ex("Verdadero o falso: puedo llenar con mi imaginación un criterio que el texto no menciona.", "Falso", "Se anota «no se menciona»."),
        ex("Verdadero o falso: la comparación termina con una semejanza y una diferencia con evidencia.", "Verdadero", "Es la estructura."),
    ],
    task=T("Compara «Las manos de la tejedora» y «Después de la cosecha». Textos: «" + TEJEDORA.split("«", 2)[2].rstrip("»") + "» y «" + COSECHA.split("«", 2)[2].rstrip("»") + "». Haz una tabla de dos columnas con las filas: lugar, actividad, materiales o alimentos, expresión significativa y forma de compartir. Escribe «no se menciona» donde corresponda. Cierra con una semejanza, una diferencia y una frase que explique por qué no se dice cuál es mejor.",
           "Lugar: patio de la casa / sede. Actividad: tejer / cosechar y repartir. Materiales o alimentos: lana / papas. Expresión: cuidar el hilo entre todas / dar las gracias a los vecinos. Compartir: conversa con las niñas / cada familia trae un canasto. Semejanza: ambos muestran que se comparte. Diferencia: uno es sobre un oficio y el otro sobre una cosecha. No se dice cuál es mejor porque cada texto muestra algo distinto.",
           ["usa criterios neutros", "marca lo que no se menciona", "no jerarquiza"], ["tabla de cinco filas", "semejanza y diferencia", "frase de cierre"], ["decir cuál es mejor", "llenar con datos inventados"],
           "Pedir que ubique cada dato en el texto; valorar «no se menciona»."),
    reinforce="Completa una tabla de tres filas con «El camino a la escuela» y «Después de la cosecha».",
    extend="Explica por qué dos textos de práctica no sirven para hablar de «todas las comunidades».",
)

# ============================================================ OA LR04 · mensajes situados con frases breves
L(
    LR4, 1,
    materials=MAT + " " + FICHA_PAL,
    use="Aprenderé a situar un mensaje breve: quién lo envía, a quién, para qué y en qué situación del medio natural, social o cultural. Sirve para escribir mensajes claros y respetuosos con frases cortas.",
    prior=["Sé que una frase breve dice una idea con pocas palabras.", "Sé que «mari mari» y «chaltumay» están en la ficha de palabras."],
    explain=[
        "Un mensaje es un texto corto que una persona escribe para otra con un propósito: avisar, invitar, agradecer o pedir. Se escribe con frases y oraciones breves, es decir, con pocas palabras y una idea por frase. Un buen mensaje se entiende rápido y no deja dudas.",
        "Antes de escribir, situamos el mensaje: quién lo envía, a quién va, para qué sirve y en qué situación se usa. Las situaciones pueden ser del medio natural, como cuidar el río; del medio social, como una reunión de vecinos; o del medio cultural, como agradecer a una persona que enseñó algo. El destinatario y la situación definen cómo escribimos.",
        "Un mensaje puede incluir una palabra en lengua indígena, como el saludo «mari mari» o el agradecimiento «chaltumay», que están en nuestra ficha de palabras. Solo las usamos si corresponden a la situación y a la comunidad. Las frases completas en lengua indígena las escribe quien la habla; nosotros pedimos ayuda al educador tradicional.",
    ],
    vocab=[("mensaje", "texto corto que una persona escribe para otra con un propósito"), ("frase breve", "frase con pocas palabras y una sola idea"), ("remitente", "persona que envía el mensaje"), ("destinatario", "persona a quien va el mensaje"), ("situación", "momento y lugar en que se usa el mensaje")],
    worked=[
        W("Situar un mensaje", "Mensaje: «Se invita a la reunión de la sede el sábado a las 10». Remitente: la directiva de la comunidad. ¿A quién va y para qué?", ["Es una invitación.", "Va a los vecinos y es para una reunión."], "A los vecinos, para invitarlos a una reunión."),
        W("Reconocer la frase breve", "Frase: «Cuidemos la vertiente entre todos». ¿Cuántas palabras tiene?", ["Separo las palabras una por una.", "Cuento: Cuidemos, la, vertiente, entre, todos."], "Cinco palabras."),
    ],
    mistakes=[
        M("Escribir un mensaje largo con varias ideas.", "Se pierde el mensaje.", "Una idea por frase."),
        M("Incluir una palabra indígena sin saber si corresponde.", "Puedo equivocarme de situación.", "Consulto al educador."),
    ],
    R=[
        ex("Un mensaje sirve para: A) avisar, invitar, agradecer o pedir B) solo contar cuentos", "A", "Son propósitos de un mensaje."),
        ex("¿Cuántas palabras tiene la frase «No botes basura al río»?", "Cinco", "Son no, botes, basura, al y río."),
        ex(FICHA_PAL + " ¿Qué es «chaltumay» en mapuzugun?", "Gracias", "La ficha lo dice."),
    ],
    C=[
        ex("Verdadero o falso: una frase breve tiene una sola idea.", "Verdadero", "Es lo que la hace clara."),
        ex("El destinatario es: A) la persona que recibe el mensaje B) la persona que lo escribe", "A", "Destinatario es a quien va el mensaje."),
        ex("Verdadero o falso: puedo escribir frases completas en lengua indígena sin ayuda.", "Falso", "Las enseña quien la habla."),
    ],
    A=[
        ex("Mensaje: «Gracias por enseñarnos a sembrar». ¿Qué propósito tiene: agradecer o invitar?", "Agradecer", "El mensaje empieza dando las gracias."),
        ex("Une cada mensaje con su situación. 1) «No botes basura al río» 2) «Reunión en la sede el sábado» 3) «Gracias por enseñarnos». a) cultural b) natural c) social", "1-b, 2-c, 3-a", "Cuidar el río es natural, la reunión es social y agradecer a quien enseña es cultural."),
        ex("¿Cuántas palabras tiene la frase «Cuidemos la vertiente entre todos»?", "Cinco", "Son cuidemos, la, vertiente, entre y todos."),
    ],
    Z=[
        ex("Un compañero escribe un mensaje con seis ideas en una sola frase muy larga. ¿Qué falla?", "No es una frase breve", "Debe haber una idea por frase."),
        ex("Una niña pone «mari mari» en un aviso de peligro sin que corresponda. ¿Qué debe hacer? A) consultar si corresponde B) dejarlo", "A", "Solo se usa lo que corresponde."),
    ],
    D=[
        ex("Dos mensajes. M1: «Reunión el sábado a las 10 en la sede». M2: «Hay una reunión de la comunidad, que se hace por muchas razones importantes y que sirve para varias cosas». ¿Cuál es más claro?", "M1", "Tiene una idea y datos concretos."),
        ex("Si un mensaje habla de un lugar de respeto de la comunidad, ¿qué haces? A) pregunto si se puede nombrar B) lo nombro", "A", "La comunidad decide."),
    ],
    context=[ex("Quieres avisar a tus vecinos que habrá una limpieza del camino. ¿Qué datos pones? A) qué, cuándo y dónde B) solo una palabra", "A", "El mensaje debe ser claro.")],
    selfcheck=[
        ex("Nombra cuatro propósitos de un mensaje.", "Avisar, invitar, agradecer y pedir", "Son los de la clase."),
        ex("Nombra los tres medios donde ocurren las situaciones.", "Natural, social y cultural", "Son los tres medios."),
        ex("Verdadero o falso: un mensaje puede incluir un saludo de la ficha de palabras si corresponde.", "Verdadero", "Es un saludo atestiguado."),
    ],
    task=T("Completa una ficha de mensaje para tres situaciones inventadas: (a) cuidar la vertiente de una comunidad; (b) invitar a una reunión de vecinos; (c) agradecer a una persona que enseñó a tejer. Para cada una escribe: remitente, destinatario, propósito, medio (natural, social o cultural) y una frase breve de no más de ocho palabras. Termina con una pregunta que le harías al educador tradicional sobre cómo se saluda o agradece en tu comunidad.",
           "(a) Remitente: la comunidad. Destinatario: los vecinos. Propósito: avisar. Medio: natural. Frase: Cuidemos la vertiente entre todos. (b) Remitente: la directiva. Destinatario: los vecinos. Propósito: invitar. Medio: social. Frase: Reunión en la sede el sábado. (c) Remitente: el curso. Destinatario: doña Berta. Propósito: agradecer. Medio: cultural. Frase: Gracias por enseñarnos a tejer. Pregunta: ¿cómo se agradece en nuestra lengua?",
           ["completa los cinco datos", "usa frases breves", "clasifica el medio"], ["tres fichas de mensaje", "pregunta escrita"], ["frases largas", "palabras indígenas sin fuente"],
           "Pedir que cuente las palabras de cada frase; valorar la pregunta final."),
    reinforce="Escribe en tu hoja una frase breve para cada propósito: avisar, invitar, agradecer y pedir.",
    extend="Escribe un aviso breve para cuidar un lugar natural de tu comunidad.",
)

L(
    LR4, 2,
    materials=MAT,
    use="Aprenderé a leer un mensaje con límites declarados: qué dice, qué no dice y qué datos faltan. Sirve para escribir mensajes completos y para entender los de otras personas sin suponer.",
    prior=["Sé situar un mensaje.", "Sé distinguir lo que dice un texto de lo que imagino."],
    explain=[
        "Un mensaje completo responde a cuatro preguntas: qué, cuándo, dónde y quién. Por ejemplo, «Limpieza del camino: sábado 10:00, frente a la sede. Trae una pala. Comunidad Quebrada Verde». Si falta alguna respuesta, quien lo lee puede equivocarse. Por eso leemos los mensajes buscando esos datos.",
        "Leer con límites declarados es decir qué dice el mensaje, qué no dice y qué datos faltan. En «Reunión en la sede», no sabemos cuándo es. Eso no se completa suponiendo una fecha. Si necesitamos el dato, preguntamos a quien envió el mensaje. Y si el mensaje habla de algo que la comunidad reserva, no lo difundimos.",
        "También revisamos el tono: un aviso para toda la comunidad se escribe con respeto y sin órdenes bruscas; un agradecimiento es cálido y breve. Los mensajes pueden llevar un saludo de la ficha de palabras si corresponde. Todo lo que no entendemos de una palabra indígena lo preguntamos al educador tradicional.",
    ],
    vocab=[("dato que falta", "información que el mensaje no trae y es necesaria"), ("tono", "manera de decir algo, amable o seria"), ("difundir", "compartir con muchas personas"), ("completo", "que trae todos los datos necesarios"), ("aviso", "mensaje que informa algo")],
    worked=[
        W("Encontrar los datos", "Mensaje: «Limpieza del camino: sábado 10:00, frente a la sede. Trae una pala». ¿Cuándo y dónde es?", ["Busco cuándo: sábado 10:00.", "Busco dónde: frente a la sede."], "El sábado a las 10:00, frente a la sede."),
        W("Dato que falta", "Mensaje: «Reunión en la sede». ¿Qué datos faltan?", ["Dice qué (reunión) y dónde (en la sede).", "No dice cuándo ni quién lo envía."], "Faltan cuándo y quién."),
    ],
    mistakes=[
        M("Suponer un dato que el mensaje no trae.", "Puedo llegar a otro momento.", "Pregunto a quien lo envió."),
        M("Difundir un mensaje que menciona algo reservado.", "La comunidad decide.", "Pregunto antes."),
    ],
    R=[
        ex("Un mensaje completo responde: A) qué, cuándo, dónde y quién B) solo quién", "A", "Esos son los datos."),
        ex("Mensaje: «Limpieza del camino: sábado 10:00, frente a la sede». ¿En qué lugar es?", "Frente a la sede", "El mensaje lo dice."),
        ex("Mensaje: «Trae una pala». ¿Qué debes llevar?", "Una pala", "El mensaje lo dice."),
    ],
    C=[
        ex("Verdadero o falso: si falta un dato, puedo suponerlo.", "Falso", "Se pregunta a quien lo envió."),
        ex("¿Qué es el tono de un mensaje? A) la manera de decir algo B) el tamaño de la letra", "A", "Puede ser amable o serio."),
        ex("Mensaje: «Reunión en la sede». ¿Dice cuándo es?", "No", "Falta ese dato."),
    ],
    A=[
        ex("Mensaje: «Gracias por enseñarnos. Comunidad Lomas del Sur». ¿Quién envía el mensaje?", "La comunidad Lomas del Sur", "Lo dice al final."),
        ex("Mensaje: «Invitación: taller de siembra, jueves 16:00, patio de la escuela». Une cada dato con su pregunta. 1) jueves 16:00 2) patio de la escuela. a) ¿dónde? b) ¿cuándo?", "1-b, 2-a", "Cada dato responde una pregunta."),
        ex("Mensaje: «Limpieza del camino mañana». ¿Qué datos faltan: la hora y el lugar o solo la hora?", "La hora y el lugar", "No dice ni hora ni lugar."),
    ],
    Z=[
        ex("Tomás lee «Reunión en la sede» y decide que es el sábado. ¿Qué error comete?", "Supone la fecha", "El mensaje no la trae."),
        ex("Un mensaje dice «Vamos al lugar de respeto de la comunidad, que está en el cerro». La comunidad no lo comparte. ¿Qué haces? A) no lo difundo y pregunto B) lo comparto", "A", "La comunidad decide."),
    ],
    D=[
        ex("Dos avisos. A1: «Limpieza del camino: sábado 10:00, frente a la sede». A2: «Limpieza del camino pronto». ¿Cuál es más completo?", "A1", "Trae cuándo y dónde; A2 solo dice «pronto»."),
        ex("¿Cuál reescritura hace más completo el mensaje «Reunión en la sede»? A) «Reunión en la sede el sábado a las 10:00. Directiva de la comunidad» B) «Reunión en la sede, ven pronto»", "A", "Agrega cuándo y quién; «pronto» no es un dato."),
    ],
    context=[ex("Recibes el mensaje «Hay trabajo en la quebrada» sin más datos. ¿Qué haces? A) pregunto qué, cuándo y dónde B) voy a cualquier hora", "A", "Faltan datos para ir.")],
    selfcheck=[
        ex("Nombra los cuatro datos de un mensaje completo.", "Qué, cuándo, dónde y quién", "Son los datos de la clase."),
        ex("Verdadero o falso: puedo completar con mi imaginación lo que el mensaje no dice.", "Falso", "Lo que falta se pregunta."),
        ex("¿Quién envía el mensaje «Gracias por enseñarnos. Comunidad Lomas del Sur»?", "La comunidad Lomas del Sur", "Se indica al final."),
    ],
    task=T("Lee estos tres mensajes de práctica: (1) «Reunión en la sede». (2) «Taller de siembra, jueves 16:00, patio de la escuela. Trae semillas». (3) «Limpieza del camino mañana». Haz una tabla de cuatro columnas: mensaje, qué dice, qué dato falta y cómo lo completarías sin suponer (a quién preguntarías). Reescribe el mensaje (1) como un mensaje completo inventando un día, una hora y un remitente.",
           "(1) dice que hay reunión en la sede; faltan cuándo y quién lo envía; preguntaría a la directiva. (2) dice taller, cuándo, dónde y qué traer; falta quién lo envía. (3) dice limpieza mañana; faltan la hora, el lugar y quién lo envía; preguntaría a quien lo envió. Reescrito: Reunión en la sede el sábado a las 10:00. Directiva de la comunidad.",
           ["identifica datos que faltan", "no supone", "reescribe un mensaje completo"], ["tabla de cuatro columnas", "mensaje reescrito"], ["suponer datos", "mensajes sin remitente"],
           "Pedir que señale cada dato en el mensaje; valorar que pregunte en vez de suponer."),
    reinforce="Subraya en cada mensaje el qué, el cuándo y el dónde con colores distintos.",
    extend="Escribe tres mensajes cortos incompletos y pide a un compañero que diga qué dato falta.",
)

L(
    LR4, 3,
    materials=MAT + " " + FICHA_PAL,
    use="Aprenderé a ajustar un mensaje a la situación y a quien lo recibirá, cuidando el medio natural, social y cultural. Sirve para escribir mensajes que se entiendan y respeten a las personas y a la comunidad.",
    prior=["Sé que un mensaje completo dice qué, cuándo, dónde y quién.", "Sé que las palabras de la ficha de palabras se usan solo si corresponden."],
    explain=[
        "Un mensaje se ajusta a quien lo recibe. A una persona mayor de la comunidad le escribimos con respeto y tratamiento amable, como «don» o «doña». A un compañero le escribimos de manera cercana. A toda la comunidad le escribimos con un tono claro y cordial, sin órdenes bruscas. El destinatario cambia las palabras, pero no los datos.",
        "Según el medio, el mensaje cambia su contenido. En el medio natural, avisamos cómo cuidar un lugar: «No botes basura al río». En el medio social, convocamos o agradecemos: «Reunión en la sede el sábado». En el medio cultural, valoramos lo que se aprende: «Gracias por enseñarnos». Un saludo como «mari mari» o un agradecimiento como «chaltumay» puede acompañar el mensaje si la comunidad lo usa así.",
        "Para usar esas palabras con cuidado, confirmamos con el educador tradicional si corresponden a la situación y a la persona. No las ponemos solo para que el mensaje «se vea indígena». Tampoco inventamos palabras en lengua indígena. Si queremos más palabras, las pedimos a quien las habla y anotamos quién nos las enseñó.",
    ],
    vocab=[("tratamiento", "forma respetuosa de dirigirse a alguien, como «doña»"), ("tono cordial", "manera amable y respetuosa de decir algo"), ("medio natural", "situación que tiene que ver con la naturaleza"), ("medio social", "situación que tiene que ver con las personas y su convivencia"), ("medio cultural", "situación que tiene que ver con saberes y prácticas de la comunidad")],
    worked=[
        W("Ajustar al destinatario", "Escribe un agradecimiento a doña Berta, que enseñó a tejer.", ["Uso «doña».", "Escribo una frase breve y cálida."], "Gracias, doña Berta, por enseñarnos a tejer."),
        W("Elegir el medio", "Mensaje: «No botes basura a la vertiente». ¿De qué medio es?", ["Pienso de qué trata el mensaje.", "Se trata de cuidar un lugar de la naturaleza."], "Medio natural."),
    ],
    mistakes=[
        M("Escribir órdenes bruscas a la comunidad.", "No muestran respeto.", "Uso un tono cordial."),
        M("Poner «mari mari» solo para que el mensaje suene indígena.", "No corresponde a la situación.", "Lo uso solo si la comunidad lo usa así."),
    ],
    R=[
        ex("A una persona mayor le escribo con: A) un tratamiento respetuoso B) bromas", "A", "Esa forma muestra respeto."),
        ex("Un mensaje para cuidar un río es del medio: A) natural B) cultural", "A", "Cuida la naturaleza."),
        ex(FICHA_PAL + " ¿Qué palabra de la ficha sirve como agradecimiento en mapuzugun?", "Chaltumay", "La ficha lo traduce como gracias."),
    ],
    C=[
        ex("Verdadero o falso: el destinatario cambia las palabras del mensaje, pero no los datos.", "Verdadero", "Los datos deben mantenerse."),
        ex("¿Qué mensaje es del medio social? A) «Reunión en la sede el sábado» B) «No botes basura al río»", "A", "Convoca a personas."),
        ex("Verdadero o falso: puedo inventar palabras indígenas para que el mensaje se vea más cultural.", "Falso", "No se inventa lengua."),
    ],
    A=[
        ex("¿Cuál es una versión cordial de «Vengan a la reunión»? A) «Los invitamos a la reunión del sábado a las 10» B) «Vengan ya, no falten»", "A", "Se cambia la orden por una invitación."),
        ex("Une cada mensaje con su medio. 1) «Gracias por enseñarnos a sembrar» 2) «Cuidemos la vertiente» 3) «Reunión de vecinos el sábado». a) social b) cultural c) natural", "1-b, 2-c, 3-a", "Cada mensaje responde a un medio."),
        ex("¿Cuál saludo a una persona mayor usa un tratamiento respetuoso? A) «Buenos días, don Mateo» B) «Ey, Mateo»", "A", "«Don» muestra respeto."),
    ],
    Z=[
        ex("Camila escribe «¡Vengan ya a limpiar!» para toda la comunidad. ¿Qué falla?", "El tono es una orden brusca", "Debe ser cordial."),
        ex("Un compañero dice que pondrá «mari mari» en todos los mensajes. ¿Qué respondes? A) que consulte si corresponde en cada situación B) que está bien", "A", "No siempre corresponde."),
    ],
    D=[
        ex("¿Cuál mensaje es breve, cordial y del medio natural? A) «Cuidemos la vertiente: no dejemos basura» B) «Reunión de vecinos el sábado en la sede»", "A", "Cuidar la vertiente es del medio natural; la reunión es del social."),
        ex("Si quieres agradecer en lengua indígena a una persona de tu comunidad y no estás seguro, ¿qué haces? A) pregunto al educador tradicional cómo se dice B) uso una palabra parecida", "A", "La forma correcta la enseña quien habla."),
    ],
    context=[ex("Vas a escribir un agradecimiento a una persona mayor que vino a tu escuela. ¿Cómo empiezas? A) “Gracias, doña Elena, por venir” B) “Ya gracias”", "A", "Se usa tratamiento respetuoso.")],
    selfcheck=[
        ex("Nombra los tres medios donde ocurren las situaciones.", "Natural, social y cultural", "Son los medios de la clase."),
        ex("Verdadero o falso: un mensaje para la comunidad debe tener tono cordial.", "Verdadero", "Un tono cordial muestra respeto."),
        ex("Verdadero o falso: puedo usar un saludo de la ficha de palabras si corresponde.", "Verdadero", "Es un saludo atestiguado."),
    ],
    task=T("Escribe tres mensajes breves (una frase cada uno, de no más de diez palabras): (a) un aviso del medio natural para cuidar un lugar de tu comunidad; (b) una invitación del medio social a una reunión, con día y hora inventados; (c) un agradecimiento del medio cultural a una persona que enseñó algo. Usa tratamiento respetuoso donde corresponda. Si quieres incluir «mari mari» o «chaltumay», pregunta antes al educador tradicional si corresponde y anota la respuesta.",
           "(a) Cuidemos la vertiente: no dejemos basura. (b) Los invitamos a la reunión del sábado a las 10. (c) Gracias, doña Berta, por enseñarnos a tejer. Consulta: le pregunté al educador tradicional si «chaltumay» corresponde en mi mensaje y anoté lo que me respondió.",
           ["tres mensajes breves", "tono cordial y tratamiento", "medios correctos"], ["tres frases", "nota de consulta"], ["órdenes bruscas", "palabras indígenas sin consulta"],
           "Pedir que cuente las palabras de cada frase; valorar la consulta."),
    reinforce="Reescribe con tono cordial: «Limpien eso ahora».",
    extend="Escribe una versión del agradecimiento para un compañero y otra para una persona mayor, y explica la diferencia.",
)

L(
    LR4, 4,
    materials=MAT,
    use="Aprenderé a escribir mensajes completos con frases breves, atribuyendo la fuente y revisando antes de enviar. Sirve para comunicar con claridad y con respeto en situaciones reales de mi comunidad.",
    prior=["Sé situar un mensaje, completarlo y ajustarlo al destinatario.", "Sé que la validación la hace el educador o la comunidad."],
    explain=[
        "Un mensaje atribuido dice quién lo envía y, si cuenta algo de otra persona, de quién viene. Por ejemplo: «Según doña Clara, la limpieza del camino es el sábado a las 10». Así quien lo recibe sabe en quién confiar. Si un dato es incierto, lo decimos: «Aún no sabemos la hora».",
        "Para escribir un mensaje completo seguimos cinco pasos: elegir el propósito, escribir una frase por idea, incluir qué, cuándo, dónde y quién, ajustar el tono al destinatario y revisar con una lista. La lista pregunta: ¿tiene los cuatro datos?, ¿las frases son breves?, ¿el tono es cordial?, ¿evité datos privados o reservados?, ¿usé solo palabras que corresponden?",
        "Si el mensaje se enviará a la comunidad o incluye palabras en lengua indígena, se lo mostramos antes al educador tradicional o a una persona de la comunidad. Ellos pueden corregir una palabra o decir que algo no debe publicarse. Aceptamos sus correcciones con gratitud. Así los mensajes ayudan a la convivencia y a cuidar lo propio.",
    ],
    vocab=[("atribuir", "decir de quién viene una información"), ("mensaje atribuido", "mensaje que dice quién lo envía o quién dio el dato"), ("lista de revisión", "preguntas para comprobar un mensaje"), ("dato privado", "información personal que no se comparte"), ("convivencia", "vivir juntos con respeto")],
    worked=[
        W("Armar un mensaje completo", "Propósito: avisar de una limpieza del camino. Datos: sábado 10:00, frente a la sede, trae una pala; envía la comunidad Quebrada Verde.", ["Una frase por idea.", "Incluyo qué, cuándo, dónde y quién."], "Limpieza del camino: sábado 10:00, frente a la sede. Trae una pala. Comunidad Quebrada Verde."),
        W("Revisar con la lista", "Mensaje: «Todos vengan a la limpieza, anoten su dirección». ¿Qué falla?", ["Falta cuándo y dónde.", "Pide la dirección, que es un dato privado."], "Faltan datos y se pide un dato privado."),
    ],
    mistakes=[
        M("Pedir datos privados en un mensaje a la comunidad.", "No es necesario y puede ser peligroso.", "Pido solo lo necesario."),
        M("Enviar el mensaje sin revisarlo.", "Pueden quedar errores.", "Uso la lista de revisión."),
    ],
    R=[
        ex("Un mensaje atribuido dice: A) quién lo envía o de quién viene el dato B) solo la hora", "A", "Atribuir es nombrar la fuente."),
        ex("Una dirección de casa es: A) un dato privado B) un dato que siempre se comparte", "A", "No se comparte."),
        ex("Un mensaje completo tiene: A) qué, cuándo, dónde y quién B) solo quién", "A", "Son los cuatro datos."),
    ],
    C=[
        ex("Verdadero o falso: debo revisar el mensaje con una lista antes de enviarlo.", "Verdadero", "Revisar evita errores."),
        ex("Verdadero o falso: puedo pedir las direcciones de todos en un aviso a la comunidad.", "Falso", "Son datos privados."),
        ex("¿Quién puede corregir una palabra indígena de mi mensaje? A) el educador tradicional B) cualquier compañero", "A", "Conoce la lengua."),
    ],
    A=[
        ex("Ordena los pasos: a) reviso con la lista b) elijo el propósito c) escribo una frase por idea d) ajusto el tono. Escribe las letras.", "b, c, d, a", "Propósito, frases, tono y revisión."),
        ex("Completa con atribución: «___ doña Clara, la limpieza del camino es el sábado a las 10».", "Según", "Atribuye la información."),
        ex("Mensaje: «Taller de siembra, jueves 16:00, patio de la escuela». ¿Está completo, con qué, cuándo, dónde y quién? Responde Sí o No.", "No", "Falta quién lo envía."),
    ],
    Z=[
        ex("Pablo envía «Según todos, la reunión es mañana». ¿Qué falla?", "No nombra una fuente concreta", "“Todos” no es una fuente."),
        ex("Una niña quiere enviar a la comunidad un mensaje con una palabra indígena que no conoce bien. ¿Qué debe hacer? A) mostrarlo antes al educador tradicional B) enviarlo igual", "A", "Él puede corregirlo."),
    ],
    D=[
        ex("¿Cuál mensaje es completo? M1: «Invitación: limpieza del camino, sábado 10:00, frente a la sede. Comunidad Quebrada Verde». M2: «Invitación: limpieza del camino, sábado 10:00».", "M1", "M1 trae qué, cuándo, dónde y quién; M2 no dice dónde ni quién."),
        ex("Si el educador tradicional dice que una palabra no corresponde, ¿qué haces? A) la saco y le agradezco B) la dejo", "A", "Se acepta la corrección."),
    ],
    context=[ex("Vas a enviar un mensaje a toda tu comunidad. ¿Qué haces antes? A) lo reviso con la lista y lo muestro a quien corresponde B) lo envío rápido", "A", "La revisión cuida el respeto.")],
    selfcheck=[
        ex("Nombra los cinco pasos para escribir un mensaje completo.", "Propósito, frase por idea, datos, tono y revisión", "Son los pasos de la clase."),
        ex("Verdadero o falso: un dato incierto debe decirse: «aún no sabemos…».", "Verdadero", "Decirlo es ser honesto."),
        ex("Verdadero o falso: puedo inventar un remitente si no sé quién envía.", "Falso", "El remitente debe ser real."),
    ],
    task=T("Escribe dos mensajes completos de dos o tres frases breves cada uno, para una comunidad inventada: (a) un aviso del medio natural (por ejemplo, cuidar un cerro o una vertiente) y (b) un agradecimiento del medio cultural a una persona que enseñó algo. Cada mensaje debe incluir qué, cuándo (si corresponde), dónde (si corresponde), quién y, si cuenta algo de otra persona, «según…». Revísalos con la lista de cinco preguntas y marca los que cumpliste. Escribe qué le mostrarías al educador tradicional antes de enviarlos.",
           "(a) Cuidemos la vertiente. Según doña Clara, este sábado a las 10 limpiamos frente a la sede. Comunidad Lomas del Sur. (b) Gracias, don Mateo, por enseñarnos a sembrar. Curso 5.º básico. Lista: cuatro datos, frases breves, tono cordial, sin datos privados, palabras que corresponden. Mostraría al educador tradicional si corresponde usar «chaltumay» en el agradecimiento.",
           ["incluye los datos necesarios", "atribuye con «según»", "revisa con la lista"], ["dos mensajes", "lista marcada", "nota para el educador"], ["pedir datos privados", "palabras indígenas sin consulta"],
           "Pedir que muestre cada punto de la lista; valorar la nota para el educador."),
    reinforce="Escribe un mensaje completo de una frase para invitar a una reunión.",
    extend="Escribe una nota de agradecimiento al educador tradicional usando «chaltumay» solo como lo dice la ficha de palabras.",
)
