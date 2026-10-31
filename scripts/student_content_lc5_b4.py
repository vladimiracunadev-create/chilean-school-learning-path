"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR01 (relatos fundacionales y expresiones culturalmente significativas en lengua indígena o castellano) y OA LR02
(diálogo cultural con vocabulario pertinente).

Criterio de autoría: las comunidades, las personas, los relatos y los diálogos de práctica son INVENTADOS, están en
castellano y se rotulan como tales; no pertenecen a ningún pueblo. Las «expresiones culturalmente significativas» que se
analizan son expresiones inventadas en castellano dentro de esos relatos; las únicas palabras en lengua indígena son las
ya atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke en mapuzugun; iorana, maururu en rapa nui),
siempre dentro de una ficha. No se explica el sentido espiritual de ninguna expresión de un pueblo real: el sentido de las
expresiones de práctica lo dan los testimonios inventados, y el de las reales lo enseñan el educador/a tradicional y la
comunidad. Cada tarea abierta remite a ellos.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LR1, LR2 = "LC05 OA LR01", "LC05 OA LR02"

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

FICHA_C = ("Ficha situada (inventada). Comunidad: Quebrada Verde (no es un pueblo real). Territorio: una quebrada con un río angosto y campos de cultivo. "
           "Fuente y responsable: doña Elsa, narradora de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Elsa autorizó usar el relato en la escuela. "
           "Límite: no se cuenta el nombre del lugar donde nace el río.")
FICHA_D = ("Ficha situada (inventada). Comunidad: Isla Niebla (no es un pueblo real). Territorio: una isla con acantilados, pasto y viento. "
           "Fuente y responsable: don Tomás, narrador de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: don Tomás autorizó usar el relato en la escuela. "
           "Límite: no se cuenta el nombre de la isla vecina.")
RELATO_C = ("Relato de práctica «Los dos hijos del río» (inventado): «Cuentan que al principio un solo río recorría la tierra seca. El río tuvo dos hijos: "
            "el Agua Mansa, que regaba los campos, y el Agua Brava, que limpiaba los caminos. Por eso, cuando alguien toma agua, debe dar las gracias.»")
RELATO_D = ("Relato de práctica «El primer canto» (inventado): «Antes de que existieran las personas, el viento no tenía voz. Una niña de piedra le prestó su canto "
            "y el viento aprendió a cantar. Desde entonces, cuando el viento canta en la isla, se recuerda que el mundo se hizo prestándose cosas unos a otros.»")
TESTIMONIO_C = ("Testimonio inventado de doña Elsa: «Cuando decimos Agua Mansa y Agua Brava, recordamos que el agua cuida los campos y también limpia lo que sobra. "
                "Por eso agradecemos antes de tomar agua.»")
FICHA_PAL = ("Ficha de palabras (de práctica): en mapuzugun «ko» es agua, «mapu» es tierra, «antü» es sol, «kuyen» es luna, «ruka» es casa y «ñuke» es madre. "
             "«mari mari» es un saludo y «chaltumay» es «gracias» en mapuzugun. «iorana» es un saludo y «maururu» es «gracias» en rapa nui.")

# ============================================================ OA LR01 · relatos fundacionales y expresiones significativas
L(
    LR1, 1,
    materials=MAT,
    use="Aprenderé a situar un relato fundacional y a reconocer las expresiones culturalmente significativas que trae. Sirve para entender por qué algunas palabras de un relato importan tanto a la comunidad que lo cuenta.",
    prior=["Sé situar un relato con una ficha de seis datos.", "Sé que un relato fundacional explica cómo empezó el mundo o un lugar."],
    explain=[
        "Un relato fundacional puede contarse en una lengua indígena o en castellano. En cualquiera de las dos, algunas palabras y frases guardan un sentido especial para la comunidad. Las llamamos expresiones culturalmente significativas. Por ejemplo, en un relato inventado de Quebrada Verde aparecen «Agua Mansa» y «Agua Brava», que son nombres con los que la comunidad de práctica recuerda al agua.",
        "Antes de analizar las expresiones, situamos el relato con su ficha: comunidad, territorio, fuente y responsable, fecha, permiso y límite. Así sabemos de quién es el relato, quién lo cuenta y qué parte no se cuenta fuera de la comunidad. Una expresión no se entiende bien sin saber quién la dice y en qué lugar.",
        "Para encontrar una expresión significativa buscamos palabras o frases que se repiten, que nombran algo muy importante o que son nombres propios dentro del relato. El sentido completo de la expresión lo explica la comunidad que la usa. Nosotros la identificamos, la anotamos y preguntamos. No inventamos qué significa.",
    ],
    vocab=[("expresión culturalmente significativa", "palabra o frase con sentido especial para la comunidad"), ("relato fundacional", "historia que explica cómo empezó el mundo o un lugar"), ("fuente", "persona de quien viene el relato"), ("nombre propio", "nombre con que se llama a alguien o algo único"), ("sentido", "lo que algo quiere decir o representa")],
    worked=[
        W("Situar el relato", FICHA_C + " ¿Quién cuenta el relato y de qué comunidad es?", ["Busco «Fuente y responsable» y «Comunidad».", "Doña Elsa, de Quebrada Verde."], "Doña Elsa, de la comunidad Quebrada Verde."),
        W("Encontrar expresiones", RELATO_C + " Anota dos nombres propios del relato.", ["Busco nombres con mayúscula en medio de la frase.", "Aparecen Agua Mansa y Agua Brava."], "Agua Mansa y Agua Brava."),
    ],
    mistakes=[
        M("Explicar el significado de una expresión sin que la comunidad lo haya dicho.", "Invento un sentido.", "Anoto la expresión y pregunto."),
        M("Analizar un relato sin saber quién lo cuenta.", "No se sabe a quién atribuir lo que significa.", "Leo primero la ficha."),
    ],
    R=[
        ex(FICHA_C + " ¿Quién es la fuente y responsable del relato?", "Doña Elsa", "La ficha la nombra."),
        ex(RELATO_C + " ¿Cómo se llama el hijo del río que regaba los campos?", "Agua Mansa", "El relato lo dice así."),
        ex(RELATO_C + " ¿Cómo se llama el hijo del río que limpiaba los caminos?", "Agua Brava", "El relato lo dice así."),
    ],
    C=[
        ex("Una expresión culturalmente significativa es: A) una palabra o frase con sentido especial para la comunidad B) una palabra muy larga", "A", "Guarda un sentido para quienes la usan."),
        ex("Verdadero o falso: el sentido completo de una expresión lo explica la comunidad que la usa.", "Verdadero", "Ella conoce su valor."),
        ex(FICHA_C + " ¿Qué dato de la ficha dice qué no se cuenta fuera de la comunidad: el permiso o el límite?", "El límite", "El límite señala lo reservado."),
    ],
    A=[
        ex("Une cada expresión del relato con lo que hacía. 1) Agua Mansa 2) Agua Brava. a) limpiaba los caminos b) regaba los campos", "1-b, 2-a", "El relato lo cuenta así."),
        ex(RELATO_C + " ¿Qué debe hacer alguien cuando toma agua según el relato?", "Dar las gracias", "La última frase lo dice."),
        ex(FICHA_C + " ¿Puedes escribir el nombre del lugar donde nace el río? Responde Sí o No.", "No", "El límite lo reserva."),
    ],
    Z=[
        ex("Luis dice: «Agua Brava quiere decir que el agua es peligrosa». ¿Está en el relato? Responde Sí o No.", "No", "El relato dice que limpiaba los caminos."),
        ex("Rosa dice: «Como el relato de Quebrada Verde usa nombres de agua, todos los pueblos nombran así al agua». ¿Qué error comete?", "Generaliza un relato a todos los pueblos", "Una ficha habla de una comunidad."),
    ],
    D=[
        ex("Dos lectores. L1: «Agua Mansa es el nombre de uno de los hijos del río en el relato». L2: «Agua Mansa es un nombre sagrado de todos los pueblos». ¿Cuál se mantiene en el texto?", "L1", "L2 agrega un sentido que el relato no da."),
        ex("Si no hay ficha ni permiso del relato, ¿qué haces? A) me detengo y pregunto al educador tradicional B) lo analizo igual", "A", "Sin ficha y permiso no se usa."),
    ],
    context=[ex("Una vecina cuenta un relato con nombres propios que tu curso no conoce. Un compañero explica enseguida qué significan. ¿Qué le dices? A) que le pregunte a la vecina qué significan B) que está muy bien explicado", "A", "El sentido lo da la comunidad.")],
    selfcheck=[
        ex("Nombra dos datos de la ficha situada.", "Dos entre: comunidad, territorio, fuente, fecha, permiso, límite", "Son datos de la ficha."),
        ex("Verdadero o falso: puedo inventar el significado de una expresión si no lo sé.", "Falso", "Se pregunta a la comunidad."),
        ex(RELATO_C + " ¿Qué hacía el río al principio: recorría la tierra seca o dormía bajo el hielo?", "Recorría la tierra seca", "Así comienza el relato."),
    ],
    task=T("Lee la ficha y el relato de práctica: «" + FICHA_D + "» «" + RELATO_D.split("«", 2)[2].rstrip("»") + "» Haz una tabla de tres columnas: «Datos de la ficha» (comunidad, fuente, permiso, límite), «Expresiones que aparecen» (al menos dos, por ejemplo «niña de piedra») y «Lo que no sé de ellas». Escribe una pregunta para el educador tradicional sobre cómo se cuentan los relatos en tu zona.",
           "Datos: Isla Niebla; don Tomás; permiso sí; límite el nombre de la isla vecina. Expresiones: niña de piedra; prestar el canto. Lo que no sé: qué significan para la comunidad. Pregunta: ¿cómo se cuentan los relatos de origen en nuestra zona?",
           ["completa la ficha", "identifica expresiones del relato", "declara lo que no sabe"], ["tabla de tres columnas", "pregunta escrita"], ["inventar significados", "escribir el nombre reservado"],
           "Pedir que señale cada expresión en el relato; valorar que no explique su sentido."),
    reinforce="Copia el relato «Los dos hijos del río» y subraya las expresiones con un color.",
    extend="Escribe una expresión inventada de tu cuaderno que podría tener un sentido especial para una comunidad y qué le preguntarías.",
)

L(
    LR1, 2,
    materials=MAT,
    use="Aprenderé a leer un relato fundacional comprendiendo qué cuenta y declarando sus límites, y a distinguir lo que dicen las expresiones de lo que yo imagino. Sirve para no confundir el relato con mis suposiciones.",
    prior=["Sé situar un relato y encontrar sus expresiones significativas.", "Sé que el sentido de una expresión lo da la comunidad."],
    explain=[
        "Comprender un relato es saber qué ocurre, en qué orden y con quiénes. En «Los dos hijos del río», primero hay un solo río en la tierra seca, luego nacen dos hijos con tareas distintas y al final se explica por qué se da las gracias al tomar agua. Si cambiamos el orden, la explicación pierde sentido.",
        "Leer con límites es decir qué dice el relato, qué no dice y qué se reserva. El relato dice que el Agua Brava limpiaba los caminos; no dice si era peligrosa ni si la comunidad le tiene temor. Eso no lo completamos. Tampoco decimos el nombre del lugar donde nace el río, porque la ficha lo reserva.",
        "Una expresión significativa se lee primero de manera literal: qué dice la frase. Después preguntamos qué sentido le da la comunidad, y si ella no lo explicó, escribimos «no lo sé». Así separamos lo literal de lo interpretado y no ponemos en boca de nadie lo que no dijo.",
    ],
    vocab=[("literal", "lo que la frase dice tal cual"), ("interpretar", "explicar qué sentido tiene algo"), ("orden de los hechos", "qué pasa primero, después y al final"), ("límite declarado", "lo que se avisa que no se cuenta"), ("completar", "agregar lo que el texto no dijo")],
    worked=[
        W("Lo literal", RELATO_C + " ¿Qué dice literalmente sobre el Agua Brava?", ["Busco la frase del Agua Brava.", "Dice que limpiaba los caminos."], "Que limpiaba los caminos."),
        W("Lo que no se dice", RELATO_C + " ¿Dice el relato si la comunidad le teme al Agua Brava?", ["Reviso el relato.", "No lo menciona."], "No, el relato no lo dice."),
    ],
    mistakes=[
        M("Mezclar lo literal con lo que imagino.", "Pongo en el relato algo que no dice.", "Separo «el relato dice» de «yo pienso»."),
        M("Cambiar el orden de lo que ocurre.", "Cambia la explicación.", "Reviso la secuencia."),
    ],
    R=[
        ex(RELATO_C + " ¿Qué recorría la tierra seca al principio?", "Un solo río", "El relato comienza así."),
        ex(RELATO_C + " ¿Cuántos hijos tuvo el río?", "Dos", "Agua Mansa y Agua Brava."),
        ex(RELATO_C + " ¿Qué regaba el Agua Mansa?", "Los campos", "El relato lo dice."),
    ],
    C=[
        ex(RELATO_C + " Verdadero o falso: el relato dice que el Agua Brava era peligrosa.", "Falso", "Dice que limpiaba los caminos."),
        ex("¿Qué significa leer una frase de manera literal? A) leer lo que dice tal cual B) imaginar lo que querría decir", "A", "Literal es lo que dice la frase."),
        ex(RELATO_C + " ¿Qué se explica al final del relato: por qué se da las gracias al tomar agua o por qué hay montañas?", "Por qué se da las gracias al tomar agua", "Es la última frase."),
    ],
    A=[
        ex(RELATO_C + " Ordena: a) el río tuvo dos hijos b) se explica que se da las gracias c) un solo río recorría la tierra seca. Escribe las letras.", "c, a, b", "El relato sigue ese orden."),
        ex(RELATO_C + " ¿Cuál afirmación está en el relato? A) el Agua Mansa regaba los campos B) el Agua Mansa se secó", "A", "La B no aparece."),
        ex("La ficha de Quebrada Verde reserva el nombre del lugar donde nace el río. Alguien pregunta cómo se llama. ¿Qué respuesta respeta el límite? A) «Ese dato no se cuenta fuera de la comunidad» B) «Seguro se llama Cerro Alto»", "A", "La B inventa un nombre."),
    ],
    Z=[
        ex("Tomás dice: «El Agua Brava seguramente asustaba a la comunidad». ¿Se puede afirmar eso con el relato? Responde Sí o No.", "No", "El relato no habla de temor."),
        ex("Ana dice que el relato explica el origen de todos los ríos de Chile. ¿Qué error comete? A) generaliza B) tiene razón", "A", "El relato es de una comunidad."),
    ],
    D=[
        ex("Dos resúmenes. R1: «El río tuvo dos hijos con tareas distintas». R2: «El río tuvo dos hijos que pelearon». ¿Cuál es fiel al relato?", "R1", "R2 agrega una pelea."),
        ex("Una frase literal y otra interpretada. L: «El Agua Brava limpiaba los caminos». I: «El Agua Brava castiga a quien ensucia». ¿Cuál es literal?", "L", "La otra agrega un sentido."),
    ],
    context=[ex("Un compañero dice que sabe lo que significa «Agua Brava» para la comunidad, pero nadie se lo contó. ¿Qué le propones? A) preguntar a doña Elsa o a una persona de la comunidad B) creerle", "A", "Solo la comunidad explica el sentido.")],
    selfcheck=[
        ex("Nombra las tres cosas que se declaran al leer con límites.", "Lo que el relato dice, lo que no dice y lo que se reserva", "Son los límites de la lectura."),
        ex("Verdadero o falso: puedo completar con mi imaginación lo que el relato no dice.", "Falso", "Se avisa que no lo dice."),
        ex(RELATO_C + " ¿Qué hacía el Agua Brava?", "Limpiaba los caminos", "Lo dice el relato."),
    ],
    task=T("Lee otra vez el relato: «" + RELATO_C.split("«", 2)[2].rstrip("»") + "» Haz una tabla de tres columnas: «El relato dice» (tres datos), «El relato no dice» (dos datos) y «Frase literal / frase interpretada» (una de cada una sobre el Agua Mansa). Escribe una pregunta que le harías a doña Elsa sobre el sentido de una expresión.",
           "Dice: un solo río recorría la tierra seca; tuvo dos hijos; hay que dar las gracias al tomar agua. No dice: dónde nace el río; si alguien teme al Agua Brava. Literal: el Agua Mansa regaba los campos. Interpretada (mía): el Agua Mansa cuida los cultivos. Pregunta: ¿qué significa para ustedes llamar «Mansa» al agua que riega?",
           ["registra datos del relato", "distingue lo que no dice", "separa lo literal de lo interpretado"], ["tabla de tres columnas", "pregunta escrita"], ["agregar datos", "presentar la interpretación como si fuera del relato"],
           "Pedir que señale en el relato cada dato; valorar que rotule la interpretación como propia."),
    reinforce="Escribe en orden los tres momentos del relato «Los dos hijos del río».",
    extend="Escribe dos preguntas que el relato no responde y cómo las harías con respeto.",
)

L(
    LR1, 3,
    materials=MAT + " " + FICHA_PAL,
    use="Aprenderé a relacionar las expresiones de un relato con la importancia que tiene para la comunidad, usando un testimonio. Sirve para explicar por qué un relato importa sin inventar su significado.",
    prior=["Sé leer un relato con límites y encontrar sus expresiones.", "Sé usar «según» para atribuir."],
    explain=[
        "Las expresiones de un relato se relacionan con la manera de vivir de la comunidad. Para ver esa relación necesitamos un testimonio: lo que una persona de la comunidad cuenta sobre cómo vive el relato. En el testimonio inventado de doña Elsa, «Agua Mansa» y «Agua Brava» recuerdan que el agua cuida los campos y también limpia; por eso se agradece antes de tomar agua.",
        "Relacionar es unir tres datos: la expresión del relato, lo que dice el testimonio y lo que la comunidad hace. Así vemos que el relato no es solo una historia: orienta cómo se cuida el agua. Pero esto lo sabemos porque doña Elsa lo dijo, no porque nosotros lo supongamos. Siempre escribimos «según doña Elsa».",
        "A veces las expresiones están en lengua indígena. En la ficha de palabras, «chaltumay» es «gracias» en mapuzugun y «ko» es agua. Que existan esas palabras no significa que el relato de Quebrada Verde sea de ese pueblo: es un relato inventado. Pero nos muestra que agradecer y nombrar el agua son temas que se pueden decir en lengua indígena.",
    ],
    vocab=[("testimonio", "relato de una persona sobre lo que vive o sabe"), ("relacionar", "unir dos datos para ver cómo se conectan"), ("orientar", "mostrar cómo actuar"), ("agradecer", "dar las gracias"), ("según", "palabra que indica de quién viene una idea")],
    worked=[
        W("Relacionar con un testimonio", TESTIMONIO_C + " ¿Qué relación hay entre «Agua Brava» y lo que hace la comunidad?", ["El testimonio dice que el agua limpia lo que sobra.", "Por eso agradecen antes de tomar agua."], "Según doña Elsa, el agua que limpia es parte de por qué se agradece el agua."),
        W("No inventar", "Alguien agrega: «Y por eso hacen una fiesta del agua». ¿Está en el testimonio?", ["Reviso el testimonio.", "No menciona fiestas."], "No: eso no lo dice el testimonio."),
    ],
    mistakes=[
        M("Relacionar la expresión con una creencia que nadie dijo.", "Invento un significado.", "Uso solo lo que dice el testimonio."),
        M("Creer que una palabra de la ficha de palabras prueba que el relato es de ese pueblo.", "El relato es inventado.", "Aclaro que son cosas distintas."),
    ],
    R=[
        ex(TESTIMONIO_C + " ¿Qué se hace antes de tomar agua según doña Elsa?", "Se agradece", "El testimonio lo dice."),
        ex(TESTIMONIO_C + " ¿Qué recuerdan las expresiones Agua Mansa y Agua Brava según doña Elsa?", "Que el agua cuida los campos y también limpia", "Así lo dice el testimonio."),
        ex(FICHA_PAL + " ¿Qué es «chaltumay» en mapuzugun?", "Gracias", "La ficha de palabras lo indica."),
    ],
    C=[
        ex("Verdadero o falso: para ver cómo vive la comunidad un relato necesito un testimonio.", "Verdadero", "El testimonio lo cuenta quien lo vive."),
        ex("¿Con qué palabras atribuyo una relación a la fuente? A) “según doña Elsa” B) “seguramente”", "A", "Nombra a quien lo dijo."),
        ex("Verdadero o falso: la palabra «ko» prueba que el relato de Quebrada Verde es de un pueblo real.", "Falso", "El relato es inventado."),
    ],
    A=[
        ex(TESTIMONIO_C + " Une la expresión con lo que recuerda. 1) Agua Mansa 2) Agua Brava. a) que el agua limpia lo que sobra b) que el agua cuida los campos", "1-b, 2-a", "Según doña Elsa, la mansa cuida y la brava limpia."),
        ex(TESTIMONIO_C + " Escribe una frase que empiece con «Según doña Elsa…» y relacione el relato con agradecer.", "Según doña Elsa, se agradece antes de tomar agua", "La frase atribuye la relación."),
        ex(FICHA_PAL + " ¿Qué dos palabras de la ficha están relacionadas con el agua y el agradecimiento: «ko» y «chaltumay» o «antü» y «kuyen»?", "ko y chaltumay", "Son agua y gracias."),
    ],
    Z=[
        ex("Pablo dice: «Según doña Elsa, hacen una fiesta del agua». ¿Qué error comete?", "Atribuye a doña Elsa algo que no dijo", "El testimonio no habla de fiestas."),
        ex("Una niña dice: «Si agradecen el agua, entonces el agua es sagrada para ellos». ¿Qué falta? A) que doña Elsa lo diga B) nada", "A", "Lo sagrado lo dice la comunidad."),
    ],
    D=[
        ex("Elige la relación bien atribuida: A) «Según doña Elsa, las expresiones recuerdan que el agua cuida y limpia» B) «Las expresiones muestran que el agua es una diosa»", "A", "La B inventa un significado."),
        ex("Si el testimonio no explica una expresión, ¿qué escribes? A) «El testimonio no lo explica» B) una explicación probable", "A", "Se declara el límite."),
    ],
    context=[ex("Para una exposición quieres explicar por qué un relato importa a una comunidad, pero el testimonio solo habla de una expresión. ¿Qué haces con las demás? A) las dejo como preguntas B) invento su significado", "A", "No se inventa.")],
    selfcheck=[
        ex("Nombra los tres datos que se unen al relacionar.", "La expresión, el testimonio y lo que hace la comunidad", "Son los tres datos de la clase."),
        ex("Verdadero o falso: puedo escribir «según doña Elsa» aunque ella no lo haya dicho.", "Falso", "Eso es atribuir falsamente."),
        ex(FICHA_PAL + " ¿Qué significa «mapu»?", "Tierra", "La ficha de palabras lo indica."),
    ],
    task=T("Lee el testimonio de práctica de don Tomás, de Isla Niebla: «En la isla, cuando el viento canta, les contamos a los niños el relato de la niña de piedra.» Haz una tabla con tres columnas: «Expresión del relato» (niña de piedra, prestar el canto), «Qué dice el testimonio» y «Qué no dice». Escribe una frase con «Según don Tomás…» y otra con «Yo pienso…». No expliques significados que el testimonio no da.",
           "Expresión: niña de piedra. Testimonio: cuando el viento canta se cuenta el relato a los niños. No dice: qué significa la niña de piedra. Según don Tomás, cuando el viento canta en la isla se cuenta a los niños el relato de la niña de piedra. Yo pienso que es una forma de enseñar el relato.",
           ["relaciona expresión y testimonio", "atribuye a la fuente", "no inventa significados"], ["tabla de tres columnas", "dos frases rotuladas"], ["inventar ceremonias", "atribuir a don Tomás lo que no dijo"],
           "Pedir que señale la frase del testimonio; valorar que declare lo que no se dice."),
    reinforce="Dibuja el relato «Los dos hijos del río» en tres cuadros y escribe debajo la expresión de cada uno.",
    extend="Explica con tus palabras por qué una palabra en lengua indígena no prueba que un relato sea de ese pueblo.",
)

L(
    LR1, 4,
    materials=MAT,
    use="Aprenderé a construir una respuesta atribuida que explique la importancia de un relato fundacional a partir de sus expresiones. Sirve para responder con claridad, con la fuente y sin generalizar.",
    prior=["Sé relacionar las expresiones de un relato con un testimonio.", "Sé separar lo literal de lo interpretado."],
    explain=[
        "Para explicar la importancia de un relato para el pueblo al que pertenece, armamos una respuesta con cinco partes. Primero, la fuente: «Según doña Elsa, de Quebrada Verde…». Segundo, la expresión elegida: «la expresión Agua Mansa…». Tercero, lo que significa para la comunidad según el testimonio. Cuarto, un dato del relato que lo apoya. Quinto, un límite: lo que no sabemos.",
        "Una respuesta atribuida no usa «todos», «siempre» ni «los pueblos indígenas». Habla de una comunidad y de una persona concreta. Si la fuente no explicó algo, lo decimos: «El testimonio no explica por qué…». Y si damos una opinión, la separamos con «Yo pienso…». Así quien lee sabe qué viene de la comunidad y qué viene de nosotros.",
        "Escribir con respeto también es revisar el lenguaje. Evitamos palabras como «leyenda» o «mito» como si el relato no fuera verdad para la comunidad. Usamos «relato» o «relato fundacional». Y no comparamos con otros pueblos. Si queremos usar una expresión en lengua indígena, la tomamos de una ficha o la preguntamos al educador tradicional.",
    ],
    vocab=[("respuesta atribuida", "respuesta que dice de dónde viene cada dato"), ("importancia", "lo valioso que algo es para alguien"), ("apoyar", "mostrar un dato que respalda lo que afirmo"), ("límite", "aclaración de lo que no se sabe o no vale"), ("revisar el lenguaje", "comprobar que las palabras no juzgan ni generalizan")],
    worked=[
        W("Armar la respuesta", RELATO_C + " " + TESTIMONIO_C + " Pregunta: ¿por qué importa este relato para Quebrada Verde?", ["Fuente: doña Elsa.", "Expresión: Agua Mansa y Agua Brava.", "Significado según el testimonio: recuerdan que el agua cuida y limpia.", "Apoyo del relato: se debe dar las gracias al tomar agua."], "Según doña Elsa, las expresiones Agua Mansa y Agua Brava recuerdan que el agua cuida los campos y limpia; por eso en el relato se debe dar las gracias al tomar agua."),
        W("Corregir el lenguaje", "Frase: «Esa leyenda de los pueblos indígenas es solo un cuento». ¿Qué corriges?", ["«Leyenda» y «solo un cuento» restan valor.", "«Los pueblos indígenas» generaliza."], "«Este relato de Quebrada Verde, según doña Elsa…»."),
    ],
    mistakes=[
        M("Usar «leyenda» o «cuento» como si el relato no fuera verdad para la comunidad.", "Resta valor.", "Escribo «relato fundacional»."),
        M("Afirmar el significado de una expresión sin testimonio.", "Invento un sentido.", "Escribo «el testimonio no explica»."),
    ],
    R=[
        ex("Completa: «Según ___, las expresiones recuerdan que el agua cuida y limpia».", "doña Elsa", "Es la fuente del testimonio."),
        ex("Un relato fundacional se llama: A) relato fundacional B) solo un cuento", "A", "Se evita restar valor."),
        ex(RELATO_C + " ¿Qué dato del relato apoya que hay que agradecer el agua?", "Por eso, cuando alguien toma agua, debe dar las gracias", "Es la frase final."),
    ],
    C=[
        ex("Verdadero o falso: puedo usar «los pueblos indígenas» para hablar de lo que cuenta doña Elsa.", "Falso", "Ella habla de su comunidad."),
        ex("Las cinco partes son fuente, expresión, significado según el testimonio, apoyo del relato y… A) límite B) chiste", "A", "El límite declara lo que no sabemos."),
        ex("Verdadero o falso: «leyenda» es una palabra neutra para el relato de una comunidad.", "Falso", "Puede restarle valor."),
    ],
    A=[
        ex("Ordena para armar la respuesta: a) El testimonio no explica el lugar donde nace el río b) Según doña Elsa c) la expresión Agua Mansa recuerda que el agua cuida los campos. Escribe las letras.", "b, c, a", "Fuente, significado y límite."),
        ex(TESTIMONIO_C + " Elige la respuesta atribuida: A) «Según doña Elsa, se agradece antes de tomar agua» B) «Se agradece el agua en todo el país»", "A", "La B generaliza."),
        ex(RELATO_D + " " + "Completa: «Según el relato que cuenta don Tomás, la niña de piedra le prestó su ___ al viento».", "canto", "El relato lo dice."),
    ],
    Z=[
        ex("Camila escribe: «Según doña Elsa, el Agua Brava es un espíritu». ¿Qué error comete?", "Atribuye algo que doña Elsa no dijo", "El testimonio no habla de espíritus."),
        ex("Rafael escribe: «Yo pienso que el relato enseña a cuidar el agua». ¿Es una frase correcta si está marcada como opinión? Responde Sí o No.", "Sí", "Está separada de la fuente."),
    ],
    D=[
        ex("Dos respuestas. R1: «Según doña Elsa, Agua Mansa recuerda que el agua cuida los campos». R2: «Los pueblos creen que Agua Mansa es buena». ¿Cuál cumple las reglas?", "R1", "La R2 generaliza y no atribuye."),
        ex("El testimonio no explica una expresión que quieres usar. ¿Qué escribes? A) «El testimonio no lo explica; preguntaré» B) un significado probable", "A", "Se declara el límite."),
    ],
    context=[ex("En un trabajo te piden explicar la importancia de un relato fundacional y solo tienes el relato, sin testimonio. ¿Qué haces? A) explico lo que dice el relato y anoto que falta el testimonio B) invento lo que significa", "A", "Se declara lo que falta.")],
    selfcheck=[
        ex("Nombra las cinco partes de la respuesta.", "Fuente, expresión, significado según el testimonio, apoyo del relato y límite", "Son las partes de la clase."),
        ex("Verdadero o falso: puedo usar «leyenda» para restar valor a un relato.", "Falso", "Se usa «relato»."),
        ex("¿Con qué palabras separo mi opinión? A) “Yo pienso” B) “según”", "A", "Marca la voz propia."),
    ],
    task=T("Responde por escrito: «¿Por qué es importante el relato “El primer canto” para Isla Niebla?». Usa el relato: «" + RELATO_D.split("«", 2)[2].rstrip("»") + "» y el testimonio de don Tomás: «En la isla, cuando el viento canta, les contamos a los niños el relato de la niña de piedra.» Tu respuesta debe tener fuente, expresión, significado según el testimonio, un dato del relato y un límite («El testimonio no explica…»). Añade una frase con «Yo pienso…».",
           "Según don Tomás, de Isla Niebla, cuando el viento canta se cuenta a los niños el relato de la niña de piedra. El relato dice que ella le prestó su canto al viento. El testimonio no explica por qué se cuenta justo cuando el viento canta. Yo pienso que es una forma de enseñar el relato.",
           ["incluye las cinco partes", "atribuye a la fuente", "evita generalizar y restar valor"], ["respuesta de cinco frases"], ["inventar significados", "usar «leyenda»"],
           "Pedir que subraye cada parte; valorar el límite declarado."),
    reinforce="Reescribe sin restar valor: «Esa leyenda es un cuento de los indígenas».",
    extend="Escribe una respuesta atribuida sobre «Los dos hijos del río» con las cinco partes.",
)

L(
    LR1, 5,
    materials=MAT,
    use="Aprenderé a comparar dos relatos fundacionales y sus expresiones sin decir que uno es mejor. Sirve para respetar las distintas maneras de explicar el origen del mundo.",
    prior=["Sé responder con una respuesta atribuida.", "Sé que contrastar es distinto de jerarquizar."],
    explain=[
        "Contrastar relatos es ver en qué se parecen y en qué se diferencian. En «Los dos hijos del río» el protagonista es el agua y se enseña a agradecer; en «El primer canto» es el viento y se recuerda que el mundo se hizo prestándose cosas. Ambos explican cómo comenzó algo en su territorio, pero lo hacen con elementos distintos.",
        "Para contrastar usamos criterios neutros: qué elemento del territorio protagoniza, qué expresiones aparecen, qué se recuerda al final y quién cuenta. Armamos una tabla y escribimos una semejanza y una diferencia con evidencia. No decimos que el relato del agua sea mejor que el del viento ni que uno sea más antiguo.",
        "También evitamos concluir que un relato representa a todo un pueblo. Cada relato es de una comunidad y de una persona que lo cuenta. Cuando comparamos, atribuimos: «Según doña Elsa…, en cambio según don Tomás…». Esa forma muestra respeto por ambas voces y evita ponerlas en competencia.",
    ],
    vocab=[("protagonista", "personaje o elemento principal de un relato"), ("criterio", "regla para comparar"), ("semejanza", "algo en lo que dos cosas se parecen"), ("diferencia", "algo en lo que dos cosas no se parecen"), ("poner en competencia", "hacer que dos cosas parezcan rivales")],
    worked=[
        W("Comparar con un criterio", RELATO_C + " " + RELATO_D + " Criterio: elemento protagonista.", ["En el primero es el agua.", "En el segundo es el viento."], "El agua en un relato y el viento en el otro."),
        W("Escribir una semejanza", "Criterio: qué se recuerda al final. En C: se debe dar las gracias. En D: el mundo se hizo prestándose cosas.", ["Uno termina recordando que se agradece el agua.", "El otro termina recordando que el mundo se hizo prestándose cosas."], "Ambos relatos terminan con una enseñanza que la comunidad recuerda."),
    ],
    mistakes=[
        M("Decir que un relato es más importante que otro.", "Jerarquiza.", "Comparo con criterios neutros."),
        M("Concluir que ambos relatos representan a todos los pueblos.", "Son de dos comunidades de práctica.", "Atribuyo a cada fuente."),
    ],
    R=[
        ex(RELATO_C + " ¿Qué elemento protagoniza «Los dos hijos del río»?", "El agua", "Los hijos del río son agua."),
        ex(RELATO_D + " ¿Qué elemento protagoniza «El primer canto»?", "El viento", "El viento aprende a cantar."),
        ex("Contrastar es: A) ver semejanzas y diferencias B) elegir el mejor", "A", "Contrastar no jerarquiza."),
    ],
    C=[
        ex("Verdadero o falso: «es más importante» es una forma de jerarquizar.", "Verdadero", "Pone un relato sobre otro."),
        ex("¿Cuál es un criterio neutro? A) qué elemento protagoniza B) cuál me gusta más", "A", "Se verifica en el texto."),
        ex("Verdadero o falso: dos relatos distintos pueden ser igual de respetables.", "Verdadero", "Cada uno es de su comunidad."),
    ],
    A=[
        ex("Une cada relato con lo que se recuerda al final. 1) Los dos hijos del río 2) El primer canto. a) el mundo se hizo prestándose cosas b) se debe dar las gracias al tomar agua", "1-b, 2-a", "Así termina cada relato."),
        ex("Criterio «cómo comienza». C: un solo río recorría la tierra seca. D: el viento no tenía voz. ¿Cuál es la diferencia? A) uno comienza con un río y el otro con un viento sin voz B) los dos comienzan con un río", "A", "Se compara el inicio de cada texto."),
        ex("Criterio «expresiones con nombre propio o imagen». ¿Cuál es una semejanza entre los dos relatos? A) ambos usan imágenes con nombre, como Agua Mansa y niña de piedra B) en ambos el viento es el protagonista", "A", "Las dos son expresiones significativas; el viento protagoniza solo uno."),
    ],
    Z=[
        ex("Marta dice: «El relato del agua es más importante porque sin agua no hay vida». ¿Qué error comete?", "Jerarquiza con un argumento ajeno al relato", "El relato del viento tiene su propio sentido."),
        ex("Un compañero dice: «Estos dos relatos muestran cómo piensan todos los pueblos». ¿Qué falla? A) generaliza dos relatos de práctica B) nada", "A", "Son de dos comunidades inventadas."),
    ],
    D=[
        ex("Elige la comparación respetuosa: A) «Según doña Elsa, el relato del agua recuerda que se agradece; según don Tomás, el del viento recuerda que el mundo se hizo prestándose cosas» B) «El del viento es más poético»", "A", "La A atribuye y describe."),
        ex("Si un criterio no aparece en uno de los relatos, ¿qué escribes? A) «no se menciona» B) lo que supongo", "A", "No se inventa."),
    ],
    context=[ex("Dos grupos presentan relatos distintos y discuten cuál es «mejor». ¿Qué propones? A) comparar qué elementos y expresiones tiene cada uno B) votar", "A", "Se contrasta sin jerarquizar.")],
    selfcheck=[
        ex("Nombra dos criterios neutros para comparar relatos.", "Dos entre: elemento protagonista, expresiones, qué se recuerda, quién cuenta", "Son criterios de la clase."),
        ex("Verdadero o falso: un relato puede ser «más antiguo» que otro según mi opinión.", "Falso", "No hay evidencia en el texto."),
        ex("Verdadero o falso: al comparar atribuyo cada relato a su fuente.", "Verdadero", "Es parte del respeto."),
    ],
    task=T("Compara «Los dos hijos del río» y «El primer canto». Textos: «" + RELATO_C.split("«", 2)[2].rstrip("»") + "» y «" + RELATO_D.split("«", 2)[2].rstrip("»") + "». Haz una tabla de dos columnas con cuatro filas: elemento protagonista, expresiones, qué se recuerda al final y quién cuenta. Escribe una semejanza, una diferencia y una frase que explique por qué no se dice cuál es mejor.",
           "Protagonista: el agua / el viento. Expresiones: Agua Mansa y Agua Brava / niña de piedra y prestar el canto. Al final se recuerda: dar las gracias / que el mundo se hizo prestándose cosas. Cuenta: doña Elsa / don Tomás. Semejanza: ambos usan expresiones con imagen. Diferencia: el elemento protagonista. No se dice cuál es mejor porque cada relato es de su comunidad.",
           ["usa criterios neutros", "atribuye a cada fuente", "no jerarquiza"], ["tabla de cuatro filas", "semejanza y diferencia", "frase de cierre"], ["decir cuál es mejor", "generalizar"],
           "Pedir que justifique cada celda; valorar que atribuya."),
    reinforce="Completa una tabla con dos columnas y la fila «qué se recuerda al final».",
    extend="Explica por qué dos relatos de comunidades distintas no se ponen en competencia.",
)

L(
    LR1, 6,
    materials=MAT,
    use="Aprenderé a comunicar la importancia de un relato fundacional a mi curso y a revisar mi trabajo con validación pertinente. Sirve para compartir lo aprendido con respeto y corregir errores antes de presentar.",
    prior=["Sé armar una respuesta atribuida y comparar relatos.", "Sé que la validación la hace el educador o la comunidad."],
    explain=[
        "Comunicar es presentar a otras personas lo que aprendimos. Para presentar un relato fundacional con respeto, decimos de qué comunidad viene, quién lo cuenta y qué permiso hay. Contamos solo lo autorizado, usamos «según…» y no cambiamos el relato. Si hay un límite, lo decimos: «esa parte no se cuenta».",
        "Revisar es leer el borrador con una lista de preguntas: ¿nombré la fuente?, ¿usé solo lo que el relato y el testimonio dicen?, ¿respeté el límite?, ¿evité generalizar?, ¿evité jerarquizar o restar valor?, ¿separé mi opinión? Si una respuesta es no, corrijo. Revisar es una forma de cuidar el relato de la comunidad.",
        "La validación pertinente la hace quien conoce el relato: el educador tradicional o una persona de la comunidad. Si nuestro trabajo trata sobre un relato real, se lo mostramos antes de presentarlo y aceptamos sus correcciones. Nosotros no podemos validar el sentido de un relato de otra comunidad.",
    ],
    vocab=[("comunicar", "presentar algo a otras personas"), ("borrador", "primera versión de un trabajo, que se puede corregir"), ("lista de revisión", "preguntas para comprobar un trabajo"), ("validación pertinente", "revisión de quien conoce y corresponde"), ("restar valor", "hacer parecer que algo importa menos")],
    worked=[
        W("Revisar un borrador", "Borrador: «Esa leyenda de los pueblos indígenas dice que el agua es sagrada». ¿Qué tres errores tiene?", ["«Leyenda» resta valor.", "«Los pueblos indígenas» generaliza.", "«Sagrada» no lo dijo la fuente."], "Resta valor, generaliza y afirma algo que la fuente no dijo."),
        W("Corregirlo", "Corrige el borrador con la fuente doña Elsa, de Quebrada Verde.", ["Cambio «leyenda» por «relato».", "Nombro la fuente y quito lo no dicho."], "Según doña Elsa, en el relato «Los dos hijos del río» se debe dar las gracias al tomar agua."),
    ],
    mistakes=[
        M("Presentar sin revisar con la lista.", "Pueden quedar errores de respeto.", "Uso la lista antes de presentar."),
        M("Presentar un relato real sin la validación del educador.", "Solo la comunidad valida su sentido.", "Se lo muestro antes."),
    ],
    R=[
        ex("¿Quién puede validar un relato real: el educador tradicional o un compañero?", "El educador tradicional", "Conoce el relato."),
        ex("En la lista de revisión, ¿qué pregunta cuida el respeto: «¿evité restar valor?» o «¿me quedó corto?»", "¿Evité restar valor?", "Cuida la forma de hablar."),
        ex("Un borrador es: A) una primera versión que se puede corregir B) la versión final", "A", "El borrador se revisa."),
    ],
    C=[
        ex("Verdadero o falso: revisar sirve para cuidar el relato de la comunidad.", "Verdadero", "Evita errores de respeto."),
        ex("Verdadero o falso: puedo cambiar el relato para que se entienda mejor sin consultar.", "Falso", "El relato pertenece a la comunidad."),
        ex("Si hay un límite en la ficha, ¿qué debo decir al presentar? A) “esa parte no se cuenta” B) nada", "A", "Así se avisa lo que no se cuenta."),
    ],
    A=[
        ex("Borrador: «Según doña Elsa, el agua cuida los campos y limpia lo que sobra en todos los pueblos». ¿Qué parte hay que quitar?", "En todos los pueblos", "Esa parte generaliza: doña Elsa habla de su comunidad."),
        ex("Borrador: «El relato dice que el río tuvo dos hijos». ¿Qué falta? A) la fuente B) un adorno", "A", "No dice quién cuenta ni la comunidad."),
        ex("Ordena los pasos antes de presentar: a) presento con «según…» b) pido validación c) reviso con la lista. Escribe las letras.", "c, b, a", "Revisar, validar y presentar."),
    ],
    Z=[
        ex("Marta revisó con la lista y está todo bien. ¿Puede decir que el educador tradicional validó su trabajo? Responde Sí o No.", "No", "La validación la hace él."),
        ex("Un compañero quiere agregar efectos de sonido para el Agua Brava. ¿Qué respondes? A) que primero consulte si corresponde B) que lo haga", "A", "No se cambia la forma del relato sin consultar."),
    ],
    D=[
        ex("Borrador: «Esa leyenda indígena dice que el agua limpia, según yo». ¿Qué dos problemas tiene?", "Resta valor y no nombra la fuente", "«Leyenda» y falta doña Elsa."),
        ex("Si el educador tradicional corrige tu trabajo, ¿qué haces? A) lo cambio y agradezco B) lo defiendo", "A", "Se acepta la validación."),
    ],
    context=[ex("Vas a presentar a tu curso lo que aprendiste de un relato de tu zona. Alguien dice que no hace falta permiso porque «ya lo conoce todo el mundo». ¿Qué haces? A) pido permiso y validación B) lo presento igual", "A", "Se pide permiso y validación.")],
    selfcheck=[
        ex("Escribe una pregunta de la lista de revisión.", "¿Nombré la fuente? o ¿respeté el límite? o ¿evité generalizar?", "Son preguntas de la lista."),
        ex("Verdadero o falso: yo puedo validar el sentido de un relato de otra comunidad.", "Falso", "Lo hace la comunidad."),
        ex("Nombra algo que no se cambia al comunicar un relato.", "El sentido, el orden o el límite", "Cambiarlo lo deforma."),
    ],
    task=T("Escribe un borrador de seis frases para presentar «Los dos hijos del río» (relato de práctica de Quebrada Verde, fuente doña Elsa): «" + RELATO_C.split("«", 2)[2].rstrip("»") + "». Incluye la fuente, las dos expresiones, lo que dice el testimonio («" + TESTIMONIO_C.split("«", 1)[1].rstrip("»") + "»), un límite y una frase con «Yo pienso…». Revísalo con la lista de seis preguntas y marca cada una que cumpliste.",
           "Según doña Elsa, de Quebrada Verde, el río tuvo dos hijos: Agua Mansa y Agua Brava. Agua Mansa regaba los campos y Agua Brava limpiaba los caminos. Según el testimonio, recuerdan que el agua cuida y limpia. No se cuenta el lugar donde nace el río. Yo pienso que el relato enseña a agradecer. Lista: seis preguntas cumplidas.",
           ["cumple la lista", "atribuye y declara límite", "separa opinión"], ["borrador de seis frases", "lista marcada"], ["generalizar", "restar valor"],
           "Pedir que muestre cada punto de la lista; valorar que anote qué consultará al educador."),
    reinforce="Revisa con la lista una respuesta tuya de una clase anterior.",
    extend="Escribe una nota de agradecimiento a doña Elsa usando «chaltumay» solo como lo dice la ficha de palabras.",
)

# ============================================================ OA LR02 · diálogo cultural con vocabulario pertinente
DIALOGO_R = ("Diálogo de práctica (inventado, en castellano). Valeria: Buenos días, don Ramón. ¿Qué trabajo hace usted en la caleta? Don Ramón: Arreglo redes. "
             "Valeria: ¿Cómo aprendió? Don Ramón: Mirando a los mayores y practicando. Valeria: ¿Qué es lo más importante? Don Ramón: Trabajar con paciencia y entre todos. "
             "Valeria: Muchas gracias por su tiempo.")

L(
    LR2, 1,
    materials=MAT,
    use="Aprenderé a situar un diálogo o una exposición breve sobre un aspecto de mi cultura: quiénes hablan, de qué tema, con qué permiso y con qué vocabulario. Sirve para conversar de mi cultura con respeto y claridad.",
    prior=["Sé qué es un diálogo y una exposición.", "Sé que cada persona habla de la cultura que vive y conoce."],
    explain=[
        "Un diálogo cultural es una conversación sobre algo de la propia cultura: un oficio, un lugar, una comida, una forma de ayudarse. Se hace con una persona de la comunidad que acepta conversar. Una exposición breve es contar ese tema a un grupo con orden. En ambos casos usamos un vocabulario pertinente, es decir, palabras que corresponden al tema.",
        "Antes de conversar, situamos el diálogo con una ficha: quiénes hablan, tema, lugar, permiso y límite. Si la persona prefiere no contar algo, se respeta. Si queremos anotar o grabar, pedimos permiso. En el diálogo de Valeria y don Ramón, por ejemplo, el tema es el oficio de arreglar redes en una caleta.",
        "El vocabulario pertinente puede estar en castellano o en lengua indígena. Si usamos palabras en lengua indígena, las tomamos de una fuente confiable, como el educador tradicional. En este cuaderno practicamos con castellano y con unas pocas palabras de fichas. El tema y las palabras elegidas deben ser de nuestra propia cultura o de una cultura que conocemos con permiso.",
    ],
    vocab=[("diálogo cultural", "conversación sobre un aspecto de la propia cultura"), ("exposición breve", "presentación corta y ordenada de un tema"), ("vocabulario pertinente", "palabras que corresponden al tema"), ("tema", "de qué se habla"), ("ficha del diálogo", "datos de quiénes hablan, tema, lugar, permiso y límite")],
    worked=[
        W("Situar el diálogo", DIALOGO_R + " ¿Quiénes hablan y de qué tema?", ["Hablan Valeria y don Ramón.", "El tema es el oficio de arreglar redes."], "Valeria y don Ramón hablan del oficio de arreglar redes."),
        W("Elegir palabras pertinentes", "Tema: arreglar redes. Palabras: malla, hilo, boya, semáforo. ¿Cuál no corresponde?", ["Pienso en el oficio.", "El semáforo es de las calles."], "Semáforo."),
    ],
    mistakes=[
        M("Grabar sin preguntar.", "La persona decide si se registra.", "Pido permiso."),
        M("Usar palabras que no corresponden al tema.", "El mensaje se confunde.", "Elijo palabras del tema."),
    ],
    R=[
        ex(DIALOGO_R + " ¿Qué trabajo hace don Ramón?", "Arregla redes", "Lo dice en su primera respuesta."),
        ex("Un diálogo cultural trata de: A) un aspecto de la propia cultura B) un tema cualquiera sin relación", "A", "Es la definición de la clase."),
        ex(DIALOGO_R + " ¿Dónde trabaja don Ramón: en la caleta o en la escuela?", "En la caleta", "Valeria lo pregunta y él responde."),
    ],
    C=[
        ex("Verdadero o falso: si la persona prefiere no contar algo, se respeta.", "Verdadero", "Es un límite."),
        ex("¿Qué es el vocabulario pertinente? A) palabras que corresponden al tema B) palabras muy largas", "A", "Pertinente es adecuado al tema."),
        ex("Verdadero o falso: puedo grabar la conversación sin pedir permiso.", "Falso", "Siempre se pide permiso."),
    ],
    A=[
        ex(DIALOGO_R + " ¿Cómo aprendió don Ramón el oficio?", "Mirando a los mayores y practicando", "Lo dice en su segunda respuesta."),
        ex("Une cada dato de la ficha con su pregunta. 1) tema 2) permiso 3) límite. a) ¿se puede grabar? b) ¿qué no se cuenta? c) ¿de qué se habla?", "1-c, 2-a, 3-b", "Cada dato responde una pregunta."),
        ex("Tema: la huerta. Palabras: semilla, riego, cosecha, ancla. ¿Cuál no corresponde?", "ancla", "El ancla es de un barco."),
    ],
    Z=[
        ex("Pablo conversa con don Ramón y anota todo lo que dice sin preguntar. ¿Qué debió hacer antes?", "Pedir permiso", "Anotar también es registrar."),
        ex("Una niña dice que va a exponer sobre el oficio de otra persona sin avisarle. ¿Qué falla? A) no pidió permiso B) nada", "A", "El oficio es de esa persona."),
    ],
    D=[
        ex("Dos fichas: F1 tiene tema, permiso y límite; F2 solo tiene tema. ¿Con cuál puedes conversar?", "Con la F1", "La F2 no tiene permiso ni límite."),
        ex("Si el tema incluye algo que la comunidad reserva, ¿qué haces? A) no lo uso B) lo uso si es corto", "A", "El límite se respeta."),
    ],
    context=[ex("Invitas a una persona de la comunidad a conversar con tu curso. ¿Qué preguntas antes? A) de qué temas puede hablar y si se puede anotar B) cuánto dura", "A", "Sitúa el tema y el permiso.")],
    selfcheck=[
        ex("Nombra tres datos de la ficha del diálogo.", "Tres entre: quiénes hablan, tema, lugar, permiso, límite", "Son datos de la ficha."),
        ex("Verdadero o falso: el vocabulario pertinente solo puede estar en lengua indígena.", "Falso", "Puede estar en castellano o en lengua indígena."),
        ex(DIALOGO_R + " ¿Cómo termina Valeria la conversación?", "Agradeciendo", "Dice muchas gracias."),
    ],
    task=T("Lee el diálogo de práctica: «" + DIALOGO_R.split("castellano). ", 1)[1] + "» Completa la ficha: quiénes hablan, tema, lugar, permiso (inventa «don Ramón autorizó») y límite (inventa «no se cuenta el nombre de su bote»). Luego escribe una lista de cinco palabras pertinentes para este tema y dos preguntas más que Valeria podría hacer.",
           "Quiénes: Valeria y don Ramón. Tema: arreglar redes. Lugar: la caleta. Permiso: don Ramón autorizó. Límite: no se cuenta el nombre de su bote. Palabras: red, malla, hilo, boya, caleta. Preguntas: ¿Cuánto tarda en arreglar una red? ¿Qué materiales usa?",
           ["completa la ficha", "elige palabras pertinentes", "formula preguntas respetuosas"], ["ficha completa", "lista de cinco palabras", "dos preguntas"], ["palabras de otro tema", "preguntas que invadan"],
           "Pedir que justifique cada palabra; valorar las preguntas."),
    reinforce="Copia el diálogo y subraya con un color las preguntas de Valeria.",
    extend="Escribe un diálogo de cuatro turnos sobre otro oficio de tu comunidad.",
)

DIALOGO_R2 = ("Diálogo de práctica (inventado, en castellano). Camila: Mari mari, doña Teresa. Doña Teresa: Mari mari, Camila. Camila: ¿Qué hace usted en la feria de la comunidad? "
              "Doña Teresa: Vendo pan y verduras de mi huerta. Camila: ¿Y qué le gusta de la feria? Doña Teresa: Que nos juntamos y nos ayudamos. Camila: Chaltumay, doña Teresa.")

L(
    LR2, 2,
    materials=MAT,
    use="Aprenderé a escuchar un diálogo cultural con límites declarados: qué se dijo, qué no se dijo y qué se reserva, y a reconocer las palabras y expresiones significativas. Sirve para conversar sin inventar lo que la otra persona no contó.",
    prior=["Sé situar un diálogo cultural.", "Sé que «mari mari» es un saludo y «chaltumay» es «gracias» en mapuzugun."],
    explain=[
        "Escuchar un diálogo es seguir los turnos y entender qué dice cada persona. Anotamos las ideas con el nombre de quien las dijo: «Doña Teresa vende pan y verduras». Así nunca atribuimos a una persona lo que dijo otra. Si no entendemos, pedimos que lo repita amablemente.",
        "Escuchar con límites declarados es distinguir tres cosas: lo que se dijo, lo que no se dijo y lo que la persona prefiere reservar. En el diálogo de Camila y doña Teresa se dice qué vende y qué le gusta de la feria, pero no se dice cuántas personas participan. Eso no se completa con ideas propias.",
        "En el diálogo aparecen un saludo y un agradecimiento de la ficha de palabras. También hay expresiones significativas en castellano, como «nos juntamos y nos ayudamos», que muestran una forma de vivir en comunidad. Su sentido completo lo explica la persona que lo dijo. Nosotros anotamos y, si queremos, preguntamos.",
    ],
    vocab=[("turno", "momento en que habla una persona"), ("idea principal", "lo más importante que dice una persona"), ("reservar", "guardar algo sin contarlo"), ("expresión significativa", "palabra o frase con sentido especial para la comunidad"), ("repetir", "volver a decir para entender mejor")],
    worked=[
        W("Anotar con el nombre", DIALOGO_R2 + " ¿Qué vende doña Teresa?", ["Busco su respuesta.", "Dice que vende pan y verduras."], "Pan y verduras de su huerta."),
        W("Lo que no se dijo", DIALOGO_R2 + " ¿Dice doña Teresa cuántas personas van a la feria?", ["Reviso sus respuestas.", "No lo menciona."], "No, ese dato no se dijo."),
    ],
    mistakes=[
        M("Atribuir una idea a la persona equivocada.", "Cada turno es de una persona.", "Anoto el nombre al lado de cada idea."),
        M("Completar con mis ideas lo que no se dijo.", "Mezclo mi voz con la suya.", "Escribo «no se dijo»."),
    ],
    R=[
        ex(DIALOGO_R2 + " ¿Qué saludo usan al comienzo?", "Mari mari", "Es el saludo que aparece."),
        ex(DIALOGO_R2 + " ¿Qué vende doña Teresa además de verduras?", "Pan", "Lo dice en su respuesta."),
        ex(DIALOGO_R2 + " ¿Con qué palabra agradece Camila?", "Chaltumay", "Es el agradecimiento que usa."),
    ],
    C=[
        ex(DIALOGO_R2 + " ¿Qué le gusta a doña Teresa de la feria: juntarse y ayudarse o que haya música?", "Juntarse y ayudarse", "Lo dice ella."),
        ex("Verdadero o falso: si la persona no contó algo, puedo completarlo con una idea mía.", "Falso", "Eso mezcla mi voz con la suya."),
        ex("Si no entiendes una respuesta, ¿qué haces? A) pido que la repita B) la invento", "A", "Se pregunta con respeto."),
    ],
    A=[
        ex(DIALOGO_R2 + " Une cada dato con quien lo dijo. 1) «vendo pan y verduras» 2) «¿qué hace usted en la feria?» a) Camila b) doña Teresa", "1-b, 2-a", "Cada turno es de una persona."),
        ex(DIALOGO_R2 + " ¿Cuántos turnos tiene el diálogo, contando cada cambio de persona?", "Siete", "Camila habla cuatro veces y doña Teresa tres: 4 + 3 = 7."),
        ex(DIALOGO_R2 + " Escribe una idea de doña Teresa con su nombre al comienzo.", "Doña Teresa vende pan y verduras de su huerta", "Nombra a quien lo dijo."),
    ],
    Z=[
        ex("Rafael dice: «Doña Teresa contó que hay una fiesta en la feria». Según el diálogo, ¿lo dijo? Responde Sí o No.", "No", "Solo habla de vender y ayudarse."),
        ex("Doña Teresa responde: «Eso no lo cuento». ¿Qué hace quien escucha? A) respeta y cambia de tema B) insiste", "A", "El límite de la persona se respeta."),
    ],
    D=[
        ex("Dos resúmenes. R1: «Doña Teresa dice que en la feria se juntan y se ayudan». R2: «Doña Teresa dice que todas las ferias del país son así». ¿Cuál es fiel?", "R1", "La R2 generaliza a todas las ferias."),
        ex("En el diálogo hay una expresión que muestra una forma de vivir en comunidad. ¿Cuál es?", "Nos juntamos y nos ayudamos", "Doña Teresa la dice."),
    ],
    context=[ex("Una vecina te cuenta cómo funciona la feria de su comunidad y dice: «eso otro no es para contarlo». ¿Qué haces con tus apuntes? A) borro eso B) lo dejo por si acaso", "A", "Se respeta su límite.")],
    selfcheck=[
        ex("Nombra las tres cosas que se distinguen al escuchar con límites.", "Lo que se dijo, lo que no se dijo y lo reservado", "Son los límites del diálogo."),
        ex(FICHA_PAL + " ¿Qué es «mari mari» en mapuzugun?", "Un saludo", "La ficha de palabras lo indica."),
        ex("Verdadero o falso: anotar el nombre de quien dijo cada idea evita atribuir mal.", "Verdadero", "Cada idea queda con su voz."),
    ],
    task=T("Lee el diálogo de práctica: «" + DIALOGO_R2.split("castellano). ", 1)[1] + "» Haz una tabla con tres columnas: «Lo que se dijo» (tres ideas con el nombre de quien las dijo), «Lo que no se dijo» (dos datos) y «Palabras o expresiones significativas» (al menos dos). Escribe dos preguntas respetuosas para doña Teresa.",
           "Se dijo: Doña Teresa vende pan y verduras; le gusta juntarse y ayudarse; Camila saluda con «mari mari». No se dijo: cuántas personas van; qué día es la feria. Expresiones: mari mari, chaltumay, nos juntamos y nos ayudamos. Preguntas: ¿Cada cuánto es la feria? ¿Cómo se preparan?",
           ["registra ideas con su autor", "identifica lo que no se dijo", "reconoce expresiones"], ["tabla de tres columnas", "dos preguntas"], ["atribuir mal", "completar con datos propios"],
           "Pedir que muestre en el diálogo cada idea; valorar que no complete."),
    reinforce="Escribe tres turnos del diálogo en orden con el nombre de quien habla.",
    extend="Escribe una pregunta que no invade la intimidad y que serviría para saber más de la feria.",
)

L(
    LR2, 3,
    materials=MAT,
    use="Aprenderé a relacionar el vocabulario y las expresiones de un diálogo con el tema cultural y con la vida de la comunidad. Sirve para elegir palabras pertinentes y explicar por qué importan.",
    prior=["Sé escuchar un diálogo con límites.", "Sé que el vocabulario pertinente corresponde al tema."],
    explain=[
        "Las palabras de un diálogo se relacionan con el tema y con la vida de la comunidad. En el diálogo de don Ramón, «red», «malla» y «boya» pertenecen al oficio de la pesca, y «paciencia» y «entre todos» muestran cómo se trabaja. Agrupar las palabras por tema ayuda a preparar una conversación o una exposición.",
        "Algunas expresiones muestran valores. Cuando don Ramón dice «trabajar con paciencia y entre todos», habla de una forma de trabajar. Podemos decir qué muestra la expresión: que el trabajo se hace con calma y en grupo. Pero no podemos decir que sea una creencia de un pueblo, porque él no lo dijo. Siempre separamos lo que dice la persona de lo que pensamos nosotros.",
        "Para dialogar con vocabulario variado evitamos repetir «cosa» o «bonito» y buscamos palabras más precisas. Si queremos añadir una palabra en lengua indígena, la pedimos al educador tradicional y anotamos quién nos la enseñó. De ese modo el vocabulario es pertinente, preciso y respetuoso.",
    ],
    vocab=[("vocabulario variado", "que no repite siempre las mismas palabras"), ("campo semántico", "grupo de palabras de un mismo tema"), ("valor", "idea sobre cómo conviene vivir o trabajar, como la paciencia"), ("preciso", "que dice justo lo que se quiere decir"), ("expresión", "palabra o frase que dice algo con sentido")],
    worked=[
        W("Agrupar palabras", "Tema: la huerta. Palabras: semilla, riego, cosecha, boya. ¿Cuál no es del tema?", ["Pienso en la huerta.", "La boya es de la pesca."], "Boya."),
        W("Qué muestra una expresión", DIALOGO_R + " ¿Qué muestra «trabajar con paciencia y entre todos»?", ["Dice cómo se trabaja.", "Muestra calma y trabajo en grupo."], "Una forma de trabajar con calma y en grupo, según don Ramón."),
    ],
    mistakes=[
        M("Afirmar que una expresión es una creencia de un pueblo.", "La persona no lo dijo.", "Digo qué muestra según lo que dice."),
        M("Repetir «cosa» en todo el diálogo.", "No se entiende bien.", "Uso palabras precisas del tema."),
    ],
    R=[
        ex("Tema: la pesca. ¿Qué palabra corresponde: red o semilla?", "Red", "La red es del oficio de pesca."),
        ex(DIALOGO_R + " ¿Qué dos palabras de valor dice don Ramón: paciencia y entre todos o dinero y rapidez?", "Paciencia y entre todos", "Son sus palabras."),
        ex("Tema: la huerta. ¿Qué palabra corresponde: riego o ancla?", "Riego", "El riego es de la huerta."),
    ],
    C=[
        ex("Verdadero o falso: un campo semántico es un grupo de palabras de un mismo tema.", "Verdadero", "Esa es su definición."),
        ex("¿Qué es un valor? A) una idea sobre cómo conviene vivir o trabajar B) un precio", "A", "Por ejemplo, la paciencia."),
        ex("Verdadero o falso: puedo decir que una expresión es una creencia de un pueblo si la persona no lo dijo.", "Falso", "Eso sería inventar un sentido."),
    ],
    A=[
        ex("Une cada palabra con su tema. 1) malla 2) cosecha. a) huerta b) pesca", "1-b, 2-a", "La malla es de la red y la cosecha de la huerta."),
        ex("¿Cuál frase usa palabras más precisas que «bonita» y «bonito»? A) «La caleta es amplia y el mar es tranquilo» B) «La caleta es cosa y el mar es cosa»", "A", "«Amplia» y «tranquilo» dicen cómo es cada cosa; «cosa» no dice nada."),
        ex(DIALOGO_R2 + " ¿Qué valor muestra «nos juntamos y nos ayudamos»: la ayuda mutua o la competencia?", "La ayuda mutua", "Se ayudan entre todos."),
    ],
    Z=[
        ex("Tomás dice: «Si don Ramón habla de paciencia, entonces todos los pescadores son pacientes». ¿Qué error comete?", "Generaliza lo que dice una persona", "Don Ramón habla de sí mismo."),
        ex("Una niña dice que «paciencia» en la lengua de su comunidad se dice de cierta manera, pero no lo sabe con certeza. ¿Qué debe hacer? A) preguntar al educador tradicional B) usar la que le parezca", "A", "Solo él puede confirmarlo."),
    ],
    D=[
        ex("¿Cuál frase usa palabras del tema de la pesca? A) «El bote sale con la red cuando sube la marea.» B) «El bote sale con la semilla cuando sube la cosecha.»", "A", "Bote, red y marea son de la pesca; semilla y cosecha, de la huerta."),
        ex("Elige la frase que explica sin inventar: A) «Según don Ramón, trabajar con paciencia y entre todos es importante» B) «La paciencia es sagrada para los pescadores»", "A", "La B inventa un sentido."),
    ],
    context=[ex("Preparas una exposición sobre un oficio de tu comunidad y repites mucho «cosa». ¿Qué haces? A) busco palabras precisas del tema B) hablo más rápido", "A", "La precisión ayuda a entender.")],
    selfcheck=[
        ex("Nombra una palabra del campo semántico de la huerta.", "Semilla, riego, cosecha o hortaliza", "Pertenecen al tema."),
        ex("Verdadero o falso: «cosa» es una palabra precisa.", "Falso", "Es muy general."),
        ex("¿Dónde confirmas una palabra indígena de tu comunidad? A) con el educador tradicional B) adivinando", "A", "Es la fuente adecuada."),
    ],
    task=T("Elige el tema «un oficio de mi comunidad» (por ejemplo, pesca, huerta o tejido). Escribe una lista de seis palabras pertinentes y una expresión que muestre un valor (por ejemplo, «trabajar entre todos»). Luego escribe un diálogo de cuatro turnos que use al menos cuatro de esas palabras y la expresión, sin repetir «cosa» ni «bonito». Si añades una palabra de la lengua de tu comunidad, anota quién te la enseñó.",
           "Tema: la huerta. Palabras: semilla, riego, cosecha, hortaliza, tierra, canasto. Expresión: «cuidar la tierra entre todos». Diálogo: Ana: ¿Cuándo es la cosecha? Rosa: Cuando las hortalizas maduran. Ana: ¿Quién ayuda con el riego? Rosa: Cuidamos la tierra entre todos.",
           ["lista pertinente", "diálogo de cuatro turnos", "expresión de valor"], ["lista de seis palabras", "diálogo", "fuente de la palabra indígena"], ["palabras de otro tema", "traducir sin fuente"],
           "Pedir que explique por qué cada palabra pertenece al tema; valorar la fuente."),
    reinforce="Escribe tres palabras más para cada tema: huerta, pesca y reunión de la comunidad.",
    extend="Prepara una lista de cinco palabras sobre un tema de tu cultura y subraya las que debes confirmar con el educador tradicional.",
)

L(
    LR2, 4,
    materials=MAT,
    use="Aprenderé a construir una exposición breve sobre un aspecto de mi cultura, con vocabulario pertinente, atribución de las ideas y límites declarados. Sirve para presentar lo que sé de modo ordenado y respetuoso.",
    prior=["Sé escuchar un diálogo con límites y relacionar vocabulario con el tema.", "Sé que una exposición tiene saludo, tema, ideas y cierre."],
    explain=[
        "Una exposición breve sobre la propia cultura tiene cinco partes: saludo, tema, ideas, límite y cierre. En el saludo nombramos a quien escucha. En el tema decimos de qué hablaremos. En las ideas contamos lo que sabemos y de dónde lo sabemos. En el límite avisamos lo que no cuento o no sé. En el cierre agradecemos.",
        "Para atribuir, usamos frases como «Mi vecino me contó que…» o «Según el educador tradicional…». Para el vocabulario, elegimos al menos tres palabras pertinentes del tema y, si corresponde, una palabra en lengua indígena aprendida de una fuente confiable. No hablamos por todo un pueblo ni inventamos significados.",
        "Antes de exponer, ensayamos en voz alta con un compañero o una persona de confianza y anotamos qué mejorar. Hablamos despacio, con un volumen que permita escuchar. Si cometemos un error con una palabra, pedimos disculpas y la repetimos. Lo importante es presentar con respeto lo que aprendimos de nuestra comunidad.",
    ],
    vocab=[("exposición breve", "presentación corta y ordenada de un tema"), ("límite", "aclaración de lo que no cuento o no sé"), ("ensayar", "practicar antes de presentar"), ("atribuir", "decir quién enseñó o contó algo"), ("volumen", "qué tan fuerte o suave se habla")],
    worked=[
        W("Ordenar las partes", "Partes: a) Gracias por escuchar b) Hoy hablaré de la huerta c) Buenos días d) Mi vecina me contó que se riega temprano e) No cuento los secretos de su huerta. ¿En qué orden va?", ["Saludo.", "Tema.", "Idea.", "Límite.", "Cierre."], "c, b, d, e, a"),
        W("Atribuir", "Idea: «Las papas crecen bajo la tierra». Atribúyela a una vecina.", ["Pienso en quién me lo contó.", "Escribo su nombre antes de la idea."], "Mi vecina me contó que las papas crecen bajo la tierra."),
    ],
    mistakes=[
        M("Saltarme el límite.", "El público cree que lo sé todo o que lo puedo contar todo.", "Aviso lo que no cuento."),
        M("Hablar por todos los pueblos.", "Solo hablo de lo que conozco.", "Digo de quién viene cada idea."),
    ],
    R=[
        ex("La primera parte de la exposición es: A) el saludo B) el cierre", "A", "Se empieza saludando."),
        ex("El agradecimiento va: A) al final B) al comienzo", "A", "Está en el cierre."),
        ex(DIALOGO_R + " ¿Qué le dice Valeria a don Ramón al final?", "Muchas gracias por su tiempo", "Es su cierre."),
    ],
    C=[
        ex("Verdadero o falso: avisar lo que no cuento es parte de una exposición respetuosa.", "Verdadero", "Es el límite."),
        ex("¿Qué frase atribuye mejor? A) «Mi vecina me contó…» B) «Todos saben…»", "A", "Nombra la fuente."),
        ex("Verdadero o falso: puedo inventar el significado de una palabra indígena en mi exposición.", "Falso", "Se confirma con el educador."),
    ],
    A=[
        ex("Ordena: a) No cuento los secretos b) Hoy hablaré del tejido c) Buenos días d) Mi vecina teje con lana e) Gracias. Escribe las letras.", "c, b, d, a, e", "Saludo, tema, idea, límite y cierre."),
        ex("Escribe la idea «el pan se hace con harina» con atribución a don Mateo.", "Don Mateo me contó que el pan se hace con harina", "Se nombra la fuente."),
        ex("Tema: la pesca. Elige tres palabras pertinentes: A) red, bote, marea B) semáforo, cancha, pizarra", "A", "Las del A son de la pesca."),
    ],
    Z=[
        ex("Pablo expone: «Todos los pueblos hacen pan igual». ¿Qué error comete?", "Habla por todos los pueblos", "Solo puede hablar de lo que conoce."),
        ex("Una niña se equivoca al decir una palabra indígena y se queda callada. ¿Qué es mejor? A) pedir disculpas, repetirla y seguir B) callarse", "A", "Corregirse con respeto es parte de aprender."),
    ],
    D=[
        ex("Dos exposiciones: la 1 tiene las cinco partes y atribuye; la 2 no atribuye ni tiene límite. ¿Cuál es mejor según lo aprendido?", "La 1", "Cumple las reglas."),
        ex("Si una vecina te pidió que no cuentes una parte de su oficio, ¿qué haces? A) no la menciono y aviso que hay un límite B) la cuento si es corta", "A", "Su límite se respeta."),
    ],
    context=[ex("Vas a exponer sobre un oficio de tu comunidad durante tres minutos. ¿Qué haces? A) preparo saludo, tema, ideas atribuidas, límite y cierre B) improviso", "A", "Una estructura clara cabe en el tiempo.")],
    selfcheck=[
        ex("Nombra las cinco partes de la exposición.", "Saludo, tema, ideas, límite y cierre", "Son las partes de la clase."),
        ex("Verdadero o falso: puedo usar palabras indígenas sin saber si las escribo bien.", "Falso", "Se confirman con la fuente."),
        ex("Verdadero o falso: ensayar ayuda a hablar mejor.", "Verdadero", "Permite detectar qué mejorar."),
    ],
    task=T("Prepara una exposición de cinco partes sobre un aspecto de tu cultura (un oficio, un lugar o una comida de tu comunidad). Escribe: saludo, tema, dos ideas con atribución («Mi vecina/vecino me contó que…»), un límite y cierre con agradecimiento. Incluye al menos tres palabras pertinentes del tema. Ensáyala en voz alta con un compañero o una persona de confianza y anota una cosa para mejorar. Si usas una palabra indígena, anota quién te la enseñó.",
           "Buenos días. Hoy hablaré de la pesca en la caleta. Don Ramón me contó que arregla redes y que lo aprendió mirando a los mayores. Me dijo que trabaja con paciencia. No cuento el nombre de su bote. Gracias por escucharme. Palabras: red, malla, boya. Mejorar: hablar más despacio.",
           ["incluye las cinco partes", "atribuye las ideas", "usa vocabulario pertinente"], ["texto de la exposición", "nota de ensayo"], ["hablar por todos", "inventar palabras indígenas"],
           "Pedir que lea y señale cada parte; valorar que declare el límite."),
    reinforce="Reordena en tu hoja las cinco partes de una exposición con tus propias frases.",
    extend="Ensaya tu exposición dos veces con volúmenes distintos y anota cuál se escucha mejor.",
)
