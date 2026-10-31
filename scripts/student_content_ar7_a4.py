"""Cuaderno del estudiante de 7.º básico Artes Visuales: AR07 OA 04 (interpretar manifestaciones visuales patrimoniales y contemporáneas según medio de expresión, materialidad y lenguaje visual)."""
from __future__ import annotations

from student_content_ar7_a import lesson, m, task, w
from student_lessons import arith, ex

OA4 = "AR07 OA 04"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA4, 1,
    "Una hoja, lápiz y una tabla de tres columnas dibujada por ti (Veo, Pienso, Me pregunto). Las obras que se observan son de ejemplo y están descritas en esta clase.",
    "Aprenderé a describir con precisión una manifestación visual antes de interpretarla. Sirve para que mi interpretación se apoye en lo que realmente se ve y no solo en una opinión.",
    ["Sé separar un dato que se ve de una opinión.", "Sé distinguir una manifestación patrimonial de una contemporánea."],
    [
        "Interpretar es explicar qué creo que significa una obra o qué idea comunica. Para hacerlo bien primero describo. Describir es decir lo que se ve sin juzgarlo: qué elementos hay, de qué colores y tamaños, cómo están ubicados, en qué medio está hecha y con qué material. Una descripción se puede comprobar mirando la obra; una interpretación se puede discutir, pero debe apoyarse en lo descrito.",
        "Sigo tres pasos: Veo, Pienso y Me pregunto. En «Veo» anoto datos: «una vasija ancha de color café con líneas blancas en zigzag alrededor del borde». En «Pienso» doy una interpretación con evidencia: «las líneas en zigzag parecen ondas de agua, por eso quizá se usaba para guardar agua». En «Me pregunto» anoto lo que no puedo saber solo mirando, como quién la hizo o para qué fiesta. Una manifestación patrimonial es una obra heredada y cuidada por una comunidad; una contemporánea se hace en nuestra época.",
        "Una buena interpretación usa frases como «parece», «podría» o «sugiere», porque no siempre hay una sola respuesta. Una mala interpretación afirma sin mostrar de dónde sale: «es triste» o «es una obra de poder». Cuando interpreto, cito al menos dos datos de la descripción. Así quien me lee puede comprobar si mi idea tiene sentido.",
    ],
    [("describir", "decir lo que se ve sin juzgarlo"), ("interpretar", "explicar qué creo que significa la obra, apoyado en lo que se ve"), ("evidencia", "dato que respalda una idea"), ("patrimonial", "heredada y cuidada por una comunidad"), ("contemporánea", "hecha en nuestra época")],
    [
        w("Pasar de describir a interpretar", "Obra de ejemplo: un textil bordado con hilos rojos y negros muestra una fila de figuras que se toman de las manos. Escribe Veo, Pienso y Me pregunto.", ["Veo: hilos rojos y negros, una fila de figuras, manos unidas.", "Pienso: las manos unidas sugieren unión o trabajo en comunidad.", "Me pregunto: quién lo bordó y para qué ocasión."], "Veo: figuras unidas en fila con hilos rojos y negros. Pienso: sugiere comunidad. Me pregunto: quién y para qué lo bordó"),
        w("Detectar una opinión disfrazada", "Alguien escribe: «Es una pintura aburrida que no dice nada». ¿Es una descripción?", ["«Aburrida» es una opinión.", "No dice qué colores, formas o elementos hay.", "Se corrige agregando datos."], "No: es una opinión sin datos; falta decir qué se ve"),
    ],
    [
        m("Interpretar sin describir: «esta obra muestra tristeza» sin decir por qué.", "Sin datos que la respalden, nadie puede comprobar la idea.", "Cita al menos dos elementos que ves y que sostienen tu idea."),
        m("Decir quién hizo la obra o para qué sirvió solo mirándola.", "La imagen no siempre da esos datos.", "Anótalo en «Me pregunto» hasta tener una fuente."),
    ],
    [
        ex("«Una vasija ancha, café, con líneas blancas en zigzag en el borde», ¿es descripción o interpretación?", "Descripción", "Dice lo que se ve y se puede comprobar."),
        ex("¿En qué columna anotas «No sé quién hizo esta vasija»? A. Me pregunto B. Veo.", "A", "Es algo que no se sabe mirando."),
        ex("¿Qué palabra suaviza una interpretación porque no hay una sola respuesta: «es» o «parece»?", "Parece", "Indica que es una lectura posible, no un hecho."),
    ],
    [
        ex("Obra de ejemplo: una fotografía en blanco y negro de un niño frente a un muro muy alto. ¿Cuál es una interpretación apoyada en datos? A. «El muro enorme frente al niño pequeño sugiere que algo es difícil de superar» B. «Es una foto triste, y ya».", "A", "La A usa tamaño y posición para sostener la idea."),
        ex("Obra de ejemplo: una escultura de piedra pulida con una forma redonda y una grieta al centro. Anota qué es un dato: «tiene una grieta al centro» o «es una escultura muy bonita».", "Tiene una grieta al centro", "Se puede ver y comprobar."),
        ex("Los tres pasos de la observación son Veo, Pienso y Me pregunto. ¿En cuál se escribe una interpretación?", "Pienso", "Ahí se explica lo que se cree que significa."),
    ],
    [
        ex("Obra de ejemplo: un mural con un sol amarillo gigante y personas pequeñas abajo. ¿Cuál frase es una descripción? A. «El sol amarillo ocupa gran parte del mural y las personas son pequeñas» B. «El mural es alegre y emocionante».", "A", "La A dice tamaños y colores que se comprueban; la B es una opinión."),
        ex("Obra de ejemplo: una vasija con líneas ondulantes alrededor del cuello. Una persona escribe «parece contener agua porque las líneas imitan ondas». ¿Qué evidencia usa?", "Las líneas ondulantes", "Apoya la idea con un dato visible."),
        arith("Una ficha de observación tiene 3 columnas y anotas 2 ideas en cada una. ¿Cuántas ideas anotaste?", "3*2", "Cada columna tiene 2 ideas."),
    ],
    [
        ex("Dos estudiantes miran el mismo textil, que muestra muchas figuras de colores brillantes que sostienen herramientas. Uno escribe «parece una celebración porque hay muchas figuras con colores brillantes». La otra escribe «parece un trabajo en conjunto porque las figuras tienen herramientas». ¿Ambas interpretaciones son aceptables?", "Sí", "Ambas se apoyan en datos distintos de la misma obra."),
        ex("Un estudiante escribe «esta vasija se usaba en una ceremonia de un pueblo» solo porque se ve antigua. ¿Qué error cometió?", "Afirmó algo sin evidencia", "La apariencia antigua no prueba para qué se usaba."),
    ],
    [
        ex("Obra de ejemplo: una instalación con 20 sillas vacías puestas en círculo. Elige la mejor frase de «Veo»: A. «Veinte sillas vacías en círculo» B. «Una sala triste».", "A", "Cuenta y describe lo que hay."),
        ex("Obra de ejemplo: una pintura con líneas rectas negras sobre fondo rojo. Elige la interpretación con evidencia: A. «Las líneas negras rectas sobre rojo intenso dan sensación de tensión» B. «El artista estaba enojado».", "A", "La B atribuye un estado al autor sin datos."),
    ],
    ex("Obra de ejemplo: una fotografía de una fila de zapatos pequeños en una puerta. Tres anotaciones: 1) «Hay seis pares de zapatos pequeños en fila». 2) «Parecen esperar a sus dueños». 3) «No sé de quién son». ¿Cuál va en «Veo»?", "La 1", "Es el único dato que se ve y se cuenta."),
    [
        ex("En Artes Visuales, ¿qué es describir?", "Decir lo que se ve sin juzgarlo", "Es el paso previo a interpretar."),
        ex("Verdadero o falso: una interpretación debe apoyarse en datos de la obra.", "Verdadero", "Con evidencia se puede comprobar la idea."),
        ex("¿Cuántos datos conviene citar al menos al interpretar?", "Dos", "Así la idea tiene respaldo."),
    ],
    task(
        "Elige UNA obra de ejemplo. A) Un textil bordado con hilos rojos y negros: una fila de figuras que se toman de las manos. B) Una fotografía en blanco y negro de un niño pequeño frente a un muro altísimo. C) Una vasija café con líneas blancas en zigzag en el borde. Haz una tabla Veo, Pienso y Me pregunto con al menos tres datos, una interpretación que cite dos de ellos y dos preguntas.",
        "Elegí la B. Veo: foto en blanco y negro; un niño muy pequeño; un muro alto que ocupa casi toda la imagen. Pienso: el muro enorme frente al niño sugiere que hay algo difícil de superar. Me pregunto: ¿quién tomó la foto?, ¿dónde se hizo?",
        ["anota al menos tres datos en Veo", "escribe una interpretación con dos datos", "escribe dos preguntas", "no mezcla opiniones en la columna de datos"],
        ["tabla de tres columnas", "interpretación escrita"],
        ["escribir opiniones en la columna de datos", "interpretar sin evidencia"],
        "Destaca el dato que más sostiene la interpretación y pregunta qué otra idea cabría con los mismos datos.",
    ),
    "Mira un mueble o un objeto de tu casa, descríbelo en voz alta con tres datos y luego di qué crees que comunica.",
    "Escribe una segunda interpretación para la misma obra y explica qué datos la sostienen.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA4, 2,
    "Una hoja, lápiz y tres obras de ejemplo descritas en esta clase. Si quieres, puedes mirar un objeto de tela o de greda de tu casa para tocar su material.",
    "Aprenderé a examinar el medio de expresión, la materialidad y el lenguaje visual de una obra. Sirve para interpretar usando pistas concretas y no solo la primera impresión.",
    ["Sé describir lo que se ve antes de interpretar.", "Sé que una interpretación necesita evidencia."],
    [
        "El medio de expresión es el tipo de obra: pintura, dibujo, escultura, grabado, fotografía, textil, cerámica, video o instalación. Cambia lo que la obra puede hacer: la fotografía congela un instante; el video muestra el tiempo; la escultura se recorre. La materialidad es el material con que está hecha y cómo se trabajó: piedra pulida o tosca, lana tejida, greda modelada, papel recortado, pintura espesa o diluida. El material influye en lo que siento: lo suave, lo áspero, lo pesado.",
        "El lenguaje visual son los recursos con que se construye la imagen: la línea (recta, curva, quebrada), la forma (geométrica u orgánica), el color (cálido o frío, brillante o apagado), la textura, la composición (cómo se ordena todo) y el espacio (lleno o vacío). Cada recurso crea efectos: las líneas quebradas sugieren tensión y las curvas suavidad. Una composición simétrica da orden y una asimétrica da movimiento.",
        "Para examinar una obra me pregunto en orden: ¿en qué medio está?, ¿con qué materiales y cómo se trabajaron?, ¿qué recursos del lenguaje visual usa? y ¿qué efecto produce cada uno? Luego conecto: «La greda rugosa y las formas redondas dan sensación de lo hecho a mano y lo cercano». Mi interpretación mejora cuando relaciona material y lenguaje visual con la idea que parece comunicar.",
    ],
    [("medio de expresión", "tipo de obra, como pintura, escultura, fotografía o textil"), ("materialidad", "material con que está hecha una obra y cómo se trabajó"), ("lenguaje visual", "recursos como línea, forma, color, textura, composición y espacio"), ("composición", "cómo se ordenan los elementos en la obra"), ("simétrica", "con las dos mitades iguales, como un espejo")],
    [
        w("Examinar una obra", "Obra de ejemplo: un tejido de lana gruesa con formas redondas en rojo, naranja y amarillo, ordenadas en cuadrícula. Examina medio, materialidad y lenguaje visual.", ["Medio: textil.", "Materialidad: lana gruesa tejida, se ve suave y artesanal.", "Lenguaje visual: formas redondas, colores cálidos y orden en cuadrícula."], "Medio textil, lana gruesa tejida, formas redondas cálidas en cuadrícula"),
        w("Conectar con la idea", "Con los datos del tejido anterior, interpreta qué sensación da.", ["Los colores cálidos dan calor y energía.", "Las formas redondas dan suavidad.", "La cuadrícula da orden."], "Da una sensación de calidez y orden hecho a mano"),
    ],
    [
        m("Confundir el medio con el material: decir que «el medio es lana».", "El medio es el tipo de obra (textil); la lana es el material.", "Anota el medio y, aparte, el material."),
        m("Decir que una línea o un color siempre significan lo mismo.", "Su efecto cambia con el contexto y la composición.", "Describe el efecto en esa obra y apóyalo con lo que la rodea."),
    ],
    [
        ex("Una obra en la que se modelan figuras de greda, ¿es de medio escultura/cerámica o fotografía?", "Escultura/cerámica", "Se trabaja con volumen y material modelado."),
        ex("La lana tejida es: A. un material B. un medio de expresión.", "A", "Es la materia con que está hecha la obra."),
        ex("¿Cuál es un recurso del lenguaje visual: la línea o el precio de la obra?", "La línea", "La línea es parte del lenguaje visual."),
    ],
    [
        ex("Obra de ejemplo: una fotografía de una calle mojada en la noche, con luces reflejadas. ¿Qué medio es?", "Fotografía", "Es una imagen captada con cámara."),
        ex("Una obra con líneas quebradas y colores muy contrastantes sugiere más probablemente: A. tensión B. calma.", "A", "Las líneas quebradas y el contraste dan sensación de tensión."),
        ex("Una escultura de piedra tosca y pesada, ¿qué sensación da su materialidad: dureza o ligereza?", "Dureza", "La piedra tosca se siente dura y pesada."),
    ],
    [
        ex("Obra de ejemplo: un grabado con líneas finas negras sobre papel blanco que representa un bosque. ¿Qué dos recursos del lenguaje visual se mencionan? A. Línea fina y contraste de negro sobre blanco B. Volumen y movimiento.", "A", "Son los recursos descritos: la línea y el contraste de color."),
        ex("Dos obras tratan el mismo tema, una familia. La primera usa formas geométricas rígidas y la segunda formas orgánicas y curvas. ¿Cuál sugiere más cercanía?", "La segunda", "Las curvas orgánicas pueden sentirse más cálidas y cercanas."),
        arith("Una instalación tiene 4 filas de 6 tubos de cartón. ¿Cuántos tubos hay?", "4*6", "Se multiplican filas por tubos por fila."),
    ],
    [
        ex("Un estudiante dice que una pintura con tonos azules y grises «siempre es triste». Otro dice que depende del contexto. Si la pintura muestra una playa con un cielo gris y una niña riendo, ¿quién tiene mejor argumento?", "El segundo", "Lo que rodea al color cambia su efecto."),
        ex("Una escultura de bronce pulido y una de arcilla sin pulir. ¿Cuál se ve más rústica y cercana al trabajo manual?", "La de arcilla sin pulir", "La superficie sin pulir muestra las huellas de las manos."),
    ],
    [
        ex("Obra de ejemplo: un afiche con una composición simétrica: dos caras iguales a cada lado y un texto al centro. ¿Qué efecto da la simetría? A. Orden y equilibrio B. Movimiento y desequilibrio.", "A", "Las dos mitades iguales dan orden."),
        ex("Obra de ejemplo: un video corto de 30 segundos que muestra el crecimiento de una planta. ¿Qué puede mostrar este medio que una fotografía no? A. El paso del tiempo B. El color verde de las hojas.", "A", "El video muestra el cambio en el tiempo."),
    ],
    ex("Examinas dos obras de ejemplo con el mismo tema, una vasija. ¿Cuál muestra más huellas del trabajo manual? A. greda modelada a mano, con huellas de dedos y color café opaco B. porcelana brillante con líneas perfectas", "A", "Las huellas de dedos y el acabado opaco muestran lo hecho a mano."),
    [
        ex("En Artes Visuales, ¿qué es la materialidad?", "El material con que está hecha una obra y cómo se trabajó", "Influye en lo que sentimos."),
        ex("Verdadero o falso: el medio y el material son lo mismo.", "Falso", "El medio es el tipo de obra y el material es la materia."),
        ex("¿Cuál es un recurso del lenguaje visual: el color o el precio?", "El color", "El color construye la imagen."),
    ],
    task(
        "Elige UNA obra de ejemplo. A) Un tejido de lana gruesa con formas redondas en rojo, naranja y amarillo en cuadrícula. B) Un grabado de líneas finas negras sobre papel blanco que muestra un bosque. C) Una escultura de piedra tosca con forma redonda y una grieta al centro. Anota medio, material, tres recursos del lenguaje visual y el efecto de cada uno. Termina con una interpretación de dos líneas.",
        "Elegí la C. Medio: escultura. Material: piedra tosca, que se ve dura y áspera. Lenguaje visual: forma redonda, grieta al centro, superficie áspera. Efectos: lo redondo se siente completo; la grieta rompe esa perfección. Interpretación: parece mostrar algo fuerte que se ha roto, por la grieta que corta la forma completa.",
        ["identifica el medio y el material", "nombra tres recursos del lenguaje visual con su efecto", "interpreta con dos datos", "no confunde medio y material"],
        ["ficha de examen de la obra", "interpretación de dos líneas"],
        ["confundir medio con material", "usar fórmulas de color"],
        "Destaca el efecto mejor relacionado con el material y pregunta cómo cambiaría con otro material.",
    ),
    "Toca dos materiales de tu casa (tela y plástico, por ejemplo) y di qué sensación da cada uno.",
    "Compara el efecto de la misma forma hecha en dos materiales distintos y explica cuál sirve más para una idea de suavidad.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA4, 3,
    "Una hoja y lápiz. Las fichas de obra que se usan son de ejemplo y están escritas en esta clase.",
    "Aprenderé a situar una obra: quién la hizo (autoría), para qué (propósito) y en qué lugar y época (contexto). Sirve para interpretar sin atribuir ideas que la obra no muestra.",
    ["Sé examinar medio, material y lenguaje visual.", "Sé distinguir patrimonial de contemporáneo."],
    [
        "Situar una obra es averiguar sus datos básicos. La autoría dice quién o quiénes la hicieron; a veces es una persona conocida, otras una comunidad o una autoría anónima, cuando no se sabe quién fue. El propósito es para qué se hizo: decorar, guardar algo, conmemorar, protestar, vender, enseñar. El contexto es cuándo, dónde y en qué situación se hizo, y para quién. Estos datos suelen estar en la ficha o cartela, el texto corto junto a la obra.",
        "Una obra patrimonial suele tener un contexto compartido por una comunidad: se usó en fiestas, en el trabajo o en el hogar, y se transmitió entre generaciones. Una contemporánea suele responder a temas de hoy y puede ser firmada por una persona. Pero no todo lo antiguo es patrimonial ni todo lo nuevo es contemporáneo en el mismo sentido: lo importante es qué dice la ficha y qué cuida la comunidad. Si falta un dato, lo anoto como pregunta y no lo invento.",
        "Con estos datos mi interpretación gana fuerza. Una vasija con líneas de agua puede interpretarse distinto si la ficha dice que se usaba para guardar agua que si dice que se hizo hace poco para decorar. Para citar una fuente, anoto de dónde saqué cada dato: la cartela, un libro o una persona de la comunidad. Así separo lo que veo, lo que sé por la ficha y lo que supongo.",
    ],
    [("autoría", "quién o quiénes hicieron la obra"), ("anónima", "de autor o autora desconocidos"), ("propósito", "para qué se hizo la obra"), ("contexto", "cuándo, dónde y para quién se hizo"), ("cartela", "texto corto junto a la obra con sus datos")],
    [
        w("Leer una ficha", "Ficha de ejemplo: «Manta tejida a telar. Autoría: grupo de tejedoras de una comunidad. Uso: abrigo y regalo en celebraciones. Época: segunda mitad del siglo XX». Identifica autoría, propósito y contexto.", ["Autoría: un grupo de tejedoras.", "Propósito: abrigar y regalar en celebraciones.", "Contexto: comunidad, segunda mitad del siglo XX."], "Autoría: grupo de tejedoras; propósito: abrigo y regalo; contexto: comunidad, siglo XX"),
        w("Separar lo que se sabe", "Una cartela dice: «Vasija de greda, autoría desconocida». Alguien afirma que la hizo una mujer joven. ¿Está respaldado?", ["La ficha no da el género ni la edad.", "Es una suposición.", "Se anota como pregunta."], "No está respaldado: es una suposición que debe anotarse como pregunta"),
    ],
    [
        m("Inventar quién hizo la obra o para qué cuando la ficha no lo dice.", "Atribuye datos sin fuente.", "Anótalo como pregunta y busca una fuente."),
        m("Creer que toda obra antigua es patrimonial y toda obra nueva es contemporánea sin mirar la ficha.", "Los datos de la ficha y el cuidado de la comunidad son los que importan.", "Lee la ficha y distingue lo que dice de lo que supones."),
    ],
    [
        ex("¿Qué dato dice «quién hizo la obra»: autoría o propósito?", "Autoría", "La autoría identifica a quienes la crearon."),
        ex("Una obra de la que no se sabe quién fue su autor es de autoría: A. anónima B. famosa.", "A", "Anónima significa autor o autora desconocidos."),
        ex("El texto corto que acompaña una obra con sus datos se llama:", "Cartela", "Es la ficha informativa de la obra."),
    ],
    [
        ex("Cartela de ejemplo: «Cuenco de madera. Uso: servir alimentos en reuniones familiares». ¿Cuál es el propósito? A. Servir alimentos B. Decorar una pared.", "A", "La cartela dice el uso."),
        ex("Cartela de ejemplo: «Fotografía en blanco y negro. Autoría: una fotógrafa. Año: 1990. Lugar: no se indica». ¿Qué dato de contexto aparece?", "El año 1990", "Es cuándo se hizo."),
        ex("Una cartela no dice dónde se hizo la obra. ¿Qué haces con ese dato? A. Anotarlo como pregunta B. Inventarlo.", "A", "No se inventan datos que faltan."),
    ],
    [
        ex("Cartela de ejemplo: «Pintura mural, autoría: colectivo de vecinos. Propósito: recordar a las personas del barrio». Un compañero escribe que lo pintó un solo pintor famoso. ¿Es correcto?", "No", "La cartela dice que fue un colectivo de vecinos."),
        ex("Una obra con una cartela «autoría anónima, usada en fiestas de la comunidad por varias generaciones» ¿qué tipo de manifestación es más probable?", "Patrimonial", "La comunidad la ha transmitido y cuidado."),
        arith("Una cartela dice que la obra se hizo en 1995. Si el año actual fuera 2025, ¿Cuántos años tiene?", "2025-1995", "Se restan los años."),
    ],
    [
        ex("Dos vasijas iguales. La cartela de la primera dice «guardar agua» y la de la segunda dice «adorno hecho recientemente». Las dos tienen líneas ondulantes. ¿En cuál las líneas pueden relacionarse con el agua del uso?", "En la primera", "La cartela conecta las ondas con el uso de guardar agua."),
        ex("Un estudiante escribe: «Esta máscara, como es antigua, es sagrada». La cartela solo dice que es del siglo XIX. ¿Qué error hay?", "Afirmó algo que la cartela no dice", "Antigua no significa sagrada; falta evidencia."),
    ],
    [
        ex("Cartela de ejemplo: «Instalación de sillas vacías. Autoría: un artista. Propósito: recordar a personas que ya no están. Lugar: una plaza». Un compañero dice que es solo un adorno. ¿Qué dato de la cartela lo contradice?", "El propósito de recordar a personas que ya no están", "Muestra una intención de memoria, no de adorno."),
        ex("Debes registrar la fuente de un dato. ¿Cuál es una buena anotación? A. «Dato de la cartela de la obra» B. «Alguien me dijo».", "A", "Indica de dónde viene el dato."),
    ],
    ex("Ficha de ejemplo: «Escultura de piedra. Autoría anónima. Época: no se sabe. Uso: en lugares de reunión de la comunidad». Tres frases: 1) «La hizo un hombre mayor». 2) «Estaba en lugares de reunión». 3) «Es de hace 100 años». ¿Cuál está respaldada por la ficha?", "La 2", "Es la única que aparece en la ficha."),
    [
        ex("En Artes Visuales, ¿qué es el propósito de una obra?", "Para qué se hizo", "Puede ser decorar, conmemorar, enseñar o usar."),
        ex("Verdadero o falso: se puede inventar la autoría si no está en la ficha.", "Falso", "Se anota como pregunta."),
        ex("En Artes Visuales, ¿qué es una autoría anónima?", "Una en que no se sabe quién fue el autor o la autora", "La ficha lo declara así."),
    ],
    task(
        "Elige UNA ficha de ejemplo. A) «Manta tejida a telar. Autoría: un grupo de tejedoras de una comunidad. Uso: abrigo y regalo en celebraciones.» B) «Pintura mural. Autoría: colectivo de vecinos. Propósito: recordar a personas del barrio.» C) «Vasija de greda. Autoría desconocida. Contexto: no se sabe.» Escribe autoría, propósito y contexto, dos preguntas que quedan abiertas y una interpretación que use un dato de la ficha.",
        "Elegí la B. Autoría: colectivo de vecinos. Propósito: recordar a personas del barrio. Contexto: un barrio, sin fecha. Preguntas: ¿cuándo se pintó?, ¿qué personas aparecen? Interpretación: como el colectivo busca recordar, los rostros grandes al centro parecen darles importancia.",
        ["identifica autoría, propósito y contexto", "anota dos preguntas abiertas", "interpreta con un dato de la ficha", "no inventa datos que faltan"],
        ["ficha completada", "interpretación"],
        ["inventar autoría o propósito", "mezclar lo que sabe con lo que supone"],
        "Destaca el dato mejor usado y pregunta qué pregunta abierta investigaría primero.",
    ),
    "Mira un objeto de tu casa hecho a mano y di qué sabes de quién lo hizo y qué solo supones.",
    "Escribe una ficha de ejemplo para un objeto de tu casa con autoría, propósito y contexto, marcando lo que no sabes.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA4, 4,
    "Una hoja y lápiz. Las obras y las interpretaciones que se comparan son de ejemplo y están escritas en esta clase.",
    "Aprenderé a comparar dos interpretaciones de una misma obra y a decidir cuál está mejor sostenida con evidencia visual y de contexto. Sirve para argumentar con respeto y para cambiar de idea con razones.",
    ["Sé describir, examinar y situar una obra.", "Sé que interpretar necesita evidencia."],
    [
        "Una misma obra puede tener más de una interpretación válida, pero no todas valen igual. Una interpretación está bien sostenida cuando cita datos de lo que se ve (evidencia visual), datos de la ficha (evidencia de contexto) y los relaciona con la idea. Está mal sostenida cuando afirma sin datos, contradice lo que se ve o usa una fórmula como «el rojo siempre es peligro».",
        "Para comparar dos interpretaciones, hago una tabla con tres filas: ¿qué dice cada una?, ¿qué evidencia usa?, ¿qué deja sin explicar? Marco la que usa más datos y explica más partes de la obra. Si las dos tienen buena evidencia, ambas pueden convivir: «La obra puede leerse como memoria y también como esperanza». Si una usa un dato que la ficha contradice, la descarto.",
        "Cuando mi interpretación cambia, lo digo: «Antes pensaba que… pero la cartela dice que…». Cambiar de idea con razones es parte de interpretar bien. Al discutir con otra persona uso frases respetuosas: «Yo veo… porque…, ¿qué dato usas tú?». No importa quién ganó, sino que ambos podamos ver las razones en la obra.",
    ],
    [("evidencia visual", "dato que se ve en la obra y respalda una idea"), ("evidencia de contexto", "dato de la ficha o del lugar que respalda una idea"), ("bien sostenida", "con datos que respaldan la idea"), ("contradecir", "decir lo contrario de lo que muestra un dato"), ("argumentar", "dar razones para defender una idea")],
    [
        w("Comparar dos lecturas", "Obra de ejemplo: una pintura con un camino largo que sube una colina, con una sola figura pequeña. Lectura 1: «Muestra esfuerzo, porque el camino es largo y la figura pequeña». Lectura 2: «Muestra alegría, porque es un día soleado». ¿Cuál está mejor sostenida si la figura aparece de espaldas y con la cabeza agachada?", ["La lectura 1 usa el camino largo y la figura pequeña.", "La lectura 2 usa el sol, pero la cabeza agachada no sugiere alegría.", "La 1 explica más partes de la obra."], "La lectura 1"),
        w("Cambiar de idea con razones", "Pensabas que una vasija era un adorno. La cartela dice que se usaba para guardar grano. ¿Qué escribes?", ["Cito la idea anterior.", "Cito el dato nuevo.", "Explico el cambio."], "«Antes pensaba que era un adorno, pero la cartela dice que servía para guardar grano»"),
    ],
    [
        m("Elegir una interpretación solo porque me gusta o porque la dijo mi amigo.", "No se basa en la evidencia de la obra.", "Compara qué datos usa cada lectura."),
        m("Decir que todas las interpretaciones valen igual.", "Algunas contradicen lo que se ve o lo que dice la ficha.", "Revisa la evidencia de cada una."),
    ],
    [
        ex("Una interpretación está bien sostenida cuando: A. cita datos de la obra o de la ficha B. usa las palabras más difíciles.", "A", "La evidencia respalda la idea."),
        ex("¿Se puede tener dos interpretaciones válidas de una misma obra? ¿Sí o no?", "Sí", "Si ambas se apoyan en evidencia."),
        ex("Si una interpretación contradice un dato de la ficha, ¿qué haces con ella?", "La descartas o la corriges", "Un dato de la ficha pesa más que una suposición."),
    ],
    [
        ex("Obra de ejemplo: una foto de una mesa con cinco platos servidos y solo tres personas sentadas. Lectura 1: «Faltan dos personas que se esperan». Lectura 2: «Es una fiesta enorme». ¿Cuál usa mejor el dato de los platos y las personas?", "La lectura 1", "Relaciona cinco platos con tres personas."),
        ex("La lectura A cita dos datos de la obra y uno de la ficha. La lectura B cita un dato de la obra. ¿Cuál tiene más evidencia?", "La A", "Tiene tres datos frente a uno."),
        ex("Dos personas leen distinto una obra. ¿Qué frase es respetuosa? A. «Yo veo esto porque…, ¿qué dato usas tú?» B. «Estás equivocado».", "A", "Pide razones sin descalificar."),
    ],
    [
        arith("La lectura 1 usa 4 datos y la lectura 2 usa 2. ¿Cuántos datos más usa la lectura 1?", "4-2", "Se resta la cantidad menor de la mayor."),
        ex("Obra de ejemplo: una escultura de metal con forma de ave con las alas cerradas y la cabeza baja, y una cartela que dice «Homenaje a las aves que ya no se ven». Lectura 1: «Muestra libertad». Lectura 2: «Muestra pérdida». ¿Cuál se apoya en la ficha y en la postura?", "La lectura 2", "El título habla de lo que ya no se ve y la postura es cerrada."),
        ex("Dos estudiantes miran un mural donde dominan los azules. Uno dice que «el azul siempre es tristeza». La otra dice que el azul del mar se relaciona con la pesca, según la cartela. ¿Cuál es más sólida?", "La segunda", "Usa un dato de contexto y no una fórmula."),
    ],
    [
        ex("Una lectura dice que un cuadro muestra «un cuidador amable» porque la figura tiene los brazos abiertos. Otra dice que muestra «peligro» porque hay una sombra grande detrás. Ambas tienen un dato. ¿Qué haces para decidir? A. Buscar más evidencia, como el título o la cartela B. Elegir la que te guste más.", "A", "Más evidencia ayuda a decidir."),
        ex("Una interpretación afirma que la obra «fue hecha para protestar», pero la cartela dice «hecha para adornar una casa». ¿Qué ocurre con la interpretación?", "Queda contradicha por la cartela", "Un dato de contexto la desmiente."),
    ],
    [
        ex("Escribe qué fila de la tabla de comparación te dice si una lectura deja partes sin explicar: A. «¿Qué deja sin explicar?» B. «¿Quién habla más?».", "A", "Es la tercera fila de la comparación."),
        ex("Cambiaste de idea tras leer la cartela. ¿Qué parte de tu texto lo debe mostrar?", "Un «antes pensaba… pero ahora veo…»", "Explica el cambio con una razón."),
    ],
    ex("Obra de ejemplo: una pintura con muchas manos de distintos tamaños que se unen en el centro. Lectura 1: «Muestra comunidad, porque las manos se juntan». Lectura 2: «Muestra soledad». ¿Cuál se apoya en la composición?", "La lectura 1", "Las manos que se juntan sugieren unión; la soledad no tiene apoyo."),
    [
        ex("En Artes Visuales, ¿qué es evidencia visual?", "Un dato que se ve en la obra y respalda una idea", "Se puede comprobar mirando."),
        ex("Verdadero o falso: todas las interpretaciones valen lo mismo.", "Falso", "Algunas contradicen datos."),
        ex("¿Qué se hace al cambiar de idea?", "Se explica con una razón", "Muestra que cambió con evidencia."),
    ],
    task(
        "Elige UNA obra de ejemplo con dos lecturas. A) Un mural de una escalera ancha que sube hacia una puerta cerrada con luz que sale por debajo; lectura 1: oportunidad que aún no se abre; lectura 2: peligro. B) Una foto de dos manos, una joven y una mayor, que sostienen juntas una taza; lectura 1: cuidado entre generaciones; lectura 2: despedida. C) Una escultura de ave con alas cerradas y título «Homenaje a las aves que ya no se ven»; lectura 1: libertad; lectura 2: pérdida. Haz una tabla comparando qué dice cada una, qué evidencia usa y qué deja sin explicar, y decide cuál está mejor sostenida.",
        "Elegí la C. Lectura 1: libertad, evidencia: es un ave; deja sin explicar las alas cerradas y el título. Lectura 2: pérdida, evidencia: alas cerradas, cabeza baja y título; deja sin explicar por qué es de metal. Mejor sostenida: la 2.",
        ["compara las dos lecturas con una tabla", "cita evidencia de la obra o la ficha", "indica lo que cada una deja sin explicar", "decide con una razón"],
        ["tabla de comparación", "decisión escrita"],
        ["elegir por gusto", "no citar evidencia"],
        "Destaca la evidencia más fuerte y pregunta qué dato nuevo cambiaría su decisión.",
    ),
    "Mira una imagen de un afiche o envase y di dos lecturas posibles con un dato para cada una.",
    "Elige la lectura que descartaste y escribe qué dato nuevo la haría convincente.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA4, 5,
    "Una hoja y lápiz. Las obras de ejemplo y las fichas están escritas en esta clase.",
    "Aprenderé a reconocer los límites de mi interpretación y a formular preguntas abiertas en lugar de afirmar lo que no sé. Sirve para hablar de obras con honestidad y respeto, sobre todo cuando son de otras culturas.",
    ["Sé comparar interpretaciones con evidencia.", "Sé que una ficha no siempre trae todos los datos."],
    [
        "Interpretar tiene límites. No puedo saber lo que sintió el autor ni la intención exacta solo mirando una obra. No puedo afirmar el significado de símbolos de otra cultura si no los conozco ni tengo una fuente confiable. Tampoco puedo saber para qué se usó un objeto sin datos. Lo honesto es separar tres cosas: lo que se ve, lo que dice la ficha y lo que supongo, y marcar con claridad lo último.",
        "Una pregunta abierta es la que no se responde con sí o no ni con un dato simple, y que invita a investigar. Por ejemplo: «¿Qué usos tuvo este objeto para la comunidad que lo hizo?» o «¿Qué relación tiene este material con el lugar donde se produjo?». Para obras patrimoniales de pueblos originarios, la voz de la comunidad y de sus educadores tradicionales es la fuente más confiable: les corresponde explicar significados que no están en la obra.",
        "Para terminar una interpretación incluyo una frase de límite: «Con los datos que tengo, parece…, pero no puedo saber…». Y una lista de dos o tres fuentes que consultaría: la cartela completa, un libro de museo o una persona de la comunidad. Reconocer lo que no sé no debilita mi análisis: lo hace más serio.",
    ],
    [("límite", "aquello que no se puede afirmar con los datos disponibles"), ("suposición", "idea que no tiene evidencia suficiente"), ("pregunta abierta", "pregunta que invita a investigar y no se responde con sí o no"), ("fuente", "persona o texto confiable de donde sale un dato"), ("símbolo", "imagen que representa una idea para un grupo")],
    [
        w("Marcar el límite", "Obra de ejemplo: una máscara de madera con ojos grandes y líneas blancas. Alguien escribe: «Representa a un espíritu protector». La cartela solo dice «Máscara de madera, siglo XIX». ¿Qué corriges?", ["La cartela no menciona espíritus.", "Lo que se ve son ojos grandes y líneas blancas.", "El significado exacto solo lo puede explicar la comunidad que la usó."], "«Tiene ojos grandes y líneas blancas; no puedo saber su significado sin consultar a la comunidad que la usó»"),
        w("Formular una pregunta abierta", "Ves un tejido con una figura repetida en zigzag. ¿Qué pregunta abierta haces?", ["No pregunto algo de sí o no.", "Pregunto por el uso y el significado.", "Indico quién podría responder."], "«¿Qué significa para quienes lo tejen esa figura repetida y cómo se aprende a tejerla?»"),
    ],
    [
        m("Afirmar el significado de un símbolo de otra cultura sin tener una fuente.", "Puede ser falso y faltar al respeto.", "Describe lo que se ve y pregunta a una fuente confiable."),
        m("Escribir solo preguntas de sí o no, como «¿es antigua?».", "No invitan a investigar.", "Pregunta por usos, relaciones y significados."),
    ],
    [
        ex("¿Se puede saber lo que sintió el artista solo mirando la obra? ¿Sí o no?", "No", "La obra muestra decisiones, pero no confirma sentimientos."),
        ex("¿Cuál es una pregunta abierta? A. «¿Qué usos tuvo este objeto para su comunidad?» B. «¿El objeto es de madera?».", "A", "La A invita a investigar; la B se responde mirando."),
        ex("Para saber el significado de un símbolo de un pueblo originario, ¿qué fuente es más confiable: la comunidad o una suposición?", "La comunidad", "Quien lo usa puede explicarlo."),
    ],
    [
        ex("Obra de ejemplo: una vasija pequeña con una cara dibujada. Elige la frase honesta. A. «Tiene una cara dibujada; no puedo saber su significado sin otra fuente» B. «Es un dios antiguo».", "A", "La A separa lo que se ve de lo que no se sabe."),
        ex("Dos frases sobre una vasija: 1) «Tiene líneas rojas». 2) «Fue hecha para una fiesta». Si la ficha no menciona fiestas, ¿cuál es una suposición?", "La 2", "No está respaldada por lo que se ve ni por la ficha."),
        ex("Una frase de límite puede empezar con: «Con los datos que tengo, parece… pero no puedo saber…». ¿Qué parte muestra el límite?", "«pero no puedo saber…»", "Indica lo que falta."),
    ],
    [
        ex("Obra de ejemplo: un textil con una figura que se repite y la cartela no la nombra. Elige la pregunta abierta más útil: A. «¿Qué significa esta figura para quienes tejen este textil?» B. «¿La figura se repite?».", "A", "Invita a investigar y se dirige a la fuente adecuada."),
        arith("Tienes 3 fuentes para consultar y ya consultaste 1. ¿Cuántas te faltan?", "3-1", "Se resta la consultada del total."),
        ex("Un compañero escribe que cierto símbolo en una vasija «significa guerra». La cartela no lo dice. ¿Qué le sugieres?", "Escribir qué se ve y preguntar a una fuente confiable", "No se afirma un significado sin respaldo."),
    ],
    [
        ex("Dos estudiantes escriben sobre una máscara. Uno: «Representa un espíritu». La otra: «Veo ojos grandes y líneas blancas; quisiera preguntar qué significan para quienes la usaron». ¿Cuál reconoce mejor el límite?", "La segunda", "Distingue lo visto de lo que no sabe y propone consultar."),
        ex("¿Por qué no basta con mirar una obra de otra cultura para explicar sus símbolos?", "Porque el significado lo da la comunidad que la usa", "La imagen sola no dice su sentido."),
    ],
    [
        ex("Escribe una frase de límite apropiada para esta situación: ves una escultura de piedra sin ficha. A. «Se ve una forma redonda con una grieta; no sé quién la hizo ni para qué» B. «La hizo un escultor famoso para un templo».", "A", "La A no inventa datos."),
        ex("Una obra de ejemplo tiene cartela completa y aun así quedan dudas. ¿Qué haces? A. Anotar la duda como pregunta abierta B. Ignorarla.", "A", "Una pregunta abierta guía una investigación."),
    ],
    ex("Obra de ejemplo: una manta con rombos de colores. Tres frases: 1) «Hay rombos rojos, azules y blancos». 2) «Cada rombo significa un antepasado». 3) «¿Qué significan los rombos para quienes tejieron la manta?» ¿Cuál es la pregunta abierta?", "La 3", "Es la que invita a investigar sin afirmar."),
    [
        ex("En Artes Visuales, ¿qué es una suposición?", "Una idea sin evidencia suficiente", "Debe marcarse como tal."),
        ex("Verdadero o falso: reconocer lo que no sé debilita mi análisis.", "Falso", "Lo hace más serio y honesto."),
        ex("¿Qué incluye una frase de límite?", "Lo que puedo decir y lo que no puedo saber", "Separa lo respaldado de lo que falta."),
    ],
    task(
        "Elige UNA obra de ejemplo. A) Una máscara de madera con ojos grandes y líneas blancas; la ficha solo dice «siglo XIX». B) Un textil con una figura en zigzag que se repite; sin ficha. C) Una vasija pequeña con una cara dibujada; la ficha dice «greda». Escribe lo que ves, lo que dice la ficha, una suposición marcada, una frase de límite, dos preguntas abiertas y dos fuentes que consultarías. La forma tradicional de entender los símbolos la enseñan las comunidades y sus educadores tradicionales.",
        "Elegí la B. Veo: una figura en zigzag que se repite en filas. Ficha: no hay. Suposición: quizá se repita por un patrón de tejido. Límite: no puedo saber su significado ni su uso. Preguntas: ¿qué significa la figura para quienes tejen?, ¿cómo se aprende ese tejido? Fuentes: una tejedora de la comunidad y un libro de museo.",
        ["separa lo que ve, la ficha y la suposición", "escribe una frase de límite", "formula dos preguntas abiertas", "propone dos fuentes confiables"],
        ["ficha con las tres partes", "preguntas y fuentes"],
        ["afirmar significados sin fuente", "preguntas de sí o no"],
        "Destaca la frase de límite y pregunta qué fuente sería la más cercana a la obra.",
    ),
    "Mira un objeto de tu casa hecho por otra persona y di una pregunta abierta que le harías.",
    "Escribe tres preguntas abiertas distintas para un mismo objeto y di a quién se las harías.",
)
