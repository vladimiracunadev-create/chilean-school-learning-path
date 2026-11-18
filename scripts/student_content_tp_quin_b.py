"""Química Industrial TP 3.º medio: OAE-03 (informes), clases 4 y 5, y OAE-04 (vigilar estándares de seguridad). Todo en papel, con datos de ejemplo; la vigilancia se limita a observar, registrar e informar, sin intervenir equipos ni sustancias."""
from __future__ import annotations

from tp_quin_common import AVISO, EMER, build, em

O3 = "TP-QUIN-3-OAE-03"
O4 = "TP-QUIN-3-OAE-04"

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada). Producción de un lote de ejemplo en la planta ficticia «Química Demo Valle Claro», en kg por turno, durante 5 turnos: 400; 420; 380; 440; 360. Meta de ejemplo: 400 kg por turno. "
     "Regla de aviso de ejemplo: se avisa al especialista si un turno se aleja de la meta en más de 8 % (es decir, más de 32 kg). El turno 4 rechazó 22 kg de lo producido por no cumplir la calidad.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar criterios con datos de ejemplo para un informe: desvío respecto de una meta, porcentaje de cumplimiento, tasa de rechazo, variación porcentual y regla de aviso.",
    prior=["Sé calcular un promedio y un porcentaje.", "Sé qué es una tendencia.", "Sé restar y dividir números enteros."],
    explain=[
        "En Química Industrial, una meta es el valor que se espera alcanzar en cada periodo, y el desvío es la diferencia entre lo medido y la meta: positivo si se supera y negativo si no se alcanza. El porcentaje de cumplimiento de la meta compara cuántos periodos la alcanzaron con el total. La tasa de rechazo es lo rechazado dividido entre lo producido, por 100.",
        "La variación porcentual compara el cambio entre dos valores con el valor inicial. Una regla de aviso fija desde qué desvío se informa al especialista; por ejemplo, avisar si el desvío supera el 8 % de la meta. El 8 % de 400 kg se calcula como 400 por 8 entre 100, que son 32 kg. Un informe incluye estos cálculos con sus datos de origen para que el especialista pueda revisarlos.",
        f"Los cálculos de un informe orientan, pero la decisión sobre el proceso es del profesional especialista. {EMER} {AVISO}",
    ],
    vocab=[("meta", "valor que se espera alcanzar en cada periodo"), ("desvío", "diferencia entre lo medido y la meta"), ("porcentaje de cumplimiento", "periodos que alcanzan la meta divididos entre el total, por 100"), ("tasa de rechazo", "cantidad rechazada dividida entre la producida, por 100"), ("variación porcentual", "cambio dividido entre el valor inicial, por 100"), ("regla de aviso", "criterio que fija desde qué desvío se informa al especialista")],
    worked=[
        ("Desvío", "En una planilla de ejemplo la meta es de 300 kg y un turno produjo 270 kg. ¿Cuál es el desvío y qué porcentaje de la meta es?", ["El desvío es 270 menos 300, es decir, menos 30 kg.", "30 por 100 entre 300 son 10 %."], "Desvío de menos 30 kg, es decir, 10 % bajo la meta"),
        ("Tasa de rechazo", "Un turno de ejemplo produjo 200 kg y rechazó 6 kg. ¿Cuál es la tasa de rechazo?", ["Se divide lo rechazado entre lo producido: 6 entre 200.", "6 por 100 son 600, y 600 entre 200 son 3."], "3 %"),
    ],
    mistakes=[("Calcular el porcentaje de variación dividiendo entre el valor final.", "La variación porcentual se compara siempre con el valor inicial.", "Divide el cambio entre el valor de partida."),
              ("Mirar solo el promedio y no avisar de un turno muy desviado.", "Un promedio parejo puede ocultar turnos que superan la regla de aviso.", "Calcula el desvío de cada turno y compáralo con la regla.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es el desvío respecto de una meta?", "La diferencia entre lo medido y la meta", "El promedio de todos los turnos", "El límite máximo de la variable", "El desvío mide cuánto se aleja el dato de la meta."),
        ("abc", "En Química Industrial: ¿qué es una regla de aviso?", "Un criterio que fija desde qué desvío se informa al especialista", "Una norma que prohíbe medir", "Un formato para firmar el informe", "La regla de aviso indica cuándo hay que informar."),
        ("abc", "En Química Industrial: ¿cómo se calcula la tasa de rechazo?", "Lo rechazado dividido entre lo producido, por 100", "Lo producido dividido entre lo rechazado, por 100", "Lo rechazado menos la meta", "La tasa compara lo rechazado con el total producido."),
        ("=", "{F} ¿Cuántos kg se produjeron en total en los 5 turnos?", "400+420+380+440+360", "Se suman las producciones de los cinco turnos.", " kg"),
        ("=", "{F} ¿Cuál es el desvío del turno 2 respecto de la meta?", "420-400", "Se resta la meta a la producción del turno.", " kg"),
        ("=", "{F} ¿Cuántos turnos alcanzaron o superaron la meta de 400 kg?", "3", "Cumplen los turnos con 400, 420 y 440 kg.", " turnos"),
        ("=", "{F} ¿Qué porcentaje de los turnos alcanzó la meta?", "3*100//5", "Se divide el número de turnos que cumplen entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es la tasa de rechazo del turno 4?", "22*100//440", "Se divide lo rechazado entre lo producido y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué turnos deben avisarse según la regla de aviso de más de 32 kg de desvío?", "Los turnos 4 y 5, con desvíos de 40 kg", "Solo el turno 5", "Los turnos 2 y 3, con desvíos de 20 kg", "Los desvíos de 40 kg superan los 32 kg; los de 20 kg no."),
        ("=", "{F} ¿Cuántos kg faltaron en total en los turnos 3 y 5 para llegar a la meta?", "(400-380)+(400-360)", "Se suman lo que faltó a la meta en cada uno de esos turnos.", " kg"),
        ("=", "{F} ¿Cuál fue la variación porcentual de la producción entre el turno 1 y el turno 5? Es una baja.", "(400-360)*100//400", "Se divide el cambio entre el valor inicial y se multiplica por 100.", " %"),
        ("abc", "{F} Un compañero dice: «el promedio fue de 400 kg, igual a la meta, así que no hay nada que avisar». ¿Es correcto?", "No: dos turnos superan la regla de aviso aunque el promedio coincida con la meta", "Sí, porque el promedio cumple la meta", "Sí, porque solo se avisa si el promedio baja", "El promedio puede compensar desvíos que igual se deben informar."),
        em("Calculas desvíos en una planilla de ejemplo cuando oyes que en la sala de producción se cayó un envase y hay un olor irritante que se extiende.", 0),
    ],
    ctx=("abc", "Un supervisor de ejemplo te pide «redondear» el turno de 360 kg a 400 kg en el informe para que no se vea el desvío. ¿Qué respondes?", "Que no: el informe debe llevar el dato real y el desvío se informa al especialista", "Que sí, si el promedio sigue igual", "Que sí, pero solo en el gráfico", "Cambiar un dato oculta una desviación y vuelve falso el informe."),
    sc=[
        ("En Química Industrial: ¿cómo se calcula el desvío?", "Dato medido menos meta", "El signo indica si se superó o no se alcanzó la meta."),
        ("En Química Industrial: ¿respecto de qué valor se calcula la variación porcentual?", "Del valor inicial", "Se compara el cambio con el punto de partida."),
        ("¿Qué se hace si un turno supera la regla de aviso?", "Se informa al profesional especialista", "La regla de aviso existe para eso."),
    ],
    op=("Planilla ficticia de «Química Demo Costa Norte»: producción en 4 turnos, en kg: 200; 220; 180; 200. Meta de 200 kg por turno. Regla de aviso: más de 10 % de desvío (más de 20 kg). El turno 2 rechazó 11 kg. Escribe (a) el desvío de cada turno, (b) qué turnos deben avisarse, (c) el porcentaje de turnos que alcanzaron la meta, (d) por qué conviene incluir los datos de origen en el informe.",
        "(a) 0; más 20; menos 20; 0 kg. (b) Ninguno, porque 20 kg no supera el límite de 20 kg. (c) 3 de 4 turnos alcanzan o superan la meta: 75 %. (d) Para que el especialista pueda revisar y repetir los cálculos.",
        ["calcula los desvíos", "aplica la regla de aviso con exactitud", "calcula el porcentaje de cumplimiento", "justifica incluir los datos de origen"],
        ["hoja con las cuatro respuestas"],
        ["decir que 20 supera a 20", "no calcular con la meta", "omitir los datos de origen"],
        "Pregunta: «¿20 es mayor que 20?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa cinco producciones con una meta y una regla de aviso, y decide qué turnos avisarías.",
    extend="Explica con un ejemplo por qué una regla de aviso debe escribirse antes de revisar los datos.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Tabla del tanque T7 de la planta ficticia «Química Demo Valle Claro»: temperatura en °C cada hora, 08:00 = 30; 09:00 = 32; 10:00 = 34; 11:00 = 36. Límite de ejemplo: de 20 a 60 °C. "
     "Versión A del informe: «Entre las 08:00 y las 11:00 la temperatura subió de 30 a 36 °C, 2 °C por hora, dentro del límite de 20 a 60 °C. Se informa al especialista para su revisión.» (con título, fecha y espacio de aprobación, pero sin la firma del responsable). "
     "Versión B: «La temperatura está subiendo mucho y es peligroso; hay que parar todo.» (con título y fecha, sin datos ni firma). Versión C: «La temperatura subió 8 °C entre las 08:00 y las 11:00.» "
     "Lista de verificación de un informe, 5 puntos: (1) título y fecha; (2) responsable y firma; (3) datos con unidad; (4) tendencia descrita con datos; (5) sin opiniones ni órdenes. "
     "Hacer un informe manual toma 30 minutos y uno digital 10 minutos; se hacen 20 informes al mes.")
build(
    O3, 5, F,
    use="Aprenderé a comparar versiones de un informe, a verificar que coincidan con la tabla de datos y a evaluarlas con una lista de verificación de cinco puntos.",
    prior=["Sé qué es una tendencia y una observación.", "Sé calcular porcentajes sencillos.", "Sé que un informe lleva firma y espacio de aprobación."],
    explain=[
        "En Química Industrial, verificar un informe es comprobar que lo que dice coincide con la tabla de datos y que cumple el formato. Una versión es coherente si cada cifra del texto se puede encontrar o calcular a partir de la tabla. Si dice que subió 8 °C y la tabla muestra una subida de 6 °C, hay una incoherencia, y se corrige antes de entregarlo.",
        "Para comparar versiones se usa una lista de verificación: cada punto se marca como cumple o no cumple, y el porcentaje de cumplimiento es los puntos cumplidos entre el total, por 100. Un buen informe usa datos, no opiniones ni órdenes. También se pueden comparar formatos: uno manual y uno digital se comparan por tiempo, orden y respaldo, y en el digital la clave personal no se comparte ni se presta.",
        f"Todo este análisis es de papel; el informe no autoriza a intervenir un equipo. {EMER} {AVISO}",
    ],
    vocab=[("coherencia", "acuerdo entre lo que dice el texto y los datos de la tabla"), ("lista de verificación", "tabla de puntos que se marcan como cumple o no cumple"), ("versión", "forma distinta de redactar un mismo informe"), ("clave personal", "contraseña que identifica a una persona y que no se comparte"), ("respaldo", "copia de seguridad de un registro")],
    worked=[
        ("Comprobar una cifra", "Una tabla de ejemplo muestra 20, 22, 24 y 26 °C, y un informe dice «subió 6 °C». ¿Es coherente?", ["La subida es 26 menos 20, es decir, 6 °C.", "La cifra coincide con la tabla."], "Sí, es coherente"),
        ("Lista de verificación", "Un informe de ejemplo cumple 4 de los 5 puntos de la lista. ¿Qué porcentaje de cumplimiento tiene?", ["Se dividen 4 entre 5 y se multiplica por 100.", "4 por 100 son 400, y 400 entre 5 son 80."], "80 %"),
    ],
    mistakes=[("Revisar un informe solo por su aspecto y no comparar sus cifras con la tabla.", "Un informe prolijo puede traer una cifra errada.", "Recalcula cada cifra del texto con la tabla."),
              ("Compartir la clave del informe digital con un compañero para ahorrar tiempo.", "La clave identifica a una persona; compartirla permite firmar en su nombre.", "Usa solo tu clave y no la prestes.")],
    T=[
        ("abc", "En Química Industrial: ¿cuándo un informe es coherente con su tabla?", "Cuando cada cifra del texto se puede obtener de la tabla", "Cuando está escrito con letra clara", "Cuando es más largo que la tabla", "La coherencia exige acuerdo entre texto y datos."),
        ("abc", "En Química Industrial: ¿para qué sirve una lista de verificación de informes?", "Para marcar punto por punto si el informe cumple lo exigido", "Para calcular el promedio de las lecturas", "Para reemplazar la tabla de datos", "La lista permite revisar de forma ordenada."),
        ("abc", "En Química Industrial: ¿por qué no se comparte la clave personal de un informe digital?", "Porque identifica a una persona y permitiría firmar en su nombre", "Porque la clave se desgasta con el uso", "Porque solo funciona en horario de turno", "La clave personal asegura quién firmó."),
        ("=", "{F} ¿Cuántos °C subió la temperatura entre las 08:00 y las 11:00?", "36-30", "Se resta la primera lectura a la última.", " °C"),
        ("abc", "{F} ¿Qué versión del informe es coherente con la tabla?", "La A, porque sus cifras coinciden con la tabla", "La C, porque dice que subió 8 °C", "La B, porque advierte del peligro", "En A, de 30 a 36 °C son 6 °C, 2 por hora."),
        ("abc", "{F} ¿Por qué la versión C no es coherente?", "Dice que subió 8 °C, pero la tabla muestra 6 °C", "Porque no menciona el límite", "Porque tiene título", "La cifra del texto no coincide con la tabla."),
        ("abc", "{F} ¿Qué punto de la lista incumple la versión B por escribir «hay que parar todo»?", "El punto 5, porque contiene una orden", "El punto 1, porque no tiene título", "El punto 3, porque tiene unidad", "Una orden no es parte de un informe de datos."),
        ("=", "{F} La versión A cumple todos los puntos menos el 2. ¿Qué porcentaje de cumplimiento tiene?", "4*100//5", "Se dividen los puntos cumplidos entre el total y se multiplica por 100.", " %"),
        ("=", "{F} La versión B cumple solo el punto 1. ¿Qué porcentaje de cumplimiento tiene?", "1*100//5", "Se divide el único punto cumplido entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué falta en la versión A para estar completa?", "La firma del responsable", "El espacio de aprobación", "El título y la fecha", "La ficha dice que la versión A no lleva la firma del responsable."),
        ("=", "{F} ¿Cuántos minutos al mes se ahorran al pasar del formato manual al digital?", "(30-10)*20", "Se resta el tiempo digital al manual y se multiplica por los informes del mes.", " minutos"),
        ("abc", "{F} Un compañero propone usar la clave de otra persona para firmar la versión digital «porque ella ya revisó». ¿Qué corresponde?", "Rechazarlo: cada persona firma con su propia clave", "Aceptarlo si ella lo autoriza de palabra", "Aceptarlo si el informe es corto", "La firma identifica a quien se hace responsable."),
        em("Comparas versiones de un informe de ejemplo cuando alguien avisa que de una sala de proceso sale humo y que una alarma suena sin parar.", 1),
    ],
    ctx=("abc", "Un jefe de ejemplo te pide entregar hoy la versión B del informe «porque es la más corta y se entiende». ¿Qué respondes?", "Que la versión A es la que corresponde, porque tiene datos y no órdenes, y que le falta solo la firma", "Que la B está bien, porque advierte", "Que da lo mismo cuál se entregue", "La B no tiene datos ni firma y trae una orden; la A cumple casi todo."),
    sc=[
        ("En Química Industrial: ¿qué se revisa para verificar un informe?", "Que las cifras coincidan con la tabla y que cumpla el formato", "La coherencia y el formato son los dos controles."),
        ("¿Cómo se calcula el porcentaje de cumplimiento de la lista?", "Puntos cumplidos entre el total, por 100", "Se expresa como porcentaje de la lista completa."),
        ("En Química Industrial: ¿se debe prestar la clave personal del informe digital?", "No, porque identifica a una persona", "La firma debe corresponder a quien realmente revisó."),
    ],
    op=("Caso ficticio de «Química Demo Costa Norte»: tabla de humedad de una bodega, en %: lunes 50; martes 52; miércoles 54. Versión X del informe: «La humedad subió 6 puntos entre lunes y miércoles; todo normal.» Versión Y: «La humedad subió de 50 a 54 % entre lunes y miércoles, es decir, 4 puntos.» (con título, fecha y espacio de aprobación, pero sin firma). Escribe (a) cuál versión es coherente con la tabla y por qué, (b) qué punto de la lista incumple la versión X por su última frase, (c) qué porcentaje de cumplimiento tiene Y si cumple 4 de los 5 puntos, (d) por qué el informe no debe incluir órdenes ni opiniones.",
        "(a) La Y, porque 54 menos 50 son 4 puntos; la X dice 6, que no coincide con la tabla. (b) El punto 5, porque «todo normal» es una opinión. (c) 80 %. (d) Porque el informe describe con datos y el especialista interpreta y decide.",
        ["comprueba la cifra con la tabla", "identifica el punto incumplido", "calcula el porcentaje", "separa informe de órdenes"],
        ["hoja con las cuatro respuestas"],
        ["no comparar con la tabla", "aceptar una opinión como dato", "incluir órdenes"],
        "Pregunta: «¿cuántos puntos subió la humedad según la tabla?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Escribe dos versiones de un informe con la misma tabla, una correcta y una con un error, y evalúalas con la lista de cinco puntos.",
    extend="Explica con un ejemplo por qué una cifra errada en un informe puede cambiar la decisión del especialista.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Ronda de inspección en la planta ficticia «Química Demo Valle Claro» con una lista de 10 puntos: salidas de emergencia libres; extintores señalizados y con revisión vigente; señalética visible; pisos secos; envases rotulados; hojas de datos de seguridad disponibles; personal con elementos de protección según su área; "
     "equipos de emergencia señalizados; orden y limpieza; registro de la ronda firmado. Resultado: 8 puntos cumplen y 2 no cumplen: «pisos mojados en el pasillo 3» y «un envase sin rótulo en la bodega». "
     "Matriz de ejemplo: puntaje = probabilidad × gravedad. Pisos mojados: probabilidad 4 y gravedad 2. Envase sin rótulo: probabilidad 3 y gravedad 4.")
build(
    O4, 1, F,
    use="Aprenderé qué significa vigilar el cumplimiento de estándares de seguridad en una planta química: observar, registrar e informar, sin intervenir equipos ni sustancias, y con la norma vigente como referencia.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé calcular un porcentaje.", "Sé qué es una lista de verificación."],
    explain=[
        "En Química Industrial, un estándar de seguridad es un requisito escrito que debe cumplirse, por ejemplo que las salidas de emergencia estén libres o que los envases estén rotulados. Se basa en la norma vigente, nacional y, en algunos casos, internacional. Vigilar su cumplimiento significa observar con una lista de verificación, registrar lo que se ve e informar a quien corresponde: no significa reparar, mover sustancias ni operar equipos.",
        "Un hallazgo es lo que la ronda encuentra, y una no conformidad es un hallazgo que incumple un estándar. Cada una se prioriza con la matriz: puntaje igual a probabilidad por gravedad. La autoridad sanitaria fiscaliza el cumplimiento, y en la empresa el prevencionista de riesgos y el comité paritario colaboran en la prevención. Cada trabajador debe avisar lo que observa.",
        f"Vigilar no te habilita para actuar sobre el riesgo: eso lo hace personal formado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("estándar de seguridad", "requisito escrito que debe cumplirse para trabajar con seguridad"), ("vigilar", "observar con una lista, registrar e informar, sin intervenir"), ("hallazgo", "lo que encuentra una ronda de inspección"), ("no conformidad", "hallazgo que incumple un estándar"), ("ronda de inspección", "recorrido planificado con una lista de verificación"), ("comité paritario", "grupo de trabajadores y empresa que colabora en la prevención")],
    worked=[
        ("Hallazgo y no conformidad", "En una ronda de ejemplo se ve un extintor con la revisión vencida. ¿Qué es y qué se hace?", ["Incumple el estándar de revisión vigente, así que es una no conformidad.", "Se registra en la lista y se informa al responsable; no se repara en el momento."], "No conformidad: se registra e informa"),
        ("Puntaje", "Una escalera sin barandas de ejemplo tiene probabilidad 2 y gravedad 5. ¿Qué puntaje tiene?", ["Se multiplica la probabilidad por la gravedad.", "2 por 5 son 10."], "10 puntos"),
    ],
    mistakes=[("Creer que vigilar incluye arreglar el problema encontrado.", "Corregir lo encontrado lo hace personal autorizado; quien vigila registra e informa.", "Anota el hallazgo y avisa al responsable del área."),
              ("No anotar un hallazgo pequeño «porque no pasó nada».", "Los hallazgos pequeños pueden ser el aviso de un problema mayor.", "Registra todo lo que incumple, aunque parezca menor.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es un estándar de seguridad?", "Un requisito escrito que debe cumplirse para trabajar con seguridad", "Una sugerencia que cada persona puede ignorar", "Un tipo de instrumento de medición", "El estándar es un requisito obligatorio, no una sugerencia."),
        ("abc", "En Química Industrial: ¿qué significa vigilar el cumplimiento de la seguridad?", "Observar con una lista, registrar e informar, sin intervenir equipos ni sustancias", "Reparar todo lo que se encuentre mal", "Operar los equipos para comprobar que funcionan", "Vigilar es observar e informar; corregir lo hace personal autorizado."),
        ("abc", "En Química Industrial: ¿qué es una no conformidad?", "Un hallazgo que incumple un estándar", "Un trabajador que opina distinto", "Un producto que no se vende", "La no conformidad es un incumplimiento detectado."),
        ("=", "{F} ¿Cuántos puntos de la lista incumplen el estándar?", "10-8", "Se resta lo que cumple al total de puntos.", " puntos"),
        ("=", "{F} ¿Qué porcentaje de los puntos de la lista cumple?", "8*100//10", "Se dividen los puntos que cumplen entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el envase sin rótulo?", "3*4", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("abc", "{F} Según la matriz, ¿qué hallazgo se atiende primero?", "El envase sin rótulo, con 12 puntos", "Los pisos mojados, con 8 puntos", "Ambos al mismo tiempo, porque los dos incumplen", "El mayor puntaje tiene prioridad: 12 es mayor que 8."),
        ("abc", "{F} Quien hace la ronda ve el piso mojado del pasillo 3. ¿Qué corresponde que haga?", "Registrarlo e informar al responsable del área", "Secar el piso con lo que tenga a mano y no anotar nada", "Ignorarlo porque tiene bajo puntaje", "Vigilar es registrar e informar; la corrección es del personal autorizado."),
        ("abc", "{F} ¿Por qué se revisa que las salidas de emergencia estén libres?", "Porque en una emergencia las personas deben poder salir sin obstáculos", "Porque así se ve más ordenado el pasillo", "Porque lo pide el proveedor de los extintores", "La salida libre protege la evacuación."),
        ("abc", "{F} ¿Qué parte de la lista revisa un estándar de la hoja de datos de seguridad?", "El punto «hojas de datos de seguridad disponibles»", "El punto «pisos secos»", "El punto «registro firmado»", "Ese punto comprueba que el documento esté a mano."),
        ("abc", "Una persona de la planta dice que, como vio un envase sin rótulo, lo va a «arreglar» rotulándolo por su cuenta según lo que parece. ¿Qué corresponde?", "No hacerlo: informar al responsable para que se identifique con la documentación", "Hacerlo, porque rotular es una tarea simple", "Abrirlo para saber qué contiene antes de rotular", "Un rótulo se coloca solo cuando se conoce el contenido con documentos."),
        ("=", "{F} Si la próxima ronda encuentra 1 solo punto incumplido de los 10, ¿qué porcentaje cumplirá?", "9*100//10", "Se dividen los puntos que cumplirían entre el total y se multiplica por 100.", " %"),
        em("Haces una ronda de inspección de ejemplo y ves que de una tubería sale vapor y que el piso de la zona está mojado con un líquido desconocido.", 2),
    ],
    ctx=("abc", "Un supervisor de ejemplo te dice: «No anotes los pisos mojados en la lista, ya los secamos». ¿Qué respondes?", "Que igual debe anotarse el hallazgo, porque el registro permite revisar y prevenir", "Que no se anota si ya se corrigió", "Que se anota solo si alguien se cayó", "El registro conserva el hallazgo y ayuda a prevenir que se repita."),
    sc=[
        ("En Química Industrial: ¿qué es un hallazgo?", "Lo que encuentra una ronda de inspección", "Puede cumplir o incumplir un estándar."),
        ("En Química Industrial: ¿quién corrige una no conformidad?", "El personal autorizado del área", "Quien vigila solo registra e informa a los responsables."),
        ("¿Cómo se calcula el puntaje de riesgo?", "Probabilidad por gravedad", "Combina cuán probable y cuán grave es el daño."),
    ],
    op=("Ronda ficticia en «Química Demo Costa Norte» con 8 puntos de lista: se incumplen «extintor con revisión vencida» (probabilidad 2, gravedad 5) y «cajas frente a una salida de emergencia» (probabilidad 3, gravedad 5). Escribe (a) cuántos puntos cumplen y qué porcentaje es, (b) los puntajes de los dos hallazgos y cuál se atiende primero, (c) qué debe hacer quien hace la ronda con cada hallazgo, (d) qué NO debe hacer por su cuenta.",
        "(a) Cumplen 6 de 8: 75 %. (b) Extintor: 10 puntos; cajas: 15 puntos; se atiende primero el de las cajas. (c) Registrarlos e informar al responsable del área. (d) No mover ni reparar por su cuenta ni intervenir equipos.",
        ["calcula el porcentaje de cumplimiento", "calcula y prioriza los puntajes", "describe el rol de vigilar", "reconoce lo que no debe hacer"],
        ["hoja con las cuatro respuestas"],
        ["priorizar por el menor puntaje", "creer que vigilar es corregir", "no informar"],
        "Pregunta: «¿quién corrige el hallazgo y quién lo informa?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una lista de 6 puntos de seguridad, marca cuáles cumplen y calcula el porcentaje de cumplimiento.",
    extend="Explica con un ejemplo por qué un hallazgo pequeño debe registrarse igual.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Informe mensual de eventos de la planta ficticia «Química Demo Valle Claro»: 3 cuasi accidentes, 1 incidente sin lesión y 1 accidente con lesión leve. "
     "Descripciones de algunos eventos y hallazgos del mes: (E1) un bidón vacío cae de un estante y no alcanza a nadie; (E2) una persona resbala en un pasillo mojado y se lastima un tobillo; (E3) una fuga leve de un envase deteriora el piso de la bodega sin que haya personas cerca; (E4) un extintor se encuentra descargado en una inspección. "
     "Código de colores de señalética de ejemplo: rojo = prohibición o equipo contra incendios; amarillo = advertencia de peligro; azul = obligación; verde = seguridad y evacuación. Roles de ejemplo: el trabajador informa lo que observa; el supervisor registra el evento; el prevencionista de riesgos investiga; el comité paritario colabora en la prevención.")
build(
    O4, 2, F,
    use="Aprenderé los conceptos y documentos de la vigilancia de seguridad: incidente, accidente, cuasi accidente, acción correctiva y preventiva, señalética y roles, usando un informe de eventos de ejemplo.",
    prior=["Sé qué es un hallazgo y una no conformidad.", "Sé calcular un porcentaje.", "Sé qué es una hoja de datos de seguridad."],
    explain=[
        "En Química Industrial, un accidente es un evento no deseado que causa lesión o daño; un incidente es un evento que pudo causar daño o lo causó a las cosas, pero no a las personas; y un cuasi accidente es un evento que estuvo a punto de causar daño y no lo causó por azar. Todos se informan, incluso los que no dejaron lesiones, porque muestran qué falla antes de que alguien se lastime.",
        "Una acción correctiva arregla lo que ya falló, como volver a cargar un extintor descargado; una acción preventiva busca que no vuelva a ocurrir, como programar revisiones periódicas. La señalética usa colores y formas con significado general: rojo para prohibición y equipos contra incendios, amarillo para advertencia, azul para obligación y verde para seguridad y evacuación. La hoja de datos de seguridad y el rótulo informan los peligros de cada producto y se leen, no se interpretan por cuenta propia.",
        f"Cada rol tiene su tarea: quien observa informa y quien tiene formación investiga y corrige. {EMER} {AVISO}",
    ],
    vocab=[("accidente", "evento no deseado que causa lesión o daño"), ("incidente", "evento que pudo causar daño o lo causó solo a las cosas"), ("cuasi accidente", "evento que estuvo a punto de causar daño y no lo causó"), ("acción correctiva", "acción que arregla lo que ya falló"), ("acción preventiva", "acción que busca que el problema no vuelva a ocurrir"), ("señalética", "señales con colores y formas que informan prohibiciones, advertencias, obligaciones y seguridad")],
    worked=[
        ("Clasificar un evento", "En una planta de ejemplo, una caja cae de un carro y casi golpea a una persona, que alcanza a apartarse. ¿Qué tipo de evento es?", ["Estuvo a punto de causar daño y no lo causó.", "Por lo tanto, es un cuasi accidente, y se informa igual."], "Cuasi accidente"),
        ("Correctiva y preventiva", "Un letrero de salida de emergencia se encuentra caído. Volver a colocarlo es una acción de un tipo; programar una revisión mensual de todos los letreros es otra. ¿De qué tipo es cada una?", ["Colocar el letrero arregla lo que falló: correctiva.", "Revisar cada mes busca que no vuelva a pasar: preventiva."], "Volver a colocarlo es correctiva y revisar cada mes es preventiva"),
    ],
    mistakes=[("Informar solo los eventos con lesión y callar los cuasi accidentes.", "Los cuasi accidentes avisan qué puede fallar antes de que alguien se lastime.", "Informa todo evento, aunque no haya daño."),
              ("Creer que una acción correctiva basta para evitar que el problema se repita.", "La correctiva arregla lo que ocurrió; la preventiva evita que vuelva a ocurrir.", "Pide ambas: corregir ahora y prevenir hacia adelante.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es un cuasi accidente?", "Un evento que estuvo a punto de causar daño y no lo causó", "Un accidente con lesión leve", "Un daño solo a las cosas", "El cuasi accidente no alcanza a producir daño."),
        ("abc", "En Química Industrial: ¿qué es una acción preventiva?", "La que busca que el problema no vuelva a ocurrir", "La que arregla lo que ya falló", "La que registra el accidente en el informe", "La preventiva actúa para evitar que el problema se repita."),
        ("abc", "En Química Industrial: ¿qué significa el amarillo en la señalética de ejemplo?", "Advertencia de peligro", "Prohibición", "Evacuación", "Según el código de la ficha, el amarillo advierte un peligro."),
        ("abc", "{F} ¿Qué tipo de evento es E2, donde una persona resbala y se lastima un tobillo?", "Un accidente", "Un cuasi accidente", "Una acción correctiva", "Hubo lesión, por eso es un accidente."),
        ("abc", "{F} ¿Qué tipo de evento es E1, el bidón vacío que cae sin alcanzar a nadie?", "Un cuasi accidente", "Un accidente", "Una acción preventiva", "Cayó sin dañar a nadie: estuvo cerca de causar daño."),
        ("=", "{F} ¿Cuántos eventos se informaron en total en el mes?", "3+1+1", "Se suman cuasi accidentes, incidentes y accidentes del informe.", " eventos"),
        ("=", "{F} ¿Qué porcentaje de los eventos del mes fueron cuasi accidentes?", "3*100//5", "Se dividen los cuasi accidentes entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} E4 es un extintor descargado. ¿Cuál es una acción correctiva?", "Que el personal autorizado recargue o reemplace el extintor", "Revisar todos los extintores cada mes", "Poner un letrero que diga «no usar»", "Corregir es arreglar lo que falló."),
        ("abc", "{F} ¿Cuál es una acción preventiva para evitar nuevos extintores descargados?", "Programar revisiones periódicas con registro", "Recargar solo el extintor que falló", "Anotar el hallazgo y no hacer nada más", "La prevención actúa sobre la causa y se mantiene en el tiempo."),
        ("abc", "{F} ¿Qué color de señalética de ejemplo corresponde a un letrero de salida de emergencia?", "Verde", "Rojo", "Azul", "El verde indica seguridad y evacuación."),
        ("abc", "{F} ¿Quién investiga las causas de un accidente, según los roles de la ficha?", "El prevencionista de riesgos", "El trabajador que lo presenció", "El supervisor, que solo lo registra", "El prevencionista tiene la tarea de investigar."),
        ("abc", "{F} Un trabajador dice: «no informé que el bidón casi me cae encima, porque no pasó nada». ¿Qué corresponde?", "Informarlo igual, porque los cuasi accidentes muestran fallas antes de que alguien se lastime", "No informar nada que no cause lesión", "Informar solo si el bidón estaba lleno", "Informar los cuasi accidentes ayuda a prevenir daños futuros."),
        em("Lees el informe de eventos de ejemplo cuando oyes que en la bodega un envase gotea un líquido y que alguien siente irritación en los ojos.", 3),
    ],
    ctx=("abc", "Un encargado de ejemplo te dice: «Si no hubo lesionados, no hace falta escribir el evento». ¿Qué respondes?", "Que igual se escribe, porque incidentes y cuasi accidentes muestran fallas antes de que ocurra un accidente", "Que tiene razón, porque no hay daño", "Que solo se escribe si ocurre de noche", "Registrar el evento sin lesión permite aprender y prevenir."),
    sc=[
        ("En Química Industrial: ¿qué diferencia hay entre accidente e incidente?", "El accidente causa lesión o daño; el incidente pudo causarlo o lo causó solo a las cosas", "Ambos se informan porque ayudan a prevenir futuros daños."),
        ("¿Qué significa el rojo en la señalética de ejemplo?", "Prohibición o equipo contra incendios", "El código de colores de la ficha lo define así."),
        ("En Química Industrial: ¿cuál es el rol del trabajador frente a un evento?", "Informar lo que observa", "Quien observa avisa; quien tiene formación investiga."),
    ],
    op=("Informe ficticio de «Química Demo Costa Norte»: (E1) una puerta de emergencia está trabada y se descubre en una revisión; (E2) una persona tropieza con una caja en el pasillo y no se lastima; (E3) una persona se corta una mano con un borde y necesita atención. Escribe (a) qué tipo de evento es cada uno, (b) una acción correctiva para E1, (c) una acción preventiva para E1, (d) qué debe hacer una persona que observa E2.",
        "(a) E1 es un hallazgo (incumple un estándar); E2, un cuasi accidente; E3, un accidente. (b) Que el personal autorizado destrabe y repare la puerta. (c) Programar revisiones periódicas de las puertas con registro. (d) Informar al supervisor, aunque no haya lesión.",
        ["clasifica los eventos", "propone una acción correctiva", "propone una acción preventiva", "indica que debe informar"],
        ["hoja con las cuatro respuestas"],
        ["confundir correctiva con preventiva", "no informar el cuasi accidente", "clasificar mal el accidente"],
        "Pregunta: «¿esta acción arregla lo ocurrido o evita que se repita?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe tres eventos de ejemplo de una planta y clasifícalos como accidente, incidente o cuasi accidente.",
    extend="Explica con un ejemplo por qué una acción preventiva es más duradera que una correctiva.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Tabla de hallazgos de una ronda en la planta ficticia «Química Demo Valle Claro» (puntaje = probabilidad × gravedad). "
     "H1: extintor sin revisión vigente, probabilidad 2 y gravedad 5, plazo de cierre 5 días. H2: cajas frente a una salida de emergencia, probabilidad 3 y gravedad 5, plazo 1 día. H3: envase sin rótulo, probabilidad 4 y gravedad 3, plazo 2 días. "
     "H4: piso mojado, probabilidad 4 y gravedad 2, plazo 3 días. H5: falta de señalética en la bodega, probabilidad 3 y gravedad 2, plazo 10 días. "
     "Regla de plazo de ejemplo: puntaje de 12 o más, plazo máximo de 2 días; de 8 a 11 puntos, máximo de 5 días; menos de 8 puntos, máximo de 10 días.")
build(
    O4, 3, F,
    use="Aprenderé a analizar en papel una tabla de hallazgos: calcular puntajes, ordenarlos por prioridad, comprobar los plazos de cierre y entender quién informa y quién corrige.",
    prior=["Sé calcular el puntaje de riesgo.", "Sé qué es un hallazgo y una no conformidad.", "Sé comparar números enteros."],
    explain=[
        "En Química Industrial, la tabla de hallazgos de una ronda ordena cada no conformidad con su puntaje, su plazo de cierre y su responsable. Se prioriza de mayor a menor puntaje: lo más grave y probable se atiende primero. El plazo de cierre es el tiempo máximo para corregir el hallazgo; entre más puntaje, menos plazo.",
        "Para revisar la tabla se calcula el puntaje de cada hallazgo, se ordena y se compara cada plazo con la regla. Si un plazo es mayor que el máximo permitido para su puntaje, se informa para que se reduzca. Si un hallazgo vence sin cerrarse, se avisa al responsable y al prevencionista. Quien vigila registra y da seguimiento a la tabla, pero no corrige por su cuenta.",
        f"Corregir un hallazgo, como mover cajas, recargar un extintor o retirar un envase, lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("tabla de hallazgos", "lista de no conformidades con puntaje, plazo y responsable"), ("prioridad", "orden de atención, de mayor a menor puntaje"), ("plazo de cierre", "tiempo máximo para corregir un hallazgo"), ("seguimiento", "revisión de que cada hallazgo se cierre en su plazo"), ("responsable", "persona del área a quien se informa y que gestiona la corrección")],
    worked=[
        ("Ordenar por prioridad", "Tres hallazgos de ejemplo tienen puntajes 6, 15 y 9. ¿En qué orden se atienden?", ["Se ordenan de mayor a menor.", "El orden es 15, 9 y 6."], "15, 9 y 6"),
        ("Revisar un plazo", "Un hallazgo de ejemplo tiene 10 puntos y un plazo de 7 días. La regla da máximo 5 días para 8 a 11 puntos. ¿Es correcto?", ["Con 10 puntos, el máximo permitido es 5 días.", "7 es mayor que 5, así que el plazo es demasiado largo."], "No: el plazo supera el máximo"),
    ],
    mistakes=[("Atender primero el hallazgo más fácil de arreglar en vez del de mayor puntaje.", "La prioridad la fija el riesgo, no la facilidad.", "Ordena por puntaje y atiende de mayor a menor."),
              ("Dejar que un hallazgo venza sin avisar porque «ya se sabe».", "Un hallazgo vencido sigue siendo un riesgo y requiere aviso.", "Avisa al responsable y al prevencionista cuando venza un plazo.")],
    T=[
        ("abc", "En Química Industrial: ¿cómo se ordenan los hallazgos por prioridad?", "De mayor a menor puntaje de riesgo", "Del más fácil al más difícil de arreglar", "Por orden alfabético", "La prioridad se decide según el riesgo que representa cada hallazgo."),
        ("abc", "En Química Industrial: ¿qué es el plazo de cierre?", "El tiempo máximo para corregir un hallazgo", "El tiempo que dura la ronda", "El horario del turno", "El plazo fija cuándo debe estar corregido el hallazgo."),
        ("abc", "En Química Industrial: ¿qué hace quien vigila cuando un hallazgo vence sin cerrarse?", "Avisa al responsable y al prevencionista", "Lo corrige por su cuenta", "Lo borra de la tabla", "Quien vigila informa; corregir es del personal autorizado."),
        ("=", "{F} ¿Qué puntaje tiene H3, el envase sin rótulo?", "4*3", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("=", "{F} ¿Qué puntaje tiene H2, las cajas frente a la salida?", "3*5", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("abc", "{F} ¿Qué hallazgo se atiende primero?", "H2, con 15 puntos", "H3, con 12 puntos", "H1, con 10 puntos", "H2 tiene el mayor puntaje de la tabla."),
        ("abc", "{F} ¿Cuál es el orden de atención completo?", "H2, H3, H1, H4, H5", "H1, H2, H3, H4, H5", "H5, H4, H3, H2, H1", "Los puntajes son 15, 12, 10, 8 y 6, de mayor a menor."),
        ("=", "{F} ¿Cuántos puntos suman los cinco hallazgos?", "10+15+12+8+6", "Se suman los puntajes de H1 a H5.", " puntos"),
        ("abc", "{F} ¿Cuál es el plazo máximo permitido para H1, con 10 puntos?", "5 días", "2 días", "10 días", "De 8 a 11 puntos, el máximo es 5 días según la regla."),
        ("abc", "{F} ¿Cumple la tabla la regla de plazos?", "Sí, porque cada plazo es menor o igual al máximo de su puntaje", "No, porque H2 tiene plazo de 1 día", "No, porque H5 tiene plazo de 10 días", "Los plazos de 5, 1, 2, 3 y 10 días respetan los máximos."),
        ("abc", "{F} Un encargado quiere atender primero H4 y H5 y mover las cajas de H2 «cuando alguien se acuerde». ¿Qué corresponde?", "Mantener el orden por puntaje y el plazo de 1 día para H2", "Aceptarlo, porque H2 se puede mover rápido", "Aceptarlo, porque solo H5 tiene plazo largo", "La prioridad y el plazo dependen del puntaje, no de la comodidad."),
        ("=", "{F} Si H4 se cierra en 3 días y el plazo máximo para su puntaje es 5 días, ¿cuántos días antes del máximo se cerró?", "5-3", "Se resta el plazo usado al máximo permitido.", " días"),
        em("Das seguimiento a una tabla de hallazgos de ejemplo cuando alguien avisa que en la bodega se cayeron cajas y que un envase está goteando.", 4),
    ],
    ctx=("abc", "El plazo de H2 vence mañana y las cajas siguen frente a la salida. ¿Qué debe hacer quien da seguimiento?", "Avisar hoy al responsable y al prevencionista para que personal autorizado las retire", "Mover las cajas él mismo para cumplir el plazo", "Esperar a que venza para avisar", "Quien vigila informa a tiempo; el retiro lo hace personal autorizado."),
    sc=[
        ("En Química Industrial: ¿cómo se prioriza una tabla de hallazgos?", "De mayor a menor puntaje", "Un mayor puntaje significa mayor riesgo y mayor urgencia."),
        ("¿Quién corrige un hallazgo?", "El personal autorizado del área", "Quien vigila registra y da seguimiento."),
        ("En Química Industrial: ¿qué se compara con la regla de plazos?", "El plazo de cada hallazgo con el máximo para su puntaje", "Los plazos largos para riesgos altos son incorrectos."),
    ],
    op=("Tabla ficticia de «Química Demo Costa Norte»: G1, extintor vencido, probabilidad 2 y gravedad 5, plazo 4 días; G2, piso mojado, probabilidad 4 y gravedad 2, plazo 8 días; G3, envase sin rótulo, probabilidad 3 y gravedad 4, plazo 2 días. Usa la regla de plazos de la clase (12 o más: máx. 2 días; 8 a 11: máx. 5 días; menos de 8: máx. 10 días). Escribe (a) los puntajes, (b) el orden de atención, (c) qué plazo no cumple la regla, (d) qué debe hacer quien da seguimiento.",
        "(a) G1: 10; G2: 8; G3: 12. (b) G3, G1 y G2. (c) El de G2: tiene 8 puntos y un plazo de 8 días, pero el máximo es 5 días. (d) Informar al responsable para que reduzca el plazo y dar seguimiento; no corregir por su cuenta.",
        ["calcula los puntajes", "ordena por prioridad", "aplica la regla de plazos", "describe el rol de seguimiento"],
        ["hoja con las cuatro respuestas"],
        ["ordenar al revés", "aceptar un plazo excesivo", "corregir por su cuenta"],
        "Pregunta: «¿cuál es el máximo para un puntaje de 8?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa cuatro hallazgos con probabilidad y gravedad, calcula los puntajes y ordénalos.",
    extend="Explica con un ejemplo por qué un plazo largo para un hallazgo de alto puntaje es un problema.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada). Resumen mensual de seguridad de la planta ficticia «Química Demo Valle Claro»: 50 trabajadores; 2 accidentes con lesión leve; 6 cuasi accidentes; 15 hallazgos de rondas, de los cuales 9 se cerraron a tiempo, 3 se cerraron con atraso y 3 siguen abiertos vencidos. "
     "Capacitación de seguridad vigente: 40 de los 50 trabajadores. Meta de ejemplo: cerrar a tiempo al menos el 80 % de los hallazgos. El último accidente fue hace 12 días. "
     "Fórmula de ejemplo: tasa de accidentes = accidentes por cada 100 trabajadores.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar indicadores de seguridad con datos de ejemplo: tasa de accidentes, porcentaje de hallazgos cerrados a tiempo, cobertura de capacitación y comparación con una meta.",
    prior=["Sé calcular porcentajes.", "Sé qué es un hallazgo y un plazo de cierre.", "Sé comparar un dato con una meta."],
    explain=[
        "En Química Industrial, un indicador de seguridad es un número que resume cómo va la prevención. La tasa de accidentes de este cuaderno es de ejemplo y se calcula como accidentes por cada 100 trabajadores: se multiplica por 100 y se divide entre el número de trabajadores. Sirve para comparar meses o áreas de distinto tamaño. El porcentaje de hallazgos cerrados a tiempo es los cerrados a tiempo entre el total, por 100.",
        "Una meta fija el valor que se quiere alcanzar. Para saber cuántos hallazgos faltan para llegar a la meta se calcula el número que exige la meta y se resta lo que ya se cumplió. La cobertura de capacitación compara los trabajadores con capacitación vigente con el total. Los indicadores no dicen por sí solos qué hacer: orientan y se informan al prevencionista de riesgos.",
        f"Estos cálculos son de planilla. Las acciones sobre el proceso las decide y ejecuta personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("indicador de seguridad", "número que resume cómo va la prevención"), ("tasa de accidentes (de ejemplo)", "accidentes por cada 100 trabajadores"), ("hallazgo cerrado a tiempo", "hallazgo corregido dentro de su plazo"), ("cobertura de capacitación", "porcentaje de trabajadores con capacitación vigente"), ("meta", "valor que se quiere alcanzar")],
    worked=[
        ("Tasa de accidentes", "Una planta de ejemplo tiene 25 trabajadores y 1 accidente en el mes. ¿Cuál es la tasa por cada 100 trabajadores?", ["Se multiplica 1 por 100 y se divide entre 25.", "100 entre 25 son 4."], "4 accidentes por cada 100 trabajadores"),
        ("Cuántos faltan para la meta", "De 20 hallazgos de ejemplo, 12 se cerraron a tiempo y la meta es 75 %. ¿Cuántos faltan para la meta?", ["La meta exige 75 por 20 entre 100, que son 15 hallazgos.", "15 menos 12 son 3."], "Faltan 3 hallazgos"),
    ],
    mistakes=[("Comparar el número de accidentes de dos áreas sin considerar cuántos trabajadores tiene cada una.", "Un área grande puede tener más accidentes aunque su tasa sea menor.", "Usa la tasa por cada 100 trabajadores."),
              ("Contar como «a tiempo» un hallazgo cerrado con atraso.", "Cerrado con atraso no cumple el plazo y distorsiona el indicador.", "Cuenta a tiempo solo los cerrados dentro del plazo.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es un indicador de seguridad?", "Un número que resume cómo va la prevención", "El nombre de un instrumento de medición", "Una norma de otro país", "El indicador resume datos para orientar."),
        ("abc", "En Química Industrial: ¿para qué sirve la tasa por cada 100 trabajadores?", "Para comparar meses o áreas de distinto tamaño", "Para saber cuántos trabajadores faltan", "Para reemplazar el registro de accidentes", "La tasa evita comparar números que dependen del tamaño."),
        ("abc", "En Química Industrial: ¿qué es la cobertura de capacitación?", "El porcentaje de trabajadores con capacitación vigente", "El número de horas de la capacitación", "El costo de los cursos", "La cobertura compara capacitados con el total."),
        ("=", "{F} ¿Cuál es la tasa de accidentes por cada 100 trabajadores?", "2*100//50", "Se multiplica por 100 y se divide entre el número de trabajadores.", " por cada 100"),
        ("=", "{F} ¿Qué porcentaje de los hallazgos se cerró a tiempo?", "9*100//15", "Se dividen los cerrados a tiempo entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos hallazgos debían cerrarse a tiempo para alcanzar la meta del 80 %?", "15*80//100", "Se calcula el 80 % del total de hallazgos.", " hallazgos"),
        ("=", "{F} ¿Cuántos hallazgos más debieron cerrarse a tiempo para llegar a la meta?", "15*80//100-9", "Se resta lo cumplido al número que exige la meta.", " hallazgos"),
        ("=", "{F} ¿Qué porcentaje de los trabajadores tiene capacitación vigente?", "40*100//50", "Se dividen los capacitados entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Se alcanzó la meta de cerrar a tiempo al menos el 80 % de los hallazgos?", "No, porque se cerró a tiempo solo el 60 %", "Sí, porque 9 es un número alto", "Sí, porque se cerraron 12 en total", "Solo los cerrados a tiempo cuentan para la meta."),
        ("=", "{F} ¿Cuántos trabajadores no tienen capacitación vigente?", "50-40", "Se resta los capacitados al total.", " trabajadores"),
        ("abc", "{F} Un jefe dice: «contemos los 3 hallazgos cerrados con atraso como a tiempo para llegar a la meta». ¿Qué corresponde?", "Rechazarlo: los cerrados con atraso no cuentan como a tiempo", "Aceptarlo, porque al final se cerraron", "Aceptarlo si el atraso fue de un solo día", "El indicador debe reflejar el cumplimiento real del plazo."),
        ("=", "{F} Otra planta de ejemplo tiene 20 trabajadores y 1 accidente. ¿Cuál es su tasa por cada 100 trabajadores?", "1*100//20", "Se multiplica por 100 y se divide entre el número de trabajadores.", " por cada 100"),
        em("Calculas indicadores de seguridad de ejemplo cuando alguien avisa que se rompió una tubería y que cae un líquido desconocido sobre el piso del taller.", 5),
    ],
    ctx=("abc", "Una jefatura de ejemplo dice: «si no hubo accidentes con lesión este mes, podemos dejar de registrar cuasi accidentes». ¿Qué respondes?", "Que se siguen registrando, porque avisan qué puede fallar antes de que ocurra un accidente", "Que tiene razón, porque el indicador ya es bueno", "Que solo se registran en otoño", "Los cuasi accidentes son una señal temprana de riesgo."),
    sc=[
        ("En Química Industrial: ¿cómo se calcula la tasa de accidentes de ejemplo?", "Accidentes por 100 entre los trabajadores", "Así se compara entre grupos de distinto tamaño."),
        ("En Química Industrial: ¿cuántos hallazgos exige una meta del 50 % si hay 20?", "10 hallazgos", "El 50 % de 20 es la mitad."),
        ("¿Cuenta como «a tiempo» un hallazgo cerrado con atraso?", "No, porque no cumplió el plazo", "A tiempo significa dentro del plazo fijado."),
    ],
    op=("Planilla ficticia de «Química Demo Costa Norte»: 40 trabajadores; 2 accidentes con lesión leve; 10 hallazgos de rondas, 6 cerrados a tiempo; capacitación vigente en 30 trabajadores; meta de ejemplo: cerrar a tiempo al menos el 70 % de los hallazgos. Escribe (a) la tasa de accidentes por cada 100 trabajadores, (b) el porcentaje de hallazgos cerrados a tiempo, (c) cuántos hallazgos más se debían cerrar a tiempo para la meta, (d) la cobertura de capacitación.",
        "(a) 2 por 100 entre 40 son 5 por cada 100. (b) 6 de 10 son 60 %. (c) La meta exige 7 hallazgos; faltaba 1. (d) 30 de 40 son 75 %.",
        ["calcula la tasa", "calcula el porcentaje de cierre", "calcula lo que faltaba para la meta", "calcula la cobertura"],
        ["hoja con los cuatro cálculos"],
        ["dividir sin multiplicar por 100", "contar los cierres con atraso", "no restar lo cumplido"],
        "Pregunta: «¿cuántos hallazgos exige la meta?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una planilla con trabajadores, accidentes y hallazgos, y calcula la tasa y el porcentaje de cierre a tiempo.",
    extend="Explica con un ejemplo por qué un indicador bueno no significa que no haya riesgo.",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Hallazgo H7 de la planta ficticia «Química Demo Valle Claro»: cajas apiladas frente a una salida de emergencia. Tres alternativas de acción: Alternativa A, que personal autorizado reubique las cajas en otro sector (costo de ejemplo $30.000, plazo 1 día); "
     "Alternativa B, colocar un letrero «no obstruir» y dejar las cajas donde están (costo de ejemplo $10.000, plazo 1 día); Alternativa C, pedir a las personas que tengan cuidado al pasar (costo $0, plazo inmediato). "
     "Regla de ejemplo (jerarquía de controles): es mejor la medida que elimina la causa del peligro que la que solo avisa o pide cuidado. "
     "Verificación del cierre de 10 acciones del mes: 7 tienen evidencia y verificación por otra persona; 2 no tienen verificación; 1 no tiene evidencia.")
build(
    O4, 5, F,
    use="Aprenderé a comparar acciones correctivas según su eficacia, costo y plazo, y a verificar la calidad del cierre de los hallazgos con evidencia y verificación independiente.",
    prior=["Sé qué es una acción correctiva y una preventiva.", "Sé calcular porcentajes.", "Sé comparar costos."],
    explain=[
        "En Química Industrial, al comparar acciones para un hallazgo no basta con elegir la más barata: se considera si eliminan la causa del peligro. La jerarquía de controles ordena las medidas de la más eficaz a la menos eficaz: primero eliminar la fuente del peligro, luego sustituir o aislar, luego avisar con letreros y procedimientos, y al final pedir cuidado o usar protección personal. Una medida que solo avisa no quita el peligro.",
        "Un hallazgo se cierra cuando la acción se hizo y hay evidencia, que es un registro de lo realizado, y cuando otra persona verifica que el problema quedó resuelto. El porcentaje de cierres verificados es un indicador de calidad. Un cierre sin evidencia ni verificación vuelve a quedar abierto.",
        f"Quien vigila no ejecuta la acción: la ejecuta personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("jerarquía de controles", "orden de las medidas, de la más eficaz a la menos eficaz"), ("eliminar la causa", "quitar la fuente del peligro"), ("evidencia", "registro de que la acción se realizó"), ("verificación independiente", "revisión de otra persona de que el problema quedó resuelto"), ("cierre de un hallazgo", "paso final cuando hay acción, evidencia y verificación")],
    worked=[
        ("Elegir según la jerarquía", "En una bodega de ejemplo hay una escalera abierta en el pasillo. Alternativa 1: guardarla en su lugar. Alternativa 2: poner un letrero «cuidado escalera». ¿Cuál es mejor?", ["Guardarla elimina la causa del peligro.", "El letrero solo avisa."], "La alternativa 1"),
        ("Cierre verificado", "De 8 acciones de ejemplo, 6 tienen evidencia y verificación. ¿Qué porcentaje de cierres verificados hay?", ["Se divide 6 entre 8 y se multiplica por 100.", "6 por 100 son 600, y 600 entre 8 son 75."], "75 %"),
    ],
    mistakes=[("Elegir un letrero porque es más barato que quitar el peligro.", "El letrero no elimina la causa; el riesgo sigue.", "Prefiere la medida que elimina la causa y usa letreros solo como complemento."),
              ("Cerrar un hallazgo con solo la firma de quien hizo la acción.", "Falta evidencia y una verificación de otra persona.", "Pide el registro de la acción y la revisión de un tercero.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es mejor según la jerarquía de controles?", "Eliminar la causa del peligro", "Poner un letrero de advertencia", "Pedir a las personas que tengan cuidado", "Eliminar la fuente es la medida más eficaz."),
        ("abc", "En Química Industrial: ¿qué es la evidencia de una acción?", "Un registro de que la acción se realizó", "Una opinión de quien la hizo", "El costo de la acción", "La evidencia permite comprobar lo realizado."),
        ("abc", "En Química Industrial: ¿qué es una verificación independiente?", "La revisión de otra persona de que el problema quedó resuelto", "La firma de quien hizo la acción", "Un cálculo del costo", "Verifica una persona distinta de quien ejecutó."),
        ("=", "{F} ¿Cuántos pesos más cuesta la alternativa A que la B?", "30000-10000", "Se resta el costo de la B al de la A.", " pesos"),
        ("abc", "{F} ¿Qué alternativa elimina la causa del peligro?", "La A, que reubica las cajas", "La B, que pone un letrero", "La C, que pide cuidado", "Solo la A quita las cajas de la salida."),
        ("abc", "{F} ¿Qué alternativa es la mejor según la jerarquía de controles?", "La A, aunque cueste más", "La B, porque es más barata que la A", "La C, porque no cuesta nada", "La jerarquía prefiere eliminar la causa antes que avisar."),
        ("abc", "{F} ¿Por qué la alternativa B no es suficiente?", "Porque el letrero avisa pero deja las cajas bloqueando la salida", "Porque su plazo es más largo", "Porque su costo es mayor que el de la A", "Un letrero no quita el obstáculo."),
        ("=", "{F} ¿Qué porcentaje de las 10 acciones del mes tiene evidencia y verificación?", "7*100//10", "Se dividen las acciones completas entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas acciones del mes no tienen verificación ni evidencia completas?", "2+1", "Se suman las que no tienen verificación y la que no tiene evidencia.", " acciones"),
        ("abc", "{F} Una de las acciones sin verificación figura como «cerrada». ¿Qué corresponde?", "Reabrirla hasta que otra persona verifique", "Dejarla cerrada porque fue firmada", "Cerrar también la que no tiene evidencia", "Sin verificación independiente el cierre no está completo."),
        ("=", "{F} Si se verifican las 3 acciones pendientes, ¿cuántas de las 10 tendrán evidencia y verificación?", "7+3", "Se suman las completas y las que se verifican.", " acciones"),
        ("abc", "{F} Un compañero ofrece mover él mismo las cajas «para cumplir el plazo del hallazgo». ¿Qué corresponde?", "Avisar al responsable para que lo haga personal autorizado", "Aceptar, porque mover cajas es sencillo", "Mover solo las cajas más livianas", "Quien vigila no ejecuta la corrección por su cuenta."),
        em("Comparas acciones en una oficina de la planta cuando alguien avisa que un estante de la bodega se cayó y que sale un olor fuerte de un envase roto.", 0),
    ],
    ctx=("abc", "Un jefe de ejemplo te dice: «Cierra el hallazgo, ya firmé la acción». No hay registro ni nadie más revisó. ¿Qué respondes?", "Que falta la evidencia y la verificación de otra persona antes de cerrarlo", "Que se cierra con su firma", "Que se cierra y se pide la evidencia el mes siguiente", "El cierre exige acción, evidencia y verificación independiente."),
    sc=[
        ("En Química Industrial: ¿qué se prefiere según la jerarquía de controles?", "Eliminar la causa del peligro", "Es la medida más eficaz de la jerarquía."),
        ("En Química Industrial: ¿qué necesita un hallazgo para cerrarse?", "Acción, evidencia y verificación", "Los tres elementos aseguran que el problema quedó resuelto."),
        ("¿Quién ejecuta la corrección de un hallazgo?", "Personal autorizado", "Quien vigila no corrige por su cuenta."),
    ],
    op=("Hallazgo ficticio en «Química Demo Costa Norte»: un pasillo tiene un charco que no se sabe de dónde viene. Alternativa 1: colocar un letrero de «piso resbaladizo». Alternativa 2: informar para que personal autorizado detecte el origen y lo repare. Alternativa 3: pedir a todos que caminen despacio. Escribe (a) cuál es la mejor según la jerarquía de controles y por qué, (b) qué debe hacer quien ve el charco, (c) qué necesita el hallazgo para cerrarse, (d) por qué el letrero solo no basta.",
        "(a) La alternativa 2, porque busca eliminar la causa. (b) No acercarse a una posible fuga ni limpiar, avisar de inmediato a un adulto responsable y a emergencias. (c) Acción, evidencia y verificación independiente. (d) Porque el letrero avisa, pero el charco y su causa siguen.",
        ["aplica la jerarquía", "indica el rol de quien observa", "nombra los requisitos del cierre", "explica por qué el letrero no basta"],
        ["hoja con las cuatro respuestas"],
        ["elegir por costo", "intervenir por su cuenta", "cerrar sin verificación"],
        "Pregunta: «¿qué alternativa quita el charco de raíz?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un hallazgo con tres acciones posibles y ordénalas de la más eficaz a la menos eficaz.",
    extend="Explica con un ejemplo por qué la verificación debe hacerla una persona distinta.",
)

# ============================================================ OAE-05, clase 1
O5 = "TP-QUIN-3-OAE-05"
F = ("Ficha 1 (caso de ejemplo, inventado). La empresa ficticia «Química Demo Valle Claro» genera en un mes (datos de ejemplo): 1.200 kg de residuos sólidos no peligrosos (cartón, plástico y papel); 300 kg de residuos sólidos peligrosos (envases contaminados); "
     "500 L de residuos líquidos peligrosos; y 2.000 L de residuos líquidos de proceso que van a la planta de tratamiento de la empresa. La bodega de residuos peligrosos tiene acceso restringido y una capacidad de ejemplo de 400 kg de sólidos. "
     "El retiro lo hace una empresa autorizada que entrega un registro del retiro. Un tambor de ejemplo admite 200 L. La planta de tratamiento procesa 400 L por día (de ejemplo).")
build(
    O5, 1, F,
    use="Aprenderé qué son los residuos industriales sólidos y líquidos, por qué se separan y se rotulan, quién los retira y por qué ante un derrame no se actúa sin formación sino que se avisa.",
    prior=["Sé qué es un rótulo y un registro.", "Sé sumar, dividir y calcular porcentajes sencillos.", "Sé qué es una condición obligatoria."],
    explain=[
        "En Química Industrial, un residuo industrial es un material que la planta genera y ya no usa, y puede ser sólido o líquido. Un residuo peligroso es el que, por sus características, puede dañar a las personas o al ambiente; la norma vigente y la hoja de datos de seguridad indican cuáles son. Los residuos se separan según su tipo (segregación en el origen), se rotulan, se guardan en una bodega de residuos y los retira una empresa autorizada que deja un registro. La autoridad sanitaria y la ambiental fiscalizan este camino.",
        "El recorrido de un residuo tiene etapas: generación, segregación, rotulado, almacenamiento temporal, retiro y disposición final en un lugar autorizado. Cada etapa deja un registro, y así se puede seguir el residuo de principio a fin. Tirar un residuo líquido por el desagüe o a un sitio no autorizado es un incumplimiento grave y un riesgo para las personas y el ambiente.",
        f"La empresa tiene un plan de contingencia para derrames, y solo el personal formado lo aplica. Quien no está capacitado no actúa: se aleja y avisa. {EMER} {AVISO}",
    ],
    vocab=[("residuo industrial", "material que la planta genera y ya no usa"), ("residuo peligroso", "residuo que puede dañar a las personas o al ambiente por sus características"), ("segregación en el origen", "separar los residuos según su tipo desde donde se generan"), ("bodega de residuos", "lugar señalado para guardar temporalmente los residuos"), ("empresa autorizada", "empresa con permiso vigente para retirar y llevar residuos"), ("disposición final", "destino definitivo del residuo en un lugar autorizado")],
    worked=[
        ("Porcentaje de residuos peligrosos", "En un mes de ejemplo, una planta genera 150 kg de residuos sólidos, de los cuales 45 kg son peligrosos. ¿Qué porcentaje es peligroso?", ["Se divide 45 entre 150 y se multiplica por 100.", "45 por 100 son 4.500, y 4.500 entre 150 son 30."], "30 %"),
        ("Tambores necesarios", "Una planta de ejemplo tiene 700 L de residuo líquido y cada tambor admite 200 L. ¿Cuántos tambores se necesitan si se redondea hacia arriba?", ["700 entre 200 son 3 y sobran 100 L.", "Los 100 L restantes también ocupan un tambor, así que son 4."], "4 tambores"),
    ],
    mistakes=[("Botar un residuo líquido por el desagüe «porque son pocos litros».", "Un residuo líquido peligroso no se elimina por el desagüe; se segrega, se rotula y lo retira una empresa autorizada.", "Entrega el residuo al responsable de la bodega de residuos para su retiro."),
              ("Creer que solo los líquidos pueden ser residuos peligrosos.", "También son peligrosos algunos sólidos, como envases contaminados.", "Revisa el tipo de residuo con el rótulo y la hoja de datos de seguridad.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es un residuo industrial?", "Un material que la planta genera y ya no usa", "Un producto terminado que se vende", "Un instrumento averiado", "Un residuo es lo que la planta descarta."),
        ("abc", "En Química Industrial: ¿qué es un residuo peligroso?", "Uno que por sus características puede dañar a las personas o al ambiente", "Uno que pesa mucho", "Uno que no tiene valor comercial", "La peligrosidad depende del daño posible, no del peso ni del valor."),
        ("abc", "En Química Industrial: ¿por qué se separan los residuos según su tipo?", "Porque mezclarlos puede aumentar el riesgo y dificulta su retiro y disposición", "Porque así ocupan más espacio", "Porque lo pide el proveedor de insumos", "La segregación reduce el riesgo y facilita el manejo."),
        ("=", "{F} ¿Cuántos kg de residuos sólidos se generaron en total en el mes?", "1200+300", "Se suman los sólidos no peligrosos y los peligrosos.", " kg"),
        ("=", "{F} ¿Qué porcentaje de los residuos sólidos del mes es peligroso?", "300*100//1500", "Se dividen los sólidos peligrosos entre el total de sólidos y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos kg más caben en la bodega de residuos peligrosos si ya contiene los 300 kg del mes?", "400-300", "Se resta lo almacenado a la capacidad.", " kg"),
        ("abc", "{F} ¿Quién retira los residuos peligrosos de la empresa?", "Una empresa autorizada que entrega un registro del retiro", "Cualquier camión de la planta", "El proveedor de los insumos sin registro", "Solo una empresa autorizada y con registro asegura la trazabilidad."),
        ("abc", "{F} Un operario propone botar los 500 L de residuo líquido peligroso al desagüe «porque son pocos». ¿Qué corresponde?", "No: se segregan, se rotulan y los retira una empresa autorizada", "Sí, si lo hace de noche", "Sí, si el desagüe va al alcantarillado de la planta", "Los residuos líquidos peligrosos no se eliminan por el desagüe."),
        ("=", "{F} ¿Cuántos tambores se necesitan para los 500 L de residuo líquido peligroso? Redondea hacia arriba.", "(500+199)//200", "Se divide entre 200 L y se redondea hacia arriba porque 100 L también ocupan un tambor.", " tambores"),
        ("=", "{F} ¿Cuántos días tarda la planta de tratamiento en procesar los 2.000 L de residuo líquido de proceso?", "2000//400", "Se divide el volumen entre lo que procesa por día.", " días"),
        ("abc", "{F} ¿Por qué la bodega de residuos peligrosos tiene acceso restringido?", "Porque solo debe entrar personal autorizado por el riesgo de lo que guarda", "Porque así se ve más ordenada", "Porque está lejos de la oficina", "El acceso se limita por el riesgo de los residuos."),
        ("abc", "{F} Un compañero dice: «los residuos peligrosos son solo los líquidos». ¿Es correcto?", "No: también hay sólidos peligrosos, como los envases contaminados de la ficha", "Sí, porque los sólidos nunca son peligrosos", "Sí, pero solo si son más de 100 kg", "La ficha incluye 300 kg de sólidos peligrosos."),
        em("Lees la ficha de residuos de ejemplo en una oficina cuando alguien avisa que un tambor de la bodega de residuos se volcó y que el líquido se esparce por el piso.", 0),
    ],
    ctx=("abc", "Un operario de ejemplo te dice: «Hay un charco de un residuo líquido en la bodega; ayúdame a limpiarlo rápido antes de que llegue el jefe». ¿Qué respondes?", "Que no te acercas, y que se debe avisar a un adulto responsable y a emergencias porque lo atiende personal formado", "Que sí, si usas guantes", "Que sí, pero solo con papel absorbente", "Un derrame lo maneja personal formado según el plan de contingencia."),
    sc=[
        ("En Química Industrial: ¿qué es la disposición final?", "El destino definitivo del residuo en un lugar autorizado", "Es la última etapa del recorrido del residuo."),
        ("En Química Industrial: ¿quién retira los residuos peligrosos de la planta?", "Una empresa autorizada con registro", "Así se puede seguir el residuo hasta su destino."),
        ("En Química Industrial: ¿qué se hace al ver un derrame sin ser personal formado?", "Alejarse y avisar", "Solo personal formado aplica el plan de contingencia."),
    ],
    op=("Caso ficticio de «Química Demo Costa Norte»: en un mes se generan 800 kg de residuos sólidos no peligrosos, 200 kg de residuos sólidos peligrosos y 600 L de residuos líquidos peligrosos, y la bodega de residuos peligrosos admite 300 kg de sólidos. Escribe (a) el total de sólidos y qué porcentaje es peligroso, (b) cuántos kg libres quedan en la bodega, (c) quién debe retirar los residuos peligrosos y qué documento debe quedar, (d) qué debe hacer una persona sin formación que ve un derrame.",
        "(a) 1.000 kg en total; 200 por 100 entre 1.000 son 20 %. (b) 300 menos 200 son 100 kg. (c) Una empresa autorizada, con un registro del retiro. (d) No acercarse, avisar a un adulto responsable y a emergencias.",
        ["calcula total y porcentaje", "calcula la capacidad libre", "nombra a quien retira y el registro", "indica la conducta ante un derrame"],
        ["hoja con las cuatro respuestas"],
        ["no sumar los sólidos", "creer que cualquiera retira", "intervenir en el derrame"],
        "Pregunta: «¿qué haces si ves un derrame y no eres personal formado?». Si no responde, pídele que relea el tercer párrafo de la explicación."),
    reinforce="Inventa tres tipos de residuos de una planta con su cantidad y di cuáles serían peligrosos y cuál sería el recorrido de uno de ellos.",
    extend="Explica con un ejemplo por qué mezclar residuos de distinto tipo puede aumentar el riesgo.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Registro de retiro N.º R-0457 (de ejemplo) de la empresa ficticia «Química Demo Valle Claro». Residuo: sólido peligroso (envases contaminados). Cantidad generada en el mes: 300 kg. Cantidad retirada: 240 kg. "
     "Transportista: «Transportes Demo Ltda.» (autorizado, de ejemplo). Destino: «Sitio Demo de disposición autorizado». Costo del retiro: $600 por kg (de ejemplo). Firmas: generador y transportista. "
     "Datos del rótulo del residuo: tipo, origen, fecha de generación y responsable. Roles de ejemplo: el generador (la empresa) es responsable de su residuo hasta la disposición final; el transportista autorizado lo traslada; el sitio autorizado lo recibe y lo dispone; el encargado ambiental lleva los registros.")
build(
    O5, 2, F,
    use="Aprenderé los documentos y roles del manejo de residuos: rótulo del residuo, registro de retiro, trazabilidad, jerarquía de gestión y responsabilidades del generador, el transportista y el sitio de disposición.",
    prior=["Sé qué es un residuo peligroso.", "Sé qué es la trazabilidad.", "Sé calcular costos y porcentajes."],
    explain=[
        "En Química Industrial, el rótulo de un residuo debe indicar su tipo, su origen, la fecha de generación y el responsable. El registro de retiro es el documento que deja constancia de qué residuo se retiró, cuánto, quién lo transportó y a qué lugar fue. Con estos documentos hay trazabilidad: se puede seguir el residuo desde que se genera hasta su disposición final. El generador, que es la empresa que produce el residuo, sigue siendo responsable hasta que el sitio autorizado lo recibe.",
        "Además existe una jerarquía de gestión de residuos: primero se previene o reduce lo que se genera, luego se reutiliza, después se recicla o valoriza y, al final, lo que no puede aprovecharse va a disposición final. Cada decisión depende de las condiciones que fija la norma vigente y de lo que informe la autoridad sanitaria y ambiental. Los registros se guardan y no se alteran.",
        f"Esta clase trabaja con documentos de ejemplo en papel; manipular residuos es tarea de personal formado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("rótulo de residuo", "etiqueta con tipo, origen, fecha de generación y responsable"), ("registro de retiro", "documento que deja constancia de qué se retiró, cuánto, quién y hacia dónde"), ("generador", "empresa que produce el residuo y responde por él hasta su disposición final"), ("transportista autorizado", "empresa con permiso vigente para trasladar residuos"), ("reciclar", "convertir un residuo en un material que se puede volver a usar"), ("valorizar", "aprovechar un residuo para obtener un beneficio")],
    worked=[
        ("Residuo pendiente", "Una empresa de ejemplo generó 500 kg de un residuo y el registro de retiro indica 420 kg retirados. ¿Cuántos kg quedan en la bodega?", ["Se resta lo retirado a lo generado.", "500 menos 420 son 80."], "Quedan 80 kg"),
        ("Costo del retiro", "Un retiro de ejemplo de 150 kg cuesta $400 por kg. ¿Cuál es el costo total?", ["Se multiplica la cantidad por el precio por kg.", "150 por 400 son 60.000."], "$60.000"),
    ],
    mistakes=[("Rotular un residuo solo con la palabra «residuo».", "El rótulo debe indicar tipo, origen, fecha y responsable para poder seguirlo.", "Completa los cuatro datos en cada rótulo."),
              ("Pensar que la empresa deja de ser responsable al entregar el residuo al camión.", "El generador responde hasta que el sitio autorizado lo recibe y lo dispone.", "Guarda el registro hasta confirmar la disposición final.")],
    T=[
        ("abc", "En Química Industrial: ¿qué datos debe tener el rótulo de un residuo?", "Tipo, origen, fecha de generación y responsable", "Solo el nombre de la empresa", "Solo la fecha del retiro", "El rótulo completo permite seguir el residuo."),
        ("abc", "En Química Industrial: ¿qué es un registro de retiro?", "El documento que deja constancia de qué se retiró, cuánto, quién y hacia dónde", "Una factura de compra de insumos", "Un plano de la bodega de residuos", "El registro de retiro respalda la trazabilidad."),
        ("abc", "En Química Industrial: ¿qué es el generador de un residuo?", "La empresa que lo produce y responde por él hasta su disposición final", "La empresa que lo transporta", "El sitio que lo recibe", "El generador mantiene su responsabilidad hasta el final."),
        ("=", "{F} ¿Cuántos kg del residuo siguen en la bodega después del retiro?", "300-240", "Se resta la cantidad retirada a la generada.", " kg"),
        ("=", "{F} ¿Qué porcentaje de lo generado se retiró?", "240*100//300", "Se divide lo retirado entre lo generado y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuánto costó el retiro?", "240*600", "Se multiplica la cantidad retirada por el costo por kg.", " pesos"),
        ("abc", "{F} ¿Quién traslada el residuo, según el registro?", "El transportista autorizado", "El sitio de disposición", "El encargado ambiental", "El registro nombra a «Transportes Demo Ltda.» como transportista."),
        ("abc", "{F} ¿Quién lleva los registros dentro de la empresa, según los roles?", "El encargado ambiental", "El transportista", "El sitio de disposición", "La ficha asigna los registros al encargado ambiental."),
        ("abc", "{F} El registro solo trae la firma del generador. ¿Qué corresponde?", "Pedir también la firma del transportista, porque el registro debe tener ambas", "Aceptarlo, porque la empresa es la responsable", "Firmar por el transportista para completar", "La ficha indica firmas del generador y del transportista."),
        ("abc", "{F} ¿Hasta cuándo el generador es responsable de su residuo?", "Hasta que el sitio autorizado lo recibe y lo dispone", "Hasta que el camión sale de la planta", "Hasta fin de mes", "El generador responde hasta la disposición final."),
        ("abc", "En la jerarquía de gestión, ¿cuál es la primera opción?", "Prevenir o reducir lo que se genera", "Enviar todo a disposición final", "Reciclar sin mirar el tipo de residuo", "Lo mejor es generar menos antes de gestionar lo generado."),
        ("=", "{F} Si el resto de los kg que faltan por retirar se retira a $600 por kg, ¿cuánto costará ese segundo retiro?", "(300-240)*600", "Se calcula primero lo que falta por retirar y se multiplica por el costo por kg.", " pesos"),
        em("Revisas un registro de retiro de ejemplo cuando alguien avisa que en la bodega de residuos hay un olor fuerte y que un envase está goteando.", 1),
    ],
    ctx=("abc", "Una persona de ejemplo ofrece retirar los residuos peligrosos «a mitad de precio» pero no muestra autorización ni entrega registro. ¿Qué corresponde?", "Rechazar la oferta, porque falta la condición obligatoria de autorización y registro", "Aceptar, porque ahorra dinero", "Aceptar, y pedir el registro después", "Sin autorización ni registro se pierde la trazabilidad y se incumple la norma."),
    sc=[
        ("En Química Industrial: ¿qué es la trazabilidad de un residuo?", "Poder seguir el residuo desde su generación hasta su disposición final", "Se logra con rótulos y registros."),
        ("En Química Industrial: ¿cuál es la primera opción de la jerarquía de gestión?", "Prevenir o reducir", "Generar menos es mejor que gestionar mucho."),
        ("¿Quién firma el registro de retiro de la ficha?", "El generador y el transportista", "Ambas firmas dan constancia del traspaso."),
    ],
    op=("Registro ficticio de retiro R-1102 de «Química Demo Costa Norte»: residuo sólido peligroso, 150 kg generados, 100 kg retirados, costo de $500 por kg, transportista autorizado, destino autorizado, firma del generador pero sin firma del transportista. Escribe (a) cuántos kg quedan por retirar, (b) el costo del retiro, (c) qué falta en el registro, (d) hasta cuándo es responsable el generador.",
        "(a) 50 kg. (b) 100 por 500 son 50.000 pesos. (c) Falta la firma del transportista. (d) Hasta que el sitio autorizado recibe y dispone el residuo.",
        ["calcula lo pendiente", "calcula el costo", "detecta la omisión", "indica la responsabilidad del generador"],
        ["hoja con las cuatro respuestas"],
        ["no restar", "no detectar la firma faltante", "creer que la responsabilidad termina con el retiro"],
        "Pregunta: «¿quién debería firmar además del generador?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un registro de retiro con residuo, cantidad generada y retirada, transportista, destino y costo, y revisa que no falte ningún dato.",
    extend="Explica con un ejemplo por qué la jerarquía de gestión prefiere reducir antes que reciclar.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Residuos sólidos peligrosos generados por la planta ficticia «Química Demo Valle Claro» en 4 meses, en kg: marzo 300; abril 320; mayo 340; junio 360. "
     "La bodega de residuos tiene una capacidad de 400 kg. Hoy contiene 150 kg y se agregan 10 kg por día (datos de ejemplo). El plazo máximo de almacenamiento de ejemplo es de 30 días (en la realidad lo fija la norma vigente). "
     "El retiro está programado dentro de 28 días. El plan de contingencia de la empresa nombra a las personas formadas que responden ante un derrame; el resto del personal se aleja y avisa.")
build(
    O5, 3, F,
    use="Aprenderé a analizar en papel un caso de residuos: ver la tendencia de generación, calcular cuándo se llenaría la bodega, programar el retiro antes del llenado y entender quién atiende un derrame.",
    prior=["Sé calcular una tendencia y un porcentaje.", "Sé qué es un registro de retiro.", "Sé qué es un plan de contingencia."],
    explain=[
        "En Química Industrial, la capacidad de una bodega de residuos es lo máximo que puede guardar. Para saber cuándo se llenará, se calcula el espacio libre y se divide entre lo que se agrega por día. Con eso se programa el retiro antes del llenado y antes del plazo máximo de almacenamiento, que fija la norma vigente. Una bodega llena o con residuos fuera de plazo es un riesgo y un incumplimiento.",
        "La generación de residuos puede subir, bajar o mantenerse; la tendencia se observa mes a mes con una tabla. Si sube, hay que revisar la causa, planificar más retiros o reducir lo que se genera. El plan de contingencia de la empresa define quién responde ante un derrame o un incidente con residuos, con qué formación y con qué equipos. Quien no está formado no responde: se aleja de la zona de riesgo y avisa.",
        f"Este análisis es de planilla; manipular residuos y atender derrames es tarea de personal formado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("capacidad", "cantidad máxima que puede guardar una bodega"), ("espacio libre", "capacidad menos lo que ya contiene"), ("plazo máximo de almacenamiento", "tiempo máximo que un residuo puede estar guardado"), ("plan de contingencia", "plan de la empresa que define quién responde ante un derrame o incidente"), ("tendencia de generación", "forma en que cambia la generación de residuos mes a mes")],
    worked=[
        ("Días hasta llenarse", "Una bodega de ejemplo tiene capacidad de 500 kg, contiene 200 kg y recibe 15 kg por día. ¿En cuántos días se llena?", ["El espacio libre es 500 menos 200, es decir, 300 kg.", "300 entre 15 son 20."], "En 20 días"),
        ("Tendencia", "Una generación de ejemplo fue 100, 110, 120 y 130 kg en cuatro meses. ¿Qué tendencia hay?", ["Cada mes sube 10 kg.", "Es una tendencia creciente pareja."], "Sube 10 kg por mes"),
    ],
    mistakes=[("Programar el retiro para después del día en que la bodega se llenaría.", "Con la bodega llena no se pueden guardar más residuos de forma segura.", "Calcula los días hasta el llenado y programa el retiro antes."),
              ("Creer que cualquier persona puede atender un derrame «porque solo hay que limpiar».", "Un derrame lo atiende personal formado según el plan de contingencia.", "Si no estás formado, aléjate y avisa.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es el espacio libre de una bodega de residuos?", "La capacidad menos lo que ya contiene", "La capacidad total", "Lo que se retiró el mes pasado", "El espacio libre se calcula restando lo guardado a la capacidad."),
        ("abc", "En Química Industrial: ¿qué es un plan de contingencia?", "El plan de la empresa que define quién responde ante un derrame o incidente", "El calendario de vacaciones del personal", "Una lista de precios de los retiros", "El plan de contingencia asigna roles de respuesta."),
        ("abc", "En Química Industrial: ¿por qué hay un plazo máximo de almacenamiento?", "Porque guardar residuos demasiado tiempo aumenta el riesgo", "Porque los residuos pierden su color", "Porque la bodega cierra por la tarde", "Un residuo guardado de más aumenta el riesgo y es incumplimiento."),
        ("=", "{F} ¿Cuántos kg de espacio libre tiene hoy la bodega?", "400-150", "Se resta lo que contiene a la capacidad.", " kg"),
        ("=", "{F} ¿En cuántos días se llena la bodega al ritmo de 10 kg por día?", "(400-150)//10", "Se divide el espacio libre entre lo que se agrega por día.", " días"),
        ("abc", "{F} ¿Qué tendencia muestra la generación de marzo a junio?", "Sube 20 kg por mes", "Baja 20 kg por mes", "Se mantiene estable", "Cada mes es 20 kg mayor que el anterior."),
        ("=", "{F} ¿Cuántos kg más se generaron en junio que en marzo?", "360-300", "Se resta la generación de marzo a la de junio.", " kg"),
        ("=", "{F} ¿Cuál fue el promedio mensual de los 4 meses?", "(300+320+340+360)//4", "Se suman las cuatro cifras y se divide entre 4.", " kg"),
        ("=", "{F} ¿Qué porcentaje de aumento hubo entre marzo y junio?", "(360-300)*100//300", "Se divide el aumento entre el valor inicial y se multiplica por 100.", " %"),
        ("abc", "{F} Con el retiro en 28 días y la bodega llena en 25, ¿qué corresponde?", "Adelantar el retiro, porque la bodega se llenaría antes", "Mantener el retiro, porque 28 es menor que 30", "Dejar que se llene y retirar después", "El retiro debe ocurrir antes del llenado, no solo antes del plazo."),
        ("=", "{F} ¿Cuántos días antes del retiro programado se llenaría la bodega?", "28-25", "Se resta el día de llenado al día de retiro.", " días"),
        ("abc", "{F} Un compañero dice: «si se derrama algo en la bodega, ayudo a limpiar, es solo un poco». ¿Qué corresponde?", "Alejarse y avisar, porque lo atiende el personal formado del plan de contingencia", "Ayudar, si el derrame es pequeño", "Cubrir el derrame con cajas para que no se vea", "Quien no está formado no atiende derrames."),
        em("Calculas el llenado de una bodega de residuos de ejemplo cuando alguien avisa que se está filtrando un líquido por un tambor y que hay olor irritante en el pasillo.", 2),
    ],
    ctx=("abc", "Un jefe de ejemplo propone no programar el retiro este mes «para ahorrar», aunque la bodega estaría llena en 12 días. ¿Qué respondes?", "Que no corresponde: hay que programar el retiro antes del llenado y del plazo máximo", "Que sí, porque ahorrar es lo más importante", "Que sí, si se agregan más tambores sin avisar", "Una bodega llena o con plazo vencido es un riesgo y un incumplimiento."),
    sc=[
        ("En Química Industrial: ¿cómo se calculan los días hasta que se llena una bodega?", "Espacio libre dividido entre lo que se agrega por día", "Así se sabe cuánto tiempo queda para programar el retiro."),
        ("En Química Industrial: ¿qué se hace si la generación sube mes a mes?", "Se revisa la causa y se planifican más retiros o menor generación", "La tendencia ayuda a anticipar el problema."),
        ("¿Quién atiende un derrame?", "El personal formado del plan de contingencia", "El resto del personal se aleja y avisa."),
    ],
    op=("Caso ficticio de «Química Demo Costa Norte»: capacidad de la bodega de residuos de 600 kg; hoy contiene 240 kg y se agregan 12 kg por día; el retiro está programado dentro de 35 días; la generación de los últimos 3 meses fue 200, 220 y 240 kg. Escribe (a) en cuántos días se llena la bodega, (b) si el retiro programado es adecuado y por qué, (c) la tendencia de generación, (d) quién atiende un derrame.",
        "(a) El espacio libre es 360 kg y 360 entre 12 son 30 días. (b) No, porque se llena a los 30 días y el retiro es a los 35. (c) Sube 20 kg por mes. (d) El personal formado según el plan de contingencia; el resto se aleja y avisa.",
        ["calcula los días hasta el llenado", "compara con el retiro programado", "describe la tendencia", "nombra quién atiende el derrame"],
        ["hoja con las cuatro respuestas"],
        ["no restar lo que ya hay", "aceptar un retiro tardío", "creer que cualquiera atiende el derrame"],
        "Pregunta: «¿cuántos kg libres hay hoy?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una bodega con capacidad, contenido y ritmo diario, y calcula cuándo se llena.",
    extend="Explica con un ejemplo por qué conviene anticipar el retiro de residuos en lugar de esperar que la bodega esté llena.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada). Mes de la planta ficticia «Química Demo Valle Claro»: 2.000 kg de residuos sólidos, de los cuales 600 kg se enviaron a reciclaje y 1.400 kg a disposición final. Producción del mes: 500 toneladas (de ejemplo). "
     "Mes anterior: 2.500 kg de residuos sólidos. Costo de ejemplo de disposición final: $100 por kg; el retiro para reciclaje no tiene costo. Meta de reciclaje de ejemplo: 40 % de los residuos sólidos. "
     "Residuo líquido peligroso del mes: 700 L; un tambor admite 200 L.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar criterios con datos de ejemplo en el manejo de residuos: porcentaje de reciclaje, generación por tonelada producida, reducción respecto del mes anterior, costos y tambores necesarios.",
    prior=["Sé calcular porcentajes.", "Sé qué es la jerarquía de gestión de residuos.", "Sé redondear hacia arriba."],
    explain=[
        "En Química Industrial, el porcentaje de reciclaje es los kg reciclados entre los kg totales, por 100. La generación específica es cuántos kg de residuo se generan por cada tonelada producida: se divide el total de residuos entre las toneladas producidas, y permite comparar meses con producción distinta. La reducción respecto del mes anterior es el cambio dividido entre el valor anterior, por 100.",
        "Una meta fija el reciclaje que se quiere alcanzar: para saber cuántos kg faltan se calcula el porcentaje de la meta sobre el total y se resta lo ya reciclado. El costo de disposición final se calcula multiplicando los kg por el precio por kg. Para elegir envases se divide el volumen entre la capacidad de cada uno y se redondea hacia arriba, porque un envase parcialmente lleno ocupa un envase entero.",
        f"Los cálculos orientan decisiones de gestión; mover o envasar residuos lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("porcentaje de reciclaje", "kg reciclados entre kg totales, por 100"), ("generación específica", "kg de residuo por cada tonelada producida"), ("reducción", "disminución de la generación respecto de un periodo anterior"), ("meta de reciclaje", "porcentaje de residuos que se quiere reciclar"), ("redondear hacia arriba", "subir al entero siguiente cuando sobra una parte")],
    worked=[
        ("Porcentaje de reciclaje", "Una planta de ejemplo genera 800 kg de residuos y recicla 200 kg. ¿Qué porcentaje recicla?", ["Se divide 200 entre 800 y se multiplica por 100.", "200 por 100 son 20.000, y 20.000 entre 800 son 25."], "25 %"),
        ("Generación específica", "Una planta de ejemplo produce 200 toneladas y genera 600 kg de residuos. ¿Cuántos kg por tonelada son?", ["Se divide el residuo entre las toneladas.", "600 entre 200 son 3."], "3 kg por tonelada"),
    ],
    mistakes=[("Calcular la reducción dividiendo entre el mes nuevo.", "La reducción se compara con el valor anterior, que es el punto de partida.", "Divide el cambio entre el valor del mes anterior."),
              ("Decir que 700 L necesitan 3 tambores de 200 L porque «3 por 200 es casi 700».", "Con 3 tambores solo caben 600 L; sobran 100 L que necesitan un tambor más.", "Divide y, si sobra algo, suma un tambor.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es la generación específica de residuos?", "Los kg de residuo generados por cada tonelada producida", "El costo de retirar un kg de residuo", "El número de bodegas de la planta", "Permite comparar meses con producción distinta."),
        ("abc", "En Química Industrial: ¿cómo se calcula el porcentaje de reciclaje?", "Kg reciclados entre kg totales, por 100", "Kg totales entre kg reciclados, por 100", "Kg reciclados menos kg totales", "El porcentaje compara la parte reciclada con el total."),
        ("abc", "En Química Industrial: ¿para qué se redondea hacia arriba al calcular tambores?", "Porque un tambor parcialmente lleno ocupa un tambor entero", "Porque así se gasta menos dinero", "Porque los tambores son siempre del mismo color", "El resto de líquido igual necesita un tambor."),
        ("=", "{F} ¿Qué porcentaje de los residuos sólidos del mes se reciclaron?", "600*100//2000", "Se dividen los kg reciclados entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos kg de residuo sólido se generan por cada tonelada producida?", "2000//500", "Se divide el total de residuos entre las toneladas producidas.", " kg por tonelada"),
        ("=", "{F} ¿Qué porcentaje se redujo la generación respecto del mes anterior?", "(2500-2000)*100//2500", "Se divide la reducción entre el valor anterior y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos kg de residuo sólido debían reciclarse para alcanzar la meta del 40 %?", "2000*40//100", "Se calcula el 40 % del total.", " kg"),
        ("=", "{F} ¿Cuántos kg más debieron reciclarse para llegar a la meta?", "2000*40//100-600", "Se resta lo reciclado a lo que exige la meta.", " kg"),
        ("=", "{F} ¿Cuánto costó la disposición final del mes?", "1400*100", "Se multiplica los kg a disposición final por el costo por kg.", " pesos"),
        ("=", "{F} ¿Cuántos pesos se habrían ahorrado si los kg que faltaban para la meta se hubieran reciclado en vez de enviarse a disposición final?", "200*100", "Cada kg que se recicla deja de pagar el costo de disposición final.", " pesos"),
        ("=", "{F} ¿Cuántos tambores se necesitan para los 700 L de residuo líquido peligroso? Redondea hacia arriba.", "(700+199)//200", "Se divide entre 200 L y se redondea hacia arriba porque 100 L también ocupan un tambor.", " tambores"),
        ("abc", "{F} Un compañero dice: «bajamos la generación, así que no hace falta reciclar más». ¿Qué corresponde?", "Seguir hacia la meta de reciclaje, porque reducir y reciclar son metas distintas", "Dejar de reciclar, porque ya se redujo", "Reciclar solo si cuesta menos que botar", "Reducir y reciclar se complementan en la jerarquía."),
        em("Haces estos cálculos en una oficina cuando alguien avisa que un tambor de residuo líquido de la planta se rompió y que el líquido corre hacia una canaleta.", 3),
    ],
    ctx=("abc", "Una jefatura de ejemplo propone declarar que se recicló el 40 % «para cumplir la meta», aunque se recicló el 30 %. ¿Qué respondes?", "Que no: el informe debe reflejar lo real y se informa cuánto falta para la meta", "Que sí, porque la meta es lo más importante", "Que sí, si se anota después", "Un registro falso impide mejorar y es un incumplimiento."),
    sc=[
        ("En Química Industrial: ¿cómo se calcula la reducción respecto del mes anterior?", "El cambio dividido entre el valor del mes anterior, por 100", "Se compara con el punto de partida."),
        ("En Química Industrial: ¿cómo se calcula la generación específica?", "Kg de residuo entre toneladas producidas", "Así se comparan meses con distinta producción."),
        ("¿Se debe declarar un reciclaje mayor al real para cumplir la meta?", "No, el informe debe ser real", "Los registros falsos impiden detectar y mejorar los problemas."),
    ],
    op=("Planilla ficticia de «Química Demo Costa Norte»: 1.000 kg de residuos sólidos, de los cuales 300 kg se reciclaron y 700 kg fueron a disposición final a $80 por kg (de ejemplo); producción de 250 toneladas; mes anterior de 1.250 kg; meta de reciclaje del 40 %. Escribe (a) el porcentaje de reciclaje, (b) cuántos kg faltaban para la meta, (c) los kg de residuo por tonelada, (d) la reducción respecto del mes anterior.",
        "(a) 300 de 1.000 son 30 %. (b) La meta exige 400 kg y faltaban 100 kg. (c) 1.000 entre 250 son 4 kg por tonelada. (d) Bajó 250 kg, que son 20 % de 1.250.",
        ["calcula el porcentaje", "calcula lo que faltaba", "calcula la generación específica", "calcula la reducción"],
        ["hoja con los cuatro cálculos"],
        ["dividir al revés", "no restar lo ya reciclado", "dividir la reducción entre el mes nuevo"],
        "Pregunta: «¿cuántos kg exige la meta del 40 %?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una planilla de residuos y calcula el porcentaje de reciclaje y la generación por tonelada.",
    extend="Explica con un ejemplo por qué la generación específica es mejor que los kg totales para comparar dos meses.",
)

# ============================================================ OAE-05, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). La planta ficticia «Química Demo Valle Claro» debe elegir una empresa para retirar 300 kg de residuos sólidos peligrosos. Empresa A: $700 por kg, autorización vigente, entrega registro de retiro y certificado de disposición. "
     "Empresa B: $450 por kg, sin autorización vigente y sin certificado de disposición. Condiciones obligatorias: autorización vigente y certificado de disposición. "
     "Lista de control de un registro de retiro, 6 puntos: (1) tipo de residuo; (2) cantidad; (3) fecha; (4) transportista autorizado; (5) destino autorizado; (6) firmas. "
     "Revisión de 5 registros: R1, R2 y R5 cumplen los 6 puntos; R3 cumple 5 (falta una firma); R4 cumple 4 (faltan el destino y la cantidad).")
build(
    O5, 5, F,
    use="Aprenderé a comparar empresas de retiro de residuos con condiciones obligatorias y costos, y a verificar la calidad de los registros de retiro con una lista de control de seis puntos.",
    prior=["Sé qué es una condición obligatoria.", "Sé qué es un registro de retiro.", "Sé calcular costos y porcentajes."],
    explain=[
        "En Química Industrial, al elegir una empresa que retira residuos peligrosos se aplican primero las condiciones obligatorias: autorización vigente y certificado de disposición. Quien no las cumple se descarta, aunque cobre menos. Entre las empresas que sí las cumplen, se compara el costo. El generador sigue siendo responsable hasta la disposición final, por eso conviene exigir un certificado de que el residuo llegó a su destino.",
        "Verificar la calidad de los registros es revisar con una lista de control que cada retiro tenga los datos exigidos: tipo de residuo, cantidad, fecha, transportista autorizado, destino autorizado y firmas. El porcentaje de cumplimiento se calcula con los puntos cumplidos entre los puntos totales, por 100. Un registro incompleto se informa al encargado ambiental para corregirlo, sin inventar los datos faltantes.",
        f"Todo esto es análisis en papel: retirar, envasar o trasladar residuos lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("condición obligatoria", "requisito que una opción debe cumplir para poder elegirse"), ("certificado de disposición", "documento que acredita que el residuo llegó a su destino autorizado"), ("lista de control", "tabla de puntos que se marcan como cumple o no cumple"), ("registro incompleto", "registro al que le falta algún dato exigido")],
    worked=[
        ("Descartar por una condición obligatoria", "Una empresa de ejemplo cobra la mitad pero no tiene autorización vigente; otra cobra más y sí la tiene. ¿Cuál se descarta?", ["La autorización vigente es una condición obligatoria.", "Se descarta la que no la tiene, aunque cueste menos."], "La empresa sin autorización"),
        ("Puntos cumplidos", "Una revisión de ejemplo revisa 5 registros de 4 puntos cada uno y encuentra 18 puntos cumplidos. ¿Qué porcentaje es?", ["Los puntos totales son 5 por 4, es decir, 20.", "18 por 100 son 1.800, y 1.800 entre 20 son 90."], "90 %"),
    ],
    mistakes=[("Elegir la empresa más barata sin mirar su autorización.", "La autorización vigente es una condición obligatoria; sin ella el residuo puede terminar en un sitio no autorizado.", "Descarta primero lo que incumple y luego compara los costos."),
              ("Completar de memoria los datos faltantes de un registro.", "Un registro con datos inventados no sirve para la trazabilidad.", "Informa lo que falta y pide la corrección con respaldo.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es un certificado de disposición?", "Un documento que acredita que el residuo llegó a su destino autorizado", "Una factura del transportista", "Un plano de la bodega de residuos", "El certificado cierra la trazabilidad del residuo."),
        ("abc", "En Química Industrial: ¿qué se hace con una empresa que incumple una condición obligatoria?", "Se descarta, aunque cobre menos", "Se elige si es la más barata", "Se elige solo si firma el registro", "Una condición obligatoria no se negocia."),
        ("abc", "En Química Industrial: ¿qué se hace con un registro incompleto?", "Se informa al encargado ambiental para corregirlo", "Se completa de memoria", "Se archiva sin avisar", "Los datos faltantes no se inventan."),
        ("=", "{F} ¿Cuánto costaría el retiro con la empresa A?", "300*700", "Se multiplica los kg por el costo por kg.", " pesos"),
        ("=", "{F} ¿Cuánto costaría el retiro con la empresa B?", "300*450", "Se multiplica los kg por el costo por kg.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta la empresa A que la B?", "300*700-300*450", "Se restan los costos totales.", " pesos"),
        ("abc", "{F} ¿Qué empresa conviene elegir y por qué?", "La A, porque cumple las condiciones obligatorias aunque cueste más", "La B, porque es más barata", "La B, si firma el registro", "La empresa B incumple la autorización y el certificado."),
        ("abc", "{F} ¿Por qué no basta que la empresa B ofrezca retirar rápido?", "Porque sin autorización no se garantiza un destino autorizado", "Porque su precio por kg es menor", "Porque no tiene camión", "Sin autorización y certificado se pierde la trazabilidad."),
        ("=", "{F} ¿Cuántos puntos de control cumplen en total los 5 registros?", "6+6+5+4+6", "Se suman los puntos cumplidos de cada registro.", " puntos"),
        ("=", "{F} ¿Qué porcentaje de los 30 puntos revisados se cumple?", "27*100//30", "Se dividen los puntos cumplidos entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de los 5 registros cumple los 6 puntos?", "3*100//5", "Se dividen los registros completos entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué corresponde con el registro R4, al que le faltan el destino y la cantidad?", "Informar al encargado ambiental para corregirlo con respaldo", "Completar de memoria el destino y la cantidad", "Archivarlo porque cumple 4 de 6 puntos", "Un registro incompleto no se completa por suposición."),
        em("Comparas empresas gestoras en una oficina cuando alguien avisa que un camión de residuos se detuvo en el patio con una fuga visible y olor irritante.", 4),
    ],
    ctx=("abc", "Un proveedor de ejemplo dice: «Te cobro la mitad, pero no te doy certificado de disposición». ¿Qué respondes?", "Que no puedes aceptar, porque sin certificado no se asegura el destino del residuo", "Que aceptas, porque el ahorro es grande", "Que aceptas, si lo retira de noche", "El certificado es una condición obligatoria para cerrar la trazabilidad."),
    sc=[
        ("En Química Industrial: ¿cuáles son las dos condiciones obligatorias de la ficha?", "Autorización vigente y certificado de disposición", "Sin ellas no hay garantía del destino del residuo."),
        ("¿Cómo se calcula el porcentaje de cumplimiento de la lista?", "Puntos cumplidos entre totales, por 100", "Se expresa como parte del total revisado."),
        ("En Química Industrial: ¿se inventan los datos faltantes de un registro?", "No, se informa y se corrige con respaldo", "Un dato inventado rompe la trazabilidad."),
    ],
    op=("Caso ficticio de «Química Demo Costa Norte»: retiro de 200 kg de residuos sólidos peligrosos. Empresa M: $600 por kg, autorizada y con certificado. Empresa N: $350 por kg, sin certificado de disposición. Dos registros revisados con la lista de 6 puntos: uno cumple los 6 y el otro cumple 3 (le faltan el destino, la fecha y la firma del transportista). Escribe (a) qué empresa se descarta y por qué, (b) el costo del retiro con la empresa elegida, (c) el porcentaje de cumplimiento de los 12 puntos revisados, (d) qué se hace con el registro incompleto.",
        "(a) Se descarta N, porque no tiene certificado de disposición. (b) 200 por 600 son 120.000 pesos. (c) 9 de 12 puntos son 75 %. (d) Se informa al encargado ambiental para completar los datos con respaldo, sin inventarlos.",
        ["descarta por condición obligatoria", "calcula el costo", "expresa el cumplimiento", "informa el registro incompleto"],
        ["hoja con las cuatro respuestas"],
        ["elegir por precio", "no aplicar la condición obligatoria", "completar la firma por sí mismo"],
        "Pregunta: «¿qué documento falta a la empresa N?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa dos empresas de retiro con costo y documentos, y decide cuál elegir usando condiciones obligatorias.",
    extend="Explica con un ejemplo por qué un retiro barato sin certificado puede salir más caro.",
)
