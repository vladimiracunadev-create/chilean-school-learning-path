"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 25 (industrialización, ambiente y desarrollo sostenible)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 25"
MAT = "Lápiz y papel. Las series, los textos y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = ("Serie de ejemplo de una ciudad industrial ficticia. Fábricas: 10 en 1800, 60 en 1850 y 200 en 1900. "
      "Carbón quemado por año: 5.000 toneladas en 1800, 60.000 en 1850 y 400.000 en 1900. "
      "Días al año con humo denso sobre la ciudad: 20 en 1800, 90 en 1850 y 200 en 1900.")
build(
    OA, 1, F1,
    use="Aprenderé a situar la industrialización en el tiempo y a plantear el problema de cómo afectó al ambiente. Sirve para entender por qué hoy se debate el desarrollo sostenible.",
    prior=["Sé qué fue la industrialización y la urbanización.", "Sé leer una serie de datos por años.", "Sé calcular cuántas veces es mayor un número que otro."],
    explain=[
        "La industrialización fue el paso de una producción hecha a mano en talleres a una producción hecha con máquinas en fábricas. Comenzó en Gran Bretaña en el siglo XVIII y se extendió por Europa, América y otras regiones durante el XIX. Usó mucho carbón como fuente de energía, que es un combustible fósil, es decir, un combustible formado hace millones de años a partir de restos de seres vivos, como el carbón, el petróleo y el gas.",
        "Esa forma de producir trajo progreso material, empleo y nuevos productos, pero también tuvo un costo para el ambiente. La quema de carbón liberó humo y gases a la atmósfera; las fábricas vertieron residuos a los ríos; la extracción de minerales y la tala de bosques transformaron paisajes. Estos efectos se llaman contaminación cuando introducen sustancias que dañan el aire, el agua o el suelo.",
        "El problema que estudiaremos es cómo el crecimiento de la producción se relacionó con el daño ambiental, en el pasado y en el presente. Hoy se discute cómo lograr un desarrollo sostenible, que significa satisfacer las necesidades de las personas actuales sin comprometer la posibilidad de las generaciones futuras de satisfacer las suyas. Para estudiarlo se ubican los hechos en el tiempo y se revisan datos.",
    ],
    vocab=[("industrialización", "paso de una producción hecha a mano a una producción con máquinas en fábricas"), ("combustible fósil", "combustible formado hace millones de años, como el carbón, el petróleo y el gas"), ("contaminación", "presencia de sustancias que dañan el aire, el agua o el suelo"), ("desarrollo sostenible", "desarrollo que satisface las necesidades actuales sin comprometer las de las generaciones futuras"), ("generación futura", "personas que vivirán después de las actuales")],
    worked=[
        ("Calcular cuántas veces creció algo", "Una ciudad de ejemplo tenía 4 fábricas en 1820 y 40 en 1880. ¿Cuántas veces mayor fue el número de fábricas?",
         ["Divido 40 entre 4.", "40 ÷ 4 = 10."], "10 veces mayor"),
        ("Relacionar dos series", "En esa ciudad de ejemplo, la quema de carbón pasó de 2.000 a 100.000 toneladas y los días con humo, de 10 a 150. ¿Qué relación sugieren los datos?",
         ["Ambas series suben en el mismo período.", "Sugieren que más carbón quemado coincide con más días de humo."], "Que más quema de carbón coincide con más humo"),
    ],
    mistakes=[
        ("Creer que la industrialización solo trajo progreso o solo trajo daño.", "Tuvo beneficios materiales y también costos ambientales y sociales.", "Registra ventajas y costos con datos."),
        ("Pensar que contaminar es un problema solo de hoy.", "Ya en el siglo XIX había humo, residuos en ríos y cambios en el paisaje.", "Busca evidencias del pasado y compáralas con el presente."),
    ],
    T=[
        ("En Historia: ¿qué es un combustible fósil?", "Un combustible formado hace millones de años a partir de restos de seres vivos, como el carbón", "Es la energía que más se usó en la industrialización."),
        ("{F} ¿Cuántas fábricas había en la ciudad en 1850?", "60", "La serie lo informa."),
        ("En Historia: ¿qué es la contaminación? A) la presencia de sustancias que dañan el aire, el agua o el suelo, B) el aumento de empleos.", "A", "Es el daño a los elementos del ambiente."),
        ("=", "{F} ¿Cuántas fábricas más había en 1900 que en 1800?", "200-10", "Se resta el número inicial al final."),
        ("=", "{F} ¿Cuántas veces mayor fue el carbón quemado en 1900 que en 1800?", "400000//5000", "Se divide la cantidad final entre la inicial."),
        ("{F} ¿Qué serie de la ciudad mide un efecto en la calidad del aire? A) los días con humo denso, B) el número de fábricas.", "A", "El humo afecta el aire."),
        ("=", "{F} ¿Cuántos días más con humo hubo en 1900 que en 1850?", "200-90", "Se resta el valor de 1850 al de 1900."),
        ("=", "{F} Si en 1850 el humo ocurría 90 días de un año que, para simplificar, tiene 360 días, ¿qué porcentaje del año fue?", "90*100//360", "Se divide los días de humo entre los días del año y se multiplica por 100.", "%"),
        ("{F} ¿Qué conclusión sostiene mejor la serie? A) al crecer las fábricas y el carbón quemado, aumentaron los días con humo, B) el humo bajó con más fábricas.", "A", "Las tres series suben juntas."),
        ("{F} Un compañero dice: «Los datos prueban que el carbón es la única causa del humo». ¿Qué respuesta es mejor? A) los datos muestran una relación, pero podrían influir otros factores, B) es correcto.", "A", "Una coincidencia no prueba una causa única."),
        ("Un texto de ejemplo dice: «Con la industria, la ciudad prosperó y a la vez se ensució el aire». ¿Qué dos aspectos reconoce? A) beneficio económico y costo ambiental, B) solo daño ambiental.", "A", "Reconoce progreso y daño."),
        ("=", "{F} ¿Cuántas toneladas más de carbón se quemaron entre 1850 y 1900?", "400000-60000", "Se resta la cantidad de 1850 a la de 1900."),
        ("En Historia: una medida satisface las necesidades de hoy pero agota un recurso que necesitarán los jóvenes del futuro. ¿Es sostenible? A) no, porque compromete a las generaciones futuras, B) sí, porque ayuda ahora.", "A", "Esa es la definición de desarrollo sostenible."),
    ],
    ctx=("Un colegio de ejemplo estudia su ciudad: en 1900 había 200 fábricas y hoy hay 40, pero aún se queman combustibles fósiles. ¿Qué pregunta ayuda a plantear el problema de la clase? A) ¿cómo se relaciona el crecimiento de la producción con el daño ambiental?, B) ¿cuántas personas trabajaban en cada fábrica?", "A", "Es la pregunta central del tema."),
    sc=[("En Historia: ¿qué es el desarrollo sostenible?", "Un desarrollo que satisface las necesidades actuales sin comprometer las de las generaciones futuras", "Considera el presente y el futuro."),
        ("Nombra dos combustibles fósiles.", "Por ejemplo: el carbón y el petróleo", "Son los combustibles fósiles más conocidos."),
        ("¿Qué fue la industrialización?", "El paso de una producción hecha a mano a una producción con máquinas en fábricas", "Cambió la forma de producir.")],
    op=("{F} Escribe un texto corto que diga: cuántas veces creció el número de fábricas entre 1800 y 1900, cuántas veces creció el carbón quemado, qué pasó con los días de humo y una pregunta que te gustaría responder sobre el ambiente en ese tiempo.",
        "Las fábricas pasaron de 10 a 200, 20 veces más. El carbón quemado pasó de 5.000 a 400.000 toneladas, 80 veces más. Los días con humo subieron de 20 a 200. Pregunta: ¿qué efectos tuvo el humo en la salud de la población?",
        ["calcula cuántas veces crecen dos series", "describe los días de humo", "formula una pregunta"], ["un texto con tres datos y una pregunta"], ["decir que el carbón es la única causa", "no usar cifras"], "Pide a una persona de tu casa que compruebe tus divisiones."),
    reinforce="Haz una tabla de tres columnas con año, fábricas y días de humo.",
    extend="Explica con tus palabras por qué un progreso material puede tener costos ambientales.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = ("Fuente A (de ejemplo, informe de un instituto de estadísticas ficticio): en la ciudad, las muertes por enfermedades respiratorias fueron 120 en 1850 y 480 en 1900. "
      "Fuente B (de ejemplo, carta de un médico ficticio, 1890): «El humo de las fábricas enferma a los niños del barrio cercano; propongo alejarlas de las casas.» "
      "Fuente C (de ejemplo, discurso de un empresario ficticio, 1890): «El humo de las chimeneas es señal de progreso y trabajo.» "
      "Fuente D (de ejemplo, informe actual de una autoridad ambiental ficticia): la ciudad registró 25 días al año con alerta por mala calidad del aire.")
build(
    OA, 2, F2,
    use="Aprenderé a seleccionar y contextualizar fuentes sobre el impacto ambiental de la industria. Sirve para distinguir datos de opiniones y ver qué perspectiva muestra cada fuente.",
    prior=["Sé qué es una fuente primaria y una secundaria.", "Sé distinguir dato y opinión.", "Conozco la industrialización y la contaminación."],
    explain=[
        "Para saber cómo afectó la industrialización al ambiente se usan fuentes de distinto tipo. Una serie estadística entrega datos que se pueden comparar en el tiempo. Una carta de un médico entrega un testimonio de alguien que observó los efectos en la salud. Un discurso de un empresario muestra la mirada de quien se beneficiaba de las fábricas. Un informe actual de una autoridad entrega datos recientes. Cada una tiene un propósito distinto.",
        "Contextualizar una fuente significa preguntar quién la escribió, cuándo, dónde y para qué. El médico escribe para proponer una medida; el empresario defiende su actividad; el instituto de estadísticas informa. Ninguna es neutral por completo, pero algunas ofrecen datos comprobables y otras, opiniones. Una buena selección combina datos con testimonios y busca voces distintas.",
        "Es importante reconocer los límites. Una serie de muertes por enfermedades respiratorias muestra un aumento, pero no prueba por sí sola que la causa sea el humo, porque pudieron influir otros factores como la población o la pobreza. Por eso se contrastan varias fuentes antes de sacar una conclusión.",
    ],
    vocab=[("serie estadística", "conjunto de datos medidos en distintos años para compararlos"), ("testimonio", "relato de una persona sobre lo que observó o vivió"), ("propósito", "intención con que se escribió una fuente"), ("neutral", "que no toma partido por ninguna posición"), ("enfermedad respiratoria", "enfermedad que afecta a los pulmones o las vías por donde pasa el aire")],
    worked=[
        ("Clasificar una fuente", "Un informe de un instituto de estadísticas muestra cuántas personas enfermaron cada año. ¿Qué tipo de fuente es y qué entrega?",
         ["Presenta cifras ordenadas por año.", "Es una serie estadística que entrega datos comparables."], "Serie estadística; entrega datos comparables"),
        ("Distinguir dato y opinión", "Dos frases de ejemplo: (1) «En 1890 hubo 120 días de humo». (2) «El humo es bello». ¿Cuál es un dato?",
         ["Un dato se puede comprobar con una cifra.", "La frase (1) tiene una cifra; la (2) expresa un gusto."], "La frase (1)"),
    ],
    mistakes=[
        ("Tomar la opinión de un empresario como si fuera un dato científico.", "Expresa su interés y no mide nada.", "Pide datos que la apoyen o la contradigan."),
        ("Creer que una serie estadística prueba una causa.", "Muestra una evolución, pero otros factores pudieron influir.", "Contrasta con otras fuentes antes de afirmar una causa."),
    ],
    T=[
        ("En Historia: ¿qué es una serie estadística?", "Un conjunto de datos medidos en distintos años para compararlos", "Permite ver cambios en el tiempo."),
        ("{F} ¿Cuántas muertes por enfermedades respiratorias hubo en 1900?", "480", "La fuente A lo informa."),
        ("{F} ¿Qué fuente es un testimonio de alguien que observó los efectos en la salud? A) la fuente B, B) la fuente C.", "A", "Es una carta de un médico."),
        ("{F} ¿Qué fuente expresa una opinión sobre el humo como señal de progreso? A) la fuente C, B) la fuente D.", "A", "Es un discurso del empresario."),
        ("{F} ¿Qué fuente es la más reciente? A) la fuente D, B) la fuente A.", "A", "Es un informe actual."),
        ("=", "{F} ¿Cuántas muertes más hubo en 1900 que en 1850?", "480-120", "Se resta el dato de 1850 al de 1900."),
        ("=", "{F} ¿Cuántas veces mayor fue la cifra de 1900 respecto de 1850?", "480//120", "Se divide la cifra final entre la inicial."),
        ("{F} ¿Con qué propósito escribe el médico de la fuente B? A) proponer alejar las fábricas de las casas, B) vender productos.", "A", "Propone una medida para proteger a los niños."),
        ("{F} ¿Qué fuente defiende la actividad de las fábricas? A) la fuente C, B) la fuente B.", "A", "Considera el humo una señal de progreso."),
        ("{F} Un compañero afirma: «La fuente A prueba que el humo causó todas las muertes». ¿Qué respuesta es mejor? A) la fuente A muestra un aumento, pero no prueba por sí sola la causa, B) es correcto.", "A", "Pudieron influir otros factores."),
        ("{F} Para comparar el pasado con el presente, ¿qué combinación de fuentes sirve? A) la A (pasado) y la D (presente), porque ambas entregan datos, aunque miden cosas distintas, B) la C sola, porque es una opinión.", "A", "Permiten contrastar épocas."),
        ("{F} ¿Qué voz falta en estas cuatro fuentes? A) la de los trabajadores de las fábricas, B) la del médico.", "A", "No hay fuente de los obreros mismos."),
        ("{F} Elige la conclusión mejor sostenida. A) las fuentes muestran distintas miradas y datos que sugieren daño a la salud, pero faltan más pruebas, B) las fuentes prueban que la industria fue un error.", "A", "Es proporcional a la evidencia."),
    ],
    ctx=("Un grupo de ejemplo debe elegir una fuente para mostrar cómo el humo afectaba a las personas en 1890. Opciones: A) la carta de un médico que atendió a niños del barrio, B) el discurso de un empresario que defiende su fábrica. ¿Cuál sirve más para mostrar efectos en la salud?", "A", "Describe lo observado en la salud de los niños."),
    sc=[("En Historia: ¿qué significa contextualizar una fuente?", "Preguntar quién la escribió, cuándo, dónde y para qué", "Permite interpretarla bien."),
        ("¿Qué diferencia hay entre un dato y una opinión?", "El dato se puede comprobar con una cifra; la opinión expresa un punto de vista", "Por eso se respaldan las opiniones con datos."),
        ("¿Por qué una serie estadística no prueba por sí sola una causa?", "Porque otros factores pudieron influir", "Muestra una evolución, no un mecanismo.")],
    op=("{F} Elige dos fuentes de distinto tipo y escribe para cada una: quién habla, qué propósito tiene y qué dato o idea entrega. Termina con una frase que explique qué ganas al usarlas juntas y qué fuente adicional buscarías.",
        "Fuente A: instituto de estadísticas; informa; entrega que las muertes pasaron de 120 a 480. Fuente C: empresario; defiende su actividad; entrega la idea de que el humo es progreso. Juntas muestran datos y una mirada contraria. Buscaría un testimonio de trabajadores.",
        ["clasifica dos fuentes", "explica el propósito", "justifica el uso conjunto"], ["dos fuentes analizadas y una conclusión"], ["tratar una opinión como dato", "no proponer una fuente adicional"], "Léele tu respuesta a una persona de tu casa y pídele que diga si la fuente adicional que propones es útil."),
    reinforce="Escribe una lista de tres tipos de fuentes que podrían servir para estudiar la contaminación de un río.",
    extend="Explica por qué una autoridad ambiental y una empresa pueden presentar datos distintos sobre el mismo río.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = ("Tabla de ejemplo, tres territorios ficticios. "
      "Zona minera del norte: antes de la industria, 500 habitantes y un río limpio; hoy, 8.000 habitantes, 900 empleos en la mina y un río con residuos; dependen de la minería. "
      "Ciudad portuaria: antes, 2.000 habitantes; hoy, 60.000, con un puerto y fábricas; 70 días al año con mala calidad del aire. "
      "Valle agrícola: antes, 3.000 habitantes y agua abundante; hoy, 3.500 habitantes y menos agua por el uso de las industrias cercanas. "
      "Dato global de ejemplo: entre 1900 y hoy, las emisiones de dióxido de carbono del mundo pasaron de 2 a 36 unidades (mil millones de toneladas al año).")
build(
    OA, 3, F3,
    use="Aprenderé a describir qué cambió y qué continuó en el ambiente de distintos territorios con la industrialización, y a relacionar lo local con lo global. Sirve para entender por qué algunos lugares sufren más impactos que otros.",
    prior=["Conozco la industrialización y la contaminación.", "Sé distinguir cambio y continuidad.", "Sé calcular cuántas veces creció una cantidad."],
    explain=[
        "El impacto de la industrialización no fue igual en todos los territorios. En las zonas mineras se transformó el paisaje y los ríos recibieron residuos; en las ciudades portuarias creció la población y empeoró la calidad del aire; en los valles agrícolas aumentó la presión sobre el agua. Hoy se habla de zonas de sacrificio ambiental para referirse a lugares donde se concentran muchas industrias y la población soporta más contaminación.",
        "También hay continuidades: muchas actividades todavía dependen de combustibles fósiles y de recursos naturales. Los combustibles fósiles, al quemarse, liberan dióxido de carbono, un gas que aumenta el efecto invernadero. El efecto invernadero es el calentamiento de la atmósfera por gases que retienen calor, y su aumento provoca el cambio climático, es decir, una variación del clima del planeta que hoy se acelera por las emisiones de esos gases.",
        "Esto muestra una relación entre escalas: un problema local, como el humo de una ciudad, se suma a un problema global, como el aumento de las emisiones. Al analizar un caso conviene decir qué ocurrió en el lugar, cómo se conecta con el mundo y qué cambió respecto del pasado. Las medidas también se pueden pensar en las dos escalas: local, como filtros en una planta, y global, como acuerdos entre países.",
    ],
    vocab=[("zona de sacrificio ambiental", "lugar donde se concentran muchas industrias y la población soporta más contaminación"), ("emisión", "cantidad de gases o residuos que se liberan al ambiente"), ("efecto invernadero", "calentamiento de la atmósfera por gases que retienen calor"), ("cambio climático", "variación del clima del planeta, hoy acelerada por el aumento de gases de efecto invernadero"), ("escala", "nivel del análisis: local, regional o global")],
    worked=[
        ("Calcular cuántas veces creció una población", "Una ciudad de ejemplo pasó de 1.500 a 30.000 habitantes. ¿Cuántas veces creció?",
         ["Divido la población final entre la inicial.", "30.000 ÷ 1.500 = 20."], "20 veces"),
        ("Relacionar lo local y lo global", "Una planta de ejemplo emite humo que afecta a su ciudad. ¿Cómo se conecta con el cambio climático?",
         ["Si quema combustibles fósiles, libera dióxido de carbono.", "Esas emisiones se suman a las del mundo y aumentan el efecto invernadero."], "Sus emisiones se suman a las globales"),
    ],
    mistakes=[
        ("Creer que los impactos fueron iguales en todos los lugares.", "Dependieron de la actividad y del territorio.", "Describe cada lugar por separado."),
        ("Pensar que el cambio climático no tiene relación con las industrias locales.", "Las emisiones locales se suman a las globales.", "Relaciona la escala local con la global."),
    ],
    T=[
        ("En Historia: ¿qué es el efecto invernadero?", "El calentamiento de la atmósfera por gases que retienen calor", "Aumenta cuando suben las emisiones."),
        ("{F} ¿Cuántos habitantes tiene hoy la zona minera?", "8.000", "La tabla lo informa."),
        ("{F} ¿Qué territorio tiene menos agua por el uso de las industrias cercanas? A) el valle agrícola, B) la zona minera.", "A", "La tabla lo dice."),
        ("=", "{F} ¿Cuántas veces creció la población de la ciudad portuaria?", "60000//2000", "Se divide la población actual entre la anterior."),
        ("=", "{F} ¿Cuántas veces creció la población de la zona minera?", "8000//500", "Se divide la población actual entre la anterior."),
        ("=", "{F} ¿Cuántos habitantes más tiene hoy el valle agrícola?", "3500-3000", "Se resta la población anterior a la actual."),
        ("=", "{F} ¿Cuántas veces mayor fueron las emisiones de dióxido de carbono hoy que en 1900?", "36//2", "Se divide la cifra actual entre la de 1900."),
        ("{F} ¿Cuál de estos territorios muestra en la tabla un dato de mala calidad del aire? A) la ciudad portuaria, B) el valle agrícola.", "A", "Solo la ciudad portuaria tiene días con mala calidad del aire."),
        ("{F} ¿Qué continuidad se mantiene en varios territorios de la tabla? A) la dependencia de actividades que usan recursos naturales, B) la ausencia total de industria.", "A", "Mina, puerto y agua industrial lo muestran."),
        ("{F} Un compañero dice: «El cambio climático es solo un problema de los países grandes». ¿Qué respuesta es mejor? A) las emisiones locales se suman y afectan a todos, B) es correcto.", "A", "Las emisiones se acumulan en la atmósfera."),
        ("{F} ¿Qué dos escalas aparecen en la tabla? Responde con dos palabras.", "Local y global", "Se muestran territorios y el dato del mundo."),
        ("{F} Una persona dice: «En la zona minera solo hay beneficios». ¿Qué dato de la tabla la contradice? A) el río con residuos, B) los 900 empleos.", "A", "Es un costo ambiental."),
        ("{F} ¿Qué medida podría reducir el humo en la ciudad portuaria? A) instalar filtros y fiscalizar las emisiones, B) aumentar el número de fábricas del puerto.", "A", "Atiende la causa local."),
    ],
    ctx=("Un concejo de ejemplo debe elegir entre construir una fundición cerca de un valle agrícola o lejos de él. Si se construye cerca, el agua podría disminuir. ¿Qué consideración territorial es importante? A) ver cómo la ubicación afecta al agua del valle, B) pensar solo en el número de empleos que ofrecerá.", "A", "El territorio determina el impacto."),
    sc=[("En Historia: ¿qué es una zona de sacrificio ambiental?", "Un lugar donde se concentran muchas industrias y la población soporta más contaminación", "Su población enfrenta más riesgos."),
        ("¿Qué gas liberan los combustibles fósiles al quemarse y aumenta el efecto invernadero?", "El dióxido de carbono", "Se acumula en la atmósfera."),
        ("¿Por qué conviene analizar escalas local y global?", "Porque un problema local se suma a uno global", "Ambas escalas se conectan.")],
    op=("{F} Elige un territorio y escribe un párrafo que diga: qué cambió, qué continuó, un cálculo con una cifra de la tabla y cómo se conecta con el cambio climático.",
        "Ciudad portuaria: cambió su población, de 2.000 a 60.000 (30 veces más). Continúa su dependencia de las fábricas y del puerto, con 70 días al año de mala calidad del aire. Si quema combustibles fósiles, sus emisiones se suman a las globales, que pasaron de 2 a 36 unidades.",
        ["describe cambio y continuidad", "incluye un cálculo", "relaciona con el cambio climático"], ["un párrafo con una cifra"], ["no mencionar ninguna continuidad", "no relacionar con el clima"], "Pide a una persona de tu casa que compruebe tu división."),
    reinforce="Haz una tabla de tres columnas con territorio, cambio y continuidad.",
    extend="Explica por qué quienes viven cerca de industrias pueden ser más afectados que quienes viven lejos.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = ("Caso de ejemplo, ciudad ficticia «Bahía Roja» con una planta industrial que da 800 empleos y aporta el 40 % del presupuesto municipal. La planta emite 10.000 toneladas de gases al año. Al año hay 30 días con alerta por mala calidad del aire. "
      "Instalar filtros costaría 2.000 millones de pesos y reduciría las emisiones en un 60 %. "
      "Voz de la empresa (de ejemplo): «Sin la planta se pierden empleos; instalar filtros es caro.» "
      "Voz de los trabajadores (de ejemplo): «Queremos conservar el empleo y respirar aire sano.» "
      "Voz de los vecinos (de ejemplo): «Los niños se enferman cada invierno; pedimos medidas.» "
      "Voz de la autoridad ambiental (de ejemplo): «Debemos fiscalizar y proponer metas de reducción.» "
      "Voz de un científico (de ejemplo): «Las emisiones de la planta contribuyen al problema, pero hay otras fuentes en la ciudad.»")
build(
    OA, 4, F4,
    use="Aprenderé a contrastar actores, causas y perspectivas en un conflicto entre producción y ambiente. Sirve para ver que empleo y ambiente no siempre se oponen de forma absoluta.",
    prior=["Conozco contaminación, emisiones y desarrollo sostenible.", "Sé que cada actor tiene una perspectiva.", "Sé calcular porcentajes de una cantidad."],
    explain=[
        "En un conflicto ambiental participan varios actores: la empresa, los trabajadores, los vecinos, las autoridades y los científicos. Cada uno tiene intereses distintos. La empresa busca producir y controlar costos; los trabajadores, conservar su empleo; los vecinos, proteger su salud; la autoridad, hacer cumplir las normas; el científico aporta datos sobre las causas del problema.",
        "Las causas de la contaminación suelen ser varias. En una ciudad, además de una planta pueden contribuir el transporte, la calefacción y otras industrias. Esto es multicausalidad, y obliga a no atribuir toda la responsabilidad a un solo actor. También se distinguen los costos y los beneficios de una medida: una medida puede reducir la contaminación pero costar dinero, y puede protegerse el empleo con un plan gradual.",
        "Oponer empleo y ambiente como si fueran opciones absolutas es un error frecuente. Muchas veces se pueden combinar con tecnologías más limpias, fiscalización y metas progresivas. Evaluar un caso significa comparar datos, escuchar todas las voces y proponer medidas que consideren las tres dimensiones del desarrollo sostenible: la económica, la social y la ambiental.",
    ],
    vocab=[("fiscalizar", "controlar que se cumplan las normas"), ("meta de reducción", "objetivo de disminuir una cantidad, como las emisiones, en un plazo"), ("tecnología más limpia", "forma de producir que emite menos residuos o gases"), ("multicausalidad", "situación en que un hecho tiene varias causas a la vez"), ("dimensión", "uno de los aspectos que se consideran en un análisis: económico, social o ambiental")],
    worked=[
        ("Calcular una reducción", "Una planta de ejemplo emite 5.000 toneladas al año. Un filtro reduce un 40 %. ¿Cuántas toneladas dejan de emitirse?",
         ["El 40 % de 5.000 es 5.000 × 40 ÷ 100.", "El resultado es 2.000."], "2.000 toneladas"),
        ("Asociar una voz con un interés", "Una voz de ejemplo dice: «Pedimos medidas porque nuestros hijos se enferman». ¿Qué interés tiene?",
         ["Habla de la salud de los niños.", "Su interés es proteger la salud."], "Proteger la salud"),
    ],
    mistakes=[
        ("Culpar solo a la empresa o solo a los vecinos.", "El problema tiene varias causas y actores.", "Revisa las distintas causas y voces."),
        ("Creer que cuidar el ambiente siempre destruye empleos.", "Hay medidas graduales y tecnologías que pueden compatibilizar ambos.", "Busca soluciones que combinen dimensiones."),
    ],
    T=[
        ("En Historia: ¿qué significa fiscalizar?", "Controlar que se cumplan las normas", "Es la función de la autoridad ambiental."),
        ("{F} ¿Cuántos empleos da la planta de Bahía Roja?", "800", "El caso lo informa."),
        ("{F} ¿Qué voz pide proteger la salud de los niños? A) la de los vecinos, B) la de la empresa.", "A", "Dice que los niños se enferman."),
        ("=", "{F} ¿Cuántas toneladas dejarían de emitirse con los filtros?", "10000*60//100", "Se calcula el 60 % de 10.000."),
        ("=", "{F} ¿Cuántas toneladas se emitirían al año con los filtros?", "10000-10000*60//100", "Se resta la reducción a las emisiones actuales."),
        ("=", "{F} Si el presupuesto municipal es de 5.000 millones, ¿cuántos millones aporta la planta (40 %)?", "5000*40//100", "Se calcula el 40 % del presupuesto."),
        ("=", "{F} Si la empresa pagara el costo de los filtros en 4 años con cuotas anuales iguales, ¿cuántos millones de pesos pagaría cada año?", "2000//4", "Se divide el costo total entre los 4 años."),
        ("{F} ¿Qué voz reconoce que hay otras fuentes de contaminación? A) la del científico, B) la de los vecinos.", "A", "Habla de otras fuentes en la ciudad."),
        ("{F} Un comentarista dice: «La planta es la única responsable de las alertas». ¿Qué voz contradice la idea? A) la del científico, B) la de la empresa.", "A", "Indica que hay otras fuentes."),
        ("{F} ¿Qué voz expresa la necesidad de compatibilizar empleo y salud? A) la de los trabajadores, B) la de la autoridad.", "A", "Quieren empleo y aire sano."),
        ("{F} ¿Qué medida combina las dimensiones económica, social y ambiental? A) filtros instalados en etapas, con protección del empleo y metas de reducción, B) cerrar la planta sin plan.", "A", "Considera empleo, salud y ambiente."),
        ("{F} La empresa dice que instalar filtros es caro. ¿Qué dato del caso puede responder a esa objeción? A) la reducción del 60 % y los 30 días de alerta, B) cuántos años lleva funcionando la planta.", "A", "Muestra el beneficio ambiental."),
        ("{F} ¿Qué información adicional necesitarías para evaluar mejor? A) cuántas de las alertas se deben a la planta y cuántas a otras fuentes, B) cuántos años lleva funcionando la planta.", "A", "Aclara la causa."),
    ],
    ctx=("Un concejo de ejemplo debe decidir si exigir filtros a una planta que emite 8.000 toneladas al año y da 300 empleos. Un filtro reduciría las emisiones en 50 %. ¿Cuántas toneladas dejarían de emitirse? A) 4.000, B) 800.", "A", "El 50 % de 8.000 es 4.000."),
    sc=[("En Historia: ¿qué es la multicausalidad en un problema ambiental?", "Que el problema tiene varias causas a la vez", "No se debe culpar a un solo actor."),
        ("¿Por qué empleo y ambiente no siempre se oponen de forma absoluta?", "Porque se pueden combinar con tecnologías más limpias y metas graduales", "Existen soluciones intermedias."),
        ("¿Qué hace una autoridad ambiental?", "Fiscaliza que se cumplan las normas", "Controla las emisiones.")],
    op=("{F} Elige dos voces y escribe para cada una: qué actor es, qué interés tiene y qué dato del caso la apoya. Termina proponiendo una medida que considere empleo, salud y ambiente, con una cifra.",
        "Empresa: busca producir y controlar costos; apoya su voz el costo de 2.000 millones. Vecinos: protegen la salud; los apoyan los 30 días de alerta. Medida: instalar filtros por etapas, conservando los 800 empleos y reduciendo 6.000 toneladas.",
        ["describe dos actores", "usa un dato", "propone una medida con cifra"], ["dos voces y una medida"], ["culpar a un solo actor", "proponer cerrar sin plan ni cifras"], "Pide a una persona de tu casa que opine si tu medida considera las tres dimensiones."),
    reinforce="Haz un cuadro con tres actores, su interés y un posible costo para cada uno.",
    extend="Explica por qué fiscalizar es importante aunque las empresas quieran cumplir.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = ("Dossier de ejemplo, «¿Es sostenible reemplazar la caldera de carbón de una planta por energía solar?» "
      "Dato 1 (económico): el cambio cuesta 5.000 millones de pesos y ahorra 500 millones al año en combustible. "
      "Dato 2 (social): la planta mantiene sus 800 empleos y capacita a 100 trabajadores en el nuevo sistema. "
      "Dato 3 (ambiental): las emisiones de dióxido de carbono bajan de 10.000 a 2.000 toneladas al año. "
      "Dato 4 (ambiental): los paneles necesitan 50 hectáreas de terreno de matorral nativo. "
      "Definición de ejemplo: una medida es sostenible si considera de manera equilibrada las dimensiones económica, social y ambiental.")
build(
    OA, 5, F5,
    use="Aprenderé a argumentar si una medida es sostenible considerando las tres dimensiones del desarrollo y no solo una ventaja. Sirve para participar en el debate actual sobre desarrollo sostenible con evidencia.",
    prior=["Conozco el desarrollo sostenible y sus tres dimensiones.", "Sé calcular porcentajes y divisiones.", "Sé armar un argumento con tesis, evidencia, objeción y límite."],
    explain=[
        "El desarrollo sostenible busca que el crecimiento económico, la justicia social y el cuidado del ambiente avancen a la vez. En el mundo actual esto se expresa en acuerdos internacionales como la Agenda 2030, que fijó 17 objetivos de desarrollo sostenible, y en debates sobre cómo reducir las emisiones sin perjudicar el empleo. Para decidir si una medida es sostenible se revisan las tres dimensiones: económica, social y ambiental.",
        "Es un error llamar sostenible a una medida por una sola ventaja. Una medida puede bajar las emisiones y aun así ser costosa o dañar un ecosistema; otra puede crear empleo y contaminar. Por eso la evaluación mira todas las dimensiones, reconoce los costos y las compensaciones, y nombra lo que falta saber. Una conclusión sólida es proporcional a la evidencia.",
        "Al argumentar, la tesis dice si la medida es sostenible o no, y la evidencia usa cifras de cada dimensión. La objeción presenta lo mejor de la postura contraria, y la respuesta propone cómo reducir los problemas, por ejemplo compensando el terreno afectado. El límite señala lo que los datos no permiten afirmar.",
    ],
    vocab=[("dimensión económica", "aspecto del análisis que mira costos, ahorros y producción"), ("dimensión social", "aspecto del análisis que mira empleo, salud y bienestar de las personas"), ("dimensión ambiental", "aspecto del análisis que mira aire, agua, suelo y biodiversidad"), ("compensación", "acción que reduce o repara un daño causado"), ("ecosistema", "conjunto de seres vivos y su entorno que interactúan entre sí")],
    worked=[
        ("Calcular cuántos años tarda en pagarse una inversión", "Una medida de ejemplo cuesta 600 millones y ahorra 100 millones al año. ¿En cuántos años se recupera el costo?",
         ["Divido el costo entre el ahorro anual.", "600 ÷ 100 = 6."], "6 años"),
        ("Revisar las tres dimensiones", "Una medida de ejemplo baja las emisiones y mantiene el empleo, pero destruye un humedal. ¿Qué dimensión queda en conflicto?",
         ["La reducción de emisiones y el empleo son ventajas.", "Destruir un humedal daña el ecosistema: es la dimensión ambiental."], "La dimensión ambiental"),
    ],
    mistakes=[
        ("Llamar sostenible a una medida por una sola ventaja.", "Puede tener costos en otra dimensión.", "Revisa las tres dimensiones antes de concluir."),
        ("Pensar que la sostenibilidad exige renunciar siempre al progreso económico.", "Busca equilibrar las dimensiones, no eliminar una.", "Propone cómo combinarlas."),
    ],
    T=[
        ("En Historia: ¿cuáles son las tres dimensiones del desarrollo sostenible?", "Económica, social y ambiental", "Se evalúan de manera equilibrada."),
        ("{F} ¿Cuánto cuesta el cambio de caldera?", "5.000 millones de pesos", "El dato 1 lo informa."),
        ("{F} ¿Qué dato del dossier es una ventaja social? A) mantener 800 empleos y capacitar a 100 trabajadores, B) bajar las emisiones.", "A", "Se refiere a las personas."),
        ("=", "{F} ¿Cuántas toneladas de dióxido de carbono dejan de emitirse al año?", "10000-2000", "Se resta la emisión nueva a la actual."),
        ("=", "{F} ¿Qué porcentaje de las emisiones se reduce?", "(10000-2000)*100//10000", "Se divide la reducción entre la emisión inicial y se multiplica por 100.", "%"),
        ("=", "{F} ¿En cuántos años se recupera el costo con el ahorro de combustible?", "5000//500", "Se divide el costo entre el ahorro anual."),
        ("{F} ¿Qué dato muestra un costo ambiental del proyecto? A) el dato 4, que ocupa matorral nativo, B) el dato 2.", "A", "Afecta un ecosistema."),
        ("{F} ¿Qué dimensión representa el dato 1? A) la económica, B) la social.", "A", "Habla de costos y ahorros."),
        ("{F} Una persona dice: «La medida es sostenible porque baja las emisiones». ¿Qué problema tiene? A) no considera el costo ni el terreno afectado, B) es demasiado larga.", "A", "Se queda en una sola ventaja."),
        ("{F} ¿Qué respuesta atiende la objeción del terreno? A) compensar el matorral con otras hectáreas protegidas, B) ignorar el dato 4.", "A", "Reduce el daño."),
        ("{F} ¿Qué conclusión es más proporcional a la evidencia? A) la medida es prometedora, pero conviene evaluar su impacto en el matorral y buscar compensaciones, B) la medida es perfecta.", "A", "Reconoce ventajas y límites."),
        ("=", "{F} Si el ahorro anual fuera de 250 millones en vez de 500, ¿en cuántos años se recuperaría el costo?", "5000//250", "Se divide el costo entre el nuevo ahorro."),
        ("{F} Ordena las partes de un argumento: a) objeción, b) tesis, c) evidencia, d) límite. Escribe las letras en el orden más lógico.", "b, c, a, d", "Primero se afirma, luego se respalda, se reconoce lo contrario y se indica el límite."),
    ],
    ctx=("Una comuna de ejemplo evalúa una planta de reciclaje que da 60 empleos y reduce los residuos que van al vertedero en un 30 %. El camino hasta la planta atraviesa un humedal. ¿Qué dimensión debe revisar antes de decidir? A) la ambiental, por el humedal, B) ninguna, porque ya da empleo.", "A", "Un beneficio no elimina un posible costo."),
    sc=[("En Historia: ¿qué es la dimensión ambiental?", "El aspecto que mira aire, agua, suelo y biodiversidad", "Evalúa el efecto sobre la naturaleza."),
        ("¿Por qué no basta una sola ventaja para llamar sostenible a una medida?", "Porque puede tener costos en otra dimensión", "Se deben revisar las tres."),
        ("¿Qué es una compensación?", "Una acción que reduce o repara un daño causado", "Ayuda a equilibrar una medida.")],
    op=("{F} Escribe un argumento de cinco a siete líneas sobre si la medida es sostenible. Incluye tu tesis, una cifra de cada dimensión, una objeción con su respuesta y un límite de los datos.",
        "Tesis: la medida es prometedora pero no plenamente sostenible aún. Económico: se recupera en 10 años. Social: mantiene 800 empleos. Ambiental: reduce 8.000 toneladas, pero ocupa 50 hectáreas de matorral. Objeción: daña el matorral; se responde con compensación. Límite: no sabemos el valor ecológico del terreno.",
        ["declara una tesis", "usa una cifra por dimensión", "responde una objeción", "indica un límite"], ["un argumento de cinco a siete líneas"], ["mirar solo una dimensión", "afirmar que la medida es perfecta"], "Léele tu argumento a una persona de tu casa y pídele que identifique las tres dimensiones."),
    reinforce="Escribe tres medidas para tu casa o colegio y marca qué dimensión mejora cada una.",
    extend="Explica por qué una medida puede ser sostenible en un territorio y no en otro.",
    materials=MAT,
)
