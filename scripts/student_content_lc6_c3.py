"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS02 (describir oralmente aspectos socioculturales y espirituales de distintos pueblos indígenas en Chile y de otras
culturas, en diálogos, conversaciones o exposiciones, con vocabulario pertinente) y OA LS03 (comprender textos orales y
escritos de otras culturas, interpretando elementos significativos y vinculándolos con la propia experiencia, con
vocabulario pertinente).

Criterio de autoría: los únicos datos reales sobre pueblos son generales y muy atestiguados: el nombre de la lengua de
cada pueblo (mapuzugun, aymara, rapa nui, kawésqar) y la macrozona donde vive. Todas las comunidades, talleres, personas,
relatos y culturas que aparecen con prácticas concretas son inventados para practicar y están rotulados como tales; no
describen lo que hace ningún pueblo real. No se describen ceremonias ni creencias de pueblos reales. Las únicas
expresiones en lengua indígena son mari mari y chaltumay. Cada tarea abierta remite al educador/a tradicional.
"""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_lc6_c import L, M, T, W

LS2 = "LC06 OA LS02"
LS3 = "LC06 OA LS03"

DG = "Datos generales (reales y muy conocidos): el pueblo mapuche habla mapuzugun y vive sobre todo en el centro y sur de Chile. El pueblo aymara habla aymara y vive en el altiplano del norte de Chile. El pueblo rapa nui habla rapa nui y vive en la Isla de Pascua, en el océano Pacífico. El pueblo kawésqar habla kawésqar y vive en los canales de la Patagonia austral."

# ============================================================ LS02 clase 1 · situar la exposición
L(
    LS2, 1,
    materials="Lápiz y hoja. Los datos están escritos aquí. No necesitas ningún dispositivo.",
    use="Aprenderé a preparar una exposición oral sobre un pueblo indígena situándola: de qué pueblo hablo, dónde vive, cuál es su lengua y quién es mi fuente. Sirve para describir sin mezclar pueblos ni generalizar.",
    prior=["Sé que cada pueblo tiene su lengua y su territorio.", "Sé que toda información necesita una fuente y un permiso."],
    explain=[
        "Describir oralmente es contar en voz alta cómo es algo. Cuando hablo de aspectos socioculturales de un pueblo, cuento cómo las personas viven y se organizan juntas: su lengua, su territorio, sus fiestas abiertas, sus oficios. Los aspectos espirituales se refieren a sus creencias. Lo espiritual lo explican quienes lo guardan; yo solo digo lo que se autorizó contar.",
        "Antes de exponer ubico mi tema con una ficha: pueblo, lugar donde vive, lengua, fuente y permiso. Los datos generales, como que el pueblo mapuche habla mapuzugun y vive sobre todo en el centro y sur de Chile, son conocidos. Para cualquier otro dato, como lo que hace una comunidad determinada, necesito una fuente concreta y su permiso.",
        "La exposición también se prepara con vocabulario pertinente: palabras que corresponden al tema, como pueblo, territorio, comunidad y lengua. Si uso una palabra en lengua indígena, solo uso las que me entregó una fuente. Y al hablar nombro siempre el pueblo exacto: digo «en esta comunidad» y no «los indígenas», porque los pueblos son distintos entre sí.",
    ],
    vocab=[("describir", "contar cómo es algo"), ("aspecto sociocultural", "forma en que las personas viven y se organizan en conjunto"), ("aspecto espiritual", "lo relacionado con las creencias de un pueblo"), ("exposición", "presentación oral de un tema ante otras personas"), ("pertinente", "que corresponde al tema")],
    worked=[
        W("Completar la ficha con datos generales", DG + " Completa: pueblo aymara; lengua ___; zona ___.", ["Busco el pueblo aymara en los datos.", "Su lengua es el aymara.", "Vive en el altiplano del norte de Chile."], "lengua: aymara; zona: altiplano del norte de Chile"),
        W("Detectar un dato sin fuente", "Un estudiante dice: «Los kawésqar celebran todos los años una fiesta en el mes de mayo». ¿Está en los datos generales?", ["Reviso los datos generales.", "Solo dicen lengua y zona del pueblo kawésqar.", "La fiesta no aparece, así que necesita fuente y permiso."], "no: no está en los datos generales y necesita una fuente"),
    ],
    mistakes=[
        M("Decir «los indígenas hacen todos lo mismo».", "Los pueblos son distintos entre sí.", "Nombro el pueblo exacto y la comunidad."),
        M("Contar una fiesta de una comunidad sin tener fuente.", "No puedo asegurar que sea verdad ni que la comunidad lo autorice.", "Anoto el dato como «por preguntar» y no lo digo."),
    ],
    R=[
        ex(DG + " ¿Qué lengua habla el pueblo rapa nui?", "rapa nui", "Los datos generales lo dicen."),
        ex(DG + " ¿Dónde vive el pueblo rapa nui?", "en la Isla de Pascua", "Los datos generales lo dicen."),
        ex(DG + " ¿Qué lengua habla el pueblo mapuche?", "mapuzugun", "Los datos generales lo dicen."),
    ],
    C=[
        ex(DG + " ¿En qué zona de Chile vive el pueblo aymara?", "en el altiplano del norte", "Los datos generales lo dicen."),
        ex(DG + " ¿Dónde vive el pueblo kawésqar?", "en los canales de la Patagonia austral", "Los datos generales lo dicen."),
        ex("Verdadero o falso: los aspectos espirituales de un pueblo los puede explicar cualquier persona que haya leído sobre ellos.", "Falso", "Lo espiritual lo explican quienes lo guardan."),
    ],
    A=[
        ex(DG + " Une cada pueblo con su lengua. Pueblos: A) mapuche, B) aymara, C) kawésqar, D) rapa nui. Lenguas: 1) aymara, 2) rapa nui, 3) mapuzugun, 4) kawésqar. Escribe los cuatro pares.", "A-3, B-1, C-4, D-2", "Cada lengua lleva el nombre de su pueblo, salvo el mapuzugun, que es la del pueblo mapuche."),
        ex("Ordena para preparar una exposición. A) anoto mi fuente y su permiso. B) elijo el pueblo del que voy a hablar. C) completo los datos generales. D) pienso qué vocabulario necesito. Escribe las letras en orden.", "B, C, A, D", "Primero el tema, luego los datos, la fuente y el vocabulario."),
        arith(DG + " Los datos generales nombran 4 pueblos. Un compañero preparó fichas de 3 pueblos. ¿Cuántos pueblos le faltan?", "4-3", "Se restan los preparados del total."),
    ],
    Z=[
        ex("Una niña va a exponer sobre un pueblo y no tiene ninguna fuente para contar sus fiestas. ¿Qué puede decir con seguridad: lengua y zona de los datos generales o los detalles de las fiestas?", "lengua y zona de los datos generales", "Es lo único que tiene respaldo."),
        ex("Un niño dice: «Todos los pueblos indígenas de Chile viven en el sur». ¿Es correcto según los datos generales? Sí o No.", "No", "El pueblo aymara vive en el norte y el rapa nui en una isla."),
    ],
    D=[
        ex(DG + " Un compañero dice: «El mapuzugun se habla en el altiplano del norte». ¿Qué dato general lo contradice?", "que el pueblo mapuche vive sobre todo en el centro y sur", "El altiplano del norte es la zona del pueblo aymara."),
        ex("Quieres incluir una palabra en lengua indígena en tu exposición, pero no sabes si se escribe así. ¿La incluyes o la consultas con el educador o la educadora tradicional?", "la consultas con el educador o la educadora tradicional", "Solo quien conoce la lengua puede confirmarla."),
    ],
    context=[ex("Tu curso hará una exposición sobre pueblos indígenas en Chile y tu grupo tiene un libro sin fecha y sin autor. ¿Lo usas como fuente de datos o buscas una fuente identificada, como un educador tradicional?", "buscas una fuente identificada, como un educador tradicional", "Una fuente debe poder identificarse.")],
    selfcheck=[
        ex("¿Qué palabra describe lo que se refiere a las creencias de un pueblo: espiritual o comercial?", "espiritual", "Es la definición vista."),
        ex("¿Debo decir «los indígenas» o nombrar el pueblo exacto?", "nombrar el pueblo exacto", "Los pueblos son distintos entre sí."),
        ex("¿Una exposición necesita fuente para los datos que no son generales? Sí o No.", "Sí", "Sin fuente no se puede asegurar un dato."),
    ],
    task=T(
        "Usa los datos generales de esta clase y esta ficha inventada: «Comunidad Muestra (inventada), pueblo aymara. Fuente: un educador tradicional que visitó la escuela. Permiso: puede contarse en la sala. Dato de la fuente: en su comunidad hay una reunión cada mes.» En tu cuaderno completa una ficha para una exposición con estas líneas: pueblo, zona donde vive, lengua, comunidad, fuente, permiso y un dato de la fuente. Luego escribe en voz alta o por escrito dos oraciones de apertura de la exposición, que ubiquen el pueblo y mencionen la fuente.",
        "Pueblo: aymara. Zona: altiplano del norte de Chile. Lengua: aymara. Comunidad: Comunidad Muestra (inventada). Fuente: un educador tradicional. Permiso: sí, en la sala. Dato: tienen una reunión cada mes. Apertura: «Hoy hablaré del pueblo aymara, que vive en el altiplano del norte de Chile y habla aymara. Según un educador tradicional, en la Comunidad Muestra hay una reunión cada mes.»",
        ["completa las siete líneas de la ficha", "ubica pueblo, zona y lengua", "nombra la fuente", "no generaliza"],
        ["ficha de siete líneas", "dos oraciones de apertura"],
        ["generalizar a todo el pueblo", "no nombrar la fuente"],
        "Si generaliza, pídele que agregue «en la Comunidad Muestra» y «según».",
    ),
    reinforce="Copia los datos generales en una tabla de tres columnas: pueblo, lengua y zona.",
    extend="Prepara una ficha inventada para otro pueblo de los datos generales, sin agregar prácticas, y márcala como inventada.",
)

# ============================================================ LS02 clase 2 · escuchar una exposición y tomar notas
EXP = "Exposición oral (inventada para practicar; la lee una persona adulta en voz alta): «Hoy hablaré del pueblo mapuche, que habla mapuzugun y vive sobre todo en el centro y sur de Chile. Según una educadora tradicional de la Escuela Ejemplo, en su comunidad hay un taller de lengua los miércoles y cada reunión comienza con un saludo, «mari mari». Ella cree que el taller ayuda a que las niñas y los niños se sientan parte de su comunidad. Aclara que habla solo por su comunidad. Yo pienso que los talleres son una buena forma de aprender.»"

L(
    LS2, 2,
    materials="Lápiz y hoja. La exposición está escrita aquí; puede leerla en voz alta una persona adulta mientras tomas notas.",
    use="Aprenderé a escuchar una exposición y a tomar notas que separan los datos generales, los datos de la fuente, las opiniones y el límite. Sirve para entender sin mezclar ni cambiar lo que dijo quien expuso.",
    prior=["Sé situar una exposición con pueblo, zona, lengua, fuente y permiso.", "Sé que «según» atribuye lo dicho a su fuente."],
    explain=[
        "Escuchar una exposición es una tarea activa. Tomo notas en cuatro columnas: datos generales, datos de la fuente, opiniones y límites. Los datos generales son los conocidos, como la lengua y la zona del pueblo. Los datos de la fuente son los que cuenta una persona de una comunidad. Las opiniones son lo que alguien cree. Los límites avisan hasta dónde vale lo dicho.",
        "En la exposición de la clase, «habla mapuzugun» y «vive sobre todo en el centro y sur de Chile» son datos generales. «Hay un taller de lengua los miércoles» y «cada reunión comienza con un saludo» son datos de la fuente. «Ella cree que el taller ayuda…» es una opinión de la fuente, y «yo pienso que…» es opinión de quien expone. «Habla solo por su comunidad» es un límite.",
        "Las notas deben copiar lo que se dijo, sin agregar. Si no entiendo una palabra, la anoto con un signo de pregunta. Si la palabra es de una lengua indígena, no la adivino ni la escribo a mi manera: la consulto al educador o a la educadora tradicional. Luego uso mis notas para resumir lo que escuché con la palabra «según».",
    ],
    vocab=[("tomar notas", "anotar lo importante mientras se escucha"), ("dato de la fuente", "dato que cuenta una persona de la comunidad"), ("dato general", "dato muy conocido sobre un pueblo"), ("opinión", "lo que alguien cree o piensa"), ("límite", "aviso de hasta dónde vale lo dicho")],
    worked=[
        W("Clasificar una frase", EXP + " ¿«Hay un taller de lengua los miércoles» es dato general, dato de la fuente u opinión?", ["Es algo que cuenta la educadora sobre su comunidad.", "No es un dato conocido de todo el pueblo.", "Entonces es un dato de la fuente."], "dato de la fuente"),
        W("Encontrar el límite", EXP + " ¿Qué límite declara la educadora?", ["Busco la frase que avisa hasta dónde vale su relato.", "Dice que habla solo por su comunidad.", "Ese es el límite."], "habla solo por su comunidad"),
    ],
    mistakes=[
        M("Anotar «todos los mapuche hacen un taller los miércoles».", "El taller es de una comunidad, según la fuente.", "Anoto «en la comunidad de la educadora hay un taller los miércoles»."),
        M("Anotar la opinión de quien expone como si fuera dato de la fuente.", "«Yo pienso» es de quien expone, no de la educadora.", "Anoto cada opinión con el nombre de quien la dice."),
    ],
    R=[
        ex(EXP + " ¿Qué día es el taller de lengua?", "los miércoles", "La exposición lo dice."),
        ex(EXP + " ¿Con qué saludo comienza cada reunión?", "mari mari", "La exposición lo dice."),
        ex(EXP + " ¿Qué lengua habla el pueblo mapuche según la exposición?", "mapuzugun", "La exposición lo dice."),
    ],
    C=[
        ex(EXP + " ¿«Vive sobre todo en el centro y sur de Chile» es dato general o dato de la fuente?", "dato general", "Es un dato conocido del pueblo."),
        ex(EXP + " ¿«Ella cree que el taller ayuda a que las niñas y los niños se sientan parte» es hecho u opinión de la educadora?", "opinión de la educadora", "La exposición usa «cree»."),
        ex(EXP + " ¿Quién dice «yo pienso que los talleres son una buena forma de aprender»: la educadora o quien expone?", "quien expone", "La frase final es de quien expone."),
    ],
    A=[
        ex(EXP + " Clasifica cada frase como G (dato general), F (dato de la fuente), O (opinión) o L (límite). 1) Habla mapuzugun. 2) Cada reunión comienza con un saludo. 3) Habla solo por su comunidad. 4) Cree que el taller ayuda. Escribe las cuatro letras.", "1 G, 2 F, 3 L, 4 O", "Cada frase corresponde a una de las cuatro columnas."),
        arith(EXP + " Supón que la comunidad hace el taller una vez por semana y que cada taller dura 2 horas. ¿Cuántas horas de taller hay en 6 semanas?", "2*6", "Dos horas por semana durante seis semanas."),
        ex(EXP + " Ordena las notas de la más general a la más específica. A) habla solo por su comunidad. B) el pueblo mapuche habla mapuzugun. C) en su comunidad hay un taller los miércoles. Escribe las letras en orden.", "B, C, A", "Primero el dato general, luego el de la fuente y al final el límite."),
    ],
    Z=[
        ex(EXP + " Un compañero anota: «El taller de lengua es en todas las comunidades mapuche». ¿Respeta el límite? Sí o No.", "No", "La educadora habla solo por su comunidad."),
        ex(EXP + " Una niña no entiende cómo se escribe una palabra en lengua. ¿Qué anota: la palabra a su manera o un signo de pregunta para consultar?", "un signo de pregunta para consultar", "No se adivina la escritura de una palabra en lengua."),
    ],
    D=[
        ex(EXP + " Elige el mejor resumen. A) «Según una educadora tradicional de la Escuela Ejemplo, en su comunidad hay un taller de lengua los miércoles; ella habla solo por su comunidad». B) «Los mapuche hacen un taller de lengua los miércoles». Escribe la letra.", "A", "Atribuye la información y mantiene el límite."),
        arith("Tomaste 12 notas en una exposición. 3 son datos generales, 5 son datos de la fuente y 2 son opiniones. El resto son límites. ¿Cuántas notas son límites?", "12-3-5-2", "Se restan las otras notas del total."),
    ],
    context=[ex("Un familiar te cuenta cómo funciona su club de lectura en lengua indígena. Mientras escuchas, ¿anotas todo mezclado o lo separas en datos, opiniones y límites?", "lo separas en datos, opiniones y límites", "Separar ayuda a no cambiar lo que dijo.")],
    selfcheck=[
        ex("¿Cuántas columnas tienen las notas de esta clase?", "4", "Datos generales, datos de la fuente, opiniones y límites."),
        ex("Una palabra en lengua que no entiendo, ¿se adivina o se consulta?", "se consulta", "Se pregunta al educador o educadora tradicional."),
        ex("¿«Cree que» introduce un hecho o una opinión?", "una opinión", "Muestra lo que alguien piensa."),
    ],
    task=T(
        "Una persona adulta te lee esta exposición inventada: «Hoy hablaré del pueblo aymara, que habla aymara y vive en el altiplano del norte de Chile. Según un educador tradicional de la Comunidad Muestra, su comunidad tiene un taller de tejido los sábados. Él cree que el taller ayuda a que los jóvenes valoren su historia. Aclara que habla solo por su comunidad.» En tu cuaderno haz una tabla de cuatro columnas (datos generales, datos de la fuente, opiniones, límites) y anota en cada una lo que corresponda. Después escribe un resumen de dos oraciones que empiece con «Según…».",
        "Generales: habla aymara; vive en el altiplano del norte. Fuente: la Comunidad Muestra tiene un taller de tejido los sábados. Opinión: el taller ayuda a que los jóvenes valoren su historia. Límite: habla solo por su comunidad. Resumen: «Según un educador tradicional de la Comunidad Muestra, su comunidad tiene un taller de tejido los sábados. Él habla solo por su comunidad.»",
        ["completa las cuatro columnas", "no mezcla datos con opiniones", "escribe un resumen con «según»", "respeta el límite"],
        ["tabla de cuatro columnas", "resumen de dos oraciones"],
        ["poner la opinión en la columna de datos", "borrar el límite"],
        "Si mezcla datos, pídele que subraye los verbos como «cree» y «aclara» y vea a qué columna llevan.",
    ),
    reinforce="Relee la exposición de la clase y subraya con cuatro colores lo que va en cada columna.",
    extend="Escribe tu propia exposición inventada de cinco oraciones que contenga un dato general, un dato de la fuente, una opinión y un límite.",
)

# ============================================================ LS02 clase 3 · relacionar aspectos socioculturales y espirituales
FIC = "Ficha de la Comunidad Ejemplo (inventada para practicar; no describe a ningún pueblo real): 1) Se reúne cada mes en la sede para conversar sus asuntos. 2) Tiene un taller de cestería los viernes. 3) Tiene una fiesta abierta cada año, a la que invita a las familias de la escuela. 4) Sus mayores guardan relatos que solo cuentan a las personas de la comunidad. 5) Su lengua se escucha en un programa de radio semanal."

L(
    LS2, 3,
    materials="Lápiz y hoja. La ficha está escrita aquí y es inventada para practicar.",
    use="Aprenderé a distinguir aspectos socioculturales y espirituales de una comunidad y a relacionarlos entre sí y con la lengua, sin explicar lo que la comunidad guarda. Sirve para describir de manera completa y respetuosa.",
    prior=["Sé tomar notas separando datos, opiniones y límites.", "Sé que lo espiritual lo explican quienes lo guardan."],
    explain=[
        "Los aspectos socioculturales son las formas en que las personas de una comunidad viven y se organizan: sus reuniones, sus talleres, sus fiestas abiertas, sus oficios y su lengua. Los aspectos espirituales son las creencias y los sentidos que la comunidad da a su vida y al mundo. Ambos se relacionan: una fiesta puede ser sociocultural y tener, además, un sentido espiritual.",
        "En la ficha de la Comunidad Ejemplo hay cosas que puedo describir: una reunión mensual, un taller de cestería y una fiesta abierta. También hay algo que la comunidad guarda: sus mayores cuentan ciertos relatos solo a su gente. Ese es un límite. Puedo decir que existen relatos guardados, pero no su contenido ni su significado.",
        "Relacionar es ver cómo se conectan los aspectos. La lengua en la radio y la reunión en la sede ayudan a que las personas se encuentren. El taller de cestería puede transmitir oficios y también historias. Cuando relaciono, uso verbos prudentes como «puede» y «según la ficha», y no invento conexiones que la fuente no dio.",
    ],
    vocab=[("sociocultural", "relacionado con la vida en comunidad y la cultura"), ("espiritual", "relacionado con las creencias de un pueblo"), ("oficio", "trabajo que se aprende y se transmite, como la cestería"), ("fiesta abierta", "fiesta a la que se puede invitar a personas de fuera"), ("guardar", "mantener algo reservado")],
    worked=[
        W("Clasificar un aspecto", FIC + " ¿La frase 2 es un aspecto sociocultural o espiritual?", ["La frase 2 habla de un taller de cestería los viernes.", "Un taller de oficio es parte de la vida de la comunidad.", "Es un aspecto sociocultural."], "sociocultural"),
        W("Respetar lo guardado", FIC + " ¿Puedo describir el contenido de los relatos de los mayores?", ["La frase 4 dice que los relatos se cuentan solo a la gente de la comunidad.", "Eso es un límite.", "Puedo decir que existen, no lo que cuentan."], "no: puedo decir que existen relatos guardados, pero no su contenido"),
    ],
    mistakes=[
        M("Explicar el significado de lo que los mayores guardan.", "No lo sé y la comunidad lo guarda.", "Digo que hay relatos guardados y respeto el límite."),
        M("Decir que la fiesta abierta es igual en todas las comunidades.", "La ficha describe una sola comunidad.", "Digo «en la Comunidad Ejemplo»."),
    ],
    R=[
        ex(FIC + " ¿Cada cuánto se reúne la comunidad en la sede?", "cada mes", "La frase 1 lo dice."),
        ex(FIC + " ¿Qué día es el taller de cestería?", "los viernes", "La frase 2 lo dice."),
        ex(FIC + " ¿A quiénes invita la fiesta abierta?", "a las familias de la escuela", "La frase 3 lo dice."),
    ],
    C=[
        ex(FIC + " ¿Qué frase habla de algo que la comunidad guarda: la 1 o la 4?", "la 4", "La 4 habla de relatos reservados."),
        ex(FIC + " ¿Qué pasa con la lengua en la frase 5?", "se escucha en un programa de radio semanal", "La ficha lo dice."),
        ex("Verdadero o falso: un aspecto sociocultural puede tener también un sentido espiritual.", "Verdadero", "Ambos aspectos pueden relacionarse."),
    ],
    A=[
        ex(FIC + " Clasifica cada frase como S (sociocultural que puedo describir) o G (guardado, solo lo puedo mencionar). 1) La reunión mensual. 2) Los relatos que cuentan solo a la comunidad. 3) El taller de cestería. 4) La radio semanal. Escribe las cuatro letras.", "1 S, 2 G, 3 S, 4 S", "Solo los relatos de los mayores se guardan."),
        arith(FIC + " La comunidad tiene 5 aspectos en la ficha y 1 de ellos se guarda. ¿Cuántos aspectos se pueden describir?", "5-1", "Se resta el aspecto guardado del total."),
        ex(FIC + " Une cada aspecto con la forma en que se relaciona con la lengua. 1) la radio. 2) el taller de cestería. Opciones: A) puede transmitir oficios y también historias. B) la lengua se escucha cada semana. Escribe los dos pares.", "1-B, 2-A", "La radio hace escuchar la lengua cada semana y el taller puede transmitir oficios e historias."),
    ],
    Z=[
        ex(FIC + " Un niño dice: «Los relatos guardados hablan del origen del mundo». ¿Puede afirmarlo? Sí o No.", "No", "No sabe qué cuentan; la comunidad los guarda."),
        ex(FIC + " Una niña dice: «La fiesta abierta ayuda a que la escuela y la comunidad se conozcan». ¿Es una relación que la ficha permite proponer con «puede»? Sí o No.", "Sí", "La ficha dice que se invita a las familias de la escuela."),
    ],
    D=[
        ex(FIC + " Elige la mejor descripción. A) «Según la ficha, la Comunidad Ejemplo se reúne cada mes, tiene un taller de cestería y guarda ciertos relatos que cuenta solo a su gente». B) «Esa comunidad hace rituales secretos». Escribe la letra.", "A", "Describe lo que la ficha dice y respeta lo guardado."),
        ex("Una compañera quiere contar en su exposición un relato guardado que le pasó un conocido. ¿Debe contarlo o consultar antes a la comunidad?", "consultar antes a la comunidad", "Lo que una comunidad guarda se cuenta solo con su autorización."),
    ],
    context=[ex("En una visita, una vecina te cuenta una historia y agrega: «esto es solo para nuestra gente». Al preparar tu exposición, ¿la incluyes o dices que existen historias que la comunidad guarda?", "dices que existen historias que la comunidad guarda", "Respetas lo reservado sin revelarlo.")],
    selfcheck=[
        ex("¿Qué aspecto se refiere a las creencias de un pueblo: espiritual o sociocultural?", "espiritual", "Es la definición vista."),
        ex("¿Puedo describir un relato que la comunidad guarda? Sí o No.", "No", "Solo puedo decir que existe."),
        ex("¿Qué verbo prudente uso al relacionar: «puede» o «seguro»?", "puede", "Evita afirmar más de lo que dice la fuente."),
    ],
    task=T(
        "Lee esta ficha inventada de la Comunidad Muestra: «1) Tiene una reunión cada dos meses. 2) Tiene un taller de tejido los sábados. 3) Sus mayores guardan un canto que solo se canta dentro de la comunidad. 4) Tiene un cartel de bienvenida en su lengua.» En tu cuaderno haz una tabla de dos columnas: «puedo describir» y «solo puedo mencionar que existe». Clasifica las cuatro frases. Luego escribe dos oraciones que relacionen un aspecto sociocultural con la lengua, usando «puede» o «según la ficha».",
        "Puedo describir: 1, 2 y 4. Solo mencionar: 3, que existe un canto guardado. Relación: «Según la ficha, el cartel de bienvenida en la lengua puede hacer visible la lengua. El taller de tejido puede ser un espacio donde se escucha y se usa.»",
        ["clasifica las cuatro frases correctamente", "no describe el canto guardado", "relaciona con prudencia", "no inventa información"],
        ["tabla de dos columnas", "dos oraciones"],
        ["describir el canto guardado", "afirmar relaciones que la ficha no da"],
        "Si describió el canto, pídele que relea la frase 3 y la mueva a la segunda columna.",
    ),
    reinforce="Copia la ficha de la Comunidad Ejemplo y marca con un color las frases que puedes describir.",
    extend="Escribe una ficha inventada de cinco frases con un aspecto guardado y dos aspectos socioculturales, y márcala como inventada.",
)

# ============================================================ LS02 clase 4 · guion atribuido de exposición
GL = "Glosario de la exposición (palabras del tema): pueblo, territorio, comunidad, lengua, taller, saludo, «mari mari» (saludo en mapuzugun que entregó la educadora tradicional)."
FG = "Ficha de la fuente (inventada para practicar): Fuente: una educadora tradicional de la Escuela Ejemplo, pueblo mapuche. Permiso: puede contarse en la sala. Dijo: en su comunidad hay un taller de lengua los miércoles; cada reunión comienza con «mari mari»; el taller ayuda a que niñas y niños se sientan parte de su comunidad. Aclaró: habla solo por su comunidad."

L(
    LS2, 4,
    materials="Lápiz y hoja. El glosario y la ficha de la fuente están escritos aquí y son inventados para practicar.",
    use="Aprenderé a escribir y decir un guion breve de exposición de cinco oraciones que atribuye la información, usa vocabulario pertinente y declara un límite. Sirve para exponer en voz alta sin inventar ni generalizar.",
    prior=["Sé separar datos generales, datos de la fuente, opiniones y límites.", "Sé que los aspectos guardados no se explican."],
    explain=[
        "Un guion de exposición breve tiene cinco partes: saludo, presentación del pueblo con sus datos generales, dato de la fuente con «según», importancia dicha por la fuente y límite. Un guion ordenado me ayuda a no perderme cuando hablo en voz alta y a no inventar mientras improviso.",
        "El vocabulario pertinente son las palabras que corresponden al tema: pueblo, territorio, comunidad, lengua, taller, saludo. Las uso con su significado y, cuando es necesario, las explico en una frase corta. Una palabra en lengua indígena, como «mari mari», la uso solo si una fuente me la entregó, y la digo como me la enseñaron.",
        "Al exponer miro a mi público, hablo con calma y no leo todo de corrido. Marco mi opinión con «yo pienso» para que se note qué es mío. Y cuando termino, pregunto al público si hay dudas; si una pregunta no la puedo responder con la ficha, digo «no lo sé; lo consultaré con la educadora tradicional», en vez de inventar.",
    ],
    vocab=[("guion", "plan escrito de lo que se va a decir"), ("vocabulario pertinente", "palabras que corresponden al tema"), ("público", "personas que escuchan una exposición"), ("improvisar", "decir algo sin haberlo preparado"), ("presentación", "parte donde se da a conocer el tema")],
    worked=[
        W("Escribir la oración del dato", FG + " Escribe una oración con «según» sobre el taller.", ["Tomo el dato: hay un taller de lengua los miércoles.", "Nombro la fuente y la comunidad.", "Escribo la oración."], "Según una educadora tradicional de la Escuela Ejemplo, en su comunidad hay un taller de lengua los miércoles."),
        W("Cerrar con el límite", FG + " Escribe la oración final de la exposición.", ["Busco lo que la fuente aclaró.", "Aclaró que habla solo por su comunidad.", "Cierro con ese límite."], "La educadora aclaró que habla solo por su comunidad."),
    ],
    mistakes=[
        M("Inventar una respuesta cuando el público pregunta algo que la ficha no dice.", "Se pierde la confianza y se puede decir algo falso.", "Digo «no lo sé; lo consultaré» y lo anoto."),
        M("Leer el guion sin mirar al público ni explicar las palabras nuevas.", "Nadie entiende el vocabulario.", "Explico las palabras clave en una frase corta."),
    ],
    R=[
        ex(FG + " ¿Qué día es el taller de lengua?", "los miércoles", "La ficha lo dice."),
        ex(FG + " ¿Qué dijo la educadora que hace cada reunión?", "comienza con «mari mari»", "La ficha lo dice."),
        ex(GL + " ¿«Mari mari» es un saludo en mapuzugun?", "sí", "El glosario lo dice."),
    ],
    C=[
        ex(FG + " ¿Qué aclaró la educadora al final?", "que habla solo por su comunidad", "Es su límite."),
        ex("Un guion de exposición breve de esta clase, ¿cuántas partes tiene?", "5", "Saludo, pueblo, dato con según, importancia y límite."),
        ex("Verdadero o falso: si el público pregunta algo que la ficha no dice, conviene inventar una respuesta.", "Falso", "Se dice que no se sabe y se consulta."),
    ],
    A=[
        ex("Ordena las partes del guion. A) límite. B) dato de la fuente con «según». C) saludo. D) importancia dicha por la fuente. E) presentación del pueblo. Escribe las letras en orden.", "C, E, B, D, A", "Se saluda, se presenta el pueblo, se cuenta el dato, se dice su importancia y se cierra con el límite."),
        ex(FG + " Elige la mejor oración de importancia. A) «Según la educadora, el taller ayuda a que niñas y niños se sientan parte de su comunidad». B) «El taller es la mejor forma de unir a los pueblos». Escribe la letra.", "A", "La A usa lo que dijo la fuente."),
        arith("Un guion debe tener 5 oraciones. Un grupo escribió 2 y escribirá otras 2 mañana. ¿Cuántas oraciones le faltarán todavía?", "5-2-2", "Se restan las escritas y las que escribirá del total."),
    ],
    Z=[
        ex(FG + " Una compañera agrega a su guion: «y la educadora dijo que todos los jóvenes participan». ¿Está en la ficha? Sí o No.", "No", "La ficha no dice cuántos jóvenes participan."),
        ex(FG + " Si quieres dar tu opinión, ¿cómo la marcas: con «yo pienso» o escribiéndola como si fuera de la educadora?", "con «yo pienso»", "Se distingue lo propio de lo que dijo la fuente."),
    ],
    D=[
        ex(GL + " Un compañero cambia a su gusto cómo se dice y se escribe «mari mari». ¿Qué debe hacer?", "decirlo y escribirlo como se lo enseñó la educadora", "Una palabra en lengua se usa como la entregó la fuente."),
        ex("Una niña olvida un dato en mitad de la exposición. ¿Qué es mejor: inventar uno parecido o decir que lo revisará en su ficha?", "decir que lo revisará en su ficha", "Es mejor ser honesta que inventar."),
    ],
    context=[ex("Presentas tu guion en la sala y alguien pregunta si lo que cuentas pasa en todas las comunidades. ¿Respondes que sí o que tu fuente habla solo por su comunidad?", "que tu fuente habla solo por su comunidad", "Respetas el límite declarado.")],
    selfcheck=[
        ex("¿Con qué palabra introduzco lo dicho por la fuente: «según» o «seguro»?", "según", "La palabra según atribuye lo dicho."),
        ex("¿Se puede improvisar un dato cultural que no está en la ficha? Sí o No.", "No", "Se consulta antes."),
        ex("¿Qué palabra de la ficha usa la educadora para saludar?", "mari mari", "Está en la ficha."),
    ],
    task=T(
        "Lee esta ficha inventada: «Fuente: un educador tradicional de la Escuela Muestra, pueblo aymara. Permiso: puede contarse en la sala. Dijo: en su comunidad hay un taller de tejido los sábados; el taller ayuda a que los jóvenes conozcan su historia. Aclaró: habla solo por su comunidad.» En tu cuaderno escribe un guion de cinco oraciones (saludo, presentación del pueblo con sus datos generales, dato de la fuente con «según», importancia dicha por la fuente y límite). Usa al menos tres palabras del glosario de la clase y no agregues palabras en lengua indígena.",
        "Buenos días a todos. Hoy hablaré del pueblo aymara, que habla aymara y vive en el altiplano del norte de Chile. Según un educador tradicional de la Escuela Muestra, en su comunidad hay un taller de tejido los sábados. Él dice que el taller ayuda a que los jóvenes conozcan su historia. Aclaró que habla solo por su comunidad.",
        ["tiene las cinco partes", "usa tres palabras del glosario", "atribuye con «según»", "declara el límite y no agrega datos"],
        ["guion de cinco oraciones"],
        ["omitir el límite", "agregar palabras en lengua inventadas"],
        "Si falta una parte, pídele que rotule cada oración con el número de su parte.",
    ),
    reinforce="Copia el guion del ejemplo de la clase y numera las cinco partes.",
    extend="Ensaya tu guion en voz alta ante una persona de tu casa y anota dos mejoras que te sugiera.",
)

# ============================================================ LS02 clase 5 · contrastar dos comunidades y una cultura de otro país
CA = "Comunidad A (inventada para practicar), pueblo mapuche: reunión mensual en la sede; taller de lengua los miércoles; programa de radio los sábados."
CB = "Comunidad B (inventada), pueblo aymara: reunión cada dos meses en la sede; taller de tejido los viernes; programa de radio los domingos."
CC = "Cultura Ejemplo (inventada, de un país imaginario): feria de oficios el primer domingo del mes; taller de cerámica los jueves; programa de radio los lunes."

L(
    LS2, 5,
    materials="Lápiz y hoja. Las tres fichas están escritas aquí y son inventadas para practicar; no describen a ningún pueblo ni cultura reales.",
    use="Aprenderé a comparar a oral y por escrito dos comunidades de pueblos distintos y una cultura de otro país con los mismos criterios, diciendo qué se parece y qué cambia sin decir que una sea mejor. Sirve para valorar la diversidad.",
    prior=["Sé armar un guion de exposición atribuido.", "Sé que jerarquizar es decir que una cultura vale más que otra."],
    explain=[
        "Compararlas es mirar con los mismos criterios. Para las tres fichas puedo usar: cada cuánto se reúnen o juntan, qué taller o actividad de oficio tienen y cómo usan la radio. Respondo cada criterio para cada ficha, escribo qué se parece y qué cambia y no pongo una por encima de otra.",
        "En esta clase las fichas incluyen dos pueblos de Chile y una cultura de otro país, que es una forma de mirar «otras culturas significativas para su contexto». Las tres son inventadas y no puedo usar sus datos para describir a pueblos reales. Lo que sí practico es el método: criterios iguales, datos de la ficha y lenguaje respetuoso.",
        "Jerarquizar sería decir «la comunidad con más reuniones es más organizada» o «la cultura con feria es más moderna». Esas frases dicen más de lo que muestran los datos y ponen unas personas sobre otras. En cambio puedo decir: «A se reúne cada mes y B cada dos meses». Eso es un dato comparable.",
    ],
    vocab=[("criterio", "aspecto que se usa para comparar"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas cambian"), ("jerarquizar", "decir que algo vale más que otra cosa"), ("dato comparable", "dato que se puede poner junto a otro con el mismo criterio")],
    worked=[
        W("Comparar con un criterio", CA + " " + CB + " Compara cada cuánto se reúnen A y B.", ["A se reúne cada mes.", "B se reúne cada dos meses.", "Es una diferencia."], "A cada mes y B cada dos meses"),
        W("Reconocer una jerarquización", "Alguien dice: «La comunidad A es más organizada porque se reúne más». ¿Compara o jerarquiza?", ["La frase dice que A es más organizada.", "Se reúne más es un dato, pero «más organizada» es un juicio.", "Pone una comunidad sobre otra."], "jerarquiza"),
    ],
    mistakes=[
        M("Escribir «la cultura con feria es más moderna».", "Es un juicio que no sale de los datos.", "Describo: «Cultura Ejemplo tiene una feria de oficios cada mes»."),
        M("Usar los datos de las fichas para describir a pueblos reales.", "Son fichas inventadas.", "Aclaro que son inventadas y uso el método, no los datos."),
    ],
    R=[
        ex(CA + " ¿Cada cuánto se reúne la comunidad A?", "cada mes", "La ficha lo dice."),
        ex(CB + " ¿Qué día es el taller de tejido de la comunidad B?", "los viernes", "La ficha lo dice."),
        ex(CC + " ¿Qué taller tiene Cultura Ejemplo?", "de cerámica", "La ficha lo dice."),
    ],
    C=[
        ex(CA + " " + CB + " " + CC + " ¿Qué día emite la radio de la comunidad B?", "los domingos", "La ficha de B lo dice."),
        ex(CA + " " + CC + " ¿Qué ficha tiene feria de oficios: la A o la Cultura Ejemplo?", "la Cultura Ejemplo", "La ficha de C lo dice."),
        ex("Verdadero o falso: se puede decir «la comunidad B es peor porque se reúne menos veces».", "Falso", "Es una jerarquización sin razón."),
    ],
    A=[
        ex(CA + " " + CB + " " + CC + " Completa con A, B o C: el taller de lengua es de la comunidad ___; el taller de tejido es de la comunidad ___; el taller de cerámica es de la ficha ___. Escribe las tres letras en orden.", "A, B, C", "Cada taller aparece en una ficha distinta."),
        arith(CA + " " + CB + " Si la comunidad A se reúne una vez al mes y la B una vez cada dos meses, ¿cuántas reuniones hacen juntas en 4 meses?", "4+4//2", "A hace 4 reuniones y B hace 2 en cuatro meses."),
        ex("Clasifica cada frase como C (compara) o J (jerarquiza). 1) «La A se reúne cada mes y la B cada dos meses». 2) «La C es más moderna». 3) «Las tres tienen un programa de radio». Escribe las tres letras.", "1 C, 2 J, 3 C", "La frase 2 pone una ficha sobre otra."),
    ],
    Z=[
        ex(CA + " " + CB + " " + CC + " ¿Cuál de estas actividades aparece en las tres fichas: una reunión mensual, un programa de radio o una feria de oficios?", "un programa de radio", "Las tres mencionan un programa de radio; la reunión y la feria no están en todas."),
        ex(CA + " " + CB + " Una compañera concluye: «Entonces los pueblos mapuche se reúnen más que los aymara». ¿Los datos permiten esa conclusión? Sí o No.", "No", "Son fichas de dos comunidades inventadas, no de pueblos enteros."),
    ],
    D=[
        ex(CA + " " + CB + " " + CC + " Elige la mejor frase de cierre. A) «Las tres fichas tienen un programa de radio; cambian el día de la radio y el taller que ofrecen». B) «La ficha C es la mejor porque tiene feria». Escribe la letra.", "A", "Dice una semejanza y una diferencia con datos."),
        ex("Quieres comparar una comunidad real que visitaste con la comunidad A de la ficha. ¿Puedes usar los datos de la ficha para hablar de la comunidad real? Sí o No.", "No", "La ficha es inventada y no describe a la comunidad real."),
    ],
    context=[ex("En una jornada escolar, dos compañeros discuten qué comunidad es «más tradicional». ¿Qué les propones: que cuenten qué hace cada comunidad con los mismos criterios, o que voten cuál es más tradicional?", "que cuenten qué hace cada comunidad con los mismos criterios", "Comparar con criterios evita jerarquizar.")],
    selfcheck=[
        ex("¿Qué se usa para comparar: los mismos criterios o criterios distintos para cada ficha?", "los mismos criterios", "Así la comparación es justa."),
        ex("¿«Más moderna» compara o jerarquiza?", "jerarquiza", "Pone una por encima de otra."),
        ex("¿Las fichas de esta clase describen pueblos reales? Sí o No.", "No", "Todas son fichas inventadas."),
    ],
    task=T(
        "Usa estas fichas inventadas. Comunidad X, pueblo rapa nui: reunión cada tres meses; taller de canto los martes; letrero de bienvenida en su lengua. Comunidad Y, pueblo kawésqar: reunión cada mes; taller de memoria oral los jueves; letrero de bienvenida en su lengua. En tu cuaderno haz una tabla con estas filas: cada cuánto se reúne, taller y letrero. Luego escribe una frase de cierre con una semejanza y una diferencia, sin jerarquizar, y aclara que las fichas son inventadas.",
        "Reunión: cada tres meses / cada mes. Taller: canto los martes / memoria oral los jueves. Letrero: sí / sí. Cierre: «Las dos fichas inventadas tienen letrero de bienvenida en su lengua; X se reúne cada tres meses e Y cada mes.»",
        ["completa las tres filas para ambas comunidades", "usa los mismos criterios", "escribe una semejanza y una diferencia", "aclara que las fichas son inventadas y no jerarquiza"],
        ["tabla de comparación", "frase de cierre"],
        ["decir que una comunidad es mejor", "olvidar aclarar que son inventadas"],
        "Si jerarquiza, pídele que cambie la palabra por un dato de la tabla.",
    ),
    reinforce="Copia las tres fichas en una tabla y subraya con un color lo que se repite en las tres.",
    extend="Agrega una cuarta ficha inventada de una cultura de otro país y compárala con las tres de la clase usando los mismos criterios.",
)

# ============================================================ LS02 clase 6 · conversar y exponer con validación
DI = "Diálogo modelo (inventado para practicar): — Ana: Mari mari. Hoy quiero contarles lo que nos dijo una educadora tradicional de la Escuela Ejemplo. — Bruno: Mari mari, Ana. ¿De qué pueblo habla ella? — Ana: Del pueblo mapuche, que habla mapuzugun. Según ella, en su comunidad hay un taller de lengua los miércoles. — Bruno: ¿Eso pasa en todas las comunidades? — Ana: No lo sé; ella aclaró que habla solo por su comunidad. Lo preguntaré. — Bruno: Gracias, Ana. Chaltumay."

L(
    LS2, 6,
    materials="Lápiz y hoja. El diálogo modelo está escrito aquí y es inventado para practicar. Se puede leer entre dos personas.",
    use="Aprenderé a conversar y exponer con turnos claros, con vocabulario pertinente y con respeto, y a pedir validación al educador o a la educadora tradicional antes de presentar. Sirve para comunicar lo que aprendí sin hablar en nombre de un pueblo.",
    prior=["Sé armar un guion atribuido.", "Sé comparar sin jerarquizar."],
    explain=[
        "Un diálogo es una conversación con turnos: cada persona habla, escucha y responde. En un buen diálogo sobre culturas se saluda, se atribuye lo dicho con «según», se hacen preguntas con respeto y se reconocen los límites. En el diálogo modelo, Ana atribuye su información y, cuando Bruno pregunta si ocurre en todas las comunidades, responde que no lo sabe y que lo preguntará.",
        "Una exposición es más larga y la hace una sola persona ante el público. También usa saludo, datos atribuidos y cierre. Tanto en diálogos como en exposiciones uso vocabulario pertinente, como pueblo, comunidad, lengua, taller y fuente, y las expresiones en lengua indígena que una fuente me entregó, por ejemplo «mari mari» y «chaltumay».",
        "Validar es mostrar mi diálogo o mi exposición al educador o a la educadora tradicional antes de presentarla. Esa persona puede confirmar si respeté lo que enseñó o pedir cambios. Si algo se debe cambiar, lo cambio. Así evito hablar en nombre de un pueblo y cuido a las personas que me enseñaron.",
    ],
    vocab=[("diálogo", "conversación en la que las personas se turnan para hablar"), ("turno", "momento en que le toca hablar a una persona"), ("validar", "mostrar un trabajo a quien conoce el tema para confirmar que lo respeta"), ("público", "personas que escuchan"), ("respeto", "trato cuidadoso hacia las personas y sus saberes")],
    worked=[
        W("Identificar la atribución", DI + " ¿Cómo atribuye Ana lo que cuenta?", ["Busco una expresión como «según».", "Ana dice: «Según ella, en su comunidad hay un taller de lengua los miércoles».", "Esa es la atribución."], "con «según ella», nombrando a la educadora tradicional"),
        W("Reconocer una respuesta honesta", DI + " ¿Qué hace Ana cuando no sabe si ocurre en todas las comunidades?", ["Lee la respuesta de Ana.", "Dice que no lo sabe y que lo preguntará.", "No inventa."], "dice que no lo sabe y que lo preguntará"),
    ],
    mistakes=[
        M("Responder «sí, pasa en todas» para no quedar sin respuesta.", "Es inventar un dato.", "Digo «no lo sé; lo preguntaré»."),
        M("Hablar sin turnos e interrumpir.", "No se escucha a la otra persona.", "Espero mi turno y respondo a lo que dijo."),
    ],
    R=[
        ex(DI + " ¿Quién saluda primero en el diálogo?", "Ana", "Ana comienza con «Mari mari»."),
        ex(DI + " ¿De qué pueblo habla Ana?", "del pueblo mapuche", "Ana lo dice."),
        ex(DI + " ¿Qué dice Bruno al final?", "Gracias, Ana. Chaltumay", "Bruno agradece al final."),
    ],
    C=[
        ex(DI + " ¿Qué le pregunta Bruno a Ana sobre las comunidades?", "si eso pasa en todas las comunidades", "Es su segunda intervención."),
        ex(DI + " ¿Qué respuesta da Ana a esa pregunta?", "que no lo sabe y que lo preguntará", "Reconoce el límite."),
        ex("Validar, ¿es mostrar el trabajo a quien conoce el tema o presentar sin avisar?", "mostrar el trabajo a quien conoce el tema", "Así se definió en la clase."),
    ],
    A=[
        ex(DI + " Ordena los turnos de Ana y Bruno. A) Ana responde que no sabe. B) Bruno pregunta si pasa en todas las comunidades. C) Ana saluda. D) Bruno agradece. Escribe las letras en orden.", "C, B, A, D", "Se saluda, se pregunta, se responde y se agradece."),
        arith(DI + " El diálogo tiene 6 intervenciones. Ana habla 3 veces. ¿Cuántas veces habla Bruno?", "6-3", "Se restan las de Ana del total."),
        ex("Une cada expresión con su uso en el diálogo. 1) mari mari. 2) chaltumay. Usos: A) agradecer al terminar. B) saludar al comenzar. Escribe los dos pares.", "1-B, 2-A", "Mari mari saluda y chaltumay agradece."),
    ],
    Z=[
        ex(DI + " Bruno propone que Ana cuente cómo se hace una ceremonia que ella vio. ¿Debe contarla sin permiso? Sí o No.", "No", "Una ceremonia se cuenta solo con permiso de quienes la conducen."),
        ex(DI + " Otra persona del diálogo dice: «Ana, tú hablas por todo el pueblo mapuche». ¿Es correcto? Sí o No.", "No", "Ana solo cuenta lo que dijo su fuente."),
    ],
    D=[
        ex("Dos finales posibles para una exposición. A) «Esto vale solo para la comunidad de mi fuente; lo revisé con la educadora tradicional». B) «Así son todos los pueblos». Escribe cuál respeta mejor los límites.", "A", "Declara el alcance y la validación."),
        ex("Descubres, antes de presentar, que citaste mal una palabra en lengua. ¿Qué haces: la dejas porque casi nadie lo notará o la corriges con ayuda del educador tradicional?", "la corriges con ayuda del educador tradicional", "La validación sirve para corregir a tiempo."),
    ],
    context=[ex("Tu grupo ensayó una exposición sobre una comunidad y quiere presentarla mañana. Falta mostrarla al educador tradicional. ¿Presentan igual o esperan a validarla?", "esperan a validarla", "Antes de presentar se pide la validación.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es un turno en un diálogo?", "el momento en que le toca hablar a una persona", "Así se definió."),
        ex("Si no sé algo que me preguntan, ¿invento o digo que lo consultaré?", "digo que lo consultaré", "Es lo honesto."),
        ex("¿Valido mi trabajo antes o después de presentarlo?", "antes", "Así se corrigen errores a tiempo."),
    ],
    task=T(
        "Lee esta ficha inventada: «Fuente: una educadora tradicional de la Escuela Muestra, pueblo rapa nui. Permiso: puede contarse en la sala. Dijo: en su comunidad se hace una feria de canto en la escuela. Aclaró: habla solo por su comunidad.» Escribe en tu cuaderno un diálogo de cuatro intervenciones entre dos estudiantes, donde uno atribuye lo que dijo la educadora con «según», el otro pregunta si pasa en todas las comunidades y el primero responde con honestidad. Usa «iorana» para saludar y «maururu» para agradecer; en esta tarea la educadora ya los autorizó. Después escribe una línea que diga a quién mostrarás el diálogo antes de presentarlo.",
        "A: Iorana. Según una educadora tradicional de la Escuela Muestra, en su comunidad se hace una feria de canto en la escuela. B: ¿Eso pasa en todas las comunidades? A: No lo sé; ella aclaró que habla solo por su comunidad. B: Maururu, A. Validación: lo mostraré a la educadora tradicional antes de presentarlo.",
        ["tiene cuatro intervenciones", "atribuye con «según»", "responde con honestidad al límite", "dice a quién mostrará el diálogo"],
        ["diálogo de cuatro intervenciones", "línea de validación"],
        ["inventar una respuesta", "olvidar la validación"],
        "Si inventa, pídele que relea la ficha y busque el límite que aclaró la educadora.",
    ),
    reinforce="Lee en voz alta el diálogo modelo con otra persona, turnándose los papeles.",
    extend="Escribe un diálogo de cinco intervenciones sobre la ficha de la Comunidad A de la clase 5, con un saludo y una pregunta respetuosa.",
)


# ============================================================ LS03 clase 1 · situar un texto de otra cultura
TX1 = "Cuento 1 (inventado para practicar; Lluvia Ejemplo es un pueblo ficticio): En Lluvia Ejemplo, cada niña y cada niño recibe a los ocho años un canasto vacío. Durante un año llena su canasto con objetos pequeños que encuentra y le gustan: una piedra lisa, una pluma caída, una semilla. Al terminar el año comparte con su familia la historia de cada objeto. La abuela dice que el canasto lleno enseña a mirar con atención el lugar donde se vive. El pueblo no cuenta a los visitantes qué objetos guardan los mayores en sus canastos."
FT1 = "Ficha del texto (inventada): Cultura: Lluvia Ejemplo (ficticia). Tipo de texto: cuento escrito. Autoría: una profesora de la escuela, que lo escribió para practicar. Permiso: sí, es un texto inventado. Forma de comunicarlo: se puede leer en voz alta (texto oral) o en silencio (texto escrito)."

L(
    LS3, 1,
    materials="Lápiz y hoja. El cuento y la ficha están escritos aquí y son inventados para practicar. Puede leerlos en voz alta una persona adulta.",
    use="Aprenderé a situar un texto oral o escrito de otra cultura: quién lo cuenta, de qué cultura es, de qué tipo es y con qué permiso circula. Sirve para comprender textos ajenos sin mezclarlos ni atribuirlos a otros pueblos.",
    prior=["Sé que cada pueblo tiene su historia y su forma de entender el mundo.", "Sé que la información necesita fuente y permiso."],
    explain=[
        "Los textos de otras culturas pueden ser orales, como un relato que se escucha, o escritos, como un cuento en un libro. Para comprenderlos primero los sitúo con una ficha: ¿de qué cultura es?, ¿qué tipo de texto es?, ¿quién lo cuenta o lo escribió? y ¿tengo permiso para usarlo? Esa ficha me protege de atribuir a un pueblo algo que no dijo.",
        "También miro la forma en que me llega. Un texto oral lo escucho de una persona que me lo cuenta; un texto escrito lo leo en una hoja. Cuando el texto es de un pueblo real, es posible que quien me lo cuente me pida guardar ciertas partes. Esa petición es parte del texto y debe respetarse. Aquí practicamos con un cuento inventado, de una cultura ficticia.",
        "Situar no es interpretar todavía. Es reunir los datos básicos: cultura, tipo de texto, autoría y permiso. Con ellos puedo decir «en este cuento inventado de Lluvia Ejemplo» y no «en las culturas indígenas». Y si falta un dato, lo anoto como «por preguntar» antes de seguir.",
    ],
    vocab=[("texto oral", "texto que se cuenta o se dice en voz alta"), ("texto escrito", "texto que se lee en una hoja o pantalla"), ("autoría", "quién creó o escribió un texto"), ("ficha del texto", "datos básicos de un texto"), ("cuento", "relato breve que cuenta una historia")],
    worked=[
        W("Completar la ficha", FT1 + " ¿Qué tipo de texto es el cuento 1 y quién lo escribió?", ["Busco «Tipo de texto»: cuento escrito.", "Busco «Autoría»: una profesora de la escuela.", "Junto los dos datos."], "es un cuento escrito, escrito por una profesora de la escuela"),
        W("Reconocer la forma", FT1 + " ¿Se puede comunicar el cuento como texto oral?", ["La ficha dice que se puede leer en voz alta.", "Un texto leído en voz alta es oral.", "Sí se puede."], "sí, leyéndolo en voz alta"),
    ],
    mistakes=[
        M("Decir «las culturas indígenas dan canastos a los niños».", "Es un cuento inventado de una cultura ficticia.", "Digo «en el cuento inventado de Lluvia Ejemplo»."),
        M("Usar un texto sin saber quién lo escribió.", "No puedo atribuirlo ni pedir permiso.", "Anoto la autoría o lo dejo «por preguntar»."),
    ],
    R=[
        ex(FT1 + " ¿Qué tipo de texto es el cuento 1?", "un cuento escrito", "La ficha lo dice."),
        ex(FT1 + " ¿De qué cultura es el cuento?", "de Lluvia Ejemplo, una cultura ficticia", "La ficha lo dice."),
        ex("Un texto oral, ¿se cuenta en voz alta o se lee solo en silencio?", "se cuenta en voz alta", "Eso significa oral."),
    ],
    C=[
        ex(TX1 + " ¿A qué edad recibe un canasto cada niña y cada niño?", "a los ocho años", "El cuento lo dice."),
        ex(TX1 + " ¿Cuánto tiempo llena su canasto?", "un año", "El cuento lo dice."),
        ex(FT1 + " Verdadero o falso: el cuento 1 describe un pueblo real de Chile.", "Falso", "La ficha dice que la cultura es ficticia."),
    ],
    A=[
        ex(FT1 + " Ordena para situar un texto. A) averiguo si tengo permiso. B) anoto la cultura. C) anoto quién lo escribió. D) anoto el tipo de texto. Escribe las letras en orden.", "B, D, C, A", "Primero la cultura, luego el tipo, la autoría y el permiso."),
        arith(TX1 + " Si en un curso hay 24 niñas y niños que ya recibieron su canasto, y 6 más lo reciben este año, ¿cuántos canastos hay entregados?", "24+6", "Se suman los que ya recibieron y los nuevos."),
        ex(TX1 + " ¿Cuántos objetos se nombran como ejemplo en el cuento: una piedra, una pluma y una semilla?", "3", "Son tres objetos.", "1+1+1"),
    ],
    Z=[
        ex(TX1 + " Un niño dice: «Todos los pueblos le dan un canasto a los niños». ¿Está bien? Sí o No.", "No", "El cuento es de una sola cultura ficticia."),
        ex(FT1 + " Si una persona te cuenta un texto de su comunidad y no sabes si autoriza difundirlo, ¿lo cuentas igual o consultas antes?", "consultas antes", "Se necesita permiso para difundir."),
    ],
    D=[
        ex(TX1 + " Elige la mejor introducción para contar el cuento. A) «En el cuento inventado de Lluvia Ejemplo, cada niño recibe un canasto vacío». B) «Así hacen los pueblos originarios». Escribe la letra.", "A", "Dice de dónde viene y no generaliza."),
        ex(TX1 + " ¿Puede una persona contar qué objetos guardan los mayores en sus canastos? Responde según el cuento.", "no, el pueblo no lo cuenta a los visitantes", "El cuento lo declara como límite."),
    ],
    context=[ex("Un familiar te cuenta un cuento que aprendió de su comunidad. Quieres leerlo en tu curso. ¿Qué haces primero: preguntarle si lo autoriza y cómo se llama quien lo cuenta, o leerlo sin avisar?", "preguntarle si lo autoriza y cómo se llama quien lo cuenta", "Un texto se comparte con permiso y atribuyendo.")],
    selfcheck=[
        ex("En Lengua y Cultura de los Pueblos Originarios: ¿qué es la autoría de un texto?", "quién lo creó o escribió", "Así se definió."),
        ex("¿Un cuento leído en voz alta es texto oral? Sí o No.", "Sí", "Se comunica en voz alta."),
        ex("Si me falta un dato de la ficha, ¿sigo o lo anoto «por preguntar»?", "lo anoto «por preguntar»", "Se pregunta antes de seguir."),
    ],
    task=T(
        "Lee este cuento inventado: «En Orilla Ejemplo, una cultura ficticia, cuando alguien cumple diez años, le entregan una cuerda con un nudo. Cada año agrega un nudo y cuenta qué aprendió ese año. Una persona mayor dice que la cuerda ayuda a recordar. Los visitantes no preguntan por la cuerda de los mayores.» En tu cuaderno completa una ficha del texto con cultura, tipo de texto (cuento escrito), autoría (una profesora que lo escribió para practicar), permiso y forma de comunicarlo. Luego escribe una oración que presente el cuento sin generalizar.",
        "Cultura: Orilla Ejemplo (ficticia). Tipo: cuento escrito. Autoría: una profesora, para practicar. Permiso: sí, es inventado. Forma: se puede leer en voz alta o en silencio. Presentación: «En el cuento inventado de Orilla Ejemplo, cada año se agrega un nudo a una cuerda.»",
        ["completa las cinco líneas", "identifica que es inventado", "presenta sin generalizar", "no inventa datos"],
        ["ficha completa", "una oración de presentación"],
        ["generalizar a todas las culturas", "olvidar el permiso"],
        "Si generaliza, pídele que agregue «en el cuento inventado de» al comienzo de su oración.",
    ),
    reinforce="Relee el cuento de Lluvia Ejemplo y subraya con un color los datos de la ficha que aparecen en el texto.",
    extend="Escribe una ficha inventada para un cuento oral ficticio que se contaría en voz alta, con las cinco líneas.",
)

# ============================================================ LS03 clase 2 · comprender con límites
TX2 = "Cuento 2 (inventado para practicar): En Isla Ejemplo, una cultura ficticia, una familia abre cada mañana la ventana que mira al este y dice una frase de saludo al día. Los niños aprenden la frase escuchando. Cuando alguien de la casa viaja, la familia le entrega un cordón con tres nudos. Cada nudo recuerda a una persona de la casa. Quien regresa devuelve el cordón y cuenta su viaje. La frase de saludo no se enseña a quienes no son de la isla."

L(
    LS3, 2,
    materials="Lápiz y hoja. El cuento está escrito aquí y es inventado para practicar. Puede leerlo una persona adulta.",
    use="Aprenderé a comprender qué dice un texto de otra cultura, a separar lo que dice de lo que imagino y a respetar los límites que el propio texto declara. Sirve para no inventar sentidos que el texto no entrega.",
    prior=["Sé situar un texto con su ficha.", "Sé que los límites declarados se respetan."],
    explain=[
        "Comprender un texto empieza por lo que dice de manera directa: quiénes son los personajes, qué hacen, dónde y cuándo. A eso se llama comprensión literal. En el cuento 2, la familia abre una ventana al este, los niños aprenden una frase escuchando y el viajero recibe un cordón con tres nudos.",
        "Luego busco los límites que el texto declara. Este cuento termina con uno: la frase de saludo no se enseña a quienes no son de la isla. Yo no puedo inventar esa frase ni adivinar su sentido. Puedo decir que existe y que se enseña escuchando en la familia.",
        "Separar lo que el texto dice de lo que imagino me permite comprender con honestidad. Si pienso «tal vez los nudos significan días», eso es una idea mía y no del texto. El texto solo dice que cada nudo recuerda a una persona. Esa precisión es parte de comprender bien.",
    ],
    vocab=[("comprensión literal", "entender lo que el texto dice de manera directa"), ("límite declarado", "aviso del texto de lo que no se cuenta"), ("cordón", "cuerda delgada"), ("nudo", "lazo apretado en una cuerda"), ("personaje", "persona o ser que aparece en un texto")],
    worked=[
        W("Responder con el texto", TX2 + " ¿Qué recuerda cada nudo del cordón?", ["Busco la parte del cordón.", "El texto dice que cada nudo recuerda a una persona de la casa.", "Respondo con esas palabras."], "a una persona de la casa"),
        W("Detectar una idea inventada", TX2 + " Alguien dice: «Cada nudo cuenta un día de viaje». ¿Lo dice el cuento?", ["Releo la parte del cordón.", "No dice nada sobre días de viaje.", "Es una idea inventada."], "no: es una idea inventada que el cuento no dice"),
    ],
    mistakes=[
        M("Escribir la frase de saludo de la isla como si la supiera.", "El cuento dice que no se enseña a quienes no son de la isla.", "Digo que existe una frase y que no se cuenta."),
        M("Agregar sentidos que el cuento no da, como que los nudos significan días.", "Es una invención.", "Uso solo lo que dice el texto."),
    ],
    R=[
        ex(TX2 + " ¿Hacia dónde mira la ventana que abre la familia?", "al este", "El cuento lo dice."),
        ex(TX2 + " ¿Cuántos nudos tiene el cordón?", "3", "El cuento lo dice.", "1+1+1"),
        ex(TX2 + " ¿Cómo aprenden la frase los niños?", "escuchando", "El cuento lo dice."),
    ],
    C=[
        ex(TX2 + " ¿Qué hace quien regresa de un viaje con el cordón?", "lo devuelve y cuenta su viaje", "El cuento lo dice."),
        ex(TX2 + " ¿Qué límite declara el cuento al final?", "que la frase de saludo no se enseña a quienes no son de la isla", "Es la última oración."),
        ex(TX2 + " Verdadero o falso: el cuento dice cuál es la frase de saludo.", "Falso", "Solo dice que existe."),
    ],
    A=[
        arith(TX2 + " Si tres personas viajan y cada una recibe un cordón con tres nudos, ¿cuántos nudos hay en total?", "3*3", "Tres cordones con tres nudos cada uno."),
        ex(TX2 + " Clasifica cada frase como T (dice el cuento) o I (idea mía). 1) La familia abre una ventana al este. 2) Tal vez los nudos significan lluvia. 3) Los niños aprenden la frase escuchando. Escribe las tres letras.", "1 T, 2 I, 3 T", "La frase 2 no está en el cuento."),
        ex(TX2 + " Ordena lo que ocurre. A) quien viaja recibe un cordón. B) la familia abre la ventana y saluda al día. C) quien regresa devuelve el cordón y cuenta su viaje. Escribe las letras en orden.", "B, A, C", "El cuento parte con el saludo diario y luego el viaje."),
    ],
    Z=[
        ex(TX2 + " Un niño propone escribir la frase de saludo de la isla en su cuaderno «inventada por él». ¿Respeta el límite del cuento? Sí o No.", "No", "El cuento dice que esa frase no se enseña ni se inventa."),
        ex(TX2 + " ¿Por qué no se puede decir que «el cordón sirve para mandar mensajes»? Porque ___.", "el cuento no dice eso", "No aparece en el texto."),
    ],
    D=[
        ex(TX2 + " Elige el mejor resumen. A) «En el cuento inventado de Isla Ejemplo, una familia saluda al día desde la ventana y entrega un cordón con tres nudos a quien viaja; la frase de saludo no se enseña a quienes no son de la isla». B) «Los habitantes de la isla usan cordones para predecir el clima». Escribe la letra.", "A", "Es la que se apoya en el texto."),
        ex("Si una persona de una comunidad real te cuenta un texto y te dice que ciertas partes se guardan, ¿al contarlo las incluyes o las dejas fuera?", "las dejas fuera", "Respetas el límite que te pidió."),
    ],
    context=[ex("Un abuelo te cuenta una historia familiar y te pide que no repitas un nombre. Al escribirla en la escuela, ¿pones el nombre o escribes «una persona de la familia»?", "escribes «una persona de la familia»", "Respetas lo que te pidió reservar.")],
    selfcheck=[
        ex("En Lengua y Cultura de los Pueblos Originarios: ¿qué es la comprensión literal?", "entender lo que el texto dice de manera directa", "Así se definió."),
        ex("Una idea que yo agrego pero el texto no dice, ¿es del texto o mía?", "mía", "No está en el texto."),
        ex("¿Debo inventar lo que un texto no cuenta? Sí o No.", "No", "Se respeta el límite."),
    ],
    task=T(
        "Lee este cuento inventado: «En Puerto Ejemplo, una cultura ficticia, cuando llega el primer día de verano, cada familia pinta con tiza blanca una línea frente a su puerta. Los niños saltan sobre las líneas de otras casas. Una persona mayor cuenta una historia breve en la plaza. La historia que cuenta cada año no se cuenta a visitantes.» En tu cuaderno escribe tres cosas: dos datos que el cuento dice, una idea que NO dice el cuento (una que alguien podría inventar) y el límite declarado.",
        "Datos: cada familia pinta con tiza blanca una línea frente a su puerta; los niños saltan sobre las líneas de otras casas. Idea que no dice: la línea sirve para alejar el calor. Límite: la historia que cuenta la persona mayor no se cuenta a visitantes.",
        ["escribe dos datos del cuento", "propone una idea que el cuento no dice", "nombra el límite", "no inventa un sentido"],
        ["tres respuestas escritas"],
        ["mezclar datos con ideas inventadas", "olvidar el límite"],
        "Si copia una idea inventada como dato, pídele que la subraye en el cuento y compruebe que no está.",
    ),
    reinforce="Relee el cuento 2 y subraya con un color lo que dice y con otro el límite.",
    extend="Escribe tres frases sobre un cuento tuyo imaginario: un dato, una idea que podrían inventar y un límite.",
)

# ============================================================ LS03 clase 3 · interpretar elementos significativos
L(
    LS3, 3,
    materials="Lápiz y hoja. Los dos cuentos están escritos en esta clase y son inventados para practicar.",
    use="Aprenderé a interpretar elementos significativos de un texto (objetos, acciones, lugares) usando solo lo que el texto dice y a vincularlos con mi propia experiencia sin afirmar que significan lo mismo en otra cultura. Sirve para comprender más profundamente sin inventar.",
    prior=["Sé comprender un texto de manera literal y respetar sus límites.", "Sé que cada texto pertenece a una cultura y a un contexto."],
    explain=[
        "Un elemento significativo es algo del texto que parece importante: un objeto, una acción repetida, un lugar. En el cuento de Lluvia Ejemplo, el canasto aparece desde el comienzo y se llena durante un año. Parece importante porque el cuento dice cuál es su sentido: según la abuela, enseña a mirar con atención el lugar donde se vive.",
        "Interpretar es explicar el sentido de ese elemento usando evidencia del texto. La evidencia es la frase del texto que apoya mi interpretación. Si digo «el canasto enseña atención», mi evidencia es la frase de la abuela. Si el texto no da la evidencia, mi idea es solo una posibilidad y la marco así, con «tal vez», o la dejo.",
        "Después puedo vincular el elemento con mi experiencia: ¿qué objeto o costumbre de mi vida enseña algo parecido? Por ejemplo, un cuaderno de observaciones también enseña a mirar con atención. Vincular no quiere decir que los dos elementos signifiquen lo mismo para sus culturas, sino que me ayudan a comprender. Y siempre nombro de qué texto o cultura hablo.",
    ],
    vocab=[("elemento significativo", "objeto, acción o lugar importante de un texto"), ("evidencia", "frase del texto que apoya una interpretación"), ("interpretar", "explicar el sentido de algo usando evidencia"), ("vincular", "relacionar con mi experiencia"), ("posibilidad", "idea que puede ser pero que el texto no confirma")],
    worked=[
        W("Interpretar con evidencia", TX1 + " ¿Qué enseña el canasto lleno según el cuento?", ["Busco la frase de la abuela.", "Dice que el canasto lleno enseña a mirar con atención el lugar donde se vive.", "Esa frase es la evidencia."], "enseña a mirar con atención el lugar donde se vive"),
        W("Vincular con mi experiencia", "Un niño compara el canasto con su cuaderno de observaciones, donde anota lo que ve en el patio. ¿Qué tienen en común?", ["El canasto recoge objetos que se encuentran en el lugar donde se vive.", "El cuaderno recoge observaciones del lugar donde se vive.", "Los dos ayudan a mirar con atención."], "ambos ayudan a mirar con atención el lugar donde se vive"),
    ],
    mistakes=[
        M("Interpretar «el cordón es mágico» sin una frase del texto.", "No hay evidencia.", "Uso solo lo que dice el texto o lo marco como posibilidad."),
        M("Decir que mi objeto significa lo mismo para otra cultura.", "El sentido pertenece a cada cultura.", "Digo que me ayuda a comprender y que no es lo mismo."),
    ],
    R=[
        ex(TX1 + " ¿Qué recibe un niño a los ocho años en el cuento 1?", "un canasto vacío", "El cuento lo dice."),
        ex(TX2 + " ¿Qué recibe quien viaja en el cuento 2?", "un cordón con tres nudos", "El cuento lo dice."),
        ex("Una evidencia, ¿es una frase del texto que apoya una interpretación o una idea que se me ocurre?", "una frase del texto que apoya una interpretación", "Así se definió."),
    ],
    C=[
        ex(TX1 + " ¿Qué dice la abuela que enseña el canasto lleno?", "a mirar con atención el lugar donde se vive", "Es su frase en el cuento."),
        ex(TX2 + " ¿Qué recuerda cada nudo en el cuento 2?", "a una persona de la casa", "El cuento lo dice."),
        ex("Verdadero o falso: puedo afirmar que el cordón significa lo mismo para todas las culturas.", "Falso", "El sentido pertenece al texto y a su cultura."),
    ],
    A=[
        ex(TX1 + " Une cada elemento con su sentido según el texto. 1) el canasto lleno. 2) compartir la historia de cada objeto con la familia. Sentidos: A) enseña a mirar con atención. B) permite que la familia conozca lo que el niño encontró. Escribe los dos pares.", "1-A, 2-B", "El texto da esos sentidos."),
        arith(TX2 + " Una familia entrega cordones de tres nudos a 4 viajeros. ¿Cuántas personas de la casa se recuerdan en total, contando un nudo por persona?", "4*3", "Cuatro cordones con tres nudos cada uno."),
        ex("Clasifica cada interpretación como E (con evidencia del texto) o P (solo posibilidad). 1) «El canasto enseña a mirar con atención», porque lo dice la abuela. 2) «El cordón tal vez sirve para medir el viaje». Escribe las dos letras.", "1 E, 2 P", "La primera tiene la frase de la abuela y la segunda no."),
    ],
    Z=[
        ex(TX1 + " Un compañero dice que el canasto representa la riqueza de la familia. ¿El texto da evidencia para eso? Sí o No.", "No", "El texto habla de atención, no de riqueza."),
        ex(TX2 + " ¿Puedes vincular los nudos con una pulsera de amistad, diciendo que ambos recuerdan a personas? Sí o No.", "Sí", "Es un vínculo con tu experiencia, sin afirmar que sean lo mismo."),
    ],
    D=[
        ex(TX1 + " Elige la mejor interpretación. A) «Según la abuela, el canasto lleno enseña a mirar con atención el lugar donde se vive». B) «El canasto sirve para esconder cosas». Escribe la letra.", "A", "Tiene evidencia en el texto."),
        ex("Quieres vincular el cordón de tres nudos con algo de tu vida y dices «es exactamente igual a mi pulsera». ¿Qué debes cambiar para respetar el texto?", "decir que se parecen en algo, no que son iguales", "Vincular no es igualar."),
    ],
    context=[ex("Imagina que alguien guarda en su casa una caja con objetos que le recuerdan lugares donde ha estado. ¿La relacionas con el canasto del cuento diciendo que se parecen en algo o que son iguales?", "diciendo que se parecen en algo", "Vincular es ver una semejanza, no igualar.")],
    selfcheck=[
        ex("Una interpretación con evidencia, ¿se apoya en una frase del texto o solo en lo que imagino?", "en una frase del texto", "Esa es la evidencia."),
        ex("¿Vincular con mi experiencia significa que sea igual? Sí o No.", "No", "Solo ayuda a comprender."),
        ex("Si el texto no da evidencia, ¿lo afirmo o lo marco como posibilidad?", "lo marco como posibilidad", "No se afirma sin evidencia."),
    ],
    task=T(
        "Lee este cuento inventado: «En Lomas Ejemplo, una cultura ficticia, cada familia cuida un árbol en el cerro. Cuando nace un niño, las personas atan una cinta amarilla a una rama. Una persona mayor dice que la cinta ayuda a recordar que el árbol y el niño crecen juntos. Los visitantes no tocan los árboles de los mayores.» En tu cuaderno escribe: un elemento significativo del cuento, su interpretación con una frase de evidencia, un vínculo con tu experiencia (diciendo qué se parece y qué cambia) y el límite que declara el texto.",
        "Elemento: la cinta amarilla en el árbol. Interpretación: «Según la persona mayor, ayuda a recordar que el árbol y el niño crecen juntos». Vínculo: en mi casa guardamos fotos de cuando era pequeño; se parece en recordar el crecimiento y cambia en que no es un árbol. Límite: los visitantes no tocan los árboles de los mayores.",
        ["nombra un elemento", "interpreta con evidencia", "vincula con semejanza y diferencia", "nombra el límite"],
        ["cuatro respuestas escritas"],
        ["interpretar sin evidencia", "decir que es igual a su experiencia"],
        "Si no hay evidencia, pídele que busque en el cuento la frase que apoya su idea.",
    ),
    reinforce="Relee el cuento 1 y subraya la frase de la abuela que da el sentido del canasto.",
    extend="Elige un objeto de tu casa y escribe qué sentido tiene para ti, con una frase de evidencia, y qué se parece al cuento 1.",
)

# ============================================================ LS03 clase 4 · interpretación atribuida
INT = "Interpretación modelo (inventada para practicar): «Según el cuento 2 de Isla Ejemplo, quien viaja recibe un cordón con tres nudos y cada nudo recuerda a una persona de la casa. Yo interpreto que el cordón ayuda a llevar a la familia en el viaje, porque el texto dice que cada nudo recuerda a una persona. Esto me hace pensar en cómo llevo una foto cuando salgo de casa. El cuento no explica la frase de saludo y yo no la invento.»"

L(
    LS3, 4,
    materials="Lápiz y hoja. La interpretación modelo está escrita aquí y es inventada para practicar.",
    use="Aprenderé a escribir una interpretación de cuatro oraciones sobre un texto de otra cultura, que cita lo que dice, interpreta con evidencia, la vincula con mi experiencia y declara el límite. Sirve para comprender de manera ordenada y honesta.",
    prior=["Sé interpretar un elemento con evidencia.", "Sé que «según» atribuye y «yo interpreto» marca lo mío."],
    explain=[
        "Una interpretación atribuida tiene cuatro partes. Primero cita lo que dice el texto, con «según». Segundo, dice mi interpretación con «yo interpreto». Tercero, da la evidencia con «porque». Cuarto, vincula con mi experiencia y declara el límite: lo que el texto no explica y yo no invento.",
        "En la interpretación modelo, la primera oración cita datos del cuento. La segunda dice qué interpreta quien escribe y da la evidencia con «porque», que es una frase del texto. La tercera vincula con su experiencia. La cuarta declara el límite: el cuento no explica la frase de saludo. Un buen texto interpretativo no pasa del texto a opiniones sin conexión.",
        "También uso vocabulario pertinente: cuento, cultura, elemento, evidencia, cordón, nudo. Cuando el texto es de una cultura real, antes de compartir mi interpretación se la muestro a una persona que conozca esa cultura, como el educador o la educadora tradicional, para ver si respeta lo que enseñó.",
    ],
    vocab=[("interpretación atribuida", "texto que dice lo que dice el texto y lo que interpreta quien escribe"), ("evidencia", "frase del texto que apoya la interpretación"), ("vínculo", "relación con mi propia experiencia"), ("límite", "lo que el texto no explica"), ("cita", "palabras tomadas de un texto")],
    worked=[
        W("Encontrar la evidencia", INT + " ¿Cuál es la evidencia de la interpretación?", ["Busco la palabra «porque».", "Dice que el texto dice que cada nudo recuerda a una persona.", "Esa es la evidencia."], "el texto dice que cada nudo recuerda a una persona"),
        W("Reconocer el vínculo", INT + " ¿Con qué experiencia propia la vincula quien escribe?", ["Busco una frase como «me hace pensar».", "Dice que lo relaciona con llevar una foto al salir de casa.", "Ese es el vínculo."], "con llevar una foto cuando sale de casa"),
    ],
    mistakes=[
        M("Interpretar sin citar ninguna frase del texto.", "No hay evidencia.", "Agrego «porque el texto dice…»."),
        M("Cerrar la interpretación explicando la frase de saludo que el cuento no cuenta.", "La inventaría.", "Cierro con «el cuento no explica la frase y yo no la invento»."),
    ],
    R=[
        ex(INT + " ¿Cuántos nudos tiene el cordón de la interpretación?", "3", "Lo dice la primera oración.", "1+1+1"),
        ex(INT + " ¿De qué cuento habla la interpretación modelo?", "del cuento 2 de Isla Ejemplo", "La primera oración lo dice."),
        ex(INT + " ¿Qué palabra introduce lo que dice el cuento: «según» o «seguro»?", "según", "Es la primera palabra de la interpretación."),
    ],
    C=[
        ex(INT + " ¿Qué palabras introducen la interpretación propia?", "yo interpreto", "Aparecen en la segunda oración."),
        ex(INT + " ¿Con qué palabra se introduce la evidencia?", "porque", "Aparece en la segunda oración."),
        ex(INT + " ¿Qué límite declara la última oración?", "que el cuento no explica la frase de saludo y no la inventa", "Lo dice la cuarta oración."),
    ],
    A=[
        ex("Ordena las partes de una interpretación atribuida. A) vínculo y límite. B) evidencia con «porque». C) lo que dice el texto con «según». D) mi interpretación con «yo interpreto». Escribe las letras en orden.", "C, D, B, A", "Se cita, se interpreta, se justifica y se cierra con el vínculo y el límite."),
        ex(INT + " Elige la mejor evidencia. A) «porque el texto dice que cada nudo recuerda a una persona de la casa». B) «porque a mí me parece». Escribe la letra.", "A", "La evidencia debe ser una frase del texto."),
        arith("Una interpretación debe tener 4 partes. Un compañero tiene la cita y la interpretación. ¿Cuántas partes le faltan?", "4-2", "Se restan las escritas de las cuatro pedidas."),
    ],
    Z=[
        ex(INT + " Un niño agrega: «El cordón también sirve para ahuyentar el mal». ¿Tiene evidencia en el cuento? Sí o No.", "No", "El cuento no dice eso."),
        ex(INT + " ¿Qué parte de la interpretación modelo permite que el lector sepa qué es de quien escribe: la cita o el «yo interpreto»?", "el «yo interpreto»", "Marca lo propio."),
    ],
    D=[
        ex("Dos interpretaciones del canasto del cuento 1. Camila: «Según el cuento, la abuela dice que el canasto lleno enseña a mirar con atención; yo interpreto que ese año de recolección entrena la mirada». Pablo: «El canasto es mágico». ¿Quién interpretó con evidencia?", "Camila", "Se apoya en la frase de la abuela."),
        ex("Antes de mostrar tu interpretación de un texto de una cultura real, ¿a quién se la muestras primero: al educador o a la educadora tradicional o a nadie?", "al educador o a la educadora tradicional", "Se pide validación antes de compartir."),
    ],
    context=[ex("En una visita, te cuentan una historia con un objeto simbólico. Al escribir tu interpretación, ¿citas lo que te contaron y declaras lo que no sabes, o completas con lo que imaginas?", "citas lo que te contaron y declaras lo que no sabes", "Una interpretación honesta tiene cita y límite.")],
    selfcheck=[
        ex("¿Cuántas partes tiene la interpretación atribuida de esta clase?", "4", "Cita, interpretación, evidencia y vínculo con límite."),
        ex("¿La evidencia sale del texto o de mi imaginación?", "del texto", "Es una frase que lo respalda."),
        ex("¿Qué marca lo mío: «yo interpreto» o «según»?", "yo interpreto", "«Según» cita el texto."),
    ],
    task=T(
        "Lee este cuento inventado: «En Valle Brisa, una cultura ficticia, cuando una persona se muda de casa, los vecinos le llevan un puñado de tierra de su antiguo patio en una bolsa de tela. La persona la guarda en una maceta. Una persona mayor dice que la tierra recuerda de dónde se viene. Los vecinos no cuentan a los visitantes el canto que dicen al entregar la bolsa.» En tu cuaderno escribe una interpretación de cuatro oraciones: lo que dice el cuento (con «según»), tu interpretación (con «yo interpreto»), la evidencia (con «porque») y un vínculo con tu experiencia más el límite.",
        "Según el cuento de Valle Brisa, los vecinos le llevan a quien se muda un puñado de tierra de su antiguo patio y la persona la guarda en una maceta. Yo interpreto que la tierra ayuda a no olvidar de dónde se viene, porque una persona mayor dice que la tierra recuerda de dónde se viene. Esto me hace pensar en la foto de mi curso anterior. El cuento no cuenta el canto de la entrega y yo no lo invento.",
        ["cita con «según»", "interpreta con «yo interpreto»", "da evidencia con una frase del texto", "vincula y declara el límite"],
        ["interpretación de cuatro oraciones"],
        ["interpretar sin evidencia", "inventar el canto"],
        "Si falta evidencia, pídele que subraye en el cuento la frase que apoya su interpretación.",
    ),
    reinforce="Copia la interpretación modelo y rotula cada oración con su parte.",
    extend="Escribe una segunda interpretación del mismo cuento de Valle Brisa con otra evidencia y otro vínculo.",
)

# ============================================================ LS03 clase 5 · contrastar dos textos
CT1 = "Cuento 1 (resumen): en Lluvia Ejemplo cada niño llena un canasto durante un año con objetos que encuentra; la abuela dice que enseña a mirar con atención el lugar donde se vive."
CT2 = "Cuento 2 (resumen): en Isla Ejemplo, quien viaja recibe un cordón con tres nudos; cada nudo recuerda a una persona de la casa; al volver, devuelve el cordón y cuenta su viaje."

L(
    LS3, 5,
    materials="Lápiz y hoja. Los dos resúmenes están escritos aquí y son inventados para practicar.",
    use="Aprenderé a comparar dos textos de culturas ficticias distintas con los mismos criterios, diciendo qué se parecen y qué cambian sin afirmar que una cultura o un texto es superior. Sirve para valorar la diversidad cultural al leer.",
    prior=["Sé interpretar elementos significativos con evidencia.", "Sé que jerarquizar es decir que algo vale más que otra cosa."],
    explain=[
        "Compararlos es mirar dos textos con los mismos criterios. Puedo usar: qué objeto central aparece, qué hace la gente con él, qué sentido da el texto y qué guarda como límite. Respondo cada criterio para cada texto y luego escribo semejanzas y diferencias con evidencia.",
        "En los resúmenes, el objeto central del cuento 1 es un canasto y el del cuento 2 es un cordón. En ambos casos el objeto acompaña un momento importante de la vida y hay una persona que cuenta algo después. En el cuento 1 el sentido es mirar con atención el lugar; en el 2 es recordar a las personas de la casa. Esas son semejanzas y diferencias comprobables en los textos.",
        "No jerarquizo: no digo que el cuento del canasto sea «más profundo» ni que el del cordón sea «más hermoso». Tampoco mezclo los cuentos como si fueran una sola cultura. Cierro con una frase que nombre cada texto, diga una semejanza y una diferencia y marque mi opinión con «yo pienso».",
    ],
    vocab=[("objeto central", "cosa más importante de un texto"), ("sentido", "razón o idea que el texto da a algo"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas cambian"), ("jerarquizar", "decir que algo vale más que otra cosa")],
    worked=[
        W("Comparar el objeto central", CT1 + " " + CT2 + " Compara el objeto central de cada cuento.", ["En el cuento 1 el objeto central es un canasto.", "En el cuento 2 es un cordón con tres nudos.", "Son objetos distintos."], "un canasto en el cuento 1 y un cordón con nudos en el 2"),
        W("Reconocer una jerarquización", "Alguien dice: «El cuento del canasto es más profundo que el del cordón». ¿Compara o jerarquiza?", ["La frase dice que uno es más profundo.", "«Más profundo» no se apoya en un dato del texto.", "Pone un cuento sobre otro."], "jerarquiza"),
    ],
    mistakes=[
        M("Escribir «la cultura del cordón es mejor que la del canasto».", "No se jerarquizan culturas.", "Digo qué se parece y qué cambia."),
        M("Mezclar los cuentos y decir «en esa cultura reciben canastos y cordones».", "Son dos culturas ficticias distintas.", "Nombro cada cuento por su cultura."),
    ],
    R=[
        ex(CT1 + " ¿Qué objeto es central en el cuento 1?", "un canasto", "El resumen lo dice."),
        ex(CT2 + " ¿Qué objeto es central en el cuento 2?", "un cordón con tres nudos", "El resumen lo dice."),
        ex("Jerarquizar, ¿es decir que algo vale más que otra cosa o mirar con los mismos criterios?", "decir que algo vale más que otra cosa", "Es la definición de la clase."),
    ],
    C=[
        ex(CT1 + " ¿Qué sentido da la abuela al canasto?", "enseña a mirar con atención el lugar donde se vive", "El resumen lo dice."),
        ex(CT2 + " ¿Qué sentido tiene cada nudo?", "recuerda a una persona de la casa", "El resumen lo dice."),
        ex("Verdadero o falso: se puede decir que el cuento 1 es mejor porque tiene más objetos.", "Falso", "La cantidad de objetos no mide el valor de un texto."),
    ],
    A=[
        ex(CT1 + " " + CT2 + " Completa con 1 o 2: en el cuento ___ el objeto se llena durante un año; en el cuento ___ el objeto se devuelve al volver. Escribe los dos números en orden.", "1, 2", "El canasto se llena durante un año y el cordón se devuelve."),
        arith(CT1 + " " + CT2 + " Si el canasto del cuento 1 recibe 3 objetos y el cordón del cuento 2 tiene 3 nudos, ¿cuántas cosas hay en total entre ambos?", "3+3", "Se suman los objetos y los nudos."),
        ex("Clasifica cada frase como C (compara) o J (jerarquiza). 1) «Los dos cuentos tienen un objeto que acompaña un momento importante». 2) «El del canasto es más hermoso». 3) «Uno enseña a mirar y el otro a recordar a las personas». Escribe las tres letras.", "1 C, 2 J, 3 C", "Solo la frase 2 pone un texto sobre el otro."),
    ],
    Z=[
        ex(CT1 + " " + CT2 + " ¿Qué tienen en común los dos cuentos según los resúmenes: un objeto que acompaña a las personas o una fiesta con música?", "un objeto que acompaña a las personas", "Los dos tienen un objeto central."),
        ex(CT1 + " " + CT2 + " Un compañero dice que son la misma cultura porque los dos tienen un objeto. ¿Es correcto? Sí o No.", "No", "Son dos culturas ficticias distintas."),
    ],
    D=[
        ex(CT1 + " " + CT2 + " Elige la mejor frase de cierre. A) «Los dos cuentos tienen un objeto que acompaña un momento importante; el canasto enseña a mirar el lugar y el cordón recuerda a las personas; yo pienso que ambos cuidan lo que importa». B) «El cuento 2 es mejor». Escribe la letra.", "A", "Dice semejanza, diferencia y marca la opinión propia."),
        ex("Quieres comparar uno de los cuentos con una historia real que te contaron en tu familia, pero esa historia es reservada. ¿La comparas con detalles o dices que existe y la respetas?", "dices que existe y la respetas", "Lo reservado no se cuenta sin permiso."),
    ],
    context=[ex("Dos amigos discuten qué cuento es mejor, el del canasto o el del cordón. ¿Qué les propones: elegir el mejor o explicar qué se parece y qué cambia entre los dos?", "explicar qué se parece y qué cambia entre los dos", "Comparar con criterios evita jerarquizar.")],
    selfcheck=[
        ex("¿Qué se usa al comparar: los mismos criterios o criterios distintos para cada texto?", "los mismos criterios", "Así es justo."),
        ex("¿«Más hermoso» compara o jerarquiza?", "jerarquiza", "Pone una cosa sobre otra."),
        ex("¿Los cuentos de la clase son de la misma cultura? Sí o No.", "No", "Son de dos culturas ficticias distintas."),
    ],
    task=T(
        "Usa estos resúmenes inventados. Cuento A (Montaña Ejemplo): cuando alguien llega a vivir al pueblo, cada vecino deja una piedra pequeña frente a su puerta; la persona mayor dice que las piedras recuerdan que nadie llega solo. Cuento B (Bahía Ejemplo): cuando alguien llega al pueblo, cada vecino le entrega una hoja seca; la persona mayor dice que las hojas recuerdan que el viento trae a las personas. En tu cuaderno haz una tabla con estas filas: objeto central, qué hace la gente y sentido que da el texto. Luego escribe una frase de cierre con una semejanza, una diferencia y tu opinión con «yo pienso», sin jerarquizar.",
        "Objeto: piedras / hojas secas. Qué hace la gente: dejan piedras frente a su puerta / entregan una hoja a quien llega. Sentido: nadie llega solo / el viento trae a las personas. Cierre: «En los dos cuentos, los vecinos reciben a quien llega con un objeto sencillo; las piedras recuerdan que nadie llega solo y las hojas que el viento trae a las personas. Yo pienso que ambos muestran bienvenida.»",
        ["completa las tres filas para ambos cuentos", "usa los mismos criterios", "escribe semejanza, diferencia y opinión marcada", "no jerarquiza"],
        ["tabla de comparación", "frase de cierre"],
        ["decir que un cuento es mejor", "dejar una fila sin completar"],
        "Si jerarquiza, pídele que reemplace la palabra por un dato de la tabla.",
    ),
    reinforce="Copia los resúmenes de la clase y subraya con un color el objeto central de cada uno.",
    extend="Compara con la misma tabla uno de los cuentos de la clase con una costumbre de bienvenida de tu familia, sin jerarquizar.",
)

# ============================================================ LS03 clase 6 · comunicar la comprensión con validación
MOD = "Resumen oral modelo (inventado para practicar): «Les voy a contar el cuento inventado de Lluvia Ejemplo. Según el cuento, cada niño recibe un canasto vacío a los ocho años y lo llena durante un año con objetos que encuentra. La abuela dice que el canasto lleno enseña a mirar con atención el lugar donde se vive. Yo pienso que es una bonita forma de aprender a observar. El pueblo no cuenta a los visitantes qué guardan los mayores en sus canastos, y yo no lo invento. Si el cuento fuera real, antes de contarlo se lo mostraría a una persona de esa cultura.»"

L(
    LS3, 6,
    materials="Lápiz y hoja. El resumen oral modelo está escrito aquí y es inventado para practicar. Puede leerlo una persona adulta en voz alta.",
    use="Aprenderé a comunicar oralmente lo que comprendí de un texto de otra cultura, con claridad y respeto, y a pedir validación cuando el texto pertenece a una cultura real. Sirve para compartir mi comprensión sin hablar en nombre de otros.",
    prior=["Sé interpretar con evidencia y comparar sin jerarquizar.", "Sé que el educador o la educadora tradicional valida lo que se refiere a pueblos reales."],
    explain=[
        "Comunicar lo que comprendí es contarlo de modo que otra persona lo entienda sin cambiar el texto. Un resumen oral breve tiene cinco partes: presentar el texto y su cultura, contar lo que dice con «según», dar mi interpretación o mi opinión con «yo pienso», declarar el límite y, si el texto es real, decir que lo validé con quien conoce la cultura.",
        "En el resumen oral modelo, la presentación dice «cuento inventado de Lluvia Ejemplo». Eso evita que parezca que se habla de un pueblo real. El límite es que el pueblo no cuenta lo que guardan los mayores. Y la última oración recuerda que, si el cuento fuera real, antes de contarlo se lo mostraría a una persona de esa cultura.",
        "Cuando el texto es de un pueblo real, la validación es obligatoria: el educador o la educadora tradicional, o la comunidad, revisa lo que voy a decir y puede pedir cambios. Hablo con calma, miro al público y no improviso datos. Si me preguntan algo que no sé, digo que lo consultaré.",
    ],
    vocab=[("resumen oral", "versión corta de un texto que se cuenta en voz alta"), ("validar", "mostrar un trabajo a quien conoce el tema para confirmar que lo respeta"), ("público", "personas que escuchan"), ("improvisar", "decir algo sin haberlo preparado"), ("presentar", "dar a conocer el texto y su cultura")],
    worked=[
        W("Identificar el límite", MOD + " ¿Qué límite declara el resumen oral modelo?", ["Busco la frase que avisa lo que no se cuenta.", "Dice que el pueblo no cuenta a los visitantes qué guardan los mayores y que no lo inventa.", "Ese es el límite."], "que el pueblo no cuenta lo que guardan los mayores y que quien resume no lo inventa"),
        W("Reconocer la validación", MOD + " ¿Qué dice el resumen sobre la validación?", ["Busco la última oración.", "Dice que, si el cuento fuera real, antes de contarlo se lo mostraría a una persona de esa cultura.", "Esa es la validación."], "que, si el cuento fuera real, lo mostraría antes a una persona de esa cultura"),
    ],
    mistakes=[
        M("Presentar un cuento de un pueblo real sin mostrarlo antes a nadie.", "Puede tener errores o contar algo reservado.", "Pido validación al educador o a la educadora tradicional."),
        M("Improvisar un dato que se me olvidó.", "Puede ser falso.", "Digo «lo consultaré» y lo reviso."),
    ],
    R=[
        ex(MOD + " ¿De qué cuento habla el resumen oral modelo?", "del cuento inventado de Lluvia Ejemplo", "La primera oración lo dice."),
        ex(MOD + " ¿A qué edad recibe cada niño el canasto?", "a los ocho años", "El resumen lo dice."),
        ex(MOD + " ¿Qué dice la abuela que enseña el canasto lleno?", "a mirar con atención el lugar donde se vive", "El resumen lo dice."),
    ],
    C=[
        ex(MOD + " ¿Qué marca la opinión de quien resume: «yo pienso» o «según»?", "yo pienso", "Aparece en la cuarta oración."),
        ex(MOD + " ¿Qué se hace con el cuento si fuera real, según el resumen?", "se muestra antes a una persona de esa cultura", "Es la validación."),
        ex("Verdadero o falso: si el texto es de un pueblo real, se puede contar sin validar si se hace con cariño.", "Falso", "La validación es necesaria."),
    ],
    A=[
        ex("Ordena las partes de un resumen oral. A) validación. B) opinión con «yo pienso». C) presentación del texto y su cultura. D) límite. E) lo que dice con «según». Escribe las letras en orden.", "C, E, B, D, A", "Se presenta, se cuenta, se opina, se declara el límite y se menciona la validación."),
        arith("Un resumen oral debe durar como máximo 2 minutos. Un grupo ya habló 75 segundos. ¿Cuántos segundos le quedan?", "2*60-75", "Dos minutos son 120 segundos, menos 75 que ya usó."),
        ex(MOD + " Elige la mejor frase para comenzar. A) «Les voy a contar el cuento inventado de Lluvia Ejemplo». B) «Así son todas las culturas». Escribe la letra.", "A", "Dice de qué texto y cultura habla."),
    ],
    Z=[
        ex(MOD + " Una compañera dice que el resumen debería contar qué guardan los mayores en sus canastos. ¿Respeta el límite? Sí o No.", "No", "El cuento dice que ese contenido no se cuenta."),
        ex(MOD + " ¿Por qué el resumen dice «cuento inventado»? Porque ___.", "así no parece que habla de un pueblo real", "Aclara que el texto es inventado."),
    ],
    D=[
        ex("Una niña presenta un cuento de un pueblo real y no tuvo tiempo de mostrárselo al educador tradicional. ¿Qué es mejor: presentar igual o pedir más tiempo para validarlo?", "pedir más tiempo para validarlo", "La validación es parte de presentar con respeto."),
        ex("Si en tu resumen aparece una palabra en lengua indígena que no estás seguro de pronunciar, ¿la dices como crees o la consultas con el educador o la educadora tradicional?", "la consultas con el educador o la educadora tradicional", "Una palabra en lengua se consulta."),
    ],
    context=[ex("En tu escuela, un abuelo cuenta un relato de su pueblo y te pide que lo resumas para tu curso. ¿Lo resumes y se lo muestras primero a él, o lo resumes y lo presentas sin avisarle?", "lo resumes y se lo muestras primero a él", "Se valida con quien lo contó.")],
    selfcheck=[
        ex("¿Cuántas partes tiene el resumen oral de esta clase?", "5", "Presentación, lo que dice, opinión, límite y validación."),
        ex("¿Puedo improvisar un dato que no recuerdo? Sí o No.", "No", "Se consulta antes."),
        ex("Un cuento inventado, ¿se presenta como inventado o como real?", "como inventado", "Así no se engaña al público."),
    ],
    task=T(
        "Lee este cuento inventado: «En Colina Ejemplo, una cultura ficticia, cuando los niños terminan el año escolar, cada uno planta una semilla en una caja de madera. Una persona mayor dice que la semilla aprende a esperar. Los visitantes no preguntan qué se canta cuando se entrega la caja.» En tu cuaderno escribe un resumen oral de cinco oraciones con estas partes: presentación del texto y su cultura, lo que dice con «según», tu opinión con «yo pienso», límite y una oración que diga a quién se lo mostrarías si fuera real. Luego léelo en voz alta a una persona de tu casa.",
        "Les voy a contar el cuento inventado de Colina Ejemplo. Según el cuento, cuando los niños terminan el año escolar, cada uno planta una semilla en una caja de madera. Yo pienso que es una forma bonita de aprender a esperar. El cuento no cuenta qué se canta cuando se entrega la caja y yo no lo invento. Si fuera real, lo mostraría antes a una persona de esa cultura.",
        ["tiene las cinco partes", "dice que el cuento es inventado", "marca la opinión con «yo pienso»", "declara el límite y menciona la validación"],
        ["resumen de cinco oraciones", "lectura en voz alta"],
        ["inventar el canto", "presentar como real un texto inventado"],
        "Si falta una parte, pídele que rotule cada oración con su número.",
    ),
    reinforce="Lee en voz alta el resumen modelo ante una persona de tu casa y anota si se entendió.",
    extend="Escribe un segundo resumen oral del cuento de Isla Ejemplo con las cinco partes.",
)
