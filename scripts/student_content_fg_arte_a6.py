"""Cuaderno del estudiante de Artes Visuales 3.º y 4.º medio FG: FG-ARTE-3y4-OAC-06 (evaluación crítica de procesos y proyectos visuales)."""
from __future__ import annotations

from fg_arte_common import build

OA = "FG-ARTE-3y4-OAC-06"

# ---------------------------------------------------------------- Clase 1
build(
    OA, 1,
    "Aprenderé a distinguir el proceso del resultado de un proyecto visual, audiovisual o multimedia y a reunir evidencias de ambos. Sirve para evaluar proyectos propios y de mis compañeros con criterios y no con impresiones.",
    ["Sé armar un juicio con criterio y evidencia.", "Sé que un comentario se dirige a la obra y no a la persona."],
    [
        "Un proyecto visual tiene un proceso y un resultado. El proceso es todo lo que ocurre desde la idea hasta la obra: pruebas, bocetos, decisiones, ajustes y cambios de plan. El resultado es la obra terminada. Evaluar críticamente es valorar ambos con criterios, que son las razones con que se juzga, y con evidencias, que son rasgos o registros observables. Un resultado puede ser muy bueno con un proceso desordenado, o un proceso muy cuidado puede dar un resultado que aún no cumple su propósito. Por eso se evalúan por separado.",
        "Las evidencias del proceso son la bitácora (cuaderno con fechas, pruebas y decisiones), los bocetos, las versiones descartadas y los registros de cambios. Las evidencias del resultado son lo que se ve y se oye en la obra final. Los criterios se toman del propósito expresivo de la obra: si busca calma, importa la coherencia del ritmo; si busca informar, importa la claridad. Un criterio sin evidencia es una opinión; una evidencia sin criterio es un dato suelto.",
        "Los proyectos de este cuaderno son de ejemplo, de estudiantes ficticios. Evaluar no es atacar: se valora el trabajo, no a la persona, y se propone cómo mejorarlo. Postura personal fundada significa decir qué pienso y por qué, con evidencias, y respetuosa significa hacerlo sin burlas ni comparaciones ofensivas. Si algo del proceso de un compañero me preocupa por su bienestar, lo converso con una persona adulta de confianza y no con el curso.",
    ],
    [("proceso", "camino desde la idea hasta la obra, con pruebas, decisiones y ajustes"), ("resultado", "obra terminada tal como la ve y la oye el público"), ("evidencia", "rasgo o registro observable que respalda un juicio"), ("bitácora", "cuaderno con fechas, pruebas y decisiones del proceso"), ("postura fundada", "opinión personal apoyada en criterios y evidencias")],
    [
        ("Separar proceso y resultado", "Proyecto de ejemplo «Lluvia»: una animación de 6 segundos con papel. La bitácora muestra cuatro pruebas de movimiento con fechas y una versión descartada. La obra final se ve a saltos en dos momentos. ¿Qué dato es del proceso y cuál del resultado?", ["Del proceso: cuatro pruebas con fechas y una versión descartada.", "Del resultado: la obra final se ve a saltos en dos momentos.", "Se evalúan por separado."], "Proceso: pruebas y versión descartada; resultado: saltos en dos momentos"),
        ("Elegir criterio según el propósito", "El proyecto de ejemplo «Pasaje» es una ilustración digital que busca informar sobre el reciclaje en un barrio. ¿Qué criterio es más pertinente: la claridad del mensaje o el número de colores?", ["Su propósito es informar.", "Si el propósito es informar, el criterio central es la claridad del mensaje.", "El número de colores no mide el propósito."], "La claridad del mensaje"),
    ],
    [
        ("Evaluar solo el resultado y olvidar cómo se llegó a él.", "Se pierde información sobre decisiones y aprendizajes.", "Revisa la bitácora, los bocetos y las versiones además de la obra final."),
        ("Mezclar el proceso con la persona: «es desordenado» en lugar de describir el registro.", "Se juzga a quien trabaja y no el trabajo.", "Describe el registro: «la bitácora no tiene fechas»."),
    ],
    [
        ("abc", "En Artes Visuales, ¿qué es el proceso de un proyecto?", "El camino desde la idea hasta la obra, con pruebas, decisiones y ajustes", "La obra ya terminada, tal como se exhibe ante el público en la sala", "La lista de materiales que se compraron para realizar todo el proyecto", "El proceso incluye todo lo que ocurre antes del resultado."),
        ("abc", "¿Cuál es una evidencia del proceso?", "Una bitácora con fechas y pruebas registradas", "El título de la obra impreso en el afiche de la muestra", "La cantidad de personas que fueron a la exposición", "La bitácora muestra cómo se trabajó."),
        ("abc", "¿Cuál es una evidencia del resultado?", "Lo que se ve y se oye en la obra final", "Los bocetos descartados en la carpeta de trabajo", "La nota que el autor espera recibir", "El resultado se evalúa en la obra terminada."),
        ("abc", "Un proyecto de ejemplo tuvo un proceso muy ordenado, pero su obra final no cumple el propósito. ¿Qué conclusión es adecuada?", "Que proceso y resultado se evalúan por separado y piden mejoras distintas", "Que el proceso no sirve de nada, porque el resultado finalmente falló", "Que el resultado es correcto, porque el proceso fue muy ordenado", "Cada uno tiene sus evidencias y sus criterios."),
        ("abc", "Un compañero dice: «Tu proyecto es malo». ¿Qué falta para que sea una evaluación crítica?", "Un criterio y una evidencia observable", "Un tono de voz más fuerte", "Una comparación con otros proyectos del curso", "Sin criterio y evidencia solo es una opinión."),
        ("abc", "Un proyecto busca informar y su mensaje es difícil de leer. ¿Qué criterio falla?", "La claridad del mensaje", "La cantidad de bocetos", "El tamaño de la bitácora", "Si el propósito es informar, el criterio central es la claridad del mensaje."),
        ("abc", "La bitácora de un grupo no tiene fechas ni explica los cambios. ¿Cómo lo describes de forma respetuosa?", "«La bitácora no registra fechas ni explica los cambios»", "«Son desordenados y no les importa el trabajo que hacen»", "«Hicieron una bitácora horrible y nadie va a entenderla»", "Se describe el registro sin juzgar a las personas."),
        ("abc", "El proyecto de ejemplo «Lluvia» tiene saltos en dos momentos. ¿Qué evidencia respalda esa afirmación?", "Se ve que el movimiento se corta entre dos fotogramas del final", "A algunos compañeros no les gustó la animación en la proyección", "El autor dice que cree que la animación está muy bien hecha", "Es un rasgo observable en la obra final."),
        ("abc", "Un compañero muestra un proceso con muchas pruebas descartadas y se siente mal por 'haber fallado'. ¿Qué respuesta ayuda?", "Mostrar que las versiones descartadas son evidencia valiosa del proceso", "Decirle que mejor oculte las pruebas para que no se note el error", "Compararlo con otro grupo que casi no descartó ninguna versión", "Las pruebas descartadas muestran cómo se decidió."),
        ("abc", "Dos evaluaciones de ejemplo de «Pasaje»: X) «Está mal». Y) «El mensaje de reciclaje se entiende, pero la letra es pequeña para leer a 3 metros». ¿Cuál es más útil?", "Y, porque tiene criterio, evidencia y orienta una mejora", "X, porque es breve y directa, y no se presta a confusiones", "Ninguna, porque cualquier evaluación es subjetiva y no sirve", "Y se puede comprobar y permite actuar."),
        ("abc", "Notas que el proceso de un compañero te preocupa porque dice que está muy agobiado. ¿Qué haces?", "Conversarlo con una persona adulta de confianza", "Comentarlo con todo el curso para que lo ayuden entre todos", "Burlarte un poco para que se anime a trabajar más rápido", "Su bienestar se cuida con apoyo adulto, no con exposición."),
        ("abc", "Un proyecto de ejemplo cumple su plazo, pero no registró ninguna prueba. ¿Qué evidencia del proceso falta?", "Registros de pruebas y decisiones", "La nota de otros proyectos", "El número de personas del grupo", "Sin registros no se puede valorar el proceso."),
        ("abc", "Un compañero dice: «Mi resultado es excelente, así que mi proceso no importa». ¿Qué responde la pauta?", "Que el proceso también se evalúa y aporta aprendizajes", "Que tiene razón, porque un buen resultado lo explica todo", "Que el resultado no importa si el proceso fue largo", "Proceso y resultado se valoran por separado."),
    ],
    ("abc", "Tu curso evalúa «Lluvia», una animación de ejemplo de 6 segundos con papel. Un compañero escribe: «La bitácora muestra cuatro pruebas con fechas. En la obra final el movimiento se corta en dos momentos. El propósito era la calma, y esos cortes la interrumpen». ¿Qué tiene esta evaluación?", "Evidencia del proceso, del resultado y un criterio ligado al propósito", "Solo una opinión general sobre el autor y su forma de trabajar", "Una comparación entre este proyecto y los de otros cursos", "Reúne evidencias y relaciona el propósito con el resultado."),
    [
        ("ab", "Las versiones descartadas, ¿son evidencia del proceso?", "Sí", "No", "Las versiones descartadas muestran cómo se tomaron las decisiones del proceso."),
        ("ab", "Evaluar críticamente, ¿es atacar a quien hizo el trabajo?", "No", "Sí", "Se valora el trabajo con respeto y se propone cómo mejorarlo."),
        ("Verdadero o falso: un criterio sin evidencia es solo una opinión.", "Verdadero", "La evidencia permite comprobar lo que se afirma."),
    ],
    (
        "Elige UN proyecto de ejemplo. A) «Lluvia»: animación de 6 segundos con papel; bitácora con cuatro pruebas con fechas; movimiento cortado en dos momentos; propósito: calma. B) «Pasaje»: ilustración digital sobre reciclaje; sin bitácora; mensaje claro, letra pequeña; propósito: informar. C) «Eco»: pieza sonora de 1 minuto con voces de vecinos (con permiso); bitácora con dos pruebas sin fechas; algunos relatos se oyen bajo; propósito: documentar. Escribe una evaluación breve con dos evidencias del proceso, dos del resultado, el criterio ligado al propósito y una recomendación respetuosa.",
        "Elegí A. Proceso: cuatro pruebas con fechas; una versión descartada. Resultado: movimiento cortado en dos momentos; ritmo lento. Criterio: coherencia con la calma. Recomendación respetuosa: repetir esos dos fotogramas para quitar los cortes.",
        ["separa proceso y resultado", "usa evidencias observables", "liga el criterio al propósito", "recomienda con respeto"],
        ["evaluación breve", "evidencias separadas"],
        ["mezclar proceso y persona", "evaluar sin evidencia"],
        "Pregunta qué evidencia respalda cada afirmación y cuál es el criterio.",
    ),
    "Piensa en algo que hiciste en un trabajo escolar y di una evidencia de tu proceso y otra de tu resultado.",
    "Escribe tres frases que expliquen por qué se evalúan por separado el proceso y el resultado.",
)

# ---------------------------------------------------------------- Clase 2
build(
    OA, 2,
    "Aprenderé a usar instrumentos de evaluación (lista de cotejo, escala de apreciación, rúbrica, bitácora) y modalidades (autoevaluación, coevaluación, heteroevaluación) en proyectos visuales. Sirve para evaluar con orden y para elegir el instrumento que mejor recoge la evidencia.",
    ["Sé separar proceso y resultado y reunir evidencias.", "Sé elegir criterios ligados al propósito."],
    [
        "Un instrumento de evaluación es una herramienta para recoger evidencias con criterios claros. La lista de cotejo registra si un rasgo está presente o no («sí» o «no»). La escala de apreciación indica en qué grado se cumple un rasgo, por ejemplo de 1 a 4. La rúbrica combina varios criterios con descripciones de cada nivel. La bitácora registra el proceso con fechas. Cada instrumento sirve para algo: la lista de cotejo es rápida y la rúbrica es más completa.",
        "Según quién evalúa, hay tres modalidades. En la autoevaluación evalúo mi propio trabajo. En la coevaluación una compañera o un compañero evalúa el mío y yo el suyo. En la heteroevaluación evalúa otra persona, como mi docente. Usarlas juntas da una mirada más completa. Una buena retroalimentación puede seguir la estructura «dos aciertos y una sugerencia»: dos cosas que funcionan, con su evidencia, y una mejora concreta.",
        "Un instrumento debe usar criterios que se entiendan y niveles que se puedan distinguir. Si dos niveles se parecen mucho, la evaluación se vuelve confusa. También debe respetar a las personas: no incluye comparaciones entre estudiantes ni juicios sobre su forma de ser. Y si el instrumento pide datos personales, se evita y se usa solo lo necesario para evaluar.",
    ],
    [("lista de cotejo", "instrumento que registra si un rasgo está presente o no"), ("escala de apreciación", "instrumento que indica en qué grado se cumple un rasgo"), ("rúbrica", "instrumento con varios criterios y descripciones de cada nivel"), ("autoevaluación", "evaluación que hace una persona de su propio trabajo"), ("coevaluación", "evaluación entre compañeros o compañeras")],
    [
        ("Elegir un instrumento", "Quieres revisar rápido si cada proyecto de ejemplo del curso cumple estos cinco rasgos: tiene título, autoría, fecha, bitácora y cartela. ¿Qué instrumento conviene?", ["Cada rasgo está o no está.", "La lista de cotejo registra presencia o ausencia.", "Es rápida de aplicar."], "Una lista de cotejo"),
        ("Dar dos aciertos y una sugerencia", "Proyecto de ejemplo «Pasaje»: el mensaje de reciclaje se entiende y la paleta (los colores elegidos) es coherente; la letra es pequeña para leer a 3 metros. Escribe la retroalimentación.", ["Acierto 1: el mensaje se entiende.", "Acierto 2: la paleta es coherente.", "Sugerencia: aumentar el tamaño de la letra."], "Dos aciertos (mensaje y paleta) y una sugerencia (letra más grande)"),
    ],
    [
        ("Usar una lista de cotejo para valorar el grado de calidad de un rasgo.", "La lista solo registra si el rasgo está o no.", "Usa una escala de apreciación o una rúbrica para graduar la calidad."),
        ("Escribir niveles de una rúbrica casi iguales entre sí.", "No se pueden distinguir y la evaluación se confunde.", "Describe cada nivel con una diferencia observable."),
    ],
    [
        ("abc", "En Artes Visuales, ¿qué es una lista de cotejo?", "Un instrumento que registra si un rasgo está presente o no", "Un instrumento que describe varios niveles de calidad en cada criterio", "Un cuaderno donde se anotan las pruebas con fechas", "La lista de cotejo se marca con sí o no."),
        ("abc", "¿Qué instrumento combina varios criterios con descripciones de cada nivel?", "La rúbrica", "La lista de cotejo", "La bitácora", "La rúbrica describe niveles por criterio."),
        ("abc", "Cuando una compañera evalúa tu trabajo y tú evalúas el suyo, ¿cómo se llama?", "Coevaluación", "Autoevaluación", "Heteroevaluación", "Es una evaluación que se hace entre compañeros o compañeras del mismo nivel."),
        ("abc", "Evalúas tu propio trabajo con una escala de 1 a 4. ¿Qué modalidad es?", "Autoevaluación", "Coevaluación", "Heteroevaluación", "Eres tú quien evalúa tu propio trabajo."),
        ("abc", "Tu docente evalúa tu proyecto con una rúbrica. ¿Qué modalidad es?", "Heteroevaluación", "Autoevaluación", "Coevaluación", "Evalúa una persona externa al grupo de trabajo."),
        ("abc", "Una rúbrica de ejemplo dice nivel 2: «el mensaje se entiende a veces» y nivel 3: «el mensaje se entiende casi siempre». ¿Qué le falta para distinguir bien esos niveles?", "Una diferencia observable, como cuántas personas lo entienden", "Letras más grandes y de otro color en cada fila de la tabla", "Un tercer criterio sin relación con el mensaje de la obra", "Los niveles deben distinguirse con rasgos observables."),
        ("abc", "¿Qué estructura propone la retroalimentación «dos aciertos y una sugerencia»?", "Dos cosas que funcionan con evidencia y una mejora concreta", "Dos críticas fuertes y una felicitación al final del texto", "Una opinión general sobre el autor y dos preguntas sobre él", "Equilibra reconocimiento y propuesta de mejora."),
        ("abc", "Un instrumento pide a los estudiantes su dirección y su teléfono para evaluar un proyecto visual. ¿Qué es adecuado hacer?", "No incluir esos datos, porque no se necesitan para evaluar", "Pedir también su correo para poder enviar los resultados", "Pedirles una foto de su casa para conocer su contexto", "Se usa solo la información necesaria."),
        ("abc", "Un grupo quiere comprobar que cada proyecto tenga título, autoría, fecha y cartela. ¿Qué instrumento le ahorra más tiempo?", "Una lista de cotejo, porque solo registra si cada rasgo está", "Una rúbrica de cuatro niveles para describir cada rasgo", "Una entrevista larga a cada integrante de los grupos", "Para saber si un rasgo está o no basta una lista de cotejo."),
        ("abc", "Para evaluar el grado de claridad de un mensaje en cuatro niveles, ¿qué instrumento conviene?", "Una escala de apreciación o una rúbrica", "Una lista de cotejo con solo sí o no en cada rasgo", "Un cuaderno con fechas donde se anotan las pruebas", "Para graduar la calidad de un rasgo se necesitan niveles, no solo sí o no."),
        ("abc", "Una compañera usa la coevaluación para burlarse del dibujo de otro. ¿Qué corresponde?", "Pedir que revise con criterios y rasgos, sin burlas", "Aceptar su comentario porque es sincero y directo con el otro", "Borrar la coevaluación sin conversar con nadie sobre ella", "La coevaluación respeta a las personas y se basa en evidencias."),
        ("abc", "Un grupo quiere evaluar su propio proyecto, el de otro grupo y recibir la evaluación del docente. ¿Cuántas modalidades usarán?", "Tres: autoevaluación, coevaluación y heteroevaluación", "Una sola, porque todas son una misma evaluación del grupo", "Dos nada más, porque la tercera no existe en proyectos", "Cada evaluador representa una modalidad distinta."),
        ("abc", "Un instrumento mezcla el criterio «claridad» con el criterio «originalidad» en una sola fila. ¿Qué problema tiene?", "No permite saber cuál de los dos se evalúa", "Es demasiado corto para evaluar un proyecto completo", "Tiene una letra pequeña que cuesta leer en la hoja", "Cada fila debe medir un solo criterio."),
    ],
    ("abc", "Tu curso diseña una rúbrica para una animación de ejemplo con tres criterios (coherencia con el propósito, uso del ritmo y claridad) y cuatro niveles. Una compañera propone agregar un criterio sobre «si el autor es simpático». ¿Qué corresponde?", "No incluirlo, porque no se relaciona con la obra ni con su propósito", "Incluirlo, porque ayuda a mantener una buena convivencia en el curso", "Incluirlo con el nivel más alto para todos los integrantes", "Los criterios deben estar ligados a la obra."),
    [
        ("ab", "La lista de cotejo, ¿registra presencia o grado?", "Presencia o ausencia", "Grado de calidad", "Se responde con sí o no."),
        ("ab", "Una rúbrica, ¿describe niveles de cada criterio?", "Sí", "No", "Describe qué se espera en cada nivel."),
        ("Verdadero o falso: los instrumentos de evaluación deben pedir datos personales de los estudiantes.", "Falso", "Un instrumento de evaluación pide solo la información necesaria y ningún dato personal."),
    ],
    (
        "Elige UN proyecto de ejemplo. A) «Lluvia»: animación de 6 segundos con papel y bitácora. B) «Pasaje»: ilustración digital sobre reciclaje. C) «Eco»: pieza sonora de 1 minuto con voces de vecinos (con permiso). Diseña un instrumento de evaluación de tu elección (lista de cotejo, escala o rúbrica) con tres criterios ligados al propósito y escribe una retroalimentación «dos aciertos y una sugerencia» usando datos de ejemplo que inventes y rotules como tales.",
        "Elegí B y una rúbrica. Criterios: claridad del mensaje, coherencia de la paleta, legibilidad del texto. Niveles 1 a 3. Retroalimentación de ejemplo: acierto 1, el mensaje se entiende; acierto 2, la paleta es coherente; sugerencia, aumentar la letra para leerla a 3 metros.",
        ["elige un instrumento adecuado", "liga los criterios al propósito", "escribe niveles distinguibles", "da dos aciertos y una sugerencia"],
        ["instrumento diseñado", "retroalimentación"],
        ["mezclar criterios en una fila", "pedir datos personales"],
        "Pregunta por qué eligió ese instrumento y cómo distinguió los niveles.",
    ),
    "Escribe para un trabajo tuyo una lista de tres rasgos que se pueden marcar con sí o no.",
    "Explica en tres frases la diferencia entre autoevaluación, coevaluación y heteroevaluación.",
)

# ---------------------------------------------------------------- Clase 3
build(
    OA, 3,
    "Aprenderé a decidir qué mejorar primero en un proyecto a partir de las evidencias, comparando impacto y esfuerzo, y a sostener esa decisión con una postura fundada. Sirve para mejorar con foco y sin abandonar lo que ya funciona.",
    ["Sé usar instrumentos y modalidades de evaluación.", "Sé separar proceso y resultado."],
    [
        "Después de evaluar, hay que decidir qué hacer. Primero listo lo que funciona, que conviene conservar, y lo que falla. Luego, para cada mejora posible, estimo dos cosas: el impacto, que es cuánto mejora el propósito de la obra, y el esfuerzo, que es el tiempo y los materiales que cuesta. La mejor mejora para empezar es la que tiene mucho impacto y poco esfuerzo. Una mejora de poco impacto y mucho esfuerzo se deja para después o se descarta.",
        "Una postura fundada es una opinión personal respaldada por criterios y evidencias. Puedo decir: «Creo que lo más urgente es aumentar la letra, porque el propósito es informar y desde 3 metros no se lee». Una postura respetuosa evita burlas, no compara a personas y reconoce lo que funciona. Cuando mi decisión difiere de la de mi grupo, expongo mis razones, escucho las suyas y buscamos un acuerdo basado en evidencias.",
        "A veces la evidencia no alcanza para decidir: entonces hago una prueba pequeña. Por ejemplo, pruebo dos tamaños de letra con tres personas y elijo el que más se lee. También cuento con el tiempo: si quedan dos sesiones, elijo mejoras que quepan. Registro la decisión en la bitácora con la evidencia, el criterio y el resultado esperado, para poder revisarla después.",
    ],
    [("impacto", "cuánto mejora una acción el propósito de la obra"), ("esfuerzo", "tiempo y materiales que cuesta una acción"), ("postura fundada", "opinión personal respaldada por criterios y evidencias"), ("conservar", "mantener lo que ya funciona"), ("decisión", "elección de qué mejorar, apoyada en evidencias")],
    [
        ("Elegir qué mejorar primero", "Proyecto de ejemplo «Pasaje» (informar sobre reciclaje). Mejoras posibles: (1) aumentar la letra: impacto alto, esfuerzo bajo; (2) rehacer todos los dibujos: impacto medio, esfuerzo alto; (3) cambiar el color del borde: impacto bajo, esfuerzo bajo. ¿Cuál haces primero?", ["Busca mucho impacto y poco esfuerzo.", "La mejora 1 cumple ambos.", "Las otras son menos eficientes."], "La mejora 1, aumentar la letra"),
        ("Expresar una postura fundada", "En «Lluvia», el movimiento se corta en dos momentos y el propósito es la calma. Escribe una postura fundada y respetuosa sobre qué mejorar.", ["Evidencia: saltos en dos momentos.", "Criterio: coherencia con la calma.", "Postura: repetir esos fotogramas."], "«Creo que conviene repetir esos fotogramas, porque los saltos interrumpen la calma»"),
    ],
    [
        ("Querer mejorar todo a la vez.", "Se pierde foco y tiempo.", "Prioriza las mejoras de más impacto y menos esfuerzo."),
        ("Cambiar lo que funciona porque alguien lo propone.", "Se pierde un rasgo valioso.", "Primero listo lo que funciona y lo conservo."),
    ],
    [
        ("abc", "En Artes Visuales, ¿qué es el impacto de una mejora?", "Cuánto mejora el propósito de la obra", "Cuánto cuesta en materiales y en horas de trabajo", "Cuánta gente conoce y comenta el proyecto terminado", "El impacto mide el efecto sobre el propósito."),
        ("abc", "¿Qué mejora conviene hacer primero?", "La de mucho impacto y poco esfuerzo", "La de poco impacto y mucho esfuerzo", "La más difícil de todas", "Es la mejora más eficiente porque logra mucho efecto con poco trabajo."),
        ("abc", "Antes de decidir mejoras, ¿qué conviene listar?", "Lo que funciona y lo que falla", "Solo lo que falla, para no perder tiempo en otras cosas", "Solo lo que más le gustó al curso en la presentación", "Para conservar lo valioso y corregir lo que falla."),
        ("abc", "Una mejora tiene impacto alto y esfuerzo alto, y necesita unas 4 sesiones; otra tiene impacto medio y esfuerzo bajo. Quedan 2 sesiones. ¿Qué decides?", "La segunda, porque cabe en el tiempo y sirve al propósito", "La primera, aunque no alcance el tiempo para terminarla", "Ninguna de las dos, para no arriesgar el trabajo hecho", "Se elige lo viable con buen efecto."),
        ("abc", "Un grupo discrepa sobre qué mejorar. ¿Qué paso es adecuado?", "Exponer razones con evidencias y buscar un acuerdo", "Votar enseguida sin conversar sobre ninguna de las ideas", "Hacer lo que diga la persona que hable más fuerte", "Las evidencias permiten acordar con respeto."),
        ("abc", "¿Cuál es una postura fundada y respetuosa?", "«Creo que conviene aumentar la letra, porque a 3 m no se lee»", "«Esto está mal y es culpa de quienes lo hicieron en el grupo»", "«Hagan lo que quieran, a mí me da lo mismo lo que pase»", "Tiene opinión, razón y evidencia sin ofender."),
        ("abc", "No sabes si una letra de 4 cm o de 6 cm se lee mejor. ¿Qué haces?", "Probar los dos tamaños con tres personas y comparar", "Elegir al azar con una moneda para no discutir más", "Elegir la más pequeña por ahorrar papel y tiempo", "Una prueba pequeña aporta la evidencia que falta para decidir con criterio."),
        ("abc", "Un compañero te dice: «Tu idea de mejora es tonta». ¿Qué respondes?", "Le pides el rasgo y el criterio que lo llevan a opinar así", "Le respondes con un insulto parecido para quedar a la par", "Dejas de hablarle y no vuelves a mostrarle nada tuyo", "Pedir razones convierte la crítica en información."),
        ("abc", "Registras en tu bitácora: «Mejora: aumentar la letra. Evidencia: no se lee a 3 m. Resultado esperado: se lea a 3 m». ¿Qué parte falta para poder revisar después?", "El resultado obtenido tras hacerla", "El color del lápiz con que escribiste la mejora", "La edad de la persona que propuso la mejora", "Para revisar, se compara lo esperado con lo obtenido."),
        ("abc", "Mejora X: impacto alto, esfuerzo bajo. Mejora Y: impacto bajo, esfuerzo alto. Si solo puedes hacer una, ¿cuál?", "X", "Y", "Ninguna", "Se elige la mejora con mayor impacto en el propósito y menor esfuerzo."),
        ("abc", "Tu grupo conserva el ritmo lento de la animación, que funciona, y repite dos fotogramas. ¿Qué decisión aplicaron?", "Conservar lo que funciona y corregir lo que falla", "Rehacer todo desde el comienzo para empezar mejor", "No cambiar nada para evitar riesgos innecesarios", "Se conserva lo que funciona y se corrige selectivamente solo lo que falla."),
        ("abc", "Un compañero expone una postura sin evidencia: «hay que cambiar todo». ¿Qué le sugieres?", "Que señale el rasgo que lo lleva a esa conclusión", "Que cambie todo de inmediato para ver si funciona", "Que no hable más hasta tener la nota del proyecto", "La evidencia es la base de la postura."),
        ("abc", "Cuando una decisión de mejora se aplica, ¿qué conviene hacer después?", "Volver a evaluar para comprobar si mejoró", "Olvidar el tema y pasar a otra tarea del curso", "Cambiar de proyecto para no repetir el trabajo", "La evaluación se repite para verificar el efecto."),
    ],
    ("abc", "Tu grupo evalúa «Pasaje» y lista cuatro mejoras: A) aumentar la letra (impacto alto, esfuerzo bajo); B) rehacer los dibujos (impacto medio, esfuerzo alto); C) cambiar el borde (impacto bajo, esfuerzo bajo); D) agregar una cartela con autoría (impacto medio, esfuerzo bajo). Hay tiempo para dos. ¿Cuáles eligen?", "A y D, porque tienen buen impacto con poco esfuerzo", "B y C, porque son las más distintas entre sí y se notarían más", "C y D, porque son las más fáciles y rápidas de hacer", "Se priorizan impacto alto o medio con esfuerzo bajo."),
    [
        ("ab", "Una mejora de mucho impacto y poco esfuerzo, ¿se hace primero?", "Sí", "No", "Es la mejora más eficiente porque logra mucho efecto con poco trabajo."),
        ("ab", "Lo que funciona en un proyecto, ¿se conserva?", "Sí", "No", "Cambiarlo sin motivo pierde un logro."),
        ("Verdadero o falso: una postura fundada necesita criterio y evidencia.", "Verdadero", "Sin ellos sería solo una opinión."),
    ],
    (
        "Elige UN proyecto de ejemplo. A) «Lluvia»: movimiento cortado en dos momentos, bitácora clara, ritmo lento que funciona. B) «Pasaje»: mensaje claro, letra pequeña, sin cartela. C) «Eco»: voces con permiso, dos relatos se oyen bajo, sin fechas en la bitácora. Haz una lista de lo que funciona y lo que falla, estima impacto y esfuerzo de tres mejoras, elige las dos que harás y redacta una postura fundada y respetuosa en dos frases.",
        "Elegí C. Funciona: voces con permiso; mapa claro. Falla: dos relatos bajos; sin fechas. Mejoras: subir el volumen (impacto alto, esfuerzo bajo); agregar fechas (impacto medio, esfuerzo bajo); regrabar todo (impacto alto, esfuerzo alto). Haré las dos primeras. Postura: creo que lo urgente es subir el volumen, porque el propósito es documentar y hoy no se oyen dos relatos.",
        ["lista lo que funciona y lo que falla", "estima impacto y esfuerzo", "elige con criterio", "expresa una postura fundada y respetuosa"],
        ["tabla de mejoras", "postura de dos frases"],
        ["querer mejorar todo", "no conservar lo que funciona"],
        "Pregunta por qué priorizó esas mejoras y qué evidencia las respalda.",
    ),
    "Piensa en un trabajo escolar y di una mejora de alto impacto y poco esfuerzo, y una de poco impacto y mucho esfuerzo.",
    "Explica en tres frases por qué conviene conservar lo que ya funciona al mejorar un proyecto.",
)

# ---------------------------------------------------------------- Clase 4
build(
    OA, 4,
    "Aprenderé a redactar una evaluación crítica de un proyecto propio con contexto, criterios, evidencias del proceso y del resultado, postura personal y plan de mejora. Sirve para dar cuenta de mi trabajo con honestidad y para dialogar con quienes lo evalúan.",
    ["Sé decidir qué mejorar con impacto y esfuerzo.", "Sé expresar una postura fundada y respetuosa."],
    [
        "Un informe de evaluación crítica de un proyecto propio tiene seis partes. 1) Contexto: qué proyecto es, su propósito expresivo y el soporte. 2) Criterios: tres o cuatro, ligados al propósito. 3) Evidencias del proceso: bitácora, pruebas, versiones. 4) Evidencias del resultado: rasgos de la obra final. 5) Postura personal: cuánto logra su propósito, con razones y límites. 6) Plan de mejora: dos acciones con impacto, esfuerzo y plazo.",
        "La honestidad es clave: reconozco aciertos y problemas con evidencia y no los exagero. Si un problema se debió a mi organización, lo digo; si se debió a un imprevisto, lo explico sin buscar culpables. Uso un tono respetuoso, tanto con mi trabajo como con el de mis compañeros. Si mi proyecto incluyó a otras personas, reconozco su aporte con nombre solo si ellas lo permiten.",
        "Un buen informe cabe en una página. Puedo apoyar con una tabla simple de criterios y niveles. Incluyo fuentes y créditos de lo que usé, y reviso que no tenga datos personales. Si el informe se mostrará a otras personas, pido permiso antes de nombrar a compañeros. Y si el proyecto trató un tema que me afectó, puedo conversarlo con una persona adulta de confianza.",
    ],
    [("informe de evaluación", "texto que valora un proyecto con criterios y evidencias"), ("plan de mejora", "acciones con impacto, esfuerzo y plazo para mejorar un proyecto"), ("contexto", "descripción del proyecto, su propósito y su soporte"), ("honestidad", "reconocer aciertos y problemas con evidencia, sin exagerar"), ("plazo", "fecha o tiempo en que se hará una acción")],
    [
        ("Armar el contexto y los criterios", "Proyecto de ejemplo «Eco»: pieza sonora de 1 minuto con voces de vecinos (con su permiso), para documentar el barrio. Escribe el contexto y tres criterios.", ["Contexto: pieza sonora de 1 minuto, documentar el barrio.", "Criterio 1: claridad de las voces.", "Criterio 2: variedad de relatos.", "Criterio 3: coherencia del montaje."], "Contexto: pieza sonora para documentar; criterios: claridad, variedad, coherencia"),
        ("Plan de mejora", "En «Eco», dos relatos se oyen bajo. Quedan 2 sesiones. Escribe una acción con impacto, esfuerzo y plazo.", ["Acción: subir el volumen de esos relatos.", "Impacto alto; esfuerzo bajo.", "Plazo: sesión 1."], "Subir volumen de los dos relatos; impacto alto, esfuerzo bajo, sesión 1"),
    ],
    [
        ("Escribir un informe solo con elogios o solo con críticas.", "Pierde honestidad y no orienta mejoras.", "Incluye aciertos y problemas con evidencias."),
        ("Nombrar a compañeros sin permiso en el informe.", "Se expone a personas sin su acuerdo.", "Pide permiso o usa «un integrante del grupo»."),
    ],
    [
        ("abc", "En Artes Visuales, ¿qué es un plan de mejora?", "Acciones con impacto, esfuerzo y plazo para mejorar un proyecto", "Una lista de errores del autor ordenada de mayor a menor", "La nota final del proyecto con los comentarios de quien evaluó", "El plan de mejora ordena qué hacer y cuándo."),
        ("abc", "¿Qué se escribe en el contexto del informe?", "El proyecto, su propósito y su soporte", "Los errores del equipo y los plazos que no se cumplieron", "La nota que se espera obtener por el trabajo realizado", "El contexto presenta el proyecto, su propósito y el soporte donde se muestra."),
        ("abc", "¿Qué parte del informe expresa tu valoración de cuánto logra el proyecto su propósito?", "La postura personal", "El contexto del proyecto", "El resumen de los criterios", "La postura personal contiene la valoración fundada."),
        ("abc", "Un informe dice: «Mi proyecto es perfecto». ¿Qué le falta?", "Honestidad con evidencias de aciertos y problemas", "Más adjetivos positivos para que se note el entusiasmo", "Un título más largo y más llamativo para el proyecto", "La honestidad exige reconocer también los límites y problemas del trabajo."),
        ("abc", "Un problema se debió a que no organizaste el tiempo. ¿Cómo lo escribes en un informe honesto?", "«No distribuí bien el tiempo y por eso quedó una prueba sin hacer»", "«El problema fue culpa de mis compañeros, que no avanzaron»", "«No hubo problemas en ningún momento del proyecto»", "Reconoce la causa sin buscar culpables."),
        ("abc", "El informe menciona a un compañero por su nombre completo sin que él lo sepa. ¿Qué corriges?", "Pedir su permiso o escribir «un integrante del grupo»", "Dejarlo igual, porque lo que se escribe es verdad", "Agregar su curso y su dirección para identificarlo mejor", "Así se resguarda la privacidad de la persona sin ocultar el aporte del grupo."),
        ("abc", "En un plan de mejora, ¿qué dato permite saber si una acción cabe en el tiempo que queda?", "El plazo y el esfuerzo estimado de cada acción", "El color elegido para el título del informe", "El número de integrantes que firman el informe", "El esfuerzo y el plazo indican si cabe en el tiempo disponible."),
        ("abc", "¿Cuál es un criterio coherente con una pieza sonora que busca documentar relatos?", "Claridad de las voces", "Cantidad de colores del afiche", "Largo del título", "Documentar relatos exige que se oigan bien."),
        ("abc", "Un informe cabe en una página y tiene seis partes. Un compañero lo alarga con 5 páginas de opiniones. ¿Qué le sugieres?", "Ceñirse a las seis partes con evidencias", "Alargarlo todavía más para que tenga más peso", "Quitar las evidencias para que quede más corto", "Un buen informe es breve y fundado."),
        ("abc", "Tu informe incluye una ilustración hecha por una ilustradora real, tomada de una revista. ¿Qué agregas?", "El crédito y la fuente, y verificar que se pueda usar", "Nada, porque es una imagen que ya es pública", "El nombre de tu curso junto a la imagen", "Se cita a quien creó la imagen para respetar su autoría y su trabajo."),
        ("abc", "Dos posturas de ejemplo sobre «Eco»: X) «Logra su propósito parcialmente: las voces son variadas, pero dos se oyen bajo». Y) «Es buena». ¿Cuál es más útil?", "X, porque da una valoración con razones", "Y, porque es más positiva y anima más al grupo", "Ninguna, porque ambas posturas son solo subjetivas", "X orienta la mejora con evidencia."),
        ("abc", "Escribes tu informe y notas que el proyecto trató un tema que te afecta mucho. ¿Qué haces?", "Conversarlo con una persona adulta de confianza", "Esconderlo en el informe para que nadie lo note", "Compartirlo con todo el curso sin pensarlo mucho", "El apoyo adulto cuida tu bienestar."),
        ("abc", "El plan de mejora dice: «Mejorar el audio». ¿Cómo lo haces más útil?", "«Subir el volumen de dos relatos en la sesión 1»", "«Hacer todo mucho mejor en las próximas semanas»", "«Cambiar de tema y empezar un proyecto nuevo»", "Se agrega acción, medida y plazo."),
    ],
    ("abc", "Un grupo revisa dos informes de ejemplo sobre «Eco». El primero tiene contexto, tres criterios, evidencias de proceso y resultado, postura y plan de mejora. El segundo dice «Nos fue bien y es muy lindo». ¿Cuál cumple mejor la tarea?", "El primero, porque tiene las seis partes y evidencias", "El segundo, porque es más breve y más fácil de leer", "Ambos por igual, porque los dos cuentan cómo les fue", "El primero es completo y fundado."),
    [
        ("ab", "La postura personal, ¿necesita razones?", "Sí", "No", "Una postura fundada se apoya en criterios."),
        ("ab", "¿Un plan de mejora incluye plazo?", "Sí", "No", "El plazo organiza el trabajo y permite saber cuándo se hará cada acción."),
        ("Verdadero o falso: un informe honesto reconoce aciertos y problemas.", "Verdadero", "La honestidad requiere reconocer tanto los aciertos como los problemas."),
    ],
    (
        "Elige UN proyecto de ejemplo y completa un informe de evaluación de las seis partes. A) «Lluvia»: animación de 6 segundos con papel; cuatro pruebas con fechas; movimiento cortado en dos momentos; propósito: calma. B) «Pasaje»: ilustración digital sobre reciclaje; sin bitácora; letra pequeña; propósito: informar. C) «Eco»: pieza sonora de 1 minuto con voces de vecinos (con permiso); dos relatos bajos; propósito: documentar. Incluye al menos tres criterios, dos evidencias del proceso, dos del resultado, una postura personal con un límite y un plan de dos acciones con impacto, esfuerzo y plazo.",
        "Elegí A. Contexto: animación de 6 segundos con papel para transmitir calma. Criterios: coherencia con el propósito, ritmo, claridad. Proceso: cuatro pruebas con fechas; versión descartada. Resultado: movimiento cortado en dos momentos; ritmo lento. Postura: logra parcialmente la calma, no conozco la reacción de un público más amplio. Plan: repetir dos fotogramas (impacto alto, esfuerzo bajo, sesión 1); sumar un sonido suave (impacto medio, esfuerzo medio, sesión 2).",
        ["incluye las seis partes", "usa evidencias del proceso y del resultado", "reconoce un límite", "propone un plan con plazos"],
        ["informe de una página", "tabla de criterios"],
        ["solo elogios", "nombrar compañeros sin permiso"],
        "Pregunta qué evidencias respaldan su postura y cómo ordenó el plan.",
    ),
    "Cuéntale a alguien de tu casa en tres frases qué lograste y qué mejorarías de un trabajo reciente.",
    "Escribe una postura personal de dos frases sobre un trabajo imaginario, con un límite reconocido.",
)

# ---------------------------------------------------------------- Clase 5
build(
    OA, 5,
    "Aprenderé a dar y recibir retroalimentación respetuosa sobre proyectos visuales propios y de pares, y a mantener una postura fundada cuando hay desacuerdos. Sirve para aprender de otras miradas sin perder el respeto ni la autoría.",
    ["Sé redactar una evaluación con criterios, evidencias y plan de mejora.", "Sé que se evalúa el trabajo y no a la persona."],
    [
        "La retroalimentación es un comentario que ayuda a mejorar un trabajo. Una buena retroalimentación es específica (señala un rasgo), basada en un criterio, equilibrada (reconoce lo que funciona), propone un cambio posible y se dirige al trabajo, no a la persona. Puedo usar la estructura: observo (rasgo), valoro (criterio), sugiero (cambio). Por ejemplo: «Observo que el ritmo es lento; eso es coherente con la calma; podrías repetir los dos fotogramas que se cortan».",
        "Recibir retroalimentación también requiere habilidad. Escucho sin interrumpir, tomo nota, pido ejemplos si no entiendo y separo lo útil de lo que no lo es. Decido qué cambiar y qué mantener: la autoría sigue siendo mía. Si no estoy de acuerdo, puedo decirlo con respeto, apoyando mi postura con evidencias, por ejemplo: «Mantengo el color porque el propósito es calma».",
        "Si la retroalimentación es hiriente, burlesca o me incomoda, no respondo con agresión: me detengo, guardo el comentario como evidencia y lo conversamos con una persona adulta de confianza o con mi docente. Tampoco publico comentarios sobre compañeros en grupos abiertos ni comparto sus trabajos sin permiso. Y cuando mi retroalimentación es la que recibe otra persona, me pregunto cómo me gustaría que me lo dijeran.",
    ],
    [("retroalimentación", "comentario que ayuda a mejorar un trabajo con rasgos concretos"), ("específica", "que señala un rasgo preciso y no una impresión general"), ("equilibrada", "que reconoce lo que funciona y propone una mejora"), ("postura fundada", "opinión personal respaldada por criterios y evidencias"), ("desacuerdo", "diferencia de opinión que se resuelve con razones y respeto")],
    [
        ("Dar retroalimentación en tres pasos", "Proyecto de ejemplo «Lluvia»: ritmo lento coherente con la calma; movimiento cortado en dos momentos. Escribe retroalimentación con observo, valoro y sugiero.", ["Observo: ritmo lento y dos cortes.", "Valoro: el ritmo es coherente con la calma.", "Sugiero: repetir los dos fotogramas."], "Observo ritmo lento y dos cortes; valoro la coherencia; sugiero repetir fotogramas"),
        ("Mantener una postura con respeto", "Un compañero te sugiere cambiar el color de fondo de tu ilustración, pero tú crees que el actual apoya el propósito de calma. ¿Cómo respondes con una postura fundada?", ["Reconoce su comentario.", "Explica tu criterio: propósito de calma.", "Decide mantener el color."], "«Gracias; mantengo el color porque apoya el propósito de calma»"),
    ],
    [
        ("Responder a una crítica con enojo o burla.", "La conversación pierde su utilidad y puede herir.", "Pide el rasgo, toma nota y decide con calma."),
        ("Cambiar todo por presión del grupo.", "Se pierde la autoría.", "Evalúa la sugerencia con tus criterios y decide."),
    ],
    [
        ("abc", "En Artes Visuales, ¿cuál es una retroalimentación específica?", "«El ritmo lento es coherente con la calma; los dos cortes la interrumpen»", "«Está bien en general, aunque podría mejorar en varios aspectos»", "«No me gusta mucho cómo quedó, siento que le falta algo»", "Señala rasgos precisos y su efecto."),
        ("abc", "¿Qué pasos propone la estructura «observo, valoro, sugiero»?", "Rasgo, criterio y cambio posible", "Opinión, burla y nota final para el grupo", "Elogio, queja y silencio hasta la próxima clase", "Cubre lo que se ve, por qué importa y cómo mejorar."),
        ("abc", "¿Qué significa que una retroalimentación sea equilibrada?", "Reconoce lo que funciona y propone una mejora", "Solo elogia el trabajo para que nadie se sienta mal", "Solo critica los errores para que se corrijan pronto", "Combina el reconocimiento de lo que funciona con una propuesta de mejora."),
        ("abc", "Recibes un comentario que no entiendes. ¿Qué haces?", "Pides un ejemplo del rasgo al que se refiere", "Lo ignoras y sigues con tu trabajo sin cambiar nada", "Te enojas y respondes que no sabe de lo que habla", "Pedir ejemplos aclara el comentario y permite decidir qué cambiar."),
        ("abc", "No estás de acuerdo con una sugerencia sobre tu ilustración. ¿Qué corresponde?", "Decirlo con respeto y apoyar tu postura con una evidencia", "Aceptar todo lo que digan para evitar una discusión con el grupo", "Responder con una burla para que no insista más con eso", "Una postura fundada se defiende con razones."),
        ("abc", "Un comentario sobre tu animación es: «es malísima y tú no sabes dibujar». ¿Qué haces?", "No respondes igual, guardas el comentario y avisas a tu docente", "Respondes con un insulto para que se sienta igual que tú", "Lo publicas en un grupo abierto para que todos lo juzguen", "Se cuida la convivencia y se pide ayuda."),
        ("abc", "Quieres comentar el trabajo de una compañera en un grupo abierto con su nombre y su foto. ¿Qué haces?", "No lo publicas; se lo entregas directamente a ella", "Lo publicas igual, porque es una crítica muy útil para todos", "Lo compartes con todo el colegio para que opinen también", "Se respeta su privacidad y se comenta con ella."),
        ("abc", "Dos grupos de ejemplo: el A recibió «dos aciertos y una sugerencia» concreta; el B, «hay que mejorar». ¿Cuál tiene mejor retroalimentación?", "El A, porque es específica y propone un cambio", "El B, porque es breve y se puede aplicar a todo trabajo", "Ambas por igual, porque las dos son comentarios del curso", "Solo la primera retroalimentación orienta acciones concretas para mejorar."),
        ("abc", "Una compañera cambia su proyecto completamente porque dos personas lo criticaron. ¿Qué observación hacen?", "Debe evaluar cada sugerencia con sus criterios antes de cambiar", "Tiene razón, porque dos personas pesan más que una sola", "Debe ignorar todos los comentarios para no confundirse más", "La autoría exige decidir con criterio."),
        ("abc", "Antes de dar una retroalimentación, ¿qué conviene preguntarse?", "Cómo me gustaría que me lo dijeran", "Cómo puedo ganar la discusión frente al grupo", "Cuánto puedo exagerar para que me hagan caso", "La empatía mejora el comentario porque cuida a la persona que lo recibe."),
        ("abc", "Tomas nota de tres comentarios sobre tu proyecto. Uno es hiriente, uno es de gusto y uno señala un rasgo y un cambio. ¿Cuál usas para mejorar?", "El que señala rasgo y cambio", "El hiriente, por ser más fuerte", "El de gusto, por ser más corto", "Solo el específico orienta una mejora."),
        ("abc", "Tienes que dar retroalimentación a un compañero que está muy sensible. ¿Qué es adecuado?", "Reconocer lo que funciona y proponer un cambio concreto con respeto", "No decirle nada nunca, para no incomodarlo ni arriesgar la amistad", "Decirle todo lo que está mal de una sola vez y sin pausas", "Se mantiene el respeto y la utilidad."),
        ("abc", "En una puesta en común, tu retroalimentación es: «Observo que la letra es pequeña; el propósito es informar; sugiero aumentarla». ¿Qué paso falta si quieres equilibrio?", "Reconocer algo que funciona, como la claridad del mensaje", "Insistir en que la letra es pequeña con más énfasis todavía", "Cambiar el tema del proyecto para evitar el problema de la letra", "El equilibrio incluye reconocer al menos un acierto además de la sugerencia."),
    ],
    ("abc", "Tu curso hace una ronda de retroalimentación. Para «Pasaje», una persona escribe: «Observo que el mensaje de reciclaje se entiende; es coherente con informar; podrías aumentar la letra para leerla a 3 metros». Otra escribe: «Está feo». ¿Cuál comentario usará el autor para mejorar?", "El primero, porque es específico y propone un cambio", "El segundo, porque es más directo y no pierde el tiempo", "Ninguno de los dos, porque el autor decide solo cómo mejorar", "El primero orienta una acción concreta."),
    [
        ("ab", "Una retroalimentación respetuosa, ¿habla de la obra o de la persona?", "De la obra", "De la persona", "Se evalúa el trabajo con respeto."),
        ("ab", "Si no estás de acuerdo con un comentario, ¿puedes explicar tu postura?", "Sí, con respeto y evidencias", "No, debes quedarte callado para evitar un conflicto", "Una postura fundada se puede defender."),
        ("Verdadero o falso: la autoría de un proyecto sigue siendo de quien lo creó aunque reciba comentarios.", "Verdadero", "Quien recibe comentarios decide qué cambiar."),
    ],
    (
        "Elige UN proyecto de ejemplo. A) «Lluvia»: ritmo lento coherente con la calma; movimiento cortado en dos momentos. B) «Pasaje»: mensaje de reciclaje claro; letra pequeña; sin cartela. C) «Eco»: voces variadas con permiso; dos relatos bajos; bitácora sin fechas. Escribe una retroalimentación con observo, valoro y sugiero (con un acierto), y una respuesta de la persona autora que mantenga una postura fundada ante una sugerencia que no comparte.",
        "Elegí C. Observo: las voces son variadas y dos se oyen bajo. Valoro: la variedad aporta al propósito de documentar. Sugiero: subir el volumen de esos dos relatos. Respuesta de la autora: gracias; subiré el volumen, pero mantendré el orden de los relatos porque sigue un recorrido del barrio.",
        ["usa observo, valoro y sugiero", "incluye un acierto", "responde con postura fundada", "mantiene el respeto"],
        ["retroalimentación", "respuesta de la persona autora"],
        ["comentar a la persona", "aceptar todo por presión"],
        "Pregunta cómo equilibró el comentario y qué evidencia sostuvo la respuesta.",
    ),
    "Piensa en un comentario que recibiste alguna vez y reescríbelo con observo, valoro y sugiero.",
    "Escribe tres frases para responder con respeto a una sugerencia con la que no estás de acuerdo.",
)
