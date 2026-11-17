"""Interpretación musical 3.º y 4.º medio HC: OAC-05 (argumentar juicios críticos sobre obras y manifestaciones musicales a partir de análisis estéticos y apreciaciones personales). Obras inventadas y descritas en texto."""
from __future__ import annotations

from hc_imus_common import build

O5 = "AR-IMUS-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (obra de ejemplo «Marea de tarde», inventada: canción para voz, guitarra y cajón, a 80 pulsos por minuto). "
     "Forma: estrofa, estribillo, estrofa, estribillo y final. Las estrofas van en p y los estribillos en mf. El estribillo, de 4 compases de 4 pulsos, sube a una nota aguda y se repite 3 veces dentro de cada aparición. "
     "El final se detiene sobre un acorde largo. Función: acompañar una tarde tranquila en una plaza. "
     "Enunciados de ejemplo: (1) «La canción tiene dos estribillos y un final largo». (2) «El estribillo sube a una nota aguda, lo que da sensación de apertura». "
     "(3) «Es una canción lograda, porque las estrofas suaves preparan un estribillo que abre el ánimo». (4) «Es la mejor canción del mundo». (5) «A mí me gusta».")
build(
    O5, 1, F,
    use="Aprenderé a distinguir una descripción, una interpretación, un juicio crítico y una apreciación personal sobre una obra, y a reconocer las tres partes de un juicio bien argumentado.",
    prior=["Sé describir elementos de una obra con evidencia.", "Sé relacionar un elemento con un efecto.", "Sé que una opinión necesita datos."],
    explain=[
        "Hablar de una obra musical puede hacerse de cuatro maneras. La descripción dice qué hay en la obra (por ejemplo, «tiene dos estribillos»). La interpretación explica qué produce un elemento (por ejemplo, «el estribillo sube y da sensación de apertura»). La apreciación personal dice lo que yo siento o me gusta («a mí me gusta»), y no necesita justificarse. El juicio crítico valora la obra (lograda o no lograda) y sí necesita una justificación.",
        "Un juicio crítico bien argumentado tiene tres partes. La afirmación es lo que se sostiene («es una obra lograda para su propósito»). La evidencia es el dato de la obra que la respalda («las estrofas van en p y los estribillos en mf»). La razón explica por qué esa evidencia apoya la afirmación («porque la subida de fuerza prepara la apertura del estribillo»). Sin evidencia y sin razón, una frase como «es la mejor del mundo» es solo una exageración.",
        "Para reconocer cada tipo se hacen preguntas simples. ¿Se puede comprobar con la obra? Entonces es descripción. ¿Explica qué produce un elemento? Entonces es interpretación. ¿Dice cómo me siento? Entonces es apreciación personal. ¿Valora con datos y razones? Entonces es un juicio crítico. Todo esto se practica con textos breves y obras inventadas, sin necesidad de escuchar música.",
    ],
    vocab=[("descripción", "enunciado que dice qué hay en la obra"), ("interpretación", "explicación de lo que produce un elemento de la obra"), ("apreciación personal", "lo que una persona siente o le gusta, sin necesidad de justificarlo"),
           ("juicio crítico", "valoración de una obra apoyada en evidencia y razones"), ("evidencia", "dato de la obra que respalda lo que se afirma"), ("razón", "explicación de por qué la evidencia apoya la afirmación")],
    worked=[
        ("Clasificar un enunciado", "Un enunciado de ejemplo dice: «la melodía baja al final y el volumen también, lo que produce sensación de calma». ¿Es descripción, interpretación, apreciación o juicio?",
         ["Dice qué hay (melodía y volumen que bajan) y explica lo que produce (calma).", "Explica el efecto de elementos: es una interpretación."],
         "Interpretación"),
        ("Armar un juicio", "Se quiere argumentar que una pieza de ejemplo cumple su propósito de dar energía. Datos: 140 pulsos por minuto y un ritmo repetido. Escribe afirmación, evidencia y razón.",
         ["Afirmación: la pieza cumple su propósito de dar energía. Evidencia: va a 140 pulsos por minuto y repite el ritmo.", "Razón: un pulso rápido y un patrón repetido dan sensación de impulso."],
         "Afirmación: da energía; evidencia: 140 pulsos y ritmo repetido; razón: dan sensación de impulso"),
    ],
    mistakes=[("Creer que «me gusta» es un juicio crítico.", "Es una apreciación personal, que no necesita justificarse pero tampoco justifica un juicio.", "Si quieres valorar la obra, agrega evidencia y razón."),
              ("Dar evidencia sin explicar por qué apoya la afirmación.", "Falta la razón que une el dato con lo que se afirma.", "Agrega «porque…» y explica la relación.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una apreciación personal?', 'Lo que una persona siente o le gusta, sin necesidad de justificarlo', 'Una valoración de la obra apoyada en datos, razones y comparaciones', 'Una lista de los elementos musicales que se pueden comprobar en ella', 'La apreciación personal expresa gusto o sensación; el juicio crítico y la descripción son otra cosa.'),
        ('abc', '{F} ¿Qué tipo de enunciado es el (1)?', 'Una descripción, porque dice qué hay en la obra', 'Una interpretación, porque explica qué produce cada elemento del estribillo', 'Una apreciación personal, porque dice lo que alguien siente al escucharla', 'El enunciado (1) nombra estribillos y un final largo, datos de la obra.'),
        ('abc', '{F} ¿Qué tipo de enunciado es el (5), «a mí me gusta»?', 'Una apreciación personal, porque expresa gusto sin justificar', 'Un juicio crítico, porque valora la obra con datos y razones', 'Una descripción, porque dice qué elementos hay en la obra', 'El enunciado (5) expresa gusto y no cita ningún dato de la obra.'),
        ('abc', '{F} ¿Qué tipo de enunciado es el (2)?', 'Una interpretación, porque explica el efecto de un elemento', 'Una descripción, porque cuenta cuántos estribillos hay en total', 'Un juicio crítico, porque dice que la obra es lograda', 'El enunciado (2) relaciona la nota aguda con una sensación de apertura.'),
        ('abc', '{F} ¿Cuál es la evidencia del enunciado (3)?', 'Las estrofas suaves que preparan el estribillo', 'La afirmación de que la canción es lograda en general y en todo sentido', 'La opinión de que la canción es la mejor del mundo entero', 'La evidencia es un dato de la obra: las estrofas van en p y preparan el estribillo.'),
        ('=', '{F} El estribillo dura 4 compases de 4 pulsos y se repite 3 veces. ¿Cuántos segundos dura cada aparición a 80 pulsos por minuto?', '3*4*4*60//80', 'Cada aparición tiene 3 repeticiones de 16 pulsos, que se pasan a segundos con el tempo.', ' s'),
        ('abc', '{F} ¿Por qué el enunciado (4), «es la mejor canción del mundo», no es un juicio bien argumentado?', 'Porque no tiene evidencia ni razón que lo respalden', 'Porque es demasiado corto para ser una descripción de la obra', 'Porque habla de una canción que no existe en el mundo', 'Un juicio argumentado necesita evidencia y razón; el (4) solo exagera.'),
        ('{F} Escribe un juicio con afirmación, evidencia y razón sobre el estribillo de «Marea de tarde» y sus cambios de fuerza.', 'Afirmación: el estribillo está bien resuelto. Evidencia: sube a una nota aguda y va en mf, después de estrofas en p. Razón: el cambio de altura y de fuerza marca un momento de apertura', 'Un juicio lleva afirmación, un dato de la obra y una razón que los une.'),
        ('=', '{F} Si el final largo dura 8 pulsos a 80 pulsos por minuto, ¿cuántos segundos dura el acorde final?', '8*60//80', 'Se multiplican los pulsos por 60 y se divide por los pulsos por minuto.', ' s'),
        ('abc', 'Un estudiante dice «el estribillo es lindo porque sí». ¿Qué le falta para que sea un juicio crítico?', 'Una evidencia de la obra y una razón que la una a lo que afirma', 'Más adjetivos que expresen cuánto le gustó el estribillo a quien opina', 'Una comparación con la canción que más le gusta a quien opina', 'Sin evidencia y razón, la frase sigue siendo una apreciación personal.'),
        ('abc', '{F} ¿Qué enunciado de la ficha es un juicio crítico bien argumentado?', 'El (3), porque tiene afirmación, evidencia y razón', 'El (4), porque valora la obra con mucha firmeza', 'El (1), porque nombra datos comprobables de la obra', 'El (3) valora la obra y explica por qué con datos.'),
        ('abc', '{F} Una estudiante dice que «(2) y (3) son lo mismo». ¿Qué observación es correcta?', 'No: el (2) explica un efecto y el (3) valora la obra', 'Sí, porque los dos explican lo que produce un elemento de la canción', 'Sí, porque los dos son apreciaciones personales sin datos de la obra', 'La interpretación explica un efecto; el juicio valora la obra, con evidencia y razón.'),
        ('=', '{F} La canción tiene dos apariciones del estribillo y cada una repite 3 veces el estribillo de 4 compases. ¿Cuántos compases de estribillo suenan en toda la canción?', '2*3*4', 'Se multiplican las apariciones por las repeticiones y por los 4 compases del estribillo.', ' compases'),
    ],
    ctx=('abc', 'Tu docente te pide escribir una crítica de una pieza inventada y tú anotas «me encantó». ¿Qué debes agregar para que sea un juicio crítico?', 'Una afirmación, una evidencia y una razón', 'Más frases sobre cuánto te emocionó la música que escuchaste', 'El nombre de otra pieza que también te encantó mucho', 'Un juicio se construye con afirmación, evidencia y razón; el gusto solo es el punto de partida.'),
    sc=[
        ("En Interpretación musical: ¿qué es un juicio crítico?", "Una valoración de la obra apoyada en evidencia y razones", "El juicio crítico se justifica con datos de la obra."),
        ('abc', 'La evidencia de un juicio es:', 'Un dato de la obra que lo respalda', 'La emoción que sintió quien opina', 'La cantidad de personas que lo comparten', 'La evidencia viene de la obra y se puede comprobar.'),
        ("¿Para qué sirve la razón en un juicio argumentado?", "Para explicar por qué la evidencia apoya la afirmación", "Sin razón, el dato y la afirmación quedan sin conexión."),
    ],
    op=("Con la {F}, escribe un juicio crítico de «Marea de tarde» con afirmación, evidencia y razón. Después escribe una apreciación personal y marca la diferencia entre ambos.",
        "Juicio: la canción es adecuada para una tarde tranquila (afirmación), porque las estrofas van en p y el tempo es de 80 pulsos por minuto (evidencia); esa fuerza baja y ese pulso pausado dan calma (razón). Apreciación personal: me gusta cómo suena el estribillo. La diferencia: el juicio se apoya en datos de la obra y la apreciación solo dice lo que yo siento.",
        ["escribe afirmación, evidencia y razón", "cita un dato verdadero de la ficha", "escribe una apreciación personal distinta", "explica la diferencia"],
        ["hoja con el juicio, la apreciación y la explicación"],
        ["citar un dato que no está en la ficha", "olvidar la razón", "mezclar apreciación y juicio"],
        "Pregunta: «¿qué dato de la obra respalda tu afirmación?». Si no lo cita, pídele que lo busque en la ficha."),
    reinforce="Escribe cuatro enunciados sobre una pieza inventada: una descripción, una interpretación, una apreciación y un juicio con evidencia y razón.",
    extend="Explica por qué una apreciación personal es válida aunque no tenga evidencia, pero no basta como crítica.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (obra de ejemplo «Cuarto de lluvia», inventada, para flauta y guitarra, a 60 pulsos por minuto). "
     "Propósito: dar calma en una sala de espera. Dinámica entre p y mf. Un solo tema de 8 compases de 4 pulsos que se repite 4 veces, y en cada repetición cambia la segunda frase. "
     "Duración total: 128 segundos. En la grabación de ejemplo, la flauta se desafina durante un pasaje de 8 segundos; la guitarra mantiene un pulso estable. "
     "Criterios de ejemplo: (1) coherencia con el propósito; (2) cuidado de la ejecución; (3) variedad dentro de la unidad, es decir, que haya cambios sin perder la idea; (4) adecuación al lugar donde se escucha.")
build(
    O5, 2, F,
    use="Aprenderé a elegir criterios para valorar una obra (coherencia con el propósito, cuidado de la ejecución, variedad y adecuación al contexto) y a aplicarlos con evidencia.",
    prior=["Distingo descripción, interpretación, apreciación y juicio.", "Sé armar un juicio con afirmación, evidencia y razón.", "Sé describir elementos de una obra."],
    explain=[
        "Un criterio es un aspecto desde el cual se valora una obra. Sin criterio, «es buena» o «es mala» no dice nada; con criterio, el juicio dice desde dónde se valora: «es coherente con su propósito», «tiene una ejecución cuidada». Cuatro criterios frecuentes son: la coherencia con el propósito (si los elementos ayudan a lograr lo que la obra quiere), el cuidado de la ejecución (afinación, pulso, claridad), la variedad dentro de la unidad (cambios que no hacen perder la idea) y la adecuación al lugar donde se escucha.",
        "Cada criterio se aplica con evidencia. Para el primero se compara el propósito con los elementos (tempo, dinámica); para el segundo se buscan datos de la ejecución (afinación, pulso); para el tercero se mira cuántas cosas cambian y cuántas se conservan; para el cuarto se piensa en el lugar y el público. Una obra puede cumplir un criterio y fallar otro, y un buen juicio dice cuáles cumple y cuáles no.",
        "Elegir criterios también es una decisión. Si el propósito es calmar, el criterio de coherencia pesa más que el de sorpresa. Un criterio no se elige para que el resultado salga bonito, sino porque corresponde a lo que la obra se propone. Por último, los criterios se aplican a la obra y no a las personas que la hacen: se dice «el pasaje de 8 segundos está desafinado» y no «quien toca es mala».",
    ],
    vocab=[("criterio", "aspecto desde el cual se valora una obra"), ("coherencia", "acuerdo entre los elementos de la obra y su propósito"), ("ejecución", "manera de tocar o cantar la obra, con afinación y pulso"),
           ("variedad dentro de la unidad", "cambios que no hacen perder la idea principal"), ("adecuación", "ajuste de la obra al lugar y al público"), ("desafinar", "sonar más agudo o más grave que la altura que corresponde")],
    worked=[
        ("Aplicar un criterio", "Una pieza de ejemplo busca dar energía y va a 50 pulsos por minuto, en p. ¿Cumple el criterio de coherencia con el propósito?",
         ["El propósito es dar energía; se esperan un pulso rápido y una fuerza media o alta.", "Un pulso de 50 y la dinámica p apuntan a calma: no es coherente."],
         "No cumple: sus elementos apuntan a calma, no a energía"),
        ("Separar obra y persona", "Un comentario dice: «el pasaje desafinado muestra que la flautista es mala». ¿Qué se corrige?",
         ["El criterio se aplica a la ejecución de la obra, no a la persona.", "Se reemplaza por «el pasaje de 8 segundos está desafinado»."],
         "«El pasaje de 8 segundos está desafinado»"),
    ],
    mistakes=[("Valorar con «es buena» o «es mala» sin nombrar el criterio.", "No dice desde dónde se valora.", "Nombra el criterio y cita la evidencia de la obra."),
              ("Aplicar el criterio a la persona y no a la ejecución.", "Se descalifica a quien toca en lugar de analizar lo que se oye.", "Habla de lo que se oye y de la obra.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es un criterio de valoración?', 'Un aspecto desde el cual se valora una obra', 'Una nota de la obra que se repite cada cierto tiempo', 'Una lista de las personas que participaron en su ejecución', 'Un criterio dice desde dónde se valora; no es una nota ni una lista de personas.'),
        ('abc', '{F} ¿Cuál es el propósito de «Cuarto de lluvia»?', 'Dar calma en una sala de espera', 'Dar energía a un grupo de personas antes de una carrera escolar', 'Acompañar una celebración con baile en una plaza grande', 'La ficha dice que la obra busca dar calma en una sala de espera.'),
        ('abc', '{F} ¿Qué dato de la ficha sirve como evidencia del criterio (2), cuidado de la ejecución?', 'La flauta se desafina durante un pasaje de 8 segundos', 'La obra tiene un tema de 8 compases que se repite 4 veces', 'La obra está escrita para flauta y guitarra a 60 pulsos', 'La desafinación es un dato de ejecución, que es lo que mide el criterio (2).'),
        ('abc', '{F} ¿Cumple el criterio (1), coherencia con el propósito?', 'Sí: el tempo de 60 y la dinámica p a mf apoyan la calma', 'No: el tempo de 60 es demasiado lento para una pieza de calma', 'No se puede saber, porque la ficha no menciona el propósito', 'Un pulso lento y una fuerza baja a media apoyan el propósito de calma.'),
        ('=', '{F} La flauta se desafina durante 8 segundos de un total de 128. ¿Cuántos segundos de la obra suenan sin esa desafinación?', '128-8', 'Se restan los segundos del pasaje desafinado al total de la obra.', ' s'),
        ('abc', '{F} ¿Qué criterio evalúa que el tema cambie la segunda frase en cada repetición?', 'La variedad dentro de la unidad', 'La adecuación al lugar de escucha', 'El cuidado de la ejecución de la flauta', 'Cambiar una parte y conservar el tema es variedad dentro de la unidad.'),
        ('abc', '{F} ¿Qué dato apoya el criterio (4), adecuación al lugar?', 'La dinámica entre p y mf encaja con una sala de espera', 'La guitarra mantiene un pulso estable durante la obra', 'El tema se repite 4 veces con cambios en la segunda frase', 'Una fuerza suave y media encaja con un espacio donde las personas esperan.'),
        ('=', '{F} El tema dura 8 compases de 4 pulsos a 60 pulsos por minuto. ¿Cuántos segundos dura cada vez que se toca el tema?', '8*4*60//60', 'Se multiplican los compases por los pulsos y se pasa a segundos con el tempo.', ' s'),
        ('abc', '{F} Un estudiante escribe: «la flautista es mala porque se desafina». ¿Cuál es la mejor corrección?', 'El pasaje de 8 segundos de la flauta está desafinado', 'La flautista debería practicar más para el próximo acto', 'La flauta es un instrumento difícil y por eso se desafina', 'El criterio se aplica a lo que se oye, no a quien toca.'),
        ('abc', '{F} Una estudiante dice que la obra «no tiene variedad porque repite el tema 4 veces». ¿Qué observación es correcta?', 'La segunda frase cambia en cada repetición, así que hay variedad', 'Repetir un tema siempre elimina cualquier variedad en una obra musical', 'Una obra con un tema único no puede evaluarse por su variedad interna', 'La ficha dice que cambia la segunda frase en cada repetición, lo que da variedad.'),
        ('abc', '{F} Un grupo quiere un juicio sobre la obra para una sala de espera. ¿Qué criterio pesa más?', 'La coherencia con el propósito de dar calma', 'La sorpresa constante de cada nueva repetición', 'La velocidad de los cambios entre una frase y otra', 'El propósito de calma hace que la coherencia sea el criterio más importante.'),
        ('abc', '{F} ¿Qué juicio usa dos criterios con evidencia?', 'Cumple la coherencia por su tempo y falla el cuidado por el pasaje desafinado', 'Es una obra buena porque a casi todas las personas del curso les gustó mucho', 'Cumple el propósito porque su título habla de lluvia y de calma en la sala', 'Un juicio con criterios cita dos criterios y una evidencia de la ficha para cada uno.'),
        ('=', '{F} Si cada vez que se toca el tema dura 8 compases de 4 pulsos a 60 pulsos por minuto, ¿cuántos segundos duran las repeticiones 3 y 4?', '2*8*4*60//60', 'Se multiplican las dos repeticiones por los 8 compases y los 4 pulsos, y se pasa a segundos con el tempo.', ' s'),
    ],
    ctx=('abc', 'Debes valorar la presentación de un grupo de tu curso. ¿Qué paso evita descalificar a las personas?', 'Aplicar criterios a lo que se oye y citar evidencia', 'Decir si te cae bien o mal el grupo antes de escucharlo tocar', 'Comparar al grupo con otro curso sin ningún dato concreto', 'Los criterios se aplican a la ejecución y no a las personas.'),
    sc=[
        ("En Interpretación musical: ¿qué es la coherencia con el propósito?", "El acuerdo entre los elementos de la obra y lo que ella busca", "Si los elementos ayudan al propósito, la obra es coherente."),
        ('abc', 'Un criterio se aplica:', 'A la obra y a su ejecución', 'A la persona que toca', 'Al gusto de quien escucha', 'Un criterio valora lo que se oye, no a quien toca.'),
        ("¿Por qué una obra puede cumplir un criterio y fallar otro?", "Porque cada criterio mira un aspecto distinto de la obra", "Un buen juicio dice cuáles cumple y cuáles no."),
    ],
    op=("Con la {F}, escribe un juicio de tres frases sobre «Cuarto de lluvia»: aplica dos criterios, cita una evidencia de la ficha para cada uno y di si la obra los cumple. Cuida que el juicio se refiera a la obra y no a las personas.",
        "Criterio 1, coherencia con el propósito: cumple, porque va a 60 pulsos por minuto y entre p y mf, lo que apoya la calma. Criterio 2, cuidado de la ejecución: falla en parte, porque la flauta se desafina durante un pasaje de 8 segundos. Conclusión: es una obra coherente con su propósito, con un pasaje de ejecución por mejorar.",
        ["aplica dos criterios", "cita una evidencia de la ficha para cada uno", "dice si cumple cada criterio", "habla de la obra y no de las personas"],
        ["hoja con el juicio de tres frases"],
        ["no citar evidencia", "juzgar a la persona", "usar solo un criterio"],
        "Pregunta: «¿qué criterio aplicas en esa frase?». Si no lo nombra, pídele que lo escriba."),
    reinforce="Elige dos criterios y escribe una frase que los aplique a una pieza inventada con una evidencia para cada uno.",
    extend="Explica por qué el criterio de sorpresa pesa menos que el de coherencia en una pieza pensada para dar calma.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (juicios de ejemplo sobre «Cuarto de lluvia», inventados: flauta y guitarra, 60 pulsos por minuto, entre p y mf, un tema de 8 compases que se repite 4 veces con cambios en la segunda frase; propósito: dar calma en una sala de espera). "
     "Juicio A: «Es lograda para su propósito, porque el tempo de 60 y la dinámica entre p y mf dan calma, y los cambios de la segunda frase evitan el aburrimiento». "
     "Juicio B: «Es lograda, porque a mí me da sueño». "
     "Juicio C: «No es lograda, porque no tiene batería». "
     "Nueva evidencia: en la sala de espera real hay ruido de calle fuerte que tapa los pasajes en p.")
build(
    O5, 3, F,
    use="Aprenderé a ensayar un juicio crítico: comparar varias versiones, elegir la mejor argumentada con dos evidencias y revisarla cuando aparece una evidencia nueva.",
    prior=["Sé armar un juicio con afirmación, evidencia y razón.", "Sé aplicar criterios con evidencia.", "Sé que revisar una decisión es parte de analizar."],
    explain=[
        "Argumentar es dar razones para que otra persona pueda revisar y compartir un juicio. Un buen argumento cumple tres condiciones: la evidencia es verdadera (está en la obra), es pertinente (tiene que ver con el criterio) y la razón la une a la afirmación. Un argumento débil puede fallar en cualquiera de ellas: puede citar algo que no está en la obra, citar algo que no tiene que ver con lo que se afirma, o dejar sin explicar la relación.",
        "Cuando hay varias versiones de un juicio, se comparan con una lista de preguntas. ¿Cita evidencia de la obra? ¿La evidencia es pertinente al criterio? ¿Explica la razón? ¿Se apoya en el propósito de la obra y no en el gusto o en un detalle que la obra no se propone tener? El juicio que responde que sí a más preguntas es el mejor argumentado. Una apreciación personal puede ser sincera, pero no basta como argumento.",
        "Un juicio también se revisa si cambia la información. Si aparece una evidencia nueva, se pregunta si debilita o fortalece la afirmación y se ajusta la conclusión. Revisar no es dar vuelta atrás: es mantener el juicio honesto con la información disponible. En este cuaderno todo se trabaja con fichas y casos inventados, sin necesidad de escuchar música.",
    ],
    vocab=[("argumento", "afirmación con evidencia y razón"), ("pertinente", "que tiene relación directa con lo que se afirma"), ("evidencia nueva", "dato que aparece después de formular un juicio"),
           ("debilitar", "restar fuerza a una afirmación"), ("fortalecer", "dar más fuerza a una afirmación"), ("comparar", "revisar varias versiones con las mismas preguntas")],
    worked=[
        ("Evaluar una evidencia", "Un juicio de ejemplo dice: «la pieza cumple su propósito de dar calma porque tiene muchos instrumentos». ¿La evidencia es pertinente?",
         ["El propósito es la calma; la cantidad de instrumentos no tiene relación directa con la calma.", "La evidencia no es pertinente al criterio de coherencia con el propósito."],
         "No es pertinente"),
        ("Revisar con una evidencia nueva", "Un juicio dice que una pieza en p es adecuada para una plaza. Aparece el dato de que la plaza tiene mucho ruido. ¿Qué pasa con el juicio?",
         ["El ruido puede tapar los pasajes suaves.", "El juicio se debilita: hay que ajustar la conclusión."],
         "Se debilita y se ajusta la conclusión"),
    ],
    mistakes=[("Citar un dato que no está en la obra para reforzar el juicio.", "La evidencia debe ser verdadera y comprobable.", "Cita solo datos de la obra o de la ficha."),
              ("Mantener el juicio igual cuando aparece una evidencia nueva importante.", "Se olvida revisar con la nueva información.", "Pregunta si la evidencia nueva debilita o fortalece la afirmación.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es un argumento?', 'Una afirmación con evidencia y razón', 'Una opinión que se repite con más fuerza', 'Una lista de datos sin una afirmación', 'Un argumento une afirmación, evidencia y razón; no es solo una opinión repetida.'),
        ('abc', '{F} ¿Qué juicio cita evidencia de la obra?', 'El juicio A, que menciona el tempo de 60 y la dinámica', 'El juicio B, que menciona el sueño que le da a quien lo dice', 'El juicio C, que menciona la falta de una batería', 'Solo A cita datos de la obra, como el tempo y la dinámica.'),
        ('abc', '{F} ¿Por qué el juicio C no es pertinente?', 'La obra no se propone tener batería para lograr la calma', 'La batería es un instrumento que no puede sonar en p nunca', 'La ficha dice que la obra debería tener más instrumentos en total', 'La evidencia de C no tiene relación con el propósito de la obra.'),
        ('abc', '{F} ¿Qué tipo de enunciado es el juicio B?', 'Una apreciación personal con forma de juicio', 'Un juicio con evidencia de la obra y razón', 'Una descripción de elementos que se pueden comprobar', 'B parte de lo que siente quien opina, sin datos de la obra.'),
        ('=', '{F} El tema dura 8 compases de 4 pulsos a 60 pulsos por minuto y se repite 4 veces. ¿Cuántos segundos dura todo?', '4*8*4*60//60', 'Se multiplican las repeticiones por los compases y los pulsos, y se pasa a segundos.', ' s'),
        ('abc', '{F} ¿Qué juicio está mejor argumentado?', 'El A, que tiene evidencia pertinente y razón', 'El B, que es sincero sobre lo que siente quien opina de la obra', 'El C, que es firme al decir que no es lograda la obra', 'A cumple las tres condiciones; B y C fallan en evidencia o pertinencia.'),
        ('abc', '{F} ¿Cuál es la razón del juicio A?', 'Que el tempo y la dinámica dan calma y hay variedad', 'Que la obra está escrita para dos instrumentos nada más que flauta y guitarra', 'Que la obra dura menos de dos minutos de principio a fin de la grabación', 'La razón explica por qué los datos apoyan la afirmación de que es lograda.'),
        ('=', '{F} En cada repetición del tema, la segunda frase (de 4 compases) cambia. ¿Cuántos compases del tema de 8 compases se conservan iguales en cada repetición?', '8-4', 'Se restan los compases que cambian a los compases totales del tema.', ' compases'),
        ('abc', '{F} La nueva evidencia dice que hay ruido de calle fuerte que tapa los pasajes en p. ¿Qué efecto tiene sobre el juicio A?', 'Lo debilita, porque los pasajes suaves ya no se oyen', 'Lo fortalece, porque el ruido ayuda a que la calma se note más en el lugar', 'No tiene efecto, porque el ruido no cambia la dinámica de la obra escrita', 'Si el ruido tapa los pasajes suaves, el efecto de calma se pierde y el juicio se debilita.'),
        ('abc', '{F} Con la nueva evidencia, ¿qué revisión del juicio A es honesta?', 'Mantener que es coherente y agregar que ahí no se oye bien', 'Eliminar el juicio y escribir que la obra es mala en todos los casos y lugares', 'Dejar el juicio igual y no mencionar el ruido de la calle en ningún momento', 'Se mantiene lo verdadero (coherencia) y se agrega el límite que impone el lugar.'),
        ('abc', '{F} Un grupo propone cambiar la ejecución a mf para que se oiga sobre el ruido. ¿Qué observación es correcta?', 'Ayuda a oírla, pero puede cambiar el propósito', 'No tiene ningún efecto sobre el propósito de la obra en la sala', 'Soluciona todos los problemas del lugar y mejora la coherencia', 'Subir la fuerza resuelve la audición, pero afecta el propósito de calma.'),
        ('abc', 'Dos estudiantes discuten un juicio. Una dice «mi juicio es verdadero porque lo dije yo»; el otro dice «mi juicio es verdadero porque cita un dato de la obra». ¿Quién argumenta mejor?', 'El segundo, porque su razón se puede comprobar', 'La primera, porque el juicio es suyo y nadie puede cuestionarlo', 'Ninguno, porque en música no se puede argumentar', 'Un argumento se sostiene en datos que otra persona puede comprobar.'),
        ('=', '{F} Si la mitad de la duración total de 128 segundos está en p y el ruido tapa esos pasajes, ¿cuántos segundos de la obra siguen audibles?', '128//2', 'Se divide la duración total en dos partes iguales y se cuenta la parte audible.', ' s'),
    ],
    ctx=('abc', 'Tu compañero escribe una crítica de un concierto y afirma «la guitarrista fue genial», sin ningún dato. ¿Cómo le ayudas a mejorar su argumento?', 'Pidiéndole un dato de la ejecución y una razón', 'Diciéndole que es mejor no opinar si no se tiene experiencia previa', 'Cambiando «genial» por otro adjetivo igual de general que ese', 'Un argumento mejora con un dato y una razón, no con un adjetivo distinto.'),
    sc=[
        ("En Interpretación musical: ¿qué es una evidencia pertinente?", "Un dato que tiene relación directa con lo que se afirma", "La pertinencia une el dato con el criterio."),
        ('abc', 'Si aparece una evidencia nueva importante, el juicio:', 'Se revisa y se ajusta si hace falta', 'Se mantiene igual siempre', 'Se elimina sin explicación', 'Revisar con la información nueva mantiene el juicio honesto.'),
        ("¿Por qué una apreciación personal no basta como argumento?", "Porque no cita datos de la obra que otra persona pueda comprobar", "Un argumento necesita una evidencia que otros puedan verificar."),
    ],
    op=("Con la {F}, elige entre los juicios A, B y C el que esté mejor argumentado y justifica con dos evidencias. Luego escribe cómo cambia ese juicio con la nueva evidencia del ruido de calle.",
        "Elijo A: cita el tempo de 60 y la dinámica entre p y mf, que dan calma, y explica por qué (razón). B es una apreciación personal y C cita algo no pertinente. Con el ruido de calle, el juicio A se debilita porque los pasajes en p no se oyen; lo reviso: la obra es coherente con su propósito, pero en ese lugar necesita otra forma de presentarse.",
        ["elige el juicio mejor argumentado", "cita dos evidencias", "explica por qué descarta otro juicio", "revisa con la nueva evidencia"],
        ["hoja con el juicio elegido, dos evidencias y la revisión"],
        ["elegir por gusto", "no revisar con la nueva evidencia", "citar un dato que no está en la ficha"],
        "Pregunta: «¿qué dato de la ficha respalda ese juicio?». Si no lo hay, pídele que elija otro."),
    reinforce="Escribe dos versiones de un juicio sobre una pieza inventada, una bien argumentada y otra con una evidencia no pertinente, y explica la diferencia.",
    extend="Explica cómo cambiaría tu juicio si la misma pieza se presentara en una sala de conciertos silenciosa.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (críticas de ejemplo sobre «Ruedas del cerro», inventada: pieza para tambor y voz, a 120 pulsos por minuto, con un patrón de 4 pulsos que se repite durante 3 minutos y un volumen parejo y alto; propósito: motivar a quienes corren una carrera escolar). "
     "Crítica de Ema: «Cumple su propósito: el pulso de 120 y la repetición del patrón dan impulso para correr». "
     "Crítica de Hugo: «No cumple su propósito: el volumen parejo y alto, sin descansos, cansa a quien escucha durante 3 minutos». "
     "Comentario de Teo: «A mí me gusta más lo que ya conozco, así que prefiero la crítica de Ema». "
     "Comentario de Lía: «Esta pieza no puede ser buena porque viene de una zona que no conozco».")
build(
    O5, 4, F,
    use="Aprenderé a distinguir mi apreciación personal del análisis, a reconocer sesgos al juzgar una obra (familiaridad, moda, prejuicio sobre su procedencia) y a respetar críticas distintas si ambas tienen evidencia.",
    prior=["Sé argumentar un juicio con evidencia.", "Sé aplicar criterios.", "Sé revisar un juicio con evidencia nueva."],
    explain=[
        "Todas las personas tenemos gustos, y los gustos son válidos. Pero un juicio crítico no puede basarse solo en el gusto, porque el gusto cambia de persona a persona y no se puede comprobar. La apreciación personal se declara («a mí me gusta»); el análisis se apoya en datos. Un buen crítico puede decir «esta obra no es de mi gusto, pero cumple su propósito por estas razones».",
        "Un sesgo es una tendencia que nos hace juzgar con ligereza. El sesgo de familiaridad hace preferir lo que ya conocemos. El sesgo de moda hace creer que algo es mejor porque es popular o reciente. El prejuicio sobre la procedencia hace pensar que una obra es peor por venir de un lugar, una época o un grupo que no conocemos. Reconocer el sesgo no lo borra, pero ayuda a volver a los datos de la obra.",
        "Dos críticas distintas pueden ser ambas válidas si cada una cita evidencia verdadera y pertinente, aunque lleguen a conclusiones opuestas. Por ejemplo, una puede valorar el impulso y otra el cansancio. Respetar una crítica distinta significa leer su evidencia y responder con evidencia, no con descalificaciones. Quien se siente herido por un comentario puede pedir apoyo a una persona adulta de confianza.",
    ],
    vocab=[("sesgo", "tendencia que nos hace juzgar con ligereza"), ("familiaridad", "preferencia por lo que ya conocemos"), ("prejuicio", "juicio previo sin conocer la obra ni su contexto"),
           ("crítica válida", "crítica que cita evidencia verdadera y pertinente"), ("descalificar", "rechazar algo o a alguien sin argumentos"), ("respeto", "escuchar una crítica distinta y responder con evidencia")],
    worked=[
        ("Reconocer un sesgo", "Un comentario de ejemplo dice: «prefiero esta pieza porque suena como las que siempre escucho». ¿Qué sesgo muestra?",
         ["La razón es que suena como lo que ya conoce, no un dato de la pieza.", "Es un sesgo de familiaridad."],
         "Sesgo de familiaridad"),
        ("Revisar dos críticas", "Dos críticas de ejemplo sobre una pieza de 3 minutos: una valora el impulso del ritmo y otra dice que el volumen cansa. Ambas citan datos de la pieza. ¿Pueden ser válidas a la vez?",
         ["Cada una cita evidencia verdadera y pertinente de la pieza.", "Sí: ven aspectos distintos y llegan a conclusiones diferentes."],
         "Sí, ambas son válidas si su evidencia es verdadera"),
    ],
    mistakes=[("Rechazar una crítica porque «piensa distinto».", "Se confunde desacuerdo con error.", "Lee su evidencia y responde con tu propia evidencia."),
              ("Pensar que reconocer un sesgo lo elimina.", "Reconocerlo ayuda, pero hay que volver a los datos.", "Después de reconocer el sesgo, revisa la obra con la evidencia.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es un sesgo al juzgar una obra?', 'Una tendencia que nos hace juzgar con ligereza', 'Un error de la grabación que cambia el sonido de la obra escuchada', 'Una regla del programa que ordena las piezas por duración total', 'Un sesgo es una tendencia al juzgar; no es un error técnico ni una regla del programa.'),
        ('abc', '{F} ¿Qué sesgo muestra el comentario de Teo?', 'El sesgo de familiaridad, que prefiere lo que ya conoce', 'El sesgo de moda, que prefiere lo más popular y reciente', 'El prejuicio sobre la procedencia de la pieza', 'Teo prefiere lo que ya conoce, que es la familiaridad.'),
        ('abc', '{F} ¿Qué muestra el comentario de Lía?', 'Un prejuicio sobre la procedencia de la pieza', 'Un análisis con evidencia sobre el ritmo de la pieza', 'Una descripción de la forma de la pieza', 'Lía juzga la pieza por su lugar de origen sin conocerla.'),
        ('abc', '{F} ¿Qué evidencia cita la crítica de Hugo?', 'El volumen parejo y alto durante 3 minutos', 'El pulso de 120 y la repetición del patrón de 4 pulsos de la pieza', 'El hecho de que la pieza viene de una zona desconocida para ella', 'Hugo cita el volumen parejo y alto durante 3 minutos.'),
        ('=', '{F} El patrón de 4 pulsos dura 2 segundos a 120 pulsos por minuto. ¿Cuántas veces se repite en 3 minutos?', '3*60//2', 'Se pasan los 3 minutos a segundos y se divide por la duración del patrón.', ' veces'),
        ('abc', '{F} ¿Son válidas las críticas de Ema y Hugo a la vez?', 'Sí, porque cada una cita evidencia verdadera y pertinente', 'No, porque una de las dos tiene que estar equivocada', 'No, porque las dos hablan de un tema distinto del propósito', 'Ambas citan datos de la pieza y valoran aspectos distintos.'),
        ('abc', '{F} ¿Cómo debe responder Hugo a Ema, si no está de acuerdo?', 'Leyendo su evidencia y respondiendo con su propia evidencia', 'Diciéndole que su crítica no sirve porque piensa distinto', 'Aceptando su crítica sin revisarla para evitar discusiones', 'Respetar es responder con evidencia, no con descalificaciones ni con silencio.'),
        ('=', '{F} Hugo propone un descanso de 10 segundos después de cada 60 segundos de música. ¿Cuántos segundos de descanso suma en los 3 minutos de la pieza?', '180//60*10', 'Se cuentan los bloques de 60 segundos en 3 minutos y se multiplican por 10 segundos.', ' s'),
        ('abc', '{F} ¿Qué debería hacer Teo para convertir su comentario en un juicio crítico?', 'Citar un dato de la pieza que apoye la crítica de Ema', 'Decir que le gusta más porque conoce a Ema desde hace tiempo', 'Repetir que le gusta lo que ya conoce con más énfasis', 'Un juicio necesita evidencia de la pieza, no solo preferencia por lo conocido.'),
        ('abc', '{F} Lía quiere revisar su prejuicio. ¿Qué paso es el más adecuado?', 'Analizar los datos de la pieza antes de juzgarla', 'Pedirle a otra persona que juzgue por ella para no equivocarse', 'Elegir otra pieza que le sea más conocida y juzgarla en su lugar', 'Revisar el sesgo exige volver a los datos de la obra.'),
        ('abc', '{F} Una persona se siente herida por un comentario de otro estudiante sobre su crítica. ¿Qué decisión es la más adecuada?', 'Pedir apoyo a una persona adulta de confianza', 'Contestar con otro comentario hiriente para igualar la situación vivida', 'Dejar de opinar en clase para no tener problemas con nadie más', 'Ante un comentario que hiere, se pide apoyo a una persona adulta de confianza.'),
        ('abc', 'Un estudiante dice «mi juicio no tiene sesgos porque soy objetivo». ¿Qué observación es correcta?', 'Todas las personas tienen sesgos; lo útil es reconocerlos', 'Es cierto, porque una persona objetiva no puede equivocarse nunca más', 'Es falso, porque solo las personas poco informadas tienen sesgos al juzgar', 'Los sesgos son frecuentes; reconocerlos permite revisar con datos.'),
        ('=', '{F} Si en un curso de 30 estudiantes 12 prefieren la crítica de Ema y 10 la de Hugo, ¿cuántos no prefieren ninguna de las dos?', '30-12-10', 'Se restan los que prefieren cada crítica al total del curso.', ' estudiantes'),
    ],
    ctx=('abc', 'Escuchas una pieza de una tradición de otra región y tu primera reacción es «no me gusta, es rara». ¿Qué decisión respeta la pieza y tu opinión?', 'Declarar que no es de tu gusto y analizar sus elementos', 'Decir que la pieza es mala porque no te gusta a ti', 'Evitar opinar y no escribir nada sobre la pieza escuchada', 'La apreciación personal se declara y el análisis se apoya en datos de la obra.'),
    sc=[
        ("En Interpretación musical: ¿qué es el prejuicio sobre la procedencia?", "Juzgar una obra por su origen sin conocerla", "Se corrige analizando los datos de la obra."),
        ('abc', 'Dos críticas opuestas pueden ser válidas si:', 'Cada una cita evidencia verdadera y pertinente', 'Una de las dos es mucho más conocida que la otra', 'Ambas son exactamente iguales de largas en el texto', 'La validez depende de la evidencia y no de la conclusión.'),
        ("¿Qué haces si un comentario sobre tu crítica te hiere?", "Pido apoyo a una persona adulta de confianza", "Se cuida el trato respetuoso y se pide ayuda."),
    ],
    op=("Con la {F}, elige una de las críticas (Ema o Hugo) y escribe una respuesta respetuosa que cite una evidencia de la pieza. Luego escribe cuál de los comentarios de Teo o Lía muestra un sesgo, de qué tipo, y cómo lo revisarías con datos.",
        "Respuesta a Hugo: tu crítica es válida porque el volumen parejo y alto dura 3 minutos; yo agrego que el pulso de 120 y el patrón repetido dan impulso. Sesgo: el comentario de Lía muestra un prejuicio sobre la procedencia. Lo revisaría analizando los datos de la pieza (pulso de 120, patrón de 4 pulsos) antes de juzgar por su origen.",
        ["responde con una evidencia de la ficha", "no descalifica a la persona", "identifica el sesgo con su tipo", "dice cómo revisarlo con datos"],
        ["hoja con la respuesta, el sesgo y la revisión"],
        ["descalificar una crítica", "no nombrar el tipo de sesgo", "revisar sin datos"],
        "Pregunta: «¿qué dato de la pieza sustenta tu respuesta?». Si no lo cita, pídele que lo busque."),
    reinforce="Escribe tres ejemplos de sesgo (familiaridad, moda y procedencia) en frases sobre piezas inventadas y cómo revisarías cada uno.",
    extend="Explica por qué un crítico con mucha experiencia también puede tener sesgos y cómo evitarlos.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (borrador de crítica y pauta, de ejemplo, inventados) sobre «Marea de tarde»: canción para voz, guitarra y cajón, a 80 pulsos por minuto; estrofas en p y estribillos en mf; el estribillo sube a una nota aguda; función: acompañar una tarde tranquila en una plaza. "
     "Borrador de Sol: (1) «La canción me parece genial». (2) «Es adecuada para una tarde tranquila, porque las estrofas van en p y el tempo es de 80 pulsos por minuto, lo que da calma». "
     "(3) «El estribillo sube a una nota aguda, lo que da sensación de apertura». (4) «Quien la canta es muy mala». "
     "Pauta: A, afirmación clara; B, evidencia verdadera de la obra; C, razón que une evidencia y afirmación; D, mención del propósito o contexto; E, trato respetuoso, sin descalificar a las personas.")
build(
    O5, 5, F,
    use="Aprenderé a escribir y ajustar una crítica breve: estructurarla en cinco frases, revisarla con una pauta de cinco criterios y corregir una sola cosa por revisión, con respeto.",
    prior=["Sé argumentar un juicio con afirmación, evidencia y razón.", "Sé reconocer sesgos.", "Sé revisar un texto con una pauta."],
    explain=[
        "Una crítica breve se puede escribir en cinco frases. Primera, la afirmación: lo que se sostiene sobre la obra. Segunda y tercera, la evidencia de la obra, con datos verdaderos. Cuarta, la razón que explica por qué esos datos apoyan la afirmación, con mención del propósito o del contexto. Quinta, una conclusión o una sugerencia respetuosa. Si hay apreciación personal, se declara como tal y se separa del juicio.",
        "Para revisar un borrador se pasa una pauta. Cada criterio se marca como «cumple» o «falta» y se cita la frase que lo respalda. Una frase que descalifica a una persona («quien la canta es muy mala») no cumple el criterio de respeto y se reemplaza por una observación sobre la ejecución («el pasaje de la nota aguda se oyó inseguro»). Se hace un solo ajuste por revisión y se anota la razón.",
        "Registrar los ajustes permite aprender de ellos. Si un ajuste mejora el texto, se conserva; si no, se prueba otro. Una crítica terminada se puede compartir con el grupo evaluado, siempre con tono cuidadoso. Si alguien se siente herido por una crítica, se retira o se reformula y se pide orientación a una persona adulta de confianza.",
    ],
    vocab=[("borrador", "primera versión de un texto, que se revisa y mejora"), ("pauta", "lista de criterios para revisar una crítica"), ("conclusión", "frase final que cierra la crítica"),
           ("sugerencia", "cambio concreto y posible que se propone"), ("ajuste", "cambio de una sola cosa para cumplir un criterio"), ("respeto", "trato cuidadoso hacia las personas que hicieron la obra")],
    worked=[
        ("Marcar un criterio", "Un borrador de ejemplo dice: «Es adecuada para una plaza, porque va en p y a 80 pulsos por minuto, lo que da calma». ¿Cumple el criterio de razón?",
         ["Hay una afirmación (es adecuada) y datos (p y 80 pulsos).", "Explica con «lo que da calma» por qué los datos apoyan la afirmación: cumple."],
         "Cumple, porque tiene una razón"),
        ("Corregir una frase", "Una frase de ejemplo dice: «la cantante es pésima». ¿Cómo se corrige para cumplir el criterio de respeto?",
         ["Se quita la descalificación de la persona.", "Se describe lo que se oye: «el pasaje agudo del estribillo se oyó inseguro»."],
         "«El pasaje agudo del estribillo se oyó inseguro»"),
    ],
    mistakes=[("Corregir toda la crítica a la vez sin anotar qué cambió.", "No se sabe cuál ajuste cumplió cada criterio.", "Cambia una sola cosa por revisión y anótala."),
              ("Dejar una descalificación porque «es la verdad».", "Se confunde opinión con respeto.", "Describe lo que se oye y sugiere un cambio posible.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una conclusión en una crítica breve?', 'La frase final que cierra la crítica con una sugerencia', 'La primera frase de la crítica, que presenta la obra al lector', 'Una lista con los datos que la obra tiene en cada compás escrito', 'La conclusión cierra la crítica; no es la afirmación inicial ni una lista de datos.'),
        ('abc', '{F} ¿Qué frase del borrador cumple el criterio B, evidencia verdadera?', 'La frase 2, porque cita estrofas en p y el tempo de 80', 'La frase 1, porque dice que la canción le parece genial', 'La frase 4, porque dice que quien canta es muy mala', 'La frase 2 cita datos verdaderos de la ficha, que es la evidencia pedida.'),
        ('abc', '{F} ¿Qué frase incumple el criterio E, respeto?', 'La frase 4, que descalifica a quien canta', 'La frase 3, que dice que el estribillo da apertura', 'La frase 1, que dice que la canción le parece genial', 'La frase 4 ataca a una persona en lugar de describir la ejecución.'),
        ('abc', '{F} ¿Qué tipo de enunciado es la frase 1, «la canción me parece genial»?', 'Una apreciación personal sin evidencia', 'Un juicio crítico con razón y evidencia', 'Una interpretación del estribillo', 'La frase 1 expresa gusto sin datos de la obra.'),
        ('=', '{F} El estribillo dura 4 compases de 4 pulsos a 80 pulsos por minuto. ¿Cuántos segundos dura una vez?', '4*4*60//80', 'Se multiplican los compases por los pulsos y se pasa a segundos con el tempo.', ' s'),
        ('abc', '{F} ¿Qué criterio cumple la frase 3 sobre el estribillo?', 'El B y el C, porque cita un dato y explica el efecto', 'El A solamente, porque afirma algo claro sobre la obra', 'El E, porque trata con respeto a quien canta', 'La frase 3 da un dato (nota aguda) y explica lo que produce.'),
        ('abc', '{F} ¿Cómo se corrige la frase 4 para cumplir el criterio E?', 'La voz quedó tapada por el cajón en el estribillo; se puede bajar su fuerza', 'Quien canta no sirve para cantar el estribillo de esta canción tan conocida', 'Hay que reemplazar a quien canta por otra persona del curso de música', 'Se describe lo que se oyó y se propone una práctica posible.'),
        ('=', '{F} Sol lee en voz alta su borrador de 4 frases, a 12 segundos por frase, y lo vuelve a leer tras corregirlo. ¿Cuántos segundos suman las dos lecturas?', '2*4*12', 'Se multiplican las dos lecturas por las 4 frases y por los 12 segundos de cada una.', ' s'),
        ('abc', '{F} ¿Qué ajuste hace Sol primero, si solo puede cambiar una cosa por revisión?', 'Reemplazar la frase 4, que incumple el respeto', 'Reescribir las cuatro frases con un tono más expresivo y emotivo', 'Eliminar las frases 2 y 3 para acortar la crítica del borrador', 'Se corrige primero lo que incumple un criterio básico, con un solo cambio.'),
        ('abc', '{F} ¿Qué falta en el borrador para cumplir el criterio D, propósito o contexto?', 'Mencionar que la canción acompaña una tarde tranquila', 'Agregar que la canción es la más escuchada del año en la radio', 'Decir que la canción es mejor que otras de su mismo estilo', 'El criterio D pide nombrar propósito o contexto, que la ficha indica.'),
        ('abc', 'Una crítica contiene la frase «tu ejecución me aburrió». ¿Cómo se reformula con evidencia y respeto?', 'En las estrofas la fuerza no cambió; sugiero marcar la subida hacia el estribillo', 'Tu ejecución estuvo mal y debes tocar de otra manera la próxima vez', 'No volveré a escuchar lo que tocas por lo aburrido que fue todo', 'Se describe lo que se oyó, con un dato y una sugerencia, sin atacar a la persona.'),
        ('abc', '{F} Una persona se siente herida porque su crítica fue calificada de «inútil». ¿Qué decisión corresponde?', 'Reformular la crítica y pedir orientación a una persona adulta', 'Reírse del comentario para quitarle importancia al problema que surgió', 'Borrar su crítica sin conversar con nadie sobre lo ocurrido en clase', 'Reformular y pedir orientación cuida a la persona y al trabajo.'),
        ('=', '{F} Si cada revisión de la crítica toma 4 minutos y Sol hace 3 revisiones, ¿cuántos minutos dedica en total?', '3*4', 'Se multiplica la cantidad de revisiones por los minutos de cada una.', ' minutos'),
    ],
    ctx=('abc', 'Tu docente te pide una crítica de dos frases sobre la presentación de un compañero. ¿Qué escribes?', 'Un logro con evidencia y una sugerencia respetuosa', 'Una frase con su nombre y otra con tu opinión sobre su persona y su forma de ser', 'Una frase de elogio y otra que compara su presentación con la tuya propia', 'Un logro con evidencia y una sugerencia posible mantienen el foco en la obra y el trato respetuoso.'),
    sc=[
        ("En Interpretación musical: ¿qué es una sugerencia?", "Un cambio concreto y posible que se propone", "La sugerencia ayuda a mejorar sin descalificar."),
        ('abc', 'Para ajustar una crítica, conviene cambiar:', 'Una sola cosa por revisión', 'Todas las frases a la vez', 'Nada y entregar el borrador', 'Un cambio por revisión permite saber qué lo mejoró.'),
        ("¿Qué haces si una crítica hiere a una persona?", "La reformulo con respeto y pido orientación a una persona adulta", "El trato cuidadoso es parte de una buena crítica."),
    ],
    op=("Con la {F}, revisa el borrador de Sol con los cinco criterios (A a E): marca «cumple» o «falta» con la frase que lo respalda. Reescribe la frase 4 y la frase 1 para que cumplan la pauta, y anota qué cambiaste y por qué.",
        "A cumple (frase 2). B cumple (frase 2: estrofas en p y 80 pulsos). C cumple (frase 2: «lo que da calma»). D cumple (frase 2 menciona tarde tranquila). E falta (frase 4). Reescribo la 4: «el pasaje de la nota aguda se oyó inseguro; puede practicarse con calma». Reescribo la 1: «me gusta la canción, y además es adecuada para una plaza». Cambié una descalificación por una observación y una apreciación por un dato.",
        ["revisa los cinco criterios con evidencia", "reescribe la frase 4 con respeto", "reescribe la frase 1 con un dato", "anota qué cambió y por qué"],
        ["hoja con la pauta marcada y las dos frases reescritas"],
        ["marcar criterios sin evidencia", "reescribir con otra descalificación", "no anotar los cambios"],
        "Pregunta: «¿qué frase respalda ese criterio?». Si no la encuentra, pídele que la subraye."),
    reinforce="Escribe una crítica de cinco frases de una pieza inventada y revísala con una pauta de tres criterios.",
    extend="Explica por qué una crítica puede ser exigente y respetuosa a la vez, con un ejemplo.",
)
