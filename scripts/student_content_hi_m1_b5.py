"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 14 (ocupación de la Araucanía y despojo territorial mapuche)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 14"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet. Los nombres y las formas tradicionales mapuche los enseñan las comunidades y los educadores tradicionales."

# ---------------------------------------------------------------- Clase 1
F1 = "Línea de tiempo: 1861, el coronel Cornelio Saavedra propone avanzar con fuertes y poblados hasta la ribera del río Malleco; 1862, se refunda Angol y se funda Mulchén; 1866, ley sobre fundación de pueblos y entrega de tierras a colonos; 1881, levantamiento mapuche y fundación de Temuco; 1883, se refunda Villarrica y termina la ocupación militar; 1884, comienza a funcionar la Comisión Radicadora de Indígenas, que entrega títulos de merced; durante la década de 1890, el ferrocarril llega a Temuco."
build(
    OA, 1, F1,
    use="Aprenderé a ubicar en el tiempo y el espacio la ocupación de la Araucanía y a explicar que fue una política de Estado con consecuencias profundas para la sociedad mapuche. Sirve para entender el origen de reclamos de tierras que continúan hoy.",
    prior=["Conozco la ocupación del sur y la soberanía.", "Sé leer una línea de tiempo y un mapa.", "Sé que el pueblo mapuche habitaba el centro-sur de Chile."],
    explain=[
        "Hasta mediados del siglo XIX, el territorio al sur del río Biobío estaba habitado y gobernado por comunidades mapuche, que mantenían relaciones con el Estado chileno a través de acuerdos y comercio. Mapuche significa «gente de la tierra» en mapuzugun, la lengua mapuche. Las formas tradicionales de nombrar y de vivir ese territorio las enseñan las comunidades y los educadores tradicionales.",
        "Entre 1861 y 1883 el Estado chileno impulsó la ocupación de la Araucanía. No fue un hecho aislado ni una decisión de unos pocos: fue una política de Estado, planificada y financiada. Incluyó la acción militar (avance de fuertes y tropas), la fundación de ciudades como Angol, Mulchén, Temuco y Villarrica, y la extensión del ferrocarril hacia el sur.",
        "Después se repartieron tierras: parte se vendió o entregó a colonos chilenos y extranjeros, y a las familias mapuche se les entregaron títulos de merced sobre extensiones mucho menores que su territorio anterior. Allí quedaron radicadas en reducciones, es decir, terrenos limitados donde la población fue reubicada. Esto afectó su economía, su organización y su relación con la tierra.",
    ],
    vocab=[("Araucanía", "región del centro-sur de Chile donde se extiende el territorio mapuche"), ("política de Estado", "decisión planificada y sostenida por el Estado a lo largo del tiempo"), ("título de merced", "documento que reconocía a una comunidad mapuche una porción limitada de tierra"), ("reducción", "terreno limitado en que se radicó a población mapuche"), ("mapuzugun", "lengua del pueblo mapuche")],
    worked=[
        ("Ubicar en el tiempo", "Con la línea de tiempo, ¿cuántos años pasaron entre el plan de Saavedra y la fundación de Temuco?",
         ["Busco las fechas: 1861 y 1881.", "Resto: 1881 - 1861."], "20 años"),
        ("Reconocer una política de Estado", "¿Qué tres tipos de acciones muestran que la ocupación fue una política de Estado y no un hecho aislado?",
         ["Hay acción militar, fundación de ciudades y extensión del ferrocarril.", "Además, la repartición de tierras y la creación de una comisión para los títulos."], "Acción militar, fundación de ciudades, ferrocarril y repartición de tierras"),
    ],
    mistakes=[
        ("Describir la ocupación como un hecho aislado.", "Fue una política planificada durante décadas.", "Ordena las acciones del Estado en una secuencia."),
        ("Hablar de «el pueblo mapuche» como si todos vivieran igual.", "Había comunidades y territorios distintos.", "Usa el nombre de la comunidad o zona cuando se pueda."),
    ],
    T=[
        ("En Historia: ¿qué es una política de Estado?", "Una decisión planificada y sostenida por el Estado a lo largo del tiempo", "La ocupación de la Araucanía lo fue."),
        ("{F} ¿En qué año se funda Temuco?", "1881", "La línea de tiempo lo indica."),
        ("{F} ¿Qué entregaba la Comisión Radicadora de Indígenas?", "Títulos de merced", "La línea lo señala."),
        ("En Historia: ¿qué es una reducción?", "Un terreno limitado en que se radicó a población mapuche", "Es la forma en que quedó la tierra mapuche."),
        ("{F} ¿Qué medio de transporte llegó a Temuco durante la década de 1890? A) el ferrocarril, B) los barcos de vapor, C) las carretas.", "A", "La línea lo menciona."),
        ("Une cada acción con su tipo: 1) avance de fuertes, 2) fundación de Angol y Temuco, 3) entrega de títulos de merced. a) reparto de tierras, b) acción militar, c) fundación de ciudades. Escribe las parejas.", "1-b, 2-c, 3-a", "Cada acción corresponde a un tipo distinto."),
        ("{F} Ordena de más antiguo a más reciente: fundación de Temuco, plan de Saavedra hasta el Malleco, llegada del ferrocarril a Temuco y término de la ocupación militar.", "Plan de Saavedra, fundación de Temuco, término de la ocupación militar, llegada del ferrocarril a Temuco", "Se ordenan por sus años: 1861, 1881, 1883 y década de 1890."),
        ("{F} ¿Qué hecho de 1866 facilitó que colonos recibieran tierras?", "La ley sobre fundación de pueblos y entrega de tierras a colonos", "La línea de tiempo la señala como base legal del reparto."),
        ("{F} Una compañera dice: «La ocupación fue un acuerdo amistoso entre iguales». ¿Qué hecho de la línea muestra que no fue solo eso?", "El avance de fuertes y tropas y el levantamiento mapuche de 1881", "Hubo acción militar y resistencia."),
        ("{F} ¿Por qué la entrega de títulos de merced no devolvió el territorio anterior?", "Porque los títulos reconocían extensiones limitadas, mucho menores que el territorio que las comunidades usaban", "Los títulos fijaban reducciones."),
        ("Explica por qué la ocupación puede llamarse una política de Estado.", "Porque combinó acción militar, fundación de ciudades, ferrocarril y reparto de tierras planificados por el Estado durante años", "Fue organizada y sostenida."),
        ("Evalúa la frase «la ocupación de la Araucanía no afectó la vida de las comunidades mapuche». A) es falsa porque redujo su tierra y cambió su organización, B) es verdadera porque las comunidades siguieron con todo su territorio, C) es verdadera porque el Estado solo fundó ciudades.", "A", "Las reducciones transformaron su vida."),
        ("{F} Una persona dice: «Todas las comunidades mapuche reaccionaron de la misma manera». Da una razón para dudar.", "Porque eran comunidades distintas, con territorios e intereses propios, y la línea muestra un levantamiento pero no una reacción uniforme", "No se debe homogeneizar."),
    ],
    ctx=("Un compañero escribe en una presentación «La Araucanía se pobló en 1881 con la fundación de Temuco». Escribe una frase que corrija el título con lo aprendido.", "La Araucanía ya estaba habitada por comunidades mapuche; en 1881 se fundó Temuco dentro de una ocupación estatal que duró décadas", "La frase debe mencionar a la población previa y el proceso largo."),
    sc=[("En Historia: ¿qué es un título de merced?", "Un documento que reconocía a una comunidad mapuche una porción limitada de tierra", "Fue el instrumento de la radicación."),
        ("¿Qué significa «mapuche» en mapuzugun?", "Gente de la tierra", "Es el significado conocido de la palabra."),
        ("Nombra dos acciones de la ocupación de la Araucanía.", "Por ejemplo: el avance militar y la fundación de ciudades", "Son acciones de la línea de tiempo.")],
    op=("{F} Con la línea de tiempo de arriba, escribe cinco líneas que expliquen por qué la ocupación fue una política de Estado y cómo afectó a las comunidades mapuche. Nombra tres acciones, dos fechas y un efecto sobre las comunidades. Para las palabras en mapuzugun, consulta siempre al educador o educadora tradicional o a la comunidad.",
        "La ocupación fue una política de Estado porque combinó fuertes, fundación de ciudades como Temuco (1881) y reparto de tierras con títulos de merced (desde 1884). Esto redujo las tierras de las comunidades mapuche a reducciones y cambió su forma de vida.",
        ["nombra tres acciones", "usa dos fechas", "señala un efecto en las comunidades"], ["texto de cinco líneas"], ["decir que fue un acuerdo entre iguales", "omitir el efecto"], "Léele tu texto a alguien de tu casa y pídele que diga cuáles fueron las tres acciones."),
    reinforce="Escribe las siete fechas de la línea de tiempo y, junto a cada una, una palabra que la resuma.",
    extend="Escribe una frase que explique por qué el ferrocarril ayudó a conectar y a controlar el territorio.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = "Fuente A (informe oficial, texto de ejemplo): «El ejército ha avanzado y ha pacificado la frontera; se fundarán pueblos y se repartirán terrenos a los colonos.» Fuente B (ley, texto de ejemplo): «Los terrenos que no tengan títulos serán considerados fiscales y se rematarán en subasta.» Fuente C (relato de una comunidad mapuche, de ejemplo): «Nuestras familias cuidaban estas tierras; después nos dieron un pedazo pequeño y el resto fue vendido.» Fuente D (tabla de ejemplo): una comunidad de ejemplo ocupaba 4.000 hectáreas y recibió título de merced por 400 hectáreas. Fuente E (historiador actual, texto de ejemplo): «La palabra pacificación suaviza una realidad de violencia y pérdida de tierras.»"
build(
    OA, 2, F2,
    use="Aprenderé a leer críticamente informes oficiales, leyes, relatos de comunidades y tablas sobre la Araucanía, y a detectar eufemismos. Sirve para hablar con precisión de coerción y despojo sin presentar a un pueblo como homogéneo.",
    prior=["Conozco la ocupación de la Araucanía.", "Distingo fuentes primarias y secundarias.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Las fuentes sobre la Araucanía muestran distintas voces. Un informe oficial refleja la mirada del Estado y usa palabras como «pacificación», un eufemismo, es decir, una palabra suave que oculta una realidad dura. En este caso oculta que hubo acción militar, violencia y pérdida de tierras. Una ley muestra la regla jurídica: los terrenos sin títulos fueron considerados fiscales y rematados.",
        "Un relato de una comunidad mapuche aporta la experiencia de quienes perdieron tierras. Debe leerse como el testimonio de una comunidad concreta, no de todas. Una tabla permite medir: si una comunidad ocupaba 4.000 hectáreas y recibió título por 400, conservó la décima parte. Un historiador actual interpreta estas fuentes y discute las palabras que se usan.",
        "Al contrastar, se ven límites: el informe oficial no dice cómo vivieron las comunidades; el relato no entrega cifras; la tabla de ejemplo no explica las razones. Un buen análisis combina las fuentes, explica los términos con precisión y evita tanto el eufemismo como la generalización sobre «el pueblo mapuche» entero.",
    ],
    vocab=[("eufemismo", "palabra suave que oculta una realidad dura"), ("pacificación", "término usado por fuentes oficiales para la ocupación militar de la Araucanía"), ("terreno fiscal", "terreno que el Estado considera de su propiedad"), ("remate", "venta de un terreno al mejor postor en subasta"), ("hectárea", "unidad de superficie equivalente a 10.000 metros cuadrados")],
    worked=[
        ("Detectar un eufemismo", "En la Fuente A aparece «ha pacificado la frontera». ¿Qué realidad puede ocultar esa palabra?",
         ["«Pacificar» suena pacífico.", "La línea de tiempo muestra acción militar y un levantamiento en 1881.", "La palabra puede ocultar la violencia y la pérdida de tierras."], "Oculta acción militar, violencia y pérdida de tierras"),
        ("Calcular con una tabla", "En la Fuente D, ¿qué parte de sus tierras conservó la comunidad con el título de merced?",
         ["Tenía 4.000 hectáreas y recibió 400.", "400 es la décima parte de 4.000."], "La décima parte, es decir, el 10 %"),
    ],
    mistakes=[
        ("Repetir «pacificación» sin explicar qué significó.", "Es un término del Estado que suaviza la realidad.", "Úsalo entre comillas y explica qué ocultaba."),
        ("Usar el relato de una comunidad como si hablara por todo el pueblo mapuche.", "Representa una experiencia concreta.", "Indica de qué comunidad proviene y no generalices."),
    ],
    T=[
        ("En Historia: ¿qué es un eufemismo?", "Una palabra suave que oculta una realidad dura", "«Pacificación» es un ejemplo."),
        ("{F} ¿Qué dice la Fuente B que se hará con los terrenos sin títulos?", "Se considerarán fiscales y se rematarán", "La ley lo dice."),
        ("En Historia: ¿qué es un remate?", "La venta de un terreno al mejor postor en subasta", "Es el mecanismo de la Fuente B."),
        ("{F} ¿La Fuente E es primaria o secundaria?", "Secundaria", "La escribe un historiador actual."),
        ("{F} ¿Qué recibió la comunidad de la Fuente D? A) título de merced por 400 hectáreas, B) 4.000 hectáreas, C) ninguna tierra.", "A", "La tabla lo indica."),
        ("{F} Una compañera dice que la Fuente A prueba que la ocupación fue pacífica. ¿Qué corrección haces?", "La Fuente A es un informe oficial que usa el término «pacificado» y no demuestra que no hubiera violencia", "Es la voz del Estado."),
        ("{F} Según la Fuente D, ¿la comunidad conservó la mayor parte o una pequeña parte de las tierras que ocupaba?", "Una pequeña parte: 400 de 4.000 hectáreas", "400 es muy poco frente a 4.000."),
        ("=", "Otra comunidad de ejemplo ocupaba 2.000 hectáreas y recibió un título de merced por 500. ¿Qué porcentaje de sus tierras conservó?", "500*100//2000", "Se calcula la proporción respecto del total."),
        ("{F} ¿Qué fuente aporta la experiencia de quienes perdieron la tierra? A) la A, B) la C, C) la B.", "B", "La Fuente C es el relato de una comunidad."),
        ("{F} Explica por qué conviene contrastar las Fuentes A y C.", "Porque el informe muestra la mirada del Estado y el relato muestra la experiencia de una comunidad", "Se complementan y se corrigen."),
        ("{F} Redacta una conclusión de una frase que use las Fuentes B y D sin exagerar.", "La ley permitió rematar terrenos sin títulos y una comunidad de ejemplo quedó con 400 de 4.000 hectáreas", "Une la regla jurídica y el dato."),
        ("{F} Evalúa la frase «el relato de la Fuente C demuestra lo que vivieron todas las comunidades». A) es excesiva porque es una comunidad, B) es correcta, C) es correcta porque es un relato.", "A", "No se debe generalizar."),
        ("Propón una fuente más para entender mejor cómo respondieron las comunidades.", "Por ejemplo: una carta de un lonko pidiendo al gobierno reconocer su tierra", "Una voz mapuche completaría el análisis."),
    ],
    ctx=("{F} Un compañero escribe en un afiche «La pacificación de la Araucanía fue un proceso tranquilo». ¿Qué cambiarías y qué fuente usarías?", "Explicaría que «pacificación» es un eufemismo y usaría el relato de la comunidad y la tabla para mostrar la pérdida de tierras", "La corrección debe incluir las voces afectadas."),
    sc=[("En Historia: ¿qué es un terreno fiscal?", "Un terreno que el Estado considera de su propiedad", "Es el término de la Fuente B."),
        ("¿Qué mide una hectárea?", "Una superficie equivalente a 10.000 metros cuadrados", "Es la unidad usada en la tabla."),
        ("¿Por qué la palabra «pacificación» es un eufemismo?", "Porque suaviza una realidad de acción militar y pérdida de tierras", "Oculta la violencia ejercida.")],
    op=("{F} Con las Fuentes A a E de arriba, escribe un párrafo de siete líneas que responda: «¿Qué muestra y qué oculta el informe oficial sobre la ocupación?». Incluye el eufemismo, un dato numérico de la tabla, una voz de la comunidad y un límite.",
        "El informe oficial dice que se «pacificó» la frontera, un eufemismo que oculta la acción militar y la pérdida de tierras. La tabla muestra que una comunidad pasó de 4.000 a 400 hectáreas. El relato de la comunidad cuenta que le dieron un pedazo pequeño. Límite: son casos de ejemplo y no se puede generalizar a todas las comunidades.",
        ["identifica el eufemismo", "usa el dato numérico", "incluye la voz de la comunidad", "anota un límite"], ["párrafo de siete líneas"], ["repetir «pacificación» sin explicar", "generalizar"], "Pide a alguien de tu casa que revise que usaste el dato de 4.000 a 400."),
    reinforce="Haz una tabla de cinco filas con las Fuentes A a E: quién habla, qué dice y un límite.",
    extend="Escribe una palabra más precisa que «pacificación» para describir el hecho y explica por qué.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = "Cuadro de ejemplo. Cambio: pasaron al control del Estado las tierras al sur del Biobío; se fundaron ciudades (Angol, Temuco, Villarrica); llegó el ferrocarril; colonos chilenos y extranjeros recibieron o compraron terrenos; las comunidades mapuche fueron radicadas en reducciones con una fracción de su territorio. Continuidad: las comunidades mapuche mantuvieron su lengua, sus vínculos familiares y sus formas de organización; siguió habiendo demandas por tierras; la agricultura y la ganadería continuaron como actividades en el campo."
build(
    OA, 3, F3,
    use="Aprenderé a distinguir qué cambió y qué continuó en la Araucanía tras la ocupación y a relacionarlo con el territorio. Sirve para comprender la pérdida de tierras sin suponer que el pueblo mapuche desapareció.",
    prior=["Conozco la ocupación y las reducciones.", "Sé leer una tabla de ejemplo.", "Distingo cambio y continuidad."],
    explain=[
        "Tras la ocupación, el mapa de la Araucanía cambió. El Estado pasó a controlar tierras que antes eran territorio mapuche, se fundaron ciudades, llegó el ferrocarril y se repartieron terrenos a colonos. Las comunidades mapuche fueron radicadas en reducciones, con una fracción de su territorio anterior. Esto cambió la propiedad de la tierra, la economía y la vida de las comunidades.",
        "Pero no todo cambió. Las comunidades mantuvieron su lengua, el mapuzugun, sus vínculos familiares y sus formas propias de organización, como el lof, que es una comunidad familiar y territorial. Siguieron las demandas por tierras. Y la agricultura y la ganadería continuaron como actividades del campo, aunque ahora con otros dueños y otras reglas.",
        "El territorio es clave para analizar este proceso. La escala local muestra cada reducción y cada comunidad; la regional muestra el cambio de la Araucanía; la nacional muestra cómo el Estado integró el territorio. Si miramos solo la escala nacional vemos una expansión del Estado; si miramos la local vemos pérdida de tierras. Por eso conviene usar varias escalas.",
    ],
    vocab=[("lof", "comunidad familiar y territorial mapuche"), ("radicación", "asignación de un lugar fijo de residencia a una comunidad"), ("colono", "persona que recibe o compra tierras para poblarlas y trabajarlas"), ("propiedad de la tierra", "derecho de una persona o grupo sobre un terreno"), ("integración territorial", "incorporación de un territorio al control y organización del Estado")],
    worked=[
        ("Clasificar", "Del cuadro de ejemplo: «se fundan ciudades como Temuco» y «las comunidades mantienen su lengua». ¿Cuál es cambio y cuál continuidad?",
         ["La fundación de ciudades es algo nuevo: cambio.", "El mapuzugun se mantiene: continuidad."], "Fundación de ciudades: cambio; mantención de la lengua: continuidad"),
        ("Cambiar de escala", "A escala nacional, ¿qué se ve en la Araucanía? ¿Y a escala local?",
         ["A escala nacional se ve la expansión y la integración del territorio.", "A escala local se ve la pérdida de tierras de cada comunidad."], "Nacional: integración del Estado; local: pérdida de tierras"),
    ],
    mistakes=[
        ("Decir que el pueblo mapuche dejó de existir con las reducciones.", "Las comunidades mantuvieron su cultura y su organización.", "Distingue la pérdida de tierras de la desaparición de un pueblo."),
        ("Mirar solo la escala nacional.", "Oculta la pérdida local de tierras.", "Compara varias escalas."),
    ],
    T=[
        ("En Historia: ¿qué es un lof?", "Una comunidad familiar y territorial mapuche", "Es una forma de organización que continuó."),
        ("{F} ¿Qué medio de transporte llegó a la región según el cuadro?", "El ferrocarril", "El cuadro lo lista como cambio."),
        ("En Historia: ¿qué es la radicación?", "La asignación de un lugar fijo de residencia a una comunidad", "Fue el mecanismo de las reducciones."),
        ("{F} Clasifica como cambio o continuidad: «colonos reciben o compran terrenos».", "Cambio", "Es una novedad en la propiedad."),
        ("{F} Clasifica como cambio o continuidad: «las comunidades mantienen sus vínculos familiares».", "Continuidad", "El cuadro lo lista como continuidad."),
        ("{F} Elige la continuidad. A) el ferrocarril llega a Temuco, B) se mantienen la lengua y las formas de organización mapuche, C) se funda Villarrica.", "B", "Las otras son cambios."),
        ("{F} ¿Qué cambio en la propiedad de la tierra muestra el cuadro?", "Las tierras pasaron al control del Estado y colonos las recibieron o compraron", "El cuadro lo presenta como cambio."),
        ("{F} ¿Qué actividad del campo continuó, aunque con otros dueños y otras reglas?", "La agricultura y la ganadería", "El cuadro la lista entre las continuidades."),
        ("Explica por qué decir que «los mapuche desaparecieron» tras la ocupación es inexacto.", "Porque las comunidades mantuvieron su lengua, sus familias y sus formas de organización, y siguieron demandando tierras", "Perdieron tierras, no dejaron de existir."),
        ("{F} Una compañera dice: «Con el ferrocarril todos los habitantes de la Araucanía ganaron igual». Corrige con un dato del cuadro.", "Las comunidades mapuche fueron radicadas con una fracción de su territorio", "Los efectos fueron desiguales."),
        ("{F} ¿Qué se aprecia a escala local que no se ve a escala nacional?", "La pérdida de tierras de cada comunidad", "La escala local muestra los efectos concretos."),
        ("Evalúa la frase «la ocupación cambió la propiedad de la tierra pero no eliminó la cultura mapuche». A) es razonable, B) es falsa porque la cultura desapareció, C) es falsa porque la propiedad no cambió.", "A", "Combina cambio y continuidad."),
        ("Propón una pregunta de escala local sobre una reducción.", "Por ejemplo: ¿cuántas hectáreas tenía antes y después una comunidad concreta?", "La pregunta se ubica en un caso."),
    ],
    ctx=("{F} Un video escolar afirma: «Con la ocupación, la Araucanía quedó vacía de mapuche». Con el cuadro, escribe una frase que lo corrija.", "Las comunidades mapuche siguieron viviendo en reducciones y mantuvieron su lengua y su organización", "La frase debe incluir continuidades."),
    sc=[("En Historia: ¿qué es una integración territorial?", "La incorporación de un territorio al control y organización del Estado", "Es el efecto a escala nacional."),
        ("Nombra un cambio en la Araucanía tras la ocupación.", "Por ejemplo: se fundaron ciudades", "Está en el cuadro."),
        ("Nombra una continuidad de las comunidades mapuche.", "Por ejemplo: la lengua o la organización en lof", "Está en el cuadro.")],
    op=("{F} Con el cuadro de ejemplo de arriba, construye una tabla de dos columnas (cambio y continuidad) con al menos tres filas, y escribe una frase final que diga qué se ve a escala local que no se ve a escala nacional.",
        "Cambio: fundación de ciudades; cambio: llegada del ferrocarril; cambio: reducciones con menos tierra. Continuidad: lengua mapuche; continuidad: organización en lof; continuidad: demandas por tierras. A escala local se ve la pérdida de tierras de cada comunidad.",
        ["dos columnas", "tres filas", "frase sobre escala local"], ["tabla y frase"], ["poner solo cambios", "no distinguir escalas"], "Revisa con alguien de tu casa que cada dato esté en su columna."),
    reinforce="Escribe tres datos del cuadro y clasifícalos como cambio o continuidad.",
    extend="Escribe una pregunta sobre cómo se transmitió la lengua mapuche a las nuevas generaciones.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = "Voces de ejemplo, redactadas para este cuaderno. Oficial del ejército: «Mi tarea es avanzar la línea de fuertes y proteger a los pobladores que lleguen.» Colono chileno pobre: «Llegué para obtener un terreno propio y trabajarlo.» Colono extranjero: «Compré tierras en un remate y busco cultivarlas.» Lonko de una comunidad: «Defendimos nuestras tierras, y después pedimos que se reconocieran nuestros límites.» Mujer de una comunidad: «Seguimos tejiendo, sembrando y transmitiendo nuestra lengua en la reducción.»"
build(
    OA, 4, F4,
    use="Aprenderé a reconocer actores, causas y perspectivas en la ocupación de la Araucanía, incluida la agencia histórica mapuche. Sirve para explicar el proceso sin presentar a las comunidades como pasivas ni como un grupo uniforme.",
    prior=["Conozco la ocupación y sus fuentes.", "Sé qué es la multicausalidad.", "Sé que un pueblo tiene comunidades distintas."],
    explain=[
        "En la ocupación actuaron muchos grupos. El Estado decidió la política y envió al ejército. Colonos chilenos pobres buscaban tierra; colonos extranjeros y empresarios compraban terrenos en remates; comerciantes aprovechaban las nuevas ciudades y el ferrocarril. Y las comunidades mapuche actuaron: resistieron, negociaron, pidieron que se reconocieran sus límites y adaptaron su vida a las nuevas condiciones. A esa capacidad de actuar se le llama agencia histórica.",
        "Las causas fueron varias: el interés del Estado por integrar el territorio y extender su soberanía, la búsqueda de tierras agrícolas, el deseo de abrir rutas y conectar con el ferrocarril, y la expansión de la economía agraria. Hablamos de multicausalidad porque ninguna razón sola explica la ocupación. Y los grupos tuvieron perspectivas distintas: para el Estado era integración, para el colono una oportunidad, para las comunidades una pérdida de territorio.",
        "Tampoco hubo una sola perspectiva mapuche. Había comunidades con territorios, lonkos y relaciones distintas con el Estado, y no todas reaccionaron igual. Por eso hay que evitar frases como «los mapuche pensaban todos lo mismo» y escuchar a cada comunidad. Para conocer nombres y formas tradicionales, es necesario consultar a las propias comunidades.",
    ],
    vocab=[("agencia histórica", "capacidad de un grupo de actuar y tomar decisiones en un proceso"), ("resistencia", "oposición a una imposición mediante acciones de defensa"), ("lonko", "autoridad de una comunidad mapuche"), ("negociar", "buscar acuerdos mediante conversaciones o peticiones"), ("perspectiva", "punto de vista desde el que se mira un hecho")],
    worked=[
        ("Reconocer la agencia", "En las voces de ejemplo, ¿qué acciones muestran la agencia de las comunidades mapuche?",
         ["El lonko habla de defender tierras y de pedir reconocimiento de límites.", "La mujer habla de seguir tejiendo, sembrando y transmitiendo la lengua."], "Defender, pedir reconocimiento de límites y mantener cultura y lengua"),
        ("Diferenciar a los colonos", "¿En qué se diferencian el colono chileno pobre y el colono extranjero en las voces de ejemplo?",
         ["El primero llegó buscando un terreno propio.", "El segundo compró tierras en un remate."], "Uno busca un terreno propio; el otro compró en un remate"),
    ],
    mistakes=[
        ("Presentar a las comunidades mapuche solo como víctimas pasivas.", "Actuaron: resistieron, negociaron y adaptaron su vida.", "Incluye sus acciones en el relato."),
        ("Hablar de todos los colonos como si fueran iguales.", "Había colonos pobres, empresarios y extranjeros con intereses distintos.", "Distingue grupos y motivos."),
    ],
    T=[
        ("En Historia: ¿qué es la agencia histórica?", "La capacidad de un grupo de actuar y tomar decisiones en un proceso", "Las comunidades la ejercieron."),
        ("{F} ¿Qué busca el colono chileno pobre?", "Un terreno propio para trabajarlo", "Su voz lo dice."),
        ("En Historia: ¿qué es un lonko?", "Una autoridad de una comunidad mapuche", "Es una de las autoridades tradicionales."),
        ("{F} ¿Cómo obtuvo tierras el colono extranjero?", "Las compró en un remate", "Su voz lo dice."),
        ("Une cada actor con su acción: 1) oficial, 2) lonko, 3) mujer de la comunidad. a) transmitir la lengua en la reducción, b) avanzar la línea de fuertes, c) defender tierras y pedir reconocimiento de límites. Escribe las parejas.", "1-b, 2-c, 3-a", "Cada voz expresa una acción distinta."),
        ("{F} Elige el actor que mejor muestra la resistencia. A) el lonko que defendió tierras, B) el colono extranjero, C) el oficial.", "A", "Resistir es defenderse de la imposición."),
        ("{F} ¿Qué acción de la mujer de la comunidad muestra que la cultura mapuche continuaba en la reducción?", "Seguir tejiendo, sembrando y transmitiendo la lengua", "Son prácticas culturales que se mantuvieron."),
        ("{F} Explica qué muestra el lonko al decir que pidieron que se reconocieran sus límites.", "Que las comunidades también negociaron y pidieron al Estado reconocimiento, además de defenderse", "La agencia incluye petición y negociación."),
        ("{F} Una compañera dice que las comunidades mapuche no hicieron nada frente a la ocupación. Responde con un dato de las voces de ejemplo.", "El lonko dice que defendieron sus tierras y pidieron el reconocimiento de sus límites", "Hay agencia en su acción."),
        ("Explica por qué la ocupación tuvo varias causas.", "Porque influyeron la integración del territorio, la búsqueda de tierras agrícolas, el ferrocarril y la expansión de la economía", "Se combinaron razones políticas y económicas."),
        ("{F} ¿En qué se diferencia la perspectiva del oficial de la del lonko?", "El oficial ve proteger y avanzar; el lonko ve defender las tierras de su comunidad", "Miran el mismo hecho desde posiciones opuestas."),
        ("Evalúa la frase «todas las comunidades mapuche pensaban y actuaban igual». A) es inexacta porque había comunidades y territorios distintos, B) es correcta, C) es correcta porque eran un pueblo.", "A", "No se debe homogeneizar."),
        ("Redacta una pregunta para contrastar el interés del colono extranjero con el de la comunidad.", "Por ejemplo: ¿qué entendía cada uno por «dueño de la tierra»?", "La pregunta compara dos ideas de propiedad."),
    ],
    ctx=("{F} En una dramatización escolar, un compañero hace que el lonko solo diga «nos rendimos». Con las voces de ejemplo, ¿qué cambiarías para mostrar su agencia?", "Haría que dijera que defendieron la tierra y después pidieron que se reconocieran sus límites", "La agencia incluye resistencia y petición."),
    sc=[("En Historia: ¿qué es una resistencia?", "Una oposición a una imposición mediante acciones de defensa", "Las comunidades la ejercieron."),
        ("Nombra dos actores de la ocupación de la Araucanía.", "Por ejemplo: el ejército y los colonos", "Ambos actuaron en el proceso."),
        ("¿Por qué no se debe hablar de «la perspectiva mapuche» como una sola?", "Porque había comunidades y territorios distintos", "Cada comunidad tuvo experiencias propias.")],
    op=("{F} Elige dos voces de ejemplo de arriba y escribe cinco líneas: qué busca cada una, una causa de la ocupación y una diferencia de perspectiva. Incluye al menos una acción de agencia mapuche.",
        "El oficial busca avanzar la línea de fuertes. El lonko defendió las tierras y pidió el reconocimiento de límites. Una causa fue la búsqueda de tierras agrícolas. El oficial ve proteger a los pobladores; el lonko ve la pérdida del territorio de su comunidad.",
        ["dos voces", "una causa", "diferencia de perspectiva", "agencia mapuche"], ["texto de cinco líneas"], ["presentar a los mapuche como pasivos", "no marcar diferencia"], "Cuenta tu texto a alguien de tu casa y pídele que diga cuál es la agencia mapuche."),
    reinforce="Haz una tabla con cinco actores y un interés o una acción para cada uno.",
    extend="Explica por qué la palabra «agencia» ayuda a contar la historia mapuche con más precisión.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = "Dossier de ejemplo. Dato 1: entre 1861 y 1883 el Estado avanzó con fuertes y tropas, y fundó ciudades como Angol y Temuco. Dato 2: el ferrocarril llegó a Temuco durante la década de 1890. Dato 3: los terrenos sin títulos se consideraron fiscales y se remataron a colonos. Dato 4: una comunidad de ejemplo pasó de ocupar 4.000 hectáreas a tener un título de merced por 400. Dato 5: las comunidades defendieron sus tierras, pidieron reconocimiento de límites y mantuvieron su lengua."
build(
    OA, 5, F5,
    use="Aprenderé a construir un argumento que explique la ocupación de la Araucanía como política de Estado y sus efectos sobre la sociedad mapuche, usando evidencia y términos precisos. Sirve para hablar de despojo y de agencia sin eufemismos ni generalizaciones.",
    prior=["Conozco la ocupación, sus fuentes y sus actores.", "Sé usar tesis, evidencia y límite.", "Sé qué es un eufemismo."],
    explain=[
        "Un argumento sobre la ocupación de la Araucanía responde a una pregunta como «¿Por qué se dice que fue una política de Estado que afectó profundamente a la sociedad mapuche?». Una tesis posible es que el Estado combinó acción militar, fundación de ciudades, ferrocarril y reparto de tierras, y que esto produjo una gran pérdida de tierras mapuche, aunque las comunidades resistieron y mantuvieron su cultura.",
        "Las evidencias deben explicarse. Los datos 1 y 2 muestran la coordinación de acciones del Estado. El dato 3 muestra el mecanismo del reparto de tierras. El dato 4 permite medir la pérdida: de 4.000 a 400 hectáreas es una reducción del 90 %. El dato 5 muestra la agencia mapuche. Cada dato se explica con la fórmula «esto muestra que…».",
        "El límite es relevante. Con el dossier no sabemos qué ocurrió en todas las comunidades ni cuántas hectáreas se repartieron en total; el caso de la tabla es de ejemplo. Tampoco hay que usar eufemismos como «pacificación» sin explicarlos ni hablar del pueblo mapuche como un bloque homogéneo.",
    ],
    vocab=[("tesis", "afirmación principal que se defiende"), ("evidencia", "dato que apoya la tesis"), ("despojo", "pérdida forzada o injusta de bienes, como tierras"), ("homogéneo", "que es igual en todas sus partes"), ("límite", "aquello que la evidencia no permite afirmar")],
    worked=[
        ("Armar tesis y evidencias", "Para sostener que «fue una política de Estado», ¿qué datos del dossier sirven?",
         ["El dato 1 muestra avance militar y fundación de ciudades.", "El dato 2 muestra el ferrocarril.", "El dato 3 muestra el reparto de tierras por remate."], "Los datos 1, 2 y 3"),
        ("Medir la pérdida", "Con el dato 4, ¿qué porcentaje de sus tierras perdió la comunidad de ejemplo?",
         ["Pasó de 4.000 a 400 hectáreas, es decir, perdió 3.600.", "3.600 de 4.000 es el 90 %."], "El 90 %"),
    ],
    mistakes=[
        ("Escribir una tesis que no menciona la agencia mapuche.", "Presenta a las comunidades solo como víctimas.", "Incluye el dato 5."),
        ("Generalizar el caso de la tabla a todas las comunidades.", "Es un caso de ejemplo.", "Escribe «en el caso de ejemplo» y no «en todos los casos»."),
    ],
    T=[
        ("En Historia: ¿qué es el despojo?", "La pérdida forzada o injusta de bienes, como tierras", "Se aplica a la pérdida de tierras mapuche."),
        ("{F} ¿Qué dato muestra el mecanismo de reparto de tierras? A) dato 2, B) dato 3, C) dato 5.", "B", "El dato 3 habla de remate de terrenos fiscales."),
        ("{F} ¿Qué dato permite medir la pérdida de tierras?", "El dato 4", "Da cifras en hectáreas."),
        ("{F} ¿Qué dato muestra la agencia mapuche?", "El dato 5", "Habla de defensa, reconocimiento de límites y lengua."),
        ("Elige la tesis mejor formulada. A) La ocupación fue un hecho aislado sin consecuencias, B) La ocupación fue una política de Estado que redujo fuertemente las tierras mapuche, aunque las comunidades resistieron y mantuvieron su cultura, C) Las tierras de la Araucanía no tenían uso antes de la ocupación y por eso nadie las perdió.", "B", "Es defendible con el dossier."),
        ("Una compañera usa el dato 4 para afirmar que «todas las comunidades perdieron el 90 %». ¿Qué corrección haces?", "El dato 4 es un caso de ejemplo y no prueba lo que pasó en todas las comunidades", "No se puede generalizar."),
        ("{F} Además del dato 3, ¿qué datos sirven para sostener que la ocupación fue una política de Estado planificada?", "Los datos 1 y 2", "Muestran avance militar, ciudades y ferrocarril."),
        ("=", "Esa otra comunidad de 3.000 hectáreas, que recibió título por 600, ¿qué porcentaje de sus tierras perdió?", "(3000-600)*100//3000", "Se divide la pérdida entre el total y se pasa a porcentaje."),
        ("{F} Con los datos 3 y 5, redacta una conclusión proporcional.", "Los terrenos sin títulos se remataron, y las comunidades defendieron sus tierras y mantuvieron su lengua", "Une despojo y agencia."),
        ("Explica por qué una tesis sobre la Araucanía debe nombrar el despojo sin eufemismos.", "Porque nombrar el despojo describe con precisión la pérdida de tierras y evita suavizar los hechos", "La precisión evita ocultar la violencia."),
        ("Un compañero escribe: «La pacificación fue un proceso tranquilo». Señala el problema.", "«Pacificación» es un eufemismo que oculta la acción militar y la pérdida de tierras", "Hay evidencia contraria en el dossier."),
        ("Evalúa este argumento: «El Estado planificó la ocupación (datos 1 a 3), y las comunidades perdieron tierras (dato 4) pero resistieron (dato 5)». A) es sólido porque usa evidencia de varios tipos, B) es débil porque solo muestra acciones del Estado y ningún efecto sobre las comunidades, C) es falso porque la ocupación no tuvo efectos sobre la tierra mapuche.", "A", "Usa datos de política, pérdida y agencia."),
        ("Escribe una pregunta que exigiría otra fuente para completar el argumento.", "Por ejemplo: ¿cómo recuerdan hoy las comunidades este periodo y qué reclaman?", "La pregunta señala una voz ausente."),
    ],
    ctx=("{F} En un foro estudiantil alguien dice que «las comunidades mapuche fueron solo víctimas pasivas». Con el dossier, escribe tu respuesta en dos frases con una evidencia.", "No solo fueron víctimas: el dato 5 muestra que defendieron sus tierras, pidieron reconocimiento de límites y mantuvieron su lengua", "La respuesta debe usar el dato 5."),
    sc=[("En Historia: ¿qué significa homogéneo?", "Que es igual en todas sus partes", "No describe bien al pueblo mapuche."),
        ("Nombra un dato del dossier sobre acciones del Estado.", "Por ejemplo: la fundación de Angol y Temuco", "Es el dato 1."),
        ("{F} ¿Qué porcentaje perdió la comunidad de ejemplo?", "El 90 %", "De 4.000 a 400 hectáreas.")],
    op=("{F} Con el dossier de ejemplo de arriba, escribe un párrafo de ocho líneas que responda: «¿Por qué la ocupación de la Araucanía fue una política de Estado que afectó profundamente a la sociedad mapuche?». Incluye una tesis, tres evidencias explicadas y un límite.",
        "La ocupación fue una política de Estado porque combinó fuertes, ciudades, ferrocarril y remate de terrenos. Una comunidad de ejemplo pasó de 4.000 a 400 hectáreas, lo que muestra un despojo del 90 %. Sin embargo, las comunidades defendieron sus tierras y mantuvieron su lengua. Límite: el caso es de ejemplo y no se puede generalizar.",
        ["tesis", "tres evidencias explicadas", "límite"], ["párrafo de ocho líneas"], ["usar eufemismos", "generalizar el caso"], "Pide a alguien de tu casa que marque tu tesis y tus tres evidencias."),
    reinforce="Escribe tu tesis en una frase y anota debajo las tres evidencias que usaste.",
    extend="Escribe una segunda tesis centrada en la agencia mapuche y un dato nuevo que necesitarías.",
    materials=MAT,
)
