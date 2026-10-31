"""Cuaderno del estudiante de 5.º básico Artes Visuales: AR05 OA 04 (analizar e interpretar obras de arte y diseño en contexto)."""
from __future__ import annotations

from student_content_ar5_a import lesson, m, task, w
from student_lessons import arith, ex

OA4 = "AR05 OA 04"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA4, 1,
    "Hoja y lápiz para tu registro de obras. Las obras que se analizan están descritas con palabras en esta clase; si puedes, mira también imágenes de obras con ayuda de una persona adulta o en un libro de la biblioteca.",
    "Aprenderé a mirar una obra en tres pasos: describir lo que veo, relacionarlo con su contexto y recién entonces interpretar lo que comunica. Sirve para hablar de una obra con evidencia y no solo con opiniones.",
    ["Sé separar una observación de una opinión.", "Sé nombrar color, forma, línea, textura, luz y sombra."],
    [
        "Analizar una obra es mirarla con atención y ordenar lo que descubro. Interpretar es explicar qué creo que comunica y por qué. El orden es: primero describir, luego analizar y relacionar con el contexto, y al final interpretar. Describir es decir lo que se ve, sin opinar: «hay botes pequeños, un cielo naranjo y manchas de azul en el agua». Analizar es nombrar cómo se usa el lenguaje visual (color, línea, forma, luz) y con qué materiales está hecha.",
        "El contexto es la información que rodea a la obra: quién la hizo, cuándo y dónde, para qué se hizo y en qué estilo. Una obra de arte puede ser una pintura o una escultura, y su función suele ser expresar ideas o sentimientos. Un diseño, como un afiche o un envase, además tiene una función práctica. Conocer el contexto ayuda a entender mejor, pero no siempre se conoce todo; entonces digo «creo que» y no «es seguro».",
        "Una interpretación tiene tres partes: lo que veo (evidencia), lo que creo que comunica y la razón que une las dos. Por ejemplo: «Veo un cielo naranjo con manchas azules en el agua; creo que el autor quiso mostrar la luz del amanecer, porque los colores cambian de a poco». Dos personas pueden interpretar distinto una misma obra, y ambas pueden estar bien si usan evidencia. Cada año conviene observar muchas obras (al menos 50) de arte y diseño chileno, latinoamericano y universal, y anotarlas en un registro.",
    ],
    [("describir", "decir lo que se ve en una obra, sin opinar"), ("analizar", "nombrar cómo se usa el lenguaje visual y los materiales"), ("interpretar", "explicar qué creo que comunica una obra y por qué"), ("contexto", "información sobre quién, cuándo, dónde y para qué se hizo una obra"), ("evidencia", "dato de la obra que apoya una interpretación")],
    [
        w("Describir antes de interpretar", "Obra A: «Un cuadro de un puerto al amanecer, con cielo naranjo pintado con pinceladas cortas, botes pequeños y agua con manchas de azul y rosado». Escribe una frase de descripción.", ["Digo solo lo que se ve.", "Nombro colores y objetos.", "No digo qué siente el autor."], "Hay un cielo naranjo, botes pequeños y manchas de azul y rosado en el agua"),
        w("Armar una interpretación", "Con la obra A, une evidencia, idea y razón.", ["Evidencia: el cielo naranjo y las manchas de colores en el agua.", "Idea: el autor quiso mostrar la luz del amanecer.", "Razón: los colores cambian de a poco, como la luz de la mañana."], "Veo cielo naranjo y manchas de colores; creo que muestra la luz del amanecer porque los colores cambian de a poco"),
    ],
    [
        m("Decir «es un cuadro hermoso» como si fuera una descripción.", "Es una opinión y no dice nada que se pueda comprobar.", "Describe colores, formas y materiales."),
        m("Interpretar sin mirar la obra y sin dar razones.", "No se apoya en evidencia.", "Primero describe; luego explica qué te hace pensar eso."),
    ],
    [
        ex("Obra A: «Un cuadro de un puerto al amanecer, con cielo naranjo, botes pequeños y manchas de azul y rosado en el agua». ¿Qué colores tiene el agua?", "Azul y rosado", "La descripción dice que hay manchas de azul y rosado en el agua."),
        ex("«Los botes son pequeños». ¿Es una descripción o una interpretación?", "Una descripción", "Dice un dato que se ve."),
        ex("Al mirar una obra, ¿qué se hace primero: describir lo que veo o decir qué quiso comunicar el autor?", "Describir lo que veo", "La interpretación se apoya en la descripción."),
    ],
    [
        ex("«Creo que el autor quiso mostrar la calma del amanecer». ¿Es una descripción o una interpretación?", "Una interpretación", "Dice qué cree la persona que comunica la obra."),
        ex("¿Qué dato de la obra A apoya mejor que el autor quiso mostrar la luz de la mañana: el cielo naranjo con manchas de colores o que sea un cuadro?", "El cielo naranjo con manchas de colores", "Es un dato visual relacionado con la luz del amanecer."),
        ex("«Fue pintado al aire libre en el siglo XIX». ¿Es un dato de contexto o del lenguaje visual?", "De contexto", "Dice cuándo y cómo se hizo, no cómo se ven los colores."),
    ],
    [
        ex("Ordena los pasos para interpretar: A) interpretar con evidencia, B) describir lo que veo, C) relacionar con el contexto. Escribe las tres letras en orden.", "B, C, A", "Primero se describe, luego se mira el contexto y al final se interpreta."),
        ex("¿Cuál es un dato de lenguaje visual de la obra A: las pinceladas cortas o la fecha de la pintura?", "Las pinceladas cortas", "Las pinceladas son parte de cómo se usa el lenguaje visual."),
        ex("Un compañero dice: «Me gusta la obra A». ¿Es una interpretación fundamentada?", "No", "Es un gusto y no explica qué comunica la obra."),
    ],
    [
        ex("Ema dice que la obra A muestra el cansancio de los pescadores. La descripción no menciona pescadores. ¿Tiene evidencia en la obra para esa interpretación?", "No", "No hay datos de pescadores en lo que se describe."),
        ex("Beto dice: «La obra A muestra luz cambiante, porque el cielo es naranjo y el agua tiene manchas azules y rosadas». ¿Su interpretación tiene evidencia?", "Sí", "Nombra datos visuales y los une con una idea."),
    ],
    [
        ex("Una interpretación tiene tres partes: lo que veo, lo que creo y la razón. Alguien dice: «Veo botes pequeños; creo que es un puerto tranquilo». ¿Qué parte le falta?", "La razón", "No explica por qué los botes pequeños dan tranquilidad."),
        ex("Dos personas interpretan distinto la misma obra, pero ambas usan datos que se ven en ella. ¿Pueden estar bien las dos?", "Sí", "Una obra puede comunicar más de una idea si hay evidencia."),
    ],
    ex("Estás en un museo y ves una escultura. Antes de leer la etiqueta, ¿qué haces: miras y anotas lo que ves o copias lo que dice la etiqueta?", "Miras y anotas lo que ves", "La descripción propia es el primer paso."),
    [
        ex("Verdadero o falso: describir es decir lo que se ve, sin opinar.", "Verdadero", "La descripción se limita a datos observables."),
        ex("¿Qué tres partes tiene una interpretación?", "Lo que veo, lo que creo y la razón", "Une evidencia, idea y razón."),
        ex("Verdadero o falso: una obra solo puede tener una interpretación.", "Falso", "Puede haber varias si tienen evidencia."),
    ],
    task(
        "Elige UNA obra descrita. A) «Un afiche con letras grandes amarillas sobre fondo azul oscuro, un dibujo simple de un árbol y la frase “Cuida tu parque”». B) «Una escultura de piedra, de una figura de pie, de tres metros de altura, ubicada en una colina que mira al mar». C) «Un cuadro de una calle con casas de colores cálidos, líneas curvas y mucha luz». Escribe: 1) tres frases de descripción, 2) un dato de lenguaje visual, 3) una interpretación con evidencia y razón.",
        "Elegí la A. Descripción: hay letras amarillas grandes, un fondo azul oscuro y un árbol simple. Lenguaje visual: contraste fuerte entre amarillo y azul. Interpretación: veo letras amarillas sobre azul oscuro; creo que quiere llamar la atención de quienes pasan, porque el contraste hace que se lea desde lejos.",
        ["describe sin opinar", "nombra un dato de lenguaje visual", "interpreta con evidencia y razón", "separa dato y opinión"],
        ["tres frases de descripción", "un dato", "una interpretación de tres partes"],
        ["opinar sin describir", "interpretar sin razón"],
        "Destaca la interpretación mejor apoyada y pregunta qué dato de la obra la sostiene.",
    ),
    "Mira un objeto de tu casa con un diseño (un envase o un afiche) y di en voz alta tres cosas que ves.",
    "Empieza tu registro anual de obras: anota la primera obra con su nombre, país y una frase de descripción.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA4, 2,
    "Hoja y lápices de colores. Las versiones de la obra están descritas en esta clase.",
    "Aprenderé a ver cómo cambiar un elemento del lenguaje visual (color, línea, luz) cambia lo que una obra comunica. Sirve para interpretar con evidencia visual y para crear con más control.",
    ["Sé describir una obra y separar dato de opinión.", "Sé que los colores cálidos y fríos dan sensaciones distintas."],
    [
        "El lenguaje visual son los elementos con los que una obra comunica: color, línea, forma, textura, luz y sombra, espacio. Cuando analizo una obra, nombro estos elementos y pregunto qué efecto tienen. Los colores cálidos (rojo, naranjo, amarillo) suelen dar sensación de calor, cercanía y energía. Los colores fríos (azul, verde y violeta) suelen dar sensación de frío, distancia o calma.",
        "Las líneas también comunican. Las curvas dan suavidad y movimiento. Las rectas dan orden y firmeza, y a veces rigidez. Las líneas quebradas dan tensión. La luz y la sombra pueden dar misterio: sombras largas y oscuras suelen sugerir silencio, soledad o inquietud. Estas asociaciones son generales y pueden cambiar según la cultura o la obra, por eso siempre las apoyo en lo que realmente veo.",
        "Una buena forma de entender el efecto de un elemento es comparar dos versiones de una misma escena cambiando solo una variable. Si solo cambia el color, puedo ver qué cambió en la sensación. Luego escribo: «Cuando el color es…, la obra se siente…». Así, mi interpretación se apoya en una comparación y no en una impresión sin explicar.",
    ],
    [("lenguaje visual", "elementos con los que una obra comunica, como color, línea, luz y forma"), ("colores cálidos", "rojo, naranjo y amarillo y sus mezclas cercanas"), ("colores fríos", "azul, verde y violeta"), ("variable", "elemento que cambio para ver su efecto"), ("sensación", "lo que me hace sentir una imagen")],
    [
        w("Comparar dos versiones", "Versión 1 de una calle: colores cálidos, líneas curvas y mucha luz. Versión 2: colores fríos, líneas rectas y sombras largas. ¿Cuál se relaciona más con una sensación acogedora?", ["Los colores cálidos dan cercanía.", "Las curvas y la luz dan suavidad.", "La versión 1 reúne esos elementos."], "La versión 1"),
        w("Cambiar una variable", "Cambias solo el color de la versión 2 a cálido, sin tocar las líneas ni la luz. ¿Cuántas variables cambiaste?", ["Solo cambié el color.", "Las líneas y la luz son las mismas.", "Es una sola variable."], "Una"),
    ],
    [
        m("Pensar que un color siempre significa lo mismo en todas las obras.", "El significado depende de cómo se use y de la cultura.", "Apoya tu interpretación en lo que se ve en esa obra."),
        m("Cambiar muchas cosas a la vez y creer que sabes cuál causó el efecto.", "No se puede saber qué variable produjo el cambio.", "Cambia una variable cada vez."),
    ],
    [
        ex("Dos versiones de una calle. Versión 1: colores cálidos, líneas curvas y mucha luz. Versión 2: colores fríos, líneas rectas y sombras largas. ¿Qué versión tiene colores cálidos?", "La 1", "La versión 1 usa colores cálidos."),
        ex("En esas mismas versiones, ¿cuál tiene líneas rectas?", "La 2", "La versión 2 usa líneas rectas."),
        ex("El azul, ¿es un color cálido o frío?", "Frío", "Los colores fríos incluyen el azul."),
    ],
    [
        ex("Entre la versión 1 y la 2 de la calle, ¿cuál se relaciona más con una sensación de soledad y silencio?", "La 2", "Los colores fríos y las sombras largas sugieren silencio."),
        ex("Las líneas curvas suelen dar una sensación de suavidad y movimiento. ¿Cuál versión de la calle las tiene?", "La 1", "La versión 1 tiene líneas curvas."),
        ex("Una versión 3 de la calle usa colores fríos, líneas curvas y mucha luz. Comparada con la versión 1 (cálidos, curvas y mucha luz), ¿qué elemento cambió: el color o las líneas?", "El color", "Las líneas curvas y la luz son iguales; solo cambian los colores."),
    ],
    [
        ex("Quieres apoyar con evidencia que la versión 2 sugiere soledad. ¿Qué dato sirve: las sombras largas y los colores fríos o el título de la obra?", "Las sombras largas y los colores fríos", "Son datos visuales de la obra."),
        ex("Las líneas muy rectas y ordenadas, ¿suelen dar una sensación de orden o de movimiento?", "De orden", "Las líneas rectas dan firmeza y orden."),
        ex("Cambias solo las líneas de la versión 1 a rectas. Los colores y la luz siguen igual. ¿Cuántas variables cambiaron?", "Una", "Solo se cambió la línea."),
    ],
    [
        ex("Beto dice que la versión 1 muestra frío porque usa naranjo y amarillo. ¿Tiene sentido su interpretación?", "No", "El naranjo y el amarillo son colores cálidos, que suelen dar sensación de calor."),
        ex("Dos personas interpretan la versión 2: una dice soledad y otra dice silencio de la noche. Ambas se apoyan en las sombras largas y los colores fríos. ¿Pueden ser válidas las dos?", "Sí", "Ambas usan evidencia visual de la obra."),
    ],
    [
        ex("Quieres transformar la versión 2 en una versión que se sienta como una fiesta. ¿Qué cambio de color ayuda más: agregar rojo, naranjo y amarillo o agregar más gris?", "Agregar rojo, naranjo y amarillo", "Los colores cálidos dan energía y alegría."),
        ex("Una persona dice: «Eso significa miedo», sin nombrar nada de la obra. ¿Qué le falta a su interpretación?", "Evidencia visual", "Debe nombrar datos de la obra que apoyen su idea."),
    ],
    ex("Un libro de cuentos tiene dos ilustraciones de un bosque. En una, hay árboles altos y rectos con luz suave. En la otra, hay árboles torcidos y oscuros. El cuento es de misterio. ¿Cuál usarías en la parte más misteriosa?", "La de árboles torcidos y oscuros", "Las formas torcidas y los valores oscuros dan inquietud."),
    [
        ex("Verdadero o falso: los colores cálidos son rojo, naranjo y amarillo.", "Verdadero", "Ese grupo se llama colores cálidos."),
        ex("¿Qué dan las líneas quebradas: tensión o calma?", "Tensión", "Los quiebres producen sensación de agitación."),
        ex("Verdadero o falso: para saber el efecto de un elemento, conviene cambiar solo una variable.", "Verdadero", "Así se ve cuál causó el cambio."),
    ],
    task(
        "Elige UNA escena: A) un puerto; B) un bosque; C) una plaza. Haz dos versiones pequeñas en las que cambies solo UNA variable (por ejemplo, colores cálidos y colores fríos). Escribe qué cambió y qué sensación da cada versión, con una evidencia visual.",
        "Elegí la C. Versión 1: la plaza con colores cálidos y una luz amarilla. Versión 2: la misma plaza con colores fríos. Cambié solo el color. La versión 1 se siente acogedora, porque el amarillo y el naranjo dan cercanía. La versión 2 se siente más lejana, porque el azul y el verde azulado dan frío.",
        ["cambia una sola variable", "describe qué cambió", "relaciona con una sensación", "da evidencia visual"],
        ["dos versiones", "una frase de comparación", "una evidencia"],
        ["cambiar varias variables", "decir la sensación sin evidencia"],
        "Muestra la comparación más clara y pregunta qué otra variable cambiaría la sensación.",
    ),
    "Mira una imagen que tengas a mano y di si sus colores son más cálidos o más fríos y qué sensación dan.",
    "Haz una tabla de dos columnas: elementos del lenguaje visual y la sensación que suelen dar. Agrega tres filas.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA4, 3,
    "Hoja y lápiz. Las obras están descritas en esta clase. Para comparar materiales puedes mirar un cuaderno, un jarrón o una tela de tu casa.",
    "Aprenderé a interpretar una obra considerando su material y su procedimiento: óleo, acuarela, grabado, escultura, cerámica, textil, fotografía y medios digitales. Sirve para entender por qué una obra se ve como se ve.",
    ["Sé reconocer materiales y procedimientos.", "Sé describir una obra con evidencia."],
    [
        "El material y el procedimiento no son un detalle: cambian lo que una obra comunica. La pintura al óleo es espesa y se puede mezclar y superponer; muchas veces deja huellas visibles del pincel. La acuarela es transparente y suave, y deja ver el papel. El grabado permite hacer muchas copias de una misma imagen, porque se pasa por una plancha. La fotografía capta un instante real.",
        "La escultura de piedra es pesada y dura mucho tiempo, y por eso se usa en plazas y lugares abiertos. La cerámica es de arcilla cocida en un horno; en Chile, por ejemplo, es conocida la de Pomaire. Los textiles unen telas e hilos; las arpilleras, por ejemplo, se hacen con retazos de tela cosidos sobre una base. Los medios digitales permiten copiar, cambiar y mostrar una imagen en pantallas.",
        "Para interpretar con el material, me pregunto: ¿con qué está hecha?, ¿cómo se hizo?, ¿qué ventajas tiene ese material?, ¿cómo se relaciona con la idea de la obra? Por ejemplo, una figura de piedra grande en una colina transmite permanencia y fuerza, porque la piedra es pesada y resiste el clima. Una acuarela suave de nubes transmite ligereza, porque es transparente. Siempre digo «creo que» cuando no tengo toda la información.",
    ],
    [("óleo", "pintura espesa hecha con aceite, que se mezcla y se superpone"), ("acuarela", "pintura transparente que se diluye con agua"), ("grabado", "procedimiento que permite hacer muchas copias de una imagen con una plancha"), ("cerámica", "obra hecha con arcilla cocida en un horno"), ("arpillera", "obra textil hecha con retazos de tela cosidos sobre una base")],
    [
        w("Material y efecto", "Una figura de piedra de tres metros está en una colina que mira al mar. ¿Qué sensación puede dar por su material?", ["La piedra es pesada y dura mucho.", "Eso sugiere permanencia y fuerza.", "El lugar abierto la hace ver importante."], "Permanencia y fuerza"),
        w("Procedimiento y copias", "Un afiche se imprimió igual cientos de veces con una plancha. ¿Qué procedimiento se parece más: grabado o escultura única?", ["Muchas copias iguales.", "El grabado permite repetir la imagen.", "La escultura única se hace una vez."], "Grabado"),
    ],
    [
        m("Pensar que el material solo sirve para que la obra «dure» y no cambia su significado.", "El material afecta lo que vemos y sentimos.", "Pregunta cómo el material se relaciona con la idea."),
        m("Confundir acuarela con óleo.", "Una es transparente y la otra es espesa.", "Recuerda: acuarela se diluye y deja ver el papel; óleo es espeso."),
    ],
    [
        ex("¿Qué procedimiento permite hacer muchas copias de una misma imagen: el grabado o una escultura única de piedra?", "El grabado", "La plancha puede imprimirse muchas veces."),
        ex("La acuarela, ¿es transparente o cubriente?", "Transparente", "Se diluye con agua y deja ver el papel."),
        ex("Una arpillera está hecha con retazos de tela cosidos sobre una base. ¿Es un trabajo textil o de piedra?", "Textil", "Está hecha de tela."),
    ],
    [
        ex("Una escultura de piedra está al aire libre en una plaza. ¿Qué propiedad de la piedra ayuda: resiste el clima o se disuelve con la lluvia?", "Resiste el clima", "La piedra es dura y dura mucho tiempo."),
        ex("¿Qué procedimiento capta un instante real: la fotografía o modelar arcilla?", "La fotografía", "La cámara registra lo que hay frente a ella en un momento."),
        ex("Una olla de Pomaire está hecha de arcilla cocida en un horno. ¿Es cerámica o grabado?", "Cerámica", "La cerámica se hace con arcilla cocida."),
    ],
    [
        ex("Una obra suave y delicada, de colores claros y transparentes, sobre papel. ¿Qué material pudo usarse: acuarela o piedra?", "Acuarela", "La acuarela es transparente y ligera."),
        ex("Una imagen que se repitió en 100 carteles iguales. ¿Qué procedimiento se parece más: el grabado o la escultura única?", "El grabado", "El grabado produce muchas copias."),
        ex("Una figura de arcilla se secó y se coció en un horno. ¿Qué procedimiento principal se usó para darle forma: el modelado o la pintura?", "El modelado", "La arcilla se moldea con las manos antes de cocerla."),
    ],
    [
        ex("Dos obras del mismo animal. A: un cuadro de 20 cm de ancho, hecho en acuarela. B: una escultura de piedra de 2 metros. ¿Cuál da más sensación de monumento?", "La B", "El material pesado y el gran tamaño dan sensación de monumento."),
        ex("Ana dice: «El material no importa para interpretar una obra». ¿Tiene razón?", "No", "El material influye en el efecto y el significado."),
    ],
    [
        ex("Quieres interpretar una arpillera. ¿Qué dato de material ayuda más: que está hecha con retazos de tela cosidos o que pesa dos kilos?", "Que está hecha con retazos de tela cosidos", "Es un dato del procedimiento y del material."),
        ex("Pintas el mismo paisaje con acuarela y luego con óleo. ¿En cuál se ven las huellas espesas del pincel: en el óleo o en la acuarela?", "En el óleo", "El óleo es espeso y marca el pincel."),
    ],
    ex("En una feria de artesanía ves una olla de greda de Pomaire. ¿Qué procedimiento se usó: modelar la arcilla y cocerla en horno o pintar sobre tela?", "Modelar la arcilla y cocerla en horno", "Es el procedimiento de la cerámica."),
    [
        ex("Verdadero o falso: el óleo es transparente como la acuarela.", "Falso", "El óleo es espeso; la acuarela es transparente."),
        ex("¿Qué permite el grabado?", "Hacer muchas copias de una imagen", "La plancha se imprime muchas veces."),
        ex("Verdadero o falso: el material influye en lo que una obra comunica.", "Verdadero", "Cambia lo que vemos y sentimos."),
    ],
    task(
        "Elige UNA obra descrita. A) «Una acuarela de nubes suaves, con colores claros y transparentes»; B) «Una figura de piedra de tres metros en una colina»; C) «Una arpillera hecha con retazos de tela cosidos que muestra una escena de feria». Escribe: material, procedimiento, una ventaja de ese material y cómo se relaciona con lo que comunica la obra.",
        "Elegí la C. Material: retazos de tela. Procedimiento: coser sobre una base. Ventaja: con telas de colores se arma una escena con relieve. Creo que comunica la vida de una feria, porque las telas de colores muestran las frutas y las personas.",
        ["nombra material y procedimiento", "da una ventaja del material", "relaciona el material con la idea", "usa «creo que» cuando no está seguro"],
        ["cuatro datos escritos", "una frase de relación"],
        ["ignorar el material", "afirmar sin evidencia"],
        "Destaca la relación entre material e idea más clara y pregunta qué cambiaría si cambiara el material.",
    ),
    "Toca dos materiales de tu casa (una tela y un papel) y di cuál sería mejor para una obra suave y delicada.",
    "Compara dos materiales para la misma idea y escribe qué cambia en la sensación.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA4, 4,
    "Hoja, lápices de colores o témpera. Las obras que sirven de inspiración están descritas en esta clase; no necesitas copiar ninguna imagen.",
    "Aprenderé a crear una respuesta propia a una obra, tomando una idea de ella sin copiarla, y a llevar un registro de las obras que observo en el año. Sirve para interpretar mejor creando y para respetar la autoría.",
    ["Sé describir y analizar una obra.", "Sé que copiar una obra no es crear una idea propia."],
    [
        "Una forma de comprender una obra es responderle con una obra propia. No es copiarla: es tomar una idea (por ejemplo, el uso de la luz o de un tipo de pincelada) y aplicarla a mi propio tema. Un estilo es un conjunto de rasgos que se repiten en obras de un artista o de una época. Si dos obras usan pinceladas cortas y luz de un momento, comparten un estilo parecido.",
        "Para responder a una obra, hago tres pasos. Primero la miro y anoto su lenguaje visual. Segundo, elijo qué idea voy a tomar y qué voy a cambiar: el tema, los colores o el material. Tercero, creo mi versión y escribo al lado qué obra me inspiró y qué cambié. Así se respeta la autoría de la obra original y se muestra la mía.",
        "También llevo un registro de obras. Cada año conviene observar al menos 50 obras de arte y diseño chileno, latinoamericano y universal. Anoto el nombre, el lugar o país, si es arte o diseño, y una frase de descripción. Así veo cuánto he mirado y voy encontrando estilos que me gustan. Puedo mirar obras en libros, en museos, en la biblioteca o en internet con ayuda de un adulto.",
    ],
    [("estilo", "conjunto de rasgos que se repiten en las obras de un artista o de una época"), ("respuesta", "obra propia que toma una idea de otra sin copiarla"), ("registro de obras", "lista de las obras observadas con algunos datos"), ("inspirar", "dar una idea para crear otra obra"), ("autoría", "que una obra sea de quien la creó")],
    [
        w("Tomar una idea", "Obra A: un puerto al amanecer con pinceladas cortas y luz de la mañana. Quieres responderle con tu plaza. ¿Qué tomas y qué cambias?", ["Tomo la idea de las pinceladas cortas y la luz de la mañana.", "Cambio el tema: mi plaza en lugar del puerto.", "Cambio los elementos: árboles y bancas en lugar de botes."], "Tomo las pinceladas cortas y la luz; cambio el tema a mi plaza"),
        w("Escribir la fuente", "Terminaste tu plaza al amanecer. ¿Qué escribes al lado de tu obra?", ["Digo qué obra me inspiró.", "Digo qué cambié.", "Lo escribo en una frase."], "Me inspiré en «Puerto al amanecer»; cambié el tema a mi plaza"),
    ],
    [
        m("Dibujar la misma obra casi igual y decir que es una respuesta propia.", "No hay una idea propia ni una decisión nueva.", "Cambia el tema, el color o el material."),
        m("No anotar qué obra me inspiró.", "No se reconoce la autoría de la obra original.", "Escribe siempre qué obra te inspiró y qué cambiaste."),
    ],
    [
        ex("Al responder a una obra, ¿la copias o tomas una idea y la haces propia?", "Tomas una idea y la haces propia", "Una respuesta es creación nueva."),
        ex("¿Qué es un estilo?", "Un conjunto de rasgos que se repiten", "Aparecen en obras de un artista o de una época."),
        ex("Dos obras usan pinceladas cortas y luz de un momento. ¿Tienen un estilo parecido?", "Sí", "Comparten los mismos rasgos."),
    ],
    [
        ex("Quieres hacer una obra con la idea de «Puerto al amanecer» (pinceladas cortas y luz de la mañana). ¿Qué mantienes: la técnica de pinceladas cortas y la luz o los mismos botes pequeños?", "La técnica y la luz", "Los mismos botes serían una copia."),
        ex("¿Cuál es una respuesta propia: dibujar el mismo puerto con los mismos botes o pintar tu plaza al amanecer con pinceladas cortas?", "Pintar tu plaza al amanecer con pinceladas cortas", "Toma una idea y cambia el tema."),
        ex("¿Qué debes anotar al lado de tu respuesta: qué obra te inspiró y qué cambiaste o solo tu nombre?", "Qué obra te inspiró y qué cambiaste", "Así se muestran la fuente y tu autoría."),
    ],
    [
        ex("Ordena los pasos: A) elegir qué idea tomas y qué cambias, B) mirar la obra y anotar su lenguaje visual, C) crear tu versión. Escribe las letras en orden.", "B, A, C", "Primero observas, luego decides y después creas."),
        ex("Quieres responder a una calle de colores fríos y sombras largas con una versión cálida. ¿Qué cambias: los colores a cálidos o las líneas a rectas?", "Los colores a cálidos", "Los colores cálidos cambian la sensación."),
        ex("Tu registro de obras tiene 20 obras chilenas, 14 latinoamericanas y 16 de otras partes del mundo. ¿Cuántas obras llevas?", "50", "Suma los tres grupos.", calc="20+14+16"),
    ],
    [
        ex("Un compañero copió una obra y la entregó diciendo «inspirada en». ¿Es una respuesta propia?", "No", "No cambió nada ni tomó una idea."),
        ex("Ana pinta su plaza con pinceladas cortas y luz de la mañana. Luis traza el mismo puerto casi igual, con botes iguales. ¿Quién creó una respuesta más propia?", "Ana", "Tomó la idea y la aplicó a su tema."),
    ],
    [
        ex("La meta del año es observar al menos 50 obras. Ya anotaste 38. ¿Cuántas faltan para llegar a la meta?", "12", "Resta 38 de 50.", calc="50-38"),
        ex("Respondes a la figura de piedra de tres metros con una figura de cartón reciclado de alguien de tu barrio. ¿Cambiaste el material y el tema?", "Sí", "Pasaste de piedra a cartón y de una figura a una persona de tu barrio."),
    ],
    ex("Tu profesora pide una obra inspirada en un cuadro, pero tu amiga dice que basta con calcarlo y cambiar el color del cielo. ¿Qué le respondes: que debes cambiar también el tema o que tiene razón?", "Que debes cambiar también el tema", "Calcar no es crear una idea propia."),
    [
        ex("Verdadero o falso: responder a una obra es copiarla exactamente.", "Falso", "Es tomar una idea y aplicarla a algo propio."),
        ex("¿Qué se anota en un registro de obras?", "Nombre, lugar o país, si es arte o diseño, y una frase de descripción", "Son los datos básicos de cada obra."),
        ex("Verdadero o falso: el registro anual debe tener al menos 50 obras de arte y diseño.", "Verdadero", "Es la meta que propone el objetivo de aprendizaje."),
    ],
    task(
        "Elige UNA obra descrita para responderle. A) «Puerto al amanecer»: cielo naranjo, pinceladas cortas, botes pequeños, agua con manchas de azul y rosado. B) «Calle de colores fríos»: casas azules y violetas, líneas rectas, sombras largas. C) «Figura de piedra»: figura de tres metros, de pie, que mira al mar. Crea tu respuesta con otro tema. Escribe qué idea tomaste, qué cambiaste y qué obra te inspiró. Agrega tres obras a tu registro de obras.",
        "Elegí la A. Tomé las pinceladas cortas y la luz del amanecer. Cambié el tema: pinté el patio de mi casa. Me inspiré en «Puerto al amanecer»; cambié el puerto por un patio y los botes por plantas. En mi registro anoté tres obras con nombre, país y una frase.",
        ["toma una idea sin copiar", "cambia el tema o el material", "escribe qué obra la inspiró y qué cambió", "agrega obras a su registro"],
        ["respuesta visual", "frase de fuente y cambios", "tres filas del registro"],
        ["copiar la obra", "no citar la obra que inspiró"],
        "Destaca la respuesta con mayor decisión propia y pregunta qué idea de la obra original conservó.",
    ),
    "Cuenta cuántas obras de arte o diseño recuerdas haber visto este mes y dilas en voz alta.",
    "Agrega diez obras a tu registro, de tres lugares distintos, y marca cuáles son arte y cuáles diseño.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA4, 5,
    "Hoja y lápiz. Las obras se describen en esta clase. Para tu registro puedes usar libros, afiches, envases o imágenes que veas con un adulto.",
    "Aprenderé a escribir una interpretación completa de una obra o diseño, usando evidencia visual, material, contexto y origen (Chile, Latinoamérica o resto del mundo). Sirve para explicar con razones lo que una obra comunica.",
    ["Sé describir, analizar y relacionar con el contexto.", "Sé que material y lenguaje visual cambian el significado."],
    [
        "Una interpretación completa une cuatro cosas: la descripción (lo que veo), el análisis (cómo se usa el lenguaje visual y el material), el contexto (quién, cuándo, dónde y para qué) y mi idea de lo que comunica. Se puede escribir así: «Veo…; está hecha con…; fue creada en…, para…; por eso creo que comunica… porque…».",
        "Las obras pueden venir de distintos lugares. Obra chilena es la creada por un artista o diseñador de Chile, como Roberto Matta, un pintor chileno. Obra latinoamericana es la creada en un país de América Latina, como las pinturas de la artista mexicana Frida Kahlo. Obra universal es la creada en cualquier otra parte del mundo, como las pinturas del francés Claude Monet. Conocer el origen ayuda a entender el contexto, pero no es lo único que importa.",
        "También distingo arte y diseño. Una obra de arte busca sobre todo expresar una idea o una emoción. Un diseño, como un afiche o un envase, busca además cumplir una función: informar, proteger o servir. Por eso, al interpretar un diseño, pregunto: ¿para qué sirve?, ¿quién lo usa?, ¿cómo ayuda su forma a su función? Una buena interpretación nunca inventa datos: si no sé algo del contexto, digo «no lo sé» o «creo que».",
    ],
    [("obra chilena", "obra creada por un artista o diseñador de Chile"), ("obra latinoamericana", "obra creada en un país de América Latina"), ("obra universal", "obra creada en cualquier otra parte del mundo"), ("diseño", "creación que, además de expresar, cumple una función práctica"), ("interpretación completa", "explicación que une descripción, análisis, contexto e idea")],
    [
        w("Interpretar un diseño", "Obra E: «Un afiche con letras amarillas grandes sobre fondo azul oscuro, un árbol simple y la frase “Cuida tu parque”, hecho para pegarse en calles». Interprétalo.", ["Veo letras amarillas grandes sobre azul oscuro y un árbol simple.", "Es un diseño: sirve para informar y convencer.", "Creo que busca llamar la atención de quienes pasan, porque el contraste se lee desde lejos."], "Veo letras amarillas sobre azul; es un diseño para informar; creo que quiere llamar la atención porque el contraste se lee de lejos"),
        w("Clasificar por origen", "Roberto Matta, pintor chileno. Frida Kahlo, artista mexicana. Claude Monet, pintor francés. ¿Cuál obra es chilena?", ["Reviso el origen de cada artista.", "Matta es chileno.", "Kahlo es de México y Monet de Francia."], "La de Roberto Matta"),
    ],
    [
        m("Decir que una obra es «universal» solo porque es famosa.", "Universal aquí significa de cualquier otra parte del mundo, no de fama.", "Clasifica según el lugar de origen."),
        m("Inventar datos del autor o de la fecha para que la interpretación suene completa.", "Se entrega información falsa.", "Si no lo sabes, escribe «no lo sé» o «creo que»."),
    ],
    [
        ex("Obra E: «Un afiche con letras amarillas sobre fondo azul oscuro, un árbol simple y la frase “Cuida tu parque”». ¿Es una obra de arte o un diseño?", "Un diseño", "Tiene una función práctica: informar a quienes pasan."),
        ex("Roberto Matta fue un pintor chileno. Una obra suya, ¿es chilena o universal?", "Chilena", "Fue creada por un artista de Chile."),
        ex("Frida Kahlo fue una artista mexicana. Una obra suya, ¿es latinoamericana o chilena?", "Latinoamericana", "México es un país de América Latina."),
    ],
    [
        ex("En el afiche «Cuida tu parque», ¿qué colores forman el contraste: amarillo y azul oscuro o rojo y verde?", "Amarillo y azul oscuro", "La descripción nombra letras amarillas sobre azul oscuro."),
        ex("Una obra del pintor francés Claude Monet, ¿es chilena, latinoamericana o universal según esta clase?", "Universal", "Francia queda fuera de Chile y de América Latina."),
        ex("En el afiche, el contraste fuerte entre las letras y el fondo, ¿ayuda a leer desde lejos o lo dificulta?", "Ayuda a leer desde lejos", "El contraste hace que las letras se noten."),
    ],
    [
        ex("Para entender la función de un afiche, ¿qué pregunta ayuda más: «¿para qué sirve?» o «¿cuántos años tiene su autor?»?", "¿Para qué sirve?", "Un diseño se interpreta también por su función."),
        ex("Quieres interpretar un cuadro y no conoces la fecha en que se pintó. ¿Qué escribes: «no lo sé» o inventas una fecha?", "No lo sé", "No se deben inventar datos."),
        ex("Ordena las partes de una interpretación completa según la clase: A) creo que comunica…, B) veo…, C) está hecha con…, D) fue creada para…. Escribe las cuatro letras en orden.", "B, C, D, A", "El orden de la clase es descripción, análisis, contexto e idea."),
    ],
    [
        ex("Dos interpretaciones del afiche. Ana: «Es lindo». Beto: «Las letras amarillas sobre azul oscuro se leen desde lejos, y por eso creo que busca llamar la atención en la calle». ¿Cuál está mejor fundamentada?", "La de Beto", "Usa evidencia visual y una razón."),
        ex("Un compañero dice que una escultura es chilena solo porque es muy famosa. ¿Es una buena razón?", "No", "El origen depende de dónde y por quién fue creada."),
    ],
    [
        ex("Un afiche hecho en Perú, ¿es una obra chilena, latinoamericana o universal según esta clase?", "Latinoamericana", "Perú es un país de América Latina."),
        ex("Un afiche de tu barrio y un cuadro de un museo expresan ideas, pero el afiche además informa. ¿Cuál de los dos es un diseño?", "El afiche", "Tiene una función práctica."),
    ],
    ex("En clases debes presentar una obra. Sabes qué ves y con qué está hecha, pero no sabes cuándo se creó. ¿Qué dices sobre la fecha: «no sé cuándo se creó» o inventas una?", "No sé cuándo se creó", "Es honesto y no inventa datos."),
    [
        ex("Verdadero o falso: un diseño también debe cumplir una función práctica.", "Verdadero", "Además de expresar, sirve para algo."),
        ex("¿Cuáles son las cuatro partes de una interpretación completa?", "Descripción, análisis, contexto e idea", "Reúnen lo que veo, cómo está hecha, para qué y qué comunica."),
        ex("Verdadero o falso: una obra de Monet es una obra universal en esta clase.", "Verdadero", "Monet era francés."),
    ],
    task(
        "Elige UNA obra descrita. A) El afiche «Cuida tu parque». B) «Un cuadro de un puerto al amanecer con pinceladas cortas, pintado al aire libre en el siglo XIX». C) «Una escultura de piedra de una figura de pie, de tres metros, en una colina que mira al mar». Escribe una interpretación completa: lo que ves, cómo está hecha, el contexto que conoces (o «no lo sé»), y qué crees que comunica con una razón. Agrega la obra a tu registro.",
        "Elegí la B. Veo un puerto al amanecer hecho con manchas de colores. Está pintado con pinceladas cortas. Fue pintado al aire libre en el siglo XIX; no sé quién fue el autor. Creo que comunica la luz del amanecer porque los colores cambian de a poco.",
        ["describe con datos", "nombra el material o la técnica", "incluye el contexto o dice «no lo sé»", "interpreta con razón"],
        ["párrafo de interpretación", "fila del registro"],
        ["inventar datos", "opinar sin evidencia"],
        "Destaca la interpretación con mejor evidencia y pregunta qué dato de contexto cambiaría su idea.",
    ),
    "Elige un objeto con diseño de tu casa y di en voz alta para qué sirve y cómo su forma lo ayuda.",
    "Escribe dos interpretaciones distintas de la misma obra, ambas con evidencia, y compara.",
)
