"""Student material for 2.º medio Música, OA 07 (valorar críticamente el rol de los medios de registro y transmisión en la evolución de la música en diferentes periodos y espacios históricos).

Los casos son generales o «de ejemplo»: no se usan fechas exactas ni obras con derechos. El audio histórico, las partituras y las grabaciones reales los selecciona el docente.
Los saberes de pueblos originarios se tratan solo en general: su registro y transmisión se consultan con educadores y educadoras tradicionales.
"""
from __future__ import annotations

from student_content_mu_m2_a import L
from student_lessons import arith, ex

OA7 = "MU2M OA 07"

# ---------------------------------------------------------------- OA 07 · clase 1 (medios de registro a lo largo del tiempo)
L(
    OA7, 1,
    "Lápiz y papel. Los casos son generales o de ejemplo y están escritos en los ejercicios. Las fuentes históricas reales las selecciona tu docente.",
    "Aprenderé qué medios de registro ha tenido la música a lo largo de la historia (la memoria y la tradición oral, la escritura, la impresión, la grabación sonora y los medios digitales) y qué conserva cada uno. Sirve para valorar cómo cada medio cambió lo que sabemos de la música.",
    ["Conozco medios de registro como partitura y grabación.", "Distingo tradición oral y escrita.", "Valoro una música con razones."],
    [
        "Durante mucho tiempo la música solo existió en la memoria y se transmitió de boca en boca y de oído a oído: es la tradición oral. Esta forma conserva el sentido de comunidad y permite variantes, pero depende de que alguien recuerde y enseñe. Más tarde, distintas sociedades crearon sistemas de escritura musical que fijan las alturas y las duraciones, de modo que una pieza puede tocarse lejos de su autor y después de mucho tiempo.",
        "La impresión de partituras permitió hacer muchas copias iguales y difundir repertorios entre más personas. A partir de fines del siglo XIX aparecieron las grabaciones sonoras, que por primera vez conservaron el sonido mismo: el timbre, los adornos y el modo de interpretar de personas concretas. Poco después se sumaron la radio y el cine sonoro y, más tarde, los medios digitales, que guardan y copian música con gran facilidad.",
        "Ningún medio conserva todo. La tradición oral conserva el sentido vivo y las variantes, pero puede perder detalles si nadie la transmite. La escritura conserva la estructura, pero no el timbre exacto. La grabación conserva una interpretación concreta, pero deja afuera las variantes que no se grabaron. Valorar críticamente es preguntar qué ganó y qué perdió la música con cada medio, sin decir que uno es siempre mejor que otro.",
    ],
    [("tradición oral", "transmisión de la música de boca en boca y de oído a oído"), ("escritura musical", "sistema de signos para anotar alturas y duraciones"), ("impresión", "técnica para hacer muchas copias iguales"), ("grabación sonora", "registro del sonido mismo"), ("medio digital", "soporte que guarda y copia música en forma de datos"), ("valorar críticamente", "juzgar con razones lo que se gana y se pierde")],
    [
        ("Qué conserva cada medio", "Una melodía se transmite siempre de oído a oído en una comunidad y cada persona la canta con pequeñas diferencias. ¿Qué conserva este medio y qué puede perder?", ["Conserva el sentido comunitario y las variantes.", "Puede perder detalles si nadie la enseña."], "Conserva comunidad y variantes; puede perder detalles si no se transmite"),
        ("Relacionar medio y cambio", "Una pieza se publica en partituras impresas y llega a muchas ciudades. ¿Qué cambió gracias a la impresión?", ["Se hacen muchas copias iguales.", "Llega a más personas."], "Se difundió a más personas con copias iguales"),
    ],
    [
        ("Pensar que un medio nuevo hace inútiles a los anteriores.", "Cada medio conserva cosas que otros no.", "Compara qué gana y qué pierde cada uno."),
        ("Creer que la grabación conserva «toda» la música.", "Solo conserva la interpretación que se grabó, no todas las variantes.", "Reconoce los límites del medio."),
    ],
    [
        ex("¿Qué es la tradición oral? A) Transmisión de boca en boca y de oído a oído. B) Un tipo de partitura.", "A", "Así se define."),
        ex("¿Qué fija una escritura musical? A) Las alturas y las duraciones. B) El color de la voz.", "A", "Eso registra la escritura."),
        ex("¿Qué conservó por primera vez la grabación sonora? A) El sonido mismo. B) La partitura.", "A", "Registró el sonido."),
    ],
    [
        ex("¿Qué permitió la impresión de partituras? A) Hacer muchas copias iguales y difundir repertorios. B) Eliminar la tradición oral.", "A", "Facilitó la difusión."),
        ex("¿Qué puede perder la tradición oral? A) Detalles si nadie la transmite. B) Todas las variantes siempre.", "A", "Depende de la transmisión."),
        ex("¿Qué no conserva la escritura musical con exactitud? A) El timbre de una intérprete concreta. B) Las alturas.", "A", "El timbre no se fija en los signos."),
    ],
    [
        ex("Un estudiante dice: «Con la grabación ya no hace falta enseñar canciones.» ¿Qué respuesta es crítica? A) La grabación conserva una interpretación, pero no reemplaza la transmisión viva con sus variantes. B) Tiene razón.", "A", "Cada medio conserva algo distinto."),
        ex("¿Qué medio conserva mejor el timbre y los adornos de una intérprete? A) La grabación sonora. B) La partitura.", "A", "Guarda el sonido real."),
        arith("En un archivo de ejemplo hay 12 partituras impresas, 8 grabaciones y 5 transcripciones escritas de canciones orales. ¿Cuántos documentos hay?", "12+8+5", "Se suman los documentos.", " documentos"),
    ],
    [
        ex("Un archivo de ejemplo guarda de una canción oral solo la partitura. ¿Qué perdió respecto a la tradición viva? A) Variantes, timbre y el contexto de uso. B) Las alturas.", "A", "La escritura no guarda esos aspectos."),
        ex("Otra persona dice: «La tradición oral es inferior porque no se escribe.» ¿Qué corrección es correcta? A) Conserva aspectos que la escritura no registra, como el sentido comunitario. B) Tiene razón, porque solo lo escrito es confiable.", "A", "No hay medios superiores en todo."),
    ],
    [
        ex("Para estudiar la música de un periodo anterior a la grabación sonora, ¿qué fuentes se pueden usar? A) Partituras, descripciones escritas y objetos o instrumentos conservados. B) Grabaciones de esa época.", "A", "No existían grabaciones."),
        ex("Un grupo comparó tres medios para conservar una canción. ¿Qué conclusión es más completa? A) Conviene combinar medios porque cada uno conserva cosas distintas. B) Hay que elegir solo uno.", "A", "Los medios se complementan entre sí."),
    ],
    [ex("Tu curso quiere conservar una canción de una abuela de la comunidad con su permiso. ¿Qué combinación es más completa? A) Grabación de la interpretación y anotación escrita del texto y del contexto. B) Solo un dibujo.", "A", "Combina sonido y escritura.")],
    [
        ex("¿Verdadero o falso? Ningún medio de registro conserva toda la música.", "Verdadero", "Cada uno tiene límites."),
        ex("¿Qué es un medio digital? A) Un soporte que guarda y copia música como datos. B) Un instrumento de cuerdas.", "A", "Es un soporte de datos."),
        ex("¿Qué significa valorar críticamente un medio? A) Preguntar qué gana y qué pierde la música. B) Decir cuál es el mejor.", "A", "Requiere razones, no preferencias."),
    ],
    (
        "Elige tres medios (tradición oral, partitura y grabación) y completa una tabla de ejemplo con dos columnas: «qué conserva» y «qué puede perder» para una canción de cuna ficticia. Termina con una frase que valore críticamente la combinación de los tres.",
        "Oral: conserva el sentido de comunidad y las variantes; puede perder detalles si no se enseña. Partitura: conserva alturas y duraciones; pierde el timbre y las variantes. Grabación: conserva el sonido de una interpretación; pierde las variantes no grabadas. Combinados se complementan y dan una imagen más completa.",
        ["tres medios con lo que conservan y pierden", "frase de valoración con razones", "no declara un medio como el mejor"],
        ["tabla de tres filas y frase final"],
        ["decir que un medio lo conserva todo", "no mencionar qué se pierde"],
        "Reconoce la tabla y pide agregar una pérdida por medio.",
    ),
    "Anota qué medios de registro usas tú en tu vida diaria para guardar música y qué conserva cada uno.",
    "Conversa con una persona mayor sobre cómo se transmitían las canciones en su juventud y anota un medio que usaban.",
)

# ---------------------------------------------------------------- OA 07 · clase 2 (transmisión y espacios)
L(
    OA7, 2,
    "Lápiz y papel. Los espacios y recorridos de las músicas son de ejemplo y están escritos en los ejercicios. Las fuentes reales las selecciona tu docente.",
    "Aprenderé cómo cambia el alcance y el uso de la música según el medio de transmisión (la comunidad, la copia, la radio, el disco y las redes) y el espacio donde se escucha. Sirve para valorar cómo se difundieron y se transformaron las músicas en distintos lugares.",
    ["Conozco medios de registro.", "Relaciono música y contexto.", "Describo función y propósito."],
    [
        "La transmisión es el modo en que una música pasa de una persona o lugar a otros. Hay transmisión directa, cuando quien sabe la música la enseña en persona; por copia, cuando se reproducen partituras o letras; y por medios masivos, como la radio, los discos y las plataformas en línea, que llegan a muchas personas al mismo tiempo y a gran distancia.",
        "El espacio también influye. En una comunidad pequeña la música se transmite en fiestas, trabajos y rituales de la vida cotidiana. En una sala de conciertos se escucha con atención y silencio. En la radio se escucha mientras se hacen otras cosas. En las plataformas en línea cada persona elige qué escuchar y cuándo. El espacio cambia cómo se hace y cómo se escucha la música: su duración, su volumen y su propósito.",
        "Los medios de transmisión permiten que una música cruce fronteras y se mezcle con otras, y así aparecen estilos nuevos. También hay desafíos: puede perderse el contexto de origen, sentirse una música como si fuera de otro lugar, o quedar fuera quienes no tienen acceso a los medios. Valorar críticamente es preguntar quién tiene acceso, quién decide qué se difunde y cómo se reconoce a quienes crearon la música.",
    ],
    [("transmisión", "paso de una música de una persona o lugar a otros"), ("medio masivo", "medio que llega a muchas personas a la vez"), ("difusión", "hacer conocida una música"), ("contexto de origen", "lugar, momento y personas donde nació la música"), ("acceso", "posibilidad real de llegar a una música"), ("mezcla", "unión de rasgos de músicas distintas")],
    [
        ("Comparar alcance", "Una canción de ejemplo se enseña en persona en un pueblo y luego se transmite por radio a todo el país. ¿Qué cambia en su alcance?", ["La enseñanza en persona llega a pocas personas.", "La radio llega a muchas a la vez."], "Pasa de pocas personas a muchas, y a más distancia"),
        ("Relacionar espacio y escucha", "Una pieza de ejemplo se toca en una sala de conciertos y la misma música se oye en una radio mientras la gente cocina. ¿Qué cambia en la escucha?", ["En la sala se escucha con atención.", "En la radio se escucha como fondo."], "La atención: en la sala es concentrada y en la radio, de fondo"),
    ],
    [
        ("Pensar que los medios masivos hacen que todas las músicas suenen igual.", "Los medios también permiten difundir músicas diversas.", "Pregunta qué se difunde, quién decide y quién tiene acceso."),
        ("Olvidar el contexto de origen al difundir una música.", "Se pierde su sentido y se desconoce a quienes la crearon.", "Cuenta de dónde viene y quién la creó."),
    ],
    [
        ex("¿Qué es la transmisión directa? A) Quien sabe la música la enseña en persona. B) La música llega por radio.", "A", "Es persona a persona."),
        ex("¿Cuál es un medio masivo? A) La radio. B) Una enseñanza uno a uno.", "A", "Llega a muchas personas."),
        ex("¿Qué es el acceso? A) La posibilidad real de llegar a una música. B) Una partitura.", "A", "Se refiere a la posibilidad de llegar."),
    ],
    [
        ex("Una canción de ejemplo se difunde por plataformas en línea y llega a otro continente. ¿Qué permite este medio? A) Que cruce fronteras y se mezcle con otras músicas. B) Que cada música quede aislada en su lugar.", "A", "Los medios facilitan el cruce de fronteras."),
        ex("¿Qué cambia entre escuchar en una sala y escuchar en la radio? A) La forma de atención y el propósito. B) Las alturas de las notas.", "A", "El espacio cambia la escucha."),
        ex("¿Qué se pregunta al valorar críticamente la difusión? A) Quién tiene acceso y quién decide qué se difunde. B) Cuál es la más rápida.", "A", "Examina acceso y decisión."),
    ],
    [
        ex("Un pueblo de ejemplo enseña una canción en las fiestas. Una radio la difunde sin decir de dónde viene. ¿Qué se pierde? A) El contexto de origen y el reconocimiento. B) La melodía.", "A", "Se omite su procedencia."),
        arith("Una canción de ejemplo es escuchada por 40 personas en una fiesta del pueblo y por 600 personas por radio. ¿Cuántas personas más la escucharon por radio que en la fiesta?", "600-40", "Se restan los públicos.", " personas"),
        ex("¿Qué desafío tiene la difusión masiva? A) Que quienes no tienen acceso queden fuera. B) Que todas las personas la escuchen.", "A", "Hay desigualdad de acceso."),
    ],
    [
        ex("Una estudiante dice: «Si una canción es famosa, es mejor.» ¿Qué responde alguien crítico? A) La fama depende de los medios y no mide por sí sola la calidad. B) Tiene razón.", "A", "Difusión y calidad son cosas distintas."),
        ex("Un grupo comenta que una canción de tradición oral cambia al pasar de una comunidad a otra. ¿Qué explicación es correcta? A) Cada comunidad la adapta a su contexto. B) Se debe a que alguien la grabó con errores.", "A", "La transmisión oral produce variantes."),
    ],
    [
        ex("Para difundir una canción de una comunidad de manera respetuosa, ¿qué conviene hacer? A) Pedir permiso, contar su origen y reconocer a quienes la cantan. B) Cambiar el nombre y presentarla como propia.", "A", "Se respeta a la comunidad."),
        ex("Una música de ejemplo se hizo para escucharse en silencio y hoy se escucha de fondo en una tienda. ¿Qué cambió? A) Su propósito y la manera de escucharla. B) Su melodía.", "A", "El espacio cambia el uso."),
    ],
    [ex("Tu curso presenta una canción tradicional en una feria escolar y la sube a un espacio acordado con la docente. ¿Qué dato debe acompañarla? A) De qué lugar viene, quiénes la cantan y qué permisos hay. B) Solo el título.", "A", "Entrega el contexto.")],
    [
        ex("¿Verdadero o falso? Los medios masivos permiten que una música cruce fronteras.", "Verdadero", "Aumentan el alcance."),
        ex("¿Qué es el contexto de origen? A) Lugar, momento y personas donde nació la música. B) El volumen de la grabación.", "A", "Es la procedencia."),
        ex("¿Qué permite la mezcla? A) Que aparezcan estilos nuevos. B) Que las músicas desaparezcan.", "A", "Es uno de sus efectos."),
    ],
    (
        "Elige una música de ejemplo (ficticia) y describe su recorrido en tres etapas: primero se transmite en persona en una comunidad, luego se copia por escrito y luego se difunde por un medio masivo. Para cada etapa escribe quién la oye, qué cambia y una pregunta crítica (acceso, decisión o reconocimiento).",
        "Etapa 1: la oyen vecinos, cambia con cada persona que la canta; pregunta: ¿quién decide cómo se enseña? Etapa 2: la leen quienes saben leer, queda más fija; pregunta: ¿quién tiene acceso a la copia? Etapa 3: la oyen miles, puede perder el contexto; pregunta: ¿se reconoce a quienes la crearon?",
        ["tres etapas con público y cambio", "una pregunta crítica por etapa", "no inventa datos históricos"],
        ["recorrido de tres etapas con preguntas"],
        ["usar fechas o hechos dudosos", "olvidar el contexto de origen"],
        "Reconoce las etapas y pide formular mejor una pregunta de acceso.",
    ),
    "Anota cómo te llegó una canción que te gusta y qué medios usó para llegar a ti.",
    "Pregunta a una persona de tu casa cómo se difundían las canciones cuando era joven y compara con hoy.",
)

# ---------------------------------------------------------------- OA 07 · clase 3 (cómo los medios transforman la música)
L(
    OA7, 3,
    "Lápiz y papel. Los casos son de ejemplo y están escritos en los ejercicios. Las fuentes históricas reales las selecciona tu docente.",
    "Aprenderé cómo los medios de registro y transmisión han influido en la música (su duración, su forma, su difusión, su autoría y su conservación) y cómo valorarlos críticamente. Sirve para entender por qué la música cambia con las tecnologías y con los espacios.",
    ["Conozco medios de registro y transmisión.", "Relaciono música y espacio.", "Valoro con razones."],
    [
        "Los medios de registro y transmisión influyen en cómo se hace la música. Un soporte con límite de tiempo lleva a hacer piezas que quepan en él: si un disco de ejemplo permite 4 minutos por lado, las canciones tienden a ajustarse a ese tiempo. La radio favorece piezas que se entiendan rápido. Las plataformas en línea facilitan escuchar piezas de cualquier duración y mezclar estilos.",
        "También cambian la forma de crear y de compartir. Con la escritura, una persona compone sin la presencia de quien tocará. Con la grabación, un grupo puede trabajar por capas, grabando cada voz o instrumento por separado. Con las copias digitales, cualquier persona puede reproducir una pieza, y por eso se vuelve importante la autoría: reconocer quién la creó y respetar los permisos de uso.",
        "Para valorar críticamente se mira el efecto en tres planos: lo que ganó la música (alcance, conservación, nuevas formas), lo que perdió o corre riesgo (contexto, variantes, reconocimiento de la autoría) y qué desigualdades de acceso hay. Una conclusión crítica no dice «lo nuevo es mejor» ni «lo antiguo es mejor»: dice qué cambió, para quién y con qué consecuencias.",
    ],
    [("soporte", "objeto o sistema donde se guarda un registro"), ("capas", "voces o instrumentos grabados por separado y unidos después"), ("autoría", "reconocimiento de quien creó una obra"), ("permiso de uso", "autorización para copiar o difundir una obra"), ("consecuencia", "efecto de un cambio"), ("desigualdad de acceso", "diferencia entre quienes pueden y no pueden llegar a un medio")],
    [
        ("Relacionar soporte y duración", "Un soporte de ejemplo permite hasta 5 minutos de música por lado. Una compositora de ejemplo quiere que su pieza de 8 minutos se publique en ese soporte. ¿Qué decisiones puede tomar?", ["La pieza supera el tiempo del lado.", "Puede acortarla o dividirla en dos partes."], "Acortarla o dividirla en dos partes para que quepa"),
        ("Valorar ganancias y pérdidas", "Un grupo de ejemplo graba cada voz por separado y las junta. ¿Qué gana y qué riesgo corre?", ["Gana precisión y posibilidad de corregir.", "Puede perder el sonido espontáneo de tocar juntos."], "Gana precisión y corrección; arriesga perder la espontaneidad de tocar juntos"),
    ],
    [
        ("Decir que la tecnología siempre mejora la música.", "La tecnología cambia la música: gana unas cosas y pierde otras.", "Describe qué cambió, para quién y con qué consecuencias."),
        ("Copiar o difundir una pieza sin pensar en la autoría.", "Se desconoce el trabajo de quien la creó y se pueden vulnerar sus derechos.", "Indica la autoría y pide permiso cuando corresponda."),
    ],
    [
        ex("¿Qué es un soporte? A) El objeto o sistema donde se guarda un registro. B) Un tipo de melodía.", "A", "Es donde se guarda."),
        ex("¿Qué es trabajar por capas? A) Grabar cada voz por separado y unirlas. B) Tocar todo junto sin grabación.", "A", "Es la técnica descrita."),
        ex("¿Qué es la autoría? A) El reconocimiento de quien creó una obra. B) El volumen de la obra.", "A", "Se refiere a la creación."),
    ],
    [
        ex("Un soporte de ejemplo limita el tiempo. ¿Qué efecto puede tener en las piezas? A) Tienden a ajustarse a esa duración. B) Se hacen siempre infinitas.", "A", "El soporte condiciona la duración."),
        ex("¿Qué efecto tuvo la copia digital sobre la autoría? A) Hizo más necesario reconocerla y respetar permisos. B) La volvió innecesaria.", "A", "Al poder copiar fácilmente se vuelve clave."),
        ex("¿Qué se mira para valorar críticamente un medio? A) Lo que ganó la música, lo que perdió y las desigualdades de acceso. B) Solo cuántas personas lo usan.", "A", "Son los tres planos."),
    ],
    [
        arith("Un soporte de ejemplo permite 6 minutos por lado y tiene dos lados. Se quieren publicar cuatro piezas de 3, 4, 5 y 6 minutos. ¿Cuántos minutos suman las piezas?", "3+4+5+6", "Se suman las duraciones.", " minutos"),
        ex("Un soporte de ejemplo permite 12 minutos en total (6 por lado) y se quieren publicar piezas que suman 18 minutos. ¿Qué ocurre? A) No caben todas en un solo soporte. B) Caben todas.", "A", "18 es mayor que 12."),
        ex("Una persona sube la pieza de otra a una plataforma sin su permiso y sin nombrarla. ¿Qué problema hay? A) Se desconoce la autoría y se pueden vulnerar sus derechos. B) Ninguno.", "A", "Falta reconocimiento y permiso."),
    ],
    [
        ex("Un estudiante dice: «Gracias a la grabación, la música de cualquier lugar está al alcance de todos.» ¿Qué matiz crítico agregarías? A) No todas las personas tienen el mismo acceso a los medios. B) Es completamente cierto.", "A", "Existen desigualdades de acceso a los medios."),
        ex("Una banda de ejemplo graba por capas y logra un sonido muy pulido, pero siente que perdió la energía de tocar en vivo. ¿Cómo se valora esto? A) Como una ganancia en precisión y una pérdida de espontaneidad. B) Solo como una ganancia.", "A", "Hay ventajas y pérdidas."),
    ],
    [
        ex("Para decidir si un medio ayudó a una música, ¿qué evidencia es más útil? A) Comparar cómo era antes y después, y quiénes accedieron. B) Su popularidad hoy.", "A", "Se compara el cambio y el acceso."),
        ex("Un grupo comunitario no tiene internet. ¿Qué medio de difusión puede usar? A) Presentaciones presenciales y copias impresas o grabaciones compartidas en persona. B) Solo plataformas en línea.", "A", "Hay alternativas de difusión."),
    ],
    [ex("Tu curso quiere publicar una canción en línea. ¿Qué paso es respetuoso con la autoría? A) Nombrar a quien la creó y comprobar los permisos de uso. B) Publicar sin mirar.", "A", "Se cuida la autoría.")],
    [
        ex("¿Verdadero o falso? Un medio nuevo siempre mejora la música en todo.", "Falso", "Gana unas cosas y pierde otras."),
        ex("¿Qué es un permiso de uso? A) Autorización para copiar o difundir una obra. B) Un tipo de soporte.", "A", "Es el permiso para usarla."),
        ex("¿Qué se evita en una conclusión crítica? A) Decir que lo nuevo es siempre mejor. B) Mencionar el acceso.", "A", "Una conclusión crítica no simplifica."),
    ],
    (
        "Elige un medio (soporte con límite de tiempo, radio, grabación por capas o copia digital) y escribe un análisis crítico de tres frases con un caso de ejemplo: qué ganó la música, qué corre riesgo de perderse y qué desigualdad de acceso podría haber. Agrega una acción respetuosa con la autoría.",
        "Medio: grabación por capas. Ganó precisión y la posibilidad de corregir cada voz. Corre riesgo de perder la espontaneidad de tocar en vivo. No todos los grupos tienen equipos para grabar así. Acción: nombrar a cada integrante que aportó una capa.",
        ["ganancia, pérdida y desigualdad de acceso", "una acción respetuosa con la autoría", "no declara que lo nuevo sea mejor"],
        ["análisis de tres frases y una acción"],
        ["afirmar que el medio solo trae ventajas", "no mencionar el acceso"],
        "Reconoce el análisis y pide precisar la pérdida con un ejemplo.",
    ),
    "Anota un cambio que viste en la forma de escuchar música en tu familia y qué medio lo provocó.",
    "Explica a una persona de tu casa por qué es importante nombrar a quien creó una canción al compartirla.",
)

# ---------------------------------------------------------------- OA 07 · clase 4 (crear un registro propio de una música de la comunidad)
L(
    OA7, 4,
    "Lápiz y papel. La ficha y los casos son de ejemplo. El registro real de una música de la comunidad (grabación, anotación) se hace con permiso y con la guía de tu docente; aquí se practica el diseño.",
    "Aprenderé a diseñar el registro de una música de mi comunidad: elegir el medio, pedir permiso, completar una ficha y valorar críticamente lo que el registro conserva y deja afuera. Sirve para cuidar y compartir una música con respeto.",
    ["Conozco medios de registro y transmisión.", "Reconozco el contexto de origen.", "Respeto la autoría."],
    [
        "Registrar una música de la comunidad es una forma de cuidarla y compartirla. Antes de hacerlo se pide permiso a quienes la cantan o tocan, se explica para qué se usará el registro y quién lo verá, y se acuerda si pueden aparecer sus nombres o sus voces. Si la música tiene un sentido especial para la comunidad o para un pueblo originario, se consulta a sus educadores o educadoras tradicionales y se sigue su indicación sobre qué puede registrarse y qué no.",
        "Se elige el medio según el propósito: una grabación de audio conserva el sonido, un video suma gestos, una anotación escrita conserva el texto y el contexto, y una partitura simple conserva la melodía. Se completa una ficha con: título o descripción, quién la interpreta, para qué se usa, en qué situación se canta o toca, qué medio se usó y qué permisos se obtuvieron. No se anotan datos personales innecesarios.",
        "Al final se valora críticamente el registro: qué conserva, qué deja afuera (las variantes, el ambiente, el sentido vivo) y cómo se devolverá a la comunidad. Un buen registro se comparte con quienes lo hicieron posible y se guarda de forma segura. El registro nunca reemplaza a la transmisión viva: complementa.",
    ],
    [("registro", "forma de dejar guardada una música"), ("consentimiento", "permiso libre e informado de las personas"), ("ficha de registro", "documento con los datos esenciales de una música"), ("devolución", "compartir el resultado con quienes participaron"), ("educador o educadora tradicional", "persona reconocida por su pueblo para enseñar sus saberes"), ("sentido vivo", "significado que la música tiene en la vida de una comunidad")],
    [
        ("Reconocer el paso previo", "Una estudiante quiere grabar a una vecina que canta una canción de cuna de ejemplo. ¿Qué paso va antes de grabar?", ["La vecina debe decidir.", "Hay que explicar para qué se usará y pedir permiso."], "Pedir y obtener su permiso, explicando para qué se usará"),
        ("Completar una ficha", "Datos de ejemplo: canción de cuna; la canta una vecina; sirve para calmar a los bebés; se grabó en audio; la vecina dio su permiso. La ficha tiene seis campos (título o descripción, quién, para qué, situación, medio, permisos). ¿Qué campo no está cubierto?", ["Hay descripción, quién, para qué, medio y permisos.", "No se dice cuándo ni dónde se canta."], "La situación en que se canta (cuándo y dónde)"),
    ],
    [
        ("Grabar sin avisar para «no incomodar».", "Se vulnera el derecho de la persona a decidir sobre su voz.", "Pide permiso antes de grabar y explica para qué."),
        ("Pensar que el registro reemplaza la transmisión viva.", "El registro conserva una versión y deja afuera variantes y sentido vivo.", "Considéralo un complemento de la transmisión."),
    ],
    [
        ex("¿Qué es el consentimiento? A) Un permiso libre e informado. B) Un tipo de soporte.", "A", "Es el permiso de las personas."),
        ex("¿Qué es una ficha de registro? A) Un documento con los datos esenciales de una música. B) Una partitura larga.", "A", "Organiza la información."),
        ex("¿Qué se hace antes de grabar a una persona? A) Pedir permiso y explicar para qué se usará. B) Grabar y después avisar.", "A", "El permiso va primero."),
    ],
    [
        ex("Una música tiene un sentido especial para un pueblo originario. ¿A quién se consulta? A) A sus educadores o educadoras tradicionales. B) A quien tenga más seguidores en redes.", "A", "Ellos orientan qué se puede registrar."),
        ex("¿Qué datos se evitan en la ficha? A) Datos personales innecesarios. B) El título.", "A", "Se protege la privacidad."),
        ex("¿Qué conserva una anotación escrita del texto y el contexto? A) El texto y la situación de uso. B) El timbre exacto.", "A", "Eso es lo que anota."),
    ],
    [
        ex("Una persona acepta que se grabe su canción pero no quiere que su nombre aparezca. ¿Qué hace el grupo? A) Respeta su decisión y anota «persona de la comunidad». B) Escribe su nombre igual.", "A", "Se respeta su voluntad."),
        ex("Un grupo grabó una canción en tres tomas de 4 minutos cada una. ¿Cuántos minutos de grabación tiene? A) 12. B) 7.", "A", "3 × 4 = 12 minutos."),
        arith("Una ficha de ejemplo tiene seis campos. Un grupo completó cuatro. ¿Cuántos campos le faltan?", "6-4", "Se restan los campos completos del total.", " campos"),
    ],
    [
        ex("Un registro de audio de una canción oral conserva muy bien el sonido, pero no el momento en que se canta en la comunidad. ¿Cómo se valora? A) Conserva el sonido y deja afuera el ambiente y el sentido vivo. B) Lo conserva todo.", "A", "El registro tiene límites claros."),
        ex("Un compañero dice: «Con la grabación ya no hace falta que nadie la cante.» ¿Qué responde alguien crítico? A) El registro complementa la transmisión viva, no la reemplaza. B) Tiene razón.", "A", "La transmisión viva sigue siendo importante."),
    ],
    [
        ex("Después de registrar una canción, ¿qué acción respeta a la comunidad? A) Compartir el resultado con quienes participaron y acordar cómo se usará. B) Guardarlo sin avisar.", "A", "Es la devolución."),
        ex("Tu curso grabó con permiso a una abuela cantando. Alguien propone subirlo a un espacio abierto para todos. ¿Qué paso hay que dar primero? A) Consultar a la abuela y a la docente sobre ese uso. B) Subirlo de inmediato.", "A", "El uso debe acordarse."),
    ],
    [ex("Para una muestra del colegio quieres presentar la música de tu comunidad. ¿Qué plan es más completo? A) Pedir permiso, completar la ficha, elegir el medio y devolver el registro. B) Presentar solo el título.", "A", "Incluye los pasos clave.")],
    [
        ex("¿Verdadero o falso? Un registro puede reemplazar totalmente a la transmisión viva.", "Falso", "El registro solo complementa la transmisión."),
        ex("¿Qué es la devolución? A) Compartir el resultado con quienes participaron. B) Guardar en secreto.", "A", "Reconoce a la comunidad."),
        ex("¿Qué conserva una partitura simple? A) La melodía. B) Todo el ambiente.", "A", "Conserva alturas y duraciones."),
    ],
    (
        "Diseña un registro de ejemplo de una música de tu comunidad (inventa el caso, sin datos personales ni letras reales). Escribe a) a quién pedirías permiso y qué explicarías, b) el medio que elegirías y por qué, c) los seis campos de la ficha, d) qué dejaría afuera el registro y cómo lo devolverías a la comunidad.",
        "a) Pediría permiso a la señora que canta en las fiestas y le explicaría que es para el archivo del curso. b) Grabación de audio y anotación escrita del contexto, porque conservan sonido y situación de uso. c) Descripción: canto de fiesta; quién: una vecina; para qué: animar; situación: fiesta de fin de año; medio: audio; permisos: sí. d) Dejaría afuera el ambiente de la fiesta; le entregaría una copia a ella y a la junta de vecinos.",
        ["pide permiso y explica el propósito", "medio justificado", "seis campos completos", "limitación del registro y devolución"],
        ["respuestas a), b), c) y d) escritas"],
        ["omitir el permiso", "creer que el registro lo conserva todo"],
        "Reconoce el diseño y pide agregar una pérdida del registro y cómo se compartirá.",
    ),
    "Anota una música de tu comunidad que valga la pena registrar y a quién le pedirías permiso.",
    "Con una persona adulta de tu casa, completa los seis campos de la ficha para una canción que conozca.",
)
