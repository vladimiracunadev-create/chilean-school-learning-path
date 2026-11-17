"""Química (electivo 3.º y 4.º medio HC): OAC-07 (integración de la química con otras ciencias e implicancias éticas, sociales y ambientales, clases 1 a 4)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, cuaderno y calculadora simple. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado o en la ficha de la clase. Los valores de referencia son inventados para practicar y no reemplazan normas oficiales. "
             "Este cuaderno no propone experimentos, mezclas ni procedimientos con sustancias: los resultados que se analizan vienen ya escritos y los cálculos se hacen en papel. "
             "Los casos presentan argumentos de varias personas sin tomar partido por una postura; si un tema te afecta o te preocupa, conversa con una persona adulta de confianza y con tu docente.")
build = make_build(MATERIALS)

O7 = "CN-QUIM-3y4-OAC-07"

# ============================================================ OAC-07, clase 1
F = ("Ficha 1 (caso de ejemplo). Una localidad de ejemplo con 100 familias (400 habitantes) tiene agua con un contaminante X de origen industrial. Aportes de cada disciplina: la química identifica y mide X y propone tratamientos; la biología estudia sus efectos en organismos y personas; la física explica cómo se mueve el agua y cómo funciona un filtro; "
     "la matemática calcula concentraciones, dosis y costos; las ciencias sociales y la economía estudian quién se ve afectado y cuánto cuesta una medida; la ética pregunta qué es justo. "
     "Preguntas de ejemplo: P1 «¿Cómo se soluciona el problema del agua?». P2 «¿Cómo se puede reducir el contaminante X en el agua de la localidad, a qué costo por familia y con qué impacto ambiental?». P3 «¿Qué ciencia es la más importante?». Costo de una medida de ejemplo: 5.000 unidades monetarias de ejemplo.")
build(
    O7, 1, F,
    use="Aprenderé a delimitar un problema actual que necesita química y otras ciencias a la vez, y a formular una pregunta que incluya sus implicancias éticas, sociales y ambientales. Sirve para valorar por qué ninguna disciplina resuelve sola un problema real.",
    prior=["Sé qué aporta la química a la medición de contaminantes.", "Sé calcular costos por persona o familia.", "Sé formular una pregunta delimitada."],
    explain=[
        "Los problemas reales, como el agua contaminada de una localidad, rara vez se resuelven con una sola ciencia. La química identifica y mide la sustancia y propone cómo tratarla. La biología estudia los efectos sobre los organismos. La física explica el movimiento del agua y el funcionamiento de los equipos. La matemática calcula concentraciones, dosis y costos. Las ciencias sociales y la economía muestran quién se ve afectado y cuánto cuesta cada opción.",
        "Además, toda solución tiene implicancias que van más allá de lo técnico. Las implicancias ambientales son los efectos sobre los ecosistemas, como los residuos que deja un tratamiento. Las sociales son los efectos sobre las personas y la comunidad, como quién accede al agua segura. Las éticas son las preguntas sobre lo justo: quién decide, quién se beneficia y quién asume los riesgos y los costos.",
        "Para investigar, se delimita una pregunta que nombre el sistema, la variable que se mide y las dimensiones que se evaluarán. «¿Cómo se soluciona el problema?» es demasiado amplia, y «¿qué ciencia es la más importante?» no tiene respuesta con datos, porque las ciencias se complementan. Integrar conocimientos significa usar el aporte de cada una para ver el problema completo.",
    ],
    vocab=[("integración de conocimientos", "uso conjunto de los aportes de varias ciencias para un mismo problema"), ("implicancia ambiental", "efecto sobre los ecosistemas"), ("implicancia social", "efecto sobre las personas y la comunidad"), ("implicancia ética", "pregunta sobre lo justo en una decisión"), ("equidad", "reparto justo de beneficios, costos y riesgos")],
    worked=[
        ("Aporte de cada disciplina", "En el caso de la ficha, ¿qué disciplina estudia los efectos de la sustancia X en las personas y los organismos?",
         ["La química mide y trata la sustancia.", "El efecto sobre seres vivos es el campo de la biología.", "Esa es la disciplina que estudia los efectos."],
         "La biología"),
        ("Costo por familia", "Otra localidad de ejemplo con 200 familias evalúa una medida de 8.000 unidades. ¿Cuánto cuesta por familia?",
         ["Costo total: 8.000.", "Familias: 200.", "8.000 ÷ 200 = 40."],
         "40 unidades por familia"),
    ],
    mistakes=[("Pensar que una sola ciencia puede resolver un problema real.", "Cada ciencia ve una parte; sin las otras faltan efectos, costos o consecuencias.", "Escribe qué aporta cada disciplina."),
              ("Considerar solo lo técnico y olvidar lo ético y social.", "Una solución puede funcionar y aun así ser injusta o dañar al ambiente.", "Agrega preguntas sobre quién se beneficia y quién asume costos y riesgos.")],
    T=[
        ("abc", "En Química: ¿qué significa integrar los conocimientos de varias ciencias en un problema?", "Usar el aporte de cada ciencia para analizar distintas partes del problema y proponer una solución más completa", "Que cada ciencia opine sin datos", "Elegir una sola ciencia y descartar las demás", "Integrar es combinar los aportes complementarios de cada ciencia."),
        ("{F} ¿Qué disciplina identifica y mide el contaminante X?", "La química", "La ficha indica que la química identifica y mide la sustancia y propone tratamientos."),
        ("{F} ¿Qué disciplina explica cómo se mueve el agua y cómo funciona un filtro?", "La física", "La ficha asigna a la física el movimiento del agua y el funcionamiento de los equipos."),
        ("=", "{F} ¿Cuánto cuesta por familia la medida de ejemplo?", "5000/100", "Se divide el costo total por el número de familias de la localidad.", " unidades por familia"),
        ("=", "{F} Si el costo de la medida se reparte entre los 400 habitantes, ¿cuánto es por habitante?", "5000/400", "Se divide el costo total por el número de habitantes.", " unidades por habitante"),
        ("abc", "{F} ¿Por qué P2 está mejor delimitada que P1?", "Porque nombra la sustancia, el costo por familia y el impacto ambiental, que son aspectos que se pueden evaluar", "Porque es más corta", "Porque no usa números", "P2 nombra el sistema y las dimensiones por evaluar."),
        ("abc", "{F} ¿Qué problema tiene P3 «¿Qué ciencia es la más importante?»?", "No se puede responder con datos y las ciencias se complementan", "Que nombra la química", "Que es demasiado específica", "Una pregunta delimitada necesita variables evaluables."),
        ("abc", "{F} ¿Qué aporta la matemática en este caso?", "Calcular concentraciones, dosis y costos", "Decidir qué es justo", "Estudiar los efectos en los organismos", "Los cálculos son el aporte de la matemática."),
        ("ab", "{F} ¿Qué aporta la ética al análisis?", "Preguntar quién decide, quién se beneficia y quién asume los riesgos", "Medir la concentración del contaminante", "La ética no mide, sino que cuestiona lo justo de una decisión."),
        ("abc", "Un equipo propone instalar un filtro sin consultar a la comunidad. ¿Qué dimensión del análisis falta?", "La social y la ética", "La física únicamente", "Ninguna", "Una solución también debe considerar a las personas afectadas y su participación."),
        ("abc", "{F} ¿Qué variable permitiría evaluar el impacto ambiental de una medida?", "La cantidad de residuos que genera y cómo se manejan", "El color del equipo", "La cantidad de habitantes del país", "Los residuos son un efecto ambiental medible."),
        ("abc", "{F} Un estudiante dice: «como el problema es de agua, solo importa la química». ¿Qué respondes?", "La química mide y trata, pero hacen falta biología, matemática, ciencias sociales y ética para decidir con justicia", "Tiene razón: la química basta", "La química no sirve para el agua", "El problema tiene dimensiones biológicas, sociales y éticas además de la química."),
        ("abc", "{F} Un grupo propone solo filtrar el agua; otro propone filtrar, estudiar los efectos en la salud y consultar a la comunidad. ¿Cuál integra mejor los conocimientos?", "El segundo, porque suma química, biología, ciencias sociales y ética", "El primero, porque la química basta", "Ninguno, porque integrar es imposible", "Integrar es sumar los aportes de varias disciplinas y la voz de las personas afectadas."),
    ],
    ctx=("abc", "Contexto: tu curso debe preparar una exposición sobre un problema de contaminación de agua en una localidad. ¿Qué plan integra mejor los conocimientos?", "Medir la sustancia (química), estudiar sus efectos (biología), calcular costos (matemática) y consultar a la comunidad (ciencias sociales y ética)", "Medir la sustancia y dar la solución", "Pedir opinión a una sola persona", "El plan integrador combina el aporte de varias disciplinas y la participación de las personas."),
    sc=[
        ("En Química: ¿qué es una implicancia ética?", "Una pregunta sobre lo justo en una decisión", "Considera quién decide, quién se beneficia y quién asume los riesgos."),
        ("ab", "Una implicancia ambiental es:", "Un efecto sobre los ecosistemas", "El precio de un equipo", "El ambiente incluye ecosistemas, como los residuos que afectan un río."),
        ("ab", "Una pregunta bien delimitada:", "Nombra el sistema y variables evaluables", "Abarca todos los problemas del mundo", "Delimitar el sistema permite responder la pregunta con datos."),
    ],
    op=("Con el caso de la ficha {F}: (1) escribe una pregunta delimitada que incluya el contaminante, un aspecto de costo y un aspecto ambiental; (2) indica dos disciplinas y qué aportaría cada una; (3) escribe una pregunta ética sobre el caso.",
        "(1) ¿Cómo se puede reducir el contaminante X en el agua de la localidad, a qué costo por familia y con qué residuos? (2) Química: medir X y proponer el tratamiento; biología: estudiar efectos en las personas. (3) ¿Quién debe pagar la medida y quién asume el riesgo mientras se espera?",
        ["pregunta con contaminante, costo y aspecto ambiental", "dos disciplinas con su aporte", "pregunta ética"],
        ["tres respuestas numeradas"],
        ["pregunta demasiado amplia", "disciplinas sin aporte concreto", "pregunta ética que ya trae la respuesta"],
        "Pregunta: «¿qué otra disciplina agregarías al análisis?»."),
    reinforce="Haz una tabla con las seis disciplinas de la ficha y escribe, en una frase, qué aporta cada una al caso.",
    extend="Explica por qué una solución técnicamente eficaz puede ser socialmente injusta, con un ejemplo del caso de la ficha.",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 2 (datos de ejemplo). Proyecto de ejemplo para producir un material para baterías. Método 1: usa 500 L de agua por kg de material. Método 2: usa 200 L de agua por kg. Producción anual de ejemplo: 1.000 kg. "
     "Fuente A: informe técnico de un equipo independiente, con método, datos y supuestos publicados. Fuente B: folleto de la empresa que dice «agua casi sin consumo», sin datos. Fuente C: relato de habitantes de una comunidad vecina, que observan que el nivel de su pozo bajó desde que comenzó el proyecto (testimonio, sin medición). "
     "Variables: método, agua usada, producción y clima. Conflicto de interés: situación en que quien informa gana o pierde con el resultado.")
build(
    O7, 2, F,
    use="Aprenderé a evaluar fuentes de distintas disciplinas y a reconocer variables y conflictos de interés en un problema que integra química, ciencias de la Tierra, economía y comunidad. Sirve para valorar tanto los datos medidos como los testimonios, cada uno con sus límites.",
    prior=["Sé qué es una variable independiente y dependiente.", "Sé evaluar una fuente por su método y sus datos.", "Sé calcular un cambio porcentual."],
    explain=[
        "En un problema que integra varias ciencias llegan fuentes de distinto tipo. Un informe técnico independiente entrega mediciones, métodos y supuestos que otras personas pueden revisar. Un folleto de una empresa puede tener un interés económico en el resultado, lo que se llama conflicto de interés. Un relato de una comunidad es un testimonio: no es una medición, pero señala efectos locales importantes que deben investigarse con datos.",
        "Para comparar alternativas se identifican las variables. La variable independiente es la que cambia, aquí el método de producción. La variable dependiente es la que se mide, aquí el agua usada. Se mantienen controladas la producción y el clima para que la comparación sea justa. Por ejemplo, con 400 L por kg y 2.000 kg al año, un método usa 800.000 L.",
        "Un resultado favorable en un indicador no resuelve todo. Aunque el método 2 usa menos agua, su efecto en el pozo de la comunidad depende de cuánta agua hay disponible y cuánto se recarga, y eso requiere ciencias de la Tierra. Una conclusión honesta dice qué muestran los datos, qué testimonios piden verificarse y qué información falta.",
    ],
    vocab=[("conflicto de interés", "situación en que quien informa gana o pierde con el resultado"), ("testimonio", "relato de una persona sobre lo que observó, sin medición"), ("informe independiente", "estudio hecho por quien no gana ni pierde con el resultado"), ("variable controlada", "la que se mantiene igual para comparar con justicia"), ("indicador", "variable que resume un aspecto de un problema")],
    worked=[
        ("Agua anual de un método", "Un método de ejemplo usa 300 L de agua por kg y la producción es de 1.000 kg al año. ¿Cuántos litros usa al año?",
         ["Se multiplica el uso por kg por la producción.", "300 × 1.000.", "El resultado es 300.000 L."],
         "300.000 L"),
        ("Valor del testimonio", "¿Qué valor tiene el relato de la comunidad sobre el pozo de la ficha (fuente C)?",
         ["No es una medición del nivel del pozo.", "Señala un posible efecto local importante.", "Debe contrastarse con mediciones del nivel del agua."],
         "Es una pista valiosa que hay que verificar"),
    ],
    mistakes=[("Descartar el testimonio de la comunidad por no ser una medición.", "Aporta información local que orienta qué medir.", "Úsalo como pista y contrástalo con datos."),
              ("Aceptar el folleto de la empresa porque tiene números llamativos.", "Hay un interés económico y no se entregan datos ni método.", "Pide el informe con método y datos.")],
    T=[
        ("abc", "En Química: ¿qué es un conflicto de interés?", "Una situación en que quien informa gana o pierde con el resultado", "Un desacuerdo entre dos ciencias", "Un error de cálculo", "Un conflicto de interés puede sesgar la información entregada."),
        ("{F} ¿Cuál es la variable independiente al comparar los métodos?", "El método de producción", "Es la variable que cambia entre las dos alternativas."),
        ("{F} ¿Cuál es la variable dependiente al comparar los métodos?", "El agua usada", "Es la variable que se mide como efecto."),
        ("=", "{F} ¿Cuántos litros de agua usa el método 1 al año?", "500*1000", "Se multiplica el uso por kg por la producción anual.", " L"),
        ("=", "{F} ¿Cuántos litros de agua usa el método 2 al año?", "200*1000", "Se multiplica el uso por kg por la producción anual.", " L"),
        ("=", "{F} ¿Cuál es el cambio porcentual del uso de agua al pasar del método 1 al método 2?", "(200-500)*100/500", "Se divide la diferencia por el valor de comparación (método 1) y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué fuente (A, B o C) es la más confiable para comparar el uso de agua de los métodos?", "La fuente A", "La fuente B", "La fuente C", "La A entrega método, datos y supuestos de un equipo independiente."),
        ("abc", "{F} ¿Qué problema tiene la fuente B?", "Tiene un interés económico y no entrega datos ni método", "Es demasiado técnica", "No menciona el agua", "Una afirmación sin datos y con interés económico no se puede evaluar."),
        ("abc", "{F} ¿Qué valor tiene la fuente C?", "Es una pista valiosa sobre un efecto local que debe contrastarse con mediciones del nivel del pozo", "Prueba con certeza que el proyecto causó el descenso", "Carece de todo valor", "El testimonio orienta qué medir, pero no prueba causalidad por sí solo."),
        ("ab", "{F} Para comparar de forma justa los métodos, ¿qué debe mantenerse igual?", "La producción y el clima", "El agua usada", "Si cambian la producción o el clima, la diferencia no se podría atribuir al método."),
        ("abc", "{F} ¿Qué disciplina aporta para evaluar el descenso del pozo, además de la química?", "Las ciencias de la Tierra, que estudian el agua subterránea y su recarga", "Las artes", "Ninguna otra", "Se requiere conocer cuánta agua hay y cuánto se recarga."),
        ("=", "{F} ¿Cuántos litros de agua menos usa el método 2 que el método 1 al año?", "500*1000-200*1000", "Se restan los litros anuales del método 2 a los del método 1.", " L"),
        ("abc", "{F} Alguien dice: «el método 2 usa 60 % menos agua, por lo tanto no afecta al pozo». ¿Qué falla?", "Usar menos agua no implica que el efecto sea nulo: depende de la disponibilidad y la recarga del agua", "Nada: la conclusión es correcta", "Que el 60 % está mal calculado", "El efecto sobre el pozo depende de factores que la tabla no mide."),
    ],
    ctx=("abc", "Contexto: una asamblea de ejemplo recibe los tres documentos de la ficha y debe decidir qué información pedir antes de opinar. ¿Qué pide?", "Datos de nivel del pozo antes y después del proyecto y el informe completo de la fuente A", "Que todos voten sin más información", "Solo el folleto de la empresa", "Se piden mediciones y el informe independiente antes de decidir."),
    sc=[
        ("En Química: ¿qué es un testimonio?", "Un relato de lo que una persona observó, sin medición", "Orienta qué medir, pero no reemplaza los datos."),
        ("ab", "Un informe independiente es más confiable porque:", "Quien lo hace no gana ni pierde con el resultado", "Es siempre más largo", "Reduce el riesgo de sesgo por interés."),
        ("ab", "Usar menos agua que otro método:", "No garantiza que el efecto local sea nulo", "Garantiza que no hay efecto", "El efecto local depende de la disponibilidad del agua."),
    ],
    op=("Con los datos de la ficha {F}: (1) clasifica las variables de la comparación entre métodos; (2) ordena las fuentes A, B y C y explica el valor y el límite de cada una; (3) escribe una conclusión honesta y una pregunta que falta responder.",
        "(1) Independiente: método; dependiente: agua usada; controladas: producción y clima. (2) A: confiable por método y datos; C: pista valiosa pero sin medición; B: interés económico sin datos. (3) El método 2 usa 60 % menos agua que el 1; falta saber cómo cambió el nivel del pozo y cuánta agua se recarga.",
        ["variables bien clasificadas", "valor y límite de cada fuente", "conclusión y pregunta pendiente"],
        ["tres respuestas numeradas"],
        ["descartar el testimonio", "confiar en el folleto", "concluir que no hay efecto local"],
        "Pregunta: «¿qué medirías primero en el pozo?»."),
    reinforce="Calcula el uso de agua anual de un tercer método de ejemplo con 100 L por kg y compara con los otros dos.",
    extend="Explica por qué un conflicto de interés no invalida un dato, pero obliga a verificarlo con una fuente independiente.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 3 (datos de ejemplo). Modelo de análisis integrado con cuatro dimensiones: ambiental, social, económica y ética (equidad, participación informada de la comunidad y responsabilidad con las generaciones futuras). "
     "Tres opciones para obtener agua segura en una localidad de ejemplo con 100 familias: Opción X: filtro central con tratamiento químico, costo 5.000 y deja lodos que requieren manejo; Opción Y: traer agua en camiones, costo 9.000 al año, sin lodos y con dependencia de un proveedor; Opción Z: reducir el contaminante en la industria vecina, costo 12.000 para la empresa, sin costo para las familias y con resultados lentos. "
     "Puntajes de ejemplo de 1 a 3 (3 es lo mejor) y pesos: ambiental (peso 2): X = 2, Y = 3, Z = 3; social (peso 3): X = 3, Y = 2, Z = 1; económica (peso 2): X = 3, Y = 1, Z = 2; ética (peso 3): X = 2, Y = 2, Z = 3. Puntaje total = suma de peso × puntaje.")
build(
    O7, 3, F,
    use="Aprenderé a interpretar un modelo de análisis integrado que evalúa una solución en las dimensiones ambiental, social, económica y ética. Sirve para ver cómo la química se combina con otras ciencias y valores, y cómo cambia el resultado si cambian los pesos.",
    prior=["Sé calcular una matriz con pesos.", "Sé qué es una implicancia ética, social y ambiental.", "Sé calcular costos por familia."],
    explain=[
        "Un modelo de análisis integrado evalúa una solución en varias dimensiones a la vez. La dimensión ambiental mira los residuos y los efectos en los ecosistemas. La social mira cómo afecta a las personas y su acceso a recursos. La económica mira los costos y quién los paga. La ética considera la equidad, la participación informada de la comunidad y la responsabilidad con las generaciones futuras.",
        "Para usarlo, cada dimensión recibe un peso según su importancia y cada opción un puntaje. El total es la suma de peso por puntaje. Por ejemplo, una opción con puntajes 1, 3, 2 y 2 (en el orden ambiental, social, económica y ética) suma 2 × 1 + 3 × 3 + 2 × 2 + 3 × 2 = 21. El modelo ordena las opciones, pero los puntajes y los pesos son juicios de quienes los fijan, no hechos medidos.",
        "Por eso se hace un análisis de sensibilidad: se cambian los pesos para ver si el orden cambia. Si el orden cambia con pequeños ajustes, la decisión es menos firme. Además, el modelo deja fuera cosas que importan, como la voz de la comunidad: quién decide los pesos es una pregunta ética, y la respuesta razonable es que lo haga la comunidad afectada con la información de especialistas.",
    ],
    vocab=[("dimensión de análisis", "aspecto con el que se evalúa una solución: ambiental, social, económico o ético"), ("peso", "importancia que se da a una dimensión"), ("análisis de sensibilidad", "ver cómo cambia el resultado al variar los pesos"), ("participación informada", "que la comunidad decida con información comprensible"), ("responsabilidad intergeneracional", "cuidar las posibilidades de las generaciones futuras")],
    worked=[
        ("Puntaje total", "Una opción de ejemplo tiene ambiental = 3, social = 2, económica = 2 y ética = 1, con los mismos pesos de la ficha. ¿Cuál es su total?",
         ["Ambiental: 2 × 3 = 6; social: 3 × 2 = 6.", "Económica: 2 × 2 = 4; ética: 3 × 1 = 3.", "Total: 6 + 6 + 4 + 3 = 19."],
         "19 puntos"),
        ("Costo por familia", "Una medida de ejemplo cuesta 6.000 y beneficia a 100 familias. ¿Cuánto es por familia?",
         ["Costo total: 6.000.", "Familias: 100.", "6.000 ÷ 100 = 60."],
         "60 unidades por familia"),
    ],
    mistakes=[("Tomar el resultado de la matriz como un hecho medido.", "Los puntajes y pesos son juicios de quienes los fijan.", "Declara quién los fijó y prueba otros pesos."),
              ("Dejar fuera la dimensión ética porque no es un número.", "La equidad y la participación influyen en si una solución es aceptable y justa.", "Inclúyela con un puntaje explícito y una justificación.")],
    T=[
        ("abc", "En Química: ¿qué mira la dimensión ética en un análisis integrado?", "La equidad, la participación informada y la responsabilidad con las generaciones futuras", "Solo el precio de las obras", "La masa molar de los contaminantes", "La dimensión ética pregunta por lo justo de la decisión."),
        ("=", "{F} ¿Cuál es el puntaje total de la opción X?", "2*2+3*3+2*3+3*2", "Se multiplica cada peso por el puntaje de X y se suman los cuatro productos.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de la opción Y?", "2*3+3*2+2*1+3*2", "Se multiplica cada peso por el puntaje de Y y se suman.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de la opción Z?", "2*3+3*1+2*2+3*3", "Se multiplica cada peso por el puntaje de Z y se suman.", " puntos"),
        ("abc", "{F} Con los pesos de la ficha, ¿qué opción tiene el mayor puntaje?", "La opción X", "La opción Y", "La opción Z", "X suma 25, más que Z (22) e Y (20)."),
        ("=", "{F} ¿Cuánto cuesta por familia la opción X?", "5000/100", "Se divide el costo total por el número de familias.", " unidades por familia"),
        ("=", "{F} ¿Cuánto cuesta por familia al año la opción Y?", "9000/100", "Se divide el costo anual por el número de familias.", " unidades por familia"),
        ("abc", "{F} ¿En qué dimensión la opción Y tiene su puntaje más bajo?", "En la económica, con puntaje 1", "En la ambiental", "En la ética", "Y tiene 1 en la económica, y 3 y 2 en las otras."),
        ("=", "{F} Si el peso social bajara a 1 y el ético subiera a 6 (los demás igual), ¿cuál sería el total de la opción Z?", "2*3+1*1+2*2+6*3", "Se recalculan los productos con los nuevos pesos y se suman.", " puntos"),
        ("=", "{F} Con esos mismos pesos nuevos (social 1 y ético 6), ¿cuál sería el total de la opción X?", "2*2+1*3+2*3+6*2", "Se recalculan los productos de X con los nuevos pesos y se suman.", " puntos"),
        ("abc", "{F} Con los pesos nuevos, el orden entre X y Z es distinto del que resulta con los pesos de la ficha. ¿Qué enseña esto?", "Que el orden depende de los pesos que se elijan", "Que Z es siempre la mejor", "Que la matriz no puede usarse", "El análisis de sensibilidad muestra que el orden puede cambiar."),
        ("abc", "{F} ¿Qué limitación tiene el modelo?", "Los puntajes y pesos son juicios y dejan fuera la voz directa de la comunidad", "Que usa números", "Que tiene cuatro dimensiones", "El modelo ordena con juicios que deben decidirse con la comunidad."),
        ("ab", "¿Quién debería fijar los pesos de las dimensiones?", "La comunidad afectada, con información de especialistas", "Una sola persona ajena al problema", "Los pesos expresan valores de quienes viven con las consecuencias."),
    ],
    ctx=("abc", "Contexto: un equipo de ejemplo presenta a la comunidad la matriz de la ficha y concluye «X es la solución». ¿Qué respuesta es la más razonable?", "Mostrar el análisis de sensibilidad, explicar los límites de los puntajes y dejar que la comunidad decida los pesos", "Aceptar el resultado sin preguntas", "Rechazar toda la matriz", "Una presentación honesta incluye sensibilidad, límites y participación."),
    sc=[
        ("En Química: ¿qué es un análisis de sensibilidad?", "Ver cómo cambia el resultado al variar los pesos", "Muestra qué tan firme es el orden de las opciones."),
        ("ab", "Los pesos de una matriz son:", "Juicios de quienes los fijan", "Hechos medidos con un instrumento", "Expresan la importancia que se da a cada dimensión."),
        ("ab", "Una solución técnicamente eficaz puede ser:", "Éticamente cuestionable", "Siempre justa", "La eficacia técnica no asegura por sí sola la equidad."),
    ],
    op=("Con la matriz de la ficha {F}: (1) calcula el total de las tres opciones; (2) cambia dos pesos a tu elección y recalcula; (3) escribe una recomendación y una limitación, sin imponer una postura: presenta lo que cambia si cambian los valores.",
        "(1) X = 25; Y = 20; Z = 22. (2) Con social 1 y ética 6: X = 25; Y = 6+2+2+12 = 22; Z = 29. (3) Con los pesos iniciales sugiere X; con más peso ético, Z; la decisión depende de los valores de la comunidad. Limitación: los puntajes son juicios.",
        ["tres totales correctos", "recalculo con nuevos pesos", "recomendación condicionada", "limitación"],
        ["tres respuestas numeradas"],
        ["sumar sin multiplicar por el peso", "presentar el resultado como único", "no declarar limitaciones"],
        "Pregunta: «¿qué dimensión nueva agregarías?»."),
    reinforce="Rehace la matriz con un peso distinto en la dimensión ambiental y anota si el orden de X, Y y Z cambia.",
    extend="Explica por qué la participación de la comunidad es parte de la ética del análisis y no un trámite aparte.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 4 (datos de ejemplo; el valor de referencia es inventado para practicar). Un fertilizante nuevo de ejemplo se usa en 100 hectáreas. Rendimiento: 4.000 kg por hectárea con el fertilizante actual y 4.400 kg con el nuevo. Precio de venta de ejemplo: 100 unidades monetarias por kg. Costo adicional del fertilizante nuevo: 25.000 unidades por hectárea. "
     "Nitrato en los pozos de las 200 familias vecinas, que beben esa agua: 20 mg/L antes y 45 mg/L tras una temporada con el fertilizante nuevo. Valor de referencia de ejemplo para nitrato en agua potable: 50 mg/L. Tratar el agua para mantenerla bajo la referencia costaría 600.000 unidades. "
     "Dimensiones por evaluar: ambiental, social, económica y ética.")
build(
    O7, 4, F,
    use="Aprenderé a analizar un caso con datos de química, agricultura, economía y salud del agua, y a valorar la integración de estos conocimientos para decidir con implicancias éticas, sociales y ambientales. Sirve para ver quién gana, quién asume riesgos y qué información falta.",
    prior=["Sé calcular ganancias y cambios porcentuales.", "Sé qué es un valor de referencia.", "Sé que correlación no es causalidad."],
    explain=[
        "Analizar un caso integrado significa calcular lo que se puede calcular en cada disciplina y luego juntar los resultados. En lo económico, la ganancia adicional por hectárea es el ingreso extra menos el costo adicional. Si el rendimiento sube 300 kg y cada kg se vende a 100, el ingreso extra es 30.000. En lo químico y ambiental, se compara el nitrato del agua con el valor de referencia y se calcula su aumento.",
        "Luego se juntan los resultados y se mira quién recibe los beneficios y quién asume los riesgos. En este caso, las personas que cultivan reciben la ganancia, mientras las familias que beben agua de pozo asumen el riesgo de un nitrato más alto. Esa distribución es una pregunta de equidad. También hay incertidumbre: un solo año de datos no muestra la tendencia, y no se sabe si el aumento de nitrato se debe solo al fertilizante.",
        "Una buena conclusión integra los datos, declara lo que no se sabe y propone medidas proporcionales, como seguir midiendo, definir quién paga el tratamiento si el nitrato supera la referencia y consultar a las familias. No se trata de tomar partido por una postura, sino de mostrar cómo los conocimientos de varias ciencias ayudan a decidir con mejor información.",
    ],
    vocab=[("ganancia neta", "ingresos extra menos costos extra"), ("riesgo", "posibilidad de un daño, que depende de la exposición y del efecto"), ("equidad", "reparto justo de beneficios, costos y riesgos"), ("incertidumbre", "lo que no se sabe con seguridad a partir de los datos"), ("tendencia", "dirección en que cambian los datos a lo largo del tiempo")],
    worked=[
        ("Ganancia neta", "Una opción de ejemplo aumenta el rendimiento en 200 kg por hectárea a 100 unidades por kg, con un costo adicional de 12.000 por hectárea. ¿Cuál es la ganancia neta por hectárea?",
         ["Ingreso extra: 200 × 100 = 20.000.", "Costo adicional: 12.000.", "Ganancia neta: 20.000 − 12.000 = 8.000."],
         "8.000 unidades por hectárea"),
        ("Porcentaje de la referencia", "Un pozo de ejemplo tiene 30 mg/L de nitrato y la referencia es 50 mg/L. ¿Qué porcentaje de la referencia es?",
         ["Se divide el valor medido por la referencia.", "30 ÷ 50 = 0,6.", "Multiplicado por 100 es 60 %."],
         "60 %"),
    ],
    mistakes=[("Decidir solo con el resultado económico.", "El análisis integrado exige mirar también el agua de las familias y su equidad.", "Junta los resultados de todas las dimensiones."),
              ("Concluir que el fertilizante causó todo el aumento de nitrato con un solo año de datos.", "Pueden influir otras variables y falta ver la tendencia.", "Declara la incertidumbre y propone seguir midiendo.")],
    T=[
        ("abc", "En Química: ¿qué es la ganancia neta?", "Los ingresos extra menos los costos extra", "Los ingresos totales sin descontar nada", "El costo total de un proyecto", "La ganancia neta resta los costos adicionales."),
        ("=", "{F} ¿Cuál es el ingreso extra por hectárea con el fertilizante nuevo?", "(4400-4000)*100", "Se multiplica el aumento de rendimiento por el precio por kg.", " unidades"),
        ("=", "{F} ¿Cuál es la ganancia neta por hectárea con el fertilizante nuevo?", "(4400-4000)*100-25000", "Se resta el costo adicional al ingreso extra por hectárea.", " unidades"),
        ("=", "{F} ¿Cuál es la ganancia neta total en las 100 hectáreas?", "((4400-4000)*100-25000)*100", "Se multiplica la ganancia neta por hectárea por el número de hectáreas.", " unidades"),
        ("=", "{F} Si hubiera que pagar el tratamiento del agua, ¿cuál sería la ganancia total menos ese costo?", "((4400-4000)*100-25000)*100-600000", "Se resta el costo del tratamiento a la ganancia neta total.", " unidades"),
        ("=", "{F} ¿Qué porcentaje de la referencia es el nitrato de 45 mg/L?", "45*100/50", "Se divide el valor medido por la referencia y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es el cambio porcentual del nitrato en los pozos, de 20 a 45 mg/L?", "(45-20)*100/20", "Se divide el aumento por el valor inicial y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Quiénes reciben los beneficios económicos y quiénes asumen el riesgo en este caso?", "Reciben la ganancia quienes cultivan y asumen el riesgo las familias que beben agua de pozo", "Todos reciben y asumen lo mismo", "Solo las familias reciben la ganancia", "Los datos muestran que beneficios y riesgos recaen en personas distintas."),
        ("abc", "{F} ¿Qué conclusión sobre el nitrato es prudente?", "Subió en una temporada y se acerca a la referencia de ejemplo sin superarla; falta ver la tendencia y otras causas", "Está sin problema para siempre porque no superó la referencia", "El fertilizante causó el aumento con certeza", "La conclusión se limita a lo medido y declara la incertidumbre."),
        ("ab", "{F} ¿Qué dato ayuda más a decidir mejor?", "Nitrato medido en varias temporadas y en otros pozos", "El color de los envases del fertilizante", "Una serie de datos repetidos permite ver la tendencia."),
        ("abc", "{F} ¿Qué medida es proporcional a la información disponible?", "Seguir midiendo, definir quién paga el tratamiento si se supera la referencia y consultar a las familias", "Prohibir todo sin medir", "Ignorar el aumento de nitrato", "Una medida proporcional responde a la incertidumbre sin ignorar el riesgo."),
        ("abc", "{F} ¿Qué disciplina aporta cada parte del análisis?", "Economía para la ganancia, química para el nitrato y ética para quién asume el riesgo", "Solo la química para todo", "Ninguna aporta", "Cada cálculo y pregunta proviene de una disciplina distinta."),
        ("=", "{F} Si el fertilizante nuevo costara 35.000 por hectárea en vez de 25.000, ¿cuál sería la ganancia total de las 100 hectáreas menos el tratamiento del agua?", "((4400-4000)*100-35000)*100-600000", "Se recalcula la ganancia neta por hectárea con el nuevo costo, se multiplica por 100 y se resta el tratamiento.", " unidades"),
    ],
    ctx=("abc", "Contexto: se presentará este caso en una reunión con agricultores y familias vecinas de ejemplo. ¿Qué mensaje integra mejor los datos?", "Hay ganancia para quienes cultivan y un aumento de nitrato para quienes beben de pozo; falta ver la tendencia, y conviene acordar entre todos quién paga el tratamiento si se supera la referencia", "El fertilizante es bueno y no hay nada más que discutir", "El fertilizante debe prohibirse sin más datos", "El mensaje correcto junta beneficios, riesgos, incertidumbre y participación."),
    sc=[
        ("En Química: ¿qué es la incertidumbre en un análisis?", "Lo que no se sabe con seguridad a partir de los datos", "Declararla evita afirmar más de lo que muestran los datos."),
        ("ab", "Un análisis integrado considera:", "Beneficios y riesgos de todos los grupos afectados", "Solo el beneficio económico", "Incluye a quienes asumen los riesgos."),
        ("ab", "Una tendencia se ve mejor con:", "Datos de varios años", "Datos de una sola temporada", "Una serie permite ver la dirección de los cambios."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula la ganancia neta por hectárea y el porcentaje que representa el nitrato respecto de la referencia; (2) describe quién se beneficia y quién asume riesgos; (3) escribe una conclusión sin tomar partido, con una incertidumbre y una pregunta ética.",
        "(1) Ganancia neta: 15.000 por hectárea; nitrato: 90 % de la referencia. (2) Se benefician quienes cultivan; asumen riesgo las familias que beben agua de pozo. (3) Los datos muestran ganancia y un aumento de nitrato; no se conoce la tendencia. ¿Quién debería pagar el tratamiento del agua si se supera la referencia?",
        ["dos cálculos correctos", "beneficios y riesgos por grupo", "conclusión sin postura, con incertidumbre y pregunta ética"],
        ["tres respuestas numeradas"],
        ["decidir solo con el dato económico", "afirmar causalidad", "tomar una postura sin argumentos"],
        "Pregunta: «¿qué dato nuevo cambiaría tu conclusión?»."),
    reinforce="Calcula la ganancia neta total si el rendimiento subiera solo 200 kg por hectárea, con los demás datos de la ficha.",
    extend="Explica por qué integrar conocimientos de varias ciencias ayuda a evitar decisiones que benefician a un grupo y perjudican a otro sin que se note.",
)
