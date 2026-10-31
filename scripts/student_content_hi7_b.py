"""Cuaderno del estudiante, 7.º básico Historia, Geografía y Ciencias Sociales: OA 11 (Europa, Bizancio e Islam medieval)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI07 OA 11"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a ubicar en el mapa y en el tiempo tres mundos de la Edad Media: el europeo latino, el bizantino y el islámico. Sirve para entender cómo se conectaron antes de estudiar sus encuentros.",
    ["Sé leer una línea de tiempo y distinguir siglos.", "Sé que una fuente tiene autor, fecha y lugar."],
    [
        "La Edad Media europea abarca más o menos desde el año 500 hasta el 1500 d.C. En esos siglos convivieron tres grandes mundos alrededor del mar Mediterráneo. La Europa latina, en el oeste, tenía su centro religioso en Roma y seguía al papa. El Imperio bizantino, en el este, tenía su capital en Constantinopla (hoy Estambul) y hablaba griego. El mundo islámico nació en Arabia en el siglo VII y se extendió por Medio Oriente, el norte de África y gran parte de la península ibérica.",
        "Una cronología simple ayuda a ordenar los hechos: en 622 se inicia el calendario islámico (la Hégira); en 711 ejércitos musulmanes llegan a la península ibérica; en 1054 se divide el cristianismo entre Roma y Constantinopla; en 1204 los cruzados saquean Constantinopla; en 1453 la ciudad cae en poder de los otomanos; en 1492 cae Granada, el último reino musulmán de la península.",
        "Estos mundos no estaban aislados. El mar Mediterráneo y las rutas terrestres los unían: por ellos viajaban mercaderes, ejércitos, peregrinos y libros. Un mapa muestra cercanía y rutas, pero no dice por sí solo si la relación fue de comercio, de guerra o de ambas. Por eso hay que mirar siempre la fecha y la procedencia de cada fuente.",
    ],
    [("Edad Media", "periodo de la historia europea entre los años 500 y 1500 aproximadamente"), ("Bizancio", "Imperio romano de Oriente, con capital en Constantinopla y cultura griega"), ("islam", "religión nacida en Arabia en el siglo VII; también nombra el mundo que se formó a su alrededor"), ("cristiandad", "conjunto de territorios y pueblos de religión cristiana"), ("península ibérica", "territorio donde hoy están España y Portugal"), ("cronología", "orden de los hechos según cuándo ocurrieron")],
    [
        ("Ubicar una fuente", "Una ficha de ejemplo dice: «Crónica escrita en Constantinopla, siglo XI». ¿A qué mundo pertenece su autor y en qué siglo la escribió?", ["Constantinopla era la capital de Bizancio.", "La ficha entrega el siglo: XI."], "Mundo bizantino, siglo XI"),
        ("Ordenar hechos", "Ordena de más antiguo a más reciente: caída de Granada (1492), llegada a la península ibérica (711), caída de Constantinopla (1453).", ["Compara las fechas: 711 es la menor.", "Luego 1453 y al final 1492."], "711, 1453, 1492"),
    ],
    [
        ("Pensar que la Edad Media fue solo europea.", "En esos mismos siglos Bizancio y el mundo islámico tenían grandes ciudades, estados y saberes.", "Ubica siempre los tres mundos en el mapa del Mediterráneo."),
        ("Creer que cercanía en el mapa significa amistad o guerra.", "El mapa solo muestra distancias y rutas; la relación hay que probarla con fuentes.", "Pregunta qué fuente muestra el tipo de relación."),
    ],
    [
        ("Un mapa de ejemplo marca Roma, Constantinopla, Córdoba y Bagdad. ¿Cuál de esas ciudades era la capital del Imperio bizantino?", "Constantinopla", "Era la capital del imperio de cultura griega en el este."),
        ("¿Qué mundo medieval tenía su centro religioso en Roma, bajo el papa: el europeo latino o el islámico?", "El europeo latino", "Roma era la sede del papa, jefe de la Iglesia latina."),
        ("Ordena de más antiguo a más reciente: A = división del cristianismo (1054), B = Hégira (622), C = llegada a la península ibérica (711).", "B, C, A", "Las fechas en orden son 622, 711 y 1054."),
    ],
    [
        ("Una crónica fue escrita en 1130 por un monje de París. ¿A qué mundo pertenece su autor y en qué siglo se escribió?", "Al mundo europeo latino; siglo XII", "París era cristiana latina y 1130 queda entre 1101 y 1200, el siglo XII."),
        ("¿Qué actual país europeo ocupa la península ibérica junto con Portugal?", "España", "La península ibérica la comparten España y Portugal."),
        ("¿Por qué el Mediterráneo sirvió para conectar a los tres mundos medievales?", "Porque sus costas permitían viajar y comerciar entre ellos", "Un mar interior comunica las costas de varios territorios."),
    ],
    [
        arith("Los cruzados saquearon Constantinopla en 1204 y los otomanos la conquistaron en 1453. ¿Cuántos años pasaron entre ambos hechos?", "1453-1204", "Se resta el año menor al mayor."),
        ("Una ficha de ejemplo dice: «Mercader de Venecia compra seda en Constantinopla». ¿Qué dos mundos conecta ese dato?", "El europeo latino y el bizantino", "Venecia era una ciudad latina y Constantinopla, bizantina."),
        ("Un viajero de la Córdoba musulmana quiere llegar a Constantinopla por la ruta más corta de agua. ¿Qué mar debe recorrer en la mayor parte del trayecto?", "El Mediterráneo", "Une las costas de la península ibérica con las de Bizancio."),
    ],
    [
        ("Alicia dice: «Bizancio y el islam existieron al mismo tiempo, así que nunca se conocieron». ¿Qué error comete?", "Existir al mismo tiempo y en regiones vecinas permitía el contacto: comerciaron y también se enfrentaron", "La coincidencia en tiempo y espacio abre la posibilidad de relación."),
        ("Una fuente bizantina es del siglo XII y otra, de Córdoba, del siglo X. ¿Por qué no conviene compararlas sin mirar sus fechas?", "Porque entre ambas pasaron cerca de dos siglos y el contexto cambió", "Los hechos y las condiciones de cada época eran distintos."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = caída de Granada (1492), B = división del cristianismo (1054), C = Hégira (622), D = caída de Constantinopla (1453).", "C, B, D, A", "Las fechas en orden son 622, 1054, 1453 y 1492."),
        arith("Desde la llegada a la península ibérica (711) hasta la caída de Granada (1492), ¿cuántos años pasaron?", "1492-711", "Se resta el año de inicio al de término."),
    ],
    [("Un mapa de ejemplo muestra la ruta Venecia – Constantinopla – Alejandría – Córdoba. Un estudiante concluye: «Esos lugares formaban una sola civilización». ¿Qué sí permite concluir el mapa?", "Que esos lugares estaban conectados por rutas, no que fueran una sola civilización", "Un mapa de rutas muestra conexión, no unidad cultural.")],
    [("¿Qué mundo medieval nació en Arabia en el siglo VII?", "El islámico", "La Hégira (622) inicia el calendario islámico."), ("¿Cuál era la capital del Imperio bizantino?", "Constantinopla", "Esa ciudad, hoy Estambul, era el centro del imperio."), ("Si una fuente dice «año 1453», ¿qué dato falta para ubicarla bien en el mundo medieval?", "Dónde se escribió y quién la escribió", "La procedencia sitúa la fuente en su mundo y su perspectiva.")],
    (
        "Elige uno de estos dos casos y escribe cuatro líneas. Caso 1: un mercader de Venecia viaja a Constantinopla y luego a Alejandría en el siglo XII. Caso 2: un peregrino de Córdoba (siglo X) viaja a La Meca. Para tu caso, nombra los mundos que cruza, el mar o la ruta, un siglo y una pregunta que el mapa no responde.",
        "Caso 1: cruza el mundo latino, el bizantino y el islámico por el Mediterráneo, en el siglo XII; pregunta: ¿qué compró en cada puerto?",
        ["nombra al menos dos mundos", "indica el mar o la ruta", "ubica un siglo correcto", "formula una pregunta que el mapa no responde"],
        ["texto de cuatro líneas con los cuatro elementos pedidos"],
        ["confundir siglo XII con el año 1200", "decir que el mapa prueba el tipo de relación"],
        "Pide a una persona de tu casa que señale en un mapa del Mediterráneo la ruta que describiste.",
    ),
    "Dibuja una línea de tiempo con las seis fechas de la clase y escribe a qué mundo pertenece cada hecho.",
    "Investiga qué nombre recibe hoy Constantinopla y en qué país está.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a comparar cómo se organizaban y cómo eran las ciudades de la Europa latina, de Bizancio y del mundo islámico. Sirve para ver diferencias reales sin decir que una era mejor que otra.",
    ["Sé ubicar los tres mundos en el Mediterráneo.", "Sé que un gobierno y una ciudad se describen con datos."],
    [
        "En la Europa latina del año 1000 la mayoría vivía en el campo. El poder estaba repartido: un rey y señores que entregaban tierras (feudos) a otros nobles, llamados vasallos, a cambio de lealtad y ayuda militar. Ese sistema se llama feudalismo. La Iglesia, dirigida por el papa, también tenía mucho poder. Muchas ciudades eran pequeñas.",
        "El Imperio bizantino tenía un poder más centralizado. Un emperador gobernaba con funcionarios y con las leyes romanas reunidas por Justiniano en el siglo VI. Su capital, Constantinopla, con murallas, puertos, mercados y la iglesia de Santa Sofía, era una de las ciudades más grandes de su tiempo. El emperador también intervenía en asuntos de la Iglesia.",
        "En el mundo islámico el califa era la máxima autoridad política y religiosa de la comunidad. Gobernaba por medio de gobernadores y funcionarios. Había grandes ciudades como Bagdad y Córdoba, con mercados (zocos), baños públicos, mezquitas y bibliotecas. Comparar no es poner notas: se miran rasgos distintos, como quién gobierna, cómo se reparte el poder y cómo es la vida en la ciudad.",
    ],
    [("feudalismo", "sistema europeo en que el poder y la tierra se repartían entre señores y vasallos"), ("vasallo", "noble que recibía tierras de un señor a cambio de lealtad y servicio"), ("califa", "jefe político y religioso de la comunidad musulmana"), ("centralizado", "con el poder concentrado en una autoridad y su administración"), ("zoco", "mercado de una ciudad islámica"), ("funcionario", "persona que cumple una tarea de administración del Estado")],
    [
        ("Clasificar un rasgo", "Ficha de ejemplo: «Un jefe único gobierna con funcionarios y leyes romanas desde una capital con murallas». ¿A qué mundo corresponde?", ["Leyes romanas de Justiniano y capital amurallada.", "Eso describe a Bizancio."], "Mundo bizantino"),
        ("Comparar con un criterio", "Compara quién tenía el poder en la Europa latina y en el califato.", ["Europa latina: rey y señores repartían el poder.", "Califato: el califa lo concentraba, con funcionarios.", "Criterio: reparto del poder."], "En la Europa latina el poder estaba repartido; en el califato estaba concentrado en el califa"),
    ],
    [
        ("Creer que toda ciudad medieval era igual.", "Constantinopla, Córdoba y una ciudad pequeña del norte de Europa se diferenciaban en tamaño, comercio y gobierno.", "Compara con un criterio: tamaño, gobierno o servicios."),
        ("Decir que el mundo más grande o más centralizado era «mejor».", "Comparar describe diferencias; no ordena a las culturas de mejor a peor.", "Usa verbos como «tenía», «se organizaba», no «era superior»."),
    ],
    [
        ("¿Cómo se llama el sistema europeo en que un señor entregaba tierras a un vasallo a cambio de lealtad?", "Feudalismo", "Así se llamó al reparto de tierras y deberes entre señores y vasallos."),
        ("¿Quién era la máxima autoridad política y religiosa del mundo islámico: el califa o el emperador?", "El califa", "El emperador era la autoridad de Bizancio."),
        ("¿Qué ciudad bizantina era famosa por sus murallas y por la iglesia de Santa Sofía?", "Constantinopla", "Era la capital del imperio y allí estaba Santa Sofía."),
    ],
    [
        ("Un monje europeo del año 1000 describe una aldea de 200 personas junto a un castillo. ¿Qué rasgo de la Europa latina muestra esa descripción?", "Que mucha gente vivía en el campo y en lugares pequeños", "Una aldea pequeña refleja un mundo mayormente rural."),
        ("¿Qué tenían en común Bagdad y Córdoba que las distinguía de la mayoría de las aldeas europeas del año 1000?", "Eran grandes ciudades con mercados, mezquitas y bibliotecas", "Se explicó que ambas tenían zocos, mezquitas y bibliotecas."),
        ("¿Por qué se dice que el poder bizantino estaba más centralizado que el feudal?", "Porque lo concentraba el emperador con sus funcionarios y no estaba repartido entre muchos señores", "En el feudalismo el poder estaba repartido."),
    ],
    [
        ("Observa: «Ciudad X: murallas, puerto, mercados, emperador, leyes romanas». ¿Es más probable que sea Constantinopla o Córdoba?", "Constantinopla", "El emperador y las leyes romanas son rasgos de Bizancio."),
        ("Observa: «Ciudad Y: mezquita mayor, zocos, baños públicos, gobernador del califa». ¿Es más probable que sea Córdoba o una aldea feudal?", "Córdoba", "Mezquita, zocos y gobernador del califa son rasgos de una ciudad islámica."),
        ("Un estudiante escribe «El mundo islámico era más civilizado que el feudal». Reescribe la idea con un criterio que sí se pueda comprobar.", "Por ejemplo: en el año 1000 Córdoba tenía bibliotecas y zocos, y la mayoría de las aldeas feudales eran pequeñas", "Se cambia un juicio por un rasgo observable."),
    ],
    [
        ("Pedro afirma: «Como el califa y el emperador gobernaban solos, eran el mismo tipo de poder». Explica por qué es una simplificación.", "Uno era jefe político y religioso de una comunidad y el otro gobernaba un imperio con una Iglesia propia", "Aunque ambos concentraban el poder, sus bases eran distintas."),
        ("Ana compara solo el tamaño de las ciudades. ¿Qué otro criterio de la clase debería añadir para una buena comparación?", "Quién gobierna o cómo se reparte el poder", "Una comparación sólida usa varios criterios."),
    ],
    [
        ("Ordena de mayor a menor concentración del poder político, según la clase: A = Europa feudal, B = Bizancio.", "B, A", "Bizancio lo concentraba en el emperador; en el feudalismo estaba repartido."),
        ("Un estudiante dice que Córdoba y Constantinopla se parecen en que ambas eran grandes ciudades con mercados. ¿Qué diferencia de gobierno debería agregar?", "Córdoba dependía de un califa y Constantinopla, de un emperador", "Ambas tenían mercados, pero su autoridad máxima era distinta."),
    ],
    [("Un mercader de ejemplo recorre tres lugares: una aldea feudal de 150 personas, Constantinopla y Córdoba. ¿En cuál de los tres encontrará con más probabilidad mercados grandes, mezquitas y gobernador del califa?", "Córdoba", "Las mezquitas y el gobernador del califa son rasgos de Córdoba.")],
    [("En la unidad de Edad Media, ¿qué es un vasallo?", "Un noble que recibía tierras de un señor a cambio de lealtad y servicio", "Es la definición del vocabulario."), ("¿Qué emperador reunió las leyes romanas en el siglo VI?", "Justiniano", "Se mencionó como creador de la recopilación de leyes bizantina."), ("¿Por qué comparar no es poner notas?", "Porque se describen rasgos distintos sin decir que una cultura vale más", "Comparar usa criterios y no jerarquiza.")],
    (
        "Completa la tabla escribiendo una frase breve por casilla. Filas: Europa latina, Bizancio, mundo islámico. Columnas: quién gobierna, cómo es una ciudad importante. Datos que puedes usar: rey y señores; emperador y funcionarios; califa y gobernadores; aldeas pequeñas con castillo; Constantinopla con murallas y puerto; Córdoba con zocos y mezquita.",
        "Europa latina: gobiernan un rey y señores; mucha vida en aldeas con castillo.",
        ["completa las seis casillas", "usa los datos correctos en cada una", "no usa palabras como «mejor» o «atrasado»"],
        ["tabla de seis casillas con frases breves"],
        ["mezclar al emperador con el califa", "calificar a una cultura de superior"],
        "Pide a una persona de tu casa que lea tu tabla y diga si alguna frase juzga en vez de describir.",
    ),
    "Escribe tres semejanzas y tres diferencias entre Constantinopla y Córdoba usando solo los datos de la clase.",
    "Busca qué es la iglesia de Santa Sofía y para qué se usó después de 1453.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a examinar intercambios de ciencia, comercio y cultura entre la Europa latina, Bizancio y el islam. Sirve para ver que las ideas y los productos circularon en varias direcciones.",
    ["Sé ubicar los tres mundos en el Mediterráneo.", "Sé que un intercambio puede ser de objetos, de ideas o de palabras."],
    [
        "Un intercambio es el paso de productos, saberes o costumbres de un lugar a otro. En el Mediterráneo medieval hubo tres tipos principales. En el comercio circularon especias, seda, telas y azúcar desde Asia y el Medio Oriente hacia ciudades como Constantinopla y Venecia. En la ciencia, sabios del mundo islámico tradujeron textos griegos al árabe y escribieron obras de medicina, matemáticas y astronomía. En la cultura pasaron palabras, música y técnicas.",
        "Hay ejemplos concretos. El matemático al-Juarismi escribió en Bagdad, en el siglo IX, un libro sobre cómo resolver ecuaciones: de «al-yabr» viene la palabra álgebra. Los números que usamos hoy (0, 1, 2, 3…) llegaron a Europa por el mundo islámico, con origen en la India. En el siglo XII, en Toledo, textos árabes se tradujeron al latín. Muchas palabras del español vienen del árabe: aceite, azúcar, almohada y alcalde.",
        "La influencia no fue de un solo lado. Bizancio conservó y copió textos griegos y el derecho romano, y después de 1453 sabios bizantinos llevaron manuscritos a Italia. Los mercaderes italianos vendían telas y madera, y compraban seda y especias. Para no exagerar, hay que recordar que una idea cambia al viajar: se traduce, se corrige y se mezcla con otras.",
    ],
    [("intercambio", "paso de productos, ideas o costumbres entre pueblos"), ("traducción", "paso de un texto de una lengua a otra"), ("especia", "sustancia vegetal que se usa para dar sabor, como la pimienta"), ("manuscrito", "texto escrito a mano"), ("álgebra", "rama de las matemáticas que usa letras para resolver ecuaciones"), ("influencia", "efecto que un pueblo o una idea produce en otro")],
    [
        ("Rastrear una palabra", "La palabra «azúcar» se usa en español y viene del árabe. ¿Qué tipo de intercambio muestra: comercio, ciencia o cultura (lenguaje)?", ["Una palabra pasa de una lengua a otra.", "Eso es un intercambio de lenguaje y también de un producto."], "Cultura (lenguaje); además el azúcar fue un producto comerciado"),
        ("Dirección de la influencia", "Un libro griego se traduce al árabe en Bagdad y siglos después al latín en Toledo. ¿Pasó por el mundo islámico antes de llegar a la Europa latina?", ["Primero al árabe, luego al latín.", "El árabe es la lengua del mundo islámico."], "Sí, pasó por el mundo islámico"),
    ],
    [
        ("Decir que los saberes viajaron solo de oriente a occidente.", "Hubo influencia en varias direcciones: los latinos también vendieron productos y los bizantinos llevaron manuscritos a Italia.", "Pregunta siempre quién enseñó, quién aprendió y quién tradujo."),
        ("Pensar que una idea llega igual a como salió.", "Al traducirse y mezclarse con otras, una idea cambia.", "Compara el original con la versión nueva."),
    ],
    [
        ("¿De qué palabra árabe viene «álgebra»?", "De «al-yabr»", "El libro de al-Juarismi usaba ese término."),
        ("¿En qué ciudad española se tradujeron textos árabes al latín en el siglo XII?", "Toledo", "Fue un centro de traducción de la época."),
        ("Nombra un producto que llegaba desde Asia y el Medio Oriente a ciudades como Constantinopla y Venecia.", "Seda, especias o azúcar (cualquiera de los tres)", "Son los productos de comercio nombrados en la explicación."),
    ],
    [
        ("Los números 0 al 9 que usamos hoy llegaron a Europa a través del mundo islámico. ¿Quiere decir eso que se inventaron en Arabia?", "No, tenían origen en la India", "Pasaron por el mundo islámico, pero su origen es indio."),
        ("¿Por qué la traducción de textos griegos al árabe fue un aporte a la ciencia?", "Porque conservó y difundió conocimientos que luego se usaron y ampliaron", "Los textos no se perdieron y se siguieron estudiando."),
        ("¿Qué dos palabras españolas de la clase vienen del árabe y se relacionan con la comida?", "Aceite y azúcar", "Ambas se mencionan como ejemplos de palabras de origen árabe."),
    ],
    [
        ("Una ficha de ejemplo dice: «Un mercader de Venecia vende telas de lana y madera y compra seda». ¿Qué mundo vende el producto de lana y madera: el latino o el bizantino?", "El latino", "Venecia era una ciudad de la Europa latina."),
        ("Un sabio bizantino lleva un manuscrito griego a Italia después de 1453. ¿Hacia dónde viajó la influencia: de Bizancio a la Europa latina o al revés?", "De Bizancio a la Europa latina", "El manuscrito salió de Bizancio hacia Italia."),
        ("Una palabra empieza con «al-» (como «alcalde» o «almohada»). ¿Qué lengua es la fuente más probable?", "El árabe", "Muchas palabras con «al-» provienen del artículo árabe."),
    ],
    [
        ("Luis afirma: «La Europa latina no aprendió nada del islam». Cita un ejemplo de la clase que lo contradice.", "Aprendió álgebra, números o palabras como aceite o azúcar", "Cualquiera de esos aportes prueba una influencia."),
        ("Marta dice: «Todo lo que Europa recibió lo inventaron los árabes». ¿Qué error comete?", "Atribuye a una sola dirección ideas que venían de varios pueblos, como los números de la India o los textos griegos", "Los saberes se transmitieron y mezclaron."),
    ],
    [
        ("Ordena el recorrido del libro, de lo más antiguo a lo más reciente: A = traducción al latín en Toledo, B = obra escrita en griego, C = traducción al árabe en Bagdad.", "B, C, A", "Primero el original griego, luego el árabe y al final el latín."),
        ("Texto de ejemplo: «Un libro griego de medicina fue traducido al árabe en Bagdad; siglos después, un sabio de Toledo lo tradujo al latín». ¿Cuántas traducciones tuvo el libro y a qué lenguas?", "Dos: al árabe y al latín", "El texto menciona una traducción al árabe y otra al latín."),
    ],
    [("Un estudiante quiere explicar por qué hay palabras árabes en español. Entre estas dos ideas, ¿cuál es mejor? A) Por la convivencia y el contacto de siglos en la península ibérica. B) Porque los árabes impusieron su idioma y el español dejó de usarse.", "A", "El contacto prolongado explica el paso de palabras.")],
    [("En la unidad de Edad Media, ¿qué es un intercambio?", "El paso de productos, ideas o costumbres entre pueblos", "Es la definición del vocabulario."), ("¿Qué mundo conservó manuscritos griegos y luego llevó algunos a Italia?", "El bizantino", "Los sabios bizantinos los llevaron después de 1453."), ("¿Por qué es mejor hablar de «influencia en varias direcciones»?", "Porque ideas y productos circularon entre los tres mundos y no solo en un sentido", "Hubo traducción, comercio y migración en ambos sentidos.")],
    (
        "Elige un producto o un saber de esta lista y escribe un párrafo de cinco líneas: seda, álgebra, números del 0 al 9, aceite (palabra). Responde: de dónde sale, por dónde viaja, a quién llega y qué cambia en el camino. Datos útiles: la seda venía de Asia; el álgebra nace en Bagdad; los números tienen origen en la India; aceite viene del árabe.",
        "Seda: viene de Asia, viaja por rutas del Medio Oriente y Constantinopla, llega a Venecia y se vende como tela de lujo.",
        ["indica el origen", "indica la ruta o el medio de paso", "indica quién la recibe", "menciona algo que cambia o se adapta"],
        ["párrafo de cinco líneas con los cuatro elementos"],
        ["decir que lo inventó el último pueblo que lo usó", "olvidar el origen indio de los números"],
        "Lee tu párrafo a una persona de tu casa y pregúntale si entendió por dónde viajó la idea.",
    ),
    "Anota cinco palabras del español de origen árabe y averigua su significado con una persona de tu casa.",
    "Investiga quién fue al-Juarismi y qué escribió.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a analizar casos de convivencia y de conflicto entre cristianos y musulmanes, en especial en la península ibérica. Sirve para entender que las relaciones no fueron solo guerra.",
    ["Sé que la península ibérica fue parte del mundo islámico desde 711.", "Sé que un hecho puede tener más de una causa."],
    [
        "Entre los siglos VIII y XV la península ibérica tuvo reinos cristianos en el norte y territorios musulmanes en el sur, llamados Al-Ándalus. Entre ellos había una frontera que cambió muchas veces. Hubo guerras y avances cristianos, que se conocen como Reconquista. Un ejemplo es la batalla de Las Navas de Tolosa, en 1212. Pero también hubo convivencia: comerciantes que cruzaban la frontera, tratados, matrimonios y traducciones.",
        "En Al-Ándalus vivían musulmanes, cristianos (llamados mozárabes) y judíos. En los reinos cristianos vivían también musulmanes, llamados mudéjares. Muchos reyes cristianos cobraban tributos (parias) a reinos musulmanes a cambio de no atacarlos. Un caso famoso es el del Cid Campeador, un caballero cristiano que sirvió a veces a un rey musulmán y otras veces lo combatió.",
        "Fuera de la península también hubo conflicto: desde 1095 el papa llamó a las Cruzadas para tomar Jerusalén, que ocurrió en 1099. Pero aun entonces había comercio entre Venecia y puertos musulmanes. Dentro del cristianismo, la división de 1054 entre Roma y Constantinopla separó a latinos y bizantinos. Por eso no se debe resumir todo en «guerra de religiones»: hubo alianzas, intereses económicos y rivalidades dentro de cada religión.",
    ],
    [("Al-Ándalus", "territorio de la península ibérica bajo gobierno musulmán"), ("Reconquista", "proceso por el cual reinos cristianos avanzaron sobre Al-Ándalus"), ("mozárabe", "cristiano que vivía en territorio musulmán"), ("mudéjar", "musulmán que vivía en territorio cristiano"), ("paria", "tributo que un reino pagaba a otro a cambio de paz"), ("Cruzadas", "expediciones militares cristianas hacia Jerusalén desde 1095")],
    [
        ("Clasificar un hecho", "Un reino musulmán paga parias a un rey cristiano para evitar ser atacado. ¿Es solo conflicto, solo convivencia o una mezcla?", ["Hay amenaza militar.", "Hay también un acuerdo con pago.", "Es una mezcla."], "Una mezcla de conflicto y acuerdo"),
        ("Corregir una generalización", "Frase: «Cristianos y musulmanes siempre se combatieron». Busca un caso que la contradiga.", ["Los comerciantes cruzaban la frontera.", "El Cid sirvió a un rey musulmán.", "Con uno basta."], "El Cid sirvió a un rey musulmán"),
    ],
    [
        ("Pensar que todos los cristianos estaban de un lado y todos los musulmanes del otro.", "Había reinos cristianos rivales entre sí y reinos musulmanes rivales entre sí, y alianzas que cruzaban religiones.", "Pregunta quién se alía con quién y por qué."),
        ("Creer que la Reconquista fue una sola guerra continua.", "Duró siglos, con paces, tratados y avances en distintas épocas.", "Ubica cada hecho con su fecha."),
    ],
    [
        ("¿Cómo se llamaba el territorio musulmán de la península ibérica?", "Al-Ándalus", "Así se nombra al territorio gobernado por musulmanes."),
        ("¿Cómo se llama el cristiano que vivía en Al-Ándalus?", "Mozárabe", "Es el término del vocabulario para cristianos bajo gobierno musulmán."),
        ("¿En qué año tomaron Jerusalén los cruzados, según la clase?", "1099", "Fue el resultado de la primera expedición llamada por el papa en 1095."),
    ],
    [
        ("¿Qué nombre reciben los musulmanes que vivían en reinos cristianos?", "Mudéjares", "Se distinguen de los mozárabes, que eran cristianos bajo gobierno musulmán."),
        ("¿Para qué se pagaban las parias?", "Para obtener paz o evitar un ataque", "Eran tributos a cambio de no ser atacado."),
        ("¿Por qué la batalla de Las Navas de Tolosa (1212) muestra conflicto y no convivencia?", "Porque enfrentó con armas a ejércitos cristianos y musulmanes", "Una batalla es un enfrentamiento militar."),
    ],
    [
        arith("La primera expedición de las Cruzadas fue llamada por el papa en 1095 y Jerusalén fue tomada en 1099. ¿Cuántos años pasaron?", "1099-1095", "Se resta el año de la convocatoria al de la toma."),
        ("Un comerciante cristiano cruza la frontera y vende telas en un zoco musulmán. ¿Qué tipo de relación muestra?", "Convivencia o intercambio comercial", "El comercio une a personas de distintas religiones."),
        ("Una ficha de ejemplo dice: «Un caballero cristiano sirvió a un rey musulmán durante dos años». ¿Qué idea queda cuestionada: que cristianos y musulmanes siempre estuvieron en bandos opuestos, o que el comercio nunca existió?", "Que cristianos y musulmanes siempre estuvieron en bandos opuestos", "El caballero luchó junto a un rey de otra religión."),
    ],
    [
        ("Julia dice: «Las Cruzadas fueron solo guerra entre religiones». Da un dato de la clase que complique esa idea.", "También hubo comercio entre Venecia y puertos musulmanes", "El comercio continuó pese a las guerras."),
        ("En 1054 se dividió el cristianismo en dos Iglesias. ¿Qué dos mundos quedaron separados religiosamente?", "El latino (Roma) y el bizantino (Constantinopla)", "Esa división ocurrió dentro del cristianismo."),
    ],
    [
        ("¿Cuáles de estos hechos son claramente un enfrentamiento armado? 1) batalla de Las Navas de Tolosa; 2) comercio en la frontera; 3) pago de parias a cambio de paz; 4) toma de Jerusalén en 1099. Responde con los números.", "1 y 4", "Una batalla y una toma de ciudad son enfrentamientos; el comercio y las parias son acuerdos."),
        ("Un estudiante dice: «Si hubo traducciones, entonces no hubo guerras en la península». ¿Qué error lógico comete?", "Piensa que lo uno excluye lo otro, pero convivencia y conflicto pudieron ocurrir a la vez o en distintas épocas", "Ambos tipos de relación coexistieron."),
    ],
    [("Una persona escribe: «En 1212 un ejército cristiano derrotó a otro musulmán en Las Navas de Tolosa; ese mismo año un comerciante cristiano seguía vendiendo en un zoco musulmán». ¿Es posible que ambos hechos sean verdaderos a la vez?", "Sí", "Una batalla y el comercio de otro lugar pueden ocurrir en el mismo año.")],
    [("¿Qué son los mudéjares?", "Musulmanes que vivían en territorio cristiano", "Es la definición del vocabulario."), ("¿Qué hecho de la clase muestra alianza entre personas de distinta religión?", "El Cid sirvió a veces a un rey musulmán", "Un caballero cristiano sirvió a un rey de otra religión."), ("¿Por qué no basta decir «guerra de religiones»?", "Porque hubo alianzas, comercio y rivalidades dentro de cada religión", "Las causas eran políticas y económicas además de religiosas.")],
    (
        "Elige uno de estos tres casos y escribe seis líneas: (1) los comerciantes de la frontera; (2) la batalla de Las Navas de Tolosa; (3) un reino que paga parias. Explica quiénes participan, qué quieren y si el caso muestra convivencia, conflicto o ambas. Termina con una frase que diga qué no demuestra el caso.",
        "Caso 3: un reino musulmán paga parias a un rey cristiano para evitar la guerra; muestra conflicto y acuerdo; no demuestra que fueran amigos.",
        ["identifica a los actores", "explica lo que cada uno quiere", "clasifica la relación", "escribe un límite de la conclusión"],
        ["texto de seis líneas con los cuatro criterios"],
        ["reducir todo a motivos religiosos", "generalizar a toda la península"],
        "Cuéntale tu caso a una persona de tu casa y pídele que diga qué parte muestra conflicto y cuál convivencia.",
    ),
    "Dibuja una línea de tiempo con 711, 1095, 1099, 1212 y 1492 y escribe un hecho en cada fecha.",
    "Averigua qué es la Mezquita-Catedral de Córdoba y qué muestra sobre las relaciones entre religiones.",
)

# ================================================================ clase 5
lesson(
    OA, 5,
    "Aprenderé a contrastar dos fuentes que cuentan el mismo hecho desde perspectivas distintas. Sirve para no tomar una sola voz como la verdad completa.",
    ["Sé que una fuente tiene autor, fecha y lugar.", "Sé que el autor puede tener intereses y opiniones."],
    [
        "Una perspectiva es el punto de vista de quien cuenta un hecho: depende de su religión, su ciudad, su rol y sus intereses. Dos cronistas pueden presenciar el mismo hecho y contarlo distinto. Para contrastar fuentes se hacen cuatro preguntas: quién escribe, cuándo y dónde, para quién escribe y qué calla o destaca.",
        "Un ejemplo: en 1204 los cruzados latinos saquearon Constantinopla. Un cronista bizantino lo cuenta como una traición de cristianos contra cristianos. Un cronista latino puede explicarlo como un asunto político o de deudas con Venecia. Ambos hablan del mismo hecho, pero no destacan lo mismo. Esas diferencias son pistas, no errores que haya que borrar.",
        "Contrastar no obliga a elegir un bando. Se buscan acuerdos, desacuerdos y datos que se repiten. Si ambas fuentes coinciden en un dato (la ciudad fue saqueada), ese dato es más sólido. Si discrepan en las causas o en los culpables, la conclusión debe ser más cuidadosa: «según el cronista X, ...». También hay que evitar usar palabras de hoy como si el autor las hubiera pensado.",
    ],
    [("perspectiva", "punto de vista desde el que alguien cuenta un hecho"), ("cronista", "persona que escribe la historia de su tiempo"), ("contrastar", "comparar para ver coincidencias y diferencias"), ("fuente", "texto, objeto o imagen que da información sobre el pasado"), ("sesgo", "inclinación que hace destacar unos datos y callar otros"), ("saqueo", "robo violento de una ciudad")],
    [
        ("Aplicar las cuatro preguntas", "Fuente de ejemplo A: «Escrito por un cronista bizantino, en Constantinopla, poco después del saqueo de 1204. Culpa a los cruzados de codicia». ¿Quién escribe, desde dónde y qué destaca?", ["Un cronista bizantino.", "Escribe desde la ciudad afectada.", "Destaca la codicia de los cruzados."], "Bizantino; desde la ciudad saqueada; destaca la codicia de los cruzados"),
        ("Encontrar el acuerdo", "Fuente B (latina, de ejemplo): «El ejército entró a Constantinopla y tomó sus riquezas». Fuente A: «Los cruzados saquearon la ciudad». ¿En qué dato coinciden?", ["Compara lo que dice cada fuente sobre la ciudad.", "Ambas dicen que hubo toma de la ciudad y de riquezas."], "En que la ciudad fue tomada y sus riquezas fueron llevadas"),
    ],
    [
        ("Creer que una fuente miente porque no coincide con otra.", "Puede decir cosas distintas porque destaca otros aspectos desde su perspectiva.", "Busca primero acuerdos y luego explica las diferencias."),
        ("Elegir un bando y descartar al otro cronista.", "Ambas voces son evidencia sobre el pasado, aunque con sesgos.", "Cita a cada uno: «según el cronista X…»."),
    ],
    [
        ("¿Cuántas preguntas básicas se hacen para contrastar fuentes en esta clase?", "Cuatro", "Son quién escribe, cuándo y dónde, para quién y qué calla o destaca."),
        ("En la unidad de Edad Media, ¿qué es una perspectiva?", "El punto de vista desde el que alguien cuenta un hecho", "Es la definición del vocabulario."),
        ("¿Cómo llamó a lo ocurrido en 1204 un cronista bizantino, según la clase: traición o victoria?", "Traición", "Lo contó como un ataque de cristianos contra cristianos."),
    ],
    [
        ("Un cronista latino de ejemplo escribe en su ciudad un año después del saqueo y explica que se debió a deudas con Venecia. ¿Qué dato de contexto de esa fuente permite entender su perspectiva?", "Que es un cronista latino que escribe desde su propia ciudad", "El lugar y el grupo del autor explican qué destaca."),
        ("Si dos fuentes coinciden en que la ciudad fue saqueada, ¿ese dato es más sólido o más débil?", "Más sólido", "Dos voces independientes que coinciden refuerzan el dato."),
        ("¿Por qué no se corrige o borra la diferencia entre dos cronistas?", "Porque la diferencia muestra sus perspectivas", "Las diferencias son pistas sobre quién cuenta y por qué."),
    ],
    [
        ("Fuente C de ejemplo (cronista árabe, siglo XII): «Los francos tomaron Jerusalén y sus habitantes sufrieron muchas muertes». Fuente D de ejemplo (cronista latino, siglo XII): «El ejército cristiano conquistó la Ciudad Santa». ¿Cuál de las dos usa un verbo que celebra el hecho?", "La D", "«Conquistó la Ciudad Santa» destaca una victoria, mientras la C destaca el sufrimiento."),
        ("¿Qué pregunta de las cuatro ayuda a explicar por qué C y D describen distinto el mismo hecho?", "Quién escribe, cuándo y dónde", "Ser parte de un grupo u otro cambia lo que se destaca."),
        ("Un estudiante concluye: «Según C y D la ciudad fue tomada por un ejército». ¿Esa conclusión está bien limitada?", "Sí, porque es el dato en que coinciden", "Se limita a lo que ambas fuentes sostienen."),
    ],
    [
        ("Marta dice: «Como el cronista bizantino estaba en la ciudad atacada, no sirve». ¿Qué responderías?", "Sí sirve: su perspectiva es una evidencia de cómo vivió el hecho un afectado, aunque tenga sesgo", "Toda fuente sirve si se sabe quién la escribe."),
        ("Pedro escribe «El cronista X cuenta la verdad». Reescribe la frase con una expresión más cuidadosa.", "Por ejemplo: «Según el cronista X, ocurrió…»", "Se atribuye la afirmación a su autor."),
    ],
    [
        ("Ordena los pasos para contrastar dos fuentes: A) formular una conclusión limitada, B) preguntar quién escribe cada una, C) comparar acuerdos y diferencias.", "B, C, A", "Primero se identifica a los autores, luego se comparan y al final se concluye."),
        ("Una conclusión dice: «En 1204 los cruzados fueron culpables ante todos los pueblos». ¿Qué parte no está respaldada por las dos fuentes de la clase?", "«Ante todos los pueblos», porque solo se tienen dos voces", "Con dos fuentes no se puede hablar de todos."),
    ],
    [("Lee: Fuente E de ejemplo (monje latino, 1150): «Los musulmanes de la ciudad eran enemigos de Dios». Fuente F de ejemplo (comerciante judío de El Cairo, 1150): «Mi socio musulmán de la ciudad cumplió todos sus pagos». ¿Qué conclusión limitada permiten ambas fuentes sobre cómo dos autores distintos veían a los musulmanes?", "Que en 1150 había visiones opuestas según el grupo y el interés de quien escribe", "La diferencia entre hostilidad y relaciones de negocio muestra perspectivas distintas.")],
    [("¿Qué hay que preguntar siempre sobre una fuente?", "Quién la escribe, cuándo y dónde, para quién y qué destaca", "Son las cuatro preguntas de la clase."), ("¿Para qué sirve contrastar fuentes?", "Para encontrar acuerdos, diferencias y limitar la conclusión", "Se evita tomar una sola voz como verdad completa."), ("En la unidad de Edad Media, ¿qué es un sesgo?", "Una inclinación que hace destacar unos datos y callar otros", "Es la definición del vocabulario.")],
    (
        "Contrasta estas dos fuentes de ejemplo escritas para esta tarea. Fuente 1 (cronista bizantino, 1204): «Los cruzados latinos rompieron la paz y saquearon iglesias y casas de Constantinopla». Fuente 2 (cronista latino, 1205): «El ejército entró a la ciudad por falta de pagos y se llevó los bienes que no le habían dado». Completa: un dato en que coinciden, una diferencia de perspectiva y una conclusión limitada que empiece con «según las dos fuentes…».",
        "Coinciden en que el ejército tomó los bienes de Constantinopla; difieren en la causa; según las dos fuentes, el ejército tomó los bienes de la ciudad.",
        ["identifica un acuerdo", "describe una diferencia de perspectiva", "redacta una conclusión limitada", "no toma partido sin evidencia"],
        ["tres frases: acuerdo, diferencia y conclusión"],
        ["elegir una fuente como verdadera", "concluir sobre todos los latinos o todos los bizantinos"],
        "Léele tu conclusión a una persona de tu casa y pregúntale si te parece que tomaste partido por una fuente.",
    ),
    "Escribe una pregunta que haría falta responder con una tercera fuente para entender el saqueo de 1204.",
    "Investiga qué fue la Cuarta Cruzada y por qué Venecia tuvo un papel importante.",
)

# ================================================================ clase 6
lesson(
    OA, 6,
    "Aprenderé a escribir una explicación sobre las relaciones entre Europa, Bizancio y el islam sin decir que un mundo fue superior. Sirve para cerrar la unidad con conclusiones justas.",
    ["Sé ubicar y comparar los tres mundos.", "Sé contrastar dos fuentes y limitar una conclusión."],
    [
        "Una jerarquía civilizatoria es la idea de que unas culturas están «arriba» y otras «abajo», por ejemplo llamar «atrasado» a un pueblo. Los historiadores la evitan, porque mide a las culturas con un solo criterio y casi siempre el de quien habla. En la Edad Media, cada mundo tuvo logros y problemas propios. Una explicación justa describe los hechos, sus causas y sus efectos sin ordenar a los pueblos de mejor a peor.",
        "Una buena explicación tiene cuatro partes. Primero, una afirmación clara: por ejemplo, «Entre los siglos VIII y XV hubo conflicto y convivencia entre cristianos y musulmanes en la península ibérica». Segundo, evidencia con fecha y lugar. Tercero, una causa o consecuencia: «El comercio mantuvo contactos aunque hubiera guerras». Cuarto, un límite: «Esto no demuestra que las relaciones fueran iguales en toda la península».",
        "También hay que evitar palabras como «oscuro», «bárbaro» o «civilizado» para describir a un pueblo entero. Se prefieren verbos que describan lo que se hizo: «tradujo», «comerció», «gobernó», «combatió». Y no se explican hechos del pasado con valores actuales como si las personas de entonces los compartieran: el pasado se entiende primero desde su contexto.",
    ],
    [("jerarquía civilizatoria", "idea de que unas culturas valen más que otras"), ("afirmación", "idea central que se quiere sostener"), ("evidencia", "dato o fuente que apoya una afirmación"), ("límite", "aquello que la evidencia no permite concluir"), ("contexto", "circunstancias de tiempo y lugar de un hecho"), ("anacronismo", "juzgar el pasado con ideas de hoy")],
    [
        ("Detectar una jerarquía", "Frase: «Los bizantinos eran más civilizados que los europeos latinos». ¿Qué problema tiene?", ["Usa «civilizados» para un pueblo entero.", "Ordena a dos culturas de mejor a peor."], "Establece una jerarquía sin criterio claro"),
        ("Reescribir con un verbo que describe", "Reescribe: «El islam era superior en ciencia». Usa un verbo y una evidencia.", ["Elige el hecho: tradujeron textos griegos.", "Pon un lugar: Bagdad."], "Sabios del mundo islámico tradujeron textos griegos al árabe en Bagdad"),
    ],
    [
        ("Usar «bárbaro» o «civilizado» para describir un pueblo completo.", "Son juicios sobre toda una cultura y no describen hechos comprobables.", "Cambia el adjetivo por un hecho con fecha y lugar."),
        ("Escribir una conclusión sin límite.", "Una conclusión sin límite parece decir más de lo que prueban las fuentes.", "Añade una frase final que diga qué no demuestra la evidencia."),
    ],
    [
        ("¿Cuántas partes tiene una buena explicación en esta clase?", "Cuatro", "Son afirmación, evidencia, causa o consecuencia y límite."),
        ("En la unidad de Edad Media, ¿qué es una jerarquía civilizatoria?", "La idea de que unas culturas valen más que otras", "Es la definición del vocabulario."),
        ("¿Qué verbo es mejor para describir un hecho: «tradujo» o «era superior»?", "«Tradujo»", "Describe una acción comprobable, no un juicio."),
    ],
    [
        ("Frase: «En el año 1000 Córdoba tenía bibliotecas y zocos». ¿Esa frase es una evidencia o una jerarquía?", "Una evidencia", "Describe rasgos comprobables."),
        ("Frase: «Los bizantinos eran más atrasados que los árabes». ¿Qué le falta para ser una frase histórica justa?", "Un criterio claro y un dato concreto, y dejar de juzgar al pueblo entero", "«Atrasado» no es un hecho."),
        ("En la unidad de Edad Media, ¿qué es un anacronismo?", "Juzgar el pasado con ideas de hoy", "Es la definición del vocabulario."),
    ],
    [
        ("Clasifica estas frases según su parte de la explicación: 1) «Esto no demuestra lo ocurrido en toda la península»; 2) «El comercio mantuvo contactos pese a las guerras»; 3) «Hubo conflicto y convivencia entre cristianos y musulmanes». ¿Cuál es el límite?", "La 1", "Dice qué no puede concluirse."),
        ("Elige la mejor afirmación: A) «El islam y el cristianismo siempre fueron enemigos» B) «Entre los siglos VIII y XV hubo conflicto y convivencia entre cristianos y musulmanes en la península».", "B", "La frase acotada en tiempo y lugar admite dos tipos de relación."),
        ("Un estudiante escribe: «Todos los cruzados eran fanáticos». ¿Qué cambio la haría más justa?", "Cambiar «todos» por una evidencia específica, como «según un cronista bizantino, los cruzados saquearon…»", "Se evita generalizar a todo un grupo."),
    ],
    [
        ("Pedro dice: «Las Cruzadas muestran que los cristianos eran peores que los musulmanes». ¿Qué error comete?", "Juzga a todo un mundo por un hecho y usa valores de hoy", "Se necesita contexto y no se ordena a las culturas."),
        ("Lucía dice: «Debemos decir que el Imperio bizantino y el islam fueron ricos y la Europa latina, pobre». ¿Qué debería agregar para no ser injusta?", "Criterios, fechas y ejemplos; la Europa latina cambió con el tiempo y hubo ciudades ricas", "Ninguna cultura fue igual en todos los siglos."),
    ],
    [
        ("Ordena la explicación: A) límite, B) afirmación, C) evidencia, D) causa o consecuencia.", "B, C, D, A", "La estructura de la clase empieza por la afirmación y termina con el límite."),
        ("Cuenta los elementos de esta explicación y di cuántos faltan de los cuatro: «Entre los siglos VIII y XV hubo conflicto y convivencia en la península; por ejemplo, en 1212 hubo una batalla».", "Faltan dos: la causa o consecuencia y el límite", "Hay afirmación y evidencia; faltan los otros dos elementos."),
    ],
    [("Una tarea de ejemplo dice: «Explica por qué circularon ideas entre el mundo islámico y la Europa latina». Elige la respuesta mejor: A) «Porque el islam era más inteligente». B) «Porque hubo contactos de siglos por comercio, traducción y convivencia en la península y los puertos».", "B", "La frase con causas históricas evita una jerarquía.")],
    [("¿Qué se debe agregar al final de una explicación?", "Un límite que diga qué no demuestra la evidencia", "El límite evita exagerar."), ("¿Por qué se evitan palabras como «bárbaro»?", "Porque juzgan a todo un pueblo y no describen hechos", "No son datos comprobables."), ("¿Qué hecho de la clase muestra influencia entre mundos?", "La traducción de textos griegos al árabe y luego al latín, o el comercio de especias", "Ambos ejemplos son de intercambio entre mundos.")],
    (
        "Escribe una explicación de seis a ocho líneas sobre este tema: «¿Cómo se relacionaron la Europa latina, Bizancio y el islam entre 622 y 1492?». Debe tener las cuatro partes de la clase. Datos que puedes usar: 711 llegada a la península ibérica; 1054 división del cristianismo; 1099 toma de Jerusalén; 1204 saqueo de Constantinopla; traducciones del árabe al latín en Toledo; comercio de seda y especias.",
        "Afirmación: hubo conflicto y convivencia. Evidencia: 1099 y las traducciones de Toledo. Consecuencia: ideas y productos circularon. Límite: no todas las regiones vivieron lo mismo.",
        ["incluye afirmación, evidencia, causa o consecuencia y límite", "usa al menos dos datos de la lista", "no usa palabras que jerarquicen culturas", "usa verbos que describen hechos"],
        ["texto de seis a ocho líneas con cuatro partes marcadas"],
        ["olvidar el límite", "usar «civilizado» o «atrasado»"],
        "Pide a una persona de tu casa que subraye cada una de las cuatro partes en tu texto.",
    ),
    "Subraya en tu texto cada verbo que describe un hecho y cambia los adjetivos de juicio que encuentres.",
    "Investiga cómo se llamaba el camino de peregrinación a Santiago de Compostela y qué aportó a las relaciones entre regiones europeas.",
)
