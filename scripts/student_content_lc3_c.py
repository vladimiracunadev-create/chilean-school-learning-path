"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR03 (comprensión de textos breves con expresiones culturalmente significativas) y
OA LR04 (escritura de palabras y frases simples), contexto de rescate y revitalización.

Criterio de autoría: todos los textos, fichas, escuelas y personas son inventados solo para practicar y están rotulados
como tales; no se adapta ningún relato tradicional. Las únicas expresiones en lengua indígena son saludos y palabras
muy atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke); no se inventa gramática, pronunciación ni
significados rituales. Las frases de la clase LR04 son frases en castellano que llevan la palabra indígena entre
paréntesis; las frases completas en lengua indígena las enseña el educador/a tradicional. Cada tarea abierta remite al
educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LR3, LR4 = "LC03 OA LR03", "LC03 OA LR04"

CONSULT = " Recuerda: la forma tradicional de escribir, decir y usar estas palabras la enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de escritura, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

FICHA_PAL = "Ficha de palabras en mapuzugun (de práctica): «ko» es agua, «antü» es sol, «kuyen» es luna, «ruka» es la casa mapuche, «mapu» es tierra, «ñuke» es madre."
FICHA_SAL = "Ficha: «mari mari» es un saludo y «chaltumay» quiere decir «gracias», ambas en mapuzugun."


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


# =================================================================== LR03 clase 1 · fuente y propósito
FP_A = "Ficha de procedencia A (inventada para practicar): Texto: «Bienvenida a la visita». Escrito por: el curso de una Escuela Ejemplo (inventada). Fuente de las palabras en lengua indígena: la educadora tradicional de la escuela. Permiso para usar las palabras: sí. Para qué se escribió: dar la bienvenida."

L(
    LR3, 1,
    materials="Lápiz y hoja. Las fichas y los textos están escritos en este cuaderno. Son inventados para practicar: no pertenecen a ninguna escuela, persona ni pueblo reales.",
    use="Aprenderé a leer una ficha de procedencia y a decir de dónde viene un texto y para qué se escribió. Sirve para leer con respeto los textos que traen palabras de una lengua indígena.",
    prior=["Sé encontrar una expresión entre comillas dentro de un texto.", "Sé que el educador o la educadora tradicional enseña la lengua y la cultura de su pueblo."],
    explain=[
        "Antes de entender un texto, conviene saber de dónde viene. La procedencia es el lugar, la persona o el grupo de donde sale un texto o una palabra. Esos datos se anotan en una ficha de procedencia. La fuente es quien sabe esa palabra y la comparte, por ejemplo un educador tradicional.",
        "El propósito es para qué se escribió el texto: saludar, agradecer, invitar, contar o enseñar. Para reconocerlo leo el texto completo y me pregunto qué quería lograr quien lo escribió. No es lo mismo que la fuente: la fuente es quién lo sabe; el propósito es para qué sirve el texto.",
        "La ficha también dice si hay permiso. El permiso es el sí de quien sabe y cuida esas palabras para usarlas de cierta manera. Si en la ficha falta la fuente o el permiso, me detengo y pregunto. No adivino ni invento de dónde viene una palabra.",
    ],
    vocab=[("procedencia", "lugar, persona o grupo de donde viene un texto"), ("fuente", "quien sabe una palabra y la comparte"), ("propósito", "para qué se escribió un texto"), ("permiso", "el sí de quien cuida unas palabras para usarlas"), ("ficha de procedencia", "papel que anota de dónde viene un texto")],
    worked=[
        W("Leer una ficha", FP_A + " ¿Cuál es el propósito del texto?", ["Busco en la ficha la línea «Para qué se escribió».", "Dice: dar la bienvenida.", "Ese es el propósito."], "dar la bienvenida"),
        W("Detenerse si falta un dato", "Ficha B (inventada): Texto: «Un saludo». Escrito por: un niño del curso. Fuente de las palabras: no se indica. Permiso: no se indica. ¿Puedo usar la palabra «mari mari» de ese texto en un cartel?", ["Reviso los datos de la ficha.", "Faltan la fuente y el permiso.", "Me detengo y pregunto al profesor o al educador tradicional."], "no todavía: faltan la fuente y el permiso; pregunto"),
    ],
    mistakes=[
        M("Decir que el propósito de un texto es lo mismo que su fuente.", "La fuente es quien sabe las palabras; el propósito es para qué se escribió.", "Pregunto dos cosas distintas: ¿quién lo sabe? y ¿para qué sirve?"),
        M("Usar una palabra en lengua indígena aunque la ficha no diga la fuente.", "Sin fuente no sé si la palabra está bien ni si se puede usar.", "Me detengo y pregunto antes de usarla."),
    ],
    R=[
        ex(FP_A + " ¿Quién es la fuente de las palabras en lengua indígena?", "la educadora tradicional de la escuela", "La ficha lo dice en la línea «Fuente de las palabras»."),
        ex("Un texto se escribió para dar la bienvenida a una visita. ¿Eso es su propósito o su fuente?", "su propósito", "Dice para qué se escribió el texto."),
        ex("En la ficha A, ¿qué dato dice si se pueden usar las palabras: el permiso o el título?", "el permiso", "El permiso es el sí para usarlas."),
    ],
    C=[
        ex("Texto de práctica: «Mari mari, queridos vecinos. Los invitamos a la reunión del curso el viernes.» ¿Cuál es el propósito: invitar o despedirse?", "invitar", "El texto invita a una reunión."),
        ex("Ficha C (inventada): Texto: «Gracias a la educadora». Escrito por: una niña del curso. Fuente de las palabras: no se indica. Permiso: no se indica. ¿Qué dos datos faltan?", "la fuente y el permiso", "La ficha dice «no se indica» en esas dos líneas."),
        ex("Verdadero o falso: un texto sin fuente indicada es seguro para copiar sus palabras en lengua indígena.", "Falso", "Sin fuente no sé si las palabras son correctas."),
    ],
    A=[
        ex("Tres fichas. A) Fuente: educador tradicional; permiso: sí. B) Fuente: «lo vi en una pantalla»; permiso: no se indica. C) Fuente: «mi memoria»; permiso: no. ¿Cuál ficha está mejor documentada?", "A", "Solo A tiene una fuente que sabe la lengua y un permiso."),
        ex(FICHA_SAL + " Escribe el propósito de cada texto, en orden: 1) «Chaltumay, Rosa, por prestarme el lápiz.» 2) «Mari mari, bienvenida a nuestra sala.»", "agradecer, saludar", "El primero da las gracias y el segundo saluda."),
        ex("Una ficha completa tiene 5 datos: título, quién lo escribió, fuente, permiso y propósito. Un papel solo trae título y quién lo escribió. ¿Qué tres datos le faltan?", "la fuente, el permiso y el propósito", "Son los datos de la ficha completa que el papel no trae."),
    ],
    Z=[
        ex("Pedro dice: «La fuente de un texto y su propósito son lo mismo». ¿Tiene razón?", "No", "La fuente es quién sabe las palabras y el propósito es para qué se escribió."),
        ex("Un texto trae la palabra «mari mari» y su ficha no tiene fuente. Opciones: A) usarla igual. B) detenerme y preguntar al profesor o al educador tradicional. ¿Cuál eliges?", "B", "Sin fuente no sé si puedo usar la palabra."),
    ],
    D=[
        ex("Ficha D (inventada): Texto: «Chaltumay». Fuente: la educadora tradicional de la Escuela Ejemplo. Permiso: solo para usar dentro de la sala, no para publicar. Propósito: agradecer. ¿Puedes subir el texto a un sitio abierto de internet? Responde Sí o No.", "No", "El permiso solo vale dentro de la sala."),
        ex("Ordena los pasos antes de usar una palabra: A) la uso solo como el permiso lo dice. B) leo la ficha de procedencia. C) reviso quién es la fuente. Escribe las letras en orden.", "B, C, A", "Primero leo la ficha, luego miro la fuente y al final uso la palabra con permiso."),
    ],
    context=[ex("Llega a tu sala un papel con la palabra «mari mari» escrita en grande y sin ficha. ¿Qué haces primero: pegarlo en la pared o preguntar de dónde viene?", "preguntar de dónde viene", "Sin ficha no conozco la fuente ni el permiso.")],
    selfcheck=[
        ex("¿Cómo se llama el dato que dice para qué se escribió un texto?", "el propósito", "Propósito es el para qué del texto."),
        ex("Si en una ficha falta la fuente, ¿sigo adelante o me detengo y pregunto?", "me detengo y pregunto", "No se usa una palabra de la que no conozco la fuente."),
        ex("¿Qué línea de la ficha me dice si puedo usar las palabras?", "el permiso", "El permiso autoriza el uso."),
    ],
    task=T(
        "Lee esta ficha y este texto, ambos inventados para practicar. Ficha: Texto: «Hoy aprendimos». Escrito por: el curso de la Escuela Ejemplo. Fuente de las palabras: la educadora tradicional de la escuela. Permiso: sí, para usar dentro de la sala. Texto: «Mari mari, familias. Hoy aprendimos a saludar. Chaltumay por venir a escucharnos.» " + FICHA_SAL + " En tu cuaderno escribe: 1) la fuente, 2) el permiso y hasta dónde llega, 3) el propósito del texto. Al final escribe una pregunta para la educadora tradicional.",
        "Fuente: la educadora tradicional de la escuela. Permiso: sí, solo dentro de la sala. Propósito: saludar y agradecer a las familias. Pregunta: ¿cómo saludan en su comunidad?",
        ["anota la fuente tal como dice la ficha", "dice que el permiso es solo dentro de la sala", "da un propósito coherente con el texto", "formula una pregunta para el educador/a tradicional"],
        ["tres líneas escritas en el cuaderno", "pregunta escrita o dicha en voz alta"],
        ["confundir fuente con propósito", "decir que el texto se puede publicar"],
        "Observa que separó fuente, permiso y propósito; si escribió un dato que la ficha no trae, pídele que lo cambie por una pregunta.",
    ),
    reinforce="Lee de nuevo la ficha A y señala con el dedo la línea de la fuente, la del permiso y la del propósito.",
    extend="Inventa una ficha de procedencia de cuatro líneas para un cartel de tu sala. Si no conoces la fuente de una palabra, escribe «por preguntar» en esa línea.",
)

# =================================================================== LR03 clase 2 · localizar expresiones
TXT_A = "Texto de práctica A (inventado): «Al entrar a la sala, la educadora dijo «mari mari». Luego escribió «ruka» en la pizarra y nos contó que esa palabra nombra la casa mapuche. Al final todos dijimos «chaltumay».»"

L(
    LR3, 2,
    materials="Lápiz y hoja. Los textos y las fichas están escritos aquí; son inventados para practicar.",
    use="Aprenderé a localizar, dentro de un texto, todas las expresiones significativas y a separarlas según su lengua. Sirve para no dejar ninguna fuera ni inventar las que no están.",
    prior=["Sé que una expresión puede tener una o más palabras.", "Sé leer una ficha de procedencia."],
    explain=[
        "Una expresión significativa es una palabra o grupo de palabras que tiene un valor cultural especial en el texto. Puede estar en lengua indígena, como «mari mari», o en castellano, como «territorio» o «comunidad», cuando el texto la usa con ese valor y lo explica.",
        "Para localizarlas hago tres pasos. Primero leo todo el texto. Segundo marco lo que va entre comillas, expresión completa y no solo un pedazo. Tercero leo la ficha y escribo al lado de cada una su lengua: lengua indígena o castellano.",
        "Hay un cuidado más. Una palabra sin comillas ni ficha no es una expresión significativa para este trabajo; no la marco. Y si una expresión se repite, la cuento una sola vez cuando me piden expresiones distintas.",
    ],
    vocab=[("expresión significativa", "palabra o grupo de palabras con valor cultural en el texto"), ("localizar", "encontrar algo dentro de un texto"), ("completa", "con todas sus palabras, sin dejar partes"), ("distintas", "que no son iguales entre sí"), ("territorio", "lugar donde vive y se cuida una comunidad")],
    worked=[
        W("Marcar y contar", TXT_A + " " + FICHA_SAL + " Ficha: «ruka» es la casa mapuche en mapuzugun. ¿Cuántas expresiones en lengua indígena hay?", ["Marco lo que va entre comillas: «mari mari», «ruka», «chaltumay».", "Reviso en las fichas que las tres son de mapuzugun.", "Cuento: 1, 2, 3."], "3"),
        W("Expresión repetida", "Texto: «Dijo «chaltumay» al entrar. Después, al salir, volvió a decir «chaltumay» y «mari mari».» ¿Cuántas expresiones distintas hay?", ["Marco todas: «chaltumay», «chaltumay», «mari mari».", "La primera y la segunda son iguales.", "Distintas hay solo dos."], "2"),
    ],
    mistakes=[
        M("Marcar solo «mari» y dejar afuera el segundo «mari».", "La expresión completa tiene dos palabras.", "Marco todo lo que va junto entre comillas: «mari mari»."),
        M("Marcar una palabra del castellano solo porque me parece importante.", "Si el texto no la destaca ni la explica, no es la expresión que busco.", "Marco lo que va entre comillas y tiene ficha."),
    ],
    R=[
        ex(TXT_A + " ¿Qué expresión dijo la educadora al entrar a la sala?", "mari mari", "El texto la pone entre comillas al entrar."),
        ex("¿Qué marca me ayuda a encontrar las expresiones en estos textos: las comillas o los números?", "las comillas", "En este cuaderno las expresiones van entre comillas."),
        ex("Del texto A, ¿qué palabra escribió la educadora en la pizarra?", "ruka", "El texto dice que escribió «ruka»."),
    ],
    C=[
        ex("Texto de práctica B (inventado): «El lunes la profesora leyó «ko» y «antü» en la ficha. Dijo que «ko» es agua y que «antü» es sol.» ¿Cuántas expresiones distintas en lengua indígena hay?", "2", "Solo aparecen «ko» y «antü», aunque cada una se repite."),
        ex("Verdadero o falso: una palabra en castellano sin comillas ni ficha es una expresión en lengua indígena.", "Falso", "Sin comillas ni ficha no puedo decir de qué lengua es."),
        ex("Marta marcó solo «mari» en «mari mari». ¿Qué error cometió?", "marcó solo una parte de la expresión", "La expresión completa lleva las dos palabras."),
    ],
    A=[
        ex("Texto de práctica C (inventado): «Mi curso hizo un cartel. Escribimos «mari mari» arriba, «kuyen» y «antü» en medio y «chaltumay» abajo.» Escribe en orden las expresiones que aparecen.", "mari mari, kuyen, antü, chaltumay", "Van en el orden en que las cita el texto."),
        ex("En el cartel del texto C, ¿cuántas expresiones son un saludo o un agradecimiento según la ficha de saludos?", "2", "«Mari mari» saluda y «chaltumay» agradece."),
        ex(FICHA_PAL + " En el texto C, ¿cuáles expresiones nombran algo del cielo?", "kuyen y antü", "Según la ficha, kuyen es luna y antü es sol."),
    ],
    Z=[
        ex("Texto de práctica D (inventado): «La educadora tradicional visitó el curso. Habló del respeto por el territorio y del cuidado de la comunidad.» Ficha: «territorio» y «comunidad» son expresiones en castellano que el texto usa con valor cultural. ¿Todas las expresiones significativas de este texto están en lengua indígena? Sí o No.", "No", "En el texto D las expresiones significativas están en castellano."),
        ex("Un niño dice: «En el texto A hay una expresión significativa en castellano: «casa»». ¿Qué le falta para que sea cierto: comillas y ficha, o más letras?", "comillas y ficha", "El texto A marca «ruka» y no destaca «casa» como expresión."),
    ],
    D=[
        ex("Texto de práctica E (inventado): «La educadora dijo «mari mari». Habló del respeto por el «territorio». Escribió «mapu» y «ruka» en la pizarra.» Ficha: «mapu» es tierra y «ruka» es la casa mapuche en mapuzugun; «territorio» es una expresión en castellano. Responde con dos números: expresiones en lengua indígena y expresiones en castellano entre comillas.", "3 y 1", "En lengua indígena hay mari mari, mapu y ruka; en castellano, territorio."),
        ex("Un texto repite 4 veces «mari mari» y 2 veces «chaltumay». ¿Cuántas expresiones distintas en lengua indígena tiene?", "2", "Las repeticiones no cuentan como expresiones distintas."),
    ],
    context=[ex("Tu escuela publica un afiche de práctica: «Chaltumay a las familias por venir a la reunión. Mari mari a todos.» ¿Cuántas expresiones en lengua indígena hay?", "2", "Hay «chaltumay» y «mari mari».")],
    selfcheck=[
        ex("Si una palabra entre comillas no tiene ficha, ¿la clasifico o pregunto de qué lengua es?", "pregunto de qué lengua es", "Sin ficha no puedo adivinar su lengua."),
        ex("Una expresión de dos palabras, como «mari mari», ¿se marca completa o por partes?", "completa", "La expresión se marca entera."),
        ex("Además de la lengua indígena, ¿en qué otra lengua puede haber una expresión significativa en un texto?", "en castellano", "El texto puede destacar expresiones en castellano."),
    ],
    task=T(
        "Lee este texto inventado para practicar: «Una visita llegó a la sala y dijo «mari mari». Habló de la «comunidad» y escribió «kuyen» y «ko» en la pizarra. Al despedirse dijimos «chaltumay».» " + FICHA_SAL + " " + FICHA_PAL + " Ficha: «comunidad» es una expresión en castellano que el texto destaca. En una tabla de dos columnas escribe las expresiones en lengua indígena en una y las expresiones en castellano en la otra. Después escribe una pregunta para el educador o la educadora tradicional.",
        "Lengua indígena: mari mari, kuyen, ko, chaltumay. Castellano: comunidad. Pregunta: ¿cuándo se dice «chaltumay» en su comunidad?",
        ["encuentra las cinco expresiones", "las separa en las dos columnas correctas", "marca cada expresión completa", "formula una pregunta para el educador/a tradicional"],
        ["tabla de dos columnas", "pregunta escrita o dicha en voz alta"],
        ["marcar solo una parte de «mari mari»", "agregar palabras que el texto no marca"],
        "Verifica que separó las lenguas con ayuda de las fichas; si agregó expresiones que el texto no marca, vuelve a leer con él las comillas.",
    ),
    reinforce="Lee en voz alta el texto B y levanta una mano cada vez que oigas una expresión en lengua indígena.",
    extend="Escribe un texto de tres oraciones que tenga exactamente dos expresiones entre comillas, tomadas de las fichas de esta clase.",
)

# =================================================================== LR03 clase 3 · relacionar información interna
TXT_F = "Texto de práctica F (inventado): «Ana llegó temprano a la sala porque la educadora tradicional venía de visita. Preparó una hoja con la palabra «chaltumay» para agradecerle. Cuando la educadora entró, Ana sonrió y dijo «mari mari». Al despedirse, Ana le entregó la hoja y la educadora sonrió también.»"

L(
    LR3, 3,
    materials="Lápiz y hoja. El texto y las fichas están escritos aquí; los personajes son inventados.",
    use="Aprenderé a relacionar las partes de un texto entre sí: quién hizo qué, por qué y en qué orden. Sirve para comprender textos con palabras de otra lengua sin quedarme solo con las palabras raras.",
    prior=["Sé localizar expresiones entre comillas.", "Sé usar la ficha para saber qué significa una expresión."],
    explain=[
        "Relacionar información interna es unir datos que están dentro del mismo texto. Puedo unir quién hace algo con lo que hace, una causa con su efecto, y un hecho con otro según el orden en que ocurren. Palabras como «porque», «luego» y «al final» son pistas.",
        "Algunas cosas el texto las dice directo, como «Ana llegó temprano». Otras las puedo deducir con pistas. Si un personaje sonrió, puede sentir alegría. Una deducción vale cuando tiene una pista escrita en el texto; si no hay pista, no la afirmo.",
        "Las expresiones en lengua indígena también se relacionan con el resto. Uso la ficha para saber qué significan y el texto para saber cuándo y por qué se dijeron. Así entiendo la escena completa y no solo la palabra.",
    ],
    vocab=[("causa", "lo que hace que algo ocurra"), ("efecto", "lo que ocurre por esa causa"), ("pista", "dato del texto que ayuda a entender algo"), ("deducir", "llegar a una idea usando pistas del texto"), ("orden", "primero, luego y al final")],
    worked=[
        W("Causa y efecto", TXT_F + " ¿Por qué llegó temprano Ana?", ["Busco la palabra «porque» en el texto.", "Después de «porque» dice que la educadora venía de visita.", "Esa es la causa."], "porque la educadora tradicional venía de visita"),
        W("Deducir con una pista", TXT_F + " ¿Qué sentía Ana al ver entrar a la educadora?", ["Busco una pista: «Ana sonrió».", "Sonreír se relaciona con la alegría.", "Concluyo que probablemente sentía alegría."], "alegría"),
    ],
    mistakes=[
        M("Afirmar algo del texto sin ninguna pista escrita.", "Estaría inventando una idea que el texto no apoya.", "Busco una pista en el texto antes de responder."),
        M("Contar los hechos en un orden distinto al del texto.", "El orden cambia lo que ocurrió primero y lo que ocurrió después.", "Voy marcando «primero», «luego» y «al final» mientras leo."),
    ],
    R=[
        ex(TXT_F + " ¿Qué palabra preparó Ana en la hoja?", "chaltumay", "El texto dice que preparó una hoja con «chaltumay»."),
        ex("En el texto F, ¿qué dijo Ana cuando entró la educadora?", "mari mari", "Ana sonrió y dijo «mari mari»."),
        ex("En el texto F, ¿por qué Ana llegó temprano?", "porque la educadora venía de visita", "Lo dice la parte que sigue a «porque»."),
    ],
    C=[
        ex(FICHA_SAL + " Según el texto F, ¿para qué preparó Ana la hoja con «chaltumay»?", "para agradecer a la educadora", "El texto dice «para agradecerle»."),
        ex("En el texto F, ¿qué ocurrió primero: Ana dijo «mari mari» o Ana entregó la hoja?", "Ana dijo «mari mari»", "La entrega ocurre al despedirse, al final."),
        ex("En el texto F, Ana sonrió. ¿Qué emoción es más probable: alegría o enojo?", "alegría", "Sonreír es una pista de alegría."),
    ],
    A=[
        ex("Une cada hecho con su motivo. Hechos: 1) Ana llegó temprano. 2) Ana preparó la hoja. Motivos: a) para agradecer. b) porque venía una visita. Escribe las parejas.", "1-b, 2-a", "Llegó temprano porque venía una visita y preparó la hoja para agradecer."),
        ex("¿Cuántas veces se dice en el texto F que un personaje sonrió?", "2", "Ana sonrió y la educadora sonrió también."),
        ex("En el texto F, ¿quién entregó la hoja y a quién?", "Ana a la educadora", "El texto dice «Ana le entregó la hoja»."),
    ],
    Z=[
        ex("Un niño dice: «Ana estaba enojada porque llegó temprano». ¿Qué frase del texto F muestra lo contrario? A) «Ana sonrió y dijo «mari mari»». B) «La educadora venía de visita».", "A", "Sonreír y saludar no son pistas de enojo."),
        ex("Si el texto F no dijera por qué llegó temprano Ana, ¿podría afirmar la razón con seguridad? Sí o No.", "No", "Sin una pista escrita estaría inventando."),
    ],
    D=[
        ex("Ordena los hechos del texto F: A) La educadora entró. B) Ana entregó la hoja. C) Ana preparó la hoja. D) Ana llegó temprano. Escribe las letras.", "D, C, A, B", "Llegó, preparó, la educadora entró y al final entregó la hoja."),
        ex("¿Qué título reúne más información del texto F? A) «Una visita llega a la sala». B) «Ana prepara un agradecimiento y saluda a una visita».", "B", "El título B incluye lo que hace Ana además de la visita."),
    ],
    context=[ex("Una compañera te cuenta: «Hoy llegué temprano porque iba a venir una visita, y le escribí «chaltumay» en una hoja». Con la ficha de saludos, ¿para qué escribió esa palabra?", "para agradecer", "Según la ficha «chaltumay» quiere decir «gracias».")],
    selfcheck=[
        ex("¿Qué palabra suele unir una causa con su efecto: porque o también?", "porque", "«Porque» muestra la causa."),
        ex("Para saber qué ocurrió primero, ¿sigo el orden del texto o lo invento?", "sigo el orden del texto", "El texto marca primero, luego y al final."),
        ex("¿Una pista escrita, como «sonrió», me ayuda a deducir una emoción?", "Sí", "Una pista sostiene la deducción."),
    ],
    task=T(
        "Lee este texto inventado para practicar: «Tomás llegó antes que sus compañeros porque quería ordenar la sala. Escribió «mari mari» en un cartel para recibir a la visita. Cuando todos llegaron, dijeron «chaltumay» a la educadora por venir.» " + FICHA_SAL + " En tu cuaderno haz una tabla de tres filas: 1) una causa y su efecto, 2) el orden de los hechos con «primero», «luego» y «al final», 3) una emoción posible con su pista. Termina con una pregunta para la educadora tradicional.",
        "Causa: Tomás llegó antes porque quería ordenar la sala. Orden: primero llegó, luego escribió el cartel, al final todos dijeron «chaltumay». Emoción posible: cariño, pista: recibir a la visita con un cartel. Pregunta: ¿cómo se recibe a una visita en su comunidad?",
        ["une una causa con su efecto", "ordena los hechos con las palabras de orden", "justifica la emoción con una pista del texto", "formula una pregunta para el educador/a tradicional"],
        ["tabla de tres filas", "pregunta escrita o dicha en voz alta"],
        ["afirmar algo sin pista", "cambiar el orden de los hechos"],
        "Comprueba que cada afirmación tenga una pista del texto; si inventó algo, pídele que lo cambie por una pregunta.",
    ),
    reinforce="Vuelve a leer el texto F y subraya con un lápiz las palabras «porque», «cuando» y «al despedirse».",
    extend="Escribe una oración que relacione dos hechos del texto F usando la palabra «porque».",
)

# =================================================================== LR03 clase 4 · responder sin exigir vivencias
TXT_G = "Texto de práctica G (inventado): «Mateo escuchó a una visita decir «mari mari» y sintió curiosidad. Nunca había oído esa expresión. Quiso saber más y levantó la mano para preguntar con respeto.»"

L(
    LR3, 4,
    materials="Lápiz y hoja. Los textos están escritos aquí. Nadie tiene que contar nada de su vida privada para hacer esta clase.",
    use="Aprenderé a relacionar un texto con lo que sé, lo que imagino y lo que siento, sin tener que contar cosas privadas. Sirve para participar con respeto y para no presionar a nadie.",
    prior=["Sé relacionar información dentro de un texto.", "Sé que una emoción es lo que siento por dentro."],
    explain=[
        "Cuando leo, puedo unir el texto con mis conocimientos y mis emociones. Mis conocimientos son lo que sé por haberlo leído, escuchado o aprendido. Mis emociones son lo que siento, como curiosidad, alegría, respeto o nervios. Todas sirven para responder.",
        "Pero nadie tiene que contar cosas privadas. Ninguna persona está obligada a decir de qué pueblo es, qué hace su familia ni qué sabe de una lengua. Puedo responder con algo que aprendí en un libro, con algo que imagino o con lo que siento hoy.",
        "Tampoco pregunto a otros por su origen ni les pido que hablen por su pueblo. Si quiero saber más sobre una cultura, hago preguntas sobre el texto o se las hago al educador o a la educadora tradicional, que es quien enseña.",
    ],
    vocab=[("conocimiento", "lo que sé porque lo aprendí"), ("emoción", "lo que siento, como alegría o curiosidad"), ("privado", "que cada persona decide si cuenta o no"), ("obligar", "exigir que alguien haga algo aunque no quiera"), ("origen", "familia o pueblo del que viene una persona")],
    worked=[
        W("Elegir una pregunta respetuosa", "Dos preguntas para el curso: A) «¿Qué sentiste al leer el texto G?». B) «¿Eres de un pueblo originario?». ¿Cuál respeta la privacidad?", ["Reviso qué pide cada pregunta.", "La A pregunta por mi emoción al leer.", "La B pide un dato privado."], "A"),
        W("Relacionar con lo que sé", "Texto: «Sofía leyó que «ko» es agua. Pensó en el agua que toma en el recreo y se sintió tranquila.» ¿Con qué relacionó Sofía la palabra?", ["Busco qué pensó Sofía.", "Pensó en el agua que toma en el recreo.", "Con eso relacionó la palabra."], "con el agua que toma en el recreo"),
    ],
    mistakes=[
        M("Pensar que, para responder, tengo que contar la historia de mi familia.", "Una respuesta puede salir de lo que sé, imagino o siento.", "Respondo con una emoción o con algo que aprendí."),
        M("Preguntarle a un compañero de qué pueblo es.", "Es un dato privado y no debo presionarlo.", "Pregunto por el texto o le pregunto al educador tradicional."),
    ],
    R=[
        ex(TXT_G + " ¿Qué sintió Mateo?", "curiosidad", "El texto lo dice al inicio."),
        ex("En el texto G, ¿Mateo había oído antes esa expresión?", "No", "El texto dice que nunca la había oído."),
        ex("En el texto G, ¿qué hizo Mateo para saber más?", "levantó la mano para preguntar con respeto", "Es lo que dice la última oración."),
    ],
    C=[
        ex("¿Cuál pregunta respeta la privacidad? A) «¿Qué sentiste al leer el texto G?». B) «¿Dónde viven tus abuelos?».", "A", "La B pide un dato privado de la familia."),
        ex("Verdadero o falso: para responder una pregunta del texto, una estudiante debe contar la historia de su familia.", "Falso", "Puede responder con lo que sabe, imagina o siente."),
        ex("Formas de responder: A) con algo que leí. B) con algo que imagino. C) con una emoción mía de hoy. Si ninguna exige contar datos privados, ¿cuántas son válidas?", "3", "Las tres son válidas y respetan la privacidad."),
    ],
    A=[
        ex("Completa con el texto G: «Mateo sintió ____ porque nunca había oído esa expresión». Elige: curiosidad, miedo o aburrimiento.", "curiosidad", "El texto dice que sintió curiosidad."),
        ex("Texto H (inventado): «Sofía leyó que «ko» es agua. Pensó en el agua que toma en el recreo y se sintió tranquila.» ¿Con qué relacionó Sofía la palabra «ko»?", "con el agua que toma en el recreo", "Lo dice la segunda oración."),
        ex("En el texto H, ¿Sofía tuvo que contar algo de su familia para relacionar la palabra con su vida?", "No", "Usó una situación cotidiana del recreo."),
    ],
    Z=[
        ex("Lucas dice: «Si no soy de un pueblo originario, no puedo responder las preguntas». ¿Tiene razón?", "No", "Cualquier estudiante puede responder con lo que sabe, imagina o siente."),
        ex("Un compañero pregunta: «¿Quién del curso es mapuche? Levanten la mano». ¿Es una pregunta adecuada? Sí o No.", "No", "Pide un dato privado y puede exponer a alguien."),
    ],
    D=[
        ex("¿Cuál reemplaza mejor la pregunta «¿Cuéntanos qué hace tu familia indígena?»? A) «¿Qué piensas de lo que escuchamos en el texto?». B) «¿Dónde viven tus abuelos?».", "A", "La A pregunta por el texto y no por datos privados."),
        ex("Ordena para responder con respeto: A) leo la pregunta. B) pienso en lo que sé o siento. C) escribo sin contar datos privados. Escribe las letras en orden.", "A, B, C", "Leo, pienso y escribo cuidando la privacidad."),
    ],
    context=[ex("En tu curso leyeron el texto G. Una compañera no quiere contar si conoce el saludo «mari mari». ¿Qué le dices: «Puedes responder con lo que sientes o imaginas» o «Tienes que decirlo»?", "«Puedes responder con lo que sientes o imaginas»", "Nadie está obligado a contar lo que no quiere.")],
    selfcheck=[
        ex("¿Quién decide qué cosas de su vida cuenta a los demás?", "cada persona", "Los datos privados los decide cada uno."),
        ex("¿Puedo responder con una emoción aunque no conozca la lengua indígena?", "Sí", "Una emoción es una respuesta válida."),
        ex("¿Qué dato no debo pedirle a un compañero: su origen o su opinión sobre el texto?", "su origen", "El origen es un dato privado."),
    ],
    task=T(
        "Lee este texto inventado para practicar: «Un niño escuchó «chaltumay» en la sala. Vio que la visita sonreía. Él también sonrió y sintió alegría.» " + FICHA_SAL + " Escribe tres respuestas con las frases que siguen: «Yo sé que…» (algo que aprendiste hoy), «Yo imagino que…» (algo que imaginas del niño) y «Yo siento…» (una emoción tuya hoy). Para cada una puedes escoger lo que prefieras: nadie leerá datos privados. Al final escribe una pregunta sobre el texto para la educadora tradicional.",
        "Yo sé que «chaltumay» es gracias en mapuzugun. Yo imagino que el niño quería dar las gracias. Yo siento curiosidad. Pregunta: ¿cuándo se dice «chaltumay» en su comunidad?",
        ["escribe las tres frases pedidas", "no cuenta datos privados de otras personas", "su respuesta tiene que ver con el texto", "formula una pregunta para el educador/a tradicional"],
        ["tres frases escritas", "pregunta escrita o dicha en voz alta"],
        ["contar datos privados de la familia", "preguntar a un compañero por su pueblo"],
        "Valora que responda con lo que sabe, imagina o siente; si cuenta un dato privado o pregunta a un compañero por su origen, recuérdale que no es necesario.",
    ),
    reinforce="Con un adulto, practica dos preguntas sobre el texto G que no pidan datos privados a nadie.",
    extend="Escribe una frase que empiece con «Yo siento…» para el texto H y otra que empiece con «Yo sé que…».",
)

# =================================================================== LR03 clase 5 · explicar significado en el texto
TXT_J = "Texto de práctica J (inventado): «Ayer, al llegar a la escuela, un abuelo invitado dijo «mari mari» a los niños. Los niños respondieron con una sonrisa y se sentaron para escuchar su charla.»"

L(
    LR3, 5,
    materials="Lápiz y hoja. Los textos y las fichas están escritos aquí; son inventados para practicar.",
    use="Aprenderé a explicar qué significa una expresión dentro de un texto usando la ficha y el contexto. Sirve para no quedarme con una traducción única, sino entender cuándo y cómo se usa.",
    prior=["Sé relacionar información interna de un texto.", "Sé que la fuente comunitaria explica el sentido de una expresión."],
    explain=[
        "El contexto es todo lo que rodea una palabra en el texto: las oraciones de al lado, quién habla y cuándo. El contexto cambia el significado. En castellano, «pie» es parte del cuerpo en «me duele el pie», pero es la base de un cerro en «al pie del cerro».",
        "Para explicar una expresión indígena hago cuatro pasos. Encuentro la expresión. Leo la ficha para saber qué significa. Leo la oración completa y las de al lado para saber cuándo se dijo. Escribo: «Según la ficha, … y en el texto se dijo cuando …».",
        "Una traducción de una sola palabra no cuenta todo. «Mari mari» es un saludo, y en castellano usamos «hola», pero el sentido completo de la expresión, cuándo y cómo se usa, lo explican el educador tradicional y la comunidad. Por eso mi explicación dice lo que sé y deja preguntas abiertas.",
    ],
    vocab=[("contexto", "todo lo que rodea una palabra en el texto"), ("explicar", "decir con claridad qué significa algo y por qué"), ("traducción", "palabra equivalente en otra lengua"), ("sentido", "lo que quiere decir algo en un lugar y momento"), ("significado", "lo que quiere decir una palabra")],
    worked=[
        W("Dos significados de una palabra", "Frases: 1) «Me duele el pie». 2) «Acampamos al pie del cerro». ¿En cuál «pie» es una parte del cuerpo?", ["Leo las palabras que rodean «pie».", "En 1 duele; en 2 hay un cerro.", "Dolerse se relaciona con el cuerpo."], "en la frase 1"),
        W("Explicar con ficha y contexto", TXT_J + " " + FICHA_SAL + " Explica «mari mari» en este texto.", ["Encuentro la expresión: «mari mari».", "La ficha dice que es un saludo.", "El texto dice que el abuelo la dijo al llegar a la escuela."], "Según la ficha, «mari mari» es un saludo; el abuelo lo dijo a los niños al llegar a la escuela"),
    ],
    mistakes=[
        M("Decir que «mari mari» significa solo «hola» y nada más.", "Una traducción no explica cuándo ni cómo se usa la expresión.", "Escribo lo que dice la ficha y dejo una pregunta para el educador tradicional."),
        M("Explicar una palabra sin leer la ficha.", "Puedo equivocarme porque no sé su significado.", "Leo la ficha y el contexto antes de explicar."),
    ],
    R=[
        ex(TXT_J + " ¿Cuándo dijo «mari mari» el abuelo invitado?", "al llegar a la escuela", "Lo dice la primera oración."),
        ex("En el texto J, ¿qué hicieron los niños al oír el saludo?", "respondieron con una sonrisa", "Está en la segunda oración."),
        ex("Una palabra del castellano, como «pie», ¿puede cambiar de significado según el texto? Sí o No.", "Sí", "El contexto decide qué significa."),
    ],
    C=[
        ex("En «Me duele el pie» y «Acampamos al pie del cerro», ¿en cuál frase «pie» es parte del cuerpo?", "en la primera", "«Me duele» se relaciona con el cuerpo."),
        ex("Para explicar una expresión del texto, ¿uso la ficha y el contexto o solo mi imaginación?", "la ficha y el contexto", "La ficha da el significado y el contexto da el momento."),
        ex("Completa: «Según la ficha, «mari mari» es ____. En el texto J se dijo al llegar a la escuela». Elige: un saludo o un número.", "un saludo", "La ficha dice que es un saludo."),
    ],
    A=[
        ex("Texto K (inventado): «La educadora escribió «ko» en la pizarra y mostró un vaso con agua. Dijo que esa palabra nombra lo que hay en el vaso.» " + FICHA_PAL + " ¿Qué nombra «ko» en el texto K?", "agua", "La ficha y el vaso con agua coinciden."),
        ex("Texto L (inventado): «Al terminar la clase, la visita dijo «chaltumay» y entregó una carta a cada niño.» " + FICHA_SAL + " ¿Qué explicación es completa? A) «Es una palabra rara». B) «Según la ficha es gracias; la visita lo dijo al terminar la clase».", "B", "La B usa la ficha y dice cuándo se dijo."),
        ex("Un profesor dice: «mari mari» significa solo «hola». Según esta clase, ¿qué falta decir? A) Que una traducción no cuenta todo y el educador o la comunidad explican más. B) Nada, está completo.", "A", "El sentido completo lo explica la comunidad."),
    ],
    Z=[
        ex("Compara. A) «Mari mari» es hola y punto. B) Según la ficha, «mari mari» es un saludo; en el texto J se usó al llegar; el educador explica más. ¿Cuál explica mejor?", "B", "La B usa ficha, contexto y reconoce a la fuente."),
        ex("Un niño explicó «kuyen» como un tipo de dulce sin mirar la ficha. ¿Qué paso omitió: leer la ficha o contar las letras?", "leer la ficha", "La ficha dice que kuyen es luna."),
    ],
    D=[
        ex("Ordena los pasos para explicar una expresión: A) escribo «Según la ficha…». B) encuentro la expresión. C) leo la ficha. D) leo la oración completa. Escribe las letras.", "B, C, D, A", "Encuentro, leo la ficha, leo el contexto y recién explico."),
        ex("En «Pedro se sentó en el banco de la plaza», ¿qué significa «banco»: un asiento o un lugar para guardar dinero?", "un asiento", "La plaza y sentarse son pistas del contexto."),
    ],
    context=[ex("Un cartel de tu escuela dice «Mari mari, visita». Un niño dice que significa «adiós». ¿Qué haces: revisar la ficha y el contexto o aceptar su idea?", "revisar la ficha y el contexto", "La ficha dice que es un saludo.")],
    selfcheck=[
        ex("¿Qué dos cosas uso para explicar una expresión de un texto?", "la ficha y el contexto", "Una da el significado y la otra el momento."),
        ex("¿Una traducción de una sola palabra explica todo el sentido de una expresión?", "No", "El sentido completo lo explica la comunidad."),
        ex("¿Quién puede explicar el sentido completo de una expresión indígena?", "el educador tradicional o la comunidad", "Ellos la cuidan y la usan."),
    ],
    task=T(
        "Lee este texto inventado para practicar: «Al comenzar la reunión, una visita dijo «mari mari» a todos. Al terminar, el curso respondió «chaltumay».» " + FICHA_SAL + " En tu cuaderno explica cada expresión con esta forma: «Según la ficha, … En el texto se dijo cuando …». Después escribe una pregunta que le harías a la educadora tradicional sobre el uso completo de una de las expresiones.",
        "Según la ficha, «mari mari» es un saludo. En el texto se dijo al comenzar la reunión. Según la ficha, «chaltumay» es gracias. En el texto se dijo al terminar. Pregunta: ¿cuándo se usa «mari mari» en su comunidad?",
        ["explica las dos expresiones con la ficha", "dice cuándo se dijo cada una en el texto", "no afirma significados que la ficha no trae", "formula una pregunta para el educador/a tradicional"],
        ["dos explicaciones escritas", "pregunta escrita o dicha en voz alta"],
        ["dar una traducción como si lo dijera todo", "inventar un uso especial"],
        "Observa que explica con ficha y contexto; si dio una traducción única como definitiva, muéstrale que el sentido completo lo explica la comunidad.",
    ),
    reinforce="Explica en voz alta, con las palabras «Según la ficha…», qué significa «ko» en el texto K.",
    extend="Busca en casa una palabra del castellano que cambie de significado según el contexto y escribe dos oraciones que lo muestren.",
)

# =================================================================== LR04 clase 1 · observar modelos y variantes
MOD = "Modelos para observar: «ko», «antü», «kuyen», «ruka», «mapu», «ñuke»."

L(
    LR4, 1,
    materials="Lápiz y hoja. Los modelos están escritos en este cuaderno.",
    use="Aprenderé a observar cómo están escritas las palabras de un modelo, con sus letras especiales, y a reconocer que una palabra puede tener variantes. Sirve para copiar con cuidado.",
    prior=["Sé que cada palabra tiene letras en cierto orden.", "Sé que debo nombrar la fuente."],
    explain=[
        "Un modelo es una palabra escrita correctamente que me sirve para copiar. Antes de escribir observo el modelo: cuántas letras tiene, con qué letra empieza y si trae letras especiales, como la ñ en «ñuke» o la ü en «antü». Esas letras no se pueden saltar.",
        "Muchas lenguas indígenas se escribieron por mucho tiempo sin una forma única. Por eso una palabra puede tener variantes: otras formas de escribir la misma palabra. La casa mapuche aparece como «ruka» o «ruca»; la araucaria, como «pewen» o «pehuén». Cuál se usa en cada lugar lo explica la comunidad.",
        "No decido cuál variante es la «buena». Anoto el modelo que me entrega la fuente y, si veo otra forma, la anoto con el lugar donde la vi. Cuál usar en un cartel lo decide el educador o la educadora tradicional con la comunidad.",
    ],
    vocab=[("modelo", "palabra bien escrita que sirve para copiar"), ("variante", "otra forma de escribir la misma palabra"), ("letra especial", "letra como ñ o ü que no puedo omitir"), ("observar", "mirar con atención para notar detalles"), ("copiar", "escribir igual a un modelo")],
    worked=[
        W("Contar y observar", MOD + " ¿Cuántas letras tiene «kuyen» y qué letra tiene en el centro?", ["Separo las letras: k, u, y, e, n.", "Son cinco letras.", "La del centro es la tercera: y."], "5 letras; en el centro está la y"),
        W("Comparar variantes", "Dos fuentes escriben «ruka» y «ruca» para la casa mapuche. ¿En qué se diferencian?", ["Comparo letra por letra: r, u, k/c, a.", "La tercera letra cambia: k en una y c en otra.", "Las demás letras son iguales."], "en la tercera letra"),
    ],
    mistakes=[
        M("Omitir la ñ o la ü porque cuesta escribirlas.", "Cambia la palabra y deja de coincidir con el modelo.", "Las copio con cuidado y reviso que estén."),
        M("Decir que una variante es un error.", "Puede ser otra forma de escribir usada en otra fuente.", "Anoto las dos y pregunto al educador qué usa su comunidad."),
    ],
    R=[
        ex(MOD + " ¿Qué palabra tiene la letra ñ?", "ñuke", "Es la única que la lleva."),
        ex(MOD + " ¿Qué palabra tiene la letra ü?", "antü", "Es la única con ü."),
        ex(MOD + " ¿Cuál es la palabra más corta?", "ko", "Tiene solo dos letras."),
    ],
    C=[
        ex("¿Cuántas letras tiene «kuyen»?", "5", "Se cuentan k, u, y, e, n."),
        ex(MOD + " ¿Cuál tiene más letras: «kuyen» o «ruka»?", "kuyen", "Tiene 5 letras y «ruka» tiene 4."),
        ex(MOD + " ¿Cuántas de las seis palabras tienen exactamente 4 letras?", "4", "antü, ruka, mapu y ñuke tienen 4 letras."),
    ],
    A=[
        ex("Dos fuentes escriben «ruka» y «ruca». ¿En qué número de letra se diferencian: 1, 2, 3 o 4?", "3", "La k y la c están en tercer lugar."),
        ex("Dos fuentes escriben «pewen» y «pehuén». ¿Qué letra de «pehuén» lleva tilde?", "la é", "La tilde está sobre la e que está antes de la n final."),
        ex("Un compañero copió «antu» desde el modelo «antü». ¿Qué letra del modelo no copió igual?", "la ü", "Escribió u en lugar de ü."),
    ],
    Z=[
        ex("Dos libros escriben «mapuzugun» y «mapudungun». ¿Quién ayuda a saber qué forma usa la comunidad: el educador tradicional o un compañero que adivina?", "el educador tradicional", "Es quien enseña la lengua."),
        ex("Copio «ñuke» y escribo «nuke». ¿Coincide con el modelo? Sí o No.", "No", "Falta la ñ."),
    ],
    D=[
        ex("Copiaste la palabra «ñuke». ¿Cuál copia coincide con el modelo? A) nuke. B) ñuke. C) ñuka.", "B", "Solo B tiene la ñ y termina en e."),
        ex("Ordena de menos a más letras: «kuyen», «ko», «ruka». Escribe las tres palabras en orden.", "ko, ruka, kuyen", "Tienen 2, 4 y 5 letras."),
    ],
    context=[ex("Tu escuela imprime un cartel con «antü», pero la impresora quitó los puntos de la ü y sale «antu». ¿Qué haces: aceptarlo así o avisar para corregirlo según el modelo?", "avisar para corregirlo según el modelo", "El cartel debe coincidir con el modelo.")],
    selfcheck=[
        ex("¿Cómo se llama otra forma de escribir la misma palabra?", "variante", "Variante es otra forma válida de escribir."),
        ex("¿Con qué comparo mi copia para saber si está bien?", "con el modelo", "El modelo es la palabra bien escrita."),
        ex("Al copiar «ñuke» o «antü», ¿puedo saltarme la ñ o la ü?", "No", "Son letras que forman parte de la palabra."),
    ],
    task=T(
        "Observa estos modelos: «ko», «antü», «kuyen», «ruka», «mapu», «ñuke». Copia en tu cuaderno cada palabra y debajo escribe: cuántas letras tiene y si tiene una letra especial. Luego observa que «ruka» también aparece escrita «ruca» y «pewen» aparece escrita «pehuén»; anota cada pareja con una línea que diga «Fuente: por preguntar». Termina con una pregunta para la educadora tradicional sobre qué forma usa su comunidad.",
        "ko: 2 letras, sin letra especial. antü: 4 letras, tiene ü. ñuke: 4 letras, tiene ñ. ruka / ruca. Fuente: por preguntar. Pregunta: ¿qué forma de «pewen» usan en su comunidad?",
        ["copia las seis palabras con sus letras especiales", "cuenta bien las letras", "anota las dos variantes sin decir que una está mal", "formula una pregunta para el educador/a tradicional"],
        ["lista de seis palabras con su conteo", "pregunta escrita o dicha en voz alta"],
        ["omitir la ñ o la ü", "decir que una variante está equivocada"],
        "Comprueba que copió con letras especiales y que no juzgó las variantes; si borró una, invítalo a anotar ambas y preguntar.",
    ),
    reinforce="Cubre el modelo «antü», escríbelo de memoria y luego compáralo letra por letra.",
    extend="Elige dos modelos y escribe una oración en castellano que explique cuántas letras tienen y cuál tiene una letra especial.",
)

# =================================================================== LR04 clase 2 · escribir para nombrar
L(
    LR4, 2,
    materials="Lápiz, hojas y colores. Los modelos y las fichas están escritos en este cuaderno.",
    use="Aprenderé a escribir palabras para nombrar cosas, como en las etiquetas de un cartel. Sirve para presentar palabras de una lengua indígena copiándolas con cuidado y con su fuente.",
    prior=["Sé observar un modelo y contar sus letras.", "Sé que ñ y ü no se pueden omitir."],
    explain=[
        "Nombrar es decir cómo se llama algo. Una etiqueta es un papelito con una palabra que nombra un objeto, un lugar o un dibujo. Para hacer una etiqueta con una palabra de una lengua indígena, copio el modelo con todas sus letras y no cambio nada.",
        "Mi etiqueta tiene tres partes: la palabra en lengua indígena entre comillas, el nombre en castellano debajo y la fuente. Por ejemplo: «ko», agua, y debajo «Fuente: ficha de la clase». Así quien lea sabe de dónde viene la palabra.",
        "Solo nombro con las palabras que tengo en la ficha. Si necesito nombrar algo que la ficha no trae, no invento una palabra: dejo la etiqueta en blanco y pregunto al educador o a la educadora tradicional. Así cuido la lengua y la verdad.",
    ],
    vocab=[("nombrar", "decir cómo se llama algo"), ("etiqueta", "papelito con una palabra que nombra algo"), ("ficha", "papel con palabras y sus significados"), ("fuente", "quien sabe la palabra y la comparte"), ("copiar", "escribir igual a un modelo")],
    worked=[
        W("Hacer una etiqueta", FICHA_PAL + " Dibujo: un vaso con agua. ¿Cómo hago su etiqueta?", ["Busco agua en la ficha: «ko».", "Copio «ko» con sus letras.", "Debajo escribo agua y la fuente: ficha de la clase."], "«ko» / agua / Fuente: ficha de la clase"),
        W("Algo que la ficha no trae", FICHA_PAL + " Dibujo: un lago. La ficha no trae esa palabra. ¿Qué hago?", ["Reviso la ficha y no la encuentro.", "No invento una palabra.", "Dejo la etiqueta en blanco y pregunto al educador tradicional."], "dejo la etiqueta en blanco y pregunto al educador"),
    ],
    mistakes=[
        M("Etiquetar un dibujo con una palabra que suena parecida pero no está en la ficha.", "Puedo estar inventando una palabra.", "Uso solo las palabras de la ficha y pregunto por las demás."),
        M("Cambiar una letra al copiar el modelo.", "La etiqueta ya no coincide con la palabra.", "Reviso mi copia letra por letra."),
    ],
    R=[
        ex(FICHA_PAL + " Dibujo: un sol. ¿Qué palabra de la ficha escribes en la etiqueta?", "antü", "La ficha dice que antü es sol."),
        ex("Dibujo de una casa mapuche. Con la ficha, ¿qué palabra copias: «ruka» o «mapu»?", "ruka", "Según la ficha «ruka» es la casa mapuche."),
        ex("Dibujo de la luna. ¿Qué palabra de la ficha usas?", "kuyen", "Según la ficha, «kuyen» es luna."),
    ],
    C=[
        ex("Copia exactamente desde el modelo la palabra que nombra la tierra y escríbela aquí.", "mapu", "La ficha dice que mapu es tierra."),
        ex("¿Cuántas letras tiene la palabra que nombra al sol?", "4", "Antü tiene a, n, t, ü."),
        ex("Ana puso «mapu» debajo del dibujo de la tierra. ¿Está bien según la ficha? Sí o No.", "Sí", "La ficha dice que «mapu» es tierra."),
    ],
    A=[
        ex("Tres dibujos en fila: 1) luna, 2) casa mapuche, 3) agua. Escribe las tres palabras en orden con ayuda de la ficha.", "kuyen, ruka, ko", "Luna es kuyen, la casa mapuche es ruka y agua es ko."),
        ex("Un cartel dice «ñuke» bajo el dibujo de una madre con su hijo. ¿A quién nombra según la ficha?", "a la madre", "La ficha dice que ñuke es madre."),
        ex("Quieres nombrar el sol y la luna juntos. ¿Cuántas etiquetas necesitas y qué palabras llevan?", "2: antü y kuyen", "Cada cosa lleva su propia etiqueta."),
    ],
    Z=[
        ex("Un niño etiquetó el dibujo de un sol con «kuyen». ¿Cuál es el error?", "usó la palabra de la luna", "Kuyen es luna y el sol es antü."),
        ex("Tienes el dibujo de un lago y la ficha no trae esa palabra. ¿Qué haces: invento una o pregunto al educador tradicional?", "pregunto al educador tradicional", "Solo quien sabe la lengua puede decir la palabra."),
    ],
    D=[
        ex("Ordena los pasos para hacer una etiqueta: A) escribo el nombre en castellano y la fuente. B) copio la palabra del modelo. C) busco la palabra en la ficha. Escribe las letras en orden.", "C, B, A", "Primero busco en la ficha, luego copio y al final agrego el nombre y la fuente."),
        ex("¿Qué etiqueta está mejor hecha? A) «mapu» y debajo «Fuente: ficha de la clase». B) «mapu» sin nada más.", "A", "La A dice de dónde viene la palabra."),
    ],
    context=[ex("Vas a pegar etiquetas en tres objetos de práctica dibujados: un vaso con agua, una ventana con sol y una casa mapuche dibujada en papel. ¿Qué palabras pegas, en ese orden?", "ko, antü, ruka", "Agua es ko, sol es antü y la casa mapuche es ruka.")],
    selfcheck=[
        ex("Cuando hago una etiqueta, ¿copio la palabra del modelo o la invento?", "la copio del modelo", "Solo se usan palabras de la ficha."),
        ex("¿Qué letras no debo olvidar al copiar «ñuke» y «antü»?", "la ñ y la ü", "Son letras especiales de esas palabras."),
        ex("Si la ficha no trae la palabra de algo, ¿a quién le pregunto?", "al educador tradicional", "Es quien enseña la lengua."),
    ],
    task=T(
        "Haz tres etiquetas de práctica con la ficha de palabras: " + FICHA_PAL + " Dibuja tres cosas: un vaso con agua, un sol y una casa mapuche. Debajo de cada dibujo escribe la palabra copiada entre comillas, su nombre en castellano y «Fuente: ficha de la clase». Dibuja una cuarta cosa que no esté en la ficha, por ejemplo un lago, y deja su etiqueta en blanco con la frase «por preguntar». Escribe una pregunta para la educadora tradicional.",
        "«ko» / agua / Fuente: ficha de la clase. «antü» / sol / Fuente: ficha de la clase. «ruka» / casa mapuche / Fuente: ficha de la clase. Lago: por preguntar. Pregunta: ¿cómo se nombra un lago en su comunidad?",
        ["copia las tres palabras sin errores", "escribe el nombre en castellano y la fuente", "deja en blanco la etiqueta que no tiene palabra", "formula una pregunta para el educador/a tradicional"],
        ["cuatro dibujos con etiqueta", "pregunta escrita o dicha en voz alta"],
        ["inventar una palabra para el lago", "cambiar una letra al copiar"],
        "Revisa letra por letra contra la ficha; si inventó una palabra, pídele que la cambie por «por preguntar».",
    ),
    reinforce="Escribe «antü» tres veces mirando el modelo y marca con un círculo la ü cada vez.",
    extend="Haz una etiqueta de práctica con «ñuke» para el dibujo de una madre y agrega la fuente.",
)

# =================================================================== LR04 clase 3 · construir una frase simple
L(
    LR4, 3,
    materials="Lápiz y hoja. Los modelos y las frases están escritos en este cuaderno.",
    use="Aprenderé a escribir una frase simple en castellano que lleve una palabra indígena entre paréntesis y diga cómo es lo que nombra. Sirve para caracterizar con claridad y cuidar la palabra.",
    prior=["Sé hacer etiquetas con una palabra de la ficha.", "Sé que una frase empieza con mayúscula y termina con punto."],
    explain=[
        "Caracterizar es decir cómo es algo. Para eso uso una cualidad, que es una palabra como «grande», «fría» o «brillante». Una frase simple tiene tres partes: lo que nombro, el verbo «es» y la cualidad. Empieza con mayúscula y termina con punto.",
        "En esta clase mis frases están en castellano y llevan la palabra indígena entre paréntesis y comillas, así: La casa mapuche («ruka») es grande. De ese modo la palabra queda claramente marcada y no la mezclo con la gramática del castellano.",
        "Las frases completas en una lengua indígena tienen sus propias reglas, que enseñan el educador o la educadora tradicional. Yo no las invento: si quiero escribir una frase entera en esa lengua, la escribo con su ayuda y su revisión.",
    ],
    vocab=[("caracterizar", "decir cómo es algo"), ("cualidad", "palabra que dice cómo es algo, como grande"), ("frase simple", "oración corta con lo que nombro, es y su cualidad"), ("mayúscula", "letra grande con que empieza una frase"), ("punto", "signo con que termina una frase")],
    worked=[
        W("Ordenar una frase", "Ordena las palabras: es / La / grande / casa / mapuche. Agrega la palabra («ruka») después de mapuche.", ["Empiezo con mayúscula: La.", "Sigo con casa mapuche y la palabra: casa mapuche («ruka»).", "Termino con es grande y un punto."], "La casa mapuche («ruka») es grande."),
        W("Elegir la cualidad", "Completa: El sol («antü») es ____. Opciones: cálido o ruidoso.", ["Pienso cómo se siente el sol.", "El sol da calor.", "Elijo cálido."], "El sol («antü») es cálido."),
    ],
    mistakes=[
        M("Escribir la frase sin verbo, por ejemplo «La casa grande».", "Falta «es» y la frase no dice cómo es la casa.", "Agrego el verbo: La casa es grande."),
        M("Inventar cómo se dice la frase completa en lengua indígena.", "No conozco las reglas de esa lengua.", "La escribo con el educador tradicional."),
    ],
    R=[
        ex("Ordena las palabras para formar una frase: es / La / grande / casa.", "La casa es grande.", "Empieza con mayúscula y termina con punto."),
        ex("¿Con qué empieza y con qué termina una frase simple?", "con mayúscula y con punto", "Así se escribe una frase en castellano."),
        ex("En «El agua («ko») es fría.», ¿qué palabra dice cómo es el agua?", "fría", "La cualidad va después de «es»."),
    ],
    C=[
        ex("Completa con una cualidad: La luna («kuyen») es ____. Opciones: brillante o ruidosa.", "brillante", "La luna se ve brillante y no hace ruido."),
        ex("¿Cuál es una frase simple completa? A) La casa mapuche («ruka»). B) La casa mapuche («ruka») es pequeña.", "B", "La B tiene verbo y cualidad."),
        ex("En «El sol («antü») es cálido.», ¿qué palabra va entre paréntesis y comillas?", "antü", "Es la palabra indígena marcada."),
    ],
    A=[
        ex("Ordena para formar una frase: húmeda / es / La tierra («mapu»).", "La tierra («mapu») es húmeda.", "Primero va el nombre, luego es y la cualidad, con punto al final."),
        ex("Elige la frase bien escrita. A) la casa mapuche («ruka») es grande B) La casa mapuche («ruka») es grande.", "B", "La B empieza con mayúscula y termina con punto."),
        ex("Ordena para formar una frase: («ko») / fría / es / El agua.", "El agua («ko») es fría.", "Primero va el nombre, luego es y la cualidad."),
    ],
    Z=[
        ex("Pedro escribió «La casa mapuche («ruka») grande». ¿Qué palabra le falta para decir cómo es la casa en una oración completa?", "es", "Falta el verbo es."),
        ex("Una frase simple sobre «kuyen» puede decir cómo es la luna. ¿Puede decir también qué significa «kuyen» sin mirar la ficha? Sí o No.", "No", "El significado lo da la ficha."),
    ],
    D=[
        ex("Corrige esta frase, que tiene dos errores: la luna («kuyen») brillante", "La luna («kuyen») es brillante.", "Faltaban la mayúscula inicial, el verbo es y el punto final."),
        ex("Una frase tiene La, tierra, («mapu»), es, húmeda. Si agregas «muy» antes de húmeda, ¿cuántas palabras en castellano tiene?", "5", "La, tierra, es, muy y húmeda."),
    ],
    context=[ex("Para un cartel de práctica escribes: La casa mapuche («ruka») del cuento es ____. Opciones: acogedora o veloz. ¿Cuál elijes?", "acogedora", "Una casa puede ser acogedora, pero no veloz.")],
    selfcheck=[
        ex("¿Con qué letra empieza una frase?", "con mayúscula", "Toda frase comienza con mayúscula."),
        ex("¿Con qué signo termina una frase simple?", "con punto", "El punto marca el final."),
        ex("¿Quién me enseña a escribir frases completas en una lengua indígena?", "el educador tradicional", "Esas reglas las conoce quien enseña la lengua."),
    ],
    task=T(
        "Escribe tres frases simples de práctica con las palabras de la ficha: " + FICHA_PAL + " Usa este modelo: «La casa mapuche («ruka») es grande.» Cada frase debe tener una palabra de la ficha entre paréntesis y comillas, el verbo «es» y una cualidad que elijas de esta lista: grande, pequeña, cálido, fría, brillante, tranquila, húmeda. Cuida la mayúscula y el punto. Termina con una pregunta para la educadora tradicional.",
        "El sol («antü») es cálido. La luna («kuyen») es brillante. El agua («ko») es fría. Pregunta: ¿cómo se dice una frase entera en su comunidad?",
        ["usa tres palabras de la ficha entre paréntesis y comillas", "cada frase tiene verbo y cualidad", "cuida la mayúscula y el punto", "formula una pregunta para el educador/a tradicional"],
        ["tres frases escritas", "pregunta escrita o dicha en voz alta"],
        ["escribir sin verbo", "inventar una frase en lengua indígena"],
        "Comprueba que usó solo palabras de la ficha; si inventó una frase en lengua indígena, remítelo al educador tradicional.",
    ),
    reinforce="Lee en voz alta «La casa mapuche («ruka») es grande.» y señala la mayúscula, el verbo y el punto.",
    extend="Escribe una frase más con la palabra «mapu» y una cualidad de la lista.",
)

# =================================================================== LR04 clase 4 · revisar con una fuente válida
L(
    LR4, 4,
    materials="Lápiz y hoja. Los modelos y las revisiones están escritos en este cuaderno.",
    use="Aprenderé a revisar mis palabras y frases comparándolas con una fuente válida. Sirve para corregir errores sin inventar lengua y para decir de dónde viene lo que escribí.",
    prior=["Sé copiar un modelo con sus letras especiales.", "Sé escribir una frase simple con una palabra indígena entre paréntesis."],
    explain=[
        "Revisar es leer de nuevo lo que escribí y compararlo con un modelo. Una fuente válida es una ficha o una persona que conoce la lengua y dice de dónde viene lo que sabe, como una ficha de la clase o la educadora tradicional. Mi memoria sin comprobar no es una fuente válida.",
        "Reviso con una lista de seis puntos. Uno: las letras coinciden con el modelo. Dos: están la ñ y la ü si las lleva. Tres: la palabra va entre comillas. Cuatro: la frase empieza con mayúscula. Cinco: termina con punto. Seis: anoté la fuente.",
        "Si encuentro una diferencia con el modelo, la corrijo. Pero si dos fuentes válidas escriben distinto, no tacho una: anoto ambas y pregunto a la educadora cuál usa su comunidad. Corregir una copia no es lo mismo que decidir cuál variante es mejor.",
    ],
    vocab=[("revisar", "leer de nuevo y comparar con un modelo"), ("fuente válida", "ficha o persona que conoce la lengua y dice de dónde viene su saber"), ("corregir", "cambiar un error por lo correcto"), ("coincidir", "ser igual a otra cosa"), ("lista de revisión", "puntos que compruebo uno por uno")],
    worked=[
        W("Comparar una copia", "Modelo: «kuyen». Mi copia: «kuyem». ¿Coincide? ¿Qué cambió?", ["Comparo letra por letra.", "Las primeras cuatro letras son iguales.", "La última es m en mi copia y n en el modelo."], "no coincide; la n cambió por m"),
        W("Revisar una frase", "Mi frase: la luna («kuyen») es redonda. ¿Qué dos cosas debo corregir?", ["Miro el inicio: empieza con minúscula.", "Miro el final: no tiene punto.", "Corrijo: La luna («kuyen») es redonda."], "poner mayúscula al inicio y punto al final"),
    ],
    mistakes=[
        M("Creer que mi memoria basta para revisar.", "Puedo recordar mal una letra.", "Comparo con el modelo o con la ficha."),
        M("Tachar una variante porque no coincide con mi modelo.", "Otra fuente válida puede escribirla distinto.", "Anoto ambas y pregunto qué usa la comunidad."),
    ],
    R=[
        ex("¿Cuál es una fuente válida: la ficha de la educadora o mi memoria sin comprobar?", "la ficha de la educadora", "La ficha dice de dónde viene el saber."),
        ex("El modelo dice «kuyen» y mi copia dice «kuyem». ¿Coincide? Sí o No.", "No", "La última letra es distinta."),
        ex("En esa copia, ¿qué letra cambió: la primera o la última?", "la última", "La n del modelo pasó a m."),
    ],
    C=[
        ex("Modelos: «ruka», «mapu», «ñuke». Copias: 1) ruka, 2) mapo, 3) nuke. ¿Qué copias están bien?", "solo la 1", "La 2 cambia la u por o y la 3 omite la ñ."),
        ex("Frase: la luna («kuyen») es redonda. ¿Qué dos cosas le faltan?", "la mayúscula inicial y el punto final", "Una frase se escribe con ambas."),
        ex("Verdadero o falso: si creo que una palabra está bien, ya no necesito revisarla.", "Falso", "Debo comprobarla con un modelo."),
    ],
    A=[
        ex("Revisas tres etiquetas: «ko» (agua), «antu» (sol), «kuyen» (luna). ¿Cuál debes corregir y cómo debe quedar?", "«antu»; debe ser «antü»", "Falta la ü del modelo."),
        ex("Tienes dos copias de «mapu»: «mapu» y «mapo». ¿Cuántas coinciden con el modelo?", "1", "Solo «mapu» coincide."),
        ex("Revisas una etiqueta: la palabra «ñuke» está bien copiada y entre comillas, pero no anotaste de dónde la sacaste. ¿Qué punto de la lista no cumples?", "el sexto: anotar la fuente", "Falta la fuente."),
    ],
    Z=[
        ex("Un libro escribe «ruca» y la ficha de la clase escribe «ruka». ¿A quién preguntas qué forma usar en el cartel del curso?", "al educador tradicional", "Es quien conoce lo que usa la comunidad."),
        ex("Valentina revisó su trabajo con un sitio sin autor y sin procedencia. ¿Es una fuente válida? Sí o No.", "No", "No dice quién lo sabe ni de dónde viene."),
    ],
    D=[
        ex("Ordena los pasos: A) comparo con el modelo letra por letra. B) corrijo y anoto la fuente. C) copio la palabra. Escribe las letras.", "C, A, B", "Primero copio, luego comparo y al final corrijo y anoto."),
        ex("Compañero: «La casa mapuche (ruka) es grande.» con fuente anotada. Con la lista de seis puntos, ¿cuál no cumple?", "el tercero: la palabra va entre comillas", "La palabra «ruka» está solo entre paréntesis."),
    ],
    context=[ex("El cartel del curso dice: La casa mapuche (ruka) es grande. La ficha escribe la palabra así: «ruka». ¿Qué corrección haces?", "poner la palabra entre comillas: La casa mapuche («ruka») es grande.", "En esta clase la palabra indígena va entre paréntesis y comillas.")],
    selfcheck=[
        ex("¿Con qué comparo mi copia para revisarla?", "con un modelo o una ficha", "Son fuentes para comprobar."),
        ex("Si dos fuentes escriben distinto una palabra, ¿tacho una o anoto las dos?", "anoto las dos", "Puede haber variantes válidas."),
        ex("¿Qué letras especiales debo revisar en «antü» y «ñuke»?", "la ü y la ñ", "Son parte de las palabras."),
    ],
    task=T(
        "Revisa este trabajo de práctica con la ficha: " + FICHA_PAL + " Trabajo: 1) etiqueta «antu» bajo un sol. 2) frase: el agua («ko») es fría. 3) etiqueta «nuke» bajo una madre. En tu cuaderno copia cada línea corregida y escribe al lado qué cambiaste (letra, mayúscula o punto). Agrega la línea «Fuente: ficha de la clase». Termina con una pregunta para el educador tradicional sobre una variante.",
        "1) «antü» (agregué la ü). 2) El agua («ko») es fría. (mayúscula y punto). 3) «ñuke» (agregué la ñ). Fuente: ficha de la clase. Pregunta: ¿qué forma de «pewen» usa su comunidad?",
        ["corrige las tres líneas", "explica qué cambió en cada una", "anota la fuente", "formula una pregunta para el educador/a tradicional"],
        ["tres líneas corregidas con su explicación", "pregunta escrita o dicha en voz alta"],
        ["no revisar las letras especiales", "tachar una variante sin preguntar"],
        "Verifica que cada corrección salga de la ficha; si cambió algo por intuición, pídele que lo compare con el modelo.",
    ),
    reinforce="Escribe «ñuke» de memoria, compara con el modelo y corrige si hace falta.",
    extend="Haz tu propia lista de revisión de seis puntos para tus etiquetas y úsala con un compañero.",
)
