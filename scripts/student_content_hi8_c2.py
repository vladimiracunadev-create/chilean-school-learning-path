"""Cuaderno del estudiante, 8.º básico Historia, Geografía y Ciencias Sociales: OA 20 (regiones: criterios físicos y humanos)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 20"
MAT = "Lápiz y papel. Las fichas, tablas y mapas descritos (de ejemplo) están escritos en cada ejercicio; no necesitas atlas ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = ("Fichas de ejemplo. Ficha 1, Región de Antofagasta: desierto con lluvias casi nulas, cordillera al este, minería del cobre. "
      "Ficha 2, Valle Central: clima templado con lluvias en invierno, suelos fértiles, agricultura y gran parte de la población del país. "
      "Ficha 3, Región de Magallanes: clima frío y ventoso, pastizales, crianza de ovejas.")
build(
    OA, 1, F1,
    use="Aprenderé qué es una región y cuáles son los criterios físicos y humanos que la definen. Sirve para entender por qué un mapa de regiones puede dibujarse de varias maneras.",
    prior=["Sé leer un mapa con leyenda y escala.", "Sé distinguir un rasgo natural de uno creado por las personas.", "Sé que Chile tiene zonas muy distintas entre sí."],
    explain=[
        "Una región es un espacio de la superficie terrestre que se distingue de otros por rasgos comunes. Para decidir qué espacios forman una misma región se usan criterios, que son los aspectos con que se compara y se agrupa. Dibujar una región es una decisión que depende del criterio elegido; por eso se habla de regionalización, el proceso de dividir un territorio en regiones.",
        "Los criterios físicos se relacionan con la naturaleza: el clima, el relieve, la vegetación, el suelo y los ríos. Los criterios humanos se relacionan con las personas: la lengua común, la religión, la historia compartida, las costumbres, la población y la economía, es decir, cómo trabajan y producen. Una misma región puede combinar criterios de ambos tipos.",
        "Según el criterio se obtienen distintos tipos de regiones. Una región geográfica se define por rasgos físicos, como un desierto. Una región cultural, por lengua, costumbres o historia. Una región económica, por la actividad productiva. Una región político-administrativa, por un límite fijado por la ley, como las regiones de Chile. Por eso una región no es solo una división administrativa, ni tiene límites naturales únicos.",
    ],
    vocab=[("región", "espacio que se distingue de otros por rasgos comunes"), ("criterio", "aspecto con que se agrupan o separan espacios"), ("regionalización", "proceso de dividir un territorio en regiones"), ("factor físico", "rasgo de la naturaleza, como clima o relieve"), ("factor humano", "rasgo de las personas, como lengua, historia o economía")],
    worked=[
        ("Separar factores", "Una región de ejemplo tiene clima templado, río con riego, lengua común y una fiesta compartida. ¿Cuáles son factores físicos y cuáles humanos?",
         ["Clima y río son de la naturaleza: físicos.", "Lengua común y fiesta compartida son de las personas: humanos."], "Físicos: clima y río; humanos: lengua común y fiesta"),
        ("Elegir un tipo de región", "Un grupo agrupa las zonas donde se cultiva uva para vino. ¿Qué criterio y qué tipo de región usa?",
         ["Agrupa por actividad productiva.", "Es una región económica."], "Criterio de producción; región económica"),
    ],
    mistakes=[
        ("Creer que una región es solo una división que traza el gobierno.", "Hay regiones geográficas, culturales y económicas que no dependen de una ley.", "Pregunta qué criterio se usó para definirla."),
        ("Pensar que las regiones tienen un límite natural único e indiscutible.", "Cada criterio produce límites distintos y suelen ser zonas de transición.", "Recuerda que el límite depende del criterio escogido."),
    ],
    T=[
        ("En Geografía: ¿qué es una región?", "Un espacio que se distingue de otros por rasgos comunes", "Esa es la definición central."),
        ("En Geografía: ¿qué es un criterio de regionalización?", "El aspecto que se usa para agrupar o separar espacios", "Con él se decide el límite de la región."),
        ("{F} ¿Qué rasgo físico se menciona en la ficha 1?", "El desierto con lluvias casi nulas", "El clima y el relieve son factores físicos."),
        ("{F} ¿Cuál es un factor humano en la ficha 1? A) la cordillera al este, B) la minería del cobre, C) las lluvias casi nulas.", "B", "La minería es una actividad económica de las personas."),
        ("{F} ¿Qué dos rasgos de la ficha 3 sirven como criterios para definir Magallanes como región?", "El clima frío y ventoso y la crianza de ovejas", "Uno es físico y el otro, humano."),
        ("Un compañero dice: «Una región es lo mismo que una división administrativa». Corrígelo con una frase.", "Hay regiones geográficas, culturales y económicas, que no dependen de un límite fijado por ley", "Un criterio puede ser natural o humano."),
        ("=", "Un mapa de ejemplo usa la escala 1 cm = 50 km. Una región mide 12 cm de largo en el mapa. ¿Cuántos kilómetros mide de largo en la realidad?", "12*50", "Se multiplican los centímetros del mapa por los km de cada uno."),
        ("=", "Un país de ejemplo está dividido en 16 regiones. Cuatro son del norte y cinco, del sur. ¿Cuántas regiones quedan en las otras zonas?", "16-4-5", "Se restan las regiones ya contadas."),
        ("Rasgos de una zona de ejemplo: suelo arenoso, lengua común, clima árido, fiestas religiosas compartidas. ¿Cuántos son factores humanos?", "2", "La lengua común y las fiestas religiosas son humanos."),
        ("Una zona de ejemplo del sur vive de criar ovejas en pastizales fríos. ¿Con cuál ficha se parece más por su actividad económica?", "Con la ficha 3, Magallanes", "Comparten la crianza de ovejas."),
        ("Explica con una frase por qué una región no tiene un límite natural único e indiscutible.", "Porque cada criterio produce límites distintos y el límite depende del criterio escogido", "Clima, lengua y economía no coinciden en el mapa."),
        ("Evalúa la frase «Una región es solo lo que dibuja el gobierno en un mapa». A) Es falsa: también hay regiones por rasgos físicos, culturales o económicos; B) Es verdadera siempre; C) Es falsa porque las regiones no existen.", "A", "Hay más de un tipo de región."),
        ("Para definir una «región de pescadores» de ejemplo, escribe un criterio físico y uno humano.", "Físico: el mar o el clima de la costa; humano: la pesca como trabajo principal", "Se combinan naturaleza y actividad."),
    ],
    ctx=("Tu curso prepara un mapa mural. Una compañera quiere dibujar «la zona del desierto» y otra, «las 16 regiones con gobierno regional». ¿Qué tipo de región es cada una?", "La primera es una región geográfica; la segunda, político-administrativa", "Una usa un rasgo físico y la otra un límite fijado por ley."),
    sc=[("En Geografía: ¿qué es la regionalización?", "El proceso de dividir un territorio en regiones", "Se hace según un criterio."),
        ("Nombra un factor físico y uno humano.", "Por ejemplo: clima y lengua común", "Uno es natural y el otro, de las personas."),
        ("¿Qué tipo de región se define por la actividad productiva?", "Región económica", "El criterio es la economía.")],
    op=("{F} Elige dos fichas y compáralas. Anota, para cada una: un factor físico, un factor humano y el tipo de región que la describe mejor. Cierra con una frase que explique por qué eligiste ese tipo.",
        "Ficha 1: físico, desierto; humano, minería del cobre; región geográfica y económica. Ficha 3: físico, clima frío y ventoso; humano, crianza de ovejas; región geográfica. Elegí esos tipos porque los rasgos más fuertes son el clima y la actividad.",
        ["identifica un factor físico y uno humano por ficha", "nombra un tipo de región", "justifica su elección"], ["dos fichas con tres datos cada una"], ["confundir factor físico con humano", "no justificar"], "Muéstrale tu clasificación a una persona de tu casa y pregúntale si algún rasgo podría ir en la otra columna."),
    reinforce="Anota dos factores físicos y dos humanos del lugar donde vives.",
    extend="Escribe un ejemplo de región que no coincida con ningún límite administrativo.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = ("Tabla de ejemplo, lluvia anual y vegetación de seis localidades. L1: 5 mm, sin vegetación. L2: 80 mm, arbustos bajos. L3: 350 mm, matorral. L4: 900 mm, bosque. L5: 1.300 mm, bosque. L6: 40 mm, sin vegetación. "
      "Regla de ejemplo: una localidad es árida si recibe menos de 100 mm de lluvia al año.")
build(
    OA, 2, F2,
    use="Aprenderé a leer distintas fuentes (mapas, tablas y textos) para identificar los criterios que forman una región. Sirve para delimitar una región con datos y no por intuición.",
    prior=["Sé qué es una región y qué es un criterio.", "Sé leer una tabla y comparar números.", "Sé distinguir factores físicos y humanos."],
    explain=[
        "Para definir una región uso fuentes. Un mapa físico muestra relieve, ríos y altura. Un mapa político muestra límites de países y de divisiones administrativas. Una tabla estadística entrega datos como lluvia, población o producción. Un texto o un testimonio informa sobre lengua, costumbres o historia. Cada fuente sirve para un criterio distinto.",
        "Al leer un mapa reviso el título, la leyenda, que explica los símbolos, la escala y la fecha. En una tabla busco la unidad de medida, como milímetros de lluvia. Un indicador es un dato que resume un aspecto, como los mm de lluvia al año. Para decidir qué espacios agrupo, puedo fijar una regla, por ejemplo «es árida si llueve menos de 100 mm».",
        "Una sola fuente casi nunca basta. Un mapa de relieve no dice qué lengua se habla, y una tabla de producción no muestra los límites políticos. Por eso combino fuentes: así evito delimitar una región con un criterio incompleto. También reviso la fecha de cada fuente, porque los datos y los límites cambian.",
    ],
    vocab=[("leyenda", "recuadro que explica los símbolos de un mapa"), ("escala", "relación entre una distancia del mapa y la real"), ("indicador", "dato que resume un aspecto, como los mm de lluvia"), ("mapa físico", "mapa que muestra relieve, ríos y otros rasgos naturales"), ("mapa político", "mapa que muestra límites de países y divisiones administrativas")],
    worked=[
        ("Elegir la fuente", "Quieres saber en qué zonas del país hay cordillera y en cuáles llanura. ¿Qué mapa usas?",
         ["Busco un mapa que muestre rasgos naturales de altura.", "El mapa físico lo hace; el político no."], "El mapa físico"),
        ("Aplicar una regla", "Regla de ejemplo: son semiáridas las localidades que reciben entre 100 y 400 mm al año. Una localidad recibe 220 mm. ¿Cuál es su clasificación?",
         ["Comparo 220 con el rango de 100 a 400.", "Está dentro del rango."], "Es semiárida"),
    ],
    mistakes=[
        ("Usar una sola fuente para definir una región por completo.", "Cada fuente muestra un solo criterio.", "Combina al menos una fuente física y una humana."),
        ("Leer un mapa sin mirar la leyenda ni la fecha.", "Los símbolos y los límites cambian de un mapa a otro.", "Revisa título, leyenda, escala y fecha antes de sacar conclusiones."),
    ],
    T=[
        ("En Geografía: ¿para qué sirve la leyenda de un mapa?", "Para explicar los símbolos que usa", "Sin leyenda no se interpretan los colores."),
        ("¿Qué muestra un mapa político?", "Los límites de países y de divisiones administrativas", "No muestra el relieve."),
        ("{F} ¿Qué localidad recibe más lluvia al año?", "L5, con 1.300 mm", "Es la cifra más alta de la tabla."),
        ("{F} Según la regla de la tabla, ¿cuántas localidades son áridas?", "3 (L1, L2 y L6)", "Las tres reciben menos de 100 mm."),
        ("{F} ¿Qué localidad tiene matorral? A) L1, B) L3, C) L5.", "B", "La tabla asocia matorral con 350 mm."),
        ("{F} Una localidad nueva, L7, recibe 60 mm y tiene arbustos. Según la regla, ¿es árida?", "Sí, porque 60 mm es menos de 100 mm", "Cumple la condición de la regla."),
        ("=", "{F} Una región de ejemplo reúne a L4 y L5. ¿Cuál es el promedio de su lluvia anual en mm?", "(900+1300)/2", "Se suman los dos valores y se divide por dos."),
        ("=", "{F} ¿Cuántos mm más llueve en L5 que en L3?", "1300-350", "Se resta la cifra menor a la mayor."),
        ("{F} ¿Qué localidades formarían una «región de bosque» según la tabla?", "L4 y L5", "Son las únicas con bosque."),
        ("Un grupo quiere definir una región cultural. ¿Qué fuente le sirve más? A) una tabla de lluvias anuales, B) testimonios y registros de lengua y fiestas, C) un mapa de relieve.", "B", "La lengua y las fiestas son criterios humanos."),
        ("Un mapa de 1900 y uno actual muestran límites distintos. ¿Qué debes revisar antes de compararlos?", "La fecha y el criterio de cada mapa", "Los límites cambian con el tiempo y con el criterio."),
        ("{F} Explica con una frase por qué solo con esta tabla no puedes definir una región humana.", "Porque solo trae lluvia y vegetación, que son datos físicos, y faltan datos de población, lengua o economía", "La tabla cubre un solo tipo de criterio."),
        ("{F} ¿Qué relación muestran la lluvia y la vegetación en la tabla?", "A más lluvia, más vegetación", "Las localidades con más mm tienen bosque."),
    ],
    ctx=("Un grupo de tu curso entrega una región dibujada solo con un mapa de relieve, y dice que «con eso sabemos dónde viven personas con la misma lengua». ¿Qué fuente falta?", "Una fuente humana, como un texto o una tabla sobre lengua y población", "El relieve no informa sobre lengua."),
    sc=[("En Geografía: ¿qué es un indicador?", "Un dato que resume un aspecto, como los mm de lluvia al año", "Sirve para comparar lugares."),
        ("¿Qué debes revisar en un mapa antes de interpretarlo?", "Título, leyenda, escala y fecha", "Permiten leerlo bien."),
        ("¿Por qué combinar fuentes para definir una región?", "Porque cada fuente muestra un solo criterio", "Así el criterio no queda incompleto.")],
    op=("{F} Con la tabla, define una «región árida» de ejemplo: lista las localidades que incluyes, escribe la regla que usaste y menciona dos fuentes humanas que necesitarías para convertirla en una región cultural.",
        "Incluyo L1, L2 y L6. Regla: menos de 100 mm de lluvia al año. Para convertirla en región cultural necesitaría testimonios sobre lengua y fiestas y datos de población.",
        ["lista las localidades", "enuncia la regla", "propone fuentes humanas"], ["tres elementos claros"], ["no decir qué regla usó", "proponer fuentes físicas como si fueran humanas"], "Pide a una persona de tu casa que compruebe la regla con las cifras de la tabla."),
    reinforce="Elige un mapa que tengas en casa y anota su título, su leyenda y su escala.",
    extend="Escribe una regla de ejemplo para separar una localidad de bosque de una de matorral usando los mm de lluvia.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = ("Línea de tiempo de ejemplo. 1975: el país se organiza en 13 regiones administrativas. 2007: se crean las regiones de Los Ríos y de Arica y Parinacota, y el país pasa a tener 15 regiones. 2018: se crea la región de Ñuble y el país pasa a tener 16 regiones. "
      "Ficha de ejemplo sobre una región económica del norte: a fines del siglo XIX y comienzos del XX destacó el salitre; hoy destaca la minería del cobre.")
build(
    OA, 3, F3,
    use="Aprenderé a ver cómo cambian las regiones en el tiempo y qué rasgos se mantienen. Sirve para entender que un mapa de regiones muestra una época y no es definitivo.",
    prior=["Sé que una región se define con criterios.", "Sé leer una línea de tiempo.", "Sé distinguir cambio y continuidad."],
    explain=[
        "Las regiones no son fijas. Una región político-administrativa cambia cuando la ley modifica sus límites o crea regiones nuevas. En Chile, el país se organizó en regiones en la década de 1970, y después se crearon otras: Arica y Parinacota y Los Ríos en 2007, y Ñuble en 2018. Cada cambio busca, por lo general, acercar la administración a las personas de ese territorio.",
        "Las regiones económicas también cambian. Cuando cambia la actividad productiva, cambia lo que identifica a una región. En el norte, el salitre fue muy importante a fines del siglo XIX y comienzos del XX; hoy lo es la minería del cobre. Un cambio económico puede modificar el empleo, la población y la forma en que se usa el territorio.",
        "Pero algo se mantiene. Los rasgos físicos, como un desierto o una cordillera, cambian muy lentamente. Por eso, al estudiar una región en el tiempo, pregunto qué cambió, como límites y actividades, y qué continuó, como el clima o la actividad extractiva. Así evito creer que el mapa de hoy existió siempre.",
    ],
    vocab=[("región administrativa", "división del país fijada por ley para gobernar y organizar el territorio"), ("cambio", "algo que se modifica con el tiempo"), ("continuidad", "algo que se mantiene"), ("actividad extractiva", "actividad que obtiene recursos de la naturaleza, como la minería"), ("transición", "paso gradual de una situación a otra")],
    worked=[
        ("Leer la línea de tiempo", "{F} Con la línea de ejemplo, ¿cuántas regiones se agregaron entre 1975 y 2018?",
         ["Veo que en 1975 había 13.", "En 2018 hay 16.", "Resto: 16 - 13."], "Se agregaron 3 regiones"),
        ("Cambio y continuidad", "{F} En la región económica del norte, ¿qué cambió y qué continuó entre el siglo XIX y hoy?",
         ["Cambió el recurso principal: del salitre al cobre.", "Continuó una economía basada en la minería."], "Cambió el recurso; continuó la minería"),
    ],
    mistakes=[
        ("Creer que el mapa de regiones de hoy existió siempre igual.", "Los límites administrativos se modifican por ley.", "Revisa en qué fecha se hizo cada mapa."),
        ("Decir que si cambia la economía, la región entera deja de existir.", "Cambian algunos rasgos, pero otros, como el clima, se mantienen.", "Separa lo que cambió de lo que continuó."),
    ],
    T=[
        ("En Geografía: ¿qué es una región administrativa?", "Una división del país fijada por ley para organizar y gobernar el territorio", "Se define por una norma."),
        ("{F} ¿Cuántas regiones había en 1975?", "13", "Lo indica la línea de tiempo."),
        ("{F} ¿Qué regiones se crearon en 2007?", "Los Ríos y Arica y Parinacota", "Pasaron de 13 a 15 regiones."),
        ("=", "{F} ¿Cuántas regiones más tuvo el país en 2018 que en 1975?", "16-13", "Se resta el número de 1975 al de 2018."),
        ("=", "{F} ¿Cuántos años pasaron entre la creación de las dos regiones de 2007 y la de Ñuble?", "2018-2007", "Se restan los años."),
        ("{F} ¿Cuál es una continuidad? A) el país sigue organizado en regiones administrativas, B) se pasó de 13 a 16 regiones, C) se creó Ñuble en 2018.", "A", "El tipo de organización se mantiene."),
        ("¿Qué razón explica mejor que se creen regiones nuevas? A) acercar la administración y las decisiones a las personas de ese territorio, B) cambió el clima del país, C) desaparecieron las regiones antiguas.", "A", "Es una de las razones de la regionalización."),
        ("{F} En la ficha económica del norte, ¿qué actividad destacaba a fines del siglo XIX?", "El salitre", "Hoy destaca el cobre."),
        ("Una región de ejemplo tiene 450.000 habitantes y crece en 12.000 personas por año durante 5 años. ¿Cuántos habitantes tiene al final?", "510.000 habitantes", "Se suma el crecimiento de cinco años a la población inicial."),
        ("{F} Un compañero dice: «Una región económica es siempre igual». ¿Qué dato de la ficha lo contradice?", "Que pasó del salitre al cobre", "Cambió el recurso principal."),
        ("Un mapa muestra 13 regiones y otro, 16. ¿Se equivoca alguno?", "No, porque corresponden a épocas distintas", "Los límites cambiaron con el tiempo."),
        ("Explica con una frase por qué los límites administrativos cambian más rápido que los rasgos físicos.", "Porque se modifican por ley, mientras clima y relieve cambian muy lentamente", "Una ley puede dictarse en cualquier momento."),
        ("{F} Escribe qué continuó en la región del norte aunque cambió el recurso principal.", "Siguió siendo una región que vive de la minería", "El tipo de actividad extractiva se mantuvo."),
    ],
    ctx=("Para un trabajo, un estudiante dibuja el mapa de las 16 regiones y escribe: «Así fueron siempre las regiones de Chile». {F} ¿Qué dato de la línea de tiempo usas para corregirlo?", "Que en 1975 eran 13 y luego se crearon otras regiones en 2007 y 2018", "Muestra que el mapa cambió."),
    sc=[("En Geografía: ¿qué es una continuidad?", "Algo que se mantiene a pesar del tiempo", "Se opone al cambio."),
        ("Nombra un cambio de las regiones administrativas de Chile.", "Por ejemplo: se creó la región de Ñuble en 2018", "Aumentó el número de regiones."),
        ("¿Por qué conviene revisar la fecha de un mapa?", "Porque los límites y las actividades cambian", "Un mapa muestra una época.")],
    op=("{F} Redacta un texto breve de cuatro líneas que explique cómo han cambiado las regiones de Chile. Incluye un dato de la línea de tiempo, un cambio económico del norte y una continuidad.",
        "En 1975 había 13 regiones y en 2018 hay 16, porque se crearon otras. En el norte, el salitre fue importante y hoy lo es el cobre. Continúa que la economía depende de la minería y que el país sigue organizado en regiones.",
        ["usa un dato de la línea", "nombra un cambio económico", "nombra una continuidad"], ["texto de cuatro líneas"], ["no incluir fechas", "confundir cambio con continuidad"], "Lee tu texto a una persona de tu casa y pídele que subraye la continuidad."),
    reinforce="Pregunta a una persona mayor cómo cambió la actividad principal de tu comuna y anótalo.",
    extend="Explica qué cambia en una comuna si se crea una región nueva.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = ("Fichas de ejemplo. Amazonía: gran selva tropical atravesada por ríos, repartida entre varios países. "
      "Patagonia: territorio de estepa, lagos y montañas, compartido entre Chile y Argentina. "
      "América Latina: conjunto de países donde predominan el español y el portugués, con una historia colonial compartida. "
      "Alianza del Pacífico: grupo de cuatro países (Chile, Colombia, México y Perú) que acordaron comerciar entre sí. "
      "Estados de Brasil: divisiones político-administrativas con gobierno propio.")
build(
    OA, 4, F4,
    use="Aprenderé a distinguir tipos de regiones de Chile y de América y a ver por qué el mismo territorio puede ser dividido de formas distintas. Sirve para comparar mapas y puntos de vista.",
    prior=["Sé qué es una región y sus criterios físicos y humanos.", "Sé que los límites cambian con el tiempo.", "Sé qué es un país y un continente."],
    explain=[
        "Los tipos de región más comunes son cuatro. La región geográfica se define por rasgos físicos, como la Amazonía, una selva con ríos. La región cultural se define por rasgos humanos como lengua, historia y costumbres, como América Latina. La región económica agrupa espacios o países que se organizan para producir o comerciar, como la Alianza del Pacífico. La región político-administrativa tiene límites fijados por ley, como las regiones de Chile o los estados de Brasil.",
        "Estas regiones pueden cruzar fronteras. La Amazonía y la Patagonia se extienden por más de un país, porque se definen por la naturaleza y no por límites políticos. En cambio, una región político-administrativa respeta las fronteras de un país. Por eso los mapas de un mismo lugar no coinciden: cada uno usa un criterio distinto.",
        "Distintas personas pueden mirar un mismo territorio con criterios diferentes. Una geógrafa lo divide por clima y relieve; un economista, por la producción; una historiadora, por la historia compartida. Ninguna visión es la única correcta: cada una responde a una pregunta distinta. Comparar esas perspectivas ayuda a entender el territorio mejor.",
    ],
    vocab=[("región geográfica", "región definida por rasgos físicos"), ("región cultural", "región definida por lengua, historia o costumbres"), ("región económica", "región definida por la producción o el comercio"), ("región político-administrativa", "región con límites fijados por ley"), ("frontera", "línea que separa el territorio de dos países")],
    worked=[
        ("Clasificar", "La Alianza del Pacífico agrupa a cuatro países para comerciar. ¿Qué tipo de región es?",
         ["El criterio es el comercio entre los países.", "Es económica."], "Región económica"),
        ("Cruzar fronteras", "¿Por qué la Patagonia puede estar en dos países?",
         ["Se define por estepa, lagos y montañas.", "Esos rasgos físicos no respetan los límites políticos."], "Porque se define por rasgos físicos y no por límites políticos"),
    ],
    mistakes=[
        ("Creer que toda región está dentro de un solo país.", "Las regiones geográficas y culturales pueden cruzar fronteras.", "Pregunta qué criterio la define."),
        ("Decir que un mapa es el verdadero y los demás están equivocados.", "Cada mapa usa un criterio distinto.", "Pregunta qué criterio usa cada mapa."),
    ],
    T=[
        ("{F} ¿Qué tipo de región es la Amazonía?", "Región geográfica", "Se define por rasgos físicos."),
        ("{F} ¿Qué tipo de región son los estados de Brasil?", "Región político-administrativa", "Tienen límites fijados por ley."),
        ("En Geografía: ¿qué es una región cultural?", "Una región definida por lengua, historia o costumbres compartidas", "Su criterio es humano."),
        ("{F} ¿Qué criterio sirve para considerar a América Latina una región cultural? A) la lengua y la historia compartidas, B) solo el clima, C) la altura de sus montañas.", "A", "Son criterios humanos."),
        ("{F} ¿Por qué la Patagonia es una región que no coincide con las fronteras de un solo país?", "Porque la definen rasgos físicos compartidos por Chile y Argentina", "La naturaleza no sigue límites políticos."),
        ("{F} ¿Qué países forman la Alianza del Pacífico según la ficha?", "Chile, Colombia, México y Perú", "La ficha los nombra."),
        ("=", "En un bloque económico de ejemplo hay 4 países con poblaciones de ejemplo de 19, 52, 128 y 34 millones. ¿Cuántos millones suman?", "19+52+128+34", "Se suman las cuatro poblaciones."),
        ("=", "La Patagonia de ejemplo mide 1.200 km de largo; 700 km están en Chile. ¿Cuántos km están en el otro país?", "1200-700", "Se resta lo chileno del total."),
        ("{F} Una geógrafa y un economista estudian la Patagonia. ¿Qué criterio usa probablemente cada uno?", "La geógrafa, relieve y clima; el economista, producción y comercio", "Cada experto responde a una pregunta distinta."),
        ("{F} Un compañero dice que la Amazonía pertenece solo a un país. Corrígelo con la ficha.", "La ficha dice que está repartida entre varios países", "Es una región geográfica que cruza fronteras."),
        ("Explica por qué el mapa de regiones climáticas de Chile no coincide con el mapa de las regiones administrativas.", "Porque el clima depende de rasgos físicos y no sigue los límites fijados por ley", "Cada mapa usa un criterio distinto."),
        ("Un territorio puede pertenecer a varios tipos de región a la vez. ¿Cuál ejemplo lo muestra? A) una región administrativa que además es parte de un desierto, B) un desierto que además es un país, C) un mapa sin criterio.", "A", "El mismo espacio se define con criterios distintos."),
        ("Evalúa la frase «El mapa verdadero de regiones es el más antiguo». ¿Por qué falla?", "Porque la validez depende del criterio y la fecha, no de la antigüedad", "No hay un único mapa correcto."),
    ],
    ctx=("En una feria escolar, un grupo muestra un mapa de la Patagonia que termina en la frontera con Argentina. Otro muestra el mismo territorio completo. ¿Qué criterio explica que el segundo mapa cruce la frontera?", "Que usa un criterio geográfico y no el límite político", "La naturaleza no respeta las fronteras."),
    sc=[("En Geografía: ¿qué es una región económica?", "Una región definida por la producción o el comercio", "El criterio es económico."),
        ("{F} Da un ejemplo de región político-administrativa de la ficha.", "Los estados de Brasil", "Tienen límites fijados por ley."),
        ("¿Por qué dos mapas de un mismo lugar pueden ser distintos?", "Porque usan criterios diferentes", "Cada uno responde a una pregunta distinta.")],
    op=("{F} Elige dos fichas y construye una comparación: el tipo de región de cada una, el criterio que la define, si cruza o no fronteras y una pregunta que cada una ayuda a responder. Termina con una frase que explique por qué ninguno de los dos mapas es «el correcto».",
        "Comparo la Amazonía y los estados de Brasil. La Amazonía es geográfica, se define por selva y ríos, y cruza fronteras. Los estados de Brasil son político-administrativos, se definen por ley y no cruzan fronteras. Ninguno es el correcto porque responden a preguntas distintas.",
        ["clasifica dos fichas", "indica criterio y fronteras", "explica por qué ningún mapa es el único correcto"], ["dos fichas comparadas con una conclusión"], ["confundir tipos de región", "decir que un tipo es mejor que otro"], "Explícale a una persona de tu casa qué significa que una región cruce una frontera."),
    reinforce="Anota dos regiones de América que conozcas y escribe su tipo.",
    extend="Explica una situación en la que un mapa económico sea más útil que uno físico.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = ("Caso de ejemplo, el Valle de Lirán (inventado). Clima templado con lluvias en invierno; suelos fértiles; sus habitantes hablan español y celebran la misma fiesta patronal; la economía se basa en la fruta y el vino; hasta 1990 pertenecía a dos provincias distintas y hoy forma un solo municipio.")
build(
    OA, 5, F5,
    use="Aprenderé a argumentar con evidencia si un territorio puede considerarse una región y de qué tipo. Sirve para defender una decisión de delimitación con datos y no con opiniones.",
    prior=["Sé qué tipos de región existen.", "Sé leer fuentes para encontrar criterios.", "Sé construir un argumento con afirmación, evidencia y explicación."],
    explain=[
        "Argumentar sobre una región es responder: ¿qué rasgos comunes tiene este espacio y por qué lo distinguen de otros? Mi afirmación indica el tipo de región. La evidencia son datos concretos de fuentes, como el clima, la lengua o la producción. La explicación conecta esos datos con el criterio que uso.",
        "Un buen argumento elige criterios pertinentes. Si quiero demostrar que un valle es una región económica, debo usar datos de producción y no el color del paisaje. Si quiero mostrar que es cultural, uso lengua, fiestas e historia. Puedo combinar criterios físicos y humanos cuando se refuerzan entre sí.",
        "También considero las objeciones: razones que van en contra. Por ejemplo, que el valle estuvo dividido en dos provincias. La respuesta es que una división administrativa antigua no impide que haya rasgos comunes. Y reconozco los límites de mi evidencia: no sé si todas las personas del valle comparten una misma identidad. Así mi argumento es honesto y más fuerte.",
    ],
    vocab=[("pertinente", "que tiene relación directa con lo que se quiere probar"), ("objeción", "razón que va en contra de una afirmación"), ("identidad", "sentimiento de pertenecer a un grupo o lugar"), ("delimitar", "trazar los límites de una región"), ("evidencia", "dato de una fuente que apoya o contradice una idea")],
    worked=[
        ("Elegir evidencia pertinente", "{F} Quieres sostener que el valle es una región cultural. ¿Qué dato del caso sirve?",
         ["Busco datos de lengua, fiestas o historia.", "El caso dice que hablan español y celebran la misma fiesta."], "La lengua común y la fiesta compartida"),
        ("Responder una objeción", "Alguien dice: «El valle estuvo en dos provincias, así que no es una región». ¿Qué respondes?",
         ["Una división administrativa antigua no borra los rasgos comunes.", "El clima, la economía y la cultura son compartidos."], "Que los rasgos comunes se mantienen aunque haya habido dos provincias"),
    ],
    mistakes=[
        ("Dar una opinión sin dato, como «es una región porque es bonita».", "La belleza no es un criterio de regionalización.", "Usa criterios físicos o humanos con evidencia."),
        ("Usar un dato que no tiene que ver con el tipo de región que se afirma.", "El argumento pierde fuerza si la evidencia no es pertinente.", "Relaciona cada dato con el criterio que defiendes."),
    ],
    T=[
        ("{F} ¿Qué datos del caso apoyan que Lirán es una región geográfica?", "El clima templado con lluvias en invierno y los suelos fértiles", "Son rasgos físicos."),
        ("{F} ¿Qué datos del caso apoyan que Lirán es una región cultural?", "La lengua común y la misma fiesta patronal", "Son rasgos humanos de costumbres."),
        ("{F} ¿Qué dato del caso apoya que Lirán es una región económica?", "Su economía basada en la fruta y el vino", "Es su actividad productiva."),
        ("{F} ¿Cuál afirmación está mejor sostenida? A) Lirán es una región porque es bonita, B) Lirán puede considerarse una región económica porque su producción de fruta y vino la distingue, C) Lirán es región porque lo dice un vecino.", "B", "Tiene afirmación y evidencia pertinente."),
        ("=", "{F} Lirán produce 4.000 cajas de fruta por mes. ¿Cuántas cajas produce en 12 meses?", "4000*12", "Se multiplica la producción mensual por los meses."),
        ("=", "{F} De 5.000 habitantes de Lirán, 3.200 trabajan en la fruticultura. ¿Cuántos trabajan en otra actividad?", "5000-3200", "Se resta lo que trabaja en fruticultura al total."),
        ("{F} Un vecino objeta: «Lirán estaba dividida en dos provincias, no es una región». ¿Cómo respondes?", "Una división administrativa antigua no impide que haya rasgos comunes de clima, economía y cultura", "Los rasgos comunes se mantienen."),
        ("{F} En Lirán, ¿qué cambió y qué continuó? Responde con una frase.", "Cambió su situación administrativa (de dos provincias a un municipio); continuaron su clima y su cultura", "La administración cambió; los rasgos se mantuvieron."),
        ("¿Qué dato NO sirve como criterio de región? A) clima, B) lengua común, C) el color de las casas de un solo vecino.", "C", "No es un rasgo del conjunto del territorio."),
        ("{F} Si solo usas el criterio económico, ¿qué rasgos del caso quedarían fuera?", "Los rasgos físicos y culturales, como el clima y la fiesta patronal", "Un solo criterio muestra una parte."),
        ("Completa el argumento: «Lirán es una región geográfica y económica porque tiene ___ (dato físico) y vive de ___ (dato económico)».", "Clima templado con lluvias en invierno y suelos fértiles; la fruta y el vino", "Une un dato físico y uno económico."),
        ("Evalúa cuál argumento es más sólido. A) «Lirán es una región porque todos lo creen», B) «Lirán es una región porque tiene clima, suelo, lengua y producción comunes», C) «Lirán no es una región porque no tiene frontera propia».", "B", "Usa varios criterios con datos del caso."),
        ("{F} Un habitante dice que en un sector del valle se habla otra lengua además del español. ¿Cómo matizas tu afirmación sobre la región cultural?", "Reconozco que la lengua común no es total y que el carácter cultural es más complejo", "Un matiz honesto fortalece el argumento."),
    ],
    ctx=("En el consejo de curso debaten si el barrio donde está su colegio es una región. Una compañera propone mirar dos criterios: uno físico (el río que lo cruza) y uno humano (la feria que se celebra cada año). ¿Qué tipo de argumento propone?", "Un argumento que combina un criterio físico y uno humano", "Cruza naturaleza y cultura."),
    sc=[("En Geografía: ¿qué es una objeción?", "Una razón que va en contra de una afirmación", "Se responde con evidencia."),
        ("¿Qué significa que un dato sea pertinente?", "Que tiene relación directa con lo que se quiere probar", "Apoya el criterio elegido."),
        ("Nombra un criterio humano.", "Por ejemplo: lengua común", "Es un rasgo de las personas.")],
    op=("{F} Escribe un argumento de cuatro partes sobre el Valle de Lirán: tu afirmación (tipo de región), dos datos como evidencia, una explicación de por qué esos datos son pertinentes y una objeción con tu respuesta.",
        "Lirán es una región económica y geográfica. Evidencias: el clima templado con suelos fértiles y la economía de fruta y vino. Explicación: el clima y el suelo permiten la producción que la distingue. Objeción: estuvo en dos provincias; respuesta: eso es administrativo y no borra los rasgos comunes.",
        ["afirmación clara", "dos evidencias pertinentes", "explicación", "objeción respondida"], ["cuatro partes completas"], ["opinión sin datos", "evidencia no pertinente"], "Pide a una persona de tu casa que ponga otra objeción y responde con un dato."),
    reinforce="Elige un lugar que conozcas y anota dos datos físicos y dos humanos que lo distinguen.",
    extend="Escribe cómo cambiaría tu argumento si Lirán perdiera su producción de fruta.",
    materials=MAT,
)
