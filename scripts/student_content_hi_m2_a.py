"""Material del estudiante de 2.º medio, Historia, Geografía y Ciencias Sociales: OA 01 (vanguardias y cultura de masas en entreguerras) y OA 02 (crisis liberal, Gran Depresión y modelos políticos)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 01"

# ================================================================ OA 01, clase 1
F = ("Ficha 1 (el período de entreguerras va de 1918, fin de la Primera Guerra Mundial, a 1939, comienzo de la Segunda). "
     "Hitos culturales: el dadaísmo nace en Zúrich en 1916, durante la guerra, y se extiende en los años siguientes; el Manifiesto del surrealismo se publica en 1924; "
     "«El cantante de jazz», película con partes habladas y cantadas, se estrena en Estados Unidos en 1927; la Gran Depresión comienza en 1929; los Juegos Olímpicos de Berlín se realizan en 1936. "
     "Actores: artistas de vanguardia, empresas de cine y de radio, anunciantes, público urbano y gobiernos.")
build(
    OA, 1, F,
    use="Aprenderé a situar en el tiempo y entre sus actores la ruptura cultural de entreguerras: qué fue una vanguardia, qué es una cultura de masas y quiénes participaron.",
    prior=["Sé qué fue la Primera Guerra Mundial y que terminó en 1918.", "Sé ubicar un año dentro de su siglo y calcular diferencias entre años.", "Sé que una fuente es una huella del pasado."],
    explain=[
        "Entreguerras es el período entre dos guerras mundiales, de 1918 a 1939. Tras una guerra de enorme destrucción, muchas personas dejaron de confiar en las reglas tradicionales del arte, la moral y la política. Los cánones son esas reglas aceptadas sobre lo que se considera bello o correcto, y las vanguardias son movimientos artísticos que los rompen a propósito.",
        "El dadaísmo rechazó las reglas del arte con humor provocador; el surrealismo exploró los sueños y el inconsciente, es decir, lo que la mente hace sin que lo decidamos. El jazz, música de raíces afroamericanas con improvisación, y los cambios en la moda, con ropa más cómoda, también rompieron costumbres.",
        "A la vez apareció una cultura de masas: cine, radio, prensa, publicidad y deporte llegaron a millones de personas gracias a la industria y a los medios de comunicación. Los actores fueron artistas, empresas, anunciantes, público y gobiernos. Para estudiarlo hay que situar cada hecho en su fecha y decir quién lo impulsaba.",
    ],
    vocab=[("entreguerras", "período entre el fin de la Primera Guerra Mundial (1918) y el inicio de la Segunda (1939)"), ("cánones", "reglas aceptadas sobre lo que se considera bello o correcto"), ("vanguardia", "movimiento artístico que rompe a propósito con las reglas tradicionales"), ("cultura de masas", "bienes culturales que llegan a muchísimas personas por medios de comunicación"), ("medios de comunicación", "canales como prensa, radio y cine que difunden mensajes a mucha gente")],
    worked=[
        ("Ubicar un hito en el período", "El Manifiesto del surrealismo se publicó en 1924. ¿Cae dentro de entreguerras?", ["El período va de 1918 a 1939.", "1924 está entre esos dos años."], "Sí, 1924 está dentro de entreguerras"),
        ("Clasificar un fenómeno", "Una estación de radio transmite el mismo noticiero a miles de casas. ¿Es vanguardia o cultura de masas?", ["La emisión llega a muchas personas por un medio de comunicación.", "No rompe una regla artística: difunde un mensaje."], "Cultura de masas"),
    ],
    mistakes=[("Pensar que vanguardia y cultura de masas son lo mismo.", "Se mezcla un movimiento que rompe reglas artísticas con medios que llegan a mucha gente.", "Pregunta si el hecho rompe un canon (vanguardia) o si difunde a millones (cultura de masas); puede ser ambos."),
              ("Poner todos los hitos en una sola fecha.", "No se separa lo que ocurrió durante la guerra de lo ocurrido después.", "Ubica cada hito con su año y compáralo con 1918 y 1939.")],
    T=[
        ("{F} ¿Qué años delimitan el período de entreguerras?", "1918 y 1939", "La ficha lo define entre el fin de la Primera Guerra y el comienzo de la Segunda."),
        ("{F} ¿En qué ciudad nace el dadaísmo?", "Zúrich", "La ficha lo ubica en Zúrich."),
        ("{F} ¿Qué película de 1927 nombra la ficha?", "«El cantante de jazz»", "La ficha la presenta como película con partes habladas y cantadas."),
        ("=", "{F} ¿Cuántos años pasaron entre el Manifiesto del surrealismo y los Juegos Olímpicos de Berlín?", "1936-1924", "Se resta el año del manifiesto al de los Juegos.", " años"),
        ("{F} ¿Qué es el dadaísmo según la ficha y la explicación? A) Una vanguardia artística B) Un medio de comunicación", "A) Una vanguardia artística", "Rechazó las reglas del arte con humor provocador, como hacen las vanguardias."),
        ("{F} El año 1916, ¿está dentro de entreguerras? A) No, es anterior a 1918 B) Sí, porque el dadaísmo es una vanguardia de esa época", "A) No, es anterior a 1918", "El período parte en 1918; el dadaísmo nace durante la guerra y solo se extiende después, dentro del período."),
        ("{F} Una radio emite el mismo programa para miles de hogares a la vez. ¿Qué rasgo de la cultura de masas muestra? A) Llega a muchas personas por un medio de comunicación B) Rompe las reglas del arte", "A) Llega a muchas personas por un medio de comunicación", "La difusión simultánea a mucha gente es el rasgo de la cultura de masas."),
        ("{F} Una artista pinta una escena de sueño con objetos imposibles para mostrar el inconsciente. ¿Qué vanguardia se parece más? A) Surrealismo B) Dadaísmo", "A) Surrealismo", "El surrealismo explora sueños e inconsciente, como indica la explicación."),
        ("{F} Un cartel repite por toda la ciudad el lema de una bebida. ¿Qué elemento de la cultura de masas es? A) Publicidad B) Jazz", "A) Publicidad", "Un mensaje repetido para vender un producto es publicidad."),
        ("{F} ¿Por qué se dice que las vanguardias rompen los cánones?", "Porque rechazan a propósito las reglas tradicionales sobre lo que es bello o correcto", "Un canon es una regla aceptada y la vanguardia la contradice de forma deliberada."),
        ("{F} Un compañero afirma: «En 1927 todo el mundo veía películas habladas». ¿Se puede sostener con la ficha? A) No, la ficha solo dice que se estrenó una película en Estados Unidos B) Sí, porque se estrenó en 1927", "A) No, la ficha solo dice que se estrenó una película en Estados Unidos", "Un estreno no prueba que lo viera todo el mundo; sería afirmar más de lo que la evidencia permite."),
        ("{F} ¿Cuál de estos actores impulsa la cultura de masas, según la ficha? A) Las empresas de cine y de radio B) Los exploradores polares", "A) Las empresas de cine y de radio", "La ficha las nombra entre los actores del período; los exploradores no aparecen."),
        ("¿Cuál es la mejor pregunta para investigar este tema? A) ¿Cómo cambiaron el arte y la forma de informarse y entretenerse entre 1918 y 1939? B) ¿Quién fue el mejor artista de la historia?", "A) ¿Cómo cambiaron el arte y la forma de informarse y entretenerse entre 1918 y 1939?", "La primera pregunta tiene tiempo, tema y se responde con hechos; la segunda es una opinión sin criterio."),
    ],
    ctx=("Una sala de exposición reúne un cartel publicitario, una grabación de radio y un cuadro dadaísta de 1921. ¿Qué título resume mejor la sala? A) Arte nuevo y cultura de masas en entreguerras B) La cultura del siglo XIX", "A) Arte nuevo y cultura de masas en entreguerras", "Vanguardia, radio y publicidad corresponden al período 1918-1939."),
    sc=[("¿Qué es una vanguardia?", "Un movimiento artístico que rompe a propósito con las reglas tradicionales", "Así se define en el vocabulario de la clase."),
        ("¿Cuál de estos es un elemento de la cultura de masas según la explicación? A) La radio B) El dadaísmo", "A) La radio", "La explicación nombra cine, radio, prensa, publicidad y deporte; el dadaísmo es una vanguardia."),
        ("En Historia: ¿qué es la cultura de masas?", "Bienes culturales, como cine, radio o prensa, que llegan a muchísimas personas por medios de comunicación", "Así se define en el vocabulario de la clase.")],
    op=("Dibuja una línea de tiempo de 1916 a 1939. Marca con una raya el dadaísmo (1916), el Manifiesto del surrealismo (1924), «El cantante de jazz» (1927), la Gran Depresión (1929) y los Juegos Olímpicos de Berlín (1936). Colorea de otro color el tramo 1918-1939. Después escribe dos frases: una sobre un hito que sea vanguardia y otra sobre uno que sea cultura de masas. {F}",
        "El tramo 1918-1939 queda marcado; el dadaísmo (1916) queda fuera, antes de 1918. Frases: «El surrealismo (1924) exploró los sueños»; «El cine hablado (1927) se difundió por medios de comunicación».",
        ["ubica los cinco hitos con su año", "marca bien el tramo de entreguerras", "distingue una vanguardia de un hecho de cultura de masas"], ["línea de tiempo dibujada", "dos frases escritas"], ["poner el dadaísmo dentro de 1918-1939 sin notar que nace en 1916", "usar el mismo hito en las dos frases"],
        "Pide que explique por qué el dadaísmo nace antes del período y aun así se estudia en él."),
    reinforce="Explica en voz alta, con tus palabras, la diferencia entre vanguardia y cultura de masas y da un hito con su año para cada una.",
    extend="Anota un objeto o un aviso de tu casa que sea publicidad y di qué quiere lograr en quien lo ve.",
)

# ================================================================ OA 01, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente 1, reseña de un diario, 1925: «El cine del barrio ofrece tres funciones diarias y se llena cada tarde; la entrada cuesta menos que un almuerzo sencillo.» "
     "Fuente 2, carta de un profesor a un colega, 1926: «Mis alumnos hablan de películas y bailan con discos de jazz; temo que olviden la música que yo les enseño.» "
     "Fuente 3, aviso de una tienda de radios, 1928: «Escuche la voz de la casa moderna. Su radio, en cuotas mensuales.»")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes de la cultura de entreguerras: quién habla, cuándo, para qué, y qué se puede y qué no se puede concluir.",
    prior=["Sé situar la cultura de masas y las vanguardias en 1918-1939.", "Sé que una fuente tiene autor, fecha y propósito.", "Sé distinguir lo que dice un texto de lo que yo opino."],
    explain=[
        "Para interrogar una fuente se preguntan cuatro cosas: quién la escribió, cuándo, para quién y con qué propósito. Una reseña de diario informa y opina, una carta privada muestra lo que piensa una persona y un aviso publicitario busca vender. Ninguna es neutral, pero todas son evidencia de lo que pensaba o quería cada autor.",
        "Hay que separar la descripción de la interpretación. Describir es repetir lo que dice el texto: «el cine ofrece tres funciones diarias». Interpretar es una idea tuya apoyada en el texto: «ir al cine ya era una costumbre en ese barrio». Una interpretación sólida no dice más de lo que las fuentes permiten.",
        "También importan los silencios: lo que la fuente no cuenta. Un aviso no dice cuántas personas compraron radios; una carta no habla por todos los profesores. Por eso se comparan varias fuentes antes de generalizar, y se escribe «esta fuente muestra que…» y no «todos pensaban que…».",
    ],
    vocab=[("procedencia", "dato de quién creó la fuente, cuándo y dónde"), ("propósito", "para qué se produjo una fuente, por ejemplo informar o vender"), ("descripción", "repetición de lo que dice una fuente sin agregar ideas propias"), ("interpretación", "idea propia apoyada en lo que dice una fuente"), ("silencio de la fuente", "información importante que la fuente no entrega")],
    worked=[
        ("Contextualizar", "Una nota de ejemplo dice: «Santiago, 1930. Un vendedor ofrece discos de jazz en la feria». ¿Quién, cuándo y dónde?", ["Autor o protagonista: un vendedor.", "Fecha: 1930.", "Lugar: Santiago."], "Un vendedor, en 1930, en Santiago"),
        ("Descripción o interpretación", "Sobre esa nota se dice: (1) «Se ofrecen discos de jazz en la feria» y (2) «El jazz era la música favorita de todos los chilenos». ¿Cuál es descripción?", ["La frase (1) repite lo que dice la nota.", "La frase (2) generaliza a todo un país con una sola nota."], "La (1) describe; la (2) afirma más de lo permitido"),
    ],
    mistakes=[("Concluir con un solo aviso que muchas familias tenían radio.", "Un aviso busca vender y no informa cuántos compraron.", "Escribe «el aviso ofrece radios» y busca otra fuente para saber cuántas se compraron."),
              ("Tomar la carta de un profesor como la opinión de todos los adultos.", "Una carta privada expresa el temor de una sola persona.", "Escribe «este profesor temía que…» y compara con otras fuentes.")],
    T=[
        ("{F} ¿En qué año se escribió la Fuente 2?", "1926", "La ficha la fecha en 1926."),
        ("{F} ¿Qué tipo de texto es la Fuente 3?", "Un aviso de una tienda de radios", "La ficha la presenta como aviso."),
        ("{F} ¿Cuántas funciones diarias ofrece el cine de la Fuente 1?", "Tres", "El texto lo dice de forma directa."),
        ("=", "{F} Si el cine de la Fuente 1 abre 6 días a la semana (dato de ejemplo) con las funciones que indica, ¿cuántas funciones ofrece por semana?", "3*6", "Se multiplican las funciones de cada día por los días de apertura.", " funciones"),
        ("=", "{F} ¿Cuántos años pasaron entre la reseña de la Fuente 1 y el aviso de la Fuente 3?", "1928-1925", "Se resta el año de la reseña al del aviso.", " años"),
        ("{F} ¿Cuál es el propósito más probable de la Fuente 3? A) Vender radios B) Informar la programación del cine", "A) Vender radios", "Es un aviso de una tienda que ofrece cuotas mensuales."),
        ("{F} ¿Cuál frase describe la Fuente 1? A) «El cine ofrece tres funciones diarias.» B) «Todo el país iba al cine.»", "A) «El cine ofrece tres funciones diarias.»", "La primera frase repite el texto; la segunda generaliza más de lo que dice."),
        ("{F} ¿Qué teme el autor de la Fuente 2? A) Que sus alumnos olviden la música que enseña B) Que las radios sean muy caras", "A) Que sus alumnos olviden la música que enseña", "La carta lo dice al final."),
        ("{F} ¿Qué fuente sirve más para saber qué temía un adulto ante los cambios culturales? A) La Fuente 2 B) La Fuente 3", "A) La Fuente 2", "La carta privada muestra una preocupación personal; el aviso solo vende."),
        ("{F} ¿Por qué la Fuente 3 no prueba que muchas familias tuvieran radio?", "Porque es un aviso que busca vender y no informa cuántas personas compraron", "El propósito de vender y el silencio sobre las compras limitan la conclusión."),
        ("{F} ¿Qué silencio tiene la Fuente 1 respecto del público?", "No dice cuántas personas asistían ni quiénes eran", "Solo habla de que se llena cada tarde, sin cifras ni descripción del público."),
        ("{F} Un compañero escribe: «La Fuente 2 prueba que todos los adultos rechazaban el jazz». ¿Qué corrección haces? A) Muestra el temor de un profesor, no el de todos los adultos B) Es correcto porque la carta lo dice", "A) Muestra el temor de un profesor, no el de todos los adultos", "Una carta de una persona no permite hablar de todos."),
        ("{F} ¿Qué fuente nueva ayudaría a saber cuántas personas escuchaban radio en 1928? A) Un registro de ventas o de receptores de la época B) Un aviso de otra tienda", "A) Un registro de ventas o de receptores de la época", "Un registro entrega cifras; otro aviso solo repite el propósito de vender."),
    ],
    ctx=("Para un trabajo sobre el cine en el barrio debes elegir entre usar solo la reseña o la reseña y la carta del profesor. ¿Qué elección da una conclusión más ajustada? A) Usar las dos, porque muestran el éxito del cine y una preocupación ante el cambio B) Usar solo la reseña, porque es más corta", "A) Usar las dos, porque muestran el éxito del cine y una preocupación ante el cambio", "Dos voces distintas permiten una conclusión más completa."),
    sc=[("¿Cuál de estas es una pregunta para interrogar una fuente? A) ¿Con qué propósito se escribió? B) ¿De qué color es la tapa?", "A) ¿Con qué propósito se escribió?", "Quién, cuándo, para quién y con qué propósito son las preguntas de procedencia de la explicación."),
        ("¿Qué es describir una fuente?", "Repetir lo que dice sin agregar ideas propias", "Describir se queda en el contenido del texto."),
        ("¿Qué busca un aviso publicitario?", "Vender un producto o servicio", "Ese es su propósito, que limita lo que prueba.")],
    op=("Elige una de las tres fuentes de la ficha. Escribe una tabla de tres filas: autor y fecha; qué dice (descripción en una frase); qué interpretas (una frase que empiece con «Esto sugiere que…»). Termina con una frase sobre lo que NO puedes concluir con esa sola fuente. {F}",
        "Fuente 2. Autor y fecha: un profesor, 1926. Dice: temía que sus alumnos olvidaran la música que enseña. Interpretación: esto sugiere que el jazz generaba preocupación en algunos adultos. No puedo concluir que todos los adultos pensaran lo mismo.",
        ["contextualiza con autor y fecha", "separa descripción de interpretación", "señala un límite de la fuente"], ["tabla de tres filas", "frase de límite"], ["escribir una interpretación como si fuera descripción", "concluir sobre toda la sociedad con un solo texto"],
        "Pide que cuente qué otra fuente buscaría para comparar y por qué."),
    reinforce="Escribe con un ejemplo propio de la Fuente 1 la diferencia entre describir e interpretar.",
    extend="Elige un aviso o un titular que veas hoy y responde: quién lo escribe, para qué y qué no podrías concluir con él.",
)

# ================================================================ OA 01, clase 3
F = ("Ficha 3 (perspectivas de ejemplo escritas para este cuaderno). "
     "Perspectiva 1, crítico de arte conservador, 1925: «La pintura debe imitar la realidad con oficio; estos cuadros de sueños confunden al público.» "
     "Perspectiva 2, joven artista, 1925: «Si el arte solo repite las reglas del pasado, no dice nada sobre un mundo que acaba de pasar por una guerra.» "
     "Escala local (dato de ejemplo): un cine de barrio con 300 butacas ofrece 3 funciones al día y las llena. "
     "Escala internacional: el jazz, nacido en Estados Unidos, se escucha en Europa y en América Latina gracias a discos y radios.")
build(
    OA, 3, F,
    use="Aprenderé a comparar perspectivas de personas distintas frente a las vanguardias y a mirar el mismo fenómeno a escala local e internacional.",
    prior=["Sé interrogar una fuente por su procedencia.", "Sé qué son una vanguardia y la cultura de masas.", "Sé calcular productos sencillos con datos."],
    explain=[
        "Una perspectiva es el punto de vista de una persona o grupo, que depende de su edad, su oficio y sus intereses. Frente a una misma obra, un crítico conservador puede ver confusión y un joven artista puede ver una forma de hablar de su tiempo. Comparar no es elegir quién tiene la razón: es entender qué valora cada uno y por qué.",
        "También se compara según la escala, es decir, el tamaño del lugar que se observa. A escala local se mira un barrio, un cine o una calle; a escala internacional se mira cómo una música, una película o una idea viaja entre países. Un mismo fenómeno puede parecer pequeño en un barrio y enorme si se suman muchos barrios y países.",
        "Para comparar bien, se escribe qué comparten las perspectivas, en qué se diferencian y qué evidencia sustenta cada una. Si un dato no está en la fuente, se rotula como hipótesis. Así se evita decir que todos los jóvenes eran vanguardistas o que todos los críticos rechazaban el cambio.",
    ],
    vocab=[("perspectiva", "punto de vista de una persona o grupo según su situación e intereses"), ("escala local", "mirada a un lugar pequeño, como un barrio"), ("escala internacional", "mirada a lo que ocurre entre varios países"), ("conservador", "que prefiere mantener las costumbres y reglas tradicionales"), ("hipótesis", "explicación posible que aún necesita evidencia")],
    worked=[
        ("Comparar perspectivas", "Según la ficha, ¿en qué difieren el crítico y el joven artista sobre el arte?", ["El crítico pide imitar la realidad con oficio.", "El joven artista pide un arte que hable de su tiempo, no solo del pasado."], "El crítico defiende las reglas tradicionales; el joven busca un arte nuevo"),
        ("Pasar de escala local a total", "Un cine de ejemplo tiene 200 butacas y ofrece 2 funciones llenas por día. ¿Cuántas personas asisten en un día?", ["Cada función se llena con 200 personas.", "200 × 2 = 400."], "400 personas"),
    ],
    mistakes=[("Decir que una perspectiva es verdadera y la otra falsa.", "Se confunde opinión con hecho comprobado.", "Describe qué valora cada una y qué evidencia presenta."),
              ("Concluir sobre el país entero a partir de un solo cine de barrio.", "Se salta de la escala local a la nacional sin datos.", "Di que el dato es local y busca otras fuentes para generalizar.")],
    T=[
        ("{F} ¿Qué pide el crítico de la Perspectiva 1 a la pintura?", "Que imite la realidad con oficio", "La ficha lo dice de forma directa."),
        ("{F} ¿Cuántas butacas tiene el cine de la escala local?", "300", "La ficha da el dato."),
        ("{F} ¿Dónde nació el jazz según la ficha?", "En Estados Unidos", "La ficha lo indica en la escala internacional."),
        ("=", "{F} ¿Cuántas personas asisten en un día al cine de barrio si todas las funciones se llenan?", "300*3", "Se multiplican las butacas por las funciones del día.", " personas"),
        ("{F} ¿Quién valora más romper las reglas del pasado? A) El joven artista B) El crítico conservador", "A) El joven artista", "El joven dice que repetir el pasado no habla del mundo posterior a la guerra."),
        ("{F} ¿Qué es la escala internacional en el caso del jazz? A) Su difusión entre países B) Su difusión en un barrio", "A) Su difusión entre países", "La escala internacional observa lo que ocurre entre varios países."),
        ("=", "{F} Si el cine de barrio abre 6 días a la semana (dato de ejemplo) y siempre llena sus funciones, ¿cuántas personas asisten por semana?", "300*3*6", "Se multiplican butacas, funciones diarias y días.", " personas"),
        ("{F} El crítico dice que los cuadros de sueños «confunden al público». ¿Qué tipo de afirmación es? A) Una opinión desde su perspectiva B) Un hecho medido", "A) Una opinión desde su perspectiva", "No entrega datos ni mediciones sobre la reacción del público."),
        ("{F} Una persona observa que en su barrio hay un cine lleno. ¿Qué escala está usando? A) Local B) Internacional", "A) Local", "Observa un lugar pequeño."),
        ("{F} ¿Qué tienen en común las dos perspectivas aunque se oponen? A) Ambas opinan sobre qué debe hacer el arte B) Ambas rechazan la pintura", "A) Ambas opinan sobre qué debe hacer el arte", "Difieren en cómo: uno pide imitar la realidad y el otro hablar del mundo tras la guerra."),
        ("{F} Un compañero dice: «El cine de barrio prueba que todo Chile iba al cine». ¿Qué problema tiene? A) Pasa de una escala local a una nacional sin datos B) Usa una fuente demasiado corta", "A) Pasa de una escala local a una nacional sin datos", "Un caso local no basta para generalizar a un país."),
        ("{F} ¿Qué afirmación sobre el jazz en América Latina respalda la ficha? A) Se escuchaba gracias a discos y radios B) Todas las familias tenían un tocadiscos", "A) Se escuchaba gracias a discos y radios", "La ficha menciona discos y radios; que todas las familias tuvieran tocadiscos no aparece en ella."),
        ("{F} ¿Cuál es la comparación más justa entre las perspectivas? A) Cada una valora algo distinto del arte y ninguna se prueba con datos B) La del joven es verdadera porque es más nueva", "A) Cada una valora algo distinto del arte y ninguna se prueba con datos", "Ser nueva no prueba que algo sea verdadero; son juicios de valor."),
    ],
    ctx=("Un curso quiere saber si el jazz era popular en su ciudad en 1927. ¿Qué plan combina mejor las escalas? A) Revisar avisos de la ciudad y también cómo se difundió el jazz en otros países B) Preguntar solo a un vecino mayor", "A) Revisar avisos de la ciudad y también cómo se difundió el jazz en otros países", "Combinar la escala local y la internacional da una mirada más completa."),
    sc=[("¿Qué es una perspectiva?", "El punto de vista de una persona o grupo según su situación e intereses", "Así se define en el vocabulario."),
        ("¿Qué mira la escala local?", "Un lugar pequeño, como un barrio o un cine", "Se contrapone a la escala internacional."),
        ("=", "Un cine de ejemplo tiene 150 butacas y llena 4 funciones al día. ¿Cuántas personas asisten?", "150*4", "Se multiplican butacas por funciones.", " personas")],
    op=("Escribe una tabla de comparación de dos columnas para las perspectivas 1 y 2 de la ficha, con tres filas: qué valora, qué evidencia o razón da y qué podría decir sobre el jazz. Después escribe una frase que explique cómo cambia la conclusión si miras solo el cine de barrio o el jazz entre países. {F}",
        "Perspectiva 1: valora el oficio y la imitación de la realidad; da como razón que el público se confunde; sobre el jazz diría que rompe la tradición musical. Perspectiva 2: valora hablar del tiempo vivido; razón: el mundo salió de una guerra; sobre el jazz diría que es música nueva para un mundo nuevo. Frase: a escala local el cine parece una costumbre del barrio; a escala internacional el jazz muestra un cambio cultural compartido entre países.",
        ["compara en las tres filas", "no declara cuál perspectiva es verdadera", "relaciona escala local e internacional"], ["tabla de dos columnas", "frase sobre escalas"], ["elegir una perspectiva como la correcta", "mezclar las dos escalas sin nombrarlas"],
        "Pide que diga qué dato nuevo necesitaría para saber si el jazz era popular en su ciudad."),
    reinforce="Explica a una persona de tu casa la diferencia entre mirar un fenómeno a escala local y a escala internacional.",
    extend="Piensa en una canción o juego que hoy se conoce en muchos países y di cómo se habrá difundido.",
)

# ================================================================ OA 01, clase 4
F = ("Ficha 4 (causas posibles de la cultura de masas, ordenadas por tipo). "
     "Técnicas: se extiende la electricidad en las ciudades; el cine y la radio se perfeccionan. "
     "Económicas: la producción en serie baja los precios de los aparatos; crece la publicidad. "
     "Sociales: más personas viven en ciudades y tienen tiempo libre; tras la guerra, muchos desconfían de las reglas tradicionales. "
     "Datos de ejemplo de una ciudad imaginaria: en 1920 hay 0 radios en los hogares y en 1930 hay 4.000. "
     "Continuidades: los museos y los teatros tradicionales siguen funcionando; muchas personas del campo no tienen electricidad.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar causas, cambios y continuidades en la transformación cultural de entreguerras y a distinguir una causa de un simple dato anterior.",
    prior=["Sé situar las vanguardias y la cultura de masas en 1918-1939.", "Sé comparar perspectivas y escalas.", "Sé calcular diferencias y promedios simples."],
    explain=[
        "Un hecho histórico rara vez tiene una sola causa: es multicausal. En entreguerras, la cultura de masas se explica por causas técnicas, como la electricidad, el cine y la radio; económicas, como la producción en serie y la publicidad; y sociales, como la vida urbana, el tiempo libre y la desconfianza hacia las reglas tradicionales tras la guerra.",
        "Un cambio es algo que se transforma, y una continuidad es algo que se mantiene. Cambió la forma de entretenerse y de informarse; continuaron los museos, los teatros y también las desigualdades, porque no todas las personas tenían electricidad ni dinero para una radio. Por eso un cambio rara vez ocurre al mismo tiempo en todas partes.",
        "Antes y después no siempre significan causa y efecto. Que el jazz y el cine hablado coincidan en una década no prueba que uno causó al otro. Para sostener una causa se necesita una razón que conecte los hechos y evidencia de que la causa ocurrió antes del efecto.",
    ],
    vocab=[("causa", "hecho o condición que ayuda a explicar otro hecho"), ("multicausalidad", "idea de que un hecho tiene varias causas a la vez"), ("cambio", "aspecto de la sociedad que se transforma en un período"), ("continuidad", "aspecto que se mantiene en un período"), ("correlación", "coincidencia entre dos hechos que no prueba que uno cause al otro")],
    worked=[
        ("Clasificar una causa", "¿La producción en serie que baja el precio de los aparatos es una causa técnica, económica o social?", ["Se refiere a precios y producción.", "La ficha la ubica entre las causas económicas."], "Económica"),
        ("Medir un cambio", "En la ciudad imaginaria de otra ficha había 500 radios en 1925 y 3.500 en 1935. ¿Cuántas radios más había?", ["Tomo los dos datos.", "3.500 − 500 = 3.000."], "3.000 radios más"),
    ],
    mistakes=[("Explicar la cultura de masas con una sola causa, por ejemplo solo la radio.", "Se ignoran las causas económicas y sociales que aparecen en la explicación.", "Nombra al menos una causa técnica, una económica y una social."),
              ("Pensar que lo que ocurre después de otro hecho fue causado por él.", "Se confunde la secuencia con la causa.", "Pregunta qué razón conecta los dos hechos y qué evidencia la apoya.")],
    T=[
        ("{F} ¿Qué tipo de causa es la extensión de la electricidad en las ciudades?", "Técnica", "La ficha la ubica entre las técnicas."),
        ("{F} ¿Cuántas radios hay en la ciudad imaginaria en 1930?", "4.000", "La ficha da el dato."),
        ("{F} ¿Qué sigue funcionando en entreguerras, según las continuidades de la ficha?", "Los museos y los teatros tradicionales", "La ficha lo nombra como continuidad."),
        ("=", "{F} ¿Cuántas radios más hay en 1930 que en 1920 en la ciudad imaginaria?", "4000-0", "Se resta el valor inicial al final.", " radios"),
        ("{F} ¿La publicidad es una causa económica o social? A) Económica B) Social", "A) Económica", "La ficha la ubica junto a la producción en serie."),
        ("{F} ¿Qué es una continuidad? A) Algo que se mantiene en el período B) Algo que se transforma en el período", "A) Algo que se mantiene en el período", "Así se define en el vocabulario."),
        ("=", "{F} Si las 4.000 radios de 1930 se repartieran en 800 hogares, ¿cuántas radios habría en cada hogar? (dato de ejemplo)", "4000/800", "Se divide el total de radios por el número de hogares.", " radios"),
        ("{F} Una persona vive en un pueblo sin electricidad y escucha cantar a sus vecinos. ¿Qué muestra eso? A) Una continuidad: la cultura de masas no llegó a todos B) Un cambio completo de la sociedad", "A) Una continuidad: la cultura de masas no llegó a todos", "La ficha señala que muchas personas del campo no tenían electricidad."),
        ("{F} Un aviso de 1927 ofrece radios en cuotas. ¿Qué causa de la cultura de masas ilustra? A) Una causa económica B) Una causa técnica", "A) Una causa económica", "Las cuotas y la publicidad ayudan a que más gente compre aparatos."),
        ("{F} ¿Por qué decir que la radio fue la única causa de la cultura de masas es un error?", "Porque hubo también causas económicas y sociales", "La ficha muestra tres tipos de causas."),
        ("{F} Un compañero dice: «El jazz se hizo popular en la misma década que el cine hablado, así que el cine causó el jazz». ¿Cuál es la crítica? A) Es una correlación y falta una razón y evidencia B) Es correcto porque ocurrió antes", "A) Es una correlación y falta una razón y evidencia", "La coincidencia en el tiempo no prueba que uno causara al otro."),
        ("{F} ¿Qué dato apoyaría más que la publicidad aumentó el consumo de radios? A) Un registro de ventas antes y después de campañas de avisos B) Un cuadro dadaísta de la misma década", "A) Un registro de ventas antes y después de campañas de avisos", "Un registro de ventas conecta la causa con el efecto; el cuadro no."),
        ("{F} ¿Cuál es la mejor explicación? A) Hubo causas técnicas, económicas y sociales, y el cambio llegó con desigualdad B) Todo cambió porque se inventó la radio", "A) Hubo causas técnicas, económicas y sociales, y el cambio llegó con desigualdad", "Reúne las tres causas y una continuidad, a diferencia de una causa única."),
    ],
    ctx=("Un diario escolar titula: «Las vanguardias nacieron solo porque la gente se aburría». ¿Qué problema tiene? A) Explica con una sola causa un hecho multicausal B) Está bien, porque las vanguardias tienen una causa evidente", "A) Explica con una sola causa un hecho multicausal", "Las vanguardias respondieron a la guerra, a la desconfianza de las reglas y a otros cambios."),
    sc=[("¿Qué es la multicausalidad?", "La idea de que un hecho tiene varias causas a la vez", "Así se define en la clase."),
        ("¿Cuál es una causa técnica de la cultura de masas? A) La extensión de la electricidad en las ciudades B) La producción en serie que baja los precios", "A) La extensión de la electricidad en las ciudades", "La producción en serie y la publicidad son causas económicas; la electricidad es técnica."),
        ("=", "En una ciudad de ejemplo había 1.200 radios en 1926 y 2.000 en 1932. ¿Cuántas más había?", "2000-1200", "Se resta el valor inicial al final.", " radios")],
    op=("Dibuja un esquema con el hecho «aparece la cultura de masas» en el centro. A la izquierda anota tres causas (una técnica, una económica y una social) y a la derecha un cambio y una continuidad. Escribe debajo una frase que diga por qué no basta una sola causa. {F}",
        "Causas: electricidad (técnica); producción en serie (económica); más gente en ciudades con tiempo libre (social). Cambio: la gente se informa y se entretiene con radio y cine. Continuidad: los teatros tradicionales siguen funcionando. Frase: un hecho histórico es multicausal y una causa sola dejaría fuera otras razones.",
        ["incluye tres tipos de causas", "distingue cambio de continuidad", "explica por qué no basta una causa"], ["esquema dibujado", "frase explicativa"], ["poner tres causas del mismo tipo", "confundir cambio con continuidad"],
        "Pide que explique con un ejemplo por qué una coincidencia en el tiempo no prueba una causa."),
    reinforce="Explica con tus palabras la diferencia entre cambio y continuidad usando un ejemplo de entreguerras.",
    extend="Piensa en un cambio reciente en cómo te informas y di una causa técnica y una social.",
)

# ================================================================ OA 01, clase 5
F = ("Ficha 5 (evidencias de ejemplo escritas para este cuaderno). "
     "Evidencia 1, aviso de 1929: una tienda ofrece radios en cuotas mensuales. "
     "Evidencia 2, programa de cine de barrio, 1930: tres funciones diarias de lunes a sábado. "
     "Evidencia 3, carta de un profesor, 1926: teme que sus alumnos olviden la música que enseña. "
     "Evidencia 4, afiche de una exposición de arte nuevo, 1928: invita a ver cuadros con figuras de sueños. "
     "Pregunta de investigación: ¿cómo cambió la vida cultural en la ciudad entre 1925 y 1930?")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada: afirmar algo, apoyarlo en evidencias de la ficha y decir qué límites tiene.",
    prior=["Sé interrogar fuentes por su procedencia.", "Sé que un hecho tiene varias causas.", "Sé separar descripción e interpretación."],
    explain=[
        "Una interpretación documentada tiene tres partes: una afirmación, la evidencia que la apoya y un límite. La afirmación responde a la pregunta de investigación; la evidencia cita qué fuente dice qué y en qué fecha; el límite dice qué no se puede concluir con lo que se tiene. Sin las tres partes, solo hay una opinión.",
        "Para elegir evidencias se pide que sean pertinentes, es decir, que hablen del tema, y variadas, es decir, de distintos tipos: un aviso, un programa, una carta. Si todas las evidencias vienen del mismo autor o del mismo lugar, la conclusión es débil. Dos evidencias que apoyan la misma idea la hacen más fuerte, y una que la contradice obliga a revisar la afirmación.",
        "La conclusión debe ser proporcional: se usa «sugiere», «muestra que» o «en esta ciudad». Evita «siempre», «todos» o «nadie», salvo que las fuentes lo digan. Con la ficha se puede decir que la vida cultural incorporó el cine, la radio y el arte nuevo, pero no cuánta gente participaba.",
    ],
    vocab=[("interpretación documentada", "explicación que cita fuentes concretas y reconoce sus límites"), ("evidencia pertinente", "dato o fuente que se relaciona directamente con la pregunta"), ("afirmación", "idea que responde a la pregunta de investigación"), ("límite", "aquello que no se puede concluir con las fuentes disponibles"), ("proporcional", "que no dice más de lo que la evidencia permite")],
    worked=[
        ("Elegir evidencia", "Para afirmar «el cine formaba parte de la vida cotidiana de la ciudad en 1930», ¿qué evidencia de la ficha sirve?", ["Busco una que hable de cine.", "La Evidencia 2 informa funciones diarias de lunes a sábado."], "La Evidencia 2"),
        ("Calcular funciones", "¿Cuántas funciones ofrece el cine de la Evidencia 2 en una semana de lunes a sábado?", ["Son 3 funciones por día.", "De lunes a sábado hay 6 días: 3 × 6 = 18."], "18 funciones"),
    ],
    mistakes=[("Afirmar que «todos» en la ciudad escuchaban radio.", "Una oferta de radios en cuotas no prueba cuántos las compraron.", "Escribe «el aviso muestra que se vendían radios en cuotas»."),
              ("Citar solo evidencias de un mismo tipo.", "Una conclusión con una sola clase de fuente es débil.", "Combina un aviso, un programa y una carta, por ejemplo.")],
    T=[
        ("{F} ¿En qué año es la Evidencia 4?", "1928", "La ficha la fecha en 1928."),
        ("{F} ¿Qué ofrece la tienda de la Evidencia 1?", "Radios en cuotas mensuales", "La ficha lo dice."),
        ("{F} ¿Cuál es la pregunta de investigación?", "¿Cómo cambió la vida cultural en la ciudad entre 1925 y 1930?", "Está escrita al final de la ficha."),
        ("=", "{F} ¿Cuántas funciones ofrece el cine de la Evidencia 2 en dos semanas completas?", "3*6*2", "Se multiplican funciones por día, días de funcionamiento y semanas.", " funciones"),
        ("{F} ¿Qué evidencia sirve para afirmar que había arte nuevo en la ciudad? A) La Evidencia 4 B) La Evidencia 1", "A) La Evidencia 4", "El afiche de la exposición habla de cuadros con figuras de sueños."),
        ("{F} ¿Qué parte de una interpretación dice qué no se puede concluir? A) El límite B) La afirmación", "A) El límite", "El límite marca lo que las fuentes no permiten."),
        ("{F} Una persona escribe: «La Evidencia 3 muestra que un profesor temía por la música que enseñaba». ¿Qué tipo de frase es? A) Descripción apoyada en la fuente B) Generalización sobre todos los profesores", "A) Descripción apoyada en la fuente", "Repite lo que dice la carta y no habla por todos."),
        ("{F} ¿Qué afirmación proporcional se puede sostener con las evidencias? A) La vida cultural de la ciudad incorporó radio, cine y arte nuevo en esos años B) Todos los habitantes iban al cine y escuchaban radio", "A) La vida cultural de la ciudad incorporó radio, cine y arte nuevo en esos años", "Las evidencias muestran presencia de esos elementos, no la participación de todos."),
        ("{F} Para respaldar la afirmación «la vida cultural incorporó radio y cine», ¿qué dos evidencias conviene combinar? A) La Evidencia 1 y la Evidencia 2 B) La Evidencia 3 y la Evidencia 4", "A) La Evidencia 1 y la Evidencia 2", "La 1 habla de radios y la 2 de cine; la carta y el afiche tratan de música y de arte nuevo."),
        ("{F} ¿Por qué la Evidencia 1 no basta para afirmar que mucha gente escuchaba radio?", "Porque un aviso muestra una oferta y no cuántas personas compraron", "Falta evidencia de compras o de uso."),
        ("{F} ¿Qué evidencia nueva reforzaría una afirmación sobre el público del cine? A) Un registro de entradas vendidas B) Otro afiche de arte", "A) Un registro de entradas vendidas", "Mide cuánta gente asistía, que es lo que la ficha no informa."),
        ("{F} Un compañero escribe: «Nadie en 1928 rechazaba el arte nuevo». ¿Qué corrección haces? A) La ficha solo muestra una exposición y una carta con temor, no lo que pensaban todos B) Es correcto porque había una exposición", "A) La ficha solo muestra una exposición y una carta con temor, no lo que pensaban todos", "Evitar «nadie» y «todos»: la carta de 1926 muestra incluso un temor."),
        ("{F} ¿Cuál es el mejor límite para la conclusión? A) No sabemos cuánta gente participaba en cada actividad B) No sabemos si la ciudad cambió", "A) No sabemos cuánta gente participaba en cada actividad", "Las evidencias de la ficha no dan cifras de asistencia ni de compras."),
    ],
    ctx=("Debes escribir un párrafo para un diario escolar sobre la vida cultural de la ciudad entre 1925 y 1930. ¿Cuál es la mejor estructura? A) Afirmación, dos evidencias de distinto tipo y un límite B) Una opinión personal sin fuentes", "A) Afirmación, dos evidencias de distinto tipo y un límite", "Esa estructura es la de una interpretación documentada."),
    sc=[("¿Cuáles son las tres partes de una interpretación documentada?", "Afirmación, evidencia y límite", "Están en el primer párrafo de la explicación."),
        ("¿Qué significa que una conclusión sea proporcional?", "Que no dice más de lo que la evidencia permite", "Así se define en el vocabulario."),
        ("=", "Un cine de ejemplo ofrece 2 funciones al día durante 5 días. ¿Cuántas funciones son?", "2*5", "Se multiplican las funciones diarias por los días.", " funciones")],
    op=("Con la ficha, escribe un párrafo de entre cinco y seis líneas que responda la pregunta de investigación. Debe tener: una afirmación, dos evidencias de distinto tipo citadas por su número y su año, y una frase de límite que empiece con «No podemos saber…». {F}",
        "Entre 1925 y 1930 la vida cultural de la ciudad incorporó radio, cine y arte nuevo. La Evidencia 1 (1929) muestra que se ofrecían radios en cuotas y la Evidencia 2 (1930) muestra tres funciones diarias de cine de lunes a sábado. No podemos saber cuántas personas participaban en cada actividad.",
        ["la afirmación responde la pregunta", "cita dos evidencias de distinto tipo con su año", "incluye un límite explícito"], ["párrafo de cinco o seis líneas"], ["afirmar sin citar evidencia", "usar «todos» o «nadie» sin respaldo"],
        "Pide que diga qué evidencia agregaría para saber cuánta gente participaba."),
    reinforce="Escribe una afirmación, una evidencia y un límite sobre cualquier tema de esta clase, en tres frases cortas.",
    extend="Busca en tu casa una foto antigua o un objeto y escribe qué evidencia entrega y qué no puedes concluir con él.",
)

# ================================================================ OA 02, clase 1
OA = "HI2M OA 02"
F = ("Ficha 1 (crisis del Estado liberal y modelos políticos, 1917-1946). "
     "Estado liberal: gobierno con constitución y elecciones, que interviene poco en la economía y deja que el mercado fije precios y salarios. "
     "Hitos: Revolución rusa, 1917; marcha sobre Roma de Mussolini, 1922; crisis económica mundial que comienza en 1929; Hitler es nombrado canciller de Alemania en 1933; "
     "plan de reformas llamado New Deal en Estados Unidos desde 1933; Ley de Seguridad Social estadounidense, 1935; Estado Novo de Vargas en Brasil, 1937; nacionalización del petróleo en México, 1938; Perón es elegido presidente de Argentina, 1946.")
build(
    OA, 1, F,
    use="Aprenderé a situar la crisis del Estado liberal después de 1917: cuándo ocurrió, qué actores participaron y qué modelos políticos aparecieron en Europa, Estados Unidos y América Latina.",
    prior=["Sé qué fue la Primera Guerra Mundial y que Europa quedó debilitada.", "Sé qué es una constitución y una elección.", "Sé calcular diferencias entre años."],
    explain=[
        "El Estado liberal del siglo XIX tenía constitución, elecciones y poca intervención en la economía. Se pensaba que el mercado, por sí solo, ajustaba precios y salarios. Después de la Primera Guerra Mundial y de la crisis de 1929, muchos desempleados y empresas arruinadas dejaron de confiar en esa idea, y se habló de la crisis del Estado liberal.",
        "Surgieron distintas respuestas. Los totalitarismos, como el nazismo, el fascismo y el comunismo soviético, ponen al Estado y a un partido por encima de las libertades individuales y se oponen a la democracia liberal. En Estados Unidos, el New Deal usó la acción del Estado dentro de una democracia; en América Latina apareció el populismo, y comenzaron a formarse Estados de Bienestar.",
        "Para estudiar este tema hay que fechar los hechos y distinguir actores: gobiernos, partidos, trabajadores, empresarios y líderes. Es un error pensar que el mundo entero cambió de modelo al mismo tiempo, porque cada país respondió de manera distinta.",
    ],
    vocab=[("Estado liberal", "Estado con constitución y elecciones que interviene poco en la economía"), ("totalitarismo", "régimen donde el Estado y un partido controlan casi todos los aspectos de la vida"), ("democracia liberal", "sistema con elecciones libres, libertades individuales y límites al poder"), ("populismo", "forma de gobierno con un líder que apela directamente al pueblo y ofrece medidas sociales"), ("Estado de Bienestar", "Estado que asegura derechos sociales como salud, educación y pensiones")],
    worked=[
        ("Calcular una distancia", "¿Cuántos años pasaron entre la Revolución rusa y la marcha sobre Roma de Mussolini?", ["Tomo 1917 y 1922 de la ficha.", "1922 − 1917 = 5."], "5 años"),
        ("Ubicar un modelo", "El New Deal se aplicó en Estados Unidos desde 1933. ¿Fue un totalitarismo?", ["Fue un plan de reformas dentro de un sistema con elecciones.", "No puso al Estado por encima de las libertades individuales."], "No, fue una respuesta dentro de la democracia"),
    ],
    mistakes=[("Creer que todos los países reaccionaron a la crisis con totalitarismos.", "Se ignoran respuestas democráticas como el New Deal.", "Clasifica cada caso según el sistema político que mantuvo."),
              ("Mezclar fechas y poner el New Deal antes de 1929.", "No se compara cada hito con la línea de tiempo.", "Ordena los hitos por año antes de explicarlos.")],
    T=[
        ("{F} ¿En qué año se produjo la Revolución rusa?", "1917", "La ficha lo indica."),
        ("{F} ¿Quién fue nombrado canciller de Alemania en 1933?", "Hitler", "La ficha lo nombra."),
        ("{F} ¿Qué país aplicó el New Deal?", "Estados Unidos", "La ficha lo ubica en Estados Unidos."),
        ("=", "{F} ¿Cuántos años pasaron entre el comienzo de la crisis económica mundial y la elección de Perón?", "1946-1929", "Se resta el año de la crisis al de la elección de Perón.", " años"),
        ("{F} ¿Qué es un totalitarismo? A) Un régimen donde el Estado y un partido controlan casi todos los aspectos de la vida B) Un régimen con elecciones libres", "A) Un régimen donde el Estado y un partido controlan casi todos los aspectos de la vida", "Así se define en el vocabulario."),
        ("{F} Ordena de más antiguo a más reciente: Estado Novo de Vargas, New Deal, nacionalización del petróleo en México.", "New Deal, Estado Novo de Vargas, nacionalización del petróleo en México", "Los años son 1933, 1937 y 1938."),
        ("{F} ¿Cuál de estos hitos ocurrió antes del comienzo de la crisis económica mundial? A) La marcha sobre Roma de Mussolini B) El New Deal", "A) La marcha sobre Roma de Mussolini", "La marcha es de 1922 y la crisis comienza en 1929; el New Deal es de 1933."),
        ("{F} Un país mantiene elecciones libres y crea un seguro de desempleo para quienes pierden su trabajo. ¿Qué modelo se parece más? A) Estado de Bienestar dentro de una democracia B) Totalitarismo", "A) Estado de Bienestar dentro de una democracia", "Protege derechos sociales sin eliminar las elecciones."),
        ("{F} Un partido único controla la prensa, la escuela y los sindicatos, y se prohíben los demás partidos. ¿Qué modelo se parece más? A) Totalitarismo B) Democracia liberal", "A) Totalitarismo", "El control casi total y el partido único son rasgos totalitarios."),
        ("{F} ¿Por qué la crisis de 1929 llevó a dudar del Estado liberal?", "Porque el mercado por sí solo no evitó desempleo ni quiebras", "El Estado liberal confiaba en que el mercado se ajustara solo."),
        ("{F} Un compañero dice: «En 1933 todos los países se volvieron totalitarios». ¿Se puede sostener? A) No, la ficha muestra también el New Deal en un país con elecciones B) Sí, porque Hitler llegó al poder", "A) No, la ficha muestra también el New Deal en un país con elecciones", "El caso estadounidense contradice la generalización."),
        ("{F} ¿Cuál es el actor principal del populismo latinoamericano en la ficha? A) Un líder que apela al pueblo, como Perón B) Un partido único que prohíbe las elecciones", "A) Un líder que apela al pueblo, como Perón", "Perón es presentado como presidente elegido en Argentina."),
        ("¿Cuál es la mejor pregunta histórica para este tema? A) ¿Cómo respondieron distintos países a la crisis del Estado liberal y de 1929? B) ¿Qué líder fue el más famoso de su época?", "A) ¿Cómo respondieron distintos países a la crisis del Estado liberal y de 1929?", "La pregunta A tiene tema, tiempo y se responde con hechos."),
    ],
    ctx=("Una exposición se titula «Después de 1929 el mundo eligió un solo modelo político». ¿Qué problema tiene? A) Ignora que hubo respuestas totalitarias, democráticas y populistas B) Es correcta, porque la crisis de 1929 solo afectó a Europa", "A) Ignora que hubo respuestas totalitarias, democráticas y populistas", "La ficha muestra modelos distintos en países distintos."),
    sc=[("¿Qué dejaba hacer al mercado el Estado liberal?", "Fijar precios y salarios", "Así se define en la ficha."),
        ("¿Qué es el populismo?", "Una forma de gobierno con un líder que apela directamente al pueblo y ofrece medidas sociales", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es un totalitarismo?", "Un régimen donde el Estado y un partido controlan casi todos los aspectos de la vida", "Así se define en el vocabulario de la clase.")],
    op=("Dibuja una línea de tiempo de 1917 a 1946 con los nueve hitos de la ficha. Marca la crisis de 1929 con un color propio como punto de partida común y pinta los otros ocho hitos con tres colores: hechos ligados a regímenes totalitarios (Revolución rusa y su régimen comunista, marcha sobre Roma, Hitler), respuestas dentro de la democracia liberal y casos latinoamericanos con rasgos populistas o nacionalistas. Escribe una frase que explique la diferencia entre los tres grupos. {F}",
        "Crisis de 1929: color propio. Ligados a regímenes totalitarios: Revolución rusa (1917), marcha sobre Roma (1922), Hitler (1933). Democráticas: New Deal (1933), Ley de Seguridad Social (1935). Latinoamericanos con rasgos populistas o nacionalistas: Estado Novo (1937), petróleo mexicano (1938), Perón (1946). Frase: el primer grupo concentra el poder en un partido, el segundo reforma el Estado con elecciones y el tercero apela al pueblo con medidas sociales y nacionalismo económico.",
        ["ubica los hitos en orden", "clasifica los hitos en tres grupos", "explica la diferencia entre los grupos"], ["línea de tiempo", "frase explicativa"], ["poner el New Deal entre los totalitarismos", "no usar la escala de tiempo"],
        "Pide que explique por qué un país pudo ser democrático y también intervenir en la economía."),
    reinforce="Explica en voz alta qué es el Estado liberal y por qué se dice que entró en crisis.",
    extend="Anota una medida social actual de tu país (por ejemplo, un seguro de salud) y di si te parece de un Estado liberal o de bienestar.",
)

# ================================================================ OA 02, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente 1, carta de un obrero desempleado a su hermano, 1932: «Llevo ocho meses sin trabajo. La fábrica cerró y el patrón dice que el mercado se arreglará solo. Mientras tanto, mis hijos comen una vez al día.» "
     "Fuente 2, discurso de un líder autoritario, 1933: «Solo un partido y un líder pueden salvar a la nación; los que discuten, retrasan la salvación.» "
     "Fuente 3, mensaje radial de un presidente democrático, 1934: «El Gobierno dará empleo en obras públicas y protegerá los ahorros, pero respetará las elecciones y la libertad de prensa.»")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre la crisis de entreguerras: quién habla, para qué, qué modelo defiende y qué se puede concluir.",
    prior=["Sé situar la crisis del Estado liberal y los modelos políticos.", "Sé separar descripción e interpretación.", "Sé que una fuente tiene un propósito."],
    explain=[
        "Al interrogar una fuente política se pregunta: quién habla, a quién le habla y qué quiere lograr. Un discurso de un líder busca convencer o movilizar; un mensaje de un presidente busca explicar medidas; una carta privada muestra una experiencia personal. Las tres son útiles, pero informan cosas distintas.",
        "En los discursos aparecen palabras que revelan el modelo. Cuando un líder dice que solo un partido y un líder pueden salvar a la nación, expresa una idea totalitaria porque rechaza la discusión. Cuando un presidente promete empleo y respeto a las elecciones, defiende una respuesta democrática con intervención del Estado. Una carta de un desempleado muestra el impacto en la vida cotidiana.",
        "Hay que cuidar la generalización. La carta de un obrero no prueba cuántos desempleados había; el discurso de un líder no prueba que el pueblo estuviera de acuerdo; el mensaje de un presidente no prueba que las medidas funcionaran. Cada fuente muestra una promesa, una experiencia o una intención, no el resultado final.",
    ],
    vocab=[("autoritario", "que concentra el poder y limita la discusión y las libertades"), ("obras públicas", "construcciones financiadas por el Estado, como caminos o puentes"), ("movilizar", "llamar a muchas personas a actuar por una causa"), ("experiencia cotidiana", "lo que una persona vive en su vida diaria"), ("intención", "aquello que una persona quiere lograr con su mensaje")],
    worked=[
        ("Identificar el propósito", "La Fuente 3 promete empleo en obras públicas. ¿Cuál es su propósito más probable?", ["Un mensaje radial de un presidente explica medidas.", "Busca informar y ganar apoyo."], "Explicar medidas y ganar apoyo"),
        ("Medir un tiempo", "El obrero de la Fuente 1 lleva ocho meses sin trabajo. ¿Cuántos meses faltan para completar dos años?", ["Dos años son 24 meses.", "24 − 8 = 16."], "16 meses"),
    ],
    mistakes=[("Creer que el discurso de un líder muestra lo que pensaba el pueblo.", "Un discurso expresa la intención del líder, no la opinión de todos.", "Escribe «el líder afirma que…» y busca otras voces."),
              ("Tomar una promesa como un resultado.", "El mensaje del presidente dice qué hará, no lo que logró.", "Pide evidencia de resultados antes de afirmar que funcionó.")],
    T=[
        ("{F} ¿Cuántos meses lleva sin trabajo el obrero de la Fuente 1?", "Ocho meses", "La carta lo dice."),
        ("{F} ¿En qué año es la Fuente 2?", "1933", "La ficha la fecha en 1933."),
        ("{F} ¿Qué promete el presidente de la Fuente 3 además de empleo?", "Proteger los ahorros", "El mensaje lo dice."),
        ("=", "{F} ¿Cuántos años pasaron entre la carta del obrero y el mensaje del presidente?", "1934-1932", "Se resta el año de la carta al del mensaje.", " años"),
        ("{F} ¿Qué tipo de texto es la Fuente 1? A) Una carta privada B) Un discurso público", "A) Una carta privada", "Es una carta de un obrero a su hermano."),
        ("{F} ¿Qué frase de la Fuente 2 expresa una idea totalitaria? A) «Solo un partido y un líder pueden salvar a la nación» B) «Mañana hay sol»", "A) «Solo un partido y un líder pueden salvar a la nación»", "Rechaza la discusión y concentra el poder en un partido y un líder."),
        ("{F} ¿Qué modelo defiende la Fuente 3? A) Democracia con intervención del Estado B) Totalitarismo", "A) Democracia con intervención del Estado", "Promete empleo estatal y respeta elecciones y libertad de prensa."),
        ("{F} ¿Cuál frase describe la Fuente 1? A) El obrero dice que su familia come una vez al día B) La crisis afectó a todos los obreros", "A) El obrero dice que su familia come una vez al día", "La primera frase repite la carta; la segunda generaliza."),
        ("{F} ¿Qué fuente sirve más para entender cómo vivió la crisis una familia? A) La Fuente 1 B) La Fuente 2", "A) La Fuente 1", "La carta cuenta una experiencia cotidiana."),
        ("{F} ¿Por qué la Fuente 3 no prueba que las medidas del presidente dieran empleo?", "Porque es una promesa y no un registro de resultados", "El mensaje dice qué hará el Gobierno, no lo que logró."),
        ("{F} ¿Qué rasgo de la Fuente 2 muestra que rechaza la democracia liberal?", "Que pide un solo partido y un solo líder y dice que quienes discuten retrasan la salvación", "Una democracia liberal acepta la discusión y varios partidos."),
        ("{F} Un compañero escribe: «La Fuente 1 prueba que en 1932 todos los trabajadores estaban desempleados». ¿Qué corrección haces? A) Muestra el caso de un obrero, no de todos B) Es correcto porque la carta es de 1932", "A) Muestra el caso de un obrero, no de todos", "Una carta personal no permite generalizar."),
        ("{F} ¿Qué fuente adicional ayudaría a saber cuánta gente quedó sin trabajo? A) Una estadística oficial de empleo de la época B) Otro discurso de un líder", "A) Una estadística oficial de empleo de la época", "Una estadística entrega cifras; otro discurso repite la intención política."),
    ],
    ctx=("Para un trabajo sobre las respuestas a la crisis debes elegir entre usar solo el discurso autoritario o las tres fuentes de la ficha. ¿Qué elección da una conclusión más ajustada? A) Las tres, porque muestran una experiencia y dos modelos políticos B) Solo el discurso, porque es el más fuerte", "A) Las tres, porque muestran una experiencia y dos modelos políticos", "Varias voces permiten una conclusión más completa."),
    sc=[("¿Qué se pregunta primero al interrogar una fuente?", "Quién habla, a quién y con qué propósito", "Son las preguntas de procedencia de la explicación."),
        ("¿Qué muestra una carta privada?", "La experiencia o el pensamiento de una persona", "No representa por sí sola a un grupo."),
        ("Un presidente promete empleo en obras públicas en 1934. ¿Qué evidencia permitiría afirmar que cumplió? A) Un registro de trabajadores contratados en esas obras B) Otro discurso del mismo presidente", "A) Un registro de trabajadores contratados en esas obras", "Una promesa no es un resultado; un registro lo mide.")],
    op=("Elige dos de las tres fuentes de la ficha. Escribe una tabla con: autor y fecha de cada una, su propósito y qué modelo o experiencia muestra. Termina con una frase sobre lo que NO puedes concluir con esas dos fuentes. {F}",
        "Fuente 1: obrero, 1932; propósito: contar su situación; muestra el impacto de la crisis. Fuente 3: presidente, 1934; propósito: explicar medidas; muestra una democracia con intervención del Estado. No puedo concluir cuántas personas quedaron sin trabajo ni si las medidas funcionaron.",
        ["contextualiza ambas fuentes", "identifica propósito y modelo", "señala un límite"], ["tabla con dos fuentes", "frase de límite"], ["confundir promesa con resultado", "generalizar a toda la sociedad"],
        "Pide que cuente qué otra fuente buscaría para comparar."),
    reinforce="Explica con tus palabras por qué un discurso no prueba lo que pensaba la mayoría.",
    extend="Lee un titular actual y di si expresa un hecho, una intención o una opinión.",
)

# ================================================================ OA 02, clase 3
F = ("Ficha 3 (cuadro comparativo, resumen escolar). "
     "Democracia liberal: elecciones libres, varios partidos, prensa libre y límites al poder. "
     "Nazismo (Alemania): partido único, líder con poder total, racismo y antisemitismo como política de Estado, y control de la prensa y la educación. "
     "Fascismo (Italia): partido único, Estado y nación por sobre el individuo, nacionalismo y uso de la fuerza contra opositores. "
     "Comunismo soviético (URSS): partido único, propiedad estatal de los medios de producción y economía planificada por el Estado. "
     "Populismo latinoamericano (por ejemplo Brasil y Argentina): líder que se dirige a trabajadores y sectores populares, medidas sociales y nacionalismo económico. "
     "Escalas: Europa, Estados Unidos y América Latina.")
build(
    OA, 3, F,
    use="Aprenderé a comparar los modelos políticos de entreguerras en distintas escalas: qué comparten, en qué se diferencian y por qué no todos son iguales.",
    prior=["Sé situar la crisis del Estado liberal.", "Sé qué es una perspectiva y una escala.", "Sé leer un cuadro comparativo."],
    explain=[
        "Comparar modelos políticos implica buscar rasgos comunes y diferencias. El nazismo, el fascismo y el comunismo soviético tuvieron un partido único y gran control del Estado, pero sus ideas eran distintas: el nazismo se basó en el racismo, el fascismo en el Estado y la nación por sobre el individuo, y el comunismo en la propiedad estatal y la economía planificada. Por eso no se dice que eran lo mismo.",
        "Frente a ellos, la democracia liberal conserva elecciones, varios partidos y prensa libre. En América Latina apareció el populismo: un líder se dirige a trabajadores y sectores populares con medidas sociales y nacionalismo económico, a veces dentro de gobiernos democráticos y a veces con rasgos autoritarios. Es un modelo distinto del totalitarismo europeo.",
        "La escala cambia la comparación: en Europa el centro fue la crisis del Estado liberal y los totalitarismos; en Estados Unidos, la acción del Estado dentro de la democracia; en América Latina, el fin de un modelo basado en exportar materias primas. Comparar exige nombrar siempre el país y el período.",
    ],
    vocab=[("nazismo", "régimen de Alemania basado en un partido único, un líder, el racismo y el control del Estado"), ("fascismo", "régimen de Italia que pone al Estado y a la nación por sobre el individuo"), ("comunismo soviético", "régimen de la URSS con partido único, propiedad estatal y economía planificada"), ("economía planificada", "economía donde el Estado decide qué se produce y a qué precio"), ("nacionalismo económico", "política que busca proteger y controlar la economía del propio país")],
    worked=[
        ("Rasgo común", "¿Qué rasgo comparten nazismo, fascismo y comunismo soviético según la ficha?", ["Reviso las tres descripciones.", "Las tres mencionan un partido único."], "Un partido único"),
        ("Diferencia de ideas", "¿Qué distingue al comunismo soviético del nazismo?", ["El comunismo se basa en la propiedad estatal y la economía planificada.", "El nazismo se basa en el racismo y el control del Estado."], "El comunismo soviético se basa en la propiedad estatal y la economía planificada; el nazismo en el racismo"),
    ],
    mistakes=[("Decir que nazismo, fascismo y comunismo eran la misma ideología.", "Se confunde el rasgo de partido único con las ideas que los guían.", "Compara a la vez lo que comparten y lo que los diferencia."),
              ("Aplicar el modelo totalitario europeo al populismo latinoamericano sin matices.", "El populismo ofreció medidas sociales y a veces mantuvo elecciones.", "Nombra el país y revisa si había elecciones y partidos.")],
    T=[
        ("{F} ¿Qué régimen aparece en Italia en la ficha?", "El fascismo", "La ficha lo ubica en Italia."),
        ("{F} ¿Qué país corresponde al comunismo soviético?", "La URSS", "La ficha lo nombra."),
        ("{F} ¿A quién se dirige el líder populista según la ficha?", "A trabajadores y sectores populares", "Así se describe el populismo."),
        ("{F} ¿Qué rasgo comparten nazismo, fascismo y comunismo soviético? A) Un partido único B) Elecciones libres con varios partidos", "A) Un partido único", "Las tres descripciones nombran un partido único."),
        ("{F} ¿Qué idea distingue al nazismo de los otros dos regímenes totalitarios? A) El racismo y el antisemitismo como política de Estado B) La propiedad estatal de los medios de producción", "A) El racismo y el antisemitismo como política de Estado", "La ficha lo presenta como rasgo propio del nazismo."),
        ("{F} ¿Qué modelo conserva prensa libre y varios partidos? A) La democracia liberal B) El fascismo", "A) La democracia liberal", "La ficha lo describe así."),
        ("{F} Un régimen decide qué se produce y a qué precio en cada fábrica. ¿Qué característica es? A) Economía planificada B) Nacionalismo económico", "A) Economía planificada", "El Estado decide la producción: esa es la economía planificada de la ficha."),
        ("{F} Un gobierno latinoamericano promete mejores salarios y toma el control de un recurso nacional. ¿Qué modelo se parece más? A) Populismo B) Comunismo soviético", "A) Populismo", "Une medidas sociales y nacionalismo económico."),
        ("{F} Un régimen declara que la nación está por encima de cada persona y reprime a sus opositores. ¿Qué modelo se parece más? A) Fascismo B) Democracia liberal", "A) Fascismo", "Así describe la ficha al fascismo."),
        ("{F} ¿Por qué es un error decir que nazismo y comunismo soviético eran iguales?", "Porque tenían ideas distintas aunque ambos tuvieran partido único", "Uno se basaba en el racismo y el otro en la propiedad estatal."),
        ("{F} ¿Qué cambia al comparar Europa con América Latina? A) En Europa se discutía la crisis del Estado liberal con totalitarismos y en América Latina el fin del modelo de exportar materias primas B) En ambas ocurrió exactamente lo mismo", "A) En Europa se discutía la crisis del Estado liberal con totalitarismos y en América Latina el fin del modelo de exportar materias primas", "La explicación distingue las escalas."),
        ("{F} Un compañero afirma: «El populismo latinoamericano fue igual al nazismo». ¿Qué corrección haces? A) Tenían objetivos y métodos distintos: el populismo ofreció medidas sociales y no se basó en el racismo B) Es correcto porque ambos tenían líder", "A) Tenían objetivos y métodos distintos: el populismo ofreció medidas sociales y no se basó en el racismo", "Tener un líder no hace iguales a dos regímenes."),
        ("{F} ¿Qué rasgo permitiría decir que un gobierno no es una democracia liberal? A) Prohíbe los demás partidos y la prensa libre B) Convoca a elecciones cada pocos años", "A) Prohíbe los demás partidos y la prensa libre", "Sin partidos ni prensa libre desaparece la democracia liberal."),
    ],
    ctx=("Una profesora pide un mural de tres columnas para comparar regímenes. ¿Qué título corresponde a la tercera columna si las dos primeras son «Nazismo» y «Fascismo»? A) Comunismo soviético B) Democracia liberal", "A) Comunismo soviético", "Las tres son regímenes con partido único; la democracia liberal tendría rasgos opuestos."),
    sc=[("¿Qué es una economía planificada?", "Una economía donde el Estado decide qué se produce y a qué precio", "Así se define en el vocabulario."),
        ("¿Qué partido tienen los regímenes totalitarios de la ficha?", "Un partido único", "Las tres descripciones lo nombran."),
        ("¿Cuál es una diferencia entre el fascismo y el comunismo soviético según la ficha? A) El fascismo pone la nación por sobre el individuo y el comunismo se basa en la propiedad estatal B) El fascismo tenía varios partidos y el comunismo uno solo", "A) El fascismo pone la nación por sobre el individuo y el comunismo se basa en la propiedad estatal", "Ambos tienen partido único; difieren en sus ideas.")],
    op=("Escribe un cuadro de tres filas (nazismo, comunismo soviético, populismo latinoamericano) y tres columnas (país, rasgo principal, un rasgo que lo distingue de los otros dos). Después escribe una frase que empiece con «Aunque…» y explique por qué no se pueden tratar como iguales. {F}",
        "Nazismo: Alemania; partido único; racismo como política de Estado. Comunismo soviético: URSS; partido único; propiedad estatal y economía planificada. Populismo: Brasil y Argentina; líder que apela a trabajadores; medidas sociales y nacionalismo económico. Frase: «Aunque los dos primeros tuvieron partido único, sus ideas eran distintas».",
        ["completa las nueve celdas", "diferencia cada modelo", "justifica por qué no son iguales"], ["cuadro completo", "frase con «Aunque…»"], ["repetir el mismo rasgo en las tres filas", "no nombrar país ni período"],
        "Pide que explique qué modelo se parece más a una democracia liberal y por qué."),
    reinforce="Explica en voz alta una semejanza y una diferencia entre fascismo y comunismo soviético.",
    extend="Elige un país y pregunta a una persona mayor qué entiende por «democracia». Anota su respuesta en una frase.",
)

# ================================================================ OA 02, clase 4
F = ("Ficha 4 (causas, cambios y continuidades; datos de ejemplo cuando se indica). "
     "Causas de la crisis liberal: consecuencias de la Primera Guerra Mundial (muertos, deudas, ciudades destruidas); tratado de Versalles, 1919, que impuso pagos a Alemania; "
     "hiperinflación alemana de 1923 (los precios subían tan rápido que el dinero perdía casi todo su valor); caída de la bolsa de Nueva York en octubre de 1929 y cierre de bancos y fábricas; miedo a una revolución como la rusa. "
     "Cambios: el Estado empieza a intervenir más en la economía, en el empleo y en la protección social. "
     "Continuidades: sigue habiendo desigualdad; en varios países las mujeres no votan; muchas economías siguen exportando materias primas. "
     "Dato de ejemplo: una fábrica de 500 trabajadores despide a 200.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar las causas de la crisis liberal con los cambios y continuidades que produjo, y a no confundir una causa con un detonante.",
    prior=["Sé situar los modelos políticos y compararlos.", "Sé que un hecho tiene varias causas.", "Sé calcular restas y porcentajes sencillos."],
    explain=[
        "La crisis del Estado liberal tuvo causas de largo plazo y un detonante. Las causas de largo plazo fueron las consecuencias de la Primera Guerra, los pagos que el tratado de Versalles impuso a Alemania, la inflación y el miedo a una revolución. El detonante fue la caída de la bolsa de Nueva York en 1929, que desencadenó cierres de bancos y fábricas.",
        "La hiperinflación es una subida tan rápida de precios que el dinero casi no vale. En Alemania en 1923 destruyó ahorros y generó descontento. Por eso se dice que en las sociedades con miedo y pobreza crecen las propuestas que prometen orden y soluciones rápidas, aunque no se puede decir que la crisis causara por sí sola el nazismo.",
        "Entre los cambios están una mayor intervención del Estado en la economía, el empleo y la protección social. Entre las continuidades están la desigualdad, el voto limitado para las mujeres en varios países y las economías que dependían de exportar materias primas. Un cambio no borra todo lo anterior.",
    ],
    vocab=[("detonante", "hecho que desencadena una crisis que ya tenía causas previas"), ("hiperinflación", "alza tan rápida de precios que el dinero casi no conserva valor"), ("tratado de Versalles", "acuerdo de paz de 1919 que impuso pagos a Alemania"), ("intervención del Estado", "acción del gobierno en la economía y la protección social"), ("largo plazo", "causas que se acumulan durante años antes de una crisis")],
    worked=[
        ("Distinguir detonante y causa", "¿La caída de la bolsa de 1929 fue causa de largo plazo o detonante?", ["Se produjo en octubre de 1929 y desencadenó cierres de bancos.", "La ficha la presenta como el hecho que dispara la crisis."], "Detonante"),
        ("Calcular un efecto", "En una fábrica de ejemplo de 800 trabajadores se despide a 300. ¿Cuántos quedan?", ["Tomo los trabajadores iniciales.", "800 − 300 = 500."], "500 trabajadores"),
    ],
    mistakes=[("Decir que la caída de la bolsa fue la única causa de todos los problemas.", "Se ignoran las causas de largo plazo como la guerra y los pagos de Versalles.", "Separa causas de largo plazo y detonante."),
              ("Afirmar que la crisis causó por sí sola el nazismo.", "Pasó otras cosas, como el miedo, la propaganda y decisiones de personas.", "Usa «contribuyó a» y no «causó» sin evidencia.")],
    T=[
        ("{F} ¿En qué año se firmó el tratado de Versalles?", "1919", "La ficha lo indica."),
        ("{F} ¿Qué fue la hiperinflación alemana de 1923?", "Una subida tan rápida de precios que el dinero casi perdía su valor", "La ficha la define así."),
        ("{F} ¿Qué hecho de octubre de 1929 se presenta como detonante?", "La caída de la bolsa de Nueva York", "La ficha lo nombra."),
        ("=", "{F} ¿Cuántos trabajadores quedan en la fábrica de la ficha después de los despidos?", "500-200", "Se resta el número de despedidos al total.", " trabajadores"),
        ("{F} ¿Qué impuso el tratado de Versalles según la ficha? A) Pagos a Alemania B) Pagos a Estados Unidos", "A) Pagos a Alemania", "La ficha dice que impuso pagos a Alemania, país derrotado en la guerra."),
        ("{F} ¿Cuál de estas es una causa de largo plazo? A) Las consecuencias de la Primera Guerra Mundial B) La caída de la bolsa de 1929", "A) Las consecuencias de la Primera Guerra Mundial", "La guerra preparó la crisis; la caída de la bolsa la desencadenó."),
        ("=", "{F} ¿Qué porcentaje de los trabajadores de la fábrica de la ficha fue despedido?", "200*100/500", "Se divide lo despedido por el total y se multiplica por 100.", " %"),
        ("{F} Un país mantiene la desigualdad y las mujeres no votan, aunque el Estado crea empleo público. ¿Qué elementos son continuidad? A) La desigualdad y el voto limitado B) La creación de empleo público", "A) La desigualdad y el voto limitado", "La ficha enumera esas continuidades; el empleo público es un cambio."),
        ("{F} El Estado empieza a pagar subsidios a quienes pierden su empleo. ¿Qué es eso? A) Un cambio: más intervención del Estado B) Una continuidad del Estado liberal", "A) Un cambio: más intervención del Estado", "El Estado liberal interviene poco; el subsidio es un cambio."),
        ("{F} ¿Por qué la hiperinflación de 1923 pudo aumentar el descontento en Alemania?", "Porque destruyó ahorros y el dinero perdió su valor", "La ficha la define como pérdida casi total del valor del dinero."),
        ("{F} ¿Qué combinación de causas permite sostener que no hubo una sola causa de la crisis liberal? A) Consecuencias de la guerra, pagos de Versalles, hiperinflación, miedo a una revolución y caída de la bolsa B) Solo la caída de la bolsa de 1929", "A) Consecuencias de la guerra, pagos de Versalles, hiperinflación, miedo a una revolución y caída de la bolsa", "La ficha nombra varias causas combinadas, no una sola."),
        ("{F} Un compañero escribe: «La caída de la bolsa en 1929 causó por sí sola el nazismo». ¿Qué corrección haces? A) La crisis contribuyó, pero hubo otras causas, como el descontento previo y decisiones de personas B) Es correcto porque ocurrió antes de 1933", "A) La crisis contribuyó, pero hubo otras causas, como el descontento previo y decisiones de personas", "Ocurrir antes no prueba una causa única."),
        ("{F} ¿Cuál es la mejor síntesis? A) Hubo causas de largo plazo y un detonante, con cambios en el rol del Estado y continuidades de desigualdad B) Todo cambió en octubre de 1929", "A) Hubo causas de largo plazo y un detonante, con cambios en el rol del Estado y continuidades de desigualdad", "Reúne causas, cambios y continuidades."),
    ],
    ctx=("Un afiche escolar dice: «La caída de la bolsa de 1929 explica todo lo que pasó después». ¿Qué problema tiene? A) Ignora causas de largo plazo y continuidades B) Usa fechas equivocadas", "A) Ignora causas de largo plazo y continuidades", "La ficha muestra otras causas y hechos que seguían igual."),
    sc=[("¿Qué es un detonante?", "El hecho que desencadena una crisis que ya tenía causas previas", "Así se define en el vocabulario."),
        ("¿Qué es la hiperinflación?", "Un alza tan rápida de precios que el dinero casi no conserva valor", "Así se define en la clase."),
        ("=", "En una fábrica de ejemplo hay 1.000 trabajadores y se despide a 350. ¿Cuántos quedan?", "1000-350", "Se resta el número de despedidos.", " trabajadores")],
    op=("Dibuja un esquema con «crisis del Estado liberal» al centro. A la izquierda escribe tres causas de largo plazo, arriba el detonante y a la derecha un cambio y una continuidad. Debajo escribe una frase con «contribuyó a…» que evite decir que algo fue la única causa. {F}",
        "Causas de largo plazo: consecuencias de la guerra, pagos de Versalles, hiperinflación. Detonante: caída de la bolsa de 1929. Cambio: el Estado interviene más. Continuidad: la desigualdad. Frase: la hiperinflación contribuyó a aumentar el descontento, pero no fue la única causa.",
        ["distingue causa de largo plazo y detonante", "incluye un cambio y una continuidad", "evita causas únicas"], ["esquema", "frase con «contribuyó a…»"], ["poner el detonante como causa de largo plazo", "usar «causó por sí sola»"],
        "Pide que explique por qué una coincidencia en el tiempo no basta para probar una causa."),
    reinforce="Explica a alguien de tu casa la diferencia entre una causa de largo plazo y un detonante.",
    extend="Piensa en una discusión que empezó por un hecho pequeño y di qué causas anteriores la hicieron posible.",
)

# ================================================================ OA 02, clase 5
F = ("Ficha 5 (populismo y primeros Estados de Bienestar; evidencias de ejemplo y hechos). "
     "Hechos: en 1935 Estados Unidos aprueba una ley de seguridad social con pensiones de vejez y seguro de desempleo; en 1938 México nacionaliza su petróleo; en 1937 Vargas instaura el Estado Novo en Brasil; en 1946 Perón es elegido presidente de Argentina. "
     "Evidencia 1, discurso de ejemplo de un líder populista, 1947: «Los trabajadores serán el centro de la nación y el Estado cuidará su salario.» "
     "Evidencia 2, editorial de ejemplo de un diario opositor, 1947: «El líder concentra demasiado poder y silencia a quienes piensan distinto.» "
     "Evidencia 3, carta de ejemplo de una obrera, 1948: «Gracias a las nuevas leyes tengo vacaciones pagadas por primera vez.» "
     "Pregunta de investigación: ¿qué aportó y qué límites tuvo el populismo en América Latina?")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada sobre el populismo latinoamericano y los primeros Estados de Bienestar, con evidencias que apoyan y evidencias que limitan.",
    prior=["Sé qué es el populismo y el Estado de Bienestar.", "Sé que una interpretación tiene afirmación, evidencia y límite.", "Sé reconocer perspectivas distintas."],
    explain=[
        "Un Estado de Bienestar es un Estado que asegura derechos sociales: pensiones, seguro de desempleo, salud y educación. En 1935 Estados Unidos aprobó una ley de seguridad social, y se considera uno de los inicios de estas políticas. En América Latina, líderes populistas como Vargas y Perón ampliaron derechos laborales y sociales.",
        "El populismo tiene aportes y críticas. Entre los aportes, muchos trabajadores obtuvieron mejoras como vacaciones pagadas o leyes laborales. Entre las críticas, los opositores señalaron que el líder concentraba demasiado poder y silenciaba a quienes pensaban distinto. Una buena interpretación muestra ambas caras con fuentes de procedencia distinta.",
        "Para construir la interpretación se sigue la regla del tema anterior: afirmación, evidencias y límite. La afirmación debe responder la pregunta; las evidencias se citan por autor y fecha; el límite dice que una carta o un editorial muestran una voz, no a toda la sociedad. Y se evitan palabras absolutas como «todos» o «nadie».",
    ],
    vocab=[("derechos sociales", "derechos como salud, educación, pensiones y condiciones de trabajo dignas"), ("seguro de desempleo", "pago temporal a quien pierde su empleo"), ("nacionalizar", "pasar un recurso o empresa a manos del Estado"), ("opositor", "persona o grupo que se opone al gobierno"), ("concentrar el poder", "reunir las decisiones en una sola persona o grupo")],
    worked=[
        ("Elegir evidencia de aporte", "¿Qué evidencia de la ficha apoya que el populismo mejoró derechos laborales?", ["Busco una evidencia sobre trabajadores.", "La carta de la obrera menciona vacaciones pagadas por primera vez."], "La Evidencia 3"),
        ("Calcular un plazo", "¿Cuántos años pasaron entre el Estado Novo y la elección de Perón?", ["Tomo 1937 y 1946.", "1946 − 1937 = 9."], "9 años"),
    ],
    mistakes=[("Usar solo evidencias favorables a un líder.", "Se ignora a los opositores y la concentración del poder.", "Incluye al menos una evidencia que limite la afirmación."),
              ("Afirmar que todos los trabajadores mejoraron por la carta de una obrera.", "Una carta muestra una experiencia personal.", "Escribe «una obrera cuenta que…» y no «todos mejoraron».")],
    T=[
        ("{F} ¿Qué país nacionalizó su petróleo en 1938?", "México", "La ficha lo indica."),
        ("{F} ¿Qué derecho menciona la obrera de la Evidencia 3?", "Vacaciones pagadas", "La carta lo dice."),
        ("{F} ¿Qué critica el editorial de la Evidencia 2?", "Que el líder concentra demasiado poder y silencia a quienes piensan distinto", "El editorial lo dice."),
        ("{F} ¿Cuál de estos hechos de la ficha es anterior a la nacionalización del petróleo en México? A) La ley de seguridad social estadounidense B) La elección de Perón", "A) La ley de seguridad social estadounidense", "La ley es de 1935, la nacionalización de 1938 y la elección de Perón de 1946."),
        ("{F} ¿Qué es nacionalizar? A) Pasar un recurso o empresa a manos del Estado B) Vender una empresa a extranjeros", "A) Pasar un recurso o empresa a manos del Estado", "Así se define en el vocabulario."),
        ("{F} ¿Qué evidencia apoya que el populismo trajo mejoras sociales? A) La Evidencia 3 B) La Evidencia 2", "A) La Evidencia 3", "La carta de la obrera cuenta una mejora concreta."),
        ("{F} ¿Qué evidencia limita la afirmación «el populismo fue completamente positivo»? A) La Evidencia 2 B) La Evidencia 3", "A) La Evidencia 2", "El editorial opositor critica la concentración de poder."),
        ("{F} Una persona escribe: «Una obrera cuenta que obtuvo vacaciones pagadas». ¿Qué tipo de frase es? A) Descripción de la fuente B) Generalización sobre todos los obreros", "A) Descripción de la fuente", "Repite lo que dice la carta sin generalizar."),
        ("{F} ¿Cuál es una afirmación proporcional? A) El populismo amplió derechos laborales para algunos trabajadores y fue criticado por concentrar poder B) Todos los trabajadores vivieron mejor y nadie criticó al líder", "A) El populismo amplió derechos laborales para algunos trabajadores y fue criticado por concentrar poder", "Usa las dos evidencias y evita «todos» y «nadie»."),
        ("{F} ¿Por qué la Evidencia 1 no basta para saber qué logró el populismo?", "Porque es un discurso que expresa intención y no resultados", "Un discurso promete, no mide efectos."),
        ("{F} ¿Qué diferencia hay entre el discurso del líder y el editorial opositor?", "El discurso defiende al líder y el editorial lo critica, con intereses distintos", "Las dos fuentes tienen perspectivas opuestas por su procedencia."),
        ("{F} Un compañero escribe: «Con la Evidencia 3 está probado que todo el país tenía vacaciones pagadas». ¿Qué corrección haces? A) Es la experiencia de una obrera, no de todo el país B) Es correcto porque la carta es de 1948", "A) Es la experiencia de una obrera, no de todo el país", "Una carta no permite generalizar."),
        ("{F} ¿Qué evidencia nueva ayudaría más a saber cuánta gente obtuvo derechos? A) Una estadística oficial sobre trabajadores cubiertos por las leyes B) Otro discurso del líder", "A) Una estadística oficial sobre trabajadores cubiertos por las leyes", "Una estadística mide el alcance; otro discurso repite la intención."),
    ],
    ctx=("Para un trabajo sobre populismo, una compañera propone usar solo discursos del líder. ¿Cuál es la mejor respuesta? A) Conviene sumar fuentes opositoras y testimonios de trabajadores para equilibrar B) Es suficiente porque el líder sabe más", "A) Conviene sumar fuentes opositoras y testimonios de trabajadores para equilibrar", "Varias perspectivas dan una conclusión más sólida."),
    sc=[("¿Qué es un Estado de Bienestar?", "Un Estado que asegura derechos sociales como pensiones, salud y educación", "Así se define en la explicación."),
        ("¿Qué partes tiene una interpretación documentada?", "Afirmación, evidencia y límite", "Está en la explicación."),
        ("En Historia: ¿qué es un opositor?", "Una persona o grupo que se opone al gobierno", "Así se define en el vocabulario de la clase.")],
    op=("Escribe un párrafo de cinco o seis líneas que responda la pregunta de investigación de la ficha. Incluye una afirmación, una evidencia que la apoye, una evidencia que la limite, y una frase final que empiece con «No podemos saber…». {F}",
        "El populismo latinoamericano aportó derechos laborales a muchos trabajadores, pero fue criticado por concentrar poder. La Evidencia 3 (1948) muestra vacaciones pagadas y la Evidencia 2 (1947) critica la concentración de poder. No podemos saber cuántos trabajadores recibieron esos beneficios.",
        ["la afirmación responde la pregunta", "usa una evidencia a favor y una que limita", "incluye una frase de límite"], ["párrafo de cinco o seis líneas"], ["usar solo evidencia favorable", "generalizar con una sola carta"],
        "Pide que cuente qué fuente nueva le gustaría tener para decidir mejor."),
    reinforce="Escribe una afirmación, una evidencia y un límite sobre el New Deal o el populismo, en tres frases.",
    extend="Anota un derecho laboral actual en Chile (por ejemplo, vacaciones) y pregunta a una persona de tu casa si recuerda cuándo se introdujo.",
)

# ================================================================ OA 02, clase 6
F = ("Ficha 6 (debate sobre consecuencias y límites, datos de ejemplo). "
     "Posición A: «Cuando el mercado falla, el Estado debe intervenir en el empleo y la protección social, aunque eso implique gastar más.» "
     "Posición B: «El Estado debe intervenir lo menos posible para no frenar la libertad económica, y las crisis se superan con tiempo.» "
     "Posición C: «Solo un partido fuerte y un líder pueden resolver la crisis; las libertades pueden esperar.» "
     "Hechos: los regímenes totalitarios eliminaron o limitaron partidos, prensa libre y elecciones libres; las democracias que usaron políticas sociales mantuvieron elecciones; el populismo latinoamericano mezcló mejoras sociales con concentración del poder. "
     "Dato de ejemplo: un programa de empleo público contrata a 2.000 personas con un sueldo mensual de $400.000 cada una.")
build(
    OA, 6, F,
    use="Aprenderé a debatir las consecuencias de los distintos modelos políticos, con argumentos que usan hechos y reconocen sus límites.",
    prior=["Sé comparar modelos políticos y sus causas.", "Sé construir una interpretación con evidencias.", "Sé calcular multiplicaciones con cifras grandes."],
    explain=[
        "Debatir no es discutir: es defender una posición con razones y evidencias, y escuchar las de otros. Un argumento tiene una tesis, es decir, lo que se afirma, y razones que la sostienen. Un buen argumento usa hechos verificables y reconoce lo que no sabe. Un mal argumento ataca a la persona o usa palabras como «todos» sin respaldo.",
        "En este tema hay posiciones fundadas distintas. Quien defiende la intervención del Estado señala que el mercado falló en 1929; quien defiende poca intervención apunta al costo y a la libertad económica; los totalitarismos propusieron sacrificar libertades, y los hechos muestran que eliminaron partidos, prensa libre y elecciones. Ese costo puede evaluarse con evidencia.",
        "Todo modelo tiene consecuencias y límites. El Estado de Bienestar protege, pero cuesta recursos; el populismo mejoró derechos para algunos, pero concentró poder; los totalitarismos prometieron orden, pero eliminaron libertades. Un buen debate pregunta qué se gana, qué se pierde y para quién.",
    ],
    vocab=[("argumento", "afirmación apoyada en razones y evidencias"), ("tesis", "idea principal que se defiende en un debate"), ("costo", "lo que se pierde o se gasta al elegir una opción"), ("consecuencia", "resultado que sigue de una decisión o hecho"), ("contraargumento", "razón que se opone a un argumento")],
    worked=[
        ("Identificar tesis y razón", "En la Posición A, ¿cuál es la tesis y cuál la razón?", ["La tesis es que el Estado debe intervenir cuando el mercado falla.", "La razón es proteger el empleo y la protección social."], "Tesis: intervenir cuando el mercado falla; razón: proteger empleo y protección social"),
        ("Calcular un costo", "Un programa de ejemplo contrata a 1.000 personas con sueldo mensual de $300.000. ¿Cuánto paga por mes?", ["Multiplico personas por sueldo.", "1.000 × $300.000 = $300.000.000."], "$300.000.000 por mes"),
    ],
    mistakes=[("Defender una posición sin dar razones.", "Una afirmación sin razones es solo una opinión.", "Escribe tesis, razón y evidencia."),
              ("Presentar una posición como si no tuviera costos.", "Todo modelo tiene consecuencias y límites.", "Pregunta qué se gana, qué se pierde y para quién.")],
    T=[
        ("{F} ¿Qué defiende la Posición A?", "Que el Estado intervenga en el empleo y la protección social cuando el mercado falla", "La ficha lo indica."),
        ("{F} ¿Qué pide la Posición C que pueda esperar?", "Las libertades", "La ficha lo dice."),
        ("{F} ¿Cuántas personas contrata el programa de empleo público de ejemplo?", "2.000", "La ficha da el dato."),
        ("=", "{F} ¿Cuánto paga por mes el programa de empleo público de ejemplo? (en pesos)", "2000*400000", "Se multiplica el número de personas por el sueldo mensual.", " pesos"),
        ("{F} ¿Qué es una tesis? A) La idea principal que se defiende B) Un dato de un mapa", "A) La idea principal que se defiende", "Así se define en el vocabulario."),
        ("{F} ¿Cuál de estas es una razón de la Posición B? A) Evitar frenar la libertad económica B) Tener un solo partido", "A) Evitar frenar la libertad económica", "La Posición B lo menciona."),
        ("=", "{F} Si el programa de ejemplo pagara sueldos durante 6 meses, ¿cuánto gastaría en total? (en pesos)", "2000*400000*6", "Se multiplica el pago mensual por los meses.", " pesos"),
        ("{F} ¿Qué contraargumento sirve contra la Posición B? A) En 1929 el mercado por sí solo no evitó el desempleo B) Los regímenes totalitarios tenían partido único", "A) En 1929 el mercado por sí solo no evitó el desempleo", "Se apoya en el hecho histórico de la crisis."),
        ("{F} ¿Qué hecho de la ficha sirve para cuestionar la Posición C? A) Los totalitarismos eliminaron o limitaron partidos, prensa libre y elecciones libres B) El populismo mejoró derechos de algunos trabajadores", "A) Los totalitarismos eliminaron o limitaron partidos, prensa libre y elecciones libres", "Muestra que las libertades se perdieron."),
        ("{F} ¿Qué costo señala la Posición A y no resuelve del todo? A) Más gasto del Estado B) Eliminar los partidos políticos", "A) Más gasto del Estado", "Ella misma admite que intervenir implica gastar más."),
        ("{F} ¿Por qué decir «todos los modelos fueron iguales» es un mal argumento?", "Porque los hechos muestran diferencias en libertades y en medidas sociales", "La ficha distingue totalitarismo, democracias con política social y populismo."),
        ("{F} Un compañero dice: «Quien defiende el New Deal no sabe nada». ¿Qué falla tiene? A) Ataca a la persona y no da razones B) Es un buen contraargumento", "A) Ataca a la persona y no da razones", "Un argumento válido usa razones y evidencias, no insultos."),
        ("{F} ¿Cuál es la mejor conclusión equilibrada? A) El Estado de Bienestar protege pero cuesta recursos, y los totalitarismos eliminaron libertades B) El Estado de Bienestar no tiene costos", "A) El Estado de Bienestar protege pero cuesta recursos, y los totalitarismos eliminaron libertades", "Reconoce beneficio y costo en cada caso."),
    ],
    ctx=("En un debate de clase, una compañera defiende la Posición A y otro la B. ¿Qué pregunta ayuda más a ambos a mejorar sus argumentos? A) ¿Qué evidencia histórica muestra lo que pasó cuando se aplicó cada posición? B) ¿Quién tiene más seguidores en la sala?", "A) ¿Qué evidencia histórica muestra lo que pasó cuando se aplicó cada posición?", "Los argumentos se mejoran con evidencia, no con el número de seguidores."),
    sc=[("¿Qué es un argumento?", "Una afirmación apoyada en razones y evidencias", "Así se define en el vocabulario."),
        ("¿Qué es un contraargumento?", "Una razón que se opone a un argumento", "Así se define en el vocabulario."),
        ("=", "Un programa de ejemplo paga $200.000 al mes a 500 personas. ¿Cuánto paga en total por mes?", "200000*500", "Se multiplica el sueldo por el número de personas.", " pesos")],
    op=("Elige una de las tres posiciones de la ficha. Escribe: tu tesis, dos razones con un hecho histórico cada una, el costo o límite de esa posición y la respuesta a un contraargumento. Máximo ocho líneas. {F}",
        "Tesis: el Estado debe intervenir cuando el mercado falla. Razón 1: en 1929 el mercado no evitó el desempleo. Razón 2: el New Deal mantuvo las elecciones y dio empleo público. Costo: más gasto del Estado. Contraargumento: «intervenir frena la libertad»; respuesta: la intervención del New Deal no eliminó elecciones.",
        ["tesis clara", "dos razones con hechos", "reconoce un costo", "responde un contraargumento"], ["texto de hasta ocho líneas"], ["dar razones sin hechos", "no reconocer ningún costo"],
        "Pide que cuente qué argumento de otra posición le pareció más fuerte y por qué."),
    reinforce="Explica en voz alta tu postura sobre el rol del Estado en una crisis y da una razón con un hecho de la clase.",
    extend="Conversa con una persona de tu casa sobre cuándo debería ayudar el Estado a quien pierde su trabajo y anota un argumento que te haya parecido bueno.",
)
