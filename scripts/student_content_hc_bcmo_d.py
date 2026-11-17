"""Biología celular y molecular (electivo 3.º y 4.º medio HC): OAC-04 (regulación génica, diferenciación, proliferación, envejecimiento y cáncer, clases 1 a 4)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas laboratorio, microscopio ni internet. "
             "Este cuaderno no propone experimentos con sustancias, seres vivos ni cuerpos: los resultados que se analizan se entregan ya escritos. "
             "Los casos de salud son generales y ficticios; no sirven para diagnosticar ni decidir tratamientos. Si una duda sobre salud te preocupa, conversa con una persona adulta de confianza o con un profesional de la salud.")
build = make_build(MATERIALS)

O4 = "CN-BCMO-3y4-OAC-04"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (tabla de ejemplo; los genes son inventados). Todas las células de un mismo organismo tienen los mismos genes. Genes de ejemplo: G1, necesario para obtener energía en cualquier célula; G2, proteína de contracción; G3, proteína de la transmisión nerviosa; G4, enzima que procesa sustancias en el hígado. "
     "Expresión (sí o no): célula muscular: G1 sí, G2 sí, G3 no, G4 no. Célula nerviosa: G1 sí, G2 no, G3 sí, G4 no. Célula del hígado: G1 sí, G2 no, G3 no, G4 sí.")
build(
    O4, 1, F,
    use="Aprenderé por qué células con el mismo ADN pueden ser tan distintas, y qué es la regulación génica. Sirve para delimitar la pregunta que se investiga en el resto de la unidad.",
    prior=["Sé que el ADN contiene genes.", "Conozco transcripción y traducción.", "Sé que hay células de distintos tipos."],
    explain=[
        "Un organismo pluricelular comienza como una sola célula, el cigoto, que se divide muchas veces. Todas sus células reciben el mismo ADN, pero unas son musculares, otras nerviosas y otras del hígado. La diferencia no está en qué genes tienen, sino en cuáles se expresan, es decir, cuáles se transcriben y se traducen. Esa selección se llama regulación génica.",
        "Algunos genes se expresan en casi todas las células porque cumplen funciones básicas, como obtener energía. Otros se expresan solo en ciertos tipos de células o en ciertos momentos. El proceso por el cual una célula se vuelve de un tipo especializado se llama diferenciación celular. En una célula diferenciada, ciertos genes están activos y muchos otros, apagados.",
        "Plantear la pregunta de investigación es delimitar el sistema: qué células, qué genes y qué condiciones. Por ejemplo: «¿qué genes se expresan en una célula muscular y en una nerviosa del mismo organismo?». Una buena pregunta tiene datos que permiten responderla y deja fuera lo que no se puede estudiar con ellos.",
    ],
    vocab=[("expresión génica", "uso de un gen para fabricar su producto (ARN y proteína)"), ("regulación génica", "control de qué genes se expresan, cuándo y cuánto"), ("diferenciación celular", "proceso por el que una célula adquiere una función especializada"), ("cigoto", "primera célula de un organismo que se forma por fecundación"), ("célula madre", "célula que puede dar origen a otros tipos de células")],
    worked=[
        ("Leer la tabla", "Con la tabla, ¿qué genes se expresan en la célula nerviosa?",
         ["Se busca la fila de la célula nerviosa.", "G1 sí y G3 sí; G2 y G4 no."],
         "G1 y G3"),
        ("Misma información, distinta expresión", "¿La célula muscular tiene el gen G3, aunque no lo exprese?",
         ["Todas las células de un organismo tienen los mismos genes.", "Que no se exprese no significa que no esté."],
         "Sí, lo tiene pero no lo expresa"),
    ],
    mistakes=[("Decir que las células musculares «perdieron» los genes que no usan.", "Conservan todos los genes; solo expresan algunos.", "Escribe «no expresa» en vez de «no tiene»."),
              ("Creer que un gen que no se expresa no sirve.", "Puede ser esencial en otro tipo de célula o en otro momento.", "Pregunta dónde y cuándo se expresa.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es la regulación génica?", "El control de qué genes se expresan, cuándo y cuánto", "La copia de todos los genes", "La eliminación de genes que no se usan", "La regulación decide qué genes se usan en cada momento y célula."),
        ("{F} ¿Qué genes se expresan en la célula muscular?", "G1 y G2", "En la fila de la célula muscular aparecen G1 y G2 con «sí»."),
        ("{F} ¿Qué gen se expresa en las tres células de la tabla?", "G1", "Solo G1 tiene «sí» en las tres filas."),
        ("abc", "{F} ¿Qué gen permite distinguir mejor la célula del hígado de las otras dos de la tabla?", "G4", "G1", "G2", "Solo la célula del hígado expresa G4; G1 se expresa en las tres y G2 en la muscular."),
        ("ab", "{F} ¿Por qué G1 se expresa en todas las células?", "Porque cumple una función básica que todas necesitan", "Porque es el gen más largo", "Obtener energía es una función que todas las células necesitan."),
        ("{F} ¿Cuántos genes de la tabla se expresan en la célula nerviosa?", "2", "En la célula nerviosa solo G1 y G3 tienen «sí»."),
        ("=", "{F} En total hay 4 genes. ¿Cuántos genes no se expresan en la célula del hígado?", "4-2", "Se expresan dos genes, G1 y G4, así que se restan del total.", " genes"),
        ("=", "{F} Entre las tres células, ¿cuántas expresiones «sí» hay en total en la tabla?", "2+2+2", "Cada célula tiene dos «sí», y se suman las tres filas.", " expresiones"),
        ("abc", "{F} Una compañera dice que la célula nerviosa perdió el gen G2. ¿Cuál es la mejor corrección?", "Lo tiene, pero no lo expresa", "Tiene razón: lo perdió", "Lo tiene en una forma distinta en cada célula", "Las células tienen los mismos genes; cambia su expresión."),
        ("abc", "{F} Una célula madre de ejemplo se diferencia en célula del hígado. ¿Qué cambia?", "Los genes que se expresan", "El número de genes del ADN", "El tipo de bases del ADN", "La diferenciación cambia qué genes se activan, no el ADN."),
        ("ab", "¿Qué pregunta está mejor delimitada?", "¿Qué genes de la tabla se expresan en la célula muscular y en la nerviosa?", "¿Qué hay en el cuerpo humano?", "La primera indica células, genes y datos para responder."),
        ("abc", "{F} Si un gen de ejemplo G5 se expresara solo durante el desarrollo temprano, ¿qué indica?", "Que la regulación depende también del momento", "Que el gen se perdió después", "Que el gen no existe en el adulto", "Un gen puede expresarse solo en cierta etapa."),
        ("abc", "{F} Se quiere saber si una célula de ejemplo es muscular. ¿Qué dato de la tabla sirve mejor?", "Que exprese G2, la proteína de contracción", "Que exprese G1", "Que tenga el gen G3 en su ADN", "G1 se expresa en todas y G3 está en todas, pero G2 se expresa solo en la muscular."),
    ],
    ctx=("abc", "Contexto: una compañera piensa que cada tipo de célula tiene un ADN distinto. Para explicárselo en una frase, ¿qué le dices?", "Tienen el mismo ADN, pero expresan distintos genes", "Tienen ADN distinto porque son distintas", "Tienen el mismo ADN y expresan los mismos genes", "La diferencia entre células está en la expresión de los genes."),
    sc=[
        ("En Biología celular y molecular: ¿qué es la diferenciación celular?", "El proceso por el que una célula adquiere una función especializada", "La diferenciación convierte una célula en un tipo especializado."),
        ("ab", "Todas las células de un organismo tienen:", "Los mismos genes", "Genes distintos", "Todas parten del mismo cigoto y reciben el mismo ADN."),
        ("ab", "Un gen que no se expresa:", "Sigue estando en el ADN", "Desaparece", "No se expresa, pero sigue en el genoma."),
    ],
    op=("Con la tabla de la ficha {F}: (1) escribe una pregunta de investigación bien delimitada sobre la expresión de genes; (2) explica en dos oraciones qué dato de la tabla responde a tu pregunta; (3) escribe un límite: algo que la tabla no permite saber.",
        "(1) ¿Qué genes se expresan en la célula muscular y no en la nerviosa? (2) G2 aparece con «sí» solo en la muscular. (3) No dice cuánto de cada gen se expresa ni qué señales lo activan.",
        ["pregunta con células y genes", "dato de la tabla que la responde", "límite bien formulado"],
        ["tres respuestas numeradas"],
        ["pregunta demasiado amplia", "citar un dato que no responde la pregunta", "no declarar límite"],
        "Pregunta: «¿qué dato nuevo necesitarías para saber qué activa G2?»."),
    reinforce="Haz una tabla de dos células inventadas y dos genes inventados con «sí» o «no» en cada celda y escribe una conclusión.",
    extend="Explica por qué el hecho de que todas las células compartan el mismo ADN se relaciona con la teoría celular.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (datos de ejemplo; unidades arbitrarias). Una bacteria de ejemplo tiene un gen que fabrica una enzima para usar lactosa. Un represor es una proteína que bloquea el gen; la lactosa se une al represor y este deja de bloquear. "
     "La glucosa es un azúcar que la bacteria prefiere: cuando hay glucosa, el gen se activa poco. Actividad de la enzima en cuatro condiciones: condición 1, con glucosa y sin lactosa: 2; condición 2, con glucosa y con lactosa: 10; condición 3, sin glucosa y con lactosa: 100; condición 4, sin glucosa y sin lactosa: 2.")
build(
    O4, 2, F,
    use="Aprenderé cómo se regula un gen en una bacteria y qué papel cumplen los represores, los factores de transcripción y las señales del ambiente. Sirve para evaluar datos con variables y para entender por qué un gen se activa solo cuando es necesario.",
    prior=["Sé qué es un gen.", "Sé qué es la transcripción.", "Sé qué es una variable."],
    explain=[
        "Las bacterias ahorran energía fabricando enzimas solo cuando las necesitan. Por ejemplo, una bacteria de ejemplo fabrica la enzima que usa lactosa solo si hay lactosa. Un conjunto de genes con un interruptor común se llama operón. El interruptor tiene una región llamada promotor, donde se une la enzima que transcribe, y una región vecina donde puede unirse una proteína represora que bloquea la transcripción.",
        "Cuando no hay lactosa, el represor bloquea el gen. Cuando hay lactosa, esta se une al represor, lo inactiva y la transcripción puede ocurrir. Además, la presencia de glucosa disminuye la activación aunque haya lactosa, porque la bacteria prefiere ese azúcar. Esta regulación combina dos señales: lactosa (enciende) y glucosa (apaga).",
        "En las células eucariontes la regulación es más compleja. Intervienen muchos factores de transcripción, que son proteínas que se unen al ADN cerca de un gen y favorecen o impiden su lectura. Algunos reciben señales de afuera de la célula, como hormonas, y así el ambiente influye en la expresión. Evaluar un experimento sobre esto exige identificar qué variable se cambia, qué se mide y qué se mantiene igual.",
    ],
    vocab=[("operón", "conjunto de genes con un mismo interruptor"), ("promotor", "región del ADN donde se une la enzima que transcribe"), ("represor", "proteína que bloquea la transcripción de un gen"), ("factor de transcripción", "proteína que se une al ADN y favorece o impide la transcripción"), ("variable", "condición que se cambia o se mide en un experimento")],
    worked=[
        ("Identificar variables", "En la ficha, ¿qué variables se cambian y cuál se mide?",
         ["Se cambia la presencia de glucosa y la de lactosa.", "Se mide la actividad de la enzima."],
         "Cambian glucosa y lactosa; se mide la actividad de la enzima"),
        ("Comparar condiciones", "¿Qué comparación muestra el efecto de la lactosa cuando no hay glucosa?",
         ["Se comparan las condiciones 3 y 4: ambas sin glucosa.", "Con lactosa es 100 y sin lactosa es 2."],
         "Condición 3 frente a condición 4"),
    ],
    mistakes=[("Comparar condiciones que difieren en dos variables a la vez.", "Así no se sabe cuál variable produjo el cambio.", "Compara condiciones que difieran en una sola variable."),
              ("Decir que el represor «destruye» el gen.", "El represor solo bloquea la transcripción; el gen sigue en el ADN.", "Escribe «bloquea» o «impide la lectura».")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué hace un represor?", "Bloquea la transcripción de un gen", "Copia el ADN", "Fabrica la lactosa", "El represor impide que el gen se transcriba."),
        ("{F} ¿Cuál es la actividad de la enzima en la condición 3?", "100", "La ficha indica 100 para la condición sin glucosa y con lactosa."),
        ("{F} ¿Qué molécula se une al represor y lo inactiva?", "La lactosa", "La lactosa se une al represor y este deja de bloquear."),
        ("abc", "{F} ¿Qué condición tiene la mayor actividad de la enzima?", "La condición 3", "La condición 1", "La condición 4", "La condición 3 tiene lactosa y no tiene glucosa, con un valor de 100."),
        ("ab", "{F} Entre las condiciones 1 y 4, ¿qué variable cambia?", "La presencia de glucosa", "La presencia de lactosa", "En ambas no hay lactosa; la 1 tiene glucosa y la 4 no."),
        ("{F} ¿Qué región del ADN reconoce la enzima que transcribe?", "El promotor", "La enzima que transcribe se une al promotor."),
        ("=", "{F} ¿Cuántas veces mayor es la actividad de la condición 3 que la de la condición 4?", "100/2", "Se divide la actividad de la condición 3 por la de la condición 4.", " veces"),
        ("=", "{F} ¿Cuántas unidades más de actividad tiene la condición 2 que la condición 1?", "10-2", "Se restan las actividades de las dos condiciones para obtener la diferencia.", " unidades"),
        ("abc", "{F} Para ver el efecto de la lactosa cuando hay glucosa, ¿qué condiciones se comparan?", "La 1 y la 2", "La 3 y la 4", "La 2 y la 3", "La 1 y la 2 tienen glucosa y solo difieren en la lactosa."),
        ("abc", "{F} ¿Qué conclusión apoyan los datos sobre la glucosa?", "Disminuye la activación del gen aunque haya lactosa", "No tiene efecto alguno", "Aumenta la activación siempre", "Con lactosa, la actividad es 10 con glucosa y 100 sin glucosa."),
        ("ab", "{F} Un compañero compara las condiciones 1 y 3 para ver el efecto de la lactosa. ¿Qué problema tiene?", "Cambian dos variables a la vez: glucosa y lactosa", "Nada: es la comparación correcta", "La condición 1 tiene glucosa y la 3 no, además de la lactosa, así que no se puede atribuir el cambio a una sola."),
        ("abc", "{F} Si el represor no pudiera inactivarse, ¿qué esperarías con lactosa y sin glucosa?", "Actividad baja, porque el gen seguiría bloqueado", "Actividad alta como siempre", "Actividad igual a la condición 3", "Un represor que no se inactiva sigue bloqueando el gen."),
        ("abc", "{F} ¿Por qué ahorra energía regular el gen de esta enzima?", "Porque solo se fabrica cuando hay lactosa que usar", "Porque así la bacteria produce más lactosa", "Porque el gen se destruye cuando no se usa", "No fabricar una enzima inútil ahorra recursos a la bacteria."),
    ],
    ctx=("abc", "Contexto: tu grupo prepara un afiche para explicar por qué una bacteria no gasta energía fabricando enzimas que no necesita. ¿Cuál es el mensaje más preciso?", "Un represor bloquea el gen y la señal del ambiente, como la lactosa, lo libera", "La bacteria elimina el gen cuando no lo usa", "El gen se enciende siempre al mismo ritmo", "La regulación se basa en un interruptor que responde a señales."),
    sc=[
        ("En Biología celular y molecular: ¿qué es un factor de transcripción?", "Una proteína que se une al ADN y favorece o impide la transcripción", "Los factores de transcripción regulan qué genes se leen."),
        ("ab", "El promotor es:", "Una región del ADN donde se une la enzima que transcribe", "Una proteína que bloquea", "El promotor es una región, no una proteína."),
        ("ab", "Para atribuir un efecto a una variable hay que:", "Cambiar solo esa variable", "Cambiar todas a la vez", "Mantener iguales las demás variables evita que otras causas expliquen el efecto."),
    ],
    op=("Con los datos de la ficha {F}: (1) escribe qué variable se cambia, cuál se mide y qué se mantiene igual en la comparación de las condiciones 3 y 4; (2) escribe tu conclusión sobre el efecto de la lactosa; (3) propón una condición nueva (con datos de ejemplo inventados) y predice qué actividad esperarías.",
        "(1) Cambia la lactosa; se mide la actividad de la enzima; sigue igual la ausencia de glucosa. (2) La lactosa aumenta mucho la actividad cuando no hay glucosa. (3) Con glucosa y mucha lactosa esperaría una actividad baja, cercana a 10.",
        ["variables bien identificadas", "conclusión apoyada en los datos", "predicción coherente con el modelo"],
        ["tres respuestas numeradas"],
        ["confundir la variable cambiada con la medida", "concluir sin citar los datos", "predicción que contradice el modelo"],
        "Pregunta: «¿qué dato de la tabla te hizo elegir esa predicción?»."),
    reinforce="Haz una tabla con las cuatro condiciones, las dos variables cambiadas y la actividad medida.",
    extend="Explica por qué las hormonas pueden considerarse señales que modifican la expresión de genes en células eucariontes.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (modelo y datos de ejemplo). Modelo de interruptor: señal (por ejemplo, una hormona o un cambio de temperatura) → factor de transcripción → gen activado. "
     "Epigenética: cambios químicos en el ADN o en las proteínas que lo empaquetan (por ejemplo, la metilación del ADN) que pueden apagar o encender genes sin cambiar la secuencia de bases. "
     "Datos de ejemplo: cultivo de células a 25 °C: producción de una proteína de protección = 10 unidades; el mismo cultivo a 40 °C: 80 unidades; al volver a 25 °C: 12 unidades.")
build(
    O4, 3, F,
    use="Aprenderé un modelo de cómo el ambiente y las señales modifican la expresión de los genes, incluidos los cambios epigenéticos, y cómo eso permite que una célula se diferencie o responda a un estímulo. Sirve para interpretar datos de respuesta celular.",
    prior=["Sé qué es un factor de transcripción.", "Sé qué es la diferenciación celular.", "Sé leer una tabla de resultados."],
    explain=[
        "Las células reciben señales del ambiente: nutrientes, hormonas, temperatura. Una señal puede activar un factor de transcripción, y este activa o apaga genes. Así la célula ajusta sus proteínas a lo que ocurre afuera. Cuando el estímulo desaparece, muchas veces la respuesta vuelve al nivel anterior, porque el cambio es reversible.",
        "La epigenética estudia cambios químicos que modifican la expresión de los genes sin cambiar la secuencia del ADN. Por ejemplo, la metilación del ADN suele asociarse a genes apagados. Algunos de estos cambios se mantienen cuando la célula se divide, y por eso ayudan a que una célula diferenciada conserve su identidad: una célula del hígado da células del hígado. Otros cambios pueden variar con la edad y con el ambiente.",
        "Un modelo sirve para predecir: si se aplica una señal que activa el factor de transcripción, se espera más producto del gen. Pero también tiene límites: no todos los cambios del ambiente actúan por el mismo camino, y muchos genes responden a varias señales a la vez. Interpretar el modelo con datos de ejemplo permite practicar este razonamiento.",
    ],
    vocab=[("señal", "molécula o condición del ambiente que informa algo a la célula"), ("epigenética", "estudio de los cambios que regulan genes sin alterar la secuencia del ADN"), ("metilación", "cambio químico del ADN que suele asociarse a genes apagados"), ("reversible", "que puede volver al estado anterior"), ("estímulo", "cambio del ambiente que provoca una respuesta")],
    worked=[
        ("Leer una respuesta reversible", "En los datos de la ficha, ¿la respuesta al calor es reversible?",
         ["A 25 °C hay 10 unidades; a 40 °C, 80.", "Al volver a 25 °C hay 12, casi el nivel inicial."],
         "Sí, casi vuelve al nivel inicial"),
        ("Aplicar el modelo", "Se bloquea en el cultivo de ejemplo el factor de transcripción. ¿Qué producción esperas a 40 °C?",
         ["El calor funciona como señal que activa el factor.", "Sin factor, el gen no se activa."],
         "Una producción baja, cercana a la de 25 °C"),
    ],
    mistakes=[("Pensar que la epigenética cambia la secuencia del ADN.", "Modifica la expresión de los genes sin cambiar las bases.", "Escribe «sin cambiar la secuencia»."),
              ("Creer que toda respuesta al ambiente es permanente.", "Muchas respuestas son reversibles cuando desaparece el estímulo.", "Revisa si los datos muestran el regreso al nivel inicial.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué estudia la epigenética?", "Cambios que regulan genes sin alterar la secuencia del ADN", "Mutaciones que cambian las bases", "La forma de los organelos", "La epigenética regula la expresión sin cambiar las bases."),
        ("{F} ¿Cuántas unidades de la proteína se producen a 25 °C al inicio?", "10", "La ficha señala 10 unidades a 25 °C."),
        ("{F} ¿Cuántas unidades se producen a 40 °C?", "80", "La ficha indica 80 unidades a 40 °C."),
        ("abc", "{F} ¿Qué actúa como señal en los datos de ejemplo?", "El aumento de temperatura", "La metilación del ADN", "La secuencia del gen", "El cambio de 25 °C a 40 °C provoca más producción."),
        ("ab", "{F} Según el modelo, ¿qué activa directamente el gen?", "El factor de transcripción activado por la señal", "La temperatura sin ninguna proteína", "La señal activa al factor y este activa al gen."),
        ("{F} ¿Qué cambio químico del ADN se menciona como ejemplo de epigenética?", "La metilación", "La metilación del ADN es un ejemplo de cambio epigenético."),
        ("=", "{F} ¿Cuántas veces mayor es la producción a 40 °C que a 25 °C al inicio?", "80/10", "Se divide la producción a 40 °C por la producción a 25 °C.", " veces"),
        ("=", "{F} ¿Cuántas unidades baja la producción al volver de 40 °C a 25 °C?", "80-12", "Se resta la producción final de la producción a 40 °C.", " unidades"),
        ("abc", "{F} Al volver a 25 °C la producción es 12. ¿Qué indica?", "Que la respuesta fue casi totalmente reversible", "Que la respuesta fue permanente", "Que el gen se destruyó", "12 es muy cercano a 10, el nivel inicial."),
        ("abc", "{F} Una célula de ejemplo tiene el gen de protección metilado y apagado. ¿Qué esperas a 40 °C?", "Poca producción, porque el gen está apagado", "Mucha producción, porque el calor siempre activa el gen", "Ninguna célula produce nada", "Un gen apagado por metilación responde poco a la señal."),
        ("ab", "Una compañera dice: «la metilación cambia las bases del ADN». ¿Qué corriges?", "Cambia la expresión del gen sin cambiar la secuencia de bases", "Tiene razón en todo", "La metilación es un cambio químico encima del ADN que no altera las bases."),
        ("abc", "{F} ¿Por qué un cambio epigenético ayuda a mantener la identidad de una célula diferenciada?", "Porque puede conservarse cuando la célula se divide", "Porque cambia el ADN de las hijas", "Porque impide que la célula se divida", "El patrón de genes encendidos y apagados se transmite a las células hijas."),
        ("abc", "{F} Un modelo predice mucha producción con la señal, pero un cultivo de ejemplo con la señal produce poco. ¿Qué haces?", "Revisar si hay otro factor que impide la activación", "Descartar todos los modelos", "Ignorar el resultado", "Un dato que no calza invita a revisar el modelo y buscar factores que faltan."),
    ],
    ctx=("abc", "Contexto: en el diario mural quieres explicar por qué dos personas con el mismo ADN pueden tener perfiles de expresión distintos. ¿Qué incluyes?", "Los cambios epigenéticos y las señales del ambiente modifican qué genes se expresan", "Que su ADN cambia cada día", "Que no es posible que difieran", "La expresión depende de señales y de cambios epigenéticos."),
    sc=[
        ("En Biología celular y molecular: ¿qué es la metilación del ADN?", "Un cambio químico que suele asociarse a genes apagados", "La metilación es un ejemplo de regulación epigenética."),
        ("ab", "Una respuesta reversible:", "Puede volver al nivel inicial", "Es siempre permanente", "Reversible significa que el estado anterior puede volver."),
        ("ab", "Un modelo sirve para:", "Predecir y detectar sus propios límites", "Evitar usar datos", "Los datos nuevos se comparan con lo que predice el modelo para ponerlo a prueba."),
    ],
    op=("Con los datos y el modelo de la ficha {F}: (1) escribe el modelo de interruptor con las tres piezas; (2) predice la producción a 32 °C (una temperatura intermedia sin dato en la ficha) y escribe qué supuesto haces; (3) explica con una frase por qué un cambio epigenético no es una mutación.",
        "(1) Señal (calor), factor de transcripción, gen activado. (2) Entre 10 y 80, por ejemplo cerca de 45, suponiendo que la respuesta crece de forma gradual con la temperatura; es un supuesto porque no hay dato. (3) Porque cambia la expresión del gen sin cambiar la secuencia de bases.",
        ["tres piezas del modelo", "predicción coherente", "diferencia entre epigenética y mutación"],
        ["tres respuestas numeradas"],
        ["omitir el factor de transcripción", "dar un valor sin declarar el supuesto", "decir que la epigenética cambia las bases"],
        "Pregunta: «¿qué dato nuevo te permitiría comprobar tu predicción?»."),
    reinforce="Dibuja el modelo de interruptor con tres cajas y flechas y rotula cada pieza con un ejemplo de la ficha.",
    extend="Explica por qué la regulación de genes por el ambiente puede ser una ventaja para una célula y para un organismo.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (datos de ejemplo; todos inventados y generales). Ciclo celular con puntos de control: la célula revisa si el ADN está dañado antes de dividirse. Genes aceleradores (protooncogenes) que estimulan la división y genes frenos (supresores de tumores) que la detienen o provocan la muerte de la célula dañada. "
     "Cáncer: células que se dividen sin control por acumulación de cambios en genes del ciclo; no tiene una sola causa. "
     "Envejecimiento: en cada división los extremos de los cromosomas (telómeros) se acortan. Telómero de ejemplo: 100 unidades al inicio y pierde 5 unidades por división. "
     "Tejidos de ejemplo: tejido 1, 2 de cada 100 células en división; tejido 2, 20 de cada 100.")
build(
    O4, 4, F,
    use="Aprenderé cómo la regulación de genes se relaciona con la proliferación celular, el envejecimiento y el cáncer, analizando datos de ejemplo. Sirve para distinguir lo que sabemos de lo que se debe consultar a profesionales de la salud.",
    prior=["Conozco el ciclo celular y la mitosis.", "Sé qué es una mutación.", "Sé qué es regulación génica."],
    explain=[
        "La proliferación celular es el aumento del número de células por división. Está regulada por genes aceleradores y frenos. Si el ADN está dañado, los puntos de control detienen el ciclo y la célula repara el daño o se elimina. Esta vigilancia mantiene a los tejidos ordenados. En respuesta a estímulos ambientales, como una herida, las células reciben señales que aumentan temporalmente la proliferación.",
        "El cáncer ocurre cuando una célula acumula cambios genéticos y epigenéticos que hacen que sus aceleradores estén siempre activos o que sus frenos fallen. La célula se divide sin control y sus descendientes también. No hay una sola causa ni un solo gen: suele requerir varios cambios acumulados con el tiempo. Los tratamientos y la prevención son temas de profesionales de la salud, no de un cuaderno de estudio.",
        "El envejecimiento es otro proceso asociado a la regulación y al daño acumulado. Entre varios factores, se ha observado que los telómeros se acortan en cada división, y que la expresión de ciertos genes cambia con la edad. Cuando los telómeros están muy cortos, la célula suele dejar de dividirse. Estas ideas se estudian con datos, y todavía hay preguntas abiertas.",
    ],
    vocab=[("proliferación", "aumento del número de células por división"), ("protooncogén", "gen acelerador de la división celular"), ("supresor de tumores", "gen que frena la división o elimina células dañadas"), ("punto de control", "momento del ciclo en que la célula revisa si puede continuar"), ("telómero", "extremo protector de un cromosoma")],
    worked=[
        ("Contar divisiones por telómero", "El telómero de la ficha parte con 100 unidades y pierde 5 por división. ¿Cuántas unidades tiene tras 8 divisiones?",
         ["Pérdida total: 5 × 8 = 40.", "Quedan 100 − 40 = 60."],
         "60 unidades"),
        ("Comparar tejidos", "En el tejido 2, 20 de cada 100 células se dividen. ¿Qué porcentaje es?",
         ["20 de 100 es 20 %.", "En el tejido 1 es 2 %."],
         "20 %"),
    ],
    mistakes=[("Decir que el cáncer tiene una sola causa.", "Suele resultar de varios cambios acumulados en genes del ciclo y en su regulación.", "Habla de acumulación de cambios y de factores."),
              ("Creer que el acortamiento de telómeros explica por sí solo todo el envejecimiento.", "Es un factor entre varios, y hay otros procesos.", "Escribe «uno de los factores».")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es un supresor de tumores?", "Un gen que frena la división o elimina células dañadas", "Un gen que acelera siempre la división", "Un organelo que fabrica proteínas", "Los supresores de tumores actúan como frenos del ciclo."),
        ("=", "{F} Si se observan 500 células del tejido 1, ¿cuántas se esperan en división con la proporción de la ficha?", "500/100*2", "Son 2 de cada 100; en 500 células hay cinco grupos de 100, y cada uno aporta 2.", " células"),
        ("{F} ¿Cuántas unidades pierde el telómero por división?", "5", "La ficha indica una pérdida de 5 unidades por división."),
        ("abc", "{F} ¿Qué hacen los puntos de control?", "Revisan si el ADN está dañado antes de dividirse", "Aceleran la división sin revisar", "Destruyen el ADN", "Los puntos de control detienen el ciclo si hay daño."),
        ("ab", "{F} ¿Qué ocurre en el cáncer según la ficha?", "Las células se dividen sin control por acumulación de cambios en genes del ciclo", "Las células dejan de dividirse por completo", "El cáncer es una proliferación sin control, no una falta de divisiones."),
        ("{F} ¿Cuál de los dos tejidos de ejemplo tiene mayor proporción de células en división?", "El tejido 2", "En el tejido 2 se dividen 20 de cada 100, más que en el tejido 1."),
        ("=", "{F} ¿Cuántas unidades de telómero quedan tras 6 divisiones?", "100-5*6", "Se resta de las 100 unidades iniciales la pérdida total de 5 por división.", " unidades"),
        ("=", "{F} ¿Cuántas veces más células en división tiene el tejido 2 que el tejido 1?", "20/2", "Se divide el número de células en división del tejido 2 por el del tejido 1.", " veces"),
        ("=", "{F} Si un telómero de ejemplo es de 100 unidades y ya no se divide al llegar a 40, ¿cuántas divisiones puede hacer?", "(100-40)/5", "Se divide lo que puede perder el telómero entre la pérdida por división.", " divisiones"),
        ("abc", "{F} En el tejido 2 de ejemplo, se observa una herida reciente. ¿Qué explica la mayor proporción de divisiones?", "Señales de la herida que aumentan temporalmente la proliferación", "Que sus células perdieron todos los genes", "Que el tejido envejeció", "Una herida es un estímulo que puede activar la proliferación."),
        ("abc", "{F} Una estudiante afirma: «el tejido 2 tiene cáncer porque se divide más». ¿Qué corriges?", "Con ese dato no se puede concluir: una mayor proliferación puede ser normal, como en una reparación", "Tiene razón en todo", "El tejido 2 no tiene células", "Dividirse más no basta; hay que mirar si el control se perdió."),
        ("ab", "{F} ¿Por qué se acorta el telómero y esto se relaciona con el envejecimiento?", "Porque al ser muy corto la célula suele dejar de dividirse", "Porque el ADN deja de existir", "Cuando el telómero es muy corto, la célula deja de dividirse, lo que afecta la renovación de los tejidos."),
        ("abc", "Alguien te pregunta cómo evitar o tratar el cáncer con lo que viste en esta clase. ¿Qué respuesta es adecuada?", "Que esas decisiones son de profesionales de la salud y que esta clase solo explica conceptos", "Que con lo visto puede indicar qué hábitos le evitarán el cáncer con seguridad", "Que no tiene tratamiento", "Un cuaderno de estudio no reemplaza la atención profesional."),
    ],
    ctx=("abc", "Contexto: en una charla del liceo, una persona dice que «el cáncer es una sola enfermedad con una sola causa». ¿Cómo respondes con precisión y respeto?", "Es un conjunto de enfermedades que suelen resultar de varios cambios acumulados en la regulación de la división", "Tiene toda la razón", "Es una infección simple", "Una respuesta precisa menciona la acumulación de cambios y varias causas."),
    sc=[
        ("En Biología celular y molecular: ¿qué es un telómero?", "El extremo protector de un cromosoma", "El telómero protege los extremos de los cromosomas."),
        ("ab", "Un protooncogén es:", "Un gen acelerador de la división", "Un gen freno", "Los protooncogenes estimulan la división celular."),
        ("ab", "El cáncer resulta de:", "Cambios acumulados en la regulación de la división", "Una sola causa simple", "Es un proceso con varios cambios."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula cuántas unidades tendrá el telómero tras 10 divisiones; (2) explica con dos oraciones qué relación hay entre los puntos de control y el cáncer; (3) escribe un límite: qué no permite concluir el dato de ejemplo sobre los dos tejidos.",
        "(1) 100 − 50 = 50 unidades. (2) Los puntos de control detienen la división si el ADN está dañado; si fallan, una célula dañada puede seguir dividiéndose. (3) No permite concluir que el tejido 2 tenga cáncer, porque se divide más por varias razones, como reparar una herida.",
        ["cálculo correcto del telómero", "relación explicada entre puntos de control y cáncer", "límite bien formulado"],
        ["un cálculo y dos respuestas"],
        ["calcular mal la pérdida", "afirmar que más divisiones siempre significa cáncer", "dar consejos de salud personales"],
        "Pregunta: «¿qué otro dato necesitarías para interpretar mejor el tejido 2?»."),
    reinforce="Escribe una frase con acelerador y otra con freno del ciclo celular, y explica qué ocurre si falla cada uno.",
    extend="Explica por qué el cáncer y el envejecimiento se estudian con datos de muchos casos y no con un solo ejemplo.",
)
