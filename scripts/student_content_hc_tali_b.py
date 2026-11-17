"""Taller de literatura (electivo 3.º y 4.º medio HC): OAC-03 (comentar y criticar la lectura y escritura de los pares, clases 1 a 4) y OAC-04 (revisar y reescribir las propias producciones, clases 1 a 4)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los textos de pares, borradores, comentarios y versiones de los ejercicios son originales, inventados para este cuaderno y están escritos completos en el enunciado: no necesitas libros ni internet. "
             "En el taller real comentarás textos de compañeras y compañeros: hazlo siempre con respeto, hablando del texto y no de la persona. Si recibes o ves un comentario que te humilla o que humilla a otra persona, no respondas con insultos y avisa a una persona adulta de confianza, como tu docente.")
build = make_build(MATERIALS)

O3 = "LL-TALI-3y4-OAC-03"
O4 = "LL-TALI-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (texto de un compañero, original de ejemplo). «El turno de la abuela»: «La abuela contaba los minutos con las manos. Cuando el reloj del living dio las seis, se levantó, ordenó el mantel y esperó. A las siete cenó sola, con dos platos servidos.» "
     "Comentarios de ejemplo. C1) «Me gustó mucho.» C2) «Los dos platos servidos hacen sentir la espera sin decirla.» C3) «Sería más fuerte si quitas «esperó», porque el mantel ordenado ya lo sugiere.» C4) «Escribes mal.»")
build(
    O3, 1, F,
    use="Aprenderé a distinguir tipos de comentario sobre el texto de un par (valoración, interpretación, sugerencia) y a reconocer cuáles ayudan a mejorar un texto. Sirve para participar en un taller de lectura y escritura con respeto y utilidad.",
    prior=["Sé qué es una interpretación.", "Sé que una opinión necesita razones.", "Conozco la diferencia entre un texto y su autor."],
    explain=[
        "En un taller literario, el comentario es una respuesta a un texto de una compañera o un compañero. Un comentario útil habla del texto, no de la persona; es específico, es decir, señala un pasaje concreto; y está orientado a ayudar, ya sea mostrando lo que funciona o proponiendo cambios. Un comentario como «me gustó mucho» es amable pero no ayuda a seguir escribiendo, porque no dice qué gustó ni por qué.",
        "Hay cuatro tipos frecuentes. La valoración dice qué funciona y por qué («los dos platos servidos hacen sentir la espera»). La interpretación cuenta qué entendió quien lee («entiendo que la abuela espera a alguien que no llega»). La sugerencia propone un cambio con una razón («quita ‘esperó’, porque ya se entiende»). La pregunta pide aclarar una decisión («¿por qué son dos platos?»). Los mejores comentarios combinan varios de estos tipos.",
        "Un comentario no es útil cuando descalifica a la persona («escribes mal»), cuando solo expresa gusto sin razones («me gustó») o cuando exige que el texto sea otro («yo lo habría escrito de otro modo»). El criterio central es el efecto que el propio texto busca: se comenta si el texto logra lo que se propone, no si coincide con lo que yo escribiría. Si un comentario te hiere, no respondas con otro insulto; conversa con tu docente.",
    ],
    vocab=[("comentario", "respuesta oral o escrita a un texto de otra persona"), ("valoración", "comentario que dice qué funciona y por qué"), ("sugerencia", "comentario que propone un cambio con una razón"), ("específico", "que señala un pasaje o un aspecto concreto"), ("descalificar", "atacar a la persona en lugar de comentar el texto")],
    worked=[
        ("Clasificar un comentario", "El comentario C2 dice que los dos platos servidos hacen sentir la espera sin decirla. ¿Qué tipo es?",
         ["Señala un pasaje concreto: los dos platos servidos.", "Dice qué funciona y por qué.", "Por eso es una valoración específica."],
         "Valoración específica"),
        ("Reconocer un comentario poco útil", "El comentario C4 dice «escribes mal». ¿Por qué no ayuda?",
         ["No señala ningún pasaje.", "Habla de la persona y no del texto.", "No propone ningún cambio ni dice qué funciona."],
         "Descalifica a la persona y no es específico"),
    ],
    mistakes=[("Creer que un comentario amable como «me gustó mucho» ya ayuda al autor.", "No dice qué gustó ni por qué, así que el autor no sabe qué conservar.", "Agrega el pasaje y la razón: «me gustó el cierre porque…»."),
              ("Comentar el texto como si fuera una prueba de la persona: «escribes mal».", "Ataca a quien escribió y no orienta la mejora del texto.", "Habla del pasaje y propón un cambio con una razón.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es una sugerencia en un comentario?", "Un cambio propuesto con una razón", "Un resumen del texto", "Un insulto con forma amable", "La sugerencia propone una modificación y explica por qué ayudaría."),
        ("{F} ¿Cuál comentario, C1, C2, C3 o C4, descalifica a la persona?", "C4", "«Escribes mal» ataca a quien escribe y no habla de ningún pasaje."),
        ("{F} ¿Cuál comentario es solo una expresión de gusto, sin razones?", "C1", "«Me gustó mucho» no dice qué ni por qué."),
        ("abc", "{F} ¿De qué tipo es el comentario C3?", "Sugerencia", "Valoración", "Descalificación", "C3 propone quitar una palabra y da una razón, lo propio de una sugerencia."),
        ("ab", "{F} ¿Qué pasaje del texto comenta C2?", "Los dos platos servidos", "La hora del reloj", "C2 se refiere a los platos servidos, que hacen sentir la espera."),
        ("abc", "{F} Una compañera dice: «entiendo que la abuela prepara la cena para alguien que ya no vendrá». ¿Qué tipo de comentario es?", "Interpretación", "Sugerencia", "Descalificación", "Cuenta lo que ella entendió del texto, que es el sentido de una interpretación."),
        ("abc", "{F} ¿Cómo mejorarías C1 para que ayude al autor?", "«Me gustó el cierre con los dos platos, porque muestra la espera sin decirla»", "«Me gustó, pero yo lo habría escrito distinto»", "«Me gustó porque me gusta»", "La mejora agrega pasaje y razón; las otras alternativas no orientan al autor."),
        ("abc", "{F} Un compañero comenta: «yo habría contado esto en primera persona». ¿Qué problema tiene el comentario?", "Pide que el texto sea otro en vez de evaluar si logra su propio efecto", "Es demasiado amable", "No tiene ningún problema", "Un buen comentario evalúa el efecto del texto, no el texto que el comentarista habría escrito."),
        ("ab", "{F} El autor busca sugerir la espera sin nombrarla. ¿Qué comentario respeta ese propósito?", "C2, porque valora cómo el texto lo logra", "C4, porque corrige al autor", "C2 evalúa el texto según su propio efecto; C4 no dice nada de eso."),
        ("abc", "{F} ¿Qué pregunta ayudaría al autor a aclarar una decisión del texto?", "«¿Por qué decidiste que fueran dos platos?»", "«¿Por qué escribes tan mal?»", "«¿Te gusta que te comenten?»", "La primera es una pregunta sobre una decisión concreta; las otras no hablan del texto."),
        ("abc", "{F} Se quiere combinar valoración y sugerencia. ¿Cuál lo logra?", "«El mantel ordenado sugiere la espera; quizá no haga falta decir ‘esperó’»", "«Está bien»", "«No me convence nada»", "La primera valora un pasaje y propone un cambio, mientras las otras no son específicas."),
        ("abc", "{F} Si un comentario te humilla en el taller, ¿qué haces?", "Hablas con tu docente o una persona adulta de confianza", "Respondes con otro insulto", "Dejas el taller para siempre sin decir nada", "El comentario que humilla no es parte del taller; se avisa a una persona adulta."),
        ("{F} Completa con una hora del texto: la abuela se levantó cuando el reloj dio las ____.", "seis", "El texto dice que se levantó cuando el reloj dio las seis."),
    ],
    ctx=("abc", "Contexto: en el taller recibes el texto de la ficha {F} y debes dejar un comentario en una nota adhesiva de pocas líneas. ¿Cuál es el más útil?", "«Los dos platos servidos muestran la espera. Quizá sobre la palabra esperó»", "«Me encantó, felicitaciones»", "«No entiendo nada de lo que escribes»", "El primero señala un pasaje, valora y sugiere con razón; los otros no ayudan a mejorar."),
    sc=[
        ("ab", "Un comentario útil habla de:", "El texto", "La persona que lo escribió", "El comentario eficaz se centra en el texto y no en quien lo escribió."),
        ("En Taller de literatura: ¿qué significa que un comentario sea específico?", "Que señala un pasaje o aspecto concreto", "Un comentario específico indica a qué parte del texto se refiere."),
        ("ab", "«Yo lo habría escrito de otro modo» es:", "Un comentario poco útil si no evalúa el efecto del texto", "El mejor comentario posible", "No evalúa lo que el texto busca, sino lo que otra persona haría."),
    ],
    op=("Lee otra vez la ficha {F}. Escribe tu comentario para el autor con tres partes: (1) una valoración específica con razón; (2) una sugerencia con razón; (3) una pregunta sobre una decisión del texto.",
        "(1) Me gustó que la abuela ordene el mantel, porque muestra su preparación sin explicarla. (2) Podrías cortar «esperó», porque el gesto del mantel ya lo sugiere. (3) ¿Por qué elegiste las siete para que cene sola?",
        ["valoración con pasaje y razón", "sugerencia con razón", "pregunta sobre una decisión", "tono respetuoso dirigido al texto"],
        ["tres partes numeradas"],
        ["valoración sin razón", "sugerencia que pide otro texto", "pregunta que ataca al autor"],
        "Pregunta: «¿tu comentario le sirve al autor si lo lee solo, sin ti al lado?»."),
    reinforce="Reescribe estos tres comentarios para que ayuden al autor: «está lindo», «no entendí», «muy largo».",
    extend="Explica por qué comentar a un compañero un texto exige respeto y también honestidad, y cómo se logra ambas cosas.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (poema de una compañera, original de ejemplo). «Escalera»: «Subo la escalera del edificio / contando los escalones que sobran. / En el cuarto piso, una puerta entreabierta / deja escapar el olor de un guiso. / No toco. Sigo subiendo.» "
     "Estructura de comentario de ejemplo: observo (lo que veo en el texto), interpreto (lo que entiendo), sugiero (lo que podría mejorar) y pregunto (lo que quiero saber).")
build(
    O3, 2, F,
    use="Aprenderé a formular un comentario con estructura: observar, interpretar, sugerir y preguntar. Sirve para que mis aportes en el taller sean claros, justificados y útiles para quien escribió.",
    prior=["Sé distinguir valoración, sugerencia y pregunta.", "Sé citar un pasaje.", "Sé que comentar es hablar del texto."],
    explain=[
        "Un comentario estructurado se arma en cuatro movimientos. Observo: describo con exactitud un pasaje del texto, sin juzgar todavía («en el cuarto piso, una puerta entreabierta»). Interpreto: digo qué entiendo o qué efecto me produce («la puerta abierta tienta a detenerse»). Sugiero: propongo un cambio con razón. Pregunto: pido aclarar una decisión. El orden ayuda a que la crítica nazca de lo que el texto hace.",
        "Observar bien es la base. Quien observa cita o parafrasea y evita adjetivos de gusto («lindo», «feo»). Si dice «en el verso cuatro, el olor de un guiso cambia el clima del poema», está señalando un pasaje preciso. A partir de esa observación, la interpretación es una hipótesis que el autor puede aceptar o corregir: «entiendo que la voz quiere entrar pero se contiene».",
        "La sugerencia debe respetar el propósito del texto. Se formula como posibilidad («podrías…», «quizá…»), con una razón, y se refiere a una parte concreta. La pregunta no es una trampa: busca información. Preguntar «¿por qué elegiste que no toque?» ayuda al autor a ver si su decisión se entiende. Al terminar, conviene repasar si el comentario habla del texto y no de la persona.",
    ],
    vocab=[("observar", "describir con exactitud un pasaje, sin juzgarlo todavía"), ("interpretar", "decir qué se entiende o qué efecto produce"), ("sugerir", "proponer un cambio con una razón"), ("hipótesis de lectura", "interpretación que el autor puede aceptar o corregir"), ("pasaje", "parte concreta del texto")],
    worked=[
        ("Armar un comentario en cuatro movimientos", "Comenta el poema «Escalera».",
         ["Observo: en el verso cuatro, el olor de un guiso sale de una puerta entreabierta.", "Interpreto: entiendo que la voz quiere entrar pero se contiene.", "Sugiero: podrías agregar un detalle sonoro, porque el poema solo tiene olor y vista.", "Pregunto: ¿por qué elegiste que la voz no toque?"],
         "Un comentario con observo, interpreto, sugiero y pregunto"),
        ("Distinguir observación de juicio", "¿«Qué lindo el verso del guiso» es una observación?",
         ["La palabra «lindo» es un juicio de gusto.", "No describe qué hace el verso.", "Una observación sería: «el verso nombra un olor que sale de una puerta»."],
         "No: es un juicio de gusto"),
    ],
    mistakes=[("Interpretar presentando la lectura como la única posible: «el poema trata de la soledad».", "La interpretación es una hipótesis que el autor puede matizar.", "Usa «entiendo que…» o «me parece que…» y señala el pasaje."),
              ("Sugerir un cambio sin razón: «cambia el final».", "Sin razón, el autor no sabe qué problema se quiere resolver.", "Agrega por qué: «cambia el final, porque repite lo que ya dice el verso cuatro».")],
    T=[
        ("{F} ¿Cuántos versos tiene el poema «Escalera»?", "5", "Se cuentan cinco líneas: subo, contando, cuarto piso, guiso y no toco."),
        ("abc", "En Taller de literatura: ¿qué es observar en un comentario?", "Describir con exactitud un pasaje sin juzgarlo todavía", "Decir si el texto gustó o no", "Proponer un cambio", "Observar es describir lo que el texto hace antes de interpretar o sugerir."),
        ("{F} ¿En qué piso hay una puerta entreabierta?", "En el cuarto", "El verso tres dice que en el cuarto piso hay una puerta entreabierta."),
        ("abc", "{F} ¿Cuál de estas frases es una observación?", "«En el último verso, la voz dice que no toca y sigue subiendo»", "«Me encantó el poema»", "«Debes cambiar el final»", "La primera describe un pasaje sin juzgar; las otras son gusto y sugerencia."),
        ("abc", "{F} ¿Cuál de estas frases es una interpretación presentada como hipótesis?", "«Entiendo que la voz respeta la intimidad de quien vive ahí»", "«En el verso cuatro hay un olor a guiso»", "«Deberías eliminar el verso cuatro»", "Interpreta con «entiendo que» lo que sugiere el texto; las otras son descripción o sugerencia."),
        ("abc", "{F} ¿Cuál es una sugerencia bien formulada?", "«Podrías decir qué siente la voz al pasar frente a la puerta, porque ahora solo vemos lo que hace»", "«Agrega algo»", "«Está mal construido»", "Propone un cambio, lo ubica y da una razón."),
        ("ab", "{F} ¿Qué sentido tiene preguntar «¿por qué elegiste que la voz no toque?»", "Aclarar una decisión del texto para saber si se entiende", "Mostrar que la decisión está equivocada", "La pregunta busca información sobre una decisión, no la condena."),
        ("abc", "{F} Un compañero comenta: «el poema es sobre una escalera y nada más». ¿Qué le falta a su lectura?", "Una interpretación que explique el efecto de la puerta entreabierta", "Más versos", "Un título más largo", "Una lectura que se limita a los objetos no interpreta qué hace el texto con ellos."),
        ("abc", "{F} En un comentario estructurado, ¿qué movimiento conviene hacer primero?", "Observo", "Sugiero", "Pregunto", "Observar es la base: sin describir el pasaje, la interpretación queda sin apoyo."),
        ("ab", "{F} Un comentario dice «sobra el verso dos». ¿Qué falta para que sea una sugerencia útil?", "Una razón que explique por qué sobra", "Una oración más amable que no cambie el contenido", "Sin razón, el autor no sabe qué problema se quiere resolver."),
        ("abc", "{F} Para ayudar al autor a ver el efecto del último verso, ¿qué comentario es mejor?", "«En ‘No toco. Sigo subiendo.’ entiendo que la voz decide no entrometerse; me hace sentir respeto y distancia»", "«El final es corto»", "«Me da lo mismo el final»", "El primero observa, interpreta y deja ver el efecto, mientras los otros no lo hacen."),
        ("abc", "{F} Un comentario combina: «Entiendo que la voz respeta a quien vive ahí. ¿Pensaste en agregar una pausa antes del último verso?». ¿Qué movimientos contiene?", "Interpreto y pregunto", "Observo y sugiero", "Solo sugiero", "Contiene una interpretación y una pregunta sobre una posible decisión."),
        ("ab", "{F} «Eliminaría el verso del guiso porque no entiendo para qué está». ¿Qué problema tiene?", "Sugiere eliminar antes de preguntar por la intención del verso", "Es una descalificación personal", "Antes de proponer un corte conviene preguntar qué busca el verso, no asumir que sobra."),
    ],
    ctx=("abc", "Contexto: tu docente da dos minutos para que cada persona comente oralmente el poema de la ficha {F} ante el curso. ¿Qué plan de comentario sirve mejor?", "Observo un verso, interpreto, sugiero una cosa con razón y hago una pregunta", "Digo todo lo que me parece mal del poema", "Leo el poema de nuevo y no digo nada", "El plan estructurado cabe en dos minutos y deja una conversación útil."),
    sc=[
        ("En Taller de literatura: ¿qué movimiento del comentario pide aclarar una decisión del texto?", "Preguntar", "La pregunta busca información sobre las decisiones del autor."),
        ("ab", "Una sugerencia debe llevar:", "Una razón", "Un insulto suave", "Con una razón el autor entiende qué problema se quiere resolver."),
        ("ab", "Una interpretación se presenta mejor como:", "Una hipótesis que el autor puede matizar", "Una verdad que no admite discusión", "Es una lectura posible, no un hecho."),
    ],
    op=("Con el poema de la ficha {F}, escribe un comentario estructurado de cuatro oraciones, una por movimiento: observo, interpreto, sugiero y pregunto. Cada oración debe hacer referencia a un pasaje o a una decisión concreta.",
        "Observo: en el verso dos, la voz cuenta los escalones que sobran. Interpreto: entiendo que cuenta para distraerse de algo. Sugiero: podrías mostrar qué la inquieta, para que ese gesto pese más. Pregunto: ¿por qué elegiste el cuarto piso?",
        ["cuatro movimientos presentes", "cada oración se refiere a un pasaje", "interpretación como hipótesis", "sugerencia con razón", "pregunta sobre una decisión"],
        ["cuatro oraciones"],
        ["observación con juicio de gusto", "sugerencia sin razón", "pregunta que ataca"],
        "Pregunta: «¿cuál de tus cuatro oraciones le serviría más al autor para decidir qué hacer?»."),
    reinforce="Escribe una observación, una interpretación y una sugerencia sobre los dos primeros versos de «Escalera», sin repetir frases del ejemplo.",
    extend="Explica por qué una buena pregunta puede ayudar más a un autor que una sugerencia directa.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (fragmento de un compañero, original de ejemplo). «—¿Vienes? —preguntó Clara. —No sé —dijo Mateo, y miró sus zapatillas—. Quizás. —Quizás es lo que dices cuando ya sabes —dijo ella. Mateo no respondió.» "
     "Comentarios de ejemplo. D1) «Los diálogos son muy naturales.» D2) «Que Mateo mire sus zapatillas muestra que evita decidir.» D3) «Me aburrí.» D4) «La frase de Clara sobre ‘quizás’ me parece lo mejor, porque dice algo que Mateo no se atreve a decir.»")
build(
    O3, 3, F,
    use="Aprenderé a respaldar mis comentarios con pasajes y con recursos del texto, y a distinguir una crítica fundamentada de una opinión de gusto. Sirve para que mis comentarios convenzan y ayuden a quien escribe.",
    prior=["Sé armar un comentario con observo, interpreto, sugiero y pregunto.", "Sé citar un pasaje.", "Reconozco el diálogo y la acotación."],
    explain=[
        "Un comentario fundamentado se apoya en evidencia del texto: una cita breve, un recurso nombrado y el efecto que produce. Decir «los diálogos son naturales» es un juicio sin apoyo; decir «el diálogo es natural porque Mateo duda y Clara lo interrumpe con una frase corta» señala por qué. La regla es: cada juicio lleva su pasaje y su razón.",
        "Es útil distinguir gusto de criterio. El gusto es una preferencia personal («me aburrí», «me encantó») y vale como información, pero no orienta la reescritura. El criterio es una pregunta compartida que se aplica al texto: ¿el diálogo suena natural?, ¿el conflicto se entiende?, ¿el final deja pensar? Un comentario con criterio dice qué criterio usa, qué pasaje lo muestra y si el texto lo cumple.",
        "En un diálogo, el subtexto es lo que los personajes no dicen directamente. Comentar el subtexto es una forma de interpretar: en el fragmento, «Quizás es lo que dices cuando ya sabes» deja ver que Clara entiende la duda de Mateo. También se pueden comentar las acotaciones, el ritmo de las frases y los silencios. Siempre se acompaña la crítica con tono respetuoso: se critica el texto, no a su autor.",
    ],
    vocab=[("criterio", "pregunta compartida que se aplica al texto para evaluarlo"), ("gusto", "preferencia personal sin razones del texto"), ("subtexto", "lo que los personajes sugieren sin decirlo directamente"), ("evidencia", "pasaje del texto que apoya un comentario"), ("acotación", "indicación sobre acciones o gestos dentro del texto")],
    worked=[
        ("Fundamentar un juicio", "D1 dice «los diálogos son muy naturales». ¿Cómo lo fundamentas?",
         ["Elige un criterio: el diálogo suena como habla real.", "Cita un pasaje: «—No sé —dijo Mateo… Quizás».", "Explica: las dudas y las frases cortas se parecen al habla cotidiana."],
         "Con criterio, pasaje y razón"),
        ("Distinguir gusto de criterio", "D3 dice «me aburrí». ¿Es gusto o criterio?",
         ["No señala ningún pasaje.", "No dice qué criterio no se cumple.", "Es una reacción personal, o sea, gusto."],
         "Gusto"),
    ],
    mistakes=[("Defender un juicio con otra opinión: «es bueno porque es bueno».", "Un juicio necesita un pasaje y una razón, no repetirse.", "Cita el pasaje y explica el efecto que produce."),
              ("Descartar lo que un texto hace por no ser de tu gusto personal.", "El gusto no es un criterio común; el texto puede lograr bien su propósito aunque no te agrade.", "Evalúa el texto con criterios y menciona tu gusto aparte.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es el subtexto en un diálogo?", "Lo que los personajes sugieren sin decirlo directamente", "El título del texto", "La lista de personajes", "El subtexto es el significado implícito detrás de lo que se dice."),
        ("{F} ¿Quién dice «Quizás es lo que dices cuando ya sabes»?", "Clara", "La frase la dice Clara en respuesta a Mateo."),
        ("{F} ¿Cuál comentario, D1, D2, D3 o D4, nombra un criterio (que el diálogo es natural) pero no trae ningún pasaje que lo respalde?", "D1", "D1 afirma que los diálogos son naturales sin citar nada del texto; D2 y D4 sí señalan pasajes."),
        ("abc", "{F} ¿Qué pasaje apoya el comentario D2, que Mateo evita decidir?", "«y miró sus zapatillas»", "«—¿Vienes? —preguntó Clara»", "«Mateo no respondió»", "Mirar las zapatillas es la acción que muestra evasión."),
        ("abc", "{F} ¿Qué criterio aplica D4?", "Si el diálogo dice algo que los personajes no dicen directamente", "Si el diálogo es largo", "Si el diálogo tiene muchas exclamaciones", "D4 destaca que Clara nombra lo que Mateo no se atreve, que es el subtexto."),
        ("ab", "{F} D4 dice que la frase de Clara sobre «quizás» dice algo que Mateo no se atreve a decir. ¿Qué la haría mejor fundamentada?", "Citar la frase de Clara y explicar qué es lo que Mateo no dice", "Agregar que a ti también te gustó mucho el fragmento", "Citar la frase y explicar su efecto convierte la valoración en una crítica con evidencia; sumar gusto personal no la respalda."),
        ("abc", "{F} Un compañero propone: «Mateo está enamorado de Clara». ¿Qué ocurre con la evidencia?", "El fragmento no dice nada que lo muestre", "Está respaldada por «Quizás»", "Está respaldada por «miró sus zapatillas»", "El texto muestra duda, no enamoramiento; la afirmación atribuye algo sin evidencia."),
        ("abc", "{F} ¿Qué comentario combina criterio, pasaje y razón?", "«El silencio final de Mateo funciona, porque deja sin respuesta la frase de Clara»", "«El final es bueno»", "«Me gustó el final porque sí»", "Solo el primero señala un criterio (el silencio), un pasaje y una razón."),
        ("abc", "{F} Se quiere sugerir una mejora sobre la acotación «y miró sus zapatillas». ¿Cuál es una sugerencia fundamentada?", "«Podrías precisar cómo mira, porque esa acción muestra su duda»", "«Quita las acotaciones»", "«Las zapatillas no me gustan»", "La primera propone un cambio razonado sobre un pasaje concreto."),
        ("ab", "{F} El comentario D3 dice «me aburrí». ¿Cómo lo transformarías en crítica fundamentada?", "Indicar qué parte, qué criterio no se cumple y por qué", "Repetirlo con más fuerza", "La crítica requiere ubicar el pasaje y el criterio, no solo reiterar el gusto."),
        ("abc", "{F} Dos comentarios: E1 «el silencio de Mateo dice que ya decidió» y E2 «el silencio de Mateo dice que duda». ¿Qué pasaje respalda E2?", "«—No sé —dijo Mateo… Quizás.»", "«—Quizás es lo que dices cuando ya sabes —dijo ella.»", "«—¿Vienes? —preguntó Clara.»", "Las palabras de Mateo expresan duda; la frase de Clara, en cambio, sostiene la lectura E1 desde la mirada de ella."),
        ("abc", "{F} Se quiere comentar el ritmo del fragmento. ¿Qué observación corresponde?", "Las frases cortas y las pausas del diálogo generan sensación de tensión", "Los personajes hablan con frases largas y complejas", "El fragmento tiene extensas descripciones del paisaje", "Las frases cortas con pausas marcan un ritmo tenso; el fragmento no tiene frases largas ni descripciones del paisaje."),
        ("abc", "{F} Un comentario dice: «el texto es mejor que cualquier otro del taller». ¿Qué problema tiene?", "Compara con otros textos y no aporta evidencia sobre este", "Es una crítica demasiado dura", "Es una observación objetiva", "Una comparación vaga no orienta ni se apoya en el texto comentado."),
    ],
    ctx=("abc", "Contexto: en la sesión de taller, tu grupo comenta el fragmento de la ficha {F}. Alguien dice «es lo mejor que leí». ¿Qué pregunta ayuda al grupo a ir más allá del gusto?", "«¿Qué pasaje te hace pensar eso y qué efecto produce?»", "«¿Por qué dices eso?» con tono molesto", "«No, no es lo mejor»", "La pregunta pide pasaje y efecto, lo que transforma el gusto en comentario fundamentado."),
    sc=[
        ("En Taller de literatura: ¿qué diferencia hay entre gusto y criterio?", "El gusto es preferencia personal; el criterio se aplica al texto", "El criterio es compartido y permite evaluar; el gusto es subjetivo."),
        ("ab", "Un juicio fundamentado lleva:", "Pasaje y razón", "Solo una opinión", "Sin pasaje y razón el juicio queda sin respaldo."),
        ("ab", "En un diálogo, comentar el subtexto es:", "Interpretar lo que se sugiere sin decirse", "Contar cuántas palabras hay", "El subtexto está en lo implícito de las palabras."),
    ],
    op=("Elige uno de los comentarios D1, D2 o D3 de la ficha {F} y reescríbelo como un comentario fundamentado: indica el criterio que usas, cita un pasaje breve y explica la razón. Luego agrega una sugerencia para el autor.",
        "Reescribo D1. Criterio: el diálogo suena natural. Pasaje: «—No sé —dijo Mateo… Quizás». Razón: duda y usa frases cortas, como en el habla real. Sugerencia: podrías variar una acotación, porque «miró sus zapatillas» ya se usó una vez.",
        ["comentario elegido de la ficha", "criterio explícito", "cita breve del texto", "razón del juicio", "sugerencia para el autor"],
        ["comentario de cuatro a cinco oraciones"],
        ["criterio ausente", "cita que no apoya el juicio", "sugerencia que no tiene relación con el criterio"],
        "Pregunta: «¿tu comentario cambiaría si no te gustara el fragmento?»."),
    reinforce="Convierte este comentario en uno fundamentado: «el final no me convence».",
    extend="Explica por qué un criterio compartido permite discutir un texto con alguien que tiene gustos distintos.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (microrrelato de un compañero, original de ejemplo). «El trueque»: «Le cambié mi bicicleta al vecino por un reloj parado. Él pedaleó feliz hasta la esquina. Yo me quedé con la hora exacta de las cuatro y diez, que a veces es todo lo que uno quiere guardar.» "
     "Dos comentarios que discrepan. Ana: «Es un texto triste: el narrador pierde algo y se queda con un objeto inútil.» Beto: «Es un texto cálido: el narrador elige guardar un momento y lo hace con humor.»")
build(
    O3, 4, F,
    use="Aprenderé a contrastar comentarios distintos sobre un mismo texto, a integrar lo valioso de cada uno y a discutir con respeto en una lectura colectiva. Sirve para enriquecer la lectura del grupo y para recibir críticas sin ponerme a la defensiva.",
    prior=["Sé fundamentar un comentario.", "Sé qué es una interpretación plausible.", "Sé distinguir gusto de criterio."],
    explain=[
        "En una lectura colectiva, varias personas leen el mismo texto y proponen interpretaciones distintas. Esas diferencias no son un problema: son la razón de leer en grupo. Dos comentarios que discrepan pueden ser ambos válidos si cada uno se apoya en el texto. Se descartan solo cuando uno contradice el texto o inventa algo que no está.",
        "Para contrastar comentarios, sigue pasos: identifica el foco de cada uno (qué parte del texto miran); busca el pasaje que lo respalda; revisa si algún pasaje lo complica; y busca qué aportan en conjunto. En «El trueque», Ana mira la pérdida de la bicicleta y Beto mira el momento guardado; juntos permiten leer un texto agridulce, con pérdida y también ternura.",
        "También hay reglas para conversar. Escucha el comentario completo antes de responder; reconoce lo que sí compartes antes de discrepar («coincido en…, pero veo otra cosa en…»); critica el argumento y no a la persona; y acepta que puedes cambiar de lectura si el otro presenta un pasaje que no habías visto. Si recibes una crítica a tu texto, anota lo que dice y decide después con calma qué aceptas. Si hay burlas o agresiones, avisa a tu docente.",
    ],
    vocab=[("lectura colectiva", "lectura en grupo en la que se comparan interpretaciones"), ("foco", "parte del texto en que se concentra un comentario"), ("agridulce", "que combina un aspecto triste y uno cálido o alegre"), ("discrepar", "pensar o decir algo distinto de otra persona"), ("argumento", "razón que apoya una afirmación")],
    worked=[
        ("Integrar dos comentarios", "Ana dice que el texto es triste; Beto, que es cálido. ¿Se contradicen?",
         ["Ana mira la pérdida de la bicicleta por un reloj parado.", "Beto mira el momento guardado con humor.", "Ambos tienen pasajes que los respaldan y no se excluyen: el texto es agridulce."],
         "No se contradicen; se complementan"),
        ("Discrepar con respeto", "No compartes la lectura de Ana. ¿Cómo lo dices?",
         ["Reconoce lo que sí compartes: «coincido en que el narrador pierde la bicicleta».", "Presenta tu diferencia con un pasaje: «pero veo ternura en ‘todo lo que uno quiere guardar’»."],
         "Con reconocimiento y un pasaje que respalde tu otra lectura"),
    ],
    mistakes=[("Responder al comentario de otro buscando «ganar» la discusión.", "El objetivo de la lectura colectiva es enriquecer la lectura, no vencer.", "Pregunta qué pasaje respalda el comentario y reconoce lo valioso antes de discrepar."),
              ("Tomar la crítica a tu texto como un ataque personal.", "La crítica se dirige al texto y puede ayudarte, aunque te incomode.", "Anota lo dicho, espera un momento y decide después qué aceptas y qué no.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué es una lectura colectiva?", "Leer en grupo comparando interpretaciones", "Leer un libro en silencio", "Copiar un texto entre varias personas", "La lectura colectiva compara interpretaciones del mismo texto."),
        ("{F} ¿Qué objeto recibe el narrador a cambio de la bicicleta?", "Un reloj parado", "El texto dice que cambió su bicicleta por un reloj parado."),
        ("{F} ¿A qué hora está parado el reloj?", "A las cuatro y diez", "El texto menciona la hora exacta de las cuatro y diez."),
        ("abc", "{F} ¿Cuál es el foco del comentario de Ana?", "La pérdida de la bicicleta", "El humor del narrador", "El vecino feliz", "Ana destaca lo que se pierde y el objeto inútil."),
        ("abc", "{F} ¿Qué pasaje respalda el comentario de Beto?", "«que a veces es todo lo que uno quiere guardar»", "«Le cambié mi bicicleta»", "«Él pedaleó feliz»", "La frase final muestra al narrador valorando guardar un momento."),
        ("abc", "{F} Carla dice: «el texto es solo humor: el narrador no pierde nada». ¿Qué pasaje complica su lectura?", "«Le cambié mi bicicleta al vecino por un reloj parado»", "«Él pedaleó feliz hasta la esquina»", "«a las cuatro y diez»", "El narrador entrega su bicicleta, es decir, pierde algo; los otros pasajes no contradicen la lectura de Carla."),
        ("abc", "{F} Un compañero dice: «el narrador fue engañado por el vecino». ¿Qué ocurre con la evidencia?", "El texto no dice que haya engaño", "Lo respalda «un reloj parado»", "Lo respalda «pedaleó feliz»", "El texto presenta un trueque aceptado por el narrador, no un engaño."),
        ("abc", "{F} Quieres discrepar con Beto. ¿Cuál es la forma más adecuada?", "«Coincido en que hay humor, pero veo también una pérdida, porque el narrador entrega su bicicleta»", "«Estás equivocado»", "«Nadie piensa como tú»", "La primera reconoce lo compartido, presenta una diferencia y la respalda con un pasaje."),
        ("abc", "{F} Ana y Beto discuten y Ana dice «tú no entiendes de textos». ¿Qué corresponde?", "Volver al texto y pedir el pasaje que respalda cada lectura, sin atacar a la persona", "Callarse y no volver a opinar", "Responder con otra descalificación", "La discusión debe centrarse en el texto; la descalificación personal no es parte del taller."),
        ("ab", "{F} Tu compañero dice que el texto es cálido y tú lo veías triste. ¿Cuál es una reacción adecuada?", "Revisar el pasaje que él cita y considerar si cambia tu lectura", "Defender tu lectura sin escuchar", "Estar abierto al pasaje que no habías visto es parte de leer en colectivo."),
        ("abc", "{F} Se quiere integrar ambas lecturas en una sola oración. ¿Cuál lo logra?", "«El texto combina la pérdida de una bicicleta con la ternura de guardar una hora»", "«El texto es solo triste»", "«El texto es solo gracioso»", "Solo la primera recoge los dos focos."),
        ("abc", "Una autora recibe una crítica a su texto que le duele. ¿Qué es lo más conveniente?", "Anotar lo dicho, esperar y decidir después qué acepta", "Romper el texto", "Responder con enojo en el momento", "Tomarse un tiempo permite separar el dolor de la utilidad de la crítica."),
        ("abc", "{F} En el taller alguien se burla de la autora de «El trueque» frente al curso. ¿Qué corresponde?", "Avisar a tu docente o a una persona adulta de confianza", "Sumarse a la burla", "Quedarte en silencio y no avisar a nadie", "Una burla es una agresión; se avisa a una persona adulta."),
    ],
    ctx=("abc", "Contexto: tu grupo debe presentar al curso una lectura colectiva de la ficha {F} en un minuto. ¿Cuál es la mejor presentación?", "Mostrar las dos lecturas, sus pasajes y la lectura agridulce que las integra", "Presentar solo la lectura de quien habla más fuerte", "Leer el texto sin decir qué se entendió", "La presentación recoge los dos focos con evidencia y los integra."),
    sc=[
        ("En Taller de literatura: ¿qué haces antes de discrepar con una lectura?", "Reconozco lo que comparto con ella", "Reconocer lo compartido permite una discrepancia respetuosa."),
        ("ab", "Dos lecturas distintas de un texto:", "Pueden ser ambas válidas si las respalda el texto", "Siempre son incompatibles", "Dos lecturas con evidencia pueden coexistir."),
        ("ab", "Una crítica a mi texto sirve si:", "Me da información sobre lo que el texto logra o no", "Me hace sentir mal", "Su utilidad está en la información sobre el texto."),
    ],
    op=("Con el texto de la ficha {F} y los comentarios de Ana y Beto: (1) escribe en una oración lo que aporta cada uno; (2) cita un pasaje que respalde a cada uno; (3) escribe una tercera lectura, tuya, que integre o supere a ambos; (4) escribe cómo le dirías a Ana, con respeto, que ves otra cosa.",
        "(1) Ana aporta la pérdida; Beto, el momento guardado con humor. (2) «un reloj parado»; «todo lo que uno quiere guardar». (3) El texto trata de cómo uno cambia algo útil por un recuerdo que no vuelve. (4) Coincido contigo en la pérdida, Ana, pero veo también cariño en cómo guarda la hora.",
        ["aporte de cada comentario", "dos pasajes de respaldo", "tercera lectura propia", "forma respetuosa de discrepar"],
        ["cuatro respuestas numeradas"],
        ["descalificar uno de los comentarios", "tercera lectura sin pasaje", "discrepar sin reconocer lo compartido"],
        "Pregunta: «¿qué le pedirías a Ana o a Beto para entender mejor su lectura?»."),
    reinforce="Escribe dos comentarios que discrepen sobre el texto «El trueque», cada uno con un pasaje de respaldo.",
    extend="Explica por qué una lectura colectiva produce una interpretación más rica que una lectura individual.",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (borrador original de ejemplo, escrito por una estudiante). Borrador: «Ayer fui a la feria con mi mama y compramos tomates que estaban muy buenos y yo estaba contento y después volvimos a la casa y mi mamá hizo ensalada y estaba rica y fue un día lindo.» "
     "Comentarios recibidos. R1) «Hay muchos ‘y’ seguidos.» R2) «No sé qué quiere provocar el texto.» R3) «Falta la tilde en una palabra.» R4) «No hay un momento especial que se cuente con detalle.»")
build(
    O4, 1, F,
    use="Aprenderé a distinguir los niveles de revisión de un texto (global y local) y a decidir en qué orden revisar. Sirve para reescribir mis producciones de forma eficaz, sin perder tiempo en lo que quizá cambie.",
    prior=["Sé qué es un efecto buscado.", "Sé comentar un texto con criterios.", "Conozco ortografía básica."],
    explain=[
        "Revisar es leer el propio texto como lector crítico para decidir qué mejorar. Hay dos niveles. La revisión global mira el texto completo: el propósito, la estructura, la voz, el efecto y la selección de lo que se cuenta. La revisión local mira frases y palabras: conectores, repeticiones, ortografía, puntuación. Cada nivel responde a preguntas distintas.",
        "El orden importa. Primero se revisa lo global; después, lo local. Si pules las palabras de un párrafo que luego vas a cortar, el trabajo se pierde. En el borrador de la ficha, hay problemas globales (no se sabe qué quiere provocar; no hay un momento destacado) y locales (muchos «y», una falta de tilde). Conviene decidir primero qué texto se quiere y después corregir las frases.",
        "La revisión se hace con una pauta. La pauta enumera los criterios del proyecto: efecto buscado, extensión, recursos y ortografía. Los comentarios de otras personas son insumos para la revisión, no órdenes: se leen, se clasifican en globales y locales y se decide qué se acepta. Una revisión útil termina en una lista de cambios concretos, no solo en la sensación de que algo no funciona.",
    ],
    vocab=[("revisión global", "mirada al texto completo: propósito, estructura, efecto"), ("revisión local", "mirada a frases y palabras: conectores, ortografía"), ("pauta", "lista de criterios con que se revisa un texto"), ("borrador", "versión de un texto que aún se puede mejorar"), ("insumo", "dato o comentario que se usa para trabajar")],
    worked=[
        ("Clasificar comentarios", "R2 dice «no sé qué quiere provocar el texto». ¿Es global o local?",
         ["Se refiere al propósito del texto completo.", "No señala una palabra ni una frase.", "Es una observación global."],
         "Global"),
        ("Decidir el orden de revisión", "El borrador tiene un problema de tilde y otro de efecto. ¿Cuál se revisa primero?",
         ["El efecto afecta al texto completo y puede cambiar qué frases se conservan.", "La tilde afecta a una palabra que quizá se elimine.", "Se revisa primero el efecto y después la tilde."],
         "Primero el efecto (global) y luego la tilde (local)"),
    ],
    mistakes=[("Corregir ortografía antes de decidir qué se mantiene del texto.", "Si luego se corta o se reescribe esa parte, la corrección se pierde.", "Revisa primero lo global y deja lo local para el final."),
              ("Quedarse solo con revisión local y creer que el texto está terminado.", "Un texto sin errores de ortografía puede seguir sin lograr su efecto.", "Pregunta antes qué quiere provocar el texto y si lo consigue.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué mira una revisión global?", "El texto completo: propósito, estructura y efecto", "Las tildes de cada palabra", "Los márgenes de la hoja", "La revisión global considera el texto entero, no frases aisladas."),
        ("{F} ¿Cuál comentario, R1, R2, R3 o R4, trata de una falta de tilde?", "R3", "R3 se refiere a una falta ortográfica, que es un asunto local."),
        ("{F} ¿Cuál comentario habla de conectores repetidos?", "R1", "R1 se refiere a los muchos «y» seguidos, que son conectores."),
        ("abc", "{F} ¿Qué nivel de revisión corresponde a R4, que no hay un momento especial contado con detalle?", "Global", "Local", "Ortográfica", "Falta de un momento destacado es una decisión de selección del texto completo."),
        ("abc", "{F} ¿Qué nivel de revisión corresponde a R1, los muchos «y»?", "Local", "Global", "Ninguno", "Es un asunto de frases y conectores, que se resuelve revisando oraciones."),
        ("ab", "{F} ¿Qué se revisa primero, R4 o R1?", "R4, porque decide qué momento se cuenta antes de pulir los conectores", "R1, porque es más fácil de corregir", "Lo global condiciona qué frases quedarán, por lo que va antes que los conectores."),
        ("abc", "{F} Una compañera sugiere reescribir todo el texto a partir de un momento concreto de la feria. ¿Qué tipo de cambio es?", "Global, porque cambia la selección y la estructura", "Local, porque cambia palabras", "Ortográfico", "Elegir otro momento central modifica todo el texto."),
        ("abc", "{F} ¿Cuál es el mejor primer paso de revisión del borrador?", "Escribir qué efecto quiere provocar el texto", "Contar cuántos «y» hay", "Cambiar la tilde de «mama»", "Definir el efecto orienta el resto de las decisiones."),
        ("abc", "{F} En el borrador, ¿qué palabra muestra una falta de tilde?", "mama", "tomates", "feria", "«Mamá» lleva tilde en la última sílaba y en el borrador aparece sin ella al principio."),
        ("ab", "{F} Un estudiante corrige las tildes y declara terminado el texto. ¿Qué problema tiene su revisión?", "Solo hizo revisión local y dejó sin resolver lo global", "Corrigió demasiado", "Corregir tildes no resuelve el efecto ni la selección del texto."),
        ("abc", "{F} Se decide dar al texto un momento central: el olor de los tomates en la feria. ¿Qué cambio conviene?", "Contar ese momento con detalles y recortar lo que no aporte", "Agregar más ‘y’ para alargar", "Eliminar el texto", "Dar un momento central reorganiza el texto y exige cortar lo que no ayuda."),
        ("abc", "{F} Hay tres comentarios globales y uno local. ¿Cómo conviene trabajar?", "Abordar primero los globales y dejar el local para después", "Corregir el local y olvidar los globales", "Ignorar todos los comentarios", "Primero se resuelve lo global; luego se pule lo local."),
        ("{F} Una compañera propone cambiar «contento» por «feliz». ¿Es un cambio global o local?", "local", "Cambiar una palabra afecta solo a una expresión, no al propósito ni a la estructura del texto."),
    ],
    ctx=("abc", "Contexto: el borrador de la ficha {F} se entregará en una semana y tienes cuatro comentarios. Una compañera dice «empieza por la tilde, que es lo más fácil». ¿Qué le respondes?", "Que conviene empezar por el efecto y el momento central, porque pueden cambiar las frases", "Que tiene razón, porque lo fácil siempre va primero", "Que no hay nada que revisar", "Lo global puede cambiar lo local; corregir primero lo fácil puede implicar rehacerlo."),
    sc=[
        ("En Taller de literatura: ¿qué mira una revisión local?", "Frases y palabras: conectores, repeticiones, ortografía", "La revisión local corrige detalles de redacción y ortografía."),
        ("ab", "El orden recomendado de revisión es:", "Primero lo global y después lo local", "Primero lo local y después lo global", "Resolver lo global evita pulir frases que luego se cortan."),
        ("ab", "Los comentarios de otras personas son:", "Insumos que se clasifican y se deciden", "Órdenes que se cumplen sin pensar", "Quien escribe decide qué acepta, con criterio y con pauta."),
    ],
    op=("Con el borrador y los comentarios de la ficha {F}: (1) clasifica R1, R2, R3 y R4 en global o local; (2) escribe en qué orden revisarías y por qué; (3) escribe una lista de tres cambios concretos que harías al borrador.",
        "(1) R1 local; R2 global; R3 local; R4 global. (2) Primero R2 y R4, porque definen el efecto y el momento central; luego R1 y R3, porque pulen frases. (3) Elegir un momento (el olor de los tomates), contarlo con tres detalles y reemplazar los «y» por puntos.",
        ["clasificación correcta de los cuatro comentarios", "orden justificado", "tres cambios concretos", "cambios coherentes con el orden"],
        ["clasificación, orden y lista de cambios"],
        ["orden sin justificar", "cambios vagos como «mejorar»", "empezar por lo local"],
        "Pregunta: «¿qué comentario cambiaría más tu texto y cuál menos?»."),
    reinforce="Escribe un comentario global y uno local que podrías recibir sobre un texto tuyo.",
    extend="Explica por qué un texto sin errores ortográficos puede seguir necesitando una revisión global.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (caso de ejemplo). Texto original: «Mi abuelo vendió el campo y yo estaba muy triste y me quedé callado.» Efecto buscado: que se sienta una pérdida sin nombrar la tristeza. "
     "Comentarios recibidos. K1) «Nombras la tristeza; podrías mostrarla con un gesto.» K2) «Agrega una descripción larga del campo.» K3) «Cambia el texto a un poema de doce versos.» K4) «El conector ‘y’ se repite dos veces.»")
build(
    O4, 2, F,
    use="Aprenderé a convertir los comentarios de otras personas en decisiones de reescritura: aceptar, adaptar o descartar con un criterio. Sirve para mejorar mi texto sin perder mi propósito.",
    prior=["Sé distinguir revisión global y local.", "Sé qué es el efecto buscado de un texto.", "Sé comentar con criterios."],
    explain=[
        "No todos los comentarios se aplican. Recibir una crítica no obliga a cambiarlo todo; obliga a decidir. Para cada comentario hay tres decisiones posibles: aceptar (se aplica tal cual), adaptar (se aplica a mi manera, cambiando la propuesta pero resolviendo el problema que señala) y descartar (no se aplica, con una razón). Decidir sin razón es dejarse llevar por el ánimo; decidir con razón es revisar.",
        "El criterio principal es el propósito del texto. Se pregunta: ¿este comentario ayuda a que mi texto logre el efecto que busco? Un comentario que señala un problema real del efecto se acepta o adapta. Un comentario que pide un texto distinto del que quiero escribir, como convertir un relato en poema, se descarta con respeto. A veces el problema que señala el comentario es válido, aunque la solución propuesta no lo sea: entonces se adapta.",
        "Una buena práctica es escribir una tabla de decisiones con cuatro columnas: el comentario, el problema que señala, la decisión (aceptar, adaptar, descartar) y la razón. Esa tabla ordena la reescritura y permite explicar a quien comentó qué hiciste con su aporte. Responder a quien comentó, con gratitud, es parte de la cultura de taller.",
    ],
    vocab=[("aceptar", "aplicar un comentario tal cual"), ("adaptar", "resolver el problema que señala un comentario con una solución propia"), ("descartar", "no aplicar un comentario, con una razón"), ("decisión de reescritura", "elección fundada sobre qué cambiar en el texto"), ("tabla de decisiones", "cuadro que registra comentarios, decisiones y razones")],
    worked=[
        ("Aceptar con razón", "K1 dice que nombras la tristeza y podrías mostrarla con un gesto. ¿Qué decisión tomas?",
         ["El efecto buscado es sentir la pérdida sin nombrar la tristeza.", "El texto nombra «muy triste», lo que contradice ese efecto.", "Acepto el comentario y cambio la tristeza por un gesto."],
         "Aceptar, porque contradice el efecto buscado"),
        ("Descartar con razón", "K3 propone convertir el texto en poema de doce versos. ¿Qué decisión tomas?",
         ["El proyecto es un relato breve y no un poema.", "Convertirlo cambiaría el género y el propósito.", "Descarto la propuesta, aunque agradezco la idea."],
         "Descartar, porque cambia el género del proyecto"),
    ],
    mistakes=[("Aplicar todos los comentarios sin pensar para «no quedar mal».", "El texto pierde su propósito si se obedece todo, incluso lo contradictorio.", "Decide con el efecto buscado como criterio y justifica cada decisión."),
              ("Descartar un comentario porque la solución propuesta no sirve, sin ver el problema.", "El problema señalado puede ser real aunque la solución sea otra.", "Pregúntate qué problema ve la persona y resuélvelo a tu manera.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué significa adaptar un comentario?", "Resolver el problema que señala con una solución propia", "Aplicarlo sin cambios", "Ignorarlo sin razón", "Adaptar es atender el problema señalado a tu manera."),
        ("{F} ¿Cuál es el efecto buscado del texto?", "Que se sienta una pérdida sin nombrar la tristeza", "La ficha declara ese efecto como propósito del texto."),
        ("{F} ¿Cuántas veces aparece el conector «y» en el texto original?", "2", "El texto dice «campo y yo» y «triste y me», es decir, dos veces."),
        ("abc", "{F} ¿Qué decisión conviene para K4, los «y» repetidos?", "Aceptarla: reemplazar algunos «y» por puntos", "Descartarla sin razón", "Agregar más ‘y’", "Es un problema local real de ritmo que se resuelve fácilmente."),
        ("abc", "{F} ¿Qué decisión conviene para K2, agregar una descripción larga del campo?", "Adaptarla: agregar un solo detalle concreto del campo", "Aceptarla tal cual", "Descartar toda descripción", "Un detalle conciso respeta el efecto sin alargar el texto; una descripción larga lo diluiría."),
        ("ab", "{F} Llega un comentario nuevo, K5: «Hazlo de cinco páginas». ¿Qué decisión conviene?", "Descartarlo: alargarlo tanto diluiría el efecto de sugerir la pérdida", "Aceptarlo: un texto más largo siempre es mejor", "El efecto buscado se logra con pocas palabras; el comentario no resuelve ningún problema de ese efecto."),
        ("abc", "{F} Si aceptas K1, ¿cuál es una reescritura adecuada?", "«Mi abuelo firmó los papeles sin soltar el sombrero»", "«Mi abuelo vendió el campo y yo estaba triste»", "«Qué triste fue todo»", "La primera muestra la pérdida con un gesto; las otras nombran la tristeza."),
        ("abc", "{F} Una compañera dice: «aplico todo lo que me dicen». ¿Qué problema puede traer?", "Aplicar comentarios contradictorios y perder el propósito del texto", "Mejorar el texto automáticamente", "Ser más rápida", "Sin criterio, los comentarios se contradicen y el texto pierde su dirección."),
        ("abc", "{F} ¿Qué columna de la tabla de decisiones justifica por qué descartas un comentario?", "La razón", "El comentario", "El problema", "La columna de razón explica la decisión tomada."),
        ("ab", "{F} Dos comentarios se contradicen: uno pide alargar y otro recortar. ¿Qué criterio decide?", "El efecto buscado del texto", "Cuántas personas lo dijeron", "La decisión se apoya en lo que el texto quiere lograr, no en una mayoría."),
        ("abc", "{F} El comentario K1 propone mostrar la tristeza con un gesto, pero tú prefieres un objeto. ¿Qué decisión tomas?", "Adaptarlo: mostrarla con un objeto, porque resuelve el mismo problema", "Descartarlo porque el gesto no es tu idea", "Aceptarlo tal cual", "El problema señalado es el de nombrar la tristeza; se resuelve con un objeto."),
        ("abc", "{F} ¿Qué haces con un comentario que no entiendes?", "Pedir a quien lo hizo que lo aclare con un ejemplo", "Descartarlo sin preguntar", "Aplicarlo al azar", "Pedir aclaración permite decidir con información."),
        ("abc", "{F} Quien comentó K3 se enoja porque no aplicaste su idea. ¿Qué haces?", "Explicarle con respeto la razón y agradecer su aporte", "Pelear con ella", "Cambiar todo el texto para complacerla", "Explicar y agradecer es parte de la cultura de taller."),
    ],
    ctx=("abc", "Contexto: recibes seis comentarios y solo tienes dos días para reescribir. ¿Cómo organizas el trabajo con el texto de la ficha {F}?", "Armo una tabla de decisiones, priorizo los comentarios globales y reservo tiempo para lo local", "Aplico los primeros tres que leí", "No hago nada porque son muchos", "La tabla permite priorizar con criterio y llegar a tiempo."),
    sc=[
        ("En Taller de literatura: ¿qué criterio principal decide si aplicar un comentario?", "El efecto o propósito buscado del texto", "El comentario se acepta si ayuda a lograr lo que el texto se propone."),
        ("ab", "Una decisión de reescritura debe llevar:", "Una razón", "Solo el ánimo del día", "Con razón la decisión se puede explicar y revisar."),
        ("ab", "Descartar un comentario es válido cuando:", "Se hace con una razón y con respeto", "Se hace sin pensarlo", "Descartar sin razón es dejar de revisar."),
    ],
    op=("Con la ficha {F}: arma una tabla de decisiones para K1, K2, K3 y K4 con estas columnas: problema que señala, decisión (aceptar, adaptar o descartar) y razón. Luego escribe tu versión reescrita del texto (una o dos oraciones) aplicando al menos dos decisiones.",
        "K1: problema, nombra la tristeza; decisión: aceptar; razón: contradice el efecto. K2: problema, falta ambiente; decisión: adaptar con un detalle; razón: una descripción larga distrae. K3: problema, ninguno real; decisión: descartar; razón: cambia el género. K4: problema, ritmo repetido; decisión: aceptar; razón: es un defecto de ritmo. Versión: «Mi abuelo firmó los papeles sin soltar el sombrero. Yo conté las tablas de la cerca».",
        ["tabla de cuatro comentarios", "decisión justificada en cada uno", "al menos dos decisiones aplicadas", "coherencia con el efecto buscado"],
        ["tabla y versión reescrita"],
        ["decisiones sin razón", "aplicar K3 sin ver el efecto", "versión que nombra la tristeza"],
        "Pregunta: «¿qué comentario te costó más decidir y por qué?»."),
    reinforce="Escribe una decisión de reescritura (aceptar, adaptar o descartar) con su razón para este comentario sobre tu texto: «agrega más personajes».",
    extend="Explica por qué rechazar una sugerencia con una razón fundada puede ser más respetuoso que aplicarla a medias.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (versiones originales de ejemplo). Versión 1: «Me dio mucha pena cuando mi abuelo vendió el campo. Estaba triste. Me quedé callado. Después fuimos a comer.» "
     "Versión 2: «Mi abuelo firmó los papeles sin soltar el sombrero. Yo conté las tablas de la cerca, una por una, hasta que me llamaron a comer.» Técnicas de reescritura: cortar, sustituir, reordenar, ampliar y cambiar el punto de vista.")
build(
    O4, 3, F,
    use="Aprenderé técnicas concretas de reescritura (cortar, sustituir, reordenar, ampliar y cambiar el punto de vista) y a aplicarlas según el efecto del texto. Sirve para pasar de comentarios a cambios reales en mis producciones.",
    prior=["Sé tomar decisiones sobre comentarios.", "Sé distinguir mostrar y decir.", "Sé qué es el punto de vista."],
    explain=[
        "Reescribir no es copiar con retoques: es tomar decisiones para acercar el texto a su efecto. Hay cinco técnicas básicas. Cortar elimina lo que no aporta. Sustituir cambia una expresión por otra más precisa o más concreta. Reordenar cambia el orden de las partes para mejorar la tensión o la claridad. Ampliar agrega un detalle o una escena cuando falta. Cambiar el punto de vista reescribe desde otra voz, por ejemplo de primera a tercera persona.",
        "Cada técnica resuelve un tipo de problema. Si el texto repite una idea, se corta. Si una emoción está nombrada y se busca mostrarla, se sustituye por una acción u objeto. Si el final llega sin preparación, se reordena o se amplía. Si la voz está demasiado cercana y se busca distancia, se cambia el punto de vista. Elegir la técnica correcta es parte de entender el problema.",
        "Entre la versión 1 y la 2 de la ficha se aplicaron varias técnicas: se cortó «me dio mucha pena», se sustituyó «estaba triste» por una acción con el sombrero y se amplió con la imagen de contar las tablas de la cerca. Conviene reescribir de a una técnica por vez y releer, para comprobar que el cambio mejora el efecto y no genera otro problema.",
    ],
    vocab=[("cortar", "eliminar lo que no aporta al efecto"), ("sustituir", "cambiar una expresión por otra más precisa o concreta"), ("reordenar", "cambiar el orden de las partes de un texto"), ("ampliar", "agregar un detalle o una escena que falta"), ("punto de vista", "voz desde la cual se cuenta el texto")],
    worked=[
        ("Elegir la técnica según el problema", "La versión 1 nombra «estaba triste». El efecto buscado es mostrar la tristeza. ¿Qué técnica usas?",
         ["El problema es una emoción nombrada.", "Se busca mostrarla con un gesto o un objeto.", "La técnica es sustituir la expresión por una acción concreta."],
         "Sustituir"),
        ("Aplicar una técnica y comprobarla", "Cortas «Después fuimos a comer.» de la versión 1. ¿Qué compruebas?",
         ["Relees el texto sin esa oración.", "El texto termina en «Me quedé callado», un cierre más fuerte.", "El cambio mejora el efecto, así que se mantiene."],
         "Que el corte mejora el cierre"),
    ],
    mistakes=[("Hacer varios cambios a la vez y no saber cuál mejoró o empeoró el texto.", "Con varios cambios juntos no se puede comprobar el efecto de cada uno.", "Aplica una técnica por vez y relee después de cada cambio."),
              ("Cortar una oración solo porque «parece sobrar», sin comprobar el efecto.", "Una oración puede sostener un detalle que da sentido a otra parte.", "Relee el texto sin la oración y decide si el efecto mejora.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué técnica de reescritura elimina lo que no aporta?", "Cortar", "Ampliar", "Reordenar", "Cortar elimina lo que no sirve al efecto."),
        ("{F} ¿Cuántas oraciones tiene la versión 1?", "4", "La versión 1 tiene cuatro oraciones: pena, triste, callado y comer."),
        ("{F} ¿Qué objeto aparece en la versión 2 y no en la versión 1?", "El sombrero", "La versión 2 menciona el sombrero del abuelo."),
        ("abc", "{F} Otra estudiante cambia «caminaba muy mal» por «arrastraba el pie derecho». ¿Qué técnica usó?", "Sustituir", "Cortar", "Reordenar", "Cambió una expresión vaga por otra más concreta, que es sustituir."),
        ("abc", "{F} ¿Qué técnica se usó al agregar «Yo conté las tablas de la cerca, una por una»?", "Ampliar", "Cortar", "Cambiar el punto de vista", "Se agregó una imagen que no estaba en la versión 1."),
        ("ab", "{F} ¿Qué técnica se usó al eliminar «Me dio mucha pena»?", "Cortar, porque la emoción ya se sugiere en otras partes", "Reordenar, porque se cambió el orden", "Se eliminó una expresión que nombraba la emoción, o sea, un corte."),
        ("abc", "{F} Quieres que el texto empiece con el gesto del abuelo y termine con la comida. ¿Qué técnica usas para pasar a ese orden?", "Reordenar", "Cortar", "Sustituir", "Cambiar el orden de las partes es reordenar."),
        ("abc", "{F} Quieres que la versión 2 se cuente desde fuera, con mayor distancia. ¿Cuál reescritura cambia el punto de vista?", "«El abuelo firmó los papeles sin soltar el sombrero. El niño contó las tablas de la cerca»", "«Yo firmé los papeles»", "«Mi abuelo firmó los papeles»", "Solo la primera pasa de primera persona a tercera persona."),
        ("abc", "{F} Una compañera propone ampliar la versión 2 con una larga descripción del campo. ¿Qué riesgo tiene?", "Que se diluya el efecto de sugerencia", "Que quede demasiado corto", "Que no se pueda leer", "Una descripción larga puede quitar fuerza a la sugerencia."),
        ("=", "{F} Una versión de un borrador tenía 150 palabras y debe quedar en 120. ¿Cuántas palabras hay que cortar?", "150-120", "Se resta la extensión final de la inicial.", " palabras"),
        ("=", "{F} Se cortaron 18 palabras de un texto de 150. ¿Cuántas palabras tiene ahora?", "150-18", "Se resta lo cortado a la extensión inicial.", " palabras"),
        ("abc", "{F} ¿Qué haces después de aplicar una técnica?", "Releer para comprobar el efecto", "Pasar a otra técnica sin releer", "Entregar el texto", "Releer permite saber si el cambio mejoró lo que el texto busca."),
        ("abc", "{F} Una estudiante reemplazó «Estaba triste» por «Estaba muy triste y sin ganas». ¿Qué ocurre?", "Sigue nombrando la emoción, así que no se logró mostrarla", "Mostró la emoción con un gesto", "Cortó el texto", "Agregar adjetivos a una emoción nombrada no la convierte en imagen."),
    ],
    ctx=("abc", "Contexto: el texto de la ficha {F} se leerá en un acto del liceo y se pidió un máximo de 30 palabras. La versión 2 tiene 25. ¿Qué decisión conviene?", "Mantenerla, porque cumple el límite y conserva el efecto", "Cortar hasta tener 10 palabras", "Ampliarla hasta 60 palabras", "Cumple la extensión pedida y logra el efecto; no hace falta cortar ni ampliar."),
    sc=[
        ("En Taller de literatura: ¿qué técnica agrega un detalle o una escena que falta?", "Ampliar", "Ampliar añade lo que falta para completar el efecto."),
        ("ab", "Conviene reescribir:", "Una técnica por vez, releyendo", "Todo a la vez sin releer", "Así se comprueba qué cambio mejora el texto."),
        ("ab", "Cambiar el punto de vista implica:", "Contar desde otra voz, como pasar de primera a tercera persona", "Cambiar solo la letra del texto", "El punto de vista es la voz que cuenta."),
    ],
    op=("Toma la versión 1 de la ficha {F}. Reescríbela aplicando al menos tres de las cinco técnicas (cortar, sustituir, reordenar, ampliar, cambiar el punto de vista), con un máximo de 40 palabras. Después escribe qué técnica aplicaste en cada cambio y por qué.",
        "Reescritura: «Mi abuelo firmó los papeles. Yo me quedé mirando el sombrero que no soltaba. Después, en silencio, comí.» Técnicas: cortar «me dio mucha pena»; sustituir «triste» por mirar el sombrero; reordenar el orden de los hechos.",
        ["reescritura propia de máximo 40 palabras", "al menos tres técnicas", "cada técnica identificada", "razón de cada cambio"],
        ["texto reescrito y lista de técnicas"],
        ["copiar la versión 2", "superar las 40 palabras", "no explicar la razón de cada cambio"],
        "Pregunta: «¿qué técnica mejoró más el texto y cuál lo mejoró menos?»."),
    reinforce="Aplica la técnica de cortar a esta oración: «Estaba muy muy cansada y no tenía fuerzas para nada de nada» y explica qué efecto se logra.",
    extend="Explica por qué cambiar el punto de vista modifica el efecto de un texto y no solo su forma.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (versiones y pauta de ejemplo). V1: «Mi abuelo vendió el campo y yo estaba muy triste y me quedé callado.» "
     "V2: «Mi abuelo firmó los papeles sin soltar el sombrero. Yo conté las tablas de la cerca hasta que me llamaron a comer.» "
     "Pauta del proyecto. P1) incluye un objeto pequeño y concreto, distinto del hecho principal; P2) no pasa de 30 palabras; P3) no nombra la emoción directamente. Bitácora de cambios: columnas Cambio, Razón y Criterio.")
build(
    O4, 4, F,
    use="Aprenderé a comparar versiones de un texto con una pauta, a llevar una bitácora de cambios y a decidir cuándo una reescritura está lista, también para producciones orales o audiovisuales. Sirve para enriquecer mi producción creativa con evidencia de mejora.",
    prior=["Sé aplicar técnicas de reescritura.", "Sé decidir qué hacer con un comentario.", "Sé comparar versiones con criterios."],
    explain=[
        "Reescribir termina cuando se comprueba que la nueva versión mejora la anterior. Esa comprobación se hace con la pauta: se aplica cada criterio a las dos versiones y se cuenta cuántos cumple cada una. En la ficha, la V1 cumple P2 (tiene 14 palabras) pero no P1 ni P3; la V2 cumple los tres criterios. Esa comparación es evidencia de mejora, no una impresión.",
        "La bitácora de cambios registra qué se modificó, por qué y con qué criterio. Sirve para recordar las decisiones, para explicarlas a quien comentó y para no deshacer por error una mejora. Por ejemplo: «cambio: sustituir ‘estaba muy triste’ por el sombrero; razón: mostrar la emoción; criterio: P3». Con la bitácora, la reescritura es un proceso visible.",
        "Las producciones orales y audiovisuales también se reescriben. Una lectura en voz alta se revisa grabándola o ensayándola ante alguien: se miden el tiempo, el ritmo, las pausas y la claridad. Un guion de video se revisa por tiempo, claridad y relación entre imagen y voz. En todos los casos hay que decidir cuándo parar: una reescritura está lista cuando cumple la pauta y no mejora de modo visible con otro cambio.",
    ],
    vocab=[("bitácora de cambios", "registro de qué se cambió, por qué y con qué criterio"), ("evidencia de mejora", "comparación con la pauta que muestra que la versión nueva cumple más criterios"), ("versión", "forma de un texto en un momento del proceso"), ("lectura en voz alta", "presentación del texto leyéndolo"), ("ensayo", "práctica previa de una presentación")],
    worked=[
        ("Comparar con la pauta", "¿Cuántos criterios cumple cada versión de la ficha?",
         ["V1: P2 sí (14 palabras); P1 no; P3 no, porque nombra «muy triste». Cumple 1.", "V2: P1 sí (sombrero y tablas); P2 sí (22 palabras); P3 sí. Cumple 3."],
         "V1 cumple 1 criterio y V2 cumple 3"),
        ("Llenar una bitácora", "Registra el cambio de «estaba muy triste» por «sin soltar el sombrero».",
         ["Cambio: sustituir una emoción nombrada por un gesto con un objeto.", "Razón: mostrar la emoción sin nombrarla.", "Criterio: P3."],
         "Cambio, razón y criterio P3"),
    ],
    mistakes=[("Reescribir sin conservar la versión anterior ni registrar los cambios.", "No se puede comprobar la mejora ni volver atrás si un cambio empeora el texto.", "Guarda cada versión y anota los cambios en una bitácora."),
              ("Seguir cambiando el texto sin parar aunque ya cumple la pauta.", "Cambios sin criterio pueden empeorar el texto y no terminan nunca.", "Termina cuando cumple la pauta y otro cambio no mejora de modo visible.")],
    T=[
        ("abc", "En Taller de literatura: ¿qué registra una bitácora de cambios?", "Qué se cambió, por qué y con qué criterio", "Solo la nota final", "La lista de comentarios descartados sin razones", "La bitácora hace visible el proceso de reescritura."),
        ("=", "{F} V2 tiene 22 palabras y la pauta permite 30. ¿Cuántas palabras de margen quedan?", "30-22", "Se resta la extensión de V2 al máximo de la pauta.", " palabras"),
        ("{F} Una V3 dice: «Mi abuelo vendió el campo y yo estaba muy triste mirando su sombrero colgado.» Tiene 14 palabras. ¿Cuántos criterios de la pauta cumple?", "2", "Cumple P1 (el sombrero) y P2 (14 palabras), pero incumple P3 porque nombra «muy triste»."),
        ("abc", "{F} ¿Qué criterio incumple V1 al decir «estaba muy triste»?", "P3, no nombrar la emoción", "P1, porque es larga", "P2, porque pasa de 30 palabras", "Nombra la tristeza, lo que contradice P3."),
        ("abc", "{F} ¿Qué detalle concreto de V2 cumple P1?", "El sombrero que el abuelo no suelta", "La palabra ‘papeles’ sola", "El título del texto", "El sombrero es un objeto que se puede imaginar con los sentidos."),
        ("abc", "{F} Una V4 dice: «Mi abuelo vendió el campo. Yo conté las tablas de la cerca, una por una, y sentí mucha tristeza.» ¿Qué criterio incumple?", "P3, porque nombra la emoción", "P1, porque no tiene un objeto concreto", "P2, porque pasa de 30 palabras", "Nombra «mucha tristeza», lo que contradice P3; tiene un objeto (las tablas) y menos de 30 palabras."),
        ("abc", "{F} Una estudiante dice que V2 es mejor porque «suena lindo». ¿Qué falta en su argumento?", "La comparación con la pauta y la evidencia de cada criterio", "Una opinión más fuerte", "Más palabras en V2", "La mejora se demuestra con la pauta, no con el gusto."),
        ("abc", "{F} ¿Qué entrada de bitácora corresponde a agregar «Yo conté las tablas de la cerca»?", "Cambio: ampliar con las tablas de la cerca; razón: dar una imagen concreta; criterio: P1", "Cambio: sin cambio; razón: ninguna", "Cambio: cortar todo el texto", "La entrada dice qué se cambió, por qué y con qué criterio."),
        ("abc", "{F} Una estudiante agrega a V2 una segunda oración de 20 palabras. ¿Qué pasa con P2?", "Se pasa del límite: 22 más 20 son 42 palabras", "Sigue cumpliendo porque no hay límite", "Queda en 22 palabras", "La suma supera las 30 palabras permitidas."),
        ("ab", "{F} Para una lectura en voz alta de V2, ¿qué conviene hacer antes?", "Ensayar ante alguien para medir ritmo y pausas", "Leerla por primera vez frente al público", "El ensayo permite detectar frases difíciles y ajustar el ritmo."),
        ("abc", "{F} Un guion de video basado en V2 dura 15 segundos y la pauta pide un máximo de 10 segundos. ¿Qué técnica de reescritura corresponde?", "Cortar", "Ampliar", "Cambiar el punto de vista", "Hay que reducir el tiempo, lo que se logra eliminando lo que no aporta."),
        ("abc", "{F} V2 ya cumple las tres condiciones. Alguien propone cambiarla por completo. ¿Qué respondes?", "Que no es necesario si cumple la pauta y otro cambio no mejoraría de forma visible", "Que siempre hay que cambiar todo", "Que se debe empezar de nuevo sin razón", "Una versión que cumple la pauta puede darse por terminada."),
        ("=", "{F} La bitácora tiene 8 cambios; 5 se aplicaron en la V2 y el resto está pendiente. ¿Cuántos están pendientes?", "8-5", "Se restan los cambios aplicados al total registrado.", " cambios"),
    ],
    ctx=("abc", "Contexto: tu grupo debe presentar al curso, además de la versión final, la evidencia de cómo mejoró el texto de la ficha {F}. ¿Qué entregan?", "V1, V2, la pauta con la comparación y la bitácora de cambios", "Solo V2", "Solo la nota final", "Presentar ambas versiones, la pauta y la bitácora muestra la mejora con evidencia."),
    sc=[
        ("En Taller de literatura: ¿cuándo se da por terminada una reescritura?", "Cuando cumple la pauta y otro cambio no mejora de modo visible", "Una reescritura se detiene cuando se cumple la pauta y no hay mejora evidente."),
        ("ab", "La mejora de una versión se demuestra:", "Comparándola con la pauta", "Diciendo que es mejor", "La comparación con criterios es evidencia."),
        ("ab", "Una lectura en voz alta se revisa:", "Ensayándola y midiendo tiempo y ritmo", "Sin escucharla nunca", "El ensayo permite ver el tiempo, las pausas y la claridad."),
    ],
    op=("Elige V1 o V2 de la ficha {F} para trabajar. (1) Escribe una V3 que cumpla las tres condiciones de la pauta, distinta de V2; (2) cuenta las palabras de tu V3 y comprueba P2; (3) llena una bitácora de tres cambios con las columnas Cambio, Razón y Criterio.",
        "V3: «El abuelo firmó con la mano libre; con la otra apretaba el sombrero. Yo miré el columpio de la cerca hasta que me llamaron a comer.» Palabras: 26. P1 columpio y sombrero, P2 26 menor que 30, P3 sin emoción nombrada. Bitácora: sustituir tristeza por gesto, criterio P3; ampliar con columpio, criterio P1; cortar «me quedé callado», criterio P3.",
        ["V3 propia y distinta de V2", "conteo correcto de palabras", "cumple P1, P2 y P3", "bitácora de tres cambios con razón y criterio"],
        ["V3, conteo y bitácora"],
        ["copiar V2", "conteo incorrecto", "bitácora sin criterio"],
        "Pregunta: «¿qué cambio de tu V3 es el más importante y por qué?»."),
    reinforce="Escribe una pauta de tres condiciones para evaluar una lectura en voz alta de un poema tuyo.",
    extend="Explica por qué conservar las versiones anteriores y la bitácora hace más confiable la mejora de un texto.",
)
