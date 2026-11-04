"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 16 (orden liberal y parlamentarismo chileno)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 16"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = "Línea de tiempo: 1833, Constitución que da amplios poderes al presidente; 1865, ley que permite practicar otros cultos en recintos privados; 1871, reforma que prohíbe la reelección inmediata del presidente; 1874, reforma electoral y constitucional que aumenta las facultades del Congreso y amplía el voto a los hombres que sepan leer y escribir; 1883-1884, leyes de cementerios laicos, registro civil y matrimonio civil; 1891, guerra civil entre el presidente Balmaceda y el Congreso; 1925, nueva Constitución que restablece un régimen presidencial."
build(
    OA, 1, F1,
    use="Aprenderé a ubicar en el tiempo las reformas liberales y el parlamentarismo en Chile y a explicar qué cambió en el poder político. Sirve para comprender cómo se transformó el régimen político después de 1833.",
    prior=["Conozco la república y la Constitución como ley máxima.", "Sé leer una línea de tiempo.", "Sé qué son el poder ejecutivo y el legislativo."],
    explain=[
        "La Constitución de 1833 dio amplios poderes al presidente, que era el jefe del poder ejecutivo, es decir, de la rama del Estado que gobierna y administra. Durante la segunda mitad del siglo XIX, grupos liberales impulsaron reformas para limitar esos poderes y fortalecer al Congreso, que es el poder legislativo, es decir, el que hace las leyes. Este proceso se conoce como orden liberal.",
        "Las reformas tocaron varios ámbitos. En lo político, en 1871 se prohibió la reelección inmediata del presidente y en 1874 se aumentaron las facultades del Congreso. En lo religioso hubo secularización, que es el proceso por el cual las instituciones dejan de depender de la Iglesia: se permitieron otros cultos (1865) y se crearon el registro civil, los cementerios laicos y el matrimonio civil (1883-1884). En lo electoral, en 1874 se amplió el voto a los hombres que supieran leer y escribir. También se ampliaron las libertades públicas, como las de prensa, reunión y asociación.",
        "En 1891 el conflicto entre el presidente Balmaceda y el Congreso terminó en una guerra civil. Después se instaló en la práctica un régimen que se llamó parlamentario, en el que el Congreso tuvo un gran peso sobre los gobiernos. No cambió la Constitución de 1833: fue un cambio de práctica política. Duró hasta 1925, cuando una nueva Constitución restableció un régimen presidencial.",
    ],
    vocab=[("poder ejecutivo", "rama del Estado que gobierna y administra, encabezada por el presidente"), ("poder legislativo", "rama del Estado que hace las leyes: el Congreso"), ("secularización", "proceso por el cual las instituciones dejan de depender de la Iglesia"), ("reelección", "volver a ser elegido para el mismo cargo"), ("libertades públicas", "derechos como la prensa, la reunión y la asociación")],
    worked=[
        ("Ubicar en el tiempo", "Con la línea de tiempo, ¿cuántos años pasaron entre la reforma que prohibió la reelección inmediata y la guerra civil?",
         ["Busco las fechas: 1871 y 1891.", "Resto: 1891 - 1871."], "20 años"),
        ("Clasificar una reforma", "La ley de matrimonio civil (1884), ¿es una reforma política, electoral o de secularización?",
         ["El matrimonio civil lo registra el Estado y no la Iglesia.", "Es un cambio en la relación entre Estado e Iglesia."], "De secularización"),
    ],
    mistakes=[
        ("Creer que la Constitución de 1833 se reemplazó en 1891.", "Siguió vigente; cambió la práctica política y se reformó.", "Distingue cambios en el texto y cambios en la práctica."),
        ("Pensar que la ampliación del voto fue universal.", "Se amplió a hombres que sabían leer y escribir; las mujeres y los analfabetos quedaron fuera.", "Revisa quién podía votar y quién no."),
    ],
    T=[
        ("En Historia: ¿qué es el poder legislativo?", "La rama del Estado que hace las leyes: el Congreso", "Las reformas lo fortalecieron."),
        ("{F} ¿En qué año se prohíbe la reelección inmediata del presidente?", "1871", "La línea de tiempo lo indica."),
        ("{F} ¿Qué hecho de 1891 se menciona en la línea?", "La guerra civil entre el presidente Balmaceda y el Congreso", "La línea lo señala."),
        ("En Historia: ¿qué es la secularización?", "El proceso por el cual las instituciones dejan de depender de la Iglesia", "Aplica al registro civil y al matrimonio civil."),
        ("{F} ¿Quién podía votar desde la reforma de 1874? A) los hombres que supieran leer y escribir, B) todas las personas mayores de edad, C) solo los dueños de haciendas.", "A", "La línea lo señala."),
        ("Une cada reforma con su tipo: 1) permitir otros cultos, 2) prohibir la reelección inmediata, 3) ampliar el voto a hombres que sepan leer y escribir. a) electoral, b) de secularización, c) de poderes del presidente. Escribe las parejas.", "1-b, 2-c, 3-a", "Cada reforma toca un ámbito distinto."),
        ("=", "{F} ¿Cuántos años pasaron entre la Constitución de 1833 y la nueva Constitución que restableció el régimen presidencial?", "1925-1833", "Se restan ambas fechas."),
        ("=", "{F} ¿Cuántos años pasaron entre la ley de otros cultos y el matrimonio civil (1884)?", "1884-1865", "Se restan las fechas de la línea."),
        ("Una compañera dice: «El parlamentarismo empezó con una nueva Constitución en 1891». ¿Qué corrección haces?", "No hubo una nueva Constitución en 1891: siguió la de 1833 y el parlamentarismo fue una práctica política", "Cambió la práctica, no el texto."),
        ("{F} ¿Qué dos reformas muestran la ampliación de las libertades públicas y de la participación? Escríbelas.", "La ampliación del voto a hombres que sepan leer y escribir en 1874 y la mayor libertad de culto en 1865", "La línea las incluye."),
        ("Explica por qué la reforma de 1874 limitó los poderes del presidente.", "Porque aumentó las facultades del Congreso, que equilibra al ejecutivo", "Más poder del Congreso reduce el poder presidencial."),
        ("Evalúa la frase «el orden liberal ampliaba la participación sin que fuera universal». A) es razonable porque el voto se amplió solo a hombres que sabían leer y escribir, B) es falsa porque en 1874 votaron todas las personas adultas, C) es falsa porque el voto se redujo.", "A", "Hay ampliación con exclusiones."),
        ("Una persona dice: «El parlamentarismo se estableció con una nueva Constitución aprobada en 1891». Da una razón para dudar usando la clase.", "Porque la Constitución de 1833 siguió vigente y el parlamentarismo fue una práctica política que se instaló después de la guerra civil", "Cambió la práctica, no el texto."),
    ],
    ctx=("En un trabajo escolar se lee «en 1874 todos los chilenos pudieron votar». Escribe una frase que corrija la afirmación con la línea de tiempo.", "En 1874 el voto se amplió a los hombres que supieran leer y escribir, pero no a las mujeres ni a quienes no sabían leer", "La frase debe precisar quiénes quedaron fuera."),
    sc=[("En Historia: ¿qué es el poder ejecutivo?", "La rama del Estado que gobierna y administra, encabezada por el presidente", "Es el poder que se limitó."),
        ("¿Qué son las libertades públicas?", "Derechos como la prensa, la reunión y la asociación", "Se ampliaron en el periodo."),
        ("{F} Nombra un hecho de 1891.", "La guerra civil entre Balmaceda y el Congreso", "Está en la línea de tiempo.")],
    op=("{F} Con la línea de tiempo de arriba, escribe cinco líneas que expliquen cómo cambió el poder político entre 1833 y 1925. Nombra tres reformas, dos fechas y una exclusión que se mantuvo.",
        "La Constitución de 1833 dio mucho poder al presidente. En 1871 se prohibió su reelección inmediata y en 1874 se aumentaron las facultades del Congreso y se amplió el voto a hombres que sabían leer y escribir. Aun así, las mujeres seguían sin votar. En 1891 hubo una guerra civil entre Balmaceda y el Congreso.",
        ["tres reformas", "dos fechas", "una exclusión"], ["texto de cinco líneas"], ["decir que el voto fue universal", "no usar fechas"], "Léele tu texto a alguien de tu casa y pídele que anote las fechas."),
    reinforce="Escribe las siete fechas de la línea de tiempo y, junto a cada una, una palabra que la resuma.",
    extend="Escribe una frase que explique por qué es importante limitar los poderes de un presidente en una república.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = "Fuente A (texto de ejemplo, reforma): «El Congreso podrá fiscalizar los actos del gobierno y los ministros responderán ante él.» Fuente B (artículo de periódico conservador, texto de ejemplo): «La Iglesia es base del orden social y no debe perder su influencia en la enseñanza.» Fuente C (registro electoral, tabla de ejemplo): en una comuna de ejemplo viven 800 hombres adultos; los 500 que saben leer y escribir están inscritos para votar; no hay mujeres inscritas. Fuente D (discurso de un diputado liberal, texto de ejemplo): «Debemos asegurar que ninguna creencia dependa del permiso del Estado.» Fuente E (historiadora actual, texto de ejemplo): «El parlamentarismo chileno fue una práctica política y no un diseño constitucional único.»"
build(
    OA, 2, F2,
    use="Aprenderé a leer críticamente textos de reforma, prensa, discursos y registros electorales del siglo XIX, detectando intención y límites. Sirve para comprender los debates sobre el poder, la Iglesia y el voto sin tomar un solo discurso como verdad.",
    prior=["Conozco las reformas del orden liberal.", "Distingo fuentes primarias y secundarias.", "Sé leer una tabla sencilla."],
    explain=[
        "Las fuentes del orden liberal muestran un debate. Un texto de reforma indica qué regla jurídica se buscaba, como que el Congreso fiscalice al gobierno. Un periódico expresa la postura de un grupo político: el conservador defendía el papel de la Iglesia en la sociedad. Un discurso de un diputado liberal defiende la libertad de creencias. Un registro electoral muestra cuántos podían votar según las reglas.",
        "Para leerlas hay que preguntar quién las escribió y para qué. Un artículo de periódico busca convencer, no describir. Un discurso es parte de un debate político. El registro electoral informa, pero no dice cómo votaban las personas ni cuánta presión recibían. Y una historiadora actual, como en la Fuente E, interpreta con distancia.",
        "Contrastar permite ver más. Si la Fuente A muestra que el Congreso podía fiscalizar al gobierno y la Fuente C muestra que pocos tenían derecho a voto, se entiende que el poder del Congreso estaba en manos de un grupo reducido. Y contrastar la Fuente B con la D muestra el debate entre quienes querían mantener la influencia de la Iglesia y quienes querían separarla del Estado.",
    ],
    vocab=[("fiscalizar", "controlar y supervisar los actos de otra autoridad"), ("registro electoral", "lista de las personas inscritas para votar"), ("conservador / liberal", "posturas políticas del siglo XIX: una defendía el papel de la Iglesia y el orden tradicional; la otra, las libertades y la secularización"), ("discurso político", "texto hablado para defender una postura ante un público"), ("sufragio", "derecho a votar")],
    worked=[
        ("Detectar la perspectiva", "¿Qué postura expresan las Fuentes B y D respecto de la Iglesia?",
         ["La Fuente B defiende la influencia de la Iglesia en la enseñanza.", "La Fuente D defiende que ninguna creencia dependa del permiso del Estado."], "B defiende la influencia de la Iglesia; D defiende la libertad de creencias"),
        ("Calcular con la tabla", "En la Fuente C, ¿cuántos de los 800 hombres adultos no están inscritos y por qué?",
         ["Total de hombres adultos: 800.", "Inscritos, porque saben leer y escribir: 500.", "Resto: 800 - 500."], "300 hombres, que no saben leer y escribir"),
    ],
    mistakes=[
        ("Tomar el artículo de un periódico de partido como descripción neutral.", "Busca convencer desde una postura.", "Pregunta qué partido o grupo habla."),
        ("Creer que un registro electoral muestra todo lo que pensaba la población.", "Solo cuenta a quienes estaban inscritos.", "Anota quién queda fuera de la fuente."),
    ],
    T=[
        ("En Historia: ¿qué es un registro electoral?", "Una lista de las personas inscritas para votar", "Es la fuente de la tabla C."),
        ("{F} ¿Cuántos hombres están inscritos para votar en la comuna de la Fuente C?", "500", "La tabla lo indica."),
        ("En Historia: ¿qué significa fiscalizar?", "Controlar y supervisar los actos de otra autoridad", "Es lo que la Fuente A le da al Congreso."),
        ("{F} ¿La Fuente E es primaria o secundaria?", "Secundaria", "La escribe una historiadora actual."),
        ("{F} ¿Qué defiende la Fuente B? A) la influencia de la Iglesia en la enseñanza, B) la separación entre Iglesia y Estado, C) el voto de las mujeres.", "A", "El periódico conservador lo afirma."),
        ("{F} Una compañera dice que la Fuente B describe de modo neutral el papel de la Iglesia. ¿Qué corrección haces?", "Es un artículo de periódico conservador que defiende una postura", "Tiene intención política."),
        ("=", "En otra comuna de ejemplo viven 600 hombres adultos y 420 saben leer y escribir, así que están inscritos. ¿Cuántos no pueden votar?", "600-420", "Se resta los inscritos del total de hombres adultos."),
        ("=", "En una votación de ejemplo hubo 500 votos: 320 para un candidato liberal y el resto para un conservador. ¿Cuántos votos obtuvo el conservador?", "500-320", "Se resta el voto liberal del total."),
        ("{F} ¿Qué fuente muestra que no había mujeres con derecho a voto en la comuna de ejemplo? A) la A, B) la C, C) la D.", "B", "La tabla dice que no hay mujeres inscritas."),
        ("{F} Explica por qué conviene contrastar las Fuentes B y D.", "Porque muestran dos posturas opuestas sobre el papel de la Iglesia y el Estado", "Revela el debate de la época."),
        ("{F} Redacta una conclusión de una frase con las Fuentes A y C sin exagerar.", "El Congreso podía fiscalizar al gobierno, pero solo un grupo reducido de hombres tenía derecho a voto", "Une poder del Congreso y límite del voto."),
        ("{F} Evalúa la frase «la Fuente C demuestra que nadie quería votar». A) es excesiva porque la tabla no muestra voluntad, B) es correcta, C) es correcta porque faltan mujeres.", "A", "La tabla solo cuenta inscritos."),
        ("¿Qué otra fuente sumarías para saber cómo se votaba en la práctica? Escríbela y explica para qué.", "Por ejemplo: un testimonio de un votante de la época, para conocer presiones y compras de votos", "Completa un límite del registro."),
    ],
    ctx=("{F} Un compañero copia la Fuente D en un afiche con el título «Todos los chilenos pensaban lo mismo sobre la libertad de culto». ¿Qué fuente agregas y por qué?", "La Fuente B, porque muestra que había quienes defendían la influencia de la Iglesia", "Se necesita contrastar para mostrar el debate."),
    sc=[("En Historia: ¿qué es el sufragio?", "El derecho a votar", "Es el tema del registro electoral."),
        ("¿Qué postura defendían los liberales sobre la Iglesia?", "Que las instituciones no dependieran de ella y que hubiera libertad de creencias", "Se vincula con la secularización."),
        ("¿Una tabla de inscritos muestra cómo se votaba? Responde sí o no y por qué.", "No, porque solo cuenta quiénes estaban inscritos", "Es un límite de la fuente.")],
    op=("{F} Con las Fuentes A a E de arriba, escribe un párrafo de siete líneas que responda: «¿Qué debates mostraba el orden liberal?». Incluye dos posturas, un dato numérico de la tabla, y un límite.",
        "La Fuente B defiende la influencia de la Iglesia y la Fuente D defiende la libertad de creencias. La tabla muestra que de 800 hombres adultos solo 500 saben leer y escribir y están inscritos. La Fuente A muestra que el Congreso fiscalizaba al gobierno. Límite: ninguna fuente dice cómo se votaba en la práctica.",
        ["dos posturas", "un dato numérico", "un límite"], ["párrafo de siete líneas"], ["tomar una postura como verdad", "olvidar el límite"], "Pide a alguien de tu casa que revise que usaste dos posturas."),
    reinforce="Haz una tabla con las Fuentes A a E: quién habla, qué dice y un límite.",
    extend="Escribe una pregunta que haría un historiador sobre la Fuente C.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = "Cuadro de ejemplo. Cambio: se limitaron los poderes del presidente y creció el peso del Congreso; se crearon el registro civil, los cementerios laicos y el matrimonio civil; se ampliaron el voto a hombres que sabían leer y escribir y las libertades de prensa, reunión y asociación; se consolidaron partidos como el Conservador, el Liberal, el Radical y el Demócrata. Continuidad: las mujeres seguían sin derecho a voto; un grupo reducido de familias influyentes dominaba la política; las decisiones de los ministros cambiaban con frecuencia; la Iglesia mantuvo influencia social."
build(
    OA, 3, F3,
    use="Aprenderé a distinguir qué cambió y qué continuó en la política chilena entre 1860 y 1920, incluyendo el voto, los partidos y la secularización. Sirve para evaluar el orden liberal sin suponer que fue plenamente democrático.",
    prior=["Conozco las reformas liberales y el parlamentarismo.", "Sé distinguir cambio y continuidad.", "Sé qué es un partido político."],
    explain=[
        "El orden liberal cambió varias reglas del juego político. Se limitaron los poderes del presidente y creció el peso del Congreso. Se consolidó el sistema de partidos: grupos organizados que presentan candidatos y programas, como el Conservador, el Liberal, el Radical y, desde 1887, el Demócrata. Se ampliaron las libertades públicas y el voto, y las instituciones se secularizaron.",
        "Pero también hubo continuidades. Las mujeres seguían sin derecho a voto, que solo obtuvieron para las elecciones municipales en 1934 y para las parlamentarias y presidenciales en 1949. Muchos hombres no podían votar por no saber leer, y existían prácticas como el cohecho, que es comprar votos. Un grupo reducido de familias influyentes conservó gran poder. Y en la práctica parlamentaria, los gabinetes cambiaban con tanta frecuencia que se hablaba de una rotativa ministerial.",
        "El territorio también importa. El control político era más fuerte en las ciudades y en las zonas rurales controladas por grandes propietarios, donde era más fácil presionar a los votantes. Así, ampliar el voto no significó igualdad plena de participación. Para analizar este periodo conviene mirar cambios formales (leyes) y prácticas reales (cómo se aplicaban).",
    ],
    vocab=[("partido político", "grupo organizado que presenta candidatos y programas para ganar elecciones"), ("cohecho", "compra de votos u otros favores a cambio de apoyo electoral"), ("rotativa ministerial", "cambio muy frecuente de los ministros del gabinete"), ("gabinete", "conjunto de ministros que ayudan al presidente a gobernar"), ("oligarquía", "grupo reducido de familias que concentra el poder político y económico")],
    worked=[
        ("Clasificar", "Del cuadro de ejemplo: «se consolidaron partidos políticos» y «las mujeres seguían sin derecho a voto». ¿Cuál es cambio y cuál continuidad?",
         ["La consolidación de partidos es una novedad: cambio.", "La exclusión de las mujeres se mantiene: continuidad."], "Partidos: cambio; mujeres sin voto: continuidad"),
        ("Distinguir ley y práctica", "La ley amplió el voto a hombres que sabían leer y escribir. ¿Qué práctica podía limitar su efecto?",
         ["La ley daba el derecho.", "El cohecho y la presión de grandes propietarios podían condicionar el voto."], "El cohecho y la presión sobre los votantes"),
    ],
    mistakes=[
        ("Decir que la ampliación del voto equivalió a un sufragio universal.", "Las mujeres y los analfabetos seguían excluidos.", "Revisa quién quedaba fuera."),
        ("Confundir cambio de reglas con cambio de prácticas.", "Una ley no siempre se aplica como se escribió.", "Pregunta si el cambio ocurrió en la práctica."),
    ],
    T=[
        ("En Historia: ¿qué es un partido político?", "Un grupo organizado que presenta candidatos y programas para ganar elecciones", "El orden liberal consolidó varios."),
        ("{F} ¿Qué cuatro partidos políticos nombra el cuadro?", "Conservador, Liberal, Radical y Demócrata", "El cuadro los lista."),
        ("En Historia: ¿qué es el cohecho?", "La compra de votos u otros favores a cambio de apoyo electoral", "Era una práctica que limitaba la libertad de voto."),
        ("{F} Clasifica como cambio o continuidad: «se crearon el registro civil y el matrimonio civil».", "Cambio", "Es una secularización nueva."),
        ("{F} Clasifica como cambio o continuidad: «un grupo reducido de familias influyentes dominaba la política».", "Continuidad", "El cuadro lo lista como continuidad."),
        ("{F} Elige la continuidad. A) crecimiento del peso del Congreso, B) las mujeres siguen sin derecho a voto, C) aparición del registro civil.", "B", "Las otras son cambios."),
        ("=", "En una elección de ejemplo, 600 personas tenían derecho a voto y 360 votaron. ¿Cuántas no votaron?", "600-360", "Se resta los votantes de los inscritos."),
        ("=", "En un año de ejemplo hubo 4 gabinetes que duraron lo mismo cada uno. Si el año tiene 12 meses, ¿cuántos meses duró cada gabinete?", "12//4", "Se reparten los meses del año entre los gabinetes."),
        ("Explica por qué hablar de «rotativa ministerial» muestra una debilidad del sistema parlamentario.", "Porque los ministros cambiaban con tanta frecuencia que era difícil mantener políticas estables", "La inestabilidad dificulta gobernar."),
        ("{F} Una compañera dice: «Con las reformas liberales, todos los chilenos participaban igual». Corrige con un dato del cuadro.", "Las mujeres no tenían derecho a voto y un grupo reducido de familias dominaba la política", "Hay exclusiones claras."),
        ("{F} ¿Qué diferencia hay entre una ley que amplía el voto y la práctica del cohecho?", "La ley da el derecho, el cohecho condiciona su ejercicio", "Una es regla, la otra práctica."),
        ("Evalúa la frase «el orden liberal amplió derechos pero mantuvo desigualdades». A) es razonable, B) es falsa porque todos votaban, C) es falsa porque las reformas no cambiaron nada del sistema político.", "A", "Combina cambio y continuidad."),
        ("Propón una pregunta de territorio sobre el voto en zonas rurales.", "Por ejemplo: ¿cómo podía influir un gran propietario en el voto de los trabajadores de su hacienda?", "La pregunta usa el territorio."),
    ],
    ctx=("{F} Un compañero escribe en un trabajo: «Entre 1860 y 1920 Chile ya era una democracia completa». Con el cuadro, escribe una frase que lo matice.", "Hubo reformas y ampliación del voto, pero las mujeres seguían excluidas y existía cohecho", "La frase debe incluir cambio y continuidad."),
    sc=[("En Historia: ¿qué es una oligarquía?", "Un grupo reducido de familias que concentra el poder político y económico", "Sigue vigente en el cuadro."),
        ("Nombra un cambio político del periodo.", "Por ejemplo: creció el peso del Congreso", "Está en el cuadro."),
        ("Nombra una continuidad política del periodo.", "Por ejemplo: las mujeres siguieron sin derecho a voto", "Está en el cuadro.")],
    op=("{F} Con el cuadro de ejemplo de arriba, construye una tabla de dos columnas (cambio y continuidad) con al menos cuatro filas, y escribe una frase final que explique por qué el voto ampliado no fue universal.",
        "Cambio: más peso del Congreso; cambio: consolidación de partidos; cambio: secularización; cambio: ampliación del voto. Continuidad: mujeres sin voto; continuidad: oligarquía; continuidad: rotativa ministerial. El voto no fue universal porque excluía a las mujeres y a los hombres que no sabían leer.",
        ["dos columnas", "cuatro filas", "frase final"], ["tabla y frase"], ["decir que el voto fue universal", "no clasificar"], "Revisa con alguien de tu casa que cada dato esté en su columna."),
    reinforce="Escribe tres datos del cuadro y clasifícalos como cambio o continuidad.",
    extend="Escribe una pregunta sobre cuándo las mujeres obtuvieron el derecho a voto y por qué tardó tanto.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = "Voces de ejemplo, redactadas para este cuaderno. Diputado liberal: «El Congreso debe controlar al gobierno y garantizar libertades.» Diputado conservador: «No debemos romper la unión entre la Iglesia y la sociedad.» Presidente Balmaceda: «El gobierno necesita disponer del presupuesto para ejecutar sus obras.» Artesano del Partido Demócrata: «Queremos que los trabajadores tengan voz en la política.» Mujer que reclama derechos: «Si pagamos impuestos y trabajamos, también debemos tener derecho a participar.»"
build(
    OA, 4, F4,
    use="Aprenderé a reconocer actores, causas y perspectivas del orden liberal y del conflicto de 1891. Sirve para explicar la guerra civil y el parlamentarismo como resultado de intereses opuestos y no de personas aisladas.",
    prior=["Conozco las reformas y las fuentes del periodo.", "Sé qué es la multicausalidad.", "Sé que las posturas políticas defienden intereses."],
    explain=[
        "En el orden liberal actuaron varios grupos. Los liberales querían limitar al presidente y ampliar libertades. Los conservadores defendían el papel de la Iglesia y un orden más tradicional. Los radicales buscaban reformas laicas y educación. El presidente José Manuel Balmaceda (1886-1891) impulsó obras públicas y quería un gobierno con más recursos. Artesanos y trabajadores formaron el Partido Demócrata (1887), y las mujeres reclamaron derechos políticos.",
        "El conflicto de 1891 tuvo varias causas: la disputa por el equilibrio de poderes entre presidente y Congreso, el desacuerdo sobre el presupuesto y la elección del sucesor, y los intereses de grupos económicos y políticos. Por eso hablamos de multicausalidad. Terminó con una guerra civil entre enero y agosto de 1891, la derrota de Balmaceda y el predominio del Congreso en la práctica política.",
        "Las perspectivas fueron muy distintas. Para el Congreso se trataba de defender las libertades y su papel de control; para el presidente, de garantizar la capacidad de gobernar; para los trabajadores y las mujeres, de conseguir ser escuchados. Estudiar estas voces muestra que el sistema político tuvo ganadores y excluidos.",
    ],
    vocab=[("presupuesto", "plan de ingresos y gastos del Estado para un año"), ("equilibrio de poderes", "reparto del poder entre el ejecutivo y el legislativo para que ninguno domine"), ("guerra civil", "conflicto armado entre grupos de un mismo país"), ("radical", "partido que impulsó reformas laicas y la educación"), ("sucesor", "persona que reemplaza a otra en un cargo")],
    worked=[
        ("Emparejar actor e interés", "¿Qué interés expresa el diputado liberal y cuál el presidente Balmaceda?",
         ["El diputado quiere que el Congreso controle al gobierno y garantice libertades.", "Balmaceda quiere disponer del presupuesto para sus obras."], "Diputado: control y libertades; presidente: presupuesto para obras"),
        ("Pasar de una a varias causas", "Un compañero dice: «la guerra civil se debió solo a un desacuerdo por el presupuesto». Da otra causa.",
         ["El presupuesto es una causa.", "También fue importante el equilibrio de poderes entre presidente y Congreso."], "El equilibrio de poderes entre presidente y Congreso"),
    ],
    mistakes=[
        ("Explicar 1891 como un conflicto entre dos personas.", "Detrás había grupos, intereses y diseños distintos de poder.", "Nombra los actores y sus intereses."),
        ("Olvidar a los grupos que no tenían voz en el Congreso.", "Trabajadores y mujeres también tenían perspectivas.", "Incluye al Partido Demócrata y a las mujeres."),
    ],
    T=[
        ("En Historia: ¿qué es un presupuesto?", "Un plan de ingresos y gastos del Estado para un año", "Fue un punto de conflicto."),
        ("{F} ¿Qué dice el diputado conservador que no debe romperse?", "La unión entre la Iglesia y la sociedad", "Su voz lo dice."),
        ("En Historia: ¿qué es una guerra civil?", "Un conflicto armado entre grupos de un mismo país", "Eso ocurrió en 1891."),
        ("{F} ¿Qué reclama la mujer de la voz de ejemplo?", "Derecho a participar, porque paga impuestos y trabaja", "Su voz lo dice."),
        ("Une cada actor con su interés: 1) presidente, 2) diputado liberal, 3) artesano demócrata. a) control del Congreso y libertades, b) disponer del presupuesto para obras, c) voz de los trabajadores en la política. Escribe las parejas.", "1-b, 2-a, 3-c", "Cada voz expresa un interés distinto."),
        ("{F} Elige el actor que expresa la defensa del papel de la Iglesia. A) el diputado conservador, B) el diputado liberal, C) el presidente.", "A", "Su voz lo plantea."),
        ("=", "La guerra civil de 1891 duró de enero a agosto. ¿Cuántos meses fueron, contando enero (mes 1) hasta agosto (mes 8)?", "8-1+1", "Se cuentan todos los meses incluidos."),
        ("=", "El período presidencial de Balmaceda fue de 1886 a 1891. ¿Cuántos años duró su gobierno?", "1891-1886", "Se restan las fechas."),
        ("Una compañera dice que 1891 fue solo una disputa personal entre dos políticos. Menciona una causa distinta.", "El desacuerdo sobre el equilibrio de poderes entre presidente y Congreso", "Había causas institucionales."),
        ("Explica por qué hablamos de multicausalidad al estudiar 1891.", "Porque influyeron el equilibrio de poderes, el presupuesto, la sucesión presidencial y los intereses de grupos", "Varias causas se combinaron."),
        ("{F} ¿En qué se diferencian las perspectivas del diputado liberal y del presidente?", "El diputado quiere control del Congreso y el presidente quiere capacidad de gobernar con recursos", "Defienden diseños de poder distintos."),
        ("Evalúa la frase «todos los grupos políticos tenían las mismas metas». A) es falsa porque tenían intereses distintos, B) es correcta, C) es correcta porque todos pertenecían al Congreso.", "A", "El periodo se explica por conflictos de intereses."),
        ("Redacta una pregunta para contrastar la voz de la mujer con la del diputado liberal.", "Por ejemplo: ¿a quiénes incluía cada uno cuando hablaba de libertades?", "La pregunta pone en tensión la exclusión."),
    ],
    ctx=("{F} En una dramatización escolar sobre 1891, un compañero hace que todos los personajes digan «el Congreso tiene la razón». Con las voces de ejemplo, ¿cómo harías hablar al presidente y al artesano?", "El presidente hablaría de disponer del presupuesto para sus obras y el artesano de la voz de los trabajadores", "Cada personaje debe hablar desde su interés."),
    sc=[("En Historia: ¿qué es el equilibrio de poderes?", "El reparto del poder entre el ejecutivo y el legislativo para que ninguno domine", "Estuvo en el centro del conflicto."),
        ("Nombra dos actores del periodo.", "Por ejemplo: los liberales y los conservadores", "Ambos participaron en el periodo."),
        ("¿Cuándo ocurrió la guerra civil entre el presidente Balmaceda y el Congreso?", "En 1891", "Es el hecho central del periodo.")],
    op=("{F} Elige dos voces de ejemplo de arriba y escribe cinco líneas: qué busca cada una, una causa del conflicto de 1891 y una diferencia de perspectiva entre ellas.",
        "El diputado liberal quiere que el Congreso controle al gobierno. El presidente quiere disponer del presupuesto para sus obras. Una causa fue el equilibrio de poderes. El diputado ve libertades y control; el presidente, capacidad de gobernar.",
        ["dos voces", "una causa", "diferencia de perspectiva"], ["texto de cinco líneas"], ["reducir el conflicto a dos personas", "no marcar diferencia"], "Cuenta tu texto a alguien de tu casa y pídele que diga cuál es la diferencia."),
    reinforce="Haz una tabla con cinco actores y un interés para cada uno.",
    extend="Explica por qué las mujeres y los trabajadores aparecen poco en el Congreso del periodo.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = "Dossier de ejemplo. Dato 1: las reformas de 1871 y 1874 limitaron al presidente y aumentaron las facultades del Congreso. Dato 2: entre 1865 y 1884 se ampliaron la libertad de culto y se crearon el registro civil, los cementerios laicos y el matrimonio civil. Dato 3: en 1874 el voto se amplió a hombres que supieran leer y escribir; las mujeres seguían sin voto. Dato 4: la guerra civil de 1891 enfrentó al presidente Balmaceda y al Congreso. Dato 5: tras 1891 se consolidó un régimen parlamentario hasta 1925, con gabinetes que duraban poco."
build(
    OA, 5, F5,
    use="Aprenderé a argumentar con evidencia cómo se transformó el orden político liberal y parlamentario, y qué límites tuvo. Sirve para evaluar el periodo sin llamarlo plenamente democrático ni totalmente excluyente.",
    prior=["Conozco las reformas, los actores y las fuentes.", "Sé distinguir cambio y continuidad.", "Sé escribir tesis, evidencia y límite."],
    explain=[
        "Un argumento sobre el orden liberal responde a una pregunta como «¿Cómo se transformó el sistema político chileno entre 1860 y 1925 y qué límites tuvo?». Una tesis posible es que las reformas aumentaron el poder del Congreso, ampliaron libertades y secularizaron instituciones, pero mantuvieron exclusiones y una inestabilidad ministerial.",
        "Las evidencias deben explicarse. El dato 1 muestra el aumento de las facultades del Congreso. El dato 2 muestra la secularización. El dato 3 muestra una ampliación del voto con exclusiones. Los datos 4 y 5 muestran el conflicto de 1891 y el parlamentarismo posterior. Cada dato se explica con la fórmula «esto muestra que…».",
        "El límite: con el dossier no sabemos cuántas personas votaban realmente ni cómo se votaba en la práctica. Tampoco podemos decir que el parlamentarismo chileno fuera igual al británico. El dossier habla de reformas y hechos, y no de la vida cotidiana de cada grupo. Una buena respuesta evita frases como «todos votaban» o «el parlamentarismo fue un fracaso total».",
    ],
    vocab=[("tesis", "afirmación principal que se defiende"), ("evidencia", "dato que apoya la tesis"), ("régimen parlamentario", "práctica política en que el Congreso tiene gran peso sobre los gobiernos"), ("inestabilidad ministerial", "cambio frecuente de ministros que dificulta mantener políticas"), ("límite", "aquello que la evidencia no permite afirmar")],
    worked=[
        ("Elegir evidencias", "Para sostener que el Congreso ganó poder, ¿qué datos del dossier sirven?",
         ["El dato 1 muestra las reformas que aumentaron sus facultades.", "El dato 5 muestra el régimen parlamentario después de 1891."], "Los datos 1 y 5"),
        ("Detectar exageración", "¿Por qué excede el dossier la frase «en 1874 todos pudieron votar»?",
         ["El dato 3 dice que se amplió a hombres que supieran leer y escribir.", "Las mujeres seguían sin voto."], "Porque las mujeres y quienes no sabían leer seguían excluidos"),
    ],
    mistakes=[
        ("Escribir una tesis que no menciona exclusiones.", "Presenta el periodo como plenamente democrático.", "Incluye el dato 3 con sus límites."),
        ("Equiparar el parlamentarismo chileno con el británico.", "Eran contextos distintos y no hubo la misma estructura.", "Describe el caso chileno con sus propias características."),
    ],
    T=[
        ("En Historia: ¿qué es un régimen parlamentario?", "Una práctica política en que el Congreso tiene gran peso sobre los gobiernos", "Fue la práctica entre 1891 y 1925."),
        ("{F} ¿Qué dato muestra la secularización? A) dato 1, B) dato 2, C) dato 4.", "B", "El dato 2 habla de registro civil y matrimonio civil."),
        ("{F} ¿Qué dato muestra la ampliación del voto con exclusiones?", "El dato 3", "Menciona hombres que sepan leer y escribir y la exclusión de las mujeres."),
        ("{F} ¿Qué dato menciona gabinetes que duraban poco?", "El dato 5", "Habla de inestabilidad ministerial."),
        ("Elige la tesis mejor formulada. A) Todo fue democrático, B) Las reformas aumentaron el poder del Congreso y ampliaron libertades, pero mantuvieron exclusiones, C) Nada cambió.", "B", "Es defendible con el dossier."),
        ("Una compañera usa solo el dato 3 para decir que «todos votaban». ¿Qué parte del dato lo contradice?", "Que las mujeres seguían sin voto y solo votaban hombres que supieran leer y escribir", "El mismo dato muestra exclusiones."),
        ("=", "{F} Si el dossier tiene 5 datos y 2 se refieren al Congreso (1 y 5), ¿cuántos datos hablan de otros temas?", "5-2", "Se restan los datos usados."),
        ("=", "Un grupo escribe un texto de 15 líneas: 2 de tesis, 9 de evidencias y el resto de límite. ¿Cuántas líneas son de límite?", "15-2-9", "Se restan tesis y evidencias del total."),
        ("{F} Con los datos 3 y 5, redacta una conclusión proporcional.", "El voto se amplió a hombres que sabían leer y escribir, y el parlamentarismo trajo gabinetes que duraban poco", "Une ampliación y debilidad."),
        ("Explica por qué una buena tesis debe nombrar tanto avances como límites del orden liberal.", "Porque hubo reformas importantes, pero también exclusiones e inestabilidad", "El periodo tuvo ambos rasgos."),
        ("Un compañero escribe: «El parlamentarismo fue un fracaso total». Señala la exageración.", "«Total» excede la evidencia, porque el dossier muestra también avances como la secularización", "Es una afirmación absoluta."),
        ("Evalúa este argumento: «El Congreso ganó poder (datos 1 y 5), pero las mujeres seguían sin voto (dato 3)». A) es sólido porque une avance y límite, B) es débil porque solo presenta avances y ningún límite, C) es falso porque el dossier muestra que el voto fue universal.", "A", "Usa evidencia de ambos lados."),
        ("Escribe una pregunta que exigiría otra fuente para completar el argumento.", "Por ejemplo: ¿cuántas personas votaban realmente en una elección y cómo?", "La pregunta indica un vacío del dossier."),
    ],
    ctx=("{F} En un foro estudiantil alguien dice que «el parlamentarismo chileno fue idéntico al británico». Con el dossier, escribe tu respuesta en dos frases con una evidencia.", "No necesariamente: el dato 5 muestra un régimen en que el Congreso pesaba mucho en la práctica, pero el dossier no muestra que sea igual al británico", "La respuesta debe usar el dato 5 con cautela."),
    sc=[("En Historia: ¿qué es la inestabilidad ministerial?", "El cambio frecuente de ministros que dificulta mantener políticas", "Era un rasgo del periodo."),
        ("Nombra un dato del dossier sobre libertades.", "Por ejemplo: se ampliaron la libertad de culto y el registro civil", "Es el dato 2."),
        ("¿Qué exclusión del voto mantuvo el dato 3?", "Las mujeres seguían sin voto", "Es el límite del dato.")],
    op=("{F} Con el dossier de ejemplo de arriba, escribe un párrafo de ocho líneas que responda: «¿Cómo se transformó el sistema político chileno y qué límites tuvo?». Incluye una tesis, tres evidencias explicadas y un límite.",
        "Las reformas de 1871 y 1874 aumentaron el poder del Congreso y, tras la guerra civil de 1891, se consolidó el parlamentarismo. Entre 1865 y 1884 se secularizaron instituciones con el registro civil y el matrimonio civil. El voto se amplió, pero las mujeres seguían sin voto y los gabinetes duraban poco. Límite: el dossier no muestra cómo se votaba en la práctica.",
        ["tesis", "tres evidencias explicadas", "límite"], ["párrafo de ocho líneas"], ["decir que fue plenamente democrático", "no explicar los datos"], "Pide a alguien de tu casa que marque tu tesis y tus tres evidencias."),
    reinforce="Escribe tu tesis en una frase y anota las tres evidencias que la apoyan.",
    extend="Escribe una segunda tesis centrada en las exclusiones del sistema político y un dato nuevo que necesitarías.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 6
F6 = "Resumen de ejemplo para evaluar proyecciones. Hacia 1900, el Congreso tenía gran peso, pero los gabinetes cambiaban con rapidez. Los partidos Conservador, Liberal, Radical y Demócrata competían; existían diarios y asociaciones; el voto seguía restringido a hombres que sabían leer y escribir. Mientras tanto, crecían las ciudades, había conventillos con hacinamiento y los trabajadores se organizaban en sociedades y mancomunales. En 1925 una nueva Constitución restableció un régimen presidencial y separó la Iglesia del Estado; en 1934 una ley dio a las mujeres el derecho a votar en elecciones municipales y en 1949 otra ley les dio el derecho a votar en elecciones parlamentarias y presidenciales."
build(
    OA, 6, F6,
    use="Aprenderé a evaluar las proyecciones del orden liberal y parlamentario: qué dejó, qué no resolvió y cómo preparó cambios posteriores. Sirve para conectar la política con la cuestión social y con la Constitución de 1925.",
    prior=["Conozco las reformas, los actores y los argumentos del orden liberal.", "Sé evaluar con evidencia y límite.", "Sé qué es la cuestión social."],
    explain=[
        "Evaluar proyecciones significa preguntar qué consecuencias de largo plazo dejó un proceso. El orden liberal dejó una tradición de partidos, libertades públicas y control del Congreso, y avanzó en la separación entre Iglesia y Estado, que se completó en 1925. También dejó límites: el voto siguió siendo restringido y el sistema político respondía poco a las demandas de los trabajadores.",
        "Esa distancia entre el sistema político y la sociedad se vio con la cuestión social. Mientras el Congreso discutía, crecían las ciudades, había conventillos con hacinamiento y los trabajadores se organizaban en sociedades y en mancomunales. La inestabilidad de los gabinetes dificultaba responder a esas demandas. En ese contexto surgieron presiones por reformar el régimen, que llevaron a la Constitución de 1925, la cual restableció un régimen presidencial.",
        "Las proyecciones políticas también incluyeron la participación de las mujeres: obtuvieron el derecho a votar en elecciones municipales en 1934 y en las parlamentarias y presidenciales en 1949. Al evaluar, hay que reconocer los límites de nuestro conocimiento y evitar juicios simples como «el parlamentarismo fue bueno» o «fue malo»: tuvo avances, limitaciones y consecuencias que se discuten.",
    ],
    vocab=[("proyección", "consecuencia de largo plazo de un proceso"), ("conventillo", "vivienda popular con piezas pequeñas alrededor de un patio, muchas veces con hacinamiento"), ("hacinamiento", "situación en que muchas personas viven en un espacio muy pequeño"), ("mancomunal", "organización de trabajadores que reunía a distintas ocupaciones de un lugar"), ("régimen presidencial", "sistema en que el presidente tiene amplios poderes de gobierno")],
    worked=[
        ("Ordenar por fecha", "Con el resumen, ¿cuántos años pasaron entre el voto municipal femenino y el voto femenino en elecciones parlamentarias y presidenciales?",
         ["Busco las fechas: 1934 y 1949.", "Resto: 1949 - 1934."], "15 años"),
        ("Conectar política y sociedad", "¿Por qué la inestabilidad de los gabinetes dificultaba responder a las demandas de los trabajadores?",
         ["Los gabinetes cambiaban con rapidez.", "Era difícil mantener y aplicar políticas sociales durante mucho tiempo."], "Porque cambiaban con rapidez y no podían sostener políticas"),
    ],
    mistakes=[
        ("Evaluar el parlamentarismo solo como un fracaso o solo como un éxito.", "Tuvo avances y límites.", "Nombra ambos."),
        ("Separar la política de la cuestión social.", "Estaban relacionadas: el sistema político respondía poco a las demandas.", "Conecta ambas con evidencia."),
    ],
    T=[
        ("En Historia: ¿qué es un conventillo?", "Una vivienda popular con piezas pequeñas alrededor de un patio, muchas veces con hacinamiento", "Es un rasgo de la cuestión social."),
        ("{F} ¿En qué año obtuvieron las mujeres el derecho a votar en elecciones municipales?", "1934", "El resumen lo indica."),
        ("En Historia: ¿qué es el hacinamiento?", "Una situación en que muchas personas viven en un espacio muy pequeño", "Describe los conventillos."),
        ("{F} ¿Qué restableció la Constitución de 1925? A) un régimen presidencial, B) un régimen parlamentario, C) una monarquía.", "A", "El resumen lo señala."),
        ("{F} ¿Qué partidos competían hacia 1900 según el resumen?", "Conservador, Liberal, Radical y Demócrata", "El resumen los nombra."),
        ("Une cada proyección con su ámbito: 1) separación entre Iglesia y Estado, 2) voto femenino, 3) organización de trabajadores. a) social, b) de secularización, c) de derechos políticos. Escribe las parejas.", "1-b, 2-c, 3-a", "Cada proyección toca un ámbito."),
        ("=", "{F} ¿Cuántos años pasaron entre la Constitución de 1925 y el voto femenino en elecciones parlamentarias y presidenciales?", "1949-1925", "Se restan ambas fechas."),
        ("=", "En un conventillo de ejemplo viven 36 personas en 9 piezas, repartidas por igual. ¿Cuántas personas hay por pieza?", "36//9", "Se divide el total entre las piezas."),
        ("Explica por qué la distancia entre política y sociedad contribuyó a reformar el régimen en 1925.", "Porque el sistema respondía poco a las demandas de los trabajadores y los gabinetes cambiaban con rapidez, lo que generó presión por reformarlo", "Existía descontento con el sistema."),
        ("{F} Una compañera dice: «El parlamentarismo no dejó ninguna proyección». Corrige con un dato del resumen.", "Dejó partidos, libertades públicas y el debate sobre el equilibrio de poderes que se resolvió en 1925", "Hay proyecciones claras."),
        ("{F} ¿Qué límite tiene el resumen para evaluar el impacto del parlamentarismo en la vida diaria?", "No muestra cifras ni testimonios de las personas", "Es un vacío de la fuente."),
        ("Evalúa la frase «el parlamentarismo fue solo un fracaso». A) es incompleta porque tuvo avances como la consolidación de partidos y libertades, B) es correcta, C) es correcta porque duró poco.", "A", "Hubo avances y límites."),
        ("Propón una pregunta para seguir investigando el periodo.", "Por ejemplo: ¿cómo respondió el Congreso a las demandas de los trabajadores entre 1900 y 1920?", "La pregunta conecta política y cuestión social."),
    ],
    ctx=("{F} Un compañero escribe en un trabajo «el parlamentarismo no tuvo relación con los problemas sociales». Con el resumen, escribe una frase que lo corrija.", "La inestabilidad de los gabinetes dificultaba responder a las demandas de trabajadores que vivían en conventillos con hacinamiento", "La corrección conecta política y sociedad."),
    sc=[("En Historia: ¿qué es un régimen presidencial?", "Un sistema en que el presidente tiene amplios poderes de gobierno", "Se restableció en 1925."),
        ("Nombra una proyección del orden liberal.", "Por ejemplo: la consolidación de partidos y libertades públicas", "Está en el resumen."),
        ("{F} ¿En qué año obtuvieron las mujeres el derecho a votar en elecciones parlamentarias y presidenciales?", "En 1949", "Está en el resumen.")],
    op=("{F} Con el resumen de ejemplo de arriba, escribe un párrafo de ocho líneas que evalúe las proyecciones del orden liberal: nombra un avance, un límite, una relación con la cuestión social y una fecha de 1925 a 1949.",
        "El orden liberal dejó partidos, libertades públicas y un Congreso con peso. Su límite fue que el voto siguió restringido y los gabinetes cambiaban con rapidez. Esto dificultó responder a trabajadores que vivían en conventillos con hacinamiento. En 1925 se restableció un régimen presidencial y las mujeres obtuvieron el derecho a votar en elecciones parlamentarias y presidenciales en 1949.",
        ["un avance", "un límite", "relación con la cuestión social", "una fecha"], ["párrafo de ocho líneas"], ["juzgarlo solo como fracaso o éxito", "no conectar con lo social"], "Pide a alguien de tu casa que revise que incluyas un avance y un límite."),
    reinforce="Haz una tabla con dos columnas (avances y límites) con dos datos en cada una.",
    extend="Escribe una pregunta sobre qué pasó con la Iglesia y el Estado después de 1925.",
    materials=MAT,
)
