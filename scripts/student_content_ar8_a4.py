"""Cuaderno del estudiante de 8.º básico Artes Visuales: AR08 OA 04 (análisis de manifestaciones visuales patrimoniales y contemporáneas)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA4 = "AR08 OA 04"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def w(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def m(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=[ctx], selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- Clase 1
lesson(
    OA4, 1,
    "Hojas, lápiz de mina y lápices de colores. Las tres manifestaciones de ejemplo están descritas en esta clase; no necesitas buscarlas.",
    "Aprenderé a distinguir una manifestación patrimonial de una contemporánea y a observarla con cuatro criterios: contexto, materialidad, lenguaje visual y propósito expresivo. Sirve para analizar obras con orden y para tomar ideas sin copiar.",
    ["Sé que un referente se reinterpreta y no se copia.", "Sé separar lo que se ve de lo que opino."],
    [
        "Una manifestación visual patrimonial es una obra, objeto o práctica que una comunidad hereda, valora y cuida, como una vasija de greda, un tejido hecho a telar o un edificio antiguo. Una manifestación contemporánea es la creada en nuestra época, como un mural reciente, una instalación o una fotografía. La frontera no siempre es rígida: una práctica patrimonial puede seguir viva y cambiar hoy.",
        "Para analizar una manifestación uso cuatro criterios. El contexto es dónde, cuándo, quién y para qué se hizo o se usó. La materialidad son los materiales y las técnicas con que está hecha. El lenguaje visual son los elementos que se ven: línea, color, forma, textura y composición. El propósito expresivo es lo que la obra quiere comunicar o hacer sentir. Siempre empiezo describiendo lo que veo, sin opinar.",
        "Observar sin copiar es elegir un recurso y cambiarlo. De una vasija con bandas repetidas puedo tomar la idea de repetir en bandas y aplicarla a otro objeto. Pero si la obra viene de una comunidad, no copio sus motivos como si fueran míos: los respeto, pregunto por su significado y cito su procedencia. Además, una sola obra no representa a toda una cultura.",
    ],
    [("patrimonial", "heredado, valorado y cuidado por una comunidad"), ("contemporáneo", "creado en nuestra época"), ("materialidad", "materiales y técnicas con que está hecha una obra"), ("lenguaje visual", "elementos con que se ve una obra: línea, color, forma, textura y composición"), ("propósito expresivo", "lo que la obra quiere comunicar o hacer sentir")],
    [
        w("Aplicar los cuatro criterios", "Vasija de greda de ejemplo: de uso doméstico, pulida, rojiza, con bandas de líneas incisas repetidas. Analízala con los cuatro criterios.", ["Contexto: objeto de uso doméstico.", "Materialidad: greda pulida.", "Lenguaje visual: color rojizo y bandas de líneas repetidas.", "Propósito expresivo: la ficha no lo dice; queda pendiente."], "Contexto: uso doméstico; materialidad: greda pulida; lenguaje visual: rojizo con bandas repetidas; propósito pendiente"),
        w("Copia o reinterpretación", "Tejido de ejemplo con rombos rojos y cafés repetidos en filas. Rocío dibuja el mismo tejido con los mismos rombos y colores. Iván toma la idea de «repetir una forma geométrica en filas» y repite triángulos azules en una tira de papel. ¿Quién copia y quién reinterpreta?", ["Rocío repite las formas y los colores.", "Iván conserva solo el recurso de repetir en filas.", "Iván cambia la forma y los colores."], "Rocío copia; Iván reinterpreta"),
    ],
    [
        m("Escribir solo «es antigua y me parece fea» al analizar una obra.", "No hay descripción ni criterio que se pueda comprobar.", "Describe lo que ves con los cuatro criterios y apoya tu opinión después."),
        m("Decir que una obra muestra cómo son todas las comunidades de un tipo.", "Una obra muestra una forma de hacer, no a todas.", "Habla de esa obra y de su procedencia."),
    ],
    [
        ex("Una manta de lana tejida en telar, con rombos repetidos, es transmitida de generación en generación por una comunidad que la cuida. ¿Es patrimonial o contemporánea?", "Patrimonial", "Una comunidad la hereda, la valora y la cuida."),
        ex("¿Qué criterio se refiere a los materiales y las técnicas de una obra?", "La materialidad", "Responde con qué y cómo está hecha."),
        ex("La frase «las líneas incisas forman bandas repetidas» corresponde a un criterio. A. Lenguaje visual B. Contexto.", "A", "Describe líneas y repetición, elementos visuales."),
    ],
    [
        ex("Un mural de ejemplo en un muro de barrio tiene figuras grandes y letras, y se pintó con pintura de exteriores. ¿Qué dato es de materialidad? A. Pintura de exteriores B. Está en un barrio.", "A", "Dice con qué material se hizo; estar en un barrio es contexto."),
        ex("Analizas la vasija y escribes «es antigua y me parece fea». ¿Qué falta? A. Describir lo que se ve y apoyar la opinión B. Agregar más adjetivos.", "A", "Una opinión necesita descripción y razón."),
        ex("Una compañera dice que la vasija muestra cómo son todas las comunidades alfareras. ¿Qué error comete?", "Generaliza a todas las comunidades desde una sola vasija", "Una obra muestra una forma de hacer, no todas."),
    ],
    [
        ex("Tres frases sobre el tejido: 1) «Tiene rombos repetidos». 2) «Es el más bonito». 3) «Está hecho con lana». ¿Cuántas son descripciones de lo que se ve o de su material?", "2", "La 1 y la 3 se comprueban; la 2 es una opinión."),
        ex("Quieres tomar el recurso de las bandas repetidas de la vasija. ¿Qué plan lo reinterpreta y respeta la procedencia? A. Rodear un vaso de cartón con bandas de líneas propias y anotar de qué referente viene la idea B. Dibujar los mismos signos de la vasija y firmarlos como diseño propio.", "A", "Crea bandas propias y cita la fuente."),
        ex("Ficha de la vasija de ejemplo: de uso doméstico, para guardar agua, de greda pulida, rojiza. Une cada dato con su criterio: a) «Se usaba para guardar agua». b) «Está hecha de greda». c) «Los colores son rojizos». Criterios: 1 contexto, 2 materialidad, 3 lenguaje visual. Escribe cada letra con su número.", "a-1, b-2, c-3", "Cada dato responde a un criterio distinto."),
    ],
    [
        ex("Marcos dibuja la vasija con las mismas bandas y el mismo color. Sara usa solo la idea de bandas repetidas para decorar una caja con bandas de puntos azules. ¿Quién da más espacio a la autoría propia?", "Sara", "Cambia forma y color y conserva un recurso."),
        ex("Dos personas describen el mismo mural. Una escribe «los colores son vivos y las figuras grandes». La otra, «es horrible». ¿Cuál es una descripción de lenguaje visual?", "La primera", "Habla de color y tamaño; la otra es solo opinión."),
    ],
    [
        ex("Para comparar un mural reciente y una vasija antigua, ¿qué es más justo? A. Usar los mismos cuatro criterios en ambas B. Preguntar solo cuál es más bonita.", "A", "Los criterios permiten comparar con orden."),
        ex("Una ficha de análisis dice: «Contexto: se usaba para guardar agua. Materialidad: greda pulida. Propósito: guardar y decorar». ¿Qué criterio falta?", "El lenguaje visual", "No describe líneas, colores ni formas."),
    ],
    ex("En una feria de patrimonio local ves un tejido con rombos repetidos y quieres diseñar tu propio cuaderno. ¿Qué haces para respetar la procedencia? A. Tomar el recurso de repetir una forma geométrica, hacer tus propias formas y citar el tejido B. Copiar los rombos y decir que los inventaste.", "A", "Reinterpreta el recurso y reconoce la fuente."),
    [
        ex("¿Cuáles son los cuatro criterios de análisis de la clase?", "Contexto, materialidad, lenguaje visual y propósito expresivo", "Son los que permiten analizar con orden."),
        ex("Verdadero o falso: una vasija patrimonial muestra cómo son todas las comunidades alfareras.", "Falso", "Solo muestra una forma de hacer."),
        ex("¿Qué haces primero al analizar una obra: describir o valorar?", "Describir", "Se parte de lo que se ve, sin opinar."),
    ],
    task(
        "Elige UNA manifestación de ejemplo. A) Vasija de greda de uso doméstico, pulida, rojiza, con bandas de líneas incisas repetidas. B) Mural en un muro de barrio, con figuras grandes de colores vivos y letras, pintado con pintura de exteriores. C) Manta tejida a telar con lana teñida con tintes vegetales y rombos rojos y cafés repetidos, usada como abrigo. Haz una tabla con los cuatro criterios y dos datos de lo que se ve, marca «pendiente» lo que la descripción no dice y dibuja un boceto que reinterprete un recurso con materiales propios.",
        "Elegí la A. Contexto: objeto doméstico. Materialidad: greda pulida. Lenguaje visual: color rojizo y bandas repetidas. Propósito: pendiente. Boceto: bandas de líneas propias alrededor de un vaso de cartón. Procedencia anotada: vasija de ejemplo de esta clase.",
        ["completa los cuatro criterios con datos de la descripción", "marca como pendiente lo que no sabe", "hace un boceto que reinterpreta un recurso", "no copia los motivos ni los presenta como propios"],
        ["tabla de cuatro criterios", "boceto", "procedencia anotada"],
        ["opinar sin describir", "copiar los motivos de la obra"],
        "Pregunta qué criterio quedó pendiente y qué recurso tomó para su boceto.",
    ),
    "Mira un objeto de uso diario en tu casa y di en voz alta su material, un detalle de su forma y para qué se usa.",
    "Elige una obra y explica en tres frases por qué podría considerarse patrimonial y por qué podría ser contemporánea.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA4, 2,
    "Hojas y lápiz. Las tres fichas de manifestaciones están escritas en esta clase.",
    "Aprenderé a investigar el contexto, la materialidad y el propósito de una manifestación, a elegir fuentes confiables y a separar datos de inferencias. Sirve para analizar con respaldo y no con suposiciones.",
    ["Sé los cuatro criterios de análisis.", "Sé separar datos de inferencias."],
    [
        "Para investigar el contexto me hago preguntas: ¿quién la hizo?, ¿dónde y cuándo?, ¿para quién?, ¿para qué se usaba o se usa? y ¿cómo cambió su uso? Para la materialidad pregunto de qué está hecha y cómo se hizo. Para el propósito pregunto qué quiere comunicar o hacer. En una manifestación patrimonial también pregunto por qué la comunidad la cuida: puede ser por su uso diario, por la memoria que guarda o por el saber hacer que se transmite.",
        "Una fuente confiable dice quién escribe, cuándo y de dónde viene la información. Puede ser la ficha de un museo, el relato de las personas que hacen la obra, un libro o el sitio de una institución. Un comentario anónimo sin datos no sirve como respaldo. Si dos fuentes dicen cosas distintas, busco una tercera con autoría y procedencia, en vez de quedarme con la que más me gusta.",
        "Distingo datos de inferencias. «Se usaba para guardar agua» es un dato si la ficha lo afirma; «porque no había llaves» es una inferencia que nadie escribió. Lo que falta lo marco como pendiente. Con el contexto, la materialidad y el propósito puedo explicar por qué una obra es como es, y no solo cómo se ve.",
    ],
    [("fuente", "lugar de donde sale una información, como una ficha de museo o el relato de quien hace la obra"), ("saber hacer", "conocimiento de una técnica que se transmite entre personas"), ("dato", "información que una fuente afirma"), ("inferencia", "idea que deduzco a partir de los datos"), ("procedencia", "lugar y autoría de donde viene una obra o una información")],
    [
        w("Leer una ficha", "Ficha de ejemplo: «Manta tejida a telar con lana teñida con tintes vegetales; rombos rojos y cafés repetidos; usada como abrigo y transmitida de una generación a otra en una comunidad». Señala contexto, materialidad y lenguaje visual.", ["Contexto: abrigo transmitido en una comunidad.", "Materialidad: lana teñida con tintes vegetales, tejida a telar.", "Lenguaje visual: rombos rojos y cafés repetidos."], "Contexto: abrigo transmitido; materialidad: lana con tintes vegetales; lenguaje visual: rombos repetidos"),
        w("Elegir entre fuentes", "Una fuente anónima dice que la manta se hizo para vender y la ficha de un museo, con autoría y procedencia, dice que se usaba como abrigo. ¿Cuál respaldo usas?", ["La ficha dice quién escribe y de dónde viene.", "El comentario anónimo no da datos."], "La ficha del museo"),
    ],
    [
        m("Quedarse con la fuente que más gusta aunque no tenga autoría.", "No hay forma de comprobar si es confiable.", "Elige fuentes que digan quién escribe y de dónde viene la información."),
        m("Escribir una explicación inventada para llenar un dato que falta.", "Se mezcla lo que se sabe con lo que se imagina.", "Márcalo como pendiente o como inferencia."),
    ],
    [
        ex("Ficha: «Vasija de greda pulida, rojiza, para guardar agua». ¿Cuál es su material?", "Greda", "La ficha lo nombra."),
        ex("¿Qué pregunta investiga el contexto? A. ¿Para qué se usaba y quién la hacía? B. ¿Qué colores tiene?", "A", "Los colores pertenecen al lenguaje visual."),
        ex("¿Qué pregunta se refiere a la materialidad? A. ¿De qué está hecha y cómo se hizo? B. ¿Para quién se hizo?", "A", "La materialidad responde con qué y cómo."),
    ],
    [
        ex("Ficha de una vasija de ejemplo: «Se usaba para guardar agua». ¿Qué afirmación es un dato? A. La vasija se usaba para guardar agua B. La vasija se usaba para guardar agua porque en esa comunidad no había llaves.", "A", "La ficha afirma el uso, pero no la razón."),
        ex("¿Por qué una manta transmitida de generación en generación es patrimonial? A. Una comunidad la transmite y la cuida B. Está hecha de lana.", "A", "El patrimonio nace del valor y el cuidado de una comunidad."),
        ex("Un mural de ejemplo está pintado en un muro exterior de un barrio. ¿A quién llega más fácilmente: a quien pasa por la calle o a quien entra a un museo?", "A quien pasa por la calle", "Un muro exterior se ve desde la vereda."),
    ],
    [
        arith("Una alfarera de ejemplo hace 4 vasijas por semana. ¿Cuántas hace en 6 semanas?", "4*6", "Se multiplica lo que hace por semana por las semanas."),
        arith("Una manta de ejemplo lleva 9 filas de rombos y cada fila tiene 14 rombos. ¿Cuántos rombos tiene en total?", "9*14", "Se multiplica la cantidad de filas por los rombos de cada fila."),
        ex("Una ficha entrega cinco datos: quién la hizo, dónde, de qué material, para qué se usaba y cuándo. ¿Cuántos son de contexto?", "4", "Quién, dónde, para qué se usaba y cuándo son contexto; el material es materialidad."),
    ],
    [
        ex("Dos fuentes dicen cosas distintas sobre el uso de una vasija. ¿Qué haces? A. Busco una tercera fuente con autoría y procedencia B. Elijo la que me gusta más.", "A", "Una tercera fuente confiable ayuda a decidir."),
        ex("El mural invita a cuidar la plaza; la vasija se usaba para guardar agua. ¿Cuál de las dos tiene el propósito de invitar a la comunidad a cuidar algo?", "El mural", "Su propósito es una invitación; la vasija era de uso doméstico."),
    ],
    [
        ex("Un compañero escribe: «La manta se hace con tintes vegetales porque antes no había otros colores». ¿Qué tipo de afirmación es y qué le falta?", "Una inferencia; le falta una fuente", "Nadie escribió esa razón en la ficha."),
        ex("La ficha del mural no dice quién lo hizo. ¿Qué criterio queda incompleto?", "El contexto", "Quién lo hizo es parte del contexto."),
    ],
    ex("Presentarás la vasija a tu curso. La ficha dice que se usaba en la vida diaria y que la hacía una alfarera de una comunidad. ¿Qué dato usas para explicar por qué se cuida? A. Que se usaba en la vida diaria y la hacía una alfarera de una comunidad B. Que es de color rojizo.", "A", "El uso y el saber de la comunidad explican el valor patrimonial."),
    [
        ex("¿Qué debe decir una fuente confiable?", "Quién escribe, cuándo y de dónde viene la información", "Así se puede comprobar."),
        ex("Verdadero o falso: si falta un dato, puedo escribirlo como si lo supiera.", "Falso", "Un dato que falta se marca como pendiente."),
        ex("¿Qué es el saber hacer?", "El conocimiento de una técnica que se transmite entre personas", "Es una razón por la que una comunidad cuida una práctica."),
    ],
    task(
        "Elige UNA ficha. A) Vasija de greda de ejemplo, hecha por una alfarera de una comunidad rural, para guardar agua, pulida, rojiza y con bandas incisas. B) Mural de ejemplo, pintado por jóvenes de un barrio en un muro exterior con pintura de exteriores, para invitar a cuidar la plaza. C) Manta de ejemplo, tejida a telar con lana teñida con tintes vegetales, con rombos rojos y cafés repetidos, usada como abrigo y transmitida en una comunidad. Haz una tabla con contexto, materialidad, lenguaje visual y propósito, marca una inferencia tuya, escribe una pregunta y nombra una fuente confiable donde la buscarías.",
        "Elegí la C. Contexto: abrigo transmitido en una comunidad. Materialidad: lana con tintes vegetales y telar. Lenguaje visual: rombos rojos y cafés repetidos. Propósito: pendiente. Inferencia: quizá cada color tiene un significado; pregunta: ¿qué significa?; fuente: relato de las personas de la comunidad que la tejen.",
        ["completa la tabla con datos de la ficha", "marca una inferencia distinta de los datos", "formula una pregunta de investigación", "nombra una fuente confiable"],
        ["tabla de cuatro criterios", "inferencia con pregunta", "fuente propuesta"],
        ["escribir como dato algo que la ficha no dice", "usar una fuente sin autoría"],
        "Señala un dato y una inferencia de la tabla y pregunta qué fuente confirmaría la inferencia.",
    ),
    "Pregunta a una persona de tu casa para qué sirve un objeto antiguo o artesanal que tengan y anota su respuesta como fuente.",
    "Escribe tres preguntas de contexto distintas para una manifestación patrimonial de tu región y di dónde buscarías cada respuesta.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA4, 3,
    "Hojas, lápiz y lápices de colores. Las descripciones de los trabajos están escritas en esta clase.",
    "Aprenderé a describir el lenguaje visual de una obra con línea, color, forma, textura y composición, y a pasar de describir a interpretar y valorar. Sirve para dar razones visuales al analizar una obra.",
    ["Sé los cuatro criterios de análisis.", "Sé separar descripción de opinión."],
    [
        "El lenguaje visual tiene varios elementos. La línea puede ser recta o curva, gruesa o delgada. El color puede ser cálido o frío, y tener alto o bajo contraste: figuras amarillas sobre fondo azul oscuro tienen alto contraste, y figuras celestes pálidas sobre fondo celeste claro, bajo. La forma puede ser geométrica, como un rombo, u orgánica, como una hoja. La textura puede ser lisa o rugosa. La composición es cómo se ordena todo: simétrica si hay lo mismo a cada lado del centro, o con repetición, que crea ritmo.",
        "Analizo en cuatro pasos. Describo lo que veo: «hay rombos rojos y cafés repetidos en filas». Analizo cómo se relacionan los elementos: «las filas son parejas y los rombos del mismo tamaño». Interpreto qué significa o qué efecto produce: «esto da sensación de orden». Valoro con una razón: «me parece una composición lograda porque el orden lleva la vista de fila en fila». Cada paso se apoya en el anterior.",
        "Una descripción no usa palabras como bonito o feo. Una interpretación se apoya en algo visible: no digo «es triste» sin decir qué detalle me hace pensar eso. Una valoración incluye una razón. Así mi análisis puede ser comprobado por otra persona que mire la misma obra, aunque piense distinto.",
    ],
    [("contraste", "diferencia marcada entre dos elementos, como el color de una figura y su fondo"), ("geométrica", "forma de lados y ángulos regulares, como un rombo o un cuadrado"), ("orgánica", "forma curva e irregular, como una hoja"), ("simetría", "orden en que hay lo mismo a cada lado de un centro"), ("ritmo", "repetición ordenada de elementos")],
    [
        w("Describir, interpretar y valorar", "Manta de ejemplo con rombos rojos y cafés del mismo tamaño, repetidos en filas parejas. Escribe una descripción, una interpretación y una valoración con razón.", ["Descripción: rombos rojos y cafés del mismo tamaño, en filas parejas.", "Interpretación: la repetición pareja da sensación de orden.", "Valoración: me parece lograda porque el orden lleva la vista de fila en fila."], "Descripción de rombos en filas, interpretación de orden y valoración con la razón de que guía la vista"),
        w("Contraste de color", "En un mural, figuras amarillas se ven sobre un fondo azul oscuro. ¿El contraste es alto o bajo?", ["El amarillo es muy claro.", "El azul oscuro es muy oscuro.", "La diferencia entre ambos es grande."], "Alto"),
    ],
    [
        m("Mezclar descripción, interpretación y valoración en una sola frase.", "El lector no sabe qué es dato y qué es opinión.", "Escribe cada paso en una frase separada."),
        m("Valorar sin dar una razón visual.", "La valoración no se puede comprobar.", "Agrega «porque…» con un detalle de la obra."),
    ],
    [
        ex("Los rombos son formas con ángulos y lados rectos. ¿Son geométricos u orgánicos?", "Geométricos", "Los lados rectos y los ángulos regulares son geométricos."),
        ex("El rojo y el café, ¿son colores cálidos o fríos?", "Cálidos", "Se asocian al calor y la tierra."),
        ex("Un mismo rombo se repite en filas. ¿Qué recurso crea ritmo?", "La repetición", "La repetición ordenada produce ritmo."),
    ],
    [
        ex("Una figura está al centro y hay los mismos elementos a cada lado. ¿Qué composición es?", "Simétrica", "Lo mismo a cada lado de un centro es simetría."),
        ex("Figuras amarillas sobre un fondo azul oscuro, ¿tienen alto o bajo contraste?", "Alto", "Los colores se diferencian mucho."),
        ex("La superficie de la vasija está pulida y brilla suavemente. ¿Su textura es lisa o rugosa?", "Lisa", "Pulida significa sin asperezas."),
    ],
    [
        arith("En una manta de ejemplo hay 8 rombos rojos y el doble de rombos cafés. ¿Cuántos rombos cafés hay?", "8*2", "El doble se calcula multiplicando por dos."),
        arith("Un borde alterna dos líneas gruesas y una delgada, en grupos de 3. Tiene 12 líneas en total. ¿Cuántas son delgadas?", "12//3", "Hay una delgada por cada grupo de 3."),
        ex("Une cada frase con su paso. a) «Hay figuras grandes con colores vivos». b) «Parece que quiere llamar la atención de quien pasa». c) «Me parece lograda porque las letras grandes se leen desde lejos». Pasos: 1 descripción, 2 interpretación, 3 valoración con razón. Escribe cada letra con su número.", "a-1, b-2, c-3", "La primera describe, la segunda interpreta y la tercera valora con razón."),
    ],
    [
        ex("Dos descripciones del mural. X) «Es bonito y alegre». Y) «Tiene figuras que ocupan casi todo el muro, colores vivos y letras grandes abajo». ¿Cuál describe el lenguaje visual?", "Y", "Habla de tamaño, color y ubicación; X es opinión."),
        ex("Quieres decir que un mural da sensación de energía. ¿Qué evidencia visual lo apoya? A. Figuras grandes con colores vivos y alto contraste B. Un fondo celeste pálido y liso.", "A", "Los colores vivos y el contraste pueden transmitir energía, y son detalles visibles que lo respaldan."),
    ],
    [
        ex("Un análisis dice: «Las letras grandes ocupan la franja inferior y tienen alto contraste; por eso se leen desde lejos». ¿Qué parte es descripción y qué parte es interpretación?", "Descripción: letras grandes en la franja inferior con alto contraste; interpretación: se leen desde lejos", "La primera parte se ve y la segunda es el efecto."),
        ex("Cambias el fondo azul oscuro del mural por un celeste claro y las figuras por un celeste pálido. ¿Qué pasa con el contraste? A. Baja porque figura y fondo son claros B. Sube.", "A", "Dos colores claros se parecen mucho."),
    ],
    ex("Te piden describir en un párrafo corto la manta de rombos sin opinar. ¿Cuál es la mejor descripción? A. «Tiene rombos rojos y cafés repetidos en filas y está hecha de lana» B. «Es una manta preciosa y muy fina».", "A", "Describe lo que se ve y su material; la otra frase opina."),
    [
        ex("¿Cuáles son los cuatro pasos para analizar el lenguaje visual?", "Describir, analizar, interpretar y valorar", "Cada paso se apoya en el anterior."),
        ex("Verdadero o falso: una descripción puede usar la palabra «bonito».", "Falso", "Describir es decir lo que se ve, sin opinión."),
        ex("¿Qué debe llevar una valoración?", "Una razón basada en algo visible", "Así otra persona puede comprobarla."),
    ],
    task(
        "Elige UNA obra de ejemplo. A) Manta con rombos rojos y cafés del mismo tamaño, repetidos en filas parejas. B) Mural con figuras amarillas muy grandes sobre fondo azul oscuro y letras grandes abajo. C) Vasija pulida y rojiza con tres bandas de líneas incisas repetidas. Escribe una descripción de línea, color, forma, textura y composición; una interpretación con un detalle visible; y una valoración con razón. Haz un dibujo rápido que cambie un elemento (por ejemplo el contraste) para ver cómo cambia el efecto.",
        "Elegí la B. Descripción: figuras amarillas grandes sobre azul oscuro, letras grandes abajo. Interpretación: el contraste alto llama la atención de quien pasa. Valoración: me parece lograda porque las letras grandes se leen desde lejos. Dibujo: cambié el fondo a celeste claro y el efecto bajó.",
        ["describe al menos tres elementos del lenguaje visual", "interpreta con un detalle visible", "valora con una razón", "hace un dibujo que cambia un elemento"],
        ["tres frases separadas", "dibujo de comparación"],
        ["mezclar opinión con descripción", "valorar sin razón"],
        "Pregunta qué detalle visible apoya la interpretación y qué cambió en el dibujo.",
    ),
    "Mira un afiche o envase en tu casa y di en voz alta un color, una forma y cómo se ordena todo, sin decir si te gusta.",
    "Escribe dos interpretaciones distintas para la misma descripción y explica qué detalle apoya a cada una.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA4, 4,
    "Hojas, lápiz y lápices de colores. Las dos obras que compararás están descritas en esta clase.",
    "Aprenderé a escribir un análisis breve y completo de una manifestación con los cuatro criterios y una valoración con razón, y a hacer una reinterpretación respetuosa. Sirve para comunicar mi análisis de manera clara.",
    ["Sé describir, interpretar y valorar con razones visuales.", "Sé citar la procedencia de un recurso."],
    [
        "Un análisis completo tiene seis partes en este orden: qué obra es, contexto, materialidad, lenguaje visual, propósito expresivo y valoración con razón. En cada parte escribo una o dos oraciones apoyadas en la descripción o la ficha. Si un dato falta, escribo «pendiente». Termino con una valoración que dice qué me parece logrado o mejorable y por qué, con un detalle visible.",
        "Para que mi análisis sea claro, uso frases específicas. En vez de «tiene colores lindos», escribo «tiene rojo y café, colores cálidos, que contrastan con el fondo claro». Comparar dos obras con los mismos criterios me ayuda a ver semejanzas y diferencias sin elegir cuál es mejor solo por su edad. Una vasija antigua y un mural reciente se pueden comparar si uso la misma regla.",
        "Como respuesta propia, también puedo hacer una reinterpretación visual: tomo un recurso, como las bandas repetidas, y lo uso en un objeto mío con formas propias. Cito de qué obra viene el recurso y no copio los motivos de una comunidad como si fueran míos. Mi análisis y mi boceto deben poder explicarse con las mismas palabras: contexto, materialidad, lenguaje visual y propósito.",
    ],
    [("análisis", "texto que explica una obra con criterios y evidencia"), ("evidencia visual", "detalle que se ve en la obra y respalda lo que digo"), ("valoración", "juicio sobre qué está logrado o mejorable, con una razón"), ("comparar", "mirar dos obras con los mismos criterios para ver semejanzas y diferencias"), ("reinterpretación", "uso propio de un recurso tomado de una obra")],
    [
        w("Armar el orden", "Ordena las partes de un análisis: valoración con razón, contexto, qué obra es, lenguaje visual, propósito, materialidad.", ["Primero se presenta la obra.", "Luego contexto y materialidad.", "Después lenguaje visual y propósito.", "Al final la valoración."], "Qué obra es, contexto, materialidad, lenguaje visual, propósito y valoración con razón"),
        w("Mejorar una frase", "Mejora esta frase: «La vasija tiene colores lindos».", ["No dice qué colores ni qué efecto.", "Agrego el color: rojizo.", "Agrego el efecto visible: contrasta con las líneas oscuras de las bandas."], "«La vasija es rojiza y sus bandas de líneas oscuras contrastan con ese color»"),
    ],
    [
        m("Elegir cuál obra es mejor solo porque es más antigua o más reciente.", "La edad no es un criterio de calidad visual.", "Compara con los mismos cuatro criterios y valora con razones."),
        m("Copiar los motivos de una comunidad como si fueran propios.", "No se reconoce su procedencia ni su significado.", "Toma el recurso, crea formas propias y cita la fuente."),
    ],
    [
        ex("En el modelo de la clase, ¿qué parte del análisis va última?", "La valoración con razón", "Cierra el análisis después de describir y analizar."),
        ex("La parte de lenguaje visual contiene... A. Línea, color, forma, textura y composición B. Quién la hizo.", "A", "Quién la hizo es contexto."),
        ex("¿Cuál valoración tiene una razón? A. «Me parece lograda porque los colores contrastan y se ve desde lejos» B. «Me parece lograda porque me gusta».", "A", "Da un detalle visible como respaldo."),
    ],
    [
        ex("Completa: «Los rombos se repiten en filas ___ y crean ___». A. regulares, ritmo B. cortadas, desorden.", "A", "Filas regulares producen ritmo."),
        ex("Un análisis dice: «Fue hecha por una alfarera de una comunidad rural para guardar agua». ¿Qué criterio desarrolla?", "El contexto", "Dice quién la hizo y para qué se usaba."),
        ex("¿Por qué conviene citar evidencia visual? A. Para que quien lea pueda comprobar lo que digo B. Para que el texto sea más largo.", "A", "La evidencia permite verificar."),
    ],
    [
        arith("Tu análisis tiene seis partes. Escribes 2 oraciones en cada una, excepto en la última, que lleva 3. ¿Cuántas oraciones escribes en total?", "2*5+3", "Cinco partes de 2 oraciones y una de 3."),
        arith("Haces una tabla para comparar 2 obras con 4 criterios. ¿Cuántas casillas debes llenar?", "2*4", "Se multiplica la cantidad de obras por la de criterios."),
        ex("¿Qué frase es un análisis de lenguaje visual con evidencia? A. «La vasija es rojiza y pulida, lo que le da un aspecto suave» B. «La vasija es linda».", "A", "Nombra color y textura y su efecto."),
    ],
    [
        ex("Análisis X del mural: «Es genial porque es colorido». Análisis Y: «Los colores vivos y las letras grandes llaman la atención de quien pasa, lo que cumple su propósito de invitar a cuidar la plaza». ¿Cuál une evidencia y propósito?", "Y", "Relaciona un detalle visible con lo que la obra quiere lograr."),
        ex("Quieres comparar una vasija y un mural con la misma regla. ¿Qué haces? A. Usar los cuatro criterios en las dos B. Usar criterios distintos para cada una.", "A", "Los mismos criterios permiten comparar."),
    ],
    [
        ex("Tu análisis dice: «La vasija representa a toda la cultura alfarera». ¿Cómo lo corriges?", "Esta vasija muestra una manera de trabajar la greda, según su ficha", "Se limita a lo que la obra muestra."),
        ex("Dos reinterpretaciones. X) Copiar los signos de una vasija y firmarlos como propios. Y) Tomar la idea de bandas repetidas, diseñar tus propias bandas y citar el referente. ¿Cuál respeta la procedencia?", "Y", "Reinterpreta el recurso y reconoce la fuente."),
    ],
    ex("Te piden un análisis breve para la mesa de una exposición del curso. ¿Qué estructura es más completa? A. Contexto, materialidad, lenguaje visual, propósito y valoración con razón B. Una opinión de dos líneas.", "A", "Cubre los cuatro criterios y la valoración."),
    [
        ex("¿Cuántas partes tiene el análisis completo de la clase?", "Seis", "Obra, contexto, materialidad, lenguaje visual, propósito y valoración."),
        ex("Verdadero o falso: una obra antigua siempre es mejor que una reciente.", "Falso", "La edad no es un criterio visual."),
        ex("¿Qué debes hacer con un dato que falta?", "Escribir «pendiente»", "No se inventa."),
    ],
    task(
        "Elige UN par de obras de ejemplo para comparar. A) Vasija pulida y rojiza con bandas de líneas incisas, de uso doméstico, y mural con figuras amarillas sobre fondo azul oscuro y letras grandes. B) Manta con rombos rojos y cafés en filas, usada como abrigo, y vasija con bandas incisas. Escribe un análisis de las seis partes para UNA de las obras y una tabla de cuatro criterios que compare las dos. Haz un boceto que reinterprete un recurso de una de ellas, con tus propias formas y la fuente citada.",
        "Elegí el par A. Análisis de la vasija: Es una vasija de ejemplo. Contexto: uso doméstico. Materialidad: greda pulida. Lenguaje visual: rojiza con bandas de líneas oscuras. Propósito: pendiente. Valoración: lograda porque las bandas repetidas dan ritmo. Tabla comparativa. Boceto: bandas propias en un vaso, recurso tomado de la vasija de ejemplo.",
        ["escribe las seis partes en orden", "compara con los mismos cuatro criterios", "valora con una razón visual", "reinterpreta un recurso y cita la fuente"],
        ["análisis escrito", "tabla comparativa", "boceto con fuente citada"],
        ["decidir por la edad de la obra", "copiar motivos como si fueran propios"],
        "Señala una frase con evidencia visual y pregunta qué recurso tomó para su boceto.",
    ),
    "Lee en voz alta tu valoración a una persona de tu casa y pregúntale si puede comprobar tu razón mirando la obra descrita.",
    "Reescribe tu valoración para un lector que no vio la obra, sumando un detalle más preciso.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA4, 5,
    "Tu análisis de la clase anterior, hojas y lápiz. Si no lo tienes, usa el de ejemplo escrito en esta clase.",
    "Aprenderé a contrastar el propósito de una manifestación con su efecto hoy, a comparar obras patrimoniales y contemporáneas y a revisar mi análisis con ayuda de otra persona. Sirve para mejorar mi análisis con evidencia.",
    ["Sé escribir un análisis de seis partes.", "Sé separar descripción, interpretación y valoración."],
    [
        "El propósito expresivo es lo que la obra quería lograr cuando se hizo; el efecto es lo que produce hoy en quien la mira. Pueden cambiar. Una vasija hecha para guardar agua, ahora en una vitrina, se mira por su decoración y su historia, no por su uso. El contexto cambió, y con él, la manera de verla. Por eso distingo el propósito original del efecto actual y no mezclo ambos.",
        "Comparar una obra patrimonial con una contemporánea con la misma tabla muestra semejanzas y diferencias. Ambas pueden repetir formas para crear ritmo; una puede nacer para el uso diario y la otra para la calle. Valoro cada una según su propósito y sus criterios, no por cuál es más antigua. Decir «lo antiguo siempre vale más» o «lo reciente siempre es mejor» no es un análisis.",
        "Para revisar mi análisis pido a otra persona que marque cada frase como evidencia visual, opinión o dato que falta. Las opiniones sin evidencia las mejoro agregando un detalle visible. Si de diez frases siete tienen evidencia, reviso las tres restantes. Concluyo solo lo que mis datos permiten: si cinco personas entendieron mi análisis, hablo de esas cinco, no de todo el curso.",
    ],
    [("propósito original", "lo que la obra quería lograr cuando se hizo"), ("efecto actual", "lo que la obra produce hoy en quien la mira"), ("semejanza", "algo que dos obras tienen en común"), ("diferencia", "algo que distingue a una obra de otra"), ("revisión", "lectura crítica de un texto para mejorarlo")],
    [
        w("Propósito y efecto", "Un tejido se hizo para abrigar del frío y hoy se muestra en una sala de exposiciones, donde se mira por sus colores. ¿Qué cambió?", ["El propósito original fue abrigar.", "El efecto actual es de contemplación.", "El contexto pasó de la casa a la sala."], "Cambió el contexto y con él la forma de mirarlo, de abrigo a contemplación"),
        w("Mejorar con evidencia", "Una frase dice: «El mural es genial». Agrégale evidencia visual.", ["No dice qué se ve.", "Agrego los colores y el fondo.", "Agrego el efecto."], "«Las figuras amarillas contrastan con el fondo azul oscuro, lo que llama la atención»"),
    ],
    [
        m("Mezclar el propósito original con el efecto que la obra produce hoy.", "El contexto cambia y con él la manera de verla.", "Anota por separado el propósito original y el efecto actual."),
        m("Concluir que un análisis sirve para todo el curso porque lo entendieron cinco personas.", "Cinco personas no representan a todos.", "Habla solo de las personas consultadas."),
    ],
    [
        ex("¿Cuál frase es opinión sin evidencia? A. «Los rombos se repiten en filas» B. «Es la mejor manta».", "B", "No señala nada que se vea."),
        ex("Una vasija pasa de la cocina a un museo. ¿Qué cambió: el contexto o el material?", "El contexto", "Cambió el lugar y el modo de mirarla."),
        ex("Otra persona lee tu análisis y marca qué frase no tiene evidencia. ¿Para qué sirve?", "Para revisar y mejorar el análisis", "Te muestra qué frases reforzar."),
    ],
    [
        ex("El mural invita a cuidar la plaza. Una persona que lo mira dice «me dan ganas de limpiarla». ¿Coinciden propósito y efecto?", "Sí", "La reacción coincide con la invitación."),
        ex("La vasija se hizo para guardar agua; hoy se mira por su decoración. ¿Qué cambió entre propósito original y efecto actual? A. La forma de mirarla, de uso a contemplación B. El material.", "A", "El material sigue igual; cambió el contexto."),
        ex("Vasija: bandas de líneas repetidas. Mural: letras repetidas en una franja. ¿Qué semejanza tienen? A. Ambas usan repetición B. Ambas son de greda.", "A", "Repiten elementos; el mural no está hecho de greda."),
    ],
    [
        arith("Comparas 3 obras con 4 criterios en una tabla. ¿Cuántas celdas llenas?", "3*4", "Se multiplica el número de obras por el de criterios."),
        arith("Una persona revisó tus 10 frases y marcó 7 con evidencia visual. ¿Cuántas debes mejorar?", "10-7", "Se restan las que ya tienen evidencia."),
        ex("Cambia «La manta es perfecta» para que tenga evidencia. A. «Los rombos rojos y cafés se repiten en filas parejas, lo que da sensación de orden» B. «La manta es perfecta y única».", "A", "Nombra qué se ve y su efecto."),
    ],
    [
        ex("Un análisis dice que el mural «cumple su propósito» sin dar evidencia. ¿Qué agregarías?", "Una evidencia visual, como letras grandes que se leen desde lejos", "Muestra por qué cumple su propósito."),
        ex("Dos compañeros valoran la manta y el mural. Uno dice «la manta vale más porque es antigua». La otra dice que cumplen propósitos distintos y los valora con razones. ¿Quién respeta el método de la clase?", "La segunda", "Valora con criterios y no por la edad."),
    ],
    [
        ex("Alguien dice «lo antiguo siempre vale más que lo reciente». ¿Qué principio del método lo contradice?", "Se valora con criterios y evidencia, no solo por la edad", "La edad no es un criterio de análisis visual."),
        ex("Cinco personas leen tu análisis y cuatro dicen entender el propósito. ¿Qué conclusión es válida? A. Para cuatro de esas cinco personas el análisis comunica el propósito B. El análisis comunica el propósito a todo el curso.", "A", "Solo se puede hablar de las personas consultadas."),
    ],
    ex("Expondrás en tu curso la comparación entre la manta y el mural. ¿Qué haces para que no suene a opinión? A. Mostrar la tabla con datos de cada criterio y una valoración con razón B. Decir cuál te gusta más.", "A", "Los datos y la razón respaldan el análisis."),
    [
        ex("¿Qué diferencia hay entre propósito original y efecto actual?", "El propósito es lo que se quiso lograr y el efecto es lo que produce hoy", "Pueden cambiar con el contexto."),
        ex("Verdadero o falso: se puede valorar una obra solo por su edad.", "Falso", "Se valora con criterios y evidencia."),
        ex("¿Qué haces con una opinión sin evidencia en tu análisis?", "Le agrego un detalle visible", "Así se puede comprobar."),
    ],
    task(
        "Usa tu análisis de la clase anterior. Si no lo tienes, usa este de ejemplo sobre un mural de figuras amarillas sobre fondo azul oscuro y letras grandes: «Es una obra genial y se nota que es la mejor del barrio. Fue pintada en un muro exterior con pintura de exteriores. Tiene colores vivos». Pide a otra persona que marque cada frase como evidencia visual, opinión o dato que falta. Mejora las frases de opinión, escribe propósito original y efecto actual por separado y haz una tabla que compare la obra con una patrimonial de ejemplo.",
        "Frase 1: opinión sin evidencia; la mejoro: «Las figuras amarillas contrastan con el azul oscuro y llaman la atención». Frase 2: dato de contexto y materialidad. Frase 3: evidencia, pero vaga; agrego «amarillo y azul». Propósito original: invitar a cuidar la plaza. Efecto actual: según dos personas, da ganas de limpiarla. Tabla con la vasija de ejemplo.",
        ["marca cada frase como evidencia, opinión o dato que falta", "mejora las opiniones con detalles visibles", "separa propósito original y efecto actual", "compara con una obra patrimonial con los mismos criterios"],
        ["análisis marcado", "frases mejoradas", "tabla comparativa"],
        ["valorar por la edad de la obra", "concluir para más gente de la consultada"],
        "Pregunta cuál frase mejoró más y qué detalle visible agregó.",
    ),
    "Lee dos frases de tu análisis a una persona de tu casa y pídele que diga cuál de las dos se puede comprobar mirando la obra.",
    "Escribe una comparación de cuatro frases entre una obra patrimonial y una contemporánea, usando la misma tabla.",
)
