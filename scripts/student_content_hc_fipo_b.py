"""Filosofía política (electivo HC, 3.º y 4.º medio): OAC-03 (textos de la tradición sobre justicia, libertad, responsabilidad, igualdad y felicidad, clases 1 a 5) y OAC-04 (diálogos sobre la organización del poder y el Estado, clases 1 a 4). Resúmenes de ejemplo y casos ficticios."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada texto y cada caso está escrito en el enunciado. "
             "Los textos son resúmenes de ejemplo escritos para este cuaderno: no son citas de obras ni reemplazan su lectura, que queda para el docente. Los casos, lugares y personas son ficticios. "
             "Las posturas se presentan con sus razones y sin tomar partido por un sector político: tu tarea es entenderlas, compararlas y evaluarlas con argumentos. "
             "Si un tema te incomoda, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O3 = "FI-FIPO-3y4-OAC-03"
O4 = "FI-FIPO-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (texto de ejemplo escrito para este cuaderno). «¿Qué hace justa a una sociedad? Algunos responden que repartir los bienes por igual; otros, que cada persona reciba según lo que aporta; otros, que se atienda primero a quien más necesita. "
     "Cada respuesta supone una imagen distinta de las personas: iguales en dignidad, responsables de sus logros o dependientes unas de otras.»")
build(
    O3, 1, F,
    use="Aprenderé a leer críticamente un texto filosófico con cinco preguntas y a ubicar en él justicia, libertad, responsabilidad, igualdad y felicidad.",
    prior=["Sé reconstruir tesis, razones y supuestos.", "Sé qué es una perspectiva.", "Sé formular una objeción."],
    explain=[
        "Examinar críticamente un texto de la tradición filosófica es leerlo con preguntas y no solo para repetirlo. Cinco preguntas ordenan la lectura. ¿Qué pregunta intenta responder? ¿Qué conceptos usa y cómo los entiende? ¿Qué tesis y qué razones ofrece? ¿Qué imagen del ser humano supone? ¿Qué consecuencias éticas y políticas tiene y qué objeción cabría?",
        "Cinco conceptos atraviesan la tradición y se relacionan entre sí. La justicia es dar a cada quien lo que le corresponde según algún criterio. La libertad es la posibilidad de actuar o decidir por uno mismo. La responsabilidad es responder por las propias acciones. La igualdad es considerar a las personas con igual valor y derechos. La felicidad es una vida buena o con bienestar. Cada texto los combina de un modo propio.",
        "La visión del ser humano que un texto supone (por ejemplo, personas iguales, ambiciosas, solidarias o temerosas) condiciona lo que propone en ética, que se pregunta cómo debemos actuar, y en política, que se pregunta cómo organizar el poder y la convivencia. Los textos de esta clase son resúmenes de ejemplo; la lectura de las obras completas la guía el docente.",
    ],
    vocab=[("justicia", "dar a cada quien lo que le corresponde según un criterio"), ("libertad", "posibilidad de actuar o decidir por uno mismo"), ("responsabilidad", "responder por las propias acciones"), ("igualdad", "considerar a las personas con igual valor y derechos"), ("felicidad", "vida buena o con bienestar"), ("ética", "reflexión sobre cómo debemos actuar")],
    worked=[
        ("Aplicar las cinco preguntas", "Aplica las dos primeras preguntas de lectura al texto de la ficha.",
         ["Pregunta 1: el texto se pregunta qué hace justa a una sociedad.", "Pregunta 2: el concepto central es justicia, y aparecen tres criterios: igualdad, aporte y necesidad."],
         "Pregunta: qué hace justa a una sociedad. Concepto: justicia, con tres criterios de reparto"),
        ("Descubrir el supuesto", "¿Qué imagen de las personas acompaña al criterio «según lo que cada uno aporta»?",
         ["Busco la frase del texto: «responsables de sus logros».", "Ese criterio supone que las personas responden por lo que logran."],
         "Personas responsables de sus logros"),
    ],
    mistakes=[("Leer el texto buscando solo una frase que repetir en un trabajo.", "Se confunde citar con examinar.", "Aplica las cinco preguntas y escribe con tus palabras tesis, razones y supuesto."),
              ("Tratar los cinco conceptos como si fueran sinónimos.", "Se pierde la diferencia entre justicia, libertad, igualdad, responsabilidad y felicidad.", "Define cada uno con un rasgo propio y relaciónalos después.")],
    T=[
        ("abc", "Según la explicación, ¿qué es la responsabilidad?", "Responder por las propias acciones", "Dar a cada quien lo que le corresponde", "Considerar a todos con igual valor", "Así se define en la lista de conceptos; las otras opciones definen justicia e igualdad."),
        ("abc", "{F} ¿Cuántas respuestas distintas a su pregunta presenta el texto?", "Tres: repartir por igual, según el aporte y atender primero a quien más necesita", "Una sola: repartir por igual", "Dos: según el aporte y según la necesidad", "El texto enumera tres respuestas con «algunos… otros… otros»."),
        ("abc", "{F} ¿Qué criterio de reparto menciona el texto como «según lo que cada uno aporta»?", "Según el aporte o mérito", "Según la necesidad", "Según la igualdad", "Es el criterio que asigna según lo aportado."),
        ("abc", "{F} ¿Qué criterio de reparto atiende primero a quien más necesita?", "El de necesidad", "El de mérito", "El de igualdad de partes", "Responde a la tercera respuesta del texto."),
        ("abc", "{F} ¿Qué imagen del ser humano acompaña a «repartir por igual»?", "Personas iguales en dignidad", "Personas dependientes unas de otras", "Personas responsables de sus logros", "Según el texto, el reparto por igual se apoya en igualdad de dignidad."),
        ("En Filosofía política: ¿cómo se llama la reflexión sobre cómo debemos actuar?", "Ética", "Es el nombre que la explicación da a esa reflexión.", ),
        ("abc", "{F} ¿Qué consecuencia política tendría el criterio de necesidad?", "Se priorizaría a quienes más lo necesitan al repartir recursos", "Se repartirían los recursos por sorteo", "Se premiaría solo a quien más aporta", "Es lo que el criterio establece."),
        ("abc", "{F} Un estudiante resume: «El texto dice que la justicia es repartir por igual y nada más». ¿Qué error comete?", "Reduce el texto a una sola respuesta, cuando presenta tres", "Ninguno, es un resumen correcto", "Confunde la justicia con la libertad", "El texto compara tres respuestas con sus imágenes del ser humano."),
        ("abc", "{F} Un lector subraya «según lo que cada persona aporta» y escribe: «Esto supone que las personas responden por lo que logran». ¿Qué pregunta de lectura respondió?", "La del supuesto sobre el ser humano", "La de la pregunta del texto", "La de la objeción", "Identificó la imagen de las personas detrás del criterio."),
        ("abc", "{F} Una objeción posible al criterio de aporte es que…", "No todas las personas parten con las mismas oportunidades para aportar", "Que repartir según el aporte obliga a repartir igual para todas las personas", "Que el mérito es irrelevante porque nadie lo reconoce", "Es una razón que cuestiona el criterio sin atacar al texto."),
        ("{F} Elige un criterio del texto y escribe una consecuencia política y una objeción posible.", "Por ejemplo: necesidad; se priorizaría a quienes más lo necesitan, pero se podría objetar que desincentiva el esfuerzo", "Combina las preguntas 4 y 5 de lectura sobre un criterio del texto."),
        ("abc", "Una lectora anota: «El texto usa justicia como dar a cada quien lo que le corresponde según un criterio». ¿Qué pregunta de lectura respondió?", "¿Qué conceptos usa y cómo los entiende?", "¿Qué tesis y razones ofrece?", "¿Qué objeción cabría?", "Anotó cómo el texto entiende un concepto, que es la segunda pregunta de lectura."),
        ("abc", "Alguien dice: «Leer filosofía es memorizar frases». ¿Qué respuesta se apoya en esta clase?", "Es examinar con preguntas sus conceptos, razones, supuestos y consecuencias", "Tiene razón, porque no hay otra forma", "Solo sirve para citar en un trabajo", "La clase propone una lectura crítica con cinco preguntas."),
    ],
    ctx=("abc", "En un club de lectura ficticio se lee: «Cada persona debería poder decidir su propio camino, pero también responder por sus decisiones». ¿Qué dos conceptos de la clase aparecen?", "Libertad y responsabilidad", "Justicia e igualdad", "Felicidad y justicia", "Decidir por uno mismo es libertad y responder por lo que se decide es responsabilidad."),
    sc=[
        ("En Filosofía política: ¿qué es la justicia en esta clase?", "Dar a cada quien lo que le corresponde según un criterio", "Es la definición de la lista de conceptos."),
        ("Nombra tres de las cinco preguntas de lectura crítica.", "Por ejemplo: qué pregunta responde, qué tesis y razones ofrece, qué imagen del ser humano supone", "Son las preguntas de lectura crítica que ordena la explicación de la clase."),
        ("¿Por qué la imagen del ser humano importa en política?", "Porque condiciona qué se propone sobre cómo organizar el poder y la convivencia", "Si cambia la imagen de las personas, cambian las consecuencias políticas."),
    ],
    op=("Lee este texto de ejemplo escrito para este cuaderno: «Una sociedad es libre cuando nadie manda sobre otro sin su acuerdo; pero para que esa libertad valga, todos deben contar con lo mínimo para decidir su vida, como educación y salud.» "
        "Aplica las cinco preguntas de lectura: pregunta, conceptos, tesis y razones, imagen del ser humano, y una consecuencia y una objeción.",
        "Pregunta: qué hace libre a una sociedad. Conceptos: libertad e igualdad de condiciones. Tesis: la libertad exige acuerdo y condiciones mínimas. Imagen: personas que deciden su vida si cuentan con lo básico. Consecuencia: el Estado debería asegurar educación y salud. Objeción: asegurarlas podría limitar otras libertades.",
        ["responde las cinco preguntas de lectura", "no agrega ideas que el texto no tiene", "distingue consecuencia de objeción", "relaciona al menos dos conceptos"],
        ["ficha de lectura con las cinco preguntas respondidas"],
        ["copiar frases sin explicarlas", "no identificar la imagen del ser humano", "confundir consecuencia con objeción"],
        "Pregunta: «¿en qué parte del texto se apoya tu respuesta sobre la imagen de las personas?». Pídele que la señale."),
    reinforce="Elige una frase sobre justicia o libertad que hayas oído y responde con tus palabras las cinco preguntas de lectura.",
    extend="Escribe cómo cambiaría el texto de la ficha si partiera de la imagen de personas temerosas unas de otras.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (caso ficticio). Un fondo escolar de «Liceo Brisas» (no existe) tiene 10 becas de transporte para 25 postulantes. "
     "Criterio 1 (igualdad): sorteo entre todas las personas postulantes. Criterio 2 (mérito): según el promedio de notas. "
     "Criterio 3 (necesidad): según la distancia entre la casa y el liceo y los medios de transporte disponibles. "
     "Una postura asociada con John Rawls propone elegir las reglas imaginando que no sabemos qué lugar ocuparemos en la sociedad (velo de ignorancia).")
build(
    O3, 2, F,
    use="Aprenderé a comparar criterios de justicia (igualdad, mérito, necesidad) y a probar una regla con el velo de ignorancia.",
    prior=["Sé leer un texto con cinco preguntas.", "Sé qué es una consecuencia política.", "Sé definir con rasgos."],
    explain=[
        "La justicia distributiva se pregunta cómo repartir bienes, cargas y oportunidades. Tres criterios clásicos de reparto son la igualdad (todas las personas reciben lo mismo o tienen la misma oportunidad), el mérito (cada quien recibe según lo que aporta o logra) y la necesidad (se atiende primero a quien más lo necesita). Cada criterio suele asociarse con una imagen distinta de las personas: iguales en dignidad, responsables de sus logros o dependientes unas de otras.",
        "Igualdad y equidad no son lo mismo. Tratar a todas las personas de la misma manera no siempre las deja en condiciones iguales; la equidad ajusta el reparto para compensar diferencias injustas de punto de partida. Los criterios pueden combinarse: por ejemplo, un sorteo entre quienes cumplen una necesidad mínima.",
        "Una postura asociada con John Rawls propone un experimento mental: el velo de ignorancia. Imagina que debes elegir las reglas de una sociedad sin saber qué lugar ocuparás en ella (si serás de quienes tienen más o menos ventajas). Esa condición obliga a pensar reglas justas para cualquier posición. Es un método para evaluar reglas, no una descripción de la realidad.",
    ],
    vocab=[("justicia distributiva", "reflexión sobre cómo repartir bienes, cargas y oportunidades"), ("mérito", "criterio que reparte según lo que cada quien aporta o logra"), ("necesidad", "criterio que atiende primero a quien más lo necesita"), ("equidad", "ajustar el reparto para compensar diferencias injustas de punto de partida"), ("velo de ignorancia", "experimento mental: elegir reglas sin saber qué lugar se ocupará"), ("punto de partida", "condiciones con las que cada persona inicia")],
    worked=[
        ("Clasificar un criterio", "Un reparto de becas da prioridad a quienes viven más lejos y no tienen transporte. ¿Qué criterio usa?",
         ["Veo que la decisión mira la situación de cada persona, no su promedio ni el azar.", "Prioriza a quien más lo necesita."],
         "El criterio de necesidad"),
        ("Aplicar el velo de ignorancia", "Si no supieras si serás una persona postulante que vive lejos o cerca del liceo, ¿qué regla preferirías para el fondo de becas?",
         ["Imagino cualquier lugar posible: podría vivir lejos y sin transporte.", "Entonces querría una regla que me protegiera si estuviera en la peor posición."],
         "Una regla que considere la necesidad, para protegerme si estuviera en la peor posición"),
    ],
    mistakes=[("Creer que igualdad y equidad significan siempre lo mismo.", "Se olvida que tratar igual no siempre deja en condiciones iguales.", "Pregunta si los puntos de partida son parecidos antes de decidir el reparto."),
              ("Pensar que el velo de ignorancia describe lo que ocurre en la realidad.", "Se confunde un método con un hecho.", "Úsalo como experimento mental para evaluar reglas.")],
    T=[
        ("abc", "Según la explicación, ¿qué es el criterio de mérito?", "Repartir según lo que cada quien aporta o logra", "Repartir lo mismo a todos", "Repartir según la necesidad", "Es la definición de la clase."),
        ("abc", "{F} ¿Qué criterio corresponde al sorteo entre todas las personas postulantes?", "Igualdad", "Mérito", "Necesidad", "El sorteo da la misma posibilidad a cada persona."),
        ("abc", "{F} ¿Qué criterio corresponde a asignar según el promedio de notas?", "Mérito", "Igualdad", "Necesidad", "Premia lo que cada persona logra."),
        ("abc", "Un banco de alimentos ficticio entrega primero a las familias que esta semana no tienen ingresos. ¿Qué criterio usa?", "Necesidad", "Mérito", "Igualdad", "Atiende primero a quien más lo necesita."),
        ("abc", "En Filosofía política: ¿qué es la equidad?", "Ajustar el reparto para compensar diferencias injustas de punto de partida", "Dar siempre la misma cantidad a todos", "Premiar solo a quien más logra", "La equidad corrige desigualdades de partida, y no siempre iguala el reparto."),
        ("abc", "{F} ¿Qué es el velo de ignorancia?", "Un experimento mental para elegir reglas sin saber qué lugar se ocupará", "Un procedimiento para ocultar los nombres de quienes postulan", "Una regla que reparte según la necesidad", "Así describe la ficha ese experimento mental para elegir reglas."),
        ("abc", "{F} Las 10 becas se reparten por sorteo entre las 25 postulaciones. ¿Qué podría objetar una postulante que vive lejos y no tiene transporte?", "Que el sorteo no considera que su necesidad de transporte es mayor", "Que el sorteo favorece a quien tiene mejor promedio", "Que el sorteo da más probabilidades a quien vive cerca", "El sorteo trata igual a todas y no tiene en cuenta diferencias de necesidad."),
        ("abc", "{F} Una estudiante vive lejos y no tiene transporte, pero su promedio es bajo. ¿Qué criterio la favorece?", "Necesidad", "Mérito", "Ningún criterio la favorece", "La necesidad atiende la situación de transporte, no el promedio."),
        ("abc", "{F} Otro estudiante tiene el mejor promedio, pero vive a una cuadra del liceo. ¿Qué criterio lo favorece más?", "Mérito", "Necesidad", "Equidad", "Sus notas altas lo ubican primero en el criterio de mérito."),
        ("abc", "{F} Una regla propone sortear solo entre quienes viven a más de una distancia mínima. ¿Qué criterios combina?", "Necesidad e igualdad", "Mérito y necesidad", "Mérito e igualdad", "Usa un umbral de necesidad y luego el azar entre iguales."),
        ("abc", "{F} Una estudiante dice: «Con el velo de ignorancia elegiría solo mérito, porque seguro tendré buen promedio». ¿Qué falla tiene?", "Desobedece el experimento, porque no puede suponer qué lugar ocupará", "Ninguna, es un uso correcto", "Confunde mérito con necesidad", "El velo exige no saber qué posición se tendrá."),
        ("abc", "¿Por qué tratar a todas las personas igual puede no ser equitativo?", "Porque si los puntos de partida son muy distintos, el mismo trato mantiene la desventaja", "Porque la igualdad nunca es justa", "Porque la equidad prohíbe repartir", "La equidad corrige desventajas de partida."),
        ("abc", "{F} Una objeción posible al criterio de mérito es que…", "El promedio puede reflejar ventajas de partida distintas y no solo esfuerzo", "El promedio mide solo la necesidad de cada persona", "El mérito reparte siempre lo mismo a todas las personas", "Cuestiona que el resultado dependa solo del aporte personal."),
    ],
    ctx=("abc", "Un municipio ficticio debe repartir entradas gratuitas a un festival entre jóvenes de distintos barrios. Una regla las sortea entre todos; otra prioriza a los barrios con menos espacios culturales. ¿Cuál se acerca más a la equidad?", "La que prioriza a los barrios con menos espacios culturales", "La que sortea entre todos sin considerar el barrio", "Ninguna, porque cualquier prioridad es injusta", "Compensa una desventaja de partida (menos oferta cultural)."),
    sc=[
        ("En Filosofía política: ¿qué es el velo de ignorancia?", "Un experimento mental para elegir reglas sin saber qué lugar se ocupará", "Sirve para evaluar reglas desde cualquier posición."),
        ("Nombra los tres criterios de reparto de la clase.", "Igualdad, mérito y necesidad", "Son los tres criterios de la explicación."),
        ("¿Por qué igualdad y equidad no son lo mismo?", "Porque tratar igual no siempre compensa diferencias injustas de punto de partida", "La equidad ajusta el reparto para corregir esas diferencias."),
    ],
    op=("Elige uno de estos reparto ficticios: (1) 8 cupos en un taller de verano para 20 estudiantes; (2) 5 computadores prestados para 12 familias del sector. "
        "Propón una regla de reparto que combine al menos dos criterios (igualdad, mérito, necesidad), pruébala con el velo de ignorancia y escribe una objeción posible.",
        "Reparto 1. Regla: sorteo entre quienes no tienen otro taller disponible (necesidad e igualdad). Velo: si no sé quién seré, quiero que me beneficie si no tengo alternativa. Objeción: no premia el esfuerzo de quien postuló con mejor proyecto.",
        ["combina dos criterios y los nombra", "prueba la regla con el velo de ignorancia", "formula una objeción pertinente", "no supone qué posición ocupará quien decide"],
        ["regla de reparto, prueba con el velo y objeción"],
        ["usar un solo criterio sin justificarlo", "usar el velo suponiendo la propia posición", "olvidar la objeción"],
        "Pregunta: «¿qué regla elegirías si fueras la persona que quedó última?». Pídele que la considere."),
    reinforce="Describe un reparto real de tu entorno (turnos, cupos, materiales) y señala qué criterio usa y si podría ser más equitativo.",
    extend="Explica por qué podría convenir mezclar necesidad y mérito en el reparto de becas, y qué objeción tendría esa mezcla.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (casos ficticios). Caso A: Elena puede hacer lo que quiera con su tiempo y nadie se lo impide, pero no tiene dinero ni transporte para salir de su sector. "
     "Caso B: un grupo de aficionados prohíbe a sus integrantes criticar al grupo en sus propias redes porque dice que daña su imagen, aunque no se ha mostrado ningún daño concreto a terceros. "
     "Caso C: Marco abre una puerta creyendo que es la bodega de materiales, pero era la sala de archivos, y desordena documentos privados sin darse cuenta de su error.")
build(
    O3, 3, F,
    use="Aprenderé a distinguir dos modos de entender la libertad, el principio de daño y las condiciones de la responsabilidad.",
    prior=["Sé qué es el poder y la autoridad.", "Sé leer un texto con cinco preguntas.", "Sé distinguir consecuencia de objeción."],
    explain=[
        "Una postura asociada con el filósofo Isaiah Berlin distingue dos modos de entender la libertad. La libertad negativa consiste en que nadie interfiera ni impida lo que una persona quiere hacer. La libertad positiva consiste en tener la capacidad real de decidir y realizar los propios proyectos, lo que depende también de condiciones como recursos, educación o salud. Una persona puede tener libertad negativa y poca libertad positiva.",
        "Una postura asociada con John Stuart Mill, llamada principio de daño, sostiene que el poder de una comunidad sobre una persona solo se justifica contra su voluntad cuando se trata de evitar daño a otras personas. El bien propio de la persona, por sí solo, no basta para obligarla. La discusión política está en qué cuenta como daño.",
        "La responsabilidad es responder por las propias acciones. Una postura clásica sostiene que, para ser plenamente responsable, una persona debe actuar sabiendo lo que hace y pudiendo elegir. Si ignora algo importante sin culpa propia o actúa obligada, la responsabilidad se reduce. No desaparece siempre: se examina cada caso.",
    ],
    vocab=[("libertad negativa", "ausencia de interferencia de otros en lo que alguien quiere hacer"), ("libertad positiva", "capacidad real de decidir y realizar los propios proyectos"), ("principio de daño", "solo se justifica limitar a alguien contra su voluntad para evitar daño a otros"), ("daño", "perjuicio concreto a otra persona"), ("responsabilidad", "responder por las propias acciones"), ("coacción", "obligar a alguien a actuar contra su voluntad")],
    worked=[
        ("Dos modos de libertad", "En el Caso A, ¿qué libertad tiene Elena y cuál le falta?",
         ["Nadie le impide hacer lo que quiere: tiene libertad negativa.", "No cuenta con dinero ni transporte, así que le falta capacidad real: libertad positiva limitada."],
         "Tiene libertad negativa y le falta libertad positiva"),
        ("Aplicar el principio de daño", "En el Caso B, ¿qué dice el principio de daño sobre la prohibición del grupo?",
         ["El principio justifica limitar solo para evitar daño a otras personas.", "En el caso no se ha mostrado ningún daño concreto a terceros."],
         "La prohibición no se justifica con el principio de daño tal como queda descrito"),
    ],
    mistakes=[("Creer que si nadie te impide algo ya tienes toda la libertad que importa.", "Se olvida que faltan condiciones para poder hacerlo.", "Pregunta si la persona cuenta con recursos y capacidades reales."),
              ("Pensar que el principio de daño permite prohibir cualquier cosa que moleste.", "Se confunde molestia con daño.", "Distingue un perjuicio concreto a otras personas de una incomodidad.")],
    T=[
        ("abc", "¿Qué es la libertad negativa según la explicación?", "Ausencia de interferencia de otros en lo que alguien quiere hacer", "Capacidad real de realizar los propios proyectos", "Obligación de obedecer", "Así se define; no habla de carencias, sino de que nadie interfiere."),
        ("abc", "¿Qué es la libertad positiva según la explicación?", "Capacidad real de decidir y realizar los propios proyectos", "Ausencia de reglas", "Permiso de otros para actuar", "Incluye condiciones como recursos, educación o salud."),
        ("abc", "Según la explicación, ¿qué sostiene el principio de daño?", "Solo se justifica limitar a alguien contra su voluntad para evitar daño a otras personas", "Se puede limitar a alguien siempre que moleste", "Nunca se puede limitar a nadie", "Pone el daño a otros como condición de la limitación."),
        ("abc", "Una trabajadora ficticia puede elegir libremente su empleo, pero ningún transporte llega a su sector y solo puede aceptar trabajos a pie. ¿Qué libertad está más limitada?", "La libertad positiva, porque le faltan condiciones reales para elegir", "La libertad negativa, porque alguien le prohíbe elegir", "Ninguna, porque nadie la obliga", "No hay una prohibición de otros, pero sí falta capacidad real de realizar su proyecto."),
        ("abc", "{F} En el Caso B, ¿qué libertad se restringe?", "La de expresarse críticamente en sus propias redes", "La de salir de su sector", "La de elegir transporte", "El grupo prohíbe a sus integrantes criticar."),
        ("abc", "{F} ¿Qué condición de la responsabilidad se ve afectada en el Caso C?", "El conocimiento de lo que se hace, porque Marco creía abrir una bodega", "La posibilidad de elegir, porque lo obligaron", "Ninguna", "Marco actuó sin saber lo que realmente abría."),
        ("abc", "{F} En el Caso C, ¿se puede decir que Marco no tiene ninguna responsabilidad?", "No necesariamente: su responsabilidad se reduce, pero hay que examinar si pudo haber verificado", "Sí, porque cualquier error la elimina", "Sí, porque no existe responsabilidad", "Una postura clásica sostiene que la ignorancia reduce la responsabilidad y se examina caso a caso."),
        ("abc", "Una empresa ficticia vierte residuos en el río del que se abastece un pueblo. ¿Qué diría el principio de daño sobre limitar a la empresa?", "Que podría justificarse, porque causa un daño concreto a otras personas", "Que no se justifica, porque cada empresa decide por sí misma", "Que depende de cuánto le moleste a la mayoría", "Hay un perjuicio concreto a terceros, que es la condición del principio."),
        ("abc", "Un estudiante afirma: «Si no hay ley que me lo prohíba, soy libre». ¿Qué le falta considerar según la libertad positiva?", "Si cuenta con las condiciones reales para hacer lo que quiere", "Si otras personas harían lo mismo", "Si otros opinan igual", "La libertad positiva exige capacidad real."),
        ("abc", "Una conductora ficticia choca por conducir muy rápido sabiendo el peligro. ¿Qué se puede decir de su responsabilidad?", "Es responsable, porque sabía lo que hacía y pudo elegir otra cosa", "No es responsable, porque nadie la obligó a chocar", "Su responsabilidad desaparece por la velocidad", "Actuó con conocimiento y posibilidad de elegir."),
        ("abc", "Una persona firma un documento que le pone un encargado bajo amenaza de perder todo. ¿Qué condición de responsabilidad se reduce?", "La posibilidad de elegir", "El conocimiento de lo que hace", "Ninguna", "La persona actuó bajo coacción, lo que limita su posibilidad de elegir."),
        ("abc", "{F} Si el grupo del Caso B mostrara que una crítica difunde información falsa que daña a una persona, ¿cambia la evaluación?", "Sí: ahora existe un posible daño concreto a un tercero y el principio de daño podría justificar una limitación", "No: la prohibición ya estaba justificada", "No: nada puede limitar la expresión", "El cambio de hechos permite aplicar la condición de daño."),
        ("abc", "¿Cuál es una objeción posible al principio de daño?", "No siempre es claro qué cuenta como daño", "Que impide limitar cualquier conducta", "Que solo vale para delitos graves", "La discusión se desplaza a definir qué es un daño."),
    ],
    ctx=("abc", "Un curso ficticio debate si prohibir celulares en el patio. Un grupo dice que solo se justifica si usarlos daña a otras personas; otro, que la distracción ya es motivo. ¿Qué postura se apoya en el principio de daño?", "La del primer grupo", "La del segundo grupo", "Ninguna", "El primer grupo exige daño a otras personas."),
    sc=[
        ("En Filosofía política: ¿qué es la libertad positiva?", "La capacidad real de decidir y realizar los propios proyectos", "Depende de condiciones, no solo de la ausencia de interferencia."),
        ("¿Qué sostiene el principio de daño?", "Que solo se justifica limitar a alguien contra su voluntad para evitar daño a otros", "Es la idea asociada con Mill en la explicación."),
        ("¿Qué dos condiciones de la responsabilidad señala la explicación?", "Actuar sabiendo lo que se hace y poder elegir", "Son las dos condiciones de la postura clásica."),
    ],
    op=("Elige un caso ficticio: (1) un liceo prohíbe pegar afiches en los pasillos para que no se ensucien; (2) una municipalidad prohíbe vender comida en una plaza sin dar razones concretas. "
        "Evalúa el caso con libertad negativa, libertad positiva y principio de daño, y escribe una conclusión con una objeción.",
        "Caso 1. Negativa: se interfiere el pegar afiches. Positiva: se limita expresar iniciativas. Daño: el ensuciar es un perjuicio menor y se podría resolver con paneles. Conclusión: es más justificable un panel que una prohibición total. Objeción: los paneles pueden ser insuficientes.",
        ["usa los tres conceptos correctamente", "distingue daño de molestia", "formula una conclusión con razón", "incluye una objeción pertinente"],
        ["evaluación con los tres conceptos y una conclusión"],
        ["confundir molestia con daño", "ignorar la libertad positiva", "no justificar la conclusión"],
        "Pregunta: «¿qué daño concreto a terceros aparece en tu caso?». Pídele que lo nombre."),
    reinforce="Observa una regla de tu entorno y anota qué libertad limita y si esa limitación evita un daño a otras personas.",
    extend="Compara libertad negativa y positiva con un ejemplo de salud o de educación y explica cuál te parece más relevante allí.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (textos de ejemplo escritos para este cuaderno). "
     "Texto A (postura utilitarista): «Una acción es correcta cuando produce la mayor felicidad posible para el mayor número de personas afectadas. La felicidad se entiende como placer y ausencia de dolor.» "
     "Texto B (postura de la vida buena, asociada con Aristóteles): «La felicidad no es solo placer: es vivir bien según las virtudes y en comunidad, desarrollando lo mejor de uno mismo. El ser humano es por naturaleza un animal político.»")
build(
    O3, 4, F,
    use="Aprenderé a comparar dos concepciones de la felicidad y de qué visión del ser humano se desprenden en ética y política.",
    prior=["Sé leer un texto con cinco preguntas.", "Sé distinguir justicia, libertad y responsabilidad.", "Sé formular una objeción."],
    explain=[
        "La felicidad puede entenderse de modos distintos. En el utilitarismo, una tradición asociada con Jeremy Bentham y John Stuart Mill, lo correcto es producir el mayor bienestar posible para el mayor número, y el bienestar se mide por placer y ausencia de dolor. La política sería entonces una forma de organizar decisiones para sumar bienestar.",
        "En una postura de la vida buena, asociada con Aristóteles, la felicidad (en griego, eudaimonía) es vivir bien según las virtudes, es decir, hábitos de carácter valiosos como la justicia y la moderación. Para ella el ser humano es un animal político: florece en comunidad. La política sería una forma de crear condiciones para que las personas desarrollen lo mejor de sí.",
        "Cada concepción supone una visión del ser humano: la primera lo ve como un ser que siente placer y dolor, la segunda como alguien que desarrolla capacidades y vive con otros. Y cada una tiene consecuencias éticas y políticas distintas. Comparar no es elegir sin razones: es ver qué explica mejor cada caso y qué objeciones enfrenta.",
    ],
    vocab=[("utilitarismo", "postura que mide lo correcto por el bienestar del mayor número"), ("eudaimonía", "vida buena como desarrollo de las virtudes en comunidad"), ("virtud", "hábito de carácter valioso, como la justicia o la moderación"), ("bienestar", "estado de placer y ausencia de dolor en el utilitarismo"), ("animal político", "ser humano que florece viviendo en comunidad"), ("florecer", "desarrollar lo mejor de uno mismo")],
    worked=[
        ("Identificar la visión del ser humano", "¿Qué visión del ser humano supone el Texto B?",
         ["Busco la frase: «el ser humano es por naturaleza un animal político».", "Esa frase indica que vive y se desarrolla en comunidad."],
         "Una visión del ser humano como alguien que se desarrolla en comunidad"),
        ("Aplicar a una decisión", "Un municipio ficticio puede construir una plaza que usan muchas personas o una biblioteca que usan pocas pero cambia su vida. ¿Qué pregunta haría un utilitarista?",
         ["Pregunta por el bienestar total: a cuántas personas afecta y cuánto.", "Compararía el bienestar sumado de ambas opciones."],
         "¿Cuál opción produce más bienestar para más personas?"),
    ],
    mistakes=[("Creer que el utilitarismo equivale a buscar el placer propio.", "Se confunde bienestar general con egoísmo.", "Recuerda que mide el bienestar del mayor número de personas afectadas."),
              ("Creer que la vida buena es solo placer.", "Se olvida la idea de virtudes y comunidad.", "Distingue placer de florecimiento en comunidad.")],
    T=[
        ("abc", "{F} Según el Texto A, ¿cuándo es correcta una acción?", "Cuando produce la mayor felicidad posible para el mayor número de personas afectadas", "Cuando cumple una virtud", "Cuando agrada a quien la realiza", "Es la definición que ofrece el texto para una acción correcta."),
        ("abc", "{F} Según el Texto B, ¿qué es la felicidad?", "Vivir bien según las virtudes y en comunidad", "Placer y ausencia de dolor", "Tener cargos de poder", "Es lo que sostiene el texto."),
        ("abc", "¿Qué significa «animal político» en la explicación?", "Ser humano que florece viviendo en comunidad", "Persona que ocupa un cargo", "Persona que vota", "Se refiere a la naturaleza social del ser humano."),
        ("abc", "{F} ¿Qué visión del ser humano supone el Texto A?", "Un ser que siente placer y dolor", "Un ser que busca poder sobre los demás", "Un ser que actúa solo por deber", "Mide el bienestar con placer y ausencia de dolor."),
        ("abc", "{F} ¿Qué consecuencia política sugiere el Texto B?", "Crear condiciones para que las personas desarrollen lo mejor de sí en comunidad", "Maximizar el placer inmediato", "Reducir la vida en comunidad para evitar conflictos", "La política sería una forma de favorecer el florecimiento."),
        ("abc", "{F} Un curso ficticio decide con la regla del Texto A y supone la misma intensidad de alegría y de molestia en todos. La opción X deja contentas a 30 personas y molestas a 5; la opción Y, contentas a 12 y molestas a 0. ¿Cuál prefiere el Texto A?", "La opción X, porque suma más bienestar total (30 − 5 = 25 frente a 12)", "La opción Y, porque nadie queda molesto", "Ninguna, porque no se pueden comparar", "Con esos supuestos, el bienestar total de X es mayor que el de Y."),
        ("abc", "{F} Una escuela ficticia decide con el Texto B. ¿Qué pregunta debe hacerse?", "¿Qué opción ayuda a las personas a desarrollar sus capacidades y a convivir bien?", "¿Qué opción suma más placer inmediato?", "¿Qué opción cuesta menos?", "Es el criterio de la vida buena."),
        ("abc", "{F} Un estudiante dice: «El Texto A busca el placer de cada uno». ¿Qué error comete?", "Olvida que habla del bienestar del mayor número de personas afectadas", "Nada, es correcto", "Confunde el texto con el B", "El utilitarismo evalúa el bienestar total."),
        ("abc", "{F} Si un taller ficticio aumenta el placer de muchos pero daña a pocos de forma grave, ¿qué plantea el Texto A?", "Que se debe comparar el bienestar total y evaluar si el daño a pocos se compensa", "Que nunca importa el daño", "Que importa solo el daño", "Calcula el bienestar total, lo que genera discusión sobre el daño a minorías."),
        ("abc", "{F} Ante lo anterior, ¿qué objeción haría una postura de la vida buena al Texto A?", "Que reducir la felicidad a placer deja fuera las virtudes y la vida en comunidad", "Que sumar el bienestar de muchas personas es imposible por definición", "Que el placer siempre es dañino para la comunidad", "Es una crítica a su idea de felicidad."),
        ("{F} Escribe una pregunta que formularía el Texto B y no el Texto A ante una decisión de la comunidad.", "Por ejemplo: ¿esta decisión ayuda a que las personas desarrollen sus capacidades y convivan mejor?", "Parte de la idea de florecer en comunidad."),
        ("abc", "{F} ¿Qué objeción podría hacer una postura utilitarista al Texto B?", "Que «vivir bien» es vago y difícil de medir para decidir políticas", "Que la comunidad impide ser feliz", "Que las virtudes son placeres", "Cuestiona la imprecisión del criterio de la vida buena."),
        ("abc", "Comparar dos concepciones de la felicidad significa…", "Ver qué explica mejor cada caso y qué objeciones enfrenta cada una", "Elegir la que más me gusta sin razones", "Afirmar que ambas son iguales", "La comparación es un trabajo de razones."),
    ],
    ctx=("abc", "Un centro de estudiantes ficticio puede financiar una fiesta masiva o un taller que desarrolla habilidades de pocos. Una delegada dice: «Elijamos lo que haga feliz a más gente». ¿Qué concepción de la felicidad usa?", "La utilitarista, centrada en el bienestar del mayor número", "La de la vida buena, centrada en las virtudes", "Ninguna", "Mide por bienestar del mayor número."),
    sc=[
        ("En Filosofía política: ¿qué es el utilitarismo?", "Una postura que mide lo correcto por el bienestar del mayor número", "Se asocia con Bentham y Mill en la explicación."),
        ("¿Qué es la eudaimonía?", "La vida buena como desarrollo de las virtudes en comunidad", "Es la concepción asociada con Aristóteles."),
        ("¿Por qué la visión del ser humano cambia la política?", "Porque cada visión sugiere distintas condiciones que la política debe procurar", "Una persona que siente placer y dolor o que florece en comunidad requiere políticas distintas."),
    ],
    op=("Elige una decisión ficticia: (1) un barrio debe elegir entre arreglar una cancha o abrir una sala de estudio; (2) un liceo debe elegir entre un paseo de curso o talleres artísticos. "
        "Analiza la decisión primero con el Texto A y luego con el B, indica qué visión del ser humano supone cada uno y escribe tu conclusión con una objeción a la postura que prefieras.",
        "Decisión 1. Texto A: ¿qué opción produce más bienestar para más personas? Supone seres que sienten placer y dolor. Texto B: ¿cuál ayuda a desarrollar capacidades en comunidad? Supone un ser que florece con otros. Conclusión: la sala de estudio, porque favorece capacidades. Objeción: la cancha es más usada.",
        ["aplica los dos textos con su criterio propio", "nombra la visión del ser humano de cada uno", "concluye con una razón", "formula una objeción a la postura elegida"],
        ["análisis comparado con conclusión y objeción"],
        ["mezclar los criterios de ambos textos", "no nombrar la visión del ser humano", "elegir sin razón"],
        "Pregunta: «¿qué criterio del texto usas para tu conclusión?». Pídele que lo cite."),
    reinforce="Pregunta a una persona de tu casa qué entiende por vivir bien y clasifica su respuesta con las dos concepciones, sin juzgarla.",
    extend="Escribe un caso donde ambas concepciones lleven a la misma decisión por razones distintas.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (objeciones de ejemplo). "
     "Postura 1 (utilitarismo): una acción es correcta si produce el mayor bienestar total. Objeción 1: «Podría aprobar perjudicar gravemente a una minoría si con eso aumenta el bienestar de los demás». "
     "Postura 2 (reparto según mérito): se recibe según lo aportado. Objeción 2: «Las personas parten con ventajas distintas, así que el mérito mide también la suerte». "
     "Postura 3 (libertad como no interferencia): lo central es que nadie impida lo que cada quien quiere hacer. Objeción 3: «Ignora si las personas cuentan con las condiciones reales para decidir».")
build(
    O3, 5, F,
    use="Aprenderé a examinar críticamente textos comparando posturas, a formular objeciones fuertes y a responderlas sin deformar las ideas.",
    prior=["Sé las cinco preguntas de lectura crítica.", "Conozco criterios de reparto, dos modos de libertad y dos concepciones de la felicidad.", "Sé conceder y distinguir."],
    explain=[
        "Examinar críticamente textos filosóficos exige poner a prueba las posturas con objeciones y ver si resisten. Una objeción fuerte apunta a una premisa o a una consecuencia central, no a un detalle. Una respuesta puede conceder lo cierto, distinguir conceptos, mostrar que la objeción supone algo dudoso o ajustar la postura.",
        "En la ficha, la objeción 1 señala una consecuencia incómoda del utilitarismo: sacrificar a una minoría. Una respuesta posible es ajustar la postura agregando derechos básicos como límite. La objeción 2 cuestiona que el mérito dependa solo de la persona. Una respuesta posible es combinar mérito con equidad. La objeción 3 señala que la libertad como no interferencia puede ignorar condiciones reales. Una respuesta posible es sumar la libertad positiva.",
        "Comparar posturas también requiere decir qué ven mejor y qué dejan de ver. Evaluar no es declarar un ganador: es mostrar las razones que cada postura tiene y los límites que enfrenta, y exponer la propia posición con consistencia.",
    ],
    vocab=[("objeción fuerte", "razón que apunta a una premisa o consecuencia central de una postura"), ("consecuencia incómoda", "resultado de una postura que parece injusto"), ("ajustar la postura", "reformularla para que resista una objeción"), ("derechos básicos", "protecciones que no se pueden sacrificar por un beneficio mayor"), ("combinar", "unir criterios de varias posturas"), ("límite", "punto donde una postura deja de explicar bien")],
    worked=[
        ("Responder ajustando", "Responde la objeción 1 sin abandonar la postura 1.",
         ["Concedo que la consecuencia es incómoda.", "Ajusto la postura: agrego que ciertos derechos básicos no se pueden sacrificar por sumar bienestar."],
         "Reformular el utilitarismo con derechos básicos como límite"),
        ("Distinguir el blanco de la objeción", "¿A qué postura va dirigida la objeción 3?",
         ["La objeción dice que se ignoran condiciones reales para decidir.", "Eso se refiere a la libertad como no interferencia (postura 3)."],
         "A la postura 3, la libertad como no interferencia"),
    ],
    mistakes=[("Responder a una objeción repitiendo la postura con otras palabras.", "No se aporta una razón nueva.", "Concede, distingue o ajusta."),
              ("Deformar la postura para que la objeción parezca más fácil de responder.", "Se ataca una versión débil.", "Reconstruye con caridad antes de responder.")],
    T=[
        ("abc", "{F} ¿A qué postura va dirigida la objeción 1?", "Al utilitarismo", "Al reparto según mérito", "A la libertad como no interferencia", "Habla de sacrificar a una minoría para aumentar el bienestar total."),
        ("abc", "{F} ¿A qué postura va dirigida la objeción 2?", "Al reparto según mérito", "Al utilitarismo", "A la libertad como no interferencia", "Cuestiona que el mérito dependa solo de la persona."),
        ("abc", "{F} ¿Qué critica la objeción 3?", "Que ignora si las personas cuentan con condiciones reales para decidir", "Que prohíbe toda libertad", "Que reparte según el mérito", "Apunta a la falta de condiciones reales."),
        ("abc", "{F} Una estudiante responde a la objeción 3: «Cada persona debe decidir sola, así que las condiciones no importan». ¿Qué problema tiene la respuesta?", "Repite la postura 3 sin aportar una razón nueva", "Concede lo cierto de la objeción", "Ajusta la postura para que resista", "No responde con una razón: solo reafirma lo que la objeción cuestiona."),
        ("abc", "{F} ¿Qué respuesta combina criterios frente a la objeción 2?", "Combinar mérito con equidad", "Eliminar el mérito sin razones", "Aceptar que no existe el mérito", "Reconoce la objeción y ajusta con un segundo criterio."),
        ("abc", "{F} ¿Qué respuesta suma un concepto a la postura 3 frente a la objeción 3?", "Incorporar la libertad positiva", "Negar las condiciones", "Prohibir toda interferencia", "La libertad positiva considera la capacidad real."),
        ("abc", "{F} Una estudiante responde a la objeción 1: «Los utilitaristas son crueles». ¿Qué error comete?", "Ataca a las personas y no la postura", "Ajusta la postura", "Distingue conceptos", "La respuesta no examina la razón de la objeción y se queda en las personas."),
        ("abc", "{F} Otro responde a la objeción 2: «No existe ventaja inicial». ¿Qué problema tiene?", "Niega sin razones una premisa que la objeción sustenta", "Concede la objeción", "Ajusta la tesis", "La respuesta niega la premisa sin ofrecer razones que la sostengan."),
        ("abc", "{F} ¿Por qué la objeción 1 es fuerte?", "Apunta a una consecuencia central que muchos consideran injusta", "Porque ataca a quien propone la postura", "Porque se refiere a un detalle secundario del texto", "Muestra una consecuencia incómoda de la postura."),
        ("{F} Elige una de las tres objeciones y escribe una respuesta que conceda algo y ajuste la postura.", "Por ejemplo: concedo que el mérito puede reflejar ventajas, por lo que combino mérito con apoyos que igualen los puntos de partida", "Aplica las estrategias de la explicación."),
        ("abc", "{F} Una estudiante compara las posturas 1 y 3 y dice: «Ambas dicen lo mismo». ¿Qué falla tiene?", "Las dos tratan criterios distintos: bienestar total y no interferencia", "Ninguna", "Las dos hablan de mérito", "Compararlas exige ver su criterio central."),
        ("abc", "Después de oír una objeción fuerte, una estudiante mantiene su postura pero precisa que no se aplica a emergencias. ¿Qué hizo?", "Ajustó su postura", "Atacó a la persona", "Abandonó toda defensa", "Precisó el alcance para resistir la objeción."),
        ("abc", "¿Qué es evaluar una postura en esta clase?", "Mostrar sus razones, límites y objeciones, y exponer una posición consistente", "Declarar un ganador sin argumentos", "Elegir la postura más antigua", "Es el trabajo de razones descrito en la explicación."),
    ],
    ctx=("abc", "En un taller de filosofía ficticio, una joven dice: «Si es mejor para la mayoría, se hace aunque perjudique gravemente a un grupo pequeño». ¿Qué objeción de la ficha la enfrenta?", "La objeción 1", "La objeción 2", "La objeción 3", "Ante la consecuencia de sacrificar a una minoría, se aplica la objeción 1."),
    sc=[
        ("En Filosofía política: ¿qué es una objeción fuerte?", "Una razón que apunta a una premisa o consecuencia central de una postura", "No se limita a un detalle."),
        ("Nombra dos formas de responder una objeción.", "Conceder lo cierto y ajustar la postura (o distinguir conceptos)", "Son dos de las estrategias para responder objeciones que enseña la explicación."),
        ("¿Por qué comparar posturas no es declarar un ganador?", "Porque se trata de mostrar razones, límites y objeciones de cada una", "La evaluación es un trabajo de razones."),
    ],
    op=("Elige dos de las tres posturas de la ficha y compáralas en un caso ficticio: un liceo debe decidir cómo asignar el uso de una cancha entre clubes grandes y pequeños. "
        "Escribe qué diría cada postura, una objeción fuerte a cada una y una respuesta, y termina con tu posición consistente en cuatro líneas.",
        "Posturas 1 y 2. Postura 1: elegir lo que produzca más bienestar total. Postura 2: dar más a quien más ha aportado. Objeción a 1: puede dejar sin cancha a un club pequeño. Respuesta: asegurar un mínimo. Objeción a 2: los clubes grandes parten con ventaja. Respuesta: combinar con equidad. Posición: mínimo asegurado más criterio de aporte.",
        ["expone cada postura sin deformarla", "formula una objeción fuerte a cada una", "responde con una estrategia nombrada", "su posición es consistente con lo anterior"],
        ["comparación con objeciones, respuestas y posición"],
        ["deformar una postura", "responder repitiendo", "tomar una posición que contradice sus respuestas"],
        "Pregunta: «¿tu posición final se desprende de tus respuestas?». Pídele que lo compruebe."),
    reinforce="Elige una postura con la que estés de acuerdo y escribe la mejor objeción que podría hacerle alguien razonable.",
    extend="Escribe una posición propia que combine dos posturas de la ficha y señala qué límite enfrenta.",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 6 (diálogo de ejemplo). Camila: «Sin Estado, cada persona haría lo que quisiera y habría abusos.» "
     "Diego: «Con Estado, unos pocos terminan mandando al resto.» "
     "Ana: «Quizá depende de cómo se organice el Estado y de quién pueda corregirlo cuando se equivoca. Camila, ¿qué entiendes por Estado?»")
build(
    O4, 1, F,
    use="Aprenderé a participar en un diálogo filosófico sobre el poder y el Estado: a formular preguntas abiertas, pedir razones y escuchar.",
    prior=["Sé qué es una relación de poder.", "Sé formular una pregunta filosófica.", "Sé reconstruir una postura."],
    explain=[
        "Un diálogo filosófico es una conversación en la que se busca entender un problema con razones, no ganar una discusión. Se distingue del debate porque no se trata de vencer, sino de examinar ideas juntos y estar dispuesto a cambiar de opinión si aparecen mejores razones. Su tema aquí son las formas de organización del poder en la sociedad: sus fundamentos (en qué se apoya el derecho a mandar) y sus finalidades (para qué existe).",
        "Algunas reglas ayudan. Formular preguntas abiertas («¿para qué existe el Estado?»). Escuchar y parafrasear lo que dijo la otra persona antes de responder. Pedir razones y definiciones («¿qué entiendes por Estado?»). Objetar a la idea y no a la persona. Conceder lo cierto y cambiar de opinión cuando hay buenas razones.",
        "Una pregunta guía para este tema es: ¿para qué existe un Estado y qué justifica su derecho a mandar? Tiene varias respuestas posibles, y es importante no asignar una posición política a nadie: en un diálogo filosófico se presentan posturas con argumentos, y cada persona puede ensayar ideas sin que se la identifique con ellas.",
    ],
    vocab=[("diálogo filosófico", "conversación que busca entender un problema con razones"), ("debate", "discusión orientada a vencer a la otra parte"), ("fundamento", "aquello en lo que se apoya el derecho a mandar"), ("finalidad", "para qué existe una forma de organización del poder"), ("parafrasear", "decir con otras palabras lo que dijo otra persona"), ("pregunta abierta", "pregunta que admite varias respuestas con razones")],
    worked=[
        ("Parafrasear", "Parafrasea la intervención de Diego en la ficha.",
         ["Identifico su idea central: que con Estado algunos pocos terminan mandando.", "La digo con otras palabras para comprobar que la entendí."],
         "Diego teme que un Estado concentre el mando en unas pocas personas"),
        ("Pedir una definición", "¿Qué pregunta hace Ana para aclarar el desacuerdo?",
         ["Observo su última frase.", "Pide definir el concepto que está en juego."],
         "«¿Qué entiendes por Estado?»"),
    ],
    mistakes=[("Confundir diálogo con debate y responder solo para ganar.", "Se pierde la búsqueda conjunta de razones.", "Parafrasea, pide razones y reconoce lo cierto de la otra postura."),
              ("Atribuir una posición política a la persona por lo que ensaya en el diálogo.", "Se confunde ensayar una idea con identificarse con un sector.", "Presenta las posturas con argumentos sin etiquetar a nadie.")],
    T=[
        ("abc", "Según la explicación, ¿qué busca un diálogo filosófico?", "Entender un problema con razones", "Vencer a las demás personas", "Repetir lo que dice la autoridad", "Su propósito es examinar ideas con razones."),
        ("abc", "¿Qué diferencia hay entre diálogo filosófico y debate según la explicación?", "El diálogo busca entender juntos y el debate busca ganar", "El diálogo no usa razones", "El debate no tiene reglas", "Esa es la diferencia que plantea el texto."),
        ("abc", "{F} ¿Qué teme Camila que ocurra sin Estado?", "Que haya abusos porque cada persona haría lo que quisiera", "Que unos pocos manden", "Que el Estado se equivoque", "Es lo que dice su intervención."),
        ("abc", "{F} ¿Qué tienen en común las intervenciones de Camila y de Diego?", "Cada una se apoya en un temor distinto sobre lo que pasaría con o sin Estado", "Ambas coinciden en que el Estado es innecesario", "Ambas piden una definición del Estado", "Camila teme abusos sin Estado y Diego teme que unos pocos manden con Estado."),
        ("abc", "{F} ¿Qué aporta la frase de Ana «depende de cómo se organice el Estado y de quién pueda corregirlo»?", "Propone mirar la organización y la posibilidad de corrección", "Elige la postura de Camila", "Elige la postura de Diego", "Introduce criterios para evaluar el Estado."),
        ("abc", "{F} ¿Qué regla del diálogo cumple Ana al preguntar a Camila qué entiende por Estado?", "Pedir razones y definiciones", "Parafrasear", "Cambiar de opinión", "Su pregunta pide aclarar el concepto que está en juego en el desacuerdo."),
        ("abc", "Una estudiante responde a Diego: «Qué ingenuo eres». ¿Qué regla incumple?", "Objetar a la idea y no a la persona", "Parafrasear", "Pedir razones", "Su respuesta ataca a la persona."),
        ("abc", "Ariel dice: «El Estado es innecesario». Cristóbal responde: «¿Qué entiendes por Estado y qué ocurriría sin él?». ¿Qué hace Cristóbal?", "Pide una definición y una razón", "Ataca a Ariel", "Cambia de tema", "Su pregunta aclara el concepto y pide la razón."),
        ("abc", "¿Cuál es una pregunta abierta sobre el tema de la clase?", "¿Qué justifica el derecho del Estado a mandar?", "¿Cuántos ministerios hay en un gobierno?", "¿Cuándo se vota?", "Admite varias respuestas posibles y cada una exige razones para defenderse."),
        ("abc", "{F} Después de escuchar a Camila, Diego dice: «Si te entendí bien, dices que sin Estado habría abusos». ¿Qué hace Diego?", "Parafrasea", "Pide una definición", "Ataca la idea", "Resume con otras palabras para comprobar que entendió."),
        ("abc", "Un grupo en diálogo concluye: «Todos tenemos que pensar igual». ¿Qué falla tiene?", "Confunde diálogo con acuerdo obligatorio, cuando el objetivo es examinar razones", "Ninguna", "Usa una pregunta abierta", "El diálogo examina razones y no obliga a que todas las personas coincidan."),
        ("abc", "{F} Si Camila cambia de opinión tras oír una razón de Diego, ¿qué muestra?", "Disposición a revisar su posición con buenas razones", "Debilidad de carácter", "Que Diego ganó", "Revisar la posición es una regla del diálogo."),
        ("abc", "En el diálogo filosófico de esta clase, ¿qué se hace con las posiciones políticas de las personas?", "No se asignan: se presentan posturas con argumentos", "Se clasifica a cada persona", "Se descalifica a quien piense distinto", "Se evita etiquetar y se examinan los argumentos."),
    ],
    ctx=("abc", "En una asamblea escolar ficticia dos estudiantes discuten si el centro de estudiantes debería poder decidir el uso del presupuesto sin consultar. ¿Cuál es el mejor aporte desde el diálogo filosófico?", "Preguntar qué justifica que unos decidan por todos y quién puede corregir esa decisión", "Decir que quien piense distinto no sabe", "Cerrar la discusión votando de inmediato", "Pide fundamentos y corrección, que son temas del diálogo."),
    sc=[
        ("En Filosofía política: ¿qué es un diálogo filosófico?", "Una conversación que busca entender un problema con razones", "No busca vencer, sino examinar ideas."),
        ("Nombra dos reglas del diálogo.", "Parafrasear y pedir razones (u objetar a la idea y no a la persona)", "Son reglas del diálogo filosófico que enumera la explicación de la clase."),
        ("¿Qué son los fundamentos y las finalidades de una forma de organizar el poder?", "En qué se apoya el derecho a mandar y para qué existe", "Son los dos ejes del tema."),
    ],
    op=("Elige una pregunta: (1) ¿Para qué existe un Estado? (2) ¿Qué justifica que una autoridad pueda mandar? "
        "Escribe un diálogo ficticio breve de cuatro intervenciones entre dos personas en el que se pida una definición, se parafrasee una idea, se presente una objeción y se conceda algo.",
        "Pregunta 2. A: Una autoridad puede mandar cuando la gente la reconoce. B: Si te entendí bien, dices que lo que cuenta es el reconocimiento. ¿Y si la gente se equivoca? A: Puede equivocarse, aunque sin reconocimiento no habría legitimidad. B: Es cierto; quizá se necesita además un modo de corregirse.",
        ["incluye una definición pedida", "incluye una paráfrasis", "presenta una objeción a la idea y no a la persona", "incluye una concesión"],
        ["diálogo de cuatro intervenciones"],
        ["debatir para ganar", "atacar a la persona", "no incluir ninguna concesión"],
        "Pregunta: «¿dónde está la concesión en tu diálogo?». Pídele que la señale."),
    reinforce="Escribe tres preguntas abiertas sobre el poder en una institución de tu entorno.",
    extend="Reescribe una discusión real o imaginada como diálogo filosófico usando las reglas de la clase.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 7 (de ejemplo). Glosario de un taller ficticio. "
     "Estado: conjunto de instituciones que ejercen el poder público sobre un territorio y su población. "
     "Gobierno: las personas que dirigen el Estado en un período. "
     "Actor social: persona o grupo que participa en la vida pública (sindicatos, juntas de vecinos, organizaciones, medios, empresas). "
     "Una postura asociada con Max Weber describe al Estado como la institución que reclama con éxito el monopolio del uso legítimo de la fuerza dentro de un territorio.")
build(
    O4, 2, F,
    use="Aprenderé a definir Estado, gobierno, institución y actor social, y a distinguir fundamentos y finalidades del poder.",
    prior=["Sé qué es el poder y la autoridad.", "Sé las reglas del diálogo filosófico.", "Sé buscar un contraejemplo."],
    explain=[
        "El Estado es el conjunto de instituciones que ejercen el poder público sobre un territorio y su población. Una postura asociada con Max Weber lo caracteriza por reclamar con éxito el monopolio del uso legítimo de la fuerza dentro de un territorio. No es lo mismo que el gobierno, que son las personas que dirigen el Estado durante un período. Cambian los gobiernos, y el Estado continúa.",
        "Una institución es un conjunto de reglas, cargos y procedimientos que organizan una actividad, como un tribunal, un colegio o un municipio. Un actor social es una persona o grupo que participa en la vida pública, como sindicatos, juntas de vecinos, organizaciones, medios o empresas. La sociedad civil agrupa a los actores que no son Estado ni empresas.",
        "Para dialogar sobre el poder conviene distinguir sus fundamentos y sus finalidades. Un fundamento es aquello en lo que se apoya su derecho a mandar, como el acuerdo de las personas, la tradición, la utilidad para todos o los derechos que protege. Una finalidad es para qué existe, como la seguridad, la justicia, la libertad o el bienestar. Dos personas pueden coincidir en la finalidad y diferir en el fundamento.",
    ],
    vocab=[("Estado", "conjunto de instituciones que ejercen el poder público sobre un territorio y su población"), ("gobierno", "personas que dirigen el Estado en un período"), ("institución", "conjunto de reglas, cargos y procedimientos que organizan una actividad"), ("actor social", "persona o grupo que participa en la vida pública"), ("fundamento", "aquello en lo que se apoya el derecho a mandar"), ("finalidad", "para qué existe una forma de organización del poder")],
    worked=[
        ("Estado y gobierno", "Cambia el equipo que dirige un municipio ficticio tras una elección. ¿Cambió el Estado o el gobierno?",
         ["Pregunto qué cambió: las personas que dirigen durante un período.", "Las instituciones (reglas, cargos, procedimientos) siguen."],
         "Cambió el gobierno; el Estado y sus instituciones continúan"),
        ("Fundamento y finalidad", "Un diálogo ficticio dice: «El Estado existe para proteger la seguridad, y manda legítimamente porque las personas lo acordaron». ¿Cuál es la finalidad y cuál el fundamento?",
         ["La finalidad responde para qué existe: proteger la seguridad.", "El fundamento responde en qué se apoya su derecho a mandar: el acuerdo de las personas."],
         "Finalidad: la seguridad. Fundamento: el acuerdo de las personas"),
    ],
    mistakes=[("Confundir Estado con gobierno.", "Se identifica el Estado con las personas que lo dirigen ahora.", "Pregunta si habla de las instituciones permanentes o de quienes dirigen en un período."),
              ("Confundir fundamento con finalidad.", "Ambos responden por qué existe el poder, pero con preguntas distintas.", "Fundamento: ¿en qué se apoya su derecho? Finalidad: ¿para qué existe?")],
    T=[
        ("abc", "{F} ¿Qué es el Estado según la ficha?", "Conjunto de instituciones que ejercen el poder público sobre un territorio y su población", "Las personas que dirigen en un período", "Cualquier grupo con armas", "Es la definición de la ficha."),
        ("abc", "{F} ¿Qué es el gobierno?", "Las personas que dirigen el Estado en un período", "El conjunto de instituciones permanentes", "Un actor social", "Así define la ficha de la clase a ese término."),
        ("abc", "{F} ¿Cuál de estos es un actor social?", "Una junta de vecinos", "El monopolio del uso legítimo de la fuerza", "Un territorio", "Los actores sociales participan en la vida pública."),
        ("abc", "¿Qué responde la pregunta «¿para qué existe?» sobre el poder?", "La finalidad", "El fundamento", "El gobierno", "La finalidad señala el para qué."),
        ("abc", "¿Qué responde la pregunta «¿en qué se apoya su derecho a mandar?»?", "El fundamento", "La finalidad", "El actor social", "El fundamento es aquello en lo que se apoya su derecho."),
        ("abc", "{F} Según la postura asociada con Weber, ¿qué caracteriza al Estado?", "Reclamar con éxito el monopolio del uso legítimo de la fuerza en un territorio", "Repartir bienes", "Tener un presidente", "Es el rasgo que la ficha destaca."),
        ("abc", "Un periodista ficticio dice: «El Estado cambió porque se eligió otro presidente». ¿Qué confusión comete?", "Confunde el Estado con el gobierno", "Confunde fundamento con finalidad", "Confunde actor con institución", "El cambio de dirigentes afecta al gobierno."),
        ("abc", "Una persona dice: «El Estado puede mandar porque protege los derechos de todas las personas». ¿Qué expresa?", "Un fundamento", "Una finalidad", "Un gobierno", "Indica en qué se apoya su derecho a mandar."),
        ("abc", "Una estudiante dice: «El Estado existe para garantizar seguridad y justicia». ¿Qué expresa?", "Finalidades", "Fundamentos", "Actores sociales", "La expresión señala para qué existe el Estado y por eso es una finalidad."),
        ("abc", "{F} Un sindicato ficticio organiza una campaña. ¿Qué es en esta clase?", "Un actor social", "Un gobierno", "Un Estado", "Participa en la vida pública sin ser parte del Estado, como define la ficha."),
        ("abc", "Dos personas coinciden en que el Estado existe para la seguridad, pero una dice que manda por acuerdo y otra por tradición. ¿En qué difieren?", "En el fundamento", "En la finalidad", "En el gobierno", "Coinciden en el para qué y difieren en el apoyo."),
        ("abc", "{F} Una definición dice: «Estado es cualquier grupo con armas». Según la ficha, ¿cuál es el problema?", "Es muy amplia: no exige que el uso de la fuerza sea reclamado como legítimo ni que sea público", "Es muy estrecha", "Es correcta", "Incluiría grupos sin legitimidad, y la definición de la ficha lo evita."),
        ("abc", "Un colegio ficticio cambia de director, pero mantiene sus reglas y cargos. ¿Qué se mantiene?", "La institución", "El gobierno", "El actor social", "Las reglas y cargos son la institución."),
    ],
    ctx=("abc", "En un foro ficticio alguien dice: «El poder público debe existir para proteger la salud de todas las personas, y puede mandar porque protege derechos». ¿Cuál es la finalidad y cuál el fundamento?", "Finalidad: proteger la salud; fundamento: que protege derechos", "Finalidad: proteger derechos; fundamento: proteger la salud", "Finalidad y fundamento son lo mismo en esta frase", "La finalidad responde para qué existe y el fundamento en qué se apoya su derecho a mandar."),
    sc=[
        ("En Filosofía política: ¿qué es el Estado?", "El conjunto de instituciones que ejercen el poder público sobre un territorio", "Se distingue del gobierno, que son las personas que dirigen por un período."),
        ("¿Qué diferencia hay entre fundamento y finalidad?", "El fundamento es en qué se apoya el derecho a mandar y la finalidad es para qué existe", "Responden dos preguntas distintas: en qué se apoya el derecho y para qué existe."),
        ("¿Quiénes son actores sociales?", "Personas o grupos que participan en la vida pública, como juntas de vecinos o sindicatos", "Incluyen organizaciones, medios o empresas, según la definición de la ficha."),
    ],
    op=("Elige un caso ficticio: (1) un liceo con directiva estudiantil, apoderados y profesorado que deben decidir un reglamento; (2) un barrio con junta de vecinos, comercio y municipio que deben decidir el uso de una plaza. "
        "Identifica instituciones y actores, y escribe en dos frases la finalidad y el fundamento que propondrías para la autoridad que decide, y una pregunta para dialogar.",
        "Caso 2. Instituciones: municipio y junta de vecinos. Actores: vecinos, comercio. Finalidad: ordenar el uso de la plaza para que sirva a todos. Fundamento: la participación de los afectados. Pregunta: ¿quién debe poder corregir una decisión sobre la plaza?",
        ["identifica instituciones y actores", "formula finalidad y fundamento por separado", "no confunde Estado con gobierno", "escribe una pregunta abierta"],
        ["identificación de instituciones y actores, finalidad, fundamento y pregunta"],
        ["confundir fundamento con finalidad", "llamar Estado al gobierno", "dar una pregunta cerrada"],
        "Pregunta: «¿tu fundamento responde en qué se apoya el derecho a decidir?». Pídele que lo compruebe."),
    reinforce="Anota tres actores sociales de tu comuna y qué hacen en la vida pública, sin juzgarlos.",
    extend="Explica un ejemplo en que dos autoridades compartan finalidad pero tengan fundamentos distintos.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 8 (posturas de ejemplo; resúmenes breves, no las obras). "
     "Postura A (tradición contractualista): el Estado se justifica por un acuerdo entre las personas para proteger su vida y sus derechos. "
     "Postura B (asociada con Robert Nozick): el Estado debe limitarse a proteger derechos básicos y hacer cumplir acuerdos; hacer más violaría libertades. "
     "Postura C (asociada con John Rawls): el Estado debe asegurar instituciones básicas justas y corregir desventajas injustas. "
     "Postura D (anarquismo filosófico): el Estado no es necesario ni está justificado; la cooperación voluntaria puede reemplazarlo.")
build(
    O4, 3, F,
    use="Aprenderé a reconstruir cuatro posturas sobre el Estado, sus actores e instituciones, y a compararlas con sus razones y objeciones.",
    prior=["Sé distinguir fundamento y finalidad.", "Sé reconstruir tesis y razones.", "Sé las reglas del diálogo filosófico."],
    explain=[
        "Existen distintas posturas filosóficas sobre el Estado. Una tradición contractualista lo explica como un acuerdo de las personas. Una postura que defiende un Estado mínimo limita sus funciones a proteger derechos básicos y hacer cumplir acuerdos. Una postura igualitaria lo ve como responsable de que las instituciones básicas sean justas y corrijan desventajas. El anarquismo filosófico sostiene que el Estado no está justificado.",
        "Cada postura da un lugar distinto a los actores sociales y a las instituciones. Para el Estado mínimo, las organizaciones voluntarias y los mercados hacen buena parte del trabajo social. Para la postura igualitaria, instituciones como la educación o la salud deben corregir desventajas. Para el anarquismo, la cooperación voluntaria entre actores reemplazaría al Estado. Lo propio de la filosofía es reconstruir las razones de cada una con caridad, sin identificar a quien la expone con un sector político.",
        "También cada postura enfrenta objeciones. Al Estado mínimo se le objeta que puede dejar sin protección a quienes parten en desventaja. A la postura igualitaria, que puede restringir libertades de quienes pagan más. Al contractualismo, que ningún acuerdo real firmó cada persona. Al anarquismo, que la cooperación voluntaria puede no bastar para resolver conflictos graves.",
    ],
    vocab=[("contractualismo", "idea de que el Estado se justifica por un acuerdo entre las personas"), ("Estado mínimo", "Estado limitado a proteger derechos básicos y hacer cumplir acuerdos"), ("postura igualitaria", "postura que pide corregir desventajas injustas mediante instituciones"), ("anarquismo filosófico", "postura que niega que el Estado esté justificado"), ("cooperación voluntaria", "colaboración sin obligación impuesta"), ("desventaja injusta", "diferencia de punto de partida que no se justifica")],
    worked=[
        ("Reconstruir una postura", "Reconstruye la postura B de la ficha en tres partes.",
         ["Tesis: el Estado debe limitarse a proteger derechos básicos y hacer cumplir acuerdos.", "Razón: hacer más violaría libertades."],
         "Tesis: Estado limitado a proteger derechos. Razón: hacer más viola libertades. Supuesto: las libertades individuales son centrales"),
        ("Identificar una objeción", "¿Qué objeción se podría hacer a la postura A?",
         ["Veo que se apoya en un acuerdo entre las personas.", "Un acuerdo real no lo firmó cada persona, así que su fundamento puede discutirse."],
         "Ningún acuerdo real fue firmado por cada persona"),
    ],
    mistakes=[("Atribuir una postura a quien la expone en el diálogo.", "Se mezcla presentar un argumento con identificarse con él.", "Habla de «una postura sostiene…» y no digas «tú eres de…»."),
              ("Presentar solo las razones de la postura que se comparte.", "Se pierde la reconstrucción caritativa de las demás.", "Reconstruye cada postura con su mejor razón antes de objetar.")],
    T=[
        ("abc", "{F} ¿Qué sostiene la postura A?", "Que el Estado se justifica por un acuerdo para proteger la vida y los derechos", "Que el Estado no es necesario", "Que el Estado debe corregir toda desventaja", "Es la tesis contractualista de la ficha."),
        ("abc", "{F} Alguien dice: «El Estado solo debería encargarse de proteger derechos y de que se cumplan los acuerdos». ¿Con qué postura de la ficha coincide?", "Con la postura B", "Con la postura C", "Con la postura D", "Limita al Estado a proteger derechos básicos y hacer cumplir acuerdos, como la postura B."),
        ("abc", "{F} ¿Qué sostiene la postura C?", "Que el Estado debe asegurar instituciones justas y corregir desventajas injustas", "Que el Estado solo hace cumplir contratos", "Que el Estado es innecesario", "Es la tesis central que la ficha atribuye a la postura igualitaria."),
        ("abc", "{F} ¿Qué sostiene la postura D?", "Que el Estado no está justificado y la cooperación voluntaria puede reemplazarlo", "Que el Estado es el único actor", "Que solo importan las leyes", "Es la tesis del anarquismo filosófico."),
        ("abc", "{F} Una estudiante dice: «B y D son lo mismo, porque ambas limitan al Estado». ¿Qué falla tiene?", "B acepta un Estado limitado a funciones básicas y D niega que el Estado esté justificado", "Ninguna, porque ambas piden menos Estado", "B y D piden que el Estado reparta riqueza", "Limitar al Estado no es lo mismo que negar su justificación."),
        ("abc", "{F} ¿Qué actor tendría un papel central en el anarquismo filosófico?", "Las organizaciones y personas que cooperan voluntariamente", "El gobierno", "Los tribunales", "La ficha propone reemplazar al Estado por cooperación voluntaria."),
        ("abc", "{F} ¿Qué objeción se suele hacer al Estado mínimo según la explicación?", "Que puede dejar sin protección a quienes parten en desventaja", "Que da demasiado poder al Estado para repartir riqueza", "Que niega que los acuerdos deban cumplirse", "Es la objeción que plantea la explicación."),
        ("abc", "{F} ¿Qué objeción se suele hacer a la postura igualitaria según la explicación?", "Que puede restringir libertades de quienes pagan más", "Que deja sin protección a quienes parten en desventaja", "Que niega que existan derechos básicos", "Es la objeción a la postura igualitaria que menciona la explicación."),
        ("abc", "{F} ¿Qué objeción se suele hacer al anarquismo filosófico?", "Que la cooperación voluntaria puede no bastar para resolver conflictos graves", "Que da al Estado poder para limitar toda libertad", "Que no reconoce ningún derecho individual", "Es la objeción al anarquismo filosófico que señala la explicación."),
        ("abc", "{F} En un diálogo, un estudiante dice: «Tú defiendes la postura B, así que eres de ese sector». ¿Qué falla tiene?", "Etiqueta a la persona en vez de discutir la postura", "Reconstruye bien la postura", "Aporta una objeción válida", "La intervención no discute las razones de la postura y solo etiqueta."),
        ("abc", "{F} Una estudiante reconstruye la postura C y dice: «Quiere que el Estado reparta todo por igual». ¿Qué falla tiene?", "Deforma la postura: pide corregir desventajas injustas, no repartir todo por igual", "Ninguna", "Confunde con la postura D", "La ficha habla de instituciones justas y corrección de desventajas."),
        ("abc", "{F} Las posturas B y C aceptan que el Estado proteja derechos básicos. ¿En qué difieren?", "En cuánto más debe hacer: B lo limita a eso y C agrega corregir desventajas injustas", "En que B rechaza el Estado y C lo acepta", "En que B exige un acuerdo firmado por cada persona y C no", "Ambas aceptan el Estado y difieren en el alcance de sus funciones."),
        ("abc", "{F} Un liceo ficticio discute si el Estado debería financiar útiles escolares para estudiantes con menos recursos. ¿Qué postura lo apoyaría más directamente?", "La C, por corregir desventajas", "La B, por limitar al Estado", "La D, por reemplazarlo", "Se alinea con la corrección de desventajas."),
    ],
    ctx=("abc", "En un taller ficticio se discute cómo asegurar el acceso seguro a un barrio. Una persona dice: «No necesitamos Estado: las organizaciones vecinales se coordinarán». Otra dice: «El Estado debe asegurar el acceso a todos los barrios». ¿Con qué posturas de la ficha se relacionan?", "La primera con la postura D y la segunda con la postura C", "La primera con la postura C y la segunda con la postura D", "La primera con la postura A y la segunda con la postura B", "La primera niega la necesidad del Estado (D) y la segunda pide corregir desventajas con instituciones (C)."),
    sc=[
        ("En Filosofía política: ¿qué es el contractualismo?", "La idea de que el Estado se justifica por un acuerdo entre las personas", "Es la postura A de la ficha."),
        ("¿Qué objeción se hace al contractualismo?", "Que ningún acuerdo real fue firmado por cada persona", "Cuestiona el fundamento del contractualismo, que es el acuerdo entre las personas."),
        ("¿Por qué no se debe identificar a una persona con la postura que expone?", "Porque presentar un argumento no es afiliarse a un sector", "El diálogo examina posturas con argumentos."),
    ],
    op=("Elige dos posturas de la ficha y un caso ficticio: un barrio debe decidir quién se encarga del alumbrado de pasajes. "
        "Escribe qué diría cada postura, una razón y una objeción para cada una, y una pregunta de diálogo que ayude a avanzar sin descalificar a nadie.",
        "Posturas B y C. B: el municipio protege la seguridad básica y el resto lo organizan vecinos; razón: evitar imponer cargas. Objeción: pasajes pobres quedarían sin luz. C: el municipio asegura luz en todos los pasajes; razón: corregir desventajas. Objeción: exige recursos de otras personas. Pregunta: ¿qué mínimo de luz debería estar asegurado para todos?",
        ["reconstruye cada postura con caridad", "incluye una razón y una objeción por postura", "la pregunta es abierta y no descalifica", "no etiqueta a ninguna persona"],
        ["comparación de dos posturas en un caso, con pregunta de diálogo"],
        ["deformar una postura", "etiquetar personas", "no incluir objeciones"],
        "Pregunta: «¿qué razón daría la postura que no prefieres?». Pídele que la escriba con caridad."),
    reinforce="Elige una institución cercana (colegio, consultorio, municipio) y describe qué haría con ella cada una de las cuatro posturas.",
    extend="Escribe una quinta postura posible sobre el Estado y señala qué objeción enfrentaría.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 9 (diálogo de ejemplo). Nora: «El Estado debe asegurar un mínimo de servicios básicos para todos, porque nadie elige dónde nace.» "
     "Pablo: «Eso es porque tú quieres un Estado gigante.» "
     "Nora: «No dije gigante; dije un mínimo. ¿Qué entiendes tú por mínimo?» "
     "Pablo: «Protección de derechos básicos. Si el Estado hace más, termina decidiendo por las personas.» "
     "Nora: «Entiendo tu temor a que decida por las personas. ¿Crees que podríamos incluir controles ciudadanos para evitarlo?»")
build(
    O4, 4, F,
    use="Aprenderé a conducir un diálogo filosófico con movimientos claros (aclarar, objetar, conceder, sintetizar) y a evaluar una intervención.",
    prior=["Sé las reglas del diálogo filosófico.", "Sé reconstruir cuatro posturas sobre el Estado.", "Sé distinguir fundamento y finalidad."],
    explain=[
        "Un diálogo filosófico avanza con movimientos reconocibles. Aclarar pide definir un término o precisar una idea («¿qué entiendes por…?»). Objetar presenta una razón en contra de una tesis. Conceder reconoce lo cierto en la idea de la otra persona. Sintetizar propone una idea que recoge lo valioso de ambas posturas. Cada movimiento debe apuntar a la idea y no a la persona.",
        "Un buen diálogo evita ciertos errores: etiquetar a la persona («tú quieres un Estado gigante»), deformar la tesis, cambiar de tema o repetir lo mismo con más fuerza. Cuando alguien comete uno de esos errores, conviene devolver el diálogo a la idea con una pregunta tranquila.",
        "Evaluar un diálogo es preguntar: ¿se aclararon los conceptos?, ¿se respondieron las objeciones?, ¿se concedió lo cierto?, ¿se avanzó hacia una idea mejor? Participar activamente no es hablar más, sino contribuir con razones y escuchar. Cuando el tema es el poder y el Estado, no se asignan posiciones partidistas: se examinan argumentos.",
    ],
    vocab=[("aclarar", "pedir que se defina un término o se precise una idea"), ("objetar", "presentar una razón en contra de una tesis"), ("conceder", "reconocer lo cierto en la idea de otra persona"), ("sintetizar", "proponer una idea que recoja lo valioso de dos posturas"), ("etiquetar", "atribuir a una persona una posición para descalificarla"), ("devolver a la idea", "volver a la tesis cuando el diálogo se desvía")],
    worked=[
        ("Reconocer un movimiento", "En la ficha, Nora pregunta: «¿Qué entiendes tú por mínimo?». ¿Qué movimiento hace?",
         ["Observo que pide precisar un término.", "Eso es aclarar."],
         "Aclarar"),
        ("Corregir una intervención", "Pablo dice: «Eso es porque tú quieres un Estado gigante». ¿Qué error comete y cómo se devuelve el diálogo a la idea?",
         ["Etiqueta a Nora en vez de discutir su razón.", "Nora lo corrige aclarando lo que dijo y pidiendo la definición."],
         "Etiqueta a la persona; se devuelve a la idea aclarando lo dicho y pidiendo una definición"),
    ],
    mistakes=[("Hablar más fuerte o más seguido creyendo que así se participa mejor.", "Se confunde participar con ocupar el tiempo.", "Participa con razones y escuchando."),
              ("Dar por terminada la discusión sin sintetizar ni conceder nada.", "Se pierde la oportunidad de avanzar.", "Busca una idea que recoja lo valioso de ambas posturas.")],
    T=[
        ("abc", "Sofía dice: «La ley debe ser igual para todos». Rafael responde: «¿A qué llamas igual: mismo trato o mismas oportunidades?». ¿Qué movimiento hace Rafael?", "Aclarar", "Objetar", "Sintetizar", "Su pregunta pide precisar el significado de un término."),
        ("abc", "Matías le dice a Valentina: «Piensas así porque eres de las que siempre quieren mandar». ¿Qué error comete Matías?", "Etiqueta a la persona en vez de discutir su idea", "Concede lo cierto", "Sintetiza dos ideas", "Atribuye una posición a Valentina para descalificarla."),
        ("abc", "{F} ¿Qué razón en contra de la tesis de Nora presenta Pablo cuando dice «si el Estado hace más, termina decidiendo por las personas»?", "Una objeción", "Una aclaración", "Una síntesis", "Es una razón contra el aumento de funciones."),
        ("abc", "{F} ¿Qué movimiento hace Nora al decir «Entiendo tu temor a que decida por las personas»?", "Conceder", "Aclarar", "Etiquetar", "Reconoce lo cierto en la preocupación de Pablo."),
        ("abc", "{F} ¿Qué movimiento hace Nora al proponer controles ciudadanos?", "Sintetizar", "Objetar", "Etiquetar", "Propone una idea que recoge el temor de Pablo y su mínimo."),
        ("abc", "{F} ¿Cuál fue la tesis de Nora al comenzar?", "El Estado debe asegurar un mínimo de servicios básicos para todos", "El Estado debe ser gigante", "El Estado no es necesario", "Es lo que dice en su primera intervención."),
        ("abc", "{F} ¿Cuál fue la razón de Nora para su tesis?", "Que nadie elige dónde nace", "Que el Estado es grande", "Que los controles son necesarios", "Es la razón que da en su primera intervención."),
        ("abc", "Un participante ficticio interrumpe y dice: «Eso ya lo dijiste, pasemos de tema». ¿Qué error comete?", "Cambia de tema sin responder a la idea", "Sintetiza", "Concede", "Cambiar de tema evita examinar la razón que ya se había planteado."),
        ("abc", "{F} Un estudiante dice: «Pablo ganó porque habló último». ¿Qué falla tiene?", "Confunde el diálogo con un debate para ganar", "Evalúa con razones", "Cita una concesión", "En un diálogo filosófico se evalúan las razones."),
        ("abc", "{F} Si Nora respondiera a Pablo «Y tú quieres un Estado inexistente», ¿qué error cometería?", "Etiquetaría a Pablo en vez de devolver el diálogo a la idea", "Sintetizaría las dos posturas", "Concedería lo cierto de su temor", "Responder a una etiqueta con otra ataca a la persona y no examina la idea."),
        ("abc", "{F} Si Pablo acepta incluir controles ciudadanos, pero pide límites a las funciones del Estado, ¿qué movimiento hace?", "Concede una parte y objeta otra", "Etiqueta a Nora", "Cambia de tema", "Recoge parte de la propuesta de Nora y mantiene una exigencia."),
        ("abc", "Alguien participa mucho, pero solo repite su tesis. ¿Cómo se evalúa su participación?", "Es activa en tiempo, pero no aporta razones nuevas", "Es muy buena porque habla más", "No participa", "Participar activamente es aportar razones y escuchar."),
        ("abc", "{F} ¿Cuál sería un buen cierre del diálogo?", "Resumir qué acuerdos hubo, qué diferencias quedan y qué pregunta sigue abierta", "Declarar un ganador", "Eliminar las diferencias", "Resumir acuerdos y diferencias muestra qué se avanzó y qué sigue abierto."),
    ],
    ctx=("abc", "Un centro de estudiantes ficticio discute si debe haber un delegado que decida solo el uso de la sala de reuniones o si debe consultarse a todo el curso. Un estudiante dice: «Quien quiere consultar todo no entiende cómo se decide». ¿Qué intervención devolvería el diálogo a la idea?", "¿Qué decisiones crees que se pueden tomar sin consultar, y por qué?", "Eso lo dices porque eres desordenado", "No hablemos más de esto", "Pide una aclaración con razones, lo que devuelve el diálogo a la idea."),
    sc=[
        ("En Filosofía política: ¿qué significa sintetizar?", "Proponer una idea que recoja lo valioso de dos posturas", "Es uno de los movimientos del diálogo que describe la explicación."),
        ("Nombra los cuatro movimientos del diálogo.", "Aclarar, objetar, conceder y sintetizar", "Son los cuatro movimientos que describe la explicación de la clase."),
        ("¿Qué se hace cuando alguien etiqueta a una persona?", "Se devuelve el diálogo a la idea con una pregunta tranquila", "Así se evita la descalificación y se vuelve a examinar la idea."),
    ],
    op=("Escribe el guion de un diálogo ficticio de seis intervenciones entre dos estudiantes sobre una de estas preguntas: (1) ¿Debe el Estado asegurar un mínimo de servicios para todas las personas? (2) ¿Pueden las organizaciones ciudadanas reemplazar funciones del Estado? "
        "Incluye al menos una aclaración, una objeción, una concesión y una síntesis. Después marca cada uno de esos movimientos.",
        "Pregunta 2. A: Creo que sí; ¿qué entiendes por reemplazar? (aclaración) B: Que cumplan funciones como seguridad. A: Pero podrían no alcanzar a todos (objeción). B: Es cierto (concesión); quizá algunas funciones podrían compartirse entre Estado y organizaciones (síntesis).",
        ["incluye los cuatro movimientos", "ninguna intervención ataca a la persona", "las intervenciones se responden entre sí", "marca los movimientos"],
        ["guion de seis intervenciones con movimientos marcados"],
        ["etiquetar personas", "cambiar de tema", "no incluir una concesión"],
        "Pregunta: «¿dónde está la síntesis y qué recoge de cada postura?». Pídele que la indique."),
    reinforce="Elige una conversación reciente y marca en ella un momento de aclaración, de objeción o de concesión.",
    extend="Escribe una versión alternativa del cierre del diálogo con otra síntesis y compara cuál recoge mejor las razones de ambas partes.",
)
