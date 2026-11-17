"""Creación y composición musical 3.º y 4.º medio HC: OAC-01 (innovar al resolver desafíos creativos: repetición, variación, contraste y evaluación crítica). Motivos, ritmos y piezas inventados, descritos en texto."""
from __future__ import annotations

from hc_ccmu_common import CLAVE, build

O1 = "AR-CCMU-3y4-OAC-01"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (desafío y pieza de ejemplo, inventados). Desafío: componer una pieza de 4 compases para la radio de un liceo ficticio. "
     "Propósito: una idea tranquila que se repite y que cambia de carácter al final. Público: estudiantes del liceo. "
     "Restricciones: 48 pulsos por minuto, máximo 20 segundos, dos instrumentos. "
     "Pieza de Ana (suave, salvo el compás 4, que suena fuerte): c1 | Do Re Mi Re |; c2 | Do Re Mi Re |; c3 | Do Re Mi Sol |; c4 | La - Sol - |. " + CLAVE)
build(
    O1, 1, F,
    use="Aprenderé a leer un desafío compositivo (propósito, público, restricciones) y a reconocer repetición, variación y contraste en una pieza breve, para decidir cuánto repetir y cuánto cambiar.",
    prior=["Sé leer una cuadrícula de pulsos y los nombres de las notas.", "Reconozco dinámica suave y fuerte.", "Sé describir lo que oigo antes de opinar."],
    explain=[
        "Innovar al resolver un desafío compositivo es dar una solución propia a un encargo musical con un propósito. Antes de componer se subrayan tres datos: el propósito (qué debe transmitir la pieza), el público (quién la va a oír) y las restricciones (duración, tempo, instrumentos). Con esos datos se toman decisiones expresivas (qué se quiere decir) y técnicas (cómo se logra con el instrumento y el tiempo disponibles).",
        "Los procedimientos compositivos son maneras de organizar las ideas musicales. La repetición presenta una idea igual en notas, ritmo y dinámica. La variación vuelve a presentar la idea cambiando algún rasgo (una nota, el ritmo, la dinámica) y conservando otros, de modo que se la reconoce. El contraste presenta una idea claramente distinta, que cambia varios rasgos a la vez.",
        "Una pieza interesante equilibra los tres: si solo repite, se vuelve monótona; si solo cambia, el oyente no reconoce nada. Para hablar de una pieza se compara compás con compás y se rotula con letras: A para la idea inicial, A' para su variación y B para un contraste. Todo se puede hacer con lápiz, papel y una cuadrícula de pulsos.",
    ],
    vocab=[("desafío compositivo", "encargo musical con propósito, público y restricciones"), ("procedimiento compositivo", "manera de organizar o transformar ideas musicales"),
           ("repetición", "volver a presentar una idea exactamente igual"), ("variación", "presentar una idea cambiando algún rasgo y conservando otros"),
           ("contraste", "presentar una idea claramente distinta"), ("compás", "grupo de pulsos entre dos barras; aquí, de 4 pulsos")],
    worked=[
        ("Rotular una frase", "Una frase de ejemplo tiene cuatro compases: | Sol Mi Sol Mi | Sol Mi Sol Mi | Sol Mi Sol La | Re - Do - |. Rotula su forma con A, A' y B.",
         ["Los compases 1 y 2 son idénticos: el segundo repite al primero, así que son A y A.", "El compás 3 conserva tres notas y cambia la última (Mi por La): es variación, A'. El compás 4 usa notas largas y otra dirección: es contraste, B."],
         "A A A' B"),
        ("Leer un desafío", "Un programa ficticio de deportes pide una cortina musical de 8 segundos a 120 pulsos por minuto, con una idea alegre. ¿Cuántos pulsos y cuántos compases de 4 pulsos caben?",
         ["A 120 pulsos por minuto hay 2 pulsos por segundo, así que en 8 segundos caben 8 × 2 = 16 pulsos.", "Como cada compás tiene 4 pulsos, 16 ÷ 4 = 4 compases."],
         "16 pulsos, es decir, 4 compases"),
    ],
    mistakes=[("Llamar contraste a cualquier cambio, aunque conserve casi toda la idea.", "No se mide cuántos rasgos cambian: un cambio pequeño es variación.", "Cuenta qué se conserva y qué cambia: si se reconoce la misma idea, es variación; si suena como otra idea, es contraste."),
              ("Creer que innovar es no repetir nada.", "Se confunde novedad con cambio constante.", "Innovar es decidir cuánto repetir, variar y contrastar según el propósito.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un procedimiento compositivo?', 'Una manera de organizar o transformar ideas musicales, como repetir, variar o contrastar', 'Un instrumento o recurso técnico que se necesita para poder tocar la pieza ya terminada', 'La calificación que se asigna a una pieza al evaluarla según una pauta del curso', 'Los procedimientos son formas de trabajar las ideas musicales; no son instrumentos ni notas de evaluación.'),
        ('abc', '{F} ¿Qué relación hay entre el compás 1 y el compás 2 de la pieza de Ana?', 'Repetición: tienen las mismas notas, el mismo ritmo y la misma dinámica', 'Variación: se reconoce la misma idea, pero cambia la última nota del compás', 'Contraste: el ritmo y las notas de un compás son muy distintos de los del otro', 'Ambos compases dicen Do Re Mi Re y suenan suaves; por eso el segundo repite exactamente al primero.'),
        ('abc', '{F} ¿Qué cambia entre el compás 1 y el compás 3?', 'Solo la última nota: Re pasa a ser Sol', 'Cambian las cuatro notas', 'Cambia el ritmo, pero las notas son las mismas', 'Do Re Mi se mantienen y solo la cuarta nota cambia de Re a Sol; el ritmo es el mismo.'),
        ('abc', '{F} ¿Qué compás presenta contraste con el compás 1?', 'El compás 4, porque usa notas largas de dos pulsos y suena fuerte', 'El compás 2, porque viene después del compás 1 y suena a continuación', 'El compás 3, porque tiene una nota distinta, aunque conserva las otras tres', 'El compás 4 cambia ritmo, dirección y dinámica a la vez; el 3 cambia solo una nota.'),
        ('=', '{F} La pieza de Ana tiene 4 compases de 4 pulsos y va a 48 pulsos por minuto. ¿Cuántos segundos dura?', '4*4*60//48', 'Se multiplican los pulsos por 60 y se divide por los pulsos por minuto para obtener los segundos.', ' s'),
        ('abc', '¿Por qué se subraya el propósito antes de componer?', 'Para decidir cuánto repetir, variar o contrastar según lo que la pieza debe transmitir', 'Para que la pieza dure más tiempo del que permiten las restricciones del desafío', 'Para poder ignorar las restricciones de duración y de instrumentos al componer', 'El propósito orienta las decisiones expresivas; no cambia la duración ni elimina las restricciones.'),
        ('{F} Rotula la forma de la pieza de Ana compás a compás con A, A\' y B, de c1 a c4.', 'A A A\' B', 'Los compases 1 y 2 son iguales (A), el 3 varía una nota (A\') y el 4 contrasta (B).'),
        ('abc', 'Ana agrega un quinto compás idéntico al compás 1. ¿Qué procedimiento usa en ese compás?', 'Repetición de la idea inicial', 'Contraste con la idea inicial', 'Variación de la altura de todas las notas', 'Si el compás es idéntico al primero en notas, ritmo y dinámica, es repetición.'),
        ('=', '{F} Ana pensó añadir un quinto compás de 4 pulsos. ¿Cuántos segundos se pasaría del máximo de 20 segundos?', '5*4*60//48-20', 'Cinco compases de 4 pulsos a 48 pulsos por minuto duran más que el máximo permitido por la restricción.', ' s'),
        ('abc', '{F} Un compañero dice: «El compás 3 es un contraste, porque no es igual al compás 2». ¿Qué respuesta es correcta?', 'Es una variación, porque conserva tres notas y cambia solo una', 'Tiene razón, porque todo lo que no es igual es contraste', 'Es una repetición, porque tiene el mismo ritmo', 'Un contraste cambia varios rasgos; aquí se reconoce la misma idea con una nota distinta, o sea, variación.'),
        ('abc', '{F} ¿Qué decisión responde mejor al propósito «idea tranquila que cambia de carácter al final»?', 'Repetir y variar suavemente al comienzo y reservar el contraste fuerte para el compás 4', 'Poner el contraste fuerte en el compás 1 y repetirlo en los demás', 'Repetir el compás 1 en los cuatro compases sin ningún cambio', 'El carácter cambia solo al final si el contraste aparece al final; las otras opciones no lo logran.'),
        ('abc', '{F} Un compañero propone tocar el compás 2 con las mismas notas, pero fuerte. ¿Qué relación tendrían entonces el compás 1 y el 2?', 'Una variación de dinámica, porque cambia un rasgo y se conservan notas y ritmo', 'Una repetición exacta, porque las notas siguen siendo las mismas', 'Un contraste total, porque se oye más volumen', 'La repetición exige igualar también la dinámica; si solo cambia un rasgo, es variación.'),
        ('abc', 'Marta dice «innovar es cambiar todo». Pablo dice «innovar es decidir cuánto repetir, variar y contrastar para cumplir el propósito». ¿Quién describe mejor lo aprendido en esta clase?', 'Pablo, porque las decisiones se toman con el propósito', 'Marta, porque lo nuevo es lo que no se parece a nada', 'Ninguno, porque los procedimientos no sirven para innovar', 'Innovar no es cambiar sin criterio: se equilibra repetición, variación y contraste según el propósito.'),
    ],
    ctx=('=', 'Tu curso debe componer un aviso sonoro para el fin del recreo, de máximo 12 segundos a 60 pulsos por minuto. ¿Cuántos compases de 4 pulsos caben?', '12*60//60//4', 'A 60 pulsos por minuto hay un pulso por segundo; los pulsos disponibles se dividen en compases de 4.', ' compases'),
    sc=[
        ("En Composición musical: ¿qué es la variación?", "Presentar de nuevo una idea cambiando algún rasgo y conservando otros", "La variación se reconoce porque la idea sigue siendo la misma con algún cambio."),
        ('abc', 'Un compás vuelve idéntico en notas, ritmo y dinámica. Es una:', 'Repetición', 'Variación', 'Contraste', 'Si nada cambia, se trata de repetición.'),
        ("¿Para qué sirve conocer las restricciones de un desafío compositivo?", "Para que la pieza sea posible en duración, tempo e instrumentos", "Las restricciones son límites que la solución debe respetar."),
    ],
    op=("Con la {F}, escribe en una frase el propósito del desafío. Luego propón cambiar un solo compás de la pieza de Ana y di si queda como repetición, variación o contraste, y por qué sirve al propósito.",
        "Propósito: una idea tranquila que cambia al final. Cambio el compás 2 a | Do Re Mi Mi |: es una variación, porque solo cambia la última nota y se reconoce la idea. Sirve al propósito porque sigue tranquilo y el contraste fuerte queda para el compás 4.",
        ["escribe el propósito con sus palabras", "propone un cambio concreto con notas", "rotula el cambio con el procedimiento correcto", "justifica con el propósito"],
        ["hoja con el propósito, el compás nuevo escrito y su rótulo"],
        ["llamar contraste a un cambio de una sola nota", "no justificar con el propósito", "cambiar más de un compás"],
        "Pregunta: «¿qué conservaste y qué cambiaste?». Si no distingue ambas cosas, pídele que cuente las notas que siguen iguales."),
    reinforce="Escribe en una cuadrícula un motivo de cuatro pulsos con notas de Do mayor. Luego escribe una repetición y una variación de un solo cambio.",
    extend="Explica con un ejemplo inventado por qué una pieza que solo repite y una pieza que solo cambia pueden resultar poco interesantes.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (registro de pruebas de ejemplo, inventado). Motivo M, para flauta dulce a 80 pulsos por minuto: | Mi Mi Fa Sol |. "
     "Desafío: el motivo debe sonar en una sola flauta, sin sumar otros instrumentos. "
     "Prueba 1 (timbre): tocar M con un xilófono en lugar de la flauta; efecto: más brillante y seco. "
     "Prueba 2 (dinámica): tocar M fuerte en lugar de suave; efecto: más energía. "
     "Prueba 3 (registro): tocar M una octava más grave (las mismas notas, más abajo); efecto: más oscuro y calmo. "
     "Prueba 4 (duración): duplicar todas las duraciones, | Mi - Mi - | Fa - Sol - |, que ocupa 8 pulsos; efecto: más solemne. " + CLAVE)
build(
    O1, 2, F,
    use="Aprenderé a explorar recursos para variar y contrastar una idea musical (altura, ritmo, dinámica, timbre, registro) con pruebas pequeñas y a registrarlas para decidir con evidencia.",
    prior=["Reconozco repetición, variación y contraste.", "Sé leer una cuadrícula de pulsos.", "Sé que el sonido tiene altura, duración, intensidad y timbre."],
    explain=[
        "Un parámetro del sonido es una característica que se puede cambiar: la altura (qué tan agudo o grave), la duración (cuánto dura), la intensidad o dinámica (qué tan fuerte o suave) y el timbre (el color del sonido, que distingue una flauta de un xilófono). El registro es la zona grave o aguda donde suena una melodía. Variar una idea es cambiar uno o más parámetros y conservar el resto.",
        "Explorar es probar en pequeño antes de decidir. Para saber qué produjo un efecto, se cambia un solo parámetro por prueba y se deja todo lo demás igual. Cada prueba se registra con cuatro datos: qué parámetro cambió, qué se conservó, el tiempo que tomó y el efecto que se oyó. Un registro útil dice «prueba 2: dinámica, fuerte, más energía»; uno inútil dice «se oyó bonito».",
        "Los recursos también tienen límites: el instrumento disponible, la cantidad de integrantes, el tiempo de la sesión y el cuidado del oído. Se trabaja a volumen moderado y con pausas. Una restricción del desafío puede descartar una prueba, por ejemplo la que necesita un instrumento que no hay. Todas las pruebas de este cuaderno se imaginan o se hacen con lápiz y voz, sin necesidad de software.",
    ],
    vocab=[("parámetro", "característica del sonido que se puede cambiar"), ("timbre", "color del sonido que distingue un instrumento de otro"), ("dinámica", "grado de fuerza o suavidad del sonido"),
           ("registro", "zona grave o aguda en que suena una melodía"), ("octava", "distancia entre una nota y la siguiente que tiene el mismo nombre, más aguda o más grave"), ("prueba", "intento pequeño para ver el efecto de un cambio")],
    worked=[
        ("Reconocer el parámetro", "Un grupo toca la melodía | Do Re Mi Re | y luego la toca con las mismas notas, pero con un tambor suave en vez de una guitarra. ¿Qué parámetro cambió?",
         ["Las notas y el ritmo se mantienen: no cambió ni la altura ni la duración.", "Cambió el instrumento, que es lo que da el color del sonido: cambió el timbre."],
         "El timbre"),
        ("Registrar una prueba", "Una estudiante canta | Sol La Sol Mi | despacio y luego más rápido, y dice «la segunda se oye mejor». Escribe un registro útil de la prueba.",
         ["Primero se anota qué cambió: el tempo (la velocidad); notas, ritmo y dinámica se conservan.", "Luego se anota un efecto que otra persona pueda comprobar, como «más rápido: suena más alegre y ligero»."],
         "Prueba: tempo más rápido; se conservan notas y dinámica; efecto: más alegre y ligero"),
    ],
    mistakes=[("Cambiar timbre, dinámica y registro a la vez y concluir qué cambio gustó.", "Con varios cambios juntos no se sabe cuál produjo el efecto.", "Cambia un solo parámetro por prueba y registra cada una."),
              ("Registrar «se oyó bonito» o «me gustó».", "No describe qué cambió ni qué efecto se oye.", "Anota el parámetro, lo que se conserva y un efecto que otra persona pueda oír.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un parámetro del sonido?', 'Una característica que se puede cambiar, como la altura, la duración, la intensidad o el timbre', 'Una nota concreta que se escribe en la cuadrícula de pulsos para formar un motivo', 'La cantidad de personas y de instrumentos que participan en la interpretación de una pieza', 'Los parámetros son características del sonido sobre las que se decide al componer.'),
        ('abc', '{F} ¿Qué parámetro cambia la prueba 1?', 'El timbre, porque se cambia la flauta por un xilófono', 'La duración, porque el xilófono suena más seco', 'La altura, porque el xilófono es más agudo', 'Las notas y los pulsos son los mismos; cambia solo el instrumento, es decir, el timbre.'),
        ('abc', '{F} ¿Qué parámetro cambia la prueba 2?', 'La dinámica, porque se toca fuerte en vez de suave', 'El registro, porque se toca más abajo', 'La duración, porque se toca más tiempo', 'Tocar fuerte o suave cambia la intensidad del sonido, o sea la dinámica.'),
        ('=', '{F} ¿Cuántos segundos dura la prueba 4 a 80 pulsos por minuto, si ocupa 8 pulsos?', '8*60//80', 'Los segundos se obtienen multiplicando los pulsos por 60 y dividiendo por los pulsos por minuto.', ' s'),
        ('abc', '¿Por qué se cambia un solo parámetro por prueba?', 'Para saber qué cambio produjo el efecto que se oye', 'Para que la prueba dure menos que las demás', 'Para evitar tener que registrar nada', 'Si cambian varios parámetros juntos, no se puede saber cuál causó el efecto.'),
        ('abc', '{F} ¿Qué se conserva en la prueba 3?', 'Las notas y el ritmo; cambia el registro, que pasa a ser más grave', 'Solo el timbre; cambian las notas, el ritmo y el registro de la melodía', 'Nada, porque tocar más grave cambia por completo la idea y la vuelve otra melodía', 'La prueba mueve las mismas notas a una zona más grave sin cambiar su orden ni su duración.'),
        ('abc', '{F} Se busca que el motivo suene más enérgico sin cambiar las notas, el ritmo ni el instrumento. ¿Qué prueba corresponde?', 'La prueba 2, cuyo efecto registrado es más energía', 'La prueba 3, cuyo efecto registrado es más oscuro y calmo', 'La prueba 4, cuyo efecto registrado es más solemne', 'Solo la prueba 2 se registró con efecto de más energía y conserva notas, ritmo e instrumento.'),
        ('=', 'Un grupo hace 5 pruebas de 6 minutos cada una y dedica 4 minutos en total a registrar. ¿Cuántos minutos dura la sesión de exploración?', '5*6+4', 'Se suman los minutos de las cinco pruebas y los minutos de registro.', ' minutos'),
        ('abc', 'Un grupo cambia el motivo | Mi Mi Fa Sol | por | Sol Sol La Si |, todas las notas dos pasos más arriba en la escala, con el mismo ritmo. ¿Qué parámetro cambia?', 'La altura, porque cada nota sube dos pasos', 'El timbre, porque cambia el color', 'La duración, porque sube la cantidad de notas', 'Las notas son más agudas y el ritmo sigue igual: cambió la altura.'),
        ('abc', '{F} Un grupo cambia a la vez el timbre, la dinámica y el registro, y concluye que «el timbre fue lo que más gustó». ¿Qué falla en esa conclusión?', 'No se puede saber cuál de los tres cambios produjo el efecto', 'El timbre nunca puede gustar más que la dinámica', 'Se debería haber probado solo la prueba 4', 'Al cambiar varios parámetros juntos, el efecto no puede atribuirse a uno solo.'),
        ('abc', 'Dos registros de la misma prueba: (1) «se oyó bonito»; (2) «prueba 2: dinámica fuerte; se conservan notas y ritmo; efecto: más energía». ¿Cuál sirve más para decidir?', 'El registro 2, porque nombra el cambio, lo conservado y un efecto comprobable', 'El registro 1, porque dice lo que sintió la persona y eso es lo que más importa', 'Ninguno de los dos, porque los registros de pruebas no sirven para decidir nada', 'Un registro útil describe lo que cambió y lo que se oye; la sola opinión no se puede comprobar.'),
        ('abc', '{F} El desafío limita la prueba a una sola flauta. ¿Qué prueba queda descartada por esa restricción?', 'La prueba 1, porque usa un xilófono en lugar de la flauta', 'La prueba 2, porque exige tocar fuerte y esa dinámica no cabe en el desafío', 'La prueba 4, porque exige ocho pulsos y eso excede lo que permite una flauta', 'La restricción habla de instrumentos; solo la prueba 1 usa otro instrumento.'),
        ('abc', 'Para lograr una dinámica fuerte en una sala pequeña con la flauta y el xilófono, ¿qué decisión cuida mejor el oído?', 'Mantener un volumen moderado, hacer pausas y lograr la intensidad con intención y no con ruido excesivo', 'Tocar lo más fuerte posible para estar seguros de que el efecto se escuche en toda la sala', 'Taparse los oídos solo cuando suene fuerte, sin cambiar el volumen ni hacer pausas', 'El cuidado del oído exige volumen moderado y descansos; se puede lograr expresión sin ruido excesivo.'),
    ],
    ctx=('abc', 'Al revisar su registro, un grupo ve que la prueba 4 dura 6 segundos a 80 pulsos por minuto y que el desafío admite 5 segundos. ¿Qué decisión conserva la idea de duplicar las duraciones?', 'Subir el tempo a 96 pulsos por minuto, con lo que los 8 pulsos duran 5 segundos', 'Bajar el tempo a 60 pulsos por minuto para que los 8 pulsos duren menos tiempo', 'Quitar la prueba del registro y no anotar la razón del descarte del resultado', 'A más pulsos por minuto cada pulso dura menos; a 96 pulsos por minuto, 8 pulsos duran 5 segundos.'),
    sc=[
        ("En Composición musical: ¿qué es el timbre?", "El color del sonido que distingue un instrumento de otro", "El timbre es lo que permite distinguir una flauta de un xilófono."),
        ('abc', 'Para explorar, ¿cuántos parámetros conviene cambiar por prueba?', 'Uno', 'Todos a la vez', 'Ninguno', 'Con uno solo se sabe qué cambio produjo el efecto.'),
        ("¿Qué cuatro datos tiene un buen registro de prueba?", "Qué cambió, qué se conservó, el tiempo que tomó y el efecto que se oyó", "Esos datos permiten comparar pruebas y decidir con evidencia."),
    ],
    op=("Con la {F}, elige dos pruebas y escribe para cada una un registro de cuatro datos (qué cambió, qué se conservó, tiempo y efecto). Después decide cuál usarías si el propósito fuera una idea calmada, y explica por qué.",
        "Prueba 3: cambió el registro (más grave); se conservan notas, ritmo y dinámica; 5 minutos; efecto: más oscuro y calmo. Prueba 2: cambió la dinámica (fuerte); se conservan notas y registro; 4 minutos; efecto: más energía. Para una idea calmada elijo la prueba 3, porque su efecto registrado es calmo.",
        ["escribe dos registros con los cuatro datos", "nombra bien el parámetro cambiado", "decide según el propósito", "justifica con el efecto registrado"],
        ["hoja con dos registros y la decisión justificada"],
        ["registrar solo «me gustó»", "olvidar qué se conservó", "elegir sin relacionar con el propósito"],
        "Pregunta: «¿qué dato de tu registro apoya tu decisión?». Si cita solo su gusto, pídele que cite el efecto registrado."),
    reinforce="Con la melodía | Do Mi Sol Mi | escribe tres pruebas: una cambia la dinámica, otra el registro y otra el ritmo. Anota qué parámetro cambió en cada una.",
    extend="Explica por qué dos grupos pueden registrar efectos distintos para el mismo cambio de timbre y cómo lo resolverían.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (plan de ejemplo, inventado). Motivo: | Do Mi Sol Mi |. Propósito: una idea que sube poco a poco y llega a un final tranquilo. "
     "Plan de Nico: c1 | Do Mi Sol Mi |; c2 | Re Fa La Fa |; c3 | Mi Sol Si Sol |; c4 | Do - - . |. "
     "Escala de Do mayor en orden: Do Re Mi Fa Sol La Si. El instrumento del grupo es una flauta dulce que, en este desafío, solo toca de Do a La. " + CLAVE)
build(
    O1, 3, F,
    use="Aprenderé a aplicar procedimientos compositivos (secuencia, retrógrado, variación rítmica, contraste) a un motivo y a decidir cuál sirve al propósito y cabe en el instrumento.",
    prior=["Reconozco repetición, variación y contraste.", "Sé registrar pruebas con un parámetro cambiado.", "Sé la escala de Do mayor en orden."],
    explain=[
        "Una secuencia repite un motivo empezando en otra altura: si el motivo sube un paso en la escala, cada nota se reemplaza por la siguiente de la escala (Do pasa a Re, Mi a Fa, Sol a La). El resultado se reconoce porque conserva el diseño del motivo. Repetir un motivo cada vez más arriba da la sensación de subir poco a poco, y cada vez más abajo, de descender.",
        "El retrógrado lee el motivo al revés, desde la última nota hasta la primera. La variación rítmica conserva las notas y cambia sus duraciones, por ejemplo prolongando una de ellas. La llegada o cierre suele usar notas largas y un silencio, porque transmite reposo. Cada procedimiento produce un efecto distinto, y la decisión se justifica con el propósito.",
        "También hay decisiones técnicas: el instrumento tiene un rango, o sea las notas que puede tocar. Si un procedimiento lleva el motivo fuera de ese rango, se ajusta, por ejemplo acortando la secuencia. Una buena decisión combina tres cosas: sirve al propósito, cabe en el instrumento y se puede registrar y comprobar.",
    ],
    vocab=[("secuencia", "repetición de un motivo empezando en otra altura"), ("retrógrado", "motivo leído de la última nota a la primera"), ("variación rítmica", "cambio de duraciones conservando las notas"),
           ("rango", "notas que un instrumento puede tocar, de la más grave a la más aguda"), ("cierre", "final que transmite reposo"), ("motivo", "idea musical breve que se reconoce")],
    worked=[
        ("Hacer una secuencia", "Aplica una secuencia ascendente de un paso al motivo | Fa Sol Fa Re | en la escala de Do mayor.",
         ["Cada nota se reemplaza por la siguiente de la escala: Fa pasa a Sol, Sol a La, Fa a Sol y Re a Mi.", "El ritmo no cambia, así que se mantiene un pulso por nota."],
         "| Sol La Sol Mi |"),
        ("Hacer un retrógrado", "Escribe el retrógrado del motivo | Sol Fa Mi Do |.",
         ["Se lee la lista desde el final: Do, Mi, Fa, Sol.", "Se escriben en ese orden, con los mismos pulsos."],
         "| Do Mi Fa Sol |"),
    ],
    mistakes=[("Hacer la secuencia moviendo solo la primera nota.", "Se olvida que la secuencia desplaza todo el motivo, no un punto.", "Mueve cada nota el mismo número de pasos en la escala."),
              ("Dar por válido un procedimiento sin revisar el rango del instrumento.", "La idea puede ser buena y aun así no poderse tocar.", "Antes de decidir, comprueba que cada nota esté dentro del rango.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es una secuencia?', 'Repetir un motivo empezando en otra altura, conservando su diseño', 'Repetir el motivo exactamente igual y en la misma altura, sin ningún cambio', 'Tocar el motivo de la última nota a la primera, es decir, de atrás hacia adelante', 'La secuencia mueve el motivo a otra altura; repetir igual es repetición y leerlo al revés es retrógrado.'),
        ('abc', 'En Composición musical: ¿qué es el retrógrado de un motivo?', 'El motivo leído de la última nota a la primera', 'El motivo tocado el doble de rápido', 'El motivo tocado una octava más agudo', 'Retrógrado significa recorrer el motivo hacia atrás, sin cambiar las duraciones de cada nota.'),
        ('abc', '{F} ¿Qué procedimiento une el compás 1 con el compás 2 del plan de Nico?', 'Una secuencia ascendente: cada nota sube un paso de la escala', 'Un retrógrado del compás 1: las mismas notas leídas de atrás hacia adelante', 'Un contraste, porque en el compás 2 se oye una idea completamente distinta', 'Do Mi Sol Mi pasa a Re Fa La Fa: cada nota subió un paso y el diseño se conserva.'),
        ('abc', '{F} ¿Cuántos pasos de la escala sube cada nota del compás 3 respecto del compás 1?', 'Dos pasos, como Do a Mi y Mi a Sol', 'Un paso, como Do a Re y Mi a Fa en cada nota', 'Tres pasos, como Do a Fa y Mi a La en cada nota', 'Do→Re→Mi son dos pasos; Mi→Fa→Sol, también dos; todas las notas suben igual.'),
        ('abc', '{F} ¿Qué compás cumple la función de «final tranquilo» y por qué?', 'El compás 4, porque usa una nota larga y un silencio', 'El compás 2, porque empieza más arriba', 'El compás 3, porque tiene la nota más aguda', 'Una nota larga y un silencio dan sensación de reposo.'),
        ('Escribe el retrógrado del motivo del compás 2 del plan de Nico, | Re Fa La Fa |.', '| Fa La Fa Re |', 'Se lee de atrás hacia adelante: Fa, La, Fa, Re.'),
        ('Aplica una secuencia ascendente de un paso a la melodía | Mi Fa Sol Fa | en la escala de Do mayor.', '| Fa Sol La Sol |', 'Cada nota pasa a la siguiente de la escala: Mi a Fa, Fa a Sol, Sol a La, Fa a Sol.'),
        ('=', '{F} ¿Cuántos segundos dura el plan completo de Nico a 80 pulsos por minuto?', '4*4*60//80', 'Son 4 compases de 4 pulsos; los segundos se calculan con pulsos por 60 sobre los pulsos por minuto.', ' s'),
        ('abc', '{F} Nico duda si en el compás 4 repetir el motivo del compás 1. ¿Por qué eso no sirve al propósito?', 'Porque el propósito pide un final tranquilo y repetir el motivo mantiene el movimiento sin cerrar', 'Porque el motivo del compás 1 no se puede tocar en la flauta dentro del rango Do a La', 'Porque repetir un motivo siempre es un error de composición y debe evitarse', 'El propósito pide llegar a un reposo; el motivo con cuatro sonidos seguidos no da esa sensación.'),
        ('abc', '{F} Marta reemplaza el compás 3 por su retrógrado, | Sol Si Sol Mi |. ¿Qué efecto tiene sobre la idea de subir poco a poco?', 'La debilita, porque el contorno termina bajando y se pierde el parecido de la secuencia', 'La refuerza, porque usa las mismas notas del compás 3 y conserva el efecto de subida', 'No tiene ningún efecto, porque las notas son las mismas aunque cambien de lugar', 'El retrógrado invierte el sentido del motivo y deja de verse la secuencia ascendente.'),
        ('abc', '{F} Un compañero propone seguir la secuencia seis compases seguidos. ¿Qué riesgo hay?', 'Volverse monótona, por lo que conviene cortarla con una variación o un contraste', 'Perder el pulso regular, porque una secuencia larga desordena los compases', 'Dejar de ser una secuencia, porque ya no se reconoce el diseño del motivo', 'Repetir el mismo diseño muchas veces cansa; una variación o un contraste renueva el interés.'),
        ('abc', '{F} Según la restricción de rango, ¿qué compás del plan no se puede tocar en la flauta?', 'El compás 3, porque incluye la nota Si, que está fuera del rango Do a La', 'El compás 2, porque incluye la nota Fa, que está fuera del rango Do a La', 'El compás 4, porque incluye un silencio, que no se puede tocar en la flauta', 'El rango llega hasta La y el compás 3 usa Si; los demás compases caben.'),
        ('abc', '{F} ¿Qué ajuste mantiene la secuencia y respeta el rango de la flauta?', 'Acortar la secuencia a los compases 1 y 2 y pasar luego a la llegada', 'Dejar el Si tal como está y esperar que la flauta pueda alcanzarlo en el ensayo', 'Cambiar el Si por un silencio sin avisar al grupo, porque nadie lo notará', 'Los compases 1 y 2 caben en Do–La; quitar sin avisar o ignorar el rango rompen el plan.'),
    ],
    ctx=('abc', 'Dos integrantes del grupo discrepan: una quiere seguir la secuencia hasta el final y el otro quiere cortarla con un contraste en el compás 3. ¿Qué criterio permite resolverlo mejor?', 'Probar ambas versiones en pequeño y compararlas con el propósito escrito', 'Votar entre las dos versiones sin tocar ninguna, para ahorrar tiempo de ensayo', 'Elegir la versión de quien habla más fuerte, para evitar una discusión larga', 'Las dos opciones se evalúan con evidencia audible y con el propósito, no con el volumen de voz.'),
    sc=[
        ("En Composición musical: ¿qué es una variación rítmica?", "Cambiar las duraciones de las notas conservando las notas", "Se reconoce porque las notas son las mismas y cambia su duración."),
        ('abc', '¿Qué procedimiento lee un motivo de atrás hacia adelante?', 'Retrógrado', 'Secuencia', 'Repetición', 'El retrógrado es el motivo leído al revés.'),
        ("¿Qué se revisa antes de decidir un procedimiento para un instrumento?", "Que todas las notas estén dentro de su rango", "Una idea no sirve si el instrumento no puede tocarla."),
    ],
    op=("Con la {F}, escribe cuatro compases: el motivo | Re Fa Mi Re | y tres secuencias ascendentes de un paso cada una (c2, c3 y c4). Revisa el rango de la flauta (Do a La) y di qué compás no cabe y cómo lo ajustarías.",
        "c1 | Re Fa Mi Re |; c2 | Mi Sol Fa Mi |; c3 | Fa La Sol Fa |; c4 | Sol Si La Sol |. El compás 4 no cabe porque usa Si. Lo ajusto acortando la secuencia: termino en el compás 3 y cierro con | Re - - . |.",
        ["escribe los cuatro compases con las notas correctas", "revisa el rango y detecta el compás fuera de rango", "explica el ajuste"],
        ["hoja con los cuatro compases, la revisión del rango y el ajuste"],
        ["mover solo la primera nota", "no revisar el rango", "no explicar el ajuste"],
        "Pregunta: «¿qué nota quedó fuera del rango y cómo lo resolviste?». Si no puede decirlo, pídele que marque cada nota con su zona."),
    reinforce="Escribe un motivo de cuatro notas con la escala de Do mayor, su retrógrado y una secuencia de un paso hacia arriba.",
    extend="Explica con un ejemplo inventado por qué un procedimiento puede ser buena idea y aun así necesitar un ajuste por el rango del instrumento.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (versiones y comentarios de ejemplo, inventados). Propósito de la pieza «Aviso de recreo»: alegre, breve y con un cierre claro. 120 pulsos por minuto. "
     "Versión 1: c1 | Mi Mi Fa Mi |; c2 | Mi Mi Fa Mi |; c3 | Mi Mi Fa Mi |. "
     "Versión 2: c1 | Mi Mi Fa Mi |; c2 | Mi Mi Fa Sol |; c3 | Do - - . |. "
     "Comentario de Pablo: «Está fome». Comentario de Camila: «En la versión 1, los tres compases son idénticos y se vuelve monótona; podrías variar el compás 2». "
     "Comentario de Rodrigo: «La versión 2 me gusta, pero tú eres malo para las melodías». " + CLAVE)
build(
    O1, 4, F,
    use="Aprenderé a evaluar críticamente mi pieza y la de otras personas con evidencia audible, a dar y recibir retroalimentación respetuosa y a decidir la mejor versión según el propósito.",
    prior=["Reconozco repetición, variación y contraste.", "Sé registrar pruebas.", "Sé que una opinión necesita razones."],
    explain=[
        "La evaluación crítica de una pieza compara lo que se oye con el propósito, usando evidencia audible: qué se repite, qué cambia, qué efecto produce y si cabe en las restricciones. Evaluar no es decir si algo «gusta» o «no gusta»: es explicar cuánto se acerca la pieza a lo que quería comunicar y por qué.",
        "Una retroalimentación útil tiene tres partes: una observación (qué se oye), un efecto (qué produce) y una sugerencia (qué se podría probar). Se habla de la obra y no de la persona: «el compás 3 es igual al 1» es un comentario sobre la obra; «tú eres malo» no es una crítica, es una ofensa. Quien recibe comentarios los compara con su propósito y decide qué incorporar.",
        "Cada versión se rotula (versión 1, versión 2) y se guarda, para saber a cuál se refiere cada comentario y poder volver atrás. En una ronda de comentarios conviene dar tiempo para escuchar, tiempo para comentar y respetar los turnos. Si un comentario no se entiende, se pide un ejemplo audible: el compás o la nota a la que se refiere.",
    ],
    vocab=[("evaluación crítica", "comparar la obra con su propósito usando evidencia audible"), ("evidencia audible", "dato que se puede oír y comprobar en la pieza"), ("retroalimentación", "comentario con observación, efecto y sugerencia"),
           ("versión", "forma de una pieza en un momento del proceso"), ("sugerencia", "cambio que se propone probar"), ("cierre", "final que transmite reposo")],
    worked=[
        ("Reescribir un comentario", "Un compañero escribe «Tu pieza es rara» sobre una pieza de tres compases idénticos | La Do La Do |. Reescríbelo con observación, efecto y sugerencia.",
         ["Observación: los tres compases son idénticos, | La Do La Do |.", "Efecto: suena repetitiva. Sugerencia: variar la última nota del compás 2."],
         "«Los tres compases son idénticos; suena repetitiva; prueba cambiar la última nota del compás 2.»"),
        ("Medir contra el propósito", "El propósito de otra pieza ficticia es «un final tranquilo». Su último compás es | Sol - - . |. ¿Cumple el propósito en ese compás?",
         ["Una nota larga seguida de un silencio transmite reposo.", "El compás tiene esas dos características, así que se acerca al propósito."],
         "Sí, porque usa una nota larga y un silencio"),
    ],
    mistakes=[("Responder a un comentario atacando a quien lo hizo.", "Se confunde la crítica a la obra con una crítica a la persona.", "Pide un ejemplo audible y decide con tu propósito."),
              ("Aceptar todos los comentarios sin compararlos con el propósito.", "Se cambia la pieza hacia direcciones opuestas.", "Contrasta cada sugerencia con tu propósito y elige las que lo ayudan.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es la retroalimentación útil?', 'Un comentario con observación, efecto y sugerencia sobre la obra', 'Un puntaje sin ninguna explicación', 'Una opinión sobre cómo es la persona que compuso', 'La retroalimentación útil describe lo que se oye, qué produce y qué se podría probar.'),
        ('abc', '{F} ¿Qué comentario incluye observación y sugerencia?', 'El de Camila, porque señala que los compases son idénticos y propone variar el compás 2', 'El de Pablo, porque dice «Está fome» y así deja clara su opinión sobre la pieza', 'El de Rodrigo, porque habla de las melodías y dice que la versión 2 le gusta', 'Solo Camila describe lo que se oye y propone qué probar.'),
        ('abc', '{F} ¿Qué comentario ataca a la persona y no a la obra?', 'El de Rodrigo, porque dice «tú eres malo para las melodías»', 'El de Camila, porque dice «se vuelve monótona»', 'Ninguno de los tres', 'Rodrigo habla de la capacidad de la persona; Camila habla de la pieza.'),
        ('abc', '{F} Según Camila, ¿por qué la versión 1 se vuelve monótona?', 'Porque los tres compases son idénticos y no hay variación ni contraste', 'Porque va demasiado rápido y el oído no alcanza a distinguir las notas', 'Porque tiene solo tres compases y eso siempre produce una pieza monótona', 'Camila identifica la repetición completa como causa de la monotonía.'),
        ('=', '{F} La pieza tiene 3 compases de 4 pulsos. ¿Cuántos segundos dura a 120 pulsos por minuto?', '3*4*60//120', 'Los segundos se calculan con pulsos por 60 dividido por los pulsos por minuto.', ' s'),
        ('abc', '{F} ¿Qué cambia en el compás 2 de la versión 2 respecto del compás 1?', 'Solo la última nota, que pasa de Mi a Sol, o sea una variación', 'Las cuatro notas, que pasan a ser distintas, o sea un contraste', 'Nada, porque los dos compases son iguales, o sea una repetición', 'Mi Mi Fa se conservan y la cuarta nota pasa de Mi a Sol.'),
        ('abc', '{F} ¿Cuál es la mejor reescritura del comentario de Pablo para la versión 1?', 'Los tres compases son idénticos y suena repetitiva; prueba cambiar la última nota del compás 2', 'La versión 1 es mala y no tiene arreglo, así que hazla de nuevo desde el principio', 'No me gusta cómo suena la versión 1, pero tú sabrás lo que haces con ella', 'La primera opción nombra lo que se oye, su efecto y una sugerencia concreta.'),
        ('abc', '{F} ¿Qué criterio del propósito cumple la versión 2 con evidencia audible?', 'Un cierre claro, porque el compás 3 usa una nota larga y un silencio', 'Un cierre claro, porque repite tres veces lo mismo', 'Un cierre claro, porque a quien lo escucha le gusta', 'La nota larga con silencio suena a final; la repetición total o el gusto no son evidencia de cierre.'),
        ('=', 'En una ronda de retroalimentación hay 6 piezas y se dedican 4 minutos a cada una, entre escucha y comentarios. ¿Cuántos minutos dura la ronda?', '6*4', 'Se multiplica la cantidad de piezas por los minutos de cada una.', ' minutos'),
        ('abc', 'Una persona recibe un comentario que dice que la pieza repite demasiado y otro que dice que le gusta la repetición. ¿Qué debe hacer?', 'Volver al propósito y decidir con evidencia cuál comentario la ayuda a lograrlo', 'Hacer caso al comentario que dijo la persona más conocida del curso', 'Borrar la pieza y empezar otra sin revisar nada', 'Los comentarios opuestos se resuelven con el propósito y con pruebas audibles, no con popularidad.'),
        ('abc', '¿Por qué conviene rotular cada versión (versión 1, versión 2)?', 'Para saber a qué versión se refiere cada comentario y poder volver atrás', 'Para que la versión 2 siempre sea considerada mejor que la versión 1', 'Para no tener que anotar nada más sobre los cambios que se hicieron', 'El rótulo asocia comentarios y decisiones con una versión concreta.'),
        ('abc', '{F} Alguien dice «la versión 2 es mejor porque tiene más notas distintas». ¿Qué falta en ese comentario?', 'Explicar cómo esa diferencia ayuda al propósito, pues tener más notas no es un criterio por sí solo', 'Nada, porque tener más notas distintas siempre hace que una versión sea mejor que otra', 'Decir cuántos minutos duró cada versión, porque la duración es lo único que se evalúa', 'Un comentario crítico relaciona el dato con el propósito y no usa una cantidad como criterio.'),
        ('abc', 'Una persona recibe un comentario que le parece injusto. ¿Qué hace una evaluación crítica madura?', 'Pide el ejemplo audible al que se refiere, lo compara con su propósito y decide', 'Responde atacando a quien comentó para que no vuelva a opinar de su pieza', 'Ignora todos los comentarios desde ese momento para no perder la confianza en su idea', 'Pedir un ejemplo audible permite comprobar el comentario sin dañar la relación.'),
    ],
    ctx=('abc', 'En una ronda, recibes tres comentarios sobre tu pieza: A «me gustó», B «el compás 3 se parece mucho al compás 1» y C «cambia todo». ¿Cuál priorizas para mejorar y por qué?', 'El B, porque señala un compás y una relación que puedes comprobar al escuchar', 'El A, porque es positivo y anima a seguir componiendo con la misma idea', 'El C, porque pide una decisión drástica que cambia por completo la pieza', 'El B es específico y verificable; A y C no dicen qué oír ni qué efecto producen.'),
    sc=[
        ("En Composición musical: ¿qué es la evidencia audible?", "Un dato que se puede oír y comprobar en la pieza", "La evidencia audible permite que otra persona verifique el comentario."),
        ('abc', 'Una crítica a la obra dice:', 'Los compases 1 y 3 son casi idénticos', 'Tú no sabes componer', 'Esa pieza solo la haría alguien sin talento', 'La crítica a la obra describe lo que se oye en ella, sin juzgar a la persona.'),
        ("¿Cuáles son las tres partes de una retroalimentación útil?", "Observación, efecto y sugerencia", "Así el comentario describe, explica y propone."),
    ],
    op=("Con la {F}, elige la versión que mejor cumple el propósito. Escribe un comentario con observación, efecto y sugerencia sobre la otra versión, sin hablar de la persona.",
        "Elijo la versión 2 porque su compás 3 cierra con una nota larga y un silencio. Sobre la versión 1: los tres compases son idénticos; suena repetitiva y no cierra; prueba variar el compás 2 y terminar con una nota larga.",
        ["elige una versión y la justifica con el propósito", "el comentario tiene observación, efecto y sugerencia", "habla de la obra, no de la persona"],
        ["hoja con la elección y el comentario"],
        ["comentar solo si gusta o no", "criticar a la persona", "no dar una sugerencia concreta"],
        "Pregunta: «¿qué compás señalaste y qué efecto tiene?». Si no cita un compás, pídele que lo marque en la cuadrícula."),
    reinforce="Escribe tres comentarios sobre una pieza inventada de dos compases: uno con observación, uno con efecto y uno con sugerencia.",
    extend="Explica por qué dos personas pueden evaluar distinto la misma pieza y cómo se puede dialogar sin descalificar.",
)
