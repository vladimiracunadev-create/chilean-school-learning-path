"""Comprensión histórica del presente (electivo HC, 3.º y 4.º medio): OAC-03 (preguntas y explicaciones históricas a partir de problemas del presente), clases 1 a 4. Problemas, fuentes y datos ficticios o de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada problema, plan, tabla o borrador está escrito en el enunciado. "
             "Todo es ficticio o de ejemplo (la comuna «Lomas del Sur» y el «Liceo Los Alerces» no existen) y sirve para practicar el método, no para aprender cifras. "
             "Las posturas se presentan con sus razones y sin tomar partido. Si un tema te afecta personalmente, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O3 = "HI-CHDP-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (problemas y preguntas de ejemplo, ficticios). Problema 1: en Lomas del Sur muchas personas mayores viven solas y tienen poco acceso a transporte. "
     "Problema 2: en el Liceo Los Alerces vota poca gente en las elecciones del centro de estudiantes. Problema 3: el estero de la comuna se desborda cada invierno en el sector bajo. "
     "Pregunta a: «¿Hay personas mayores que viven solas en la comuna?» Pregunta b: «¿Cómo ha cambiado, entre 1990 y 2020, la forma en que las personas mayores de Lomas del Sur se movilizan por la comuna, y por qué?» "
     "Pregunta c: «¿Fue buena la política de transporte?»")
build(
    O3, 1, F,
    use="Aprenderé a transformar un problema del presente en una pregunta histórica abierta, acotada e investigable, y a reconocer las categorías de la disciplina (cambio y continuidad, causa y consecuencia, periodización) que la orientan.",
    prior=["Sé contextualizar hechos en tiempo, espacio y actores.", "Sé qué es una fuente y una hipótesis.", "Distingo causas, consecuencias y perspectivas."],
    explain=[
        "Una pregunta histórica nace de un problema del presente, pero busca entenderlo mirando al pasado: ¿cómo se llegó a esta situación?, ¿qué cambió y qué permaneció?, ¿quiénes intervinieron? No se estudia el pasado para justificar el presente, sino porque el presente deja preguntas que solo se comprenden con perspectiva histórica. Puede formularse a escala local (un barrio, una comuna) o nacional.",
        "Una buena pregunta histórica es abierta (no se responde con sí o no), acotada (indica un lugar y un período), investigable (existen fuentes que permiten responderla) y relevante (ayuda a comprender el problema). Una pregunta que pide solo un juicio como «¿fue bueno?» sin criterios, o que ya trae la respuesta, sirve poco para investigar.",
        "La disciplina ofrece categorías para pensar. El cambio y la continuidad preguntan qué se transformó y qué permaneció. La causa y la consecuencia preguntan por qué ocurrió algo y qué efectos tuvo. La periodización divide el tiempo en etapas según un criterio explícito. La perspectiva pregunta desde qué sujeto o enfoque se mira. Una pregunta potente suele combinar dos o tres de estas categorías.",
    ],
    vocab=[("pregunta histórica", "pregunta sobre el pasado que ayuda a comprender un problema del presente"), ("pregunta abierta", "pregunta que no se responde con sí o no"), ("pregunta acotada", "pregunta que indica un lugar y un período"), ("cambio y continuidad", "categoría que pregunta qué se transformó y qué permaneció"), ("periodización", "división del tiempo en etapas según un criterio explícito"), ("investigable", "que existen fuentes para responderla")],
    worked=[
        ("De problema a pregunta", "Problema de ejemplo: «En el barrio hay pocas áreas verdes.» Formula una pregunta histórica.",
         ["Se acota con un lugar y un período: el barrio, entre 1990 y 2020.", "Se pide cambio y causas: ¿cómo cambió y qué decisiones influyeron?"],
         "¿Cómo cambió entre 1990 y 2020 la cantidad de áreas verdes del barrio y qué decisiones influyeron?"),
        ("Evaluar una pregunta", "Pregunta de ejemplo: «¿Quién es el culpable de que se asista poco al consultorio?» ¿Es una buena pregunta histórica?",
         ["Busca un culpable y no un proceso, y se podría responder con un nombre.", "No indica lugar ni período y no es claro qué fuentes servirían."],
         "No: no es abierta, ni acotada ni investigable"),
    ],
    mistakes=[("Formular una pregunta que se responde con sí o no.", "Se confunde preguntar con comprobar un dato.", "Reformula con «cómo», «por qué» o «qué cambió» y agrega lugar y período."),
              ("Usar el pasado para demostrar que el presente era inevitable.", "Se mira la historia como si todo llevara a hoy.", "Pregunta por alternativas, tensiones y decisiones que pudieron ser otras.")],
    T=[
        ("abc", "{F} ¿Qué problema del presente se refiere al liceo?", "El problema 2", "El problema 1", "El problema 3", "El problema 2 trata de la baja votación en el centro de estudiantes."),
        ("abc", "{F} ¿Cuál de las preguntas se responde con sí o no?", "La pregunta a", "La pregunta b", "Ninguna", "«¿Hay personas mayores que viven solas?» admite una respuesta de sí o no."),
        ("abc", "{F} ¿Cuál es la mejor pregunta histórica de las tres?", "La pregunta b: abierta, acotada y que pregunta por cambio y causas", "La pregunta a: es breve", "La pregunta c: es más directa", "La pregunta b cumple con los cuatro rasgos de una buena pregunta histórica."),
        ("abc", "En Comprensión histórica, ¿qué es una pregunta histórica?", "Una pregunta sobre el pasado que ayuda a comprender un problema del presente", "Una pregunta cuya respuesta es una fecha", "Una pregunta sobre el futuro del país", "Conecta un problema actual con su pasado para comprenderlo."),
        ("abc", "{F} ¿Por qué la pregunta c es débil?", "Pide un juicio sin criterios y no acota lugar ni período", "Es demasiado larga", "Contiene demasiados nombres propios", "«Bueno» no se define y no se sabe qué fuentes servirían."),
        ("abc", "{F} ¿Qué acotaciones tiene la pregunta b?", "Lugar (Lomas del Sur) y período (1990 a 2020)", "Solo el lugar", "Ninguna", "Nombra la comuna y las fechas de inicio y término."),
        ("abc", "Una pregunta que indaga «¿qué permaneció igual?» usa la categoría de", "Continuidad", "Consecuencia", "Periodización", "Preguntar por lo que permanece corresponde a la continuidad."),
        ("abc", "Una pregunta que indaga «¿qué efectos tuvo esta decisión?» usa la categoría de", "Consecuencia", "Continuidad", "Perspectiva", "Preguntar por efectos de una decisión corresponde a la categoría de consecuencia."),
        ("abc", "{F} ¿Cuál es una buena pregunta histórica para el problema 2?", "¿Cómo ha cambiado, desde 2010, la participación en las elecciones del centro de estudiantes del liceo y qué factores influyeron?", "¿Vota poca gente en el liceo?", "¿Es malo que voten pocos estudiantes?", "Es abierta, acotada, investigable y pregunta por cambio y causas."),
        ("abc", "{F} ¿Cuál es una buena pregunta histórica para el problema 3?", "¿Cómo se ha poblado el sector bajo del estero desde 1990 y cómo ha enfrentado la comuna los desbordes?", "¿Cuántos esteros hay en Chile?", "¿Por qué llueve en invierno?", "Se centra en la comuna, en un período y en procesos humanos que se pueden investigar."),
        ("abc", "Un compañero dice que su pregunta debe traer la respuesta incluida. ¿Qué le dirías?", "Una pregunta que ya contiene la respuesta no permite investigar", "Tiene razón: así ahorra tiempo", "Solo vale si es de sí o no", "Si la respuesta ya está dada, la investigación no puede descubrir nada."),
        ("abc", "{F} ¿Qué fuentes ayudarían a investigar la pregunta b?", "Registros municipales de recorridos de buses y entrevistas a personas mayores", "Una receta de cocina del barrio", "Un mapa del sistema solar", "Esas fuentes permiten reconstruir cómo se movilizaban las personas mayores en el período."),
        ("abc", "¿Por qué se parte de un problema del presente para formular una pregunta histórica?", "Porque los problemas actuales orientan qué preguntas son relevantes, sin buscar justificar el presente", "Porque el pasado solo sirve para defender las decisiones de hoy", "Porque el pasado no tiene sentido por sí mismo", "El presente aporta la pregunta, pero la respuesta se construye con evidencia del pasado."),
    ],
    ctx=("abc", "En un taller escolar ficticio, un grupo quiere investigar por qué en su barrio hay pocas bibliotecas. Una estudiante propone «¿Por qué no hay bibliotecas?»; otra, «¿Cómo ha cambiado el acceso a bibliotecas en el barrio entre 1990 y hoy y quiénes impulsaron esos cambios?». ¿Cuál conviene y por qué?", "La segunda, porque es abierta, acotada e investigable", "La primera, porque es más corta", "Ninguna, porque no se puede investigar", "La segunda indica lugar, período y categorías de cambio y sujetos."),
    sc=[
        ("En Comprensión histórica: ¿qué cuatro rasgos tiene una buena pregunta histórica?", "Abierta, acotada, investigable y relevante", "Así permite una investigación con fuentes sobre un problema que importa."),
        ("¿Qué pregunta hace la categoría de cambio y continuidad?", "Qué se transformó y qué permaneció", "Mira cuánto y cómo se modificó una situación."),
        ("¿Para qué sirve la periodización?", "Para dividir el tiempo en etapas según un criterio explícito", "Ordena el proceso en fases comprensibles."),
    ],
    op=("Elige un problema de ejemplo. Problema 1: hay poca asistencia de público a las ferias de libros de la comuna. Problema 2: muchas familias del barrio tienen dificultades para acceder a vivienda. Problema 3: hay poca participación juvenil en organizaciones del barrio. "
        "Escribe tres preguntas (una mala, una regular y una buena), explica por qué la buena cumple con ser abierta, acotada, investigable y relevante, y nombra dos fuentes que usarías.",
        "Problema 3. Mala: ¿Hay pocos jóvenes? Regular: ¿Por qué participan pocos? Buena: ¿Cómo cambió entre 2000 y 2020 la participación de jóvenes en organizaciones del barrio y qué factores influyeron? Fuentes: actas de organizaciones y entrevistas a dirigentes.",
        ["formula tres preguntas de distinta calidad", "justifica la buena con los cuatro rasgos", "propone dos fuentes pertinentes"],
        ["tres preguntas con justificación y dos fuentes"],
        ["dejar la pregunta buena sin acotación", "proponer fuentes que no permiten responder", "usar sí o no en la pregunta buena"],
        "Pregunta: «¿qué fuente podría contradecir tu pregunta?». Si no encuentra ninguna, la pregunta está demasiado cerrada."),
    reinforce="Con el problema 1 de la ficha, escribe una pregunta distinta de la b que incluya lugar, período y una categoría de la disciplina.",
    extend="Elige un problema de tu liceo y escribe dos preguntas históricas, una local y otra que lo relacione con un cambio nacional.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (plan de investigación de ejemplo, ficticio). Pregunta: ¿cómo ha cambiado, entre 1990 y 2020, el acceso de las personas mayores de Lomas del Sur a atención de salud cercana? "
     "Hipótesis provisoria: el acceso mejoró cuando se abrió un consultorio en el sector alto, aunque el sector bajo siguió lejos. "
     "Fuentes disponibles: (a) registro del consultorio con las atenciones de personas mayores por año; (b) entrevistas a personas mayores de ambos sectores; (c) un afiche de una campaña de verano; "
     "(d) un mapa de la comuna con la ubicación de los servicios; (e) un acta del consejo comunal sobre el consultorio. Datos de ejemplo del registro (a): atenciones de personas mayores en 1995, 600; en 2005, 900; en 2015, 1.500.")
build(
    O3, 2, F,
    use="Aprenderé la metodología básica de la historia: formular una hipótesis, elegir fuentes pertinentes, leer indicadores con sus límites y revisar la hipótesis cuando la evidencia no la respalda.",
    prior=["Sé formular una pregunta histórica.", "Sé clasificar y interrogar fuentes.", "Sé qué es un indicador y que tiene límites."],
    explain=[
        "Una hipótesis es una respuesta provisoria a la pregunta de investigación, que se pone a prueba con fuentes. No es una verdad ni una opinión: es una guía que se puede confirmar, corregir o descartar. Una buena hipótesis es clara y compatible con la evidencia que se puede encontrar. Si la evidencia la contradice, se reformula; no se descarta la evidencia.",
        "La metodología sigue una secuencia: formular la pregunta, plantear una hipótesis, ubicar fuentes pertinentes, interrogarlas y contrastarlas, y construir una explicación que declare sus límites. Una fuente es pertinente cuando permite responder la pregunta; un afiche de una campaña de verano, por ejemplo, rara vez dice algo sobre el acceso a la salud durante treinta años.",
        "Los indicadores ayudan a medir un aspecto del proceso, como las atenciones por año. Pero cada indicador tiene límites: no distingue cuántas personas distintas se atendieron, ni la calidad de la atención, ni el sector de cada persona. Por eso se combinan indicadores con fuentes cualitativas, como entrevistas, y con documentos que explican decisiones.",
    ],
    vocab=[("hipótesis", "respuesta provisoria a la pregunta que se pone a prueba con fuentes"), ("fuente pertinente", "fuente que permite responder la pregunta de investigación"), ("fuente cualitativa", "fuente que describe experiencias, opiniones o motivos, como una entrevista"), ("contrastar", "comparar fuentes para ver coincidencias y diferencias"), ("reformular", "ajustar una hipótesis o pregunta cuando la evidencia no la respalda"), ("plan de investigación", "secuencia de pasos con pregunta, hipótesis y fuentes")],
    worked=[
        ("Elegir fuentes pertinentes", "Pregunta de ejemplo: ¿cómo cambió el uso de una plaza entre 2000 y 2020? Fuentes: (1) fotografías de la plaza de distintos años; (2) un menú de un café; (3) entrevistas a vecinos. ¿Cuáles son pertinentes?",
         ["Las fotos muestran cómo se usaba la plaza en distintos años.", "Las entrevistas aportan experiencias; el menú del café no se relaciona con el uso de la plaza."],
         "Las fotos y las entrevistas son pertinentes; el menú no"),
        ("Revisar una hipótesis", "Hipótesis de ejemplo: «El uso de la plaza aumentó porque se instaló iluminación.» Las entrevistas indican que la iluminación llegó cuando el uso ya había aumentado. ¿Qué se hace?",
         ["La evidencia contradice la parte causal de la hipótesis: la iluminación vino después.", "Se reformula la hipótesis y se buscan otros factores, como una feria o un nuevo colegio cercano."],
         "Se reformula la hipótesis y se buscan otros factores"),
    ],
    mistakes=[("Defender la hipótesis aunque la evidencia la contradiga.", "Se confunde la hipótesis con una conclusión fija.", "Trátala como respuesta provisoria y reformúlala con lo que muestran las fuentes."),
              ("Elegir fuentes porque son fáciles de conseguir y no porque sean pertinentes.", "Se prioriza la comodidad sobre el objetivo.", "Pregunta qué parte de la pregunta responde cada fuente.")],
    T=[
        ("abc", "En Comprensión histórica, ¿qué es una hipótesis?", "Una respuesta provisoria a la pregunta que se pone a prueba con fuentes", "Una verdad que ya no se discute", "Una opinión sin necesidad de fuentes", "Es una guía de trabajo que se puede confirmar, corregir o descartar."),
        ("abc", "{F} ¿Cuál es la fuente menos pertinente para la pregunta del plan?", "El afiche de una campaña de verano (c)", "El registro del consultorio (a)", "El acta del consejo comunal (e)", "Un afiche de una campaña puntual no dice cómo cambió el acceso en treinta años."),
        ("abc", "{F} ¿Qué fuente permite ubicar la distancia entre los sectores y los servicios?", "El mapa de la comuna (d)", "El registro del consultorio (a)", "Las entrevistas (b)", "El mapa muestra dónde están los servicios y los sectores."),
        ("abc", "{F} ¿Qué fuente muestra experiencias de personas de ambos sectores?", "Las entrevistas (b)", "El mapa (d)", "El registro (a)", "Las entrevistas recogen vivencias de personas de distintos sectores."),
        ("=", "{F} ¿Cuántas atenciones más hubo en 2015 que en 1995, según el registro?", "1500-600", "El aumento se calcula restando las atenciones de 1995 a las de 2015."),
        ("abc", "{F} ¿Qué mide el registro (a)?", "La cantidad de atenciones de personas mayores por año", "La calidad de la atención", "La satisfacción de cada persona", "Cuenta atenciones, pero no distingue personas ni calidad."),
        ("abc", "{F} ¿Qué fuentes apoyan mejor la parte de la hipótesis que dice que el sector bajo siguió lejos?", "El mapa (d) junto con entrevistas (b) del sector bajo", "El afiche (c)", "El registro (a) solo", "El mapa muestra la distancia y las entrevistas muestran cómo se vivió."),
        ("abc", "{F} Un alumno concluye: «Como subieron las atenciones, mejoró el acceso de todas las personas mayores.» ¿Qué es lo más prudente?", "Decir que aumentaron las atenciones, pero falta saber si mejoró el acceso en ambos sectores y para cuántas personas distintas", "Aceptar la conclusión porque hay un aumento", "Descartar el registro porque es un número", "Un indicador de atenciones no prueba por sí solo un mejor acceso para todas las personas."),
        ("=", "{F} ¿En cuántas atenciones fue mayor el aumento de 2005 a 2015 que el de 1995 a 2005?", "(1500-900)-(900-600)", "El aumento del segundo tramo fue 600 y el del primero 300, y la diferencia entre ellos es 300."),
        ("abc", "¿Cuál es el orden correcto de pasos de una investigación histórica?", "Formular la pregunta, plantear una hipótesis, ubicar y contrastar fuentes, construir la explicación", "Plantear una conclusión, buscar fuentes que la confirmen, formular la pregunta", "Reunir fuentes, escribir la conclusión, plantear la pregunta", "La pregunta y la hipótesis guían la búsqueda de fuentes, y la explicación se construye al final."),
        ("abc", "{F} ¿Qué riesgo tiene entrevistar solo a personas mayores del sector alto?", "Sesgo: no representa la experiencia de las personas del sector bajo", "Ninguno, porque todas las personas piensan igual", "Que la entrevista sea demasiado corta", "La hipótesis distingue sectores, así que faltaría una parte de la evidencia."),
        ("abc", "{F} ¿Qué aporta el acta del consejo comunal (e)?", "Las decisiones y argumentos que explican por qué se abrió el consultorio", "La cantidad de atenciones por año", "La distancia entre los sectores", "Un acta registra qué se decidió y por qué."),
        ("abc", "Si una fuente contradice la hipótesis, lo correcto es", "Reformular la hipótesis a partir de la evidencia", "Ignorar la fuente", "Cambiar la pregunta sin explicarlo", "La hipótesis es provisoria y se ajusta cuando la evidencia la contradice."),
    ],
    ctx=("abc", "Un grupo del Liceo Los Alerces investiga cómo cambió el uso de la biblioteca escolar entre 2005 y 2020. Dispone de: libros de préstamos por año, entrevistas a la bibliotecaria, fotos de eventos y el reglamento de 2010. ¿Qué plan de fuentes es más sólido?", "Combinar préstamos por año (indicador), entrevistas (experiencia) y reglamento (decisiones)", "Usar solo las fotos de eventos", "Usar solo el reglamento", "Cada tipo de fuente responde a un aspecto distinto de la pregunta."),
    sc=[
        ("En Comprensión histórica: ¿qué se hace si la evidencia contradice la hipótesis?", "Se reformula la hipótesis", "La hipótesis es provisoria y se ajusta con las fuentes."),
        ("¿Cuándo una fuente es pertinente?", "Cuando permite responder la pregunta de investigación", "La pertinencia depende de la pregunta, no de la facilidad."),
        ("¿Por qué se combinan indicadores con entrevistas?", "Porque los indicadores miden un aspecto y las entrevistas explican experiencias y motivos", "Cada tipo de fuente cubre los límites del otro."),
    ],
    op=("Arma un plan de investigación con esta pregunta de ejemplo: ¿cómo ha cambiado, entre 2000 y 2020, el uso de las bicicletas para ir al liceo en una comuna? "
        "Fuentes disponibles: (a) conteo de bicicletas estacionadas en el liceo cada año (2000: 10, 2010: 35, 2020: 80); (b) entrevistas a estudiantes de distintas generaciones; (c) un plano de ciclovías de la comuna; (d) un afiche de una fiesta de la bicicleta; (e) un acta del liceo sobre estacionamientos. "
        "Escribe una hipótesis, elige tres fuentes pertinentes con una razón, dos límites del conteo (a) y qué harías si la evidencia no respalda tu hipótesis.",
        "Hipótesis: el uso aumentó cuando se construyeron ciclovías. Fuentes: (a) por la evolución de 10 a 80; (b) por las razones; (c) por la fecha de las ciclovías. Límites de (a): no dice cuántas personas distintas, ni cuántas vienen de lejos. Si no se respalda, reformularía la hipótesis.",
        ["formula una hipótesis coherente con la pregunta", "elige fuentes pertinentes y justifica", "señala dos límites del indicador", "describe cómo ajustaría la hipótesis"],
        ["plan con hipótesis, tres fuentes con razón, dos límites y una nota de ajuste"],
        ["elegir el afiche como fuente principal", "no declarar límites del conteo", "hacer una hipótesis que no puede ponerse a prueba"],
        "Pregunta: «¿qué dato te haría cambiar tu hipótesis?». Si no hay ninguno, la hipótesis es demasiado rígida."),
    reinforce="Escribe una hipótesis para la pregunta de la ficha 2 distinta de la que aparece y di qué fuente la pondría a prueba.",
    extend="Explica por qué un indicador numérico y una entrevista pueden llevar a conclusiones distintas y cómo resolverías esa diferencia.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (datos y hechos de ejemplo, ficticios). Porcentaje de estudiantes que votó en las elecciones del centro de estudiantes del Liceo Los Alerces: 2008, 30 %; 2012, 28 %; 2016, 52 %; 2020, 60 %. "
     "Hechos del liceo: en 2014 se instaló una urna en cada sala; en 2015 el liceo comenzó a publicar las propuestas de cada lista; en todos los años la votación se hizo en horario de clases. "
     "Explicación 1: la urna en cada sala facilitó votar. Explicación 2: la publicación de las propuestas aumentó el interés.")
build(
    O3, 3, F,
    use="Aprenderé a construir una explicación histórica con varias causas, a distinguir cambio y continuidad y a periodizar un proceso con un criterio explícito.",
    prior=["Sé formular preguntas e hipótesis históricas.", "Distingo causas estructurales y coyunturales.", "Sé leer un indicador con sus límites."],
    explain=[
        "Una explicación histórica responde a una pregunta mostrando cómo y por qué ocurrió un proceso. Rara vez tiene una sola causa: se habla de multicausalidad. Además de las causas, se distinguen los cambios de las continuidades, porque en un mismo proceso algunas cosas se transforman y otras se mantienen. Reconocer ambas evita la idea de que todo cambió o de que nada cambió.",
        "La periodización divide el proceso en etapas. Para hacerlo se necesita un criterio explícito: por ejemplo, antes y después de una decisión importante, o según el nivel de un indicador. Distintos criterios producen distintas periodizaciones, y esa elección debe justificarse. Una etapa no es un hecho de la realidad, sino una herramienta para ordenar y comprender.",
        "Cuando dos hechos ocurren casi a la vez y ambos podrían explicar un cambio, no se puede repartir la influencia sin más evidencia. Lo prudente es decir que coinciden con el cambio, que no se puede saber cuánto aportó cada uno y proponer qué fuente ayudaría, como entrevistas que expliquen por qué la gente actuó de una u otra manera.",
    ],
    vocab=[("multicausalidad", "idea de que un proceso tiene varias causas"), ("cambio", "aspecto de una situación que se transformó"), ("continuidad", "aspecto de una situación que permaneció"), ("periodización", "división del proceso en etapas según un criterio"), ("criterio de periodización", "razón que se usa para decidir dónde empieza y termina una etapa"), ("coincidir", "ocurrir al mismo tiempo, sin que eso pruebe una relación causal")],
    worked=[
        ("Cambio y continuidad", "Un club de lectura de ejemplo pasó de 15 a 40 integrantes entre 2005 y 2020, pero siguió reuniéndose los jueves en la misma sede. ¿Qué cambió y qué permaneció?",
         ["Cambió el número de integrantes: aumentó.", "Permaneció el día de reunión y la sede."],
         "Cambió: la cantidad de integrantes; continuidad: el día y la sede"),
        ("Periodizar con un criterio", "En una comuna de ejemplo, la tasa de reciclaje fue baja hasta 2012, año en que se instalaron contenedores, y alta después. Propón dos etapas.",
         ["El criterio es la instalación de los contenedores.", "Etapa 1: hasta 2012; etapa 2: desde 2012."],
         "Etapa 1: hasta 2012; etapa 2: desde 2012, con el criterio de la instalación de contenedores"),
    ],
    mistakes=[("Atribuir un cambio al hecho que ocurrió justo antes sin considerar otros factores.", "Se confunde la secuencia con la causa.", "Busca otras posibles causas y evidencia de cómo cada una habría actuado."),
              ("Presentar las etapas como si fueran divisiones naturales.", "Se olvida que el criterio lo elige quien investiga.", "Explica el criterio de periodización y reconoce que otro habría servido.")],
    T=[
        ("abc", "{F} ¿En qué año fue mayor la participación según la tabla?", "2020, con 60 %", "2008, con 30 %", "2016, con 52 %", "El 60 % es el valor más alto de la serie."),
        ("=", "{F} ¿Cuántos puntos subió la participación entre 2012 y 2016?", "52-28", "Se resta el porcentaje de 2012 al de 2016."),
        ("abc", "{F} ¿Qué se mantuvo igual en todos los años?", "Que la votación se hizo en horario de clases", "La participación", "La existencia de una urna en cada sala", "La ficha indica que la votación siempre fue en horario de clases."),
        ("abc", "{F} ¿Qué cambió en el liceo a partir de 2014 y 2015?", "Se instalaron urnas en cada sala y se publicaron las propuestas", "Se cambió la fecha de la votación", "Se cerró el centro de estudiantes", "Son los dos hechos que la ficha presenta como novedades."),
        ("abc", "{F} ¿Qué criterio de periodización es razonable?", "Antes y después de los cambios de 2014 y 2015", "Por décadas calendario, sin relación con lo ocurrido en el liceo", "Una etapa por cada año medido, sin un criterio común", "El criterio se basa en hechos que pudieron influir en el proceso."),
        ("abc", "{F} Las explicaciones 1 y 2 son", "Causas de tipo coyuntural: decisiones puntuales del liceo", "Causas estructurales de larga duración", "Consecuencias del aumento de votantes", "Una urna nueva y una publicación son decisiones concretas y cercanas en el tiempo."),
        ("abc", "{F} ¿Qué dato muestra el salto más grande de la serie?", "El paso de 28 % en 2012 a 52 % en 2016", "El paso de 30 % a 28 %", "El paso de 52 % a 60 %", "Son 24 puntos, mayores que los otros cambios entre medidas."),
        ("abc", "{F} Un estudiante dice: «La urna en cada sala explica todo.» ¿Qué falta considerar?", "Que la publicación de propuestas ocurrió casi al mismo tiempo y también pudo influir", "Que la votación fue en horario de clases", "Que la tabla tiene cuatro años", "Dos hechos coinciden con el cambio y no se puede atribuir todo a uno."),
        ("abc", "{F} ¿Qué evidencia ayudaría a distinguir entre las explicaciones 1 y 2?", "Entrevistas o encuestas a estudiantes sobre por qué votaron", "Otra tabla con los mismos porcentajes", "La lista de los nombres de las listas", "Los motivos de las personas aportan información que el porcentaje no tiene."),
        ("abc", "{F} ¿Cuál frase recoge cambio y continuidad?", "La participación creció, aunque la votación siguió realizándose en horario de clases", "La participación creció y todo cambió", "Nada cambió en el liceo", "Menciona un cambio y una continuidad del mismo proceso."),
        ("abc", "{F} ¿Cuál es una conclusión prudente?", "La participación pasó de 30 % a 60 % entre 2008 y 2020 y coincide con dos cambios del liceo, pero los datos no permiten decir cuánto aportó cada uno", "La urna causó exactamente la mitad del aumento", "Los estudiantes de hoy son más responsables que los de antes", "Reconoce la coincidencia y declara lo que no se puede afirmar."),
        ("abc", "Si en el país entero también aumentó la participación juvenil en el mismo período, ¿qué conviene hacer en el estudio del liceo?", "Considerar si el aumento local se debe a factores locales, nacionales o a ambos", "Ignorar el dato nacional", "Afirmar que el liceo causó el cambio nacional", "Relacionar escalas evita atribuir todo a un solo nivel."),
        ("abc", "¿Por qué la multicausalidad hace más completa una explicación?", "Porque reconoce que varias causas pudieron actuar a la vez", "Porque obliga a escribir textos más largos", "Porque permite no usar evidencia", "Un proceso social rara vez tiene una única causa."),
    ],
    ctx=("abc", "En una comuna ficticia, el uso de la biblioteca pública subió después de que se amplió el horario y también después de que se abrió una escuela cercana. La alcaldesa dice que fue por el nuevo horario. ¿Qué respuesta histórica es más rigurosa?", "Ambos hechos pudieron influir; se necesitan datos de los usuarios para saber cuánto aportó cada uno", "Fue solo por el horario, porque lo dijo la autoridad", "Fue solo por la escuela, porque está más cerca", "Hay dos causas posibles y se requiere evidencia para distinguirlas."),
    sc=[
        ("En Comprensión histórica: ¿qué es la continuidad?", "Un aspecto de una situación que permaneció", "Se contrasta con el cambio al analizar un proceso."),
        ("¿Qué necesita una periodización para ser útil?", "Un criterio explícito y justificado", "Las etapas son herramientas, no hechos naturales."),
        ("¿Qué se dice cuando dos hechos coinciden con un cambio y no hay evidencia para separarlos?", "Que coinciden con el cambio, pero no se puede decir cuánto aportó cada uno", "Así se evita atribuir una causa sin prueba."),
    ],
    op=("Elige un caso de ejemplo. Caso 1: el uso del transporte público en una comuna subió de 20 % a 45 % de los viajes entre 2005 y 2020; en 2012 se rebajó la tarifa a estudiantes y en 2014 se abrió una línea nueva; los horarios de funcionamiento no cambiaron. "
        "Caso 2: la matrícula en talleres artísticos de un liceo subió de 40 a 110 entre 2010 y 2020; en 2013 se contrató a un profesor de música y en 2016 se compraron instrumentos; los talleres siguieron siendo gratuitos. "
        "Escribe una periodización con su criterio, un cambio y una continuidad, dos causas posibles y una conclusión prudente.",
        "Caso 2. Etapas: 2010–2013, 2013–2016 y 2016–2020 según contratación y compra. Cambio: la matrícula; continuidad: la gratuidad. Causas: el profesor y los instrumentos. Conclusión: coincide con dos mejoras; faltan entrevistas para saber cuál motivó más.",
        ["propone una periodización con criterio explícito", "distingue un cambio y una continuidad", "plantea dos causas posibles", "redacta una conclusión prudente"],
        ["tabla con etapas, criterio, cambio, continuidad, causas y conclusión"],
        ["periodizar sin criterio", "atribuir todo a una sola causa", "confundir continuidad con falta de cambio en el dato principal"],
        "Pregunta: «¿por qué cortaste el tiempo en esos años y no en otros?»."),
    reinforce="Con la tabla de la ficha 3, escribe una periodización distinta de la propuesta y explica su criterio.",
    extend="Explica una situación de tu liceo en la que algo cambió y algo permaneció, y por qué ambas cosas son importantes para explicarla.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (borrador de explicación, ejemplo). Pregunta: ¿cómo cambió la participación en las elecciones del centro de estudiantes del Liceo Los Alerces entre 2008 y 2020? "
     "Borrador de un estudiante: «La participación subió de 30 % a 60 %. La urna en cada sala y la publicación de las propuestas lo explican totalmente, y por eso todos los liceos del país deberían hacer lo mismo. "
     "Hoy los estudiantes son más responsables que antes.»")
build(
    O3, 4, F,
    use="Aprenderé a redactar una explicación histórica con pregunta, tesis, evidencia y límites, y a detectar errores frecuentes: absolutos, generalización desde un caso, valoraciones sin evidencia y relaciones mal planteadas entre escala local y nacional.",
    prior=["Sé formular preguntas, hipótesis y periodizaciones.", "Distingo cambio y continuidad.", "Sé que las conclusiones deben declarar sus límites."],
    explain=[
        "Una explicación histórica bien construida tiene cuatro partes: una pregunta clara, una tesis que responde esa pregunta, argumentos apoyados en evidencia de fuentes y un reconocimiento de los límites. La tesis es lo que se defiende, y los argumentos muestran cómo la evidencia la sostiene. Los límites indican qué no se puede afirmar con lo que se tiene, y por eso fortalecen la explicación.",
        "Hay errores frecuentes. Los absolutos, como «totalmente» o «siempre», afirman más de lo que la evidencia permite. La generalización desde un caso extiende lo observado en un lugar a todo el país. Las valoraciones sin evidencia, como «los estudiantes son más responsables», mezclan un juicio con un dato. Y hay que evitar mirar el pasado solo para explicar cómo se llegó a hoy, como si no hubiera existido otro camino.",
        "La relación entre escala local y nacional es una herramienta, no una jerarquía. Un caso local puede ilustrar un proceso nacional, pero no lo representa por sí solo, y un proceso nacional puede manifestarse de modo distinto en cada comuna. Una explicación sólida dice qué parte de su conclusión vale para el caso estudiado y qué habría que investigar para ampliarla.",
    ],
    vocab=[("tesis", "afirmación central que se defiende con evidencia"), ("argumento", "razón apoyada en evidencia que sostiene la tesis"), ("límite", "aquello que no puede afirmarse con la evidencia disponible"), ("generalización", "extender lo observado en un caso a muchos otros"), ("valoración", "juicio sobre algo, que no es un dato comprobable"), ("escala", "nivel de estudio: barrio, comuna, región o país")],
    worked=[
        ("Reescribir un absoluto", "Frase de ejemplo: «La nueva biblioteca explica totalmente que lean más.» Reescríbela moderando el absoluto.",
         ["Se cambia «explica totalmente» por un verbo de certeza moderada.", "Se señala que coincide con el aumento, sin afirmar que sea la única causa."],
         "La apertura de la biblioteca coincide con un aumento de la lectura y pudo contribuir a él"),
        ("Separar dato y valoración", "Frase de ejemplo: «Las ventas aumentaron un 20 % porque la gente es más trabajadora.» ¿Qué parte es dato y cuál valoración?",
         ["«Aumentaron un 20 %» es un dato comprobable.", "«La gente es más trabajadora» es una valoración sin evidencia."],
         "Dato: aumento de 20 %; valoración: la gente es más trabajadora"),
    ],
    mistakes=[("Cerrar la explicación con una generalización a todo el país a partir de un caso.", "Se confunde ilustrar con demostrar.", "Indica qué vale para el caso y qué habría que investigar para ampliarlo."),
              ("Introducir juicios de valor sobre las personas sin evidencia.", "Se mezcla lo que se piensa con lo que se muestra.", "Retira la valoración o apóyala con fuentes y criterios explícitos.")],
    T=[
        ("abc", "{F} ¿Qué dato de evidencia incluye el borrador?", "Que la participación subió de 30 % a 60 %", "Que hay una urna en cada sala de todos los liceos", "Que los estudiantes son más responsables", "Es el único dato comprobable que cita con cifras."),
        ("abc", "{F} ¿Qué dos factores propone el borrador como explicación?", "La urna en cada sala y la publicación de las propuestas", "La edad de los votantes y el clima", "El horario y el número de listas", "Son los factores que el borrador nombra."),
        ("abc", "{F} ¿Qué problema tiene la palabra «totalmente» en el borrador?", "Es un absoluto que la evidencia no permite sostener", "Es una palabra que no existe", "Está en la frase equivocada", "Un absoluto afirma más de lo que los datos muestran."),
        ("abc", "{F} ¿Qué error muestra la frase «todos los liceos del país deberían hacer lo mismo»?", "Generalizar desde un solo caso", "Usar una fuente primaria", "Citar un porcentaje sin fecha", "Un caso no basta para recomendar lo mismo a todo el país."),
        ("abc", "{F} ¿Qué tipo de afirmación es «los estudiantes son más responsables que antes»?", "Una valoración sin evidencia", "Un dato comprobable", "Una hipótesis con fuentes", "Habla de un juicio sobre las personas que el borrador no respalda."),
        ("abc", "{F} ¿Cuál es la mejor reescritura de la segunda frase del borrador?", "La urna en cada sala y la publicación de las propuestas coinciden con el aumento y pudieron contribuir a él", "La urna y las propuestas son las únicas causas", "La urna y las propuestas no influyeron", "Usa un verbo moderado y reconoce que son posibles causas."),
        ("abc", "¿Cuál es el orden de las cuatro partes de una explicación histórica?", "Pregunta, tesis, argumentos con evidencia y límites", "Límites, evidencia, pregunta y tesis", "Tesis, valoración, pregunta y fuentes", "Se parte de la pregunta, se responde con una tesis, se sostiene con evidencia y se declaran los límites."),
        ("abc", "{F} ¿Cuál es una tesis adecuada para la pregunta de la ficha?", "Entre 2008 y 2020 la participación en el liceo aumentó y coincidió con dos cambios de procedimiento, aunque no se puede atribuir el aumento a uno solo", "Los estudiantes son mejores", "Todos los liceos mejoran con urnas", "Responde la pregunta con el lugar y el período, y reconoce un límite."),
        ("=", "{F} Si el liceo se hubiera propuesto llegar a 75 % de participación en 2020, ¿cuántos puntos faltaron?", "75-60", "Se resta lo logrado a la meta."),
        ("abc", "{F} Para sostener que la urna influyó, ¿qué fuente agregarías?", "Entrevistas a estudiantes sobre si les resultó más fácil votar con la urna en la sala", "Una lista de los nombres de las listas", "El horario de clases", "Los motivos de las personas aportan evidencia sobre el mecanismo."),
        ("abc", "Un caso local puede relacionarse con un proceso nacional de la siguiente manera:", "Puede ilustrarlo, pero no lo representa por sí solo", "Lo demuestra por completo", "No tiene ninguna relación", "El caso aporta una muestra concreta, y para generalizar se necesitan más casos."),
        ("abc", "{F} ¿Qué límite agregarías a la explicación?", "Los datos corresponden a un solo liceo y no permiten extender la conclusión al país", "Que los estudiantes deberían votar más en el futuro", "Que el porcentaje de 2008 es menor que el de 2020", "Declara el alcance real de la evidencia."),
        ("abc", "¿Cuál de estos rasgos hace más sólida una explicación histórica?", "Declarar los límites de la evidencia", "Evitar citar datos", "Escribir en un tono rotundo", "Mostrar hasta dónde llega la evidencia permite revisarla y confiar en ella."),
    ],
    ctx=("abc", "Una alumna presenta su explicación sobre el aumento de usuarios de una plaza y escribe: «Siempre fue un lugar abandonado y ahora todos la quieren». Su profesor le pide mejorarla. ¿Qué cambio es más útil?", "Reemplazar «siempre» y «todos» por datos del período y una fuente, y declarar sus límites", "Agregar más adjetivos", "Quitar la pregunta de investigación", "Los absolutos se reemplazan por evidencia acotada."),
    sc=[
        ("En Comprensión histórica: ¿cuáles son las cuatro partes de una explicación histórica?", "Pregunta, tesis, argumentos con evidencia y límites", "Juntas, permiten una explicación clara y revisable."),
        ("¿Por qué «siempre» y «todos» suelen ser un problema?", "Porque afirman más de lo que la evidencia permite", "Son absolutos que casi nunca se pueden sostener."),
        ("¿Por qué un caso local no basta para afirmar algo sobre todo el país?", "Porque es una generalización desde un solo caso", "Para ampliar la conclusión se necesitan más casos."),
    ],
    op=("Revisa este borrador de ejemplo: «En la comuna de Costa Verde (ficticia) aumentó el uso de bicicletas porque la gente se volvió más sana. Las ciclovías de 2015 explican todo, y por eso todo Chile debe construir ciclovías.» "
        "Datos de ejemplo: el uso pasó de 5 % a 18 % de los viajes entre 2010 y 2020; en 2015 se abrieron ciclovías; en 2018 subió el precio de la bencina. Escribe los tres errores del borrador, una versión corregida con tesis, evidencia, una causa más y un límite.",
        "Errores: valoración sin evidencia (más sana), absoluto (explican todo) y generalización (todo Chile). Versión: «Entre 2010 y 2020 el uso de bicicletas en Costa Verde pasó de 5 % a 18 %. Coincide con las ciclovías de 2015 y con el alza de la bencina de 2018, y los datos no permiten decir cuánto aportó cada uno; el caso no representa al país.»",
        ["identifica los tres errores", "reescribe con tesis acotada", "usa dos causas posibles y evidencia", "incluye un límite"],
        ["lista de errores y párrafo corregido"],
        ["mantener un absoluto", "dejar una valoración sin evidencia", "olvidar el límite de escala"],
        "Pregunta: «¿qué frase de tu versión corregida se puede comprobar con los datos?»."),
    reinforce="Escribe una explicación de cuatro líneas sobre un cambio de tu barrio con pregunta, tesis, un dato de ejemplo y un límite.",
    extend="Compara dos explicaciones de ejemplo sobre un mismo cambio y escribe cuál tiene mejor estructura y por qué.",
)
