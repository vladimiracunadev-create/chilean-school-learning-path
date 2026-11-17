"""Estética (electivo HC, 3.º y 4.º medio): OAC-06 (dialogar sobre la función del arte y la experiencia estética) y OAC-07 (visión personal sobre la influencia de la sociedad y la cultura actual en la sensibilidad), clases 1 a 4 de cada OA."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada texto, caso o ficha está escrito en el enunciado. "
             "Los textos filosóficos son resúmenes originales de posturas y las obras de arte son casos ficticios descritos con palabras: no se reproducen obras con derechos ni se usan imágenes o audio. "
             "Las posturas se presentan con sus razones y sin tomar partido: tu tarea es analizar y evaluar. Si tu docente propone mirar o escuchar una obra real, hazlo en sala y con las pautas que él o ella indique. "
             "En los temas de moral, política o bienestar emocional se usan casos ficticios; si algo te afecta, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O6 = "FI-ESTE-3y4-OAC-06"

# ============================================================ OAC-06, clase 1
F = ("Ficha 26 (diálogo ficticio de un club de lectura). Valentina: «El arte sirve para expresar lo que sentimos y no sabemos decir.» "
     "Diego: «Sirve para conocer cosas que de otro modo no veríamos, como la vida de otras personas.» "
     "Sofía: «Sirve para unir a la comunidad: pensemos en las fiestas, los cantos y los murales del barrio.» "
     "Tomás: «Quizá no sirve para nada, y justamente eso es valioso: se disfruta por sí mismo.» "
     "Funciones posibles del arte: expresar, conocer, comunicar, entretener, criticar, conmemorar, unir a una comunidad.")
build(
    O6, 1, F,
    use="Aprenderé a plantear la pregunta por la función del arte y de la experiencia estética en la cultura, a distinguir visiones personales y colectivas y a reconocer qué razón da cada una.",
    prior=["Reconstruyo posturas con tesis y razones.", "Conozco propósitos de la creación artística.", "Sé evaluar argumentos simples."],
    explain=[
        "La función del arte es aquello para lo que sirve o lo que hace en la vida de las personas y de una cultura. Se han propuesto varias: expresar emociones, conocer realidades, comunicar ideas, entretener, criticar, conmemorar o unir a una comunidad. Una misma obra puede cumplir varias funciones a la vez, y distintas personas pueden valorar funciones distintas.",
        "Hay también quien sostiene que el arte vale por sí mismo, aunque no «sirva» para nada: su valor estaría en la experiencia estética que ofrece. Esta postura no niega que el arte pueda tener efectos, pero dice que su valor no depende de ellos. Dialogar sobre esto exige distinguir entre lo que el arte hace y lo que el arte vale.",
        "Una visión personal es la que cada quien elabora con sus razones y experiencias. Una visión colectiva es la que un grupo construye al conversar, reconociendo acuerdos y desacuerdos. No son opuestas: la visión colectiva se enriquece con visiones personales bien argumentadas, y la personal mejora al escuchar a otras personas.",
    ],
    vocab=[("función del arte", "lo que el arte hace o aporta en la vida de las personas y de una cultura"), ("valor intrínseco", "valor que algo tiene por sí mismo, no por su utilidad"), ("visión personal", "la que una persona elabora con sus razones y experiencias"), ("visión colectiva", "la que un grupo construye al conversar"), ("diálogo filosófico", "conversación en que se preguntan, se dan y se evalúan razones")],
    worked=[
        ("Reconocer una función", "Sofía dice: «El arte sirve para unir a la comunidad». ¿Qué función propone?",
         ["Busca qué hace el arte según Sofía: reunir a las personas.", "Esa función es unir a una comunidad."],
         "Unir a una comunidad"),
        ("Distinguir hacer y valer", "Tomás dice: «Se disfruta por sí mismo». ¿Qué postura expresa?",
         ["Observa que no menciona un efecto: dice que se disfruta por sí mismo.", "Defiende que el arte tiene valor intrínseco."],
         "Que el arte tiene valor intrínseco"),
    ],
    mistakes=[("Creer que el arte tiene una sola función.", "Se simplifica lo que una obra puede hacer.", "Pregunta qué funciones puede cumplir una misma obra."),
              ("Confundir lo que el arte hace con lo que el arte vale.", "Se mezcla efecto con valor.", "Distingue la función (lo que hace) del valor (lo que vale).")],
    T=[
        ("abc", "{F} ¿Qué función propone Valentina?", "Expresar lo que sentimos", "Conocer otras vidas", "Unir a la comunidad", "Valentina dice que el arte sirve para expresar lo que sentimos."),
        ("abc", "{F} ¿Qué función propone Diego?", "Conocer cosas que de otro modo no veríamos", "Entretener", "Criticar", "Diego habla de conocer la vida de otras personas."),
        ("abc", "{F} ¿Qué respondería Tomás a quien dice «un mural que no sirve para nada no tiene valor»?", "Que puede valer por la experiencia que ofrece, aunque no «sirva»", "Que el mural debe dejar de pintarse", "Que solo vale si une a la comunidad", "Tomás sostiene que el arte se disfruta por sí mismo, sin depender de su utilidad."),
        ("En Estética: ¿cómo se llama el valor que algo tiene por sí mismo, no por su utilidad?", "Valor intrínseco", "Es el nombre de ese tipo de valor."),
        ("abc", "{F} ¿Qué ejemplo da Sofía para sostener su idea?", "Las fiestas, los cantos y los murales del barrio", "Las pinturas de museo", "Las clases de música del liceo", "Sofía da ejemplos de arte comunitario."),
        ("ab", "{F} ¿Cuál de las visiones de la ficha es más colectiva?", "La de Sofía, porque habla de la comunidad", "La de Valentina, porque habla de sentimientos", "Sofía se refiere a lo que el arte hace entre las personas, mientras Valentina habla de lo personal."),
        ("abc", "Una escuela ficticia usa un mural para recordar a sus ex estudiantes. ¿Qué función cumple principalmente?", "Conmemorar", "Entretener", "Criticar", "Recordar a personas con una obra es una forma de conmemorar."),
        ("abc", "Una canción ficticia denuncia la contaminación de un río. ¿Qué función cumple principalmente?", "Criticar", "Conmemorar", "Entretener", "Señala un problema y lo cuestiona."),
        ("abc", "{F} Un estudiante dice: «Si el arte vale por sí mismo, no puede unir a la comunidad». ¿Qué falla?", "Un arte con valor propio también puede tener efectos, como unir a la comunidad", "Que el valor intrínseco no existe", "Que lo que vale por sí mismo no puede tener efectos", "Valor intrínseco y función no se excluyen."),
        ("abc", "{F} Otra estudiante dice: «Sofía y Tomás no pueden coincidir en nada». ¿Qué corrección es mejor?", "Pueden coincidir en que el arte es importante para las personas, aunque den razones distintas", "Tiene razón", "Ambos piensan lo mismo", "Se puede coincidir en lo valioso y discrepar en el porqué."),
        ("abc", "{F} Si una obra ficticia nos lleva a conocer la vida de personas lejanas y además nos emociona, ¿qué se puede decir?", "Cumple al menos dos funciones: conocer y expresar o conmover", "Cumple solo una función", "Cumple una función y pierde su valor", "Una obra puede cumplir varias funciones a la vez."),
        ("abc", "{F} ¿Qué pregunta sirve para empezar un diálogo sobre la función del arte?", "¿Qué hace el arte por las personas y qué vale aunque no «sirva»?", "¿Cuál de las funciones del arte es la única correcta?", "¿Qué obras de arte son las más caras?", "Invita a considerar función y valor."),
        ("abc", "{F} Una visión colectiva sobre la función del arte debería…", "Reunir razones de las personas y reconocer acuerdos y desacuerdos", "Silenciar a quien piense distinto", "Repetir lo que diga la primera persona", "La visión colectiva se construye conversando."),
    ],
    ctx=("abc", "En un centro cultural ficticio, un vecino dice que el teatro comunitario debe cerrar porque «no sirve para nada». ¿Qué responde alguien que piensa que el arte tiene función y valor?", "Que el teatro puede unir al barrio, expresar emociones y además vale por la experiencia que ofrece", "Que el teatro solo vale si sirve para algo", "Que el teatro es un pasatiempo sin importancia", "Reconoce tanto las funciones sociales del teatro como su valor por sí mismo."),
    sc=[
        ("En Estética: ¿qué es la función del arte?", "Lo que el arte hace o aporta en la vida de las personas y de una cultura", "No es lo mismo que su valor."),
        ("¿Qué es el valor intrínseco?", "El valor que algo tiene por sí mismo, no por su utilidad", "Tomás defendía este valor al decir que el arte se disfruta por sí mismo."),
        ("¿En qué se diferencian una visión personal y una colectiva?", "La personal la elabora una persona y la colectiva la construye un grupo al conversar", "La visión colectiva se enriquece con las personales y viceversa."),
    ],
    op=("Elige una función del arte de la lista de la ficha y escribe tu visión personal en cinco líneas: tu tesis, una razón, un ejemplo (puede ser una obra ficticia), una objeción que alguien podría hacerte y tu respuesta. "
        "Termina con una pregunta para tu grupo.",
        "Función: unir a una comunidad. Tesis: el arte vale porque nos hace sentir parte de algo. Razón: en una fiesta con música todos participan. Ejemplo: una fiesta de barrio ficticia con un coro. Objeción: también se puede ir solo a un museo. Respuesta: aun así, el arte puede unir sin que todos estén presentes. Pregunta: ¿qué otras funciones tiene una fiesta?",
        ["tesis clara", "razón y ejemplo", "objeción y respuesta", "una pregunta abierta para el grupo"],
        ["visión personal de cinco líneas"],
        ["no incluir razón", "dar un ejemplo sin relación con la tesis", "no considerar ninguna objeción"],
        "Pregunta: «¿tu ejemplo apoya tu tesis o solo la decora?». Pídele que lo explique en una frase."),
    reinforce="Pregunta a una persona de tu casa para qué sirve el arte y anota su razón en dos líneas, sin juzgarla.",
    extend="Explica por qué una persona puede valorar el arte por sí mismo y también por sus funciones sociales.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 27 (diálogo con errores y glosario). Diálogo en una clase ficticia sobre si el arte debería enseñarse en todos los cursos. "
     "Camila: «Creo que sí, porque ayuda a expresar emociones.» "
     "Nicolás: «Tú dices eso porque eres de las que pintan, o sea que no cuenta.» "
     "Camila: «Bueno, ¿y tú por qué crees que no?» "
     "Nicolás: «Porque hay cosas más importantes. Y todos saben que el arte es solo para ratos libres.» "
     "Glosario: preguntar para aclarar = pedir que alguien explique o precise; parafrasear = decir con otras palabras lo que otra persona dijo; ejemplificar = dar un caso concreto; objetar con respeto = señalar un problema en una razón sin atacar a la persona; acuerdo = coincidencia en una idea; desacuerdo razonable = diferencia en que ambas partes dan razones; consenso = acuerdo logrado por un grupo.")
build(
    O6, 2, F,
    use="Aprenderé a definir y usar reglas del diálogo filosófico (preguntar, parafrasear, ejemplificar, objetar con respeto, acordar y discrepar) para conversar sobre la función del arte.",
    prior=["Conozco funciones del arte y valor intrínseco.", "Distingo ataque a la persona de crítica a las razones.", "Sé formular una objeción."],
    explain=[
        "Un diálogo filosófico es una conversación en que las personas se preguntan, dan razones y las evalúan en conjunto. No busca ganar, sino entender mejor un problema. Para lograrlo se usan acciones sencillas: preguntar para aclarar, parafrasear lo que dijo otra persona, ejemplificar con casos concretos y objetar con respeto.",
        "Parafrasear ayuda a comprobar que se entendió bien: «Si entiendo bien, tú dices que…». Objetar con respeto es señalar un problema en una razón, no en la persona: «Esa razón no considera que…». Un ataque a la persona, como «dices eso porque eres de tal grupo», aleja la conversación de las razones y suele cerrarla.",
        "Un buen diálogo reconoce acuerdos y desacuerdos. Un desacuerdo razonable es una diferencia en que ambas partes ofrecen razones y escuchan. A veces se alcanza un consenso, un acuerdo del grupo; otras veces se acuerda que existen visiones distintas y se dejan claras las razones de cada una. Ambos resultados son valiosos.",
    ],
    vocab=[("diálogo filosófico", "conversación en que se preguntan, se dan y se evalúan razones"), ("parafrasear", "decir con otras palabras lo que otra persona dijo"), ("objetar con respeto", "señalar un problema en una razón sin atacar a la persona"), ("desacuerdo razonable", "diferencia en que ambas partes ofrecen razones y escuchan"), ("consenso", "acuerdo logrado por un grupo")],
    worked=[
        ("Reconocer un ataque a la persona", "Nicolás dice: «Tú dices eso porque eres de las que pintan, o sea que no cuenta». ¿Qué error comete?",
         ["Observa que no examina la razón de Camila, sino algo de ella.", "Es un ataque a la persona."],
         "Ataque a la persona"),
        ("Parafrasear", "Parafrasea la frase de Camila «El arte ayuda a expresar emociones».",
         ["Cambia las palabras sin cambiar el sentido.", "«Si entiendo bien, dices que el arte nos permite sacar lo que sentimos.»"],
         "Si entiendo bien, dices que el arte nos permite sacar lo que sentimos"),
    ],
    mistakes=[("Responder a una persona atacando algo de ella en vez de su razón.", "Se confunde discutir con ganar.", "Objeta la razón, no a la persona."),
              ("Dar por hecho que todos piensan lo mismo, como en «todos saben que…».", "Se sustituyen las razones por una supuesta unanimidad.", "Sustituye esa frase por una razón concreta y un ejemplo.")],
    T=[
        ("abc", "{F} ¿Qué hace Camila al decir «¿y tú por qué crees que no?»", "Pregunta para aclarar la razón de Nicolás", "Ataca a Nicolás", "Parafrasea a Nicolás", "Camila pide a Nicolás que explique la razón de su postura."),
        ("abc", "{F} ¿Qué error comete Nicolás con «todos saben que el arte es solo para ratos libres»?", "Reemplaza la razón por una supuesta unanimidad", "Pregunta para aclarar", "Ejemplifica", "Nicolás no ofrece una razón sino una supuesta unanimidad."),
        ("abc", "{F} ¿Cómo podría Nicolás objetar con respeto la razón de Camila?", "«Entiendo que ayuda a expresar emociones, pero no sé si eso justifica ponerlo en todos los cursos»", "«Tú no sabes»", "«Todos saben que no»", "Señala un problema en la razón sin atacar."),
        ("En Estética: ¿cómo se llama decir con otras palabras lo que otra persona dijo?", "Parafrasear", "Es la acción que ayuda a comprobar que se entendió."),
        ("abc", "{F} ¿Cuál es un ejemplo que Camila podría dar para apoyar su razón?", "Una canción ficticia que ayuda a un grupo a expresar la tristeza por una pérdida", "Una cifra sobre el costo de los materiales", "Una opinión sobre el curso de Nicolás", "Un ejemplo concreto de expresión de emociones."),
        ("ab", "{F} Camila dice: «Si entiendo bien, para ti hay temas más urgentes que el arte, ¿es así?». ¿Qué hace?", "Parafrasea lo que dijo Nicolás para comprobar que lo entendió", "Ataca a la persona", "Reformula con otras palabras la idea de Nicolás y pregunta si lo entendió bien."),
        ("abc", "{F} Si Camila y Nicolás concluyen: «Ambos pensamos que el arte es importante, pero discrepamos en si debe estar en todos los cursos», ¿qué lograron?", "Reconocer un acuerdo parcial y un desacuerdo razonable", "Un consenso total", "Un ataque a la persona", "Identifican lo que comparten y lo que no."),
        ("abc", "{F} ¿Qué cambio haría más respetuosa la frase «Tú dices eso porque eres de las que pintan»?", "«Tu razón se apoya en tu experiencia; ¿qué pasaría con quien no pinta?»", "«Tú siempre dices lo mismo»", "«No digas nada»", "Pasa del ataque a la razón."),
        ("abc", "{F} Camila quiere invitar a Nicolás a dar un ejemplo. ¿Qué pregunta le conviene?", "¿Puedes dar un caso concreto en que el arte quite tiempo de cosas más importantes?", "¿Por qué eres así?", "¿Quién te enseñó?", "La pregunta le pide a Nicolás un ejemplo concreto de su afirmación."),
        ("abc", "{F} Un estudiante dice: «Dialogar es ganar la discusión». ¿Qué corrección es mejor?", "Dialogar busca entender mejor un problema con razones, no ganar", "Tiene razón", "Dialogar es repetir lo que uno piensa", "El diálogo filosófico busca comprender mejor un problema, no ganar una discusión."),
        ("abc", "{F} Camila propone: «Hagamos una lista con dos razones a favor y dos en contra de enseñar arte en todos los cursos». ¿Qué ayuda eso a lograr?", "Que el grupo vea las razones antes de decidir", "Que gane quien tenga más razones", "Que se evite el desacuerdo", "Ordenar razones a favor y en contra ayuda a ver el problema completo."),
        ("abc", "{F} Un grupo no logró consenso, pero dejó por escrito las razones de cada posición. ¿Fue un buen diálogo?", "Sí: dejó claras las razones y los desacuerdos razonables", "No: sin consenso, nada vale", "Sí: ganó una persona", "Un resultado valioso es esclarecer las diferencias."),
        ("abc", "{F} ¿Qué acción mejora más rápido un diálogo que se está volviendo agresivo?", "Parafrasear lo que dijo la otra persona y preguntar por su razón", "Subir la voz", "Interrumpir", "Parafrasear y preguntar baja la tensión y aclara."),
    ],
    ctx=("abc", "En una asamblea ficticia de curso se discute si el liceo debe tener un taller de arte. Un estudiante dice: «Eso es de gente rara». ¿Qué respuesta mantiene el diálogo filosófico?", "«¿Qué razón tienes para pensar que el taller no sirve? ¿Puedes dar un ejemplo?»", "«Tú sí que eres raro»", "«Todos saben que eso es cierto»", "Pregunta por la razón en lugar de descalificar."),
    sc=[
        ("En Estética: ¿qué es objetar con respeto?", "Señalar un problema en una razón sin atacar a la persona", "Objetar con respeto se centra en las razones y no en la persona."),
        ("¿Qué es un desacuerdo razonable?", "Una diferencia en que ambas partes ofrecen razones y escuchan", "Un desacuerdo razonable puede quedar abierto sin llegar a un consenso."),
        ("¿Para qué sirve parafrasear?", "Para comprobar que se entendió bien lo que dijo otra persona", "Parafrasear permite comprobar que se entendió y evita malentendidos."),
    ],
    op=("Escribe un diálogo de ocho turnos entre dos personas sobre esta pregunta: «¿Debería el arte ser parte obligatoria de la educación?». En tu diálogo deben aparecer al menos una pregunta para aclarar, una paráfrasis, un ejemplo concreto y una objeción respetuosa. "
        "Al final, escribe una frase con lo que acordaron y lo que sigue en desacuerdo.",
        "A: Creo que sí, porque el arte ayuda a expresar emociones. B: ¿Puedes dar un ejemplo? A: Un coro ficticio que ayuda a un curso a superar una pena. B: Si entiendo bien, dices que expresa lo que cuesta decir. A: Sí. B: Entiendo, pero no sé si eso justifica que sea obligatorio... Acuerdo: el arte es importante. Desacuerdo: si debe ser obligatorio.",
        ["incluye pregunta, paráfrasis, ejemplo y objeción respetuosa", "no hay ataques a la persona", "la frase final reconoce acuerdo y desacuerdo", "las razones se distinguen de las opiniones"],
        ["diálogo de ocho turnos y frase final"],
        ["dar solo opiniones sin razones", "incluir ataques a la persona", "cerrar con un falso consenso"],
        "Pregunta: «¿en qué turno aparece la paráfrasis?». Pídele que lo marque."),
    reinforce="Observa una conversación de tu casa o de un recreo y anota una vez en que alguien parafraseó o preguntó para aclarar.",
    extend="Explica por qué un diálogo sin consenso puede ser valioso para quienes participan.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 28 (transcripción de un diálogo ficticio). Tema: «¿Debería el liceo gastar su presupuesto de cultura en un mural, en un taller de música o en entradas a un museo?» "
     "Elena: «El mural, porque queda para siempre y lo ve todo el liceo.» "
     "Hugo: «El taller de música, porque permite que el estudiantado haga arte y no solo mire.» "
     "Inés: «Las entradas al museo, porque se conoce arte que el liceo no tiene.» "
     "Elena: «Hugo, entiendo que hacer arte es importante; ¿el taller llegaría a todo el liceo?» "
     "Hugo: «Quizá a menos personas, pero con experiencias más profundas.» "
     "Inés: «Podríamos combinar: un mural pintado por el taller con visitas al museo para inspirarse.»")
build(
    O6, 3, F,
    use="Aprenderé a reconstruir las perspectivas de un diálogo: qué propone cada persona, qué valora, en qué coinciden y en qué se separan, y qué propuestas intermedias aparecen.",
    prior=["Conozco las reglas del diálogo filosófico.", "Reconstruyo tesis y razones.", "Distingo acuerdo y desacuerdo razonable."],
    explain=[
        "Reconstruir las perspectivas de un diálogo es hacer un mapa de quién propone qué, qué valora cada persona y qué razones da. Se anotan las posiciones, los valores que las sostienen (alcance, profundidad, acceso a otras obras), los puntos de acuerdo, los desacuerdos y las propuestas que combinan ideas.",
        "Un valor es aquello que una persona considera importante y que orienta sus elecciones. En la ficha, Elena valora el alcance (que muchos lo vean), Hugo, la profundidad de la experiencia (hacer arte) e Inés, el acceso a otras obras. Entender los valores explica por qué personas razonables llegan a propuestas distintas.",
        "Una propuesta intermedia combina elementos de varias posiciones respetando sus valores. No siempre es posible, y a veces se debe elegir con costos. Un mapa claro ayuda a que el grupo decida con conciencia de lo que gana y lo que deja de lado. Mapear no es opinar: primero se entiende, después se evalúa.",
    ],
    vocab=[("mapa de perspectivas", "esquema de quién propone qué, con qué valores y razones"), ("valor", "aquello que una persona considera importante y orienta sus elecciones"), ("propuesta intermedia", "la que combina elementos de varias posiciones"), ("costo de oportunidad", "lo que se deja de lado al elegir una opción")],
    worked=[
        ("Identificar el valor", "Elena propone el mural porque «queda para siempre y lo ve todo el liceo». ¿Qué valora?",
         ["Mira sus razones: durabilidad y número de personas que lo ven.", "Valora el alcance y la permanencia."],
         "El alcance y la permanencia"),
        ("Reconocer una propuesta intermedia", "¿Qué propuesta intermedia hace Inés al final?",
         ["Observa que combina el mural con el taller y con el museo.", "Es una propuesta intermedia."],
         "Un mural pintado por el taller, con visitas al museo para inspirarse"),
    ],
    mistakes=[("Resumir un diálogo con las opiniones del resumidor.", "Se mezcla mapear con evaluar.", "Anota lo que cada persona dijo y valora aparte."),
              ("Olvidar los valores de fondo y quedarse con las propuestas.", "Se pierde por qué hay desacuerdo.", "Pregunta qué valora cada persona para elegir lo que elige.")],
    T=[
        ("abc", "{F} ¿Qué propone Elena?", "Gastar en un mural", "Gastar en entradas al museo", "Gastar en un taller de música", "Elena propone usar el presupuesto en un mural, según la ficha."),
        ("abc", "{F} ¿Qué valora Hugo?", "Que el estudiantado haga arte con experiencias profundas", "Que llegue a todo el liceo", "Que dure para siempre", "Hugo dice que el taller permite hacer arte."),
        ("abc", "{F} ¿Qué valora Inés?", "Conocer arte que el liceo no tiene", "Hacer arte", "Que lo vea todo el liceo", "Propone entradas al museo para conocer otras obras."),
        ("abc", "{F} ¿En qué coinciden Elena, Hugo e Inés?", "En que el liceo debe invertir en arte", "En que el mural es la mejor opción", "En que el museo es innecesario", "Los tres discuten cómo invertir el presupuesto cultural."),
        ("abc", "{F} ¿Qué pregunta de Elena muestra respeto por Hugo?", "«Entiendo que hacer arte es importante; ¿el taller llegaría a todo el liceo?»", "«Tú no sabes de arte»", "«Eso es una tontería»", "Reconoce su punto y pregunta con una duda."),
        ("En Estética: ¿cómo se llama lo que se deja de lado al elegir una opción?", "Costo de oportunidad", "Es el nombre de esa idea."),
        ("abc", "{F} ¿Qué admite Hugo al responder a Elena?", "Que el taller llegaría a menos personas", "Que el museo es mejor", "Que su taller no costaría nada", "Reconoce un costo de su propuesta."),
        ("abc", "{F} ¿Qué se deja de lado si el liceo solo hace el mural?", "La experiencia de hacer arte y el acceso a otras obras", "El alcance del mural", "La permanencia del mural", "Elegir una opción deja fuera otras."),
        ("abc", "{F} ¿Qué valores se respetan en la propuesta intermedia de Inés?", "Alcance (mural), práctica (taller) y acceso a otras obras (museo)", "Solo el costo", "Solo el alcance", "La propuesta intermedia combina los valores de las tres personas."),
        ("abc", "{F} Un estudiante dice: «Hugo y Elena no pueden ponerse de acuerdo porque piensan lo contrario». ¿Qué corrección es mejor?", "Valoran cosas distintas, y una propuesta intermedia podría acercarlos", "Tiene razón", "Piensan lo mismo", "Los valores explican el desacuerdo y permiten propuestas combinadas."),
        ("abc", "{F} Un mapa de perspectivas de este diálogo debería incluir…", "Propuesta, valor y razón de cada persona, más acuerdos y desacuerdos", "Solo las opiniones del que lo escribe", "Solo la propuesta de Elena", "Un mapa de perspectivas recoge propuestas, valores, razones y desacuerdos."),
        ("abc", "{F} ¿Qué pregunta ayuda a evaluar la propuesta intermedia?", "¿Alcanza el presupuesto para las tres cosas y qué se debe recortar?", "¿Qué propuesta tuvo más votos?", "¿Qué propuesta se presentó primero?", "Evalúa la viabilidad y los costos."),
        ("abc", "{F} Si el presupuesto no alcanza para la propuesta intermedia, ¿qué debe hacer el grupo?", "Priorizar y ser consciente de lo que se deja fuera", "Elegir al azar sin conversar", "Esconder el problema", "Una decisión consciente muestra el costo."),
    ],
    ctx=("abc", "Una junta de vecinos ficticia debate si usar un salón para un taller de teatro o para una biblioteca. Hay tres propuestas y un mapa de valores. ¿Cuál es el paso siguiente más razonable?", "Evaluar costos, alcance y compatibilidad de cada propuesta y considerar una combinación", "Votar sin leer el mapa", "Descartar a quien piense distinto", "El mapa ayuda a decidir con conciencia."),
    sc=[
        ("En Estética: ¿qué es un valor en un diálogo?", "Aquello que una persona considera importante y orienta sus elecciones", "Explica por qué se llega a distintas propuestas."),
        ("¿Qué es una propuesta intermedia?", "Una que combina elementos de varias posiciones", "Respeta varios valores a la vez."),
        ("¿Por qué conviene mapear antes de evaluar?", "Porque primero se entiende lo que cada persona dijo y después se evalúa", "Mapear primero evita mezclar la descripción con la opinión propia."),
    ],
    op=("Elige una de estas preguntas ficticias para un diálogo con tres personas: (1) ¿qué tipo de espacio cultural debería tener un barrio nuevo: teatro, biblioteca o plaza con escenario?, (2) ¿qué actividad artística debería ofrecer el liceo en las tardes?, (3) ¿cómo recordar a una persona querida del barrio: mural, concierto o libro de relatos? "
        "Escribe, para tres personas imaginarias, su propuesta, su valor y su razón. Luego redacta una propuesta intermedia y un costo de oportunidad.",
        "Pregunta 3. A: mural; valora la permanencia; razón: queda para siempre. B: concierto; valora la emoción compartida. C: libro; valora el relato detallado. Intermedia: un concierto en la inauguración del mural. Costo: no se escribe un libro este año.",
        ["tres propuestas distintas con valor y razón", "una propuesta intermedia coherente", "indica un costo de oportunidad", "no mezcla opinión propia con el mapa"],
        ["mapa de tres perspectivas y una propuesta intermedia"],
        ["repetir la misma propuesta", "no indicar valores", "proponer algo que ignora los valores"],
        "Pregunta: «¿qué valor respeta tu propuesta intermedia?». Pídele que lo escriba junto a la propuesta."),
    reinforce="Haz un mapa de perspectivas de una discusión de tu casa sobre qué ver en familia: quién propone qué y qué valora.",
    extend="Explica por qué una propuesta intermedia no siempre es la mejor, aunque parezca contentar a todos.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 29 (turnos de un diálogo ficticio para evaluar y registro de acuerdos). Pregunta del grupo: «¿Qué función debería tener el arte en nuestra comunidad escolar?» "
     "Turno 1, Marcela: «Debería ayudarnos a conocernos entre cursos; por ejemplo, con un festival.» "
     "Turno 2, Pablo: «Eso no es arte, es una fiesta.» "
     "Turno 3, Marcela: «¿Qué distingue una fiesta de una obra para ti?» "
     "Turno 4, Pablo: «Una obra se prepara y se piensa.» "
     "Turno 5, Marcela: «En un festival también se prepara y se piensa; por ejemplo, las coreografías.» "
     "Turno 6, Pablo: «Tienes razón, aunque sigo pensando que no todo festival es arte.» "
     "Registro de acuerdos: (a) el arte puede ayudar a conocerse; (b) no todo evento es una obra; (c) falta definir qué hace de un festival una obra. "
     "Criterios para valorar un turno: pertinencia (responde al tema), razón (da un motivo), respeto (no ataca a la persona) y apertura (admite que puede cambiar de idea).")
build(
    O6, 4, F,
    use="Aprenderé a formular y evaluar argumentos dentro de un diálogo sobre la función del arte, a construir una visión personal y una colectiva y a registrar acuerdos, desacuerdos y preguntas abiertas.",
    prior=["Uso las reglas del diálogo.", "Mapeo perspectivas.", "Evalúo argumentos con criterios."],
    explain=[
        "En un diálogo, cada turno puede evaluarse con cuatro criterios: la pertinencia, o sea si responde al tema; la razón, si da un motivo; el respeto, si evita atacar a la persona; y la apertura, si admite que podría cambiar de idea. Un turno puede ser breve y aun así cumplir los cuatro.",
        "Una visión personal se construye con una tesis, una razón y un ejemplo propio, y mejora cuando considera una objeción. Una visión colectiva se registra como una lista de acuerdos, desacuerdos y preguntas abiertas, no como una sola frase que borre las diferencias. El registro permite que el grupo vuelva sobre lo conversado.",
        "Al terminar, una persona puede reformular su visión personal tras escuchar a las demás. Cambiar de idea por buenas razones no es perder: es aprender. Mantener la idea con mejores razones también es válido. Lo importante es que el cambio, o la permanencia, se justifique.",
    ],
    vocab=[("pertinencia", "responder al tema que se discute"), ("apertura", "disposición a cambiar de idea si hay buenas razones"), ("registro de acuerdos", "lista de acuerdos, desacuerdos y preguntas abiertas de un grupo"), ("pregunta abierta", "cuestión que el grupo reconoce que aún no resolvió")],
    worked=[
        ("Evaluar un turno", "Evalúa el Turno 2 de Pablo («Eso no es arte, es una fiesta») con los cuatro criterios.",
         ["Pertinencia: responde al tema. Razón: no da una razón.", "Respeto: no ataca a la persona. Apertura: no la muestra todavía."],
         "Pertinente y respetuoso, pero sin razón ni apertura aún"),
        ("Registrar una pregunta abierta", "Escribe una pregunta abierta que surja del diálogo de la ficha.",
         ["Nota lo que el grupo no resolvió: qué hace de un festival una obra.", "Formula la pregunta."],
         "¿Qué hace de un festival una obra de arte?"),
    ],
    mistakes=[("Registrar solo los acuerdos y omitir los desacuerdos.", "Se produce un falso consenso.", "Anota también los desacuerdos y las preguntas abiertas."),
              ("Creer que cambiar de idea es perder.", "Se confunde diálogo con competencia.", "Cambiar por buenas razones es aprender; di cuál fue la razón.")],
    T=[
        ("abc", "{F} Al preguntar «¿Qué distingue una fiesta de una obra para ti?», ¿qué criterio de valoración muestra Marcela en el Turno 3?", "Apertura, porque quiere entender la razón de Pablo", "Razón propia, porque defiende su tesis con un motivo", "Ninguno: es un ataque a la persona", "Pide a Pablo que explique su criterio antes de objetarlo: muestra disposición a entender."),
        ("abc", "{F} ¿Qué criterio cumple el Turno 4 de Pablo («Una obra se prepara y se piensa»)?", "Razón, porque ofrece un criterio", "Ataque a la persona", "Solo la apertura", "Da un motivo para distinguir obra de fiesta."),
        ("abc", "{F} ¿Qué hace Marcela en el Turno 5?", "Objeta con un ejemplo concreto", "Ataca a Pablo", "Cierra la conversación", "Muestra que también en un festival se prepara y se piensa."),
        ("abc", "{F} ¿Qué criterio muestra el Turno 6 de Pablo?", "Apertura, porque admite que Marcela tiene razón en parte", "Ataque a la persona", "Falta de razón", "Reconoce parte del argumento y mantiene su duda."),
        ("En Estética: ¿cómo se llama la disposición a cambiar de idea si hay buenas razones?", "Apertura", "Es uno de los criterios de valoración de un turno."),
        ("ab", "{F} ¿Quién sostiene directamente que no todo festival es arte?", "Pablo, en el Turno 6", "Marcela, en el Turno 5", "Pablo lo afirma al final de su Turno 6, mientras Marcela solo da el ejemplo de las coreografías."),
        ("abc", "{F} ¿Cuántos puntos tiene el registro de acuerdos de la ficha y cuántos son preguntas abiertas?", "Tres puntos, de los cuales uno es una pregunta abierta", "Tres puntos y todos son acuerdos", "Dos puntos y ninguno es una pregunta abierta", "Los puntos (a) y (b) son acuerdos y el (c), «falta definir», queda abierto."),
        ("abc", "{F} Una estudiante propone borrar el desacuerdo y escribir «Todos pensamos igual». ¿Qué falla?", "Crea un falso consenso y pierde información", "Que el registro quedaría muy largo", "Que Marcela no estaría de acuerdo", "El registro debe mostrar acuerdos y desacuerdos."),
        ("abc", "{F} Un estudiante dice: «Pablo perdió porque cambió de opinión». ¿Qué corrección es mejor?", "Cambiar de opinión por buenas razones es aprender, no perder", "Tiene razón", "Pablo cambió solo para terminar la conversación", "En un diálogo no se compite."),
        ("abc", "{F} Escribe una visión personal de Marcela en una frase.", "«El arte puede ayudar a que los cursos se conozcan y compartan una experiencia, por ejemplo, en un festival con coreografías.»", "«El arte no sirve»", "«Pablo no entiende»", "Resume su tesis con razón y ejemplo."),
        ("abc", "{F} Escribe una visión colectiva razonable.", "«Acordamos que el arte puede ayudar a conocerse; no coincidimos en si todo festival es una obra.»", "«Todos pensamos igual»", "«Ganó Marcela»", "El registro colectivo incluye lo acordado y lo que sigue en desacuerdo."),
        ("abc", "{F} ¿Qué tarea podría proponer el grupo para avanzar sobre la pregunta abierta?", "Escribir dos criterios posibles para distinguir un festival que sea obra de uno que no", "Votar sin conversar", "Cerrar el tema", "Proponer criterios para distinguir casos permite seguir dialogando con razones."),
        ("abc", "{F} Si el grupo repite la conversación en una semana, ¿qué conviene hacer primero?", "Releer el registro de acuerdos y la pregunta abierta", "Empezar de cero", "Ignorar lo hablado", "El registro permite retomar el diálogo."),
    ],
    ctx=("abc", "Un grupo de estudiantes ficticios termina un diálogo sobre arte y comunidad. Una persona escribe en el registro: «Se decidió que el arte es importante». Otra dice que falta señalar en qué no coincidieron. ¿Qué conviene?", "Añadir los desacuerdos y las preguntas abiertas", "Dejarlo así", "Borrar el registro", "Un registro útil incluye lo que quedó abierto."),
    sc=[
        ("En Estética: ¿cuáles son los cuatro criterios para valorar un turno de un diálogo?", "Pertinencia, razón, respeto y apertura", "Son los cuatro criterios para valorar un turno que da la ficha."),
        ("¿Qué incluye un registro de acuerdos?", "Acuerdos, desacuerdos y preguntas abiertas", "Un registro completo evita presentar como consenso lo que no lo es."),
        ("¿Por qué cambiar de idea con buenas razones no es perder?", "Porque en el diálogo se busca entender mejor, no ganar", "Al cambiar de idea con buenas razones se aprende algo nuevo."),
    ],
    op=("Con la pregunta «¿Qué función debería tener el arte en nuestra comunidad escolar?», elabora: (a) tu visión personal en cuatro líneas (tesis, razón, ejemplo y una objeción posible); (b) el registro de un diálogo imaginario que escribirías con dos compañeros (dos acuerdos, un desacuerdo y una pregunta abierta). "
        "Si tu docente lo organiza, puedes hacer este diálogo en voz alta con dos compañeros reales y llenar el registro después.",
        "Visión personal: el arte debería ayudar a que los cursos se conozcan. Razón: comparte experiencias. Ejemplo: un coro entre cursos. Objeción: no todos quieren cantar. Registro: acuerdos: el arte puede unir; hay que dar opciones. Desacuerdo: si debe ser obligatorio. Pregunta abierta: ¿cómo participar sin presión?",
        ["la visión personal tiene tesis, razón, ejemplo y objeción", "el registro incluye acuerdos, desacuerdos y una pregunta abierta", "no hay ataques a la persona", "las razones están separadas de las opiniones"],
        ["visión personal y registro de diálogo"],
        ["omitir los desacuerdos", "no dar razón", "escribir una pregunta abierta de sí o no"],
        "Pregunta: «¿qué razón apoya tu tesis?». Pídele que la subraye y que anote el desacuerdo que no quiso borrar."),
    reinforce="Anota en tu cuaderno una conversación breve que hayas tenido sobre una canción o serie y evalúa un turno con los cuatro criterios.",
    extend="Explica por qué una pregunta abierta puede ser el mejor resultado de un diálogo filosófico.",
)

O7 = "FI-ESTE-3y4-OAC-07"

# ============================================================ OAC-07, clase 1
F = ("Ficha 30 (casos ficticios). Isidora pasa una tarde viendo muchos videos de pocos segundos; al terminar recuerda poco de cada uno, pero le parecen entretenidos. "
     "Joaquín escucha un disco completo en la tarde, sin mirar ninguna pantalla, y después dice que notó detalles que no había oído antes. "
     "Marcia visita una feria de artesanía y compra una pieza hecha a mano; dice que le gusta saber quién la hizo. "
     "Pregunta de la clase: ¿cómo influye la cultura de hoy en lo que percibimos y sentimos? Los casos son ficticios y no establecen qué es mejor o peor: sirven para plantear el problema.")
build(
    O7, 1, F,
    use="Aprenderé a plantear el problema de cómo la sociedad y la cultura actual influyen en la experiencia y la sensibilidad, a distinguir influir de determinar y a empezar a elaborar una visión personal.",
    prior=["Distingo percepción de interpretación.", "Conozco la experiencia estética.", "Sé formular preguntas de investigación."],
    explain=[
        "La sensibilidad es la capacidad de percibir, sentir y ser afectado por lo que nos rodea. La cultura es el conjunto de modos de vida, creencias, objetos y prácticas que comparte un grupo. Ambas se relacionan: lo que una cultura valora, produce y hace circular influye en lo que sus integrantes miran, escuchan y sienten.",
        "Decir que la cultura influye no es decir que determina. La influencia es un condicionamiento que puede ser mayor o menor, y cada persona puede reforzarlo, cuestionarlo o transformarlo. Por ejemplo, la cantidad de estímulos disponibles hoy puede entrenar ciertos modos de atención, pero una persona puede elegir otros ritmos y otras prácticas.",
        "Una visión personal sobre este tema parte de preguntas: qué cambió en mi forma de percibir, qué ayudó o dificultó vivir experiencias estéticas, qué le debo a mi cultura y qué decido yo. Los casos de la ficha no dicen que un estilo de vida sea mejor que otro; ayudan a formular preguntas. Si algo de esto te produce inquietud, conversa con una persona adulta de confianza.",
    ],
    vocab=[("sensibilidad", "capacidad de percibir, sentir y ser afectado por lo que nos rodea"), ("cultura", "conjunto de modos de vida, creencias, objetos y prácticas que comparte un grupo"), ("influir", "condicionar sin determinar por completo"), ("determinar", "decidir por completo, sin margen de elección"), ("visión personal", "postura propia, elaborada con razones y experiencias")],
    worked=[
        ("Distinguir influir de determinar", "Una frase dice: «La cultura actual determina totalmente cómo sentimos». ¿Qué problema tiene?",
         ["La palabra «totalmente» elimina el margen de elección de las personas.", "La cultura puede influir o condicionar, pero no necesariamente determinar por completo."],
         "Convierte la influencia en determinación total"),
        ("Plantear una pregunta", "Con los casos de Isidora y Joaquín, escribe una pregunta que compare sus experiencias.",
         ["Nota la diferencia: muchos estímulos breves frente a un disco completo.", "Pregunta: ¿cómo cambia lo que se percibe según el ritmo y la cantidad de estímulos?"],
         "¿Cómo cambia lo que se percibe según el ritmo y la cantidad de estímulos?"),
    ],
    mistakes=[("Concluir que un estilo de vida es mejor que otro a partir de un caso.", "Se generaliza desde un solo ejemplo.", "Usa el caso para formular preguntas, no para juzgar a las personas."),
              ("Decir que la cultura lo determina todo o que no influye en nada.", "Se pasa a extremos.", "Examina qué parte de la experiencia está condicionada y qué parte depende de la elección.")],
    T=[
        ("abc", "{F} ¿Qué recuerda Isidora al terminar?", "Poco de cada video, aunque le parecieron entretenidos", "Todos los detalles", "Solo el último video", "La ficha dice que recuerda poco de cada uno."),
        ("abc", "{F} ¿Qué dice Joaquín después de escuchar el disco?", "Que notó detalles que no había oído antes", "Que se distrajo con otra pantalla", "Que no recuerda el disco", "La ficha dice que Joaquín notó detalles que no había oído antes."),
        ("abc", "{F} ¿Qué valora Marcia de la pieza de artesanía?", "Saber quién la hizo", "Que la pieza es barata", "Que sea decorativa", "La ficha dice que a Marcia le gusta saber quién hizo la pieza."),
        ("En Estética: ¿cómo se llama la capacidad de percibir, sentir y ser afectado por lo que nos rodea?", "Sensibilidad", "Es la definición de sensibilidad dada en la clase."),
        ("abc", "{F} ¿Qué pregunta plantea el problema de la clase?", "¿Cómo influye la cultura de hoy en lo que percibimos y sentimos?", "¿Quién tiene la razón entre Isidora y Joaquín?", "¿Cuántos videos se pueden ver en una tarde?", "Es la pregunta central de la clase."),
        ("ab", "{F} ¿Qué es verdadero según la ficha sobre los casos?", "No establecen qué es mejor o peor, sino que sirven para plantear el problema", "Muestran que ver videos es malo", "Los casos son ejemplos de apoyo para preguntar, no una evaluación de las personas."),
        ("abc", "Una frase dice: «La cultura condiciona nuestra sensibilidad, pero cada persona puede cambiar sus hábitos». ¿Qué relación plantea?", "Influencia sin determinación total", "Determinación total", "Ninguna influencia", "Reconoce condicionamiento y margen de elección."),
        ("abc", "Una frase dice: «Como Isidora ve muchos videos, no puede sentir nada». ¿Qué falla?", "Generaliza desde un caso y afirma algo que no se desprende de él", "Es una descripción", "Es una pregunta", "La ficha no dice que no sienta nada."),
        ("abc", "{F} ¿Qué pregunta aprovecha mejor el caso de Marcia?", "¿Cómo influye saber quién hizo un objeto en la experiencia que tenemos de él?", "¿Cuántas personas visitan la feria?", "¿Qué materiales usó quien la hizo?", "Plantea una relación entre contexto y experiencia."),
        ("abc", "{F} Un estudiante dice: «Isidora y Joaquín prueban que el pasado era mejor». ¿Qué corrección es mejor?", "Los casos no prueban eso; solo ayudan a formular preguntas sobre percepción y ritmo", "Tiene razón", "No prueban nada ni sirven para preguntas", "Los casos no sostienen una comparación de épocas."),
        ("abc", "{F} ¿Cuál es una forma prudente de comenzar una visión personal sobre el tema?", "Describir una experiencia propia y decir qué parte creo que viene de mi cultura y qué parte de mi elección", "Afirmar una verdad sobre toda la sociedad", "No decir nada", "Parte de la experiencia propia y distingue influencia de elección."),
        ("abc", "{F} ¿Qué puede hacer una persona que sienta que los hábitos de pantalla le cuestan concentración?", "Conversar con una persona adulta de confianza y probar otros ritmos", "Callarse", "Culpar a otros", "Pedir apoyo es una respuesta prudente."),
        ("abc", "{F} ¿Qué pregunta de investigación combina los tres casos?", "¿Qué prácticas culturales favorecen distintos modos de atención y de relación con las obras?", "¿Cuál de las prácticas es la mejor para todos?", "¿Quién usa más pantallas?", "Relaciona prácticas culturales con modos de percibir."),
    ],
    ctx=("abc", "En un liceo ficticio, un grupo propone una «hora sin pantallas» en el recreo para escuchar música en vivo. Otro grupo dice que eso es imponer un estilo de vida. ¿Qué pregunta ayuda a decidir con razones?", "¿Qué experiencias estéticas buscamos y cómo influyen las pantallas, sin que nadie quede forzado?", "¿Qué grupo tiene más integrantes?", "¿Quién tiene que pagar la música en vivo?", "Se busca una decisión con razones y respeto."),
    sc=[
        ("En Estética: ¿qué es la cultura?", "El conjunto de modos de vida, creencias, objetos y prácticas que comparte un grupo", "Lo que una cultura valora influye en la sensibilidad de sus integrantes."),
        ("¿Qué diferencia hay entre influir y determinar?", "Influir condiciona y determinar decide por completo", "Con influencia queda margen de elección."),
        ("¿Por qué no se debe juzgar a las personas a partir de un caso?", "Porque un caso no basta para generalizar", "Un caso aislado sirve para formular preguntas, no para generalizar."),
    ],
    op=("Elige una de estas experiencias ficticias: (1) alguien pasa un día sin teléfono, (2) alguien visita una feria artesanal, (3) alguien asiste a una función de teatro del barrio. "
        "Escribe una descripción breve de cómo imaginas esa experiencia, qué parte podría estar influida por la cultura actual, qué parte dependería de la elección de la persona y una pregunta que te quede.",
        "Experiencia 3. Descripción: la persona atiende a las voces y gestos en vivo. Influida por la cultura: hábitos de atención. Elección: decidir ir y no mirar el teléfono. Pregunta: ¿cómo cambia la atención cuando sabemos que lo que se ve no se puede repetir?",
        ["describe una experiencia posible", "distingue influencia y elección", "formula una pregunta abierta", "evita juzgar a las personas"],
        ["descripción, influencia, elección y pregunta"],
        ["tratar la cultura como si lo determinara todo", "emitir un juicio sobre un tipo de personas", "formular una pregunta de sí o no"],
        "Pregunta: «¿qué parte es de tu cultura y qué parte de tu elección?». Pídele que marque ambas."),
    reinforce="Anota durante un día dos momentos en que algo de tu entorno cultural (música, imágenes, pantallas) cambió tu ánimo o tu atención.",
    extend="Explica por qué la frase «la cultura influye en la sensibilidad» no equivale a «las personas no tienen opinión propia».",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 31 (glosario y casos ficticios). Glosario: industria cultural = producción en gran escala de bienes culturales (música, series, imágenes) para un público amplio; masificación = difusión de lo mismo a muchísimas personas; gusto = inclinación a valorar ciertas cosas; moda = preferencia colectiva pasajera; identidad = modo en que una persona o un grupo se reconoce a sí mismo; diversidad cultural = existencia de muchas formas culturales en una sociedad. "
     "Una postura crítica sostiene que la industria cultural tiende a estandarizar el gusto; otra postura sostiene que también amplía el acceso a obras y permite nuevas creaciones. "
     "Caso A: una banda ficticia de barrio graba una canción y la sube a una plataforma; llega a oyentes de lugares lejanos. "
     "Caso B: en una ciudad ficticia, casi todas las vitrinas muestran los mismos estilos de ropa esta temporada.")
build(
    O7, 2, F,
    use="Aprenderé a definir industria cultural, masificación, gusto, moda, identidad y diversidad cultural, y a usarlos para analizar cómo la cultura actual influye en la sensibilidad.",
    prior=["Distingo influir de determinar.", "Conozco sensibilidad y cultura.", "Sé aplicar un concepto a un caso."],
    explain=[
        "La industria cultural es la producción en gran escala de bienes culturales, como música, series e imágenes, para un público amplio. La masificación es la difusión de lo mismo a muchísimas personas. Estos fenómenos influyen en el gusto, la inclinación a valorar ciertas cosas, y en las modas, preferencias colectivas pasajeras.",
        "Una postura crítica sostiene que la industria cultural tiende a estandarizar el gusto, porque produce lo que más se vende y lo repite. Otra postura sostiene que amplía el acceso a obras y permite que más personas creen y compartan. Ambas ofrecen razones y se discuten con casos. No hace falta que una gane: sirven para pensar con matices.",
        "La identidad es el modo en que una persona o un grupo se reconoce a sí mismo, y la diversidad cultural es la existencia de muchas formas culturales en una sociedad. El gusto y las modas pueden fortalecer o debilitar la identidad y la diversidad según cómo se vivan. Aplicar estos conceptos a casos permite decir con precisión qué está pasando.",
    ],
    vocab=[("industria cultural", "producción en gran escala de bienes culturales para un público amplio"), ("masificación", "difusión de lo mismo a muchísimas personas"), ("gusto", "inclinación a valorar ciertas cosas"), ("moda", "preferencia colectiva pasajera"), ("identidad", "modo en que una persona o un grupo se reconoce a sí mismo"), ("diversidad cultural", "existencia de muchas formas culturales en una sociedad")],
    worked=[
        ("Aplicar masificación", "En el Caso B, casi todas las vitrinas muestran los mismos estilos esta temporada. ¿Qué concepto se aplica?",
         ["Observa que lo mismo se difunde a muchísimas personas.", "Eso es masificación, y por ser pasajera, también moda."],
         "Masificación y moda"),
        ("Aplicar acceso ampliado", "En el Caso A, la canción de barrio llega a oyentes lejanos. ¿Qué postura apoya ese caso?",
         ["Mira qué ocurre: una obra de un grupo pequeño llega a mucha gente.", "Apoya la postura que dice que se amplía el acceso y se permiten nuevas creaciones."],
         "La que sostiene que amplía el acceso y permite nuevas creaciones"),
    ],
    mistakes=[("Creer que moda y gusto son lo mismo.", "Se confunde algo pasajero y colectivo con una inclinación más duradera y personal.", "La moda es colectiva y pasajera; el gusto es una inclinación a valorar."),
              ("Usar «industria cultural» como insulto.", "Se pierde el matiz de que también amplía el acceso.", "Úsala como concepto, mirando efectos positivos y negativos.")],
    T=[
        ("abc", "{F} ¿Qué detalle del Caso B muestra el carácter pasajero de una moda?", "Que los mismos estilos se vean «esta temporada»", "Que haya vitrinas en una ciudad", "Que se venda ropa", "Una moda es pasajera: la ficha dice que son los estilos de esta temporada."),
        ("abc", "{F} Si una gran empresa contratara a la banda del Caso A y le exigiera repetir siempre la misma fórmula, ¿qué postura ganaría apoyo?", "La que dice que la industria cultural tiende a estandarizar el gusto", "La que dice que amplía el acceso y permite nuevas creaciones", "Ninguna de las dos", "Repetir lo que más se vende es lo que la postura crítica advierte."),
        ("abc", "{F} ¿Qué postura apoya mejor el Caso B?", "La que dice que la industria cultural tiende a estandarizar el gusto", "La que dice que amplía el acceso", "Ambas por igual", "Muestra la repetición de los mismos estilos."),
        ("En Estética: ¿cómo se llama la preferencia colectiva pasajera?", "Moda", "Es la definición de moda del glosario."),
        ("abc", "{F} ¿Qué es la identidad?", "El modo en que una persona o un grupo se reconoce a sí mismo", "La producción en gran escala", "La existencia de muchas formas culturales", "Es la definición de identidad dada en el glosario."),
        ("ab", "{F} ¿Qué es la diversidad cultural?", "La existencia de muchas formas culturales en una sociedad", "La difusión de lo mismo a muchísimas personas", "Es la definición del glosario; la otra opción describe masificación."),
        ("abc", "Un joven ficticio dice: «Me gusta cierto tipo de música desde hace años, aunque no esté de moda». ¿Qué ejemplifica?", "Gusto distinto de moda", "Masificación", "Industria cultural", "Su preferencia es duradera y personal."),
        ("abc", "Una plataforma ficticia ofrece cientos de documentales de pueblos del país y muchas personas empiezan a verlos. ¿Qué concepto aplica?", "Acceso ampliado a la diversidad cultural", "Masificación de lo mismo", "Estandarización del gusto", "Pone a disposición formas culturales diversas."),
        ("abc", "{F} Un estudiante dice: «La industria cultural siempre destruye la identidad». ¿Qué corrección es mejor?", "Puede ocurrir en algunos casos, pero también puede ampliar el acceso, como en el Caso A", "Tiene razón", "No tiene ningún efecto", "La afirmación «siempre» no resiste el Caso A."),
        ("abc", "{F} Otro estudiante dice: «Si algo es masivo, es malo». ¿Qué falla?", "Confunde cantidad de público con calidad", "Es una buena regla", "Usa el concepto de gusto bien", "Que algo sea masivo no determina su valor."),
        ("abc", "{F} Una estudiante dice: «Mis preferencias son solo mías, sin influencia de nada». ¿Qué matiz se puede agregar?", "Las preferencias pueden estar influidas por lo que circula en la cultura, aunque la persona también elige", "Tiene toda la razón", "No tiene preferencias", "Las preferencias pueden estar influidas sin estar determinadas por completo."),
        ("abc", "{F} ¿Qué pregunta ayuda a analizar el Caso B?", "¿Qué se pierde y qué se gana cuando muchas personas visten igual esta temporada?", "¿Qué marca vende más ropa?", "¿Quién usa la ropa más cara?", "Considera efectos en identidad y diversidad."),
        ("abc", "{F} ¿Qué haría una persona crítica y matizada ante la industria cultural?", "Reconocer riesgos de estandarización y beneficios de acceso, y decidir con atención", "Rechazar todo", "Aceptar todo sin pensar", "Un análisis matizado considera ambos lados."),
    ],
    ctx=("abc", "En una radio escolar ficticia, un estudiante propone poner solo las canciones más escuchadas. Otra propone mezclarlas con música local poco conocida. ¿Qué razonamiento sigue la segunda?", "Que ampliar la diversidad enriquece la experiencia y no depende solo de la moda", "Que lo más escuchado es malo", "Que no hay que escuchar nada", "Defiende combinar lo masivo con la diversidad."),
    sc=[
        ("En Estética: ¿qué es la industria cultural?", "La producción en gran escala de bienes culturales para un público amplio", "Puede estandarizar y también ampliar el acceso."),
        ("¿Qué diferencia hay entre gusto y moda?", "El gusto es una inclinación a valorar y la moda es una preferencia colectiva pasajera", "La moda es pasajera, mientras que el gusto es una inclinación más estable."),
        ("¿Qué es la diversidad cultural?", "La existencia de muchas formas culturales en una sociedad", "Se puede ampliar o reducir según las prácticas."),
    ],
    op=("Elige una situación ficticia: (1) en un barrio todas las radios pasan los mismos temas, (2) un colegio abre un taller de música de tres pueblos distintos, (3) una serie se vuelve famosa y todos hablan de ella. "
        "Analiza con tres conceptos de la clase (por ejemplo, masificación, gusto, diversidad cultural), señala un efecto positivo y uno negativo posible y escribe tu postura provisoria con una razón.",
        "Situación 2. Conceptos: diversidad cultural, identidad, gusto. Efecto positivo: se conocen músicas distintas. Efecto negativo: podría quedar poco tiempo para profundizar. Postura provisoria: me parece valioso, porque amplía lo que sabemos escuchar.",
        ["usa tres conceptos con sentido", "indica efectos positivo y negativo", "formula una postura con una razón", "no generaliza desde la situación"],
        ["análisis con tres conceptos, dos efectos y postura provisoria"],
        ["usar conceptos sin relación con la situación", "dar solo efectos negativos", "generalizar a toda la sociedad"],
        "Pregunta: «¿qué parte de la situación muestra ese concepto?». Pídele que cite un rasgo."),
    reinforce="Anota una moda de tu curso y una preferencia tuya que no sea moda. Explica la diferencia.",
    extend="Explica por qué la masificación puede tener efectos opuestos según cómo se use.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 32 (tres miradas ficticias, resumidas por el cuaderno). Mirada optimista: «Hoy hay más acceso a obras de todo el mundo y más personas pueden crear y compartir; la cultura actual amplía la sensibilidad.» "
     "Mirada crítica: «La cantidad de estímulos y la rapidez con que cambian pueden acostumbrarnos a una atención breve y a gustos parecidos; la cultura actual puede empobrecer la sensibilidad.» "
     "Mirada intermedia: «El efecto depende del uso: según cómo elijamos y qué aprendamos a mirar, la cultura actual puede ampliar o empobrecer la sensibilidad.» "
     "Tabla de reconstrucción: tesis / razón / supuesto / qué propone hacer.")
build(
    O7, 3, F,
    use="Aprenderé a reconstruir tres perspectivas filosóficas sobre la influencia de la cultura actual en la sensibilidad (optimista, crítica e intermedia) y a compararlas por sus razones, supuestos y propuestas.",
    prior=["Conozco industria cultural, gusto y moda.", "Reconstruyo tesis, razón y supuesto.", "Distingo influir de determinar."],
    explain=[
        "Reconstruir perspectivas es explicar con fidelidad lo que sostiene cada una antes de elegir. En esta clase hay tres. La optimista destaca el acceso y la posibilidad de crear. La crítica advierte que la sobreabundancia y la rapidez pueden acostumbrarnos a una atención breve y a gustos parecidos. La intermedia dice que el efecto depende del uso y de lo que aprendamos a mirar.",
        "Cada perspectiva tiene supuestos. La optimista supone que más acceso lleva a más experiencias valiosas. La crítica, que la atención se entrena y que lo que se repite moldea el gusto. La intermedia supone que las personas pueden educar su manera de mirar. Hacer visibles los supuestos permite evaluar mejor y no discutir solo conclusiones.",
        "Las perspectivas también proponen acciones distintas. La optimista, aprovechar el acceso. La crítica, cuidar espacios de atención profunda. La intermedia, educar la sensibilidad para elegir. Una visión personal puede inspirarse en una, combinar varias o proponer otra, siempre que explique sus razones.",
    ],
    vocab=[("perspectiva optimista", "destaca el acceso y la posibilidad de crear"), ("perspectiva crítica", "advierte riesgos como la atención breve y gustos parecidos"), ("perspectiva intermedia", "sostiene que el efecto depende del uso y de lo que aprendemos a mirar"), ("supuesto", "idea que una postura da por cierta sin decirla"), ("educar la sensibilidad", "aprender a percibir y valorar con más atención y variedad")],
    worked=[
        ("Reconstruir la mirada crítica", "Reconstruye con tesis, razón y supuesto la Mirada crítica de la ficha.",
         ["Tesis: la cultura actual puede empobrecer la sensibilidad.", "Razón: los estímulos abundantes y rápidos acostumbran a una atención breve y a gustos parecidos. Supuesto: la atención y el gusto se entrenan."],
         "Tesis: puede empobrecer la sensibilidad; razón: atención breve y gustos parecidos; supuesto: la atención y el gusto se entrenan"),
        ("Comparar propuestas", "¿Qué propone hacer la Mirada intermedia?",
         ["Mira su tesis: el efecto depende del uso.", "Propone educar la manera de mirar para elegir con más criterio."],
         "Educar la sensibilidad para elegir mejor"),
    ],
    mistakes=[("Presentar la mirada con la que uno no coincide como una caricatura.", "Se pierde la razón central.", "Reconstruye cada mirada en su versión más razonable."),
              ("Creer que la mirada intermedia es no tomar partido.", "Se confunde matizar con evadir.", "La intermedia afirma una tesis: el efecto depende del uso.")],
    T=[
        ("abc", "{F} ¿Qué sostiene la Mirada optimista?", "Que la cultura actual amplía la sensibilidad por el acceso y la posibilidad de crear", "Que la cultura actual empobrece la sensibilidad", "Que la cultura no influye", "La mirada optimista destaca el acceso."),
        ("abc", "{F} ¿Qué razón da la Mirada optimista?", "Que hoy hay más acceso a obras de todo el mundo y más personas pueden crear y compartir", "Que la atención se acostumbra a lo breve", "Que las obras cuestan menos que antes", "Es la razón que da la ficha para decir que la sensibilidad se amplía."),
        ("abc", "{F} ¿Qué sostiene la Mirada intermedia?", "Que el efecto depende del uso y de lo que aprendamos a mirar", "Que siempre amplía", "Que siempre empobrece", "Esa es la tesis central de la mirada intermedia en la ficha."),
        ("En Estética: ¿cómo se llama aprender a percibir y valorar con más atención y variedad?", "Educar la sensibilidad", "Es la propuesta de la perspectiva intermedia."),
        ("abc", "{F} ¿Qué supone la Mirada optimista?", "Que más acceso lleva a más experiencias valiosas", "Que no hay acceso", "Que la atención no se entrena", "Ese es el supuesto básico de la mirada optimista según la ficha."),
        ("ab", "{F} ¿Qué supone la Mirada intermedia?", "Que las personas pueden educar su manera de mirar", "Que la cultura determina por completo lo que sentimos", "Si el efecto depende del uso y de lo que aprendamos a mirar, se supone que mirar se puede aprender."),
        ("abc", "{F} ¿Qué propone hacer la Mirada crítica?", "Cuidar espacios de atención profunda", "Eliminar toda tecnología", "No hacer nada", "Su propuesta es proteger la atención profunda."),
        ("abc", "{F} Un estudiante dice: «La mirada intermedia no dice nada». ¿Qué corrección es mejor?", "Dice que el efecto depende del uso y propone educar la sensibilidad", "Tiene razón", "Dice lo mismo que la crítica", "La mirada intermedia afirma una tesis matizada y propone educar la sensibilidad."),
        ("abc", "{F} Un estudiante resume: «La optimista cree que no hay problemas». ¿Qué falla?", "Caricaturiza: destaca el acceso y la creación, no niega todo problema", "Es una buena reconstrucción", "Usa un supuesto", "Reconstruir exige ser fiel a la razón."),
        ("abc", "{F} ¿Qué evidencia ayudaría a evaluar la Mirada crítica?", "Comparar la atención de personas con distintos hábitos con descripciones de sus experiencias", "Contar cuántas pantallas hay en una casa", "Medir el tamaño de las pantallas", "Pone a prueba su supuesto sobre la atención."),
        ("abc", "{F} ¿Qué caso complicaría a la Mirada optimista?", "Alguien con acceso a muchas obras que sigue prefiriendo lo mismo sin explorar", "Alguien que crea una canción", "Alguien que descubre un libro nuevo", "El acceso solo no garantiza la ampliación de la sensibilidad."),
        ("abc", "{F} Una visión personal que combine las tres miradas podría decir…", "«Aprovecho el acceso, cuido momentos de atención profunda y educo mi manera de mirar»", "«La cultura lo decide todo»", "«No hay nada que decir»", "Combina las propuestas de las tres miradas y las apoya con razones."),
        ("abc", "{F} ¿Qué paso sigue a la reconstrucción de las tres miradas?", "Evaluarlas con criterios antes de elaborar una visión personal", "Elegir sin razones", "Olvidarlas", "Reconstruir con fidelidad es un paso previo a evaluar."),
    ],
    ctx=("abc", "Una radio escolar ficticia hace un programa con tres invitados que representan las miradas optimista, crítica e intermedia. La conductora pide que cada uno diga su tesis y su razón antes de debatir. ¿Qué logra con esa petición?", "Que se entienda cada mirada antes de discutirlas", "Que gane el invitado que hable más fuerte", "Que se hable solo de lo que más conocen", "Reconstruir primero cada mirada evita discutir contra una caricatura."),
    sc=[
        ("En Estética: ¿qué sostiene la perspectiva intermedia?", "Que el efecto de la cultura actual depende del uso y de lo que aprendamos a mirar", "Afirma que depende del uso, lo cual es una tesis matizada."),
        ("¿Qué es un supuesto?", "Una idea que una postura da por cierta sin decirla", "Se descubre preguntando qué debe ser cierto."),
        ("¿Por qué conviene reconstruir antes de evaluar?", "Para entender cada mirada en su versión más razonable", "Reconstruir cada mirada con fidelidad evita caricaturas."),
    ],
    op=("Completa una tabla con las tres miradas de la ficha: tesis, razón, supuesto y qué propone hacer. Después escribe una pregunta que le harías a cada una para ponerla a prueba, y una frase que diga con cuál te identificas más hoy y por qué (sin que sea definitivo).",
        "Crítica: tesis: la cultura puede empobrecer la sensibilidad; razón: estímulos abundantes y rápidos; supuesto: la atención se entrena; propone: cuidar espacios de atención profunda. Pregunta: ¿qué experiencias muestran lo contrario? Me identifico con la intermedia, porque depende de cómo elijamos.",
        ["la tabla es fiel a la ficha", "las preguntas ponen a prueba cada mirada", "la frase final tiene una razón", "no caricaturiza"],
        ["tabla de tres miradas, tres preguntas y una frase"],
        ["mezclar opiniones propias en la tabla", "dejar celdas vacías", "elegir sin razón"],
        "Pregunta: «¿qué frase de la ficha respalda esa celda?». Pídele que la subraye."),
    reinforce="Pregunta a dos personas de tu entorno qué opinan de la cultura de hoy y ubica sus ideas en una de las tres miradas.",
    extend="Explica qué supuesto compartirían la Mirada crítica y la intermedia y en qué se separan.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 33 (borrador y pauta). Borrador de visión personal de Ema (ficticia): «Creo que la cultura actual influye en mi sensibilidad, pero no la determina. Por ejemplo, cuando veo muchos videos cortos me cuesta quedarme en una canción larga, pero si apago el teléfono, descubro detalles. Una objeción sería que los videos también me muestran música nueva; respondo que sí, y por eso intento alternar. Quiero expresarlo en un collage de papel que muestre una pantalla rota por una melodía.» "
     "Pauta de una visión personal: (1) tesis; (2) razón o experiencia propia; (3) una perspectiva distinta considerada; (4) una objeción y respuesta; (5) forma de expresión elegida y por qué. "
     "Formas de expresión posibles: ensayo breve, relato corto, collage de papel con explicación, composición sonora descrita en palabras, escena teatral breve.")
build(
    O7, 4, F,
    use="Aprenderé a formular una visión personal sobre la influencia de la sociedad y la cultura actual en la sensibilidad, a evaluarla con una pauta y a elegir una forma de expresión coherente con lo que quiero decir.",
    prior=["Reconstruyo tres perspectivas sobre el tema.", "Evalúo argumentos.", "Respondo objeciones con matices."],
    explain=[
        "Elaborar una visión personal no es dar una opinión suelta: es presentar una tesis propia, apoyarla en razones o experiencias, considerar al menos una perspectiva distinta y responder una objeción. Una pauta de cinco elementos ayuda: tesis, razón o experiencia propia, perspectiva distinta, objeción con respuesta y forma de expresión elegida.",
        "La forma de expresión debe ser coherente con la tesis. Un ensayo breve permite argumentar con orden. Un relato corto muestra una experiencia. Un collage de papel con explicación puede mostrar contrastes visuales. Una composición sonora descrita en palabras, o una escena teatral breve, pueden mostrar ritmos y relaciones. Lo importante es explicar por qué esa forma ayuda a decir lo que se quiere decir.",
        "Para compartir una visión personal con respeto, se evitan los juicios sobre personas y se usan expresiones como «en mi experiencia» o «una razón que me convence». Después de compartirla, se escucha la reacción de otras personas y se puede ajustar la visión. Una visión personal bien trabajada es provisoria: puede cambiar con nuevas razones.",
    ],
    vocab=[("visión personal", "postura propia con tesis, razones, perspectiva distinta y respuesta a una objeción"), ("forma de expresión", "modo elegido para comunicar una visión, como un ensayo, un relato o un collage"), ("coherencia entre forma y tesis", "ajuste entre cómo se expresa algo y lo que se quiere decir"), ("provisoria", "abierta a cambiar con nuevas razones")],
    worked=[
        ("Aplicar la pauta", "Aplica la pauta al borrador de Ema: ¿cuál es su tesis?",
         ["Busca la primera afirmación general: la cultura actual influye en su sensibilidad pero no la determina.", "Esa es la tesis."],
         "La cultura actual influye en su sensibilidad pero no la determina"),
        ("Evaluar la coherencia de la forma", "Ema quiere un collage de papel con una pantalla rota por una melodía. ¿Es coherente con su tesis?",
         ["Mira lo que muestra: una pantalla que cede ante una melodía.", "Es coherente si explica que no determina, sino que la melodía abre otra experiencia."],
         "Sí, si explica que la melodía abre otra experiencia y no que la pantalla sea mala"),
    ],
    mistakes=[("Presentar la visión personal como una verdad para todos.", "Se confunde una postura propia con un hecho general.", "Usa «en mi experiencia» o «una razón que me convence» y reconoce otras miradas."),
              ("Elegir una forma de expresión solo porque es llamativa.", "No hay conexión con la tesis.", "Explica por qué esa forma ayuda a decir lo que quieres decir.")],
    T=[
        ("abc", "{F} ¿Cuál es la razón o experiencia propia en el borrador de Ema?", "Que con muchos videos cortos le cuesta quedarse en una canción larga, pero al apagar el teléfono descubre detalles", "Que los videos cortos son útiles", "Que sus amigos usan más pantallas", "Es la experiencia que ofrece como apoyo."),
        ("abc", "{F} ¿Qué objeción considera Ema?", "Que los videos también le muestran música nueva", "Que no tiene tiempo para escuchar música", "Que apagar el teléfono es imposible", "Es la objeción de su texto."),
        ("abc", "{F} ¿Cómo responde Ema a la objeción?", "Reconoce que es cierto y por eso intenta alternar", "La niega", "La ignora", "La acepta y ajusta su práctica."),
        ("En Estética: ¿cómo se llama el modo elegido para comunicar una visión, como un ensayo o un collage?", "Forma de expresión", "Es la parte final de la pauta."),
        ("abc", "{F} ¿Qué elemento de la pauta no aparece en el borrador de Ema?", "Una perspectiva distinta considerada, separada de la objeción", "La tesis", "La forma de expresión", "El borrador tiene tesis, experiencia, objeción con respuesta y forma; no presenta otra perspectiva."),
        ("ab", "{F} Ema duda entre su collage y una lista de cifras de uso de pantallas. ¿Cuál muestra mejor el contraste que describe su tesis?", "El collage, porque hace visible el contraste entre pantalla y melodía", "La lista de cifras, porque las cifras son más serias", "Su tesis habla de una experiencia de atención; el collage la muestra y las cifras no."),
        ("abc", "Un estudiante ficticio quiere expresar con una escena teatral cómo un grupo escucha una canción por primera vez. ¿Qué tesis podría apoyar?", "Que la escucha atenta cambia la manera de percibir", "Que la música no se puede representar", "Que solo los actores perciben", "La forma permite mostrar la escucha."),
        ("abc", "Una estudiante quiere expresar con un relato corto cómo se siente al elegir entre dos actividades. ¿Qué ventaja tiene el relato?", "Muestra una experiencia con detalles", "Mide la atención", "Reemplaza la tesis", "El relato permite narrar una vivencia."),
        ("abc", "{F} Un estudiante dice: «Mi visión personal es verdad para todos». ¿Qué corrección es mejor?", "Una visión personal es una postura propia, con razones, abierta a cambiar", "Tiene razón", "Una visión personal no necesita razones", "Debe presentarse como postura y no como hecho."),
        ("abc", "{F} Otro estudiante dice: «Si cambio mi visión después de escuchar a otros, perdí». ¿Qué falla?", "Cambiar con buenas razones es parte de una visión provisoria", "Nada falla", "Siempre hay que cambiar", "Una visión personal es provisoria y puede cambiar con nuevas razones."),
        ("abc", "{F} Escribe una tesis personal prudente sobre el tema.", "«En mi experiencia, la cultura de hoy influye en cómo atiendo, pero puedo decidir cómo mirar»", "«La cultura lo determina todo»", "«No hay cultura»", "Presenta una postura prudente con margen de elección."),
        ("abc", "{F} Una estudiante sostiene la tesis «En mi experiencia, la cultura de hoy influye en cómo atiendo, pero puedo decidir cómo mirar». ¿Qué forma de expresión sería coherente con esa tesis?", "Un relato corto sobre un día con y sin pantallas, que muestra la diferencia de atención", "Un afiche de una película popular", "Un informe de promedios de notas", "La forma muestra el contraste de atención que la tesis describe."),
        ("abc", "{F} Una compañera dice que la visión de Ema no tiene perspectiva distinta. ¿Qué podría agregar Ema?", "Un párrafo que explique la Mirada optimista y por qué en parte la comparte", "Una foto de su pantalla", "Eliminar la objeción", "Incorporar otra perspectiva cumple la pauta."),
    ],
    ctx=("abc", "Un liceo ficticio organiza una muestra de «visiones personales» sobre cultura y sensibilidad. Un estudiante quiere presentar solo un cuadro sin ninguna explicación. ¿Qué conviene agregarle?", "Una explicación breve con su tesis, una razón y por qué eligió esa forma", "Un título llamativo", "Un marco decorativo", "La explicación hace evaluable su visión."),
    sc=[
        ("En Estética: ¿qué cinco elementos tiene la pauta de una visión personal?", "Tesis, razón o experiencia, perspectiva distinta, objeción con respuesta y forma de expresión", "Son los elementos de la ficha."),
        ("¿Por qué una visión personal es provisoria?", "Porque puede cambiar con nuevas razones", "Una visión personal es una postura abierta a nuevas razones."),
        ("¿Qué significa que la forma sea coherente con la tesis?", "Que la forma ayuda a decir lo que se quiere decir", "Evita elegir solo por lo llamativo."),
    ],
    op=("Elabora tu propia visión personal con la pauta de cinco elementos sobre la pregunta «¿cómo influye la cultura actual en lo que percibimos y sentimos?». Elige una forma de expresión de la lista (ensayo breve, relato corto, collage de papel con explicación, composición sonora descrita en palabras o escena teatral breve) y escribe una versión de cinco a siete líneas. "
        "No incluyas datos privados ni juicios sobre personas; si algo personal te incomoda, conversa con una persona adulta de confianza.",
        "Tesis: en mi experiencia, la cultura actual influye en mi atención, pero puedo decidir cómo mirar. Razón: cuando escucho un disco sin pantalla noto más detalles. Perspectiva distinta: la mirada optimista valora el acceso a música nueva. Objeción: ¿no es más fácil con pantalla? Respuesta: sí, por eso alterno. Forma: un relato corto, porque muestra la diferencia de experiencia.",
        ["incluye los cinco elementos de la pauta", "la forma es coherente con la tesis", "considera una perspectiva distinta y una objeción", "usa un tono prudente y respetuoso"],
        ["texto de cinco a siete líneas con forma elegida"],
        ["presentar la visión como verdad universal", "omitir la objeción", "elegir una forma sin explicar por qué"],
        "Pregunta: «¿qué elemento de la pauta te cuesta más?». Pídele que lo marque y que lo mejore."),
    reinforce="Escribe una versión en tres líneas de tu visión y compártela con una persona de confianza para ver qué razón la convence más.",
    extend="Rehace tu visión incorporando una razón de alguien que piense distinto y explica qué cambió y qué mantuviste.",
)
