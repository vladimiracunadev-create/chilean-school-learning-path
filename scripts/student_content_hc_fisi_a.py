"""Física (electivo HC, 3.º y 4.º medio): OAC-01 (cambio climático global), clases 1 a 6, y OAC-02 (origen y evolución del universo), clases 1 a 4.
Todo en papel: sin laboratorio, sin electricidad de red ni fuentes de calor. Los datos son de ejemplo y están escritos en cada ficha."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel; calculadora simple opcional. No se necesita laboratorio, instrumentos, fuentes de calor ni electricidad de red: "
             "todos los datos son de ejemplo (inventados o redondeados para practicar) y están escritos en la ficha. Las constantes que aparecen "
             "(por ejemplo, la velocidad de la luz de unos 300.000 km/s) son valores aproximados y se rotulan como tales.")
build = make_build(MATERIALS)

O1 = "CN-FISI-3y4-OAC-01"
O2 = "CN-FISI-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (de ejemplo, datos inventados). Ciudad ficticia de Valle Claro. Un lunes de enero llovió y la máxima fue 18 °C. "
     "Temperatura media de enero (°C) en seis años seguidos: 20, 22, 21, 20, 22, 21.")
build(
    O1, 1, F,
    use="Aprenderé a delimitar una pregunta sobre el cambio climático global: qué sistema estudio, qué variable mido y en qué escala de tiempo, para distinguir clima de tiempo atmosférico.",
    prior=["Sé calcular un promedio.", "Sé que la atmósfera y los océanos intercambian calor.", "Sé leer una tabla con unidades."],
    explain=[
        "En Física del clima, el sistema climático es el conjunto de componentes que intercambian energía y materia: la atmósfera (el aire), la hidrosfera (océanos, lagos y ríos), la criosfera (hielo y nieve), la litosfera (la superficie sólida de la Tierra) y la biosfera (los seres vivos). Una pregunta de investigación debe nombrar qué parte del sistema se estudia, qué variable se mide (con su unidad) y en qué lugar y período.",
        "El tiempo atmosférico es el estado de la atmósfera en un momento y lugar, por ejemplo la lluvia de un lunes. El clima es el patrón promedio de esas condiciones durante muchos años; por convención se usan períodos de 30 años. Por eso un día frío no prueba nada sobre el clima. El cambio climático global es un cambio sostenido del clima promedio del planeta durante décadas.",
        "El efecto invernadero natural ocurre porque gases como el vapor de agua, el dióxido de carbono (CO2) y el metano absorben parte de la radiación infrarroja que emite la superficie y la devuelven hacia ella. Gracias a él, la temperatura media de la Tierra es de unos 15 °C y no de unos −18 °C. El problema actual no es que exista, sino que su intensidad aumenta al sumar más gases.",
    ],
    vocab=[("sistema climático", "conjunto de atmósfera, hidrosfera, criosfera, litosfera y biosfera que intercambian energía"), ("tiempo atmosférico", "estado de la atmósfera en un momento y lugar"), ("clima", "patrón promedio del tiempo durante muchos años (convención: 30)"), ("variable", "magnitud que se mide y puede cambiar, con su unidad"), ("efecto invernadero", "retención de parte del calor infrarrojo por gases de la atmósfera"), ("criosfera", "hielo y nieve del planeta")],
    worked=[
        ("Clima o tiempo", "Una noticia dice: «Hoy amaneció con escarcha en la ciudad de Roca Alta». ¿Describe clima o tiempo atmosférico?", ["Identifica el período: se habla de «hoy», un solo momento.", "Un patrón de muchos años sería clima; un estado puntual es tiempo atmosférico."], "Describe tiempo atmosférico, no clima"),
        ("Delimitar una pregunta", "Mejora la pregunta «¿Está cambiando todo en el planeta?» para poder investigarla.", ["Elige un sistema y una variable con unidad: la atmósfera y la temperatura media anual del aire en °C.", "Agrega lugar y período: una estación ficticia, con el registro de 30 años."], "«¿Aumentó la temperatura media anual de la estación Norte entre los primeros y los últimos 10 años de un registro de 30 años?»"),
    ],
    mistakes=[("Decir que una ola de frío demuestra que el clima global no cambia.", "Se confunde un episodio de tiempo atmosférico con un promedio de décadas.", "Pregunta siempre: ¿cuántos años abarca este dato?"),
              ("Confundir efecto invernadero natural con cambio climático.", "El primero existe siempre y mantiene el planeta habitable; el segundo es el cambio sostenido del clima.", "Distingue el fenómeno (natural) de su intensificación (cambio).")],
    T=[
        ("abc", "¿Cuál de estas descripciones corresponde al clima y no al tiempo atmosférico?", "En Valle Claro, la temperatura media de enero de los últimos 30 años es 21 °C", "Hoy en Valle Claro hay neblina en la mañana", "Mañana se espera una lluvia débil por la tarde", "El clima es un promedio de muchos años; la neblina de hoy y la lluvia de mañana son estados puntuales del tiempo."),
        ("abc", "¿A qué componente del sistema climático pertenecen los glaciares y la nieve?", "La criosfera", "La biosfera", "La litosfera", "La criosfera agrupa el hielo y la nieve; la biosfera son los seres vivos y la litosfera el suelo y las rocas."),
        ("ab", "¿Qué papel cumple el efecto invernadero natural?", "Retiene parte del calor infrarrojo de la superficie y mantiene temperaturas habitables", "Produce el calor del Sol dentro de la atmósfera", "Sin él la temperatura media sería muy baja, porque los gases devuelven parte del calor hacia la superficie."),
        ("abc", "¿Cuál de estas es una pregunta investigable sobre el clima?", "¿Disminuyó la precipitación anual de una ciudad entre dos períodos de 30 años?", "¿Es triste que haya sequía?", "¿Todas las personas deberían ahorrar agua?", "Solo la primera tiene una variable medible, un lugar y un período; las otras son valoraciones u opiniones."),
        ("abc", "{F} ¿Por qué una sola jornada lluviosa no basta para decir que el clima de Valle Claro cambió?", "Porque el clima es un patrón de muchos años y un día es tiempo atmosférico", "Porque la lluvia no se relaciona con el clima", "Porque en enero la temperatura nunca varía", "El clima se define con promedios de décadas; un día no muestra un patrón."),
        ("ab", "¿Cuál es la diferencia correcta entre efecto invernadero natural y cambio climático global?", "El primero existe siempre; el segundo es un cambio sostenido del clima promedio durante décadas", "Son dos nombres para el mismo proceso", "El efecto natural es permanente y el cambio es una variación sostenida del promedio en el tiempo."),
        ("=", "{F} Calcula la temperatura media de enero de los seis años.", "(20+22+21+20+22+21)//6", "La media se obtiene sumando los seis valores y dividiendo por el número de años.", " °C"),
        ("En una investigación se pregunta: «¿cambió la lluvia de una ciudad en 30 años?». ¿Qué variable se mide y en qué unidad se suele expresar?", "La precipitación, en milímetros (mm)", "La lluvia acumulada se mide como altura de agua caída, que se expresa en milímetros."),
        ("abc", "Se estudia si aumentó la temperatura media anual del aire de una ciudad. ¿Qué componente del sistema climático se mide directamente?", "La atmósfera", "La criosfera", "La biosfera", "La temperatura del aire es una propiedad de la atmósfera; los otros componentes no se miden con ese dato."),
        ("abc", "Una persona afirma: «Este invierno fue muy frío, así que el calentamiento global no existe». ¿Qué falla en el razonamiento?", "Confunde el tiempo de una estación con el promedio de muchos años", "Los inviernos fríos prueban que el clima no cambia", "El calentamiento global solo se mide en verano", "Una estación fría es una variación dentro de un clima; para evaluar una tendencia se necesitan décadas de datos."),
        ("abc", "Para estudiar el clima conviene usar un registro de 30 años y no uno de 3 porque", "un período largo permite distinguir una tendencia de la variación normal entre años", "un período corto solo sirve para medir lluvia y no temperatura", "un período largo elimina la necesidad de medir con instrumentos", "Con pocos años un episodio excepcional pesa demasiado; con muchos se ve el patrón de fondo."),
        ("abc", "Un grupo estudia el calentamiento de la Tierra e ignora los océanos. ¿Qué problema tendrá su análisis?", "Dejará fuera un componente que almacena y transporta mucho calor, y su explicación quedará incompleta", "Ninguno, porque los océanos no intercambian calor con la atmósfera", "Ninguno, porque el océano solo influye en el color del cielo", "Los océanos intercambian calor con la atmósfera y guardan gran parte del calor extra; omitirlos deja un vacío."),
        ("=", "{F} Se agrega un séptimo año de enero muy cálido, con 28 °C. ¿Cuánto vale ahora la media de los siete años?", "(126+28)//7", "Se suma el valor nuevo a los seis anteriores (que suman 126) y se divide por 7; un año extremo sube la media pero no prueba una tendencia.", " °C"),
    ],
    ctx=("abc", "Un colegio de Valle Claro quiere saber si su ciudad se calienta y tiene el registro de la temperatura media anual de los últimos 30 años. ¿Qué pregunta investigable debería formular?", "¿Cuántos °C cambió la temperatura media anual entre los primeros 10 y los últimos 10 años del registro?", "¿Es justo que cada vez haga más calor?", "¿Qué temperatura habrá el próximo lunes?", "La primera tiene variable, unidad y períodos de comparación; las otras son una opinión y un pronóstico de tiempo atmosférico."),
    sc=[
        ("En Física del clima: ¿qué es el clima?", "El patrón promedio del estado de la atmósfera en un lugar durante muchos años (convención: 30)", "El clima se define por promedios largos, no por el estado de un día."),
        ("¿Cuántos componentes del sistema climático se nombran en esta clase?", "Cinco", "Son atmósfera, hidrosfera, criosfera, litosfera y biosfera."),
        ("¿Una ola de frío de una semana prueba que el clima global no cambia?", "No", "Una semana es tiempo atmosférico y no un promedio de décadas."),
    ],
    op=("Elige un caso. Caso 1: la cuenca ficticia «Río Seco», donde los vecinos dicen que llueve menos. Caso 2: el glaciar ficticio «Glaciar Azul», que según el guía «se hace más chico». Escribe (a) una pregunta investigable, (b) los componentes del sistema climático que participan, (c) la variable con su unidad, (d) el lugar y el período que usarías y (e) un dato que no bastaría como evidencia.",
        "Caso 1: (a) ¿Disminuyó la precipitación anual de Río Seco entre los primeros y los últimos 15 años de un registro de 30? (b) atmósfera, hidrosfera y biosfera. (c) precipitación en mm por año. (d) estación de Río Seco, 30 años. (e) La lluvia de un solo mes, porque es tiempo atmosférico.",
        ["la pregunta tiene variable, unidad, lugar y período", "nombra al menos dos componentes del sistema", "explica por qué un dato puntual no basta"],
        ["hoja con las cinco partes (a) a (e) escritas con ejemplos de este caso"],
        ["preguntas con opiniones («¿es injusto?»)", "olvidar la unidad", "usar un solo día como evidencia"],
        "Pregunta: «¿cuántos años abarca tu dato y qué mide exactamente?». Si no puede responder, pídele que reescriba la pregunta con período y unidad."),
    reinforce="Escribe tres frases: dos que describan tiempo atmosférico y una que describa clima, y marca cuál es cuál.",
    extend="Explica con tus palabras por qué la intensidad del efecto invernadero puede cambiar aunque el efecto exista de forma natural.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (de ejemplo, datos inventados). Estación «Cumbre»: promedio de referencia de 30 años = 10 °C. Temperatura media anual en cinco años seguidos (°C): "
     "año 1 = 10, año 2 = 11, año 3 = 12, año 4 = 11, año 5 = 11. Fuente X: publicación anónima sin datos ni método. Fuente Y: informe de un instituto que explica su método y entrega los datos.")
build(
    O1, 2, F,
    use="Aprenderé a distinguir registros directos e indirectos del clima, a evaluar la calidad de una fuente y a calcular anomalías, separando correlación de causalidad.",
    prior=["Sé que el clima se estudia con promedios de años.", "Sé calcular diferencias y promedios.", "Sé leer tablas de datos."],
    explain=[
        "Los registros instrumentales son medidas directas hechas con instrumentos: termómetros de estaciones, boyas en el mar y satélites. Para épocas sin instrumentos se usan registros indirectos o proxies: anillos de árboles (en muchos árboles su grosor cambia con las condiciones de cada año), burbujas de aire antiguo atrapadas en testigos de hielo, sedimentos y corales. Un proxy no mide temperatura: se calibra comparándolo con épocas de las que sí hay mediciones.",
        "Evaluar una fuente es preguntar quién la produce, con qué método midió, cuándo y dónde, si entrega los datos, si declara su incertidumbre y si fue revisada por pares (otros especialistas independientes que evalúan el método antes de publicar). También se contrastan fuentes independientes: si distintos grupos y distintos proxies muestran un patrón parecido, la conclusión tiene más respaldo.",
        "Una anomalía es la diferencia entre un valor y un promedio de referencia. Si la referencia es 10 °C y un año marca 12 °C, la anomalía es +2 °C. Dos variables pueden subir juntas (correlación) sin que una cause la otra: los helados y el calor dependen de la estación. Para afirmar causalidad se necesita además un mecanismo físico y descartar otras explicaciones.",
    ],
    vocab=[("registro instrumental", "medida directa hecha con un instrumento"), ("proxy", "señal indirecta del clima pasado, como los anillos de árboles"), ("anomalía", "diferencia entre un valor y el promedio de referencia"), ("revisión por pares", "evaluación del método por especialistas independientes"), ("correlación", "dos variables que cambian juntas"), ("causalidad", "relación en que una variable produce el cambio de otra")],
    worked=[
        ("Calcular una anomalía", "En otra estación ficticia, la referencia de 30 años es 8 °C y un año marcó 9 °C. ¿Cuál es la anomalía?", ["Resta la referencia al valor: 9 − 8.", "Escribe el signo: el valor superó la referencia."], "La anomalía es +1 °C"),
        ("Correlación sin causalidad", "En un pueblo ficticio, cuando aumenta el uso de ventiladores sube la temperatura media del mes. ¿Los ventiladores causan el calor?", ["Los dos datos suben juntos: hay correlación.", "Hay una causa común: en los meses cálidos se usan más los ventiladores, no al revés."], "No: es correlación; el calor causa el uso de ventiladores"),
    ],
    mistakes=[("Creer que si dos datos suben juntos, uno causa al otro.", "Se confunde correlación con causalidad.", "Busca una causa común y un mecanismo físico antes de afirmar una causa."),
              ("Dar el mismo valor a una publicación anónima sin datos y a un informe con método y datos.", "Se evalúa por el titular y no por la calidad de la fuente.", "Pregunta quién, cómo, cuándo, dónde y si se pueden revisar los datos.")],
    T=[
        ("abc", "¿Cuál de estos es un registro indirecto (proxy) del clima pasado?", "Las burbujas de aire antiguo atrapadas en un testigo de hielo", "Un termómetro de una estación meteorológica actual", "Una boya que mide hoy la temperatura del mar", "Las burbujas de hielo conservan aire de otras épocas; los otros dos son instrumentos que miden hoy."),
        ("ab", "¿Para qué sirven los anillos de los árboles en esta clase?", "Para reconstruir condiciones de años pasados cuando no había termómetros", "Para medir con décimas la temperatura de hoy", "Su grosor cambia con las condiciones de cada año, y por eso sirven como registro del pasado."),
        ("abc", "¿Qué es una anomalía de temperatura?", "La diferencia entre un valor medido y el promedio de referencia", "Un termómetro descompuesto", "La temperatura más alta de un año", "La anomalía compara un valor con una referencia y por eso lleva signo."),
        ("abc", "{F} ¿Cuál fuente es más confiable para estudiar la temperatura de Cumbre?", "La fuente Y, porque se puede revisar su método y sus datos", "La fuente X, porque es anónima y por eso imparcial", "Las dos por igual, porque ambas hablan de temperatura", "Una fuente que explica su método y entrega datos permite que otros la revisen; la anónima no."),
        ("abc", "Se quiere saber si el combustible que se quema afecta la temperatura local. ¿Cuál es la variable que se mide como posible efecto?", "La temperatura medida", "La cantidad de combustible quemado", "El nombre de la ciudad", "El posible efecto es lo que cambia y se mide: aquí la temperatura."),
        ("ab", "¿Qué significa que una publicación sea revisada por pares?", "Otros especialistas independientes evaluaron su método antes de publicarla", "Dos personas de la misma institución la firmaron", "La revisión por pares la hacen especialistas independientes del equipo autor."),
        ("=", "{F} ¿Cuál es la anomalía del año 3, en °C?", "12-10", "La anomalía es el valor del año menos el promedio de referencia.", " °C"),
        ("=", "{F} ¿Cuál es la anomalía media de los cinco años (suma de las anomalías dividida por 5)?", "(0+1+2+1+1)//5", "Las anomalías son 0, 1, 2, 1 y 1, que suman 5; se divide por el número de años.", " °C"),
        ("abc", "Dos fuentes dan valores distintos de la temperatura de una ciudad. La primera explica su método y publica sus datos; la segunda no cita datos ni método. ¿Qué haces primero?", "Priorizo la primera, porque se puede revisar y contrastar", "Promedio ambos valores sin mirar de dónde vienen", "Elijo la segunda porque su valor es más alto", "Con una fuente verificable se puede comprobar el dato; la otra no entrega cómo se obtuvo."),
        ("abc", "En una ciudad, cuando suben las ventas de helados sube también la temperatura media del mes. ¿Qué conclusión es correcta?", "Hay correlación, pero ambos dependen de la estación del año: los helados no causan el calor", "Los helados calientan el aire", "El calor fabrica helados", "Una causa común (el verano) explica que ambas variables suban juntas."),
        ("abc", "Una estación meteorológica estaba en un campo abierto y hoy está rodeada de edificios y pavimento, que retienen calor. ¿Qué problema introduce al evaluar la tendencia?", "Parte del aumento medido puede venir del entorno local y no del clima global", "Ninguno, porque el pavimento no cambia la temperatura", "El termómetro deja de medir en °C", "Un cambio del entorno puede sesgar los datos; por eso se compara con estaciones cercanas bien ubicadas."),
        ("abc", "{F} Alguien dice: «El año 3 tuvo anomalía +2 °C, entonces el clima cambió». ¿Qué falta para sostener esa conclusión?", "Una serie larga que muestre si los valores altos se repiten y forman una tendencia", "Nada, un año basta", "Cambiar el promedio de referencia a 12 °C", "Un año puede ser excepcional; el clima cambia solo si hay una tendencia sostenida."),
        ("abc", "El grupo 1 reconstruye la temperatura de hace 500 años con anillos de un solo bosque. El grupo 2 usa anillos, testigos de hielo y sedimentos de tres regiones y obtiene un patrón parecido. ¿Qué conclusión tiene más respaldo?", "La del grupo 2, porque proxies independientes coinciden", "La del grupo 1, porque usó menos datos", "Ninguna, porque los proxies no sirven", "La coincidencia de fuentes independientes reduce el riesgo de error de un solo registro."),
    ],
    ctx=("abc", "Un colegio tiene una estación bajo el techo metálico soleado del gimnasio y quiere usar sus datos como evidencia del clima local. ¿Qué debería hacer primero?", "Comparar con una estación cercana bien ubicada y dejar anotado que su ubicación puede sesgar los valores", "Usar los datos igual, porque cualquier termómetro mide el clima", "Borrar los datos más altos", "Una ubicación expuesta al sol y al metal sesga la medición; contrastar con otra fuente permite corregirla o avisar el límite."),
    sc=[
        ("En Física del clima: ¿qué es un proxy?", "Una señal indirecta del clima pasado, como los anillos de árboles", "No mide temperatura directamente: se calibra con épocas medidas."),
        ("Si un año marca 14 °C y la referencia es 11 °C, ¿cuál es la anomalía?", "+3 °C", "Se resta la referencia: 14 − 11 = 3."),
        ("¿Dos variables que suben juntas prueban que una causa a la otra?", "No", "Puede haber una causa común; se necesita un mecanismo y descartar otras explicaciones."),
    ],
    op=("Recibes dos textos ficticios sobre la temperatura de la ciudad «Alto Sur». Texto 1: una publicación anónima que dice «hace más calor que nunca» sin datos. Texto 2: un informe de un instituto que explica que midió la temperatura media anual durante 30 años en tres estaciones y entrega la tabla. Evalúa ambos con cinco preguntas (quién, cómo, cuándo y dónde, si entrega datos, si declara incertidumbre) y concluye cuál usarías y qué te faltaría para estar seguro.",
        "Texto 1: no dice quién, cómo ni dónde; no entrega datos; no declara incertidumbre. Texto 2: identifica la institución, el método (tres estaciones, 30 años) y la tabla; me falta saber si fue revisado por otros especialistas. Usaría el 2 y lo contrastaría con otra fuente independiente.",
        ["aplica las cinco preguntas a cada texto", "elige una fuente con una razón concreta", "nombra qué falta para tener más seguridad"],
        ["hoja con una tabla de cinco filas y dos columnas, una por texto, y la conclusión"],
        ["elegir por el titular", "aceptar un dato sin pedir método", "confundir correlación con causa"],
        "Pregunta: «¿cómo podría otra persona comprobar este dato?». Si no hay manera, la fuente es débil."),
    reinforce="Con la ficha, calcula las anomalías de los cinco años y dibuja un gráfico de barras con ellas.",
    extend="Explica por qué un registro con muchos proxies independientes que coinciden es más convincente que uno solo, aunque ese uno sea muy preciso.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (de ejemplo, números redondeados). Constante solar S = 1360 W/m² (potencia por m² que llega perpendicular al Sol). Albedo de referencia = 0,3, es decir, 3 de cada 10 partes de la luz se reflejan. "
     "Promedio sobre toda la esfera: S ÷ 4. Bañera de CO2 (modelo de ejemplo, en unidades inventadas): cada año entran 40 unidades por emisiones y salen 15 por océano y vegetación; la reserva inicial es 100 unidades.")
build(
    O1, 3, F,
    use="Aprenderé a interpretar y usar dos modelos simples del clima: el balance de energía de la Tierra y la «bañera» de CO2, y a reconocer sus límites.",
    prior=["Sé que el Sol entrega energía a la Tierra.", "Sé multiplicar y dividir con números enteros y décimas simples.", "Sé qué es un porcentaje."],
    explain=[
        "El modelo de balance de energía compara lo que entra con lo que sale. El Sol entrega a la Tierra una potencia de unos 1360 W/m² medida sobre una superficie perpendicular a sus rayos (W es vatio, unidad de potencia). Como la Tierra es una esfera, la superficie que intercepta los rayos es un círculo, cuya área es la cuarta parte del área total de la esfera: el promedio es S ÷ 4, unos 340 W/m². Una parte de esa luz se refleja: el albedo.",
        "La energía absorbida por m² es (S ÷ 4) × (1 − albedo). En equilibrio, la energía que la Tierra devuelve al espacio como radiación infrarroja iguala a la absorbida. Los gases de efecto invernadero reducen la radiación infrarroja que escapa, así que la salida queda menor que la entrada y la temperatura sube hasta que la salida vuelve a igualar la entrada. Si baja el albedo (menos hielo), se absorbe más energía.",
        "El modelo de la bañera sirve para cantidades que se acumulan: la reserva cambia según lo que entra menos lo que sale. En la atmósfera, las emisiones de CO2 son la entrada y la absorción del océano y la vegetación son la salida; la concentración se mide en ppm (partes por millón: 1 ppm es una molécula de CO2 por cada millón de moléculas de aire). Todo modelo simplifica: estos dejan fuera nubes, corrientes marinas y muchos efectos, y por eso sirven para entender la lógica, no para predecir detalles.",
    ],
    vocab=[("albedo", "fracción de la luz solar que se refleja"), ("constante solar", "potencia solar por m² que llega perpendicular a los rayos"), ("equilibrio", "situación en que la energía que entra iguala a la que sale"), ("reserva", "cantidad acumulada en un modelo de bañera"), ("ppm", "partes por millón, unidad de concentración"), ("modelo", "representación simplificada de un sistema")],
    worked=[
        ("Energía absorbida", "En un planeta ficticio S = 1200 W/m² y el albedo es 0,2. ¿Cuánta energía por m² absorbe en promedio?", ["Promedio sobre la esfera: 1200 ÷ 4 = 300 W/m².", "Parte absorbida: 8 de cada 10 partes, es decir, 300 × 8 ÷ 10 = 240."], "240 W/m²"),
        ("Bañera", "Una reserva ficticia parte en 50 unidades; cada año entran 30 y salen 10. ¿Cuánto hay tras 2 años?", ["Cambio por año: 30 − 10 = +20 unidades.", "En 2 años: 50 + 2 × 20 = 90."], "90 unidades"),
    ],
    mistakes=[("Usar la constante solar completa (1360) sin dividir por 4 al calcular el promedio de la Tierra.", "Se olvida que la luz llega a un círculo y la Tierra tiene el área de una esfera.", "Divide por 4 antes de aplicar el albedo."),
              ("Sumar solo las entradas sin restar las salidas en la bañera.", "La reserva cambia por la diferencia entre entradas y salidas.", "Calcula primero entradas − salidas y luego multiplica por los años.")],
    T=[
        ("abc", "En el modelo de balance de energía, ¿qué significa albedo?", "La fracción de la luz solar que se refleja al espacio", "La cantidad de calor que producen los volcanes", "La concentración de CO2 en el aire", "El albedo mide la reflexión: hielo y nubes reflejan mucho; el océano, poco."),
        ("abc", "Si la energía que entra a la Tierra es mayor que la que sale, ¿qué ocurre con la temperatura del sistema?", "Sube hasta que la salida iguale a la entrada", "Baja hasta enfriarse", "Se mantiene igual para siempre", "Sobra energía, que se acumula como calor hasta que la salida crece y vuelve el equilibrio."),
        ("ab", "En la bañera de CO2, si entran más unidades de las que salen, la reserva", "aumenta", "disminuye", "La reserva cambia según entradas menos salidas; si sobran entradas, crece."),
        ("=", "{F} Calcula la potencia solar promedio por m² sobre toda la esfera terrestre (S ÷ 4).", "1360//4", "El área que intercepta la luz es la cuarta parte del área de la esfera.", " W/m²"),
        ("abc", "¿Por qué se divide la constante solar por 4 al promediar sobre la Tierra?", "Porque el círculo que intercepta los rayos tiene un cuarto del área de la esfera completa", "Porque el año tiene cuatro estaciones", "Porque la Tierra refleja cuatro partes de la luz", "El círculo de radio R tiene área πR² y la esfera 4πR²: la razón es 1 a 4."),
        ("abc", "¿Qué efecto tienen los gases de efecto invernadero en este modelo?", "Reducen la radiación infrarroja que escapa, y la temperatura sube hasta que la salida iguale a la entrada", "Aumentan la luz solar que llega a la Tierra", "Aumentan el albedo y enfrían el planeta", "Retienen calor infrarrojo: la salida baja y el sistema se calienta hasta compensar."),
        ("=", "{F} Calcula la energía solar absorbida por m² en promedio: (S ÷ 4) × (1 − albedo).", "1360//4*7//10", "Con albedo 0,3 se absorben 7 de cada 10 partes del promedio de 340 W/m².", " W/m²"),
        ("=", "{F} ¿Cuántas unidades tendrá la reserva de la bañera después de 3 años?", "100+3*(40-15)", "Cada año la reserva aumenta en entradas menos salidas.", " unidades"),
        ("=", "En un planeta ficticio S = 800 W/m² y el albedo es 0,5 (5 de cada 10 partes se reflejan). ¿Cuánta energía por m² absorbe en promedio?", "800//4*5//10", "Se promedia sobre la esfera y se conserva la mitad que no se refleja.", " W/m²"),
        ("abc", "{F} Si el albedo bajara de 0,3 a 0,2 por menos hielo y más superficie oscura, ¿qué pasa con la energía absorbida promedio?", "Aumenta, de 238 a 272 W/m²", "Disminuye, de 238 a 204 W/m²", "No cambia", "Con albedo 0,2 se absorben 8 de cada 10 partes de 340, es decir 272 W/m²."),
        ("abc", "Un estudiante dice: «el modelo de balance no sirve porque no incluye nubes ni corrientes marinas». ¿Qué respuesta es la más adecuada?", "Es una simplificación útil para ver la lógica entre entrada y salida de energía, y sus límites obligan a usar modelos más completos para detalles", "Tiene razón: un modelo que omite algo no enseña nada", "El modelo es exacto y no tiene límites", "Un modelo simple ilustra el mecanismo, pero se debe declarar qué deja fuera."),
        ("abc", "{F} ¿Cuántas unidades por año deberían entrar para que la reserva de la bañera se mantenga constante?", "15, igual a lo que sale", "0, porque nunca debe entrar nada", "40, que es lo actual", "La reserva no cambia solo si entradas y salidas son iguales."),
        ("=", "{F} Las salidas aumentan de 15 a 20 unidades por año y las entradas siguen en 40. ¿Cuántas unidades tendrá la reserva tras 4 años desde las 100 iniciales?", "100+4*(40-20)", "Con salidas de 20 la reserva crece 20 por año, y esa cantidad se suma durante 4 años.", " unidades"),
    ],
    ctx=("=", "Un colegio quiere explicar el balance de energía con una tabla para un planeta ficticio con S = 1000 W/m² y albedo 0,4 (4 de cada 10 partes se reflejan). ¿Qué valor de energía absorbida promedio por m² debe escribir en la tabla?", "1000//4*6//10", "Se promedia S entre 4 y se conservan 6 de cada 10 partes.", " W/m²"),
    sc=[
        ("En Física del clima: ¿qué relación debe cumplirse en equilibrio entre la energía que entra y la que sale?", "Son iguales", "En equilibrio no se acumula energía ni se pierde."),
        ("¿Qué fracción del área de la esfera terrestre es el círculo que intercepta los rayos del Sol?", "Un cuarto", "El círculo tiene área πR² y la esfera 4πR²."),
        ("En el modelo de la bañera, ¿qué se calcula para saber cuánto cambia la reserva en un año?", "Entradas menos salidas", "La reserva solo cambia por la diferencia entre lo que entra y lo que sale."),
    ],
    op=("Elige un planeta ficticio. Planeta 1: S = 600 W/m² y albedo 0,5. Planeta 2: S = 2000 W/m² y albedo 0,1. Calcula la energía absorbida por m² en promedio, explica con una frase qué pasaría con su temperatura si un gas retuviera parte del infrarrojo, y anota dos cosas que tu modelo deja fuera.",
        "Planeta 1: 600 ÷ 4 = 150 W/m²; se absorben 5 de cada 10 partes: 75 W/m². Si un gas retuviera parte del infrarrojo, saldría menos energía de la que entra y el planeta se calentaría hasta que la salida igualara a la entrada. El modelo deja fuera nubes y océanos.",
        ["calcula la energía absorbida con la fórmula correcta", "explica el efecto de un gas con la idea entrada y salida", "nombra al menos dos límites del modelo"],
        ["hoja con el cálculo paso a paso, la explicación y la lista de límites"],
        ["olvidar dividir por 4", "confundir albedo con absorción", "afirmar que el modelo es exacto"],
        "Pregunta: «¿qué parte de la luz absorbe tu planeta y qué haría un gas que retiene infrarrojo?»."),
    reinforce="Recalcula el ejemplo de la ficha con albedo 0,4 y compara el resultado con el de albedo 0,3.",
    extend="Explica por qué, en el modelo de la bañera, reducir las emisiones a la mitad no basta por sí solo para que la reserva deje de crecer si siguen siendo mayores que las salidas.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (de ejemplo, valores inventados y redondeados). Concentración de CO2 (ppm): año 0 = 300; año 20 = 320; año 40 = 350; año 60 = 390. "
     "Nivel del mar de un puerto ficticio (cm respecto de una referencia): año 0 = 0; año 30 = 6; año 60 = 15. Actividad solar (índice de 0 a 100), promedio por tramos: años 0 a 20 = 50; años 20 a 40 = 51; años 40 a 60 = 50. En esos 60 años la temperatura media del puerto subió (dato de ejemplo).")
build(
    O1, 4, F,
    use="Aprenderé a analizar evidencia sobre patrones, causas probables y efectos del cambio climático, calculando tendencias y contrastando explicaciones.",
    prior=["Sé calcular el cambio de una variable entre dos instantes.", "Sé qué es un modelo de balance de energía.", "Sé leer tablas con unidades."],
    explain=[
        "Los patrones observados son cambios que se repiten en muchos registros independientes: aumento de la temperatura media global desde fines del siglo XIX (del orden de 1 °C, cifra aproximada), retroceso de glaciares y aumento del nivel del mar. La concentración de CO2 pasó de cerca de 280 ppm antes de la industrialización a más de 400 ppm hoy (valores aproximados). Los testigos de hielo muestran que, durante cientos de miles de años, CO2 y temperatura variaron juntos.",
        "Las causas probables se contrastan con las alternativas. La quema de carbón, petróleo y gas libera CO2 que estuvo almacenado por millones de años; la deforestación y la ganadería también aportan gases. Causas naturales como la actividad solar, los volcanes y los ciclos orbitales existen, pero los registros de actividad solar de las últimas décadas no muestran un aumento comparable al del CO2 ni a la temperatura. Una causa se sostiene si hay un mecanismo físico (el CO2 absorbe infrarrojo) y si las alternativas no explican los datos.",
        "Entre los efectos está el aumento del nivel del mar, por dos razones: el agua se dilata al calentarse y el hielo de glaciares y capas de hielo sobre tierra firme se derrite y aporta agua nueva. El hielo marino que ya flota casi no cambia el nivel al derretirse. Además, el CO2 disuelto en el océano forma un ácido débil y baja su pH (acidificación). Para medir un ritmo se usa la tendencia: cambio de la variable dividido por el tiempo.",
    ],
    vocab=[("tendencia", "cambio de una variable dividido por el tiempo"), ("ppm", "partes por millón de CO2 en el aire"), ("dilatación térmica", "aumento de volumen de un material al calentarse"), ("acidificación", "disminución del pH del océano por CO2 disuelto"), ("atribución", "asignar una causa a un cambio observado"), ("hielo continental", "hielo sobre tierra firme, como glaciares")],
    worked=[
        ("Calcular una tendencia", "El CO2 de un lugar ficticio pasó de 280 a 340 ppm en 30 años. ¿Cuál es el ritmo medio?", ["Calcula el cambio: 340 − 280 = 60 ppm.", "Divide por el tiempo: 60 ÷ 30."], "2 ppm por año"),
        ("Descartar una causa", "En un período ficticio la actividad solar se mantiene en 40 mientras la temperatura sube de 14 a 15 °C. ¿La actividad solar explica ese aumento por sí sola?", ["Si fuera la causa, debería haber aumentado junto con la temperatura.", "Los datos muestran que no cambió: no puede explicar el alza."], "No: por sí sola no explica el aumento"),
    ],
    mistakes=[("Afirmar que como el CO2 y la temperatura suben juntos, el CO2 no puede ser la causa.", "Se confunde la existencia de correlación con la ausencia de causa.", "Revisa si hay un mecanismo físico y si las alternativas fueron descartadas."),
              ("Creer que al derretirse el hielo marino que flota sube mucho el nivel del mar.", "Ese hielo ya desplaza su propio peso en agua.", "Distingue hielo flotante (casi no cambia el nivel) de hielo continental (sí lo sube).")],
    T=[
        ("abc", "¿Cuál de estas es una causa humana del aumento del CO2 atmosférico?", "Quemar carbón, petróleo y gas", "Que el Sol salga cada día", "El movimiento de rotación de la Tierra", "La combustión de fósiles libera CO2 almacenado por millones de años; las otras no cambian su cantidad."),
        ("ab", "¿Qué hace subir el nivel del mar cuando se derriten glaciares ubicados sobre tierra firme?", "Agua que antes estaba sobre el continente llega al océano", "Hielo que ya flotaba en el mar y se derrite en el mismo lugar", "El agua de los glaciares continentales es un aporte nuevo al océano; el hielo flotante ya desplazaba su peso."),
        ("abc", "El aumento del CO2 disuelto en el océano provoca principalmente", "acidificación del agua", "que el océano se enfríe", "que el agua se vuelva más dulce", "El CO2 disuelto forma un ácido débil y baja el pH, es decir, acidifica."),
        ("=", "{F} ¿Cuántas ppm subió el CO2 entre el año 0 y el año 60?", "390-300", "El cambio es el valor final menos el inicial.", " ppm"),
        ("abc", "{F} ¿Qué indica la actividad solar de la ficha respecto de la idea de que el Sol explica el calentamiento?", "Casi no cambia, así que por sí sola no explica un aumento sostenido de la temperatura", "Subió tanto como el CO2 y por eso lo explica todo", "No se puede interpretar nunca", "Con un índice que se mantiene cerca de 50, el Sol no puede ser la causa de un alza sostenida."),
        ("abc", "¿Por qué los testigos de hielo sirven para estudiar el clima pasado?", "Guardan burbujas de aire antiguo y capas anuales que permiten reconstruir CO2 y temperatura de miles de años", "Miden hoy la temperatura del mar", "Contienen fotografías del pasado", "El aire atrapado en el hielo conserva la composición de la atmósfera de otras épocas."),
        ("=", "{F} ¿Cuántos cm subió el nivel del mar en el puerto entre el año 30 y el año 60?", "15-6", "Se resta el nivel inicial del final del tramo.", " cm"),
        ("=", "{F} Calcula el ritmo medio de aumento del CO2 entre el año 40 y el año 60, en ppm por año.", "(390-350)//20", "El cambio de 40 ppm se divide por 20 años.", " ppm por año"),
        ("abc", "{F} ¿En qué tramo de 20 años subió más rápido el CO2?", "Del año 40 al 60", "Del año 0 al 20", "Del año 20 al 40", "Los aumentos por tramo son 20, 30 y 40 ppm: el último es el mayor."),
        ("abc", "Alguien dice: «El CO2 y la temperatura suben juntos, así que el CO2 no puede ser la causa». ¿Qué falla en el razonamiento?", "Que suban juntos no descarta la causa; se evalúan además el mecanismo físico y las alternativas", "Nada: si suben juntos, la causa siempre es otra", "Nada: la causa siempre es el que sube primero", "La correlación no prueba ni descarta una causa; se necesita un mecanismo y descartar otras explicaciones."),
        ("abc", "{F} Un grupo afirma que el Sol explica el calentamiento de esos 60 años. ¿Qué dato de la ficha lo contradice?", "La actividad solar se mantiene cerca de 50 mientras el CO2 sube", "El nivel del mar sube", "El CO2 se mide en ppm", "Si el Sol fuera la causa, su actividad debería haber subido junto con la temperatura."),
        ("=", "{F} Si el nivel del mar siguiera subiendo al mismo ritmo medio que entre el año 30 y el 60, ¿cuántos cm más subiría en 20 años?", "9*20//30", "Entre los años 30 y 60 subió 9 cm en 30 años; ese ritmo se aplica a 20 años.", " cm"),
        ("abc", "Todo el hielo marino que flota en el océano Ártico se derrite. ¿Qué efecto tiene por el agua que aporta sobre el nivel del mar?", "Casi ninguno, porque ya desplazaba su propio peso de agua", "Sube tanto como si se derritiera un glaciar continental", "Baja de forma notable", "El hielo flotante desplaza un volumen de agua igual al que da al derretirse."),
    ],
    ctx=("abc", "Una comuna costera ficticia observa que su puerto sube 3 cm cada 10 años y que su glaciar de cabecera retrocede. Un vecino dice que «es solo el ciclo normal del Sol». ¿Cuál es la respuesta más sólida?", "Revisar si la actividad solar medida cambió en ese período; si no cambió, no explica el alza", "Aceptar la idea sin datos, porque el Sol es muy grande", "Descartar el glaciar porque los glaciares no cambian", "Una afirmación sobre causas se contrasta con datos: si el Sol no cambió, no explica el aumento."),
    sc=[
        ("En Física del clima: ¿qué es una tendencia?", "El cambio de una variable dividido por el tiempo", "Mide el ritmo con que cambia una variable."),
        ("¿Qué dos fenómenos hacen subir el nivel del mar al calentarse el planeta?", "La dilatación térmica del agua y el derretimiento del hielo continental", "Ambos fenómenos añaden volumen de agua al océano."),
        ("¿El hielo marino que flota sube mucho el nivel del mar al derretirse?", "No", "Ya desplazaba un volumen de agua igual a su derretimiento."),
    ],
    op=("Elige un conjunto de datos de ejemplo. Conjunto 1: CO2 en ppm: año 0 = 310; año 30 = 340; año 60 = 400. Conjunto 2: nivel del mar en cm: año 0 = 0; año 25 = 5; año 50 = 15. Calcula el cambio total y el ritmo medio, indica si el ritmo aumentó entre la primera y la segunda mitad y escribe qué otra causa deberías descartar antes de atribuir el cambio a la quema de combustibles.",
        "Conjunto 1: cambio total = 90 ppm en 60 años (1,5 ppm por año). Primera mitad: 30 ppm en 30 años (1 ppm por año); segunda: 60 ppm (2 ppm por año): el ritmo aumentó. Antes de atribuir la causa, descartaría un cambio en la actividad solar.",
        ["calcula cambio total y ritmo medio", "compara el ritmo de las dos mitades", "propone una causa alternativa que descartar"],
        ["hoja con los cálculos y una conclusión de tres líneas"],
        ["dividir por el tiempo equivocado", "mezclar unidades (ppm con cm)", "afirmar una causa sin descartar otras"],
        "Pregunta: «¿qué dato te permitiría descartar otra explicación?»."),
    reinforce="Con la ficha, calcula el aumento de CO2 en cada tramo de 20 años y escribe qué muestra sobre su ritmo.",
    extend="Explica por qué las dos razones del aumento del nivel del mar (dilatación y hielo continental) no se pueden estudiar con la misma medición.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (de ejemplo, valores redondeados e inventados para practicar). Factores de emisión de CO2 por kWh de energía eléctrica: carbón 1000 g; gas 500 g; solar 50 g. "
     "Un barrio consume 200 kWh por día. Medida A: cambiar la fuente del barrio, de carbón a solar. Medida B: cambiar de carbón a gas. Energía = potencia × tiempo, con potencia en kW y tiempo en horas.")
build(
    O1, 5, F,
    use="Aprenderé a comparar medidas de mitigación y de adaptación con criterios, calculando las emisiones de CO2 que evitan.",
    prior=["Sé qué causa el aumento del CO2.", "Sé multiplicar y restar con números enteros.", "Sé que 1 kg son 1000 g."],
    explain=[
        "La mitigación reduce las causas del cambio climático: disminuir emisiones (energías renovables, eficiencia energética, transporte público) o aumentar los sumideros (bosques que absorben CO2). La adaptación reduce los daños de los efectos que ya no se pueden evitar: sistemas de alerta de crecidas, muros de protección costera, cultivos que toleran sequía. Son complementarias: sin mitigación los efectos crecen y sin adaptación el daño inmediato es mayor.",
        "Para comparar medidas se necesita un efecto medible. La energía se calcula como potencia por tiempo: una cocina de 2 kW que funciona 3 horas usa 6 kWh (kilovatio-hora). Si cada kWh emite un factor de emisión (por ejemplo 1000 g de CO2 con carbón), las emisiones son energía × factor. La medida evita la diferencia entre el factor antes y el factor después, multiplicada por la energía.",
        "El número de emisiones evitadas no basta para decidir. Se comparan además el costo, el plazo en que funciona, los efectos colaterales (empleos, paisaje, salud) y quiénes se benefician. Una medida muy eficaz pero que se completa en 30 años puede ser menos útil que una más modesta que opera desde el primer año. La decisión debe explicitar qué criterios pesan más.",
    ],
    vocab=[("mitigación", "acciones que reducen las causas del cambio climático"), ("adaptación", "acciones que reducen daños de los efectos inevitables"), ("sumidero", "sistema que absorbe más CO2 del que emite, como un bosque"), ("kWh", "kilovatio-hora: energía de 1 kW durante 1 hora"), ("factor de emisión", "gramos de CO2 emitidos por cada kWh producido"), ("criterio", "aspecto que se usa para comparar opciones")],
    worked=[
        ("Calcular emisiones", "Una escuela ficticia usa 50 kWh por día con gas (500 g de CO2 por kWh). ¿Cuántos kg de CO2 emite por día?", ["Gramos: 50 × 500 = 25.000 g.", "Pasa a kg dividiendo por 1000."], "25 kg de CO2 por día"),
        ("Clasificar una medida", "Un pueblo ficticio instala alarmas para avisar de aludes. ¿Es mitigación o adaptación?", ["Pregunta si reduce la emisión de gases o reduce el daño de un efecto.", "Las alarmas no reducen emisiones: reducen el daño de un riesgo."], "Es adaptación"),
    ],
    mistakes=[("Elegir la medida que más reduce emisiones sin mirar plazo ni costo.", "Se usa un solo criterio.", "Compara al menos tres criterios y di cuál pesa más."),
              ("Olvidar convertir gramos a kilogramos.", "Los factores están en g y el resultado se pide en kg.", "Divide por 1000 al final.")],
    T=[
        ("abc", "¿Cuál de estas es una medida de mitigación?", "Reemplazar una central de carbón por energía solar", "Construir un muro contra el oleaje", "Sembrar cultivos que toleran la sequía", "Solo el cambio de fuente reduce las emisiones, que son la causa; las otras dos reducen daños."),
        ("abc", "¿Cuál de estas es una medida de adaptación?", "Instalar un sistema de alerta ante crecidas de ríos", "Cambiar una caldera de carbón por una solar", "Plantar un bosque para absorber CO2", "Una alerta reduce el daño de un efecto; las otras reducen emisiones o las absorben."),
        ("=", "Un horno eléctrico de 4 kW funciona 2 horas. ¿Cuántos kWh consume?", "4*2", "La energía es potencia por tiempo.", " kWh"),
        ("ab", "¿Por qué se dice que mitigación y adaptación son complementarias?", "Una reduce las causas y la otra reduce los daños de lo que ya no se puede evitar", "Porque ambas cuestan lo mismo", "Mitigar baja las emisiones futuras y adaptar protege de los efectos que llegan igual."),
        ("abc", "{F} ¿Qué mide el factor de emisión?", "Los gramos de CO2 emitidos por cada kWh producido con esa fuente", "La cantidad de kWh que consume un barrio", "El costo de cada kWh en pesos", "Es una razón entre masa de CO2 y energía producida por cada fuente."),
        ("abc", "¿Por qué una solución más barata puede no ser la mejor?", "Porque hay que comparar también su efecto, plazo y consecuencias para las personas", "Porque lo barato siempre contamina", "Porque el costo nunca se debe considerar", "Una buena decisión pesa varios criterios y no solo el costo."),
        ("=", "{F} Con carbón, ¿cuántos kg de CO2 emite el barrio en un día? (1000 g = 1 kg)", "200*1000//1000", "Se multiplican los kWh por el factor del carbón y se pasa a kg.", " kg"),
        ("=", "{F} ¿Cuántos kg de CO2 por día se evitan con la medida A?", "200*(1000-50)//1000", "Se multiplica el consumo por la diferencia de factores y se pasa a kg.", " kg"),
        ("=", "{F} ¿Cuántos kg de CO2 por día se evitan con la medida B?", "200*(1000-500)//1000", "Se multiplica el consumo por la diferencia entre carbón y gas.", " kg"),
        ("abc", "{F} Comparando solo las emisiones evitadas por día, ¿qué medida es mejor y cuánto más evita?", "A evita 90 kg más que B", "B evita 90 kg más que A", "Evitan lo mismo", "A evita 190 kg y B evita 100 kg por día; la diferencia es 90 kg."),
        ("abc", "Una isla sufre inundaciones frecuentes y el nivel del mar seguirá subiendo por décadas aunque se reduzcan las emisiones desde hoy. ¿Qué conviene priorizar en la isla?", "Medidas de adaptación, junto con apoyar la mitigación global", "Solo mitigación local, porque la adaptación no sirve", "Ninguna, por ser un problema global", "El daño ya es inevitable en parte, así que se necesita adaptación además de mitigar."),
        ("=", "La medida C reduce 100 kg de CO2 por día pero solo desde el día 51 de un plan de 100 días. La medida D reduce 80 kg por día desde el día 1. ¿Cuántos kg más habrá evitado D que C al terminar el día 100?", "100*80-50*100", "D actúa 100 días y C solo 50 días; se comparan los totales.", " kg"),
        ("=", "Una casa gasta 10 kWh por día de calefacción con gas (500 g de CO2 por kWh). Con aislación gasta 6 kWh por día. ¿Cuántos g de CO2 evita por día?", "(10-6)*500", "Ahorra 4 kWh y cada kWh evita 500 g de CO2.", " g"),
    ],
    ctx=("abc", "Una comuna costera ficticia evalúa dos proyectos: un muro de contención contra marejadas y un programa de aislación térmica en viviendas. ¿Cómo se clasifican, en ese orden?", "Adaptación y mitigación", "Mitigación y adaptación", "Ambos son mitigación", "El muro reduce el daño de un efecto; la aislación baja la energía usada y, con ella, las emisiones."),
    sc=[
        ("En Física del clima: ¿qué es un sumidero de carbono?", "Un sistema que absorbe más CO2 del que emite, como un bosque", "Los sumideros retiran CO2 de la atmósfera."),
        ("¿Cuánta energía consume un aparato de 3 kW durante 2 horas?", "6 kWh", "La energía se calcula como potencia por tiempo."),
        ("¿Basta con comparar las emisiones evitadas para decidir entre medidas?", "No", "También se comparan costo, plazo, efectos colaterales y quiénes se benefician."),
    ],
    op=("Elige un problema. Problema 1: una ciudad ficticia cuyo transporte público usa buses diésel y quiere reducir emisiones. Problema 2: un pueblo ficticio con crecidas de río cada invierno. Propón una medida de mitigación o de adaptación (según el problema), clasifícala, compárala con una alternativa usando tres criterios (efecto, costo, plazo) y justifica tu elección. Usa datos de ejemplo que inventes y rotula como «de ejemplo».",
        "Problema 2: medida 1: sistema de alerta (adaptación), efecto: avisa con 2 horas de anticipación, costo bajo, plazo de 6 meses. Medida 2: muro (adaptación), efecto: protege casi todas las casas, costo alto, plazo 3 años. Elijo la 1 primero y la 2 después, porque es rápida y barata.",
        ["clasifica correctamente la medida", "compara con una alternativa en tres criterios", "justifica la elección con los criterios"],
        ["hoja con una tabla de comparación de dos medidas y tres criterios, y la justificación"],
        ["usar solo el costo", "clasificar mal una medida", "inventar cifras sin rotularlas «de ejemplo»"],
        "Pregunta: «¿qué criterio pesó más en tu decisión y por qué?»."),
    reinforce="Con la ficha, calcula cuánto CO2 emite el barrio en un día con cada fuente (carbón, gas y solar).",
    extend="Explica por qué una medida de adaptación puede ser necesaria incluso si todos los países redujeran sus emisiones mañana.",
)

# ============================================================ OAC-01, clase 6
F = ("Ficha 6 (de ejemplo, valores inventados). Proyección del aumento del nivel del mar en un puerto ficticio en 50 años: escenario de emisiones bajas, entre 10 y 20 cm; escenario de emisiones altas, entre 30 y 50 cm. "
     "Medición actual del nivel: 120 cm ± 2 cm.")
build(
    O1, 6, F,
    use="Aprenderé a comunicar con honestidad lo que se sabe y lo que no sobre el cambio climático, usando rangos y escenarios, y a decidir bajo incertidumbre.",
    prior=["Sé interpretar proyecciones con rangos.", "Sé comparar medidas con criterios.", "Sé que toda medición tiene un margen de error."],
    explain=[
        "La incertidumbre es el margen en que puede estar un valor. Se escribe con un rango: «120 cm ± 2 cm» significa que el valor verdadero probablemente está entre 118 y 122 cm. Una proyección del futuro también lleva rango, porque depende de cuánto se emita de gases y de cómo responde el sistema. Por eso se presentan escenarios: «si las emisiones son bajas, ocurre esto; si son altas, ocurre esto otro». Un escenario no es una predicción única, sino una condicional.",
        "Comunicar con honestidad significa entregar la fuente, el período, las unidades y el rango; usar un lenguaje graduado («es muy probable», «es probable») y distinguir lo bien establecido (el CO2 aumenta y el planeta se calienta) de lo más incierto (la magnitud exacta en un lugar). También implica no truncar un eje para exagerar un cambio pequeño ni mostrar solo los datos que apoyan una idea.",
        "Tener incertidumbre no es ignorancia: se puede decidir con rangos. Al diseñar una obra de larga duración se suele usar el escenario más desfavorable razonable para tener margen de seguridad, y se prefieren decisiones reversibles o ajustables cuando la información cambia. Decidir implica explicar qué criterios pesan más: costo, riesgo, plazo y justicia entre las personas afectadas.",
    ],
    vocab=[("incertidumbre", "margen en que puede estar un valor"), ("escenario", "proyección que depende de supuestos, como el nivel de emisiones"), ("rango", "intervalo entre un valor mínimo y uno máximo"), ("eje truncado", "eje de un gráfico que no parte desde cero y exagera cambios pequeños"), ("margen de seguridad", "holgura que se agrega al diseñar para cubrir lo desfavorable"), ("reversible", "que se puede deshacer o ajustar después")],
    worked=[
        ("Leer un rango", "Una medición ficticia dice 50 cm ± 3 cm. ¿Entre qué valores probablemente está el valor verdadero?", ["Límite inferior: 50 − 3 = 47.", "Límite superior: 50 + 3 = 53."], "Entre 47 y 53 cm"),
        ("Elegir escenario", "Un muelle ficticio durará 40 años. Sus proyecciones son: emisiones bajas, 8 a 12 cm; altas, 25 a 40 cm. ¿Qué valor máximo usar para tener margen?", ["Elige el escenario más desfavorable razonable: emisiones altas.", "Toma su extremo superior: 40 cm."], "40 cm, y se informa el rango completo"),
    ],
    mistakes=[("Presentar un número único («subirá 15 cm») sin rango, escenario ni fuente.", "Parece más exacto, pero oculta la incertidumbre.", "Escribe siempre el rango, el escenario y la fuente."),
              ("Pensar que la incertidumbre impide decidir.", "Se confunde no saber con no poder comparar escenarios.", "Decide con el rango, eligiendo un margen de seguridad.")],
    T=[
        ("abc", "¿Qué es un escenario climático?", "Una proyección que depende de supuestos sobre las emisiones futuras", "Una predicción exacta del día en que ocurrirá un evento", "El nombre de una estación meteorológica", "Un escenario es condicional: dice qué pasa si ocurre cierto nivel de emisiones."),
        ("abc", "La expresión 120 cm ± 2 cm significa que", "el valor verdadero probablemente está entre 118 y 122 cm", "el valor es exactamente 120 cm", "el valor está entre 100 y 140 cm", "El ± indica el margen: se suma y se resta 2 al valor central."),
        ("ab", "¿Qué debe incluir un gráfico honesto?", "Fuente, período, unidades y rango de incertidumbre", "Solo la parte que apoya la idea del autor", "Un gráfico honesto permite a otra persona revisar y contrastar los datos."),
        ("=", "{F} ¿Cuál es el ancho del rango de la proyección de emisiones altas, en cm?", "50-30", "El ancho es el máximo menos el mínimo.", " cm"),
        ("abc", "{F} ¿Por qué se entregan dos escenarios y no un solo número?", "Porque el resultado depende de decisiones futuras de emisiones y además hay incertidumbre", "Porque los científicos no saben nada del tema", "Porque dos números son más fáciles de graficar", "El nivel del mar futuro depende de cuánto se emita y de cómo responde el sistema."),
        ("abc", "¿Cuál oración comunica mejor la incertidumbre?", "Es muy probable que el nivel suba entre 10 y 20 cm en 50 años si las emisiones son bajas", "El nivel subirá exactamente 15 cm", "Nadie puede saber nada del futuro", "Entrega probabilidad, rango, plazo y condición; las otras dan certeza falsa o ninguna información."),
        ("=", "{F} ¿Cuántos cm separan el extremo superior del escenario de emisiones altas del extremo superior del de emisiones bajas?", "50-20", "Se resta el máximo bajo del máximo alto.", " cm"),
        ("=", "{F} Con la medición actual como valor central, ¿cuál es el nivel máximo posible dentro del margen de error, en cm?", "120+2", "Se suma el margen al valor central.", " cm"),
        ("abc", "Un gráfico muestra la temperatura entre 14,0 y 14,5 °C, pero su eje vertical va de 14,0 a 14,6 °C, y el aumento parece enorme. ¿Qué problema de comunicación tiene?", "El eje truncado exagera un cambio pequeño", "Ninguno, porque está en °C", "Que usa números decimales", "Si el eje no parte de un valor razonable, un cambio pequeño parece grande."),
        ("abc", "{F} Si el puerto planea una obra para durar 50 años, ¿qué escenario conviene usar para diseñar la protección con margen de seguridad?", "El de emisiones altas, porque protege también en el caso desfavorable razonable", "El de emisiones bajas, porque es el más probable por definición", "Ninguno, porque hay incertidumbre", "Con obras largas y daños costosos se diseña para el caso desfavorable, informando el rango."),
        ("abc", "Una autoridad dice: «No hay certeza exacta, así que no hay que hacer nada». ¿Qué problema tiene?", "Confunde incertidumbre con ignorancia: se puede decidir con rangos y escenarios", "Ninguno, porque sin certeza no se decide", "Que la certeza exacta siempre existe", "La incertidumbre se maneja con rangos, escenarios y márgenes de seguridad."),
        ("=", "Se midió dos veces el nivel de un puerto: 120 cm ± 2 cm y 125 cm ± 2 cm. ¿Cuántos cm hay entre el extremo inferior de la segunda (123 cm) y el superior de la primera? (Un valor positivo significa que los rangos no se traslapan).", "123-122", "El extremo inferior de la segunda es 125 − 2 y el superior de la primera 120 + 2; la resta indica si se separan.", " cm"),
        ("abc", "Un informe dice «el nivel subirá 15 cm en 50 años» sin rango, sin escenario y sin fuente. ¿Qué elementos le faltan para comunicar con honestidad?", "Rango de incertidumbre, escenario de emisiones y fuente de los datos", "Color, título y fecha de impresión", "Firma, logotipo y número de página", "Sin esos tres elementos el lector no puede evaluar ni revisar la afirmación."),
    ],
    ctx=("abc", "Un colegio debe presentar a su comunidad la proyección de la ficha en un afiche. ¿Cuál texto es el más honesto?", "«En 50 años el mar subiría entre 10 y 20 cm si bajan las emisiones, y entre 30 y 50 cm si siguen altas (datos de ejemplo)»", "«El mar subirá 50 cm y será una catástrofe»", "«No se sabe nada del futuro»", "Presenta escenarios con rangos y rotula los datos; las otras opciones exageran o no informan."),
    sc=[
        ("En Física del clima: ¿qué significa 30 cm ± 4 cm?", "Que el valor está probablemente entre 26 y 34 cm", "El margen se resta y se suma al valor central."),
        ("¿Un escenario es una predicción única?", "No", "Es una proyección condicionada a supuestos, como el nivel de emisiones."),
        ("¿Qué elementos básicos debe llevar un dato bien comunicado?", "Fuente, período, unidades y rango", "Con ellos otras personas pueden revisar el dato."),
    ],
    op=("Elige una afirmación. Afirmación 1: «El nivel del mar subirá 40 cm». Afirmación 2: «Habrá más sequías en la zona central». Reescríbela con honestidad: agrega período, escenario, rango (inventa uno rotulado «de ejemplo»), fuente ficticia y un límite. Luego escribe una frase que explique qué decisión tomarías con esa información y por qué.",
        "Afirmación 1 reescrita: «En 50 años el nivel del mar del puerto Sur subiría entre 30 y 50 cm si las emisiones siguen altas (estimación de ejemplo, Instituto ficticio X); no incluye cambios locales del terreno». Decisión: diseñar el muelle con 50 cm de margen.",
        ["incluye período, escenario, rango y fuente", "declara un límite", "justifica una decisión usando el rango"],
        ["hoja con la afirmación original, la reescrita y la decisión"],
        ["dar un número único", "usar lenguaje alarmista", "olvidar rotular los datos inventados"],
        "Pregunta: «¿qué diría una persona que lea tu texto sobre cuánto sabes y cuánto no?»."),
    reinforce="Convierte «subirá 15 cm» en una frase con rango, escenario y fuente (con datos de ejemplo rotulados como tales).",
    extend="Explica por qué usar el escenario más desfavorable razonable al diseñar una obra no es lo mismo que afirmar que ese escenario ocurrirá.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (de ejemplo, línea de tiempo simplificada). Siglo XVI: Copérnico propone el modelo heliocéntrico. Año 1915: Einstein publica la relatividad general. "
     "Año 1929: Hubble informa que las galaxias lejanas se alejan de nosotros. Año 1965: se detecta la radiación cósmica de fondo.")
build(
    O2, 1, F,
    use="Aprenderé a delimitar preguntas de cosmología y a reconocer, con apoyo de la historia de la ciencia, cómo cambiaron las explicaciones sobre el universo.",
    prior=["Sé qué es una galaxia y una estrella.", "Sé que la luz viaja con rapidez finita.", "Sé que un modelo científico puede cambiar con nuevas observaciones."],
    explain=[
        "En Física, la cosmología estudia el origen, la evolución y la estructura del universo. Su sistema de estudio es el universo observable: la parte desde la cual ha podido llegarnos luz desde que existe. Una buena pregunta cosmológica es medible y acotada, por ejemplo: «¿cómo cambió la distancia entre galaxias lejanas a lo largo de miles de millones de años?». Preguntas como «¿qué es lo más bello del cielo?» no se pueden contrastar con observaciones.",
        "Una explicación científica se apoya en observaciones y en modelos que otras personas pueden contrastar, corregir o rechazar. Los relatos míticos y religiosos del universo cumplen otras funciones (dar sentido, identidad y ética) y no se evalúan con mediciones. La historiografía de la ciencia estudia cómo y por qué cambiaron las ideas: del modelo geocéntrico (Tierra al centro) al heliocéntrico (Sol al centro) y de un universo estático a uno en expansión.",
        "Los cambios no ocurren por decreto ni por moda: surgen cuando nuevas observaciones y mejores teorías explican más datos. Copérnico propuso en el siglo XVI el modelo heliocéntrico; el telescopio se usó para observar el cielo desde inicios del siglo XVII. La relatividad general de Einstein (1915) permitía universos que se expanden, y las observaciones de Hubble (1929) mostraron que las galaxias lejanas se alejan, lo que respaldó el modelo de expansión.",
    ],
    vocab=[("cosmología", "estudio del origen, evolución y estructura del universo"), ("universo observable", "parte del universo de la que ha podido llegarnos luz"), ("geocéntrico", "modelo con la Tierra en el centro"), ("heliocéntrico", "modelo con el Sol en el centro"), ("historiografía", "estudio de cómo y por qué cambian las ideas con el tiempo"), ("fuente primaria", "documento o dato original de la época estudiada")],
    worked=[
        ("Delimitar una pregunta", "Mejora «¿Cómo es el universo?» para convertirla en una pregunta de cosmología.", ["Elige qué se estudia: la distancia entre galaxias lejanas.", "Agrega una variable y un tiempo: cómo cambia a lo largo de miles de millones de años."], "«¿Cómo cambió la distancia entre galaxias lejanas en miles de millones de años?»"),
        ("Ordenar ideas", "Ordena de más antigua a más reciente: modelo de universo en expansión, modelo geocéntrico, modelo heliocéntrico.", ["El geocéntrico es la idea más antigua y dominó en la antigüedad.", "El heliocéntrico se propuso en el siglo XVI y la expansión en el siglo XX."], "Geocéntrico, heliocéntrico, expansión"),
    ],
    mistakes=[("Pensar que las ideas científicas cambian por decisión de una autoridad.", "Se ignora que cambian por nuevas observaciones y mejores explicaciones.", "Pregunta qué dato nuevo apoyó el cambio."),
              ("Mezclar fechas y hechos sin comprobar el orden (por ejemplo, el telescopio con Copérnico).", "Se une todo en una sola «época».", "Ubica cada hecho en una línea de tiempo antes de explicar.")],
    T=[
        ("abc", "¿Qué estudia la cosmología?", "El origen, la evolución y la estructura del universo", "Solo la composición química del Sol", "Los climas de cada país", "La cosmología se ocupa del universo como un todo y de su historia."),
        ("abc", "¿Qué es el universo observable?", "La parte del universo de la que ha podido llegarnos luz", "Todo el universo, sin límite alguno", "Solo el Sistema Solar", "Solo lo que la luz ha alcanzado puede observarse."),
        ("abc", "En el modelo geocéntrico, ¿qué ocupa el centro?", "La Tierra", "El Sol", "La Vía Láctea", "Geo significa Tierra; en ese modelo todo gira alrededor de ella."),
        ("abc", "¿Qué distingue a una explicación científica del universo?", "Se puede contrastar con observaciones y corregir si los datos no calzan", "Es más antigua que las otras", "Usa palabras más difíciles", "Su criterio es la contrastación con datos observables."),
        ("abc", "{F} ¿Qué hecho de la ficha aporta una observación directa a favor de un universo en expansión?", "Año 1929: Hubble informa que las galaxias lejanas se alejan", "Siglo XVI: Copérnico propone el modelo heliocéntrico", "Año 1915: Einstein publica la relatividad general", "Alejarse es una observación; la relatividad general es una teoría y Copérnico trató otro asunto."),
        ("ab", "¿Qué es la historiografía de la ciencia?", "El estudio de cómo y por qué cambiaron las ideas científicas con el tiempo", "La lista de instrumentos de un laboratorio", "Estudia el desarrollo histórico de las ideas y no solo sus resultados."),
        ("=", "{F} ¿Cuántos años pasaron entre la publicación de la relatividad general y el informe de Hubble?", "1929-1915", "Se resta el año anterior al posterior.", " años"),
        ("abc", "Ordena cronológicamente, de más antiguo a más reciente: I) radiación cósmica de fondo detectada, II) propuesta de Copérnico, III) informe de Hubble.", "II, III, I", "III, II, I", "II, I, III", "El siglo XVI precede a 1929 y 1929 precede a 1965."),
        ("abc", "Una pregunta bien delimitada de cosmología es:", "¿Cómo cambió la distancia entre galaxias lejanas en miles de millones de años?", "¿Por qué el universo es tan hermoso?", "¿Cuál es el mejor planeta?", "Tiene sistema, variable y escala de tiempo, y se puede contrastar con datos."),
        ("abc", "Un modelo pasa de «universo estático» a «universo en expansión». ¿Qué lo justifica según la historia de la ciencia?", "Nuevas observaciones (galaxias que se alejan) y una teoría que las explicaba mejor", "Un decreto de un gobierno", "Que el modelo anterior era más antiguo", "Los modelos cambian cuando datos nuevos y mejores explicaciones lo respaldan."),
        ("abc", "¿Por qué un modelo científico del universo siempre puede revisarse?", "Porque cada observación nueva puede confirmarlo, ajustarlo o contradecirlo", "Porque los científicos cambian de opinión por moda", "Porque nunca se usan datos", "La ciencia queda abierta a la contrastación futura."),
        ("abc", "Un texto afirma: «Copérnico demostró en el siglo XVI, con un telescopio, que la Tierra gira alrededor del Sol». ¿Qué problema historiográfico tiene?", "Mezcla hechos: el telescopio se usó en astronomía desde inicios del siglo XVII y Copérnico propuso un modelo sin él", "Ninguno, porque es exacto", "Copérnico propuso el modelo geocéntrico", "Se debe ubicar cada hecho en su época antes de relacionarlo."),
        ("abc", "La fuente 1 es un libro de divulgación escrito cien años después de una observación y la fuente 2 es la carta original de quien la hizo. Para saber qué observó realmente, ¿cuál es mejor punto de partida?", "La fuente 2, por ser primaria, aunque se contraste con otras", "La fuente 1, por ser más reciente", "Ninguna de las dos", "Una fuente primaria está más cerca de lo ocurrido, aunque debe contrastarse."),
    ],
    ctx=("abc", "Un museo ficticio quiere un panel titulado «¿Por qué cambió la idea que se tenía del universo?». ¿Qué texto es el más adecuado según la historia de la ciencia?", "Porque nuevas observaciones, como el alejamiento de las galaxias, y teorías que las explicaban mejor respaldaron la nueva idea", "Porque una autoridad ordenó cambiar la idea", "Porque la idea anterior ya era muy vieja", "Las ideas científicas cambian cuando datos nuevos y mejores explicaciones las respaldan, no por orden ni por antigüedad."),
    sc=[
        ("En Física: ¿qué es el universo observable?", "La parte del universo de la que ha podido llegarnos luz", "Solo lo que su luz alcanzó puede observarse."),
        ("¿Qué observación de 1929 respaldó el modelo de expansión?", "Que las galaxias lejanas se alejan de nosotros", "Esa observación fue informada por Hubble."),
        ("¿Las ideas científicas cambian por decreto?", "No", "Cambian cuando nuevas observaciones y teorías las respaldan."),
    ],
    op=("Elige un tema. Tema 1: del modelo geocéntrico al heliocéntrico. Tema 2: del universo estático al universo en expansión. Escribe (a) una pregunta cosmológica delimitada, (b) una línea de tiempo con tres hechos (usa solo los de esta clase), (c) qué observación o teoría motivó el cambio y (d) una limitación de esa línea de tiempo (por ejemplo, qué hechos se dejaron fuera).",
        "Tema 2: (a) ¿Cómo cambia la distancia entre galaxias lejanas con el tiempo? (b) 1915: relatividad general; 1929: Hubble informa que galaxias lejanas se alejan; 1965: se detecta la radiación cósmica de fondo. (c) Las galaxias que se alejan. (d) La línea omite a otros investigadores.",
        ["pregunta con variable y escala", "tres hechos en orden cronológico", "relaciona el cambio con observaciones o teoría"],
        ["hoja con las cuatro partes (a) a (d) completas"],
        ["ordenar mal los hechos", "preguntas valorativas", "atribuir el cambio a una autoridad"],
        "Pregunta: «¿qué dato nuevo hizo cambiar la idea?»."),
    reinforce="Escribe en una línea de tiempo los cuatro hechos de la ficha y subraya cuál es una observación y cuál es una teoría.",
    extend="Explica por qué contrastar una fuente primaria con una de divulgación ayuda a detectar errores históricos.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (de ejemplo, datos inventados). Constante de Hubble de ejemplo: H = 70 km/s por Mpc (Mpc = megaparsec, unidad de distancia muy grande que se usa para galaxias). "
     "Galaxia P a 10 Mpc; galaxia Q a 30 Mpc; galaxia R a 50 Mpc. Ley: velocidad de alejamiento v = H × distancia d.")
build(
    O2, 2, F,
    use="Aprenderé a evaluar qué observaciones respaldan la expansión del universo, a usar la ley de Hubble y a reconocer las variables y límites de las mediciones.",
    prior=["Sé que la luz tiene una rapidez finita.", "Sé usar proporciones.", "Sé que las galaxias están a distancias enormes."],
    explain=[
        "Para saber si una galaxia se acerca o se aleja se estudia su luz. Al descomponerla en colores (espectro) aparecen líneas que corresponden a elementos conocidos. Si la fuente se aleja, esas líneas se desplazan hacia longitudes de onda mayores, es decir, hacia el rojo: es el desplazamiento al rojo. Si se acerca, se desplazan hacia el azul. La medida del corrimiento permite calcular la velocidad de la galaxia.",
        "La ley de Hubble relaciona dos variables: la velocidad de alejamiento v y la distancia d de la galaxia, mediante v = H × d. Por ejemplo, con H = 70 km/s por Mpc, una galaxia a 10 Mpc se aleja a 700 km/s. La distancia debe medirse con otro método independiente (por ejemplo, a partir del brillo de objetos de luminosidad conocida), pues la ley relaciona dos medidas distintas. Las mediciones iniciales tenían incertidumbres grandes y se han mejorado con instrumentos mejores.",
        "La ley describe el promedio a grandes distancias: galaxias cercanas también se mueven por su atracción gravitatoria local. Por eso hay galaxias con desplazamiento al azul sin que se contradiga la expansión. Al evaluar una fuente sobre este tema conviene revisar qué variable se midió, con qué método, qué incertidumbre se declara y si distintos grupos con métodos independientes obtienen resultados compatibles.",
    ],
    vocab=[("espectro", "luz descompuesta en colores o longitudes de onda"), ("desplazamiento al rojo", "corrimiento de la luz hacia longitudes de onda mayores cuando la fuente se aleja"), ("constante de Hubble (H)", "razón entre la velocidad de alejamiento y la distancia"), ("Mpc", "megaparsec: unidad de distancia usada para galaxias"), ("velocidad de alejamiento", "rapidez con que una galaxia se separa de nosotros"), ("método independiente", "forma de medir que no usa el mismo dato que la otra medida")],
    worked=[
        ("Calcular v", "Con H = 70 km/s por Mpc, una galaxia ficticia está a 8 Mpc. ¿Con qué velocidad se aleja?", ["Usa v = H × d.", "Calcula 70 × 8 = 560."], "560 km/s"),
        ("Calcular d", "Otra galaxia ficticia se aleja a 4.900 km/s. Con H = 70 km/s por Mpc, ¿a qué distancia está?", ["Despeja d = v ÷ H.", "Calcula 4.900 ÷ 70 = 70."], "70 Mpc"),
    ],
    mistakes=[("Confundir la constante H (70 km/s por Mpc) con la velocidad de una galaxia.", "H es una razón; la velocidad depende de la distancia.", "Multiplica H por la distancia de cada galaxia."),
              ("Decir que una sola galaxia con desplazamiento al azul refuta la expansión.", "Las galaxias cercanas se mueven por gravedad local, no solo por la expansión.", "Aplica la ley a muestras grandes y lejanas.")],
    T=[
        ("abc", "¿Qué indica el desplazamiento al rojo de la luz de una galaxia?", "Que la galaxia se aleja de nosotros", "Que la galaxia se acerca", "Que la galaxia es de color rojo por su composición", "Las líneas del espectro se corren hacia longitudes mayores cuando la fuente se aleja."),
        ("abc", "En la ley v = H × d, ¿qué representa d?", "La distancia a la galaxia", "La velocidad de la galaxia", "La masa de la galaxia", "En la fórmula, v es la velocidad y d la distancia."),
        ("ab", "Según la ley de Hubble, una galaxia más lejana se aleja", "más rápido", "más lento", "La velocidad es proporcional a la distancia: a mayor distancia, mayor velocidad."),
        ("=", "{F} ¿Con qué velocidad se aleja la galaxia Q, en km/s?", "70*30", "Se multiplica H por la distancia de la galaxia Q.", " km/s"),
        ("abc", "{F} ¿Qué significa que H valga 70 km/s por Mpc?", "Que por cada Mpc de distancia la velocidad de alejamiento aumenta 70 km/s", "Que la galaxia mide 70 km", "Que el universo mide 70 Mpc", "Es una razón entre velocidad y distancia."),
        ("abc", "¿Por qué hay que medir la distancia con un método distinto del desplazamiento al rojo para comprobar la ley de Hubble?", "Porque la ley relaciona dos medidas independientes: velocidad (desde el desplazamiento al rojo) y distancia (desde otro método)", "Porque el desplazamiento al rojo no existe", "Porque la distancia no se puede medir nunca", "Si ambas salieran del mismo dato, la relación sería circular."),
        ("=", "{F} ¿Con qué velocidad se aleja la galaxia R, en km/s?", "70*50", "Se multiplica H por la distancia de la galaxia R.", " km/s"),
        ("=", "{F} ¿Cuántos km/s más rápido se aleja R que Q?", "70*50-70*30", "Se calcula la velocidad de cada galaxia y se resta.", " km/s"),
        ("=", "Una galaxia se aleja a 2.100 km/s. Con H = 70 km/s por Mpc, ¿a qué distancia está, en Mpc?", "2100//70", "La distancia es la velocidad dividida por H.", " Mpc"),
        ("abc", "Se miden dos galaxias: una a 20 Mpc con velocidad 1.400 km/s y otra a 40 Mpc con 2.800 km/s. ¿Qué relación entre velocidad y distancia se observa?", "Proporcional: al duplicar la distancia se duplica la velocidad", "No hay relación", "Al duplicar la distancia la velocidad baja a la mitad", "Los cocientes 1.400 ÷ 20 y 2.800 ÷ 40 dan el mismo valor, 70."),
        ("abc", "Una galaxia vecina muestra desplazamiento al azul (se acerca). ¿Contradice la expansión del universo?", "No: la gravedad local mueve las galaxias cercanas, y la ley describe el promedio a grandes distancias", "Sí, y la expansión queda anulada", "Sí, porque todas las galaxias deberían alejarse sin excepción", "Cerca, la atracción gravitatoria domina sobre la expansión."),
        ("abc", "Una fuente de divulgación dice: «todas las galaxias se alejan a exactamente 70 km/s». ¿Qué error comete respecto de la ley de Hubble?", "Confunde la constante H con la velocidad, que depende de la distancia", "Ninguno, porque 70 es la velocidad universal", "Que el desplazamiento al rojo no se mide en km/s", "La velocidad cambia con la distancia, y 70 es una razón y no una velocidad."),
        ("abc", "Un nuevo método muestra que todas las galaxias están al doble de la distancia supuesta y las velocidades no cambian. ¿Qué pasa con el valor calculado de H?", "Se reduce a la mitad", "Se duplica", "No cambia", "H = v ÷ d; si d se duplica con v igual, H se divide por 2."),
    ],
    ctx=("=", "Un grupo ficticio recibe la distancia de una galaxia: 60 Mpc. Con la constante de la ficha, ¿qué velocidad de alejamiento esperan, en km/s?", "70*60", "Se multiplica H por la distancia dada.", " km/s"),
    sc=[
        ("En Física: ¿qué mide el desplazamiento al rojo de una galaxia?", "Su velocidad de alejamiento", "El corrimiento de las líneas del espectro depende de la velocidad."),
        ("Con H = 70 km/s por Mpc, ¿a cuánto se aleja una galaxia a 20 Mpc?", "1.400 km/s", "Se multiplica la constante H por la distancia de 20 Mpc."),
        ("¿Por qué una galaxia cercana puede acercarse sin refutar la expansión?", "Porque la gravedad local domina a corta distancia", "La ley de Hubble vale en promedio a grandes distancias."),
    ],
    op=("Elige una galaxia: galaxia 1 a 15 Mpc o galaxia 2 a 45 Mpc (datos de ejemplo, con H = 70 km/s por Mpc). Calcula su velocidad de alejamiento, explica qué observarías en su espectro, di qué otra medida necesitas para verificar la distancia y escribe una frase sobre una limitación del cálculo.",
        "Galaxia 1: v = 70 × 15 = 1.050 km/s. En su espectro las líneas estarían corridas hacia el rojo. La distancia se verifica con otro método, por ejemplo el brillo de objetos de luminosidad conocida. Limitación: H tiene incertidumbre y la ley es un promedio.",
        ["calcula v con la fórmula", "relaciona la velocidad con el espectro", "nombra un método independiente y una limitación"],
        ["hoja con el cálculo y las tres explicaciones"],
        ["usar H como velocidad", "confundir rojo con acercamiento", "no mencionar la incertidumbre"],
        "Pregunta: «¿qué medida de la galaxia viene del espectro y cuál de otro método?»."),
    reinforce="Con la ficha, calcula las velocidades de las galaxias P, Q y R y anota qué patrón siguen.",
    extend="Explica por qué la ley de Hubble no puede aplicarse a una sola galaxia cercana para decidir si el universo se expande.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (de ejemplo). Modelo de la masa con pasas: las pasas representan galaxias y la masa representa el espacio. Tres pasas A, B y C están en línea a 2, 4 y 6 cm de una pasa observadora; "
     "en una hora la masa duplica su tamaño y todas las distancias se duplican. Modelo de ejemplo en unidades inventadas: la velocidad de alejamiento es la distancia dividida por 10 (v = d ÷ 10).")
build(
    O2, 3, F,
    use="Aprenderé a interpretar un modelo de la expansión del universo (masa con pasas), a razonar la historia del universo hacia el pasado y a reconocer los límites del modelo.",
    prior=["Sé qué es una razón y una proporcionalidad.", "Sé usar velocidad = distancia ÷ tiempo.", "Sé que las galaxias se alejan unas de otras."],
    explain=[
        "El modelo de la masa con pasas ayuda a imaginar la expansión: cuando la masa crece, todas las distancias entre pasas aumentan. Una pasa a 2 cm de la observadora se aleja 2 cm si la masa duplica su tamaño; una a 6 cm se aleja 6 cm. Por eso las más lejanas se alejan más: ese es el origen de la proporcionalidad v = H × d. Además, desde cualquier pasa parece que las demás se alejan; no existe un «centro» de la expansión.",
        "Si las galaxias se alejan hoy, en el pasado estuvieron más cerca. Si todas se hubieran alejado con velocidad constante, la distancia dividida por la velocidad daría el tiempo transcurrido, y ese cociente es igual para todas: 1 ÷ H. Con la constante real, este cálculo da un orden de magnitud cercano a los 14 mil millones de años, consistente con la estimación actual de unos 13.800 millones de años.",
        "El universo temprano era muy caliente y denso; al expandirse se enfrió. En los primeros minutos se formaron los núcleos de helio y de otros elementos muy ligeros; después de unos cientos de miles de años se formaron átomos neutros y la luz pudo viajar libre; luego, con la gravedad, surgieron estrellas y galaxias. El Big Bang no fue una explosión en un punto de un espacio vacío: ocurrió en todo el espacio a la vez. Los límites del modelo: no muestra la gravedad que mantiene unidos a los sistemas ni la radiación.",
    ],
    vocab=[("expansión", "aumento de las distancias entre galaxias lejanas con el tiempo"), ("Big Bang", "modelo según el cual el universo fue muy caliente y denso y se expande desde entonces"), ("proporcional", "que crece en la misma razón que otra cantidad"), ("1 ÷ H", "tiempo que resulta de dividir la distancia por la velocidad, igual para todas las galaxias"), ("átomo neutro", "átomo con la misma cantidad de cargas positivas y negativas"), ("modelo", "representación simplificada de un sistema")],
    worked=[
        ("Expansión de la masa", "En el modelo, una pasa está a 3 cm de la observadora y la masa se triplica en una hora. ¿A qué distancia queda y cuánto se alejó?", ["Todas las distancias se triplican: 3 × 3 = 9 cm.", "Se alejó 9 − 3 = 6 cm."], "Queda a 9 cm y se alejó 6 cm"),
        ("Tiempo hacia atrás", "En un modelo ficticio, una galaxia está a 90 unidades y se aleja a 6 unidades por segundo con rapidez constante. ¿Hace cuántos segundos estaba junto a nosotros?", ["Tiempo = distancia ÷ velocidad.", "Calcula 90 ÷ 6 = 15."], "Hace 15 segundos"),
    ],
    mistakes=[("Pensar que el Big Bang ocurrió en un punto del espacio con vacío alrededor.", "Se imagina una explosión dentro de un espacio ya existente.", "Piensa en el espacio mismo expandiéndose en todas partes."),
              ("Creer que la pasa del medio es el centro de la expansión.", "Desde cualquier pasa se ve que las demás se alejan.", "Cambia de pasa observadora y comprueba que ocurre lo mismo.")],
    T=[
        ("abc", "En el modelo de la masa con pasas, ¿qué representan las pasas?", "Las galaxias", "Las estrellas individuales", "Los planetas", "Las pasas se separan unas de otras, igual que las galaxias lejanas."),
        ("abc", "En ese modelo, ¿qué representa que la masa crezca?", "La expansión del espacio entre las galaxias", "Que cada galaxia se hace más grande", "Una explosión que lanza galaxias desde un centro", "La masa que crece hace que aumenten las distancias entre pasas."),
        ("ab", "En el modelo, ¿hay una pasa que sea el «centro» de la expansión?", "No: desde cualquier pasa las demás se alejan", "Sí: la que está en medio", "Cada pasa ve alejarse a las demás, sin lugar privilegiado."),
        ("=", "{F} ¿Cuántos cm miden las distancias de la pasa C a la observadora una hora después?", "6*2", "Todas las distancias se duplican.", " cm"),
        ("=", "{F} ¿Cuántos cm se alejó la pasa B de la observadora en esa hora?", "4*2-4", "Se resta la distancia inicial de la final.", " cm"),
        ("abc", "¿Qué limitación tiene el modelo de la masa con pasas?", "No muestra la gravedad que mantiene unidos a los sistemas ni la radiación del universo temprano", "Muestra todo el universo con exactitud", "Muestra que las galaxias se destruyen", "Es una analogía simple y por eso deja fuera fuerzas y radiación."),
        ("=", "En el modelo, una pasa que estaba a 5 cm de la observadora queda a 10 cm una hora después. Con la misma proporción, ¿a qué distancia queda una pasa que estaba a 9 cm?", "9*2", "La distancia inicial se duplica: 5 cm pasó a 10 cm, así que 9 cm pasa al doble.", " cm"),
        ("=", "En un modelo de ejemplo una galaxia está a 120 unidades y se aleja a 8 unidades por segundo con rapidez constante. ¿Hace cuántos segundos estaba junto a nosotros?", "120//8", "El tiempo es la distancia dividida por la velocidad.", " s"),
        ("abc", "{F} En esa hora, ¿qué relación hay entre cuánto se alejó cada pasa y su distancia inicial?", "Es proporcional: al duplicar la distancia inicial se duplica lo que se aleja", "No hay relación", "Se alejan más las que estaban más cerca", "Las pasas se alejaron 2, 4 y 6 cm, igual a sus distancias iniciales."),
        ("abc", "El universo temprano era muy caliente y denso. ¿Qué ocurrió con su temperatura al expandirse?", "Bajó, porque la energía se repartió en un volumen cada vez mayor", "Subió, porque había más espacio", "Se mantuvo igual", "Al expandirse, el universo se enfrió."),
        ("abc", "¿Dónde ocurrió el Big Bang según el modelo de expansión?", "En todo el espacio a la vez, no en un punto con espacio vacío alrededor", "En un punto del espacio y la materia salió disparada", "En el centro del Sol", "El espacio mismo se expande; no hay un centro desde el cual salga la materia."),
        ("=", "{F} En el modelo de ejemplo v = d ÷ 10 (en unidades por segundo). Una galaxia se aleja a 30 unidades por segundo. ¿A qué distancia está?", "30*10", "Se despeja d multiplicando la velocidad por 10.", " unidades"),
        ("abc", "{F} En ese modelo, ¿cuánto vale d ÷ v para cualquier galaxia?", "10 segundos, el mismo para todas", "Es distinto para cada galaxia", "30 segundos", "Como v = d ÷ 10, el cociente d ÷ v es siempre 10."),
    ],
    ctx=("abc", "Una profesora ficticia imagina un globo con puntos dibujados que se infla. ¿Qué punto se aleja más rápido de uno elegido como referencia?", "El que está más lejos de la referencia", "El que está más cerca de la referencia", "Todos se alejan con la misma rapidez", "En la expansión, a mayor distancia, mayor velocidad de alejamiento."),
    sc=[
        ("En Física: ¿qué representa la masa en el modelo de la masa con pasas?", "El espacio", "Las pasas son galaxias; la masa que crece es el espacio."),
        ("¿Cuántos centros tiene la expansión del universo en el modelo?", "Ninguno", "Desde cualquier galaxia se ve alejarse a las demás."),
        ("¿Qué pasa con la temperatura del universo al expandirse?", "Baja", "La energía se reparte en un volumen mayor."),
    ],
    op=("Elige un caso. Caso 1: modelo con tres pasas a 1, 3 y 5 cm de una pasa observadora y una masa que se triplica. Caso 2: modelo con v = d ÷ 20 (en unidades inventadas) y galaxias a 100, 200 y 400 unidades. Calcula las nuevas distancias o las velocidades, comprueba la proporcionalidad y escribe dos límites del modelo.",
        "Caso 1: las distancias finales son 3, 9 y 15 cm; se alejaron 2, 6 y 10 cm, proporcional a 1, 3 y 5 (el doble). Límites: no incluye gravedad y no explica el origen de la expansión.",
        ["calcula distancias o velocidades con la regla", "comprueba la proporcionalidad", "nombra dos límites del modelo"],
        ["hoja con una tabla de tres filas y la conclusión"],
        ["aplicar mal la razón", "no comprobar la proporcionalidad", "creer que el modelo es el universo"],
        "Pregunta: «¿desde otra pasa ocurre lo mismo?»."),
    reinforce="Haz una tabla con la distancia inicial, la final y cuánto se alejó cada pasa de la ficha.",
    extend="Explica con tus palabras por qué el cociente distancia ÷ velocidad da la misma edad para todas las galaxias en el modelo simple.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (cifras aproximadas). Velocidad de la luz: unos 300.000 km/s. Un año luz es la distancia que recorre la luz en un año: unos 9,5 billones de km. "
     "Distancia Tierra–Sol: unos 150 millones de km. Composición aproximada del gas primordial, en masa: 75 % hidrógeno y 25 % helio. La radiación cósmica de fondo corresponde a una temperatura de unos −270 °C. Edad estimada del universo: unos 13.800 millones de años.")
build(
    O2, 4, F,
    use="Aprenderé a analizar las principales evidencias del modelo del Big Bang y a reconocer las preguntas que aún siguen abiertas.",
    prior=["Sé que las galaxias se alejan y que el universo se expande.", "Sé calcular tiempos con velocidad y distancia.", "Sé calcular porcentajes de una cantidad."],
    explain=[
        "El modelo del Big Bang caliente se apoya en tres evidencias independientes. Primera: la expansión, observada en el alejamiento de las galaxias. Segunda: la radiación cósmica de fondo, una luz débil de microondas que llega de todas direcciones con una temperatura de unos −270 °C; es la luz liberada cuando el universo se enfrió lo suficiente para formar átomos neutros. Tercera: la proporción de elementos ligeros, de unos 75 % de hidrógeno y 25 % de helio, que coincide con lo que predice el universo temprano.",
        "Mirar lejos es mirar al pasado: la luz tarda en llegar. La luz del Sol demora unos 500 segundos, porque 150.000.000 km ÷ 300.000 km/s = 500 s. Un año luz es una distancia, no un tiempo. Si una galaxia está a 100 millones de años luz, vemos cómo era hace 100 millones de años. Así se puede observar el pasado del universo y contrastar el modelo.",
        "Las evidencias no explican todo. Para entender cómo giran las galaxias y cómo se agrupan se propone la materia oscura, y para explicar que la expansión se acelera se propone la energía oscura. Son nombres para efectos medidos cuya naturaleza aún no se conoce, y son campos de investigación abiertos. Hablar de ellas con honestidad significa decir qué se mide y qué se ignora.",
    ],
    vocab=[("radiación cósmica de fondo", "luz débil de microondas que llega de todas direcciones, resto del universo temprano"), ("año luz", "distancia que recorre la luz en un año"), ("elementos ligeros", "hidrógeno y helio, los primeros que se formaron"), ("materia oscura", "materia que no emite luz pero se detecta por su gravedad"), ("energía oscura", "nombre del efecto que acelera la expansión, aún sin explicar"), ("evidencia independiente", "dato obtenido por un método distinto del de otras evidencias")],
    worked=[
        ("Tiempo de la luz", "La luz de una lámpara ficticia viaja 600.000 km a 300.000 km/s. ¿Cuánto demora?", ["Tiempo = distancia ÷ velocidad.", "600.000 ÷ 300.000 = 2."], "2 segundos"),
        ("Fracción de elementos", "En 400 kg de un gas con 75 % de hidrógeno, ¿cuántos kg son de hidrógeno?", ["75 % es 75 de cada 100.", "400 × 75 ÷ 100 = 300."], "300 kg"),
    ],
    mistakes=[("Creer que un año luz es una unidad de tiempo.", "El nombre incluye «año», pero mide distancia.", "Recuerda: año luz = distancia recorrida por la luz en un año."),
              ("Decir que la materia oscura es una invención porque no se ve.", "Se infiere por sus efectos gravitatorios y su naturaleza se investiga.", "Distingue lo medido (efecto) de lo desconocido (naturaleza).")],
    T=[
        ("abc", "¿Cuál de estas es una de las tres evidencias principales del Big Bang caliente que se estudian en la clase?", "La radiación cósmica de fondo", "El número de satélites artificiales", "La edad de los volcanes", "La radiación de fondo es luz del universo temprano, y es una de las tres evidencias."),
        ("abc", "¿Cuál es la proporción aproximada de hidrógeno en el gas primordial, en masa?", "75 %", "25 %", "5 %", "Del gas primordial, unos 75 % es hidrógeno y 25 % helio."),
        ("ab", "La luz de una galaxia muy lejana salió hace mucho tiempo, así que mirar lejos es", "mirar al pasado", "mirar al futuro", "La luz tarda en llegar, y por eso vemos a la galaxia como era cuando salió la luz."),
        ("abc", "¿Qué es un año luz?", "La distancia que recorre la luz en un año", "El tiempo que dura un año en otra galaxia", "La velocidad de la luz medida en un año", "Es una distancia, igual a la rapidez de la luz por un año."),
        ("abc", "¿Por qué la radiación cósmica de fondo respalda el Big Bang?", "Porque un universo muy caliente y denso que se enfrió debería dejar una luz débil y uniforme en todas direcciones", "Porque es la luz de una sola estrella", "Porque prueba que el universo es estático", "Su uniformidad y su temperatura coinciden con lo esperado de un universo que se enfrió."),
        ("abc", "¿Qué son la materia oscura y la energía oscura en cosmología?", "Hipótesis necesarias para explicar observaciones (rotación de galaxias y expansión acelerada), cuya naturaleza aún se investiga", "Gases ya identificados en laboratorio", "Sombras producidas por las nubes de polvo", "Se infieren por sus efectos medidos y siguen siendo un tema de investigación abierto."),
        ("=", "{F} ¿Cuántos segundos tardaría la luz en recorrer el doble de la distancia Tierra–Sol?", "2*150000000//300000", "Se duplica la distancia y se divide por la velocidad de la luz.", " s"),
        ("=", "{F} Si 25 de cada 100 partes de masa del gas primordial son helio, ¿cuántos kg de helio hay en 2.000 kg de ese gas?", "2000*25//100", "Se toma el 25 % de la masa total.", " kg"),
        ("=", "Una nave ficticia viaja a la décima parte de la velocidad de la luz. ¿Cuántos años tardaría en recorrer 20 años luz?", "20*10", "Con una rapidez diez veces menor que la de la luz, tarda diez veces más.", " años"),
        ("abc", "Si las galaxias se alejan hoy, ¿qué se infiere hacia el pasado?", "Que estuvieron más cerca, y que el universo fue más denso y caliente", "Que estuvieron igual de lejos", "Que no existían", "Al retroceder en el tiempo, las distancias y el volumen eran menores."),
        ("abc", "Una persona afirma: «Como la materia oscura no se ve, es una invención». ¿Qué respuesta es más razonable?", "Se infiere por sus efectos gravitatorios medidos; su naturaleza aún no se conoce y es un tema de investigación abierto", "Tiene razón: lo que no se ve no puede estudiarse", "Ya se fabricó en laboratorio, así que todo está resuelto", "La ciencia estudia efectos medibles aunque la causa no se haya identificado."),
        ("abc", "Un grupo propone que el universo siempre fue igual y no tuvo origen. ¿Qué evidencia de la clase es más difícil de explicar con esa idea?", "La radiación cósmica de fondo y la proporción de hidrógeno y helio", "Que existan galaxias", "Que la Luna gire alrededor de la Tierra", "Ambas evidencias son huellas de un universo más caliente y denso en el pasado."),
        ("=", "{F} La luz de una galaxia tardó 6.000 millones de años en llegar. ¿Cuántos millones de años habían pasado desde el origen cuando salió esa luz?", "13800-6000", "A la edad del universo se le resta el tiempo de viaje de la luz.", " millones de años"),
    ],
    ctx=("abc", "Una persona observa con un telescopio una galaxia a 100 millones de años luz. ¿Qué ve?", "La galaxia como era hace 100 millones de años", "La galaxia tal como es hoy", "La galaxia como será en 100 millones de años", "La luz tarda 100 millones de años en llegar, así que muestra la galaxia del pasado."),
    sc=[
        ("En Física: ¿cuáles son las tres evidencias principales del modelo del Big Bang caliente que se estudian en esta clase?", "La expansión, la radiación cósmica de fondo y la proporción de elementos ligeros", "Son tres evidencias independientes entre sí."),
        ("¿Un año luz mide tiempo o distancia?", "Distancia", "Es lo que recorre la luz en un año."),
        ("¿Cuánto tarda la luz en recorrer 900.000 km a 300.000 km/s?", "3 segundos", "Se divide la distancia por la velocidad de la luz."),
    ],
    op=("Elige una afirmación para evaluar. Afirmación 1: «El Big Bang no tiene ninguna evidencia». Afirmación 2: «La materia oscura ya se identificó por completo». Escribe si es correcta o no, nombra al menos dos evidencias de la clase para sostener tu respuesta y escribe qué parte sigue siendo desconocida.",
        "Afirmación 1: es incorrecta. Evidencias: la expansión observada en el alejamiento de las galaxias y la radiación cósmica de fondo. Falta conocer, por ejemplo, la naturaleza de la materia oscura y de la energía oscura.",
        ["decide si la afirmación es correcta", "nombra dos evidencias", "indica qué es desconocido"],
        ["hoja con la respuesta en tres partes"],
        ["decir que todo está resuelto", "negar sin evidencia", "confundir año luz con tiempo"],
        "Pregunta: «¿qué dato medido sostiene tu respuesta?»."),
    reinforce="Calcula cuántos segundos tarda la luz en recorrer 1.200.000 km a 300.000 km/s.",
    extend="Explica por qué la coincidencia de tres evidencias independientes es más convincente que una sola.",
)
