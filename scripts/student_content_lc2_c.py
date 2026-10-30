"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR03 (textos en castellano con expresiones en lengua indígena), LR04 (escritura de palabras y frases)
y LR05 (recursos tecnológicos para escuchar, ver y transcribir).

Criterio de autoría: los textos y fichas son inventados solo para practicar la lectura y se declaran como tales.
Las únicas expresiones en lengua indígena son saludos y palabras muy conocidas y atestiguadas (mari mari, chaltumay,
iorana, maururu, ko, antü, kuyen, ruka, mapu, ñuke, pewen, lafken). No se inventa gramática, pronunciación ni
significados rituales. Cada tarea abierta remite al educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LR3, LR4, LR5 = "LC02 OA LR03", "LC02 OA LR04", "LC02 OA LR05"

CONSULT = " Recuerda: la forma tradicional de escribir, decir y usar estas palabras la enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de escritura, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

FICHA_MARI = "Ficha: «mari mari» es un saludo en mapuzugun, la lengua del pueblo mapuche."
FICHA_RN = "Ficha: «iorana» es un saludo y «maururu» es «gracias», ambos en rapa nui, la lengua del pueblo rapa nui."
FICHA_CHAL = "Ficha: «chaltumay» quiere decir «gracias» en mapuzugun."
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


# =================================================================== LR03 · textos en castellano con expresiones en lengua indígena
L(
    LR3, 1,
    materials="Lápiz y hoja. Los textos de práctica están escritos en este cuaderno: fueron inventados para entrenar la lectura y no son relatos de ningún pueblo.",
    use="Aprenderé a encontrar las palabras en lengua indígena que aparecen dentro de un texto en castellano. Sirve para leer con atención y respeto textos de varias culturas.",
    prior=["Sé leer oraciones cortas en castellano.", "Sé que en Chile hay pueblos originarios con sus propias lenguas."],
    explain=[
        "Un texto en castellano puede traer una palabra o una expresión de una lengua indígena. En este cuaderno las escribimos entre comillas «así». Una expresión es una palabra o un grupo de palabras que se dicen juntas, como «mari mari».",
        "Para reconocerlas, leo todo el texto y busco las comillas. Luego leo la ficha que viene con el texto. La ficha dice de qué lengua es la expresión y qué quiere decir. Si no hay ficha, no adivino: pregunto.",
        "Una lengua indígena se cuida cuando la escuchamos y la leemos con respeto. Hoy hay lenguas que hablan pocas personas, y muchas comunidades trabajan para que vuelvan a usarse. Eso se llama revitalizar. Yo ayudo leyendo con atención y sin burlarme.",
    ],
    vocab=[("texto", "escrito que cuenta o explica algo"), ("castellano", "la lengua en que está escrito este cuaderno"), ("lengua indígena", "lengua de un pueblo originario"), ("expresión", "palabra o grupo de palabras que se dicen juntas"), ("ficha", "papel con datos para entender un texto")],
    worked=[
        W("Encontrar la expresión", "Texto: «Una visita llegó a la sala y dijo «mari mari». Todos la saludamos.» " + FICHA_MARI + " ¿Qué expresión está en lengua indígena?", ["Busco las comillas dentro del texto.", "Encuentro «mari mari».", "La ficha dice que es mapuzugun."], "«mari mari»"),
        W("Separar los dos idiomas", "Texto: «Dijo «iorana» y sonrió.» " + FICHA_RN + " ¿Qué palabras del texto están en castellano?", ["La expresión «iorana» es de rapa nui.", "El resto es castellano: dijo, y, sonrió.", "Son tres palabras en castellano."], "dijo, y, sonrió"),
    ],
    mistakes=[
        M("Pensar que todo el texto está en lengua indígena porque trae una expresión.", "El texto está escrito en castellano y solo algunas partes son de otra lengua.", "Marco con lápiz solo lo que está entre comillas y lo separo del resto."),
        M("Decir de qué lengua es una palabra sin leer la ficha.", "Muchas palabras se parecen y puedo equivocarme.", "Leo la ficha; si no hay, pregunto al profesor o al educador tradicional."),
    ],
    R=[
        ex("Texto: «Mi tía entró y dijo «mari mari»». ¿Qué expresión está entre comillas?", "«mari mari»", "Lo que va entre comillas es la expresión en lengua indígena."),
        ex("La expresión «mari mari» tiene dos palabras. ¿Cuántas palabras tiene: 1, 2 o 3?", "2", "Se lee «mari» y otra vez «mari»: son dos palabras."),
        ex(FICHA_MARI + " ¿De qué lengua es «mari mari»?", "mapuzugun", "La ficha dice que es una expresión en mapuzugun."),
    ],
    C=[
        ex("Texto: «Al llegar, la visita dijo «mari mari» y todos respondimos con una sonrisa.» " + FICHA_MARI + " ¿Para qué se usa la expresión en este texto?", "para saludar", "La ficha dice que «mari mari» es un saludo."),
        ex("Verdadero o falso: en el texto «Dijo «iorana» y sonrió», todas las palabras están en rapa nui.", "Falso", "Solo «iorana» es rapa nui; las otras palabras son castellano."),
        ex("En «Vi un «pewen» cerca de casa», ¿qué parte del texto es castellano: «Vi un» o «pewen»? (Ficha: «pewen» es una palabra en mapuzugun).", "«Vi un»", "«Pewen» es la palabra mapuzugun; «Vi un» está en castellano."),
    ],
    A=[
        ex("Texto: «En la mañana, la visita dijo «iorana» y al irse dijo «maururu». Yo dije «gracias».» " + FICHA_RN + " ¿Cuántas expresiones en rapa nui hay?", "2", "«Iorana» y «maururu» son las dos expresiones en rapa nui."),
        ex("Mismo texto de la visita que dijo «iorana» y «maururu». ¿Cuál de las dos expresiones quiere decir «gracias»?", "maururu", "La ficha dice que «maururu» es «gracias»."),
        ex("Texto: «Vimos un «pewen» cerca del «lafken».» Ficha: «pewen» es un árbol (araucaria) y «lafken» es mar, ambas en mapuzugun. ¿Cuál palabra nombra el mar?", "lafken", "La ficha dice que «lafken» es el mar."),
    ],
    Z=[
        ex("Ana dice: «Este texto está en castellano, así que «mari mari» también es castellano». ¿Tiene razón? Responde Sí o No.", "No", "El texto es castellano, pero la expresión «mari mari» es mapuzugun."),
        ex("Dos niños leen «iorana» y «hola». Con la ficha de rapa nui, ¿cuál de las dos es la expresión en lengua indígena?", "iorana", "La ficha de rapa nui dice que «iorana» es de esa lengua; «hola» es castellano."),
    ],
    D=[
        ex("Texto: «Dijo «mari mari», sonrió y dijo «chaltumay».» " + FICHA_MARI + " " + FICHA_CHAL + " ¿Cuántas palabras en castellano hay en el texto?", "4", "Las palabras en castellano son: dijo, sonrió, y, dijo."),
        ex("Un texto trae la palabra «lof» sin ninguna ficha. ¿Qué haces: adivinas la lengua o preguntas a una fuente?", "preguntas a una fuente", "Sin ficha no sé de qué lengua es ni qué significa."),
    ],
    context=[ex("El cartel de la puerta de tu sala dice: «Bienvenidos. Mari mari. Pasen con calma.» ¿Cuál es la expresión en lengua indígena?", "Mari mari", "Es el saludo en mapuzugun dentro de un texto en castellano.")],
    selfcheck=[
        ex("¿Dónde busco primero las expresiones en lengua indígena de un texto de este cuaderno?", "entre comillas", "En este cuaderno las expresiones van entre comillas."),
        ex("¿Qué papel me dice de qué lengua es una expresión y qué significa?", "la ficha", "La ficha trae esos datos."),
        ex("Si no hay ficha y no sé el significado, ¿qué hago?", "pregunto", "No adivino; pregunto al educador tradicional o a otra fuente."),
    ],
    task=T(
        "Lee este texto inventado para practicar: «Hoy llegó una invitada a mi curso. Dijo «mari mari» y nos miró con cariño. Después dijo «chaltumay» a la profesora.» " + FICHA_MARI + " " + FICHA_CHAL + " En tu cuaderno copia las dos expresiones en lengua indígena y escribe al lado de cada una qué quiere decir, según la ficha. Después escribe una pregunta que le harías a la educadora tradicional.",
        "«mari mari» = saludo en mapuzugun. «chaltumay» = gracias en mapuzugun. Pregunta: ¿cuándo se dice «mari mari» en su comunidad?",
        ["encuentra las dos expresiones", "escribe el significado que dice la ficha", "formula una pregunta para el educador/a tradicional"],
        ["dibujo o escritura de las expresiones", "pregunta escrita o dicha en voz alta"],
        ["escribir un significado que la ficha no dice", "copiar una palabra del castellano como si fuera de la lengua indígena"],
        "Reconoce que separó castellano y lengua indígena con ayuda de la ficha; si inventó un significado, pídele que lo cambie por una pregunta.",
    ),
    reinforce="Lee en voz alta el texto «Dijo «iorana» y sonrió» y señala con el dedo la expresión que está en rapa nui.",
    extend="Escribe una oración tuya en castellano que incluya el saludo «mari mari» entre comillas, como en los textos de esta clase.",
)

L(
    LR3, 2,
    materials="Lápiz y hoja. Las fichas de fuentes están escritas aquí y son inventadas para practicar; en la vida real, la fuente es una persona o un material de la comunidad.",
    use="Aprenderé a distinguir lo que dice una fuente de lo que yo pienso. Sirve para entender de verdad una expresión en lengua indígena y no inventarla.",
    prior=["Sé encontrar una expresión entre comillas en un texto.", "Sé que hay educadores tradicionales que enseñan la lengua."],
    explain=[
        "Una fuente es la persona, el libro o el material de donde viene un dato. Una fuente comunitaria es una persona o un grupo de la comunidad que conoce y cuida su lengua, como un educador o una educadora tradicional. Ellos y ellas pueden explicar qué quiere decir una expresión y cuándo se usa.",
        "Cuando leo, separo dos cosas. Una es lo que dice la fuente. Otra es lo que yo pienso o me imagino. Puedo escribir «la fuente dice…» para lo primero y «yo creo…» para lo segundo. Así no mezclo mis ideas con el saber de la comunidad.",
        "También escucho con cuidado. Si un adulto lee en voz alta lo que explicó la educadora, yo escucho hasta el final y recién después respondo. Si no entendí, pido que lo repita. Preguntar no es un error.",
    ],
    vocab=[("fuente", "persona o material de donde viene un dato"), ("fuente comunitaria", "persona o grupo de la comunidad que conoce y cuida su lengua"), ("según", "palabra para decir quién lo dice"), ("opinión", "lo que yo pienso, que no viene de la fuente"), ("repetir", "volver a decir algo para entenderlo mejor")],
    worked=[
        W("Qué dice la fuente", "Ficha de práctica (inventada): la educadora tradicional de una escuela explicó que «chaltumay» se dice para agradecer. Un niño piensa que «chaltumay» es el nombre de un animal. ¿Quién tiene el dato de la fuente?", ["Leo qué explicó la educadora: se dice para agradecer.", "Lo del animal es solo lo que piensa el niño.", "El dato de la fuente es el de la educadora."], "la educadora: «chaltumay» se dice para agradecer"),
        W("Escribir con «según»", "La ficha dice que «iorana» es un saludo en rapa nui. ¿Cómo lo escribo diciendo quién lo dice?", ["Empiezo con «Según la ficha…».", "Sigo con lo que dice: «iorana» es un saludo.", "Termino con un punto."], "Según la ficha, «iorana» es un saludo en rapa nui."),
    ],
    mistakes=[
        M("Escribir mi idea como si la hubiera dicho la fuente.", "Mezclo lo que pienso con lo que enseñó la comunidad.", "Uso «la fuente dice» para su dato y «yo creo» para el mío."),
        M("Responder sin escuchar hasta el final.", "Me pierdo una parte importante de la explicación.", "Espero a que termine y, si dudo, pido que lo repita."),
    ],
    R=[
        ex("Una educadora tradicional explica una palabra. ¿Ella es una fuente o una opinión?", "una fuente", "Ella conoce la lengua y da el dato."),
        ex("Completa: «____ la ficha, «iorana» es un saludo». Elige: según o también.", "según", "«Según» dice quién da el dato."),
        ex("Si no entiendo lo que leyó el adulto, ¿qué hago: pido que lo repita o me quedo callado?", "pido que lo repita", "Preguntar de nuevo ayuda a entender y no es un error."),
    ],
    C=[
        ex("Ficha de práctica (inventada): la educadora dijo que «mari mari» es un saludo. Mateo dice: «Yo creo que es una comida». ¿Quién tiene el dato de la fuente?", "la educadora", "Lo de Mateo es solo lo que él cree."),
        ex("Verdadero o falso: lo que yo me imagino sobre una palabra vale lo mismo que lo que explica la educadora tradicional.", "Falso", "La educadora conoce su lengua; mi idea no es un dato."),
        ex("La frase «Yo creo que «ko» es una flor». ¿Es un dato de la fuente o una opinión?", "una opinión", "Empieza con «yo creo» y nadie la comprobó."),
    ],
    A=[
        ex("Ficha: la educadora dijo que «maururu» es «gracias» en rapa nui. Elige la mejor frase: A) «Según la educadora, «maururu» es gracias en rapa nui.» B) «Yo creo que «maururu» es un baile».", "A", "A dice quién da el dato; B es una idea sin fuente."),
        ex("Texto leído en voz alta por un adulto: «La educadora dijo: «ko» es agua en mapuzugun. Se usa cuando hablamos del agua». ¿Qué significa «ko»?", "agua", "El texto dice que «ko» es agua."),
        ex("Mismo texto de la educadora y «ko». ¿En qué lengua está «ko»?", "mapuzugun", "El texto dice que «ko» es agua en mapuzugun."),
    ],
    Z=[
        ex("Sofía dice: «La educadora no vino, pero yo sé qué significa «kuyen»: es un pájaro». ¿Qué le falta a Sofía?", "una fuente", "Sin fuente su dato no está comprobado."),
        ex("Diego escribió: «Según la educadora, «antü» es sol. Yo creo que también es un cuento». ¿Cuál parte es el dato de la fuente?", "«antü» es sol", "Después de «yo creo» viene su opinión, no el dato."),
    ],
    D=[
        ex("Lees tres frases. 1) «Según el educador, «ruka» es casa.» 2) «Yo creo que «ruka» es un árbol.» 3) «La ficha dice que «mapu» es tierra.» ¿Cuáles vienen de una fuente? Escribe los números.", "1 y 3", "La frase 2 empieza con «yo creo»; las otras dicen quién da el dato."),
        ex("El adulto lee: «Esta palabra se usa en ciertos momentos. Eso lo explica la comunidad». ¿Quién puede explicarte esos momentos?", "la comunidad", "El texto dice que lo explica la comunidad."),
    ],
    context=[ex("En tu sala, una educadora tradicional enseña que «mari mari» es un saludo. Un compañero grita que es un nombre de planta. ¿Qué frase usas para corregir con respeto: «Según la educadora, es un saludo» o «Tú no sabes nada»?", "«Según la educadora, es un saludo»", "Dice la fuente con calma y sin ofender.")],
    selfcheck=[
        ex("¿Qué palabra uso para decir quién da un dato: según o quizás?", "según", "«Según» muestra de dónde viene el dato."),
        ex("¿Quién puede explicar qué quiere decir una expresión de su lengua?", "el educador tradicional o la comunidad", "Ellos conocen y cuidan su lengua."),
        ex("¿«Yo creo…» marca un dato de la fuente o una opinión mía?", "una opinión mía", "Lo que yo creo no es dato de la fuente."),
    ],
    task=T(
        "Lee esta ficha inventada: «La educadora de una escuela explicó: «mapu» es tierra en mapuzugun y «kuyen» es luna en mapuzugun». Escribe dos frases que empiecen con «Según la educadora,…», una para «mapu» y otra para «kuyen». Después escribe una frase con «Yo creo…» sobre lo que te gustaría preguntarle.",
        "Según la educadora, «mapu» es tierra en mapuzugun. Según la educadora, «kuyen» es luna en mapuzugun. Yo creo que me gustaría preguntarle cuándo se usan.",
        ["usa «según» para los dos datos de la fuente", "no cambia los significados de la ficha", "separa su opinión con «yo creo»"],
        ["frases escritas en el cuaderno", "frases dichas en voz alta"],
        ["escribir un significado que la ficha no dice", "poner su opinión como dato de la educadora"],
        "Valora que separó dato y opinión; si mezcló ambos, muéstrale la diferencia entre «según…» y «yo creo…».",
    ),
    reinforce="Con un adulto, practica decir en voz alta «Según la ficha, «mari mari» es un saludo en mapuzugun».",
    extend="Escribe dos frases sobre tu familia: una que empiece con «Según mi abuelo o abuela…» y otra con «Yo creo…». Observa la diferencia.",
)

L(
    LR3, 3,
    materials="Lápiz y hoja. Las fichas y los textos están escritos aquí. Los personajes son inventados para practicar.",
    use="Aprenderé a relacionar una palabra en lengua indígena con una situación de la vida diaria. Sirve para entender por qué las lenguas están ligadas a lo que las personas viven.",
    prior=["Sé qué es una expresión en lengua indígena.", "Sé separar el dato de la fuente de mi opinión."],
    explain=[
        "Las palabras no son solo sonidos. Se usan en momentos de la vida: al llegar, al comer, al agradecer o al cuidar el agua. Cuando relaciono una palabra con una situación, entiendo mejor para qué sirve.",
        "En mapuzugun, «ko» es agua, «antü» es sol, «kuyen» es luna, «ruka» es casa, «mapu» es tierra y «ñuke» es madre. Son palabras de la vida diaria: el agua que bebemos, el sol del día, la luna de la noche y la casa donde vivimos.",
        "Para relacionar, hago una pregunta sencilla: ¿en qué situación de mi día aparece esto? Si la situación es la misma que dice el texto, la palabra calza. Pero no invento usos ceremoniales ni espirituales: eso lo explica la comunidad.",
    ],
    vocab=[("situación", "momento o hecho de la vida diaria"), ("relacionar", "unir dos cosas que tienen que ver"), ("vida diaria", "lo que hacemos todos los días"), ("calzar", "ser la pareja correcta de algo"), ("uso", "para qué o cuándo se dice o se hace algo")],
    worked=[
        W("Unir palabra y situación", FICHA_PAL + " Situación: Pedro se sirve un vaso de agua. ¿Qué palabra de la ficha se relaciona?", ["Leo la situación: toma agua.", "En la ficha, «ko» es agua.", "Une la situación con «ko»."], "«ko»"),
        W("Una situación de la noche", FICHA_PAL + " Situación: Rosa mira la luna por la ventana antes de dormir. ¿Qué palabra se relaciona?", ["Miro qué cosa se menciona: la luna.", "La ficha dice que «kuyen» es luna.", "Une la situación con «kuyen»."], "«kuyen»"),
    ],
    mistakes=[
        M("Unir la palabra solo por cómo suena.", "Dos palabras pueden sonar distinto y yo no sé su significado.", "Uno la palabra con la situación usando lo que dice la ficha."),
        M("Inventar un uso especial de la palabra.", "No sé si ese uso existe en la comunidad.", "Solo digo lo que dice la ficha; el resto lo pregunto."),
    ],
    R=[
        ex(FICHA_PAL + " ¿Qué quiere decir «antü»?", "sol", "La ficha dice que «antü» es sol."),
        ex(FICHA_PAL + " ¿Cuál palabra quiere decir casa: «ruka» o «mapu»?", "ruka", "La ficha dice que «ruka» es casa."),
        ex(FICHA_PAL + " ¿Qué palabra se relaciona con la luna?", "kuyen", "La ficha dice que «kuyen» es luna."),
    ],
    C=[
        ex(FICHA_PAL + " Situación: una niña riega plantas con agua. ¿Qué palabra se relaciona con lo que usa para regar?", "ko", "Lo que usa para regar es agua, y «ko» es agua."),
        ex(FICHA_PAL + " Verdadero o falso: «ñuke» es una palabra para nombrar a la madre.", "Verdadero", "La ficha dice que «ñuke» es madre."),
        ex(FICHA_PAL + " ¿Qué palabra se relaciona con el suelo donde crece un árbol?", "mapu", "«Mapu» es tierra, y el árbol crece en la tierra."),
    ],
    A=[
        ex(FICHA_PAL + " Une cada situación con su palabra. 1) Sale el sol y empieza el día. 2) Entro a mi casa. Escribe las dos palabras en orden.", "antü, ruka", "El sol es «antü» y la casa es «ruka»."),
        ex(FICHA_PAL + " Texto inventado: «Mi mamá me abraza antes de dormir». ¿Qué palabra se relaciona con mi mamá?", "ñuke", "Mamá es madre y «ñuke» es madre."),
        ex(FICHA_PAL + " Situación: de noche veo la luna llena sobre el cerro. ¿Qué palabra de la ficha nombra lo que veo en el cielo?", "kuyen", "Lo que se ve en el cielo de noche es la luna, «kuyen»."),
    ],
    Z=[
        ex("Tomás dice: «La palabra «ko» sirve para nombrar el sol, porque suena fuerte». ¿Tiene razón según la ficha?", "No", "La ficha dice que «ko» es agua, no sol."),
        ex(FICHA_PAL + " Lucía cuenta que «antü» se usa en una ceremonia secreta. ¿Qué debes decirle: «lo dice la ficha» o «eso lo explica la comunidad»?", "eso lo explica la comunidad", "La ficha no habla de ceremonias; eso lo cuida la comunidad."),
    ],
    D=[
        ex(FICHA_PAL + " Lee: «Al amanecer, el ____ ilumina la ____ donde vivo». Completa con dos palabras de la ficha: una que sea sol y otra que sea casa.", "antü, ruka", "El sol es «antü» y la casa es «ruka»."),
        ex(FICHA_PAL + " Hay 6 palabras en la ficha. Si ya relacioné 4 con una situación, ¿cuántas me faltan?", "2", "6 − 4 = 2 palabras faltan por relacionar."),
    ],
    context=[ex(FICHA_PAL + " Tu familia cena y hay una jarra de agua en la mesa. ¿Qué palabra de la ficha usarías para nombrar lo que hay en la jarra?", "ko", "En la jarra hay agua, y «ko» es agua.")],
    selfcheck=[
        ex("¿Con qué relaciono una palabra para entender para qué sirve?", "con una situación", "La situación muestra cuándo se usa."),
        ex("¿Dónde veo lo que significa «kuyen» en esta clase?", "en la ficha", "La ficha dice que es luna."),
        ex("Si me preguntan por un uso ceremonial de una palabra, ¿qué respondo?", "eso lo explica la comunidad", "No invento usos que no conozco."),
    ],
    task=T(
        "Usa la ficha de palabras (ko, antü, kuyen, ruka, mapu, ñuke) y elige tres. En tu cuaderno haz tres filas: la palabra en mapuzugun, su significado según la ficha y una situación de tu día en que aparece lo que nombra. Por ejemplo, ko con tomar agua en el recreo. Al final escribe una pregunta para la educadora tradicional.",
        "ko = agua: tomo agua en el recreo. ruka = casa: llego a mi casa a las cinco. antü = sol: salgo al patio con sol. Pregunta: ¿cómo se dice «agua fría»?",
        ["escribe tres palabras de la ficha", "el significado coincide con la ficha", "cada situación tiene que ver con la palabra", "formula una pregunta para la educadora"],
        ["tabla de tres filas", "dibujo de las tres situaciones"],
        ["cambiar el significado de la ficha", "inventar un uso ritual"],
        "Reconoce la relación entre palabra y vida diaria; si inventó un significado, remítelo a la ficha o a la educadora tradicional.",
    ),
    reinforce="Mira tu casa y nombra tres cosas. Después busca en la ficha cuál de ellas tiene su palabra en mapuzugun.",
    extend="Cuenta a alguien de tu familia tres palabras de la ficha y en qué situación del día aparecen.",
)

L(
    LR3, 4,
    materials="Lápiz y hoja. Las fichas con las formas de escribir están en este cuaderno.",
    use="Aprenderé que una misma palabra de una lengua indígena puede escribirse de más de una manera. Sirve para respetar las fuentes sin decir que una forma es «mala».",
    prior=["Sé que una palabra tiene letras en cierto orden.", "Sé que debo nombrar la fuente."],
    explain=[
        "Muchas lenguas indígenas se hablaron durante siglos sin escribirse como el castellano. Hoy hay varias formas de escribirlas. Por eso una misma palabra puede verse distinta en dos libros, y los dos pueden ser válidos.",
        "Por ejemplo, la casa mapuche se puede ver escrita «ruka» o «ruca». El árbol que da piñones se puede ver como «pewen» o «pehuén». La lengua del pueblo mapuche se ve como «mapuzugun» o «mapudungun». Son variantes de escritura.",
        "Cuando registro una palabra, anoto la forma que vi y la fuente donde la vi. No digo «esta es la única correcta». Si dos fuentes escriben distinto, anoto las dos y pregunto al educador o a la educadora tradicional qué forma usa su comunidad.",
    ],
    vocab=[("variante", "otra forma de escribir o decir la misma palabra"), ("registrar", "anotar algo para recordarlo"), ("escritura", "forma de poner una palabra en letras"), ("válida", "que se puede aceptar"), ("comunidad", "grupo de personas que comparte una cultura")],
    worked=[
        W("Dos escrituras", "La fuente A escribe «ruka» y la fuente B escribe «ruca». Las dos hablan de la casa mapuche. ¿Cuál es la correcta?", ["Veo que las dos hablan de lo mismo.", "Las dos son escrituras usadas en fuentes distintas.", "No elijo una; anoto ambas con su fuente."], "las dos son variantes; anoto ambas con su fuente"),
        W("Registrar con fuente", "Vi «pehuén» en un libro de la biblioteca y «pewen» en un cartel de mi escuela. ¿Cómo lo anoto?", ["Escribo las dos formas.", "Al lado de cada una anoto dónde la vi.", "Dejo una pregunta para el educador."], "pehuén (libro), pewen (cartel); pregunta pendiente"),
    ],
    mistakes=[
        M("Tachar una variante diciendo que está «mal escrita».", "Puede ser otra forma válida de escribirla.", "Anoto las dos y pregunto qué usa la comunidad."),
        M("Registrar la palabra sin decir dónde la vi.", "Después nadie sabe de qué fuente salió.", "Escribo siempre «Fuente: …» junto a la palabra."),
    ],
    R=[
        ex("La casa mapuche se escribe «ruka» o «ruca». ¿Son la misma palabra con dos formas?", "Sí", "Ambas nombran la casa y son dos escrituras."),
        ex("¿Cómo se llama otra forma de escribir la misma palabra: variante o error?", "variante", "Una variante es otra forma de escribir o decir lo mismo."),
        ex("Al registrar una palabra, ¿qué anoto además de la palabra: la fuente o mi color favorito?", "la fuente", "La fuente dice de dónde salió la palabra."),
    ],
    C=[
        ex("El árbol de los piñones se ve escrito «pewen» y «pehuén». ¿Cuántas formas de escritura hay?", "2", "Hay «pewen» y «pehuén»: dos formas."),
        ex("Verdadero o falso: si una palabra se escribe distinto en dos libros, uno de los dos libros se equivocó siempre.", "Falso", "Pueden ser dos variantes válidas de escritura."),
        ex("La lengua mapuche se ve como «mapuzugun» y «mapudungun». ¿Qué hago con las dos formas?", "las anoto con su fuente", "No decido cuál sobra; registro ambas."),
    ],
    A=[
        ex("Anota en una línea esta información: vi «kuyen» en un cartel de la escuela. Elige: A) «kuyen» (Fuente: cartel de la escuela). B) «kuyen».", "A", "A incluye la fuente; B no."),
        ex("Dos fuentes: libro de la biblioteca dice «copihue» y la ficha de la comunidad dice «kopiwe». ¿Cuántas formas debo anotar?", "2", "Anoto las dos formas y la fuente de cada una."),
        ex("Una fuente escribe «ruka» y otra «ruca» para la casa. ¿Qué pregunta es mejor al educador: «¿Cuál es la correcta?» o «¿Qué forma usa su comunidad?»?", "¿Qué forma usa su comunidad?", "Esa pregunta respeta la variante sin juzgar."),
    ],
    Z=[
        ex("Camila dijo: «Mi libro escribe «ruca», así que «ruka» está mal». ¿Tiene razón? Responde Sí o No.", "No", "«Ruka» es otra escritura usada en otras fuentes."),
        ex("Si un cartel de la escuela y un libro escriben distinto una palabra, ¿por qué es útil anotar la fuente de cada uno?", "para saber de dónde salió cada forma", "La fuente explica por qué hay dos formas."),
    ],
    D=[
        ex("Ordena los pasos para registrar: A) pregunto qué usa su comunidad B) anoto la palabra y su fuente C) veo la palabra escrita de dos formas. Escribe las letras.", "C, B, A", "Primero veo, luego anoto y al final pregunto."),
        ex("Tienes 3 palabras con 2 formas cada una: «ruka/ruca», «pewen/pehuén», «mapuzugun/mapudungun». ¿Cuántas formas anotas en total?", "6", "3 palabras × 2 formas = 6 formas."),
    ],
    context=[ex("Tu curso hace un cartel y un niño escribe «mapudungun» pero la ficha del educador dice «mapuzugun». ¿Qué propones: borrar una o preguntarle al educador qué forma usar en el cartel?", "preguntarle al educador qué forma usar", "La comunidad decide cómo escribir su lengua en el cartel.")],
    selfcheck=[
        ex("¿Cómo se llama otra forma válida de escribir una palabra?", "variante", "Variante es otra forma de escribir lo mismo."),
        ex("¿Qué dato anoto junto a la palabra que registro?", "la fuente", "Así sé de dónde la saqué."),
        ex("¿Puedo decir que una variante es «la única correcta»?", "No", "Pueden existir varias formas válidas."),
    ],
    task=T(
        "Completa esta tabla en tu cuaderno con las dos formas de cada palabra y su fuente inventada para practicar: 1) casa: «ruka» (libro de la biblioteca) y «ruca» (cartel de la escuela). 2) árbol de piñones: «pewen» (ficha de la clase) y «pehuén» (cuento del curso). Después elige una palabra y escribe una pregunta para el educador tradicional sobre qué forma usa su comunidad.",
        "Casa: ruka (libro) / ruca (cartel). Árbol: pewen (ficha) / pehuén (cuento). Pregunta: ¿qué forma de «pewen» usan en su comunidad?",
        ["anota las dos formas de cada palabra", "incluye la fuente", "no dice que una forma es incorrecta", "pregunta al educador tradicional"],
        ["tabla de registro", "pregunta escrita o dicha en voz alta"],
        ["tachar una variante", "olvidar la fuente"],
        "Reconoce que registró variantes con fuente; si descartó una, invítalo a anotar ambas y preguntar a quien enseña la lengua.",
    ),
    reinforce="Escribe «ruka» y «ruca» una al lado de la otra y di con tus palabras por qué las dos pueden ser válidas.",
    extend="Busca en casa dos etiquetas o carteles que escriban distinto una misma palabra del castellano y anota qué diferencia ves.",
)

L(
    LR3, 5,
    materials="Lápiz y hoja. Las situaciones están escritas en este cuaderno.",
    use="Aprenderé qué significa revitalizar una lengua y qué puedo hacer yo para ayudar con respeto. Sirve para cuidar las lenguas de los pueblos originarios.",
    prior=["Sé separar el dato de la fuente de mi opinión.", "Sé que una palabra puede tener variantes de escritura."],
    explain=[
        "Una lengua se mantiene viva cuando las personas la usan. Hay lenguas indígenas que hablan pocas personas, por distintas razones que vienen de la historia. Hoy muchas comunidades trabajan para recuperarlas. A eso se le llama revitalizar una lengua.",
        "Yo también puedo ayudar, pero con respeto. Puedo escuchar al educador o a la educadora tradicional, aprender sus palabras y usarlas como me enseñen. Puedo pedir permiso antes de grabar o copiar. Puedo contar a mi familia lo que aprendí y nombrar siempre a la fuente.",
        "Hay cosas que no ayudan: burlarse del acento, cambiar las palabras para que sean «más fáciles», inventar significados o usar la lengua como un chiste. Ayudar es aprender de quien sabe y cuidar lo que aprendo.",
    ],
    vocab=[("revitalizar", "ayudar a que una lengua vuelva a usarse y a vivir"), ("hablante", "persona que habla una lengua"), ("aporte", "algo que pongo para ayudar"), ("respeto", "tratar con cuidado lo que importa a otros"), ("burla", "reírse de alguien para hacerle daño")],
    worked=[
        W("Elegir una acción que ayuda", "Acciones: A) preguntar al educador cómo se dice «gracias» en mapuzugun B) reírme del acento de una compañera. ¿Cuál ayuda a revitalizar?", ["Reviso cada acción: A aprende de quien sabe.", "B es una burla y daña.", "Elijo la que aprende y cuida."], "A"),
        W("Agradecer con la palabra", "La ficha dice que «chaltumay» es «gracias» en mapuzugun. La educadora enseñó la palabra a mi curso. ¿Qué puedo hacer al terminar la clase?", ["Recuerdo que la educadora nos enseñó la palabra.", "Puedo agradecerle con la palabra que enseñó.", "Digo «chaltumay» y la miro con respeto."], "agradecerle con «chaltumay»"),
    ],
    mistakes=[
        M("Pensar que ayudo si cambio las palabras para que sean más fáciles.", "Cambiar las palabras puede hacer perder la forma de la lengua.", "Uso las palabras como las enseña el educador tradicional."),
        M("Grabar o copiar a alguien sin pedir permiso.", "La voz y el saber de las personas se cuidan.", "Primero pregunto si puedo y para qué."),
    ],
    R=[
        ex("¿Qué palabra significa «ayudar a que una lengua vuelva a usarse»: revitalizar o apagar?", "revitalizar", "Revitalizar es darle vida de nuevo a una lengua."),
        ex("¿Quién enseña mejor una lengua indígena: el educador tradicional o alguien que la inventa?", "el educador tradicional", "El educador conoce la lengua de verdad."),
        ex("Decir «gracias» con una palabra que me enseñaron, ¿es una forma de respeto?", "Sí", "Uso lo aprendido y reconozco a quien lo enseñó."),
    ],
    C=[
        ex("Verdadero o falso: reírme del acento de alguien que habla una lengua indígena ayuda a que la lengua viva.", "Falso", "La burla daña y hace que las personas no quieran hablar."),
        ex("Una lengua tiene pocos hablantes. ¿Qué quiere decir eso: que muchas o que pocas personas la hablan?", "pocas", "Pocos hablantes significa que pocas personas la hablan."),
        ex("Elige la acción que cuida: A) pedir permiso antes de grabar B) grabar a escondidas.", "A", "Pedir permiso respeta a la persona y su saber."),
    ],
    A=[
        ex("Tu curso tiene tres acciones: 1) escuchar a la educadora 2) inventar un significado 3) contar a mi familia lo que aprendí con la fuente. ¿Cuáles ayudan? Escribe los números.", "1 y 3", "Escuchar y compartir con fuente ayuda; inventar no."),
        ex("Aprendiste 3 palabras nuevas con el educador y cada día repasas 1 con tu familia. ¿En cuántos días repasas las 3?", "3", "Una palabra por día durante 3 días."),
        ex("Quieres decir «gracias» a la educadora con una palabra de la ficha. Ficha: «chaltumay» es gracias en mapuzugun. ¿Qué dices?", "chaltumay", "La ficha dice que esa es la palabra para agradecer."),
    ],
    Z=[
        ex("Un compañero dice: «Mejor cambio la palabra para que me salga más fácil». ¿Qué le respondes: que la use como la enseña el educador o que la cambie?", "que la use como la enseña el educador", "El educador conoce la forma de su lengua."),
        ex("¿Por qué ayuda que muchas personas escuchen con respeto a quienes hablan una lengua indígena?", "porque los hablantes quieren seguir usándola", "El respeto anima a seguir hablándola."),
    ],
    D=[
        ex("Sigues una regla de 3 pasos: 1) pedir permiso 2) escuchar 3) agradecer. Si ya hiciste los pasos 1 y 2, ¿cuál te falta?", "agradecer", "Faltan los pasos que no hiciste: el tercero."),
        ex("Dos niños proponen: A) hacer un cartel con palabras que enseñó el educador y su nombre como fuente B) hacer un cartel con palabras inventadas. ¿Cuál es mejor para revitalizar?", "A", "Usa palabras reales y nombra la fuente."),
    ],
    context=[ex("En el recreo un niño imita con burla la forma de hablar de una visita que dijo «mari mari». ¿Qué le dices: «Eso no ayuda; mejor aprendamos con respeto» o «Sigue, es gracioso»?", "«Eso no ayuda; mejor aprendamos con respeto»", "La burla no ayuda a que una lengua viva.")],
    selfcheck=[
        ex("¿Qué es revitalizar una lengua?", "ayudar a que vuelva a usarse", "Es darle vida de nuevo."),
        ex("Nombra una acción que ayuda a revitalizar con respeto.", "escuchar al educador tradicional", "Aprender de quien sabe cuida la lengua."),
        ex("¿Debo pedir permiso antes de grabar la voz de otra persona?", "Sí", "La voz y el saber de las personas se cuidan."),
    ],
    task=T(
        "Escribe en tu cuaderno una tarjeta con tres compromisos para ayudar a una lengua indígena. Elige tres de estos: A) Escuchar al educador/a tradicional con atención. B) Usar las palabras como las enseña. C) Pedir permiso antes de grabar o copiar. D) Contar a mi familia lo que aprendí y nombrar a la fuente. E) No reírme de cómo habla alguien. Escribe cada compromiso con tus palabras y dibuja uno.",
        "Compromisos: 1) Escuchar al educador con atención. 2) Pedir permiso antes de grabar. 3) No reírme de cómo habla alguien. Dibujo: yo escuchando a la educadora.",
        ["elige tres compromisos de la lista", "los escribe con sus palabras", "los compromisos cuidan a las personas y a la lengua", "agrega un dibujo"],
        ["tarjeta escrita y dibujo", "compromisos dichos en voz alta"],
        ["escribir un compromiso que no cuida a nadie", "copiar la lista sin explicar con sus palabras"],
        "Reconoce que sus compromisos protegen a la lengua y a las personas; si propuso cambiar palabras o inventar, aclara que lo enseña la comunidad.",
    ),
    reinforce="Di en voz alta dos acciones que ayudan a revitalizar una lengua y una que no ayuda.",
    extend="Invita a alguien de tu casa a escuchar contigo, con respeto, un saludo en lengua indígena que aprendiste en clase.",
)

# =================================================================== LR04 · escritura de palabras y frases en lengua indígena
L(
    LR4, 1,
    materials="Lápiz, goma y hoja con líneas. Las palabras modelo están escritas en este cuaderno.",
    use="Aprenderé a copiar con cuidado una palabra en lengua indígena, letra por letra. Sirve para escribir con respeto lo que otros me enseñan.",
    prior=["Sé escribir letras y palabras en castellano.", "Sé contar hasta 20."],
    explain=[
        "Escribir una palabra en lengua indígena es una tarea de cuidado. Primero miro el modelo. El modelo es la palabra escrita por una fuente confiable, como la ficha del educador o la educadora. Luego copio letra por letra, sin cambiar ninguna.",
        "Las palabras de estas fichas son: «mari mari», «chaltumay», «iorana», «maururu», «pewen» y «ruka». Cada una tiene letras en un orden. Si cambio una letra, la palabra cambia. Por eso cuento las letras y reviso al final que mi copia sea igual al modelo.",
        "No sé pronunciar bien todas estas palabras y no pasa nada: la pronunciación la enseña el educador o la educadora. Mi tarea hoy es copiar sin errores y decir qué modelo usé.",
    ],
    vocab=[("modelo", "palabra escrita por la fuente que yo copio"), ("copiar", "escribir igual que el modelo"), ("letra", "cada signo con que se escribe una palabra"), ("revisar", "mirar otra vez para encontrar errores"), ("orden", "lugar que ocupa cada letra")],
    worked=[
        W("Contar las letras", "Modelo: «ruka». ¿Cuántas letras tiene?", ["Separo las letras: r, u, k, a.", "Cuento una por una: 1, 2, 3, 4.", "La palabra tiene cuatro letras."], "4"),
        W("Revisar una copia", "Modelo: «iorana». Mi copia: «iorama». ¿Qué letra cambió?", ["Comparo letra por letra: i, o, r, a, n, a.", "Mi copia: i, o, r, a, m, a.", "La quinta letra cambió: n por m."], "la n cambió por m"),
    ],
    mistakes=[
        M("Copiar rápido y cambiar una letra.", "Escribí de memoria y no miré el modelo.", "Miro el modelo y toco cada letra con el lápiz mientras copio."),
        M("Poner tildes o letras que el modelo no tiene.", "Quise que la palabra se parezca al castellano.", "Copio exactamente lo que dice el modelo."),
    ],
    R=[
        ex("Modelo: «ruka». ¿Cuál es la primera letra?", "r", "La palabra «ruka» empieza con r."),
        ex("Modelo: «pewen». ¿Cuántas letras tiene la palabra?", "5", "p, e, w, e, n son cinco letras."),
        ex("Modelo: «iorana». ¿Cuál es la última letra?", "a", "La palabra «iorana» termina con a."),
    ],
    C=[
        ex("Modelo: «maururu». Copias: A) maururu B) maurruru C) maururu. ¿Cuál copia es igual al modelo?", "A", "A tiene las mismas letras y en el mismo orden."),
        ex("Verdadero o falso: al copiar puedo cambiar una letra si me parece parecida.", "Falso", "Si cambio una letra, la palabra cambia."),
        ex("Modelo: «chaltumay». Copia de Ana: «chaltumai». ¿Qué letra cambió?", "la y por i", "La última letra del modelo es y y Ana escribió i."),
    ],
    A=[
        arith("Modelo: «mari mari». Cada palabra «mari» tiene 4 letras. ¿Cuántas letras tiene la expresión completa sin contar el espacio?", "4+4", "Son dos palabras de cuatro letras."),
        ex("Modelo: «iorana». Cuenta cuántas veces aparece la letra a.", "2", "i-o-r-a-n-a: la a está en la posición 4 y la 6."),
        ex("Modelo: «maururu». Cuenta cuántas veces aparece la letra u.", "3", "m-a-u-r-u-r-u: hay una u en la 3.ª, una en la 5.ª y una en la 7.ª posición."),
    ],
    Z=[
        ex("Pedro copió «ruka» como «ruca». Su modelo dice «ruka». ¿Está bien su copia respecto del modelo? Responde Sí o No.", "No", "Hoy el modelo manda: la copia debe ser igual al modelo."),
        ex("Dos copias del modelo «pewen»: A) pewen B) peuen. ¿Cuál es mejor y por qué?", "A, porque es igual al modelo", "En B cambió la w por u."),
    ],
    D=[
        ex("Las letras k, a, u, r están desordenadas. Si ordenas la palabra modelo «ruka», ¿en qué orden van?", "r, u, k, a", "El modelo «ruka» empieza con r, sigue u, luego k y termina con a."),
        ex("Modelo: «mari mari». Copia: «marimari». ¿Qué le falta a la copia?", "el espacio entre las dos palabras", "El modelo tiene dos palabras separadas por un espacio."),
    ],
    context=[ex("La educadora te muestra la palabra «chaltumay» en una tarjeta para que la copies en tu cuaderno. ¿Cuántas letras tendrá tu copia si la copias bien?", "9", "c, h, a, l, t, u, m, a, y son nueve letras.")],
    selfcheck=[
        ex("¿Qué miro mientras copio una palabra?", "el modelo", "Copio igual a lo que dice el modelo."),
        ex("¿Qué hago al terminar de copiar?", "reviso letra por letra", "Reviso para encontrar errores."),
        ex("¿Quién enseña cómo se pronuncia una palabra en lengua indígena?", "el educador tradicional", "La pronunciación la enseña quien conoce la lengua."),
    ],
    task=T(
        "Elige dos modelos de esta lista: «mari mari», «chaltumay», «iorana», «maururu», «ruka». Cópialos dos veces cada uno en tu cuaderno, con letra clara. Debajo de cada copia escribe cuántas letras tiene la palabra. Revisa letra por letra con el modelo y pinta con verde las copias que están iguales.",
        "ruka: ruka, ruka (4 letras). iorana: iorana, iorana (6 letras). Todas las copias están en verde.",
        ["copia dos modelos sin cambiar letras", "cuenta las letras de cada palabra", "revisa letra por letra"],
        ["cuaderno con las copias", "dibujo con colores de la revisión"],
        ["cambiar o agregar letras", "contar mal las letras"],
        "Reconoce que revisó letra por letra; si cambió una letra, pídele comparar con el modelo y corregir sin apuro.",
    ),
    reinforce="Copia la palabra «ruka» cuatro veces despacio y revisa cada una con el modelo.",
    extend="Con un adulto, cuenta cuántas letras tiene tu nombre y compáralo con las letras de «chaltumay».",
)

L(
    LR4, 2,
    materials="Lápiz y hoja. Las tarjetas modelo y los guiones para el adulto están escritos en este cuaderno.",
    use="Aprenderé que la forma de escribir una palabra viene de la fuente y que hay letras especiales que se copian tal cual. Sirve para escribir bien lo que me enseñan.",
    prior=["Sé copiar una palabra letra por letra.", "Sé qué es una fuente."],
    explain=[
        "El modelo que copio viene de una fuente: la educadora, un libro o una ficha. Yo no cambio el modelo. Si la fuente escribe una palabra de cierta manera, la copio de esa manera y anoto quién me la dio.",
        "En las palabras mapuzugun de esta ficha hay letras especiales. En «antü» hay una ü con dos puntos. En «ñuke» hay una ñ. No es lo mismo escribir «ñuke» que «nuke», ni «antü» que «antu». Si el modelo trae esa letra, la copio igual.",
        "A veces un adulto me lee la palabra en voz alta. Yo escucho y miro la tarjeta modelo para escribirla igual. Escuchar y mirar juntos ayuda. Si no estoy segura de una letra, pregunto y no la invento.",
    ],
    vocab=[("fuente", "persona o material que me da el modelo"), ("ñ", "letra especial que tiene una virgulilla arriba"), ("ü", "letra u con dos puntos arriba"), ("tarjeta modelo", "papel con la palabra bien escrita"), ("letra especial", "letra que no siempre se usa en castellano")],
    worked=[
        W("Copiar una letra especial", "Tarjeta modelo de la educadora: «antü». ¿Cómo copio la última letra?", ["Miro la última letra del modelo: ü, con dos puntos.", "Pongo los dos puntos arriba de la u.", "Escribo «antü»."], "antü"),
        W("Escuchar y mirar", "El adulto lee: «ñuke». La tarjeta modelo dice «ñuke». ¿Con qué letra empiezo?", ["Miro la tarjeta: la primera letra es ñ.", "La ñ lleva una virgulilla arriba.", "Escribo «ñuke» con la ñ."], "con la ñ"),
    ],
    mistakes=[
        M("Escribir «antu» sin los dos puntos de la ü.", "Pensé que la ü era igual a la u.", "Miro el modelo y copio los dos puntos."),
        M("Cambiar la ñ por n.", "No vi la virgulilla.", "Toco la ñ del modelo con el dedo antes de escribirla."),
    ],
    R=[
        ex("Tarjeta modelo: «ñuke». ¿Con qué letra empieza?", "ñ", "La primera letra de «ñuke» es la ñ."),
        ex("Tarjeta modelo: «antü». ¿Qué letra tiene dos puntos arriba?", "ü", "La ü es la u con dos puntos."),
        ex("¿De dónde viene el modelo que copio: de la fuente o de mi imaginación?", "de la fuente", "El modelo lo da la educadora, la ficha o el libro."),
    ],
    C=[
        ex("Modelo: «ñuke». Copias: A) nuke B) ñuke C) ñuque. ¿Cuál es igual al modelo?", "B", "B tiene la ñ y las letras en el mismo orden."),
        ex("Modelo: «antü». Copias: A) antu B) antü. ¿Cuál es igual al modelo?", "B", "La ü lleva dos puntos en el modelo."),
        ex("Verdadero o falso: «ñuke» y «nuke» son la misma escritura.", "Falso", "La ñ es una letra distinta de la n."),
    ],
    A=[
        ex("El adulto lee: «kuyen». Tarjeta modelo: «kuyen». Escribe la palabra y cuenta sus letras.", "kuyen, 5 letras", "k, u, y, e, n son cinco letras."),
        ex("Tarjeta modelo: «ñuke». Cuenta cuántas letras tiene.", "4", "ñ, u, k, e son cuatro letras."),
        ex("Tarjeta modelo: «antü». ¿Cuántas letras tiene?", "4", "a, n, t, ü son cuatro letras."),
    ],
    Z=[
        ex("Sofía copió «antü» como «antu» y dijo: «Da igual». ¿Qué le dices: «Copia lo que dice el modelo» o «Tienes razón»?", "«Copia lo que dice el modelo»", "El modelo trae la ü y la copia debe respetarla."),
        ex("Si dudas de una letra del modelo, ¿cuál es mejor: preguntar a la fuente o inventarla?", "preguntar a la fuente", "Preguntar evita errores."),
    ],
    D=[
        ex("Modelos: «ñuke» (4 letras) y «antü» (4 letras). ¿Cuántas letras escribes si copias ambos una vez?", "8", "4 + 4 = 8 letras."),
        ex("Tienes tres tarjetas: «ñuke», «antü» y «kuyen». Solo una no tiene letras especiales. ¿Cuál es?", "kuyen", "«Ñuke» tiene ñ, «antü» tiene ü y «kuyen» no tiene letras especiales."),
    ],
    context=[ex("La educadora te pasa una tarjeta con «ñuke» para tu cartel de la sala. Escribes «nuke». ¿Qué corriges?", "la ñ", "La primera letra de «ñuke» es ñ, no n.")],
    selfcheck=[
        ex("¿Qué letra tiene una virgulilla arriba en «ñuke»?", "ñ", "La ñ lleva virgulilla."),
        ex("¿Quién me da el modelo para copiar?", "la fuente", "La fuente es quien escribe bien la palabra."),
        ex("Si el modelo lleva ü, ¿copio la ü o la cambio por u?", "copio la ü", "El modelo no se cambia."),
    ],
    task=T(
        "Lee este guion para un adulto: «Lea en voz alta, despacio: antü, ñuke, kuyen». Con las tarjetas modelo «antü», «ñuke» y «kuyen», copia cada palabra en tu cuaderno. Marca con un círculo la letra especial de cada una. Revisa que cada copia sea igual a su tarjeta y escribe «Fuente: tarjeta modelo».",
        "antü (círculo en ü), ñuke (círculo en ñ), kuyen (sin letra especial). Fuente: tarjeta modelo.",
        ["copia las tres palabras igual que el modelo", "marca las letras especiales", "anota la fuente"],
        ["cuaderno con las tres palabras", "dibujo con círculos en las letras especiales"],
        ["cambiar ü por u o ñ por n", "olvidar la fuente"],
        "Valora que copió las letras especiales y anotó la fuente; si cambió alguna, vuelve a mostrarle el modelo.",
    ),
    reinforce="Copia «ñuke» y «antü» tres veces cada una, dibujando bien la virgulilla y los dos puntos.",
    extend="Busca en tu casa un texto en castellano con la letra ñ y copia una palabra con ella.",
)

L(
    LR4, 3,
    materials="Lápiz y hoja. Las fichas y las frases modelo están escritas en este cuaderno.",
    use="Aprenderé a escribir una frase corta en castellano que lleve una palabra en lengua indígena, con un significado de mi vida diaria. Sirve para usar con respeto las palabras que aprendo.",
    prior=["Sé que una oración empieza con mayúscula y termina con punto.", "Sé copiar una palabra modelo."],
    explain=[
        "Una frase es un grupo de palabras que dice una idea. Puedo escribir una frase en castellano y poner dentro una palabra en lengua indígena entre comillas. Por ejemplo: «Mi abuela dice «ko» cuando habla del agua». Ahí «ko» es una palabra de la ficha y el resto está en castellano.",
        "Para que una frase se entienda, uso la palabra con el significado que dice la ficha. «Ko» es agua, «antü» es sol, «ruka» es casa y «ñuke» es madre. No cambio el significado ni invento un uso especial.",
        "Mi frase empieza con mayúscula y termina con punto. Copio la palabra indígena igual que el modelo. Después reviso tres cosas: que la palabra esté bien copiada, que el significado sea el de la ficha y que la frase tenga sentido.",
    ],
    vocab=[("frase", "grupo de palabras que dice una idea"), ("comillas", "signos « » que encierran una palabra"), ("mayúscula", "letra grande con que empieza una oración"), ("punto", "signo con que termina una oración"), ("sentido", "que la frase se entiende")],
    worked=[
        W("Completar una frase", FICHA_PAL + " Frase: «Bebí un vaso de «____»». ¿Qué palabra de la ficha falta?", ["La frase habla de beber un vaso.", "Se bebe agua.", "En la ficha, «ko» es agua."], "ko"),
        W("Revisar una frase", "Frase: «el sol se llama «antü»». Le falta algo al comienzo y al final. ¿Qué le falta?", ["La oración debe empezar con mayúscula: «El».", "Debe terminar con punto.", "La corrijo: «El sol se llama «antü».»"], "mayúscula al inicio y punto al final"),
    ],
    mistakes=[
        M("Usar la palabra indígena con otro significado.", "No leí la ficha y me imaginé el significado.", "Miro la ficha antes de escribir mi frase."),
        M("Olvidar la mayúscula y el punto.", "Pensé solo en la palabra especial.", "Reviso al final: mayúscula, palabra bien copiada, punto."),
    ],
    R=[
        ex("¿Con qué letra empieza una oración: mayúscula o minúscula?", "mayúscula", "Toda oración empieza con letra grande."),
        ex("¿Con qué signo termina una oración: punto o coma?", "punto", "La oración termina con punto."),
        ex(FICHA_PAL + " ¿Cuál palabra de la ficha significa «casa»?", "ruka", "La ficha dice que «ruka» es casa."),
    ],
    C=[
        ex(FICHA_PAL + " Frase: «En mi «ruka» hay mucha luz». ¿Qué significa «ruka» en esa frase?", "casa", "Según la ficha, «ruka» es casa."),
        ex("Verdadero o falso: puedo inventar un significado nuevo para «ñuke» si mi frase suena bonita.", "Falso", "Debo usar el significado de la ficha."),
        ex("Frase: «Mi «ñuke» me abraza». ¿Quién abraza según la frase (ficha: ñuke es madre)?", "mi madre", "«Ñuke» significa madre."),
    ],
    A=[
        ex(FICHA_PAL + " Completa la frase: «De noche veo la «____» en el cielo». Elige la palabra de la ficha que significa luna.", "kuyen", "La ficha dice que «kuyen» es luna."),
        ex(FICHA_PAL + " Ordena las palabras para formar una frase: «brilla» / «El» / «antü». Escribe la frase con «antü» entre comillas.", "El «antü» brilla.", "Empieza con mayúscula, tiene la palabra de la ficha y termina con punto."),
        ex(FICHA_PAL + " Elige la frase correcta: A) «Plantamos un árbol en la «mapu»». B) «Plantamos un árbol en el «ko»».", "A", "«Mapu» es tierra y el árbol se planta en la tierra."),
    ],
    Z=[
        ex("Juan escribió: mi ñuke me cuida (sin mayúscula, sin comillas en la palabra indígena y sin punto). ¿Cuántas cosas debe corregir?", "3", "Le faltan la mayúscula, las comillas en «ñuke» y el punto."),
        ex(FICHA_PAL + " Rocío escribió: «Tomo «antü» cuando tengo sed». ¿Está bien usada la palabra? Responde Sí o No.", "No", "«Antü» es sol; para la sed va «ko», que es agua."),
    ],
    D=[
        ex(FICHA_PAL + " Elige la frase bien escrita: A) mi «ruka» es pequeña B) Mi «ruka» es pequeña.", "B", "B empieza con mayúscula, tiene «ruka» entre comillas y termina con punto."),
        ex(FICHA_PAL + " La frase «Por la mañana el «____» sale y yo salgo al patio» se completa con la palabra del sol. ¿Cuál es?", "antü", "«Antü» es el sol, que sale por la mañana."),
    ],
    context=[ex(FICHA_PAL + " Tu profesora pide una frase para el cartel de la sala: «Cuidemos el ____ de nuestra escuela». Quieren la palabra mapuzugun para agua. ¿Cuál es?", "ko", "La ficha dice que «ko» es agua.")],
    selfcheck=[
        ex("¿Con qué signo empieza y con cuál termina mi frase?", "mayúscula y punto", "La oración empieza con letra grande y termina con punto."),
        ex("¿Qué miro antes de escribir la palabra indígena?", "la ficha", "La ficha dice su significado."),
        ex("¿Dónde puedo poner la palabra indígena dentro de una frase en castellano?", "entre comillas", "Las comillas la señalan."),
    ],
    task=T(
        "Usa la ficha de palabras (ko, antü, kuyen, ruka, mapu, ñuke). Escribe dos frases en castellano, cada una con una palabra distinta de la ficha entre comillas. Por ejemplo: «Mi «ñuke» me espera en la «ruka»». Revisa que cada frase tenga mayúscula, punto, la palabra bien copiada y el significado de la ficha. Dibuja la idea de una de tus frases.",
        "Frase 1: Hoy salió el «antü» sobre el patio. Frase 2: Tomo «ko» en el recreo. Dibujo: un sol sobre el patio.",
        ["escribe dos frases completas", "usa dos palabras distintas de la ficha", "respeta el significado", "mayúscula, punto y comillas"],
        ["cuaderno con las dos frases", "dibujo de una frase"],
        ["inventar otro significado", "copiar mal la palabra"],
        "Reconoce que usó el significado de la ficha y cuidó la escritura; si cambió el significado, vuelve a leer la ficha con él.",
    ),
    reinforce="Escribe una frase con «kuyen» y léela en voz alta a alguien de tu casa.",
    extend="Escribe tres frases cortas con tres palabras distintas de la ficha, cada una sobre algo de tu día.",
)

L(
    LR4, 4,
    materials="Lápiz y hoja. Las fichas de registro y las fuentes de práctica están escritas en este cuaderno.",
    use="Aprenderé a escribir una palabra o frase y registrar de dónde la copié, sin decir que una forma es la única correcta. Sirve para cuidar las variantes de cada lengua.",
    prior=["Sé que una palabra puede escribirse de más de una manera.", "Sé copiar un modelo letra por letra."],
    explain=[
        "Cuando escribo una palabra en lengua indígena, anoto tres datos: la palabra tal como la vi, la fuente donde la vi y la fecha en que la anoté. Eso se llama registro. El registro ayuda a que otras personas sepan de dónde salió lo que escribí.",
        "A veces dos fuentes escriben distinto. Por ejemplo, una escribe «mapuzugun» y otra «mapudungun». Si las dos son fuentes confiables, anoto las dos y no elijo una como «la mejor». Una comunidad puede preferir una forma, y esa decisión la toma ella.",
        "Con mi registro puedo hacer una pregunta clara: «¿Qué forma de escribir usa su comunidad?». Esa pregunta muestra interés y respeto. Así aprendo sin dejar fuera otras formas de escribir.",
    ],
    vocab=[("registro", "anotación con la palabra, la fuente y la fecha"), ("fecha", "día, mes y año en que anoté algo"), ("fuente confiable", "persona o material que cuida y conoce lo que dice"), ("preferir", "elegir una forma entre varias"), ("tal como", "igual a como está en el original")],
    worked=[
        W("Llenar un registro", "Vi la palabra «ruka» en una tarjeta de la educadora, hoy 12 de mayo. ¿Qué tres datos anoto?", ["Anoto la palabra tal como la vi: «ruka».", "Anoto la fuente: tarjeta de la educadora.", "Anoto la fecha: 12 de mayo."], "palabra «ruka»; fuente: tarjeta de la educadora; fecha: 12 de mayo"),
        W("Dos fuentes distintas", "El libro dice «mapuzugun» y el cartel dice «mapudungun». ¿Qué hago?", ["Veo que las dos hablan de la misma lengua.", "Anoto las dos formas con su fuente.", "Escribo la pregunta: ¿qué forma usa su comunidad?"], "anoto las dos con su fuente y pregunto"),
    ],
    mistakes=[
        M("Anotar solo la palabra y olvidar la fuente.", "Después no sé de dónde la copié.", "Uso siempre la ficha de registro de tres datos."),
        M("Copiar una sola forma y tachar la otra.", "Pensé que una variante sobra.", "Registro las dos y pregunto a la comunidad."),
    ],
    R=[
        ex("¿Cuántos datos tiene un registro: palabra, fuente y fecha?", "3", "Son tres: palabra, fuente y fecha."),
        ex("Si anoto de dónde copié una palabra, ¿qué dato estoy anotando: la fecha o la fuente?", "la fuente", "La fuente es de dónde viene la palabra."),
        ex("¿Qué es el registro: una anotación o un dibujo?", "una anotación", "Es la anotación con palabra, fuente y fecha."),
    ],
    C=[
        ex("Registro incompleto: «Palabra: kuyen. Fecha: 3 de junio». ¿Qué dato falta?", "la fuente", "Faltan los datos de dónde copié la palabra."),
        ex("Verdadero o falso: si dos fuentes escriben distinto, debo anotar solo una.", "Falso", "Anoto las dos con su fuente."),
        ex("Dos fuentes: «mapuzugun» y «mapudungun». ¿Cuántas formas debo registrar?", "2", "Registro cada forma con su fuente."),
    ],
    A=[
        ex("Ficha: «Palabra: pewen. Fuente: ____. Fecha: 8 de abril». Hoy la copié del cartel de la biblioteca. ¿Qué escribo en la fuente?", "cartel de la biblioteca", "La fuente es el cartel donde la copié."),
        ex("Dos registros: 1) «ruka», libro de la sala, 10 de mayo. 2) «ruca», cartel del pasillo, 10 de mayo. ¿Cuántas fuentes distintas hay?", "2", "El libro de la sala y el cartel del pasillo."),
        ex("Eliges la mejor pregunta para el educador: A) «¿Qué forma de «ruka» o «ruca» usa su comunidad?» B) «¿Cuál de las dos está mal?»", "A", "A pregunta con respeto; B juzga sin saber."),
    ],
    Z=[
        ex("Beto dice: «Elijo solo «mapuzugun» porque me gusta más». ¿Qué debería hacer en vez?", "registrar ambas y preguntar a la comunidad", "Elegir por gusto deja fuera otra forma válida."),
        ex("¿Por qué ayuda anotar la fecha en un registro?", "para saber cuándo lo copié", "La fecha muestra el momento en que anoté la palabra."),
    ],
    D=[
        ex("Hay 5 palabras para registrar y cada registro tiene 3 datos. ¿Cuántos datos escribes en total?", "15", "5 registros × 3 datos = 15 datos."),
        ex("Un registro dice: «Palabra: ruka. Fuente: tarjeta de la educadora». Otro dice: «Palabra: ruca. Fuente: libro de la biblioteca». ¿Qué letra cambia entre las dos formas?", "la k por c", "En «ruka» y «ruca» cambia la tercera letra; se registran ambas."),
    ],
    context=[ex("Tu curso copia «ruka» de una tarjeta de la educadora y «ruca» de un libro de la biblioteca. Quieren hacer un cartel. ¿Qué paso va primero: registrar las dos formas con su fuente o elegir la que más guste?", "registrar las dos formas con su fuente", "Primero se registra para no perder ninguna variante.")],
    selfcheck=[
        ex("¿Qué tres datos tiene un registro?", "palabra, fuente y fecha", "Esos tres datos forman el registro."),
        ex("Si veo dos formas de escribir una palabra, ¿las anoto las dos?", "Sí", "Anoto ambas y su fuente."),
        ex("¿A quién pregunto qué forma usa su comunidad?", "al educador tradicional", "El educador conoce lo que usa su comunidad."),
    ],
    task=T(
        "Haz un registro con estas fuentes de práctica. Fuente 1: tarjeta del educador (escribe «pewen»). Fuente 2: libro de la biblioteca (escribe «pehuén»). Crea una tabla con tres columnas: palabra, fuente y fecha de hoy. Escribe las dos formas y una pregunta: «¿Qué forma de pewen usa su comunidad?». Dibuja un árbol de piñones al lado.",
        "pewen | tarjeta del educador | hoy. pehuén | libro de la biblioteca | hoy. Pregunta: ¿qué forma de pewen usa su comunidad?",
        ["registra las dos formas", "anota fuente y fecha en cada una", "escribe la pregunta para la comunidad"],
        ["tabla de registro", "dibujo del árbol"],
        ["registrar solo una forma", "no anotar la fuente"],
        "Valora el registro con fuente; si descartó una forma, invítalo a anotarla y preguntar a la comunidad.",
    ),
    reinforce="Haz un registro de una sola palabra de la clase con los tres datos: palabra, fuente y fecha.",
    extend="Explica a alguien de tu casa por qué es mejor registrar dos formas de escribir una palabra y no tachar una.",
)

# =================================================================== LR05 · recursos tecnológicos para escuchar, ver y transcribir
L(
    LR5, 1,
    materials="Lápiz y hoja. Los casos y las fichas están escritos aquí. Si usas un aparato, siempre con un adulto de tu casa o de la escuela.",
    use="Aprenderé qué recursos tecnológicos sirven para escuchar, ver y escribir palabras en lengua indígena. Sirve para elegir bien y usar la tecnología con cuidado.",
    prior=["Sé que hay aparatos como computador, tablet, radio y grabadora.", "Sé qué es una fuente."],
    explain=[
        "Un recurso tecnológico es un aparato o programa que ayuda a hacer algo. Para escuchar usamos una radio, un parlante o una grabación de audio. Para ver usamos un video, una foto o una pantalla. Para transcribir usamos un cuaderno, un lápiz o un computador con un adulto.",
        "Transcribir es escribir lo que escucho o veo, igual a como está. Si escucho una palabra en lengua indígena, la escribo tal como la fuente la muestra en su texto o subtítulo. No la cambio para que me guste más.",
        "Siempre uso la tecnología con un adulto y con permiso. No pongo mi nombre, mi dirección ni fotos de personas. Y elijo recursos hechos o autorizados por la comunidad, la escuela o una institución conocida.",
    ],
    vocab=[("recurso tecnológico", "aparato o programa que ayuda a hacer algo"), ("audio", "sonido grabado que se escucha"), ("video", "imagen en movimiento que se ve en una pantalla"), ("transcribir", "escribir lo que escucho o veo tal como es"), ("autorización", "permiso para usar algo")],
    worked=[
        W("Elegir el recurso", "Quiero escuchar cómo una persona dice un saludo. ¿Qué recurso me sirve: audio o foto?", ["Escuchar usa el oído.", "Un audio tiene sonido; una foto no.", "Elijo el audio."], "audio"),
        W("Elegir para ver", "Quiero ver cómo una persona teje en un telar. ¿Qué me sirve mejor: radio o video?", ["Ver necesita imagen.", "La radio solo tiene sonido.", "Elijo el video."], "video"),
    ],
    mistakes=[
        M("Usar un aparato sin avisar a un adulto.", "Puedo abrir algo que no corresponde.", "Pido ayuda a un adulto antes de usarlo."),
        M("Escribir mis datos personales en una página.", "Esos datos son privados.", "No escribo nombre completo, dirección ni fotos."),
    ],
    R=[
        ex("Para escuchar un saludo en una lengua indígena, ¿necesito un audio o una pintura?", "un audio", "El audio tiene sonido."),
        ex("Para ver cómo se teje, ¿me sirve más un video o una radio?", "un video", "El video muestra imágenes en movimiento."),
        ex("¿Qué palabra significa «escribir lo que escucho tal como es»: transcribir o dibujar?", "transcribir", "Transcribir es escribir lo que escucho."),
    ],
    C=[
        ex("Verdadero o falso: puedo usar un computador a escondidas porque solo es para escuchar.", "Falso", "Debo usarlo con un adulto y con permiso."),
        ex("Un video muestra a una persona diciendo «iorana». ¿Qué recurso estoy usando: video o audio solamente?", "video", "Veo imagen y escucho sonido."),
        ex("¿Qué dato personal NO debo escribir en una página: mi nombre completo o la palabra «iorana»?", "mi nombre completo", "Los datos personales son privados."),
    ],
    A=[
        ex("Tienes que elegir recursos: 1) escuchar un saludo 2) ver una foto de un tejido 3) escribir lo que escuchaste. Une cada uno con audio, foto o cuaderno. Escribe la lista en orden.", "audio, foto, cuaderno", "Cada recurso sirve para esa tarea."),
        ex("Ves un video de 6 minutos. Ya viste 4 minutos. ¿Cuántos minutos faltan?", "2", "6 − 4 = 2 minutos faltan."),
        ex("Quieres transcribir la palabra «maururu» que escuchaste. ¿Con qué te ayudas: lápiz y cuaderno o pelota?", "lápiz y cuaderno", "Para escribir necesito lápiz y cuaderno."),
    ],
    Z=[
        ex("Marta dice: «Cualquier video sobre cultura sirve, aunque no diga quién lo hizo». ¿Tiene razón? Responde Sí o No.", "No", "Hay que saber quién lo hizo y si está autorizado."),
        ex("¿Por qué es mejor usar un recurso hecho o autorizado por la comunidad?", "porque cuida lo que ella quiere compartir", "La comunidad decide qué comparte."),
    ],
    D=[
        ex("En la escuela hay 3 audios y 2 videos autorizados. Escuchas 2 audios y ves 1 video. ¿Cuántos recursos te quedan?", "2", "5 recursos − 3 usados = 2."),
        ex("Un adulto te ofrece un video de internet sin nombre de autor. ¿Qué haces primero: verlo sin preguntar o preguntar quién lo hizo?", "preguntar quién lo hizo", "Primero verifico la fuente."),
    ],
    context=[ex("Tu profesora te muestra un audio de la escuela con la voz de la educadora tradicional diciendo «mari mari». Quieres escribirlo en tu cuaderno. ¿Qué recurso usas para escribir?", "cuaderno y lápiz", "El audio se escucha y se anota en el cuaderno.")],
    selfcheck=[
        ex("¿Qué es transcribir?", "escribir lo que escucho o veo tal como es", "Transcribir es escribir igual a lo escuchado."),
        ex("¿Con quién uso la tecnología: solo o con un adulto?", "con un adulto", "Siempre uso la tecnología acompañado."),
        ex("¿Qué datos personales no pongo en internet?", "mi nombre, dirección y fotos", "Esos datos son privados."),
    ],
    task=T(
        "Haz una tabla con tres filas en tu cuaderno. Fila 1: quiero escuchar un saludo (recurso: audio). Fila 2: quiero ver cómo se teje (recurso: video). Fila 3: quiero escribir lo que escuché (recurso: lápiz y cuaderno). Dibuja un aparato al lado de cada fila. Después escribe una regla para usar la tecnología con respeto.",
        "Escuchar: audio. Ver: video. Escribir: cuaderno. Regla: uso la tecnología con un adulto y no pongo datos personales.",
        ["une cada acción con un recurso", "dibuja un aparato en cada fila", "escribe una regla de cuidado"],
        ["tabla en el cuaderno", "dibujos de los aparatos"],
        ["usar un aparato sin adulto", "poner datos personales"],
        "Valora que unió acción y recurso y que escribió una regla de cuidado; si olvidó al adulto, recuérdalo con una pregunta.",
    ),
    reinforce="Nombra un recurso para escuchar, uno para ver y uno para escribir.",
    extend="Pregunta a alguien de tu casa qué aparatos usa para escuchar música o ver videos y cuáles usa con permiso.",
)

L(
    LR5, 2,
    materials="Lápiz y hoja. El guion de audio de práctica y la ficha de la fuente están escritos aquí. Un adulto lee el guion en voz alta, despacio.",
    use="Aprenderé a escuchar un audio y escribir las palabras, y a revisar que la fuente sea confiable. Sirve para anotar bien lo que escucho.",
    prior=["Sé qué es transcribir.", "Sé usar la tecnología con un adulto."],
    explain=[
        "Antes de escuchar un audio o ver un video, reviso la fuente. Una buena fuente dice quién lo hizo, de qué pueblo habla y para qué se grabó. Por ejemplo: una escuela, una radio comunitaria, un museo o una institución conocida. Si no dice nada, mejor pregunto a un adulto.",
        "Un audio puede tener la voz de una persona de la comunidad. Esa voz tiene dueño. Solo uso un audio si fue publicado para compartir o si tengo permiso de quien lo grabó. No lo cambio, no lo recorto ni lo uso en bromas.",
        "Al transcribir, escucho una parte pequeña, la pauso y escribo. Luego la escucho de nuevo para revisar. Si hay una palabra que no entiendo, dejo un espacio y pregunto. No escribo algo solo porque suena parecido.",
    ],
    vocab=[("autoría", "quién hizo un audio, video o texto"), ("pausar", "detener un audio o video por un momento"), ("autorizado", "que tiene permiso para compartirse"), ("institución", "grupo organizado, como una escuela o un museo"), ("voz", "sonido de una persona al hablar")],
    worked=[
        W("Revisar la fuente", "Ficha de práctica (inventada): «Audio de la escuela, grabado por la educadora tradicional con permiso del curso». ¿Quién hizo el audio?", ["Leo la ficha.", "Dice «grabado por la educadora tradicional».", "Ella es la autora."], "la educadora tradicional"),
        W("Transcribir con pausa", "Guion de práctica leído por un adulto: «iorana». Pauso, escucho y escribo. ¿Qué escribo?", ["Escucho la palabra completa.", "La pauso y miro la ficha: «iorana».", "Escribo «iorana» y la reviso."], "iorana"),
    ],
    mistakes=[
        M("Usar un audio sin saber quién lo grabó.", "Podría no tener permiso para compartirse.", "Reviso la autoría antes de usarlo."),
        M("Escribir lo que me imagino, no lo que escucho.", "Rellené una palabra que no entendí.", "Dejo un espacio y pregunto al adulto o a la fuente."),
    ],
    R=[
        ex("Antes de usar un audio, ¿qué reviso: la fuente o el color de la pantalla?", "la fuente", "La fuente dice quién lo hizo."),
        ex("¿Qué botón uso para detener un audio un momento: pausa o apagar?", "pausa", "Pausar detiene el audio sin perderlo."),
        ex("¿Cómo se llama quien hizo un audio: autor o ayudante?", "autor", "El autor es quien lo hizo."),
    ],
    C=[
        ex("Ficha: «Video de un museo regional, publicado para uso en escuelas». ¿Quién lo hizo?", "un museo regional", "La ficha dice que viene de un museo regional."),
        ex("Verdadero o falso: puedo recortar y cambiar la voz de una persona de la comunidad para hacer una broma.", "Falso", "Esa voz tiene dueño y se usa con respeto."),
        ex("Guion leído por un adulto: «maururu». Ficha: es gracias en rapa nui. ¿Qué escribo?", "maururu", "Escribo la palabra como está en la ficha."),
    ],
    A=[
        ex("Tres fichas: A) «Audio sin nombre ni fecha». B) «Audio de la escuela con permiso». C) «Video que subió un desconocido». ¿Cuál es la mejor fuente?", "B", "B dice quién lo hizo y que tiene permiso."),
        ex("Un audio dura 30 segundos y lo pausas cada 10 segundos para escribir. ¿Cuántas pausas haces si pausas al terminar cada trozo?", "3", "30 ÷ 10 = 3 trozos, con una pausa en cada uno."),
        ex("Guion de un adulto: «Escribe dos palabras: ko, antü». Ficha: ko es agua y antü es sol. ¿Cuál significa sol?", "antü", "La ficha dice que «antü» es sol."),
    ],
    Z=[
        ex("Pía escribe una palabra distinta a la del audio «porque suena parecido». ¿Está bien? Responde Sí o No.", "No", "Debo escribir lo que dice la fuente, no lo que me imagino."),
        ex("Ficha de práctica: «Radio comunitaria de una escuela rural, entrevista a un educador tradicional, con permiso». ¿Qué dato muestra que el audio es autorizado?", "con permiso", "La ficha dice que se grabó con permiso."),
    ],
    D=[
        ex("Escuchas 3 audios de 2 minutos cada uno. ¿Cuántos minutos escuchas en total?", "6", "3 audios × 2 minutos = 6 minutos."),
        ex("Una ficha dice: «audio sin autor, sin fecha y sin pueblo». ¿Qué tres datos le faltan?", "autor, fecha y pueblo", "La ficha no los trae."),
    ],
    context=[ex("Tu profesora pone un audio de práctica que dice: «iorana, maururu». La ficha dice que son palabras rapa nui. Te piden anotarlas. ¿Cuántas palabras anotas?", "2", "Son «iorana» y «maururu».")],
    selfcheck=[
        ex("¿Qué reviso antes de escuchar un audio?", "la fuente", "Veo quién lo hizo."),
        ex("Si no entiendo una palabra al transcribir, ¿qué hago?", "dejo un espacio y pregunto", "No escribo algo que no escuché."),
        ex("¿Puedo cambiar la voz de una persona sin su permiso?", "No", "Esa voz tiene dueño."),
    ],
    task=T(
        "Un adulto te lee este guion de audio de práctica: «iorana… maururu… mari mari». Fichas: «iorana» es un saludo en rapa nui, «maururu» es gracias en rapa nui y «mari mari» es un saludo en mapuzugun. Escribe las tres expresiones en tu cuaderno con su lengua al lado. Anota la fuente: «guion de práctica de la clase». Si no entendiste alguna, deja un espacio y escribe una pregunta.",
        "iorana (rapa nui), maururu (rapa nui), mari mari (mapuzugun). Fuente: guion de práctica de la clase.",
        ["transcribe las tres expresiones sin cambiarlas", "anota la lengua de cada una", "anota la fuente"],
        ["cuaderno con la transcripción", "pregunta escrita para el educador"],
        ["escribir algo que no escuchó", "olvidar la fuente"],
        "Reconoce que transcribió con la ficha y anotó la fuente; si inventó una palabra, pídele que deje un espacio y pregunte.",
    ),
    reinforce="Pide a un adulto que lea «maururu» y escríbela en tu cuaderno con su lengua.",
    extend="Pregunta a alguien de tu casa cómo reconoce que un video o un audio es confiable.",
)

L(
    LR5, 3,
    materials="Lápiz y hoja. La ficha de práctica y los guiones de video descritos están escritos aquí. Un adulto acompaña.",
    use="Aprenderé a ver y escuchar un video corto, relacionar las palabras con lo que se ve y transcribir sin cambiar nada. Sirve para aprender de la cultura con la mirada y el oído.",
    prior=["Sé elegir un recurso para escuchar o ver.", "Sé revisar la fuente."],
    explain=[
        "Un video une imagen y sonido. Eso ayuda a relacionar una palabra con lo que se ve. Por ejemplo, si veo agua en un río y escucho «ko», entiendo mejor que la palabra nombra el agua.",
        "Para aprender de un video hago tres pasos. Primero lo veo completo. Luego lo veo de nuevo por partes y lo pauso. Por último transcribo las palabras que aparecen en pantalla o que se dicen, sin cambiarlas, y anoto de qué fuente son.",
        "También puedo tomar notas de lo que veo, pero cuido las personas. No tomo fotos ni capturas de la pantalla con caras de otras personas sin permiso. Anoto con palabras y dibujos.",
    ],
    vocab=[("subtítulo", "texto que aparece en el video y dice lo que se habla"), ("nota", "anotación breve de algo que vi o escuché"), ("pantalla", "parte del aparato donde se ve el video"), ("captura", "foto de lo que se ve en la pantalla"), ("completo", "desde el comienzo hasta el final")],
    worked=[
        W("Relacionar imagen y palabra", "Video de práctica (descrito): se ve un río con agua clara; en pantalla aparece la palabra «ko», y la ficha dice que es agua en mapuzugun. ¿Qué nombra «ko»?", ["Veo un río con agua.", "La palabra «ko» aparece mientras se ve el agua.", "La ficha dice que «ko» es agua."], "el agua"),
        W("Transcribir sin cambiar", "En el video de práctica aparecen dos palabras en pantalla: «antü» y «kuyen». ¿Cómo las transcribo?", ["Leo cada palabra en la pantalla.", "Las copio igual: antü, kuyen.", "Anoto la fuente: video de práctica."], "antü, kuyen"),
    ],
    mistakes=[
        M("Ver el video una sola vez y escribir de memoria.", "Se me olvidan partes o cambio letras.", "Lo veo de nuevo por partes y lo pauso."),
        M("Hacer capturas de personas sin pedir permiso.", "Las imágenes de personas se cuidan.", "Anoto con palabras y dibujos, o pido permiso."),
    ],
    R=[
        ex("Un video muestra agua y aparece «ko». Según la ficha, ¿qué es «ko»?", "agua", "La ficha dice que «ko» es agua en mapuzugun."),
        ex("¿Qué muestra un subtítulo: lo que se dice o el color del video?", "lo que se dice", "El subtítulo escribe lo que se dice."),
        ex("¿Qué hago primero con un video: lo veo completo o lo recorto?", "lo veo completo", "Primero lo veo entero."),
    ],
    C=[
        ex("Verdadero o falso: puedo sacar fotos de la pantalla con la cara de una persona sin pedir permiso.", "Falso", "Las imágenes de personas se cuidan y se pide permiso."),
        ex("Video de práctica (descrito): sale el sol sobre un cerro y aparece «antü». Según la ficha, «antü» es sol. ¿Qué se ve en el video?", "el sol sobre un cerro", "La descripción dice eso."),
        ex("¿Qué hago para transcribir mejor: pauso y veo por partes o paso todo muy rápido?", "pauso y veo por partes", "Así no se me pasan letras ni palabras."),
    ],
    A=[
        ex("Video de práctica (descrito): aparece una casa de madera y la palabra «ruka». Ficha: «ruka» es casa. Escribe una nota con la palabra y lo que ves.", "ruka: casa de madera", "La nota une la palabra con la imagen."),
        ex("Un video de práctica dura 5 minutos y lo ves en partes de 1 minuto. ¿Cuántas partes ves?", "5", "5 ÷ 1 = 5 partes."),
        ex("Video de práctica (descrito): hay un telar y aparece el subtítulo «Gracias, maururu». Ficha: maururu es gracias en rapa nui. ¿Cuál palabra del subtítulo es rapa nui?", "maururu", "La ficha dice que «maururu» es rapa nui."),
    ],
    Z=[
        ex("Hugo transcribió «antu» pero la pantalla decía «antü». ¿Qué debe revisar?", "los dos puntos de la ü", "La transcripción debe ser igual a la pantalla."),
        ex("¿Por qué es mejor anotar con palabras y dibujos que sacar fotos a personas?", "porque se cuida su imagen", "Las personas tienen derecho a decidir sobre su imagen."),
    ],
    D=[
        ex("Ves 4 palabras en pantalla y transcribes 3. ¿Cuántas faltan por transcribir?", "1", "4 − 3 = 1 palabra falta."),
        ex("Video de práctica (descrito): se ve el mar y la ficha dice «lafken» es mar. Un niño dice «lafken» es montaña. ¿Qué debes hacer: corregir con la ficha o aceptar?", "corregir con la ficha", "La ficha dice que «lafken» es mar."),
    ],
    context=[ex("Tu curso ve un video corto de la escuela. Aparecen las palabras «mapu» y «ko» con imágenes de tierra y de agua. La ficha dice mapu = tierra y ko = agua. ¿Qué palabra va con la imagen de la tierra?", "mapu", "La ficha dice que «mapu» es tierra.")],
    selfcheck=[
        ex("¿Qué hago con un video para transcribir bien?", "lo veo por partes y lo pauso", "Así copio sin errores."),
        ex("¿Puedo sacar capturas de caras de otras personas sin permiso?", "No", "Se cuida la imagen de las personas."),
        ex("¿Qué ayuda a relacionar una palabra con su significado en un video?", "la imagen", "Veo la imagen mientras escucho la palabra."),
    ],
    task=T(
        "Lee esta descripción de un video de práctica: «Se ve un río, luego sale el sol sobre un cerro y al final aparece la palabra «chaltumay» en pantalla». Fichas: «ko» es agua, «antü» es sol y «chaltumay» es gracias, en mapuzugun. En tu cuaderno haz una tabla de tres filas con lo que se ve y la palabra que se relaciona, y transcribe «chaltumay» igual que en la pantalla. Anota la fuente: video de práctica.",
        "Río: ko (agua). Sol: antü. Final: chaltumay = gracias. Fuente: video de práctica.",
        ["une cada imagen con su palabra", "transcribe «chaltumay» igual", "anota la fuente"],
        ["tabla en el cuaderno", "dibujo de las tres escenas"],
        ["cambiar el significado", "olvidar anotar la fuente"],
        "Reconoce que relacionó imagen y palabra con la ficha; si cambió un significado, vuelve a la ficha.",
    ),
    reinforce="Describe con palabras una escena del video de práctica y di qué palabra se relaciona.",
    extend="Explica a alguien de tu casa cómo se hace una transcripción en tres pasos: ver, pausar y escribir.",
)

L(
    LR5, 4,
    materials="Lápiz y hoja. La ficha de registro y las fuentes de práctica están escritas aquí. Un adulto acompaña si usas un aparato.",
    use="Aprenderé a guardar mis transcripciones con la fuente y la fecha, y a compartirlas con permiso. Sirve para cuidar lo que escucho y escribo.",
    prior=["Sé transcribir una palabra de un audio o video.", "Sé registrar con fuente y fecha."],
    explain=[
        "Cuando transcribo, anoto lo que escuché o vi tal como lo escuché o vi. A veces dos personas dicen o escriben una misma palabra de formas distintas. No elijo una como «la única». Anoto la forma que escuché y la fuente donde la escuché.",
        "Mi registro tiene cuatro datos: la palabra, la fuente, la fecha y el recurso. El recurso puede ser un audio, un video o un texto. Así otras personas pueden revisar mi trabajo. Si alguna parte no la entendí, escribo una pregunta.",
        "Antes de compartir mi trabajo con otros, pido permiso. Si usé la voz de una persona de la comunidad, pregunto si puedo mostrarla. Mi registro no debe llevar datos personales de nadie. Y agradezco a la fuente con una frase: «Gracias, chaltumay».",
    ],
    vocab=[("registro", "anotación con palabra, fuente, fecha y recurso"), ("recurso", "audio, video o texto de donde viene el dato"), ("compartir", "mostrar mi trabajo a otras personas"), ("agradecer", "decir gracias a quien me ayudó"), ("revisar", "mirar otra vez para encontrar errores")],
    worked=[
        W("Registrar con cuatro datos", "Escuché «iorana» en un audio de la escuela, hoy 5 de junio. ¿Cuáles son los cuatro datos?", ["Palabra: iorana.", "Fuente: audio de la escuela.", "Fecha: 5 de junio. Recurso: audio."], "iorana; audio de la escuela; 5 de junio; audio"),
        W("Dos formas escuchadas", "Vi «ruka» escrito en una tarjeta y «ruca» escrito en un libro. Las dos se refieren a la casa. ¿Qué hago?", ["Veo que son dos formas de la misma palabra.", "Anoto las dos con su recurso.", "Pregunto al educador qué forma usa su comunidad."], "anoto las dos y pregunto"),
    ],
    mistakes=[
        M("Compartir un audio de otra persona sin su permiso.", "Esa voz tiene dueño.", "Pido permiso antes de mostrarlo."),
        M("Registrar solo la palabra y olvidar el recurso.", "Después nadie sabe de dónde vino.", "Anoto los cuatro datos: palabra, fuente, fecha y recurso."),
    ],
    R=[
        ex("¿Cuántos datos tiene el registro de esta clase: 3 o 4?", "4", "Son palabra, fuente, fecha y recurso."),
        ex("Si el audio es de la escuela, ¿qué dato es «audio de la escuela»: la fuente o la fecha?", "la fuente", "Dice de dónde vino la palabra."),
        ex("¿Qué recurso es un sonido grabado: audio o foto?", "audio", "El audio es sonido grabado."),
    ],
    C=[
        ex("Verdadero o falso: puedo compartir cualquier audio con mi curso sin pedir permiso.", "Falso", "Antes de compartir se pide permiso a quien corresponde."),
        ex("Registro: «Palabra: maururu. Fuente: audio de la escuela. Fecha: 7 de junio». ¿Qué dato falta?", "el recurso", "Falta anotar si fue audio, video o texto."),
        ex("Si dos recursos muestran formas distintas, ¿anoto una o las dos?", "las dos", "Anoto cada forma con su fuente."),
    ],
    A=[
        ex("Escribe el registro: palabra «ko», fuente video de práctica, fecha hoy, recurso video. ¿Cuántos datos escribiste?", "4", "Palabra, fuente, fecha y recurso."),
        ex("Eliges la mejor frase para agradecer a la educadora que te prestó el audio: A) «Gracias por prestarme el audio.» B) «Ya lo tengo.»", "A", "A agradece con respeto."),
        ex("Tienes 6 registros y revisas 2 cada día. ¿Cuántos días tardas en revisar todos?", "3", "6 ÷ 2 = 3 días."),
    ],
    Z=[
        ex("Samuel quiere publicar un audio con la voz de una invitada sin avisarle. ¿Qué le dices?", "que primero le pida permiso", "La voz es de ella y decide cómo se usa."),
        ex("¿Por qué es útil anotar el recurso (audio, video o texto) en el registro?", "para saber de dónde vino la palabra", "El recurso ayuda a revisar y confiar en el dato."),
    ],
    D=[
        ex("Tu registro tiene 4 datos por palabra y registras 3 palabras. ¿Cuántos datos escribes en total?", "12", "4 × 3 = 12 datos."),
        ex("Dos registros: 1) «mapuzugun», libro, 4 de mayo. 2) «mapudungun», cartel, 4 de mayo. ¿Qué pregunta le haces al educador?", "¿qué forma usa su comunidad?", "Respeta las dos y pide la decisión de la comunidad."),
    ],
    context=[ex("Tu curso hace un afiche con las palabras «iorana» y «maururu» de un audio de la escuela. Antes de colgarlo, ¿qué haces primero con la persona que grabó el audio?", "le pides permiso", "La voz es de ella y decide cómo se comparte.")],
    selfcheck=[
        ex("¿Cuáles son los cuatro datos del registro?", "palabra, fuente, fecha y recurso", "Estos cuatro datos completan el registro."),
        ex("Antes de compartir un audio de otra persona, ¿qué hago?", "pido permiso", "La voz tiene dueño."),
        ex("¿Qué palabra uso para agradecer en mapuzugun según la ficha?", "chaltumay", "La ficha dice que significa gracias."),
    ],
    task=T(
        "Haz tu registro de tres palabras. Palabras y fuentes de práctica: «iorana» (audio de la escuela), «ko» (video de la clase) y «mari mari» (guion de la clase). En tu cuaderno haz una tabla con las columnas: palabra, fuente, fecha de hoy y recurso. Debajo escribe una frase de agradecimiento a la persona que te prestó los materiales y una pregunta para el educador tradicional.",
        "iorana | audio de la escuela | hoy | audio. ko | video de la clase | hoy | video. mari mari | guion de la clase | hoy | texto. Gracias por prestarme los materiales. Pregunta: ¿cómo se dice «gracias» en su comunidad?",
        ["registra tres palabras con los cuatro datos", "copia igual que la fuente", "escribe agradecimiento y pregunta"],
        ["tabla de registro", "frase de agradecimiento"],
        ["no anotar la fuente", "compartir sin permiso"],
        "Valora el registro completo y el agradecimiento; si faltó un dato, recuérdale los cuatro del registro.",
    ),
    reinforce="Haz un registro de una sola palabra con los cuatro datos y revisa que no falte ninguno.",
    extend="Cuenta a alguien de tu casa por qué es importante pedir permiso antes de compartir un audio.",
)
