"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 09 (cultura global, cultura de los pueblos indígenas y otras culturas, desde la interculturalidad) y
OA 10 (formas de concepción de mundo de los pueblos indígenas y de otras culturas).

Las comunidades, personas y testimonios son INVENTADOS y se rotulan así; no se afirma nada de la lengua, los ritos
ni la cosmovisión de un pueblo real. Lo tradicional lo enseñan el educador o la educadora tradicional y la comunidad.
"""
from __future__ import annotations

from student_content_lc6_a import L, M, MAT, T, W
from student_lessons import arith, ex

OA9, OA10 = "LC06 OA 09", "LC06 OA 10"

# ------------------------------------------------------------------ OA 09
FLE = ("Ficha situada (inventada). Comunidad: Lago Espejo (no es un pueblo real). Territorio: un lago, un bosque y un camino hacia una ciudad vecina. "
       "Fuente y responsable: don Mateo, pescador de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: don Mateo autorizó usar esta ficha en la escuela. "
       "Límite: no se cuentan las historias del lago que la comunidad reserva.")
TLE = ("Testimonio inventado de don Mateo, de Lago Espejo: «Mi nieta Camila escucha música de muchos países en su teléfono y ve videos de todo el mundo. También va a la feria de la ciudad vecina, "
       "donde se juntan campesinos, vendedores y artesanos. En casa le enseñamos a cuidar el lago como lo aprendimos de los mayores. A veces ella dice que las costumbres de la comunidad son lentas; yo le digo que también tienen su razón.»")

L(
    OA9, 1, materials=MAT,
    use="Aprenderé a situar tres tipos de cultura que se encuentran hoy en un mismo lugar: la cultura global, la cultura de un pueblo indígena y otras culturas del entorno. Sirve para problematizar su relación desde la interculturalidad.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que una cultura es la forma de vida que un grupo comparte y transmite."],
    explain=[
        "La cultura global es el conjunto de modas, músicas, videos, comidas y costumbres que circulan por todo el mundo y llegan a muchos lugares al mismo tiempo, sobre todo por las pantallas. La cultura de un pueblo indígena es su forma de vida propia, con su lengua, sus saberes y su relación con el territorio, que los mayores transmiten a las nuevas generaciones.",
        "En el entorno local y nacional hay además otras culturas: la de quienes viven en el campo, la de las ciudades, la de las familias que llegaron de otras regiones o países. Todas conviven en la escuela, en la feria y en el barrio. Cada una tiene sus costumbres y no es mejor ni peor que las otras.",
        "Problematizar esa relación es preguntarse qué pasa cuando se encuentran: ¿qué se aprende?, ¿qué se puede perder?, ¿quién decide? La interculturalidad es la manera de relacionarse en que las culturas se conocen y aprenden unas de otras con respeto, sin que una domine a las demás. Para empezar, situamos la fuente: quién cuenta, de qué comunidad es y qué no se puede contar.",
    ],
    vocab=[("cultura global", "modas, músicas, videos y costumbres que circulan por todo el mundo"), ("cultura de un pueblo indígena", "forma de vida propia de un pueblo, transmitida por los mayores"), ("entorno local", "el lugar cercano donde se vive, como el barrio o la localidad"), ("interculturalidad", "relación respetuosa entre culturas que aprenden unas de otras sin dominarse"), ("problematizar", "hacerse preguntas sobre algo para entenderlo mejor")],
    worked=[
        W("Leer una ficha situada", FLE + " ¿De quién es el relato y qué no se puede contar?", ["La comunidad es Lago Espejo y la fuente es don Mateo.", "Él dio permiso para usar la ficha en la escuela.", "El límite dice que no se cuentan las historias del lago que la comunidad reserva."], "El relato es de don Mateo, de Lago Espejo; no se cuentan las historias reservadas del lago."),
        W("Clasificar tres culturas", "Camila escucha música de muchos países en su teléfono, va a la feria de la ciudad vecina y aprende de los mayores a cuidar el lago. ¿A qué tipo de cultura pertenece cada cosa?", ["La música que viaja por todo el mundo es cultura global.", "La feria con campesinos, vendedores y artesanos es parte del entorno local.", "Cuidar el lago como enseñan los mayores es cultura de la comunidad."], "Música: global. Feria: entorno local. Cuidado del lago: cultura de la comunidad."),
    ],
    mistakes=[
        M("Pensar que la cultura global es mejor que la cultura de una comunidad.", "Ninguna cultura es mejor que otra por circular más.", "Describe lo que cada una aporta sin ordenarlas."),
        M("Decir que la comunidad de Lago Espejo representa a todos los pueblos indígenas.", "La ficha habla de una sola comunidad.", "Escribe siempre el nombre de la comunidad y de la fuente."),
    ],
    R=[
        ex("Según la ficha de Lago Espejo, ¿quién es la fuente?", "Don Mateo", "La ficha lo nombra como fuente y responsable."),
        ex("¿Qué territorio tiene Lago Espejo? A) un puerto grande y cerros de pastoreo B) un lago, un bosque y un camino hacia una ciudad vecina", "B", "El puerto y los cerros son de otras fichas."),
        ex("La ficha de Lago Espejo dice que no se cuentan las historias reservadas del lago. ¿Las escribes en tu trabajo? Responde Sí o No.", "No", "El límite de la ficha lo prohíbe."),
    ],
    C=[
        ex("En Lengua y Cultura, ¿qué es la cultura global? A) las costumbres de una sola comunidad B) modas, músicas y videos que circulan por todo el mundo", "B", "Son rasgos que llegan a muchos lugares a la vez."),
        ex("Verdadero o falso: la interculturalidad significa que una cultura reemplaza a las demás.", "Falso", "Significa aprender unas de otras con respeto."),
        ex("Verdadero o falso: en una misma localidad pueden convivir varias culturas.", "Verdadero", "Campo, ciudad, comunidades y familias de otros lugares pueden convivir."),
    ],
    A=[
        ex("Clasifica en GLOBAL, LOCAL o COMUNIDAD: a) un video de moda que ven jóvenes de muchos países b) una feria de barrio en una ciudad del país c) el cuidado del lago que los mayores enseñan en Lago Espejo.", "a global, b local, c comunidad", "Cada uno corresponde a un alcance distinto de la cultura."),
        ex("Don Mateo dice que Camila escucha música de muchos países. ¿Qué tipo de cultura aparece en esa frase? A) cultura de la comunidad B) cultura global", "B", "La música que viaja por el mundo es parte de la cultura global."),
        ex("Una compañera trae una ficha con comunidad y fuente, pero sin límite. ¿Qué falta? A) el nombre de la ciudad vecina B) lo que no se puede contar", "B", "El límite dice qué no se cuenta."),
    ],
    Z=[
        ex("Pablo escribe: «Como Camila escucha música de muchos países, en toda comunidad indígena los jóvenes dejaron sus costumbres». ¿Qué error comete?", "Generaliza el caso de una joven a todas las comunidades", "Un testimonio no representa a todos los pueblos."),
        ex("¿Por qué conviene situar la fuente antes de hablar de cómo se relacionan las culturas? A) para escribir más rápido B) porque el relato es la mirada de una persona de una comunidad", "B", "Situar muestra de quién es la mirada."),
    ],
    D=[
        ex("Una ficha dice solo: «Comunidad: Lago Espejo. Territorio: lago y bosque». ¿Qué datos de una ficha situada faltan?", "Fuente, permiso y límite", "La ficha situada exige esos tres datos además de comunidad y territorio."),
        ex("Un cartel dice: «Todas las comunidades viven como Lago Espejo». ¿Qué corriges? A) escribo «Lago Espejo (comunidad inventada) vive así» B) lo dejo igual", "A", "El cartel debe atribuir el dato a esa comunidad."),
    ],
    context=[ex("En tu escuela se organiza una feria cultural. Alguien propone un puesto sobre «la cultura de los pueblos indígenas» sin decir de cuál pueblo ni con permiso de quién. ¿Qué haces primero? A) hago el puesto con lo que recuerdo B) pregunto de qué pueblo se trata y con permiso de quién se presenta", "B", "Sin pueblo ni permiso no se puede representar su cultura.")],
    selfcheck=[
        ex("Nombra los tres tipos de cultura de esta clase.", "Cultura global, cultura de un pueblo indígena y otras culturas del entorno", "Son los tres que se encuentran en un mismo lugar."),
        ex("Verdadero o falso: la ficha de Lago Espejo sirve para hablar de todos los pueblos indígenas.", "Falso", "Una comunidad no representa a todos los pueblos."),
        ex("Tema: el encuentro de culturas. Ante una duda sobre una comunidad real, ¿qué haces? A) pregunto al educador tradicional o a la comunidad B) lo supongo", "A", "Ellos son la fuente."),
    ],
    task=T("Lee esta lista inventada de lo que ve Camila en un día: música de muchos países en su teléfono; la feria de la ciudad vecina; una clase en la escuela; ayudar a su abuelo a cuidar el lago como se lo enseñaron los mayores. Haz una tabla con tres columnas: «cultura global», «entorno local» y «cultura de la comunidad». Ubica cada cosa de la lista en una columna y escribe una pregunta que problematice cómo se relacionan las tres.",
           "Global: música de muchos países. Entorno local: la feria de la ciudad vecina y la escuela. Comunidad: cuidar el lago como enseñan los mayores. Pregunta: ¿cómo puede Camila aprender de la música del mundo sin dejar de aprender de los mayores?",
           ["ubica cada elemento en una columna", "justifica con la definición", "formula una pregunta que problematice"], ["tabla de tres columnas", "pregunta"], ["decir que una cultura es mejor", "generalizar a todos los pueblos"],
           "Pedir que explique por qué ubicó cada elemento en esa columna; valorar que no ordene las culturas."),
    reinforce="Subraya en la ficha de Lago Espejo la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué una cultura no es mejor que otra solo porque circula por más lugares.",
)

L(
    OA9, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre el encuentro de culturas con límites declarados: qué dice la fuente, qué tensión o aprendizaje cuenta, qué interpreto yo y qué no se cuenta.",
    prior=["Sé distinguir cultura global, cultura de una comunidad y entorno local.", "Sé que una interpretación se marca con «yo pienso que»."],
    explain=[
        "Un testimonio sobre el encuentro de culturas puede contar tensiones y aprendizajes. Una tensión es una dificultad que aparece cuando dos formas de ver o hacer las cosas no coinciden. Un aprendizaje es algo nuevo que alguien gana al conocer otra cultura. Para leer con respeto separamos lo que la fuente dice, la tensión o el aprendizaje que cuenta, lo que yo interpreto y lo que no se cuenta.",
        "En el testimonio de don Mateo, la nieta escucha música de muchos países y a la vez aprende del lago con los mayores. Don Mateo cuenta que ella a veces ve las costumbres de la comunidad como lentas. Eso es lo que él dice. Si yo agrego que Camila «quiere dejar la comunidad», ya estoy interpretando algo que nadie dijo.",
        "Problematizar es preguntar sin acusar. Una buena pregunta es «¿cómo puede aprender de ambas?» y una mala es «¿por qué traiciona a su comunidad?». Cerramos con un límite: decimos qué no sabemos y qué debe responder la propia comunidad. Si queremos saber más sobre una comunidad real, preguntamos al educador o a la educadora tradicional.",
    ],
    vocab=[("tensión", "dificultad que aparece cuando dos formas de ver o hacer las cosas no coinciden"), ("aprendizaje", "algo nuevo que se gana al conocer o practicar algo"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("acusar", "culpar a alguien de algo sin que la fuente lo diga"), ("límite", "lo que no se cuenta o no se sabe")],
    worked=[
        W("Separar cuatro cosas", TLE + " Separa lo que dice, la tensión, lo que interpreto y lo que no se cuenta.", ["Dice: Camila escucha música de muchos países y va a la feria de la ciudad vecina.", "Tensión que cuenta: ella a veces dice que las costumbres de la comunidad son lentas.", "Interpreto: yo pienso que Camila quiere conocer más cosas.", "No se cuenta: cómo responde la comunidad cuando Camila dice eso."], "Dice: Camila escucha música del mundo y va a la feria. Tensión: ve lentas las costumbres. Interpreto: quiere conocer más. No se cuenta: cómo responde la comunidad."),
        W("Corregir una pregunta", "Un niño escribe: «¿Por qué Camila traiciona a su comunidad?». ¿Está bien como pregunta para problematizar?", ["La fuente no dice que Camila traicione a nadie.", "La pregunta acusa sin tener un dato.", "Una mejor sería: ¿cómo puede Camila aprender de ambas culturas?"], "No: acusa sin respaldo; conviene preguntar cómo puede aprender de ambas culturas."),
    ],
    mistakes=[
        M("Escribir una acusación como si estuviera en el testimonio.", "La fuente no dijo que Camila traicione a nadie.", "Formula la duda como pregunta respetuosa."),
        M("Rellenar con ideas lo que la comunidad no contó.", "Lo no contado se respeta y no se inventa.", "Escribe «el testimonio no lo dice»."),
    ],
    R=[
        ex("Según don Mateo, ¿qué escucha Camila en su teléfono? A) música de muchos países B) cuentos secretos del lago", "A", "El testimonio dice que escucha música de muchos países."),
        ex("Tema: el encuentro de culturas. Una interpretación, ¿es una idea mía o un dato de la fuente?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Don Mateo dice que en casa le enseñan a cuidar el lago. ¿A quién le enseñan: a Camila o a la feria?", "A Camila", "El testimonio habla de la nieta."),
    ],
    C=[
        ex("Verdadero o falso: una tensión es una dificultad que aparece cuando dos formas de hacer las cosas no coinciden.", "Verdadero", "Esa es la definición de tensión."),
        ex("¿Cuál es una pregunta para problematizar sin acusar? A) ¿por qué traiciona a su comunidad? B) ¿cómo puede Camila aprender de ambas culturas?", "B", "La primera pregunta no acusa."),
        ex("Verdadero o falso: lo que yo agrego sin marcarlo se puede leer como si fuera dicho por don Mateo.", "Verdadero", "Por eso conviene marcarlo con «yo pienso que»."),
    ],
    A=[
        ex("Clasifica en DICE LA FUENTE o INTERPRETO: a) Camila va a la feria de la ciudad vecina b) Camila se aburre con la comunidad.", "a dice la fuente, b interpreto", "La segunda no está en el testimonio."),
        ex("Don Mateo dice: «A veces ella dice que las costumbres de la comunidad son lentas». ¿Qué cuenta ese dato? A) una tensión entre dos formas de ver las cosas B) un aprendizaje sobre música", "A", "La frase muestra un desacuerdo entre su manera y la de la nieta."),
        ex("Don Mateo dice: «Yo le digo que también tienen su razón». ¿Qué actitud muestra hacia la nieta? A) le explica sin descartar lo que ella piensa B) le prohíbe escuchar música", "A", "El testimonio habla de explicar, no de prohibir."),
    ],
    Z=[
        ex("Rosa escribe, sin marcarlo: «Camila quiere abandonar Lago Espejo». ¿Qué debería hacer con esa frase?", "Marcarla como su opinión o quitarla", "No está en el testimonio, así que es opinión."),
        ex("¿Por qué conviene cerrar con un límite? A) para llenar la hoja B) para mostrar hasta dónde llega lo afirmado", "B", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        ex("Dos frases sobre el mismo testimonio. 1) «Don Mateo cuenta que Camila va a la feria de la ciudad vecina». 2) «Don Mateo cuenta que Camila odia el lago». ¿Cuál se queda en la fuente?", "La primera", "La segunda agrega algo que el testimonio no contiene."),
        ex("La ficha de Lago Espejo reserva ciertas historias del lago. Un compañero quiere inventarlas para completar su cartel. ¿Qué haces? A) le pido que respete el límite y no las invente B) le ayudo a inventarlas", "A", "Lo reservado no se inventa."),
    ],
    context=[ex("Para un panel de la escuela, una compañera quiere escribir «Las comunidades indígenas rechazan la cultura global». Solo leyó el testimonio de don Mateo. ¿Qué cambio respeta la fuente? A) dejar la frase igual B) «Don Mateo cuenta que su nieta combina música del mundo y aprendizajes del lago»", "B", "La frase A atribuye el dato y no generaliza.")],
    selfcheck=[
        ex("Nombra las cuatro cosas que separo al leer un testimonio sobre el encuentro de culturas.", "Lo que dice la fuente, la tensión o aprendizaje que cuenta, lo que interpreto y lo que no se cuenta", "Son los pasos de la lectura con límites."),
        ex("Tema: el encuentro de culturas. Verdadero o falso: puedo completar con mi imaginación lo que la comunidad no contó.", "Falso", "Eso sería inventar."),
        ex("Escribe una pregunta para problematizar sin acusar.", "Por ejemplo: ¿cómo puede aprender de ambas culturas?", "Debe preguntar y no culpar."),
    ],
    task=T("Lee este testimonio inventado de don Mateo: «En la escuela de la ciudad vecina, mi nieta presentó un trabajo sobre el lago. La profesora le dijo que le gustó mucho. Después algunos compañeros le preguntaron si en la comunidad se usan teléfonos. Ella se sintió incómoda, porque pensaban que somos distintos a todos.» Haz cuatro columnas: «La fuente dice», «Tensión o aprendizaje», «Yo interpreto» y «No se cuenta». Pon al menos un dato en cada una. Cierra con una pregunta que problematice sin acusar.",
           "La fuente dice: la nieta presentó un trabajo sobre el lago y le gustó a la profesora. Tensión: ella se sintió incómoda con la pregunta de sus compañeros. Yo interpreto: yo pienso que los compañeros tenían una idea simple de la comunidad. No se cuenta: qué respondió ella. Pregunta: ¿cómo podemos preguntar sobre una comunidad sin suponer que es distinta a todos?",
           ["separa cuatro columnas", "usa datos del testimonio", "formula una pregunta respetuosa"], ["tabla de cuatro columnas", "pregunta"], ["acusar a los compañeros", "inventar lo no contado"],
           "Pedir que indique en qué línea del testimonio está cada dato; valorar que la pregunta no acuse."),
    reinforce="Subraya con un color lo que dice la fuente y con otro lo que interpretas en el testimonio de don Mateo.",
    extend="Explica por qué una pregunta puede ayudar a entender mejor una tensión entre culturas, y otra puede dañar.",
)

L(
    OA9, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre culturas: cuándo hay interculturalidad, cuándo hay falta de respeto y cuándo una cultura termina absorbiendo a otra. Sirve para problematizar casos sin jerarquizar.",
    prior=["Sé leer un testimonio con límites.", "Sé qué es la interculturalidad y qué es una tensión."],
    explain=[
        "No todo contacto entre culturas es intercultural. Hay interculturalidad cuando las culturas se conocen y aprenden unas de otras en condiciones de respeto, con el permiso de quienes comparten algo suyo y sin que una domine a las demás. Es un encuentro en que todas las partes participan y deciden.",
        "Hay otros casos que no lo son. La apropiación ocurre cuando alguien toma y usa como suyo algo de otra cultura sin permiso ni reconocimiento. La asimilación ocurre cuando un grupo termina dejando sus rasgos propios para parecerse a otro porque se siente obligado. Y la simple convivencia sin conocerse tampoco es todavía interculturalidad.",
        "Para analizar un caso usamos preguntas iguales para todos: ¿hay permiso?, ¿se reconoce a quien lo creó?, ¿todos participan y deciden?, ¿alguien debe dejar lo suyo? Con las respuestas decidimos si el caso muestra interculturalidad o no. Así comparamos sin decir que una cultura es mejor que otra y sin generalizar desde un solo caso.",
    ],
    vocab=[("interculturalidad", "relación respetuosa entre culturas que aprenden unas de otras sin dominarse"), ("apropiación", "usar como propio algo de otra cultura sin permiso ni reconocimiento"), ("asimilación", "dejar los rasgos propios para parecerse a otro grupo por sentirse obligado"), ("reconocimiento", "decir quién creó o enseñó algo"), ("permiso", "autorización de quien comparte algo suyo")],
    worked=[
        W("Analizar un caso", "Caso inventado A: en una feria, una comunidad presenta un tejido con su permiso, dice quién lo hizo y las demás personas hacen preguntas y aprenden. ¿Es intercultural?", ["¿Hay permiso? Sí, la comunidad presenta su tejido.", "¿Se reconoce a quien lo hizo? Sí, lo dice.", "¿Todos participan? Sí, hacen preguntas y aprenden."], "Sí: hay permiso, reconocimiento y participación de todos."),
        W("Distinguir apropiación", "Caso inventado B: una tienda vende como suyo un diseño hecho por una comunidad, sin pedir permiso ni decir quién lo creó. ¿Qué es?", ["No hay permiso.", "No hay reconocimiento de quien lo creó.", "Se toma algo de otra cultura como propio."], "Es apropiación, no interculturalidad."),
    ],
    mistakes=[
        M("Pensar que toda convivencia entre culturas ya es interculturalidad.", "Se necesita conocimiento mutuo, respeto y participación.", "Aplica las cuatro preguntas del caso."),
        M("Decir que un caso de apropiación demuestra cómo son todas las empresas o todas las culturas.", "Un caso no representa a todos.", "Describe solo el caso estudiado."),
    ],
    R=[
        ex("Caso E inventado: una escuela invita a un artesano de una comunidad y escribe su nombre en el diario mural para agradecerle. ¿Se reconoce a quien enseñó? Responde Sí o No.", "Sí", "El caso dice que se escribe su nombre para agradecerle."),
        ex("Caso F inventado: una revista publica una canción de una comunidad como si fuera de la revista. ¿Se reconoce a la comunidad? Responde Sí o No.", "No", "El caso dice que se publica como si fuera de la revista."),
        ex("Usar como propio algo de otra cultura sin permiso, ¿se llama apropiación o interculturalidad?", "Apropiación", "Esa es la definición de apropiación."),
    ],
    C=[
        ex("Verdadero o falso: para que haya interculturalidad todas las partes participan y deciden.", "Verdadero", "Es parte de la relación respetuosa."),
        ex("En Lengua y Cultura, ¿qué es la asimilación? A) compartir algo con permiso B) dejar los rasgos propios para parecerse a otro grupo por sentirse obligado", "B", "La otra opción describe interculturalidad."),
        ex("Verdadero o falso: convivir en el mismo barrio sin conocerse ya es interculturalidad.", "Falso", "Se requiere conocimiento mutuo y respeto."),
    ],
    A=[
        ex("Caso C inventado: una familia deja de usar las costumbres de su comunidad porque en su nuevo barrio la hacen sentir que debe parecerse a los demás. ¿Qué es? A) interculturalidad B) asimilación", "B", "La familia deja lo propio por sentirse obligada."),
        ex("Clasifica cada caso en INTERCULTURAL o NO: a) una escuela invita a una persona de la comunidad a enseñar y le agradece b) una revista copia el diseño de una comunidad sin avisar.", "a intercultural, b no", "La primera tiene invitación y reconocimiento; la segunda, no."),
        ex("Caso D inventado: una profesora pide permiso a una comunidad para mostrar a su curso un trabajo suyo y cita quién lo hizo. ¿Qué dos condiciones cumple? A) permiso y reconocimiento B) apropiación y asimilación", "A", "Pide permiso y nombra a quien lo hizo."),
    ],
    Z=[
        ex("Ana dice: «Como en el caso B una tienda se apropió de un diseño, todas las tiendas lo hacen». ¿Qué error comete?", "Generaliza un caso a todos", "Un solo caso no representa a todas las tiendas."),
        ex("Un compañero dice que la asimilación es buena porque «así todos son iguales». ¿Qué le falta considerar? A) que implica dejar lo propio por sentirse obligado B) que es más rápida", "A", "La asimilación implica pérdida de rasgos propios."),
    ],
    D=[
        ex("Un caso: una feria presenta bailes y comidas de varias comunidades, pero nadie pidió permiso ni dijo de qué comunidad es cada cosa. Según las cuatro preguntas, ¿cuáles dos faltan?", "Permiso y reconocimiento", "El caso omite pedir permiso y nombrar a la comunidad."),
        ex("Otro caso: un taller reúne a jóvenes de dos culturas para aprender técnicas de ambas con permiso de quienes las enseñan. ¿Es intercultural? A) Sí B) No", "A", "Hay permiso, enseñanza y participación mutua."),
    ],
    context=[ex("Tu curso quiere hacer un mural con símbolos de varias culturas. Un compañero propone copiar de internet un diseño de una comunidad, sin consultar. ¿Qué haces para que sea intercultural? A) copiarlo igual B) pedir permiso y reconocer a quien lo creó", "B", "Permiso y reconocimiento son parte de la interculturalidad.")],
    selfcheck=[
        ex("Nombra dos preguntas para analizar un caso de encuentro de culturas.", "Dos entre: ¿hay permiso?, ¿se reconoce a quien lo creó?, ¿todos participan?, ¿alguien debe dejar lo suyo?", "Son las preguntas de la explicación."),
        ex("Verdadero o falso: la apropiación consiste en pedir permiso y reconocer a la comunidad.", "Falso", "La apropiación es hacerlo sin permiso ni reconocimiento."),
        ex("Escribe una diferencia entre interculturalidad y asimilación.", "En la interculturalidad se aprende con respeto; en la asimilación se deja lo propio por obligación", "Se distinguen por el respeto y la obligación."),
    ],
    task=T("Analiza estos dos casos inventados. Caso 1: una escuela invita a una persona de una comunidad a enseñar una técnica de tejido, le agradece, dice su nombre en el diario mural y los estudiantes preguntan y aprenden. Caso 2: una tienda imprime en sus poleras un diseño de una comunidad, sin pedir permiso ni decir de dónde viene. Haz una tabla con cuatro preguntas: «¿hay permiso?», «¿se reconoce a quien lo creó?», «¿todos participan?» y «¿alguien debe dejar lo suyo?». Responde para cada caso y escribe si es o no intercultural.",
           "Caso 1: permiso sí; reconocimiento sí; participan todos sí; nadie deja lo suyo. Es intercultural. Caso 2: permiso no; reconocimiento no; participan no; la comunidad no decide. No es intercultural, es apropiación.",
           ["responde las cuatro preguntas por caso", "decide con base en las respuestas", "no jerarquiza culturas"], ["tabla con cuatro preguntas y dos casos"], ["generalizar a todas las tiendas", "no usar los criterios"],
           "Pedir que señale en el caso la frase que justifica cada respuesta; valorar que no ordene las culturas."),
    reinforce="Marca con verde las respuestas «sí» y con rojo las «no» en tu tabla para ver cómo cambia el resultado.",
    extend="Propón un cambio para que el caso 2 se vuelva intercultural, indicando qué permiso y qué reconocimiento harían falta.",
)

L(
    OA9, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida que problematice la relación entre la cultura global, la de un pueblo indígena y otras culturas, desde la interculturalidad, con fuente, reflexión, límite y pregunta.",
    prior=["Sé analizar un caso con cuatro preguntas.", "Sé leer un testimonio con límites."],
    explain=[
        "Una respuesta atribuida sobre la relación entre culturas tiene cinco partes. Primero, el dato de la fuente con su nombre: «Don Mateo cuenta que…». Segundo, el encuentro de culturas que aparece: global, de la comunidad o del entorno. Tercero, tu reflexión con «yo pienso que», que incluya una pregunta para problematizar. Cuarto, un límite. Quinto, una propuesta intercultural o una pregunta para el educador tradicional.",
        "Una propuesta intercultural es una idea concreta para que las culturas se encuentren con respeto. Por ejemplo, una feria donde cada comunidad presenta lo que quiere compartir, con su permiso, nombrando a quien lo creó y con espacio para que todas las personas pregunten y aprendan. Una propuesta no puede decidir por la comunidad: solo puede invitar.",
        "Una buena respuesta no dice que una cultura es mejor, no acusa a personas y no generaliza desde un solo testimonio. Reconoce lo que sabe y lo que no. Al final se devuelve a la comunidad o al educador, para que la revise y diga si falta algo o si algo no debe contarse así.",
    ],
    vocab=[("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("propuesta intercultural", "idea concreta para que las culturas se encuentren con respeto"), ("problematizar", "hacerse preguntas sobre algo para entenderlo mejor"), ("devolución", "mostrar el trabajo a la comunidad o al educador para que lo revisen"), ("generalizar", "extender un caso a todos los casos sin pruebas")],
    worked=[
        W("Armar una respuesta", TLE + " Arma una respuesta atribuida de cinco partes.", ["Dato: don Mateo cuenta que su nieta escucha música de muchos países y aprende del lago con los mayores.", "Encuentro: cultura global y cultura de la comunidad.", "Reflexión: yo pienso que ella podría aprender de ambas, y me pregunto cómo apoyarla.", "Límite y propuesta: no sé qué opina la comunidad; propongo una feria con permiso, y pregunto al educador tradicional."], "Respuesta con dato atribuido, encuentro de culturas, reflexión con pregunta, límite y propuesta."),
        W("Revisar una propuesta", "Una niña propone: «Que la escuela muestre los bailes de todas las comunidades indígenas sin consultar, para que todos conozcan». ¿Es intercultural?", ["Falta el permiso de cada comunidad.", "Falta reconocer de cuál comunidad es cada baile.", "No todas las comunidades participan en la decisión."], "No es intercultural todavía: falta permiso, reconocimiento y participación."),
    ],
    mistakes=[
        M("Proponer mostrar algo de una comunidad sin consultarla.", "Una propuesta no puede decidir por la comunidad.", "Invita, pide permiso y reconoce a quien lo creó."),
        M("Concluir que todas las comunidades viven como la del testimonio.", "Un testimonio no representa a todos los pueblos.", "Escribe «según don Mateo, en Lago Espejo…»."),
    ],
    R=[
        ex("¿Con qué frase atribuyes un dato a don Mateo? A) «Todos saben que…» B) «Don Mateo cuenta que…»", "B", "Nombra a la fuente."),
        ex("Tema: el encuentro de culturas. ¿Cuántas partes tiene la respuesta atribuida de esta clase? Escribe el número.", "5", "Son dato, encuentro de culturas, reflexión con pregunta, límite y propuesta."),
        ex("Tema: el encuentro de culturas. Verdadero o falso: mi reflexión es una idea mía y no del testimonio.", "Verdadero", "Por eso se marca como mía."),
    ],
    C=[
        ex("¿Qué es una propuesta intercultural? A) una orden para una comunidad B) una idea concreta para que las culturas se encuentren con respeto", "B", "Invita; no ordena."),
        ex("Verdadero o falso: una propuesta puede decidir por la comunidad qué mostrar.", "Falso", "La comunidad decide qué comparte."),
        ex("Tema: el encuentro de culturas. ¿Para qué sirve el límite? A) para decir qué no sé ni se cuenta B) para ocultar errores", "A", "El límite muestra hasta dónde llega lo afirmado."),
    ],
    A=[
        ex("Don Mateo dice: «Mi nieta va a la feria de la ciudad vecina». Completa la atribución: «Don Mateo cuenta que su nieta…»", "Va a la feria de la ciudad vecina", "Se repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) don Mateo cuenta que cuidan el lago como lo aprendieron de los mayores b) yo pienso que eso une a la familia.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        ex("Una propuesta dice: «Hagamos una feria donde cada comunidad presente lo que quiera, con su permiso y nombrando a quien lo creó». ¿Qué cumple? A) permiso y reconocimiento B) apropiación", "A", "La propuesta incluye permiso y nombrar a quien lo creó."),
    ],
    Z=[
        ex("Marta escribe una propuesta sin límite. ¿Qué mejoraría? A) agregar más datos inventados B) agregar lo que no sé o no decide la comunidad", "B", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu respuesta al educador tradicional? A) porque conoce la cultura y puede corregir errores B) porque es una tarea de decoración", "A", "Quien conoce su cultura puede corregir lo equivocado."),
    ],
    D=[
        ex("Dos reflexiones. 1) «Don Mateo cuenta que su nieta combina música del mundo y aprendizajes del lago; yo pienso que puede aprender de ambas». 2) «Las comunidades indígenas deben dejar sus costumbres para modernizarse». ¿Cuál está bien construida?", "La primera", "La segunda ordena culturas y propone asimilación."),
        ex("Un compañero agrega una celebración que, según él, «seguro hacen» en Lago Espejo. El testimonio no la menciona. ¿Qué debe hacer?", "Quitarla porque no está en la fuente", "Lo que la fuente no dijo no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre cómo conviven la música del mundo y los saberes del lago en la familia de Camila. ¿Qué empieza mejor? A) «Todos los pueblos indígenas piensan que…» B) «Don Mateo cuenta que…»", "B", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cinco partes de una respuesta atribuida sobre la relación entre culturas.", "Dato de la fuente, encuentro de culturas, reflexión con pregunta, límite y propuesta", "Están en la explicación."),
        ex("Verdadero o falso: puedo escribir una propuesta que decida por la comunidad.", "Falso", "Solo puede invitar."),
        ex("Tema: el encuentro de culturas. ¿Qué haces al terminar? A) mostrarlo a la comunidad o al educador para que lo revise B) guardarlo sin mostrarlo", "A", "Es la devolución."),
    ],
    task=T("Usa este testimonio inventado de don Mateo: «En mi comunidad, los jóvenes conocen canciones y videos de todo el mundo. En la feria de la ciudad vecina compran y venden con otras personas. Yo creo que lo importante es que no dejen de aprender a cuidar el lago.» Escribe una respuesta de cinco partes: 1) dato de don Mateo, 2) qué culturas se encuentran, 3) tu reflexión con «yo pienso que» y una pregunta, 4) un límite y 5) una propuesta intercultural que invite sin decidir por la comunidad.",
           "1) Don Mateo cuenta que los jóvenes conocen canciones del mundo y que quiere que sigan aprendiendo a cuidar el lago. 2) Se encuentran la cultura global, la cultura de la comunidad y el entorno de la feria. 3) Yo pienso que pueden aprender de todas; ¿cómo puede la escuela apoyarlos? 4) No sé qué opinan los jóvenes. 5) Propongo invitar a la comunidad a una feria donde decida qué compartir, con su permiso.",
           ["atribuye cada dato", "formula una pregunta que problematiza", "propone sin decidir por la comunidad"], ["texto de cinco partes"], ["generalizar a todos los pueblos", "proponer sin permiso"],
           "Pedir que señale la línea del testimonio que respalda su reflexión."),
    reinforce="Numera del 1 al 5 las partes de tu respuesta para comprobar que están todas.",
    extend="Reescribe tu propuesta para que incluya a una cultura del entorno que no aparece en el testimonio, con permiso de quienes la comparten.",
)

# ------------------------------------------------------------------ OA 10
FPA = ("Ficha situada (inventada). Comunidad: Pampa Alta (no es un pueblo real). Territorio: una llanura alta, una vertiente y cerros cercanos. "
       "Fuente y responsable: doña Carmen, vecina de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Carmen autorizó usar esta ficha en la escuela. "
       "Límite: no se cuentan los relatos que la comunidad reserva.")
TPA = ("Testimonio inventado de doña Carmen, de Pampa Alta: «Para mí el agua no es de una sola persona. Es de todos y hay que cuidarla porque nos cuida a nosotros. "
       "Los mayores dicen que cada cosa tiene su lugar y que se vive mejor cuando uno no toma más de lo que necesita.»")
TVP = ("Testimonio inventado de don Hernán, de Villa del Puerto (familia de pescadores de una ciudad, no indígena): «Para mí el mar es mi trabajo y la comida de mi casa. "
       "Mi padre me enseñó a respetarlo, porque si uno lo trata mal, el mar no da. Pesco solo lo que puedo vender en el día.»")

L(
    OA10, 1, materials=MAT,
    use="Aprenderé a situar una concepción de mundo: de qué comunidad es, quién la cuenta y qué sentido le da a las cosas. Sirve para valorar distintas formas de entender el mundo sin mezclarlas ni inventar.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que cada comunidad cuenta su vida a su manera."],
    explain=[
        "La concepción de mundo, también llamada cosmovisión o visión de mundo, es la manera en que un pueblo entiende el mundo: qué es la naturaleza, cómo se relacionan las personas con ella y qué lugar tiene cada cosa. Los pueblos indígenas de Chile tienen distintas concepciones de mundo, y otras culturas también tienen la suya.",
        "Cada cultura da sentido a lo que vive. La significación es el sentido que una cultura le da a algo, como el agua, el trabajo o un lugar. La misma cosa puede tener significaciones distintas: el agua puede ser un recurso, un compañero o una responsabilidad compartida. Para valorar una concepción de mundo, hay que entenderla desde sus propias significaciones.",
        "Antes de reflexionar hay que situar. Una ficha situada dice la comunidad, el territorio, la fuente, el permiso y el límite. Con ella sabemos de quién es la visión y qué no se cuenta. Lo que dice una ficha vale para esa comunidad y no para todos los pueblos.",
    ],
    vocab=[("concepción de mundo", "manera en que un pueblo entiende el mundo y la vida; también se llama cosmovisión"), ("significación", "sentido que una cultura le da a algo"), ("cosmovisión", "otro nombre para la concepción de mundo"), ("fuente", "persona o texto que entrega el dato"), ("límite", "lo que no se cuenta o no se sabe")],
    worked=[
        W("Leer una ficha situada", FPA + " ¿De quién es la visión y qué no se cuenta?", ["La comunidad es Pampa Alta y la fuente es doña Carmen.", "Ella dio permiso para usar la ficha en la escuela.", "El límite dice que no se cuentan los relatos reservados."], "La visión es de doña Carmen, de Pampa Alta; no se cuentan los relatos que la comunidad reserva."),
        W("Distinguir significaciones", "Doña Carmen dice: «El agua es de todos y hay que cuidarla». Un vendedor dice: «El agua es un producto que vendo». ¿Qué muestran?", ["Para doña Carmen el agua es algo compartido que se cuida.", "Para el vendedor es un producto.", "Cada uno le da un sentido distinto al agua."], "Muestran dos significaciones distintas del agua."),
    ],
    mistakes=[
        M("Pensar que hay una sola concepción de mundo para todos los pueblos.", "Cada pueblo y cada cultura tiene la suya.", "Nombra la comunidad y la fuente de cada visión."),
        M("Decir que la visión de una comunidad es «la de todos los pueblos indígenas».", "La ficha habla de una sola comunidad.", "Escribe «según doña Carmen, en Pampa Alta…»."),
    ],
    R=[
        ex("Según la ficha de Pampa Alta, ¿quién es la fuente?", "Doña Carmen", "La ficha la nombra como fuente y responsable."),
        ex("¿Qué territorio tiene Pampa Alta? A) un lago y un bosque B) una llanura alta, una vertiente y cerros cercanos", "B", "El lago y el bosque son de otra ficha."),
        ex("La ficha de Pampa Alta dice que no se cuentan los relatos reservados. ¿Los escribes en tu trabajo? Responde Sí o No.", "No", "El límite lo prohíbe."),
    ],
    C=[
        ex("En Lengua y Cultura, ¿qué es una concepción de mundo? A) la manera en que un pueblo entiende el mundo y la vida B) un mapa del país", "A", "Es su forma de entender la naturaleza y la vida."),
        ex("Verdadero o falso: la significación es el sentido que una cultura le da a algo.", "Verdadero", "Esa es la definición de significación."),
        ex("Verdadero o falso: la concepción de mundo de una comunidad vale para todos los pueblos indígenas.", "Falso", "Cada pueblo tiene la suya."),
    ],
    A=[
        ex("Doña Carmen dice: «El agua es de todos y hay que cuidarla porque nos cuida». ¿Qué significación le da al agua? A) algo compartido que se cuida B) un producto para vender", "A", "La frase muestra una responsabilidad compartida."),
        ex("Una ficha dice: «Comunidad: Pampa Alta. Fuente: doña Carmen. Permiso: no consta». ¿Puedes usarla? Responde Sí o No.", "No", "Sin permiso no se sabe si se puede compartir."),
        ex("Clasifica en DATO DE LA FICHA o IDEA MÍA: a) el territorio incluye una vertiente b) seguro la vertiente es sagrada.", "a dato de la ficha, b idea mía", "La ficha no dice nada de lo sagrado."),
    ],
    Z=[
        ex("Joaquín dice: «Como doña Carmen cuida el agua, todos los pueblos indígenas ven el agua igual». ¿Qué error comete?", "Generaliza una ficha a todos los pueblos", "Una comunidad no representa a todos los pueblos."),
        ex("Un compañero afirma, sin mostrar ninguna ficha: «En Pampa Alta cuidan la vertiente porque le tienen miedo». ¿Por qué no es válido? A) porque es demasiado corto B) no hay fuente que lo diga", "B", "Sin fuente no se puede afirmar nada sobre una comunidad."),
    ],
    D=[
        ex("Hay dos significaciones del agua. Pampa Alta: «es de todos y se cuida». Un vendedor del ejemplo: «es un producto». ¿Cuál es la significación de Pampa Alta?", "Que es de todos y se cuida", "Es lo que dice la ficha de esa comunidad."),
        ex("Tema: las concepciones de mundo. Una ficha trae comunidad y territorio, pero no dice quién es la fuente ni si hay permiso. ¿Qué haces primero? A) usarla igual B) pedir los datos que faltan", "B", "Sin fuente y permiso se detiene la actividad hasta completarlos."),
    ],
    context=[ex("Tu profesora te da un relato breve sobre cómo una comunidad entiende un lugar, pero no dice quién lo contó. Antes de usarlo, ¿qué haces? A) lo uso porque parece interesante B) pregunto quién lo contó y si autorizó compartirlo", "B", "Un relato sin fuente ni permiso no se usa.")],
    selfcheck=[
        ex("Escribe dos datos que debe tener una ficha situada.", "Dos entre: comunidad, fuente, permiso, límite", "Son los datos que permiten situar la visión."),
        ex("Verdadero o falso: otra cultura, no indígena, también tiene su propia concepción de mundo.", "Verdadero", "Todas las culturas dan sentido al mundo a su manera."),
        ex("Tema: las concepciones de mundo. ¿Qué haces ante una duda sobre una comunidad real? A) lo imagino B) pregunto al educador tradicional o a la comunidad", "B", "Ellos son la fuente."),
    ],
    task=T("Lee esta nota inventada de doña Carmen, de Pampa Alta: «Mi comunidad vive en una llanura alta. La vertiente es de todos y la cuidamos por turnos. De los relatos antiguos no hablamos con visitas.» Haz una ficha con: comunidad, territorio, fuente, qué dice la fuente y un límite. Después escribe una frase con «Yo pienso que…» sobre qué sentido le da la comunidad a la vertiente.",
           "Comunidad: Pampa Alta. Territorio: llanura alta con vertiente. Fuente: doña Carmen. Dice: la vertiente es de todos y se cuida por turnos. Límite: no se cuentan los relatos antiguos. Yo pienso que para la comunidad la vertiente es algo compartido que hay que cuidar.",
           ["completa la ficha con datos de la nota", "separa lo que dice la fuente de lo que piensa", "pone un límite"], ["ficha completa", "frase con «Yo pienso que»"], ["agregar datos que la nota no dice", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea de la nota está cada dato; valorar que separe la fuente de su opinión."),
    reinforce="Subraya en la ficha de Pampa Alta la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué una misma cosa, como el agua, puede tener significaciones distintas en dos culturas.",
)

L(
    OA10, 2, materials=MAT,
    use="Aprenderé a escuchar o leer una concepción de mundo con límites declarados: qué dice la fuente, qué sentido le da a las cosas, qué interpreto yo y qué no se cuenta.",
    prior=["Sé situar una comunidad con su ficha.", "Sé qué es una significación."],
    explain=[
        "Para valorar una concepción de mundo hay que escucharla o leerla sin cambiarla. Separamos cuatro cosas. Lo que la fuente dice, con sus propias palabras. La significación que da a lo que nombra, como el agua o el trabajo. Lo que yo interpreto, que es una idea mía. Y lo que no se cuenta o no sé.",
        "En el testimonio de doña Carmen aparecen dos ideas: el agua es de todos y se vive mejor cuando uno no toma más de lo que necesita. Esas ideas pertenecen a esa fuente y esa comunidad. Si yo agrego que «para ella todo es sagrado», ya no estoy leyendo lo que dijo, estoy sumando algo que nadie dijo.",
        "También escuchamos con límites: hay relatos que la comunidad reserva y no corresponde pedirlos ni inventarlos. Cerramos con una frase que dice hasta dónde llega lo que afirmamos. Si queremos saber más sobre la visión de mundo de un pueblo real, preguntamos al educador o a la educadora tradicional.",
    ],
    vocab=[("significación", "sentido que una cultura le da a algo"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("atribuir", "decir de quién viene una idea"), ("reservado", "lo que una comunidad prefiere no compartir con todos"), ("límite", "lo que no se cuenta o no se sabe")],
    worked=[
        W("Separar cuatro cosas", TPA + " Separa lo que dice, la significación, lo que interpreto y lo que no se cuenta.", ["Dice: el agua es de todos y hay que cuidarla porque nos cuida.", "Significación: el agua es algo compartido y con lo que se tiene una relación de cuidado.", "Interpreto: yo pienso que doña Carmen quiere que nadie se quede sin agua.", "No se cuenta: cómo se reparte el agua entre las familias."], "Dice: el agua es de todos. Significación: algo compartido y cuidado. Interpreto: que nadie se quede sin agua. No se cuenta: cómo se reparte."),
        W("Detectar una exageración", "Un niño escribe: «Doña Carmen cuenta que para su comunidad todo en la naturaleza es sagrado». ¿Está bien?", ["Reviso el testimonio: habla del agua y de no tomar más de lo necesario.", "No dice que todo sea sagrado.", "La frase del niño agrega algo que la fuente no dijo."], "No: agrega «todo es sagrado», que doña Carmen no dijo."),
    ],
    mistakes=[
        M("Escribir mi interpretación como si la hubiera dicho la fuente.", "Se atribuye a la comunidad algo que no dijo.", "Marca mis ideas con «yo pienso que»."),
        M("Completar con ideas lo que la comunidad reserva.", "Lo reservado se respeta; inventarlo puede ser falso e irrespetuoso.", "Escribe «el testimonio no lo dice»."),
    ],
    R=[
        ex("Según doña Carmen, ¿de quién es el agua: de una sola persona o de todos?", "De todos", "El testimonio dice que el agua es de todos."),
        ex("Tema: las concepciones de mundo. Una interpretación, ¿es una idea mía o un dato de la fuente?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Si el testimonio no dice cómo se reparte el agua, ¿qué escribes? A) el testimonio no lo dice B) se reparte por sorteo", "A", "No se inventan datos."),
    ],
    C=[
        ex("Doña Carmen dice: «Se vive mejor cuando uno no toma más de lo que necesita». ¿Qué idea expresa? A) tomar solo lo necesario B) tomar todo lo que se pueda", "A", "La frase habla de tomar solo lo que se necesita."),
        ex("Verdadero o falso: lo que yo interpreto puede escribirse como si lo hubiera dicho la fuente.", "Falso", "Hay que marcarlo con «yo pienso que»."),
        ex("Verdadero o falso: respetar lo que la comunidad reserva es parte de valorar su concepción de mundo.", "Verdadero", "Cuidar lo reservado muestra respeto."),
    ],
    A=[
        ex("Doña Carmen dice: «Los mayores dicen que cada cosa tiene su lugar». Clasifica en DICE LA FUENTE o INTERPRETO: a) cada cosa tiene su lugar b) en Pampa Alta todo está muy ordenado.", "a dice la fuente, b interpreto", "La segunda es una deducción de quien lee."),
        ex("Un niño lee el testimonio de doña Carmen y escribe: «Para su comunidad la naturaleza es sagrada». ¿Qué dato no está en el testimonio?", "Que la naturaleza es sagrada", "El testimonio habla del agua compartida y de tomar lo necesario."),
        ex("Don Hernán, de Villa del Puerto, dice: «Mi padre me enseñó a respetar el mar, porque si uno lo trata mal, el mar no da». ¿Qué significación le da al mar? A) un lugar de fiesta B) sustento que hay que respetar", "B", "La frase habla de trabajo y de respeto."),
    ],
    Z=[
        ex("Rodrigo escribe, sin marcarlo: «Las personas de Pampa Alta son más sabias que las de las ciudades». ¿Qué debería hacer con esa frase?", "Quitarla porque ordena culturas y no está en la fuente", "No está en el testimonio y jerarquiza."),
        ex("Tema: las concepciones de mundo. ¿Por qué conviene escribir los límites al final de un trabajo? A) para mostrar hasta dónde llega lo afirmado B) para llenar la hoja", "A", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        ex("Dos frases. 1) «Doña Carmen dice que el agua es de todos y hay que cuidarla». 2) «Doña Carmen dice que quien contamina el agua es malo». Testimonio: «el agua es de todos y hay que cuidarla porque nos cuida». ¿Cuál se queda en la fuente?", "La primera", "La segunda agrega un juicio que doña Carmen no dijo."),
        ex("Doña Carmen no contó cómo se reparte el agua. ¿Qué escribes en los límites? A) no sé cómo se reparte el agua B) se reparte por turnos de una semana", "A", "Declarar lo que no sé evita inventar."),
    ],
    context=[ex("Para un afiche escolar, un compañero quiere dibujar un ritual del agua que «seguro hacen en Pampa Alta». El testimonio y la ficha no hablan de ningún ritual. ¿Qué le dices? A) que no lo dibuje porque no está en la fuente B) que lo dibuje con detalles", "A", "No se inventan prácticas que la fuente no cuenta.")],
    selfcheck=[
        ex("Nombra las cuatro cosas que separo al escuchar o leer una concepción de mundo.", "Lo que dice la fuente, la significación, lo que interpreto y lo que no se cuenta", "Son los pasos de la lectura con límites."),
        ex("Tema: las concepciones de mundo. Verdadero o falso: puedo completar con mi imaginación lo que la comunidad no contó.", "Falso", "Eso sería inventar."),
        ex("Tema: las concepciones de mundo. ¿Qué escribes cuando el testimonio no explica algo? Escribe una frase corta.", "El testimonio no lo dice", "Es la manera honesta de marcar un vacío."),
    ],
    task=T("Lee este testimonio inventado de doña Carmen: «Cuando vamos al cerro, tomamos solo la leña seca que necesitamos. Mi abuela decía que lo que uno se lleva se debe agradecer cuidando el lugar. De las historias del cerro no hablamos con visitas.» Haz tres columnas: «La fuente dice», «Yo interpreto» y «No se cuenta». Pon al menos dos datos en cada una. Cierra con una frase de límites.",
           "La fuente dice: toman solo la leña seca que necesitan; lo que se lleva se agradece cuidando el lugar. Yo interpreto: yo pienso que cuidar el cerro es una forma de devolver lo que se toma. No se cuenta: las historias del cerro. Límite: no sé cómo se cuida el lugar en la práctica.",
           ["separa tres columnas", "usa datos del testimonio", "marca sus ideas como interpretación"], ["tabla de tres columnas", "frase de límites"], ["escribir interpretaciones como datos", "inventar lo reservado"],
           "Pedir que indique en qué línea del testimonio está cada dato; valorar que deje sin completar lo no contado."),
    reinforce="Subraya con un color lo que dice la fuente y con otro lo que interpretas en el testimonio de doña Carmen.",
    extend="Explica por qué callar unas historias puede ser una manera de cuidarlas, usando el testimonio de doña Carmen.",
)

L(
    OA10, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre la significación que una cultura da a las cosas y lo que hace en su vida, comparando una comunidad indígena inventada con otra cultura, sin decir que una es mejor.",
    prior=["Sé separar lo que dice la fuente de lo que interpreto.", "Sé qué es una significación."],
    explain=[
        "Una relación cultural une una idea con una práctica. Por ejemplo: la idea de que el agua es de todos se relaciona con la práctica de cuidar la vertiente por turnos. La idea de que el mar da si se lo respeta se relaciona con pescar solo lo que se puede vender en el día. Siempre decimos que es una relación que la fuente nombra o que yo propongo.",
        "Comparamos dos testimonios inventados: el de doña Carmen, de Pampa Alta, y el de don Hernán, de Villa del Puerto, una familia de pescadores de ciudad. Hay semejanzas: ambos hablan de respeto y de tomar solo lo necesario. Y hay diferencias: una comunidad habla del agua compartida y la otra, del mar como sustento y trabajo.",
        "Para comparar usamos los mismos criterios: qué cosa nombra la fuente, qué sentido le da y qué práctica cuenta. No ordenamos las culturas de «más sabia» a «menos sabia». Y dos testimonios no bastan para decir que todos los pueblos o todas las familias de pescadores piensan igual.",
    ],
    vocab=[("relación cultural", "unión entre una idea y una práctica de una cultura"), ("práctica", "lo que las personas hacen en su vida diaria"), ("semejanza", "algo parecido entre dos fuentes"), ("diferencia", "algo distinto entre dos fuentes"), ("criterio", "punto de comparación igual para los dos casos")],
    worked=[
        W("Relacionar idea y práctica", TPA + " ¿Qué relación hay entre una idea y una práctica?", ["Idea: el agua es de todos y hay que cuidarla.", "Práctica que ella cuenta en otra nota (inventada): la comunidad cuida la vertiente por turnos.", "Entonces la idea de compartir se ve en el cuidado por turnos."], "La idea de que el agua es de todos se relaciona con cuidar la vertiente por turnos."),
        W("Comparar con un criterio", TVP + " Criterio: «qué respeto muestra la fuente». Doña Carmen: tomar solo lo necesario. Don Hernán: respetar el mar porque si no, no da. ¿Qué semejanza hay?", ["Doña Carmen habla de tomar solo lo necesario.", "Don Hernán habla de respetar el mar.", "Las dos fuentes muestran respeto por lo que les da la naturaleza."], "Semejanza: ambas fuentes muestran respeto por lo que les da la naturaleza."),
    ],
    mistakes=[
        M("Decir que una concepción de mundo es más sabia que la otra.", "Comparar no es ordenar de más sabia a menos sabia.", "Describe semejanzas y diferencias con los mismos criterios."),
        M("Concluir que todos los pueblos y todos los pescadores piensan igual porque dos testimonios se parecen.", "Dos ejemplos no representan a todos.", "Escribe «en estos dos testimonios» y no más."),
    ],
    R=[
        ex("Doña Carmen cuenta: «La vertiente la cuidamos por turnos». ¿Quién cuida la vertiente: una empresa o las familias por turnos?", "Las familias por turnos", "Así lo cuenta doña Carmen."),
        ex("Don Hernán dice: «Pesco solo lo que puedo vender en el día». ¿Cuánto pesca: todo lo que puede o solo lo que vende en el día?", "Solo lo que vende en el día", "El testimonio lo dice así."),
        ex("¿Qué testimonio habla del mar: el de doña Carmen o el de don Hernán?", "El de don Hernán", "Doña Carmen habla del agua y del cerro."),
    ],
    C=[
        ex("Verdadero o falso: comparar dos concepciones de mundo significa decir cuál es más sabia.", "Falso", "Comparar es buscar semejanzas y diferencias."),
        ex("¿Qué es una relación cultural? A) un parentesco entre dos personas B) la unión entre una idea y una práctica de una cultura", "B", "Une lo que se piensa con lo que se hace."),
        ex("Verdadero o falso: si dos testimonios se parecen, todos los pueblos piensan igual.", "Falso", "Dos testimonios no representan a todos los pueblos."),
    ],
    A=[
        ex("Criterio: «cuánto se toma de la naturaleza». Doña Carmen: solo lo necesario. Don Hernán: solo lo que vende en el día. ¿Qué semejanza hay? A) en ambos casos se toma una cantidad limitada B) en ambos se toma todo lo posible", "A", "Ambos limitan lo que toman."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) las dos fuentes hablan de respetar lo que da la naturaleza b) una habla del agua compartida y la otra del mar como trabajo.", "a semejanza, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        ex("Doña Carmen dice: «El agua es de todos». Su comunidad cuida la vertiente por turnos. ¿Qué relación puedes proponer? A) la idea de compartir se ve en el cuidado por turnos B) la idea de vender se ve en los turnos", "A", "Compartir y cuidar por turnos van juntos."),
    ],
    Z=[
        ex("Ana dice: «La visión de Pampa Alta es mejor que la de Villa del Puerto porque cuida más». ¿Qué falla en su comparación?", "Ordena dos visiones sin un criterio común", "Comparar no es jerarquizar."),
        ex("Un compañero escribe: «Como estos dos testimonios hablan de respeto, todos los pueblos piensan lo mismo». ¿Qué debería escribir? A) «en estos dos testimonios» B) «en todos los pueblos»", "A", "Dos testimonios no permiten hablar de todos los pueblos."),
    ],
    D=[
        ex("Don Hernán no dijo si su familia agradece al mar de alguna forma. Alguien escribe que sí lo hace, con una ceremonia. ¿Qué parte es interpretación? A) nada, porque es posible B) toda la frase, porque el testimonio no lo dice", "B", "Lo que la fuente no dice no se agrega."),
        ex("Dos conclusiones. 1) «Doña Carmen y don Hernán muestran respeto por lo que les da la naturaleza». 2) «Los pescadores respetan menos que los pueblos indígenas». ¿Cuál está bien formulada?", "La primera", "La segunda ordena a dos grupos."),
    ],
    context=[ex("Tu curso arma un panel con dos formas de entender la naturaleza. Una compañera quiere titularlo «Los pueblos indígenas sí saben cuidar y los demás, no». ¿Qué título respeta lo aprendido? A) «La mejor forma de vivir» B) «Dos formas de respetar lo que da la naturaleza»", "B", "El título A compara sin jerarquizar.")],
    selfcheck=[
        ex("Escribe una relación entre una idea y una práctica con el testimonio de doña Carmen.", "El agua es de todos y se cuida por turnos", "Une la idea con la práctica."),
        ex("Verdadero o falso: puedo ordenar dos culturas de «más sabia» a «menos sabia».", "Falso", "Cada cultura da sentido al mundo a su manera."),
        ex("Tema: las concepciones de mundo. Nombra un criterio de comparación para dos testimonios.", "Por ejemplo: cuánto se toma de la naturaleza", "Debe ser un punto igual para ambos."),
    ],
    task=T("Compara estos dos testimonios inventados. Doña Carmen, de Pampa Alta: «El agua es de todos y se cuida por turnos». Don Hernán, de Villa del Puerto: «El mar es mi trabajo; lo respeto y pesco solo lo que vendo en el día». Haz una tabla con tres criterios: «qué cosa nombra la fuente», «qué sentido le da» y «qué práctica cuenta». Escribe una semejanza, una diferencia y una frase que termine con «en estos dos testimonios».",
           "Cosa: el agua; el mar. Sentido: algo compartido que se cuida; el trabajo y sustento que se respeta. Práctica: cuidar la vertiente por turnos; pescar solo lo que se vende en el día. Semejanza: ambos toman solo lo necesario. Diferencia: uno habla de algo compartido y el otro, de trabajo. Esto se ve en estos dos testimonios.",
           ["usa los mismos criterios para ambos", "distingue semejanza y diferencia", "no jerarquiza"], ["tabla de tres criterios", "semejanza y diferencia"], ["decir cuál visión es mejor", "generalizar a todos los pueblos"],
           "Pedir que muestre en la tabla la fila que respalda cada semejanza; valorar que no ordene las visiones."),
    reinforce="Marca en la tabla con un color las semejanzas y con otro las diferencias.",
    extend="Agrega un cuarto criterio (por ejemplo, «a quién enseñaron esa idea») y explica qué deberías preguntar para completarlo.",
)

L(
    OA10, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida que valore una concepción de mundo desde sus propias significaciones, con fuente, reflexión, límite y pregunta.",
    prior=["Sé relacionar una idea con una práctica.", "Sé comparar dos testimonios sin jerarquizar."],
    explain=[
        "Una respuesta atribuida que valora una concepción de mundo tiene cinco partes. Primero, el dato de la fuente con su nombre: «Doña Carmen cuenta que…». Segundo, la significación que ella da a lo que nombra. Tercero, tu reflexión sobre por qué esa visión tiene sentido en su comunidad, marcada con «yo pienso que». Cuarto, un límite. Quinto, una pregunta para el educador o la educadora tradicional.",
        "Valorar una concepción de mundo no es estar de acuerdo con todo ni imitarla. Es reconocer que tiene sentido para quienes la viven y que da un orden a su vida. Por eso explicamos las ideas desde sus propias significaciones: no decimos que «están equivocadas» porque no coinciden con las nuestras.",
        "Una buena respuesta no exagera, no suma ideas que la fuente no dijo y no habla por todo un pueblo. Reconoce lo que no sabe y lo que la comunidad reserva. Al final se devuelve a la comunidad o al educador, para que la revise y corrija lo que no esté bien dicho.",
    ],
    vocab=[("valorar", "reconocer que algo tiene importancia y sentido para quienes lo viven"), ("significación", "sentido que una cultura le da a algo"), ("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("exagerar", "decir más de lo que la fuente dijo"), ("devolución", "mostrar el trabajo a la comunidad o al educador para que lo revisen")],
    worked=[
        W("Armar una respuesta", TPA + " Arma una respuesta atribuida de cinco partes.", ["Dato: doña Carmen cuenta que el agua es de todos y hay que cuidarla.", "Significación: para ella el agua es algo compartido con lo que se tiene una relación de cuidado.", "Reflexión: yo pienso que esa visión ayuda a que la comunidad cuide el agua entre todos.", "Límite y pregunta: no sé cómo se reparte el agua; preguntaré al educador tradicional."], "Respuesta con dato atribuido, significación, «yo pienso que», límite y pregunta."),
        W("Revisar una respuesta", "Una niña escribe: «Los pueblos indígenas creen en cosas falsas sobre el agua». ¿Qué le falta a la respuesta?", ["No dice de qué fuente viene el dato.", "Juzga como falsa una visión sin entenderla.", "Generaliza a todos los pueblos."], "Le falta atribuir, valorar desde las significaciones propias y no generalizar."),
    ],
    mistakes=[
        M("Decir que la visión de una comunidad está equivocada porque no coincide con la mía.", "Cada visión se entiende desde sus propias significaciones.", "Explica qué sentido tiene para quienes la viven."),
        M("No marcar qué parte es opinión mía.", "El lector no distingue la voz de la comunidad de la mía.", "Usa «yo pienso que…»."),
    ],
    R=[
        ex("¿Con qué frase atribuyes un dato a doña Carmen? A) «Todos saben que…» B) «Doña Carmen cuenta que…»", "B", "Nombra a la fuente."),
        ex("Tema: las concepciones de mundo. ¿Cuántas partes tiene la respuesta atribuida de esta clase? Escribe el número.", "5", "Son dato, significación, reflexión, límite y pregunta."),
        ex("Tema: las concepciones de mundo. Verdadero o falso: mi reflexión es una idea mía y no del testimonio.", "Verdadero", "Por eso se marca como mía."),
    ],
    C=[
        ex("¿Qué significa valorar una concepción de mundo? A) estar de acuerdo con todo sin revisar B) reconocer que tiene sentido para quienes la viven", "B", "Valorar no es aceptar sin pensar."),
        ex("Verdadero o falso: valorar una visión de mundo significa decir que las demás están equivocadas.", "Falso", "Se valora sin ordenar ni descartar a las demás."),
        ex("Tema: las concepciones de mundo. ¿Para qué sirve la pregunta final? A) para terminar rápido B) para consultar al educador tradicional lo que no sé", "B", "La pregunta señala lo que se debe consultar."),
    ],
    A=[
        ex("Testimonio de doña Carmen: «Los mayores dicen que cada cosa tiene su lugar». Completa la atribución: «Doña Carmen cuenta que los mayores dicen que…»", "Cada cosa tiene su lugar", "Se repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) doña Carmen cuenta que se vive mejor cuando no se toma más de lo necesario b) yo pienso que esa idea ayuda a cuidar el agua entre todos.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        ex("Una reflexión dice: «Don Hernán cuenta que respeta el mar porque da; yo pienso que su trabajo le enseñó a cuidarlo». ¿Qué parte es la reflexión?", "Yo pienso que su trabajo le enseñó a cuidarlo", "Es la idea de quien escribe."),
    ],
    Z=[
        ex("Tema: las concepciones de mundo. Marta escribe una respuesta sin límite. ¿Qué mejoraría? A) agregar lo que no sé o no se cuenta B) agregar más datos inventados", "A", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu respuesta al educador tradicional? A) porque conoce la visión de su pueblo y puede corregir errores B) porque es una tarea de decoración", "A", "Quien conoce su cultura puede corregir lo equivocado."),
    ],
    D=[
        ex("Dos reflexiones. 1) «Doña Carmen cuenta que el agua es de todos; yo pienso que eso ayuda a cuidarla entre todos». 2) «Doña Carmen demuestra que los pueblos indígenas cuidan mejor que nadie». ¿Cuál está bien construida?", "La primera", "La segunda exagera y jerarquiza."),
        ex("Un compañero agrega a su respuesta una creencia que, según él, «seguro tiene» la comunidad. El testimonio no la menciona. ¿Qué debe hacer?", "Quitarla porque no está en la fuente", "Lo que la fuente no dijo no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre cómo entiende el agua la comunidad de Pampa Alta. ¿Qué empieza mejor? A) «Todos los pueblos indígenas creen que…» B) «Doña Carmen cuenta que…»", "B", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cinco partes de una respuesta atribuida sobre una concepción de mundo.", "Dato de la fuente, significación, reflexión, límite y pregunta", "Están en la explicación."),
        ex("Tema: las concepciones de mundo. Verdadero o falso: debo marcar qué parte es mi opinión.", "Verdadero", "Así no se confunde con la fuente."),
        ex("Tema: las concepciones de mundo. ¿Qué haces al terminar? A) guardarlo sin mostrarlo B) mostrarlo a la comunidad o al educador para que lo revise", "B", "Es la devolución."),
    ],
    task=T("Usa este testimonio inventado de doña Carmen: «Antes de sembrar, las familias se juntan a limpiar el canal de la vertiente. Mi abuelo decía que si cuidamos el agua, el agua nos cuida. De los relatos antiguos no hablamos con visitas.» Escribe una respuesta de cinco partes sobre cómo entiende el agua la comunidad de Pampa Alta: 1) dato de doña Carmen, 2) la significación que le da al agua, 3) tu reflexión con «yo pienso que», 4) un límite y 5) una pregunta para el educador tradicional.",
           "1) Doña Carmen cuenta que las familias limpian juntas el canal antes de sembrar y que su abuelo decía que si cuidan el agua, el agua los cuida. 2) Para ella el agua es algo con lo que se tiene una relación de cuidado mutuo. 3) Yo pienso que esa idea une a las familias en el trabajo. 4) No sé cuándo empezó esta costumbre. 5) Pregunta: ¿cómo explica mi pueblo la relación entre las personas y el agua?",
           ["atribuye cada dato", "explica desde las significaciones de la fuente", "incluye límite y pregunta"], ["texto de cinco partes"], ["generalizar a todos los pueblos", "no marcar la opinión propia"],
           "Pedir que señale la línea del testimonio que respalda su reflexión."),
    reinforce="Numera del 1 al 5 las partes de tu respuesta para comprobar que están todas.",
    extend="Reescribe tu respuesta con el testimonio de don Hernán, de Villa del Puerto, y su forma de entender el mar.",
)

L(
    OA10, 5, materials=MAT,
    use="Aprenderé a contrastar concepciones de mundo sin jerarquizarlas: compararlas con los mismos criterios y evitar el error de juzgar a otra cultura desde la propia como si fuera la mejor.",
    prior=["Sé armar una respuesta atribuida.", "Sé comparar dos testimonios con criterios iguales."],
    explain=[
        "Contrastar es poner dos o más visiones una al lado de la otra para ver en qué coinciden y en qué se diferencian. Sin jerarquizar quiere decir que no las ordenamos de mejor a peor ni decimos que una es más verdadera. Cada concepción de mundo tiene sentido dentro de la cultura que la vive.",
        "Un error frecuente es el etnocentrismo: juzgar a otra cultura desde la propia, como si la propia fuera la medida de todo. Por ejemplo, decir «esa forma de ver el agua es atrasada» sin conocer qué sentido tiene para quienes la viven. Para evitarlo, usamos preguntas iguales para todas las visiones y pedimos que cada fuente explique sus significaciones con sus propias palabras.",
        "Contrastar sin jerarquizar no significa que todo valga lo mismo en cualquier situación. Significa que primero entendemos cada visión desde su propia lógica y que cualquier discusión sobre decisiones prácticas, como cuánto pescar o cómo repartir el agua, se hace con respeto y con las personas involucradas. Y dos o tres testimonios no representan a todos los pueblos.",
    ],
    vocab=[("contrastar", "poner dos o más visiones juntas para ver en qué coinciden y en qué se diferencian"), ("jerarquizar", "ordenar de mejor a peor o decir que una cosa es más verdadera"), ("etnocentrismo", "juzgar a otra cultura desde la propia, como si la propia fuera la medida de todo"), ("criterio", "punto de comparación igual para todas las visiones"), ("lógica propia", "razón con que una cultura da orden y sentido a su vida")],
    worked=[
        W("Contrastar tres testimonios", "Doña Carmen (Pampa Alta): «El agua es de todos y se cuida». Don Hernán (Villa del Puerto): «El mar es mi trabajo y lo respeto». Doña Lucía (comunidad campesina inventada): «La tierra es herencia: la cuidamos para dejársela a los hijos». Criterio: «a quién se debe cuidado». ¿En qué coinciden?", ["Doña Carmen: a la comunidad y al agua.", "Don Hernán: al mar, que da el sustento.", "Doña Lucía: a la tierra y a los hijos que la heredarán.", "Las tres fuentes hablan de cuidar algo de lo que dependen."], "Coinciden en que las tres hablan de cuidar algo de lo que dependen."),
        W("Detectar etnocentrismo", "Un niño dice: «Esa forma de ver el agua es atrasada». ¿Qué error hay?", ["Juzga la visión desde la propia sin conocer su sentido.", "Ordena culturas de atrasadas a modernas.", "Debería preguntar qué sentido tiene para quienes la viven."], "Es etnocentrismo: juzga desde su propia cultura sin entender la otra."),
    ],
    mistakes=[
        M("Decir que una concepción de mundo es más atrasada o más avanzada que otra.", "Eso es jerarquizar y juzgar desde la propia cultura.", "Pregunta qué sentido tiene para quienes la viven."),
        M("Pensar que contrastar sin jerarquizar significa no opinar.", "Se puede opinar con respeto después de entender cada visión.", "Entiende primero, discute después, con las personas involucradas."),
    ],
    R=[
        ex("¿Cómo se llama juzgar a otra cultura desde la propia como si fuera la medida de todo?", "Etnocentrismo", "Esa es la definición de etnocentrismo."),
        ex("Doña Lucía dice que la tierra es herencia para los hijos. ¿Qué cuida: la tierra o el mar?", "La tierra", "Su testimonio habla de la tierra."),
        ex("Contrastar, ¿es poner visiones juntas para ver coincidencias y diferencias o es elegir la mejor?", "Poner visiones juntas para ver coincidencias y diferencias", "Contrastar no es elegir la mejor."),
    ],
    C=[
        ex("Verdadero o falso: contrastar sin jerarquizar significa que no se puede decir nada de ninguna cultura.", "Falso", "Se puede opinar con respeto después de entender cada visión."),
        ex("¿Cuál es una frase etnocéntrica? A) «Quiero entender qué sentido tiene el agua para ellos» B) «Su forma de ver el agua es atrasada»", "B", "La primera juzga desde la propia cultura."),
        ex("Verdadero o falso: para contrastar se usan preguntas iguales para todas las visiones.", "Verdadero", "Eso permite comparar con el mismo criterio."),
    ],
    A=[
        ex("Criterio: «qué sentido le da a lo que cuida». Doña Carmen: lo compartido. Don Hernán: el sustento. Doña Lucía: la herencia. ¿Cuál habla del futuro de los hijos?", "Doña Lucía", "Ella cuida la tierra para dejársela a los hijos."),
        ex("Clasifica en COINCIDENCIA o DIFERENCIA: a) las tres fuentes hablan de cuidar algo de lo que dependen b) una habla de agua, otra de mar y otra de tierra.", "a coincidencia, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        ex("Un joven dice: «El mar de don Hernán es menos importante que el agua de doña Carmen». ¿Qué falla? A) ordena sin un criterio común B) usa el nombre de ambos", "A", "Contrastar no es jerarquizar."),
    ],
    Z=[
        ex("Ana dice: «La visión de doña Lucía es más natural que la de don Hernán». ¿Qué problema tiene?", "Jerarquiza sin criterio y sin fuente", "Las fuentes no dicen que una sea más natural."),
        ex("¿Por qué conviene usar los mismos criterios para todas las visiones? A) para llenar la tabla B) para que ninguna reciba preguntas más difíciles que otra", "B", "Los criterios iguales evitan el trato desigual."),
    ],
    D=[
        ex("Una compañera concluye: «Las tres fuentes demuestran que todos los pueblos y todas las culturas piensan igual». ¿Qué debería escribir? A) «las tres fuentes coinciden en cuidar algo de lo que dependen» B) dejar la frase", "A", "Tres fuentes no representan a todos."),
        ex("Un grupo discute cuánto pescar y dice: «Decidamos sin preguntar a los pescadores, que seguro se equivocan». ¿Qué principio del contraste no respeta? A) usar criterios iguales B) las decisiones prácticas se discuten con las personas involucradas", "B", "Debe participar quien vive la situación."),
    ],
    context=[ex("En tu curso discuten cómo cuidar un río del barrio. Un compañero dice que la visión de una comunidad indígena «no sirve porque es antigua». ¿Qué le propones? A) escuchar primero qué sentido tiene y luego discutir con respeto B) ignorarla", "A", "Se entiende primero y se discute con respeto.")],
    selfcheck=[
        ex("Escribe qué es el etnocentrismo con tus palabras.", "Juzgar otra cultura desde la propia como si fuera la medida de todo", "Es el error de considerar la propia cultura como la mejor."),
        ex("Verdadero o falso: puedo ordenar dos concepciones de mundo de mejor a peor.", "Falso", "Cada cultura da sentido al mundo a su manera."),
        ex("Tema: las concepciones de mundo. Nombra un criterio de contraste para tres testimonios.", "Por ejemplo: a quién se debe cuidado", "Debe ser un punto igual para todos."),
    ],
    task=T("Contrasta estos tres testimonios inventados. Doña Carmen: «El agua es de todos y se cuida por turnos». Don Hernán: «El mar es mi trabajo; lo respeto y pesco lo que vendo en el día». Doña Lucía: «La tierra es herencia; la cuidamos para dejársela a los hijos». Haz una tabla con tres criterios: «qué cosa nombra», «qué sentido le da» y «a quién se debe cuidado». Escribe una coincidencia, una diferencia y una frase que muestre cómo evitarías el etnocentrismo.",
           "Cosa: agua, mar, tierra. Sentido: compartido, sustento, herencia. A quién se debe cuidado: a la comunidad, al mar que da, a los hijos. Coincidencia: las tres cuidan algo de lo que dependen. Diferencia: cada una da un sentido distinto. Para evitar el etnocentrismo preguntaría qué sentido tiene cada visión para quien la vive, sin ordenarlas.",
           ["usa los mismos criterios para las tres", "distingue coincidencia y diferencia", "muestra cómo evitar el etnocentrismo"], ["tabla de tres criterios", "coincidencia, diferencia y frase"], ["decir cuál visión es mejor", "juzgar desde la propia cultura"],
           "Pedir que muestre en la tabla la fila que respalda cada afirmación; valorar que no ordene las visiones."),
    reinforce="Marca en la tabla con un color las coincidencias y con otro las diferencias.",
    extend="Agrega un cuarto testimonio inventado y explica qué criterio nuevo haría falta para contrastarlo con los otros tres.",
)
