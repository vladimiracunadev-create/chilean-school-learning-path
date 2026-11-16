"""Chile y la región latinoamericana 3.º/4.º medio FG: OA 06 clases 5 y 6 (evaluar alternativas de integración y cooperación; comunicar una conclusión situada) y OA 07 clase 1 (problema local y trabajo colaborativo). Casos y datos de ejemplo inventados."""
from __future__ import annotations

from fg_chla_common import build

O6 = "FG-CHLA-3y4-OAC-06"
O7 = "FG-CHLA-3y4-OAC-07"

# ============================================================ OA 06, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado; país ficticio Alto Valle). El gobierno evalúa tres alternativas dentro de la Unión del Sur (bloque ficticio). "
     "Alternativa A: profundizar el tratado comercial, con aranceles aún más bajos. Alternativa B: crear un fondo común de cooperación en salud y ciencia. "
     "Alternativa C: un acuerdo de reconocimiento de títulos y movilidad de estudiantes. "
     "Puntajes de ejemplo de 1 (bajo) a 3 (alto). Beneficio económico: A = 3, B = 1, C = 2. Beneficio social: A = 1, B = 3, C = 2. Bajo riesgo para sectores que compiten con importaciones (3 = riesgo bajo): A = 1, B = 3, C = 3. "
     "Primera ponderación: el beneficio económico pesa 2, el social pesa 3 y el bajo riesgo pesa 1.")
build(
    O6, 5, F,
    use="Aprenderé a evaluar alternativas de integración y cooperación entre Estados latinoamericanos usando criterios con distinto peso y a explicar cómo cambia la decisión.",
    explain=[
        'Evaluar alternativas de integración y cooperación supone comparar sus ventajas y costos en varios ámbitos: economía, salud, educación, ciencia, género y derechos humanos. Se usan criterios como el beneficio económico, el beneficio social, el riesgo para ciertos sectores, el costo y la facilidad de cumplir lo acordado. Como no todos los criterios importan igual, se les asigna un peso: el puntaje de cada criterio se multiplica por su peso y luego se suman los resultados.',
        'La ponderación obliga a explicitar qué se valora más, y por eso puede cambiar la decisión. Si se cambian los pesos, la alternativa mejor puede ser otra. Esto no significa que los números «mientan»: significa que reflejan valores. Es buena práctica mostrar la matriz, probar varias ponderaciones y explicar a quién beneficia y a quién perjudica cada alternativa. En una decisión pública, también corresponde escuchar a los sectores afectados antes de resolver.',
    ],
    vocab=[("ponderación", "asignar a cada criterio un peso según su importancia"), ("peso", "número por el que se multiplica el puntaje de un criterio"), ("matriz de decisión", "tabla que compara alternativas con criterios y puntajes"), ("sensibilidad", "cuánto cambia el resultado si cambian los pesos"), ("sector afectado", "grupo que gana o pierde con una decisión")],
    worked=[
        ("Calcular un total ponderado", "Una alternativa de ejemplo tiene puntajes 3 y 2 en dos criterios con pesos 2 y 1. ¿Cuál es su total?", ["Se multiplica cada puntaje por su peso: 3 × 2 y 2 × 1.", "Se suman los resultados: 6 + 2."], "8"),
        ("Probar otra ponderación", "Si el peso del primer criterio sube de 2 a 4, ¿qué pasa con el total anterior?", ["El primer término pasa de 6 a 12.", "El total sube y la decisión puede cambiar."], "El total aumenta y la decisión puede cambiar"),
    ],
    mistakes=[("Sumar los puntajes sin considerar los pesos.", "No todos los criterios importan igual.", "Multiplica cada puntaje por su peso antes de sumar."),
              ("Creer que existe una ponderación «correcta» única.", "Los pesos reflejan valores y prioridades que se discuten.", "Prueba varias ponderaciones y explica la que elegiste.")],
    T=[
        ('¿Qué es la ponderación de criterios?', 'Asignar a cada criterio un peso según su importancia', 'Dar el mismo peso a todos los criterios', 'Eliminar los criterios que no favorecen', 'Ponderar es reflejar que los criterios no valen lo mismo.'),
        ('¿Qué es una matriz de decisión?', 'Una tabla que compara alternativas según criterios y puntajes', 'Una lista de las decisiones que otros países ya tomaron', 'Un documento que obliga a elegir la alternativa más barata', 'La matriz ordena la comparación.'),
        ('¿Para qué sirve probar distintas ponderaciones?', 'Para ver si la decisión cambia cuando cambian las prioridades', 'Para encontrar la ponderación que asegure el resultado esperado', 'Para evitar tener que explicar los criterios usados', 'Se prueba la sensibilidad del resultado a los pesos.'),
        ('=', '{F} ¿Cuál es el total ponderado de la Alternativa A (3×2 + 1×3 + 1×1)?', '3*2+1*3+1*1', 'Se multiplica cada puntaje por su peso y se suman.', ' puntos'),
        ('=', '{F} ¿Cuál es el total ponderado de la Alternativa B (1×2 + 3×3 + 3×1)?', '1*2+3*3+3*1', 'Se multiplica cada puntaje por su peso y se suman.', ' puntos'),
        ('=', '{F} ¿Cuál es el total ponderado de la Alternativa C (2×2 + 2×3 + 3×1)?', '2*2+2*3+3*1', 'Se multiplica cada puntaje por su peso y se suman.', ' puntos'),
        ('{F} Con la primera ponderación, ¿qué alternativa tiene el mayor total?', 'La Alternativa B', 'La Alternativa A', 'La Alternativa C', 'B suma 14, C suma 13 y A suma 10.'),
        ('=', '{F} Si ahora el beneficio económico pesa 4, el social 3 y el bajo riesgo 1, ¿cuánto suma la Alternativa A (3×4 + 1×3 + 1×1)?', '3*4+1*3+1*1', 'Se multiplica cada puntaje por su nuevo peso y se suman.', ' puntos'),
        ('=', '{F} Con los pesos 4, 3 y 1, ¿cuánto suma la Alternativa C (2×4 + 2×3 + 3×1)?', '2*4+2*3+3*1', 'Se multiplica cada puntaje por su nuevo peso y se suman.', ' puntos'),
        ('{F} Con los pesos 4, 3 y 1, la A suma 16, la B suma 16 y la C suma 17. ¿Qué conclusión es correcta?', 'Cambió el resultado: ahora lidera la C, con 17 puntos', 'No cambió nada: la B sigue liderando', 'La ponderación no influye en el resultado', 'Al dar más peso a lo económico, C pasa al primer lugar.'),
        ('{F} Un funcionario dice: «La matriz demuestra que B es la mejor». ¿Qué respuesta es más precisa?', 'Lo es con unos pesos; con otros puede ganar C, y hay que justificarlos', 'Es cierto, porque los números no dependen de los pesos', 'Es falso, porque la matriz no sirve para comparar', 'El resultado depende de los pesos, que reflejan valores.'),
        ('{F} ¿Qué sector podría estar preocupado por la Alternativa A?', 'Los sectores que compiten con importados', 'Los que exportan frutas y verduras al resto del bloque', 'Los estudiantes que quieren movilidad entre universidades del bloque', 'La A tiene el menor puntaje de bajo riesgo para sectores que compiten con importaciones.'),
        ('{F} Antes de decidir, ¿qué paso es recomendable?', 'Escuchar a los afectados y probar varias ponderaciones', 'Elegir la alternativa con más puntos en la primera ponderación', 'Esperar que el bloque decida sin consultar a nadie', 'Probar la sensibilidad y escuchar mejora la legitimidad.'),
    ],
    ctx=('Una alternativa de ejemplo tiene puntajes 3, 1 y 2 en tres criterios con pesos 1, 2 y 3. ¿Cuál es su total ponderado?', '11', '6', '14', 'Se calcula 3×1 + 1×2 + 2×3 = 3 + 2 + 6 = 11.'),
    sc=[
        ('En Chile y la región, ¿por qué se ponderan los criterios al evaluar acuerdos?', 'Porque no todos los criterios importan igual', 'Los pesos reflejan las prioridades de quien decide.'),
        ('=', 'Una alternativa de ejemplo tiene puntajes 2 y 3 con pesos 3 y 2. ¿Cuál es su total?', '2*3+3*2', 'Se multiplica cada puntaje por su peso y se suman.', ' puntos'),
        ('¿Qué pasa si se cambian los pesos de una matriz?', 'Puede cambiar la alternativa mejor evaluada', 'Por eso se prueba la sensibilidad del resultado.'),
    ],
    op=("Usa la {F} Escribe una recomendación de seis líneas: totales ponderados de A, B y C con la primera ponderación; qué ocurre con pesos 4, 3 y 1; quién podría resultar afectado por tu alternativa; y qué harías para escucharlo antes de decidir.",
        "Con la primera ponderación A suma 10, B suma 14 y C suma 13. Con pesos 4, 3 y 1, A suma 16, B suma 16 y C suma 17: cambia el liderazgo. Recomiendo B si se prioriza lo social y C si se prioriza lo económico, justificando la elección. Los sectores que compiten con importaciones podrían verse afectados si se elige A. Antes de decidir, realizaría consultas a esos sectores y a las universidades.",
        ["calcula los totales", "prueba otra ponderación", "reconoce a quién afecta"], ["recomendación de seis líneas"], ["ignorar los pesos", "no escuchar a los afectados"],
        "Pregunta si cambiarías el peso de algún criterio después de escuchar a los afectados."),
    rx=("Calcula el total ponderado de una alternativa inventada con tres criterios y pesos distintos.", "Conversa con tu docente sobre cómo se decide qué acuerdos regionales firma tu país."),
)

# ============================================================ OA 06, clase 6
F = ("Ficha 6 (datos de ejemplo, inventados; país ficticio Alto Valle en la Unión del Sur). Resultados de los dos primeros años: el comercio dentro del bloque pasó de 20 % a 25 % de las exportaciones; "
     "el empleo del sector de fruta subió de 300 a 420 y el del textil bajó de 500 a 450; se firmó un acuerdo de salud y uno de reconocimiento de títulos. "
     "Todavía no hay datos sobre precios de los productos para las familias. "
     "Borrador A: «La integración es un éxito total y debe aplicarse en toda América Latina». Borrador B: «En Alto Valle, durante los dos primeros años, el comercio dentro del bloque subió y el empleo neto aumentó en 70 puestos, aunque el sector textil perdió empleos; faltan datos de precios; se recomienda reunir más información y apoyar a quienes perdieron empleo».")
build(
    O6, 6, F,
    use="Aprenderé a comunicar una conclusión situada sobre integración y cooperación, con afirmación, evidencia, matiz y propuesta, sin generalizar a toda la región.",
    explain=[
        'Una conclusión situada sobre integración dice a qué país, bloque y período se refiere, y no extiende lo observado a toda América Latina. Tiene cuatro partes: una afirmación, la evidencia que la respalda con cifras y fuente, un matiz o límite (qué no se puede decir con los datos) y una propuesta o pregunta para seguir investigando o actuando. Es importante incluir a quienes ganaron y a quienes perdieron.',
        'También conviene usar un lenguaje preciso: palabras como «éxito total» o «fracaso» son juicios que necesitan evidencia, mientras que «subió de 20 % a 25 %» es un dato. Se debe distinguir lo que sabemos de lo que falta saber. Si hay desacuerdo entre fuentes, se menciona. Una buena conclusión puede ser breve, pero cada afirmación se puede rastrear hasta una cifra o una fuente.',
    ],
    vocab=[("conclusión situada", "conclusión que dice a qué lugar, tiempo y datos se refiere"), ("matiz", "precisión que limita o completa una afirmación"), ("juicio", "valoración que necesita evidencia, como «éxito total»"), ("dato", "cifra o hecho comprobable"), ("generalizar", "extender lo observado en un caso a todos los casos")],
    worked=[
        ("Separar juicio y dato", "En un texto de ejemplo se lee «el bloque fue un desastre» y «las exportaciones bajaron de 100 a 90». ¿Cuál es dato y cuál es juicio?", ["«Las exportaciones bajaron de 100 a 90» se puede comprobar.", "«Un desastre» es una valoración."], "Dato: la cifra. Juicio: «desastre»"),
        ("Acotar una conclusión", "Con datos de un país en dos años, un texto dice «en toda la región funciona». ¿Cómo se acota?", ["Se nombra el país y el período.", "Se evita extender a toda la región."], "«En ese país, durante esos dos años…»"),
    ],
    mistakes=[("Usar «éxito» o «fracaso» sin cifras.", "Son juicios que necesitan evidencia.", "Escribe primero el dato y luego tu valoración."),
              ("Ocultar a quienes perdieron.", "La conclusión queda incompleta y puede ser injusta.", "Menciona ganadores y perdedores con sus cifras.")],
    T=[
        ('¿Qué es una conclusión situada sobre integración regional?', 'Una que dice qué lugar, tiempo y datos abarca la afirmación', 'Una que no necesita datos ni fuentes', 'Una que se aplica a todos los países de la región', 'Situar es acotar la conclusión a lo que muestran los datos.'),
        ('¿Cuál de estas es un juicio y no un dato?', '«La integración fue un éxito total»', '«El comercio subió de 20 % a 25 %»', '«El empleo de fruta subió de 300 a 420»', 'Los dos últimos son datos comprobables; «éxito total» es una valoración.'),
        ('¿Qué es un matiz?', 'Una precisión que limita o completa lo que se afirma', 'Una opinión que reemplaza los datos de la fuente', 'Una cifra que se agrega sin indicar su origen', 'El matiz muestra los límites de la afirmación.'),
        ('=', '{F} ¿Cuántos puntos porcentuales subió el comercio dentro del bloque?', '25-20', 'Se resta el porcentaje inicial al final.', ' puntos porcentuales'),
        ('=', '{F} ¿Cuántos empleos ganó el sector de fruta?', '420-300', 'Se resta el empleo inicial al final.', ' empleos'),
        ('=', '{F} ¿Cuál es el cambio neto de empleo entre los dos sectores de la ficha?', '(420-300)-(500-450)', 'Se restan los empleos perdidos a los ganados.', ' empleos'),
        ('{F} ¿Qué problema tiene el Borrador A?', 'Usa un juicio sin evidencia y generaliza a toda la región', 'Menciona datos con su fuente y su año', 'Incluye un matiz y una propuesta de investigación', 'El Borrador A afirma «éxito total» y extiende a toda la región.'),
        ('{F} ¿Qué mejora trae el Borrador B?', 'Indica país, período, datos, matiz y propuesta', 'Evita mencionar a quienes perdieron empleos', 'Declara que los datos de precios son innecesarios', 'B es una conclusión situada.'),
        ('{F} En el Borrador B, ¿cuál es el matiz?', 'Que el textil perdió empleos y faltan datos de precios', 'Que el comercio dentro del bloque subió en los dos años', 'Que se recomienda aplicar el modelo a toda la región', 'El matiz limita la afirmación general.'),
        ('{F} En el Borrador B, ¿cuál es la propuesta?', 'Reunir información y apoyar a quienes perdieron empleo', 'Cerrar el acuerdo del bloque sin evaluar sus efectos', 'Aplicar el modelo del bloque a otros países sin estudiarlo', 'La propuesta orienta acciones a partir de los datos.'),
        ('{F} Alguien dice: «El Borrador A es más corto y claro, por eso es mejor». ¿Qué respuesta es más completa?', 'Es corto, pero no se comprueba y deja fuera a los perjudicados', 'Tiene razón, porque la brevedad es lo único que importa en un informe', 'Es peor solo porque usa menos palabras que el Borrador B completo', 'La brevedad no compensa la falta de evidencia ni la generalización.'),
        ('{F} Un estudiante propone escribir: «Los precios bajaron para las familias». ¿Qué falla tiene?', 'La ficha dice que aún no hay datos de precios', 'La ficha muestra que los precios subieron mucho', 'La frase es correcta, porque el comercio subió', 'Sin datos de precios no se puede afirmar esa consecuencia.'),
        ('{F} ¿Qué dato adicional ayudaría a fortalecer la conclusión?', 'Datos de precios y del nuevo trabajo de los afectados', 'El nombre de las autoridades que firmaron el tratado del bloque', 'La cantidad de páginas del texto completo del tratado', 'Esos datos aportan efectos sobre las familias y los trabajadores.'),
    ],
    ctx=('Un estudiante redacta: «En el país P, entre los años 1 y 2, las exportaciones al bloque subieron de 30 % a 35 %; no se conocen aún los efectos en los precios». ¿Qué cualidad tiene su frase?', 'Está situada y reconoce lo que falta saber', 'Generaliza sus resultados a toda América Latina', 'Usa un juicio sin respaldo en datos', 'Indica lugar, período, dato y un límite.'),
    sc=[
        ('Nombra las cuatro partes de una conclusión situada.', 'Afirmación, evidencia, matiz y propuesta', 'Son las partes que permiten respaldar, matizar y seguir investigando.'),
        ('=', 'El empleo en un sector de ejemplo baja de 200 a 170. ¿Cuántos empleos se perdieron?', '200-170', 'Se resta el empleo final al inicial.', ' empleos'),
        ('¿Por qué conviene mencionar a quienes perdieron con un acuerdo?', 'Porque la conclusión queda incompleta si solo muestra a los ganadores', 'Mostrar a todos los afectados da una imagen más justa.'),
    ],
    op=("Usa la {F} Escribe tu propia conclusión de seis líneas con las cuatro partes (afirmación, evidencia, matiz y propuesta) sobre la integración de Alto Valle. Evita juicios como «éxito total» y no generalices a toda la región.",
        "Afirmación: en Alto Valle, durante los dos primeros años, la integración aumentó el comercio dentro del bloque. Evidencia: pasó de 20 % a 25 % de las exportaciones y el empleo neto subió 70 puestos. Matiz: el sector textil perdió 50 empleos y faltan datos de precios. Propuesta: reunir datos de precios y de empleo por sector, y apoyar con capacitación a quienes perdieron empleo.",
        ["incluye las cuatro partes", "usa cifras de la ficha", "evita juicios y generalizaciones"], ["conclusión de seis líneas"], ["generalizar a toda la región", "ocultar a quienes perdieron"],
        "Revisa que cada afirmación tenga su cifra y que el matiz sea honesto."),
    rx=("Reescribe una frase con juicio («fue un fracaso») en una frase con dato.", "Pide a alguien de tu casa que lea tu conclusión y diga si entendió qué evidencia la respalda."),
)

# ============================================================ OA 07, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado; barrio ficticio Villa Esperanza). La plaza del barrio tiene basura, poca luz en la tarde y pocas actividades. "
     "Viven allí familias de distintos orígenes, algunas llegadas hace poco desde otros países, y también adultos mayores y jóvenes. "
     "Un curso de 3.º medio del liceo del barrio quiere proponer algo para mejorar la plaza. Los actores cercanos son: la junta de vecinos, la municipalidad, comerciantes de la esquina y el centro de estudiantes. "
     "El equipo de seis estudiantes aún no se ha repartido tareas.")
build(
    O7, 1, F,
    use="Aprenderé a delimitar un problema local relacionado con temas del nivel, identificar sus actores, tiempo y espacio, y organizar un equipo para trabajar de forma colaborativa.",
    explain=[
        'Diseñar una propuesta para un problema local empieza por delimitarlo: decir qué ocurre, dónde, desde cuándo y a quiénes afecta. Un buen problema es concreto (se puede observar), local (está en tu barrio o comuna) y relacionado con los temas del nivel, como migración y diversidad, derechos y democracia, economía, medioambiente o integración. Conviene distinguir el síntoma (lo que se ve, como la basura) de las causas (por qué ocurre). Luego se identifican los actores, que pueden ayudar, decidir o verse afectados.',
        'Trabajar de forma colaborativa significa repartir responsabilidades, escuchar a todas las personas, tomar acuerdos y revisar cómo va el trabajo. Algunos roles útiles son coordinar las reuniones, registrar los acuerdos, buscar información y comunicar con otros actores. Se recomienda definir normas del equipo, como hablar por turnos y respetar los plazos, y resolver los desacuerdos con argumentos y no con imposiciones. En todo trabajo con la comunidad, salir a terreno debe hacerse en grupo, en espacios públicos, de día y con conocimiento de una persona adulta del liceo.',
    ],
    vocab=[("problema local", "situación concreta del barrio o comuna que afecta a personas y puede mejorar"), ("síntoma", "lo que se observa de un problema"), ("causa", "razón por la que ocurre el problema"), ("actor", "persona o institución que puede ayudar, decidir o verse afectada"), ("rol", "responsabilidad que asume una persona en el equipo"), ("acuerdo", "decisión tomada entre todas las personas del equipo")],
    worked=[
        ("Distinguir síntoma y causa", "En un barrio de ejemplo hay basura en la calle. ¿Qué es síntoma y qué podría ser causa?", ["La basura visible es lo que se observa: síntoma.", "La falta de contenedores o de recolección podría ser una causa."], "Síntoma: basura. Causa posible: falta de contenedores"),
        ("Repartir roles", "Un equipo de ejemplo de cuatro personas debe coordinar, registrar, investigar y comunicar. ¿Cómo lo reparte?", ["Una persona por rol, de modo que todos tengan una tarea.", "Los roles pueden rotar."], "Un rol por persona, con rotación"),
    ],
    mistakes=[("Elegir un problema demasiado grande para un equipo escolar.", "Un problema muy amplio no se puede abordar en pocas semanas.", "Acótalo a un lugar y a un aspecto concreto."),
              ("Trabajar sin repartir tareas ni registrar acuerdos.", "Se pierde tiempo y se generan malentendidos.", "Define roles, plazos y un registro de acuerdos desde el inicio.")],
    T=[
        ('¿Qué es un síntoma de un problema?', 'Lo que se observa del problema, como la basura', 'La razón profunda por la que ocurre el problema', 'La solución que se aplicará más adelante', 'El síntoma es lo visible; la causa es lo que lo origina.'),
        ('¿Qué es un actor en un problema local?', 'Una persona o institución que puede ayudar, decidir o verse afectada', 'Un lugar del barrio donde ocurren los hechos', 'Un dato numérico medido por una oficina del Estado', 'Los actores participan o son afectados; un lugar o un dato no lo son.'),
        ('¿Qué es un rol en un equipo?', 'Una responsabilidad que asume una persona', 'Una norma que impide la participación de otras personas', 'Una decisión que toma solo quien coordina', 'Los roles reparten el trabajo.'),
        ('{F} ¿Cuál es el síntoma que describe la ficha?', 'La plaza tiene basura, poca luz y pocas actividades', 'Las familias de distintos orígenes viven en el barrio', 'El equipo de seis estudiantes no tiene tareas', 'La basura, la poca luz y las pocas actividades son lo que se observa.'),
        ('{F} ¿Cuál es un actor cercano que podría decidir sobre la iluminación?', 'La municipalidad, por su rol en el espacio público', 'El centro de estudiantes del liceo', 'Un comerciante de la esquina', 'La municipalidad suele ser responsable del alumbrado público.'),
        ('{F} ¿Quiénes son afectados por el estado de la plaza?', 'Vecinas y vecinos de distintas edades y orígenes', 'Solo los estudiantes del curso del liceo que hacen el trabajo', 'Únicamente las autoridades municipales que administran la plaza', 'La ficha dice que viven allí familias de distintos orígenes y personas de varias edades.'),
        ('{F} ¿Qué espacio y qué tiempo se pueden delimitar?', 'La plaza de Villa Esperanza, hoy, en la tarde', 'Todo el país, durante los próximos diez años completos', 'La ciudad completa, desde comienzos del siglo pasado', 'El problema es local y reciente; la poca luz se nota en la tarde.'),
        ('{F} Un integrante propone «mejorar todo el barrio». ¿Qué problema tiene la propuesta?', 'Es demasiado amplia para un equipo escolar', 'Es demasiado pequeña para interesar a la comunidad', 'No se relaciona con ningún tema del nivel', 'Un problema muy amplio no se puede abordar bien.'),
        ('{F} ¿Cuál es una forma de acotar mejor el problema?', 'Enfocarse en la plaza y su alumbrado, basura y actividades', 'Enfocarse en la economía de toda la región latinoamericana', 'Enfocarse en cambiar por completo la forma de gobierno de la comuna', 'La plaza es un lugar concreto y observable.'),
        ('{F} ¿Qué roles convendría repartir entre las seis personas?', 'Coordinar, registrar, investigar y comunicar', 'Un solo rol para todas las personas', 'Que cada persona haga todo por su cuenta', 'Un reparto de roles ordena el trabajo.'),
        ('{F} Dos integrantes discuten qué problema elegir. ¿Cuál es una forma colaborativa de resolverlo?', 'Dar argumentos y decidir con un criterio acordado', 'Dejar que decida quien habla más fuerte', 'Elegir al azar sin discutir las razones', 'Los desacuerdos se resuelven con argumentos y criterios.'),
        ('{F} ¿Qué conexión hay entre la diversidad del barrio y el problema de la plaza?', 'La plaza podría ser un lugar de encuentro intercultural si se cuida', 'La diversidad del barrio es la causa de la basura que hay en la plaza', 'La diversidad del barrio impide cualquier mejora en la plaza del lugar', 'Culpar a la diversidad no tiene respaldo en la ficha; la plaza puede ser un espacio de encuentro.'),
        ('{F} Para salir a observar la plaza en terreno, ¿qué precaución corresponde?', 'Ir en grupo, de día y avisando a una persona adulta', 'Ir en grupo al caer la tarde para ver mejor la poca luz de la plaza', 'Ir sin avisar a nadie del liceo para no llamar la atención del barrio', 'La seguridad requiere compañía, luz de día y aviso a una persona adulta.'),
    ],
    ctx=('Un equipo de ejemplo decide ayudar a su barrio. Escriben: «Queremos mejorar la economía de todo el país». ¿Qué le falta a esa formulación para ser un problema local?', 'Concretar un lugar y un aspecto observable', 'Agregar más países a la formulación para que sea más importante', 'Cambiar la palabra economía por otra palabra más complicada', 'Un problema local se delimita a un lugar y a un aspecto concreto.'),
    sc=[
        ('¿Qué diferencia hay entre síntoma y causa?', 'El síntoma es lo que se ve; la causa es por qué ocurre', 'Para proponer soluciones útiles hay que ir a las causas.'),
        ('Nombra dos roles útiles en un equipo de trabajo.', 'Por ejemplo, coordinar y registrar acuerdos', 'También sirven buscar información y comunicar con otros actores.'),
        ('¿Qué precauciones se toman al salir a terreno?', 'Ir en grupo, de día y con conocimiento de una persona adulta', 'La seguridad es parte del trabajo colaborativo.'),
    ],
    op=("Usa la {F} Redacta la ficha de inicio del equipo: el problema en una oración (qué, dónde y a quiénes afecta), tres actores y qué puede hacer cada uno, tres roles con una persona imaginaria para cada uno y dos normas del equipo.",
        "Problema: la plaza de Villa Esperanza tiene basura, poca luz y pocas actividades, y afecta a vecinas y vecinos de distintas edades y orígenes. Actores: la municipalidad puede mejorar el alumbrado; la junta de vecinos puede organizar actividades; los comerciantes pueden colaborar con contenedores. Roles: coordinación (Ana), registro (Luis) y comunicación (Sofía). Normas: hablar por turnos y registrar los acuerdos al final de cada reunión.",
        ["delimita el problema", "nombra actores con su aporte", "define roles y normas"], ["ficha de inicio"], ["problema demasiado amplio", "no repartir roles"],
        "Pregunta qué dato o actor falta para conocer mejor el problema."),
    rx=("Escribe un problema local de tu barrio o liceo y distingue su síntoma de una posible causa.", "Conversa con alguien de tu casa sobre qué le gustaría que mejorara en el barrio, sin datos personales."),
)
