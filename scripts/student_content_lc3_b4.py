"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR01 (comprensión de textos orales breves con expresiones en lengua indígena o en castellano culturalmente
significativas) y OA LR02 (comunicación oral de ideas y sentimientos con esas expresiones), ambos pensados para
contextos de revitalización lingüística.

Criterio de autoría: los relatos, personajes, diálogos y planes de práctica son inventados, están en castellano y se
declaran como tales; no pertenecen a ningún pueblo. Las únicas expresiones en lengua indígena son las ya atestiguadas
en 2.º (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke en mapuzugun; iorana, maururu en rapa nui), siempre con
su ficha. No se mide la pertenencia ni la identidad de nadie por hablar o no una lengua; nadie está obligado a contar
cosas de su familia ni a mostrar emociones: siempre hay una opción ficticia o de pasar. La forma tradicional de decir,
cuándo y a quién, y la pronunciación, las enseñan el educador/a tradicional y la comunidad; cada tarea abierta lo remite
a ellos.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LR1, LR2 = "LC03 OA LR01", "LC03 OA LR02"

CONSULT = " Recuerda: la forma tradicional de decir y usar estas palabras la enseñan el educador o la educadora tradicional y tu comunidad. Consúltales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No evaluar la identidad ni la fluidez de nadie."

FICHA_EXP = "Ficha de expresiones: «mari mari» es un saludo en mapuzugun. «chaltumay» es «gracias» en mapuzugun. «iorana» es un saludo en rapa nui. «maururu» es «gracias» en rapa nui."
FICHA_PAL = "Ficha de palabras en mapuzugun: «ko» es agua, «antü» es sol, «kuyen» es luna, «ruka» es casa, «mapu» es tierra, «ñuke» es madre."

RELATO_A = "Relato de práctica (inventado): Rosa llegó temprano a la sala y dijo «mari mari». La educadora le sonrió y le dijo: «Buen camino hoy». Rosa hizo una pregunta. Al irse, dijo «chaltumay»."
RELATO_B = "Relato de práctica (inventado): Primero, Pedro encontró una planta seca en el patio. Luego pidió permiso a la profesora para regarla. Después la regó con un vaso de «ko». Al final la planta levantó sus hojas."


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


# =================================================================== LR01 · textos orales y expresiones en revitalización
L(
    LR1, 1,
    materials="Lápiz y hoja. Los personajes y las situaciones son inventados. No hay preguntas con respuesta obligatoria ni nota: puedes pasar cuando quieras.",
    use="Aprenderé qué es la memoria lingüística y a compartir lo que quiera sin sentirme examinado. Sirve para que todas las personas participen con tranquilidad.",
    prior=["Sé que existen lenguas indígenas y que algunas hablan pocas personas.", "Sé que nadie debe contar cosas privadas."],
    explain=[
        "La memoria lingüística es lo que recuerdo de las lenguas que oí o dije. Pueden ser palabras, saludos, canciones o frases que escuché en mi casa, mi barrio o mi escuela. También puede ser una frase en castellano que mi comunidad dice de una forma especial.",
        "No todas las personas recuerdan lo mismo. Algunas personas recuerdan muchas palabras de una lengua indígena, otras recuerdan pocas y otras ninguna. Todas son bienvenidas. Nadie mide si pertenece a un pueblo por saber o no hablar una lengua.",
        "Compartir mi memoria lingüística es una opción, no una obligación. Puedo decir lo que quiera, contar la de un personaje inventado o decir «paso». Y si alguien comparte, lo escucho con respeto y no me burlo ni lo corrijo.",
    ],
    vocab=[("memoria lingüística", "lo que recuerdo de palabras, saludos o frases que oí o dije"), ("compartir", "contar algo a otros si yo quiero"), ("pasar", "decidir no responder"), ("opción", "una forma de elegir entre varias"), ("pertenecer", "ser parte de un pueblo o grupo")],
    worked=[
        W("Elegir cómo participar", "Luis no recuerda ninguna palabra en lengua indígena. Opciones: A) decir «paso» B) inventar que recuerda muchas C) hablar de un personaje inventado que sí las recuerda. ¿Cuáles son buenas opciones?", ["A es una opción válida.", "B es mentir y no ayuda.", "C permite participar sin exponerse."], "A y C"),
        W("Escuchar con respeto", "Rosa cuenta que recuerda una sola palabra, «mari mari». Un compañero se ríe. ¿Qué debe hacer el compañero?", ["La risa puede dañar.", "Debe escuchar con respeto.", "Puede decir: «Gracias por compartir»."], "Escuchar con respeto y agradecer"),
    ],
    mistakes=[
        M("Pensar que quien sabe menos palabras pertenece menos.", "Nadie mide su pertenencia por hablar una lengua.", "Escucho a todos con respeto."),
        M("Obligar a un compañero a decir palabras que no quiere decir.", "Compartir es una opción.", "Le ofrezco decir «paso» o hablar de un personaje inventado."),
    ],
    R=[
        ex("La memoria lingüística es lo que recuerdo de: A) palabras o frases que oí o dije B) los números.", "A", "Es el recuerdo de palabras y frases."),
        ex("Si no quiero responder, puedo decir: A) paso B) mentir.", "A", "Pasar es una opción."),
        ex("¿Todas las personas recuerdan las mismas palabras?", "No", "Cada persona recuerda distinto."),
    ],
    C=[
        ex("Verdadero o falso: quien recuerda menos palabras en una lengua indígena pertenece menos a un pueblo.", "Falso", "Nadie mide la pertenencia por la lengua."),
        ex("Un compañero comparte una sola palabra. ¿Qué haces: lo escucho con respeto o me burlo?", "lo escucho con respeto", "Compartir es una decisión."),
        ex("Una persona no recuerda ninguna palabra. ¿Puede participar? Responde Sí o No.", "Sí", "Puede decir paso o hablar de un personaje inventado."),
    ],
    A=[
        ex("Eliges una opción para participar sin exponerte: A) «Mi personaje inventado, Pablo, recuerda el saludo «mari mari».» B) «Debo decir algo de mi familia aunque no quiera.»", "A", "A respeta mi decisión."),
        arith("Un grupo de 20 niños. 6 quieren compartir su memoria lingüística. ¿Cuántos no quieren compartir hoy?", "20 - 6", "Resto los que comparten del total."),
        ex("Marta no recuerda palabras, pero recuerda que en su barrio dicen «buen camino» al despedirse. ¿Su recuerdo cuenta como memoria lingüística? Responde Sí o No.", "Sí", "También son frases del castellano de su comunidad."),
    ],
    Z=[
        ex("Pedro dice: «Si no hablas la lengua, no tienes derecho a participar». ¿Tiene razón? Responde Sí o No.", "No", "Todas las personas son bienvenidas."),
        ex("La profesora pregunta: «¿Quién habla mapuzugun?». ¿Esa pregunta puede hacer que alguien se sienta examinado? Responde Sí o No.", "Sí", "Obliga a mostrar si sabe o no."),
    ],
    D=[
        ex("¿Cuál de estas cosas es siempre opcional: A) escuchar con respeto a quien comparte B) compartir mi memoria lingüística?", "B", "Escuchar con respeto lo hacemos todos; compartir es siempre una opción."),
        arith("En una sala, 4 niños comparten una palabra cada uno y 3 niños comparten dos palabras cada uno. ¿Cuántas palabras se comparten?", "4 * 1 + 3 * 2", "Cuatro por una más tres por dos."),
    ],
    context=[ex("Tu profesora dice: «Quien quiera, cuente una palabra que recuerde». Tú no recuerdas ninguna. ¿Qué haces: escucho y digo «paso» o invento una palabra?", "escucho y digo «paso»", "No tengo que inventar nada.")],
    selfcheck=[
        ex("¿Qué es la memoria lingüística?", "lo que recuerdo de palabras o frases", "Es el recuerdo de lo que oí o dije."),
        ex("¿Estoy obligado a compartir mi memoria lingüística?", "No", "Es una opción."),
        ex("¿Se mide la pertenencia a un pueblo por hablar una lengua?", "No", "Nadie debe ser examinado."),
    ],
    task=T(
        "Haz un cuadro con tres columnas: «Lo que quiero compartir», «Lo que prefiero guardar» y «Lo que puede contar un personaje inventado». Escribe en cada una una o dos ideas, por ejemplo: un saludo que recuerdas, una frase de tu barrio, o lo que recordaría un niño inventado llamado Pablo. Si no recuerdas ninguna palabra, escribe «paso» en la primera columna y completa las otras con lo que quieras. Termina con una pregunta para el educador tradicional sobre palabras que se estén recuperando en la comunidad.",
        "Compartir: el saludo «mari mari». Guardar: una canción de mi casa. Personaje: Pablo recuerda «chaltumay». Pregunta: ¿qué palabras están volviendo a usarse en la comunidad?",
        ["completa las tres columnas", "respeta que compartir es opcional", "no cuenta cosas privadas", "hace una pregunta al educador/a"],
        ["cuadro escrito", "conversación opcional en voz alta"],
        ["obligar a otros a compartir", "medir quién sabe más"],
        "Acepta cualquier respuesta, incluso «paso». Si alguien compara o se burla, recuérdale que nadie es examinado.",
    ),
    reinforce="Escribe «paso» en una hoja y di con tus palabras cuándo puedes usarlo.",
    extend="Explica a otra persona por qué nadie debe ser examinado por saber o no una lengua.",
)

L(
    LR1, 2,
    materials="Lápiz y hoja. Un adulto lee en voz alta el relato inventado de esta clase. Está escrito aquí, en castellano, con expresiones de la ficha.",
    use="Aprenderé a escuchar un relato breve y a reconocer las expresiones importantes que trae, en lengua indígena o en castellano. Sirve para entender qué frases tienen valor especial en una comunidad.",
    prior=["Sé separar castellano y lengua indígena con una ficha.", "Sé escuchar un relato la primera vez para disfrutarlo."],
    explain=[
        "Una expresión culturalmente significativa es una palabra o frase que tiene un valor especial para un grupo de personas. Puede estar en una lengua indígena, como «mari mari», o en castellano, como una frase que una familia dice al despedirse. El valor de una expresión lo explica quien la usa.",
        "Al escuchar un relato, reconozco las expresiones así: las oigo, las anoto con una palabra clave y miro la ficha si es de una lengua indígena. Si es una frase en castellano, pregunto quién la dice y en qué momento. No supongo su valor.",
        "Una expresión no es un adorno. No la pongo en un texto solo porque se ve linda. La uso cuando tiene sentido para la situación, y reconociendo de dónde viene. Si no sé su valor, pregunto al educador o a la educadora tradicional.",
    ],
    vocab=[("expresión", "palabra o frase que se dice junta"), ("culturalmente significativa", "que tiene un valor especial para un grupo de personas"), ("adorno", "algo que pongo solo para que se vea lindo"), ("reconocer", "darme cuenta de que algo está ahí"), ("valor", "importancia que algo tiene para alguien")],
    worked=[
        W("Reconocer las expresiones", RELATO_A + " " + FICHA_EXP + " ¿Qué expresiones en mapuzugun hay en el relato?", ["Busco las expresiones entre comillas que estén en la ficha.", "«Mari mari» es un saludo y «chaltumay» es gracias.", "«Buen camino hoy» está en castellano."], "«mari mari» y «chaltumay»"),
        W("Una expresión en castellano", RELATO_A + " ¿Qué expresión en castellano dice la educadora?", ["Busco lo que la educadora dice.", "Dice: «Buen camino hoy».", "Pregunto en qué momento la usa."], "«Buen camino hoy»"),
    ],
    mistakes=[
        M("Poner una expresión de otra lengua solo para que quede lindo.", "Es usar la palabra como adorno.", "La uso cuando tiene sentido y nombro su fuente."),
        M("Suponer lo que significa una frase sin preguntar.", "El valor lo explica quien la usa.", "Pregunto quién la dice y cuándo."),
    ],
    R=[
        ex(RELATO_A + " ¿Qué dijo Rosa al llegar?", "«mari mari»", "Su saludo está al comienzo del relato."),
        ex("Una palabra o frase que tiene un valor especial para un grupo se llama expresión: A) culturalmente significativa B) larga.", "A", "Tiene un valor especial."),
        ex("Poner una palabra solo para que se vea linda es usarla como: A) adorno B) saludo.", "A", "No tiene un sentido para la situación."),
    ],
    C=[
        ex(RELATO_A + " " + FICHA_EXP + " ¿Para qué sirve «chaltumay» en el relato?", "para agradecer", "La ficha dice que es gracias."),
        ex("Verdadero o falso: una expresión significativa solo puede estar en una lengua indígena.", "Falso", "También puede estar en castellano."),
        ex(RELATO_A + " ¿En qué lengua está «Buen camino hoy»?", "en castellano", "La educadora lo dice en castellano."),
    ],
    A=[
        arith("En el relato de Rosa hay 2 expresiones en mapuzugun y 1 en castellano. ¿Cuántas expresiones hay en total?", "2 + 1", "Sumo las expresiones."),
        ex(RELATO_A + " Ordena lo que pasa: C) se despide con «chaltumay» A) llega con «mari mari» B) la educadora le desea buen camino. Escribe las letras.", "A, B, C", "Llega, recibe un deseo y se despide."),
        ex("Una niña quiere poner «iorana» en su cartel solo porque se ve linda. ¿Qué es mejor: preguntar si tiene sentido para el cartel o ponerla igual?", "preguntar si tiene sentido para el cartel", "No debo usarla como adorno."),
    ],
    Z=[
        ex("Tomás dice: «Si una frase está en castellano, no puede ser significativa para una comunidad». ¿Tiene razón? Responde Sí o No.", "No", "Una frase en castellano también puede tener valor especial."),
        ex("Don Mario (inventado) dice «buen camino» cuando alguien sale de su casa. Ana dice: «Seguro que es muy antigua y viene de un pueblo». ¿Qué le falta a Ana?", "preguntar a don Mario", "El valor lo explica quien la usa."),
    ],
    D=[
        ex(RELATO_A + " ¿Cuántas expresiones entre comillas dicen Rosa y la educadora?", "3", "Son «mari mari», «Buen camino hoy» y «chaltumay»."),
        arith("Un cartel tiene 3 expresiones y cada una necesita 1 pregunta al educador. ¿Cuántas preguntas haces?", "3 * 1", "Una pregunta por expresión."),
    ],
    context=[ex("En una fiesta de tu curso, alguien propone poner «ruka» en todas las decoraciones solo porque queda lindo. ¿Qué dices: «Preguntemos si tiene sentido para la fiesta» o «Dale»?", "«Preguntemos si tiene sentido para la fiesta»", "No se usa como adorno.")],
    selfcheck=[
        ex("¿Qué es una expresión culturalmente significativa?", "una palabra o frase con valor especial para un grupo", "Su valor lo explica quien la usa."),
        ex("¿Puede estar en castellano?", "Sí", "También hay frases en castellano con valor especial."),
        ex("¿Debo usar una expresión como adorno?", "No", "La uso cuando tiene sentido."),
    ],
    task=T(
        "Pídele a un adulto que lea en voz alta el relato de práctica de esta clase. Escribe en dos columnas las expresiones que escuchaste: una columna para las que están en mapuzugun (con su significado según la ficha) y otra para las que están en castellano. Después escribe una pregunta para el educador tradicional sobre cuándo se usa una de ellas.",
        "Mapuzugun: «mari mari» = saludo; «chaltumay» = gracias. Castellano: «Buen camino hoy». Pregunta: ¿cuándo se dice «mari mari» en su comunidad?",
        ["escribe las dos expresiones en mapuzugun con su significado", "escribe la expresión en castellano", "formula una pregunta al educador/a"],
        ["dos columnas escritas", "pregunta escrita o dicha en voz alta"],
        ["suponer significados", "poner expresiones como adorno"],
        "Valora que reconoció expresiones en ambas lenguas; si inventó un significado, pídele que vuelva a la ficha.",
    ),
    reinforce="Escucha otra vez el relato de Rosa y levanta la mano cada vez que oigas una expresión.",
    extend="Escribe una expresión que se diga en tu casa y que sea significativa para ti, sin contar nada privado.",
)

L(
    LR1, 3,
    materials="Lápiz y hoja. Un adulto lee en voz alta el relato inventado de esta clase. Está escrito aquí, en castellano, con una palabra de la ficha.",
    use="Aprenderé a ordenar los hechos de un relato breve y a explicar qué significan sus expresiones. Sirve para comprender de verdad lo que escucho.",
    prior=["Sé reconocer expresiones en un relato.", "Sé usar «porque» para unir una causa con lo que pasó."],
    explain=[
        "Comprender un relato es saber qué pasó, en qué orden y por qué. La secuencia es el orden de los hechos. Los marcadores como primero, luego, después y al final me ayudan a ordenarlos.",
        "Además, comprendo el significado de las expresiones. El significado de una expresión en lengua indígena está en la ficha o lo explica el educador tradicional. El significado de una frase en castellano lo explica quien la usa. Anoto cuál es su sentido en el relato y no agrego otro.",
        "Cuando cuento el relato con mis palabras, uso la secuencia y el significado de las expresiones. No agrego hechos que no estaban ni cambio las expresiones. Si no estoy seguro, vuelvo a escuchar esa parte.",
    ],
    vocab=[("secuencia", "el orden en que pasan los hechos"), ("marcador", "palabra como primero o luego que ordena"), ("significado", "lo que quiere decir algo"), ("sentido", "para qué sirve algo en el relato"), ("agregar", "poner algo más")],
    worked=[
        W("Ordenar los hechos", RELATO_B + " ¿Qué hizo Pedro después de encontrar la planta seca?", ["Busco el marcador «luego».", "Dice que pidió permiso para regarla.", "Es lo siguiente."], "Pidió permiso a la profesora para regarla"),
        W("El significado de una palabra", RELATO_B + " " + FICHA_PAL + " ¿Con qué regó Pedro la planta?", ["Busco la palabra entre comillas: «ko».", "La ficha dice que «ko» es agua.", "Regó con agua."], "con agua"),
    ],
    mistakes=[
        M("Contar el final antes que el comienzo.", "El orden cambia lo que pasó.", "Uso primero, luego, después y al final."),
        M("Agregar hechos que no estaban en el relato.", "Cambio el relato de quien lo contó.", "Cuento solo lo que escuché."),
    ],
    R=[
        ex(RELATO_B + " ¿Qué encontró Pedro primero?", "una planta seca", "Es el primer hecho."),
        ex("La palabra que marca el último hecho es: A) al final B) primero.", "A", "«Al final» cierra el relato."),
        ex(FICHA_PAL + " ¿Qué quiere decir «ko»?", "agua", "La ficha lo dice."),
    ],
    C=[
        ex(RELATO_B + " ¿Qué pasó al final con la planta?", "levantó sus hojas", "Es el último hecho del relato."),
        ex("Verdadero o falso: al contar un relato, puedo agregar hechos que me parecen buenos.", "Falso", "Cuento solo lo que escuché."),
        ex(RELATO_B + " Completa: «Pedro pidió permiso ____ regarla». Elige: para o aunque.", "para", "Pidió permiso con el propósito de regar."),
    ],
    A=[
        ex(RELATO_B + " Ordena los hechos: B) regó con «ko» A) encontró una planta seca C) la planta levantó sus hojas D) pidió permiso. Escribe las letras.", "A, D, B, C", "Encontró, pidió permiso, regó y levantó sus hojas."),
        arith("Otro día, Pedro usó 1 vaso de agua en la mañana y 2 vasos en la tarde para otra planta. ¿Cuántos vasos usó en total?", "1 + 2", "Sumo los vasos."),
        ex(FICHA_PAL + " " + RELATO_B + " Explica con otras palabras qué pasó con la planta: ¿se secó más o se recuperó?", "se recuperó", "Levantó sus hojas después de regarla."),
    ],
    Z=[
        ex("Tomás dice: «Pedro regó la planta con agua de lluvia». El relato no lo dice. ¿Qué debe hacer Tomás?", "contar solo lo que dice el relato", "No debe agregar hechos."),
        ex(RELATO_B + " Rita dice que la planta levantó sus hojas porque Pedro la regó. ¿Es una buena relación entre causa y hecho? Responde Sí o No.", "Sí", "El riego viene antes y explica que se recuperó."),
    ],
    D=[
        ex(RELATO_B + " ¿Cuántos marcadores de orden hay (primero, luego, después, al final)?", "4", "Hay cuatro marcadores."),
        arith("Cuentas el relato en 4 frases y cada frase tiene 5 palabras. ¿Cuántas palabras dices?", "4 * 5", "Cuatro frases por cinco palabras."),
    ],
    context=[ex("Tu hermano no escuchó el relato de Pedro. Le dices: «Primero…». ¿Con qué hecho comienzas: Pedro encontró una planta seca o la planta levantó sus hojas?", "Pedro encontró una planta seca", "Comienzo por el primer hecho.")],
    selfcheck=[
        ex("¿Cómo se llama el orden de los hechos?", "secuencia", "Es la secuencia."),
        ex("¿Dónde veo el significado de «ko»?", "en la ficha", "La ficha dice que es agua."),
        ex("¿Puedo agregar hechos al contar un relato?", "No", "Cuento solo lo escuchado."),
    ],
    task=T(
        "Pídele a un adulto que lea dos veces el relato de práctica de esta clase. Anota tres palabras clave en la segunda escucha. Después cuéntalo con tus palabras, en orden, con «primero», «luego», «después» y «al final», y explica qué significa la palabra «ko» según la ficha. Termina con una pregunta para el educador tradicional sobre el agua en la comunidad.",
        "Palabras clave: planta, permiso, ko. Primero Pedro encontró la planta seca. Luego pidió permiso. Después la regó con ko, que es agua. Al final la planta levantó sus hojas. Pregunta: ¿cómo cuida el agua la comunidad?",
        ["cuenta los hechos en orden", "explica el significado de «ko» con la ficha", "no agrega hechos", "hace una pregunta al educador/a"],
        ["palabras clave escritas", "relato contado en voz alta"],
        ["cambiar el orden", "agregar hechos"],
        "Revisa el orden y el significado de «ko»; si agregó hechos, pídele que vuelva a escuchar.",
    ),
    reinforce="Cuenta el relato de Pedro con solo cuatro frases: primero, luego, después y al final.",
    extend="Inventa un relato breve de cuatro hechos que incluya la palabra «ko» y pídele a alguien que lo cuente de vuelta.",
)

L(
    LR1, 4,
    materials="Lápiz y hoja. La tabla de conocimientos está escrita aquí. Los personajes son inventados. Puedes usar un personaje inventado en lugar de contar lo tuyo.",
    use="Aprenderé a relacionar un relato con lo que yo sé y con lo que saben otras personas, usando una opción ficticia si lo prefiero. Sirve para comprender sin invadir la privacidad de nadie.",
    prior=["Sé reconstruir un relato en orden.", "Sé que nadie está obligado a contar cosas privadas."],
    explain=[
        "Cuando escucho un relato, lo uno con conocimientos. Hay tres clases: lo que sé yo, lo que sabe otra persona y lo que sabe la comunidad. Lo que sabe la comunidad no lo adivino: lo pregunto al educador o a la educadora tradicional.",
        "Para no contar cosas privadas, puedo usar una opción ficticia. Una opción ficticia es un personaje inventado que sabe o siente algo parecido. Por ejemplo: «Un niño inventado llamado Pablo sabe que las plantas necesitan agua». Así participo igual y me cuido.",
        "Mis conocimientos y los de otros pueden ser distintos, y eso está bien. Si alguien sabe algo diferente a lo que yo sé, lo escucho y no digo que está equivocado. Puedo preguntar de dónde viene lo que sabe.",
    ],
    vocab=[("conocimiento", "lo que sé porque lo aprendí"), ("comunidad", "grupo de personas que comparte una cultura"), ("ficticio", "inventado"), ("relacionar", "unir dos cosas que tienen que ver"), ("privado", "personal, que no se obliga a contar")],
    worked=[
        W("Clasificar un conocimiento", RELATO_B + " Pedro sabe que las plantas necesitan agua. ¿De quién es ese conocimiento: mío, de otra persona o de la comunidad?", ["Lo dice un personaje, Pedro.", "Es de otra persona, no mío.", "Si fuera una creencia de la comunidad, la preguntaría."], "De otra persona (Pedro)"),
        W("Usar una opción ficticia", "Ana no quiere contar nada de su casa. ¿Qué puede hacer para relacionar el relato de Pedro con lo que sabe?", ["Puede inventar un personaje.", "Dice: «Una niña inventada llamada Lola sabe que las plantas necesitan sol»."], "Usar un personaje inventado"),
    ],
    mistakes=[
        M("Decir que lo que sabe la comunidad es lo que yo me imagino.", "Puedo inventar algo falso.", "Pregunto al educador tradicional."),
        M("Decir que otra persona está equivocada porque sabe algo distinto.", "Puede venir de otra experiencia.", "Pregunto de dónde viene lo que sabe."),
    ],
    R=[
        ex("Una opción ficticia es: A) un personaje inventado B) un secreto de mi casa.", "A", "Ficticio quiere decir inventado."),
        ex("Lo que sabe la comunidad lo pregunto: A) al educador tradicional B) a nadie.", "A", "Él puede enseñarlo."),
        ex("¿Estoy obligado a contar cosas privadas para relacionar un relato?", "No", "Puedo usar una opción ficticia."),
    ],
    C=[
        ex("Verdadero o falso: si otra persona sabe algo distinto, está equivocada.", "Falso", "Puede venir de otra experiencia."),
        ex("Frase: «Una niña inventada llamada Lola sabe que las plantas necesitan sol». ¿Es un conocimiento mío, de un personaje o de la comunidad?", "de un personaje", "Lola es un personaje inventado."),
        ex("¿Cuántas clases de conocimientos hay en la clase: 2 o 3?", "3", "Hay lo mío, lo de otra persona y lo de la comunidad."),
    ],
    A=[
        ex("Clasifica: «Yo sé que el agua es necesaria para las plantas». ¿Es conocimiento mío, de otra persona o de la comunidad?", "mío", "Empieza con «yo sé»."),
        arith("Anotas 2 conocimientos tuyos, 2 de personajes inventados y 1 que debes preguntar a la comunidad. ¿Cuántos conocimientos anotas?", "2 + 2 + 1", "Sumo los tres grupos."),
        ex("Quieres relacionar el relato de Pedro con algo que sabes, pero es muy personal. Elige: A) invento un niño llamado Pablo que lo sabe B) cuento todo aunque no quiera.", "A", "Una opción ficticia me protege."),
    ],
    Z=[
        ex("Luis dice: «En mi comunidad se hace así; seguro que en todas las comunidades también». ¿Tiene razón? Responde Sí o No.", "No", "Cada comunidad tiene sus propios saberes."),
        ex("Una niña dice que sabe lo que cree una comunidad, pero nunca preguntó. ¿Qué le falta?", "preguntar al educador tradicional", "Lo que sabe la comunidad se pregunta."),
    ],
    D=[
        ex("¿Qué conocimiento NO debo inventar: A) lo que sabe la comunidad B) lo que sabe un personaje inventado?", "A", "Lo que sabe la comunidad se pregunta; el personaje inventado es mío para imaginar."),
        arith("Cada persona de un grupo de 4 aporta 2 conocimientos. ¿Cuántos conocimientos hay en total?", "4 * 2", "Cuatro personas por dos conocimientos."),
    ],
    context=[ex("Después del relato de Pedro, tu profesora pregunta: «¿Qué sabes de las plantas?». Prefieres no hablar de tu casa. ¿Qué haces: invento a una niña llamada Lola que sabe algo o me obligo a contar de mi casa?", "invento a una niña llamada Lola que sabe algo", "Una opción ficticia me deja participar.")],
    selfcheck=[
        ex("¿Cuáles son las tres clases de conocimientos?", "lo mío, lo de otra persona y lo de la comunidad", "Son las tres de la clase."),
        ex("¿Qué es una opción ficticia?", "un personaje inventado", "Ficticio es inventado."),
        ex("¿A quién pregunto lo que sabe la comunidad?", "al educador tradicional", "Él puede enseñarlo."),
    ],
    task=T(
        "Usa el relato de Pedro y la planta seca. Haz una tabla de tres filas: «Lo que sé yo» (algo sobre plantas o agua), «Lo que sabe un personaje inventado» (inventa uno, por ejemplo Lola) y «Lo que sabe la comunidad» (no lo inventes: escribe una pregunta para el educador tradicional). Si prefieres no contar lo tuyo, escribe «paso» en la primera fila.",
        "Lo que sé yo: las plantas necesitan agua. Personaje: Lola sabe que las plantas necesitan sol. Comunidad: ¿qué plantas cuidan en la comunidad?",
        ["completa las tres filas", "no cuenta cosas privadas", "pregunta en vez de inventar lo de la comunidad"],
        ["tabla escrita", "participación voluntaria en voz alta"],
        ["inventar lo que sabe la comunidad", "obligar a otros a contar"],
        "Acepta «paso». Si inventó lo que sabe la comunidad, pídele que lo cambie por una pregunta.",
    ),
    reinforce="Inventa un personaje con nombre y di una cosa que sabe sobre las plantas.",
    extend="Escribe dos preguntas para el educador tradicional sobre las plantas de la comunidad.",
)

L(
    LR1, 5,
    materials="Lápiz, hoja y colores. Las ideas de devolución están escritas aquí. Todo se queda en tu casa o tu curso, sin publicar en internet.",
    use="Aprenderé a crear una devolución que ayuda a revitalizar una lengua con respeto. Sirve para agradecer a quien enseñó y cuidar lo aprendido.",
    prior=["Sé qué es revitalizar una lengua.", "Sé reconocer expresiones y su significado."],
    explain=[
        "Revitalizar es ayudar a que una lengua vuelva a usarse y a vivir. No lo hace una sola persona: lo hacen las comunidades y quienes las acompañan con respeto. Una devolución es lo que yo le entrego a quien me enseñó, para agradecer y cuidar lo aprendido.",
        "Mi devolución puede ser un dibujo con una palabra de la ficha y el nombre de la fuente, una nota de agradecimiento con «chaltumay» o un cartel que diga qué aprendí. Para que ayude de verdad, uso las palabras como me las enseñaron, nombro a quien me las enseñó y pido permiso antes de mostrar o compartir.",
        "Hay cosas que no ayudan: burlarse, usar las palabras de adorno, cambiarlas para que sean más fáciles o publicar el saber de la comunidad sin permiso. Ayudar es aprender de quien sabe, usar con respeto y compartir con permiso.",
    ],
    vocab=[("revitalizar", "ayudar a que una lengua vuelva a usarse"), ("devolución", "lo que entrego a quien me enseñó"), ("aporte", "lo que pongo para ayudar"), ("fuente", "persona de donde viene lo que aprendí"), ("permiso", "aviso de que sí puedo compartir algo")],
    worked=[
        W("Elegir una devolución que ayuda", "Opciones: A) un dibujo con «ko» (agua), el nombre de la educadora como fuente y su permiso para mostrarlo B) un cartel con palabras cambiadas para que sean más fáciles. ¿Cuál ayuda a revitalizar?", ["A usa la palabra como se enseña.", "A nombra la fuente y pide permiso.", "B cambia las palabras."], "A"),
        W("Agradecer con respeto", "La educadora te enseñó «chaltumay». ¿Cómo puedes agradecerle al terminar la clase?", ["Pienso en lo que me enseñó.", "Uso la palabra que me enseñó.", "Digo «chaltumay» con respeto."], "Diciéndole «chaltumay»"),
    ],
    mistakes=[
        M("Cambiar una palabra para que sea más fácil.", "La lengua pierde su forma.", "La uso como la enseñó el educador."),
        M("Mostrar mi trabajo en internet sin permiso.", "El saber de la comunidad se cuida.", "Lo muestro en mi curso o en mi casa."),
    ],
    R=[
        ex("Revitalizar es: A) ayudar a que una lengua vuelva a usarse B) olvidar una lengua.", "A", "Revitalizar es dar vida de nuevo."),
        ex("Lo que entrego a quien me enseñó se llama: A) devolución B) examen.", "A", "Es mi forma de agradecer."),
        ex(FICHA_EXP + " ¿Qué palabra en mapuzugun uso para agradecer?", "chaltumay", "La ficha dice que es gracias."),
    ],
    C=[
        ex("Verdadero o falso: burlarme del acento de alguien ayuda a que la lengua viva.", "Falso", "La burla daña y aleja a las personas."),
        ex("Para que mi devolución ayude, ¿nombro a quien me enseñó o no digo nada?", "nombro a quien me enseñó", "Reconozco la fuente."),
        ex("Un dibujo con «ko» y el nombre de la fuente, ¿ayuda a cuidar lo aprendido? Responde Sí o No.", "Sí", "Reconoce la fuente y usa la palabra bien."),
    ],
    A=[
        ex("Elige la devolución con respeto: A) nota de agradecimiento con «chaltumay» y el nombre de la educadora B) subir su explicación a internet sin avisar.", "A", "A agradece y cuida; B no pide permiso."),
        arith("Preparas 3 notas de agradecimiento para cada una de 2 personas que te enseñaron. ¿Cuántas notas preparas?", "3 * 2", "Tres notas por dos personas."),
        ex("Tu cartel dice «ko» y debajo «agua en mapuzugun». ¿Qué le falta para ser una buena devolución: nombrar la fuente o cambiar el color?", "nombrar la fuente", "Debo reconocer a quien me enseñó."),
    ],
    Z=[
        ex("Pedro dice: «Voy a cambiar las palabras para que más gente las diga». ¿Ayuda a revitalizar? Responde Sí o No.", "No", "Cambiar las palabras cambia la lengua."),
        ex("¿Por qué es mejor mostrar mi devolución en mi curso o en mi casa que subirla de inmediato a internet?", "porque primero hay que pedir permiso", "El saber de la comunidad se cuida."),
    ],
    D=[
        ex("Ordena para crear una devolución: C) la muestro con permiso A) escucho y aprendo B) hago mi trabajo con la fuente. Escribe las letras.", "A, B, C", "Aprendo, creo y muestro."),
        arith("Tu cuaderno tiene 5 palabras de la ficha y las usas todas con su fuente. Si ya presentaste 3, ¿cuántas faltan?", "5 - 3", "Resto las presentadas."),
    ],
    context=[ex("Para el cierre de la unidad, tu curso hace un cartel. Una compañera dice: «Pongamos solo las palabras que nos gusten». ¿Qué propones: usar las palabras que enseñó la educadora y nombrarla o elegir solo las lindas?", "usar las palabras que enseñó la educadora y nombrarla", "Reconozco la fuente y cuido las palabras.")],
    selfcheck=[
        ex("¿Qué significa revitalizar?", "ayudar a que una lengua vuelva a usarse", "Es darle vida de nuevo."),
        ex("¿Qué palabra uso para agradecer en mapuzugun?", "chaltumay", "La ficha lo dice."),
        ex("¿Puedo cambiar una palabra para que sea más fácil?", "No", "La uso como me la enseñaron."),
    ],
    task=T(
        "Crea tu devolución en papel: un dibujo o una nota que incluya una palabra de la ficha («ko», «antü», «kuyen», «ruka», «mapu» o «ñuke») con su significado, el nombre de quien te la enseñó (puede ser la educadora tradicional de tu escuela o «la ficha de la clase») y una frase que diga qué aprendiste. Escribe también quién la verá (tu curso o tu casa) y confirma que pedirás permiso antes de mostrarla. No la subas a internet.",
        "Dibujo de un sol con «antü» = sol. Fuente: la educadora. Frase: aprendí que antü es sol. La verá mi curso con permiso.",
        ["incluye una palabra de la ficha bien copiada", "nombra la fuente", "escribe quién la verá y que pedirá permiso", "no la publica"],
        ["dibujo o nota", "frase escrita"],
        ["cambiar la palabra", "no nombrar la fuente"],
        "Valora que reconoció la fuente y cuidó el permiso; si cambió la palabra, pídele que la copie igual a la ficha.",
    ),
    reinforce="Di «chaltumay» a alguien que te haya enseñado algo hoy, y explica por qué lo dices.",
    extend="Escribe una segunda devolución para otra persona que te haya enseñado algo, siguiendo los mismos pasos.",
)

# =================================================================== LR02 · comunicación oral de ideas y sentimientos
L(
    LR2, 1,
    materials="Lápiz y hoja. Las situaciones son inventadas para practicar. Nadie está obligado a contar cosas personales ni a mostrar emociones: puedes comunicar una idea o usar un personaje inventado.",
    use="Aprenderé a elegir una situación para comunicar una idea o un sentimiento. Sirve para hablar con claridad y cuidando mi privacidad.",
    prior=["Conozco las expresiones «mari mari» y «chaltumay» con su ficha.", "Sé que nadie debe contar lo que no quiere."],
    explain=[
        "Comunicar es decir una idea o un sentimiento a otra persona. Una idea es algo que pienso. Un sentimiento es algo que siento, como alegría o curiosidad. Puedo comunicar una idea sin hablar de mis sentimientos, y puedo elegir qué sentimiento comparto.",
        "Primero elijo una situación. Una situación puede ser personal, familiar o comunitaria. Por ejemplo: presentar una palabra nueva a mi curso, agradecer a una persona invitada o contar una idea sobre cuidar el agua. En cada una pienso a quién le hablo y qué quiero lograr.",
        "En mi intervención puedo usar expresiones en lengua indígena que conozco por la ficha, o expresiones en castellano que sean importantes para mi comunidad. Si no tengo una expresión, hablo en castellano y pregunto. Nadie debe mostrarme cómo me siento si no quiero, y puedo usar un personaje inventado.",
    ],
    vocab=[("comunicar", "decir una idea o un sentimiento a otra persona"), ("idea", "algo que pienso"), ("sentimiento", "algo que siento"), ("situación", "momento y lugar en que hablo"), ("intervención", "lo que digo cuando me toca hablar")],
    worked=[
        W("Elegir la situación", "Rosa quiere agradecer a una educadora que visitó la sala. Opciones: A) saludar a la entrada B) agradecer al final de la visita C) contar un secreto de su casa. ¿Qué situación elige?", ["Quiere agradecer.", "La situación B es la del final de la visita.", "No necesita contar secretos."], "B"),
        W("Elegir idea o sentimiento", "Pedro quiere comunicar una idea sobre cuidar el agua pero no quiere hablar de sus sentimientos. ¿Puede?", ["Una idea y un sentimiento son cosas distintas.", "Puede comunicar solo la idea.", "Nadie lo obliga a decir cómo se siente."], "Sí, puede comunicar solo la idea"),
    ],
    mistakes=[
        M("Obligar a alguien a decir cómo se siente.", "Compartir sentimientos es una opción.", "Le ofrezco comunicar solo una idea."),
        M("Elegir una situación sin pensar a quién le hablo.", "No sé cómo decirlo.", "Pienso a quién le hablo y qué quiero lograr."),
    ],
    R=[
        ex("Algo que pienso es una: A) idea B) emoción.", "A", "Idea es lo que pienso."),
        ex("Algo que siento, como alegría, es un: A) sentimiento B) título.", "A", "Es lo que siento."),
        ex("¿Estoy obligado a contar cómo me siento?", "No", "Es una opción."),
    ],
    C=[
        ex("Verdadero o falso: para comunicarme debo contar siempre cosas de mi casa.", "Falso", "Puedo comunicar una idea o usar un personaje inventado."),
        ex("Situaciones: A) agradecer a una persona invitada B) contar un secreto de mi familia. ¿Cuál es adecuada para la clase?", "A", "No debo contar cosas privadas."),
        ex(FICHA_EXP + " Quiero agradecer en mapuzugun. ¿Qué expresión uso?", "chaltumay", "La ficha dice que es gracias."),
    ],
    A=[
        ex("Eliges una situación: A) presentar a mi curso una palabra nueva de la ficha B) contar algo privado. ¿Cuál elegirías para practicar?", "A", "Es adecuada y no expone a nadie."),
        arith("Tienes 3 situaciones posibles y en cada una puedes comunicar 2 cosas: una idea y un sentimiento. ¿Cuántas cosas puedes comunicar en total?", "3 * 2", "Tres situaciones por dos cosas."),
        ex("Quiero comunicar una idea sobre cuidar el agua y mi sentimiento es curiosidad. ¿Qué es la idea y qué es el sentimiento? Escribe: idea, sentimiento. Opciones: cuidar el agua / curiosidad.", "cuidar el agua, curiosidad", "Lo que pienso es la idea y lo que siento es la curiosidad."),
    ],
    Z=[
        ex("Luis dice: «Si no quiero decir cómo me siento, no puedo hablar». ¿Tiene razón? Responde Sí o No.", "No", "Puedo comunicar una idea."),
        ex("Una niña no tiene una expresión en lengua indígena para lo que quiere decir. ¿Qué es mejor: inventarla o hablar en castellano y preguntar?", "hablar en castellano y preguntar", "No se inventan expresiones."),
    ],
    D=[
        ex("Ordena para preparar mi comunicación: C) pienso qué expresión usar A) elijo la situación B) pienso a quién le hablo. Escribe las letras.", "A, B, C", "Situación, interlocutor y expresión."),
        arith("Preparas 2 comunicaciones breves y para cada una escribes 3 frases. ¿Cuántas frases escribes en total?", "2 * 3", "Dos comunicaciones por tres frases."),
    ],
    context=[ex("Tu profesora te pide hablar un minuto frente al curso sobre algo que aprendiste. Prefieres no hablar de tu casa. ¿Qué eliges: presentar la palabra «ko» y su significado o contar algo privado?", "presentar la palabra «ko» y su significado", "Es una situación segura para mí.")],
    selfcheck=[
        ex("¿Qué es una idea?", "algo que pienso", "Idea es lo que pienso."),
        ex("¿Qué es un sentimiento?", "algo que siento", "Sentimiento es lo que siento."),
        ex("¿Puedo comunicar una idea sin contar mis sentimientos?", "Sí", "Compartir sentimientos es una opción."),
    ],
    task=T(
        "Haz una tabla con tres situaciones posibles: A) presentar a tu curso una palabra de la ficha; B) agradecer a una persona invitada con «chaltumay»; C) contar una idea sobre cuidar el agua. Para cada una escribe a quién le hablarías, qué idea quieres comunicar y si quieres agregar un sentimiento (puedes escribir «paso»). Marca con una estrella la situación que elegirías para practicar.",
        "A: le hablo a mi curso; idea: «ko» es agua; sentimiento: paso. B: le hablo a la educadora; idea: gracias; sentimiento: alegría. C: le hablo a mi curso; idea: cerrar la llave; sentimiento: paso. Elijo B.",
        ["completa las tres situaciones", "indica a quién habla", "puede decir «paso» al sentimiento", "marca una situación"],
        ["tabla escrita", "elección dicha en voz alta"],
        ["contar cosas privadas", "obligar a otros a decir sus sentimientos"],
        "Acepta «paso» al sentimiento. Si contó algo privado, recuérdale que puede usar un personaje inventado.",
    ),
    reinforce="Elige una situación del cuadro y di en voz alta a quién le hablarías y qué idea dirías.",
    extend="Escribe una cuarta situación posible para comunicar una idea en tu escuela.",
)

L(
    LR2, 2,
    materials="Lápiz y hoja. La ficha de expresiones está escrita aquí. Para aprender las expresiones con su forma tradicional, necesitas al educador o a la educadora tradicional.",
    use="Aprenderé cómo aprender expresiones desde la fuente, sin inventar. Sirve para decirlas con respeto y saber de dónde las aprendí.",
    prior=["Sé elegir una situación para comunicar.", "Conozco las expresiones de la ficha."],
    explain=[
        "Aprender desde la fuente es aprender una expresión de la persona que la conoce, no de mi imaginación. La fuente puede ser el educador o la educadora tradicional, una persona mayor de la comunidad o una ficha hecha con ellos. Siempre anoto quién me la enseñó.",
        "Sigo estos pasos: escucho la expresión, pregunto qué significa y cuándo se usa, la repito, y pido que me ayuden a mejorar. Anoto el significado según la fuente, no según lo que me suena. Si dos fuentes dicen cosas distintas, anoto las dos y pregunto.",
        "En la ficha tengo cuatro expresiones: «mari mari» e «iorana» son saludos; «chaltumay» y «maururu» son «gracias». No sé más sobre ellas que lo que dice la ficha. Cuándo, cómo y a quién se dicen lo enseña la comunidad.",
    ],
    vocab=[("fuente", "persona o material de donde aprendo algo"), ("anotar", "escribir para recordar"), ("repetir", "decir otra vez"), ("mejorar", "hacer algo cada vez mejor"), ("comunidad", "grupo de personas que comparte una cultura")],
    worked=[
        W("Anotar la fuente", "La educadora tradicional te enseñó «mari mari». ¿Qué anotas junto a la expresión?", ["Anoto la expresión.", "Anoto su significado: saludo.", "Anoto la fuente: la educadora tradicional."], "«mari mari», saludo; fuente: la educadora tradicional"),
        W("Dos fuentes que no coinciden", "Un cartel dice que «iorana» es gracias y la ficha dice que es un saludo. ¿Qué haces?", ["Las dos fuentes no coinciden.", "No elijo yo.", "Anoto las dos y pregunto a la educadora tradicional."], "Anoto las dos y pregunto"),
    ],
    mistakes=[
        M("Aprender una expresión de un video sin saber quién la dice.", "No sé si está bien dicha ni si se puede usar.", "Aprendo de una fuente confiable."),
        M("Cambiar el significado de una expresión porque me parece mejor.", "El significado lo define la fuente.", "Anoto el significado que dice la fuente."),
    ],
    R=[
        ex("Aprender desde la fuente es aprender de: A) quien conoce la lengua B) mi imaginación.", "A", "La fuente conoce la expresión."),
        ex(FICHA_EXP + " ¿Qué quiere decir «maururu»?", "gracias", "La ficha dice que es gracias en rapa nui."),
        ex("Junto a la expresión anoto: A) quién me la enseñó B) mi color favorito.", "A", "La fuente es parte del registro."),
    ],
    C=[
        ex("Verdadero o falso: puedo aprender una expresión de cualquier video sin saber quién la dice.", "Falso", "Necesito una fuente confiable."),
        ex(FICHA_EXP + " ¿Cuántas expresiones de la ficha son saludos?", "2", "«Mari mari» e «iorana» son saludos."),
        ex("Dos fuentes dicen cosas distintas de una expresión. ¿Qué hago: anoto las dos y pregunto o elijo la que me suena mejor?", "anoto las dos y pregunto", "No decido yo."),
    ],
    A=[
        ex("Ordena los pasos: C) la repito B) pregunto qué significa A) escucho la expresión D) pido ayuda para mejorar. Escribe las letras.", "A, B, C, D", "Escucho, pregunto, repito y pido ayuda."),
        arith("La ficha tiene 4 expresiones y ya aprendiste 3 desde la fuente. ¿Cuántas te faltan?", "4 - 3", "Resto las aprendidas."),
        ex(FICHA_EXP + " Une cada expresión con su significado. 1) «iorana» 2) «chaltumay». Significados: gracias, saludo. Escribe los significados en orden.", "saludo, gracias", "«Iorana» es saludo y «chaltumay» es gracias."),
    ],
    Z=[
        ex("Ana dice: «Aprendí «mari mari» de un compañero, así que está bien». ¿Qué le falta?", "una fuente confiable", "Debe confirmarlo con el educador tradicional o una ficha hecha con él."),
        ex("Pedro dice: «Agrego una palabra mía a la ficha porque me parece que falta». ¿Tiene razón? Responde Sí o No.", "No", "No se agregan palabras que no vienen de la fuente."),
    ],
    D=[
        ex("¿Qué es más confiable para saber qué significa «mari mari»: A) un compañero que lo oyó en un recreo B) la ficha hecha con la educadora?", "B", "La ficha viene de una fuente confiable."),
        arith("Aprendes 2 expresiones por semana durante 2 semanas. ¿Cuántas expresiones aprendiste?", "2 * 2", "Dos expresiones por dos semanas."),
    ],
    context=[ex("Un compañero te dice: «Aprendí una expresión en un juego y significa 'amigo' en mapuzugun». No está en la ficha. ¿Qué le sugieres: preguntarle a la educadora tradicional o usarla ya?", "preguntarle a la educadora tradicional", "No tiene una fuente confiable.")],
    selfcheck=[
        ex("¿Qué anoto junto a cada expresión que aprendo?", "la fuente", "Anoto quién me la enseñó."),
        ex("¿Quién puede enseñarme cuándo se dice una expresión?", "el educador tradicional o la comunidad", "Ellos conocen su uso."),
        ex("¿Puedo cambiar el significado de una expresión?", "No", "Lo define la fuente."),
    ],
    task=T(
        "Haz un registro de aprendizaje con dos expresiones de la ficha (por ejemplo «mari mari» y «chaltumay»). En una tabla escribe: expresión, significado según la ficha, fuente (la ficha de la clase o la educadora tradicional) y una pregunta para la educadora sobre cuándo se usa. Escribe también cuándo vas a repetirla y con quién.",
        "«mari mari» = saludo; fuente: ficha de la clase; pregunta: ¿cuándo se usa? Repetiré el lunes con un adulto. «chaltumay» = gracias; fuente: ficha de la clase; pregunta: ¿se usa con compañeros? Repetiré el martes.",
        ["registra dos expresiones con significado y fuente", "escribe una pregunta para cada una", "no inventa significados"],
        ["tabla escrita", "preguntas dichas en voz alta"],
        ["inventar significados", "no anotar la fuente"],
        "Valora la fuente y las preguntas; si inventó un significado, pídele que vuelva a la ficha.",
    ),
    reinforce="Di en voz alta las cuatro expresiones de la ficha con su significado.",
    extend="Explica los pasos para aprender una expresión desde la fuente a otra persona.",
)

L(
    LR2, 3,
    materials="Lápiz y hoja. El modelo de intervención está escrito aquí. Si quieres, un adulto marca el tiempo.",
    use="Aprenderé a armar una intervención breve de tres partes con una expresión de la ficha. Sirve para hablar con orden frente a mi curso o mi familia.",
    prior=["Sé elegir una situación para comunicar.", "Sé aprender una expresión desde la fuente."],
    explain=[
        "Una intervención es lo que digo cuando me toca hablar. Una intervención breve dura menos de un minuto. Tiene tres partes: comienzo, idea y cierre. En el comienzo saludo. En la idea digo lo que quiero comunicar. En el cierre agradezco o me despido.",
        "Por ejemplo: comienzo con «mari mari». Idea en castellano: «Hoy aprendí que ko es agua y hay que cuidarla». Cierre con «chaltumay». Uso solo expresiones de la ficha y hablo en castellano el resto.",
        "Para prepararme, escribo mi intervención en papel y la ensayo en voz alta. Cuento mis palabras y mis segundos. Hablo despacio y miro a quien me escucha. Si me equivoco, respiro y sigo. No es una prueba: es una forma de compartir.",
    ],
    vocab=[("intervención", "lo que digo cuando me toca hablar"), ("comienzo", "la primera parte de lo que digo"), ("cierre", "la última parte de lo que digo"), ("ensayar", "practicar antes de hablar"), ("segundo", "unidad de tiempo; 60 segundos son un minuto")],
    worked=[
        W("Armar las tres partes", "Intervención de práctica: «Mari mari. Hoy aprendí que ko es agua y hay que cuidarla. Chaltumay». ¿Cuál es el cierre?", ["Veo la última palabra.", "Dice «Chaltumay».", "Es el agradecimiento."], "«Chaltumay»"),
        W("Contar palabras", "Intervención de práctica: «Hoy aprendí que ko es agua». ¿Cuántas palabras tiene?", ["Cuento una por una: Hoy, aprendí, que, ko, es, agua.", "Son seis.", "Reviso otra vez."], "6 palabras"),
    ],
    mistakes=[
        M("Hablar muy rápido para terminar pronto.", "El curso no entiende.", "Hablo despacio y hago pausas."),
        M("Inventar expresiones para sonar mejor.", "Puedo decir cosas que no existen.", "Uso solo las de la ficha y el resto en castellano."),
    ],
    R=[
        ex("Una intervención breve tiene comienzo, idea y: A) cierre B) examen.", "A", "La tercera parte es el cierre."),
        ex("En el comienzo suelo: A) saludar B) despedirme.", "A", "El comienzo abre la intervención."),
        ex("Antes de hablar frente al curso, ¿ensayo o no ensayo?", "ensayo", "Practicar ayuda a hablar con calma."),
    ],
    C=[
        ex("Verdadero o falso: una intervención breve debe durar más de diez minutos.", "Falso", "Una breve dura menos de un minuto."),
        ex("Intervención: «Mari mari. Cuidemos el agua. Chaltumay». ¿Cuál es la idea?", "Cuidemos el agua", "Es la parte del medio."),
        ex(FICHA_EXP + " En mi cierre quiero agradecer en mapuzugun. ¿Qué expresión uso?", "chaltumay", "La ficha dice que es gracias."),
    ],
    A=[
        ex("Cuenta las palabras de la idea «Cuidemos el agua todos los días».", "6", "Son: Cuidemos, el, agua, todos, los, días."),
        arith("El comienzo dura 3 segundos, la idea 12 segundos y el cierre 3 segundos. ¿Cuántos segundos dura tu intervención?", "3 + 12 + 3", "Sumo las tres partes."),
        ex("Elige una buena idea para tu intervención: A) «Hoy aprendí que antü es sol» B) «Mari mari mari mari mari».", "A", "A comunica una idea clara."),
    ],
    Z=[
        ex("Pedro dice: «Voy a poner muchas expresiones en lengua indígena para que se vea lindo». ¿Es una buena idea? Responde Sí o No.", "No", "Sería usarlas como adorno."),
        ex("Una niña se equivoca en su intervención y se queda callada. ¿Qué le conviene: respirar y seguir o quedarse sin hablar?", "respirar y seguir", "No es una prueba y puede continuar."),
    ],
    D=[
        ex("Ordena las partes: C) agradezco con «chaltumay» A) saludo con «mari mari» B) digo mi idea. Escribe las letras.", "A, B, C", "Comienzo, idea y cierre."),
        arith("Ensayas tu intervención 5 veces y cada ensayo dura 20 segundos. ¿Cuántos segundos ensayaste?", "5 * 20", "Cinco ensayos por veinte segundos."),
    ],
    context=[ex("Tu curso hará intervenciones de un minuto. La tuya dura 80 segundos. ¿Qué haces: la acorto o la dejo igual?", "la acorto", "Debe durar menos de un minuto.")],
    selfcheck=[
        ex("¿Cuáles son las tres partes de una intervención breve?", "comienzo, idea y cierre", "Son las tres partes."),
        ex("¿Cuánto dura una intervención breve?", "menos de un minuto", "Es la medida de la clase."),
        ex("¿Qué hago antes de hablar frente al curso?", "ensayo", "Practico en voz alta."),
    ],
    task=T(
        "Escribe una intervención breve de tres partes: comienzo con «mari mari»; idea en castellano sobre el agua, el sol o la luna usando «ko», «antü» o «kuyen» con su significado; cierre con «chaltumay». Cuenta las palabras, ensáyala en voz alta con un adulto y anota los segundos. Debe durar menos de un minuto. Si prefieres, puedes decirla como un personaje inventado.",
        "Mari mari. Hoy aprendí que antü es el sol y que nos da luz. Chaltumay. Palabras: 15. Tiempo: 12 segundos.",
        ["tiene comienzo, idea y cierre", "usa las expresiones de la ficha bien copiadas", "dura menos de un minuto", "ensayada en voz alta"],
        ["intervención escrita", "ensayo en voz alta con un adulto"],
        ["inventar expresiones", "pasar de un minuto"],
        "Valora la claridad y el orden; si inventó una expresión, pídele que la reemplace por una de la ficha.",
    ),
    reinforce="Lee tu intervención en voz alta tres veces, cada vez un poco más despacio.",
    extend="Escribe otra intervención con otra idea y compara cuánto dura cada una.",
)

L(
    LR2, 4,
    materials="Lápiz y hoja. Los diálogos de práctica están escritos aquí y son inventados.",
    use="Aprenderé a escuchar a la otra persona y a responderle con atención. Sirve para conversar de verdad y no solo hablar por turnos.",
    prior=["Sé armar una intervención breve.", "Sé esperar mi turno."],
    explain=[
        "Interactuar es hablar y escuchar con otra persona. No solo espero mi turno: escucho lo que dice y respondo a eso. Para hacerlo, sigo tres pasos: escucho, repito con mis palabras lo que entendí y respondo.",
        "Repetir con mis palabras me ayuda a comprobar si entendí. Puedo decir: «Entendí que…». Si no entendí, pregunto: «¿Puedes repetirlo?». Y cuando respondo, uso lo que dijo la otra persona, no una respuesta ya preparada.",
        "También cuido a quien me habla. No interrumpo, no me burlo de su manera de hablar y no le corrijo su forma de decir las palabras. Puedo usar una expresión de la ficha cuando tenga sentido, como «chaltumay» para agradecer.",
    ],
    vocab=[("interactuar", "hablar y escuchar con otra persona"), ("escuchar", "poner atención a lo que dice otra persona"), ("parafrasear", "repetir con mis palabras lo que entendí"), ("interrumpir", "hablar cuando otra persona todavía habla"), ("responder", "decir algo después de escuchar")],
    worked=[
        W("Los tres pasos", "Ana dice: «Hoy aprendí que ko es agua». Pedro responde: «Entendí que aprendiste una palabra nueva. ¿Qué otra palabra aprendiste?». ¿Qué paso hizo Pedro al decir «Entendí que aprendiste una palabra nueva»?", ["Pedro repitió con sus palabras.", "Ese es el segundo paso.", "Después hizo una pregunta."], "Repetir con sus palabras"),
        W("Pedir que repitan", "Rosa no entendió lo que dijo Luis. ¿Qué frase usa?", ["No entendió.", "Pide que repita.", "Dice: «¿Puedes repetirlo?»."], "«¿Puedes repetirlo?»"),
    ],
    mistakes=[
        M("Responder con una frase ya preparada sin escuchar.", "No sigo lo que dijo la otra persona.", "Escucho primero y respondo a lo que dijo."),
        M("Corregir la forma de hablar de quien me escucha.", "Puede ser una variante o una forma suya de hablar.", "Escucho con respeto."),
    ],
    R=[
        ex("Hablar y escuchar con otra persona se llama: A) interactuar B) interrumpir.", "A", "Interactuar es conversar."),
        ex("Repetir con mis palabras lo que entendí se llama: A) parafrasear B) corregir.", "A", "Es repetir con mis palabras."),
        ex("Si no entendí, ¿pido que repitan o me quedo callado?", "pido que repitan", "Preguntar ayuda a comprender."),
    ],
    C=[
        ex("Verdadero o falso: interrumpir ayuda a conversar mejor.", "Falso", "Hay que esperar a que la otra persona termine."),
        ex("Luis dice: «Aprendí que antü es sol». Rita responde: «Entendí que aprendiste que antü es sol». ¿Rita parafraseó? Responde Sí o No.", "Sí", "Repitió con sus palabras lo que entendió."),
        ex("Los tres pasos son escuchar, repetir con mis palabras y: A) responder B) irme.", "A", "El tercer paso es responder."),
    ],
    A=[
        ex("Pedro dice: «Hoy aprendí que kuyen es luna». ¿Qué respuesta usa los tres pasos? A) «Entendí que aprendiste que kuyen es luna. ¿Qué más aprendiste?» B) «Yo ya me sé todo.»", "A", "A repite y pregunta."),
        arith("En una conversación, Ana habla 3 veces y Pedro habla 3 veces. ¿Cuántas veces hablan entre los dos?", "3 + 3", "Sumo los turnos."),
        ex("Ana agradece a Pedro por explicarle algo. ¿Qué expresión de mapuzugun puede usar: chaltumay o mari mari?", "chaltumay", "La ficha dice que es gracias."),
    ],
    Z=[
        ex("Tomás dice: «Si yo ya sé qué voy a decir, no necesito escuchar». ¿Tiene razón? Responde Sí o No.", "No", "Sin escuchar no puedo responder a lo que dijo."),
        ex("Una niña dice «ruca» y tú sabías «ruka». ¿Qué conviene: corregirla o preguntar cómo lo dicen donde ella aprendió?", "preguntar cómo lo dicen donde ella aprendió", "Puede ser una variante válida."),
    ],
    D=[
        ex("Ordena una conversación: C) respondo con una pregunta A) escucho a Ana B) digo «Entendí que…». Escribe las letras.", "A, B, C", "Escucho, repito y respondo."),
        arith("En una conversación hay 4 turnos y en cada turno la persona habla 8 palabras. ¿Cuántas palabras se dicen?", "4 * 8", "Cuatro turnos por ocho palabras."),
    ],
    context=[ex("En el recreo un compañero te cuenta lo que aprendió de la educadora. No escuchaste una parte. ¿Qué le dices: «¿Puedes repetirlo?» o «No me interesa»?", "«¿Puedes repetirlo?»", "Pido que repita para comprender.")],
    selfcheck=[
        ex("¿Cuáles son los tres pasos de interactuar?", "escuchar, repetir con mis palabras y responder", "Son los tres pasos."),
        ex("¿Debo interrumpir a quien habla?", "No", "Espero a que termine."),
        ex("¿Qué expresión de la ficha uso para agradecer en mapuzugun?", "chaltumay", "La ficha lo dice."),
    ],
    task=T(
        "Con un compañero, un adulto o un personaje inventado, hagan una conversación de seis turnos. Cada persona dice una idea sobre el agua, el sol o la luna. Antes de responder, repite con tus palabras lo que dijo la otra persona («Entendí que…»). Usa «chaltumay» al final para agradecer. Escribe tres de los turnos en tu cuaderno.",
        "Turno 1, Ana: «Hoy aprendí que ko es agua». Turno 2, yo: «Entendí que aprendiste que ko es agua. ¿Qué más aprendiste?». Turno 3, Ana: «Que hay que cuidarla». Al final: «Chaltumay».",
        ["repite con sus palabras", "responde a lo que dijo la otra persona", "usa «chaltumay» para agradecer", "no interrumpe"],
        ["tres turnos escritos", "conversación en voz alta"],
        ["responder sin escuchar", "corregir la forma de hablar de otra persona"],
        "Observa que haya escucha y respuesta; si interrumpió o corrigió, recuérdale escuchar y preguntar.",
    ),
    reinforce="Pídele a alguien que te cuente una idea corta y repítela con tus palabras antes de responder.",
    extend="Escribe cinco frases para empezar a parafrasear, como «Entendí que…».",
)

L(
    LR2, 5,
    materials="Lápiz y hoja. La lista de revisión y las intervenciones están escritas aquí. Son inventadas.",
    use="Aprenderé a revisar si una expresión es pertinente para la situación y a pedir ayuda con la pronunciación sin juzgar a nadie. Sirve para mejorar con respeto.",
    prior=["Sé armar una intervención breve.", "Sé interactuar escuchando."],
    explain=[
        "Revisar es mirar de nuevo mi intervención para mejorarla. Reviso la pertinencia: ¿la expresión sirve para la situación? Si quiero agradecer y uso un saludo, no es pertinente. Reviso también la forma en que digo la palabra, que es la pronunciación.",
        "No puedo revisar la pronunciación solo, porque no la sé de memoria. La revisa el educador o la educadora tradicional, que escucha y me dice cómo mejorar. Yo pido: «¿Puede escucharme y decirme cómo mejorar?». Si recibo ayuda, la agradezco y vuelvo a practicar.",
        "Cuando reviso lo que dijo otra persona, uso una regla: dos cosas que estuvieron bien y una que se puede mejorar. Nunca digo que alguien habla mal ni comento su acento. Nadie es evaluado por su forma de hablar o por su identidad.",
    ],
    vocab=[("pertinencia", "que una expresión sirve para la situación"), ("pronunciación", "la manera de decir una palabra en voz alta"), ("mejorar", "hacer algo cada vez mejor"), ("acento", "la forma particular de hablar de una persona"), ("ayuda", "apoyo que me da otra persona")],
    worked=[
        W("Revisar la pertinencia", FICHA_EXP + " Quiero agradecer a la educadora y digo «mari mari». ¿Es pertinente?", ["Quiero agradecer.", "La ficha dice que «mari mari» es un saludo.", "No es pertinente; debo usar «chaltumay»."], "No, debo usar «chaltumay»"),
        W("Pedir ayuda con la pronunciación", "Pedro quiere saber si dice bien «chaltumay». ¿A quién se lo pide?", ["La pronunciación se aprende escuchando a quien conoce la lengua.", "Pedro se lo pide a la educadora tradicional.", "Le dice: «¿Puede escucharme y decirme cómo mejorar?»."], "A la educadora tradicional"),
    ],
    mistakes=[
        M("Decirle a un compañero que habla mal.", "Su forma de hablar puede ser una variante o su manera propia.", "Digo dos cosas que estuvieron bien y una por mejorar."),
        M("Creer que sé la pronunciación solo por leer.", "No la he escuchado a quien la conoce.", "Pido a la educadora que me escuche y me ayude."),
    ],
    R=[
        ex("Pertinente quiere decir que la expresión: A) sirve para la situación B) es la más larga.", "A", "Pertinente es que sirve."),
        ex("¿Quién me ayuda a revisar la pronunciación: el educador tradicional o yo con la imaginación?", "el educador tradicional", "Él conoce cómo se dice."),
        ex("Al revisar a un compañero uso: A) dos cosas buenas y una por mejorar B) solo críticas.", "A", "Es una forma respetuosa."),
    ],
    C=[
        ex(FICHA_EXP + " Quiero saludar y digo «chaltumay». ¿Es pertinente? Responde Sí o No.", "No", "«Chaltumay» es gracias, no saludo."),
        ex("Verdadero o falso: puedo comentar el acento de otra persona para ayudarla.", "Falso", "Nadie debe ser juzgado por su forma de hablar."),
        ex("Pedro pide: «¿Puede escucharme y decirme cómo mejorar?». ¿A quién se lo pide mejor: al educador tradicional o a un compañero que tampoco lo sabe?", "al educador tradicional", "Él conoce la pronunciación."),
    ],
    A=[
        ex(FICHA_EXP + " Revisa: Rosa quiere agradecer a una persona invitada en rapa nui y dice «iorana». ¿Qué expresión es pertinente: iorana o maururu?", "maururu", "La ficha dice que «maururu» es gracias en rapa nui."),
        arith("Tienes 3 cosas buenas y 1 cosa por mejorar para la intervención de Ana. ¿Cuántos comentarios das en total?", "3 + 1", "Sumo las cosas buenas y la que mejora."),
        ex("Elige la mejor revisión de la intervención de un compañero: A) «Me gustó cómo saludaste y tu idea fue clara. Podrías hablar un poco más despacio.» B) «Hablas mal.»", "A", "A dice cosas buenas y una por mejorar."),
    ],
    Z=[
        ex("Luis dice: «Si digo la palabra distinto a la educadora, es un error grave». ¿Tiene razón? Responde Sí o No.", "No", "Practicar y recibir ayuda es parte de aprender."),
        ex("Una niña dice «ruca» y otra dice «ruka». ¿Cuál es el error? Responde: ninguno o una de las dos.", "ninguno", "Son dos escrituras de la misma palabra."),
    ],
    D=[
        ex("Ordena para revisar: C) practico de nuevo A) reviso si la expresión es pertinente B) pido a la educadora que me escuche. Escribe las letras.", "A, B, C", "Reviso, pido ayuda y practico."),
        arith("Practicas tu intervención 3 veces después de recibir ayuda y cada vez dura 20 segundos. ¿Cuántos segundos practicaste?", "3 * 20", "Tres veces por veinte segundos."),
    ],
    context=[ex("Un compañero terminó su intervención y te toca decir un comentario. ¿Qué dices: «Me gustó que saludaras y fue clara tu idea; podrías hablar más despacio» o «Hablas muy raro»?", "«Me gustó que saludaras y fue clara tu idea; podrías hablar más despacio»", "Dice cosas buenas y una por mejorar, sin juzgar.")],
    selfcheck=[
        ex("¿Qué reviso en una intervención?", "la pertinencia y la pronunciación", "Son los dos criterios de la clase."),
        ex("¿Quién revisa la pronunciación de una expresión en lengua indígena?", "el educador tradicional", "Él conoce la forma de decirla."),
        ex("¿Debo comentar el acento de una persona?", "No", "Nadie es evaluado por cómo habla."),
    ],
    task=T(
        "Revisa esta intervención inventada de una niña llamada Rosa: «Iorana. Hoy quiero agradecer a la educadora. Mari mari». " + FICHA_EXP + " Escribe: 1) si cada expresión es pertinente o no y cuál usarías en vez de la que no lo es, 2) dos cosas buenas que dirías a Rosa y una por mejorar, 3) una pregunta para el educador tradicional sobre cómo se pronuncia una de las expresiones.",
        "«Iorana» es saludo en rapa nui y está bien al comienzo. «Mari mari» no es pertinente para cerrar agradeciendo; usaría «chaltumay» o «maururu» según su lengua. Bien: saludó y dijo su idea con claridad. Mejorar: hablar más despacio. Pregunta: ¿puede decirme cómo se pronuncia «maururu»?",
        ["evalúa la pertinencia de cada expresión", "da dos cosas buenas y una por mejorar", "no comenta el acento", "hace una pregunta al educador/a"],
        ["revisión escrita", "pregunta escrita o dicha en voz alta"],
        ["decir que alguien habla mal", "decidir la pronunciación sin preguntar"],
        "Valora que revisó con la ficha y con respeto; si comentó el acento, recuérdale que nadie es evaluado por cómo habla.",
    ),
    reinforce="Elige una expresión de la ficha y di en qué situación es pertinente y en cuál no.",
    extend="Escribe una regla propia para dar comentarios amables sobre la intervención de otra persona.",
)
