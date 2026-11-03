"""Material del estudiante de 8.º básico, Historia, Geografía y Ciencias Sociales: OA 05 (encuentro y enfrentamiento entre culturas en América)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 05"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (mapa y fechas, simplificados). Pueblos de América hacia 1492: los mexicas, con capital en Tenochtitlan, en el valle de México; los mayas, con ciudades-estado en el sur de México y en Centroamérica; "
     "los incas, con capital en Cusco, que gobernaban el Tahuantinsuyo a lo largo de los Andes; los mapuche, en el centro-sur de lo que hoy es Chile y Argentina, organizados en comunidades sin un Estado central. "
     "Europa: reinos cristianos gobernados por reyes, como Castilla. "
     "Fechas: 1492, Colón llega a América, a islas del Caribe; 1519, Hernán Cortés llega a México; 1532, Francisco Pizarro captura al Inca Atahualpa en Cajamarca, en los Andes del actual Perú; 1541, Pedro de Valdivia funda Santiago.")
build(
    OA, 1, F,
    use="Aprenderé a situar el encuentro entre europeos y pueblos americanos en el tiempo y en el espacio, y a plantear por qué ese contacto se convirtió en un enfrentamiento entre culturas.",
    prior=["Conozco la expansión europea del siglo XVI.", "Sé ubicar América y sus regiones en un mapa.", "Sé calcular diferencias entre años."],
    explain=[
        "Cuando los europeos llegaron a América, el continente no estaba vacío ni era uniforme. Vivían muchos pueblos, con lenguas, formas de gobierno y creencias distintas. Los mexicas y los incas formaban grandes imperios con capitales como Tenochtitlan y Cusco. Los mayas tenían ciudades-estado. Los mapuche vivían en comunidades sin un Estado central.",
        "Para situar el encuentro hay que usar el tiempo y el espacio. Colón llegó en 1492; Cortés, a México en 1519; Pizarro capturó al Inca Atahualpa en 1532; Valdivia fundó Santiago en 1541. Cada fecha corresponde a un lugar distinto y a un pueblo distinto. Por eso no se debe hablar de «los indígenas» como si fueran un bloque.",
        "El encuentro no fue neutral. Chocaron culturas muy diferentes en su forma de entender el poder, la tierra y lo sagrado. El OA pide argumentar por qué hubo enfrentamiento considerando tres aspectos: la profundidad de las diferencias culturales, la magnitud del escenario natural americano y la desarticulación de la cosmovisión indígena. En esta clase solo planteamos el problema.",
    ],
    vocab=[("pueblo originario", "pueblo que vivía en un territorio antes de la llegada de los europeos"), ("imperio", "Estado muy extenso que gobierna a varios pueblos"), ("cosmovisión", "manera de entender el mundo, la naturaleza y lo sagrado"), ("encuentro", "contacto entre pueblos que no se conocían"), ("enfrentamiento", "choque entre grupos con intereses o formas de vida distintas")],
    worked=[
        ("Calcular una diferencia", "Según la ficha, ¿cuántos años pasaron entre la llegada de Colón y la fundación de Santiago?", ["Busco los años: 1492 y 1541.", "Resto: 1541 − 1492 = 49."], "49 años"),
        ("Evitar un bloque homogéneo", "Un texto dice «los indígenas vivían en imperios». ¿Qué pueblo de la ficha lo contradice?", ["Busco un pueblo sin Estado central.", "Los mapuche vivían en comunidades sin un Estado central."], "Los mapuche"),
    ],
    mistakes=[("Hablar de «los indígenas» como si todos fueran iguales.", "Se ignora que eran pueblos con lenguas y organizaciones distintas.", "Nombra el pueblo concreto: mexicas, incas, mayas o mapuche."),
              ("Pensar que el encuentro fue un hecho de un solo año.", "Se confunden varios encuentros en lugares y fechas diferentes.", "Ubica cada hecho con su fecha y lugar.")],
    T=[
        ("{F} ¿Cuál era la capital de los mexicas?", "Tenochtitlan", "La ficha la nombra."),
        ("{F} ¿Qué pueblo vivía en comunidades sin un Estado central en el centro-sur de Chile y Argentina?", "Los mapuche", "La ficha lo indica."),
        ("{F} ¿Qué capital tenían los incas?", "Cusco", "Aparece en la ficha."),
        ("=", "{F} ¿Cuántos años pasaron entre la llegada de Colón y la de Cortés a México?", "1519-1492", "Se resta el primer año al segundo.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la llegada de Cortés a México y la captura de Atahualpa?", "1532-1519", "Se restan los dos años.", " años"),
        ("{F} ¿A qué siglo pertenece la fundación de Santiago en 1541?", "Siglo XVI", "El siglo XVI va de 1501 a 1600."),
        ("{F} Ordena del hecho más antiguo al más reciente: fundación de Santiago, llegada de Cortés a México, llegada de Colón, captura de Atahualpa.", "Llegada de Colón, llegada de Cortés a México, captura de Atahualpa, fundación de Santiago", "Los años son 1492, 1519, 1532 y 1541."),
        ("{F} Clasifica a cada pueblo según su organización: a) incas, b) mapuche. Opciones: Estado central o comunidades sin Estado central.", "a) Estado central; b) comunidades sin Estado central", "Los incas tenían capital en Cusco; los mapuche no tenían Estado central."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 10 años y parte en 1492. ¿A cuántos cm queda 1541, redondeando hacia abajo?", "(1541-1492)//10", "Se divide la diferencia de años por la escala.", " cm"),
        ("{F} ¿Por qué es un error decir «los indígenas hablaban todos la misma lengua y tenían el mismo gobierno»?", "Porque la ficha muestra pueblos con capitales, ciudades-estado o comunidades distintas", "Los pueblos tenían organizaciones diferentes."),
        ("{F} ¿Qué afirmación es correcta? A) El encuentro ocurrió en varios lugares y en fechas distintas B) El encuentro ocurrió solo en 1492 en un único lugar", "A) El encuentro ocurrió en varios lugares y en fechas distintas", "La ficha da fechas de 1492 a 1541."),
        ("{F} Un compañero dice: «América estaba vacía antes de 1492». ¿Qué datos de la ficha lo contradicen?", "La ficha nombra mexicas, mayas, incas y mapuche viviendo en distintos territorios", "Había pueblos con capitales y ciudades."),
        ("{F} ¿Qué pregunta problema plantea esta clase?", "Por qué el encuentro entre europeos y pueblos americanos se convirtió en un enfrentamiento", "Es el problema central del OA."),
    ],
    ctx=("Un afiche escolar dice «Colón descubrió un continente vacío». ¿Qué título más preciso propondrías con la ficha? {F} A) Colón llegó a un continente donde vivían muchos pueblos distintos B) Colón llegó a un continente sin habitantes", "A) Colón llegó a un continente donde vivían muchos pueblos distintos", "La ficha nombra varios pueblos con organización propia."),
    sc=[("¿Qué es una cosmovisión?", "Una manera de entender el mundo, la naturaleza y lo sagrado", "Se definió en el vocabulario."),
        ("¿Qué pueblo tenía su capital en Tenochtitlan?", "Los mexicas", "La ficha lo indica."),
        ("=", "¿Cuántos años pasaron entre la captura de Atahualpa (1532) y la fundación de Santiago (1541)?", "1541-1532", "Se restan los dos años.", " años")],
    op=("Dibuja un mapa muy simple de América y marca con una raya los cuatro lugares donde ocurrieron las fechas de la ficha: islas del Caribe, México, Cajamarca y la zona de Santiago. Escribe cada año al lado de su lugar. Debajo escribe una frase que explique por qué no se puede hablar de un solo pueblo. {F}",
        "Caribe con 1492, México (Tenochtitlan) con 1519, Cajamarca en los Andes con 1532 y Santiago, en Chile central, con 1541. Frase: «Eran pueblos distintos, con capitales o comunidades distintas».",
        ["ubica los cuatro puntos", "escribe los cuatro años", "explica la diversidad"], ["mapa", "frase"], ["poner todos los pueblos como uno solo", "mezclar las fechas con lugares equivocados"],
        "Pide que explique qué diferencia observa entre incas y mapuche."),
    reinforce="Nombra de memoria los cuatro pueblos de la ficha y un dato de cada uno.",
    extend="Escribe una pregunta que le harías a un historiador para saber más sobre un pueblo que no aparece en la ficha.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, crónica de un cronista español de ejemplo, 1550, escrita en España para el rey: «En estas tierras hay muchos pueblos que no conocen la fe verdadera. Sus templos están llenos de figuras, y sus costumbres son distintas de las nuestras. Es nuestra misión enseñarles.» "
     "Fuente B, testimonio de un cronista indígena de ejemplo, 1580, traducido al español: «Nuestros abuelos tenían leyes, calendario y maestros. Cuando llegaron los extranjeros, nuestras autoridades fueron sustituidas y se prohibieron muchas de nuestras costumbres.»")
build(
    OA, 2, F,
    use="Aprenderé a analizar una crónica europea y un testimonio indígena sobre el encuentro, a contextualizarlos y a reconocer qué dice y qué no dice cada uno.",
    prior=["Sé contextualizar una fuente.", "Sé distinguir descripción e interpretación.", "Sé que cada actor tiene una perspectiva."],
    explain=[
        "Las fuentes sobre el encuentro entre europeos y pueblos americanos muestran perspectivas distintas. Una crónica europea suele escribirse para el rey o para la Iglesia, desde la fe y los valores de su autor. Un testimonio indígena, escrito o transmitido después, muestra cómo vivieron los cambios quienes los sufrieron. Ambas son fuentes valiosas, pero ninguna cuenta toda la historia.",
        "Para analizarlas hay que contextualizarlas: ¿quién las escribió, cuándo, dónde y para qué? La Fuente A está escrita en España para el rey, y su autor juzga las costumbres americanas desde su cultura. La Fuente B fue escrita treinta años después de la A, en otro contexto, y habla de lo perdido. Una fuente traducida también puede perder matices en el cambio de idioma.",
        "Un buen historiador compara ambas voces: busca qué coincide, qué se contradice y qué falta. No debe aceptar la valoración de una fuente como un hecho. Por ejemplo, «sus costumbres son distintas» describe una diferencia; «no conocen la fe verdadera» es un juicio de valor del autor.",
    ],
    vocab=[("crónica", "relato histórico escrito por alguien que vio o recogió los hechos"), ("testimonio", "relato de quien vivió o conoció los hechos"), ("juicio de valor", "opinión que dice si algo es bueno o malo según quien habla"), ("traducción", "paso de un texto a otro idioma, que puede perder matices"), ("perspectiva", "punto de vista según la posición de cada actor")],
    worked=[
        ("Contextualizar una fuente", "La Fuente A, ¿quién la escribió, para quién y cuándo?", ["Es un cronista español.", "Se escribió en 1550 para el rey."], "Un cronista español, para el rey, en 1550"),
        ("Separar hecho y juicio", "En la Fuente A, «sus costumbres son distintas de las nuestras» ¿es hecho o juicio de valor?", ["Describe una diferencia que se puede observar.", "No dice que sea buena o mala."], "Es una descripción; el juicio está en «no conocen la fe verdadera»"),
    ],
    mistakes=[("Tomar la opinión del cronista como si fuera un hecho.", "No se distingue descripción de juicio de valor.", "Subraya lo que describe y lo que valora."),
              ("Creer que el testimonio indígena cuenta lo que pensaban todos los pueblos.", "Un testimonio expresa la voz de una persona o comunidad.", "Di de qué pueblo o autor habla y busca otras voces.")],
    T=[
        ("{F} ¿Para quién escribió el cronista de la Fuente A?", "Para el rey", "La ficha lo indica."),
        ("{F} ¿En qué año se escribió la Fuente B?", "1580", "Es el año dado."),
        ("=", "{F} ¿Cuántos años separan la Fuente A de la Fuente B?", "1580-1550", "Se resta el año de la A al de la B.", " años"),
        ("{F} ¿Qué dice la Fuente B que se prohibió?", "Muchas de sus costumbres", "La fuente lo dice."),
        ("{F} ¿Qué cosa describe la Fuente B que tenían sus abuelos: leyes, calendario y maestros, o ejércitos y fortalezas?", "Leyes, calendario y maestros", "Son los tres elementos que nombra."),
        ("{F} Clasifica: a) «Sus templos están llenos de figuras», b) «No conocen la fe verdadera». ¿Cuál es descripción y cuál juicio de valor?", "a) descripción; b) juicio de valor", "La primera dice lo que se ve; la segunda valora según la fe del autor."),
        ("{F} ¿Qué objetivo declara el cronista de la Fuente A? A) Enseñar a esos pueblos su fe B) Pedir que se respete su cultura", "A) Enseñar a esos pueblos su fe", "La fuente dice: «Es nuestra misión enseñarles»."),
        ("{F} ¿Qué cambio denuncia la Fuente B? A) Sus autoridades fueron sustituidas B) Sus autoridades fueron respetadas", "A) Sus autoridades fueron sustituidas", "La fuente lo afirma."),
        ("{F} ¿Por qué la traducción de la Fuente B puede limitar su análisis?", "Porque al traducir se pueden perder matices del idioma original", "Se definió en el vocabulario."),
        ("{F} Un compañero dice: «La Fuente A prueba que los pueblos americanos no tenían religión». ¿Qué falla?", "La fuente solo muestra lo que piensa el cronista, que juzga desde su fe", "Es un juicio de valor, no una prueba."),
        ("{F} ¿Qué fuente muestra mejor cómo se vivió la pérdida de autoridades propias?", "La Fuente B, porque lo cuenta desde la perspectiva indígena", "Habla de autoridades sustituidas."),
        ("{F} ¿Qué conclusión es proporcional al comparar ambas fuentes? A) Muestran visiones distintas sobre el encuentro: una desde la misión y otra desde lo perdido B) Muestran que todos pensaban lo mismo", "A) Muestran visiones distintas sobre el encuentro: una desde la misión y otra desde lo perdido", "Las dos fuentes tienen perspectivas diferentes."),
        ("{F} ¿Qué otra fuente buscarías para conocer mejor la vida antes del encuentro? A) Restos arqueológicos de ciudades y objetos B) Un resumen escolar moderno sin fuentes", "A) Restos arqueológicos de ciudades y objetos", "Complementan lo que cuentan los textos."),
    ],
    ctx=("Un historiador escolar debe elegir una cita para un panel sobre el encuentro. ¿Qué precaución debe tener con la Fuente A? {F}", "Aclarar que es la visión de un cronista español que juzga desde su fe", "Hay que contextualizar la fuente y no presentar su opinión como hecho."),
    sc=[("¿Qué es un juicio de valor?", "Una opinión que dice si algo es bueno o malo según quien habla", "Se definió en el vocabulario."),
        ("¿Qué fuente de la ficha es un testimonio indígena?", "La Fuente B", "La A es de un cronista español."),
        ("=", "La Fuente A es de 1550 y la B de 1580. ¿Cuántos años pasaron entre ambas?", "1580-1550", "Se resta el primer año al segundo.", " años")],
    op=("Haz una tabla con las dos fuentes y cuatro filas: autor, fecha, para quién escribe y qué valora o critica. Después escribe una frase que explique en qué se diferencian sus perspectivas y una pregunta que no puedan responder. {F}",
        "A: cronista español, 1550, para el rey, valora enseñar la fe. B: cronista indígena, 1580, traducido, critica que se sustituyeron autoridades y costumbres. Pregunta: ¿cómo se sentían las mujeres?",
        ["completa las cuatro filas", "compara las perspectivas", "plantea una pregunta"], ["tabla", "frase", "pregunta"], ["mezclar autores", "tomar una opinión como hecho"],
        "Pide que explique por qué importan la fecha y el idioma de cada fuente."),
    reinforce="Explica a otra persona la diferencia entre una crónica europea y un testimonio indígena.",
    extend="Escribe una pregunta que quisieras hacer a quien escribió la Fuente B.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (escenario natural americano, simplificado). La cordillera de los Andes se extiende por más de 7.000 kilómetros de norte a sur. En ella viven pueblos como los incas y los mapuche. "
     "La selva amazónica, en el interior de Sudamérica, es muy extensa y de difícil acceso. El valle de México, donde estaba Tenochtitlan, se ubica en una zona alta y rodeada de montañas. "
     "Los europeos venían de un continente con distancias menores y con otros climas, animales y cultivos. Los europeos traían caballos, ganado, hierro y armas de fuego; en América se cultivaban el maíz, la papa y otras plantas desconocidas para ellos. "
     "Continuidades de los pueblos originarios: se siguen hablando lenguas como el quechua, el náhuatl y el mapuzugun, y se siguen cultivando maíz y papa.")
build(
    OA, 3, F,
    use="Aprenderé a describir la magnitud del escenario natural americano y a explicar qué cambió y qué continuó con la llegada de los europeos.",
    prior=["Sé ubicar cordilleras y selvas en un mapa de América.", "Conozco a los pueblos que vivían en América.", "Sé distinguir cambio y continuidad."],
    explain=[
        "El escenario natural americano era enorme y variado: cordilleras, selvas, desiertos, valles y costas. Los Andes se extienden por más de 7.000 kilómetros. La selva amazónica es muy extensa y de difícil acceso. Para los europeos, esas distancias y paisajes eran nuevos, y por eso hablaron de un «Nuevo Mundo», aunque para los pueblos que vivían allí era su territorio conocido.",
        "El territorio influyó en el encuentro. Los pueblos originarios conocían sus caminos, cultivos y recursos. Los europeos llegaron con caballos, ganado, hierro y armas de fuego, pero también dependieron de guías y alimentos locales. La magnitud del escenario hizo que la conquista fuera lenta en algunas zonas, como las selvas o el sur de Chile.",
        "Hubo cambios: nuevos animales, nuevas ciudades y enfermedades que antes no existían en América. Pero también continuidades: los pueblos siguieron cultivando maíz y papa y siguen hablando lenguas como el quechua, el náhuatl y el mapuzugun. Mirar cambio y continuidad evita pensar que todo desapareció.",
    ],
    vocab=[("escenario natural", "conjunto de relieves, climas, ríos y paisajes de un territorio"), ("cordillera", "cadena larga de montañas"), ("selva", "bosque muy denso de clima cálido y húmedo"), ("ganado", "animales domésticos que se crían para trabajo o alimento"), ("lengua originaria", "idioma de un pueblo originario, como el quechua o el mapuzugun")],
    worked=[
        ("Medir una magnitud", "Los Andes miden más de 7.000 km de norte a sur. Si un viajero recorre 35 km por día, ¿cuántos días tardaría en recorrer solo 700 km de esa cordillera?", ["Divido: 700 ÷ 35.", "El resultado es 20."], "20 días"),
        ("Clasificar cambio y continuidad", "Llegan caballos a América y se sigue cultivando maíz. ¿Qué es cambio y qué continuidad?", ["Los caballos son nuevos en América: cambio.", "El maíz ya se cultivaba: continuidad."], "Cambio: caballos; continuidad: cultivo de maíz"),
    ],
    mistakes=[("Pensar que el territorio americano era un lugar poco conocido para sus habitantes.", "Se mira solo desde la perspectiva europea.", "Recuerda que los pueblos originarios conocían sus caminos y recursos."),
              ("Creer que la llegada de los europeos borró todas las costumbres.", "Se ignoran las continuidades.", "Nombra lenguas y cultivos que continuaron.")],
    T=[
        ("{F} ¿Cuántos kilómetros se extienden los Andes, como mínimo?", "Más de 7.000 km", "La ficha lo indica."),
        ("{F} ¿Qué animales traían los europeos?", "Caballos y ganado", "La ficha los nombra."),
        ("{F} ¿Qué dos cultivos americanos menciona la ficha?", "Maíz y papa", "La ficha los nombra."),
        ("=", "{F} Un viajero recorre 40 km por día. ¿Cuántos días tarda en recorrer 800 km de los Andes?", "800//40", "Se divide la distancia entre lo que recorre por día.", " días"),
        ("=", "{F} En un mapa, 1 cm representa 500 km. ¿Cuántos centímetros ocupan los 7.000 km de los Andes?", "7000//500", "Se divide la longitud real por lo que vale cada centímetro.", " cm"),
        ("{F} ¿Qué lenguas originarias se siguen hablando según la ficha?", "Quechua, náhuatl y mapuzugun", "La ficha las nombra."),
        ("{F} Clasifica como cambio o continuidad: a) llegan caballos, b) se sigue cultivando maíz, c) se siguen hablando lenguas originarias.", "a) cambio; b) continuidad; c) continuidad", "Los caballos son lo nuevo."),
        ("{F} ¿Por qué la selva amazónica dificultó el avance de los europeos? A) Es muy extensa y de difícil acceso B) Estaba totalmente deshabitada", "A) Es muy extensa y de difícil acceso", "Lo dice la ficha."),
        ("{F} ¿Qué elementos de la lista de la ficha daban una ventaja militar a los europeos?", "Caballos, hierro y armas de fuego", "Eran tecnología distinta de la local; el ganado, en cambio, era alimento y trabajo."),
        ("{F} ¿Por qué los pueblos originarios no vivían en un «Nuevo Mundo»?", "Porque era su territorio conocido, con caminos y recursos que ya usaban", "El término es una perspectiva europea."),
        ("{F} Un compañero dice: «La conquista fue igual de rápida en todos los territorios». ¿Qué idea de la explicación de la clase lo contradice?", "La magnitud y dificultad del escenario, como selvas y el sur de Chile, hicieron lenta la conquista en algunas zonas", "El territorio influyó en el ritmo."),
        ("{F} ¿Qué conclusión es proporcional? A) El escenario natural influyó en el encuentro, pero no lo explica por sí solo B) El escenario natural explica todo", "A) El escenario natural influyó en el encuentro, pero no lo explica por sí solo", "Hubo otros factores como culturas y armas."),
        ("{F} ¿Qué pregunta de territorio ayudaría a entender mejor el encuentro?", "¿Qué zonas fueron más difíciles de controlar para los europeos y por qué?", "Relaciona el ritmo de la conquista con el escenario."),
    ],
    ctx=("Un afiche escolar dice «La naturaleza americana era un obstáculo para los europeos y nada más». ¿Qué le agregas desde la perspectiva de los pueblos originarios? {F}", "Que para ellos era su territorio conocido, con caminos, cultivos y recursos", "El afiche solo muestra la perspectiva europea."),
    sc=[("¿Qué es una cordillera?", "Una cadena larga de montañas", "Se definió en el vocabulario."),
        ("¿Qué lengua originaria nombra la ficha además del quechua y el náhuatl?", "El mapuzugun", "La ficha la nombra."),
        ("=", "Un viajero camina 25 km al día. ¿Cuántos kilómetros recorre en 8 días?", "25*8", "Se multiplica lo que recorre por día por los días.", " km")],
    op=("Dibuja un croquis de Sudamérica con la cordillera de los Andes y la selva amazónica. Marca con flechas tres cosas que llegaron con los europeos (caballos, ganado, hierro) y tres que ya existían en América (maíz, papa, lenguas originarias). Escribe una frase sobre una continuidad. {F}",
        "Andes a lo largo de la costa oeste y selva en el interior; flechas de Europa con caballos, ganado y hierro; maíz, papa y lenguas ya existentes. Frase: «Los pueblos siguieron cultivando maíz y hablando sus lenguas».",
        ["ubica Andes y selva", "separa lo que llegó de lo que existía", "nombra una continuidad"], ["croquis", "frase"], ["mezclar lo que llegó con lo que existía", "no mencionar continuidades"],
        "Pide que explique cómo el escenario natural pudo ayudar a un pueblo local a resistir."),
    reinforce="Cuenta tres cosas que llegaron de Europa y tres que ya existían en América.",
    extend="Escribe una pregunta sobre cómo cambió un alimento americano la comida de otro continente.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno; no son testimonios reales). "
     "Voz 1, capitán español, 1530: «Venimos a servir al rey, a difundir la fe y a buscar riqueza. Nuestras leyes y nuestra religión son las correctas.» "
     "Voz 2, sacerdote español, 1530: «Debemos enseñar la fe cristiana y bautizar a quienes habitan estas tierras.» "
     "Voz 3, autoridad de un pueblo andino, 1530 (ejemplo): «La tierra es de la comunidad y se trabaja en reciprocidad. Las personas se ayudan unas a otras y todos tienen un lugar.» "
     "Voz 4, líder de una comunidad mapuche, 1550 (ejemplo): «Nuestro territorio es parte de nuestra vida; las decisiones se toman en comunidad y defendemos lo que es nuestro.» "
     "Vocabulario: reciprocidad significa ayudarse unos a otros de manera mutua y organizada.")
build(
    OA, 4, F,
    use="Aprenderé a contrastar la cosmovisión europea con la de pueblos originarios, para explicar por qué el encuentro se volvió un enfrentamiento entre culturas.",
    prior=["Sé qué es una cosmovisión.", "Sé contrastar perspectivas.", "Conozco a los pueblos andinos y mapuche."],
    explain=[
        "La cosmovisión es la manera en que un pueblo entiende el mundo, la naturaleza, el poder y lo sagrado. Los europeos del siglo XVI veían un mundo organizado por el rey y por una fe cristiana que creían universal. Su idea de la tierra incluía la propiedad privada y el beneficio económico.",
        "Los pueblos originarios tenían otras formas de entender la vida. En el mundo andino, por ejemplo, el trabajo en reciprocidad y la vida en comunidad eran centrales. En el pueblo mapuche, las decisiones se toman en comunidad y el territorio es parte de la vida. No eran todos iguales, pero compartían una relación con la tierra distinta de la de la mirada europea.",
        "Estas diferencias llevaron a un choque. Cuando los europeos impusieron su religión, sus leyes y sus formas de propiedad, se desarticuló la cosmovisión de las sociedades indígenas: es decir, se rompieron las bases de su manera de entender el mundo. Para comprender el enfrentamiento hay que ver las razones y los intereses de cada lado sin reducir a los pueblos originarios a un bloque.",
    ],
    vocab=[("cosmovisión", "manera de entender el mundo, la naturaleza y lo sagrado"), ("reciprocidad", "ayuda mutua y organizada entre personas"), ("propiedad privada", "derecho de una persona a poseer tierra o bienes como suyos"), ("desarticular", "romper las partes que mantienen unida una forma de vida"), ("comunidad", "grupo de personas que comparten territorio y decisiones")],
    worked=[
        ("Contrastar dos voces", "¿En qué se diferencian la voz 1 y la voz 3 respecto de la tierra y de la ley?", ["La voz 1 habla de leyes y religión correctas y de riqueza.", "La voz 3 habla de tierra de la comunidad y reciprocidad."], "La voz 1 impone su ley y busca riqueza; la voz 3 vive en comunidad y reciprocidad"),
        ("Reconocer una desarticulación", "Si se prohíbe una costumbre que organizaba el trabajo en comunidad, ¿qué se está desarticulando?", ["La costumbre sostenía el trabajo en reciprocidad.", "Prohibirla rompe esa base."], "Parte de la cosmovisión y organización del pueblo"),
    ],
    mistakes=[("Presentar a todos los pueblos originarios con la misma cosmovisión.", "Se ignora la diversidad entre pueblos.", "Nombra el pueblo y su forma de decidir."),
              ("Explicar el enfrentamiento solo por la violencia de las armas.", "Se olvida el choque entre formas de entender el mundo.", "Incluye diferencias religiosas, de propiedad y de organización.")],
    T=[
        ("{F} ¿Quién dice que sus leyes y su religión son las correctas?", "El capitán español", "Es la voz 1."),
        ("{F} ¿Qué quiere hacer el sacerdote con quienes habitan estas tierras?", "Enseñarles la fe cristiana y bautizarlos", "La voz 2 lo dice."),
        ("{F} ¿Qué significa reciprocidad según la ficha?", "Ayudarse unos a otros de manera mutua y organizada", "Es la definición que da la ficha."),
        ("{F} ¿Cómo se toman las decisiones en la voz de la comunidad mapuche?", "En comunidad", "La voz 4 lo afirma."),
        ("{F} ¿Qué voz habla de la tierra como de la comunidad: la voz 1 o la voz 3?", "La voz 3", "La voz 3 dice que la tierra es de la comunidad."),
        ("=", "{F} ¿Cuántos años pasaron entre las voces 1 (1530) y 4 (1550)?", "1550-1530", "Se resta el primer año al segundo.", " años"),
        ("{F} Clasifica cada voz según su principal idea: a) voz 2, b) voz 3. Opciones: difundir la fe cristiana; vivir en comunidad y reciprocidad.", "a) difundir la fe cristiana; b) vivir en comunidad y reciprocidad", "Cada voz expresa una prioridad distinta."),
        ("{F} ¿Por qué la voz 1 y la voz 3 chocan respecto de la tierra? A) La voz 1 busca riqueza y la voz 3 defiende la tierra de la comunidad B) Ambas piensan lo mismo", "A) La voz 1 busca riqueza y la voz 3 defiende la tierra de la comunidad", "Sus ideas de tierra son distintas."),
        ("{F} ¿Qué se desarticula cuando se prohíbe una costumbre del trabajo en comunidad?", "Parte de la manera de vivir y entender el mundo del pueblo", "Se rompen las bases de su cosmovisión."),
        ("{F} Un compañero dice: «Los pueblos andinos y los mapuche pensaban exactamente igual». ¿Qué falla?", "La ficha muestra una voz andina sobre reciprocidad y una mapuche sobre decisiones en comunidad; eran pueblos distintos", "No se deben unir pueblos diferentes en un bloque."),
        ("{F} ¿Qué conclusión es proporcional a las cuatro voces? A) El encuentro enfrentó formas distintas de entender el poder, la tierra y la fe B) Todos buscaban lo mismo", "A) El encuentro enfrentó formas distintas de entender el poder, la tierra y la fe", "Las voces muestran valores diferentes."),
        ("{F} La voz 3 y la voz 4 tienen un punto en común. ¿Cuál es?", "La importancia de la comunidad", "Ambas hablan de decisiones o trabajo en comunidad."),
        ("{F} ¿Qué voz falta en la ficha y sería importante escuchar?", "La de una mujer o la de un niño de un pueblo originario", "No aparecen mujeres ni jóvenes."),
    ],
    ctx=("Una profesora pregunta a su curso: «¿Qué dos valores chocaron entre los europeos y los pueblos andinos?». Con la ficha, ¿qué responderías? {F}", "La riqueza y la imposición de una fe y ley frente a la tierra de la comunidad y la reciprocidad", "Cada voz expresa un valor central."),
    sc=[("¿Qué es la reciprocidad?", "La ayuda mutua y organizada entre personas", "Se definió en la ficha."),
        ("¿Qué quiere hacer el capitán, además de difundir la fe?", "Servir al rey y buscar riqueza", "La voz 1 lo dice."),
        ("¿Qué significa desarticular? A) Romper las partes que mantienen unida una forma de vida B) Fortalecer una costumbre", "A) Romper las partes que mantienen unida una forma de vida", "Así se definió.")],
    op=("Escribe un diálogo de seis líneas entre el sacerdote español y la autoridad andina de la ficha. Cada uno debe usar una idea de su voz y deben notarse sus diferencias sobre la tierra y la fe. Cierra con una frase tuya sobre por qué esa diferencia puede llevar a un choque. {F}",
        "Sacerdote: debemos enseñar la fe cristiana. Autoridad andina: la tierra es de la comunidad y trabajamos en reciprocidad. Cierre: quieren cosas distintas y por eso chocan.",
        ["usa ideas de la ficha", "muestra las diferencias", "cierra con una explicación"], ["diálogo", "frase"], ["inventar ritos o costumbres", "hacer que se pongan de acuerdo sin evidencia"],
        "Pide que diga qué voz indígena falta en su diálogo."),
    reinforce="Explica con tus palabras qué es una cosmovisión y da un ejemplo de la ficha.",
    extend="Escribe una pregunta que le harías a una persona de un pueblo originario hoy sobre su relación con la tierra. Recuerda que la forma tradicional la enseñan sus propias comunidades.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (pregunta y evidencias de ejemplo). Pregunta: ¿por qué la llegada de los europeos implicó un enfrentamiento entre culturas? "
     "Evidencia 1 (diferencias culturales): los europeos buscaban difundir su fe cristiana y los pueblos americanos tenían sus propias creencias. "
     "Evidencia 2 (diferencias culturales): los europeos entendían la tierra como propiedad privada; en el mundo andino y mapuche la tierra se vinculaba con la comunidad. "
     "Evidencia 3 (escenario natural): las distancias americanas y las selvas, desiertos y cordilleras hicieron difícil controlar el territorio. "
     "Evidencia 4 (cosmovisión): se prohibieron costumbres y se sustituyeron autoridades propias. "
     "Evidencia 5 (contexto): los europeos tenían caballos, hierro y armas de fuego y pueblos originarios resistieron en muchas zonas.")
build(
    OA, 5, F,
    use="Aprenderé a argumentar por qué el encuentro fue un enfrentamiento entre culturas, usando los tres aspectos del OA: diferencias culturales, escenario natural y desarticulación de la cosmovisión.",
    prior=["Sé que un argumento tiene tesis, evidencias y límite.", "Conozco las diferencias entre cosmovisiones.", "Conozco el escenario natural americano."],
    explain=[
        "El OA pide argumentar por qué el encuentro implicó un enfrentamiento entre culturas, considerando tres aspectos. El primero es la profundidad de las diferencias culturales: religión, propiedad de la tierra y forma de gobierno eran muy distintas. El segundo es la magnitud del escenario natural, que hizo difícil el control del territorio. El tercero es la desarticulación de la cosmovisión indígena, cuando se prohibieron costumbres y se sustituyeron autoridades.",
        "Un argumento sólido combina estos tres aspectos con evidencias. Por ejemplo: «El encuentro fue un enfrentamiento porque las diferencias culturales eran profundas y los europeos impusieron su fe y sus leyes, lo que desarticuló la cosmovisión indígena». La evidencia 4 apoya esa idea, y la 3 explica por qué en algunas zonas el control fue difícil.",
        "Todo argumento necesita un límite. Las evidencias de la ficha no distinguen entre pueblos ni entre momentos, y hubo también alianzas y acuerdos entre algunos grupos. Reconocer eso evita presentar a los pueblos como un bloque o al encuentro como un hecho neutral.",
    ],
    vocab=[("tesis", "respuesta que se defiende con evidencias"), ("aspecto", "parte o rasgo de un tema"), ("alianza", "acuerdo entre grupos que se apoyan entre sí"), ("imponer", "obligar a aceptar algo"), ("límite", "lo que la evidencia no permite concluir")],
    worked=[
        ("Clasificar evidencias", "¿Qué aspecto del OA ilustra la evidencia 3?", ["Habla de distancias, selvas, desiertos y cordilleras.", "Eso es el escenario natural."], "La magnitud del escenario natural"),
        ("Redactar un límite", "Tesis: «El encuentro fue un enfrentamiento entre culturas». ¿Qué límite agregas?", ["Las evidencias no distinguen pueblos ni momentos.", "También hubo alianzas."], "Las evidencias no muestran que todos los pueblos lo vivieran igual y hubo alianzas"),
    ],
    mistakes=[("Explicar el enfrentamiento solo por el escenario natural.", "Se olvidan las diferencias culturales y la imposición.", "Combina los tres aspectos."),
              ("Presentar el encuentro como un hecho neutral.", "Se ignora la imposición y la pérdida de autoridades propias.", "Cita evidencias de prohibición y sustitución.")],
    T=[
        ("{F} ¿Qué evidencia habla de la tierra como propiedad privada?", "La evidencia 2", "Contrasta la propiedad privada con la comunidad."),
        ("{F} ¿Qué evidencia muestra la desarticulación de la cosmovisión?", "La evidencia 4", "Habla de prohibir costumbres y sustituir autoridades."),
        ("{F} ¿Qué aspecto del OA corresponde a las evidencias 1 y 2?", "Las diferencias culturales", "Se rotulan así en la ficha."),
        ("{F} ¿Qué evidencia muestra la resistencia de pueblos originarios?", "La evidencia 5", "Dice que resistieron en muchas zonas."),
        ("{F} ¿Cuántas de las cinco evidencias se refieren a diferencias culturales?", "Dos: la 1 y la 2", "Son las que la ficha rotula así."),
        ("{F} ¿Qué tesis se apoya mejor en las evidencias? A) El encuentro fue un enfrentamiento porque las diferencias eran profundas y se desarticuló la cosmovisión indígena B) El encuentro fue un hecho neutral", "A) El encuentro fue un enfrentamiento porque las diferencias eran profundas y se desarticuló la cosmovisión indígena", "Las evidencias 1, 2 y 4 apoyan la tesis."),
        ("{F} Un compañero dice: «Fue solo un choque de armas». ¿Qué evidencias le opones?", "La 1, 2 y 4, que muestran diferencias de fe, tierra y cosmovisión", "El choque también fue cultural."),
        ("{F} Clasifica cada evidencia con su aspecto del OA: a) 3, b) 4. Opciones: escenario natural; desarticulación de la cosmovisión.", "a) escenario natural; b) desarticulación de la cosmovisión", "Cada evidencia corresponde a un aspecto."),
        ("{F} ¿Por qué el escenario natural ayuda a explicar el enfrentamiento?", "Porque la magnitud del territorio hizo difícil controlarlo y permitió resistir en algunas zonas", "La evidencia 3 y la 5 se conectan."),
        ("{F} Escribe un límite honesto para la tesis.", "Las evidencias no distinguen entre pueblos y momentos, y hubo también alianzas", "Un argumento reconoce lo que no prueba."),
        ("{F} ¿Qué respuesta es más sólida? A) «Hubo enfrentamiento por diferencias de fe y tierra, por el territorio difícil y por la imposición sobre la cosmovisión» B) «Fue un choque porque sí»", "A) «Hubo enfrentamiento por diferencias de fe y tierra, por el territorio difícil y por la imposición sobre la cosmovisión»", "Cita los tres aspectos del OA."),
        ("{F} ¿Qué error comete quien cita solo la evidencia 5?", "Muestra solo la tecnología y la resistencia, sin las diferencias culturales ni la cosmovisión", "No cubre los tres aspectos."),
        ("{F} ¿Qué diferencia hay entre decir «todos los pueblos resistieron» y la evidencia 5?", "La evidencia 5 habla de muchas zonas, no de todas", "No se debe generalizar."),
    ],
    ctx=("Un concurso escolar pide una respuesta de una frase a «¿Por qué fue un enfrentamiento?». Redáctala usando dos aspectos del OA. {F}", "Fue un enfrentamiento porque las diferencias culturales eran profundas y se desarticuló la cosmovisión indígena", "Usa dos aspectos y evidencias de la ficha."),
    sc=[("¿Qué tres aspectos pide considerar el OA?", "Diferencias culturales, escenario natural y desarticulación de la cosmovisión", "Son los tres del OA."),
        ("¿Qué es una alianza?", "Un acuerdo entre grupos que se apoyan entre sí", "Se definió en el vocabulario."),
        ("¿Qué evidencia habla de prohibir costumbres? A) La evidencia 4 B) La evidencia 3", "A) La evidencia 4", "La 4 habla de prohibiciones y sustitución de autoridades.")],
    op=("Escribe un párrafo de seis líneas con tu tesis, tres evidencias numeradas de la ficha (una de cada aspecto del OA) y un límite. Evita decir «los indígenas» sin precisar y nombra al menos un pueblo. {F}",
        "Pienso que fue un enfrentamiento porque las diferencias eran profundas. Evidencia 2: propiedad frente a comunidad. Evidencia 3: territorio difícil. Evidencia 4: se prohibieron costumbres. Límite: no distinguen entre mapuche, incas o mexicas.",
        ["tiene tesis", "tres evidencias de aspectos distintos", "incluye un límite"], ["párrafo"], ["citar una sola evidencia", "hablar de un bloque homogéneo"],
        "Pide que explique por qué su límite es importante."),
    reinforce="Explica oralmente los tres aspectos que explican el enfrentamiento.",
    extend="Escribe una pregunta que ayudaría a saber cómo vivió un pueblo concreto el encuentro.",
)

# ---------------------------------------------------------------- clase 6
F = ("Ficha 6 (decisión ciudadana de ejemplo, ficticia). Un municipio de ejemplo piensa instalar en una plaza un panel que diga «El descubrimiento de América fue un encuentro pacífico entre culturas». "
     "Datos de apoyo: (1) hubo intercambios de productos y de ideas; (2) hubo alianzas entre algunos pueblos indígenas y los europeos; (3) hubo guerras, trabajos forzados y prohibición de costumbres; (4) hoy viven personas de pueblos como mapuche, aymara, rapanui y diaguita en Chile, con sus lenguas y tradiciones. "
     "Fuentes disponibles: crónicas europeas, testimonios indígenas traducidos, estudios arqueológicos y estudios actuales.")
build(
    OA, 6, F,
    use="Aprenderé a evaluar una afirmación sobre el encuentro con fuentes variadas, a reconocer sus límites y a distinguir qué se puede concluir y qué no sobre el pasado y el presente.",
    prior=["Sé analizar fuentes y perspectivas.", "Sé argumentar con evidencias y límites.", "Conozco los aspectos del encuentro entre culturas."],
    explain=[
        "Evaluar una afirmación histórica significa compararla con las evidencias y ver si las acepta o las contradice. La frase del panel dice que fue un encuentro pacífico. Los datos de la ficha muestran que hubo intercambios y alianzas, pero también guerras, trabajos forzados y prohibición de costumbres. Por eso la frase simplifica demasiado.",
        "Todo juicio tiene límites. Las fuentes disponibles —crónicas europeas, testimonios indígenas traducidos, estudios arqueológicos y estudios actuales— se complementan, pero ninguna da toda la información. Las crónicas europeas muestran la visión de quien conquistó. Los testimonios indígenas muestran la visión de quienes sufrieron cambios. Las dos perspectivas se necesitan.",
        "También hay que distinguir pasado y presente. Hoy viven en Chile personas de pueblos como mapuche, aymara, rapanui y diaguita, con sus lenguas y tradiciones. Eso muestra una continuidad. Pero no podemos trasladar el pasado de manera directa al presente: los contextos son distintos y las preguntas de hoy, como la dignidad y los derechos de los pueblos, se discuten con nuevas fuentes.",
    ],
    vocab=[("evaluar", "comparar una afirmación con las evidencias para juzgar si se sostiene"), ("simplificar", "reducir un tema complejo a una sola idea"), ("complementar", "sumar información que completa a otra"), ("continuidad", "algo que se mantiene a lo largo del tiempo"), ("proyección", "idea de cómo el pasado influye en el presente")],
    worked=[
        ("Evaluar una afirmación", "La frase dice «fue un encuentro pacífico». ¿Qué dato de la ficha la contradice?", ["Busco datos de violencia.", "El dato 3 menciona guerras, trabajos forzados y prohibición de costumbres."], "El dato 3"),
        ("Reconocer un límite", "Si solo usamos crónicas europeas, ¿qué voz falta?", ["Las crónicas son de quienes conquistaron.", "Faltan los testimonios indígenas."], "La voz indígena"),
    ],
    mistakes=[("Aceptar una frase solo porque suena amable.", "No se contrasta con las evidencias.", "Revisa cada dato y pregunta si lo sostiene."),
              ("Decir que el pasado explica por sí solo la situación de hoy.", "Se ignoran los contextos distintos.", "Distingue lo que continúa de lo que cambió.")],
    T=[
        ("{F} ¿Qué dato de la ficha apoya la idea de intercambio entre culturas?", "El dato 1: intercambios de productos y de ideas", "Es el que menciona intercambios."),
        ("{F} ¿Qué dato muestra violencia y pérdida de costumbres?", "El dato 3", "Habla de guerras, trabajos forzados y prohibición de costumbres."),
        ("{F} ¿Qué pueblos viven hoy en Chile según el dato 4?", "Mapuche, aymara, rapanui y diaguita", "La ficha los nombra."),
        ("{F} Un panel que cita solo los datos 1 y 2, ¿qué datos deja fuera?", "Los datos 3 y 4: la violencia y la presencia actual de los pueblos", "Los datos 3 y 4 no aparecen en esa selección."),
        ("{F} ¿La frase del panel sobre un «encuentro pacífico» se sostiene con todos los datos? A) No, porque el dato 3 la contradice B) Sí, porque el dato 1 la apoya", "A) No, porque el dato 3 la contradice", "Un solo dato favorable no basta si otros la contradicen."),
        ("{F} ¿Qué tipo de fuente son los estudios arqueológicos?", "Fuentes que estudian restos materiales, como objetos y ciudades", "La arqueología analiza restos materiales."),
        ("{F} ¿Qué voz falta si se usan solo las crónicas europeas?", "La voz indígena", "Las crónicas europeas muestran la visión de quien conquistó."),
        ("{F} Clasifica cada dato como cooperación o conflicto: a) 2, b) 3.", "a) cooperación; b) conflicto", "El dato 2 habla de alianzas y el 3 de guerras y prohibiciones."),
        ("{F} ¿Por qué la continuidad de pueblos y lenguas hoy no permite decir que «nada cambió»?", "Porque hubo cambios como guerras, trabajos forzados y prohibiciones", "Continuidad y cambio coexisten."),
        ("{F} Un compañero dice: «Como hubo alianzas, no hubo conflicto». ¿Qué falla?", "Ignora el dato 3 de guerras, trabajos forzados y prohibición de costumbres", "Las alianzas no cancelan los conflictos."),
        ("{F} ¿Qué frase propondrías para el panel? A) «El encuentro combinó intercambios, alianzas, guerras y pérdidas para los pueblos originarios» B) «Todo fue pacífico»", "A) «El encuentro combinó intercambios, alianzas, guerras y pérdidas para los pueblos originarios»", "Recoge los cuatro datos."),
        ("{F} ¿Qué límite tendría ese panel? A) No distingue entre pueblos ni momentos B) Usa demasiadas fuentes", "A) No distingue entre pueblos ni momentos", "Una frase general no detalla las experiencias de cada pueblo."),
        ("{F} ¿Qué otra fuente agregarías para completar la visión? A) Relatos de comunidades de los pueblos originarios hoy B) Una crónica europea más del siglo XVI", "A) Relatos de comunidades de los pueblos originarios hoy", "Agrega la voz de quienes continúan esa historia."),
    ],
    ctx=("El concejo del municipio de la ficha pide tu opinión para decidir el texto del panel. ¿Qué recomiendas en una frase? {F}", "Cambiar el texto para incluir intercambios, alianzas y también guerras y pérdidas, y consultar a pueblos originarios", "Una frase equilibrada y con consulta evita simplificar."),
    sc=[("¿Qué significa evaluar una afirmación?", "Compararla con las evidencias para ver si se sostiene", "Se definió en el vocabulario."),
        ("¿Qué quiere decir simplificar?", "Reducir un tema complejo a una sola idea", "Se definió en el vocabulario."),
        ("¿Qué muestra que viven hoy mapuche, aymara, rapanui y diaguita? A) Una continuidad B) Que nada cambió", "A) Una continuidad", "Es algo que se mantiene en el tiempo.")],
    op=("Redacta un texto de cuatro a cinco líneas para el panel del municipio de la ficha que sea más preciso que el original. Debe incluir un dato de intercambio o alianza, un dato de conflicto o pérdida y una frase que reconozca la presencia de pueblos originarios hoy. Escribe después un límite de tu texto. {F}",
        "Entre los siglos XV y XVII, el encuentro incluyó intercambios y alianzas, pero también guerras y prohibiciones. Hoy mapuche, aymara, rapanui y diaguita mantienen sus lenguas y tradiciones. Límite: el texto no distingue entre pueblos.",
        ["incluye intercambio y conflicto", "reconoce a los pueblos hoy", "incluye un límite"], ["texto de panel"], ["decir que fue pacífico", "no mencionar a los pueblos originarios hoy"],
        "Pide que explique por qué consultó o consultaría a comunidades."),
    reinforce="Explica por qué una frase como «fue un encuentro pacífico» simplifica demasiado.",
    extend="Escribe una pregunta que le harías a un historiador y otra a una persona de un pueblo originario sobre este tema.",
)
