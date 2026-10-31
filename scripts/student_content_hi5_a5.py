"""Material del estudiante de 5.º básico, Historia, Geografía y Ciencias Sociales: OA 09 (zonas naturales de Chile) y OA 10 (recursos naturales y desarrollo sostenible)."""
from __future__ import annotations

from hi5_lib import build

OA9 = "HI05 OA 09"
OA10 = "HI05 OA 10"

# ================================================================ OA 09 · ZONAS NATURALES DE CHILE
# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (las cinco zonas, hecha para este cuaderno). De norte a sur, Chile se divide en cinco grandes zonas naturales. "
     "Norte Grande: desde Arica y Parinacota hasta Antofagasta; es un desierto. Norte Chico: las regiones de Atacama y Coquimbo; es una zona semiárida. "
     "Zona Central: desde Valparaíso hasta el Maule, donde está Santiago; tiene un valle fértil entre dos cordilleras. Zona Sur: desde el Biobío hasta Los Lagos; es lluviosa, con lagos, volcanes y bosques. "
     "Zona Austral: Aysén y Magallanes, en el extremo sur; es fría, con fiordos, canales, islas y glaciares.")
build(
    OA9, 1, F,
    use="Aprenderé a ubicar las cinco zonas naturales de Chile y sus regiones principales. Sirve para localizar cualquier lugar de Chile y entender cómo cambia el paisaje.",
    prior=["Sé que Chile es largo y angosto.", "Sé el orden norte, centro y sur.", "Sé que Chile tiene cordillera, valles, costa y mar."],
    explain=[
        "Chile es un país muy largo, así que su paisaje cambia mucho de norte a sur. Por eso se divide en cinco grandes zonas naturales. Una zona natural es un territorio con rasgos parecidos de clima, relieve y vegetación. De norte a sur son: Norte Grande, Norte Chico, Zona Central, Zona Sur y Zona Austral.",
        "El Norte Grande va desde Arica y Parinacota hasta Antofagasta y es un desierto. El Norte Chico comprende las regiones de Atacama y Coquimbo y es una zona semiárida. La Zona Central va desde Valparaíso hasta el Maule; allí está Santiago, la capital, en un valle fértil entre dos cordilleras.",
        "La Zona Sur va desde el Biobío hasta Los Lagos y es lluviosa, con lagos, volcanes y bosques. La Zona Austral, en el extremo sur, comprende Aysén y Magallanes; es fría, con fiordos, canales, islas y glaciares. Para ubicar una zona, decimos su nombre y su posición norte-sur.",
    ],
    vocab=[("zona natural", "territorio con rasgos parecidos de clima, relieve y vegetación"), ("desierto", "lugar donde llueve muy poco"), ("semiárido", "con poca lluvia, pero más que un desierto"), ("fiordo", "entrada de mar larga y angosta entre montañas"), ("glaciar", "gran masa de hielo que se mueve muy lento")],
    worked=[
        ("Ordenar las zonas", "{F} ¿Qué zona está más al norte y cuál más al sur?", ["Leo el orden de norte a sur.", "El Norte Grande es la primera y la Zona Austral la última."], "Norte Grande al norte; Zona Austral al sur"),
        ("Ubicar una ciudad", "{F} Santiago, ¿en qué zona está?", ["Busco Santiago en la ficha.", "Está en la Zona Central."], "En la Zona Central"),
    ],
    mistakes=[("Poner la Zona Austral al norte.", "Se confunde austral con el sentido contrario.", "Austral significa del sur: es la zona más al sur."),
              ("Creer que Santiago está en el Norte Chico.", "Se confunde la posición.", "Santiago está en la Zona Central.")],
    T=[
        ("{F} ¿Cuántas zonas naturales tiene Chile?", "cinco", "La ficha las enumera."),
        ("{F} ¿Qué zona es un desierto?", "el Norte Grande", "La ficha lo dice."),
        ("{F} ¿Qué zona está en el extremo sur?", "la Zona Austral", "La ficha lo dice."),
        ("{F} ¿En qué zona están las regiones de Atacama y Coquimbo?", "en el Norte Chico", "La ficha lo dice."),
        ("{F} ¿Qué rasgo tiene la Zona Sur: es lluviosa o seca?", "lluviosa", "La ficha lo dice."),
        ("{F} ¿Entre qué dos regiones va la Zona Central?", "desde Valparaíso hasta el Maule", "La ficha lo dice."),
        ("Ordena de norte a sur: Zona Sur, Norte Chico, Zona Austral, Norte Grande, Zona Central.", "Norte Grande, Norte Chico, Zona Central, Zona Sur, Zona Austral", "Así es el orden en Chile."),
        ("{F} Une cada zona con un rasgo: 1) Zona Austral; 2) Zona Central. a) valle fértil entre dos cordilleras; b) fiordos y glaciares.", "1 con b; 2 con a", "La ficha asigna esos rasgos."),
        ("{F} Un mapa muestra lagos y volcanes con bosques. ¿De qué zona podría ser?", "de la Zona Sur", "La ficha describe la Zona Sur así."),
        ("{F} Pedro dice: «Chile tiene tres zonas». ¿Qué corrección haces?", "tiene cinco: Norte Grande, Norte Chico, Zona Central, Zona Sur y Zona Austral", "La ficha da cinco."),
        ("{F} Ana dice: «Antofagasta está en la Zona Sur». ¿Qué dato la corrige?", "el Norte Grande llega hasta Antofagasta", "Está en el norte."),
        ("{F} Clasifica como zona «del norte» o «del sur»: a) Norte Chico; b) Zona Austral; c) Norte Grande; d) Zona Sur.", "del norte: a y c; del sur: b y d", "Por su posición en el país."),
        ("{F} ¿Por qué se divide Chile en zonas?", "porque es muy largo y su paisaje cambia de norte a sur", "La ficha lo explica."),
    ],
    ctx=("En un mapa escolar ves una foto de un glaciar con la palabra «Magallanes». ¿De qué zona es?", "de la Zona Austral", "Magallanes está en la Zona Austral."),
    sc=[("{F} ¿Qué es una zona natural?", "un territorio con rasgos parecidos de clima, relieve y vegetación", "Así se define."),
        ("{F} ¿En qué zona está Santiago?", "en la Zona Central", "La ficha lo dice."),
        ("¿Qué significa austral?", "del sur", "Por eso la Zona Austral está en el extremo sur.")],
    op=("Dibuja un rectángulo largo y angosto que represente a Chile, con el norte arriba. Divídelo en cinco partes y escribe en cada una el nombre de la zona y un rasgo de la ficha. {F}",
        "De arriba abajo: Norte Grande (desierto), Norte Chico (semiárido), Zona Central (valle fértil), Zona Sur (lluviosa), Zona Austral (fría, glaciares).",
        ["cinco zonas en orden", "un rasgo por zona", "orientación norte-sur correcta"], ["rectángulo dividido"], ["poner la Zona Austral arriba", "dejar zonas sin rasgo"],
        "Pregunta cómo cambia el paisaje de arriba hacia abajo."),
    reinforce="Nombra de memoria las cinco zonas de norte a sur con un rasgo cada una.",
    extend="Escribe en qué zona vives y compárala con la zona de otra ciudad que conozcas.",
)

# ---------------------------------------------------------------- clase 2
F = ("Fuentes sobre las zonas (hechas para este cuaderno; los números son valores de ejemplo, no oficiales). Fuente A: un climograma de la Ciudad ejemplo 1: lluvia total del año, 2 mm; temperatura media, 18 °C. "
     "Fuente B: un climograma de la Ciudad ejemplo 2: lluvia total del año, 350 mm, casi toda en invierno; temperatura media, 14 °C. "
     "Fuente C: un climograma de la Ciudad ejemplo 3: lluvia total del año, 1.300 mm, repartida en todo el año; temperatura media, 10 °C. "
     "Fuente D: un folleto de una agencia de turismo que dice: «El sur de Chile es el paraíso perfecto, sin ningún problema».")
build(
    OA9, 2, F,
    use="Aprenderé a leer climogramas y textos para saber de qué zona hablan y a preguntar quién los hizo. Sirve para caracterizar el clima de una zona con evidencia.",
    prior=["Sé las cinco zonas.", "Sé que la temperatura se mide en grados Celsius y la lluvia en milímetros (mm)."],
    explain=[
        "El clima describe cómo son la temperatura y las lluvias de un lugar a lo largo del año. Un climograma es un gráfico o tabla que muestra la temperatura y la lluvia. Leerlo permite saber si el lugar es muy seco, de lluvias en invierno o muy lluvioso.",
        "En el Norte Grande llueve muy poco, a veces casi nada. En el Norte Chico llueve poco, sobre todo en invierno. En la Zona Central hay inviernos con lluvias y veranos secos. En la Zona Sur llueve mucho y casi todo el año. En la Zona Austral hace frío y hay lluvia o nieve según el lugar.",
        "Una fuente siempre tiene procedencia. Un climograma lo hace un organismo que mide el clima. Un folleto turístico quiere atraer visitantes, y por eso muestra solo lo bueno. Decir «sin ningún problema» es una opinión, no un dato. Para caracterizar una zona usamos datos y revisamos quién los entrega.",
    ],
    vocab=[("clima", "cómo son la temperatura y la lluvia de un lugar durante el año"), ("climograma", "gráfico o tabla de la temperatura y la lluvia de un lugar"), ("precipitación", "agua que cae del cielo como lluvia, nieve o granizo"), ("temperatura media", "promedio de las temperaturas del año"), ("milímetro (mm)", "unidad con que se mide la lluvia caída")],
    worked=[
        ("Leer un climograma", "{F} ¿Qué clima muestra la fuente A?", ["Veo que llueve 2 mm al año, casi nada.", "Es un clima desértico, como el del Norte Grande."], "Un clima muy seco, de desierto"),
        ("Reconocer una opinión", "{F} ¿La frase del folleto «sin ningún problema» es un dato o una opinión?", ["Pregunto si se puede medir.", "No se puede medir; es una valoración."], "Una opinión"),
    ],
    mistakes=[("Creer que un folleto turístico es una fuente neutral.", "No se revisa la procedencia.", "Pregunta quién lo hizo y para qué."),
              ("Confundir lluvia total con temperatura.", "Se mezclan las unidades.", "La lluvia se mide en mm y la temperatura en °C.")],
    T=[
        ("{F} ¿Cuántos milímetros de lluvia al año tiene la ciudad ejemplo 1?", "2 mm", "La fuente A lo dice."),
        ("{F} ¿En qué estación cae casi toda la lluvia de la ciudad ejemplo 2?", "en invierno", "La fuente B lo dice."),
        ("{F} ¿Qué ciudad ejemplo tiene más lluvia?", "la ciudad ejemplo 3", "Tiene 1.300 mm."),
        ("{F} ¿Qué fuente es un folleto de turismo?", "la fuente D", "La ficha lo dice."),
        ("=", "{F} ¿Cuántos mm más llueve en la ciudad ejemplo 3 que en la ejemplo 2?", "1300-350", "Se resta la lluvia menor a la mayor.", " mm"),
        ("{F} ¿Qué ciudad ejemplo es la más fría?", "la ciudad ejemplo 3", "Tiene 10 °C de temperatura media."),
        ("{F} La fuente A, ¿corresponde mejor a una ciudad del Norte Grande o de la Zona Sur?", "del Norte Grande", "Llueve casi nada, como en el desierto."),
        ("{F} La fuente C, ¿corresponde mejor a una ciudad de la Zona Sur o del Norte Chico?", "de la Zona Sur", "Llueve mucho todo el año."),
        ("{F} La fuente B, con lluvias de invierno y veranos secos, ¿corresponde mejor a la Zona Central o a la Zona Austral?", "a la Zona Central", "Es el clima típico de esa zona."),
        ("{F} Luis dice: «El folleto prueba que el sur no tiene problemas». ¿Qué respuesta le das?", "es una opinión de una agencia que quiere atraer visitantes", "Un folleto no es una fuente neutral."),
        ("{F} Ana dice: «Como la ciudad ejemplo 1 llueve 2 mm, todo Chile es seco». ¿Qué corrección haces?", "una ciudad no representa todo el país; la ciudad ejemplo 3 llueve mucho", "Las zonas son distintas."),
        ("{F} Elige la pregunta que los climogramas no responden. A) ¿Cuánto llueve al año en cada ciudad? B) ¿Cuántas personas viven en cada ciudad?", "B", "Los climogramas no entregan población."),
        ("{F} Para comparar clima seco y clima muy lluvioso, ¿qué dos fuentes enfrentas?", "la fuente A con la fuente C", "Una tiene 2 mm y la otra 1.300 mm."),
    ],
    ctx=("Un compañero te muestra un climograma de una ciudad con 700 mm de lluvia en el invierno y casi 0 en el verano. ¿A qué zona se parece más y por qué?", "a la Zona Central, porque tiene inviernos lluviosos y veranos secos", "Es el clima típico de esa zona."),
    sc=[("¿Qué es un climograma?", "un gráfico o tabla de la temperatura y la lluvia de un lugar", "Así se define."),
        ("¿En qué unidad se mide la lluvia?", "en milímetros (mm)", "Así se mide la precipitación."),
        ("{F} ¿Por qué hay que cuidarse de un folleto turístico?", "porque quiere atraer visitantes y muestra solo lo bueno", "Su propósito es promocional.")],
    op=("Haz una tabla con las fuentes A, B y C y las columnas «lluvia al año», «temperatura media», «zona a la que se parece» y «razón». Usa solo los valores de la ficha. {F}",
        "A: 2 mm, 18 °C, Norte Grande, casi no llueve. B: 350 mm, 14 °C, Zona Central o Norte Chico, lluvia de invierno. C: 1.300 mm, 10 °C, Zona Sur, llueve mucho.",
        ["tres filas completas", "zona coherente con los datos", "razón con un dato"], ["tabla de cuatro columnas"], ["mezclar lluvia con temperatura", "usar el folleto como dato"],
        "Pregunta por qué los datos de una sola ciudad no describen toda la zona."),
    reinforce="Di en voz alta qué clima muestra cada fuente y de qué zona podría ser.",
    extend="Anota la lluvia que cae en tu ciudad en un año cualquiera si la conoces, y compárala con las fuentes de la ficha.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (relaciones entre rasgos, hecha para este cuaderno). Relieve: la cordillera de los Andes recorre todo Chile por el este. Norte Grande: clima desértico, casi sin lluvia; hay pocos ríos, como el Loa; la gente vive en la costa y en oasis; hay minas de cobre y salares con litio. "
     "Norte Chico: clima semiárido; los ríos corren por valles que van de la cordillera al mar; en los valles hay agricultura, como uva y frutas; hay minería. "
     "Zona Central: clima de inviernos con lluvia y veranos secos; ríos como el Maipo y el Maule; valle fértil; vive allí la mayor parte de la población de Chile; hay agricultura, industria y minería. "
     "Zona Sur: clima lluvioso; muchos ríos y lagos; bosques; ganadería, forestal y pesca; ciudades como Concepción, Temuco y Puerto Montt. "
     "Zona Austral: clima frío; fiordos, glaciares y canales; muy poca población; ganadería de ovejas, pesca y turismo.")
build(
    OA9, 3, F,
    use="Aprenderé a relacionar el clima, el relieve, el agua, la población y los recursos de cada zona. Sirve para explicar por qué las personas viven y trabajan donde lo hacen.",
    prior=["Sé las cinco zonas y su clima.", "Sé qué es un recurso natural."],
    explain=[
        "Los rasgos de una zona se relacionan entre sí. En todas las zonas, la cordillera de los Andes recorre el país por el este. Donde el clima es desértico, hay pocos ríos y poca gente. En el Norte Grande la gente vive en la costa y en oasis, que son lugares con agua. Allí hay minas de cobre y salares con litio.",
        "En el Norte Chico los ríos corren por valles que van de la cordillera al mar y permiten agricultura, como uva y frutas. En la Zona Central, el clima de inviernos con lluvia y veranos secos y un valle fértil explican que viva allí la mayor parte de la población y que haya agricultura e industria.",
        "En la Zona Sur, la lluvia abundante da origen a ríos, lagos y bosques, y a la ganadería, la actividad forestal y la pesca. En la Zona Austral, el frío, los fiordos y los glaciares hacen que haya muy poca población, con ganadería de ovejas, pesca y turismo. Siempre buscamos la causa: el rasgo natural, y la consecuencia: lo que hace la gente.",
    ],
    vocab=[("oasis", "lugar de un desierto donde hay agua y se puede vivir y cultivar"), ("valle", "zona baja entre montañas, por donde suele correr un río"), ("salar", "terreno cubierto de sal en un desierto"), ("actividad forestal", "trabajo con los bosques para obtener madera"), ("ganadería", "crianza de animales para obtener carne, leche o lana")],
    worked=[
        ("Relacionar clima y población", "{F} ¿Por qué la gente del Norte Grande vive en la costa y en oasis?", ["Busco el rasgo natural: clima desértico y pocos ríos.", "En esos lugares hay agua."], "Porque ahí hay agua y el resto es desierto"),
        ("Relacionar clima y actividad", "{F} ¿Qué rasgo natural permite la agricultura en el Norte Chico?", ["Reviso la ficha.", "Los ríos que corren por los valles."], "Los ríos que corren por los valles"),
    ],
    mistakes=[("Decir que la población se reparte igual en todas las zonas.", "No se mira el clima ni el agua.", "La mayor parte vive en la Zona Central y muy poca en la Austral."),
              ("Creer que el desierto no tiene recursos.", "Se piensa que sin agua no hay riqueza.", "Hay cobre y litio en el Norte Grande.")],
    T=[
        ("{F} ¿Qué río nombra la ficha en el Norte Grande?", "el Loa", "La ficha lo dice."),
        ("{F} ¿Qué mineral hay en los salares del Norte Grande?", "litio", "La ficha lo dice."),
        ("{F} ¿Qué zona tiene la mayor parte de la población de Chile?", "la Zona Central", "La ficha lo dice."),
        ("{F} ¿Qué zona tiene muy poca población?", "la Zona Austral", "La ficha lo dice."),
        ("{F} ¿Qué se cultiva en los valles del Norte Chico?", "uva y frutas", "La ficha lo dice."),
        ("{F} ¿Qué cordillera recorre todo Chile por el este?", "la cordillera de los Andes", "La ficha lo dice."),
        ("{F} Une cada rasgo con su consecuencia: 1) lluvia abundante en el sur; 2) clima desértico en el norte. a) pocos ríos y poca gente; b) ríos, lagos y bosques.", "1 con b; 2 con a", "La ficha enlaza cada rasgo con su efecto."),
        ("{F} Clasifica como «agua» o «mineral»: a) río Maipo; b) cobre; c) lago; d) litio.", "agua: a y c; mineral: b y d", "Los ríos y lagos son agua; el cobre y el litio son minerales."),
        ("{F} ¿Qué actividad económica se relaciona con los bosques de la Zona Sur?", "la actividad forestal", "La ficha lo dice."),
        ("{F} Pedro dice: «La Zona Austral tiene muchísima población porque es hermosa». ¿Qué corrección haces?", "tiene muy poca población por su clima frío, sus fiordos y sus glaciares", "La ficha lo dice."),
        ("{F} Ana dice: «En el desierto no hay actividad económica». ¿Qué dato la contradice?", "hay minas de cobre y salares con litio", "La ficha nombra esa minería."),
        ("{F} Explica por qué la Zona Central tiene tanta población.", "porque tiene valle fértil, clima favorable, agricultura e industria", "La ficha enlaza esos rasgos."),
        ("{F} Ordena una cadena: a) se desarrolla la agricultura; b) los ríos riegan los valles; c) hay frutas y uva.", "b, a, c", "El agua permite la agricultura y esta da los productos."),
    ],
    ctx=("Una compañera dice que su familia se mudó a una zona con lagos, bosques y mucha lluvia para trabajar en la actividad forestal. ¿A qué zona se mudó?", "a la Zona Sur", "La ficha describe esos rasgos en la Zona Sur."),
    sc=[("¿Qué es un oasis?", "un lugar de un desierto donde hay agua y se puede vivir y cultivar", "Así se define."),
        ("{F} ¿Qué actividad se hace en la Zona Austral además de la pesca y el turismo?", "ganadería de ovejas", "La ficha lo dice."),
        ("¿Qué relación hay entre el clima y la población?", "que donde el clima es más favorable suele vivir más gente", "El clima y el agua influyen en dónde se vive.")],
    op=("Dibuja un cuadro de cinco filas, una por zona, con las columnas «clima», «agua», «población» y «actividades». Completa cada casilla con una palabra o frase de la ficha. {F}",
        "Norte Grande: desértico; pocos ríos; costa y oasis; minería. Zona Sur: lluvioso; ríos y lagos; ciudades como Temuco; forestal y pesca.",
        ["cinco filas", "cuatro columnas completas", "datos de la ficha"], ["cuadro completo"], ["inventar datos", "mezclar zonas"],
        "Pregunta qué zona le parece más fácil para vivir y por qué."),
    reinforce="Explica en voz alta cómo el clima influye en las actividades en dos zonas.",
    extend="Escribe una relación entre clima, agua y actividad económica en tu región, si la conoces.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (comparación de zonas, hecha para este cuaderno). Norte Grande: desierto, muy seco, minería, población en costa y oasis. "
     "Zona Sur: lluviosa, con ríos, lagos, bosques y volcanes, agricultura, ganadería y forestal, ciudades medianas. "
     "Zona Central: clima de inviernos con lluvia y veranos secos, valle fértil, la mayor población y las ciudades más grandes. "
     "Zona Austral: muy fría, con glaciares y fiordos, poca población. "
     "Perspectivas: una persona del Norte Grande valora cada gota de agua; una persona de la Zona Sur valora el bosque y los lagos; una persona de la Zona Austral valora los glaciares y la naturaleza casi intacta.")
build(
    OA9, 4, F,
    use="Aprenderé a comparar zonas de Chile con criterios y a ver cómo las personas valoran distinto cada paisaje. Sirve para explicar semejanzas y diferencias entre territorios.",
    prior=["Sé las características de cada zona.", "Sé comparar con criterios."],
    explain=[
        "Comparar zonas es mirar los mismos criterios en dos lugares. Podemos comparar clima, agua, población y actividades. El Norte Grande es seco y desértico; la Zona Sur es lluviosa, con ríos, lagos y bosques. La Zona Central tiene la mayor población y las ciudades más grandes; la Zona Austral tiene poca población.",
        "También hay semejanzas. Por ejemplo, el Norte Grande y la Zona Sur tienen actividades importantes ligadas a sus recursos: minería en el norte y actividad forestal en el sur. Al comparar siempre decimos en qué criterio se parecen o se diferencian.",
        "Cada persona valora de manera distinta su paisaje. Una persona del Norte Grande valora cada gota de agua. Una de la Zona Sur valora el bosque y los lagos. Una de la Zona Austral valora los glaciares y la naturaleza casi intacta. La perspectiva depende del lugar donde se vive.",
    ],
    vocab=[("criterio", "aspecto que se usa para comparar"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas se distinguen"), ("perspectiva", "punto de vista de una persona o grupo"), ("naturaleza casi intacta", "naturaleza poco modificada por las personas")],
    worked=[
        ("Comparar con un criterio", "{F} Compara el agua del Norte Grande y de la Zona Sur.", ["En el Norte Grande es muy escasa.", "En la Zona Sur hay ríos y lagos."], "El Norte Grande tiene muy poca agua y la Zona Sur mucha"),
        ("Comparar perspectivas", "{F} ¿Qué valora una persona del Norte Grande?", ["Busco la perspectiva en la ficha.", "Cada gota de agua."], "Cada gota de agua"),
    ],
    mistakes=[("Comparar sin criterio claro.", "Se mezclan temas.", "Elige un criterio: clima, agua, población o actividades."),
              ("Creer que una zona es mejor que otra.", "Se confunde comparar con juzgar.", "Cada zona tiene ventajas y dificultades.")],
    T=[
        ("{F} ¿Qué zona es muy seca?", "el Norte Grande", "La ficha lo dice."),
        ("{F} ¿Qué zona tiene la mayor población?", "la Zona Central", "La ficha lo dice."),
        ("{F} ¿Qué zona tiene glaciares y fiordos?", "la Zona Austral", "La ficha lo dice."),
        ("{F} ¿Qué zona tiene ríos, lagos, bosques y volcanes?", "la Zona Sur", "La ficha lo dice."),
        ("{F} ¿Qué valora una persona de la Zona Sur?", "el bosque y los lagos", "La ficha lo dice."),
        ("{F} ¿Qué valora una persona de la Zona Austral?", "los glaciares y la naturaleza casi intacta", "La ficha lo dice."),
        ("{F} Clasifica como «Norte Grande» o «Zona Sur»: a) desierto; b) bosques; c) minería; d) lluvia abundante.", "Norte Grande: a y c; Zona Sur: b y d", "La ficha asigna cada rasgo."),
        ("{F} Elige la comparación correcta de población. A) La Zona Central tiene más población que la Zona Austral. B) La Zona Austral tiene más población que la Zona Central.", "A", "La ficha lo dice."),
        ("{F} Nombra dos criterios de la ficha para comparar la Zona Central con la Zona Austral.", "por ejemplo clima y población", "La ficha da datos de clima y de población de ambas."),
        ("{F} Pedro dice: «El Norte Grande y la Zona Sur son iguales». Da una diferencia.", "el Norte Grande es muy seco y la Zona Sur muy lluviosa", "Es una diferencia de clima."),
        ("{F} Ana dice: «La Zona Austral es mala porque tiene poca gente». ¿Qué respuesta le das?", "cada zona tiene valores distintos, como los glaciares y la naturaleza casi intacta", "Comparar no es juzgar."),
        ("{F} ¿Qué semejanza tienen el Norte Grande y la Zona Sur?", "ambas tienen actividades ligadas a sus recursos", "La clase lo explica."),
        ("{F} ¿Por qué distintas personas valoran distinto su paisaje?", "porque viven en lugares con rasgos distintos y necesitan cosas distintas", "La perspectiva depende del lugar."),
    ],
    ctx=("Una compañera del Norte Grande y uno de la Zona Sur conversan por video. Ella dice que cuida el agua; él, que cuida el bosque. ¿Qué perspectiva muestra cada uno?", "ella, la del agua escasa; él, la del bosque y los lagos", "Cada uno valora lo que hay en su zona."),
    sc=[("¿Qué es comparar con criterios?", "mirar el mismo aspecto en dos lugares para ver semejanzas y diferencias", "Así se define."),
        ("{F} ¿Qué zona tiene las ciudades más grandes?", "la Zona Central", "La ficha lo dice."),
        ("Nombra dos criterios para comparar zonas.", "por ejemplo clima y población", "Son criterios de la clase.")],
    op=("Elige dos zonas y haz una tabla de comparación con cuatro criterios: clima, agua, población y actividades. Escribe una semejanza, una diferencia y una frase con la perspectiva de una persona que vive en cada zona. {F}",
        "Norte Grande y Zona Sur. Clima: desértico / lluvioso. Agua: escasa / abundante. Una semejanza: ambas viven de sus recursos. Una diferencia: la cantidad de lluvia.",
        ["dos zonas", "cuatro criterios", "semejanza y diferencia", "dos perspectivas"], ["tabla", "dos frases"], ["comparar sin criterio", "inventar datos"],
        "Pregunta qué zona le gustaría visitar y qué le llamó la atención."),
    reinforce="Compara en voz alta dos zonas con dos criterios.",
    extend="Escribe una pregunta que te gustaría hacer a una persona que vive en otra zona de Chile.",
)

# ================================================================ OA 10 · RECURSOS NATURALES Y DESARROLLO SOSTENIBLE
# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (recursos naturales de Chile, hecha para este cuaderno). Un recurso natural es algo de la naturaleza que las personas usan. "
     "Cobre: se extrae en minas del Norte Grande, como Chuquicamata y Escondida, y también en El Teniente, en la Zona Central. Hierro: hay minas en las regiones de Atacama y Coquimbo, en el Norte Chico. "
     "Recursos marítimos: peces, mariscos y algas, a lo largo de toda la costa; el salmón se cría en el sur. Recursos forestales: bosques de pino y eucalipto, sobre todo en la Zona Sur. "
     "Litio: se obtiene de los salares del Norte Grande. Sol: el Norte Grande recibe mucho sol y se usa para producir energía.")
build(
    OA10, 1, F,
    use="Aprenderé a reconocer y ubicar en un mapa los recursos naturales importantes de Chile. Sirve para saber qué recurso hay en cada zona.",
    prior=["Sé las cinco zonas de Chile.", "Sé leer un mapa simple."],
    explain=[
        "Un recurso natural es algo de la naturaleza que las personas usan para vivir o producir. Chile tiene muchos. El cobre se extrae en minas del Norte Grande, como Chuquicamata y Escondida, y también en El Teniente, en la Zona Central. El hierro se encuentra en minas de Atacama y Coquimbo, en el Norte Chico.",
        "Los recursos marítimos son peces, mariscos y algas, que se encuentran a lo largo de toda la costa; el salmón se cría en el sur. Los recursos forestales, como el pino y el eucalipto, se encuentran sobre todo en la Zona Sur. El litio se obtiene de los salares del Norte Grande.",
        "El sol también es un recurso: el Norte Grande recibe mucho y se usa para producir energía. Para ubicar un recurso en un mapa, decimos qué es y en qué zona está. Así vemos que no todos los recursos están en todas partes.",
    ],
    vocab=[("recurso natural", "algo de la naturaleza que las personas usan"), ("mina", "lugar de donde se saca un mineral"), ("recurso marítimo", "recurso que viene del mar, como peces o algas"), ("recurso forestal", "recurso que viene del bosque, como la madera"), ("litio", "metal liviano que se usa en baterías")],
    worked=[
        ("Ubicar un recurso", "{F} ¿En qué zona está la mina de Escondida?", ["Busco Escondida en la ficha.", "Está en el Norte Grande."], "En el Norte Grande"),
        ("Clasificar un recurso", "{F} El pino y el eucalipto, ¿qué tipo de recurso son?", ["Vienen de bosques.", "Son recursos forestales."], "Recursos forestales"),
    ],
    mistakes=[("Pensar que todos los recursos están en todas las zonas.", "No se mira el mapa.", "Cada recurso se encuentra en ciertas zonas."),
              ("Ubicar el hierro en el sur.", "Se mezclan recursos.", "El hierro está en el Norte Chico.")],
    T=[
        ("{F} ¿Dónde se extrae el cobre de Chuquicamata?", "en el Norte Grande", "La ficha lo dice."),
        ("{F} ¿Qué recurso se obtiene de los salares?", "litio", "La ficha lo dice."),
        ("{F} ¿En qué zona se cría el salmón?", "en el sur", "La ficha lo dice."),
        ("{F} ¿En qué zona hay minas de hierro?", "en el Norte Chico", "La ficha lo dice."),
        ("{F} ¿En qué zona está la mina El Teniente?", "en la Zona Central", "La ficha lo dice."),
        ("{F} ¿Para qué se usa el sol en el Norte Grande?", "para producir energía", "La ficha lo dice."),
        ("{F} Clasifica como «minero», «marítimo» o «forestal»: a) cobre; b) algas; c) pino.", "minero: a; marítimo: b; forestal: c", "Cada uno corresponde a ese tipo."),
        ("{F} Une cada recurso con su zona: 1) hierro; 2) bosques de pino y eucalipto. a) Zona Sur; b) Norte Chico.", "1 con b; 2 con a", "La ficha los ubica."),
        ("{F} Un mapa muestra bosques de pino en el desierto de Atacama. ¿Es correcto?", "No, esos bosques están sobre todo en la Zona Sur", "El desierto no tiene bosques de pino."),
        ("{F} Pedro dice: «El cobre solo está en el sur». Corrígelo.", "se extrae en el Norte Grande y en la Zona Central", "La ficha lo dice."),
        ("{F} Ana dice: «El mar no es un recurso». ¿Qué dato la contradice?", "peces, mariscos y algas son recursos marítimos", "La ficha los nombra."),
        ("{F} Ordena de norte a sur estos recursos: bosques de pino, litio de salares, minas de hierro.", "litio de salares, minas de hierro, bosques de pino", "Los salares están en el Norte Grande, el hierro en el Norte Chico y los bosques en el sur."),
        ("{F} ¿Por qué es útil ubicar recursos en un mapa?", "para saber dónde están y qué actividades se hacen en cada zona", "El mapa relaciona recurso y lugar."),
    ],
    ctx=("En una exposición sobre minería hay un cartel que dice «Cobre». ¿En qué zonas de Chile se extrae ese recurso, según la ficha?", "en el Norte Grande y en la Zona Central", "La ficha nombra esas zonas."),
    sc=[("¿Qué es un recurso natural?", "algo de la naturaleza que las personas usan", "Así se define."),
        ("{F} Nombra un recurso marítimo.", "por ejemplo peces, mariscos o algas", "La ficha los nombra."),
        ("{F} ¿Qué recurso se usa en baterías y se saca de salares?", "el litio", "La ficha lo dice.")],
    op=("Dibuja un mapa simple de Chile dividido en cinco zonas. Marca con un símbolo cuatro recursos de la ficha donde corresponden: cobre, hierro, bosques de pino y salares. Haz una leyenda con los símbolos. {F}",
        "Cobre en Norte Grande y Zona Central; hierro en Norte Chico; bosques en Zona Sur; salares en Norte Grande.",
        ["cuatro recursos", "ubicación correcta", "leyenda"], ["mapa con leyenda"], ["poner los bosques en el desierto", "olvidar la leyenda"],
        "Pregunta qué zona tiene más recursos distintos."),
    reinforce="Nombra cuatro recursos de Chile con su zona.",
    extend="Escribe un recurso natural que se use en tu casa y de dónde viene, si lo sabes.",
)

# ---------------------------------------------------------------- clase 2
F = ("Fuentes sobre los recursos (hechas para este cuaderno; las cifras son valores de ejemplo). Fuente A: una tabla de un organismo público con la pesca de una especie, en toneladas: año 1, 100; año 2, 90; año 3, 70; año 4, 50. "
     "Fuente B: un aviso de una empresa minera que dice: «Extraemos cobre de manera responsable y sin ningún daño». "
     "Fuente C: un informe de un organismo público que explica que se prohibió pescar esa especie durante unos meses al año, llamado veda, para que se reproduzca. "
     "Fuente D: la carta de una comunidad cercana a una mina que pide que se cuide el agua del río.")
build(
    OA10, 2, F,
    use="Aprenderé a leer tablas y textos sobre recursos y a preguntar quién los hizo y para qué. Sirve para distinguir datos de opiniones y entender distintos intereses.",
    prior=["Sé qué son los recursos naturales.", "Sé qué es la procedencia de una fuente."],
    explain=[
        "Para estudiar los recursos naturales usamos fuentes. Una tabla de un organismo público entrega datos medibles, como cuántas toneladas se pescan cada año. Una tonelada es una medida de peso igual a mil kilos. Mirando los números vemos si el recurso aumenta o disminuye.",
        "Un aviso de una empresa minera busca mostrar una buena imagen. Decir «sin ningún daño» es una afirmación sin prueba. Un informe público sobre una veda explica una medida: prohibir pescar durante unos meses para que la especie se reproduzca. La carta de una comunidad entrega la mirada de las personas que viven cerca de la mina y piden cuidar el agua.",
        "Cada fuente tiene intereses. Un aviso quiere vender una imagen, un informe público explica una norma y una comunidad defiende su entorno. Para entender bien un tema comparamos fuentes y distinguimos los datos de las opiniones.",
    ],
    vocab=[("tonelada", "medida de peso igual a mil kilos"), ("veda", "prohibición de pescar o cazar durante un tiempo para que la especie se reproduzca"), ("organismo público", "institución del Estado"), ("interés", "lo que un grupo quiere lograr"), ("dato", "información que se puede medir o comprobar")],
    worked=[
        ("Leer una tabla", "{F} ¿Qué pasó con la pesca entre el año 1 y el año 4?", ["Veo 100 y luego 50.", "Bajó."], "Disminuyó de 100 a 50 toneladas"),
        ("Distinguir dato y opinión", "{F} ¿«Sin ningún daño» es un dato o una opinión?", ["Pregunto si hay una prueba.", "No hay ninguna medida."], "Una afirmación sin prueba, más cerca de una opinión"),
    ],
    mistakes=[("Creer que un aviso es una fuente neutral.", "No se revisa quién lo hizo.", "Pregunta quién lo hizo y qué gana."),
              ("Leer una tabla sin mirar la tendencia.", "Se mira un solo número.", "Compara el primer y el último año.")],
    T=[
        ("{F} ¿Cuántas toneladas se pescaron en el año 1?", "100", "La tabla lo dice."),
        ("{F} ¿Cuántas toneladas se pescaron en el año 4?", "50", "La tabla lo dice."),
        ("{F} ¿Qué es una veda?", "una prohibición temporal de pescar para que la especie se reproduzca", "La ficha lo explica."),
        ("=", "{F} ¿Cuántas toneladas menos se pescaron en el año 4 que en el año 1?", "100-50", "Se resta la cifra menor a la mayor.", " toneladas"),
        ("{F} ¿Qué fuente es una carta de una comunidad?", "la fuente D", "La ficha lo dice."),
        ("{F} ¿Qué pide la comunidad de la fuente D?", "que se cuide el agua del río", "La ficha lo dice."),
        ("{F} ¿Quién hizo el aviso de la fuente B?", "una empresa minera", "La ficha lo dice."),
        ("{F} ¿La tabla muestra aumento o disminución de la pesca?", "disminución", "Los números bajan año a año."),
        ("=", "{F} ¿Cuántas toneladas se pescaron en total entre el año 2 y el año 3?", "90+70", "Se suman las dos cifras.", " toneladas"),
        ("{F} Luis dice: «El aviso prueba que la minería no daña». ¿Qué respuesta le das?", "es un aviso de la empresa, sin pruebas, y quiere mostrar una buena imagen", "Un aviso tiene interés propio."),
        ("{F} Ana dice: «La tabla prueba que la especie desapareció». ¿Qué corrección haces?", "solo muestra que la pesca disminuyó, no que desapareció", "No se debe afirmar más de lo que muestra."),
        ("{F} Elige la pregunta que las fuentes no responden. A) ¿Qué pidió la comunidad? B) ¿Cuántas personas viven cerca de la mina?", "B", "Ninguna fuente da esa cifra."),
        ("{F} Para entender por qué se hizo una veda, ¿qué dos fuentes unes?", "la fuente A con la fuente C", "A muestra la baja y C explica la medida."),
    ],
    ctx=("Un diario escolar publica: «La empresa X dice que no daña el río». ¿Qué pregunta de procedencia debes hacer antes de creerle?", "quién lo dice, con qué pruebas y qué le conviene", "La empresa tiene interés."),
    sc=[("En Historia y Geografía, ¿qué diferencia a un dato de una opinión?", "el dato se puede medir o comprobar y la opinión no", "Así se distingue la información de una valoración."),
        ("{F} ¿Qué fuente entrega datos medibles: la A o la B?", "la fuente A", "La tabla tiene cifras."),
        ("¿Por qué comparar fuentes de distintos intereses?", "porque cada una muestra una parte distinta del problema", "Así se entiende mejor.")],
    op=("Haz una tabla con las fuentes A, B, C y D. En las columnas escribe «quién habla», «qué quiere» y «dato u opinión». {F}",
        "A: organismo público; informar; dato. B: empresa minera; mostrar buena imagen; opinión sin prueba. C: organismo público; explicar la veda; dato. D: comunidad; cuidar el agua; opinión y petición.",
        ["cuatro filas completas", "interés identificado", "dato u opinión bien clasificado"], ["tabla de tres columnas"], ["creer que el aviso es neutral", "confundir dato con opinión"],
        "Pregunta cuál fuente le sirve más para saber si una especie está disminuyendo."),
    reinforce="Nombra las cuatro fuentes y di cuál es dato y cuál opinión.",
    extend="Escribe una pregunta que te gustaría hacer a una empresa y otra a una comunidad sobre el uso del agua.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (renovables y no renovables, hecha para este cuaderno). Un recurso renovable puede volver a formarse o reproducirse si se usa con cuidado: los peces, los bosques, el agua dulce de los ríos, el sol y el viento. "
     "Un recurso no renovable no se repone en un tiempo útil para las personas: el cobre, el hierro, el litio, el petróleo y el carbón. "
     "Si se pesca demasiado, los peces disminuyen; si se corta un bosque sin plantar árboles nuevos, el bosque desaparece. Por eso existen la veda, las cuotas de pesca y la reforestación, que es plantar árboles. "
     "El desarrollo sostenible significa satisfacer las necesidades de hoy sin quitarles a las futuras generaciones la posibilidad de satisfacer las suyas.")
build(
    OA10, 3, F,
    use="Aprenderé la diferencia entre recursos renovables y no renovables y por qué hay que cuidarlos. Sirve para explicar qué es el desarrollo sostenible.",
    prior=["Sé qué recursos tiene Chile y dónde están.", "Sé qué es una causa y una consecuencia."],
    explain=[
        "Un recurso renovable puede volver a formarse o reproducirse si se usa con cuidado. Son renovables los peces, los bosques, el agua dulce de los ríos, el sol y el viento. Un recurso no renovable no se repone en un tiempo útil para las personas. Son no renovables el cobre, el hierro, el litio, el petróleo y el carbón.",
        "Un recurso renovable también puede agotarse si se usa mal. Si se pesca demasiado, los peces disminuyen. Si se corta un bosque sin plantar árboles nuevos, el bosque desaparece. Por eso hay medidas de cuidado: la veda, las cuotas de pesca, que limitan cuánto se puede pescar, y la reforestación, que es plantar árboles.",
        "El desarrollo sostenible significa satisfacer las necesidades de hoy sin quitarles a las futuras generaciones la posibilidad de satisfacer las suyas. Un recurso no renovable se agota al usarlo, por eso conviene usarlo con cuidado, reciclar y buscar otras fuentes de energía como el sol y el viento.",
    ],
    vocab=[("renovable", "que puede volver a formarse o reproducirse si se usa con cuidado"), ("no renovable", "que no se repone en un tiempo útil para las personas"), ("reforestación", "plantar árboles donde se cortó un bosque"), ("cuota de pesca", "límite de cuánto se puede pescar"), ("desarrollo sostenible", "satisfacer necesidades de hoy sin quitar a las futuras generaciones la posibilidad de satisfacer las suyas")],
    worked=[
        ("Clasificar un recurso", "{F} ¿El cobre es renovable o no renovable?", ["Busco el cobre en la ficha.", "Está en los no renovables."], "No renovable"),
        ("Causa y consecuencia", "{F} Si se pesca demasiado, ¿qué consecuencia tiene?", ["Reviso la ficha.", "Los peces disminuyen."], "Los peces disminuyen"),
    ],
    mistakes=[("Creer que un recurso renovable no se puede agotar.", "Se olvida el uso excesivo.", "Un recurso renovable también se agota si se usa mal."),
              ("Creer que desarrollo sostenible es no usar nada.", "Se confunde cuidar con prohibir.", "Es usar sin quitar a las futuras generaciones.")],
    T=[
        ("{F} ¿Qué recurso renovable nombra la ficha además de los peces?", "los bosques, el agua dulce de los ríos, el sol o el viento", "La ficha los nombra."),
        ("{F} ¿Qué recurso no renovable nombra la ficha además del cobre?", "el hierro, el litio, el petróleo o el carbón", "La ficha los nombra."),
        ("{F} ¿Qué es la reforestación?", "plantar árboles donde se cortó un bosque", "La ficha lo dice."),
        ("{F} ¿Qué es una cuota de pesca?", "un límite de cuánto se puede pescar", "La clase lo explica."),
        ("{F} ¿Cuál es un recurso renovable: el viento o el petróleo?", "el viento", "El petróleo es no renovable."),
        ("{F} Clasifica como «renovable» o «no renovable»: a) litio; b) sol; c) carbón; d) bosque.", "renovable: b y d; no renovable: a y c", "La ficha los clasifica."),
        ("{F} ¿Qué medida ayuda a que los peces se reproduzcan?", "la veda", "Prohíbe pescar por un tiempo."),
        ("{F} ¿Qué pasa si se corta un bosque sin plantar árboles nuevos?", "el bosque desaparece", "La ficha lo dice."),
        ("{F} Une cada problema con su medida: 1) se pesca demasiado; 2) se cortó un bosque. a) reforestación; b) veda o cuota.", "1 con b; 2 con a", "Cada medida responde a su problema."),
        ("{F} Pedro dice: «Los peces son renovables, así que se puede pescar sin límite». Corrígelo.", "también se agotan si se pesca demasiado; por eso hay veda y cuotas", "La ficha lo explica."),
        ("{F} Ana dice: «El cobre se volverá a formar en pocos años». Corrígela.", "el cobre es no renovable y no se repone en un tiempo útil", "La ficha lo clasifica así."),
        ("{F} ¿Por qué usar sol y viento ayuda al desarrollo sostenible?", "porque son renovables y no se agotan al usarlos con cuidado", "Cuidan a las futuras generaciones."),
        ("{F} Ordena la cadena: a) disminuyen los peces; b) se pesca demasiado; c) se decreta una veda.", "b, a, c", "El abuso lleva a la baja y luego a la medida."),
    ],
    ctx=("Una familia recicla papel y botellas, y apaga las luces que no usa. ¿Qué idea de la ficha están poniendo en práctica?", "cuidar los recursos para un desarrollo sostenible", "Ahorrar y reciclar cuida los recursos."),
    sc=[("{F} ¿Qué es un recurso renovable?", "uno que puede volver a formarse o reproducirse si se usa con cuidado", "Así se define."),
        ("{F} ¿Qué es el desarrollo sostenible?", "satisfacer las necesidades de hoy sin quitar a las futuras generaciones la posibilidad de satisfacer las suyas", "Así lo define la ficha."),
        ("Nombra una medida para cuidar los peces.", "la veda o las cuotas de pesca", "Son medidas de la ficha.")],
    op=("Haz un cuadro de dos columnas, «renovables» y «no renovables», con tres recursos en cada una. Debajo escribe dos acciones que ayuden al desarrollo sostenible. {F}",
        "Renovables: peces, bosque, viento. No renovables: cobre, hierro, litio. Acciones: respetar la veda y reciclar.",
        ["seis recursos bien clasificados", "dos acciones", "datos de la ficha"], ["cuadro", "dos acciones"], ["poner el cobre como renovable", "olvidar las acciones"],
        "Pregunta qué recurso le preocuparía más agotar y por qué."),
    reinforce="Di en voz alta la diferencia entre renovable y no renovable con dos ejemplos de cada uno.",
    extend="Escribe una acción de tu escuela que podría ahorrar agua o energía.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (perspectivas, hecha para este cuaderno). Situación: una empresa quiere abrir una mina de cobre cerca de un río. "
     "Perspectiva de la empresa: «La mina creará empleos y aportará dinero al país». Perspectiva de la comunidad: «Necesitamos el agua del río para beber y regar; no queremos que se ensucie ni se acabe». "
     "Perspectiva de una autoridad: «Debemos revisar el plan para proteger el agua y permitir el trabajo». Perspectiva de una persona que cuida el medioambiente: «El cobre no se renueva; hay que usarlo con cuidado y reciclar». "
     "Territorios: en el Norte Grande, el agua es muy escasa; en la Zona Sur, es abundante.")
build(
    OA10, 4, F,
    use="Aprenderé a comparar cómo ven el uso de un recurso la empresa, la comunidad, la autoridad y una persona que cuida el medioambiente. Sirve para buscar soluciones sostenibles.",
    prior=["Sé qué es un recurso renovable y no renovable.", "Sé qué es una perspectiva."],
    explain=[
        "Cuando se usa un recurso natural, distintas personas tienen intereses diferentes. Una empresa minera puede decir que la mina creará empleos y aportará dinero al país. Una comunidad cercana puede decir que necesita el agua del río para beber y regar, y que no quiere que se ensucie ni se acabe.",
        "Una autoridad puede decir que debe revisar el plan para proteger el agua y permitir el trabajo. Una persona que cuida el medioambiente puede recordar que el cobre no se renueva y que hay que usarlo con cuidado y reciclar. Todas estas perspectivas pueden tener parte de razón.",
        "También comparamos territorios. En el Norte Grande el agua es muy escasa, así que un río es muy valioso. En la Zona Sur el agua es abundante. Una decisión sostenible busca que el recurso se use sin dañar a la comunidad ni a las futuras generaciones.",
    ],
    vocab=[("interés", "lo que un grupo quiere lograr"), ("autoridad", "persona o institución que decide y fiscaliza"), ("medioambiente", "naturaleza y lugares que nos rodean"), ("empleo", "trabajo con sueldo"), ("sostenible", "que puede mantenerse en el tiempo sin agotar los recursos")],
    worked=[
        ("Comparar perspectivas", "{F} ¿Qué diferencia hay entre lo que pide la empresa y la comunidad?", ["La empresa pide abrir la mina por los empleos.", "La comunidad pide cuidar el agua del río."], "La empresa quiere empleos y dinero; la comunidad, agua limpia"),
        ("Buscar un punto en común", "{F} ¿Qué puede querer tanto la empresa como la comunidad?", ["Reviso las cuatro perspectivas.", "Puede ser trabajo y agua cuidada."], "Un acuerdo que permita trabajo y cuide el agua"),
    ],
    mistakes=[("Pensar que hay una sola postura correcta.", "Se simplifica el problema.", "Revisa cada perspectiva y su interés."),
              ("Olvidar a las futuras generaciones.", "Se mira solo el presente.", "Pregunta qué pasará con el recurso más adelante.")],
    T=[
        ("{F} ¿Qué dice la empresa que creará la mina?", "empleos", "La ficha lo dice."),
        ("{F} ¿Para qué necesita el agua la comunidad?", "para beber y regar", "La ficha lo dice."),
        ("{F} ¿Qué dice la autoridad que debe revisar?", "el plan", "La ficha lo dice."),
        ("{F} ¿Qué recuerda la persona que cuida el medioambiente sobre el cobre?", "que no se renueva", "La ficha lo dice."),
        ("{F} ¿Dónde es muy escasa el agua?", "en el Norte Grande", "La ficha lo dice."),
        ("{F} Clasifica cada frase por perspectiva: a) necesitamos el agua del río; b) la mina creará empleos.", "a: comunidad; b: empresa", "Cada frase refleja ese interés."),
        ("{F} Elige quién busca equilibrio entre proteger el agua y permitir el trabajo: A) la autoridad; B) la empresa.", "A", "La ficha lo dice de la autoridad."),
        ("{F} ¿Qué perspectiva destaca que el recurso es no renovable?", "la de la persona que cuida el medioambiente", "Así lo dice la ficha."),
        ("{F} Pedro dice: «La empresa y la comunidad quieren lo mismo». Corrígelo.", "la empresa quiere empleos y dinero; la comunidad, agua limpia", "Sus intereses son distintos."),
        ("{F} Ana dice: «La comunidad no quiere ningún trabajo». ¿Qué dato lo corrige?", "la comunidad pide cuidar el agua, no prohíbe el trabajo", "La ficha dice que pide cuidar el agua."),
        ("{F} Explica por qué el agua importa más en el Norte Grande que en la Zona Sur.", "porque en el Norte Grande es muy escasa", "La ficha lo dice."),
        ("{F} ¿Qué solución podría satisfacer a varias perspectivas?", "un plan que permita el trabajo, proteja el agua y promueva reciclar el cobre", "Combina los intereses de la ficha."),
        ("{F} Compara la perspectiva de la empresa con la de la autoridad.", "la empresa destaca empleos y dinero; la autoridad quiere revisar el plan para proteger el agua y permitir el trabajo", "Cada una pone el acento en un interés distinto."),
    ],
    ctx=("En una reunión del barrio, una vecina dice «necesitamos agua limpia» y un dirigente dice «necesitamos trabajo». ¿Qué perspectivas de la ficha se parecen a cada uno?", "la vecina se parece a la comunidad; el dirigente, a la empresa", "Cada uno defiende un interés."),
    sc=[("¿Qué es una perspectiva?", "el punto de vista de una persona o grupo sobre un hecho", "Así se define."),
        ("{F} ¿Qué perspectiva pide reciclar?", "la de la persona que cuida el medioambiente", "La ficha lo dice."),
        ("¿Por qué conviene escuchar varias perspectivas antes de decidir?", "porque cada una muestra intereses y riesgos distintos", "Así se decide mejor.")],
    op=("Haz una tabla con cuatro filas: «empresa», «comunidad», «autoridad» y «persona que cuida el medioambiente». En las columnas escribe «qué quiere» y «qué teme». Después escribe una solución que sirva a por lo menos dos de ellos. {F}",
        "Empresa: empleos; teme no abrir. Comunidad: agua limpia; teme que se ensucie. Autoridad: equilibrio. Persona ambiental: cuidar el cobre. Solución: abrir con reglas para cuidar el agua.",
        ["cuatro filas completas", "dos columnas", "una solución para dos intereses"], ["tabla", "una solución"], ["inventar datos", "no considerar a la comunidad"],
        "Pregunta qué perspectiva te costó más entender."),
    reinforce="Explica en voz alta lo que quiere cada actor de la ficha.",
    extend="Escribe una pregunta que le harías a la autoridad para decidir con más información.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (argumento, hecha para este cuaderno; las cifras son valores de ejemplo). Afirmación: «Cuidar los recursos naturales es necesario para un desarrollo sostenible». Datos: "
     "1) La pesca de una especie bajó de 100 a 50 toneladas en cuatro años, y por eso se decretó una veda. 2) El cobre y el hierro son no renovables. 3) El sol y el viento son renovables y se usan para producir energía. "
     "4) La reforestación permite recuperar bosques cortados. 5) Una comunidad pidió cuidar el agua de un río cercano a una mina. 6) Reciclar metales ayuda a usar menos recursos nuevos.")
build(
    OA10, 5, F,
    use="Aprenderé a defender con evidencia por qué hay que cuidar los recursos naturales dentro de un desarrollo sostenible. Sirve para argumentar con datos y proponer acciones.",
    prior=["Sé qué recursos tiene Chile, cuáles son renovables y cuáles no.", "Sé armar un argumento con afirmación, evidencia y conclusión."],
    explain=[
        "Hoy defendemos esta afirmación: cuidar los recursos naturales es necesario para un desarrollo sostenible. Un argumento necesita evidencia. La primera evidencia es que la pesca de una especie bajó de 100 a 50 toneladas en cuatro años, y por eso se decretó una veda.",
        "La segunda es que el cobre y el hierro son no renovables y se agotan al usarlos. La tercera es que el sol y el viento son renovables y sirven para producir energía. La cuarta es que la reforestación permite recuperar bosques cortados. La quinta es que una comunidad pidió cuidar el agua de un río. La sexta es que reciclar metales ayuda a usar menos recursos nuevos.",
        "Con estos datos concluimos que cuidar los recursos asegura que las personas de hoy y las futuras puedan usarlos. Pero la ficha no dice cuántos recursos quedan ni cuánto cuesta cuidarlos. Un buen argumento reconoce lo que no sabe y propone acciones concretas.",
    ],
    vocab=[("evidencia", "dato de una fuente que apoya una idea"), ("conclusión", "idea final que sale de unir la afirmación y la evidencia"), ("reciclar", "volver a usar materiales ya usados para hacer nuevos productos"), ("acción", "cosa concreta que se hace para lograr algo"), ("futuras generaciones", "personas que vivirán después de nosotros")],
    worked=[
        ("Elegir evidencia", "{F} ¿Qué dato apoya que los peces necesitan cuidado?", ["Busco un dato de peces.", "La pesca bajó de 100 a 50 toneladas y se decretó una veda."], "La pesca bajó de 100 a 50 toneladas y se decretó una veda"),
        ("Reconocer un límite", "{F} ¿La ficha dice cuántas toneladas de cobre quedan?", ["Busco una cifra.", "No hay ninguna."], "No, no da esa cifra"),
    ],
    mistakes=[("Defender una idea sin dar evidencia.", "Se cree que basta con opinar.", "Agrega al menos tres datos de la ficha."),
              ("Decir que cuidar significa no usar nada.", "Se confunde cuidar con prohibir.", "Cuidar es usar sin agotar.")],
    T=[
        ("=", "{F} ¿Cuántas toneladas bajó la pesca entre el primer y el cuarto año?", "100-50", "Se resta la cifra menor a la mayor.", " toneladas"),
        ("{F} ¿Qué dos recursos nombra el dato 2 como no renovables?", "el cobre y el hierro", "El dato 2 los nombra."),
        ("{F} ¿Qué dos recursos renovables nombra el dato 3?", "el sol y el viento", "El dato 3 los nombra."),
        ("{F} ¿Qué permite recuperar bosques cortados según el dato 4?", "la reforestación", "El dato 4 lo dice."),
        ("{F} ¿Qué pidió la comunidad según el dato 5?", "cuidar el agua de un río", "El dato 5 lo dice."),
        ("{F} ¿Qué ayuda a usar menos recursos nuevos según el dato 6?", "reciclar metales", "El dato 6 lo dice."),
        ("{F} ¿Qué dato apoya que los recursos no renovables hay que usarlos con cuidado: el dato 2 o el dato 3?", "el dato 2", "Dice que se agotan."),
        ("{F} ¿Qué dato muestra una solución para recuperar un recurso renovable?", "el dato 4, la reforestación", "Permite recuperar bosques."),
        ("{F} Ordena el argumento: a) conclusión: cuidar los recursos asegura su uso futuro; b) afirmación: cuidar es necesario; c) evidencia: la pesca bajó de 100 a 50 toneladas.", "b, c, a", "Se afirma, se prueba y se concluye."),
        ("{F} Pedro dice: «Como hay mucho sol, no hace falta cuidar los demás recursos». Corrígelo.", "el sol es renovable, pero el cobre y el hierro no, y los peces y bosques pueden agotarse", "La ficha muestra recursos distintos."),
        ("{F} Ana dice: «Quedan 5.000.000 de toneladas de cobre». ¿Qué respuesta le das?", "la ficha no da esa cifra, necesitaría una fuente", "No se afirma una cifra sin fuente."),
        ("{F} Argumento A: «Hay que cuidar los recursos». Argumento B: «Hay que cuidar los recursos, pues la pesca bajó de 100 a 50 toneladas y se decretó una veda». ¿Cuál es mejor?", "B, porque incluye evidencia", "Un argumento necesita datos."),
        ("{F} Elige la acción que apoya la afirmación. A) Reciclar latas de metal. B) Dejar una llave de agua abierta sin necesidad.", "A", "Reciclar metales usa menos recursos nuevos, como dice el dato 6."),
    ],
    ctx=("En una asamblea escolar alguien dice: «El cobre es de Chile, así que podemos usarlo sin cuidado». Usa dos datos de la ficha para responder.", "el cobre es no renovable y reciclar metales ayuda a usar menos recursos nuevos", "Los datos muestran que hay que cuidarlo."),
    sc=[("¿Cuáles son las tres partes de un argumento?", "afirmación, evidencia y conclusión", "Así se ordena."),
        ("{F} ¿Qué es la veda en el dato 1?", "la prohibición temporal de pescar para que la especie se reproduzca", "Se decretó por la baja de la pesca."),
        ("¿Por qué hay que reconocer lo que no se sabe?", "porque evita afirmar más de lo que prueban los datos", "Es parte de argumentar bien.")],
    op=("Escribe un párrafo de cinco líneas que defienda la afirmación de la ficha. Usa tres datos de la ficha, propone una acción personal y termina con «La ficha no dice…». {F}",
        "Cuidar los recursos es necesario para un desarrollo sostenible. La pesca bajó de 100 a 50 toneladas. El cobre no se renueva. Yo puedo reciclar papel. La ficha no dice cuánto cobre queda.",
        ["afirmación clara", "tres datos de la ficha", "una acción personal", "un límite reconocido"], ["párrafo escrito"], ["inventar cifras", "no proponer acción"],
        "Pide que subraye con colores los datos y la acción."),
    reinforce="Explica en voz alta tres datos que prueban que hay que cuidar los recursos.",
    extend="Escribe otra afirmación sobre el cuidado de los recursos y qué datos necesitarías buscar para defenderla.",
)
