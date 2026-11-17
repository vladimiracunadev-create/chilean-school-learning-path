"""Ciencias del ejercicio físico y deportivo, 3.º y 4.º medio HC: OAC-05 (diseñar y aplicar sistemas de entrenamiento), clases 1 a 5, y OAC-06 (factores fisiológicos, biomecánicos, psicológicos y sociológicos del rendimiento), clases 1 a 5. Datos de ejemplo escritos en cada enunciado; sin cargas ni acrobacias."""
from __future__ import annotations

from hc_cefd_common import build

O5 = "EF-CEFD-3y4-OAC-05"
O6 = "EF-CEFD-3y4-OAC-06"

# ============================================================ OAC-05, clase 1
F = ("Ficha 20 (demandas de ejemplo de tres situaciones deportivas, descritas en general). "
     "Prueba A: carrera de velocidad muy corta, de unos pocos segundos, con esfuerzo máximo. Prueba B: carrera continua larga, de más de 40 minutos, a ritmo estable. "
     "Prueba C: partido de un deporte con pelota, con carreras cortas, pausas y cambios de ritmo durante un tiempo largo. "
     "Capacidades: velocidad (moverse rápido), resistencia (sostener un esfuerzo), fuerza, flexibilidad y coordinación.")
build(
    O5, 1, F,
    use="Aprenderé a diagnosticar lo que pide un deporte (duración, intensidad, pausas y capacidades) antes de diseñar un sistema de entrenamiento, y a hacerlo con seguridad y de forma privada.",
    prior=["Sé qué es una meta medible.", "Sé describir un programa con FITT.", "Conozco las señales de detención."],
    explain=[
        "Un sistema de entrenamiento es una forma organizada de repartir esfuerzo y pausas en una sesión para trabajar una capacidad. Antes de diseñarlo se diagnostica la demanda del deporte: cuánto dura, qué tan intenso es, si hay pausas y qué capacidades predominan, como velocidad, resistencia, fuerza, flexibilidad o coordinación.",
        "El cuerpo obtiene energía de varias formas que funcionan siempre juntas, pero con distinto predominio. En los esfuerzos muy cortos y máximos predomina la energía anaeróbica, de uso inmediato, que no depende del oxígeno en ese momento. En los esfuerzos largos y estables predomina la energía aeróbica, que usa oxígeno. En deportes con carreras cortas, pausas y cambios de ritmo participan ambas, y el trabajo es mixto.",
        "El diagnóstico sirve para que el entrenamiento se parezca a la demanda del deporte (especificidad). Es privado y no evalúa cuerpos. En cualquier prueba o sesión se hace calentamiento, se lleva agua y, ante dolor, mareo o falta de aire inusual, se detiene la actividad y se avisa a una persona adulta o a un profesional de la salud.",
    ],
    vocab=[("sistema de entrenamiento", "forma organizada de repartir esfuerzo y pausas"), ("demanda del deporte", "lo que el deporte exige: duración, intensidad, pausas y capacidades"), ("aeróbico", "esfuerzo que se sostiene sobre todo con oxígeno"), ("anaeróbico", "esfuerzo de uso inmediato que no depende del oxígeno en ese momento"), ("trabajo mixto", "esfuerzos con participación de ambas formas de energía")],
    worked=[
        ("Diagnosticar una demanda", "Una prueba de ejemplo dura 3 horas a ritmo estable. ¿Qué capacidad y qué energía predominan?", ["Es un esfuerzo muy largo y estable.", "Predomina la resistencia y la energía aeróbica."], "Resistencia y energía aeróbica"),
        ("Reconocer un trabajo mixto", "En un juego de ejemplo hay 5 segundos de carrera, 20 segundos de pausa y se repite durante una hora. ¿Qué tipo de trabajo es?", ["Alterna esfuerzos cortos y pausas.", "Es un trabajo mixto, con ambas formas de energía."], "Trabajo mixto"),
    ],
    mistakes=[("Decir que en un esfuerzo largo se usa «solo» energía aeróbica.", "Todas las formas de energía funcionan juntas; cambia cuál predomina.", "Habla de predominio, no de exclusividad."),
              ("Entrenar sin mirar lo que pide el deporte.", "El entrenamiento pierde especificidad.", "Diagnostica duración, intensidad, pausas y capacidades.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es un sistema de entrenamiento?', 'Una forma organizada de repartir esfuerzo y pausas para una capacidad', 'Una lista de ejercicios sin ningún orden que se repite siempre', 'Una prueba final para comparar a las personas del mismo grupo', 'Un sistema organiza esfuerzo y pausas; no es una lista sin orden ni una comparación.'),
        ('abc', '{F} ¿Qué capacidad predomina en la prueba A?', 'La velocidad', 'La flexibilidad', 'La resistencia', 'Un esfuerzo máximo de pocos segundos exige sobre todo velocidad.'),
        ('abc', '{F} ¿Qué capacidad predomina en la prueba B?', 'La resistencia', 'La velocidad', 'La coordinación', 'Una carrera de más de 40 minutos exige sostener el esfuerzo.'),
        ('abc', '{F} ¿Por qué la prueba C es un trabajo mixto?', 'Porque alterna esfuerzos cortos y pausas durante un tiempo largo', 'Porque dura solo unos segundos, con un esfuerzo máximo único', 'Porque se hace a ritmo estable y sin pausas de ningún tipo', 'Alternar esfuerzos cortos con pausas por mucho tiempo implica ambas formas de energía.'),
        ('abc', 'En Ciencias del ejercicio: ¿qué significa que un esfuerzo sea aeróbico?', 'Que se sostiene sobre todo con aporte de oxígeno', 'Que se hace sin ningún gasto de energía durante la actividad', 'Que dura siempre unos pocos segundos con esfuerzo máximo', 'Aeróbico se refiere al uso de oxígeno en esfuerzos sostenidos.'),
        ('abc', '{F} ¿Qué predomina en la prueba A?', 'La energía anaeróbica, de uso inmediato', 'La energía aeróbica de un ritmo estable', 'La energía que se guarda para la parte final de un esfuerzo largo', 'Los esfuerzos muy cortos y máximos usan sobre todo energía anaeróbica.'),
        ('abc', '{F} ¿Por qué no se dice que en la prueba B se usa «solo» energía aeróbica?', 'Porque las formas de energía funcionan juntas y cambia cuál predomina', 'Porque en la prueba B no se usa energía, solo la fuerza muscular', 'Porque la energía aeróbica no existe en las carreras largas de 40 minutos', 'Hay un predominio, pero ninguna forma de energía actúa sola.'),
        ('=', '{F} Un jugador de ejemplo hace en el partido C 20 repeticiones de 6 segundos de carrera, cada una seguida de 24 segundos de pausa. ¿Cuántos minutos dura esa secuencia?', '20*(6+24)/60', 'Se suman 6 y 24 segundos de cada repetición, se multiplican por 20 y se pasan a minutos.', ' minutos'),
        ('ab', '{F} Una estudiante quiere mejorar para una prueba como la B. ¿Qué diagnóstico inicial es más útil?', 'Cuántos minutos puede sostener un esfuerzo suave sin detenerse', 'Cuántos segundos tarda en una carrera de pocos segundos', 'Para una prueba de resistencia conviene medir cuánto sostiene un esfuerzo continuo.'),
        ('abc', 'Alguien propone para un jugador del partido C solo trote continuo suave. ¿Qué falla?', 'No refleja las carreras cortas, pausas y cambios de ritmo del deporte', 'Nada, porque el trote suave sirve para cualquier deporte con pelota', 'Que el trote suave es demasiado intenso para empezar el entrenamiento', 'El entrenamiento debe parecerse a la demanda del deporte.'),
        ('abc', 'Un compañero dice: «En la prueba A no hace falta ninguna preparación, es muy corta». ¿Qué corresponde?', 'Calentar bien y parar ante dolor, pues el esfuerzo máximo exige preparación', 'Nada: si la prueba es corta, no hay ningún riesgo ni hace falta calentar', 'Hacerla sin calentar para no gastar energía antes del esfuerzo máximo', 'Los esfuerzos máximos requieren calentamiento y atención a las señales de detención.'),
        ('=', '{F} En una sesión de ejemplo para algo parecido a la prueba A, se hacen 8 repeticiones de 5 segundos de carrera fuerte, cada una seguida de 55 segundos de pausa. ¿Cuántos minutos dura esa parte?', '8*(5+55)/60', 'Se suman 5 y 55 segundos de cada repetición, se multiplican por 8 y se pasan a minutos.', ' minutos'),
        ('abc', '{F} Para un sistema pensado para un deporte como el de la prueba C, ¿qué conviene reproducir en la sesión?', 'Esfuerzos cortos con pausas y cambios de ritmo, parecidos a los del deporte', 'Un ritmo estable muy largo sin pausas, como una marcha continua', 'Un solo esfuerzo máximo al final de la sesión, sin cambios de ritmo', 'La especificidad pide que la sesión se parezca a la demanda del deporte.'),
    ],
    ctx=('abc', 'Rodrigo, persona ficticia, practica un deporte con carreras cortas y pausas, y su docente le pide diagnosticar la demanda antes de planificar. ¿Qué diagnóstico es más completo?', 'Duración, esfuerzos cortos, pausas y capacidades, como velocidad y resistencia', 'Solo cuántos goles hizo en el último partido y qué tan bien jugó', 'Solo la edad y la estatura de sus compañeros de equipo', 'Un buen diagnóstico describe duración, intensidad, pausas y capacidades.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué se diagnostica antes de diseñar un sistema?", "La demanda del deporte: duración, intensidad, pausas y capacidades", "El entrenamiento debe parecerse a esa demanda."),
        ("¿Qué energía predomina en un esfuerzo largo y estable?", "La aeróbica, aunque todas funcionan juntas", "Hay un predominio de una energía, no exclusividad."),
        ("¿Qué haces ante dolor o mareo en una prueba?", "Detenerte y avisar a una persona adulta o a un profesional de la salud", "La seguridad va antes que la prueba."),
    ],
    op=("Con estas tres situaciones de ejemplo: (1) una marcha continua de 90 minutos a ritmo estable; (2) una carrera de 10 segundos a esfuerzo máximo; (3) un juego de pelota con carreras de 4 segundos y pausas de 20 segundos durante 50 minutos, escribe un diagnóstico de cada una: duración, intensidad, pausas, capacidad que predomina y energía que predomina. Agrega una medida de seguridad.",
        "(1) 90 minutos, intensidad suave, sin pausas; resistencia; aeróbica. (2) 10 segundos, esfuerzo máximo; velocidad; anaeróbica. (3) 50 minutos, esfuerzos cortos con pausas; velocidad y resistencia; trabajo mixto. Seguridad: calentar y, ante dolor o mareo, parar y avisar a una persona adulta.",
        ["describe duración, intensidad y pausas", "identifica capacidad y energía que predominan", "incluye una medida de seguridad"],
        ["tabla de tres diagnósticos"],
        ["decir que se usa solo una energía", "diagnosticar sin pausas ni duración", "olvidar la seguridad"],
        "Pregunta: «¿qué hace que esa situación sea aeróbica o mixta?». Si responde con una opinión, pídele duración y pausas."),
    reinforce="Elige dos deportes que conozcas y escribe, para cada uno, duración, intensidad, pausas y capacidad que predomina. Solo en papel.",
    extend="Explica por qué el diagnóstico de la demanda del deporte es el primer paso para que un sistema de entrenamiento sea específico.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 21 (cinco sistemas de ejemplo, descritos). Continuo: ritmo estable, sin pausas, durante un tiempo largo. "
     "Interválico: repeticiones de esfuerzo con pausas planificadas entre ellas. Circuito: varias estaciones de ejercicios suaves entre las que se rota, con un tiempo de trabajo y uno de pausa por estación. "
     "Fartlek (juego de velocidad): carrera continua con cambios libres de ritmo, de más suave a más rápido. "
     "Series y repeticiones: un ejercicio se repite varias veces (repeticiones) y ese bloque se hace varias veces con pausa entre ellos (series).")
build(
    O5, 2, F,
    use="Aprenderé a elegir un sistema de entrenamiento según la meta, el tiempo, el espacio y la seguridad, y a distinguir los sistemas continuo, interválico, circuito, fartlek y de series y repeticiones.",
    prior=["Sé diagnosticar la demanda de un deporte.", "Sé aplicar especificidad y progresión.", "Conozco las señales de detención."],
    explain=[
        "Un sistema de entrenamiento organiza el esfuerzo y la pausa. En el sistema continuo se mantiene un ritmo estable sin pausas y sirve para trabajar la resistencia. En el interválico se alterna esfuerzo y pausa planificados y sirve para deportes con cambios de ritmo. El circuito rota por varias estaciones de ejercicios suaves y permite trabajar varias capacidades en poco espacio. El fartlek cambia libremente el ritmo en una carrera continua. En series y repeticiones, un ejercicio se repite varias veces (repeticiones) y el bloque se hace varias veces con pausa (series).",
        "Para elegir se mira la meta (qué capacidad), el tiempo y el espacio disponibles, el nivel de práctica del grupo y la seguridad. Ningún sistema sirve para todo: cada uno tiene ventajas y límites. Se elige el que se parece más a la demanda del deporte y se puede hacer con seguridad. Un sistema exigente exige más recuperación y progresión.",
        "Para personas con distintos niveles se ofrecen variantes: más tiempo de pausa, menos repeticiones o ejercicios más suaves. Si aparecen dolor, mareo o malestar, se detiene la sesión y se avisa a una persona adulta o a un profesional de la salud. Las cifras de este cuaderno son de ejemplo, sin cargas ni saltos.",
    ],
    vocab=[("continuo", "ritmo estable sin pausas durante un tiempo largo"), ("interválico", "repeticiones de esfuerzo con pausas planificadas"), ("circuito", "rotación por estaciones de ejercicios suaves"), ("fartlek", "carrera continua con cambios libres de ritmo"), ("serie y repetición", "repetición de un ejercicio y bloques con pausa")],
    worked=[
        ("Elegir según la meta", "Una persona de ejemplo quiere mejorar su resistencia con esfuerzo suave y parejo durante 25 minutos. ¿Qué sistema conviene?", ["La meta es resistencia con ritmo estable.", "El sistema continuo calza."], "Continuo"),
        ("Elegir según el espacio", "Un grupo de ejemplo tiene un patio pequeño y quiere trabajar varias capacidades con ejercicios suaves. ¿Qué sistema conviene?", ["Necesita poco espacio y variedad.", "El circuito permite rotar por estaciones."], "Circuito"),
    ],
    mistakes=[("Elegir el sistema más exigente porque «entrena más».", "Puede no calzar con la meta, el nivel ni la seguridad.", "Elige según la meta, el tiempo, el espacio y la seguridad."),
              ("Mezclar varios sistemas distintos en una sola sesión sin plan.", "No se sabe qué capacidad se trabajó ni cómo responde el cuerpo.", "Usa un sistema por sesión y cambia una condición a la vez.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué caracteriza al sistema continuo?', 'Un ritmo estable, sin pausas, durante un tiempo largo', 'Esfuerzos cortos con pausas planificadas entre ellos', 'Cambios libres de ritmo sin ninguna regla', 'El sistema continuo mantiene un ritmo estable sin pausas.'),
        ('abc', '{F} ¿Qué sistema alterna esfuerzo y pausas planificadas?', 'El interválico', 'El continuo', 'El fartlek', 'La alternancia de esfuerzo y pausas planificadas define al sistema interválico.'),
        ('abc', '{F} ¿Qué es una serie en el sistema de series y repeticiones?', 'Un bloque de repeticiones que se hace varias veces con pausa entre bloques', 'Una sola repetición de un ejercicio, sin pausa antes de la siguiente', 'Un ejercicio que se hace sin pausa hasta terminar el tiempo total', 'La serie es el bloque de repeticiones; se hacen varias con pausa.'),
        ('abc', '{F} Una persona quiere mejorar su resistencia con un trote de ritmo estable, sin paradas, durante 35 minutos. ¿Qué sistema calza?', 'El continuo', 'El interválico con esfuerzos máximos', 'Series de un solo ejercicio de fuerza', 'Un ritmo estable, sin paradas, durante un tiempo largo es un sistema continuo.'),
        ('abc', '{F} Una profesora tiene una sala chica y 8 estudiantes que deben rotar por ejercicios suaves distintos, con tiempo de trabajo y de pausa en cada uno. ¿Qué sistema se ajusta?', 'El circuito', 'El continuo', 'El fartlek', 'El circuito rota por estaciones suaves y ocupa poco espacio.'),
        ('abc', '{F} ¿Qué diferencia hay entre el fartlek y el interválico?', 'El fartlek cambia libremente el ritmo; el interválico tiene pausas planificadas', 'Son idénticos: los dos tienen pausas planificadas entre repeticiones', 'El fartlek no tiene cambios de ritmo y se hace siempre a ritmo estable', 'El fartlek es continuo con cambios libres; el interválico tiene pausas planificadas.'),
        ('=', '{F} Un circuito de ejemplo tiene 6 estaciones; en cada una se trabaja 30 segundos y se pausa 30 segundos. ¿Cuántos minutos dura una vuelta?', '6*(30+30)/60', 'Se suman 30 y 30 segundos por estación, se multiplican por 6 y se pasan a minutos.', ' minutos'),
        ('=', '{F} Con esa vuelta de 6 minutos, se hacen 3 vueltas con 2 minutos de pausa solo entre una vuelta y otra. ¿Cuántos minutos dura el circuito completo?', '3*6+2*2', 'Se suman los minutos de las 3 vueltas y los de las 2 pausas entre ellas.', ' minutos'),
        ('abc', '{F} Para un deporte con cambios de ritmo, ¿qué sistemas se parecen más a su demanda?', 'El interválico o el fartlek, que alternan ritmos', 'El continuo muy largo, a ritmo constante y sin cambios', 'Series largas de un solo ejercicio, sin cambios de ritmo', 'Alternar ritmos reproduce los cambios del deporte.'),
        ('abc', 'Una estudiante dice: «Si conozco un solo sistema, no necesito otro». ¿Qué corresponde?', 'Elegir según meta, tiempo, espacio y seguridad; ningún sistema sirve para todo', 'Usar siempre el mismo sistema, porque es más simple de organizar', 'Cambiar de sistema todos los días, sin plan y sin registrar nada', 'Cada sistema tiene ventajas y límites; se elige según la situación.'),
        ('abc', 'Un plan usa un sistema interválico con esfuerzo muy alto y pausas casi nulas para alguien que recién empieza. ¿Qué falla?', 'No respeta la progresión ni la recuperación y aumenta el riesgo', 'Nada, porque más duro siempre es mejor para todas las personas', 'Que no usa series, y sin series un sistema no puede ser interválico', 'Sin progresión ni recuperación, el riesgo aumenta.'),
        ('=', '{F} Un ejercicio de ejemplo se hace en 4 series de 10 repeticiones, con 6 segundos por repetición y 60 segundos de pausa entre series (3 pausas). ¿Cuántos segundos dura todo?', '4*10*6+3*60', 'Se suman los segundos de las 40 repeticiones y de las 3 pausas entre series.', ' segundos'),
        ('abc', '{F} Un grupo de niveles distintos quiere un sistema en que cada persona pueda ajustar el tiempo de trabajo y de pausa de su estación. ¿Cuál es más adaptable?', 'El circuito con estaciones suaves y variantes de tiempo', 'El fartlek en una pista larga, con cambios libres de ritmo', 'El continuo de 40 minutos, sin pausas y a ritmo estable', 'El circuito se adapta al espacio y permite variantes por nivel.'),
    ],
    ctx=('abc', 'Daniela, persona ficticia, tiene 25 minutos, un patio pequeño y un grupo de seis personas con distintos niveles que quiere trabajar varias capacidades con esfuerzo suave. ¿Qué sistema y variante son más razonables?', 'Un circuito de estaciones suaves con tiempos de trabajo y pausa ajustables', 'Un fartlek de 25 minutos en una pista larga que el grupo no tiene', 'Un interválico de esfuerzo máximo con pausas mínimas y sin variantes', 'El circuito se adapta al espacio, al tiempo y a los distintos niveles.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué sistema alterna esfuerzo y pausa planificados?", "El interválico", "Las pausas están planificadas dentro del sistema."),
        ("¿Qué se mira para elegir un sistema?", "La meta, el tiempo, el espacio, el nivel y la seguridad", "Ningún sistema sirve para todos los casos."),
        ("¿Qué haces ante dolor o mareo en una sesión?", "Detenerte y avisar a una persona adulta o a un profesional de la salud", "La seguridad va antes que el plan."),
    ],
    op=("Elige un sistema de entrenamiento para cada uno de estos casos de ejemplo y justifica con meta, tiempo, espacio y seguridad. Caso 1: una persona quiere resistencia con esfuerzo suave y 30 minutos disponibles. Caso 2: un grupo de 8 tiene 20 minutos y solo un patio pequeño. Caso 3: una estudiante entrena para un deporte con carreras cortas y pausas.",
        "Caso 1: continuo suave, 30 minutos. Caso 2: circuito con estaciones suaves, variantes de tiempo. Caso 3: interválico con pausas planificadas. En todos: calentar, agua y, ante dolor o mareo, parar y avisar a una persona adulta.",
        ["un sistema distinto justificado para cada caso", "usa meta, tiempo, espacio y seguridad", "menciona una señal de detención"],
        ["tres casos con sistema y justificación"],
        ["elegir siempre el más exigente", "no considerar el espacio ni el nivel", "olvidar la seguridad"],
        "Pregunta: «¿por qué ese sistema calza con el caso?». Si responde que es el más duro, pídele la meta del caso."),
    reinforce="Escribe en papel un ejemplo de cada sistema (continuo, interválico, circuito, fartlek y series) con su duración, sin hacerlo en la práctica si no tienes supervisión.",
    extend="Explica por qué cada sistema tiene ventajas y límites y por qué no se elige solo por ser el más exigente.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 22 (sesión interválica de ejemplo, inventada). Calentamiento: 8 minutos. "
     "Parte principal: 6 repeticiones de 1 minuto de trote más rápido (esfuerzo percibido 6 de 10, cifra de ejemplo), cada una seguida de 2 minutos de caminata suave de recuperación. "
     "Enfriamiento: 5 minutos. Se lleva agua y se detiene ante dolor, mareo o falta de aire inusual.")
build(
    O5, 3, F,
    use="Aprenderé a diseñar y aplicar una sesión interválica con calentamiento, repeticiones, pausas y enfriamiento, a calcular tiempos y a hacerlo con seguridad.",
    prior=["Sé elegir un sistema de entrenamiento.", "Sé describir un programa con FITT.", "Conozco las señales de detención."],
    explain=[
        "Una sesión interválica se diseña con cuatro decisiones: cuántas repeticiones, cuánto dura cada esfuerzo, cuánto dura la pausa y qué intensidad tiene el esfuerzo. La relación trabajo-pausa compara el tiempo de esfuerzo con el de pausa: 1 minuto de esfuerzo con 2 de pausa es una relación de 1 a 2. A más intensidad, más pausa se necesita para repetir el esfuerzo con calidad y seguridad.",
        "La sesión tiene calentamiento (preparar el cuerpo), parte principal (repeticiones con pausas) y enfriamiento (bajar la exigencia). La progresión cambia una sola condición a la vez: más repeticiones, o esfuerzos más largos, o pausas más cortas, nunca todo junto. Cada repetición se anota con el esfuerzo percibido para comprobar que se mantiene dentro de lo planificado.",
        "La seguridad es parte del diseño: se lleva agua, se respeta la pausa y, ante dolor, mareo, falta de aire inusual o malestar, se detiene la sesión y se avisa a una persona adulta o a un profesional de la salud. Las cifras de esfuerzo son de ejemplo; tu docente define la intensidad adecuada para tu grupo.",
    ],
    vocab=[("repetición", "cada esfuerzo de la parte principal"), ("pausa o recuperación", "tiempo entre esfuerzos para recuperarse"), ("relación trabajo-pausa", "comparación entre el tiempo de esfuerzo y el de pausa"), ("intensidad", "qué tan exigente es el esfuerzo"), ("progresión", "cambio gradual de una condición")],
    worked=[
        ("Calcular la parte principal", "Una parte principal de ejemplo tiene 5 repeticiones de 2 minutos de esfuerzo y 3 minutos de pausa. ¿Cuánto dura?", ["Cada repetición con su pausa dura 2 + 3 = 5 minutos.", "5 repeticiones × 5 minutos = 25 minutos."], "25 minutos"),
        ("Aplicar una progresión", "Esa misma parte principal pasa de 5 a 6 repeticiones, igual en lo demás. ¿Cuánto dura ahora?", ["Cambia una sola condición: el número de repeticiones.", "6 × 5 = 30 minutos."], "30 minutos"),
    ],
    mistakes=[("Acortar las pausas y alargar los esfuerzos a la vez para «entrenar más».", "Cambia dos condiciones y reduce la recuperación.", "Cambia una sola condición y respeta la pausa."),
              ("No anotar el esfuerzo percibido de cada repetición.", "No se sabe si la sesión se mantuvo dentro de lo planificado.", "Anota el esfuerzo de cada repetición.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es la relación trabajo-pausa?', 'La comparación entre el tiempo de esfuerzo y el de pausa, por ejemplo 1 a 2', 'El número de personas que trabajan en cada estación del circuito', 'La velocidad máxima alcanzada por la persona durante la sesión', 'La relación compara minutos de esfuerzo con minutos de pausa.'),
        ('abc', '{F} ¿Cuántas repeticiones tiene la parte principal?', '6 repeticiones', '8 repeticiones', '2 repeticiones', 'La ficha indica 6 repeticiones de 1 minuto de esfuerzo.'),
        ('abc', '{F} ¿Cuál es la relación trabajo-pausa de la ficha?', '1 minuto de esfuerzo por 2 de pausa, o sea 1 a 2', '2 minutos de esfuerzo por 1 de pausa, o sea 2 a 1', '1 minuto de esfuerzo por 1 de pausa', 'Cada esfuerzo de 1 minuto va seguido de 2 minutos de pausa.'),
        ('=', '{F} ¿Cuántos minutos dura la parte principal?', '6*(1+2)', 'Cada repetición con su pausa dura 3 minutos y son 6 repeticiones.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos dura la sesión completa?', '8+6*(1+2)+5', 'Se suman calentamiento, parte principal de 18 minutos y enfriamiento.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos de trote más rápido suma la sesión?', '6*1', 'Se multiplican las 6 repeticiones por 1 minuto de esfuerzo.', ' minutos'),
        ('abc', '{F} Para progresar sin subir el riesgo, ¿qué cambio de una sola condición es adecuado?', 'Pasar de 6 a 7 repeticiones y mantener lo demás igual', 'Duplicar las repeticiones y reducir la pausa a la mitad', 'Subir el esfuerzo a 9 de 10 y quitar la pausa', 'Un aumento pequeño en una sola condición es una progresión segura.'),
        ('=', '{F} Con 7 repeticiones y la misma relación trabajo-pausa, ¿cuántos minutos dura la parte principal?', '7*(1+2)', 'Cada repetición con su pausa dura 3 minutos y ahora son 7.', ' minutos'),
        ('ab', '{F} Al terminar una repetición, Camila siente mareo. ¿Qué hace?', 'Detener la sesión, sentarse, tomar agua y avisar a una persona adulta', 'Hacer la siguiente repetición más lenta para no perder la sesión', 'El mareo es una señal de detención y se informa.'),
        ('abc', 'Un compañero propone: «Si quitamos la pausa, la sesión será mejor». ¿Qué falla?', 'La pausa permite recuperarse y repetir el esfuerzo con calidad', 'Nada, porque sin pausa se entrena más y se mejora más rápido', 'Que la pausa debe ser siempre más corta que el tiempo de esfuerzo', 'Sin pausa baja la calidad del esfuerzo y aumenta el riesgo.'),
        ('abc', 'Un diseño dice: «10 repeticiones de 3 minutos muy exigentes con 30 segundos de pausa». ¿Qué problema tiene?', 'La pausa es muy corta para el esfuerzo y sube el riesgo de cansancio', 'La parte principal es demasiado corta para producir algún cambio', 'No incluye repeticiones, así que no se puede considerar interválico', 'Esfuerzos largos y exigentes necesitan pausas suficientes.'),
        ('=', '{F} Si se pasa a una relación 1 a 3 con 6 repeticiones de 1 minuto de esfuerzo, ¿cuántos minutos dura la parte principal?', '6*(1+3)', 'Cada repetición con su pausa dura 4 minutos y son 6.', ' minutos'),
        ('abc', '{F} Una persona anota esfuerzo 9 de 10 en la repetición 6, cuando se esperaba 6. ¿Qué se interpreta?', 'Se pasó del esfuerzo planificado; conviene reducir el ritmo y registrar', 'Que mejoró mucho y debe subir el ritmo en la próxima repetición', 'Que no hace falta registrar nada, porque el esfuerzo no importa', 'Superar el esfuerzo planificado indica reducir y anotar.'),
    ],
    ctx=('abc', 'Matías, persona ficticia, diseña una sesión interválica de 5 repeticiones de 1 minuto de trote y 2 minutos de caminata suave, con calentamiento de 8 minutos y enfriamiento de 5. Siente mucha fatiga en la repetición 4. ¿Qué decisión es más razonable?', 'Terminar con caminata suave, registrar y reducir las repeticiones la próxima vez', 'Hacer la quinta repetición más fuerte para compensar las anteriores', 'Quitar la pausa de la quinta repetición para terminar más rápido', 'Ante fatiga se baja la exigencia y se ajusta una condición.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué cuatro decisiones definen una sesión interválica?", "Repeticiones, duración del esfuerzo, duración de la pausa e intensidad", "Con ellas se calcula y se diseña la sesión."),
        ("¿Cuántas condiciones se cambian a la vez en la progresión?", "Una sola", "Así se entiende la respuesta del cuerpo."),
        ("¿Qué haces ante mareo, dolor o falta de aire inusual?", "Detenerte y avisar a una persona adulta o a un profesional de la salud", "La seguridad va antes que completar la sesión."),
    ],
    op=("Diseña una sesión interválica de ejemplo para una persona ficticia que trota con esfuerzo suave: indica calentamiento, número de repeticiones, duración del esfuerzo y de la pausa, enfriamiento, esfuerzo percibido de ejemplo, relación trabajo-pausa y la duración total. Propón una progresión de una sola condición y dos medidas de seguridad.",
        "Calentamiento 8 minutos; 5 repeticiones de 1 minuto de trote suave y 2 de caminata; enfriamiento 5. Relación 1 a 2. Duración: 8 + 5×3 + 5 = 28 minutos. Progresión: 6 repeticiones. Seguridad: agua y parar ante dolor o mareo, avisando a una persona adulta.",
        ["decisiones completas y duración correcta", "progresión de una sola condición", "dos medidas de seguridad"],
        ["diseño de sesión con cálculo"],
        ["no calcular bien la duración", "subir varias condiciones a la vez", "olvidar las pausas"],
        "Pregunta: «¿qué cambiarás la próxima semana y qué dejarás igual?». Si cambia varias, pídele dejar una."),
    reinforce="Cambia en el diseño de la ficha solo una condición (por ejemplo, la pausa) y calcula la nueva duración. Hazlo en papel.",
    extend="Explica por qué en un sistema interválico la pausa es parte del diseño y no un tiempo perdido.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 23 (registro de ejemplo, inventado). Dato de ejemplo de una persona ficticia: pulso máximo de 190 latidos por minuto (un dato dado para practicar cálculos). "
     "Zonas de ejemplo de este cuaderno: suave, menos de 70 % del máximo; moderada, de 70 % a 80 % del máximo, ambos incluidos; fuerte, más de 80 %. Tu docente define las zonas para tu grupo. "
     "Pulsos medidos en una sesión continua de 20 minutos: minuto 5, 114; minuto 10, 133; minuto 15, 152; minuto 20, 171.")
build(
    O5, 4, F,
    use="Aprenderé a registrar el pulso y el esfuerzo en un sistema de entrenamiento, a calcular porcentajes del máximo de ejemplo y a interpretar zonas para decidir ajustes con seguridad.",
    prior=["Sé tomar el pulso y convertirlo a latidos por minuto.", "Sé calcular porcentajes.", "Conozco las señales de detención."],
    explain=[
        "Registrar un sistema de entrenamiento es anotar los datos de la sesión: el tiempo, el pulso y el esfuerzo percibido. El pulso se puede expresar como porcentaje de un pulso máximo de referencia, dividiendo el pulso medido por el máximo y multiplicando por 100. En este cuaderno el máximo es un dato de ejemplo, no una fórmula para aplicar a tu cuerpo.",
        "Las zonas son rangos de porcentaje que ayudan a decidir cuánta exigencia tiene la sesión. Las zonas de este cuaderno son de ejemplo: tu docente define las del grupo. Si el pulso sale de la zona planificada, se reduce el ritmo y se anota. El pulso también depende del calor, el sueño y el nerviosismo, por lo que se interpreta junto con el esfuerzo percibido.",
        "El registro es propio y no se usa para comparar a las personas. Si aparecen mareo, dolor, falta de aire inusual o malestar, se detiene la sesión, se descansa y se avisa a una persona adulta o a un profesional de la salud, aunque el pulso parezca estar en la zona.",
    ],
    vocab=[("pulso máximo de referencia", "valor dado para calcular porcentajes"), ("porcentaje del máximo", "pulso medido dividido por el máximo, por 100"), ("zona", "rango de porcentaje que orienta la exigencia"), ("esfuerzo percibido", "qué tan duro se siente el ejercicio, de 1 a 10"), ("registro", "anotación ordenada de los datos de la sesión")],
    worked=[
        ("Calcular un porcentaje del máximo", "Un pulso máximo de referencia de ejemplo es 200. ¿Qué porcentaje es un pulso de 140?", ["Divide 140 entre 200: 0,7.", "Multiplica por 100: 70 %."], "70 %"),
        ("Interpretar una zona", "Con ese máximo de 200, un pulso de 170 es 85 %. Con las zonas de la ficha, ¿qué zona es?", ["85 % es más de 80 %.", "Es la zona fuerte: se reduce el ritmo si el plan era suave."], "Fuerte"),
    ],
    mistakes=[("Usar el pulso máximo de ejemplo como si fuera el de mi cuerpo.", "Es un dato dado para practicar; el valor personal lo orienta un profesional.", "Usa el dato de ejemplo solo para el cálculo."),
              ("Ignorar el mareo porque el pulso está en zona suave.", "Los síntomas mandan sobre cualquier número.", "Detén la sesión ante mareo, dolor o falta de aire inusual.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es el pulso máximo de referencia de la ficha?', 'El valor de 190 latidos por minuto que se usa para calcular porcentajes', 'El pulso en reposo de la persona, medido por la mañana al despertar', 'La cantidad de sesiones hechas en la semana respecto de lo planificado', 'Es un dato dado para practicar el cálculo de porcentajes.'),
        ('=', '{F} ¿Qué porcentaje del máximo es el pulso del minuto 5, de 114 latidos por minuto?', '114*100/190', 'Se divide el pulso entre 190 y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Qué porcentaje del máximo es el pulso del minuto 10, de 133 latidos por minuto?', '133*100/190', 'Se divide el pulso entre 190 y se multiplica por 100.', ' %'),
        ('abc', '{F} El pulso del minuto 15 es 152, o sea 80 % del máximo. ¿En qué zona está?', 'Moderada', 'Suave', 'Fuerte', 'La zona moderada incluye de 70 % a 80 %, ambos incluidos.'),
        ('abc', '{F} El pulso del minuto 20 es 171, o sea 90 %. ¿En qué zona está?', 'Fuerte', 'Suave', 'Moderada', 'Más de 80 % es la zona fuerte.'),
        ('abc', '{F} ¿Qué muestra el registro de los 20 minutos?', 'El pulso aumentó en cada medición, de la zona suave a la fuerte', 'El pulso bajó a medida que pasó el tiempo y se pasó a la zona suave', 'El pulso no cambió en toda la sesión y siempre estuvo en zona suave', 'Los pulsos suben de 114 a 171 a lo largo de los 20 minutos.'),
        ('abc', '{F} Si el plan era mantenerse en zona suave a moderada, ¿qué decisión conviene?', 'Reducir el ritmo cuando el pulso entra a la zona fuerte y registrar', 'Aumentar el ritmo para igualar la zona fuerte y no perder el esfuerzo', 'Ignorar el pulso y seguir igual, porque el plan ya está hecho y no cambia', 'El plan pide quedarse en zonas suave y moderada, por eso se baja el ritmo.'),
        ('=', '{F} ¿Cuántos latidos por minuto subió el pulso entre el minuto 5 y el minuto 20?', '171-114', 'Se resta el pulso del minuto 5 al del minuto 20.', ' latidos por minuto'),
        ('=', '{F} Otra medición de la sesión fue 95 latidos por minuto en un descanso. ¿Qué porcentaje del máximo es?', '95*100/190', 'Se divide el pulso entre 190 y se multiplica por 100.', ' %'),
        ('abc', 'Una compañera dice: «El pulso máximo de 190 es el mío y el tuyo debe ser igual». ¿Qué corresponde?', 'Cada persona tiene su propio dato; el de ejemplo solo sirve para calcular', 'Sí, porque todas las personas tienen exactamente el mismo máximo de pulso', 'El máximo se elige según quién gane la sesión de ese día de entrenamiento', 'El máximo de la ficha es un dato de ejemplo, no un valor personal.'),
        ('abc', 'Durante una sesión, una persona siente mareo y falta de aire inusual, aunque su pulso está en zona suave. ¿Qué hace?', 'Detenerse, sentarse y avisar a una persona adulta o a un profesional', 'Aumentar el ritmo para que el pulso suba y se normalice pronto', 'Ignorar el malestar porque el pulso está bien dentro de la zona', 'Los síntomas mandan sobre cualquier número.'),
        ('=', '{F} Si se quiere mantener el pulso por debajo del 70 % del máximo de 190, ¿cuántos latidos por minuto es ese límite?', '190*70/100', 'Se calcula el 70 % de 190.', ' latidos por minuto'),
        ('abc', 'Un registro dice: «mi pulso fue alto», sin números ni tiempos. ¿Qué le falta?', 'Valores y momentos medidos, para calcular el porcentaje y ver la zona', 'Más adjetivos para describirlo mejor, como «muy alto» o «altísimo»', 'El pulso de otra persona para comparar los números entre ambas', 'Sin números y tiempos no se puede interpretar el registro.'),
    ],
    ctx=('abc', 'Tras cuatro mediciones de una sesión continua, Pablo, persona ficticia, anota porcentajes del máximo de ejemplo de 62 %, 68 %, 75 % y 84 %, y esfuerzo percibido 4, 5, 6 y 8. El plan era suave a moderado. ¿Qué decisión es más razonable?', 'Reducir el ritmo al final, porque pasó a zona fuerte y el esfuerzo subió a 8', 'Mantener el ritmo, porque el plan siempre se cumple a pesar del esfuerzo', 'Aumentar el ritmo para que el pulso suba aún más en la última parte', 'El pulso y el esfuerzo salieron de lo planificado, así que se baja el ritmo.'),
    sc=[
        ("En Ciencias del ejercicio: ¿cómo se calcula el porcentaje del máximo?", "Pulso medido dividido por el máximo, por 100", "Así se compara con las zonas."),
        ("¿Qué manda más: un síntoma como el mareo o el número del pulso?", "El síntoma: se detiene la sesión y se avisa", "La seguridad va antes que cualquier dato."),
        ("¿Con quién se comparan tus registros?", "Contigo en otras sesiones", "Cada persona parte de un punto distinto."),
    ],
    op=("Con este registro de ejemplo de una persona ficticia, de pulso máximo de referencia de 180 latidos por minuto: minuto 4, 108; minuto 8, 126; minuto 12, 135; minuto 16, 153. Usa las zonas de la ficha. Calcula el porcentaje de cada medición, indica la zona, decide qué ajuste harías si el plan era suave a moderado y escribe una medida de seguridad.",
        "Porcentajes: 60 %, 70 %, 75 % y 85 %. Zonas: suave, moderada, moderada y fuerte. Ajuste: reducir el ritmo en la parte final y registrar. Seguridad: si aparecen mareo, dolor o falta de aire inusual, detener la sesión y avisar a una persona adulta.",
        ["calcula los cuatro porcentajes", "identifica las zonas", "decide un ajuste y menciona la seguridad"],
        ["tabla con porcentajes, zonas, ajuste y seguridad"],
        ["no usar la zona para decidir", "usar el máximo de ejemplo como dato personal", "ignorar los síntomas"],
        "Pregunta: «¿qué haces si el número está bien pero te sientes mareada?». Si responde seguir, vuelve a las señales de detención."),
    reinforce="Con un máximo inventado, calcula porcentajes de cuatro pulsos de ejemplo y ubícalos en las zonas. No uses este cuaderno para decidir tu intensidad personal.",
    extend="Explica por qué los síntomas pesan más que el número del pulso al decidir si continuar una sesión.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 24 (registro de cuatro semanas de ejemplo, inventado). Sistema: interválico, con 1 minuto de esfuerzo y 2 minutos de pausa por repetición. "
     "Semana 1: 6 repeticiones, esfuerzo percibido promedio 5. Semana 2: 7 repeticiones, esfuerzo 6. Semana 3: 8 repeticiones, esfuerzo 8 y cansancio anotado como «mucho». "
     "Semana 4, de menor carga: 5 repeticiones, misma pausa. Prueba de 1 kilómetro, en segundos: inicial 500; tras la semana 3, 495; tras la semana 4, 475.")
build(
    O5, 5, F,
    use="Aprenderé a evaluar un sistema de entrenamiento con carga, esfuerzo y resultado, y a ajustarlo con una semana de menor carga o un cambio de una sola condición, cuidando la recuperación.",
    prior=["Sé diseñar una sesión interválica.", "Sé registrar pulso y esfuerzo.", "Sé que el descanso es parte del entrenamiento."],
    explain=[
        "Evaluar un sistema es mirar juntos tres tipos de datos: la carga (cuánto trabajo, por ejemplo el número de repeticiones), el esfuerzo percibido y el resultado en una prueba repetida. Si la carga sube, el esfuerzo sube mucho y el resultado casi no mejora, es una señal de que conviene recuperar o reducir la carga, no de aumentar más.",
        "Una semana de menor carga es una semana planificada con menos trabajo para favorecer la recuperación. En un ciclo de ejemplo se aumenta la carga durante tres semanas y la cuarta se reduce. Después de una semana de menor carga el cuerpo puede responder mejor, pero otros factores también pueden influir. Se ajusta una sola condición, se registra y se vuelve a evaluar.",
        "Los datos son propios y no se comparan con los de otras personas. Si aparecen dolor, mareo, cansancio que no se va o malestar, se reduce la carga o se detiene la práctica y se avisa a una persona adulta o a un profesional de la salud. Las cifras del cuaderno son de ejemplo y no son una prescripción personal.",
    ],
    vocab=[("carga", "cantidad y exigencia del trabajo"), ("semana de menor carga", "semana planificada con menos trabajo para recuperarse"), ("ciclo", "conjunto de semanas con un patrón de carga"), ("indicador", "dato medible que muestra el avance"), ("ajuste", "cambio de una condición según los datos")],
    worked=[
        ("Leer un registro", "Un registro de ejemplo: semana 1, 5 repeticiones y esfuerzo 4; semana 2, 6 repeticiones y esfuerzo 5; semana 3, 7 repeticiones y esfuerzo 8 con cansancio. ¿Qué indica?", ["Entre las semanas 2 y 3 el esfuerzo subió bastante con solo una repetición más.", "Es una señal de reducir la carga."], "Conviene reducir la carga"),
        ("Decidir un ajuste", "Con esa señal, ¿qué ajuste de una sola condición conviene para la semana 4?", ["Reducir las repeticiones y mantener la misma pausa.", "Registrar el esfuerzo y el cansancio de nuevo."], "Reducir las repeticiones y registrar"),
    ],
    mistakes=[("Responder al cansancio aumentando la carga.", "Empeora la recuperación y el riesgo.", "Reduce la carga o planifica una semana de menor carga."),
              ("Atribuir una mejora solo al último cambio.", "Pudieron influir las semanas anteriores y la recuperación.", "Interpreta la mejora con cuidado y mira el conjunto.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es una semana de menor carga?', 'Una semana planificada con menos trabajo para favorecer la recuperación', 'Una semana sin ningún plan, en la que cada persona decide qué hacer', 'Una semana en la que se entrena el doble para compensar la anterior', 'Una semana de menor carga se planifica para recuperarse.'),
        ('=', '{F} ¿Cuántas repeticiones suman las semanas 1 a 3?', '6+7+8', 'Se suman las repeticiones de las tres primeras semanas.', ' repeticiones'),
        ('abc', '{F} ¿En qué semana fue más alto el esfuerzo percibido?', 'En la semana 3', 'En la semana 1', 'En la semana 2', 'El esfuerzo fue 8 en la semana 3, el más alto del registro.'),
        ('=', '{F} ¿Cuántos segundos mejoró el tiempo de la prueba entre la inicial y la de después de la semana 4?', '500-475', 'Se resta el tiempo de la prueba final al inicial.', ' segundos'),
        ('abc', '{F} ¿Qué indica el cansancio «mucho» con esfuerzo 8 en la semana 3?', 'Que la carga fue alta y conviene una semana de menor carga', 'Que debe subir aún más la carga para superar el cansancio', 'Que la prueba no sirve para nada y debe eliminarse del plan', 'Cansancio y esfuerzo altos indican reducir la carga.'),
        ('abc', '{F} ¿Qué cambio de una sola condición se hizo en la semana 4?', 'Redujo las repeticiones a 5 y mantuvo la misma pausa', 'Cambió el sistema interválico por un circuito de estaciones suaves', 'Quitó las pausas y mantuvo las ocho repeticiones de la semana 3', 'La ficha reduce las repeticiones y mantiene la pausa.'),
        ('abc', '{F} ¿Qué se puede decir con cuidado del resultado de la prueba tras la semana 4?', 'Mejoró tras la semana de menor carga, y pudo influir la recuperación', 'Mejoró solo porque la pausa entre repeticiones se hizo más larga', 'Prueba que el sistema funciona igual de bien en todas las personas', 'Se interpreta con cuidado, porque influyen varios factores.'),
        ('=', '{F} ¿Qué porcentaje del tiempo inicial bajó el tiempo tras la semana 4?', '(500-475)*100/500', 'Se calcula la baja de 25 segundos y se divide entre los 500 iniciales.', ' %'),
        ('ab', '{F} Para la semana 5, ¿qué decisión es razonable?', 'Volver a aumentar poco a poco, por ejemplo a 6 repeticiones, y registrar', 'Pasar a 12 repeticiones de golpe para recuperar el tiempo perdido', 'Subir poco a poco permite comprobar cómo responde el cuerpo.'),
        ('abc', 'Un compañero dice: «Descansar una semana es retroceder». ¿Qué corresponde?', 'Una semana de menor carga bien planificada ayuda a recuperarse', 'Nada: descansar siempre retrocede, porque el cuerpo olvida lo logrado', 'Que el descanso no se planifica: se toma solo cuando ya no se puede más', 'La recuperación planificada es parte del entrenamiento.'),
        ('abc', 'Alguien concluye: «Mejoré en la semana 4, así que la semana 3 fue demasiado fácil». ¿Qué falla?', 'Ignora el esfuerzo 8 y el cansancio de la semana 3', 'Nada: la semana 3 fue fácil y por eso mejoró el resultado', 'Que no debía medir la prueba después de la semana de menor carga', 'La semana 3 fue exigente, según el esfuerzo y el cansancio.'),
        ('=', '{F} La sesión de la semana 4 tiene 8 minutos de calentamiento, la parte principal con 5 repeticiones y 5 minutos de enfriamiento. ¿Cuántos minutos dura?', '8+5*(1+2)+5', 'Se suman calentamiento, parte principal de 15 minutos y enfriamiento.', ' minutos'),
        ('abc', '{F} Una persona repite el plan del registro y siente cansancio otra vez en la semana 3. ¿Qué ajuste de una condición conviene?', 'Reducir las repeticiones de esa semana o adelantar la de menor carga', 'Aumentar las repeticiones y quitar las pausas para ganar tiempo', 'Dejar de registrar los datos para no preocuparse por el cansancio', 'Reducir la carga ante el cansancio es el ajuste adecuado.'),
    ],
    ctx=('abc', 'Isidora, persona ficticia, hizo tres semanas con más repeticiones; en la tercera el esfuerzo subió a 8, durmió mal y su tiempo en la prueba no mejoró. ¿Qué decisión es más razonable?', 'Planificar una semana de menor carga, cuidar el sueño y volver a medir', 'Aumentar las repeticiones cada semana hasta que el tiempo mejore', 'Quitar las pausas para ahorrar tiempo y poder exigirse mucho más', 'Con esfuerzo alto, mal sueño y sin mejora, se recupera antes de seguir.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué tres datos se evalúan en un sistema?", "Carga, esfuerzo percibido y resultado de la prueba", "Juntos muestran cómo responde la persona."),
        ("¿Qué se hace si el esfuerzo sube mucho y aparece cansancio?", "Reducir la carga o planificar una semana de menor carga", "Aumentar la carga empeora la recuperación."),
        ("¿Con quién se comparan los resultados?", "Con los propios de otras semanas", "Cada persona parte de un punto distinto."),
    ],
    op=("Con este registro de ejemplo de una persona ficticia: semana 1, 6 repeticiones, esfuerzo 5; semana 2, 7 repeticiones, esfuerzo 6; semana 3, 8 repeticiones, esfuerzo 8 y cansancio; prueba de 1 kilómetro, 450 segundos inicial y 446 tras la semana 3. Evalúa carga, esfuerzo y resultado, decide un ajuste de una sola condición para la semana 4 y escribe una señal que te haría detener y avisar.",
        "La carga subió de 6 a 8, el esfuerzo de 5 a 8 y el resultado mejoró solo 4 segundos: conviene reducir. Ajuste: semana de menor carga con 5 repeticiones y misma pausa, y registrar. Señal: dolor o mareo; detengo la sesión y aviso a una persona adulta.",
        ["lee carga, esfuerzo y resultado", "decide un ajuste de una condición", "incluye una señal de detención"],
        ["evaluación escrita con ajuste y seguridad"],
        ["aumentar la carga ante el cansancio", "cambiar varias condiciones a la vez", "no mirar el esfuerzo"],
        "Pregunta: «¿qué pasó con el esfuerzo cuando subió la carga?». Si no mira el registro, pídele que lo relea."),
    reinforce="Con datos inventados de tres semanas, escribe una evaluación de carga, esfuerzo y resultado y un ajuste de una sola condición.",
    extend="Explica por qué una semana de menor carga puede ser parte de un plan y no un retroceso.",
)

# ============================================================ OAC-06, clase 1
F = ("Ficha 25 (factores de ejemplo en un caso inventado). Camila, persona ficticia, corre 100 metros en el club escolar y su tiempo cambia de una semana a otra. Datos anotados: "
     "a) durmió poco la noche anterior; b) su técnica de salida es inestable; c) se siente nerviosa antes de competir y duda de sí misma; d) cerca de su casa hay una pista y su familia la apoya para ir; "
     "e) el calor del día fue fuerte; f) usó zapatillas gastadas con poco agarre en el piso mojado; g) se siente motivada porque disfruta correr; "
     "h) personas de su entorno dicen en tono de burla que una mujer no debería practicar atletismo.")
build(
    O6, 1, F,
    use="Aprenderé a diagnosticar los factores fisiológicos, biomecánicos, psicológicos y sociológicos que pueden influir en el rendimiento de un caso, clasificándolos con criterios y sin juzgar a las personas.",
    prior=["Sé que el rendimiento es un resultado medible.", "Sé que cada persona se compara consigo misma.", "Conozco las señales de detención."],
    explain=[
        "Los factores que influyen en el rendimiento se agrupan en cuatro tipos. Los fisiológicos tienen que ver con el funcionamiento del cuerpo: energía, fatiga, sueño, hidratación y temperatura. Los biomecánicos tienen que ver con cómo se mueve el cuerpo: técnica, fuerzas, postura, equilibrio y equipo. Los psicológicos tienen que ver con la mente: motivación, nerviosismo, concentración y confianza. Los sociológicos tienen que ver con el entorno social: apoyo de familia y amistades, acceso a lugares, ideas y estereotipos de la comunidad.",
        "Un estereotipo es una idea fija y simplificada sobre un grupo de personas, como creer que una actividad es solo de hombres o de mujeres. No tiene respaldo y puede impedir que alguien practique lo que le interesa. Analizar un caso es separar los datos por tipo de factor, ver cómo se relacionan entre sí y no atribuir todo a un único factor ni a la voluntad de la persona.",
        "El análisis es privado y no evalúa cuerpos. Si alguien siente un malestar fuerte o persistente por nervios, presión o burlas, conviene hablarlo con una persona adulta de confianza o con un profesional. Ante dolor, mareo o lesión en la práctica, se detiene la actividad y se avisa a una persona adulta.",
    ],
    vocab=[("factor fisiológico", "tiene que ver con el funcionamiento del cuerpo"), ("factor biomecánico", "tiene que ver con cómo se mueve el cuerpo y el equipo"), ("factor psicológico", "tiene que ver con la mente y las emociones"), ("factor sociológico", "tiene que ver con el entorno social"), ("estereotipo", "idea fija y simplificada sobre un grupo de personas")],
    worked=[
        ("Clasificar un dato", "Un dato de ejemplo dice: «le faltó concentración antes de la partida». ¿Qué tipo de factor es?", ["Se refiere a la mente y la atención.", "Es un factor psicológico."], "Psicológico"),
        ("Revisar la relación entre factores", "Un caso de ejemplo duerme poco y además siente más nervios antes de competir. ¿Cómo se relacionan?", ["El sueño es fisiológico y los nervios, psicológicos.", "Pueden influirse entre sí: no se explican por un solo factor."], "Se relacionan; no hay un único factor"),
    ],
    mistakes=[("Atribuir un mal resultado a un solo factor, como «no se esfuerza».", "Hay factores de varios tipos que influyen y que se pueden revisar.", "Clasifica los datos y revisa los cuatro tipos."),
              ("Aceptar un estereotipo como si fuera un dato.", "No tiene respaldo y limita la participación.", "Pide hablar de datos y condiciones, y trata con respeto a las personas.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué estudian los factores biomecánicos?', 'Cómo las fuerzas, la técnica y el equipo influyen en el movimiento', 'Cómo las emociones y los pensamientos influyen en el rendimiento', 'Cómo la familia y el entorno influyen en la práctica deportiva', 'Lo biomecánico se refiere al movimiento, la técnica y el equipo.'),
        ('abc', '{F} ¿Qué tipo de factor es el dato a, dormir poco la noche anterior?', 'Fisiológico', 'Sociológico', 'Biomecánico', 'El sueño afecta el funcionamiento del cuerpo.'),
        ('abc', '{F} ¿Qué tipo de factor es el dato b, la técnica de salida inestable?', 'Biomecánico', 'Psicológico', 'Sociológico', 'La técnica se refiere a cómo se mueve el cuerpo.'),
        ('abc', '{F} ¿Qué tipo de factor es el dato c, el nerviosismo y la duda de sí misma?', 'Psicológico', 'Fisiológico', 'Biomecánico', 'Los nervios y la confianza son aspectos de la mente.'),
        ('abc', '{F} ¿Qué tipo de factor es el dato d, la pista cercana y el apoyo de la familia?', 'Sociológico', 'Fisiológico', 'Psicológico', 'El acceso a lugares y el apoyo son factores del entorno social.'),
        ('abc', '{F} ¿Cuál de estos datos es un factor psicológico a favor?', 'El dato g: disfruta correr y se siente motivada', 'El dato a: durmió poco la noche anterior a la carrera', 'El dato e: el calor del día fue fuerte durante la carrera', 'Disfrutar y estar motivada es un factor psicológico favorable.'),
        ('abc', '{F} ¿Cuál dato muestra un estereotipo que es un factor sociológico a revisar con respeto?', 'El dato h: dicen que una mujer no debería practicar atletismo', 'El dato f: las zapatillas gastadas con poco agarre en el piso', 'El dato e: el calor fuerte del día en que corrió la carrera', 'El dato h es una idea fija sin respaldo sobre quién puede practicar.'),
        ('=', '{F} Si el dato e se clasifica como fisiológico y el f como biomecánico, quedan 2 datos de cada tipo entre los 8. ¿Qué porcentaje de los datos es de tipo psicológico?', '2*100/8', 'Se divide los 2 datos psicológicos entre el total de 8 y se pasa a porcentaje.', ' %'),
        ('ab', '{F} ¿Qué decisión de análisis es más completa?', 'Revisar los datos de los cuatro tipos antes de explicar el cambio del tiempo', 'Explicar todo con el dato psicológico, porque la mente decide siempre', 'Un análisis completo revisa los cuatro tipos de factores y no uno solo.'),
        ('abc', 'Alguien dice: «Camila corrió peor solo porque no se esfuerza». ¿Qué falla?', 'Atribuye todo a un factor y no revisa otros, como el sueño o la técnica', 'Nada, porque el esfuerzo es el único factor que explica el rendimiento', 'Que los factores de un caso no se pueden revisar con los datos anotados', 'Hay varios factores de distinto tipo que pueden influir.'),
        ('abc', 'Un comentario dice: «Las mujeres no son buenas para correr». ¿Qué corresponde?', 'Reconocerlo como un estereotipo sin respaldo y pedir hablar con datos', 'Aceptarlo, porque es la opinión del grupo y hay que respetarla', 'Responder con burlas a quien lo dijo, para que no lo repita', 'Un estereotipo no es un dato, y se responde con respeto.'),
        ('abc', '{F} Para mejorar sin sobrecargar, ¿qué ajuste de un factor es razonable primero?', 'Cuidar el sueño y el descanso antes de competir y registrar el efecto', 'Cambiar a la vez el sueño, la técnica, las zapatillas y el entrenamiento', 'Dejar de correr hasta que las burlas del entorno hayan terminado', 'Un ajuste simple y registrado permite evaluar su efecto.'),
        ('abc', '{F} Camila siente que los nervios le afectan mucho y no se le pasan. ¿Qué corresponde?', 'Conversarlo con una persona adulta de confianza o con un profesional', 'Ocultarlo, porque los nervios son una debilidad que no debe mostrarse', 'Competir más veces para acostumbrarse, sin hablar con nadie del tema', 'Un malestar persistente se conversa con una persona adulta o un profesional.'),
    ],
    ctx=('abc', 'Tomás, persona ficticia, anota: durmió bien, tiene buena técnica, siente mucha presión de su grupo de amistades por «ganar siempre» y su tiempo empeoró. ¿Qué tipo de factor parece destacar en el caso y qué conviene?', 'Psicológico y sociológico, la presión; se conversa con una persona adulta', 'Fisiológico, la falta de sueño, porque es lo que más afecta el tiempo', 'Biomecánico, la técnica, porque siempre explica un cambio en el tiempo', 'Los datos de sueño y técnica son favorables; destaca la presión, que se conversa y se ajusta.'),
    sc=[
        ("En Ciencias del ejercicio: ¿cuáles son los cuatro tipos de factores del rendimiento?", "Fisiológicos, biomecánicos, psicológicos y sociológicos", "Cada tipo mira un aspecto distinto."),
        ("En Ciencias del ejercicio físico y deportivo: ¿Qué es un estereotipo?", "Una idea fija y simplificada sobre un grupo de personas", "No es un dato y puede limitar la participación."),
        ("¿Qué haces si un nerviosismo o malestar es fuerte y persistente?", "Hablarlo con una persona adulta de confianza o con un profesional", "Un malestar intenso no se enfrenta en soledad."),
    ],
    op=("Con este caso de ejemplo: una estudiante ficticia lanza una pelota blanda a un blanco y su puntaje baja de 8 a 5 aciertos de 10. Anota: durmió mal, su brazo se mueve tenso, se siente observada y nerviosa, y su grupo comenta que «eso no es para ella». Clasifica cada dato en uno de los cuatro tipos de factor, explica cómo se podrían relacionar y propone un ajuste de un solo factor.",
        "Dormir mal: fisiológico. Brazo tenso: biomecánico. Nervios al sentirse observada: psicológico. Comentario del grupo: sociológico, un estereotipo. Se pueden relacionar: dormir mal y los nervios pueden aumentar la tensión. Ajuste: cuidar el sueño y registrar. Si el nerviosismo es fuerte, conversar con una persona adulta.",
        ["clasifica los cuatro datos con razón", "explica una relación entre factores", "propone un ajuste de un solo factor"],
        ["clasificación, relación y ajuste"],
        ["atribuir todo a un solo factor", "aceptar el estereotipo", "cambiar varias cosas a la vez"],
        "Pregunta: «¿qué tipo de factor es y por qué?». Si dice «es mala suerte», pídele que revise los datos."),
    reinforce="Anota en papel cuatro factores que podrían influir en una actividad que practicas, uno de cada tipo, y una forma de revisarlos. No compares con otras personas.",
    extend="Explica por qué analizar un caso con los cuatro tipos de factores evita culpar a la persona de un mal resultado.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 26 (datos de ejemplo, inventados). Velocidad al correr = longitud de zancada por pasos por segundo. "
     "Corredor A (persona ficticia): zancada de 1 metro y 3 pasos por segundo. Corredor B: zancada de 1 metro y 4 pasos por segundo. Corredor C: zancada de 2 metros y 2 pasos por segundo. "
     "En un salto de ejemplo se observan: (1) balanceo de los brazos hacia adelante al despegar; (2) caída con las rodillas flexionadas; (3) base de apoyo amplia al recibir un balón en un deporte de pelota.")
build(
    O6, 2, F,
    use="Aprenderé a analizar factores fisiológicos y biomecánicos del rendimiento con datos y observaciones: fatiga, hidratación, técnica, equilibrio y velocidad, sin evaluar cuerpos.",
    prior=["Sé clasificar factores en cuatro tipos.", "Sé calcular productos sencillos.", "Conozco las señales de detención."],
    explain=[
        "La biomecánica estudia cómo las fuerzas y la técnica influyen en el movimiento. En la carrera, la velocidad depende de dos cosas: la longitud de la zancada y los pasos por segundo (velocidad = longitud de zancada × pasos por segundo). Una misma velocidad puede lograrse con combinaciones distintas. Para el equilibrio, una base de apoyo amplia y un cuerpo más bajo dan más estabilidad. Al caer de un salto, flexionar las rodillas ayuda a amortiguar el impacto.",
        "Los factores fisiológicos se relacionan con el funcionamiento del cuerpo. La fatiga acumulada y la energía disponible pueden reducir el ritmo en esfuerzos largos. Al sudar se pierde líquido: si no se repone durante una actividad larga o con calor, el rendimiento puede bajar, y por eso se bebe agua. El sueño y la recuperación también influyen.",
        "Los datos de este cuaderno son de ejemplo y no se usan para comparar ni juzgar cuerpos. La mejora de la técnica se practica con supervisión y de forma gradual. Ante dolor, mareo o malestar, se detiene la actividad y se avisa a una persona adulta o a un profesional de la salud.",
    ],
    vocab=[("zancada", "distancia entre un paso y el siguiente al correr"), ("paso por segundo", "cantidad de pasos que se dan en un segundo"), ("base de apoyo", "superficie sobre la que se apoya el cuerpo"), ("amortiguar", "disminuir un impacto"), ("fatiga", "pérdida de capacidad de seguir con el mismo esfuerzo")],
    worked=[
        ("Calcular una velocidad", "Un corredor de ejemplo tiene zancada de 1 metro y 2 pasos por segundo. ¿Qué velocidad lleva?", ["Aplica velocidad = zancada × pasos por segundo.", "1 × 2 = 2 metros por segundo."], "2 metros por segundo"),
        ("Relacionar técnica y estabilidad", "Una persona de ejemplo recibe un balón con los pies juntos y casi pierde el equilibrio. ¿Qué ajuste biomecánico propones?", ["Una base de apoyo más amplia da más estabilidad.", "También ayuda flexionar un poco las rodillas."], "Ampliar la base de apoyo y flexionar un poco las rodillas"),
    ],
    mistakes=[("Pensar que solo se corre más rápido moviendo las piernas más rápido.", "La velocidad depende también de la longitud de la zancada.", "Considera zancada y pasos por segundo."),
              ("Creer que la técnica no importa si hay fuerza.", "Una mala técnica puede reducir la eficacia y aumentar el riesgo.", "Practica la técnica de forma gradual y con supervisión.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué indica una base de apoyo amplia?', 'Mayor estabilidad, porque el cuerpo se apoya en una superficie más ancha', 'Menor equilibrio, porque el cuerpo está más abierto y se mueve más', 'Más velocidad siempre, porque el cuerpo ocupa más espacio', 'Una base amplia aumenta la estabilidad del cuerpo.'),
        ('=', '{F} ¿Cuántos metros por segundo corre el corredor A?', '1*3', 'Se multiplica la longitud de zancada por los pasos por segundo.', ' metros por segundo'),
        ('=', '{F} ¿Cuántos metros por segundo corre el corredor B?', '1*4', 'Se multiplica la longitud de zancada por los pasos por segundo.', ' metros por segundo'),
        ('abc', '{F} ¿Qué corredores tienen la misma velocidad?', 'B y C, con 4 metros por segundo', 'A y B, con 3 metros por segundo', 'A y C, con 4 metros por segundo', 'B lleva 1 × 4 y C lleva 2 × 2, ambos 4 metros por segundo.'),
        ('abc', '{F} ¿Qué muestra la comparación entre A y B?', 'Con la misma zancada, más pasos por segundo dan más velocidad', 'Con la misma zancada, menos pasos por segundo dan más velocidad', 'Que la zancada no influye en la velocidad', 'B tiene la misma zancada que A y más pasos por segundo, y es más rápido.'),
        ('abc', '{F} ¿Para qué sirve caer con las rodillas flexionadas (observación 2)?', 'Para amortiguar el impacto y cuidar las articulaciones', 'Para hacer el salto siempre más alto que con las piernas rígidas', 'Para dejar de sentir fatiga durante el resto de la sesión', 'Flexionar las rodillas disminuye la fuerza del impacto.'),
        ('=', '{F} El corredor A mantiene su zancada de 1 metro y sube a 5 pasos por segundo en un esfuerzo corto de ejemplo. ¿Qué velocidad alcanza?', '1*5', 'Se multiplica la zancada por los nuevos pasos por segundo.', ' metros por segundo'),
        ('abc', '{F} Un corredor aumenta su zancada de 1 a 2 metros y mantiene 3 pasos por segundo. ¿Qué pasa con la velocidad, según la fórmula de la ficha?', 'Sube de 3 a 6 metros por segundo', 'Baja de 3 a 2 metros por segundo', 'No cambia', 'La fórmula multiplica zancada y pasos: 2 × 3 es 6.'),
        ('ab', 'Un corredor sudó mucho en un día de calor y no repuso líquido durante una actividad larga. ¿Qué puede ocurrir?', 'Su rendimiento puede bajar, por eso conviene hidratarse', 'Su rendimiento siempre sube, porque el cuerpo se adapta al calor', 'Perder líquido sin reponerlo puede disminuir el rendimiento.'),
        ('abc', 'Una estudiante dice: «Para ser más rápida basta mover las piernas más rápido sin cuidar la técnica». ¿Qué falla?', 'La velocidad depende de zancada y pasos, y una mala técnica aumenta el riesgo', 'Nada, porque la técnica no importa si se mueven rápido las piernas', 'Que la velocidad no se puede medir con una fórmula de ese tipo', 'La técnica influye en la eficacia y en la seguridad.'),
        ('abc', 'Dos corredores de ejemplo tienen igual velocidad: uno con zancada larga y pocos pasos y otro con zancada corta y muchos pasos. ¿Qué se concluye?', 'Una misma velocidad se logra con combinaciones distintas de zancada y pasos', 'Uno de los dos corredores se equivoca al contar sus pasos por segundo', 'Solo la zancada larga es correcta, porque da más velocidad que la corta', 'La fórmula admite combinaciones distintas con el mismo producto.'),
        ('=', 'Un corredor de ejemplo con zancada de 2 metros y 3 pasos por segundo corre 10 segundos a esa velocidad constante. ¿Cuántos metros recorre?', '2*3*10', 'Se calcula la velocidad de 6 metros por segundo y se multiplica por 10 segundos.', ' metros'),
        ('abc', 'En los últimos minutos de una carrera larga, un corredor reduce sus pasos por segundo. ¿Qué factor fisiológico puede explicarlo?', 'La fatiga acumulada y la energía disponible', 'El tipo de calzado que usa en la pista', 'El apoyo de las amistades que lo esperan en la meta', 'La fatiga y la energía son factores fisiológicos que reducen el ritmo.'),
    ],
    ctx=('abc', 'Marta, persona ficticia, recibe un balón con los pies juntos y los brazos rígidos, y se desequilibra. Además corrió con calor sin tomar agua y se sintió muy cansada. ¿Qué análisis y ajuste son coherentes?', 'Biomecánico, la base estrecha, y fisiológico, el agua; se ajustan ambos', 'Solo psicológico: debe esforzarse más y no pensar en la base de apoyo', 'Ningún factor influye: fue mala suerte y se resuelve repitiendo la prueba', 'La base estrecha es biomecánica y la falta de agua es fisiológica, y cada una tiene un ajuste.'),
    sc=[
        ("En Ciencias del ejercicio: ¿de qué dos cosas depende la velocidad al correr?", "De la longitud de la zancada y de los pasos por segundo", "La velocidad es el producto de ambas."),
        ("¿Qué ayuda a ganar estabilidad?", "Una base de apoyo amplia y flexionar un poco las rodillas", "Aumenta el equilibrio y la estabilidad del cuerpo."),
        ("¿Qué se hace si aparece dolor o mareo en la práctica?", "Detener la actividad y avisar a una persona adulta o a un profesional de la salud", "La seguridad va antes que la técnica."),
    ],
    op=("Con estos datos de ejemplo de dos personas ficticias: Persona 1 corre con zancada de 2 metros y 3 pasos por segundo; Persona 2, con zancada de 1 metro y 5 pasos por segundo. Calcula la velocidad de cada una, explica qué muestra la comparación y menciona un factor fisiológico que podría bajar su ritmo en una carrera larga y cómo cuidarlo.",
        "Persona 1: 6 metros por segundo. Persona 2: 5 metros por segundo. Muestran que la velocidad depende de zancada y pasos: la zancada larga compensa menos pasos. Factor fisiológico: la fatiga y la pérdida de líquido; se cuida con agua y descanso. Si hay dolor o mareo, paro y aviso.",
        ["calcula las dos velocidades", "explica la comparación con la fórmula", "menciona un factor fisiológico y su cuidado"],
        ["cálculos y explicación escrita"],
        ["usar solo la zancada o solo los pasos", "ignorar la hidratación y la fatiga", "juzgar cuerpos"],
        "Pregunta: «¿qué dos datos usas para la velocidad?». Si dice uno, pídele el otro."),
    reinforce="Con una zancada y una cantidad de pasos por segundo de ejemplo, calcula una velocidad y anota qué cambiarías para aumentarla en un solo factor. Solo en papel.",
    extend="Explica por qué la técnica y la hidratación pueden influir juntas en el rendimiento de una misma carrera.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 27 (caso de ejemplo, inventado). Fabián, estudiante ficticio, anota antes de una competencia escolar su nerviosismo de 1 (calmado) a 10 (muy nervioso): la noche anterior, 7; una hora antes, 8; "
     "tras 3 minutos de respiración lenta y repetir una frase de ánimo, 5. También anota su concentración de 1 a 10: 4 al empezar el calentamiento y 7 después de fijarse una meta concreta para esa carrera, «mantener el ritmo los primeros 200 metros». "
     "Su motivación viene de que disfruta correr con su equipo.")
build(
    O6, 3, F,
    use="Aprenderé a analizar factores psicológicos del rendimiento, como la motivación, el nerviosismo, la concentración y la confianza, y a conocer estrategias sencillas y seguras, sabiendo cuándo pedir ayuda a una persona adulta o a un profesional.",
    prior=["Sé clasificar factores en cuatro tipos.", "Sé registrar datos en escalas de 1 a 10.", "Sé avisar a una persona adulta ante un malestar."],
    explain=[
        "La motivación es lo que nos impulsa a practicar. Es intrínseca cuando viene del disfrute de la actividad misma, y extrínseca cuando viene de algo externo, como un premio o el reconocimiento de otras personas. La motivación intrínseca suele sostener más la práctica en el tiempo. El nerviosismo (activación) antes de competir es común: un nivel moderado ayuda a estar atento, pero un nivel muy alto puede perjudicar.",
        "La concentración es dirigir la atención a lo que importa en la tarea. Se ayuda con metas concretas que dependen de la propia persona (por ejemplo, «mantener el ritmo los primeros 200 metros») y no de ganarle a otras. Estrategias sencillas y seguras son la respiración lenta, frases de ánimo, una rutina previa corta y la visualización del movimiento. La confianza mejora con práctica y con metas alcanzables.",
        "Si el nerviosismo o el malestar son muy intensos, no se pasan o afectan el sueño y el ánimo durante varios días, no se enfrentan en soledad: se habla con una persona adulta de confianza o con un profesional de la salud. Este cuaderno no diagnostica ni reemplaza esa ayuda. Los datos de ejemplo son ficticios.",
    ],
    vocab=[("motivación intrínseca", "impulso que viene del disfrute de la actividad"), ("motivación extrínseca", "impulso que viene de algo externo, como un premio"), ("nerviosismo", "activación antes de una tarea importante"), ("concentración", "dirigir la atención a lo importante de la tarea"), ("meta concreta", "objetivo propio, claro y alcanzable")],
    worked=[
        ("Reconocer una motivación", "Una estudiante de ejemplo practica porque le encanta jugar con su grupo. ¿Qué tipo de motivación es?", ["El impulso viene del disfrute de la actividad.", "Es motivación intrínseca."], "Intrínseca"),
        ("Elegir una estrategia", "Una persona de ejemplo se siente muy nerviosa justo antes de partir. ¿Qué estrategia sencilla puede probar?", ["Puede hacer respiración lenta y repetir una frase de ánimo.", "Si el malestar es muy fuerte, lo conversa con una persona adulta."], "Respiración lenta y frase de ánimo"),
    ],
    mistakes=[("Pensar que sentir nervios es una debilidad.", "Es una reacción común y se puede aprender a regularla.", "Usa estrategias y pide ayuda si pesa mucho."),
              ("Fijar como meta «ganarle a todas las demás».", "Depende de otras personas y no de lo que se puede controlar.", "Fija una meta propia y concreta.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es la motivación intrínseca?', 'El impulso de practicar que viene del disfrute de la actividad misma', 'Practicar solo para obtener un premio o un reconocimiento externo', 'Practicar porque otra persona lo exige y no se puede evitar', 'Intrínseca significa que el impulso viene del disfrute propio.'),
        ('=', '{F} ¿Cuántos puntos bajó su nerviosismo desde una hora antes hasta después de la respiración?', '8-5', 'Se resta el nerviosismo posterior al de una hora antes.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos subió su concentración después de fijarse la meta concreta?', '7-4', 'Se resta la concentración inicial a la posterior.', ' puntos'),
        ('abc', '{F} ¿Qué estrategia usó Fabián para bajar el nerviosismo?', 'Respiración lenta y repetir una frase de ánimo', 'Evitar el calentamiento para llegar con más energía', 'Competir sin ninguna preparación previa ni rutina de concentración', 'La ficha dice que usó respiración lenta y una frase de ánimo.'),
        ('abc', '{F} ¿Por qué la meta «mantener el ritmo los primeros 200 metros» ayuda a la concentración?', 'Porque es concreta y dirige la atención a algo que puede controlar', 'Porque es muy general y no exige a la persona nada en concreto', 'Porque ignora lo que ocurre durante la carrera y se centra en ganar', 'Una meta concreta y propia dirige la atención.'),
        ('abc', '{F} ¿Qué tipo de motivación aparece en el caso?', 'Intrínseca: disfruta correr con su equipo', 'Extrínseca: busca solo un premio por practicar', 'Ninguna: el caso no menciona por qué practica', 'Disfrutar la actividad con su equipo es motivación intrínseca.'),
        ('abc', 'Un poco de nerviosismo antes de competir, ¿es siempre algo negativo?', 'No: un nivel moderado puede ayudar a estar atento, pero uno muy alto perjudica', 'Sí, siempre perjudica el rendimiento, por pequeño que sea el nerviosismo', 'Sí, porque indica que la persona no se preparó bien para competir', 'Un nivel moderado de activación puede ayudar.'),
        ('abc', '{F} Fabián anota 9 de 10 de nerviosismo, siente el corazón latir muy fuerte y no logra calmarse. ¿Qué corresponde?', 'Avisar a una persona adulta o a un profesional, y probar respirar lento', 'Ocultarlo y competir igual, porque el nerviosismo se pasa solo al partir', 'Tomar un producto con promesa de calma que le ofrezca un amigo', 'Un malestar intenso se conversa con una persona adulta o un profesional.'),
        ('=', 'Fabián anota su nerviosismo antes de cada una de 4 competencias de ejemplo: 8, 6, 6 y 4. ¿Cuál es el promedio?', '(8+6+6+4)/4', 'Se suman los cuatro valores y se divide entre 4.', ' puntos'),
        ('abc', 'Alguien le dice: «Los nervios son debilidad». ¿Qué corresponde responder?', 'Es común sentir nervios y se pueden regular; se pide ayuda si pesan mucho', 'Tiene razón: debe esconderlos para que nadie piense que es débil', 'Debe competir sin pensar en ello y no hablar con nadie del tema', 'Los nervios son comunes y existen estrategias para regularlos.'),
        ('abc', 'Una estudiante tiene como meta «ganarle a todas las demás». ¿Qué problema tiene esa meta?', 'Depende de otras personas; mejor una meta propia, como mejorar su tiempo', 'Es perfecta, porque motiva más que cualquier otra meta personal', 'No tiene ningún problema, porque ganarle a otras personas se puede controlar', 'Una meta propia depende de lo que la persona puede controlar.'),
        ('abc', '{F} Fabián quiere que su rutina previa funcione cada vez. ¿Qué conviene?', 'Repetir una rutina corta con calentamiento, respiración y una meta concreta', 'Cambiar la rutina cada vez, para sorprenderse y mantener la atención', 'Eliminar el calentamiento para no cansarse antes de empezar la carrera', 'Una rutina repetida da seguridad y prepara cuerpo y mente.'),
        ('abc', '{F} Tras una competencia, Fabián anota: «salió mal porque soy un fracaso». ¿Qué respuesta es más útil?', 'Revisar qué se pudo ajustar en preparación, técnica o estrategia', 'Aceptar que es un fracaso y no volver a pensar en la carrera', 'Evitar competir de nuevo hasta sentirse completamente seguro de ganar', 'Se analizan acciones ajustables, no se etiqueta a la persona.'),
    ],
    ctx=('abc', 'Antonia, persona ficticia, se pone tan nerviosa antes de cada prueba que no duerme desde hace varios días. ¿Qué decisión es más razonable?', 'Conversar con una persona adulta de confianza o con un profesional', 'Guardarlo en secreto y competir igual, porque ya pasará con el tiempo', 'Tomar un producto para dormir sin preguntar a ninguna persona adulta', 'Si el malestar dura varios días y afecta el sueño, se pide ayuda.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué diferencia hay entre motivación intrínseca y extrínseca?", "La intrínseca viene del disfrute; la extrínseca, de algo externo como un premio", "El origen del impulso es distinto."),
        ("¿Qué tipo de meta ayuda a la concentración?", "Una meta propia, concreta y alcanzable", "Depende de lo que la persona puede controlar."),
        ("¿Qué haces si el nerviosismo es muy intenso o dura varios días?", "Hablarlo con una persona adulta de confianza o con un profesional", "Un malestar intenso no se enfrenta en soledad."),
    ],
    op=("Con estos datos de ejemplo de una persona ficticia: nerviosismo 9 de 10 antes de una carrera, concentración 3 de 10 y motivación porque su equipo la apoya. Elige dos estrategias seguras (respiración lenta, frase de ánimo, rutina previa, visualización, meta concreta), explica cómo las aplicarías y qué harías si el nerviosismo fuera muy intenso o durara varios días.",
        "Estrategias: una rutina previa corta y una meta concreta, «mantener un ritmo parejo en la primera mitad de la carrera». Si el nerviosismo fuera muy intenso o durara varios días, lo conversaría con una persona adulta de confianza o con un profesional de la salud.",
        ["dos estrategias seguras explicadas", "meta propia y concreta", "plan de pedir ayuda si el malestar es intenso"],
        ["texto con estrategias y plan de ayuda"],
        ["fijar metas que dependen de otras personas", "ocultar un malestar intenso", "tomar productos para calmarse"],
        "Pregunta: «¿qué haces si el nerviosismo no se pasa en varios días?». Si dice «lo aguanto», pídele recordar a quién avisaría."),
    reinforce="Escribe una rutina previa corta de tres pasos (calentamiento, respiración, meta concreta) para una actividad que practiques.",
    extend="Explica por qué fijar metas propias es mejor para la concentración y la confianza que compararse con otras personas.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 28 (encuesta de ejemplo, inventada, en un colegio ficticio). Se preguntó a 100 estudiantes que casi no practican actividad física por qué. Cada estudiante eligió una razón: "
     "falta de tiempo, 35; no hay espacios o equipos cerca, 25; las actividades que se ofrecen no les interesan, 20; comentarios burlones de otras personas sobre cómo se mueven o cómo se ven, 12; no tienen con quién practicar, 8.")
build(
    O6, 4, F,
    use="Aprenderé a analizar factores sociológicos del rendimiento y de la práctica, como el acceso, el apoyo, la convivencia y los estereotipos, leyendo datos de una encuesta de ejemplo y proponiendo medidas de respeto e inclusión.",
    prior=["Sé qué es un estereotipo.", "Sé calcular porcentajes.", "Sé avisar a una persona adulta ante una falta de respeto."],
    explain=[
        "Los factores sociológicos son condiciones del entorno social que influyen en cuánto y cómo se practica actividad física. Incluyen el apoyo de la familia y las amistades, el acceso (tiempo, espacios, equipos y costos), la oferta de actividades y su variedad, la convivencia (respeto o burlas), las ideas y estereotipos de la comunidad y los modelos que muestran los medios y las redes.",
        "Una encuesta resume razones en porcentajes. Con 100 personas, cada número es también un porcentaje. Se analiza agrupando razones por tipo (acceso, interés, convivencia, compañía) y se proponen medidas: horarios más cortos, espacios cercanos, más variedad de actividades, reglas de respeto y espacios con compañía. Faltar tiempo no es lo mismo que no tener interés: hay que preguntar y ofrecer opciones.",
        "Los comentarios burlones sobre cómo se mueve o se ve una persona son una falta de respeto: no se repiten, se apoya a quien los recibe y se avisa a una persona adulta responsable, como un docente, si se repiten. Nadie evalúa ni compara cuerpos. Los datos del cuaderno son de ejemplo.",
    ],
    vocab=[("factor sociológico", "condición del entorno social que influye en la práctica"), ("acceso", "posibilidad de usar tiempo, espacios y equipos"), ("convivencia", "forma de tratarse entre las personas"), ("inclusión", "que todas las personas puedan participar con respeto"), ("encuesta", "preguntas a un grupo para resumir sus respuestas")],
    worked=[
        ("Agrupar razones", "Una encuesta de ejemplo tiene: falta de tiempo 30, falta de espacios 20, burlas 10, falta de interés 40. ¿Qué porcentaje es de acceso?", ["Acceso reúne tiempo y espacios: 30 + 20 = 50.", "Con 100 personas, es 50 %."], "50 %"),
        ("Proponer una medida", "Una razón frecuente de ejemplo es «las actividades no me interesan». ¿Qué medida responde?", ["Ofrecer una mayor variedad de actividades.", "Preguntar a las personas cuáles les gustarían."], "Más variedad de actividades"),
    ],
    mistakes=[("Interpretar «no tengo tiempo» como «no quiero practicar».", "Son razones distintas y se resuelven distinto.", "Pregunta y ofrece opciones cortas y variadas."),
              ("Reírse de un comentario burlón para no quedar fuera.", "Mantiene la falta de respeto y daña a la persona.", "No lo repitas, apoya a la persona y avisa a una persona adulta si se repite.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es un factor sociológico?', 'Una condición del entorno social, como el apoyo o el acceso a espacios', 'Una característica del corazón de una persona que practica deporte', 'Una característica de la técnica de un salto o de una carrera', 'Lo sociológico se refiere al entorno social.'),
        ('=', '{F} Entre las razones de falta de espacios o equipos y las actividades que no interesan, ¿qué porcentaje reúnen?', '25+20', 'Con 100 estudiantes, cada número equivale a un porcentaje y se suman ambos.', ' %'),
        ('abc', '{F} ¿Cuál es la razón más frecuente?', 'La falta de tiempo', 'Los comentarios burlones', 'No tener con quién practicar', 'La falta de tiempo reúne 35, el número más alto.'),
        ('abc', '{F} ¿Qué razones se relacionan con el acceso?', 'Falta de tiempo y falta de espacios o equipos cerca', 'Comentarios burlones y falta de compañía para practicar', 'Intereses distintos y burlas de otras personas del colegio', 'El acceso es la posibilidad de contar con tiempo, espacios y equipos.'),
        ('=', '{F} ¿Cuántos de los 100 estudiantes mencionan razones ligadas al trato de otras personas, es decir, burlas o falta de compañía?', '12+8', 'Se suman los estudiantes que mencionan burlas y los que no tienen con quién practicar.', ' estudiantes'),
        ('abc', '{F} ¿Qué razón es un problema de convivencia que el colegio debe abordar?', 'Los comentarios burlones sobre cómo se mueven o cómo se ven', 'La falta de tiempo para practicar durante los días de semana', 'Las actividades que no interesan a las personas que respondieron', 'Las burlas son una falta de respeto entre personas.'),
        ('abc', '{F} ¿Qué medida responde a la razón «las actividades ofrecidas no les interesan»?', 'Ofrecer más variedad de actividades, como baile, juegos y caminatas', 'Eliminar todas las actividades que hoy se ofrecen en el colegio', 'Obligar a participar en una sola actividad para todo el curso', 'La variedad permite que más personas encuentren algo de su interés.'),
        ('=', '{F} Si 7 de los 12 estudiantes que señalan burlas dejan de sentirse señalados tras una campaña de respeto, ¿cuántos siguen con el problema?', '12-7', 'Se resta a los 12 los 7 que ya no tienen el problema.', ' estudiantes'),
        ('ab', '{F} ¿Qué actitud corresponde ante un comentario burlón sobre el cuerpo de alguien?', 'No repetirlo, apoyar a la persona y avisar a un adulto si se repite', 'Reírse para no quedar fuera del grupo y no tener problemas con él', 'No repetir la burla y apoyar a la persona evita dañar y mantiene el respeto.'),
        ('abc', 'Alguien concluye: «Si el 35 % no tiene tiempo, esas personas no quieren practicar». ¿Qué falla?', 'Confunde falta de tiempo con falta de interés de las personas', 'Nada: no tener tiempo es lo mismo que no querer practicar nunca', 'Que el porcentaje es incorrecto, porque los datos no se pueden sumar', 'Falta de tiempo y falta de interés son razones distintas.'),
        ('abc', 'Un grupo dice: «Ese deporte es solo para hombres». ¿Qué corresponde?', 'Reconocer que es un estereotipo y que cada persona puede elegir su deporte', 'Aceptarlo como una regla del colegio y aplicarla a todo el curso', 'Burlarse de quienes lo dicen, para que dejen de decirlo en el patio', 'Un estereotipo no es una regla ni un dato.'),
        ('=', '{F} Si la mitad de los 20 estudiantes a quienes no interesan las actividades ofrecidas encuentran una que les gusta, ¿cuántos siguen sin interés?', '20-20/2', 'Se resta a los 20 la mitad que ya encontró una actividad.', ' estudiantes'),
        ('abc', '{F} Alguien propone preguntar también por qué practican las personas que sí lo hacen. ¿Qué ventaja tiene?', 'Permite conocer qué ayuda, como apoyo y compañía, y no solo los obstáculos', 'Ninguna, porque con la primera encuesta ya se sabe todo lo necesario', 'Sirve para ordenar a las personas según su cuerpo y su rendimiento', 'Conocer los apoyos ayuda a diseñar medidas más completas.'),
    ],
    ctx=('abc', 'En otra encuesta de ejemplo con 100 estudiantes, 40 dicen «no tengo con quién practicar» y 30 «no hay horarios que me sirvan». ¿Qué medida es más coherente?', 'Organizar grupos con horarios variados y cortos, abiertos a todos los niveles', 'Eliminar la actividad física del colegio para evitar los problemas', 'Pedir a cada persona que practique sola en su casa y sin apoyo de nadie', 'Se responde a la compañía y a los horarios con grupos y horarios variados.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué es el acceso a la práctica?", "La posibilidad de usar tiempo, espacios y equipos", "Es un factor sociológico del entorno social."),
        ("¿Qué se hace ante un comentario burlón sobre el cuerpo de alguien?", "No repetirlo, apoyar a la persona y avisar a una persona adulta responsable si se repite", "El respeto es parte de la convivencia."),
        ("¿Una idea fija sobre quién puede practicar un deporte es un dato?", "No: es un estereotipo", "No tiene respaldo y es solo una idea fija."),
    ],
    op=("Con esta encuesta de ejemplo de 100 estudiantes: falta de tiempo, 25; falta de espacios, 15; las actividades no interesan, 30; burlas, 20; falta de compañía, 10. Agrupa las razones por tipo (acceso, interés, convivencia, compañía), calcula los porcentajes de acceso y de convivencia y propone dos medidas, una de ellas de respeto e inclusión.",
        "Acceso: 25 + 15 = 40 %. Convivencia: 20 %. Interés: 30 %. Compañía: 10 %. Medidas: horarios cortos y espacios cercanos; reglas de respeto, apoyo a quien recibe burlas y aviso a una persona adulta si se repiten.",
        ["agrupa las razones por tipo", "calcula bien los dos porcentajes", "propone dos medidas, una de respeto e inclusión"],
        ["agrupación, cálculos y medidas escritas"],
        ["confundir falta de tiempo con falta de interés", "culpar a las personas", "proponer burlas o comparar cuerpos"],
        "Pregunta: «¿qué razón no se resuelve con más horarios?». Si dice «ninguna», pídele mirar las burlas y los intereses."),
    reinforce="Escribe tres razones por las que una persona podría no practicar una actividad y una medida para cada una. No uses datos reales de personas.",
    extend="Explica por qué un buen clima de respeto es una condición para que más personas practiquen actividad física.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 29 (caso de ejemplo, inventado). Valeria, estudiante ficticia, corre 1 kilómetro y su tiempo pasó de 400 a 420 segundos en dos semanas. Datos anotados: "
     "(1) durmió poco cuatro noches; (2) sus hombros se ven más tensos al correr; (3) siente mucha presión antes de las pruebas; (4) cambió de horario y ahora entrena sola, sin su grupo. Hace 4 sesiones por semana.")
build(
    O6, 5, F,
    use="Aprenderé a evaluar un caso integrando factores fisiológicos, biomecánicos, psicológicos y sociológicos, a priorizar ajustes de uno en uno y a reconocer los límites de las conclusiones.",
    prior=["Sé clasificar factores en los cuatro tipos.", "Sé registrar y ajustar una sola condición.", "Sé pedir ayuda ante un malestar."],
    explain=[
        "Evaluar un caso es juntar los datos de los cuatro tipos de factores, ver cómo se pueden relacionar y decidir qué ajustar. Los factores se influyen entre sí: dormir poco puede aumentar la sensación de presión y la tensión al moverse, y entrenar sin el grupo puede bajar la motivación. Por eso rara vez un solo factor explica un cambio.",
        "Para ajustar se prioriza: primero la seguridad y la salud; luego los factores que se pueden cambiar con facilidad y bajo riesgo, como el sueño o el horario de práctica; después la técnica y los aspectos mentales con ayuda del docente. Se cambia una sola condición, se registra y se vuelve a evaluar. Una mejora posterior se interpreta con cuidado: puede relacionarse con el cambio, pero otros factores también influyen.",
        "Las conclusiones tienen límites: con pocos datos no se puede asegurar la causa, y no se juzga a la persona. Si hay presión o malestar intensos, o dolor, se conversa con una persona adulta de confianza o con un profesional de la salud. Los datos de este cuaderno son ficticios.",
    ],
    vocab=[("integrar", "juntar datos de varios tipos para entender un caso"), ("prioridad", "lo que se atiende primero"), ("relación entre factores", "forma en que un factor puede influir en otro"), ("límite de la conclusión", "lo que los datos no permiten asegurar"), ("ajuste", "cambio de una condición según los datos")],
    worked=[
        ("Priorizar ajustes", "Un caso de ejemplo duerme poco, tiene la técnica tensa y entrena solo. ¿Qué cambia primero?", ["Elige un factor fácil de cambiar y de bajo riesgo: el sueño.", "Registra el efecto antes de cambiar otro."], "El sueño, y luego se registra"),
        ("Reconocer un límite", "Tras dormir mejor dos semanas, el tiempo de una persona de ejemplo mejora un poco. ¿Qué se dice con cuidado?", ["Pudo relacionarse con el sueño.", "No se puede asegurar que sea la única causa."], "Pudo relacionarse con el sueño, sin asegurar una única causa"),
    ],
    mistakes=[("Cambiar varios factores a la vez para «arreglarlo rápido».", "No se sabe cuál produjo el efecto.", "Cambia uno y registra."),
              ("Concluir que la persona «perdió condición física» con estos datos.", "Hay varios factores posibles y los datos no bastan para juzgar.", "Habla de factores posibles y no etiquetes a la persona.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿por qué conviene analizar varios factores a la vez?', 'Porque el rendimiento suele depender de varios factores que se influyen', 'Porque un solo factor siempre lo explica todo en cualquier caso', 'Porque así se evita tener que medir cualquier dato de la persona', 'Los factores de distinto tipo se influyen mutuamente.'),
        ('=', '{F} ¿Cuántos segundos empeoró su tiempo en las dos semanas?', '420-400', 'Se resta el tiempo inicial al tiempo final.', ' segundos'),
        ('abc', '{F} ¿Cuál de los datos es sociológico?', 'El dato 4: ahora entrena sola, sin su grupo', 'El dato 1: durmió poco', 'El dato 2: hombros tensos al correr', 'Entrenar sin el grupo es una condición del entorno social.'),
        ('abc', '{F} ¿Qué dato es biomecánico?', 'El dato 2, los hombros tensos al correr', 'El dato 3, la presión antes de las pruebas', 'El dato 1, dormir poco', 'La tensión en los hombros se relaciona con la técnica del movimiento.'),
        ('=', '{F} ¿Qué porcentaje del tiempo inicial empeoró?', '(420-400)*100/400', 'Se calcula el empeoramiento de 20 segundos y se divide entre los 400 iniciales.', ' %'),
        ('abc', '{F} ¿Qué relación puede haber entre los datos 1 y 3?', 'Dormir poco puede aumentar la presión que se siente y ambos influyen en el tiempo', 'No pueden estar relacionados, porque son de tipos distintos de factor', 'El dato 1 explica el dato 3 sin ninguna duda ni otra causa posible', 'Los factores pueden influirse, pero no se asegura una relación única.'),
        ('abc', '{F} ¿Qué ajuste de una sola condición es razonable primero?', 'Cuidar el sueño por dos semanas y registrar el efecto en el tiempo', 'Cambiar sueño, técnica, grupo y ritmo a la vez, para ir más rápido', 'Dejar de correr hasta que el rendimiento mejore solo, sin hacer nada', 'Cambiar una sola condición permite evaluar su efecto.'),
        ('abc', '{F} ¿Qué conviene hacer con el dato sociológico 4?', 'Buscar entrenar con su grupo o con compañía y ver si cambia su motivación', 'Ignorar el dato, porque el entorno social no influye en el rendimiento', 'Culparla por entrenar sola, porque debió pedir permiso al grupo antes', 'Restablecer la compañía puede ayudar a la motivación.'),
        ('ab', '{F} ¿Se puede asegurar que dormir poco causó el peor tiempo?', 'No: es un factor posible entre varios; se ajusta y se registra', 'Sí: es la única causa del cambio y no hace falta revisar más', 'Con pocos datos solo se pueden proponer factores posibles, no una causa única.'),
        ('abc', 'Un compañero dice: «Con estos datos se sabe que Valeria perdió condición física». ¿Qué falla?', 'Hay varios factores posibles y no se puede juzgar a la persona', 'Nada: es evidente que pierde condición cuando el tiempo empeora', 'Que no se pueden registrar datos de una persona en una semana', 'Los datos no bastan para asegurar una causa ni para etiquetar a alguien.'),
        ('abc', 'Valeria siente una presión intensa y un malestar que no se van. ¿Qué corresponde?', 'Hablarlo con una persona adulta de confianza o con un profesional', 'Ocultarlo para no preocupar a nadie y esperar que se pase solo', 'Entrenar más fuerte hasta que pase, porque el esfuerzo cura todo', 'Un malestar intenso se conversa con una persona adulta o un profesional.'),
        ('=', 'Valeria registra 4 sesiones por semana durante 3 semanas con 3 datos por sesión: sueño, esfuerzo y ánimo. ¿Cuántos datos reúne?', '4*3*3', 'Se multiplican sesiones por semana, semanas y datos por sesión.', ' datos'),
        ('abc', '{F} Tras 3 semanas con más sueño, su tiempo baja de 420 a 410 segundos. ¿Qué se concluye con cuidado?', 'Hubo mejora que puede relacionarse con el sueño, junto a otros factores', 'El sueño es la única causa de la mejora, porque el tiempo bajó', 'Los demás factores no importan, porque el sueño lo explica todo', 'Se interpreta la mejora con cuidado y sin una causa única.'),
    ],
    ctx=('abc', 'Joaquín, persona ficticia, corre peor desde que se cambió de horario: duerme menos, entrena solo y siente más presión. Su técnica no cambió. ¿Qué plan de evaluación es más razonable?', 'Priorizar un cambio simple, como la compañía, y registrar el efecto', 'Cambiar su técnica de carrera porque es lo único que se puede medir', 'Dejar el deporte hasta que todo vuelva a ser como era antes del cambio', 'Se prioriza un cambio simple y se registra, sin juzgar a la persona.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué se prioriza primero al ajustar un caso?", "La seguridad y la salud, y luego un factor fácil y de bajo riesgo", "Se cambia una sola condición a la vez."),
        ("¿Se puede asegurar la causa de un cambio con pocos datos?", "No: solo se proponen factores posibles", "Los datos tienen límites y no prueban todo."),
        ("¿Qué haces ante una presión o malestar intensos?", "Hablarlo con una persona adulta de confianza o con un profesional", "Estos malestares no se enfrentan en soledad."),
    ],
    op=("Con este caso de ejemplo: una persona ficticia baja su rendimiento en una prueba de pases contra una pared, de 20 a 14 pases correctos en 30 segundos. Datos: duerme poco, su muñeca se ve rígida al pasar, teme equivocarse frente al grupo y ahora practica sola. Integra los factores de los cuatro tipos, prioriza un ajuste de una sola condición, escribe qué conclusión no podrías asegurar y a quién pedirías ayuda si el malestar fuera intenso.",
        "Fisiológico: duerme poco. Biomecánico: muñeca rígida. Psicológico: teme equivocarse. Sociológico: practica sola. Ajuste: volver a practicar con compañía y registrar. No podría asegurar la causa única. Si el malestar fuera intenso, lo conversaría con una persona adulta de confianza o con un profesional.",
        ["integra los cuatro tipos de factores", "prioriza un ajuste de una condición", "reconoce los límites y pide ayuda si hace falta"],
        ["integración, ajuste y límites escritos"],
        ["atribuir todo a un solo factor", "cambiar varias condiciones a la vez", "asegurar la causa sin datos"],
        "Pregunta: «¿qué no puedes asegurar con estos datos?». Si dice «todo», pídele separar lo que sí muestran."),
    reinforce="Escribe un caso inventado con un dato de cada tipo de factor y propón un ajuste de una sola condición con la forma de registrarlo.",
    extend="Explica por qué las conclusiones sobre el rendimiento deben decir lo que los datos no permiten asegurar.",
)
