"""Material del estudiante de 7.º básico, Historia, Geografía y Ciencias Sociales: OA 05 (el Mediterráneo antiguo como espacio de intercambio)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI07 OA 05"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (datos resumidos, hechos para este cuaderno; las distancias y velocidades son de ejemplo). "
     "El mar Mediterráneo está rodeado por tres continentes: al norte Europa (Grecia, Italia), al este Asia (Fenicia, Anatolia) y al sur África (Egipto, Cartago). "
     "Se une al océano Atlántico por el estrecho de Gibraltar, de unos 14 km de ancho en su punto más angosto. Tiene muchas islas, como Sicilia, Creta, Chipre y Cerdeña. "
     "Clima: veranos secos y calurosos, e inviernos suaves y lluviosos. Cultivos típicos: trigo, olivo y vid. "
     "Las costas tienen montañas cercanas y pocas llanuras. En verano el mar suele estar tranquilo; en invierno hay temporales. "
     "Dato de ejemplo: un barco a vela avanzaba unos 100 km en un día de buen tiempo.")
build(
    OA, 1, F,
    use="Aprenderé a describir el espacio mediterráneo: sus costas, islas, clima y condiciones para navegar. Sirve para entender por qué el mar fue un camino de contacto.",
    prior=["Sé ubicar Europa, Asia y África.", "Sé qué es un factor geográfico.", "Sé usar escalas de distancia."],
    explain=[
        "El Mediterráneo es un mar casi cerrado rodeado por Europa, Asia y África. Se une al océano Atlántico por el estrecho de Gibraltar y tiene muchas islas, como Sicilia, Creta y Chipre. Sus costas son montañosas y con pocas llanuras, por lo que las comunidades buscaron cultivos que se dieran en ese terreno.",
        "El clima mediterráneo tiene veranos secos y calurosos e inviernos suaves y lluviosos. En esas condiciones se cultivaron trigo, olivo y vid, que dieron pan, aceite y vino. En verano el mar suele estar tranquilo, por lo que la navegación era más segura entre la primavera y el otoño; en invierno, los temporales hacían peligroso navegar.",
        "Las islas servían de escalas y orientación para barcos que navegaban cerca de la costa. Por eso el mar funcionó como un espacio de contacto y no como una frontera vacía: fue la ecúmene de griegos, fenicios y romanos, es decir, el espacio habitado y conocido por ellos. Pero la geografía no obligó a nadie: facilitó el viaje, y los pueblos decidieron comerciar, fundar ciudades o hacer guerras.",
    ],
    vocab=[("estrecho", "paso angosto de agua entre dos tierras"), ("isla", "tierra rodeada de agua por todos lados"), ("clima mediterráneo", "clima de veranos secos y calurosos e inviernos suaves y lluviosos"), ("ecúmene", "espacio habitado y conocido por una sociedad"), ("temporal", "tormenta fuerte en el mar"), ("escala", "parada de un barco en un puerto durante un viaje")],
    worked=[
        ("Calcular un tiempo de viaje", "{F} ¿Cuántos días tarda un barco en avanzar 200 km?", ["Avanza 100 km por día.", "Divido: 200 ÷ 100 = 2."], "2 días"),
        ("Leer el clima", "{F} ¿En qué estación es más segura la navegación y por qué?", ["En verano el mar suele estar tranquilo.", "En invierno hay temporales."], "En verano, porque el mar está más tranquilo"),
    ],
    mistakes=[("Describir el mar como un espacio vacío que separaba a los pueblos.", "Se piensa solo en el agua y no en las rutas.", "Con islas y costas cercanas, el mar fue un camino que conectó."),
              ("Decir que la geografía obligó a los pueblos a navegar.", "Se confunde facilitar con determinar.", "El mar permitió viajar, pero cada pueblo decidió qué hacer.")],
    T=[
        ("{F} ¿Con qué océano se une el Mediterráneo?", "Con el océano Atlántico", "La ficha lo indica."),
        ("{F} ¿Cuáles son los tres cultivos típicos?", "Trigo, olivo y vid", "La ficha los nombra."),
        ("{F} ¿En qué continente está Cartago?", "En África", "La ficha ubica a Cartago al sur."),
        ("=", "{F} ¿Cuántos días tarda un barco en avanzar 300 km?", "300//100", "Se divide la distancia por lo que avanza en un día.", " días"),
        ("En Historia: ¿qué significa que el Mediterráneo fue la «ecúmene» de griegos y romanos?", "Que era el espacio habitado y conocido por ellos, unido por el mar", "Ecúmene es el espacio habitado y conocido por una sociedad."),
        ("{F} ¿Qué estación tenía temporales que dificultaban navegar?", "El invierno", "La ficha lo dice."),
        ("=", "{F} Dos puertos están separados por 500 km. ¿Cuántos días de buen tiempo necesita un barco para ir de uno a otro?", "500//100", "Se divide la distancia por 100 km diarios.", " días"),
        ("{F} ¿Por qué las islas ayudaban a los barcos que navegaban cerca de la costa?", "Servían de escalas y de puntos de orientación", "Permitían detenerse y no perder de vista la tierra."),
        ("{F} Clasifica cada lugar según su continente: Grecia, Egipto, Fenicia.", "Grecia: Europa; Egipto: África; Fenicia: Asia", "La ficha los ubica por costas."),
        ("{F} Ana dice: «El Mediterráneo era un espacio vacío que separaba a los pueblos». Corrígela con dos datos de la ficha.", "Tenía muchas islas y costas cercanas que servían de escalas, y rodeaba tres continentes conectados por el mar", "El mar fue un camino de contacto."),
        ("{F} Las costas tienen montañas cercanas y pocas llanuras. ¿Por qué eso pudo hacer más importante la navegación?", "Porque por tierra era difícil mover cargas y por mar se conectaban las costas", "El relieve dificultaba los caminos terrestres."),
        ("{F} Un viajero quiere salir de Grecia a Egipto en enero. ¿Qué dificultad tiene según la ficha?", "Los temporales del invierno hacen peligrosa la navegación", "Enero está en invierno."),
        ("{F} Un compañero dice: «Como había mar, los pueblos tuvieron que navegar». Corrígelo.", "El mar facilitó el viaje, pero los pueblos decidieron si navegar, comerciar o no", "La geografía no determina las decisiones."),
    ],
    ctx=("Un agente de viajes de la Antigüedad debe llevar trigo desde Egipto hasta una isla a 400 km. ¿Cuántos días necesita y en qué estación le conviene salir? {F}", "4 días, en verano", "400 ÷ 100 = 4 días; el verano es más seguro."),
    sc=[("¿Qué es un estrecho?", "Un paso angosto de agua entre dos tierras", "Gibraltar es un ejemplo."),
        ("¿Qué clima tiene el Mediterráneo?", "Veranos secos y calurosos e inviernos suaves y lluviosos", "Es el clima que lleva su nombre."),
        ("=", "{F} ¿Cuántos km avanza un barco en 6 días de buen tiempo?", "6*100", "Se multiplican los días por 100 km diarios.", " km")],
    op=("Dibuja un mapa sencillo del Mediterráneo con tres costas (norte, este y sur), tres islas y el estrecho de Gibraltar. Escribe junto a cada costa un país o ciudad de la ficha y una frase que explique por qué el mar conectaba esos lugares. {F}",
        "Norte: Grecia; este: Fenicia; sur: Egipto; islas: Sicilia, Creta, Chipre; Gibraltar al oeste.",
        ["ubica tres costas e islas", "marca Gibraltar", "la frase explica la conexión"], ["mapa dibujado", "frase escrita"], ["poner Egipto en Europa", "decir que el mar separaba"],
        "Pide que explique qué lugar sería una buena escala para un barco que va de Fenicia a Sicilia."),
    reinforce="Nombra tres islas y tres cultivos del Mediterráneo.",
    extend="Escribe una pregunta sobre cómo se orientaban los marineros cuando no veían la costa.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (datos resumidos, hechos para este cuaderno; los días de viaje son de ejemplo). "
     "Productos: Fenicia vendía madera de cedro, púrpura (un tinte) y vidrio. Egipto vendía trigo, papiro y lino. Grecia vendía aceite de oliva, vino y cerámica. Iberia, en el extremo oeste, vendía plata. "
     "Ruta fenicia de ejemplo, de este a oeste: Tiro, Chipre, Creta, Sicilia, Cartago y Gádir (hoy Cádiz). "
     "Días de viaje entre puertos, en ese orden: 3, 4, 5, 3 y 6.")
build(
    OA, 2, F,
    use="Aprenderé a trazar rutas comerciales y a relacionar cada lugar con sus productos. Sirve para entender qué circulaba por el Mediterráneo y entre quiénes.",
    prior=["Sé describir el espacio mediterráneo.", "Sé sumar y multiplicar con números pequeños.", "Sé leer un mapa de rutas."],
    explain=[
        "Una ruta comercial es un camino que siguen las mercancías y las personas entre lugares. En el Mediterráneo, muchas rutas pasaban de puerto en puerto. Una ruta fenicia podía ir de Tiro a Chipre, Creta, Sicilia, Cartago y Gádir, en el extremo oeste. Cada tramo se contaba en días de viaje.",
        "Cada región ofrecía productos distintos. Fenicia vendía cedro, púrpura y vidrio; Egipto, trigo, papiro y lino; Grecia, aceite, vino y cerámica; Iberia, plata. Así, un mismo barco podía salir cargado de un producto y volver con otros. La diversidad de productos es una razón por la que el intercambio resultaba útil para todos.",
        "No fue un solo pueblo el que comerció: fenicios, griegos, egipcios y cartagineses lo hicieron. Para reconstruir las rutas, los historiadores usan evidencias como ánforas (vasijas de transporte) con marcas, restos de naufragios y textos. Una ruta es una reconstrucción, y puede cambiar con nuevos hallazgos.",
    ],
    vocab=[("ruta comercial", "camino que siguen las mercancías entre lugares"), ("mercancía", "producto que se compra y se vende"), ("ánfora", "vasija grande para transportar aceite, vino u otros productos"), ("naufragio", "hundimiento de un barco"), ("tramo", "parte de un recorrido entre dos puntos")],
    worked=[
        ("Sumar tramos", "{F} ¿Cuántos días tarda el viaje de Tiro hasta Creta?", ["Tiro a Chipre: 3 días. Chipre a Creta: 4 días.", "Sumo: 3 + 4 = 7."], "7 días"),
        ("Asociar producto y lugar", "{F} ¿Qué producto de Egipto se podía escribir encima?", ["Egipto vendía trigo, papiro y lino.", "El papiro sirve para escribir."], "Papiro"),
    ],
    mistakes=[("Pensar que la ruta es una línea recta de un punto a otro.", "Se ignoran las escalas en islas y puertos.", "La ruta pasa de puerto en puerto, con paradas."),
              ("Atribuir todo el comercio a un solo pueblo, como los fenicios.", "Se simplifica a un solo actor.", "Griegos, egipcios y cartagineses también comerciaban.")],
    T=[
        ("{F} ¿Qué vendía Grecia?", "Aceite de oliva, vino y cerámica", "La ficha lo indica."),
        ("{F} ¿Qué vendía Iberia?", "Plata", "La ficha lo indica."),
        ("{F} ¿Cuál es el último puerto de la ruta fenicia de ejemplo?", "Gádir", "Es el extremo oeste."),
        ("=", "{F} ¿Cuántos días tarda el viaje completo, de Tiro a Gádir?", "3+4+5+3+6", "Se suman los días de todos los tramos.", " días"),
        ("=", "{F} ¿Cuántos días tarda el viaje de Tiro hasta Sicilia?", "3+4+5", "Se suman los tres primeros tramos.", " días"),
        ("{F} ¿Cuántos puertos y cuántos tramos tiene la ruta de ejemplo?", "6 puertos y 5 tramos", "Hay un tramo menos que puertos."),
        ("{F} Clasifica cada producto como alimento (A), material (M) o fabricado (F): 1) trigo; 2) cedro; 3) vidrio; 4) aceite.", "1 A, 2 M, 3 F, 4 A", "Trigo y aceite se comen; el cedro es madera sin trabajar; el vidrio se fabrica."),
        ("{F} Un barco sale de Tiro con cedro y llega a Gádir. ¿Qué producto de la ficha puede traer de vuelta?", "Plata", "Iberia vendía plata."),
        ("=", "{F} Si un barco hace la ruta completa de ida y vuelta, ¿cuántos días viaja en total?", "2*(3+4+5+3+6)", "Se duplica el tiempo de la ida.", " días"),
        ("{F} Pedro dice: «Solo los fenicios comerciaban en el Mediterráneo». Corrígelo con la ficha.", "También vendían productos Egipto, Grecia e Iberia, así que había varios pueblos que comerciaban", "La ficha lista productos de varios lugares."),
        ("{F} ¿Por qué una ruta tiene escalas en islas como Chipre y Creta?", "Porque los barcos viajaban de puerto en puerto, sin perder de vista la costa", "Las islas servían de paradas."),
        ("{F} ¿Qué evidencia arqueológica probaría que el aceite griego llegó a Egipto?", "Ánforas con marcas griegas halladas en un sitio de Egipto", "El objeto aparece lejos de su origen."),
        ("{F} Un barco carga solo cedro desde Tiro. ¿Es una buena idea volver vacío? Explica con un dato.", "No: conviene traer otro producto, como plata desde Iberia, para aprovechar el viaje", "La diversidad de productos hace útil el intercambio."),
    ],
    ctx=("Una tienda de museo vende un mapa de rutas con productos. Un visitante pregunta qué se llevaba de Egipto a Grecia. Usa la ficha para dar tres opciones posibles. {F}", "Trigo, papiro y lino", "Son los productos que vende Egipto."),
    sc=[("¿Qué es una ánfora?", "Una vasija grande para transportar aceite, vino u otros productos", "Sirve como evidencia de comercio."),
        ("=", "{F} ¿Cuántos días tarda el viaje de Sicilia a Gádir?", "3+6", "Se suman los dos últimos tramos.", " días"),
        ("¿Es una ruta una línea recta o una serie de puertos y escalas?", "Una serie de puertos y escalas", "Los barcos viajaban de puerto en puerto.")],
    op=("Dibuja un mapa esquemático de la ruta de la ficha, con los seis puertos y los días de cada tramo. Escribe un producto que se vendiera en cada región y qué evidencia arqueológica probaría esa ruta. {F}",
        "Tiro–Chipre: 3; Chipre–Creta: 4; Creta–Sicilia: 5; Sicilia–Cartago: 3; Cartago–Gádir: 6; productos y ánforas como evidencia.",
        ["marca los seis puertos y los cinco tramos", "los días coinciden con la ficha", "nombra una evidencia"], ["mapa dibujado"], ["olvidar un tramo", "no mencionar evidencia"],
        "Pide que explique qué ruta de regreso usaría y qué traería."),
    reinforce="Nombra tres productos de tres regiones distintas.",
    extend="Escribe una pregunta sobre cómo se cobraba el pago de un cargamento en puertos lejanos.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (datos resumidos, hechos para este cuaderno; los números de barcos son de ejemplo). "
     "Navegación: los barcos viajaban cerca de la costa, de puerto en puerto, y por la noche fondeaban o se orientaban por las estrellas. "
     "Puertos: en un puerto había muelles, astilleros (talleres donde se construyen barcos), bodegas y un mercado. "
     "Colonias: los fenicios fundaron Cartago, en la costa de África, según la tradición hacia el siglo IX a. C.; los griegos fundaron Siracusa, en Sicilia, hacia 730 a. C., y Massalia (hoy Marsella), en la costa de Francia, hacia 600 a. C. "
     "Un puerto de ejemplo recibe 40 barcos al mes durante 8 meses de buen tiempo y 5 barcos al mes durante los 4 meses de invierno.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar la navegación, las ciudades portuarias y los contactos entre pueblos. Sirve para entender cómo el comercio hizo crecer puertos y colonias.",
    prior=["Sé qué son las rutas comerciales.", "Sé que el clima limita la navegación en invierno.", "Sé multiplicar y sumar."],
    explain=[
        "Los barcos antiguos, de vela y remos, navegaban en general cerca de la costa, de puerto en puerto. De noche fondeaban cerca de tierra o se orientaban por las estrellas. Esta navegación era más segura entre la primavera y el otoño, y se reducía en invierno por los temporales.",
        "Los puertos eran ciudades activas: tenían muelles, astilleros, bodegas y mercados. Allí se encontraban marineros, comerciantes y artesanos de muchos lugares. Algunas ciudades fundaron colonias, es decir, nuevas ciudades lejos de la original: los fenicios fundaron Cartago y los griegos fundaron Siracusa y Massalia. Las colonias facilitaban el comercio y también significaban nuevos contactos con los pueblos que ya vivían allí.",
        "Los contactos no fueron solo de comercio: también se intercambiaron lenguas, costumbres y creencias. Pero no fueron siempre pacíficos: hubo alianzas, competencia y guerras entre ciudades. Para explicar el crecimiento de un puerto se combinan varios factores: su ubicación, la navegación, el comercio y las decisiones de sus gobernantes.",
    ],
    vocab=[("astillero", "taller donde se construyen y reparan barcos"), ("fondear", "dejar el barco anclado cerca de la costa"), ("colonia", "ciudad nueva fundada lejos de la ciudad de origen"), ("bodega", "lugar para guardar mercancías"), ("puerto", "lugar de la costa donde llegan y salen barcos")],
    worked=[
        ("Calcular la actividad de un puerto", "{F} ¿Cuántos barcos recibe en los 8 meses de buen tiempo?", ["Recibe 40 barcos cada mes.", "Multiplico: 8 × 40 = 320."], "320 barcos"),
        ("Reconocer una colonia", "{F} ¿Por qué Siracusa es una colonia griega?", ["Los griegos la fundaron en Sicilia.", "Está lejos de su ciudad de origen."], "Porque es una ciudad fundada lejos de Grecia por griegos"),
    ],
    mistakes=[("Pensar que los barcos antiguos cruzaban el mar abierto como los barcos de hoy.", "Se aplican técnicas modernas.", "Navegaban cerca de la costa y se orientaban por tierra y estrellas."),
              ("Creer que los contactos eran siempre pacíficos.", "Se mira solo el comercio.", "Hubo comercio, alianzas, competencia y guerras.")],
    T=[
        ("{F} ¿Dónde fundaron los fenicios la colonia de Cartago?", "En la costa de África", "La ficha lo indica."),
        ("{F} ¿Cómo se orientaban los marineros por la noche?", "Por las estrellas, o fondeaban cerca de tierra", "La ficha lo indica."),
        ("{F} ¿Qué es un astillero?", "Un taller donde se construyen barcos", "La ficha lo define."),
        ("=", "{F} ¿Cuántos barcos recibe el puerto de ejemplo en los 4 meses de invierno?", "4*5", "Se multiplican los meses por los barcos mensuales.", " barcos"),
        ("=", "{F} ¿Cuántos barcos recibe el puerto de ejemplo en un año?", "8*40+4*5", "Se suman los barcos del buen tiempo y del invierno.", " barcos"),
        ("{F} ¿Quiénes fundaron Massalia y dónde está hoy esa ciudad?", "Los griegos; hoy es Marsella, en la costa de Francia", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos barcos más recibe el puerto al mes en buen tiempo que en invierno?", "40-5", "Se resta la cifra de invierno a la de buen tiempo.", " barcos"),
        ("{F} Ordena las colonias de la más antigua a la más reciente: Massalia, Siracusa.", "Siracusa (hacia 730 a. C.), Massalia (hacia 600 a. C.)", "En a. C., el número mayor es más antiguo."),
        ("{F} ¿Por qué un puerto necesitaba astilleros y bodegas?", "Para construir y reparar barcos y para guardar las mercancías que llegaban", "Eran servicios que sostenían el comercio."),
        ("{F} Lucía dice: «Los contactos del Mediterráneo eran siempre pacíficos». Corrígela.", "Hubo comercio, pero también competencia, alianzas y guerras entre ciudades", "El contacto incluye relaciones de distinto tipo."),
        ("{F} ¿Por qué el puerto de ejemplo recibe tantos menos barcos en invierno?", "Porque los temporales hacían peligrosa la navegación", "Se navegaba sobre todo de primavera a otoño."),
        ("{F} Un compañero afirma: «Un puerto crece solo porque está en la costa». Nombra otro factor.", "El comercio, la navegación o las decisiones de sus gobernantes", "Hay varios factores combinados."),
        ("{F} ¿Qué contactos con los pueblos locales podía significar fundar una colonia?", "Intercambios de productos y costumbres, pero también competencia o conflictos por la tierra", "Las colonias se fundaban en tierras con habitantes."),
    ],
    ctx=("Una ciudad portuaria quiere construir un muelle nuevo, un astillero y una bodega. ¿Qué dos de esas obras ayudarían más a recibir y guardar mercancías? {F}", "El muelle y la bodega", "El muelle recibe barcos y la bodega guarda lo que llega."),
    sc=[("¿Qué es una colonia?", "Una ciudad nueva fundada lejos de la ciudad de origen", "Cartago y Siracusa son ejemplos."),
        ("¿Qué es fondear?", "Dejar el barco anclado cerca de la costa", "Era lo que hacían de noche."),
        ("=", "{F} ¿Cuántos barcos recibe en 3 meses de buen tiempo?", "3*40", "Se multiplican los meses por los barcos mensuales.", " barcos")],
    op=("Imagina que eres comerciante en un puerto de la ficha. Escribe un diario de 5 líneas con los productos que llegan, un contacto con otro pueblo, un problema de la navegación y una decisión que tomas. {F}",
        "Llegan cerámica y aceite; conozco a un marinero fenicio; hay temporales; decido esperar hasta la primavera.",
        ["menciona productos y un contacto", "incluye un problema de navegación", "usa datos de la ficha"], ["diario escrito"], ["usar objetos modernos", "mostrar solo contactos pacíficos"],
        "Pide que explique qué pasaría con su negocio en invierno."),
    reinforce="Explica con tus palabras qué hacía un astillero y para qué servía una bodega.",
    extend="Escribe una pregunta sobre cómo se comunicaban dos marineros que hablaban idiomas distintos.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (datos resumidos, hechos para este cuaderno). "
     "El alfabeto fenicio, de hacia 1050 a. C., tiene 22 signos que representan consonantes; sus nombres incluyen aleph (buey) y beth (casa). "
     "El alfabeto griego, de hacia 800 a. C., tiene 24 letras; usa signos fenicios y añade letras para las vocales; sus primeras letras se llaman alfa y beta. "
     "El alfabeto latino, de hacia 600 a. C., se basa en el griego, a través del etrusco (pueblo de Italia). "
     "Moneda: las primeras monedas aparecen en Lidia, en Asia Menor, hacia el siglo VII a. C., y luego se usan en ciudades griegas.")
build(
    OA, 4, F,
    use="Aprenderé a inferir cómo circularon ideas y técnicas por el Mediterráneo a partir de evidencias. Sirve para razonar con fechas y semejanzas sin exagerar.",
    prior=["Sé que el comercio crea contactos.", "Sé comparar años a. C.", "Sé distinguir descripción e interpretación."],
    explain=[
        "Con los productos viajaron también ideas y técnicas. Un ejemplo es el alfabeto: el fenicio, de unos 22 signos para consonantes, fue adaptado por los griegos, que agregaron letras para las vocales. Después el alfabeto latino se basó en el griego, a través del etrusco. La palabra «alfabeto» viene de alfa y beta, las dos primeras letras griegas.",
        "Los historiadores infieren una circulación de ideas con pistas: semejanza de formas, nombres parecidos, fechas y lugares de contacto. Si el alfabeto fenicio es de hacia 1050 a. C. y el griego de hacia 800 a. C., es razonable pensar que el fenicio fue el modelo. Pero una semejanza sola no basta: hace falta una fecha anterior y un contacto posible.",
        "La moneda es otro ejemplo: las primeras aparecen en Lidia, en Asia Menor, y luego se usan en ciudades griegas. Una inferencia es una conclusión razonable, no una certeza. Se mejora al sumar evidencias y se debe expresar con prudencia, con frases como «es probable que» o «parece que».",
    ],
    vocab=[("inferir", "sacar una conclusión razonable a partir de pistas"), ("alfabeto", "conjunto de signos que representan sonidos"), ("consonante", "sonido que se pronuncia con ayuda de una vocal; en fenicio se escribían sin vocales"), ("difusión", "paso de una idea o técnica de un lugar a otros"), ("moneda", "pieza de metal con valor fijado por una autoridad")],
    worked=[
        ("Comparar fechas", "{F} ¿Cuántos años antes que el griego aparece el alfabeto fenicio?", ["Fechas: 1050 y 800 a. C.", "Resto: 1050 − 800 = 250."], "250 años"),
        ("Inferir con prudencia", "{F} ¿Qué se puede decir con prudencia sobre el origen del alfabeto griego?", ["El fenicio es anterior al griego.", "Y los griegos comerciaban con los fenicios."], "Es probable que se haya basado en el fenicio"),
    ],
    mistakes=[("Afirmar con certeza que los griegos copiaron todo de los fenicios.", "Se pasa de una pista a una certeza.", "Di «es probable» y nombra la evidencia: fechas y semejanzas."),
              ("Decir que dos cosas parecidas siempre tienen origen común.", "Se usa solo la semejanza.", "Agrega la fecha, el lugar y el contacto posible.")],
    T=[
        ("{F} ¿Cuántos signos tiene el alfabeto fenicio?", "22", "La ficha lo indica."),
        ("{F} ¿Cuántas letras tiene el alfabeto griego de la ficha?", "24", "La ficha lo indica."),
        ("{F} ¿Dónde aparecen las primeras monedas según la ficha?", "En Lidia, en Asia Menor", "La ficha lo indica."),
        ("=", "{F} ¿Cuántas letras más tiene el alfabeto griego que el fenicio?", "24-22", "Se resta el número menor al mayor.", " letras"),
        ("=", "{F} ¿Cuántos años antes que el latino aparece el alfabeto griego?", "800-600", "Se restan los años a. C.", " años"),
        ("{F} ¿Qué agregaron los griegos al alfabeto fenicio?", "Letras para las vocales", "La ficha lo dice."),
        ("{F} ¿De dónde viene la palabra «alfabeto»?", "De alfa y beta, las dos primeras letras griegas", "La ficha lo indica."),
        ("{F} Ordena de más antiguo a más reciente: alfabeto latino, alfabeto fenicio, alfabeto griego.", "Fenicio, griego, latino", "Las fechas son 1050, 800 y 600 a. C."),
        ("{F} ¿Qué dos pistas apoyan que el alfabeto griego se basó en el fenicio?", "Que el fenicio es anterior y que los griegos usan signos fenicios", "La ficha da la fecha y la semejanza de signos."),
        ("{F} Pedro dice: «Se sabe con certeza que los griegos copiaron todo de los fenicios». Corrígelo.", "Es una inferencia probable, no una certeza, y los griegos hicieron cambios como agregar vocales", "La ficha muestra un cambio original."),
        ("{F} Un compañero dice: «Dos alfabetos con letras parecidas deben tener origen común». ¿Qué le falta a su razonamiento?", "Agregar fechas, lugar y un contacto posible, no solo semejanzas", "La semejanza sola no basta."),
        ("{F} ¿Qué evidencia ayudaría a saber si las monedas lidias influyeron en las ciudades griegas?", "Monedas lidias halladas en ciudades griegas, o monedas griegas posteriores con diseños parecidos", "Las fechas y los objetos muestran el paso de la técnica."),
        ("{F} Elige la frase más prudente: A) Es probable que los griegos adaptaran el alfabeto fenicio; B) Es seguro que los griegos copiaron cada letra fenicia sin cambiar nada.", "A) Es probable que los griegos adaptaran el alfabeto fenicio", "Una inferencia debe expresarse con prudencia."),
    ],
    ctx=("Un museo exhibe una vasija con escritura que usa signos parecidos al fenicio, pero con letras para vocales. ¿A qué conclusión prudente llega el rótulo? {F}", "Es probable que sea una escritura griega temprana, derivada de la fenicia", "Tiene signos fenicios con vocales agregadas."),
    sc=[("¿Qué es inferir?", "Sacar una conclusión razonable a partir de pistas", "No es una certeza."),
        ("¿Qué alfabeto es anterior: el fenicio o el griego?", "El fenicio", "Su fecha es hacia 1050 a. C."),
        ("=", "{F} ¿Cuántos años antes que el latino aparece el alfabeto fenicio?", "1050-600", "Se restan los años a. C.", " años")],
    op=("Escribe una inferencia sobre cómo viajó el alfabeto por el Mediterráneo: nombra dos pistas de la ficha, una fecha y una frase con «es probable que». Añade qué evidencia nueva la haría más segura. {F}",
        "Es probable que el alfabeto griego se basara en el fenicio, porque es posterior y usa signos parecidos; ayudarían inscripciones griegas muy antiguas.",
        ["usa dos pistas", "cita una fecha", "la frase es prudente"], ["inferencia escrita"], ["afirmar con certeza", "usar solo semejanzas"],
        "Pide que explique por qué los fenicios no «regalaron» el alfabeto, sino que los griegos lo adaptaron."),
    reinforce="Di en voz alta los tres alfabetos en orden de antigüedad.",
    extend="Escribe una pregunta sobre otra técnica o idea que pudo viajar por el Mediterráneo.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (datos resumidos y de ejemplo, hechos para este cuaderno). "
     "Oportunidades del mar: llevar una carga por mar cuesta menos que por tierra; hay muchos puertos naturales; las islas sirven de escalas. "
     "Límites: temporales en invierno; piratas en algunas rutas; costas con montañas y pocos ríos navegables; escasez de agua en algunas islas; guerras entre ciudades. "
     "Dato de ejemplo: llevar una carga cuesta 3 monedas por mar y 30 por tierra. "
     "Grecia: relieve de montañas que separan valles, con islas y bahías que sirven de puertos; cada ciudad con su valle (polis o ciudad-Estado) se gobernaba por su cuenta. "
     "Roma: en la península italiana, en el centro del Mediterráneo, junto al río Tíber, a unos 25 km del mar y entre colinas fáciles de defender; desde 509 a. C., según la tradición, se gobernó como república (sin rey). "
     "Caso: la ciudad de Atenas importaba una parte de su trigo desde la costa del mar Negro, y pactó alianzas para proteger esas rutas.")
build(
    OA, 5, F,
    use="Aprenderé a explicar las oportunidades y los límites que el espacio geográfico ofrecía al intercambio. Sirve para evitar que la geografía parezca la única causa de lo ocurrido.",
    prior=["Sé describir el espacio mediterráneo y sus rutas.", "Sé que el comercio crea contactos.", "Sé multiplicar y restar con números pequeños."],
    explain=[
        "El Mediterráneo ofrecía grandes oportunidades al intercambio. Llevar una carga por mar costaba menos que por tierra, había muchos puertos naturales y las islas servían de escalas. Por eso las ciudades de la costa pudieron conseguir productos de lugares lejanos y vender los propios.",
        "También había límites. Los temporales del invierno reducían la navegación, algunos tramos tenían piratas, las costas montañosas dificultaban los caminos hacia el interior y había poca agua en algunas islas. Además, las guerras entre ciudades cortaban rutas. Por eso las ciudades pactaban alianzas y construían flotas para protegerlas.",
        "El relieve de Grecia, con montañas que separaban valles, ayuda a explicar las ciudades-Estado independientes (polis), y sus puertos las llevaron al mar. Roma, en el centro del Mediterráneo, junto al río Tíber y entre colinas defendibles, tuvo acceso al río y al mar y pudo expandirse como república. La geografía abrió posibilidades, pero no decidió todo. Dos ciudades con puertos parecidos pudieron actuar de manera distinta: una pactar alianzas, la otra cerrar su puerto. Una explicación sólida combina geografía, decisiones políticas, tecnología y relaciones con otros pueblos, y reconoce que no sabemos todo.",
    ],
    vocab=[("oportunidad", "condición que permite hacer algo útil"), ("límite", "condición que dificulta o impide hacer algo"), ("pirata", "persona que asalta barcos en el mar"), ("alianza", "pacto entre ciudades o pueblos para ayudarse"), ("importar", "traer productos desde otro lugar")],
    worked=[
        ("Calcular un ahorro", "{F} ¿Cuántas monedas se ahorran al llevar una carga por mar y no por tierra?", ["Por tierra cuesta 30 y por mar 3.", "Resto: 30 − 3 = 27."], "27 monedas"),
        ("Distinguir oportunidad y límite", "{F} ¿Un temporal de invierno es una oportunidad o un límite?", ["Dificulta navegar.", "Por eso es un límite."], "Un límite"),
    ],
    mistakes=[("Decir que la geografía determinó todas las decisiones de los pueblos.", "Se ignoran las alianzas, la política y la tecnología.", "La geografía abrió posibilidades, pero los pueblos decidieron."),
              ("Mirar solo las ventajas del mar.", "Se omiten los riesgos y límites.", "Nombra oportunidades y límites antes de concluir.")],
    T=[
        ("{F} ¿Qué rasgo del relieve de Grecia ayuda a explicar que hubiera muchas ciudades-Estado independientes?", "Las montañas separaban los valles, y cada ciudad con su valle se gobernaba por su cuenta", "El relieve aislaba a unas ciudades de otras."),
        ("{F} ¿Cuánto cuesta llevarla por tierra?", "30 monedas", "La ficha lo indica."),
        ("{F} ¿Desde dónde importaba Atenas parte de su trigo?", "Desde la costa del mar Negro", "La ficha lo indica."),
        ("=", "{F} ¿Cuántas monedas se ahorran al llevar 20 cargas por mar y no por tierra?", "(30-3)*20", "Se calcula el ahorro por carga y se multiplica por 20.", " monedas"),
        ("{F} ¿Qué rasgo de la ubicación de Roma ayudaba a defenderla?", "Estar entre colinas fáciles de defender", "La ficha describe el sitio de Roma entre colinas."),
        ("{F} Clasifica como oportunidad (O) o límite (L): 1) puertos naturales; 2) piratas; 3) islas como escalas; 4) temporales de invierno.", "1 O, 2 L, 3 O, 4 L", "Los puertos y las islas facilitan; los piratas y temporales dificultan."),
        ("{F} ¿Por qué las costas montañosas hacían más importante el transporte por mar?", "Porque los caminos por tierra eran difíciles y costosos", "Por mar era más barato llevar cargas."),
        ("{F} ¿Qué hizo Atenas para proteger sus rutas de trigo?", "Pactó alianzas", "La ficha lo indica."),
        ("{F} Mateo dice: «Como el mar era barato, todas las ciudades comerciaban igual». Corrígelo.", "Las decisiones políticas y las alianzas cambiaban lo que hacía cada ciudad, y los límites afectaban de manera distinta a cada una", "La geografía no decide por sí sola."),
        ("{F} Dos ciudades tienen un puerto similar. Una pacta alianzas y la otra cierra su puerto. ¿Qué muestra eso?", "Que la geografía permite posibilidades, pero las personas toman decisiones distintas", "Con las mismas condiciones, hay decisiones distintas."),
        ("{F} ¿Por qué depender del trigo importado podía ser un riesgo para Atenas?", "Porque si una ruta se cortaba por temporales, piratas o guerra, podía faltar el alimento", "Los límites de la ficha afectaban esa ruta."),
        ("{F} Una carga de 30 monedas por tierra es 10 veces más cara que la de 3 por mar. ¿Qué otra información falta para decir que el mar siempre convenía?", "Los riesgos y el tiempo del viaje, como temporales y piratas", "Un costo bajo puede venir con riesgos."),
        ("{F} Un compañero dice: «El mar vacío separaba a los pueblos». Refútalo con un dato de la ficha.", "Las rutas marítimas costaban menos y tenían puertos y escalas, así que conectaban a los pueblos", "El mar fue un camino de contacto."),
    ],
    ctx=("Una ciudad portuaria de la Antigüedad debe decidir si construye una flota para proteger sus barcos de los piratas o si envía las cargas por tierra. Usa la ficha para decir qué conviene considerar. {F}", "El costo (3 monedas por mar y 30 por tierra) y el riesgo de piratas", "Se compara ahorro con riesgo."),
    sc=[("¿Qué es una oportunidad geográfica? Da un ejemplo.", "Una condición del lugar que permite hacer algo útil, como puertos naturales que facilitan el comercio", "Es lo contrario de un límite."),
        ("¿Por qué la geografía no explica todo por sí sola?", "Porque los pueblos toman decisiones, como alianzas o guerras", "Las decisiones también influyen."),
        ("=", "{F} ¿Cuánto cuesta llevar 10 cargas por tierra?", "10*30", "Se multiplican las cargas por el costo de cada una.", " monedas")],
    op=("Escribe una explicación de 6 líneas: dos oportunidades y dos límites del Mediterráneo para el comercio, una decisión humana que cambió una situación y una frase final que evite decir que la geografía lo explica todo. {F}",
        "Oportunidades: puertos y costo bajo; límites: temporales y piratas; decisión: Atenas pactó alianzas.",
        ["dos oportunidades y dos límites", "una decisión humana", "frase final prudente"], ["explicación escrita"], ["mostrar solo ventajas", "decir que la geografía decidió todo"],
        "Pide que explique qué otra decisión pudo cambiar la situación."),
    reinforce="Nombra tres oportunidades y tres límites del mar para el comercio.",
    extend="Escribe una pregunta sobre cómo se repartían los costos de proteger una ruta marítima.",
)
