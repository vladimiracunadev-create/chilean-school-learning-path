"""Creación y composición musical 3.º y 4.º medio HC: OAC-06 (evaluar críticamente procesos y resultados de obras y proyectos musicales personales y de pares). Proyectos, bitácoras y rúbricas inventados."""
from __future__ import annotations

from hc_ccmu_common import CLAVE, build

O6 = "AR-CCMU-3y4-OAC-06"

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (proyecto y rúbrica de ejemplo, inventados). Proyecto «Mañana de feria», de un grupo de 4 estudiantes. "
     "Propósito expresivo: transmitir el bullicio alegre de una feria que se calma al final. "
     "Decisiones: forma ABA; ostinato rápido de percusión con objetos en A; sección B con notas largas; final con dinámica que decrece hasta el silencio. "
     "Evidencias disponibles: bitácora con 3 versiones y registro escrito de la presentación. "
     "Rúbrica del curso, con niveles de 1 a 4 en cada criterio: C1 relación entre propósito y decisiones; C2 aspectos estéticos (unidad, variedad y expresividad); C3 proceso (registro de versiones y ensayos); C4 comunicación (presentación y créditos). "
     "Niveles obtenidos por el grupo: C1, 3; C2, 4; C3, 2; C4, 3.")
build(
    O6, 1, F,
    use="Aprenderé a reconocer el propósito de un proyecto musical y a derivar de él criterios de evaluación observables, para evaluar procesos y resultados con evidencia.",
    prior=["Sé qué es un propósito expresivo.", "Sé usar criterios estéticos.", "Sé registrar versiones."],
    explain=[
        "Evaluar críticamente un proyecto musical es comparar lo que se hizo con lo que se quería lograr, y explicar con evidencia qué decisiones lo explican. No es solo poner una nota: implica decir cuánto se cumplió el propósito y por qué. Se evalúan dos cosas: el proceso (las decisiones, las versiones, el uso del tiempo) y el resultado (la obra terminada y el efecto que logra).",
        "Una rúbrica es una tabla con criterios y niveles de logro, descritos con rasgos observables. Un criterio observable se puede comprobar con evidencia: «el final tiene dinámica más suave que el comienzo» es observable; «la pieza es linda» no lo es. De un propósito se pueden derivar criterios: si el propósito es que la pieza se calme al final, el criterio observable puede ser que la dinámica y el ritmo se hagan más suaves y lentos en el último tramo.",
        "La evidencia puede ser del proceso (una bitácora con versiones, tiempos y razones de cambio) o del resultado (el registro escrito de la presentación). Una pieza muy lograda sin registro del proceso queda sin evidencia de cómo se tomaron las decisiones. Este cuaderno no usa grabaciones reales: la evidencia de ejemplo se describe por escrito.",
    ],
    vocab=[("evaluación crítica", "comparar lo hecho con el propósito y explicar con evidencia"), ("rúbrica", "tabla de criterios con niveles de logro observables"), ("criterio observable", "criterio que se puede comprobar con evidencia"),
           ("proceso", "decisiones, versiones y uso del tiempo al crear"), ("resultado", "obra terminada y el efecto que logra"), ("evidencia", "dato o registro que apoya una evaluación")],
    worked=[
        ("Derivar un criterio", "El propósito de un proyecto ficticio es «transmitir una carrera que se acelera». ¿Qué criterio observable se puede derivar?",
         ["Acelerarse se relaciona con el tempo y el ritmo.", "El criterio observable puede ser: el tempo aumenta o el ritmo se hace más rápido a lo largo de la pieza."],
         "El tempo o el ritmo se hacen más rápidos a lo largo de la pieza"),
        ("Sumar una rúbrica", "Una rúbrica de ejemplo tiene 3 criterios con niveles de 1 a 5. Un grupo obtiene 4, 5 y 3. ¿Cuántos puntos suma y cuántos le faltan para el máximo?",
         ["Suma 4 + 5 + 3 = 12 puntos.", "El máximo es 3 × 5 = 15, así que faltan 15 − 12 = 3 puntos."],
         "12 puntos; faltan 3"),
    ],
    mistakes=[("Usar criterios como «es linda» o «me gustó».", "No son observables y no se pueden comprobar.", "Deriva criterios del propósito que se puedan comprobar con evidencia."),
              ("Evaluar solo el resultado y no el proceso.", "No se ve cómo se tomaron las decisiones.", "Pide evidencia del proceso, como una bitácora con versiones.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es una rúbrica?', 'Una tabla de criterios con niveles de logro descritos con rasgos observables', 'Una lista de las personas que participan en el proyecto y de sus roles', 'Una pieza que se toca antes de comenzar para afinar a todo el grupo', 'La rúbrica ordena criterios y niveles de logro observables.'),
        ('abc', '{F} ¿Cuál es el propósito expresivo del proyecto «Mañana de feria»?', 'Transmitir el bullicio alegre de una feria que se calma al final', 'Mostrar el instrumento más difícil de tocar que el grupo pueda conseguir', 'Cumplir con una duración exacta de diez minutos, sin importar el efecto', 'La ficha declara ese propósito expresivo para el proyecto.'),
        ('abc', '{F} ¿Qué criterio de la rúbrica relaciona el propósito con las decisiones?', 'C1', 'C3', 'C4', 'C1 se define como relación entre propósito y decisiones.'),
        ('abc', '{F} ¿Cuál es una evidencia del proceso?', 'La bitácora con tres versiones', 'El registro escrito de la presentación', 'Los aplausos del público', 'La bitácora muestra cómo avanzó el trabajo.'),
        ('=', '{F} ¿Cuántos puntos suman los niveles obtenidos por el grupo en los cuatro criterios?', '3+4+2+3', 'Se suman los niveles de C1, C2, C3 y C4.', ' puntos'),
        ('abc', '{F} El criterio C2 evalúa:', 'Los aspectos estéticos: unidad, variedad y expresividad', 'El uso del tiempo de ensayo y el cumplimiento de los plazos del grupo', 'Los créditos y la forma en que se presenta el proyecto al público', 'La ficha define C2 como aspectos estéticos.'),
        ('=', '{F} Con 4 criterios de nivel máximo 4, ¿cuántos puntos le faltan al grupo para el máximo?', '4*4-(3+4+2+3)', 'Se calcula el máximo posible y se resta lo obtenido.', ' puntos'),
        ('abc', '{F} ¿Qué criterio observable se deriva del propósito «se calma al final»?', 'La dinámica y el ritmo se hacen más suaves y lentos en el último tramo', 'La pieza debe tener un final lindo y gustar a todas las personas', 'El grupo debe sentirse feliz al terminar de tocar la pieza', 'Se puede comprobar escuchando el final; los otros dos no se comprueban.'),
        ('abc', '¿Cuál de estos criterios es observable?', 'La melodía se repite tres veces y cambia en la cuarta', 'La pieza es hermosa y emociona a quienes la escuchan', 'La pieza gustó mucho al curso y por eso es buena', 'Se puede comprobar si la melodía se repite y cuándo cambia.'),
        ('abc', '¿Cuál es la diferencia entre evaluar el proceso y evaluar el resultado?', 'El proceso mira decisiones, versiones y uso del tiempo; el resultado mira la obra terminada y su efecto', 'No hay diferencia, porque en ambos casos se mira solo la obra terminada', 'El proceso es solo el ensayo general y el resultado es el ensayo anterior', 'Cada uno entrega evidencia distinta sobre el proyecto.'),
        ('abc', '{F} El grupo tiene muy buen resultado, pero no registró versiones. ¿Qué criterio se ve afectado?', 'C3, porque falta evidencia del proceso', 'C2, porque la estética se pierde', 'C4, porque no puede presentar', 'C3 evalúa el registro de versiones y ensayos.'),
        ('abc', 'Otro grupo declara «propósito: energía constante» y su pieza termina con un final muy suave. ¿Cómo se relaciona esto con la evaluación?', 'Hay una incoherencia entre la decisión del final y el propósito, que debe señalarse en el criterio que relaciona propósito y decisiones', 'No hay problema, porque cualquier final sirve a cualquier propósito expresivo', 'Es un problema solo del público, que no entendió lo que el grupo quería decir', 'La evaluación crítica compara decisiones con propósito.'),
        ('abc', '¿Por qué evaluar críticamente no es lo mismo que poner una nota?', 'Porque implica explicar con evidencia cuánto se logró el propósito y qué decisiones lo explican', 'Porque la nota no importa nunca y lo único relevante es el comentario', 'Porque la evaluación crítica no usa criterios ni evidencia, solo la impresión', 'La evaluación crítica da razones, no solo un puntaje.'),
    ],
    ctx=('abc', 'Antes de componer, tu curso acuerda una rúbrica con criterios observables. ¿Qué ventaja principal tiene hacerlo?', 'Todos saben qué se evaluará y pueden orientar sus decisiones al propósito', 'No se necesita registrar nada del proceso, porque la rúbrica ya lo guarda todo', 'Se evita evaluar el resultado y solo se mira cuánto tiempo trabajó el grupo', 'Conocer los criterios desde el inicio ayuda a decidir con claridad.'),
    sc=[
        ("En Composición musical: ¿qué es un criterio observable?", "Un criterio que se puede comprobar con evidencia", "Los criterios observables permiten verificar la evaluación."),
        ('abc', 'Evaluar el proceso implica mirar:', 'Las decisiones, las versiones y el uso del tiempo', 'Solo el volumen de la pieza y la cantidad de personas que la tocan', 'Solo el título de la obra y los nombres de quienes la presentan', 'El proceso son los pasos y decisiones de la creación.'),
        ("¿Qué se obtiene al derivar criterios del propósito?", "Criterios que permiten comprobar si la obra lo logra", "Los criterios derivados conectan la evaluación con lo que se quería lograr."),
    ],
    op=("Con la {F}, escribe dos criterios observables derivados del propósito de «Mañana de feria» y, para cada uno, qué evidencia (del proceso o del resultado) permitiría evaluarlo.",
        "Criterio 1: en la sección A el ritmo es rápido y los objetos suenan juntos; evidencia: registro escrito de la presentación. Criterio 2: el final baja la dinámica hasta el silencio; evidencia: bitácora que registra la decisión y su razón.",
        ["dos criterios observables", "derivados del propósito", "cada uno con una evidencia"],
        ["hoja con los dos criterios y sus evidencias"],
        ["criterios no observables, como «es lindo»", "no relacionar con el propósito", "no indicar evidencia"],
        "Pregunta: «¿cómo se comprobaría tu criterio?». Si no puede decirlo, pídele que lo escriba como algo que se oye."),
    reinforce="Escribe un propósito para una pieza imaginaria y deriva de él tres criterios observables.",
    extend="Explica con un ejemplo inventado por qué un resultado muy logrado puede evaluarse mal si no hay evidencia del proceso.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (bitácora y lista de cotejo de ejemplo, inventadas). Bitácora de un grupo: "
     "Lunes: «Probamos 3 ritmos para el ostinato (20 minutos). Elegimos el segundo porque se oye más claro.» "
     "Miércoles: «Variamos la melodía (25 minutos). La versión 2 suena más suave.» "
     "Viernes: «Ensayo general; el final no se entiende (15 minutos).» "
     "Lunes siguiente: «Cambiamos el final con una nota larga (30 minutos); el plan decía 20 minutos.» "
     "Lista de cotejo del proyecto: propósito escrito, sí; registro de 2 versiones, sí; créditos, no; plan de mejora, no. "
     "Tipos de evaluación: autoevaluación (evalúa quien hizo la obra), coevaluación (evalúan pares) y heteroevaluación (evalúa el docente u otra persona).")
build(
    O6, 2, F,
    use="Aprenderé a elegir y usar instrumentos de evaluación (bitácora, rúbrica, lista de cotejo, autoevaluación, coevaluación) para recoger evidencia del proceso y del resultado de un proyecto.",
    prior=["Sé qué es una rúbrica.", "Sé distinguir proceso y resultado.", "Sé que un criterio debe ser observable."],
    explain=[
        "Un instrumento de evaluación es una herramienta para recoger evidencia. La bitácora es un registro ordenado de lo que se hace en el proceso: fechas, decisiones, tiempos y resultados. La rúbrica evalúa qué tan bien se logra cada criterio, en varios niveles. La lista de cotejo verifica si algo está o no está (sí o no), por ejemplo si hay créditos. Cada una muestra aspectos distintos, así que conviene usar más de una.",
        "También se distingue quién evalúa. En la autoevaluación evalúa quien hizo la obra; en la coevaluación evalúan sus pares; en la heteroevaluación evalúa el docente u otra persona. Una evaluación se vuelve más completa cuando se combinan miradas. Cada evaluación debe apoyarse en evidencia, no en impresiones.",
        "Comparar versiones de una obra sirve para ver si una decisión mejoró el resultado. Con audio real se podrían oír ambas versiones; en este cuaderno no hay audio, así que se comparan los registros escritos de cada versión y las observaciones. La comparación con audio queda como complemento del trabajo en sala del docente.",
    ],
    vocab=[("bitácora", "registro ordenado de lo que se hace en el proceso"), ("lista de cotejo", "lista que verifica si algo está o no está"), ("autoevaluación", "evaluación que hace quien creó la obra"),
           ("coevaluación", "evaluación que hacen los pares"), ("heteroevaluación", "evaluación que hace otra persona, como el docente"), ("versión", "forma de la obra en un momento del proceso")],
    worked=[
        ("Elegir el instrumento", "Un grupo quiere saber rápidamente si su entrega incluye créditos, título y propósito escrito. ¿Qué instrumento conviene?",
         ["Se trata de comprobar si cada elemento está o no está.", "El instrumento adecuado es la lista de cotejo."],
         "Lista de cotejo"),
        ("Sumar tiempos de una bitácora", "Una bitácora ficticia registra sesiones de 15, 25 y 20 minutos. ¿Cuánto tiempo suma?",
         ["Se suman los minutos de las tres sesiones: 15 + 25 + 20.", "15 + 25 + 20 = 60 minutos."],
         "60 minutos"),
    ],
    mistakes=[("Usar un solo instrumento para evaluar todo.", "Cada instrumento muestra aspectos distintos del proyecto.", "Combina bitácora, rúbrica y lista de cotejo según lo que necesites evidenciar."),
              ("Confundir autoevaluación con coevaluación.", "Se olvida quién evalúa.", "Recuerda: auto, quien hizo la obra; co, los pares.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es una bitácora?', 'Un registro ordenado de fechas, decisiones, tiempos y resultados del proceso', 'La partitura final de la obra, con todas sus notas y sus compases', 'Una lista de los instrumentos del curso y sus rangos de notas', 'La bitácora muestra cómo avanzó el trabajo.'),
        ('abc', 'En Composición musical: ¿qué es la coevaluación?', 'Una evaluación que hacen los pares sobre el trabajo de otros', 'Una evaluación que hace solo el docente', 'Una evaluación que hace cada estudiante de su propio trabajo', 'En la coevaluación evalúan los pares.'),
        ('abc', '{F} ¿Qué día eligió el grupo el segundo ritmo del ostinato?', 'El lunes', 'El miércoles', 'El viernes', 'La primera entrada de la bitácora es del lunes.'),
        ('=', '{F} ¿Cuántos minutos suman las cuatro sesiones de la bitácora?', '20+25+15+30', 'Se suman los minutos de cada sesión registrada.', ' minutos'),
        ('abc', '{F} ¿Qué entrada de la bitácora muestra una decisión con su razón?', 'La del lunes: eligen el segundo ritmo porque se oye más claro', 'La del viernes: dice que hubo ensayo general y que el final no se entiende', 'La del miércoles: dice que la versión 2 suena más suave, sin explicar qué decisión se tomó', 'La entrada del lunes explica la decisión con una razón.'),
        ('=', '{F} La lista de cotejo tiene 4 ítems y 2 se cumplen. ¿Cuántos ítems no se cumplen?', '4-2', 'Se resta la cantidad de ítems cumplidos a los ítems totales.', ' ítems'),
        ('abc', '{F} ¿Qué instrumento sirve para comprobar si el proyecto tiene créditos y plan de mejora?', 'La lista de cotejo', 'La bitácora', 'La rúbrica de cuatro niveles', 'La lista de cotejo verifica si cada elemento está o no está.'),
        ('abc', '¿Qué instrumento sirve para evaluar en varios niveles qué tan bien se logra cada criterio?', 'La rúbrica', 'La lista de cotejo', 'La bitácora sin criterios', 'La rúbrica describe niveles de logro por criterio.'),
        ('abc', 'Un grupo comenta la pieza de otro con una pauta. ¿Qué tipo de evaluación es?', 'Coevaluación', 'Autoevaluación', 'Heteroevaluación', 'La hacen los pares del grupo evaluado.'),
        ('abc', '{F} La bitácora del viernes dice «el final no se entiende». ¿Qué evidencia aporta?', 'Evidencia del proceso: detectó un problema en el ensayo general', 'Evidencia del resultado final, porque ya se oye cómo quedó la pieza completa', 'Ninguna evidencia, porque un problema anotado no sirve para evaluar el proceso', 'Registra un problema observado durante el proceso.'),
        ('abc', '¿Por qué conviene usar más de un instrumento de evaluación?', 'Porque cada uno muestra aspectos distintos y se complementan', 'Porque así se gasta más papel y se ve que el grupo trabajó mucho', 'Porque uno solo nunca sirve y siempre hay que usar los cinco', 'Un instrumento por sí solo no recoge toda la evidencia.'),
        ('=', '{F} El ajuste del final tomó 30 minutos y el plan decía 20. ¿Cuántos minutos más tomó de lo planificado?', '30-20', 'Se resta la duración planificada a la duración real.', ' minutos'),
        ('abc', 'Sin audio, ¿cómo se comparan dos versiones de una obra en este cuaderno?', 'Con el registro escrito de cada versión y las observaciones, y la comparación con audio queda como complemento del docente', 'No se pueden comparar versiones nunca sin audio, así que no se evalúa el proceso', 'Con una grabación que el cuaderno trae incluida en cada clase para escuchar', 'El cuaderno no trae audio, por eso se comparan registros escritos.'),
    ],
    ctx=('abc', 'Tu grupo debe entregar una evaluación completa de su proyecto. ¿Qué combinación de instrumentos y miradas es la más completa?', 'Bitácora y rúbrica, con autoevaluación del grupo y coevaluación de otro grupo', 'Solo una lista de cotejo hecha por una persona, sin otras miradas ni niveles', 'Solo la opinión del público al final, sin registros del proceso ni criterios', 'Combina evidencia del proceso, niveles de logro y varias miradas.'),
    sc=[
        ("En Composición musical: ¿qué es una lista de cotejo?", "Una lista que verifica si algo está o no está", "La lista de cotejo responde sí o no a cada ítem."),
        ('abc', 'Cuando quien hizo la obra evalúa su propio trabajo, es una:', 'Autoevaluación', 'Coevaluación', 'Heteroevaluación', 'Auto indica que evalúa quien creó la obra.'),
        ("¿Por qué una bitácora ayuda a evaluar el proceso?", "Porque registra decisiones, razones y tiempos", "Sin registro no hay evidencia del proceso."),
    ],
    op=("Con la {F}, escribe una entrada de bitácora para un día de trabajo inventado de tu grupo (fecha, qué se hizo, cuántos minutos, qué decidieron y por qué). Después agrega dos ítems de lista de cotejo para el proyecto.",
        "Jueves: «Escribimos tres compases del final (25 minutos). Decidimos terminar con una nota larga porque el propósito es cerrar en calma.» Ítems de cotejo: título escrito, sí; créditos incluidos, no.",
        ["la entrada tiene fecha, tarea, tiempo, decisión y razón", "dos ítems de lista de cotejo", "razón relacionada con el propósito"],
        ["hoja con la entrada de bitácora y la lista de cotejo"],
        ["no registrar la razón", "olvidar el tiempo", "ítems de la lista que no son verificables"],
        "Pregunta: «¿qué razón escribiste para esa decisión?». Si no la tiene, pídele que vuelva al propósito."),
    reinforce="Escribe tres entradas de bitácora de una semana inventada de trabajo en una pieza y suma los minutos.",
    extend="Explica con un ejemplo inventado cómo cambiarían las conclusiones si solo se usara la autoevaluación.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (bitácora de versiones de ejemplo, inventada). Pieza «Orilla», con propósito «cerrar en calma». Tempo: 100 pulsos por minuto. "
     "V1: | Do Mi Sol Mi | | Do Mi Sol Mi | | Do Mi Sol Mi | | Do Mi Sol Mi |; tiempo planificado, 20 minutos; tiempo real, 30 minutos. "
     "V2: se agregó variación; el compás 3 queda | Do Mi Sol Sol | y el compás 4 queda | La - Sol - |; razón registrada: «el grupo notó monotonía»; tiempo planificado, 25 minutos; tiempo real, 25 minutos. "
     "V3: se bajó la dinámica del compás 4; razón registrada: «cerrar en calma»; tiempo planificado, 20 minutos; tiempo real, 35 minutos. " + CLAVE)
build(
    O6, 3, F,
    use="Aprenderé a evaluar el proceso de creación de un proyecto: sus decisiones, sus razones, sus versiones y el uso del tiempo, con evidencia.",
    prior=["Sé usar una bitácora.", "Sé qué es un propósito.", "Sé reconocer repetición y variación."],
    explain=[
        "Evaluar el proceso es revisar cómo se llegó a la obra. Una decisión de proceso está justificada cuando se hizo por una razón relacionada con el propósito y existe un registro que la muestra. Por ejemplo, si el grupo agregó una variación porque notó monotonía, la decisión tiene razón. Si no hay razón escrita, la decisión puede ser buena, pero no se puede evaluar si respondió al propósito.",
        "El uso del tiempo también es evidencia del proceso. Se compara el tiempo planificado con el tiempo real de cada versión. Una diferencia grande no significa necesariamente un mal proceso: hay que ver por qué ocurrió y si el tiempo extra mejoró el resultado. Una versión más reciente no es mejor por ser más reciente: se compara cada versión con el propósito.",
        "Conviene registrar cuatro cosas en cada versión: qué cambió, por qué, cuánto tardó y qué resultado tuvo. Con esos datos otra persona puede evaluar el proceso sin haber estado presente. Todo esto se hace por escrito, con la notación de pulsos del cuaderno.",
    ],
    vocab=[("decisión de proceso", "cambio que se hace al crear para acercarse al propósito"), ("justificada", "con una razón relacionada con el propósito y un registro"), ("tiempo planificado", "minutos que se pensaba usar"),
           ("tiempo real", "minutos que efectivamente se usaron"), ("versión", "forma de la obra en un momento del proceso"), ("monotonía", "falta de cambios que cansa")],
    worked=[
        ("Evaluar una decisión", "Una entrada ficticia dice: «Subimos el tempo de la pieza porque el propósito es transmitir energía». ¿Está justificada la decisión?",
         ["Hay una razón relacionada con el propósito: transmitir energía.", "Hay un registro que la muestra, así que la decisión está justificada."],
         "Sí, está justificada"),
        ("Comparar tiempos", "Una versión ficticia se planificó en 30 minutos y tomó 45. ¿Cuántos minutos más tomó?",
         ["Se resta lo planificado a lo real: 45 − 30.", "45 − 30 = 15 minutos."],
         "15 minutos más"),
    ],
    mistakes=[("Pensar que la última versión es la mejor por ser la más reciente.", "No se compara con el propósito.", "Compara cada versión con el propósito y con la evidencia."),
              ("Juzgar mal un proceso solo por haber tardado más.", "El tiempo extra puede haber mejorado el resultado.", "Revisa por qué se tardó más y qué cambió en la versión.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es una decisión de proceso justificada?', 'Un cambio hecho por una razón relacionada con el propósito y registrado', 'Un cambio hecho al azar para probar si ocurre algo mejor en la obra', 'Un cambio que le gustó a una persona del grupo, aunque no haya razón escrita', 'Una decisión justificada tiene razón y registro.'),
        ('abc', '{F} ¿Qué decisión llevó de V1 a V2?', 'Agregar variación al compás 3 y al compás 4', 'Bajar la dinámica del compás 4 para que la pieza cierre en calma', 'Subir el tempo de toda la pieza para que se note menos la monotonía', 'La ficha dice que V2 agregó variación.'),
        ('abc', '{F} ¿Por qué se hizo esa decisión según la bitácora?', 'Porque el grupo notó monotonía', 'Porque el docente la pidió', 'Porque faltaba tiempo', 'La razón registrada es la monotonía.'),
        ('abc', '{F} ¿Qué decisión llevó de V2 a V3?', 'Bajar la dinámica del compás 4', 'Agregar un compás más con notas nuevas para alargar el cierre', 'Cambiar el tempo de toda la pieza para que termine más rápido', 'La ficha dice que V3 bajó la dinámica del compás 4.'),
        ('=', '{F} ¿Cuántos minutos se habían planificado en total para las tres versiones?', '20+25+20', 'Se suman los minutos planificados para V1, V2 y V3.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos reales tomaron las tres versiones en total?', '30+25+35', 'Se suman los minutos reales de V1, V2 y V3.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos más de lo planificado tomó el proceso completo?', '(30+25+35)-(20+25+20)', 'Se resta el tiempo planificado total al tiempo real total.', ' minutos'),
        ('abc', '{F} ¿En qué versión fue mayor la diferencia entre el tiempo real y el planificado?', 'V3, con 15 minutos más', 'V1, con 10 minutos más', 'V2, con 5 minutos más', 'V3 tomó 35 minutos frente a 20 planificados, 15 más; V1 tomó 10 más; V2 no tuvo diferencia.'),
        ('abc', '{F} ¿Qué relación tiene el compás 3 de V2 con el de V1?', 'Es una variación: cambia solo la última nota', 'Es una repetición exacta, porque conserva tres de las cuatro notas', 'Es un contraste total, porque cambia la última nota del compás', 'Do Mi Sol Mi pasa a Do Mi Sol Sol; solo cambia la última nota.'),
        ('abc', 'Una decisión no tiene ninguna razón escrita. ¿Qué se puede decir al evaluar el proceso?', 'Puede haber sido buena, pero no se puede evaluar si respondió al propósito', 'Fue mala seguro, porque sin razón escrita nada de lo que se haga sirve', 'Fue buena seguro, porque el grupo la tomó y eso es suficiente para evaluarla', 'Sin razón registrada no hay evidencia para evaluarla.'),
        ('abc', '{F} V3 tomó 15 minutos más de lo planificado. ¿Qué conclusión es más razonable?', 'No se puede decir que fue un mal proceso sin ver por qué se tardó y si el tiempo extra mejoró el resultado', 'Fue un mal proceso, sin dudas, porque tardó más de lo que se había planificado', 'Fue un buen proceso, sin dudas, porque trabajar más tiempo siempre mejora la obra', 'El tiempo es solo una parte de la evidencia del proceso.'),
        ('abc', '{F} Alguien afirma que V3 es mejor que V1 porque es más reciente. ¿Qué falla?', 'Ser más reciente no prueba que sea mejor; hay que comparar con el propósito', 'Nada, porque la última versión siempre es mejor que las anteriores', 'Que V3 no tiene compases escritos que se puedan comparar con V1', 'Cada versión se evalúa con el propósito y con evidencia.'),
        ('abc', '¿Qué conviene registrar en cada versión para evaluar mejor el proceso?', 'Qué cambió, por qué, cuánto tardó y qué resultado tuvo', 'Solo cuánto tardó cada versión, porque lo demás se ve en la obra terminada', 'Solo qué cambió, sin anotar la razón ni cuánto tiempo se usó en el cambio', 'Los cuatro datos juntos permiten evaluar la decisión.'),
    ],
    ctx=('=', 'Un grupo planificó 4 sesiones de 25 minutos y trabajó 3 sesiones de 30 minutos. ¿Cuántos minutos menos de los planificados trabajó?', '4*25-3*30', 'Se calcula el tiempo planificado y el tiempo real y se restan.', ' minutos'),
    sc=[
        ("En Composición musical: ¿qué es el tiempo real de una versión?", "Los minutos que efectivamente se usaron", "El tiempo real se compara con el planificado."),
        ('abc', 'Una decisión sin razón escrita:', 'No se puede evaluar si respondió al propósito', 'Siempre es buena, porque el grupo la tomó con convicción', 'Siempre es mala, porque si no hay razón escrita no es una decisión válida', 'Sin razón no hay evidencia para evaluarla.'),
        ("¿Qué se compara para evaluar una versión?", "La versión y el propósito, con evidencia", "No se evalúa por ser reciente sino por responder al propósito."),
    ],
    op=("Con la {F}, escribe una evaluación breve del proceso de «Orilla»: una decisión bien justificada, una evidencia del uso del tiempo y una pregunta que le harías al grupo para entender mejor un dato.",
        "Decisión bien justificada: agregar variación en V2 porque el grupo notó monotonía. Tiempo: V3 tomó 15 minutos más de lo planificado. Pregunta: «¿Qué cambios tomaron más tiempo en V3 y mejoraron el cierre en calma?».",
        ["una decisión justificada con su razón", "una evidencia de tiempo con datos de la ficha", "una pregunta que busca entender el dato"],
        ["hoja con la evaluación y la pregunta"],
        ["juzgar solo por el tiempo", "no citar la razón registrada", "preguntas que atacan al grupo"],
        "Pregunta: «¿en qué dato de la ficha te apoyas?». Si no lo menciona, pídele que lo cite."),
    reinforce="Escribe una bitácora de tres versiones de un motivo de cuatro pulsos con una razón para cada cambio.",
    extend="Explica con un ejemplo inventado cuándo tardar más de lo planificado mejora el resultado de un proyecto.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (pieza de un par y comentarios de ejemplo, inventados). Pieza «Tarde de lluvia», de otro grupo del curso. Propósito: transmitir una tarde tranquila con lluvia. "
     "Resultado: botella plástica con arroz que imita la lluvia; flauta con melodía lenta; ostinato suave de caja; forma ABA con secciones de 8 compases; 4 pulsos por compás; 60 pulsos por minuto; dinámica suave en general. "
     "Problema observado: en la sección B (compases 9 a 16) la caja sube de volumen y tapa a la flauta. "
     "Comentarios de pares: P1, «Está bonita.» P2, «La sección B no cumple lo tranquilo porque la caja suena más fuerte que la flauta; prueben bajar la caja en los compases 9 a 16.» P3, «Les falló el propósito.»")
build(
    O6, 4, F,
    use="Aprenderé a evaluar el resultado de una obra frente a su propósito y a dar retroalimentación a pares que reconozca logros y proponga mejoras con respeto y evidencia.",
    prior=["Sé usar criterios observables.", "Sé dar retroalimentación con observación, efecto y sugerencia.", "Sé que una obra tiene un propósito expresivo."],
    explain=[
        "Evaluar el resultado de una obra es comparar lo logrado con el propósito expresivo, usando evidencia audible o registrada. Se pregunta: ¿qué rasgos de la obra cumplen el propósito?, ¿cuáles no?, ¿en qué compases? La evaluación crítica es proporcionada: si un problema ocurre en una sección, se señala en esa sección y no se concluye que toda la obra falla. También reconoce lo que sí se logra.",
        "Al evaluar el trabajo de un par se da retroalimentación con tres partes: una observación (qué se oye y dónde), un efecto (qué produce respecto del propósito) y una sugerencia (qué se podría probar). Se empieza reconociendo un logro concreto, se señala una mejora específica y se propone cómo comprobarla. Se habla de la obra, nunca de la persona, y se evitan frases vagas como «está bonita» o «les falló», que no dicen qué hacer.",
        "Quien recibe la retroalimentación la compara con su propósito y decide qué incorporar. Para comprobar una sugerencia se vuelve a tocar el trozo señalado y se verifica si el problema se resolvió. Todo esto se puede hacer por escrito con las observaciones de la ficha, sin audio real.",
    ],
    vocab=[("resultado", "obra terminada y el efecto que logra"), ("evaluación proporcionada", "evaluación que señala el problema donde ocurre y reconoce lo logrado"), ("observación", "descripción de lo que se oye y dónde"),
           ("efecto", "lo que produce un rasgo respecto del propósito"), ("sugerencia", "cambio que se propone probar"), ("logro", "aspecto que sí cumple el propósito")],
    worked=[
        ("Reconocer un logro y una mejora", "Una pieza ficticia debe sonar «solemne». Tiene tempo lento y notas largas, pero un ritmo de percusión muy movido en el compás 5. ¿Qué logro y qué mejora se señalan?",
         ["El logro es el tempo lento y las notas largas, que se relacionan con lo solemne.", "La mejora es el ritmo movido del compás 5, que contradice el propósito."],
         "Logro: tempo lento y notas largas; mejora: ritmo movido del compás 5"),
        ("Calcular la duración", "Una sección ficticia tiene 6 compases de 4 pulsos a 80 pulsos por minuto. ¿Cuántos segundos dura?",
         ["Son 6 × 4 = 24 pulsos.", "A 80 pulsos por minuto, 24 pulsos duran 24 × 60 ÷ 80 = 18 segundos."],
         "18 segundos"),
    ],
    mistakes=[("Concluir que toda la obra falla por un problema en una sección.", "Se generaliza y no se reconoce lo logrado.", "Señala el problema donde ocurre y reconoce lo que sí funciona."),
              ("Dar comentarios vagos como «está bonita».", "No dicen qué se oye ni qué se puede mejorar.", "Escribe qué observas, qué efecto produce y qué probarías.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es evaluar el resultado de una obra?', 'Comparar lo logrado con el propósito expresivo usando evidencia', 'Contar cuántas veces se tocó la pieza antes de la presentación', 'Decidir quién es mejor intérprete dentro del grupo que la presentó', 'Evaluar el resultado compara la obra con su propósito.'),
        ('abc', '{F} ¿Cuál es el propósito de «Tarde de lluvia»?', 'Transmitir una tarde tranquila con lluvia', 'Mostrar una percusión muy fuerte', 'Hacer una pieza de baile', 'La ficha declara ese propósito expresivo para el proyecto.'),
        ('abc', '{F} ¿Qué rasgos de la pieza cumplen el propósito?', 'El tempo lento, la dinámica suave y la botella que imita la lluvia', 'La caja que sube de volumen en la sección B y tapa a la flauta', 'Ninguno de los rasgos de la pieza cumple el propósito de una tarde tranquila', 'Esos rasgos coinciden con una tarde tranquila con lluvia.'),
        ('abc', '{F} ¿Qué rasgo no cumple el propósito?', 'La caja que sube de volumen en la sección B y tapa la flauta', 'La botella con arroz, que imita la lluvia y mantiene la calma de la pieza', 'La melodía lenta de la flauta, que sostiene la tranquilidad de la sección A', 'La caja fuerte contradice lo tranquilo.'),
        ('=', '{F} La pieza tiene 24 compases de 4 pulsos a 60 pulsos por minuto. ¿Cuántos segundos dura?', '24*4*60//60', 'Se calculan los pulsos totales y se pasan a segundos con los pulsos por minuto.', ' s'),
        ('=', '{F} La sección B tiene 8 compases de 4 pulsos a 60 pulsos por minuto. ¿Cuántos segundos dura?', '8*4*60//60', 'Se calculan los pulsos de la sección y se pasan a segundos.', ' s'),
        ('abc', '{F} ¿Qué comentario tiene observación, efecto y sugerencia?', 'P2', 'P1', 'P3', 'P2 dice qué se oye, qué efecto produce y qué probar.'),
        ('abc', '{F} ¿Por qué P1, «está bonita», no es útil para mejorar?', 'Porque no dice qué se oye ni qué se podría cambiar', 'Porque es demasiado largo y no se alcanza a leer en la clase', 'Porque solo habla de la sección B y deja de lado el resto de la pieza', 'Un comentario útil nombra rasgos y propone cambios.'),
        ('abc', '{F} ¿Qué le falta a P3, «les falló el propósito»?', 'Decir en qué compases y por qué, con evidencia', 'Decir cuántas personas lo oyeron y cuántas aplaudieron al terminar', 'Agregar más adjetivos para que el comentario suene más seguro', 'Un juicio crítico se apoya en evidencia y ubicación.'),
        ('abc', '{F} ¿Cuál es la sugerencia más respetuosa y útil?', 'Prueben bajar la caja en los compases 9 a 16 para que se oiga la flauta', 'Deben rehacer toda la pieza desde el principio con otros instrumentos', 'Esa caja nunca debió usarse, porque tapa a la flauta en cualquier pieza', 'La primera señala dónde y qué probar sin juzgar a las personas.'),
        ('abc', '{F} Alguien dice: «como B falla, toda la pieza falla». ¿Qué falla en esa evaluación?', 'Generaliza: el problema ocurre en 8 de los 24 compases y no reconoce lo logrado', 'Nada, porque un problema en una sección invalida el resto de la pieza', 'Que la pieza tiene demasiados compases para poder evaluarla con criterios', 'La evaluación crítica es proporcionada y no generaliza un problema local.'),
        ('abc', '{F} El grupo acepta P2. ¿Cómo comprueba que la sugerencia funcionó?', 'Vuelve a tocar la sección B con la caja más baja y comprueba si se oye la flauta', 'Asume que funcionó, porque quien comentó parecía estar seguro de su sugerencia', 'Cambia toda la pieza sin probar, para estar seguro de que el problema desaparezca', 'Se verifica volviendo a tocar el trozo señalado.'),
        ('abc', 'Al evaluar a un par con respeto, ¿qué conviene incluir?', 'Un logro concreto y una mejora específica con una sugerencia', 'Solo críticas, porque los elogios no sirven para mejorar una pieza', 'Solo elogios, para que el grupo evaluado no se sienta mal con el comentario', 'Reconocer lo logrado y proponer una mejora hace útil el comentario.'),
    ],
    ctx=('abc', 'Debes evaluar la pieza de un compañero que no logró su propósito de calma porque toca todo fuerte. ¿Cuál es la mejor manera de comenzar tu comentario?', 'Reconocer un logro concreto y luego señalar con ejemplos dónde la dinámica contradice la calma', 'Decir que todo está mal desde el principio para que quede clara la crítica', 'No decir nada para no incomodar, aunque se note que la pieza no cumple su propósito', 'Un comentario respetuoso y útil reconoce un logro y ubica el problema.'),
    sc=[
        ("En Composición musical: ¿qué es una evaluación proporcionada?", "Una evaluación que señala el problema donde ocurre y reconoce lo logrado", "No generaliza un problema local a toda la obra."),
        ('abc', 'Una buena retroalimentación se dirige:', 'A la obra y no a la persona', 'A la persona y no a la obra', 'A nadie en particular', 'Se critica la obra para ayudar a mejorarla.'),
        ("¿Cómo se comprueba una sugerencia?", "Volviendo a tocar el trozo señalado y verificando si el problema se resolvió", "Sin probarla no se sabe si funcionó."),
    ],
    op=("Con la {F}, escribe una retroalimentación de tres partes para el grupo de «Tarde de lluvia» sobre un logro y una mejora diferentes de los de P2. Debe tener observación, efecto y sugerencia y referirse a un compás o sección.",
        "Logro: la botella con arroz imita la lluvia y sostiene la calma en la sección A. Mejora: la melodía de la flauta empieza muy bajito en el compás 1 y cuesta oírla; prueben acercarla un poco al grupo o subir un punto su dinámica.",
        ["observación, efecto y sugerencia", "refiere a un compás o sección", "habla de la obra y no de las personas", "distinto de P2"],
        ["hoja con la retroalimentación escrita"],
        ["comentarios vagos", "criticar a las personas", "no proponer una sugerencia concreta"],
        "Pregunta: «¿dónde de la pieza se observa lo que dices?». Si no lo ubica, pídele que indique el compás."),
    reinforce="Escribe tres frases de retroalimentación sobre una canción que conozcas: un logro, un efecto y una sugerencia.",
    extend="Explica con un ejemplo inventado cómo una crítica muy general puede ayudar menos que una específica aunque sea amable.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (hallazgos de una evaluación, de ejemplo). Después de evaluar «Tarde de lluvia», el grupo anotó cuatro hallazgos con su impacto en el propósito (3 es alto, 2 medio, 1 bajo) y el tiempo de trabajo que necesitan. "
     "H1: la caja tapa a la flauta en la sección B; impacto 3; 10 minutos. "
     "H2: el final no se entiende; impacto 2; 20 minutos. "
     "H3: faltan los créditos; impacto 1; 5 minutos. "
     "H4: cambiar el título; impacto 1; 20 minutos. "
     "Tiempo disponible antes de la próxima clase: 30 minutos.")
build(
    O6, 5, F,
    use="Aprenderé a convertir una evaluación en un plan de mejora priorizado, a recibir críticas con apertura y a hacer una reflexión final sobre mis decisiones.",
    prior=["Sé evaluar proceso y resultado.", "Sé dar retroalimentación.", "Sé registrar versiones y ajustes."],
    explain=[
        "Un plan de mejora convierte una evaluación en acciones: qué se cambiará, por qué y cómo se comprobará. Como casi nunca alcanza el tiempo para todo, se priorizan los hallazgos: se eligen los que más ayudan al propósito y caben en el tiempo disponible. Un hallazgo de alto impacto y poco esfuerzo se hace primero; uno de bajo impacto y mucho esfuerzo se deja para después.",
        "Recibir críticas es parte de evaluar un proyecto. Conviene escuchar la crítica completa, pedir un ejemplo audible si no se entiende, compararla con el propósito y decidir qué incorporar. Una crítica es sobre la obra, no sobre la persona. Si una crítica te afecta mucho, hacer una pausa y conversar con una persona adulta de confianza ayuda a volver a revisarla con calma.",
        "La reflexión final cierra el proyecto: qué decisiones repetirías, cuáles cambiarías y qué evidencia las apoya. Después de aplicar un plan de mejora se comprueba si el problema se resolvió volviendo a tocar el trozo señalado. Este cuaderno trabaja por escrito, sin audio, por lo que la comprobación con audio queda como complemento del docente.",
    ],
    vocab=[("plan de mejora", "acciones para cambiar la obra o el proceso a partir de la evaluación"), ("priorizar", "ordenar lo que se hace según su importancia y el tiempo"), ("impacto", "cuánto ayuda un cambio al propósito"),
           ("esfuerzo", "tiempo y trabajo que toma un cambio"), ("reflexión final", "balance de las decisiones tomadas y lo aprendido"), ("crítica", "comentario que evalúa una obra o un proceso")],
    worked=[
        ("Priorizar con poco tiempo", "Un grupo ficticio tiene 20 minutos y dos hallazgos: X (impacto 3, 15 minutos) e Y (impacto 1, 5 minutos). ¿Qué hallazgos puede hacer y cuál prioriza?",
         ["Los dos suman 15 + 5 = 20 minutos, así que caben justo en el tiempo.", "Se hace primero X, que tiene el mayor impacto, y luego Y."],
         "Puede hacer ambos; prioriza X"),
        ("Sumar el esfuerzo", "Tres tareas de un plan ficticio toman 8, 12 y 15 minutos. ¿Cuánto tiempo necesitan en total?",
         ["Se suman los minutos: 8 + 12 + 15.", "8 + 12 + 15 = 35 minutos."],
         "35 minutos"),
    ],
    mistakes=[("Intentar cambiar todo a la vez.", "El tiempo no alcanza y no se sabe qué cambio funcionó.", "Prioriza los cambios de mayor impacto que caben en el tiempo."),
              ("Tomar una crítica como un ataque personal.", "Se confunde la obra con la persona.", "Escucha, pide un ejemplo y compara con el propósito; si te afecta mucho, conversa con una persona adulta de confianza.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un plan de mejora?', 'Acciones para cambiar la obra o el proceso a partir de la evaluación', 'La nota final de un proyecto, que resume cuánto se logró en una cifra', 'Una lista de los comentarios que gustaron más al grupo durante la presentación', 'El plan de mejora transforma la evaluación en acciones.'),
        ('abc', '{F} ¿Cuál hallazgo tiene el mayor impacto en el propósito?', 'H1, la caja que tapa a la flauta', 'H3, los créditos, porque es lo que más ayuda a que el resultado cumpla el propósito', 'H4, el título, porque cambia lo que el público piensa de la pieza', 'H1 tiene impacto 3, el más alto.'),
        ('abc', '{F} ¿Cuál hallazgo toma menos tiempo?', 'H3, con 5 minutos', 'H1, con 10 minutos', 'H2, con 20 minutos', 'H3 es el de menor esfuerzo.'),
        ('=', '{F} ¿Cuántos minutos suman las cuatro tareas?', '10+20+5+20', 'Se suman los minutos que necesita cada hallazgo.', ' minutos'),
        ('=', '{F} Si se quisieran hacer los cuatro hallazgos, ¿cuántos minutos faltarían respecto de los 30 disponibles?', '10+20+5+20-30', 'Se resta el tiempo disponible al tiempo total que necesitan las tareas.', ' minutos'),
        ('abc', '{F} ¿Qué combinación de hallazgos cabe en 30 minutos y logra el mayor impacto total?', 'H1 y H2', 'H1 y H3', 'H2 y H3', 'H1 y H2 suman 30 minutos y un impacto de 5; las otras combinaciones suman menos impacto.'),
        ('=', '{F} ¿Cuánto impacto suman H1 y H2?', '3+2', 'Se suman los impactos de los dos hallazgos.', ' puntos'),
        ('abc', '{F} ¿Qué combinación no cabe en el tiempo disponible?', 'H1, H2 y H3, que suman 35 minutos', 'H1 y H2, que suman 30 minutos', 'H1 y H3, que suman 15 minutos', 'Tres hallazgos suman más de 30 minutos solo en el primer caso.'),
        ('abc', '¿Cómo conviene recibir una crítica a tu obra?', 'Escuchar completa, pedir un ejemplo si no se entiende y decidir con el propósito', 'Interrumpir para defenderse y explicar cada decisión antes de oír el resto', 'Ignorarla si no gusta y seguir con lo planificado sin cambiar nada', 'Escuchar y comparar con el propósito permite decidir con criterio.'),
        ('abc', 'Una crítica te hizo sentir mal y no logras concentrarte. ¿Qué conviene hacer?', 'Hacer una pausa y conversar con una persona adulta de confianza, y luego volver a revisarla con calma', 'Guardarlo en secreto y no volver a componer para no sentirse mal otra vez', 'Responder con enojo al grupo que dio la crítica para dejar clara la molestia', 'Pedir apoyo y volver con calma cuida el bienestar y permite aprovechar la crítica.'),
        ('abc', '{F} ¿Por qué se prioriza H1 antes que H4?', 'Porque H1 tiene mayor impacto en el propósito y toma menos tiempo', 'Porque el título siempre es menos importante que cualquier otro aspecto de la pieza', 'Porque H1 es el hallazgo más fácil de entender para todo el grupo', 'H1 mejora más el resultado con menos esfuerzo.'),
        ('abc', '¿Qué pregunta es más útil para una reflexión final?', '¿Qué decisión repetiría y cuál cambiaría, y qué evidencia tengo?', '¿Quién fue la mejor persona del grupo en el proyecto, y quién la peor?', '¿Cuánta gente me felicitó al terminar y cuánta gente se quedó en silencio?', 'La reflexión final busca aprender de las decisiones con evidencia.'),
        ('abc', '{F} Tras aplicar H1 y H2, ¿cómo se comprueba el resultado?', 'Volviendo a tocar la sección B y el final y comparándolos con el propósito y con la observación anterior', 'Asumiendo que funcionó, porque se hizo el cambio que se había propuesto', 'Cambiando otra vez toda la pieza, para estar seguro de que quede distinta', 'Se verifica en el trozo señalado y con el propósito.'),
    ],
    ctx=('abc', 'Tu grupo tiene 25 minutos y tres tareas: A (impacto 3, 20 minutos), B (impacto 2, 10 minutos) y C (impacto 1, 5 minutos). ¿Qué combinación logra más impacto dentro del tiempo?', 'A y C, con 25 minutos e impacto 4', 'A y B, con 30 minutos e impacto 5', 'B y C, con 15 minutos e impacto 3', 'A y B no caben en 25 minutos; A y C suman 25 minutos y tienen más impacto que B y C.'),
    sc=[
        ("En Composición musical: ¿qué es priorizar?", "Ordenar lo que se hace según su importancia y el tiempo disponible", "Priorizar permite elegir primero lo que más ayuda al propósito."),
        ('abc', 'Un hallazgo de alto impacto y poco esfuerzo se hace:', 'Primero', 'Al final', 'Nunca', 'Es el que más ayuda con menos trabajo.'),
        ("¿Qué incluye una reflexión final?", "Qué decisiones repetir, cuáles cambiar y qué evidencia las apoya", "Cierra el proyecto con aprendizajes basados en evidencia."),
    ],
    op=("Con la {F}, arma un plan de mejora para 30 minutos: elige los hallazgos que harás, di en qué orden y cómo comprobarás cada uno. Escribe además una pregunta de reflexión final para tu grupo.",
        "Haré primero H1 (10 minutos): bajar la caja en los compases 9 a 16; lo comprobaré tocando de nuevo la sección B. Luego H2 (20 minutos): cambiar el final con una nota larga; lo comprobaré tocando el cierre y comparándolo con el propósito. Pregunta: «¿qué decisión de este proyecto repetiríamos y por qué?».",
        ["elige hallazgos que caben en 30 minutos", "ordena por impacto", "indica cómo comprobar cada uno", "incluye una pregunta de reflexión"],
        ["hoja con el plan, la comprobación y la pregunta"],
        ["elegir más tareas de las que caben", "no indicar cómo comprobar", "elegir por gusto y no por impacto"],
        "Pregunta: «¿por qué elegiste ese orden?». Si no usa impacto y tiempo, pídele que los incluya."),
    reinforce="Haz un plan de mejora con tres hallazgos inventados de una pieza, con impacto y minutos, y elige cuáles caben en 25 minutos.",
    extend="Explica con un ejemplo inventado cuándo conviene dejar sin hacer un hallazgo de poco impacto aunque sea fácil.",
)
