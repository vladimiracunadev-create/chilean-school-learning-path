"""Material del estudiante de 7.º básico, Historia, Geografía y Ciencias Sociales: OA 04 (primeras civilizaciones en perspectiva comparada)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI07 OA 04"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (fechas redondeadas y aproximadas, hechas para este cuaderno). Los años a. C. se cuentan hacia atrás: 3500 a. C. es más antiguo que 3100 a. C. "
     "Mesopotamia: entre los ríos Tigris y Éufrates (hoy Irak); ciudades-Estado desde 3500 a. C. hasta 539 a. C. "
     "Egipto: valle del río Nilo, en África; reino unificado desde 3100 a. C. hasta 30 a. C. "
     "Valle del Indo: ríos Indo y vecinos (hoy Pakistán e India); ciudades como Harappa y Mohenjo-Daro desde 2600 a. C. hasta 1900 a. C. "
     "China: río Amarillo (Huang He); dinastía Shang desde 1600 a. C. hasta 1046 a. C.")
build(
    OA, 1, F,
    use="Aprenderé a ubicar las primeras civilizaciones en el tiempo y en el espacio. Sirve para no mezclar épocas ni lugares al compararlas.",
    prior=["Sé qué es un Estado.", "Sé leer una línea de tiempo.", "Sé ubicar continentes y ríos en un mapa."],
    explain=[
        "Una civilización es una sociedad compleja con ciudades, Estados, escritura y especialización del trabajo. Las primeras civilizaciones surgieron junto a grandes ríos, donde había agua y tierra fértil: Mesopotamia entre los ríos Tigris y Éufrates, Egipto en el valle del Nilo, el valle del Indo y China junto al río Amarillo.",
        "Para compararlas hay que ubicarlas bien. Los años antes de Cristo (a. C.) se cuentan hacia atrás: mientras mayor es el número, más antiguo es el hecho. Así, 3500 a. C. es anterior a 3100 a. C. Las cuatro civilizaciones no surgieron al mismo tiempo: Mesopotamia fue la primera, y Egipto y el Indo coexistieron por varios siglos.",
        "Ubicar bien evita errores como creer que todas ocurrieron a la vez o que un solo lugar fue el centro de todo. Al comparar, recuerda que las fechas son aproximadas y que las civilizaciones no eran bloques uniformes: cambiaron durante cientos o miles de años. Antes de comparar rasgos, siempre se responde cuándo y dónde.",
    ],
    vocab=[("civilización", "sociedad compleja con ciudades, Estado, escritura y trabajo especializado"), ("a. C.", "antes de Cristo: años que se cuentan hacia atrás"), ("valle", "tierra baja junto a un río"), ("coexistir", "existir al mismo tiempo en distintos lugares"), ("dinastía", "serie de gobernantes de una misma familia")],
    worked=[
        ("Comparar años a. C.", "{F} ¿Cuántos años antes comenzó Mesopotamia que Egipto?", ["Los años a. C. se restan: 3500 − 3100.", "El resultado es 400."], "400 años antes"),
        ("Ordenar civilizaciones", "Si un reino empieza en 2000 a. C. y otro en 1500 a. C., ¿cuál es más antiguo?", ["En a. C., el número mayor es más antiguo.", "2000 es mayor que 1500."], "El que empieza en 2000 a. C."),
    ],
    mistakes=[("Creer que 1500 a. C. es más antiguo que 3000 a. C. porque «el número es menor».", "Se cuentan los años a. C. como si fueran d. C.", "En a. C. el número mayor es el más antiguo."),
              ("Suponer que las cuatro civilizaciones surgieron a la vez.", "Se mira la lista sin las fechas.", "Mesopotamia fue la primera y la dinastía Shang comenzó 1.900 años después.")],
    T=[
        ("{F} ¿Junto a qué río surgió Egipto?", "Junto al Nilo", "La ficha lo indica."),
        ("{F} ¿Entre qué dos ríos se ubicó Mesopotamia?", "Entre el Tigris y el Éufrates", "La ficha lo indica."),
        ("{F} ¿Qué civilización de la ficha es la más antigua?", "Mesopotamia", "Su fecha, 3500 a. C., es la mayor."),
        ("=", "{F} ¿Cuántos años antes comenzó Egipto que el valle del Indo?", "3100-2600", "Se restan los años a. C.", " años"),
        ("{F} Ordena de la más antigua a la más reciente: dinastía Shang, valle del Indo, Egipto, Mesopotamia.", "Mesopotamia, Egipto, valle del Indo, dinastía Shang", "Los años son 3500, 3100, 2600 y 1600 a. C."),
        ("{F} ¿En qué continente está el río Nilo?", "En África", "La ficha ubica a Egipto en África."),
        ("=", "{F} ¿Cuántos años duró el valle del Indo con ciudades, según la ficha?", "2600-1900", "Se resta el año final al inicial.", " años"),
        ("=", "{F} ¿Cuántos años transcurrieron entre el fin del valle del Indo y el comienzo de la dinastía Shang?", "1900-1600", "Se restan los dos años a. C.", " años"),
        ("{F} ¿Coexistieron Egipto y el valle del Indo? Explica con las fechas.", "Sí: Egipto existió de 3100 a 30 a. C. y el Indo de 2600 a 1900 a. C., así que se superponen", "El Indo está dentro del periodo de Egipto."),
        ("{F} Camila dice: «Las cuatro civilizaciones surgieron todas al mismo tiempo». Corrígela con dos fechas de la ficha.", "No: Mesopotamia desde 3500 a. C. y la dinastía Shang desde 1600 a. C., 1.900 años después", "Las fechas de inicio son muy distintas."),
        ("{F} Un compañero dice que 3500 a. C. es más reciente que 1600 a. C. porque 3500 es un número mayor, como pasa con los años d. C. ¿Qué error comete?", "Se cuentan los años a. C. hacia atrás: el número mayor, 3500, es el más antiguo", "En a. C. el orden se invierte."),
        ("{F} ¿Coexistieron el valle del Indo y la dinastía Shang? Explica.", "No: el Indo terminó en 1900 a. C. y la dinastía Shang comenzó en 1600 a. C., 300 años después", "Entre el fin del Indo y el inicio de Shang no hubo superposición."),
        ("=", "{F} ¿Cuántos años duró Egipto como reino unificado según la ficha?", "3100-30", "Se resta el año final al inicial.", " años"),
    ],
    ctx=("Un afiche escolar dice «Egipto es la civilización más antigua del mundo». Usa las fechas de la ficha para corregirlo. {F}", "Mesopotamia comenzó en 3500 a. C., antes que Egipto en 3100 a. C.", "El afiche ignora la fecha de Mesopotamia."),
    sc=[("¿Qué significa a. C.?", "Antes de Cristo, años que se cuentan hacia atrás", "Un número mayor es más antiguo."),
        ("¿Cuál es más antigua: 2800 a. C. o 2300 a. C.?", "2800 a. C.", "El número mayor es el más antiguo en a. C."),
        ("{F} ¿Cuál de estos ríos está en África: el Nilo o el Tigris?", "El Nilo", "La ficha ubica a Egipto y su río en África.")],
    op=("Dibuja una línea de tiempo de 3500 a. C. a 500 a. C. con la escala 1 cm = 250 años (12 cm en total). Marca el inicio de las cuatro civilizaciones de la ficha y el fin de las tres que terminan dentro de ese tramo (Mesopotamia, Indo y Shang), con colores distintos. {F}",
        "Mesopotamia de 3500 a 539 a. C.; Egipto desde 3100 a. C. (a 1,6 cm del comienzo); Indo de 2600 a 1900 a. C.; Shang de 1600 a 1046 a. C.",
        ["usa la escala", "marca inicio y fin", "las civilizaciones se distinguen por color"], ["línea de tiempo dibujada"], ["invertir el orden de los años a. C.", "no respetar la escala"],
        "Pide que explique cuáles civilizaciones coexistieron según su línea."),
    reinforce="Di en voz alta las cuatro civilizaciones con su río y su año de inicio.",
    extend="Escribe una pregunta sobre qué ocurría en otros lugares del mundo mientras surgían estas civilizaciones.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (datos resumidos, hechos para este cuaderno). "
     "Mesopotamia: llanura entre dos ríos cuyas crecidas son irregulares y poco predecibles; no hay piedra ni madera cerca; casas y templos de ladrillo de barro; canales de riego. "
     "Egipto: el Nilo crece cada año en una época casi regular y deja limo (barro fértil); desiertos a ambos lados protegen el valle; hay piedra abundante; ciudades y aldeas junto al río. "
     "Valle del Indo: ríos con crecidas; ciudades planificadas con calles en cuadrícula, desagües y pozos; ladrillos cocidos con medidas en proporción 1:2:4 (por ejemplo, 7 cm × 14 cm × 28 cm). "
     "China (río Amarillo): el río arrastra limo fértil y sus crecidas fuertes obligaron a construir diques; aldeas de tierra apisonada y murallas.")
build(
    OA, 2, F,
    use="Aprenderé a comparar cómo el ambiente y las decisiones humanas dieron forma a los asentamientos de las primeras civilizaciones. Sirve para explicar semejanzas y diferencias sin simplificar.",
    prior=["Sé ubicar las cuatro civilizaciones.", "Sé qué es un factor geográfico.", "Sé que el riego y los excedentes ayudaron a crear ciudades."],
    explain=[
        "Las cuatro civilizaciones surgieron junto a ríos, pero sus ambientes eran distintos. El Nilo crece en una época casi regular y deja limo fértil; los ríos de Mesopotamia crecen de manera más irregular; el río Amarillo tiene crecidas fuertes. Cada sociedad debió organizar canales, diques y almacenamiento de agua de manera diferente.",
        "Los materiales disponibles también influyeron. En Mesopotamia faltaban piedra y madera cerca, por lo que se construyó con ladrillo de barro. En Egipto había piedra abundante, y se construyó con ella. En el Indo, las ciudades planificadas usaron ladrillos cocidos de medidas uniformes. Así, los asentamientos reflejan ambiente y decisiones de sus habitantes.",
        "El ambiente no lo determinó todo. Dos ciudades junto a ríos pueden ser muy distintas, porque las personas toman decisiones: planificar calles, construir diques, levantar templos. Al comparar se contrastan ambiente, recursos y decisiones, y se evita decir que una civilización fue mejor que otra solo por su geografía.",
    ],
    vocab=[("limo", "barro muy fértil que deja un río al crecer"), ("crecida", "aumento fuerte del caudal de un río"), ("dique", "muro que contiene el agua de un río"), ("ciudad planificada", "ciudad trazada con un plan previo, con calles ordenadas"), ("ladrillo cocido", "ladrillo de arcilla endurecido al fuego")],
    worked=[
        ("Relacionar ambiente y material", "{F} ¿Por qué en Mesopotamia se usaba ladrillo de barro?", ["La ficha dice que no hay piedra ni madera cerca.", "El barro era el material disponible."], "Porque faltaban piedra y madera cerca"),
        ("Usar una proporción", "{F} Un ladrillo del Indo mide 5 cm de alto y sigue la proporción 1:2:4. ¿Cuánto mide de largo?", ["La proporción 1:2:4 indica alto, ancho y largo.", "Largo = 5 × 4 = 20."], "20 cm"),
    ],
    mistakes=[("Decir que todos los ríos se comportan igual.", "Se generaliza a partir de un solo río.", "Compara el Nilo, el Éufrates y el río Amarillo: tienen crecidas distintas."),
              ("Explicar una ciudad solo por su ambiente.", "Se piensa que la geografía lo determina todo.", "Agrega las decisiones de las personas: planificar, construir diques, elegir materiales.")],
    T=[
        ("{F} ¿Qué material usaban en Mesopotamia para casas y templos?", "Ladrillo de barro", "La ficha lo indica."),
        ("{F} ¿Qué deja el Nilo al crecer?", "Limo fértil", "La ficha lo dice."),
        ("{F} ¿Qué protegía el valle del Nilo a ambos lados?", "Los desiertos", "La ficha lo dice."),
        ("{F} ¿Qué tenían las ciudades del Indo para sacar el agua usada?", "Desagües", "La ficha lo indica."),
        ("{F} ¿Cuál río tiene crecidas más regulares: el Nilo o los ríos de Mesopotamia?", "El Nilo", "La ficha dice que crece en una época casi regular."),
        ("{F} ¿Qué construyeron en China para enfrentar las crecidas fuertes del río Amarillo?", "Diques", "La ficha lo indica."),
        ("=", "{F} Un ladrillo del Indo mide 6 cm de alto con la proporción 1:2:4. ¿Cuánto mide de largo?", "6*4", "Se multiplica el alto por la parte mayor de la proporción.", " cm"),
        ("=", "{F} Una ciudad del Indo tiene 8 calles en un sentido y 5 en el otro, formando una cuadrícula. ¿Cuántos cruces hay?", "8*5", "Cada calle de un sentido cruza todas las del otro.", " cruces"),
        ("{F} Una ciudad tiene calles en cuadrícula y desagües iguales en cada casa. ¿Sugiere (A) un plan previo o (B) que cada familia construyó por su cuenta?", "A) un plan previo", "Un plan previo explica el trazado uniforme."),
        ("{F} Ana dice: «El Nilo y los ríos de Mesopotamia se comportaban igual». Corrígela.", "El Nilo crece en una época casi regular, mientras las crecidas de Mesopotamia son irregulares y poco predecibles", "La ficha lo contrasta."),
        ("{F} Mesopotamia y el Indo están junto a ríos. ¿Qué diferencia en sus ciudades muestra que el ambiente no lo determinó todo?", "El Indo trazó ciudades en cuadrícula con desagües; Mesopotamia construyó templos de barro y canales: hubo decisiones distintas", "Con ríos parecidos, las ciudades fueron distintas."),
        ("{F} ¿Qué problema comparten el río Amarillo y los ríos de Mesopotamia y qué solución usó China?", "Las crecidas; China construyó diques", "La ficha menciona crecidas en ambos y diques en China."),
        ("{F} Un compañero dice: «Egipto fue mejor porque tenía piedra». Corrígelo.", "La piedra explica un material, no una superioridad; Mesopotamia hizo grandes obras con ladrillo de barro", "No se mide superioridad con el ambiente."),
    ],
    ctx=("Un equipo arqueológico halla una ciudad con calles en cuadrícula y desagües iguales y piensa que no es de Mesopotamia. ¿Con qué rasgo de la ficha lo relaciona? {F}", "Con las ciudades planificadas del valle del Indo", "El trazado en cuadrícula con desagües es rasgo del Indo."),
    sc=[("¿Qué es el limo?", "Barro muy fértil que deja un río al crecer", "Mejora los campos."),
        ("¿Qué es un dique?", "Un muro que contiene el agua de un río", "Ayuda a enfrentar crecidas."),
        ("=", "{F} Un ladrillo del Indo mide 3 cm de alto con la proporción 1:2:4. ¿Cuánto mide de ancho?", "3*2", "El ancho es el doble del alto.", " cm")],
    op=("Haz un cuadro con las cuatro civilizaciones de la ficha: ambiente, material de construcción y una decisión humana de cada una. Después escribe una frase que explique por qué no todo se explica por el ambiente. {F}",
        "Egipto: valle del Nilo, piedra, aldeas junto al río; decisión: construir con piedra.",
        ["completa las cuatro civilizaciones", "distingue ambiente y decisión", "la frase evita el determinismo"], ["cuadro escrito", "frase escrita"], ["mezclar ambiente y decisión", "decir que una civilización es superior por su ambiente"],
        "Pide que explique qué decisión pudo cambiar el asentamiento aunque el ambiente fuera el mismo."),
    reinforce="Nombra un material y un ambiente de cada civilización.",
    extend="Escribe una pregunta sobre cómo se repartía el agua en una ciudad de Mesopotamia.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (datos resumidos, hechos para este cuaderno). "
     "Mesopotamia: ciudades-Estado con reyes y templos; escritura cuneiforme en tablillas de arcilla; usaban la rueda, el arado y el bronce; comerciaban cebada, lana y textiles, y recibían metales y madera de otras regiones. "
     "Egipto: reino gobernado por un faraón con funcionarios; escritura jeroglífica en piedra y papiro; usaban cobre y bronce y barcos a vela y barcazas por el Nilo; recibían oro de Nubia y madera de cedro desde el Líbano. "
     "Valle del Indo: no hay evidencia clara de reyes ni palacios; sellos de piedra con signos aún no descifrados; pesas de piedra de medidas uniformes; cuentas de cornalina (piedra roja) fabricadas en talleres; sellos del Indo hallados en Mesopotamia. "
     "China (dinastía Shang): rey que consultaba a los antepasados; escritura sobre huesos y caparazones; objetos rituales de bronce; carros tirados por caballos.")
build(
    OA, 3, F,
    use="Aprenderé a contrastar la organización política, la tecnología y el intercambio de las primeras civilizaciones. Sirve para comparar con criterios claros y no con juicios.",
    prior=["Sé ubicar y describir el ambiente de cada civilización.", "Sé qué es un Estado y un tributo.", "Sé distinguir descripción e interpretación."],
    explain=[
        "Al comparar civilizaciones se eligen criterios y se aplican a todas por igual. Tres criterios útiles son la organización política (quién gobierna y cómo), la tecnología (herramientas, escritura, materiales) y el intercambio (qué se compra, vende o regala, y con quién).",
        "En organización, Mesopotamia tuvo ciudades-Estado con reyes y templos, y Egipto un reino con faraón. En el Indo, los hallazgos no muestran claramente reyes ni palacios, por lo que no sabemos cómo se gobernaba. En tecnología, usaron escrituras muy distintas: cuneiforme, jeroglífica, signos de sellos y huesos con inscripciones. En Mesopotamia, Egipto y China se trabajó el bronce.",
        "En intercambio, Egipto obtenía oro de Nubia y cedro del Líbano; el Indo y Mesopotamia se conectaron, como muestran sellos del Indo hallados en Mesopotamia. Esos hallazgos permiten hablar de contacto, no de dominio. La ficha no lista todo lo que cada civilización sabía hacer, así que no se puede decir que una sea más avanzada solo por lo que aparece o no en un resumen.",
    ],
    vocab=[("criterio", "aspecto que se usa para comparar"), ("cuneiforme", "escritura de signos en forma de cuña sobre arcilla"), ("jeroglífico", "escritura egipcia con signos que son dibujos"), ("sello", "pieza con signos o figuras para marcar o identificar"), ("contacto", "relación entre sociedades distintas, por ejemplo por comercio")],
    worked=[
        ("Comparar con un criterio", "{F} ¿Qué escritura usaban en Mesopotamia y cuál en Egipto?", ["Busco la tecnología de cada una.", "Mesopotamia: cuneiforme; Egipto: jeroglífica."], "Cuneiforme y jeroglífica"),
        ("Calcular viajes", "Una barcaza transporta 8 troncos de cedro por viaje. ¿Cuántos viajes necesita para llevar 40 troncos?", ["Divido: 40 ÷ 8 = 5.", "Cada viaje lleva 8 troncos, así que 5 viajes completan los 40."], "5 viajes"),
    ],
    mistakes=[("Decir que una civilización era más avanzada porque en la ficha aparecen más tecnologías.", "Se confunde el resumen con lo que de verdad sabían hacer.", "Compara con el mismo criterio y reconoce que la ficha no lista todo."),
              ("Afirmar que el Indo era gobernado por reyes como Egipto.", "Se aplica un modelo de otra civilización.", "Los hallazgos del Indo no muestran claramente reyes ni palacios; di que no se sabe.")],
    T=[
        ("{F} ¿Dónde se hallaron sellos del Indo?", "En Mesopotamia", "La ficha lo indica."),
        ("{F} ¿Qué recibía Egipto de Nubia?", "Oro", "La ficha lo indica."),
        ("{F} ¿Sobre qué escribían en la dinastía Shang?", "Huesos y caparazones", "La ficha lo indica."),
        ("{F} ¿Qué civilización de la ficha no tiene evidencia clara de reyes ni palacios?", "El valle del Indo", "La ficha lo dice."),
        ("{F} Relaciona cada escritura con su civilización: cuneiforme, jeroglífica, huesos con inscripciones.", "Cuneiforme: Mesopotamia; jeroglífica: Egipto; huesos con inscripciones: Shang", "La ficha las describe así."),
        ("{F} ¿En qué tres civilizaciones de la ficha se menciona el bronce?", "Mesopotamia, Egipto y la dinastía Shang", "La ficha lo nombra en esas tres."),
        ("=", "{F} Una barcaza lleva 12 troncos de cedro por viaje. ¿Cuántos viajes necesita para transportar 60 troncos?", "60//12", "Se divide el total por lo que cabe en cada viaje.", " viajes"),
        ("{F} ¿Qué diferencia de organización hay entre Mesopotamia y Egipto?", "Mesopotamia tuvo ciudades-Estado con reyes; Egipto, un reino gobernado por un faraón", "La ficha lo contrasta."),
        ("{F} Clasifica cada dato como organización (O), tecnología (T) o intercambio (I): 1) un faraón con funcionarios; 2) escritura cuneiforme; 3) oro que llega desde Nubia; 4) uso de la rueda.", "1 O, 2 T, 3 I, 4 T", "Cada dato responde a un criterio distinto."),
        ("{F} ¿Qué conclusión es más prudente sobre los sellos del Indo hallados en Mesopotamia? A) Hubo contacto entre ambas regiones; B) El Indo gobernaba Mesopotamia.", "A) Hubo contacto entre ambas regiones", "Un objeto lejos de su origen muestra contacto, no dominio."),
        ("{F} Lucía dice: «La civilización del Indo era menos avanzada porque no se menciona un rey». Corrígela.", "No se puede medir el nivel por la falta de un dato; el Indo tuvo ciudades planificadas, pesas y talleres", "La ficha muestra otros logros y los hallazgos no muestran reyes."),
        ("{F} Si se hallaran sellos del Indo también en Egipto, ¿qué sugeriría?", "Que el Indo tuvo contactos o intercambios con más regiones", "Más objetos lejos de su origen amplían la red de contacto."),
        ("{F} Un compañero dice: «Egipto era un solo gobernante y Mesopotamia muchos». ¿Qué parte de la ficha lo respalda?", "Egipto era un reino con faraón; Mesopotamia tenía ciudades-Estado con reyes", "La ficha lo indica."),
    ],
    ctx=("Para una feria escolar, un curso compara las civilizaciones con una tabla de tres columnas: política, tecnología e intercambio. Elige en qué columna va «oro de Nubia». {F}", "En intercambio", "El oro llega por comercio desde otra región."),
    sc=[("En Historia: ¿Qué es un criterio de comparación?", "Un aspecto que se usa para comparar, como organización, tecnología o intercambio", "Se aplica a todas las civilizaciones."),
        ("¿Es prudente decir que la civilización del Indo fue gobernada por reyes?", "No, porque los hallazgos no lo muestran con claridad", "Hay que declarar el límite de la evidencia."),
        ("=", "{F} Si cada viaje de una barcaza lleva 4 troncos de cedro, ¿cuántos troncos transporta en 9 viajes?", "4*9", "Se multiplican los troncos por los viajes.", " troncos")],
    op=("Haz una tabla con tres criterios (organización, tecnología, intercambio) y las cuatro civilizaciones. Completa cada celda con un dato de la ficha y escribe una celda como «no se sabe» cuando falte evidencia. {F}",
        "Organización: Mesopotamia, ciudades-Estado; Egipto, faraón; Indo, no hay evidencia clara; Shang, rey que consultaba antepasados.",
        ["completa las celdas con datos de la ficha", "usa los mismos criterios para todas", "reconoce al menos un «no se sabe»"], ["tabla escrita"], ["comparar con criterios distintos", "llenar los vacíos con suposiciones"],
        "Pide que explique por qué el Indo no se puede describir con el modelo de Egipto."),
    reinforce="Explica con tus palabras qué es un criterio de comparación.",
    extend="Escribe una pregunta sobre cómo se pudo transmitir una técnica entre dos civilizaciones.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (datos resumidos, hechos para este cuaderno). "
     "Diferencias internas: en Mesopotamia, las ciudades de Ur y Uruk tenían sus propios reyes y a veces se enfrentaban; hacia 2300 a. C., Sargón de Acad unió varias ciudades bajo su mando. "
     "Egipto tuvo épocas de unidad, llamadas Reino Antiguo, Reino Medio y Reino Nuevo, y épocas de división entre ellas. "
     "Contactos: Egipto comerciaba y a veces combatía con Nubia, al sur; sellos del Indo se encontraron en Mesopotamia. "
     "En América del Sur, en el valle de Supe (Perú), la ciudad de Caral tiene pirámides de piedra y una antigüedad de unos 5.000 años; no hay evidencia de contacto con las civilizaciones de otros continentes. "
     "Otras civilizaciones del mismo tipo: la minoica, en la isla de Creta (desde unos 2000 a. C.); la fenicia, en la costa del actual Líbano (desde unos 1200 a. C.); la olmeca, en Mesoamérica (desde unos 1200 a. C.); y la chavín, en los Andes de Perú (desde unos 900 a. C.).")
build(
    OA, 4, F,
    use="Aprenderé a reconocer diferencias dentro de cada civilización y los contactos entre ellas. Sirve para no presentar a las civilizaciones como bloques uniformes ni aislados.",
    prior=["Sé comparar organización, tecnología e intercambio.", "Sé ubicar las civilizaciones en el tiempo y el espacio.", "Sé qué es una ciudad-Estado."],
    explain=[
        "Una civilización no era un bloque uniforme. En Mesopotamia, ciudades como Ur y Uruk tenían reyes propios y a veces se enfrentaban; hacia 2300 a. C., Sargón de Acad unió varias bajo su mando. En Egipto hubo épocas de unidad, como el Reino Antiguo, el Medio y el Nuevo, y épocas de división. Hablar de «los egipcios» o «los mesopotámicos» oculta esos cambios.",
        "Las civilizaciones tampoco estaban aisladas. Egipto comerciaba y a veces combatía con Nubia; sellos del Indo aparecen en Mesopotamia, lo que muestra contactos por comercio. Estos contactos permitían que circularan objetos, ideas y técnicas. Un contacto no implica dominio: dos sociedades pueden intercambiar sin que una gobierne a la otra.",
        "Además, no todas las civilizaciones se relacionaron entre sí. En el valle de Supe, en Perú, Caral levantó pirámides hace unos 5.000 años; no hay evidencia de contacto con las civilizaciones de Mesopotamia, Egipto, el Indo o China. Esto muestra que ciudades complejas pueden surgir de manera independiente. Algo parecido ocurrió con la civilización minoica en Creta, la fenicia en la costa del actual Líbano, la olmeca en Mesoamérica y la chavín en los Andes: procesos similares en lugares y tiempos muy distintos. Comparar no es medir quién fue mejor, sino entender cada caso en su contexto.",
    ],
    vocab=[("diferencia interna", "variación dentro de una misma civilización, según lugar o época"), ("unidad política", "situación en que un solo gobierno controla un territorio"), ("contacto", "relación entre sociedades por comercio, guerra o viajes"), ("dominio", "control de una sociedad sobre otra"), ("desarrollo independiente", "surgimiento de algo sin influencia de otras sociedades")],
    worked=[
        ("Reconocer una diferencia interna", "{F} ¿Qué muestra que Mesopotamia no era un bloque uniforme?", ["La ficha dice que Ur y Uruk tenían reyes propios.", "A veces se enfrentaban."], "Que sus ciudades tenían reyes propios y se enfrentaban"),
        ("Calcular una distancia en el tiempo", "Un hecho ocurre en 2300 a. C. y otro en 1900 a. C. ¿Cuántos años los separan?", ["Resto: 2300 − 1900 = 400.", "En a. C. el número mayor es el más antiguo, por eso se resta el menor al mayor."], "400 años"),
    ],
    mistakes=[("Hablar de «los egipcios» como si hubieran pensado y vivido igual durante miles de años.", "Se ignoran los cambios y divisiones.", "Indica la época y la región: Reino Antiguo, Medio o Nuevo."),
              ("Creer que si dos civilizaciones tienen contacto, una gobierna a la otra.", "Se confunde contacto con dominio.", "Los sellos del Indo en Mesopotamia muestran intercambio, no que una mandara.")],
    T=[
        ("{F} ¿Qué dos ciudades de Mesopotamia nombra la ficha?", "Ur y Uruk", "La ficha las nombra."),
        ("{F} ¿Quién unió varias ciudades de Mesopotamia hacia 2300 a. C.?", "Sargón de Acad", "La ficha lo indica."),
        ("{F} ¿Cuántas épocas de unidad menciona la ficha para Egipto?", "3", "Son el Reino Antiguo, el Medio y el Nuevo."),
        ("{F} ¿Con qué región, al sur de Egipto, tenía contacto?", "Nubia", "La ficha lo indica."),
        ("=", "{F} Sargón unió ciudades hacia 2300 a. C. y Egipto se unificó hacia 3100 a. C. ¿Cuántos años después de Egipto ocurrió lo de Sargón?", "3100-2300", "Se restan los años a. C.", " años"),
        ("{F} ¿Dónde se encontraron sellos del Indo?", "En Mesopotamia", "La ficha lo dice."),
        ("{F} Clasifica cada hecho como diferencia interna (D) o contacto (C): 1) Ur y Uruk tenían reyes propios; 2) Egipto comerciaba con Nubia; 3) Egipto tuvo épocas de unidad y de división; 4) sellos del Indo aparecen en Mesopotamia.", "1 D, 2 C, 3 D, 4 C", "Los hechos 1 y 3 son variaciones internas; 2 y 4 son relaciones entre sociedades."),
        ("{F} ¿Qué dice la ficha sobre un posible contacto entre Caral y las civilizaciones de otros continentes?", "No hay evidencia de contacto", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años antes comenzó la civilización olmeca que la chavín, según la ficha?", "1200-900", "Se restan los años a. C. de la ficha.", " años"),
        ("{F} Pedro dice: «Egipto fue siempre un reino unido». Corrígelo con la ficha.", "Hubo épocas de unidad y épocas de división", "La ficha nombra tres reinos con épocas de división entre ellos."),
        ("{F} ¿Por qué no se debe usar a Egipto como la medida para evaluar las demás civilizaciones?", "Porque cada civilización tuvo su ambiente, organización y desarrollo propios, y compararlas no es medir quién fue mejor", "Comparar es entender cada caso en su contexto."),
        ("{F} Un compañero dice: «Como no hay contacto, Caral fue menos importante». ¿Qué le respondes?", "El desarrollo independiente de Caral muestra que ciudades complejas surgieron por su cuenta; no se mide la importancia por el contacto", "Surgió sin influencia de las otras."),
        ("{F} ¿Qué puede circular, además de objetos, cuando dos civilizaciones comercian?", "Ideas y técnicas", "Los contactos permiten que se difundan conocimientos."),
    ],
    ctx=("Un libro dice «Mesopotamia era una sola nación con un solo rey». Con la ficha, corrige esa idea con un dato. {F}", "Ur y Uruk tenían reyes propios, y solo hacia 2300 a. C. Sargón unió varias ciudades", "Las ciudades eran políticamente independientes antes de Sargón."),
    sc=[("¿Contacto significa dominio?", "No: dos sociedades pueden comerciar sin que una gobierne a la otra", "Contacto es relación; dominio es control."),
        ("¿Qué es una diferencia interna? Da un ejemplo de la clase.", "Una variación dentro de una civilización, como las ciudades de Mesopotamia con reyes propios", "Muestra que no eran bloques uniformes."),
        ("=", "{F} ¿Cuántos años separan 3100 a. C. y 2600 a. C.?", "3100-2600", "Se restan los años a. C.", " años")],
    op=("Escribe un párrafo de 6 líneas que compare dos civilizaciones de las cuatro estudiadas: una diferencia interna de cada una, un contacto que conozcamos y una frase sobre qué no se sabe. {F}",
        "Mesopotamia: ciudades con reyes propios; Egipto: épocas de unidad y de división; contacto: sellos del Indo en Mesopotamia; no sabemos cómo llegaron.",
        ["nombra una diferencia interna de cada civilización", "incluye un contacto con evidencia", "reconoce un límite"], ["párrafo escrito"], ["tratar a las civilizaciones como bloques", "convertir un contacto en dominio"],
        "Pide que explique por qué Caral no encaja en ninguna ruta de contacto de la ficha."),
    reinforce="Nombra tres diferencias internas y dos contactos de la ficha.",
    extend="Escribe una pregunta sobre cómo habrá sido viajar con comercio entre Mesopotamia y el Indo.",
)
