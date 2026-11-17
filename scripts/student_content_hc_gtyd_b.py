"""Geografía, territorio y desafíos socioambientales (electivo HC, 3.º y 4.º medio): OAC-04 (organización territorial y ambiental e instrumentos de planificación), OAC-05 (carácter social del riesgo de desastres) y OAC-06 (métodos de la geografía), 15 clases. Lugares, mapas descritos y cifras ficticios o de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno; si quieres, una regla y lápices de colores para dibujar los croquis. No se necesita computador ni internet: cada mapa, croquis, tabla o texto se describe por escrito en el enunciado, con su cuadrícula y sus escalas. "
             "Las comunas, los barrios, los grupos y las cifras (Villa Alta, Quebrada Seca, Puerto Claro, etc.) son ficticios o de ejemplo y sirven para practicar el método de la geografía, no para aprender datos de un territorio real. "
             "Cuando un tema toque los territorios de los pueblos originarios, la información propia la entregan el educador o la educadora tradicional y la comunidad. "
             "Las posturas se presentan con sus razones y sin tomar partido. En los temas de riesgo de desastres, si algo te preocupa o te afecta, conversa con una persona adulta de confianza; no necesitas exponer tu experiencia personal. Si haces trabajo de campo, acude acompañado por una persona adulta y a lugares seguros.")
build = make_build(MATERIALS)

O4 = "HI-GTYD-3y4-OAC-04"
O5 = "HI-GTYD-3y4-OAC-05"
O6 = "HI-GTYD-3y4-OAC-06"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (croquis descrito de la comuna ficticia de Villa Alta). Cuadrícula de 6 columnas (1 a 6, de oeste a este) y 4 filas (1 a 4, de norte a sur); cada cuadro mide 1 kilómetro por lado. "
     "Centro cívico, con municipalidad, consultorio y escuela: columna 2, fila 2. Población nueva «Los Aromos»: columna 6, fila 4. Cerro con bosque nativo: columna 3, fila 1. "
     "Un estero cruza de norte a sur por la columna 4, con zona inundable en las filas 3 y 4. Una única calle une Los Aromos con el centro y cruza el estero por un puente en la columna 4, fila 4. "
     "Distancia por calles: se suman los cuadros recorridos en horizontal y en vertical.")
build(
    O4, 1, F,
    use="Aprenderé a situar la organización territorial del país (regiones, provincias y comunas) y los instrumentos de planificación que la regulan, y a ubicar un caso local en esa organización antes de evaluarlo con criterios.",
    prior=["Conozco decisiones y actores de un territorio.", "Sé leer un croquis con cuadrícula.", "He estudiado la organización político-administrativa de Chile."],
    explain=[
        "El territorio de Chile se organiza en regiones, estas en provincias y estas en comunas. La comuna es la unidad más cercana a las personas y la gobierna una municipalidad. La organización territorial es la forma en que el Estado divide el espacio para administrarlo y planificarlo. La organización ambiental es la forma en que se protegen y se usan los ambientes: parques, reservas, humedales, cuencas.",
        "Los instrumentos de planificación son documentos que orientan y regulan qué se puede hacer en el territorio. A escala comunal, el plan regulador define los usos del suelo urbano (vivienda, comercio, industria, áreas verdes, zonas de riesgo) y las vías; el plan de desarrollo comunal fija metas y proyectos de la municipalidad para varios años. A escala regional, una estrategia de desarrollo orienta las prioridades de la región. A escala del país hay políticas nacionales y normas ambientales. Las áreas protegidas son territorios con reglas especiales de cuidado.",
        "Evaluar la organización territorial y ambiental significa preguntar si estos instrumentos y la forma en que se aplican cumplen criterios. En esta asignatura los criterios son la accesibilidad, la conectividad, la conservación, la preservación, la reducción de riesgos, la sustentabilidad ambiental y la justicia socioespacial. En esta primera clase se contextualiza: quién planifica, a qué escala y con qué instrumento, y cómo se ubica el caso en el espacio.",
    ],
    vocab=[("organización territorial", "forma en que el Estado divide el espacio para administrarlo y planificarlo"), ("plan regulador", "instrumento que define usos del suelo y vías de una ciudad o comuna"), ("plan de desarrollo comunal", "instrumento con metas y proyectos de la municipalidad para varios años"), ("área protegida", "territorio con reglas especiales de cuidado"), ("criterio de evaluación", "aspecto con que se juzga una organización o una decisión")],
    worked=[
        ("Leer una distancia en la cuadrícula", "En el croquis de una comuna ficticia, el consultorio está en columna 1, fila 1 y una escuela en columna 4, fila 3. ¿Cuál es la distancia por calles?",
         ["Cuadros en horizontal: 4 − 1 = 3.", "Cuadros en vertical: 3 − 1 = 2; total 3 + 2 = 5."],
         "5 kilómetros"),
        ("Asociar instrumento y escala", "Una región ficticia quiere definir sus prioridades de desarrollo para los próximos años. ¿Qué escala e instrumento corresponden?",
         ["Se trata de toda la región, no de una comuna.", "Lo orienta una estrategia regional de desarrollo."],
         "Escala regional; estrategia regional de desarrollo"),
    ],
    mistakes=[("Confundir la escala comunal con la regional.", "Se supone que el plan regulador decide por toda la región.", "Ubica cada instrumento en su escala: el plan regulador es comunal; la estrategia de desarrollo, regional."),
              ("Evaluar un caso sin ubicarlo primero.", "Se salta la contextualización.", "Antes de evaluar, nombra la escala, el instrumento y los actores que planifican.")],
    T=[
        ("abc", "{F} ¿En qué cuadro está el centro cívico de Villa Alta?", "Columna 2, fila 2", "Columna 6, fila 4", "Columna 3, fila 1", "La ficha ubica el centro cívico en la columna 2, fila 2."),
        ("En Geografía: ¿cómo se llama el instrumento que define los usos del suelo urbano y las vías de una comuna?", "Plan regulador", "El plan regulador define usos del suelo y vías, según la explicación."),
        ("abc", "{F} ¿Qué unidad administrativa gobierna una municipalidad?", "La comuna", "La región", "La provincia", "La municipalidad gobierna la comuna, que es la unidad más cercana a las personas."),
        ("=", "{F} ¿Cuántos kilómetros hay por calles entre Los Aromos y el centro cívico? Suma los cuadros en horizontal y en vertical.", "(6-2)+(4-2)", "Son 4 cuadros en horizontal y 2 en vertical, y cada cuadro mide 1 kilómetro.", " kilómetros"),
        ("abc", "{F} ¿Qué rasgo del territorio de Villa Alta obliga a considerar un riesgo en su planificación?", "El estero con zona inundable en las filas 3 y 4", "El cerro con bosque nativo", "El centro cívico", "Una zona inundable es un riesgo que debe regularse en el plan regulador."),
        ("abc", "{F} ¿Qué instrumento y escala corresponden a decidir dónde habrá áreas verdes en Villa Alta?", "El plan regulador, a escala comunal", "La estrategia regional, a escala del país", "Una política mundial", "Los usos del suelo urbano de una comuna los define su plan regulador."),
        ("abc", "{F} El plan de desarrollo comunal de Villa Alta define metas para cinco años. ¿Qué lo diferencia del plan regulador?", "Fija metas y proyectos, mientras el regulador define usos del suelo", "Define los usos del suelo y las zonas de riesgo, igual que el plan regulador", "Solo se aplica a las áreas protegidas", "Uno orienta metas y proyectos; el otro regula usos del suelo y vías."),
        ("abc", "{F} ¿Qué dato permite evaluar la accesibilidad de Los Aromos?", "La distancia por calles al centro y a los servicios", "El número de árboles del cerro", "El nombre del estero", "La accesibilidad se mide por la facilidad de llegar a los servicios."),
        ("abc", "{F} Se propone un parque protegido en el cerro de la columna 3, fila 1. ¿Qué tipo de territorio sería?", "Un área protegida", "Una zona de expansión urbana", "Una región administrativa", "Un territorio con reglas especiales de cuidado es un área protegida."),
        ("{F} Explica por qué Los Aromos podría tener menor accesibilidad que el centro.", "Porque está a mayor distancia del centro y depende de una única calle que cruza el estero", "La distancia y la dependencia de una sola vía limitan el acceso a los servicios."),
        ("abc", "{F} Si el puente en la columna 4, fila 4 quedara cerrado por una inundación, ¿qué criterio sería el más afectado?", "La conectividad, porque Los Aromos quedaría aislada del centro", "La conservación del bosque nativo", "La preservación del cerro", "Una única vía cortada deja un sector sin enlace con el resto, lo que afecta la conectividad."),
        ("abc", "{F} Antes de evaluar la organización territorial de Villa Alta, ¿qué conviene hacer?", "Identificar la escala, el instrumento y los actores que planifican", "Decidir si el plan es bueno o malo", "Elegir un actor al azar", "Contextualizar es el primer paso: ubicar escala, instrumento y actores."),
        ("abc", "{F} ¿Cuál es una pregunta de contexto para estudiar Los Aromos?", "¿Cuándo se construyó, quién la planificó y con qué instrumento?", "¿Cuál es la comuna más poblada de otra región?", "¿Qué opina de ella alguien que nunca la ha visitado?", "Contextualizar es ubicar tiempo, actores e instrumento de planificación."),
    ],
    ctx=("abc", "Una comuna ficticia planea una población nueva junto a un río que se desborda. ¿Qué instrumento debería regular esta decisión a escala comunal?", "El plan regulador, que define usos del suelo y zonas de riesgo", "Una norma de otro país", "La estrategia de turismo de una región lejana", "El plan regulador comunal es el instrumento que regula dónde puede haber viviendas y dónde hay riesgo."),
    sc=[
        ("En Geografía: ¿en qué orden se organiza el territorio de Chile, de mayor a menor?", "Regiones, provincias y comunas", "Cada región se divide en provincias y cada provincia en comunas."),
        ("¿Qué es un área protegida?", "Un territorio con reglas especiales de cuidado", "Su protección se define por reglas propias."),
        ("¿Qué instrumento define los usos del suelo urbano de una comuna?", "El plan regulador", "Define vivienda, comercio, industria, áreas verdes y zonas de riesgo."),
    ],
    op=("Dibuja o describe un croquis de una comuna ficticia con una cuadrícula de 5 columnas por 4 filas (cada cuadro de 1 kilómetro). Ubica un centro cívico, una población nueva, un río con zona inundable, un parque protegido y una carretera. "
        "Escribe la distancia por calles entre la población y el centro, qué instrumento regularía cada elemento y a qué escala, y una pregunta de contexto.",
        "Centro: columna 2, fila 2. Población: columna 5, fila 4. Distancia: 3 + 2 = 5 kilómetros. Río en la columna 4: plan regulador, escala comunal. Parque: área protegida. Carretera: política nacional. Pregunta: ¿quién planificó la población y cuándo?",
        ["ubica los cinco elementos en la cuadrícula", "calcula bien la distancia por calles", "asocia cada elemento con un instrumento y una escala", "formula una pregunta de contexto"],
        ["croquis con cinco elementos, un cálculo y una pregunta"],
        ["contar mal los cuadros", "asociar un instrumento regional a un elemento comunal", "olvidar la zona inundable"],
        "Pregunta: «¿cuántos cuadros recorres en horizontal y cuántos en vertical?». Si no lo calcula, pídele que cuente las columnas y las filas."),
    reinforce="Dibuja el croquis de tu barrio con una cuadrícula simple, ubica tres servicios y anota la distancia por calles desde tu casa a cada uno.",
    extend="Averigua con tu municipalidad o tu colegio qué instrumentos de planificación tiene tu comuna y para qué sirve cada uno.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (datos de ejemplo, ficticios). Tres sectores de Villa Alta. Centro: 2.000 habitantes; consultorio a 400 metros; 8 buses por hora; áreas verdes 12.000 metros cuadrados. "
     "Las Lomas: 1.500 habitantes; consultorio a 1.800 metros; 3 buses por hora; áreas verdes 6.000 metros cuadrados. Los Aromos: 1.000 habitantes; consultorio a 6.000 metros; 1 bus por hora; áreas verdes 1.000 metros cuadrados. "
     "Fuentes: (M) registro municipal con estos datos; (V) encuesta vecinal que dice «en Los Aromos nos sentimos aislados»; (A) folleto de la municipalidad que afirma «todos los sectores tienen buena conexión».")
build(
    O4, 2, F,
    use="Aprenderé a interrogar indicadores de accesibilidad, conectividad y áreas verdes y a distinguir lo que un promedio o un total esconde, para evaluar la organización territorial con evidencia.",
    prior=["Sé qué es un indicador y una fuente.", "Calculo razones sencillas.", "Conozco los instrumentos de planificación."],
    explain=[
        "La accesibilidad es la facilidad con que las personas llegan a los servicios y lugares que necesitan: depende de la distancia, el tiempo, el costo y las barreras (un río, una pendiente, una calle sin vereda). La conectividad es el grado en que los lugares están enlazados por vías y transporte: depende de cuántas rutas hay, con qué frecuencia pasan los buses y si existe una alternativa cuando una vía se corta. Ambas se miden con indicadores, pero no son lo mismo: un servicio puede estar cerca (accesible) y una población aislada si solo tiene una vía (poco conectada).",
        "Un indicador útil de áreas verdes es la superficie por habitante, que se calcula dividiendo los metros cuadrados de áreas verdes entre el número de habitantes. Un total comunal o un promedio puede esconder desigualdades: si un sector tiene mucho y otro casi nada, el promedio parece aceptable aunque haya sectores desfavorecidos. Por eso se desagrega, es decir, se separa el indicador por sectores.",
        "Como toda fuente, los registros, las encuestas y los folletos tienen productor y propósito. Un folleto municipal que dice «todos los sectores tienen buena conexión» necesita datos que lo respalden. La encuesta vecinal entrega la experiencia de quienes viven allí, que los números no siempre muestran. Se usan juntas: los datos dicen cuánto, los testimonios dicen cómo se vive.",
    ],
    vocab=[("accesibilidad", "facilidad con que las personas llegan a los servicios que necesitan"), ("conectividad", "grado en que los lugares están enlazados por vías y transporte"), ("desagregar", "separar un indicador por sectores o grupos"), ("áreas verdes por habitante", "metros cuadrados de áreas verdes divididos por el número de habitantes"), ("frecuencia", "cuántas veces pasa un servicio en un tiempo")],
    worked=[
        ("Calcular un indicador por habitante", "Un sector ficticio tiene 9.000 metros cuadrados de áreas verdes y 3.000 habitantes. ¿Cuántos metros cuadrados hay por habitante?",
         ["Divide la superficie entre los habitantes.", "9.000 ÷ 3.000 = 3."],
         "3 metros cuadrados por habitante"),
        ("Distinguir accesibilidad y conectividad", "Un barrio ficticio tiene un consultorio a 300 metros, pero solo una calle que se inunda y lo une al resto. ¿Qué criterio es bueno y cuál es débil?",
         ["El consultorio cercano implica buena accesibilidad.", "La calle única que se corta implica baja conectividad."],
         "Buena accesibilidad y baja conectividad"),
    ],
    mistakes=[("Usar el promedio comunal para decir que todos los sectores están bien.", "El promedio esconde las diferencias entre sectores.", "Desagrega los indicadores por sector."),
              ("Confundir accesibilidad con conectividad.", "Ambas se refieren a llegar a lugares, pero miden cosas distintas.", "Accesibilidad es llegar a un servicio; conectividad es el enlace entre lugares mediante vías y transporte.")],
    T=[
        ("abc", "{F} ¿Qué sector está más lejos del consultorio?", "Los Aromos", "Las Lomas", "Centro", "Los Aromos está a 6.000 metros, la mayor distancia."),
        ("abc", "{F} ¿Qué fuente corresponde a la experiencia de los vecinos?", "La encuesta vecinal (V)", "El registro municipal (M)", "El folleto de la municipalidad (A)", "La ficha rotula con (V) la encuesta de los vecinos."),
        ("En Geografía: ¿cómo se llama la facilidad con que las personas llegan a los servicios que necesitan?", "Accesibilidad", "Esa es la definición de accesibilidad."),
        ("=", "{F} ¿Cuántos metros cuadrados de áreas verdes por habitante tiene el Centro?", "12000//2000", "Se divide la superficie de áreas verdes entre el número de habitantes.", " metros cuadrados por habitante"),
        ("=", "{F} ¿Cuántos metros cuadrados de áreas verdes por habitante tiene Las Lomas?", "6000//1500", "Se divide 6.000 metros cuadrados entre 1.500 habitantes.", " metros cuadrados por habitante"),
        ("=", "{F} ¿Cuántos metros cuadrados de áreas verdes por habitante tiene Los Aromos?", "1000//1000", "Se divide 1.000 metros cuadrados entre 1.000 habitantes.", " metro cuadrado por habitante"),
        ("abc", "{F} El folleto (A) dice que todos los sectores tienen buena conexión. ¿Qué dato de la ficha lo cuestiona?", "Los Aromos tiene solo 1 bus por hora", "El Centro tiene 8 buses por hora", "Las Lomas tiene áreas verdes", "Un solo bus por hora es una frecuencia baja que contradice «buena conexión»."),
        ("abc", "{F} ¿Qué indicador de la ficha mide la conectividad por transporte?", "Los buses por hora de cada sector", "Los habitantes de cada sector", "Los metros cuadrados de áreas verdes", "La frecuencia de buses indica qué tan enlazado está cada sector."),
        ("abc", "{F} Un funcionario dice: «Villa Alta tiene en promedio suficientes áreas verdes». ¿Qué conviene hacer?", "Desagregar por sector para ver si hay desigualdades", "Aceptarlo porque es un funcionario", "Eliminar el indicador", "Un promedio puede esconder diferencias entre sectores."),
        ("abc", "{F} Un estudiante afirma: «Los Aromos tiene la peor accesibilidad». ¿Qué datos de la ficha lo respaldan?", "Consultorio a 6.000 metros y 1 bus por hora", "Solo la cantidad de habitantes", "Solo las áreas verdes", "La distancia y la frecuencia de transporte miden facilidad de llegada a los servicios."),
        ("abc", "{F} ¿Qué aporta la encuesta vecinal (V) que no aportan los números?", "Cómo viven los vecinos la falta de conexión", "Una cifra exacta de buses", "La superficie del cerro", "Un testimonio muestra la experiencia vivida."),
        ("{F} Explica por qué Los Aromos podría estar cerca de algo y aun así estar poco conectada.", "Porque la cercanía mide accesibilidad, pero la conexión depende de rutas y frecuencia de transporte", "Accesibilidad y conectividad no son lo mismo: puede haber cercanía con pocas vías o poca frecuencia."),
        ("abc", "{F} ¿Qué dato falta para evaluar la accesibilidad de Las Lomas con más precisión?", "El tiempo real de viaje y si hay vereda o ciclovía", "El nombre de las calles", "El año de fundación", "La accesibilidad depende de tiempo, costo y barreras, no solo de la distancia."),
    ],
    ctx=("abc", "Un concejo comunal ficticio debe elegir dónde ubicar un nuevo parque. El promedio comunal de áreas verdes es de 4 metros cuadrados por habitante, pero un sector tiene 1 y otro 7. ¿Qué criterio conviene aplicar?", "Priorizar el sector con menos áreas verdes por habitante", "Ubicarlo donde ya hay más áreas verdes", "No construirlo, porque el promedio es suficiente", "El promedio esconde desigualdades; priorizar donde hay menos es un criterio de justicia."),
    sc=[
        ("En Geografía: ¿qué es la conectividad?", "El grado en que los lugares están enlazados por vías y transporte", "Depende de rutas, frecuencia y alternativas."),
        ("¿Qué significa desagregar un indicador?", "Separarlo por sectores o grupos", "Así se ven las diferencias que un promedio esconde."),
        ("¿Cómo se calculan las áreas verdes por habitante?", "Dividiendo la superficie de áreas verdes entre el número de habitantes", "Es una razón entre metros cuadrados y personas."),
    ],
    op=("Usa estos datos ficticios de tres barrios: Barrio Norte, 800 habitantes, 4.000 metros cuadrados de áreas verdes, 6 buses por hora, escuela a 300 metros; Barrio Centro, 1.000 habitantes, 5.000 metros cuadrados, 10 buses por hora, escuela a 200 metros; Barrio Sur, 500 habitantes, 500 metros cuadrados, 1 bus por hora, escuela a 2.500 metros. "
        "Calcula las áreas verdes por habitante de cada barrio, señala qué barrio tiene menor accesibilidad y conectividad, y escribe qué dato adicional pedirías para completar el diagnóstico.",
        "Norte: 4.000 ÷ 800 = 5. Centro: 5.000 ÷ 1.000 = 5. Sur: 500 ÷ 500 = 1. Menor accesibilidad y conectividad: Barrio Sur (escuela a 2.500 metros, 1 bus por hora). Dato: tiempo de viaje real y seguridad del camino.",
        ["calcula bien las áreas verdes por habitante", "identifica el barrio con menor accesibilidad y conectividad con datos", "propone un dato adicional pertinente", "no usa solo el promedio"],
        ["tabla con tres cálculos, una conclusión y un dato por pedir"],
        ["dividir al revés", "confundir accesibilidad con conectividad", "proponer un dato irrelevante"],
        "Pregunta: «¿qué barrio quedaría peor si solo miraras el promedio?». Si no lo identifica, pídele que revise la desagregación."),
    reinforce="Mide con pasos o con un mapa cuánto demoras desde tu casa al servicio más cercano y escribe qué barreras encuentras.",
    extend="Compara dos barrios de tu comuna por su acceso a áreas verdes y transporte, y anota qué datos tendrías que pedir a la municipalidad.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (tres terrenos de Villa Alta, ficticios). Terreno 1, Humedal del Estero: refugio de aves y suelo muy sensible; el plan propone mantenerlo sin intervenciones. "
     "Terreno 2, Bosque del Cerro: bosque nativo donde se permite recoger hojas y ramas secas y hacer senderos con reglas y guardaparques; el plan propone proteger y usar de forma regulada. "
     "Terreno 3, Borde del Río: barrio con calles de tierra, sin plazas ni transporte frecuente y con riesgo de crecidas; los beneficios de parques y buses se concentran en otros sectores.")
build(
    O4, 3, F,
    use="Aprenderé a distinguir conservación de preservación y a reconocer la justicia socioespacial como criterio, para comparar causas y perspectivas en decisiones sobre la organización ambiental del territorio.",
    prior=["Conozco accesibilidad y conectividad.", "Sé qué es un área protegida.", "Distingo posición e interés."],
    explain=[
        "La preservación es mantener un ambiente sin intervención o con intervención mínima, para que sus condiciones y especies sigan existiendo tal como son. La conservación es proteger un ambiente permitiendo un uso racional que asegure su permanencia y su capacidad de regeneración, por ejemplo con senderos, recolección regulada o turismo cuidado. Ambas buscan que el ambiente no se degrade, pero una limita el uso y la otra lo regula.",
        "La justicia socioespacial es el criterio según el cual los beneficios y las cargas del territorio deben repartirse de forma justa entre los grupos. Los beneficios son parques, transporte, servicios y seguridad; las cargas son riesgos, contaminación o falta de servicios. Hay injusticia socioespacial cuando los beneficios se concentran en unos sectores y los riesgos o las carencias se concentran en otros, sin que esa diferencia tenga una razón justificada.",
        "Las causas de estas desigualdades suelen ser varias: el precio del suelo, las reglas de planificación de otras épocas, las decisiones de inversión y la falta de participación de algunos grupos. Los actores tienen perspectivas distintas: una ONG puede defender la preservación, una cooperativa de recolectores puede defender la conservación con uso regulado y los vecinos del Borde del Río pueden priorizar servicios y seguridad. Comparar significa entender qué criterio prioriza cada uno.",
    ],
    vocab=[("preservación", "mantener un ambiente sin intervención o con intervención mínima"), ("conservación", "proteger un ambiente permitiendo un uso racional que asegure su permanencia"), ("justicia socioespacial", "reparto justo de beneficios y cargas del territorio entre los grupos"), ("carga territorial", "riesgo, contaminación o carencia que recae sobre un sector"), ("uso regulado", "uso permitido con reglas, límites y control")],
    worked=[
        ("Distinguir conservación y preservación", "Un humedal ficticio no admite ninguna intervención; un bosque ficticio admite senderos con reglas. ¿Cuál es preservación y cuál conservación?",
         ["Sin intervención: preservación.", "Con uso regulado: conservación."],
         "Humedal: preservación; bosque: conservación"),
        ("Detectar injusticia socioespacial", "Un barrio ficticio tiene tres plazas y buses cada 10 minutos; otro tiene riesgo de aluvión y una sola calle de tierra. ¿Qué criterio está en juego?",
         ["Los beneficios están en un barrio.", "Las cargas y carencias están en el otro."],
         "Justicia socioespacial"),
    ],
    mistakes=[("Usar «conservación» y «preservación» como sinónimos.", "Ambas protegen, pero una limita el uso y la otra lo regula.", "Pregunta si el plan prohíbe el uso o lo permite con reglas."),
              ("Pensar que justicia socioespacial es dar lo mismo a todos.", "Se confunde reparto justo con reparto idéntico.", "Pregunta si las diferencias se explican por necesidades o riesgos y no por el origen del sector.")],
    T=[
        ("abc", "{F} ¿Qué terreno propone el plan mantener sin intervenciones?", "El Humedal del Estero", "El Bosque del Cerro", "El Borde del Río", "Según la ficha, el plan propone mantener el humedal sin intervenciones."),
        ("En Geografía: ¿cómo se llama mantener un ambiente sin intervención o con intervención mínima?", "Preservación", "Esa es la definición de preservación."),
        ("abc", "{F} ¿Qué terreno se destinaría a conservación con uso regulado?", "El Bosque del Cerro", "El Humedal del Estero", "El Borde del Río", "El bosque admite recolección y senderos con reglas, que es un uso regulado."),
        ("abc", "{F} ¿Qué criterio está en juego en el Borde del Río?", "La justicia socioespacial", "La preservación", "La conservación", "Los beneficios se concentran en otros sectores mientras el barrio carga con riesgos."),
        ("abc", "{F} ¿Qué carga territorial soporta el Borde del Río?", "El riesgo de crecidas", "Un bosque nativo", "Un refugio de aves", "La ficha menciona el riesgo de crecidas como carga del barrio."),
        ("abc", "{F} ¿Qué diferencia hay entre el plan del humedal y el del bosque?", "El humedal limita el uso y el bosque lo regula", "El humedal permite más usos que el bosque", "El humedal se conserva con uso regulado y el bosque se preserva sin uso", "Uno es preservación y el otro conservación."),
        ("abc", "Una ONG ficticia pide no autorizar ningún sendero en un humedal frágil. ¿Qué criterio prioriza?", "La preservación", "La conectividad", "La accesibilidad", "Pedir cero intervención es una postura de preservación."),
        ("abc", "Una cooperativa ficticia pide recolectar hojas y ramas secas del bosque con reglas y control. ¿Qué criterio prioriza?", "La conservación con uso regulado", "La preservación sin uso", "La justicia socioespacial únicamente", "Permitir un uso con reglas es la lógica de la conservación."),
        ("abc", "{F} Un vecino del Borde del Río dice que su prioridad es contar con transporte y protección frente a crecidas. ¿Qué criterio destaca?", "La justicia socioespacial y la reducción de riesgos", "Solo la preservación", "Ninguno", "Pide acceso a beneficios y menos riesgo, que son criterios de justicia y seguridad."),
        ("abc", "{F} ¿Qué estrategia permitiría combinar los intereses de los tres terrenos?", "Preservar el humedal, conservar el bosque con uso regulado y mejorar servicios y protección en el Borde del Río", "Preservar los tres terrenos por igual", "Construir viviendas en los tres terrenos", "Cada terreno requiere un criterio distinto según su fragilidad y sus necesidades."),
        ("{F} Explica por qué dar un parque a un barrio que ya tiene tres plazas no resuelve la injusticia del Borde del Río.", "Porque la injusticia es la falta de beneficios y el riesgo en el Borde del Río, no en el barrio que ya tiene parques", "La justicia exige corregir la desigualdad en el sector que carece de beneficios."),
        ("abc", "{F} Dos actores discuten: uno dice «preservar todo» y otro «usar todo». ¿Qué posición se acerca más a la conservación?", "Usar de forma regulada, con reglas que aseguren la permanencia del ambiente", "Prohibir todo uso", "Permitir cualquier uso sin control", "La conservación busca un uso racional con regulación."),
        ("abc", "{F} ¿Qué evidencia ayudaría a decidir si un terreno debe preservarse o conservarse?", "Un estudio de su fragilidad y de cuánto uso soporta sin degradarse", "Cuántos vecinos prefieren caminar por el lugar", "La cantidad de calles cercanas", "La decisión depende de cuán frágil es el ambiente y cuánto uso resiste."),
    ],
    ctx=("abc", "Una comuna ficticia tiene una laguna frágil y un barrio sin áreas verdes. Hay recursos para un solo proyecto. ¿Qué enfoque es más coherente con la justicia socioespacial?", "Evaluar cuál sector soporta mayores carencias o riesgos y cómo proteger la laguna a la vez", "Elegir el proyecto más barato", "Elegir el sector con más votos en redes", "La justicia pide mirar necesidades y riesgos de cada sector, sin dejar de proteger el ambiente."),
    sc=[
        ("En Geografía: ¿qué es la conservación?", "Proteger un ambiente permitiendo un uso racional que asegure su permanencia", "Admite usos con reglas, a diferencia de la preservación."),
        ("¿Qué es la justicia socioespacial?", "El reparto justo de beneficios y cargas del territorio entre los grupos", "Se pregunta quién recibe parques y servicios y quién carga con riesgos."),
        ("¿Qué criterio limita el uso de un ambiente al mínimo?", "La preservación", "Mantiene el ambiente sin intervención o casi."),
    ],
    op=("Lee este caso ficticio: una comuna tiene una duna costera frágil, un bosque de pino plantado y un barrio sin plaza ni paradero. Hay tres propuestas: cerrar la duna al público, abrir senderos con reglas en el bosque y construir una plaza y un paradero en el barrio. "
        "Para cada propuesta escribe qué criterio prioriza (preservación, conservación o justicia socioespacial), qué actor la defendería y qué evidencia pedirías.",
        "Cerrar la duna: preservación; defendería una ONG ambiental; pediría un estudio de fragilidad. Senderos en el bosque: conservación; defendería una agrupación de excursionistas; pediría datos de visitas. Plaza y paradero: justicia socioespacial; defenderían los vecinos; pediría un catastro de servicios.",
        ["asocia cada propuesta con el criterio correcto", "nombra un actor plausible por propuesta", "propone una evidencia pertinente por propuesta", "no declara ganadora a ninguna sin razón"],
        ["tabla de tres filas con criterio, actor y evidencia"],
        ["confundir preservación con conservación", "elegir una evidencia que no sirve para el criterio", "ignorar al barrio"],
        "Pregunta: «¿prohíbe o regula el uso?». Si no responde, pídele que relea las dos definiciones."),
    reinforce="Elige un espacio natural cercano a tu casa y escribe si sería más adecuado preservarlo o conservarlo con uso regulado, y por qué.",
    extend="Conversa con alguien de tu comunidad sobre un espacio natural que se cuida y anota qué reglas existen y quién las hace cumplir.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (dos propuestas ficticias de expansión de Villa Alta). Propuesta X: construir 200 viviendas en la zona inundable del estero (columna 4, filas 3 y 4), con suelo barato y cerca de la ruta principal. "
     "Propuesta Y: densificar el centro con edificios de baja altura sobre sitios sin uso y proteger el estero como parque inundable que recibe el agua en invierno. "
     "Cadena de efectos de X: se pavimenta el borde del estero, el agua no se absorbe, aumenta el anegamiento en invierno y se necesitan obras de defensa costosas.")
build(
    O4, 4, F,
    use="Aprenderé a explicar cómo la reducción de riesgos y la sustentabilidad ambiental se relacionan con la ubicación de viviendas y servicios, y qué consecuencias tiene planificar sin considerar esos criterios.",
    prior=["Distingo conservación y preservación.", "Reconozco accesibilidad y conectividad.", "Sé seguir cadenas de efectos."],
    explain=[
        "La reducción de riesgos es el criterio según el cual el territorio debe organizarse para disminuir la probabilidad de daño por fenómenos como inundaciones, aluviones, sismos o incendios. Una forma de lograrlo es no ubicar viviendas ni servicios críticos en zonas de amenaza. Otra es proteger los espacios que absorben el agua, como los humedales y los esteros, que actúan como defensas naturales.",
        "La sustentabilidad ambiental es el criterio según el cual se satisfacen las necesidades presentes sin comprometer las de las generaciones futuras. En planificación significa usar el suelo y el agua de modo que el ambiente pueda regenerarse. Una ciudad que se expande sobre zonas inundables o sobre suelos agrícolas puede resolver una necesidad hoy y crear riesgos y costos mañana.",
        "Estos criterios se relacionan con otros. Concentrar la vivienda en terrenos bien conectados (densificar) puede mejorar la accesibilidad y reducir la presión sobre el ambiente, pero exige cuidar la calidad de vida y las áreas verdes. Ubicar a las personas más pobres en los terrenos más baratos y más riesgosos genera injusticia socioespacial. Evaluar es seguir esas relaciones: qué ganan y qué pierden los actores y el ambiente con cada propuesta.",
    ],
    vocab=[("reducción de riesgos", "organizar el territorio para disminuir el daño posible por un fenómeno"), ("sustentabilidad ambiental", "satisfacer necesidades presentes sin comprometer las de las generaciones futuras"), ("zona de amenaza", "área expuesta a un fenómeno que puede causar daño"), ("densificar", "concentrar más viviendas en una superficie ya urbanizada"), ("defensa natural", "ambiente que reduce el daño, como un humedal que absorbe agua")],
    worked=[
        ("Relacionar una decisión con el riesgo", "Una comuna ficticia pavimenta el borde de un humedal que absorbía agua de lluvia. ¿Qué efecto tiene sobre el riesgo?",
         ["El suelo pavimentado absorbe menos agua.", "El agua queda en la superficie y aumenta el anegamiento."],
         "Aumenta el riesgo de anegamiento"),
        ("Evaluar sustentabilidad", "Una ciudad ficticia se expande sobre suelo agrícola. ¿Qué pregunta de sustentabilidad ambiental conviene hacer?",
         ["Pregunta qué se pierde: el suelo que alimenta.", "Pregunta si las generaciones futuras podrán recuperarlo."],
         "¿Se compromete la capacidad futura de producir alimentos?"),
    ],
    mistakes=[("Creer que construir donde el suelo es barato siempre es un ahorro.", "No se cuentan los costos de las obras de defensa ni los daños posteriores.", "Suma el costo del suelo y el costo del riesgo y de las obras."),
              ("Pensar que proteger el ambiente y construir viviendas son objetivos opuestos.", "Se mira cada decisión por separado.", "Busca alternativas que combinen viviendas bien ubicadas con ambientes protegidos.")],
    T=[
        ("abc", "{F} ¿Dónde ubica la propuesta X las 200 viviendas?", "En la zona inundable del estero", "En el centro sobre sitios sin uso", "Sobre el cerro de bosque nativo", "La propuesta X construye en la zona inundable del estero."),
        ("abc", "{F} ¿Qué propone la propuesta Y para el estero?", "Protegerlo como parque inundable", "Pavimentarlo", "Rellenarlo", "La propuesta Y protege el estero como parque inundable."),
        ("En Geografía: ¿cómo se llama el criterio de organizar el territorio para disminuir el daño posible por un fenómeno?", "Reducción de riesgos", "Esa es la definición del criterio de reducción de riesgos."),
        ("abc", "{F} ¿Qué efecto de la propuesta X aumenta el riesgo en invierno?", "El agua no se absorbe y se acumula", "El agua se absorbe mejor", "Hay menos viviendas", "Al pavimentar, el agua se acumula en la superficie."),
        ("abc", "{F} ¿Qué es un parque inundable?", "Un espacio que recibe agua en invierno y la absorbe", "Un parque que siempre está seco", "Un parque cerrado para siempre", "Funciona como defensa natural que recibe y absorbe el agua."),
        ("abc", "¿Qué significa densificar?", "Concentrar más viviendas en una superficie ya urbanizada", "Expandir la ciudad sobre el campo", "Eliminar las viviendas", "Densificar es construir más compacto sobre suelo ya urbanizado."),
        ("abc", "{F} ¿Qué criterio mejora más la propuesta Y respecto de la X?", "La reducción de riesgos", "Solo el costo del suelo", "Nada", "Evita viviendas en zona de amenaza y protege una defensa natural."),
        ("abc", "{F} Un concejal dice: «La propuesta X es mejor porque el suelo es barato». ¿Qué falta en su análisis?", "El costo de las obras de defensa y de los daños por anegamiento", "El nombre del estero", "La cantidad de concejales de la comuna", "El ahorro inicial puede ser menor que los costos posteriores."),
        ("abc", "{F} Si las viviendas de X son para familias de bajos ingresos, ¿qué problema de justicia socioespacial aparece?", "Quedarían ubicadas en el terreno más riesgoso", "No tendrían techo", "Estarían demasiado cerca del centro", "Si la vivienda barata se ubica en zona riesgosa, la carga recae en quienes tienen menos recursos."),
        ("{F} Explica una ventaja de Y para la accesibilidad y una condición para que no empeore la calidad de vida.", "Acerca a las personas al centro y sus servicios; debe cuidar áreas verdes y cantidad de personas por edificio", "Densificar acerca a los servicios, pero exige mantener espacios verdes y buena calidad de vida."),
        ("abc", "{F} Un estudiante dice: «Proteger el estero significa no construir viviendas». ¿Qué corrección es más precisa?", "Significa construir viviendas en terrenos adecuados, como el centro, y proteger el estero", "Es verdad: no se puede construir nada", "No tiene relación con las viviendas", "La propuesta Y muestra que se puede construir en otros terrenos y proteger el estero."),
        ("abc", "{F} ¿Qué evidencia ayudaría a comparar X e Y?", "Un estudio de zonas inundables y de la capacidad del centro para recibir viviendas", "Una votación sin información", "Cuántos concejales viven cerca del estero", "La comparación necesita datos del riesgo y de la capacidad de cada terreno."),
        ("abc", "{F} Si se construye X y falla la defensa, ¿qué tipo de consecuencia sería?", "Una consecuencia grave y difícil de revertir para los habitantes", "Un efecto positivo", "Un efecto sin relación con la planificación", "Un daño por inundación en viviendas es grave y no fácilmente reversible."),
    ],
    ctx=("abc", "Una comuna ficticia debe ubicar un nuevo consultorio. Una opción está en una quebrada con riesgo de aluvión y otra en un terreno plano alejado de las quebradas. ¿Qué criterio decide?", "La reducción de riesgos, porque un servicio de salud debe poder funcionar en una emergencia", "El menor costo del terreno", "El nombre de la calle", "Un servicio esencial no debe ubicarse en una zona de amenaza."),
    sc=[
        ("En Geografía: ¿qué es la sustentabilidad ambiental?", "Satisfacer necesidades presentes sin comprometer las de las generaciones futuras", "Busca usar los recursos sin agotar su capacidad de regenerarse."),
        ("¿Qué es una zona de amenaza?", "Un área expuesta a un fenómeno que puede causar daño", "Por ejemplo, una zona inundable o una ladera con aluviones."),
        ("¿Por qué un humedal puede ser una defensa natural?", "Porque absorbe agua y reduce el daño por anegamiento", "Recibe agua en invierno y la libera lentamente."),
    ],
    op=("Elige un caso ficticio: (1) una comuna costera quiere ubicar casas cerca de una duna que protege de las marejadas; (2) una comuna de valle quiere construir sobre terrenos agrícolas fértiles. Para el caso elegido escribe una propuesta de ubicación que reduzca el riesgo, una cadena de al menos tres efectos de la decisión menos adecuada, un beneficio y un costo para dos actores distintos, y qué criterio de la asignatura aplicas en cada paso.",
        "Duna. Propuesta: casas detrás de la duna y paseo peatonal por el borde. Cadena de la peor decisión: casas en la duna, duna dañada, marejadas llegan a las casas. Beneficio: vecinos con vista; costo: familias con daños. Criterios: reducción de riesgos, sustentabilidad.",
        ["propone una ubicación que reduce el riesgo", "la cadena de efectos tiene al menos tres pasos coherentes", "nombra beneficio y costo para dos actores", "aplica criterios de la asignatura"],
        ["propuesta, cadena de tres efectos y tabla de dos actores"],
        ["decir que el suelo barato siempre conviene", "olvidar un actor perjudicado", "no nombrar el criterio aplicado"],
        "Pregunta: «¿qué se pierde si la peor decisión falla?». Si no lo dice, pídele que sume los costos de las consecuencias."),
    reinforce="Observa tu barrio y anota un lugar donde se acumula agua en invierno y qué cambio lo explicaría.",
    extend="Pregunta en tu municipalidad o en tu colegio si hay un plano de zonas de riesgo y anota qué zonas aparecen.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 5 (matriz de ejemplo, ficticia). Tres alternativas para el crecimiento de Villa Alta: 1) expandir hacia el estero; 2) densificar el centro y proteger el estero; 3) alternativa mixta con parque lineal en el estero y transporte nuevo a Los Aromos. "
     "Puntajes de 0 a 2, de ejemplo, en el orden de las alternativas 1, 2 y 3. Accesibilidad: 2, 2, 2. Conectividad: 2, 1, 2. Conservación: 0, 1, 1. Preservación: 0, 2, 1. Reducción de riesgos: 0, 2, 2. Sustentabilidad ambiental: 1, 2, 2. Justicia socioespacial: 0, 1, 2.")
build(
    O4, 5, F,
    use="Aprenderé a evaluar alternativas de organización territorial con los siete criterios de la asignatura, a leer puntajes con prudencia y a justificar una recomendación con evidencia y con límites.",
    prior=["Conozco los siete criterios.", "Sé usar una matriz de decisión.", "Distingo costos y beneficios por actor."],
    explain=[
        "Evaluar la organización territorial y ambiental es juzgar una alternativa con criterios explícitos. En esta asignatura se usan siete: accesibilidad (llegar a los servicios), conectividad (enlace por vías y transporte), conservación (proteger con uso regulado), preservación (proteger sin intervención), reducción de riesgos (disminuir el daño posible), sustentabilidad ambiental (cuidar el ambiente para el futuro) y justicia socioespacial (repartir de forma justa beneficios y cargas).",
        "Una matriz de puntajes ayuda a comparar, pero hay que leerla con cuidado. Algunos criterios pueden chocar entre sí: lo que mejora la preservación puede limitar la accesibilidad. El puntaje total depende de los pesos que se den, y esos pesos son decisiones de valores. Un puntaje bajo en un criterio no siempre se compensa con altos puntajes en otros: si una alternativa pone vidas en riesgo, ese costo puede ser inaceptable aunque sume mucho en otros criterios.",
        "Una buena evaluación termina con una recomendación fundamentada: qué alternativa se elige, con qué criterios y datos, qué costos reconoce, qué medidas de mitigación propone y qué evidencia falta. También se pregunta quiénes participaron en la decisión y quiénes no fueron consultados. Recomendar no es decretar: es argumentar con los criterios a la vista.",
    ],
    vocab=[("criterio", "aspecto con que se juzga una alternativa"), ("puntaje total", "suma de los puntajes de una alternativa en todos los criterios"), ("compensación", "ganar en un criterio lo que se pierde en otro"), ("recomendación fundamentada", "elección justificada con criterios, datos y límites"), ("límite de una evaluación", "aspecto que la evaluación no pudo medir")],
    worked=[
        ("Sumar los puntajes", "Una alternativa ficticia obtiene en siete criterios 2, 1, 1, 0, 2, 2 y 1. ¿Cuál es su total?",
         ["Suma los siete puntajes.", "2 + 1 + 1 + 0 + 2 + 2 + 1 = 9."],
         "9 puntos"),
        ("Revisar un criterio inaceptable", "Una alternativa ficticia suma 12 puntos de 14, pero obtiene 0 en reducción de riesgos y pone viviendas en una zona de aluvión. ¿Qué conviene concluir?",
         ["El total alto no compensa un riesgo grave para las personas.", "Hay que revisar la alternativa o agregar medidas."],
         "No recomendarla sin cambios que reduzcan el riesgo"),
    ],
    mistakes=[("Elegir siempre la alternativa con el puntaje total más alto.", "Se olvida que el total depende de los pesos y que algunos costos no se compensan.", "Mira el total, los puntajes bajos y los criterios críticos."),
              ("Presentar la recomendación sin decir qué falta saber.", "Se esconden los límites de la evaluación.", "Declara qué evidencia falta y qué medidas propones.")],
    T=[
        ("abc", "{F} ¿Qué alternativa obtiene 0 en reducción de riesgos?", "La alternativa 1", "La alternativa 2", "La alternativa 3", "La ficha asigna 0 a la alternativa 1 en reducción de riesgos."),
        ("En Geografía: ¿cómo se llama ganar en un criterio lo que se pierde en otro?", "Compensación", "Esa es la definición de compensación en una evaluación."),
        ("=", "{F} ¿Cuál es el puntaje total de la alternativa 1 en los siete criterios?", "2+2+0+0+0+1+0", "Se suman accesibilidad 2, conectividad 2, conservación 0, preservación 0, riesgos 0, sustentabilidad 1 y justicia 0.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de la alternativa 2?", "2+1+1+2+2+2+1", "Se suman los siete puntajes de la alternativa 2 en el orden de la ficha.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de la alternativa 3?", "2+2+1+1+2+2+2", "Se suman los siete puntajes de la alternativa 3 en el orden de la ficha.", " puntos"),
        ("abc", "{F} Según los totales, ¿qué alternativa obtiene el puntaje más alto?", "La alternativa 3", "La alternativa 1", "La alternativa 2", "Los totales son 5, 11 y 12, y el mayor corresponde a la alternativa 3."),
        ("abc", "{F} ¿En qué criterio la alternativa 2 supera a la alternativa 3?", "En preservación", "En conectividad", "En justicia socioespacial", "La alternativa 2 tiene 2 en preservación y la 3 tiene 1."),
        ("abc", "{F} ¿Qué criterio explica que la alternativa 3 sea mejor que la 2 en justicia socioespacial?", "Mejora el transporte hacia Los Aromos, el sector menos conectado", "Elimina todas las áreas verdes", "Permite construir en el estero", "La alternativa 3 incluye transporte hacia el sector con menor conectividad."),
        ("abc", "{F} La alternativa 1 suma pocos puntos y pone viviendas en zona inundable. ¿Qué conclusión es más sólida?", "No conviene recomendarla sin medidas que reduzcan el riesgo", "Conviene aprobarla por ser barata", "Conviene aprobarla porque es rápida", "Un 0 en reducción de riesgos es una carga grave sobre las personas."),
        ("abc", "{F} Un estudiante dice: «La diferencia entre 11 y 12 puntos es pequeña, así que elijo cualquiera». ¿Qué conviene responder?", "Revisar los criterios críticos, los pesos y a qué actores favorece o perjudica cada una", "Que lo decida el azar", "Que no se puede decidir", "Una diferencia pequeña obliga a mirar los criterios que importan más y los actores afectados."),
        ("{F} Propón una medida de mitigación para la alternativa 3 si el transporte nuevo aumentara el ruido en Los Aromos.", "Instalar pantallas acústicas o reordenar los horarios de los buses para reducir el ruido", "Una medida de mitigación reduce el daño de una decisión sin eliminar sus beneficios."),
        ("abc", "{F} ¿Qué evidencia falta para fundamentar mejor la recomendación?", "Costos de las obras y opinión de los vecinos de cada sector", "La opinión de una sola persona que apoya la alternativa 3", "El puntaje total de otra comuna distinta", "Costos y participación son evidencias que cambian la recomendación."),
        ("abc", "{F} ¿Qué estructura tiene una recomendación fundamentada?", "Alternativa elegida, criterios y datos, costos reconocidos, mitigaciones y evidencia faltante", "Solo el nombre de la alternativa", "Una opinión personal sin datos", "Una recomendación se sostiene en criterios, datos y límites explícitos."),
    ],
    ctx=("abc", "Un consejo regional ficticio debe elegir entre una carretera nueva por una cuenca frágil y una mejora del camino actual. La nueva suma 10 puntos y la mejora 9, pero la nueva obtiene 0 en sustentabilidad. ¿Qué conviene?", "Analizar qué significa ese 0 y qué medidas cambiarían el resultado antes de decidir", "Elegir la nueva por tener más puntos", "Elegir la mejora sin analizar", "Un puntaje crítico bajo debe discutirse aunque el total sea más alto."),
    sc=[
        ("En Geografía: ¿cuáles son los siete criterios de evaluación de la organización territorial?", "Accesibilidad, conectividad, conservación, preservación, reducción de riesgos, sustentabilidad ambiental y justicia socioespacial", "Los siete se usan para juzgar una alternativa de planificación."),
        ("¿Basta el puntaje total más alto para decidir?", "No", "Hay que mirar los criterios críticos y los pesos."),
        ("¿Qué incluye una recomendación fundamentada?", "Criterios, datos, costos, mitigaciones y evidencia faltante", "Debe mostrar cómo y con qué límites se llega a la decisión."),
    ],
    op=("Usa esta matriz ficticia para una comuna que debe decidir cómo usar un terreno: alternativas 1) conjunto de viviendas, 2) parque con humedal, 3) mezcla de viviendas pequeñas y parque. Puntajes de 0 a 2 en el orden de las alternativas. Accesibilidad: 2, 1, 2. Conectividad: 2, 1, 2. Conservación: 0, 2, 1. Preservación: 0, 2, 1. Reducción de riesgos: 1, 2, 2. Sustentabilidad ambiental: 1, 2, 2. Justicia socioespacial: 1, 1, 2. "
        "Calcula los totales, elige una alternativa y escribe una recomendación con criterios, un costo que reconoces, una mitigación y una evidencia que falta.",
        "Totales: 1) 2+2+0+0+1+1+1 = 7; 2) 1+1+2+2+2+2+1 = 11; 3) 2+2+1+1+2+2+2 = 12. Recomiendo la 3: mejor justicia y accesibilidad. Costo: menos conservación que la 2. Mitigación: franja del humedal protegida. Evidencia: estudio de riesgo.",
        ["calcula bien los tres totales", "elige una alternativa y la justifica con criterios", "reconoce un costo y propone una mitigación", "indica una evidencia faltante"],
        ["tabla con tres totales y una recomendación de cinco líneas"],
        ["sumar mal los puntajes", "elegir sin justificar", "no reconocer ningún costo"],
        "Pregunta: «¿qué criterio pierde la alternativa que elegiste?». Si no lo nombra, pídele que compare filas."),
    reinforce="Haz una matriz con dos alternativas para el uso de un espacio de tu colegio, con tres criterios de la asignatura y puntajes del 0 al 2.",
    extend="Cambia los pesos de tu matriz y anota si la alternativa elegida cambia; explica por qué.",
)

# ============================================================ OAC-04, clase 6
F = ("Ficha 6 (borradores de conclusión, ficticios). Tres estudiantes concluyen sobre el crecimiento de Villa Alta. Estudiante 1: «Villa Alta debe crecer, porque necesita viviendas.» "
     "Estudiante 2: «En Villa Alta, comuna ficticia de 4.500 habitantes organizada con un plan regulador comunal, la alternativa 3 es la más adecuada porque mejora la accesibilidad y la conectividad de Los Aromos y reduce el riesgo del estero, aunque requiere obras de transporte cuyo costo falta estimar.» "
     "Estudiante 3: «Todas las comunas de Chile deberían densificar sus centros.»")
build(
    O4, 6, F,
    use="Aprenderé a comunicar una conclusión situada: una afirmación fundamentada que indica el lugar, la escala, los actores, los criterios y los datos, y que reconoce sus límites.",
    prior=["Sé evaluar alternativas con criterios.", "Puedo calcular totales y porcentajes.", "Distingo conclusiones prudentes de generalizaciones."],
    explain=[
        "Una conclusión situada es una afirmación que responde a la pregunta de investigación indicando dónde (el lugar y la escala), quiénes (los actores), con qué criterios y con qué datos. «Situada» significa que no pretende valer para todos los lugares: reconoce que depende del contexto estudiado. Una conclusión como «todas las comunas deberían densificar» generaliza sin evidencia; «en Villa Alta, la alternativa 3 es la más adecuada» queda anclada al caso.",
        "Una buena conclusión tiene partes: la tesis (qué se afirma), el lugar y la escala, los criterios aplicados, la evidencia (cifras, mapas, testimonios), las perspectivas de los actores, los límites (qué no se pudo medir) y una recomendación. Cada parte responde una pregunta: qué, dónde, con qué criterio, con qué datos, quién gana o pierde y qué falta. Es mejor decir menos y respaldarlo que decir mucho sin respaldo.",
        "Comunicar también tiene forma: ordenar la información, usar términos geográficos con precisión, indicar las fuentes y escribir con frases claras. Un mapa o una tabla bien rotulados ayudan, pero no reemplazan la redacción. Se evita presentar la propia opinión como si fuera un dato, y se invita a otros a revisar la evidencia.",
    ],
    vocab=[("conclusión situada", "afirmación fundamentada que indica lugar, escala, actores, criterios, datos y límites"), ("tesis", "afirmación principal que se defiende"), ("evidencia", "dato, mapa o testimonio que respalda una afirmación"), ("generalizar", "extender sin evidencia lo observado en un caso a todos los casos"), ("límite", "aquello que no se pudo medir o comprobar")],
    worked=[
        ("Detectar lo que falta", "Una estudiante escribe: «El puerto debe ampliarse». ¿Qué le falta para ser una conclusión situada?",
         ["No indica lugar ni escala.", "No dice criterios, datos ni límites."],
         "Lugar, escala, criterios, datos y límites"),
        ("Reescribir una conclusión", "Reescribe «Hay que proteger los humedales» para un caso ficticio con datos: un humedal de 60 hectáreas en una comuna que perdió 15.",
         ["Agrega lugar y escala: un humedal comunal.", "Agrega dato: 15 de 60 hectáreas perdidas (25 %) y criterio: preservación y reducción de riesgos."],
         "En el humedal comunal, que perdió 15 de 60 hectáreas (25 %), conviene preservar lo que queda por su rol en reducir riesgos, aunque falta medir el efecto en las aves"),
    ],
    mistakes=[("Generalizar la conclusión de un caso a todo el país.", "Se olvida que la conclusión depende del contexto.", "Indica el lugar y la escala, y limita lo que afirmas a ese caso."),
              ("Escribir una opinión sin evidencia.", "Se confunde conclusión con preferencia personal.", "Respalda cada afirmación con un dato, un mapa o un testimonio.")],
    T=[
        ("abc", "{F} ¿Qué estudiante ubica su conclusión en un lugar y una escala?", "El estudiante 2", "El estudiante 1", "El estudiante 3", "El estudiante 2 comienza con «En Villa Alta, comuna ficticia de 4.500 habitantes»."),
        ("En Geografía: ¿cómo se llama la afirmación principal que se defiende en una conclusión?", "Tesis", "La tesis es la afirmación principal que se defiende."),
        ("abc", "{F} ¿Qué estudiante generaliza a todo el país?", "El estudiante 3", "El estudiante 1", "El estudiante 2", "El estudiante 3 dice «todas las comunas de Chile»."),
        ("abc", "{F} ¿Qué falta en la conclusión del estudiante 1?", "Criterios, datos, lugar y límites", "Solo el nombre de la comuna", "Nada, está completa", "Dice «debe crecer» sin criterios, datos ni límites."),
        ("abc", "{F} ¿Qué límite reconoce el estudiante 2?", "Que el costo de las obras de transporte falta estimar", "Que no se conocen las perspectivas de los vecinos", "Que la comuna es demasiado pequeña para planificar", "Declara que falta estimar el costo de las obras."),
        ("abc", "{F} ¿Qué criterios aplica el estudiante 2?", "Accesibilidad, conectividad y reducción de riesgos", "Solo el costo del suelo", "Solo la belleza del paisaje", "Nombra la mejora de accesibilidad y conectividad y la reducción del riesgo."),
        ("abc", "¿Qué significa que una conclusión sea situada?", "Que indica el lugar, la escala y el contexto en que vale", "Que vale para todos los lugares", "Que no necesita datos", "Una conclusión situada reconoce que depende del contexto estudiado."),
        ("abc", "{F} El estudiante 2 escribe «comuna ficticia de 4.500 habitantes». ¿Para qué sirve ese dato en su conclusión?", "Para indicar el tamaño del caso y situar la conclusión en ese lugar", "Para probar que todas las comunas tienen esa población", "Para reemplazar los criterios de evaluación", "El dato describe el caso estudiado y ayuda a ubicar hasta dónde vale la conclusión."),
        ("abc", "Una estudiante concluye sobre su comuna ficticia: «Los datos muestran que el 25 % del humedal se perdió, pero no sabemos la causa». ¿Qué parte de una conclusión situada incluye al final?", "Un límite de la evidencia", "Una generalización", "Una opinión sin datos", "Reconoce lo que no se pudo comprobar, que es el límite."),
        ("abc", "{F} ¿Qué cambio mejora la conclusión del estudiante 3?", "Limitarla a un caso y agregar criterios y datos", "Agregar más países", "Eliminar toda cifra", "Situar el lugar y respaldar con evidencia vuelve la conclusión comprobable."),
        ("{F} Reescribe la conclusión del estudiante 1 agregando lugar y un criterio.", "En Villa Alta, la comuna debe crecer en terrenos bien conectados y fuera del estero inundable, aplicando los criterios de accesibilidad y de reducción de riesgos", "Debe nombrar el lugar y aplicar al menos un criterio de la asignatura."),
        ("abc", "{F} ¿Qué recomendación es más prudente?", "Adoptar la alternativa 3 y estimar antes el costo de las obras de transporte", "Adoptar la alternativa 3 sin mirar costos", "No hacer nada nunca", "Una recomendación prudente reconoce los límites y propone cómo cubrirlos."),
        ("abc", "Un informe incluye un mapa sin título, sin escala y sin fuente. ¿Qué problema comunica?", "No permite saber qué muestra ni de dónde provienen sus datos", "Muestra más información que un mapa completo", "Es más claro porque tiene menos texto", "Un mapa necesita título, escala y fuente para ser evidencia."),
    ],
    ctx=("abc", "Un grupo de estudiantes ficticios presenta ante un concejo comunal un informe sobre el uso de una plaza. ¿Qué cierre es más adecuado?", "Una conclusión con lugar, criterios, datos, perspectivas, límites y recomendación", "Una frase que dice que todo está bien", "Una opinión personal sin datos", "El concejo necesita una conclusión situada y respaldada."),
    sc=[
        ("En Geografía: ¿qué es una conclusión situada?", "Una afirmación fundamentada que indica lugar, escala, actores, criterios, datos y límites", "No generaliza más allá del caso estudiado."),
        ("¿Qué significa generalizar?", "Extender sin evidencia lo observado en un caso a todos los casos", "Es un error frecuente en las conclusiones."),
        ("¿Para qué sirve declarar los límites?", "Para decir qué no se pudo medir ni comprobar", "Así otros pueden revisar y completar la evidencia."),
    ],
    op=("Elige uno de estos casos ficticios: (1) en la comuna de Puerto Claro, 2.000 habitantes, la costanera quedó dañada tras un temporal y se propone reconstruirla igual o mover las casas; (2) en la comuna de Valle Sur, 3.000 habitantes, se propone ampliar el vertedero o cerrar y llevar los residuos a otra comuna. "
        "Escribe una conclusión situada de cinco o seis líneas con tesis, lugar y escala, dos criterios de la asignatura, una cifra o un dato, la perspectiva de un actor, un límite y una recomendación.",
        "En Puerto Claro, comuna de 2.000 habitantes, conviene mover las casas más expuestas, porque la reducción de riesgos pesa más que la accesibilidad al borde. Según el informe de ejemplo, 300 personas viven en la franja dañada. Los vecinos temen perder su barrio. Límite: falta estimar costos. Recomiendo un estudio de terrenos.",
        ["incluye tesis, lugar y escala", "aplica dos criterios de la asignatura", "usa al menos un dato o cifra", "reconoce un límite y formula una recomendación"],
        ["texto de cinco o seis líneas"],
        ["generalizar a otras comunas", "no incluir ningún límite", "presentar una opinión como dato"],
        "Pregunta: «¿qué parte de tu texto puede revisar otra persona con datos?». Si ninguna, pídele que agregue una cifra."),
    reinforce="Elige una noticia local y escribe una conclusión situada de tres líneas con lugar, un dato y un límite.",
    extend="Intercambia tu conclusión con un compañero y anota qué parte (tesis, lugar, criterios, datos, límite) le falta a cada una.",
)

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (caso ficticio). Una lluvia intensa e inusual cae sobre la comuna de Quebrada Seca, que tiene dos barrios junto a una quebrada normalmente seca. Villa Cauce: 80 viviendas construidas dentro del cauce, una sola salida a pie hacia el cerro, sin alarma ni señalética. "
     "Barrio Alto: 80 viviendas fuera del cauce, tres salidas hacia zonas altas, alarma comunitaria y simulacros todos los años. La lluvia hace bajar un aluvión (flujo de agua, barro y piedras) por la quebrada. Resultado de ejemplo: 60 viviendas dañadas en Villa Cauce y 4 en Barrio Alto.")
build(
    O5, 1, F,
    use="Aprenderé a explicar por qué el riesgo de desastres tiene carácter social: depende de la amenaza natural y también de la exposición, la vulnerabilidad y la capacidad de las comunidades, que se relacionan con los usos del espacio.",
    prior=["Conozco las dinámicas físico-naturales de Chile.", "Sé que las decisiones sobre el espacio tienen consecuencias.", "Distingo causas naturales y sociales."],
    explain=[
        "Chile tiene una geografía con muchas amenazas: está en un borde de placas tectónicas (sismos, tsunamis y volcanes), tiene cordilleras con fuertes pendientes (aluviones y deslizamientos), climas muy variados (sequías, inundaciones, incendios forestales) y una costa muy larga. Una amenaza es un fenómeno natural que puede causar daño. Pero una amenaza por sí sola no es un desastre: el desastre ocurre cuando ese fenómeno supera la capacidad de una comunidad para resistirlo.",
        "El riesgo depende de cuatro elementos. La amenaza es el fenómeno que puede ocurrir. La exposición es que personas, viviendas e infraestructura se encuentren en el lugar donde puede ocurrir. La vulnerabilidad son las condiciones que hacen más probable el daño: viviendas mal ubicadas, falta de alarma, pocas vías de salida, pobreza, falta de información. La capacidad son los recursos y la preparación para enfrentar el fenómeno. A mayor amenaza, exposición y vulnerabilidad, y a menor capacidad, mayor riesgo.",
        "Por eso se dice que el riesgo tiene carácter social: se construye por cómo se usa el espacio, dónde se permite construir, quién puede elegir dónde vivir y qué se prepara. Dos barrios con la misma lluvia pueden sufrir daños muy distintos. Hablar de «desastre natural» puede ocultar estas decisiones: la amenaza es natural, pero el desastre se explica también por factores sociales, territoriales y ambientales.",
    ],
    vocab=[("amenaza", "fenómeno natural que puede causar daño"), ("exposición", "presencia de personas y bienes en el lugar donde puede ocurrir la amenaza"), ("vulnerabilidad", "condiciones que hacen más probable el daño"), ("capacidad", "recursos y preparación para enfrentar un fenómeno"), ("desastre", "situación en que el fenómeno supera la capacidad de la comunidad")],
    worked=[
        ("Reconocer los elementos del riesgo", "Un pueblo ficticio tiene casas al pie de un volcán activo y no tiene ruta de evacuación. ¿Qué elementos del riesgo aparecen?",
         ["El volcán activo es la amenaza.", "Las casas cercanas son la exposición y la falta de ruta es vulnerabilidad."],
         "Amenaza (volcán), exposición (casas cercanas) y vulnerabilidad (sin ruta)"),
        ("Distinguir amenaza y desastre", "Un temblor fuerte ocurre en dos ciudades ficticias. Una sufre pocos daños y la otra muchos. ¿Qué explica la diferencia?",
         ["La amenaza es la misma en las dos ciudades.", "La diferencia está en cómo se construyó y qué tan preparadas estaban."],
         "Diferencias de exposición, vulnerabilidad y capacidad, no de la amenaza"),
    ],
    mistakes=[("Hablar de «desastre natural» como si solo dependiera de la naturaleza.", "Se confunde la amenaza con el desastre.", "Distingue la amenaza natural de los factores sociales que explican el daño."),
              ("Culpar a las personas afectadas por vivir en una zona de amenaza.", "Se ignora que muchas veces no tienen alternativas de vivienda.", "Pregunta qué condiciones sociales llevaron a esa ubicación.")],
    T=[
        ("abc", "{F} ¿Qué fenómeno natural bajó por la quebrada?", "Un aluvión", "Un tsunami", "Una erupción", "La ficha dice que la lluvia hizo bajar un aluvión por la quebrada."),
        ("En Geografía: ¿cómo se llama el fenómeno natural que puede causar daño, como un aluvión o un sismo?", "Amenaza", "Según la explicación, una amenaza es un fenómeno natural que puede causar daño."),
        ("abc", "{F} ¿Qué barrio tenía alarma comunitaria?", "Barrio Alto", "Villa Cauce", "Ninguno de los dos", "La ficha atribuye la alarma comunitaria a Barrio Alto."),
        ("abc", "¿Qué es la vulnerabilidad?", "Las condiciones que hacen más probable el daño, como la falta de alarma o de vías de salida", "El fenómeno natural que ocurre", "La cantidad de lluvia que cae", "La vulnerabilidad es una condición social y territorial que facilita el daño."),
        ("abc", "{F} Ambos barrios recibieron la misma lluvia. ¿Por qué el daño fue distinto?", "Por las diferencias de ubicación, alerta y rutas de salida", "Porque en Villa Cauce llovió más fuerte", "Porque Barrio Alto está más cerca del mar", "La amenaza fue la misma; cambiaron la exposición, la vulnerabilidad y la capacidad."),
        ("abc", "¿Qué es la exposición?", "Que personas y bienes se encuentren donde puede ocurrir la amenaza", "Que el fenómeno sea muy intenso", "Que haya un plan de evacuación", "La exposición se refiere a quiénes y qué están en el área de la amenaza."),
        ("=", "{F} ¿Qué porcentaje de las viviendas de Villa Cauce quedó dañado?", "60*100//80", "Se divide la cantidad de viviendas dañadas entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas viviendas más quedaron dañadas en Villa Cauce que en Barrio Alto?", "60-4", "Se resta el número de viviendas dañadas de Barrio Alto al de Villa Cauce.", " viviendas"),
        ("abc", "En un pueblo ficticio, una ladera inestable amenaza con deslizarse. Las casas de abajo no tienen alarma. ¿Qué elementos del riesgo están presentes?", "Amenaza (ladera), exposición (casas) y vulnerabilidad (sin alarma)", "Solo amenaza", "Solo vulnerabilidad", "La ladera es la amenaza, las casas están expuestas y la falta de alarma agrega vulnerabilidad."),
        ("abc", "{F} Un locutor dice: «Fue un desastre natural». ¿Qué corrección es más precisa?", "La amenaza fue natural, pero el daño depende de cómo se usó el espacio y de la capacidad de la comunidad", "No hubo ninguna causa natural", "La culpa fue solo de los vecinos", "El carácter social del riesgo muestra que el desastre también se construye."),
        ("{F} Explica por qué se dice que el riesgo de desastres tiene carácter social.", "Porque depende de dónde se permite vivir, de cómo se usa el espacio y de lo que la comunidad ha preparado", "Los factores sociales y territoriales determinan la exposición, la vulnerabilidad y la capacidad."),
        ("abc", "{F} Una vecina de Villa Cauce construyó en el cauce porque no encontró otro terreno que pudiera pagar. ¿Qué afirmación es más justa?", "La exposición puede deberse a la falta de alternativas de vivienda, no solo a decisiones individuales", "Ella es la única responsable del daño", "El aluvión fue un castigo imprevisible", "El riesgo social depende de las opciones reales de las personas y de las decisiones sobre el territorio."),
        ("abc", "Una comuna ficticia no puede cambiar la intensidad de las lluvias. ¿Qué puede hacer para reducir el riesgo de aluvión?", "Mejorar las alertas y vías de salida, y evitar nuevas viviendas en el cauce", "Esperar a que no llueva", "Culpar a la lluvia", "La comuna actúa sobre exposición, vulnerabilidad y capacidad, que sí dependen de las decisiones."),
    ],
    ctx=("abc", "El consejo vecinal de una población ficticia nota que la quebrada de su sector se llena cuando llueve fuerte. ¿Qué primera pregunta ayuda a evaluar el riesgo?", "¿Cuántas viviendas están en el cauce y cuántas vías de salida tienen?", "¿Cuántas personas visitan la quebrada en verano?", "¿Qué opinan de la quebrada los habitantes de otras regiones?", "Contar viviendas expuestas y vías de salida permite medir la exposición y la capacidad."),
    sc=[
        ("En Geografía: ¿qué es una amenaza?", "Un fenómeno natural que puede causar daño", "Por ejemplo, un sismo, un aluvión o un incendio forestal."),
        ("¿Cuándo ocurre un desastre?", "Cuando el fenómeno supera la capacidad de la comunidad", "Depende del fenómeno y de la capacidad de enfrentarlo."),
        ("¿Qué cuatro elementos determinan el riesgo?", "Amenaza, exposición, vulnerabilidad y capacidad", "Su combinación define cuánto riesgo existe."),
    ],
    op=("Elige un caso ficticio: (1) un pueblo costero con casas en una playa baja y sin señalética de evacuación; (2) un barrio de ladera con casas bajo un cerro desprovisto de árboles y con una sola calle de salida. Escribe la amenaza, la exposición, dos factores de vulnerabilidad, una capacidad que podría fortalecerse y una frase que explique por qué el riesgo tiene carácter social en tu caso.",
        "Barrio de ladera. Amenaza: deslizamiento. Exposición: casas bajo el cerro. Vulnerabilidad: sin árboles y una sola calle de salida. Capacidad: organizar simulacros y señalética. El riesgo es social porque se permitió vivir bajo el cerro y no hay alternativas de vivienda.",
        ["distingue amenaza, exposición y vulnerabilidad", "nombra una capacidad que se puede fortalecer", "explica el carácter social del riesgo", "no culpa a las personas afectadas"],
        ["ficha con amenaza, exposición, dos vulnerabilidades, capacidad y explicación"],
        ["llamar «amenaza» a la vulnerabilidad", "culpar a los habitantes", "olvidar la capacidad"],
        "Pregunta: «¿qué decisión humana influye en este riesgo?». Si responde solo con la naturaleza, pídele que relea la explicación."),
    reinforce="Identifica en tu barrio una amenaza posible, qué parte de la gente está expuesta y una condición que aumenta la vulnerabilidad.",
    extend="Averigua con una persona mayor de tu entorno qué fenómeno natural ha afectado tu zona y qué se hizo después para prepararse mejor.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (datos de ejemplo, ficticios) de la comuna de Quebrada Seca. Sector Cauce: 80 viviendas, todas en zona de amenaza alta, 1 vía de evacuación. Sector Lomas: 120 viviendas, 20 en zona de amenaza media, 3 vías de evacuación. Sector Plano: 200 viviendas, ninguna en zona de amenaza, 2 vías de evacuación. "
     "Fuentes: (C) catastro municipal con estos datos; (V) relato de vecinos del sector Cauce: «nadie nos avisó»; (P) folleto de una inmobiliaria que dice «terrenos seguros» para un loteo junto a la quebrada.")
build(
    O5, 2, F,
    use="Aprenderé a interrogar mapas de amenaza, catastros e indicadores de exposición y vulnerabilidad, reconociendo lo que miden y lo que dejan fuera, para describir el riesgo de un territorio.",
    prior=["Conozco amenaza, exposición, vulnerabilidad y capacidad.", "Sé calcular porcentajes.", "Interrogo fuentes por su productor y propósito."],
    explain=[
        "Para estudiar el riesgo se usan mapas de amenaza, que muestran dónde puede ocurrir un fenómeno (por ejemplo, zonas inundables o de aluvión). Un mapa de amenaza no dice cuántas personas viven allí ni qué tan preparadas están: para eso se cruzan con otros datos, como el catastro de viviendas. El cruce de capas de información, como amenaza y población, es la base del análisis espacial del riesgo.",
        "Los indicadores de exposición miden cuántas personas o viviendas están en zona de amenaza. Los de vulnerabilidad miden condiciones como la cantidad de vías de evacuación, la existencia de alarma o el estado de las viviendas. Los de capacidad miden recursos, como simulacros, equipos o acceso a información. Un porcentaje de viviendas expuestas se calcula dividiendo las viviendas en zona de amenaza entre el total y multiplicando por 100.",
        "Como toda fuente, los datos de riesgo tienen límites. Un catastro puede estar desactualizado; un folleto inmobiliario tiene interés comercial; un relato vecinal muestra experiencias reales, pero no es una medición. Además, un indicador puede engañar: tener muchas viviendas por vía de evacuación en un sector sin amenaza no es lo mismo que tenerlas en uno con amenaza alta. Se interpretan los indicadores juntos y en su contexto.",
    ],
    vocab=[("mapa de amenaza", "mapa que muestra dónde puede ocurrir un fenómeno dañino"), ("catastro", "registro de viviendas o bienes de un territorio"), ("vía de evacuación", "ruta para salir de una zona de amenaza hacia un lugar seguro"), ("indicador de exposición", "dato que mide cuántos bienes o personas están en zona de amenaza"), ("cruce de capas", "combinación de dos o más tipos de información sobre un mismo territorio")],
    worked=[
        ("Calcular un porcentaje de viviendas expuestas", "En otro sector ficticio hay 250 viviendas y 50 están en zona de amenaza. ¿Qué porcentaje está expuesto?",
         ["Divide las expuestas entre el total: 50 ÷ 250.", "Multiplica por 100: 20 %."],
         "20 %"),
        ("Leer un indicador con cuidado", "Un sector ficticio tiene 150 viviendas y 3 vías de evacuación, pero la amenaza en ese sector es muy alta. Otro tiene 300 viviendas y 3 vías, pero ninguna amenaza. ¿Cuál es más preocupante?",
         ["El primero tiene 150 ÷ 3 = 50 viviendas por vía y amenaza alta.", "El segundo tiene 100 por vía, pero no tiene amenaza."],
         "El primero, porque combina amenaza alta con exposición"),
    ],
    mistakes=[("Interpretar un indicador sin mirar la amenaza del sector.", "Un indicador de vías o viviendas se interpreta en su contexto.", "Cruza siempre amenaza, exposición, vulnerabilidad y capacidad."),
              ("Aceptar un folleto que dice «terrenos seguros» sin pedir el mapa de amenaza.", "Se confunde un aviso comercial con un estudio técnico.", "Pide el mapa de amenaza y la fuente que respalda la afirmación.")],
    T=[
        ("abc", "{F} ¿Qué sector tiene todas sus viviendas en zona de amenaza alta?", "El sector Cauce", "El sector Lomas", "El sector Plano", "La ficha dice que las 80 viviendas del sector Cauce están en zona de amenaza alta."),
        ("En Geografía: ¿cómo se llama el registro de viviendas o bienes de un territorio?", "Catastro", "Un catastro es el registro de viviendas o bienes de un territorio."),
        ("abc", "{F} ¿Qué fuente de la ficha tiene interés comercial?", "El folleto de la inmobiliaria (P)", "El catastro municipal (C)", "El relato de los vecinos (V)", "El folleto busca vender lotes, por lo que tiene interés comercial."),
        ("=", "{F} ¿Cuántas viviendas de la comuna están en alguna zona de amenaza? Suma las del sector Cauce y las expuestas del sector Lomas.", "80+20", "Se suman las viviendas expuestas de los sectores con amenaza.", " viviendas"),
        ("=", "{F} ¿Cuántas viviendas tiene la comuna en total?", "80+120+200", "Se suman las viviendas de los tres sectores.", " viviendas"),
        ("=", "{F} ¿Qué porcentaje de las viviendas de toda la comuna está en zona de amenaza? Usa 100 viviendas expuestas y 400 en total.", "100*100//400", "Se divide la cantidad de viviendas expuestas entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} El folleto (P) dice «terrenos seguros». ¿Qué conviene pedir?", "El mapa de amenaza y quién lo elaboró", "Más fotografías del loteo", "El precio de los lotes", "Una afirmación sobre seguridad necesita un estudio técnico de amenaza."),
        ("abc", "{F} Los vecinos dicen: «nadie nos avisó». ¿Qué indicador de capacidad podría medirse?", "Si existe una alarma o un sistema de aviso en el sector", "La altura del cerro", "El precio de las viviendas", "Un sistema de alerta es un indicador de capacidad."),
        ("abc", "{F} En el sector Cauce hay 1 vía de evacuación para 80 viviendas. ¿Qué indica ese dato?", "Una vulnerabilidad alta por pocas salidas para muchas viviendas", "Una capacidad alta", "Ausencia de exposición", "Pocas salidas para muchas viviendas es una vulnerabilidad."),
        ("abc", "{F} El sector Plano tiene 200 viviendas y 2 vías, es decir, 100 viviendas por vía. ¿Por qué no es el más preocupante?", "Porque no tiene viviendas en zona de amenaza", "Porque tiene menos vías que Cauce", "Porque tiene la misma cantidad de viviendas que Lomas", "Sin exposición a la amenaza, el número de viviendas por vía no define el riesgo."),
        ("abc", "{F} ¿Qué sector necesita más atención para reducir el riesgo?", "Cauce, porque combina amenaza alta, toda la población expuesta y una sola vía", "Plano, porque tiene más viviendas", "Lomas, porque tiene tres vías", "El riesgo es mayor donde coinciden amenaza, exposición y vulnerabilidad."),
        ("{F} Explica por qué un mapa de amenaza solo no basta para saber el riesgo.", "Porque no dice cuántas personas viven allí ni qué tan preparadas están", "Hay que cruzarlo con exposición, vulnerabilidad y capacidad."),
        ("abc", "{F} Un funcionario dice: «El catastro (C) tiene diez años y no ha cambiado». ¿Qué problema puede tener?", "Podría no reflejar las viviendas nuevas, por lo que subestimaría la exposición", "Que es muy preciso", "Que solo incluye al sector Plano", "Un catastro desactualizado deja fuera viviendas nuevas."),
    ],
    ctx=("abc", "Una familia ficticia quiere comprar un terreno cerca de un río. La vendedora le asegura que es seguro, sin mostrar ningún estudio. ¿Qué conviene hacer?", "Pedir el mapa de amenaza y consultarlo con la municipalidad", "Comprar de inmediato porque la vendedora lo asegura", "Descartar el terreno sin averiguar", "Una afirmación de seguridad debe respaldarse con un estudio técnico."),
    sc=[
        ("En Geografía: ¿qué muestra un mapa de amenaza?", "Dónde puede ocurrir un fenómeno dañino", "No muestra por sí solo cuántas personas viven allí."),
        ("¿Qué mide un indicador de exposición?", "Cuántas personas o viviendas están en zona de amenaza", "Se compara con el total para obtener un porcentaje."),
        ("¿Qué es una vía de evacuación?", "Una ruta para salir de una zona de amenaza hacia un lugar seguro", "Permite el desplazamiento hacia zonas altas o seguras."),
    ],
    op=("Elige un caso ficticio. Caso 1: una población de 300 viviendas, con 90 en zona inundable, 1 vía de salida y una alarma que no funciona; fuentes: catastro municipal y un relato vecinal que dice «el agua llegó rápido». Caso 2: una villa de 500 viviendas, con 100 en zona de incendio forestal, 2 vías de salida y simulacros anuales; fuentes: registro comunal y un folleto de una empresa forestal que dice «bosques seguros». "
        "Calcula el porcentaje de viviendas expuestas, indica un dato de vulnerabilidad y uno de capacidad, interroga una fuente (quién, para qué, qué deja fuera) y escribe una pregunta que haría falta responder para completar el diagnóstico.",
        "Caso 1. Porcentaje: 90 ÷ 300 × 100 = 30 %. Vulnerabilidad: una sola vía. Capacidad: alarma que no funciona. El relato vecinal muestra la experiencia, pero no mide. Pregunta: ¿cuánto tarda en subir el agua?",
        ["calcula bien el porcentaje de viviendas expuestas", "distingue vulnerabilidad y capacidad", "interroga una fuente con quién, para qué y qué deja fuera", "formula una pregunta pertinente"],
        ["ficha con cálculo, dos datos clasificados, interrogación de una fuente y una pregunta"],
        ["dividir por la parte y no por el total", "confundir capacidad con vulnerabilidad", "aceptar el folleto como estudio técnico"],
        "Pregunta: «¿qué dato falta para saber qué tan preparada está la comunidad?». Si no lo identifica, pídele que relea la definición de capacidad."),
    reinforce="Haz una lista con tres indicadores que medirías en tu barrio para conocer su exposición y su vulnerabilidad frente a una amenaza.",
    extend="Pide a tu colegio o junta de vecinos un plano de evacuación y anota las vías, los puntos de reunión y las zonas de amenaza que aparecen.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (versiones ficticias, después del aluvión en Quebrada Seca). Radio local: «Fue un desastre natural imprevisible.» Vecina de Villa Cauce: «Nos dejaron construir en el cauce porque el terreno era barato y no teníamos otro lugar donde vivir.» "
     "Municipalidad: «El plan regulador antiguo no consideraba la quebrada y no hubo fiscalización oportuna de las nuevas viviendas.» Servicio de emergencia: «Hubo menos daño donde había alarma y ruta de evacuación.»")
build(
    O5, 3, F,
    use="Aprenderé a comparar las causas naturales y sociales de un desastre y las perspectivas de distintos actores, sin buscar culpables únicos y reconociendo que las causas de fondo son territoriales y sociales.",
    prior=["Distingo amenaza y desastre.", "Reconozco causas próximas y de fondo.", "Sé separar posición e interés."],
    explain=[
        "Los desastres tienen varias causas. La causa próxima es el fenómeno que los dispara (una lluvia intensa, un sismo). Las causas de fondo son las condiciones previas que hicieron que el fenómeno causara daño: dónde se permitió construir, qué precio tenía el suelo, qué tan bien se fiscalizó, qué información tenía la comunidad y qué opciones de vivienda existían. Muchas veces las personas con menos recursos terminan viviendo en los lugares más expuestos.",
        "Por eso se distinguen las explicaciones. Una explicación solo natural dice «fue imprevisible» y deja fuera las decisiones sobre el uso del espacio. Una explicación solo individual dice «fue culpa de quienes vivían allí» y deja fuera la falta de alternativas. Una explicación territorial y social combina el fenómeno, la ubicación, las normas, la desigualdad y la preparación. Es la más completa, aunque requiere más evidencia.",
        "Cada actor ve el desastre desde su perspectiva. La radio destaca el fenómeno; la vecina destaca la falta de alternativas de vivienda; la municipalidad reconoce una falla de planificación y fiscalización; el servicio de emergencia destaca la diferencia que hizo la preparación. Comparar perspectivas no es repartir culpas, sino identificar qué decisiones y qué condiciones se pueden cambiar para reducir el riesgo futuro.",
    ],
    vocab=[("causa próxima", "fenómeno o hecho que dispara el desastre"), ("causa de fondo", "condición previa que permitió que el fenómeno causara daño"), ("fiscalización", "control del cumplimiento de las normas por parte de una autoridad"), ("explicación territorial y social", "explicación que combina fenómeno, ubicación, normas, desigualdad y preparación"), ("desigualdad", "diferencia injusta en recursos, opciones o seguridad entre grupos")],
    worked=[
        ("Distinguir causas próximas y de fondo", "En una ciudad ficticia, un sismo derriba viviendas construidas sin respetar la norma de construcción. ¿Cuál es la causa próxima y cuál la de fondo?",
         ["El sismo dispara el desastre.", "La construcción que no cumplió la norma y la falta de control permitieron el daño."],
         "Próxima: el sismo; de fondo: viviendas fuera de norma y falta de fiscalización"),
        ("Comparar dos explicaciones", "Un diario ficticio dice «la lluvia causó la inundación» y una junta de vecinos dice «el humedal fue rellenado hace años». ¿Qué relación hay?",
         ["La lluvia es la causa próxima.", "El relleno del humedal es una causa de fondo."],
         "Son complementarias: una explica el disparo y la otra la condición previa"),
    ],
    mistakes=[("Buscar un solo culpable del desastre.", "Se simplifica un problema de varias causas.", "Identifica las causas próximas y de fondo y qué actores intervinieron."),
              ("Quedarse con la explicación de «fue la naturaleza» porque es la más simple.", "Se deja fuera las decisiones sobre el territorio.", "Pregunta qué decisiones sobre el espacio influyeron en el daño.")],
    T=[
        ("abc", "{F} ¿Qué actor destaca la falta de otro lugar donde vivir?", "La vecina de Villa Cauce", "La radio local", "El servicio de emergencia", "La vecina dice que no tenían otro lugar donde vivir."),
        ("abc", "{F} ¿Qué actor reconoce una falla de planificación?", "La municipalidad", "La radio local", "La vecina", "La municipalidad dice que el plan regulador no consideraba la quebrada."),
        ("En Geografía: ¿cómo se llama el control del cumplimiento de las normas por parte de una autoridad?", "Fiscalización", "Esa es la definición de fiscalización."),
        ("abc", "{F} ¿Qué causa próxima aparece en el caso?", "La lluvia intensa que dispara el aluvión", "El precio del suelo", "El plan regulador antiguo", "La lluvia dispara el fenómeno, por lo que es la causa próxima."),
        ("abc", "{F} ¿Qué es una causa de fondo mencionada por la municipalidad?", "El plan regulador antiguo que no consideraba la quebrada", "La lluvia", "El aluvión", "Es una condición previa del territorio que permitió el daño."),
        ("abc", "{F} ¿Qué dice el servicio de emergencia que explica la diferencia del daño entre sectores?", "La preparación: alarma y ruta de evacuación", "El tamaño de las viviendas", "La cercanía de cada sector al mar", "Atribuye el menor daño a la alarma y a la ruta de evacuación."),
        ("abc", "{F} La radio dice «fue imprevisible». ¿Qué deja fuera esa explicación?", "Las decisiones sobre dónde construir y cómo prepararse", "La lluvia", "El aluvión", "Una explicación solo natural omite las causas sociales y territoriales."),
        ("abc", "{F} Una estudiante dice: «Los vecinos de Villa Cauce tienen la culpa por vivir ahí». ¿Qué falta en su razonamiento?", "Las razones por las que no tenían otra opción y las decisiones de planificación y fiscalización", "Nada, es una explicación completa", "La cantidad de lluvia", "Una explicación completa considera las condiciones sociales que limitan las opciones."),
        ("abc", "{F} ¿Qué combinación de causas da una explicación territorial y social?", "Lluvia intensa, viviendas en el cauce, plan antiguo, falta de fiscalización y falta de alternativas", "Solo la lluvia", "Solo la fiscalización", "Combina el fenómeno con el territorio, las normas y la desigualdad."),
        ("{F} Explica por qué las perspectivas de la vecina y de la municipalidad pueden ser compatibles.", "Porque la falta de alternativas de vivienda y las fallas de planificación y fiscalización pueden actuar juntas", "Ambas apuntan a causas de fondo distintas que se refuerzan."),
        ("abc", "{F} ¿Qué decisión reduciría el riesgo futuro en Villa Cauce?", "Ofrecer alternativas de vivienda segura y mejorar la alerta y la evacuación", "Esperar que no vuelva a llover", "Construir más viviendas en el cauce", "Cambiar las condiciones de fondo reduce la exposición y la vulnerabilidad."),
        ("abc", "{F} Un concejal dice que repartir culpas es lo más importante. ¿Qué respuesta es más constructiva?", "Identificar qué decisiones y condiciones se pueden cambiar para reducir el riesgo", "Culpar solo a la municipalidad", "Culpar solo a los vecinos", "Comparar perspectivas sirve para encontrar cambios posibles, no solo para culpar."),
        ("abc", "{F} ¿Qué evidencia ayudaría a evaluar la explicación municipal sobre la fiscalización?", "Un registro de permisos y de controles de las viviendas nuevas", "La opinión de alguien que no vive en la comuna", "La cantidad de lluvia caída ese día", "Un registro de permisos y controles muestra si hubo fiscalización."),
    ],
    ctx=("abc", "Una comuna ficticia sufre incendios forestales cada verano. Un vecino dice que es por el calor; otro, que por plantaciones muy cerca de las casas sin cortafuegos. ¿Qué conclusión es más completa?", "Las dos causas pueden actuar juntas, y conviene revisar el uso del espacio y la preparación", "Solo importa el calor", "Solo importan las plantaciones", "Explicar un riesgo requiere combinar el fenómeno con las decisiones sobre el territorio."),
    sc=[
        ("En Geografía: ¿qué es una causa de fondo de un desastre?", "Una condición previa que permitió que el fenómeno causara daño", "Por ejemplo, la ubicación de las viviendas y la falta de fiscalización."),
        ("¿Es completa una explicación solo natural de un desastre?", "No", "Deja fuera las decisiones sobre el territorio."),
        ("¿Para qué se comparan perspectivas después de un desastre?", "Para identificar qué decisiones y condiciones se pueden cambiar", "Sirve para reducir el riesgo futuro."),
    ],
    op=("Lee este caso ficticio: una población junto a un estero sufre una inundación. Un vecino dice: «Es culpa de la lluvia». Otra vecina dice: «Rellenaron el humedal que absorbía el agua y nadie lo impidió». El comité de emergencia dice: «Donde había señalética y alerta, la gente salió a tiempo». "
        "Haz una tabla con actor, causa que destaca y tipo (próxima o de fondo), y escribe una explicación que combine las tres versiones más dos medidas posibles para reducir el riesgo futuro.",
        "Vecino: lluvia, causa próxima. Vecina: relleno del humedal y falta de control, causa de fondo. Comité: señalética y alerta, capacidad. Explicación: la lluvia disparó la inundación, pero el relleno aumentó la exposición y la alerta redujo el daño. Medidas: restaurar el humedal y mejorar la señalética.",
        ["clasifica bien las causas como próximas o de fondo", "combina las tres versiones", "propone dos medidas coherentes", "no culpa a las personas afectadas"],
        ["tabla de tres filas, explicación de tres o cuatro líneas y dos medidas"],
        ["tratar la lluvia como única causa", "proponer medidas sin relación con las causas", "culpar a los vecinos"],
        "Pregunta: «¿qué causa de fondo se puede cambiar?». Si no responde, pídele que mire la columna de causas de fondo."),
    reinforce="Elige una noticia sobre un desastre y escribe una causa próxima, una causa de fondo y una perspectiva distinta a la del texto.",
    extend="Conversa con una persona mayor sobre un fenómeno que afectó a tu zona y anota qué cambios se hicieron después en el uso del espacio.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (croquis descrito de un barrio ficticio de ladera). Cuadrícula de 5 columnas (1 a 5, de oeste a este) y 3 filas (1 a 3, de norte a sur); cada cuadro mide 100 metros. Las viviendas están en las columnas 1 y 2. "
     "Una quebrada ocupa las filas 2 y 3 de la columna 3; la fila 1 de la columna 3 es ladera alta, sin quebrada. El punto de reunión seguro está en la columna 5, fila 1. Un puente cruza la quebrada en la columna 3, fila 3 y podría cortarse en una crecida. "
     "Una familia vive en la columna 1, fila 2. Ruta A: hacia el norte hasta la fila 1 y luego al este hasta el punto seguro, sin entrar a la quebrada. Ruta B: hacia el sur hasta la fila 3, al este por el puente y luego al norte hasta el punto seguro.")
build(
    O5, 4, F,
    use="Aprenderé a explicar las consecuencias de un desastre y las medidas para reducir el riesgo (prevención, mitigación, preparación, respuesta y recuperación), y a evaluar rutas de evacuación en un croquis.",
    prior=["Conozco los elementos del riesgo.", "Comparo causas naturales y sociales.", "Sé leer un croquis con cuadrícula."],
    explain=[
        "Las consecuencias de un desastre son humanas (personas heridas o desplazadas), materiales (viviendas e infraestructura dañadas), económicas (trabajo y producción interrumpidos), ambientales (suelo, agua y vegetación alterados) y sociales (pérdida de redes, de vida de barrio, de salud emocional). No se distribuyen por igual: afectan más a quienes tienen menos recursos para prepararse y para recuperarse. Las consecuencias pueden aparecer de inmediato o durar años.",
        "La gestión del riesgo busca reducirlas con cinco tipos de acciones. La prevención evita crear nuevo riesgo, por ejemplo no autorizando viviendas en zonas de amenaza. La mitigación reduce el daño de la amenaza, por ejemplo con obras o con forestación de laderas. La preparación organiza a la comunidad: alertas, simulacros, rutas de evacuación y puntos de reunión. La respuesta es la acción durante la emergencia y la recuperación es la reconstrucción en condiciones más seguras que las anteriores.",
        "Una ruta de evacuación se evalúa por su largo, por si cruza zonas de amenaza y por si depende de una obra que puede fallar. La más corta no siempre es la mejor: si pasa por un puente que puede cortarse o por una quebrada, es más riesgosa. Las comunidades también deben participar en el diseño de sus rutas, porque conocen su territorio. Ante una emergencia real, se siguen las indicaciones de las autoridades y se avisa a una persona adulta.",
    ],
    vocab=[("prevención", "evitar crear nuevo riesgo"), ("mitigación", "reducir el daño que puede causar una amenaza"), ("preparación", "organizar a la comunidad para actuar: alertas, simulacros y rutas"), ("respuesta", "acciones durante la emergencia"), ("recuperación", "reconstrucción en condiciones más seguras")],
    worked=[
        ("Clasificar una medida", "Una comuna ficticia prohíbe construir viviendas en una zona de aluvión. ¿Qué tipo de acción de gestión del riesgo es?",
         ["La medida evita que aparezca nuevo riesgo.", "Eso es prevención."],
         "Prevención"),
        ("Calcular una ruta", "En un croquis ficticio de 100 metros por cuadro, una ruta pasa por 6 cuadros. ¿Cuántos metros mide?",
         ["Multiplica el número de cuadros por 100.", "6 × 100 = 600."],
         "600 metros"),
    ],
    mistakes=[("Elegir siempre la ruta de evacuación más corta.", "No se considera que pueda pasar por una zona de amenaza.", "Evalúa el largo, las zonas de amenaza que cruza y las obras que pueden fallar."),
              ("Confundir prevención con preparación.", "Ambas buscan reducir el riesgo, pero actúan en momentos distintos.", "La prevención evita el riesgo nuevo; la preparación organiza a la comunidad para actuar.")],
    T=[
        ("abc", "{F} ¿Dónde está el punto de reunión seguro?", "En la columna 5, fila 1", "En la columna 3, fila 3", "En la columna 1, fila 2", "La ficha ubica el punto seguro en la columna 5, fila 1."),
        ("En Geografía: ¿cómo se llama la acción de reducir el daño que puede causar una amenaza, por ejemplo con obras?", "Mitigación", "Esa es la definición de mitigación."),
        ("abc", "{F} ¿Qué cruza la Ruta B?", "El puente sobre la quebrada", "Solo la ladera alta", "Un cerro", "La ruta B pasa por el puente de la columna 3, fila 3."),
        ("=", "{F} ¿Cuántos metros mide la Ruta A? Recorre 1 cuadro al norte y 4 cuadros al este, con 100 metros cada cuadro.", "(1+4)*100", "Se suman los cuadros recorridos y se multiplican por 100 metros.", " metros"),
        ("=", "{F} ¿Cuántos metros mide la Ruta B? Recorre 1 cuadro al sur, 4 al este y 2 al norte, con 100 metros cada cuadro.", "(1+4+2)*100", "Se suman los cuadros recorridos y se multiplican por 100 metros.", " metros"),
        ("abc", "{F} ¿Qué ruta es más segura?", "La Ruta A, porque no entra a la quebrada ni depende del puente", "La Ruta B, porque es más corta", "Ninguna", "La ruta A evita la zona de amenaza y la obra que podría cortarse."),
        ("abc", "{F} ¿Por qué la ruta más corta puede no ser la mejor?", "Porque puede cruzar zonas de amenaza o depender de obras que pueden fallar", "Porque siempre tiene más cuadros", "Porque los puntos de reunión no importan", "En evacuación, la seguridad de la ruta pesa más que el largo."),
        ("abc", "Una municipalidad ficticia hace un simulacro anual de evacuación. ¿A qué tipo de acción corresponde?", "Preparación", "Recuperación", "Prevención", "Un simulacro organiza a la comunidad para actuar, que es preparación."),
        ("abc", "Tras un aluvión, una comuna ficticia reconstruye las viviendas en un terreno plano y seguro. ¿Qué acción es?", "Recuperación", "Mitigación", "Respuesta", "Reconstruir en condiciones más seguras es recuperación."),
        ("{F} Explica por qué la participación de la comunidad es importante para diseñar la ruta.", "Porque quienes viven allí conocen el territorio, sus peligros y sus caminos reales", "El conocimiento local mejora el diseño de rutas realistas."),
        ("abc", "{F} Si el puente se cortara y la familia solo conociera la Ruta B, ¿qué fallaría?", "La preparación, porque la comunidad no tendría una alternativa conocida", "La amenaza natural", "La exposición", "La falta de una ruta alternativa conocida es una debilidad de preparación."),
        ("abc", "{F} Una estudiante dice: «Con una buena ruta ya no hay riesgo». ¿Qué respuesta es más precisa?", "La ruta reduce el riesgo, pero no elimina la amenaza ni la exposición", "Tiene razón: no hay riesgo", "La ruta aumenta el riesgo", "Reducir el riesgo exige varias acciones; la ruta es solo una."),
        ("abc", "{F} ¿Qué combinación de acciones reduce más el riesgo del barrio?", "No autorizar nuevas viviendas en la quebrada, forestar la ladera, señalizar la Ruta A y hacer simulacros", "Solo hacer simulacros", "Solo señalizar el puente", "Prevención, mitigación y preparación juntas cubren más aspectos del riesgo."),
    ],
    ctx=("abc", "Una escuela ficticia está en una zona de tsunami y debe definir su plan. ¿Qué paso es más adecuado?", "Elegir una ruta hacia una zona alta, señalizarla y practicarla con simulacros, siguiendo las indicaciones oficiales", "Esperar a que ocurra el tsunami", "Elegir una ruta que pase por la playa porque es más corta", "El plan combina una ruta hacia lo alto, señalética y práctica."),
    sc=[
        ("En Geografía: ¿qué es la prevención en gestión del riesgo?", "Evitar crear nuevo riesgo", "Por ejemplo, no autorizar viviendas en zonas de amenaza."),
        ("¿Qué es la recuperación?", "La reconstrucción en condiciones más seguras", "No es volver a lo mismo, sino reducir el riesgo."),
        ("¿Se reparten por igual las consecuencias de un desastre?", "No", "Afectan más a quienes tienen menos recursos."),
    ],
    op=("Dibuja un croquis con cuadrícula (6 columnas por 4 filas, cuadro de 100 metros) de un barrio ficticio con una quebrada, un puente, viviendas y un punto de reunión seguro. Marca dos rutas desde una vivienda, calcula sus largos en metros y escribe cuál recomiendas y por qué, qué acción de prevención y qué acción de preparación agregarías.",
        "Vivienda en columna 1, fila 3. Quebrada en columna 4. Punto seguro en columna 6, fila 1. Ruta A por el norte: 2 + 5 = 7 cuadros = 700 metros, sin cruzar. Ruta B por el puente: 5 + 2 = 7 cuadros = 700 metros. Recomiendo A. Prevención: no construir en la quebrada. Preparación: simulacro anual.",
        ["dibuja un croquis con cuadrícula y al menos cuatro elementos", "calcula bien el largo de dos rutas", "recomienda una ruta con una razón de seguridad", "propone una acción de prevención y una de preparación"],
        ["croquis, dos cálculos, una recomendación y dos acciones"],
        ["recomendar la ruta más corta sin mirar los riesgos", "confundir prevención con preparación", "olvidar el punto de reunión"],
        "Pregunta: «¿qué pasaría con tu ruta si una obra falla?». Si no responde, pídele que revise la ruta que depende del puente."),
    reinforce="Dibuja la ruta de evacuación de tu casa o de tu colegio hasta un punto seguro y anota su largo en pasos.",
    extend="Averigua cuáles son los simulacros que realiza tu colegio o tu comuna y compara con lo que aprendiste sobre preparación.",
)

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (mapa descrito de la comuna ficticia de Puerto Claro). Título: «Puerto Claro: relieve y servicios». Escala 1:50.000, es decir, 1 centímetro en el mapa representa 50.000 centímetros (500 metros) en el terreno. El norte está hacia arriba del papel. "
     "Leyenda: triángulo = cerro; línea azul = río; cuadrado negro = escuela; cruz roja = consultorio; línea gris = camino. Medidas hechas con regla sobre el mapa: de la escuela al consultorio hay 6 centímetros en línea recta, hacia el este; el río corre a 3 centímetros al sur de la escuela; el cerro está a 4 centímetros al norte del consultorio. "
     "Curvas de nivel (líneas que unen puntos de igual altura) cada 20 metros: la curva de la base del cerro marca 100 metros y el cerro tiene 5 curvas en total, contando la de la base como la primera y llegando hasta la más alta. Fuente: levantamiento municipal de ejemplo.")
build(
    O6, 1, F,
    use="Aprenderé a interpretar y analizar cartografía: leer título, leyenda, orientación y escala, medir distancias y alturas, y preguntar quién produjo el mapa y para qué.",
    prior=["Sé leer un croquis con cuadrícula.", "Multiplico y divido con números enteros.", "Conozco los puntos cardinales."],
    explain=[
        "La cartografía es el conjunto de técnicas para representar el territorio en mapas. Un mapa tiene partes que se deben leer antes de interpretar: el título (qué muestra), la leyenda (qué significan los símbolos y colores), la orientación (hacia dónde está el norte), la escala (cuánto se redujo la realidad) y la fuente (quién lo hizo y cuándo). Un mapa que no tiene alguna de estas partes entrega información incompleta.",
        "La escala numérica 1:50.000 significa que 1 unidad del mapa equivale a 50.000 unidades del terreno. Con 1 centímetro en el mapa se representan 50.000 centímetros, es decir, 500 metros. Para hallar una distancia real se multiplican los centímetros medidos por 500 metros. Una escala con un número menor después de los dos puntos (1:25.000) muestra más detalle; con un número mayor (1:100.000), menos detalle y más territorio. No hay que confundir esta escala cartográfica con la escala geográfica de análisis (barrio, comuna, región).",
        "Los mapas topográficos muestran el relieve mediante curvas de nivel: cada curva une puntos de igual altura, y si están muy juntas indican una pendiente fuerte. Los mapas temáticos muestran un tema, como servicios o riesgos. Todo mapa es una representación hecha por alguien con un propósito: se interroga igual que cualquier fuente, preguntando qué muestra, qué omite y para quién fue hecho.",
    ],
    vocab=[("cartografía", "técnicas para representar el territorio en mapas"), ("escala cartográfica", "relación entre una medida en el mapa y la medida real"), ("leyenda", "explicación de los símbolos y colores de un mapa"), ("curva de nivel", "línea que une puntos de igual altura"), ("mapa temático", "mapa que muestra un tema específico, como servicios o riesgos")],
    worked=[
        ("Convertir una medida del mapa", "En un mapa a escala 1:50.000, dos puntos están a 5 centímetros. ¿Qué distancia real hay?",
         ["Cada centímetro representa 500 metros.", "5 × 500 = 2.500."],
         "2.500 metros (2,5 kilómetros)"),
        ("Leer curvas de nivel", "En un cerro ficticio las curvas de nivel están cada 10 metros y la curva de la base marca 50 metros. ¿Qué altura marca la tercera curva, contando la de la base como la primera?",
         ["La base es la primera: 50 metros.", "La segunda marca 60 y la tercera 70."],
         "70 metros"),
    ],
    mistakes=[("Medir una distancia en el mapa y olvidar convertirla con la escala.", "Se confunde la medida del papel con la del terreno.", "Multiplica la medida del mapa por lo que representa 1 centímetro."),
              ("Interpretar los símbolos sin leer la leyenda.", "Se supone que los símbolos significan lo mismo en todos los mapas.", "Lee la leyenda antes de interpretar el mapa.")],
    T=[
        ("abc", "{F} ¿Qué símbolo representa una escuela en la leyenda?", "Un cuadrado negro", "Una cruz roja", "Un triángulo", "La leyenda indica cuadrado negro para la escuela."),
        ("En Geografía: ¿cómo se llama la línea de un mapa que une puntos de igual altura?", "Curva de nivel", "Esa es la definición de curva de nivel."),
        ("abc", "{F} ¿Qué representa 1 centímetro en este mapa?", "500 metros del terreno", "50 metros del terreno", "5 kilómetros del terreno", "La escala 1:50.000 equivale a 500 metros por centímetro."),
        ("=", "{F} ¿Qué distancia real hay entre la escuela y el consultorio, en metros?", "6*500", "Se multiplican los 6 centímetros del mapa por 500 metros.", " metros"),
        ("=", "{F} ¿Qué distancia real hay entre la escuela y el río, en metros?", "3*500", "Se multiplican los 3 centímetros del mapa por 500 metros.", " metros"),
        ("abc", "{F} ¿En qué dirección desde la escuela está el consultorio?", "Al este", "Al oeste", "Al sur", "La ficha dice que el consultorio está a 6 centímetros hacia el este."),
        ("abc", "{F} ¿A qué altura está la curva más alta del cerro, si la base marca 100 metros y las curvas están cada 20 metros?", "180 metros", "200 metros", "120 metros", "Las cinco curvas marcan 100, 120, 140, 160 y 180 metros."),
        ("=", "{F} ¿Cuántos kilómetros hay en línea recta entre el cerro y el consultorio? Mide 4 centímetros en el mapa; convierte los metros a kilómetros.", "4*500//1000", "Son 4 centímetros por 500 metros, es decir, 2.000 metros, que equivalen a 2 kilómetros.", " kilómetros"),
        ("abc", "Dos mapas de la misma comuna ficticia tienen escalas 1:25.000 y 1:100.000. ¿Cuál muestra más detalle?", "El de 1:25.000", "El de 1:100.000", "Los dos muestran el mismo detalle", "Un número menor después de los dos puntos significa menos reducción y más detalle."),
        ("abc", "{F} Si las curvas de nivel estuvieran muy juntas en una ladera, ¿qué indicarían?", "Una pendiente fuerte", "Una pendiente suave", "Un lago", "Curvas muy juntas indican que la altura cambia rápido en poca distancia."),
        ("abc", "{F} En un mapa a 1:25.000, 6 centímetros equivalen a 1.500 metros. ¿Cómo cambia la distancia real respecto del mapa a 1:50.000, donde 6 centímetros son 3.000 metros?", "Es la mitad, porque 1 centímetro representa menos terreno", "Es la misma", "Es el doble", "Con una escala menos reducida cada centímetro representa 250 metros en lugar de 500."),
        ("{F} Explica por qué es importante revisar la fuente y la fecha de un mapa.", "Porque indican quién lo hizo, cuándo y con qué propósito, y si los datos están actualizados", "Toda representación tiene productor y época, que condicionan lo que muestra."),
        ("abc", "{F} Un estudiante dice: «Como el consultorio está a 6 centímetros, queda a 6 kilómetros». ¿Qué error comete?", "No convirtió los centímetros con la escala", "Midió mal con la regla", "Confundió norte con sur", "Los 6 centímetros del mapa equivalen a 3.000 metros, no a 6 kilómetros."),
    ],
    ctx=("abc", "Una junta de vecinos ficticia recibe un mapa de riesgo sin título, sin escala y sin fuente. ¿Qué conviene hacer antes de usarlo?", "Pedir los datos que faltan y comprobar quién lo hizo y para qué", "Usarlo como si fuera exacto", "Descartarlo sin mirarlo", "Un mapa sin escala ni fuente no permite medir ni evaluar su confiabilidad."),
    sc=[
        ("En Geografía: ¿qué es la escala cartográfica?", "La relación entre una medida en el mapa y la medida real", "Permite convertir distancias del mapa en distancias del terreno."),
        ("¿Para qué sirve la leyenda?", "Para explicar los símbolos y colores del mapa", "Sin ella no se pueden interpretar los símbolos."),
        ("¿Qué distancia real representan 2 centímetros en un mapa a 1:50.000?", "1.000 metros", "Cada centímetro representa 500 metros, así que 2 centímetros son 1.000."),
    ],
    op=("Dibuja un mapa sencillo de tu colegio y sus alrededores (o de un lugar ficticio) con título, leyenda de al menos cuatro símbolos, indicación del norte, una escala gráfica (por ejemplo, 1 centímetro = 20 metros) y fuente. "
        "Mide con una regla la distancia entre dos puntos de tu mapa, conviértela con la escala y escribe una pregunta que alguien podría contestar leyendo tu mapa.",
        "Mapa del colegio con título «Mi colegio», leyenda con patio, sala, biblioteca y entrada, flecha de norte y escala 1 cm = 20 m. Entre la entrada y la biblioteca hay 4 cm: 4 × 20 = 80 metros. Pregunta: ¿qué distancia hay de la entrada a la biblioteca?",
        ["incluye título, leyenda, norte, escala y fuente", "convierte bien la distancia con la escala", "la leyenda tiene al menos cuatro símbolos claros", "la pregunta se contesta con el mapa"],
        ["mapa dibujado con sus partes, un cálculo y una pregunta"],
        ["olvidar la escala", "medir con una unidad distinta de la escala", "dibujar símbolos sin leyenda"],
        "Pregunta: «¿qué distancia real representan 3 centímetros de tu mapa?». Si no responde, pídele que relea su escala."),
    reinforce="Mide en un mapa o croquis de tu barrio la distancia entre tu casa y un servicio, y conviértela con la escala.",
    extend="Compara un mapa de tu comuna con una imagen aérea o satelital y anota tres diferencias en lo que muestran.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (coordenadas e imágenes de ejemplo, ficticias). Localidades de ejemplo: Puerto Claro, 33° de latitud sur y 72° de longitud oeste; Villa Alta, 36° de latitud sur y 71° de longitud oeste; Valle Sur, 40° de latitud sur y 73° de longitud oeste. "
     "Regla aproximada: 1 grado de latitud equivale a unos 111 kilómetros. Imagen satelital de ejemplo de un recuadro del humedal de Puerto Claro, dividido en 80 cuadros: en la fecha 1, los 80 cuadros se ven verdes (vegetación); en la fecha 2, 20 de esos cuadros se ven grises (suelo construido).")
build(
    O6, 2, F,
    use="Aprenderé a georreferenciar con coordenadas geográficas, a leer imágenes satelitales y a interpretar información geográfica en capas, usando estadísticas y datos para describir procesos del espacio.",
    prior=["Sé leer un mapa con escala.", "Calculo diferencias y porcentajes.", "Conozco los puntos cardinales y el ecuador."],
    explain=[
        "Georreferenciar es asignar coordenadas a un lugar, a una imagen o a un dato para ubicarlo en la superficie terrestre. Las coordenadas geográficas son la latitud y la longitud. La latitud mide la distancia angular al ecuador, de 0° a 90°, hacia el norte o hacia el sur; Chile está en latitudes sur. La longitud mide la distancia angular al meridiano de Greenwich, hacia el este o hacia el oeste; Chile está en longitudes oeste.",
        "Para comparar dos puntos se compara su latitud y su longitud. En el hemisferio sur, un número mayor de latitud sur significa más al sur: 40° sur está más al sur que 36° sur. En longitudes oeste ocurre al revés para la posición este-oeste: 71° oeste está más al este que 73° oeste, porque está más cerca del meridiano de Greenwich. La diferencia de latitud en grados, multiplicada por unos 111 kilómetros, da una distancia norte-sur aproximada.",
        "Las imágenes satelitales y aéreas muestran la superficie en cuadros pequeños (píxeles); si se comparan dos fechas se detecta el cambio del uso del suelo. Un sistema de información geográfica (SIG) es un conjunto de programas y datos que superpone capas de información sobre un mismo territorio, como relieve, población y servicios, y permite cruzarlas. Las estadísticas geográficas entregan cifras por comuna o por región. Todas estas fuentes tienen un productor, una fecha y una resolución (el tamaño del cuadro más pequeño que se distingue: si es grande, se pierden los detalles), que limitan lo que muestran.",
    ],
    vocab=[("georreferenciar", "asignar coordenadas a un lugar o dato para ubicarlo en la Tierra"), ("latitud", "distancia angular al ecuador, hacia el norte o el sur"), ("longitud", "distancia angular al meridiano de Greenwich, hacia el este o el oeste"), ("píxel", "cuadro mínimo de una imagen digital"), ("sistema de información geográfica (SIG)", "conjunto de programas y datos que superpone capas de información de un territorio")],
    worked=[
        ("Comparar latitudes", "Dos localidades ficticias están en 30° sur y 35° sur. ¿Cuál está más al sur y a cuántos kilómetros aproximados?",
         ["35° sur está más al sur que 30° sur.", "La diferencia es 5° y 5 × 111 = 555."],
         "La de 35° sur, a unos 555 kilómetros"),
        ("Detectar un cambio en una imagen", "Un recuadro ficticio de una imagen tiene 50 cuadros; en la fecha 1 hay 10 grises y en la fecha 2 hay 25. ¿Qué porcentaje de la superficie cambió?",
         ["Aumento: 25 − 10 = 15 cuadros.", "15 ÷ 50 × 100 = 30 %."],
         "30 %"),
    ],
    mistakes=[("Pensar que un número mayor de longitud oeste significa más al este.", "Se confunde el sentido de la numeración al oeste del meridiano.", "En Chile, a mayor longitud oeste, más al oeste."),
              ("Usar una imagen satelital sin mirar su fecha.", "Se supone que muestra el presente.", "Revisa la fecha y compara con otras para saber qué cambió.")],
    T=[
        ("abc", "{F} ¿Qué localidad está más al sur?", "Valle Sur", "Puerto Claro", "Villa Alta", "40° sur es la mayor latitud sur de las tres localidades."),
        ("En Geografía: ¿cómo se llama el proceso de asignar coordenadas a un lugar o a un dato para ubicarlo en la Tierra?", "Georreferenciar", "Esa es la definición de georreferenciar."),
        ("abc", "{F} ¿Qué localidad está más al norte?", "Puerto Claro", "Villa Alta", "Valle Sur", "33° sur es la menor latitud sur, es decir, la más cercana al ecuador."),
        ("=", "{F} ¿Cuántos grados de latitud separan a Puerto Claro de Villa Alta?", "36-33", "Se resta la menor latitud sur a la mayor.", " grados"),
        ("=", "{F} ¿A cuántos kilómetros aproximados, de norte a sur, están Puerto Claro y Villa Alta? Usa la regla aproximada de la ficha.", "(36-33)*111", "Se multiplica la diferencia de latitud por 111 kilómetros.", " kilómetros"),
        ("abc", "{F} ¿Qué localidad está más al este?", "Villa Alta, en 71° oeste", "Valle Sur, en 73° oeste", "Puerto Claro, en 72° oeste", "En longitud oeste, el menor número está más cerca del meridiano de Greenwich, es decir, más al este."),
        ("abc", "{F} ¿Qué localidad está más al oeste?", "Valle Sur, en 73° oeste", "Villa Alta, en 71° oeste", "Puerto Claro, en 72° oeste", "73° oeste es el mayor valor de longitud oeste, el más alejado del meridiano de Greenwich."),
        ("=", "{F} En la fecha 2, ¿cuántos de los 80 cuadros del recuadro siguen verdes?", "80-20", "De los 80 cuadros, 20 pasaron a gris; los demás siguen verdes.", " cuadros"),
        ("=", "{F} ¿Qué porcentaje del recuadro cambió de verde a gris?", "20*100//80", "Se divide la cantidad de cuadros que cambiaron entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} Un estudiante dice: «La imagen prueba que el humedal fue destruido». ¿Qué corrección es más precisa?", "Muestra que 20 de 80 cuadros del recuadro cambiaron, pero no dice la causa ni el estado de los 60 restantes", "Tiene razón: la imagen lo prueba todo", "La imagen no muestra nada", "Una imagen muestra un cambio; la causa y el estado total requieren otras fuentes."),
        ("abc", "{F} ¿Qué es una capa de información en un SIG?", "Un conjunto de datos sobre un tema, como servicios o relieve, que se superpone con otros", "Una pintura del mapa", "Una fotografía de las personas", "Un SIG organiza el territorio en capas que se pueden cruzar."),
        ("{F} Explica qué capas cruzarías para saber qué viviendas de Puerto Claro están cerca del humedal.", "La capa de viviendas y la capa del humedal", "El cruce de una capa de ubicación de viviendas con la capa de humedal permite medir cercanía."),
        ("abc", "{F} Si una imagen satelital tiene baja resolución, ¿qué limitación tiene?", "No permite distinguir detalles pequeños", "Permite medir con exactitud cada árbol", "Solo sirve para fechas antiguas", "La resolución es el tamaño del cuadro mínimo; si es grande, se pierden los detalles."),
    ],
    ctx=("abc", "Una comuna ficticia quiere saber si el área de dunas protegidas ha disminuido. Dispone de dos imágenes aéreas de fechas distintas y un informe de una empresa. ¿Qué estrategia es más sólida?", "Comparar las imágenes de las dos fechas y contrastar con el informe y con el testimonio de vecinos", "Usar solo el informe de la empresa", "Usar solo una imagen", "La comparación entre fechas y fuentes diversas permite detectar el cambio con respaldo."),
    sc=[
        ("En Geografía: ¿qué mide la latitud?", "La distancia angular al ecuador, hacia el norte o el sur", "Se expresa en grados de 0° a 90°."),
        ("¿Qué localidad está más al sur: una en 38° sur o una en 34° sur?", "La de 38° sur", "A mayor latitud sur, más al sur."),
        ("¿Qué es un SIG?", "Un conjunto de programas y datos que superpone capas de información de un territorio", "Sirve para cruzar información sobre un mismo lugar."),
    ],
    op=("Usa estos datos ficticios: Localidad A, 30° sur y 70° oeste; Localidad B, 35° sur y 72° oeste; Localidad C, 38° sur y 71° oeste. Escribe cuál está más al norte, más al sur, más al este y más al oeste; calcula la distancia norte-sur aproximada entre A y C con la regla de 111 kilómetros por grado; y propone una pregunta sobre un cambio del uso del suelo que podrías responder comparando dos imágenes satelitales de una de las localidades.",
        "Más al norte: A. Más al sur: C. Más al este: A (70° oeste). Más al oeste: B (72° oeste). A–C: 38 − 30 = 8 grados; 8 × 111 = 888 kilómetros. Pregunta: ¿cuánta superficie de bosque se transformó en suelo construido en B entre dos fechas?",
        ["ordena bien las localidades por latitud y longitud", "calcula bien la distancia aproximada", "formula una pregunta que se puede responder con imágenes de dos fechas", "usa el vocabulario de coordenadas con precisión"],
        ["cuatro respuestas, un cálculo y una pregunta"],
        ["confundir latitud con longitud", "invertir el sentido de la longitud oeste", "proponer una pregunta que una imagen no puede contestar"],
        "Pregunta: «¿por qué 70° oeste está más al este que 72° oeste?». Si no sabe, pídele que relea la explicación sobre longitud."),
    reinforce="Escribe las coordenadas de ejemplo de tres lugares (inventados) y ordénalos de norte a sur y de este a oeste.",
    extend="Compara dos imágenes de un mismo lugar de tu comuna en fechas distintas (si las tienes) y anota qué cambió y qué no puedes saber con ellas.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (encuesta de ejemplo, ficticia). En el barrio El Sauzal viven unas 1.000 personas adultas. Un grupo de estudiantes encuesta a 50 personas que pasan por la plaza entre las 10 y las 12 horas de un día de semana. "
     "Pregunta 1 (cerrada): ¿con qué frecuencia usa la plaza? Todos los días: 10; algunas veces a la semana: 20; casi nunca: 15; nunca: 5. Pregunta 2 (cerrada): ¿qué mejoraría? Más sombra: 22; más seguridad: 18; más juegos: 10. "
     "Pregunta 3 (abierta): ¿qué recuerdo tiene de la plaza? Antes de entrevistar, el grupo pide permiso, explica para qué usará las respuestas y no anota nombres.")
build(
    O6, 3, F,
    use="Aprenderé a recoger información con encuestas y entrevistas, a distinguir universo y muestra, preguntas cerradas y abiertas, a tabular y a calcular porcentajes, reconociendo sesgos y cuidando la ética de la investigación.",
    prior=["Calculo porcentajes.", "Interrogo fuentes e indicadores.", "Sé qué es una muestra."],
    explain=[
        "Una encuesta recoge datos de muchas personas con un cuestionario igual para todas. El universo es el grupo completo que se quiere conocer (por ejemplo, las personas adultas de un barrio) y la muestra es la parte de ese grupo que efectivamente responde. Una muestra es útil si se parece al universo; si se elige solo a quienes pasan a cierta hora, puede dejar fuera a otros grupos y producir un sesgo, es decir, una distorsión en los resultados.",
        "Las preguntas cerradas ofrecen alternativas fijas y se pueden contar y expresar en porcentajes. Las preguntas abiertas permiten respuestas libres y entregan matices, pero se analizan agrupando ideas. Para tabular se cuenta cuántas personas eligieron cada alternativa; el porcentaje se calcula dividiendo ese número entre el total de respondientes y multiplicando por 100. Una entrevista es una conversación guiada por preguntas abiertas, que explora experiencias y significados.",
        "La investigación con personas tiene reglas éticas: pedir permiso, explicar para qué se usará la información, no anotar datos personales si no son necesarios, respetar quien no quiere responder y entregar los resultados sin identificar a nadie. Con menores de edad se pide además el permiso de una persona adulta responsable. Una encuesta bien hecha declara su muestra, su fecha y sus límites, y no extiende sus resultados a quienes no fueron consultados.",
    ],
    vocab=[("universo", "grupo completo que se quiere conocer"), ("muestra", "parte del universo que responde"), ("sesgo", "distorsión en los resultados por cómo se eligió la muestra o se hizo la pregunta"), ("pregunta cerrada", "pregunta con alternativas fijas de respuesta"), ("tabulación", "conteo y orden de las respuestas en una tabla")],
    worked=[
        ("Calcular un porcentaje de una encuesta", "En una encuesta ficticia de 80 personas, 20 eligieron «más árboles». ¿Qué porcentaje es?",
         ["Divide 20 entre 80.", "20 ÷ 80 × 100 = 25 %."],
         "25 %"),
        ("Detectar un sesgo", "Una encuesta ficticia sobre el transporte público se aplica solo en el paradero a las 8 de la mañana. ¿Qué sesgo puede haber?",
         ["Solo responden quienes usan el bus a esa hora.", "Quedan fuera quienes usan otros horarios o no lo usan."],
         "Una muestra sesgada hacia usuarios de la hora punta"),
    ],
    mistakes=[("Extender los resultados de la muestra a todo el universo sin revisar cómo se eligió.", "Se supone que cualquier muestra representa al universo.", "Declara cómo se eligió la muestra y limita las conclusiones a quienes respondieron."),
              ("Anotar nombres y datos personales sin necesidad.", "Se olvida el cuidado de la privacidad.", "Pide permiso, no anotes datos personales innecesarios y presenta resultados sin identificar.")],
    T=[
        ("abc", "{F} ¿Cuántas personas fueron encuestadas?", "50", "1.000", "10", "La ficha dice que se encuestó a 50 personas."),
        ("En Geografía: ¿cómo se llama la parte del universo que responde una encuesta?", "Muestra", "La muestra es la parte del universo que efectivamente responde."),
        ("abc", "{F} ¿Qué tipo de pregunta es «¿con qué frecuencia usa la plaza?»?", "Cerrada", "Abierta", "Ninguna", "Ofrece alternativas fijas entre las que se elige una respuesta."),
        ("=", "{F} ¿Qué porcentaje de las personas encuestadas usa la plaza algunas veces a la semana?", "20*100//50", "Se divide la cantidad de esa respuesta entre el total de encuestados y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de las personas encuestadas eligió «más sombra»?", "22*100//50", "Se divide 22 entre 50 y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de las 1.000 personas adultas del barrio fue encuestado?", "50*100//1000", "Se divide el tamaño de la muestra entre el universo y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué sesgo puede tener la muestra?", "Dejar fuera a quienes no pasan por la plaza entre las 10 y las 12 horas de un día de semana", "Haber encuestado a demasiadas personas", "No incluir preguntas cerradas", "Encuestar a una hora y día fijos puede dejar fuera a trabajadores y a quienes van en otros horarios."),
        ("abc", "{F} ¿Qué conclusión es válida con esta encuesta?", "Entre las 50 personas encuestadas, 22 piden más sombra", "A todas las personas del barrio les falta sombra", "La plaza es poco usada en toda la comuna", "Una conclusión válida se limita a quienes respondieron."),
        ("abc", "{F} ¿Qué aporta la pregunta abierta que las cerradas no aportan?", "Matices y experiencias que no caben en alternativas", "Un porcentaje exacto", "Una muestra mayor", "Las respuestas libres entregan significados que las alternativas no recogen."),
        ("abc", "{F} ¿Qué acción ética hace el grupo antes de entrevistar?", "Pedir permiso y explicar para qué usará las respuestas", "Anotar los nombres de todos", "Grabar sin avisar", "El permiso informado es una regla básica de la investigación con personas."),
        ("abc", "{F} Un estudiante quiere agregar la pregunta «¿cuál es su dirección?». ¿Qué conviene responder?", "Que no es necesaria y puede afectar la privacidad", "Que sí, porque es útil siempre", "Que solo se pregunte a los vecinos", "Los datos personales innecesarios no se piden."),
        ("{F} Propón una forma de mejorar la muestra para que se parezca más al universo.", "Encuestar en distintos horarios y días, incluyendo fines de semana", "Una muestra más diversa en horarios reduce el sesgo."),
        ("abc", "{F} Si el 44 % pide sombra y el 36 % pide seguridad, ¿qué decisión es más prudente?", "Informar ambos porcentajes y pedir más información antes de decidir", "Elegir sombra sin más análisis", "Descartar la seguridad por tener menos porcentaje", "Los porcentajes orientan, pero no reemplazan otras fuentes ni la participación."),
    ],
    ctx=("abc", "Un colegio ficticio quiere conocer cómo llegan sus estudiantes al colegio. Una alumna propone encuestar solo a su curso. ¿Qué conviene hacer?", "Encuestar a estudiantes de distintos cursos y declarar cuántos respondieron", "Usar solo su curso y afirmar que vale para todo el colegio", "No hacer encuesta", "Una muestra diversa se parece más al universo; declarar su tamaño ayuda a leer los resultados."),
    sc=[
        ("En Geografía: ¿qué es el universo en una encuesta?", "El grupo completo que se quiere conocer", "La muestra es solo una parte de él."),
        ("¿Qué es un sesgo?", "Una distorsión en los resultados por cómo se eligió la muestra o se hizo la pregunta", "Un sesgo puede llevar a conclusiones erradas sobre el universo."),
        ("¿Cómo se calcula un porcentaje de respuestas?", "Dividiendo las respuestas de una alternativa entre el total y multiplicando por 100", "Así se comparan alternativas con distintos totales."),
    ],
    op=("Diseña una mini encuesta ficticia de tres preguntas sobre el uso de un espacio de tu barrio o colegio (una cerrada con tres alternativas, una cerrada con dos alternativas y una abierta). Inventa los resultados de 40 respuestas para las cerradas (que sumen 40), calcula dos porcentajes, indica tu universo y tu muestra, un posible sesgo y una regla ética que aplicarías.",
        "Pregunta 1: ¿usa la cancha? Todos los días: 10; a veces: 20; nunca: 10. Total 40. A veces: 20 ÷ 40 × 100 = 50 %. Todos los días: 10 ÷ 40 × 100 = 25 %. Universo: estudiantes del colegio. Muestra: 40 estudiantes del recreo. Sesgo: solo quienes están en el patio. Regla: no anotar nombres.",
        ["las alternativas suman el total declarado", "calcula bien dos porcentajes", "declara universo y muestra", "identifica un sesgo y una regla ética"],
        ["cuestionario de tres preguntas, tabla de resultados y cálculos"],
        ["resultados que no suman el total", "confundir universo con muestra", "no incluir ninguna regla ética"],
        "Pregunta: «¿quién quedó fuera de tu muestra?». Si no lo identifica, pídele que piense en horarios y lugares."),
    reinforce="Escribe una pregunta cerrada y una abierta sobre un tema de tu barrio y explica para qué sirve cada una.",
    extend="Aplica a cinco personas (con su permiso) una pregunta cerrada sobre un servicio de tu barrio, sin anotar sus nombres, y calcula los porcentajes.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (trabajo de campo y mapeo de ejemplo, ficticios). Un grupo de estudiantes, acompañados por una docente y con permiso del colegio, recorre un tramo de 400 metros de una calle comercial (cuatro cuadras de 100 metros) y registra con una pauta: locales abiertos, 14; locales cerrados, 6; árboles, 9; bancas, 3; rampas de acceso, 2. "
     "Mapeo participativo: un grupo de vecinos marca sobre un plano del barrio puntos verdes en lugares donde se sienten seguros y puntos rojos donde no: 12 puntos verdes y 8 rojos, concentrados en una esquina sin iluminación. "
     "Mapa mental: tres vecinos dibujan el barrio de memoria; dos dibujan muy grande la plaza y la feria, y uno dibuja muy pequeña la calle donde no se siente seguro.")
build(
    O6, 4, F,
    use="Aprenderé a recoger información con trabajo de campo, mapeos participativos y escalas de percepción, a registrarla con una pauta y a reconocer el valor y los límites de la experiencia de las personas.",
    prior=["Sé tabular y calcular porcentajes.", "Conozco la ética de las encuestas.", "Interpreto un plano o croquis."],
    explain=[
        "El trabajo de campo es salir a observar y registrar en el terreno. Para que sea ordenado se usa una pauta, es decir, una lista de lo que se observará (locales abiertos, árboles, rampas), con el lugar, la fecha y la hora. La observación se hace en grupo, acompañado por una persona adulta, en lugares seguros, con permiso cuando corresponda y sin entrar a propiedades privadas ni fotografiar personas sin su autorización.",
        "El mapeo participativo es una técnica en que las personas de un territorio marcan en un plano sus saberes, usos y percepciones, por ejemplo, dónde se sienten seguras o dónde hay riesgos. Reconoce que quienes viven en un lugar son una fuente de conocimiento. Sus resultados son experiencias de personas, no mediciones: se usan junto a datos y mapas para entender mejor el territorio.",
        "Las escalas de percepción son las formas en que las personas viven y dimensionan el espacio: la casa, la cuadra, el barrio, la ciudad. Los mapas mentales, dibujos del barrio hechos de memoria, muestran qué lugares son importantes para cada persona: el tamaño que se da a un lugar refleja su significado y no su tamaño real. Estas técnicas permiten comprender cómo distintos grupos viven el mismo espacio.",
    ],
    vocab=[("trabajo de campo", "observación y registro de información en el terreno"), ("pauta de observación", "lista ordenada de lo que se registrará en terreno"), ("mapeo participativo", "técnica en que las personas marcan en un plano sus saberes y percepciones del territorio"), ("mapa mental", "dibujo del espacio hecho de memoria"), ("escala de percepción", "forma en que las personas dimensionan el espacio: casa, cuadra, barrio o ciudad")],
    worked=[
        ("Calcular un porcentaje de una pauta", "En una pauta ficticia se contaron 18 locales: 12 abiertos y 6 cerrados. ¿Qué porcentaje está cerrado?",
         ["Divide los cerrados entre el total: 6 ÷ 18.", "Eso es un tercio, un 33 %."],
         "Un tercio (aproximadamente 33 %)"),
        ("Interpretar un mapa mental", "En un mapa mental ficticio, una persona dibuja enorme la biblioteca de su barrio y pequeño el supermercado. ¿Qué indica?",
         ["El tamaño muestra importancia personal.", "No muestra el tamaño real de los lugares."],
         "Que la biblioteca es muy significativa para esa persona"),
    ],
    mistakes=[("Salir a terreno sin pauta ni permiso.", "Se improvisa y se corre riesgo.", "Prepara una pauta, pide permiso y sal acompañado por una persona adulta."),
              ("Tratar un mapa mental como si midiera distancias reales.", "Se confunde percepción con medición.", "Úsalo para entender significados y compáralo con un mapa a escala.")],
    T=[
        ("abc", "{F} ¿Cuántos locales abiertos registró el grupo?", "14", "6", "9", "La pauta anota 14 locales abiertos."),
        ("En Geografía: ¿cómo se llama la lista ordenada de lo que se registrará en terreno?", "Pauta de observación", "Esa es la definición de pauta de observación."),
        ("abc", "{F} ¿Quién acompañó al grupo en el recorrido?", "Una docente", "Un vecino", "Nadie", "La ficha dice que los estudiantes iban acompañados por una docente."),
        ("=", "{F} ¿Cuántos locales hay en total en el tramo?", "14+6", "Se suman los locales abiertos y los cerrados.", " locales"),
        ("=", "{F} ¿Qué porcentaje de los locales está abierto?", "14*100//20", "Se divide la cantidad de locales abiertos entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de los puntos marcados por los vecinos es rojo?", "8*100//20", "Se suman 12 verdes y 8 rojos para tener 20, y se calcula el porcentaje de los rojos.", " %"),
        ("abc", "{F} ¿Qué técnica usaron los vecinos para marcar dónde se sienten seguros?", "Mapeo participativo", "Encuesta aleatoria", "Georreferenciación satelital", "Los vecinos marcan sus percepciones en un plano, que es un mapeo participativo."),
        ("abc", "{F} ¿Qué dato falta en la pauta de observación para repetirla en otro momento?", "La fecha y la hora del registro", "El color de las bancas", "El nombre de cada vecino", "Sin fecha y hora no se pueden comparar registros."),
        ("abc", "{F} Los puntos rojos se concentran en una esquina sin iluminación. ¿Qué conviene hacer?", "Contrastar con datos y visitar la esquina para observar, acompañados por una persona adulta", "Concluir que esa esquina es peligrosa sin más análisis", "Descartar los puntos rojos", "Las percepciones se contrastan con observaciones y otros datos."),
        ("abc", "{F} Un estudiante dice: «El tamaño del dibujo de la plaza muestra que mide más que la calle». ¿Qué error comete?", "Confunde la importancia que le da la persona con el tamaño real", "No sabe dibujar", "Usó mal la pauta", "El tamaño en un mapa mental refleja significado, no medida."),
        ("{F} Explica por qué el mapeo participativo es una fuente de conocimiento válida aunque no sea una medición.", "Porque quienes viven en el lugar conocen sus usos y riesgos y su experiencia complementa los datos", "Los saberes locales entregan información que los instrumentos no captan."),
        ("abc", "{F} ¿Qué regla de seguridad se debe respetar al hacer trabajo de campo?", "Ir acompañado de una persona adulta, en lugares seguros y con permiso", "Ir solo para terminar más rápido", "Entrar a propiedades privadas", "La seguridad y el permiso son condiciones del trabajo en terreno."),
        ("abc", "{F} Tres mapas mentales muestran lugares distintos como importantes. ¿Qué conclusión es válida?", "Que distintas personas viven y valoran el mismo barrio de modos diferentes", "Que los tres mapas son erróneos", "Que el barrio no tiene plaza", "Los mapas mentales muestran perspectivas, no errores."),
    ],
    ctx=("abc", "Un colegio ficticio quiere decidir dónde poner una nueva ciclovía. Tiene un mapa técnico y un mapeo participativo de los vecinos. ¿Qué conviene hacer?", "Combinar el mapa técnico con las marcas de los vecinos y visitar el lugar", "Usar solo el mapa técnico", "Usar solo las marcas de los vecinos", "Los datos técnicos y los saberes locales se complementan."),
    sc=[
        ("En Geografía: ¿qué es el trabajo de campo?", "La observación y el registro de información en el terreno", "Se hace con pauta, permiso y acompañamiento."),
        ("¿Qué es un mapeo participativo?", "Una técnica en que las personas marcan en un plano sus saberes y percepciones del territorio", "Reconoce a los habitantes como fuente de conocimiento."),
        ("¿Qué muestra el tamaño de un lugar en un mapa mental?", "La importancia que le da la persona", "El tamaño dibujado no muestra el tamaño real del lugar."),
    ],
    op=("Prepara en papel una pauta de observación de cinco elementos para recorrer una calle de tu barrio o de un lugar ficticio descrito por tu docente (por ejemplo: árboles, bancas, rampas, locales abiertos, luminarias). Incluye lugar, fecha, hora y una regla de seguridad. "
        "Con datos de ejemplo que inventes (por ejemplo, 12 locales abiertos y 4 cerrados), calcula un porcentaje, y dibuja un mapa mental de ese lugar con tres elementos, explicando por qué elegiste su tamaño.",
        "Pauta: árboles, bancas, rampas, locales abiertos y luminarias. Lugar: calle ficticia; fecha y hora de ejemplo. Seguridad: ir acompañado. Datos: 12 abiertos y 4 cerrados: 12 ÷ 16 × 100 = 75 % abiertos. Mapa mental: plaza grande porque es el lugar de encuentro.",
        ["la pauta tiene cinco elementos, lugar, fecha, hora y regla de seguridad", "calcula bien un porcentaje con los datos de ejemplo", "dibuja un mapa mental con tres elementos", "explica el tamaño como importancia y no como medida"],
        ["pauta, cálculo y mapa mental con una explicación"],
        ["no incluir regla de seguridad", "confundir tamaño real con importancia", "olvidar la fecha y la hora"],
        "Pregunta: «¿cómo repetirías la observación para comparar?». Si no sabe, pídele que revise lo que anotó de lugar, fecha y hora."),
    reinforce="Haz un mapa mental de tu barrio con cinco lugares y explica por qué elegiste el tamaño de cada uno.",
    extend="Con permiso y acompañamiento, recorre una cuadra de tu barrio con una pauta de tres elementos y compara los resultados con los de un compañero.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (datos de ejemplo de un trabajo de campo ficticio sobre el uso de una plaza en El Sauzal). Personas contadas por un grupo de estudiantes en la plaza durante una hora en cuatro momentos del mismo día: de 9 a 10 horas, 6; de 12 a 13 horas, 14; de 16 a 17 horas, 22; de 19 a 20 horas, 8. "
     "Alternativas para comunicar el resultado: (1) un gráfico de barras con un eje que parte de cero; (2) un gráfico de barras con un eje que parte en 5; (3) una tabla con los cuatro valores; (4) un párrafo sin cifras que diga «la plaza se usa mucho». Fuente: conteo de ejemplo del grupo. Límite: un solo día de la semana.")
build(
    O6, 5, F,
    use="Aprenderé a sistematizar datos en tablas y gráficos, a elegir la mejor forma de comunicar un resultado y a redactar una conclusión que indique fuente, método y límites, evitando representaciones engañosas.",
    prior=["Tabulo respuestas y calculo porcentajes.", "Leo mapas, coordenadas y encuestas.", "Sé que toda fuente tiene límites."],
    explain=[
        "Sistematizar es ordenar la información recogida para analizarla: se cuenta, se agrupa en una tabla, se calculan totales y porcentajes y se busca el valor mayor, el menor y los cambios. Recién entonces se comunica. Un buen informe indica la pregunta, el método (qué se hizo, dónde y cuándo), los resultados, la conclusión, la fuente y los límites.",
        "La forma de comunicar importa. Una tabla entrega los valores exactos. Un gráfico de barras compara categorías. Un gráfico de líneas muestra cambios en el tiempo. Un mapa muestra dónde ocurre algo. Un texto explica y relaciona. Un gráfico engaña si el eje no parte de cero en barras, si no tiene unidades o título, o si omite la fuente. Las cifras deben poder revisarse.",
        "Evaluar alternativas de comunicación es preguntar qué forma muestra mejor el mensaje sin distorsionarlo, para qué público y con qué límites. También se cuida la ética: no se identifica a las personas, se reconoce lo que no se midió y se evita generalizar más allá de los datos. Comunicar bien es dar a otros la posibilidad de revisar y discutir.",
    ],
    vocab=[("sistematizar", "ordenar la información recogida para analizarla"), ("gráfico de barras", "gráfico que compara categorías con barras proporcionales"), ("gráfico de líneas", "gráfico que muestra cambios en el tiempo"), ("eje truncado", "eje que no parte de cero y exagera diferencias"), ("fuente y límites", "origen de los datos y aquello que no pueden mostrar")],
    worked=[
        ("Elegir un gráfico", "Un grupo ficticio quiere mostrar cómo cambió el número de visitantes de un museo de enero a abril. ¿Qué gráfico conviene?",
         ["Se trata de un cambio en el tiempo.", "El gráfico de líneas muestra el cambio mes a mes."],
         "Un gráfico de líneas"),
        ("Detectar un gráfico engañoso", "Un gráfico ficticio de barras muestra 52 y 56 personas, pero su eje parte en 50, y la segunda barra parece tres veces más alta. ¿Qué falla?",
         ["Con eje desde 50 se comparan 2 y 6, no 52 y 56.", "La diferencia real es pequeña."],
         "El eje truncado exagera la diferencia"),
    ],
    mistakes=[("Elegir un gráfico por lo vistoso sin pensar en el mensaje.", "Se prioriza el aspecto sobre la claridad.", "Elige la forma que muestre mejor el mensaje sin distorsionarlo."),
              ("Presentar conclusiones sin indicar fuente, método ni límites.", "Se impide que otros revisen la evidencia.", "Incluye siempre fuente, método y límites en tu informe.")],
    T=[
        ("abc", "{F} ¿En qué momento se contó la mayor cantidad de personas?", "De 16 a 17 horas", "De 9 a 10 horas", "De 19 a 20 horas", "El conteo más alto es 22 personas, de 16 a 17 horas."),
        ("=", "{F} ¿Cuántas personas se contaron en total en los cuatro momentos?", "6+14+22+8", "Se suman los cuatro conteos.", " personas"),
        ("En Geografía: ¿cómo se llama el eje de un gráfico de barras que no parte de cero y exagera las diferencias?", "Eje truncado", "Ese eje que no parte de cero se llama eje truncado."),
        ("=", "{F} ¿Cuántas personas más se contaron de 16 a 17 horas que de 9 a 10 horas?", "22-6", "Se resta el valor menor al mayor.", " personas"),
        ("=", "{F} ¿Qué porcentaje del total de personas contadas corresponde al momento de mayor uso? El total es 50.", "22*100//50", "Se divide el mayor conteo entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué alternativa de comunicación exagera las diferencias?", "El gráfico de barras con el eje que parte en 5", "La tabla con los cuatro valores", "El gráfico de barras con el eje desde cero", "Si el eje parte en 5, las barras no son proporcionales a los valores."),
        ("abc", "{F} ¿Qué alternativa carece de datos que permitan revisar?", "El párrafo sin cifras", "La tabla", "El gráfico desde cero", "Decir «se usa mucho» sin cifras impide comprobar la afirmación."),
        ("abc", "{F} ¿Qué gráfico compara mejor los cuatro momentos del día?", "El gráfico de barras con el eje desde cero", "Un mapa de calor del país", "Un dibujo sin cifras", "Las barras desde cero comparan categorías de forma honesta."),
        ("abc", "{F} ¿Qué límite debe declarar el grupo?", "Que los datos corresponden a un solo día de la semana", "Que la plaza es pequeña", "Que hay muchos árboles", "La ficha declara que se contó un solo día."),
        ("abc", "{F} Un estudiante concluye: «La plaza se usa más por la tarde en todos los días y barrios». ¿Qué corrección es más precisa?", "En ese día, en esa plaza, se contó más gente por la tarde", "Tiene razón: se usa más por la tarde siempre", "No se puede concluir nada", "Una conclusión situada se limita al lugar y al día observados."),
        ("{F} Explica por qué la tabla puede ser mejor que el texto para comunicar este resultado.", "Porque entrega los valores exactos y permite revisarlos y compararlos", "Las cifras exactas permiten comprobar y discutir la afirmación."),
        ("abc", "{F} Si el grupo quiere mostrar cómo cambia el uso durante el día, ¿qué conviene usar además de la tabla?", "Un gráfico de líneas o de barras con eje desde cero", "Un gráfico de barras sin título ni unidades", "Una fotografía de la plaza vacía", "Estos gráficos muestran la variación entre momentos del día."),
        ("abc", "{F} ¿Qué estructura debería tener el informe final del grupo?", "Pregunta, método, resultados, conclusión, fuente y límites", "Solo una conclusión", "Una opinión sin datos", "Esa estructura permite revisar y discutir el trabajo."),
    ],
    ctx=("abc", "Un grupo ficticio debe presentar a la junta de vecinos el resultado de un conteo de buses por hora en tres esquinas. ¿Qué forma de comunicar es más adecuada?", "Una tabla y un gráfico de barras desde cero, con título, unidades, fuente y límites", "Un gráfico sin título ni unidades", "Un párrafo que diga que pasan muchos buses", "Datos claros y revisables permiten una discusión informada."),
    sc=[
        ("En Geografía: ¿qué es sistematizar la información?", "Ordenarla para analizarla", "Se cuenta, se agrupa en tablas y se calculan totales y porcentajes."),
        ("¿Qué gráfico muestra mejor un cambio a lo largo del tiempo?", "Un gráfico de líneas", "La línea une los valores en orden temporal."),
        ("¿Qué debe incluir siempre un informe sobre sus datos?", "La fuente, el método y los límites", "Así otras personas pueden revisar y discutir el trabajo."),
    ],
    op=("Usa los datos de ejemplo de una huerta escolar ficticia: producción de lechugas por mes: marzo 20; abril 40; mayo 60; junio 30; la fuente es el registro del curso, con un mes de datos por columna. "
        "Haz una tabla, calcula el total y el porcentaje del mes de mayor producción, elige y dibuja un tipo de gráfico (justifica la elección), y escribe una conclusión de tres líneas con la fuente y un límite.",
        "Total: 20 + 40 + 60 + 30 = 150. Mayo: 60 ÷ 150 × 100 = 40 %. Gráfico de barras desde cero (compara meses). Conclusión: en la huerta escolar, la producción fue mayor en mayo. Fuente: registro del curso. Límite: solo cuatro meses de datos.",
        ["la tabla y el total son correctos", "elige y justifica un tipo de gráfico", "el eje parte de cero y tiene título y unidades", "la conclusión indica fuente y límite"],
        ["tabla, cálculo, gráfico dibujado y una conclusión de tres líneas"],
        ["usar un eje que no parte de cero", "no declarar la fuente", "concluir más allá de los datos"],
        "Pregunta: «¿qué pasaría con la conclusión si hubiera datos de otro año?». Si no lo piensa, pídele que revise el límite."),
    reinforce="Con tres datos de tu vida diaria (por ejemplo, minutos de caminata por día), haz una tabla y un gráfico de barras desde cero.",
    extend="Revisa un gráfico de una noticia y anota si tiene título, unidades, fuente y eje desde cero; si falta algo, escribe cómo lo corregirías.",
)
