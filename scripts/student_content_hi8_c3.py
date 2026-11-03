"""Cuaderno del estudiante, 8.º básico Historia, Geografía y Ciencias Sociales: OA 21 (conectividad, migración y desigualdades regionales)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 21"
MAT = "Lápiz y papel; una calculadora es opcional. Las fichas, tablas y testimonios (de ejemplo) están escritos en cada ejercicio; no necesitas atlas ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = ("Fichas de ejemplo (localidades inventadas). Bahía Norte: camino pavimentado a la capital regional, 3 viajes de bus al día, antena de internet, consultorio y colegio. "
      "Isla Chica: se llega solo en barco 2 veces por semana, internet inestable, una posta rural con una técnica en enfermería y una escuela básica. "
      "Valle Alto: camino de ripio que se cierra por nieve unas semanas al año, un bus al día, internet solo en la escuela.")
build(
    OA, 1, F1,
    use="Aprenderé a medir la conectividad y el aislamiento de un lugar según sus redes de transporte, de comunicaciones y su acceso a bienes, servicios e información. Sirve para entender desigualdades dentro de un país largo como Chile.",
    prior=["Sé leer fichas y tablas.", "Sé qué es una región y un territorio.", "Sé multiplicar y restar números de cuatro cifras."],
    explain=[
        "La conectividad es la facilidad con que un lugar se relaciona con otros. Depende de las redes de transporte, como caminos, puertos y aeropuertos, y de las redes de comunicaciones, como la telefonía y el internet. Un lugar bien conectado llega rápido a otros lugares y recibe información con facilidad.",
        "El aislamiento es lo contrario: una conectividad baja que dificulta llegar a otros lugares o recibir lo que se necesita. No depende solo de la distancia. Un lugar cercano puede quedar aislado si su camino se corta con la nieve, y un lugar lejano puede estar bien conectado si tiene buen transporte e internet. El aislamiento también puede ser temporal, como cuando un temporal impide navegar.",
        "Un buen indicador de conectividad es el acceso a bienes, servicios e información. Bienes son los productos que se compran, servicios son la salud, la educación o el transporte, e información es lo que se sabe por medios como el internet. Cuando el acceso es bajo, las personas pierden oportunidades y quedan más vulnerables. En un país largo y con cordillera, mar y desierto, como Chile, esto es un desafío real.",
    ],
    vocab=[("conectividad", "facilidad con que un lugar se relaciona con otros"), ("aislamiento", "conectividad baja que dificulta llegar o recibir lo necesario"), ("red de transporte", "conjunto de caminos, puertos, aeropuertos u otras vías"), ("red de comunicaciones", "conjunto de medios como telefonía e internet"), ("acceso", "posibilidad real de llegar a un bien, servicio o información")],
    worked=[
        ("Leer una ficha", "{F} En la ficha de Isla Chica, ¿qué dato muestra baja conectividad de transporte?",
         ["Busco cómo se llega al lugar.", "Solo hay barco 2 veces por semana."], "Solo se llega en barco 2 veces por semana"),
        ("Distinguir distancia y aislamiento", "Un valle está a 40 km de una ciudad, pero su camino se cierra por nieve semanas. ¿Está aislado solo por la distancia?",
         ["Cuarenta km es una distancia corta.", "El aislamiento viene del corte del camino."], "No; lo aísla el corte del camino"),
    ],
    mistakes=[
        ("Decir que un lugar está aislado solo porque queda lejos.", "También cuentan las redes y los servicios.", "Revisa transporte, comunicaciones y acceso a servicios."),
        ("Creer que con un solo camino ya no hay aislamiento.", "También importan internet, servicios y horarios.", "Mira todos los tipos de conectividad."),
    ],
    T=[
        ("En Geografía: ¿qué es la conectividad?", "La facilidad con que un lugar se relaciona con otros", "Depende de redes de transporte y comunicaciones."),
        ("{F} ¿Cómo se llega a Isla Chica?", "Solo en barco 2 veces por semana", "Lo indica la ficha."),
        ("{F} ¿Qué localidad tiene la mayor conectividad de transporte? A) Bahía Norte, B) Isla Chica, C) Valle Alto.", "A", "Tiene camino pavimentado y 3 buses al día."),
        ("¿Cuál es una red de transporte? A) una antena de internet, B) un puerto, C) un consultorio.", "B", "Un puerto permite llegar y salir por mar."),
        ("{F} ¿Por qué el camino de Valle Alto produce aislamiento temporal?", "Porque se cierra por nieve unas semanas al año", "Interrumpe el transporte por un tiempo."),
        ("{F} ¿Qué acceso a información tiene Valle Alto? A) internet solo en la escuela, B) ninguno, C) internet en cada casa.", "A", "La ficha lo dice."),
        ("=", "{F} Si el barco a Isla Chica sale 2 veces por semana, ¿cuántos viajes hace en 6 semanas?", "2*6", "Se multiplican los viajes por las semanas."),
        ("=", "{F} Bahía Norte tiene 3 buses al día y Valle Alto uno. ¿Cuántos buses más tiene Bahía Norte en una semana de 7 días?", "(3-1)*7", "Se calcula la diferencia diaria y se multiplica por siete."),
        ("{F} Un compañero dice que Isla Chica está aislada solo porque queda lejos. Corrígelo.", "Su aislamiento viene de que solo hay barco dos veces por semana, internet inestable y pocos servicios, no solo de la distancia", "El aislamiento depende de las redes y los servicios."),
        ("{F} Si un temporal impide navegar, ¿qué localidad queda sin acceso externo directo? A) Bahía Norte, B) Isla Chica, C) Valle Alto.", "B", "Solo se llega a ella por barco."),
        ("{F} ¿Qué dos servicios tiene Isla Chica según la ficha?", "Una posta rural y una escuela básica", "Los nombra la ficha."),
        ("Evalúa la frase «El aislamiento se resuelve solo con construir más caminos». ¿Qué le falta considerar?", "Que también importan el internet, los servicios locales y el acceso a información", "Hay más tipos de conectividad que los caminos."),
        ("{F} ¿Qué medida mejora el acceso a salud de Isla Chica aunque el barco sea semanal? A) internet estable para consultas a distancia con profesionales, B) cerrar la posta, C) quitar los viajes en barco.", "A", "La comunicación puede acercar un servicio."),
    ],
    ctx=("En tu curso una compañera dice que su abuela vive en un pueblo «aislado» porque queda a 80 km de la ciudad, aunque hay un bus cada hora y buen internet. ¿Qué dato muestra que ese pueblo no está tan aislado como se cree?", "El bus cada hora y el buen internet", "Hay conectividad de transporte y de comunicaciones."),
    sc=[("En Geografía: ¿qué es el aislamiento?", "Una conectividad baja que dificulta llegar o recibir lo necesario", "No depende solo de la distancia."),
        ("Nombra una red de comunicaciones.", "Por ejemplo: el internet o la telefonía", "Transmiten información entre lugares distintos."),
        ("¿Qué incluye el acceso a servicios?", "Por ejemplo: salud, educación y transporte", "Son servicios que se usan a diario.")],
    op=("{F} Compara dos localidades de la ficha con tres criterios: transporte, comunicaciones y servicios. Después escribe cuál tiene mayor riesgo de aislamiento y por qué.",
        "Comparo Bahía Norte e Isla Chica. Transporte: camino pavimentado y 3 buses frente a barco 2 veces por semana. Comunicaciones: antena de internet frente a internet inestable. Servicios: consultorio y colegio frente a posta y escuela básica. Isla Chica tiene mayor riesgo de aislamiento porque depende del barco.",
        ["compara con tres criterios", "usa datos de la ficha", "concluye con justificación"], ["tres comparaciones y una conclusión"], ["comparar solo la distancia", "no justificar la conclusión"], "Pide a una persona de tu casa que te diga cuál criterio le parece más importante."),
    reinforce="Anota cómo llegan a tu casa el transporte, el internet y los servicios de salud.",
    extend="Escribe una situación en que un lugar cercano esté aislado de manera temporal.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = ("Tabla de ejemplo, tres comunas inventadas. "
      "Roble: 24.000 habitantes, 120 km², 360 nacimientos y 240 defunciones en el año, llegaron 500 personas y salieron 300. "
      "Cerro: 6.000 habitantes, 300 km², 60 nacimientos y 90 defunciones, llegaron 100 personas y salieron 250. "
      "Mar: 40.000 habitantes, 80 km², 600 nacimientos y 320 defunciones, llegaron 900 personas y salieron 400.")
build(
    OA, 2, F2,
    use="Aprenderé a leer y calcular índices demográficos (densidad, natalidad, mortalidad, crecimiento natural y migración neta). Sirve para describir cómo cambia la población de una región.",
    prior=["Sé dividir y multiplicar números de varias cifras.", "Sé leer una tabla.", "Sé qué es una comuna y una región."],
    explain=[
        "La demografía estudia las poblaciones. Un índice demográfico es un número que resume un aspecto de la población. La densidad de población indica cuántos habitantes hay por cada kilómetro cuadrado: se calcula dividiendo los habitantes por la superficie en km². La tasa de natalidad es el número de nacimientos de un año por cada 1.000 habitantes, y la tasa de mortalidad, el número de defunciones por cada 1.000 habitantes.",
        "El crecimiento natural es la diferencia entre nacimientos y defunciones del año. Si nacen más personas de las que mueren, es positivo; si mueren más, es negativo. La migración neta es la diferencia entre las personas que llegan a un lugar (inmigrantes) y las que salen (emigrantes). El cambio total de la población combina ambos: crecimiento natural más migración neta.",
        "Cada índice responde una pregunta. La densidad dice qué tan concentrada está la gente; la natalidad y la mortalidad, cómo se renueva; la migración, si el lugar atrae o expulsa. Siempre leo la unidad (por km², por 1.000 habitantes) y comparo lugares con la misma unidad. Los datos de este cuaderno son de ejemplo y no representan comunas reales.",
    ],
    vocab=[("densidad de población", "habitantes por cada kilómetro cuadrado"), ("tasa de natalidad", "nacimientos del año por cada 1.000 habitantes"), ("crecimiento natural", "nacimientos menos defunciones del año"), ("migración neta", "personas que llegan menos personas que salen"), ("inmigrante / emigrante", "persona que llega a un lugar / persona que sale de él")],
    worked=[
        ("Calcular la densidad", "Una comuna de ejemplo tiene 9.000 habitantes y 30 km². ¿Cuál es su densidad?",
         ["Divido habitantes por superficie.", "9.000 ÷ 30 = 300."], "300 habitantes por km²"),
        ("Calcular migración neta", "En una comuna de ejemplo llegaron 700 personas y salieron 400. ¿Cuál es la migración neta?",
         ["Resto las que salen a las que llegan.", "700 - 400 = 300."], "+300; la comuna gana población"),
    ],
    mistakes=[
        ("Confundir tasa con cantidad: pensar que la comuna con más nacimientos tiene más natalidad.", "La tasa se mide por cada 1.000 habitantes.", "Divide por los habitantes antes de comparar."),
        ("Olvidar la unidad (km² o por 1.000 habitantes).", "Sin unidad el número no se entiende.", "Escribe siempre la unidad."),
    ],
    T=[
        ("En Geografía: ¿qué es la densidad de población?", "Los habitantes que hay por cada kilómetro cuadrado", "Se calcula dividiendo habitantes por superficie."),
        ("En Geografía: ¿qué es el crecimiento natural?", "La diferencia entre nacimientos y defunciones del año", "No incluye la migración."),
        ("=", "{F} ¿Cuál es la densidad de Mar, en habitantes por km²?", "40000/80", "Se dividen los habitantes por la superficie."),
        ("=", "{F} ¿Cuántas defunciones más que nacimientos tuvo Cerro?", "90-60", "Se resta la cifra menor a la mayor."),
        ("=", "{F} ¿Cuál es la migración neta de Roble?", "500-300", "Se restan las que salieron a las que llegaron."),
        ("{F} ¿Qué comuna perdió habitantes por migración? A) Roble, B) Cerro, C) Mar.", "B", "Salieron más personas de las que llegaron."),
        ("=", "{F} ¿Cuál es la tasa de natalidad de Cerro, en nacimientos por cada 1.000 habitantes? (Divide los nacimientos por los miles de habitantes: 6.000 habitantes son 6 miles.)", "60/6", "Se divide por los miles de habitantes."),
        ("=", "{F} ¿Cuál es el crecimiento natural de Mar?", "600-320", "Se restan las defunciones a los nacimientos."),
        ("{F} ¿Qué comuna tiene la menor densidad y qué significa?", "Cerro, con 20 habitantes por km², porque su población está más dispersa", "6.000 dividido en 300 da 20."),
        ("{F} Roble y Mar tienen la misma tasa de natalidad, de 15 por 1.000, aunque Mar tiene más nacimientos. ¿Por qué?", "Porque la tasa se calcula por cada 1.000 habitantes y Mar tiene más población", "La tasa relaciona nacimientos y población."),
        ("{F} Un compañero dice: «Cerro crece porque nacen niños». ¿Qué dato lo contradice?", "Que Cerro tuvo más defunciones que nacimientos y además salieron más personas de las que llegaron", "Su población disminuye por ambos motivos."),
        ("=", "{F} ¿Cuánto cambió la población de Mar en el año, sumando crecimiento natural y migración neta?", "(600-320)+(900-400)", "Se suman ambos componentes."),
        ("{F} Mar tiene la mayor densidad y crecimiento. ¿Qué podría necesitar? A) más cupos en colegios y consultorios, B) menos servicios, C) cerrar caminos.", "A", "Más población aumenta la demanda de servicios."),
    ],
    ctx=("Una alcaldesa de ejemplo debe decidir si construye un nuevo consultorio en Roble o en Cerro. Con la tabla, ¿qué comuna tiene más habitantes y, por lo tanto, mayor demanda de salud en términos absolutos?", "Roble, con 24.000 habitantes", "Tiene más personas que atender que Cerro."),
    sc=[("En Geografía: ¿qué es la migración neta?", "Las personas que llegan menos las que salen", "Indica si un lugar atrae o expulsa."),
        ("¿Qué mide la tasa de mortalidad?", "Las defunciones del año por cada 1.000 habitantes", "Relaciona defunciones y población."),
        ("¿Por qué conviene comparar con la misma unidad?", "Porque con unidades distintas no se pueden comparar", "Sin la misma unidad el número engaña.")],
    op=("{F} Elige dos comunas de la tabla y calcula para cada una la densidad y la migración neta. Escribe una frase que diga cuál atrae más población y qué necesitaría esa comuna.",
        "Elijo Roble y Mar. Densidad: Roble 200 y Mar 500. Migración neta: Roble +200 y Mar +500. Mar atrae más población y necesitaría más colegios, consultorios y transporte.",
        ["calcula las dos densidades", "calcula las migraciones netas", "relaciona con necesidades"], ["cálculos y una frase"], ["olvidar la unidad", "no relacionar con servicios"], "Pídele a una persona de tu casa que compruebe tus cálculos con calculadora."),
    reinforce="Cuenta cuántas personas viven en tu casa y calcula cuántas habría en 5 casas iguales.",
    extend="Calcula la tasa de mortalidad de Roble por cada 1.000 habitantes.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = ("Datos de ejemplo de la comuna Lomas (inventada). Año 1970: 8.000 habitantes, de los cuales el 70 % vivía en zonas rurales; 400 personas tenían 65 años o más. "
      "Año 2020: 12.000 habitantes, de los cuales el 30 % vivía en zonas rurales; 1.800 personas tenían 65 años o más.")
build(
    OA, 3, F3,
    use="Aprenderé a describir cómo cambian en el tiempo la migración campo-ciudad y la estructura de la población. Sirve para explicar por qué algunos territorios crecen y otros pierden habitantes.",
    prior=["Sé calcular densidad y migración neta.", "Sé distinguir cambio y continuidad.", "Sé calcular porcentajes sencillos."],
    explain=[
        "La migración interna es el traslado de personas dentro de un mismo país. Una forma muy frecuente es la migración del campo a la ciudad, también llamada éxodo rural. Muchas personas dejan zonas rurales para buscar trabajo, estudios o servicios que no hay cerca. Como resultado, las ciudades crecen, un proceso que se llama urbanización.",
        "Cuando muchas personas jóvenes emigran, el campo queda con menos habitantes y con mayor proporción de personas mayores. Esto se llama envejecimiento de la población. En las ciudades suele aumentar la demanda de vivienda, transporte, colegios y consultorios. Así, la migración cambia tanto el lugar de origen como el de destino.",
        "También existe la relación centro-periferia. El centro es el espacio que concentra servicios, empleo y decisiones, como una gran ciudad. La periferia es el espacio alejado del centro, con menor acceso a esos recursos. La migración suele ir de la periferia hacia el centro, y por eso aumenta la diferencia entre ambos. Algo continúa: el campo sigue produciendo alimentos, aunque tenga menos población.",
    ],
    vocab=[("migración interna", "traslado de personas dentro de un mismo país"), ("éxodo rural", "salida de personas del campo hacia la ciudad"), ("urbanización", "crecimiento de la población que vive en ciudades"), ("envejecimiento", "aumento de la proporción de personas mayores"), ("centro-periferia", "relación entre un espacio que concentra servicios y otro más alejado y con menos acceso")],
    worked=[
        ("Calcular población rural", "Una comuna de ejemplo tenía 5.000 habitantes y el 40 % vivía en zona rural. ¿Cuántas personas vivían en el campo?",
         ["Calculo el 40 % de 5.000.", "5.000 × 40 ÷ 100 = 2.000."], "2.000 personas"),
        ("Interpretar un cambio", "Si la proporción rural baja de 40 % a 20 %, ¿qué proceso se observa?",
         ["Hay menos proporción en el campo.", "Hay más población en la ciudad."], "Urbanización"),
    ],
    mistakes=[
        ("Creer que la migración campo-ciudad solo beneficia a las personas que migran.", "También cambia el campo, que pierde población joven, y la ciudad, que debe atender más gente.", "Revisa efectos en el origen y en el destino."),
        ("Pensar que si el campo pierde población ya no tiene actividad.", "Muchas actividades rurales continúan con menos gente.", "Separa lo que cambió de lo que continuó."),
    ],
    T=[
        ("En Geografía: ¿qué es el éxodo rural?", "La salida de personas del campo hacia la ciudad", "Es una migración interna."),
        ("En Geografía: ¿qué significa emigrar?", "Salir de un lugar para vivir en otro", "El que llega se llama inmigrante."),
        ("=", "{F} ¿Cuántas personas vivían en zonas rurales de Lomas en 1970?", "8000*70/100", "Se calcula el 70 % de 8.000."),
        ("=", "{F} ¿Cuántas personas vivían en zonas rurales de Lomas en 2020?", "12000*30/100", "Se calcula el 30 % de 12.000."),
        ("=", "{F} ¿Cuántas personas vivían en zonas urbanas de Lomas en 2020?", "12000-3600", "Se resta lo rural al total de 2020."),
        ("{F} ¿Qué cambió en la distribución rural-urbana de Lomas entre 1970 y 2020? A) pasó de predominar lo rural a predominar lo urbano, B) no cambió, C) desapareció la zona rural.", "A", "La proporción rural bajó de 70 % a 30 %."),
        ("=", "{F} ¿Cuánto aumentó entre 1970 y 2020 el número de personas de 65 años o más de Lomas?", "1800-400", "Se restan las cifras de ambos años."),
        ("{F} ¿Por qué puede envejecer el campo cuando los jóvenes se van?", "Porque quedan proporcionalmente más personas mayores", "Los jóvenes salen y los mayores se quedan."),
        ("¿Cuál es una causa que atrae a las personas a la ciudad? A) oportunidades de trabajo y servicios, B) mucha nieve, C) pocas escuelas.", "A", "Es un factor de atracción."),
        ("{F} Un compañero dice que en 2020 casi toda la población de Lomas vive en el campo. ¿Qué dato lo contradice?", "Que solo 3.600 de 12.000 personas (30 %) viven en zonas rurales", "En 2020 la mayoría de la población vive en zonas urbanas."),
        ("En un país de ejemplo, la capital reúne hospitales, universidades y sedes de empresas, y un pueblo lejano tiene solo una posta. ¿Quién es centro y quién periferia?", "La capital es el centro; el pueblo lejano, la periferia", "El centro concentra servicios."),
        ("{F} Si en 2020 aún viven 3.600 personas en zona rural, ¿qué continuidad muestra?", "Que siguen existiendo vida y actividad rural", "El campo no desapareció."),
        ("Evalúa la frase «La migración campo-ciudad solo trae beneficios». A) Es inexacta: también deja al campo con menos población joven y a la ciudad con más demanda de servicios; B) Es correcta; C) No tiene relación con la población.", "A", "Tiene beneficios y costos."),
    ],
    ctx=("Una joven de una localidad rural piensa emigrar a la ciudad para estudiar una carrera que no se imparte cerca. ¿Es esa decisión puramente individual, o también influyen las condiciones del lugar? Responde con una frase.", "También influyen las condiciones del lugar, porque no hay esa carrera ni oferta de estudios cerca", "Las decisiones ocurren dentro de condiciones."),
    sc=[("En Geografía: ¿qué es la urbanización?", "El crecimiento de la población que vive en ciudades", "Suele aumentar con la migración campo-ciudad."),
        ("¿Qué es la periferia?", "Un espacio alejado del centro y con menos acceso a servicios", "Se define por relación con el centro."),
        ("Nombra un efecto de la migración en el campo.", "Por ejemplo: pierde población joven", "Es un efecto de origen.")],
    op=("{F} Escribe un párrafo de cuatro líneas que explique qué cambió en Lomas entre 1970 y 2020. Incluye: un dato de población rural, un dato de personas mayores, un efecto en la ciudad y una continuidad.",
        "En 1970 había 5.600 personas en el campo y en 2020, 3.600. Las personas de 65 años o más pasaron de 400 a 1.800. En la zona urbana aumentó la demanda de colegios y consultorios. Continúa la actividad agrícola, aunque con menos gente.",
        ["usa un dato rural", "usa un dato de personas mayores", "menciona un efecto urbano", "señala una continuidad"], ["cuatro frases"], ["olvidar la continuidad", "no usar cifras"], "Lee tu párrafo a una persona de tu casa y pídele que revise tus cifras."),
    reinforce="Pregunta a una persona de tu familia si alguien migró de un lugar a otro y anota por qué.",
    extend="Calcula qué porcentaje de la población de Lomas tenía 65 años o más en 2020.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = ("Testimonios de ejemplo escritos para este ejercicio. "
      "Camila, 18 años, localidad rural: «Me voy a la ciudad a estudiar; en mi pueblo no hay carreras técnicas ni trabajo para jóvenes.» "
      "Don Hugo, agricultor: «Me quedo, porque mi tierra es mi trabajo; pero cada año hay menos vecinos y cerraron la escuela.» "
      "Alcalde de la ciudad que recibe migrantes: «Llegan familias y faltan cupos en colegios y consultorios.» "
      "Alcaldesa de la comuna rural: «Perdemos jóvenes y cada año quedan menos personas para sostener los servicios.»")
build(
    OA, 4, F4,
    use="Aprenderé a contrastar las causas y las perspectivas de quienes migran o quedan aislados, sin reducir todo a una decisión individual. Sirve para comprender por qué se mueve la gente.",
    prior=["Sé qué es la migración interna y el éxodo rural.", "Sé calcular migración neta.", "Sé distinguir una causa de una consecuencia."],
    explain=[
        "Las causas de la migración se clasifican en factores de expulsión y de atracción. Los factores de expulsión empujan a salir de un lugar, como la falta de trabajo, de estudios o de servicios. Los factores de atracción son los que hacen atractivo el destino, como empleo, universidades o mejores servicios. Casi siempre actúan juntos.",
        "La decisión de migrar es personal, pero se toma dentro de condiciones: redes de transporte, oportunidades de empleo, precios de la vivienda y servicios disponibles. Por eso no basta con decir «se fue porque quiso». Los actores son varios: las personas que migran, las que se quedan, los gobiernos locales de origen y de destino, las empresas y el Estado.",
        "Cada actor tiene una perspectiva. Una joven ve oportunidades en la ciudad; un agricultor ve su tierra y el cierre de servicios; un alcalde de destino ve presión sobre colegios y consultorios; una alcaldesa de origen ve pérdida de población. También existe la migración internacional, cuando personas cruzan fronteras para vivir en otro país. Contrastar perspectivas permite comprender el problema completo.",
    ],
    vocab=[("factor de expulsión", "condición que empuja a las personas a salir de un lugar"), ("factor de atracción", "condición que hace atractivo un lugar de destino"), ("migración internacional", "traslado de personas de un país a otro"), ("presión sobre los servicios", "aumento de la demanda por encima de lo que pueden atender"), ("perspectiva", "punto de vista según la posición de quien habla")],
    worked=[
        ("Clasificar un factor", "Camila dice que en su pueblo no hay carreras técnicas. ¿Es factor de expulsión o de atracción?",
         ["Es una carencia del lugar de origen.", "Empuja a salir."], "Factor de expulsión"),
        ("Contrastar perspectivas", "¿Qué preocupa al alcalde de destino y qué a la alcaldesa de origen?",
         ["Al alcalde de destino le faltan cupos en colegios y consultorios.", "A la alcaldesa de origen le preocupa perder jóvenes y servicios."], "Presión sobre servicios en el destino; pérdida de población en el origen"),
    ],
    mistakes=[
        ("Explicar la migración solo como una elección individual.", "Las condiciones del lugar también empujan o atraen.", "Pregunta qué factores de expulsión y de atracción hay."),
        ("Creer que todos los actores quieren lo mismo.", "Cada uno ve el problema desde su posición.", "Pregunta qué teme o espera cada actor."),
    ],
    T=[
        ("En Geografía: ¿qué es un factor de expulsión?", "Una condición que empuja a las personas a salir de un lugar", "Es una carencia o problema del origen."),
        ("En Geografía: ¿qué es un factor de atracción?", "Una condición que hace atractivo un lugar de destino", "Es una oportunidad del destino."),
        ("{F} ¿Qué actor dice que quedan menos personas para sostener los servicios?", "La alcaldesa de la comuna rural", "Habla de pérdida de población."),
        ("{F} ¿Qué factor de atracción busca Camila en la ciudad? A) estudios y trabajo, B) más nieve, C) menos servicios.", "A", "Dice que se va a estudiar."),
        ("{F} ¿Qué dos cambios de su pueblo menciona don Hugo?", "Que cada año hay menos vecinos y que cerraron la escuela", "Don Hugo describe pérdida de población y de servicios."),
        ("{F} ¿Qué problema enfrenta el alcalde de la ciudad receptora?", "Faltan cupos en colegios y consultorios", "Aumentó la demanda de servicios."),
        ("=", "En la ciudad receptora de ejemplo llegan 270 niños y cada sala atiende a 30 estudiantes. ¿Cuántas salas nuevas se necesitan?", "270/30", "Se divide el número de niños por la capacidad de cada sala."),
        ("=", "Una localidad rural de ejemplo tenía 850 habitantes y en un año emigraron 120 y nacieron 40. ¿Cuántos quedan?", "850-120+40", "Se resta lo que salió y se suma lo que nació."),
        ("{F} Don Hugo decide quedarse. ¿Qué muestra eso sobre la migración? A) que no todos emigran, aunque haya factores de expulsión, B) que nadie se va, C) que no existen condiciones.", "A", "Las personas responden de forma distinta."),
        ("{F} ¿Qué diferencia hay entre la perspectiva de Camila y la de la alcaldesa rural?", "Camila ve una oportunidad al irse; la alcaldesa ve pérdida de población y servicios", "Cada una habla desde su posición."),
        ("Explica por qué decir «migró porque quiso» es una explicación incompleta.", "Porque no considera las condiciones del lugar, como la falta de trabajo o de estudios", "Las decisiones ocurren dentro de condiciones."),
        ("Una familia cruza la frontera para trabajar en otro país. ¿Qué tipo de migración es y cómo se llama la persona que llega al país de destino?", "Migración internacional; inmigrante", "Cruza fronteras entre países."),
        ("{F} Propón un factor de atracción y uno de expulsión a partir de los testimonios.", "Atracción: estudios y trabajo en la ciudad; expulsión: falta de carreras y de trabajo en el pueblo", "Se obtienen de Camila."),
    ],
    ctx=("En una reunión vecinal en el pueblo de Camila, alguien dice: «Los jóvenes se van porque no quieren trabajar». {F} Con los testimonios, ¿qué respondes?", "Que Camila se va porque no hay carreras técnicas ni trabajo para jóvenes en su pueblo", "El testimonio muestra una causa de expulsión."),
    sc=[("En Geografía: ¿qué es la migración internacional?", "El traslado de personas de un país a otro", "Implica cruzar fronteras entre países."),
        ("¿Por qué conviene conocer varias perspectivas?", "Porque cada actor ve el problema desde su posición", "Así se entiende el problema completo."),
        ("Nombra un factor de atracción.", "Por ejemplo: empleo o estudios en el destino", "Hace atractivo el lugar.")],
    op=("{F} Elige dos testimonios y compáralos: qué espera o teme cada uno, un factor de expulsión o de atracción presente y una acción que podría ayudar a ambos.",
        "Comparo a Camila y a la alcaldesa rural. Camila espera estudiar y trabajar; la alcaldesa teme perder población. Factor de expulsión: falta de carreras. Una acción: crear una sede de estudios técnicos en la zona rural, para que jóvenes no deban irse.",
        ["compara dos testimonios", "identifica un factor", "propone una acción coherente"], ["tres partes claras"], ["culpar a una persona", "proponer algo que no responde al factor"], "Explícale tu comparación a una persona de tu casa y pídele otra acción posible."),
    reinforce="Pregunta a una persona mayor por qué su familia migró o decidió quedarse.",
    extend="Escribe qué factor de atracción podría crear un pueblo rural para retener a sus jóvenes.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = ("Caso de ejemplo, comuna Piedra Azul (inventada). Está a 60 km de la capital regional por un camino de ripio. Datos de ejemplo: un médico la visita cada 15 días; "
      "el desempleo juvenil es de 24 %, frente a 8 % en la capital regional; en 2010 vivían 3.000 personas y en 2020, 2.400; "
      "la mayoría de los empleos es en pesca artesanal y turismo de verano; el camino se cierra algunos días de invierno por lluvias.")
build(
    OA, 5, F5,
    use="Aprenderé a evaluar con evidencia cómo el aislamiento y la migración afectan el empleo, la salud y la relación campo-ciudad. Sirve para argumentar sobre desigualdades regionales.",
    prior=["Sé qué son conectividad, aislamiento y migración.", "Sé usar índices demográficos.", "Sé armar un argumento con afirmación, evidencia y explicación."],
    explain=[
        "Evaluar un problema regional es juzgar su gravedad con datos. Los ámbitos que se analizan son el mercado laboral (qué empleos hay y cuánto desempleo), los servicios de salud (cuán frecuentes y cercanos son), la relación campo-ciudad (qué intercambian y quién depende de quién) y la relación centro-periferia (cómo se reparten servicios y decisiones).",
        "Mi argumento tiene tres partes. La afirmación responde la pregunta, como «el aislamiento afecta el acceso a salud». La evidencia son datos, como la frecuencia de visitas médicas. La explicación conecta los datos con la afirmación. Además considero otras causas, porque no todo se debe al aislamiento: también influyen la economía y la edad de la población.",
        "Cuido tres cosas. Primero, no generalizo a toda una región a partir de una sola comuna. Segundo, distingo correlación de causa: que dos datos aparezcan juntos no prueba que uno cause el otro. Tercero, uso cifras con su unidad y con un año de referencia. Los datos del caso son de ejemplo.",
    ],
    vocab=[("mercado laboral", "conjunto de empleos disponibles y personas que buscan trabajo"), ("desempleo", "situación de quienes buscan trabajo y no lo encuentran"), ("relación campo-ciudad", "intercambio y dependencia entre zonas rurales y urbanas"), ("correlación", "coincidencia entre dos datos que no prueba por sí sola una causa"), ("generalizar", "extender una conclusión a más casos de los que muestra la evidencia")],
    worked=[
        ("Elegir evidencia", "{F} Quieres afirmar que Piedra Azul tiene menor acceso a salud. ¿Qué dato del caso usas?",
         ["Busco un dato sobre servicios de salud.", "Un médico la visita cada 15 días."], "Un médico la visita cada 15 días"),
        ("Evitar generalizar", "{F} Con el caso de Piedra Azul, un estudiante afirma que «todas las comunas rurales de Chile tienen 24 % de desempleo juvenil». ¿Qué falla?",
         ["Generaliza desde una sola comuna.", "Además los datos son de ejemplo."], "Que generaliza a todas las comunas con un solo caso"),
    ],
    mistakes=[
        ("Atribuir todo el problema al aislamiento.", "Pueden influir la economía y la edad de la población.", "Considera otras causas antes de concluir."),
        ("Concluir que dos datos juntos prueban una causa.", "Es una correlación, no una causa demostrada.", "Pregunta si hay otras explicaciones."),
    ],
    T=[
        ("En Geografía: ¿qué es el mercado laboral?", "El conjunto de empleos disponibles y de personas que buscan trabajo", "Incluye ofertas y demanda de empleo."),
        ("{F} ¿Con qué frecuencia visita un médico a Piedra Azul?", "Cada 15 días", "Lo dice el caso."),
        ("{F} ¿Qué ámbito se afecta por el cierre del camino en invierno? A) acceso a servicios y a bienes, B) el color del mar, C) la fiesta de verano.", "A", "El corte limita llegar y recibir lo necesario."),
        ("=", "{F} ¿Cuántos habitantes perdió Piedra Azul entre 2010 y 2020?", "3000-2400", "Se restan las poblaciones de ambos años."),
        ("=", "{F} ¿Cuántos puntos más alto es el desempleo juvenil de Piedra Azul (24 %) que el de la capital regional (8 %)?", "24-8", "Se restan los porcentajes."),
        ("=", "{F} Si un médico visita cada 15 días, ¿cuántas visitas hace en 60 días?", "60/15", "Se divide el tiempo total por el intervalo."),
        ("{F} ¿Qué dato apoya la afirmación «hay desigualdad centro-periferia en empleo»? A) 24 % de desempleo juvenil frente a 8 % en la capital regional, B) camino de ripio, C) pesca artesanal.", "A", "Compara la periferia con el centro."),
        ("{F} Un estudiante afirma que el aislamiento es la única causa de la pérdida de habitantes. ¿Qué otra causa podría influir según el caso?", "El desempleo juvenil alto y la economía de pesca y turismo de verano", "Hay otros factores económicos."),
        ("{F} Explica con una frase por qué no puedes concluir que las comunas aisladas tienen siempre menos médicos.", "Porque solo es un caso y no basta para generalizar", "Un caso no representa a todas."),
        ("{F} Se dice: «Como la población bajó y hay desempleo, el desempleo causó la baja». ¿Qué falta? A) comprobar otras causas, porque dos datos juntos no prueban una causa, B) nada, C) más años.", "A", "Es correlación, no causa."),
        ("{F} ¿Qué relación campo-ciudad muestra el caso?", "Piedra Azul depende de la capital regional para recibir servicios, como la visita del médico", "Hay dependencia del centro."),
        ("Completa el argumento: «El aislamiento limita el acceso a salud porque ___ (dato) y esto ___ (explicación)».", "El médico la visita cada 15 días; eso significa que las urgencias no pueden atenderse a tiempo", "Une dato y consecuencia."),
        ("{F} Escribe una afirmación matizada sobre Piedra Azul que reconozca otras causas, además del aislamiento.", "El aislamiento influye en el acceso a salud y empleo, pero también pesa una economía basada en pocas actividades", "Reconoce más de una causa."),
    ],
    ctx=("Un periodista de ejemplo escribe: «Todas las comunas aisladas del país pierden población por su culpa». Con el caso de Piedra Azul, ¿qué dos reparos científicos le pondrías?", "Que generaliza desde un solo caso y que atribuye la causa al aislamiento sin considerar otras", "Falla en generalización y en causalidad."),
    sc=[("En Geografía: ¿qué es una correlación?", "Una coincidencia entre dos datos que no prueba por sí sola una causa", "Hay que revisar otras explicaciones."),
        ("¿Qué es generalizar?", "Extender una conclusión a más casos de los que muestra la evidencia", "Con un solo caso no se puede hacerlo."),
        ("Nombra un ámbito afectado por el aislamiento.", "Por ejemplo: la salud o el empleo", "Dependen de la conectividad.")],
    op=("{F} Redacta un argumento de cuatro partes sobre Piedra Azul: tu afirmación (cómo afecta el aislamiento), dos datos del caso, una explicación y una advertencia sobre un límite de la evidencia.",
        "El aislamiento limita el acceso a salud y a empleo. Datos: un médico visita cada 15 días y el desempleo juvenil es de 24 %. Explicación: sin conexión fácil a la capital regional hay menos atención y menos oportunidades. Límite: es un solo caso de ejemplo, no se puede generalizar.",
        ["afirmación clara", "dos datos del caso", "explicación", "límite de la evidencia"], ["cuatro partes completas"], ["generalizar", "olvidar una explicación"], "Pide a una persona de tu casa que busque el punto más débil de tu argumento."),
    reinforce="Anota un servicio que tu comuna tenga y otro que falte, y por qué crees que pasa.",
    extend="Escribe qué dato adicional pedirías para saber si el aislamiento causa el desempleo.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 6
F6 = ("Propuestas de ejemplo para Piedra Azul (costos y plazos inventados). A) Pavimentar los 60 km de camino: 6.000 millones de pesos y 3 años de obra. "
      "B) Internet de buena calidad en la escuela y la posta: 200 millones y 6 meses. "
      "C) Ronda médica cada semana: 120 millones al año. "
      "D) Becas para jóvenes que estudian fuera y vuelven a trabajar a la comuna: 150 millones al año.")
build(
    OA, 6, F6,
    use="Aprenderé a evaluar propuestas para reducir el aislamiento y las desigualdades regionales, considerando costos, plazos y límites. Sirve para tomar decisiones informadas sobre el territorio.",
    prior=["Sé analizar conectividad, migración e índices demográficos.", "Sé armar un argumento con evidencia.", "Sé hacer cálculos simples con costos."],
    explain=[
        "Evaluar una propuesta es juzgar si sirve para resolver un problema. Se pueden usar cuatro criterios: el alcance (a cuántas personas ayuda), el costo (cuánto dinero cuesta), el plazo (cuánto demora en dar resultados) y los riesgos o límites (qué podría salir mal o qué no resuelve). Una propuesta barata puede tener poco alcance, y una de gran alcance puede ser lenta o muy costosa.",
        "Hay medidas de conectividad física, como pavimentar un camino; de conectividad digital, como mejorar el internet; de servicios, como rondas médicas; y de incentivos, como becas para que los jóvenes vuelvan. Ninguna resuelve todo por sí sola. Por eso conviene combinarlas. También hay que cuidar el medio: una obra grande puede afectar el paisaje y los ecosistemas.",
        "Finalmente, proyecto qué pasaría con cada medida y reconozco los límites de mi juicio. No sé cuánto cambiarían las decisiones de migración, y los datos de costos son de ejemplo. Una buena evaluación no promete soluciones perfectas: explica ventajas, límites y qué más habría que averiguar.",
    ],
    vocab=[("alcance", "cantidad de personas a las que una medida ayuda"), ("plazo", "tiempo que demora una medida en dar resultados"), ("incentivo", "estímulo para que las personas tomen una decisión"), ("descentralización", "traslado de decisiones y recursos desde el centro hacia las regiones"), ("proyección", "idea de lo que podría ocurrir en el futuro")],
    worked=[
        ("Comparar plazos", "{F} Con la ficha, ¿qué propuesta da resultados más rápido, la A o la B?",
         ["La A demora 3 años.", "La B demora 6 meses."], "La B es más rápida"),
        ("Evaluar un límite", "{F} La propuesta B mejora internet. ¿Qué no resuelve?",
         ["Mejora comunicaciones e información.", "No cambia que el camino se cierre por lluvia."], "No resuelve el corte del camino"),
    ],
    mistakes=[
        ("Elegir la medida más barata sin mirar su alcance.", "Puede ayudar a muy pocas personas.", "Compara costo con alcance y plazo."),
        ("Creer que una sola medida resuelve todo el aislamiento.", "Cada medida resuelve una parte.", "Considera combinar medidas."),
    ],
    T=[
        ("En Geografía: ¿qué es el alcance de una medida?", "La cantidad de personas a las que ayuda", "Es un criterio de evaluación."),
        ("{F} ¿Cuántos años demora la obra de la propuesta A?", "3 años", "La ficha lo indica."),
        ("{F} ¿Cuál propuesta cuesta menos en el primer año? A) la A, B) la B, C) la C.", "C", "Cuesta 120 millones, menos que 200 y 6.000."),
        ("=", "{F} ¿Cuánto cuestan en total las propuestas C y D en un año?", "120+150", "Se suman los costos anuales."),
        ("=", "{F} ¿Cuánto costaría la propuesta C durante 3 años?", "120*3", "Se multiplica el costo anual por los años."),
        ("=", "{F} ¿Cuántos millones más cuesta pavimentar el camino que instalar internet?", "6000-200", "Se resta el costo menor al mayor."),
        ("{F} ¿Qué propuesta mejora el acceso a información sin cambiar el transporte? A) la B, B) la D, C) la A.", "A", "Mejora internet en la escuela y la posta."),
        ("{F} ¿Qué límite tiene la propuesta C? A) no resuelve el desempleo juvenil, B) no cuesta nada, C) elimina el camino.", "A", "Atiende salud, pero no empleo."),
        ("{F} ¿Cuál propuesta busca retener jóvenes en la comuna y cómo?", "La D, con becas para que vuelvan a trabajar", "Es un incentivo."),
        ("{F} Un vecino dice: «Con pavimentar el camino se resuelve todo». ¿Qué respondes?", "Que no basta: también se necesitan servicios, internet y empleo, y la obra es cara y lenta", "Una medida resuelve una parte."),
        ("Explica por qué conviene combinar medidas para reducir el aislamiento.", "Porque cada una resuelve un aspecto distinto, como transporte, comunicaciones o servicios", "Ninguna cubre todo."),
        ("Evalúa la frase «La mejor propuesta es siempre la más cara». ¿Qué falla?", "Que el costo no mide por sí solo el alcance ni la utilidad", "Hay que ver costo, alcance y plazo."),
        ("{F} ¿Qué dos propuestas combinadas mejoran el acceso a salud en pocos meses y a bajo costo?", "B y C, porque internet en la posta y la ronda médica semanal dan resultados rápidos y cuestan poco", "Combina medidas rápidas y baratas; la A tarda 3 años y la D no mejora la salud directamente."),
    ],
    ctx=("El concejo de la comuna debe elegir una sola propuesta con un presupuesto de 300 millones. {F} ¿Qué dos de las propuestas B, C y D caben juntas en ese monto si se paga solo el primer año?", "C y D, que suman 270 millones", "B con C suman 320 y B con D, 350; solo C con D no se pasan."),
    sc=[("En Geografía: ¿qué es un incentivo?", "Un estímulo para que las personas tomen una decisión", "Por ejemplo, una beca."),
        ("¿Qué es la descentralización?", "El traslado de decisiones y recursos desde el centro hacia las regiones", "Busca reducir la distancia con el centro."),
        ("Nombra un criterio para evaluar una propuesta.", "Por ejemplo: costo, plazo, alcance o riesgo", "Permiten comparar medidas.")],
    op=("{F} Elige dos propuestas y evalúalas con cuatro criterios: alcance, costo, plazo y límite. Termina con una recomendación breve y una pregunta que te falte responder.",
        "Evalúo B y C. B: ayuda a escuela y posta, cuesta 200 millones, demora 6 meses y no resuelve el corte del camino. C: ayuda a la salud, cuesta 120 millones al año, es inmediata y no mejora el empleo. Recomiendo ambas. Me falta saber cuántas personas usan la posta.",
        ["usa los cuatro criterios", "compara dos propuestas", "da una recomendación", "formula una pregunta"], ["evaluación y recomendación breves"], ["recomendar sin criterios", "olvidar los límites"], "Pide a una persona de tu casa que elija una propuesta y compara su razón con la tuya."),
    reinforce="Anota una mejora que le harías a tu barrio y quién se beneficiaría.",
    extend="Escribe cómo cambiaría tu recomendación si el presupuesto fuera de 100 millones.",
    materials=MAT,
)
