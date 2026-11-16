"""Teatro 3.º y 4.º medio FG: OAC-05 (evaluación crítica de procesos y obras teatrales), clases 4 y 5. Funciones y críticas originales e inventadas; sin video real."""
from __future__ import annotations

from fg_teat_common import build

O5 = "FG-TEAT-3y4-OAC-05"

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (dos funciones de ejemplo, inventadas). Función 1: una compañía de barrio de una ciudad de Chile, en una sala pequeña, con 3 intérpretes y sin escenografía; cuenta con humor una historia sobre una feria de verduras. "
     "Función 2: una compañía extranjera de ejemplo, en un teatro grande con muchos recursos técnicos y proyecciones; cuenta un drama sobre irse a vivir a otra ciudad.")
build(
    O5, 4, F,
    use="Aprenderé a evaluar obras de artistas nacionales y extranjeros considerando su contexto, sin prejuicios ni comparaciones injustas, y a reconocer desde dónde miro yo.",
    prior=["Sé evaluar con criterios y propósito.", "Sé considerar época, entorno y contexto de una obra.", "Sé evitar estereotipos."],
    explain=[
        "Las obras de artistas nacionales y extranjeras se evalúan con los mismos pasos: describir, interpretar y valorar con criterios y propósito. Lo que cambia es el contexto: los recursos disponibles, el espacio, el público para el que se hizo y la tradición teatral de la que viene. Una compañía de barrio con pocos recursos y un teatro con grandes recursos técnicos no se comparan por el tamaño del presupuesto, sino por cómo cada una logra lo que se propone con lo que tiene.",
        "Para evaluar sin prejuicios conviene averiguar antes sobre el contexto de la obra en fuentes confiables, como el programa, entrevistas o reseñas, y distinguir lo que dice cada fuente de lo que se observa en la función. Ni lo nacional ni lo extranjero es mejor por ese solo hecho. También conviene reconocer la propia perspectiva: se mira desde las costumbres, los gustos y la información que cada persona tiene, y eso influye en lo que se entiende.",
        "Se habla de las obras con respeto hacia las culturas y las personas que las crean, sin burlas ni generalizaciones sobre un país o un pueblo. Las funciones de esta clase son inventadas; si el grupo ve una obra real, el docente indica la fuente y las normas de la sala, y se respeta la autoría.",
    ],
    vocab=[("obra nacional", "obra creada por artistas del propio país"), ("obra extranjera", "obra creada por artistas de otro país"), ("recursos", "medios económicos, técnicos y humanos con que cuenta una compañía"), ("perspectiva", "punto de vista desde el que cada persona mira una obra"), ("fuente", "documento o persona que informa sobre la obra o su contexto"), ("prejuicio", "juicio formado antes de conocer la obra")],
    worked=[
        ("Comparar sin injusticia", "Una compañía con pocos recursos y otra con muchos presentan obras distintas. ¿Cómo se comparan?", ["No se compara el tamaño de los recursos, sino cómo cada obra logra su propósito.", "Se mira qué logró con lo que tenía."], "Se compara el logro del propósito, no el presupuesto"),
        ("Reconocer la propia perspectiva", "Una obra extranjera usa bromas que no entiendes. ¿Qué haces antes de valorarla?", ["Averiguas en una fuente confiable el contexto de esas bromas.", "Reconoces que tu mirada parte de otras costumbres y puedes no entender todo."], "Averiguar el contexto y reconocer tu perspectiva"),
    ],
    mistakes=[("Pensar que una obra extranjera es mejor, o peor, solo por venir de otro país.", "El origen no mide la calidad; hay que mirar la obra.", "Evalúa con criterios y propósito."),
              ("Comparar una obra con grandes recursos con una de pocos recursos por el tamaño del espectáculo.", "Se juzga el presupuesto y no el logro artístico.", "Compara cómo cada una logra su propósito.")],
    T=[
        ('abc', '¿Qué cambia al evaluar una obra extranjera respecto de una nacional?', 'El contexto que se debe averiguar, no los pasos de la evaluación', 'Los pasos de evaluación, que son otros para obras extranjeras', 'La obligación de valorarla mejor que una obra nacional', 'Se usan los mismos pasos; el contexto es lo que conviene conocer mejor.'),
        ('abc', '{F} ¿Qué diferencia de recursos hay entre las dos funciones?', 'La función 1 usa una sala pequeña sin escenografía; la 2, un teatro grande con proyecciones', 'La función 1 usa más proyecciones que la 2', 'Las dos usan exactamente los mismos recursos técnicos y solo cambian el tema y la cantidad de público', 'La ficha describe una sala pequeña sin escenografía y un teatro grande con muchos recursos.'),
        ('abc', '{F} ¿Cómo conviene comparar ambas funciones?', 'Por cómo cada una logra su propósito con los recursos que tiene', 'Por cuál tiene más proyecciones y mayor presupuesto', 'Por cuál proviene del país con más tradición teatral', 'Evaluar el logro del propósito evita juzgar solo el presupuesto.'),
        ('abc', '¿Por qué conviene averiguar el contexto de una obra extranjera?', 'Porque ayuda a entender referencias y costumbres que pueden no ser las propias', 'Porque así se evita tener que mirar la obra con atención', 'Porque el contexto siempre dice de antemano si la obra es buena o mala, sin necesidad de mirarla', 'El contexto aporta información para entender, pero no reemplaza la observación.'),
        ('abc', '¿Qué es una fuente confiable sobre una obra?', 'Un documento o persona que informa con datos verificables, como el programa o una entrevista', 'Un comentario anónimo que repite lo que dijo otra persona sin datos, pero que muchos comparten en línea', 'Una opinión que coincide con lo que ya pensabas', 'La confiabilidad viene de los datos verificables y de su origen.'),
        ('abc', 'Tu primera reacción ante una obra extranjera es «no entendí nada, entonces es mala». ¿Qué haces?', 'Reviso mi perspectiva, averiguo el contexto y vuelvo a mirar los rasgos', 'Confirmo mi reacción y no sigo analizando, porque la primera impresión suele ser la más certera', 'Culpo al país de donde viene por ser distinto', 'No entender puede deberse al contexto; se revisa antes de valorar.'),
        ('=', '{F} La función 1 tiene 3 intérpretes. Una compañía de la función 2 tiene 5 veces la cantidad de intérpretes de la función 1. ¿Cuántos intérpretes tiene?', '3*5', 'Se multiplica la cantidad de la función 1 por el factor dado.', ' intérpretes'),
        ('abc', 'Un grupo dice: «Las obras de ese país son todas iguales». ¿Qué error comete?', 'Generaliza desde pocos casos y cae en un estereotipo', 'Confunde una obra de teatro con una película y analiza sus recursos como si fueran los mismos', 'Olvida el nombre de la compañía', 'Una generalización ignora la variedad de obras y de contextos.'),
        ('abc', 'Dos obras, una nacional y otra extranjera, logran muy bien su propósito. ¿Qué conclusión es razonable?', 'Ambas logran su propósito, cada una con su propio estilo y recursos', 'La nacional es mejor, porque es del propio país', 'La extranjera es mejor, porque trae algo nuevo', 'La evaluación se basa en el logro, no en el origen.'),
        ('abc', '{F} Una espectadora dice sobre la función 1: «Es solo una obrita, no tiene escenografía». ¿Qué falta en esa valoración?', 'Evaluar el logro del propósito con los recursos disponibles y no por su ausencia', 'Una mejor escenografía y más intérpretes en escena para poder valorarla como una obra completa', 'Compararla con la función 2 por el tamaño', 'Una carencia de recursos no define la calidad; se evalúa el logro del propósito.'),
        ('abc', 'Quieres comentar una obra de una cultura que no conoces. ¿Qué actitud es respetuosa?', 'Preguntar y buscar información sin burlarte de lo que no entiendes', 'Dar por supuesto que sabes lo que significan sus costumbres', 'Evitar leer sobre el tema para no influir tu opinión', 'El respeto empieza por averiguar y no asumir.'),
        ('=', 'Un curso ve las dos funciones. Dieron una pauta de 20 puntos máximo a cada una: la función 1 obtuvo 16 y la 2 obtuvo 15. ¿Cuántos puntos tienen entre las dos?', '16+15', 'Se suman los puntos de las dos funciones.', ' puntos'),
        ('abc', 'Un curso quiere comparar las dos funciones solo por sus puntajes de 16 y 15. ¿Qué advertencia es adecuada?', 'Un puntaje cercano no dice por qué cada obra logró su propósito; hay que leer las razones', 'Hay que declarar mejor a la de 16 puntos y dejar de analizar, porque el puntaje ya lo dice todo', 'El puntaje alto siempre indica que la obra es nacional', 'Las razones de cada puntaje explican la valoración y evitan conclusiones apresuradas.'),
    ],
    ctx=('ab', 'Vas a ver una obra de un país que no conoces. ¿Qué haces antes?', 'Busco información del contexto en fuentes confiables', 'Decido que no me va a gustar por ser extranjera', 'Averiguar el contexto ayuda a comprender sin prejuicios.'),
    sc=[
        ("En Teatro: ¿cómo se comparan obras con recursos distintos?", "Por cómo cada una logra su propósito con lo que tiene", "Así se evita juzgar el presupuesto."),
        ("En Teatro: ¿Qué es un prejuicio?", "Un juicio formado antes de conocer la obra", "Se evita informándose y mirando la obra."),
        ("En Teatro: ¿Qué es una fuente confiable?", "Un documento o persona que informa con datos verificables", "Permite contrastar lo que se observa con datos comprobables."),
    ],
    op=("Escoge dos obras de ejemplo inventadas (una nacional y una extranjera) o usa las de la ficha. Escribe: una diferencia de recursos, una diferencia de contexto, cómo compararías cómo logran su propósito (sin comparar presupuestos) y una fuente confiable que consultarías.",
        "Función 1 (nacional) y función 2 (extranjera): recursos, sala pequeña sin escenografía frente a un teatro grande con proyecciones; contexto, compañía de barrio frente a una compañía profesional; comparo cómo cada una logra su propósito; consulto el programa de mano y una entrevista a la compañía.",
        ["diferencia de recursos", "diferencia de contexto", "compara el logro del propósito", "indica una fuente confiable"],
        ["hoja con cuatro respuestas"],
        ["comparar por presupuesto", "generalizar sobre un país"],
        "Pregunta: «¿qué logró cada obra con lo que tenía?». Debe responder por separado."),
    reinforce="Elige una película, serie u obra de otro país que conozcas y anota qué contexto averiguarías antes de evaluarla.",
    extend="Explica por qué la misma obra puede entenderse distinto desde dos perspectivas diferentes.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (crítica de ejemplo sobre «Los paraguas», inventada). Tesis: «Los paraguas» logra su propósito de mostrar la presión del grupo. Razones con evidencia: ocultar a quien se detiene bajo los paraguas muestra cómo el grupo lo borra, y la luz azul refuerza la frialdad. "
     "Otra lectura: alguien puede ver soledad; sin embargo, rodear a una persona indica un grupo y no un aislamiento. Sugerencia: acortar el final para que no repita la idea.")
build(
    O5, 5, F,
    use="Aprenderé a construir una postura personal fundada y respetuosa sobre una obra: tesis, razones con evidencia, reconocimiento de otra lectura y una sugerencia, y a conversar sobre desacuerdos sin herir.",
    prior=["Sé describir, interpretar y valorar.", "Sé evaluar según el propósito.", "Sé que una opinión sin evidencia es solo gusto."],
    explain=[
        "Una postura personal fundada se expresa en una crítica breve que tiene cuatro partes. La tesis dice con claridad qué piensas de la obra. Las razones sostienen la tesis con evidencia observable y criterios estéticos. El reconocimiento de otra lectura muestra que has considerado otro punto de vista razonable y explica por qué tu postura se sostiene. La sugerencia propone una mejora concreta. Así la crítica informa y ayuda, en vez de solo calificar.",
        "Una postura respetuosa critica la obra y sus decisiones, no a las personas. Evita burlas, apodos y exageraciones como «todo estuvo horrible». Es posible estar en desacuerdo sin herir: se pregunta por la evidencia de la otra persona, se reconoce lo que tiene de razonable y se explica la propia razón. Cambiar de opinión ante buenas razones muestra madurez, no debilidad.",
        "En redes y comentarios en línea se mantiene el mismo cuidado. Si recibes mensajes ofensivos o de hostigamiento sobre tu trabajo, no respondas con insultos ni los reenvíes, guarda captura como evidencia, bloquea a quien te hostiga y avisa a una persona adulta de confianza. Ese protocolo vale para cualquier persona del curso que sea objeto de burlas o amenazas.",
    ],
    vocab=[("tesis", "idea central que se defiende en una crítica"), ("razón", "motivo que sostiene la tesis, con evidencia"), ("otra lectura", "interpretación distinta y razonable de la misma obra"), ("respeto", "trato que no hiere ni descalifica a las personas"), ("hostigamiento", "ataque repetido contra una persona, por ejemplo con mensajes ofensivos")],
    worked=[
        ("Identificar las partes", "En una crítica: «Creo que la obra no logra emocionar. Los silencios son tan largos que se pierde la tensión. Otra persona puede verlos como suspenso, pero aquí repiten la misma idea. Podrían acortarse». Marca las partes.", ["Tesis: no logra emocionar.", "Razón: los silencios largos pierden tensión. Otra lectura: suspenso. Sugerencia: acortarlos."], "Tesis, razón, otra lectura y sugerencia identificadas"),
        ("Responder a un desacuerdo", "Una compañera dice: «La obra es aburrida». Tú piensas que es lenta pero intencional. ¿Cómo respondes con respeto?", ["Preguntas qué momento le pareció aburrido y por qué.", "Explicas tu razón: el ritmo lento sostiene la sensación de espera, y reconoces que puede cansar."], "Preguntar por su evidencia y explicar tu razón sin descalificarla"),
    ],
    mistakes=[("Escribir una crítica con puro adjetivo: «horrible», «genial».", "No dice qué se vio ni por qué.", "Agrega razones con evidencia."),
              ("Responder a un mensaje ofensivo con otro insulto.", "Aumenta el conflicto y puede perjudicarte.", "No respondas, guarda captura, bloquea y avisa a una persona adulta.")],
    T=[
        ('abc', '{F} ¿Cuál es la tesis de la crítica de ejemplo?', 'Los paraguas logra su propósito de mostrar la presión del grupo', 'Los paraguas debería tener un final más corto, porque repite la idea de la obra', 'Los paraguas es una obra sobre soledad', 'La tesis es la idea central: la obra logra su propósito.'),
        ('abc', '{F} ¿Qué evidencia cita la crítica para sostener su tesis?', 'Ocultar a quien se detiene bajo los paraguas y la luz azul', 'Que la obra tiene cuatro intérpretes', 'Que el público aplaudió al final', 'Cita rasgos observables que respaldan la presión del grupo.'),
        ('abc', '{F} ¿Para qué sirve el reconocimiento de otra lectura en la crítica?', 'Para mostrar que se consideró otra mirada razonable y explicar por qué la propia se sostiene', 'Para cambiar de tesis y adoptar la otra lectura, porque la crítica debe terminar coincidiendo con ella', 'Para evitar comprometerse con una postura', 'Reconocer otra lectura da solidez y respeto a la postura propia.'),
        ('abc', '{F} ¿Qué cumple la última frase de la crítica?', 'Una sugerencia concreta de mejora', 'Una descripción de la luz', 'Una burla a los intérpretes', 'Propone acortar el final, lo que es una sugerencia.'),
        ('abc', 'Una crítica dice: «La obra es horrible». ¿Qué le falta?', 'Razones con evidencia que expliquen qué se vio y por qué no funciona', 'Más adjetivos negativos y exclamaciones, para que se note cuánto disgustó la obra a quien escribe', 'Una nota final del uno al siete', 'Sin razones y evidencia, la crítica solo expresa disgusto.'),
        ('abc', '¿Cuál comentario critica con respeto?', 'La escena del final se alarga y repite la idea; podría ser más breve', 'Los intérpretes no sirven para este trabajo y deberían dejar de hacerlo cuanto antes', 'Quien dirigió no entiende nada de teatro', 'El primero critica una decisión; los otros descalifican a las personas.'),
        ('abc', '{F} La crítica reconoce que alguien puede ver soledad en la obra. ¿Cómo explica por qué mantiene su postura?', 'Señala que rodear a una persona indica un grupo y no un aislamiento', 'Afirma que quien ve soledad no entendió bien la obra', 'Cambia su tesis para coincidir con esa otra lectura', 'La crítica responde a la otra lectura con evidencia de la obra, sin descalificar a quien la propone.'),
        ('abc', 'Alguien opina distinto a ti sobre una obra. ¿Cómo respondes con respeto?', 'Le pregunto qué evidencia lo lleva a pensar eso y explico la mía', 'Le digo que su opinión es un error y que no vale la pena seguir hablando del tema', 'Evito conversar para que no se moleste', 'Preguntar por la evidencia permite dialogar sin descalificar.'),
        ('abc', 'Cambias de opinión sobre una obra después de escuchar una buena razón de un compañero. ¿Qué indica?', 'Que consideras la evidencia y estás abierto a revisar tu postura', 'Que no tenías opinión propia y te dejas llevar por lo que dice el último que habla', 'Que perdiste el debate', 'Cambiar ante buenas razones es parte de una postura fundada.'),
        ('abc', 'Recibes en una red un mensaje que se burla de tu escena y de ti. ¿Qué haces?', 'No respondo con insultos, guardo captura, bloqueo y aviso a una persona adulta de confianza', 'Respondo con otro insulto para defenderme y dejar claro que no me intimida nadie', 'Borro todo para que nadie se entere', 'El protocolo evita escalar el conflicto y deja evidencia para pedir ayuda.'),
        ('abc', 'Un compañero comparte la captura de un mensaje ofensivo hacia otra persona para reírse. ¿Qué corresponde?', 'No reenviarla y avisar a una persona adulta', 'Reenviarla a más compañeros para que opinen', 'Comentarla en otro chat con burlas', 'Reenviar o burlarse amplía el daño; lo adecuado es no compartirla y pedir ayuda.'),
        ('=', 'En un taller, 20 estudiantes escribieron críticas y 14 incluyeron una razón con evidencia. ¿Qué porcentaje lo hizo?', '14*100//20', 'Se divide quienes incluyeron razón entre el total y se pasa a porcentaje.', ' %'),
        ('abc', 'Una crítica concluye: «La obra falla, pero no por culpa de los intérpretes; el ritmo del final repite la idea». ¿Qué valor tiene esa frase?', 'Separa la crítica a una decisión de la crítica a las personas', 'Disminuye el valor de la evidencia presentada antes', 'Evita proponer cualquier mejora', 'Dirige la crítica a la decisión y cuida el respeto a las personas.'),
    ],
    ctx=('ab', 'Debes escribir una crítica de una obra que no te gustó. ¿Cómo la empiezas?', 'Con una tesis clara y una razón con evidencia', 'Con un comentario burlón para captar atención', 'Una tesis con evidencia permite criticar con respeto y fundamento.'),
    sc=[
        ("En Teatro: ¿qué partes tiene una crítica breve fundada?", "Tesis, razones con evidencia, reconocimiento de otra lectura y sugerencia", "Es la estructura que hace la crítica útil."),
        ("¿Se critica la obra o a las personas?", "La obra y sus decisiones", "Criticar a las personas hiere y no ayuda."),
        ("Si recibes mensajes ofensivos en línea, ¿qué haces?", "No respondo con insultos, guardo captura, bloqueo y aviso a una persona adulta", "Es el protocolo seguro para cuidarse y pedir ayuda."),
    ],
    op=("Escoge una obra o escena de ejemplo (la que quieras o «Los paraguas») y escribe una crítica de cuatro a seis oraciones con: tesis, dos razones con evidencia, el reconocimiento de otra lectura y una sugerencia. Usa lenguaje respetuoso y no critiques a las personas.",
        "Creo que «Los paraguas» logra su propósito. Los paraguas que ocultan a quien se detiene muestran cómo el grupo lo borra, y la luz azul refuerza la frialdad. Alguien puede leerlo como soledad, pero el gesto de rodear indica un grupo. Sugiero acortar el final para que no repita la idea.",
        ["tesis clara", "dos razones con evidencia", "reconoce otra lectura", "incluye una sugerencia y lenguaje respetuoso"],
        ["crítica escrita de cuatro a seis oraciones"],
        ["usar solo adjetivos", "criticar a las personas"],
        "Pregunta: «¿qué viste exactamente para pensar eso?». Debe citar la evidencia."),
    reinforce="Escribe dos frases que expresen desacuerdo con respeto sobre una escena que viste, citando una evidencia en cada una.",
    extend="Explica por qué cambiar de opinión ante una buena razón fortalece la postura personal en lugar de debilitarla.",
)
