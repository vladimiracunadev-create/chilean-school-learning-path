"""Cuaderno del estudiante, 5.º básico Orientación: OA 01 (valoración positiva de sí mismo) y OA 02 (emociones y su expresión)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1, OA2 = "OR05 OA 01", "OR05 OA 02"


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 01
lesson(
    OA1, 1,
    "Una hoja y un lápiz. El caso de Noa y todos los datos están escritos en los ejercicios. Trabajas con un personaje inventado: no necesitas contar nada privado tuyo.",
    "Aprenderé a distinguir habilidades, fortalezas y aspectos a superar usando evidencia. Sirve para valorarme con sinceridad, sin presumir y sin criticarme de más.",
    ["Sé que un hecho se puede observar y una etiqueta no.", "Sé que lo íntimo se cuenta solo si uno quiere."],
    [
        "Valorarse de forma positiva es reconocer con sinceridad lo que uno vale. Eso incluye tres cosas. Una habilidad es algo que sabes hacer y puedes mejorar. Una fortaleza es una habilidad o una forma de ser que te ayuda a ti y también a otros. Un aspecto a superar es algo que hoy te cuesta y que puedes mejorar con práctica y con ayuda.",
        "Valorarse bien no es presumir ni decir «soy perfecto». Tampoco es insultarse con frases como «soy un desastre». Para no equivocarte necesitas evidencia: un hecho que se pueda mostrar. «Entregué el cartel a tiempo» es evidencia. «Todos piensan que soy genial» no lo es, porque no dice qué hiciste.",
        "Imagina a Noa, una estudiante inventada. Esta semana dibujó el cartel del curso, escribió la lista de turnos sin errores y ayudó a Pía con una resta. También aceptó cinco tareas y entregó solo dos. Noa tiene habilidades y fortalezas, y además un aspecto a superar: organizar su tiempo. Todo eso es verdad al mismo tiempo.",
    ],
    [("habilidad", "algo que sé hacer y puedo mejorar"), ("fortaleza", "habilidad o forma de ser que me ayuda a mí y a otros"), ("aspecto a superar", "algo que hoy me cuesta y puedo mejorar"), ("evidencia", "un hecho que se puede mostrar"), ("valoración positiva", "reconocer con sinceridad lo que valgo, también lo que quiero mejorar")],
    [
        W("Clasificar un hecho", "Hecho: «Noa escribió la lista de turnos sin errores». ¿Es evidencia de una habilidad o de un aspecto a superar?", ["Pregunta: ¿lo hizo bien y se puede mostrar? Sí, la lista existe.", "Escribir sin errores es algo que Noa sabe hacer.", "Por eso es evidencia de una habilidad."], "Evidencia de una habilidad"),
        W("Frase justa", "Noa entregó 2 de 5 tareas. ¿Qué frase es más justa: «Soy un desastre» o «Todavía me cuesta organizar mi tiempo: entregué 2 de 5 tareas»?", ["«Soy un desastre» juzga a toda la persona sin evidencia.", "La segunda frase dice un hecho y deja espacio para mejorar.", "Una valoración positiva es sincera y no hiere."], "«Todavía me cuesta organizar mi tiempo: entregué 2 de 5 tareas»"),
    ],
    [
        M("Pensar que valorarme bien es decir que soy perfecto.", "Se confunde sentirse bien con no tener nada que mejorar.", "Reconoce lo que haces bien y también lo que quieres mejorar, con evidencia."),
        M("Decir «no sirvo para esto» después de un solo error.", "Un solo hecho parece mostrar cómo es toda la persona.", "Di «todavía me cuesta» y cuenta el hecho que lo muestra."),
    ],
    R=[
        ex("«Noa dibujó el cartel del curso y lo entregó a tiempo». ¿Muestra una habilidad o un aspecto a superar?", "Una habilidad", "Es algo que Noa sabe hacer y que se puede mostrar con el cartel."),
        ex("«A Noa todavía le cuesta decir que no cuando le piden demasiadas tareas». ¿Es una habilidad o un aspecto a superar?", "Un aspecto a superar", "Es algo que hoy le cuesta y puede mejorar con práctica."),
        ex("¿Qué es una evidencia: «Todos dicen que Noa es genial» o «Noa entregó la lista sin errores»?", "«Noa entregó la lista sin errores»", "Cuenta algo que Noa hizo y que se puede comprobar."),
    ],
    U=[
        ex("¿Por qué tener un aspecto a superar no significa ser una mala persona?", "Porque se puede mejorar con práctica", "Es algo que cambia con tiempo y ayuda, no una forma fija de ser."),
        ex("¿La valoración positiva de uno mismo incluye reconocer lo que se quiere mejorar? Responde sí o no.", "Sí", "Valorarse con sinceridad mira lo que se hace bien y lo que se puede mejorar."),
        ex("¿Cuál frase es una valoración sincera: «Soy perfecta en todo» o «Soy buena para dibujar y todavía me cuesta organizar mi tiempo»?", "«Soy buena para dibujar y todavía me cuesta organizar mi tiempo»", "Incluye una habilidad y un aspecto a superar, sin exagerar."),
    ],
    A=[
        ex("Hechos de Noa: 1) dibujó el cartel, 2) escribió la lista sin errores, 3) ayudó a Pía con una resta, 4) no alcanzó a entregar las invitaciones. ¿Cuántos son evidencia de habilidades o fortalezas?", "3", "Los hechos 1, 2 y 3 muestran algo que Noa sabe hacer; el 4 muestra un aspecto a superar."),
        ex("¿Qué fortaleza apoya el hecho «Noa ayudó a Pía con una resta»: dibujar bien o ayudar a otros?", "Ayudar a otros", "Explicarle algo a una compañera la ayudó a ella, no solo a Noa."),
        ex("Escribe «No sirvo para organizarme» como aspecto a superar con «todavía» y un hecho de Noa.", "Todavía me cuesta organizar mi tiempo: no entregué las invitaciones", "Usa «todavía» y un hecho comprobable en vez de una etiqueta."),
    ],
    Z=[
        ex("Un compañero dice: «Noa no entregó las invitaciones, entonces Noa no sirve». ¿Qué error comete?", "Usa un solo hecho para juzgar a toda la persona", "Un hecho aislado no muestra cómo es Noa en todo lo demás."),
        ex("Noa tiene tres evidencias de habilidades y un aspecto a superar. ¿Es justo decir que solo tiene defectos?", "No", "Los hechos muestran más habilidades que dificultades, y la dificultad puede mejorar."),
    ],
    D=[
        arith("Noa aceptó 5 tareas y entregó 2. ¿Cuántas tareas quedaron sin entregar?", "5-2", "Las tareas pendientes son las aceptadas menos las entregadas."),
        arith("Noa tenía 90 minutos para sus tareas. Gastó 45 minutos en el cartel y 25 en la lista de turnos. ¿Cuántos minutos le quedaron para las otras 3 tareas?", "90-45-25", "Al total se le restan los dos tiempos ya usados."),
    ],
    context=[ex("El profesor pide completar: «Una habilidad mía es… porque…; quiero mejorar… y mi primer paso es…». Luz escribe: «Una habilidad mía es leer, porque terminé 2 libros del plan lector. Quiero mejorar mi letra; mi primer paso es escribir una línea despacio cada día». ¿Luz usó evidencia?", "Sí", "Apoyó su habilidad con un hecho: los 2 libros terminados.")],
    selfcheck=[ex("En Orientación: ¿valorarse bien es lo mismo que presumir?", "No", "Es reconocer con sinceridad lo que uno hace bien y lo que puede mejorar."), ex("¿Una evidencia es algo que se puede mostrar?", "Sí", "Es un hecho, no una opinión."), ex("¿Un aspecto a superar se puede mejorar con práctica?", "Sí", "Lo que cuesta hoy puede cambiar con tiempo y ayuda.")],
    task=T("Lee el perfil de Teo, un estudiante inventado. Hechos: ordenó el material de arte de su grupo; tradujo una instrucción de inglés a sus compañeros; se puso nervioso al exponer y habló muy bajo; esperó su turno para hablar aunque estaba nervioso. Escribe una habilidad con su evidencia, una fortaleza con su evidencia y un aspecto a superar con «todavía». No uses etiquetas.", "Habilidad: ordenar, porque ordenó el material de arte de su grupo. Fortaleza: ayudar a otros, porque tradujo una instrucción de inglés a sus compañeros. Aspecto a superar: todavía me cuesta hablar fuerte al exponer; hoy habló muy bajo.", ["escribe una habilidad con evidencia", "escribe una fortaleza con evidencia", "escribe un aspecto a superar con «todavía» y un hecho", "no usa etiquetas ni cuenta algo íntimo"], ["texto escrito o dicho", "cuadro de tres columnas"], ["decir la habilidad sin evidencia", "usar una etiqueta como «tímido»"], "Reconoce lo bien escrito y pregunta qué hecho apoya cada afirmación."),
    reinforce="Escribe tres hechos de un personaje de cuento y clasifica cada uno como habilidad o aspecto a superar.",
    extend="Cambia una frase negativa que hayas escuchado sobre alguien («es un desastre») por un hecho con «todavía».",
)

lesson(
    OA1, 2,
    "Una hoja y un lápiz. El caso de Alex está escrito en los ejercicios.",
    "Aprenderé a separar lo que pasó, lo que siento y lo que me digo, y a poner un límite cuando me piden demasiado. Sirve para valorarme sin dejar que una mala racha me defina.",
    ["Sé distinguir habilidades, fortalezas y aspectos a superar con evidencia.", "Sé que un hecho se puede observar."],
    [
        "Cuando algo sale mal, se mezclan tres cosas. El hecho es lo que pasó y se puede observar: «Alex respondió bien 9 de 20 preguntas». La emoción es lo que siente la persona: desánimo, vergüenza o rabia. Y la voz crítica es lo que se dice a sí misma: «soy tonto». La voz crítica suele parecer un hecho, pero no lo es. Es una suposición sin evidencia y exagera.",
        "Separar las tres cosas ayuda a valorarse bien. El hecho se acepta. La emoción se reconoce: «me siento desanimado». Y la voz crítica se cambia por una frase más justa: «hoy me fue mal en esta prueba y puedo estudiar de otra manera». Una mala racha no define a una persona entera.",
        "También hay un límite. Un límite es lo que puedo y no puedo hacer ahora sin perjudicarme. Si te piden más cosas de las que alcanzas a hacer, puedes decir: «ahora no puedo asumir eso, pero puedo ayudar con esto otro». Poner un límite con respeto también es cuidar tu valoración.",
    ],
    [("hecho", "lo que pasó y se puede observar"), ("emoción", "lo que siente una persona"), ("voz crítica", "frase dura que una persona se dice a sí misma"), ("límite", "lo que puedo y no puedo hacer ahora sin perjudicarme"), ("mala racha", "período en que varias cosas salen mal, pero que pasa")],
    [
        W("Separar hecho y voz crítica", "Alex dice: «Respondí bien 9 de 20 preguntas. Soy un tonto». ¿Cuál parte es el hecho?", ["Pregunta: ¿se puede observar? Las 9 respuestas buenas sí.", "«Soy un tonto» no se puede observar: es una suposición dura.", "El hecho es la primera frase."], "«Respondí bien 9 de 20 preguntas»"),
        W("Poner un límite", "A Alex le piden hacer los carteles, la lista y las invitaciones, y solo alcanza a hacer una cosa. ¿Qué puede decir?", ["Un límite dice lo que puede hacer ahora.", "Puede proponer algo posible sin enojarse.", "Así cuida su tiempo y colabora."], "«Ahora solo puedo hacer los carteles; ¿alguien puede tomar la lista?»"),
    ],
    [
        M("Creer que sentir desánimo prueba que no sirvo.", "Se confunde una emoción pasajera con un hecho sobre uno mismo.", "Reconoce la emoción y mira los hechos: qué pasó y qué puedes hacer."),
        M("Aceptar todas las tareas para que no se enojen conmigo.", "Se piensa que decir que no pone en riesgo la amistad.", "Di lo que alcanzas a hacer con respeto: «esto sí puedo»."),
    ],
    R=[
        ex("«Alex respondió bien 9 de 20 preguntas». ¿Es un hecho o una voz crítica?", "Un hecho", "Cuenta algo que pasó y se puede comprobar."),
        ex("«Me siento desanimado después de la prueba». ¿Nombra una emoción o un hecho?", "Una emoción", "Dice lo que siente la persona, no lo que pasó."),
        ex("«Soy un tonto». ¿Es una voz crítica o un hecho?", "Una voz crítica", "Es una frase dura que Alex se dice sin evidencia."),
    ],
    U=[
        ex("¿Por qué «soy un tonto» no puede ser un hecho?", "No se puede observar ni comprobar", "Es una exageración que se dice a sí mismo."),
        ex("¿Qué frase reemplaza mejor la voz crítica: «Hoy me fue mal en esta prueba y puedo estudiar de otra manera» o «Nunca voy a aprender»?", "«Hoy me fue mal en esta prueba y puedo estudiar de otra manera»", "Es justa: acepta el hecho y deja espacio para mejorar."),
        ex("¿Poner un límite con respeto ayuda a cuidar mi valoración personal? Responde sí o no.", "Sí", "Me permite cumplir lo que prometo sin agotarme."),
    ],
    A=[
        ex("Separa: «Perdí el partido de mi equipo, me da pena y creo que soy un inútil». ¿Cuál es la voz crítica?", "«creo que soy un inútil»", "Es la frase dura sin evidencia; lo otro es hecho y emoción."),
        ex("Alex dice: «Entregué 6 de 8 trabajos de la semana». ¿Es un hecho que muestra un aspecto a superar o un fracaso total?", "Un hecho que muestra un aspecto a superar", "La mayoría de los trabajos se entregó y puede mejorar la organización."),
        ex("Un compañero pide a Alex otra tarea que no alcanza a hacer. ¿Cuál respuesta pone un límite respetuoso: «Ahora no puedo asumir eso, pero puedo ayudar con la lista» o «Hazlo tú, no me importa»?", "«Ahora no puedo asumir eso, pero puedo ayudar con la lista»", "Dice lo que puede hacer, con respeto y sin ofender."),
    ],
    Z=[
        ex("Si una persona confunde su voz crítica con un hecho, ¿qué es probable que pase con su valoración de sí misma?", "Se valorará menos de lo justo", "Cree frases duras que no están comprobadas."),
        ex("Una niña piensa: «Si digo que no a una tarea, ya no me van a querer». ¿Qué suposición hace?", "Que decir que no la deja sin cariño", "No tiene evidencia: un límite respetuoso no quita el afecto."),
    ],
    D=[
        arith("Alex respondió bien 9 de 20 preguntas. ¿Cuántas respondió mal o dejó en blanco?", "20-9", "Las que no acertó son el total menos las acertadas."),
        arith("En tres pruebas Alex acertó 9, 12 y 15 preguntas. ¿Cuántas preguntas más acertó en la tercera que en la primera?", "15-9", "La diferencia entre la tercera y la primera muestra su progreso."),
    ],
    context=[ex("Después de un partido en el patio, un niño inventado dice: «Fallé dos pases, me da vergüenza y soy un desastre en el fútbol». Si quiere hablarse con justicia, ¿qué parte debe cambiar?", "La parte «soy un desastre en el fútbol»", "Es la voz crítica; los pases fallados y la vergüenza sí son hecho y emoción.")],
    selfcheck=[ex("En Orientación: ¿una emoción es lo mismo que un hecho?", "No", "La emoción es lo que siento; el hecho es lo que pasó."), ex("¿Una mala racha define a toda la persona?", "No", "Pasa y se puede cambiar."), ex("¿Poner un límite puede hacerse con respeto?", "Sí", "Se dice lo que sí puedo hacer.")],
    task=T("Lee el caso de Alex, un estudiante inventado: «Hoy respondí bien 9 de 20 preguntas. Me siento muy desanimado. Pienso que soy un tonto. Además, mis compañeros me pidieron preparar toda la presentación yo solo». Escribe: el hecho, la emoción, la voz crítica con una frase más justa, y un límite respetuoso que Alex podría decir.", "Hecho: acerté 9 de 20. Emoción: desánimo. Voz crítica: «soy un tonto»; más justa: «hoy me fue mal y puedo estudiar distinto». Límite: «puedo preparar la introducción; ¿quién hace el resto?»", ["separa hecho, emoción y voz crítica", "reescribe la voz crítica con una frase justa", "escribe un límite respetuoso concreto"], ["texto escrito o dicho", "tabla de cuatro partes"], ["tomar la voz crítica como hecho", "un límite que ofende"], "Reconoce lo bien separado y pide que el límite diga qué sí puede hacer."),
    reinforce="Escribe un hecho, una emoción y una voz crítica de un personaje inventado y reescribe su voz crítica.",
    extend="Escribe dos límites respetuosos para dos situaciones inventadas en las que alguien pide más de lo que alcanzas.",
)

lesson(
    OA1, 3,
    "Una hoja y un lápiz. El caso de Tomás está escrito en los ejercicios.",
    "Aprenderé a comparar distintas formas de enfrentar algo que me cuesta y a prever qué pasa con cada una. Sirve para elegir una forma que me ayude a mejorar.",
    ["Sé separar hecho, emoción y voz crítica.", "Sé que un aspecto a superar puede mejorar."],
    [
        "Cuando algo te cuesta, tienes varias opciones. Una opción es evitarlo: no leer en voz alta nunca. Otra es insistir solo sin apoyo, aunque te salga mal una y otra vez. Otra es practicar poco a poco y pedir ayuda. Cada opción tiene consecuencias: lo que pasa después, para ti y para otros. Para elegir bien, hay que mirar las consecuencias de cada una.",
        "Imagina a Tomás, un estudiante inventado. Le da nervios leer en voz alta. Si lo evita, hoy se siente aliviado, pero mañana le costará lo mismo o más. Si practica un párrafo corto con una persona de su casa y luego en clase, hoy siente nervios, pero con el tiempo mejora. Si pide ayuda al profesor, recibe una idea que a solas no encontraba.",
        "Una buena opción es segura, posible y le sirve a la persona para avanzar. Pedir ayuda no es un fracaso: es una estrategia. Se pide ayuda a quien puede orientar, por ejemplo un profesor, una persona de tu casa o un orientador del colegio.",
    ],
    [("opción", "una de las formas posibles de actuar"), ("consecuencia", "lo que pasa después de una acción"), ("evitar", "no hacer algo para no sentir incomodidad"), ("estrategia", "plan de acciones para lograr un objetivo"), ("pedir ayuda", "contar lo que nos cuesta a alguien que puede apoyar")],
    [
        W("Comparar consecuencias", "Tomás evita leer en voz alta todos los días durante un mes. ¿Qué probablemente pasa con su aspecto a superar?", ["Evitar da alivio hoy.", "Pero sin práctica, no hay avance.", "Con el tiempo sigue costando lo mismo o más."], "Probablemente sigue costándole igual o más"),
        W("Elegir una opción posible", "Tomás puede (a) leer un párrafo corto de 4 líneas a una persona de su casa o (b) leer el capítulo entero frente al curso mañana. ¿Cuál es mejor primer paso?", ["Un primer paso debe ser posible y seguro.", "(a) es pequeño y con apoyo.", "(b) es demasiado grande para empezar."], "(a), leer 4 líneas a una persona de su casa"),
    ],
    [
        M("Creer que evitar siempre es lo más seguro.", "Evitar quita la incomodidad hoy, pero no deja practicar.", "Elige un primer paso pequeño y con apoyo."),
        M("Pensar que pedir ayuda muestra que soy débil.", "Se cree que uno debe poder con todo solo.", "Pedir ayuda es una estrategia que usan las personas para aprender."),
    ],
    R=[
        ex("Si Tomás evita leer en voz alta, ¿se siente más tranquilo hoy o mañana mejora seguro?", "Más tranquilo hoy", "Evitar da alivio inmediato, pero no entrena la habilidad."),
        ex("¿Pedir ayuda al profesor es una estrategia o un fracaso?", "Una estrategia", "Es una forma de aprender con apoyo."),
        ex("Una consecuencia, ¿es lo que pasa antes o después de una acción?", "Después", "Es el resultado de lo que se hace."),
    ],
    U=[
        ex("¿Por qué practicar poco a poco suele ayudar más que evitar?", "Porque con práctica la habilidad mejora", "Repetir con calma entrena lo que cuesta."),
        ex("Tomás tiene nervios al leer en voz alta. ¿Es una opción segura leer 4 líneas a una persona de su casa?", "Sí", "Es pequeña, posible y con apoyo."),
        ex("¿Qué debe mirar quien elige entre varias opciones: las consecuencias o solo lo que le da menos incomodidad hoy?", "Las consecuencias", "Así prevé lo que pasa después, para sí y para otros."),
    ],
    A=[
        ex("Opciones para Tomás: 1) no leer nunca, 2) leer 4 líneas a alguien de su casa, 3) leer el capítulo entero mañana frente al curso, 4) contarle al profesor que le cuesta. ¿Cuántas son pequeñas, seguras y con apoyo?", "2", "La opción 2 y la 4 son posibles y con apoyo; la 1 evita y la 3 es demasiado grande."),
        ex("Si Tomás elige la opción 4 y le cuenta al profesor, ¿qué consecuencia positiva es probable: recibir una idea nueva o que el profesor lo regañe sin escucharlo?", "Recibir una idea nueva", "Quien orienta puede sugerir un primer paso que Tomás no conocía."),
        ex("Completa: «Si evito hacerlo siempre, la consecuencia es que mi habilidad… (mejora/se queda igual)».", "Se queda igual", "Sin práctica no hay avance."),
    ],
    Z=[
        ex("Dos niños tienen vergüenza al exponer. Uno practica un minuto cada día y el otro no practica. ¿Cuál tiene más probabilidad de mejorar?", "El que practica cada día", "La práctica repetida entrena la habilidad."),
        ex("¿Por qué la opción «insistir solo sin apoyo y sin cambiar nada» puede no funcionar aunque sea valiente?", "Porque repite lo mismo sin una idea nueva", "A veces falta información o una guía para cambiar la forma de practicar."),
    ],
    D=[
        arith("Tomás practica leer 4 líneas cada día durante 5 días. ¿Cuántas líneas lee en total?", "4*5", "Son 4 líneas repetidas en 5 días."),
        arith("En la semana 1 Tomás lee 4 líneas. Cada semana siguiente lee 2 líneas más que la anterior. ¿Cuántas líneas lee en la semana 4?", "4+2+2+2", "Parte de 4 en la semana 1 y suma 2 en cada una de las 3 semanas siguientes."),
    ],
    context=[ex("Una estudiante inventada se pone nerviosa al preguntar en clase. Puede (a) nunca preguntar, (b) escribir su pregunta y leerla, (c) preguntarle al profesor al final de la clase. ¿Cuál opción deja la duda sin respuesta?", "(a)", "Si nunca pregunta, la duda sigue; en (b) y (c) pregunta con un apoyo.")],
    selfcheck=[ex("En Orientación: ¿evitar siempre ayuda a mejorar un aspecto a superar?", "No", "Sin práctica, no hay avance."), ex("¿Pedir ayuda es una estrategia?", "Sí", "Permite aprender con apoyo."), ex("¿Hay que mirar las consecuencias antes de elegir?", "Sí", "Ayuda a prever lo que pasa.")],
    task=T("Lee el caso de Sofía, una estudiante inventada: le cuesta ordenar sus tareas y varias veces llegó sin ellas. Opciones: A) no hacer nada; B) anotar en una hoja las tareas de la semana; C) pedirle al profesor una idea para organizarse; D) copiar la tarea de un compañero. Compara dos opciones. Para cada una escribe una consecuencia para Sofía y una para otras personas. Elige una y explica por qué.", "Comparo B y C. B: tendrá una lista; el curso no se atrasa por ella. C: recibirá una idea; el profesor sabrá cómo ayudar. Elijo B primero.", ["compara dos opciones", "escribe una consecuencia para Sofía y una para otros en cada una", "elige una y explica", "no elige copiar ni evitar sin motivo"], ["texto escrito o dicho", "cuadro de dos columnas"], ["elegir D (copiar)", "no escribir consecuencias"], "Reconoce las consecuencias y pregunta si la opción elegida es segura y posible."),
    reinforce="Escribe dos opciones para un aspecto a superar de un personaje y una consecuencia de cada una.",
    extend="Agrega una tercera opción al caso de Sofía y compárala con las otras.",
)

lesson(
    OA1, 4,
    "Una hoja y un lápiz. El plan de Camila está escrito en los ejercicios.",
    "Aprenderé a elegir una acción segura para mejorar algo que me cuesta: una meta pequeña, un plazo, apoyo y evidencia. Sirve para avanzar sin presión.",
    ["Sé comparar opciones y sus consecuencias.", "Sé que pedir ayuda es una estrategia."],
    [
        "Elegir una acción segura es escoger algo posible, que no me haga daño y que me ayude a avanzar. Un buen plan para superar un aspecto tiene cuatro partes. La meta debe ser pequeña y concreta. El plazo dice cuándo lo voy a revisar. El apoyo dice quién puede ayudarme. Y la evidencia dice cómo sabré que avancé.",
        "Una meta como «ser mejor en matemática» es muy grande. Una meta como «practicar 10 minutos de tablas cada día durante 5 días» se puede cumplir y comprobar. Si al final lograste 4 de los 5 días, avanzaste y puedes ajustar el plan. Un tropiezo no borra lo avanzado.",
        "Hay un cuidado más. Si el malestar con uno mismo es muy fuerte, dura mucho o te hace sentir sin ganas de nada, conviene contarlo a una persona adulta de confianza, como alguien de tu casa, un profesor o el orientador. Pedir ayuda así también es cuidarte.",
    ],
    [("meta", "lo que quiero lograr"), ("plazo", "tiempo en que reviso mi avance"), ("apoyo", "persona que puede ayudarme"), ("evidencia de avance", "algo que muestra cuánto progresé"), ("acción segura", "algo posible que no me daña y me ayuda a avanzar")],
    [
        W("Meta pequeña y concreta", "¿Cuál meta es mejor para empezar: «ser el mejor en matemática» o «practicar 10 minutos de tablas cada día, 5 días»?", ["La primera es enorme y no se puede comprobar.", "La segunda tiene minutos, días y se puede revisar.", "Una meta clara permite ver el avance."], "«Practicar 10 minutos de tablas cada día, 5 días»"),
        W("Medir el avance", "Camila se propuso practicar 5 días y practicó 4. ¿Cuántos días le faltaron para cumplir la meta?", ["La meta eran 5 días.", "Practicó 4 días.", "Se resta: 5 menos 4."], "Le faltó 1 día; avanzó y puede ajustar el plan"),
    ],
    [
        M("Ponerme una meta enorme para sentirme motivado.", "Una meta enorme se vuelve imposible y desanima.", "Elige una meta pequeña, con plazo y evidencia."),
        M("Guardar para mí un malestar muy grande sobre mí mismo.", "Se piensa que hay que resolverlo solo.", "Cuéntalo a una persona adulta de confianza: pedir ayuda cuida."),
    ],
    R=[
        ex("¿Una meta pequeña y concreta se puede comprobar al final?", "Sí", "Tiene días, minutos o cantidades que se revisan."),
        ex("En un plan, ¿el apoyo es la persona que puede ayudar o el tiempo para revisar?", "La persona que puede ayudar", "El plazo es el tiempo de revisión; el apoyo es quien acompaña."),
        ex("«Practicar 10 minutos cada día». ¿Es una meta concreta?", "Sí", "Dice cuánto y con qué frecuencia."),
    ],
    U=[
        ex("¿Por qué «ser la mejor en todo» es una mala meta para empezar?", "Es muy grande y no se puede comprobar", "No dice qué hacer ni cómo saber si avanzó."),
        ex("Camila no cumplió un día de su plan. ¿Eso borra lo que avanzó los otros días?", "No", "Un tropiezo no borra el avance; se ajusta el plan."),
        ex("¿Para qué sirve la evidencia de avance en un plan?", "Para saber si estoy progresando", "Muestra algo concreto que cambió."),
    ],
    A=[
        arith("Camila practica 10 minutos cada día durante 5 días. ¿Cuántos minutos practica en total?", "10*5", "Son 10 minutos repetidos en 5 días."),
        arith("Camila quería sumar 50 minutos de práctica y llegó a 40. ¿Cuántos minutos le faltaron?", "50-40", "Se resta lo logrado a lo que se propuso."),
        ex("Camila quiere mejorar su lectura en voz alta. ¿Qué plan tiene meta, plazo y apoyo: «Leer un párrafo de 6 líneas a una persona de mi casa cada tarde hasta el viernes» o «Leer más»?", "«Leer un párrafo de 6 líneas a una persona de mi casa cada tarde hasta el viernes»", "Dice cuánto, cuándo y con quién."),
    ],
    Z=[
        ex("Si Camila siente que «no sirve para nada» durante muchos días y se siente sin ganas, ¿qué conviene hacer?", "Contárselo a una persona adulta de confianza", "Un malestar fuerte y duradero necesita apoyo, no solo fuerza de voluntad."),
        ex("¿Por qué conviene revisar el plan al final del plazo?", "Para ver el avance y ajustar", "Sin revisión no sabes si funcionó."),
    ],
    D=[
        arith("En 4 semanas Camila practicó 5, 6, 8 y 9 veces. ¿Cuántas veces practicó en total?", "5+6+8+9", "Se suman las prácticas de cada semana."),
        arith("Camila se propuso 12 prácticas en 2 semanas. Hizo 5 la primera semana y 6 la segunda. ¿Cuántas le faltaron?", "12-5-6", "A la meta se le restan las dos semanas practicadas."),
    ],
    context=[ex("Un estudiante inventado quiere mejorar su ortografía. Su plan: «Escribir 5 palabras que me cuestan, cada día lunes a viernes, y revisarlas el viernes con el profesor». ¿Cuántas palabras escribirá en la semana?", "25", "Son 5 palabras por 5 días: 5 × 5 = 25.", calc="5*5")],
    selfcheck=[ex("En Orientación: ¿una meta debe ser pequeña y concreta?", "Sí", "Así puede cumplirse y comprobarse."), ex("¿Un plan necesita una forma de comprobar el avance?", "Sí", "La evidencia muestra cuánto progresé."), ex("¿Es bueno pedir ayuda si un malestar sobre mí es muy fuerte?", "Sí", "Una persona adulta de confianza puede apoyar.")],
    task=T("Elige un aspecto a superar de la lista: leer más rápido, ordenar mi mochila, hablar en voz más alta al exponer, terminar tareas a tiempo. Escribe un plan de una semana con cuatro partes: meta pequeña, plazo, apoyo y evidencia de avance. Usa solo cosas que puedas hacer con lo que hay en tu casa.", "Aspecto: ordenar mi mochila. Meta: sacar lo que no sirvo y dejar los útiles en su lugar, 5 minutos cada tarde. Plazo: viernes. Apoyo: una persona de mi casa mira el viernes. Evidencia: marco con una cruz cada día.", ["elige un aspecto de la lista", "meta pequeña y concreta", "plazo, apoyo y evidencia de avance", "no incluye información privada"], ["plan escrito o dibujado"], ["meta enorme", "plan sin forma de comprobar"], "Reconoce lo concreto del plan y pregunta cómo sabría que avanzó."),
    reinforce="Escribe una meta pequeña, un plazo, un apoyo y una evidencia para otro aspecto de la lista.",
    extend="Escribe cómo ajustarías el plan si solo cumples 3 de los 5 días.",
)

# ================================================================ OA 02
lesson(
    OA2, 1,
    "Una hoja y un lápiz. El caso de Sam y la lista de emociones están escritos en los ejercicios. Trabajas con personajes inventados.",
    "Aprenderé a distinguir y describir emociones, su intensidad y sus señales. Sirve para entender lo que siento y lo que sienten otros.",
    ["Sé que una emoción es lo que siento.", "Sé que lo que siento no siempre se ve desde afuera."],
    [
        "Una emoción es una reacción de tu cuerpo y tu mente ante algo que pasa. Algunas emociones son la alegría, la tristeza, la rabia, el miedo, la vergüenza y la frustración. Todas las emociones son normales. No son buenas ni malas: lo que importa es qué haces con ellas. Describir una emoción es decir cuál es, qué la provocó y cuánta intensidad tiene.",
        "La intensidad puede ser leve, media o fuerte. Sentir rabia leve es distinto de sentir rabia fuerte. El cuerpo da señales: el corazón late más rápido, las manos sudan, el estómago se aprieta, las mejillas se ponen calientes. A veces se sienten dos emociones a la vez, como alegría por la invitación y miedo por no conocer a nadie.",
        "Para describir bien una emoción, usa una frase como esta: «Me siento frustrado, con intensidad media, porque nadie me dejó participar». Así separas la emoción, su fuerza y su causa. Sam, un personaje inventado, quedó fuera de una decisión grupal. Puede sentir rabia, tristeza y vergüenza al mismo tiempo.",
    ],
    [("emoción", "reacción del cuerpo y la mente ante algo que pasa"), ("intensidad", "cuánta fuerza tiene una emoción"), ("señal del cuerpo", "cambio que se siente cuando hay una emoción"), ("frustración", "emoción cuando algo que queremos no resulta"), ("vergüenza", "emoción de sentirse expuesto o equivocado frente a otros")],
    [
        W("Describir una emoción", "Sam quedó fuera de una decisión grupal. Su corazón late rápido y siente que nadie lo escuchó. Describe su emoción.", ["Nombra la emoción: rabia o tristeza.", "Dices la causa: nadie lo escuchó.", "Dices una intensidad: media."], "Sam siente rabia o tristeza de intensidad media porque nadie lo escuchó"),
        W("Emociones mezcladas", "A Pía la invitaron a un cumpleaños donde no conoce a nadie. Siente alegría y también miedo. ¿Es posible sentir dos emociones a la vez?", ["Cada emoción tiene su causa.", "La alegría viene de la invitación.", "El miedo viene de no conocer a nadie."], "Sí, es posible sentir dos emociones a la vez"),
    ],
    [
        M("Pensar que hay emociones malas que no debería sentir.", "Se confunde la emoción con lo que se hace cuando se siente.", "Todas las emociones son normales; lo que importa es cómo las expreso."),
        M("Creer que si no se nota desde afuera, no estoy sintiendo nada.", "Muchas señales son internas.", "Fíjate también en el cuerpo y en lo que piensas."),
    ],
    R=[
        ex("«Corazón rápido y manos sudadas antes de exponer». ¿Son señales del cuerpo o causas?", "Señales del cuerpo", "Son cambios que se sienten cuando hay una emoción."),
        ex("«Me da rabia que no me dejen participar». ¿Qué emoción nombra?", "Rabia", "La palabra rabia dice la emoción."),
        ex("¿Las emociones son buenas o malas, o todas son normales?", "Todas son normales", "Lo que importa es qué hacemos con ellas."),
    ],
    U=[
        ex("¿Qué tres cosas dice una buena descripción de una emoción?", "La emoción, su intensidad y su causa", "Así se separa lo que siento, cuánto y por qué."),
        ex("¿Una persona puede sentir alegría y miedo a la vez? Responde sí o no.", "Sí", "Una situación puede tener partes que provocan emociones distintas."),
        ex("Sam siente rabia leve. Después de oír una burla siente rabia fuerte. ¿Qué cambió?", "La intensidad", "Es la misma emoción con más fuerza."),
    ],
    A=[
        ex("Lucía se equivocó al leer en voz alta delante del curso, siente las mejillas calientes y no quiere que la miren. ¿Qué emoción describe mejor lo que siente: vergüenza o rabia?", "Vergüenza", "Se sintió expuesta y no quiere que la miren; la causa fue equivocarse delante de otros."),
        ex("Un niño estudió mucho y el trabajo no salió como quería. Dice: «Me da mucha rabia que no resulte». ¿Qué emoción describe mejor: frustración o alegría?", "Frustración", "Es lo que sentimos cuando algo que queremos no resulta."),
        ex("Lista: 1) corazón rápido, 2) «es injusto», 3) manos sudadas, 4) estómago apretado. ¿Cuántas son señales del cuerpo?", "3", "Las señales 1, 3 y 4 son cambios del cuerpo; la 2 es un pensamiento."),
    ],
    Z=[
        ex("Dos niños sienten rabia por lo mismo. Uno dice «rabia leve» y el otro «rabia fuerte». ¿Pueden sentir lo mismo con distinta fuerza?", "Sí", "La intensidad puede variar entre personas y momentos."),
        ex("Si alguien dice «no sentí nada» pero tenía el corazón rápido antes de exponer, ¿qué podría estar pasando?", "Sentía una emoción como nervios que no nombró", "El cuerpo mostraba una emoción que no puso en palabras."),
    ],
    D=[
        arith("Una escala va de 1 (muy leve) a 5 (muy fuerte). Sam sintió rabia en nivel 4 y después bajó 2 niveles. ¿En qué nivel quedó?", "4-2", "Se restan los niveles que bajó."),
        arith("Tres compañeros calificaron su nerviosismo en la escala de 1 a 5 con 2, 3 y 4. ¿Cuántos niveles hay entre la calificación más alta y la más baja?", "4-2", "Se resta la calificación más baja a la más alta."),
    ],
    context=[ex("Mientras esperan los resultados de una votación, una niña inventada dice: «Estoy ansiosa y también tengo esperanza». ¿Cuántas emociones nombra?", "2", "Nombra ansiedad y esperanza.")],
    selfcheck=[ex("En Orientación: ¿una emoción tiene intensidad?", "Sí", "Puede ser leve, media o fuerte."), ex("¿Las emociones se sienten solo en la cabeza?", "No", "El cuerpo también da señales."), ex("¿Todas las emociones son normales?", "Sí", "Lo que importa es cómo las expreso.")],
    task=T("Lee: «Sam propuso una idea y el grupo ya había decidido sin escucharlo. Le late el corazón rápido y le queda un nudo en el estómago». Escribe una frase que describa su emoción con las tres partes: emoción, intensidad y causa. Escribe también dos señales del cuerpo que aparecen en el texto.", "Sam siente rabia de intensidad media porque el grupo decidió sin escucharlo. Señales: corazón rápido y nudo en el estómago.", ["nombra una emoción", "dice una intensidad", "dice la causa", "identifica dos señales del cuerpo"], ["frase escrita o dicha"], ["decir solo «mal» o «bien»", "confundir causa con señal"], "Reconoce la frase completa y pregunta qué otra emoción podría sentir Sam."),
    reinforce="Describe con emoción, intensidad y causa lo que sentiría un personaje de cuento ante un problema.",
    extend="Escribe dos emociones que Sam podría sentir al mismo tiempo y la causa de cada una.",
)

lesson(
    OA2, 2,
    "Una hoja y un lápiz. Los casos están escritos en los ejercicios.",
    "Aprenderé a separar lo que siento de lo que hago y a decir mi emoción con un mensaje «yo». Sirve para expresarme sin herir y poner un límite respetuoso.",
    ["Sé describir una emoción con intensidad y causa.", "Sé que todas las emociones son normales."],
    [
        "Sentir y actuar no son lo mismo. La emoción es lo que siento. La conducta es lo que hago por esa emoción: gritar, callar, empujar, explicar. La emoción no se elige, pero la conducta sí. Por eso puedes sentir rabia fuerte y decidir hablar con calma. Distinguir ambas cosas ayuda a expresar lo que sientes sin dañar a nadie.",
        "Un mensaje «yo» dice tres cosas: cuando pasa esto, me siento así, necesito esto otro. Por ejemplo: «Cuando decidieron sin preguntarme, me sentí ignorado. Necesito que me escuchen antes de decidir». El mensaje «yo» habla de ti y no acusa. Una frase como «tú nunca escuchas» acusa y casi siempre provoca defensa.",
        "También puedes poner un límite: decir qué no aceptas y qué sí. «No me gusta que me griten, pero puedo hablar si me hablas con calma». Un límite respetuoso cuida a ambas personas. Si alguien no respeta tu límite o te hace sentir inseguro, avisa a una persona adulta.",
    ],
    [("conducta", "lo que hago cuando siento una emoción"), ("mensaje «yo»", "frase que dice lo que me pasó, lo que siento y lo que necesito"), ("acusar", "culpar a otra persona sin escucharla"), ("límite", "lo que no acepto y lo que sí propongo"), ("calma", "estado tranquilo del cuerpo y la mente")],
    [
        W("Separar emoción y conducta", "Sam siente rabia y grita en el pasillo. ¿Cuál es la emoción y cuál la conducta?", ["La rabia es lo que siente.", "Gritar es lo que hace.", "La emoción se siente; la conducta se elige."], "Emoción: rabia. Conducta: gritar"),
        W("Reconocer las partes de un mensaje «yo»", "Mira el mensaje: «Cuando decidieron sin preguntarme, me sentí ignorado. Necesito que me escuchen antes de decidir». ¿Qué partes tiene?", ["Cuando… dice qué pasó.", "Me sentí… dice la emoción.", "Necesito… dice lo que pide."], "Tiene el hecho, la emoción y lo que necesita"),
    ],
    [
        M("Decir «tú siempre me haces enojar».", "Se acusa en vez de hablar de lo que uno siente.", "Usa «cuando…, me siento…, necesito…»."),
        M("Pensar que si siento rabia debo gritar.", "Se confunde emoción con conducta.", "La rabia se puede sentir y expresar con calma."),
    ],
    R=[
        ex("«Sentí rabia». ¿Es una emoción o una conducta?", "Una emoción", "Dice lo que se siente."),
        ex("«Le grité en el pasillo». ¿Es una emoción o una conducta?", "Una conducta", "Dice lo que se hizo."),
        ex("¿Un mensaje «yo» acusa o habla de lo que yo siento?", "Habla de lo que yo siento", "Evita culpar y dice lo que necesito."),
    ],
    U=[
        ex("¿Se puede elegir la emoción, la conducta o ambas?", "Solo la conducta", "La emoción aparece sola; la conducta se decide."),
        ex("¿Por qué «tú nunca escuchas» suele provocar defensa?", "Porque acusa sin escuchar", "La otra persona siente culpa y responde atacando."),
        ex("Un límite respetuoso, ¿dice qué no acepto y qué sí propongo? Responde sí o no.", "Sí", "Así cuida a ambos."),
    ],
    A=[
        ex("Completa el mensaje «yo»: «Cuando se rieron de mi respuesta, me sentí…, necesito que me respeten». ¿Qué emoción calza mejor: avergonzado o contento?", "Avergonzado", "La emoción nombra lo que se siente después de que se rieran de su respuesta."),
        ex("Cuál es un mensaje «yo»: «Cuando me interrumpen, me siento ignorada y necesito terminar mi idea» o «Siempre me interrumpes, eres insoportable»?", "«Cuando me interrumpen, me siento ignorada y necesito terminar mi idea»", "Habla de lo que ocurre, siente y necesita sin acusar."),
        ex("Tres frases: 1) «Me da miedo», 2) «Salí corriendo», 3) «Estoy triste». ¿Cuántas son emociones?", "2", "Las frases 1 y 3 nombran emociones; la 2 es una conducta."),
    ],
    Z=[
        ex("Una niña siente rabia fuerte. ¿Es mejor responder de inmediato o esperar un momento para decir lo que siente con calma?", "Esperar un momento", "Con calma se puede explicar sin herir."),
        ex("Si alguien no respeta un límite y te hace sentir inseguro, ¿con quién conviene hablar?", "Con una persona adulta de confianza", "No tienes que resolver solo una situación que te incomoda."),
    ],
    D=[
        arith("Tres mensajes «yo» tienen 3 partes cada uno. ¿Cuántas partes hay en total?", "3*3", "Se multiplica por 3 partes cada uno."),
        arith("De 12 frases, 5 acusan y el resto son mensajes «yo». ¿Cuántos mensajes «yo» hay?", "12-5", "Se restan las que acusan al total."),
    ],
    context=[ex("Dos niños inventados discuten porque uno tomó el borrador sin pedirlo. El afectado dice: «Cuando tomas mis cosas sin preguntar, me enojo; necesito que me pidas permiso». ¿Esa frase acusa?", "No", "Habla de lo que ocurre y lo que necesita, sin culpar a la persona.")],
    selfcheck=[ex("En Orientación: ¿la rabia es una emoción?", "Sí", "Es una emoción como cualquier otra."), ex("¿Gritar es una conducta?", "Sí", "Es lo que se hace, no lo que se siente."), ex("¿Un mensaje «yo» dice lo que necesito?", "Sí", "Incluye lo que pido.")],
    task=T("Lee: «Alex mostró a otros un dibujo tuyo sin pedirte permiso. Te da vergüenza y rabia». Escribe un mensaje «yo» con sus tres partes (cuando…, me siento…, necesito…) para decírselo a Alex con calma. Después escribe una conducta que NO usarías y por qué.", "Cuando mostraste mi dibujo sin permiso, me sentí avergonzado. Necesito que me preguntes antes. No gritaría porque lo asustaría y dejaría de escucharme.", ["usa el esquema cuando-me siento-necesito", "no acusa ni insulta", "propone una conducta que no usaría y la razón"], ["texto escrito o dicho"], ["acusar", "no decir lo que necesita"], "Reconoce el esquema y pregunta qué respuesta esperaría de Alex."),
    reinforce="Convierte «tú siempre me interrumpes» en un mensaje «yo».",
    extend="Escribe un límite respetuoso para alguien que te grita al hablarte.",
)

lesson(
    OA2, 3,
    "Una hoja y un lápiz. Los casos de Sam están escritos en los ejercicios.",
    "Aprenderé a comparar formas de expresar una emoción y a ver el impacto en mí y en los demás. Sirve para elegir cómo expresarme.",
    ["Sé separar emoción y conducta.", "Sé armar un mensaje «yo»."],
    [
        "Una misma emoción se puede expresar de varias formas. La rabia puede expresarse gritando, callándose todo, hablando con calma o escribiendo lo que sientes. Cada forma tiene un impacto: lo que provoca en ti y en las otras personas. Un impacto puede ser positivo, como entender y resolver, o negativo, como herir o quedarse con un malestar guardado.",
        "Gritar suele asustar o herir y la otra persona deja de escuchar. Callarse todo puede aliviar al principio, pero el malestar queda adentro y crece. Hablar con calma o usar un mensaje «yo» ayuda a que el otro entienda. Pedir un momento para calmarte también es una forma apropiada. Una forma apropiada de expresar es aquella que dice lo que sientes sin dañar a nadie ni a ti.",
        "Piensa en Sam, el personaje inventado que quedó fuera de la decisión del grupo. Puede gritar, callarse, escribir su emoción o decir un mensaje «yo». Antes de elegir, imagina cómo se sentirá él después y cómo se sentirán los demás.",
    ],
    [("impacto", "efecto que algo produce en mí y en otros"), ("expresar", "mostrar o decir lo que siento"), ("apropiado", "adecuado y respetuoso para la situación"), ("reprimir", "guardar una emoción sin decirla ni resolverla"), ("herir", "causar dolor a otra persona")],
    [
        W("Comparar dos formas", "Sam siente rabia. Compara: (a) gritar «¡todos son injustos!» y (b) decir «cuando decidieron sin mí, me sentí ignorado». ¿Cuál tiene mejor impacto?", ["(a) suele asustar y cierra la conversación.", "(b) dice lo que siente sin culpar.", "El impacto es mejor si el otro puede escuchar."], "(b), el mensaje «yo»"),
        W("Impacto en mí y en otros", "Sam se calla todo. Se siente aliviado hoy. ¿Qué probablemente pasa con su malestar?", ["Callar evita el conflicto hoy.", "El malestar sigue adentro.", "Después puede crecer."], "Probablemente se queda guardado y puede crecer"),
    ],
    [
        M("Pensar que callarlo todo es la mejor forma de expresar una emoción.", "Se confunde calma con ocultar.", "Busca decirlo con calma o con ayuda."),
        M("Creer que gritar sirve para que me escuchen.", "Se piensa que la fuerza convence.", "Gritar suele hacer que el otro deje de escuchar."),
    ],
    R=[
        ex("Gritar a un compañero, ¿suele ayudar a que te escuche o a que se asuste?", "A que se asuste", "La otra persona se defiende o se cierra."),
        ex("Hablar con calma, ¿es una forma apropiada de expresar rabia?", "Sí", "Dice lo que se siente sin dañar."),
        ex("Guardar todo el malestar, ¿se llama expresar o reprimir?", "Reprimir", "Es guardar la emoción sin decirla."),
    ],
    U=[
        ex("¿Qué es el impacto de una forma de expresar una emoción?", "El efecto en mí y en otras personas", "Es lo que provoca la forma de expresarse."),
        ex("¿Por qué un mensaje «yo» suele tener mejor impacto que insultar?", "Porque no ataca y el otro puede escuchar", "Se habla de lo que uno siente."),
        ex("Pedir «un momento para calmarme» antes de hablar, ¿es una forma apropiada?", "Sí", "Ayuda a expresarse con respeto."),
    ],
    A=[
        ex("Opciones de Sam: 1) gritar, 2) callarse todo, 3) escribir lo que siente y luego hablar, 4) decir un mensaje «yo». ¿Cuántas son formas apropiadas?", "2", "Escribir antes de hablar y usar un mensaje «yo» no dañan a nadie."),
        ex("Si Sam grita, ¿cuál es un impacto probable en los demás: se sienten escuchados o se asustan?", "Se asustan", "El volumen alto suele asustar o molestar."),
        ex("¿Cuál de estas formas suele herir a otros: gritar un insulto o usar un mensaje «yo»?", "Gritar un insulto", "El insulto ataca a la persona; el mensaje «yo» habla de lo que uno siente."),
    ],
    Z=[
        ex("Un niño dice: «Si grito, me hacen caso». ¿Cuál es el problema de esa estrategia a largo plazo?", "Los demás pueden temerle y dejar de escucharlo", "El miedo no construye confianza."),
        ex("¿Por qué a veces conviene esperar unos minutos antes de expresar una emoción muy fuerte?", "Porque con calma se expresa mejor", "La emoción baja de intensidad y se puede pensar."),
    ],
    D=[
        arith("En un curso, 8 estudiantes eligieron expresar su rabia con calma y 3 gritando. ¿Cuántos estudiantes respondieron?", "8+3", "Se suman ambos grupos."),
        arith("Sam pasó 6 minutos calmándose y 4 minutos conversando. ¿Cuántos minutos dedicó en total?", "6+4", "Se suman los dos tiempos."),
    ],
    context=[ex("Ana y Luz quieren el mismo balón en el recreo. Luz dice: «Cuando agarras el balón sin preguntar, me enojo; ¿lo turnamos?». ¿Qué forma de expresar usó Luz?", "Un mensaje «yo» con una propuesta", "Dijo qué hizo Ana, cómo se sintió y qué propone.")],
    selfcheck=[ex("En Orientación: ¿la forma de expresar una emoción tiene impacto en otros?", "Sí", "Afecta lo que sienten y hacen."), ex("¿Gritar suele ayudar a que me escuchen?", "No", "Suele asustar o molestar."), ex("¿Pedir un momento para calmarme es apropiado?", "Sí", "Permite expresarse con respeto.")],
    task=T("Sam quedó fuera de la decisión del grupo y siente rabia. Compara dos formas de expresarla: (a) gritar «¡todos son injustos!» y (b) decir «cuando decidieron sin mí, me sentí ignorado; necesito participar». Para cada una escribe el impacto en Sam y en el grupo. Elige una y di por qué.", "(a): Sam se desahoga, pero el grupo se asusta y no escucha. (b): Sam se siente escuchado y el grupo entiende. Elijo (b).", ["escribe impacto en Sam y en el grupo para cada forma", "elige una forma apropiada", "justifica con el impacto"], ["texto escrito o dicho", "cuadro de dos columnas"], ["no escribir el impacto en el grupo", "elegir una forma que hiere"], "Reconoce los impactos y pregunta qué otra forma apropiada podría usar Sam."),
    reinforce="Escribe tres formas de expresar tristeza y clasifica cuáles son apropiadas.",
    extend="Elige una emoción y escribe dos formas apropiadas de expresarla y el impacto de cada una.",
)

lesson(
    OA2, 4,
    "Una hoja y un lápiz. Las situaciones están escritas en los ejercicios.",
    "Aprenderé a elegir una acción segura cuando una emoción es muy fuerte: calmar el cuerpo, expresar con respeto y pedir ayuda. Sirve para cuidarme y cuidar a otros.",
    ["Sé comparar formas de expresar una emoción.", "Sé armar un mensaje «yo»."],
    [
        "Cuando una emoción es muy fuerte, primero hay que calmar el cuerpo. Un paso simple es detenerte y respirar. Inhala por la nariz contando hasta 4 y exhala despacio por la boca contando hasta 6. Repite cuatro veces. También puedes apretar y soltar los puños, tomar agua o pedir permiso para alejarte unos minutos del lugar.",
        "Luego, cuando estés más calmado, expresa con respeto: usa un mensaje «yo» y escucha la respuesta. Puedes seguir tres pasos: parar, pensar y actuar. Parar es detenerse. Pensar es preguntarte qué siento y qué necesito. Actuar es elegir una forma respetuosa de decirlo o de pedir ayuda.",
        "Hay emociones que necesitan apoyo de una persona adulta. Si una emoción dura muchos días, te cuesta dormir o comer, o te sientes sin ganas de nada, conviene contárselo a una persona adulta de confianza, como alguien de tu casa, tu profesor o el orientador. Pedir ayuda no es debilidad. Es una forma de cuidarte. Si alguna vez piensas en hacerte daño, díselo enseguida a una persona adulta de confianza.",
    ],
    [("calmar", "bajar la fuerza de una emoción"), ("respirar con calma", "inhalar y exhalar despacio"), ("parar-pensar-actuar", "tres pasos para elegir cómo responder"), ("apoyo", "ayuda de una persona de confianza"), ("seguro", "que no daña ni me pone en riesgo")],
    [
        W("Los tres pasos", "Alex siente rabia fuerte porque un compañero rompió su dibujo. ¿Qué paso va primero: parar, pensar o actuar?", ["Primero hay que detener la reacción.", "Luego se piensa qué siento.", "Por último se actúa con respeto."], "Parar"),
        W("Respirar contando", "Sam inhala 4 segundos y exhala 6 segundos, y repite 4 veces. ¿Cuántos segundos respira en total?", ["Cada vuelta dura 4 + 6 segundos.", "Cada vuelta dura 10 segundos.", "Cuatro vueltas son 40 segundos."], "40 segundos"),
    ],
    [
        M("Responder de inmediato cuando estoy muy enojado.", "Se piensa que esperar es perder.", "Primero para y respira; luego responde con calma."),
        M("Esconder una tristeza que dura muchos días.", "Se cree que debe pasar sola.", "Cuéntala a una persona adulta de confianza."),
    ],
    R=[
        ex("Cuando la emoción es muy fuerte, ¿primero respondes o primero calmas el cuerpo?", "Calmas el cuerpo", "Con calma se piensa mejor."),
        ex("«Parar, pensar, actuar». ¿Cuál paso es «detenerse»?", "Parar", "Detenerse evita reaccionar sin pensar."),
        ex("¿Respirar despacio ayuda a bajar la intensidad de una emoción?", "Sí", "Calma el cuerpo."),
    ],
    U=[
        ex("¿Por qué es mejor hablar cuando ya estás más calmado?", "Porque puedes expresarte con respeto", "Con calma se elige mejor qué decir."),
        ex("¿Qué dice el paso «pensar»?", "Qué siento y qué necesito", "Es ordenar lo que me pasa antes de actuar."),
        ex("Si una tristeza dura muchos días, ¿qué conviene hacer?", "Contárselo a una persona adulta de confianza", "Es una forma de cuidarse y de recibir apoyo."),
    ],
    A=[
        arith("Alex inhala 4 segundos y exhala 6, y repite 3 veces. ¿Cuántos segundos respira en total?", "(4+6)*3", "Cada vuelta dura 10 segundos y se repite 3 veces."),
        ex("Alex siente rabia fuerte en clase. ¿Cuál es una acción segura: salir corriendo del colegio sin avisar o pedir un momento para respirar?", "Pedir un momento para respirar", "Es seguro y le permite calmarse sin riesgo."),
        ex("Ordena los pasos: A) actuar con respeto, B) parar, C) pensar. Escribe las letras en orden.", "B, C, A", "Primero se para, luego se piensa y al final se actúa."),
    ],
    Z=[
        ex("Dos niños sienten rabia fuerte. Uno respira y luego habla. El otro grita de inmediato. ¿Cuál tiene más probabilidad de ser escuchado?", "El que respira y luego habla", "La calma facilita que el otro escuche."),
        ex("¿Por qué pedir ayuda a una persona adulta de confianza cuida a quien siente una emoción muy fuerte y duradera?", "Porque alguien puede orientarlo y acompañarlo", "No tiene que enfrentar solo algo que le pesa."),
    ],
    D=[
        arith("Sam respiró 4 vueltas de 10 segundos y después esperó 20 segundos en silencio. ¿Cuántos segundos pasaron en total?", "4*10+20", "Primero se calcula la respiración (40 segundos) y se suma la espera."),
        arith("Una escala de rabia va de 0 a 10. Alex estaba en 8 y bajó 3 puntos con la respiración. ¿En qué punto quedó?", "8-3", "Se restan los puntos que bajó."),
    ],
    context=[ex("En la fila, Ema siente rabia porque un niño la empujó sin querer. Ella piensa: «Paro, respiro, y le digo que me dolió». ¿Qué paso usó primero?", "Parar", "Lo primero fue detenerse antes de reaccionar.")],
    selfcheck=[ex("En Orientación: ¿se puede calmar el cuerpo respirando despacio?", "Sí", "Baja la intensidad de la emoción."), ex("¿Parar, pensar y actuar ayuda a responder mejor?", "Sí", "Da tiempo a elegir una conducta respetuosa."), ex("¿Es bueno pedir ayuda si una emoción dura muchos días?", "Sí", "Una persona adulta de confianza puede apoyar.")],
    task=T("Lee: «Alex recibe un comentario que lo hace sentir mal delante de todos. Siente rabia fuerte y quiere responder gritando». Escribe un plan de tres pasos (parar, pensar, actuar) para Alex. Incluye una acción para calmar el cuerpo, un mensaje «yo» y a quién puede acudir si el comentario se repite.", "Parar: respiro 4 veces. Pensar: siento rabia y vergüenza; necesito respeto. Actuar: «Cuando dices eso delante de todos, me siento mal; necesito que no lo repitas». Si se repite, aviso a mi profesor.", ["incluye parar, pensar y actuar", "una acción para calmar el cuerpo", "un mensaje «yo»", "nombra a una persona adulta de apoyo"], ["plan escrito o dibujado"], ["saltarse el paso de parar", "no nombrar apoyo"], "Reconoce los tres pasos y pregunta cómo sabrá Alex que se calmó."),
    reinforce="Escribe los tres pasos parar-pensar-actuar para una situación inventada de enojo.",
    extend="Diseña una señal discreta para pedir un momento de calma en clase.",
)
