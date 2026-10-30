"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR03 (comprensión de textos breves con palabras o expresiones en lengua indígena o en castellano
culturalmente significativas, con opiniones fundamentadas sobre su contenido cultural), contexto de rescate y
revitalización.

Criterio de autoría: todas las invitaciones, notas, cuentos y carteles son inventados, están escritos en castellano
y se declaran como tales; no son textos de ningún pueblo. Las únicas expresiones en lengua indígena son las ya
atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke en mapuzugun; iorana, maururu en rapa nui),
siempre con su ficha y con su grafía exacta. Las expresiones en castellano culturalmente significativas que se
usan (territorio, comunidad, educador tradicional) se definen en la propia clase y se presentan como vocabulario
general, sin atribuir a ningún pueblo un significado especial. No se escribe pronunciación ni gramática, y no se
exige a nadie contar vivencias personales: todas las respuestas se apoyan en el texto. El significado profundo y el
uso de las expresiones los enseñan el educador/a tradicional y la comunidad; cada tarea abierta lo remite a ellos.
"""
from __future__ import annotations

from student_content_lc4_b import FICHA_PAL, L, M, T, W
from student_lessons import arith, ex

LR3 = "LC04 OA LR03"

INVITA = "Invitación de práctica (inventada). De: el 4.º A de una escuela de práctica. Para: las familias del curso. Texto: «Los invitamos a conocer nuestra huerta. Habrá una muestra de palabras: antü, ko y mapu. Será el viernes a las 10. Chaltumay por venir.»"
NOTA = "Nota de práctica (inventada): «Hoy en la huerta usamos mapu para sembrar y ko para regar. El antü nos dio calor. Al terminar dijimos: chaltumay.»"
SEMILLAS = "Nota de práctica (inventada): «Sembramos 8 semillas en la mapu. Regamos con ko cada día. A la semana, 6 semillas brotaron.»"
CUENTO = "Cuento de práctica (inventado): «Mía llevó ko desde el río hasta la ruka. En la puerta la esperaba su ñuke. Mía sintió alegría y dijo: chaltumay. Luego ambas regaron las plantas.»"
KUYEN = "Texto de práctica (inventado): «Esa noche el kuyen iluminó el patio. Los niños miraron el cielo y guardaron silencio.»"

L(
    LR3, 1,
    materials="Lápiz y hoja. Los textos están escritos en este cuaderno y son inventados. " + FICHA_PAL,
    use="Aprenderé a reconocer quién escribió un texto y para qué lo escribió. Sirve para leer con atención y entender lo que el texto quiere lograr.",
    prior=["Sé que un texto tiene título, fuente y dibujos.", "Sé usar la ficha de palabras."],
    explain=[
        "Todo texto nace de alguien que lo escribe, para alguien más y con un propósito. La fuente es quién lo escribió y dónde. El propósito es para qué lo escribió. Algunos textos informan, es decir, dan datos. Otros invitan a hacer algo. Otros agradecen. Para descubrir el propósito pregunto: ¿qué quiere que sepa, haga o sienta quien lee?",
        "Las pistas están en el texto. La palabra «invitamos» muestra que invita. Datos como el día y la hora informan. Una palabra como «chaltumay» agradece. En un mismo texto puede haber más de un propósito, pero casi siempre hay uno principal.",
        "Cuando un texto trae palabras de una lengua indígena, la fuente me ayuda a saber quién las puso. En un texto real de una comunidad, pregunto al educador tradicional de dónde viene el texto y si lo puedo usar. Hoy leo una invitación inventada.",
    ],
    vocab=[("fuente", "quién escribió el texto y de dónde viene"), ("propósito", "para qué se escribió un texto"), ("informar", "dar datos"), ("invitar", "pedir que alguien venga o participe"), ("agradecer", "decir gracias")],
    worked=[
        W("Reconocer la fuente", INVITA + " ¿Quién escribe la invitación?", ["Busco el dato «De».", "Dice «el 4.º A de una escuela de práctica»."], "El 4.º A de una escuela de práctica"),
        W("Reconocer el propósito", INVITA + " ¿Cuál es el propósito principal?", ["La palabra «invitamos» pide que vengan.", "Hay día y hora."], "Invitar a conocer la huerta"),
    ],
    mistakes=[
        M("Leer el texto sin preguntar quién lo escribió.", "No sé de dónde viene lo que dice.", "Busco la fuente primero."),
        M("Pensar que todos los textos solo informan.", "Algunos invitan o agradecen.", "Busco pistas del propósito."),
    ],
    R=[
        ex("El propósito de un texto es: A) para qué se escribió B) cuántas hojas tiene.", "A", "Propósito es el motivo."),
        ex(INVITA + " ¿Para quiénes es la invitación?", "las familias del curso", "El dato «Para» lo dice."),
        ex("Una invitación sirve para: A) pedir que alguien venga B) despedirse.", "A", "Invitar es convocar."),
    ],
    C=[
        ex(INVITA + " ¿Qué día será?", "el viernes", "El texto dice «el viernes»."),
        ex("Verdadero o falso: un texto solo puede tener un propósito.", "Falso", "Puede tener varios, aunque uno sea el principal."),
        ex(INVITA + " ¿Qué palabra de la ficha agradece al final?", "Chaltumay", "La ficha dice que chaltumay es gracias."),
    ],
    A=[
        ex("Texto: «Gracias por ayudarnos a regar la huerta». ¿Cuál es su propósito principal: agradecer o invitar?", "agradecer", "Las palabras «Gracias por ayudarnos» muestran que agradece."),
        ex(INVITA + " ¿A qué hora será la muestra?", "a las 10", "El texto dice «a las 10»."),
        arith("La invitación se envió a 12 familias y llegaron 9. ¿Cuántas no llegaron?", "12 - 9", "Resto las que llegaron."),
    ],
    Z=[
        ex("Un aviso dice: «Hoy no hay clases». Otro dice: «Los invitamos al acto». ¿Cuál es una invitación?", "el segundo", "Pide que asistan."),
        ex("Una persona dice que la invitación fue escrita por una comunidad indígena. ¿Qué dato contradice su error: A) la fuente dice que la escribió un curso de una escuela de práctica B) la hora de la muestra?", "A", "La fuente no menciona ninguna comunidad indígena."),
    ],
    D=[
        arith("La muestra empieza a las 10 y dura 2 horas. ¿A qué hora termina?", "10 + 2", "Sumo la duración a la hora de inicio."),
        ex("Quieres usar un texto real de una comunidad y no sabes quién lo escribió. ¿Qué haces: A) pregunto al educador tradicional de dónde viene B) lo uso igual?", "A", "Debo conocer la fuente y el permiso."),
    ],
    context=[ex("Encuentras un papel que dice: «Los invitamos al acto del curso». ¿Qué propósito tiene: «invitar» o «despedirse»?", "«invitar»", "La palabra «invitamos» lo indica.")],
    selfcheck=[
        ex("¿Qué dato dice quién escribió un texto?", "la fuente", "Fuente es el origen."),
        ex("¿Qué es el propósito?", "para qué se escribió", "Es el motivo del texto."),
        ex("¿Qué palabra de la ficha agradece?", "chaltumay", "Significa gracias en mapuzugun."),
    ],
    task=T(
        "Lee esta invitación inventada: " + INVITA + " Escribe quién la escribe, para quién es, su propósito principal y una pista del texto que lo muestra. Luego escribe una pregunta que le harías al educador tradicional sobre cómo se invita a una comunidad.",
        "Escribe: el 4.º A. Es para: las familias. Propósito: invitar. Pista: «Los invitamos». Pregunta: ¿cómo se invita a la comunidad?",
        ["identifica fuente y destinatario", "dice el propósito con una pista", "pregunta para quien enseña"],
        ["respuestas escritas en el cuaderno"],
        ["no dar una pista del texto", "atribuir el texto a una comunidad"],
        "Valora que justificó el propósito con una pista; si atribuyó el texto a una comunidad, pídele que relea la fuente.",
    ),
    reinforce="Elige un aviso de tu sala y di quién lo escribió y para qué.",
    extend="Pide a una persona de tu casa un papel con texto (una nota) y reconoce con ella la fuente y el propósito.",
)

L(
    LR3, 2,
    materials="Lápiz y hoja. La nota y las definiciones están escritas aquí. " + FICHA_PAL,
    use="Aprenderé a localizar expresiones significativas en un texto, en lengua indígena o en castellano, y a leer su significado en la ficha. Sirve para no perder palabras importantes al leer.",
    prior=["Sé la fuente y el propósito de un texto.", "Sé leer la ficha de palabras."],
    explain=[
        "Una expresión significativa es una palabra o frase que lleva un valor especial para una cultura. Puede estar en una lengua indígena, como «ko» o «chaltumay», o en castellano, como «territorio», «comunidad» o «educador tradicional». El territorio es el lugar donde vive y trabaja una comunidad. La comunidad es un grupo que comparte un lugar y una cultura. El educador tradicional es una persona de la comunidad que enseña saberes de su pueblo.",
        "Para localizar expresiones leo el texto dos veces. La primera, completo. La segunda, subrayo las palabras de la ficha y las expresiones en castellano que son significativas. Luego anoto su significado y verifico que el texto las use de esa manera.",
        "No cambio ni invento significados. Si una expresión no está en la ficha, la marco con un signo de pregunta y consulto al educador tradicional. Y no asumo que una expresión significa lo mismo para todos los pueblos.",
    ],
    vocab=[("expresión significativa", "palabra o frase que tiene un valor especial para una cultura"), ("territorio", "lugar donde vive y trabaja una comunidad"), ("comunidad", "grupo que comparte un lugar y una cultura"), ("educador tradicional", "persona de la comunidad que enseña saberes de su pueblo"), ("subrayar", "marcar con una línea")],
    worked=[
        W("Localizar en la nota", NOTA + " Subraya las palabras de la ficha. ¿Cuáles son?", ["Leo con atención.", "Aparecen mapu, ko, antü y chaltumay."], "mapu, ko, antü y chaltumay"),
        W("Leer el significado", "En la nota, ¿qué significa «mapu» según la ficha?", ["Busco mapu.", "La ficha dice tierra."], "tierra"),
    ],
    mistakes=[
        M("Pasar por alto una palabra de la ficha.", "Pierdo parte del sentido.", "Leo dos veces y subrayo."),
        M("Inventar el significado de una palabra que no está en la ficha.", "Puedo equivocarme.", "La marco y pregunto."),
    ],
    R=[
        ex("Según la ficha, «ko» es: A) agua B) casa.", "A", "La ficha dice agua."),
        ex("El territorio es: A) el lugar donde vive y trabaja una comunidad B) un tipo de comida.", "A", "Es el lugar de la comunidad."),
        ex("Subrayar sirve para: A) marcar palabras importantes B) borrar.", "A", "Marca lo importante."),
    ],
    C=[
        ex(NOTA + " ¿Para qué se usó el ko?", "para regar", "La nota dice «ko para regar»."),
        ex("Verdadero o falso: una expresión significa siempre lo mismo para todos los pueblos.", "Falso", "Cada cultura tiene su significado."),
        ex(NOTA + " ¿Qué palabra de la ficha agradece?", "chaltumay", "Significa gracias en mapuzugun."),
    ],
    A=[
        ex(NOTA + " ¿Cuál de estas palabras de la ficha NO aparece en la nota: mapu, kuyen o ko?", "kuyen", "La nota usa mapu y ko, pero no kuyen."),
        ex(NOTA + " ¿Para qué se usó la mapu?", "para sembrar", "La nota dice «mapu para sembrar»."),
        arith("La nota tiene 4 palabras de la ficha y la invitación tiene 4 palabras de la ficha. ¿Cuántas hay entre las dos?", "4 + 4", "Sumo las palabras de los dos textos."),
    ],
    Z=[
        ex("Eva subrayó mapu, ko, antü y chaltumay. Gaspar subrayó solo ko. ¿Quién localizó todas las expresiones de la ficha?", "Eva", "Subrayó las cuatro."),
        ex("Una persona dice que «comunidad» significa lo mismo para todos los pueblos. ¿Qué debe hacer: A) preguntar al educador tradicional B) afirmarlo?", "A", "El significado lo explica la comunidad."),
    ],
    D=[
        arith("Un texto tiene 9 expresiones y la ficha explica 6. ¿Cuántas faltan en la ficha?", "9 - 6", "Resto las explicadas."),
        ex("Una expresión no está en la ficha. ¿Qué haces: A) la marco y pregunto B) invento su significado?", "A", "No debo inventar."),
    ],
    context=[ex("Lees «la comunidad cuida el territorio». ¿Qué haces con «territorio»: «reviso su definición de la clase» o «adivino»?", "«reviso su definición de la clase»", "La definición me da el significado.")],
    selfcheck=[
        ex("¿Qué es una expresión significativa?", "una palabra o frase con valor especial para una cultura", "Eso la hace significativa."),
        ex("¿Qué es el territorio?", "el lugar donde vive y trabaja una comunidad", "Es el lugar de la comunidad."),
        ex("¿Qué hago si una expresión no está en la ficha?", "la marco y pregunto", "Así no invento significados."),
    ],
    task=T(
        "Lee esta nota inventada: " + NOTA + " Subraya las palabras de la ficha y escribe una tabla con cada palabra y su significado. Marca con un signo de pregunta cualquier expresión que no esté en la ficha. Escribe una pregunta para el educador tradicional sobre las expresiones de la nota.",
        "mapu: tierra. ko: agua. antü: sol. chaltumay: gracias. Pregunta: ¿cómo usan estas palabras en la comunidad?",
        ["subraya las palabras de la ficha", "escribe su significado", "marca y pregunta por lo que no sabe"],
        ["tabla escrita en el cuaderno"],
        ["inventar significados", "pasar por alto palabras"],
        "Valora que localizó todas; si inventó un significado, pídele que mire la ficha.",
    ),
    reinforce="Lee la nota en voz alta y señala cada palabra de la ficha.",
    extend="Busca en un texto de tu casa una palabra importante y pregunta a una persona qué significa.",
)

L(
    LR3, 3,
    materials="Lápiz y hoja. La nota está escrita aquí y es inventada. " + FICHA_PAL,
    use="Aprenderé a relacionar datos dentro del mismo texto, como causa y efecto o antes y después. Sirve para entender mejor lo que pasa y por qué.",
    prior=["Sé localizar expresiones significativas.", "Sé ordenar hechos."],
    explain=[
        "Relacionar información interna es unir datos que están en el mismo texto. Puedo unir un dato con su causa, con su efecto o con otro dato de cantidad. Por ejemplo, si el texto dice que se sembraron 8 semillas y que brotaron 6, puedo calcular cuántas no brotaron.",
        "La causa es lo que hace que algo pase y el efecto es lo que pasa. Palabras como porque, por eso y entonces ayudan. En la nota de las semillas, regar con ko cada día puede ayudar a que las semillas broten, pero la nota no lo afirma. Distingo lo que el texto dice de lo que yo supongo.",
        "Trabajo solo con datos del texto. Si me piden algo que el texto no dice, respondo «el texto no lo dice». Así no invento nada sobre la cultura ni sobre las personas.",
    ],
    vocab=[("causa", "lo que hace que algo pase"), ("efecto", "lo que pasa por una causa"), ("dato", "información concreta del texto"), ("cantidad", "cuánto o cuántos hay"), ("suponer", "pensar algo que el texto no dice")],
    worked=[
        W("Unir cantidades", SEMILLAS + " ¿Cuántas semillas no brotaron?", ["Sembraron 8.", "Brotaron 6.", "Resto 8 − 6."], "2"),
        W("Distinguir lo que dice el texto", SEMILLAS + " ¿El texto afirma que el ko hizo brotar las semillas?", ["El texto dice que regaron con ko y que brotaron 6.", "No dice que una cosa causó la otra."], "No, solo da los dos datos"),
    ],
    mistakes=[
        M("Afirmar una causa que el texto no dice.", "Estoy suponiendo.", "Digo «el texto no lo dice»."),
        M("Mirar solo un dato y olvidar otro.", "La información se completa uniendo datos.", "Releo y uno los datos."),
    ],
    R=[
        ex(SEMILLAS + " ¿Cuántas semillas sembraron?", "8", "La nota dice 8 semillas."),
        ex(SEMILLAS + " ¿Cuántas brotaron?", "6", "La nota dice 6 semillas."),
        ex("La causa es: A) lo que hace que algo pase B) lo que pasa después.", "A", "Causa es el origen."),
    ],
    C=[
        ex(SEMILLAS + " ¿Con qué regaron?", "con ko", "La nota dice ko."),
        ex("Verdadero o falso: puedo decir que el ko hizo brotar las semillas porque lo imagino.", "Falso", "El texto no lo dice."),
        ex(SEMILLAS + " ¿Cuándo regaron: cada día o cada mes?", "cada día", "La nota dice cada día."),
    ],
    A=[
        arith("Sembraron 8 semillas y brotaron 6. ¿Cuántas no brotaron?", "8 - 6", "Resto las brotadas del total."),
        ex("Ordena según la nota: A) brotaron 6 B) regaron cada día C) sembraron 8. Escribe las letras.", "C, B, A", "Sembraron, regaron y brotaron."),
        arith("Imagina que cada semilla que brotó da 2 hojas. ¿Cuántas hojas hay con las 6 brotadas?", "6 * 2", "Multiplico semillas por hojas."),
    ],
    Z=[
        ex("Eva dice: «Brotaron 6 de 8». Gaspar dice: «Brotaron todas». ¿Quién relacionó bien los datos?", "Eva", "6 de 8 es lo que dice la nota."),
        ex("Una persona pregunta qué significa el ko para el pueblo que sembró. ¿Qué respondes: A) el texto no lo dice B) es sagrado?", "A", "El texto no da ese dato."),
    ],
    D=[
        arith("En otra nota, sembraron 10 semillas y brotaron 7. ¿Cuántas no brotaron?", "10 - 7", "Resto las brotadas."),
        ex("Dos datos de la nota: sembraron en la mapu y regaron con ko. Si falta uno de los dos, ¿se entiende la nota completa: sí o no?", "no", "Faltaría información importante."),
    ],
    context=[ex("Lees que sembraron semillas y que brotaron 6. Te preguntan por qué brotaron. ¿Respondes «el texto no lo dice, solo da los datos» o «por magia»?", "«el texto no lo dice, solo da los datos»", "No agrego causas que el texto no da.")],
    selfcheck=[
        ex("¿Qué es relacionar información interna?", "unir datos del mismo texto", "Los datos están en el texto."),
        ex("¿Qué palabra ayuda a unir causa y efecto?", "porque", "Une una causa con su efecto."),
        ex("¿Qué digo si el texto no da un dato?", "el texto no lo dice", "No invento nada que falte."),
    ],
    task=T(
        "Lee esta nota inventada: " + SEMILLAS + " Escribe tres frases: una con un dato de cantidad, una que una dos datos (por ejemplo, cuántas no brotaron) y una que empiece con «el texto no dice…».",
        "Sembraron 8 semillas. Brotaron 6, así que 2 no brotaron (8 − 6 = 2). El texto no dice por qué algunas no brotaron.",
        ["una frase con cantidad", "una frase que une dos datos", "una frase con «el texto no dice…»"],
        ["tres frases escritas en el cuaderno"],
        ["afirmar causas que no están", "no usar los datos"],
        "Valora que unió datos sin inventar; si inventó una causa, pídele que escriba «el texto no dice».",
    ),
    reinforce="Cuenta con tus palabras qué pasó con las semillas de la nota.",
    extend="Busca una nota breve en tu casa y une dos datos de ella.",
)

L(
    LR3, 4,
    materials="Lápiz y hoja. El cuento está escrito aquí y es inventado. " + FICHA_PAL,
    use="Aprenderé a responder sobre un texto usando solo lo que dice, sin tener que contar vivencias personales. Sirve para opinar con respeto y sin exponerme.",
    prior=["Sé unir datos del texto.", "Sé opinar con una razón."],
    explain=[
        "Responder un texto con respeto significa usar el texto como evidencia. Puedo responder de tres formas: con un dato del texto, con una opinión sobre el contenido o con una pregunta que me gustaría hacer. Ninguna de las tres exige contar mi vida.",
        "Una opinión fundamentada lleva «porque» y un dato. Por ejemplo, sobre el cuento de Mía: «Me gustó que Mía agradeciera porque dijo chaltumay al llegar a la ruka». No necesito decir si me ha pasado algo así. Si quiero conectar con mi experiencia puedo hacerlo, pero es siempre voluntario.",
        "Cuando el texto habla de una cultura, mi opinión no corrige su cosmovisión ni compara pueblos. Hablo de lo que dice el texto y, si tengo dudas, las convierto en preguntas para el educador tradicional.",
    ],
    vocab=[("evidencia", "dato del texto que apoya una respuesta"), ("opinión", "lo que pienso con una razón"), ("voluntario", "que se hace solo si uno quiere"), ("contenido cultural", "lo que el texto muestra de una cultura"), ("pregunta abierta", "pregunta que tiene varias respuestas posibles")],
    worked=[
        W("Responder con evidencia", CUENTO + " ¿Qué sintió Mía al llegar?", ["Busco la emoción.", "El texto dice alegría."], "alegría"),
        W("Opinar sin contar la vida", "Pía no quiere hablar de su casa. ¿Cómo opina sobre el cuento?", ["Usa un dato del cuento.", "Dice «me gustó porque Mía agradeció»."], "Con un dato del cuento y un porque"),
    ],
    mistakes=[
        M("Pedir a alguien que cuente algo de su familia para responder.", "Es privado.", "Ofrezco responder con el texto."),
        M("Opinar que la cultura del texto «está mal».", "No corresponde juzgar la cultura.", "Pregunto con respeto al educador tradicional."),
    ],
    R=[
        ex(CUENTO + " ¿De dónde trajo Mía el ko?", "del río", "El cuento dice «desde el río»."),
        ex(CUENTO + " ¿Quién la esperaba?", "su ñuke", "El cuento dice que la esperaba su ñuke."),
        ex(CUENTO + " Opinión: «Mía estaba contenta». ¿Qué dato del cuento la apoya: «Mía sintió alegría» o «Luego ambas regaron las plantas»?", "«Mía sintió alegría»", "Ese dato del texto es la evidencia de la opinión."),
    ],
    C=[
        ex("Verdadero o falso: debo contar una vivencia mía para responder.", "Falso", "Puedo responder con el texto."),
        ex(CUENTO + " ¿Qué dijo Mía cuando llegó?", "chaltumay", "El cuento lo dice."),
        ex("Una pregunta abierta tiene: A) varias respuestas posibles B) una sola respuesta.", "A", "Abierta admite varias."),
    ],
    A=[
        ex(CUENTO + " Respuesta 1: «Me gustó el cuento». Respuesta 2: «Me gustó el cuento porque Mía agradeció a su ñuke». ¿Cuál lleva una razón apoyada en el texto? Escribe 1 o 2.", "2", "La respuesta 2 dice porque y cita lo que hace Mía en el cuento."),
        arith("Imagina que Mía llevó 3 vasijas de ko y su ñuke llevó 2 más. ¿Cuántas vasijas llevaron en total?", "3 + 2", "Sumo las vasijas de ambas."),
        ex(CUENTO + " Tres respuestas: 1) «Mía sintió alegría». 2) «Me gustó que agradeciera porque dijo chaltumay». 3) «¿Cómo agradecen en la comunidad?». ¿Cuál es la opinión? Escribe 1, 2 o 3.", "2", "La 1 es un dato del texto, la 2 es una opinión con porque y la 3 es una pregunta."),
    ],
    Z=[
        ex("Eva: «Me gustó porque Mía agradeció». Gaspar: «Tienes que contar una vez que tú agradeciste». ¿Quién respeta la privacidad?", "Eva", "No exige vivencias."),
        ex("Una niña dice que «esa cultura está mal por hacer eso». ¿Qué error comete: A) juzga una cultura B) cita un dato?", "A", "No debo juzgar la cultura."),
    ],
    D=[
        arith("De 20 respuestas del curso, 14 usaron datos del texto. ¿Cuántas no los usaron?", "20 - 14", "Resto las que usaron datos."),
        ex("Si quiero preguntar al educador tradicional sobre el cuento, ¿qué tipo de pregunta hago: A) una abierta B) una que juzgue?", "A", "Las preguntas abiertas respetan."),
    ],
    context=[ex("Te piden opinar sobre el cuento de Mía. ¿Respondes «Me gustó porque Mía agradeció» o «Me pasó lo mismo»?", "«Me gustó porque Mía agradeció»", "Usa el texto como evidencia.")],
    selfcheck=[
        ex("¿Qué uso como evidencia?", "un dato del texto", "El texto sostiene mi respuesta."),
        ex("¿Estoy obligado a contar mi vida?", "No", "Es una decisión voluntaria."),
        ex("¿Qué hago con una duda sobre la cultura del texto?", "pregunto al educador tradicional", "Él o ella orienta."),
    ],
    task=T(
        "Lee el cuento inventado: " + CUENTO + " Escribe tres respuestas usando solo el texto: un dato que lo muestre (¿qué sintió Mía?), una opinión con «porque» y una pregunta abierta para el educador tradicional. No cuentes cosas de tu familia.",
        "Mía sintió alegría. Me gustó que agradeciera porque dijo chaltumay. Pregunta: ¿cómo agradecen en la comunidad?",
        ["un dato del texto", "una opinión con porque", "una pregunta abierta"],
        ["tres respuestas escritas en el cuaderno"],
        ["contar vivencias privadas", "juzgar la cultura"],
        "Valora que usó evidencia; si contó cosas privadas, recuérdale que no es necesario.",
    ),
    reinforce="Di en voz alta tu opinión sobre el cuento con «porque» y un dato.",
    extend="Lee el cuento a una persona de tu casa y escucha su opinión sin discutir.",
)

L(
    LR3, 5,
    materials="Lápiz y hoja. Los textos están escritos aquí y son inventados. " + FICHA_PAL,
    use="Aprenderé a explicar el significado de una expresión usando el texto donde aparece. Sirve para entender una palabra por su contexto y confirmar con la ficha.",
    prior=["Sé localizar expresiones significativas.", "Sé unir datos del texto."],
    explain=[
        "El significado de una expresión depende de lo que la rodea. Esto se llama contexto. Si leo «el kuyen iluminó el patio de noche», el contexto me dice que algo ilumina de noche; la ficha confirma que kuyen es luna. Primero uso el contexto y después compruebo con la ficha.",
        "Explicar el significado «dentro del texto» significa decirlo con mis palabras, apoyándome en frases del mismo texto. Por ejemplo: «En el texto, kuyen es la luna, porque ilumina el patio de noche». No agrego significados espirituales ni históricos que el texto no menciona.",
        "Hay significados más profundos de una expresión que pertenecen a una cultura. Esos los explica el educador tradicional. Yo explico solo lo que el texto muestra y la ficha confirma, y reconozco lo que no sé.",
    ],
    vocab=[("contexto", "lo que rodea a una palabra en el texto"), ("parafrasear", "decir con mis palabras lo que dice el texto"), ("confirmar", "comprobar que algo es correcto"), ("significado", "lo que quiere decir una palabra"), ("pista", "dato que ayuda a descubrir")],
    worked=[
        W("Explicar con contexto", KUYEN + " ¿Qué significa kuyen en el texto?", ["Busco pistas: es de noche, ilumina el patio y los niños miraron el cielo.", "La ficha dice luna."], "luna"),
        W("Parafrasear", KUYEN + " Explica con tus palabras qué pasó.", ["Fue de noche.", "La luna iluminó el patio y los niños miraron en silencio."], "La luna iluminó el patio de noche y los niños la miraron en silencio"),
    ],
    mistakes=[
        M("Agregar un significado espiritual al texto.", "El texto no lo dice.", "Explico solo lo que el texto muestra."),
        M("Explicar sin mirar el contexto.", "Puedo equivocarme.", "Busco pistas alrededor de la palabra."),
    ],
    R=[
        ex(KUYEN + " ¿Dónde iluminó el kuyen?", "en el patio", "El texto dice el patio."),
        ex("Según la ficha, «kuyen» es: A) luna B) agua.", "A", "La ficha dice luna."),
        ex("El contexto es: A) lo que rodea a una palabra B) el título.", "A", "El contexto da pistas."),
    ],
    C=[
        ex(KUYEN + " ¿Cuándo pasó: de noche o de día?", "de noche", "El texto dice «esa noche»."),
        ex("Verdadero o falso: puedo agregar significados espirituales que el texto no dice.", "Falso", "Eso lo explica la comunidad."),
        ex(KUYEN + " ¿Qué hicieron los niños?", "miraron el cielo y guardaron silencio", "Lo dice la segunda oración."),
    ],
    A=[
        ex("Texto: «El kuyen iluminó el patio». Ya buscaste pistas en el contexto. ¿Qué haces para confirmar el significado: A) reviso la ficha B) agrego un significado espiritual?", "A", "Primero el contexto y después la ficha; no se agregan significados que el texto no dice."),
        ex("Texto: «El antü calentó la mapu». Según la ficha, ¿qué calentó el sol?", "la tierra", "La ficha dice que mapu es tierra."),
        arith("Imagina que los niños miraron el cielo 5 minutos el lunes y 4 el martes. ¿Cuántos minutos miraron en total?", "5 + 4", "Sumo los minutos de los dos días."),
    ],
    Z=[
        ex("Dos explicaciones de kuyen en el texto. Eva: «Es la luna, porque ilumina de noche». Gaspar: «Es un animal». ¿Quién usa el contexto?", "Eva", "Su explicación se apoya en el texto."),
        ex("Una persona explica el significado espiritual de la luna para un pueblo sin haberlo aprendido. ¿Qué error comete: A) afirma lo que no sabe B) usa la ficha?", "A", "No puede afirmarlo."),
    ],
    D=[
        arith("El texto tiene 2 oraciones: la primera tiene 7 palabras y la segunda tiene 8. ¿Cuántas palabras tiene el texto?", "7 + 8", "Sumo las palabras de las dos oraciones."),
        ex("Quieres saber el significado profundo de una expresión para una cultura. ¿A quién preguntas: A) al educador tradicional B) a nadie?", "A", "Él o ella conoce ese significado."),
    ],
    context=[ex("Lees «el kuyen iluminó el patio» y no recuerdas qué es kuyen. ¿Qué haces: «busco pistas en el texto y reviso la ficha» o «invento»?", "«busco pistas en el texto y reviso la ficha»", "Así confirmo el significado.")],
    selfcheck=[
        ex("¿Qué uso primero para entender una palabra?", "el contexto", "Aporta pistas para entender."),
        ex("¿Qué significa parafrasear?", "decir con mis palabras lo que dice el texto", "Es explicar con mis palabras."),
        ex("¿Quién explica los significados profundos?", "el educador tradicional", "Él o ella los conoce."),
    ],
    task=T(
        "Lee este texto inventado: " + KUYEN + " Escribe qué significa kuyen en el texto y qué pista del contexto lo muestra. Luego escribe con tus palabras (sin agregar significados que el texto no dice) qué pasó. Termina con una pregunta para el educador tradicional sobre lo que no puedes saber del texto.",
        "Kuyen es la luna. Pistas: es de noche, ilumina el patio y los niños miraron el cielo. Pasó que, de noche, la luna iluminó el patio y los niños miraron en silencio. Pregunta: ¿qué significa la luna para su pueblo?",
        ["explica el significado con contexto", "parafrasea sin agregar", "formula una pregunta para quien enseña"],
        ["explicación escrita en el cuaderno"],
        ["agregar significados espirituales", "no usar el contexto"],
        "Valora que usó el contexto y no agregó; si agregó significados, pídele que se quede con el texto.",
    ),
    reinforce="Elige una frase del texto y explícala con tus palabras.",
    extend="Lee el texto a una persona de tu casa y explícale qué significa kuyen y por qué.",
)
