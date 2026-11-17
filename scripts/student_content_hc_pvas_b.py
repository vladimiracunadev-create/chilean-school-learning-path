"""Promoción de estilos de vida activos y saludables, 3.º y 4.º medio HC: OAC-03 (programas de entrenamiento para la condición física asociada a la salud) y OAC-04 (impacto del ejercicio en el bienestar personal y social). Pruebas, registros y encuestas inventados «de ejemplo», descritos por escrito; sin mediciones reales."""
from __future__ import annotations

from hc_pvas_common import build

O3 = "EF-PVAS-3y4-OAC-03"
O4 = "EF-PVAS-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 9 (pruebas de ejemplo, inventadas; se hacen solo con docente cerca, con calentamiento y sin forzar). Componentes de la condición física asociada a la salud: "
     "a) resistencia: prueba de caminata de 6 minutos a paso firme, se anota la distancia en metros; "
     "b) fuerza muscular: sentarse y pararse de una silla estable, apoyada en la pared, durante 30 segundos, se anotan las repeticiones; "
     "c) flexibilidad: sentada o sentado con las piernas extendidas, se estira el brazo hacia los pies y se anota a cuántos centímetros de la punta de los pies se llega; "
     "d) composición corporal: proporción entre músculo, grasa, hueso y agua del cuerpo; la evalúan profesionales de la salud, y en este cuaderno no se mide ni se compara. "
     "Registro privado de Daniela (de ejemplo): caminata de 6 minutos, 540 metros; silla en 30 segundos, 12 repeticiones; alcance, a 4 centímetros de la punta de los pies.")
build(
    O3, 1, F,
    use="Aprenderé a diagnosticar de forma privada y segura los componentes de la condición física asociada a la salud (resistencia, fuerza, flexibilidad y composición corporal) y a fijar una línea de base propia para un programa de entrenamiento.",
    prior=["Sé clasificar actividades por tipo e intensidad.", "Sé que mis registros son privados.", "Sé que la salud no es una apariencia."],
    explain=[
        "La condición física asociada a la salud es el conjunto de capacidades del cuerpo que ayudan a vivir con energía y a cuidar la salud a largo plazo. Tiene cuatro componentes: la resistencia (sostener un esfuerzo), la fuerza muscular (mover una resistencia), la flexibilidad (mover las articulaciones en buen rango) y la composición corporal (la proporción de músculo, grasa, hueso y agua).",
        "Un programa de entrenamiento comienza con un diagnóstico: pruebas simples y seguras que dan una línea de base, es decir, el punto de partida de una persona. Se repiten con las mismas condiciones para ver cambios en el tiempo. La resistencia se puede probar con una caminata de 6 minutos, la fuerza con repeticiones de sentarse y pararse de una silla estable y la flexibilidad con el alcance hacia los pies. La composición corporal la evalúan profesionales de la salud: aquí solo se conoce el concepto, no se mide ni se compara.",
        "Los resultados son privados y se comparan solo con uno mismo, nunca para ordenar personas ni opinar sobre cuerpos. Se hacen con calentamiento, con una persona docente cerca y sin forzar: si hay dolor, mareo o falta de aire inusual, se detiene la prueba y se avisa a una persona adulta.",
    ],
    vocab=[("condición física asociada a la salud", "capacidades del cuerpo que ayudan a cuidar la salud"), ("resistencia", "capacidad de sostener un esfuerzo"), ("fuerza muscular", "capacidad de mover una resistencia"), ("flexibilidad", "capacidad de mover las articulaciones en buen rango"), ("composición corporal", "proporción de músculo, grasa, hueso y agua; la evalúan profesionales"), ("línea de base", "punto de partida con el que se comparan los cambios")],
    worked=[
        ("Relacionar prueba y componente", "Una persona de ejemplo anota que en 30 segundos se sentó y se paró 9 veces de una silla estable. ¿Qué componente refleja?", ["La prueba cuenta repeticiones contra la resistencia del propio cuerpo.", "Eso corresponde a la fuerza muscular."], "Fuerza muscular"),
        ("Fijar una línea de base", "Una persona de ejemplo camina 480 metros en los 6 minutos de la prueba. ¿Qué papel tiene ese dato?", ["Es su punto de partida: no se compara con nadie.", "Se repetirá en las mismas condiciones para ver si cambia."], "Es su línea de base de resistencia"),
    ],
    mistakes=[("Medir el cuerpo de otras personas o comparar cifras entre estudiantes.", "La composición corporal la evalúan profesionales y compararla daña la convivencia.", "Usa solo pruebas de ejecución y compara contigo en el tiempo."),
              ("Cambiar las condiciones de la prueba cada vez.", "Si cambian el lugar o el calzado, no se sabe si hubo mejora real.", "Repite la prueba en las mismas condiciones.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es la condición física asociada a la salud?', 'El conjunto de capacidades del cuerpo que ayudan a cuidar la salud', 'El rendimiento que se logra en un deporte de competencia', 'La apariencia y las medidas del cuerpo de cada persona', 'Son capacidades del cuerpo, no resultados de competencias ni apariencia.'),
        ('abc', '{F} ¿Qué prueba de la ficha refleja la resistencia?', 'La caminata de 6 minutos', 'La silla durante 30 segundos', 'El alcance hacia los pies', 'La caminata sostiene un esfuerzo y se mide en metros.'),
        ('abc', '{F} ¿Qué mide la prueba c, el alcance hacia los pies?', 'La flexibilidad', 'La fuerza muscular', 'La composición corporal', 'El alcance en centímetros refleja el rango de movimiento de las articulaciones.'),
        ('abc', '{F} ¿Por qué la composición corporal no se mide en este cuaderno?', 'Porque la evalúan profesionales de la salud, y compararla puede dañar', 'Porque es un dato que no tiene ninguna relación con la salud de las personas', 'Porque se mide solo con la prueba de caminata de 6 minutos de la ficha', 'Su evaluación corresponde a profesionales; en el curso no se mide ni se compara.'),
        ('abc', '¿Qué es una línea de base?', 'El punto de partida con el que se comparan los cambios', 'La meta final que se debe alcanzar al terminar el programa', 'El resultado más alto de todo el curso', 'La línea de base es el punto de partida propio, no la meta ni un récord.'),
        ('abc', '{F} ¿Por qué se repite una prueba en las mismas condiciones?', 'Para atribuir un cambio del resultado a la práctica y no al lugar', 'Para que el resultado salga siempre igual y no cambie nunca durante el programa', 'Para que todas las personas del curso obtengan exactamente el mismo número', 'Mantener las condiciones permite comparar sesiones de forma honesta.'),
        ('=', '{F} ¿Cuántos metros por minuto, en promedio, caminó Daniela en la prueba?', '540/6', 'Se divide la distancia total por los 6 minutos de la prueba.', ' metros por minuto'),
        ('abc', '{F} Daniela quiere llegar a 15 repeticiones en la silla. ¿Qué dato de la ficha es su línea de base en fuerza?', '12 repeticiones en 30 segundos', '15 repeticiones en 30 segundos', '4 centímetros de la punta de los pies', 'La línea de base es el punto de partida, no la meta.'),
        ('=', '{F} Si Daniela mantiene el ritmo de la prueba de la silla durante 60 segundos, ¿cuántas repeticiones haría?', '12*2', 'Se duplica el resultado de 30 segundos para estimar 60 segundos con el mismo ritmo.', ' repeticiones'),
        ('abc', 'Ana dice: «mi caminata de 6 minutos fue de 500 metros y la de Bruno de 580, así que soy peor». ¿Qué respuesta es más adecuada?', 'Las líneas de base son personales; lo útil es comparar a Ana con otra semana propia', 'Tiene razón, porque la distancia caminada mide el valor completo de cada persona', 'Debe repetir la prueba hasta superar a Bruno cueste lo que cueste, aunque se canse', 'La línea de base se compara con uno mismo; no ordena personas.'),
        ('abc', 'Un compañero pide que cada estudiante anote públicamente su peso y su estatura para «ver quién está mejor». ¿Qué corresponde?', 'No participar y explicar que esos datos son privados y no miden la salud de nadie', 'Hacerlo, porque medirse en público ayuda a comparar los resultados con honestidad', 'Anotar cifras inventadas para no quedar al final de la lista de estudiantes', 'Los datos del cuerpo son privados y su comparación pública daña; la salud no es una cifra.'),
        ('abc', 'Durante la prueba de caminata, una estudiante de ejemplo siente mareo. ¿Qué hace el docente y qué hace ella?', 'Ella se detiene, se sienta y avisa; el docente avisa a una persona adulta', 'Ella sigue caminando más lento para poder completar los 6 minutos de la prueba', 'Ella se apura para terminar la prueba antes de que el mareo aumente más', 'El mareo es señal de detención: se para, se descansa y se avisa.'),
        ('=', '{F} En la caminata, Daniela repite la prueba en otras condiciones y logra 600 metros. ¿Cuántos metros más que en su línea de base?', '600-540', 'Se resta la distancia de la línea de base de la distancia nueva.', ' metros'),
    ],
    ctx=('abc', 'Elías hizo las tres pruebas de la ficha: caminata 500 metros, silla 10 repeticiones y alcance a 6 centímetros de la punta de los pies. ¿Qué anotación es coherente para su diagnóstico?', 'Línea de base propia de resistencia, fuerza y flexibilidad para comparar luego', 'Una nota que lo ubica frente a su curso según el resultado de su caminata de 6 minutos', 'Una meta que lo obliga a igualar a la persona con el mejor resultado del curso entero', 'Los números son su punto de partida; se comparan con sus repeticiones y no con las del curso.'),
    sc=[
        ("En Educación Física: ¿cuáles son los cuatro componentes de la condición física asociada a la salud de la clase?", "Resistencia, fuerza muscular, flexibilidad y composición corporal", "Son los cuatro que nombra el objetivo de aprendizaje."),
        ("¿Quién evalúa la composición corporal?", "Profesionales de la salud, no el curso", "No se mide ni se compara en el aula."),
        ("En esta asignatura: ¿con qué punto de partida se comparan los resultados de tus pruebas?", "Con mi propia línea de base de otro momento", "La comparación entre personas no tiene sentido ni respeto."),
    ],
    op=("Elige una de las tres pruebas de la ficha (caminata de 6 minutos, silla en 30 segundos o alcance hacia los pies). Describe en tu cuaderno las condiciones que mantendrías iguales al repetirla (lugar, calzado, hora, ropa), anota un resultado inventado como tu línea de base y escribe una regla de seguridad que cumplirías. El resultado es privado.",
        "Elijo la silla en 30 segundos: silla estable contra la pared, mismo calzado, misma hora. Línea de base inventada: 11 repeticiones. Seguridad: calentamiento de 5 minutos, docente cerca y detenerme si siento dolor o mareo.",
        ["condiciones que se mantienen", "línea de base anotada", "una regla de seguridad"],
        ["una prueba descrita con línea de base y seguridad"],
        ["comparar con otra persona", "cambiar las condiciones cada vez", "no incluir seguridad"],
        "Pregunta: «¿qué mantendrías igual para comparar la próxima vez?». Si dice «nada», pídele lugar, hora y calzado."),
    reinforce="Anota en tu cuaderno una prueba de ejemplo con sus condiciones y un resultado inventado como línea de base. No compares con otras personas.",
    extend="Explica por qué la composición corporal se deja a profesionales de la salud y por qué no se compara entre estudiantes.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 10 (programas de ejemplo, inventados, para elegir según la meta). "
     "P1: caminata rápida de 30 minutos, 3 veces por semana (resistencia). "
     "P2: circuito de 6 estaciones con el peso del propio cuerpo, 20 minutos, 2 veces por semana (fuerza muscular). "
     "P3: estiramientos suaves, sin dolor, 10 minutos al terminar cada sesión (flexibilidad). "
     "P4: «cambio rápido de cuerpo en 7 días», con ejercicios agotadores a diario (programa de moda, sin base y sin seguridad). "
     "Reglas de ejemplo de esta ficha: la meta se asocia a un componente de la condición física; el programa progresa de a poco (por ejemplo, 5 minutos más por semana como máximo); "
     "hay días de descanso entre sesiones de fuerza; no se promete ningún resultado del cuerpo. "
     "La composición corporal cambia lentamente con práctica regular y otros hábitos y se evalúa con profesionales; no se entrena con metas de cuerpo.")
build(
    O3, 2, F,
    use="Aprenderé a elegir un programa de entrenamiento según el componente de la condición física que se quiere mejorar, aplicando criterios de progresión, descanso y seguridad, y a descartar programas que prometen resultados rápidos del cuerpo.",
    prior=["Conozco los cuatro componentes de la condición física.", "Sé qué es una línea de base.", "Sé que la composición corporal no se compara."],
    explain=[
        "Un programa de entrenamiento es un plan con actividades, duración y frecuencia para mejorar un componente de la condición física. Para elegirlo, primero se nombra la meta y el componente que la trabaja: la resistencia se trabaja con caminata rápida u otra actividad aeróbica; la fuerza muscular con ejercicios con el peso del propio cuerpo; la flexibilidad con estiramientos suaves.",
        "Un programa seguro cumple reglas: avanza de a poco (se aumenta una condición por vez y en pequeñas cantidades), incluye descanso entre sesiones de fuerza, usa calentamiento y vuelta a la calma y no promete resultados del cuerpo. El «5 minutos más por semana» de la ficha es solo una regla de ejemplo para practicar el cálculo; no es una indicación para una persona real, cuyo plan lo define un profesional. La composición corporal no se entrena con metas de cuerpo: cambia lentamente con práctica regular y otros hábitos, y su evaluación corresponde a profesionales de la salud.",
        "Un programa de moda que promete cambios rápidos o ejercicios agotadores a diario no cumple esas reglas y puede causar daño. Si alguien quiere aplicar un programa, lo conversa con el docente o con un profesional, y ante dolor, mareo o falta de aire inusual detiene la práctica y avisa a una persona adulta.",
    ],
    vocab=[("programa de entrenamiento", "plan con actividades, duración y frecuencia para mejorar un componente"), ("progresión", "aumento gradual de una condición del programa"), ("frecuencia", "cuántas veces por semana se practica"), ("descanso", "tiempo para recuperarse entre sesiones"), ("programa de moda", "plan que promete resultados rápidos sin base ni seguridad")],
    worked=[
        ("Elegir por meta", "Una persona de ejemplo quiere sostener mejor un esfuerzo largo. ¿Qué programa de la ficha le corresponde?", ["La meta es la resistencia.", "El programa de caminata rápida de 30 minutos, 3 veces por semana, trabaja resistencia."], "P1"),
        ("Aplicar la progresión", "Con la regla de la ficha, una persona que hace 30 minutos de caminata quiere avanzar. ¿Hasta cuántos minutos puede llegar la semana siguiente?", ["La regla permite agregar como máximo 5 minutos por semana.", "30 + 5 son 35 minutos."], "Hasta 35 minutos"),
    ],
    mistakes=[("Elegir el programa más duro para lograr resultados más rápidos.", "Aumentar demasiado y sin descanso eleva el riesgo de lesión.", "Avanza de a poco y deja descanso entre sesiones."),
              ("Aceptar un programa que promete cambiar el cuerpo en pocos días.", "Ningún programa puede asegurarlo con seguridad y puede dañar.", "Compáralo con las reglas de seguridad y conversa con un profesional.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es un programa de entrenamiento?', 'Un plan con actividades, duración y frecuencia para mejorar un componente', 'Una competencia entre estudiantes con premios para quienes ganan cada prueba', 'Una sesión de práctica improvisada, sin objetivo ni registro de lo que se hizo', 'Un programa organiza qué, cuánto y cuántas veces se practica para una meta.'),
        ('abc', '{F} ¿Qué programa trabaja la flexibilidad?', 'P3, estiramientos suaves al terminar cada sesión', 'P1, caminata rápida de 30 minutos, 3 veces por semana', 'P2, circuito con el peso del cuerpo, 2 veces por semana', 'P3 son estiramientos suaves, que corresponden a la flexibilidad.'),
        ('abc', '{F} ¿Qué programa trabaja la fuerza muscular?', 'P2, circuito de 6 estaciones con el peso del cuerpo', 'P1, caminata rápida de 30 minutos, 3 veces por semana', 'P3, estiramientos suaves de 10 minutos al terminar la sesión', 'P2 mueve el propio cuerpo contra una resistencia.'),
        ('abc', '{F} ¿Por qué P4 no es un programa seguro?', 'Promete cambios rápidos del cuerpo y exige ejercicios agotadores a diario', 'Tiene demasiados días de descanso entre las sesiones de la semana completa', 'Se hace solo con el peso del propio cuerpo y sin ningún tipo de equipo', 'P4 incumple la progresión, el descanso y la regla de no prometer resultados del cuerpo.'),
        ('abc', '{F} Según la ficha, ¿qué ocurre con la composición corporal?', 'Cambia lentamente con práctica regular y otros hábitos, y la evalúan profesionales', 'Se entrena con metas de cuerpo y se mide cada semana dentro del curso entero', 'Cambia en una semana de entrenamiento si el programa es muy exigente y agotador', 'La composición corporal no se entrena con metas ni cambia rápido.'),
        ('abc', '¿Qué significa que un programa progrese de a poco?', 'Que aumenta una condición por vez y en cantidades pequeñas', 'Que cada semana cambia todo el programa por uno distinto', 'Que se mantiene igual para siempre aunque la persona mejore', 'La progresión gradual cambia una condición y poco a poco.'),
        ('=', '{F} ¿Cuántos minutos de práctica suma P1 en una semana?', '3*30', 'Se multiplican las sesiones por los minutos de cada una.', ' minutos'),
        ('abc', '{F} Una persona de ejemplo quiere fuerza y propone P2 cuatro días seguidos «para avanzar rápido». ¿Qué regla de la ficha se incumple?', 'La del descanso entre sesiones de fuerza', 'La de no prometer resultados del cuerpo', 'La de asociar la meta a un componente', 'Cuatro días seguidos de fuerza no dejan descanso entre sesiones.'),
        ('=', '{F} Una persona hace P2 durante 4 semanas, con 2 sesiones por semana. ¿Cuántos minutos de circuito suma?', '4*2*20', 'Se multiplican semanas por sesiones semanales y por minutos de cada sesión.', ' minutos'),
        ('abc', 'Una estudiante dice: «quiero un abdomen plano en una semana; elijo P4 porque lo promete». ¿Qué respuesta es más adecuada?', 'No elegirlo: ningún programa asegura eso; conversar con el docente o un profesional', 'Elegirlo, porque un programa que promete resultados tan rápidos debe funcionar bien', 'Elegir P4 pero hacerlo solo los fines de semana, con ejercicios algo más suaves', 'Una promesa rápida del cuerpo no es segura; la meta debe ser de salud y se conversa con un profesional.'),
        ('abc', '{F} Dos estudiantes proponen: Luz hace P1 y suma 10 minutos por semana; Mario hace P1 y suma 5 minutos por semana. Según la regla de la ficha, ¿qué propuesta cumple?', 'La de Mario, porque agrega el máximo permitido de 5 minutos', 'La de Luz, porque agrega más minutos y avanza más rápido', 'Las dos, porque ambas agregan algo de tiempo', 'La regla de ejemplo permite hasta 5 minutos más por semana.'),
        ('abc', 'Un cartel dice: «Programa X: 15 minutos diarios para bajar de peso». ¿Qué corresponde hacer al curso?', 'No usarlo como meta; los temas del cuerpo se conversan con profesionales', 'Adoptarlo en el curso, porque 15 minutos diarios parece poco tiempo y seguro', 'Aplicarlo con otro nombre en el curso para medir el peso de cada estudiante', 'Las metas de peso no corresponden a este cuaderno ni se aplican sin profesionales.'),
        ('abc', '{F} Si una persona siente dolor durante P2, ¿qué decisión es correcta?', 'Detenerse, descansar y avisar a una persona adulta antes de seguir', 'Bajar el ritmo y terminar las 6 estaciones del circuito completo', 'Pasar al programa P4, que tiene ejercicios más agotadores y rápidos', 'El dolor es señal de detención; no se continúa sin avisar.'),
    ],
    ctx=('abc', 'Mara quiere sentirse con más resistencia y más movilidad, y no tiene tiempo para más de 3 sesiones por semana. Con la ficha y sus reglas, ¿qué programa es coherente?', 'P1 tres veces por semana, con P3 de 10 minutos al terminar cada sesión', 'P4 siete días, porque promete cubrir ambas metas más rápido', 'P2 cuatro veces por semana, porque la fuerza mejora todos los componentes', 'P1 trabaja resistencia y P3 movilidad; se avanza de a poco y con 3 sesiones.'),
    sc=[
        ("En Educación Física: ¿qué componente trabaja un programa de caminata rápida?", "La resistencia", "La caminata sostiene un esfuerzo durante más tiempo."),
        ("¿Cuántas condiciones se aumentan por vez en la progresión?", "Una sola, en cantidades pequeñas", "Así se cuida el cuerpo y se sabe qué funcionó."),
        ("¿Qué se hace ante un programa que promete cambiar el cuerpo en pocos días?", "No usarlo y consultar a un profesional", "No tiene base ni es seguro."),
    ],
    op=("Elige un componente (resistencia, fuerza muscular o flexibilidad) y describe un programa de 2 semanas con tres sesiones por semana: actividad, minutos, descanso entre sesiones y cómo avanzarías de la semana 1 a la 2 sin pasar de los 5 minutos más de la regla de ejemplo de la ficha. Incluye una regla de seguridad. No incluyas metas de peso ni de apariencia.",
        "Resistencia: caminata rápida, lunes, miércoles y viernes. Semana 1: 20 minutos; semana 2: 25 minutos. Descanso: martes, jueves y fin de semana. Seguridad: calentamiento de 5 minutos, agua a mano y detenerme si hay mareo o dolor.",
        ["componente y actividad coherentes", "frecuencia, descanso y progresión de a poco", "regla de seguridad y sin metas de cuerpo"],
        ["programa de dos semanas con progresión y seguridad"],
        ["subir demasiado entre semanas", "no dejar descanso", "incluir metas de peso o apariencia"],
        "Pregunta: «¿cómo cambia tu programa entre la semana 1 y la 2?». Si responde «hago más», pídele cuánto y en qué condición."),
    reinforce="Escribe dos programas de ejemplo para componentes distintos y marca en cada uno la regla de progresión y el descanso.",
    extend="Explica por qué la progresión gradual cuida el cuerpo mejor que un programa de moda con resultados rápidos.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 11 (sesión de ejemplo, inventada, de un circuito para un curso; con docente cerca, espacio despejado y sin cargas ni saltos). "
     "Calentamiento: 6 minutos. Circuito: 6 estaciones; en cada una, 40 segundos de trabajo y 20 segundos para cambiar de estación; 2 vueltas con 2 minutos de pausa entre vueltas. "
     "Estaciones: 1) marcha en el lugar; 2) sentarse y pararse de una silla estable; 3) apoyos inclinados en la pared; 4) elevación de talones apoyando las manos en la pared; "
     "5) puente acostado boca arriba, con los pies apoyados; 6) estiramiento suave de piernas. Vuelta a la calma: 5 minutos, con respiración tranquila. "
     "Frecuencia de ejemplo del programa: 3 sesiones por semana durante 4 semanas.")
build(
    O3, 3, F,
    use="Aprenderé a implementar un programa de entrenamiento con una sesión bien armada, calculando tiempos y frecuencia, con calentamiento, circuito y vuelta a la calma, y con medidas de seguridad claras.",
    prior=["Sé elegir un programa según el componente.", "Sé calcular minutos de una sesión.", "Sé que hay que detenerse ante dolor o mareo."],
    explain=[
        "Implementar un programa es pasar del plan a la práctica. Una sesión bien armada tiene tres partes: calentamiento, parte principal y vuelta a la calma. En la parte principal un circuito reúne varias estaciones con ejercicios distintos; en cada estación hay un tiempo de trabajo y un tiempo corto para cambiar. Si se repite el circuito, se deja una pausa entre vueltas.",
        "Para implementar bien hay que calcular tiempos: cuánto dura una vuelta, cuánto dura la sesión completa y cuántos minutos suma el programa en total. También hay que asegurar el espacio, las sillas estables apoyadas en la pared, el calzado y el agua a mano. Todos los ejercicios son con el peso del propio cuerpo, sin cargas, sin saltos y sin retener la respiración.",
        "Cada persona trabaja a su ritmo: se adapta una estación si hace falta (por ejemplo, apoyos en la pared en vez de en el suelo) y nadie compara cuánto o cómo lo hace otra persona. Si aparece dolor, mareo o falta de aire inusual, se detiene la sesión y se avisa a una persona adulta.",
    ],
    vocab=[("implementar", "llevar un plan a la práctica"), ("circuito", "serie de estaciones con ejercicios distintos"), ("estación", "lugar donde se hace un ejercicio por un tiempo"), ("vuelta", "recorrido completo por todas las estaciones"), ("vuelta a la calma", "parte final que baja la respiración y el pulso")],
    worked=[
        ("Calcular una vuelta", "Un circuito de ejemplo tiene 4 estaciones con 30 segundos de trabajo y 15 de cambio. ¿Cuántos segundos dura una vuelta?", ["Cada estación suma 30 + 15 = 45 segundos.", "Cuatro estaciones: 4 × 45 segundos."], "180 segundos, o 3 minutos"),
        ("Adaptar una estación", "En una estación de apoyos en el suelo, una persona de ejemplo siente molestia en la muñeca. ¿Qué adaptación segura existe en la ficha?", ["La ficha ofrece apoyos inclinados en la pared, que cargan menos las muñecas.", "Si la molestia continúa, se detiene y se avisa a una persona adulta."], "Cambiar a apoyos inclinados en la pared y avisar si continúa"),
    ],
    mistakes=[("Pasar de una estación a otra sin el tiempo de cambio.", "Sin cambio se acumula cansancio y aumenta el riesgo de caídas.", "Respeta los 20 segundos de cambio y la pausa entre vueltas."),
              ("Agregar saltos o cargas para hacer el circuito más difícil.", "Aumenta el riesgo y no está en el programa.", "Si quieres más desafío, agrega una vuelta de a poco y con la persona docente cerca.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es un circuito?', 'Una serie de estaciones con ejercicios distintos', 'Una carrera larga sin pausas hasta el agotamiento', 'Un juego de equipo con puntos para quienes ganan', 'Un circuito es una serie de estaciones; no es una carrera ni un juego de puntos.'),
        ('abc', '{F} ¿Cuántas estaciones tiene el circuito de la ficha?', '6', '4', '12', 'La ficha enumera seis estaciones numeradas del 1 al 6.'),
        ('abc', '{F} ¿Qué estación de la ficha trabaja la flexibilidad?', 'La 6, estiramiento suave de piernas', 'La 2, sentarse y pararse de la silla', 'La 5, puente acostado boca arriba', 'La estación 6 es el estiramiento suave.'),
        ('=', '{F} ¿Cuántos segundos dura cada estación, contando trabajo y cambio?', '40+20', 'Se suman los segundos de trabajo y los segundos de cambio.', ' segundos'),
        ('=', '{F} ¿Cuántos minutos dura una vuelta completa de las 6 estaciones?', '6*(40+20)/60', 'Se multiplican las seis estaciones por 60 segundos y se pasa a minutos.', ' minutos'),
        ('abc', '{F} ¿Por qué hay una pausa de 2 minutos entre vueltas?', 'Para recuperar el aliento antes de repetir el circuito', 'Para que las personas más rápidas esperen a las demás', 'Para que se complete una evaluación de cuerpo entre vueltas', 'La pausa permite recuperarse y repetir con seguridad.'),
        ('=', '{F} ¿Cuántos minutos dura la sesión completa, con calentamiento, 2 vueltas con una pausa entre ellas y vuelta a la calma?', '6+2*6+2+5', 'Se suman calentamiento, dos vueltas de 6 minutos, la pausa de 2 minutos y la vuelta a la calma.', ' minutos'),
        ('abc', '{F} Con la frecuencia de ejemplo, ¿cuántas sesiones tiene el programa de 4 semanas?', '12', '7', '16', 'Tres sesiones por semana durante 4 semanas dan 12 sesiones.'),
        ('=', '{F} Si el programa se hace con la sesión completa de la ficha, ¿cuántos minutos suma en las 4 semanas con 3 sesiones por semana?', '4*3*(6+2*6+2+5)', 'Cada sesión dura 25 minutos y hay 12 sesiones en total.', ' minutos'),
        ('abc', '{F} Una persona siente cansancio fuerte en la segunda vuelta. ¿Qué decisión es más segura?', 'Reducir el ritmo, descansar y adaptar o detener la vuelta si hace falta', 'Acelerar para terminar más pronto y descansar recién al final del circuito', 'Agregar saltos para activar más el cuerpo y no sentir tanto cansancio', 'Ante cansancio fuerte se baja el ritmo y se adapta; no se aumenta el esfuerzo.'),
        ('abc', 'Un compañero comenta en voz alta que otro estudiante «hace las sentadillas mal y tiene un cuerpo raro». ¿Qué corresponde?', 'Pedirle que no comente cuerpos y, si se repite, avisar al docente', 'Reírse con él, para que no vuelva a molestar a nadie más del grupo', 'Hacer una lista pública de quién hace bien y quién hace mal cada ejercicio', 'Las observaciones sobre cuerpos faltan el respeto; se corrige y se avisa a un adulto si continúa.'),
        ('abc', 'Dos estudiantes proponen mejorar el circuito. Pía: agregar una vuelta de a poco, con el docente cerca. Rafa: sumar saltos y mochilas con libros para más esfuerzo. ¿Qué propuesta respeta el programa?', 'La de Pía, porque cambia una condición de a poco y sin cargas ni saltos', 'La de Rafa, porque más esfuerzo siempre es mejor para el cuerpo y la salud', 'Las dos, porque ambas buscan más desafío en el circuito de la sesión', 'Sin cargas ni saltos y con cambios graduales; la propuesta de Rafa rompe esas reglas.'),
        ('abc', 'Antes de comenzar el circuito, una persona de ejemplo se da cuenta de que la silla se mueve. ¿Qué hace?', 'Detener la actividad, apoyarla contra la pared o cambiarla por otra estable', 'Usarla igual y sentarse con cuidado más despacio para no empujarla de lugar', 'Reemplazarla por una caja de cartón del salón que esté disponible en el momento', 'Una silla inestable es riesgo de caída; se corrige antes de empezar.'),
    ],
    ctx=('abc', 'Marcelo quiere armar una sesión de 25 minutos con calentamiento de 5, vuelta a la calma de 5 y circuito de estaciones de 30 segundos de trabajo y 15 de cambio en el tiempo restante, sin pausas. ¿Cuántas estaciones caben?', '20 estaciones, porque quedan 15 minutos y cada estación dura 45 segundos', '15 estaciones, porque quedan 15 minutos y cada estación dura 1 minuto', '30 estaciones, porque solo se cuenta el tiempo de trabajo de 30 segundos', 'Quedan 15 minutos, es decir 900 segundos; divididos por 45 segundos dan 20.'),
    sc=[
        ("En Educación Física: ¿qué tres partes tiene una sesión bien armada?", "Calentamiento, parte principal y vuelta a la calma", "Cada parte cumple una función de preparación, trabajo o recuperación."),
        ("¿Qué ejercicios se usan en el circuito de la ficha?", "Ejercicios con el peso del propio cuerpo, sin cargas ni saltos", "Así se cuida la seguridad de todas las personas."),
        ("¿Qué se hace ante dolor, mareo o falta de aire inusual?", "Detener la sesión y avisar a una persona adulta", "Son señales de detención y no deben ignorarse."),
    ],
    op=("Arma una sesión de circuito para tu curso con 5 estaciones. Elige ejercicios con el peso del cuerpo, define el tiempo de trabajo y de cambio, el calentamiento y la vuelta a la calma, y calcula cuánto dura la sesión. Anota una adaptación para una persona con una molestia leve y una regla de seguridad.",
        "Calentamiento 5 min. 5 estaciones de 30 s de trabajo y 15 s de cambio: marcha, sentarse y pararse, apoyos en la pared, puente y estiramiento. Una vuelta: 5 × 45 s = 225 s, casi 4 minutos. Vuelta a la calma 5 min. Total aproximado: 14 minutos. Adaptación: apoyos en la pared si hay molestia en la muñeca; si continúa, detenerse y avisar.",
        ["ejercicios con el peso del cuerpo y sin saltos", "tiempos calculados correctamente", "una adaptación y una regla de seguridad"],
        ["sesión de circuito con cálculo de tiempo y seguridad"],
        ["no calcular el tiempo", "agregar cargas o saltos", "no considerar una adaptación"],
        "Pregunta: «¿cuántos segundos dura una vuelta y cómo lo calculaste?». Si no puede, pídele multiplicar estaciones por trabajo más cambio."),
    reinforce="Con la ficha, calcula la duración de una vuelta si cambias el trabajo a 30 segundos y el cambio a 15 segundos. No practiques sin docente cerca.",
    extend="Explica por qué cada estación del circuito necesita un tiempo de cambio y por qué no se agregan cargas ni saltos.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 12 (registro de ejemplo, inventado, de Elías, tras un programa de 4 semanas). Las pruebas se repitieron con las mismas condiciones. "
     "Semana 0, línea de base: caminata de 6 minutos, 500 metros; silla en 30 segundos, 10 repeticiones; alcance, a 6 centímetros de la punta de los pies. "
     "Semana 4: caminata de 6 minutos, 550 metros (ese día hacía calor); silla en 30 segundos, 14 repeticiones; alcance, a 3 centímetros de la punta de los pies. "
     "Asistencia: 11 de 12 sesiones planificadas; una sesión se suspendió por un resfrío. "
     "Composición corporal: no se midió; si surgen dudas sobre este tema, se consulta a un profesional de la salud. "
     "Regla: un cambio pequeño puede deberse a cómo amaneció la persona ese día; se interpreta con cuidado.")
build(
    O3, 4, F,
    use="Aprenderé a registrar y comparar los resultados de un programa de entrenamiento con la línea de base, a calcular cambios y a decidir un ajuste sin comparar personas ni cuerpos.",
    prior=["Sé qué es una línea de base.", "Sé armar una sesión de circuito.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Registrar es anotar los resultados de las pruebas y la asistencia a las sesiones. Para saber si un programa produjo cambios se compara el resultado actual con la línea de base, calculando la diferencia y, cuando conviene, el porcentaje de cambio. Si la caminata subió de 500 a 550 metros, la diferencia es 50 metros y equivale a un 10 % más.",
        "Hay que interpretar con cuidado. Un cambio pequeño puede deberse a cómo amaneció la persona, al clima o al sueño, y no solo al programa. Por eso se anotan las condiciones de cada prueba y se piensa en qué otras cosas pudieron influir. También se registra la asistencia: un programa con muchas sesiones perdidas se interpreta distinto.",
        "La regulación es decidir un ajuste a partir del registro: mantener el programa si se avanza con seguridad, bajar la carga si hubo cansancio fuerte o consultar a un profesional si hay dolor o dudas. Los resultados son privados, se comparan solo con la propia línea de base y nunca se usan para opinar sobre cuerpos.",
    ],
    vocab=[("diferencia", "resultado actual menos línea de base"), ("porcentaje de cambio", "diferencia dividida por la línea de base, por 100"), ("asistencia", "sesiones realizadas sobre sesiones planificadas"), ("condiciones de prueba", "lugar, hora, clima y estado de ánimo al medir"), ("ajuste", "cambio pequeño al programa a partir del registro")],
    worked=[
        ("Calcular una diferencia y un porcentaje", "Una persona de ejemplo pasa de 8 a 10 repeticiones en la prueba de la silla. ¿Cuántas más y qué porcentaje de cambio?", ["Diferencia: 10 − 8 = 2 repeticiones.", "Porcentaje: 2 dividido por 8 y por 100 es 25 %."], "2 repeticiones más, un 25 % de aumento"),
        ("Interpretar con cuidado", "Una persona de ejemplo mejoró en la caminata, pero esa vez hacía mucho calor y la primera vez no. ¿Qué se anota?", ["Se anota la diferencia de condiciones: calor.", "Se dice que el cambio puede deberse en parte al clima y se repite la prueba en condiciones parecidas."], "Anotar el calor y repetir la prueba en condiciones parecidas"),
    ],
    mistakes=[("Afirmar que el programa causó todo el cambio sin mirar las condiciones.", "El clima o el estado del día también influyen.", "Anota las condiciones y di «puede deberse en parte»."),
              ("Comparar el cambio propio con el de otra persona.", "Cada línea de base y cada historia es distinta.", "Compara solo con tu propia línea de base.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es la asistencia a un programa?', 'Las sesiones realizadas respecto de las planificadas', 'La cantidad de personas que miran una sesión de práctica', 'El nivel de esfuerzo más alto que se alcanzó en toda la sesión', 'La asistencia compara sesiones hechas con sesiones planificadas.'),
        ('abc', '{F} ¿Cuál fue la línea de base de Elías en la prueba de la silla?', '10 repeticiones', '14 repeticiones', '6 repeticiones', 'La ficha indica 10 repeticiones en la semana 0.'),
        ('abc', '{F} ¿Por qué se anota que el día de la prueba final hacía calor?', 'Porque una condición distinta puede influir en el resultado', 'Porque el calor siempre mejora el rendimiento', 'Porque solo se anotan las condiciones cuando el resultado empeora', 'El clima es una condición que pudo influir en la caminata.'),
        ('=', '{F} ¿Cuántos metros más caminó Elías en la semana 4 que en su línea de base?', '550-500', 'Se resta la distancia de la línea de base de la distancia de la semana 4.', ' metros'),
        ('=', '{F} ¿Qué porcentaje de aumento tuvo la caminata respecto de su línea de base?', '(550-500)/500*100', 'Se divide la diferencia por la línea de base y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Qué porcentaje de aumento tuvo la prueba de la silla respecto de su línea de base?', '(14-10)/10*100', 'La diferencia de 4 repeticiones se divide por 10 y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Cuántos centímetros más cerca de la punta de los pies llegó Elías en la semana 4?', '6-3', 'Una distancia menor a la punta de los pies es una mejora; se resta 3 de 6.', ' centímetros'),
        ('=', '{F} ¿Cuántas de las sesiones planificadas no realizó Elías?', '12-11', 'Se restan las sesiones realizadas de las 12 planificadas.', ' sesión'),
        ('abc', '{F} ¿Qué conclusión sobre su caminata es más prudente?', 'Mejoró, pero el calor de ese día invita a repetir la prueba en condiciones parecidas', 'Quedó demostrado que el programa mejora la caminata de todas las personas por igual', 'Los datos no sirven para nada porque la prueba se midió una sola vez al final', 'Con una persona y condiciones distintas se interpreta con cuidado, no se generaliza.'),
        ('abc', 'Ana anota: «mejoré 2 repeticiones». Bruno anota: «de 8 a 10 repeticiones, mismas condiciones, 11 de 12 sesiones». ¿Qué registro permite ajustar mejor el programa?', 'El de Bruno, porque da línea de base, condiciones y asistencia', 'El de Ana, porque es más corto y muy fácil de recordar al día siguiente', 'Los dos igual, porque ambos reconocen que hubo una mejora en el resultado', 'Un registro útil incluye punto de partida, condiciones y asistencia.'),
        ('abc', 'Dos estudiantes tienen un aumento de 10 % en la caminata. Una tuvo 12 de 12 sesiones y otra 6 de 12. ¿Qué interpretación es más cuidadosa?', 'Son aumentos iguales, pero la asistencia distinta cambia cómo se explica cada resultado', 'Son iguales en todo sentido, porque el porcentaje de aumento es exactamente el mismo', 'La que asistió menos mejoró más, porque se esforzó en cada una de sus pocas sesiones', 'El mismo porcentaje no significa lo mismo con distinta asistencia.'),
        ('abc', 'Un grupo propone publicar los porcentajes de mejora de todo el curso en un ranking. ¿Qué corresponde?', 'No publicarlo y compartir, si se desea, resultados del curso sin nombres', 'Publicarlo, porque la competencia motiva por igual a todas las personas del curso', 'Publicar solo los nombres de quienes mejoraron más para felicitarlos frente al curso', 'Los resultados son privados; la comparación útil es con la propia línea de base.'),
        ('abc', 'Tras el programa, una estudiante de ejemplo pregunta si debería cambiar su cuerpo para «verse saludable». ¿Qué respuesta es más adecuada?', 'Que la salud no es una apariencia y que sus dudas las converse con un profesional', 'Que debe seguir otro programa más fuerte hasta lograr el cuerpo que describe en su duda', 'Que mida su cuerpo cada semana y anote las cifras en la bitácora del programa', 'La salud no depende de la apariencia; las dudas del cuerpo se consultan a un profesional.'),
    ],
    ctx=('abc', 'Camilo registra en 4 semanas: caminata de 400 a 440 metros, silla de 8 a 8 repeticiones, alcance sin cambios, y asistió a 12 de 12 sesiones. ¿Qué ajuste de una sola condición es más coherente?', 'Mantener la caminata, y agregar de a poco series de fuerza con apoyo del docente', 'Cambiar todo el programa por uno más intenso y agotador, para ver si mejora más', 'Suspender el programa completo, porque mejoró solo en una de las tres pruebas', 'La caminata mejoró y la fuerza no cambió: se ajusta fuerza, de a poco.'),
    sc=[
        ("En Educación Física: ¿con qué se comparan los resultados de una persona al evaluar un programa?", "Con su propia línea de base", "La comparación con otras personas no tiene sentido ni respeto."),
        ("¿Qué se anota junto al resultado de cada prueba?", "Las condiciones, como clima y lugar", "Las condiciones ayudan a interpretar el resultado."),
        ("¿A quién se consultan dudas sobre el cuerpo?", "A un profesional de la salud", "El curso no evalúa ni mide cuerpos."),
    ],
    op=("Inventa los resultados de una persona en 4 semanas de programa para las tres pruebas de la ficha (caminata, silla y alcance). Calcula la diferencia de cada una, el porcentaje de cambio de una de ellas y la asistencia. Escribe una frase que explique el resultado con cuidado y un ajuste de una sola condición.",
        "Caminata: 480 a 528 m, diferencia 48, 10 %. Silla: 9 a 12, diferencia 3. Alcance: 8 a 5 cm de los pies, 3 cm más cerca. Asistencia 10 de 12. Frase: «Se observó que mejoró; pudo influir el clima». Ajuste: agregar 5 minutos a la caminata la semana siguiente.",
        ["diferencias y un porcentaje bien calculados", "asistencia calculada", "una frase con cuidado y un ajuste de una condición"],
        ["registro de cuatro semanas con cálculos y un ajuste"],
        ["afirmar una causa segura", "cambiar varias condiciones a la vez", "comparar con otra persona"],
        "Pregunta: «¿cómo calculaste el porcentaje y qué otra cosa pudo influir?». Si no sabe, pídele diferencia sobre línea de base."),
    reinforce="Con tres resultados inventados de una prueba, calcula la diferencia y el porcentaje de cambio. No uses datos de personas reales.",
    extend="Explica por qué un cambio pequeño entre dos pruebas puede no ser prueba suficiente de que el programa funcionó.",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 13 (indicadores de ejemplo, inventados, para evaluar un programa de «recreos activos» en un curso ficticio). Un indicador es un dato que se puede anotar siempre de la misma forma. "
     "I1: horas de sueño por noche (número, anotado en la bitácora personal). I2: energía en la tarde (1 a 5). I3: ánimo del día (1 a 5). I4: minutos moderados a vigorosos por día. "
     "I5: cantidad de recreos de la semana en que cada estudiante jugó con otras personas (0 a 5). I6: sensación de pertenencia al curso (1 a 5). I7: participación en actividades del curso (veces por mes). "
     "I8: «cómo se ve el cuerpo de cada estudiante» (propuesta rechazada por el curso, porque no mide la salud ni el bienestar y expone a las personas). "
     "Impacto personal: cambios en el bienestar de cada persona (I1 a I4). Impacto social: cambios en las relaciones y la participación del grupo (I5 a I7).")
build(
    O4, 1, F,
    use="Aprenderé a diagnosticar, de forma privada y segura, qué cambios del bienestar personal y social se pueden evaluar después de practicar ejercicio, eligiendo indicadores claros y rechazando los que exponen a las personas.",
    prior=["Sé nombrar beneficios por dimensión.", "Sé llevar una bitácora con escala de 1 a 5.", "Sé que la salud no es una apariencia."],
    explain=[
        "Evaluar el impacto del ejercicio es mirar qué cambios se observan en las personas y en el grupo después de practicar durante un tiempo. El bienestar tiene una parte personal (el sueño, la energía, el ánimo y la actividad de cada quien) y una parte social (las relaciones, la pertenencia y la participación en el curso). El impacto puede ser personal, social o ambos.",
        "Para evaluarlo se necesitan indicadores: datos que se anotan siempre de la misma forma, como una escala de 1 a 5, un conteo de veces o una cantidad de minutos. Un buen indicador es observable, repetible y respetuoso: no pide nombres ni datos del cuerpo, y se puede registrar de manera anónima cuando es del curso. «Cómo se ve el cuerpo» no es un indicador válido: no mide salud y expone a las personas.",
        "El diagnóstico previo, antes de empezar un programa, sirve para saber desde dónde se parte. Se hace en privado y los resultados se comparan después con ese punto de partida, nunca para ordenar personas. Si un indicador revela que alguien se siente muy mal, la respuesta es avisar a una persona adulta de confianza o a un profesional.",
    ],
    vocab=[("impacto", "cambio observado en personas o grupo después de una acción"), ("indicador", "dato que se anota siempre de la misma forma"), ("bienestar personal", "cómo se siente cada persona: sueño, energía y ánimo"), ("bienestar social", "relaciones, pertenencia y participación en el grupo"), ("anónimo", "sin nombre de quien responde")],
    worked=[
        ("Clasificar un indicador", "¿El indicador «cantidad de actividades del curso a las que asistió esta persona este mes» es personal o social?", ["Mide participación en el grupo, no solo cómo se siente una persona.", "Pertenece al bienestar social."], "Social"),
        ("Rechazar un indicador", "Un compañero propone medir «cuántos centímetros mide la cintura de cada estudiante». ¿Se acepta?", ["No mide salud ni bienestar y expone a las personas.", "Se reemplaza por un indicador respetuoso, como la energía de 1 a 5."], "No se acepta; se usa un indicador como la energía de 1 a 5"),
    ],
    mistakes=[("Proponer un indicador sobre cómo se ve el cuerpo.", "No mide la salud y daña la convivencia.", "Elige datos de conducta, ánimo, energía o participación."),
              ("Usar indicadores distintos cada vez que se mide.", "No se pueden comparar los cambios en el tiempo.", "Anota siempre lo mismo y de la misma forma.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es un indicador?', 'Un dato que se puede anotar siempre de la misma forma', 'Una opinión que cambia según cada persona que responde', 'El nombre de la persona que lidera la actividad', 'Un indicador es un dato repetible; una opinión suelta no se puede comparar.'),
        ('abc', '{F} ¿Qué indicador mide el bienestar social?', 'I5, los recreos en que jugó con otras personas', 'I1, las horas de sueño por noche anotadas en la bitácora', 'I4, los minutos moderados a vigorosos de cada día de la semana', 'I5 describe relaciones con otras personas, que es dimensión social.'),
        ('abc', '{F} ¿Qué indicador mide el bienestar personal?', 'I3, el ánimo del día', 'I7, la participación en actividades del curso', 'I6, la pertenencia al curso', 'I3 refleja cómo se siente cada persona, lo que es bienestar personal.'),
        ('abc', '{F} ¿Por qué el curso rechazó I8?', 'Porque no mide la salud ni el bienestar y expone a las personas', 'Porque no se puede anotar con una escala de 1 a 5', 'Porque es un indicador que sirve solo para el bienestar social y no para el personal', 'La apariencia del cuerpo no mide salud y expone; por eso se rechaza.'),
        ('abc', '¿Por qué la encuesta de un curso es anónima?', 'Para que cada persona responda con libertad y sin exponerse', 'Para que el docente no pueda leer los resultados de ningún estudiante', 'Para que luego se pueda saber quién respondió cada cosa y corregir sus respuestas', 'El anonimato protege a quien responde y permite respuestas más honestas.'),
        ('abc', '{F} ¿Qué diferencia hay entre impacto personal e impacto social?', 'El personal habla de cambios en cada persona; el social, de relaciones del grupo', 'El personal sirve solo para quienes practican y el social solo para quienes no practican', 'El personal siempre se mide con minutos y el social siempre se mide con horas', 'La ficha separa el cambio en cada persona del cambio en el grupo.'),
        ('=', '{F} Una estudiante anota energía de 3, 4, 2, 5 y 1 en cinco tardes (I2). ¿Cuál fue el promedio?', '(3+4+2+5+1)/5', 'Se suman los cinco valores y se dividen por cinco.', ''),
        ('abc', '{F} Un curso decide medir tres indicadores: I2, I6 y I7. ¿Qué mezcla de bienestar cubre?', 'Personal y social', 'Solo personal', 'Solo social', 'I2 es personal; I6 e I7 son sociales.'),
        ('=', '{F} En la bitácora de ejemplo, una persona duerme 7, 8, 6, 7, 7, 8 y 9 horas en una semana (I1). ¿Cuántas horas durmió en total?', '7+8+6+7+7+8+9', 'Se suman las horas de las siete noches.', ' horas'),
        ('abc', 'Dos estudiantes proponen indicadores. Ana: «cuánto se sienten parte del curso, de 1 a 5». Bruno: «quién se ve más saludable». ¿Cuál indicador es válido?', 'El de Ana, porque es una escala observable y respetuosa', 'El de Bruno, porque es lo que se nota a simple vista', 'Los dos, porque ambos se refieren a la salud', 'La pertenencia se mide con escala; el aspecto físico no mide la salud.'),
        ('abc', 'Un curso propone medir cuántos kilos baja cada estudiante con el programa. ¿Qué respuesta corresponde?', 'No usarlo: no mide bienestar y expone; elegir energía, ánimo o participación', 'Usarlo, porque es el dato más objetivo que existe para evaluar un programa', 'Usarlo, pero solo con quienes quieran bajar de peso y lo pidan en voz alta', 'El peso no mide bienestar y su comparación daña; se reemplaza.'),
        ('abc', '{F} Un estudiante de ejemplo anota en el indicador I3 un ánimo de 1 durante muchos días seguidos. ¿Qué corresponde?', 'Contárselo a una persona adulta de confianza o a un profesional', 'Anotar un número más alto para que su curso no note cómo se siente', 'Esperar a que el ánimo suba solo con más minutos de ejercicio', 'Un ánimo muy bajo y sostenido se conversa con un adulto; el registro no reemplaza esa ayuda.'),
        ('abc', 'Alguien propone que la bitácora de cada estudiante se lea en voz alta para comparar. ¿Qué respuesta corresponde?', 'Mantenerla privada y compartir solo datos del curso sin nombres', 'Leerla en voz alta, porque comparar entre estudiantes ayuda a mejorar a todos', 'Leer solo las bitácoras con mejores resultados para motivar al resto del curso', 'Los datos personales son privados; se comparte lo general y sin nombres.'),
    ],
    ctx=('abc', 'Un curso ficticio quiere evaluar su programa de recreos activos durante 6 semanas. ¿Qué conjunto de indicadores es más completo y respetuoso?', 'Ánimo de 1 a 5, minutos moderados a vigorosos por día y recreos jugados con otras personas', 'Cómo se ve el cuerpo de cada estudiante antes y después de las seis semanas del programa', 'Solo la cantidad de estudiantes que dicen que el programa «estuvo bien» al final del periodo', 'Cubre bienestar personal y social con datos respetuosos y repetibles.'),
    sc=[
        ("En Educación Física: ¿qué es un indicador?", "Un dato que se anota siempre de la misma forma", "Anotar igual permite comparar cambios en el tiempo."),
        ("¿Qué tipo de bienestar mide la pertenencia al curso?", "El bienestar social", "Describe la relación con el grupo."),
        ("¿Qué indicador no se usa porque expone a las personas?", "Cómo se ve el cuerpo de cada estudiante", "No mide salud ni bienestar y daña la convivencia."),
    ],
    op=("Elige un programa de ejemplo (recreos activos, caminata semanal o un baile de curso) y propone cuatro indicadores: dos de bienestar personal y dos de bienestar social. Para cada uno escribe cómo se anota (escala, conteo o minutos) y cada cuánto. Agrega una razón por la que descartaste un indicador sobre el cuerpo.",
        "Programa: caminata semanal de curso. Personal: energía de 1 a 5 cada tarde; minutos moderados a vigorosos por día. Social: veces por mes que participó en una actividad del curso; pertenencia de 1 a 5 una vez por semana. Descarté «cómo se ve el cuerpo» porque no mide salud y expone.",
        ["dos indicadores personales y dos sociales", "cómo se anota cada uno y cada cuánto", "razón para descartar un indicador sobre el cuerpo"],
        ["cuatro indicadores con forma de registro y una razón de descarte"],
        ["proponer datos del cuerpo", "no decir cómo se anota", "pedir nombres a quienes responden"],
        "Pregunta: «¿cómo anotarías ese indicador siempre igual?». Si responde «según el día», pídele una escala o un conteo."),
    reinforce="Escribe cinco indicadores posibles para un programa de actividad física y marca cuáles son personales y cuáles sociales. Descarta los que expongan a alguien.",
    extend="Explica por qué un buen indicador debe ser repetible y respetuoso, y da un ejemplo que no lo sea.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 14 (preguntas candidatas de ejemplo, inventadas, para una encuesta sobre un programa de recreos activos). "
     "Q1: «¿Cómo fue tu ánimo hoy? (1 a 5)». Q2: «¿No es cierto que el programa fue genial?». Q3: «¿En cuántos recreos de esta semana jugaste con otras personas? (0 a 5)». "
     "Q4: «Escribe el nombre de quien menos se mueve en tu curso». Q5: «¿Te sentiste parte del curso esta semana? (1 a 5)». "
     "Reglas de una buena encuesta: máximo 5 preguntas; las mismas preguntas antes y después; respuesta anónima; preguntas neutrales (no inducen la respuesta); sin nombres ni datos del cuerpo. "
     "Otros instrumentos: bitácora personal (1 a 5 cada noche) y observación del recreo, contando cuántas personas juegan durante 10 minutos, en 3 días y a la misma hora.")
build(
    O4, 2, F,
    use="Aprenderé a elegir un instrumento para evaluar el impacto del ejercicio (encuesta anónima, bitácora u observación del recreo) y a revisar preguntas con reglas de respeto, neutralidad y repetibilidad.",
    prior=["Sé qué es un indicador.", "Sé la diferencia entre bienestar personal y social.", "Sé que algunos datos son privados."],
    explain=[
        "Un instrumento es la herramienta con la que se recogen datos. La encuesta anónima sirve para saber cómo se siente un grupo; la bitácora personal registra la evolución de una persona; la observación del recreo cuenta lo que ocurre en el patio, sin nombres. Cada instrumento responde algo distinto: ninguno lo mide todo.",
        "Una buena encuesta cumple reglas: es breve (como máximo 5 preguntas), repite las mismas preguntas antes y después, es anónima, usa preguntas neutrales y no pide nombres ni datos del cuerpo. Una pregunta que induce la respuesta, como «¿no es cierto que fue genial?», no sirve porque empuja a decir que sí. Una pregunta que pide el nombre de quien menos se mueve expone a una persona y es irrespetuosa.",
        "Elegir un instrumento es mirar qué impacto se quiere evaluar y qué datos lo muestran: el ánimo se mide con una escala, la participación con un conteo, la pertenencia con una escala. Después se decide cuándo y con quién se aplicará, y cómo se cuidará la privacidad.",
    ],
    vocab=[("instrumento", "herramienta con la que se recogen datos"), ("encuesta", "serie corta de preguntas contestadas por un grupo"), ("pregunta neutral", "pregunta que no empuja una respuesta"), ("observación", "registro de lo que ocurre sin intervenir"), ("repetible", "que se puede aplicar igual antes y después")],
    worked=[
        ("Revisar una pregunta", "Revisa «¿Verdad que fue un programa muy divertido?» con las reglas de la ficha.", ["Empuja a contestar que sí: no es neutral.", "Una versión neutral sería: «¿Qué tan entretenido fue el programa? (1 a 5)»."], "No es neutral; se reescribe con una escala de 1 a 5"),
        ("Elegir un instrumento", "Un curso quiere saber cuántas personas juegan en el recreo, sin pedirles nada. ¿Qué instrumento es adecuado?", ["No necesita preguntas; solo contar lo que ocurre en el patio.", "La observación del recreo cumple y no expone a nadie."], "Observación del recreo"),
    ],
    mistakes=[("Hacer una encuesta con 15 preguntas y nombres.", "Cansa a quien responde, y los nombres exponen a las personas.", "Máximo 5 preguntas y anónima."),
              ("Cambiar las preguntas de la encuesta final.", "No se puede comparar con el antes.", "Repite las mismas preguntas, en el mismo orden.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es una pregunta neutral?', 'Una pregunta que no empuja a una respuesta determinada', 'Una pregunta que se contesta siempre con sí o con no', 'Una pregunta que solo puede responder el docente a cargo', 'Una pregunta neutral deja libre la respuesta.'),
        ('abc', '{F} ¿Cuál es la pregunta que induce la respuesta?', 'Q2, «¿No es cierto que el programa fue genial?»', 'Q1, la pregunta de ánimo del día con una escala de 1 a 5', 'Q3, la pregunta de recreos jugados con otras personas esa semana', 'Q2 empuja a decir que sí y por eso no es neutral.'),
        ('abc', '{F} ¿Por qué se descarta Q4?', 'Porque pide el nombre de una persona y la expone', 'Porque se contesta con un número del 1 al 5', 'Porque se repite antes y después del programa', 'Pedir el nombre de quien menos se mueve es irrespetuoso y expone.'),
        ('abc', '{F} ¿Qué preguntas de la ficha cumplen todas las reglas de una buena encuesta?', 'Q1, Q3 y Q5', 'Q1, Q2 y Q3', 'Q3, Q4 y Q5', 'Q2 induce y Q4 expone; las otras tres son neutrales, anónimas y repetibles.'),
        ('abc', '{F} ¿Qué instrumento sirve para contar cuántas personas juegan en el recreo sin preguntarles nada?', 'La observación del recreo', 'La encuesta con nombres', 'La bitácora personal', 'La observación cuenta lo que ocurre sin pedir datos a nadie.'),
        ('abc', '¿Por qué la encuesta final repite las mismas preguntas que la inicial?', 'Para poder comparar los resultados del antes y del después', 'Para que las personas no tengan que pensar respuestas nuevas', 'Para que la encuesta final dure más tiempo', 'Solo preguntas iguales permiten comparar cambios.'),
        ('=', '{F} Una encuesta de ejemplo tiene 5 preguntas de 1 a 5. Si una persona responde 4, 3, 5, 4 y 4, ¿cuál es el promedio de sus respuestas?', '(4+3+5+4+4)/5', 'Se suman las cinco respuestas, que dan 20, y se dividen por cinco.', ''),
        ('abc', '{F} Un curso quiere saber si las personas se sienten más parte del grupo. ¿Qué pregunta de la ficha sirve?', 'Q5, de pertenencia de 1 a 5', 'Q1, de ánimo de 1 a 5', 'Q3, de recreos con otras personas', 'Q5 pregunta de forma directa por la pertenencia al curso.'),
        ('=', '{F} En la observación del recreo se cuentan 12, 15 y 18 personas jugando en 3 días a la misma hora. ¿Cuál es el promedio?', '(12+15+18)/3', 'Se suman los tres conteos y se dividen por tres.', ' personas'),
        ('abc', 'Dos encuestas de ejemplo: la A tiene 4 preguntas anónimas de 1 a 5; la B tiene 14 preguntas con espacio para nombre. ¿Cuál cumple mejor las reglas?', 'La A, porque es breve y anónima', 'La B, porque recoge más información de cada persona', 'Las dos, porque ambas buscan conocer al curso', 'La breve y anónima cumple las reglas; la larga cansa y expone.'),
        ('abc', 'Un grupo cambia en la encuesta final la escala de 1 a 5 por una de 1 a 10. ¿Qué problema trae?', 'Los datos del antes y del después ya no se pueden comparar de forma directa', 'La encuesta final se vuelve más corta y menos clara para quienes la responden', 'Las personas ya no pueden responder de forma anónima, porque cambia la escala', 'Cambiar la escala impide comparar con la medición inicial.'),
        ('abc', 'Una estudiante de ejemplo escribe en la encuesta anónima: «a veces me excluyen en el recreo y me da vergüenza». ¿Qué corresponde al equipo del curso?', 'Avisar a una persona adulta de confianza, sin buscar quién escribió', 'Preguntar en voz alta quién escribió eso para poder conversar con la persona', 'Ignorarlo, porque la encuesta solo cuenta números y no sirve para otra cosa', 'La exclusión se comunica a un adulto; la encuesta es anónima y no se identifica a nadie.'),
        ('abc', 'Alguien propone aplicar la encuesta solo a quienes participaron en el programa. ¿Qué problema trae?', 'Mostraría solo la opinión de quienes ya estaban motivadas, no la del curso completo', 'Haría la encuesta demasiado corta y rápida de aplicar para el tiempo disponible', 'Impediría que las respuestas sean anónimas, porque se sabría quiénes participaron', 'Responden solo quienes participaron; el resultado queda sesgado hacia lo positivo.'),
    ],
    ctx=('abc', 'Un curso ficticio quiere saber si el programa de recreos activos mejoró el ánimo y la participación. Tiene poco tiempo. ¿Qué plan de instrumentos es el más adecuado?', 'Encuesta anónima de 4 preguntas antes y después, y observación del recreo con conteo', 'Una entrevista pública a cada estudiante frente a todos los compañeros del curso', 'Una lista con los nombres de quienes se mueven más y de quienes se mueven menos', 'Combina una encuesta anónima y breve con una observación que no expone a nadie.'),
    sc=[
        ("En Educación Física: ¿cuántas preguntas como máximo debe tener la encuesta de la ficha?", "Cinco", "Una encuesta breve se contesta con atención."),
        ("¿Qué se hace con las preguntas de la encuesta final respecto de la inicial?", "Se repiten iguales", "Así se puede comparar el antes y el después."),
        ("¿Qué no debe pedir nunca una encuesta de curso sobre una persona?", "Su nombre ni datos de su cuerpo", "Protege la privacidad y evita exponer."),
    ],
    op=("Diseña una encuesta anónima de 4 preguntas para evaluar el impacto de un programa de actividad física en tu curso. Escribe cada pregunta con su escala, indica cuál mide bienestar personal y cuál social y escribe una pregunta que tuviste que descartar y por qué. Agrega cuándo la aplicarías.",
        "1) Ánimo del día (1 a 5): personal. 2) Energía en la tarde (1 a 5): personal. 3) Recreos de la semana en que jugaste con otras personas (0 a 5): social. 4) Te sentiste parte del curso (1 a 5): social. Descarté «¿verdad que el programa fue genial?» porque induce. Se aplica el primer lunes y de nuevo a las 6 semanas.",
        ["cuatro preguntas neutrales con escala", "clasificación personal o social", "una pregunta descartada con razón y los momentos de aplicación"],
        ["encuesta anónima de cuatro preguntas con descarte justificado"],
        ["preguntas que inducen la respuesta", "pedir nombres o datos del cuerpo", "cambiar la escala entre antes y después"],
        "Pregunta: «¿qué regla cumple cada pregunta tuya?». Si dice «ninguna», pídele que la revise con la ficha."),
    reinforce="Revisa cinco preguntas de una encuesta de ejemplo con las reglas de la ficha y marca cuáles hay que cambiar.",
    extend="Explica por qué una pregunta que induce la respuesta no sirve para evaluar el impacto de un programa.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 15 (resultados de ejemplo, inventados, de la encuesta anónima de un curso ficticio de 50 estudiantes; contestaron las dos encuestas 40 de ellos, antes y después de 6 semanas de recreos activos). "
     "Ánimo de 4 o 5: antes, 14 estudiantes; después, 22. "
     "Jugó con otras personas en 3 o más recreos de la semana: antes, 10; después, 26. "
     "Se sintió parte del curso (4 o 5): antes, 18; después, 24. "
     "Observación: durante esas semanas hubo una salida pedagógica y un paseo de curso.")
build(
    O4, 3, F,
    use="Aprenderé a aplicar el análisis de una encuesta del curso, calculando porcentajes y cambios en puntos porcentuales, para evaluar el impacto personal y social de un programa de actividad física.",
    prior=["Sé qué es un indicador.", "Sé que la encuesta es anónima y repetible.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Para evaluar el impacto con una encuesta se comparan los resultados del antes con los del después, siempre con las mismas preguntas. Como el número de respuestas puede ser distinto de un grupo a otro, se convierten los conteos a porcentajes: se divide la cantidad que respondió algo entre el total que respondió y se multiplica por 100.",
        "Después se calcula el cambio en puntos porcentuales, que es la resta entre el porcentaje del después y el del antes. Por ejemplo, si el porcentaje pasó de 30 % a 45 %, el cambio es de 15 puntos porcentuales. Esta resta es distinta del «por ciento de aumento», que compara el cambio con el valor inicial; aquí se usa la resta simple.",
        "El resultado se lee con cuidado: indica qué cambió en el curso, pero no prueba por sí solo que el programa fue la causa, porque pudieron influir otros hechos, como una salida o un paseo. Se escribe «se observó que» y se nombran los factores que pudieron influir. Los resultados son del curso, no de personas, y se presentan sin nombres.",
    ],
    vocab=[("porcentaje", "parte de cada 100"), ("punto porcentual", "unidad en que se mide la diferencia entre dos porcentajes"), ("antes y después", "dos mediciones con las mismas preguntas"), ("factor", "hecho que pudo influir en el resultado"), ("conclusión prudente", "frase que dice lo observado sin asegurar la causa")],
    worked=[
        ("Calcular un porcentaje", "En otro curso de ejemplo, 18 de 30 estudiantes que respondieron dicen tener ánimo 4 o 5. ¿Qué porcentaje es?", ["Divide 18 entre 30.", "Multiplica por 100: 60 %."], "60 %"),
        ("Calcular un cambio", "En otro curso de ejemplo, el porcentaje de estudiantes que juega en 3 o más recreos pasó de 20 % a 50 %. ¿Cuántos puntos porcentuales cambió?", ["Resta el porcentaje del antes del porcentaje del después.", "50 − 20 = 30 puntos porcentuales."], "30 puntos porcentuales"),
    ],
    mistakes=[("Comparar solo los conteos sin pasarlos a porcentaje cuando responden números distintos.", "Los grupos pueden ser de tamaños diferentes.", "Convierte a porcentaje antes de comparar."),
              ("Decir «el programa causó el cambio» con una sola encuesta.", "Otros hechos del periodo pudieron influir.", "Usa «se observó que» y nombra otros factores.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es un punto porcentual?', 'La unidad en que se mide la diferencia entre dos porcentajes', 'La cantidad de estudiantes que contestan una encuesta anónima', 'La diferencia entre dos conteos de estudiantes', 'Se usa al restar un porcentaje de otro.'),
        ('=', '{F} ¿Qué porcentaje de las 40 personas que respondieron tenía ánimo de 4 o 5 antes del programa?', '14*100/40', 'Se divide 14 entre 40 y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Qué porcentaje de las 40 personas tenía ánimo de 4 o 5 después del programa?', '22*100/40', 'Se divide 22 entre 40 y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Cuántos puntos porcentuales cambió el ánimo de 4 o 5?', '22*100/40-14*100/40', 'Se resta el porcentaje del antes del porcentaje del después.', ' puntos porcentuales'),
        ('abc', '{F} ¿Por qué se usan porcentajes y no solo conteos para comparar antes y después?', 'Porque permite comparar aunque los grupos cambien de tamaño', 'Porque el porcentaje no necesita conocer el total que respondió', 'Porque los conteos no sirven para ninguna comparación', 'Los porcentajes ajustan por el total que respondió.'),
        ('=', '{F} ¿Cuántos puntos porcentuales subió el porcentaje de estudiantes que jugó con otras personas en 3 o más recreos?', '26*100/40-10*100/40', 'Se calcula 65 % menos 25 %.', ' puntos porcentuales'),
        ('=', '{F} ¿Cuántos puntos porcentuales subió la pertenencia al curso (4 o 5)?', '24*100/40-18*100/40', 'Se calcula 60 % menos 45 %.', ' puntos porcentuales'),
        ('abc', '{F} ¿Qué indicador tuvo el mayor cambio en puntos porcentuales?', 'Jugar con otras personas en 3 o más recreos', 'El ánimo de 4 o 5 que declararon las personas', 'La pertenencia al curso de 4 o 5 de ese grupo', 'Subió 40 puntos, frente a 20 del ánimo y 15 de la pertenencia.'),
        ('abc', '{F} ¿Qué conclusión es más prudente sobre el ánimo?', 'Se observó que el porcentaje con ánimo de 4 o 5 subió; otros hechos pudieron influir', 'Quedó demostrado que el programa fue la causa del mejor ánimo de todo el curso', 'No se observó ningún cambio en el ánimo de las personas que respondieron', 'Es prudente decir qué se observó y nombrar otros factores.'),
        ('abc', 'Dos estudiantes: Ana dice que el programa fue un éxito porque «subió el ánimo». Bruno dice que «subió 20 puntos porcentuales el ánimo de 4 o 5, y hubo una salida en esas semanas». ¿Qué conclusión es más completa?', 'La de Bruno, porque entrega el cambio y un factor que puede influir', 'La de Ana, porque resume el resultado en una frase corta y clara para todos', 'Las dos igual, porque ambas dicen que el ánimo del curso subió con el programa', 'Un dato con valor y condiciones es más claro y prudente.'),
        ('abc', 'En un curso de 60 responden 30 y en otro de 20 responden 10, y en ambos el 50 % dice tener ánimo 4 o 5. ¿Qué afirmación es correcta?', 'Los porcentajes son iguales, aunque los conteos sean distintos', 'El primer curso tiene mejor ánimo, porque 30 es mayor que 10', 'El segundo curso tiene mejor ánimo, porque su curso es menor', 'Los porcentajes permiten comparar cursos de distinto tamaño.'),
        ('abc', 'Al presentar los resultados, alguien pide mostrar el ánimo de cada estudiante por nombre. ¿Qué corresponde?', 'Presentar solo resultados del curso, sin nombres', 'Mostrar los nombres, porque así se entiende mejor', 'Mostrar solo los nombres de quienes mejoraron', 'La encuesta es anónima y los resultados son del grupo.'),
        ('=', 'En otra medición de ejemplo, 40 estudiantes responden y el porcentaje con ánimo de 4 o 5 pasa de 35 % a 60 %. ¿Cuántos estudiantes más tienen ánimo de 4 o 5?', '40*60/100-40*35/100', 'Se calculan 24 y 14 estudiantes y se restan.', ' estudiantes'),
    ],
    ctx=('abc', 'El centro de estudiantes de ejemplo lee: antes del programa 12 de 40 dicen sentirse parte del curso (4 o 5) y después 20 de 40. ¿Qué frase informa mejor al curso?', 'Se observó que el porcentaje pasó de 30 % a 50 %, y hubo otras actividades en esas semanas', 'El programa fue un éxito rotundo porque ahora 20 personas se sienten parte del curso entero', 'El programa no sirvió porque 20 de 40 es solo la mitad de todos los estudiantes del curso', 'Entrega los porcentajes, el cambio y un factor que puede influir, sin afirmar una causa segura.'),
    sc=[
        ("En Educación Física: ¿cómo se calcula el cambio en puntos porcentuales?", "Restando el porcentaje del antes al del después", "Es una resta simple entre dos porcentajes."),
        ("¿Qué se usa para comparar grupos de distinto tamaño?", "Los porcentajes", "Ajustan por el total que respondió."),
        ("¿Qué frase evita afirmar una causa segura?", "«Se observó que…»", "Informa lo que cambió sin asegurar el motivo."),
    ],
    op=("Un curso ficticio de 40 estudiantes respondió antes y después: «ánimo de 4 o 5» pasó de 12 a 20; «jugó en 3 o más recreos» pasó de 8 a 22. Calcula los porcentajes y el cambio en puntos porcentuales de cada indicador y escribe una frase prudente para el diario mural, sin nombres, que mencione un factor que pudo influir.",
        "Ánimo: de 30 % a 50 %, cambio de 20 puntos porcentuales. Recreos: de 20 % a 55 %, cambio de 35 puntos porcentuales. Frase: «Se observó que más estudiantes dicen tener buen ánimo y juegan más en los recreos; también hubo un paseo de curso en esas semanas».",
        ["porcentajes y cambios bien calculados", "frase prudente con «se observó que»", "un factor que pudo influir y sin nombres"],
        ["dos indicadores calculados y una frase para el diario mural"],
        ["comparar solo conteos", "afirmar una causa segura", "mostrar nombres de estudiantes"],
        "Pregunta: «¿qué otra cosa pudo influir en el cambio?». Si responde «nada», pídele pensar en actividades, clima o fechas."),
    reinforce="Inventa una encuesta de 20 estudiantes antes y después, calcula los porcentajes y el cambio de un indicador, y escribe una frase prudente.",
    extend="Explica por qué dos cursos de distinto tamaño se comparan con porcentajes y no con conteos.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 16 (resultados de ejemplo, inventados, de dos cursos ficticios de 50 estudiantes cada uno; respondieron 40 en cada uno, de forma voluntaria y anónima). "
     "Curso B, con 6 semanas de recreos activos: ánimo de 4 o 5, antes 10 estudiantes; después 20. "
     "Curso C, sin programa: ánimo de 4 o 5, antes 12 estudiantes; después 16. "
     "Notas: en el curso C hubo vacaciones de invierno entre ambas mediciones; en el curso B hubo una semana de pruebas. "
     "Regla: una comparación entre dos cursos orienta, pero no prueba la causa.")
build(
    O4, 4, F,
    use="Aprenderé a registrar y valorar el impacto de un programa con un grupo de comparación, a calcular tasas de respuesta y a decir con cuidado qué se puede concluir y qué no.",
    prior=["Sé calcular porcentajes y puntos porcentuales.", "Sé que una encuesta es anónima y repetible.", "Sé que una sola medición no prueba una causa."],
    explain=[
        "Un grupo de comparación es otro grupo parecido que no participa del programa y se mide igual. Si el grupo con programa cambia más que el grupo sin programa, esa diferencia orienta la valoración del impacto. Se calcula el cambio de cada grupo en puntos porcentuales y se resta un cambio de otro.",
        "También se calcula la tasa de respuesta: el porcentaje de personas del curso que respondió. Si responden pocas personas, o solo quienes quieren, el resultado puede ser sesgado, es decir, no representa al curso entero. Por eso se informa cuántas personas respondieron y cómo se las invitó.",
        "Un resultado se interpreta con límites: cada curso es uno solo, las condiciones de ambos eran distintas (vacaciones, pruebas) y el periodo fue corto. Por eso se dice «se observó una diferencia» y no «el programa causó». La regulación consiste en decidir un ajuste: repetir la medición, ampliar el periodo o mejorar la forma de invitar a responder.",
    ],
    vocab=[("grupo de comparación", "grupo parecido que no participa y se mide igual"), ("tasa de respuesta", "porcentaje de personas que respondió"), ("sesgo", "distorsión por quiénes responden o cómo se mide"), ("voluntaria", "que responde solo quien quiere"), ("límite", "aspecto que impide afirmar más de lo observado")],
    worked=[
        ("Calcular una tasa de respuesta", "De 50 estudiantes de un curso de ejemplo, respondieron 35. ¿Qué porcentaje respondió?", ["Divide 35 entre 50.", "Multiplica por 100: 70 %."], "70 %"),
        ("Comparar dos cambios", "Un grupo con programa cambió 30 puntos porcentuales y otro sin programa, 10. ¿Cuánto más cambió el grupo con programa?", ["Resta los cambios: 30 − 10.", "Es una diferencia de 20 puntos porcentuales, que orienta pero no prueba la causa."], "20 puntos porcentuales más; orienta pero no prueba"),
    ],
    mistakes=[("Concluir que el programa produjo toda la diferencia entre dos cursos.", "Otras condiciones también pudieron influir.", "Describe la diferencia y nombra lo que pudo influir."),
              ("No informar cuántas personas respondieron.", "Sin la tasa de respuesta no se sabe cuánto representa el resultado.", "Anota cuántas personas respondieron y qué porcentaje es.")],
    T=[
        ('abc', 'En Educación Física: ¿para qué se usa un grupo de comparación al evaluar un programa?', 'Para ver qué cambia en un grupo parecido que no participa y se mide igual', 'Para repetir el programa dos veces seguidas con el mismo grupo de personas', 'Para comparar las personas más activas con las menos activas del colegio', 'El grupo de comparación permite ver qué cambia sin el programa en un grupo parecido.'),
        ('abc', '{F} ¿Qué curso es el grupo de comparación?', 'El C, sin programa', 'El B, con recreos activos', 'Ambos cursos a la vez', 'El C no recibió el programa y se midió igual.'),
        ('=', '{F} ¿Qué porcentaje de cada curso respondió?', '40/50*100', 'Se divide los 40 que respondieron entre los 50 estudiantes y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Cuántos puntos porcentuales cambió el ánimo de 4 o 5 en el curso B?', '20*100/40-10*100/40', 'Se calcula 50 % menos 25 %.', ' puntos porcentuales'),
        ('=', '{F} ¿Cuántos puntos porcentuales cambió el ánimo de 4 o 5 en el curso C?', '16*100/40-12*100/40', 'Se calcula 40 % menos 30 %.', ' puntos porcentuales'),
        ('abc', '{F} ¿Qué curso tuvo el mayor cambio de ánimo?', 'El B, con programa', 'El C, sin programa', 'Los dos cambiaron igual', 'El B cambió 25 puntos y el C, 10.'),
        ('=', '{F} ¿Cuántos puntos porcentuales más cambió el curso B que el curso C?', '(20*100/40-10*100/40)-(16*100/40-12*100/40)', 'Se resta el cambio del curso C (10) del cambio del curso B (25).', ' puntos porcentuales'),
        ('abc', '{F} ¿Qué nota de la ficha limita comparar los dos cursos?', 'Que en C hubo vacaciones y en B, una semana de pruebas', 'Que ambos cursos tienen 50 estudiantes cada uno al comienzo del año', 'Que las dos encuestas fueron anónimas y se aplicaron de forma voluntaria', 'Las condiciones distintas impiden afirmar que la diferencia se debe al programa.'),
        ('abc', '{F} ¿Qué frase es más prudente?', 'Se observó que el ánimo subió más en el curso con programa, aunque las condiciones diferían', 'Quedó probado que el programa produce más ánimo que cualquier otra actividad que exista', 'No hay ninguna diferencia entre los dos cursos, porque son cursos distintos entre sí', 'Describe la diferencia y reconoce el límite.'),
        ('abc', 'Un curso de 50 estudiantes tiene una tasa de respuesta de 20 % y responden solo quienes quieren. ¿Qué problema tiene el resultado?', 'Puede estar sesgado, porque pocas personas respondieron y no se sabe si representan al curso', 'No tiene ningún problema, porque las respuestas voluntarias son siempre las más honestas', 'Es mejor que el de otro curso con más respuestas, porque responde menos gente y es más claro', 'Una tasa baja y voluntaria puede mostrar solo una parte del curso.'),
        ('abc', 'Dos estudiantes valoran el resultado. Ana dice: «el programa sirve, por la diferencia de 15 puntos». Bruno dice: «orienta, pero faltan más cursos y más semanas». ¿Qué valoración es más cuidadosa?', 'La de Bruno, porque reconoce los límites de una sola comparación', 'La de Ana, porque la diferencia de 15 puntos es un número claro y directo', 'Las dos igual, porque ambas se apoyan en un dato calculado de la tabla', 'Reconocer los límites evita afirmar más de lo observado.'),
        ('abc', 'Un estudiante propone que, para subir la tasa de respuesta, se pida el nombre a cada persona. ¿Qué corresponde?', 'No pedirlo: mejor explicar para qué sirve la encuesta y asegurar el anonimato', 'Pedirlo, porque así se sabe quién no respondió y se presiona a responder', 'Pedirlo solo a quienes no respondieron la vez anterior', 'La encuesta es anónima; mejorar la invitación respeta la privacidad.'),
        ('abc', 'Alguien comenta que el curso C «no hace nada» y que por eso es un curso poco activo. ¿Qué corresponde?', 'Pedir que no juzguen al curso: el grupo de comparación solo valora el programa', 'Aceptarlo, porque los datos lo muestran de forma clara en la ficha del curso C', 'Publicar los resultados del curso C para que todo el colegio lo sepa de inmediato', 'Un grupo de comparación no es un juicio sobre personas.'),
    ],
    ctx=('abc', 'Un equipo de ejemplo evaluó un programa de caminatas en el curso D, con 60 estudiantes de los cuales respondieron 30. El ánimo de 4 o 5 pasó de 20 % a 40 % entre los que respondieron. ¿Qué informe es más adecuado?', 'Informar que respondió la mitad y que, entre quienes respondieron, subió 20 puntos, con cautela', 'Informar que todo el curso mejoró 20 puntos porcentuales y que el programa funcionó sin dudas', 'No informar nada, porque respondió solo la mitad del curso y con eso no se puede decir nada', 'Debe decir quiénes respondieron y limitar la conclusión a esa parte.'),
    sc=[
        ("En Educación Física: ¿qué es la tasa de respuesta?", "El porcentaje de personas que respondió", "Indica cuánto representa el resultado al grupo."),
        ("¿Qué frase evita afirmar una causa segura?", "«Se observó una diferencia…»", "Describe lo visto sin asegurar la causa."),
        ("¿Qué se hace si la tasa de respuesta es baja?", "Informarla y mejorar la invitación respetando el anonimato", "No se presiona ni se exponen nombres."),
    ],
    op=("Un curso ficticio con programa y otro sin programa, ambos con 40 respuestas, informan «jugó en 3 o más recreos»: con programa pasó de 10 a 24; sin programa pasó de 12 a 16. Calcula los cambios en puntos porcentuales, la diferencia entre ambos y escribe una conclusión prudente con dos límites de la comparación.",
        "Con programa: 25 % a 60 %, cambio de 35 puntos. Sin programa: 30 % a 40 %, cambio de 10 puntos. Diferencia: 25 puntos porcentuales. Conclusión: «Se observó más cambio en el curso con programa; pero es un solo curso y no sabemos qué otras actividades hubo».",
        ["cambios y diferencia bien calculados", "conclusión con «se observó»", "dos límites de la comparación"],
        ["cálculos, conclusión prudente y dos límites"],
        ["afirmar una causa segura", "no mencionar límites", "juzgar al curso sin programa"],
        "Pregunta: «¿qué dos cosas impiden asegurar la causa?». Si dice «ninguna», pídele que mire las notas de la ficha."),
    reinforce="Con una tabla inventada de dos grupos, calcula los cambios y la diferencia, y escribe dos límites de la comparación.",
    extend="Explica por qué el grupo de comparación ayuda a valorar el impacto, pero no permite afirmar la causa.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 17 (seguimiento de ejemplo, inventado, de un programa de recreos activos en un curso de 40 estudiantes). "
     "Estudiantes que jugaron en al menos un recreo activo: semana 1, 24; semana 2, 28; semana 3, 30; semana 4, 27 (dos días de lluvia); semana 5, 20 (cuatro días de lluvia); semana 6, 22. "
     "Encuesta anónima sobre qué dificulta participar (puede marcarse más de una; total de menciones): lluvia sin espacio techado, 12; solo hay juegos competitivos, 9; no tengo con quién jugar, 7; no me gusta correr, 5. "
     "Ajustes posibles: A1) habilitar el gimnasio techado los días de lluvia; A2) sumar juegos cooperativos y variantes sin carrera; A3) crear «parejas de bienvenida» para invitar a quienes están solos; A4) dar puntos a los equipos que ganan.")
build(
    O4, 5, F,
    use="Aprenderé a evaluar el impacto de un programa en el bienestar personal y social con datos de seguimiento y a ajustarlo con medidas inclusivas, eligiendo cambios que respondan a las dificultades que las personas mencionan.",
    prior=["Sé calcular promedios y porcentajes.", "Sé interpretar resultados con cuidado.", "Sé que ante exclusión o burlas se avisa a una persona adulta."],
    explain=[
        "Evaluar y ajustar es mirar cómo evoluciona un programa y decidir cambios con los datos. Se observa la participación semana a semana, se buscan las semanas en que bajó y se relacionan con lo que las personas dicen que dificulta participar. Si bajó cuando llovió, se piensa en un lugar techado; si muchas personas dicen que solo hay juegos competitivos, se suman juegos cooperativos.",
        "Un ajuste inclusivo responde a las dificultades concretas y permite que más personas participen sin tener que cambiar quiénes son. Se prefiere cambiar la actividad, el lugar o la forma de invitar, y no pedir que las personas se adapten solas. El ajuste debe ser seguro, simple y medible para volver a evaluar después.",
        "Si una persona cuenta que se siente excluida o que otras se burlan de ella, no se enfrenta a las demás ni se guarda en secreto: se avisa a una persona adulta de confianza, como docente u orientador. El programa busca el bienestar de todo el grupo y no mide ni juzga cuerpos.",
    ],
    vocab=[("seguimiento", "registro repetido de un mismo dato en el tiempo"), ("barrera", "dificultad que impide o reduce la participación"), ("ajuste inclusivo", "cambio que permite participar a más personas"), ("juego cooperativo", "juego donde el grupo gana o logra algo en conjunto"), ("exclusión", "dejar a una persona fuera de un grupo o actividad")],
    worked=[
        ("Relacionar una baja con una causa", "En un seguimiento de ejemplo, la participación baja las dos semanas de lluvia. ¿Qué ajuste responde a esa causa?", ["La dificultad es el clima sin lugar techado.", "Habilitar un espacio techado para esos días responde directamente."], "Habilitar un espacio techado"),
        ("Priorizar con datos", "Entre cuatro barreras, una tiene 9 menciones, otra 6, otra 4 y otra 2. ¿Con cuál se empieza?", ["Se empieza por la que más personas mencionan.", "Es la de 9 menciones."], "Con la barrera de 9 menciones"),
    ],
    mistakes=[("Culpar a quienes dejaron de participar.", "Las barreras suelen estar en la actividad, el lugar o la invitación.", "Revisa qué barreras se mencionan y ajusta el programa."),
              ("Elegir un ajuste que aumenta la competencia cuando la barrera es la competencia.", "Empeora el problema que las personas señalaron.", "Elige un ajuste que responda a la barrera.")],
    T=[
        ('abc', 'En Educación Física: ¿qué es una barrera para participar?', 'Una dificultad que impide o reduce la participación', 'Un cerco que separa las canchas del resto del patio del colegio', 'Una regla de seguridad que deben cumplir los juegos del recreo', 'Las barreras son dificultades; no son solo objetos físicos ni reglas.'),
        ('abc', '{F} ¿En qué semana participó el mayor número de estudiantes?', 'La semana 3, con 30', 'La semana 2, con 28', 'La semana 5, con 20', 'La semana 3 fue la de mayor participación.'),
        ('abc', '{F} ¿Qué barrera mencionó la mayor cantidad de estudiantes?', 'La lluvia sin espacio techado', 'Solo hay juegos competitivos', 'No tengo con quién jugar', 'Se menciona 12 veces, más que cualquier otra.'),
        ('=', '{F} ¿Cuántas menciones en total hay entre las cuatro barreras?', '12+9+7+5', 'Se suman las menciones de las cuatro barreras.', ' menciones'),
        ('abc', '{F} ¿Qué ajuste responde a la barrera «no tengo con quién jugar»?', 'A3, parejas de bienvenida', 'A1, gimnasio techado', 'A4, puntos a los equipos que ganan', 'A3 invita a quienes están solos y responde esa barrera.'),
        ('abc', '{F} ¿Por qué A4 no es un buen ajuste?', 'Porque aumenta la competencia, que es una barrera mencionada', 'Porque exige un gimnasio techado que el colegio todavía no tiene', 'Porque no se puede medir cuántas personas participan en ese juego', 'La competencia ya es una barrera; premiar a quienes ganan la refuerza.'),
        ('=', '{F} ¿Cuántos estudiantes menos participaron en la semana 5 que en la semana 3?', '30-20', 'Se resta la participación de la semana 5 de la de la semana 3.', ' estudiantes'),
        ('=', '{F} ¿Cuál fue el promedio de estudiantes participantes en las semanas 1, 2, 3 y 6?', '(24+28+30+22)/4', 'Se suman las cuatro semanas, que dan 104, y se dividen por 4.', ' estudiantes'),
        ('abc', '{F} ¿Qué ajuste se relaciona con las semanas 4 y 5, en que hubo lluvia?', 'A1, habilitar el gimnasio techado los días de lluvia', 'A2, sumar juegos cooperativos y variantes sin carrera', 'A3, crear parejas de bienvenida para quienes están solos', 'La participación bajó en las semanas de lluvia; A1 responde a esa causa.'),
        ('abc', '{F} El equipo del curso solo puede aplicar dos ajustes en la próxima etapa. ¿Qué par es más coherente con los datos?', 'A1 y A2, porque responden a las dos barreras más mencionadas', 'A3 y A4, porque son los más sencillos de organizar', 'A2 y A4, porque ambos aumentan el movimiento en el recreo', 'Las barreras con más menciones son la lluvia (12) y los juegos competitivos (9).'),
        ('abc', 'Alguien dice: «los que no participan no quieren moverse; es su problema». ¿Qué respuesta es más adecuada?', 'Las personas mencionaron dificultades concretas y el programa puede ajustarse', 'Tiene razón, y el programa debe seguir igual para quienes sí quieren participar', 'Hay que obligar a participar a quienes no lo hacen, para que los datos mejoren', 'La participación depende también del lugar, de la actividad y de la invitación.'),
        ('abc', 'Una estudiante de ejemplo cuenta que algunos compañeros se burlan de cómo se mueve en los juegos y que por eso dejó de ir al recreo activo. ¿Qué corresponde?', 'Avisar a una persona adulta de confianza, como un docente u orientador', 'Enfrentar a esos compañeros ella sola para que dejen de hacerlo de inmediato', 'Guardarlo en secreto para evitar que la situación empeore con el paso del tiempo', 'Ante burlas se avisa a una persona adulta; no se enfrenta sola ni se guarda en secreto.'),
        ('abc', '{F} El curso quiere volver a evaluar después de aplicar A1 y A2. ¿Qué plan permite saber si funcionaron?', 'Repetir el conteo semanal y la misma encuesta anónima, y comparar con esta ficha', 'Preguntar en voz alta a cada estudiante si le gustó el cambio de los recreos', 'Cambiar los indicadores y las preguntas para hacerlas más completas que las del comienzo', 'Repetir las mismas mediciones permite comparar con esta línea de base.'),
    ],
    ctx=('abc', 'En el seguimiento de ejemplo de otro curso, la participación sube 4 semanas y baja las dos últimas, cuando comienzan las pruebas. Las barreras dicen: «falta de tiempo» (14 menciones) y «no sé a qué juegos puedo unirme» (8). ¿Qué ajuste de una sola condición es más coherente?', 'Ofrecer sesiones breves de 10 minutos y un panel con los juegos del día en las semanas de pruebas', 'Cancelar el programa hasta que terminen las pruebas y retomarlo recién el semestre siguiente', 'Exigir participación a todas las personas del curso para que los datos de asistencia no bajen', 'Responde a las dos barreras con sesiones breves y una invitación clara.'),
    sc=[
        ("En Educación Física: ¿qué se hace primero para decidir un ajuste inclusivo?", "Mirar las barreras que las personas mencionan", "El ajuste debe responder a dificultades reales."),
        ("¿Qué se hace si una persona cuenta que se burlan de ella?", "Avisar a una persona adulta de confianza", "No se enfrenta ni se guarda como secreto."),
        ("¿Qué mediciones se repiten para saber si un ajuste funcionó?", "Las mismas del seguimiento inicial", "Solo mediciones iguales se pueden comparar."),
    ],
    op=("Inventa el seguimiento de 5 semanas de un programa de actividad física para un curso de 30 estudiantes (participantes por semana) y tres barreras con su número de menciones. Elige dos ajustes inclusivos que respondan a las barreras más mencionadas, explica por qué y escribe cómo volverías a evaluar.",
        "Participantes: 15, 18, 20, 17, 12. Barreras: horario (10), solo juegos de correr (7), vergüenza de equivocarse (5). Ajustes: mover el horario a un bloque con más tiempo y sumar juegos sin carrera. Para evaluar: repetir el conteo semanal y la misma encuesta anónima de barreras por 4 semanas.",
        ["seguimiento y barreras con números", "dos ajustes que responden a las barreras principales", "plan para volver a evaluar con las mismas mediciones"],
        ["seguimiento, dos ajustes justificados y un plan de reevaluación"],
        ["culpar a quienes no participan", "elegir un ajuste que no responde a las barreras", "cambiar las mediciones al reevaluar"],
        "Pregunta: «¿qué barrera atiende cada ajuste?». Si no puede decirlo, pídele que lo conecte con las menciones."),
    reinforce="Con la ficha de la clase, escribe qué ajuste responde a cada barrera y qué dato revisarías después de aplicarlo.",
    extend="Explica por qué un ajuste inclusivo cambia la actividad o el lugar en vez de pedir a las personas que se adapten solas.",
)
