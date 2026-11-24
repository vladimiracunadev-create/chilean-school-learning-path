"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 1 (parte 3): OAD-03, características de periodos de la historia de Chile y de la humanidad (hitos, procesos y rasgos) a partir de fuentes de ejemplo. Los periodos se describen de forma general y los límites son aproximados."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y cuaderno. Todas las fuentes son resúmenes o textos de ejemplo escritos para este cuaderno: no son citas de obras reales. Las descripciones de los periodos son generales y sus límites son aproximados; "
             "para profundizar, un docente o un libro de historia de Chile puede entregar más detalle. Algunos temas (conquista, guerra, trabajo obligado) fueron dolorosos para muchas personas: se tratan con rigor y sin juzgar a las personas de hoy. "
             "Nadie debe contar datos personales; puedes pasar tu turno cuando lo necesites. Si algo cuesta leer, pide apoyo.")
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-03"

# ======================================================= clase 1
F1 = ("Ficha 1 (de ejemplo, pueblo ficticio de Los Robles). Antes de que llegara la luz eléctrica (hasta los años 1950, dato de ejemplo): se alumbraba con velas; la gente se acostaba temprano; las noticias se sabían en la plaza o por cartas. "
      "Después de la luz eléctrica: se usan ampolletas y radios; la gente se informa por la radio; algunos talleres trabajan de noche. En ambos tiempos, los domingos las familias se reúnen en la plaza.")
build(
    O, 1, F1,
    use="Hoy parto de lo que ya sé: comparo cómo era la vida antes y después de un cambio y reconozco los rasgos de un periodo.",
    prior=["Reconozco cambios en mi barrio o en mi ciudad con los años.", "Sé ordenar hechos por fecha.", "Distingo hecho de opinión."],
    explain=[
        "Un periodo histórico es una etapa del pasado con rasgos propios. Los rasgos son las características que lo distinguen: cómo vivía la gente, a qué se dedicaba, quién gobernaba, qué creía y cómo se informaba. Tú ya comparas periodos cuando dices «antes se hacía así y ahora se hace distinto».",
        "Para describir un periodo puedes preguntar: ¿cómo se vivía? ¿cómo se trabajaba? ¿cómo se gobernaba? ¿qué cambió y qué siguió igual? Lo que cambia se llama cambio; lo que sigue igual se llama continuidad. Ambas cosas son parte de la historia.",
        "Al estudiar el pasado hay que evitar juzgarlo solo con los valores de hoy. Decir que la gente de entonces era «atrasada» porque no tenía luz eléctrica es injusto: vivían con los medios y las ideas de su tiempo. Se trata de comprender, no de calificar.",
    ],
    vocab=[("rasgo", "característica que distingue un periodo"), ("cambio", "algo que es distinto de un periodo a otro"), ("continuidad", "algo que sigue igual a lo largo del tiempo"), ("periodo", "etapa de la historia con rasgos propios"), ("valores", "ideas sobre lo que se considera bueno o correcto")],
    worked=[
        ("Cambio y continuidad", "{F} ¿Qué cambió y qué siguió igual?", ["Cambió el alumbrado (velas a ampolletas) y la forma de informarse (plaza a radio).", "Siguió igual que los domingos las familias se reúnen en la plaza."], "Cambios: alumbrado e información; continuidad: la reunión de los domingos"),
        ("Evitar juzgar con valores de hoy", "Un estudiante dice: «Antes la gente era atrasada». ¿Cómo lo corriges?", ["Revisa qué medios tenía esa gente.", "Describe sus rasgos sin calificarla desde el presente."], "Vivían con los medios de su tiempo, que eran otros"),
    ],
    mistakes=[("Describir un periodo con solo lo que cambió y olvidar lo que siguió igual.", "La continuidad también explica cómo vivía la gente.", "Anota siempre un cambio y una continuidad."),
              ("Juzgar el pasado solo con los valores de hoy.", "Se pierde de vista las condiciones de ese tiempo.", "Describe primero cómo se vivía y evita calificar con palabras como «atrasado».")],
    T=[
        ("abc", "{F} ¿Cómo se alumbraba el pueblo antes de la luz eléctrica?", "Con velas", "Con ampolletas", "Con radios", "La ficha dice que se alumbraba con velas."),
        ("ab", "En HGCS: ¿qué es un rasgo de un periodo?", "Una característica que lo distingue", "Una fecha exacta", "Los rasgos describen cómo era la vida de esa etapa."),
        ("{F} ¿Qué medio usa la gente para informarse después de la luz eléctrica?", "la radio", "La ficha dice que después de la luz la gente se informa por la radio."),
        ("abc", "{F} ¿Qué es una continuidad en este caso?", "Que los domingos las familias se reúnen en la plaza", "Que se usan ampolletas", "Que se acuesta temprano", "Lo que se mantiene en ambos tiempos es la reunión de la plaza."),
        ("ab", "{F} ¿Cuál es un cambio?", "El uso de radios en las casas", "La reunión en la plaza", "Las radios aparecieron después de la luz, por eso son un cambio."),
        ("{F} ¿Qué hacía la gente por la noche antes de la luz, según la ficha? Responde con una acción.", "se acostaba temprano", "La ficha dice que la gente se acostaba temprano."),
        ("abc", "{F} Una persona dice: «Antes la gente era atrasada porque usaba velas». ¿Qué problema tiene esa frase?", "Juzga el pasado solo con los valores de hoy", "Usa números romanos", "Cita mal la fecha", "Califica a las personas desde el presente en vez de comprender sus condiciones."),
        ("abc", "{F} ¿Cuál es una forma de describir ese periodo sin juzgar?", "Se alumbraban con velas y se informaban en la plaza o por cartas", "Eran personas atrasadas", "Vivían peor que hoy", "Describe los rasgos sin calificar a las personas desde el presente."),
        ("ab", "¿Por qué se pregunta «qué siguió igual»?", "Porque la continuidad también forma parte del periodo", "Porque el pasado nunca cambia", "Los periodos no son solo cambios; hay cosas que permanecen."),
        ("abc", "{F} Si en el periodo posterior se agregara «la gente sigue encendiendo velas cuando se corta la luz», ¿qué sería?", "Una continuidad parcial", "Un cambio total", "Un error", "Sigue existiendo un rasgo del periodo anterior."),
        ("abc", "{F} Un taller trabaja de noche después de la luz. ¿Qué rasgo del periodo nuevo muestra?", "Que la luz eléctrica permitió trabajar de noche", "Que se acostaban temprano", "Que no había talleres", "Es un cambio en la forma de trabajar ligado a la luz."),
        ("ab", "¿Cuál pregunta ayuda a caracterizar un periodo?", "¿Cómo se vivía, se trabajaba y se informaba la gente?", "¿Quién fue la persona más famosa?", "Los rasgos se descubren preguntando por la vida cotidiana."),
        ("abc", "{F} Elige la mejor descripción corta del periodo anterior a la luz:", "Alumbrado con velas, vida nocturna reducida e información en la plaza o por cartas", "Una época mala", "Un tiempo sin reuniones", "Resume rasgos concretos de la ficha."),
    ],
    ctx=("abc", "En una charla de memoria barrial se presenta un cuadro de ejemplo: «Antes del pavimento, la calle se llenaba de barro cuando llovía; después, los buses pasan todo el año. Los vecinos siguen conversando en la vereda». ¿Qué parte es continuidad?", "Los vecinos siguen conversando en la vereda", "Los buses pasan todo el año", "La calle tenía barro", "Es lo que se mantiene antes y después del cambio."),
    sc=[("¿Qué es un periodo?", "Una etapa de la historia con rasgos propios", "Se reconoce por sus rasgos comunes."),
        ("En HGCS: ¿qué es la continuidad?", "Lo que sigue igual a lo largo del tiempo", "La continuidad se contrapone al cambio y muestra lo que permanece."),
        ("¿Por qué no hay que juzgar el pasado solo con valores de hoy?", "Porque se pierden las condiciones de esa época", "Comprender una época requiere entender su contexto y sus condiciones.")],
    op=("Ficha de ejemplo: «Antes de la locomoción colectiva, las personas del sector Las Quilas caminaban dos horas hasta el pueblo. Después, un bus pasa tres veces al día. Las ferias se siguen haciendo los sábados». "
        "Describe el periodo de antes y el de después con un rasgo cada uno. Anota un cambio y una continuidad.",
        "Antes: caminaban dos horas hasta el pueblo. Después: un bus pasa tres veces al día. Cambio: el transporte. Continuidad: la feria de los sábados.",
        ["describe antes y después con rasgos", "señala un cambio y una continuidad", "no califica a las personas"],
        ["una tabla de dos columnas y una frase"], ["usar la palabra «atrasado»", "olvidar la continuidad"],
        "Pregunta: «¿Qué cambió y qué siguió igual?»."),
    reinforce="Describe cómo se hacía una tarea de tu vida diaria hace diez años y cómo se hace ahora.",
    extend="Explica por qué estudiar solo los cambios puede dar una imagen incompleta del pasado.",
)

# ======================================================= clase 2
F2 = ("Ficha 2 (de ejemplo). Resumen: «Entre 1810 y 1818, Chile pasó por un proceso de independencia. En 1810 se formó la Primera Junta Nacional de Gobierno. "
      "En 1818 se proclamó la independencia. Hubo años de guerra y de organización de un gobierno propio». "
      "Otra ficha: «Hace miles de años, grupos humanos que vivían de la caza y la recolección comenzaron a cultivar plantas. Este cambio se llama proceso de adopción de la agricultura y duró muchísimo tiempo».")
build(
    O, 2, F2,
    use="Hoy aprendo la diferencia entre hito, proceso y rasgo, y las uso para hablar de periodos de Chile y de la humanidad.",
    prior=["Describo antes y después de un cambio.", "Sé qué es un periodo.", "Ubico fechas en siglos."],
    explain=[
        "Un hito es un hecho puntual e importante que marca un cambio, como la proclamación de la independencia de Chile en 1818. Un proceso es un conjunto de cambios que ocurren durante un tiempo largo, como el proceso de independencia entre 1810 y 1818 o la adopción de la agricultura. Al periodo en que grupos humanos pasaron de la caza y la recolección a cultivar plantas y criar animales se le llama Neolítico.",
        "Los rasgos son las características que distinguen a un periodo. Si hablas de la Colonia, un rasgo es que gobernaba la Corona española. Para caracterizar un periodo conviene nombrar sus hitos, explicar sus procesos y señalar sus rasgos principales.",
        "Distinguir hito de proceso evita errores. El hito es una fecha; el proceso es una duración. Por eso se dice «la independencia fue un proceso» y «la proclamación de 1818 fue un hito dentro de ese proceso».",
    ],
    vocab=[("hito", "hecho importante que ocurre en un momento y marca un cambio"), ("proceso", "conjunto de cambios que ocurren en un tiempo largo"), ("rasgo", "característica que distingue un periodo"), ("Neolítico", "periodo en que grupos humanos comenzaron a cultivar y a criar animales"), ("agricultura", "cultivo de plantas para alimentarse")],
    worked=[
        ("Hito o proceso", "{F} ¿La proclamación de la independencia es un hito o un proceso?", ["Ocurre en un momento: el año 1818.", "Marca un cambio importante."], "Es un hito"),
        ("Proceso largo", "{F} ¿La adopción de la agricultura es un hito o un proceso?", ["Duró muchísimo tiempo y tuvo muchos cambios.", "No se puede fechar en un solo año."], "Es un proceso"),
    ],
    mistakes=[("Llamar hito a algo que dura mucho tiempo, como la independencia completa.", "Un hito ocurre en un momento; la independencia fue un proceso con varios hitos.", "Pregunta si tiene una fecha precisa (hito) o una duración (proceso)."),
              ("Confundir rasgo con hito.", "Los rasgos son características permanentes del periodo; el hito es un hecho puntual.", "Pregunta si describe cómo era el periodo o qué ocurrió en una fecha.")],
    T=[
        ("abc", "{F} ¿Cuál de estos es un hito?", "La proclamación de la independencia en 1818", "La adopción de la agricultura", "El proceso de independencia", "Ocurre en una fecha precisa y marca un cambio."),
        ("ab", "En HGCS: ¿qué es un proceso histórico?", "Un conjunto de cambios en un tiempo largo", "Un hecho de un solo día", "Los procesos duran años o siglos."),
        ("{F} ¿En qué año se formó la Primera Junta Nacional de Gobierno según la ficha?", "1810", "El resumen dice que en 1810 se formó la Primera Junta."),
        ("=", "{F} ¿Cuántos años duró el proceso de independencia contado de 1810 a 1818?", "1818-1810", "Se resta el año de inicio del año de proclamación.", " años"),
        ("abc", "{F} ¿Cuál de estos es un proceso?", "Los años de guerra y de organización de un gobierno propio", "La proclamación de 1818", "La formación de la Primera Junta en 1810", "Los años de guerra y de organización duraron mucho tiempo; las otras dos opciones son hechos de una fecha."),
        ("{F} ¿Cómo se llama el periodo en que grupos humanos pasaron a cultivar plantas y criar animales?", "Neolítico", "Neolítico es el nombre del periodo de la agricultura y la ganadería."),
        ("ab", "{F} La formación de la Primera Junta en 1810, ¿es un hito o un proceso?", "Un hito dentro del proceso de independencia", "Un proceso completo", "Es un hecho de una fecha que forma parte de un proceso mayor."),
        ("abc", "{F} ¿Qué relación hay entre el hito de 1818 y el proceso de independencia?", "El hito es un punto importante dentro del proceso", "Son lo mismo", "El hito ocurre antes del proceso", "Los hitos jalonan los procesos largos."),
        ("abc", "En la Colonia, un rasgo es que la Corona española gobernaba Chile. ¿Qué es eso?", "Un rasgo del periodo", "Un hito", "Un proceso", "Describe cómo era el periodo, no un hecho de un día."),
        ("abc", "Alguien dice: «La agricultura se inventó el día 5 de mayo de un año». ¿Qué problema tiene?", "Trata como hito algo que fue un proceso largo", "Usa números romanos", "Cita mal una década", "La agricultura se adoptó de forma gradual en milenios."),
        ("ab", "¿Por qué conviene nombrar hitos, procesos y rasgos para caracterizar un periodo?", "Porque cada uno muestra una parte distinta del periodo", "Porque son sinónimos", "Cada concepto aporta una mirada: fecha, duración y características."),
        ("abc", "{F} Si el proceso de independencia empezó en 1810, ¿qué hito marca su inicio según la ficha?", "La formación de la Primera Junta", "La proclamación de 1818", "La adopción de la agricultura", "La ficha ubica en 1810 el inicio del proceso."),
        ("abc", "{F} Para un esquema del periodo de independencia, ¿cuál es la mejor combinación?", "Hitos: 1810 y 1818; proceso: años de guerra y organización de gobierno propio", "Solo una fecha", "Solo rasgos de la Colonia", "Reúne hitos y proceso del mismo periodo."),
    ],
    ctx=("abc", "Una dirigente prepara un cartel sobre la historia de su organización: «Fundada en 1995 (hecho puntual). Durante diez años aumentó su número de socios. Se reúne cada mes». ¿Cuál es el proceso?", "El aumento de socios durante diez años", "La fundación en 1995", "La reunión mensual", "Los diez años de crecimiento son un conjunto de cambios en el tiempo."),
    sc=[("¿Cuál es la diferencia entre hito y proceso?", "El hito ocurre en un momento; el proceso dura un tiempo largo", "Se distinguen por la duración: un momento frente a un tiempo largo."),
        ("En HGCS: ¿qué es un rasgo de un periodo?", "Una característica que distingue un periodo", "Describe cómo era el periodo y no un hecho de un día."),
        ("En HGCS: ¿qué es el Neolítico?", "Periodo en que se empezó a cultivar y criar animales", "Se asocia a la adopción de la agricultura.")],
    op=("Ficha de ejemplo: «En 1900 se funda la escuela del pueblo de Las Colinas. En los años siguientes, más niñas y niños pasaron a la escuela. Los vecinos organizan una fiesta cada año». "
        "Clasifica cada afirmación como hito, proceso o rasgo, y explica en una frase por qué.",
        "Fundación de la escuela en 1900: hito (hecho puntual). Más niñas y niños asisten con los años: proceso (cambio en el tiempo). Fiesta anual: rasgo (característica que se repite).",
        ["clasifica bien las tres afirmaciones", "da una razón para cada una", "usa los tres términos"],
        ["tres frases con clasificación y razón"], ["llamar hito a todo", "no justificar"],
        "Pregunta: «¿Esto pasó en un momento o durante un tiempo?»."),
    reinforce="Nombra un hito y un proceso de tu barrio o de la historia de Chile.",
    extend="Explica con un ejemplo cómo un hito puede ser parte de varios procesos.",
)

# ======================================================= clase 3
F3 = ("Ficha 3 (resumen de ejemplo, escrito para este cuaderno). Antes de la llegada de los españoles, en el territorio de lo que hoy es Chile vivían muchos pueblos originarios distintos. "
      "Entre ellos estaban los aymara en el altiplano del norte, los diaguita en los valles del norte chico, los mapuche en el centro-sur y el sur, y el pueblo rapanui en Isla de Pascua; en el extremo sur vivían pueblos canoeros como los kawésqar y los yagán. "
      "Cada pueblo tenía su lengua, sus creencias y su forma de organizarse. Según el territorio, se vivía de la agricultura, la pesca, la caza o la recolección.")
build(
    O, 3, F3,
    use="Hoy sigo pasos para analizar una fuente y sacar los rasgos de un periodo: los pueblos originarios de Chile antes de la llegada de los españoles.",
    prior=["Distingo hito, proceso y rasgo.", "Obtengo datos de una fuente.", "Ubico periodos de Chile."],
    explain=[
        "Los pueblos originarios son los pueblos que vivían en el territorio antes de la llegada de los españoles en el siglo XVI. No eran uno solo: había varios, con lenguas, creencias y formas de vida distintas. Algunos de esos pueblos viven hoy en Chile y mantienen su cultura.",
        "Para analizar una fuente y sacar los rasgos de un periodo hay cuatro pasos. Primero, identifica qué tipo de fuente es y de cuándo. Segundo, subraya lo que dice sobre cómo vivían, qué hacían y cómo se organizaban. Tercero, escribe cada rasgo con tus palabras. Cuarto, revisa que no estés suponiendo cosas que la fuente no dice.",
        "Un rasgo general del periodo es la diversidad: pueblos distintos en territorios distintos, adaptados a su entorno. Decir «los indígenas eran todos iguales» sería un error. Para conocer en detalle la cultura de cada pueblo conviene consultar a sus comunidades y a especialistas.",
    ],
    vocab=[("pueblo originario", "pueblo que vivía en el territorio antes de la llegada de los españoles"), ("diversidad", "existencia de cosas distintas"), ("territorio", "espacio donde vive un grupo de personas"), ("recolección", "juntar frutos y plantas que da la naturaleza"), ("organización social", "forma en que un grupo se organiza para vivir")],
    worked=[
        ("Los cuatro pasos", "{F} Analiza la fuente.", ["Paso 1: es un resumen escrito, de ejemplo.", "Paso 2: dice que había muchos pueblos, con lenguas y creencias propias.", "Paso 3: rasgo: diversidad y adaptación al territorio.", "Paso 4: no dice cuántas personas había, así que no lo afirmo."], "Rasgos: diversidad de pueblos y formas de vida según el territorio"),
        ("Un rasgo según el territorio", "{F} ¿De qué podía vivir un pueblo en el extremo sur?", ["La ficha menciona pueblos canoeros.", "Los canoeros viven cerca del mar."], "Probablemente de la pesca y de recursos del mar: la ficha nombra la pesca como una forma de vida"),
    ],
    mistakes=[("Hablar de «los indígenas» como si fueran un solo pueblo.", "Había varios pueblos con lenguas y costumbres distintas.", "Nombra el pueblo y el territorio cuando se pueda."),
              ("Afirmar costumbres que la fuente no menciona.", "Se inventan datos y se falsea el pasado.", "Escribe solo lo que dice la fuente y consulta a especialistas para lo demás.")],
    T=[
        ("abc", "{F} ¿En qué zona vivían los aymara, según la ficha?", "En el altiplano del norte", "En Isla de Pascua", "En los valles del norte chico", "La ficha ubica a los aymara en el altiplano del norte."),
        ("ab", "{F} ¿Dónde vive el pueblo rapanui?", "En Isla de Pascua", "En el altiplano", "La ficha dice que el pueblo rapanui vive en Isla de Pascua."),
        ("En HGCS: ¿qué es un pueblo originario?", "Pueblo que vivía en el territorio antes de la llegada de los españoles", "Se refiere a quienes estaban antes de los españoles."),
        ("abc", "{F} ¿Qué pueblo vivía en los valles del norte chico?", "Diaguita", "Mapuche", "Kawésqar", "La ficha asigna los valles del norte chico a los diaguita."),
        ("ab", "{F} ¿Qué rasgo general destaca la ficha?", "La diversidad de pueblos y formas de vida", "Que todos eran iguales", "La ficha subraya que había muchos pueblos distintos."),
        ("{F} ¿Qué pueblo canoero nombra primero la ficha para el extremo sur?", "kawésqar", "La ficha nombra primero a los kawésqar y después a los yagán."),
        ("abc", "{F} ¿Qué actividad NO se menciona en la ficha como forma de vida?", "La minería industrial", "La pesca", "La agricultura", "La ficha nombra agricultura, pesca, caza y recolección; no la minería industrial."),
        ("abc", "{F} ¿Cuál es el paso 4 del análisis de una fuente?", "Revisar que no estoy suponiendo cosas que no dice", "Copiar la ficha completa", "Elegir la parte que más gusta", "El cuarto paso es la revisión crítica."),
        ("ab", "Una persona escribe: «Todos los pueblos originarios vivían de lo mismo». ¿Qué falla?", "La ficha dice que había diferencias según el territorio", "Nada, está bien", "Se vivía de la agricultura, pesca, caza o recolección según el lugar."),
        ("abc", "{F} ¿Por qué se menciona que cada pueblo tenía su lengua?", "Porque muestra la diversidad cultural", "Porque eran pocos", "Porque no se comunicaban", "Es un rasgo que ilustra las diferencias entre pueblos."),
        ("abc", "Alguien afirma: «Los mapuche vivían en el altiplano». Según la ficha, ¿qué corrección corresponde?", "Vivían en el centro-sur y el sur", "Vivían en Isla de Pascua", "Vivían en el extremo norte", "La ficha ubica a los mapuche en el centro-sur y el sur."),
        ("ab", "¿Qué conviene hacer para conocer en detalle la cultura de un pueblo?", "Consultar a sus comunidades y a especialistas", "Suponer detalles que parezcan lógicos", "Las comunidades y especialistas tienen el conocimiento más completo."),
        ("abc", "{F} ¿Qué descripción es la más cuidadosa?", "Antes del siglo XVI vivían varios pueblos con lenguas y formas de vida distintas según su territorio", "Todos los pueblos eran iguales", "Los pueblos desaparecieron", "Resume la ficha y no inventa."),
    ],
    ctx=("abc", "Un museo comunal prepara un panel para una escuela de adultos: «Pueblos originarios de Chile: viven desde antes del siglo XVI y mantienen su cultura hoy». Una visitante pregunta si es lo mismo hablar de «un pueblo» o de «varios pueblos». ¿Qué corresponde?", "Varios pueblos, cada uno con su cultura", "Un solo pueblo", "Ninguno", "La fuente destaca que había diversidad de pueblos y formas de vida."),
    sc=[("¿Qué dice la ficha sobre la cantidad de pueblos?", "Que había muchos pueblos distintos", "El rasgo central de la ficha es la diversidad de pueblos."),
        ("¿Qué hago al analizar una fuente?", "Identificarla, subrayar lo que dice, escribir los rasgos y revisar", "Son los cuatro pasos del método."),
        ("¿Dónde consulto para conocer en detalle una cultura?", "En las comunidades y con especialistas", "Ellas conocen mejor su cultura y pueden explicarla con precisión.")],
    op=("Ficha de ejemplo (inventada): «Según un resumen escrito para este cuaderno, un pueblo de la costa del norte vivía de la pesca, secaba pescado para guardarlo y se organizaba en comunidades». "
        "Sigue los cuatro pasos: identifica la fuente, escribe dos rasgos, indica qué NO dice la fuente y escribe una frase de conclusión.",
        "Fuente: resumen escrito de ejemplo. Rasgos: vivía de la pesca; secaba pescado. No dice: cuántas personas había ni sus creencias. Conclusión: vivía de la pesca y guardaba alimentos secándolos.",
        ["identifica la fuente", "escribe rasgos que están en el texto", "señala lo que no dice"],
        ["cuatro líneas escritas"], ["inventar costumbres", "no revisar"],
        "Pregunta: «¿Esto lo dice la fuente o lo estoy suponiendo?»."),
    reinforce="Elige un pueblo de la ficha y escribe dos cosas que la ficha dice de él.",
    extend="Explica por qué conviene consultar a las comunidades para conocer su cultura en detalle.",
)

# ======================================================= clase 4
F4 = ("Ficha 4 (resumen de ejemplo, escrito para este cuaderno, con límites aproximados). Conquista (siglo XVI): llegan los españoles al territorio de Chile; en 1541 se funda Santiago; hubo guerras, la muerte de muchas personas indígenas por la guerra y las enfermedades traídas, y un largo conflicto en la zona mapuche. "
      "Colonia (desde fines del siglo XVI hasta 1810): Chile era parte de los dominios de la Corona española; las autoridades eran nombradas desde la Corona; la economía se basaba en la agricultura y la minería; la sociedad era desigual y hubo mestizaje, es decir, mezcla de poblaciones indígena, española y africana; existió la encomienda, un sistema de trabajo obligado de indígenas.")
build(
    O, 4, F4,
    use="Hoy practico con apoyo para caracterizar la Conquista y la Colonia en Chile con una tabla de hitos, procesos y rasgos.",
    prior=["Distingo hito, proceso y rasgo.", "Ubico siglos y periodos.", "Analizo una fuente en cuatro pasos."],
    explain=[
        "La Conquista es el periodo de la llegada de los españoles, en el siglo XVI. Un hito es la fundación de Santiago en 1541. Fue un proceso con guerras, con muertes por la violencia y las enfermedades que llegaron, y con un conflicto largo en la zona mapuche. Fue un tiempo muy doloroso para los pueblos indígenas.",
        "La Colonia dura desde fines del siglo XVI hasta 1810. Sus rasgos principales: Chile dependía de la Corona española, las autoridades venían de España, la economía vivía de la agricultura y la minería, y la sociedad era desigual. Hubo mestizaje, es decir, mezcla de poblaciones, y también un sistema de trabajo obligado llamado encomienda.",
        "Para practicar, completa una tabla con tres columnas: hitos, procesos y rasgos. Así separas lo puntual de lo largo y de lo que caracteriza al periodo. Recuerda describir estos hechos con rigor y sin escoger bandos ni lenguaje que humille a nadie.",
    ],
    vocab=[("Conquista", "periodo de la llegada de los españoles al territorio de Chile, siglo XVI"), ("Colonia", "periodo en que Chile dependía de la Corona española"), ("Corona española", "autoridad máxima del reino de España"), ("mestizaje", "mezcla de poblaciones distintas"), ("encomienda", "sistema de trabajo obligado de indígenas en la Colonia")],
    worked=[
        ("Llenar la tabla", "{F} Clasifica: fundación de Santiago en 1541, economía de agricultura y minería, mestizaje.", ["La fundación es un hecho puntual: hito.", "El mestizaje es un cambio largo: proceso. La economía es una característica: rasgo."], "Hito: fundación de Santiago; proceso: mestizaje; rasgo: economía de agricultura y minería"),
        ("Ubicar en el periodo", "{F} Un documento de 1750 sobre una hacienda, ¿en qué periodo está?", ["1750 es del siglo XVIII.", "La Colonia llega hasta 1810."], "En la Colonia"),
    ],
    mistakes=[("Describir la Conquista solo como «el descubrimiento».", "Para los pueblos que ya vivían allí fue una conquista, con guerra y enfermedades.", "Usa un lenguaje preciso: llegada, conquista, fundación."),
              ("Creer que en la Colonia todas las personas tenían los mismos derechos.", "La sociedad era desigual.", "Describe que había diferencias según origen y condición.")],
    T=[
        ("abc", "{F} ¿Qué hito de 1541 se menciona?", "La fundación de Santiago", "La proclamación de la independencia", "La Primera Junta", "La ficha dice que en 1541 se funda Santiago."),
        ("ab", "{F} ¿En qué siglo ocurre la Conquista de Chile?", "XVI", "XVIII", "La ficha ubica la Conquista en el siglo XVI."),
        ("En HGCS: ¿qué autoridad gobernaba desde lejos a Chile en la Colonia?", "la Corona española", "La ficha dice que Chile dependía de la Corona española."),
        ("abc", "{F} ¿De qué vivía principalmente la economía colonial?", "De la agricultura y la minería", "De las fábricas de máquinas", "Del comercio por internet", "La ficha menciona agricultura y minería."),
        ("ab", "{F} ¿Qué es la encomienda?", "Un sistema de trabajo obligado de indígenas", "Una fiesta religiosa", "La ficha la define como sistema de trabajo obligado."),
        ("=", "{F} ¿Cuántos años pasaron entre la fundación de Santiago (1541) y la Primera Junta (1810)?", "1810-1541", "Se resta el año de inicio del año de término.", " años"),
        ("abc", "{F} ¿Qué es el mestizaje?", "Mezcla de poblaciones indígena, española y africana", "La separación de grupos", "La llegada de máquinas", "La ficha lo define como mezcla de poblaciones."),
        ("abc", "{F} Clasifica «la sociedad era desigual».", "Un rasgo de la Colonia", "Un hito de 1541", "Un proceso del siglo XX", "Describe una característica general del periodo y no un hecho puntual."),
        ("ab", "{F} Un documento de 1820 sobre una hacienda, ¿pertenece a la Colonia?", "No, es posterior a 1810", "Sí, es de la Colonia", "La Colonia llega hasta 1810; 1820 es parte del proceso de independencia y la República."),
        ("abc", "{F} ¿Cuál afirmación sobre la Conquista es cuidadosa?", "Hubo guerras y la muerte de muchas personas indígenas por la guerra y las enfermedades traídas", "Fue un tiempo sin conflictos", "Fue un tiempo feliz para todos", "Respeta lo que dice la fuente."),
        ("abc", "Alguien dice: «Los españoles trajeron la civilización a un territorio vacío». ¿Qué falla?", "El territorio ya estaba habitado por pueblos originarios con sus culturas", "Nada", "Fue en el siglo XX", "Antes de la llegada vivían muchos pueblos; hablar de vacío es erróneo."),
        ("ab", "¿Por qué conviene un lenguaje preciso al hablar de la Conquista?", "Porque fue un tiempo doloroso y se debe describir con rigor", "Porque nadie lo estudia", "El rigor evita negar el sufrimiento o simplificarlo."),
        ("abc", "{F} Elige la tabla bien completada:", "Hitos: fundación de Santiago, 1541; proceso: mestizaje; rasgo: dependencia de la Corona", "Hitos: la agricultura; proceso: 1541; rasgo: Santiago", "Todo en una sola columna", "Separa lo puntual, lo largo y lo característico."),
    ],
    ctx=("abc", "Un centro cultural exhibe un documento de ejemplo de 1680 sobre una hacienda: nombra al dueño y a un grupo de trabajadores indígenas «encomendados». ¿Qué rasgo de la Colonia ilustra?", "El trabajo obligado de indígenas", "El mestizaje en el siglo XX", "La independencia", "La encomienda fue un sistema de trabajo obligado."),
    sc=[("¿Qué es la Colonia?", "Periodo en que Chile dependía de la Corona española", "Va desde fines del siglo XVI hasta 1810."),
        ("En la Colonia de Chile: ¿qué es el mestizaje?", "Mezcla de poblaciones distintas", "Hubo mezcla de poblaciones indígena, española y africana."),
        ("¿Por qué no se dice que el territorio estaba vacío?", "Porque vivían pueblos originarios", "Decir que estaba vacío desconoce la existencia de los pueblos originarios.")],
    op=("Ficha de ejemplo: «En 1541 se funda Santiago. En los años siguientes hubo guerras y la población indígena disminuyó por la violencia y las enfermedades. Desde fines del siglo XVI, Chile dependía de la Corona española. La economía se basaba en haciendas y minas». "
        "Completa una tabla de tres columnas con hitos, procesos y rasgos. Añade una frase de síntesis sobre cada periodo.",
        "Hitos: fundación de Santiago, 1541. Procesos: disminución de la población indígena y guerras. Rasgos: dependencia de la Corona; economía de haciendas y minas. Síntesis: en la Conquista llegan los españoles y hay guerra; en la Colonia Chile depende de la Corona.",
        ["clasifica bien", "usa lenguaje preciso", "escribe una síntesis breve de cada periodo"],
        ["una tabla de tres columnas y dos frases"], ["usar «descubrimiento» sin matices", "mezclar columnas"],
        "Pregunta: «¿Esto es un hecho puntual, un cambio largo o una característica?»."),
    reinforce="Escribe tres palabras que resumen la Conquista y tres que resumen la Colonia.",
    extend="Explica por qué la misma época puede describirse distinto desde pueblos originarios y desde españoles.",
)

# ======================================================= clase 5
F5 = ("Ficha 5 (de ejemplo, general). Sociedad agraria antes de la Revolución Industrial (hasta el siglo XVIII): la mayoría de las personas vivía en el campo; se trabajaba con herramientas manuales y animales; se fabricaba en talleres pequeños; los viajes eran lentos. "
      "Revolución Industrial (desde fines del siglo XVIII y durante el siglo XIX): se inventan máquinas movidas por vapor; se construyen fábricas; crece la población de las ciudades; aparece el ferrocarril; muchas personas trabajan por un salario y se organizan en sindicatos para pedir mejores condiciones.")
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a un periodo de la humanidad: comparo la sociedad agraria con la Revolución Industrial y reconozco sus rasgos.",
    prior=["Describo antes y después de un cambio.", "Distingo hito, proceso y rasgo.", "Ubico siglos."],
    explain=[
        "La Revolución Industrial fue un proceso de cambios en la producción que comenzó a fines del siglo XVIII y siguió durante el siglo XIX. Se inventaron máquinas movidas por vapor, se abrieron fábricas y se construyeron ferrocarriles. Se dice «revolución» porque los cambios fueron muy profundos.",
        "Sus rasgos principales: más producción con máquinas, crecimiento de las ciudades, trabajo por salario y nuevas formas de organización de las personas que trabajan, como los sindicatos. Antes de este proceso, la mayor parte de la gente vivía en el campo y la producción era manual.",
        "Para comparar dos periodos usa una tabla: filas con aspectos (dónde vive la gente, cómo se produce, cómo se viaja) y dos columnas, una por periodo. Así ves los cambios sin juzgar a nadie y comprendes cómo se transformó la vida.",
    ],
    vocab=[("Revolución Industrial", "proceso de cambios en la producción desde fines del siglo XVIII, con máquinas y fábricas"), ("salario", "pago por el trabajo"), ("sindicato", "organización de trabajadores para defender sus derechos"), ("ferrocarril", "transporte en tren sobre rieles"), ("urbanización", "crecimiento de las ciudades")],
    worked=[
        ("Comparar con una tabla", "{F} Compara cómo se producía antes y después.", ["Antes: herramientas manuales y talleres pequeños.", "Después: máquinas movidas por vapor y fábricas."], "La producción pasó de lo manual a las máquinas y las fábricas"),
        ("Rasgo o hito", "{F} ¿La aparición del ferrocarril es un rasgo, un hito o un proceso de ese periodo?", ["Es un cambio de transporte que se expande con los años.", "Aparece como característica del periodo."], "Un rasgo (y parte de un proceso de transformación)"),
    ],
    mistakes=[("Pensar que la Revolución Industrial ocurrió en un solo día.", "Fue un proceso de más de un siglo.", "Habla de proceso y no de hito."),
              ("Describir solo las máquinas y olvidar a las personas.", "También cambió dónde vivía y cómo trabajaba la gente.", "Incluye la vida de las personas en la tabla.")],
    T=[
        ("abc", "{F} ¿Desde qué siglo comienza la Revolución Industrial, según la ficha?", "Fines del siglo XVIII", "Siglo V", "Siglo XX", "La ficha ubica el comienzo a fines del siglo XVIII."),
        ("ab", "{F} ¿Con qué se movían las máquinas de la Revolución Industrial?", "Con vapor", "Con electricidad de internet", "La ficha dice máquinas movidas por vapor."),
        ("En HGCS: ¿cómo se llama la organización de trabajadores para defender sus derechos?", "sindicato", "La ficha dice que se organizaban en sindicatos."),
        ("abc", "{F} ¿Dónde vivía la mayoría de las personas antes de la Revolución Industrial?", "En el campo", "En grandes ciudades", "En fábricas", "La ficha dice que la mayoría vivía en el campo."),
        ("ab", "{F} ¿Qué transporte aparece con la Revolución Industrial?", "El ferrocarril", "La carreta", "La ficha menciona el ferrocarril como novedad."),
        ("{F} ¿Cómo se llama el pago que recibían muchas personas por su trabajo en las fábricas?", "salario", "La ficha habla de personas que trabajan por un salario."),
        ("abc", "{F} ¿Qué pasó con las ciudades durante este proceso?", "Su población creció", "Su población desapareció", "Se quedaron vacías", "La ficha dice que creció la población de las ciudades."),
        ("abc", "{F} ¿Qué se fabricaba en el periodo anterior?", "Productos en talleres pequeños", "Máquinas de vapor", "Trenes", "La ficha dice que se fabricaba en talleres pequeños."),
        ("ab", "{F} ¿La Revolución Industrial es un hito o un proceso?", "Un proceso de más de un siglo", "Un hecho de un solo día", "La ficha la describe durante siglos XVIII y XIX."),
        ("abc", "{F} Una persona dice: «Antes todo era peor y ahora todo es mejor». ¿Qué problema tiene?", "Juzga con los valores de hoy en vez de describir rasgos", "Cita mal un siglo", "Usa números", "Conviene describir los cambios sin calificar a las personas ni a la época."),
        ("abc", "{F} ¿Por qué se organizaron los trabajadores en sindicatos?", "Para pedir mejores condiciones de trabajo", "Para fabricar más máquinas", "Para viajar en tren", "La ficha menciona ese motivo de forma directa."),
        ("ab", "¿Qué fila podría tener una tabla que compara dos periodos?", "Cómo se produce y cómo se viaja", "Los nombres de los museos", "Esas filas permiten comparar rasgos entre periodos."),
        ("abc", "{F} Elige la mejor síntesis del cambio:", "Se pasó de un trabajo manual en el campo a la producción con máquinas, la vida en ciudades y el trabajo por salario", "Todo siguió igual", "Solo cambiaron los nombres", "Resume los rasgos de la ficha."),
    ],
    ctx=("abc", "Un museo ferroviario de ejemplo muestra una máquina de vapor y una fotografía de una fábrica de 1860 con muchas trabajadoras y trabajadores. ¿Qué periodo de la humanidad ilustra?", "La Revolución Industrial", "La Prehistoria", "La Edad Media", "Máquinas de vapor y fábricas del siglo XIX son rasgos de la Revolución Industrial."),
    sc=[("¿Qué es la Revolución Industrial?", "Proceso de cambios en la producción con máquinas y fábricas", "Se inicia a fines del siglo XVIII."),
        ("En la Revolución Industrial: ¿qué es un sindicato?", "Organización de trabajadores", "Reúne a quienes trabajan para defender derechos."),
        ("¿Qué hago para comparar dos periodos?", "Uso una tabla con aspectos y dos columnas", "Permite ver los cambios con orden.")],
    op=("Tabla de ejemplo para completar: aspectos «dónde vive la gente», «cómo se produce», «cómo se viaja»; columnas «antes de la Revolución Industrial» y «durante la Revolución Industrial». "
        "Complétala con tus palabras usando la ficha y añade una frase sobre un cambio y una continuidad (por ejemplo, la necesidad de alimentos).",
        "Dónde vive: campo / ciudades que crecen. Producción: manual y talleres / máquinas y fábricas. Viajes: lentos / ferrocarril. Continuidad: las personas siguen necesitando alimentos y vivienda.",
        ["completa seis casillas", "usa datos de la ficha", "señala un cambio y una continuidad"],
        ["una tabla completa y una frase"], ["inventar datos", "no marcar la continuidad"],
        "Pregunta: «¿Qué dice la ficha sobre este aspecto?»."),
    reinforce="Nombra un objeto de tu casa que no existiría sin la producción en fábricas.",
    extend="Explica por qué el ferrocarril cambió la vida de las ciudades y del campo.",
)

# ======================================================= clase 6
F6 = ("Ficha 6 (resumen de ejemplo, general). En 1808, el rey de España fue apartado del trono y en las colonias americanas se discutió quién debía gobernar. "
      "En Chile, en 1810 se formó la Primera Junta Nacional de Gobierno y en 1818 se proclamó la independencia: hubo años de guerra. "
      "Luego se organizó la República: se redactaron constituciones y se eligieron autoridades, aunque no todas las personas podían participar. "
      "En el mundo, durante el siglo XIX, se extendieron las repúblicas en América y las fábricas en Europa.")
build(
    O, 6, F6,
    use="Hoy reviso lo logrado: junto hitos, procesos y rasgos de varios periodos y decido qué quiero repasar.",
    prior=["Describo periodos con hitos, procesos y rasgos.", "Ubico fechas y siglos.", "Comparo periodos con una tabla."],
    explain=[
        "El proceso de independencia de Chile no ocurrió de golpe. Comenzó cuando, en 1808, el rey de España fue apartado del trono y se debatió quién gobernaba. En 1810 se formó la Primera Junta, en 1818 se proclamó la independencia y hubo años de guerra. Después se organizó la República.",
        "La República es una forma de gobierno en que las autoridades son elegidas y no heredan el cargo. En el siglo XIX, en Chile, se redactaron constituciones y se eligieron autoridades, pero no todas las personas podían participar. Con el tiempo, más personas obtuvieron derechos.",
        "Para revisar tu aprendizaje, arma una tabla con los periodos que estudiaste: pueblos originarios, Conquista, Colonia, Independencia y República. Para cada uno escribe un hito, un proceso y un rasgo. Después marca con una cruz el que quieres repasar.",
    ],
    vocab=[("independencia", "momento en que un país deja de depender de otro y se gobierna solo"), ("República", "gobierno con autoridades elegidas y sin cargos heredados"), ("constitución", "ley principal que organiza un país"), ("Junta de Gobierno", "grupo que gobierna temporalmente"), ("síntesis", "resumen de lo más importante")],
    worked=[
        ("Hito, proceso y rasgo de un periodo", "{F} Caracteriza el periodo de la Independencia.", ["Hitos: 1810 (Primera Junta) y 1818 (proclamación).", "Proceso: años de guerra y organización de un gobierno propio. Rasgo: la discusión sobre quién debe gobernar."], "Hitos: 1810 y 1818; proceso: guerra y organización; rasgo: debate sobre quién gobierna"),
        ("Revisar una afirmación", "Alguien afirma: «En el siglo XIX todas las personas podían votar en Chile». {F} ¿Qué dice la ficha?", ["La ficha dice que no todas las personas podían participar.", "La afirmación contradice la ficha."], "No es correcta: no todos podían participar"),
    ],
    mistakes=[("Creer que con la independencia todos pasaron a tener los mismos derechos.", "Hubo personas que no podían participar y los derechos se ampliaron con el tiempo.", "Describe el proceso de ampliación sin simplificarlo."),
              ("Confundir Colonia y República.", "La Colonia dependía de la Corona; la República tiene gobierno propio con autoridades elegidas.", "Revisa quién gobierna en cada periodo.")],
    T=[
        ("abc", "{F} ¿Qué ocurrió en 1810 según la ficha?", "Se formó la Primera Junta Nacional de Gobierno", "Se proclamó la independencia", "Se fundó Santiago", "La ficha menciona esa organización de forma directa."),
        ("ab", "{F} ¿Qué se proclamó en 1818?", "La independencia de Chile", "La Primera Junta", "La ficha anota la proclamación de la independencia en 1818."),
        ("En HGCS: ¿cómo se llama la forma de gobierno con autoridades elegidas y sin cargos heredados?", "República", "Esa es la definición de República."),
        ("abc", "{F} ¿Qué pasó en 1808 según la ficha?", "El rey de España fue apartado del trono", "Se proclamó la independencia", "Se formó la República", "El debate sobre quién gobernar partió de ese hecho."),
        ("ab", "{F} ¿Qué hubo entre la Primera Junta y la proclamación?", "Años de guerra", "Años de paz total", "La ficha dice que hubo años de guerra."),
        ("=", "{F} ¿Cuántos años pasaron entre 1808 y 1818?", "1818-1808", "Se resta el año de inicio del año de la proclamación.", " años"),
        ("abc", "{F} ¿Qué se hizo para organizar la República?", "Se redactaron constituciones y se eligieron autoridades", "Se cerraron todas las ciudades", "Se volvió a la Colonia", "La ficha menciona ese hecho de forma directa."),
        ("abc", "{F} ¿Qué limitación señala la ficha sobre la participación?", "No todas las personas podían participar", "Todas votaban", "Nadie votaba", "La ficha dice que no todas las personas podían participar."),
        ("ab", "{F} La proclamación de 1818, ¿es hito o proceso?", "Hito", "Proceso", "Es un hecho puntual dentro del proceso de independencia."),
        ("abc", "¿Cuál es la diferencia principal entre la Colonia y la República?", "En la Colonia gobernaba la Corona española; en la República, autoridades propias elegidas", "No hay diferencia", "La República es anterior a la Colonia", "La Colonia dependía de España; la República tiene gobierno propio."),
        ("abc", "Ordena de más antiguo a más reciente: A) Colonia, B) pueblos originarios (antes del siglo XVI), C) República, D) Conquista. Escribe las letras.", "B, D, A, C", "A, B, C, D", "C, A, D, B", "Pueblos originarios, Conquista, Colonia y República siguen ese orden."),
        ("ab", "¿Por qué conviene marcar el tema que quieres repasar?", "Para decidir qué estudiar después", "Para borrar lo que ya sabes", "Marcarlo ayuda a planificar el estudio."),
        ("abc", "{F} Elige la síntesis mejor del periodo:", "Entre 1810 y 1818 Chile pasó por un proceso de independencia y luego organizó una República en la que no todos participaban", "Chile siempre fue independiente", "La independencia fue pacífica y sin debates", "Es coherente con todos los datos de la ficha."),
    ],
    ctx=("abc", "En un taller de historia local se arma un cuadro con cinco periodos. Una participante propone escribir como hito de la Colonia «proclamación de la independencia (1818)». ¿Qué corrige el grupo?", "Es un hito de la Independencia, no de la Colonia", "Es un rasgo de los pueblos originarios", "Está perfecto", "La Colonia llegó hasta 1810; 1818 pertenece al proceso de independencia."),
    sc=[("En HGCS: ¿qué es una República?", "Gobierno con autoridades elegidas, sin cargos heredados", "Se diferencia de la monarquía hereditaria."),
        ("¿Cuándo se formó la Primera Junta?", "1810", "Es el hito que abre el proceso de independencia."),
        ("¿Qué hago para repasar lo que aprendí?", "Armo una tabla con hito, proceso y rasgo de cada periodo", "Organiza el repaso por periodo y muestra qué falta.")],
    op=("Arma una síntesis de ejemplo con este esquema: periodos pueblos originarios, Conquista, Colonia, Independencia y República. Para cada uno escribe un hito o dato, un proceso y un rasgo, usando solo lo que aprendiste en este cuaderno. "
        "Marca con una cruz el periodo que quieres repasar y di por qué.",
        "Pueblos originarios: diversidad de pueblos (rasgo). Conquista: fundación de Santiago 1541 (hito). Colonia: dependencia de la Corona (rasgo). Independencia: 1810 y 1818 (hitos). República: constituciones y autoridades elegidas (rasgo). Quiero repasar la Colonia porque me cuesta ubicar los años.",
        ["completa los cinco periodos", "separa hito, proceso y rasgo", "elige qué repasar y justifica"],
        ["una tabla de cinco filas y una frase"], ["dejar casillas vacías", "mezclar periodos"],
        "Pregunta: «¿Qué periodo de la tabla no puedo explicar con mis palabras?»."),
    reinforce="Cuenta a otra persona, con tus palabras, qué pasó entre 1808 y 1818 en Chile.",
    extend="Explica qué cambió entre la Colonia y la República en la forma de gobernar.",
)
