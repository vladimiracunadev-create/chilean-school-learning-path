"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 15 (guerra del Pacífico, salitre y relaciones vecinales)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 15"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = "Línea de tiempo: 1874, tratado de límites entre Chile y Bolivia, que fija la frontera en el paralelo 24; 1878, Bolivia crea un impuesto a las exportaciones de una empresa chilena de salitre; 14 de febrero de 1879, tropas chilenas ocupan Antofagasta; 5 de abril de 1879, Chile declara la guerra a Bolivia y a Perú; 21 de mayo de 1879, combate naval de Iquique; 8 de octubre de 1879, combate naval de Angamos; 7 de junio de 1880, toma del Morro de Arica; enero de 1881, ocupación de Lima; 1883, tratado de Ancón con Perú; 1884, pacto de tregua con Bolivia."
build(
    OA, 1, F1,
    use="Aprenderé a ubicar en el tiempo y en el mapa la guerra del Pacífico y a explicar su relación con el salitre. Sirve para comprender cómo cambió el territorio de Chile y por qué el conflicto sigue siendo parte de las relaciones con los países vecinos.",
    prior=["Conozco la exploración y la ocupación del territorio en el siglo XIX.", "Sé qué es una frontera y un tratado.", "Sé leer una línea de tiempo."],
    explain=[
        "La guerra del Pacífico (1879-1884) enfrentó a Chile con Bolivia y Perú. Ocurrió en el desierto de Atacama, una zona con grandes depósitos de salitre, un mineral que se usaba como fertilizante y para fabricar explosivos, y que se vendía a los mercados del mundo atlántico. Por eso se habla de un conflicto económico en torno al salitre.",
        "Un tratado de 1874 había fijado la frontera entre Chile y Bolivia en el paralelo 24 y establecía que Bolivia no subiría los impuestos a las empresas chilenas. En 1878 Bolivia creó un nuevo impuesto a una empresa chilena de salitre; Chile consideró que se rompía el tratado y ocupó Antofagasta el 14 de febrero de 1879. El 5 de abril Chile declaró la guerra a Bolivia y a Perú, que tenían una alianza.",
        "La guerra se desarrolló en el mar y en tierra. Hubo combates navales, como los de Iquique y Angamos, y campañas terrestres que llegaron hasta Lima. Terminó con acuerdos que ampliaron el territorio chileno: con Perú, en 1883, y con Bolivia, en 1884 y 1904. Las causas fueron varias; no se explican solo por el salitre ni solo por la defensa del honor.",
    ],
    vocab=[("salitre", "mineral del desierto de Atacama usado como fertilizante y para explosivos"), ("paralelo 24", "línea imaginaria de latitud que se fijó como límite entre Chile y Bolivia en 1874"), ("alianza", "acuerdo entre países para ayudarse en caso de guerra"), ("campaña", "serie de operaciones militares con un objetivo"), ("tratado", "acuerdo escrito entre Estados")],
    worked=[
        ("Ubicar en el tiempo", "Con la línea de tiempo, ¿cuántos años pasaron entre el tratado de límites de 1874 y la declaración de guerra de 1879?",
         ["Busco las fechas: 1874 y 1879.", "Resto: 1879 - 1874."], "5 años"),
        ("Distinguir causas", "¿Por qué decir que la guerra se explica solo por el salitre sería incompleto?",
         ["El salitre es una causa económica.", "También hubo desacuerdos sobre tratados, impuestos y alianzas entre países."], "Porque hubo otras causas además del salitre"),
    ],
    mistakes=[
        ("Explicar la guerra solo por heroísmo.", "Dejaría fuera los intereses económicos y políticos.", "Distingue causas económicas, políticas y diplomáticas."),
        ("Creer que la guerra fue solo entre Chile y Perú.", "Bolivia también participó y la alianza fue entre Perú y Bolivia.", "Nombra a los tres países."),
    ],
    T=[
        ("En Historia: ¿qué es el salitre?", "Un mineral del desierto de Atacama usado como fertilizante y para explosivos", "Es el recurso en torno al cual giró el conflicto."),
        ("{F} ¿En qué fecha ocupan las tropas chilenas Antofagasta?", "14 de febrero de 1879", "La línea de tiempo lo indica."),
        ("{F} ¿Qué paralelo fijó el tratado de 1874 como frontera con Bolivia?", "El paralelo 24", "La línea lo señala."),
        ("En Historia: ¿qué es una alianza?", "Un acuerdo entre países para ayudarse en caso de guerra", "Perú y Bolivia estaban aliados."),
        ("{F} ¿Con qué país se firmó el tratado de Ancón? A) Bolivia, B) Perú, C) Argentina.", "B", "La línea lo indica."),
        ("Une cada país con su relación con la guerra: 1) Chile, 2) Bolivia, 3) Perú. a) aliado de Bolivia, b) ocupó Antofagasta, c) creó un impuesto en 1878. Escribe las parejas.", "1-b, 2-c, 3-a", "Cada país tuvo un papel distinto."),
        ("=", "{F} ¿Cuántos años pasaron entre la declaración de guerra de 1879 y el tratado de Ancón?", "1883-1879", "Se restan ambas fechas."),
        ("=", "{F} ¿Cuántos años pasaron entre el impuesto boliviano de 1878 y el pacto de tregua con Bolivia?", "1884-1878", "Se restan las dos fechas de la línea."),
        ("{F} Una compañera dice: «La guerra empezó porque Chile y Perú se declararon la guerra en 1874». ¿Qué corrección haces con la línea?", "En 1874 hubo un tratado con Bolivia; la guerra se declaró en 1879", "Mezcla fechas y países."),
        ("{F} ¿Qué dos combates navales se mencionan en la línea de tiempo?", "Iquique (21 de mayo de 1879) y Angamos (8 de octubre de 1879)", "La línea los menciona."),
        ("Explica por qué el conflicto puede llamarse económico en torno al salitre.", "Porque ocurrió en una zona con grandes depósitos de salitre que se exportaba a los mercados del mundo y había impuestos y empresas en disputa", "El recurso y sus impuestos estaban en el centro."),
        ("Evalúa la frase «la guerra del Pacífico se explica solo por el honor nacional». A) es incompleta porque también hubo causas económicas y diplomáticas, B) es correcta, C) es correcta porque hubo batallas.", "A", "Hubo varias causas."),
        ("Una persona dice: «Hoy los chilenos y los peruanos se odian por la guerra». ¿Qué problema tiene esa frase?", "Traslada un conflicto histórico a estereotipos actuales y generaliza sobre personas", "Es una generalización sin evidencia."),
    ],
    ctx=("Un afiche escolar dice: «Chile ganó territorios porque era mejor que sus vecinos». Escribe una frase que lo corrija con lo aprendido.", "La guerra tuvo causas económicas, políticas y diplomáticas, y terminó con acuerdos que ampliaron el territorio chileno", "La frase debe evitar estereotipos y mencionar causas."),
    sc=[("En Historia: ¿qué es un tratado?", "Un acuerdo escrito entre Estados", "Fija reglas como los límites."),
        ("¿Qué países se enfrentaron en la guerra del Pacífico?", "Chile contra Bolivia y Perú", "Es el esquema básico."),
        ("Nombra un hecho de 1879.", "Por ejemplo: la ocupación de Antofagasta o el combate de Iquique", "Están en la línea de tiempo.")],
    op=("{F} Con la línea de tiempo de arriba, escribe cinco líneas que expliquen cómo empezó la guerra del Pacífico. Nombra tres países, dos fechas y dos causas (una económica y una diplomática o política).",
        "La guerra empezó cuando Chile ocupó Antofagasta el 14 de febrero de 1879 tras el impuesto boliviano de 1878. El 5 de abril Chile declaró la guerra a Bolivia y a Perú, que estaban aliados. Una causa fue económica: el salitre; otra, diplomática: el desacuerdo sobre el tratado de 1874.",
        ["nombra tres países", "usa dos fechas", "dos causas distintas"], ["texto de cinco líneas"], ["explicar por una sola causa", "no usar fechas"], "Léele tu texto a alguien de tu casa y pídele que anote las fechas."),
    reinforce="Escribe las diez fechas de la línea de tiempo y, junto a cada una, una palabra que la resuma.",
    extend="Escribe una frase que explique por qué un impuesto puede generar un conflicto entre países.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = "Fuente A (cláusula de tratado, texto de ejemplo): «Los impuestos a las empresas de la otra parte no se aumentarán durante veinticinco años.» Fuente B (proclama oficial chilena, texto de ejemplo): «Chile defiende sus derechos y la libertad del comercio en el desierto.» Fuente C (carta de un soldado, texto de ejemplo): «Hemos marchado por arenales sin agua; la sed pesa más que el fusil.» Fuente D (periódico peruano, texto de ejemplo): «El país se prepara para defender su territorio y sus recursos.» Fuente E (tabla de ejemplo): el salitre exportado pasó de 100.000 toneladas en un año a 150.000 toneladas cinco años después."
build(
    OA, 2, F2,
    use="Aprenderé a leer fuentes de distintos países y tipos sobre la guerra del Pacífico, detectando intención, perspectiva y límites. Sirve para estudiar un conflicto sin quedarnos con un solo relato.",
    prior=["Conozco la cronología de la guerra.", "Distingo fuentes primarias y secundarias.", "Sé leer una tabla y calcular diferencias."],
    explain=[
        "Las fuentes de la guerra del Pacífico vienen de todos los bandos. Un tratado fija reglas jurídicas. Una proclama busca motivar a la población y justificar las acciones del gobierno. La carta de un soldado muestra la experiencia de quien combatió. Un periódico expresa la postura de su país y de su editor. Y una tabla de exportaciones entrega números sobre la economía.",
        "Para usarlas hay que preguntar quién habla, a quién le habla y para qué. La proclama chilena y el periódico peruano de ejemplo defienden sus respectivos países; no sirven para saber «la verdad» sino para conocer cómo cada gobierno presentaba la guerra. La carta de un soldado muestra sufrimiento, pero habla de una sola experiencia. La tabla muestra crecimiento, pero no dice quién se benefició.",
        "Por eso es importante contrastar: leer fuentes chilenas, peruanas y bolivianas, y combinar fuentes oficiales con testimonios personales. También conviene evitar el uso de estereotipos nacionales al interpretar las fuentes: ninguna fuente prueba cómo son «los chilenos», «los peruanos» o «los bolivianos» en general.",
    ],
    vocab=[("proclama", "texto con que un gobierno o jefe se dirige al público para motivarlo o justificar sus acciones"), ("propaganda", "información presentada para influir en la opinión de las personas"), ("testimonio", "relato de alguien que vivió un hecho"), ("estereotipo", "idea simplificada y generalizada sobre un grupo de personas"), ("tonelada", "unidad de masa equivalente a mil kilogramos")],
    worked=[
        ("Detectar intención", "¿Qué intención tienen la Fuente B (proclama chilena) y la Fuente D (periódico peruano)?",
         ["Ambas hablan de defender derechos o territorio.", "Buscan justificar la postura de cada país ante su público."], "Justificar y motivar a su propio público"),
        ("Calcular con la tabla", "En la Fuente E, ¿cuántas toneladas aumentó el salitre exportado?",
         ["Pasó de 100.000 a 150.000.", "Resto: 150.000 - 100.000."], "50.000 toneladas"),
    ],
    mistakes=[
        ("Creer que una proclama describe fielmente lo ocurrido.", "Busca convencer y justificar.", "Pregunta a quién habla y qué quiere lograr."),
        ("Usar una fuente para concluir cómo es «un pueblo».", "Una fuente muestra un caso, no un carácter nacional.", "Limita la conclusión a lo que dice la fuente."),
    ],
    T=[
        ("En Historia: ¿qué es una proclama?", "Un texto con que un gobierno se dirige al público para motivarlo o justificar sus acciones", "Es una fuente con intención."),
        ("{F} ¿Por cuántos años prometía el tratado de la Fuente A no aumentar los impuestos?", "Veinticinco años", "La cláusula lo indica."),
        ("En Historia: ¿qué es un estereotipo?", "Una idea simplificada y generalizada sobre un grupo de personas", "Debe evitarse al analizar el conflicto."),
        ("{F} ¿Qué dice el soldado de la Fuente C que pesa más que el fusil?", "La sed", "La carta lo dice."),
        ("{F} ¿La Fuente D es de qué país? A) Perú, B) Chile, C) Bolivia.", "A", "El enunciado de la fuente indica periódico peruano."),
        ("{F} Una compañera dice que la Fuente B prueba que Chile actuó solo por defender la libertad. ¿Qué corrección haces?", "Una proclama justifica y motiva; no prueba las causas reales del conflicto", "Tiene propósito político."),
        ("=", "En otra tabla de ejemplo, el salitre exportado pasó de 80.000 a 120.000 toneladas. ¿Cuántas toneladas aumentó?", "120000-80000", "Se resta la cifra inicial de la final."),
        ("=", "{F} ¿Qué porcentaje aumentó el salitre exportado entre las dos cifras de la Fuente E?", "(150000-100000)*100//100000", "Se divide el aumento entre la cifra inicial."),
        ("{F} ¿Qué fuente aporta la experiencia personal de la guerra? A) la A, B) la C, C) la E.", "B", "La carta de un soldado es un testimonio."),
        ("Explica por qué conviene leer fuentes chilenas, peruanas y bolivianas.", "Porque cada país presenta la guerra desde su perspectiva y contrastarlas da una visión más completa", "La contrastación reduce el sesgo."),
        ("{F} Redacta una conclusión de una frase con las Fuentes C y E sin exagerar.", "Mientras crecía la exportación de salitre, los soldados sufrían la falta de agua en el desierto", "Une economía y experiencia."),
        ("{F} Evalúa la frase «la Fuente C demuestra que todos los soldados chilenos eran valientes y todos los soldados peruanos cobardes». A) es un estereotipo sin evidencia, B) es correcta, C) es correcta porque es una carta.", "A", "Generaliza sobre grupos."),
        ("¿Qué fuente de Bolivia sumarías para completar el análisis? Escríbela y explica para qué.", "Por ejemplo: un diario boliviano de la época, para conocer cómo presentaba el impuesto y la guerra", "Completa la perspectiva faltante."),
    ],
    ctx=("{F} Un compañero copia la Fuente B en un afiche con el título «Así fue la guerra del Pacífico». ¿Qué fuentes agregarías para equilibrar?", "La Fuente D, para ver la perspectiva peruana, y la C, para ver la experiencia de un soldado", "Hay que contrastar voces de varios países."),
    sc=[("En Historia: ¿qué es la propaganda?", "Información presentada para influir en la opinión de las personas", "Una proclama puede serlo."),
        ("¿Qué es un testimonio?", "El relato de alguien que vivió un hecho", "La carta del soldado lo es."),
        ("¿Una tabla de exportaciones dice quién se benefició? Responde sí o no y por qué.", "No, porque solo muestra cantidades", "Es un límite de la fuente.")],
    op=("{F} Con las Fuentes A a E de arriba, escribe un párrafo de siete líneas que responda: «¿Qué muestran y qué ocultan estas fuentes sobre la guerra?». Incluye una fuente chilena, una peruana, un dato numérico y un límite.",
        "La proclama chilena justifica la acción del gobierno y el periódico peruano defiende el territorio de su país. La tabla muestra que el salitre exportado aumentó 50.000 toneladas, pero no dice quién se benefició. La carta del soldado muestra el sufrimiento por la sed. Límite: ninguna fuente prueba cómo son los habitantes de un país.",
        ["una fuente chilena", "una fuente peruana", "un dato numérico", "un límite"], ["párrafo de siete líneas"], ["tomar una proclama como verdad", "usar estereotipos"], "Pide a alguien de tu casa que revise que usaste una fuente de cada país."),
    reinforce="Haz una tabla con las Fuentes A a E: quién habla, qué dice y un límite.",
    extend="Escribe una frase que reemplace un estereotipo sobre «los peruanos» o «los bolivianos» por una afirmación basada en una fuente.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = "Cuadro de ejemplo. Cambio: Chile incorporó las provincias de Tarapacá y Antofagasta, ricas en salitre; Bolivia quedó sin costa marítima; el Estado aumentó sus ingresos por los impuestos a la exportación de salitre; miles de hombres fueron reclutados y volvieron muchos heridos; mujeres colaboraron como cantineras y enfermeras; crecieron las ciudades del norte. Continuidad: el desierto seguía siendo una zona de difícil acceso; la economía chilena seguía dependiendo de exportar recursos naturales; la hacienda y la minería continuaron en el centro y el norte chico; las fronteras con Argentina seguían por precisar."
build(
    OA, 3, F3,
    use="Aprenderé a distinguir qué cambió y qué continuó con la guerra del Pacífico en el territorio y en distintos ámbitos de la sociedad chilena. Sirve para evaluar el impacto de la guerra sin reducirlo a la victoria militar.",
    prior=["Conozco la cronología y las causas de la guerra.", "Sé distinguir cambio y continuidad.", "Sé qué es una escala."],
    explain=[
        "La guerra del Pacífico produjo cambios en varios ámbitos. En el territorio, Chile incorporó Tarapacá y Antofagasta, ampliando su superficie hacia el norte. En la economía, el Estado pasó a recibir ingresos por los impuestos a la exportación del salitre. En la sociedad, miles de hombres fueron reclutados y las mujeres participaron en tareas como cantineras y enfermeras. Y en las ciudades del norte aumentó la población.",
        "También hubo continuidades. La economía siguió siendo exportadora de recursos naturales: del cobre y el trigo se pasó a depender también del salitre. El desierto siguió siendo de difícil acceso, la hacienda continuó en el campo central, y las fronteras con Argentina todavía debían precisarse. Es decir, la victoria no transformó todo; amplió y reforzó modelos anteriores.",
        "Mirar varias escalas ayuda. A escala nacional, el Estado creció en territorio e ingresos; a escala regional, el norte se transformó con oficinas salitreras; a escala local, familias de soldados, enfermos y heridos vivieron costos personales. Un análisis completo incluye los ámbitos político, económico, social y territorial, y reconoce que los efectos no fueron iguales para todos.",
    ],
    vocab=[("ámbito", "área de la vida social: política, economía, sociedad o territorio"), ("cantinera", "mujer que acompañaba a las tropas y colaboraba con alimentos y cuidados"), ("reclutar", "reunir personas para que sirvan en el ejército"), ("ingreso fiscal", "dinero que recibe el Estado, por ejemplo por impuestos"), ("oficina salitrera", "instalación del desierto donde se extraía y procesaba el salitre")],
    worked=[
        ("Clasificar por ámbito", "Del cuadro de ejemplo: «el Estado aumentó sus ingresos por impuestos al salitre» y «las mujeres colaboraron como cantineras y enfermeras». ¿En qué ámbito entra cada una?",
         ["Los ingresos del Estado son un asunto económico.", "La participación de las mujeres es un asunto social."], "Ingresos: ámbito económico; mujeres: ámbito social"),
        ("Cambiar de escala", "A escala nacional, ¿qué cambió para Chile con la guerra? ¿Y a escala local?",
         ["Nacional: más territorio e ingresos.", "Local: familias con soldados reclutados y heridos."], "Nacional: territorio e ingresos; local: costos para las familias"),
    ],
    mistakes=[
        ("Reducir el impacto de la guerra a la ampliación del territorio.", "Hubo efectos sociales, económicos y políticos.", "Revisa los cuatro ámbitos."),
        ("Pensar que todos los chilenos tuvieron el mismo impacto.", "Soldados, mujeres, familias y empresarios vivieron la guerra de modo distinto.", "Indica a quién afectó cada cambio."),
    ],
    T=[
        ("En Historia: ¿qué es un ingreso fiscal?", "El dinero que recibe el Estado, por ejemplo por impuestos", "Aumentó con el salitre."),
        ("{F} ¿Qué provincias incorporó Chile según el cuadro?", "Tarapacá y Antofagasta", "El cuadro las nombra."),
        ("En Historia: ¿qué es reclutar?", "Reunir personas para que sirvan en el ejército", "Miles de hombres fueron reclutados."),
        ("{F} Clasifica como cambio o continuidad: «Bolivia quedó sin costa marítima».", "Cambio", "Es una consecuencia nueva de la guerra."),
        ("{F} Clasifica como cambio o continuidad: «la economía seguía dependiendo de exportar recursos naturales».", "Continuidad", "El cuadro lo lista como continuidad."),
        ("Elige el ámbito de la frase «mujeres como cantineras y enfermeras». A) social, B) fiscal, C) territorial.", "A", "Describe la participación de personas en la sociedad."),
        ("=", "Un regimiento de ejemplo salió con 900 hombres y regresó con 640. ¿Cuántos no regresaron?", "900-640", "Se resta los que regresaron del total."),
        ("=", "El Estado recibía 4 millones de pesos de ejemplo por impuestos antes de la guerra y 10 millones después. ¿Cuántos millones más recibe?", "10-4", "Se restan los ingresos antiguos."),
        ("Une cada dato con su ámbito: 1) nuevas provincias, 2) impuestos al salitre, 3) reclutamiento de soldados. a) social, b) económico, c) territorial. Escribe las parejas.", "1-c, 2-b, 3-a", "Cada dato corresponde a un ámbito."),
        ("Explica por qué decir que la guerra solo amplió el territorio es incompleto.", "Porque también cambió la economía del Estado, la vida de las familias y la participación de las mujeres", "Hubo cambios en varios ámbitos."),
        ("{F} Una compañera dice: «Con la guerra, Chile dejó de depender de recursos naturales». Corrige con un dato del cuadro.", "La economía seguía dependiendo de exportar recursos naturales como el salitre", "Hay continuidad en el modelo."),
        ("Evalúa la afirmación «la guerra amplió el territorio y reforzó una economía exportadora». A) es razonable, B) es falsa porque la guerra no cambió ni el territorio ni la economía, C) es falsa porque la guerra solo produjo cambios sociales.", "A", "Combina cambio y continuidad."),
        ("Propón una pregunta de escala local sobre la guerra.", "Por ejemplo: ¿cómo vivió una familia de un pueblo del sur la ausencia de un hijo soldado?", "La pregunta se ubica en un caso concreto."),
    ],
    ctx=("{F} Un video escolar afirma: «La guerra del Pacífico solo trajo beneficios a Chile». Con el cuadro, escribe una frase que lo matice.", "Trajo territorio e ingresos, pero también soldados muertos y heridos y costos para las familias", "La frase debe incluir beneficios y costos."),
    sc=[("En Historia: ¿qué es una cantinera?", "Una mujer que acompañaba a las tropas y colaboraba con alimentos y cuidados", "Es una forma de participación femenina."),
        ("Nombra un cambio territorial de la guerra.", "Chile incorporó Tarapacá y Antofagasta", "Está en el cuadro."),
        ("Nombra un ámbito de la sociedad que cambió.", "Por ejemplo: el económico o el social", "Hubo varios ámbitos afectados.")],
    op=("{F} Con el cuadro de ejemplo de arriba, construye una tabla de dos columnas (cambio y continuidad) con al menos cuatro filas, y escribe una frase final que mencione dos ámbitos distintos afectados por la guerra.",
        "Cambio: Chile incorpora Tarapacá y Antofagasta; cambio: más ingresos fiscales; cambio: reclutamiento de soldados; continuidad: economía exportadora; continuidad: desierto de difícil acceso. La guerra afectó el ámbito territorial y el social.",
        ["dos columnas", "cuatro filas", "dos ámbitos"], ["tabla y frase"], ["mencionar solo el territorio", "no clasificar"], "Revisa con alguien de tu casa que cada dato esté en su columna."),
    reinforce="Escribe cuatro datos del cuadro y clasifícalos por ámbito (territorial, económico, social, político).",
    extend="Escribe una pregunta sobre cómo cambió la vida de las ciudades del norte tras la guerra.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = "Voces de ejemplo, redactadas para este cuaderno. Presidente de Chile: «El tratado de 1874 se ha roto y debemos proteger el comercio y las inversiones.» Empresario del salitre: «Necesitamos que no suban los impuestos para seguir produciendo.» Soldado: «Marcho porque me reclutaron y espero regresar con mi familia.» Cantinera: «Llevo agua y alimentos y cuido a los heridos.» Gobernante boliviano: «Nuestro Estado necesita recursos y debe cobrar impuestos.» Periodista peruano: «Nuestro país está comprometido a defender su alianza.»"
build(
    OA, 4, F4,
    use="Aprenderé a identificar actores, intereses, causas y perspectivas de la guerra del Pacífico en Chile, Perú y Bolivia. Sirve para explicar un conflicto sin culpar a un solo grupo ni reducirlo a héroes y villanos.",
    prior=["Conozco la cronología y los ámbitos de impacto.", "Sé qué es la multicausalidad.", "Sé que cada voz tiene una perspectiva."],
    explain=[
        "En la guerra participaron muchos actores. Los gobiernos de Chile, Bolivia y Perú tomaban decisiones políticas y diplomáticas. Los empresarios del salitre, chilenos y extranjeros, tenían intereses económicos. Los soldados, reclutados en su mayoría entre la población trabajadora, cumplían órdenes. Las mujeres, como las cantineras, colaboraban en la retaguardia y en los campamentos. Y los trabajadores del salitre vivían en las oficinas del desierto.",
        "Las causas fueron varias: el valor económico del salitre, el desacuerdo sobre los impuestos y el tratado de 1874, la alianza secreta entre Perú y Bolivia, los límites poco claros en el desierto y las necesidades fiscales de los Estados. La multicausalidad evita explicar la guerra solo con una causa, como el honor o la ambición. Distintas fuentes ponen el acento en causas distintas.",
        "Las perspectivas varían. Un gobierno habla de derechos y territorio; un empresario, de producción; un soldado, de su deber y de su familia; una cantinera, de cuidado; un periodista, de la patria. Ninguna basta por sí sola para entender el conflicto. Y al estudiar a los países vecinos conviene evitar los estereotipos: hubo personas con distintos intereses en cada país.",
    ],
    vocab=[("retaguardia", "zona detrás del frente donde se apoya a quienes combaten"), ("alianza secreta", "acuerdo entre países que no se hace público"), ("necesidad fiscal", "necesidad del Estado de obtener dinero para sus gastos"), ("actor económico", "persona o empresa que participa en la producción y el comercio"), ("deber", "obligación de una persona hacia su país o comunidad")],
    worked=[
        ("Emparejar actor e interés", "¿Qué interés expresa el empresario del salitre y cuál el gobernante boliviano?",
         ["El empresario quiere que no suban los impuestos para seguir produciendo.", "El gobernante quiere recursos y cobrar impuestos."], "Empresario: impuestos bajos; gobernante: obtener recursos"),
        ("Contrastar perspectivas", "¿En qué se diferencian la voz del soldado y la del presidente?",
         ["El presidente habla de tratados, comercio e inversiones.", "El soldado habla de su reclutamiento y de su familia."], "El presidente, de política y comercio; el soldado, de su deber y su familia"),
    ],
    mistakes=[
        ("Explicar la guerra solo por heroísmo o solo por salitre.", "Hubo varias causas en juego.", "Ordena causas económicas, políticas y diplomáticas."),
        ("Convertir a un país entero en «bueno» o «malo».", "Dentro de cada país había intereses distintos.", "Habla de gobiernos, empresas y personas, no de países como bloques morales."),
    ],
    T=[
        ("En Historia: ¿qué es una necesidad fiscal?", "La necesidad del Estado de obtener dinero para sus gastos", "Explica la creación de impuestos."),
        ("{F} ¿Qué lleva la cantinera según su voz?", "Agua y alimentos, y cuida a los heridos", "Su voz lo dice."),
        ("En Historia: ¿qué es la retaguardia?", "La zona detrás del frente donde se apoya a quienes combaten", "Allí colaboraban muchas mujeres."),
        ("{F} ¿Qué espera el soldado?", "Regresar con su familia", "Su voz lo dice."),
        ("Une cada actor con su interés: 1) empresario, 2) presidente de Chile, 3) gobernante boliviano. a) cobrar impuestos para el Estado, b) proteger comercio e inversiones, c) que no suban los impuestos. Escribe las parejas.", "1-c, 2-b, 3-a", "Cada voz expresa un interés distinto."),
        ("{F} Elige el actor que representa la retaguardia. A) la cantinera, B) el presidente, C) el empresario.", "A", "Ella apoya a las tropas sin combatir."),
        ("=", "En un campamento de ejemplo hay 600 soldados y 25 cantineras. ¿Cuántas personas hay en total?", "600+25", "Se suman ambos grupos."),
        ("=", "Una oficina salitrera de ejemplo emplea 1.200 trabajadores y 300 se enrolan como soldados. ¿Cuántos siguen trabajando?", "1200-300", "Se resta los enrolados del total."),
        ("Una compañera dice: «La guerra fue solo por la ambición de los empresarios». Menciona otra causa que lo complete.", "El desacuerdo sobre el tratado de 1874 o la alianza entre Perú y Bolivia", "La multicausalidad incluye otras razones."),
        ("Explica por qué hablamos de multicausalidad al estudiar la guerra.", "Porque influyeron el salitre, los impuestos, el tratado, la alianza y los límites poco claros", "Varias causas se combinaron."),
        ("{F} ¿En qué se diferencian las perspectivas del soldado y del empresario?", "El soldado habla de deber y familia; el empresario, de producción y costos", "Sus lugares son distintos."),
        ("Evalúa la frase «todos los chilenos pensaban lo mismo sobre la guerra». A) es inexacta porque había intereses distintos, B) es correcta, C) es correcta porque todos compartían una misma patria.", "A", "No se debe homogeneizar."),
        ("Redacta una pregunta para contrastar la perspectiva de un gobierno con la de una cantinera.", "Por ejemplo: ¿qué cuenta cada uno de lo que vivió y qué deja fuera?", "La pregunta contrasta dos lugares."),
    ],
    ctx=("{F} En una dramatización escolar todos los personajes dicen «luchamos por la patria». Con las voces de ejemplo, ¿cómo harías hablar a la cantinera y al empresario?", "La cantinera hablaría de llevar agua y cuidar a los heridos; el empresario, de que no suban los impuestos", "Cada personaje debe hablar desde su interés."),
    sc=[("En Historia: ¿qué es la multicausalidad?", "La explicación de un hecho por varias causas a la vez", "Evita las explicaciones de una sola causa."),
        ("Nombra dos actores de la guerra.", "Por ejemplo: los soldados y los empresarios del salitre", "Ambos participaron en la guerra."),
        ("{F} ¿Qué quiere el gobernante boliviano de la voz de ejemplo?", "Recursos y cobrar impuestos", "Es su necesidad fiscal.")],
    op=("{F} Elige dos voces de ejemplo de arriba y escribe cinco líneas: qué busca cada una, una causa de la guerra y una diferencia de perspectiva entre ellas. No uses estereotipos sobre ningún país.",
        "El empresario quiere que no suban los impuestos y el gobernante boliviano quiere cobrarlos. Una causa fue el desacuerdo sobre el tratado de 1874. El empresario habla de producción; el gobernante, de recursos del Estado.",
        ["dos voces", "una causa", "diferencia de perspectiva", "sin estereotipos"], ["texto de cinco líneas"], ["culpar a un solo grupo", "usar estereotipos"], "Cuenta tu texto a alguien de tu casa y pídele que diga cuál es la diferencia."),
    reinforce="Haz una tabla con cinco actores y un interés para cada uno.",
    extend="Explica por qué es importante estudiar las voces de los tres países.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = "Dossier de ejemplo. Dato 1: el tratado de 1874 fijó el paralelo 24 y limitó los impuestos a empresas chilenas; en 1878 Bolivia creó un nuevo impuesto. Dato 2: el salitre del desierto de Atacama se exportaba a los mercados del mundo. Dato 3: la guerra (1879-1884) terminó con el tratado de Ancón con Perú (1883) y el pacto de tregua con Bolivia (1884). Dato 4: Chile incorporó Tarapacá y Antofagasta y aumentaron sus ingresos fiscales. Dato 5: miles de hombres fueron reclutados y las mujeres colaboraron como cantineras y enfermeras."
build(
    OA, 5, F5,
    use="Aprenderé a construir un argumento sobre las causas y el impacto de la guerra del Pacífico, con evidencia y límite. Sirve para explicar el conflicto en sus ámbitos económico, político, social y territorial sin recurrir a estereotipos.",
    prior=["Conozco la cronología, los actores y las fuentes.", "Sé distinguir cambio y continuidad.", "Sé usar tesis, evidencia y límite."],
    explain=[
        "Un argumento sobre la guerra del Pacífico responde a una pregunta como «¿Cuáles fueron las causas económicas de la guerra y cuál fue su impacto en la sociedad chilena?». Una tesis posible es que el conflicto en torno al salitre y a los impuestos desencadenó una guerra que amplió el territorio y los ingresos de Chile, pero con costos sociales importantes.",
        "Las evidencias se explican. Los datos 1 y 2 sostienen la causa económica: el tratado, el impuesto y el valor del salitre. El dato 4 muestra el impacto territorial y fiscal. El dato 5 muestra el impacto social: miles de reclutados y mujeres colaborando. El dato 3 ubica el fin de la guerra en acuerdos con Perú y Bolivia. Cada dato se explica con «esto muestra que…».",
        "El límite: con el dossier no podemos medir cuántas personas murieron ni cómo vivió cada familia, ni afirmar que la causa económica fuera la única. Tampoco debemos extender la guerra a estereotipos actuales: el dossier habla de gobiernos, empresas y personas del siglo XIX, no de «cómo son» los habitantes de hoy.",
    ],
    vocab=[("tesis", "afirmación principal que se defiende"), ("evidencia", "dato que apoya la tesis"), ("impacto", "efecto que un hecho produce en la sociedad"), ("causa económica", "razón relacionada con recursos, impuestos o producción"), ("límite", "aquello que la evidencia no permite afirmar")],
    worked=[
        ("Elegir evidencias", "Para sostener la causa económica, ¿qué datos del dossier sirven?",
         ["El dato 1 muestra el tratado y el impuesto de 1878.", "El dato 2 muestra el valor del salitre."], "Los datos 1 y 2"),
        ("Detectar exageración", "¿Por qué la frase «la guerra solo trajo beneficios» excede el dossier?",
         ["El dato 4 muestra territorio e ingresos.", "El dato 5 muestra miles de reclutados y mujeres colaborando, es decir, costos sociales."], "Porque hubo costos sociales además de beneficios"),
    ],
    mistakes=[
        ("Escribir una tesis sin mencionar la causa económica.", "Omite el salitre y los impuestos.", "Incluye los datos 1 y 2."),
        ("Usar la victoria para opinar sobre los habitantes de los países vecinos.", "Es un estereotipo sin evidencia.", "Limita la conclusión a gobiernos y procesos."),
    ],
    T=[
        ("En Historia: ¿qué es un impacto?", "El efecto que un hecho produce en la sociedad", "Se estudia en ámbitos distintos."),
        ("{F} ¿Qué dato muestra el impacto territorial y fiscal? A) dato 2, B) dato 4, C) dato 5.", "B", "El dato 4 habla de territorio e ingresos."),
        ("{F} ¿Qué dato muestra el impacto social?", "El dato 5", "Habla de reclutados y mujeres."),
        ("{F} ¿Con qué país se firmó el tratado de Ancón según el dato 3?", "Perú", "El dato lo señala."),
        ("Elige la tesis mejor formulada. A) La guerra fue solo heroísmo, B) El conflicto en torno al salitre y los impuestos desencadenó una guerra que amplió el territorio y los ingresos de Chile, con costos sociales, C) Los países vecinos son malos.", "B", "Es defendible con el dossier."),
        ("Una compañera usa solo el dato 4 para decir que «la guerra solo trajo beneficios». ¿Qué dato le falta considerar?", "El dato 5, que muestra los costos sociales", "La evidencia es parcial."),
        ("=", "{F} Si el dossier tiene 5 datos y 2 sostienen la causa económica (1 y 2), ¿cuántos datos quedan para otros temas?", "5-2", "Se restan los datos usados."),
        ("=", "Un grupo escribe un texto de 16 líneas: 2 de tesis, 10 de evidencias y el resto de límite. ¿Cuántas líneas son de límite?", "16-2-10", "Se restan tesis y evidencias del total."),
        ("{F} Con los datos 4 y 5, redacta una conclusión proporcional.", "Chile incorporó territorio y aumentó sus ingresos, pero miles de hombres fueron reclutados y las mujeres colaboraron en la guerra", "Une beneficios y costos."),
        ("Explica por qué una buena tesis sobre la guerra debe incluir una causa económica.", "Porque el salitre y los impuestos estuvieron en el origen del conflicto", "Los datos 1 y 2 lo muestran."),
        ("Un compañero escribe: «Los peruanos y bolivianos son enemigos naturales de Chile». Señala el problema.", "Es un estereotipo sin evidencia y traslada el conflicto histórico a la actualidad", "El dossier habla de gobiernos del siglo XIX."),
        ("Evalúa este argumento: «El salitre y los impuestos (datos 1 y 2) causaron un conflicto que amplió el territorio (dato 4) y reclutó a miles de hombres (dato 5)». A) es sólido porque usa varios tipos de evidencia, B) es débil porque solo explica causas y no menciona ningún impacto, C) es falso porque la guerra no tuvo ningún efecto en Chile.", "A", "Une causa e impacto."),
        ("Escribe una pregunta que exigiría otra fuente para completar el argumento.", "Por ejemplo: ¿qué vivieron las poblaciones del norte que cambiaron de Estado?", "La pregunta indica un vacío del dossier."),
    ],
    ctx=("{F} En una charla escolar alguien dice que «Chile ganó la guerra por ser un pueblo superior». Con el dossier, escribe tu respuesta en dos frases con una evidencia.", "El dossier explica causas económicas y políticas y no muestra superioridad de ningún pueblo; el dato 1 habla de tratados e impuestos", "La respuesta debe evitar el estereotipo."),
    sc=[("En Historia: ¿qué es una causa económica?", "Una razón relacionada con recursos, impuestos o producción", "El salitre lo ilustra."),
        ("{F} Nombra un dato del dossier sobre el impacto social.", "Miles de hombres fueron reclutados", "Es el dato 5."),
        ("{F} ¿Qué tratado puso fin a la guerra con Perú?", "El tratado de Ancón de 1883", "Está en el dato 3.")],
    op=("{F} Con el dossier de ejemplo de arriba, escribe un párrafo de ocho líneas que responda: «¿Cuáles fueron las causas económicas de la guerra y cuál fue su impacto en la sociedad chilena?». Incluye una tesis, tres evidencias explicadas y un límite, sin estereotipos.",
        "El conflicto por el salitre y los impuestos desencadenó la guerra. El tratado de 1874 limitaba los impuestos y en 1878 Bolivia creó uno nuevo. Chile incorporó Tarapacá y Antofagasta y aumentó sus ingresos fiscales, pero miles de hombres fueron reclutados y las mujeres colaboraron como cantineras. Límite: el dossier no mide cuántas personas murieron.",
        ["tesis", "tres evidencias explicadas", "límite"], ["párrafo de ocho líneas"], ["usar estereotipos", "no explicar los datos"], "Pide a alguien de tu casa que marque tu tesis y tus tres evidencias."),
    reinforce="Escribe tu tesis en una frase y anota las tres evidencias que la apoyan.",
    extend="Escribe una segunda tesis sobre el impacto social de la guerra y un dato nuevo que necesitarías.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 6
F6 = "Resumen de ejemplo para evaluar proyecciones. 1883: tratado de Ancón, por el que Perú cede Tarapacá, mientras Tacna y Arica quedan bajo administración chilena por diez años. 1884: pacto de tregua con Bolivia. 1904: tratado de paz y amistad con Bolivia, que reconoce el territorio chileno y asegura libre tránsito de mercaderías bolivianas por puertos chilenos. 1929: tratado de Lima, que deja Arica en Chile y Tacna en Perú. 2014: la Corte Internacional de Justicia fija el límite marítimo entre Chile y Perú. 2018: la Corte Internacional de Justicia concluye que Chile no tiene la obligación de negociar un acceso soberano al mar para Bolivia."
build(
    OA, 6, F6,
    use="Aprenderé a evaluar cómo la guerra del Pacífico proyectó consecuencias hasta hoy en las relaciones de Chile con Perú y Bolivia, y qué tratados y fallos las ordenaron. Sirve para entender conflictos actuales con fuentes y sin estereotipos.",
    prior=["Conozco la guerra, sus causas y su impacto.", "Sé qué es un tratado.", "Sé evaluar evidencias y límites."],
    explain=[
        "El fin de la guerra no cerró todos los asuntos pendientes. El tratado de Ancón (1883) dejó que Perú cediera Tarapacá y que Tacna y Arica quedaran bajo administración chilena por diez años; la situación de esas ciudades se resolvió en 1929, con el tratado de Lima: Arica quedó en Chile y Tacna volvió a Perú. Con Bolivia, un pacto de tregua en 1884 y un tratado de paz en 1904 fijaron los límites y aseguraron libre tránsito de mercaderías bolivianas por puertos chilenos.",
        "Estos acuerdos explican por qué la relación con los vecinos conserva temas sensibles. Bolivia perdió su costa marítima y ha planteado en distintos momentos su aspiración de acceso al mar. En 2018 la Corte Internacional de Justicia concluyó que Chile no tiene la obligación de negociar ese acceso. Con Perú, en 2014 la Corte fijó el límite marítimo entre ambos países. Estos fallos muestran que hoy los conflictos se resuelven en instancias internacionales.",
        "Evaluar una proyección implica pensar en el largo plazo y en los límites de nuestro conocimiento. Podemos describir tratados y fallos, pero no podemos afirmar cómo piensan todas las personas de cada país. Una buena evaluación distingue lo jurídico (tratados y fallos), lo diplomático (relaciones entre Estados) y lo social (memorias y actitudes), y evita estereotipos.",
    ],
    vocab=[("libre tránsito", "derecho a pasar mercaderías por el territorio de otro país, por ejemplo, hacia un puerto"), ("acceso soberano al mar", "salida al mar sobre la cual un Estado tiene autoridad exclusiva"), ("Corte Internacional de Justicia", "tribunal de las Naciones Unidas que resuelve disputas entre Estados"), ("límite marítimo", "línea que separa los espacios del mar de dos Estados"), ("relaciones vecinales", "vínculos políticos, económicos y culturales entre países vecinos")],
    worked=[
        ("Ordenar por fecha", "Con el resumen, ¿cuántos años pasaron entre el tratado de Ancón y el tratado de Lima?",
         ["Busco las fechas: 1883 y 1929.", "Resto: 1929 - 1883."], "46 años"),
        ("Distinguir lo jurídico y lo social", "¿Un fallo de la Corte Internacional de Justicia permite saber lo que piensa cada persona de Chile, Perú o Bolivia?",
         ["Un fallo resuelve una disputa jurídica entre Estados.", "No mide opiniones personales."], "No: el fallo es jurídico y no mide opiniones"),
    ],
    mistakes=[
        ("Creer que los tratados cerraron para siempre todos los temas.", "Siguieron existiendo discusiones diplomáticas.", "Revisa los hitos posteriores."),
        ("Usar los fallos para generalizar sobre los habitantes de un país.", "Un fallo resuelve una disputa jurídica entre Estados.", "Habla de Estados, no de «los chilenos» o «los bolivianos»."),
    ],
    T=[
        ("En Historia: ¿qué es el libre tránsito?", "El derecho a pasar mercaderías por el territorio de otro país", "Se estableció para Bolivia en 1904."),
        ("{F} ¿En qué año se firmó el tratado de Lima?", "1929", "El resumen lo indica."),
        ("En Historia: ¿qué es la Corte Internacional de Justicia?", "Un tribunal de las Naciones Unidas que resuelve disputas entre Estados", "Dictó los fallos de 2014 y 2018."),
        ("{F} ¿Qué quedó en Chile y qué volvió a Perú según el tratado de Lima? A) Arica en Chile y Tacna en Perú, B) Tacna en Chile y Arica en Perú, C) ambas en Perú.", "A", "El resumen lo dice."),
        ("{F} ¿Qué fijó la Corte en 2014?", "El límite marítimo entre Chile y Perú", "El resumen lo dice."),
        ("{F} ¿Qué concluyó la Corte en 2018 sobre el acceso al mar para Bolivia?", "Que Chile no tiene la obligación de negociar un acceso soberano al mar", "El resumen lo dice."),
        ("=", "{F} ¿Cuántos años pasaron entre el tratado de paz con Bolivia de 1904 y el fallo de 2018?", "2018-1904", "Se restan ambas fechas."),
        ("=", "{F} ¿Cuántos años pasaron entre el pacto de tregua con Bolivia de 1884 y el tratado de Lima?", "1929-1884", "Se restan las fechas del resumen."),
        ("Une cada tratado o fallo con su resultado: 1) Ancón (1883), 2) paz con Bolivia (1904), 3) Lima (1929). a) libre tránsito de mercaderías, b) Tarapacá cedida y administración de Tacna y Arica, c) Arica en Chile y Tacna en Perú. Escribe las parejas.", "1-b, 2-a, 3-c", "Cada tratado tuvo un resultado propio."),
        ("Explica por qué la guerra del Pacífico sigue siendo importante para las relaciones vecinales.", "Porque sus resultados territoriales y los tratados posteriores siguen presentes en temas como el acceso al mar y los límites", "Sus proyecciones llegan hasta hoy."),
        ("Una compañera dice: «Como hubo una guerra hace más de 140 años, hoy los pueblos siguen peleando». Corrige con lo aprendido.", "Hoy las diferencias entre Estados se resuelven en instancias internacionales, como la Corte, y no se puede generalizar sobre los pueblos", "Los fallos de 2014 y 2018 lo muestran."),
        ("Evalúa la afirmación «los fallos de 2014 y 2018 son pruebas de que los habitantes de los tres países se odian». A) es falsa porque son resoluciones jurídicas entre Estados, B) es correcta, C) es correcta porque los fallos favorecieron a un solo país.", "A", "Un fallo no mide sentimientos."),
        ("Propón una pregunta para seguir investigando las relaciones vecinales.", "Por ejemplo: ¿cómo cooperan hoy Chile, Perú y Bolivia en comercio y cultura?", "La pregunta amplía la mirada a la cooperación."),
    ],
    ctx=("{F} Un compañero escribe en un trabajo «la guerra del Pacífico fue solo un conflicto del pasado sin consecuencias hoy». Con el resumen, escribe una frase que lo corrija.", "Los tratados y los fallos de 2014 y 2018 muestran que sus consecuencias siguen presentes en los límites y en el acceso al mar", "La corrección usa hitos posteriores."),
    sc=[("En Historia: ¿qué es un límite marítimo?", "La línea que separa los espacios del mar de dos Estados", "Fue fijado en 2014 entre Chile y Perú."),
        ("Nombra un tratado posterior a la guerra.", "Por ejemplo: el de Ancón (1883) o el de Lima (1929)", "Están en el resumen."),
        ("¿Dónde se resuelven hoy muchas disputas entre Estados?", "En tribunales internacionales como la Corte Internacional de Justicia", "Es una vía pacífica.")],
    op=("{F} Con el resumen de ejemplo de arriba, escribe un párrafo de ocho líneas que evalúe la proyección de la guerra: nombra dos tratados, un fallo, una consecuencia para Bolivia, una para Perú y un límite de lo que sabemos, sin estereotipos.",
        "El tratado de Ancón (1883) cedió Tarapacá y dejó Tacna y Arica en administración chilena; el de Lima (1929) las repartió. El tratado de 1904 con Bolivia aseguró libre tránsito de mercaderías, aunque Bolivia perdió su costa. En 2014 la Corte fijó el límite marítimo con Perú. Límite: los fallos no miden lo que piensan las personas.",
        ["dos tratados", "un fallo", "consecuencia para Bolivia y Perú", "un límite"], ["párrafo de ocho líneas"], ["usar estereotipos", "omitir el límite"], "Pide a alguien de tu casa que revise que nombraste dos tratados y un fallo."),
    reinforce="Haz una tabla con los seis hitos del resumen (1883, 1884, 1904, 1929, 2014 y 2018) y una palabra para cada uno.",
    extend="Escribe una pregunta sobre cómo se puede enseñar este tema sin fomentar estereotipos.",
    materials=MAT,
)
