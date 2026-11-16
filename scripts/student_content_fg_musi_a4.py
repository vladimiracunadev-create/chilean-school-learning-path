"""Música 3.º y 4.º medio FG: OAC-04 (análisis de propósitos expresivos en obras musicales). Obras descritas de ejemplo, inventadas; sin audio real."""
from __future__ import annotations

from fg_musi_common import build

O4 = "FG-MUSI-3y4-OAC-04"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (obra de ejemplo «Marea», inventada). Una voz canta frases largas y suaves; una guitarra repite un patrón de cuatro notas; al fondo suena un teclado con sonido de cuerdas. "
     "El tempo es lento (60 pulsos por minuto). La forma es A-B-A: la parte A es tranquila, la B sube el volumen y agrega percusión, y la A final vuelve a la calma. "
     "Se oye una grabación limpia, sin ruidos, con la voz al centro.")
build(
    O4, 1, F,
    use="Aprenderé a escoger criterios estéticos para analizar una obra (lenguaje musical, aspectos técnicos y emociones, sensaciones e ideas) y a clasificar cada observación en el criterio que le corresponde.",
    prior=["Describo tempo, timbre, textura y forma.", "Separo rasgo audible, contexto y opinión.", "Sé que la emoción es una tendencia, no una regla."],
    explain=[
        "Analizar una obra musical es examinarla por partes para entender cómo funciona y qué busca expresar. Para eso se usan criterios estéticos, es decir, aspectos desde los cuales se observa y se valora una obra. Hay tres grupos útiles. El lenguaje musical: ritmo, melodía, armonía (los acordes que acompañan y su sucesión), timbre, textura y forma. Los aspectos técnicos: cómo se interpretó y cómo se grabó o produjo. Y lo que la obra genera: emociones, sensaciones e ideas.",
        "Una observación bien clasificada ayuda a ordenar el análisis. «El tempo es lento» pertenece al lenguaje musical; «la grabación es limpia, sin ruidos» a lo técnico; «da sensación de calma» a lo que genera. Distinguir estos grupos evita mezclar lo que se oye con lo que se siente. Las emociones se describen con prudencia, porque varían entre personas.",
        "El propósito expresivo es lo que la obra parece querer comunicar. Se infiere a partir de la evidencia, y se reconoce que puede haber más de una lectura razonable.",
    ],
    vocab=[("criterio estético", "aspecto desde el que se observa y valora una obra"), ("lenguaje musical", "ritmo, melodía, armonía, timbre, textura y forma"), ("armonía", "acordes que acompañan la melodía y su sucesión"), ("aspecto técnico", "lo que tiene que ver con la ejecución y la producción"), ("propósito expresivo", "lo que la obra parece querer comunicar"), ("forma A-B-A", "parte A, luego otra parte B y retorno a la A")],
    worked=[
        ("Clasificar observaciones", "De la obra «Marea» se anota: (1) «el tempo es lento», (2) «la voz está al centro y la grabación es limpia», (3) «transmite calma». Clasifica cada una.", ["El tempo es un elemento del lenguaje musical.", "La ubicación de la voz y la limpieza son aspectos de la grabación.", "La calma es una sensación que genera."], "1 lenguaje musical; 2 aspecto técnico; 3 lo que genera"),
        ("Reconocer la forma", "Una pieza de ejemplo tiene una parte tranquila, luego otra más fuerte y luego vuelve la tranquila. ¿Qué forma tiene?", ["Parte tranquila = A.", "Parte fuerte = B.", "Vuelve A: A-B-A."], "Forma A-B-A"),
    ],
    mistakes=[("Mezclar en una misma frase lo que se oye con lo que se siente.", "El oyente no puede separar la evidencia de la interpretación.", "Escribe primero el rasgo y luego «sugiere» o «puede transmitir»."),
              ("Decir que la grabación «es mala» sin indicar qué se nota.", "No hay un aspecto técnico comprobable.", "Describe: ruido de fondo, voz muy baja, volumen desparejo.")],
    T=[
        ('abc', '{F} ¿Qué parte de la forma es más fuerte y tiene percusión?', 'La parte B, que sube el volumen y agrega percusión', 'La parte A inicial, que es tranquila y suave', 'La parte A final, que vuelve a la calma', 'Solo la B sube el volumen y agrega percusión.'),
        ('abc', '{F} ¿A qué grupo de criterios pertenece «la grabación es limpia, sin ruidos»?', 'Aspectos técnicos, porque habla de la grabación', 'Lenguaje musical, porque habla de la pieza', 'Emociones e ideas, porque habla de una sensación', 'Habla de cómo se grabó o produjo la obra.'),
        ('abc', '{F} ¿Qué elemento del lenguaje musical describe «la guitarra repite un patrón de cuatro notas»?', 'Lenguaje musical: un patrón melódico que se repite', 'Aspectos técnicos de la grabación', 'Lo que la obra genera en quien escucha', 'Un patrón repetido es parte del lenguaje musical.'),
        ('abc', '¿Qué es el propósito expresivo de una obra?', 'Lo que la obra parece querer comunicar, según la evidencia', 'Los instrumentos que se usaron', 'El lugar donde se grabó', 'Se infiere a partir de la evidencia de la obra.'),
        ('abc', '{F} ¿Cuántas partes distintas (A y B) tiene la forma A-B-A?', '2', '3', '1', 'Aunque A aparece dos veces, solo hay dos partes diferentes: A y B.'),
        ('abc', '{F} ¿Cuántas secciones tiene la obra en total?', '3', '2', '4', 'A, B y A final son tres secciones.'),
        ('abc', 'Una estudiante escribe: «Es hermosa». ¿En qué grupo cae esa frase si no incluye un rasgo?', 'Opinión de gusto, que por sí sola no es un criterio de análisis', 'Lenguaje musical, porque habla de la obra', 'Aspecto técnico, porque habla de la ejecución', 'Sin rasgos comprobables, es una opinión.'),
        ('abc', '{F} ¿Qué frase sobre «Marea» es una sensación que genera, expresada con prudencia?', 'Puede transmitir calma, porque el efecto varía entre personas', 'Siempre produce tristeza en todas las personas', 'Tiene exactamente 60 pulsos por minuto', 'Usa «puede», lo que reconoce la variabilidad de las emociones.'),
        ('abc', '{F} El teclado con cuerdas al fondo aporta principalmente', 'timbre y una capa de textura de fondo', 'una mejor afinación de la voz', 'una grabación más ruidosa', 'Es un recurso de timbre y textura.'),
        ('abc', 'Dos estudiantes proponen propósitos distintos para una misma obra y ambos citan rasgos. ¿Qué se puede concluir?', 'Puede haber más de una lectura razonable', 'Uno de los dos necesariamente miente', 'No se puede analizar la obra', 'Si cada lectura se apoya en evidencia, ambas pueden ser válidas.'),
        ('abc', '{F} ¿Qué observación pertenece a lo técnico?', 'La voz está al centro de la mezcla', 'El tempo es lento', 'La parte B sube el volumen', 'La ubicación de la voz es parte de la producción.'),
        ('abc', 'Para analizar, ¿qué orden es más claro?', 'Observar rasgos, clasificarlos y recién entonces inferir el propósito', 'Decidir el propósito y buscar rasgos que lo confirmen', 'Escribir una opinión y no mirar los rasgos', 'El propósito se infiere de la evidencia observada.'),
        ('abc', '{F} Si la parte B durara el doble de compases que cada parte A y cada A tiene 8 compases, ¿cuántos compases tiene la obra?', '32', '24', '16', 'A: 8 + 8 y B: 16; en total 32.'),
    ],
    ctx=('abc', 'En una clase se escucha una obra de ejemplo y un estudiante escribe: «Me gusta porque suena lenta, tiene voz suave y emociona». ¿Cómo se ordena mejor su observación?', 'Lenguaje musical: lenta y voz suave; lo que genera: emociona', 'Aspecto técnico: me gusta; lenguaje musical: emociona', 'Todo es una opinión sin criterios', 'Lento y voz suave son rasgos musicales; emocionar es lo que la obra genera.'),
    sc=[
        ('En Música: ¿Qué es la armonía?', 'Los acordes que acompañan la melodía y su sucesión', 'La armonía forma parte del lenguaje musical de la obra.'),
        ('¿Cuántas secciones tiene una forma A-B-A?', '3', 'Se cuentan A, B y A final.'),
        ('abc', 'Un aspecto técnico es', 'la limpieza de la grabación o la ejecución', 'la emoción que siento', 'el título de la obra', 'Se refiere a la ejecución y la producción.'),
    ],
    op=("Con la {F} escribe una ficha de análisis con tres filas: una observación del lenguaje musical, una técnica y una de lo que genera. Cierra con una frase prudente sobre el propósito expresivo.",
        "Lenguaje musical: tempo lento de 60. Técnico: voz al centro y grabación limpia. Genera: puede transmitir calma. Propósito: parece buscar una atmósfera tranquila que se retoma al final.",
        ["tres criterios", "observaciones comprobables", "propósito con prudencia"], ["ficha de tres filas"], ["mezclar opinión y rasgo", "afirmar sin prudencia"],
        "Reconoce la ficha y pide cambiar cada opinión por un rasgo comprobable."),
    reinforce="Escucha una canción y completa tres filas: lenguaje musical, técnico y lo que genera.",
    extend="Compara dos canciones de estilos distintos con la misma ficha de tres criterios.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (obra de ejemplo «Alarma», inventada). Solo golpes de objetos metálicos sin filo, cortos y agudos; el pulso se acelera de 90 a 150 pulsos por minuto en 12 compases; el volumen crece de a poco (crescendo). "
     "Un efecto de eco repite cada golpe. Al final todo se corta de golpe, seguido de dos pulsos de silencio. No hay melodía cantada. Se grabó a volumen moderado.")
build(
    O4, 2, F,
    use="Aprenderé a explicar cómo los recursos de producción (voz, objetos, instrumentos y tecnologías como el eco) y los elementos del lenguaje musical sirven al propósito expresivo de una obra.",
    prior=["Clasifico observaciones por criterios.", "Conozco los recursos de producción.", "Sé qué es un crescendo y un silencio expresivo."],
    explain=[
        "Un recurso de producción no se analiza solo por lo que es, sino por lo que hace en la obra. Los golpes metálicos aportan un timbre brillante y cortante; el crescendo suma intensidad; el aumento del tempo transmite urgencia; el eco prolonga cada golpe y crea sensación de espacio; el silencio final puede dejar al oyente en suspenso. Cada decisión se relaciona con el propósito expresivo.",
        "Para analizar un recurso se pregunta tres cosas: qué es, qué efecto audible produce y para qué sirve en esta obra. Un mismo recurso puede cumplir propósitos distintos en obras diferentes: el eco puede dar amplitud en una pieza calmada o intensificar la tensión en una pieza inquieta. Por eso se analiza siempre en contexto.",
        "También se revisa si los recursos son coherentes entre sí. Si el propósito es inquietud, un timbre muy suave y un tempo lento irían en contra. Conviene citar el rasgo y el instante donde se oye.",
    ],
    vocab=[("recurso", "elemento de producción o de lenguaje musical que usa la obra"), ("urgencia", "sensación de que algo debe ocurrir pronto"), ("eco", "efecto que repite un sonido, cada vez más suave"), ("suspenso", "estado de espera ante algo que no se resuelve"), ("coherencia", "relación lógica entre las decisiones de una obra")],
    worked=[
        ("Explicar un recurso", "En «Alarma», los golpes de objetos metálicos son cortos y agudos. ¿Qué efecto tienen y para qué sirven?", ["Qué es: timbre metálico, corto y agudo.", "Efecto audible: un sonido cortante.", "Sirve para dar sensación de alerta."], "Aportan un timbre cortante que sugiere alerta"),
        ("Calcular el aumento de tempo", "En otra pieza de ejemplo el tempo pasa de 80 a 130 pulsos por minuto. ¿Cuánto aumentó?", ["Se resta el tempo inicial del final.", "130 − 80 = 50 pulsos por minuto."], "50 pulsos por minuto"),
    ],
    mistakes=[("Explicar un recurso solo con su nombre («usa eco»).", "No dice qué efecto produce ni para qué sirve.", "Agrega el efecto audible y el propósito en la obra."),
              ("Creer que un recurso significa siempre lo mismo.", "El sentido depende del contexto de cada obra.", "Analiza el recurso con los demás elementos de la pieza.")],
    T=[
        ('=', '{F} ¿Cuántos pulsos por minuto aumenta el tempo desde el inicio hasta el final?', '150-90', 'Se resta el tempo inicial del tempo final.', ' pulsos por minuto'),
        ('abc', '{F} ¿Qué recurso sugiere intensificación gradual?', 'El crescendo, que sube el volumen de a poco', 'El silencio final', 'La ausencia de melodía', 'Subir el volumen de a poco aumenta la intensidad.'),
        ('abc', '{F} ¿Qué efecto produce el eco sobre cada golpe?', 'Lo repite y lo prolonga, como una huella del sonido', 'Lo vuelve más lento y grave', 'Lo cambia por una voz', 'El eco repite el sonido y deja una huella.'),
        ('abc', '{F} El corte brusco seguido de dos pulsos de silencio puede producir', 'suspenso o sobresalto en quien escucha', 'una melodía alegre', 'un tempo más lento', 'Cortar y callar deja al oyente en espera.'),
        ('abc', '{F} ¿Por qué el aumento del tempo apoya el propósito de «alerta»?', 'Transmite urgencia, porque el pulso se acelera', 'Hace la pieza más afinada', 'Baja el volumen general', 'Un pulso que se acelera suele sugerir prisa.'),
        ('abc', 'Un estudiante escribe: «Usa eco». ¿Qué le falta a esta explicación?', 'El efecto audible y para qué sirve en la obra', 'El nombre del grupo que la hizo', 'Una opinión de gusto', 'Un recurso se explica por su efecto y su propósito.'),
        ('abc', '{F} Si se reemplazaran los golpes metálicos por una flauta suave, ¿qué sería probable?', 'Disminuiría la sensación de alerta', 'Aumentaría la urgencia', 'Nada cambiaría en el timbre', 'El timbre suave contradice el propósito de alerta.'),
        ('abc', '¿Por qué un mismo recurso puede significar cosas distintas en dos obras?', 'Porque su sentido depende del contexto de cada obra', 'Porque los recursos no tienen efectos', 'Porque cambian de nombre', 'Se analiza en conjunto con los demás elementos.'),
        ('abc', '{F} ¿Cuántos pulsos hay en los 12 compases si cada compás es de 4/4?', '48', '36', '24', '12 compases por 4 pulsos son 48 pulsos.'),
        ('abc', '{F} Una compañera dice que la obra es mala porque no tiene melodía cantada. ¿Qué responde un análisis con criterios?', 'Que la ausencia de melodía se relaciona con el propósito de alerta', 'Que toda música debe tener una melodía cantada', 'Que sin voz no se puede analizar', 'Falta de melodía no es un defecto en sí, depende del propósito.'),
        ('abc', 'Un propósito es «inquietud». ¿Qué conjunto de recursos es coherente?', 'Tempo que se acelera, timbre agudo y silencios sorpresivos', 'Tempo lento, timbre suave y notas largas', 'Volumen estable y melodía repetida sin cambios', 'Los otros conjuntos sugieren calma o monotonía.'),
        ('abc', '{F} Se grabó a volumen moderado. ¿Qué criterio estético sirve para comentarlo?', 'Los aspectos técnicos', 'La forma A-B-A', 'La melodía cantada', 'El volumen de grabación es un asunto técnico.'),
        ('abc', '¿Qué pregunta ayuda a analizar un recurso de una obra?', '¿Qué efecto audible produce y para qué sirve en esta obra?', '¿Qué recurso es más moderno?', '¿Qué recurso usa más gente?', 'Solo la primera explora el efecto y el propósito; la novedad o el uso de un recurso no explican qué hace en la obra.'),
    ],
    ctx=('abc', 'Un grupo quiere crear una pieza de «alerta» como «Alarma», pero usa tempo lento, flauta suave y volumen bajo. ¿Qué observación de análisis corresponde?', 'Los recursos son incoherentes con el propósito de alerta', 'Los recursos son perfectos para cualquier propósito', 'El tempo no influye en el propósito', 'Un tempo lento y un timbre suave no generan urgencia.'),
    sc=[
        ('¿Qué tres preguntas se hacen sobre un recurso?', 'Qué es, qué efecto produce y para qué sirve', 'Así se explica con evidencia y propósito.'),
        ('¿Cuántos pulsos hay en 10 compases de 4/4?', '40', 'Se multiplican 10 compases por 4 pulsos.'),
        ('abc', 'El eco', 'repite un sonido, cada vez más suave, y lo prolonga', 'acelera el tempo', 'cambia una voz por un instrumento', 'Es un efecto que prolonga el sonido.'),
    ],
    op=("Con la {F} escribe un análisis breve de tres recursos de «Alarma»: nombre del recurso, efecto audible y para qué sirve, y una frase final sobre si son coherentes con el propósito de alerta.",
        "Crescendo: sube el volumen de a poco y sugiere que algo se acerca. Eco: repite cada golpe y crea sensación de espacio. Silencio final: deja al oyente en suspenso. Son coherentes porque todos refuerzan la alerta.",
        ["tres recursos", "efecto y propósito", "juicio de coherencia"], ["análisis breve"], ["solo nombrar recursos", "no relacionar con el propósito"],
        "Reconoce el análisis y pide agregar el instante donde se oye cada recurso."),
    reinforce="Elige un recurso de tu canción favorita y explica qué es, qué efecto produce y para qué sirve.",
    extend="Propone cómo cambiaría el propósito de «Alarma» si el tempo bajara de 150 a 60 pulsos por minuto.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (obra de ejemplo «Amanecer en el patio», inventada). Una flauta toca una melodía que sube de a poco, en notas largas, sobre un fondo de cuerdas en acordes estables; el tempo es 72 pulsos por minuto; "
     "el volumen crece levemente. Al final una voz entona una frase corta y brillante. Texto de presentación escrito por el autor (ficticio): «Quise mostrar el comienzo tranquilo de un día».")
build(
    O4, 3, F,
    use="Aprenderé a enlazar evidencia, efecto y propósito en un análisis, y a distinguir el propósito del autor (lo que quiso comunicar) del efecto en cada oyente (lo que siente).",
    prior=["Clasifico observaciones por criterios.", "Explico un recurso por su efecto y su propósito.", "Sé que las emociones varían entre personas."],
    explain=[
        "Un análisis sólido sigue una cadena: evidencia, efecto y propósito. La evidencia es lo que se oye («la melodía sube de a poco en notas largas»). El efecto es lo que esa evidencia produce o sugiere («una sensación de avance tranquilo»). El propósito es lo que la obra parece querer comunicar («el comienzo de un día calmado»). Si falta un eslabón, el análisis queda débil: sin evidencia es una opinión, y sin propósito es solo una lista.",
        "Es importante distinguir el propósito del autor del efecto en el oyente. El propósito puede conocerse por lo que el autor dice o por lo que muestra la obra. El efecto, en cambio, depende de cada persona: una puede sentir calma y otra nostalgia. Ambos son válidos como lectura personal, pero solo el que se apoya en evidencia sirve para sostener un análisis.",
        "Cuando existe un texto del autor, se usa como una fuente más, no como la única verdad: se comprueba con la escucha si la obra realmente muestra lo que se afirma.",
    ],
    vocab=[("evidencia", "lo que se oye y se puede comprobar"), ("efecto", "lo que la evidencia produce o sugiere"), ("propósito del autor", "lo que quien creó la obra quiso comunicar"), ("lectura personal", "lo que siente o interpreta cada oyente"), ("acorde estable", "acorde que suena firme, sin tensión fuerte")],
    worked=[
        ("Armar la cadena", "En «Amanecer en el patio» la melodía sube de a poco en notas largas. Escribe evidencia, efecto y propósito.", ["Evidencia: melodía ascendente en notas largas.", "Efecto: sensación de avance tranquilo.", "Propósito: mostrar el comienzo de un día."], "Evidencia: melodía ascendente; efecto: avance tranquilo; propósito: comienzo de un día"),
        ("Separar autor y oyente", "Un estudiante siente nostalgia y el autor dice haber querido mostrar un comienzo tranquilo. ¿Se contradicen?", ["El autor habla de su propósito.", "El estudiante habla de su efecto personal.", "Pueden convivir."], "No: son cosas distintas"),
    ],
    mistakes=[("Escribir solo el propósito, sin evidencia («quiere mostrar calma»).", "No se puede comprobar ni discutir.", "Agrega qué se oye y qué efecto produce."),
              ("Aceptar el texto del autor sin comprobarlo con la escucha.", "Lo dicho puede no verse reflejado en la obra.", "Verifica con rasgos audibles que la obra lo muestra.")],
    T=[
        ('abc', '{F} ¿Cuál es una evidencia audible en la obra?', 'La melodía de la flauta sube de a poco en notas largas', 'Es la obra más tranquila que existe', 'Se nota que el autor estaba tranquilo', 'Solo el primero se comprueba escuchando.'),
        ('abc', '{F} ¿Qué efecto es coherente con acordes estables y notas largas?', 'Sensación de calma y de reposo', 'Sensación de peligro', 'Sensación de carrera', 'Acordes firmes y notas largas suelen sugerir quietud.'),
        ('abc', '{F} ¿Cuál es el propósito que declara el autor?', 'Mostrar el comienzo tranquilo de un día, según su texto', 'Mostrar una persecución', 'Presentar una fiesta ruidosa', 'Está en el texto de presentación de la ficha.'),
        ('abc', 'En una cadena de análisis, la evidencia es', 'lo que se oye y se puede comprobar al escuchar', 'lo que siente cada persona', 'lo que el autor desea', 'La evidencia es la base audible.'),
        ('abc', '{F} Una compañera siente nostalgia al escucharla. ¿Qué se puede decir?', 'Es una lectura personal que puede ser válida si se apoya en rasgos audibles', 'Está mal porque el autor habló de calma', 'No puede sentir algo distinto del autor', 'El efecto varía entre oyentes; la lectura personal puede ser válida.'),
        ('abc', '{F} ¿Qué evidencia de la ficha apoya la idea de «día que comienza»?', 'El volumen crece levemente y la melodía asciende', 'El tempo es exactamente 100', 'La voz entona una frase muy larga', 'Subir y crecer sugiere avance, como un amanecer.'),
        ('abc', 'Un análisis dice: «Es hermosa y triste». ¿Qué le falta?', 'Evidencia audible y efecto', 'Un título más largo', 'La fecha de su creación', 'Solo hay opiniones, sin rasgos ni cadena.'),
        ('abc', '{F} ¿Qué rasgo de la voz final puede reforzar el propósito de «comienzo»?', 'Una frase corta y brillante, que sugiere apertura', 'Un grito prolongado', 'Una frase lenta en tonos graves', 'Lo corto y brillante sugiere claridad y apertura.'),
        ('abc', 'Un autor dice que su obra muestra un «comienzo tranquilo», pero quien la analiza nota que el tempo aumenta mucho a mitad de pieza. ¿Qué debe hacer?', 'Comprobar si la obra realmente muestra calma y señalar la diferencia', 'Aceptar el texto sin escuchar', 'Descartar toda la obra', 'El texto del autor se contrasta con la escucha.'),
        ('=', '{F} A 72 pulsos por minuto, ¿cuántos pulsos suenan en 5 minutos?', '72*5', 'Se multiplican los pulsos por minuto por los minutos.', ' pulsos'),
        ('abc', 'Dos análisis de la flauta: (1) «Asciende en notas largas, lo que sugiere un avance tranquilo.» (2) «Se nota que el autor quería algo bonito.» ¿Cuál es más sólido?', 'El (1), porque enlaza evidencia y efecto', 'El (2), porque menciona al autor', 'Ambos, porque los dos opinan', 'El primero cita un rasgo y su efecto; el segundo supone intenciones.'),
        ('abc', '{F} ¿Qué es un acorde estable?', 'Uno que suena firme, sin tensión fuerte', 'Uno que cambia de volumen rápidamente', 'Uno que solo suena en voz', 'La estabilidad de los acordes sugiere reposo y firmeza.'),
        ('abc', 'Un autor explica su propósito y un oyente nota que la obra muestra otra cosa. ¿Cuál es la actitud más razonable?', 'Describir con evidencia lo que la obra muestra y compararlo con lo dicho', 'Ignorar al autor por completo', 'Aceptar cualquier cosa que diga el autor', 'El análisis considera las dos fuentes y las contrasta.'),
    ],
    ctx=('abc', 'En el curso discuten una obra de ejemplo. Una persona dice que transmite alegría; otra, que transmite inquietud. Ambas citan el tempo rápido y los acentos fuertes. ¿Qué conviene concluir?', 'Que hay dos lecturas posibles apoyadas en la misma evidencia', 'Que una de las dos no sabe de música', 'Que no se puede analizar la obra', 'Una misma evidencia puede sostener lecturas distintas, y eso se reconoce.'),
    sc=[
        ('¿Cuáles son los eslabones de la cadena de análisis?', 'Evidencia, efecto y propósito', 'Son tres pasos que se enlazan.'),
        ('¿Cuántos pulsos suenan en 3 minutos a 60 pulsos por minuto?', '180', 'Se multiplica 60 por 3 minutos.'),
        ('abc', 'El efecto en el oyente', 'varía entre personas, aunque oigan lo mismo', 'siempre coincide con la intención del autor', 'no existe en música', 'Cada oyente puede sentir algo distinto.'),
    ],
    op=("Con la {F} escribe una cadena de análisis con una evidencia distinta a las ya mencionadas (por ejemplo el crescendo o la frase final), su efecto y el propósito que apoya. Añade una frase sobre cómo comprobarías el texto del autor.",
        "Evidencia: la voz final entona una frase corta y brillante. Efecto: sensación de claridad. Propósito: comienzo luminoso del día. Comprobaría el texto escuchando si el resto de la obra se mantiene tranquilo.",
        ["evidencia", "efecto", "propósito"], ["cadena completa"], ["saltar la evidencia", "aceptar al autor sin comprobar"],
        "Reconoce la cadena y pide justificar el efecto con otro rasgo."),
    reinforce="Escoge una canción y escribe una cadena de evidencia, efecto y propósito.",
    extend="Escribe dos lecturas distintas de una misma evidencia y explica por qué ambas son posibles.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (dos obras de ejemplo, de estilos distintos, con un propósito parecido: calmar). Obra P: guitarra de nailon sola, tempo de 60 pulsos por minuto, frases repetidas con pequeñas variaciones, volumen suave, grabación con un poco de eco de sala. "
     "Obra Q: sintetizador con notas largas que se superponen, sin pulso marcado, sonido suave y espacioso, y un efecto de reverberación (efecto de sala grande) en toda la mezcla; dura el doble que P.")
build(
    O4, 4, F,
    use="Aprenderé a comparar dos obras de estilos distintos con un mismo propósito expresivo, mostrando qué recursos distintos pueden servir a un mismo fin y qué matices cambia cada uno.",
    prior=["Enlazo evidencia, efecto y propósito.", "Explico recursos por su efecto.", "Reconozco textura y timbre."],
    explain=[
        "Comparar dos obras permite ver que un mismo propósito puede lograrse con recursos muy distintos. Para comparar bien se eligen criterios comunes (por ejemplo timbre, pulso, textura, dinámica y espacio) y se describe cada obra con ellos. Luego se señalan semejanzas y diferencias, y se concluye qué matiz aporta cada una al propósito compartido.",
        "En la ficha, las dos obras buscan calmar. La obra P lo hace con una sola guitarra, un pulso claro y frases repetidas; la obra Q, con notas largas superpuestas, sin pulso marcado y mucha reverberación. P transmite una calma cercana y ordenada; Q, una calma amplia y flotante. Son matices, no una escala de mejor o peor: cada estilo usa sus recursos para su propósito.",
        "Evita comparar obras con una vara de otro estilo: juzgar a Q por no tener pulso marcado sería exigirle algo que su estilo no busca. Compara siempre según el propósito y los criterios acordados.",
    ],
    vocab=[("comparar", "señalar semejanzas y diferencias con criterios comunes"), ("matiz", "diferencia sutil en cómo se logra o se siente un propósito"), ("reverberación", "efecto que da la impresión de un espacio grande"), ("superponer", "hacer sonar capas que se traslapan"), ("criterio común", "aspecto que se usa para describir ambas obras")],
    worked=[
        ("Elegir criterios comunes", "Para comparar P y Q, ¿qué criterios sirven?", ["Deben poder describirse en ambas obras.", "Timbre, pulso, textura, dinámica y espacio aplican a las dos."], "Timbre, pulso, textura, dinámica y espacio"),
        ("Hallar una diferencia", "La obra P tiene pulso claro; la Q no. ¿Qué diferencia produce en la calma?", ["Un pulso claro da una calma cercana, ordenada.", "La ausencia de pulso da una calma flotante."], "P: calma ordenada y cercana; Q: calma flotante"),
    ],
    mistakes=[("Decir que una obra es mejor porque tiene más recursos.", "Más recursos no significa mejor logro del propósito.", "Valora cómo cada obra logra el propósito con lo que usa."),
              ("Criticar a Q por no tener pulso marcado.", "Juzga con un criterio ajeno al estilo y al propósito.", "Compara según el propósito compartido y los criterios comunes.")],
    T=[
        ('abc', '{F} ¿Qué propósito comparten las obras P y Q?', 'Calmar, según lo que declara la ficha para ambas obras', 'Alertar, porque ambas son suaves', 'Animar una fiesta, porque suenan juntas', 'La ficha lo declara como el propósito común.'),
        ('abc', '{F} ¿Qué diferencia de textura hay entre P y Q?', 'P es una guitarra sola y Q superpone notas largas', 'Ambas usan una sola capa de sonido', 'P superpone notas y Q usa una voz sola', 'La ficha describe a P con un instrumento y a Q con capas superpuestas.'),
        ('abc', '{F} ¿Qué obra tiene pulso marcado?', 'La obra P, con 60 pulsos por minuto y una guitarra sola', 'La obra Q, con notas largas', 'Las dos, porque ambas calman', 'Q no tiene pulso marcado, según la ficha.'),
        ('abc', '{F} Si P dura 3 minutos, ¿cuánto dura Q?', '6 minutos, porque Q dura el doble de los 3 minutos de P', '3 minutos, porque dura igual que P', '9 minutos, porque dura el triple', 'Q dura el doble que P.'),
        ('abc', '{F} ¿Qué recurso de Q crea sensación de espacio grande?', 'La reverberación en toda la mezcla', 'El pulso claro de 60', 'La guitarra de nailon', 'La reverberación imita una sala grande.'),
        ('abc', 'Un estudiante dice «Q es peor porque no tiene un ritmo claro». ¿Qué error comete?', 'Juzga con un criterio ajeno al estilo y al propósito', 'Confunde el tempo con la tonalidad', 'No sabe contar pulsos', 'Q busca otra calma, no un pulso claro.'),
        ('abc', '{F} ¿Qué matiz de calma transmite P?', 'Una calma cercana y ordenada, por su pulso claro', 'Una calma flotante y amplia', 'Una calma interrumpida', 'Pulso claro y una sola guitarra dan cercanía.'),
        ('abc', '¿Qué conviene hacer antes de comparar dos obras?', 'Elegir criterios comunes que se puedan describir en ambas', 'Elegir la que más gusta', 'Contar cuál tiene más instrumentos', 'Con criterios comunes se compara con justicia.'),
        ('abc', '{F} ¿Qué semejanza hay entre P y Q?', 'Ambas usan un volumen suave para calmar', 'Ambas tienen pulso marcado', 'Ambas usan guitarra', 'La ficha dice volumen suave en P y sonido suave en Q.'),
        ('=', '{F} P dura 4 minutos y se escucha 3 veces seguidas. ¿Cuántos minutos son?', '4*3', 'Se multiplican los minutos de una escucha por las veces.', ' minutos'),
        ('abc', 'Dos obras con recursos muy distintos pueden tener el mismo propósito. Esto muestra que', 'un propósito puede lograrse de varias maneras', 'una de las dos fracasa', 'el propósito no se puede analizar', 'Los recursos cambian pero el fin puede ser el mismo.'),
        ('abc', '{F} ¿Qué criterio común permite contrastar la sensación de movimiento en ambas?', 'El pulso, que está en P y no en Q', 'La reverberación', 'La duración de las obras', 'El pulso está presente en P y ausente en Q.'),
        ('abc', 'En una conclusión comparativa, ¿qué frase es mejor?', 'P y Q buscan calmar, pero P lo logra con un pulso claro y Q con capas flotantes', 'P es mejor porque se entiende más', 'Q es mejor porque dura más', 'La primera señala la semejanza y los matices según evidencia.'),
    ],
    ctx=('abc', 'Para una actividad de relajación en el colegio, un estudiante debe elegir entre P y Q. Dice que elegirá Q «porque dura más». ¿Qué argumento es más sólido?', 'Elegir según el matiz de calma que busca el grupo', 'Elegir la que dura más sin otro criterio', 'Elegir la que tenga más instrumentos', 'Se decide según el propósito, no por duración.'),
    sc=[
        ('¿Qué son los criterios comunes?', 'Aspectos que se describen en ambas obras', 'Permiten comparar las dos obras con justicia y claridad.'),
        ('Si Q dura el doble que una obra de 5 minutos, ¿cuántos minutos dura?', '10', 'El doble de 5 minutos es 10 minutos.'),
        ('abc', 'Un matiz es', 'una diferencia sutil en cómo se logra algo', 'una nota errónea que se corrige luego', 'un instrumento que se usa para variar', 'Dos obras con igual propósito pueden diferir en matices.'),
    ],
    op=("Con la {F} escribe una comparación breve de P y Q con tres criterios comunes (por ejemplo timbre, pulso y espacio): una semejanza, dos diferencias y una conclusión sobre el matiz de calma de cada una.",
        "Semejanza: ambas suenan suaves. Diferencias: P tiene un pulso claro y Q no; P es una guitarra sola y Q superpone sintetizadores con reverberación. Conclusión: P da calma cercana y Q, una calma flotante.",
        ["tres criterios comunes", "evidencia de la ficha", "conclusión sobre matices"], ["comparación breve"], ["comparar con criterios distintos", "decir cuál es mejor sin criterio"],
        "Reconoce la comparación y pide usar los mismos criterios en las dos obras."),
    reinforce="Compara dos canciones tuyas en volumen, pulso y timbre.",
    extend="Elige un propósito (alegría, tensión, nostalgia) y describe dos formas de lograrlo con recursos distintos.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 5 (borrador de análisis de ejemplo sobre la obra «Marea» de la clase 1). Borrador: «Marea es una canción lenta. Me gustó mucho. La voz es suave. Creo que quiere ser tranquila.» "
     "Datos de la obra: 60 pulsos por minuto; forma A-B-A; la parte B sube el volumen y agrega percusión; la A final vuelve a la calma; voz suave y cuerdas de fondo. "
     "Estructura que se pide para un párrafo: afirmación sobre el propósito, dos evidencias con su efecto, una frase sobre aspectos técnicos y una sobre el contraste entre las partes.")
build(
    O4, 5, F,
    use="Aprenderé a registrar y ajustar un análisis escrito: ordenar el párrafo, usar conceptos disciplinarios y reemplazar opiniones sueltas por evidencia, efecto y propósito.",
    prior=["Enlazo evidencia, efecto y propósito.", "Comparo obras con criterios comunes.", "Uso vocabulario de lenguaje musical."],
    explain=[
        "Un análisis escrito se registra en un párrafo ordenado. Una estructura útil es: primero una afirmación sobre el propósito expresivo; luego dos evidencias, cada una con su efecto; después una observación técnica (ejecución o producción); y por último un comentario sobre el contraste o la forma. Se usan conceptos del lenguaje musical como tempo, timbre, textura, dinámica, forma y armonía, y no frases vagas como «suena bonito».",
        "Revisar y ajustar el borrador significa preguntar por cada frase: ¿qué se oye?, ¿qué efecto produce?, ¿qué propósito apoya? Las frases de gusto personal pueden quedar, pero rotuladas como opinión y sin sostener el análisis. También se verifica que cada dato sea correcto: el tempo, el número de partes y los recursos que se mencionan.",
        "Un buen análisis reconoce sus límites: puede haber otras lecturas y la descripción escrita de la obra puede no mostrar todos los detalles. Dilo con prudencia.",
    ],
    vocab=[("párrafo de análisis", "texto breve que ordena propósito, evidencias, efectos y observaciones técnicas"), ("concepto disciplinario", "término propio de la música, como tempo, timbre o forma"), ("opinión rotulada", "frase de gusto personal que se marca como tal"), ("contraste", "diferencia marcada entre dos partes"), ("revisión", "relectura para corregir y mejorar un texto")],
    worked=[
        ("Reemplazar una frase vaga", "Mejora la frase «La voz es suave» usando evidencia y efecto, con los datos de «Marea».", ["Evidencia: la voz canta suave sobre cuerdas de fondo.", "Efecto: sensación de cercanía y calma."], "La voz canta suave sobre cuerdas de fondo, lo que transmite cercanía y calma"),
        ("Corregir un dato", "Un borrador dice que Marea tiene 4 partes. ¿Cuántas secciones tiene realmente?", ["Forma A-B-A: A, B y A final.", "Son 3 secciones y 2 partes distintas."], "3 secciones (2 partes distintas)"),
    ],
    mistakes=[("Dejar el borrador con frases como «me gustó mucho» como base del análisis.", "El gusto no demuestra ni explica nada.", "Rotúlalo como opinión y suma evidencia."),
              ("Usar términos sin entender su significado.", "Un término mal usado confunde y resta credibilidad.", "Comprueba la definición antes de usarlo.")],
    T=[
        ('abc', '{F} ¿Qué frase del borrador es una opinión de gusto?', 'Me gustó mucho, que expresa preferencia personal', 'La voz es suave, que describe un rasgo', 'Es una canción lenta, que describe un rasgo', 'Es la única que expresa preferencia personal.'),
        ('abc', '{F} ¿Qué mejora convierte «Es una canción lenta» en un dato comprobable?', 'Es lenta, a 60 pulsos por minuto, un dato que se puede comprobar', 'Es lentísima y muy aburrida', 'Es lenta porque eso gusta más', 'Un dato numérico se puede comprobar.'),
        ('abc', '{F} ¿Cuál es el primer elemento del párrafo pedido?', 'Una afirmación sobre el propósito expresivo', 'Una opinión personal', 'Una lista de instrumentos', 'La estructura abre con el propósito.'),
        ('abc', '{F} ¿Qué evidencia de la parte B apoya el comentario sobre el contraste?', 'Sube el volumen y agrega percusión', 'Hay una voz suave', 'La obra dura 60 pulsos por minuto', 'La parte B contrasta con la calma de la A.'),
        ('abc', '{F} ¿Qué afirmación sobre propósito es la más prudente?', 'Parece buscar una atmósfera tranquila, con un contraste central', 'Siempre busca provocar tristeza en toda persona', 'Quiere que el público baile', 'La prudencia reconoce que es una inferencia basada en evidencia.'),
        ('abc', '{F} ¿Cuál es una observación técnica para el párrafo?', 'La voz se escucha clara y suave sobre las cuerdas', 'La obra es hermosa y emocionante', 'El autor es famoso y respetado', 'Habla de cómo se oye la mezcla.'),
        ('abc', '{F} Al revisar, un estudiante detecta que escribió «3 partes distintas». ¿Qué debe corregir?', 'Son 2 partes distintas (A y B) en 3 secciones', 'Son 4 partes distintas', 'Son 1 parte', 'La forma A-B-A repite la A.'),
        ('abc', 'Una estudiante usa «armonía» para referirse al volumen. ¿Qué debe hacer?', 'Corregir el término: armonía se refiere a los acordes', 'Mantenerlo porque suena técnico', 'Quitar todos los términos técnicos', 'Los conceptos deben usarse con su significado.'),
        ('abc', '{F} Se piden dos evidencias con su efecto. ¿Qué par cumple mejor?', 'Voz suave: cercanía; parte B con percusión: contraste', 'Voz suave: gusta; percusión: se escucha', 'Tempo: es lento; forma: tiene partes', 'Cada evidencia va acompañada de un efecto.'),
        ('=', '{F} A 60 pulsos por minuto, ¿cuántos pulsos suenan en 4 minutos?', '60*4', 'Se multiplican los pulsos por minuto por los minutos.', ' pulsos'),
        ('abc', 'Para ajustar un borrador, la pregunta clave por cada frase es', '¿qué se oye, qué efecto produce y qué propósito apoya?', '¿Cuántas palabras tiene?', '¿Le gusta a mis amistades?', 'Esa pregunta convierte frases sueltas en análisis.'),
        ('abc', '{F} ¿Qué frase reconoce un límite del análisis?', 'Con solo la descripción escrita no se puede juzgar la grabación real', 'No hay otras lecturas posibles porque el análisis es único', 'La obra no tiene límites porque su análisis es completo', 'Reconoce lo que la evidencia no permite afirmar.'),
        ('abc', '{F} ¿Qué orden del párrafo es el pedido?', 'Propósito, dos evidencias con efecto, observación técnica y contraste', 'Contraste, opinión personal y título', 'Dos opiniones y una conclusión', 'Es la estructura indicada en la ficha.'),
    ],
    ctx=('abc', 'Un estudiante escribe: «Marea tiene 5 partes y se nota que es genial». ¿Cuál es el mejor ajuste?', 'Corregir a 3 secciones (A, B y A) y reemplazar «genial» por evidencia y efecto', 'Mantener el texto porque suena entusiasta', 'Quitar todo dato del análisis', 'Hay un dato incorrecto y una opinión sin respaldo.'),
    sc=[
        ('¿Qué lleva un párrafo de análisis?', 'Propósito, evidencias con efecto y observación técnica', 'Es la estructura que ordena el texto.'),
        ('¿Cuántos pulsos suenan en 2 minutos a 60 pulsos por minuto?', '120', 'Se multiplican 60 por 2 minutos.'),
        ('abc', 'Una opinión personal en un análisis debe', 'rotularse como tal y no sostener el análisis', 'ocupar la mayor parte del texto del análisis', 'ocultarse para que nadie la vea en el texto', 'El análisis se apoya en evidencia.'),
    ],
    op=("Con la {F} reescribe el borrador en un párrafo de 5 oraciones que siga la estructura pedida, usando al menos tres conceptos de la disciplina y corrigiendo cualquier dato.",
        "Marea parece buscar una atmósfera tranquila. La voz canta suave sobre cuerdas de fondo, lo que transmite cercanía. El tempo lento de 60 pulsos por minuto refuerza la calma. Técnicamente la mezcla deja la voz al centro. La parte B contrasta con la A porque sube el volumen y agrega percusión, y la A final recupera la calma.",
        ["estructura completa", "tres conceptos", "datos correctos"], ["párrafo de 5 oraciones"], ["datos incorrectos", "opinión como base"],
        "Reconoce el párrafo y pide revisar que cada dato coincida con la ficha."),
    reinforce="Subraya en un texto tuyo las frases de gusto y reemplázalas por evidencia.",
    extend="Intercambia tu párrafo con una compañera y propón un ajuste que mejore la evidencia.",
)
