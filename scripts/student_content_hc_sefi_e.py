"""Seminario de filosofía (electivo HC, 3.º y 4.º medio): OAC-05 (formular una tesis filosófica sobre un problema relevante para su contexto, a partir de una investigación sobre diversas perspectivas filosóficas, clases 1 a 4). Fuentes, autores y casos ficticios o «de ejemplo»."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada situación, ficha de lectura y fuente está escrita en el enunciado. "
             "Los autores, los lugares y los textos son ficticios o «de ejemplo»: sirven para practicar la investigación filosófica y no son citas de ninguna obra real. "
             "La investigación con obras filosóficas reales queda para tu docente y la biblioteca del liceo. Las perspectivas se presentan con sus razones y sin tomar partido: tu tesis será tuya, con razones y con objeciones consideradas. "
             "Si un tema te incomoda, puedes elegir otro caso ficticio y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O5 = "FI-SEFI-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (situaciones ficticias). Situación 1: el liceo «Puerto Sur» (no existe) recorta los recreos para ganar horas de clase. "
     "Situación 2: una joven ficticia siente culpa cada vez que descansa, porque piensa que el tiempo debe usarse en algo útil. "
     "Situación 3: un barrio ficticio debate si convertir un sitio vacío en una cancha o en un estacionamiento. "
     "Preguntas candidatas: P1: «¿Cuántos minutos duran los recreos de Puerto Sur?» P2: «¿Es justo recortar los recreos?» P3: «¿Tiene valor el tiempo que no se usa para algo útil?» P4: «¿Qué es el tiempo?»")
build(
    O5, 1, F,
    use="Aprenderé a elegir un problema relevante para mi contexto y a convertirlo en una pregunta de investigación filosófica bien delimitada.",
    prior=["Sé formular un problema filosófico.", "Sé reconstruir argumentos.", "Sé dialogar con razones sobre una pregunta."],
    explain=[
        "Formular una tesis filosófica comienza por elegir un problema relevante para tu contexto: algo que aparezca en tu vida, tu liceo o tu entorno y que tenga raíces filosóficas. No basta un tema. Un tema es un asunto general («el tiempo libre»). Un problema es una tensión de ideas dentro del tema. Una pregunta de investigación es una pregunta concreta, abierta y delimitada, que se puede investigar leyendo perspectivas filosóficas y argumentando.",
        "Una buena pregunta de investigación cumple cinco condiciones. Es relevante: importa en tu contexto. Es abierta: admite varias respuestas razonadas, y no se responde con un dato. Es delimitada: su alcance no es tan amplio que no se pueda tratar ni tan estrecho que no tenga discusión. Tiene conceptos que se pueden definir. Y es investigable: hay perspectivas filosóficas que ofrecen razones para responderla.",
        "En la ficha, P1 es una pregunta de dato. P2 es relevante y abierta, pero está atada a una sola decisión de un liceo y no llega al concepto de fondo (el valor del tiempo). P4 es tan amplia que cualquier respuesta quedaría incompleta. P3 conecta las tres situaciones y trabaja conceptos como valor y utilidad, y permite buscar perspectivas distintas.",
    ],
    vocab=[("tema", "asunto general sobre el cual se podría investigar"), ("problema", "tensión de ideas dentro de un tema"), ("pregunta de investigación", "pregunta concreta, abierta y delimitada que se puede investigar con perspectivas filosóficas"), ("delimitar", "acotar el alcance de una pregunta para poder tratarla"), ("relevante para el contexto", "que importa en la vida o el entorno de quien investiga"), ("investigable", "que existen perspectivas y razones con las que se puede trabajar")],
    worked=[
        ("Clasificar una pregunta", "¿Por qué P1 de la ficha no sirve como pregunta de investigación filosófica?",
         ["Pregunto si se responde con un dato: bastaría mirar el horario del liceo.", "No exige evaluar razones ni definir conceptos."],
         "Porque es una pregunta de dato, no abierta ni filosófica"),
        ("Elegir la mejor", "¿Por qué P3 es mejor que P4 como pregunta de investigación?",
         ["P4 es tan amplia que ninguna respuesta la agotaría.", "P3 está acotada al valor del tiempo no útil, conecta las situaciones y se puede trabajar con perspectivas filosóficas."],
         "Porque está delimitada, es relevante y es investigable"),
    ],
    mistakes=[("Elegir un tema («el tiempo libre») sin convertirlo en una pregunta.", "Un tema no tiene una tensión concreta que investigar.", "Pregúntate qué tensión de ideas hay en el tema y formúlala como una pregunta."),
              ("Elegir una pregunta tan amplia que ninguna respuesta bastaría.", "Sin delimitar, no se puede argumentar con profundidad.", "Acota el alcance con un concepto y un contexto concretos.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es un problema, a diferencia de un tema?", "Una tensión de ideas dentro de un tema", "Un asunto general", "Una respuesta definitiva", "El tema es el asunto; el problema es la tensión dentro de él."),
        ("abc", "¿Qué significa que una pregunta de investigación esté delimitada?", "Que su alcance no es ni demasiado amplio ni demasiado estrecho", "Que tiene una sola respuesta", "Que se responde con un dato", "Delimitar es acotar el alcance para poder tratarla."),
        ("abc", "{F} Una compañera propone investigar «¿Cuántos estudiantes de Puerto Sur prefieren recreos más largos?». ¿Qué tipo de pregunta es?", "De dato: se responde con una encuesta", "Filosófica, porque trata de preferencias", "Demasiado amplia", "Se contesta contando respuestas y no discutiendo conceptos."),
        ("abc", "{F} ¿Cuál es una forma de delimitar P4, «¿Qué es el tiempo?»?", "Preguntar por un aspecto concreto, como el valor del tiempo que no se usa para algo útil", "Agregar otra pregunta igual de amplia, como «¿qué es el espacio?»", "Preguntar cuántas horas tiene un día", "Delimitar es acotar el alcance con un concepto y un contexto concretos."),
        ("abc", "{F} ¿Qué condición cumple P3 que P1 no cumple?", "Es abierta y trabaja conceptos como valor y utilidad", "Menciona un número", "Habla de un liceo", "Esa es la diferencia con una pregunta de dato."),
        ("ab", "{F} ¿Con qué situación se relaciona más directamente P3: «¿tiene valor el tiempo que no se usa para algo útil?»?", "Con la de la joven que siente culpa al descansar", "Con la del sitio vacío del barrio", "Ella piensa que el tiempo debe usarse en algo útil, que es justo lo que P3 pregunta."),
        ("abc", "{F} Un estudiante dice: «P2 es igual de buena que P3, porque también es abierta». ¿Qué se puede responder?", "Es abierta y relevante, pero está atada a una decisión y P3 llega al concepto de fondo y conecta las tres situaciones", "Que P2 es una pregunta de dato", "Que P2 no trata de un liceo", "P2 sirve de punto de partida, pero P3 profundiza en un concepto filosófico y abarca más situaciones."),
        ("abc", "{F} Si se quisiera una pregunta sobre la Situación 3, ¿cuál sería mejor?", "¿Debe un sitio vacío del barrio destinarse a lo más útil o a lo que más reúne a las personas?", "¿Cuántos metros mide el sitio?", "¿Qué es una cancha?", "Es abierta, delimitada y trabaja conceptos."),
        ("abc", "Un estudiante propone investigar «la felicidad». ¿Qué mejora conviene?", "Acotar con un concepto y un contexto, como «¿es la felicidad lo que da sentido a una vida escolar?»", "Dejarlo igual, porque es un tema excelente", "Preguntar cuántas personas son felices", "Un tema general necesita convertirse en una pregunta acotada."),
        ("abc", "¿Qué significa que una pregunta sea relevante para tu contexto?", "Que importa en tu vida, liceo o entorno", "Que la hizo una persona famosa", "Que tiene muchas palabras", "La relevancia conecta la investigación con quien la hace."),
        ("abc", "¿Qué significa que una pregunta sea investigable?", "Que existen perspectivas filosóficas con razones para trabajarla", "Que se responde con una encuesta", "Que nadie la ha pensado", "Necesita perspectivas con las que se pueda dialogar."),
        ("abc", "{F} Si un grupo investigara «¿Tiene valor el tiempo que no se usa para algo útil?» y concluyera «el tiempo no existe», ¿qué falla?", "Cambia de problema: responde otra pregunta y no la planteada", "Responde bien", "Demuestra con un dato", "Una respuesta debe ser sobre la pregunta formulada."),
        ("abc", "¿Qué conviene hacer antes de elegir una pregunta de investigación?", "Comprobar que sea relevante, abierta, delimitada, con conceptos e investigable", "Elegir la más corta", "Elegir la más difícil", "Son las cinco condiciones de la explicación."),
    ],
    ctx=("abc", "Una estudiante ficticia quiere investigar «las redes sociales». ¿Cuál de estas es una pregunta de investigación filosófica mejor delimitada?", "¿Es más auténtica la amistad que se mantiene en línea que la que se mantiene en persona?", "¿Qué son las redes sociales?", "¿Cuántas personas usan una red?", "La primera acota el tema con un concepto (autenticidad) y se puede trabajar con perspectivas."),
    sc=[
        ("En Seminario de filosofía: ¿qué es una pregunta de investigación?", "Una pregunta concreta, abierta y delimitada que se puede trabajar con perspectivas filosóficas", "Va más allá del tema general."),
        ("¿Cuáles son las cinco condiciones de una buena pregunta?", "Relevante, abierta, delimitada, con conceptos e investigable", "Son las cinco condiciones de la explicación."),
        ("¿Por qué «la felicidad» sola no basta como pregunta?", "Porque es un tema general y no una pregunta delimitada", "Hay que convertirlo en una pregunta con concepto y contexto."),
    ],
    op=("Elige una situación ficticia para investigar. Situación 1: un colegio ficticio pone cámaras en los patios para mejorar la convivencia. Situación 2: una comunidad ficticia decide que cada vecino debe aportar horas de trabajo comunitario. Situación 3: un grupo de estudiantes ficticio decide no usar apodos en el curso. "
        "Escribe: el tema, el problema (la tensión), dos preguntas candidatas con un defecto cada una, y una pregunta de investigación final que cumpla las cinco condiciones.",
        "Situación 1. Tema: convivencia y vigilancia. Problema: la seguridad frente a la privacidad. Candidatas: «¿Cuántas cámaras hay?» (de dato) y «¿Qué es la privacidad?» (muy amplia). Final: ¿Es justo renunciar a parte de la privacidad en el patio para mejorar la convivencia?",
        ["distingue tema y problema", "descarta dos preguntas con defectos señalados", "formula una pregunta que cumple las cinco condiciones", "ancla la pregunta en un contexto"],
        ["tema, problema, dos candidatas descartadas y una pregunta final"],
        ["elegir una pregunta de dato", "elegir una pregunta demasiado amplia", "no explicar el defecto de las descartadas"],
        "Pregunta: «¿tu pregunta se podría responder con un dato o con una definición del diccionario?». Si sí, pídele que agregue un concepto en tensión."),
    reinforce="Elige un tema de tu entorno y escribe tres preguntas sobre él: una de dato, una demasiado amplia y una bien delimitada.",
    extend="Escribe cinco preguntas de investigación posibles sobre el uso del tiempo en el liceo y ordénalas de la más a la menos delimitada, explicando tu criterio.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (fuentes de ejemplo para investigar «¿tiene valor el tiempo que no se usa para algo útil?»). "
     "Fuente A: ensayo filosófico ficticio que argumenta con razones si el descanso tiene valor. "
     "Fuente B: titular de una noticia ficticia: «Jóvenes duermen una hora más los fines de semana». "
     "Fuente C: anuncio ficticio de una aplicación: «Aprovecha cada minuto con nuestra agenda inteligente». "
     "Fuente D: capítulo de un libro filosófico ficticio sobre el sentido del juego y del ocio.")
build(
    O5, 2, F,
    use="Aprenderé a definir los conceptos de mi pregunta y a planificar una investigación: qué perspectivas buscar y con qué criterios elegir fuentes.",
    prior=["Sé formular una pregunta de investigación.", "Sé definir conceptos con rasgos y casos.", "Sé reconstruir una perspectiva."],
    explain=[
        "Antes de investigar, se definen los conceptos clave de la pregunta. En «¿tiene valor el tiempo que no se usa para algo útil?», los conceptos son valor, utilidad, descanso y ocio. Una distinción importante es entre valor instrumental y valor intrínseco. Algo tiene valor instrumental si vale por lo que permite lograr, como estudiar para aprobar. Algo tiene valor intrínseco si vale por sí mismo, como disfrutar una conversación. Definir estos términos orienta toda la investigación.",
        "Luego se planifica qué perspectivas buscar. Conviene encontrar al menos tres perspectivas filosóficas distintas sobre el problema, de modo que se vean razones diferentes. Para elegir fuentes se usan criterios: que sean pertinentes (tratan el problema), que argumenten con razones identificables, que sean de perspectivas distintas y que su procedencia sea clara. Un titular o un anuncio pueden aportar un fenómeno que investigar, pero no son por sí solos una perspectiva filosófica.",
        "Cada fuente se lee con las mismas preguntas: qué problema aborda, qué tesis sostiene, qué razones ofrece, qué entiende por los conceptos clave y en qué contexto surgió. Con las mismas preguntas para todas, se pueden comparar. Anota también lo que no entendiste y lo que le cuestionarías.",
    ],
    vocab=[("valor instrumental", "valor de algo por lo que permite lograr"), ("valor intrínseco", "valor de algo por sí mismo"), ("pertinente", "que trata de verdad el problema investigado"), ("plan de investigación", "lista de conceptos, perspectivas y criterios que guía la búsqueda"), ("ficha de lectura", "registro ordenado de lo que dice y argumenta una fuente")],
    worked=[
        ("Valor instrumental o intrínseco", "Escuchar música porque te gusta, ¿tiene valor intrínseco o instrumental?",
         ["Pregunto si vale por sí mismo o por lo que permite lograr.", "Si se escucha por gusto, vale por sí mismo."],
         "Valor intrínseco, si se escucha solo por el gusto de hacerlo"),
        ("Elegir fuentes", "De la ficha, ¿qué fuentes servirían como perspectivas filosóficas?",
         ["Busco fuentes que argumenten con razones sobre el problema.", "A y D lo hacen; B y C muestran un fenómeno, no argumentan."],
         "Las fuentes A y D"),
    ],
    mistakes=[("Usar una noticia o un anuncio como si fuera una perspectiva filosófica.", "No ofrecen argumentos sobre el problema, solo muestran un fenómeno.", "Úsalos como ejemplo del fenómeno y busca fuentes que argumenten."),
              ("Leer cada fuente con preguntas distintas.", "Después no se pueden comparar.", "Aplica a todas las mismas preguntas: problema, tesis, razones, conceptos y contexto.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es el valor intrínseco?", "El valor de algo por sí mismo", "El valor de algo por lo que permite lograr", "El precio de algo", "Lo contrario es el valor instrumental, que depende de lo que se logra."),
        ("abc", "¿Qué es el valor instrumental?", "El valor de algo por lo que permite lograr", "El valor de algo por sí mismo", "El valor que da una autoridad", "Se vale por su utilidad para otro fin."),
        ("abc", "Estudiar solo para aprobar una prueba, ¿qué valor tiene?", "Instrumental, porque se estudia por lo que permite lograr", "Intrínseco, porque estudiar es siempre bueno", "Ninguno", "El estudio aparece como medio para aprobar."),
        ("abc", "Jugar con amigos porque disfrutas el juego, ¿qué valor tiene?", "Intrínseco, porque se valora por sí mismo", "Instrumental, porque sirve para ganar", "Ninguno, porque no es útil", "Vale por el disfrute que da."),
        ("abc", "{F} ¿Qué conceptos clave tiene la pregunta de la ficha?", "Valor, utilidad, descanso y ocio", "Trabajo, esfuerzo y salario", "Tiempo, reloj y calendario", "Son los conceptos centrales de la pregunta."),
        ("ab", "{F} ¿Cuáles fuentes son perspectivas filosóficas pertinentes?", "A y D, porque argumentan con razones sobre el problema", "B y C, porque son más actuales", "B es solo un titular y C es un anuncio; no argumentan sobre el problema."),
        ("abc", "{F} ¿Qué aporta la Fuente B a la investigación?", "Un fenómeno que se puede investigar, no una perspectiva filosófica", "Una tesis filosófica completa", "Una definición de ocio", "Muestra que hay un hecho social sobre el descanso."),
        ("abc", "{F} ¿Qué aporta la Fuente C a la investigación?", "Un ejemplo de cómo se presenta socialmente la utilidad del tiempo", "Una respuesta a la pregunta", "Una prueba de que el descanso no vale", "Sirve para ilustrar el fenómeno que se investiga."),
        ("abc", "Un estudiante dice: «Con una sola fuente basta». ¿Qué conviene responder?", "Conviene buscar al menos tres perspectivas distintas para ver razones diferentes", "Tiene razón: una fuente es suficiente", "Mejor usar cien fuentes iguales", "La investigación necesita perspectivas diversas para contrastar razones."),
        ("abc", "¿Por qué se aplican las mismas preguntas a todas las fuentes?", "Para poder compararlas", "Para que todas digan lo mismo", "Para acortar la lectura", "Solo se pueden comparar fuentes leídas con los mismos criterios."),
        ("abc", "¿Cuál de estas es una pregunta de ficha de lectura?", "¿Qué entiende esta fuente por «ocio»?", "¿Cuántas páginas tiene el libro?", "¿Quién es más famoso?", "Pregunta por un concepto clave de la investigación."),
        ("abc", "{F} Una compañera propone usar la Fuente D porque es larga. ¿Cuál es un criterio mejor?", "Que trate el problema y argumente con razones identificables", "Que tenga muchas páginas", "Que esté en un libro grueso", "El criterio es pertinencia y razones, no extensión."),
        ("abc", "{F} Si la Fuente A y la D coincidieran en todo, ¿qué convendría hacer?", "Buscar una perspectiva distinta para contrastar razones", "Dejar de investigar", "Elegir la más larga", "El plan de investigación pide perspectivas diversas."),
    ],
    ctx=("abc", "Un grupo ficticio investiga «¿es justo que se premie solo el rendimiento?». Tienen un ensayo filosófico ficticio con argumentos, un afiche de un concurso y un informe estadístico de notas. ¿Cuál es el mejor uso del afiche?", "Ejemplificar el fenómeno de premiar el rendimiento, no como perspectiva filosófica", "Como la tesis del trabajo", "Descartarlo y no mirarlo", "Aporta un ejemplo del fenómeno, pero no argumenta sobre el problema."),
    sc=[
        ("En Seminario de filosofía: ¿qué es una ficha de lectura?", "Un registro ordenado de lo que dice y argumenta una fuente", "Permite comparar fuentes con las mismas preguntas."),
        ("¿Qué diferencia hay entre valor instrumental e intrínseco?", "El primero vale por lo que permite lograr y el segundo por sí mismo", "Son dos maneras distintas de valorar algo."),
        ("¿Qué criterios sirven para elegir fuentes?", "Pertinencia, razones identificables, perspectivas distintas y procedencia clara", "Son los cuatro criterios de la explicación."),
    ],
    op=("Elige la pregunta de investigación de tu preferencia entre: «¿es justo que se premie solo el rendimiento?», «¿es mejor un vínculo que dura o uno que se renueva?» o «¿se puede ser libre dentro de una regla?». "
        "Escribe un plan: los dos o tres conceptos clave con su definición provisoria, el tipo de perspectivas que buscarías (al menos tres), los criterios para elegir fuentes y tres preguntas de ficha de lectura.",
        "Pregunta: ¿es justo que se premie solo el rendimiento? Conceptos: mérito (lo que se obtiene por esfuerzo y logro), justicia (dar a cada uno lo que corresponde) y rendimiento. Perspectivas: una que defienda el mérito, una que defienda la necesidad y otra que defienda la igualdad de oportunidades. Criterios: pertinencia, razones, variedad y procedencia. Preguntas: ¿qué tesis sostiene?, ¿qué entiende por mérito?, ¿en qué contexto escribe?",
        ["define al menos dos conceptos con claridad", "propone al menos tres perspectivas distintas", "usa criterios claros para elegir fuentes", "escribe tres preguntas útiles de ficha"],
        ["plan con conceptos, perspectivas, criterios y preguntas de ficha"],
        ["elegir perspectivas que son la misma", "usar fuentes sin argumentos", "definir con sinónimos"],
        "Pregunta: «¿tus tres perspectivas darían razones diferentes?». Si no, pídele que cambie una."),
    reinforce="Para tres cosas que haces cada semana, anota si tienen valor instrumental, intrínseco o ambos, con una razón.",
    extend="Escribe una ficha de lectura vacía con seis preguntas útiles para cualquier fuente filosófica.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (textos de ejemplo; autores ficticios). Problema: ¿tiene valor el tiempo que no se usa para algo útil? "
     "Perspectiva P1 (Julián Roca): «El tiempo es un recurso limitado, y quien lo gasta sin provecho pierde oportunidades. Solo lo que sirve para lograr algo da valor al tiempo.» "
     "Perspectiva P2 (Elvira Soto): «Hay actividades que valen por sí mismas: conversar, jugar, mirar el cielo. Si todo el tiempo se midiera por su utilidad, la vida perdería lo que la hace valiosa.» "
     "Perspectiva P3 (Nazaret Gil): «El descanso no es útil por sí mismo, pero sin él no podríamos cumplir nuestras metas. Por eso conviene reconocerle un valor, aunque sea de apoyo.»")
build(
    O5, 3, F,
    use="Aprenderé a reconstruir varias perspectivas con una misma ficha, compararlas y detectar dónde coinciden, dónde discrepan y qué falta responder.",
    prior=["Sé hacer un plan de investigación.", "Sé distinguir valor instrumental e intrínseco.", "Sé reconstruir tesis, razón y supuesto."],
    explain=[
        "Con las perspectivas elegidas, se hace una ficha de lectura de cada una con las mismas preguntas: tesis, razón principal, qué entiende por los conceptos clave, supuesto y posible objeción. Luego se organiza una matriz comparativa: una tabla con las perspectivas en las columnas y las preguntas en las filas. La matriz permite ver coincidencias y discrepancias de un vistazo.",
        "En la ficha, P1 sostiene que solo lo útil da valor al tiempo (valor instrumental). P2 sostiene que hay actividades con valor intrínseco, y que medirlo todo por utilidad empobrece la vida. P3 sostiene una posición intermedia: el descanso tiene un valor de apoyo, porque permite cumplir metas, aunque no sea útil por sí mismo. Las tres coinciden en que el tiempo tiene valor; discrepan en de dónde viene ese valor.",
        "Una buena comparación no se limita a repetir cada texto. Señala el punto exacto de desacuerdo (si todo valor es instrumental), qué supuesto lo explica y qué pregunta queda abierta. No hay que decidir todavía cuál es correcta: primero se comprende cada una con caridad.",
    ],
    vocab=[("matriz comparativa", "tabla que organiza perspectivas y preguntas para ver coincidencias y discrepancias"), ("coincidencia", "punto en que dos perspectivas concuerdan"), ("discrepancia", "punto en que dos perspectivas se oponen"), ("posición intermedia", "perspectiva que combina rasgos de otras dos"), ("pregunta abierta", "aspecto que las perspectivas no resuelven")],
    worked=[
        ("Completar una fila de la matriz", "En la ficha, ¿qué entiende cada perspectiva por «valor» del tiempo?",
         ["P1: valor es utilidad para lograr algo.", "P2: valor también puede estar en actividades por sí mismas; P3: valor de apoyo para cumplir metas."],
         "P1: instrumental. P2: intrínseco. P3: instrumental de apoyo, reconociendo el descanso"),
        ("Hallar el punto de desacuerdo", "¿En qué punto exacto discrepan P1 y P2?",
         ["Ambas aceptan que el tiempo tiene valor.", "P1 dice que todo valor viene de la utilidad; P2 dice que hay actividades con valor por sí mismas."],
         "En si todo valor del tiempo es instrumental o puede ser intrínseco"),
    ],
    mistakes=[("Resumir cada perspectiva por separado y no compararlas.", "Sin comparación no se ve el punto de desacuerdo.", "Usa una matriz y escribe coincidencias y discrepancias."),
              ("Declarar una perspectiva falsa antes de reconstruirla con caridad.", "Se critica una caricatura.", "Reconstruye su versión más fuerte antes de objetar.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es una matriz comparativa?", "Una tabla que organiza perspectivas y preguntas para comparar", "Una lista de autores", "Un resumen de una línea", "Muestra coincidencias y discrepancias a la vista."),
        ("abc", "{F} ¿Cuál es la tesis de P1?", "Solo lo que sirve para lograr algo da valor al tiempo", "Hay actividades que valen por sí mismas", "El descanso es un valor de apoyo", "Es la conclusión de su texto."),
        ("abc", "{F} ¿Cuál es la razón principal de P2 para criticar el criterio de utilidad?", "Si todo se midiera por su utilidad, la vida perdería lo que la hace valiosa", "Que el tiempo es limitado", "Que el descanso es útil", "Es el argumento que da en su texto."),
        ("abc", "{F} ¿Qué tipo de valor le reconoce P3 al descanso?", "Un valor de apoyo para cumplir metas", "Un valor intrínseco absoluto", "Ningún valor", "Reconoce valor, aunque no sea útil por sí mismo."),
        ("abc", "{F} ¿En qué coinciden las tres perspectivas?", "En que el tiempo tiene valor", "En que todo valor es intrínseco", "En que el descanso es inútil", "Las tres aceptan que el tiempo vale, aunque discrepen en por qué."),
        ("ab", "{F} ¿Qué supuesto se aprecia en P1?", "Que el valor del tiempo se mide por lo que se logra con él", "Que jugar es lo más valioso", "El texto afirma que solo lo útil da valor, así que supone que valor y utilidad coinciden."),
        ("abc", "{F} ¿Qué perspectiva está más cerca de P1 en su idea de valor?", "P3, porque reconoce valor al descanso por su apoyo a las metas", "P2, porque rechaza medir todo por utilidad", "Ninguna de las dos", "P3 también justifica el descanso por lo que permite lograr."),
        ("abc", "{F} P3 es una posición intermedia. ¿Qué toma de P1 y qué de P2?", "De P1, que el valor viene de lo que permite lograr; de P2, que el descanso merece reconocimiento aunque no sea útil por sí mismo", "De P1, que todo es juego; de P2, que el descanso no vale", "De P1 y de P2, que el tiempo no tiene valor", "Combina el criterio de utilidad con el reconocimiento del descanso."),
        ("abc", "{F} Un estudiante resume: «Para P2, la utilidad no importa nunca». ¿Qué falla?", "Es una caricatura: P2 dice que no todo valor viene de la utilidad", "Es una paráfrasis fiel", "Es una objeción válida", "P2 no niega la utilidad; critica medir todo por ella."),
        ("abc", "{F} ¿Cuál es una pregunta abierta que queda tras comparar las tres perspectivas?", "¿Puede una actividad tener valor por sí misma y también ser útil?", "¿Cuántas horas tiene un día?", "¿Quién escribió P1?", "Plantea un aspecto que ninguna de las tres resuelve del todo."),
        ("abc", "¿Qué se debe hacer antes de decidir qué perspectiva es correcta?", "Comprender cada una con caridad", "Elegir la que más gusta", "Elegir la más corta", "Primero se comprende bien, luego se evalúa."),
        ("abc", "{F} Si una nueva perspectiva P4 dijera «el valor del tiempo es lo que cada persona le da», ¿qué habría que hacer?", "Reconstruirla con las mismas preguntas y sumarla a la matriz", "Descartarla porque no es útil", "Copiar solo su título", "Toda perspectiva se lee con las mismas preguntas."),
        ("abc", "¿Por qué una buena comparación no repite cada texto?", "Porque debe señalar el punto exacto de desacuerdo y el supuesto que lo explica", "Porque los textos no importan", "Porque las perspectivas son iguales", "La comparación explica por qué difieren, no solo qué dicen."),
    ],
    ctx=("abc", "Un grupo ficticio compara tres perspectivas sobre el esfuerzo. P1: «El esfuerzo vale porque lleva a logros.» P2: «El esfuerzo vale cuando uno disfruta el proceso.» P3: «El esfuerzo vale si no daña la salud.» ¿En qué se diferencian P1 y P2?", "En la fuente de valor: los logros frente al disfrute del proceso", "En que una habla de esfuerzo y la otra no", "En que P2 niega que el esfuerzo exista", "Cada una ubica el valor en algo distinto."),
    sc=[
        ("En Seminario de filosofía: ¿qué es una discrepancia entre perspectivas?", "Un punto en que dos perspectivas se oponen", "Se encuentra en lo que cada una sostiene sobre el concepto clave."),
        ("¿Qué preguntas lleva cada ficha de lectura?", "Tesis, razón principal, concepto clave, supuesto y posible objeción", "Son las preguntas de la explicación."),
        ("¿Por qué conviene comprender con caridad antes de evaluar?", "Para criticar lo que realmente dice y no una caricatura", "Así la evaluación posterior es justa con la perspectiva."),
    ],
    op=("Lee estas tres perspectivas de ejemplo sobre «¿puede un deber ser más importante que un deseo?»: P1 (autor ficticio): «Los deberes dan estructura a la vida; sin ellos, solo seguiríamos impulsos.» P2: «Solo los deseos propios dan sentido; un deber impuesto vacía a la persona.» P3: «Los deberes valen cuando se eligen libremente y se vuelven deseos propios.» "
        "Construye una matriz con cuatro filas (tesis, razón, concepto de «deber», supuesto), escribe una coincidencia, el punto exacto de desacuerdo entre P1 y P2 y una pregunta abierta.",
        "Tesis: P1 el deber estructura; P2 el deseo da sentido; P3 el deber elegido se vuelve deseo. Razón: P1 sin deberes seguimos impulsos; P2 un deber impuesto vacía; P3 la elección une ambos. Concepto de deber: P1 estructura; P2 imposición; P3 compromiso elegido. Supuesto: P1 los impulsos son desordenados; P2 el sentido es personal; P3 se puede elegir un deber. Coincidencia: las tres valoran el sentido de la vida. Desacuerdo P1-P2: si el deber da o quita sentido. Pregunta abierta: ¿qué es un deber realmente elegido?",
        ["construye la matriz con cuatro filas", "señala una coincidencia", "identifica el punto exacto de desacuerdo", "formula una pregunta abierta"],
        ["matriz, coincidencia, desacuerdo y pregunta abierta escritos"],
        ["resumir cada texto sin compararlos", "no señalar un punto exacto de desacuerdo", "caricaturizar una perspectiva"],
        "Pregunta: «¿en qué fila ves la diferencia más fuerte?». Pídele que la escriba en una frase."),
    reinforce="Escribe una ficha de lectura de dos perspectivas ficticias que inventes sobre «¿qué hace a una persona confiable?», con tesis, razón y supuesto.",
    extend="Agrega una cuarta perspectiva intermedia a la matriz de la ficha y explica qué rasgos toma de las otras.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (borradores de ejemplo para el problema «¿tiene valor el tiempo que no se usa para algo útil?»). "
     "T1: «El tiempo libre es un tema muy importante.» "
     "T2: «Muchos jóvenes descansan los fines de semana.» "
     "T3: «El tiempo libre tiene valor.» "
     "T4: «El tiempo que no se usa para algo útil tiene valor intrínseco, porque hay actividades que valen por sí mismas; aunque se objete que sin metas nada se logra, el descanso y el juego también hacen posible una vida con sentido.»")
build(
    O5, 4, F,
    use="Aprenderé a formular una tesis filosófica propia a partir de las perspectivas investigadas, con razones, una objeción considerada y una respuesta.",
    prior=["Sé comparar perspectivas en una matriz.", "Sé formular un argumento con premisas y conclusión.", "Sé responder una objeción."],
    explain=[
        "Una tesis filosófica es una afirmación discutible que responde a la pregunta de investigación y que se defiende con razones. Se distingue de un tema («el tiempo libre es importante»), de un dato («muchos jóvenes descansan») y de una pregunta. También se distingue de un resumen de perspectivas. Una buena tesis es discutible (alguien razonable podría pensar otra cosa), precisa (usa conceptos definidos), fundamentada (se apoya en razones) y relevante para el problema.",
        "Para formularla se parte de lo investigado. Primero decides qué respondes a la pregunta, tomando posición frente a las perspectivas, ya sea a favor de una, combinando varias o rechazándolas con razones. Luego escribes al menos dos razones. Después anticipas la mejor objeción y escribes una respuesta. Finalmente, reconoces un límite: hasta dónde llega tu tesis.",
        "Tu tesis no tiene que coincidir con la de ninguna fuente, pero debe dialogar con ellas: mostrar qué aprendiste, con quién discutes y por qué tus razones son mejores o más completas. Tomar posición con razones no es partidismo: es el trabajo de la filosofía.",
    ],
    vocab=[("tesis filosófica", "afirmación discutible que responde a la pregunta de investigación y se defiende con razones"), ("discutible", "que una persona razonable podría rechazar con razones"), ("precisa", "que usa conceptos definidos"), ("fundamentada", "apoyada en razones que se pueden examinar"), ("límite de la tesis", "hasta dónde vale lo que se sostiene")],
    worked=[
        ("Distinguir tesis de tema y dato", "En la ficha, ¿cuáles de T1, T2 y T3 son una tesis fundamentada?",
         ["T1 es un tema; T2 es un dato.", "T3 afirma algo discutible, pero no ofrece razones ni precisa el concepto de valor."],
         "Ninguna todavía: T3 es discutible, pero le faltan razones y precisión"),
        ("Revisar una tesis", "¿Por qué T4 es una tesis mejor que T3?",
         ["T4 precisa que se trata de valor intrínseco.", "Además ofrece una razón, anticipa una objeción y la responde."],
         "Porque es discutible, precisa, fundamentada y considera una objeción"),
    ],
    mistakes=[("Escribir como tesis un resumen de lo que dijeron las fuentes.", "No hay posición propia que se pueda discutir.", "Responde a la pregunta con tu posición y explica con quién discutes."),
              ("Formular una tesis sin considerar ninguna objeción.", "Una tesis sin objeciones no se ha puesto a prueba.", "Busca la mejor objeción y escribe cómo la responderías.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es una tesis filosófica?", "Una afirmación discutible que responde a la pregunta y se defiende con razones", "Un dato comprobable", "Un resumen de las fuentes", "Una tesis debe tomar posición con razones."),
        ("abc", "{F} ¿Qué es T1?", "Un tema, porque nombra un asunto general", "Una tesis fundamentada", "Un dato", "No toma posición ni responde la pregunta."),
        ("abc", "{F} ¿Qué es T2?", "Un dato, porque se puede comprobar con una encuesta", "Una tesis filosófica", "Una pregunta", "Describe un hecho y no una posición discutible."),
        ("abc", "{F} Un estudiante mejora T3 así: «El tiempo libre tiene valor, porque sí». ¿Qué le sigue faltando?", "Una razón real que la apoye y precisar de qué valor habla", "Que sea más corta", "Un dato numérico", "Es discutible, pero no está fundamentada ni precisada."),
        ("abc", "{F} ¿Cuál es la razón que ofrece T4 para apoyar su tesis?", "Que hay actividades que valen por sí mismas", "Que sin metas nada se logra", "Que muchos jóvenes descansan los fines de semana", "La razón va tras «porque»; lo que sigue a «aunque» es la objeción y el dato describe un hecho."),
        ("ab", "{F} ¿Qué objeción anticipa T4?", "Que sin metas nada se logra", "Que el descanso es siempre malo", "Es la objeción que T4 menciona antes de responderla."),
        ("abc", "{F} ¿Cómo responde T4 a esa objeción?", "Afirma que el descanso y el juego también hacen posible una vida con sentido", "Niega que las metas existan", "Repite la tesis sin razón", "Ofrece una razón que complementa la objeción en vez de rechazarla."),
        ("abc", "¿Por qué una tesis debe ser discutible?", "Porque si nadie razonable podría rechazarla, no habría nada que argumentar", "Porque así se evitan las razones", "Porque debe ser falsa", "Una tesis necesita una posición que otra persona podría rebatir."),
        ("abc", "Un estudiante escribe como tesis: «Según P1, el tiempo vale por su utilidad; según P2, por sí mismo; según P3, por apoyo». ¿Qué es eso?", "Un resumen de perspectivas, no una tesis propia", "Una tesis excelente", "Un dato", "Solo describe y no toma una posición propia."),
        ("abc", "{F} Otro estudiante propone esta tesis: «El tiempo no útil tiene valor intrínseco, y por eso las escuelas deben eliminar todas las tareas». ¿Qué falla?", "Salta a una conclusión que no se sigue de su razón y excede el alcance de la tesis", "Es una tesis perfecta", "No usa conceptos", "De ese valor no se sigue eliminar todas las tareas; falta justificarlo y delimitarlo."),
        ("abc", "¿Qué hace un «límite de la tesis»?", "Indica hasta dónde vale lo que se sostiene", "Aumenta el número de razones", "Elimina las objeciones", "Reconocer el alcance es parte de argumentar con honestidad."),
        ("abc", "{F} Un estudiante cambia T4 así: «El tiempo no útil tiene valor intrínseco, aunque no todo el tiempo libre lo tiene». ¿Qué agrega?", "Un límite que acota el alcance de la tesis", "Una objeción nueva sin respuesta", "Un dato sin relación", "Reconoce que no todo el tiempo libre vale lo mismo."),
        ("abc", "¿Quién decide si tu tesis debe coincidir con la de una fuente?", "Nadie: debe dialogar con las fuentes, pero con tus propias razones", "El autor más famoso", "La mayoría del curso", "La tesis es propia y se apoya en razones examinadas."),
    ],
    ctx=("abc", "Un grupo ficticio investigó «¿es mejor un vínculo que dura o uno que se renueva?». Su borrador dice: «Los vínculos largos son mejores porque generan confianza; aunque se diga que renovar enriquece, la confianza permite conocer a fondo». ¿Qué parte es la objeción respondida?", "«Aunque se diga que renovar enriquece, la confianza permite conocer a fondo»", "«Los vínculos largos son mejores»", "«Porque generan confianza»", "La frase con «aunque» anticipa una objeción y la responde."),
    sc=[
        ("En Seminario de filosofía: ¿qué cuatro rasgos tiene una buena tesis?", "Discutible, precisa, fundamentada y relevante", "Son los cuatro rasgos de la explicación."),
        ("¿Qué diferencia hay entre una tesis y un resumen de perspectivas?", "La tesis toma una posición propia con razones", "El resumen solo describe lo que otros dicen."),
        ("¿Qué incluye una tesis bien construida?", "Posición, razones, una objeción respondida y un límite", "Son las partes del proceso de formulación."),
    ],
    op=("Elige una pregunta: «¿es justo que se premie solo el rendimiento?», «¿puede un deber ser más importante que un deseo?» o «¿tiene valor el tiempo que no se usa para algo útil?». "
        "Escribe tu tesis en una o dos frases, dos razones, la mejor objeción, tu respuesta y un límite. Indica con qué perspectiva de las de la unidad dialogas.",
        "Pregunta: ¿puede un deber ser más importante que un deseo? Tesis: un deber puede ser más importante que un deseo cuando protege algo de lo que depende otra persona. Razones: (1) los deseos pueden cambiar, pero la promesa afecta a otros; (2) sostener un deber en el tiempo construye confianza. Objeción: un deber impuesto puede vaciar a la persona. Respuesta: el deber que protege a otros se vuelve valioso al ser asumido libremente. Límite: no vale para deberes que dañan a la persona. Dialoga con P2 y P3.",
        ["formula una tesis discutible y precisa", "da al menos dos razones", "considera una objeción y la responde", "indica un límite y con qué perspectiva dialoga"],
        ["tesis, dos razones, objeción, respuesta, límite y perspectiva con la que dialoga"],
        ["escribir un resumen en lugar de una tesis", "no considerar objeciones", "no precisar los conceptos"],
        "Pregunta: «¿alguien razonable podría pensar lo contrario?». Si no, pídele que reformule su tesis para tomar posición."),
    reinforce="Convierte esta frase en una tesis discutible con una razón: «El deporte es importante».",
    extend="Reescribe tu tesis para dos públicos distintos (por ejemplo, tu curso y un docente) y explica qué cambiaste y por qué.",
)
