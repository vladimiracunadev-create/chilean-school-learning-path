"""Biología celular y molecular (electivo 3.º y 4.º medio HC): OAC-06 (desarrollo del conocimiento en Chile y el mundo; ciencia, tecnología y sociedad, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los proyectos, instituciones, tablas y cifras de los ejercicios son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas internet. "
             "Los datos sobre personas e instituciones reales se limitan a hechos generales muy conocidos; para profundizar, tu docente o tu biblioteca te darán fuentes actualizadas y verificables. "
             "En los debates se presentan posturas con sus argumentos, sin tomar partido político, y se respeta a las personas con distintas opiniones.")
build = make_build(MATERIALS)

O6 = "CN-BCMO-3y4-OAC-06"

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (cuatro proyectos de investigación de ejemplo, inventados). Proyecto 1: estudia cómo las células de una planta de altura regulan sus genes frente al frío. "
     "Proyecto 2: compara los genomas de bacterias que viven en ambientes extremos. Proyecto 3: investiga cómo una proteína de la membrana de neuronas transporta un ion. "
     "Proyecto 4: desarrolla un método para detectar el ARN de un virus y apoyar el diagnóstico. "
     "Tipos de investigación: básica, busca comprender un fenómeno sin una aplicación inmediata; aplicada, busca resolver un problema práctico.")
build(
    O6, 1, F,
    use="Aprenderé a distinguir líneas de investigación en biología celular y molecular y a diferenciar la investigación básica de la aplicada. Sirve para delimitar una pregunta sobre el desarrollo del conocimiento en Chile y el mundo.",
    prior=["Conozco los contenidos de las unidades anteriores.", "Sé qué es una pregunta de investigación.", "Sé que la ciencia se hace en equipo."],
    explain=[
        "El conocimiento de la biología celular y molecular se desarrolla en muchas líneas de investigación. Algunas estudian la estructura y función de las proteínas, otras la regulación de los genes, otras comparan genomas (genómica), otras los procesos de las neuronas, y otras desarrollan métodos de diagnóstico y de producción biotecnológica. Todas usan los mismos conceptos básicos: biomoléculas, membranas, dogma central y regulación.",
        "La investigación básica busca comprender cómo funciona algo, sin una aplicación inmediata. La investigación aplicada busca resolver un problema práctico, como un método de diagnóstico. No son mundos separados: lo que se aprende en la básica suele fundar lo aplicado, y los problemas de lo aplicado generan nuevas preguntas para lo básico. La tecnología es el conjunto de métodos e instrumentos que resultan del conocimiento y que, a su vez, permiten nuevas investigaciones.",
        "En Chile y en el mundo, las investigaciones se realizan en universidades, institutos y empresas, y suelen apoyarse en cooperación entre equipos de distintos países. Para analizar el desarrollo del conocimiento se parte por delimitar una pregunta: qué línea, qué lugar y qué período. Por ejemplo: «¿cómo se relacionan la investigación básica y la aplicada en el estudio de microorganismos de ambientes extremos?».",
    ],
    vocab=[("línea de investigación", "tema o conjunto de preguntas relacionadas que un equipo estudia"), ("investigación básica", "busca comprender un fenómeno sin aplicación inmediata"), ("investigación aplicada", "busca resolver un problema práctico"), ("tecnología", "métodos e instrumentos que resultan del conocimiento científico"), ("genómica", "estudio de los genomas completos")],
    worked=[
        ("Clasificar un proyecto", "El proyecto 4 desarrolla un método para detectar el ARN de un virus. ¿Es básica o aplicada?",
         ["Busca resolver un problema práctico: apoyar un diagnóstico.", "Eso corresponde a la investigación aplicada."],
         "Aplicada"),
        ("Relacionar con una unidad", "El proyecto 3 estudia una proteína de membrana que transporta un ion. ¿Con qué contenido del curso se relaciona?",
         ["Una proteína de membrana que transporta un ion es un canal o una bomba.", "Eso se estudió en la relación entre estructura y función de proteínas."],
         "Estructura y función de proteínas de membrana"),
    ],
    mistakes=[("Pensar que la investigación básica no sirve.", "Aporta el conocimiento sobre el que se construyen muchas aplicaciones.", "Describe la básica como base de lo aplicado."),
              ("Creer que la ciencia la hace una persona sola en un laboratorio.", "Se hace en equipos y redes de cooperación.", "Habla de equipos, instituciones y cooperación.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es la investigación básica?", "La que busca comprender un fenómeno sin aplicación inmediata", "La que solo hacen los principiantes", "La que desarrolla productos para vender", "La investigación básica busca comprender, no resolver un problema práctico inmediato."),
        ("{F} ¿Qué proyecto (1, 2, 3 o 4) compara los genomas de bacterias?", "Proyecto 2", "El proyecto 2 compara genomas, es decir, hace genómica."),
        ("{F} ¿Qué proyecto desarrolla un método de diagnóstico?", "Proyecto 4", "El proyecto 4 busca detectar el ARN de un virus para apoyar el diagnóstico."),
        ("abc", "{F} ¿Qué proyecto se relaciona con la regulación de los genes?", "El proyecto 1, sobre la respuesta al frío", "El proyecto 4, sobre diagnóstico", "Ninguno", "Regular genes frente al frío es regulación génica."),
        ("ab", "{F} El proyecto 3 estudia una proteína de membrana. ¿Qué tipo de investigación es probablemente?", "Básica, porque busca comprender cómo funciona", "Aplicada, porque ya vende un producto", "Describe un mecanismo, sin una aplicación inmediata."),
        ("Un proyecto de ejemplo quiere comprender cómo se pliega una proteína y no busca una aplicación inmediata. ¿Qué tipo de investigación es?", "Básica", "Comprender un fenómeno sin aplicación inmediata es investigación básica."),
        ("=", "Un centro de ejemplo tiene 24 proyectos: 15 son de investigación básica y el resto de aplicada. ¿Cuántos son de aplicada?", "24-15", "Se resta el número de proyectos básicos del total.", " proyectos"),
        ("=", "Otro centro de ejemplo tiene 20 proyectos y 15 son de investigación básica. ¿Qué porcentaje de sus proyectos es de investigación básica?", "15*100/20", "Se divide 15 entre 20 y se multiplica por 100 para obtener el porcentaje.", " %"),
        ("abc", "{F} El proyecto 2 estudia bacterias de ambientes extremos. ¿Qué podría aportar a una aplicación futura?", "Descubrir proteínas que funcionen en condiciones extremas", "Nada, porque las bacterias extremas no tienen proteínas", "Que todas las bacterias sean peligrosas", "El conocimiento básico puede dar origen a aplicaciones imprevistas."),
        ("abc", "{F} Un periodista dice: «la investigación básica es un gasto inútil». ¿Qué respuesta es más razonable?", "La básica genera conocimiento que luego se usa en aplicaciones", "Tiene razón en todo", "La básica es siempre más barata", "Muchas aplicaciones se apoyaron en conocimiento básico previo."),
        ("ab", "Una pregunta de investigación bien delimitada sobre el tema de la ficha es:", "¿Cómo se relaciona el estudio básico de bacterias extremas con aplicaciones biotecnológicas?", "¿Qué pasa en la ciencia?", "La primera indica el sistema, la relación y el alcance de la pregunta."),
        ("abc", "{F} ¿Cómo se llama el estudio de genomas completos, como el que hace el proyecto 2?", "Genómica", "Mitosis", "Desnaturalización", "Comparar genomas completos es hacer genómica."),
        ("abc", "{F} Los proyectos 1, 2 y 3 podrían compartir datos con equipos de otros países. ¿Por qué esto es útil?", "Porque se comparan resultados y se avanza más rápido", "Porque así ya no hace falta revisar los resultados", "Porque no es posible", "La cooperación permite contrastar resultados y compartir métodos."),
    ],
    ctx=("abc", "Contexto: tu curso visitará una universidad y debe preparar una pregunta sobre cómo se desarrolla la investigación en biología celular en Chile. ¿Cuál es la pregunta mejor delimitada?", "¿Qué líneas de investigación en biología celular y molecular se desarrollan en esta universidad y qué preguntas estudian?", "¿Qué es la ciencia?", "¿Cuánto cuesta un laboratorio?", "La mejor pregunta nombra el lugar, la disciplina y el aspecto que se quiere conocer."),
    sc=[
        ("En Biología celular y molecular: ¿qué es la investigación aplicada?", "La que busca resolver un problema práctico", "Se orienta a resolver una necesidad concreta."),
        ("ab", "La genómica estudia:", "Genomas completos", "Solo proteínas", "Genómica viene de genoma, el conjunto de genes."),
        ("ab", "La investigación se realiza en:", "Equipos e instituciones", "Solo individuos aislados", "La ciencia es un trabajo colectivo."),
    ],
    op=("Con los proyectos de la ficha {F}: (1) clasifica cada proyecto como básico o aplicado; (2) relaciona cada uno con un contenido del curso; (3) escribe una pregunta de investigación bien delimitada que combine dos de los proyectos.",
        "(1) 1 básico, 2 básico, 3 básico, 4 aplicado. (2) 1 regulación génica; 2 genomas y evolución; 3 proteínas de membrana; 4 dogma central (ARN). (3) ¿Cómo pueden las proteínas de bacterias extremas servir para un método de diagnóstico?",
        ["clasificación coherente", "relación con contenidos del curso", "pregunta bien delimitada con dos proyectos"],
        ["tres respuestas numeradas"],
        ["clasificar mal por el nombre", "relacionar con un contenido que no corresponde", "pregunta demasiado amplia"],
        "Pregunta: «¿qué dato necesitarías para saber si tu pregunta se puede responder?»."),
    reinforce="Escribe una oración que diferencie investigación básica y aplicada con un ejemplo inventado de cada una.",
    extend="Explica por qué la tecnología es a la vez un resultado de la ciencia y una herramienta para nuevas investigaciones.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (datos de ejemplo; el centro, las fuentes y las cifras son inventados). Centro de biología celular de ejemplo: publicaciones por año: año 1: 12; año 2: 18; año 3: 24; año 4: 30. Personas investigadoras en el centro: año 1: 6; año 4: 10. "
     "Fuentes sobre un mismo hallazgo de ejemplo. Fuente 1: artículo en una revista científica con revisión por pares, es decir, evaluado por especialistas independientes antes de publicarse, que incluye métodos y datos. "
     "Fuente 2: comunicado de prensa del propio centro. Fuente 3: publicación anónima en una red social que afirma que el hallazgo «cura todo».")
build(
    O6, 2, F,
    use="Aprenderé a evaluar fuentes sobre ciencia y a interpretar indicadores como la cantidad de publicaciones, distinguiendo cantidad de calidad y correlación de causalidad. Sirve para analizar cómo se desarrolla el conocimiento sin dejarse llevar por afirmaciones exageradas.",
    prior=["Sé qué es una fuente primaria y una secundaria.", "Sé calcular promedios y porcentajes.", "Sé qué es una variable."],
    explain=[
        "La ciencia se comunica en artículos publicados en revistas científicas. Muchas aplican la revisión por pares: especialistas independientes evalúan el trabajo antes de publicarlo. Esto no garantiza que sea perfecto, pero filtra errores evidentes. Un artículo incluye métodos, datos y limitaciones. Un comunicado de prensa, en cambio, resume y destaca lo positivo, y una publicación anónima en redes sociales no ofrece datos ni responsabilidad.",
        "Para evaluar el desarrollo del conocimiento se usan indicadores, como el número de publicaciones de un centro o de personas investigadoras. Pero cada indicador tiene límites: más publicaciones no siempre significa más calidad, y al comparar centros de distinto tamaño conviene usar proporciones, por ejemplo publicaciones por persona investigadora. Además, que dos variables suban juntas no prueba que una cause la otra: es una correlación, y puede haber una tercera causa.",
        "Una buena evaluación hace tres cosas: identifica quién habla y con qué datos, calcula indicadores comparables y declara qué no se puede concluir. También reconoce la incertidumbre: los resultados científicos se expresan con límites, no como verdades absolutas.",
    ],
    vocab=[("revisión por pares", "evaluación de un trabajo por especialistas independientes antes de publicarlo"), ("indicador", "dato que resume un aspecto, como el número de publicaciones"), ("correlación", "relación en la que dos variables varían juntas"), ("causalidad", "relación en que una variable produce cambios en otra"), ("incertidumbre", "margen de duda que acompaña a un resultado")],
    worked=[
        ("Calcular un indicador comparable", "En el año 1 había 12 publicaciones y 6 personas. ¿Cuántas publicaciones por persona?",
         ["Se divide el número de publicaciones por el de personas.", "12 ÷ 6 = 2."],
         "2 publicaciones por persona"),
        ("Distinguir correlación y causalidad", "Subieron las publicaciones y también el número de personas. ¿Se puede decir que más personas causaron más publicaciones?",
         ["Ambas variables aumentaron a la vez: hay correlación.", "No se ha mostrado que una cause la otra: puede haber otros factores, como más financiamiento."],
         "No se puede afirmar la causalidad solo con esos datos"),
    ],
    mistakes=[("Suponer que más publicaciones significa mejor ciencia.", "La cantidad no mide la calidad ni el impacto.", "Complementa con la revisión de los métodos y la calidad."),
              ("Comparar centros de distinto tamaño solo con totales.", "Un centro grande publica más aunque cada persona publique menos.", "Calcula una proporción, como publicaciones por persona.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es la revisión por pares?", "La evaluación de un trabajo por especialistas independientes antes de publicarlo", "La revisión que hace el autor de su propio trabajo", "La aprobación de la prensa", "La revisión por pares filtra errores antes de la publicación."),
        ("{F} ¿Cuántas publicaciones tuvo el centro en el año 3?", "24", "La ficha indica 24 publicaciones en el año 3."),
        ("{F} ¿Cuántas personas investigadoras tenía el centro en el año 4?", "10", "La ficha indica 10 personas en el año 4."),
        ("abc", "{F} ¿Cuál de las fuentes ofrece métodos y datos para evaluar el hallazgo?", "La fuente 1, el artículo de la revista", "La fuente 2, el comunicado", "La fuente 3, la publicación anónima", "El artículo con revisión por pares presenta métodos y datos."),
        ("ab", "{F} ¿Por qué conviene desconfiar de la fuente 3, que afirma que el hallazgo «cura todo»?", "Porque no ofrece datos y exagera", "Porque está escrita en un lugar muy visitado", "Una afirmación absoluta y sin datos no permite evaluar nada."),
        ("{F} ¿Qué tipo de fuente es el comunicado de prensa del propio centro?", "Una fuente que resume y destaca lo positivo, por lo que conviene contrastarla con el artículo", "Un comunicado resume y selecciona información del hallazgo."),
        ("=", "{F} ¿Cuántas publicaciones más hubo en el año 4 que en el año 1?", "30-12", "Se resta el número de publicaciones del año 1 al del año 4.", " publicaciones"),
        ("=", "{F} ¿Cuántas publicaciones por persona hubo en el año 4?", "30/10", "Se divide el número de publicaciones por el de personas investigadoras.", " por persona"),
        ("abc", "{F} Entre el año 1 y el año 4 las publicaciones por persona subieron. ¿Qué indica?", "Que cada persona publicó más, en promedio", "Que bajó la productividad", "Que no hay cambios", "El indicador por persona subió de 2 en el año 1 a 3 en el año 4."),
        ("abc", "{F} Un periodista dice: «como subieron las personas y las publicaciones, contratar más personas causa más publicaciones». ¿Qué falta?", "Mostrar que no hay otros factores, como más financiamiento", "Nada, está probado", "Contratar menos personas", "Con una sola correlación no se prueba la causalidad."),
        ("ab", "{F} Se quiere comparar el centro con otro centro mucho más grande. ¿Qué indicador es más justo?", "Publicaciones por persona investigadora", "Total de publicaciones", "Un centro grande publica más por tamaño; la proporción permite comparar."),
        ("abc", "{F} El comunicado de prensa dice que el hallazgo «cambiará la medicina». ¿Qué haces antes de aceptarlo?", "Revisar el artículo de la revista y sus limitaciones", "Compartirlo de inmediato", "Ignorar todos los artículos", "Una afirmación fuerte requiere revisar métodos y datos en la fuente primaria."),
        ("abc", "{F} ¿Qué significa que un resultado tenga incertidumbre?", "Que se expresa con un margen de duda", "Que es falso", "Que no se puede usar", "Reconocer el margen de duda es parte honesta de la ciencia."),
    ],
    ctx=("abc", "Contexto: tu grupo prepara un informe breve sobre «cuánto crece la investigación en un centro». ¿Qué incluyes para que sea justo?", "Publicaciones por persona, además del total, y una nota sobre los límites", "Solo el total más alto", "Una opinión sin datos", "El informe justo usa proporciones y declara límites."),
    sc=[
        ("En Biología celular y molecular: ¿qué es un indicador?", "Un dato que resume un aspecto, como el número de publicaciones", "Los indicadores resumen en un dato un aspecto que se puede medir."),
        ("ab", "Correlación significa:", "Dos variables varían juntas", "Una causa a la otra siempre", "Que dos variables varíen juntas no prueba que una cause la otra."),
        ("ab", "La mejor fuente para evaluar un hallazgo suele ser:", "Un artículo con revisión por pares", "Un mensaje anónimo", "Los artículos entregan métodos y datos revisables."),
    ],
    op=("Con la ficha {F}: (1) calcula las publicaciones por persona de los años 1 y 4; (2) ordena las tres fuentes de más a menos confiable y explica en una frase por qué; (3) escribe una afirmación que no se pueda concluir con esos datos.",
        "(1) Año 1: 2; año 4: 3. (2) Fuente 1, fuente 2, fuente 3: la primera ofrece métodos y datos; la segunda resume; la tercera no da datos. (3) Que contratar más personas causó el aumento de publicaciones.",
        ["cálculos correctos", "orden con justificación", "afirmación que no se puede concluir"],
        ["tres respuestas numeradas"],
        ["no dividir por el número de personas", "ordenar por el tono y no por los datos", "afirmar causalidad sin evidencia"],
        "Pregunta: «¿qué dato adicional necesitarías para saber si la calidad aumentó?»."),
    reinforce="Escribe dos preguntas que harías a cualquier noticia científica antes de compartirla.",
    extend="Explica por qué dos centros con el mismo número de publicaciones pueden tener un impacto muy distinto.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (modelo de ejemplo de las relaciones entre ciencia, tecnología y sociedad). Ciclo: conocimiento científico → tecnología (métodos e instrumentos) → aplicación en la sociedad → nuevas preguntas y nuevas necesidades → nuevo conocimiento. "
     "Ejemplos del ciclo: el microscopio permitió observar células y formular la teoría celular; la comprensión del ARN mensajero y de la traducción permitió pensar en vacunas que usan un ARN mensajero para enseñar al cuerpo a reconocer una proteína de un virus; la secuenciación de genomas generó grandes bases de datos y nuevas preguntas. "
     "Tiempos de ejemplo entre un descubrimiento básico y su aplicación en tres casos inventados: caso 1: 12 años; caso 2: 20 años; caso 3: 4 años.")
build(
    O6, 3, F,
    use="Aprenderé un modelo de cómo se relacionan ciencia, tecnología y sociedad en biología celular y molecular, y cómo usarlo para interpretar casos. Sirve para explicar por qué un descubrimiento puede tardar años en convertirse en una aplicación y cómo la sociedad influye en la investigación.",
    prior=["Conozco la diferencia entre investigación básica y aplicada.", "Sé qué es un modelo.", "Sé calcular un promedio."],
    explain=[
        "Un modelo de ciencia, tecnología y sociedad (CTS) muestra un ciclo: el conocimiento científico permite crear tecnologías; las tecnologías se aplican en la sociedad; la sociedad plantea nuevas necesidades y preguntas; y estas orientan nuevas investigaciones. Por ejemplo, el microscopio, un invento basado en la óptica, permitió ver células y formular la teoría celular, que a su vez generó nuevas preguntas y mejores instrumentos.",
        "Entre un descubrimiento básico y su aplicación suelen pasar muchos años. Hay que comprender el fenómeno, desarrollar tecnologías para usarlo, probar que es seguro y decidir cómo ponerlo al alcance de las personas. Los casos recientes, como las vacunas que usan ARN mensajero, se apoyaron en décadas de conocimiento sobre el ARN, la traducción y los lípidos de membrana, y en el trabajo de equipos de muchos países.",
        "El modelo tiene límites. No siempre el orden es lineal: a veces una tecnología nueva, como la secuenciación, abre preguntas que antes no se podían plantear. Además, las decisiones sobre qué investigar dependen de intereses, financiamiento y valores de la sociedad. Un buen análisis usa el modelo para ordenar un caso y señala dónde el caso no encaja.",
    ],
    vocab=[("ciencia, tecnología y sociedad (CTS)", "enfoque que estudia cómo se influyen mutuamente el conocimiento, las técnicas y la vida social"), ("aplicación", "uso práctico de un conocimiento"), ("ciclo", "secuencia que vuelve a empezar"), ("financiamiento", "recursos que permiten realizar una investigación"), ("base de datos", "conjunto organizado de datos")],
    worked=[
        ("Ubicar un caso en el ciclo", "El microscopio permitió observar células. ¿Qué parte del ciclo representa?",
         ["Es un instrumento creado a partir de la óptica.", "Un instrumento corresponde a la tecnología."],
         "Tecnología"),
        ("Calcular un promedio de tiempos", "Los tres casos tardaron 12, 20 y 4 años. ¿Cuál es el promedio?",
         ["Suma: 12 + 20 + 4 = 36.", "36 ÷ 3 = 12."],
         "12 años"),
    ],
    mistakes=[("Creer que una aplicación llega inmediatamente tras un descubrimiento.", "Suele pasar mucho tiempo y muchas pruebas antes.", "Considera las etapas intermedias y los tiempos."),
              ("Pensar que la sociedad no influye en lo que se investiga.", "El financiamiento, las necesidades y los valores orientan las preguntas.", "Incluye a la sociedad como parte del ciclo.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué muestra un modelo CTS?", "Cómo se influyen mutuamente el conocimiento, la tecnología y la sociedad", "Cómo se divide una célula", "Cómo se transcribe un gen", "El modelo CTS relaciona ciencia, técnica y sociedad."),
        ("{F} ¿Cuál es el primer elemento del ciclo?", "El conocimiento científico", "El ciclo parte del conocimiento científico, que permite crear tecnologías."),
        ("{F} ¿Cuántos años tardó el caso 2 entre descubrimiento y aplicación?", "20", "La ficha indica 20 años para el caso 2."),
        ("abc", "{F} ¿Qué parte del ciclo representa una vacuna basada en ARN mensajero que se aplica a las personas?", "La aplicación en la sociedad", "El conocimiento científico básico", "Una nueva pregunta", "Su uso por las personas es la aplicación."),
        ("ab", "{F} La secuenciación de genomas generó grandes bases de datos. ¿Qué parte del ciclo muestra?", "Nuevas preguntas y necesidades que surgen de una tecnología", "Una aplicación sin tecnología previa", "Los datos y preguntas nuevas son un resultado que reabre la investigación."),
        ("{F} ¿Qué instrumento permitió formular la teoría celular, según la ficha?", "El microscopio", "La ficha señala que el microscopio permitió observar células y formular la teoría celular."),
        ("=", "Otros tres casos de ejemplo tardaron 6, 10 y 14 años. ¿Cuál es el promedio de tiempos?", "(6+10+14)/3", "El promedio suma los tiempos y divide por la cantidad de casos.", " años"),
        ("=", "{F} ¿Cuántos años más tardó el caso 2 que el caso 3?", "20-4", "Se resta el tiempo del caso más corto al del más largo.", " años"),
        ("abc", "{F} Un estudiante dice: «el caso 3 prueba que cualquier descubrimiento se aplica en 4 años». ¿Qué corriges?", "Un solo caso corto no representa a todos; los tiempos varían mucho", "Tiene razón en todo", "Los tiempos nunca varían", "Los tres casos tienen 4, 12 y 20 años: hay gran variación."),
        ("abc", "{F} La comprensión del ARN mensajero se apoyó en décadas de trabajo. ¿Qué implica eso para quien evalúa una noticia que dice «se descubrió ayer»?", "Que probablemente se apoya en conocimiento previo acumulado", "Que no hubo trabajo previo", "Que la noticia es falsa", "Las aplicaciones recientes se apoyan en conocimiento previo."),
        ("ab", "{F} ¿Cómo influye la sociedad en el ciclo?", "Plantea necesidades y aporta recursos que orientan nuevas investigaciones", "No influye en nada", "Las necesidades y el financiamiento orientan qué se investiga."),
        ("abc", "{F} ¿Dónde el modelo lineal no calza bien?", "Cuando una tecnología nueva abre preguntas antes imposibles, invirtiendo el orden", "Cuando se usa un microscopio", "Cuando se publica un artículo", "A veces la tecnología precede a la pregunta científica."),
        ("abc", "Un buen análisis con el modelo debe:", "Ordenar el caso y señalar dónde no encaja", "Ocultar lo que no calza", "Evitar los datos", "El modelo se usa de forma crítica, reconociendo sus límites."),
    ],
    ctx=("abc", "Contexto: en una conversación familiar alguien dice que «la ciencia básica es una pérdida de tiempo porque no cura a nadie». ¿Qué argumento usas con el modelo CTS?", "Que muchas aplicaciones surgen de conocimiento básico acumulado durante años", "Que tienen razón en todo", "Que la ciencia básica no se relaciona con nada", "El ciclo muestra que la aplicación depende del conocimiento previo."),
    sc=[
        ("En Biología celular y molecular: ¿qué es una aplicación?", "El uso práctico de un conocimiento", "Una aplicación lleva el conocimiento a la vida práctica."),
        ("ab", "Entre descubrimiento y aplicación suelen pasar:", "Varios años", "Pocos minutos", "Hay etapas de desarrollo y prueba."),
        ("ab", "La sociedad en el ciclo:", "Plantea necesidades y aporta recursos", "No participa", "Las necesidades de las personas orientan qué preguntas se investigan."),
    ],
    op=("Con el modelo de la ficha {F}: (1) ordena en el ciclo los cuatro elementos y escribe un ejemplo de cada uno; (2) calcula el promedio de tiempos de los tres casos y explica por qué el promedio oculta la variación; (3) escribe un caso del ciclo en que la tecnología haya abierto una pregunta nueva.",
        "(1) Conocimiento: teoría celular; tecnología: microscopio; aplicación: uso del microscopio en laboratorios para estudiar tejidos; nuevas preguntas: ¿qué hay dentro de la célula? (2) 12 años; oculta que hubo casos de 4 y de 20. (3) La secuenciación de genomas abrió preguntas sobre el papel de cada gen.",
        ["ciclo ordenado con ejemplos", "promedio correcto y explicación de la variación", "caso de tecnología que abre preguntas"],
        ["tres respuestas numeradas"],
        ["ordenar mal el ciclo", "calcular mal el promedio", "no explicar la variación"],
        "Pregunta: «¿qué dato extra necesitarías para predecir cuánto tardará una aplicación nueva?»."),
    reinforce="Dibuja el ciclo con cuatro cajas y flechas, y escribe un ejemplo breve en cada caja.",
    extend="Explica cómo el financiamiento y las necesidades de la sociedad pueden hacer que unas líneas de investigación avancen más rápido que otras.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (tres aportes de ejemplo, resumidos; para fechas, cifras y detalles de personas o instituciones reales consulta fuentes verificables con tu docente). "
     "Aporte 1: el biólogo chileno Humberto Maturana, junto con Francisco Varela, propuso la idea de autopoiesis: un ser vivo se define como un sistema que produce y mantiene sus propios componentes. "
     "Aporte 2: grupos de investigación de universidades y centros del país estudian microorganismos de ambientes extremos de la región, como desiertos, alturas y zonas australes. "
     "Aporte 3: a comienzos del siglo XXI, equipos de varios países cooperaron para secuenciar el genoma humano. "
     "Datos de ejemplo de un cuestionario inventado: 60 de 100 estudiantes dicen haber oído hablar de una investigación biológica chilena; 25 de esos 60 pueden nombrar una.")
build(
    O6, 4, F,
    use="Aprenderé a analizar con evidencia aportes al conocimiento de la biología celular y molecular en Chile y en el mundo, distinguiendo lo que muestran los datos de lo que no. Sirve para reconocer que la ciencia chilena participa en redes internacionales y tiene líneas propias.",
    prior=["Sé qué es una fuente primaria y secundaria.", "Sé calcular porcentajes.", "Conozco el modelo CTS."],
    explain=[
        "El conocimiento de la biología celular se desarrolla en Chile y en el mundo. En Chile hay investigadores y centros con líneas propias; por ejemplo, el biólogo Humberto Maturana, con Francisco Varela, propuso la autopoiesis, una idea sobre qué distingue a un sistema vivo: produce y mantiene sus propios componentes. Otros grupos del país estudian microorganismos de ambientes extremos, que ofrecen oportunidades por su diversidad.",
        "A escala mundial, grandes proyectos de cooperación, como la secuenciación del genoma humano a comienzos del siglo XXI, reunieron a equipos de distintos países. Nadie puede hacer solo un proyecto de ese tamaño. Estos esfuerzos generan datos abiertos que luego usan muchos grupos, incluidos grupos chilenos.",
        "Al analizar evidencia sobre estos aportes conviene separar tres cosas: qué se afirma, con qué fuente y qué no se puede concluir. Por ejemplo, un cuestionario muestra cuánto conoce un grupo de estudiantes, no cuánta ciencia se hace. Las cifras de este cuaderno son de ejemplo; los datos reales y actualizados se buscan en fuentes verificables.",
    ],
    vocab=[("autopoiesis", "idea de que un sistema vivo produce y mantiene sus propios componentes"), ("ambiente extremo", "lugar con condiciones muy exigentes para la vida, como desierto o altura"), ("cooperación internacional", "trabajo conjunto de equipos de varios países"), ("datos abiertos", "datos disponibles para que otros equipos los usen"), ("cuestionario", "conjunto de preguntas para recoger información")],
    worked=[
        ("Calcular un porcentaje", "De 100 estudiantes, 60 han oído de una investigación chilena. ¿Qué porcentaje es?",
         ["60 de 100 es 60 de cada 100.", "Es 60 %."],
         "60 %"),
        ("Leer los límites de un cuestionario", "El cuestionario dice que 25 de 60 pueden nombrar una investigación. ¿Qué no permite concluir?",
         ["Mide el conocimiento de un grupo de 100 estudiantes.", "No mide cuánta investigación se hace ni su calidad."],
         "No permite concluir sobre la cantidad o calidad de la investigación"),
    ],
    mistakes=[("Usar el cuestionario como si midiera la calidad de la ciencia chilena.", "Mide lo que conoce un grupo, no la investigación.", "Declara qué mide el instrumento y qué no."),
              ("Dar fechas y cifras de memoria sin fuente.", "Pueden estar equivocadas.", "Consulta fuentes verificables antes de afirmarlas.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué propone la idea de autopoiesis?", "Que un sistema vivo produce y mantiene sus propios componentes", "Que los seres vivos no tienen células", "Que el ADN no tiene función", "La autopoiesis define lo vivo por su automantención."),
        ("{F} ¿Cuántos estudiantes de los 100 dicen haber oído hablar de una investigación chilena?", "60", "La ficha indica 60 de 100."),
        ("{F} ¿Cuántos de esos 60 pueden nombrar una investigación?", "25", "La ficha señala que 25 de esos 60 pueden nombrar una."),
        ("abc", "{F} ¿Qué muestra el aporte 3?", "Que algunos proyectos requieren cooperación de equipos de varios países", "Que ningún país participó", "Que se hizo sin datos", "El proyecto de secuenciación reunió equipos internacionales."),
        ("ab", "{F} Los microorganismos de ambientes extremos son interesantes porque:", "Muestran adaptaciones a condiciones muy exigentes", "Son siempre peligrosos", "Vivir en condiciones extremas obliga a adaptaciones que pueden estudiarse."),
        ("{F} ¿Quién propuso la idea de autopoiesis junto con Francisco Varela?", "Humberto Maturana", "La ficha atribuye la autopoiesis a Maturana y Varela."),
        ("=", "{F} ¿Cuántos estudiantes de los 100 no han oído hablar de una investigación chilena?", "100-60", "Se restan los que sí han oído del total del cuestionario.", " estudiantes"),
        ("=", "{F} Si 30 de esos 60 estudiantes pudieran nombrar una investigación, ¿qué porcentaje de los 60 sería?", "30*100/60", "Se divide 30 entre 60 y se multiplica por 100 para obtener el porcentaje.", " %"),
        ("abc", "{F} Un estudiante concluye: «solo se hace poca ciencia en Chile porque solo 25 pueden nombrarla». ¿Qué falla?", "El cuestionario mide el conocimiento del grupo, no la cantidad de ciencia", "Nada: la conclusión es correcta", "El cuestionario mide la calidad", "Un cuestionario sobre lo que conocen no mide la actividad científica."),
        ("abc", "{F} Una compañera cita una fecha de memoria sobre el genoma humano y duda. ¿Qué haces?", "Buscar una fuente verificable antes de usar la fecha", "Usarla de todos modos", "Cambiarla por otra al azar", "Una fecha dudosa debe contrastarse con una fuente verificable."),
        ("ab", "{F} ¿Qué ventaja tienen los datos abiertos de un proyecto como el del genoma?", "Que muchos grupos pueden usarlos para nuevas preguntas", "Que solo un equipo puede usarlos", "Compartir datos permite que otros equipos avancen sin repetir el trabajo."),
        ("abc", "{F} El aporte 2 indica que hay grupos chilenos que estudian ambientes extremos. ¿Qué pregunta se puede formular con ese aporte?", "¿Qué adaptaciones tienen esos microorganismos y qué aplicaciones podrían tener?", "¿Cuánto cuesta hoy secuenciar un genoma en Chile?", "¿Quién inventó el microscopio?", "La mejor pregunta se relaciona con el aporte descrito."),
        ("abc", "Alguien dice: «Chile solo copia lo que se hace en el mundo». ¿Qué respuesta, con lo visto, es más justa?", "Hay aportes propios, como la autopoiesis, y también cooperación con redes internacionales", "Tiene razón en todo", "Chile no participa de ninguna red", "La ciencia chilena combina líneas propias con cooperación."),
    ],
    ctx=("abc", "Contexto: tu liceo organiza una semana de la ciencia y debes elegir un afiche sobre ciencia chilena en biología celular. ¿Cuál es el mejor enfoque?", "Presentar líneas de investigación y personas con fuentes verificables, sin exagerar", "Presentar cifras sin fuente", "Destacar solo los logros de otros países", "Un afiche honesto usa fuentes verificables."),
    sc=[
        ("En Biología celular y molecular: ¿qué son datos abiertos?", "Datos disponibles para que otros equipos los usen", "Compartir datos permite que otros equipos hagan nuevas investigaciones."),
        ("ab", "Un cuestionario sobre conocimiento mide:", "Lo que sabe un grupo", "La calidad de la ciencia", "Solo mide lo que contestan las personas."),
        ("ab", "Para afirmar una fecha conviene:", "Verificarla en una fuente confiable", "Decirla de memoria", "Las fechas dudosas se contrastan con fuentes confiables antes de usarlas."),
    ],
    op=("Con la ficha {F}: (1) elige uno de los tres aportes y escribe qué afirma, con qué fuente podrías verificarlo y qué no permite concluir; (2) calcula cuántos de los 60 que han oído hablar de una investigación no pueden nombrar ninguna; (3) propone una pregunta de investigación sobre cómo se conoce la ciencia en tu liceo.",
        "(1) Aporte 2: afirma que hay estudios de ambientes extremos; verificarlo en la página de una universidad; no permite concluir cuánta ciencia se hace en total. (2) De los 60 que han oído hablar, 60 − 25 = 35 no pueden nombrar ninguna. (3) ¿Cuánto conocen mis compañeras y compañeros sobre las investigaciones de su región?",
        ["afirmación, fuente y límite", "resta bien calculada", "pregunta bien delimitada"],
        ["tres respuestas"],
        ["no indicar fuente verificable", "confundir los 60 con los 100 estudiantes", "pregunta demasiado amplia"],
        "Pregunta: «¿qué fuente confiable consultarías primero?»."),
    reinforce="Escribe tres preguntas que harías a un afiche de ciencia chilena antes de aceptar sus datos.",
    extend="Explica por qué la cooperación internacional no resta valor a los aportes propios de un país, sino que los amplía.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (problema local de ejemplo). Una localidad ficticia quiere vigilar la contaminación de su agua con microorganismos. Se comparan dos soluciones con datos inventados. "
     "Método 1, cultivo en laboratorio: costo por muestra 2 unidades; tiempo para el resultado 3 días; detecta pocas especies. "
     "Método 2, detección de ADN: costo por muestra 6 unidades; tiempo para el resultado 1 día; detecta muchas especies. "
     "Se analizarán 50 muestras. Criterios sociales: costo, rapidez, alcance y capacidad local para usar el método.")
build(
    O6, 5, F,
    use="Aprenderé a comparar dos soluciones tecnológicas basadas en el conocimiento molecular a partir de criterios de costo, rapidez, alcance y condiciones locales. Sirve para decidir con argumentos y reconocer el papel de la sociedad en la ciencia y la tecnología.",
    prior=["Conozco el modelo CTS.", "Sé calcular costos y tiempos.", "Sé que una decisión se justifica con criterios."],
    explain=[
        "Un mismo problema puede tener varias soluciones tecnológicas. Compararlas exige elegir criterios claros: costo, rapidez, alcance (qué detectan), seguridad y condiciones locales, como si hay personal y equipos para usarlas. Ninguna solución es perfecta: lo que conviene depende del problema, del lugar y de los recursos.",
        "Para comparar se usan datos y se declaran supuestos. Por ejemplo, si la localidad necesita resultados rápidos para tomar decisiones, el criterio de tiempo pesa más; si el presupuesto es limitado, pesa más el costo. Una tabla de decisión ayuda a ordenar la información, pero la decisión final incluye valores de la comunidad, que no se reducen a números.",
        "Las soluciones basadas en el conocimiento molecular, como detectar el ADN de un microorganismo, nacen de la investigación básica sobre el ADN. Su uso en la sociedad exige además formación de personas, mantenimiento de equipos y reglas para usar los datos de manera responsable. Esta es una forma concreta de ver la relación entre ciencia, tecnología y sociedad.",
    ],
    vocab=[("criterio", "aspecto con el que se juzga una opción"), ("alcance", "qué tan amplio es lo que un método puede detectar"), ("capacidad local", "personas, equipos y recursos disponibles en un lugar"), ("tabla de decisión", "tabla que compara opciones según criterios"), ("supuesto", "condición que se da por cierta para comparar")],
    worked=[
        ("Calcular el costo total", "Con el método 1, ¿cuánto cuestan las 50 muestras?",
         ["Costo por muestra: 2 unidades.", "50 × 2 = 100."],
         "100 unidades"),
        ("Elegir según el criterio", "Si la prioridad absoluta es tener resultados en 1 día, ¿qué método conviene?",
         ["El método 1 tarda 3 días y el 2 tarda 1.", "El criterio de rapidez favorece al método 2."],
         "El método 2"),
    ],
    mistakes=[("Elegir un método por tener el menor costo sin considerar los otros criterios.", "Un método más barato puede no detectar lo que se necesita.", "Compara todos los criterios y explica cuál pesa más."),
              ("Pensar que la decisión solo depende de los datos.", "También depende de los valores y recursos de la comunidad.", "Incluye la capacidad local y las prioridades.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es un criterio de comparación?", "Un aspecto con el que se juzga una opción, como el costo", "Un tipo de microorganismo", "Un instrumento del laboratorio", "Los criterios permiten comparar soluciones de forma ordenada."),
        ("{F} ¿Cuántos días tarda el método 1 en dar un resultado?", "3", "La ficha indica 3 días para el cultivo en laboratorio."),
        ("{F} ¿Qué método detecta más especies?", "El método 2", "La detección de ADN detecta muchas especies, según la ficha."),
        ("abc", "{F} ¿Qué método tiene el menor costo por muestra?", "El método 1, con 2 unidades", "El método 2, con 6 unidades", "Ambos cuestan igual", "El cultivo cuesta 2 unidades y la detección de ADN, 6."),
        ("ab", "{F} Si el presupuesto es la prioridad principal, ¿qué método conviene?", "El método 1, por su menor costo", "El método 2, por su mayor costo", "El criterio de costo favorece al más barato."),
        ("abc", "{F} La localidad solo puede pagar 150 unidades en total por las 50 muestras. ¿Qué método puede costear?", "El método 1", "El método 2", "Ninguno de los dos", "El método 1 cuesta 50 × 2 = 100 unidades, y el 2 cuesta 50 × 6 = 300, más de lo que hay."),
        ("=", "{F} ¿Cuánto cuestan las 50 muestras con el método 2?", "50*6", "Se multiplica el número de muestras por el costo por muestra.", " unidades"),
        ("=", "{F} ¿Cuántas unidades más cuesta usar el método 2 que el método 1 en las 50 muestras?", "50*6-50*2", "Se restan los costos totales de ambos métodos.", " unidades"),
        ("=", "{F} ¿Cuántos días menos tarda el método 2 que el método 1 en dar un resultado?", "3-1", "Se resta el tiempo del método 2 al tiempo del método 1.", " días"),
        ("abc", "{F} Un brote de enfermedad de ejemplo exige conocer rápido qué microorganismos hay. ¿Qué criterio pesa más?", "La rapidez y el alcance", "El color del recipiente", "El nombre del método", "Cuando hay urgencia, la rapidez y el alcance son claves."),
        ("ab", "{F} La localidad no tiene personal formado para el método 2. ¿Qué implica?", "Hay que formar personas o buscar apoyo externo", "El método 2 ya es mejor", "Sin capacidad local, un método sofisticado puede no poder usarse."),
        ("abc", "{F} Un concejal propone elegir solo el más barato sin discutir con la comunidad. ¿Qué corriges?", "La decisión debe incluir las prioridades de la comunidad además del costo", "Tiene razón: el costo es lo único importante", "No se debe decidir nunca", "Las decisiones sobre tecnología incluyen valores y participación."),
        ("abc", "{F} Una tabla de decisión sirve para:", "Ordenar la información y comparar según criterios", "Reemplazar todo el debate", "Evitar tomar decisiones", "La tabla ordena, pero la decisión incluye juicio y valores."),
    ],
    ctx=("abc", "Contexto: tu curso debe recomendar un método a la localidad de la ficha. ¿Qué informe es más sólido?", "Una tabla con costos, tiempos y alcances, una recomendación y los supuestos declarados", "Una opinión sin datos", "Copiar la solución de otro lugar", "Un informe sólido combina datos, criterios y supuestos."),
    sc=[
        ("En Biología celular y molecular: ¿qué es la capacidad local?", "Las personas, equipos y recursos disponibles en un lugar", "Determina si una tecnología puede usarse allí."),
        ("ab", "Comparar soluciones exige:", "Criterios claros", "Elegir al azar", "Los criterios hacen justa la comparación."),
        ("ab", "Una tabla de decisión:", "Ordena la información para decidir", "Decide sola", "Ayuda, pero no reemplaza el juicio."),
    ],
    op=("Con la ficha {F}: (1) construye una tabla comparando los dos métodos según los cuatro criterios; (2) escribe tu recomendación para la localidad y qué criterio pesa más; (3) escribe un supuesto que podría cambiar tu recomendación.",
        "(1) Costo: método 1 más barato; rapidez: método 2 más rápido; alcance: método 2 detecta más; capacidad local: depende de la localidad. (2) Recomiendo el método 2 si se prioriza el alcance y la rapidez, y el método 1 si se prioriza el costo. (3) Si la localidad no tiene personal formado, cambiaría a favor del método 1.",
        ["tabla con los cuatro criterios", "recomendación justificada con el criterio que más pesa", "supuesto que podría cambiar la decisión"],
        ["una tabla y dos respuestas"],
        ["no usar los cuatro criterios", "recomendar sin justificar", "no declarar ningún supuesto"],
        "Pregunta: «¿qué opina la comunidad y qué dato necesitarías para decidir?»."),
    reinforce="Elige otro problema local inventado y escribe dos soluciones posibles y tres criterios para compararlas.",
    extend="Explica por qué dos comunidades con el mismo problema pueden elegir soluciones distintas y ambas decidir bien.",
)
