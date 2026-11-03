"""Material del estudiante de 8.º básico, Historia, Geografía y Ciencias Sociales: OA 09 (barroco y cultura colonial)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 09"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (resumen). Barroco: estilo artístico y cultural que se desarrolla en Europa y América durante el siglo XVII y buena parte del XVIII. "
     "Rasgos: ornamentación abundante, movimiento, contrastes fuertes de luz y sombra (claroscuro), dramatismo y búsqueda de emocionar. "
     "Contexto: la Iglesia católica respondió a la Reforma con el Concilio de Trento (1545-1563) y usó el arte para acercar a los fieles a la fe. "
     "Expresiones coloniales: arquitectura (iglesias con fachadas muy decoradas, como la de la Compañía de Jesús en Cusco, del siglo XVII), pintura (escuela cuzqueña, siglos XVII y XVIII), música (compositores como el jesuita Domenico Zipoli), teatro (autos sacramentales y obras de autores como Sor Juana Inés de la Cruz) y ceremonias (procesiones y fiestas).")
build(
    OA, 1, F,
    use="Aprenderé a situar el barroco en el tiempo y el espacio, a reconocer sus rasgos y a nombrar las expresiones culturales de la sociedad colonial en que se manifestó.",
    prior=["Conozco la Reforma y la Contrarreforma.", "Conozco la ciudad colonial.", "Sé ubicar siglos y calcular diferencias de años."],
    explain=[
        "El barroco es un estilo artístico y cultural que se desarrolló en Europa y América durante el siglo XVII y buena parte del siglo XVIII. Se caracteriza por la ornamentación abundante, el movimiento, los contrastes fuertes de luz y sombra, el dramatismo y la búsqueda de emocionar. Se usaba para impresionar y para transmitir ideas religiosas y de poder.",
        "Su contexto es la respuesta de la Iglesia católica a la Reforma. En el Concilio de Trento, entre 1545 y 1563, la Iglesia defendió sus enseñanzas y promovió el uso de las artes para acercar a los fieles a la fe. En América, esas ideas llegaron con misioneros, artistas y encargos de iglesias y de elites coloniales.",
        "El OA pide caracterizar el barroco a través de distintas expresiones de la sociedad colonial: arte, arquitectura, música, teatro y ceremonias. En la música, compositores como Zipoli escribieron obras con contrastes de ritmo y de volumen para emocionar en las ceremonias religiosas; en el teatro, los autos sacramentales y las obras de Sor Juana trataban temas de fe con mucho dramatismo. Un error es definir el barroco solo por el exceso decorativo, sin ver quiénes lo hicieron y para qué. En esta clase situamos el tema y reconocemos sus rasgos.",
    ],
    vocab=[("barroco", "estilo de los siglos XVII y XVIII con ornamentación abundante, movimiento y dramatismo"), ("claroscuro", "contraste fuerte entre luz y sombra en una pintura"), ("ornamentación", "conjunto de adornos de una obra"), ("Concilio de Trento", "reunión de la Iglesia católica entre 1545 y 1563 como respuesta a la Reforma"), ("auto sacramental", "obra de teatro religiosa breve")],
    worked=[
        ("Calcular una duración", "Según la ficha, ¿cuántos años duró el Concilio de Trento?", ["Busco los años: 1545 y 1563.", "Resto: 1563 − 1545 = 18."], "18 años"),
        ("Reconocer un rasgo", "Una pintura muestra una escena oscura con un haz de luz muy fuerte sobre una figura. ¿Qué rasgo barroco es?", ["Hay contraste fuerte de luz y sombra.", "Eso es claroscuro."], "Claroscuro"),
    ],
    mistakes=[("Pensar que el barroco es solo «muchos adornos».", "Se ignora su función de emocionar y transmitir ideas religiosas y de poder.", "Relaciona los rasgos con su propósito."),
              ("Creer que el barroco existió solo en Europa.", "Se ignora su desarrollo en América.", "Nombra ejemplos coloniales.")],
    T=[
        ("{F} ¿En qué siglo se desarrolla principalmente el barroco?", "En el siglo XVII y buena parte del XVIII", "La ficha lo indica."),
        ("{F} ¿Qué reunión de la Iglesia se menciona entre 1545 y 1563?", "El Concilio de Trento", "La ficha lo nombra."),
        ("{F} ¿Qué es el claroscuro?", "Un contraste fuerte entre luz y sombra", "Se define en la ficha."),
        ("{F} Una obra de teatro religiosa presenta un tema de fe con mucho dramatismo para emocionar al público. ¿Qué rasgos barrocos muestra?", "El dramatismo y la búsqueda de emocionar", "Son dos rasgos de la ficha, también presentes en el teatro y la música barrocos."),
        ("{F} ¿Qué compositor jesuita se menciona en la ficha?", "Domenico Zipoli", "La ficha lo nombra."),
        ("{F} ¿A qué siglo pertenecen la escuela cuzqueña y la fachada de la Compañía en Cusco, según la ficha?", "A los siglos XVII y XVIII la escuela, y al siglo XVII la fachada", "La ficha da esas épocas."),
        ("{F} Clasifica cada obra con su expresión: a) iglesia con fachada muy decorada, b) procesión por las calles, c) obra de Sor Juana. Opciones: arquitectura; ceremonia; teatro o literatura.", "a) arquitectura; b) ceremonia; c) teatro o literatura", "Cada ejemplo corresponde a una expresión distinta."),
        ("{F} ¿Por qué la Iglesia usó el arte después de la Reforma? A) Para acercar a los fieles a la fe y emocionar B) Para prohibir que los fieles vieran imágenes religiosas", "A) Para acercar a los fieles a la fe y emocionar", "Esa es la intención según el contexto."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 25 años y parte en 1545. ¿A cuántos cm queda 1700?", "(1700-1545)//25", "Se divide la diferencia de años por la escala.", " cm"),
        ("{F} Un compañero dice: «El barroco solo se hizo en Europa». ¿Qué dato de la ficha lo contradice?", "La ficha menciona obras coloniales como la escuela cuzqueña y la Compañía en Cusco", "También se desarrolló en América."),
        ("{F} Una pintura de 1650 muestra una escena dramática con luz y sombra muy marcadas. ¿Qué rasgo barroco la identifica?", "El claroscuro y el dramatismo", "Son rasgos de la ficha."),
        ("{F} ¿Qué afirmación es correcta? A) El barroco buscaba emocionar y transmitir ideas religiosas y de poder B) El barroco buscaba la simplicidad y el equilibrio de las formas", "A) El barroco buscaba emocionar y transmitir ideas religiosas y de poder", "La ficha lo indica."),
        ("{F} ¿Qué pregunta problema plantea esta clase?", "Cómo se expresó el barroco en la sociedad colonial y quiénes lo hicieron", "Es el problema del OA."),
    ],
    ctx=("Un guía de museo dice: «Esta fachada es barroca solo porque tiene muchos adornos». ¿Qué agregarías con la ficha? {F}", "Que el barroco también busca emocionar, usa movimiento y contrastes, y se vincula a la respuesta de la Iglesia a la Reforma", "Relaciona rasgos con su propósito."),
    sc=[("¿Qué es el barroco?", "Un estilo de los siglos XVII y XVIII con ornamentación abundante, movimiento y dramatismo", "Se definió en el vocabulario."),
        ("¿Qué es un auto sacramental?", "Una obra de teatro religiosa breve", "Se definió en el vocabulario."),
        ("=", "El Concilio de Trento comenzó en 1545 y terminó en 1563. ¿Cuántos años duró?", "1563-1545", "Se resta el año de inicio al de término.", " años")],
    op=("Haz una tabla con cinco columnas: arquitectura, pintura, música, teatro y ceremonias. En cada columna escribe un ejemplo de la ficha y un rasgo barroco que podría mostrar. Debajo escribe una frase que explique por qué el barroco no es solo decoración. {F}",
        "Arquitectura: fachada de la Compañía, ornamentación. Pintura: escuela cuzqueña, colores y dramatismo. Música: Zipoli, emoción. Teatro: autos sacramentales, dramatismo. Ceremonias: procesiones, movimiento. Frase: busca emocionar y transmitir ideas.",
        ["llena las cinco columnas", "relaciona ejemplo y rasgo", "explica el propósito"], ["tabla", "frase"], ["definir solo por decoración", "no usar ejemplos de la ficha"],
        "Pide que explique qué expresión le pareció más fácil de reconocer."),
    reinforce="Nombra los cinco tipos de expresión barroca del OA y un ejemplo para cada uno.",
    extend="Escribe una pregunta que un historiador haría para saber quiénes construyeron una iglesia barroca.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, descripción de una fachada de iglesia de una ciudad andina de ejemplo, siglo XVII: piedra tallada con columnas retorcidas, flores, frutos y animales locales, y figuras de santos en nichos. "
     "Fuente B, relato de un viajero de ejemplo sobre una procesión, 1680: «Salió la imagen en andas con velas y flores, seguida de músicos, danzantes y cofradías de artesanos con sus estandartes. La plaza se llenó de gente, desde los vecinos principales hasta los indígenas de los pueblos cercanos.» "
     "Fuente C, pintura de ejemplo de la escuela cuzqueña, siglo XVIII: una Virgen con manto muy decorado en oro, rodeada de ángeles con ropa de la época colonial y flores locales.")
build(
    OA, 2, F,
    use="Aprenderé a analizar una fachada, una procesión y una pintura como fuentes del barroco colonial, a contextualizarlas y a ver sus límites.",
    prior=["Sé contextualizar una fuente.", "Conozco los rasgos del barroco.", "Sé distinguir descripción e interpretación."],
    explain=[
        "Las obras barrocas son fuentes materiales (una fachada, una pintura) y escritas (un relato de una procesión). Para analizarlas se contextualizan: ¿quién las hizo, en qué ciudad, para qué y para quién? Una fachada de iglesia se hizo para impresionar a los fieles y mostrar el poder de la Iglesia. Una pintura se encargaba para un templo o una casa.",
        "En la Fuente A, la fachada incluye flores, frutos y animales locales junto a columnas y santos europeos. Esto sugiere una mezcla de tradiciones, probablemente por el trabajo de artesanos locales. En la Fuente C, la Virgen se pinta con ropa colonial y adornos de oro, y la pintura combina elementos europeos y locales. La Fuente B muestra que las ceremonias reunían a muchos grupos sociales en la plaza.",
        "Hay límites. Un viajero puede describir con admiración o prejuicio. Una fachada no dice quién la talló ni qué pensaban esos artesanos. Una pintura no explica por sí sola quién la pagó ni quién la miraba. Para interpretar con cuidado hay que combinar fuentes y reconocer lo que no sabemos.",
    ],
    vocab=[("fuente material", "objeto o edificio que es huella del pasado"), ("fachada", "parte exterior principal de un edificio"), ("procesión", "desfile religioso por las calles"), ("cofradía", "asociación de personas con una devoción o un oficio"), ("andas", "plataforma para llevar una imagen en procesión")],
    worked=[
        ("Identificar una mezcla", "¿Qué elementos de la Fuente A son europeos y cuáles locales?", ["Columnas y santos son de tradición europea.", "Flores, frutos y animales locales son de América."], "Europeos: columnas y santos; locales: flores, frutos y animales"),
        ("Reconocer un límite", "¿Qué no dice la Fuente A sobre quién talló la piedra?", ["La descripción menciona qué se ve.", "No nombra a los artesanos."], "No dice quién la talló"),
    ],
    mistakes=[("Afirmar quién fue el artista de una obra sin tener datos.", "Se supone en vez de contextualizar.", "Escribe «no sabemos quién la hizo» y busca otra fuente."),
              ("Creer que un relato de viajero es neutral.", "El viajero describe con su mirada y prejuicios.", "Pregunta qué sentía y qué quería mostrar.")],
    T=[
        ("{F} ¿Qué elementos locales aparecen en la fachada de la Fuente A?", "Flores, frutos y animales locales", "La descripción los nombra."),
        ("{F} ¿Qué llevaban en la procesión de la Fuente B?", "La imagen en andas con velas y flores", "El relato lo dice."),
        ("{F} ¿Quiénes se reunieron en la plaza según la Fuente B?", "Desde los vecinos principales hasta los indígenas de los pueblos cercanos", "El relato lo indica."),
        ("=", "{F} La procesión es de 1680. ¿Cuántos años pasaron hasta 1700?", "1700-1680", "Se resta el año del relato a 1700.", " años"),
        ("{F} ¿Qué detalle de la pintura (Fuente C) muestra una mezcla de tradiciones?", "Ángeles con ropa de la época colonial y flores locales junto a la Virgen europea", "La pintura combina elementos."),
        ("{F} Clasifica cada fuente como material o escrita: a) A, b) B, c) C.", "a) material; b) escrita; c) material", "La fachada y la pintura son objetos; el relato es un texto."),
        ("{F} ¿Qué rasgo barroco muestra el manto decorado en oro de la Virgen? A) Ornamentación abundante B) Sencillez", "A) Ornamentación abundante", "Los adornos abundantes son un rasgo barroco."),
        ("{F} ¿Por qué se hacían las fachadas tan decoradas? A) Para impresionar a los fieles y mostrar el poder de la Iglesia B) Para ahorrar piedra y trabajo", "A) Para impresionar a los fieles y mostrar el poder de la Iglesia", "Esa era su función."),
        ("{F} Un compañero dice: «La Fuente A prueba que los artesanos eran pagados con justicia». ¿Qué falla?", "La descripción no dice nada sobre pagos ni condiciones de trabajo", "La fuente solo describe la fachada."),
        ("{F} ¿Qué límite tiene la Fuente B? A) Es la visión de un viajero B) Fue escrita por un artesano", "A) Es la visión de un viajero", "Puede describir con su propia mirada."),
        ("{F} ¿Qué muestra la Fuente B sobre las ceremonias?", "Que reunían a distintos grupos sociales en la plaza", "Menciona vecinos, músicos, cofradías e indígenas."),
        ("{F} ¿Qué conclusión es proporcional al mirar las tres fuentes? A) El barroco colonial mezcló elementos europeos y locales y reunía a distintos grupos B) El barroco colonial copió exactamente a Europa", "A) El barroco colonial mezcló elementos europeos y locales y reunía a distintos grupos", "Las fuentes A, B y C lo muestran."),
        ("{F} ¿Qué otra fuente ayudaría a saber quién talló la fachada? A) Contratos o cuentas de la construcción B) Otra descripción de la misma fachada hecha por un viajero", "A) Contratos o cuentas de la construcción", "Mostrarían quién trabajó y cuánto se pagó."),
    ],
    ctx=("Un museo quiere explicar la Fuente C a visitantes. ¿Qué dos elementos señalaría para mostrar una mezcla de tradiciones? {F}", "El manto decorado en oro de tradición europea y las flores locales o la ropa colonial de los ángeles", "La obra combina elementos de origen europeo y local."),
    sc=[("¿Qué es una fuente material?", "Un objeto o edificio que es huella del pasado", "Se definió en el vocabulario."),
        ("¿Qué es una cofradía?", "Una asociación de personas con una devoción o un oficio", "Se definió en el vocabulario."),
        ("¿Qué fuente de la ficha es un relato escrito? A) La B B) La A", "A) La B", "Es el relato del viajero.")],
    op=("Elige una de las tres fuentes y haz una tabla con cuatro filas: qué fuente es, qué muestra, qué rasgo barroco aparece y qué no sabemos. Después escribe una frase de descripción y otra de interpretación que no exagere. {F}",
        "Fuente A: fachada; muestra piedra tallada con flores y santos; rasgo: ornamentación; no sabemos quién la talló. Descripción: tiene flores y santos. Interpretación: pudo haber artesanos locales.",
        ["completa las cuatro filas", "separa descripción e interpretación", "reconoce lo que no sabemos"], ["tabla", "dos frases"], ["afirmar quién fue el artista", "no incluir lo que se desconoce"],
        "Pide que explique qué otra fuente usaría para completar su análisis."),
    reinforce="Explica a otra persona cómo reconoces una mezcla de elementos europeos y locales en una obra.",
    extend="Escribe una pregunta que le harías a un artesano que talló una fachada barroca.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (cambios, continuidades y territorios, simplificados). Cambios respecto del arte del siglo XVI europeo y colonial: más ornamentación, más movimiento, más dramatismo, y mayor mezcla de motivos locales en la decoración. "
     "Continuidades: la religión católica sigue siendo el tema principal de muchas obras; las iglesias siguen siendo el espacio central de la vida pública; el encargo de obras sigue dependiendo de la Iglesia y de las elites. "
     "Territorios: en los Andes, ciudades como Cusco, Potosí y Lima tuvieron talleres y templos barrocos; en México, el barroco se desarrolló en ciudades como México y Puebla; en Chile se construyeron iglesias y conventos con elementos barrocos, de menor escala por los terremotos y los recursos disponibles.")
build(
    OA, 3, F,
    use="Aprenderé a describir qué cambió y qué continuó con el barroco en América, y a ubicar en el territorio los centros donde se desarrolló.",
    prior=["Conozco los rasgos del barroco.", "Conozco la ciudad colonial.", "Sé distinguir cambio y continuidad."],
    explain=[
        "El barroco trajo cambios respecto del arte anterior: más ornamentación, más movimiento y más dramatismo. En América, además, se sumó una mayor mezcla de motivos locales, como flores, frutos y animales de la zona. Esta mezcla se explica en gran parte por la presencia de artesanos indígenas y mestizos en los talleres, que incorporaron su propia mirada.",
        "También hubo continuidades. La religión católica seguía siendo el tema principal de muchas obras. Las iglesias seguían siendo el espacio central de la vida pública. Las obras se encargaban a la Iglesia y a las elites, que pagaban. El barroco no significó una ruptura total con el pasado, sino una nueva manera de expresar ideas conocidas.",
        "El territorio importa: el barroco se desarrolló sobre todo en ciudades ricas y con talleres, como Cusco, Potosí, Lima, México y Puebla. En Chile hubo iglesias y conventos con elementos barrocos, pero de menor escala porque los terremotos y los recursos limitaban las construcciones. No todo el territorio tuvo el mismo desarrollo.",
    ],
    vocab=[("motivo", "elemento que se repite en una decoración, como una flor o un animal"), ("taller", "lugar donde artesanos o artistas hacen obras en grupo"), ("mestizo", "persona de ascendencia indígena y europea"), ("convento", "edificio donde viven religiosos o religiosas"), ("escala", "tamaño de una obra respecto de otras")],
    worked=[
        ("Clasificar cambio y continuidad", "Una iglesia de 1700 tiene flores locales en su fachada, pero sigue siendo el centro de la vida de la ciudad. ¿Qué es cambio y qué continuidad?", ["Las flores locales en la fachada son un cambio.", "Ser el centro de la ciudad es continuidad."], "Cambio: motivos locales; continuidad: la iglesia como centro"),
        ("Explicar por qué los motivos locales", "¿Por qué aparecen motivos locales en el arte colonial?", ["Había artesanos indígenas y mestizos en los talleres.", "Incorporaron su propia mirada."], "Porque artesanos locales trabajaban en los talleres"),
    ],
    mistakes=[("Pensar que el barroco colonial copió exactamente al europeo.", "Se ignora la mezcla de motivos locales.", "Nombra motivos locales y quiénes los hicieron."),
              ("Creer que todo el territorio colonial tuvo el mismo desarrollo barroco.", "Se ignoran las diferencias entre ciudades.", "Compara Cusco, México y Chile.")],
    T=[
        ("{F} ¿Qué ciudades andinas con barroco menciona la ficha?", "Cusco, Potosí y Lima", "La ficha las lista."),
        ("{F} ¿Qué ciudades de México menciona la ficha?", "México y Puebla", "La ficha las lista."),
        ("{F} ¿Qué limitaba las construcciones en Chile?", "Los terremotos y los recursos disponibles", "La ficha lo indica."),
        ("{F} Clasifica como cambio o continuidad: a) más ornamentación, b) la religión católica como tema principal, c) mayor mezcla de motivos locales.", "a) cambio; b) continuidad; c) cambio", "Solo el tema religioso se mantiene."),
        ("{F} ¿Quiénes pagaban las obras?", "La Iglesia y las elites", "La ficha lo indica como continuidad."),
        ("=", "{F} Un taller hace 4 pinturas cada mes. ¿Cuántas pinturas hace en un año de 12 meses?", "4*12", "Se multiplica por los meses del año.", " pinturas"),
        ("{F} ¿Por qué aparecen motivos locales en las obras? A) Porque artesanos indígenas y mestizos trabajaban en los talleres B) Porque no se podía copiar nada", "A) Porque artesanos indígenas y mestizos trabajaban en los talleres", "La explicación de la clase lo señala."),
        ("{F} ¿Qué diferencia hay entre el barroco de Cusco y el de Chile según la ficha?", "En Chile las iglesias fueron de menor escala por terremotos y recursos", "La ficha compara esas condiciones."),
        ("{F} Un compañero dice: «El barroco colonial fue idéntico en todos los lugares». ¿Qué dato lo contradice?", "La ficha muestra distintas ciudades y una menor escala en Chile", "Hubo diferencias territoriales."),
        ("{F} ¿Qué relación hay entre ciudad rica y barroco? A) Las ciudades ricas pagaban talleres y templos B) Las ciudades pobres financiaban los talleres más grandes", "A) Las ciudades ricas pagaban talleres y templos", "La ficha menciona ciudades con talleres."),
        ("{F} ¿Qué afirmación es proporcional? A) El barroco cambió la forma de decorar, pero mantuvo el tema religioso y el rol de la Iglesia B) El barroco rompió con la religión", "A) El barroco cambió la forma de decorar, pero mantuvo el tema religioso y el rol de la Iglesia", "La ficha muestra cambios y continuidades."),
        ("{F} ¿Qué dato necesitarías para saber cuántas iglesias barrocas había en cada región?", "Un inventario de iglesias de cada región", "Permitiría comparar las regiones."),
        ("{F} ¿Qué quiere decir mestizo?", "Persona de ascendencia indígena y europea", "Se definió en el vocabulario."),
    ],
    ctx=("Un guía dice: «En Cusco y en Santiago el barroco es igual». Con la ficha, ¿cómo lo corriges? {F}", "En Cusco hubo templos y talleres más grandes; en Chile las construcciones fueron de menor escala por terremotos y recursos", "La ficha marca diferencias territoriales."),
    sc=[("¿Qué es un taller?", "Un lugar donde artesanos o artistas hacen obras en grupo", "Se definió en el vocabulario."),
        ("¿Qué continuidad del barroco menciona la ficha?", "La religión católica como tema principal", "La ficha lo indica."),
        ("¿Qué trajo el barroco? A) Más ornamentación y dramatismo B) Menos adornos", "A) Más ornamentación y dramatismo", "Son sus cambios.")],
    op=("Haz una tabla con dos columnas, «Cambio» y «Continuidad», y escribe en cada una tres rasgos de la ficha. Después dibuja un mapa muy simple con tres puntos (Cusco, México y una ciudad de Chile) y escribe al lado una característica del barroco en cada lugar. {F}",
        "Cambio: ornamentación, movimiento, motivos locales. Continuidad: religión, iglesia central, encargos de la Iglesia. Mapa: Cusco con talleres, México con Puebla, Chile con iglesias de menor escala.",
        ["tabla con tres rasgos por columna", "ubica tres puntos", "describe una característica por lugar"], ["tabla", "mapa"], ["mezclar cambios y continuidades", "decir que fue igual en todos lados"],
        "Pide que explique por qué Chile tuvo menor escala."),
    reinforce="Explica con tus palabras un cambio y una continuidad del barroco colonial.",
    extend="Escribe una pregunta sobre cómo afectaron los terremotos a las iglesias de Chile.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno; no son testimonios reales). "
     "Voz 1, obispo, 1690: «Estas fachadas, pinturas y fiestas acercan a los fieles a Dios y muestran la grandeza de la Iglesia.» "
     "Voz 2, comerciante criollo rico, 1690: «Pago un retablo para mi capilla porque honra a mi familia y muestra mi lugar en la ciudad.» "
     "Voz 3, artesano indígena de un taller, 1690: «Tallamos las flores y los frutos de nuestra tierra en la piedra; el taller nos paga poco, pero nuestro trabajo queda en la fachada.» "
     "Voz 4, monja y escritora, 1690: «Escribo versos y obras de teatro para el convento; muchas mujeres no tienen permiso de estudiar fuera de él.» "
     "Voz 5, vecino pobre de la ciudad, 1690: «En la procesión me siento parte de algo, pero no puedo pagar una cofradía.»")
build(
    OA, 4, F,
    use="Aprenderé a contrastar quiénes hicieron, pagaron y vivieron el barroco colonial, y a reconocer apropiaciones, mezclas y desigualdades.",
    prior=["Conozco los rasgos del barroco y sus expresiones.", "Sé contrastar perspectivas.", "Conozco la sociedad colonial."],
    explain=[
        "El barroco colonial no fue obra de un solo grupo. La Iglesia lo promovía para acercar a los fieles y mostrar su grandeza. Las elites criollas pagaban retablos y capillas para mostrar su lugar en la ciudad. Artesanos indígenas y mestizos tallaban y pintaban, incorporando motivos locales. Religiosas y escritoras participaron en el teatro y la poesía, aunque con limitaciones. Muchos vecinos pobres participaban como público en ceremonias y procesiones.",
        "Contrastar estas voces permite ver desigualdades. Quien pagaba obtenía prestigio; quien trabajaba recibía poco; y muchas personas solo veían las obras desde la plaza. También permite ver apropiación y mezcla: los motivos locales muestran que artesanos indígenas dejaron su huella, aunque el sistema los mantenía en una posición subordinada.",
        "Por eso conviene evitar dos simplificaciones: decir que el barroco es solo exceso decorativo, o decir que fue una expresión armónica de todos. Fue un lenguaje del poder y también un espacio de creatividad de grupos diversos.",
    ],
    vocab=[("retablo", "estructura decorada detrás del altar de una iglesia"), ("apropiación", "uso que un grupo hace de elementos de otro, adaptándolos"), ("subordinado", "que está bajo la autoridad o el mando de otro"), ("desigualdad", "diferencia injusta de poder, riqueza o derechos entre grupos"), ("público", "personas que miran o participan como espectadoras")],
    worked=[
        ("Reconocer una desigualdad", "¿Qué desigualdad muestra la voz 3 del artesano?", ["Dice que el taller paga poco.", "Pero su trabajo queda en la fachada."], "Trabaja mucho y recibe poco, aunque su huella queda"),
        ("Contrastar dos propósitos", "¿Qué diferencia hay entre el propósito del obispo y el del comerciante?", ["El obispo busca acercar a los fieles a Dios.", "El comerciante busca honrar a su familia y su lugar."], "El obispo, un fin religioso; el comerciante, prestigio familiar"),
    ],
    mistakes=[("Definir el barroco solo como exceso decorativo.", "Se ignora quiénes lo hicieron y para qué.", "Incluye actores, propósitos y desigualdades."),
              ("Borrar el trabajo de artesanos indígenas y mestizos.", "Se atribuye todo a la Iglesia o a las elites.", "Menciona quién tallaba y pintaba.")],
    T=[
        ("{F} ¿Quién paga un retablo para su capilla?", "El comerciante criollo rico", "Es la voz 2."),
        ("{F} ¿Qué tallan los artesanos indígenas en la piedra?", "Las flores y los frutos de su tierra", "La voz 3 lo dice."),
        ("{F} ¿Qué escribe la monja de la voz 4?", "Versos y obras de teatro para el convento", "Lo dice su voz."),
        ("{F} ¿Qué dice el vecino pobre sobre la procesión?", "Se siente parte de algo, pero no puede pagar una cofradía", "La voz 5 lo expresa."),
        ("=", "{F} Con datos de ejemplo, un artesano gana 5 monedas por semana y el comerciante paga 200 monedas por un retablo. ¿Cuántas semanas de sueldo del artesano equivalen al retablo?", "200//5", "Se divide el precio del retablo por el sueldo semanal.", " semanas"),
        ("{F} Clasifica cada voz según su papel: a) voz 1, b) voz 2, c) voz 3. Opciones: promotor religioso; patrocinador rico; artesano que trabaja.", "a) promotor religioso; b) patrocinador rico; c) artesano que trabaja", "Cada voz tiene un papel."),
        ("{F} ¿Qué voz muestra una apropiación de motivos locales? A) La voz 3 B) La voz 2", "A) La voz 3", "El artesano pone flores y frutos de su tierra."),
        ("{F} ¿Qué desigualdad señala la voz 4?", "Que muchas mujeres no pueden estudiar fuera del convento", "La voz 4 lo dice."),
        ("{F} Un compañero dice: «El barroco fue una expresión armónica de todos los grupos». ¿Qué voces lo contradicen?", "La voz 3, por el poco pago, y la voz 5, por no poder pagar una cofradía", "Ambas voces muestran desigualdades."),
        ("{F} ¿Qué propósito comparten las voces 1 y 2? A) Mostrar grandeza o prestigio con las obras B) Esconder las obras para protegerlas", "A) Mostrar grandeza o prestigio con las obras", "Ambos usan el arte para mostrar poder o prestigio."),
        ("{F} ¿Qué voz falta en la ficha y sería importante escuchar?", "La de una persona esclavizada o de un niño", "La ficha no incluye a esos grupos."),
        ("{F} ¿Qué conclusión es proporcional? A) El barroco colonial fue un lenguaje del poder y también un espacio de creatividad de grupos diversos B) Fue solo decoración", "A) El barroco colonial fue un lenguaje del poder y también un espacio de creatividad de grupos diversos", "Las voces muestran ambos aspectos."),
        ("{F} ¿Qué error comete quien atribuye toda la fachada al obispo?", "Borra el trabajo de los artesanos indígenas", "La voz 3 muestra quién tallaba."),
    ],
    ctx=("Un museo quiere una etiqueta justa para la fachada de la ficha. ¿Qué voces debe incluir para evitar borrar a los artesanos? {F}", "La del obispo o el comerciante que pagan, y la del artesano indígena que talla los motivos locales", "Así se muestran quienes pagan y quienes hacen la obra."),
    sc=[("¿Qué es un retablo?", "Una estructura decorada detrás del altar de una iglesia", "Se definió en el vocabulario."),
        ("¿Qué es una apropiación?", "El uso que un grupo hace de elementos de otro, adaptándolos", "Se definió en el vocabulario."),
        ("¿Qué voz critica el pago del taller? A) La del artesano indígena B) La del obispo", "A) La del artesano indígena", "La voz 3 dice que paga poco.")],
    op=("Escribe un diálogo de seis líneas entre el comerciante criollo y el artesano indígena de la ficha, sobre el retablo y la fachada. Cada uno usa un dato de su voz. Cierra con una frase tuya que explique en qué se diferencian sus situaciones y qué dejó cada uno en la obra. {F}",
        "Comerciante: pago el retablo para honrar a mi familia. Artesano: tallamos flores y frutos de nuestra tierra y el taller paga poco. Cierre: uno deja prestigio, el otro deja huella en la piedra.",
        ["usa datos de las voces", "muestra la desigualdad", "cierra explicando las diferencias"], ["diálogo", "frase"], ["inventar hechos que contradicen la ficha", "borrar al artesano"],
        "Pide que explique qué le parece justo o injusto en esa relación."),
    reinforce="Explica con tus palabras tres grupos que participaron en el barroco colonial y su papel.",
    extend="Escribe una pregunta que le harías a una monja escritora de la época.",
)
