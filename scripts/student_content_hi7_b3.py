"""Cuaderno del estudiante, 7.º básico Historia, Geografía y Ciencias Sociales: OA 13 (civilizaciones maya y azteca)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI07 OA 13"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a ubicar en el mapa y en el tiempo a los mayas y a los aztecas. Sirve para no confundir civilizaciones que vivieron en épocas y lugares distintos.",
    ["Sé que Mesoamérica es una región cultural de América.", "Sé calcular cuántos años pasan entre dos fechas."],
    [
        "Mesoamérica es la región de América que incluye el centro y sur de México y parte de Centroamérica. Allí se desarrollaron varias civilizaciones con rasgos comunes: cultivaban maíz, construían pirámides, usaban calendarios y comerciaban. Los mayas ocuparon el sur de México (península de Yucatán), Guatemala, Belice y partes de Honduras y El Salvador. Los aztecas, que se llamaban a sí mismos mexicas, vivieron en el valle de México, en torno a la actual Ciudad de México.",
        "Sus tiempos fueron distintos. El periodo clásico maya va, aproximadamente, del año 250 al 900 d.C., cuando florecieron ciudades como Tikal, Palenque y Copán. Después muchas ciudades del sur se despoblaron, pero los mayas siguieron viviendo, sobre todo en el norte de Yucatán. Los aztecas fundaron Tenochtitlan hacia 1325 en una isla del lago de Texcoco, formaron una alianza con Texcoco y Tlacopan en 1428 y dominaron una gran región hasta 1521, cuando los españoles y sus aliados indígenas tomaron la ciudad.",
        "Por eso los aztecas no son «los mayas de después». Fueron pueblos con idiomas, formas de gobierno y ciudades diferentes, aunque compartieron rasgos mesoamericanos. Para ubicarlos en un mapa conviene recordar: mayas al sur y al este; aztecas en el valle central de México.",
    ],
    [("Mesoamérica", "región cultural que abarca el centro y sur de México y parte de Centroamérica"), ("periodo clásico maya", "época de mayor esplendor de las ciudades mayas, entre los años 250 y 900 d.C."), ("mexica", "nombre con que se llamaban a sí mismos los aztecas"), ("Tenochtitlan", "capital de los aztecas, construida en una isla del lago de Texcoco"), ("civilización", "sociedad compleja con ciudades, gobierno, religión y conocimientos organizados"), ("alianza", "acuerdo entre pueblos o ciudades para actuar juntos")],
    [
        ("Ubicar en el mapa", "Una ficha de ejemplo dice: «Ciudad con pirámides en el valle central de México, construida sobre una isla en un lago». ¿Es maya o azteca?", ["Valle central de México y una isla en un lago.", "Eso describe Tenochtitlan.", "Es azteca."], "Azteca"),
        ("Calcular una duración", "El periodo clásico maya va del año 250 al 900. ¿Cuántos años dura?", ["Se resta 250 de 900.", "900 − 250 = 650."], "650 años"),
    ],
    [
        ("Pensar que mayas y aztecas fueron la misma civilización.", "Vivieron en lugares y épocas distintas y tuvieron idiomas y gobiernos diferentes.", "Pregunta siempre dónde y cuándo."),
        ("Creer que los mayas desaparecieron.", "Muchas ciudades se despoblaron, pero los mayas siguieron viviendo y hoy existen pueblos mayas.", "Distingue entre el fin de una etapa y la desaparición de un pueblo."),
    ],
    [
        ("¿Cómo se llamaban a sí mismos los aztecas?", "Mexicas", "Es el nombre del vocabulario."),
        ("¿Cuál era la capital azteca?", "Tenochtitlan", "Fue construida en una isla del lago de Texcoco."),
        ("¿En qué península del sur de México vivieron los mayas?", "Yucatán", "La explicación la nombra como parte del territorio maya."),
    ],
    [
        ("¿Qué ciudad maya aparece en la lista: Tikal o Tenochtitlan?", "Tikal", "Tenochtitlan es azteca."),
        ("¿Quiénes tomaron Tenochtitlan en 1521?", "Los españoles y sus aliados indígenas", "La explicación indica que no fueron solo los españoles."),
        ("¿Por qué Mesoamérica se llama región «cultural»?", "Porque sus pueblos compartían rasgos, como maíz, pirámides, calendarios y comercio", "No es un país, sino un conjunto de rasgos compartidos."),
    ],
    [
        arith("Los aztecas fundaron Tenochtitlan hacia 1325 y los españoles tomaron la ciudad en 1521. ¿Cuántos años pasaron?", "1521-1325", "Se resta el año de fundación al de la toma."),
        ("Una ficha de ejemplo dice: «El periodo clásico de Tikal fue entre 250 y 900». ¿El año 1400 está dentro de ese periodo?", "No, porque 1400 es posterior a 900", "El periodo clásico termina en el año 900."),
        ("Un mapa de ejemplo muestra puntos en el sur de México y Guatemala y otro en el valle central. ¿Cuál pertenece mayoritariamente a los mayas?", "Los puntos del sur de México y Guatemala", "Los mayas ocuparon esa región."),
    ],
    [
        ("Pedro dice: «Los aztecas construyeron Tikal». ¿Qué dos datos de la clase lo contradicen?", "Tikal es una ciudad maya del sur y de época clásica; los aztecas vivieron en el valle central y fundaron Tenochtitlan hacia 1325", "El lugar y la época son distintos."),
        ("Lucía afirma: «Los mayas dejaron de existir en el año 900». Corrige la afirmación con un dato de la clase.", "Muchas ciudades del sur se despoblaron, pero los mayas siguieron viviendo, sobre todo en el norte de Yucatán", "Un periodo termina, pero el pueblo continúa."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A) fundación de Tenochtitlan, B) esplendor de Tikal, C) toma de Tenochtitlan.", "B, A, C", "Primero el esplendor clásico maya, luego la fundación de Tenochtitlan y por último su toma."),
        arith("La Triple Alianza azteca se formó en 1428. ¿Cuántos años pasaron desde la fundación de Tenochtitlan (1325) hasta la alianza?", "1428-1325", "Se resta 1325 de 1428."),
    ],
    [("Un estudiante lee una ficha de ejemplo: «Pueblo con pirámides, calendario y comercio de cacao, en la península de Yucatán, año 700». ¿Qué civilización describe y en qué periodo?", "Los mayas, en el periodo clásico", "El lugar es Yucatán y el año 700 está dentro de 250–900.")],
    [("En la unidad de mayas y aztecas, ¿qué es Mesoamérica?", "Una región cultural del centro y sur de México y parte de Centroamérica", "Es la definición del vocabulario."), ("¿Dónde fundaron los aztecas Tenochtitlan?", "En una isla del lago de Texcoco", "Así lo dice la explicación."), ("¿Por qué no se pueden mezclar mayas y aztecas?", "Porque vivieron en lugares y épocas distintos, con idiomas y gobiernos diferentes", "Son dos civilizaciones distintas.")],
    (
        "Haz una tabla de dos columnas, «mayas» y «aztecas», y completa tres filas: dónde vivieron, cuándo tuvieron su mayor esplendor, ciudades que conoces. Usa solo datos de la clase. Después escribe una frase que explique por qué no son la misma civilización.",
        "Mayas: sur de México, Guatemala; 250–900 (clásico); Tikal. Aztecas: valle de México; 1325–1521; Tenochtitlan.",
        ["completa seis casillas", "usa datos correctos", "escribe una frase de distinción", "no mezcla fechas"],
        ["tabla de seis casillas y una frase"],
        ["poner fechas aztecas en los mayas", "no incluir ciudades"],
        "Muestra tu tabla a una persona de tu casa y pídele que diga una diferencia clave entre ambos pueblos.",
    ),
    "Dibuja un mapa sencillo de Mesoamérica y ubica con una marca el territorio maya y el azteca.",
    "Averigua cómo se llama hoy el lago donde estaba Tenochtitlan y qué ciudad está sobre él.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a examinar cómo los mayas y los aztecas cultivaron y transformaron el territorio. Sirve para entender cómo se adaptaron a selvas, montañas y lagos.",
    ["Sé que maíz, frijol y zapallo fueron alimentos de América.", "Sé que las personas cambian su entorno para vivir."],
    [
        "Los mayas y los aztecas cultivaban maíz, frijol y zapallo (o calabaza), que se complementan: el maíz da energía, el frijol da proteínas y el zapallo cubre el suelo. Los mayas practicaban la milpa: cultivo de maíz asociado con otras plantas. También construían terrazas en las laderas, campos elevados en terrenos húmedos y depósitos de agua para la época seca.",
        "Los aztecas desarrollaron las chinampas, que eran islas artificiales para cultivar construidas en lagos poco profundos con barro, vegetación y estacas. En ellas producían maíz, frijol, calabaza y flores, a veces con varias cosechas al año. En la ciudad de Tenochtitlan, sobre una isla, construyeron calzadas (caminos elevados) que la unían a la orilla, diques para controlar el agua y acueductos que traían agua dulce.",
        "Estas obras muestran adaptación al ambiente: en lugar de abandonar terrenos difíciles, los transformaron. Pero también se sabe que algunas ciudades mayas del sur sufrieron sequías y desgaste del suelo hacia el año 900. Por eso hay que hablar de una relación compleja entre sociedades y ambiente, con éxitos y problemas.",
    ],
    [("milpa", "cultivo de maíz junto con frijol y zapallo"), ("chinampa", "isla artificial de cultivo construida en un lago"), ("terraza", "escalón de tierra construido en una ladera para cultivar"), ("calzada", "camino elevado que cruza un lago o terreno bajo"), ("acueducto", "construcción que lleva agua de un lugar a otro"), ("adaptación", "cambio que hace una sociedad para vivir en un ambiente")],
    [
        ("Elegir la técnica", "Un pueblo vive junto a un lago poco profundo y quiere más tierra de cultivo. ¿Qué técnica azteca de la clase le sirve?", ["Necesita tierra sobre el agua.", "Las chinampas son islas artificiales."], "Chinampas"),
        ("Explicar la milpa", "¿Por qué el maíz, el frijol y el zapallo se cultivan juntos en la milpa?", ["El maíz da energía.", "El frijol da proteínas.", "El zapallo cubre el suelo."], "Porque se complementan"),
    ],
    [
        ("Creer que las chinampas flotaban sin estar fijas.", "Eran islas de barro y vegetación sujetas con estacas en un lago poco profundo.", "Describe cómo se construían."),
        ("Pensar que la adaptación fue siempre perfecta.", "También hubo sequías y desgaste del suelo, sobre todo en el sur maya hacia el 900.", "Menciona éxitos y problemas."),
    ],
    [
        ("¿Qué cultivo base de Mesoamérica forma la milpa junto con frijol y zapallo?", "El maíz", "Es el cultivo principal de la milpa."),
        ("¿Cómo se llamaba el camino elevado que unía Tenochtitlan con la orilla?", "Calzada", "Es la definición del vocabulario."),
        ("¿Qué construían los mayas en las laderas para cultivar?", "Terrazas", "Escalones de tierra en la ladera."),
    ],
    [
        ("¿Para qué servían los depósitos de agua de los mayas?", "Para tener agua durante la época seca", "Permitían guardar el agua de lluvia."),
        ("¿Qué obra de Tenochtitlan traía agua dulce?", "Los acueductos", "Llevaban agua desde fuentes a la ciudad."),
        ("¿Por qué se dice que las chinampas son una adaptación al lago?", "Porque aprovechan el lago para cultivar en vez de dejarlo sin uso", "Convierten un terreno difícil en tierra de cultivo."),
    ],
    [
        arith("Una chinampa de ejemplo mide 30 m de largo y 4 m de ancho. ¿Cuántos metros cuadrados tiene?", "30*4", "Área del rectángulo: largo por ancho.", " m²"),
        ("Un campesino de ejemplo cultiva solo maíz año tras año y su suelo se desgasta. ¿Qué práctica de la clase le ayudaría?", "Cultivar maíz junto con frijol y zapallo, como en la milpa", "La milpa combina cultivos que se complementan."),
        ("Una ciudad maya de ejemplo del sur sufre varios años de sequía. ¿Qué obra de la clase le habría servido para aguantar mejor?", "Depósitos de agua", "Guardan agua para cuando falta."),
    ],
    [
        ("Julia dice: «Los mayas y aztecas destruían su ambiente sin pensar». ¿Qué dato de la clase la contradice?", "Construyeron terrazas, chinampas y depósitos de agua para adaptarse", "Esas obras muestran adaptación."),
        ("Mario dice: «Las técnicas de cultivo nunca fallaron». ¿Qué dato de la clase lo contradice?", "Hubo sequías y desgaste del suelo en el sur maya hacia el 900", "Las técnicas tuvieron límites."),
    ],
    [
        ("¿Cuál modifica más el paisaje: una milpa en un claro o las calzadas, diques y acueductos de una ciudad en un lago?", "Las calzadas, diques y acueductos", "Son obras de gran escala que cambian el lago y su entorno."),
        arith("Un agricultor tiene 6 chinampas y cosecha 3 veces al año en cada una. ¿Cuántas cosechas en total consigue en un año?", "6*3", "Se multiplica el número de chinampas por las cosechas de cada una."),
    ],
    [("Una ficha de ejemplo dice: «Pueblo en una ladera con poca tierra plana: construye escalones de tierra para sembrar maíz». ¿Qué técnica usa y qué civilización la practicó?", "Terrazas, que usaron los mayas", "Las terrazas están entre las técnicas mayas de la clase.")],
    [("En la unidad de mayas y aztecas, ¿qué es una chinampa?", "Una isla artificial de cultivo construida en un lago", "Es la definición del vocabulario."), ("En la unidad de mayas y aztecas, ¿qué es una milpa?", "Un cultivo de maíz junto con frijol y zapallo", "Es la definición del vocabulario."), ("¿Por qué no todo fue éxito?", "Porque hubo sequías y desgaste del suelo", "Hubo problemas ambientales.")],
    (
        "Elige un ambiente y propón una técnica de la clase para cultivarlo: A) una ladera con mucha pendiente; B) un lago poco profundo; C) una selva con mucha lluvia pero sin agua en la época seca. Explica cómo funcionaría, qué cultivarías y qué problema podría aparecer.",
        "B: construiría chinampas con barro y vegetación; cultivaría maíz y flores; el problema sería mantener el nivel del agua.",
        ["elige una técnica adecuada", "explica cómo funciona", "nombra un cultivo", "menciona un posible problema"],
        ["párrafo de cinco líneas con los cuatro elementos"],
        ["usar una técnica que no corresponde al ambiente", "no mencionar problemas"],
        "Cuéntale tu propuesta a una persona de tu casa y pídele que diga qué parte le parece más ingeniosa.",
    ),
    "Dibuja una chinampa en corte lateral y rotula agua, barro, vegetación y estacas.",
    "Averigua si hoy se cultivan chinampas en la Ciudad de México y dónde.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a analizar cómo se organizaban política y urbanamente las ciudades mayas y aztecas. Sirve para entender quién mandaba y cómo era una ciudad mesoamericana.",
    ["Sé que una ciudad puede ser capital de un Estado.", "Sé que un gobierno cobra tributos."],
    [
        "Las ciudades mayas del periodo clásico eran ciudades-Estado: cada una tenía su gobernante, llamado ajaw, y su territorio. A veces se aliaban y otras veces se enfrentaban en guerras. Había nobles, sacerdotes, artesanos, campesinos y esclavos. En el centro de la ciudad se levantaban templos-pirámide, palacios, plazas y canchas para el juego de pelota.",
        "Los aztecas formaron un imperio. En 1428 Tenochtitlan, Texcoco y Tlacopan formaron la Triple Alianza y dominaron a muchos pueblos que debían pagar tributos en alimentos, telas y otros bienes. El gobernante de Tenochtitlan se llamaba tlatoani. La sociedad se dividía en nobles, guerreros, sacerdotes, comerciantes (pochteca), artesanos, campesinos y esclavos.",
        "Tenochtitlan era una ciudad grande y planificada, con una plaza central, el Templo Mayor, mercados, canales y calzadas. Cuando llegaron los españoles en 1519 la describieron con admiración. Para ambas civilizaciones hay que recordar que muchos datos vienen de inscripciones, códices y relatos escritos después por españoles, de modo que la información tiene límites.",
    ],
    [("ciudad-Estado", "ciudad con gobierno propio que controla un territorio"), ("ajaw", "gobernante de una ciudad maya"), ("tlatoani", "gobernante de Tenochtitlan"), ("tributo", "pago en bienes o trabajo que un pueblo dominado entrega"), ("Triple Alianza", "alianza de Tenochtitlan, Texcoco y Tlacopan, formada en 1428"), ("Templo Mayor", "gran templo en el centro de Tenochtitlan")],
    [
        ("Clasificar la organización", "Ficha de ejemplo: «Cada ciudad tiene su propio gobernante y a veces guerrean entre ellas». ¿Es una organización de ciudades-Estado o de imperio?", ["Hay varios gobernantes independientes.", "Eso es una ciudad-Estado."], "Ciudades-Estado"),
        ("Reconocer un título", "Una ficha de ejemplo dice: «Murió el gobernante de Tenochtitlan y eligieron a su sucesor». ¿Qué título tenía ese gobernante?", ["Tenochtitlan era la capital azteca.", "El título del vocabulario para su gobernante es tlatoani."], "Tlatoani"),
    ],
    [
        ("Creer que todos los mayas estaban unidos bajo un solo emperador.", "Eran ciudades-Estado independientes, con alianzas y guerras.", "Pregunta si hay un solo gobierno o varios."),
        ("Pensar que el tributo era voluntario.", "Era un pago exigido a pueblos dominados.", "Pregunta quién manda y quién paga."),
    ],
    [
        ("¿Cómo se llamaba el gobernante de una ciudad maya?", "Ajaw", "Está en el vocabulario."),
        ("¿Qué tres ciudades formaron la Triple Alianza?", "Tenochtitlan, Texcoco y Tlacopan", "La explicación las menciona."),
        ("¿En qué año se formó la Triple Alianza?", "1428", "La explicación da ese año."),
    ],
    [
        ("¿Quiénes eran los pochteca?", "Los comerciantes aztecas", "La explicación los menciona dentro de la sociedad."),
        ("¿Qué entregaban los pueblos dominados al imperio azteca?", "Tributos en alimentos, telas y otros bienes", "Pagaban lo que el Estado les exigía."),
        ("Nombra dos construcciones del centro de una ciudad maya.", "Dos de estas: templos-pirámide, palacios, plazas, canchas de juego de pelota", "Son las construcciones de la clase."),
    ],
    [
        ("Una fuente de ejemplo dice: «Cada seis meses llega una caravana con maíz, tela de algodón y plumas desde un pueblo conquistado a Tenochtitlan». ¿Qué institución muestra?", "El tributo", "El pueblo conquistado entrega bienes a la capital."),
        ("Una plaza con pirámide y palacio, en una ciudad con varios gobernantes independientes en la región. ¿Es más probable que sea maya clásica o del imperio azteca?", "Maya clásica", "Las ciudades-Estado eran propias del mundo maya clásico."),
        arith("Una ciudad de ejemplo debe entregar cada año 400 cargas de maíz y 120 cargas de tela. ¿Cuántas cargas entrega en total?", "400+120", "Se suman las cargas de ambos bienes."),
    ],
    [
        ("Ana afirma: «El imperio azteca y las ciudades mayas se organizaban igual». Da un dato que la contradiga.", "Los mayas eran ciudades-Estado independientes y los aztecas formaron un imperio con tributos", "Es una diferencia de organización."),
        ("Pedro dice: «Sabemos todo de Tenochtitlan porque los españoles la describieron». ¿Qué advertencia hace la clase?", "Los relatos escritos después por españoles tienen límites y sesgos", "Hay que contrastar con códices y arqueología."),
    ],
    [
        ("Ordena de la menor a la mayor concentración de poder en una sola ciudad: A) ciudad-Estado maya, B) capital del imperio azteca.", "A, B", "El imperio concentraba más poder y tributo en Tenochtitlan."),
        ("Una afirmación dice: «Tenochtitlan era una ciudad planificada». ¿Qué dos elementos de la clase la apoyan?", "Plaza central y Templo Mayor, mercados, canales y calzadas", "Esos elementos muestran una organización ordenada."),
    ],
    [("Un estudiante lee que una ciudad de ejemplo paga tributo, tiene un tlatoani y un Templo Mayor. ¿Qué civilización describe?", "La azteca", "Son rasgos de la clase para Tenochtitlan.")],
    [("En la unidad de mayas y aztecas, ¿qué es una ciudad-Estado?", "Una ciudad con gobierno propio que controla un territorio", "Es la definición del vocabulario."), ("En la unidad de mayas y aztecas, ¿qué es un tributo?", "Un pago en bienes o trabajo que entrega un pueblo dominado", "Es la definición del vocabulario."), ("¿Por qué hay que tener cuidado con los relatos de los españoles?", "Porque fueron escritos después y desde su perspectiva", "Tienen sesgos y límites.")],
    (
        "Completa una tabla comparativa con estas filas: gobernante, tipo de organización política, edificios centrales, quién paga tributo. Columnas: ciudad maya clásica y Tenochtitlan. Usa solo datos de la clase y escribe «no sé con certeza» donde falte información. Luego escribe una frase que explique la mayor diferencia política.",
        "Gobernante: ajaw / tlatoani. Organización: ciudad-Estado / imperio. Edificios: templos-pirámide, palacios, juego de pelota / Templo Mayor, mercados, calzadas. Tributo: no sé con certeza / pueblos dominados.",
        ["completa ocho casillas", "usa datos correctos", "admite lo que no sabe", "explica una diferencia política"],
        ["tabla de ocho casillas y una frase"],
        ["inventar datos", "confundir ajaw con tlatoani"],
        "Muestra tu tabla a una persona de tu casa y pídele que mire dónde dijiste «no sé con certeza».",
    ),
    "Dibuja el plano de una plaza central con un templo, un palacio y una cancha, y rotula cada parte.",
    "Averigua qué es el juego de pelota mesoamericano y cuál era su importancia ritual.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a comparar las tecnologías, el intercambio y el conocimiento de los mayas y los aztecas. Sirve para ver cómo la red comercial unió a Mesoamérica.",
    ["Sé que el comercio conecta lugares distintos.", "Sé que una técnica puede resolver un problema práctico."],
    [
        "Los mayas y los aztecas no usaron la rueda para transportar carga ni animales de tiro: transportaban los productos a pie, con cargadores, o en canoas por ríos y lagos. Sí usaron la rueda en juguetes. Trabajaron la piedra, la obsidiana (un vidrio volcánico muy filoso) y el hueso; hacían tejidos de algodón y cerámica. No tenían herramientas de hierro.",
        "Una red comercial vinculaba a Mesoamérica. Circulaban cacao, sal, algodón, jade, obsidiana y plumas del quetzal. Los mayas usaban caminos blancos llamados sacbeob y rutas por el mar. Los comerciantes aztecas, los pochteca, viajaban lejos y también espiaban para el Estado. El cacao y las telas servían como dinero en los mercados, como el de Tlatelolco, vecino a Tenochtitlan.",
        "También compartían conocimientos: los mayas escribían con glifos y llevaron un calendario muy preciso; los aztecas usaban un calendario parecido, de 365 y 260 días. Comparar tecnologías no es decidir cuál civilización fue más avanzada, sino ver qué problema resolvía cada una. Para sus ambientes, esas técnicas eran muy eficaces.",
    ],
    [("obsidiana", "vidrio volcánico muy filoso, usado para herramientas y armas"), ("cacao", "semilla que se usaba para preparar bebidas y como dinero"), ("sacbé", "camino blanco de piedra de los mayas"), ("pochteca", "comerciantes aztecas de larga distancia"), ("glifo", "signo de la escritura maya"), ("red comercial", "conjunto de rutas y mercados que conectaban lugares")],
    [
        ("Identificar un producto", "Un comerciante de ejemplo lleva semillas que sirven para preparar una bebida y también como moneda. ¿Qué producto es?", ["Se usa como bebida y dinero.", "Es el cacao."], "Cacao"),
        ("Aplicar la tecnología", "Un grupo necesita transportar cargas desde un lago hasta la costa y no tiene animales de tiro. ¿Qué medio de la clase puede usar en el lago?", ["No usan carretas.", "Usan canoas en ríos y lagos."], "Canoas"),
    ],
    [
        ("Decir que no tenían tecnología porque no usaron rueda para carga.", "Resolvían el transporte con cargadores y canoas y tenían otras tecnologías avanzadas.", "Pregunta qué problema resolvía cada técnica."),
        ("Pensar que la red comercial era solo de cercanía.", "Unía lugares distantes de Mesoamérica con rutas y mercados.", "Ubica en el mapa el origen de cada producto."),
    ],
    [
        ("¿Qué vidrio volcánico usaban para herramientas?", "Obsidiana", "Está en el vocabulario."),
        ("¿Cómo se llamaban los comerciantes aztecas de larga distancia?", "Pochteca", "Está en el vocabulario."),
        ("¿Cómo se llamaban los caminos blancos de los mayas?", "Sacbeob", "Plural de sacbé."),
    ],
    [
        ("¿Por qué las telas y el cacao servían como dinero?", "Porque eran valorados y todos los aceptaban en los mercados", "Una moneda necesita que todos la acepten."),
        ("¿Qué mercado vecino a Tenochtitlan se menciona?", "Tlatelolco", "Aparece en la explicación."),
        ("¿Qué dos productos de la clase eran de uso ritual o de lujo y venían de lejos?", "Jade y plumas de quetzal", "Eran bienes valiosos del comercio."),
    ],
    [
        ("Un comerciante de ejemplo lleva obsidiana, sal y plumas del quetzal. ¿Qué muestra su carga sobre Mesoamérica?", "Una red comercial que conectaba regiones distintas", "Cada producto viene de una zona diferente."),
        arith("Un pochteca sale con 8 cargadores y cada uno lleva 25 kilogramos de carga. ¿Cuántos kilogramos transporta la expedición?", "8*25", "Se multiplica el número de cargadores por la carga de cada uno.", " kg"),
        ("Una ficha de ejemplo dice: «Se usó una rueda en juguetes mayas pero no en transporte». ¿Qué conclusión limitada permite?", "Que conocían la rueda pero no la usaban en transporte", "La ficha solo dice dónde se usó la rueda."),
    ],
    [
        ("Julián dice: «Como no tenían herramientas de hierro, los mayas y aztecas eran menos avanzados». ¿Qué respuesta de la clase le darías?", "Cada civilización resolvía sus problemas con las técnicas y materiales que tenía; no se compara con un solo criterio", "Comparar no es jerarquizar."),
        ("Andrea sostiene que las civilizaciones mesoamericanas no se comunicaban entre sí. Cita un dato que la contradice.", "Circulaban cacao, sal, jade y obsidiana por una red comercial", "La red comercial muestra contacto."),
    ],
    [
        ("Ordena el viaje de una pieza de jade: A) llega a una ciudad maya, B) se extrae en una zona, C) se vende en un mercado.", "B, C, A", "Primero se extrae, luego se vende y al final llega a la ciudad donde se usa."),
        ("Una afirmación dice: «El calendario maya y el azteca eran idénticos». ¿Qué dato de la clase la matiza?", "Eran parecidos, con ciclos de 365 y 260 días, pero no idénticos", "La clase los llama parecidos y no iguales."),
    ],
    [("Un mercado de ejemplo ofrece: cacao, telas, plumas, obsidiana, sal. Un visitante dice que todos esos productos eran locales de un solo pueblo. ¿Qué información de la clase puede corregirlo?", "Que las rutas comerciales traían productos de distintas regiones", "Una red comercial vinculaba áreas.")],
    [("En la unidad de mayas y aztecas, ¿qué es la obsidiana?", "Un vidrio volcánico muy filoso", "Es la definición del vocabulario."), ("¿Qué producto servía como dinero además de las telas?", "El cacao", "La explicación lo dice."), ("¿Por qué no hay que decir que una civilización fue «más avanzada»?", "Porque cada una resolvió problemas distintos con sus recursos", "No hay un único criterio.")],
    (
        "Imagina que eres un pochteca. Escribe un diario de seis líneas con un viaje desde Tenochtitlan hasta el mundo maya. Incluye: dos productos que llevas, uno que traes de vuelta, el medio de transporte, un mercado y un peligro. Usa solo productos y medios de la clase.",
        "Salí de Tenochtitlan con telas y obsidiana; viajamos a pie con cargadores; en un mercado cambié por cacao; el camino era largo y había peligro de asaltos.",
        ["incluye dos productos de ida y uno de regreso", "menciona el medio de transporte", "menciona un mercado o ciudad", "menciona un peligro"],
        ["diario de seis líneas con los cinco elementos"],
        ["inventar productos o medios que no están en la clase", "poner animales de tiro"],
        "Lee tu diario a una persona de tu casa y pídele que diga qué parte le dio más imagen del viaje.",
    ),
    "Haz una lista de cinco productos mesoamericanos y anota para qué servía cada uno.",
    "Averigua qué productos de Mesoamérica llegaron a Europa y qué usos tienen hoy.",
)

# ================================================================ clase 5
lesson(
    OA, 5,
    "Aprenderé a reconocer la diversidad dentro de los mayas y los aztecas y los límites de las fuentes. Sirve para no hablar de «los mayas» o «los aztecas» como si fueran todos iguales.",
    ["Sé que una fuente tiene autor y fecha.", "Sé que dentro de un mismo pueblo hay diferencias."],
    [
        "Cada civilización tenía diversidad interna. Los mayas hablaban muchas lenguas, como el yucateco, y vivían en distintas ciudades-Estado, con costumbres propias. Había nobles, artesanos, campesinos y esclavos. El imperio azteca incluía pueblos distintos, como los tlaxcaltecas, que se resistieron a los mexicas y luego se aliaron con los españoles en 1519.",
        "Hoy se conocen estas civilizaciones por varias fuentes: restos de edificios, tumbas y objetos (arqueología), inscripciones en piedra, códices (libros pintados) y textos escritos por españoles y por indígenas después de la conquista. Cada fuente tiene límites. Muchos códices mayas fueron destruidos, y se conservan pocos. Los cronistas españoles escribieron desde su mirada y a veces para justificar la conquista.",
        "Por eso conviene hablar con cuidado: «según las fuentes disponibles». También se deben reconocer las voces actuales de pueblos maya y nahua, que viven en México y Centroamérica y mantienen lenguas y tradiciones. Una explicación justa muestra diversidad, usa varias fuentes y no convierte a un pueblo en un estereotipo.",
    ],
    [("diversidad interna", "diferencias entre grupos dentro de un mismo pueblo o civilización"), ("códice", "libro pintado o escrito por pueblos mesoamericanos"), ("arqueología", "ciencia que estudia restos materiales del pasado"), ("estereotipo", "imagen simple y repetida que oculta las diferencias"), ("cronista", "persona que escribe la historia de su tiempo"), ("nahua", "pueblo que habla náhuatl, la lengua de los aztecas")],
    [
        ("Reconocer la diversidad", "Dato: los tlaxcaltecas eran enemigos de los mexicas y se aliaron con los españoles en 1519. ¿Qué muestra eso sobre el mundo azteca?", ["Hay dos pueblos con intereses opuestos.", "Había pueblos distintos y no todos estaban de acuerdo."], "Que dentro del imperio y a su alrededor había pueblos con intereses distintos"),
        ("Distinguir fuentes", "¿Una tumba con jade excavada por arqueólogos es una fuente escrita o material?", ["Es un objeto.", "Se estudia con arqueología."], "Material"),
    ],
    [
        ("Hablar de «el maya» o «el azteca» como si fuera una sola persona.", "Dentro de cada pueblo había nobles, campesinos, artesanos y otras diferencias.", "Nombra el grupo del que hablas."),
        ("Creer que lo que dicen los cronistas españoles es toda la verdad.", "Escribieron desde su mirada y a veces para justificar la conquista.", "Contrasta con códices, tumbas y voces actuales."),
    ],
    [
        ("¿Qué ciencia estudia los restos materiales del pasado?", "La arqueología", "Está en el vocabulario."),
        ("En la unidad de mayas y aztecas, ¿qué es un códice?", "Un libro pintado o escrito por pueblos mesoamericanos", "Es la definición del vocabulario."),
        ("¿Cómo se llamaban los pueblos que hablaban náhuatl?", "Nahuas", "Está en el vocabulario."),
    ],
    [
        ("¿Por qué se conservan pocos códices mayas?", "Porque muchos fueron destruidos", "La explicación lo dice."),
        ("Nombra dos tipos de fuentes sobre mayas y aztecas.", "Dos de estas: restos materiales, inscripciones, códices, textos de españoles o indígenas", "Son las fuentes mencionadas."),
        ("¿Por qué se recomienda decir «según las fuentes disponibles»?", "Porque faltan datos y las fuentes tienen límites", "Evita afirmar más de lo que se sabe."),
    ],
    [
        ("Un cronista español de ejemplo escribió: «Los indios eran bárbaros». ¿Qué pregunta debes hacer a esa fuente?", "Desde qué mirada y con qué propósito escribió", "El cronista escribía desde su perspectiva."),
        ("Un testimonio de ejemplo de una comunidad maya actual dice que su lengua se enseña en las escuelas de la comunidad. ¿Qué muestra?", "Que las lenguas mayas siguen vivas", "Es un dato del presente."),
        ("Un estudiante lee que los mayas hablaban distintas lenguas. ¿Qué error evita al decir «los mayas hablaban una sola lengua»?", "Simplificar la diversidad lingüística", "Había muchas lenguas mayas."),
    ],
    [
        ("Marta dice: «Los mexicas y los tlaxcaltecas eran el mismo pueblo». Da un dato de la clase que lo contradiga.", "Los tlaxcaltecas se resistieron a los mexicas y se aliaron con los españoles", "Eran pueblos distintos con intereses opuestos."),
        ("¿Por qué las voces actuales de pueblos maya y nahua son importantes para entender el pasado?", "Porque mantienen lenguas y tradiciones y pueden aportar otra mirada", "Son fuentes vivas y no solo objeto de estudio."),
    ],
    [
        ("Ordena de la fuente más cercana al hecho a la más lejana: A) inscripción en piedra de la época, B) texto de un cronista escrito décadas después, C) libro moderno.", "A, B, C", "La inscripción es contemporánea; el cronista escribe después; el libro moderno es lo más tardío."),
        ("Una afirmación dice: «Todos los mayas fueron destruidos en 900». Corrígela usando un dato de la clase.", "Muchas ciudades del sur se despoblaron, pero los mayas siguieron viviendo y hoy existen", "La afirmación confunde un cambio de etapa con una desaparición."),
    ],
    [("Un estudiante escribe «Los mayas y aztecas eran crueles». ¿Cuál es una forma más justa de decirlo, según la clase?", "Describir hechos concretos con fuentes y mencionar la diversidad y los límites", "Se evita el estereotipo.")],
    [("En la unidad de mayas y aztecas, ¿qué es un estereotipo?", "Una imagen simple y repetida que oculta las diferencias", "Es la definición del vocabulario."), ("En la unidad de mayas y aztecas, ¿qué es diversidad interna?", "Diferencias entre grupos dentro de un mismo pueblo", "Es la definición del vocabulario."), ("¿Por qué se recomienda usar varias fuentes?", "Para contrastar y no depender de una sola mirada", "Cada fuente tiene límites.")],
    (
        "Escribe un texto de siete líneas titulado «Lo que sabemos y lo que no sabemos de los mayas y aztecas». Incluye: dos diferencias dentro de un pueblo, dos tipos de fuentes, un límite de una fuente y una pregunta que quedó sin responder. Usa solo datos de la unidad.",
        "Diferencias: los mayas hablaban varias lenguas y vivían en ciudades-Estado distintas. Fuentes: arqueología y códices. Límite: muchos códices fueron destruidos. Pregunta: ¿qué decían?",
        ["incluye dos diferencias internas", "incluye dos tipos de fuentes", "incluye un límite", "incluye una pregunta pendiente"],
        ["texto de siete líneas con los cuatro elementos"],
        ["generalizar a todos los mayas o aztecas", "no incluir límites"],
        "Léele tu texto a una persona de tu casa y pídele que diga qué fue lo más sorprendente.",
    ),
    "Anota dos formas de hablar de los mayas o aztecas que evitarían estereotipos.",
    "Averigua qué lenguas mayas se hablan hoy y en qué países.",
)
