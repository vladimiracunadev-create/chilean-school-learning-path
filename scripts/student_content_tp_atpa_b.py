"""Atención de Párvulos TP 3.º y 4.º medio: OAE-03 (comunicarse en forma efectiva y afectiva con niños, niñas y familias), OAE-04 (alimentar a menores de seis años) y OAE-05 (mudar, apoyar a vestirse y desvestirse resguardando salud, seguridad, higiene y ergonomía). Todo en papel: jardines, niños, niñas y familias inventados y rotulados «de ejemplo»."""
from __future__ import annotations

from tp_atpa_common import LIM, build

O3 = "TP-ATPA-3y4-OAE-03"
O4 = "TP-ATPA-3y4-OAE-04"
O5 = "TP-ATPA-3y4-OAE-05"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (comunicación, de ejemplo). Con los niños y niñas: agacharse a su altura, mirarlos, hablar con voz calmada y frases cortas, y reconocer lo que sienten («veo que estás enojado»). "
     "Con las familias: saludo al llegar y al retirarse, libreta de comunicaciones y reuniones o entrevistas conducidas por la educadora. Regla del jardín de ejemplo: los temas delicados sobre un niño (salud, conducta o situación familiar) los conversa la educadora en un lugar privado.")
build(
    O3, 1, F,
    use="Aprenderé qué es comunicarse de forma efectiva y afectiva con niños, niñas y familias, qué es el buen trato y qué derechos de la infancia se cuidan al hacerlo.",
    prior=["Conozco el rol de la técnica y de la educadora.", "Sé que cada niño tiene su ritmo.", "Sé sumar y restar."],
    explain=[
        "En Atención de Párvulos, comunicarse de forma efectiva es lograr que el mensaje se entienda, y de forma afectiva es hacerlo con calidez y respeto. Con los niños se usan frases cortas y claras, se les mira a los ojos, se les habla desde su altura y se reconoce lo que sienten, aunque no se pueda hacer lo que piden. Así se crean ambientes cordiales y se cuida el bienestar de cada uno.",
        "El buen trato es tratar a niños y niñas con respeto, ternura y límites claros, sin gritos, burlas, comparaciones ni castigos humillantes. La Convención sobre los Derechos del Niño reconoce, entre otros, el derecho a ser escuchado, a jugar y a ser cuidado y protegido. Con las familias se mantiene un diálogo cordial: se saluda cada día, se usan mensajes breves y claros, y los temas delicados los conversa la educadora en privado.",
        "La comunicación puede ser individual (con un niño o una familia) o colectiva (con todo el grupo). Las familias son distintas entre sí, y la técnica las trata a todas con el mismo respeto." + LIM,
    ],
    vocab=[("comunicación efectiva", "lograr que el mensaje se entienda"), ("comunicación afectiva", "comunicarse con calidez y respeto"), ("buen trato", "trato respetuoso, tierno y con límites claros, sin gritos ni humillaciones"), ("derecho del niño", "algo que todo niño o niña merece, como ser escuchado, jugar y ser protegido"), ("validar una emoción", "reconocer lo que el niño siente sin burlarse ni negarlo"), ("comunicación colectiva", "la que se dirige a todo el grupo")],
    worked=[
        ("Validar una emoción", "Un niño de ejemplo llora porque se terminó el tiempo de juego. ¿Qué frase valida su emoción?", ["Validar es reconocer lo que siente.", "Se puede decir «veo que estás triste porque se terminó el juego»."], "«Veo que estás triste porque se terminó el juego»"),
        ("Quién conversa un tema delicado", "Una madre de ejemplo pregunta a la técnica, frente a otras familias, por qué su hija mordió a un compañero. ¿Qué corresponde?", ["Es un tema de conducta, delicado.", "Lo conversa la educadora en privado; la técnica ofrece avisarle para coordinar."], "Derivar a la educadora para conversarlo en privado"),
    ],
    mistakes=[("Decir «no llores, no pasó nada» a un niño que llora.", "Niega lo que siente y le enseña a ocultar sus emociones.", "Reconoce lo que siente y acompáñalo con calma."),
              ("Comentar frente a otras familias que un niño «anda agresivo».", "Expone al niño y a su familia y la conversación no es privada.", "Deriva la conversación a la educadora, en un lugar reservado.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es comunicarse de forma afectiva con un niño?", "Hacerlo con calidez y respeto", "Hablarle muy rápido para que no se aburra", "Darle siempre lo que pide", "Lo afectivo es el trato cálido y respetuoso, no la rapidez ni ceder siempre."),
        ("abc", "{F} ¿Por qué se recomienda agacharse a la altura del niño al hablarle?", "Para mirarlo a los ojos y que se sienta escuchado", "Para terminar más rápido la conversación", "Para que el niño no se distraiga con otros niños", "Estar a su altura facilita el contacto visual y muestra interés."),
        ("abc", "{F} ¿Quién conversa los temas delicados sobre un niño con su familia?", "La educadora, en un lugar privado", "La técnica, a la salida y delante de todos", "Cualquier adulta del jardín que lo vea primero", "La regla del jardín asigna esa conversación a la educadora en privado."),
        ("abc", "Un niño llora porque otro le quitó un juguete. ¿Qué frase valida su emoción?", "«Veo que estás enojado porque te quitaron el juguete»", "«No llores, no pasó nada»", "«Si sigues así, no juegas más»", "Validar es reconocer la emoción; negarla o amenazar no ayuda."),
        ("abc", "¿Cuál de estas es una muestra de buen trato?", "Poner un límite con voz calmada y explicar la razón", "Burlarse del niño para que no lo repita", "Comparar al niño con su hermano", "El buen trato pone límites sin humillar ni comparar."),
        ("abc", "Una técnica dice frente al grupo: «Miren cómo Noa sí se sentó, no como Tomás». ¿Qué falla?", "Compara a los niños y expone a Tomás", "Nada, es una forma de motivar", "Que no mencionó a un tercer niño", "Comparar y exponer a un niño no es buen trato."),
        ("=", "{F} Entre las 8:00 y las 8:30 llegan 12 familias y la técnica dedica 2 minutos a saludar a cada una. ¿Cuántos minutos quedan del período?", "30-12*2", "Se restan los minutos de saludo a la media hora de llegada.", " minutos"),
        ("abc", "{F} Un padre pregunta en la puerta, con otras familias cerca, por qué su hijo «anda agresivo». ¿Qué responde la técnica?", "Que la educadora podrá conversarlo con él en privado y que le avisará para coordinar", "Le cuenta lo que vio, para que lo sepa pronto", "Le dice que es un niño difícil", "Los temas delicados los conversa la educadora en privado, no la técnica en público."),
        ("abc", "¿Qué nota de ejemplo en la libreta de comunicaciones está bien escrita?", "«Hoy Mateo comió su almuerzo y jugó con bloques»", "«Mateo se portó mal»", "«Mateo es tímido»", "La nota describe hechos; las otras frases son juicios sobre el niño."),
        ("abc", "{F} Una niña llora y pregunta si su familia vendrá. ¿Qué hace la técnica?", "Reconoce su emoción, le dice que su familia viene a buscarla al final de la jornada y la acompaña", "Le dice que deje de llorar porque ya es grande", "Le promete que vendrá en cinco minutos", "Se valida, se informa lo que se sabe y se acompaña; no se hacen promesas falsas."),
        ("abc", "Un niño no quiere dar un abrazo a un visitante del jardín. ¿Qué respeta la técnica?", "Su decisión, y le ofrece saludar con la mano si lo desea", "Que lo abrace igual, por cortesía", "Que pida disculpas por no abrazar", "El niño tiene derecho a decidir sobre su cuerpo; se ofrecen otras formas de saludar."),
        ("=", "{F} A una reunión de ejemplo con 18 familias asisten 13. ¿A cuántas familias se les envía un resumen por la libreta?", "18-13", "Se restan las familias presentes del total del grupo.", " familias"),
        ("abc", "Para avisar a todo el grupo que mañana habrá salida al patio con ropa abrigada, ¿qué comunicación corresponde?", "Un aviso breve y claro en la libreta o el panel, dirigido a todas las familias", "Decírselo solo a la familia que pregunta", "No avisar y confiar en que lo sepan", "Un aviso colectivo asegura que todas las familias reciban el mismo mensaje."),
    ],
    ctx=("abc", "{F} A la salida, una abuela llega apurada y pregunta si su nieto «se portó bien». Otras familias esperan. ¿Qué responde la técnica?", "Le cuenta un hecho positivo del día y ofrece que la educadora la contacte si desea conversar más", "Le dice que no puede decirle nada", "Le cuenta delante de todos los problemas del día", "Se comunica con calidez y con hechos, y los temas delicados quedan para la educadora."),
    sc=[
        ("En Atención de Párvulos: ¿qué es validar una emoción?", "Reconocer lo que el niño siente sin negarlo", "Así el niño aprende a nombrar sus emociones."),
        ("¿Quién conversa en privado los temas delicados con una familia?", "La educadora", "Es la regla del jardín para cuidar al niño y a su familia."),
        ("¿Qué derecho se cuida al dejar que un niño decida si abraza o no?", "El derecho a ser escuchado y a decidir sobre su cuerpo", "El niño aprende que sus decisiones sobre su cuerpo importan."),
    ],
    op=("Caso de ejemplo. Una niña, Lía, de 3 años, se niega a lavarse las manos antes de comer y dice «¡no!» muy fuerte. Otro adulto grita «¡siempre igual contigo!». La madre de Lía pregunta a la técnica a la salida: «¿Se portó mal?». "
        "Escribe: una frase de buen trato para Lía; qué falla en el grito del adulto; qué responderías a la madre; y qué le contarías a la educadora.",
        "A Lía: «Veo que no quieres lavarte; vamos juntas y después comemos». El grito falla porque humilla y compara con otras veces; no es buen trato. A la madre: «Hoy lavarse las manos fue difícil, pero lo hicimos con calma; la educadora puede conversar con usted si quiere». A la educadora le contaría el hecho: Lía dijo que no, se le habló con calma y se lavó.",
        ["usa una frase que valida y propone", "identifica el trato inadecuado", "responde a la madre con hechos y deriva a la educadora"],
        ["hoja con tres frases y un breve aviso"],
        ["etiquetar a la niña", "responder a la madre con un juicio", "no avisar a la educadora"],
        "Pregunta: «¿Qué cambia si Lía llora?». Debe validar la emoción y acompañarla, sin amenazar."),
    reinforce="Escribe tres frases de buen trato que podrías decir a un niño que no quiere guardar los juguetes.",
    extend="Explica con un ejemplo por qué el buen trato ayuda a que un niño o niña se sienta seguro.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (documentos de comunicación, de ejemplo). Libreta de comunicaciones: mensajes breves entre el jardín y la casa. Panel informativo: avisos para todas las familias. "
     "Entrevista: conversación privada conducida por la educadora, con acuerdos anotados. Aviso de ejemplo: «El martes hay salida al patio grande a las 10:00; los niños deben venir con polerón y zapatillas cómodas».")
build(
    O3, 2, F,
    use="Aprenderé los documentos de comunicación con las familias, cómo se escribe un aviso claro y cómo se escucha a niños y adultos con respeto.",
    prior=["Conozco el buen trato y la validación de emociones.", "Sé escribir una nota breve.", "Sé leer una ficha."],
    explain=[
        "La comunicación con las familias se apoya en documentos: la libreta de comunicaciones, para mensajes breves entre el jardín y la casa; el panel informativo, para avisos dirigidos a todas las familias; y las entrevistas, conversaciones privadas conducidas por la educadora donde se anotan los acuerdos. La técnica ayuda a que los avisos lleguen a todos, sin conversar los temas delicados.",
        "Un aviso claro responde tres preguntas: qué ocurrirá, cuándo (día y hora) y qué se necesita (por ejemplo, qué traer). Se escribe con frases cortas y sin palabras técnicas. Si una familia tiene dificultad para leer o habla otro idioma, se consulta a la educadora por otra forma de comunicar, como conversar en persona o usar dibujos.",
        "La comunicación verbal usa palabras y la no verbal usa gestos, mirada y postura. Con los niños, ambas deben decir lo mismo: una sonrisa con un tono molesto confunde. La escucha activa es atender sin interrumpir y mostrar que se entiende." + LIM,
    ],
    vocab=[("libreta de comunicaciones", "cuaderno de mensajes breves entre el jardín y la familia"), ("panel informativo", "lugar visible con avisos para todas las familias"), ("entrevista", "conversación privada con una familia, conducida por la educadora"), ("acuerdo", "compromiso que se anota después de conversar"), ("comunicación no verbal", "mensaje que se da con gestos, mirada y postura"), ("escucha activa", "atender sin interrumpir y mostrar que se entiende")],
    worked=[
        ("Elegir el documento", "El jardín de ejemplo quiere avisar a todas las familias que el viernes no habrá clases. ¿Qué documento usa?", ["Es un aviso para todas las familias.", "Sirve el panel informativo y la libreta."], "El panel informativo y la libreta"),
        ("Revisar un aviso", "Un aviso de ejemplo dice: «Mañana habrá una actividad especial». ¿Qué le falta?", ["Un aviso debe decir qué, cuándo y qué se necesita.", "Falta la hora y qué traer."], "La hora y lo que deben traer"),
    ],
    mistakes=[("Escribir en el panel el nombre de un niño que no entregó un documento.", "Expone a la familia y el panel lo ven todos.", "Avisa en la libreta, de forma privada."),
              ("Decir «tranquila, no pasa nada» con el ceño fruncido y los brazos cruzados.", "El gesto dice lo contrario de las palabras y confunde.", "Cuida que las palabras y los gestos digan lo mismo.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿para qué sirve la libreta de comunicaciones?", "Para mensajes breves entre el jardín y la casa", "Para registrar el peso de los niños", "Para anotar el menú de la semana de todos los jardines", "Es un cuaderno de comunicación breve; otros registros tienen otros fines."),
        ("abc", "{F} ¿Quién conduce las entrevistas con las familias?", "La educadora", "La técnica", "Una persona de la familia", "Según la ficha, la educadora conduce las entrevistas y anota los acuerdos."),
        ("abc", "{F} ¿Qué datos entrega el aviso de ejemplo?", "Qué ocurrirá, cuándo y qué traer", "Quién cuidará a los niños", "Cuánto costará la salida", "El aviso dice la salida, el día y la hora y qué traer."),
        ("abc", "¿Qué documento sirve para informar a todas las familias la fecha de una reunión?", "El panel informativo", "La entrevista", "El registro de un solo niño", "El panel llega a todas las familias; la entrevista es privada."),
        ("abc", "Un aviso dice: «Se pide traer una muda de ropa». ¿Qué le falta?", "Qué ocurrirá y cuándo (día y hora)", "El nombre de cada niño", "Una opinión de la técnica", "Un aviso claro dice qué ocurrirá, cuándo y qué se necesita."),
        ("abc", "Una técnica sonríe y dice «bien» con los brazos cruzados y la mirada en otro lado. ¿Qué ocurre con el mensaje?", "Las palabras dicen una cosa y los gestos otra, y confunde", "Se entiende perfecto", "Es un mensaje solo verbal", "El mensaje no verbal contradice al verbal."),
        ("=", "{F} Un aviso del panel se lee en 30 segundos. Si 15 familias lo leen una por una, ¿cuántos segundos suman en total?", "30*15", "Se multiplican los segundos de cada lectura por el número de familias.", " segundos"),
        ("abc", "{F} ¿Qué falla en este aviso: «Mañana salida; traer ropa»?", "No indica la hora ni qué ropa traer", "Que usa frases cortas", "Que está escrito en el panel", "Un aviso útil necesita hora y detalle de lo que se debe traer."),
        ("abc", "{F} Una madre no lee bien y pide que se lo expliquen. ¿Qué hace la técnica?", "Le explica con calma y consulta a la educadora por otras formas de avisarle", "Le dice que busque a alguien que se lo lea", "Le pasa el papel y se va", "Se respeta a la familia y se consultan alternativas."),
        ("abc", "Un niño dice «mi mamá no vendrá a buscarme» y la técnica contesta «ya pues» mirando el teléfono. ¿Qué falla?", "No escucha con atención ni mira al niño", "Nada, porque respondió", "Que debió gritar", "La escucha activa exige atención y mostrar que se entiende."),
        ("=", "{F} Para que las 20 familias reciban el aviso en la libreta, hay que escribir una copia por familia. Si ya se escribieron 14, ¿cuántas faltan?", "20-14", "Se restan las copias hechas al total necesario.", " copias"),
        ("abc", "{F} Una familia pide en el pasillo detalles de la salud de su hija a la técnica. ¿Qué responde?", "Que la educadora puede conversarlo en una entrevista privada", "Le cuenta lo que sabe delante de todos", "Le dice que no se preocupe, sin más", "Los temas de salud se conversan en privado con la educadora."),
        ("abc", "{F} ¿Qué mensaje no verbal ayuda a que un niño se sienta bienvenido por la mañana?", "Sonreír, agacharse a su altura y saludarlo por su nombre", "Mirar el reloj mientras llega", "Decirle que no llore antes de saludarlo", "El saludo cálido muestra acogida; los gestos apurados o la orden no."),
    ],
    ctx=("abc", "{F} La técnica debe avisar a las familias que mañana el jardín abrirá a las 9:00 en lugar de las 8:00 por una reunión interna. ¿Qué aviso corresponde?", "«Mañana el jardín abre a las 9:00; los niños llegan desde esa hora», en el panel y la libreta", "«Mañana abre más tarde»", "Un llamado solo a las familias que preguntaron", "El aviso claro dice el día, la hora y a quién llega por más de un medio."),
    sc=[
        ("En Atención de Párvulos: ¿qué debe decir un aviso claro?", "Qué ocurrirá, cuándo y qué se necesita", "Así la familia puede prepararse con anticipación para la actividad."),
        ("¿Para qué sirve el panel informativo?", "Para avisos dirigidos a todas las familias", "Todas las familias pueden verlo cuando llegan o se retiran."),
        ("¿Qué hace la técnica con un tema delicado que plantea una familia?", "Deriva a la educadora para una entrevista privada", "Los temas delicados se conversan en privado con la educadora."),
    ],
    op=("Información de ejemplo: el jardín celebrará el viernes a las 11:00 una muestra de juegos para las familias; deben venir con ropa cómoda y avisar si no pueden asistir. "
        "Escribe: un aviso para el panel con qué, cuándo y qué se necesita; una nota breve para la libreta de una familia que no lee bien; y una frase que usarías al recibir a un niño por la mañana, con el gesto que la acompaña.",
        "Panel: «El viernes a las 11:00 hay una muestra de juegos para las familias. Vengan con ropa cómoda y avisen si no pueden asistir». Libreta: «Viernes 11:00, muestra de juegos; venir con ropa cómoda; puedo explicarle en persona». Saludo: «Buenos días, Lía» sonriendo y agachada a su altura.",
        ["el aviso incluye qué, cuándo y qué se necesita", "la nota adapta la comunicación a la familia", "la frase y el gesto dicen lo mismo"],
        ["hoja con aviso, nota y saludo"],
        ["dejar fuera la hora", "usar palabras técnicas", "gesto que contradice la frase"],
        "Pregunta: «¿Qué cambiarías para una familia que habla otro idioma?». Debe proponer consultar a la educadora y usar apoyos como dibujos."),
    reinforce="Escribe un aviso para el panel sobre una reunión de familias e indica qué, cuándo y qué se necesita.",
    extend="Explica por qué los gestos y las palabras deben decir lo mismo al hablar con un niño.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (caso de ejemplo). Mariana, de 2 años (nombre ficticio), llora al llegar al jardín; su papá se queda en la puerta preocupado. Rutina de ejemplo del jardín: despedida corta y con palabras, permitir un objeto querido de la casa y ofrecer un juego. "
     "Registro de la técnica: 8:05 llora; 8:10 se despide con la mano; 8:15 juega con bloques; 8:40 pide agua. En la tarde el papá pregunta: «¿Lloró mucho?».")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso de separación en la llegada y a responder a una familia con hechos, calidez y sin promesas ni juicios.",
    prior=["Sé validar una emoción.", "Sé qué se avisa a la educadora.", "Sé calcular minutos."],
    explain=[
        "Cuando los niños pequeños llegan al jardín, algunos lloran al separarse de su familia. Esto es parte de la adaptación, el período en que se acostumbran al jardín. No es una conducta mala. La técnica ayuda con una despedida corta y cálida, con palabras claras, permitiendo un objeto querido de la casa y ofreciendo un juego, siguiendo la rutina que la educadora indica.",
        "Para analizar el caso se leen los hechos del registro: a qué hora lloró, cuándo se calmó y qué hizo después. Con eso se responde a la familia con información real: «llegó llorando, se despidió con la mano y después se interesó en un juego». No se promete lo que no se sabe ni se culpa a la familia. Si la familia está angustiada, la técnica la escucha con calma y le ofrece que la educadora converse con ella.",
        "En todo caso se cuida la privacidad: nada se comenta sobre otros niños ni sobre la familia con personas ajenas." + LIM,
    ],
    vocab=[("adaptación", "período en que un niño se acostumbra al jardín"), ("despedida corta", "saludo breve y claro al separarse, sin alargar ni escaparse"), ("objeto querido", "objeto de la casa que acompaña al niño, como un peluche"), ("hecho", "lo que realmente ocurrió y se anotó"), ("promesa falsa", "decir algo que no se sabe si se cumplirá")],
    worked=[
        ("Responder con hechos", "Según un registro de ejemplo, un niño lloró desde las 8:00 hasta las 8:08 y luego jugó. ¿Qué se informa a su familia?", ["Se usan los hechos del registro.", "Lloró unos 8 minutos y luego jugó."], "Que lloró unos 8 minutos y luego jugó"),
        ("Evitar una promesa falsa", "Una madre de ejemplo pregunta: «¿Mañana ya no llorará?». ¿Qué respuesta es adecuada?", ["No se sabe qué ocurrirá mañana.", "Se puede decir que cada niño tiene su ritmo y que seguirán acompañándolo."], "Cada niño tiene su ritmo y seguiremos acompañándolo"),
    ],
    mistakes=[("Decirle a la familia «mañana ya no llorará, seguro».", "Es una promesa que no se puede cumplir y puede generar desconfianza.", "Informa los hechos y comenta que seguirán acompañando."),
              ("Decirle al padre «usted la malcría por quedarse en la puerta».", "Culpa a la familia sin conocerla y deteriora la relación.", "Explica con respeto la despedida corta del jardín.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es la adaptación al jardín?", "El período en que un niño se acostumbra al jardín", "El examen de ingreso al jardín", "La suspensión de las clases", "La adaptación es el proceso de acostumbrarse, no un examen ni una suspensión."),
        ("abc", "{F} ¿A qué hora empezó Mariana a jugar con bloques?", "A las 8:15", "A las 8:05", "A las 8:40", "El registro muestra el juego con bloques a las 8:15; 8:05 es el llanto y 8:40 el pedido de agua."),
        ("=", "{F} ¿Cuántos minutos pasaron entre que Mariana lloró y que empezó a jugar?", "(8*60+15)-(8*60+5)", "Se restan las horas del llanto y del juego, en minutos.", " minutos"),
        ("abc", "{F} Según la rutina del jardín, ¿cómo debe ser la despedida?", "Corta y con palabras claras, ofreciendo un objeto querido y un juego", "Larga, hasta que la niña deje de llorar", "A escondidas, sin que la niña lo note", "La ficha pide una despedida corta, con palabras y apoyo."),
        ("abc", "{F} ¿Qué responde la técnica al papá que pregunta si lloró mucho?", "«Lloró unos 10 minutos, se despidió con la mano y luego jugó»", "«No lloró nada»", "«Lloró todo el día»", "Se informan los hechos del registro, sin exagerar ni ocultar."),
        ("abc", "{F} El papá dice «mañana sufrirá igual». ¿Qué responde?", "Que cada niño tiene su ritmo y que seguirán acompañándola", "Que mañana no llorará, seguro", "Que él es el culpable", "No se prometen cosas que no se saben ni se culpa a la familia."),
        ("abc", "{F} Una compañera dice: «A Mariana la malcrían en su casa». ¿Qué observación corresponde?", "Es un juicio sin respaldo; solo se describen los hechos", "Es verdad: se nota por el llanto", "Debe decírselo al papá", "Un juicio sobre la familia no se basa en hechos y no ayuda a la niña."),
        ("=", "{F} Si cada día de adaptación la niña llora 3 minutos menos que el anterior, y el primer día lloró 10 minutos, ¿cuántos minutos llorará al tercer día?", "10-3-3", "Se resta dos veces la disminución diaria al llanto del primer día.", " minutos"),
        ("abc", "{F} El papá se queda en la puerta y la niña llora más. ¿Qué hace la técnica?", "Le explica con respeto que una despedida corta ayuda y lo invita a despedirse", "Le pide que se vaya enseguida sin explicar", "Le dice que es culpa suya", "Se explica el sentido de la rutina y se acompaña a la familia."),
        ("abc", "{F} Una vecina del jardín pregunta a la técnica si «esa niña que lloraba» siempre llora. ¿Qué responde?", "Que no puede comentar nada sobre los niños del jardín", "Que sí, que llora todos los días", "Que depende de lo que diga su papá", "Los datos de un niño no se comentan con personas ajenas."),
        ("abc", "{F} La técnica anota en el registro: «Mariana llora porque su papá es sobreprotector». ¿Qué falla?", "Atribuye una causa que no observó; debe anotar solo hechos", "Nada, explica el caso", "Que usó el nombre de la niña", "El registro no incluye interpretaciones sobre la familia."),
        ("=", "{F} El día siguiente, la niña llora 4 minutos menos que el día del caso. ¿Cuántos minutos lloró, si el día del caso fueron 10 minutos?", "10-4", "Se resta la disminución a los minutos del día del caso.", " minutos"),
        ("abc", "{F} Una semana después, la niña llega sonriendo, pero un día llora. ¿Cómo lo interpreta la técnica?", "Como parte del ritmo de adaptación y lo informa a la educadora con hechos", "Como un retroceso grave", "Como señal de un problema en la casa", "Los altibajos pueden ocurrir en la adaptación; se informan los hechos sin conclusiones."),
    ],
    ctx=("abc", "{F} A las 16:00 el papá llega angustiado y exige que le muestren «todo lo que anotaron sobre su hija». ¿Qué hace la técnica?", "Lo escucha con calma, le cuenta los hechos del día y ofrece que la educadora converse con él", "Le entrega el cuaderno de registros de todos los niños", "Le dice que se vaya", "Se escucha, se informa con hechos y se deriva; el cuaderno tiene datos de otros niños."),
    sc=[
        ("En Atención de Párvulos: ¿qué hace una despedida corta?", "Ayuda a que el niño se separe con calma", "Alargarla suele aumentar la angustia del niño y de la familia."),
        ("¿Qué informas a la familia sobre el llanto?", "Los hechos: cuánto duró y qué ocurrió después", "Con hechos se da confianza sin exagerar."),
        ("¿Prometes a la familia que el niño no llorará mañana?", "No", "Es una promesa que no se puede cumplir."),
    ],
    op=("Caso de ejemplo. Un niño de ejemplo, Tomás, de 3 años, llega con un peluche y llora desde las 8:00 hasta las 8:12; luego juega con una caja de bloques y a las 8:30 pide agua. A la salida, su madre pregunta: «¿Qué pasó hoy?». "
        "Escribe: el registro de hechos de la mañana; la respuesta a la madre con hechos; y una frase para la educadora sobre qué ofrecerías para mañana.",
        "Registro: 8:00 llora al llegar con su peluche; 8:12 deja de llorar; 8:30 pide agua. Madre: «Lloró unos 12 minutos, después jugó con bloques y pidió agua». Educadora: «Podemos mantener la despedida corta y que Tomás conserve su peluche; ¿lo coordinamos con su madre?».",
        ["registra hechos con horas", "responde a la madre sin promesas ni juicios", "deriva a la educadora la coordinación"],
        ["hoja con registro, respuesta y mensaje"],
        ["agregar juicios", "prometer que no llorará", "no avisar a la educadora"],
        "Pregunta: «¿Qué pasaría si la madre llorara?». Debe escucharla con calma y ofrecer que la educadora converse con ella."),
    reinforce="Escribe dos frases de despedida corta y cálida para un niño que llora al llegar.",
    extend="Explica por qué informar con hechos da más confianza a una familia que dar una promesa.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (agenda de entrevistas, de ejemplo). La educadora conduce entrevistas de 16:00 a 18:00; cada una dura 15 minutos y se dejan 5 minutos entre una y otra para anotar los acuerdos. "
     "Hay 20 familias en el grupo y 3 pidieron horario de mañana. Aviso por la libreta: debe decir día, hora y lugar. Para cada entrevista se prepara una hoja con los acuerdos anteriores de esa familia.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio con datos para organizar la comunicación con las familias: agendas, tiempos y avisos, y a mantener privacidad.",
    prior=["Conozco la libreta, el panel y la entrevista.", "Sé calcular horarios y dividir.", "Sé que los temas delicados los conversa la educadora."],
    explain=[
        "Organizar la comunicación con las familias es calcular tiempos y avisar con claridad. La educadora conduce las entrevistas y la técnica puede ayudar a preparar la agenda: cuántas caben en la tarde, a qué hora comienza cada una y cuántas jornadas se necesitan para ver a todas. Cada entrevista ocupa el tiempo de conversación más el tiempo entre una y otra para anotar los acuerdos.",
        "Para calcular cuántas entrevistas caben se divide el tiempo disponible por la duración de cada franja, incluyendo la pausa. Si las familias son más que las entrevistas posibles, se agregan jornadas. El aviso a cada familia indica día, hora y lugar, y llega por la libreta. Las hojas de acuerdos son confidenciales: se guardan en el archivo y no se dejan a la vista.",
        "Si una familia no puede asistir, se ofrece otra hora, sin reproches. La escucha de la familia es parte de la comunicación afectiva." + LIM,
    ],
    vocab=[("franja", "tiempo reservado para una entrevista, con su pausa"), ("agenda", "lista de horarios y familias citadas"), ("jornada", "tarde o mañana con entrevistas"), ("acuerdos anteriores", "compromisos anotados en entrevistas pasadas"), ("confidencial", "que no se muestra ni se comenta con personas ajenas")],
    worked=[
        ("Calcular la franja", "En otra agenda de ejemplo cada entrevista dura 10 minutos y se dejan 5 de pausa. ¿Cuánto dura cada franja?", ["Franja = entrevista + pausa.", "10 + 5 = 15."], "15 minutos"),
        ("Entrevistas por tarde", "Una tarde de ejemplo dura 90 minutos con franjas de 15. ¿Cuántas entrevistas caben?", ["Se divide el tiempo por la franja.", "90 ÷ 15 = 6."], "6 entrevistas"),
    ],
    mistakes=[("Programar entrevistas de 15 minutos sin dejar pausa y descubrir que la educadora se atrasa.", "Los acuerdos quedan sin anotar y todas las entrevistas se retrasan.", "Incluye la pausa en cada franja."),
              ("Dejar sobre el escritorio abierto la hoja de acuerdos de una familia.", "Otras personas podrían leer datos confidenciales.", "Guarda las hojas en el archivo y no las dejes a la vista.")],
    T=[
        ("=", "{F} ¿Cuántos minutos dura cada franja de entrevista?", "15+5", "Se suman la entrevista y la pausa para anotar los acuerdos.", " minutos"),
        ("=", "{F} ¿Cuántos minutos hay entre las 16:00 y las 18:00?", "(18*60)-(16*60)", "Se restan las horas, convertidas a minutos.", " minutos"),
        ("abc", "{F} ¿Quién conduce las entrevistas?", "La educadora", "La técnica", "El jardín completo", "Según la ficha, la educadora las conduce; la técnica ayuda con la agenda."),
        ("=", "{F} ¿Cuántas entrevistas caben en una tarde de 16:00 a 18:00?", "120//20", "Se divide el tiempo de la tarde por la duración de cada franja.", " entrevistas"),
        ("=", "{F} Si 3 familias piden horario de mañana, ¿cuántas familias se agendan en las tardes?", "20-3", "Al total de familias se le restan las que piden mañana.", " familias"),
        ("abc", "{F} ¿Qué debe decir el aviso de la libreta?", "Día, hora y lugar", "Solo el nombre de la familia", "Los temas que se conversarán", "Según la ficha, el aviso indica día, hora y lugar."),
        ("=", "{F} Con las 17 familias de la tarde y 6 entrevistas por tarde, ¿cuántas tardes se necesitan?", "(17+5)//6", "Se divide en tardes de 6 y se redondea hacia arriba, porque las familias sobrantes necesitan otra tarde.", " tardes"),
        ("=", "{F} La primera entrevista empieza a las 16:00. ¿A qué minutos después de las 16:00 empieza la cuarta?", "3*20", "Cada franja dura 20 minutos y antes de la cuarta pasaron tres.", " minutos"),
        ("abc", "{F} Una familia no puede asistir a su hora. ¿Qué hace la técnica?", "Ofrece otra hora disponible y lo anota en la agenda, sin reproches", "Le dice que perderá la oportunidad", "La borra de la agenda", "La flexibilidad y el respeto son parte de la comunicación afectiva."),
        ("abc", "{F} Una compañera deja sobre el escritorio la hoja de acuerdos de la familia anterior mientras llega la siguiente. ¿Qué observación corresponde?", "Las hojas son confidenciales y se guardan en el archivo", "Está bien, porque la familia anterior ya se fue", "Está bien si está dada vuelta", "Los acuerdos contienen datos de una familia y no deben quedar a la vista."),
        ("abc", "{F} Las 3 familias de la mañana avisan que no podrán ir en esa jornada. ¿Qué hace la técnica?", "Consulta a la educadora y agenda otra jornada para ellas", "Las agrega a las tardes sin avisar", "Las olvida porque el cupo ya está", "La agenda se ajusta con la educadora y se avisa a las familias."),
        ("=", "{F} Si cada entrevista se prepara con 2 hojas (acuerdos previos y registro), ¿cuántas hojas se necesitan para las 20 familias?", "20*2", "Se multiplican las hojas por entrevista por el número de familias.", " hojas"),
        ("abc", "{F} En la puerta, una familia comenta que otra «no vino porque no le interesa». ¿Qué corresponde?", "No opinar sobre otras familias y recordar que cada una tiene su situación", "Estar de acuerdo, para llevarse bien", "Contarle los motivos que conoce de esa familia", "No se hacen juicios ni se comentan situaciones de otras familias."),
    ],
    ctx=("abc", "{F} A la 17:00, una familia se retira de la entrevista molesta y la educadora aún escribe. Otra familia espera fuera. ¿Qué hace la técnica?", "Atiende a la familia que espera con amabilidad, avisa el pequeño retraso y no comenta lo ocurrido", "Cuenta a la familia que espera por qué se fue molesta la anterior", "Le pide a la familia que espera que se vaya", "Se cuida el trato con quienes esperan y se mantiene la privacidad de la entrevista anterior."),
    sc=[
        ("En Atención de Párvulos: ¿qué incluye cada franja de entrevista?", "La entrevista y la pausa para anotar acuerdos", "Sin la pausa, la agenda se atrasa."),
        ("¿Qué datos lleva el aviso de la libreta?", "Día, hora y lugar", "Así la familia puede organizarse para llegar a la hora."),
        ("¿Dónde se guardan las hojas de acuerdos?", "En el archivo, fuera de la vista", "Son datos confidenciales de la familia."),
    ],
    op=("Datos de ejemplo: la educadora conduce entrevistas el miércoles de 15:00 a 18:00; cada entrevista dura 20 minutos, con 10 minutos de pausa. Hay 14 familias del grupo. "
        "Escribe: la duración de cada franja; cuántas entrevistas caben en la tarde; cuántas tardes se necesitan; un aviso de libreta para una familia, con día, hora y lugar; y cómo guardarías las hojas de acuerdos.",
        "Franja: 20 + 10 = 30 minutos. Tarde: 180 minutos, caben 6. Tardes: 14 familias ÷ 6 = 2 tardes y sobran 2, se necesitan 3. Aviso: «Entrevista el miércoles a las 15:00 en la sala del nivel». Las hojas se guardan en el archivo, no a la vista.",
        ["calcula franja, entrevistas y tardes", "redondea hacia arriba las tardes", "redacta un aviso completo y propone guardar con reserva"],
        ["hoja con cálculos y aviso"],
        ["olvidar la pausa", "no redondear las tardes", "dejar el aviso sin hora"],
        "Pregunta: «¿qué cambiaría si cada entrevista durara 30 minutos?». Debe recalcular la franja y la cantidad por tarde."),
    reinforce="Calcula cuántas entrevistas de 10 minutos con 5 de pausa caben en 120 minutos.",
    extend="Explica por qué las hojas de acuerdos de cada familia no deben quedar a la vista de otras personas.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (rutina de alimentación, jardín de ejemplo). Horarios de ejemplo: desayuno a las 8:30, almuerzo a las 12:00 y colación a las 15:30. Antes de comer, todos se lavan las manos con jabón y se secan. "
     "Cada niño tiene una ficha de requerimientos escrita por la educadora con la información entregada por su familia o por un profesional de salud (por ejemplo, «no puede comer maní»). La técnica no cambia ni decide nada sobre esas indicaciones.")
build(
    O4, 1, F,
    use="Aprenderé el contexto de la alimentación de niños y niñas menores de seis años: horarios, higiene, autonomía, requerimientos y el aviso ante una emergencia.",
    prior=["Conozco el rol de la técnica y de la educadora.", "Sé leer horarios.", "Sé que los datos de los niños son confidenciales."],
    explain=[
        "En Atención de Párvulos, alimentar a niños y niñas es parte de su cuidado y su aprendizaje. Una alimentación saludable es variada, incluye frutas, verduras y agua, y se sirve en horarios regulares. Los horarios convenidos ordenan la jornada, y antes de comer todos se lavan las manos. El momento de comer es tranquilo: se come sentados y acompañados por un adulto que no se distrae.",
        "Cada niño tiene requerimientos dietéticos: indicaciones sobre lo que puede o no comer, que da la familia o un profesional de salud y que la educadora anota en una ficha. La técnica las cumple sin cambiarlas ni opinar sobre ellas. También se favorece la autonomía: dejar que el niño coma por sí mismo, con apoyo, según su edad. No se fuerza a comer ni se usa la comida como premio o castigo.",
        "Si un niño se atraganta o presenta una reacción tras comer, la técnica no actúa por su cuenta: no lo deja solo, pide ayuda de inmediato a la educadora o al adulto responsable y se avisa a emergencias. Practicar con niños exige supervisión de la educadora." + LIM,
    ],
    vocab=[("alimentación saludable", "variada, con frutas, verduras y agua, en horarios regulares"), ("requerimiento dietético", "indicación sobre lo que un niño puede o no comer"), ("ficha de requerimientos", "documento de la educadora con esas indicaciones"), ("autonomía", "hacer algo por sí mismo con el apoyo necesario"), ("colación", "comida pequeña entre el almuerzo y el final de la jornada"), ("horario convenido", "hora de comer acordada por el jardín")],
    worked=[
        ("Calcular una espera", "Con el desayuno a las 8:30 y el almuerzo a las 12:00, ¿cuántas horas y minutos pasan entre ambos?", ["De 8:30 a 12:00 hay 3 horas y 30 minutos.", "Son 210 minutos."], "3 horas y 30 minutos"),
        ("Respetar un requerimiento", "La ficha de un niño de ejemplo dice «no puede comer maní» y hoy hay galletas con maní. ¿Qué hace la técnica?", ["No decide por su cuenta.", "Avisa a la educadora y espera la indicación para entregar una alternativa."], "Avisar a la educadora y no darle la galleta"),
    ],
    mistakes=[("Decir «come un poquito más» y volver a servir cuando el niño ya dijo que no quiere.", "Forzar a comer quita autonomía y convierte la comida en un conflicto.", "Ofrece con calma y respeta cuando dice que no quiere más."),
              ("Usar el postre como premio por terminar el plato.", "Enseña que la comida es un premio o castigo en vez de algo para nutrirse.", "Sirve el postre como parte normal de la comida.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es una alimentación saludable?", "Variada, con frutas, verduras y agua, en horarios regulares", "Muy abundante, para que no tengan hambre", "Solo de alimentos que le gustan a cada niño", "Lo saludable es variado y regular, no solo abundante o a gusto."),
        ("abc", "{F} ¿Qué se hace antes de comer?", "Todos se lavan las manos con jabón y se secan", "Se limpian las manos solo si se ven sucias", "Se lavan solo al terminar de comer", "La ficha fija el lavado de manos antes de comer."),
        ("abc", "{F} ¿Quién escribe la ficha de requerimientos de cada niño?", "La educadora, con la información de la familia o de un profesional de salud", "La técnica, según lo que cree mejor", "El propio niño", "La educadora recoge y anota las indicaciones; la técnica las cumple."),
        ("=", "{F} ¿Cuántos minutos pasan entre el desayuno de las 8:30 y la colación de las 15:30?", "(15*60+30)-(8*60+30)", "Se restan las horas, convertidas a minutos.", " minutos"),
        ("abc", "{F} Un niño dice «ya no quiero más» sin haber terminado. ¿Qué hace la técnica?", "Respeta su decisión y registra cuánto comió", "Le pide que coma tres cucharadas más", "Le avisa que no hay postre si no termina", "Se favorece la autonomía y no se fuerza; el registro permite informar a la educadora."),
        ("abc", "¿Por qué el momento de comer debe ser tranquilo y supervisado?", "Para que los niños coman sentados con un adulto atento a ellos", "Para que terminen lo antes posible", "Para que el adulto pueda hacer otras tareas mientras comen", "Un ambiente tranquilo y atento previene riesgos y favorece una buena relación con la comida."),
        ("=", "{F} Si la colación dura 20 minutos y empieza a las 15:30, ¿a qué minuto después de las 15:00 termina?", "30+20", "Se suman los minutos de inicio y la duración.", " minutos"),
        ("abc", "{F} La ficha de una niña dice «no puede tomar leche» y la colación de hoy es un yogur. ¿Qué hace la técnica?", "Avisa a la educadora y espera su indicación antes de entregarle algo", "Le entrega el yogur pero solo la mitad", "Le entrega el yogur y observa si pasa algo", "No se cambia ni se interpreta una indicación; se avisa a la educadora."),
        ("abc", "Durante el almuerzo, un niño se pone rojo, tose y no puede respirar bien. ¿Qué hace la técnica?", "No lo deja solo, pide ayuda de inmediato a la educadora o adulto responsable y se avisa a emergencias", "Le da agua rápido", "Espera a ver si se le pasa", "Ante un atragantamiento se acompaña al niño, no se le deja solo y se avisa de inmediato a la educadora y a emergencias, sin improvisar."),
        ("abc", "Una técnica dice: «Si terminas todo, hoy te doy el postre». ¿Qué falla?", "Usa la comida como premio", "Nada: motiva a comer", "Que el postre es poco saludable", "Usar la comida como premio o castigo no favorece una buena relación con ella."),
        ("abc", "{F} Una familia pide por la puerta que su hijo «no coma pescado», pero no hay ficha. ¿Qué hace la técnica?", "Le dice que informe a la educadora, que registrará la indicación en la ficha", "Anota ella misma la restricción y la aplica", "La ignora porque no está escrito", "Las indicaciones deben pasar por la educadora, que las anota en la ficha."),
        ("=", "{F} En el almuerzo se sientan 18 niños en 3 mesas iguales. ¿Cuántos niños hay por mesa?", "18//3", "Se divide el total de niños entre las mesas.", " niños"),
        ("abc", "{F} Un niño de 4 años pide servirse la fruta él mismo con una cuchara grande. ¿Qué es lo más adecuado?", "Dejarlo hacerlo con apoyo, porque favorece su autonomía", "Servirle siempre para que no se ensucie", "Impedirlo porque se puede caer algo", "Con apoyo, servirse solo es una forma de autonomía."),
    ],
    ctx=("abc", "{F} Un niño de ejemplo recibe de otro compañero un pedazo de galleta con maní, pero su ficha dice que no puede comerlo. Aún no lo ha probado. ¿Qué hace la técnica?", "Retira la galleta con calma, avisa de inmediato a la educadora y observa al niño", "Le dice que se enjuague y sigue con el almuerzo", "Espera a ver si le pasa algo", "Se aparta el riesgo y se avisa enseguida; no se improvisa."),
    sc=[
        ("En Atención de Párvulos: ¿quién anota las indicaciones sobre lo que un niño puede comer?", "La educadora, en su ficha", "Así quedan registradas con la información de la familia."),
        ("¿Qué haces si un niño se atraganta?", "Aviso de inmediato a la educadora y a emergencias", "No se improvisa; se pide ayuda enseguida."),
        ("¿Usas el postre como premio?", "No", "La comida no debe ser premio ni castigo."),
    ],
    op=("Datos de ejemplo. Rutina de un jardín: desayuno 8:30, almuerzo 12:15 y colación 15:30. Ficha de la educadora: Noa no puede comer huevo; Tomás come sin carne por decisión de su familia. Hoy el almuerzo es «cazuela de verduras con arroz y una manzana». "
        "Escribe: las horas que separan el desayuno del almuerzo; qué haces antes de sentar a los niños a comer; qué le dirías a un niño que no quiere terminar; y qué harías si Noa se pone mal después de comer.",
        "Desayuno a almuerzo: 3 horas y 45 minutos (225 minutos). Antes de comer: lavado de manos con jabón y revisar las fichas. A un niño que no quiere terminar: «está bien, ¿quieres tomar agua?» y registrar cuánto comió. Si Noa se pone mal: no dejarla sola, avisar de inmediato a la educadora o adulto responsable y a emergencias; no actuar por mi cuenta.",
        ["calcula bien la espera entre comidas", "cumple las fichas sin cambiarlas", "ante un malestar avisa de inmediato a la educadora y a emergencias"],
        ["hoja con cálculo, tres acciones y un aviso"],
        ["forzar a comer", "decidir un cambio de dieta por cuenta propia", "intentar resolver el malestar sin avisar"],
        "Pregunta: «¿qué anotarías en el registro de ese día?». Debe anotar hechos: lo que comió y lo que ocurrió."),
    reinforce="Escribe tres reglas para el momento de comer en un jardín infantil.",
    extend="Explica por qué la técnica no cambia las indicaciones de la ficha de requerimientos aunque piense que son demasiado estrictas.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (minuta y fichas, de ejemplo). Grupos de alimentos: cereales y legumbres, verduras y frutas, lácteos, carnes y huevos, y agua. Minuta del lunes: lentejas con arroz, ensalada de zanahoria y una manzana. Minuta del martes: pollo con puré de papas, ensalada de tomate y yogur. "
     "Fichas de ejemplo: Lía, alergia al maní; Mateo, sin carne por decisión de la familia; Amaru, sin cerdo por motivos religiosos de la familia. Cada familia indica y la educadora anota.")
build(
    O4, 2, F,
    use="Aprenderé los conceptos básicos de la alimentación infantil: grupos de alimentos, minuta, requerimientos y alergias, y a leer una ficha sin interpretar.",
    prior=["Conozco la ficha de requerimientos.", "Sé leer una tabla en texto.", "Sé que la técnica no cambia las indicaciones."],
    explain=[
        "Los alimentos se agrupan según lo que aportan: cereales y legumbres, verduras y frutas, lácteos, carnes y huevos, y el agua, que se ofrece durante todo el día. La minuta es el plan de comidas del jardín, que dice qué se sirve cada día. La preparan las personas responsables del establecimiento. La técnica la conoce para saber qué se servirá y revisar que coincida con las fichas.",
        "Un requerimiento dietético puede deberse a una alergia (una reacción adversa del cuerpo a un alimento), a una indicación de un profesional de salud o a las creencias de una familia, como no comer carne o cerdo. En todos los casos se respeta lo que la ficha dice, sin hacer comentarios que hagan sentir distinto al niño. La técnica no diagnostica alergias ni da consejos de salud.",
        "Si algo en la minuta contradice una ficha, se avisa a la educadora antes de servir. La forma de preparar y servir los alimentos a cada edad, por ejemplo la textura o el tamaño de los trozos, la indica la educadora o la persona responsable del establecimiento, según la norma vigente." + LIM,
    ],
    vocab=[("minuta", "plan de comidas del jardín, día por día"), ("grupo de alimentos", "conjunto de alimentos que aportan algo parecido"), ("alergia", "reacción adversa del cuerpo a un alimento, indicada por la familia o un profesional de salud"), ("sin carne por decisión de la familia", "requerimiento por una elección familiar, no por salud"), ("textura", "qué tan blando o duro es un alimento al comerlo")],
    worked=[
        ("Ubicar un alimento", "¿A qué grupo pertenece el yogur de la minuta del martes?", ["El yogur se hace con leche.", "Pertenece al grupo de los lácteos."], "Lácteos"),
        ("Revisar la minuta con una ficha", "Un niño de ejemplo no come carne. La minuta dice «tallarines con salsa de verduras». ¿Hay conflicto?", ["La minuta no tiene carne.", "No hay conflicto, pero igual se revisa con la educadora."], "No hay conflicto"),
    ],
    mistakes=[("Decirle a Mateo frente al grupo: «tú no comes carne porque eres distinto».", "Lo hace sentir diferente y expone una decisión de su familia.", "Sirve su alternativa con naturalidad, sin comentarios."),
              ("Pensar que una alergia es lo mismo que «no le gusta».", "Una alergia puede causar una reacción grave; no es un gusto.", "Cumple siempre las fichas y avisa a la educadora ante cualquier duda.")],
    T=[
        ("abc", "{F} ¿A qué grupo de alimentos pertenece el yogur?", "Lácteos", "Cereales y legumbres", "Carnes y huevos", "El yogur se elabora con leche, por eso es un lácteo."),
        ("abc", "{F} ¿A qué grupo pertenecen las lentejas?", "Cereales y legumbres", "Verduras y frutas", "Lácteos", "Las lentejas son legumbres, que la ficha agrupa con los cereales."),
        ("abc", "En Atención de Párvulos: ¿qué es una minuta?", "El plan de comidas del jardín, día por día", "El registro de peso de los niños", "La lista de materiales de cocina", "La minuta dice qué se sirve cada día."),
        ("abc", "{F} ¿Qué indica la ficha de Lía?", "Que tiene alergia al maní", "Que no come carne por decisión de su familia", "Que no come cerdo", "Esos otros dos requerimientos corresponden a Mateo y a Amaru."),
        ("abc", "{F} El martes se sirve pollo con puré. ¿Qué ficha exige un reemplazo?", "La de Mateo, que no come carne", "La de Lía, que no puede comer maní", "Ninguna", "El pollo es carne; la ficha de Mateo pide otra preparación."),
        ("abc", "{F} La cocina avisa que las lentejas del lunes se cocinaron con trozos de cerdo. ¿Qué fichas exigen reemplazo?", "La de Mateo y la de Amaru", "Solo la de Amaru", "Solo la de Lía", "Mateo no come carne de ningún tipo y Amaru no come cerdo, así que ambos necesitan reemplazo."),
        ("=", "{F} En una semana de ejemplo la minuta se repite igual por 5 días y cada día hay 18 niños. ¿Cuántas raciones se sirven en total?", "5*18", "Se multiplican los días por los niños que reciben una ración.", " raciones"),
        ("=", "{F} Hoy hay 18 niños. 3 tienen fichas con requerimientos especiales. ¿Cuántos niños comen la minuta sin cambios?", "18-3", "Al total se le restan los niños con ficha especial.", " niños"),
        ("abc", "{F} Una compañera dice: «Lía exagera con el maní; un poquito no le hace nada». ¿Qué corresponde?", "Recordar que la ficha se cumple siempre, porque una alergia puede ser grave", "Dar la galleta con un poquito de maní", "Esperar a ver qué pasa", "Las alergias se respetan sin ponerlas a prueba."),
        ("abc", "{F} Un niño cuyo requerimiento no está en ninguna ficha dice: «mi abuela dice que me hace mal el pescado». ¿Qué hace la técnica?", "Avisa a la educadora para que consulte con la familia", "Le sirve igual el pescado", "Le sirve algo distinto por su cuenta", "Un posible requerimiento nuevo debe verificarse con la familia a través de la educadora."),
        ("=", "{F} Si de las 18 raciones, 4 son de reemplazo, ¿cuántas raciones se preparan con el plato de la minuta?", "18-4", "Se restan las raciones de reemplazo al total.", " raciones"),
        ("abc", "{F} ¿Cuándo se avisa a la educadora que la minuta contradice una ficha?", "Antes de servir la comida", "Después de que los niños comieron", "Solo si algún niño se queja", "La revisión se hace antes para evitar riesgos."),
        ("abc", "{F} Otro niño pregunta por qué Amaru no come cerdo. ¿Qué responde la técnica?", "Que cada familia decide qué come y que todos comemos cosas distintas", "Que Amaru tiene una enfermedad", "Que se lo pregunte a su familia en voz alta", "Se respeta a la familia con una explicación sencilla y sin exponer a Amaru."),
    ],
    ctx=("abc", "{F} Al preparar el almuerzo del martes, la técnica nota que el puré del día llegó con un envase que dice «puede contener maní en pequeñas cantidades». Lía está presente. ¿Qué hace?", "No lo sirve a Lía, avisa a la educadora y espera su indicación", "Se lo sirve, porque es muy poca cantidad", "Se lo sirve y observa cómo reacciona", "Ante un posible contacto con el alimento de la ficha, se avisa antes de servir; no se pone a prueba."),
    sc=[
        ("En Atención de Párvulos: ¿a qué grupo pertenece el arroz?", "A los cereales", "El arroz es un cereal, por eso va en ese grupo."),
        ("¿Qué haces si la minuta contradice una ficha?", "Aviso a la educadora antes de servir", "La revisión previa evita riesgos antes de que el niño coma."),
        ("¿Una alergia es lo mismo que un gusto?", "No", "La alergia puede ser grave y no es una preferencia."),
    ],
    op=("Datos de ejemplo. Minuta del jueves: tallarines con salsa de carne, ensalada de repollo y una pera. Fichas: Noa, alergia al maní; Tomás, sin carne por decisión de su familia; Camila, sin restricciones. 20 niños presentes, 2 de ellos con ficha de las anteriores. "
        "Escribe: a qué grupo pertenece cada alimento de la minuta; qué ficha genera un conflicto y qué harías; cuántos niños comen la minuta sin cambios; y qué dirías a un niño que pregunta por qué Tomás come distinto.",
        "Tallarines: cereales; salsa de carne: carnes; repollo: verduras; pera: frutas. El conflicto está en la ficha de Tomás (sin carne): avisaría a la educadora antes de servir. 20 − 2 = 18 niños comen la minuta sin cambios. Al niño: «Cada familia decide qué come; todos comemos cosas distintas».",
        ["clasifica los alimentos", "detecta el conflicto y avisa a la educadora antes de servir", "responde con respeto y sin exponer a Tomás"],
        ["hoja con grupos, conflicto, cuenta y frase para el niño"],
        ["servir la salsa a Tomás", "no avisar a la educadora", "hacer sentir distinto a Tomás"],
        "Pregunta: «¿Qué pasa con la ficha de Noa y el maní?». Debe ver que no hay conflicto aparente, pero igual se confirma con la educadora si alguna preparación lo contiene."),
    reinforce="Clasifica en grupos de alimentos diez alimentos de una minuta que inventes.",
    extend="Explica por qué respetar el requerimiento de un niño sin hacerlo notar es parte del buen trato.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (almuerzo de ejemplo). Minuta del día: cazuela de pollo con papas y zapallo, y de postre una galleta con maní y una manzana. 18 niños y niñas en 3 mesas de 6. "
     "Fichas: Lía, alergia al maní; Mateo, sin carne por decisión de su familia; ambos tienen reemplazo preparado y rotulado con su nombre en bandejas aparte. "
     "Hora de almuerzo: 12:00. Una técnica atiende cada mesa.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso de almuerzo: revisar minuta, fichas y reemplazos, evitar confusiones entre niños y avisar ante un riesgo.",
    prior=["Conozco grupos de alimentos y fichas de requerimientos.", "Sé que la alergia es un riesgo.", "Sé que ante una emergencia se avisa de inmediato."],
    explain=[
        "Para analizar un caso de alimentación se revisan tres cosas antes de servir: lo que dice la minuta del día, lo que dicen las fichas de cada niño y qué reemplazos preparó la cocina. Cada reemplazo va rotulado con el nombre del niño y se entrega solo a él. Se verifica la bandeja antes de ponerla frente al niño, y nadie sirve un plato sin comprobar a quién corresponde.",
        "En la mesa se previene que los niños intercambien comida: se sientan separados de su bandeja ajena y el adulto observa. Si un niño toma comida que no le corresponde, se retira con calma y se avisa a la educadora. Si hay señales de que una alergia está afectando a un niño, como tos fuerte, rostro rojo o dificultad para respirar, no se improvisa: no se le deja solo, se pide ayuda de inmediato a la educadora o al adulto responsable y se avisa a emergencias.",
        "Después de comer se registra cuánto comió cada niño y cualquier hecho importante, sin interpretar." + LIM,
    ],
    vocab=[("reemplazo", "plato distinto preparado para un niño por su ficha"), ("rotulado", "con una etiqueta con el nombre del niño"), ("verificar", "comprobar antes de entregar que el plato corresponde a ese niño"), ("señales de alerta", "hechos observables que indican que un niño puede estar mal"), ("registro de alimentación", "anotación de cuánto comió cada niño")],
    worked=[
        ("Verificar una bandeja", "Una bandeja rotulada «Mateo» llega a la mesa 2. ¿Quién la recibe?", ["El rótulo dice el nombre del niño.", "La recibe Mateo, tras comprobar que la ficha coincide."], "Mateo"),
        ("Registrar una comida", "En una mesa de 6 niños, 4 comieron todo y 2 la mitad. ¿Cuántos comieron todo y cuántos menos?", ["Comieron todo: 4.", "Comieron menos: 2."], "4 comieron todo y 2 menos"),
    ],
    mistakes=[("Poner la bandeja de reemplazo en cualquier lugar de la mesa para repartir más rápido.", "Puede entregarse a otro niño, con riesgo para quien tiene la alergia.", "Entrega cada bandeja rotulada directamente al niño correspondiente."),
              ("Retirar la galleta con maní a un niño con ficha sin avisar a nadie.", "La educadora no sabría que pudo ocurrir un intercambio.", "Retírala con calma y avisa de inmediato.")],
    T=[
        ("abc", "{F} ¿Qué reemplazos están preparados?", "Para Lía y para Mateo", "Solo para Mateo", "Para los 18 niños", "La ficha dice que ambos tienen reemplazo rotulado."),
        ("abc", "{F} ¿Qué postre no puede comer Lía?", "La galleta con maní", "La manzana", "Los dos postres", "La alergia de Lía es al maní, que lleva la galleta."),
        ("abc", "{F} ¿Por qué la bandeja de reemplazo lleva el nombre del niño?", "Para entregarla solo a ese niño y evitar confusiones", "Para que el niño aprenda a leer su nombre", "Para decorar la bandeja", "El rótulo evita entregar un plato a otro niño."),
        ("=", "{F} ¿Cuántos niños hay en total en las 3 mesas?", "3*6", "Se multiplican las mesas por los niños de cada una.", " niños"),
        ("abc", "{F} Antes de poner la bandeja frente al niño, ¿qué hace la técnica?", "Verifica que el nombre y la ficha coincidan", "Pide al niño que la revise", "La entrega sin mirar para ir más rápido", "Verificar es comprobar antes de entregar."),
        ("abc", "{F} Un niño de la mesa 1 toma de la mano de Lía su galleta con maní. ¿Qué hace la técnica?", "Retira la galleta con calma y avisa a la educadora", "Espera a ver si Lía la come", "Le dice a Lía que no vuelva a mirar", "Se retira el riesgo y se informa para actuar si hace falta."),
        ("=", "{F} En la mesa de Lía hay 6 niños. 1 recibe reemplazo. ¿Cuántos reciben el plato de la minuta?", "6-1", "Se resta el niño con reemplazo a los de la mesa.", " niños"),
        ("abc", "{F} Lía tose, se pone roja y le cuesta respirar después de comer. ¿Qué hace la técnica?", "No la deja sola, pide ayuda de inmediato a la educadora o adulto responsable y se avisa a emergencias", "Le da agua y espera", "Le dice que respire lento y sigue con la mesa", "Ante señales graves se acompaña a la niña, no se le deja sola y se avisa de inmediato, sin improvisar."),
        ("abc", "{F} Mateo no quiere comer su reemplazo y mira el plato de su vecino. ¿Qué hace la técnica?", "Le ofrece su plato con calma y registra lo ocurrido", "Le cambia el plato por el del vecino", "Le da un poco del plato de su vecino", "Se respeta su ficha y se acompaña sin ceder a pedir otra cosa que no corresponda."),
        ("abc", "{F} Una técnica reemplaza la bandeja de Lía por otra sin rótulo «porque se parecen». ¿Qué falla?", "No verifica quién corresponde ni respeta el rótulo", "Nada: son iguales", "Que cambió de mesa", "Sin rótulo no se puede comprobar el plato."),
        ("=", "{F} Hoy 11 niños comieron todo, 5 la mitad y 2 no quisieron. ¿Cuántos niños suman?", "11+5+2", "Se suman los tres grupos de registro.", " niños"),
        ("abc", "{F} La técnica anota «Mateo no come porque es mañoso». ¿Qué falla?", "Interpreta; debe anotar «Mateo no quiso comer su plato»", "Nada, es una anotación breve", "Que debió escribir el nombre completo", "El registro describe hechos y no etiqueta."),
        ("abc", "{F} Un niño dice que le duele la guatita después de comer. ¿Qué hace la técnica?", "Lo acompaña, no le da nada y avisa a la educadora", "Le da agua con azúcar", "Le dice que es por comer rápido", "No se da nada por cuenta propia; se avisa para que decida la educadora."),
    ],
    ctx=("abc", "{F} A las 12:20 la técnica nota que dos niños de una mesa se pasaron los platos mientras ella servía en otra. Uno de ellos es Lía. ¿Qué hace?", "Revisa con calma qué comió Lía, la acompaña y avisa de inmediato a la educadora", "Deja que sigan y registra al final", "Regaña a los dos niños", "Se verifica, se acompaña y se avisa enseguida; regañar no resuelve el riesgo."),
    sc=[
        ("En Atención de Párvulos: ¿qué se verifica antes de entregar una bandeja de reemplazo?", "Que el nombre y la ficha coincidan", "Así no se entrega al niño equivocado."),
        ("¿Qué haces si hay señales de reacción grave tras comer?", "Aviso de inmediato a la educadora y a emergencias", "No se improvisa ante una emergencia."),
        ("¿Cómo registras que un niño no comió?", "«No quiso comer su plato», sin etiqueta", "Los hechos no marcan al niño."),
    ],
    op=("Caso de ejemplo. Minuta: arroz con pollo y ensalada; postre: yogur. 12 niños en 2 mesas de 6. Fichas: Noa, postre sin lácteos según la indicación de su familia, con reemplazo rotulado; Amaru, sin pollo por decisión de su familia, con reemplazo rotulado. "
        "Escribe: qué verificarías antes de servir; qué harías si Noa toma el yogur de su vecino; cómo registrarías que Amaru comió la mitad; y qué avisarías a la educadora.",
        "Antes de servir verificaría minuta, fichas y rótulos de las dos bandejas. Si Noa toma el yogur de su vecino: retirarlo con calma y avisar de inmediato a la educadora y, si hay señales graves, a emergencias; no improviso. Registro: «Amaru comió la mitad de su plato». Aviso: contaría los hechos reales, por ejemplo «Noa tomó el yogur de su vecino y alcanzó a probarlo».",
        ["verifica minuta, fichas y rótulos", "ante el riesgo retira, avisa y no improvisa", "el registro es un hecho sin etiqueta"],
        ["hoja con verificación, acción ante el riesgo y registro"],
        ["improvisar un tratamiento", "no avisar a la educadora", "etiquetar a Amaru"],
        "Pregunta: «¿qué pasaría si Noa muestra señales graves?». Debe decir que avisa de inmediato a la educadora y a emergencias."),
    reinforce="Escribe tres cosas que verificas antes de servir un almuerzo a niños con fichas especiales.",
    extend="Explica por qué retirar con calma un alimento riesgoso y avisar es mejor que reaccionar con gritos.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (desayuno de ejemplo). 18 niños y niñas presentes. Cada niño recibe 1 pan y 1 vaso de leche; se preparan 2 panes y 2 vasos extra. Los panes vienen en bolsas de 6. La técnica registra al final cuánto comió cada niño: comió todo, comió la mitad o no quiso. "
     "Registro de hoy: 11 comieron todo, 5 la mitad y 2 no quisieron. Duración del desayuno: 30 minutos, de 8:30 a 9:00. Cada vaso tiene un círculo marcado con el nombre del niño y su dibujo.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio con datos: calcular raciones y panes, comprobar un registro de alimentación y comunicarlo a la educadora sin etiquetar.",
    prior=["Conozco la ficha de requerimientos y la minuta.", "Sé dividir y redondear hacia arriba.", "Sé registrar hechos."],
    explain=[
        "Calcular las raciones es multiplicar lo que recibe cada niño por el número de niños y sumar los extras. Si algo se compra o llega en bolsas, se divide lo necesario entre el contenido de la bolsa y se redondea hacia arriba. Antes de servir se comprueban los totales: ni faltan platos, ni sobran sin razón.",
        "El registro de alimentación cuenta cuántos niños comieron todo, la mitad o no quisieron. Los tres grupos deben sumar los niños presentes; si no suman, se revisa. Al comunicar el registro a la educadora se usan cifras y hechos, como «5 comieron la mitad», y no frases como «no comen bien», que son juicios. La técnica no interpreta si un niño come poco o mucho: informa y la educadora decide.",
        "La autonomía también se planifica: vasos marcados con el nombre y el dibujo, mesas a la altura de los niños y tiempo suficiente para comer sin apuro." + LIM,
    ],
    vocab=[("ración", "porción de comida o bebida para un niño"), ("extra", "ración adicional preparada por si hace falta"), ("registro de alimentación", "anotación de cuánto comió cada niño"), ("comprobar los totales", "verificar que los grupos sumen los niños presentes"), ("juicio", "opinión sobre un niño que no se puede comprobar")],
    worked=[
        ("Calcular raciones", "En otro desayuno de ejemplo hay 14 niños, cada uno con 1 pan, y se preparan 3 extras. ¿Cuántos panes se preparan?", ["14 por niño más 3 extras.", "14 + 3 = 17."], "17 panes"),
        ("Comprobar un registro", "Un registro dice: 8 comieron todo, 4 la mitad y 3 no quisieron, con 16 niños presentes. ¿Está bien?", ["Se suman los tres grupos: 8 + 4 + 3 = 15.", "Faltaría 1 niño."], "No: suman 15 y hay 16 presentes"),
    ],
    mistakes=[("Informar «hoy los niños no comieron bien».", "Es un juicio vago que no dice cuántos ni qué ocurrió.", "Informa cifras: «11 comieron todo, 5 la mitad y 2 no quisieron»."),
              ("Servir a todos y descubrir que falta pan para el último niño.", "No se calculó antes ni se comprobaron los totales.", "Calcula y cuenta antes de servir.")],
    T=[
        ("=", "{F} ¿Cuántos panes se preparan en total, con los extras?", "18+2", "Se suman los panes extra a uno por niño.", " panes"),
        ("=", "{F} ¿Cuántas bolsas de 6 panes hay que abrir para tener los panes preparados?", "(20+5)//6", "Se dividen los panes necesarios por los de cada bolsa y se redondea hacia arriba.", " bolsas"),
        ("=", "{F} ¿Cuántos niños suman los tres grupos del registro?", "11+5+2", "Se suman los que comieron todo, la mitad y no quisieron.", " niños"),
        ("abc", "{F} ¿Coincide el registro con los niños presentes?", "Sí: suma 18, igual que los presentes", "No: suma 20", "No: suma 16", "11 + 5 + 2 = 18 coincide con los 18 presentes."),
        ("=", "{F} ¿Cuántos niños comieron menos que todo?", "5+2", "Se suman los que comieron la mitad y los que no quisieron.", " niños"),
        ("abc", "{F} ¿Cómo informa la técnica el registro a la educadora?", "«11 comieron todo, 5 la mitad y 2 no quisieron»", "«Los niños comen mal»", "«Hoy hubo mañosos»", "Se informan cifras y hechos, no juicios."),
        ("=", "{F} Si el desayuno dura 30 minutos y empieza a las 8:30, ¿a qué minuto después de las 8:00 termina?", "30+30", "Se suman los minutos del inicio y la duración.", " minutos"),
        ("abc", "{F} ¿Para qué sirven los vasos con nombre y dibujo?", "Para que cada niño reconozca su vaso y se evite el intercambio", "Para decorar las mesas", "Para que solo los grandes los usen", "El nombre y el dibujo favorecen la autonomía y la higiene."),
        ("abc", "{F} Un niño derrama su leche. ¿Qué hace la técnica?", "Lo tranquiliza, limpia con calma y le ofrece otro vaso si hay extra", "Lo regaña frente al grupo", "Le dice que se quedó sin leche", "El derrame es normal y se resuelve con calma."),
        ("abc", "{F} Una técnica anota: «Camila no quiso nada, seguro está enferma». ¿Qué corresponde?", "Anotar «Camila no quiso comer» y avisar a la educadora, sin suponer causas", "Mantener la nota", "Darle un remedio casero", "La técnica no diagnostica; informa lo observado."),
        ("=", "{F} Si faltaran 3 niños mañana, ¿cuántos panes sin extras se prepararían?", "18-3", "A los niños de hoy se les restan los ausentes.", " panes"),
        ("abc", "{F} El registro de otro día muestra 4 niños que no quisieron comer, más que los 2 de hoy. ¿Qué hace la técnica?", "Informa la cifra a la educadora para que decida si hay algo que revisar", "Cambia la minuta ella sola", "No lo informa porque son pocos", "Informar permite que la educadora evalúe; la técnica no interpreta."),
        ("abc", "{F} Al servir, la técnica ve que solo hay 16 panes para los 18 niños presentes, porque dos bolsas llegaron incompletas. ¿Qué hace?", "Avisa a la educadora y propone repartir lo disponible entre todos mientras se resuelve", "Quita pan a otros niños sin avisar", "Los deja sin desayuno", "Se avisa de la falta y se busca una solución inmediata con la educadora."),
    ],
    ctx=("abc", "{F} La educadora pregunta al final cuántos niños comieron menos del desayuno. La técnica no registró durante el desayuno y no recuerda con certeza. ¿Qué responde?", "Dice lo que recuerda con claridad, aclara que no tomó registro y lo hará desde mañana", "Inventa una cifra para quedar bien", "Dice que todos comieron bien", "Una cifra inventada daña la confianza; la honestidad permite mejorar."),
    sc=[
        ("En Atención de Párvulos: ¿cómo se calculan las raciones?", "Se multiplica por los niños y se suman los extras", "Así se prepara lo necesario para todos los niños presentes."),
        ("¿Cuándo está bien un registro de alimentación?", "Cuando los grupos suman los niños presentes", "Si los grupos no suman los presentes, se revisa el registro."),
        ("¿Informas cifras o juicios a la educadora?", "Cifras y hechos", "Los juicios no se pueden comprobar."),
    ],
    op=("Datos de ejemplo: colación de 20 niños y niñas. Cada niño recibe 1 fruta y 1 vaso de agua; se preparan 3 frutas y 3 vasos extra. Las frutas vienen en cajas de 8. Registro: 12 comieron toda su fruta, 6 la mitad y 3 no quisieron. "
        "Escribe: cuántas frutas se preparan y cuántas cajas; si el registro cuadra con los niños presentes; y cómo informarías el registro a la educadora.",
        "Frutas: 20 + 3 = 23; cajas: 23 ÷ 8 = 2 y sobran 7, se necesitan 3 cajas. Registro: 12 + 6 + 3 = 21, pero hay 20 presentes: no cuadra; hay que revisarlo. Informe: «Hay un error en el registro que debo corregir; ya conté 12, 6 y 3; reviso y te aviso». Una vez corregido se informan solo cifras.",
        ["calcula frutas y cajas", "detecta que el registro no cuadra", "informa con honestidad y sin etiquetar"],
        ["hoja con cuentas, revisión del registro y mensaje"],
        ["no redondear hacia arriba las cajas", "no revisar el registro", "informar un juicio"],
        "Pregunta: «¿qué harías si el error fuera un niño contado dos veces?». Debe corregir el registro y avisar."),
    reinforce="Inventa un registro de alimentación para 12 niños con tres grupos y comprueba que suma 12.",
    extend="Explica por qué informar cifras ayuda más a la educadora que decir «hoy comieron mal».",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (rutina de higiene, sala cuna de ejemplo). 8 niños y niñas. Cada muda se anota en una planilla con la hora, el tipo (mojado o sucio) y las observaciones. Reglas del jardín de ejemplo: lavarse las manos antes y después; tener el material preparado antes de comenzar; "
     "no dejar nunca a un niño solo sobre la superficie de mudar; hablarle y mirarlo mientras se le atiende. La técnica de mudar se aprende en práctica supervisada por la educadora.")
build(
    O5, 1, F,
    use="Aprenderé el contexto de la muda y del apoyo al vestir y desvestir: higiene, seguridad, respeto, ergonomía y qué se registra y se avisa.",
    prior=["Conozco el buen trato y el registro de hechos.", "Sé que ante una duda se avisa a la educadora.", "Sé multiplicar."],
    explain=[
        "En Atención de Párvulos, mudar es cambiar el pañal y la ropa de un niño o niña pequeño. Es un momento de cuidado y de vínculo: se le habla, se le mira y se le explica lo que se hace, porque también se aprende a confiar. Los principios que lo guían son la higiene (lavado de manos, superficie limpia y residuos en el basurero indicado), la seguridad (material preparado antes y nunca dejar al niño solo en la superficie de mudar) y el respeto por su intimidad.",
        "Los niños mayores de dos años aprenden a vestirse y desvestirse con autonomía: se les ofrece tiempo, ropa fácil de poner y la posibilidad de elegir entre dos prendas, y el adulto ayuda solo en lo que aún no pueden hacer. La ergonomía es cuidar la postura y el esfuerzo del adulto para no lesionar su espalda: superficie a la altura adecuada, espalda recta y pedir ayuda si hace falta.",
        "Se anota cada muda en la planilla. Si se observa algo distinto, como la piel muy roja o una lesión, no se interpreta ni se aplica nada: se avisa a la educadora. La técnica concreta de mudar se aprende solo en práctica supervisada." + LIM,
    ],
    vocab=[("muda", "cambio de pañal y de ropa de un niño pequeño"), ("autonomía al vestirse", "ponerse y sacarse prendas con el apoyo justo"), ("ergonomía", "cuidado de la postura y del esfuerzo del adulto para no lesionarse"), ("planilla de mudas", "registro de hora, tipo y observaciones de cada muda"), ("intimidad", "derecho a que el cuerpo y su cuidado se respeten"), ("residuos", "pañales y toallitas usados, que se eliminan en el basurero indicado")],
    worked=[
        ("Calcular registros", "En una sala de ejemplo hay 5 niños y se espera anotar 3 mudas por niño. ¿Cuántos registros hay en la planilla?", ["Se multiplican niños por mudas.", "5 × 3 = 15."], "15 registros"),
        ("Qué hacer con una observación", "La técnica nota que un niño de ejemplo tiene la piel muy roja en la zona del pañal. ¿Qué hace?", ["No le corresponde interpretar ni aplicar productos.", "Anota el hecho y avisa a la educadora."], "Anotar lo observado y avisar a la educadora"),
    ],
    mistakes=[("Dejar a un niño solo un momento sobre la superficie de mudar para buscar el pañal.", "Un niño pequeño puede caer en segundos.", "Prepara todo antes de comenzar y no te alejes."),
              ("Decirle a un niño que se vista rápido porque «se hace tarde», sin darle tiempo.", "Le quita la oportunidad de aprender y le genera presión.", "Ofrece tiempo y apoyo solo en lo necesario.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es mudar a un niño o niña?", "Cambiar su pañal y su ropa", "Llevarlo a dormir", "Darle de comer", "Mudar es cambiar el pañal y la ropa."),
        ("abc", "{F} ¿Cuándo se lava las manos la técnica?", "Antes y después de la muda", "Solo después", "Solo si se ve sucia", "La ficha pide lavarse antes y después."),
        ("abc", "{F} ¿Qué nunca se hace con un niño sobre la superficie de mudar?", "Dejarlo solo", "Hablarle", "Mirarlo", "La regla central es no dejarlo solo ni un instante."),
        ("abc", "{F} ¿Por qué el material se prepara antes de comenzar?", "Para no tener que alejarse del niño", "Para ahorrar pañales", "Para que otro niño lo use", "Con todo a mano no hay que dejar al niño solo."),
        ("=", "{F} Si se espera anotar 3 mudas por niño, ¿cuántos registros deben quedar en la planilla de los 8 niños?", "8*3", "Se multiplican los niños por las mudas de cada uno.", " registros"),
        ("abc", "{F} Una técnica nota la piel de un niño muy roja en la zona del pañal. ¿Qué hace?", "Anota lo observado y avisa a la educadora", "Le aplica una crema de su bolso", "Lo comenta con la familia en la puerta", "No se interpreta ni se aplica nada; se anota y se avisa."),
        ("abc", "Un niño de 3 años quiere ponerse solo sus zapatillas y tarda. ¿Qué es lo más adecuado?", "Darle tiempo y ayudar solo si lo pide o no puede", "Ponérselas de inmediato", "Decirle que tarda mucho", "Dar tiempo favorece la autonomía del niño al vestirse."),
        ("=", "{F} Si una muda tarda 5 minutos con los preparativos, ¿cuántos minutos se necesitan para 8 niños, una muda cada uno?", "5*8", "Se multiplican los minutos por el número de niños.", " minutos"),
        ("abc", "Una visita del jardín se ofrece a mudar a un niño «para ayudar». ¿Qué corresponde?", "Agradecer y avisar a la educadora: solo lo hacen las personas del equipo autorizadas", "Dejarla porque es amable", "Pedirle que lo haga si el niño está tranquilo", "La muda es parte del cuidado a cargo del equipo, para proteger a los niños."),
        ("abc", "{F} Una técnica explica a un niño: «ahora te voy a cambiar el pañal; te aviso todo lo que hago». ¿Qué principio se aplica?", "El respeto: se le informa lo que se hace", "La ergonomía de la espalda", "El inventario de pañales", "Hablarle e informarle respeta su intimidad y lo tranquiliza."),
        ("abc", "La superficie de mudar está muy baja y la técnica se agacha cada vez. ¿Qué principio revisa?", "La ergonomía, para cuidar su espalda", "La autonomía del niño", "El inventario", "La altura de la superficie afecta la postura del adulto."),
        ("=", "{F} La planilla debía tener 24 registros pero tiene 19. ¿Cuántos faltan?", "24-19", "A los registros esperados se les restan los anotados.", " registros"),
        ("abc", "{F} Se agotan las toallitas húmedas en mitad de una muda. ¿Qué hace la técnica?", "Pide ayuda sin dejar al niño solo y repone después", "Va a buscarlas y deja al niño un momento", "Termina sin limpiar bien", "Se pide ayuda, porque nunca se deja al niño solo."),
    ],
    ctx=("abc", "{F} Un niño de ejemplo se resiste a que lo mude, llora y dice «no quiero». ¿Qué hace la técnica?", "Le habla con calma, le explica lo que hará, le da una opción pequeña y avisa a la educadora si persiste", "Lo sujeta y lo muda rápido", "Lo deja sin mudar para no incomodarlo", "Se respeta al niño con calma y explicaciones, y la educadora decide cómo apoyar."),
    sc=[
        ("En Atención de Párvulos: ¿qué haces antes de comenzar una muda?", "Lavo mis manos y preparo el material", "Así no dejo al niño solo ni contamino."),
        ("¿Qué haces si ves la piel de un niño muy enrojecida?", "Anoto y aviso a la educadora, sin interpretar", "La técnica no diagnostica ni aplica productos."),
        ("En educación de párvulos: ¿qué es la ergonomía?", "Cuidar mi postura y el esfuerzo para no lesionarme", "La espalda del adulto también se protege."),
    ],
    op=("Caso de ejemplo. Sala cuna con 6 niños y niñas, 2 técnicas y la educadora. La regla de ejemplo es revisar a cada niño cada 2 horas. A las 8:30 la planilla marca mudas para Lía y Bruno. Emilia, de 2 años y medio, quiere ponerse sola sus calcetines y se demora. "
        "Escribe: qué se prepara antes de mudar; cómo hablar a un niño durante la muda; qué harías con Emilia; y qué anotarías y avisarías si ves una lesión en la piel.",
        "Preparo pañales, toallitas, ropa y el basurero antes de comenzar, y me lavo las manos. Hablo y miro al niño: «te voy a cambiar el pañal». A Emilia le doy tiempo y ayudo solo si lo pide. Si veo una lesión: la anoto como hecho y aviso a la educadora; no aplico nada.",
        ["nombra preparación e higiene", "respeta la intimidad y la autonomía", "ante una lesión anota y avisa sin interpretar"],
        ["hoja con cuatro respuestas breves"],
        ["dejar al niño solo", "aplicar un producto", "no avisar a la educadora"],
        "Pregunta: «¿qué pasaría si Emilia no quiere ponerse los calcetines?». Debe ofrecer una opción y respetar su ritmo."),
    reinforce="Escribe tres reglas de seguridad, higiene y respeto para el momento de la muda.",
    extend="Explica por qué la técnica concreta de mudar solo se aprende en práctica supervisada.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (vocabulario, de ejemplo). Superficie de mudar: firme, limpia y a la altura de la cintura del adulto. Planilla de mudas: hora, tipo y observaciones. "
     "Ropa de cambio: prendas limpias y rotuladas con el nombre, guardadas en la mochila de cada niño. Residuos: pañales y toallitas usados, que se eliminan en el basurero con tapa que indica el jardín. "
     "Para vestirse a partir de los dos años: ofrecer dos prendas a elegir, ropa fácil de poner, tiempo suficiente y ayuda solo en lo que el niño aún no logra.")
build(
    O5, 2, F,
    use="Aprenderé el vocabulario y los documentos de la muda y del vestir: higiene, residuos, ropa de cambio, planilla y apoyo a la autonomía.",
    prior=["Conozco el contexto de la muda.", "Sé la importancia de no dejar solo al niño.", "Sé leer una ficha."],
    explain=[
        "Los documentos y elementos de la muda son: la planilla, donde se anota cada muda con su hora, su tipo y las observaciones; la ropa de cambio, que cada familia envía limpia y rotulada; y los residuos, que se eliminan en el basurero con tapa que indica el jardín. La superficie se limpia y se desinfecta según el protocolo del establecimiento después de cada uso. Las manos se lavan antes y después.",
        "La higiene protege la salud del niño y del equipo: se evita tocar con las manos sucias objetos de la sala, y se usa material propio de cada niño. La seguridad exige no dejar nunca solo al niño en la superficie de mudar y comprobar que los objetos peligrosos estén fuera de su alcance. El respeto es hablar con el niño, informarle y proteger su intimidad, sin comentarios sobre su cuerpo.",
        "Para vestirse, el niño de dos años o más aprende mejor si elige entre dos prendas, si la ropa es fácil de poner y si hay tiempo. La ergonomía cuida la espalda del adulto: superficie a la altura de la cintura, cuerpo cerca del niño y pedir ayuda cuando haga falta." + LIM,
    ],
    vocab=[("superficie de mudar", "lugar firme, limpio y a la altura adecuada para el adulto"), ("ropa de cambio", "prendas limpias y rotuladas que cada niño tiene en el jardín"), ("desinfectar", "limpiar de modo que no queden gérmenes, según el protocolo del establecimiento"), ("rotulado", "con el nombre escrito para reconocer lo que es de cada niño"), ("elegir entre dos prendas", "ofrecer dos opciones para favorecer la autonomía"), ("protocolo", "pasos acordados por el establecimiento para una tarea")],
    worked=[
        ("Elegir con autonomía", "Un niño de ejemplo de 3 años debe vestirse. ¿Qué es mejor: «ponte esto» o «¿quieres la polera roja o la azul?»?", ["La segunda da una elección.", "La elección favorece su autonomía."], "«¿Quieres la polera roja o la azul?»"),
        ("Ropa de cambio", "Una mochila de ejemplo tiene 2 poleras, 2 pantalones y 3 calcetines para 4 niños, a razón de una de cada para todos. ¿Alcanza?", ["Cada niño necesita 1 polera, 1 pantalón y 1 calcetín.", "Hay 2 poleras para 4 niños: no alcanza."], "No alcanza"),
    ],
    mistakes=[("Comentar «qué grande está» sobre el cuerpo de un niño mientras se le muda.", "Los comentarios sobre el cuerpo vulneran su intimidad.", "Habla de lo que haces y no de su cuerpo."),
              ("Usar la ropa de cambio de un niño para otro porque es parecida.", "Es poco higiénico y la ropa es de cada niño.", "Usa solo su ropa rotulada o consulta a la educadora.")],
    T=[
        ("abc", "{F} ¿Dónde se eliminan los pañales usados?", "En el basurero con tapa que indica el jardín", "En cualquier basurero de la sala", "En la mochila del niño", "La ficha pide un basurero con tapa indicado por el jardín."),
        ("abc", "{F} ¿Cómo debe ser la ropa de cambio?", "Limpia y rotulada con el nombre del niño", "Usada pero doblada", "Sin rotular, para usarla en cualquiera", "Rotular evita confusiones y cuida la higiene."),
        ("abc", "En Atención de Párvulos: ¿qué es la planilla de mudas?", "El registro de hora, tipo y observaciones de cada muda", "La lista de compras de pañales", "El horario de siesta", "La planilla registra la hora, el tipo y las observaciones de cada muda."),
        ("abc", "{F} ¿A qué altura debe estar la superficie de mudar?", "A la altura de la cintura del adulto", "Al nivel del piso", "A la altura de los hombros", "A la cintura se evita doblar la espalda."),
        ("abc", "{F} Un niño de 3 años va a vestirse. ¿Qué opción favorece su autonomía?", "Ofrecerle dos prendas a elegir", "Vestirlo rápido sin hablarle", "Decirle que lo haga solo sin ayuda ni tiempo", "Dos opciones lo hacen participar y decidir en su vestido."),
        ("=", "{F} Cada muda usa 1 pañal. Si hay 8 niños y cada uno recibe 3 mudas, ¿cuántos pañales se usan?", "8*3", "Se multiplican los niños por las mudas de cada uno.", " pañales"),
        ("abc", "{F} ¿Qué se hace con la superficie de mudar después de cada uso?", "Se limpia y desinfecta según el protocolo del jardín", "Se deja sin limpiar si no se ensució", "Se seca con la ropa del niño", "La superficie se limpia siempre según el protocolo."),
        ("=", "{F} Una mochila lleva 3 prendas de cambio por niño. Para 8 niños, ¿cuántas prendas hay en total?", "3*8", "Se multiplican las prendas por los niños.", " prendas"),
        ("abc", "{F} Un niño no tiene ropa de cambio rotulada. ¿Qué hace la técnica?", "Avisa a la educadora para que coordine con la familia", "Le pone la ropa de otro niño sin avisar", "Le deja la ropa mojada", "Se coordina con la familia a través de la educadora."),
        ("abc", "{F} Una técnica comenta en voz alta mientras muda: «qué barriguita tan grande». ¿Qué falla?", "Hace un comentario sobre el cuerpo que no respeta su intimidad", "Nada: es cariñoso", "Que no usó su nombre", "Los comentarios sobre el cuerpo no corresponden."),
        ("abc", "{F} La técnica nota que levantar al niño le duele la espalda. ¿Qué hace?", "Revisa su postura y la altura de la superficie, y pide ayuda a la educadora", "Sigue igual para no molestar", "Lo levanta más rápido", "La ergonomía cuida la espalda del adulto y se revisa la tarea."),
        ("=", "{F} Hay 2 poleras de cambio para 5 niños que las necesitan. ¿Cuántas poleras faltan?", "5-2", "Se restan las poleras disponibles a las necesarias.", " poleras"),
        ("abc", "{F} ¿Qué lavado de manos corresponde?", "Antes y después de cada muda", "Una vez al llegar", "Solo cuando termina el turno", "La ficha pide lavarse antes y después."),
    ],
    ctx=("abc", "{F} Durante la muda, un niño toca el rostro de la técnica y luego su boca con las manos sucias. ¿Qué hace la técnica?", "Termina la muda con calma, lava las manos del niño y las suyas y limpia la superficie", "Lo regaña por tocarla", "Sigue con otra muda sin lavarse", "El lavado de manos y la limpieza son parte de la higiene en cada paso."),
    sc=[
        ("En Atención de Párvulos: ¿dónde se guardan los pañales usados?", "En el basurero con tapa indicado", "Evita la contaminación de los alimentos o del material del niño."),
        ("¿Cómo favoreces la autonomía al vestir?", "Ofreciendo dos prendas y tiempo", "El niño participa, decide y aprende a hacer cosas por sí mismo."),
        ("¿Qué cuida la ergonomía?", "La espalda y el esfuerzo del adulto", "Evita lesiones en el equipo que atiende a los niños."),
    ],
    op=("Datos de ejemplo. Sala cuna de 10 niños. Cada niño tiene en su mochila 2 mudas de ropa rotulada; hoy faltan 3 mochilas con ropa de cambio. La superficie de mudar está a la altura de las rodillas de la técnica. Un niño de 2 años quiere vestirse solo. "
        "Escribe: cuántas mochilas sí tienen ropa; qué corregirías en la superficie y por qué; qué ofrecerías al niño que quiere vestirse solo; y qué harías con las mochilas sin ropa.",
        "Hay 10 − 3 = 7 mochilas con ropa. La superficie debe estar a la altura de la cintura, para cuidar la espalda de la técnica. Al niño le ofrecería dos prendas a elegir y tiempo para ponérselas, ayudando solo lo necesario. Las 3 mochilas sin ropa: avisaría a la educadora para que coordine con las familias.",
        ["calcula las mochilas", "explica la corrección ergonómica", "favorece la autonomía y avisa a la educadora"],
        ["hoja con cuatro respuestas breves"],
        ["usar ropa de otro niño", "no corregir la altura", "no avisar a la educadora"],
        "Pregunta: «¿qué ocurre si el niño elige una prenda que no es para el clima?». Debe consultar a la educadora o dar otra opción."),
    reinforce="Escribe tres elementos que debe tener la mochila de un niño pequeño y por qué se rotulan.",
    extend="Explica por qué elegir entre dos prendas ayuda a un niño de tres años a ser más autónomo.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (planilla de ejemplo, sala cuna de 6 niños, mañana). 8:30 Sofía, mojado. 9:00 Bruno, sucio; observación: piel enrojecida en la zona del pañal. 9:30 Emilia, mojado. 10:00 Tomás, mojado. 10:30 Sofía, sucio. 11:00 Bruno, mojado. "
     "Regla de ejemplo del jardín: revisar a cada niño al menos cada 2 horas (la frecuencia real la fija el protocolo del establecimiento).")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso con una planilla de mudas: contar registros, revisar tiempos, reconocer una observación importante y avisar.",
    prior=["Conozco la planilla y la regla de higiene.", "Sé calcular minutos.", "Sé que lo observado se avisa a la educadora."],
    explain=[
        "Para analizar una planilla se lee cada fila: hora, niño, tipo y observación. Se cuentan los registros, se mira si algún niño lleva más tiempo sin revisión que lo que indica el protocolo del jardín y se detectan las observaciones que requieren aviso. Una observación es un hecho anotado en palabras simples, por ejemplo «piel enrojecida en la zona del pañal».",
        "Cuando aparece una observación así, la técnica avisa a la educadora y no aplica nada por su cuenta. Tampoco la comenta con otras familias ni escribe un diagnóstico. En la planilla se escribe lo que se vio y la hora. Si un niño lleva mucho tiempo sin revisión según la regla del jardín, se revisa de inmediato.",
        "También se revisa que cada muda se haya hecho con la higiene y la seguridad ya aprendidas: manos lavadas, material preparado y ningún niño solo sobre la superficie." + LIM,
    ],
    vocab=[("registro", "fila de la planilla con hora, niño, tipo y observación"), ("observación", "hecho anotado con palabras simples"), ("revisión", "comprobación de si el niño necesita una muda"), ("protocolo", "pasos y reglas acordados por el jardín"), ("aviso", "información dada a la educadora")],
    worked=[
        ("Contar mudas por niño", "En una planilla de ejemplo, Noa tiene registros a las 8:00, 10:00 y 12:00. ¿Cuántas mudas tuvo?", ["Cada hora anotada es una muda.", "Son tres horas."], "3 mudas"),
        ("Reconocer un aviso", "En otra planilla de ejemplo aparece «mancha roja nueva en la espalda». ¿Qué corresponde?", ["Es una observación sobre la piel.", "Se anota el hecho y se avisa a la educadora."], "Avisar a la educadora"),
    ],
    mistakes=[("Escribir en la planilla «tiene una infección» al ver piel enrojecida.", "Es un diagnóstico que la técnica no puede hacer.", "Escribe el hecho: «piel enrojecida en la zona del pañal»."),
              ("No avisar de la observación y esperar a que la familia lo note.", "La educadora debe saberlo para decidir cómo actuar.", "Avisa el mismo día.")],
    T=[
        ("abc", "{F} ¿Cuántos registros tiene la planilla?", "6", "5", "7", "La planilla tiene seis filas: 8:30, 9:00, 9:30, 10:00, 10:30 y 11:00."),
        ("abc", "{F} ¿Qué niño tiene una observación sobre la piel?", "Bruno", "Sofía", "Tomás", "La observación aparece en la fila de Bruno a las 9:00."),
        ("abc", "{F} ¿Cuántas veces fue mudada Sofía, según la planilla?", "2", "1", "3", "Sofía aparece a las 8:30 y a las 10:30."),
        ("=", "{F} Sofía tuvo su primera muda a las 8:30 y la segunda a las 10:30. ¿Cuántos minutos pasaron?", "(10*60+30)-(8*60+30)", "Se restan las horas, convertidas a minutos.", " minutos"),
        ("abc", "{F} ¿Qué hace la técnica con la observación de Bruno?", "Avisa a la educadora y no aplica nada", "Le aplica una crema de la mochila", "Le dice a la madre que tiene una enfermedad", "Se informa; la técnica no diagnostica ni aplica productos."),
        ("abc", "{F} ¿Cuál es la forma correcta de anotar la observación?", "«Piel enrojecida en la zona del pañal»", "«Tiene una infección»", "«Es por no cambiarlo a tiempo»", "Se anota el hecho y no el diagnóstico ni la causa."),
        ("abc", "{F} Emilia fue mudada a las 9:30. Según la regla de ejemplo, ¿a qué hora como máximo debe revisarse de nuevo?", "A las 11:30", "A las 10:30", "A las 12:30", "Dos horas después de las 9:30 son las 11:30; las otras horas son una hora y tres horas después."),
        ("abc", "{F} Son las 12:15 y a Tomás no se le ha revisado desde su muda de las 10:00. ¿Qué corresponde?", "Revisarlo de inmediato, porque ya pasaron más de 2 horas", "Esperar hasta las 13:00", "Esperar a que llore", "De las 10:00 a las 12:15 pasaron 2 horas y 15 minutos, más de lo que indica la regla."),
        ("abc", "{F} La madre de Bruno pregunta en la puerta qué le pasa en la piel a su hijo. ¿Qué responde la técnica?", "Que la educadora podrá conversarlo con ella en privado", "Que probablemente es por el pañal", "Que debe comprarle una crema", "Los temas de salud los conversa la educadora en privado y sin diagnósticos."),
        ("=", "{F} Si la sala tiene 6 niños y la planilla debería tener 12 registros esta mañana, ¿cuántos faltan?", "12-6", "A los registros esperados se les restan los anotados.", " registros"),
        ("abc", "{F} La técnica olvidó anotar la hora de la muda de Emilia. ¿Qué hace?", "La anota con la hora aproximada y lo aclara a la educadora", "No anota nada", "Inventa una hora exacta", "Se anota con honestidad lo que se recuerda y se aclara."),
        ("abc", "{F} Otra técnica propone comentar el caso de Bruno con las demás familias «para prevenir». ¿Qué observación corresponde?", "Es un dato confidencial que no se comenta con otras familias", "Está bien, para informar", "Está bien si se omite el apellido", "Los datos de un niño no se comparten con otras familias."),
        ("abc", "{F} ¿Qué falla si la técnica mudó a Tomás sin lavarse las manos antes?", "No cumplió la higiene antes de la muda", "Nada, porque las lava después", "Que no registró la hora", "La ficha de reglas exige lavarse antes y después."),
    ],
    ctx=("abc", "{F} A las 11:15 un niño de la sala llora y la técnica nota que su pañal está sucio. Pero la educadora la llama por otro motivo. ¿Qué hace?", "Avisa a la educadora que debe mudar al niño y lo hace en cuanto puede, o pide a otra técnica que lo atienda", "Lo deja llorando hasta terminar lo demás", "Lo muda dejando solo a otro niño", "Se prioriza el cuidado del niño y se coordina para no dejar a nadie solo."),
    sc=[
        ("En Atención de Párvulos: ¿qué anotas ante piel enrojecida?", "El hecho, sin diagnóstico", "Los hechos no se interpretan ni se transforman en diagnóstico."),
        ("¿A quién avisas de una observación en la piel?", "A la educadora", "Ella decide cómo actuar y a quién más avisar."),
        ("¿Dejas a un niño solo en la superficie de mudar para ir a buscar algo?", "Nunca", "Un niño pequeño puede caer en segundos."),
    ],
    op=("Planilla de ejemplo (sala cuna de 5 niños): 8:30 Noa, mojado. 9:00 Amaru, sucio; observación: «lloró y se tocaba la barriga». 9:30 Lía, mojado. 10:30 Noa, sucio. "
        "Regla de ejemplo: revisar a cada niño cada 2 horas como máximo. "
        "Escribe: cuántos registros hay y cuántas mudas tuvo Noa; cuál es la observación importante y a quién avisarías; cómo la anotarías sin diagnosticar; y qué hora límite tendría Amaru para su próxima revisión.",
        "Hay 4 registros y Noa tuvo 2 mudas. La observación de Amaru (se tocaba la barriga y lloró) se avisa a la educadora. Se anota el hecho tal cual: «lloró y se tocaba la barriga». La próxima revisión de Amaru, desde las 9:00 más 2 horas, es a más tardar a las 11:00.",
        ["cuenta bien los registros y las mudas", "avisa a la educadora y no diagnostica", "calcula la hora límite"],
        ["hoja con cuatro respuestas breves"],
        ["escribir un diagnóstico", "no avisar", "calcular mal la hora"],
        "Pregunta: «¿qué pasaría si Amaru vuelve a llorar?». Debe volver a avisar a la educadora y seguir anotando hechos."),
    reinforce="Cuenta los registros de una planilla inventada de 5 niños y marca cuáles requieren aviso a la educadora.",
    extend="Explica por qué anotar «piel enrojecida» ayuda más que anotar un diagnóstico.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (turno de ejemplo, sala cuna de 10 niños y niñas). En promedio, cada niño necesita 4 mudas por jornada (dato de ejemplo). Cada muda usa 1 pañal y 3 toallitas húmedas. Los pañales vienen en paquetes de 30 y las toallitas en paquetes de 80. "
     "Hay 2 técnicas en la sala. Principios de ergonomía: superficie a la altura de la cintura, espalda recta, rodillas flexionadas para levantar, cuerpo cerca de la carga, evitar girar el tronco y pedir ayuda cuando la tarea no sea segura.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar un criterio con datos: calcular mudas, insumos y reposición, repartir el trabajo y aplicar principios de ergonomía.",
    prior=["Conozco la planilla y la higiene.", "Sé redondear hacia arriba.", "Sé multiplicar y dividir."],
    explain=[
        "Calcular los insumos de una muda es multiplicar: mudas totales por unidades usadas. Primero se multiplica el número de niños por las mudas de cada uno y luego los pañales y las toallitas por muda. Como los insumos vienen en paquetes, se divide lo necesario entre el contenido y se redondea hacia arriba, porque no se puede abrir medio paquete. Estos números son datos de ejemplo; en un jardín se usan los que fija su protocolo.",
        "Repartir el trabajo es dividir las mudas entre las técnicas disponibles para no sobrecargar a ninguna. La ergonomía ayuda a prevenir lesiones: la superficie a la altura de la cintura, la espalda recta, las rodillas flexionadas para levantar, el cuerpo cerca de la carga y evitar girar el tronco al levantar. Si el niño pesa o la tarea no parece segura, se pide ayuda a otra persona del equipo.",
        "Todo se registra en la planilla y los insumos que sobran se guardan en el lugar indicado, fuera del alcance de los niños." + LIM,
    ],
    vocab=[("insumo", "material que se gasta, como pañales y toallitas"), ("reposición", "compra o reemplazo de lo que se gastó"), ("sobrecarga", "exceso de trabajo o esfuerzo en una persona"), ("postura", "forma de colocar el cuerpo"), ("pedir ayuda", "pedir a otra persona que colabore cuando la tarea no es segura")],
    worked=[
        ("Calcular mudas totales", "En una sala de ejemplo hay 7 niños con 3 mudas cada uno. ¿Cuántas mudas hay?", ["Se multiplican los niños por las mudas.", "7 × 3 = 21."], "21 mudas"),
        ("Paquetes necesarios", "Se necesitan 50 pañales y el paquete trae 20. ¿Cuántos paquetes hay que abrir?", ["50 ÷ 20 = 2 y sobran 10.", "Se necesita un tercer paquete."], "3 paquetes"),
    ],
    mistakes=[("Levantar al niño con la espalda doblada y girando el tronco.", "Es una postura que puede lesionar la espalda.", "Flexiona las rodillas, mantén la espalda recta y el cuerpo cerca."),
              ("Calcular los paquetes sin redondear hacia arriba.", "Quedan sin pañales los últimos niños.", "Redondea hacia arriba y prepara con anticipación.")],
    T=[
        ("=", "{F} ¿Cuántas mudas se esperan en la jornada, con los 10 niños?", "10*4", "Se multiplican los niños por las mudas de cada uno.", " mudas"),
        ("=", "{F} ¿Cuántos pañales se usan en la jornada?", "10*4*1", "Cada muda usa un pañal.", " pañales"),
        ("=", "{F} ¿Cuántas toallitas húmedas se usan en la jornada?", "40*3", "Cada muda usa 3 toallitas.", " toallitas"),
        ("=", "{F} ¿Cuántos paquetes de pañales hay que abrir en la jornada?", "(40+29)//30", "Se dividen los pañales entre los del paquete y se redondea hacia arriba.", " paquetes"),
        ("=", "{F} ¿Cuántos paquetes de toallitas hay que abrir en la jornada?", "(120+79)//80", "Se dividen las toallitas entre las del paquete y se redondea hacia arriba.", " paquetes"),
        ("=", "{F} Si las 40 mudas se reparten por igual entre las 2 técnicas, ¿cuántas hace cada una?", "40//2", "Se divide el total de mudas entre las técnicas.", " mudas"),
        ("abc", "{F} ¿Qué postura cuida la espalda al levantar a un niño?", "Rodillas flexionadas, espalda recta y niño cerca del cuerpo", "Espalda doblada y brazos extendidos", "Tronco girado hacia un lado", "La ficha recomienda flexionar rodillas, espalda recta y carga cerca."),
        ("abc", "{F} Una técnica siente dolor al levantar siempre al mismo niño. ¿Qué hace?", "Revisa su postura, pide ayuda a su compañera y avisa a la educadora", "Lo levanta más rápido", "Deja de mudarlo", "Se previenen lesiones pidiendo ayuda y revisando la tarea."),
        ("=", "{F} Si cada muda tarda 6 minutos, ¿cuántos minutos suma una técnica que hace 20 mudas?", "20*6", "Se multiplican las mudas por los minutos de cada una.", " minutos"),
        ("abc", "{F} Faltan 5 toallitas para terminar la jornada. ¿Qué hace la técnica?", "Avisa a la educadora para reponerlas y no deja a ningún niño solo", "Usa una sola toallita por muda", "Reutiliza toallitas usadas", "Se informa y se repone; reutilizar rompe la higiene."),
        ("=", "{F} Si hoy faltan 2 niños, ¿cuántos pañales se usan en lugar de 40?", "8*4", "Se multiplican los niños presentes por las mudas de cada uno.", " pañales"),
        ("abc", "{F} Dos niños necesitan muda a la vez y hay una técnica sola con ellos. ¿Qué hace?", "Atiende a uno sin dejar solo al otro y pide ayuda a la otra técnica o a la educadora", "Deja a uno en el piso mientras muda al otro", "Muda a ambos a la vez", "Se pide ayuda; no se deja solo a un niño ni se actúa con riesgo."),
        ("abc", "{F} El jardín ofrece una superficie de mudar muy baja. ¿Qué observación corresponde?", "Avisar a la educadora que debe ajustarse a la altura de la cintura", "Aceptarla porque no se puede cambiar", "Mudar a los niños en el piso", "La ergonomía exige ajustar la altura; se avisa a quien corresponde."),
    ],
    ctx=("abc", "{F} A mitad de la jornada, la técnica nota que quedan 12 pañales y aún faltan 14 mudas. ¿Qué hace?", "Avisa a la educadora para reponer, ya que los pañales no alcanzan", "Espera a que se acaben", "Usa un pañal por cada dos niños", "Se avisa con tiempo y no se compromete la higiene."),
    sc=[
        ("En Atención de Párvulos: ¿cómo se calculan los pañales de una jornada?", "Multiplicando niños por mudas por pañales", "El total depende de cuántas mudas hay."),
        ("¿Cómo se calcula cuántos paquetes abrir?", "Dividiendo y redondeando hacia arriba", "No se abre medio paquete, por eso se redondea hacia arriba."),
        ("¿Qué haces si una tarea no es segura para tu espalda?", "Pido ayuda", "Pedir ayuda previene lesiones de la técnica y caídas del niño."),
    ],
    op=("Datos de ejemplo. Sala cuna de 12 niños y niñas, con 3 mudas por niño en la jornada. Cada muda usa 1 pañal y 2 toallitas. Los pañales vienen en paquetes de 25 y las toallitas en paquetes de 50. Hay 2 técnicas. "
        "Escribe: las mudas, los pañales y las toallitas de la jornada; cuántos paquetes de cada uno; cuántas mudas hace cada técnica; y dos reglas de ergonomía que aplicarías.",
        "Mudas: 12 × 3 = 36. Pañales: 36; toallitas: 72. Paquetes de pañales: 36 ÷ 25 = 1 y sobran 11, se necesitan 2. Paquetes de toallitas: 72 ÷ 50 = 1 y sobran 22, se necesitan 2. Cada técnica hace 18 mudas. Ergonomía: espalda recta con rodillas flexionadas al levantar y superficie a la altura de la cintura.",
        ["calcula mudas e insumos", "redondea hacia arriba los paquetes", "nombra dos reglas de ergonomía"],
        ["hoja con cálculos y dos reglas"],
        ["no redondear hacia arriba", "olvidar las toallitas", "decir reglas inseguras"],
        "Pregunta: «¿qué cambiaría si faltara una técnica?». Debe decir que una sola haría 36 mudas y habría que pedir apoyo."),
    reinforce="Calcula las mudas y pañales de una sala cuna de ejemplo de 9 niños con 3 mudas cada uno.",
    extend="Explica por qué pedir ayuda cuando la tarea no es segura protege al niño y a la técnica.",
)
