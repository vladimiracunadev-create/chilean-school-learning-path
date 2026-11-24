"""Lenguaje y Comunicación EPJA Nivel 2 básico, módulo 2 (parte 1): OAD-05, relacionar información del texto con los conocimientos previos e inferir. Textos no literarios originales, con datos inventados y rotulados; la comprensión oral se trabaja con el guion escrito."""
from __future__ import annotations

from epja_leco_nb2_common import build

O = "EPJA-LECO-NB2-OAD-05"

F1 = ("Aviso de ejemplo (datos inventados): La empresa del agua informa que el jueves habrá corte de agua en el sector Los Aromos, "
      "de 9:00 a 14:00 horas, por trabajos en una tubería. Se pide juntar agua el miércoles en la noche.")
F2 = ("Tres textos de ejemplo. Texto 1, informativo: «La biblioteca del barrio cambió su horario. Desde este lunes abre de 10:00 a 18:00 horas.» "
      "Texto 2, explicativo: «El refrigerador conserva los alimentos porque saca el calor del interior; con menos calor, los microbios se multiplican más lento.» "
      "Texto 3, argumentativo: «Creo que la plaza necesita más basureros, porque los fines de semana los que hay se llenan y la basura queda en el suelo.»")
F3 = ("Nota de ejemplo (datos inventados): El domingo, la calle Los Olmos amaneció con ramas y hojas por todas partes. "
      "En la tarde, vecinos con escobas y bolsas la dejaron limpia. El lunes, un camión retiró las bolsas.")
F4 = ("Columna de ejemplo: Creo que la biblioteca del barrio debería abrir también los sábados. De lunes a viernes cierra a las 18:00, "
      "cuando muchas personas recién salen de sus tareas, y la sala queda vacía. Si abriera el sábado en la mañana, más vecinos podrían pedir libros y usar los computadores.")
F5 = ("Guion de ejemplo para leer en voz alta (datos inventados): «Buenas tardes. La junta de vecinos informa que el sábado, en la sede, habrá un taller de primeros auxilios "
      "de 10:00 a 12:00 horas. Hay 20 cupos. Quien quiera asistir debe inscribirse con la tesorera hasta el miércoles. Se pide llegar con ropa cómoda.»")
F6 = ("Dos frases de un afiche de ejemplo. Frase A: «Si apagas la luz de una pieza vacía, gastas menos electricidad.» "
      "Frase B: «Tus cuentas de la luz bajan si dejas todas las luces prendidas todo el día.»")

build(
    O, 1, F1,
    use="Hoy aprendo a unir lo que dice un aviso con lo que ya sé de la vida diaria para entenderlo mejor.",
    prior=["He leído avisos, carteles y mensajes informativos.", "Sé que un texto da datos como fecha, hora y lugar.", "Puedo contar lo que entendí con mis palabras."],
    explain=[
        "Leer no es solo pasar los ojos por las palabras. Cuando lees, tu cabeza trae lo que ya sabes y lo junta con lo que dice el texto. A eso se le llama relacionar la información con los conocimientos previos.",
        "Los conocimientos previos son lo que aprendiste antes, en la calle, en la casa, en un trámite o en otras lecturas. En el aviso de ejemplo, el texto dice que habrá corte de agua; tú ya sabes que sin agua no se puede cocinar ni lavar. Por eso entiendes por qué piden juntar agua con anticipación.",
        "Un texto no literario es el que sirve para informar, explicar o convencer, como un aviso, una noticia o una carta. Leerlo mejor significa preguntarse: ¿qué dice?, ¿qué sé yo de esto?, ¿qué conclusión puedo sacar? Tu experiencia cuenta y ayuda a entender.",
    ],
    vocab=[("conocimiento previo", "lo que una persona ya sabe antes de leer"), ("relacionar", "unir dos ideas para entenderlas mejor"), ("texto no literario", "texto que informa, explica o convence, no cuenta un cuento"), ("sector", "zona de un barrio o de una ciudad")],
    worked=[
        ("Para qué piden dejar los autos en otra calle", "Aviso de ejemplo (datos inventados): «La junta de vecinos informa que el sábado se cortará el tránsito de la calle Sur, de 8:00 a 12:00 horas, por la feria. Se pide dejar los autos en otra calle el viernes en la noche».", ["El texto dice: la calle Sur se corta el sábado por la feria.", "Yo sé que una feria ocupa la calle con puestos y personas.", "Unidos: piden retirar los autos para que la feria pueda instalarse."], "Piden dejar los autos en otra calle para que la feria pueda ocupar la calle Sur."),
        ("Cuánto dura el corte de tránsito", "El mismo aviso de la calle Sur.", ["El texto da la hora de inicio: 8:00, y la de término: 12:00.", "Yo sé restar horas: de 8 a 12 hay 4 horas.", "Relaciono el dato del texto con mi forma de contar el tiempo."], "El corte de tránsito dura 4 horas."),
    ],
    mistakes=[
        ("Leer solo las palabras y no pensar qué sé del tema.", "Entiendes cada frase suelta, pero no ves por qué el texto pide algo.", "Antes de seguir, pregúntate: ¿qué sé yo de esto?"),
        ("Creer que lo que sé reemplaza al texto y agregar datos que no están.", "El texto manda: tu conocimiento ayuda a entender, no a cambiar lo escrito.", "Verifica que tu idea no contradiga lo que el texto dice."),
    ],
    T=[
        ("abc", "{F} ¿Qué informa este aviso?", "Que habrá un corte de agua el jueves", "Que el agua subirá de precio", "Que se abrirá una nueva tubería para todos", "El primer dato del aviso es el corte de agua del jueves."),
        ("ab", "{F} ¿Cuándo piden juntar agua?", "El miércoles en la noche", "El jueves a las 14:00", "El texto indica la noche del miércoles, antes del corte."),
        ("=", "{F} Si el corte parte a las 9:00 y termina a las 14:00, ¿cuántas horas dura?", "14-9", "De las 9 a las 14 hay 5 horas, porque 14 menos 9 es 5.", "horas"),
        ("abc", "{F} ¿Qué conocimiento previo explica que pidan juntar agua?", "Sin agua no se puede cocinar ni lavar", "Los jueves siempre se corta el agua", "Las tuberías son de metal", "Saber que el agua se usa a diario explica la petición del aviso."),
        ("ab", "{F} Una persona dice: «Entiendo el aviso porque sé que las reparaciones cortan el servicio». ¿Qué hizo?", "Relacionó el texto con lo que ya sabía", "Copió el aviso sin pensarlo", "Usó un conocimiento previo para entender la causa de los trabajos."),
        ("{F} ¿En qué sector será el corte? (una o dos palabras)", "Los Aromos", "El aviso nombra el sector de Los Aromos."),
        ("abc", "{F} ¿Cuál es una buena pregunta para relacionar el aviso con lo que sé?", "¿Qué necesito tener listo si no hay agua?", "¿De qué color es la tubería?", "¿Cuántas letras tiene el aviso?", "Esa pregunta une el texto con tu experiencia y sirve para decidir qué hacer."),
        ("ab", "{F} ¿Qué dato NO está en el aviso?", "Cuánta agua hay que juntar en litros", "La hora de inicio del corte", "El aviso no dice litros; sí da la hora, el sector y el día."),
        ("{F} ¿Qué día de la semana es el corte?", "jueves", "El aviso dice que el corte es el jueves."),
        ("ab", "{F} Una persona dice: «Seguro el corte durará hasta la noche». ¿Se apoya en el texto?", "No, el aviso dice que termina a las 14:00", "Sí, porque los trabajos se alargan siempre", "El texto fija el término a las 14:00; lo demás es adivinar."),
        ("abc", "{F} ¿Qué hace una persona que lee bien este aviso?", "Une lo que dice con lo que sabe y se prepara", "Lo lee sin detenerse en los datos", "Supone que el corte es solo para otro sector", "Leer bien es relacionar el texto con la experiencia propia."),
        ("abc", "Un aviso de ejemplo dice: «Mañana se cerrará el paso por la calle Sur por una feria». ¿Qué conocimiento previo ayuda a entender?", "Las ferias ocupan la calzada y por eso se cierra", "Todos los días hay ferias", "Las calles cerradas no existen", "Saber cómo funciona una feria explica por qué se cierra la calle."),
        ("ab", "Un texto dice «Lleve su cédula». Una persona piensa: «La piden para comprobar quién soy, como en otros trámites». ¿Qué usó?", "Un conocimiento previo", "Un dato del texto que no existe", "Recordó una experiencia anterior para entender el motivo de la petición."),
    ],
    ctx=("abc", "Llega a una sede vecinal este aviso de ejemplo: «Por mantención, el ascensor del edificio estará sin servicio el lunes». ¿Qué relación con lo que ya sabes ayuda a decidir qué hacer ese día?", "Sin ascensor habrá que usar las escaleras o planificar con más tiempo", "El lunes es el primer día de la semana", "Los ascensores son siempre lentos", "El conocimiento de cómo se usa un ascensor lleva a anticipar qué cambia ese día."),
    sc=[("En Lenguaje EPJA: ¿qué es un conocimiento previo al leer?", "Lo que ya sé antes de leer", "Es la experiencia que ayuda a entender el texto."),
        ("¿Para qué relaciono lo que leo con lo que sé?", "Para entender mejor y sacar conclusiones", "Unir ambas cosas permite comprender el motivo y las consecuencias."),
        ("¿Qué mando sobre mi idea: el texto o mi memoria?", "El texto", "Mi conocimiento ayuda a entender, pero no puede contradecir lo escrito.")],
    op=("Lee este aviso de ejemplo: «El sábado habrá una feria de intercambio de libros en la plaza, de 11:00 a 15:00 horas. Traiga los libros limpios». Escribe: 1) tres datos que da el aviso, 2) un conocimiento previo tuyo que ayuda a entenderlo y 3) una oración que una ambos.",
        "Datos: sábado, plaza, de 11:00 a 15:00. Conocimiento: en un intercambio cada persona lleva un libro y se lleva otro. Oración: Como en un intercambio se llevan y se reciben libros, entiendo que debo traer libros limpios para dejarlos a otras personas.",
        ["anota tres datos del aviso", "nombra un conocimiento previo", "escribe una oración que une ambas cosas"],
        ["tres datos, un conocimiento y una oración"],
        ["agregar datos que el aviso no da", "escribir solo el conocimiento sin relacionarlo"],
        "Pregunta: «¿Mi oración dice algo que el aviso no contradice?»."),
    reinforce="Lee un aviso cualquiera y escribe qué sabías tú antes que ayuda a entenderlo.",
    extend="Busca un texto informativo breve y marca con color qué datos son del texto y cuáles son tu conocimiento previo.",
)

build(
    O, 2, F2,
    use="Hoy distingo textos que informan, explican o convencen, encuentro su idea central y entiendo palabras nuevas por el contexto.",
    prior=["Leí un aviso y lo relacioné con lo que sé.", "Sé que un texto puede dar datos, razones u opiniones.", "Reconozco palabras que conozco y otras que no."],
    explain=[
        "Los textos no literarios se parecen en que tratan temas reales, pero no tienen el mismo propósito. Un texto informativo da datos: qué pasó, cuándo y dónde. Un texto explicativo cuenta cómo funciona algo o por qué ocurre. Un texto argumentativo defiende una opinión con razones.",
        "La idea central es lo más importante que quiere decir el texto, en una sola oración. Si una nota dice «El taller de costura cambió su horario: ahora comienza a las 19:00», la idea central es que cambió el horario del taller. Las demás frases la completan.",
        "Si aparece una palabra que no conoces, mira las frases de alrededor: el contexto da pistas. En el texto 3, «basureros» se entiende porque se habla de basura en el suelo. Tu conocimiento previo también ayuda a adivinar el significado.",
    ],
    vocab=[("texto informativo", "texto que da datos sobre algo"), ("texto explicativo", "texto que cuenta cómo o por qué ocurre algo"), ("texto argumentativo", "texto que defiende una opinión con razones"), ("idea central", "lo más importante que dice un texto")],
    worked=[
        ("Reconocer el tipo de texto", "«Creo que la sede debería tener una cartelera, porque muchos avisos se pierden en las puertas».", ["Hay una opinión: «Creo que la sede debería tener una cartelera».", "Hay una razón: «porque muchos avisos se pierden en las puertas».", "Una opinión con razón es propio de un texto argumentativo."], "Es un texto argumentativo."),
        ("Idea central de una nota", "«El taller de computación empezará el lunes 3. Las clases serán a las 19:00 horas, en la sede. Quedan pocos cupos».", ["La primera oración dice qué pasa: empieza un taller.", "Las otras dan el horario, el lugar y el aviso de cupos.", "La idea que reúne todo es el inicio del taller de computación."], "Empieza un taller de computación."),
    ],
    mistakes=[
        ("Decir que un texto es informativo solo porque habla de un tema real.", "También los textos que explican o convencen tratan temas reales.", "Fíjate en el propósito: ¿da datos, explica un proceso o defiende una opinión?"),
        ("Tomar un detalle como idea central.", "Un detalle es parte del texto, pero la idea central reúne todo.", "Pregúntate: ¿de qué trata todo el texto en una oración?"),
    ],
    T=[
        ("abc", "{F} ¿Qué tipo de texto es el texto 1?", "Informativo", "Argumentativo", "Explicativo", "Da datos sobre el horario de la biblioteca sin explicar un proceso ni defender una opinión."),
        ("abc", "{F} ¿Qué tipo de texto es el texto 2?", "Explicativo", "Informativo", "Argumentativo", "Cuenta por qué el refrigerador conserva los alimentos."),
        ("ab", "{F} ¿Qué tipo de texto es el texto 3?", "Argumentativo", "Informativo", "Contiene la opinión «Creo que...» y una razón que la apoya."),
        ("abc", "{F} ¿Cuál es la idea central del texto 2?", "El refrigerador conserva los alimentos al sacar el calor", "Los microbios son animales grandes", "Los refrigeradores se venden en tiendas", "La oración reúne la explicación completa del texto."),
        ("ab", "{F} En el texto 1, ¿qué dato es nuevo?", "El horario de 10:00 a 18:00 horas", "El nombre del dueño de la biblioteca", "El texto dice que el horario cambió y cuál es el nuevo."),
        ("{F} ¿Con qué palabra comienza la opinión del texto 3? (una palabra)", "Creo", "La opinión se marca con «Creo que»."),
        ("abc", "{F} En el texto 2, ¿qué significa «se multiplican»?", "Hay cada vez más", "Se secan", "Se esconden", "«Se multiplican» significa que su cantidad aumenta; con menos calor lo hacen más lento."),
        ("ab", "{F} ¿Qué razón da el texto 3 para pedir más basureros?", "Que los que hay se llenan los fines de semana", "Que la plaza es muy grande", "La razón sigue a la palabra «porque»."),
        ("=", "{F} En el texto 1, la biblioteca abre de 10:00 a 18:00. ¿Cuántas horas al día está abierta?", "18-10", "De 10 a 18 hay 8 horas, porque 18 menos 10 es 8.", "horas"),
        ("abc", "{F} Una persona dice que el texto 3 informa que habrá más basureros. ¿Qué error cometió?", "No notó que es una opinión y no un dato confirmado", "Leyó el texto 1 en vez del 3", "Confundió la hora de la biblioteca", "El texto 3 pide más basureros; no anuncia que los habrá."),
        ("ab", "{F} ¿Cuál texto explica por qué ocurre algo?", "El texto 2", "El texto 1", "Solo el 2 explica una causa y su efecto."),
        ("abc", "Texto de ejemplo: «El pan se hace con harina, agua, sal y levadura. La levadura produce gas, y por eso la masa sube». ¿Qué tipo de texto es?", "Explicativo", "Argumentativo", "Informativo", "Cuenta cómo ocurre el proceso: la masa sube por el gas de la levadura."),
        ("ab", "Texto de ejemplo: «Pienso que el bus debería pasar cada diez minutos, porque en la mañana se acumula mucha gente». ¿Cuál es la razón?", "Porque en la mañana se acumula mucha gente", "Que el bus pase cada diez minutos", "La razón es lo que sigue a «porque»; lo otro es lo que se pide."),
    ],
    ctx=("abc", "Una sede vecinal publica tres notas de ejemplo. Nota 1: «El taller de costura empieza el martes». Nota 2: «La costura a máquina une las telas porque el hilo de arriba y el de abajo se enlazan». Nota 3: «Creo que el taller debería tener más sesiones, porque hay lista de espera». ¿Cuál es la argumentativa?", "La nota 3", "La nota 1", "La nota 2", "Solo la nota 3 defiende una opinión con una razón."),
    sc=[("En Lenguaje: ¿qué hace un texto explicativo?", "Cuenta cómo o por qué ocurre algo", "Su propósito es explicar un proceso o una causa."),
        ("En Lenguaje: ¿qué es la idea central de un texto?", "Lo más importante del texto en una oración", "Reúne lo que dice todo el texto."),
        ("¿Cómo averiguo una palabra nueva?", "Mirando las frases de alrededor", "El contexto da pistas sobre su significado.")],
    op=("Lee estos tres textos de ejemplo. A: «El consultorio atenderá hoy hasta las 17:00». B: «Las nubes se forman cuando el vapor de agua se enfría y se junta en gotitas muy pequeñas». C: «Pienso que el consultorio debería atender hasta más tarde, porque hay personas que salen tarde de sus tareas». Escribe qué tipo es cada uno y la idea central de uno de ellos.",
        "A: informativo. B: explicativo. C: argumentativo. Idea central de C: el consultorio debería atender hasta más tarde.",
        ["clasifica los tres textos", "escribe la idea central de uno", "usa las palabras informativo, explicativo y argumentativo"],
        ["tres clasificaciones y una idea central"],
        ["confundir opinión con dato", "copiar el texto entero como idea central"],
        "Pregunta: «¿Mi idea central cabe en una sola oración?»."),
    reinforce="Elige tres textos cortos (un aviso, una nota y una opinión) y di de qué tipo es cada uno.",
    extend="Escribe un texto de tres oraciones que explique cómo hacer algo sencillo y señala su idea central.",
)

build(
    O, 3, F3,
    use="Hoy aprendo a hacer una inferencia: unir una pista del texto con lo que sé para sacar una conclusión que el texto no dice.",
    prior=["Sé unir lo que leo con lo que ya sé.", "Distingo textos que informan, explican y convencen.", "Sé identificar los datos que da un texto."],
    explain=[
        "Una inferencia es una conclusión que sacas cuando juntas lo que dice el texto con lo que ya sabes. El texto no la dice con palabras, pero está apoyada en sus pistas. Es como cuando ves la calle mojada y piensas que llovió.",
        "Para inferir, sigue cuatro pasos. Primero, lee y subraya los datos del texto. Segundo, recuerda qué sabes tú de esa situación. Tercero, une ambas cosas y piensa una conclusión posible. Cuarto, comprueba que ningún dato del texto la contradiga.",
        "Si entras a una casa y ves muchos zapatos en la entrada, puedes inferir que hay visitas. Tú sabes que las visitas llegan con su calzado puesto. Entonces la conclusión es probable. Es probable, no seguro: por eso se dice «se puede inferir» y no «el texto asegura».",
    ],
    vocab=[("inferir", "sacar una conclusión a partir de pistas y de lo que ya se sabe"), ("pista", "dato del texto que ayuda a concluir algo"), ("probable", "que es lo más posible según las pistas"), ("contradecir", "decir lo contrario de lo que dice otra cosa")],
    worked=[
        ("Inferir la causa", "Nota de ejemplo: «El martes, al abrir la sede, Rosa encontró el piso mojado, un balde en el centro de la sala y una mancha en el techo».", ["Pistas del texto: piso mojado, balde y mancha en el techo.", "Lo que yo sé: un balde bajo una mancha en el techo se usa para recibir el agua que gotea.", "Unidos: lo más probable es que haya llovido y el techo tenga una gotera."], "Probablemente hubo lluvia y el techo gotea."),
        ("Comprobar la inferencia", "La misma nota de la sede.", ["Mi inferencia: el techo tiene una gotera.", "Reviso el texto: ningún dato dice que el piso se mojara por otro motivo.", "El balde y la mancha calzan con una gotera."], "La inferencia es razonable porque el texto no la contradice y las pistas la apoyan."),
    ],
    mistakes=[
        ("Decir «el texto dice que hubo viento».", "El texto no lo dice: lo concluyes tú a partir de pistas.", "Escribe «se puede inferir que hubo viento»."),
        ("Inventar una conclusión sin pistas, por ejemplo «hubo una fiesta en la calle».", "Ningún dato del texto apoya esa idea.", "Antes de concluir, nombra la pista del texto que la apoya."),
    ],
    T=[
        ("abc", "{F} ¿Qué amaneció con ramas y hojas por todas partes?", "La calle Los Olmos", "La plaza", "El techo de una casa", "El texto lo dice en la primera oración."),
        ("ab", "{F} ¿Quiénes dejaron limpia la calle?", "Vecinos con escobas y bolsas", "Un camión municipal", "El texto indica que fueron vecinos; el camión retiró las bolsas."),
        ("{F} ¿Qué día retiró las bolsas el camión?", "lunes", "El texto dice «El lunes, un camión retiró las bolsas»."),
        ("abc", "{F} ¿Qué inferencia se apoya mejor en las pistas?", "Probablemente hubo mucho viento en la noche", "Seguramente hubo una gran fiesta", "Es seguro que nadie ayudó", "Las ramas y hojas por todas partes apuntan al viento y no a una fiesta."),
        ("ab", "{F} ¿Cuál es una pista del texto?", "La calle amaneció con ramas y hojas", "Los vecinos son amables", "Es un dato escrito; la amabilidad es una suposición."),
        ("abc", "{F} Una persona infiere que los vecinos se organizaron. ¿Qué pista lo apoya?", "Varios vecinos limpiaron juntos con escobas y bolsas", "El camión era blanco", "La calle se llama Los Olmos", "Que varios vecinos actuaran en la tarde muestra organización."),
        ("ab", "{F} ¿Qué conocimiento previo apoya la inferencia de que hubo viento?", "El viento fuerte quiebra ramas", "Las bolsas son de plástico", "Es la experiencia que une la pista con la conclusión."),
        ("abc", "{F} ¿Cuál inferencia es la más débil porque no tiene pistas?", "Hubo un desfile por la calle el sábado", "Hubo viento fuerte durante la noche", "Los vecinos limpiaron juntos", "Ningún dato del texto menciona un desfile."),
        ("ab", "{F} Alguien afirma: «El texto dice que hubo temporal». ¿Es correcto?", "No, es una inferencia y no una palabra del texto", "Sí, porque amaneció con hojas", "El texto no menciona temporal: es una conclusión que se saca."),
        ("abc", "{F} ¿Qué paso falta? 1) Subrayar los datos. 2) Recordar qué sé. 3) Unir pista y conocimiento. 4) …", "Comprobar que el texto no contradiga la conclusión", "Cambiar el texto", "Copiar el texto completo", "El cuarto paso es verificar que la conclusión no choque con lo escrito."),
        ("abc", "Nota de ejemplo: «En la fila del consultorio había mucha gente con paraguas y las veredas brillaban». ¿Qué se puede inferir?", "Probablemente estaba lloviendo o había llovido", "Que el consultorio estaba cerrado", "Que era verano", "Los paraguas y las veredas brillantes son pistas de lluvia."),
        ("ab", "Texto de ejemplo: «Marta guardó la bufanda y abrió todas las ventanas». ¿Qué se puede inferir sobre la temperatura?", "Hacía calor", "Hacía mucho frío", "Quien guarda la bufanda y ventila suele estar con calor."),
        ("ab", "Texto de ejemplo: «El vecino llegó con las manos llenas de tierra y una pala». ¿Qué se puede inferir?", "Probablemente estuvo trabajando en un jardín o huerta", "Estaba pintando una pared", "La tierra y la pala son pistas de trabajo en un jardín."),
    ],
    ctx=("abc", "En un taller se lee la nota de ejemplo: «La panadería puso un cartel que dice \"Hoy no hay pan integral\" y la fila dio la vuelta a la esquina». ¿Qué inferencia se apoya en las pistas?", "Que había mucha gente que quería comprar pan aunque faltara el integral", "Que no quedaba ningún tipo de pan", "Que nadie quería comprar pan", "La fila larga es una pista de que había demanda aunque faltara un tipo de pan."),
    sc=[("En Lenguaje: ¿qué es una inferencia al leer?", "Una conclusión a partir de pistas y de lo que sé", "No está escrita, pero se apoya en el texto."),
        ("¿Qué debo comprobar al terminar de inferir?", "Que el texto no contradiga mi conclusión", "Una conclusión válida no choca con los datos."),
        ("¿Cómo escribo una inferencia sin afirmar de más?", "Con «se puede inferir» o «probablemente»", "Marca que es una conclusión y no un dato del texto.")],
    op=("Lee esta nota de ejemplo: «Al llegar a la sede, Pedro vio la puerta con candado, las luces apagadas y un papel pegado con la palabra \"Suspendido\"». Escribe dos inferencias, cada una con la pista del texto y lo que tú sabes que las une.",
        "Inferencia 1: la reunión se suspendió. Pista: el papel dice «Suspendido». Conocimiento: los avisos de suspensión se pegan en la puerta. Inferencia 2: no hay nadie dentro. Pista: luces apagadas y candado. Conocimiento: una sede abierta tiene luz y puerta sin candado.",
        ["escribe dos inferencias", "nombra la pista de cada una", "nombra el conocimiento previo de cada una"],
        ["dos inferencias con pista y conocimiento"],
        ["dar una conclusión sin pista", "decir que el texto lo afirma"],
        "Pregunta: «¿Puedo señalar con el dedo la pista en el texto?»."),
    reinforce="Mira una situación de la calle y escribe una inferencia con su pista.",
    extend="Escribe una nota de tres oraciones con pistas para que otra persona infiera lo que ocurrió.",
)

build(
    O, 4, F4,
    use="Hoy practico inferencias en un texto argumentativo y distingo lo que se puede concluir de lo que solo se supone.",
    prior=["Sé inferir con pistas y conocimiento previo.", "Reconozco la opinión y la razón de un texto.", "Comparo mi conclusión con lo escrito."],
    explain=[
        "En un texto argumentativo, quien escribe defiende una opinión. A veces no dice todo con palabras: deja ideas implícitas que tú puedes inferir. Por ejemplo, si dice que «los pasillos están llenos de gente esperando», puedes inferir que hay mucha demanda por ese servicio.",
        "Hay inferencias bien apoyadas y suposiciones sin base. La inferencia se apoya en una pista del texto. La suposición agrega datos que no están. En la columna de ejemplo se puede inferir que quien escribe quiere más horas de atención; no se puede asegurar que existan muchos computadores, solo que existen algunos.",
        "Para evaluar lo que lees, pregúntate también si la razón convence con lo que tú sabes. Una razón es buena si es verdadera y se relaciona con la opinión. Estar de acuerdo o no es decisión tuya; lo importante es apoyarla con el texto.",
    ],
    vocab=[("implícito", "que no está dicho con palabras, pero se entiende"), ("suposición", "idea que se agrega sin tener pistas en el texto"), ("razón", "motivo que se da para apoyar una opinión"), ("horario", "horas en que algo está abierto o funciona")],
    worked=[
        ("Inferir lo que quiere quien escribe", "Columna de ejemplo: «Creo que la plaza debería tener más bancas, porque las personas mayores no tienen dónde sentarse mientras esperan el bus».", ["Pistas: «más bancas» y «no tienen dónde sentarse».", "Lo que sé: si faltan bancas, las personas esperan de pie.", "Inferencia: quien escribe cree que hoy hay pocas bancas junto a la parada."], "Cree que hoy hay pocas bancas para quienes esperan el bus."),
        ("Separar inferencia y suposición", "La misma columna de las bancas.", ["«Las personas esperan el bus cerca de la plaza»: el texto da esa pista, así que la inferencia es posible.", "«Hay veinte personas mayores esperando»: el texto no da cifras, es una suposición.", "Me quedo con lo que tiene pista."], "Es inferencia lo primero; lo segundo es suposición."),
    ],
    mistakes=[
        ("Aceptar una suposición como si fuera inferencia.", "No hay ninguna pista en el texto que la apoye.", "Pide la pista: ¿qué frase del texto lo permite?"),
        ("Rechazar la razón del texto solo porque no comparto la opinión.", "Evaluar es revisar si la razón es verdadera y se relaciona con la opinión, no solo si me gusta.", "Primero entiende la razón; después decide si te convence."),
    ],
    T=[
        ("abc", "{F} ¿Qué opinión defiende la columna?", "Que la biblioteca abra también los sábados", "Que la biblioteca cierre más temprano", "Que se vendan libros nuevos", "La opinión aparece con «Creo que… debería abrir también los sábados»."),
        ("ab", "{F} ¿A qué hora cierra la biblioteca de lunes a viernes?", "A las 18:00", "A las 10:00", "El texto dice que cierra a las 18:00."),
        ("{F} ¿Qué día se propone abrir además de los días de lunes a viernes? (una palabra)", "sábado", "La opinión pide abrir el sábado."),
        ("abc", "{F} ¿Qué razón da la columna?", "Que después de las 18:00 muchas personas recién pueden ir", "Que los libros son caros", "Que la biblioteca es nueva", "La razón central es que cierra cuando muchas personas recién terminan sus tareas."),
        ("ab", "{F} ¿Qué se puede inferir de «la sala queda vacía»?", "Que a esa hora casi nadie usa la sala", "Que la sala se incendió", "Una sala vacía indica poco uso en ese horario."),
        ("abc", "{F} ¿Qué inferencia es la mejor apoyada?", "Quien escribe cree que un horario más amplio serviría a más personas", "Quien escribe es el director de la biblioteca", "La biblioteca no tiene libros", "La opinión y la razón apuntan a ampliar el acceso."),
        ("ab", "{F} Alguien dice que la biblioteca tiene 40 computadores. ¿Qué es eso?", "Una suposición, porque el texto no da la cifra", "Una inferencia, porque se ve en el texto", "El texto menciona computadores, pero no cuántos."),
        ("abc", "{F} ¿Qué conocimiento previo apoya la razón de la columna?", "Muchas personas terminan sus tareas a una hora tardía y no alcanzan a ir", "Todos los sábados llueve", "Los libros se prestan por un mes", "Es una experiencia común que explica por qué un cierre temprano deja a gente fuera."),
        ("ab", "{F} ¿Es verdadero decir «El texto asegura que más vecinos usarán la biblioteca»?", "No, solo dice que podrían usarla", "Sí, lo asegura con una cifra", "El verbo «podrían» expresa una posibilidad, no un hecho seguro."),
        ("abc", "{F} Una persona dice: «No estoy de acuerdo, pero la razón del texto es clara». ¿Qué hizo bien?", "Entendió la razón antes de evaluarla", "Ignoró el texto", "Copió la columna", "Evaluó sin dejar de comprender el argumento del texto."),
        ("ab", "{F} ¿Qué cambio haría más fuerte la razón de la columna?", "Agregar un dato de cuántas personas piden el sábado", "Escribir la columna más corta", "Un dato concreto apoya la razón mejor que una frase general."),
        ("abc", "Columna de ejemplo: «Creo que el bus debería llegar hasta la plaza, porque hoy hay que caminar quince cuadras con bolsas pesadas». ¿Qué se puede inferir?", "Que a quien escribe le cuesta llegar caminando con carga", "Que la plaza está cerrada", "Que el bus ya llega hasta la plaza", "La razón apunta a la dificultad de caminar con carga."),
        ("ab", "Texto de ejemplo: «Pido que la feria no termine tan temprano, porque a las 13:00 ya no queda verdura». ¿Qué se infiere de la hora?", "Que la verdura se acaba temprano", "Que la feria abre a las 13:00", "Si ya no queda verdura a las 13:00, se agotó antes."),
    ],
    ctx=("abc", "Se lee en una reunión de vecinos una carta de ejemplo: «Creo que la luminaria de la esquina debería arreglarse, porque desde que se apagó hay que caminar a oscuras». ¿Qué se puede inferir para decidir qué pedir?", "Que la esquina es menos segura sin luz y que piden arreglar la luminaria", "Que ya la arreglaron", "Que la esquina no se usa", "Caminar a oscuras es la pista que justifica el arreglo."),
    sc=[("¿Qué diferencia hay entre inferencia y suposición?", "La inferencia se apoya en una pista; la suposición no", "Solo la inferencia tiene apoyo en el texto."),
        ("En Lenguaje: ¿qué es una razón en un texto argumentativo?", "El motivo que apoya una opinión", "Sin razón, una opinión queda sin respaldo."),
        ("¿Qué pregunto para comprobar una inferencia?", "¿Qué frase del texto la apoya?", "La pista debe poder señalarse en una frase concreta del texto.")],
    op=("Lee esta carta de ejemplo: «Creo que la sede debería prestar sillas de ruedas para los eventos del barrio, porque algunas personas no pueden llegar caminando hasta el patio». Escribe: 1) la opinión, 2) la razón, 3) una inferencia con su pista y 4) una suposición que NO se puede apoyar en el texto.",
        "Opinión: que la sede preste sillas de ruedas. Razón: algunas personas no pueden llegar caminando hasta el patio. Inferencia: el patio queda lejos o es de difícil acceso (pista: «no pueden llegar caminando»). Suposición: que la sede ya tiene diez sillas.",
        ["identifica opinión y razón", "escribe una inferencia con su pista", "da una suposición sin apoyo y la reconoce como tal"],
        ["cuatro respuestas breves"],
        ["tomar la suposición como dato", "no nombrar la pista"],
        "Pregunta: «¿Mi inferencia puede apoyarse en una frase concreta?»."),
    reinforce="Lee una opinión breve y subraya la razón; luego escribe qué se infiere de ella.",
    extend="Escribe una opinión de dos oraciones con una razón implícita y pide a alguien que infiera cuál es.",
)

build(
    O, 5, F5,
    use="Hoy aplico estrategias de comprensión en un texto escuchado: tomo notas clave, infiero lo que no se dijo y pregunto lo que falta.",
    prior=["Sé inferir con pistas.", "Distingo datos de opiniones.", "Puedo escuchar o leer un anuncio y anotar lo principal."],
    explain=[
        "La comprensión oral es entender lo que se dice en voz alta, como un anuncio en una reunión. Aquí usamos el guion escrito: si quieres, que otra persona lo lea en voz alta. Como al escuchar no puedes volver atrás, conviene tomar notas con palabras clave.",
        "Las estrategias de comprensión son pasos que ayudan a entender: antes, anticipa de qué trata; durante, anota quién, qué, cuándo y dónde; después, repasa y haz preguntas por lo que falta. Si algo no queda claro, pedir que lo repitan es parte de entender bien.",
        "En el guion de ejemplo hay datos y también pistas. «Llegar con ropa cómoda» no dice qué se hará, pero tú puedes inferir que el taller incluirá movimiento o práctica. Aplicar lo que sabes ayuda a completar lo que no se dijo.",
    ],
    vocab=[("comprensión oral", "entender lo que otra persona dice en voz alta"), ("palabra clave", "palabra que guarda lo más importante de una frase"), ("cupo", "lugar disponible para una persona"), ("inscribirse", "anotar el nombre para participar")],
    worked=[
        ("Tomar notas del guion", "Guion de ejemplo: «El jueves, en la biblioteca, habrá una charla sobre cuidado de la voz, de 18:00 a 19:00 horas. Hay 30 cupos. La inscripción es en el mesón hasta el martes. Se ruega puntualidad».", ["Qué: charla sobre cuidado de la voz. Cuándo: jueves, 18:00 a 19:00.", "Dónde: en la biblioteca. Cupos: 30.", "Cómo inscribirse: en el mesón, hasta el martes."], "Las notas reúnen los datos clave: qué, cuándo, dónde, cupos e inscripción."),
        ("Inferir con una pista", "El mismo guion de la charla.", ["La pista: «Se ruega puntualidad».", "Lo que sé: se pide puntualidad cuando una actividad parte a una hora exacta.", "Inferencia: lo más probable es que la charla comience a las 18:00 en punto."], "Probablemente la charla comience puntual."),
    ],
    mistakes=[
        ("Tratar de anotar todo palabra por palabra.", "Mientras escribes se pierde lo que sigue.", "Anota solo palabras clave: quién, qué, cuándo, dónde."),
        ("Quedarse con una duda y no preguntar.", "Sin ese dato puede perderse la inscripción u otro paso importante.", "Haz la pregunta o pide que repitan al final."),
    ],
    T=[
        ("abc", "{F} ¿Sobre qué es el taller?", "Primeros auxilios", "Cocina", "Pintura", "El guion nombra un taller de primeros auxilios."),
        ("ab", "{F} ¿Dónde será el taller?", "En la sede", "En la plaza", "El guion dice «en la sede»."),
        ("=", "{F} El taller es de 10:00 a 12:00 horas. ¿Cuántas horas dura?", "12-10", "De 10 a 12 hay 2 horas, porque 12 menos 10 es 2.", "horas"),
        ("abc", "{F} ¿Con quién debe inscribirse quien quiera asistir?", "Con la tesorera", "Con el presidente", "Con quien hace el taller", "El guion lo dice de forma directa."),
        ("{F} ¿Cuántos cupos hay? (un número)", "20", "El guion dice «Hay 20 cupos»."),
        ("ab", "{F} ¿Hasta cuándo se puede inscribir?", "Hasta el miércoles", "Hasta el sábado", "El plazo es el miércoles, antes del taller."),
        ("abc", "{F} ¿Qué palabras clave conviene anotar de este guion?", "Sábado, sede, 10:00 a 12:00, 20 cupos, tesorera, miércoles", "Buenas tardes, la, de, en", "Solo «Buenas tardes»", "Las palabras clave guardan los datos que se necesitan."),
        ("ab", "{F} ¿Qué se puede inferir de que haya solo 20 cupos?", "Que conviene inscribirse pronto", "Que el taller será gratis para todos", "Los cupos limitados hacen que los lugares se acaben."),
        ("abc", "{F} ¿Qué pregunta ayuda a completar información que falta?", "¿Hay que llevar algo más aparte de ropa cómoda?", "¿Cuántas palabras tiene el guion?", "¿Quién escribió el guion con lápiz?", "Esa pregunta pide un dato útil que el guion no da."),
        ("ab", "{F} ¿Qué estrategia usa quien anota «qué, cuándo, dónde» al escuchar?", "Tomar notas con palabras clave", "Memorizar sin anotar", "Las notas breves permiten recordar los datos esenciales."),
        ("abc", "{F} ¿Cuál de estas ideas NO se puede afirmar con el guion?", "Que el taller es gratuito", "Que hay 20 cupos", "Que es en la sede", "El guion no dice nada sobre costo."),
        ("abc", "Guion de ejemplo: «Les recordamos que la reunión empieza en cinco minutos y se necesita traer el cuaderno de actas». ¿Qué se puede inferir?", "Que se tomará nota de lo que se acuerde", "Que la reunión será al día siguiente", "Que no habrá reunión", "El cuaderno de actas se usa para anotar lo acordado."),
        ("ab", "Guion de ejemplo: «El bus no pasará por la calle Norte hoy; tome el paradero de la plaza». ¿Qué se puede inferir?", "Que la calle Norte tiene algún problema ese día", "Que la plaza se cerró", "Si desvían el bus, hay un motivo en la calle Norte."),
    ],
    ctx=("abc", "En una reunión se lee el guion de ejemplo: «El miércoles se entregarán las canastas de verduras de 15:00 a 17:00 en la sede; cada persona retira una y debe firmar». Quien anota usa palabras clave. ¿Cuál es la nota más útil?", "Miércoles, 15:00 a 17:00, sede, una canasta, firmar", "Verduras buenas", "Reunión larga", "La nota reúne cuándo, dónde, cuánto y qué hacer."),
    sc=[("¿Qué conviene anotar al escuchar un anuncio?", "Palabras clave: qué, cuándo, dónde y cómo", "No se puede volver atrás, por eso se anota lo esencial."),
        ("¿Qué hago si algo no quedó claro?", "Preguntar o pedir que lo repitan", "Preguntar a tiempo evita errores y olvidos."),
        ("¿Se puede inferir algo que no se dijo?", "Sí, si hay una pista y lo que sé", "La pista y el conocimiento sostienen la inferencia.")],
    op=("Pide a otra persona que lea en voz alta, o léelo tú, este guion de ejemplo: «La junta informa que el domingo se limpiará la plaza de 9:00 a 11:00. Se pide traer guantes y bolsas. Quien tenga una carretilla, por favor avise a la secretaria». Anota las palabras clave, escribe una inferencia con su pista y una pregunta que harías.",
        "Notas: domingo, plaza, 9:00 a 11:00, guantes y bolsas, carretilla, secretaria. Inferencia: se necesita ayuda para mover tierra o basura (pista: la carretilla). Pregunta: ¿se entregan guantes si alguien no tiene?",
        ["anota las palabras clave", "escribe una inferencia con su pista", "formula una pregunta útil"],
        ["notas, una inferencia y una pregunta"],
        ["anotar frases enteras", "preguntar algo que el guion ya dijo"],
        "Pregunta: «¿Mis notas permiten recordar qué hacer sin volver a escuchar?»."),
    reinforce="Pide que te lean un aviso breve y anota qué, cuándo y dónde.",
    extend="Escribe un guion breve con cuatro datos y una pista para inferir algo; que otra persona lo lea y anote.",
)

build(
    O, 6, F6,
    use="Hoy evalúo lo que leo contra lo que sé: decido si una afirmación coincide con mi conocimiento y reviso cómo mejoré mi comprensión.",
    prior=["Sé inferir y tomar notas.", "Distingo datos de opiniones simples.", "Relaciono el texto con lo que ya sé."],
    explain=[
        "Leer también es evaluar. Evaluar lo que se lee significa preguntarse si lo que dice el texto calza con lo que ya sabes y con lo que otros textos dicen. No todo lo que está escrito es cierto o está bien razonado.",
        "Para evaluar, compara la afirmación con tu conocimiento. Si coincide, la información se vuelve más confiable. Si choca, no la rechaces de inmediato: busca una fuente confiable, como un aviso oficial o un texto de una institución, y revisa de nuevo. Tu experiencia es una buena guía, pero no la única.",
        "En el afiche de ejemplo, la frase A calza con algo que sabes: la luz prendida gasta electricidad. La frase B choca con eso, porque dice que dejar todo prendido baja la cuenta. Aquí tu conocimiento previo te permite evaluar el texto.",
    ],
    vocab=[("evaluar", "decidir si algo es acertado o confiable"), ("afirmación", "frase que dice que algo es de cierta manera"), ("fuente confiable", "origen de información que merece confianza, como una institución conocida"), ("electricidad", "energía que hace funcionar luces y aparatos")],
    worked=[
        ("Evaluar la frase A", F6, ["La frase A dice que apagar la luz de una pieza vacía gasta menos electricidad.", "Yo sé que una luz prendida consume electricidad mientras está prendida.", "Coinciden: la frase A es acertada."], "La frase A calza con lo que sé."),
        ("Evaluar la frase B", F6, ["La frase B dice que las cuentas bajan si todas las luces quedan prendidas todo el día.", "Yo sé que prender más luces durante más horas gasta más electricidad, no menos.", "Choca con lo que sé: lo mejor es comprobar en una fuente confiable antes de aceptarla."], "La frase B no coincide con lo que sé y requiere comprobación."),
    ],
    mistakes=[
        ("Aceptar todo lo que dice un afiche porque está impreso.", "Estar escrito no lo hace verdadero.", "Compara con lo que sabes y busca una fuente confiable si dudas."),
        ("Rechazar un texto solo porque trae una idea nueva.", "Una idea nueva puede ser correcta y enseñarte algo.", "Revisa en una fuente confiable antes de decidir."),
    ],
    T=[
        ("abc", "{F} ¿Qué dice la frase A?", "Apagar la luz de una pieza vacía gasta menos electricidad", "Dejar todas las luces prendidas baja la cuenta", "La electricidad se acaba en las piezas", "La frase A es la primera del afiche."),
        ("ab", "{F} ¿Qué dice la frase B?", "Que las cuentas bajan si se dejan todas las luces prendidas", "Que hay que apagar la luz de piezas vacías", "La frase B afirma justo lo contrario de A."),
        ("{F} ¿Cuántas frases tiene el afiche? (un número)", "2", "El afiche tiene la frase A y la frase B."),
        ("abc", "{F} ¿Qué conocimiento previo sirve para evaluar la frase A?", "Una luz prendida gasta electricidad mientras está prendida", "Las piezas son cuadradas", "La luz se compra en el almacén", "Ese conocimiento se compara con lo que dice la frase."),
        ("ab", "{F} ¿Con qué conocimiento choca la frase B?", "Con que más luces prendidas más horas gastan más", "Con que las cuentas llegan por correo", "Más consumo debería subir la cuenta, no bajarla."),
        ("abc", "{F} ¿Qué hace quien dice «La frase A calza con lo que sé»?", "Evalúa el texto con su conocimiento previo", "Cambia la frase", "Deja de leer", "Está comparando la información con lo que ya sabe."),
        ("ab", "{F} Si una persona duda de la frase B, ¿qué conviene hacer?", "Buscar una fuente confiable", "Aceptarla porque está en un afiche", "Una duda se resuelve revisando una fuente confiable."),
        ("abc", "{F} ¿Cuál de estas es una fuente confiable de ejemplo?", "Una guía de ahorro de energía de una institución conocida", "Un mensaje reenviado sin autor", "Un comentario sin nombre", "Se reconoce por tener un origen claro y responsable."),
        ("ab", "{F} ¿Es correcto concluir que el afiche completo es falso?", "No, solo la frase B choca con lo que sé", "Sí, porque tiene una frase equivocada", "La frase A calza; por eso se evalúa cada frase por separado."),
        ("abc", "Texto de ejemplo: «Los frutos secos conservados en un frasco bien tapado duran más que los dejados al aire». ¿Qué hace quien lo evalúa con su experiencia?", "Compara con lo que sabe sobre guardar alimentos", "Lo descarta sin leerlo", "Lo copia en un cuaderno", "Contrasta la afirmación con una experiencia conocida."),
        ("ab", "Texto de ejemplo: «El agua hierve a 50 grados». Una persona recuerda que el agua hierve a 100 grados al nivel del mar. ¿Qué concluye?", "Que la afirmación choca con lo que sabe y hay que revisarla", "Que el texto es perfecto", "Un dato muy distinto de lo conocido merece verificarse."),
        ("abc", "Un cartel de ejemplo dice: «Lavarse las manos con jabón ayuda a eliminar los gérmenes». ¿Con qué se puede relacionar?", "Con lo que se enseña de higiene en centros de salud", "Con la hora del día", "Con el color del cartel", "Es una idea conocida de higiene general."),
        ("ab", "Una persona lee: «Todos los trámites se hacen en un minuto». Piensa en las filas que ha visto. ¿Qué evalúa?", "Que la afirmación parece exagerada", "Que es una verdad segura", "Su experiencia con las filas le dice que no siempre es tan rápido."),
    ],
    ctx=("abc", "Una publicación de ejemplo en una sede dice: «Las plantas se riegan mejor al mediodía, con el sol más fuerte, para que absorban más agua». Quien la lee recuerda que regar bajo el sol fuerte hace que el agua se evapore rápido. ¿Qué conviene?", "Comprobar en una fuente confiable de jardinería antes de seguir el consejo", "Aceptar la publicación sin dudar", "Regar siempre de noche sin revisar nada", "Hay una duda: se evalúa con el conocimiento y se contrasta con una fuente."),
    sc=[("¿Qué es evaluar lo que leo?", "Decidir si calza con lo que sé y si es confiable", "Se compara el texto con el conocimiento y otras fuentes."),
        ("¿Qué hago si un texto choca con lo que sé?", "Busco una fuente confiable", "Mi experiencia sirve de alerta, pero la comprobación la completa."),
        ("¿Estar impreso lo hace verdadero?", "No", "Un texto puede estar equivocado aunque esté impreso.")],
    op=("Lee estas dos frases de ejemplo y evalúalas. Frase 1: «Si tapas la olla, el agua hierve más rápido». Frase 2: «Una persona que duerme poco rinde más que otra que duerme bien». Para cada una escribe: ¿calza con lo que sabes?, ¿por qué? y qué harías si dudas. Termina con una oración sobre cómo mejoró tu forma de leer en estas seis clases.",
        "Frase 1: calza con lo que sé: la tapa guarda el calor y el agua se calienta antes. Frase 2: choca con lo que sé, porque dormir poco cansa; buscaría una fuente confiable de salud. Mi lectura mejoró porque ahora pienso qué sé antes de aceptar un texto.",
        ["evalúa las dos frases", "explica con lo que sabe", "dice qué haría ante una duda", "escribe una oración final"],
        ["cuatro respuestas breves"],
        ["aceptar o rechazar sin razón", "no nombrar una fuente confiable"],
        "Pregunta: «¿Mi razón nombra un conocimiento concreto?»."),
    reinforce="Lee un consejo breve y escribe si calza con lo que sabes y cómo lo comprobarías.",
    extend="Escribe una afirmación verdadera y una falsa sobre un tema que conozcas; que otra persona las evalúe.",
)
