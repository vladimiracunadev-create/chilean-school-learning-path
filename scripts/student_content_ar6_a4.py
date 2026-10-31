"""Cuaderno del estudiante de 6.º básico Artes Visuales: AR06 OA 04 (analizar e interpretar obras de arte y objetos según lenguaje visual, contextos, materiales y estilos)."""
from __future__ import annotations

from student_content_ar6_a import lesson, m, task, w
from student_lessons import arith, ex

OA4 = "AR06 OA 04"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA4, 1,
    "Una hoja y un lápiz para anotar. Las obras se describen con palabras dentro de la clase; si tienes acceso a imágenes de ellas con una persona adulta, puedes mirarlas, pero no es necesario.",
    "Aprenderé a analizar una obra describiendo su lenguaje visual (línea, forma, color, textura y espacio) para después interpretarla. Sirve para decir qué veo, qué recursos usó el autor y qué creo que comunica, con evidencias.",
    ["Sé que interpretar es decir qué comunica una obra y fundamentar es apoyarlo con evidencias.", "Sé qué son la gama de color y el contraste."],
    [
        "Analizar una obra es separarla en partes para entender cómo está hecha. Se parte describiendo el lenguaje visual, que son los recursos con que se construye una imagen. La línea puede ser recta, curva o quebrada. La forma puede ser grande, pequeña, redondeada o angulosa. El color puede ser cálido o frío, brillante o apagado. La textura es lo que parece o se siente en la superficie. El espacio es cómo se ubican las cosas: cerca, lejos, llenas o vacías.",
        "Después de describir, interpreto. La descripción dice qué veo y la interpretación dice qué creo que comunica. Por ejemplo, la pintura «La noche estrellada» de Vincent van Gogh, pintor de los Países Bajos, de 1889, muestra un cielo con remolinos azules y amarillos, estrellas grandes, un ciprés oscuro y un pueblo pequeño abajo. Descripción: líneas curvas que giran, colores azules y amarillos y un pueblo muy chico. Interpretación posible: el cielo parece estar vivo y mover todo, mientras el pueblo duerme tranquilo.",
        "Un buen análisis usa frases con evidencia, como «las líneas curvas y repetidas dan sensación de movimiento». Evita decir solo «es bonito». También reconoce que dos personas pueden interpretar distinto una misma obra. Lo importante es que cada interpretación se apoye en algo que se ve. Mirar con calma, de a una parte, ayuda a no pasar por alto detalles.",
    ],
    [("analizar", "separar una obra en partes para entender cómo está hecha"), ("lenguaje visual", "recursos de una imagen: línea, forma, color, textura y espacio"), ("descripción", "decir qué veo, sin opinar"), ("interpretación", "decir qué creo que comunica la obra"), ("composición", "cómo están ubicadas las cosas en la obra")],
    [
        w("Describir y luego interpretar", "Una pintura muestra una casa pequeña y gris en medio de un campo inmenso, muy vacío, bajo un cielo oscuro. Describe y luego interpreta.", ["Describo: casa pequeña y gris, campo muy grande y vacío, cielo oscuro.", "Observo el espacio: hay mucho vacío alrededor de la casa.", "Interpreto: creo que comunica soledad, porque la casa es pequeña y está rodeada de espacio vacío."], "Creo que comunica soledad, porque la casa es pequeña y está rodeada de mucho espacio vacío"),
        w("Separar descripción e interpretación", "Frase A: «El cielo tiene círculos azules y amarillos». Frase B: «El cielo está enojado». ¿Cuál es descripción y cuál interpretación?", ["La A se puede ver en la imagen.", "La B es lo que creo que comunica.", "Una interpretación necesita evidencia."], "A es descripción; B es interpretación"),
    ],
    [
        m("Mezclar opinión con descripción: «hay un cielo horrible».", "«Horrible» no es un dato que se vea.", "Describe colores, líneas y formas antes de opinar."),
        m("Decir una interpretación sin señalar qué detalle la sostiene.", "Sin evidencia, la interpretación es solo una opinión.", "Agrega «porque se ve…»."),
    ],
    [
        ex("¿Qué recurso del lenguaje visual describe «curva» o «quebrada»: la línea o el color?", "La línea", "Las líneas pueden ser rectas, curvas o quebradas."),
        ex("«Hay estrellas amarillas grandes en un cielo azul oscuro». ¿Es una descripción o una interpretación?", "Una descripción", "Dice lo que se ve, sin decir qué comunica."),
        ex("¿Qué dice la interpretación de una obra: lo que veo o lo que creo que comunica?", "Lo que creo que comunica", "La descripción es la que dice lo que veo."),
    ],
    [
        ex("«La noche estrellada» es de Vincent van Gogh. ¿De qué país es este pintor: los Países Bajos o Chile?", "Los Países Bajos", "Van Gogh nació en los Países Bajos."),
        ex("En «La noche estrellada», ¿qué recurso da la sensación de movimiento en el cielo: las líneas curvas que giran o los cuadrados rojos?", "Las líneas curvas que giran", "Las curvas repetidas se sienten como movimiento."),
        ex("Una pintura tiene una figura diminuta al fondo de una sala enorme. ¿Qué recurso del lenguaje visual dice más: el espacio o la textura?", "El espacio", "La relación de tamaños y el vacío son parte del espacio."),
    ],
    [
        ex("Tu descripción menciona la línea, la forma, el color y el espacio de una obra. ¿Qué recurso falta para completar los cinco del lenguaje visual?", "La textura", "Los cinco son línea, forma, color, textura y espacio."),
        ex("Una escultura de piedra tiene una superficie áspera con huecos. ¿Qué recurso describes: la textura o la gama?", "La textura", "Lo áspero es la superficie."),
        ex("Si en una pintura el cielo ocupa tres cuartos del cuadro y el pueblo solo un cuarto, ¿qué parte domina?", "El cielo", "Ocupa más espacio."),
    ],
    [
        ex("Una persona dice que una obra es «triste». ¿Cómo debe completar su análisis para fundamentarlo: «porque usa colores grises y una figura sola» o «porque a mí me da pena»?", "Porque usa colores grises y una figura sola", "Debe apoyarse en lo que se ve."),
        ex("Dos estudiantes interpretan la misma pintura. Una dice «es calma» por los azules suaves y las líneas horizontales; otro dice «es soledad» por el espacio vacío. ¿Ambas interpretaciones pueden ser válidas?", "Sí", "Cada una se apoya en evidencia visible."),
    ],
    [
        ex("Una obra tiene muchas líneas diagonales rojas que se cruzan. Entre «transmite calma» y «transmite tensión o movimiento», ¿cuál interpretación tiene más apoyo en el lenguaje visual?", "Transmite tensión o movimiento", "Las diagonales rojas y cruzadas suelen sentirse tensas y en movimiento."),
        ex("En el análisis de un cuadro, ¿qué va primero: describir lo que se ve o interpretar lo que comunica?", "Describir lo que se ve", "La interpretación se apoya en la descripción."),
    ],
    ex("Ves en un mural una niña muy grande de color amarillo sobre un fondo azul oscuro, rodeada de figuras pequeñas y grises. Escribes: «Creo que la niña es importante porque es la más grande y la única de color amarillo». ¿Esta frase es descripción pura, interpretación con evidencia o solo opinión?", "Interpretación con evidencia", "Dice qué comunica y lo apoya con detalles visibles."),
    [
        ex("¿Qué cinco recursos forman el lenguaje visual en esta clase?", "Línea, forma, color, textura y espacio", "Son los recursos con que se construye una imagen."),
        ex("Verdadero o falso: una interpretación puede ser distinta a la de otra persona y seguir siendo válida.", "Verdadero", "Mientras se apoye en evidencia visible."),
        ex("¿Qué debe llevar toda interpretación?", "Una evidencia visible", "La evidencia evita que sea solo una opinión."),
    ],
    task(
        "Elige UNA obra descrita. A) «La noche estrellada» (Van Gogh, 1889): cielo con remolinos azules y amarillos, estrellas grandes, ciprés oscuro y pueblo pequeño abajo. B) «Guernica» (Pablo Picasso, 1937): pintura muy grande en blanco, negro y grises, con figuras de personas y animales de formas angulosas. C) «Las dos Fridas» (Frida Kahlo, 1939): dos mujeres sentadas, tomadas de la mano, una con vestido blanco y otra con vestido de colores. Escribe una descripción con los cinco recursos y una interpretación con «porque se ve…».",
        "Elegí la A. Descripción: línea curva en espirales; formas redondas de estrellas; color azul y amarillo; textura de pinceladas visibles; espacio con un cielo enorme y un pueblo pequeño. Interpretación: creo que comunica un cielo lleno de vida sobre un pueblo dormido, porque las líneas giran y las estrellas son muy grandes.",
        ["describe los cinco recursos", "separa descripción e interpretación", "usa evidencia visible", "no inventa datos"],
        ["texto de descripción", "interpretación con «porque»"],
        ["opinar sin evidencia", "mezclar descripción e interpretación"],
        "Pregunta qué detalle sostiene su interpretación y si otra persona podría ver otra cosa con la misma evidencia.",
    ),
    "Elige una imagen que tengas a mano y nombra su línea, forma, color, textura y espacio.",
    "Describe la misma obra pensando solo en el color y luego solo en el espacio y compara qué interpretación aparece en cada caso.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA4, 2,
    "Una hoja y lápices de colores para probar. Las obras y los estilos se describen en esta clase; si tienes imágenes de ellas, puedes mirarlas con una persona adulta.",
    "Aprenderé qué es el estilo de una obra y a reconocer tres formas de resolver una imagen: realista, abstracta y expresiva. Sirve para explicar por qué dos obras del mismo tema se ven tan distintas.",
    ["Sé analizar una obra con línea, forma, color, textura y espacio.", "Sé que el impresionismo busca captar la luz de un momento con pinceladas cortas."],
    [
        "El estilo es la manera en que una obra o un artista resuelve el lenguaje visual. Un estilo se reconoce porque repite ciertos recursos. En un estilo realista las figuras se parecen mucho a como las vemos: proporciones normales, colores naturales y detalles. En un estilo abstracto la obra no copia cosas reales: usa formas, líneas y colores por sí mismos. En un estilo expresivo el artista exagera formas y colores para mostrar una emoción, aunque no se parezca a lo real.",
        "Muchos artistas combinan estilos o inventan uno propio. Fernando Botero, pintor y escultor de Colombia, hizo figuras con volúmenes muy grandes y redondeados; ese rasgo es su estilo personal. Roberto Matta, artista chileno, hizo pinturas con formas y espacios imaginarios, asociadas al surrealismo, que intenta mostrar sueños e ideas fuera de lo cotidiano. El impresionismo, visto en 5.º, es un estilo que capta la luz con pinceladas cortas.",
        "Para reconocer un estilo no basta el tema; hay que mirar los recursos. Dos pinturas de una plaza pueden verse completamente distintas si una es realista y la otra expresiva. Me pregunto: ¿las figuras se parecen a lo real? ¿Los colores son naturales o exagerados? ¿Hay detalles o solo formas simples? Con esas preguntas ubico la obra en un estilo y explico mi respuesta con evidencias.",
    ],
    [("estilo", "manera de resolver el lenguaje visual, que se repite en una obra o un artista"), ("realista", "que se parece mucho a lo que vemos"), ("abstracto", "que no copia cosas reales y usa formas y colores por sí mismos"), ("expresivo", "que exagera formas y colores para mostrar una emoción"), ("surrealismo", "estilo que muestra sueños e ideas fuera de lo cotidiano")],
    [
        w("Reconocer el estilo", "Una pintura de un perro muestra pelo con muchos detalles, colores naturales y proporciones normales. ¿Qué estilo es?", ["El perro se parece mucho a uno real.", "Los colores son naturales.", "Eso es un estilo realista."], "Realista"),
        w("Mismo tema, distinto estilo", "Dos pinturas de un árbol: una tiene un árbol con hojas muy detalladas y la otra, tres manchas verdes sin forma de árbol. ¿Qué estilo es cada una?", ["La primera copia detalles reales.", "La segunda usa solo manchas de color.", "La primera es realista y la segunda abstracta."], "Primera: realista; segunda: abstracta"),
    ],
    [
        m("Decidir el estilo solo por el tema («es un paisaje, entonces es realista»).", "Un paisaje puede pintarse en estilos muy distintos.", "Mira los recursos: formas, colores y detalles."),
        m("Pensar que lo abstracto son «garabatos» sin pensar.", "El artista decide cuidadosamente líneas, colores y espacios.", "Pregunta qué decisiones se ven en la obra."),
    ],
    [
        ex("Un estilo en que las figuras se parecen mucho a lo real se llama...", "Realista", "Copia con detalle lo que se ve."),
        ex("Una obra que usa solo líneas y colores sin copiar cosas reales, ¿es realista o abstracta?", "Abstracta", "No representa objetos reconocibles."),
        ex("Fernando Botero hizo figuras con volúmenes grandes y redondeados. ¿De qué país es este artista: Colombia o Japón?", "Colombia", "Botero es colombiano."),
    ],
    [
        ex("Una pintura exagera los colores y deforma una cara para mostrar enojo. ¿Qué estilo es: expresivo o realista?", "Expresivo", "Exagera para mostrar una emoción."),
        ex("Roberto Matta es un artista chileno asociado al surrealismo. ¿Qué intenta mostrar el surrealismo: sueños e ideas fuera de lo cotidiano o mapas exactos?", "Sueños e ideas fuera de lo cotidiano", "Esa es la idea central del surrealismo."),
        ex("Dos cuadros de una misma plaza: A) con árboles y bancas detallados y colores naturales; B) con colores muy exagerados y formas deformadas. ¿Cuál es expresivo?", "B", "Exagera colores y formas para comunicar emoción."),
    ],
    [
        ex("Descripción: «Un cuadrado rojo, un círculo azul y líneas negras, sin ningún objeto reconocible.» ¿Qué estilo es?", "Abstracto", "No representa cosas reales."),
        ex("Descripción: «Una niña con zapatos de cuero, trenzas y un vestido de rayas, pintada con muchos detalles y colores naturales.» ¿Qué estilo es?", "Realista", "Los detalles y colores naturales indican realismo."),
        ex("Descripción: «Una ciudad con calles que se doblan como ondas y casas de colores muy fuertes, para mostrar un sentimiento de mareo.» ¿Qué estilo es?", "Expresivo", "Exagera formas y colores para mostrar una emoción."),
    ],
    [
        ex("Un compañero dice: «Esta pintura es abstracta porque es un paisaje». ¿Es correcto su argumento?", "No", "Un paisaje puede ser realista o expresivo; hay que mirar los recursos."),
        ex("Dos pinturas muestran un mar. En la primera hay olas con espuma detallada y colores naturales. En la segunda hay bandas horizontales de azul y gris sin olas. ¿Qué diferencia de estilo hay?", "La primera es realista y la segunda abstracta", "La segunda no copia detalles reales."),
    ],
    [
        ex("Tienes que explicar por qué una obra es expresiva. ¿Qué evidencia sirve: colores exagerados y figuras deformadas, o que fue pintada con óleo?", "Colores exagerados y figuras deformadas", "El estilo se reconoce por los recursos visuales que exageran la emoción."),
        ex("Un artista repite figuras redondeadas y voluminosas en muchas obras. ¿Eso es parte de su estilo?", "Sí", "El estilo se reconoce porque se repiten recursos."),
    ],
    ex("Hay un afiche que muestra un tren con ruedas, ventanas y vías dibujados con exactitud. Otro afiche muestra el mismo tren como un montón de líneas diagonales rojas y negras que dan idea de velocidad. ¿En cuál se ve un estilo más abstracto?", "En el segundo", "No copia los detalles; usa líneas y colores para la idea de velocidad."),
    [
        ex("¿Qué es el estilo de una obra?", "La manera de resolver el lenguaje visual", "Se reconoce porque se repiten recursos."),
        ex("Verdadero o falso: dos obras del mismo tema pueden tener estilos distintos.", "Verdadero", "Los recursos visuales pueden ser muy diferentes."),
        ex("¿Qué estilo exagera colores y formas para mostrar emociones?", "Expresivo", "Prioriza la emoción más que la copia de la realidad."),
    ],
    task(
        "Elige UN tema. A) Un perro en una plaza. B) Una casa bajo la lluvia. C) Un grupo de personas en una micro. Haz tres bocetos pequeños del mismo tema: uno realista, uno abstracto y uno expresivo. Escribe qué recursos usaste en cada uno (línea, forma, color, textura o espacio).",
        "Elegí la B. Realista: casa con tejas y gotas, colores naturales. Abstracto: líneas diagonales azules y un rectángulo gris. Expresivo: casa torcida, cielo rojizo y gotas enormes. Recursos: la expresiva usa color exagerado y forma deformada.",
        ["hace tres bocetos del mismo tema", "cada boceto tiene un estilo reconocible", "nombra los recursos", "separa lo que veo de lo que significa"],
        ["tres bocetos", "texto con recursos"],
        ["mezclar estilos sin intención", "no justificar"],
        "Pregunta qué recurso cambió más entre los bocetos y qué sensación produce cada estilo.",
    ),
    "Mira una imagen de tu casa (una foto o un afiche) y di si es realista, abstracta o expresiva.",
    "Rehaz un boceto en un cuarto estilo (por ejemplo, de mezcla) y explica qué recursos cambias.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA4, 3,
    "Una hoja, lápiz y, si quieres, un trozo de tela con trama gruesa (como un saco), lana y una aguja de lana de punta roma para probar un bordado simple con una persona adulta cerca. Las obras se describen en la clase.",
    "Aprenderé cómo los materiales de una obra influyen en lo que comunica, con ejemplos de arte chileno, latinoamericano y universal. Sirve para analizar por qué el artista eligió ese material y qué efecto tiene.",
    ["Sé analizar una obra con lenguaje visual.", "Sé qué es un estilo."],
    [
        "El material es parte del mensaje de una obra. Un artista elige un material por sus características: textura, color, resistencia, y también por lo que ese material significa. La pintura al óleo, que se aplica sobre tela, permite mezclar colores con suavidad y trabajar con calma; la usaron Van Gogh y muchos otros pintores. La piedra es dura, pesada y dura siglos, y por eso se usa en obras que quieren permanecer. Los moai de Rapa Nui, por ejemplo, son esculturas hechas de piedra volcánica.",
        "Violeta Parra, artista chilena, además de cantautora hizo arpilleras. Son bordados hechos con lanas de colores sobre una tela áspera de saco, llamada arpillera. Los materiales son humildes y cotidianos, y eso acerca la obra a la vida diaria del pueblo. Parra expuso sus arpilleras en París en 1964. La textura de la lana y el saco se nota: es áspera, con relieve y con puntadas visibles, lo que da un aspecto artesanal y cálido.",
        "Para analizar un material respondo tres preguntas: ¿de qué está hecha la obra? ¿Cómo se ve y se siente ese material? ¿Qué efecto o significado le da a la obra? Por ejemplo, el hormigón y el hierro de una escultura grande dan sensación de fuerza y resistencia al clima. En cambio un papel delgado dura poco y se siente frágil. Un mismo tema cambia mucho según el material con que se haga.",
    ],
    [("material", "sustancia con que está hecha una obra"), ("óleo", "pintura que se mezcla con aceite y se aplica sobre tela"), ("arpillera", "tela áspera de saco usada como base de bordados"), ("hormigón", "mezcla de cemento, arena y piedras que se endurece"), ("artesanal", "hecho a mano, con trabajo manual visible")],
    [
        w("Material y mensaje", "Una escultura de una mano gigante está hecha de hormigón y hierro, en un desierto. ¿Qué efecto dan esos materiales?", ["El hormigón y el hierro son duros y resistentes.", "Aguantan sol, viento y el paso de los años.", "Dan sensación de fuerza y permanencia."], "Fuerza y permanencia"),
        w("Textura de un bordado", "Una arpillera tiene lanas de colores bordadas sobre tela áspera, y se ven las puntadas. Describe su textura.", ["La tela es áspera.", "Las lanas dejan relieve y puntadas visibles.", "Se ve artesanal y cálido."], "Áspera, con relieve y puntadas visibles; aspecto artesanal"),
    ],
    [
        m("Pensar que el material solo sirve para sostener la obra.", "El material también comunica por su textura y significado.", "Pregunta qué efecto tiene el material en la obra."),
        m("Decir que una obra está hecha de «pintura» sin precisar el material.", "Hay muchos tipos de pintura y de soporte.", "Nombra el material y el soporte, como óleo sobre tela."),
    ],
    [
        ex("¿La arpillera es una tela áspera o una tela muy suave?", "Una tela áspera", "Es una tela de trama gruesa, como la de un saco."),
        ex("Los moai de Rapa Nui están hechos de piedra volcánica. ¿Qué característica tiene la piedra: es dura o se deshace con el agua?", "Es dura", "La piedra volcánica es dura y resistente."),
        ex("El óleo se aplica sobre tela. ¿Es una pintura o una escultura?", "Una pintura", "El óleo es un tipo de pintura."),
    ],
    [
        ex("Violeta Parra hizo bordados con lanas sobre arpillera. ¿Por qué se ven artesanales: porque se hicieron a mano y se ven las puntadas o porque se hicieron con máquina?", "Porque se hicieron a mano y se ven las puntadas", "El trabajo manual visible da aspecto artesanal."),
        ex("¿Qué material da más sensación de duración: la piedra o el papel delgado?", "La piedra", "Resiste siglos; el papel se destruye con facilidad."),
        ex("Una obra de hormigón y hierro está al aire libre en el desierto. ¿Qué cualidad del material es útil allí: resiste el clima o se deshace con el sol?", "Resiste el clima", "Una obra pública debe resistir sol y viento."),
    ],
    [
        ex("Una escultura de 2 m está hecha de hormigón y otra del mismo tamaño, de espuma blanda. Las dos se dejarán en una plaza durante el invierno. ¿Cuál resiste mejor la lluvia?", "La de hormigón", "El hormigón es duro y resiste el agua; la espuma blanda se deteriora."),
        ex("Dos obras del mismo tema: una es un bordado de lana y otra una escultura de metal. Ambas muestran una casa. ¿Cuál se verá más blanda y cálida?", "El bordado de lana", "La lana es blanda y artesanal."),
        ex("Una obra se hizo con papel de diario pegado. ¿Qué tipo de material es: cotidiano y fácil de conseguir o muy raro y caro?", "Un material cotidiano", "El papel de diario se encuentra en la vida diaria."),
    ],
    [
        ex("Un compañero dice: «Da lo mismo si la figura es de lana o de metal; el mensaje es igual». ¿Es correcto?", "No", "El material cambia la textura, el peso y lo que se siente."),
        ex("Un artista quiere mostrar la fragilidad de la vida. Elige entre una figura de papel de seda delgado y una de granito macizo. ¿Qué material apoya mejor su idea?", "El papel de seda delgado", "Lo frágil refuerza la idea de fragilidad."),
    ],
    [
        ex("Describes una arpillera: «lana roja bordada sobre tela áspera, con puntadas visibles». Un compañero dice que es un óleo. ¿Qué evidencia muestra que no lo es?", "El bordado de lana sobre tela áspera", "El óleo es pintura; aquí hay lana bordada."),
        arith("Una arpillera lleva 8 hileras de puntadas y en cada hilera hay 12 puntadas de lana. ¿Cuántas puntadas tiene en total?", "8*12", "Se multiplican hileras por puntadas de cada una."),
    ],
    ex("Quieres explicar por qué una escultura de hormigón en el desierto da sensación de fuerza. ¿Qué escribes: «porque el hormigón es duro y resiste» o «porque es bonito»?", "Porque el hormigón es duro y resiste", "Explica el efecto con una característica del material."),
    [
        ex("¿Qué tres preguntas haces al analizar el material de una obra?", "De qué está hecha, cómo se ve y se siente y qué efecto da", "Cubren material, textura y significado."),
        ex("Verdadero o falso: el material forma parte del mensaje de una obra.", "Verdadero", "La textura y el significado del material cambian lo que comunica."),
        ex("¿Qué es una arpillera?", "Una tela áspera de saco usada como base de bordados", "Su trama gruesa se nota en la obra."),
    ],
    task(
        "Elige UNA obra o prueba. A) Una arpillera con lana de colores sobre tela áspera que muestra una casa y un sol. B) Una escultura de piedra volcánica con una cara de nariz larga. C) Una pintura al óleo sobre tela de un paisaje con cerros. Escribe de qué material está hecha, cómo se ve y se siente, y qué efecto o significado da al mensaje. Opcional: con una persona adulta cerca, haz una prueba de puntadas de lana con aguja de punta roma sobre un trozo de tela con trama gruesa.",
        "Elegí la B. Material: piedra volcánica. Se ve áspera y gris, con relieve; se siente dura. Efecto: da sensación de fuerza y de que dura mucho tiempo, porque la piedra aguanta siglos.",
        ["nombra el material", "describe cómo se ve y se siente", "explica el efecto o significado", "no inventa datos"],
        ["texto con tres respuestas"],
        ["decir solo «es bonito»", "no nombrar el material"],
        "Pregunta cómo cambiaría el mensaje si la obra se hiciera con otro material.",
    ),
    "Toca un objeto de tu casa y di qué material es y qué sensación da.",
    "Elige un mismo tema y explica cómo cambiaría con tres materiales distintos.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA4, 4,
    "Una hoja y lápiz. Las fichas de obras con sus datos están escritas en la clase; no necesitas buscar nada.",
    "Aprenderé qué es el contexto de una obra (quién, cuándo, dónde y para qué se hizo) y a distinguir obras del arte chileno, latinoamericano y universal. Sirve para entender una obra mejor y situarla en el mundo.",
    ["Sé analizar el lenguaje visual, el estilo y el material.", "Sé que algunas obras están en el espacio público."],
    [
        "El contexto es la situación en que se hizo una obra: quién la hizo, cuándo, en qué lugar y para qué. Conocer el contexto ayuda a interpretar mejor. «Guernica» es una pintura muy grande en blanco, negro y grises que Pablo Picasso, pintor de España, hizo en 1937, después de un bombardeo a la ciudad de Guernica durante la guerra civil española. Por eso se interpreta como una obra contra los horrores de la guerra. Sus formas angulosas y la falta de color refuerzan la sensación de dolor.",
        "El arte se suele agrupar según su origen. El arte chileno es el hecho en Chile, como la «Mano del Desierto» de Mario Irarrázabal o las arpilleras de Violeta Parra. El arte latinoamericano es el de América Latina: «Las dos Fridas», de Frida Kahlo, de México, de 1939, o las figuras voluminosas de Fernando Botero, de Colombia. El arte universal reúne obras de todo el mundo, como las de Van Gogh, Picasso o Leonardo da Vinci. En Chillán, en la Escuela México, el mexicano David Alfaro Siqueiros pintó un mural en los años 1940.",
        "Para analizar un contexto me pregunto: ¿quién la hizo? ¿Cuándo y dónde? ¿Para quién y con qué fin? Un mural en una escuela se interpreta distinto de una pintura de museo. Lo importante es no inventar: si no sé un dato, digo que lo desconozco o lo busco en un libro. El contexto no reemplaza lo que veo en la obra: lo complementa, y las dos fuentes juntas dan una interpretación más sólida.",
    ],
    [("contexto", "situación en que se hizo una obra: quién, cuándo, dónde y para qué"), ("arte chileno", "obras hechas en Chile"), ("arte latinoamericano", "obras de países de América Latina"), ("arte universal", "obras de todo el mundo, incluidas las de otros continentes"), ("ficha", "resumen con los datos principales de una obra")],
    [
        w("Armar una ficha", "Con los datos de la clase, arma la ficha de «Las dos Fridas».", ["Autora: Frida Kahlo, de México.", "Año: 1939.", "Origen: arte latinoamericano; muestra dos mujeres sentadas, tomadas de la mano."], "Frida Kahlo, México, 1939; arte latinoamericano"),
        w("Usar el contexto", "«Guernica» se pintó en 1937 tras un bombardeo en la guerra civil española. ¿Por qué eso ayuda a interpretar la obra?", ["La obra usa blanco, negro y grises.", "Sabemos que se hizo después de una tragedia.", "Interpretamos que habla del dolor de la guerra."], "Ayuda a interpretar que habla del dolor de la guerra"),
    ],
    [
        m("Inventar datos sobre la vida del artista para justificar una interpretación.", "Un dato falso confunde el análisis.", "Usa solo datos seguros y, si dudas, dilo."),
        m("Usar solo el contexto y olvidarse de mirar la obra.", "La interpretación debe apoyarse también en lo visible.", "Combina contexto con lenguaje visual."),
    ],
    [
        ex("¿La «Mano del Desierto» de Mario Irarrázabal es arte chileno o arte universal de otro continente?", "Arte chileno", "Es una obra hecha en Chile, en el desierto de Atacama."),
        ex("Frida Kahlo, autora de «Las dos Fridas», es de México. ¿Es arte latinoamericano o arte europeo?", "Arte latinoamericano", "México es parte de América Latina."),
        ex("Pablo Picasso, autor de «Guernica», es de España. ¿Es arte latinoamericano o arte universal?", "Arte universal", "España está en otro continente."),
    ],
    [
        ex("¿Qué cuatro preguntas ayudan a conocer el contexto: quién, cuándo, dónde y para qué, o cuánto, cuántos, cuál y cómo?", "Quién, cuándo, dónde y para qué", "Son las preguntas del contexto de una obra."),
        ex("«Guernica» es en blanco, negro y grises. Según el contexto de la guerra, ¿qué refuerza esa falta de color: el dolor o la alegría?", "El dolor", "La falta de color refuerza la sensación de tristeza."),
        ex("En la Escuela México de Chillán hay un mural del mexicano David Alfaro Siqueiros. ¿De qué país es el artista: México o Chile?", "México", "Siqueiros es mexicano, aunque pintó este mural en Chile."),
    ],
    [
        ex("Clasifica estas obras por origen: A) arpilleras de Violeta Parra. B) figuras voluminosas de Fernando Botero. C) «La noche estrellada» de Van Gogh. ¿Cuál es arte chileno?", "A", "Violeta Parra es chilena."),
        ex("Entre las figuras voluminosas de Fernando Botero y «La noche estrellada» de Van Gogh, ¿cuál es arte latinoamericano?", "Las figuras de Botero", "Botero es de Colombia, país de América Latina; Van Gogh es de los Países Bajos."),
        ex("Una ficha dice: «Autor: Vincent van Gogh. País: Países Bajos. Año: 1889». ¿Es arte latinoamericano?", "No", "Los Países Bajos están en Europa."),
    ],
    [
        ex("Un compañero dice: «Guernica es alegre porque tiene un caballo». ¿Qué datos del contexto lo contradicen?", "Se pintó después de un bombardeo en una guerra", "El contexto de guerra y el color gris indican dolor."),
        ex("Alguien afirma que Frida Kahlo pintó «Las dos Fridas» en 1989. ¿Es correcto?", "No, fue en 1939", "La fecha de la ficha es 1939."),
    ],
    [
        ex("Quieres comparar una obra pública y una de museo. Un mural en un paradero lo ven miles de personas al día; una pintura en una sala se ve solo con entrada. ¿En cuál influye más el contexto del lugar público?", "En el mural del paradero", "Está en la calle y llega a mucha gente."),
        arith("En una ficha de 3 obras chilenas, 4 latinoamericanas y 5 universales, ¿cuántas obras hay en total?", "3+4+5", "Se suman las obras de cada origen."),
    ],
    ex("Tienes que hacer una ficha de una obra y no sabes en qué año se hizo. ¿Qué haces: inventar un año o escribir que ese dato se desconoce?", "Escribir que ese dato se desconoce", "En un análisis no se inventan datos."),
    [
        ex("¿Qué es el contexto de una obra?", "La situación en que se hizo: quién, cuándo, dónde y para qué", "Ayuda a interpretar mejor."),
        ex("Verdadero o falso: el arte universal incluye solo obras de Chile.", "Falso", "Universal reúne obras de todo el mundo."),
        ex("¿Por qué no hay que inventar datos en una ficha?", "Porque un dato falso confunde el análisis", "La interpretación debe apoyarse en datos seguros."),
    ],
    task(
        "Elige UNA obra con sus datos. A) «Guernica», Pablo Picasso, España, 1937. B) «Las dos Fridas», Frida Kahlo, México, 1939. C) «La noche estrellada», Vincent van Gogh, Países Bajos, 1889. Arma la ficha (autor, país, año, origen: chileno, latinoamericano o universal) y escribe qué te ayuda a entender el contexto. Si falta algún dato, escribe «dato no incluido» y no lo inventes.",
        "Elegí la B. Autora: Frida Kahlo. País: México. Año: 1939. Origen: latinoamericano. Contexto: es de México y se pintó en 1939. Interpretación posible: dos partes de una misma persona, porque las dos mujeres están unidas de la mano.",
        ["arma la ficha con los cuatro datos", "clasifica el origen", "relaciona contexto y obra", "no inventa datos"],
        ["ficha completa", "frase sobre el contexto"],
        ["inventar datos", "olvidar la obra"],
        "Pregunta cómo el contexto cambió su interpretación y qué dato más le gustaría conocer.",
    ),
    "Elige una imagen de un libro o una pared y pregunta quién, cuándo, dónde y para qué se hizo.",
    "Haz una ficha de una obra de un artista chileno y otra de uno latinoamericano y compara sus contextos.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA4, 5,
    "Una hoja y lápiz. La obra de ejemplo, «Los paraguas de la feria», está descrita en esta clase y no existe en la realidad; es un texto original para practicar.",
    "Aprenderé a escribir un análisis completo de una obra con cuatro partes: descripción, análisis de recursos y materiales, contexto e interpretación con evidencias. Sirve para explicar con claridad lo que veo y lo que creo que comunica.",
    ["Sé analizar lenguaje visual, estilo, material y contexto.", "Sé que una interpretación necesita evidencia."],
    [
        "Un análisis completo reúne todo lo aprendido en cuatro partes. Primero describo qué veo. Segundo analizo cómo está hecha: línea, forma, color, textura, espacio, estilo y material. Tercero explico el contexto: quién la hizo, cuándo, dónde y para qué, solo con datos seguros. Cuarto interpreto qué comunica y lo apoyo con evidencias de las partes anteriores. Si un dato no es seguro, no lo incluyo.",
        "Practiquemos con una obra imaginaria, «Los paraguas de la feria»: una pintura al óleo sobre tela donde hay muchos paraguas de colores muy fuertes vistos desde arriba; casi no se ven las personas, solo círculos de colores que se tocan; las líneas de las varillas forman estrellas. Es de una autora imaginaria y se pintó en una ciudad lluviosa. Descripción: círculos de colores. Análisis: color vivo, formas redondas, vista desde arriba y óleo. Interpretación: comunica compañía en un día de lluvia, porque los paraguas se tocan.",
        "Para escribir bien, uso conectores: «además», «porque», «por eso», «en cambio». Evito frases como «me gustó» o «es raro». También conviene comparar dos obras: ¿en qué se parecen? ¿En qué se distinguen en estilo, material o mensaje? Comparar enseña a ver detalles que de una sola obra no aparecen. Al final reviso si cada afirmación tiene evidencia y si separé lo que veo de lo que interpreto.",
    ],
    [("análisis", "explicación de cómo está hecha una obra y qué comunica"), ("evidencia", "detalle visible o dato seguro que sostiene una idea"), ("comparar", "buscar semejanzas y diferencias entre dos obras"), ("conector", "palabra que une ideas, como porque o por eso"), ("dato seguro", "dato que se sabe con certeza")],
    [
        w("Armar el análisis", "Con la descripción de «Los paraguas de la feria», escribe una frase para cada parte del análisis.", ["Descripción: muchos paraguas de colores vistos desde arriba.", "Análisis: óleo sobre tela, colores fuertes y formas redondas que se tocan.", "Interpretación: comunica compañía en un día de lluvia, porque los paraguas están pegados."], "Descripción, análisis de recursos, contexto e interpretación con evidencia"),
        w("Comparar dos obras", "Obra 1: «Guernica», blanco, negro y grises, formas angulosas. Obra 2: «La noche estrellada», azul y amarillo, líneas curvas. ¿En qué se diferencian en color?", ["Guernica usa casi solo blanco, negro y grises.", "La noche estrellada usa azules y amarillos intensos.", "Una es sin color y la otra muy colorida."], "Guernica casi sin color; La noche estrellada, muy colorida"),
    ],
    [
        m("Escribir solo una descripción y llamarla «análisis».", "El análisis incluye recursos, contexto e interpretación.", "Agrega las cuatro partes."),
        m("Incluir datos que no se saben para que suene más completo.", "Un dato falso debilita todo el análisis.", "Escribe solo lo seguro."),
    ],
    [
        ex("¿Cuántas partes tiene el análisis completo de esta clase?", "Cuatro", "Son descripción, análisis de recursos, contexto e interpretación."),
        ex("En «Los paraguas de la feria», ¿qué forma domina: círculos o triángulos?", "Círculos", "Los paraguas vistos desde arriba son círculos."),
        ex("¿La interpretación de una obra va al principio o después de describir y analizar?", "Después de describir y analizar", "Se apoya en esas partes."),
    ],
    [
        ex("«Los paraguas de la feria» se ve desde arriba y los paraguas se tocan. ¿Qué interpretación tiene más apoyo: compañía o aislamiento?", "Compañía", "Los círculos pegados dan idea de cercanía."),
        ex("¿Qué conector introduce una evidencia: «porque» o «también»?", "Porque", "«Porque» introduce la razón o evidencia."),
        ex("Comparas dos obras que usan el mismo material pero se ven muy distintas. ¿Qué recurso explica la diferencia: el estilo o el material?", "El estilo", "El material es igual; lo que cambia es el estilo."),
    ],
    [
        ex("En tu análisis de «Los paraguas de la feria», ¿en qué parte pones «es un óleo sobre tela»: descripción, recursos y material o contexto?", "En los recursos y el material", "Habla de cómo está hecha la obra y de su material."),
        ex("Escribes: «La obra es hermosa». ¿Qué falta para convertirla en análisis: señalar recursos y evidencias o decir que a ti te gusta?", "Señalar recursos y evidencias", "El análisis se apoya en lo que se ve."),
        arith("Un análisis tiene 4 partes y cada parte lleva 2 frases. ¿Cuántas frases tiene el análisis completo?", "4*2", "Se multiplican partes por frases de cada una."),
    ],
    [
        ex("Un compañero escribe sobre «Los paraguas de la feria»: «Comunica tristeza porque son paraguas». ¿Tiene evidencia suficiente?", "No", "Los colores fuertes y los círculos pegados no sostienen tristeza."),
        ex("Un compañero compara dos obras: «las dos representan una casa, pero una es blanda y colorida, de lana, y la otra es dura y gris, de piedra». ¿Es una buena comparación?", "Sí", "Señala una semejanza y una diferencia visibles."),
    ],
    [
        ex("Escribes sobre una obra de la que no sabes el año. ¿Qué escribes en la parte de contexto: «año desconocido» o un año inventado?", "Año desconocido", "No se inventan datos."),
        ex("Quieres comparar una arpillera de lana con un óleo sobre tela. ¿Qué diferencia de material puedes señalar?", "La lana bordada es blanda y rugosa; el óleo es pintura sobre tela", "Son materiales de aspecto y textura distintos."),
    ],
    ex("Debes explicar «La noche estrellada» a un compañero que no la conoce. Tienes cuatro frases: A) «Es de Van Gogh, de 1889, de los Países Bajos». B) «Se ve un cielo con remolinos, estrellas grandes y un pueblo pequeño». C) «Las líneas curvas dan idea de movimiento». D) «Creo que comunica un cielo vivo sobre un pueblo en calma, porque las curvas giran». ¿Cuál frase es la interpretación?", "D", "Dice qué comunica y se apoya con evidencia."),
    [
        ex("¿Qué cuatro partes tiene el análisis completo de una obra?", "Descripción, análisis de recursos, contexto e interpretación", "Así se reúne todo lo aprendido."),
        ex("Verdadero o falso: comparar dos obras ayuda a ver detalles nuevos.", "Verdadero", "Las diferencias muestran recursos que en una sola obra pasan inadvertidos."),
        ex("¿Qué haces con un dato que no es seguro?", "No lo incluyo", "Un dato falso debilita el análisis."),
    ],
    task(
        "Elige UNA obra con descripción. A) «Los paraguas de la feria» (descrita en la clase). B) «La noche estrellada», Van Gogh, 1889: cielo con remolinos, ciprés oscuro, pueblo pequeño. C) Una arpillera: casa, sol y árbol bordados con lana de colores sobre tela áspera, de autora desconocida. Escribe un análisis de cuatro partes (descripción, recursos y material, contexto con solo datos seguros e interpretación con «porque») y una frase que compare tu obra con otra de esta unidad.",
        "Elegí la C. Descripción: casa, sol y árbol de lana sobre tela. Recursos: textura áspera, colores vivos, formas simples. Contexto: autora desconocida; dato no incluido. Interpretación: comunica vida cotidiana y calidez, porque la lana de colores y la casa pequeña se sienten cercanas. Comparación: a diferencia de «La noche estrellada», usa lana y no óleo.",
        ["escribe las cuatro partes", "usa solo datos seguros", "apoya la interpretación con evidencia", "incluye una comparación"],
        ["texto de cuatro partes", "frase de comparación"],
        ["mezclar descripción e interpretación", "inventar datos"],
        "Pregunta qué parte del análisis le costó más y cómo la mejoraría.",
    ),
    "Mira una imagen cualquiera y di cuatro frases: qué veo, cómo está hecha, dónde o cuándo (si lo sé) y qué creo que comunica.",
    "Compara dos obras de la unidad y escribe tres semejanzas y tres diferencias.",
)
