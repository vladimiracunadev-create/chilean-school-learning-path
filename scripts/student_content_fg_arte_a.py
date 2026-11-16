"""Cuaderno del estudiante de Artes Visuales 3.º y 4.º medio FG: FG-ARTE-3y4-OAC-01 (experimentación en ilustración, audiovisual y multimedia)."""
from __future__ import annotations

from fg_arte_common import build

OA = "FG-ARTE-3y4-OAC-01"

# ---------------------------------------------------------------- Clase 1
build(
    OA, 1,
    "Aprenderé a observar un referente de ilustración, audiovisual o multimedia y a describir su soporte, su procedimiento, su lenguaje visual y su propósito. Sirve para decidir qué experimentar sin copiar y para juzgar con razones y no solo con gusto.",
    ["Sé que una obra se puede describir con rasgos que se ven y se oyen.", "Sé que una opinión personal no es lo mismo que un rasgo comprobable."],
    [
        "La ilustración es una imagen creada para acompañar, explicar o contar una idea, por ejemplo en un libro, un afiche o un manual. Una obra audiovisual combina imagen en movimiento y sonido, como una animación o un cortometraje. Una obra multimedia junta varios medios (texto, imagen, sonido, video) y muchas veces permite que quien la usa participe, lo que se llama interactividad. Un referente es una obra que observo para aprender de ella, no para copiarla.",
        "Para observar un referente completo una ficha con cuatro datos. El soporte es el material o medio donde está la obra, como el papel, un muro o una pantalla. El procedimiento es la manera en que se hizo, por ejemplo dibujo a lápiz, collage o fotografía cuadro a cuadro (fotografiar un objeto moviéndolo un poco entre foto y foto). El lenguaje visual es el conjunto de recursos que se ven y se oyen: línea, color (la paleta es el conjunto de colores elegidos), composición (cómo se ordenan los elementos), encuadre (qué parte de la escena se muestra), ritmo y sonido. El propósito es lo que la obra busca: informar, narrar, persuadir o expresar una emoción.",
        "Una ficha usa rasgos que cualquiera puede comprobar. «Me gusta» es un gusto personal; «las líneas finas y las etiquetas permiten reconocer cada parte» es un juicio apoyado en un criterio, que es la razón con que se juzga. Las obras de este cuaderno son de ejemplo e inventadas. Si usas obras reales, atribúyelas con su autoría y no las copies.",
    ],
    [("soporte", "material o medio donde está o se muestra una obra"), ("procedimiento", "manera en que se hizo una obra"), ("lenguaje visual", "recursos que se ven y se oyen: línea, color, composición, encuadre, ritmo, sonido"), ("propósito", "lo que la obra busca lograr"), ("interactividad", "posibilidad de que quien usa la obra participe en ella")],
    [
        ("Leer una ficha de ilustración", "Obra de ejemplo «Mapa de las abejas», de la ilustradora de ejemplo Ana Peralta: lápiz grafito y acuarela sobre papel; líneas finas; cada parte del insecto lleva una etiqueta escrita; se publicó en una guía escolar. Completa la ficha.", ["Soporte: papel.", "Procedimiento: lápiz grafito y acuarela.", "Lenguaje visual: líneas finas y etiquetas.", "Propósito probable: informar, para reconocer las partes del insecto."], "Soporte papel; procedimiento grafito y acuarela; propósito informar"),
        ("Separar gusto de juicio", "Dos comentarios sobre una animación de ejemplo hecha con recortes de papel: (1) «Es lindísima». (2) «Los recortes se mueven poco a poco y eso da una calma que acompaña la historia». ¿Cuál es un juicio con criterio?", ["El primero solo expresa gusto, sin rasgo ni razón.", "El segundo nombra un rasgo (movimiento lento de recortes) y su efecto (calma).", "Por eso el segundo se puede comprobar viendo la obra."], "El segundo, porque nombra un rasgo y su efecto"),
    ],
    [
        ("Describir una obra con «es horrible» o «es bonita» y creer que eso es observar.", "Una opinión no se puede comprobar mirando la obra.", "Anota primero rasgos concretos, como «fondo azul oscuro y recortes blancos», y deja el juicio para el final."),
        ("Confundir el soporte con el procedimiento.", "Ambos tratan de materiales y se parecen.", "El soporte es dónde está la obra; el procedimiento es cómo se hizo."),
    ],
    [
        ("abc", "En Artes Visuales, ¿qué es un soporte?", "El material o medio donde está la obra, como papel o pantalla", "El tema o la historia que cuenta la obra, por ejemplo una espera", "El conjunto de colores y líneas que se usan para hacerla", "El soporte es el lugar físico o digital de la obra; el tema y los colores son otros asuntos."),
        ("abc", "Una obra de ejemplo combina texto, imágenes y sonidos, y permite tocar un punto para abrir otro contenido. ¿Cómo se clasifica?", "Multimedia, por juntar varios medios y dejar participar", "Ilustración, porque en toda la obra hay imágenes fijas", "Audiovisual, porque tiene sonido y se puede ver en pantalla", "Reúne varios medios y es interactiva, rasgos propios de una obra multimedia."),
        ("abc", "La animación de ejemplo «La noche del paradero» se hizo moviendo recortes de papel y fotografiando cada posición. ¿Qué dato describe su procedimiento?", "Se fotografió cada posición de los recortes", "Dura dos minutos y tiene música de piano", "Se proyectó en una sala con otras personas", "Cómo se hizo la obra es el procedimiento; la duración y el lugar de muestra son otros datos."),
        ("abc", "¿Cuál de estas frases describe un rasgo que se puede comprobar en un afiche de ejemplo?", "Las letras blancas están sobre un fondo azul oscuro", "Es el afiche más original y atractivo del liceo", "A todos los estudiantes les va a encantar este afiche", "Solo la primera señala algo visible; las otras son opiniones o predicciones."),
        ("abc", "Una ilustración de ejemplo muestra el ciclo del agua con flechas y etiquetas para estudiantes. ¿Cuál es su propósito más probable?", "Informar y explicar cómo funciona el ciclo del agua", "Hacer reír al público con un dibujo exagerado", "Vender un producto escolar a quienes pasen cerca", "Las flechas y etiquetas ayudan a entender un proceso, es decir, a explicar."),
        ("abc", "Dos fichas de ejemplo: la 1 dice «soporte: pantalla; procedimiento: dibujo digital»; la 2 dice «soporte: muro; procedimiento: pintura con rodillo». ¿Qué ficha corresponde a una obra pensada para verse en una calle?", "La 2, porque su soporte es un muro", "La 1, porque usa dibujo digital y se ve en pantalla", "Ninguna, porque las fichas no dicen el público", "El muro es un soporte de calle; una pantalla se ve en un dispositivo."),
        ("abc", "Para un cortometraje de ejemplo se anota «tiene sonido de lluvia y la cámara se acerca despacio a una ventana». ¿Qué parte de la ficha completa esa nota?", "El lenguaje visual y sonoro", "El soporte donde se proyectará", "La autoría de la obra completa", "Sonido y movimiento de cámara son recursos del lenguaje de la obra."),
        ("abc", "Mapa sonoro de ejemplo: al tocar un punto del plano dibujado suena la grabación de una feria y aparece un texto breve. ¿Cuál es su propósito más probable?", "Documentar y compartir los sonidos de un lugar", "Enseñar a dibujar planos y mapas a estudiantes", "Anunciar la venta de un producto del barrio", "Une sonido, imagen y texto para dar a conocer cómo suena el lugar."),
        ("abc", "Dos descripciones del mismo mural digital de ejemplo: X) «Es el mejor del año». Y) «Tiene una paleta de tres colores y figuras repetidas que dan ritmo». ¿Cuál puede usarse como evidencia en una ficha?", "Y, porque nombra rasgos que se ven", "X, porque expresa una opinión muy fuerte y segura", "Ninguna, porque las dos son juicios sin criterio", "Una ficha necesita rasgos comprobables; «el mejor del año» no lo es."),
        ("abc", "Un grupo debe elegir un referente para experimentar con movimiento. ¿Cuál criterio es más útil para elegir?", "Que muestre con claridad cómo se logra el movimiento", "Que sea el más conocido entre sus compañeros", "Que tenga más colores y más personajes", "Para aprender un procedimiento, el referente debe dejarlo ver; la fama no enseña."),
        ("abc", "Un compañero copia al pie de la letra un afiche de ejemplo para su trabajo y dice «es mi referente». ¿Qué debería hacer?", "Tomar un recurso y transformarlo con decisiones propias", "Cambiar la firma y el título y dejar todo lo demás igual", "Pintarlo más grande para que parezca otra obra distinta", "Un referente se usa para aprender un recurso; copiarlo igual no es crear."),
        ("abc", "Una compañera dice que su animación de ejemplo es «mejor» porque tiene más colores que la de otro grupo. Ambas buscan transmitir calma. ¿Qué respuesta usa un criterio válido?", "Que habría que mirar si el ritmo y los colores producen calma, no cuántos colores hay", "Que tiene razón, porque más colores siempre es mejor en una animación", "Que depende de quién la mire primero y de cuánto le agrade", "El criterio debe ligarse al propósito; contar colores no dice si logra calma."),
        ("abc", "Una ficha dice: «soporte: papel; procedimiento: collage; propósito: expresar nostalgia». ¿Qué falta para ser una ficha completa de este cuaderno?", "El lenguaje visual, como color, composición o línea", "El precio de la obra y el lugar donde se compró", "El nombre de la persona que hace la observación", "La ficha pide soporte, procedimiento, lenguaje visual y propósito; falta el tercero."),
    ],
    ("abc", "En tu liceo se muestra el cortometraje de ejemplo «Ventana». Una persona escribe: «Los planos cerrados y el silencio hacen sentir encierro». ¿Qué debe agregar para que sea un buen juicio?", "El criterio con que juzga y el rasgo que lo respalda", "Su opinión sobre si le gustó o no el cortometraje, con más énfasis", "El nombre de los amigos que lo vieron con ella", "Un juicio necesita razón y evidencia; el gusto o los nombres no lo mejoran."),
    [
        ("ab", "La ilustradora de ejemplo Ana Peralta publica en un libro escolar. ¿Qué es el libro para su obra?", "Su soporte", "Su procedimiento", "El libro es donde se ve la obra, es decir, el soporte."),
        ("ab", "Un referente de ejemplo usa pantalla, texto y sonido para contar una historia. ¿Cuál es el lenguaje más probable?", "Multimedia", "Solo ilustración fija", "Une varios medios, por lo que es multimedia."),
        ("Verdadero o falso: se puede juzgar bien una obra sin haber descrito antes ningún rasgo.", "Falso", "Un buen juicio parte de rasgos observados y de un criterio."),
    ],
    (
        "Elige UN referente de ejemplo. A) Ilustración «Mapa de las abejas»: grafito y acuarela, líneas finas, etiquetas, para una guía escolar. B) Animación «La noche del paradero»: recortes de papel fotografiados cuadro a cuadro, fondo azul, música de piano, 2 minutos. C) Mapa sonoro del barrio: plano dibujado donde cada punto abre un sonido y un texto breve. Escribe una ficha con soporte, procedimiento, dos rasgos de lenguaje visual y propósito probable, y cierra con un juicio de dos líneas apoyado en un criterio.",
        "Elegí la B. Soporte: pantalla. Procedimiento: recortes fotografiados cuadro a cuadro. Lenguaje: fondo azul y música de piano. Propósito: narrar una espera con calma. Juicio: el movimiento lento de los recortes da calma, que es lo que el relato necesita.",
        ["completa los cuatro datos de la ficha", "incluye dos rasgos comprobables", "apoya el juicio en un criterio", "no mezcla gusto con evidencia"],
        ["ficha de observación", "juicio con criterio"],
        ["escribir solo opiniones", "confundir soporte con procedimiento"],
        "Pregunta qué rasgo respalda su juicio y qué parte de la ficha es descripción y cuál interpretación.",
    ),
    "Mira un afiche, un envase ilustrado o una pantalla de tu casa y di en voz alta su soporte, un rasgo del lenguaje visual y su propósito probable.",
    "Escribe tres frases que expliquen la diferencia entre decir «me gusta» y dar un juicio con criterio sobre un referente.",
)

# ---------------------------------------------------------------- Clase 2
build(
    OA, 2,
    "Aprenderé a explorar soportes, procedimientos y materiales de ilustración, audiovisual y multimedia haciendo pruebas pequeñas y seguras. Sirve para saber qué efecto produce cada material antes de decidir con qué trabajar.",
    ["Sé describir soporte, procedimiento, lenguaje visual y propósito de un referente.", "Sé que un referente se estudia y no se copia."],
    [
        "Explorar es hacer pruebas pequeñas para conocer qué efecto produce cada material o procedimiento. En ilustración puedes comparar grafito, lápices de colores, témpera, collage de papel rasgado y estampado con tapas limpias. En una pantalla puedes usar una aplicación gratuita de dibujo, que trabaja con capas: hojas transparentes superpuestas donde puedes cambiar un elemento sin tocar el resto. Cada soporte da una textura distinta: el papel liso, el cartón rugoso o la pantalla no tienen la misma respuesta.",
        "En audiovisual, una forma segura de explorar es la animación cuadro a cuadro. Un fotograma es una imagen fija; al mostrar varios seguidos aparece el movimiento. Con el teléfono puedes fotografiar un objeto moviéndolo un poco entre foto y foto. Si decides mostrar 10 fotogramas por segundo, un clip de 6 segundos necesita 60 fotografías. Otro recurso es el plano, que es el tamaño con que se ve lo filmado: un plano general muestra todo el lugar y un primer plano muestra un detalle, como una mano.",
        "En multimedia se combinan medios en un solo recorrido: por ejemplo texto, una grabación de audio y una imagen. Antes de decidir, anota en una bitácora, que es un cuaderno donde registras cada prueba, qué cambiaste y qué efecto viste. Trabaja con materiales limpios y seguros, sin objetos cortantes ni productos químicos. Usa fotos y sonidos propios, y pide permiso a cualquier persona que aparezca.",
    ],
    [("fotograma", "imagen fija; varias seguidas producen la sensación de movimiento"), ("plano", "tamaño con que se ve lo que se filma o se encuadra"), ("capa", "hoja transparente digital que se superpone a otras"), ("bitácora", "cuaderno donde se anotan las pruebas y sus efectos"), ("textura", "aspecto de una superficie, lisa o rugosa")],
    [
        ("Comparar materiales", "Pruebas de ejemplo para ilustrar un bosque en 5 cm de ancho: grafito da línea fina y gris; témpera con tapa da manchas redondas y llenas; papel rasgado da bordes irregulares. Quieres un bosque de siluetas con bordes suaves e irregulares. ¿Qué material eliges?", ["Criterio: bordes suaves e irregulares.", "El papel rasgado produce justo bordes irregulares.", "El grafito es fino y la tapa redondea."], "Papel rasgado, porque sus bordes irregulares calzan con el criterio"),
        ("Calcular fotogramas", "Quieres una animación de 8 segundos a 10 fotogramas por segundo. ¿Cuántas fotografías necesitas?", ["Fotogramas por segundo: 10.", "Duración: 8 segundos.", "Multiplicar: 10 por 8."], "80 fotografías"),
    ],
    [
        ("Probar un solo material y quedarse con él por costumbre.", "Sin comparar no se sabe si otro material daría un mejor efecto.", "Haz al menos dos pruebas con materiales distintos y anota el efecto de cada una."),
        ("Mover mucho el objeto entre una foto y la siguiente en la animación.", "El movimiento se ve a saltos y no continuo.", "Muévelo muy poco cada vez y repite las fotos con el mismo encuadre."),
    ],
    [
        ("abc", "En Artes Visuales, ¿qué es un fotograma?", "Una imagen fija que, junto a otras seguidas, da movimiento", "Un fragmento de sonido grabado que acompaña a las imágenes", "El borde de la pantalla donde se proyecta el video", "El movimiento aparece al pasar fotogramas seguidos; los otros dos no son imágenes."),
        ("abc", "En una aplicación de dibujo cambias el color de una nube sin alterar el cielo. ¿Qué función usaste?", "Las capas del dibujo", "El zoom de la pantalla", "El borrador completo", "Las capas separan elementos y permiten cambiar uno sin tocar el resto."),
        ("abc", "¿Cuál es una prueba segura para explorar texturas en casa?", "Estampar con una tapa plástica limpia mojada en témpera", "Quemar el borde de un papel para darle textura", "Tallar un trozo de goma con un cuchillo de cocina", "Es la única sin fuego ni objetos cortantes, como pide el trabajo seguro."),
        ("abc", "Un plano que muestra todo un patio con las personas pequeñas al fondo, ¿cómo se llama?", "Plano general", "Primer plano", "Plano de detalle", "El plano general abarca todo el lugar; los otros acercan a una parte."),
        ("abc", "Para anotar qué probaste y qué efecto viste, ¿qué herramienta de trabajo sirve?", "Una bitácora con fecha, cambio y resultado", "Un boceto de la obra final con su título y su firma", "Una lista de los materiales que compraste y su precio", "La bitácora registra el proceso de prueba y sus resultados."),
        ("abc", "Quieres un efecto de papel rugoso en una ilustración digital. ¿Qué haces primero?", "Probar una textura de papel en una capa aparte", "Cambiar de tema para evitar la textura difícil", "Borrar todo el dibujo y empezar sin capas", "Una capa aparte permite probar la textura sin dañar el resto del trabajo."),
        ("abc", "Dos pruebas de ejemplo para un cielo tormentoso: grafito suave y témpera con esponja. La obra debe verse de lejos con manchas grandes. ¿Qué conviene?", "La témpera con esponja, por sus manchas grandes", "El grafito suave, porque el gris se ve de lejos", "Ninguna, porque ambas funcionan solo de cerca", "El criterio es lectura a distancia, que logran mejor las manchas grandes de témpera."),
        ("abc", "Una animación de ejemplo dura 5 segundos y usa 8 fotogramas por segundo. ¿Cuántas fotos necesita?", "40 fotos", "13 fotos", "85 fotos", "Se multiplica 8 fotogramas por 5 segundos, no se suman."),
        ("abc", "En un recorrido multimedia de ejemplo hay una foto, un audio y un texto. Si el audio dura mucho y el texto es corto, ¿qué ajuste ayuda al público?", "Acortar el audio o dividirlo para que acompañe al texto", "Alargar el texto hasta que dure lo mismo que el audio", "Quitar la foto para que no distraiga de los demás medios", "Equilibrar los medios evita que uno canse o tape a los otros."),
        ("abc", "Una compañera quiere grabar un audio en la plaza con voces de personas desconocidas y subirlo. ¿Qué cuidado corresponde?", "Evitar voces identificables o pedir permiso a quienes se oyen", "Subirlo igual, porque la plaza es un lugar público y abierto", "Cambiar solo el título del audio para que nadie lo note", "Las voces de personas son datos personales; hace falta su consentimiento."),
        ("abc", "Probaste el mismo dibujo en papel liso y en cartón rugoso, y en el cartón la línea se corta. ¿Qué concluyes?", "Que el soporte influye en cómo se ve la línea", "Que el cartón es mejor soporte para todos los dibujos", "Que el dibujo estaba mal hecho desde un comienzo", "El efecto distinto aparece al cambiar solo el soporte."),
        ("abc", "Un grupo debe presentar una obra multimedia sin conexión a internet en la sala. ¿Qué decisión de soporte es más prudente?", "Guardar los archivos en el dispositivo y probarlos antes", "Depender de abrirlos en línea durante la presentación", "Cambiar de tema el mismo día para que cargue más rápido", "Sin red, solo funciona lo que ya está guardado y probado."),
        ("abc", "Un clip animado se ve a saltos. Moviste el objeto 3 cm entre fotos. ¿Cuál es la mejor corrección?", "Mover el objeto solo uno o dos centímetros cada vez", "Agregar música más fuerte para que los saltos se noten menos", "Aumentar mucho el tamaño del objeto en el encuadre", "Cambios más pequeños entre fotos hacen el movimiento más continuo."),
    ],
    ("abc", "Tu curso explora procedimientos para ilustrar la frase «la ciudad de noche». Tienes cartulina negra, lápices de cera claros y una aplicación de dibujo. ¿Qué plan permite comparar de verdad?", "Hacer la misma escena con cera y en la aplicación, y anotar el efecto", "Usar solo la aplicación y probar tres paletas de color distintas", "Dibujar tres escenas distintas, cada una con el mismo material", "Para comparar procedimientos se mantiene la escena y se cambian los materiales."),
    [
        ("ab", "El papel liso y el cartón rugoso, ¿qué son en una ilustración?", "Distintos soportes", "Distintos propósitos", "Son materiales donde se hace la obra, es decir, soportes."),
        ("ab", "Un plano que muestra solo una mano abriendo una carta, ¿cómo se llama?", "Primer plano o plano de detalle", "Plano general, porque muestra el lugar completo", "Muestra un detalle cercano, no todo el espacio."),
        ("Verdadero o falso: basta con probar un material para saber si es el mejor.", "Falso", "Para decidir se compara con al menos otra opción."),
    ],
    (
        "Elige UNA consigna. A) Ilustrar la frase «llegó la lluvia» en una hoja. B) Animar 4 segundos un objeto de tu casa que se mueva despacio, a 5 fotogramas por segundo (necesitas 20 fotos). C) Diseñar en papel una pantalla de mapa sonoro con tres puntos que abren tres sonidos. Haz dos pruebas con materiales o procedimientos distintos, anota en una bitácora qué cambiaste y qué efecto viste, y elige uno según una intención.",
        "Elegí la A. Prueba 1: grafito y líneas finas inclinadas; efecto: lluvia ligera. Prueba 2: témpera diluida con tapa en manchas; efecto: lluvia espesa. Mi intención es una llovizna tranquila, por eso elijo la prueba 1.",
        ["hace dos pruebas distintas", "anota qué cambió y qué efecto vio", "elige según una intención", "usa materiales seguros y propios"],
        ["dos pruebas y bitácora", "elección justificada"],
        ["probar un solo material", "no anotar el efecto"],
        "Pregunta qué cambió entre las dos pruebas y qué efecto respalda la elección.",
    ),
    "Prueba en una hoja dos formas de hacer una misma línea (lápiz suave y lápiz duro, o presionando más y menos) y describe la diferencia.",
    "Explica con tres frases cuántas fotos necesita una animación de 6 segundos a 10 fotogramas por segundo y qué harías para que el movimiento no se vea a saltos.",
)

# ---------------------------------------------------------------- Clase 3
build(
    OA, 3,
    "Aprenderé a tomar una decisión visual a partir de pruebas: comparar dos versiones, nombrar el criterio y elegir con evidencia. Sirve para que mis decisiones tengan una razón y no dependan solo del gusto.",
    ["Sé explorar soportes y procedimientos con pruebas pequeñas.", "Sé anotar en una bitácora qué cambié y qué efecto vi."],
    [
        "Una decisión visual es elegir cómo se verá o se oirá una parte de la obra: el color del fondo, el tipo de línea, el tamaño del plano, el ritmo de una animación. Para decidir bien, comparo dos versiones que cambian una sola variable, que es la única diferencia entre ellas. Si cambio dos cosas a la vez, no sabré cuál produjo el efecto. Después miro ambas con un criterio, que es la razón con que juzgo, ligada al propósito de la obra.",
        "El criterio nace del propósito. Si una ilustración informa, importa la claridad; si una animación busca calma, importa el ritmo lento; si un afiche se verá de lejos, importa el contraste. Confundir gusto con juicio es elegir lo que me gusta sin preguntarme si cumple el propósito. El gusto puede acompañar, pero la razón de la decisión es el criterio. También cuenta el soporte: un detalle muy fino se pierde en una pantalla pequeña o en un muro lejano.",
        "Registro en una bitácora la versión A, la versión B, la variable, el criterio y la elección. Guardo la versión que descarto: es evidencia de mi proceso. Una prueba pequeña con cuatro o cinco personas sirve para decidir, no para demostrar algo definitivo, y lo que diga una persona no es una verdad absoluta. Si alguien opina de forma hiriente sobre una obra mía, me quedo con lo que sirve del comentario y lo comento con una persona adulta de confianza si me afecta.",
    ],
    [("decisión visual", "elección de cómo se verá o se oirá una parte de la obra"), ("variable", "única diferencia entre dos versiones comparadas"), ("criterio", "razón con la que se juzga, ligada al propósito"), ("contraste", "diferencia marcada entre claro y oscuro o entre colores"), ("ritmo", "velocidad y repetición con que se suceden imágenes o sonidos")],
    [
        ("Comparar dos versiones", "Afiche de ejemplo para verse a 4 metros. Versión A: letras amarillas sobre fondo blanco. Versión B: letras amarillas sobre fondo azul oscuro. Todo lo demás es igual. En una prueba de ejemplo, 4 de 5 personas leyeron la B desde 4 metros y solo 1 de 5 la A. ¿Qué decides?", ["Variable: el color del fondo.", "Criterio: leerse a 4 metros.", "Resultado: 4 de 5 con B frente a 1 de 5 con A."], "Conservo la B, porque se lee mejor a 4 metros"),
        ("Elegir según el propósito", "Una animación de ejemplo busca transmitir calma. Versión 1: cambios cada medio segundo. Versión 2: cambios cada cuatro segundos. ¿Cuál eliges y por qué?", ["Propósito: calma.", "El ritmo lento calma; el rápido agita.", "Decisión: la versión 2."], "La versión 2, porque su ritmo lento calza con el propósito"),
    ],
    [
        ("Elegir la versión que «me gusta más» sin mirar el propósito.", "Se confunde gusto con juicio.", "Pregunta qué busca la obra y compara con ese criterio."),
        ("Cambiar color, tamaño y frase a la vez entre las dos versiones.", "No se sabe cuál cambio produjo el efecto.", "Cambia una sola variable por prueba."),
    ],
    [
        ("abc", "En Artes Visuales, ¿qué es una variable al comparar dos versiones de una obra?", "La única diferencia que se cambia entre ambas", "Todo lo que se ve distinto en las dos versiones", "El material más caro de los que se usan", "Si solo cambia una cosa, se puede atribuir el efecto a ella."),
        ("abc", "¿Qué significa confundir gusto con juicio?", "Elegir por lo que agrada sin revisar si cumple el propósito", "Elegir con ayuda de un criterio ligado al propósito de la obra", "Preguntar a varias personas cuál versión les gusta más", "El juicio exige un criterio; el gusto solo expresa preferencia personal."),
        ("abc", "Una ilustración busca explicar el ciclo de una planta. ¿Qué criterio es más pertinente?", "La claridad con que se distinguen las etapas", "La cantidad de colores brillantes que aparezcan", "El tamaño del marco con que se exhibe", "Si el propósito es explicar, importa que se entienda cada etapa."),
        ("abc", "Dos afiches iguales, pero uno con letras de 3 cm y otro de 6 cm de alto. Se verán desde lejos. ¿Qué variable se compara?", "El tamaño de las letras", "El color de fondo del afiche", "El tipo de papel utilizado", "Lo único que cambia es el tamaño de las letras."),
        ("abc", "Una prueba mostró que la versión B se leyó mejor. ¿Qué dato falta para registrar bien la decisión?", "El criterio con que se comparó", "La hora del día en que se hizo", "El color de las paredes de la sala", "Sin criterio no se sabe qué significa leer mejor."),
        ("abc", "Una animación de ejemplo busca humor. ¿Qué ritmo es más coherente con ese propósito?", "Cambios rápidos y movimientos exagerados", "Una sola imagen quieta con fondo gris", "Silencio total y colores apagados siempre", "El humor suele apoyarse en velocidad y exageración."),
        ("abc", "Una compañera decide usar un trazo muy fino en un cartel que se verá a 5 metros. ¿Qué problema probable tiene su decisión?", "Que el trazo fino se pierde a esa distancia", "Que el papel del cartel es de color blanco", "Que usó un solo color en todo el cartel", "La distancia exige líneas más gruesas para que se lean."),
        ("abc", "Probaste dos versiones y la A fue entendida por 3 de 4 personas y la B por 4 de 4. ¿Qué conclusión es más prudente?", "La B parece funcionar mejor, pero la muestra es pequeña", "La B es la mejor, porque quedó demostrado", "Las dos son iguales, porque casi todos entendieron", "Con cuatro personas la prueba orienta pero no demuestra."),
        ("abc", "Si descartas una versión, ¿qué conviene hacer con ella?", "Guardarla en la bitácora como parte del proceso", "Botarla para no confundirte con la versión final", "Mostrarla como si fuera la versión final elegida", "Las versiones descartadas son evidencia de cómo decidiste."),
        ("abc", "Una pieza multimedia de ejemplo se verá en un teléfono. Versión 1: texto de 8 puntos. Versión 2: texto de 14 puntos. Todo lo demás es igual. ¿Cuál conviene por el soporte?", "La versión 2, porque en pantalla pequeña la letra debe ser grande", "La versión 1, porque con letra chica cabe más texto", "Ninguna, porque el soporte no influye en la letra", "El soporte pequeño exige letra legible; el soporte influye en la decisión."),
        ("abc", "Un compañero dice: «Lo hice así porque soy el autor y punto». ¿Qué le falta a su decisión?", "Una razón ligada al propósito y una evidencia", "Más seguridad al hablar frente a todo el curso", "Un título más largo y más llamativo para la obra", "Una decisión visual necesita criterio y evidencia, no solo autoridad."),
        ("abc", "En una prueba de ejemplo, la versión con color intenso se entendió mejor, pero también era la única con un título más grande. ¿Qué se puede afirmar?", "Que no se sabe si ayudó el color o el título", "Que el color intenso fue la causa del resultado", "Que el título más grande no influyó para nada", "Cambiaron dos cosas a la vez y no se puede separar el efecto."),
        ("abc", "El propósito es expresar tristeza en una animación breve. ¿Qué decisión visual podría ayudar y es defendible?", "Colores apagados y movimientos lentos, explicando la relación", "Colores muy brillantes, porque llaman la atención", "Cualquier color, porque el gusto del autor decide", "Es defendible porque une un recurso con un propósito mediante un criterio."),
    ],
    ("abc", "Tu curso prepara un cartel para anunciar una muestra y se verá en el pasillo. Tres personas dicen: «A mí me gusta el rojo», «el azul se lee mejor», «el verde es mi color». ¿Cuál aporte conviene usar para decidir?", "Que el azul se lee mejor, si se comprueba en el pasillo", "Que el rojo les gusta, porque lo dijo una persona", "Que el verde es el color favorito de otra persona", "Solo la lectura a distancia es un criterio ligado al propósito del cartel."),
    [
        ("ab", "¿Qué criterio corresponde a un afiche que se verá de lejos?", "El contraste entre letras y fondo", "El nombre del autor y la fecha", "A distancia se necesita contraste para leer."),
        ("ab", "¿Cuántas variables conviene cambiar entre dos versiones de una prueba?", "Una", "Todas las posibles", "Así se sabe qué cambio produjo el efecto."),
        ("Verdadero o falso: guardar la versión descartada ayuda a explicar cómo decidiste.", "Verdadero", "Es evidencia del proceso de decisión."),
    ],
    (
        "Elige UNA consigna. A) Cartel de ejemplo «Feria del libro» que se verá a 4 metros. B) Animación de ejemplo de 5 segundos que transmita calma. C) Pantalla de ejemplo de un mapa sonoro que se verá en un teléfono. Haz dos versiones que cambien UNA variable, nombra el criterio ligado al propósito, pide a tres personas de tu casa o curso que comparen (o simula resultados de ejemplo escritos por ti y rotulados así) y decide cuál conservas. Guarda la versión descartada.",
        "Elegí la A. Variable: color de fondo (blanco o azul oscuro), letras amarillas. Criterio: leerse a 4 metros. Resultado de ejemplo: con azul lo leen 3 de 3; con blanco, 1 de 3. Conservo el azul y guardo la versión blanca en mi bitácora.",
        ["cambia una sola variable", "nombra un criterio ligado al propósito", "decide con evidencia", "guarda la versión descartada"],
        ["dos versiones", "tabla de resultados y decisión"],
        ["cambiar varias variables", "decidir por gusto"],
        "Pregunta qué variable cambió, qué criterio usó y qué resultado respalda su elección.",
    ),
    "Escribe una frase en dos tamaños de letra y pide a una persona que la lea desde dos distancias; anota qué tamaño funcionó mejor.",
    "Explica con tres frases por qué una versión elegida solo por gusto puede no cumplir el propósito de una obra.",
)

# ---------------------------------------------------------------- Clase 4
build(
    OA, 4,
    "Aprenderé a desarrollar una propuesta propia de experimentación: plantear una pregunta, hacer pruebas con soportes y procedimientos, elegir y revisar. Sirve para convertir mis exploraciones en un proyecto con proceso visible y autoría.",
    ["Sé comparar versiones cambiando una variable.", "Sé decidir con un criterio ligado al propósito."],
    [
        "Una propuesta de experimentación parte de una pregunta que se puede probar con materiales. Por ejemplo: «¿Cómo cambia la sensación de una escena de noche si uso papel rasgado en vez de línea de lápiz?». Luego se planifican tres pruebas: una base, una con un cambio de procedimiento y una con un cambio de soporte. Cada prueba se registra con la fecha, lo que se cambió y el efecto observado. Al final se elige una y se desarrolla una versión final.",
        "La autoría es la responsabilidad de quien crea una obra. Aunque uses un referente, las decisiones deben ser tuyas y debes anotar cuáles son: tema, composición, color, material, ritmo. Si usas imágenes, sonidos o textos de otras personas, indica la procedencia y verifica que se pueda usar. Si una persona aparece en tu video o foto, pide su consentimiento, que es su aceptación libre y previa. Con material propio evitas problemas de derechos de autor.",
        "Revisar es volver a mirar la obra con la pregunta inicial. Pregúntate si el resultado responde la pregunta, qué parte funciona y qué cambiarías. Una revisión sirve cuando es concreta: «subiría el contraste del fondo» es útil; «mejorar todo» no lo es. Organiza el tiempo en etapas con un cronograma, que es el reparto del tiempo entre las tareas. Y trabaja con materiales seguros: sin fuego, sin objetos cortantes y sin productos químicos.",
    ],
    [("autoría", "responsabilidad de quien crea una obra y de sus decisiones"), ("consentimiento", "aceptación libre y previa de una persona para aparecer o usar su imagen"), ("cronograma", "reparto del tiempo entre las tareas de un proyecto"), ("revisión", "mirar de nuevo la obra con una pregunta para decidir qué cambiar"), ("pregunta de experimentación", "pregunta que se puede responder haciendo pruebas")],
    [
        ("Formular la pregunta", "Quieres experimentar con una escena de ejemplo llamada «Mercado de madrugada». ¿Cuál es una pregunta de experimentación bien formulada?", ["Debe poder probarse con materiales.", "Debe comparar al menos dos procedimientos.", "Pregunta: ¿qué sensación da la escena con papel rasgado en vez de línea de lápiz?"], "¿Qué sensación da la escena con papel rasgado en vez de línea de lápiz?"),
        ("Repartir el tiempo", "Tienes 4 sesiones de 45 minutos: una para la pregunta y el plan, dos para pruebas y una para la versión final y la revisión. ¿Cuántos minutos hay para las pruebas?", ["Cada sesión dura 45 minutos.", "Dos sesiones son para pruebas.", "Multiplicar: 2 por 45."], "90 minutos"),
    ],
    [
        ("Hacer una sola versión final sin pruebas previas.", "No hay evidencia de que sea la mejor decisión.", "Haz al menos dos pruebas distintas y elige con un criterio."),
        ("Escribir «mejorar todo» como revisión.", "No indica qué cambiar ni con qué fin.", "Escribe cambios concretos ligados a la pregunta, como «subir el contraste del fondo»."),
    ],
    [
        ("abc", "En Artes Visuales, ¿qué es el consentimiento al usar la imagen de una persona?", "Su aceptación libre y previa para aparecer", "Una foto en la que no se ve su rostro", "El permiso de la profesora para mostrar la obra", "Solo la persona retratada puede aceptar que se use su imagen."),
        ("abc", "¿Cuál es una pregunta de experimentación que se puede probar?", "¿Cómo cambia el ritmo si muevo el objeto la mitad en cada foto?", "¿Por qué el arte ha sido siempre importante para la humanidad?", "¿Quién es el artista más famoso entre los estudiantes?", "La primera se responde haciendo pruebas con materiales."),
        ("abc", "¿Qué parte de la bitácora corresponde a la autoría?", "Las decisiones propias, como tema, material o composición", "El nombre del referente que se tomó como modelo", "Una copia exacta de la imagen de otra persona", "Autoría es responsabilizarse de las decisiones que uno toma."),
        ("abc", "Una revisión útil de un cartel dice:", "«Aumentaría el contraste del fondo para que se lea a 4 metros»", "«Habría que mejorar todo el trabajo para que quede mejor»", "«No me convence del todo, no sé bien por qué»", "Es concreta y señala un cambio ligado al propósito."),
        ("abc", "Si usarás una fotografía tomada por otra persona en tu collage digital, ¿qué debes hacer?", "Verificar que se pueda usar y anotar su procedencia", "Usarla sin decirlo, porque la cambiaste de color", "Borrar el nombre de quien la tomó para simplificar", "Usar obra ajena exige permiso o licencia y citar de dónde viene."),
        ("abc", "En una sesión de 45 minutos de animación, ¿qué orden de trabajo es más seguro?", "Preparar la escena, fotografiar con encuadre fijo y revisar", "Fotografiar sin ningún plan y cambiar de encuadre en cada foto", "Dejar la edición para otra hora sin guardar lo avanzado", "Un plan con encuadre fijo evita saltos y permite revisar."),
        ("abc", "Tu grupo quiere filmar a un compañero en un video de prueba. ¿Qué es lo primero?", "Pedirle su consentimiento y explicarle para qué se usará", "Filmarlo primero y avisarle después de terminar", "Filmarlo de espaldas sin decirle nada para que no se note", "El consentimiento debe ser previo, sin sorpresas."),
        ("abc", "Un grupo tiene 3 pruebas: base, cambio de procedimiento y cambio de soporte. ¿Qué pasa si cambian procedimiento y soporte a la vez en una sola prueba?", "No sabrán cuál de los dos cambios produjo el efecto", "Obtendrán el mejor resultado posible de la prueba", "Tendrán una prueba más clara y mucho más fácil de leer", "Se mezclan dos variables, lo que impide atribuir el efecto."),
        ("abc", "El cronograma de un grupo dice: sesión 1 plan, sesión 2 y 3 pruebas, sesión 4 versión final y revisión. Si en la sesión 3 la prueba se atrasa, ¿qué ajuste es razonable?", "Acortar la versión final y dejar la revisión breve", "Saltarse todas las pruebas y pasar a la versión final", "Entregar sin revisar nada para cumplir la fecha", "Se ajusta la etapa final de forma realista sin eliminar el proceso."),
        ("abc", "Un compañero dice que su propuesta es propia porque cambió el color del referente. ¿Qué observación corresponde?", "Debe cambiar más decisiones, como tema o composición", "Está bien así, porque con un cambio basta", "Debe cambiar únicamente el título de la obra", "Un cambio mínimo deja la obra casi igual al referente."),
        ("abc", "Tu video de ejemplo usa una música que bajaste de un sitio sin saber su licencia. ¿Qué es lo más prudente?", "Reemplazarla por un sonido propio o por música de uso permitido", "Dejarla igual, porque es un trabajo escolar", "Cambiar solo la velocidad para que no la reconozcan", "Sin permiso claro, conviene usar material propio o con uso autorizado."),
        ("abc", "Tu proyecto de ejemplo tiene una pregunta, tres pruebas y una elección, pero nadie ha anotado quién decidió el tema ni la composición. ¿Qué parte de la ficha falta?", "Las decisiones de autoría propia, con su justificación", "El precio de cada uno de los materiales que se usaron", "El nombre del colegio y del curso que lo presenta", "Sin anotar las decisiones propias no se puede distinguir lo creado de lo tomado del referente."),
        ("abc", "Una prueba falla: el papel rasgado se despega del cartón. ¿Qué conclusión de proceso es útil?", "Registrar el problema y probar otro modo seguro de fijar", "Borrar la prueba y no anotar nada para no confundir", "Culpar al material y abandonar por completo el proyecto", "Los fallos registrados son datos para decidir mejor."),
    ],
    ("abc", "Un grupo presenta el proyecto «Mercado de madrugada» con tres pruebas registradas, una elección justificada y una revisión concreta. Otro grupo solo muestra la obra final. ¿Cuál evidencia mejor la experimentación?", "El primero, porque muestra pruebas, decisión y revisión", "El segundo, porque la obra se ve más limpia y terminada", "Ambos por igual, porque la obra final es lo único que cuenta", "La experimentación se evidencia en el proceso, no solo en el resultado."),
    [
        ("ab", "¿Qué debe poder hacerse con una pregunta de experimentación?", "Probarse con materiales", "Responderse solo con una opinión", "Una pregunta de experimentación se responde mediante pruebas hechas con materiales."),
        ("ab", "Antes de usar la imagen de un compañero en un video, ¿qué se necesita?", "Su consentimiento libre y previo", "La nota que el curso le puso a su trabajo", "La aceptación debe ser libre y previa."),
        ("Verdadero o falso: una revisión como «mejorar todo» es concreta y útil.", "Falso", "Una revisión útil señala qué cambiar y para qué."),
    ],
    (
        "Elige UNA pregunta de experimentación. A) ¿Cómo cambia la sensación de la escena «Mercado de madrugada» al pasar de línea de lápiz a papel rasgado? B) ¿Cómo cambia el ritmo de una animación de 5 segundos si muevo el objeto cada vez la mitad? C) ¿Cómo cambia la lectura de una pantalla de mapa sonoro si cambio el fondo de claro a oscuro? Escribe una ficha con la pregunta, tres pruebas registradas (base, cambio de procedimiento, cambio de soporte), tu elección con el criterio, una revisión concreta y las decisiones propias que tomaste.",
        "Elegí la A. Prueba 1 base: lápiz sobre papel. Prueba 2: papel rasgado sobre el mismo papel. Prueba 3: papel rasgado sobre cartón. Criterio: sensación de movimiento del mercado. Elegí la 3, porque la textura del cartón da mayor profundidad. Revisión: subiría el contraste en el centro. Decisiones propias: tema de la feria, composición en diagonal y paleta de tres colores.",
        ["plantea una pregunta probable", "registra tres pruebas", "elige con un criterio", "anota decisiones de autoría propia"],
        ["ficha con pruebas", "elección y revisión concretas"],
        ["hacer una sola prueba", "copiar el referente sin transformarlo"],
        "Pregunta qué prueba respalda su elección y qué decisiones son propias frente al referente.",
    ),
    "Escribe una pregunta de experimentación que puedas probar en casa con papel y lápices y di qué dos pruebas harías.",
    "Explica con tres frases qué evidencia muestra tu proceso de experimentación además de la obra final.",
)
