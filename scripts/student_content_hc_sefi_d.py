"""Seminario de filosofía (electivo HC, 3.º y 4.º medio): OAC-04 (participar activamente en diálogos filosóficos sobre preguntas y conceptos y su relación con la vida y con fenómenos sociales y culturales contemporáneos, clases 1 a 4). Casos y diálogos ficticios."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada caso y cada diálogo está escrito en el enunciado. "
             "Los personajes, los cursos y los grupos son ficticios: sirven para practicar el diálogo filosófico y no representan a nadie real. "
             "En las actividades abiertas puedes usar un caso ficticio en lugar de uno propio; nadie está obligado a contar su vida. "
             "Las posturas se presentan con sus razones y sin tomar partido: tu tarea es escuchar, preguntar y razonar con respeto. "
             "Si un tema te incomoda, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O4 = "FI-SEFI-3y4-OAC-04"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (caso ficticio). En el grupo de mensajería del 3.º B del liceo «Los Alerces» (no existe), cada comentario recibe «corazones». Tres estudiantes comentan. "
     "Sofía: «A veces escribo lo que creo que recibirá más corazones, no lo que pienso.» "
     "Tomás: «Si a mucha gente le gusta algo, debe ser bueno.» "
     "Elisa: «Pero algo puede ser verdadero o justo aunque nadie le dé un corazón.»")
build(
    O4, 1, F,
    use="Aprenderé a pasar de una situación de mi vida o de un fenómeno social a una pregunta filosófica que se pueda dialogar con razones.",
    prior=["Sé formular un problema filosófico.", "Distingo una pregunta de dato de una pregunta abierta.", "Sé qué es una razón."],
    explain=[
        "Un diálogo filosófico es una conversación cooperativa en la que un grupo examina una pregunta con razones, escucha otras perspectivas y está dispuesto a cambiar de opinión. Se diferencia de un debate, donde cada parte busca vencer, y de una charla de opiniones, donde cada persona dice lo que piensa sin examinarlo. En el diálogo filosófico se busca comprender mejor, no ganar.",
        "Para que una situación de la vida o un fenómeno social, como las reacciones en una red, se convierta en tema de diálogo, hay que transformarla en una pregunta abierta con conceptos que se puedan aclarar. En la ficha aparece un fenómeno: se escribe pensando en la aprobación. De allí surge una pregunta como «¿el valor de una idea depende de cuánta gente la aprueba?». Aprobación, valor y verdad son conceptos que pueden discutirse.",
        "Participar activamente significa hacer cuatro cosas: aportar una razón y no solo una opinión, preguntar para aclarar, escuchar y responder a lo que dijo la otra persona, y esperar tu turno. Las reglas del diálogo protegen a todos: se critica la idea, no a quien la dice; nadie está obligado a contar su vida; y siempre se puede pasar el turno.",
    ],
    vocab=[("diálogo filosófico", "conversación cooperativa que examina una pregunta con razones y escucha otras perspectivas"), ("debate", "intercambio en que cada parte busca vencer a la otra"), ("opinión", "lo que una persona piensa, sin necesariamente examinarlo con razones"), ("pregunta abierta", "pregunta que admite varias respuestas razonadas"), ("fenómeno social", "hecho o práctica compartida por un grupo o una sociedad")],
    worked=[
        ("Del fenómeno a la pregunta", "Transforma el fenómeno de la ficha en una pregunta para dialogar.",
         ["Detecto el fenómeno: se escribe pensando en los corazones.", "Nombro los conceptos en juego: aprobación, valor y verdad; y formulo la pregunta abierta."],
         "«¿El valor de una idea depende de cuánta gente la aprueba?»"),
        ("Distinguir tipos de intercambio", "Dos personas discuten y cada una solo quiere que la otra reconozca que perdió. ¿Es un diálogo filosófico?",
         ["Veo cuál es el propósito: ganar.", "En el diálogo filosófico el propósito es comprender mejor."],
         "No: es un debate, porque busca vencer y no comprender"),
    ],
    mistakes=[("Creer que dialogar es decir cada uno su opinión por turnos.", "Se reduce el diálogo a una charla sin examen de razones.", "Responde a lo que dijo la otra persona y pide o da razones."),
              ("Tomar una crítica a una idea como un ataque personal.", "Se confunde la idea con quien la dice.", "Recuerda la regla: se critica la idea, no a la persona.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es un diálogo filosófico?", "Una conversación cooperativa que examina una pregunta con razones", "Un intercambio en que se busca vencer", "Una lista de opiniones sin examen", "Se caracteriza por cooperar, razonar y escuchar."),
        ("abc", "¿En qué se diferencia un diálogo filosófico de un debate?", "En el diálogo se busca comprender mejor; en el debate, vencer", "En que el debate no tiene razones", "En que el diálogo no admite desacuerdo", "El propósito es lo que marca la diferencia."),
        ("abc", "{F} ¿Qué fenómeno social aparece en la ficha?", "Escribir pensando en cuántos corazones se recibirán", "Compartir apuntes con el curso", "Chatear durante las clases", "Sofía dice que a veces escribe lo que cree que recibirá más corazones."),
        ("abc", "{F} ¿Qué conceptos están en juego en la ficha?", "Aprobación, valor y verdad", "Amistad, lealtad y confianza", "Esfuerzo, tiempo y descanso", "Los tres estudiantes hablan de lo que vale una idea según su aprobación."),
        ("abc", "{F} ¿Qué supuesto se aprecia en lo que dice Tomás?", "Que algo es bueno si a mucha gente le gusta", "Que las ideas buenas no gustan", "Que nadie puede opinar", "La frase conecta aprobación con bondad."),
        ("ab", "{F} ¿Cuál es una buena pregunta abierta para dialogar sobre la ficha?", "¿Una idea puede ser verdadera aunque a casi nadie le guste?", "¿Cuántos corazones recibió el último comentario?", "La primera admite varias respuestas razonadas y usa conceptos como verdad y aprobación; la otra se contesta contando."),
        ("abc", "{F} ¿Qué hace Elisa en el diálogo?", "Ofrece una objeción: algo puede ser verdadero o justo aunque nadie lo apruebe", "Ataca a Tomás por su manera de ser", "Repite lo que dijo Sofía", "Su razón separa aprobación de verdad."),
        ("abc", "Un estudiante responde a Elisa: «Tú solo dices eso porque nadie te da corazones». ¿Qué regla del diálogo no respeta?", "Se critica la idea, no a la persona", "Esperar el turno", "Pasar el turno", "Ataca a la persona y no responde a la razón."),
        ("abc", "{F} ¿Cuál es una intervención que aporta una razón?", "«Un dato falso puede recibir muchos corazones, así que la aprobación no prueba la verdad»", "«No sé»", "«Que se calle Tomás»", "Entrega una razón que se puede examinar."),
        ("abc", "En un grupo ficticio, Camilo dice: «Esta pregunta es tonta». ¿Qué es mejor que haga?", "Explicar qué le parece poco claro o por qué no ve el problema", "Insistir en que es tonta hasta que la cambien", "Burlarse de quien la propuso", "Aportar la razón de su duda ayuda a seguir dialogando."),
        ("abc", "¿Por qué nadie está obligado a contar su vida en un diálogo filosófico?", "Porque se puede razonar con casos ficticios o generales y proteger la privacidad", "Porque las experiencias personales nunca sirven como ejemplos", "Porque se trata solo de debatir", "Se protege a las personas sin perder el análisis."),
        ("abc", "{F} Si en el grupo la mayoría escribiera sin pensar en los corazones, ¿cambiaría la pregunta filosófica?", "No: seguiría siendo discutible si la aprobación indica valor", "Sí: dejaría de ser un problema", "Sí: se resolvería con una encuesta", "La pregunta sobre el valor de la aprobación es de fondo, no depende del hábito de una mayoría."),
        ("abc", "¿Qué significa «participar activamente» según la explicación?", "Aportar razones, preguntar, escuchar y esperar el turno", "Hablar más que los demás", "Estar de acuerdo con todos", "Incluye cuatro acciones que construyen el diálogo."),
    ],
    ctx=("abc", "En un taller ficticio, un grupo comenta que muchas personas compran lo que ven que otros compran. ¿Cuál es una pregunta filosófica para dialogar?", "¿Sirve lo que hacen los demás como razón para decidir qué conviene hacer?", "¿Cuánto cuesta el producto más vendido?", "¿Cuántas personas fueron a la tienda ayer?", "Solo la primera es abierta y requiere aclarar conceptos como razón y decisión."),
    sc=[
        ("En Seminario de filosofía: ¿qué es una pregunta abierta?", "Una pregunta que admite varias respuestas razonadas", "No se resuelve con un dato."),
        ("¿Qué se hace en un diálogo filosófico con las ideas de otra persona?", "Se examinan y se critican las ideas, no a la persona", "Es la regla de respeto del diálogo."),
        ("¿Qué cuatro acciones implica participar activamente?", "Aportar razones, preguntar, escuchar y esperar turno", "Son las cuatro acciones de la explicación."),
    ],
    op=("Elige un fenómeno ficticio para dialogar. Fenómeno 1: un liceo ficticio premia con puntos a quien más tareas entrega. Fenómeno 2: un grupo de amigos ficticio decide siempre según lo que hace la mayoría. Fenómeno 3: una persona publica solo lo que le sale bien y esconde lo demás. "
        "Escribe: el fenómeno en una frase, los conceptos en juego, una pregunta abierta, una razón a favor de una respuesta y una pregunta que le harías a alguien que piense distinto.",
        "Fenómeno 3. Conceptos: autenticidad e imagen. Pregunta: ¿mostrar solo lo que sale bien es engañar? Razón: no es engañar si todos saben que se muestra una selección. Pregunta a quien piense distinto: ¿qué diferencia hay entre elegir qué mostrar y fingir lo que no es?",
        ["describe el fenómeno sin identificar a personas reales", "nombra los conceptos en juego", "formula una pregunta abierta", "da una razón y una pregunta al otro"],
        ["fenómeno, conceptos, pregunta abierta, razón y pregunta al otro escritos"],
        ["formular una pregunta de dato", "dar solo una opinión sin razón", "usar a personas reales como ejemplo"],
        "Pregunta: «¿tu pregunta tiene varias respuestas razonables?». Si no, pídele que agregue un concepto en discusión."),
    reinforce="Elige una costumbre de tu entorno (por ejemplo, responder de inmediato un mensaje) y escribe una pregunta filosófica que se pueda dialogar sobre ella.",
    extend="Escribe cinco reglas que pondrías a un diálogo filosófico de tu curso y explica la razón de cada una.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (diálogo ficticio). Tema: «Tener 500 amigos en una red social.» "
     "Ema: «Amigo es quien está en mi lista de contactos.» "
     "Bruno: «Amigo es quien me ayuda cuando lo necesito.» "
     "Carla: «Amigo es quien comparte mis gustos.» "
     "Caso 1: una persona de tu lista con la que nunca has hablado. Caso 2: una compañera de gustos distintos que te acompañó cuando tuviste un problema. Caso 3: alguien que comparte tus gustos, pero se ríe cuando te va mal.")
build(
    O4, 2, F,
    use="Aprenderé a aclarar conceptos dentro de un diálogo: pedir precisión, detectar ambigüedades y probar una definición con casos.",
    prior=["Sé participar en un diálogo filosófico.", "Sé definir con rasgos y casos.", "Sé formular una pregunta abierta."],
    explain=[
        "Muchos desacuerdos en un diálogo vienen de palabras que cada persona entiende distinto. Por eso, una acción clave es pedir precisión: «¿qué quieres decir con…?», «¿puedes dar un ejemplo?». Una palabra es ambigua cuando tiene dos o más sentidos distintos, como «banco» (para sentarse o para guardar dinero). Un término es vago cuando no tiene límites claros, como «mucho» o «a veces».",
        "En la ficha, «amigo» tiene tres sentidos propuestos: estar en una lista de contactos, ayudar cuando se necesita o compartir gustos. Para probar cada sentido se usan casos. Si un sentido deja entrar a alguien que no llamaríamos amigo, es demasiado amplio. Si deja fuera a alguien que sí llamaríamos amigo, es demasiado estrecho. Con el Caso 1, la definición de Ema deja entrar a alguien con quien nunca se habló.",
        "Aclarar conceptos no es una pérdida de tiempo: permite saber si hay un desacuerdo de fondo o solo de palabras. A veces, tras aclarar, se descubre que dos personas pensaban lo mismo con distinto vocabulario; otras veces, que de verdad discrepan.",
    ],
    vocab=[("pedir precisión", "preguntar qué significa una palabra o pedir un ejemplo"), ("ambigüedad", "palabra con dos o más sentidos distintos"), ("vaguedad", "falta de límites claros en un término"), ("definición amplia", "deja entrar casos que no deberían entrar"), ("definición estrecha", "deja fuera casos que sí deberían entrar"), ("desacuerdo verbal", "desacuerdo que se debe a que se usa una palabra con sentidos distintos")],
    worked=[
        ("Probar una definición", "Con el Caso 1 de la ficha, ¿qué problema tiene la definición de Ema?",
         ["Aplico la definición: la persona del Caso 1 está en la lista de contactos.", "Pero nunca hemos hablado; no la llamaríamos amiga."],
         "Es demasiado amplia: deja entrar a alguien con quien nunca se habló"),
        ("Detectar el tipo de problema", "Dos personas discuten si «una película larga» es la de más de dos horas. ¿Qué problema tiene la palabra «larga»?",
         ["Pregunto si hay un límite claro: no lo hay, depende de cada persona.", "No hay dos sentidos distintos, sino límites difusos."],
         "Es vaga, no ambigua"),
    ],
    mistakes=[("Pensar que pedir una definición es una forma de evitar opinar.", "Se confunde aclarar con esquivar.", "Pide precisión y luego da tu razón con el significado que aclaraste."),
              ("Aceptar una definición solo porque encaja con un ejemplo favorito.", "No se prueba con casos que la ponen en problemas.", "Busca un caso que la ponga a prueba antes de aceptarla.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es una palabra ambigua?", "La que tiene dos o más sentidos distintos", "La que no tiene límites claros", "La que nadie entiende", "Ambigua significa tener varios sentidos diferentes."),
        ("abc", "¿Qué es un término vago?", "El que no tiene límites claros", "El que tiene dos sentidos distintos", "El que es incorrecto", "La vaguedad es la falta de límites precisos."),
        ("abc", "{F} ¿Qué sentido de «amigo» propone Bruno?", "Quien ayuda cuando uno lo necesita", "Quien está en la lista de contactos", "Quien comparte gustos", "Es lo que Bruno dice textualmente en la ficha."),
        ("abc", "{F} Según la definición de Bruno, ¿qué es el Caso 2 (la compañera de gustos distintos)?", "Una amiga, porque acompañó cuando hubo un problema", "No es amiga, porque tiene gustos distintos", "Alguien que está en la lista", "Cumple lo que Bruno pide: ayudar cuando se necesita."),
        ("abc", "{F} Según la definición de Carla, ¿qué es el Caso 3 (comparte gustos, pero se ríe cuando te va mal)?", "Un amigo, aunque no parezca serlo", "No es amigo, porque no ayuda", "No cumple nada de la definición", "Cumple compartir gustos, y eso muestra un problema de la definición."),
        ("ab", "{F} ¿Qué problema tiene la definición de Carla con el Caso 3?", "Es demasiado amplia: cuenta como amigo a alguien que no lo parece", "Es demasiado estrecha: deja fuera a las amistades", "Admite como amigo a quien comparte gustos, aunque se burle de uno; el caso la pone en problemas."),
        ("abc", "{F} ¿Qué problema tiene la definición de Bruno con alguien que fue amigo toda la vida pero nunca tuvo la oportunidad de ayudar?", "Es demasiado estrecha: lo deja fuera", "Es demasiado amplia", "No tiene ningún problema", "No cuenta como amistad lo que no se probó con ayuda."),
        ("abc", "Dos estudiantes discuten si una persona «tiene mucho dinero». Uno dice que sí y el otro que no. ¿Qué conviene hacer primero?", "Pedir precisión: qué significa «mucho» para cada uno", "Votar quién tiene razón", "Cambiar de tema", "Aclarar el término vago permite ver si hay desacuerdo de fondo."),
        ("abc", "Alguien dice: «La banda llegó tarde». ¿Qué hace falta aclarar?", "Cuál de los sentidos de «banda» usa", "Cuántos años tiene la banda", "Quién fundó la banda", "La palabra es ambigua y cambia el sentido de la frase."),
        ("abc", "{F} Un estudiante propone mezclar: «Amigo es quien me ayuda y comparte mis valores». ¿Qué conviene hacer?", "Probarla con casos para ver si es amplia o estrecha", "Aceptarla porque es más larga", "Rechazarla porque mezcla ideas", "Toda definición se prueba con casos."),
        ("abc", "Después de aclarar «amigo», dos personas descubren que usaban la palabra con sentidos distintos pero opinaban lo mismo. ¿Qué tipo de desacuerdo era?", "Verbal", "De fondo", "Sobre un dato", "El desacuerdo desaparece al aclarar el sentido de la palabra."),
        ("abc", "{F} ¿Cuál de estas preguntas ayuda a probar la definición de Ema?", "¿Una persona de mi lista con la que nunca hablé es mi amiga?", "¿Cuántos contactos tengo?", "¿Qué red social uso?", "Pone a prueba la definición con un caso que puede mostrar si es amplia."),
        ("abc", "¿Por qué aclarar conceptos no es perder el tiempo?", "Porque permite saber si el desacuerdo es de fondo o solo de palabras", "Porque evita siempre el desacuerdo", "Porque cada palabra tiene un solo sentido", "Aclarar ayuda a ubicar bien la discrepancia."),
    ],
    ctx=("abc", "En un grupo ficticio, una estudiante dice: «Tener éxito es ganar dinero». Otro pregunta: «¿Una persona que dedica su vida a cuidar un huerto comunitario y gana poco, tiene éxito?». ¿Qué hace la pregunta?", "Prueba la definición con un caso que muestra que podría ser estrecha", "Ataca a la persona", "Cambia de tema", "Usa un caso para ver si la definición deja fuera algo que sí debería entrar."),
    sc=[
        ("En Seminario de filosofía: ¿qué es un desacuerdo verbal?", "El que se debe a usar una palabra con sentidos distintos", "Desaparece cuando se aclara el sentido de la palabra."),
        ("¿Qué dos frases sirven para pedir precisión?", "«¿Qué quieres decir con…?» y «¿puedes dar un ejemplo?»", "Son preguntas que sirven para aclarar los conceptos."),
        ("¿Cuándo una definición es demasiado amplia?", "Cuando deja entrar casos que no deberían entrar", "Incluye en el concepto algo que no corresponde."),
    ],
    op=("Elige una palabra para aclarar con tu grupo: «respeto», «justo» o «éxito». Escribe dos sentidos posibles de la palabra, un caso breve que ponga a prueba cada sentido, una pregunta de precisión que harías en el diálogo y si el desacuerdo parece de fondo o solo de palabras.",
        "Palabra: respeto. Sentidos: (1) obedecer a quien manda; (2) tratar a cada persona como alguien con derechos. Caso: un docente da una orden injusta. Con (1) habría que obedecer; con (2) no necesariamente. Pregunta: «¿Respetar es lo mismo que obedecer?». Desacuerdo: de fondo, porque los sentidos llevan a conductas distintas.",
        ["escribe dos sentidos claros", "propone casos que los ponen a prueba", "formula una pregunta de precisión", "decide si el desacuerdo es verbal o de fondo con una razón"],
        ["dos sentidos, casos, una pregunta de precisión y un juicio sobre el desacuerdo"],
        ["usar sinónimos como definición", "no probar con casos", "no decidir qué tipo de desacuerdo es"],
        "Pregunta: «¿tu caso se interpreta distinto con cada sentido?». Si no, pídele que cambie un detalle."),
    reinforce="Elige tres palabras que uses a diario (por ejemplo, «normal», «justo», «libre») y escribe para cada una si es ambigua o vaga y por qué.",
    extend="Escribe un diálogo breve donde dos personas parecen discrepar y, al aclarar una palabra, descubren que opinaban lo mismo.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (diálogo ficticio). Tema: ¿es correcto publicar la foto de un grupo sin preguntar a todos los que salen? "
     "Joaquín: «Si la foto es del curso, cualquiera puede subirla; es de todos.» "
     "Renata: «Que sea de todos no significa que cada uno haya aceptado salir en un lugar público; uno debería poder decidir cómo aparece.» "
     "Dora: «Yo creo que depende: si fue una actividad abierta, no hay problema; si fue en privado, sí.»")
build(
    O4, 3, F,
    use="Aprenderé a escuchar y reconstruir con fidelidad la postura de otra persona en un diálogo, y a parafrasearla antes de responder.",
    prior=["Sé aclarar conceptos en un diálogo.", "Sé reconstruir tesis y razones.", "Conozco el principio de caridad."],
    explain=[
        "Escuchar activamente es atender a lo que la otra persona dice, no a lo que uno ya piensa responder. Una herramienta es parafrasear: decir con tus palabras lo que entendiste, por ejemplo «si te entiendo bien, sostienes que…». Parafrasear sirve para comprobar que entendiste y para que la otra persona corrija si hace falta. Debe ser fiel: no agregar ni quitar ideas ni exagerar.",
        "En la ficha, Joaquín sostiene que cualquiera puede subir la foto porque es de todos. Renata sostiene que cada persona debe poder decidir cómo aparece, porque que algo sea de todos no implica que todos hayan aceptado exponerse. Dora propone una condición: depende de si la actividad fue abierta o privada. Una buena paráfrasis de Renata sería: «Para ti, aunque la foto sea del grupo, cada persona debería decidir cómo aparece».",
        "Reconstruir con caridad significa presentar la versión más fuerte de la postura de otra persona antes de responder. Una caricatura, como «Renata no quiere que nadie suba nada», deforma y hace fácil la crítica. Reconstruir bien no obliga a estar de acuerdo; permite criticar lo que de verdad se dijo.",
    ],
    vocab=[("escuchar activamente", "atender a lo que dice la otra persona para comprenderla antes de responder"), ("parafrasear", "decir con palabras propias lo que se entendió de otra persona"), ("paráfrasis fiel", "la que no agrega ni quita ideas ni las exagera"), ("caricatura", "versión deformada de una postura, fácil de criticar"), ("condición", "circunstancia de la que depende que una tesis valga")],
    worked=[
        ("Parafrasear a Renata", "Escribe una paráfrasis fiel de lo que dice Renata en la ficha.",
         ["Identifico su tesis: cada persona debería poder decidir cómo aparece.", "Identifico su razón: que algo sea de todos no implica que todos hayan aceptado salir en un lugar público."],
         "«Si te entiendo bien, sostienes que, aunque la foto sea del grupo, cada persona debe decidir cómo aparece»"),
        ("Detectar una caricatura", "Alguien resume a Joaquín como «quiere que todos suban todo sin permiso». ¿Es fiel?",
         ["Releo lo que dijo: que si la foto es del curso, cualquiera puede subirla.", "Habla de una foto del curso, no de subir cualquier cosa de cualquiera."],
         "No: exagera y generaliza su tesis"),
    ],
    mistakes=[("Parafrasear agregando lo que uno piensa («lo que dices es injusto, pero…»).", "Se mezcla la reconstrucción con la crítica.", "Primero parafrasea sin juicios y después responde."),
              ("Resumir a otra persona con una frase extrema para refutarla más fácil.", "Se hace una caricatura.", "Reconstruye la versión más razonable de lo que dijo.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es parafrasear?", "Decir con palabras propias lo que se entendió de otra persona", "Repetir la misma frase sin cambiar nada", "Decir lo que uno piensa de lo que dijo la otra persona", "La paráfrasis comprueba la comprensión sin sumar opiniones."),
        ("abc", "{F} ¿Cuál es la tesis de Joaquín?", "Si la foto es del curso, cualquiera puede subirla", "Nadie debe subir fotos", "Se necesita permiso de todos", "Es lo que sostiene en su frase."),
        ("abc", "{F} ¿Cuál es la razón de Renata?", "Que algo sea de todos no implica que todos hayan aceptado salir en un lugar público", "Que las fotos del curso no deberían existir", "Que la foto es de quien la sacó", "Es la razón que da para su tesis."),
        ("abc", "{F} ¿Qué condición propone Dora?", "Depende de si la actividad fue abierta o privada", "Siempre se debe pedir permiso", "Nunca se debe pedir permiso", "Ofrece una condición de la que depende la respuesta."),
        ("abc", "{F} ¿Cuál es una paráfrasis fiel de Dora?", "«Si te entiendo bien, dices que no hay una sola respuesta: depende de si la actividad fue abierta o privada»", "«Dora no quiere decidir nada»", "«Dora piensa igual que Joaquín»", "Reproduce su idea con palabras propias sin agregar ni deformar."),
        ("ab", "{F} ¿Cuál es una paráfrasis fiel de Joaquín?", "«Para ti, una foto del curso es de todos y por eso cualquiera puede subirla»", "«Para ti, cualquiera puede subir cualquier foto de cualquiera»", "La segunda generaliza más de lo que dijo Joaquín."),
        ("abc", "{F} Un estudiante dice: «Renata quiere prohibir todas las fotos». ¿Qué defecto tiene?", "Es una caricatura: exagera su tesis", "Es una paráfrasis fiel", "Es una pregunta de aclaración", "Renata habla de decidir cómo aparece cada persona, no de prohibir."),
        ("abc", "Antes de responder a una persona con una objeción, ¿qué conviene hacer?", "Parafrasear su postura para comprobar que se entendió", "Corregir su manera de hablar", "Esperar a que se calle y decir lo que ya pensabas", "Verificar la comprensión evita criticar algo que no dijo."),
        ("abc", "{F} ¿Cuál de estas respuestas a Renata empieza con una paráfrasis y no con una crítica?", "«Si te entiendo bien, dices que cada persona debe decidir cómo aparece; mi duda es qué pasa si la actividad fue abierta»", "«Lo que dices es exagerado, igual la foto es del curso»", "«Eso no tiene sentido, porque a todos les gusta salir en fotos»", "Reproduce su idea sin juicios y recién después plantea una duda."),
        ("abc", "{F} ¿Qué pregunta de aclaración se podría hacer a Dora?", "¿Qué entiendes por actividad abierta?", "¿Quién te dio permiso para opinar sobre esto?", "¿No te parece que Joaquín tiene razón?", "Pide precisión de un concepto que usa."),
        ("abc", "¿Por qué reconstruir bien no obliga a estar de acuerdo?", "Porque se puede entender con fidelidad una postura y aun así criticarla", "Porque entender es lo mismo que aceptar", "Porque criticar está prohibido", "La fidelidad se refiere a lo que dijo, no a si es correcto."),
        ("abc", "{F} Si Joaquín dijera «si la foto es del curso, cualquiera puede subirla, siempre que nadie se oponga», ¿qué ocurriría con su postura?", "Se acercaría a la de Renata, porque admite que alguien pueda oponerse", "Sería idéntica a la anterior", "Se opondría totalmente a Renata", "Agrega una condición que reconoce el derecho de cada persona a decidir."),
        ("abc", "¿Qué señal indica que una paráfrasis no es fiel?", "Agrega juicios o exagera lo que se dijo", "Usa palabras distintas", "Es más corta que el original", "Parafrasear permite palabras distintas, pero no cambiar la idea."),
    ],
    ctx=("abc", "En un diálogo ficticio, Ana dice: «Prefiero que los trabajos grupales se evalúen por separado, porque no siempre todos aportan igual». Luis responde: «O sea, no confías en nadie». ¿Qué falla en la respuesta de Luis?", "Deforma la postura de Ana en una caricatura", "Parafrasea con fidelidad", "Pide una precisión", "Ana habla de aportes desiguales, no de desconfianza total."),
    sc=[
        ("En Seminario de filosofía: ¿qué es una paráfrasis fiel?", "La que dice con otras palabras lo mismo, sin agregar ni quitar ideas", "Permite comprobar que se comprendió a la otra persona."),
        ("¿Qué es una caricatura de una postura?", "Una versión deformada, fácil de criticar", "Es lo contrario del principio de caridad."),
        ("¿Qué se hace antes de objetar?", "Se parafrasea la postura para comprobar que se entendió", "Así se critica lo que de verdad se dijo."),
    ],
    op=("Lee este diálogo ficticio: Paula: «Creo que no debería haber celulares en la sala, porque distraen y se pierde la atención.» Martín: «Yo pienso que deben permitirse, porque sirven para buscar información y a veces ayudan a aprender.» "
        "Escribe: (1) una paráfrasis fiel de cada postura, (2) una pregunta de aclaración para cada persona, (3) en qué punto coinciden y en cuál discrepan.",
        "(1) A Paula: «Si te entiendo bien, sostienes que sin celulares hay más atención.» A Martín: «Si te entiendo bien, dices que los celulares pueden ayudar a aprender.» (2) A Paula: ¿qué tipo de distracción te preocupa? A Martín: ¿en qué actividades ayudan? (3) Coinciden en que importa aprender; discrepan en si el celular favorece o perjudica ese fin.",
        ["escribe paráfrasis fieles sin juicios", "formula preguntas de aclaración", "identifica una coincidencia y una discrepancia", "no deforma las posturas"],
        ["dos paráfrasis, dos preguntas y una coincidencia y una discrepancia"],
        ["agregar juicios en la paráfrasis", "caricaturizar una postura", "no encontrar ninguna coincidencia"],
        "Pregunta: «¿quién diría que lo entendió bien al leer tu paráfrasis?». Pídele que la reescriba con las palabras de la persona."),
    reinforce="Elige una opinión que escuches a diario y escribe una paráfrasis fiel y una caricatura de ella, para ver la diferencia.",
    extend="Practica con un compañero: uno defiende una postura en un minuto y el otro la parafrasea; luego cambian roles y anotan qué se entendió mal.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (diálogo ficticio). Tema: ¿es mejor memorizar o tener siempre a mano dónde buscar? "
     "Intervención 1 (Marta): «Memorizar es inútil; todo se puede buscar.» "
     "Intervención 2 (Leo): «¿Quieres decir que no sirve para nada o que sirve poco?» "
     "Intervención 3 (Marta): «Sirve poco, porque la información está siempre disponible.» "
     "Intervención 4 (Iván): «Pero para razonar con rapidez necesitas tener ideas en la cabeza; si buscas todo, no ves relaciones entre ellas.» "
     "Intervención 5 (Dora): «Entonces memorizar y buscar parecen servir para cosas distintas. ¿Qué tareas necesitan cada una?»")
build(
    O4, 4, F,
    use="Aprenderé a intervenir en un diálogo con razones: aclarar, aportar, objetar, sintetizar y cambiar de postura cuando las razones lo piden.",
    prior=["Sé parafrasear una postura.", "Sé aclarar conceptos en un diálogo.", "Sé qué es una objeción."],
    explain=[
        "En un diálogo filosófico hay distintos tipos de intervención. Aclarar es pedir o dar precisión sobre una palabra o una idea. Aportar una razón es ofrecer un motivo que apoya una postura. Objetar es dar una razón contra lo que se dijo. Sintetizar es resumir lo acordado y lo pendiente y abrir una nueva pregunta. Pedir razones es preguntar por qué se sostiene algo. Una buena participación combina estos tipos y responde a lo que dijo la persona anterior.",
        "Mantener un buen diálogo exige evitar algunos errores comunes. Atacar a la persona en vez de a la idea (como «dice eso porque es floja»). Apelar a la mayoría (como «todos buscan en el celular, así que memorizar no sirve»). Presentar solo dos opciones cuando hay más (como «o memorizas todo o no aprendes nada»). Antes de nombrar un error, hay que reconstruir el argumento y mostrar dónde falla.",
        "Cambiar de postura con razones no es perder. En un diálogo filosófico, es una señal de que se está pensando: si una objeción te convence, puedes reformular tu postura. En la ficha, Marta pasa de «inútil» a «sirve poco», y Dora propone distinguir tareas.",
    ],
    vocab=[("aclarar", "pedir o dar precisión sobre una palabra o idea"), ("objetar", "dar una razón contra lo que se dijo"), ("sintetizar", "resumir lo acordado y lo pendiente y abrir una nueva pregunta"), ("pedir razones", "preguntar por qué se sostiene algo"), ("ataque a la persona", "criticar a quien habla en lugar de su idea"), ("apelación a la mayoría", "dar como razón que muchos piensan o hacen algo"), ("falso dilema", "presentar solo dos opciones cuando hay más")],
    worked=[
        ("Clasificar intervenciones", "¿Qué tipo de intervención es la Intervención 2 (Leo)?",
         ["Leo pregunta qué quiere decir «inútil».", "Pide precisión sobre una palabra."],
         "Es una intervención de aclarar"),
        ("Evaluar un cambio de postura", "Marta pasa de «inútil» a «sirve poco». ¿Perdió en el diálogo?",
         ["Veo por qué cambió: respondió a la pregunta de Leo y precisó lo que quería decir.", "El cambio nace de aclarar una idea, no de una derrota."],
         "No: precisó su postura con razones, que es parte de dialogar"),
    ],
    mistakes=[("Responder a una objeción repitiendo la tesis con más fuerza.", "Se sustituye una razón por insistencia.", "Ofrece una razón nueva o ajusta tu postura."),
              ("Decir «es una falacia» sin mostrar dónde falla el argumento.", "Se nombra el error sin reconstruir.", "Reconstruye el argumento y señala la premisa o el paso que falla.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es sintetizar en un diálogo?", "Resumir lo acordado y lo pendiente y abrir una nueva pregunta", "Repetir lo que dijo la otra persona", "Terminar la conversación", "Ayuda a avanzar con lo ya dialogado."),
        ("abc", "{F} ¿Qué tipo de intervención es la Intervención 4 (Iván)?", "Una objeción con razón", "Una aclaración", "Una síntesis", "Da una razón contra la postura de Marta."),
        ("abc", "{F} ¿Qué tipo de intervención es la Intervención 5 (Dora)?", "Una síntesis que abre una nueva pregunta", "Una objeción", "Un ataque a la persona", "Resume que ambas cosas parecen servir para tareas distintas y pregunta cuáles."),
        ("abc", "{F} ¿Qué tipo de intervención es la Intervención 1 (Marta)?", "Una afirmación sin razón", "Una síntesis", "Una aclaración", "Afirma que memorizar es inútil sin dar motivos."),
        ("abc", "{F} ¿Qué razón ofrece Marta en la Intervención 3?", "La información está siempre disponible", "Memorizar es difícil", "Todos buscan en el celular", "Es la razón por la que dice que memorizar sirve poco."),
        ("ab", "{F} ¿Qué cambia en la postura de Marta entre las intervenciones 1 y 3?", "Pasa de «inútil» a «sirve poco», tras la aclaración de Leo", "Pasa de «inútil» a «es necesario»", "La precisión de Leo la lleva a una postura menos extrema, no al polo opuesto."),
        ("abc", "{F} Según Iván, ¿qué se pierde si se busca todo y no se tiene nada en la cabeza?", "Ver las relaciones entre las ideas", "El tiempo para buscar", "La información disponible", "Iván sostiene que, sin ideas propias a mano, no se ven relaciones entre ellas."),
        ("abc", "Un compañero responde a Marta: «Dices eso porque nunca has estudiado de memoria». ¿Qué error comete?", "Ataque a la persona", "Apelación a la mayoría", "Falso dilema", "Critica a quien habla y no a su idea."),
        ("abc", "Otro dice: «Casi todo el curso prefiere buscar antes que memorizar, así que memorizar no vale la pena». ¿Qué error comete?", "Apelación a la mayoría: que muchos lo hagan no prueba que sea correcto", "Ataque a la persona", "Falso dilema", "La cantidad de personas no es una razón por sí misma."),
        ("abc", "Otro más dice: «O el celular reemplaza a la memoria, o la memoria reemplaza al celular». ¿Qué error comete?", "Falso dilema: hay más opciones entre esas dos", "Apelación a la mayoría", "Ataque a la persona", "Presenta solo dos opciones extremas y omite las demás."),
        ("abc", "{F} Para responder a Iván sin repetir la tesis, ¿cuál es una buena intervención de Marta?", "«Puede ser que para razonar sirva memorizar algunas ideas básicas; para el resto, buscar es suficiente»", "«Insisto: memorizar es inútil»", "«Tú solo dices eso porque estudias mucho»", "Responde a la razón de Iván y ajusta su postura."),
        ("abc", "¿Cuál es una buena razón para cambiar de postura en un diálogo?", "Una objeción que muestra un problema real en mi razonamiento", "Que la otra persona hable más fuerte", "Que la mayoría piense distinto", "Cambiar por razones es parte del diálogo filosófico."),
        ("abc", "{F} Alguien dice sobre Marta: «Su argumento es una falacia» y no agrega nada. ¿Qué debería hacer para que su crítica sirva?", "Reconstruir el argumento y mostrar qué premisa o paso falla", "Repetir la palabra falacia", "Preguntarle quién se lo enseñó", "Nombrar el error sin mostrarlo no ayuda a nadie."),
    ],
    ctx=("abc", "En un diálogo ficticio sobre si los apuntes deben escribirse a mano o en pantalla, Clara dice: «A mano es mejor». Benja pregunta: «¿Mejor para qué?». ¿Qué tipo de intervención hace Benja?", "Pedir precisión o razones", "Una síntesis", "Un ataque a la persona", "Pregunta qué criterio usa Clara para decir «mejor»."),
    sc=[
        ("En Seminario de filosofía: ¿qué es un falso dilema?", "Presentar solo dos opciones cuando hay más", "Oculta las alternativas intermedias que sí existen."),
        ("¿Qué es objetar?", "Dar una razón contra lo que se dijo", "Una objeción se dirige a una idea, no a una persona."),
        ("¿Por qué cambiar de postura con razones no es perder?", "Porque muestra que se está pensando y respondiendo a razones", "Es una señal de un buen diálogo."),
    ],
    op=("Elige una pregunta para dialogar con un compañero: «¿conviene que los exámenes sean orales o escritos?», «¿es mejor trabajar solo o en grupo?» o «¿conviene tener horario fijo para estudiar?». "
        "Escribe un diálogo de seis intervenciones entre dos personas ficticias que incluya al menos una aclaración, una razón, una objeción, una síntesis y un cambio de postura con razones.",
        "Pregunta: trabajar solo o en grupo. A: Trabajar solo es mejor (afirmación). B: ¿Mejor para qué? (aclaración). A: Para concentrarse (razón). B: En grupo se pueden corregir errores (objeción). A: Entonces conviene combinar: solo para concentrarse y en grupo para revisar (cambio). B: Parece que cada forma sirve para algo distinto; ¿cuándo usar cada una? (síntesis).",
        ["escribe seis intervenciones coherentes", "incluye los cinco tipos pedidos", "no ataca a la persona", "muestra un cambio de postura con razones"],
        ["diálogo breve de seis intervenciones con los cinco tipos señalados"],
        ["repetir la tesis sin razones", "atacar a la persona", "cambiar de postura sin razones"],
        "Pregunta: «¿en qué línea cambia la postura y por qué razón?». Pídele que la marque."),
    reinforce="Escribe una intervención de cada tipo (aclarar, aportar, objetar, sintetizar) sobre un tema de tu curso.",
    extend="Observa una conversación o foro de ejemplo y escribe dos intervenciones que aporten razones y dos que no, explicando la diferencia.",
)
