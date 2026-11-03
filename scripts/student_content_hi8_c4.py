"""Cuaderno del estudiante, 8.º básico Historia, Geografía y Ciencias Sociales: OA 22 (desarrollo regional y sustentabilidad)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 22"
MAT = "Lápiz y papel; una calculadora es opcional. Las tablas y los casos (de ejemplo, con datos inventados) están escritos en cada ejercicio; no necesitas internet."

# ---------------------------------------------------------------- Clase 1
F1 = ("Tabla de ejemplo (regiones inventadas, datos inventados). "
      "Región Alfa: IDH 0,82; esperanza de vida 80 años; escolaridad promedio 12 años; ingreso medio mensual por persona $900.000. "
      "Región Beta: IDH 0,76; esperanza de vida 78 años; escolaridad 11 años; ingreso $700.000. "
      "Región Gamma: IDH 0,70; esperanza de vida 74 años; escolaridad 9 años; ingreso $500.000.")
build(
    OA, 1, F1,
    use="Aprenderé qué es el desarrollo, en qué se diferencia del crecimiento económico y cómo lo mide el índice de desarrollo humano (IDH). Sirve para analizar las regiones de Chile con más de un indicador.",
    prior=["Sé leer tablas con varias columnas.", "Sé qué es una región.", "Sé comparar números decimales sencillos."],
    explain=[
        "El crecimiento económico es el aumento de lo que produce y gana un país o región. El desarrollo es un concepto más amplio: busca que las personas tengan una vida larga y saludable, acceso a educación y recursos suficientes para vivir bien. Una región puede crecer económicamente y tener un desarrollo bajo si esa riqueza no mejora la vida de la mayoría.",
        "El índice de desarrollo humano, o IDH, es una medida que combina tres dimensiones: salud, medida con la esperanza de vida al nacer; educación, medida con los años de escolaridad; e ingreso, medido con el ingreso medio por persona. El IDH va de 0 a 1: mientras más cerca de 1, mayor desarrollo humano. Se calcula para países y también para regiones.",
        "Para usar el IDH hay que leerlo con cuidado. Un número solo no dice cuál dimensión está más débil: dos regiones pueden tener el mismo IDH por razones distintas. Por eso miro también las tres dimensiones por separado. Y recuerdo que el IDH no mide todo: no incluye, por ejemplo, el cuidado del medio ambiente ni la seguridad de las personas.",
    ],
    vocab=[("crecimiento económico", "aumento de la producción y los ingresos"), ("desarrollo humano", "mejora de la salud, la educación y los recursos para vivir bien"), ("IDH", "índice que combina salud, educación e ingreso, de 0 a 1"), ("esperanza de vida", "años que se espera que viva una persona al nacer"), ("escolaridad", "años de estudio que alcanza una persona")],
    worked=[
        ("Leer una dimensión", "En la tabla de ejemplo de una región Sigma, la escolaridad es de 10 años y la esperanza de vida, de 76. ¿Qué dimensión del IDH mide cada dato?",
         ["Los años de estudio miden educación.", "Los años de vida esperados miden salud."], "Escolaridad: educación; esperanza de vida: salud"),
        ("Distinguir crecimiento y desarrollo", "Una región duplicó su producción, pero la escolaridad y la esperanza de vida no cambiaron. ¿Creció? ¿Se desarrolló?",
         ["Su producción aumentó: creció.", "Las otras dimensiones no mejoraron."], "Creció económicamente, pero no necesariamente se desarrolló"),
    ],
    mistakes=[
        ("Decir que desarrollo es lo mismo que riqueza.", "El desarrollo incluye salud y educación, no solo ingreso.", "Revisa las tres dimensiones del IDH."),
        ("Pensar que un IDH alto significa que no hay problemas.", "El IDH no mide todo, como el medio ambiente.", "Úsalo junto con otros indicadores."),
    ],
    T=[
        ("En Geografía: ¿qué mide el IDH?", "Salud, educación e ingreso en un solo índice", "Combina tres dimensiones."),
        ("En Geografía: ¿qué diferencia hay entre crecimiento y desarrollo?", "El crecimiento es aumento de la producción y los ingresos; el desarrollo incluye además salud y educación", "El desarrollo es más amplio."),
        ("{F} ¿Qué región tiene el IDH más alto?", "Alfa", "Tiene 0,82, la cifra mayor."),
        ("{F} ¿Qué dimensión del IDH mide la escolaridad? A) salud, B) educación, C) ingreso.", "B", "Los años de estudio son educación."),
        ("=", "{F} ¿Cuántos años más de escolaridad tiene Alfa que Gamma?", "12-9", "Se restan los años de escolaridad."),
        ("=", "{F} ¿Cuántos años más de esperanza de vida tiene Alfa que Gamma?", "80-74", "Se restan las esperanzas de vida."),
        ("=", "{F} ¿Cuántos pesos más de ingreso medio mensual tiene Alfa que Gamma?", "900000-500000", "Se restan los ingresos."),
        ("{F} ¿Cuál afirmación es correcta? A) Si el IDH de Beta es 0,76, está más cerca de 1 que Gamma, B) Gamma tiene más desarrollo que Beta, C) el IDH no puede compararse.", "A", "0,76 está más cerca de 1 que 0,70."),
        ("Una región tiene ingresos muy altos, pero poca escolaridad y baja esperanza de vida. ¿Tiene un desarrollo alto? Explica.", "No necesariamente, porque el IDH también depende de la salud y la educación", "Una sola dimensión alta no basta."),
        ("{F} ¿Qué región tiene la esperanza de vida más baja? A) Alfa, B) Beta, C) Gamma.", "C", "Tiene 74 años, menos que 78 y 80."),
        ("Explica con una frase por qué dos regiones pueden tener el mismo IDH y problemas distintos.", "Porque el IDH combina tres dimensiones y una región puede ser débil en salud y otra en educación", "El número final esconde las dimensiones."),
        ("Evalúa la frase «Si el ingreso sube, el desarrollo sube automáticamente». ¿Qué le falta?", "Que también deben mejorar la salud y la educación", "El desarrollo es más amplio que el ingreso."),
        ("¿Qué aspecto importante NO mide el IDH? A) el medio ambiente, B) la esperanza de vida, C) los años de escolaridad.", "A", "El IDH no incluye el cuidado ambiental."),
    ],
    ctx=("Un diario de ejemplo titula: «La Región Delta es la más desarrollada porque tiene el ingreso más alto». ¿Qué dos dimensiones debes revisar antes de aceptar el titular?", "La salud y la educación", "El desarrollo humano incluye las tres dimensiones."),
    sc=[("En Geografía: ¿qué es la esperanza de vida?", "Los años que se espera que viva una persona al nacer", "Mide la dimensión de salud."),
        ("¿Entre qué valores va el IDH?", "Entre 0 y 1", "Más cerca de 1 es mayor desarrollo humano."),
        ("Nombra una dimensión del IDH.", "Por ejemplo: salud, educación o ingreso", "Son las tres dimensiones que mide.")],
    op=("{F} Compara Alfa y Gamma con las tres dimensiones del IDH: escribe la diferencia de cada una y una frase que explique por qué sus IDH son distintos. Agrega una cosa que el IDH no mide.",
        "Salud: 80 frente a 74 años. Educación: 12 frente a 9 años. Ingreso: $900.000 frente a $500.000. Alfa tiene un IDH más alto porque es mejor en las tres dimensiones. El IDH no mide el cuidado del medio ambiente.",
        ["compara las tres dimensiones", "explica la diferencia del IDH", "nombra una limitación"], ["tres comparaciones, una explicación y una limitación"], ["mirar solo el ingreso", "olvidar la limitación"], "Pide a una persona de tu casa que te diga qué agregaría al IDH."),
    reinforce="Pregunta a alguien de tu casa hasta qué curso estudió y compáralo con 12 años de escolaridad.",
    extend="Escribe un indicador que agregarías al IDH para medir el cuidado ambiental.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = ("Tabla de ejemplo de la Región Delta (inventada, datos inventados). IDH regional: 0,78. "
      "Comuna Centro: 60.000 habitantes, IDH 0,85, ingreso medio mensual $1.000.000. "
      "Comuna Costa: 30.000 habitantes, IDH 0,70, ingreso $600.000. "
      "Comuna Cordillera: 10.000 habitantes, IDH 0,62, ingreso $300.000.")
build(
    OA, 2, F2,
    use="Aprenderé a leer tablas de desarrollo por región y a reconocer que un promedio regional puede ocultar desigualdades internas. Sirve para usar datos con espíritu crítico.",
    prior=["Sé qué es el IDH y sus tres dimensiones.", "Sé leer tablas y calcular promedios.", "Sé distinguir fuentes primarias y secundarias."],
    explain=[
        "Un indicador regional resume la situación de toda una región con un solo número, como el IDH regional. Es útil para comparar regiones, pero tiene un límite: ese número es un promedio, y un promedio mezcla lugares muy distintos. Una región puede tener un IDH alto en total y, a la vez, comunas con situaciones muy difíciles.",
        "Para detectar las desigualdades internas se desagregan los datos, es decir, se dividen en grupos más pequeños, como las comunas. Así se ve qué parte de la población vive mejor o peor. También conviene mirar el rango, que es la diferencia entre el valor más alto y el más bajo, y quién está en cada extremo.",
        "Al usar una tabla reviso quién la produjo, en qué año y con qué unidad. Una fuente estadística oficial se construye con censos y encuestas; una opinión no es un dato. Además verifico que las cifras sean de la misma época. Con esos cuidados, puedo usar los datos como evidencia para decir qué territorios necesitan más apoyo.",
    ],
    vocab=[("promedio", "valor que resume un conjunto de datos y puede ocultar diferencias"), ("desagregar", "dividir datos en grupos más pequeños, como comunas"), ("rango", "diferencia entre el valor más alto y el más bajo"), ("desigualdad interna", "diferencias dentro de una misma región"), ("fuente estadística", "documento con datos construidos con censos o encuestas")],
    worked=[
        ("Calcular un rango", "En una región de ejemplo, el ingreso de una comuna es $800.000 y el de otra, $350.000. ¿Cuál es el rango?",
         ["Resto el valor menor al mayor.", "800.000 - 350.000 = 450.000."], "$450.000"),
        ("Detectar lo que oculta el promedio", "Una región de ejemplo tiene IDH promedio 0,75. Una comuna tiene 0,88 y otra, 0,55. ¿Qué oculta el promedio?",
         ["El promedio mezcla a una comuna con alto desarrollo y a otra con bajo desarrollo.", "Los habitantes de la segunda viven una situación mucho más difícil."], "La gran diferencia entre las dos comunas"),
    ],
    mistakes=[
        ("Creer que si el promedio es alto, todas las comunas están bien.", "El promedio mezcla situaciones distintas.", "Desagrega los datos por comuna."),
        ("Usar cifras de años distintos como si fueran del mismo.", "Los datos cambian con el tiempo.", "Comprueba el año y la unidad de cada cifra."),
    ],
    T=[
        ("En Geografía: ¿qué significa desagregar datos?", "Dividirlos en grupos más pequeños, como comunas", "Permite ver diferencias internas."),
        ("En Geografía: ¿qué es el rango de un conjunto de datos?", "La diferencia entre el valor más alto y el más bajo", "Mide qué tan separados están los extremos."),
        ("{F} ¿Qué comuna tiene el IDH más bajo?", "Cordillera", "Tiene 0,62, la cifra menor."),
        ("=", "{F} ¿Cuántos habitantes tiene en total la región Delta?", "60000+30000+10000", "Se suman las poblaciones de las tres comunas."),
        ("=", "{F} ¿Cuál es el rango del ingreso medio mensual entre las comunas?", "1000000-300000", "Se resta el ingreso menor al mayor."),
        ("=", "{F} ¿Cuál es el ingreso medio de la región, pesando cada comuna por su población? (Suma los ingresos totales de las tres comunas y divide por 100.000 habitantes.)", "(60000*1000000+30000*600000+10000*300000)/100000", "Se pesa el ingreso de cada comuna por su población."),
        ("{F} El IDH regional es 0,78. ¿Qué comuna está por debajo de ese promedio en más de 0,10? A) Cordillera, B) Costa, C) Centro.", "A", "0,78 menos 0,62 es 0,16; Costa está a 0,02."),
        ("{F} ¿Qué porcentaje de la población de Delta vive en la comuna Centro?", "60 %", "60.000 de 100.000 habitantes."),
        ("=", "{F} ¿Cuántas veces es mayor el ingreso de Costa que el de Cordillera?", "600000/300000", "Se divide un ingreso por el otro."),
        ("{F} Un informe dice: «Delta es una región desarrollada porque su IDH es 0,78». ¿Qué le falta considerar?", "Las diferencias entre comunas, como la Cordillera con 0,62", "El promedio oculta desigualdades."),
        ("{F} ¿Qué comuna necesita más apoyo para mejorar sus condiciones de vida según la tabla y por qué?", "Cordillera, porque tiene el menor IDH y el menor ingreso", "Sus indicadores son los más bajos."),
        ("Para conocer la esperanza de vida por comuna, ¿qué fuente es más confiable? A) una estadística oficial basada en censos, B) la opinión de un vecino, C) un afiche publicitario.", "A", "Una estadística oficial usa datos medidos."),
        ("La tabla es de 2015 y hoy existen datos de 2022. ¿Qué debes hacer antes de comparar? A) revisar el año de cada cifra, B) usar la más antigua, C) ignorar el año.", "A", "Los datos cambian con el tiempo."),
    ],
    ctx=("{F} Un concejal de ejemplo dice: «Delta no necesita nuevos servicios, su IDH es 0,78». Con la tabla, ¿a qué comuna responde que sí los necesita?", "A la comuna Cordillera, con IDH 0,62", "Allí el desarrollo es más bajo que el promedio."),
    sc=[("En Geografía: ¿qué puede ocultar un promedio regional?", "Desigualdades entre comunas", "Mezcla lugares distintos."),
        ("¿Qué debes revisar en una tabla de datos?", "Quién la produjo, el año y la unidad", "Permite usarla bien como evidencia."),
        ("Nombra una fuente estadística oficial posible.", "Por ejemplo: un censo o una encuesta nacional", "Producen datos medidos.")],
    op=("{F} Escribe un breve informe con tres frases: una que use el IDH regional, una que muestre la desigualdad interna con dos comunas y una que diga qué comuna necesita más apoyo y por qué. Anota una pregunta que te gustaría responder con más datos.",
        "El IDH regional de Delta es 0,78. Centro tiene 0,85 y Cordillera 0,62, así que hay una desigualdad interna. Cordillera necesita más apoyo porque tiene el menor IDH. Me gustaría saber la esperanza de vida y la escolaridad de cada comuna.",
        ["usa el IDH regional", "muestra desigualdad con dos comunas", "identifica la comuna prioritaria", "formula una pregunta"], ["tres frases y una pregunta"], ["usar solo el promedio", "no justificar la comuna prioritaria"], "Lee tu informe a una persona de tu casa y pídele que diga si cambiaría la comuna prioritaria."),
    reinforce="Busca una cifra en una noticia o documento de tu casa y anota su año, su unidad y quién la produjo.",
    extend="Calcula cuántas veces es mayor el ingreso de Centro que el de Costa y escribe qué significa.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = ("Fichas de ejemplo (regiones inventadas, datos inventados). "
      "Región Norte: desierto con yacimientos de cobre; de cada 100 dólares que exporta, 90 vienen del cobre; poca agricultura. "
      "Región Centro: fruta, vino, industria y servicios; exporta fruta por 800 millones de dólares, vino por 300, productos industriales por 600 y servicios por 300. "
      "Región Sur: bosques, ganadería, salmones y turismo; los salmones necesitan aguas frías y limpias.")
build(
    OA, 3, F3,
    use="Aprenderé a describir la diversidad productiva, el intercambio y el consumo de una región y a explicar sus ventajas comparativas. Sirve para entender por qué cada región se especializa en algo distinto.",
    prior=["Sé qué es desarrollo y IDH.", "Sé distinguir factores físicos y humanos.", "Sé calcular porcentajes y sumas de cifras grandes."],
    explain=[
        "Una economía regional tiene tres momentos. La producción es crear bienes, como fruta o cobre, y servicios, como transporte o turismo. El intercambio es vender y comprar esos bienes y servicios dentro de la región, con otras regiones y con otros países. El consumo es usar los bienes y servicios para satisfacer necesidades. Los tres se relacionan: lo que se produce se intercambia y se consume.",
        "La diversidad productiva es la variedad de actividades económicas de una región. Una región con muchas actividades es menos vulnerable: si una pierde mercado, las otras siguen. Una región que depende de un solo producto, como el cobre, corre más riesgo cuando su precio baja. Pero la especialización también puede traer beneficios si el producto es muy valioso.",
        "Una ventaja comparativa es una condición que permite a una región o país producir un bien a menor costo relativo, o con mejor calidad, que otros. Puede venir de la naturaleza (clima, minerales), del trabajo (conocimientos) o de la tecnología. Por ejemplo, una región con yacimientos de cobre tiene ventaja en minería, y una con aguas frías y limpias, en salmones. Gracias a las ventajas, las regiones se especializan y luego intercambian. Aprovechar una ventaja exige cuidar el recurso: el mar y los lagos donde se crían los salmones también necesitan protección.",
    ],
    vocab=[("producción", "creación de bienes y servicios"), ("intercambio", "compra y venta de bienes y servicios"), ("consumo", "uso de bienes y servicios para satisfacer necesidades"), ("diversidad productiva", "variedad de actividades económicas de una región"), ("ventaja comparativa", "condición que permite producir algo a menor costo relativo o con mejor calidad que otros")],
    worked=[
        ("Identificar la ventaja", "Una región de ejemplo tiene mucho sol, poca nubosidad y terrenos planos. ¿Qué actividad podría tener como ventaja comparativa?",
         ["Busco una actividad que use esas condiciones.", "El sol permite generar energía solar."], "Producir energía solar"),
        ("Medir la dependencia", "De cada 100 dólares que exporta una región, 80 vienen de un solo producto. ¿Es diversa su producción?",
         ["Gran parte depende de un producto.", "Eso indica poca diversidad."], "No; depende mucho de un solo producto"),
    ],
    mistakes=[
        ("Creer que especializarse siempre es malo.", "Si se usa una ventaja comparativa puede dar muchos beneficios; el riesgo es depender de un solo producto.", "Evalúa ventaja y riesgo a la vez."),
        ("Decir que el consumo es solo comprar cosas caras.", "El consumo es usar cualquier bien o servicio para satisfacer necesidades.", "Piensa en alimentos, transporte, salud o educación."),
    ],
    T=[
        ("En Geografía: ¿qué es la producción?", "La creación de bienes y servicios", "Es el primer momento de la actividad económica."),
        ("En Geografía: ¿qué es el consumo?", "El uso de bienes y servicios para satisfacer necesidades", "Es el momento final del ciclo."),
        ("{F} ¿Qué región tiene la mayor diversidad productiva? A) Norte, B) Centro, C) Sur.", "B", "Exporta cuatro tipos de producto."),
        ("{F} ¿Qué ventaja comparativa tiene la Región Norte?", "Los yacimientos de cobre que le da su desierto", "Tiene un recurso mineral de alto valor."),
        ("=", "{F} Si el Norte exporta 5.000 millones de dólares, ¿cuántos millones corresponden al cobre?", "5000*90/100", "Se calcula el 90 % del total."),
        ("=", "{F} ¿Cuántos millones de dólares exporta la Región Centro en total?", "800+300+600+300", "Se suman las cuatro exportaciones."),
        ("{F} Si el precio del cobre baja a la mitad, ¿qué región se afecta más? A) Norte, B) Centro, C) Sur.", "A", "El 90 % de sus exportaciones es cobre."),
        ("{F} ¿Qué condición natural explica una posible ventaja comparativa del Sur en salmones?", "Las aguas frías y limpias que necesitan los salmones", "La ventaja depende de las condiciones del lugar."),
        ("Una familia de la Región Centro come en la mesa el pan que compró en su región. ¿Qué momento de la actividad económica realiza al comerlo?", "Consumo", "Usa un bien para satisfacer una necesidad."),
        ("Explica con una frase por qué las regiones intercambian entre sí.", "Porque cada una tiene ventajas distintas y necesita lo que otras producen mejor", "La especialización genera intercambio."),
        ("{F} Propón una actividad que complemente la minería en el Norte para depender menos del cobre.", "Por ejemplo, turismo de observación de estrellas", "Usa el cielo despejado del desierto."),
        ("Evalúa la frase «Una región con muchas actividades es siempre más desarrollada». ¿Qué falla?", "Que la diversidad ayuda a reducir riesgos, pero el desarrollo depende también de salud, educación e ingresos", "Son dos conceptos distintos."),
        ("{F} ¿Qué porcentaje de la exportación del Norte NO es cobre?", "10 %", "100 menos 90 da lo que no es cobre."),
    ],
    ctx=("En el curso se discute si una región debe producir solo lo que mejor sabe hacer o crear también otras actividades. {F} Con la ficha, ¿qué riesgo tiene el Norte al depender del cobre?", "Que si baja el precio del cobre perdería gran parte de sus ingresos", "Casi todas sus exportaciones dependen de un producto."),
    sc=[("En Geografía: ¿qué es el intercambio?", "La compra y venta de bienes y servicios", "Ocurre dentro de la región y fuera de ella."),
        ("¿Qué es una ventaja comparativa?", "Una condición que permite producir algo a menor costo o con mejor calidad", "Puede venir de la naturaleza o del trabajo."),
        ("¿Qué riesgo tiene depender de un solo producto?", "Que si baja su precio se pierden muchos ingresos", "Falta de diversidad.")],
    op=("{F} Elige una región de la ficha y escribe: su ventaja comparativa, dos cifras o datos de su producción, un riesgo que enfrenta y una actividad nueva que podría desarrollar.",
        "Región Centro: su ventaja es su variedad de actividades con clima favorable para la fruta y el vino. Exporta 800 millones en fruta y 300 en vino. Riesgo: depender del clima para la agricultura. Podría desarrollar más servicios de tecnología.",
        ["nombra una ventaja comparativa", "usa datos de la ficha", "señala un riesgo", "propone una actividad"], ["cuatro partes breves"], ["inventar datos fuera de la ficha", "proponer algo sin relación con la región"], "Explícale tu región a una persona de tu casa y pídele que sugiera otra actividad."),
    reinforce="Anota tres bienes que se producen en tu región y tres que llegan desde otras.",
    extend="Escribe una razón por la que una región podría decidir diversificar aunque su producto principal sea muy rentable.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = ("Testimonios de ejemplo escritos para este ejercicio. "
      "Exportador de fruta: «Vendo mis productos a varios países; si aparecen barreras al comercio, pierdo mercados.» "
      "Temporera: «En verano hay trabajo y mi ingreso sube, pero el resto del año no tengo contrato.» "
      "Dirigente de una caleta: «Queremos empleo, pero cuidando el mar donde pescamos.» "
      "Funcionario del Estado: «Los tratados de libre comercio abren mercados, pero hay que proteger a quienes se ven afectados.» "
      "Datos de ejemplo: una región exporta 3.000 millones de dólares e importa 2.200 millones.")
build(
    OA, 4, F4,
    use="Aprenderé qué es la inserción de una región en los mercados internacionales y cómo la ven distintos actores. Sirve para evaluar los beneficios y costos de exportar.",
    prior=["Sé qué son producción, intercambio y ventaja comparativa.", "Sé contrastar perspectivas.", "Sé restar cifras grandes."],
    explain=[
        "Una región se inserta en los mercados internacionales cuando vende sus productos a otros países, es decir, exporta, y compra productos de otros países, es decir, importa. La diferencia entre lo que exporta y lo que importa se llama saldo comercial: es positivo si exporta más de lo que importa. Chile ha firmado tratados de libre comercio, que son acuerdos entre países para facilitar el intercambio al reducir barreras.",
        "Exportar trae oportunidades: nuevos clientes, más empleo y más ingresos. Pero también trae riesgos: los precios internacionales cambian y la región depende de la demanda de otros países. Un producto con valor agregado, es decir, elaborado y procesado, suele dar más ingresos que uno vendido sin procesar. Por eso se habla de agregar valor.",
        "Los efectos no son iguales para todos los actores. Los exportadores ganan mercados; los trabajadores de temporada pueden tener empleo solo parte del año; las comunidades locales se preocupan por el uso de recursos como el agua o el mar; el Estado busca equilibrar beneficios y protección. Para evaluar la inserción miro estas perspectivas y no solo las cifras de exportación.",
    ],
    vocab=[("exportar", "vender productos a otros países"), ("importar", "comprar productos de otros países"), ("saldo comercial", "exportaciones menos importaciones"), ("tratado de libre comercio", "acuerdo entre países para facilitar el intercambio"), ("valor agregado", "valor adicional que se obtiene al elaborar o procesar un producto")],
    worked=[
        ("Calcular el saldo", "Una región de ejemplo exporta 4.000 millones de dólares e importa 3.500 millones. ¿Cuál es el saldo comercial?",
         ["Resto las importaciones a las exportaciones.", "4.000 - 3.500 = 500."], "+500 millones de dólares"),
        ("Ver quién gana y quién arriesga", "{F} ¿Qué preocupa al dirigente de la caleta y qué al exportador?",
         ["El dirigente teme que se dañe el mar donde pesca.", "El exportador teme perder mercados por barreras."], "Cuidado del mar frente a pérdida de mercados"),
    ],
    mistakes=[
        ("Creer que exportar más beneficia automáticamente a toda la región.", "Los beneficios pueden repartirse de manera desigual.", "Pregunta qué actores ganan y cuáles arriesgan."),
        ("Confundir exportar con importar.", "Exportar es vender al exterior e importar es comprar del exterior.", "Piensa hacia dónde salen los productos."),
    ],
    T=[
        ("En Geografía: ¿qué es exportar?", "Vender productos a otros países", "Los productos salen del país."),
        ("En Geografía: ¿qué es un tratado de libre comercio?", "Un acuerdo entre países para facilitar el intercambio", "Reduce barreras al comercio."),
        ("{F} ¿Quién dice que quiere empleo, pero cuidando el mar?", "El dirigente de la caleta", "Se preocupa por su entorno."),
        ("=", "{F} ¿Cuál es el saldo comercial de la región de ejemplo, en millones de dólares?", "3000-2200", "Se restan las importaciones a las exportaciones."),
        ("{F} ¿Qué preocupa a la temporera? A) tener contrato todo el año, B) vender más fruta, C) firmar tratados.", "A", "Dice que fuera del verano no tiene contrato."),
        ("{F} ¿Qué beneficio de exportar menciona el exportador? A) llegar a varios países, B) pagar menos impuestos, C) usar menos agua.", "A", "Vende a varios países."),
        ("=", "Una región de ejemplo exporta 600 toneladas de fruta y 4 de cada 5 toneladas van a mercados lejanos. ¿Cuántas toneladas van a mercados lejanos?", "600*4/5", "Se calculan cuatro quintos de 600."),
        ("=", "Una temporera de ejemplo gana $450.000 al mes durante 4 meses de verano y nada el resto del año. ¿Cuánto gana en el año?", "450000*4", "Se multiplica el ingreso mensual por los meses de trabajo."),
        ("=", "Un producto se vende sin procesar a $100 la unidad, y elaborado, a $250. ¿Cuántos pesos de valor agregado gana por unidad?", "250-100", "El valor agregado es la diferencia de precios."),
        ("{F} Explica con una frase por qué no basta mirar solo cuánto se exporta.", "Porque los beneficios y costos son distintos para exportadores, trabajadores, comunidades y el Estado", "Hay perspectivas diversas."),
        ("{F} ¿Qué perspectiva tiene el funcionario del Estado frente a los tratados?", "Abren mercados, pero hay que proteger a quienes se ven afectados", "Busca equilibrar beneficios y protección."),
        ("Evalúa: «Si una región exporta mucho, ya está insertada de forma justa». ¿Qué falla?", "Que exportar mucho no asegura empleo estable ni cuidado del entorno", "La inserción tiene efectos desiguales."),
        ("{F} Propón una medida que ayude a la temporera sin impedir las exportaciones.", "Por ejemplo, capacitaciones para trabajar en otras actividades fuera de la temporada", "Reduce la dependencia de la temporada."),
    ],
    ctx=("Una radio de ejemplo informa que se firmó un nuevo tratado y que las exportaciones de fruta subirán. {F} Con los testimonios, ¿qué actor podría salir perjudicado si el trabajo sigue siendo solo de temporada?", "La temporera", "Su ingreso depende solo de los meses de cosecha."),
    sc=[("En Geografía: ¿qué es el saldo comercial?", "Las exportaciones menos las importaciones", "Si es positivo, se exporta más de lo que se importa."),
        ("¿Qué es el valor agregado?", "El valor adicional que se obtiene al elaborar o procesar un producto", "Un producto elaborado vale más."),
        ("Nombra un riesgo de depender de la exportación.", "Por ejemplo: que cambien los precios internacionales", "La demanda externa no se controla.")],
    op=("{F} Elige dos testimonios y compáralos: qué beneficio o riesgo ve cada uno, una cifra del saldo comercial y una idea que ayude a ambos. Termina con una frase sobre si la inserción internacional es solo buena o solo mala.",
        "Comparo al exportador y a la temporera. El exportador gana mercados y arriesga barreras; la temporera gana ingreso en verano, pero no tiene contrato el resto del año. El saldo de 800 millones muestra que se exporta más de lo que se importa. Una idea: ofrecer contratos más estables. La inserción internacional trae beneficios y riesgos.",
        ["compara dos actores", "usa el saldo comercial", "propone una idea", "concluye con matiz"], ["cuatro partes breves"], ["decir que es solo buena o solo mala", "olvidar el dato"], "Pide a una persona de tu casa que te diga qué actor te faltó considerar."),
    reinforce="Mira la etiqueta de un producto de tu casa y anota si es nacional o importado.",
    extend="Escribe una idea para agregar valor a un producto de tu región.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = ("Caso de ejemplo, Caleta Marina (inventada, datos inventados). La pesca da empleo a 200 familias. En 5 años la extracción aumentó 30 %, pero la captura por barco bajó de 100 cajas a 70 cajas por salida. "
      "Propuesta: una veda de 2 meses al año (prohibición temporal de pescar) con un apoyo económico a las familias mientras dura. "
      "Datos de la propuesta: el apoyo cuesta $200.000 por familia al mes.")
build(
    OA, 5, F5,
    use="Aprenderé qué es el desarrollo sustentable y cómo argumentar con evidencia sobre una decisión que mezcla economía, sociedad y medio ambiente. Sirve para evaluar proyectos en una región.",
    prior=["Sé qué es el desarrollo y cómo se mide.", "Sé qué es una ventaja comparativa.", "Sé armar un argumento con afirmación, evidencia y explicación."],
    explain=[
        "El desarrollo sustentable busca satisfacer las necesidades de las personas de hoy sin dañar la posibilidad de que las generaciones futuras satisfagan las suyas. Tiene tres dimensiones que deben equilibrarse: la económica (empleo e ingresos), la social (calidad de vida y justicia) y la ambiental (cuidado de los recursos y los ecosistemas).",
        "Un recurso renovable puede recuperarse con el tiempo si se usa con cuidado, como los peces; uno no renovable se agota, como el petróleo. Si se extrae un recurso renovable más rápido de lo que se recupera, se sobreexplota y puede agotarse. Medidas como las vedas, que son prohibiciones temporales de extraer, ayudan a recuperar el recurso.",
        "Para argumentar sobre una decisión miro las tres dimensiones y uso evidencia. Si la captura baja mientras la extracción sube, hay una señal de sobreexplotación. Una buena propuesta busca resultados en las tres dimensiones, aunque a veces hay costos a corto plazo. Reconozco también los límites de mis datos y las objeciones de quienes pierden ingresos.",
    ],
    vocab=[("desarrollo sustentable", "desarrollo que satisface necesidades presentes sin comprometer las de las generaciones futuras"), ("recurso renovable", "recurso que puede recuperarse si se usa con cuidado"), ("recurso no renovable", "recurso que se agota con su uso"), ("sobreexplotación", "extraer un recurso más rápido de lo que se recupera"), ("veda", "prohibición temporal de extraer un recurso")],
    worked=[
        ("Detectar sobreexplotación", "Una caleta de ejemplo extrae cada año más peces, pero captura menos por barco. ¿Qué indica?",
         ["Se extrae más.", "Se captura menos por barco.", "Eso sugiere que el recurso se está agotando."], "Una señal de sobreexplotación"),
        ("Ubicar la dimensión", "Un apoyo económico a las familias durante una veda, ¿qué dimensión protege?",
         ["Ayuda a mantener los ingresos de las familias.", "Eso es la dimensión social y económica."], "La social y la económica"),
    ],
    mistakes=[
        ("Creer que cuidar el ambiente y tener empleo siempre se oponen.", "Una veda puede proteger el recurso y mantener el empleo futuro.", "Busca un equilibrio entre las tres dimensiones."),
        ("Pensar que un recurso renovable no se puede agotar.", "Si se extrae más rápido de lo que se recupera, sí se agota.", "Compara la extracción con la recuperación."),
    ],
    T=[
        ("En Geografía: ¿qué es el desarrollo sustentable?", "El que satisface las necesidades de hoy sin comprometer las de las generaciones futuras", "Equilibra economía, sociedad y ambiente."),
        ("En Geografía: ¿qué es una veda?", "Una prohibición temporal de extraer un recurso", "Permite que el recurso se recupere."),
        ("{F} ¿Cuántas familias dependen de la pesca en Caleta Marina?", "200", "Lo indica el caso."),
        ("=", "{F} ¿Cuántas cajas menos por salida se capturan ahora que hace 5 años?", "100-70", "Se resta la captura actual a la antigua."),
        ("=", "{F} ¿Cuánto cuesta el apoyo a las 200 familias durante 1 mes?", "200*200000", "Se multiplica el apoyo por familia por las 200 familias."),
        ("=", "{F} ¿Cuánto cuesta el apoyo a las 200 familias durante los 2 meses de veda?", "200*200000*2", "Se multiplica el costo mensual por dos meses."),
        ("{F} ¿Qué dato muestra una señal de sobreexplotación? A) la extracción subió 30 % y la captura por barco bajó, B) hay 200 familias, C) la veda dura 2 meses.", "A", "Se extrae más y se captura menos."),
        ("{F} ¿Qué dimensión del desarrollo sustentable protege la veda? A) la ambiental, B) ninguna, C) solo la económica.", "A", "Ayuda a recuperar el recurso."),
        ("{F} Un pescador objeta: «Con la veda perdemos dos meses de ingresos». ¿Qué dato del caso responde parcialmente?", "El apoyo económico de $200.000 por familia al mes", "Compensa parte del ingreso."),
        ("¿Cuál es un recurso no renovable? A) los peces, B) el petróleo, C) un bosque bien manejado.", "B", "Se agota con su uso."),
        ("{F} Explica con una frase por qué la veda puede asegurar empleo a largo plazo.", "Porque permite que el recurso se recupere y siga habiendo pesca en el futuro", "Cuida la base del trabajo."),
        ("Evalúa la frase «Sustentable es lo mismo que no usar ningún recurso». ¿Qué falla?", "Que se pueden usar recursos si se hace de manera que no se agoten ni dañen a las generaciones futuras", "Sustentable es uso responsable."),
        ("{F} Escribe un límite de la evidencia del caso.", "Que no sabemos cuánto se recuperarán los peces ni si dos meses bastan", "Los datos no lo muestran."),
    ],
    ctx=("En una asamblea, un vecino de la caleta dice: «Mientras haya pescado, no hay problema». {F} Con el caso, ¿qué dato le muestras?", "Que la captura por barco bajó de 100 a 70 cajas aunque se extrae más", "Es evidencia de sobreexplotación."),
    sc=[("En Geografía: ¿qué es un recurso renovable?", "Un recurso que puede recuperarse si se usa con cuidado", "Como los peces o los bosques."),
        ("¿Cuáles son las tres dimensiones del desarrollo sustentable?", "Económica, social y ambiental", "Deben equilibrarse entre sí."),
        ("¿Qué es la sobreexplotación?", "Extraer un recurso más rápido de lo que se recupera", "Puede agotar el recurso.")],
    op=("{F} Escribe un argumento de cuatro partes sobre la propuesta de veda: tu afirmación, dos datos del caso, una explicación que use las tres dimensiones y una objeción con su respuesta.",
        "Afirmación: la veda es una buena propuesta. Datos: la captura bajó de 100 a 70 cajas; el apoyo es de $200.000 por familia al mes. Explicación: protege el recurso, mantiene un ingreso y cuida el empleo futuro. Objeción: perder dos meses de pesca; respuesta: el apoyo compensa en parte.",
        ["afirmación clara", "dos datos del caso", "explicación con tres dimensiones", "objeción respondida"], ["cuatro partes completas"], ["no usar datos", "olvidar la objeción"], "Pide a una persona de tu casa que ponga otra objeción y respóndela."),
    reinforce="Anota un recurso renovable y uno no renovable que uses en tu casa.",
    extend="Escribe otra medida, además de la veda, que cuide el recurso pesquero.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 6
F6 = ("Proyecto de ejemplo para el Valle Verde (inventado, datos inventados): una planta que procesa fruta. "
      "Económico: crea 300 empleos con un sueldo de $600.000 al mes cada uno y agrega valor a la fruta. "
      "Social: ofrece capacitación a 100 jóvenes; solo 2 de las 3 comunas del valle están cerca de la planta. "
      "Ambiental: usa 20 % más agua que la agricultura actual y genera residuos que deben tratarse.")
build(
    OA, 6, F6,
    use="Aprenderé a evaluar un proyecto regional con las tres dimensiones del desarrollo sustentable y a proyectar sus efectos y límites. Sirve para tomar decisiones informadas sobre el futuro de una región.",
    prior=["Sé qué es el desarrollo sustentable.", "Sé qué son el IDH y la desigualdad interna.", "Sé calcular costos y porcentajes."],
    explain=[
        "Evaluar un proyecto regional es juzgar sus efectos en las tres dimensiones. En lo económico miro empleos, ingresos y valor agregado. En lo social, a quiénes beneficia, si reduce o aumenta desigualdades y si mejora la educación o la salud. En lo ambiental, el uso de agua y energía, los residuos y el efecto sobre ecosistemas.",
        "Un buen análisis considera los tiempos. Hay beneficios inmediatos, como el empleo, y efectos de largo plazo, como el desgaste del agua. También considero a quienes quedan fuera: si un proyecto beneficia solo a una parte del territorio, puede aumentar la desigualdad interna. Para ello comparo el promedio regional con la situación de cada comuna.",
        "Finalmente proyecto escenarios: qué pasa si el proyecto funciona bien y qué pasa si falla. Propongo medidas para reducir los costos, como tratar residuos o usar agua con más eficiencia. Y declaro los límites de mi juicio: los datos de ejemplo son parciales y habría que consultar a la comunidad y a especialistas antes de decidir.",
    ],
    vocab=[("escenario", "situación posible que se imagina a futuro"), ("eficiencia", "lograr un resultado usando menos recursos"), ("mitigación", "medida para reducir un daño"), ("corto plazo / largo plazo", "efectos inmediatos / efectos que se ven después de años"), ("consulta a la comunidad", "proceso en que se pregunta a las personas del territorio su opinión")],
    worked=[
        ("Calcular un beneficio", "Un proyecto de ejemplo crea 50 empleos con sueldo de $500.000 al mes. ¿Cuánto suman los sueldos mensuales?",
         ["Multiplico empleos por sueldo.", "50 × 500.000 = 25.000.000."], "$25.000.000 al mes"),
        ("Ubicar un costo ambiental", "Un proyecto usa más agua en una zona seca. ¿Qué dimensión afecta y qué medida podría reducir el daño?",
         ["Afecta la dimensión ambiental.", "Una medida: reutilizar el agua o usar sistemas más eficientes."], "La ambiental; reutilizar agua"),
    ],
    mistakes=[
        ("Evaluar un proyecto mirando solo los empleos.", "Falta revisar los efectos sociales y ambientales.", "Revisa las tres dimensiones."),
        ("Creer que si el promedio mejora, todas las comunas mejoran.", "Un proyecto puede beneficiar a unas comunas y dejar fuera a otras.", "Compara comunas, no solo el promedio."),
    ],
    T=[
        ("En Geografía: ¿qué es un escenario?", "Una situación posible que se imagina a futuro", "Sirve para proyectar efectos."),
        ("En Geografía: ¿qué es la mitigación?", "Una medida para reducir un daño", "Disminuye los efectos negativos."),
        ("{F} ¿Cuántos empleos crea la planta?", "300", "Lo indica la ficha."),
        ("=", "{F} ¿Cuánto suman los sueldos mensuales de los 300 empleos?", "300*600000", "Se multiplica el número de empleos por el sueldo."),
        ("=", "{F} Si la planta capacita a 100 jóvenes por año, ¿cuántos jóvenes habrá capacitado en 4 años?", "100*4", "Se multiplica por los años."),
        ("{F} ¿Qué dimensión afecta el uso de 20 % más agua? A) la ambiental, B) la económica, C) la social.", "A", "El agua es un recurso natural."),
        ("{F} ¿Qué límite social tiene el proyecto? A) solo 2 de las 3 comunas están cerca de la planta, B) crea 300 empleos, C) agrega valor a la fruta.", "A", "Una comuna queda fuera de los beneficios directos."),
        ("{F} Si una comuna tiene IDH 0,60 y es la que queda lejos de la planta, ¿puede aumentar la desigualdad interna? Explica.", "Sí, porque las otras comunas se benefician más y la lejana queda relativamente atrás", "Los beneficios no llegan a todas."),
        ("{F} Propón una medida de mitigación para los residuos de la planta.", "Tratar los residuos antes de verterlos o reutilizarlos como abono", "Reduce el daño ambiental."),
        ("{F} ¿Qué beneficio de corto plazo y qué riesgo de largo plazo ves en el proyecto?", "Corto plazo, el empleo; largo plazo, el desgaste del agua", "Uno es inmediato y el otro se acumula."),
        ("Explica con una frase por qué conviene consultar a la comunidad antes de decidir.", "Porque las personas del territorio conocen los efectos y pueden aportar información y preocupaciones", "La decisión las afecta."),
        ("Evalúa: «El proyecto es sustentable porque crea empleo». ¿Qué falta? A) revisar los efectos sociales y ambientales, B) nada, C) más sueldos.", "A", "Hay que mirar las tres dimensiones."),
        ("{F} Escribe un escenario optimista y uno pesimista para el Valle Verde.", "Optimista: la planta da empleo y trata sus residuos; pesimista: falta agua y una comuna queda sin beneficios", "Cada escenario muestra una posible evolución."),
    ],
    ctx=("El concejo del Valle Verde debe votar el proyecto. Un vecino dice: «Con 300 empleos se arregla todo». {F} Con la ficha, ¿qué dos asuntos le recuerdas que faltan por evaluar?", "El uso de agua (20 % más) y la comuna que queda lejos de la planta", "Son un límite ambiental y uno social."),
    sc=[("En Geografía: ¿qué es la eficiencia?", "Lograr un resultado usando menos recursos", "Reduce el desperdicio de recursos."),
        ("Nombra una dimensión que revisas al evaluar un proyecto.", "Por ejemplo: económica, social o ambiental", "Son las tres del desarrollo sustentable."),
        ("¿Por qué conviene considerar efectos de largo plazo?", "Porque algunos daños aparecen después de años", "El agua puede agotarse con el tiempo.")],
    op=("{F} Evalúa el proyecto en las tres dimensiones con un dato por cada una, propone una medida de mitigación y escribe una recomendación final (aprobar, aprobar con condiciones o rechazar) con una razón. Cierra con una pregunta que te falte responder.",
        "Económico: 300 empleos. Social: capacitación a 100 jóvenes, pero una comuna queda lejos. Ambiental: 20 % más de agua. Mitigación: reutilizar agua y tratar residuos. Recomiendo aprobar con condiciones, porque da empleo pero necesita cuidar el agua. Me falta saber cuánta agua tiene el valle.",
        ["un dato por dimensión", "una medida de mitigación", "recomendación justificada", "una pregunta pendiente"], ["evaluación completa y breve"], ["mirar una sola dimensión", "recomendar sin razón"], "Compara tu recomendación con la de una persona de tu casa y escribe en qué se parecen."),
    reinforce="Anota un proyecto que haya en tu comuna y una cosa buena y una dudosa que tenga.",
    extend="Escribe cómo cambiaría tu recomendación si el valle tuviera poca agua.",
    materials=MAT,
)
