"""Cuaderno del estudiante, 7.º básico Historia, Geografía y Ciencias Sociales: OA 12 (transformaciones europeas desde el siglo XII)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI07 OA 12"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a explicar por qué las ciudades europeas crecieron desde el siglo XII. Sirve para entender que un cambio grande tiene varias causas que se refuerzan entre sí.",
    ["Sé que en la Edad Media la mayoría vivía en el campo.", "Sé que un hecho puede tener varias causas."],
    [
        "Desde el siglo XI y sobre todo desde el XII, Europa occidental vivió un renacimiento urbano: las ciudades antiguas se repoblaron y nacieron otras nuevas. Los habitantes de una ciudad o «burgo» se llamaban burgueses. Eran artesanos y comerciantes, no campesinos ni señores. Vivían de su trabajo y de vender sus productos.",
        "Este crecimiento tuvo causas que se combinaron. Primero, aumentó la población: hubo más gente porque había menos guerras graves y más comida. Segundo, el campo produjo más gracias a nuevas técnicas, como el arado pesado de hierro, el molino de agua y la rotación de tres campos, que dejaba descansar la tierra. Tercero, el comercio se reactivó y las ciudades se convirtieron en mercados donde se compraba y vendía.",
        "Para vivir con más libertad, muchas ciudades obtuvieron cartas o privilegios de reyes y señores que las reconocían como comunidades con reglas propias. Aun así, una ciudad medieval era pequeña según los números de hoy: la mayoría tenía algunos miles de habitantes. Hay que cuidar las cifras, porque no hay censos exactos y las fuentes se contradicen.",
    ],
    [("burgo", "ciudad o población medieval, a menudo amurallada"), ("burgués", "habitante de una ciudad que vive del comercio o de un oficio"), ("renacimiento urbano", "regreso y crecimiento de las ciudades desde los siglos XI y XII"), ("excedente", "lo que sobra después de cubrir lo que se necesita"), ("rotación de tres campos", "sistema agrícola que dividía la tierra en tres partes y dejaba una en descanso cada año"), ("carta de franquicia", "documento que daba derechos y libertades a una ciudad")],
    [
        ("Ordenar causas", "Un campo produce más trigo, así que hay más comida; por eso nacen más niños que sobreviven. ¿Cuál es la causa y cuál la consecuencia?", ["La causa es lo que ocurre primero.", "Más trigo permite alimentar a más personas.", "La consecuencia es el aumento de la población."], "Causa: más producción agrícola; consecuencia: más población"),
        ("Leer datos de ejemplo", "Datos de ejemplo: una ciudad tenía 3.000 habitantes en el año 1100 y 6.000 en el año 1200. ¿Qué pasó con su población?", ["Compara 6.000 con 3.000.", "6.000 es el doble de 3.000."], "Se duplicó"),
    ],
    [
        ("Pensar que las ciudades crecieron por una sola causa.", "Crecieron porque se combinaron más población, mejores técnicas agrícolas y más comercio.", "Busca al menos dos causas y cómo se refuerzan."),
        ("Imaginar las ciudades medievales como grandes metrópolis modernas.", "La mayoría tenía algunos miles de habitantes y estaba rodeada de murallas.", "Compara siempre con el tamaño de la época, no con el de hoy."),
    ],
    [
        ("¿Cómo se llamaba el habitante de una ciudad que vivía del comercio o de un oficio?", "Burgués", "Esa es la definición del vocabulario."),
        ("¿Qué técnica agrícola dejaba descansar una parte de la tierra cada año?", "La rotación de tres campos", "Dividía la tierra en tres y una descansaba."),
        ("¿Desde qué siglo se habla de renacimiento urbano con más fuerza, según la clase?", "Desde el siglo XII", "La clase indica que el proceso se acelera en ese siglo."),
    ],
    [
        ("¿Por qué más comida en el campo ayuda a que crezcan las ciudades?", "Porque permite alimentar a más gente y deja productos para vender en el mercado", "Un excedente agrícola abastece a quienes no cultivan."),
        ("¿Qué querían lograr las ciudades al pedir una carta de franquicia?", "Libertades y reglas propias reconocidas por un rey o un señor", "La carta les daba derechos como comunidad."),
        ("Nombra dos innovaciones agrícolas del texto que aumentaron la producción.", "Dos de estas: arado pesado de hierro, molino de agua, rotación de tres campos", "Son las técnicas que se mencionan como causa del aumento de la producción."),
    ],
    [
        arith("Una ciudad de ejemplo pasó de 4.500 habitantes a 9.000 en cien años. ¿Cuántos habitantes más tenía al final?", "9000-4500", "Se resta la población inicial a la final."),
        ("Datos de ejemplo: en 1100 la ciudad A tenía 2.000 habitantes y la B, 3.000; en 1200, la A tenía 5.000 y la B, 4.500. ¿Cuál creció más en cantidad de personas?", "La A", "La A subió en 3.000 personas y la B, en 1.500."),
        ("Un campesino se muda a una ciudad y se hace tejedor. ¿Se convirtió en burgués o siguió siendo campesino?", "Se convirtió en burgués", "Pasó a vivir de un oficio en la ciudad."),
    ],
    [
        ("Lucas afirma: «Las ciudades crecieron solo porque llegó el comercio». ¿Qué otras dos causas de la clase le faltan?", "El aumento de la población y las nuevas técnicas agrícolas", "El texto presenta tres causas que se combinan."),
        ("Una fuente de ejemplo dice que una ciudad tenía «cien mil almas» en el año 1200. ¿Por qué hay que dudar de esa cifra?", "Porque no existían censos exactos y la mayoría de las ciudades tenían algunos miles de habitantes", "La clase advierte que las cifras medievales son imprecisas."),
    ],
    [
        ("Ordena esta cadena de causa a efecto final: A) más comida, B) más población, C) mercados más activos, D) ciudades más grandes.", "A, B, C, D", "La cadena de la clase va de la comida al tamaño de las ciudades."),
        ("Una fuente de ejemplo de 1150 dice: «Los habitantes de este burgo pagan cada año una cantidad fija al rey y a cambio eligen a sus jueces». ¿Qué documento de la clase explica ese acuerdo?", "Una carta de franquicia", "Reconocía derechos a la ciudad a cambio de pagos."),
    ],
    [("Una aldea de ejemplo cultiva con la rotación de tres campos. Cada año una de las tres partes descansa. Si la aldea tiene 90 hectáreas, ¿cuántas hectáreas descansan cada año?", "30 hectáreas", "Una tercera parte de 90 hectáreas son 30.")],
    [("En la unidad de transformaciones europeas, ¿qué es un burgués?", "Un habitante de la ciudad que vive del comercio o de un oficio", "Es la definición del vocabulario."), ("Nombra una causa del renacimiento urbano.", "Aumento de la población, nuevas técnicas agrícolas o reactivación del comercio", "Son las tres causas de la explicación."), ("¿Por qué conviene dudar de las cifras de población medievales?", "Porque no había censos exactos", "Las fuentes se contradicen.")],
    (
        "Escribe una explicación de cinco líneas: «¿Por qué crecieron las ciudades europeas desde el siglo XII?». Usa al menos dos causas de la lista (más población, nuevas técnicas agrícolas, más comercio, cartas de franquicia) y una frase que diga cómo una causa refuerza a otra. Termina con una advertencia sobre las cifras.",
        "Crecieron porque el campo produjo más y hubo más población; más gente compró y vendió, y eso reforzó el comercio. Las cifras de entonces son imprecisas.",
        ["menciona dos causas", "explica una relación entre causas", "incluye la advertencia sobre cifras", "usa fechas o siglos correctos"],
        ["párrafo de cinco líneas con los cuatro elementos"],
        ["dar una sola causa", "usar cifras actuales para ciudades medievales"],
        "Léele tu explicación a una persona de tu casa y pídele que repita cuántas causas entendió.",
    ),
    "Dibuja una cadena de causas desde la rotación de tres campos hasta el crecimiento de una ciudad.",
    "Averigua cuántos habitantes tiene hoy la comuna donde vives y compara con los miles de una ciudad medieval.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a relacionar el comercio, las ferias y las rutas europeas desde el siglo XII. Sirve para entender cómo se conectaron ciudades lejanas y qué cambió en la economía.",
    ["Sé que las ciudades crecieron desde el siglo XII.", "Sé leer rutas en un mapa."],
    [
        "Con más producción y más gente, aumentó el comercio. Una feria era un mercado grande que se reunía en fechas fijas, con protección del señor local. Las ferias de Champaña, en el este de Francia, reunían mercaderes de Italia, Flandes y otros lugares durante los siglos XII y XIII. Allí se vendían telas, lana, cuero, vino y especias, y también se arreglaban pagos.",
        "Las rutas conectaban regiones. Por el Mediterráneo las ciudades italianas, como Venecia y Génova, comerciaban con Constantinopla y con puertos del mundo islámico, de donde traían especias y seda. En el norte, ciudades de Flandes producían telas de lana. Muchas ciudades del Báltico y del mar del Norte se unieron en una liga comercial, la Hansa, desde el siglo XIII. Los mercaderes viajaban en grupos y usaban ríos, caminos y barcos.",
        "El comercio trajo innovaciones. Se usó más la moneda de plata. Los mercaderes inventaron la letra de cambio, un documento que permitía pagar en otra ciudad sin cargar monedas. También se extendió la contabilidad por escrito. Con estos cambios, aparecieron los banqueros, que guardaban dinero y hacían préstamos. Algunos grupos, como la Iglesia, discutían si cobrar intereses era correcto, y los préstamos podían causar conflictos.",
    ],
    [("feria", "gran mercado que se reunía en fechas y lugares fijos"), ("ruta comercial", "camino por tierra, río o mar que recorrían los mercaderes"), ("letra de cambio", "documento que permitía pagar en otra ciudad sin llevar monedas"), ("Hansa", "liga de ciudades comerciales del norte de Europa"), ("interés", "dinero extra que se cobra por un préstamo"), ("mercader", "persona que compra y vende productos para ganar dinero")],
    [
        ("Leer una ruta", "Un mercader de ejemplo lleva lana de Flandes a las ferias de Champaña y vuelve con especias compradas a mercaderes italianos. ¿Qué dos productos viajan y en qué sentido?", ["La lana va de Flandes a Champaña.", "Las especias llegan desde Italia a Champaña y luego a Flandes."], "Lana hacia Champaña y especias hacia Flandes"),
        ("Usar una letra de cambio", "Un mercader de Génova no quiere viajar con monedas a Champaña. ¿Qué documento puede usar para pagar allí?", ["El documento permite pagar sin cargar monedas.", "Se llama letra de cambio."], "Una letra de cambio"),
    ],
    [
        ("Pensar que el comercio medieval era solo local.", "Las ferias y las rutas conectaban regiones lejanas como Flandes, Champaña e Italia.", "Ubica las ciudades en la ruta."),
        ("Decir que el dinero apareció recién en el siglo XII.", "El dinero existía antes; lo nuevo fue el uso de la letra de cambio y de bancos más desarrollados.", "Distingue entre existencia y generalización."),
    ],
    [
        ("¿Dónde se celebraban las famosas ferias del este de Francia que reunían mercaderes de varias regiones?", "En Champaña", "La clase las menciona como centro de comercio de los siglos XII y XIII."),
        ("¿Qué documento permitía pagar en otra ciudad sin cargar monedas?", "La letra de cambio", "La definición está en el vocabulario."),
        ("¿Cómo se llamaba la liga de ciudades comerciales del norte?", "Hansa", "Fue una liga de ciudades del Báltico y del mar del Norte."),
    ],
    [
        ("¿Qué ciudades italianas de la clase comerciaban con Constantinopla y puertos islámicos?", "Venecia y Génova", "Son los dos ejemplos que se dan en la explicación."),
        ("¿Por qué una feria necesitaba protección del señor local?", "Porque los mercaderes viajaban con mercancías valiosas y necesitaban seguridad", "La protección permitía comerciar sin ser asaltados."),
        ("Nombra un producto que se vendía en las ferias de Champaña.", "Telas, lana, cuero, vino o especias (cualquiera)", "Son los productos que se mencionan."),
    ],
    [
        arith("Un mercader de ejemplo compra 120 piezas de tela en Flandes y vende 45 en Champaña y 38 en otra feria. ¿Cuántas piezas le quedan?", "120-45-38", "Se restan las piezas vendidas al total."),
        ("Un barco de ejemplo sale de Venecia con vidrio y regresa de Constantinopla con seda. ¿Qué dos mundos comerciaron?", "El latino (Venecia) y el bizantino (Constantinopla)", "Venecia era una ciudad latina y Constantinopla, bizantina."),
        ("Un prestamista de ejemplo presta 100 monedas y pide 110 de vuelta. ¿Cuánto es el interés?", "10 monedas", "El interés es lo que se devuelve de más: 110 menos 100."),
    ],
    [
        ("Ana dice: «Sin la letra de cambio no habría habido comercio a larga distancia». ¿Es exagerada la afirmación? Explica.", "Sí, el comercio existía antes; la letra de cambio lo facilitó", "El comercio ya existía y el documento solo lo volvió más seguro."),
        ("Mario sostiene que cobrar intereses no generó discusiones. Cita un dato de la clase que lo contradice.", "La Iglesia discutía si cobrar intereses era correcto", "El texto menciona esa discusión."),
    ],
    [
        ("Ordena el recorrido de una tela de lana: A) se vende en Champaña, B) se fabrica en Flandes, C) llega a un mercader de Italia.", "B, A, C", "Primero se fabrica, luego se vende en la feria y por último llega al comprador italiano."),
        ("Una fuente de ejemplo dice: «Las ferias se hacían solo para los vecinos del pueblo». Usa un dato de la clase para corregirla.", "Reunían mercaderes de Italia, Flandes y otras regiones", "Eran mercados de alcance regional e internacional."),
    ],
    [("Un historiador de ejemplo afirma: «Las ferias y los puertos italianos muestran que la Europa latina tenía contacto comercial con Bizancio y con el mundo islámico». ¿Qué dato de la clase respalda la frase?", "Venecia y Génova comerciaban con Constantinopla y puertos islámicos", "Es la evidencia de la explicación.")],
    [("En la unidad de transformaciones europeas, ¿qué es una feria?", "Un gran mercado en fechas y lugares fijos", "Es la definición del vocabulario."), ("En la unidad de transformaciones europeas, ¿qué es una letra de cambio?", "Un documento para pagar en otra ciudad sin llevar monedas", "Así se explica en el texto."), ("¿Qué ciudad del norte producía telas de lana?", "Las ciudades de Flandes", "Se mencionan como productoras de lana.")],
    (
        "Dibuja en una hoja un mapa simple con estos puntos: Flandes, Champaña, Venecia, Constantinopla. Une con flechas las rutas y escribe sobre cada flecha un producto que viaja (lana, vino, seda, especias). Escribe después dos líneas diciendo qué rutas unieron a dos mundos distintos.",
        "Flandes → Champaña: lana; Venecia → Champaña: especias; Venecia ← Constantinopla: seda. La ruta Venecia–Constantinopla unía el mundo latino y el bizantino.",
        ["ubica los cuatro puntos", "dibuja al menos tres flechas con productos", "explica qué ruta unió dos mundos", "usa solo productos de la clase"],
        ["mapa simple con flechas y dos líneas de explicación"],
        ["poner productos que no se mencionan", "olvidar la explicación"],
        "Enséñale tu mapa a una persona de tu casa y pídele que siga una ruta con el dedo.",
    ),
    "Escribe qué ventaja tenía la letra de cambio frente a viajar con bolsas de monedas.",
    "Investiga qué productos se vendían en una feria de tu región hoy y compara con las ferias medievales.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a examinar los gremios y las nuevas actividades de las ciudades medievales. Sirve para entender cómo se organizaba el trabajo y quiénes quedaban dentro o fuera.",
    ["Sé que en las ciudades vivían artesanos y comerciantes.", "Sé que una regla puede proteger a unos y excluir a otros."],
    [
        "Un gremio era una asociación de personas que ejercían el mismo oficio en una ciudad, como panaderos, tejedores o herreros. Los gremios fijaban reglas: cómo se hacía el producto, a qué precio se vendía y quién podía ejercer el oficio. Así buscaban asegurar la calidad y evitar la competencia dentro de la ciudad.",
        "Dentro de un gremio había tres categorías. El maestro era dueño del taller y tenía derecho a votar. El oficial trabajaba para un maestro a cambio de un salario. El aprendiz era un niño o joven que aprendía el oficio viviendo en casa del maestro, a veces por varios años. Para llegar a maestro, el oficial debía presentar una obra maestra y, muchas veces, pagar derechos.",
        "Los gremios tuvieron ventajas: protegían a sus miembros, ayudaban a viudas y huérfanos de socios y cuidaban la calidad. También tuvieron límites: era difícil entrar para quienes no eran hijos de maestros, y las mujeres tenían menos acceso, aunque había mujeres en oficios como el hilado o la cerveza. Además aparecieron nuevas actividades urbanas, como banqueros, notarios, médicos y maestros de escuela.",
    ],
    [("gremio", "asociación de personas del mismo oficio en una ciudad"), ("maestro", "dueño de un taller con derecho a votar en el gremio"), ("oficial", "trabajador que recibe un salario de un maestro"), ("aprendiz", "joven que aprende un oficio en casa de un maestro"), ("obra maestra", "trabajo que un oficial presentaba para ser reconocido como maestro"), ("notario", "persona que redacta y certifica documentos")],
    [
        ("Identificar categorías", "Ana tiene 14 años, vive en casa de un panadero y aprende a amasar. ¿Qué categoría tiene en el gremio?", ["Vive en casa del maestro.", "Está aprendiendo el oficio.", "Es aprendiz."], "Aprendiz"),
        ("Aplicar una regla", "Una regla de ejemplo dice: «Nadie puede vender pan a un precio distinto del fijado por el gremio». ¿Qué buscaba el gremio con esa regla?", ["Fijar un precio evita que unos vendan mucho más barato.", "Busca controlar la competencia."], "Controlar la competencia y proteger a sus miembros"),
    ],
    [
        ("Creer que cualquiera podía abrir un taller.", "Había que pertenecer al gremio y ser reconocido maestro.", "Pregunta qué categoría tiene cada persona."),
        ("Pensar que los gremios solo tuvieron ventajas.", "También limitaban el acceso de quienes no eran hijos de maestros y reducían la competencia.", "Para evaluar, nombra ventajas y límites."),
    ],
    [
        ("¿Quién era el dueño del taller en un gremio?", "El maestro", "El maestro dirigía el taller y votaba."),
        ("¿Cómo se llamaba el joven que aprendía un oficio en casa de un maestro?", "Aprendiz", "Es la definición del vocabulario."),
        ("¿Qué debía presentar un oficial para ser reconocido como maestro?", "Una obra maestra", "Era la prueba de su habilidad."),
    ],
    [
        ("¿Por qué un gremio fijaba reglas de calidad?", "Para asegurar productos buenos y proteger la reputación del oficio", "Un mal producto dañaba a todos los miembros."),
        ("¿Qué ayuda daba un gremio a viudas y huérfanos de socios?", "Ayuda y protección", "El gremio funcionaba también como ayuda mutua entre sus miembros."),
        ("Nombra dos nuevas actividades urbanas que aparecieron además de los oficios manuales.", "Dos de estas: banqueros, notarios, médicos, maestros de escuela", "Son las actividades que se mencionan."),
    ],
    [
        arith("Un aprendiz de ejemplo estudia siete años con un maestro y luego trabaja cuatro años como oficial antes de intentar ser maestro. ¿Cuántos años pasan desde que empieza hasta que intenta ser maestro?", "7+4", "Se suman los años de aprendizaje y de trabajo como oficial."),
        ("Beatriz es hija de un tejedor maestro. Pedro es hijo de un campesino sin oficio. ¿Quién tiene más facilidad para entrar al gremio de tejedores y por qué?", "Beatriz, porque era hija de un maestro", "Los gremios favorecían a los hijos de maestros."),
        ("Una regla de ejemplo dice: «Ningún taller puede tener más de dos aprendices». ¿A quién protege principalmente: a los talleres grandes o a los pequeños?", "A los talleres pequeños", "Evita que un taller grande concentre a todos los aprendices."),
    ],
    [
        ("Tomás dice: «Los gremios eran justos porque todos los vecinos podían unirse». ¿Qué dato lo contradice?", "Era difícil entrar para quienes no eran hijos de maestros y las mujeres tenían menos acceso", "La clase señala límites de acceso."),
        ("Un taller vende camisas con calidad baja. ¿Qué regla del gremio estaría incumpliendo, según la clase?", "Faltaría a las reglas de calidad del gremio, que existían para vigilar los productos", "Una función del gremio era cuidar la calidad con reglas."),
    ],
    [
        ("Ordena de menor a mayor autonomía dentro del gremio: A = maestro, B = aprendiz, C = oficial.", "B, C, A", "El aprendiz es el que aprende, el oficial trabaja por salario y el maestro es dueño del taller."),
        ("Un historiador de ejemplo dice: «Las mujeres nunca trabajaron en oficios organizados». ¿Qué ejemplo de la clase lo contradice?", "Había mujeres en oficios como el hilado o la cerveza", "La clase indica que tenían menos acceso, pero sí había presencia."),
    ],
    [("Una ciudad de ejemplo tiene tres gremios: panaderos, herreros y tejedores. Un forastero llega y quiere vender pan sin pertenecer a ningún gremio. Según las reglas de la clase, ¿qué podría ocurrir?", "No le permitirían vender pan sin ser parte del gremio de panaderos", "El gremio controlaba quién ejercía el oficio.")],
    [("En la unidad de transformaciones europeas, ¿qué es un gremio?", "Una asociación de personas del mismo oficio en una ciudad", "Es la definición del vocabulario."), ("Nombra una ventaja de los gremios.", "Aseguraban calidad, protegían a sus miembros o daban ayuda mutua", "Son ventajas del texto."), ("Nombra un límite de los gremios.", "Era difícil entrar para quien no era hijo de maestro o limitaban la competencia", "Son límites del texto.")],
    (
        "Imagina que eres un oficial de zapatero que quiere ser maestro. Lee estas reglas de ejemplo: 1) hay que presentar una obra maestra, 2) hay que pagar un derecho al gremio, 3) solo se admite a quien lleva cuatro años como oficial. Escribe seis líneas explicando qué ventajas y qué problemas tienen esas reglas para el oficial y para la ciudad.",
        "La obra maestra asegura calidad, pero el derecho de pago dificulta a los pobres; los cuatro años aseguran experiencia, pero retrasan a algunos.",
        ["menciona una ventaja para la ciudad", "menciona un problema para el oficial", "usa las tres reglas dadas", "no juzga con palabras actuales sin explicar"],
        ["texto de seis líneas con ventajas y problemas"],
        ["decir solo ventajas o solo problemas", "olvidar nombrar las reglas"],
        "Cuéntale tu análisis a una persona de tu casa y pídele que diga qué regla le parece más justa y por qué.",
    ),
    "Compara un gremio medieval con una asociación de oficio actual y anota una semejanza y una diferencia.",
    "Averigua qué oficios medievales dieron apellidos comunes, como Herrero o Molinero.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a analizar el surgimiento de las universidades y cómo circularon los saberes. Sirve para entender que el conocimiento viajó por ciudades, lenguas y libros.",
    ["Sé que los saberes pasaron entre el mundo islámico y la Europa latina.", "Sé que la ciudad concentraba actividades nuevas."],
    [
        "Las universidades nacieron entre los siglos XI y XIII, en ciudades que ya tenían maestros y estudiantes. Una universidad era una asociación de maestros y estudiantes con reglas propias, como los gremios. Las más antiguas fueron Bolonia (famosa por el derecho), París (por la teología) y Oxford. La de Salamanca se fundó en 1218.",
        "En las universidades se estudiaba en latín. Primero se cursaba el programa de artes: gramática, retórica, lógica, aritmética, geometría, astronomía y música. Luego se podía seguir derecho, medicina o teología. Se aprendía leyendo textos y debatiendo preguntas con argumentos a favor y en contra. Al terminar, el estudiante recibía un grado, como bachiller o maestro.",
        "Los saberes circulaban. Muchos textos de la Antigüedad, como obras de Aristóteles, llegaron traducidos del árabe y del griego a latín, en ciudades como Toledo. Los estudiantes viajaban de ciudad en ciudad, así que las ideas se movían con ellos. Pero el acceso era limitado: en general solo estudiaban varones, muchos de familias con recursos y vinculados a la Iglesia. Las universidades dependían de permisos de reyes o del papa.",
    ],
    [("universidad", "asociación medieval de maestros y estudiantes con reglas propias"), ("grado", "título que se obtenía al terminar los estudios, como bachiller o maestro"), ("teología", "estudio de la religión y de Dios"), ("retórica", "arte de hablar y escribir con claridad y fuerza"), ("traducción", "paso de un texto a otra lengua"), ("lógica", "estudio del razonamiento correcto")],
    [
        ("Ubicar universidades", "Una ficha de ejemplo dice: «Bolonia era famosa por el derecho y París por la teología». Si alguien quiere estudiar derecho, ¿a cuál iría?", ["Bolonia destacaba por el derecho.", "París destacaba por la teología."], "A Bolonia"),
        ("Seguir un grado", "Un estudiante de ejemplo cursa gramática, retórica y lógica. ¿Qué parte del programa estudia?", ["Esas materias están en el programa de artes.", "Después se podría pasar a derecho, medicina o teología."], "El programa de artes"),
    ],
    [
        ("Creer que cualquiera podía estudiar en una universidad medieval.", "El acceso era limitado: en general varones, con recursos y vinculados a la Iglesia.", "Pregunta quiénes estaban incluidos y quiénes excluidos."),
        ("Pensar que las universidades se crearon solo con saberes europeos.", "Muchos textos llegaron traducidos desde el árabe y el griego.", "Rastrea de dónde viene cada texto."),
    ],
    [
        ("¿En qué lengua se enseñaba en las universidades medievales?", "En latín", "Era la lengua común de los estudios."),
        ("¿Qué universidad, fundada en 1218, se menciona en la clase?", "Salamanca", "La clase la ubica en ese año."),
        ("¿Qué universidad era famosa por el derecho?", "Bolonia", "Se explica en el primer párrafo."),
    ],
    [
        ("¿Qué quiere decir que la universidad era como un gremio?", "Que era una asociación de personas con un mismo objetivo y reglas propias", "Maestros y estudiantes se organizaban con normas comunes."),
        ("Nombra tres materias del programa de artes.", "Tres de estas: gramática, retórica, lógica, aritmética, geometría, astronomía, música", "Son las siete materias del programa de artes."),
        ("¿Quiénes daban permiso para que una universidad funcionara?", "Reyes o el papa", "La explicación lo menciona."),
    ],
    [
        arith("Una universidad de ejemplo tiene 24 estudiantes de derecho, 18 de medicina y 33 de artes. ¿Cuántos estudiantes tiene en total?", "24+18+33", "Se suman los estudiantes de las tres áreas."),
        ("Una ficha de ejemplo dice: «Un texto de Aristóteles fue traducido del árabe al latín en Toledo». ¿Qué mundos participaron en el viaje del texto?", "El mundo islámico (árabe) y la Europa latina", "El texto pasó del árabe al latín."),
        ("Un estudiante de ejemplo viaja de París a Bolonia para estudiar con un maestro. ¿Qué rasgo de la vida universitaria medieval muestra esto?", "Que los estudiantes viajaban de ciudad en ciudad y llevaban ideas", "La explicación lo señala."),
    ],
    [
        ("Pedro dice: «La universidad medieval era igual a la de hoy». Da dos diferencias de la clase.", "Se enseñaba en latín y estaban vinculadas a la Iglesia, con acceso casi solo para varones", "La clase indica lengua y acceso."),
        ("¿Por qué la traducción de libros fue importante para las universidades?", "Porque dio a los maestros textos antiguos que antes no conocían", "Las traducciones ampliaron el contenido de los estudios."),
    ],
    [
        ("Ordena los pasos de un estudiante de ejemplo: A) obtiene un grado, B) estudia artes, C) se especializa en medicina.", "B, C, A", "Primero artes, luego una facultad y al final el grado."),
        ("Una fuente de ejemplo dice: «La universidad de mi ciudad fue fundada gracias a un permiso del rey». ¿Qué dato de la clase explica esto?", "Las universidades dependían de permisos de reyes o del papa", "Sin permiso, la universidad no tenía reconocimiento."),
    ],
    [("Imagina una universidad de ejemplo con tres estudiantes: Juan (familia rica, estudia teología), Marta (hija de un campesino) y Luis (hijo de un notario, estudia derecho). Según la clase, ¿quién tenía más dificultades para estudiar y por qué?", "Marta, porque era mujer e hija de campesinos", "La clase señala que el acceso era limitado en términos de género y recursos.")],
    [("En la unidad de transformaciones europeas, ¿qué es una universidad medieval?", "Una asociación de maestros y estudiantes con reglas propias", "Es la definición del vocabulario."), ("¿En qué ciudad se tradujeron textos del árabe al latín?", "Toledo", "Se menciona en la clase."), ("Nombra una limitación del acceso a la universidad.", "En general solo estudiaban varones con recursos y vinculados a la Iglesia", "Son los límites descritos.")],
    (
        "Elige un estudiante de ejemplo y escribe cinco líneas sobre su camino. Opciones: A) Pedro, hijo de un mercader de Bolonia, quiere estudiar derecho; B) Luis, de familia pobre y que sabe latín, quiere estudiar en París. Indica en qué ciudad estudiaría, qué programa seguiría, qué obstáculos tendría y qué texto o saber podría encontrar.",
        "Pedro estudiaría derecho en Bolonia, después del programa de artes; podría encontrar obras traducidas; su obstáculo sería el costo.",
        ["indica ciudad y programa", "menciona un obstáculo", "menciona un texto o saber", "no inventa instituciones que no estén en la clase"],
        ["párrafo de cinco líneas con los cuatro elementos"],
        ["olvidar el obstáculo", "poner mujeres estudiando sin explicar que era excepcional"],
        "Cuéntale el camino de tu estudiante a una persona de tu casa y pídele que diga qué obstáculo le parece más grande.",
    ),
    "Escribe una semejanza y una diferencia entre una universidad medieval y un colegio de hoy.",
    "Investiga cuándo se fundó la primera universidad de Chile y qué se enseñaba al principio.",
)

# ================================================================ clase 5
lesson(
    OA, 5,
    "Aprenderé a relacionar los cambios del campo, de la ciudad y de la política desde el siglo XII. Sirve para ver que las transformaciones se conectan entre sí.",
    ["Sé que crecieron ciudades, comercio, gremios y universidades.", "Sé distinguir causa y consecuencia."],
    [
        "Los cambios del campo, la ciudad y la política estaban conectados. En el campo, los campesinos usaron arados pesados, molinos y rotación de tres campos, y así se produjo más. Una parte de los campesinos se fue a las ciudades. Otra siguió trabajando tierras de los señores, a quienes pagaba rentas.",
        "En las ciudades creció una nueva clase, la burguesía, con dinero propio. Muchos reyes se aliaron con las ciudades: les daban privilegios y recibían a cambio impuestos y apoyo contra los nobles. Por eso los reyes pudieron gobernar mejor sus reinos y administrar con funcionarios que sabían leer, escribir y calcular, muchos formados en universidades.",
        "Pero estos cambios tuvieron límites. En el siglo XIV, hambrunas y la peste negra (desde 1347) mataron a una parte de la población, y la expansión se detuvo. Además, no todos ganaron: había campesinos que seguían sujetos a un señor, y pobres en las ciudades. Por eso hay que hablar de transformaciones y no de un «progreso» continuo para todos.",
    ],
    [("burguesía", "grupo de habitantes de las ciudades que vivían del comercio, los oficios o las finanzas"), ("renta", "pago que un campesino hacía a un señor por usar la tierra"), ("impuesto", "dinero que se paga al rey o al Estado"), ("privilegio", "derecho especial que se concede a un grupo"), ("peste negra", "epidemia que llegó a Europa en 1347 y mató a muchas personas"), ("transformación", "cambio profundo en una sociedad")],
    [
        ("Conectar cambios", "Un rey de ejemplo concede privilegios a una ciudad y recibe impuestos. ¿Quién gana qué?", ["La ciudad gana derechos.", "El rey gana dinero.", "Ambos ganan algo distinto."], "La ciudad gana derechos y el rey gana impuestos"),
        ("Distinguir causa y efecto", "Datos de ejemplo: más producción agrícola, más campesinos que se van a la ciudad. ¿Cuál es la causa y cuál la consecuencia?", ["Primero hay más producción.", "Luego algunos campesinos pueden irse."], "Causa: más producción; consecuencia: migración a la ciudad"),
    ],
    [
        ("Pensar que todos mejoraron su vida.", "Hubo ganadores y perdedores: campesinos sujetos al señor y pobres de las ciudades.", "Pregunta quién ganó y quién no."),
        ("Creer que la peste negra ocurrió en el siglo XII.", "Llegó a Europa en 1347, en el siglo XIV, y detuvo la expansión.", "Ubica cada hecho en su siglo."),
    ],
    [
        ("¿Qué grupo urbano creció desde el siglo XII con dinero propio?", "La burguesía", "Es el grupo que vivía del comercio, los oficios o las finanzas."),
        ("¿En qué año llegó la peste negra a Europa, según la clase?", "1347", "La clase da esa fecha."),
        ("¿Qué pagaban los campesinos a los señores por usar la tierra?", "Rentas", "Es la definición del vocabulario."),
    ],
    [
        ("¿Por qué los reyes se aliaron con las ciudades?", "Para recibir impuestos y apoyo contra los nobles", "La alianza daba fuerza al rey."),
        ("¿Por qué las universidades ayudaron a los reyes a gobernar mejor?", "Porque formaban funcionarios que sabían leer, escribir y calcular", "Los funcionarios formados administraban el reino."),
        ("¿Qué dos hechos del siglo XIV detuvieron la expansión?", "Las hambrunas y la peste negra", "Son los dos hechos que se mencionan."),
    ],
    [
        arith("Un reino de ejemplo cobraba 200 monedas de impuesto a cada una de 12 ciudades. ¿Cuántas monedas recibía en total?", "200*12", "Se multiplica el impuesto de cada ciudad por el número de ciudades."),
        ("Observa: «El señor X tiene muchos campesinos que no pueden irse de sus tierras». ¿Qué parte de la clase explica que algunos campesinos no se beneficiaron del crecimiento?", "Algunos campesinos seguían sujetos a un señor", "El texto lo menciona como límite."),
        ("Un reino de ejemplo sufre una peste que mata a muchos campesinos y faltan trabajadores en el campo. ¿Qué podría pasar con la producción en los años siguientes?", "Probablemente bajaría", "Con menos trabajadores se cultiva menos."),
    ],
    [
        ("Luis dice: «Después del siglo XII todo mejoró para todos». ¿Qué dos datos de la clase contradicen esa idea?", "Hubo campesinos sujetos al señor y pobres en las ciudades, y en el siglo XIV llegaron hambrunas y peste", "La clase muestra límites del crecimiento."),
        ("Marta dice: «Los reyes dejaron de depender de la nobleza gracias a las ciudades». ¿Qué matiz agregarías?", "Dependieron menos, no completamente; la nobleza seguía teniendo poder", "La alianza con las ciudades fortaleció al rey, pero sin eliminar a los nobles."),
    ],
    [
        ("Ordena esta cadena de cambios: A) las ciudades pagan impuestos al rey, B) hay más producción agrícola, C) crece el comercio, D) el rey contrata funcionarios.", "B, C, A, D", "El campo produce más, crece el comercio, el rey cobra impuestos y con ese dinero contrata funcionarios."),
        ("En un esquema de ejemplo hay tres columnas: campo, ciudad y política. Ubica «arado pesado», «gremios» y «cartas de privilegio» en la columna correcta, en ese orden.", "Campo, ciudad, política", "El arado es del campo, los gremios de la ciudad y los privilegios de la relación con el poder."),
    ],
    [("Un reino de ejemplo cuenta con estos datos: sus ciudades crecen, el rey cobra más impuestos y la peste mata a un tercio de sus campesinos. ¿Cuál es una conclusión prudente?", "El reino creció y luego sufrió una crisis que afectó su economía", "Respeta los datos sin exagerar.")],
    [("En la unidad de transformaciones europeas, ¿qué es la burguesía?", "El grupo de habitantes de las ciudades que vivían del comercio, los oficios o las finanzas", "Es la definición del vocabulario."), ("¿Qué ganaban las ciudades con los privilegios del rey?", "Derechos y autonomía", "Los privilegios les daban libertades."), ("¿Por qué no se habla de «progreso para todos»?", "Porque hubo ganadores y perdedores", "No todos se beneficiaron.")],
    (
        "Escribe un esquema de tres columnas (campo, ciudad, política) y rellénalo con tres cambios en cada columna usando solo datos de la unidad. Después escribe tres líneas diciendo qué cambio del campo causó uno de la ciudad y qué cambio de la ciudad afectó a la política.",
        "Campo: arado pesado, molino, rotación de tres campos. Ciudad: gremios, ferias, universidades. Política: cartas de privilegio, impuestos, funcionarios.",
        ["completa nueve casillas", "usa datos correctos", "explica una relación campo-ciudad", "explica una relación ciudad-política"],
        ["esquema de nueve casillas más tres líneas de explicación"],
        ["poner datos en la columna equivocada", "no explicar la relación"],
        "Muestra tu esquema a una persona de tu casa y pídele que siga una flecha de causa a efecto.",
    ),
    "Escribe una pregunta que no puedas responder con los datos de la unidad y que exigiría otra fuente.",
    "Investiga cómo llegó la peste negra a Europa y qué efectos tuvo en las ciudades.",
)
