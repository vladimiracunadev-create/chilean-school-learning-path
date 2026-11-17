"""Creación y composición musical 3.º y 4.º medio HC: OAC-04 (analizar estéticamente obras de diferentes épocas y procedencias). Obras y análisis inventados; sin audio ni partituras reales."""
from __future__ import annotations

from hc_ccmu_common import build

O4 = "AR-CCMU-3y4-OAC-04"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (tres obras de ejemplo, inventadas; no son obras reales). "
     "Obra 1, «Canto de trilla», de tradición oral rural (procedencia inventada): una voz sola, sin instrumentos; 5 notas distintas; cuatro estrofas que repiten la misma melodía con distinta letra; tempo moderado y pulso algo flexible. "
     "Obra 2, «Minueto del jardín», de estilo cortesano de épocas pasadas (de ejemplo): teclado y dos violines; compás de 3 pulsos; 90 pulsos por minuto; forma ABA con secciones de 8 compases; una melodía principal con acompañamiento; la dinámica cambia de suave a fuerte de forma gradual. "
     "Obra 3, «Neón», pista electrónica de nuestro siglo (de ejemplo): 120 pulsos por minuto; compás de 4 pulsos; 32 compases; bombo en cada pulso; un motivo de sintetizador repetido en bucle; entran y salen capas cada 8 compases; sin voz.")
build(
    O4, 1, F,
    use="Aprenderé a describir con evidencia cómo obras de distintas épocas y procedencias trabajan los elementos del lenguaje musical, como primer paso de un análisis estético.",
    prior=["Reconozco ritmo, melodía, timbre, textura y forma.", "Sé la diferencia entre repetición, variación y contraste.", "Sé que describir es distinto de opinar."],
    explain=[
        "Un análisis estético de una obra musical describe con evidencia cómo trabaja los elementos del lenguaje musical (ritmo, melodía, armonía, timbre, textura, forma, dinámica y tempo) y qué efecto expresivo producen. El primer paso es describir: anotar rasgos que otra persona pueda comprobar al escuchar. «La obra usa una voz sola» es una descripción; «la obra me da pena» es una impresión.",
        "La textura es la manera en que se combinan las capas sonoras: puede ser una sola línea melódica sin acompañamiento, una melodía con acompañamiento, o varias capas que suenan a la vez. La procedencia de una obra es el lugar y la cultura de donde viene, y la época es el tiempo en que se creó o a que pertenece su estilo. Obras de distintas épocas y procedencias se pueden describir con los mismos elementos del lenguaje musical.",
        "Describir no es juzgar. Una obra más reciente no es mejor ni peor que una más antigua; se analiza lo que hace. Este cuaderno usa obras inventadas, descritas por escrito, porque no se puede reproducir audio ni partituras reales; en clase, tu docente puede aportar audiciones de obras reales y tú aplicarás los mismos pasos.",
    ],
    vocab=[("análisis estético", "estudio de cómo una obra trabaja el lenguaje musical y qué efecto produce"), ("textura", "manera en que se combinan las capas sonoras"), ("procedencia", "lugar y cultura de origen de una obra"),
           ("época", "tiempo al que pertenece una obra o su estilo"), ("evidencia", "dato que se puede comprobar en la obra"), ("rasgo", "característica de una obra que se puede describir")],
    worked=[
        ("Describir la textura", "Una obra ficticia la cantan cuatro personas, todas con la misma melodía y sin instrumentos. ¿Qué textura tiene?",
         ["Todas las voces cantan la misma línea melódica y no hay acompañamiento.", "Como solo se oye una línea melódica, aunque la canten varias personas, es una textura de una sola línea."],
         "Una sola línea melódica"),
        ("Distinguir descripción e impresión", "Dos frases sobre una obra ficticia: «tiene un bombo en cada pulso» y «es muy emocionante». ¿Cuál es descripción con evidencia?",
         ["Se puede comprobar al escuchar si hay un bombo en cada pulso.", "«Es muy emocionante» depende de quien escucha y no se comprueba."],
         "«Tiene un bombo en cada pulso»"),
    ],
    mistakes=[("Escribir «suena antiguo» o «suena moderno» como único dato.", "Es una impresión que no indica qué rasgo se oye.", "Cita rasgos concretos, como el instrumento, el compás o la textura."),
              ("Creer que una obra reciente es más avanzada que una antigua.", "Se confunde época con calidad.", "Analiza qué hace cada obra con los elementos del lenguaje musical.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es el análisis estético de una obra?', 'Describir con evidencia cómo trabaja los elementos del lenguaje musical y qué efecto producen', 'Decir si la obra es bonita o fea según lo que siente cada persona al escucharla', 'Contar cuántas veces se ha tocado la obra y en cuántos lugares se ha presentado', 'El análisis estético se apoya en rasgos comprobables y en su efecto expresivo.'),
        ('abc', '{F} ¿Qué textura tiene la obra 1?', 'Una sola línea melódica, sin acompañamiento', 'Melodía con acompañamiento de teclado', 'Varias capas electrónicas', 'La ficha describe una voz sola, sin instrumentos.'),
        ('abc', '{F} ¿Qué obra tiene forma ABA?', 'La obra 2, «Minueto del jardín»', 'La obra 1, «Canto de trilla»', 'La obra 3, «Neón»', 'La ficha indica forma ABA solo para la obra 2.'),
        ('abc', '{F} ¿Qué rasgo del timbre tiene la obra 3?', 'Sonidos electrónicos de sintetizador y un bombo, sin voz', 'Una voz sola, sin instrumentos ni sonidos electrónicos de ningún tipo', 'Teclado y dos violines que tocan juntos una melodía con acompañamiento', 'La ficha describe sintetizador, bombo y ausencia de voz.'),
        ('=', '{F} La obra 3 tiene 32 compases de 4 pulsos. ¿Cuántos segundos dura a 120 pulsos por minuto?', '32*4*60//120', 'Se calculan los pulsos totales y se pasan a segundos con los pulsos por minuto.', ' s'),
        ('abc', '{F} ¿Cuántos pulsos tiene cada compás de la obra 2?', '3 pulsos', '4 pulsos', '2 pulsos', 'La ficha indica compás de 3 pulsos para la obra 2.'),
        ('=', '{F} La obra 2 tiene 3 secciones de 8 compases, cada compás de 3 pulsos, a 90 pulsos por minuto. ¿Cuántos segundos dura?', '3*8*3*60//90', 'Se multiplican secciones, compases y pulsos para obtener los pulsos totales y luego se pasan a segundos.', ' s'),
        ('abc', '{F} ¿Cuál de estas frases es una descripción con evidencia de la obra 1?', 'Repite la misma melodía en cuatro estrofas con distinta letra', 'Se siente triste y transmite una sensación de nostalgia por el campo', 'Es la obra más auténtica de todas las que se presentan en la ficha', 'Solo la primera se puede comprobar al escuchar la obra.'),
        ('{F} Escribe la textura de cada obra, en el orden 1, 2 y 3.', '1: una sola línea; 2: melodía con acompañamiento; 3: varias capas', 'La ficha describe una voz sola, una melodía con acompañamiento y capas que entran y salen.'),
        ('abc', '{F} Un estudiante dice: «la obra 3 es más moderna, por eso es mejor que la obra 1». ¿Qué falla?', 'Confunde época con calidad y no cita rasgos de ninguna de las obras', 'Nada, porque las obras modernas siempre son mejores', 'Que la obra 3 no tiene bombo', 'Un análisis compara rasgos; la época no mide la calidad.'),
        ('abc', '¿Por qué conviene describir antes de interpretar?', 'Porque la interpretación debe apoyarse en rasgos que otras personas puedan comprobar', 'Porque interpretar una obra está prohibido en un análisis estético de música', 'Porque describir es más corto y por eso siempre conviene dejarlo para el final', 'Una interpretación sin descripción previa queda sin evidencia.'),
        ('abc', '{F} ¿Qué procedimiento compositivo comparten las obras 1 y 3?', 'La repetición: la melodía de las estrofas y el motivo en bucle', 'El retrógrado de la melodía, porque en las estrofas se toca de atrás hacia adelante', 'El contraste total entre secciones, porque ambas obras cambian por completo', 'La obra 1 repite la melodía en las estrofas y la obra 3 repite el motivo en bucle.'),
        ('abc', '{F} ¿Qué afirmación contradice la ficha?', '«La obra 1 usa muchos instrumentos»', '«La obra 2 está en compás de 3 pulsos»', '«La obra 3 no tiene voz»', 'La ficha dice que la obra 1 es una voz sola, sin instrumentos.'),
    ],
    ctx=('abc', 'Debes analizar una obra que escuchas por primera vez. ¿Qué haces primero?', 'La escuchas varias veces y anotas rasgos que se puedan comprobar', 'Buscas una opinión famosa sobre la obra y la copias como si fuera tu análisis', 'Decides si te gusta y escribes solo eso, sin anotar ningún rasgo de la obra', 'El análisis parte de rasgos comprobables que se anotan al escuchar.'),
    sc=[
        ("En Composición musical: ¿qué es la textura?", "La manera en que se combinan las capas sonoras", "La textura describe cuántas líneas hay y cómo se relacionan."),
        ('abc', 'Una frase que se puede comprobar al escuchar es:', 'La obra tiene un bombo en cada pulso', 'La obra es preciosa', 'La obra es la mejor del mundo', 'Solo la primera describe un rasgo comprobable.'),
        ("¿Qué elementos del lenguaje musical se pueden describir en cualquier obra?", "Ritmo, melodía, armonía, timbre, textura, forma, dinámica y tempo", "Esos elementos están presentes en obras de cualquier época y procedencia."),
    ],
    op=("Con la {F}, elige una obra y escribe una ficha de descripción con cuatro rasgos comprobables (por ejemplo, textura, forma, timbre y tempo). Después escribe una impresión personal y márcala como tal.",
        "Obra 2: textura de melodía con acompañamiento; forma ABA; timbres de teclado y dos violines; 90 pulsos por minuto. Impresión personal (no es evidencia): me parece elegante.",
        ["cuatro rasgos comprobables de la ficha", "distingue evidencia de impresión", "usa los elementos del lenguaje musical"],
        ["hoja con la ficha de descripción y la impresión señalada"],
        ["usar solo adjetivos como «bonita»", "mezclar impresión con evidencia", "inventar rasgos que la ficha no dice"],
        "Pregunta: «¿cómo lo comprobaría alguien que escuche la obra?». Si no sabe, pídele que cambie el adjetivo por un rasgo."),
    reinforce="Escribe una descripción de cuatro rasgos de una canción que conozcas, sin usar adjetivos de gusto.",
    extend="Explica con un ejemplo inventado por qué dos obras de épocas distintas pueden compartir un mismo rasgo, como la repetición.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (cinco recursos de producción y sus posibilidades, de ejemplo). "
     "R1, voz sin amplificar: se oye bien a pocos metros y transmite el texto con claridad. "
     "R2, instrumentos acústicos (cuerdas, vientos y percusión): cada material da un timbre propio; su volumen depende de cómo se toca y de la sala. "
     "R3, amplificación eléctrica (micrófono y parlante): permite que sonidos suaves se oigan en espacios grandes. "
     "R4, grabación de sonido: guarda una interpretación para oírla muchas veces y en otros lugares. "
     "R5, síntesis electrónica y bucle: genera sonidos con circuitos o programas y repite trozos sin cansarse. "
     "Situaciones: S1, fiesta al aire libre de una comunidad pequeña, sin electricidad; S2, concierto para 800 personas en un gimnasio, con electricidad; S3, una obra que se oye en audífonos, en distintos lugares y momentos.")
build(
    O4, 2, F,
    use="Aprenderé a relacionar los instrumentos y recursos de producción de una obra con el sonido que logra, y a ver cómo cambian las posibilidades según la época y el lugar.",
    prior=["Reconozco voz, objetos sonoros, instrumentos y tecnologías.", "Sé describir timbre y textura.", "Sé que una obra se produce en un contexto."],
    explain=[
        "Los recursos de producción musical son los medios con que se hace sonar y se registra una obra. Han cambiado con el tiempo y varían según el lugar. La voz y los instrumentos acústicos se pueden usar en cualquier parte, sin electricidad. La amplificación eléctrica permite que un sonido suave llegue a un público grande. La grabación permite oír una interpretación muchas veces y en otros lugares. La síntesis electrónica genera sonidos nuevos y repite trozos con bucles.",
        "Antes de que existiera la grabación de sonido, la música se conservaba en la memoria, en la tradición oral y en la escritura. La grabación no creó la música, pero cambió cómo se guarda, se difunde y se escucha. Cada recurso ofrece posibilidades y límites: un instrumento acústico tiene un timbre propio y un volumen limitado; una pista electrónica puede repetirse sin cansancio, pero no cambia sola.",
        "Un recurso no determina por sí solo la calidad estética de una obra. Lo importante es cómo se usa para lograr un efecto expresivo. Por eso se analiza el recurso, el sonido que produce y el contexto: no se dice «la tecnología nueva es mejor». Las situaciones de este cuaderno son de ejemplo y no se hacen con equipos reales.",
    ],
    vocab=[("amplificación", "aumento eléctrico del volumen con micrófono y parlante"), ("grabación de sonido", "registro de una interpretación para oírla después"), ("síntesis electrónica", "generación de sonidos con circuitos o programas"),
           ("bucle", "trozo que se repite una y otra vez"), ("recurso de producción", "medio con que se hace sonar o se registra una obra"), ("posibilidad", "lo que un recurso permite hacer")],
    worked=[
        ("Relacionar recurso y posibilidad", "Una cantante ficticia debe cantar suave en un teatro grande y quiere que se la oiga hasta el final de la sala. ¿Qué recurso la ayuda?",
         ["La voz sin amplificar se oye bien a pocos metros, no en una sala grande.", "La amplificación eléctrica hace que sonidos suaves se oigan en espacios grandes."],
         "La amplificación eléctrica"),
        ("Calcular con una grabación", "Un registro de ejemplo guarda 6 interpretaciones de 5 minutos cada una. ¿Cuántos minutos de música contiene?",
         ["Se multiplican las interpretaciones por los minutos de cada una: 6 × 5.", "6 × 5 = 30 minutos."],
         "30 minutos"),
    ],
    mistakes=[("Decir que un recurso nuevo hace mejor a la obra.", "Se confunde tecnología con calidad.", "Analiza qué efecto logra el recurso en esa obra."),
              ("Creer que antes de la grabación no había música.", "Se olvida la tradición oral y la escritura.", "Recuerda que la grabación cambió cómo se guarda y se difunde la música.")],
    T=[
        ('abc', '{F} ¿Qué posibilidad principal ofrece la amplificación eléctrica?', 'Que sonidos suaves se oigan en espacios grandes', 'Que la música se pueda guardar para siempre', 'Que los instrumentos suenen sin tocarlos', 'La ficha describe la amplificación como el recurso que permite oír sonidos suaves en espacios grandes.'),
        ('abc', '{F} ¿Qué recurso permite oír una interpretación muchas veces y en otros lugares?', 'La grabación de sonido', 'La voz sin amplificar', 'Los instrumentos acústicos', 'La ficha dice que la grabación guarda una interpretación para volver a oírla.'),
        ('abc', '{F} ¿Qué posibilidad ofrece la voz sin amplificar?', 'Transmite el texto con claridad a pocos metros', 'Repite trozos sin cansarse, porque genera sonidos con circuitos o programas', 'Genera sonidos nuevos con circuitos, sin necesidad de una persona que cante', 'La ficha indica que la voz sola se oye bien a pocos metros.'),
        ('abc', '{F} ¿Qué recursos son los más adecuados para S1, la fiesta sin electricidad?', 'La voz sin amplificar y los instrumentos acústicos', 'La amplificación eléctrica y la síntesis', 'La grabación y los audífonos', 'En S1 no hay electricidad y los recursos acústicos funcionan sin ella.'),
        ('=', '{F} Un álbum grabado de ejemplo tiene 8 piezas de 4 minutos cada una. ¿Cuántos minutos de una hora quedan libres si se oye completo?', '60-8*4', 'Se multiplican las piezas por su duración y se resta del total de 60 minutos.', ' minutos'),
        ('abc', '{F} ¿De qué depende el timbre de los instrumentos acústicos según la ficha?', 'Del material con que está hecho cada instrumento', 'De la cantidad de personas del público', 'De que haya electricidad', 'La ficha dice que cada material da un timbre propio.'),
        ('abc', '{F} ¿Qué combinación de recursos es coherente para S2, el concierto para 800 personas en un gimnasio?', 'Voces e instrumentos con micrófono y parlante', 'Solo voces sin amplificar', 'Solo una grabación sin intérpretes', 'La amplificación permite que el sonido llegue a un público numeroso.'),
        ('abc', '{F} ¿Cuál de las situaciones se puede realizar sin electricidad?', 'S1, la fiesta al aire libre, con voz e instrumentos acústicos', 'S2, el concierto para 800 personas en el gimnasio, con micrófonos y parlantes', 'S3, la escucha de una obra en audífonos, en distintos lugares y momentos', 'S2 y S3 necesitan equipos eléctricos; S1 puede hacerse con recursos acústicos.'),
        ('abc', '{F} Un compositor quiere una base de capas exactas que se repitan durante 10 minutos sin variar. ¿Qué recurso le sirve?', 'La síntesis electrónica y el bucle', 'La voz sin amplificar', 'Los instrumentos acústicos tocados en vivo', 'El bucle repite el mismo trozo sin cansarse.'),
        ('abc', 'Una estudiante afirma que antes de la grabación no existía música. ¿Qué es más preciso?', 'Existía música que se conservaba por tradición oral y escritura, y la grabación permitió oír una misma interpretación muchas veces', 'Es correcto: sin grabación no existía música, porque nada podía conservarse', 'La música se conservaba solo por escrito, porque la tradición oral no podía guardarla', 'La grabación cambió cómo se guarda y se difunde la música, no su existencia.'),
        ('abc', 'Otro estudiante dice que una obra con sintetizador es mejor que una con instrumentos acústicos porque usa más tecnología. ¿Qué falla?', 'El recurso no determina la calidad estética; importa cómo se usa para lograr un efecto', 'Nada, porque la tecnología siempre mejora la calidad estética de cualquier obra', 'Que los sintetizadores no se pueden usar en obras que tengan valor estético', 'La calidad depende del uso expresivo del recurso, no de su novedad.'),
        ('abc', 'Dos grupos tocan las mismas notas: uno con guitarra acústica en una plaza y otro con sintetizador en un estudio. ¿Qué cambia por los recursos?', 'El timbre y las posibilidades de efectos y de volumen, aunque las notas pueden ser las mismas', 'Las notas, que deben ser distintas, porque cada recurso exige una melodía propia', 'La obra deja de ser la misma en cualquier caso, aunque se conserven las notas', 'Los recursos modifican el sonido y sus posibilidades; la melodía puede conservarse.'),
        ('abc', '{F} Un compositor quiere una obra íntima, para pocas personas muy cerca. ¿Qué recursos apoyan ese carácter?', 'Voz sin amplificar e instrumentos acústicos a poca distancia', 'Amplificación a todo volumen para que el sonido llegue a todas las personas', 'Un bucle repetido sin pausas, que mantenga el mismo sonido durante toda la obra', 'La cercanía se logra con sonido natural a poca distancia.'),
    ],
    ctx=('abc', 'El liceo graba una pieza de ensayo para que apoderados que no pudieron asistir la oigan. ¿Qué recurso hace posible esa difusión y qué debe cuidar el grupo?', 'La grabación de sonido, con permiso de todas las personas que participan', 'La amplificación eléctrica, sin pedir permiso a quienes participan de la grabación', 'El bucle, porque repite lo grabado y no necesita permiso de nadie', 'La grabación guarda la interpretación; las personas grabadas deben dar permiso.'),
    sc=[
        ("En Composición musical: ¿qué es una grabación de sonido?", "Un registro de una interpretación para oírla después", "La grabación guarda la interpretación para volver a oírla."),
        ('abc', 'Un trozo que se repite una y otra vez es un:', 'Bucle', 'Retorno', 'Acorde', 'El bucle repite un trozo sin variar.'),
        ("¿Determina un recurso nuevo la calidad estética de una obra?", "No; importa cómo se usa para lograr un efecto", "El valor estético está en el uso expresivo del recurso."),
    ],
    op=("Con la {F}, elige dos recursos y describe, para cada uno, una posibilidad y un límite. Luego di cuál elegirías para una obra íntima de cinco personas en una sala pequeña y por qué.",
        "R2, instrumentos acústicos: posibilidad, timbre propio de cada material; límite, su volumen depende de cómo se toca. R3, amplificación: posibilidad, sonidos suaves se oyen en espacios grandes; límite, necesita electricidad. Para cinco personas en una sala pequeña elijo R2, porque se oye bien sin amplificar y mantiene la cercanía.",
        ["describe dos recursos con posibilidad y límite", "elige un recurso para el caso", "justifica con una posibilidad del recurso"],
        ["hoja con la descripción y la decisión justificada"],
        ["decir «es mejor porque es nuevo»", "no mencionar límites", "no justificar la elección"],
        "Pregunta: «¿qué límite tiene el recurso que elegiste?». Si no lo ve, pídele que busque qué necesita para funcionar."),
    reinforce="Anota tres recursos de producción de una canción que escuches y una posibilidad que cada uno aporta.",
    extend="Explica con un ejemplo inventado cómo cambió la manera de compartir música entre dos épocas con recursos distintos.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (tres obras y sus contextos de ejemplo, inventados). "
     "Obra A, «Canto de faena»: música para acompañar un trabajo en grupo; seis voces en llamada y respuesta (tres llaman y tres responden); ritmo marcado; sin instrumentos; función: coordinar el esfuerzo del grupo. "
     "Obra B, «Marcha de plaza»: banda de vientos y tambores; 100 pulsos por minuto; pulso fuerte y regular; función: acompañar un desfile en el que cada pulso es un paso. "
     "Obra C, «Sala de espera»: pieza ambiental electrónica; 50 pulsos por minuto; sin ritmo marcado; sonidos largos y suaves; función: crear un ambiente calmo en un espacio cerrado.")
build(
    O4, 3, F,
    use="Aprenderé a relacionar los rasgos de una obra con su contexto y su función, formulando hipótesis prudentes que se apoyan en evidencia y en fuentes.",
    prior=["Sé describir rasgos con evidencia.", "Conozco recursos de producción.", "Sé que una impresión no es evidencia."],
    explain=[
        "El contexto de una obra es la situación de origen y de uso: el lugar, el grupo de personas, la época y la tecnología disponible. La función es para qué se usa la obra en una situación: bailar, trabajar en grupo, acompañar un desfile, crear un ambiente. Muchos rasgos musicales se relacionan con la función. Un ritmo marcado y regular ayuda a coordinar el esfuerzo o los pasos de un grupo; un tempo lento y sonidos largos y suaves favorecen la calma.",
        "Estas relaciones son hipótesis, no certezas. Se formulan con palabras prudentes como «probablemente» o «puede relacionarse con» y se apoyan en dos cosas: un rasgo de la obra y una fuente sobre su contexto, como un testimonio de la comunidad o un registro escrito. Un solo rasgo no basta para fechar una obra ni para decir de dónde viene. Dos obras con rasgos parecidos pueden tener funciones distintas.",
        "La función también puede cambiar cuando la obra cambia de contexto: una pieza hecha para la calma pierde su efecto en un patio de recreo. Para entender la función original de una obra de tradición oral, se consulta a la comunidad de origen o fuentes confiables. Este cuaderno no inventa ritos ni datos de pueblos originarios: eso lo entregan las personas que portan la tradición.",
    ],
    vocab=[("contexto", "situación de origen y uso de una obra: lugar, grupo, época y tecnología"), ("función", "para qué se usa una obra en una situación"), ("hipótesis", "explicación probable que necesita evidencia"),
           ("fuente", "persona o documento que informa sobre algo"), ("llamada y respuesta", "diálogo en que un grupo llama y otro responde"), ("ambiental", "música que crea un ambiente más que una melodía principal")],
    worked=[
        ("Formular una hipótesis", "Una pieza ficticia de baile tiene un pulso fuerte, tempo rápido y un patrón rítmico que se repite. ¿Qué hipótesis prudente puede plantearse sobre su función?",
         ["El pulso fuerte y el patrón repetido facilitan que el cuerpo siga el ritmo.", "Se plantea con prudencia: probablemente sirve para bailar, y se confirma con una fuente."],
         "Probablemente sirve para bailar, porque tiene un pulso fuerte y un patrón repetido"),
        ("Calcular pasos", "Un desfile ficticio marcha a 90 pulsos por minuto, un paso por pulso. ¿Cuántos pasos da en 2 minutos?",
         ["En un minuto hay 90 pasos.", "En 2 minutos hay 90 × 2 = 180 pasos."],
         "180 pasos"),
    ],
    mistakes=[("Afirmar con seguridad quién creó una obra solo por su estilo.", "Un rasgo aislado no basta para saber la autoría ni la época.", "Usa «probablemente» y busca una fuente."),
              ("Creer que una obra cumple la misma función en cualquier lugar.", "Se ignora que el contexto de uso cambia.", "Pregunta dónde y para qué se usa la obra en cada situación.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es el contexto de una obra?', 'La situación de origen y de uso: lugar, grupo, época y tecnología', 'La cantidad de notas que tiene la obra y el compás en que está escrita', 'El título de la obra y el nombre de quien la compuso, sin otros datos', 'El contexto describe dónde, por quién y en qué condiciones se creó y se usa la obra.'),
        ('abc', 'En Composición musical: ¿qué es la función de una obra?', 'Para qué se usa la obra en una situación', 'La nota más aguda de la melodía', 'El volumen al que se toca', 'La función explica la utilidad social o expresiva de la obra.'),
        ('abc', '{F} ¿Cuál es la función de la obra A?', 'Coordinar el esfuerzo de un grupo en un trabajo', 'Acompañar un desfile', 'Crear un ambiente calmo en un espacio cerrado', 'La ficha lo declara para la obra A.'),
        ('abc', '{F} ¿Qué rasgos de la obra A se relacionan con coordinar el esfuerzo?', 'El ritmo marcado y la llamada y respuesta entre las voces', 'La ausencia de ritmo marcado y de diálogo entre las voces', 'Los sonidos largos y suaves, que invitan a quedarse quieto', 'El ritmo marcado y el diálogo de voces ayudan a que el grupo se mueva junto.'),
        ('=', '{F} En la obra B cada pulso es un paso. ¿Cuántos pasos da un desfile en 30 segundos a 100 pulsos por minuto?', '100*30//60', 'Se calculan los pulsos por segundo y se multiplican por los segundos del desfile.', ' pasos'),
        ('abc', '{F} ¿Qué rasgos de la obra C se relacionan con la calma?', 'El tempo muy lento y los sonidos largos y suaves', 'El pulso fuerte y regular', 'La llamada y respuesta entre seis voces', 'Un tempo lento y sonidos largos y suaves favorecen la calma.'),
        ('abc', '{F} ¿Qué hipótesis está bien formulada para la obra B?', 'Probablemente su pulso fuerte y regular facilita que el grupo marche junto', 'Seguro que la compuso un ejército, porque es una marcha y todas las marchas son militares', 'Es la mejor obra de la ficha, por eso se la usa en los desfiles', 'Una hipótesis prudente relaciona un rasgo con la función y usa «probablemente».'),
        ('=', '{F} Se suman 4 personas al canto de la obra A, que ya tenía 6 voces; se reparten por igual entre quienes llaman y quienes responden. ¿Cuántas voces responden?', '(6+4)//2', 'Se calcula el total de voces y se divide por 2 entre los dos grupos.', ' voces'),
        ('{F} ¿Qué obra usarías para acompañar un desfile y por qué rasgo?', 'La obra B, por su pulso fuerte y regular', 'Un desfile necesita que cada persona dé un paso al pulso; la obra B tiene pulso fuerte y regular.'),
        ('abc', '{F} Un estudiante dice: «como la obra C es electrónica, es anterior a la obra A». ¿Qué falla?', 'Un rasgo aislado no basta para fechar una obra y la ficha no entrega épocas', 'Nada, porque lo electrónico es siempre más antiguo que lo cantado por varias voces', 'Que la obra C no es electrónica, porque la ficha describe un ambiente calmo', 'Para ordenar obras en el tiempo se necesitan fuentes, no un rasgo suelto.'),
        ('abc', '¿Por qué se usan palabras como «probablemente» al relacionar rasgos con contexto?', 'Porque la relación es una hipótesis que necesita fuentes para confirmarse', 'Porque no se sabe nada de la música y todo lo que se diga es una invención', 'Porque así el texto se alarga y parece más completo para quien lo evalúa', 'Las relaciones entre rasgos y contexto no son certezas.'),
        ('abc', '{F} La obra C se usa de pronto en un patio de recreo con estudiantes corriendo. ¿Qué ocurre con su función?', 'No cumple su función de crear calma, porque el contexto de uso cambió', 'Cumple igual su función, porque la función no depende del contexto', 'Pasa a ser una marcha', 'La función se relaciona con el contexto en que se usa.'),
        ('abc', '{F} Para comprobar la hipótesis sobre la función de la obra A, ¿qué fuente es más útil?', 'Un testimonio o registro escrito de la comunidad que la usa, que explique para qué se canta', 'La opinión de alguien que nunca ha oído la obra pero tiene muchos seguidores', 'Un cartel sin autor ni fecha que dice para qué sirve la obra', 'La fuente más confiable es la comunidad de origen o un registro suyo.'),
    ],
    ctx=('abc', 'Un museo ficticio presenta una obra de tradición oral en una sala silenciosa, sin contar nada de su origen. ¿Cómo se analiza su función original?', 'Consultando a la comunidad o a fuentes confiables, porque el museo es otro contexto de uso', 'Suponiendo que su función es la que tiene en el museo, donde hoy se la presenta', 'Decidiendo la función según lo que opine la primera persona que visita el museo', 'La función original se averigua con fuentes sobre el contexto de origen.'),
    sc=[
        ("En Composición musical: ¿qué es una hipótesis sobre una obra?", "Una explicación probable que necesita evidencia", "Una hipótesis se apoya en un rasgo y en una fuente, y se formula con prudencia."),
        ('abc', 'Para relacionar un rasgo con la función, conviene decir:', 'Probablemente este rasgo se relaciona con la función', 'Seguro que fue creada por un grupo famoso', 'Todo ritmo marcado sirve solo para marchar', 'La prudencia evita afirmar lo que no se puede comprobar.'),
        ("¿Qué puede cambiar la función de una obra?", "Que cambie el contexto en que se usa", "La misma obra puede cumplir funciones distintas en contextos distintos."),
    ],
    op=("Con la {F}, elige una obra y escribe una hipótesis prudente que relacione un rasgo con su función, qué fuente usarías para comprobarla y qué pasaría si la usaras en otro contexto.",
        "Obra C: probablemente su tempo muy lento y sus sonidos largos y suaves se relacionan con la calma. Fuente: un registro de la persona que la creó o de quienes la usan. En un patio de recreo no cumpliría esa función.",
        ["relaciona un rasgo con la función", "usa un lenguaje prudente", "propone una fuente", "considera otro contexto"],
        ["hoja con la hipótesis, la fuente y el cambio de contexto"],
        ["afirmar sin prudencia", "no proponer una fuente", "usar un rasgo que la ficha no dice"],
        "Pregunta: «¿cómo comprobarías tu hipótesis?». Si no tiene respuesta, pídele que nombre una fuente posible."),
    reinforce="Escribe una hipótesis prudente que relacione un rasgo de una música de baile que conozcas con su función.",
    extend="Explica con un ejemplo inventado cómo una misma obra puede tener una función distinta en dos situaciones.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (obra y dos análisis de ejemplo, inventados). Obra «Neón» (de ejemplo): pista electrónica de nuestro siglo; 120 pulsos por minuto; compás de 4 pulsos; 32 compases; bombo en cada pulso; "
     "un motivo de sintetizador de 2 compases repetido en bucle; entra una capa nueva cada 8 compases (en los compases 9, 17 y 25); sin voz. "
     "Análisis de Lía: «Describo: 120 pulsos por minuto, bombo en cada pulso y un motivo en bucle. "
     "Relaciono: el bucle y las capas son recursos de la producción electrónica y mantienen un pulso estable que sirve para bailar. "
     "Interpreto: la entrada gradual de capas crea expectativa y una sensación de crecimiento.» "
     "Análisis de Nico: «Neón es genial porque suena muy moderna y todos la conocen.»")
build(
    O4, 4, F,
    use="Aprenderé a escribir un análisis estético completo en tres pasos (describir, relacionar e interpretar) con evidencia de la obra, su contexto y sus recursos de producción.",
    prior=["Sé describir rasgos con evidencia.", "Sé relacionar rasgos con contexto y función.", "Conozco recursos de producción."],
    explain=[
        "Un análisis estético completo tiene tres pasos. Describir es anotar rasgos comprobables de la obra (tempo, compás, timbres, forma, textura, procedimientos). Relacionar es vincular esos rasgos con las técnicas, los recursos de producción y el contexto, por ejemplo con la función de la obra. Interpretar es proponer qué efecto expresivo produce la obra, apoyándose en los rasgos descritos.",
        "La interpretación es una lectura razonada de quien analiza: puede haber otras, pero cada una necesita evidencia. «La entrada gradual de capas crea expectativa» se apoya en el rasgo de que entra una capa cada 8 compases. Un juicio sin evidencia, como «es genial porque todos la conocen», no es un análisis: la fama no describe cómo trabaja la obra.",
        "Para comparar obras de épocas y procedencias distintas, se usan los mismos criterios: los elementos del lenguaje musical, los procedimientos, los recursos de producción y el contexto. Así la comparación no depende del gusto personal. Todo se puede hacer por escrito con una ficha de la obra, sin audio real.",
    ],
    vocab=[("describir", "anotar rasgos comprobables de la obra"), ("relacionar", "vincular los rasgos con técnicas, recursos y contexto"), ("interpretar", "proponer el efecto expresivo apoyándose en rasgos"),
           ("expectativa", "sensación de que algo va a ocurrir"), ("criterio", "aspecto común que se usa para comparar obras"), ("pulso estable", "pulso que se mantiene regular")],
    worked=[
        ("Clasificar una frase", "En un análisis ficticio aparece: «el piano toca acordes largos y suaves, lo que crea una sensación de quietud». ¿Qué pasos aparecen?",
         ["«El piano toca acordes largos y suaves» es una descripción comprobable.", "«Crea una sensación de quietud» es una interpretación apoyada en esa descripción."],
         "Describir e interpretar"),
        ("Contar entradas", "Una pista ficticia tiene 24 compases y una capa nueva entra cada 6 compases a partir del compás 7. ¿En qué compases entran las capas?",
         ["La primera entrada es el compás 7, y la siguiente 6 compases después.", "Las entradas son en los compases 7, 13 y 19."],
         "En los compases 7, 13 y 19"),
    ],
    mistakes=[("Escribir solo una interpretación sin describir.", "Queda sin evidencia y no se puede comprobar.", "Antes de interpretar, anota los rasgos en que te apoyas."),
              ("Usar la fama de la obra como argumento.", "La fama no describe rasgos de la obra.", "Cita rasgos y relaciónalos con el contexto.")],
    T=[
        ('abc', 'En Composición musical: ¿qué tres pasos tiene un análisis estético completo?', 'Describir, relacionar e interpretar', 'Escuchar, opinar y votar', 'Resumir, copiar y citar', 'Los tres pasos van de los rasgos comprobables al efecto expresivo.'),
        ('abc', '{F} La frase «el bucle y las capas son recursos de la producción electrónica y mantienen un pulso estable» corresponde al paso de:', 'Relacionar', 'Describir', 'Interpretar', 'Vincula rasgos con recursos de producción y función; eso es relacionar.'),
        ('abc', '{F} La frase «la entrada gradual de capas crea expectativa» corresponde al paso de:', 'Interpretar', 'Describir', 'Relacionar', 'Atribuye un efecto expresivo a un rasgo; eso es interpretar.'),
        ('=', '{F} ¿Cuántos segundos dura «Neón»? Tiene 32 compases de 4 pulsos a 120 pulsos por minuto.', '32*4*60//120', 'Se calculan los pulsos totales y se pasan a segundos con los pulsos por minuto.', ' s'),
        ('=', '{F} ¿Cuántas veces entra una capa nueva en los 32 compases, si entra una cada 8 compases y la primera no entra en el compás 1?', '32//8-1', 'Se cuentan los bloques de 8 compases y se descuenta el primero, que no tiene entrada.', ' veces'),
        ('abc', '{F} ¿Qué rasgo de la ficha sirve de evidencia para «mantiene un pulso estable»?', 'El bombo en cada pulso', 'La ausencia de voz', 'La fama de la obra', 'El bombo en cada pulso da un pulso regular que se puede comprobar.'),
        ('abc', '{F} ¿Qué falla en el análisis de Nico?', 'No describe rasgos ni relaciona con contexto, y su juicio se apoya en la fama', 'Que es demasiado largo para ser un análisis y por eso no se entiende', 'Que usa nombres de notas, que no sirven para describir una obra de música', 'Un análisis necesita rasgos y relaciones, no popularidad.'),
        ('abc', '{F} ¿Cuál es la mejor reescritura de «Neón es genial» como descripción con evidencia?', 'Neón tiene 120 pulsos por minuto, un bombo en cada pulso y un motivo de dos compases en bucle', 'Neón es la obra más famosa del siglo y por eso todo el mundo la baila', 'Neón me parece muy buena, y creo que a todas las personas les va a gustar', 'Solo la primera cita rasgos comprobables.'),
        ('=', '{F} Si la última capa entra en el compás 25 y la obra termina en el compás 32, ¿cuántos compases suenan con todas las capas presentes, contando el 25?', '32-25+1', 'Se restan los compases y se suma uno para incluir el compás de entrada.', ' compases'),
        ('abc', '{F} Lía dice que el bucle sirve para bailar. ¿Qué evidencia de la ficha la apoya mejor?', 'El pulso estable del bombo en cada pulso y la repetición del motivo', 'Que la obra no tiene voz y por eso no hay ninguna melodía que seguir', 'Que la obra tiene 32 compases, número que siempre se relaciona con bailar', 'Un pulso estable y repetido favorece seguir el ritmo con el cuerpo.'),
        ('abc', '¿Por qué «crea expectativa» es una interpretación y no una descripción?', 'Porque atribuye un efecto expresivo, que es una lectura de quien analiza apoyada en un rasgo', 'Porque se puede medir con un reloj y por eso siempre es objetiva', 'Porque se limita a contar los compases y los instrumentos, sin proponer ningún efecto', 'Una interpretación propone un efecto; una descripción anota un rasgo.'),
        ('abc', '{F} Otro estudiante interpreta que «Neón» transmite soledad solo porque no tiene voz. ¿Qué se puede decir?', 'Es discutible: la falta de voz es un rasgo, pero la interpretación necesita más evidencia y hay otras lecturas', 'Es la única interpretación posible, porque la falta de voz siempre transmite soledad', 'Es falsa, porque Neón no tiene voz y por tanto no puede transmitir nada', 'Una interpretación válida se apoya en varios rasgos; puede haber otras lecturas.'),
        ('abc', 'Quieres comparar «Neón» con una obra de tradición oral de ejemplo. ¿Qué criterios conviene usar?', 'Los mismos elementos del lenguaje musical, los recursos de producción y el contexto de cada obra', 'Cuál obra tiene más reproducciones en internet y cuántas personas la conocen', 'Cuál obra le gusta a más gente del curso, porque así se evita el gusto personal', 'Se comparan obras con criterios comunes, no con la popularidad.'),
    ],
    ctx=('abc', 'Debes escribir un análisis de una obra en tres párrafos. ¿Qué orden es el más lógico?', 'Primero describir los rasgos, luego relacionarlos con el contexto y por último interpretar el efecto', 'Primero dar una opinión y luego buscar rasgos que la apoyen, para que suene convincente', 'Primero contar cuántas personas la han oído y luego decir si es famosa', 'El orden va de lo comprobable a las relaciones y a la interpretación.'),
    sc=[
        ("En Composición musical: ¿qué es interpretar una obra en un análisis?", "Proponer su efecto expresivo apoyándose en rasgos", "La interpretación se apoya en la descripción."),
        ('abc', 'Una frase que vincula un rasgo con la función de la obra es de:', 'Relacionar', 'Describir', 'Aplaudir', 'Relacionar conecta rasgos con contexto, técnica o función.'),
        ("¿Por qué la fama no es un argumento de análisis?", "Porque no describe cómo trabaja la obra", "La fama no es un rasgo de la obra."),
    ],
    op=("Con la {F} escribe un análisis de «Neón» en tres frases, una para describir, una para relacionar y una para interpretar. Marca cada frase con su paso. No uses la frase de Lía ni la de Nico.",
        "Describo: la obra repite un motivo de dos compases y entra una capa cada 8 compases. Relaciono: la repetición permite mantener un ritmo estable y la entrada gradual de capas es posible gracias a la producción electrónica. Interpreto: el crecimiento por capas puede transmitir una sensación de avance.",
        ["una frase para cada paso", "cada frase se apoya en un rasgo de la ficha", "no copia frases de la ficha"],
        ["hoja con tres frases rotuladas"],
        ["mezclar pasos en una sola frase", "usar la fama como argumento", "inventar rasgos"],
        "Pregunta: «¿qué rasgo apoya tu interpretación?». Si no lo menciona, pídele que lo agregue a la frase."),
    reinforce="Elige una canción conocida y escribe una frase de descripción, una de relación y una de interpretación sobre ella.",
    extend="Explica con un ejemplo inventado cómo dos personas pueden interpretar de manera distinta la misma obra y ambas tener evidencia.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 5 (borrador y matriz de ejemplo, inventados). Borrador sobre la obra «Canto de trilla» (una voz sola; cuatro estrofas que repiten la misma melodía de cinco notas; tradición oral rural de ejemplo): "
     "(1) «La obra es una voz sola con cuatro estrofas que repiten la melodía.» (2) «Es la obra más bonita de todas.» "
     "(3) «Como es de tradición oral, seguro la compuso una sola persona hace mucho tiempo.» (4) «La repetición de la melodía probablemente facilita que un grupo la aprenda y la cante.» (5) «Fuente: lo escuché en clase.» "
     "Matriz comparativa de 2 obras por 5 elementos (ritmo, melodía, timbre, textura, forma) = 10 casillas. Obra 1 tiene completas 4 casillas (todas menos forma). Obra 2 tiene completas 3 casillas (ritmo, melodía y forma).")
build(
    O4, 5, F,
    use="Aprenderé a registrar un análisis estético, a revisar un borrador separando evidencia de opinión y a ajustar mi texto con fuentes y conclusiones prudentes.",
    prior=["Sé describir, relacionar e interpretar.", "Sé formular hipótesis prudentes.", "Sé citar una fuente."],
    explain=[
        "Registrar un análisis es dejarlo por escrito de modo que otra persona lo entienda y lo pueda comprobar. Una matriz comparativa es una tabla que compara obras con los mismos criterios, por ejemplo cinco elementos del lenguaje musical en cada obra. Las casillas vacías muestran qué falta describir. Cada dato debe volver a la obra o a una fuente: no se rellena con suposiciones.",
        "Para ajustar un borrador se revisan sus frases una a una. Una descripción con evidencia queda; una opinión sin evidencia se reemplaza por un rasgo y un efecto; una afirmación segura sin fuente se vuelve prudente («probablemente») o se respalda con una fuente; una fuente se anota con quién informó, qué título tiene y cuándo se consultó. «Lo escuché en clase» no basta como fuente.",
        "Después de ajustar se comprueba que el texto mejoró: cada afirmación tiene un rasgo comprobable o una fuente, la interpretación se apoya en lo descrito y la conclusión es prudente. Ajustar no es hacer un texto más largo, sino más claro y más fundado.",
    ],
    vocab=[("matriz comparativa", "tabla que compara obras con los mismos criterios"), ("borrador", "primera versión de un texto que se revisa"), ("fuente", "persona o documento que informa sobre algo"),
           ("prudente", "que no afirma más de lo que se puede comprobar"), ("casilla", "celda de una tabla"), ("ajustar", "cambiar un texto para mejorarlo con criterios")],
    worked=[
        ("Corregir una opinión", "En un borrador ficticio dice: «La obra es preciosa». Reescríbela como un rasgo con efecto.",
         ["Se reemplaza el adjetivo por rasgos de la obra, por ejemplo una voz sola y un tempo lento.", "Se agrega el efecto: da un aire tranquilo."],
         "«La voz sola y el tempo lento dan un aire tranquilo.»"),
        ("Contar casillas vacías", "Una matriz de ejemplo compara 3 obras en 4 elementos; hay 9 casillas completas. ¿Cuántas faltan?",
         ["La matriz tiene 3 × 4 = 12 casillas.", "Faltan 12 − 9 = 3 casillas."],
         "3 casillas"),
    ],
    mistakes=[("Rellenar casillas con datos que no se comprobaron.", "Se inventa para completar la tabla.", "Vuelve a la obra o a una fuente antes de escribir."),
              ("Anotar como fuente «lo escuché por ahí».", "Nadie puede comprobar de dónde viene el dato.", "Anota quién informó, el título y la fecha.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es una matriz comparativa?', 'Una tabla que compara obras con los mismos criterios', 'Una lista de las obras que más gustan a un grupo, ordenadas por preferencia', 'Un cuadro con nombres de intérpretes y fechas de sus presentaciones en vivo', 'La matriz compara obras con criterios comunes.'),
        ('abc', '¿Para qué se registran las fuentes de un análisis?', 'Para que otras personas puedan comprobar de dónde viene cada dato', 'Para que el análisis parezca más largo y así sea más difícil de revisar', 'Para evitar que alguien lo lea y descubra que faltan datos en el texto', 'Las fuentes permiten verificar los datos.'),
        ('abc', '{F} ¿Cuál frase del borrador es una descripción con evidencia?', 'La frase 1, porque indica una voz sola y la repetición de la melodía en cuatro estrofas', 'La frase 2, porque dice que la obra es bonita y se refiere a un efecto', 'La frase 3, porque afirma quién la compuso y cuándo, sin dudar de ello', 'La frase 1 se puede comprobar al escuchar la obra.'),
        ('abc', '{F} ¿Cuál frase es una opinión sin evidencia?', 'La frase 2, «es la obra más bonita de todas»', 'La frase 1, porque dice que la obra es una voz sola con cuatro estrofas', 'La frase 4, porque propone que la repetición probablemente ayuda a aprender', 'La frase 2 depende del gusto y no describe un rasgo.'),
        ('=', '{F} ¿Cuántas casillas de la matriz quedan vacías?', '2*5-(4+3)', 'Se calculan las casillas totales y se restan las completas de las dos obras.', ' casillas'),
        ('abc', '{F} La frase 4 vincula la repetición de la melodía con que un grupo la aprenda. ¿Qué paso del análisis es?', 'Relacionar, y está bien formulada con «probablemente»', 'Describir, porque cuenta las estrofas y dice cuántas veces se repite la melodía', 'Interpretar, porque da una opinión sobre lo bonita que es la melodía', 'La frase 4 relaciona un rasgo con una función de forma prudente.'),
        ('abc', '{F} ¿Cómo se reescribe con prudencia la frase 3?', 'Por ser de tradición oral, es probable que se transmitiera de persona en persona; falta una fuente sobre su autoría', 'Seguro la compuso una sola persona, porque toda obra tiene un único autor', 'No se sabe nada de la obra, así que se borra toda la frase del borrador', 'La prudencia indica lo probable y reconoce la falta de fuente.'),
        ('abc', '{F} ¿Cómo se corrige la frase 2 para que tenga evidencia?', 'Reemplazarla por «la melodía de cinco notas es fácil de recordar»', 'Agregar más adjetivos, como «preciosa» y «única», para dar fuerza a la opinión', 'Dejarla igual, porque cada persona tiene derecho a opinar lo que quiera', 'Cambia el adjetivo por un rasgo y un efecto comprobables.'),
        ('abc', '{F} ¿Cómo se completa la fuente de la frase 5, «lo escuché en clase»?', 'Anotando quién entregó la información, su título y la fecha en que se consultó', 'Anotando solo «internet», porque con eso cualquiera puede encontrar la fuente', 'Dejándola igual, porque la clase es una fuente suficiente para todo el análisis', 'Una fuente completa permite que otra persona la encuentre y la compruebe.'),
        ('abc', '¿Por qué conviene separar descripción e interpretación en el texto?', 'Porque así se ve qué es evidencia comprobable y qué es lectura de quien analiza', 'Porque la interpretación no necesita evidencia, mientras que la descripción sí la necesita', 'Porque describir es más corto y así el texto queda ordenado por el largo', 'Separarlas permite revisar cada parte con criterios distintos.'),
        ('abc', '{F} La casilla «forma» de la obra 1 está vacía. ¿Qué se hace antes de rellenarla?', 'Volver a la descripción de la obra y comprobar el rasgo, sin inventar', 'Copiar lo que dice la obra 2 en esa casilla, porque debe ser parecido', 'Escribir lo primero que se le ocurra, para que la tabla quede completa', 'Las casillas se completan con datos de la obra o de una fuente.'),
        ('abc', '{F} Un compañero dice que la frase 4 está mal porque nadie probó que la repetición ayude a aprender. ¿Qué respuesta es adecuada?', 'Es una hipótesis razonable; se puede reforzar con una fuente o dejarla formulada con prudencia', 'Tiene razón: hay que borrarla porque toda hipótesis es una afirmación errónea', 'No importa su comentario, porque nadie va a leer el borrador con atención', 'Una hipótesis prudente puede quedar si se declara como tal o se respalda con fuentes.'),
        ('abc', 'Después de ajustar el borrador, ¿cómo se sabe que mejoró?', 'Cada afirmación tiene un rasgo comprobable o una fuente y la conclusión es prudente', 'Tiene más adjetivos, que hacen que el juicio suene más convincente', 'Tiene más líneas, por lo que parece más completo que el borrador anterior', 'La mejora se mide con evidencia y prudencia, no con la extensión.'),
    ],
    ctx=('=', 'Tienes 45 minutos para entregar un análisis: 15 para escuchar y anotar, 20 para redactar y el resto para revisar. ¿Cuántos minutos te quedan para revisar?', '45-15-20', 'Se restan del total los minutos de escucha y de redacción.', ' minutos'),
    sc=[
        ("En Composición musical: ¿qué es un borrador?", "La primera versión de un texto, que se revisa y se ajusta", "El borrador se mejora con criterios antes de la versión final."),
        ('abc', 'Una fuente completa indica:', 'Quién informó, el título y la fecha de consulta', 'Solo el nombre de la página donde se encontró el dato, sin fecha ni autor', 'Solo «lo escuché por ahí», porque es suficiente para recordar de dónde vino', 'Una fuente completa se puede encontrar y comprobar.'),
        ("¿Con qué se rellena una casilla de la matriz?", "Con un dato comprobado en la obra o en una fuente", "Las casillas se completan con datos comprobables y no con suposiciones."),
    ],
    op=("Con la {F}, reescribe las frases 2, 3 y 5 del borrador para que cada una tenga evidencia o prudencia, y completa una casilla vacía de la matriz con un dato comprobable de «Canto de trilla».",
        "Frase 2: la melodía de cinco notas es fácil de recordar. Frase 3: por ser de tradición oral, es probable que se transmitiera de persona en persona; falta una fuente sobre su autoría. Frase 5: Fuente: ficha de la docente, 2.ª clase, con fecha. Casilla: forma de la obra 1 = cuatro estrofas que repiten la melodía.",
        ["tres frases reescritas", "una casilla vacía completada", "cada frase usa un rasgo o es prudente"],
        ["hoja con las frases corregidas y la casilla completada"],
        ["rellenar la casilla con un dato inventado", "dejar la fuente incompleta", "no hacer prudente la frase 3"],
        "Pregunta: «¿de dónde sale el dato de tu casilla?». Si no puede decirlo, pídele que vuelva a la ficha."),
    reinforce="Escribe tres frases sobre una canción tuya: una descripción, una opinión y una hipótesis prudente, y rotula cada una.",
    extend="Explica con un ejemplo inventado por qué una matriz comparativa ayuda a evitar que el gusto personal decida un análisis.",
)
