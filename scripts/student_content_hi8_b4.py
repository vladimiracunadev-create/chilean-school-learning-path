"""Cuaderno del estudiante, 8.º básico Historia, Geografía y Ciencias Sociales: OA 13 (hacienda y sociedad rural colonial en Chile)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI08 OA 13"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a situar en el tiempo y el espacio la hacienda del Chile colonial y a plantear el problema: cómo una gran propiedad rural organizó la economía y la sociedad.",
    ["Sé que Chile fue colonia española entre los siglos XVI y XIX.", "Sé ubicar el valle central de Chile en un mapa."],
    [
        "Durante la Colonia, la mayor parte de la población chilena vivía en el campo. La economía era rural: se basaba en la agricultura, la ganadería y, en algunas zonas, en la minería. La unidad más importante era la hacienda, una gran propiedad de tierra con casa patronal, capilla, bodegas, campos de cultivo y potreros para animales. Las haciendas se concentraron en el valle central, entre Santiago y el río Maule, donde el clima y los ríos favorecían la producción.",
        "Las haciendas surgieron en los siglos XVII y XVIII. Se formaron con tierras que la Corona entregaba a los conquistadores y a sus descendientes, llamadas mercedes de tierra, y con compras y herencias posteriores. Producían trigo, vino, ganado y cueros, que se vendían en Chile y en el Perú.",
        "El problema que estudiaremos es: ¿qué papel tuvo la hacienda en la formación de los rasgos del Chile colonial, como la economía rural, el inquilinaje, la élite terrateniente y una sociedad con jerarquías, y qué proyecciones tuvo después? Para responder hay que ubicar el tiempo, el lugar y los actores de la hacienda.",
    ],
    [("hacienda", "gran propiedad rural con tierras, casa patronal y trabajadores, dedicada a producir para vender"), ("merced de tierra", "terreno que la Corona entregaba a un colono como premio o para poblar"), ("economía rural", "economía basada sobre todo en actividades del campo"), ("valle central", "zona fértil de Chile entre las cordilleras, donde se concentraron las haciendas"), ("potrero", "terreno cercado donde pastan los animales")],
    [
        ("Ubicar la hacienda", "¿En qué zona de Chile se concentraron las haciendas coloniales?", ["La clase menciona una zona fértil.", "Es el valle central."], "En el valle central"),
        ("Reconocer el origen", "Un colono recibe de la Corona un terreno como premio. ¿Cómo se llama ese terreno entregado?", ["Es un premio de la Corona.", "Se llama merced de tierra."], "Merced de tierra"),
    ],
    [
        ("Creer que la mayor parte de la población vivía en ciudades.", "En la Colonia la mayoría vivía en el campo y la economía era rural.", "Piensa en el campo como centro de la vida colonial."),
        ("Pensar que una hacienda era solo un campo de cultivo.", "Incluía casa patronal, capilla, bodegas y potreros, y reunía trabajadores.", "Describe la hacienda como una comunidad productiva."),
    ],
    [
        ("¿Qué es una hacienda?", "Una gran propiedad rural con tierras, casa patronal y trabajadores", "Es la definición de la clase."),
        ("¿Cómo se llamaba el terreno que la Corona entregaba a un colono?", "Merced de tierra", "Está en el vocabulario."),
        ("¿En qué siglos surgieron las haciendas, según la clase?", "En los siglos XVII y XVIII", "Se explicó en el segundo párrafo."),
    ],
    [
        ("¿Por qué las haciendas se concentraron en el valle central?", "Porque el clima y los ríos favorecían la producción", "Lo dice el primer párrafo."),
        ("Nombra dos productos de la hacienda colonial.", "Trigo, vino, ganado o cueros", "Se nombran en el segundo párrafo."),
        ("¿Dónde se vendían los productos de las haciendas?", "En Chile y en el Perú", "Se indica en el segundo párrafo."),
    ],
    [
        arith("Una hacienda de ejemplo tiene 300 vacas y 450 ovejas. ¿Cuántos animales tiene en total?", "300+450", "Se suman las dos cantidades."),
        ("Un plano de ejemplo muestra una hacienda con una casa patronal, una capilla y tres bodegas. ¿Cuántos edificios hay?", "5", "1 más 1 más 3 es 5."),
        ("Una ficha dice: «Año 1740: la hacienda se encuentra entre Santiago y el río Maule». ¿En qué siglo y en qué zona está?", "Siglo XVIII; valle central", "1740 está en el siglo XVIII y esa zona es el valle central."),
    ],
    [
        ("Un estudiante dice: «Como había ciudades, la economía colonial era urbana». ¿Qué dato de la clase lo contradice?", "Que la mayoría vivía en el campo y la economía era rural", "La clase indica población rural mayoritaria."),
        ("¿Por qué las mercedes de tierra ayudaron a formar las haciendas?", "Porque entregaron grandes terrenos a pocas familias, que luego los ampliaron", "Las mercedes concentraron la propiedad."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = haciendas consolidadas (siglo XVIII), B = fundación de Santiago (1541), C = Independencia de Chile (siglo XIX).", "B, A, C", "Los momentos en orden son 1541, siglo XVIII y siglo XIX."),
        arith("Una hacienda de ejemplo tenía 800 cuadras (unidad de superficie de la época) y heredó 350 más. ¿Cuántas cuadras tiene ahora?", "800+350", "Se suman las cuadras iniciales y las heredadas."),
    ],
    [("Un inventario de ejemplo de 1750 dice: «Hacienda con casa patronal, capilla, 3 bodegas, 500 vacas y 2.000 cuadras». ¿Cuántos tipos de edificios se mencionan?", "3 tipos", "Casa patronal, capilla y bodegas son tres tipos.")],
    [("¿Qué es una economía rural?", "Una economía basada sobre todo en actividades del campo", "Está en el vocabulario."), ("¿Qué incluía una hacienda además de las tierras?", "Casa patronal, capilla, bodegas y trabajadores", "Se explicó en la clase."), ("¿Qué zona era el centro de las haciendas?", "El valle central", "Se explicó en el primer párrafo.")],
    (
        "Dibuja el plano de una hacienda colonial de ejemplo con cinco elementos: casa patronal, capilla, bodega, campo de cultivo y potrero. Rotula cada uno y escribe debajo dos actividades que se hacían ahí (por ejemplo, guardar el vino en la bodega). Agrega una pregunta que el plano no responde.",
        "Plano con casa patronal, capilla, bodega, campo de trigo y potrero. Bodega: guardar vino y trigo. Potrero: pastoreo. Pregunta: ¿quiénes trabajaban y cómo vivían?",
        ["incluye los cinco elementos", "asigna actividades correctas", "formula una pregunta que el plano no responde"],
        ["plano rotulado con actividades y una pregunta"],
        ["olvidar a los trabajadores", "confundir potrero con campo de cultivo"],
        "Muestra tu plano a una persona de tu casa y explícale la función de cada edificio.",
    ),
    "Escribe una definición propia de hacienda en dos líneas.",
    "Escribe una pregunta sobre cómo vivían los trabajadores de una hacienda.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a contextualizar y seleccionar fuentes sobre la hacienda y el inquilinaje. Sirve para saber qué dicen los inventarios, los testamentos y los relatos, y quién queda sin voz.",
    ["Conozco qué es una hacienda.", "Sé que una fuente tiene autor, fecha y propósito."],
    [
        "Para estudiar la hacienda se usan varias fuentes. Un inventario enumera tierras, animales, herramientas y a veces personas; sirve para saber cuánto tenía una hacienda. Un testamento muestra cómo se repartían los bienes y qué valor daba la familia a la tierra. Un contrato o acuerdo entre un patrón y un inquilino muestra lo que cada uno debía hacer. Los relatos de viajeros describen lo que vieron, pero con su mirada.",
        "Cada fuente tiene un límite. El inventario cuenta cosas, no cuenta cómo vivían los trabajadores. El testamento es escrito por un propietario y solo habla de lo que le interesa. El relato de un viajero extranjero puede exagerar o malinterpretar lo que vio. Por eso hay que cruzar varias fuentes.",
        "Contextualizar es preguntar: ¿quién escribió?, ¿cuándo?, ¿dónde?, ¿para qué? Si un inventario se hizo para pagar una deuda, quizá omite lo que no se podía vender. Si un viajero era de una familia rica, su mirada será distinta a la de un trabajador. Elegir la fuente adecuada para cada pregunta es parte del oficio histórico.",
    ],
    [("inventario", "lista detallada de bienes de una persona o propiedad"), ("testamento", "documento en que una persona dice cómo se repartirán sus bienes cuando muera"), ("contrato", "acuerdo escrito que fija obligaciones de cada parte"), ("viajero", "persona que visita un lugar y deja un relato de lo que ve"), ("inquilino", "trabajador agrícola que recibía un terreno a cambio de trabajar para el patrón")],
    [
        ("Elegir la fuente", "Pregunta: ¿cuántos animales tenía una hacienda en 1750? Opciones: inventario o poema. ¿Cuál conviene?", ["La pregunta pide una cantidad.", "El inventario enumera los animales."], "El inventario"),
        ("Identificar el límite", "Un inventario de ejemplo enumera 500 vacas y 20 herramientas. ¿Qué no dice sobre los trabajadores?", ["Solo cuenta cosas.", "No dice cómo vivían."], "No dice cómo vivían los trabajadores"),
    ],
    [
        ("Creer que un inventario cuenta cómo vivían los trabajadores.", "Solo enumera bienes; no describe la vida de las personas.", "Cruza con otros testimonios."),
        ("Aceptar sin dudar el relato de un viajero.", "Habla desde su mirada, a veces con prejuicios.", "Pregunta quién es y qué buscaba."),
    ],
    [
        ("¿Qué enumera un inventario?", "Tierras, animales, herramientas y otros bienes", "Se explicó en el primer párrafo."),
        ("¿Qué muestra un testamento?", "Cómo se repartían los bienes", "Se explicó en el primer párrafo."),
        ("¿Qué muestra un contrato entre patrón e inquilino?", "Lo que cada uno debía hacer", "Se explicó en el primer párrafo."),
    ],
    [
        ("¿Por qué un testamento tiene límites?", "Porque lo escribe un propietario y habla de lo que le interesa", "Lo dice el segundo párrafo."),
        ("Un viajero extranjero escribe: «Los trabajadores parecen felices». ¿Qué duda debe tener un historiador?", "Que hable desde su mirada y no pregunte a los trabajadores", "Es una fuente con perspectiva."),
        ("¿Por qué conviene cruzar varias fuentes?", "Porque cada una tiene límites y se complementan", "Se explicó en el segundo párrafo."),
    ],
    [
        arith("Un inventario de ejemplo anota 120 fanegas de trigo y 80 de cebada. ¿Cuántas fanegas de grano hay?", "120+80", "Se suman las dos cantidades."),
        ("Pregunta: ¿cómo se repartió una hacienda entre los hijos de un propietario? Fuentes: 1 = inventario; 2 = testamento; 3 = relato de viajero. ¿Cuál es la más adecuada?", "El testamento (la 2)", "El testamento fija cómo se reparten los bienes."),
        ("Un contrato de ejemplo dice: «El inquilino trabajará 200 días al año para el patrón a cambio de un terreno». ¿Qué obligación del inquilino muestra?", "Trabajar 200 días al año para el patrón", "El contrato fija la obligación."),
    ],
    [
        ("Un estudiante concluye: «Como el inventario no menciona maltrato, no hubo maltrato». ¿Qué límite tiene la conclusión?", "Que un inventario no registra el trato, solo cosas", "La falta de mención no prueba que no ocurriera."),
        ("¿Por qué un contrato escrito puede no mostrar las condiciones reales de vida?", "Porque lo redacta el más poderoso y no registra todo lo que ocurría", "El patrón tenía más poder para fijar los términos."),
    ],
    [
        arith("En un inventario de 1740 había 400 vacas y en otro de 1780 había 650. ¿Cuántas vacas más tenía en 1780?", "650-400", "Se resta el valor menor al mayor."),
        ("Ordena por qué tan cerca estaba la fuente de los hechos, de más cerca a más lejos: A = inventario hecho al comprar la hacienda, B = estudio escrito hoy.", "A, B", "El inventario de la época está más cerca del hecho."),
    ],
    [("Un viajero de ejemplo escribe en 1820: «Visité una hacienda de 300 cuadras y vi 40 trabajadores; parecían tranquilos». ¿Qué datos aporta y qué no puede decir?", "Aporta superficie y cantidad de trabajadores; no puede decir cómo vivían ni qué pensaban", "Los números son observables; la tranquilidad es una impresión.")],
    [("¿Qué es un inquilino?", "Un trabajador agrícola que recibía un terreno a cambio de trabajar para el patrón", "Está en el vocabulario."), ("¿Qué fuente enumera bienes?", "El inventario", "Se explicó en la clase."), ("¿Qué pregunta ayuda a contextualizar una fuente?", "¿Quién la escribió y para qué?", "Se explicó en el tercer párrafo.")],
    (
        "Lee esta fuente de ejemplo: «Inventario de 1760: 1.200 cuadras, 300 vacas, 5 arados, casa patronal, capilla y 25 inquilinos con sus familias». Escribe una tabla con tres filas: qué datos entrega, qué límite tiene, qué otra fuente pedirías. Cierra con una frase.",
        "Entrega superficie, animales, herramientas y cantidad de inquilinos. Límite: no dice cómo vivían ni qué obligaciones tenían. Pediría un contrato de inquilinaje.",
        ["indica datos del inventario", "señala un límite", "propone una fuente complementaria pertinente"],
        ["tabla de tres filas y una frase final"],
        ["inventar datos que no están en la fuente", "no señalar límite"],
        "Lee tu tabla a una persona de tu casa y dile qué fuente adicional te gustaría tener.",
    ),
    "Escribe tres preguntas sobre la hacienda y qué fuente usarías para cada una.",
    "Explica por qué un testamento es una fuente útil y a la vez limitada.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a relacionar cambio, continuidad y territorio en la hacienda: de la encomienda a la hacienda, del sebo al trigo, y la permanencia del inquilinaje. Sirve para ver cómo cambió la economía rural sin perder su base.",
    ["Sé qué es una hacienda y una merced de tierra.", "Conozco la encomienda y el servicio personal."],
    [
        "En el siglo XVI el trabajo indígena se organizaba sobre todo con la encomienda. Al disminuir la población indígena y perder fuerza la encomienda, los terratenientes empezaron a retener a trabajadores en sus tierras, dando origen al inquilinaje. Así, la hacienda reemplazó gradualmente a la encomienda como centro de la vida rural.",
        "La economía de las haciendas también cambió. En el siglo XVII predominaron la ganadería y el comercio de sebo, cueros y charqui, que se enviaban al Perú. En el siglo XVIII creció el cultivo del trigo, vendido sobre todo en Lima. Después, en el siglo XIX, el trigo chileno también se exportó a otros mercados, como California y Australia. Cada ciclo mostró que la hacienda dependía de la demanda externa.",
        "Hubo continuidades: la gran propiedad de tierra en pocas manos, el trabajo de los inquilinos y la autoridad del patrón se mantuvieron hasta bien entrado el siglo XX. El territorio explica parte de esto: el valle central era fértil y estaba cerca de Santiago y de los puertos, y por eso concentró las haciendas.",
    ],
    [("inquilinaje", "sistema en que un trabajador recibía un terreno para vivir y cultivar a cambio de trabajar para el dueño de la hacienda"), ("sebo", "grasa animal que se usaba para velas y jabón"), ("charqui", "carne secada para conservarla"), ("ciclo económico", "período en que un producto domina la economía de una región"), ("demanda externa", "necesidad de comprar un producto que viene de otros mercados")],
    [
        ("Reconocer un cambio", "En el siglo XVII dominó el sebo y en el XVIII, el trigo. ¿Qué tipo de cambio es?", ["Cambió el producto principal.", "Es un cambio de ciclo económico."], "Un cambio de ciclo económico"),
        ("Reconocer una continuidad", "Los inquilinos siguieron trabajando para el patrón hasta el siglo XX. ¿Es cambio o continuidad?", ["Se mantuvo por siglos.", "Es una permanencia."], "Una continuidad"),
    ],
    [
        ("Creer que la economía de la hacienda siempre produjo lo mismo.", "Pasó del sebo al trigo según la demanda externa.", "Ubica el ciclo en el siglo."),
        ("Pensar que el inquilinaje terminó con la Colonia.", "Se mantuvo en el siglo XIX y gran parte del XX.", "Distingue colonia y república."),
    ],
    [
        ("¿Qué producto predominó en el siglo XVII en las haciendas?", "Sebo y cueros (ganadería)", "Se explicó en el segundo párrafo."),
        ("¿A qué ciudad se vendía sobre todo el trigo en el siglo XVIII?", "Lima", "Se explicó en el segundo párrafo."),
        ("¿Qué sistema reemplazó gradualmente a la encomienda en el campo?", "El inquilinaje y la hacienda", "Se explicó en el primer párrafo."),
    ],
    [
        ("¿Por qué el valle central concentró las haciendas?", "Porque era fértil y estaba cerca de Santiago y de los puertos", "Lo dice el tercer párrafo."),
        ("¿Qué muestra que la hacienda dependía de la demanda externa?", "Que su producto principal cambió según lo que se compraba en otros mercados", "El sebo y el trigo respondían a la demanda."),
        ("Menciona una continuidad de la hacienda según la clase.", "La gran propiedad en pocas manos o la autoridad del patrón", "Se nombra en el tercer párrafo."),
    ],
    [
        arith("Una hacienda de ejemplo vendió 200 quintales de sebo en el siglo XVII y 500 quintales de trigo en el XVIII. ¿Cuántos quintales más vendió en el XVIII?", "500-200", "Se resta la cifra menor a la mayor."),
        ("Un mapa de ejemplo muestra haciendas entre Santiago y el Maule. ¿Por qué no hay haciendas coloniales al sur del Biobío?", "Porque allí estaba el territorio mapuche, más allá de la frontera", "La frontera del Biobío limitaba la expansión de las haciendas."),
        ("Un precio de ejemplo: el trigo valía 10 pesos en 1700 y 25 en 1750. ¿Qué podía hacer un hacendado con ese cambio?", "Cultivar más trigo porque se vendía mejor", "El precio mayor estimula la producción."),
    ],
    [
        ("Un estudiante dice: «Como cambió el producto, cambió toda la sociedad rural». ¿Qué continuidad ignora?", "La gran propiedad, el inquilinaje y la autoridad del patrón", "Siguieron igual por siglos."),
        ("¿Qué riesgo tenía depender de un solo producto como el trigo?", "Que si caía la demanda o el precio, la hacienda perdía ingresos", "La dependencia externa genera riesgos."),
    ],
    [
        ("Ordena los ciclos de más antiguo a más reciente: A = trigo para Lima, B = sebo y cueros, C = trigo para California.", "B, A, C", "El orden es siglo XVII, XVIII y XIX."),
        arith("En un año de ejemplo una hacienda envió 40 sacos de trigo a Lima por barco y 25 por tierra. ¿Cuántos sacos envió?", "40+25", "Se suman los dos envíos."),
    ],
    [("Un cuadro de ejemplo dice: «1650: sebo y cueros. 1750: trigo. 1850: trigo a California y Australia». ¿Qué dos mercados externos se mencionan para 1850?", "California y Australia", "El cuadro nombra esos dos mercados para 1850.")],
    [("¿Qué es el inquilinaje?", "Un sistema en que el trabajador recibía un terreno a cambio de trabajar para el patrón", "Está en el vocabulario."), ("¿Qué es el sebo?", "Grasa animal que se usaba para velas y jabón", "Está en el vocabulario."), ("¿Qué cambió y qué continuó en la hacienda?", "Cambió el producto principal y continuó la gran propiedad y el inquilinaje", "Se explicó en la clase.")],
    (
        "Completa una tabla con tres filas: siglo XVII, siglo XVIII y siglo XIX. Escribe en cada una el producto principal de la hacienda y a quién se vendía. Luego escribe una frase que indique una continuidad y un cambio.",
        "XVII: sebo y cueros al Perú. XVIII: trigo a Lima. XIX: trigo a California y Australia. Cambió el producto y el mercado; continuó la gran propiedad y el inquilinaje.",
        ["completa los tres siglos", "indica producto y mercado", "señala un cambio y una continuidad"],
        ["tabla de tres filas y una frase"],
        ["confundir los siglos", "decir que todo cambió"],
        "Cuenta a una persona de tu casa por qué la hacienda cambió de producto.",
    ),
    "Dibuja una línea de tiempo con los tres ciclos de la hacienda.",
    "Explica en tres líneas por qué la frontera del Biobío limitó el avance de las haciendas.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a contrastar los actores de la hacienda (patrón, inquilino, peón, mujeres y personas esclavizadas), sus causas y perspectivas. Sirve para entender una sociedad rural jerárquica.",
    ["Conozco la hacienda y el inquilinaje.", "Sé que cada actor tiene una perspectiva."],
    [
        "En la hacienda había varios grupos. El patrón o hacendado era el dueño de la tierra y tenía autoridad sobre la vida de la hacienda: decidía qué se cultivaba, quién trabajaba y quién vivía ahí. Los inquilinos recibían un terreno para vivir y cultivar, y debían trabajar para el patrón y respetarlo. Los peones eran trabajadores sin tierra, a veces temporales. También había personas indígenas, mestizas y, en menor número, esclavizadas.",
        "Las relaciones eran de dependencia y de lealtad. El patrón protegía y daba tierra; el inquilino daba trabajo y obediencia. Esto se llama a veces relación paternalista, porque el patrón se presentaba como protector, aunque el poder era muy desigual. Las mujeres cumplían roles distintos: las de la familia propietaria administraban la casa y a veces la hacienda al enviudar; las mujeres de los inquilinos cultivaban, cocinaban, hilaban y criaban animales.",
        "Cada actor veía la hacienda distinto. El patrón veía propiedad, prestigio y producción. El inquilino veía un terreno y seguridad, pero también obligaciones y falta de libertad. Para contrastar perspectivas, hay que preguntar qué ganaba y qué perdía cada uno y quién habla en cada fuente.",
    ],
    [("patrón", "dueño de la hacienda con autoridad sobre sus trabajadores"), ("peón", "trabajador agrícola sin tierra propia, a veces temporal"), ("dependencia", "situación en que una persona necesita a otra para vivir o trabajar"), ("lealtad", "fidelidad y obediencia debida a alguien"), ("paternalismo", "trato en que el poderoso se presenta como protector de los demás")],
    [
        ("Distinguir roles", "Un trabajador de ejemplo recibe un terreno para vivir y debe trabajar para el dueño. ¿Es inquilino o peón?", ["Recibe un terreno.", "Eso es inquilino."], "Inquilino"),
        ("Contrastar perspectivas", "El patrón dice «protejo a mis trabajadores» y el inquilino dice «no puedo irme». ¿Qué diferencia de perspectiva muestran?", ["El patrón destaca la protección.", "El inquilino destaca la falta de libertad."], "El patrón destaca la protección; el inquilino, la falta de libertad"),
    ],
    [
        ("Creer que inquilinos y peones eran lo mismo.", "El inquilino tenía terreno y obligaciones fijas; el peón no tenía tierra.", "Define cada uno con un dato."),
        ("Creer que la relación entre patrón e inquilino era entre iguales.", "El poder estaba muy desigualmente repartido.", "Busca quién fijaba las reglas."),
    ],
    [
        ("¿Quién era el dueño de la hacienda?", "El patrón o hacendado", "Está en el vocabulario."),
        ("¿Qué recibía un inquilino?", "Un terreno para vivir y cultivar", "Se explicó en el primer párrafo."),
        ("¿Quién era un peón?", "Un trabajador agrícola sin tierra, a veces temporal", "Está en el vocabulario."),
    ],
    [
        ("¿Qué daba el inquilino a cambio de la tierra?", "Su trabajo y su obediencia", "Se explicó en el segundo párrafo."),
        ("¿Qué hacían las mujeres de las familias de inquilinos?", "Cultivaban, cocinaban, hilaban y criaban animales", "Se enumeran en el segundo párrafo."),
        ("¿Por qué se habla de paternalismo?", "Porque el patrón se presentaba como protector, aunque el poder era desigual", "Está en el vocabulario."),
    ],
    [
        arith("Una hacienda de ejemplo tiene 25 familias de inquilinos y 10 familias de peones. ¿Cuántas familias trabajan en ella?", "25+10", "Se suman los dos grupos."),
        ("Una fuente de ejemplo del patrón dice: «Mis inquilinos son como de la familia». Otra, de un inquilino, dice: «Debo pedir permiso para salir». ¿Qué contradicción muestran?", "Una habla de cercanía y la otra, de falta de libertad", "Cada actor describe la relación de forma distinta."),
        ("Una viuda propietaria de ejemplo administra la hacienda tras la muerte de su esposo. ¿Qué rol de género ilustra?", "Que una mujer de la élite podía administrar bienes al enviudar", "Se mencionó en el segundo párrafo."),
    ],
    [
        ("Un estudiante dice: «El patrón protegía, por lo tanto no había desigualdad». ¿Qué error comete?", "Una protección puede coexistir con una relación muy desigual", "El paternalismo mantiene el poder del patrón."),
        ("¿Por qué conviene buscar la voz de un inquilino y no solo del patrón?", "Porque cada uno cuenta lo que vive y se complementan", "Evita ver solo el lado del poderoso."),
    ],
    [
        ("Ordena de menos a más poder sobre las decisiones de la hacienda: A = patrón, B = inquilino.", "B, A", "El patrón decidía qué se cultivaba, quién trabajaba y quién vivía en la hacienda; el inquilino debía obedecer."),
        arith("En una hacienda de ejemplo hay 120 personas; 20 son de la familia del patrón. ¿Cuántas no lo son?", "120-20", "Se restan las del patrón del total."),
    ],
    [("Una lista de ejemplo de una hacienda de 1790: «Patrón y familia, 8 personas; inquilinos con familias, 60 personas; peones, 12 personas». ¿Cuántas personas viven allí y qué grupo es el más numeroso?", "80 personas; los inquilinos", "8 más 60 más 12 es 80, y 60 es el número mayor.")],
    [("¿Qué es la lealtad?", "La fidelidad y obediencia debida a alguien", "Está en el vocabulario."), ("¿Qué grupo vivía con tierra pero con obligaciones?", "Los inquilinos", "Se explicó en el primer párrafo."), ("¿Qué roles tenían las mujeres de la élite?", "Administrar la casa y a veces la hacienda al enviudar", "Se explicó en el segundo párrafo.")],
    (
        "Escribe una tabla con cuatro actores: patrón, inquilino, peón y mujer de un inquilino. Para cada uno anota qué recibía y qué daba a cambio. Termina con una frase que explique por qué sus perspectivas podían ser distintas.",
        "Patrón: recibía trabajo y daba tierra y protección. Inquilino: recibía terreno y daba trabajo. Peón: recibía pago o comida y daba trabajo temporal. Mujer de inquilino: aportaba cultivo y labores domésticas. Sus perspectivas diferían porque tenían poder y derechos desiguales.",
        ["incluye los cuatro actores", "indica qué recibía y qué daba", "explica la diferencia de perspectivas"],
        ["tabla de cuatro filas y una frase final"],
        ["decir que todos tenían el mismo poder", "olvidar a las mujeres"],
        "Comparte tu tabla con una persona de tu casa y comenten quién tenía más poder.",
    ),
    "Escribe un diálogo de seis líneas entre un patrón y un inquilino con perspectivas distintas.",
    "Escribe una pregunta sobre la vida de los niños en una hacienda.",
)

# ================================================================ clase 5
lesson(
    OA, 5,
    "Aprenderé a construir un argumento con evidencia sobre el papel de la hacienda en la formación del Chile colonial: economía rural, élite terrateniente y sociedad estamental. Sirve para explicar por qué la hacienda fue clave.",
    ["Conozco los actores y los ciclos de la hacienda.", "Sé que un argumento tiene afirmación, evidencia y límite."],
    [
        "Un rasgo del Chile colonial fue la élite terrateniente: un grupo de familias que concentraba la tierra, la riqueza y los cargos locales, como los de alcalde o regidor del cabildo. Esas familias aseguraban la herencia de las tierras con el mayorazgo, una institución por la cual la propiedad se transmitía completa al hijo mayor y no se dividía. Así la tierra se mantenía en pocas manos.",
        "La sociedad era estamental, es decir, dividida en grupos con distinto honor, derechos y oficios según el nacimiento. En la cima estaban los hacendados y sus familias; después, los artesanos, comerciantes y pequeños propietarios; y abajo, inquilinos, peones, indígenas y esclavizados. El mundo rural reforzaba esta jerarquía: el patrón mandaba y los trabajadores obedecían.",
        "Un argumento posible es: «La hacienda fue el centro de la economía y de la sociedad coloniales porque concentró la tierra, organizó el trabajo en el inquilinaje y sostuvo el poder de una élite». La evidencia puede ser un inventario, un contrato de inquilinaje y una lista de cargos del cabildo. El límite es que esas fuentes dicen poco sobre la vida de los inquilinos.",
    ],
    [("élite terrateniente", "grupo de familias dueñas de grandes extensiones de tierra"), ("mayorazgo", "institución para transmitir una propiedad completa al hijo mayor"), ("sociedad estamental", "sociedad dividida en grupos con distinto honor y derechos según el nacimiento"), ("cabildo", "consejo del gobierno local en las ciudades coloniales"), ("jerarquía", "orden de grupos de mayor a menor poder")],
    [
        ("Reconocer una institución", "Una familia de ejemplo asegura que su tierra pase completa al hijo mayor. ¿Qué institución usa?", ["La tierra no se divide.", "Se llama mayorazgo."], "Mayorazgo"),
        ("Clasificar en la jerarquía", "¿Qué grupo estaba en la cima de la sociedad estamental rural: los hacendados o los peones?", ["Los hacendados tenían tierra y cargos.", "Los peones estaban abajo."], "Los hacendados"),
    ],
    [
        ("Creer que todos los grupos tenían los mismos derechos.", "La sociedad estamental repartía derechos según el nacimiento.", "Ubica cada grupo en la jerarquía."),
        ("Dar solo la afirmación sin evidencia.", "Sin datos es solo una opinión.", "Agrega un inventario, un contrato o una lista de cargos."),
    ],
    [
        ("¿Qué es una élite terrateniente?", "Un grupo de familias dueñas de grandes extensiones de tierra", "Está en el vocabulario."),
        ("¿Qué hacía el mayorazgo?", "Transmitía la propiedad completa al hijo mayor", "Está en el vocabulario."),
        ("¿Qué es el cabildo?", "El consejo del gobierno local en las ciudades coloniales", "Está en el vocabulario."),
    ],
    [
        ("¿Por qué el mayorazgo mantenía la tierra en pocas manos?", "Porque evitaba dividirla entre varios herederos", "Lo explica el primer párrafo."),
        ("¿Qué significa que la sociedad era estamental?", "Que estaba dividida en grupos con distinto honor y derechos según el nacimiento", "Está en el vocabulario."),
        ("¿Qué grupos estaban abajo en la jerarquía rural?", "Inquilinos, peones, indígenas y esclavizados", "Se enumeran en el segundo párrafo."),
    ],
    [
        arith("Una familia de ejemplo posee 3 haciendas con 400 cuadras cada una. ¿Cuántas cuadras tiene en total?", "3*400", "Se multiplica el número de haciendas por las cuadras."),
        ("Datos de ejemplo de un cabildo de 1780: «De 6 regidores, 5 eran dueños de haciendas». ¿Qué afirmación apoyan estos datos?", "Que la élite terrateniente tenía poder político local", "La mayoría de los cargos estaban en manos de hacendados."),
        ("Elige la mejor evidencia para «La hacienda organizó el trabajo en el inquilinaje»: 1 = un contrato de inquilino con obligaciones de trabajo; 2 = un poema; 3 = un mapa de ríos.", "La 1", "El contrato muestra obligaciones concretas."),
    ],
    [
        ("Un estudiante concluye: «Como había cabildo, todos participaban en el gobierno». ¿Qué error comete?", "Los cargos del cabildo los ocupaban las élites, no todos", "La participación estaba restringida por la jerarquía."),
        ("¿Por qué un buen argumento sobre la hacienda debe incluir un límite?", "Porque las fuentes dicen poco sobre la vida de los inquilinos y otros grupos", "El límite reconoce lo que la evidencia no muestra."),
    ],
    [
        ("Ordena las partes de un argumento: A = límite, B = afirmación, C = evidencia.", "B, C, A", "Primero se afirma, luego se prueba y al final se declara el límite."),
        arith("En un cabildo de ejemplo hay 8 cargos y 6 son de hacendados. ¿Cuántos no lo son?", "8-6", "Se restan los hacendados del total."),
    ],
    [("Datos de ejemplo: «En 1790, el 70 % de las tierras del valle pertenecía a 10 familias». ¿Qué afirmación apoya este dato: A = la tierra estaba concentrada en pocas familias; B = la tierra estaba repartida por igual entre todas?", "A", "Diez familias con el 70 % de la tierra muestran concentración. El dato no dice cómo vivían los trabajadores: ese es su límite.")],
    [("¿Qué es una sociedad estamental?", "Una sociedad dividida en grupos con distinto honor y derechos según el nacimiento", "Está en el vocabulario."), ("¿Qué fuentes sirven de evidencia?", "Inventario, contrato de inquilinaje y lista de cargos del cabildo", "Se nombran en el tercer párrafo."), ("¿Qué institución mantenía la tierra en pocas manos?", "El mayorazgo", "Se explicó en el primer párrafo.")],
    (
        "Responde en cinco líneas: «¿Por qué fue importante la hacienda en el Chile colonial?». Usa esta evidencia de ejemplo: inventario con 2.000 cuadras; contrato de inquilino que debe trabajar 200 días; cabildo con 5 hacendados de 6 regidores; mayorazgo. Incluye afirmación, dos datos y un límite.",
        "La hacienda concentró la tierra, organizó el trabajo y sostuvo el poder de una élite. Datos: cabildo con 5 hacendados de 6 y contrato de 200 días de trabajo. Límite: no sabemos cómo vivían los inquilinos.",
        ["escribe una afirmación clara", "usa al menos dos datos", "incluye un límite"],
        ["texto de cinco líneas"],
        ["no incluir límite", "decir que todos participaban igual"],
        "Lee tu texto a una persona de tu casa y pídele que identifique la afirmación.",
    ),
    "Dibuja una pirámide de la sociedad estamental rural con cinco grupos.",
    "Escribe una frase que explique cómo el mayorazgo mantenía la riqueza en pocas manos.",
)

# ================================================================ clase 6
lesson(
    OA, 6,
    "Aprenderé a evaluar las proyecciones de la hacienda en los siglos XIX y XX y los límites de lo que sabemos. Sirve para entender qué parte de la sociedad rural chilena viene de la Colonia.",
    ["Conozco la élite terrateniente, el inquilinaje y la sociedad estamental.", "Sé construir un argumento con afirmación, evidencia y límite."],
    [
        "La hacienda no desapareció con la Independencia. En el siglo XIX, muchas familias terratenientes siguieron siendo parte de la élite política y económica del país. El inquilinaje se mantuvo y, en algunas zonas, el trigo y otros productos se exportaron a nuevos mercados. Hasta bien avanzado el siglo XX, parte del campo chileno siguió organizado en grandes propiedades con trabajadores dependientes.",
        "En la década de 1960 el Estado impulsó la Reforma Agraria, que expropió y repartió grandes propiedades. En 1967 se aprobó una ley que permitió la sindicalización campesina. Con estos cambios fue desapareciendo el inquilinaje tradicional. Aun así, en el campo persisten desigualdades de propiedad de la tierra y de condiciones de trabajo.",
        "Evaluar una proyección es preguntar cuánto se parece el presente al pasado y qué cambió en medio. No todo el campo era hacienda ni todas las haciendas eran iguales. Además, las fuentes de la élite hablan más de los dueños que de los trabajadores. Por eso hay que declarar los límites antes de concluir.",
    ],
    [("Reforma Agraria", "proceso de los años 1960 y 1970 en que el Estado expropió y repartió grandes propiedades rurales"), ("sindicalización campesina", "organización de los trabajadores del campo en sindicatos"), ("expropiar", "quitar una propiedad por decisión del Estado, con una compensación"), ("proyección", "continuidad de un rasgo hacia épocas posteriores"), ("desigualdad", "diferencia injusta en riqueza, poder o derechos")],
    [
        ("Reconocer una proyección", "¿Qué sistema de trabajo de la hacienda colonial se mantuvo hasta el siglo XX?", ["La clase nombra un sistema que duró siglos.", "Es el inquilinaje."], "El inquilinaje"),
        ("Reconocer un cambio", "En la década de 1960 el Estado repartió grandes propiedades. ¿Cómo se llama ese proceso?", ["Se repartieron grandes campos.", "Es la Reforma Agraria."], "Reforma Agraria"),
    ],
    [
        ("Creer que la hacienda desapareció con la Independencia.", "Siguió existiendo y las familias terratenientes mantuvieron su poder.", "Revisa los siglos XIX y XX."),
        ("Pensar que todo el campo chileno era hacienda.", "Había pequeñas propiedades y otras formas de vida rural.", "Evita generalizar."),
    ],
    [
        ("¿Qué siglo vio terminar el inquilinaje tradicional, según la clase?", "El siglo XX", "Se explicó en el segundo párrafo."),
        ("¿Qué hizo la Reforma Agraria?", "Expropió y repartió grandes propiedades", "Está en el vocabulario."),
        ("¿Qué se aprobó en 1967?", "Una ley que permitió la sindicalización campesina", "Se explicó en el segundo párrafo."),
    ],
    [
        ("¿Por qué la hacienda no desapareció con la Independencia?", "Porque las familias terratenientes mantuvieron su poder y el inquilinaje continuó", "Lo dice el primer párrafo."),
        ("Menciona una desigualdad actual relacionada con el campo, según la clase.", "La propiedad de la tierra o las condiciones de trabajo", "Se nombra en el segundo párrafo."),
        ("¿Por qué las fuentes de la élite tienen límites?", "Porque hablan más de los dueños que de los trabajadores", "Lo dice el tercer párrafo."),
    ],
    [
        arith("La Reforma Agraria se impulsó en la década de 1960 y la ley de sindicalización campesina es de 1967. Si una hacienda existió desde 1750, ¿cuántos años pasaron hasta 1967?", "1967-1750", "Se resta el año de inicio al de término."),
        ("Una afirmación de ejemplo dice: «Después de la Reforma Agraria no quedó ninguna desigualdad en el campo». ¿Qué dice la clase al respecto?", "Que aún persisten desigualdades de propiedad y de condiciones de trabajo", "La clase lo señala."),
        ("Elige la mejor fuente para evaluar «los inquilinos vivieron mejor o peor con la reforma»: 1 = testimonio de un campesino de esa época; 2 = un mapa de ríos; 3 = una receta.", "La 1", "El testimonio muestra su experiencia."),
    ],
    [
        ("Un estudiante dice: «El campo de hoy es igual al de la Colonia». ¿Qué cambios ignora?", "La Reforma Agraria, la sindicalización campesina y otros cambios del siglo XX", "Hubo transformaciones importantes."),
        ("¿Por qué no se puede concluir que todas las haciendas eran iguales?", "Porque variaban en tamaño, producción y trato, según la zona y la época", "La evidencia muestra diversidad."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = Reforma Agraria (década de 1960), B = surgimiento de las haciendas (siglos XVII y XVIII), C = Independencia de Chile (siglo XIX).", "B, C, A", "Los períodos en orden son XVII-XVIII, XIX y la década de 1960."),
        arith("Si en 1960 una hacienda de ejemplo tenía 3.000 hectáreas y se expropiaron 1.200, ¿cuántas hectáreas le quedaron?", "3000-1200", "Se restan las hectáreas expropiadas."),
    ],
    [("Una entrevista de ejemplo: «Mi abuelo era inquilino; después de 1967 formó un sindicato». ¿Qué cambio de la clase ilustra este relato?", "La sindicalización campesina", "El sindicato fue posible por la ley de 1967.")],
    [("¿Qué es expropiar?", "Quitar una propiedad por decisión del Estado, con una compensación", "Está en el vocabulario."), ("¿Qué se mantuvo en el siglo XIX de la hacienda colonial?", "La élite terrateniente y el inquilinaje", "Se explicó en el primer párrafo."), ("¿Por qué conviene declarar los límites antes de concluir?", "Porque las fuentes no muestran todo y no se debe generalizar", "Se explicó en el tercer párrafo.")],
    (
        "Escribe un párrafo de seis líneas: «Qué viene de la hacienda colonial y qué cambió». Incluye dos proyecciones que se mantuvieron en el siglo XIX o XX, dos cambios del siglo XX y un límite. Usa solo los datos de la clase.",
        "Se mantuvieron la élite terrateniente y el inquilinaje hasta el siglo XX. Cambiaron con la Reforma Agraria y la sindicalización campesina de 1967. Límite: no sabemos cómo vivía cada familia.",
        ["incluye dos proyecciones", "incluye dos cambios", "declara un límite"],
        ["párrafo de seis líneas"],
        ["decir que todo cambió", "decir que nada cambió"],
        "Lee el párrafo a una persona de tu casa y pregúntale si alguien de su familia conoció el campo antiguo.",
    ),
    "Escribe una frase con cada término del vocabulario.",
    "Escribe una pregunta para entrevistar a una persona mayor sobre cómo era el campo antes.",
)
