"""Material del estudiante de 1.º medio, Historia, Geografía y Ciencias Sociales: OA 03 (Estado-nación, soberanía y geografía política)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 03"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (siglo XIX: años 1801 a 1900). "
     "Estado: organización política que gobierna un territorio con fronteras y tiene soberanía, es decir, el poder supremo de decidir dentro de ese territorio sin depender de otro poder. "
     "Nación: comunidad de personas que comparten lengua, historia y sentido de pertenencia. "
     "Estado-nación: Estado cuya población se reconoce como una nación. "
     "Hitos: Chile declara su independencia, 1818; Brasil, 1822; Bélgica, 1830; reino de Italia proclamado, 1861; imperio alemán proclamado, 1871.")
build(
    OA, 1, F,
    use="Aprenderé a situar el surgimiento del Estado-nación en América Latina y Europa, y a plantear la pregunta que guía este tema: ¿cómo se reorganizó el mapa político en el siglo XIX?",
    prior=["Sé qué son el liberalismo y el republicanismo.", "Sé calcular diferencias entre años.", "Sé qué es una frontera."],
    explain=[
        "Un Estado es una organización política que gobierna un territorio con fronteras. Tiene soberanía, que significa el poder supremo de decidir dentro de ese territorio, sin obedecer a otro poder superior. Una nación, en cambio, es una comunidad de personas que sienten que comparten lengua, historia y una identidad. El Estado-nación junta ambas cosas: un Estado cuyos habitantes se reconocen como una nación.",
        "Durante el siglo XIX el mapa político cambió. En América Latina, las antiguas colonias españolas y la portuguesa se independizaron y formaron nuevos Estados, como Chile en 1818 y Brasil en 1822. En Europa, territorios divididos en muchos Estados pequeños se unificaron: Italia en 1861 y Alemania en 1871. Así, en unos casos hubo fragmentación y en otros unificación.",
        "La idea de nación es una construcción histórica: se enseña en las escuelas, se difunde con símbolos como himnos y banderas, y se refuerza con una historia común. Por eso conviene preguntar quién define la nación y a quiénes deja fuera. No todos los habitantes de un territorio se sentían parte de la comunidad que el nuevo Estado decía representar.",
    ],
    vocab=[("Estado", "organización política que gobierna un territorio con fronteras"), ("soberanía", "poder supremo de decidir dentro de un territorio sin depender de otro poder"), ("nación", "comunidad que comparte lengua, historia y sentido de pertenencia"), ("Estado-nación", "Estado cuya población se reconoce como una nación"), ("unificación", "unión de varios territorios en un solo Estado")],
    worked=[
        ("Calcular una diferencia", "¿Cuántos años pasaron entre la unificación de Italia (1861) y la de Alemania (1871)?", ["Tomo los dos años de la ficha.", "Resto: 1871 − 1861 = 10."], "10 años"),
        ("Distinguir Estado y nación", "Un grupo comparte lengua e historia pero no tiene un gobierno propio. ¿Es una nación, un Estado o las dos cosas?", ["Comparte lengua e historia: es una nación.", "No tiene gobierno propio con soberanía: no es un Estado."], "Es una nación, pero no un Estado"),
    ],
    mistakes=[("Usar Estado y nación como si fueran sinónimos.", "El Estado es una organización política; la nación es una comunidad con identidad compartida.", "Define cada uno con sus propias palabras."),
              ("Decir que la nación siempre existió antes del Estado.", "En muchos casos el Estado ayudó a construir la identidad nacional.", "Pregunta cómo se difundió la idea de nación.")],
    T=[
        ("{F} ¿Qué es la soberanía según la ficha?", "El poder supremo de decidir dentro de un territorio sin depender de otro poder", "La ficha la define así."),
        ("{F} ¿Qué tres rasgos comparte una nación?", "Lengua, historia y sentido de pertenencia", "Son los rasgos de la ficha."),
        ("{F} ¿Cómo se llama el Estado cuya población se reconoce como una nación?", "Estado-nación", "La ficha lo define."),
        ("=", "{F} ¿Cuántos años pasaron entre la independencia de Chile y la de Bélgica?", "1830-1818", "Se resta el año de Chile al de Bélgica.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la independencia de Brasil y la unificación de Alemania?", "1871-1822", "Se resta el año de Brasil al de Alemania.", " años"),
        ("{F} ¿Qué hito es más antiguo? A) La independencia de Brasil B) La proclamación del reino de Italia", "A) La independencia de Brasil", "1822 es anterior a 1861."),
        ("{F} Un grupo de personas habla la misma lengua y comparte historia, pero vive dividido en varios gobiernos. ¿Qué es? A) Una nación sin Estado propio B) Un Estado-nación", "A) Una nación sin Estado propio", "Tiene identidad común, pero no un Estado único."),
        ("{F} Un gobierno decide solo sobre su territorio sin obedecer a ningún poder externo. ¿Qué principio ejerce? A) Soberanía B) Nacionalidad", "A) Soberanía", "La soberanía es el poder supremo dentro de un territorio."),
        ("{F} Ordena del más antiguo al más reciente: Alemania, Chile, Italia, Bélgica.", "Chile, Bélgica, Italia, Alemania", "Los años son 1818, 1830, 1861 y 1871."),
        ("{F} ¿Por qué la independencia de Chile y la unificación de Italia son procesos distintos?", "Chile se separó de un imperio y formó un Estado; Italia unió varios Estados en uno", "Uno es separación y el otro unificación."),
        ("{F} Un compañero dice: «Una nación es lo mismo que un Estado». ¿Qué le respondes?", "El Estado es una organización política con soberanía; la nación es una comunidad con identidad compartida", "Son conceptos distintos, aunque en un Estado-nación coinciden."),
        ("{F} ¿Por qué se dice que la idea de nación es una construcción histórica? A) Porque se difunde con escuelas, símbolos y relatos comunes B) Porque está escrita en la naturaleza", "A) Porque se difunde con escuelas, símbolos y relatos comunes", "La nación se enseña y se difunde, no es un hecho natural."),
        ("¿Cuál es la mejor pregunta histórica para este tema? A) ¿Cómo y por qué se reorganizó la geografía política de América Latina y Europa con el Estado-nación? B) ¿Qué país tiene la mejor bandera?", "A) ¿Cómo y por qué se reorganizó la geografía política de América Latina y Europa con el Estado-nación?", "La A se responde con hechos y causas; la B es una preferencia."),
    ],
    ctx=("Un afiche escolar dice: «Italia y Alemania se unificaron en el mismo año». ¿Qué corrección haces con los datos de la ficha? A) Italia se proclamó en 1861 y Alemania en 1871 B) Italia y Alemania se unificaron en 1861", "A) Italia se proclamó en 1861 y Alemania en 1871", "Los dos hitos tienen diez años de diferencia."),
    sc=[("¿Qué es una nación?", "Una comunidad que comparte lengua, historia y sentido de pertenencia", "Así se define."),
        ("¿Qué es la soberanía?", "El poder supremo dentro de un territorio", "Es el principio del Estado."),
        ("=", "¿Cuántos años pasaron entre 1822 y 1861?", "1861-1822", "Se resta el año menor al mayor.", " años")],
    op=("Dibuja una línea de tiempo de 1810 a 1880 con escala 1 cm = 10 años y marca estos cinco hitos: independencia de Chile (1818), de Brasil (1822), de Bélgica (1830), reino de Italia (1861) e imperio alemán (1871). Al lado de cada hito escribe si es independencia o unificación. Escribe una frase que explique qué diferencia hay entre un Estado y una nación. {F}",
        "Posiciones desde 1810: 0,8; 1,2; 2,0; 5,1; 6,1 cm. Chile, Brasil y Bélgica: independencia; Italia y Alemania: unificación. Frase: «El Estado es una organización política con soberanía; la nación es una comunidad con identidad compartida».",
        ["respeta la escala", "clasifica los hitos", "distingue Estado y nación"], ["línea de tiempo", "frase escrita"], ["no medir con la escala", "usar Estado y nación como sinónimos"],
        "Pide que explique por qué Alemania e Italia se unificaron mientras América Latina se dividió."),
    reinforce="Explica en voz alta, con tus palabras, qué es un Estado-nación y da dos ejemplos de la ficha.",
    extend="Busca en tu casa un símbolo nacional (bandera, billete, moneda) y di qué idea de nación representa.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, proclama de un grupo nacionalista, 1860: «Hablamos la misma lengua, recordamos la misma historia y habitamos la misma tierra. Por eso debemos vivir bajo un solo Estado y un solo gobierno.» "
     "Fuente B, informe de un funcionario a su gobierno, 1865: «En esta región se hablan cuatro lenguas y viven comunidades que no se sienten parte de la nación. Los maestros deben enseñar una sola lengua y una sola historia.»")
build(
    OA, 2, F,
    use="Aprenderé a leer fuentes sobre el nacionalismo del siglo XIX, a ver quién las escribe y para qué, y a separar la descripción de la interpretación.",
    prior=["Sé qué es el Estado-nación.", "Sé contextualizar una fuente.", "Sé que una proclama busca convencer."],
    explain=[
        "El nacionalismo es la idea de que cada nación debe tener su propio Estado y de que las personas deben sentir lealtad a su nación. Una proclama, como la Fuente A, es un texto público que busca convencer y movilizar. No es un dato neutral: expresa lo que un grupo quiere, no necesariamente lo que piensa toda la población.",
        "La Fuente B es un informe oficial. Un funcionario escribe a su gobierno para describir un problema. Usa la palabra «deben», lo que muestra un propósito: que la escuela enseñe una sola lengua y una sola historia. Con eso el Estado puede construir un sentido de pertenencia, pero también puede dejar fuera a quienes no comparten esa lengua.",
        "Para analizar, separa lo que el texto dice de lo que tú interpretas. La Fuente B describe una región con cuatro lenguas. Tú interpretas que el Estado quería unificar la cultura por medio de la escuela. Una conclusión sólida se apoya en el texto y reconoce que son dos voces de una misma época, no la opinión de todos.",
    ],
    vocab=[("nacionalismo", "idea de que cada nación debe tener su Estado y sentir lealtad a él"), ("proclama", "texto público que busca convencer y movilizar"), ("informe", "texto oficial que describe una situación a una autoridad"), ("lealtad", "sentimiento de fidelidad hacia algo o alguien"), ("homogeneizar", "hacer que algo sea igual en todo el territorio")],
    worked=[
        ("Contextualizar", "¿Quién escribe la Fuente A, cuándo y para qué?", ["Autor: un grupo nacionalista.", "Fecha: 1860. Propósito: convencer de vivir en un solo Estado."], "Un grupo nacionalista, en 1860, para convencer de unificar el Estado"),
        ("Descripción o interpretación", "(1) «La región tiene cuatro lenguas». (2) «El Estado quería borrar las lenguas de los pueblos». ¿Cuál es descripción?", ["La (1) repite lo que dice el informe.", "La (2) agrega una intención fuerte que el texto no dice."], "La (1) describe; la (2) interpreta de más"),
    ],
    mistakes=[("Tomar la proclama como la opinión de toda la población.", "Una proclama expresa lo que quiere un grupo.", "Escribe «el grupo nacionalista pedía» en lugar de «todos querían»."),
              ("Afirmar que el funcionario odiaba las lenguas locales.", "El texto no dice sus sentimientos, solo propone enseñar una sola lengua.", "Limítate a lo que dice y a lo que se puede inferir.")],
    T=[
        ("{F} ¿Qué pide la Fuente A?", "Vivir bajo un solo Estado y un solo gobierno", "La proclama lo dice de forma directa."),
        ("{F} ¿Cuántas lenguas se hablan en la región según la Fuente B?", "Cuatro", "El informe lo señala."),
        ("{F} ¿Qué tipo de texto es la Fuente B?", "Un informe oficial de un funcionario", "La ficha la presenta así."),
        ("=", "{F} ¿Cuántos años separan la Fuente A de la Fuente B?", "1865-1860", "Se resta el año de la proclama al del informe.", " años"),
        ("{F} ¿Qué fuente busca movilizar a un grupo? A) La Fuente A B) La Fuente B", "A) La Fuente A", "Una proclama convoca y moviliza."),
        ("{F} ¿Qué propone la Fuente B para la escuela? A) Enseñar una sola lengua y una sola historia B) Enseñar cuatro lenguas", "A) Enseñar una sola lengua y una sola historia", "El informe lo dice con la palabra «deben»."),
        ("{F} ¿Cuál frase describe la Fuente A? A) La proclama dice que comparten lengua, historia y tierra B) El grupo era el más numeroso de la región", "A) La proclama dice que comparten lengua, historia y tierra", "La B agrega un dato que la fuente no entrega."),
        ("{F} ¿Qué rasgo de nación aparece en la Fuente A? A) Lengua e historia compartidas B) Un comercio libre", "A) Lengua e historia compartidas", "Son dos rasgos que la proclama nombra."),
        ("{F} ¿Qué relación hay entre la Fuente B y el sentido de pertenencia? A) Propone la escuela como medio para crearlo B) Propone eliminarlo", "A) Propone la escuela como medio para crearlo", "Una sola historia y una sola lengua crean identidad común."),
        ("{F} ¿Por qué la Fuente A no prueba que todos los habitantes querían un solo Estado?", "Porque expresa lo que pide un grupo nacionalista, no toda la población", "Una proclama muestra la voz de quien la escribe."),
        ("{F} ¿Qué dato de la Fuente B limita la idea de una nación homogénea?", "Que hay comunidades que no se sienten parte de la nación y cuatro lenguas", "El informe reconoce la diversidad."),
        ("{F} Un compañero concluye: «En 1865 todas las comunidades aceptaban la lengua del Estado». ¿Qué corrección haces?", "El informe dice que hay comunidades que no se sienten parte de la nación", "Contradice la conclusión del compañero."),
        ("{F} ¿Qué fuente nueva ayudaría a conocer la perspectiva de las comunidades de la región? A) Una carta de una persona de esas comunidades B) Un mapa actual del país", "A) Una carta de una persona de esas comunidades", "Aporta la voz que falta en las dos fuentes."),
    ],
    ctx=("Un compañero prepara una presentación sobre el nacionalismo y solo usa la Fuente A. ¿Qué le recomiendas? A) Agregar la Fuente B para mostrar cómo el Estado intentó unificar la lengua B) Quitar la fuente B porque contradice a la A", "A) Agregar la Fuente B para mostrar cómo el Estado intentó unificar la lengua", "Dos fuentes con propósitos distintos dan una visión más completa."),
    sc=[("¿Qué es una proclama?", "Un texto público que busca convencer y movilizar", "Así se define."),
        ("¿Qué es el nacionalismo?", "La idea de que cada nación debe tener su Estado", "Es su definición."),
        ("¿Qué fuente de la ficha es un informe oficial?", "La Fuente B", "Es el informe del funcionario.")],
    op=("Elige una fuente de la ficha. Haz una tabla de tres filas con: autor y fecha; qué dice (descripción en una frase); qué interpretas (una frase que empiece con «Esto sugiere que…»). Cierra con una frase que diga qué no puedes concluir con esa sola fuente. {F}",
        "Fuente B. Autor y fecha: un funcionario, 1865. Dice: la región tiene cuatro lenguas y comunidades que no se sienten parte de la nación. Interpretación: esto sugiere que el Estado quería unificar la cultura por la escuela. No puedo concluir qué pensaban esas comunidades.",
        ["contextualiza con autor y fecha", "separa descripción de interpretación", "señala un límite"], ["tabla de tres filas", "frase de límite"], ["escribir una interpretación como descripción", "concluir sobre toda la población"],
        "Pide que diga qué voz no aparece en las fuentes."),
    reinforce="Explica por qué una proclama y un informe sirven para cosas distintas.",
    extend="Observa un cartel o aviso público de tu barrio y di quién lo escribe y para qué.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (cuadro de cambio territorial). "
     "Italia: antes de 1861 estaba dividida en varios Estados, entre ellos el Reino de Piamonte-Cerdeña, el Reino de las Dos Sicilias y los Estados Pontificios; el reino de Italia se proclama en 1861. "
     "Alemania: antes de 1871 había decenas de Estados alemanes agrupados en la Confederación Germánica; el imperio alemán se proclama en 1871. "
     "Gran Colombia: creada en 1819, se disuelve en 1831 y da origen a Colombia, Venezuela y Ecuador. "
     "América española: en muchas fronteras se siguieron los límites de las antiguas divisiones coloniales.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar cambio, continuidad y territorio: cuándo el mapa se unificó, cuándo se fragmentó y qué se mantuvo igual.",
    prior=["Sé qué es el Estado-nación y la soberanía.", "Sé leer un cuadro de hitos.", "Sé calcular diferencias de años."],
    explain=[
        "En el siglo XIX hay dos movimientos en el mapa. En Europa, territorios divididos se unificaron: Italia en 1861 y Alemania en 1871 reunieron Estados más pequeños en uno mayor. En América Latina ocurrió casi lo contrario: los grandes imperios coloniales se fragmentaron en muchos Estados nuevos. La Gran Colombia, por ejemplo, duró de 1819 a 1831 y se dividió en tres países.",
        "También hay continuidades. En América española muchas de las nuevas fronteras siguieron las divisiones administrativas coloniales, porque eran los límites que ya existían. Esto se conoce como principio de límites heredados. Las élites que dirigieron los nuevos Estados eran, en muchos casos, las mismas que habían tenido poder en la colonia.",
        "El territorio es clave: una frontera es una línea que marca hasta dónde llega la soberanía de un Estado. Cuando se fijó, no siempre coincidía con las comunidades ni con las lenguas. Por eso, mirar un mapa ayuda a explicar los conflictos y las identidades. Cada cambio de mapa tuvo causas políticas, económicas y culturales.",
    ],
    vocab=[("frontera", "línea que marca hasta dónde llega la soberanía de un Estado"), ("fragmentación", "división de un territorio en varios Estados"), ("unificación", "unión de varios Estados en uno"), ("límites heredados", "fronteras que siguen las divisiones coloniales anteriores"), ("élite", "grupo pequeño con mucho poder económico o político")],
    worked=[
        ("Medir una duración", "¿Cuántos años duró la Gran Colombia según la ficha?", ["Creada en 1819, disuelta en 1831.", "Resto: 1831 − 1819 = 12."], "12 años"),
        ("Clasificar un cambio", "Cuando Colombia, Venezuela y Ecuador se separaron, ¿fue unificación o fragmentación?", ["Un solo Estado se dividió en tres.", "Eso es fragmentación."], "Fragmentación"),
    ],
    mistakes=[("Pensar que en todo el mundo el mapa se unificó en el siglo XIX.", "En América Latina hubo fragmentación.", "Distingue por región."),
              ("Creer que las fronteras latinoamericanas se inventaron desde cero.", "Muchas siguieron límites coloniales.", "Busca qué se heredó y qué se cambió.")],
    T=[
        ("{F} ¿En qué año se proclama el reino de Italia?", "1861", "La ficha lo indica."),
        ("{F} ¿En qué año se disuelve la Gran Colombia?", "1831", "La ficha lo indica."),
        ("{F} ¿Qué tres países surgen de la disolución de la Gran Colombia?", "Colombia, Venezuela y Ecuador", "La ficha los nombra."),
        ("=", "{F} ¿Cuántos años pasaron entre la creación de la Gran Colombia y la proclamación del reino de Italia?", "1861-1819", "Se resta el año de creación al de Italia.", " años"),
        ("{F} ¿Qué proceso ocurrió en Italia y Alemania? A) Unificación B) Fragmentación", "A) Unificación", "Reunieron Estados más pequeños en uno."),
        ("{F} ¿Qué proceso ocurrió con la Gran Colombia? A) Fragmentación B) Unificación", "A) Fragmentación", "Un Estado se dividió en tres."),
        ("{F} ¿Qué continuidad señala la ficha en América española? A) Muchas fronteras siguieron límites coloniales B) Se borraron todos los límites", "A) Muchas fronteras siguieron límites coloniales", "Es el principio de límites heredados."),
        ("{F} Un Estado italiano antes de 1861 era el Reino de las Dos Sicilias. Después de 1861, ¿qué cambió para él? A) Pasó a formar parte del reino de Italia B) Se dividió en tres países, como la Gran Colombia", "A) Pasó a formar parte del reino de Italia", "La ficha dice que Italia unió varios Estados."),
        ("{F} En 1850, ¿existía el imperio alemán? A) No, se proclama en 1871 B) Sí", "A) No, se proclama en 1871", "La ficha fija la proclamación en 1871."),
        ("{F} ¿Por qué decir «el mapa se unificó» solo es válido para Europa y no para toda América?", "Porque en América Latina hubo fragmentación de imperios coloniales", "El proceso fue distinto en cada región."),
        ("{F} Un compañero dice: «Las fronteras sudamericanas se trazaron al azar en el siglo XIX». ¿Qué dato de la ficha lo contradice?", "Muchas fronteras siguieron límites de divisiones coloniales", "Hay una continuidad respecto de la colonia."),
        ("{F} ¿Qué dos cambios de territorio de la ficha muestran procesos opuestos? A) Unificación de Italia y fragmentación de la Gran Colombia B) Dos unificaciones", "A) Unificación de Italia y fragmentación de la Gran Colombia", "Uno junta Estados y el otro los separa."),
        ("{F} ¿Qué conclusión es más ajustada? A) En el siglo XIX el mapa cambió por unificación en Europa y por fragmentación en América Latina, con continuidades heredadas B) En el siglo XIX el mapa solo se unificó, en Europa y en América por igual", "A) En el siglo XIX el mapa cambió por unificación en Europa y por fragmentación en América Latina, con continuidades heredadas", "Reúne cambios y continuidades."),
    ],
    ctx=("En una guía turística de ejemplo dice: «Italia existe desde la antigüedad como un solo Estado». ¿Qué corrección haces con la ficha? A) Como Estado, Italia se proclama en 1861, antes de eso había varios Estados B) Italia siempre fue un solo Estado", "A) Como Estado, Italia se proclama en 1861, antes de eso había varios Estados", "La ficha muestra que el Estado italiano es del siglo XIX."),
    sc=[("¿Qué es una frontera?", "Una línea que marca hasta dónde llega la soberanía de un Estado", "Así se define."),
        ("¿Qué es la fragmentación?", "La división de un territorio en varios Estados", "Es el proceso contrario a la unificación."),
        ("=", "¿Cuántos años pasaron entre 1831 y 1861?", "1861-1831", "Se resta el año menor al mayor.", " años")],
    op=("Haz una tabla con dos columnas, «Cambió» y «Continuó», y escribe dos datos en cada una usando solo la ficha. Luego dibuja un esquema de dos flechas: una que muestre cómo varios Estados italianos pasan a ser uno (1861) y otra que muestre cómo la Gran Colombia se divide (1831). {F}",
        "Cambió: Italia se unifica en 1861; la Gran Colombia se divide en 1831. Continuó: fronteras que siguen límites coloniales; élites que mantienen poder. Esquema: varias flechas hacia un cuadro «Italia 1861»; una flecha desde «Gran Colombia» hacia tres cuadros.",
        ["usa datos de la ficha", "separa cambio y continuidad", "esquema de unificación y fragmentación"], ["tabla completa", "esquema con flechas"], ["poner el mismo dato en ambas columnas", "invertir unificación y fragmentación"],
        "Pide que explique qué ventaja tiene para un Estado heredar fronteras coloniales."),
    reinforce="Explica en voz alta la diferencia entre unificación y fragmentación con un ejemplo de cada una.",
    extend="Mira un mapa de tu región y anota un límite que sea una frontera administrativa.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno). "
     "Nacionalista de la ciudad, 1860: «Nuestra lengua y nuestra historia son una sola. Es hora de unir el territorio en un Estado fuerte.» "
     "Rey de un pequeño Estado vecino, 1860: «No quiero perder mi trono ni mi autoridad. Prefiero seguir gobernando mi territorio.» "
     "Comerciante, 1860: «Con un solo Estado habría una sola moneda y menos aduanas, y mis negocios crecerían.» "
     "Campesino de una zona fronteriza, 1860: «Hablo otra lengua en casa. No sé si me van a respetar en el nuevo Estado.»")
build(
    OA, 4, F,
    use="Aprenderé a contrastar actores, causas y perspectivas en el surgimiento de los Estados-nación: quién ganaba, quién perdía y por qué.",
    prior=["Sé qué es la unificación.", "Sé que cada actor tiene intereses.", "Sé separar descripción de interpretación."],
    explain=[
        "Los Estados-nación no surgieron solo por una idea. Hubo actores con distintos intereses. Un nacionalista quiere unir a quienes comparten lengua e historia. Un rey o gobernante local teme perder su poder. Un comerciante puede ganar con un solo mercado, una moneda y menos aduanas, que son los puestos donde se cobra impuesto a los productos que pasan. Un campesino de una zona fronteriza teme que no respeten su lengua.",
        "Las causas también se combinan. Hubo causas políticas, como el deseo de tener un Estado propio; causas económicas, como unir mercados; y causas culturales, como la difusión de una lengua y una historia comunes. En el caso de Alemania, el reino de Prusia tuvo un rol central; en el de Italia, el reino de Piamonte-Cerdeña lideró la unificación. Las decisiones de estos Estados fueron decisivas.",
        "Para contrastar, compara qué quiere cada actor, qué le conviene y qué teme. Una explicación buena no dice que todos querían la unificación. Muestra que algunos ganaban, otros perdían y otros dudaban. Así se entienden las tensiones y por qué algunas comunidades quedaron en posición vulnerable dentro del nuevo Estado.",
    ],
    vocab=[("aduana", "lugar donde se cobra impuesto a los productos que cruzan una frontera"), ("trono", "cargo y autoridad de un rey"), ("mercado nacional", "territorio donde se comercia sin barreras internas"), ("minoría cultural", "grupo con lengua o costumbres distintas a las de la mayoría"), ("vulnerable", "que puede sufrir daño con más facilidad")],
    worked=[
        ("Identificar quién gana", "Si desaparecen las aduanas internas, ¿qué actor de la ficha gana más?", ["Con menos aduanas se comercia más fácil.", "El comerciante dice que sus negocios crecerían."], "El comerciante"),
        ("Identificar quién teme", "¿Qué actor teme perder su cargo si se unifica el territorio?", ["Un rey perdería su autoridad en un Estado mayor.", "La ficha lo dice en su voz."], "El rey de un pequeño Estado vecino"),
    ],
    mistakes=[("Decir que todos los habitantes querían el nuevo Estado.", "Hubo actores que temían perder poder o respeto.", "Incluye al menos un actor que gana y uno que teme."),
              ("Olvidar las causas económicas y quedarse solo con la lengua.", "Los negocios y las aduanas también impulsaron la unificación.", "Nombra causas políticas, económicas y culturales.")],
    T=[
        ("{F} ¿Qué quiere el nacionalista de la ciudad?", "Unir el territorio en un Estado fuerte", "Su voz lo dice."),
        ("{F} ¿Qué teme perder el rey de un pequeño Estado vecino?", "Su trono y su autoridad", "La ficha lo dice."),
        ("{F} ¿Qué ventaja ve el comerciante en un solo Estado?", "Una sola moneda y menos aduanas", "Lo señala en su voz."),
        ("{F} ¿Qué dudas tiene el campesino de la zona fronteriza?", "Si respetarán su lengua en el nuevo Estado", "Habla otra lengua en casa."),
        ("{F} ¿Qué actor tiene un interés económico? A) El comerciante B) El rey", "A) El comerciante", "Busca crecer sus negocios."),
        ("{F} ¿Qué actor tiene una preocupación cultural? A) El campesino de la zona fronteriza B) El nacionalista", "A) El campesino de la zona fronteriza", "Teme por su lengua."),
        ("{F} ¿Qué actor se opone más a la unificación? A) El rey de un pequeño Estado B) El comerciante", "A) El rey de un pequeño Estado", "Perdería su poder y su cargo."),
        ("{F} Si se unifica el Estado y se enseña una sola lengua en las escuelas, ¿qué actor se siente más amenazado? A) El campesino de la zona fronteriza B) El comerciante", "A) El campesino de la zona fronteriza", "Su lengua de casa podría perder espacio."),
        ("{F} ¿Qué causa es política? A) Tener un Estado propio B) Unir mercados", "A) Tener un Estado propio", "Se refiere al poder y a la organización del Estado."),
        ("{F} ¿Qué causa es económica? A) Una sola moneda y menos aduanas B) Compartir la historia", "A) Una sola moneda y menos aduanas", "Se relaciona con el comercio."),
        ("{F} Un compañero dice: «Todos los habitantes querían la unificación». Refútalo con la ficha.", "El rey teme perder su trono y el campesino duda de ser respetado", "Hay actores que temen o dudan."),
        ("{F} ¿Por qué el comerciante y el rey tienen perspectivas opuestas?", "Porque uno gana mercado con la unificación y el otro pierde su poder", "Sus intereses son contrarios."),
        ("{F} ¿Qué explicación es más completa para la unificación? A) Hubo causas políticas, económicas y culturales, y actores con intereses distintos B) Fue solo por la lengua", "A) Hubo causas políticas, económicas y culturales, y actores con intereses distintos", "La explicación combina varias causas y actores."),
    ],
    ctx=("Para un reportaje sobre la unificación de un país de ejemplo, un grupo solo entrevista al nacionalista. ¿Qué voz les falta para mostrar a quién podría perjudicar? A) La del campesino de la zona fronteriza B) La de otro nacionalista", "A) La del campesino de la zona fronteriza", "Contrastar exige incluir voces de quienes dudan o pierden."),
    sc=[("¿Qué es una aduana?", "Un lugar donde se cobra impuesto a los productos que cruzan una frontera", "Así se define."),
        ("¿Qué actor teme por su lengua?", "El campesino de la zona fronteriza", "Lo dice su voz."),
        ("¿Qué actor gana con una sola moneda?", "El comerciante", "Menos aduanas y una sola moneda facilitan su comercio.")],
    op=("Elige dos actores de la ficha y haz una tabla con tres columnas: qué quiere, qué le conviene y qué teme. Después redacta tres líneas que expliquen por qué sus perspectivas sobre la unificación son distintas. {F}",
        "Comerciante: quiere vender más; le conviene una sola moneda; teme las aduanas. Rey: quiere gobernar; le conviene seguir como está; teme perder el trono. Texto: «El comerciante gana con la unificación y el rey pierde poder; por eso opinan distinto».",
        ["elige dos actores", "completa las tres columnas", "explica el choque con evidencia"], ["tabla completa", "tres líneas"], ["escribir lo mismo para ambos actores", "opinar sin base en la ficha"],
        "Pide que diga qué actor quedó con menos voz en el nuevo Estado."),
    reinforce="Elige un actor y explica en voz alta qué quiere y qué teme.",
    extend="Piensa en una decisión de tu escuela que beneficie a unos y preocupe a otros. Nombra a dos actores.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (datos para construir un argumento; fechas reales y afirmaciones de ejemplo). "
     "Pregunta: ¿qué explica el surgimiento de los Estados-nación en el siglo XIX? "
     "Dato 1: el reino de Italia se proclama en 1861 y el imperio alemán en 1871. "
     "Dato 2: las nuevas escuelas enseñaban una lengua y una historia comunes. "
     "Dato 3: la unificación permitió un mercado más grande con menos aduanas internas. "
     "Dato 4: en América Latina las independencias formaron Estados nuevos con fronteras que seguían límites coloniales.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento sobre las causas del Estado-nación con afirmación, evidencia, razonamiento y una conclusión proporcional.",
    prior=["Sé qué partes tiene un argumento.", "Sé contrastar actores y causas.", "Sé que una conclusión debe ser proporcional."],
    explain=[
        "Un argumento sobre el Estado-nación puede afirmar: «el surgimiento de los Estados-nación tuvo causas políticas, económicas y culturales». La evidencia son los datos: la proclamación de Italia y Alemania, la enseñanza de una lengua común, el mercado más grande y los Estados de América Latina. El razonamiento explica cómo cada dato apoya cada causa.",
        "La causa política es el deseo de tener un Estado con soberanía. La causa económica es el mercado más amplio con menos aduanas. La causa cultural es la difusión de una lengua y una historia comunes en las escuelas. No es necesario elegir una sola: la historia suele ser multicausal, es decir, tiene más de una causa que actúa a la vez.",
        "Para que el argumento sea proporcional, debe reconocer que los procesos no fueron iguales en Europa y en América Latina. En Europa hubo sobre todo unificación; en América Latina, independencias y fragmentación. Un contraargumento posible es que no todos los habitantes se sentían parte de la nación. Responderlo mejora el texto.",
    ],
    vocab=[("multicausal", "con más de una causa que actúa a la vez"), ("causa política", "razón relacionada con el poder y el Estado"), ("causa económica", "razón relacionada con el comercio y la producción"), ("causa cultural", "razón relacionada con la lengua, la historia y las costumbres"), ("contraargumento", "dato o idea que podría contradecir la afirmación")],
    worked=[
        ("Elegir evidencia económica", "¿Qué dato de la ficha apoya una causa económica?", ["Busco un dato sobre comercio.", "El dato 3 habla de mercado más grande y menos aduanas."], "Dato 3"),
        ("Elegir evidencia cultural", "¿Qué dato apoya una causa cultural?", ["Busco un dato sobre lengua o historia.", "El dato 2 menciona escuelas con lengua e historia comunes."], "Dato 2"),
    ],
    mistakes=[("Explicar el Estado-nación con una sola causa.", "El proceso tuvo causas políticas, económicas y culturales.", "Nombra al menos dos causas y su evidencia."),
              ("Citar un dato sin explicar su vínculo con la afirmación.", "Falta el razonamiento.", "Agrega «Esto muestra que…».")],
    T=[
        ("{F} ¿Qué dato muestra la causa política de tener un Estado propio?", "El dato 1, la proclamación de Italia y Alemania", "Son nuevos Estados con soberanía."),
        ("{F} ¿Qué dato muestra una causa cultural?", "El dato 2, escuelas con una lengua e historia comunes", "Refuerza la identidad."),
        ("{F} ¿Qué dato muestra una causa económica?", "El dato 3, un mercado más grande con menos aduanas", "Habla de comercio."),
        ("=", "{F} ¿Cuántos años pasaron entre la proclamación de Italia y la de Alemania?", "1871-1861", "Se resta el año de Italia al de Alemania.", " años"),
        ("{F} ¿Qué afirmación responde la pregunta? A) Los Estados-nación surgieron por causas políticas, económicas y culturales B) Surgieron por una sola causa, la lengua", "A) Los Estados-nación surgieron por causas políticas, económicas y culturales", "Se apoya en los datos 1, 2 y 3."),
        ("{F} ¿Qué dato muestra que el proceso no fue igual en toda la región? A) El dato 4, sobre las independencias en América Latina B) El dato 2", "A) El dato 4, sobre las independencias en América Latina", "Contrasta con la unificación de Europa."),
        ("{F} Completa el razonamiento: «El dato 3 apoya la causa económica porque…» A) un mercado más grande facilita el comercio B) las escuelas enseñan lengua", "A) un mercado más grande facilita el comercio", "Conecta el dato con la causa."),
        ("{F} Un compañero escribe: «Los Estados-nación surgieron solo por la lengua». ¿Qué datos usas para corregirlo?", "Los datos 1 y 3, que muestran causas políticas y económicas", "Hay más causas además de la cultura."),
        ("{F} ¿Por qué el dato 4 es un contraargumento a la idea de que siempre hubo unificación?", "Porque en América Latina surgieron Estados nuevos por independencia", "No fue unificación sino separación."),
        ("{F} ¿Qué palabra hace más proporcional la conclusión? A) «multicausal» B) «única»", "A) «multicausal»", "Refleja varias causas."),
        ("{F} Ordena las partes de un buen argumento: razonamiento, afirmación, evidencia.", "Afirmación, evidencia, razonamiento", "Primero se responde, luego se prueba y se explica."),
        ("{F} ¿Qué dato falta para incluir la voz de los pueblos que quedaron dentro de nuevas fronteras? A) Un dato sobre comunidades que no se sentían parte de la nación B) Otro dato del mercado", "A) Un dato sobre comunidades que no se sentían parte de la nación", "Permite reconocer límites."),
        ("{F} ¿Qué conclusión se ajusta mejor a los cuatro datos? A) El Estado-nación surgió por causas políticas, económicas y culturales, con procesos distintos en Europa y América Latina B) El Estado-nación surgió solo por unificación", "A) El Estado-nación surgió por causas políticas, económicas y culturales, con procesos distintos en Europa y América Latina", "Reúne causas y diferencias regionales."),
    ],
    ctx=("Un diario escolar publica: «Alemania e Italia se unificaron porque todos hablaban igual». ¿Qué evidencia de la ficha usarías para matizar? A) El dato 3, que muestra una causa económica B) El dato 2, que muestra escuelas con lengua común", "A) El dato 3, que muestra una causa económica", "Muestra que no fue solo la lengua."),
    sc=[("¿Qué significa multicausal?", "Con más de una causa a la vez", "Así se define."),
        ("¿Qué parte de un argumento explica cómo el dato apoya la afirmación?", "El razonamiento", "Es la función del razonamiento."),
        ("=", "¿Cuántos años pasaron entre 1861 y 1900?", "1900-1861", "Se resta el año menor al mayor.", " años")],
    op=("Escribe un párrafo de seis a ocho líneas que responda: «¿Qué explica el surgimiento de los Estados-nación en el siglo XIX?». Usa tres datos de la ficha, incluye el dato 4 como diferencia entre regiones y marca la afirmación, la evidencia y el razonamiento. {F}",
        "«Los Estados-nación surgieron por causas políticas, económicas y culturales. Italia (1861) y Alemania (1871) crearon Estados con soberanía. La unificación creó un mercado más grande con menos aduanas y las escuelas enseñaban lengua e historia comunes. Sin embargo, en América Latina el proceso fue distinto: surgieron Estados nuevos por independencia, con fronteras que seguían límites coloniales».",
        ["responde la pregunta", "usa tres datos y una diferencia", "conclusión proporcional"], ["párrafo escrito", "partes marcadas"], ["usar una sola causa", "no explicar el vínculo"],
        "Pide que diga qué grupo habría quedado fuera de esta explicación."),
    reinforce="Explica en voz alta una causa política, una económica y una cultural del Estado-nación.",
    extend="Escribe un contraargumento a tu párrafo y respóndelo con un dato de la ficha.",
)

# ---------------------------------------------------------------- clase 6
F = ("Ficha 6 (límites del Estado-nación; casos de ejemplo y datos generales). "
     "Imperio austrohúngaro: formado en 1867, reunía a muchas poblaciones con lenguas distintas; con el crecimiento del nacionalismo, varios grupos reclamaron Estados propios. "
     "Chile: durante la segunda mitad del siglo XIX el Estado ocupó el territorio de La Araucanía, donde vivía el pueblo mapuche, y esto tuvo graves consecuencias para esa población. "
     "Escuelas nacionales: enseñaban una lengua y una historia comunes, a veces sin considerar las lenguas de los pueblos originarios. "
     "Caso de ejemplo: en una región de frontera, un 30 % de la población habla otra lengua que la oficial.")
build(
    OA, 6, F,
    use="Aprenderé a evaluar proyecciones y límites del Estado-nación: qué logró, a quiénes dejó fuera y qué problemas dejó para el siglo XX.",
    prior=["Sé qué es el Estado-nación y por qué surgió.", "Sé contrastar actores y causas.", "Sé que una conclusión debe ser proporcional."],
    explain=[
        "El Estado-nación tuvo logros: creó identidades compartidas, permitió leyes comunes y mercados más amplios. Pero también tuvo límites. Uno es que la nación se definió desde un grupo dominante y dejó fuera a otros. El imperio austrohúngaro, por ejemplo, reunía a poblaciones con lenguas distintas, y con el nacionalismo varios grupos reclamaron Estados propios, lo que generó tensiones.",
        "En América Latina, los Estados nuevos también tuvieron límites. En Chile, durante la segunda mitad del siglo XIX, el Estado ocupó La Araucanía, donde vivía el pueblo mapuche, y ese proceso tuvo graves consecuencias para esa población. Las escuelas enseñaban una lengua y una historia comunes, a veces sin considerar las lenguas de los pueblos originarios. Es un ejemplo de cómo la integración nacional pudo implicar exclusión.",
        "Evaluar significa pesar logros y costos con evidencia. Una buena conclusión no dice que el Estado-nación fue solo bueno o solo malo. Reconoce que dio ciudadanía y leyes comunes y que, a la vez, ignoró o perjudicó a minorías. También permite proyectar: los nacionalismos del siglo XIX influyeron en conflictos posteriores del siglo XX.",
    ],
    vocab=[("integración", "incorporar a un grupo dentro de una comunidad más amplia"), ("exclusión", "dejar fuera a un grupo de derechos o decisiones"), ("pueblos originarios", "pueblos que habitaban un territorio antes de la formación del Estado"), ("proyección", "efecto que un proceso tiene hacia el futuro"), ("minoría", "grupo menos numeroso dentro de una población")],
    worked=[
        ("Calcular una proporción", "En el caso de ejemplo, si la región tiene 2.000 habitantes y el 30 % habla otra lengua, ¿cuántos son?", ["30 % de 2.000.", "2.000 × 30 ÷ 100 = 600."], "600 personas"),
        ("Pesar un logro y un costo", "La escuela nacional unió una lengua común. ¿Qué costo señala la ficha?", ["Un logro es la identidad común.", "El costo es no considerar las lenguas de los pueblos originarios."], "Costo: a veces ignoró las lenguas de los pueblos originarios"),
    ],
    mistakes=[("Concluir que el Estado-nación fue solo positivo.", "Se ignoran los costos para minorías y pueblos originarios.", "Pesa logros y costos con evidencia."),
              ("Concluir que fue solo negativo.", "Se ignoran los logros como leyes comunes y ciudadanía.", "Reconoce ambas caras.")],
    T=[
        ("{F} ¿En qué año se formó el imperio austrohúngaro?", "1867", "La ficha lo indica."),
        ("{F} ¿Qué territorio ocupó el Estado chileno en la segunda mitad del siglo XIX según la ficha?", "La Araucanía", "La ficha lo menciona."),
        ("{F} ¿Qué pueblo vivía en La Araucanía?", "El pueblo mapuche", "La ficha lo indica."),
        ("=", "{F} En el caso de ejemplo, una región de 4.000 habitantes tiene un 30 % que habla otra lengua. ¿Cuántas personas son?", "4000*30/100", "Se calcula el 30 % de 4.000.", " personas"),
        ("{F} ¿Qué es un logro del Estado-nación? A) Creó leyes comunes y una identidad compartida B) Eliminó toda la diversidad", "A) Creó leyes comunes y una identidad compartida", "La explicación lo señala como logro."),
        ("{F} ¿Qué es un costo del Estado-nación? A) Dejó fuera a minorías y a pueblos originarios B) Creó leyes comunes", "A) Dejó fuera a minorías y a pueblos originarios", "La ficha lo muestra como exclusión."),
        ("{F} ¿Qué dificultad enfrentó el imperio austrohúngaro con el nacionalismo? A) Varios grupos reclamaron Estados propios B) Todos aceptaron un solo Estado", "A) Varios grupos reclamaron Estados propios", "La ficha dice que había lenguas distintas y reclamos."),
        ("{F} ¿Qué efecto pudo tener una escuela que solo enseña una lengua en una zona con otra lengua? A) Que la lengua local pierda espacio B) Que la lengua local se fortalezca", "A) Que la lengua local pierda espacio", "La ficha dice que a veces no se consideraban las lenguas de los pueblos originarios."),
        ("{F} En el caso de ejemplo, el 30 % de la población habla otra lengua que la oficial. ¿Qué proporción habla la lengua oficial? A) 70 % B) 30 %", "A) 70 %", "Se resta 30 de 100."),
        ("{F} ¿Por qué ocupar La Araucanía muestra un límite del Estado-nación?", "Porque la integración implicó exclusión y graves consecuencias para el pueblo mapuche", "El Estado se amplió sin considerar a ese pueblo."),
        ("{F} Un compañero dice: «El Estado-nación siempre fue justo con todos». Refútalo con la ficha.", "El imperio austrohúngaro tuvo reclamos y la Araucanía implicó graves consecuencias para el pueblo mapuche", "Hay exclusiones en la ficha."),
        ("{F} ¿Qué conclusión pesa logros y costos? A) El Estado-nación dio leyes e identidad comunes, pero excluyó a minorías y pueblos originarios B) El Estado-nación no tuvo ningún efecto", "A) El Estado-nación dio leyes e identidad comunes, pero excluyó a minorías y pueblos originarios", "Considera ambas caras."),
        ("{F} ¿Qué proyección puede hacerse desde el caso austrohúngaro? A) Los nacionalismos pudieron generar conflictos en el siglo XX B) Los nacionalismos desaparecieron", "A) Los nacionalismos pudieron generar conflictos en el siglo XX", "La explicación vincula el nacionalismo con tensiones posteriores."),
    ],
    ctx=("Una escuela de ejemplo en una zona con otra lengua enseña solo la lengua oficial. ¿Qué podría hacer para ser más inclusiva? A) Valorar también la lengua local y enseñar su historia B) Enseñar solo la lengua oficial para que todos sean iguales", "A) Valorar también la lengua local y enseñar su historia", "La inclusión reconoce la diversidad."),
    sc=[("¿Qué es la exclusión?", "Dejar fuera a un grupo de derechos o decisiones", "Así se define."),
        ("¿Qué son los pueblos originarios?", "Pueblos que habitaban un territorio antes del Estado", "Así se define."),
        ("=", "¿Cuánto es el 30 % de 1.000?", "1000*30/100", "Se calcula el porcentaje.", "")],
    op=("Haz una tabla con dos columnas, «Logros» y «Costos», con tres datos en cada una usando solo la ficha y la explicación. Después escribe una frase que pese ambos y diga si, en tu opinión, el Estado-nación fue más beneficioso o más costoso, con una razón apoyada en la ficha. {F}",
        "Logros: identidad compartida; leyes comunes; mercados más amplios. Costos: exclusión de minorías; ocupación de La Araucanía; escuelas que ignoraron lenguas originarias. Frase: «Dio ciudadanía e identidad común, pero los costos fueron graves para pueblos originarios».",
        ["tres logros y tres costos", "usa evidencia de la ficha", "frase que pesa ambos"], ["tabla completa", "una frase"], ["poner solo logros o solo costos", "opinar sin evidencia"],
        "Pide que diga quién debería participar al escribir la historia de una nación."),
    reinforce="Explica en voz alta un logro y un costo del Estado-nación con ejemplos de la ficha.",
    extend="Averigua con una persona de tu casa si en su familia se habla otra lengua además del castellano y anota una frase.",
)
