"""Student material for 2.º medio Música, OA 05 (improvisar y crear música con fluidez e innovación, con énfasis en arreglos de canciones y secciones musicales, a partir de proposiciones dadas o rasgos estilísticos y formales acordados).

Las piezas de los ejercicios son descripciones inventadas («de ejemplo»); no hay letras ni partituras con derechos.
La improvisación sonora, el canto y la práctica instrumental quedan para el docente; el cuaderno prepara la planificación y el análisis escrito.
"""
from __future__ import annotations

from student_content_mu_m2_a import L
from student_lessons import arith, ex

OA5 = "MU2M OA 05"

# ---------------------------------------------------------------- OA 05 · clase 1 (improvisar dentro de acuerdos)
L(
    OA5, 1,
    "Lápiz y papel. Los patrones rítmicos y los acuerdos están escritos en los ejercicios. Improvisar con voz o instrumento lo dirige tu docente.",
    "Aprenderé qué es improvisar dentro de rasgos acordados (pulso, compás, notas permitidas y forma) y a contar su extensión. Sirve para improvisar con libertad sin perder el pulso ni el estilo del grupo.",
    ["Mantengo un pulso estable.", "Sé qué es un compás y cómo contar pulsos.", "Distingo forma y textura."],
    [
        "Improvisar es crear música en el momento de tocarla o cantarla. No es hacer cualquier cosa: casi siempre se improvisa dentro de acuerdos. Pueden ser un pulso y un tempo, un compás (por ejemplo, 4 pulsos por compás), un conjunto de notas permitidas, una forma (cuántos compases dura cada parte) y un estilo. Esos acuerdos son las proposiciones dadas o rasgos acordados.",
        "Con un acuerdo claro la improvisación gana fluidez, es decir, avanza sin detenerse. Por ejemplo, se acuerda improvisar 4 compases de 4 pulsos sobre un pulso marcado por el grupo; cada persona responde con una frase distinta. Para saber cuánto dura, se multiplican los compases por los pulsos de cada compás: 4 compases de 4 pulsos son 16 pulsos.",
        "Para escribir un patrón rítmico en este cuaderno se usa una notación simple: «ta» es un sonido que dura un pulso, «ti-ti» son dos sonidos que caben en un pulso y «sh» es un silencio de un pulso. Así, «ta ti-ti ta sh» ocupa 4 pulsos (uno por cada grupo) y tiene 4 sonidos: 1 + 2 + 1. Improvisar no es lo mismo que componer: al improvisar se decide sobre la marcha, y al componer se prueba, se corrige y se registra.",
    ],
    [("improvisar", "crear música en el momento de interpretarla"), ("rasgos acordados", "condiciones que el grupo fija para improvisar"), ("compás", "grupo de pulsos que se repite"), ("fluidez", "avance parejo sin detenerse"), ("frase", "idea musical con inicio y final"), ("notación simple", "palabras como «ta», «ti-ti» y «sh» para anotar ritmos")],
    [
        ("Contar la extensión", "Un grupo de ejemplo improvisa 6 compases de 3 pulsos cada uno. ¿Cuántos pulsos dura la improvisación?", ["Se multiplica la cantidad de compases por los pulsos de cada compás.", "6 × 3 = 18."], "18 pulsos"),
        ("Contar pulsos y sonidos", "El patrón de ejemplo «ta ta ti-ti sh» ¿cuántos pulsos ocupa y cuántos sonidos tiene?", ["Cada grupo ocupa un pulso: ta, ta, ti-ti, sh son 4 pulsos.", "Los sonidos son 1 + 1 + 2 = 4; el silencio no suena."], "4 pulsos y 4 sonidos"),
    ],
    [
        ("Pensar que improvisar es tocar sin ninguna regla.", "Sin acuerdos el grupo pierde el pulso y la forma.", "Fija el pulso, el compás, las notas y la duración antes de improvisar."),
        ("Contar el silencio como un sonido.", "El silencio ocupa tiempo pero no suena.", "Cuenta pulsos para el tiempo y sonidos solo para lo que suena."),
    ],
    [
        ex("¿Qué es improvisar? A) Crear música en el momento de interpretarla. B) Repetir una partitura sin cambios.", "A", "Se crea sobre la marcha."),
        ex("¿Cuál es un rasgo acordado? A) Las notas permitidas. B) El color de la sala.", "A", "Las notas permitidas limitan la improvisación."),
        ex("En el patrón «ta ta ta sh», ¿cuántos sonidos hay? A) Tres. B) Cuatro.", "A", "Hay tres «ta»; el silencio no suena."),
    ],
    [
        ex("¿Qué significa «ti-ti» en la notación de la clase? A) Dos sonidos en un pulso. B) Un silencio.", "A", "Es la definición de la notación."),
        ex("¿Qué es la fluidez al improvisar? A) Avanzar sin detenerse. B) Tocar lo más fuerte.", "A", "Se mide por continuidad."),
        ex("¿Qué diferencia a improvisar de componer? A) Al improvisar se decide sobre la marcha y al componer se corrige y registra. B) Al improvisar se registra todo por escrito y al componer no.", "A", "La composición se revisa."),
    ],
    [
        arith("Un grupo de ejemplo improvisa 5 compases de 4 pulsos. ¿Cuántos pulsos hay en total?", "5*4", "Se multiplican compases por pulsos.", " pulsos"),
        ex("El patrón «ti-ti ti-ti ta sh» ¿cuántos pulsos ocupa? A) Cuatro. B) Seis.", "A", "Cada grupo ocupa un pulso: ti-ti, ti-ti, ta y sh son cuatro."),
        ex("El patrón «ti-ti ti-ti ta sh» ¿cuántos sonidos tiene? A) Cinco. B) Seis.", "A", "Suman 2 + 2 + 1 = 5 sonidos; el silencio no suena."),
    ],
    [
        ex("Una persona improvisa 8 compases de 4 pulsos pero el acuerdo era de 4 compases. ¿Qué ocurre? A) Se pasa del acuerdo y puede romper la forma del grupo. B) Cumple el acuerdo.", "A", "No respeta la duración fijada."),
        ex("En un grupo se acuerdan tres notas permitidas. Una persona usa una cuarta nota. ¿Qué observación corresponde? A) Se aparta del acuerdo y habría que consensuarla antes. B) Es válido, porque improvisar significa no tener ningún acuerdo.", "A", "La libertad se ejerce dentro de lo acordado."),
    ],
    [
        ex("Se improvisa preguntas y respuestas: una persona toca una frase de 2 compases y otra responde con otra de 2 compases. Tras 3 intercambios de ida y vuelta, ¿cuántos compases se tocaron en total? A) 12. B) 6.", "A", "Cada intercambio tiene 4 compases y son 3: 12 compases."),
        ex("Un grupo quiere improvisar de manera segura y ordenada. ¿Qué conviene hacer primero? A) Acordar pulso, compás, notas y duración. B) Empezar cada persona con su propio pulso.", "A", "Los acuerdos dan estructura."),
    ],
    [ex("Tu curso hará una ronda de improvisación en la que cada estudiante toca 2 compases de 4 pulsos. ¿Cómo evitas que alguien se sienta presionado? A) Ofrecer elegir entre tocar, marcar el pulso o aportar un ritmo corporal. B) Pedir voluntarios y que los demás no participen.", "A", "Se mantiene la participación con opciones.")],
    [
        ex("¿Verdadero o falso? Improvisar se hace casi siempre dentro de acuerdos.", "Verdadero", "Los acuerdos dan orden."),
        ex("El patrón «ta sh ta sh» ocupa: A) cuatro pulsos. B) dos pulsos.", "A", "Cada grupo es un pulso."),
        ex("¿Qué es una frase? A) Una idea musical con inicio y final. B) Una nota aislada.", "A", "Es la unidad de la improvisación."),
    ],
    (
        "Inventa un acuerdo de improvisación: pulso (lento, medio o rápido), compás de 4 pulsos, tres notas permitidas (nómbralas con los nombres do, re y mi), duración de 4 compases. Escribe a) cuántos pulsos dura tu improvisación, b) un patrón de un compás con «ta», «ti-ti» y «sh», c) cuántos sonidos tiene ese patrón.",
        "a) 4 compases × 4 pulsos = 16 pulsos. b) «ta ti-ti ta sh». c) 4 sonidos (1 + 2 + 1).",
        ["cuenta bien los pulsos totales", "el patrón ocupa exactamente 4 pulsos", "cuenta los sonidos sin incluir el silencio"],
        ["respuestas a), b) y c) escritas"],
        ["patrón que no suma cuatro pulsos", "contar el silencio como sonido"],
        "Reconoce el acuerdo y pide contar los pulsos del patrón uno a uno.",
    ),
    "Palmea un patrón de 4 pulsos con palabras «ta» y «sh» y cuéntalo en voz baja dos veces.",
    "Escribe tres patrones de 4 pulsos distintos y cuenta cuántos sonidos tiene cada uno.",
)

# ---------------------------------------------------------------- OA 05 · clase 2 (innovar a partir de un motivo)
L(
    OA5, 2,
    "Lápiz y papel. Los motivos y sus variaciones están escritos con palabras y con «ta», «ti-ti» y «sh». Tocar o cantar las variaciones lo guía tu docente.",
    "Aprenderé a innovar a partir de un motivo (una idea musical corta) con repetición, variación y contraste, sin perder el estilo acordado. Sirve para improvisar y crear con fluidez y con ideas propias.",
    ["Improviso dentro de rasgos acordados.", "Cuento pulsos y sonidos.", "Distingo forma y textura."],
    [
        "Un motivo es una idea musical corta y reconocible, por ejemplo un patrón rítmico de un compás o tres notas seguidas. Con un motivo se puede construir una improvisación completa. Hay tres recursos básicos: la repetición, que repite el motivo igual; la variación, que lo cambia un poco; y el contraste, que presenta algo distinto.",
        "Se puede variar un motivo cambiando el ritmo (agregar o quitar sonidos), el registro (tocarlo más agudo o más grave), la dinámica (suave o fuerte) o el timbre (otra voz o instrumento). Innovar es proponer una variación nueva que se oiga distinta, pero que mantenga relación con el motivo original y con el estilo acordado. Si todo cambia, se pierde el hilo.",
        "Un buen equilibrio es: presentar el motivo, repetirlo, variarlo y recién entonces contrastarlo. Por ejemplo, el motivo «ta ta ti-ti ta» tiene 4 pulsos y 5 sonidos (1 + 1 + 2 + 1). Una variación puede ser «ta ta ta ta»: mantiene los 4 pulsos pero baja a 4 sonidos. Un contraste puede ser un silencio largo, dos pulsos de «sh» y una melodía nueva.",
    ],
    [("motivo", "idea musical corta y reconocible"), ("repetición", "presentar el motivo igual"), ("variación", "presentar el motivo cambiado un poco"), ("contraste", "presentar algo distinto"), ("registro", "altura general de los sonidos: agudo o grave"), ("innovar", "proponer algo nuevo que mantenga relación con lo acordado")],
    [
        ("Reconocer el recurso", "Un motivo de ejemplo es «ta ti-ti ta sh». Una persona lo toca igual dos veces seguidas. ¿Qué recurso usa?", ["No cambia nada.", "Eso es repetir."], "Repetición"),
        ("Crear una variación", "Motivo de ejemplo: «ta ta ti-ti sh». Propón una variación que mantenga 4 pulsos pero cambie los sonidos.", ["Mantén cuatro grupos de un pulso.", "Cambia, por ejemplo, el segundo «ta» por «ti-ti»."], "«ta ti-ti ti-ti sh», que mantiene 4 pulsos y cambia el ritmo"),
    ],
    [
        ("Cambiar todo el motivo y llamarlo «variación».", "Si no queda nada del motivo, se pierde la relación con la idea original.", "Cambia solo una cualidad a la vez, como el ritmo o el registro."),
        ("Repetir siempre igual y creer que innovas.", "La repetición exacta no propone nada nuevo.", "Alterna repetición, variación y contraste."),
    ],
    [
        ex("¿Qué es un motivo? A) Una idea musical corta y reconocible. B) Una canción completa.", "A", "Es una unidad corta."),
        ex("Tocar el motivo cambiado un poco es: A) variación. B) repetición.", "A", "La variación modifica el motivo."),
        ex("Presentar algo claramente distinto del motivo es: A) contraste. B) repetición.", "A", "El contraste contrasta."),
    ],
    [
        ex("¿Qué cualidad se cambia al tocar el motivo más agudo? A) El registro. B) La forma.", "A", "Agudo o grave es el registro."),
        ex("¿Qué es innovar en la improvisación? A) Proponer algo nuevo que mantenga relación con lo acordado. B) Hacer algo que no tenga relación con nada.", "A", "Debe existir relación con el acuerdo."),
        ex("¿Qué sucede si se cambian todas las cualidades del motivo a la vez? A) Se pierde el hilo con el motivo original. B) Se refuerza la relación.", "A", "No queda rastro del motivo."),
    ],
    [
        ex("Motivo de ejemplo: «ta ti-ti ta ta». ¿Cuántos sonidos tiene? A) Cinco. B) Cuatro.", "A", "1 + 2 + 1 + 1 = 5 sonidos."),
        ex("Motivo «ta ta ta sh» y variación «ta ti-ti ta sh». ¿Qué cambió? A) El ritmo del segundo pulso (de un sonido a dos). B) El número de pulsos.", "A", "Ambos tienen 4 pulsos; el segundo pulso pasó de «ta» a «ti-ti»."),
        arith("Una improvisación de ejemplo repite 3 veces un motivo de 4 pulsos y luego toca un contraste de 8 pulsos. ¿Cuántos pulsos son en total?", "3*4+8", "Se suman las repeticiones y el contraste.", " pulsos"),
    ],
    [
        ex("Una intérprete toca el motivo, lo repite y luego lo toca más suave y más agudo. ¿Qué recursos usó? A) Repetición y variación. B) Solo contraste.", "A", "Repite y luego varía en dinámica y registro."),
        ex("Dos compañeros comparan: Uno cambia el motivo cada compás sin que se reconozca. La otra lo repite, lo varía y lo contrasta en ese orden. ¿Quién logra mejor un hilo musical? A) La que combina los tres recursos. B) El que cambia todo siempre.", "A", "El hilo exige relación con el motivo."),
    ],
    [
        ex("El motivo de ejemplo es «ta ti-ti ta sh». Una variación válida que conserve el estilo es: A) «ta ta ti-ti sh». B) Un silencio de ocho pulsos.", "A", "Mantiene 4 pulsos y cambia el ritmo."),
        ex("Una improvisación tiene motivo (4 pulsos), repetición (4 pulsos), variación (4 pulsos) y contraste (8 pulsos). ¿Cuántos pulsos dura? A) 20. B) 16.", "A", "4 + 4 + 4 + 8 = 20."),
    ],
    [ex("En una ronda de improvisación de tu curso, una estudiante propone usar el nombre de su calle como ritmo hablado. ¿Qué cuidado conviene tener? A) Preferir palabras sin datos personales, por ejemplo un ritmo inventado. B) Usar su dirección completa para que todos la recuerden.", "A", "No se comparten datos personales.")],
    [
        ex("¿Verdadero o falso? Repetir igual un motivo es innovar.", "Falso", "La repetición no propone novedad."),
        ex("¿Qué se mantiene al variar? A) La relación con el motivo. B) El motivo exactamente igual, sin ningún cambio.", "A", "La variación conserva un vínculo."),
        ex("Tocar el motivo con otro instrumento cambia: A) el timbre. B) el compás.", "A", "Otro instrumento cambia el color."),
    ],
    (
        "Crea un motivo de 4 pulsos con «ta», «ti-ti» y «sh». Luego escribe a) una repetición, b) una variación que cambie una cualidad (indica cuál), c) un contraste, d) cuántos sonidos tiene tu motivo.",
        "Motivo: «ta ti-ti ta sh». a) «ta ti-ti ta sh». b) «ta ti-ti ti-ti sh», cambió el ritmo del tercer pulso. c) «sh sh ta ta» o una melodía distinta más lenta. d) 4 sonidos (1 + 2 + 1).",
        ["motivo de exactamente 4 pulsos", "variación con una sola cualidad cambiada", "conteo correcto de sonidos"],
        ["motivo, repetición, variación y contraste escritos"],
        ["variación que no se relaciona con el motivo", "motivo que no suma cuatro pulsos"],
        "Reconoce el motivo y pide indicar qué cualidad cambia la variación.",
    ),
    "Palmea un motivo de 4 pulsos y cámbialo de tres maneras diferentes.",
    "Escribe una improvisación de 16 pulsos con motivo, repetición, variación y contraste.",
)

# ---------------------------------------------------------------- OA 05 · clase 3 (arreglar una canción: partes y recursos)
L(
    OA5, 3,
    "Lápiz y papel. La estructura de las canciones y los arreglos están descritos en los ejercicios (son de ejemplo). Probar los arreglos con instrumentos lo organiza tu docente.",
    "Aprenderé qué es un arreglo, cuáles son las partes de una canción y cómo se cambian los recursos (instrumentos, tempo, textura y dinámica) para dar un carácter nuevo. Sirve para crear mi propia versión de una canción.",
    ["Improviso con acuerdos.", "Varío un motivo.", "Distingo forma y textura."],
    [
        "Un arreglo es una versión de una canción en la que se decide cómo se interpretará: qué voces o instrumentos participan, cuántas veces se repite cada parte, con qué tempo y dinámica y con qué textura. Un arreglo no cambia la canción por completo: mantiene lo que la hace reconocible y modifica lo que la renueva.",
        "Las canciones se organizan en secciones: introducción (comienzo instrumental), estrofa (parte que cambia de texto), estribillo (parte que se repite), puente (sección de contraste) y final o coda. Un arreglo puede alargar una introducción, repetir el estribillo, agregar un puente o cerrar con un final más suave. Cada decisión busca un efecto: más energía, más calma o más emoción.",
        "Para calcular cuánto dura un arreglo se suman los compases de cada sección y se convierten en tiempo con los pulsos. Si cada compás tiene 4 pulsos, se multiplican los compases por 4. Después se divide por los pulsos por minuto para saber los minutos. Por ejemplo, 24 compases de 4 pulsos son 96 pulsos; a 96 pulsos por minuto duran un minuto.",
    ],
    [("arreglo", "versión de una canción con decisiones de interpretación"), ("introducción", "comienzo de la canción, generalmente sin texto"), ("estrofa", "parte que cambia de texto"), ("estribillo", "parte que se repite igual"), ("puente", "sección de contraste"), ("coda", "final de una pieza")],
    [
        ("Calcular una estructura", "Arreglo de ejemplo: introducción de 4 compases, estrofa de 8, estribillo de 8 y final de 4. ¿Cuántos compases tiene en total?", ["Se suman las secciones.", "4 + 8 + 8 + 4 = 24."], "24 compases"),
        ("Elegir una decisión por su efecto", "Se quiere que el final de una canción de ejemplo transmita calma. ¿Qué decisión de arreglo ayuda?", ["La calma se asocia con dinámica suave y tempo lento.", "Un final más lento y suave."], "Cerrar con dinámica suave y tempo más lento"),
    ],
    [
        ("Cambiar tanto la canción que ya no se reconoce.", "Un arreglo debe mantener lo que la hace reconocible.", "Conserva la melodía o el texto y cambia otros recursos."),
        ("Creer que arreglar es solo agregar más instrumentos.", "Más instrumentos no siempre mejoran; a veces conviene quitarlos.", "Decide según el efecto buscado."),
    ],
    [
        ex("¿Qué es un arreglo? A) Una versión de una canción con decisiones de interpretación. B) Una canción nueva sin relación con otra.", "A", "Se basa en una canción existente."),
        ex("¿Qué parte de una canción se repite igual? A) El estribillo. B) La estrofa.", "A", "El estribillo se repite sin cambios."),
        ex("¿Qué parte contrasta con las demás? A) El puente. B) La introducción.", "A", "El puente es de contraste."),
    ],
    [
        ex("¿Qué decisión de arreglo da más energía a un estribillo? A) Sumar voces e instrumentos y subir la dinámica. B) Bajar el tempo y la dinámica.", "A", "Más capas y fuerza dan energía."),
        ex("Un arreglo agrega una introducción de 4 compases a una canción. ¿Qué cambia? A) La forma, porque suma una sección. B) La melodía del estribillo.", "A", "Altera la estructura."),
        ex("¿Qué debe conservar un arreglo? A) Lo que hace reconocible a la canción. B) Solo el título de la canción.", "A", "Si no, ya no sería un arreglo."),
    ],
    [
        arith("Un arreglo de ejemplo tiene 6 compases de introducción, 12 de estrofa, 8 de estribillo, 12 de estrofa, 8 de estribillo y 4 de final. ¿Cuántos compases tiene en total?", "6+12+8+12+8+4", "Se suman todas las secciones.", " compases"),
        arith("Una pieza de ejemplo tiene 30 compases de 4 pulsos y se toca a 60 pulsos por minuto. ¿Cuántos minutos dura?", "30*4//60", "Se multiplica por 4 pulsos y se divide por los pulsos por minuto.", " minutos"),
        ex("Un arreglo repite el estribillo tres veces para terminar con más fuerza. ¿Qué efecto busca? A) Dar énfasis y energía. B) Calmar para dormir.", "A", "La repetición refuerza."),
    ],
    [
        ex("Un grupo propone un arreglo con tempo mucho más lento, dinámica suave y una sola voz con guitarra para una canción que era de baile. ¿Qué efecto cambia? A) Pasa de un carácter para bailar a uno íntimo. B) Se mantiene idéntico.", "A", "Los recursos cambian el carácter."),
        ex("Un arreglo quita el puente porque «no se nota». ¿Qué ocurre con la forma? A) Se pierde el contraste y la pieza se vuelve más lineal. B) Se mantiene igual.", "A", "El puente aporta contraste."),
    ],
    [
        ex("Una estudiante dice: «Mi arreglo es mejor porque tiene más instrumentos.» ¿Qué pregunta es más útil? A) ¿Qué efecto buscabas con esos instrumentos? B) ¿Cuántos instrumentos más podrías sumar?", "A", "El efecto justifica la decisión."),
        ex("Un arreglo de ejemplo tiene 20 compases de 4 pulsos y pasa de 80 a 100 pulsos por minuto. ¿Qué sucede con el tiempo total al acelerar? A) Disminuye. B) Aumenta.", "A", "A más pulsos por minuto, menos tiempo."),
    ],
    [ex("Tu curso arreglará una canción de ejemplo para un acto de despedida. ¿Qué plan está mejor justificado? A) Introducción con una voz, estrofas con guitarra, estribillo con todo el curso y final suave. B) Todo igual a la versión original sin ningún cambio.", "A", "Cada sección tiene una decisión con efecto.")],
    [
        ex("¿Verdadero o falso? Un arreglo puede cambiar el tempo y la dinámica.", "Verdadero", "Son recursos de arreglo."),
        ex("¿Qué es la coda? A) El final de una pieza. B) El comienzo.", "A", "Coda es final."),
        ex("¿Qué decide cuántos compases tendrá un arreglo? A) Las secciones que se incluyan y su duración. B) La cantidad de integrantes del grupo.", "A", "La forma determina el total."),
    ],
    (
        "Planifica un arreglo de ejemplo para una canción conocida (no copies letra): escribe a) las secciones con sus compases, b) el total de compases, c) una decisión de recursos y el efecto que busca.",
        "a) Introducción 4, estrofa 8, estribillo 8, puente 4, estribillo 8, final 4. b) 36 compases. c) Dinámica suave en el puente para dar contraste y luego estribillo con todo el grupo para más energía.",
        ["secciones con compases", "total bien sumado", "una decisión relacionada con un efecto"],
        ["lista de secciones, suma y decisión"],
        ["sumar mal los compases", "decisión sin efecto buscado"],
        "Reconoce la estructura y pide revisar la suma y justificar con un efecto.",
    ),
    "Anota las secciones de una canción que conozcas (introducción, estrofa, estribillo) en el orden en que suenan.",
    "Cambia dos recursos de una canción (tempo y cantidad de voces) y explica el nuevo carácter que logra.",
)

# ---------------------------------------------------------------- OA 05 · clase 4 (crear una sección nueva)
L(
    OA5, 4,
    "Lápiz y papel. Las secciones se crean con palabras, «ta», «ti-ti» y «sh». Interpretarlas con voz o instrumento lo organiza tu docente.",
    "Aprenderé a crear una sección musical nueva (introducción, puente o final) sobre una proposición dada, con un procedimiento de cuatro pasos. Sirve para completar un arreglo con ideas propias y comprobar que encajan.",
    ["Varío un motivo.", "Conozco las secciones de una canción.", "Cuento pulsos y compases."],
    [
        "Crear una sección nueva parte de una proposición dada: una consigna con condiciones, por ejemplo «un puente de 4 compases de 4 pulsos, más suave que el estribillo, con el mismo motivo rítmico variado». Con esa consigna se siguen cuatro pasos: primero, definir la función de la sección (qué efecto debe lograr); segundo, elegir los recursos (voces, ritmo, dinámica); tercero, escribir o anotar la idea; cuarto, probar, escuchar y ajustar.",
        "La sección debe encajar con el resto: respeta el tempo, el compás y el estilo acordados. Una introducción prepara lo que viene; un puente contrasta y renueva el interés; un final cierra y da sensación de término. Para comprobar que la sección cumple, se cuentan sus compases y pulsos y se compara con la consigna.",
        "También se evalúa con criterios audibles: si se entiende el motivo, si el contraste es claro, si la dinámica cambia como se pidió y si la sección dura lo acordado. Cuando algo no funciona se cambia una cualidad a la vez, para saber qué produjo el efecto.",
    ],
    [("proposición dada", "consigna con condiciones para crear"), ("función", "efecto que debe lograr una sección"), ("encajar", "ser coherente con el tempo, compás y estilo del resto"), ("ajustar", "cambiar algo para mejorar el resultado"), ("sección", "parte de una pieza con una función propia"), ("criterio audible", "pauta que se puede comprobar escuchando")],
    [
        ("Verificar la duración de una sección", "Consigna de ejemplo: un puente de 4 compases de 4 pulsos. La estudiante escribe 3 compases de 4 pulsos. ¿Cumple?", ["Se calcula lo pedido: 4 × 4 = 16 pulsos.", "Lo escrito: 3 × 4 = 12 pulsos."], "No: tiene 12 pulsos y se pedían 16"),
        ("Elegir la función de una sección", "Se necesita una sección que prepare la entrada de las voces en una pieza de ejemplo. ¿Qué sección conviene?", ["Prepara lo que viene.", "Eso hace una introducción."], "Una introducción"),
    ],
    [
        ("Empezar a escribir sin definir la función de la sección.", "Sin función clara, no se sabe qué efecto lograr ni qué recursos elegir.", "Define primero qué debe hacer la sección."),
        ("Cambiar varias cosas a la vez al ajustar.", "No se sabe cuál cambio mejoró o empeoró.", "Cambia una cualidad por vez y vuelve a escuchar."),
    ],
    [
        ex("¿Cuál es el primer paso para crear una sección? A) Definir su función. B) Probarla frente al curso.", "A", "Se parte por el propósito."),
        ex("¿Qué es una proposición dada? A) Una consigna con condiciones para crear. B) Un instrumento musical.", "A", "Son las condiciones del trabajo."),
        ex("¿Qué sección contrasta con el estribillo? A) El puente. B) La introducción.", "A", "El puente contrasta."),
    ],
    [
        ex("¿Qué significa «encajar» una sección nueva? A) Ser coherente con el tempo, el compás y el estilo del resto. B) Ser más larga que las demás.", "A", "La coherencia es la condición."),
        ex("Una sección se probó y no logró el contraste pedido. ¿Qué haces? A) Cambiar una cualidad y escuchar de nuevo. B) Cambiar todo a la vez.", "A", "Se ajusta paso a paso."),
        ex("¿Qué sección da sensación de término? A) El final. B) La introducción.", "A", "Cierra la pieza."),
    ],
    [
        arith("Consigna de ejemplo: un final de 6 compases de 3 pulsos. ¿Cuántos pulsos debe tener?", "6*3", "Se multiplican compases por pulsos.", " pulsos"),
        ex("La consigna pide una introducción de 2 compases de 4 pulsos con «ta ta ta sh» en cada compás. La estudiante entrega «ta ta ta sh / ta ta ta ta». ¿Cumple? A) No: el segundo compás no tiene el silencio pedido. B) Sí.", "A", "El segundo compás cambia el patrón pedido."),
        ex("Una sección dura 4 compases de 4 pulsos y se toca a 80 pulsos por minuto. ¿Cuántos segundos dura? A) 12. B) 16.", "A", "16 pulsos × 60 ÷ 80 = 12 segundos."),
    ],
    [
        ex("Una estudiante quiere un puente más suave y baja la dinámica, pero también cambia el tempo y el motivo. Después no sabe qué mejoró. ¿Qué error cometió? A) Cambió varias cualidades a la vez. B) Bajó la dinámica.", "A", "No pudo aislar el efecto de cada cambio."),
        ex("Un puente de ejemplo mantiene el motivo del estribillo pero más lento y suave. ¿Qué relaciona con el estribillo? A) El motivo, que se reconoce. B) El tempo, que es idéntico.", "A", "Mantiene el motivo."),
    ],
    [
        ex("La consigna pide un puente de 8 compases de 4 pulsos. Una persona entrega 6 compases de 4 y 2 compases de 3. ¿Cuántos pulsos le faltan para cumplir? A) 2. B) 0.", "A", "Se pedían 32; entregó 6 × 4 + 2 × 3 = 30."),
        ex("Un grupo prueba su sección con instrumentos y el volumen es muy alto en una sala pequeña. ¿Qué decisión conviene? A) Bajar el volumen para proteger el oído. B) Subirlo para sentir el efecto.", "A", "El volumen seguro protege el oído."),
    ],
    [ex("Tu grupo debe crear un final de 4 compases de 4 pulsos para una canción alegre de ejemplo. ¿Qué propuesta cumple mejor? A) Repetir el motivo cada vez más lento y terminar con un silencio. B) Cambiar a un estilo muy distinto sin relación.", "A", "Cierra, mantiene el motivo y respeta la duración.")],
    [
        ex("¿Verdadero o falso? Al ajustar conviene cambiar una cualidad a la vez.", "Verdadero", "Así se identifica el efecto."),
        ex("¿Qué sección prepara lo que viene? A) La introducción. B) El final.", "A", "Es su función."),
        ex("¿Qué se compara con la consigna al verificar? A) Los compases y pulsos. B) El nombre del grupo.", "A", "La duración es una condición."),
    ],
    (
        "Consigna de ejemplo: crear un puente de 4 compases de 4 pulsos, más suave que el estribillo, con el motivo «ta ti-ti ta sh» variado. Escribe a) la función del puente, b) los 4 compases con «ta», «ti-ti» y «sh» (cada uno de 4 pulsos), c) la dinámica que usarás, d) la verificación: cuántos pulsos tiene en total.",
        "a) Dar contraste y calma antes del último estribillo. b) «ta ti-ti ta sh / ta ti-ti ti-ti sh / ta ta ta sh / ta sh sh sh». c) Suave. d) 4 compases × 4 pulsos = 16 pulsos.",
        ["función definida", "cuatro compases de exactamente 4 pulsos", "verificación correcta de los pulsos"],
        ["a), b), c) y d) escritos"],
        ["compases que no suman 4 pulsos", "no relacionar con el motivo"],
        "Reconoce los compases y pide contar los pulsos de cada compás.",
    ),
    "Cuenta dos veces los pulsos de cada compás que escribiste y marca si alguno no suma cuatro.",
    "Crea una introducción de 2 compases de 4 pulsos que prepare el puente que escribiste.",
)

# ---------------------------------------------------------------- OA 05 · clase 5 (registrar y contrastar versiones de un arreglo)
L(
    OA5, 5,
    "Lápiz y papel. Las versiones del arreglo están descritas en los ejercicios. La grabación y la audición de las versiones las organiza tu docente.",
    "Aprenderé a llevar una bitácora de versiones de un arreglo y a contrastarlas con criterios. Sirve para decidir con evidencia qué cambios conservar y mejorar la innovación.",
    ["Creo secciones nuevas.", "Registro interpretaciones.", "Contrasto con criterios."],
    [
        "Una bitácora de versiones es un registro ordenado de cada intento de un arreglo. Para cada versión se anota: número de versión, qué se cambió, cómo suena el resultado y si se conserva o se descarta. Con ella se evita repetir ensayos y se puede volver a una versión anterior si la nueva no mejora.",
        "Para contrastar dos versiones se usan los mismos criterios: reconocimiento de la canción, claridad de las secciones, equilibrio entre repetición y novedad, coherencia con el estilo acordado y efecto logrado. Se compara qué cambió y qué se mantuvo. Una versión no es mejor por ser más larga, más rápida o más fuerte, sino por lograr el efecto buscado con coherencia.",
        "Registrar también significa dejar constancia de la autoría de las ideas: quién propuso cada cambio, para reconocer los aportes del grupo. Si la canción original es de otra persona, se anota su autoría y se aclara que el arreglo es una versión. Al final se decide qué versión se presentará y se explica por qué con evidencia de la bitácora.",
    ],
    [("bitácora", "registro ordenado de lo realizado"), ("versión", "estado del arreglo después de un cambio"), ("conservar", "mantener un cambio que mejoró"), ("descartar", "dejar un cambio que no mejoró"), ("coherencia", "relación lógica entre las decisiones y el estilo acordado"), ("aporte", "idea o trabajo que alguien suma")],
    [
        ("Leer una bitácora", "Bitácora de ejemplo. V1: base. V2: estribillo repetido tres veces, se alarga y se vuelve monótono: se descarta. V3: estribillo repetido dos veces con un puente: se conserva. ¿Cuál es la versión que se conserva?", ["V2 se descartó.", "V3 se conservó."], "La versión 3"),
        ("Contrastar con criterios", "Versión A de ejemplo: se reconoce la canción, hay un puente claro y el final es suave. Versión B de ejemplo: se reconoce la canción, pero el puente suena igual al estribillo. Para un criterio de «claridad de las secciones», ¿cuál es mejor?", ["Se compara el mismo criterio.", "A tiene un puente claro; B no."], "La versión A"),
    ],
    [
        ("Elegir la versión por ser la más reciente.", "Lo nuevo no siempre mejora.", "Decide con la bitácora y los criterios."),
        ("No anotar lo que se cambió.", "Después no se sabe qué produjo el efecto.", "Anota cada cambio y su resultado."),
    ],
    [
        ex("¿Qué se anota en una bitácora? A) Qué se cambió y cómo suena. B) Solo la fecha.", "A", "Esos datos permiten comparar."),
        ex("¿Para qué sirve la bitácora? A) Para volver a una versión anterior si hace falta. B) Para evitar tener que escuchar las versiones.", "A", "Conserva el historial."),
        ex("¿Qué es una versión? A) El estado del arreglo después de un cambio. B) Un tipo de instrumento.", "A", "Es el resultado de cada intento."),
    ],
    [
        ex("¿Qué se mantiene al contrastar dos versiones? A) Los mismos criterios para ambas. B) Un criterio distinto para cada una.", "A", "Así se compara con justicia."),
        ex("Una versión es más larga pero pierde el estilo acordado. ¿Es mejor por ser más larga? A) No: lo importante es el efecto y la coherencia. B) Sí.", "A", "La extensión no mide calidad."),
        ex("¿Por qué anotar quién propuso cada cambio? A) Para reconocer los aportes del grupo. B) Para culpar a alguien.", "A", "Se reconoce el trabajo colectivo."),
    ],
    [
        ex("Bitácora de ejemplo: V1 (base), V2 (se agrega una introducción: mejora), V3 (se sube el tempo: pierde claridad), V4 (V2 más un final suave: mejora). ¿Qué versión conviene presentar? A) V4. B) V3.", "A", "V4 conserva las mejoras y evita lo que empeoró."),
        arith("Un arreglo de ejemplo tenía 24 compases en V1. En V2 se agregan 4 compases de introducción y en V3 se agregan 8 de puente. ¿Cuántos compases tiene V3?", "24+4+8", "Se suman los compases agregados.", " compases"),
        ex("Una versión mantiene el estribillo igual y cambia el tempo, la dinámica y las voces. ¿Qué dice la bitácora de lo que se mantuvo? A) El estribillo. B) El tempo.", "A", "Es lo que permanece."),
    ],
    [
        ex("Un grupo descarta la V3 sin anotar por qué. ¿Qué problema tendrá? A) No recordará qué cambio no funcionó y podría repetirlo. B) Ninguno.", "A", "La bitácora previene repeticiones."),
        ex("Una persona propone presentar la versión con más instrumentos «porque es la más impresionante». ¿Qué respuesta es adecuada? A) Revisar con los criterios si logra el efecto buscado. B) Aceptar sin más.", "A", "Se decide con criterios."),
    ],
    [
        ex("Tu arreglo pasó de 32 compases a 40 compases al agregar un puente. Se toca a 80 pulsos por minuto en compases de 4 pulsos. ¿Cuántos pulsos se añadieron? A) 32. B) 8.", "A", "Se añadieron 8 compases × 4 pulsos = 32 pulsos."),
        ex("En el grupo hay desacuerdo sobre qué versión presentar. ¿Qué proceso es respetuoso? A) Escuchar ambas, aplicar los mismos criterios y decidir con la bitácora. B) Imponer la opinión de quien dirige.", "A", "Se decide con evidencia y escucha."),
    ],
    [ex("Para la muestra de música de tu colegio, tu curso tiene tres versiones de un arreglo. ¿Qué haces primero? A) Revisar la bitácora y comparar con los mismos criterios. B) Elegir al azar.", "A", "La bitácora y los criterios ordenan la decisión.")],
    [
        ex("¿Verdadero o falso? Una versión es mejor si es más rápida.", "Falso", "El efecto y la coherencia importan más."),
        ex("¿Qué se anota sobre la canción original si es de otra persona? A) Su autoría y que el arreglo es una versión. B) Nada.", "A", "Se reconoce la autoría."),
        ex("¿Qué significa conservar un cambio? A) Mantenerlo porque mejoró. B) Dejarlo sin usar para siempre.", "A", "Se mantiene lo que funciona."),
    ],
    (
        "Escribe una bitácora de ejemplo de 3 versiones de un arreglo (V1 base, V2 y V3): para cada una anota el cambio, cómo suena y si se conserva o se descarta. Cierra con la versión que presentarías y dos criterios que apoyan tu decisión.",
        "V1: base, se reconoce la canción. V2: se agrega una introducción de 4 compases, entra suave: se conserva. V3: se sube el tempo, pierde claridad: se descarta. Presento V2 porque conserva el estilo y tiene las secciones más claras.",
        ["tres versiones con cambio, resultado y decisión", "decisión final coherente con la bitácora", "dos criterios que apoyan la elección"],
        ["bitácora de tres versiones y decisión"],
        ["no anotar el resultado", "elegir sin criterios"],
        "Reconoce la bitácora y pide agregar un criterio más para justificar la decisión.",
    ),
    "Anota en tres líneas los cambios que hiciste a un arreglo y si los conservarías.",
    "Contrasta tu versión con la de otra persona del curso usando tres criterios iguales.",
)
