"""Cuaderno del estudiante, 8.º básico Historia, Geografía y Ciencias Sociales: OA 19 (transformaciones y desafíos de la Independencia de Chile)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 19"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = "Línea de tiempo de ejemplo: 1810, Primera Junta Nacional de Gobierno; 1814, batalla de Rancagua y comienzo de la Reconquista; 1817, victoria patriota en Chacabuco; 1818, declaración de la independencia y batalla de Maipú; 1823, renuncia de Bernardo O'Higgins al cargo de Director Supremo."
build(
    OA, 1, F1,
    use="Aprenderé a ubicar la independencia de Chile en el tiempo y a distinguir qué cambió con ella y qué desafíos dejó. Sirve para no confundir «ser independientes» con «tener un país ya organizado e igualitario».",
    prior=["Sé qué fue la Colonia y quién gobernaba en nombre del rey.", "Sé leer una línea de tiempo y calcular años entre dos fechas.", "Sé que una fuente es un testimonio del pasado."],
    explain=[
        "La independencia de Chile fue un proceso: comenzó en 1810 con la Primera Junta Nacional de Gobierno, pasó por una guerra con retrocesos y avances, y se declaró en 1818. Independencia significa que un territorio deja de depender de otro poder, en este caso de la monarquía española, y se gobierna a sí mismo. Pero declararla no bastó: había que construir un país.",
        "Para eso se buscó un orden republicano. Una república es una forma de gobierno donde las autoridades no heredan el cargo, ejercen el poder por un tiempo y deben respetar una constitución, que es la ley máxima. También surgió la idea de soberanía popular: el poder de gobernar nace del pueblo y no de un rey. De ahí viene la ciudadanía, que es la condición de quienes tienen derechos y deberes políticos, como elegir a sus autoridades.",
        "Además había que formar un Estado nacional: una organización con territorio, leyes, autoridades e instituciones comunes para todo el país. Estas transformaciones fueron desafíos, no resultados inmediatos. Por ejemplo, la independencia no trajo igualdad inmediata: muchas personas siguieron sin los mismos derechos, y el nuevo orden tardó años en estabilizarse.",
    ],
    vocab=[("independencia", "fin de la dependencia de otro poder para gobernarse por sí mismo"), ("república", "forma de gobierno con autoridades no hereditarias y sujetas a una constitución"), ("soberanía popular", "idea de que el poder de gobernar nace del pueblo"), ("ciudadanía", "condición de quien tiene derechos y deberes políticos"), ("Estado nacional", "organización con territorio, leyes e instituciones comunes para todo el país")],
    worked=[
        ("Ubicar un hecho en el proceso", "Con una línea de tiempo de ejemplo que marca 1810, 1814, 1817 y 1818, ¿dentro de qué años se desarrolla la guerra de la independencia que muestra la línea y cuántos años abarca?",
         ["Tomo el primer hito: 1810.", "Tomo el último hito de la declaración y la batalla que la afirma: 1818.", "Resto: 1818 - 1810."], "De 1810 a 1818, ocho años"),
        ("Distinguir independencia e igualdad", "Un texto de ejemplo dice: «Desde la declaración, en Chile todos fueron iguales ante la ley en la práctica». ¿Qué le falta considerar?",
         ["La declaración cambió quién gobernaba.", "Pero las diferencias de riqueza, de origen y de derechos políticos continuaron.", "La igualdad plena fue un desafío posterior."], "Que la independencia no trajo igualdad inmediata"),
    ],
    mistakes=[
        ("Creer que la independencia ocurrió en un solo día.", "Fue un proceso con etapas, guerra y construcción de instituciones.", "Ubica la declaración dentro de un periodo más largo."),
        ("Pensar que, tras la declaración, el nuevo orden fue estable desde el comienzo.", "Hubo cambios de gobierno, falta de acuerdos y guerra posterior.", "Busca datos de inestabilidad antes de afirmar que todo estaba resuelto."),
    ],
    T=[
        ("En Historia: ¿qué significa que un territorio se vuelve independiente?", "Deja de depender de otro poder y se gobierna a sí mismo", "Es el significado central de independencia."),
        ("{F} Según la línea de tiempo, ¿en qué año se declara la independencia de Chile?", "1818", "La línea la ubica en ese año."),
        ("En Historia: ¿qué es la soberanía popular?", "La idea de que el poder de gobernar nace del pueblo", "Se opone a que el poder venga del rey."),
        ("{F} ¿Qué hecho de 1814 que aparece en la línea muestra que la independencia no fue un camino recto? A) la batalla de Rancagua y el comienzo de la Reconquista, B) la victoria de Chacabuco, C) la renuncia de O'Higgins.", "A", "En 1814 los patriotas perdieron y volvió el poder del rey."),
        ("Elige la frase que expresa mejor un orden republicano: A) un gobernante hereda el cargo de su padre, B) las autoridades ejercen el poder por un tiempo y respetan una constitución, C) el jefe del ejército decide todo sin límites.", "B", "La república exige cargos no hereditarios y sujetos a la ley."),
        ("Una compañera dice: «Con la independencia, todos los habitantes pasaron a tener los mismos derechos». ¿Por qué esa afirmación es inexacta?", "Porque la independencia cambió quién gobernaba, pero las desigualdades y la ciudadanía restringida continuaron", "Independencia no es igualdad inmediata."),
        ("=", "{F} ¿Cuántos años pasaron entre la batalla de Chacabuco y la renuncia de O'Higgins?", "1823-1817", "Se restan los años de ambos hitos."),
        ("=", "{F} ¿Cuántos años separan la batalla de Rancagua de la declaración de la independencia?", "1818-1814", "Se restan los años de la línea."),
        ("Un decreto de ejemplo dice: «Los cargos de gobierno se elegirán y durarán cinco años; ninguno podrá pasarse a un hijo». ¿Qué rasgo del orden republicano muestra? A) cargos temporales y no hereditarios, B) cargos vitalicios, C) poder del rey.", "A", "Dura un tiempo fijo y no se hereda."),
        ("{F} Un texto afirma: «Desde 1818 el país vivió en completa estabilidad». ¿Qué dos hechos de la línea contradicen esa idea?", "La batalla de Maipú en 1818, que muestra que la guerra seguía, y la renuncia de O'Higgins en 1823", "La guerra continuó y el gobierno cambió de manos."),
        ("Explica con una frase por qué declarar la independencia no bastaba para tener un Estado nacional.", "Porque además hacían falta leyes, instituciones, autoridades y control del territorio comunes para todo el país", "El Estado nacional se construye más allá de la declaración."),
        ("Evalúa la frase «La independencia de Chile fue un solo día». A) Es correcta porque la declaración fue un día; B) Es incompleta porque fue un proceso con etapas, guerra y construcción de instituciones; C) Es falsa porque nunca hubo declaración.", "B", "La declaración es un hito dentro de un proceso largo."),
        ("{F} ¿Cuántos años pasaron entre la declaración de la independencia y la renuncia de O'Higgins, y qué desafío sugiere ese tiempo?", "Cinco años; sugiere que el nuevo orden tardó en estabilizarse", "1823 menos 1818 son cinco años de dificultades."),
    ],
    ctx=("Para un panel del colegio, un grupo escribe: «En 1818 Chile era un país organizado, con ciudadanos iguales y leyes aceptadas por todos». ¿Cuál de los términos del vocabulario muestra que la frase se adelanta: «Estado nacional» o «independencia»?", "«Estado nacional», porque organizar instituciones y leyes comunes tomó años", "La independencia se declara; el Estado se construye después."),
    sc=[("En Historia: ¿qué es una república?", "Una forma de gobierno con autoridades no hereditarias y sujetas a una constitución", "Se define por cargos temporales y ley."),
        ("¿Qué es la ciudadanía?", "La condición de quien tiene derechos y deberes políticos", "Incluye, por ejemplo, el derecho a elegir."),
        ("Nombra un desafío que dejó la independencia.", "Por ejemplo: organizar un Estado nacional o lograr la igualdad", "Eran tareas pendientes tras la declaración.")],
    op=("Un compañero resume la independencia en tres líneas: «1810 comenzó, 1818 se declaró, desde entonces todo fue igual para todos». Escribe: una frase que corrija esa idea, dos desafíos que dejó la independencia y un hecho de 1810 a 1823 que sirva de evidencia (por ejemplo, la Reconquista o la renuncia de O'Higgins).",
        "La independencia no trajo igualdad inmediata. Los desafíos fueron crear un orden republicano y formar un Estado nacional. Evidencia: en 1814 la batalla de Rancagua dio paso a la Reconquista, lo que muestra que el proceso tuvo retrocesos.",
        ["corrige la idea de igualdad inmediata", "nombra dos desafíos", "usa un hecho fechado entre 1810 y 1823"], ["tres partes claras en pocas frases"], ["decir que todo cambió de inmediato", "no entregar ningún hecho"], "Léele tu respuesta a una persona de tu casa y pídele que señale cuál fue tu evidencia."),
    reinforce="En una tarjeta anota las cinco fechas de la línea de tiempo y, al lado de cada una, una palabra que la resuma.",
    extend="Escribe una frase que explique qué diferencia hay entre «independencia» y «Estado nacional».",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = ("Fuente A (de ejemplo, escrita para este ejercicio, simula un bando oficial de 1818): «Habitantes de Chile: la nación es libre. Todos obedecerán las leyes del Director Supremo y entregarán lo que el ejército necesite.» "
      "Fuente B (de ejemplo, simula una carta privada de 1819): «Entregué cuarenta mulas y dos cosechas al ejército y aún no recibo pago. Temo perder la hacienda.» "
      "Fuente C (de ejemplo, simula un texto escolar actual): «La independencia inició la formación de un orden republicano, aunque no resolvió de inmediato las desigualdades sociales.»")
build(
    OA, 2, F2,
    use="Aprenderé a distinguir tipos de fuentes sobre la independencia y a preguntarles quién las escribió, cuándo y para qué. Sirve para elegir evidencia confiable al evaluar un proceso histórico.",
    prior=["Sé qué es una línea de tiempo.", "Sé que no todas las personas de una época piensan igual.", "Sé distinguir un hecho de una opinión."],
    explain=[
        "Una fuente histórica es cualquier testimonio que permite conocer el pasado: un bando, una carta, un mapa, una constitución o un texto actual. Una fuente primaria nace en la época que se estudia, como un decreto o una carta de 1819. Una fuente secundaria se escribe después, como un libro escolar, y explica o interpreta lo ocurrido usando otras fuentes.",
        "Para analizar una fuente pregunto por su contexto: quién la escribió, cuándo, dónde y con qué propósito. Un bando oficial busca ordenar a la población; una carta privada cuenta una experiencia personal. Cada fuente muestra una perspectiva, es decir, un punto de vista según la posición de quien habla. Por eso ninguna fuente sola cuenta toda la historia.",
        "Al evaluar las transformaciones de la independencia combino fuentes de distinto tipo. Un decreto muestra lo que el gobierno quería hacer; una carta muestra cómo lo vivió una persona; un texto actual ofrece una visión de conjunto. Contrastar sus datos permite ver si se confirman entre sí o si se contradicen.",
    ],
    vocab=[("fuente primaria", "testimonio nacido en la época que se estudia"), ("fuente secundaria", "texto posterior que interpreta lo ocurrido a partir de otras fuentes"), ("contexto", "circunstancias de quién, cuándo, dónde y para qué se creó una fuente"), ("propósito", "intención con que alguien escribió una fuente"), ("perspectiva", "punto de vista según la posición de quien habla")],
    worked=[
        ("Clasificar una fuente", "Se encuentra un bando de 1818 firmado por el gobierno. ¿Es fuente primaria o secundaria, y cuál es su propósito más probable?",
         ["Fue escrito en 1818, en la época estudiada: primaria.", "Un bando es una orden pública: busca informar y ordenar a la población."], "Primaria; busca ordenar a la población"),
        ("Contrastar dos fuentes", "Un decreto de ejemplo dice que el ejército recibirá lo necesario, y una carta de ejemplo cuenta que a una familia no le pagaron lo entregado. ¿Qué muestra el contraste?",
         ["El decreto muestra lo que el gobierno ordenaba.", "La carta muestra cómo lo vivió una persona.", "Juntos, enseñan que el costo de la guerra recayó en los particulares."], "Que lo ordenado y lo vivido pudieron diferir"),
    ],
    mistakes=[
        ("Creer que una fuente primaria siempre dice la verdad completa.", "Quien la escribió tenía un propósito y un punto de vista.", "Pregunta quién escribió, cuándo y para qué."),
        ("Usar un solo documento para explicar todo el proceso.", "Una fuente solo muestra una parte de lo ocurrido.", "Contrasta al menos dos fuentes de tipo distinto."),
    ],
    T=[
        ("En Historia: ¿qué diferencia hay entre una fuente primaria y una secundaria?", "La primaria nació en la época estudiada; la secundaria se escribió después e interpreta", "Se distinguen por el momento en que se crean."),
        ("{F} ¿Cuál de las fuentes (A, B o C) es secundaria?", "La fuente C", "Es un texto escolar actual que interpreta lo ocurrido."),
        ("En Historia: ¿qué es el contexto de una fuente?", "Las circunstancias de quién, cuándo, dónde y para qué se creó", "Permite interpretarla bien."),
        ("{F} ¿Cuál es el propósito más probable de la fuente A? A) ordenar a la población y pedir colaboración, B) contar una experiencia íntima, C) explicar la historia a estudiantes de hoy.", "A", "Un bando oficial manda e informa."),
        ("{F} La fuente B cuenta que la familia de la hacienda no recibió pago. ¿Qué perspectiva muestra? A) la de una persona que vivió el costo de la guerra, B) la de un historiador actual, C) la de un oficial que redactó el bando.", "A", "Es una experiencia personal y privada."),
        ("{F} Un compañero usa solo la fuente A y concluye que «todos colaboraron felices con el ejército». ¿Qué fuente contradice la idea?", "La fuente B", "Muestra a alguien perjudicado por la entrega de bienes."),
        ("=", "{F} La fuente B menciona 40 mulas entregadas. Si el ejército recibió esa cifra de 9 haciendas parecidas, ¿cuántas mulas fueron en total?", "40*9", "Se multiplica la cifra de una hacienda por las nueve."),
        ("Si la carta se escribió en 1819 y un texto escolar se imprimió 200 años después, ¿en qué año se imprimió?", "En 2019", "Se suma el tiempo transcurrido a la fecha de la carta: 1819 + 200."),
        ("{F} La fuente C dice que la independencia «no resolvió de inmediato las desigualdades». ¿Qué fuente de las otras dos aporta un ejemplo de dificultad concreta?", "La fuente B, porque cuenta un problema de pago a una familia", "La carta da un caso concreto."),
        ("{F} ¿Es confiable usar solo la fuente C para saber qué sintió una persona en 1819? Responde con una frase.", "No, porque es un texto posterior y general, y no cuenta una vivencia de la época", "Para vivencias conviene una fuente primaria."),
        ("Un libro actual cita una carta de 1820 y dice que el autor de la carta «exageró» sus pérdidas. ¿Qué dos fuentes hay y de qué tipo es cada una?", "La carta de 1820, primaria, y el libro actual, secundaria", "Una es testimonio de la época y la otra interpreta."),
        ("Para evaluar cómo vivieron la independencia distintas personas, ¿qué conjunto de fuentes es mejor? A) tres decretos del gobierno, B) un decreto, una carta privada y un texto escolar actual, C) tres textos escolares iguales.", "B", "Combina tipos distintos y perspectivas distintas."),
        ("{F} Si la fuente A dice «la nación es libre» y la fuente B habla de temor a perder la hacienda, escribe una pregunta que ayude a contrastarlas.", "Por ejemplo: ¿cómo afectó la guerra a las personas aunque el gobierno hablara de libertad?", "Une la promesa del bando con la vivencia de la carta."),
    ],
    ctx=("Tu curso debe elegir una fuente para un afiche sobre las dificultades de la independencia. Opciones: A) un bando que ordena obediencia, B) una carta que cuenta pérdidas de cosechas por la guerra, C) un dibujo de un desfile festivo. ¿Cuál sirve mejor para mostrar dificultades de la población?", "B", "Muestra un problema vivido, no una orden ni una fiesta."),
    sc=[("En Historia: ¿qué es una perspectiva?", "El punto de vista según la posición de quien habla", "Todas las fuentes tienen una."),
        ("Nombra una fuente primaria posible sobre la independencia.", "Por ejemplo: un bando, una carta o una constitución de la época", "Nacen en el periodo estudiado."),
        ("¿Por qué conviene contrastar fuentes?", "Porque cada una muestra una parte y así se confirman o se contradicen los datos", "Evita conclusiones con un solo punto de vista.")],
    op=("{F} Elige dos de las tres fuentes y completa para cada una: tipo (primaria o secundaria), propósito y qué dato nos entrega sobre la independencia. Termina con una frase que diga qué ganan al usar ambas juntas.",
        "Fuente A: primaria; propósito: ordenar a la población; dato: el gobierno pedía obediencia y apoyo al ejército. Fuente B: primaria; propósito: contar una pérdida personal; dato: una familia entregó mulas y cosechas sin recibir pago. Juntas muestran lo ordenado y lo vivido.",
        ["clasifica cada fuente", "señala propósito y dato", "justifica el valor de usar dos fuentes"], ["dos fuentes analizadas y una conclusión"], ["no distinguir primaria de secundaria", "no explicar la ganancia de contrastar"], "Pide a una persona de tu casa que te diga si tus dos fuentes muestran perspectivas distintas."),
    reinforce="Elige un documento de tu casa (una boleta o una carta) y anota si es primario o secundario y para qué se escribió.",
    extend="Escribe cómo cambiaría tu conclusión sobre la independencia si solo tuvieras bandos del gobierno.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = ("Tabla de ejemplo, Chile antes de 1810 y hacia 1833. Autoridad: antes, un gobernador designado por el rey; hacia 1833, un presidente y un Congreso según una constitución. "
      "Comercio: antes, reglas del monopolio con España; hacia 1833, comercio con otras naciones. "
      "Esclavitud: antes, existía; hacia 1833, abolida desde 1823. "
      "Tierra: antes y hacia 1833, grandes haciendas en pocas manos. "
      "Voto: hacia 1833, solo algunos hombres con propiedad que sabían leer y escribir. "
      "Sur del río Biobío: antes y hacia 1833, territorio mapuche fuera del control del Estado.")
build(
    OA, 3, F3,
    use="Aprenderé a separar lo que cambió y lo que continuó tras la independencia, y a ubicarlo en el territorio. Sirve para evaluar si las transformaciones fueron profundas o limitadas.",
    prior=["Sé que la independencia fue un proceso entre 1810 y 1823.", "Sé qué es una fuente y una perspectiva.", "Sé leer una tabla de dos columnas."],
    explain=[
        "Cambio es algo que se modifica con el tiempo; continuidad es algo que se mantiene. Una misma época suele tener ambos. Tras la independencia hubo cambios importantes: la autoridad ya no era un gobernador designado por el rey, sino un presidente y un Congreso que debían respetar una constitución. También se abrió el comercio con otras naciones, y la esclavitud se abolió en 1823.",
        "Sin embargo, muchas cosas continuaron. La tierra seguía concentrada en grandes haciendas, la sociedad mantenía fuertes diferencias entre ricos y pobres, y la participación política estaba limitada: hacia 1833 solo votaba un grupo reducido de hombres. Esto muestra que la soberanía popular se aplicó al principio de forma restringida, es decir, solo a una parte de la población.",
        "El territorio también importa. El Estado no controlaba todo el espacio del país: al sur del río Biobío seguía el territorio mapuche, con autoridades propias. Formar un Estado nacional significó, con el tiempo, extender su autoridad por todo el territorio, algo que generó conflictos. Para evaluar un proceso, entonces, pregunto qué cambió, qué siguió igual y en qué lugares.",
    ],
    vocab=[("cambio", "algo que se modifica con el paso del tiempo"), ("continuidad", "algo que se mantiene a pesar del tiempo"), ("hacienda", "gran propiedad agrícola en pocas manos"), ("abolir", "eliminar por ley una práctica o institución"), ("restringido", "limitado a una parte de las personas")],
    worked=[
        ("Clasificar un rasgo", "En la tabla, el comercio pasa del monopolio con España al comercio con otras naciones. ¿Es cambio o continuidad? ¿Por qué?",
         ["Comparo las dos columnas: antes monopolio, después comercio abierto.", "El rasgo se modifica, no se mantiene."], "Cambio, porque las reglas del comercio se modificaron"),
        ("Evaluar un cambio con límites", "La esclavitud se abolió en 1823. ¿Significa que la sociedad pasó a ser igualitaria?",
         ["La abolición es un cambio importante.", "Pero otros datos muestran continuidad: haciendas concentradas y voto restringido.", "Entonces el cambio fue real pero parcial."], "No; fue un cambio real, pero otras desigualdades continuaron"),
    ],
    mistakes=[
        ("Decir que todo cambió con la independencia.", "Varios rasgos, como las haciendas y la desigualdad, se mantuvieron.", "Revisa qué rasgos aparecen igual antes y después."),
        ("Decir que nada cambió porque siguió habiendo desigualdad.", "Hubo cambios reales, como la constitución y la abolición de la esclavitud.", "Reconoce cambios y continuidades a la vez."),
    ],
    T=[
        ("En Historia: ¿qué es una continuidad?", "Algo que se mantiene a pesar del paso del tiempo", "Se opone al cambio."),
        ("{F} ¿Qué rasgo de la tabla pasó de un gobernador designado por el rey a un presidente y un Congreso?", "La autoridad", "Es el primer ítem de la tabla."),
        ("{F} Según la tabla, ¿desde qué año estaba abolida la esclavitud?", "1823", "El dato aparece en la fila de esclavitud."),
        ("{F} ¿Cuál de estos rasgos es una continuidad? A) el comercio con otras naciones, B) las grandes haciendas en pocas manos, C) la elección de un Congreso.", "B", "Aparece igual antes y después."),
        ("{F} ¿Por qué se dice que la soberanía popular se aplicó de forma restringida hacia 1833?", "Porque solo votaban algunos hombres con propiedad que sabían leer y escribir", "Gran parte de la población quedaba sin voto."),
        ("{F} Según la tabla, ¿qué ocurría al sur del río Biobío? A) estaba bajo control total del Estado, B) seguía siendo territorio mapuche fuera del control del Estado, C) no tenía habitantes.", "B", "La tabla lo indica como continuidad."),
        ("=", "La esclavitud se abolió en 1823. Si el voto restringido seguía vigente en 1833, ¿cuántos años pasaron entre ambos hitos?", "1833-1823", "Se restan los años."),
        ("=", "En una hacienda de ejemplo, 120 personas trabajan la tierra de 1 dueño. Si otras 4 haciendas iguales siguen el mismo esquema, ¿cuántas personas trabajan en las 5 haciendas sin ser dueñas?", "120*5", "Se multiplica la cifra de una hacienda por cinco."),
        ("{F} Un compañero dice: «La independencia cambió el gobierno, así que cambió también la propiedad de la tierra». ¿Qué fila de la tabla lo contradice?", "La fila de tierra, que muestra haciendas en pocas manos antes y después", "Es una continuidad."),
        ("{F} ¿Por qué el territorio al sur del Biobío es un desafío para formar un Estado nacional?", "Porque el Estado todavía no controlaba ese espacio y debía definir cómo relacionarse con el pueblo mapuche", "Un Estado nacional necesita autoridad en todo su territorio."),
        ("Explica con una frase por qué la abolición de la esclavitud es un cambio real aunque la desigualdad continuara.", "Porque terminó legalmente con una forma de propiedad sobre personas, aunque otras diferencias siguieron", "Un cambio puede ser real y parcial."),
        ("{F} Evalúa: «La independencia fue solo un cambio de nombre». ¿Qué respuesta usa evidencia de la tabla? A) Es falsa: cambió la autoridad y se abolió la esclavitud, aunque las haciendas continuaron; B) Es verdadera: nada cambió; C) Es falsa porque el voto fue universal.", "A", "Combina cambios y continuidades de la tabla."),
        ("{F} Anota dos continuidades y un cambio de la tabla.", "Continuidades: haciendas y territorio mapuche al sur del Biobío; cambio: autoridad con presidente y Congreso", "Se toman filas distintas de la tabla."),
    ],
    ctx=("Para una exposición, un grupo escribe: «Tras la independencia, todo fue distinto para todos los habitantes». {F} Tu tarea es corregir la frase con evidencia de la tabla sobre el voto y la tierra. ¿Qué dos datos usas?", "El voto restringido a algunos hombres con propiedad y las haciendas concentradas en pocas manos", "Ambos muestran continuidades de desigualdad."),
    sc=[("En Historia: ¿qué es un cambio?", "Algo que se modifica con el paso del tiempo", "Se opone a la continuidad."),
        ("{F} Nombra un cambio y una continuidad de la tabla.", "Cambio: presidente y Congreso; continuidad: grandes haciendas", "Están en filas distintas."),
        ("¿Qué significa que la ciudadanía era restringida?", "Que solo una parte de la población podía votar", "Se limitaba por propiedad, sexo y alfabetización.")],
    op=("{F} Elige tres filas de la tabla y clasifícalas como cambio o continuidad. Luego escribe una frase que responda: ¿fue profunda o limitada la transformación en la sociedad hacia 1833? Usa al menos un dato de la tabla.",
        "Autoridad: cambio. Esclavitud: cambio. Tierra: continuidad. Fue una transformación política importante, pero limitada en la sociedad, porque las haciendas y el voto restringido seguían.",
        ["clasifica tres filas", "responde con una evaluación", "usa un dato de la tabla"], ["tres clasificaciones y una evaluación"], ["decir que todo cambió", "decir que nada cambió"], "Cuéntale tu evaluación a una persona de tu casa y pídele que señale el dato de la tabla que la apoya."),
    reinforce="Anota un cambio y una continuidad que veas en tu barrio comparando hoy con lo que te cuenten personas mayores.",
    extend="Escribe por qué el sur del río Biobío es importante para entender los límites del Estado nacional.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = ("Testimonios de ejemplo escritos para este ejercicio. "
      "Patriota criollo (propietario): «Queremos gobernarnos nosotros mismos y comerciar libremente.» "
      "Realista (funcionario del rey): «Rompen la lealtad al rey y traen desorden a estas tierras.» "
      "Mujer de un pueblo cercano a la guerra: «Cuidé heridos, cosí uniformes y perdí a mi hermano; nadie me preguntó mi opinión.» "
      "Persona esclavizada: «Si luchamos, ¿seremos libres de verdad cuando termine la guerra?»")
build(
    OA, 4, F4,
    use="Aprenderé a contrastar a los actores de la independencia, sus causas y perspectivas. Sirve para entender que el proceso no lo vivieron todos igual.",
    prior=["Sé distinguir cambio y continuidad.", "Sé qué es una fuente y una perspectiva.", "Sé que una causa explica por qué ocurre un hecho."],
    explain=[
        "Un actor histórico es una persona o un grupo que participa en los hechos. En la independencia hubo patriotas, que querían gobernarse sin depender del rey, y realistas, que seguían leales a la monarquía. Pero también participaron mujeres, soldados, campesinos, personas esclavizadas y pueblos indígenas, con posturas y expectativas distintas.",
        "Los hechos tienen varias causas a la vez, lo que se llama multicausalidad. En 1808 el rey de España quedó fuera del trono por una invasión francesa, y eso abrió una crisis de autoridad en sus territorios. A eso se sumaron el descontento de los criollos, hijos de españoles nacidos en América, con las restricciones al comercio, y la influencia de ideas ilustradas sobre la soberanía popular y los derechos.",
        "Contrastar perspectivas es comparar cómo cada actor entendió y vivió el proceso. Un criollo propietario esperaba poder gobernar y comerciar; una persona esclavizada esperaba su libertad; una mujer cargó con tareas de guerra sin voz política. Por eso la independencia trajo oportunidades distintas, y las expectativas de muchos no se cumplieron de inmediato.",
    ],
    vocab=[("actor histórico", "persona o grupo que participa en los hechos"), ("patriota", "partidario de la independencia"), ("realista", "partidario de mantener la lealtad al rey"), ("criollo", "hijo o hija de españoles nacido en América"), ("multicausalidad", "idea de que un hecho tiene varias causas a la vez")],
    worked=[
        ("Identificar la perspectiva", "En los testimonios, un propietario dice: «Queremos gobernarnos nosotros mismos y comerciar libremente». ¿Qué actor habla y qué espera?",
         ["Es un patriota criollo propietario.", "Espera autogobierno y libertad de comercio."], "Un patriota criollo; espera autogobierno y libre comercio"),
        ("Separar causas", "¿Cuáles son dos causas de la independencia, según la explicación?",
         ["La crisis de la monarquía española en 1808.", "El descontento criollo con las restricciones comerciales y la influencia de ideas ilustradas."], "La crisis de 1808 y el descontento criollo, junto con las ideas ilustradas"),
    ],
    mistakes=[
        ("Creer que toda la población quería lo mismo.", "Cada actor tuvo intereses y expectativas propias.", "Pregunta qué esperaba cada grupo."),
        ("Explicar la independencia con una sola causa.", "Los procesos históricos tienen varias causas que se combinan.", "Busca causas externas, económicas e ideológicas."),
    ],
    T=[
        ("En Historia: ¿qué es un actor histórico?", "Una persona o grupo que participa en los hechos", "Incluye a más que los gobernantes."),
        ("En Historia: ¿qué es un criollo?", "Un hijo o hija de españoles nacido en América", "Es un término propio de la época colonial."),
        ("En Historia: ¿qué es la multicausalidad?", "La idea de que un hecho tiene varias causas a la vez", "Se opone a explicar con una sola causa."),
        ("{F} ¿Quién dice que la ruptura trae desorden? A) el realista, B) el patriota criollo, C) la persona esclavizada.", "A", "Defiende la lealtad al rey."),
        ("{F} ¿Qué expectativa expresa la persona esclavizada? A) obtener su libertad real al terminar la guerra, B) mantener las haciendas, C) volver a España.", "A", "Pregunta si será libre de verdad."),
        ("{F} ¿Qué actor dice que nadie le preguntó su opinión, y qué muestra eso?", "La mujer; muestra que no tenía voz política aunque participó en la guerra", "Participación en tareas, sin derechos políticos."),
        ("=", "En un barrio de ejemplo, 240 familias apoyaron a los patriotas y 90 a los realistas. ¿Cuántas familias participaron en total?", "240+90", "Se suman los dos grupos."),
        ("=", "En una hacienda de ejemplo vivían 56 personas esclavizadas. Si 14 se unieron al ejército patriota, ¿cuántas quedaron en la hacienda?", "56-14", "Se resta lo que se fue del total."),
        ("Un texto dice: «La independencia ocurrió solo porque las ideas ilustradas llegaron a Chile». ¿Qué falla en esa explicación?", "Que usa una sola causa y deja fuera la crisis de la monarquía y el descontento criollo", "El proceso tuvo varias causas."),
        ("{F} ¿Qué perspectiva comparten el patriota criollo y la persona esclavizada? A) ambos esperan cambios, aunque distintos, B) ambos son realistas, C) ambos tienen ya los mismos derechos.", "A", "Ambos esperan algo de la independencia, pero no lo mismo."),
        ("{F} Explica por qué la independencia no trajo las mismas oportunidades a todos los actores.", "Porque cada grupo tenía expectativas distintas y no todos tuvieron derechos políticos ni libertad inmediata", "Varía según la posición social."),
        ("¿Qué respuesta usa mejor la multicausalidad? A) La independencia ocurrió por la invasión francesa a España; B) Hubo una crisis de la monarquía, descontento criollo con el comercio y nuevas ideas sobre la soberanía popular; C) Fue solo cosa de un general.", "B", "Combina varias causas."),
        ("{F} Elige un actor y escribe una pregunta que le harías para entender su perspectiva.", "Por ejemplo, a la mujer: ¿qué tareas hizo en la guerra y qué esperaba después?", "La pregunta parte del testimonio."),
    ],
    ctx=("En una charla del colegio, un expositor dice: «Todos los habitantes celebraron la independencia por igual». {F} Con los testimonios sobre la mujer y la persona esclavizada, ¿qué dato usas para cuestionarlo?", "Que la mujer no tuvo voz política y la persona esclavizada dudaba de ser libre de verdad", "Muestra expectativas y vivencias distintas."),
    sc=[("En Historia: ¿qué quería un patriota?", "Gobernarse sin depender del rey", "Defendía la independencia."),
        ("¿Qué quería un realista?", "Mantener la lealtad al rey", "Defendía la monarquía."),
        ("Nombra una causa de la independencia.", "Por ejemplo: la crisis de la monarquía en 1808", "Fue una causa externa que abrió la crisis.")],
    op=("{F} Elige dos actores de los testimonios y escribe: qué esperaba cada uno de la independencia, qué los diferencia y una causa de la independencia que puedas relacionar con uno de ellos.",
        "Elijo al patriota criollo y a la persona esclavizada. El criollo esperaba autogobierno y libre comercio; la persona esclavizada, libertad real. Los diferencia que uno ya tenía propiedad y el otro no. La causa del descontento por el comercio se relaciona con el criollo.",
        ["compara las expectativas de dos actores", "señala una diferencia", "relaciona una causa con un actor"], ["tres partes claras"], ["suponer que todos esperaban lo mismo", "dar solo una causa sin relacionarla"], "Pide a una persona de tu casa que adivine qué actor describiste."),
    reinforce="Dibuja una tabla con cuatro actores y escribe al lado lo que esperaban de la independencia.",
    extend="Escribe por qué las expectativas de las mujeres y de las personas esclavizadas muestran límites de la ciudadanía.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = ("Pregunta de investigación de ejemplo: ¿cambió de manera profunda la vida de la mayoría de los habitantes tras la independencia? "
      "Evidencia 1: se aprobaron constituciones y se eligieron autoridades. "
      "Evidencia 2: se abolió la esclavitud en 1823. "
      "Evidencia 3: el voto quedó limitado a algunos hombres con propiedad que sabían leer y escribir. "
      "Evidencia 4: las grandes haciendas siguieron concentrando la tierra.")
build(
    OA, 5, F5,
    use="Aprenderé a construir un argumento histórico con una afirmación, evidencia y una explicación. Sirve para defender una evaluación de la independencia con datos.",
    prior=["Sé distinguir cambio y continuidad.", "Sé contrastar perspectivas de varios actores.", "Sé usar fuentes como evidencia."],
    explain=[
        "Un argumento histórico tiene tres partes. La afirmación es la respuesta que doy a la pregunta. La evidencia son los datos de las fuentes que la apoyan. La explicación es el razonamiento que conecta la evidencia con la afirmación y dice por qué esos datos sí prueban lo que digo. Sin evidencia, una afirmación es solo una opinión.",
        "Para evaluar la independencia puedo preguntar: ¿qué tan profundas fueron sus transformaciones? Una buena respuesta reconoce matices. Puedo afirmar, por ejemplo, que el cambio político fue profundo pero la transformación social fue limitada. Uso evidencia de ambos lados y explico por qué pesa más una que otra.",
        "También anticipo una objeción, que es un argumento contrario. Si alguien dice que «todo cambió», respondo con datos de continuidad. Un argumento sólido no ignora lo que lo contradice: lo toma en cuenta. Además, dejo claro el límite de mi evidencia, por ejemplo si solo dispongo de fuentes de un grupo social.",
    ],
    vocab=[("afirmación", "respuesta que se defiende ante una pregunta"), ("evidencia", "dato de una fuente que apoya o contradice una afirmación"), ("explicación", "razonamiento que conecta la evidencia con la afirmación"), ("objeción", "argumento contrario a lo que se afirma"), ("matiz", "detalle que impide una respuesta absoluta")],
    worked=[
        ("Identificar las partes", "Argumento: «El cambio político fue profundo (afirmación), porque se aprobaron constituciones (evidencia), ya que el poder dejó de depender del rey (explicación)». ¿Cuál es la evidencia?",
         ["La evidencia es el dato de una fuente.", "Es lo que está entre paréntesis como «se aprobaron constituciones»."], "Se aprobaron constituciones"),
        ("Anticipar una objeción", "{F} Un compañero afirma que «todo cambió en la sociedad». ¿Qué respuesta usa evidencia contraria?",
         ["Busco datos de continuidad.", "Las haciendas siguieron concentrando la tierra y el voto era restringido."], "Responder con las haciendas y el voto restringido"),
    ],
    mistakes=[
        ("Dar una afirmación sin ninguna evidencia.", "Queda como opinión que nadie puede comprobar.", "Agrega un dato de fuente por cada afirmación."),
        ("Escoger solo la evidencia que apoya mi idea y esconder la contraria.", "El argumento se vuelve parcial.", "Menciona la evidencia contraria y explica por qué pesa menos o más."),
    ],
    T=[
        ("En Historia: ¿qué es una evidencia?", "Un dato de una fuente que apoya o contradice una afirmación", "Sustenta el argumento."),
        ("En Historia: ¿para qué sirve la explicación en un argumento?", "Para conectar la evidencia con la afirmación", "Muestra por qué el dato prueba la idea."),
        ("{F} ¿Qué evidencia indica que hubo un cambio político? A) la evidencia 1, B) la evidencia 3, C) la evidencia 4.", "A", "Hablan de constituciones y elección de autoridades."),
        ("{F} ¿Qué evidencia muestra una limitación de la ciudadanía? A) la evidencia 2, B) la evidencia 3, C) la evidencia 1.", "B", "Dice quién podía votar."),
        ("{F} ¿Qué evidencia muestra una continuidad social? A) la evidencia 4, B) la evidencia 1, C) la evidencia 2.", "A", "Las haciendas se mantuvieron."),
        ("{F} Un estudiante afirma «Sí, cambió profundamente la vida de la mayoría». ¿Qué dos evidencias podrían usarse en su contra?", "La evidencia 3 sobre el voto restringido y la evidencia 4 sobre las haciendas", "Muestran continuidad de desigualdad."),
        ("=", "En una escuela de ejemplo hay 6 grupos y cada grupo presenta 3 evidencias. ¿Cuántas evidencias se presentan en total?", "6*3", "Se multiplica el número de grupos por las evidencias de cada uno."),
        ("=", "De 45 estudiantes, 28 usaron evidencia de cambio y el resto de continuidad. ¿Cuántos usaron evidencia de continuidad?", "45-28", "Se resta lo que usó cambio del total."),
        ("{F} Completa el argumento: «Fue profundo el cambio político, aunque limitado el social, porque ... (evidencia 1) y ... (evidencia 4)». Escribe qué falta en cada espacio.", "Se aprobaron constituciones y se eligieron autoridades; las haciendas siguieron concentrando la tierra", "Cada espacio toma una evidencia."),
        ("{F} ¿Qué objeción podría hacer alguien que cree que el cambio fue completo? Responde con una frase.", "Que se abolió la esclavitud y hubo constituciones, así que la sociedad ya era igualitaria", "Ignora la evidencia de continuidad."),
        ("¿Cuál es un argumento completo? A) Fue profundo, y ya; B) El cambio político fue profundo porque se eligieron autoridades, lo que muestra que el poder ya no dependía del rey; C) Mucha gente opina eso.", "B", "Tiene afirmación, evidencia y explicación."),
        ("{F} Un estudiante solo cita la evidencia 2 para decir que la sociedad cambió totalmente. ¿Qué matiz le falta?", "Que otras evidencias, como el voto restringido, muestran límites", "Un solo dato no basta para un juicio general."),
        ("{F} Escribe una afirmación matizada que use al menos una evidencia de cambio y una de continuidad.", "Hubo cambios políticos y legales importantes, pero la desigualdad social continuó, porque se abolió la esclavitud y las haciendas seguían concentradas", "Equilibra ambos tipos de evidencia."),
    ],
    ctx=("En un debate de curso, una estudiante dice: «La independencia fue un fracaso porque los pobres seguían sin votar». ¿Qué evidencia de cambio puedes mencionar para matizar su juicio?", "Que se aprobaron constituciones y se abolió la esclavitud en 1823", "Reconoce un fracaso parcial y cambios reales."),
    sc=[("En Historia: ¿qué es una objeción?", "Un argumento contrario a lo que se afirma", "Se anticipa para fortalecer el argumento."),
        ("¿Cuáles son las tres partes de un argumento histórico?", "Afirmación, evidencia y explicación", "Forman la estructura básica."),
        ("¿Por qué conviene dejar claro el límite de la evidencia?", "Porque ayuda a no generalizar más allá de lo que muestran los datos", "Evita conclusiones excesivas.")],
    op=("{F} Responde la pregunta de investigación con un argumento de tres partes: afirmación, dos evidencias de la lista y explicación. Agrega una objeción posible y tu respuesta a ella.",
        "Afirmación: el cambio político fue profundo, pero la vida de la mayoría cambió poco. Evidencias: se aprobaron constituciones; las haciendas siguieron concentrando la tierra. Explicación: el poder ya no dependía del rey, pero las bases económicas no cambiaron. Objeción: «se abolió la esclavitud». Respuesta: fue un cambio importante, aunque no eliminó las demás desigualdades.",
        ["afirmación clara", "dos evidencias de la lista", "explicación que las conecta", "objeción respondida"], ["un argumento de cuatro partes"], ["no incluir evidencia", "no responder la objeción"], "Pide a una persona de tu casa que intente refutar tu afirmación y responde a su objeción."),
    reinforce="Escribe una afirmación sobre tu barrio y apóyala con dos datos que hayas observado.",
    extend="Reescribe tu afirmación incluyendo un matiz que reconozca algo de la posición contraria.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 6
F6 = ("Ficha de ejemplo, herencias de la independencia. "
      "Orden republicano: separación de poderes (Ejecutivo, Legislativo y Judicial) y constituciones. "
      "Ciudadanía: hoy pueden votar las personas desde los 18 años, mujeres y hombres, sin exigir propiedad. "
      "Estado nacional: instituciones comunes, como los tribunales, las escuelas públicas y los servicios del Estado. "
      "Desafíos actuales (de ejemplo): participación baja de jóvenes en elecciones, desigualdades entre regiones y reconocimiento de los pueblos indígenas.")
build(
    OA, 6, F6,
    use="Aprenderé a explicar por qué las transformaciones de la independencia importan en el Chile actual y a reconocer sus límites. Sirve para relacionar el pasado con decisiones de hoy.",
    prior=["Sé qué son república, soberanía popular, ciudadanía y Estado nacional.", "Sé distinguir cambio y continuidad.", "Sé construir un argumento con evidencia."],
    explain=[
        "Evaluar la relevancia de un proceso es preguntar qué de él sigue vigente hoy. De la independencia nacen ideas que usamos a diario: tenemos una constitución, autoridades que se eligen, poderes del Estado separados y una ciudadanía que puede votar. También vivimos dentro de un Estado nacional, con instituciones comunes como los tribunales y las escuelas públicas.",
        "Pero esas herencias no son iguales a las del siglo XIX. La ciudadanía de hoy es mucho más amplia: votan mujeres y hombres desde los 18 años sin exigir propiedad. Esto muestra una proyección, es decir, cómo una idea se desarrolla con el tiempo, y una ampliación de derechos que no ocurrió de inmediato. Un valor del pasado, como la soberanía popular, pudo crecer gracias a nuevas demandas de la sociedad.",
        "Evaluar también implica ver límites y desafíos pendientes. Aún hay desigualdades entre regiones, baja participación en algunas elecciones y discusiones sobre el reconocimiento de los pueblos indígenas. Un buen juicio histórico no idealiza ni condena el pasado: explica qué logró, qué dejó pendiente y por qué eso importa hoy.",
    ],
    vocab=[("herencia", "idea o institución del pasado que sigue presente"), ("proyección", "desarrollo de una idea con el paso del tiempo"), ("ampliación de derechos", "extensión de un derecho a más personas"), ("relevancia", "importancia de algo para el presente"), ("desafío pendiente", "tarea que aún no se resuelve")],
    worked=[
        ("Relacionar pasado y presente", "La ficha dice que hoy hay separación de poderes. ¿De qué proceso de la independencia es herencia?",
         ["Busco la idea en el orden republicano.", "Nace del intento de limitar el poder con una constitución y repartirlo."], "Del orden republicano que se buscó construir"),
        ("Evaluar una ampliación", "Hacia 1833 votaban pocos hombres con propiedad; hoy votan mujeres y hombres desde los 18 años. ¿Qué muestra eso?",
         ["La soberanía popular se aplicó de forma restringida al comienzo.", "Con el tiempo se amplió."], "Una ampliación progresiva de la ciudadanía"),
    ],
    mistakes=[
        ("Creer que las instituciones de hoy existen igual que en 1818.", "Cambiaron mucho: por ejemplo, el voto se amplió.", "Compara qué se mantiene y qué se transformó."),
        ("Idealizar la independencia como un proceso sin límites ni conflictos.", "Dejó desigualdades y conflictos territoriales pendientes.", "Reconoce logros y límites a la vez."),
    ],
    T=[
        ("En Historia: ¿qué es una herencia histórica?", "Una idea o institución del pasado que sigue presente", "Aparece aún en la vida de hoy."),
        ("{F} Según la ficha, ¿desde qué edad pueden votar las personas hoy?", "Desde los 18 años", "Lo dice la fila de ciudadanía."),
        ("{F} ¿Cuáles son los tres poderes del Estado que menciona la ficha?", "Ejecutivo, Legislativo y Judicial", "Son los poderes del orden republicano."),
        ("{F} ¿Qué institución común del Estado nacional aparece en la ficha? A) los tribunales, B) la nobleza, C) los virreyes.", "A", "Los tribunales son una institución de todo el país."),
        ("{F} ¿Qué cambio de la ciudadanía muestra la ficha respecto de 1833? A) ya no se exige propiedad y votan mujeres, B) votan solo hombres con propiedad, C) se prohibió el voto.", "A", "La ciudadanía hoy es más amplia."),
        ("Explica con una frase por qué una constitución es una herencia republicana.", "Porque limita el poder de quienes gobiernan y fija reglas comunes, como pedía el nuevo orden", "Era una idea central de la república."),
        ("=", "En un grupo de ejemplo de 30 jóvenes, 18 tienen 18 años o más y pueden votar. ¿Cuántos no pueden votar todavía?", "30-18", "Se resta lo que sí pueden votar."),
        ("=", "En una comuna de ejemplo hay 4 tribunales y cada uno atiende 150 casos por mes. ¿Cuántos casos atienden en un mes?", "4*150", "Se multiplica el número de tribunales por los casos de cada uno."),
        ("{F} Un compañero dice que «hoy somos ciudadanos igual que en 1818». ¿Qué dato de la ficha lo corrige?", "Que hoy votan mujeres y hombres desde los 18 años sin exigir propiedad", "La ciudadanía se amplió."),
        ("{F} ¿Por qué la baja participación de jóvenes es un desafío pendiente para la soberanía popular?", "Porque si no votan, la voluntad del pueblo se expresa menos", "La soberanía popular necesita participación."),
        ("Elige la evaluación equilibrada: A) La independencia resolvió todos los problemas del país; B) Dejó herencias como la república y la ciudadanía, pero también desafíos que siguen pendientes; C) No dejó ninguna herencia.", "B", "Reconoce logros y límites."),
        ("{F} Explica con una frase por qué las desigualdades entre regiones muestran un límite de la formación del Estado nacional.", "Porque un Estado nacional debería llegar con servicios e instituciones a todo su territorio", "Las diferencias regionales muestran tareas pendientes."),
        ("{F} Escribe una frase que evalúe la relevancia de la independencia hoy, usando una herencia y un desafío de la ficha.", "Dejó herencias como la separación de poderes, aunque aún hay desafíos como la baja participación de jóvenes", "Combina una herencia y un desafío."),
    ],
    ctx=("{F} En una charla, alguien dice: «La independencia ya no importa porque pasó hace más de doscientos años». ¿Qué herencia de la ficha usas para responderle?", "La constitución y la separación de poderes, que organizan hoy el gobierno", "Son herencias republicanas aún vigentes."),
    sc=[("En Historia: ¿qué es una proyección?", "El desarrollo de una idea con el paso del tiempo", "Muestra cómo cambia una herencia."),
        ("Nombra una herencia de la independencia que usas hoy.", "Por ejemplo: la constitución o el derecho a votar", "Son instituciones republicanas."),
        ("{F} Nombra un desafío pendiente que mencione la ficha.", "Por ejemplo: la baja participación de jóvenes o las desigualdades entre regiones", "Aparecen en la última fila.")],
    op=("{F} Escribe un párrafo de cinco líneas que evalúe la relevancia de la independencia hoy. Incluye: una herencia, una ampliación de derechos respecto de 1833, un desafío pendiente y una conclusión propia que diga si fue un proceso más de logros o más de tareas pendientes.",
        "La independencia dejó la república y la idea de soberanía popular. Hoy votan mujeres y hombres desde los 18 años, algo que en 1833 no ocurría. Sin embargo, quedan desafíos como las desigualdades entre regiones. Creo que fue un proceso de logros importantes, pero con muchas tareas pendientes, porque los derechos se ampliaron con el tiempo.",
        ["nombra una herencia", "compara con 1833", "señala un desafío", "da una conclusión justificada"], ["párrafo de cinco líneas"], ["idealizar el pasado", "no justificar la conclusión"], "Léele tu párrafo a una persona de tu casa y pídele que diga si convence."),
    reinforce="Escribe tres cosas de tu vida que dependen de instituciones del Estado, como la escuela o la salud pública.",
    extend="Explica cómo cambiaría tu evaluación si la ficha dijera que la participación electoral es muy alta.",
    materials=MAT,
)
