"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 12 (exploración estatal, ciencias y delimitación territorial)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 12"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = "Línea de tiempo: 1830, el Estado contrata al naturalista francés Claudio Gay para estudiar el territorio; 1842, se funda la Universidad de Chile; 1853-1854, el alemán Rodulfo Amando Philippi explora el desierto de Atacama; 1854, primer censo general moderno de población; 1874, se crea la Oficina Hidrográfica; 1881, tratado de límites con Argentina."
build(
    OA, 1, F1,
    use="Aprenderé a ubicar en el tiempo los viajes de exploración, los censos y las instituciones científicas del siglo XIX y a explicar para qué los impulsó el Estado. Sirve para entender cómo se conoció, administró y delimitó el territorio.",
    prior=["Sé qué es el Estado y qué fue la Independencia.", "Sé leer una línea de tiempo.", "Sé qué es un mapa y una escala."],
    explain=[
        "Después de la Independencia, el Estado chileno sabía poco de su propio territorio. Para gobernarlo necesitaba conocerlo: cuántas personas lo habitaban, qué recursos tenía, cómo eran sus costas y montañas, y hasta dónde llegaban sus fronteras. Por eso impulsó la exploración y el reconocimiento del territorio, que significa recorrerlo, describirlo y registrarlo.",
        "Para esa tarea contrató a científicos y creó instituciones. Claudio Gay recorrió el país desde 1830 y escribió una historia física y política de Chile con mapas. Rodulfo Philippi exploró el desierto de Atacama; la Universidad de Chile, fundada en 1842, formó profesionales y estudios científicos; el censo de 1854 contó a la población; y la Oficina Hidrográfica, creada en 1874, estudió costas y canales.",
        "Estas acciones tenían cuatro propósitos: caracterizar la población (quiénes y cuántos), desarrollar los recursos (minas, tierras, puertos), organizar la administración (dónde instalar autoridades) y delimitar las fronteras (hasta dónde llega Chile). Pero conocer el territorio no era lo mismo que ocuparlo, y reconocer no significa que estuviera vacío: en él vivían pueblos con sus propias formas de conocerlo.",
    ],
    vocab=[("exploración", "recorrido de un territorio para conocerlo y describirlo"), ("censo", "recuento oficial de la población y de sus características"), ("misión científica", "viaje o encargo de científicos para estudiar un territorio"), ("frontera", "línea que separa el territorio de dos Estados"), ("administración", "organización de autoridades y servicios del Estado en el territorio")],
    worked=[
        ("Ubicar en el tiempo", "Con la línea de tiempo, ¿cuántos años pasaron entre la contratación de Claudio Gay y el censo de 1854?",
         ["Busco ambas fechas: 1830 y 1854.", "Resto: 1854 - 1830."], "24 años"),
        ("Relacionar institución y propósito", "¿Qué propósito del Estado se relaciona con el censo de 1854 y cuál con la Oficina Hidrográfica?",
         ["El censo cuenta personas: caracterizar la población.", "La Oficina estudia costas y canales: conocer el territorio para su uso y administración."], "Censo: caracterizar la población; Oficina Hidrográfica: conocer costas y canales"),
    ],
    mistakes=[
        ("Creer que un territorio era vacío porque el Estado no lo conocía.", "El Estado lo desconocía, pero estaba habitado por pueblos y personas.", "Pregunta quién vivía allí antes del reconocimiento estatal."),
        ("Pensar que explorar es lo mismo que ocupar o controlar.", "Explorar describe; ocupar implica presencia y autoridad.", "Distingue conocer, ocupar y administrar."),
    ],
    T=[
        ("En Historia: ¿qué es un censo?", "Un recuento oficial de la población y de sus características", "Es la herramienta para caracterizar la población."),
        ("{F} ¿En qué año se crea la Oficina Hidrográfica?", "1874", "La línea de tiempo lo señala."),
        ("{F} ¿Quién exploró el desierto de Atacama según la línea de tiempo?", "Rodulfo Amando Philippi", "La línea lo nombra."),
        ("En Historia: ¿qué es una frontera?", "La línea que separa el territorio de dos Estados", "Es un concepto de delimitación territorial."),
        ("{F} ¿Con qué país es el tratado de límites de 1881? A) Perú, B) Argentina, C) Bolivia.", "B", "La línea lo menciona."),
        ("Une cada propósito con una acción: 1) caracterizar la población, 2) delimitar fronteras, 3) conocer costas. a) tratado de límites, b) censo, c) Oficina Hidrográfica. Escribe las parejas.", "1-b, 2-a, 3-c", "Cada acción responde a un propósito."),
        ("{F} Ordena de más antiguo a más reciente: Oficina Hidrográfica, censo general de 1854, contratación de Claudio Gay y tratado de límites con Argentina.", "Contratación de Claudio Gay, censo de 1854, Oficina Hidrográfica, tratado de límites con Argentina", "Se ordenan por sus años: 1830, 1854, 1874 y 1881."),
        ("{F} ¿Qué hecho de la línea corresponde al propósito de delimitar las fronteras?", "El tratado de límites con Argentina de 1881", "Un tratado de límites fija hasta dónde llega cada Estado."),
        ("Una compañera dice: «Como Claudio Gay recorrió el país, el Estado ya controlaba todo el territorio». ¿Qué corrección haces?", "Recorrer y describir no es ocupar ni controlar; el Estado aún no administraba todos los lugares", "Explorar y controlar son cosas distintas."),
        ("{F} ¿Qué hecho de la línea muestra interés por las costas y no solo por la tierra? Justifica.", "La Oficina Hidrográfica de 1874, porque estudiaba costas y canales", "Su función era marítima."),
        ("Explica por qué decir «el Estado descubrió el territorio» es problemático.", "Porque el territorio estaba habitado por pueblos que ya lo conocían, aunque el Estado no lo hubiera registrado", "Desconocer no es lo mismo que estar vacío."),
        ("Evalúa la frase «la exploración sirvió para organizar la administración». A) es razonable, porque conocer el territorio ayudaba a instalar autoridades y servicios, B) es falsa porque la exploración solo tuvo fines científicos y no servía para administrar, C) es falsa porque el Estado ya conocía y administraba todo el territorio antes de explorarlo.", "A", "La exploración tenía fines de administración."),
        ("Una persona dice: «Todo lo que está en un mapa de 1850 era conocido y aceptado por quienes vivían ahí». Da una razón para dudar.", "Porque el mapa lo hizo el Estado o sus científicos y podía no incluir a quienes vivían allí ni su forma de nombrar el lugar", "Un mapa tiene autor y propósito."),
    ],
    ctx=("En una exposición del colegio, un grupo escribe «El Estado descubrió el norte y el sur de Chile entre 1830 y 1880». Escribe una frase que corrija el título usando lo aprendido.", "El Estado exploró y reconoció territorios que ya estaban habitados, para administrarlos y delimitarlos", "La frase debe sustituir «descubrir» por «reconocer» y reconocer la presencia de pueblos."),
    sc=[("En Historia: ¿qué es una misión científica?", "Un viaje o encargo de científicos para estudiar un territorio", "Es el tipo de trabajo de Gay y Philippi."),
        ("Nombra dos propósitos del reconocimiento del territorio.", "Por ejemplo: caracterizar la población y delimitar fronteras", "Son propósitos de la clase."),
        ("{F} ¿Qué institución, fundada en 1842, formó profesionales y estudios científicos?", "La Universidad de Chile", "Está en la línea de tiempo.")],
    op=("{F} Con la línea de tiempo de arriba, escribe cinco líneas que expliquen cómo conoció el Estado su territorio. Debes nombrar una persona, una institución, un propósito y recordar que había pueblos que ya vivían en esos lugares.",
        "El Estado contrató a Claudio Gay para estudiar el país y creó la Oficina Hidrográfica para conocer costas y canales. Su propósito fue organizar la administración y delimitar las fronteras. Sin embargo, esos territorios ya estaban habitados por pueblos que los conocían.",
        ["nombra persona e institución", "señala un propósito", "recuerda la presencia de pueblos"], ["texto de cinco líneas"], ["decir que el territorio estaba vacío", "no nombrar propósito"], "Lee tu texto a alguien de tu casa y pídele que identifique el propósito."),
    reinforce="Escribe las seis fechas de la línea de tiempo y, junto a cada una, una palabra que la resuma.",
    extend="Escribe una frase que explique por qué la Oficina Hidrográfica era útil para el comercio marítimo.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = "Fuente A (tabla de censo, de ejemplo): en una provincia de ejemplo se contaron 30.000 habitantes, clasificados por sexo, edad, oficio y si sabían leer; no hay una categoría para pertenencia a pueblos originarios. Fuente B (diario de un científico viajero, texto de ejemplo): «Recorrí el valle durante dos semanas; hallé minas abandonadas y pocas casas; mis guías conocían cada sendero.» Fuente C (mapa de ejemplo del Estado): marca como «desconocido» una zona del sur donde viven familias que no figuran. Fuente D (historiadora actual, texto de ejemplo): «Los mapas del siglo XIX informan y también expresan los intereses del Estado que los encargó.»"
build(
    OA, 2, F2,
    use="Aprenderé a leer críticamente censos, diarios de viaje y mapas del siglo XIX, preguntando quién los hizo y qué dejan fuera. Sirve para no tratar mapas y censos como fotografías neutrales.",
    prior=["Conozco la exploración estatal del siglo XIX.", "Distingo fuentes primarias y secundarias.", "Sé qué es un censo."],
    explain=[
        "Los censos, los mapas y los diarios de viaje son fuentes valiosas, pero no son espejos neutrales. Un censo cuenta lo que quien lo diseña considera importante: las categorías (sexo, edad, oficio, alfabetización) las decide el Estado. Lo que no está en las categorías, como la pertenencia a un pueblo originario en el ejemplo de la Fuente A, queda sin registro y se vuelve invisible en las cifras.",
        "Un mapa selecciona y simplifica. Decide qué lugares marca, cómo los nombra y qué deja en blanco. Una zona marcada como «desconocida» por el Estado puede estar habitada, como muestra la Fuente C: lo desconocido es para quien hizo el mapa, no necesariamente para las personas que viven allí. Por eso reconocimiento estatal no equivale a territorio vacío.",
        "El diario de un científico viajero (Fuente B) es una fuente primaria que mezcla observación e interpretación. Dice que hay pocas casas y minas abandonadas, pero también que los guías conocían cada sendero: eso revela un saber local que el científico necesitó. Al contrastar el censo, el mapa y el diario, se obtiene una visión más completa y se reconocen los límites de cada una.",
    ],
    vocab=[("categoría", "grupo con que un censo clasifica a las personas"), ("fuente cartográfica", "mapa u otra representación del territorio como fuente histórica"), ("saber local", "conocimiento del territorio de quienes viven allí"), ("invisible", "que no aparece en un registro"), ("fuente institucional", "fuente producida por una institución del Estado")],
    worked=[
        ("Detectar lo que queda fuera", "Con la Fuente A, ¿qué grupo queda invisible en las cifras del censo de ejemplo y por qué?",
         ["Miro las categorías: sexo, edad, oficio y alfabetización.", "No hay una categoría de pertenencia a un pueblo originario.", "Lo que no se pregunta no se cuenta."], "Los pueblos originarios, porque no hay categoría para registrarlos"),
        ("Contrastar mapa y diario", "La Fuente C marca una zona como «desconocida» y la Fuente B dice que los guías conocían los senderos. ¿Qué se puede concluir con cuidado?",
         ["El mapa refleja lo que el Estado conocía.", "El diario muestra que había personas con conocimiento del lugar.", "La zona era desconocida para el Estado, no para sus habitantes."], "Desconocida para el Estado, no para quienes vivían allí"),
    ],
    mistakes=[
        ("Tomar una tabla de censo como un retrato completo de la sociedad.", "Solo cuenta lo que sus categorías permiten.", "Revisa qué categorías usa y cuáles faltan."),
        ("Creer que lo que un mapa llama «desconocido» estaba vacío.", "Puede ser un lugar habitado ignorado por el Estado.", "Pregunta quién vivía allí y qué sabía del lugar."),
    ],
    T=[
        ("En Historia: ¿qué es una categoría en un censo?", "Un grupo con que se clasifica a las personas", "Define lo que se cuenta."),
        ("{F} ¿Cuántos habitantes se contaron en la provincia de la Fuente A?", "30.000", "La tabla lo indica."),
        ("{F} ¿Qué categorías incluye el censo de la Fuente A? A) sexo, edad, oficio y alfabetización, B) religión y color de ojos, C) ingresos y estudios universitarios.", "A", "La fuente las lista."),
        ("{F} ¿La Fuente B es una fuente primaria o secundaria?", "Primaria", "Es un diario escrito por un viajero de la época."),
        ("{F} ¿Qué sabían los guías, según la Fuente B?", "Cada sendero del valle", "El diario lo dice."),
        ("Una compañera dice: «El censo de la Fuente A muestra a toda la población, sin dejar a nadie fuera». ¿Qué corrección haces?", "No incluye una categoría para pertenencia a pueblos originarios, así que ese grupo queda invisible", "Las categorías limitan lo que se cuenta."),
        ("{F} ¿Podría usarse el censo de la Fuente A para saber cuántas personas de esa provincia pertenecían a pueblos originarios? Justifica.", "No, porque no tiene una categoría para esa pertenencia", "Lo que no se pregunta no se cuenta."),
        ("{F} ¿Qué describe el diario de la Fuente B sobre el valle que recorrió el científico?", "Minas abandonadas y pocas casas", "Es lo que el viajero observó y anotó."),
        ("{F} ¿Qué dos fuentes se oponen en cuanto a quién conoce la zona del sur? A) la Fuente C y la Fuente B, B) la Fuente A y la Fuente D, C) ninguna.", "A", "El mapa la llama desconocida y el diario muestra a guías que la conocen."),
        ("{F} Explica por qué un mapa del Estado puede no ser neutral.", "Porque selecciona qué marca y cómo nombra según los intereses de quien lo encargó", "La Fuente D lo afirma como idea central."),
        ("{F} Redacta una conclusión de una frase que use las Fuentes B y C sin exagerar.", "El Estado consideraba desconocida una zona donde los guías conocían los senderos", "Une las dos fuentes con cuidado."),
        ("Evalúa la afirmación «los mapas del Estado muestran exactamente cómo era el territorio». A) es falsa porque seleccionan y responden a intereses, B) es verdadera porque son oficiales, C) es verdadera porque tienen escala.", "A", "Un mapa es una representación con propósito."),
        ("¿Qué fuente sumarías para saber cómo describían el lugar los habitantes del sur? Escríbela.", "Por ejemplo: un testimonio de una familia que vivía allí", "La fuente nueva cubre la voz que falta."),
    ],
    ctx=("{F} Un compañero copia la Fuente C en una presentación con el título «El sur de Chile en 1850: un territorio vacío». ¿Qué fuente agregas y qué título propones?", "Agrego la Fuente B y propongo un título como «Zona desconocida para el Estado, conocida por sus habitantes»", "El título debe incluir la perspectiva de los habitantes."),
    sc=[("En Historia: ¿qué es un saber local?", "El conocimiento del territorio de quienes viven allí", "Lo aportan guías y habitantes."),
        ("¿Quién decide las categorías de un censo?", "Quien lo diseña, en este caso el Estado", "Determinan lo que se cuenta."),
        ("¿Un mapa del siglo XIX es neutral? Responde sí o no y por qué.", "No, porque selecciona qué marca y responde a intereses", "Tiene autor y propósito.")],
    op=("{F} Con las Fuentes A, B y C de arriba, escribe un párrafo de seis líneas que responda: «¿Qué muestran y qué ocultan un censo y un mapa del Estado?». Incluye un ejemplo de lo que muestra, uno de lo que oculta y una frase sobre el saber local.",
        "El censo muestra cuántos habitantes hay y su sexo, edad, oficio y alfabetización. Oculta la pertenencia a pueblos originarios porque no hay categoría. El mapa muestra zonas conocidas por el Estado y oculta que en el sur vivían familias. Los guías del diario conocían los senderos, un saber local.",
        ["un ejemplo de lo que muestra", "un ejemplo de lo que oculta", "frase sobre saber local"], ["párrafo de seis líneas"], ["tomar el censo como completo", "no hablar de saber local"], "Pide a alguien de tu casa que te diga qué entendió de lo que oculta el mapa."),
    reinforce="Haz una tabla con las Fuentes A, B y C: qué muestra y qué oculta cada una.",
    extend="Escribe dos categorías que añadirías al censo de la Fuente A para registrar mejor a la población.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = "Cuadro de ejemplo. Cambio: hacia 1830 el Estado tenía mapas parciales; hacia 1880 contaba con cartas más completas, censos regulares (1854, 1865, 1875), una Oficina Hidrográfica (1874) y acuerdos de límites (1881). Continuidad: al sur del río Biobío había territorios mapuche que el Estado aún no controlaba; en el norte y los canales australes vivían pueblos que el Estado solo conocía en parte; muchos territorios se administraban desde lejos."
build(
    OA, 3, F3,
    use="Aprenderé a comparar qué cambió y qué continuó en el conocimiento y control del territorio entre 1830 y 1880, ubicando lugares en el espacio. Sirve para no pensar el siglo XIX como un avance uniforme del Estado sobre un mapa en blanco.",
    prior=["Conozco la exploración y los censos.", "Sé leer un mapa de Chile.", "Distingo cambio y continuidad."],
    explain=[
        "Entre 1830 y 1880 el conocimiento estatal del territorio cambió mucho. Se hicieron cartas geográficas más completas, se repitieron los censos (1854, 1865, 1875), se estudiaron las costas con la Oficina Hidrográfica y se firmaron acuerdos de límites con países vecinos. El Estado pasó de tener mapas parciales a tener herramientas para administrar.",
        "Aun así, hubo continuidades. Al sur del río Biobío se mantuvieron territorios mapuche que el Estado no controlaba, y en el extremo norte y en los canales australes vivían pueblos que el Estado conocía solo en parte. Muchos lugares se administraban desde lejos, con pocas autoridades presentes. El control no avanzó parejo ni al mismo tiempo en todo el país.",
        "Para analizarlo conviene relacionar tres escalas: la local (un valle o un puerto), la regional (una zona como el norte o el sur) y la nacional (todo el país). Un mismo proceso se ve distinto en cada escala. Por ejemplo, a escala nacional hay más mapas y censos; a escala local, hay lugares que seguían fuera del control estatal.",
    ],
    vocab=[("carta geográfica", "mapa detallado de un territorio con información de relieve y límites"), ("escala local / regional / nacional", "tamaño del espacio estudiado: un lugar, una zona o el país"), ("control territorial", "capacidad del Estado de ejercer autoridad en un lugar"), ("acuerdo de límites", "tratado que fija la frontera entre dos Estados"), ("territorio indígena", "espacio habitado y gobernado por un pueblo originario")],
    worked=[
        ("Clasificar", "Del cuadro de ejemplo: «hacia 1880 había censos regulares» y «al sur del Biobío había territorios mapuche no controlados por el Estado». ¿Cuál es cambio y cuál continuidad?",
         ["Los censos regulares son una novedad en la administración: cambio.", "El control mapuche en el sur es algo que se mantenía: continuidad."], "Censos regulares: cambio; territorios mapuche no controlados: continuidad"),
        ("Cambiar de escala", "A escala nacional se puede decir que el Estado conoció mejor su territorio en 1880. ¿Qué precisión agrega la escala regional del sur?",
         ["La escala nacional resume avances.", "En el sur había zonas que el Estado aún no controlaba."], "El conocimiento avanzó, pero el control del sur seguía incompleto"),
    ],
    mistakes=[
        ("Decir que en 1880 el Estado ya controlaba todo el territorio actual.", "Había zonas con presencia indígena y otras mal conocidas.", "Pregunta qué parte del territorio estaba controlada."),
        ("Mezclar escalas sin avisar.", "Un dato nacional puede ocultar diferencias regionales o locales.", "Escribe a qué escala se refiere cada dato."),
    ],
    T=[
        ("En Historia: ¿qué es una carta geográfica?", "Un mapa detallado de un territorio con relieve y límites", "Es el producto de los reconocimientos del territorio."),
        ("{F} ¿Qué años de censos regulares menciona el cuadro? Escríbelos.", "1854, 1865 y 1875", "El cuadro los lista."),
        ("{F} ¿Qué organismo se creó en 1874 según el cuadro?", "La Oficina Hidrográfica", "Se cita en la lista de cambios."),
        ("En Historia: ¿qué es el control territorial?", "La capacidad del Estado de ejercer autoridad en un lugar", "No es lo mismo que conocerlo."),
        ("{F} Clasifica como cambio o continuidad: «acuerdo de límites de 1881».", "Cambio", "Es una novedad del periodo."),
        ("{F} Clasifica como cambio o continuidad: «territorios mapuche al sur del Biobío».", "Continuidad", "El cuadro dice que se mantenían."),
        ("{F} ¿Qué cambio muestra el cuadro entre 1830 y 1880 en los mapas que tenía el Estado?", "Pasó de mapas parciales a cartas más completas", "El cuadro contrasta mapas parciales con cartas más completas."),
        ("Una historiadora estudia el mapa de un solo valle. ¿A qué escala trabaja: local, regional o nacional?", "A escala local", "Un valle es un espacio pequeño y puntual."),
        ("Une cada dato con su escala: 1) un censo de todo el país, 2) una carta de la costa del norte, 3) el mapa de un solo valle. a) escala local, b) escala nacional, c) escala regional. Escribe las parejas.", "1-b, 2-c, 3-a", "El tamaño del espacio define la escala."),
        ("Explica por qué que el Estado conociera mejor su territorio en 1880 no significa que lo controlara todo.", "Porque conocer es describir y controlar es ejercer autoridad, y en el sur y otros lugares había territorios que no controlaba", "Conocimiento y control son cosas distintas."),
        ("{F} Una compañera dice: «En 1880 el territorio chileno estaba completamente integrado». Corrige con un dato del cuadro.", "Al sur del Biobío había territorios mapuche que el Estado aún no controlaba", "El cuadro muestra una continuidad."),
        ("Evalúa la afirmación «hubo avances en el conocimiento del territorio, pero el control estatal fue desigual». A) es razonable, B) es falsa porque no hubo avances, C) es falsa porque el control era total.", "A", "Combina cambio y continuidad."),
        ("Propón una pregunta de escala regional sobre el norte del país.", "Por ejemplo: ¿qué censos y mapas existían para el desierto de Atacama en 1860?", "La pregunta se ubica en una región concreta."),
    ],
    ctx=("{F} Un video escolar afirma: «En 1880 Chile ya tenía el mismo mapa y el mismo control territorial que hoy». Con el cuadro, escribe una frase que lo matice.", "En 1880 había más mapas y censos, pero aún había territorios que el Estado no controlaba, como parte del sur", "La frase debe incluir un cambio y una continuidad."),
    sc=[("En Historia: ¿qué es una escala regional?", "El tamaño de una zona como el norte o el sur", "Está entre lo local y lo nacional."),
        ("Nombra un cambio entre 1830 y 1880.", "Por ejemplo: aparecieron censos regulares", "Está en el cuadro."),
        ("Nombra una continuidad del cuadro.", "Territorios mapuche al sur del Biobío no controlados por el Estado", "Está en el cuadro.")],
    op=("{F} Con el cuadro de ejemplo de arriba, completa una tabla de dos columnas (cambio y continuidad) con al menos tres filas y escribe una frase final con escalas: una frase nacional y otra regional que no se contradigan.",
        "Cambio: censos regulares; cambio: Oficina Hidrográfica; cambio: acuerdo de límites. Continuidad: territorios mapuche al sur del Biobío; continuidad: pueblos del norte y los canales australes poco registrados. A escala nacional hubo más conocimiento; a escala regional del sur, el control seguía incompleto.",
        ["tabla de dos columnas", "tres filas", "frase con dos escalas"], ["tabla y frase"], ["poner todo como avance", "no distinguir escalas"], "Revisa con alguien de tu casa que cada dato esté en la columna correcta."),
    reinforce="Anota tres datos del cuadro y clasifícalos como cambio o continuidad en una tabla.",
    extend="Escribe una pregunta sobre cómo se habría visto la misma zona en un mapa hecho por quienes vivían allí.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = "Voces de ejemplo, redactadas para este cuaderno. Ministro: «Necesitamos mapas y censos para cobrar impuestos y planificar caminos.» Científico extranjero contratado: «Mi tarea es describir la geología y las plantas del territorio.» Profesor de la Universidad de Chile: «Formamos ingenieros y naturalistas chilenos.» Guía local: «Conozco los pasos de la cordillera desde niño.» Autoridad de una zona de frontera: «Necesitamos saber hasta dónde llega nuestro territorio frente al país vecino.»"
build(
    OA, 4, F4,
    use="Aprenderé a identificar quién impulsó el reconocimiento del territorio, con qué propósitos y qué papel cumplieron científicos, instituciones y habitantes. Sirve para explicar el proceso como obra de varios actores y causas.",
    prior=["Conozco las acciones estatales de exploración.", "Sé qué es la multicausalidad.", "Sé que un testimonio expresa una perspectiva."],
    explain=[
        "El reconocimiento del territorio fue obra de varios actores. El Estado financiaba y decidía; los científicos, muchos extranjeros contratados, describían la geología, las plantas y las costas; la Universidad de Chile formaba profesionales chilenos; y las personas del lugar, como guías, arrieros y mineros, aportaban un conocimiento local sin el cual los viajes habrían sido difíciles.",
        "Los propósitos eran variados y se combinaban. El Estado quería cobrar impuestos, planificar caminos, impulsar la minería y la agricultura, instalar autoridades y fijar los límites frente a países vecinos. Los científicos buscaban conocimiento; algunas autoridades de frontera buscaban seguridad. Por eso hablamos de multicausalidad: no hubo una sola razón para explorar.",
        "Las perspectivas también eran distintas. Para el ministro, conocer el territorio significaba gobernarlo y obtener recursos. Para el guía local, el territorio era su lugar de vida y de trabajo. Estas miradas no siempre coincidían, y los saberes de quienes vivían allí a veces quedaron poco reconocidos en los informes oficiales.",
    ],
    vocab=[("naturalista", "científico que estudia la naturaleza: plantas, animales, rocas"), ("arriero", "persona que conduce animales de carga por caminos y pasos de montaña"), ("impuesto", "pago obligatorio que hacen las personas al Estado"), ("fiscal", "relacionado con los ingresos y gastos del Estado"), ("seguridad fronteriza", "protección del territorio ante conflictos con países vecinos")],
    worked=[
        ("Asociar actor y propósito", "En las voces de ejemplo, ¿qué propósito expresa el ministro y cuál la autoridad de frontera?",
         ["El ministro habla de cobrar impuestos y planificar caminos.", "La autoridad de frontera habla de saber hasta dónde llega el territorio."], "El ministro: recursos y planificación; la autoridad de frontera: delimitar el territorio"),
        ("Valorar el saber local", "¿Por qué el guía local era importante para un viaje científico?",
         ["El científico se movía por un territorio que no conocía.", "El guía conocía los pasos de la cordillera desde niño.", "Sin ese saber el viaje sería más difícil o imposible."], "Porque conocía los pasos y sin él el viaje sería difícil"),
    ],
    mistakes=[
        ("Atribuir la exploración solo a científicos extranjeros.", "Participaron el Estado, la Universidad, guías y habitantes.", "Haz una lista de actores y de su aporte."),
        ("Explicar la exploración con una sola causa, como el interés científico.", "El Estado tenía fines fiscales, económicos y de frontera.", "Escribe al menos tres propósitos."),
    ],
    T=[
        ("En Historia: ¿qué es un naturalista?", "Un científico que estudia la naturaleza: plantas, animales y rocas", "Es el tipo de científico como Gay y Philippi."),
        ("{F} ¿Para qué quiere el ministro mapas y censos?", "Para cobrar impuestos y planificar caminos", "Su voz lo dice."),
        ("{F} ¿Qué dice el profesor de la Universidad de Chile que se forma?", "Ingenieros y naturalistas chilenos", "Su voz lo dice."),
        ("{F} ¿Qué actor conoce los pasos de la cordillera desde niño?", "El guía local", "Su voz lo dice."),
        ("Une cada actor con su propósito: 1) ministro, 2) científico extranjero, 3) autoridad de frontera. a) saber hasta dónde llega el territorio, b) describir geología y plantas, c) cobrar impuestos y planificar caminos. Escribe las parejas.", "1-c, 2-b, 3-a", "Cada voz expresa un propósito."),
        ("{F} Elige el propósito que se relaciona con ingresos del Estado. A) cobrar impuestos, B) describir plantas, C) delimitar la frontera.", "A", "El impuesto es un ingreso fiscal."),
        ("{F} ¿Qué voz representa el saber local y cuál el interés por la frontera?", "El guía local y la autoridad de una zona de frontera", "Cada voz expresa un propósito y un lugar distinto."),
        ("{F} Explica con las voces de ejemplo por qué el Estado combinó propósitos científicos y fiscales.", "Contrató científicos para describir el territorio y quería mapas y censos para cobrar impuestos", "Había varios propósitos a la vez."),
        ("Una compañera dice: «Los guías no importaban porque los científicos tenían los conocimientos». Responde con un dato de las voces de ejemplo.", "El guía conocía los pasos de la cordillera desde niño, un saber que el científico necesitaba", "El saber local era indispensable."),
        ("Explica por qué hablamos de multicausalidad al estudiar la exploración del territorio.", "Porque había varios propósitos a la vez: fiscales, económicos, científicos y de frontera", "Ninguna causa sola lo explica."),
        ("{F} ¿Qué diferencia hay entre la mirada del ministro y la del guía local sobre el territorio?", "El ministro ve recursos y administración; el guía lo ve como su lugar de vida y trabajo", "Sus perspectivas parten de lugares distintos."),
        ("Evalúa la afirmación «la ciencia fue la única razón de la exploración estatal». A) es falsa porque también hubo razones fiscales, económicas y de frontera, B) es verdadera porque el Estado solo financiaba a científicos, C) es verdadera porque los censos y los mapas no tenían usos prácticos.", "A", "Hubo varios propósitos."),
        ("Redacta una pregunta que contraste el interés del científico extranjero con el del guía local.", "Por ejemplo: ¿qué buscaba cada uno al recorrer el territorio y quién se benefició del informe?", "La pregunta compara propósitos y beneficios."),
    ],
    ctx=("{F} En un video del colegio sobre una expedición, aparecen solo el científico y el ministro. ¿A qué otros dos actores de las voces de ejemplo incluirías y por qué?", "Incluiría al guía local, que conoce los pasos, y al profesor de la Universidad, que forma profesionales", "Ambos aportan al reconocimiento del territorio."),
    sc=[("En Historia: ¿qué es un impuesto?", "Un pago obligatorio que hacen las personas al Estado", "Es uno de los propósitos fiscales."),
        ("Nombra dos actores del reconocimiento del territorio.", "Por ejemplo: el Estado y los científicos", "Ambos participaron en el proceso."),
        ("¿Qué aportaba un guía local?", "Conocimiento de los pasos y senderos del lugar", "Era un saber local.")],
    op=("{F} Elige dos voces de ejemplo de arriba y escribe cinco líneas: qué propósito expresa cada una, una causa de la exploración y una diferencia de perspectiva entre ellas.",
        "El ministro quiere cobrar impuestos y planificar caminos. El guía local conoce los pasos de la cordillera. Una causa de la exploración fue el interés por desarrollar los recursos. El ministro mira el territorio como algo por administrar; el guía, como su lugar de vida y trabajo.",
        ["dos voces", "una causa", "diferencia de perspectiva"], ["texto de cinco líneas"], ["usar una sola voz", "no marcar diferencia"], "Cuéntale tu texto a alguien de tu casa y pídele que diga cuál es la diferencia."),
    reinforce="Haz una tabla con cuatro actores del tema y un propósito para cada uno.",
    extend="Explica por qué es importante reconocer el saber local en la historia de los viajes científicos.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = "Dossier de ejemplo. Dato 1: el Estado contrató científicos (Gay, Philippi, Pissis) y financió misiones de exploración. Dato 2: el censo de 1854 y los siguientes contaron a la población según categorías definidas por el Estado. Dato 3: la Universidad de Chile formó profesionales y la Oficina Hidrográfica estudió costas y canales. Dato 4: el tratado de límites de 1881 fijó la frontera con Argentina por las altas cumbres que dividen aguas. Dato 5: había territorios habitados por pueblos que el Estado conocía solo en parte."
build(
    OA, 5, F5,
    use="Aprenderé a argumentar con evidencia para qué sirvieron los censos, las misiones científicas y las instituciones, y qué límites tuvo ese conocimiento. Sirve para responder con equilibrio entre avances científicos y control estatal.",
    prior=["Conozco la exploración, los censos y las fuentes cartográficas.", "Sé distinguir cambio y continuidad.", "Sé qué es una tesis y una evidencia."],
    explain=[
        "Un argumento sobre la exploración estatal responde a una pregunta como «¿Para qué reconoció el Estado su territorio y qué papel cumplió la ciencia?». Una tesis posible es que el Estado usó la ciencia para caracterizar la población, desarrollar recursos, administrar y fijar fronteras, y que ese conocimiento, aunque útil, no era neutral ni completo.",
        "Las evidencias deben explicarse. El dato de que se contrató a Gay, Philippi y Pissis muestra interés en el conocimiento científico. El dato de los censos muestra que el Estado definía las categorías con que contaba a las personas. El dato del tratado de 1881 muestra el propósito de delimitar la frontera. Y el dato 5 muestra el límite: había pueblos que el Estado conocía solo en parte.",
        "El argumento debe incluir un límite. Con el dossier no podemos afirmar que los censos fueran inexactos ni que los científicos actuaran solo al servicio del Estado; solo que su trabajo respondía a propósitos estatales y dejaba vacíos. Evita frases como «el Estado lo sabía todo» o «los científicos no sirvieron para nada».",
    ],
    vocab=[("tesis", "afirmación principal que se defiende"), ("evidencia", "dato o fuente que apoya la tesis"), ("neutral", "que no toma partido ni responde a intereses"), ("delimitar", "fijar los límites o fronteras de un territorio"), ("vacío de una fuente", "aquello que la fuente no cubre")],
    worked=[
        ("Elegir evidencias", "Para sostener que «el conocimiento científico no era neutral», ¿qué dos datos del dossier sirven?",
         ["El dato 2 muestra que el Estado define las categorías del censo.", "El dato 5 muestra que había pueblos poco registrados."], "Datos 2 y 5"),
        ("Formular el límite", "¿Qué frase excede el dossier: «los censos fueron siempre falsos»?",
         ["El dossier muestra categorías definidas por el Estado.", "No prueba que las cifras fueran falsas."], "Excede porque el dossier no prueba que fueran falsos"),
    ],
    mistakes=[
        ("Escribir que la ciencia fue neutral.", "Los proyectos científicos respondían a propósitos del Estado.", "Pregunta quién encargó y para qué."),
        ("Afirmar que la ciencia no sirvió.", "Aportó conocimiento real sobre el territorio.", "Reconoce aportes y límites a la vez."),
    ],
    T=[
        ("En Historia: ¿qué significa delimitar?", "Fijar los límites o fronteras de un territorio", "Es el propósito del tratado de 1881."),
        ("{F} ¿Qué dato muestra el propósito de fijar la frontera? A) dato 1, B) dato 4, C) dato 3.", "B", "El dato 4 menciona el tratado de 1881."),
        ("{F} ¿Qué científicos nombra el dato 1?", "Gay, Philippi y Pissis", "El dossier los menciona."),
        ("{F} ¿Qué institución estudió costas y canales según el dato 3?", "La Oficina Hidrográfica", "El dato la nombra."),
        ("Elige la tesis mejor formulada. A) El Estado conoció todo su territorio gracias a los censos, B) El Estado usó la ciencia para conocer, administrar y delimitar el territorio, aunque ese conocimiento no era neutral ni completo, C) Los científicos extranjeros trabajaron por su cuenta, sin relación con el Estado.", "B", "Es defendible con el dossier."),
        ("Una compañera usa solo el dato 3 para afirmar que «el Estado conocía todo el territorio». ¿Qué dato le falta considerar?", "El dato 5, que muestra pueblos conocidos solo en parte", "La evidencia es parcial."),
        ("{F} ¿Qué dato del dossier muestra un límite del conocimiento estatal?", "El dato 5", "Dice que había pueblos que el Estado conocía solo en parte."),
        ("Un grupo escribe una tesis con tres datos, pero ninguna frase de límite. ¿Qué podría agregar?", "Una frase que diga qué no se puede afirmar con esos datos, como lo que pensaban los pueblos que vivían allí", "El límite señala lo que la evidencia no permite afirmar."),
        ("{F} Con los datos 2 y 5, redacta una conclusión proporcional.", "El censo contaba según categorías del Estado y había pueblos que el Estado conocía solo en parte", "Une el dato y su límite."),
        ("Explica por qué una buena respuesta debe reconocer los aportes y los límites de la ciencia estatal.", "Porque la ciencia produjo conocimiento útil, pero respondió a propósitos del Estado y dejó vacíos", "Evita los extremos en la conclusión."),
        ("Un compañero escribe: «Los censos mostraron la realidad exacta de todos». Señala la exageración.", "«Exacta» y «todos» exceden la evidencia, porque el censo usa categorías del Estado", "Es una afirmación absoluta."),
        ("Evalúa este argumento: «El Estado financió ciencia (dato 1) para conocer el territorio, pero hubo pueblos poco registrados (dato 5)». A) es sólido porque une avance y límite, B) es débil porque solo menciona avances y no reconoce ningún límite, C) es falso porque el Estado conocía por completo a todos los pueblos.", "A", "Usa evidencias de ambos lados."),
        ("Escribe una pregunta que exigiría otra fuente para completar el argumento.", "Por ejemplo: ¿cómo describían el territorio las comunidades que vivían allí?", "La pregunta señala un vacío del dossier."),
    ],
    ctx=("{F} En una charla escolar alguien dice «los mapas y censos del siglo XIX eran puramente científicos, sin intereses políticos». Con el dossier, escribe tu respuesta en dos frases con una evidencia.", "No eran puramente científicos: el Estado los usaba para administrar y delimitar, como el tratado de 1881", "La respuesta debe usar el dato 4."),
    sc=[("En Historia: ¿qué es un vacío de una fuente?", "Aquello que la fuente no cubre", "Toda fuente tiene vacíos."),
        ("Nombra un propósito estatal del reconocimiento del territorio.", "Por ejemplo: delimitar las fronteras", "Es el dato 4."),
        ("¿Qué muestra el dato 5?", "Que había pueblos que el Estado conocía solo en parte", "Es un límite del conocimiento estatal.")],
    op=("{F} Con el dossier de ejemplo de arriba, escribe un párrafo de siete líneas que responda: «¿Para qué reconoció el Estado su territorio y qué límites tuvo ese conocimiento?». Incluye una tesis, dos evidencias explicadas y un límite.",
        "El Estado reconoció el territorio para caracterizar la población, desarrollar recursos, administrar y fijar fronteras. Contrató a científicos y realizó censos, pero estos usaban categorías definidas por el Estado. Además, había pueblos que el Estado conocía solo en parte. Límite: no sabemos qué opinaban esos pueblos.",
        ["tesis", "dos evidencias explicadas", "límite"], ["párrafo de siete líneas"], ["omitir el límite", "no explicar las evidencias"], "Pide a alguien de tu casa que marque tu tesis."),
    reinforce="Reescribe tu tesis en una frase y apunta debajo las dos evidencias del dossier que usaste.",
    extend="Escribe una segunda tesis centrada en los límites del conocimiento estatal y el dato nuevo que necesitarías.",
    materials=MAT,
)
