"""Mecánica Industrial, mención Matricería, 4.º medio: OAM-04 (mantenimiento y retocado de matrices y moldes: pautas por golpes, registros, costos, sin procedimientos), OAM-05 (dibujo de moldes con software: conceptos, revisión de planos y cálculo, sin instalar software) y OAM-06 (residuos de matrices y moldes: clasificación, documentos y cálculo). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_mema_common import AVISO, EMER, build

O4 = "TP-MEMA-4-OAM-04"
O5 = "TP-MEMA-4-OAM-05"
O6 = "TP-MEMA-4-OAM-06"

# ============================================================ OAM-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La matriz de corte M-07 del «Taller Demo de Matricería» lleva 262.000 golpes. El mantenimiento puede ser preventivo (según una pauta por golpes), correctivo (después de una falla) o de retocado: un ajuste fino de una superficie o de una medida para que la pieza coincida con el modelo (el diseño de referencia) y con la muestra (una pieza de ejemplo aprobada). "
     "Peligros anotados: aplastamiento al mover la matriz, cargas pesadas, bordes filosos, energía almacenada en resortes, aceites y solventes de limpieza, polvo abrasivo y ruido.")
build(
    O4, 1, F,
    use="Aprenderé qué es el mantenimiento preventivo, correctivo y el retocado de una matriz o un molde, qué riesgos tienen y qué reglas generales los rodean, sin intervenir ningún equipo.",
    prior=["Sé qué es una matriz y un molde.", "Sé qué es mantenimiento preventivo y correctivo.", "Sé qué es energía almacenada."],
    explain=[
        "El mantenimiento preventivo de una matriz se hace antes de la falla, según una pauta que usa los golpes acumulados en lugar de la fecha. El correctivo se hace después de una falla. El retocado es un ajuste fino de una superficie o de una medida para que las piezas coincidan con el modelo y con la muestra aprobada. Cada tipo se registra en la ficha de la matriz.",
        "Estas tareas tienen riesgos: aplastamiento al mover una matriz, cargas pesadas, bordes filosos, energía almacenada en resortes, aceites y solventes, polvo abrasivo y ruido. Se controlan con orden y limpieza, bloqueo y etiquetado, resguardos y EPP como última barrera. Los aceites usados, los trapos contaminados y el polvo abrasivo son residuos que se manejan según la norma vigente.",
        f"Estas tareas las hace personal autorizado; este cuaderno no enseña a hacerlas. {EMER} {AVISO}",
    ],
    vocab=[("mantenimiento por golpes", "pauta que cuenta los golpes de la matriz en vez de los días"), ("retocado", "ajuste fino de una superficie o de una medida para coincidir con la muestra"), ("modelo", "diseño de referencia de la pieza"), ("muestra", "pieza de ejemplo aprobada que sirve de referencia"), ("ficha de la matriz", "documento con el historial de golpes y mantenciones")],
    worked=[
        ("Tipo de mantenimiento", "Una matriz de ejemplo se revisa cada 50.000 golpes aunque funcione bien. ¿Qué tipo de mantenimiento es?", ["Se hace antes de la falla, por una pauta.", "Es preventivo."], "Preventivo"),
        ("Qué es el retocado", "Una pieza de ejemplo sale 20 µm fuera de la muestra y se ajusta una superficie de la matriz para corregirlo. ¿Qué tarea es?", ["Es un ajuste fino para coincidir con la muestra.", "Es un retocado."], "Un retocado"),
    ],
    mistakes=[("Creer que una matriz detenida ya no tiene energía.", "Puede quedar energía almacenada en resortes o en el sistema hidráulico.", "Considera el bloqueo y etiquetado de la empresa y deja la tarea a personal autorizado."),
              ("Botar el aceite o los trapos con solvente a la basura común.", "Son residuos que requieren gestión.", "Llévalos al punto de acopio según la norma vigente.")],
    T=[
        ("abc", "En Matricería: ¿qué es el mantenimiento preventivo de una matriz por golpes?", "El que se hace antes de la falla, según los golpes acumulados", "El que se hace después de una falla", "El que se hace cuando alguien lo recuerda", "El preventivo anticipa la falla según una pauta."),
        ("abc", "En Matricería: ¿qué es el retocado?", "Un ajuste fino para que las piezas coincidan con el modelo y la muestra", "El cambio completo de la matriz", "La limpieza del taller", "En este caso, El retocado afina un detalle."),
        ("abc", "En Matricería: ¿qué es la muestra?", "Una pieza de ejemplo aprobada que sirve de referencia", "La pieza defectuosa de un lote", "El plano de la prensa", "La muestra aprobada es la referencia."),
        ("abc", "{F} ¿Qué peligro de la lista se debe a los resortes comprimidos de la matriz?", "La energía almacenada", "El ruido", "El polvo abrasivo", "En este caso, Un resorte comprimido guarda energía."),
        ("abc", "{F} ¿Cuál de los residuos mencionados requiere un manejo especial por ser contaminado?", "Los trapos con aceite y solvente", "Los recortes de chapa limpios", "El papel de oficina", "Los trapos contaminados no van a la basura común."),
        ("abc", "{F} Un resguardo que impide acercar las manos a la zona de cierre es un control:", "De ingeniería", "Administrativo", "De EPP", "El resguardo es una barrera física."),
        ("=", "{F} La pauta pide una limpieza cada 20.000 golpes. ¿Cuántas limpiezas corresponden desde cero hasta los 260.000 golpes?", "260000//20000", "Se divide el total de golpes entre el intervalo.", " limpiezas"),
        ("=", "{F} ¿Cuántos golpes pasaron desde los 240.000 de la última limpieza hasta los 262.000 actuales?", "262000-240000", "Se resta el último registro a los golpes actuales.", " golpes"),
        ("abc", "{F} Un aprendiz dice: «la matriz está parada, puedo limpiarla con las manos». ¿Qué respuesta es correcta?", "Es falso: pueden quedar energía almacenada y bordes filosos, y solo personal autorizado interviene", "Es cierto, porque parada no se mueve", "Es cierto, si usa guantes", "En este caso, detenida no significa sin riesgo."),
        ("abc", "En una visita a un taller de ejemplo, una matriz suspendida de una grúa se suelta y una persona queda atrapada. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar levantar la matriz", "Tirar de la persona", "Intervenir sin formación puede causar otro accidente."),
        ("=", "{F} El taller tiene 5 matrices con la misma pauta y cada una requiere 3 horas de mantenimiento preventivo. ¿Cuántas horas suman?", "5*3", "Se multiplican las matrices por las horas de cada una.", " horas"),
        ("abc", "En Matricería: ¿qué se hace con el polvo abrasivo y los aceites usados de una mantención?", "Se almacenan en recipientes rotulados y se gestionan según la norma vigente", "Se barren al desagüe", "Se botan a la basura común", "En este caso, son residuos que requieren gestión."),
        ("abc", "{F} Un jefe dice: «la matriz sigue cortando, no necesita preventivo». ¿Qué respuesta es correcta?", "Es falso: el preventivo se hace antes de la falla justamente para evitarla", "Es cierto, porque funciona", "Es cierto, si es nueva", "El preventivo se planifica aunque la matriz funcione."),
    ],
    ctx=("abc", "Un amigo de ejemplo te dice: «afilemos la matriz del liceo con una piedra, no cuesta nada». ¿Qué respondes?", "Que intervenir una matriz exige personal autorizado, y que consultarás a un adulto responsable", "Que sí, si tenemos cuidado", "Que sí, con gafas", "Este cuaderno no habilita para intervenir matrices."),
    sc=[
        ("En Matricería: ¿qué cuenta una pauta por golpes?", "Los golpes acumulados de la matriz", "Se usa en lugar de la fecha."),
        ("En Matricería: ¿qué es el retocado?", "Un ajuste fino para coincidir con la muestra", "Afina un detalle de una superficie o medida."),
        ("En Matricería: ¿quién interviene una matriz?", "Personal autorizado", "El trabajo exige formación y norma vigente."),
    ],
    op=("Ficha de ejemplo: una matriz de doblado ficticia lleva 150.000 golpes, con una pauta de limpieza cada 25.000 golpes y último registro a los 125.000. Peligros: energía almacenada, bordes filosos y aceite. Escribe (a) cuántos golpes pasaron desde la última limpieza, (b) si la limpieza está vencida, (c) un control de ingeniería y uno administrativo, (d) qué haces con el aceite usado. No describas cómo se interviene.",
        "(a) 150.000 − 125.000 = 25.000 golpes. (b) Corresponde justo a los 150.000: toca hacerla ahora. (c) Ingeniería: un resguardo; administrativo: bloqueo y etiquetado y orden de trabajo. (d) Almacenarlo en un recipiente rotulado hasta su retiro, según la norma vigente.",
        ["calcula los golpes", "evalúa la pauta", "propone dos controles", "indica el manejo del aceite"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "proponer solo EPP", "describir cómo se interviene"],
        "Pregunta: «¿qué se resta a qué?». Si duda, pídele que relea cómo se cuenta una pauta por golpes."),
    reinforce="Escribe una pauta inventada por golpes con tres tareas y su intervalo.",
    extend="Explica con un ejemplo por qué la pauta de una matriz se mide en golpes y no en días.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 2 (pauta y registro de ejemplo, inventados, para la matriz M-07; no reemplazan el manual del fabricante). Pauta por golpes: limpieza e inspección visual, cada 20.000 golpes; revisión de la lubricación, cada 50.000; medición del desgaste del filo por personal autorizado, cada 100.000; revisión general, cada 500.000. "
     "Registro de la ficha: golpes actuales 262.000; última limpieza a los 240.000; última lubricación a los 250.000; última medición del filo a los 200.000; última revisión general a los 0. Documentos: pauta, ficha de la matriz, orden de trabajo, lista de repuestos y pieza muestra con su plano.")
build(
    O4, 2, F,
    use="Aprenderé a leer una pauta por golpes y la ficha de una matriz, a calcular qué tareas están vencidas y qué roles intervienen.",
    prior=["Sé qué es una pauta por golpes.", "Sé qué es una orden de trabajo.", "Sé sumar y restar enteros."],
    explain=[
        "La pauta por golpes lista tareas con su intervalo en golpes. La próxima ejecución de una tarea es la última ejecución más el intervalo. Si los golpes actuales superan ese valor, la tarea está vencida y se informa; si no, se calcula cuántos golpes faltan. La ficha de la matriz anota los golpes y la última vez que se hizo cada tarea.",
        "La orden de trabajo pide y registra cada tarea con la matriz detenida y asegurada, la hace personal autorizado y la aprueba el supervisor. La lista de repuestos indica las piezas que se reponen, como resortes o insertos. La pieza muestra y su plano sirven para comparar el resultado. El planificador programa, el matricero ejecuta, el inspector verifica y el supervisor aprueba.",
        f"Solo se leen documentos y se calcula en papel. {EMER} {AVISO}",
    ],
    vocab=[("próxima ejecución", "última ejecución más el intervalo"), ("tarea vencida", "la que ya pasó su momento de ejecución"), ("inserto", "pieza que se puede reemplazar en la zona de corte de una matriz"), ("planificador", "persona que programa las tareas de mantenimiento"), ("matricero", "especialista en construir y mantener matrices y moldes")],
    worked=[
        ("Próxima ejecución", "Una tarea de ejemplo se hace cada 30.000 golpes y la última fue a los 90.000. ¿A qué golpe corresponde la próxima?", ["Se suma el intervalo a la última ejecución.", "90.000 más 30.000 son 120.000."], "A los 120.000 golpes"),
        ("Tarea vencida", "Una tarea de ejemplo debía hacerse a los 70.000 golpes y la matriz lleva 75.000. ¿Está vencida?", ["75.000 supera 70.000.", "Pasó su momento."], "Sí, por 5.000 golpes"),
    ],
    mistakes=[("Contar el intervalo desde cero y no desde la última ejecución.", "El intervalo se cuenta desde la última vez que se hizo.", "Suma el intervalo a la última ejecución."),
              ("Dejar sin informar una tarea vencida.", "El atraso puede producir una falla.", "Se informa al supervisor.")],
    T=[
        ("abc", "En Matricería: ¿cómo se calcula la próxima ejecución de una tarea por golpes?", "Sumando el intervalo a la última ejecución", "Restando el intervalo a los golpes actuales", "Multiplicando el intervalo por los golpes", "La próxima parte de la última más el intervalo."),
        ("abc", "En Matricería: ¿qué es un inserto?", "Una pieza reemplazable en la zona de corte de una matriz", "La prensa completa", "El plano de la matriz", "El inserto se reemplaza sin cambiar toda la matriz."),
        ("abc", "En Matricería: ¿quién ejecuta las tareas de mantenimiento de una matriz?", "El matricero autorizado", "El proveedor del plano", "El cliente", "En este caso, El matricero ejecuta con autorización."),
        ("=", "{F} ¿A qué golpe corresponde la próxima limpieza?", "240000+20000", "Se suma el intervalo a la última limpieza.", " golpes"),
        ("=", "{F} ¿A qué golpe corresponde la próxima revisión de lubricación?", "250000+50000", "Se suma el intervalo a la última lubricación.", " golpes"),
        ("=", "{F} ¿A qué golpe corresponde la próxima medición del filo?", "200000+100000", "Se suma el intervalo a la última medición.", " golpes"),
        ("abc", "{F} Con 262.000 golpes, ¿qué tarea está vencida?", "La limpieza, que correspondía a los 260.000", "La revisión de lubricación", "La revisión general", "La limpieza venció a los 260.000 golpes."),
        ("=", "{F} ¿Cuántos golpes de atraso tiene esa limpieza?", "262000-260000", "Se resta el momento previsto a los golpes actuales.", " golpes"),
        ("=", "{F} ¿Cuántos golpes faltan para la próxima medición del filo?", "300000-262000", "Se resta los golpes actuales al momento previsto.", " golpes"),
        ("abc", "{F} Un jefe dice: «la limpieza vencida no importa, la matriz corta bien». ¿Qué respuesta es correcta?", "Es falso: una tarea vencida se informa y se programa, porque el atraso puede producir una falla", "Es cierto, porque corta bien", "Es cierto, si hay poca producción", "La pauta se cumple aunque la matriz parezca bien."),
        ("abc", "{F} Un operario sugiere hacer una revisión del filo por su cuenta porque «es fácil». ¿Qué respuesta es correcta?", "No corresponde: la medición del filo la hace personal autorizado con la matriz detenida y asegurada", "Corresponde, si lo hace rápido", "Corresponde, si usa guantes", "La pauta indica que lo hace personal autorizado."),
        ("=", "{F} Con 9 matrices iguales y 4 tareas de limpieza al año por matriz, ¿cuántas limpiezas se hacen al año?", "9*4", "Se multiplican las matrices por las limpiezas de cada una.", " limpiezas"),
        ("Una matriz de ejemplo debía hacerse una tarea a los 150.000 golpes y lleva 148.000. ¿Está vencida?", "No, faltan 2.000 golpes", "En este caso, 148.000 es menor que 150.000."),
    ],
    ctx=("abc", "Un matricero de ejemplo dice: «yo sé cuándo le toca, no necesito la pauta». ¿Qué propones?", "Seguir la pauta y el registro, porque dan evidencia verificable del estado de la matriz", "Aceptarlo por su experiencia", "Eliminar la pauta", "La pauta y el registro permiten a otros planificar."),
    sc=[
        ("En Matricería: ¿cuál es la próxima ejecución si la última fue a los 90.000 y el intervalo es 30.000?", "A los 120.000 golpes", "En este caso, Se suma el intervalo."),
        ("En Matricería: ¿qué es una tarea vencida?", "La que pasó su momento de ejecución", "En este caso, Se debe informar y programar."),
        ("En Matricería: ¿qué documento guarda el historial de la matriz?", "La ficha de la matriz", "En este caso, registra golpes y tareas."),
    ],
    op=("Ficha de ejemplo: una matriz con pauta por golpes: limpieza cada 15.000; lubricación cada 40.000; revisión del filo cada 80.000. Registro: golpes actuales 100.000; limpieza a los 90.000; lubricación a los 80.000; revisión del filo a los 80.000. Escribe (a) cuándo corresponde la próxima limpieza, (b) si la lubricación está vencida, (c) cuántos golpes faltan para la revisión del filo, (d) quién la hace.",
        "(a) 90.000 + 15.000 = 105.000 golpes. (b) Corresponde a los 120.000; aún no está vencida. (c) 80.000 + 80.000 = 160.000, y faltan 60.000. (d) Personal autorizado, con la matriz detenida y asegurada.",
        ["calcula la próxima limpieza", "evalúa la lubricación", "calcula los golpes que faltan", "indica quién la hace"],
        ["hoja con las cuatro respuestas"],
        ["contar desde cero", "no sumar el intervalo", "asignar a cualquiera"],
        "Pregunta: «¿cuándo fue la última vez y cuál es el intervalo?». Si duda, pídele que anote ambos datos."),
    reinforce="Inventa una pauta con tres tareas y calcula la próxima ejecución de cada una.",
    extend="Explica con un ejemplo por qué una tarea vencida debe informarse aunque la matriz parezca funcionar bien.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 3 (informe de una matriz de ejemplo, inventado; las mediciones las tomó personal autorizado). Matriz M-07 lleva 262.000 golpes. Desgaste medido del filo: a los 200.000 golpes, 40 µm; a los 250.000 golpes, 60 µm. Límite de desgaste admisible del fabricante de ejemplo: 80 µm. "
     "Rebabas medidas en las piezas: 45 µm; rebaba tolerada: 50 µm; hace un mes eran 20 µm. Producción: 8.000 golpes por día. Regla del taller: se programa el afilado cuando se prevé alcanzar el límite en menos de 10 días de producción. Costo de ejemplo: afilado preventivo, $250.000 y 10 horas de parada; rotura por falla, $1.500.000 y 40 horas de parada; costo de una hora de parada, $50.000.")
build(
    O4, 3, F,
    use="Aprenderé a proyectar el desgaste de una matriz con datos, a decidir cuándo programar el afilado con una regla y a comparar el costo preventivo con el de una falla, en un caso escrito.",
    prior=["Sé qué es un límite admisible.", "Sé calcular una tasa de cambio con enteros.", "Sé comparar costos."],
    explain=[
        "El desgaste del filo aumenta con los golpes. Con dos mediciones se calcula cuántos µm se desgasta por cada cierto número de golpes y se proyecta cuándo llegará al límite admisible. Los golpes que faltan hasta el límite, divididos por los golpes por día, dan los días de producción que quedan. Si quedan menos de los que fija la regla del taller, se programa el afilado.",
        "Las rebabas medidas también avisan: si están cerca de la tolerada o crecen, el filo se está desgastando. Comparar el costo del afilado preventivo con el de una rotura por falla, incluyendo las horas de parada, ayuda a decidir. El afilado lo hace personal autorizado y las decisiones quedan registradas.",
        f"El análisis es de papel. {EMER} {AVISO}",
    ],
    vocab=[("proyección", "estimación de un valor futuro a partir de datos previos"), ("tasa de desgaste", "µm de desgaste por cada cierto número de golpes"), ("límite de desgaste admisible", "desgaste máximo que el fabricante permite"), ("afilado", "tarea que recupera el filo de corte, hecha por personal autorizado"), ("días de producción que quedan", "golpes que faltan divididos por los golpes por día")],
    worked=[
        ("Tasa de desgaste", "Un filo de ejemplo medía 30 µm a los 100.000 golpes y 50 µm a los 200.000. ¿Cuántos µm se desgasta por cada 100.000 golpes?", ["Se resta la primera medición a la segunda.", "50 menos 30 son 20."], "20 µm por 100.000 golpes"),
        ("Días que quedan", "A una matriz de ejemplo le faltan 40.000 golpes para el límite y produce 10.000 golpes por día. ¿Cuántos días quedan?", ["Se dividen los golpes entre los golpes por día.", "40.000 dividido en 10.000 son 4."], "4 días"),
    ],
    mistakes=[("Mirar solo la última medición y no la tendencia.", "El desgaste crece y la proyección avisa antes del límite.", "Usa dos mediciones para proyectar."),
              ("Esperar a que el filo llegue al límite para programar el afilado.", "Pueden salir piezas defectuosas y la matriz puede fallar.", "Aplica la regla del taller con anticipación.")],
    T=[
        ("abc", "En Matricería: ¿qué es una proyección de desgaste?", "Una estimación de cuándo se llegará al límite a partir de mediciones previas", "La medición actual del desgaste", "La tolerancia del plano", "La proyección mira hacia adelante con datos."),
        ("abc", "En Matricería: ¿qué es el límite de desgaste admisible?", "El desgaste máximo que el fabricante permite", "El desgaste que tiene hoy el filo", "El costo del afilado", "Es el tope fijado por el fabricante."),
        ("abc", "En Matricería: ¿qué avisan las rebabas que crecen?", "Que el filo se está desgastando", "Que la chapa es más gruesa", "Que la prensa está nueva", "Una rebaba mayor suele indicar un filo desgastado."),
        ("=", "{F} ¿Cuántos µm se desgastó el filo entre los 200.000 y los 250.000 golpes?", "60-40", "Se resta la primera medición a la segunda.", " µm"),
        ("=", "{F} Con 20 µm de desgaste por cada 50.000 golpes, ¿a qué golpe llegará a los 80 µm, desde los 60 µm a los 250.000?", "250000+50000", "Faltan 20 µm, que son 50.000 golpes más.", " golpes"),
        ("=", "{F} ¿Cuántos golpes faltan desde los 262.000 actuales hasta los 300.000?", "300000-262000", "Se resta los golpes actuales al golpe del límite.", " golpes"),
        ("=", "{F} ¿Cuántos días de producción quedan, con 8.000 golpes por día? Redondea hacia arriba.", "(38000+7999)//8000", "Se dividen los golpes entre los golpes por día, redondeando hacia arriba.", " días"),
        ("abc", "{F} Según la regla del taller, ¿qué corresponde?", "Programar el afilado, porque quedan menos de 10 días de producción", "Esperar, porque aún no llega el límite", "Cambiar la matriz de inmediato", "Quedan unos 5 días y la regla pide programar antes de 10."),
        ("abc", "{F} ¿Qué dice la rebaba de 45 µm frente a la tolerada de 50 µm?", "Está cerca de la tolerancia y creciendo, lo que apoya programar el afilado", "No importa porque cumple", "Ya no cumple", "Hace un mes eran 20 µm y ahora son 45, casi la tolerada."),
        ("=", "{F} ¿Cuánto cuesta el afilado preventivo en total, con el costo de la parada de 10 horas a $50.000 por hora?", "250000+10*50000", "Se suma el costo del afilado y el de la parada.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuesta una rotura por falla en total, con el costo de la parada de 40 horas?", "1500000+40*50000", "Se suma el costo de la rotura y el de la parada.", " pesos de ejemplo"),
        ("abc", "{F} Un jefe dice: «esperemos a que falle, así aprovechamos la matriz al máximo». ¿Qué respuesta es correcta?", "Es falso: una falla cuesta mucho más que el afilado y además es un riesgo para las personas", "Es cierto, porque se aprovecha más", "Es cierto, si la matriz es vieja", "La falla cuesta más y es más peligrosa."),
        ("abc", "{F} Un operario propone afilar el filo él mismo con una lima para ahorrar. ¿Qué respuesta es correcta?", "No corresponde: el afilado lo hace personal autorizado con el procedimiento de la empresa", "Corresponde, si es poco desgaste", "Corresponde, si es rápido", "En este caso, intervenir una matriz exige autorización."),
    ],
    ctx=("abc", "El supervisor de ejemplo dice: «el filo está bajo el límite, no hay que hacer nada». ¿Qué propones?", "Proyectar el desgaste y aplicar la regla del taller antes de llegar al límite", "No hacer nada", "Ignorar la rebaba", "La proyección permite actuar a tiempo."),
    sc=[
        ("En Matricería: ¿cuántos µm se desgasta un filo que pasa de 30 a 50 µm?", "20 µm", "Se resta la primera medición a la segunda."),
        ("En Matricería: ¿cómo se obtienen los días de producción que quedan?", "Dividiendo los golpes que faltan entre los golpes por día", "Es una división simple de golpes."),
        ("En Matricería: ¿qué cuesta más, una falla o un afilado preventivo?", "La falla", "Incluye reparación y más horas de parada."),
    ],
    op=("Ficha de ejemplo: un filo midió 20 µm a los 100.000 golpes y 40 µm a los 200.000. Límite 70 µm. La matriz lleva 230.000 golpes y produce 5.000 golpes por día. Regla: programar el afilado si quedan menos de 20 días de producción. Escribe (a) la tasa de desgaste cada 100.000 golpes, (b) el golpe al que se llegaría a los 60 µm, (c) los días de producción que quedan hasta el golpe de los 300.000, (d) si se programa el afilado.",
        "(a) 40 − 20 = 20 µm por 100.000 golpes. (b) Desde 40 µm a los 200.000, 60 µm a los 300.000 golpes. (c) 300.000 − 230.000 = 70.000 golpes, y 70.000 ÷ 5.000 son 14 días. (d) Sí, porque 14 días son menos de 20.",
        ["calcula la tasa", "proyecta el golpe", "calcula los días", "aplica la regla"],
        ["hoja con las cuatro respuestas"],
        ["calcular mal la tasa", "olvidar dividir entre los golpes por día", "no aplicar la regla"],
        "Pregunta: «¿cuántos golpes faltan?». Si duda, pídele que reste los golpes actuales al golpe del límite."),
    reinforce="Inventa dos mediciones de desgaste y calcula la tasa por cada 100.000 golpes.",
    extend="Explica con un ejemplo por qué una rebaba creciente apoya la decisión de afilar.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 4 (plan anual de mantenimiento de ejemplo, inventado). Taller con 6 matrices iguales, cada una con 12 resortes de vida útil 400.000 golpes. Cada matriz da 160.000 golpes al mes. Pauta: limpieza cada 20.000 golpes, 2 horas cada vez; afilado cada 300.000 golpes, 10 horas cada vez. "
     "Equipo: 2 matriceros que trabajan 160 horas al mes cada uno. Costo de una hora de matricero: $10.000. Costo de un resorte: $4.000. Stock de resortes en bodega: 30. Año de 12 meses.")
build(
    O4, 4, F,
    use="Aprenderé a calcular las tareas y las horas de un plan anual de mantenimiento, a comparar la carga con la capacidad del equipo y a calcular el costo y el stock de repuestos.",
    prior=["Sé multiplicar y dividir enteros.", "Sé calcular horas-técnico.", "Sé comparar una necesidad con un stock."],
    explain=[
        "Un plan anual se calcula a partir de los golpes al año: los golpes por mes por los meses. Las tareas del año de cada tipo son los golpes al año divididos por el intervalo. Las horas de la tarea se obtienen multiplicando el número de tareas por las horas de cada una. La carga del plan es la suma de las horas de todas las tareas y de todas las matrices.",
        "La capacidad del equipo es el número de personas por las horas al mes por los meses. Si la carga supera la capacidad, el plan no se cumple y se debe pedir más personal o reprogramar. Los repuestos se calculan con su vida útil: los golpes al año divididos por la vida útil dan la fracción del año que dura, y el stock debe cubrir las reposiciones. Los valores son de ejemplo.",
        f"Es un cálculo de papel; no se interviene ninguna matriz. {EMER} {AVISO}",
    ],
    vocab=[("golpes al año", "golpes por mes por 12"), ("carga del plan", "suma de las horas de todas las tareas"), ("capacidad del equipo", "horas que el equipo puede entregar"), ("reposición", "cambio de un repuesto por otro nuevo"), ("stock", "cantidad de repuestos disponibles")],
    worked=[
        ("Tareas del año", "Una matriz de ejemplo da 120.000 golpes al año y una tarea se hace cada 30.000. ¿Cuántas veces al año?", ["Se divide los golpes entre el intervalo.", "120.000 dividido en 30.000 son 4."], "4 veces"),
        ("Horas de una tarea", "Una tarea de ejemplo se hace 4 veces al año y toma 3 horas cada vez. ¿Cuántas horas al año?", ["Se multiplican las veces por las horas.", "4 por 3 son 12."], "12 horas"),
    ],
    mistakes=[("Calcular la carga de una sola matriz y olvidar las demás.", "Cada matriz genera su propia carga.", "Multiplica por el número de matrices."),
              ("Comparar la carga con las horas del año completas.", "El equipo no trabaja todas las horas.", "Calcula la capacidad con personas, horas y meses.")],
    T=[
        ("abc", "En Matricería: ¿qué es la carga de un plan de mantenimiento?", "La suma de las horas de todas las tareas", "El número de matrices", "El costo de un resorte", "La carga es lo que pide el plan."),
        ("abc", "En Matricería: ¿qué es la capacidad del equipo?", "Las horas que el equipo puede entregar", "Las horas de parada de la prensa", "El número de golpes", "La capacidad es lo que el equipo puede aportar."),
        ("abc", "En Matricería: ¿qué se hace si la carga supera la capacidad?", "Se pide más personal o se reprograma", "Se omiten tareas sin informar", "Se anotan como hechas", "El plan debe ser realizable o ajustarse con informe."),
        ("=", "{F} ¿Cuántos golpes da una matriz al año?", "160000*12", "Se multiplican los golpes por mes por los meses.", " golpes"),
        ("=", "{F} ¿Cuántas limpiezas al año necesita una matriz?", "1920000//20000", "Se dividen los golpes al año entre el intervalo.", " limpiezas"),
        ("=", "{F} ¿Cuántas horas al año de limpieza requiere una matriz, con 2 horas cada una?", "96*2", "Se multiplican las limpiezas por las horas de cada una.", " horas"),
        ("=", "{F} ¿Cuántos afilados al año necesita una matriz?", "1920000//300000", "Se dividen los golpes al año entre el intervalo, sin considerar el resto.", " afilados"),
        ("=", "{F} ¿Cuántas horas de afilado requiere una matriz al año, con 6 afilados de 10 horas?", "6*10", "Se multiplican los afilados por las horas de cada uno.", " horas"),
        ("=", "{F} ¿Cuántas horas suman limpieza y afilado de las 6 matrices, con 192 horas de limpieza y 60 de afilado por matriz?", "6*(192+60)", "Se suman las horas de una matriz y se multiplican por las matrices.", " horas"),
        ("=", "{F} ¿Cuántas horas al año entrega el equipo de 2 matriceros que trabajan 160 horas al mes?", "2*160*12", "Se multiplican personas, horas por mes y meses.", " horas"),
        ("abc", "{F} Comparando la carga de 1.512 horas con la capacidad de 3.840 horas, ¿qué conclusión corresponde?", "La capacidad alcanza para el plan de mantenimiento preventivo", "La carga supera la capacidad", "No se puede comparar", "En este caso, 1.512 es menor que 3.840."),
        ("abc", "{F} Un jefe dice: «sobra mucha capacidad, reduzcamos las tareas de limpieza». ¿Qué respuesta es correcta?", "No corresponde: la pauta se cumple, y la capacidad sobrante puede usarse en otras tareas o en retocados", "Corresponde, porque sobra capacidad", "Corresponde, si baja el costo", "La pauta no se reduce por sobrar horas."),
        ("=", "{F} ¿Cuántos resortes tienen las 6 matrices en total?", "6*12", "Se multiplican las matrices por los resortes de cada una.", " resortes"),
    ],
    ctx=("abc", "El jefe de ejemplo pregunta si el equipo de 2 matriceros alcanza para el plan. ¿Qué dos cálculos le propones?", "La carga del plan y la capacidad del equipo", "El costo de un resorte", "El número de matrices solamente", "Se compara la carga con la capacidad."),
    sc=[
        ("En Matricería: ¿cómo se calcula la capacidad anual?", "Personas por horas al mes por meses", "Se multiplica lo que el equipo puede entregar."),
        ("En Matricería: ¿cómo se calcula el número de tareas al año?", "Golpes al año divididos por el intervalo", "En este caso, cada intervalo genera una tarea."),
        ("En Matricería: ¿qué se multiplica para obtener la carga de un tipo de tarea?", "Las tareas del año por las horas de cada una", "La carga son las horas totales."),
    ],
    op=("Ficha de ejemplo: 4 matrices dan 100.000 golpes al mes cada una. Limpieza cada 25.000 golpes, 2 horas; afilado cada 200.000 golpes, 8 horas. 1 matricero trabaja 160 horas al mes. Año de 12 meses. Escribe (a) los golpes al año de una matriz, (b) las horas de limpieza al año de una matriz, (c) las horas de afilado al año de una matriz, (d) si la capacidad anual de 1 matricero alcanza para las 4 matrices.",
        "(a) 100.000 × 12 = 1.200.000. (b) 1.200.000 ÷ 25.000 = 48 limpiezas por 2 horas son 96 horas. (c) 1.200.000 ÷ 200.000 = 6 afilados por 8 horas son 48 horas. (d) Carga: 4 × (96 + 48) = 576 horas; capacidad: 160 × 12 = 1.920 horas; alcanza.",
        ["calcula los golpes", "calcula las horas de limpieza", "calcula las horas de afilado", "compara carga y capacidad"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por los meses", "olvidar las matrices", "comparar mal"],
        "Pregunta: «¿cuántas veces al año se hace cada tarea?». Si duda, pídele que divida los golpes entre el intervalo."),
    reinforce="Inventa una matriz con golpes por mes y una pauta y calcula las horas de mantenimiento al año.",
    extend="Explica con un ejemplo por qué una buena planificación compara siempre la carga con la capacidad.",
)

# ============================================================ OAM-04, clase 5
F = ("Ficha 5 (comparación de alternativas de mantenimiento, de ejemplo). La matriz M-07 necesita recuperar su capacidad de corte. Alternativa AF: afilar el filo actual; $250.000 y 10 horas de parada; vida adicional de 150.000 golpes; certificado del proceso disponible. "
     "Alternativa AR: reemplazar el inserto de corte por uno nuevo; $700.000 y 12 horas de parada; vida de 325.000 golpes; con certificado del material. Alternativa AX: reparar con un proceso sin certificado; $100.000 y 6 horas de parada; vida estimada de 60.000 golpes. "
     "Condición obligatoria: contar con certificado. Costo de una hora de parada: $50.000. Lista de verificación: pieza muestra aprobada; medidas dentro de tolerancia; ficha de la matriz actualizada; registro firmado; residuos gestionados.")
build(
    O4, 5, F,
    use="Aprenderé a comparar alternativas de mantenimiento con una condición obligatoria y el costo por golpe de vida, y a verificar la calidad de lo hecho con una lista y la muestra aprobada.",
    prior=["Sé qué es una condición obligatoria.", "Sé calcular un costo por unidad de vida.", "Sé qué es una lista de verificación."],
    explain=[
        "Al comparar alternativas se descartan primero las que no cumplen la condición obligatoria, como tener certificado. Entre las que cumplen, se calcula el costo total de cada una, que suma el costo de la tarea y el de las horas de parada, y se divide entre los golpes de vida adicional para obtener el costo por golpe. La alternativa con menor costo por golpe suele ser la mejor, si cumple todo lo demás.",
        "Después de la tarea se verifica la calidad con una lista: pieza muestra aprobada, medidas dentro de tolerancia, ficha actualizada, registro firmado y residuos gestionados. Una pieza producida después de la mantención se compara con la muestra aprobada. Una lista incompleta no se firma. Los valores son de ejemplo.",
        f"El análisis es de papel. {EMER} {AVISO}",
    ],
    vocab=[("vida adicional", "golpes que se espera que dure la matriz después de la tarea"), ("costo total de la alternativa", "costo de la tarea más costo de las horas de parada"), ("costo por golpe", "costo total dividido por los golpes de vida adicional"), ("pieza muestra aprobada", "pieza de referencia con la que se comparan las nuevas"), ("lista de verificación", "lista de puntos que se comprueban uno a uno")],
    worked=[
        ("Costo total", "Una alternativa de ejemplo cuesta $200.000 y requiere 5 horas de parada a $40.000 la hora. ¿Cuál es el costo total?", ["La parada cuesta 5 por 40.000, es decir 200.000.", "200.000 más 200.000 son 400.000."], "$400.000"),
        ("Costo por golpe", "Un costo total de ejemplo de $400.000 con 100.000 golpes de vida. ¿Cuánto cuesta cada golpe?", ["Se divide el costo entre los golpes.", "400.000 dividido en 100.000 son 4."], "$4 por golpe"),
    ],
    mistakes=[("Elegir la alternativa más barata sin revisar el certificado.", "No cumple la condición obligatoria.", "Descarta primero las que no cumplen."),
              ("Comparar solo el precio de la tarea y olvidar la parada.", "Las horas de parada también cuestan.", "Suma el costo de la parada al de la tarea.")],
    T=[
        ("abc", "En Matricería: ¿qué es la vida adicional de una alternativa?", "Los golpes que se espera que dure la matriz después de la tarea", "Las horas de parada", "El precio del repuesto", "La vida adicional se mide en golpes."),
        ("abc", "En Matricería: ¿cómo se obtiene el costo por golpe?", "Dividiendo el costo total entre los golpes de vida adicional", "Multiplicando el costo total por los golpes", "Sumando el costo y los golpes", "Se reparte el costo entre los golpes que dura."),
        ("abc", "En Matricería: ¿para qué sirve la pieza muestra aprobada en la verificación?", "Para comparar con ella las piezas producidas después de la mantención", "Para reemplazar al plano", "Para medir la parada", "En este caso, La muestra es la referencia."),
        ("abc", "{F} ¿Qué alternativas cumplen la condición obligatoria del certificado?", "AF y AR", "AR y AX", "Solo AX", "En este caso, AX no tiene certificado."),
        ("=", "{F} ¿Cuál es el costo total de AF, con la parada de 10 horas?", "250000+10*50000", "Se suman el costo de la tarea y el de la parada.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuál es el costo total de AR, con la parada de 12 horas?", "700000+12*50000", "Se suman el costo de la tarea y el de la parada.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuesta cada golpe con AF?", "750000//150000", "Se divide el costo total entre los golpes de vida.", " pesos de ejemplo por golpe"),
        ("=", "{F} ¿Cuánto cuesta cada golpe con AR?", "1300000//325000", "Se divide el costo total entre los golpes de vida.", " pesos de ejemplo por golpe"),
        ("abc", "{F} Entre AF y AR, ¿cuál tiene menor costo por golpe?", "AR, con 4 pesos de ejemplo frente a 5 de AF", "AF, porque cuesta menos la tarea", "Ambos cuestan igual por golpe", "AR dura más golpes y su costo por golpe es menor."),
        ("abc", "{F} Un jefe dice: «AX es la más barata, usémosla». ¿Qué respuesta es correcta?", "No corresponde: AX no tiene certificado y se descarta", "Corresponde, porque cuesta menos", "Corresponde, si dura poco", "La condición obligatoria se aplica antes del costo."),
        ("abc", "{F} Falta firmar el registro y el resto de la lista cumple. ¿Qué corresponde?", "No firmar la lista hasta completar el registro", "Firmarla porque el resto cumple", "Borrar ese punto", "Una lista incompleta no se firma."),
        ("=", "{F} Si se elige AR y la matriz da 160.000 golpes al mes, ¿cuántos meses dura la vida adicional? Redondea hacia abajo.", "325000//160000", "Se dividen los golpes de vida entre los golpes por mes.", " meses"),
        ("En una comparación de ejemplo, A cuesta $500.000 y dura 100.000 golpes; B cuesta $900.000 y dura 300.000. ¿Cuál tiene menor costo por golpe?", "B, con 3 frente a 5", "900.000 dividido en 300.000 son 3 y 500.000 dividido en 100.000 son 5."),
    ],
    ctx=("abc", "Un proveedor de ejemplo ofrece una reparación muy barata sin certificado. ¿Qué propones?", "No aceptarla mientras no cumpla la condición obligatoria", "Aceptarla para ahorrar", "Aceptarla si el proveedor es conocido", "Sin certificado no se cumple la condición."),
    sc=[
        ("En Matricería: ¿qué se hace primero al comparar alternativas?", "Descartar las que no cumplen la condición obligatoria", "En este caso, después se comparan los costos."),
        ("En Matricería: ¿cuánto cuesta cada golpe si $600.000 dan 200.000 golpes?", "$3", "Se divide el costo entre los golpes."),
        ("En Matricería: ¿con qué se comparan las piezas producidas tras la mantención?", "Con la pieza muestra aprobada", "En este caso, La muestra es la referencia."),
    ],
    op=("Ficha de ejemplo: dos alternativas con certificado. P: $300.000, 8 horas de parada, vida 140.000 golpes. Q: $500.000, 10 horas de parada, vida 250.000 golpes. Hora de parada: $50.000. Escribe (a) el costo total de P y de Q, (b) el costo por golpe de cada una, (c) cuál conviene, (d) qué compruebas al terminar con la lista de verificación.",
        "(a) P: 300.000 + 8 × 50.000 = 700.000; Q: 500.000 + 10 × 50.000 = 1.000.000. (b) P: 700.000 ÷ 140.000 = 5; Q: 1.000.000 ÷ 250.000 = 4. (c) Q, porque su costo por golpe es menor. (d) Pieza muestra aprobada, medidas, ficha actualizada, registro firmado y residuos gestionados.",
        ["calcula los costos totales", "calcula el costo por golpe", "elige con razón", "usa la lista de verificación"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la parada", "comparar solo el precio", "firmar sin verificar"],
        "Pregunta: «¿cuántos golpes dura cada alternativa?». Si duda, pídele que relea el enunciado."),
    reinforce="Inventa dos alternativas con costo, parada y vida y calcula cuál tiene menor costo por golpe.",
    extend="Explica con un ejemplo por qué las horas de parada se suman al costo de una mantención.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La oficina técnica del «Taller Demo de Matricería» tiene 3 personas diseñadoras de moldes que usan un software de diseño asistido por computador (CAD) con 3 licencias. Cada persona pasa varias horas al día frente a la pantalla. "
     "Los archivos de los clientes son confidenciales. Riesgos anotados: dolor de espalda, cuello y muñecas por la postura, fatiga visual, pérdida de archivos, uso de software sin licencia, filtración de diseños de un cliente y errores de dibujo que se fabrican mal. Se hacen copias de respaldo diarias de los archivos.")
build(
    O5, 1, F,
    use="Aprenderé qué es el dibujo de moldes con software de diseño, qué riesgos tiene el trabajo con computador y cómo se protegen los archivos y los derechos de uso, sin instalar nada.",
    prior=["Sé qué es un plano.", "Sé qué es un molde.", "Sé qué es una copia de seguridad."],
    explain=[
        "El software de diseño asistido por computador, o CAD, permite dibujar piezas y moldes en dos y tres dimensiones, con medidas y vistas. Un dibujo bien hecho es la base para fabricar un molde sin errores; un error de dibujo se repite en la fabricación y es costoso. El diseñador trabaja con la carpeta del proyecto, que incluye el plano de la pieza, el modelo y la lista de piezas del molde.",
        "El trabajo con computador tiene riesgos de postura y de fatiga visual, que se reducen con una buena ergonomía, pausas regulares y una pantalla bien ubicada. También hay riesgos de información: los archivos de un cliente son confidenciales y no se comparten sin autorización; el software se usa solo con licencia; y se hacen copias de seguridad y versiones ordenadas para no perder el trabajo. No se instala software sin autorización de la empresa.",
        f"Aquí se aprenden conceptos, sin usar software real. {EMER} {AVISO}",
    ],
    vocab=[("CAD", "software para dibujar piezas y moldes en computador"), ("licencia", "autorización legal para usar un software"), ("confidencial", "que no debe compartirse sin autorización"), ("copia de seguridad", "copia de un archivo guardada para no perderlo"), ("ergonomía", "organización del trabajo para cuidar el cuerpo"), ("versión", "estado de un archivo en un momento")],
    worked=[
        ("Elegir la medida", "Un diseñador de ejemplo ve que su archivo se dañó y no tiene respaldo. ¿Qué medida habría evitado perder el trabajo?", ["Una copia guardada aparte permite recuperarlo.", "Una copia de seguridad."], "Una copia de seguridad"),
        ("Confidencialidad", "Un compañero de ejemplo quiere enviar el diseño de un cliente a un amigo «para que opine». ¿Corresponde?", ["El diseño del cliente es confidencial.", "No se comparte sin autorización."], "No corresponde"),
    ],
    mistakes=[("Usar un programa sin licencia «solo para practicar».", "Se infringen los derechos de uso y puede haber riesgos.", "Usa solo software autorizado por la empresa o el liceo."),
              ("Trabajar muchas horas seguidas sin pausas.", "Aumentan la fatiga y las molestias de postura.", "Haz pausas regulares, según la indicación del prevencionista.")],
    T=[
        ("abc", "En Matricería: ¿qué es el CAD?", "Un software para dibujar piezas y moldes en computador", "Una máquina que inyecta plástico", "Un tipo de plano en papel", "El CAD es el software de dibujo."),
        ("abc", "En Matricería: ¿qué significa que un archivo sea confidencial?", "Que no debe compartirse sin autorización", "Que es muy pesado", "Que es de uso gratuito", "Confidencial protege la información del cliente."),
        ("abc", "En Matricería: ¿qué es una licencia de software?", "La autorización legal para usarlo", "El nombre del archivo", "La velocidad del computador", "En este caso, sin licencia no se usa."),
        ("abc", "{F} ¿Qué riesgo de la lista se reduce con pausas y buena postura?", "El dolor de espalda y la fatiga visual", "La pérdida de archivos", "El uso de software sin licencia", "En este caso, La ergonomía cuida el cuerpo."),
        ("abc", "{F} ¿Qué medida de la ficha ayuda a no perder los archivos?", "Las copias de respaldo diarias", "Las licencias", "La pantalla grande", "La copia de seguridad permite recuperar."),
        ("abc", "{F} ¿Qué riesgo corresponde a que un diseño de un cliente llegue a otra empresa?", "La filtración de información confidencial", "La fatiga visual", "El dolor de muñecas", "Compartir sin autorización filtra la información."),
        ("=", "{F} La oficina tiene 3 licencias y 3 personas diseñadoras. ¿Cuántas licencias sobran?", "3-3", "Se resta el número de personas a las licencias.", " licencias"),
        ("=", "{F} Cada persona genera 4 copias de respaldo por semana. ¿Cuántas copias generan las 3 personas en 4 semanas?", "3*4*4", "Se multiplican personas, copias por semana y semanas.", " copias"),
        ("abc", "{F} Un diseñador dice: «instalo un programa gratis de internet en el computador de la oficina». ¿Qué respuesta es correcta?", "No corresponde: se instala solo software autorizado por la empresa y con licencia", "Corresponde, porque es gratis", "Corresponde, si lo desinstala después", "Un programa no autorizado puede traer riesgos."),
        ("abc", "{F} Un compañero dice: «mi archivo tiene un error pequeño en una cota, se arregla en la fábrica». ¿Qué respuesta es correcta?", "Es falso: un error de dibujo se fabrica mal; se corrige en el dibujo antes", "Es cierto, porque en la fábrica se arreglan", "Es cierto, si es pequeño", "Un error del dibujo se traslada al molde."),
        ("abc", "En una oficina de ejemplo, una persona dice sentir dolor fuerte en la espalda y no puede levantarse. ¿Qué corresponde según las reglas generales?", "Avisar a un adulto responsable y a emergencias, sin moverla", "Pedirle que siga trabajando", "Darle un medicamento que tengas", "No das diagnósticos ni medicamentos; avisas a quienes pueden ayudar."),
        ("=", "{F} Si el taller guarda cada proyecto en 5 versiones y hay 8 proyectos, ¿cuántas versiones de archivo hay?", "5*8", "Se multiplican las versiones por los proyectos.", " versiones"),
        ("abc", "En Matricería: ¿para qué sirven las versiones ordenadas de un archivo?", "Para saber cuál es la más reciente y no perder cambios", "Para ocupar más espacio", "Para ocultar errores", "El orden de versiones evita confusiones."),
    ],
    ctx=("abc", "Un amigo de ejemplo te ofrece una copia gratis de un programa de diseño pagado. ¿Qué respondes?", "Que no, porque sería uso sin licencia, y que se usa solo software autorizado", "Que sí, porque es gratis", "Que sí, si es solo para practicar", "El software sin licencia no se usa."),
    sc=[
        ("En Matricería: ¿qué protege la copia de seguridad?", "El trabajo ante pérdida o daño del archivo", "En este caso, permite recuperar lo guardado."),
        ("En Matricería: ¿qué hacer con los archivos confidenciales de un cliente?", "No compartirlos sin autorización", "En este caso, protegen el negocio del cliente."),
        ("En Matricería: ¿qué reducen las pausas regulares?", "La fatiga y las molestias de postura", "En este caso, La ergonomía cuida el cuerpo."),
    ],
    op=("Ficha de ejemplo: una oficina de diseño de moldes tiene 4 diseñadores y 4 licencias; cada uno trabaja varias horas frente a la pantalla y guarda sus archivos sin copia de respaldo. Escribe (a) un riesgo para el cuerpo y una medida, (b) un riesgo para la información y una medida, (c) qué haces ante un programa sin licencia, (d) cuántas copias de respaldo hay por semana si cada persona hace 3.",
        "(a) Riesgo: dolor de espalda por la postura; medida: pausas regulares y una buena ergonomía. (b) Riesgo: pérdida de archivos; medida: copias de seguridad ordenadas. (c) No usarlo y avisar a la jefatura. (d) 4 × 3 = 12 copias.",
        ["nombra un riesgo y una medida para el cuerpo", "nombra un riesgo y una medida para la información", "indica qué hacer con el software sin licencia", "calcula las copias"],
        ["hoja con las cuatro respuestas"],
        ["no proponer pausas", "ignorar la licencia", "no calcular bien"],
        "Pregunta: «¿qué se cuida con la ergonomía?». Si duda, pídele que relea el vocabulario."),
    reinforce="Escribe tres medidas para cuidar el cuerpo y tres para cuidar la información en una oficina de diseño.",
    extend="Explica con un ejemplo por qué un error de dibujo se vuelve más costoso en la fabricación.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (plano de molde descrito por escrito, de ejemplo e inventado). Pieza «Tapa-01» de polipropileno (un plástico): 150 mm de largo y 50 mm de ancho; espesor de pared de 2 mm; ángulo de desmoldeo de ejemplo de 2 grados. Contracción del plástico de ejemplo: 2 %. "
     "Molde de 2 cavidades. Líneas de partición: el plano donde se separan las dos mitades del molde. Capas del dibujo: contornos, cotas, ejes y notas. Lista de piezas del molde: 2 placas, 4 columnas, 8 pernos, 2 expulsores. Revisión del plano: B. "
     "Regla: la cavidad se dibuja con la medida de la pieza aumentada por la contracción, porque el plástico se encoge al enfriarse.")
build(
    O5, 2, F,
    use="Aprenderé el vocabulario de un plano de molde: contracción, ángulo de desmoldeo, espesor de pared, línea de partición, capas y lista de piezas, y a calcular una cavidad.",
    prior=["Sé qué es un molde de inyección.", "Sé qué es un plano con cotas.", "Sé calcular un porcentaje de números redondos."],
    explain=[
        "En un plano de molde, la contracción es el porcentaje que se encoge el plástico al enfriarse, por lo que la cavidad se dibuja más grande que la pieza: la medida de la cavidad es la medida de la pieza más su contracción. El ángulo de desmoldeo es una pequeña inclinación de las paredes que permite sacar la pieza del molde sin dañarla. El espesor de pared debe ser parejo para que el plástico enfríe de manera uniforme.",
        "La línea de partición es el plano donde se separan las dos mitades del molde. Las capas ordenan el dibujo en grupos, como contornos, cotas, ejes y notas, que se pueden mostrar u ocultar. La lista de piezas anota las placas, columnas, pernos y expulsores del molde. La revisión indica la versión del plano. Los valores de contracción son de ejemplo y los reales dependen del plástico y del fabricante.",
        f"Aquí solo se aprende vocabulario y se calcula en papel. {EMER} {AVISO}",
    ],
    vocab=[("contracción", "porcentaje que se encoge el plástico al enfriarse"), ("ángulo de desmoldeo", "inclinación de las paredes que facilita sacar la pieza del molde"), ("espesor de pared", "grosor de las paredes de la pieza"), ("línea de partición", "plano donde se separan las dos mitades del molde"), ("capa", "grupo de elementos del dibujo que se puede mostrar u ocultar"), ("lista de piezas del molde", "tabla con las piezas del molde y sus cantidades")],
    worked=[
        ("Medida de la cavidad", "Una pieza de ejemplo mide 100 mm y la contracción es del 3 %. ¿Cuánto debe medir la cavidad?", ["El 3 % de 100 mm son 3 mm.", "100 más 3 son 103."], "103 mm"),
        ("Ángulo de desmoldeo", "Una pieza de ejemplo no tiene ninguna inclinación en sus paredes y se atasca al sacarla del molde. ¿Qué característica de diseño faltó?", ["Falta la inclinación que facilita sacar la pieza.", "Es el ángulo de desmoldeo."], "El ángulo de desmoldeo"),
    ],
    mistakes=[("Dibujar la cavidad con la medida exacta de la pieza.", "El plástico se contrae y la pieza saldría más chica.", "Aumenta la medida de la cavidad con la contracción."),
              ("Dibujar paredes sin inclinación.", "La pieza se atasca al sacarla del molde.", "Incluye el ángulo de desmoldeo.")],
    T=[
        ("abc", "En Matricería: ¿qué es la contracción del plástico?", "El porcentaje que se encoge al enfriarse", "El porcentaje que se dilata al calentarse", "El peso de la pieza", "La razón es que contracción significa encogerse."),
        ("abc", "En Matricería: ¿para qué sirve el ángulo de desmoldeo?", "Para facilitar sacar la pieza del molde sin dañarla", "Para calentar el plástico", "Para sujetar la pieza en la prensa", "La inclinación evita que la pieza se atasque."),
        ("abc", "En Matricería: ¿qué es la línea de partición?", "El plano donde se separan las dos mitades del molde", "El borde de la pieza", "La capa de cotas", "La línea de partición define la separación del molde."),
        ("=", "{F} ¿Cuántos mm es la contracción del largo de 150 mm, con 2 %?", "150*2//100", "Se multiplica el largo por el porcentaje y se divide por 100.", " mm"),
        ("=", "{F} ¿Cuánto debe medir el largo de la cavidad?", "150+3", "Se suma la contracción al largo de la pieza.", " mm"),
        ("=", "{F} ¿Cuántos mm es la contracción del ancho de 50 mm, con 2 %?", "50*2//100", "Se multiplica el ancho por el porcentaje y se divide por 100.", " mm"),
        ("=", "{F} ¿Cuánto debe medir el ancho de la cavidad?", "50+1", "Se suma la contracción al ancho de la pieza.", " mm"),
        ("=", "{F} ¿Cuántas piezas suma la lista de piezas del molde?", "2+4+8+2", "Se suman las cantidades de las cuatro piezas.", " piezas"),
        ("abc", "{F} ¿Por qué se dibuja la cavidad más grande que la pieza?", "Porque el plástico se encoge al enfriarse", "Porque la pieza se dilata al enfriarse", "Porque así cuesta menos el molde", "La contracción hace que la pieza salga más chica."),
        ("abc", "{F} Un diseñador dibuja la cavidad con 150 mm exactos. ¿Qué respuesta es correcta?", "Es un error: la pieza saldría más chica por la contracción; debe medir 153 mm", "Es correcto, porque la pieza mide 150 mm", "Es correcto, si el molde es nuevo", "La cavidad debe compensar la contracción."),
        ("abc", "{F} Un diseñador propone paredes de 2 mm en una zona y de 6 mm en otra «para ahorrar material». ¿Qué observación es correcta?", "El espesor desigual enfría de manera irregular y puede deformar la pieza; conviene un espesor parejo", "Es mejor, porque ahorra material", "No importa, el plástico se adapta", "El espesor parejo ayuda a un enfriamiento uniforme."),
        ("=", "{F} Si el molde tiene 2 cavidades y se necesitan 10.000 piezas, ¿cuántos ciclos se requieren?", "10000//2", "Se dividen las piezas entre las cavidades.", " ciclos"),
        ("En un plano de ejemplo, una pieza de 200 mm con contracción del 2 % tiene una cavidad dibujada de 202 mm. ¿Es correcta?", "No, debería medir 204 mm", "El 2 % de 200 son 4 y 200 más 4 son 204."),
    ],
    ctx=("abc", "Un compañero de ejemplo dice: «da lo mismo dibujar la cavidad exacta, el plástico no cambia». ¿Qué respondes?", "Que el plástico se contrae al enfriarse y la cavidad debe compensarlo", "Que tiene razón", "Que el plástico se dilata", "La contracción es una característica del plástico."),
    sc=[
        ("En Matricería: ¿cuánto debe medir una cavidad para una pieza de 300 mm con 2 % de contracción?", "306 mm", "Se suma el 2 % de 300, que son 6 mm."),
        ("En Matricería: ¿qué permite el ángulo de desmoldeo?", "Sacar la pieza sin dañarla", "La inclinación evita que se atasque."),
        ("En Matricería: ¿qué ordena una capa del dibujo?", "Grupos de elementos que se muestran u ocultan", "Facilita leer y modificar el dibujo."),
    ],
    op=("Ficha de ejemplo: pieza de 200 mm de largo y 100 mm de ancho; contracción del 3 %; molde de 4 cavidades; lista de piezas del molde: 2 placas, 4 columnas, 6 pernos. Escribe (a) cuánto debe medir el largo de la cavidad, (b) cuánto el ancho, (c) cuántas piezas suma la lista, (d) por qué se incluye un ángulo de desmoldeo.",
        "(a) 3 % de 200 son 6; 206 mm. (b) 3 % de 100 son 3; 103 mm. (c) 2 + 4 + 6 = 12 piezas. (d) Para facilitar sacar la pieza del molde sin dañarla.",
        ["calcula el largo de la cavidad", "calcula el ancho", "suma las piezas", "explica el desmoldeo"],
        ["hoja con las cuatro respuestas"],
        ["no aplicar la contracción", "calcular el porcentaje al revés", "no explicar el desmoldeo"],
        "Pregunta: «¿la cavidad es más grande o más chica que la pieza?». Si duda, pídele que relea la contracción."),
    reinforce="Inventa una pieza y una contracción y calcula las medidas de la cavidad.",
    extend="Explica con un ejemplo por qué el espesor de pared parejo ayuda a que la pieza no se deforme.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (dibujo de molde descrito por escrito, de ejemplo e inventado, con errores). Pieza «Caja-02»: 150 mm de largo, 100 mm de ancho; contracción de ejemplo 2 %. El dibujo anota: cavidad de 150 mm de largo y de 100 mm de ancho; espesor de pared 2 mm en un tramo y 5 mm en otro; paredes sin ángulo de desmoldeo; la cota del ancho aparece dos veces, una de 100 mm y otra de 105 mm; "
     "lista de piezas: 4 columnas, mientras el dibujo muestra 6; revisión del dibujo: A, y del plano del cliente: B; capas: todas mezcladas en una sola. Archivo guardado sin copia de respaldo.")
build(
    O5, 3, F,
    use="Aprenderé a revisar un dibujo de molde en papel detectando errores de contracción, desmoldeo, espesor, cotas, lista de piezas, revisión y orden del archivo.",
    prior=["Sé qué es la contracción y el desmoldeo.", "Sé calcular una cavidad.", "Sé qué es una lista de piezas."],
    explain=[
        "Revisar un dibujo de molde es comprobar punto por punto que cumpla las reglas del oficio y los datos del cliente: la cavidad debe compensar la contracción, las paredes deben tener ángulo de desmoldeo y espesor parejo, cada cota debe aparecer una sola vez con un solo valor, la lista de piezas debe coincidir con el dibujo, la revisión debe ser la del plano vigente y las capas deben estar ordenadas.",
        "Los errores se registran con el dato y el motivo y se informan a quien emitió el dibujo, que lo corrige y emite una nueva revisión; no se corrigen por cuenta propia. El archivo debe tener copia de respaldo. Un error no detectado en el dibujo se fabrica mal y puede costar un molde completo. La revisión es solo documental.",
        f"No se usa software real. {EMER} {AVISO}",
    ],
    vocab=[("revisión de dibujo", "comprobación de que un dibujo cumple las reglas y los datos del cliente"), ("cota duplicada", "medida anotada dos veces, a veces con valores distintos"), ("capas ordenadas", "elementos del dibujo organizados en grupos"), ("nueva revisión", "versión corregida de un dibujo"), ("respaldo", "copia guardada aparte para no perder el archivo")],
    worked=[
        ("Cota duplicada", "Un dibujo de ejemplo anota 40 mm y 42 mm para la misma cota. ¿Qué error es?", ["La misma cota tiene dos valores.", "Es una cota duplicada con valores distintos."], "Cota duplicada con valores distintos"),
        ("Lista de piezas", "El dibujo de ejemplo muestra 8 pernos y la lista anota 6. ¿Qué hay?", ["Los números no coinciden.", "Es una incoherencia entre dibujo y lista."], "Una incoherencia"),
    ],
    mistakes=[("Corregir el dibujo de otra persona sin avisar.", "Solo quien emitió el dibujo lo modifica.", "Registra el error e infórmalo."),
              ("Dejar el archivo sin respaldo.", "Si se daña, se pierde el trabajo.", "Guarda una copia de seguridad.")],
    T=[
        ("abc", "En Matricería: ¿qué es una cota duplicada?", "Una medida anotada dos veces, a veces con valores distintos", "Una medida que se repite sin errores", "Una cota sin unidad", "En este caso, duplicar puede generar contradicciones."),
        ("abc", "En Matricería: ¿qué se hace con un error detectado en el dibujo de otra persona?", "Se registra e informa a quien lo emitió", "Se corrige sin avisar", "Se ignora", "Quien emitió el dibujo lo corrige."),
        ("abc", "En Matricería: ¿para qué sirven las capas ordenadas?", "Para mostrar u ocultar grupos de elementos del dibujo", "Para aumentar el tamaño del archivo", "Para cambiar los colores", "Facilitan leer y modificar el dibujo."),
        ("=", "{F} ¿Cuánto debe medir el largo de la cavidad, con 150 mm de largo y 2 % de contracción?", "150+150*2//100", "Se suma la contracción al largo de la pieza.", " mm"),
        ("=", "{F} ¿Cuánto debe medir el ancho de la cavidad, con 100 mm de ancho y 2 % de contracción?", "100+100*2//100", "Se suma la contracción al ancho de la pieza.", " mm"),
        ("abc", "{F} ¿Qué error hay en la cavidad dibujada de 150 mm por 100 mm?", "No compensa la contracción", "Es mayor de lo necesario", "Tiene el ángulo de desmoldeo", "Una cavidad igual a la pieza dejaría la pieza más chica."),
        ("abc", "{F} ¿Qué error hay en las paredes?", "Falta el ángulo de desmoldeo y el espesor no es parejo", "Todo está correcto", "Falta solo una capa", "La pieza se atascaría y se deformaría."),
        ("abc", "{F} ¿Qué error hay con la cota del ancho?", "Aparece dos veces con valores distintos, 100 mm y 105 mm", "Aparece una sola vez", "Falta la unidad", "En este caso, las dos cotas se contradicen."),
        ("=", "{F} ¿Cuántas columnas más hay en el dibujo que en la lista de piezas?", "6-4", "Se resta lo anotado en la lista a lo que muestra el dibujo.", " columnas"),
        ("abc", "{F} ¿Qué corresponde por la diferencia de revisión, A en el dibujo y B en el plano del cliente?", "Informarlo y pedir el dibujo actualizado antes de fabricar", "Fabricar con el dibujo A", "Cambiar a mano la letra a B", "Una revisión distinta puede tener datos desactualizados."),
        ("abc", "{F} Un diseñador dice: «el archivo no tiene respaldo, pero no se va a dañar». ¿Qué respuesta es correcta?", "Es falso: conviene tener una copia de seguridad porque el archivo puede dañarse", "Es cierto, porque los archivos no se dañan", "Es cierto, si el computador es nuevo", "El respaldo evita perder el trabajo."),
        ("abc", "{F} Un compañero propone corregir el dibujo ahora y avisar después. ¿Qué respuesta es correcta?", "No corresponde: se registran los errores y se informan a quien lo emitió para que lo corrija", "Corresponde, porque es más rápido", "Corresponde, si lo corrige bien", "Solo quien emitió el dibujo lo modifica."),
        ("En un dibujo de ejemplo todas las capas están mezcladas en una sola. ¿Qué dificultad trae?", "Dificulta leer y modificar el dibujo", "No se pueden mostrar u ocultar los grupos de elementos."),
    ],
    ctx=("abc", "El jefe de ejemplo dice: «ese dibujo tiene errores, pero fabriquemos igual y ajustamos en el molde». ¿Qué propones?", "Registrar los errores y pedir un dibujo corregido antes de fabricar", "Fabricar igual", "Ajustar el molde a ojo", "Un error de dibujo se vuelve costoso en el molde."),
    sc=[
        ("En Matricería: ¿qué debe compensar la cavidad?", "La contracción del plástico", "La pieza se encoge al enfriarse."),
        ("En Matricería: ¿quién corrige un dibujo con errores?", "Quien lo emitió, con una nueva revisión", "En este caso, así queda registro del cambio."),
        ("En Matricería: ¿qué evita perder un archivo dañado?", "Una copia de seguridad", "En este caso, permite recuperar el trabajo."),
    ],
    op=("Ficha de ejemplo: dibujo de una pieza de 100 mm por 60 mm, contracción 2 %. El dibujo anota la cavidad en 100 por 60, paredes sin ángulo de desmoldeo, 8 pernos mientras la lista anota 6, y la revisión A frente a la B del cliente. Escribe (a) el largo correcto de la cavidad, (b) el error de las paredes, (c) la diferencia de pernos, (d) qué haces con la revisión distinta.",
        "(a) El 2 % de 100 son 2; 102 mm. (b) Falta el ángulo de desmoldeo. (c) 8 − 6 = 2 pernos de diferencia. (d) Informar a quien emitió el dibujo y pedir la versión actualizada antes de fabricar.",
        ["calcula el largo de la cavidad", "nombra el error de las paredes", "calcula la diferencia", "indica qué hacer con la revisión"],
        ["hoja con las cuatro respuestas"],
        ["no sumar la contracción", "no detectar el desmoldeo", "corregir por cuenta propia"],
        "Pregunta: «¿la cavidad es igual a la pieza o más grande?». Si duda, pídele que relea la regla."),
    reinforce="Escribe cinco puntos que revisarías en un dibujo de molde.",
    extend="Explica con un ejemplo por qué un error de dibujo es más barato de corregir antes de fabricar.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (cálculo de un molde de ejemplo, inventado). Pieza de 250 mm por 100 mm, de 20 mm de alto y paredes de 2 mm; volumen de plástico de la pieza de ejemplo: 48.000 mm cúbicos. Densidad de ejemplo del plástico: 1 g por cm cúbico, es decir 1 g por cada 1.000 mm cúbicos. Contracción de ejemplo: 2 %. "
     "Molde de 4 cavidades; volumen del canal de entrada por ciclo: 28.000 mm cúbicos. Pedido: 24.000 piezas. Ciclo: 30 segundos. Diseño del molde en CAD: 36 horas de diseñador a $12.000 la hora. Precio del plástico: $2.000 por kg. Inyectora con volumen máximo de 250 g.")
build(
    O5, 4, F,
    use="Aprenderé a calcular las medidas de la cavidad con la contracción, la masa de inyección, los ciclos de un pedido y el costo de diseño y de plástico, con datos de ejemplo.",
    prior=["Sé calcular la contracción.", "Sé calcular masa de inyección.", "Sé calcular ciclos y costos."],
    explain=[
        "Las medidas de la cavidad se obtienen sumando a las de la pieza su contracción: la medida por el porcentaje dividido por 100. La masa de una pieza se calcula con su volumen y la densidad: con 1 g por cada 1.000 mm cúbicos, la masa en gramos es el volumen dividido por 1.000. La masa de inyección por ciclo suma las piezas de todas las cavidades y el canal de entrada.",
        "Los ciclos del pedido son las piezas pedidas divididas por las cavidades. El tiempo de producción son los ciclos por el tiempo de ciclo. El costo de diseño es las horas por el costo de cada hora, y el costo del plástico se calcula con los gramos y el precio por gramo. La masa por ciclo no debe superar el volumen máximo de la inyectora. Los valores son de ejemplo.",
        f"Es un cálculo de papel. {EMER} {AVISO}",
    ],
    vocab=[("masa de la pieza", "volumen de la pieza dividido por 1.000, en gramos, con la densidad de ejemplo"), ("masa de inyección", "masa de las piezas más la del canal de entrada"), ("ciclos del pedido", "piezas pedidas divididas por las cavidades"), ("costo de diseño", "horas de diseño por el costo de cada hora"), ("volumen máximo de la inyectora", "masa máxima que la máquina puede inyectar por ciclo")],
    worked=[
        ("Masa de una pieza", "Una pieza de ejemplo tiene 30.000 mm cúbicos y la densidad es de 1 g por 1.000 mm cúbicos. ¿Cuántos g pesa?", ["Se divide el volumen entre 1.000.", "30.000 dividido en 1.000 son 30."], "30 g"),
        ("Ciclos del pedido", "Se piden 6.000 piezas y el molde tiene 3 cavidades. ¿Cuántos ciclos se necesitan?", ["Se dividen las piezas entre las cavidades.", "6.000 dividido en 3 son 2.000."], "2.000 ciclos"),
    ],
    mistakes=[("Olvidar el canal de entrada en la masa de inyección.", "El canal también se inyecta.", "Suma la masa del canal a la de las piezas."),
              ("Usar la medida de la pieza para dibujar la cavidad.", "No se compensa la contracción.", "Suma la contracción a cada medida.")],
    T=[
        ("abc", "En Matricería: ¿cómo se obtiene la masa de una pieza con la densidad de ejemplo?", "Dividiendo su volumen en mm cúbicos entre 1.000", "Multiplicando su volumen por 1.000", "Sumando 1.000 a su volumen", "La densidad de ejemplo relaciona gramos y mm cúbicos."),
        ("abc", "En Matricería: ¿cómo se obtienen los ciclos de un pedido?", "Dividiendo las piezas pedidas entre las cavidades", "Multiplicando las piezas por las cavidades", "Sumando piezas y cavidades", "Cada ciclo produce tantas piezas como cavidades."),
        ("abc", "En Matricería: ¿qué se compara con el volumen máximo de la inyectora?", "La masa de inyección por ciclo", "La masa de una sola pieza", "El peso del molde", "La máquina debe inyectar todo el plástico del ciclo."),
        ("=", "{F} ¿Cuántos mm es la contracción del largo de 250 mm, con 2 %?", "250*2//100", "Se multiplica el largo por el porcentaje y se divide por 100.", " mm"),
        ("=", "{F} ¿Cuánto debe medir el largo de la cavidad?", "250+5", "Se suma la contracción al largo.", " mm"),
        ("=", "{F} ¿Cuánto debe medir el ancho de la cavidad, con 100 mm y 2 %?", "100+100*2//100", "Se suma la contracción al ancho.", " mm"),
        ("=", "{F} ¿Cuántos g pesa una pieza?", "48000//1000", "Se divide el volumen entre 1.000.", " g"),
        ("=", "{F} ¿Cuántos g pesa el canal de entrada por ciclo?", "28000//1000", "Se divide el volumen del canal entre 1.000.", " g"),
        ("=", "{F} ¿Cuántos g se inyectan por ciclo, con las 4 piezas y el canal?", "4*48+28", "Se suman las 4 piezas y el canal.", " g"),
        ("abc", "{F} ¿Supera la masa por ciclo el volumen máximo de la inyectora de 250 g?", "No, 220 g es menor que 250 g", "Sí, porque 220 es mayor que 200", "No se puede saber", "En este caso, 220 no supera 250."),
        ("=", "{F} ¿Cuántos ciclos se necesitan para el pedido de 24.000 piezas?", "24000//4", "Se dividen las piezas entre las cavidades.", " ciclos"),
        ("=", "{F} ¿Cuánto cuesta el diseño del molde en CAD, con 36 horas a $12.000 la hora?", "36*12000", "Se multiplican las horas por el costo de cada hora.", " pesos de ejemplo"),
        ("abc", "{F} Un jefe dice: «la masa por ciclo es la de una pieza, 48 g». ¿Qué respuesta es correcta?", "Es falso: son 4 piezas más el canal, es decir 220 g", "Es cierto, porque una pieza pesa 48 g", "Es cierto, si hay una sola cavidad", "El ciclo inyecta todas las cavidades y el canal."),
    ],
    ctx=("abc", "El cliente de ejemplo pregunta cuánto plástico se necesita para el pedido de 24.000 piezas. ¿Qué dato necesitas además de la masa de una pieza?", "El número de cavidades y la masa del canal, para calcular los ciclos y el plástico total", "El color de la pieza", "El nombre de la inyectora", "El plástico total depende de los ciclos y de la masa por ciclo."),
    sc=[
        ("En Matricería: ¿cuánto pesan 30.000 mm cúbicos con la densidad de ejemplo?", "30 g", "En este caso, Se divide entre 1.000."),
        ("En Matricería: ¿qué parte del plástico se suma a las piezas para obtener la masa de inyección de un ciclo?", "El canal de entrada", "En este caso, también se inyecta ese plástico."),
        ("En Matricería: ¿cómo se obtiene la medida de la cavidad?", "Sumando la contracción a la medida de la pieza", "La pieza se encoge al enfriarse."),
    ],
    op=("Ficha de ejemplo: pieza de 300 mm por 150 mm; contracción 2 %; volumen de la pieza 60.000 mm cúbicos; canal por ciclo 20.000 mm cúbicos; molde de 2 cavidades; pedido de 10.000 piezas; inyectora con volumen máximo de 200 g. Escribe (a) las medidas de la cavidad, (b) la masa de inyección por ciclo, (c) si cabe en la inyectora, (d) cuántos ciclos necesita el pedido.",
        "(a) Largo: 300 + 6 = 306 mm; ancho: 150 + 3 = 153 mm. (b) 2 × 60 + 20 = 140 g. (c) Sí, 140 g es menor que 200 g. (d) 10.000 ÷ 2 = 5.000 ciclos.",
        ["calcula las medidas", "calcula la masa por ciclo", "compara con la inyectora", "calcula los ciclos"],
        ["hoja con las cuatro respuestas"],
        ["no aplicar la contracción", "olvidar el canal", "dividir al revés"],
        "Pregunta: «¿cuántos gramos tiene cada pieza?». Si duda, pídele que divida el volumen entre 1.000."),
    reinforce="Inventa una pieza con volumen y contracción y calcula las medidas de la cavidad y la masa de la pieza.",
    extend="Explica con un ejemplo por qué la masa por ciclo debe compararse con el volumen máximo de la inyectora.",
)

# ============================================================ OAM-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Taller Demo de Matricería» genera estos residuos en un mes: recortes y virutas de acero; aceites usados de prensas e inyectoras; líquido de enfriamiento usado; trapos con aceite y solvente; plásticos (bebederos, rebabas y piezas rechazadas); discos abrasivos gastados; envases vacíos de solventes; y cartón y papel. "
     "Peligros anotados: derrames, contacto con solventes, incendio por trapos con solvente guardados juntos, cortes con recortes de chapa, almacenamiento mezclado y vertido al desagüe. La empresa tiene un punto de acopio señalizado.")
build(
    O6, 1, F,
    use="Aprenderé qué son los residuos de matrices y moldes, por qué algunos son peligrosos, qué riesgos tiene su manejo y cuál es la responsabilidad del taller y de las personas.",
    prior=["Sé qué es un residuo.", "Sé que algunos residuos no van a la basura común.", "Sé qué es un punto de acopio."],
    explain=[
        "Un residuo es todo material que se deja de usar. Los residuos peligrosos pueden dañar a las personas o al ambiente: por ejemplo los aceites usados, los solventes, los trapos contaminados con ellos y los envases que los contuvieron. Los no peligrosos, como los recortes de acero limpios, el plástico limpio o el cartón, se pueden reciclar con más facilidad. El manejo correcto de unos y otros se rige por la norma vigente y la autoridad competente.",
        "Los riesgos al manejar residuos son los derrames, el contacto con solventes, el incendio por guardar trapos con solvente juntos, los cortes con recortes de chapa y la mezcla de residuos incompatibles. Los controles incluyen un punto de acopio señalizado, recipientes adecuados y rotulados, orden y limpieza, capacitación y EPP. Nunca se vierte un residuo líquido al desagüe ni se bota uno peligroso a la basura común. Cada persona responde por separar bien sus residuos.",
        f"El manejo de residuos peligrosos lo hace personal capacitado; este cuaderno no enseña a hacerlo. {EMER} {AVISO}",
    ],
    vocab=[("residuo", "material que se deja de usar"), ("residuo peligroso", "residuo que puede dañar a las personas o al ambiente"), ("residuo no peligroso", "residuo sin ese riesgo, como el cartón o el acero limpio"), ("punto de acopio", "lugar señalizado donde se guardan los residuos antes de retirarlos"), ("derrame", "salida de un líquido fuera de su recipiente"), ("segregación", "separación de los residuos por tipo")],
    worked=[
        ("Clasificar", "Un residuo de ejemplo es un trapo con aceite y solvente. ¿Es peligroso o no peligroso?", ["Está contaminado con aceite y solvente.", "Es un residuo peligroso."], "Peligroso"),
        ("Qué no hacer", "Un trabajador de ejemplo quiere verter aceite usado al desagüe para limpiar rápido. ¿Corresponde?", ["El aceite daña el ambiente.", "No se vierte al desagüe."], "No corresponde"),
    ],
    mistakes=[("Guardar trapos con solvente en una bolsa común junto a cartón.", "Hay riesgo de incendio y de mala disposición.", "Se separan y van al punto de acopio, en recipientes rotulados."),
              ("Creer que leer sobre residuos habilita para manejar sustancias peligrosas.", "Su manejo lo hace personal capacitado con la norma vigente.", "Aprende el concepto y deja la tarea a quien corresponde.")],
    T=[
        ("abc", "En Matricería: ¿qué es un residuo peligroso?", "Un residuo que puede dañar a las personas o al ambiente", "Cualquier residuo grande", "El residuo que más pesa", "La peligrosidad se define por el daño posible."),
        ("abc", "En Matricería: ¿qué es la segregación de residuos?", "La separación de los residuos por tipo", "La mezcla de todos los residuos", "El retiro de los residuos del taller", "En este caso, segregar es separar por tipo."),
        ("abc", "En Matricería: ¿qué es un punto de acopio?", "Un lugar señalizado donde se guardan los residuos antes de retirarlos", "Un lugar donde se queman los residuos", "Un recipiente de basura común", "En este caso, El acopio ordena y señaliza."),
        ("abc", "{F} ¿Cuál de los residuos de la ficha es no peligroso?", "El cartón y el papel", "El aceite usado", "Los trapos con solvente", "El cartón limpio no es peligroso."),
        ("abc", "{F} ¿Cuál de los residuos de la ficha es peligroso?", "Los envases vacíos de solventes", "Los recortes limpios de acero", "El papel", "Los envases de solvente conservan restos."),
        ("abc", "{F} ¿Qué peligro de la lista se evita con un punto de acopio señalizado?", "El almacenamiento mezclado", "El ruido", "La falta de luz", "El acopio ordena y separa los residuos."),
        ("=", "{F} La ficha lista 8 tipos de residuos. Si 4 son peligrosos, ¿cuántos no lo son?", "8-4", "Se resta los peligrosos al total de tipos.", " tipos"),
        ("=", "{F} El taller genera 15 kg de trapos con solvente por semana. ¿Cuántos kg genera en 4 semanas?", "15*4", "Se multiplican los kg por semana por las semanas.", " kg"),
        ("abc", "{F} Una persona propone botar los trapos con solvente a la basura común porque «son pocos». ¿Qué respuesta es correcta?", "No corresponde: son residuos peligrosos y van al punto de acopio, aunque sean pocos", "Corresponde, porque son pocos", "Corresponde, si los envuelve", "La peligrosidad no depende de la cantidad."),
        ("abc", "{F} Un aprendiz dice: «el líquido de enfriamiento usado lo vierto al desagüe, se va con el agua». ¿Qué respuesta es correcta?", "Es falso: el líquido usado es un residuo que se almacena y gestiona según la norma vigente", "Es cierto, porque se diluye", "Es cierto, si hay poco", "Verter líquidos usados daña el ambiente."),
        ("abc", "En una visita a un taller de ejemplo, se derrama solvente y una persona se desmaya. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a sacarla", "Limpiar el derrame con las manos", "Los vapores pueden afectarte a ti también; se pide ayuda."),
        ("=", "{F} El punto de acopio tiene 6 recipientes rotulados y cada uno guarda 20 kg. ¿Cuántos kg caben en total?", "6*20", "Se multiplican los recipientes por los kg de cada uno.", " kg"),
        ("abc", "En Matricería: ¿quién maneja los residuos peligrosos?", "Personal capacitado, con la norma vigente", "Cualquier persona sin formación", "Un estudiante sin supervisión", "El manejo exige formación y autorización."),
    ],
    ctx=("abc", "Un compañero de ejemplo dice: «junto todos los residuos en un solo contenedor para ahorrar tiempo». ¿Qué respondes?", "Que se separan por tipo y los peligrosos van al punto de acopio, en recipientes rotulados", "Que sí, ahorra tiempo", "Que da lo mismo", "En este caso, mezclar residuos puede ser peligroso."),
    sc=[
        ("En Matricería: ¿qué hacer con un residuo peligroso?", "Llevarlo al punto de acopio en un recipiente rotulado", "No se bota a la basura común."),
        ("En Matricería: ¿qué es un derrame?", "Salida de un líquido fuera de su recipiente", "Puede dañar a personas y ambiente."),
        ("En Matricería: ¿quién maneja residuos peligrosos?", "Personal capacitado", "En este caso, exige formación y norma vigente."),
    ],
    op=("Ficha de ejemplo: un taller genera recortes de acero limpios, aceite usado, trapos con aceite, cartón y plásticos rechazados. Escribe (a) cuáles son peligrosos, (b) cuáles no, (c) un control administrativo y uno de ingeniería para los residuos, (d) qué no se hace nunca con el aceite usado. No describas cómo se manipulan.",
        "(a) El aceite usado y los trapos con aceite. (b) Los recortes de acero limpios, el cartón y los plásticos rechazados limpios. (c) Administrativo: capacitación y rotulado; ingeniería: un punto de acopio con bandeja de contención. (d) Nunca se vierte al desagüe ni se bota a la basura común.",
        ["clasifica los residuos peligrosos", "clasifica los no peligrosos", "propone controles", "indica lo que no se hace"],
        ["hoja con las cuatro respuestas"],
        ["mezclar todo en una sola categoría", "proponer verter el aceite", "describir cómo se manipulan"],
        "Pregunta: «¿esto está contaminado o limpio?». Si duda, pídele que relea la definición de residuo peligroso."),
    reinforce="Escribe cinco residuos de un taller y clasifícalos como peligrosos o no peligrosos.",
    extend="Explica con un ejemplo por qué los trapos con solvente no se guardan junto al cartón.",
)

# ============================================================ OAM-06, clase 2
F = ("Ficha 2 (documentos de residuos de ejemplo, inventados). Jerarquía de manejo de residuos, de lo más a lo menos deseable: reducir (generar menos), reutilizar (usar de nuevo), reciclar (convertir en un material nuevo), valorizar (aprovechar su energía o sus componentes) y eliminar (disponer finalmente). "
     "Etiqueta de un recipiente de ejemplo: nombre del residuo, símbolo de peligro, fecha de inicio de acopio y responsable. Registro de retiro: fecha, tipo de residuo, cantidad en kg, empresa autorizada que lo retira y firma. "
     "Hoja de datos de seguridad (HDS): informa peligros y manejo seguro de un producto. Plan de manejo de residuos del taller: lista de residuos, recipientes, punto de acopio y responsables.")
build(
    O6, 2, F,
    use="Aprenderé la jerarquía de manejo de residuos, a leer una etiqueta y un registro de retiro y qué documentos y roles intervienen, sin manipular ningún residuo.",
    prior=["Sé qué es un residuo peligroso.", "Sé qué es un punto de acopio.", "Sé leer una tabla."],
    explain=[
        "La jerarquía de manejo de residuos ordena las opciones de la más a la menos deseable: reducir lo que se genera, reutilizar, reciclar, valorizar y, como último recurso, eliminar. Cada recipiente de residuos lleva una etiqueta con el nombre del residuo, un símbolo de peligro si corresponde, la fecha de inicio de acopio y un responsable. El registro de retiro anota cuánto y qué se retira, y la empresa autorizada que lo hace.",
        "La hoja de datos de seguridad informa los peligros de un producto y cómo manejarlo. El plan de manejo de residuos del taller reúne todo: qué residuos hay, en qué recipientes, en qué punto de acopio y quién responde. El prevencionista asesora, el supervisor hace cumplir el plan y cada persona separa bien sus residuos. Los residuos peligrosos solo los retira una empresa autorizada.",
        f"Aquí se leen documentos; no se manipulan residuos. {EMER} {AVISO}",
    ],
    vocab=[("reducir", "generar menos residuos"), ("reutilizar", "usar de nuevo un material sin transformarlo"), ("reciclar", "convertir un residuo en un material nuevo"), ("valorizar", "aprovechar la energía o los componentes de un residuo"), ("eliminar", "disponer finalmente un residuo, como último recurso"), ("empresa autorizada", "empresa que cuenta con permiso para retirar y tratar residuos")],
    worked=[
        ("Ordenar la jerarquía", "Un taller de ejemplo puede reducir, reciclar o eliminar un residuo. ¿Cuál es la opción más deseable?", ["La jerarquía parte por generar menos.", "Es reducir."], "Reducir"),
        ("Leer un registro", "Un registro de ejemplo anota 30 kg de aceite usado retirados por una empresa autorizada. ¿Qué dato falta para que sea completo?", ["Falta lo que acredite la fecha y la firma.", "Sin fecha ni firma el registro no está completo."], "La fecha y la firma"),
    ],
    mistakes=[("Elegir eliminar primero porque «es lo más fácil».", "Eliminar es el último recurso de la jerarquía.", "Prefiere reducir, reutilizar o reciclar si es posible."),
              ("Entregar residuos peligrosos a cualquier persona que los retire.", "Solo una empresa autorizada puede retirarlos.", "Verifica que la empresa esté autorizada y registra el retiro.")],
    T=[
        ("abc", "En Matricería: ¿qué es reciclar un residuo?", "Convertirlo en un material nuevo", "Usarlo de nuevo sin transformarlo", "Disponerlo finalmente", "En este caso, reciclar transforma el residuo."),
        ("abc", "En Matricería: ¿cuál es el último recurso de la jerarquía de manejo de residuos?", "Eliminar", "Reducir", "Reutilizar", "En este caso, eliminar es lo menos deseable."),
        ("abc", "En Matricería: ¿qué es una empresa autorizada para el retiro de residuos?", "Una empresa con permiso para retirarlos y tratarlos", "Cualquier empresa de transporte", "El taller que los generó", "La autorización garantiza un manejo legal."),
        ("abc", "{F} ¿Qué datos lleva la etiqueta de un recipiente?", "Nombre del residuo, símbolo de peligro, fecha de inicio de acopio y responsable", "Solo el nombre del taller", "Solo el color del recipiente", "La etiqueta identifica y da trazabilidad."),
        ("abc", "{F} ¿Qué documento informa los peligros de un producto?", "La hoja de datos de seguridad", "El registro de retiro", "La etiqueta del recipiente", "La HDS describe peligros y manejo seguro."),
        ("abc", "{F} ¿Qué anota el registro de retiro?", "Fecha, tipo, cantidad, empresa autorizada y firma", "El plano del taller", "La lista de los trabajadores", "En este caso, Es el comprobante del retiro."),
        ("=", "{F} El registro anota 40 kg de aceite, 25 kg de trapos y 15 kg de solventes retirados. ¿Cuántos kg suman?", "40+25+15", "Se suman los kg de los tres residuos.", " kg"),
        ("=", "{F} El taller genera 120 kg de plástico al mes y con una mejora reduce el 25 %. ¿Cuántos kg genera después?", "120-120*25//100", "Se resta el 25 % al total.", " kg"),
        ("abc", "{F} Un taller reutiliza envases limpios para guardar tornillos. ¿En qué nivel de la jerarquía está?", "Reutilizar", "Reciclar", "Eliminar", "Usa el envase de nuevo sin transformarlo."),
        ("abc", "{F} Un supervisor dice: «el retiro lo hace un conocido con su camioneta, es más barato». ¿Qué respuesta es correcta?", "No corresponde: los residuos peligrosos solo los retira una empresa autorizada, con registro", "Corresponde, porque es más barato", "Corresponde, si firma", "Un retiro no autorizado es ilegal y riesgoso."),
        ("abc", "{F} Un recipiente de residuos no tiene etiqueta. ¿Qué corresponde?", "Rotularlo con el nombre, el peligro, la fecha y el responsable antes de seguir", "Dejarlo así", "Cambiar el color del recipiente", "Sin etiqueta no se sabe qué contiene."),
        ("=", "{F} Si el taller recicla 30 kg de plástico al mes durante 6 meses, ¿cuántos kg recicla?", "30*6", "Se multiplican los kg por mes por los meses.", " kg"),
        ("En un registro de ejemplo hay 3 retiros de 20 kg cada uno. ¿Cuántos kg se retiraron en total?", "60 kg", "En este caso, 3 por 20 son 60."),
    ],
    ctx=("abc", "El jefe de ejemplo propone eliminar todos los residuos porque «reciclar da trabajo». ¿Qué propones?", "Seguir la jerarquía: reducir, reutilizar y reciclar antes de eliminar", "Eliminar todo", "Quemar los residuos", "La jerarquía prioriza lo más deseable."),
    sc=[
        ("En Matricería: ¿cuál es la opción más deseable de la jerarquía?", "Reducir", "Generar menos residuos es lo mejor."),
        ("En Matricería: ¿qué documento informa peligros de un producto?", "La hoja de datos de seguridad", "En este caso, describe peligros y manejo seguro."),
        ("En Matricería: ¿quién retira residuos peligrosos?", "Una empresa autorizada", "Es una exigencia de la norma vigente."),
    ],
    op=("Ficha de ejemplo: un taller de otra ciudad entrega 50 kg de aceite usado y 30 kg de trapos con aceite a una persona sin autorización. Escribe (a) cuántos kg son en total, (b) qué problema hay, (c) qué debería hacer el taller, (d) en qué lugar de la jerarquía de manejo está «eliminar».",
        "(a) 50 + 30 = 80 kg. (b) El retiro lo hace una persona sin autorización. (c) Entregarlos solo a una empresa autorizada y registrar el retiro con fecha, cantidad y firma. (d) Es el último recurso.",
        ["suma los kg", "detecta el problema", "indica qué hacer", "ubica eliminar en la jerarquía"],
        ["hoja con las cuatro respuestas"],
        ["no ver el problema de la autorización", "no registrar", "ubicar eliminar primero"],
        "Pregunta: «¿quién puede retirar residuos peligrosos?». Si duda, pídele que relea el vocabulario."),
    reinforce="Escribe la jerarquía de manejo en orden y un ejemplo inventado de cada nivel.",
    extend="Explica con un ejemplo por qué eliminar es el último recurso.",
)

# ============================================================ OAM-06, clase 3
F = ("Ficha 3 (inventario mensual de residuos de ejemplo, inventado; el inventario lo hizo personal capacitado). Residuos del mes, en kg: recortes de acero limpios, 500; plástico limpio, 250; cartón y papel, 100; aceite usado, 80; trapos con aceite y solvente, 50; envases vacíos de solvente, 20. "
     "Observaciones de la revisión: 6 kg de trapos con solvente aparecieron en el contenedor de cartón; 2 recipientes de aceite no tienen etiqueta; 5 kg de plástico limpio se botaron a la basura común; el registro de retiro del mes anterior no tiene firma. Precio de ejemplo de la chatarra de acero: $200 por kg; costo de ejemplo de retiro de residuos peligrosos: $1.000 por kg.")
build(
    O6, 3, F,
    use="Aprenderé a analizar un inventario de residuos y una revisión, a detectar errores de segregación, etiquetado y registro y a calcular cantidades y valores, solo en papel.",
    prior=["Sé qué es un residuo peligroso.", "Sé qué es una etiqueta y un registro de retiro.", "Sé sumar y calcular porcentajes de números redondos."],
    explain=[
        "Un inventario de residuos anota, por tipo, cuántos kg hay. Con él se calcula el total, el porcentaje de cada tipo y cuánto se puede reciclar. Una revisión del manejo compara el inventario con lo que se observa: residuos mal segregados, recipientes sin etiqueta, residuos reciclables botados y registros incompletos. Cada hallazgo se informa a la jefatura con el dato y se asigna una acción correctiva.",
        "Los residuos peligrosos cuestan por kg retirarlos, mientras que la chatarra limpia se puede vender. Por eso mezclar un residuo peligroso con uno limpio contamina el limpio y aumenta el costo. Separar bien ahorra dinero y protege el ambiente. Los registros incompletos son una no conformidad.",
        f"El análisis es de papel. {EMER} {AVISO}",
    ],
    vocab=[("inventario de residuos", "lista de los residuos por tipo con su cantidad en kg"), ("mala segregación", "residuos mezclados que debían separarse"), ("hallazgo", "problema detectado en una revisión"), ("acción correctiva", "medida que corrige un hallazgo y evita que se repita"), ("contaminar", "mezclar un residuo limpio con uno peligroso")],
    worked=[
        ("Porcentaje de un tipo", "En un inventario de ejemplo de 200 kg, 50 kg son cartón. ¿Qué porcentaje es?", ["Se multiplican 50 por 100: 5.000.", "5.000 dividido en 200 son 25."], "25 %"),
        ("Detectar una mala segregación", "En una revisión de ejemplo aparece un envase de solvente en el contenedor de plástico limpio. ¿Qué hallazgo es?", ["Un residuo peligroso está mezclado con uno limpio.", "Es una mala segregación."], "Mala segregación"),
    ],
    mistakes=[("Mezclar un residuo peligroso con uno limpio «porque es poco».", "Se contamina el limpio y aumenta el costo.", "Separa por tipo siempre."),
              ("Firmar el registro de retiro sin comprobarlo.", "Un registro falso es una no conformidad.", "Comprueba cantidad, tipo y empresa antes de firmar.")],
    T=[
        ("abc", "En Matricería: ¿qué es una mala segregación?", "Residuos mezclados que debían separarse", "Un residuo bien rotulado", "Un recipiente vacío", "La segregación correcta separa por tipo."),
        ("abc", "En Matricería: ¿qué es un hallazgo de una revisión?", "Un problema detectado", "Un residuo reciclado", "Una firma", "Un hallazgo se informa y se corrige."),
        ("abc", "En Matricería: ¿qué significa contaminar un residuo limpio?", "Mezclarlo con uno peligroso", "Pesarlo", "Venderlo", "Se vuelve más caro de manejar."),
        ("=", "{F} ¿Cuántos kg suman todos los residuos del mes?", "500+250+100+80+50+20", "Se suman los kg de los seis tipos.", " kg"),
        ("=", "{F} ¿Cuántos kg suman los residuos peligrosos: aceite, trapos y envases?", "80+50+20", "Se suman los tres residuos peligrosos.", " kg"),
        ("=", "{F} ¿Qué porcentaje del total de 1.000 kg son los recortes de acero limpios?", "500*100//1000", "Se multiplican por 100 y se dividen por el total.", " %"),
        ("=", "{F} ¿Cuánto vale la chatarra de acero limpia, a $200 por kg?", "500*200", "Se multiplican los kg por el precio por kg.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuesta retirar los residuos peligrosos, a $1.000 por kg?", "150*1000", "Se multiplican los kg peligrosos por el costo por kg.", " pesos de ejemplo"),
        ("abc", "{F} ¿Qué hallazgo hay en el contenedor de cartón?", "Hay 6 kg de trapos con solvente, una mala segregación", "Hay demasiado cartón", "Todo está correcto", "Un residuo peligroso mezclado con cartón."),
        ("abc", "{F} ¿Qué hallazgo hay en los recipientes de aceite?", "2 recipientes no tienen etiqueta", "Están bien rotulados", "Falta aceite", "Sin etiqueta no se sabe qué contienen."),
        ("abc", "{F} ¿Qué hallazgo hay en el registro de retiro del mes anterior?", "No tiene firma, por lo que es incompleto", "Está firmado", "Tiene demasiadas firmas", "El registro sin firma es una no conformidad."),
        ("abc", "{F} Un jefe dice: «los 5 kg de plástico botados son pocos, no importan». ¿Qué respuesta es correcta?", "Es un hallazgo: era plástico reciclable y debía ir al reciclaje", "Es correcto, porque son pocos", "Es correcto, si nadie lo vio", "La cantidad no cambia que era reciclable."),
        ("=", "{F} Si los trapos con solvente contaminaron 14 kg de cartón y esos 14 kg deben retirarse como peligrosos, ¿cuánto cuesta retirarlos, a $1.000 por kg?", "14*1000", "Se multiplican los kg de cartón contaminado por el costo de retiro de peligrosos.", " pesos de ejemplo"),
    ],
    ctx=("abc", "El supervisor de ejemplo dice: «arreglemos el registro y firmemos, para que no haya hallazgos». ¿Qué propones?", "Registrar los hallazgos tal como son y definir acciones correctivas", "Cambiar el registro", "Firmar sin revisar", "El registro debe reflejar la realidad."),
    sc=[
        ("En Matricería: ¿cuánto es 50 kg de 200 kg en porcentaje?", "25 %", "Se multiplica por 100 y se divide por el total."),
        ("En Matricería: ¿qué pasa si se mezcla un residuo peligroso con uno limpio?", "El limpio se contamina y cuesta más manejarlo", "En este caso, La mezcla encarece el manejo."),
        ("En Matricería: ¿qué es un registro de retiro sin firma?", "Una no conformidad", "En este caso, El registro está incompleto."),
    ],
    op=("Ficha de ejemplo: inventario en kg: recortes limpios, 200; plástico limpio, 50; aceite usado, 30; trapos con aceite, 20. Revisión: 4 kg de trapos aparecieron entre el plástico; un recipiente de aceite sin etiqueta. Precio de la chatarra: $150 por kg; retiro de peligrosos: $800 por kg. Escribe (a) el total de kg, (b) los kg peligrosos y su costo de retiro, (c) el valor de la chatarra, (d) los hallazgos.",
        "(a) 200 + 50 + 30 + 20 = 300 kg. (b) 30 + 20 = 50 kg; 50 × 800 = 40.000 pesos de ejemplo. (c) 200 × 150 = 30.000 pesos de ejemplo. (d) Mala segregación de los trapos y un recipiente sin etiqueta.",
        ["suma los kg", "calcula los peligrosos y su costo", "calcula el valor de la chatarra", "nombra los hallazgos"],
        ["hoja con las cuatro respuestas"],
        ["no separar peligrosos", "calcular mal los costos", "no nombrar los hallazgos"],
        "Pregunta: «¿cuáles residuos son peligrosos?». Si duda, pídele que relea el inventario."),
    reinforce="Inventa un inventario de cuatro residuos y calcula el porcentaje de cada uno.",
    extend="Explica con un ejemplo por qué una mala segregación aumenta los costos de un taller.",
)

# ============================================================ OAM-06, clase 4
F = ("Ficha 4 (cálculo de mejora de manejo de residuos, de ejemplo e inventado). Situación actual del taller en un mes: recortes de acero, 600 kg, de los cuales se vende solo el 50 % porque el resto se contamina con aceite; plástico, 200 kg, de los cuales se recicla el 40 %; residuos peligrosos, 150 kg. "
     "Precio de la chatarra: $200 por kg; retiro de residuos peligrosos: $1.000 por kg; retiro de residuos comunes: $100 por kg. Plan de mejora de ejemplo: separar bien, con lo que se vende el 90 % del acero, se recicla el 80 % del plástico y los peligrosos bajan a 100 kg; una bandeja de contención cuesta $60.000 y 5 etiquetas rotuladoras, $5.000 en total.")
build(
    O6, 4, F,
    use="Aprenderé a calcular el efecto económico y ambiental de mejorar la segregación de residuos, con porcentajes y costos de ejemplo, y a decidir si una mejora se justifica.",
    prior=["Sé calcular porcentajes de números redondos.", "Sé multiplicar y restar enteros.", "Sé comparar costos."],
    explain=[
        "Para evaluar una mejora se comparan la situación actual y la propuesta. Se calcula cuántos kg se venden o reciclan en cada una con los porcentajes, el ingreso por la chatarra vendida y el costo de retirar los residuos peligrosos. La diferencia entre ambas situaciones es el beneficio mensual de la mejora. Si el beneficio supera la inversión, la mejora se justifica.",
        "La inversión es lo que cuesta implementar la mejora, como una bandeja de contención o etiquetas. El tiempo en que el beneficio cubre la inversión se calcula dividiendo la inversión entre el beneficio mensual. Reducir residuos peligrosos y reciclar más protege el ambiente además de ahorrar. Los valores son de ejemplo.",
        f"El cálculo es de papel. {EMER} {AVISO}",
    ],
    vocab=[("beneficio mensual", "diferencia entre lo que se gana o se ahorra con la mejora y la situación actual"), ("inversión", "lo que cuesta implementar la mejora"), ("tasa de venta", "porcentaje de un residuo que se vende"), ("tasa de reciclaje", "porcentaje de un residuo que se recicla"), ("costo de retiro", "costo por kg de retirar un residuo")],
    worked=[
        ("Porcentaje vendido", "Se generan 200 kg de chatarra de ejemplo y se vende el 50 %. ¿Cuántos kg se venden?", ["Se multiplican 200 por 50: 10.000.", "10.000 dividido en 100 son 100."], "100 kg"),
        ("Plazo de recuperación", "Una mejora de ejemplo cuesta $90.000 y da un beneficio de $30.000 al mes. ¿En cuántos meses recupera la inversión?", ["Se divide la inversión entre el beneficio.", "90.000 dividido en 30.000 son 3."], "3 meses"),
    ],
    mistakes=[("Calcular el beneficio sin comparar con la situación actual.", "El beneficio es la diferencia entre ambas.", "Calcula las dos situaciones y réstalas."),
              ("Olvidar el costo de retiro de los peligrosos en la comparación.", "También baja con la mejora.", "Incluye el costo de retiro en ambas situaciones.")],
    T=[
        ("abc", "En Matricería: ¿qué es la inversión de una mejora?", "Lo que cuesta implementarla", "Lo que se ahorra cada mes", "El precio de la chatarra", "La inversión es el gasto inicial."),
        ("abc", "En Matricería: ¿cómo se calcula el plazo de recuperación de una mejora?", "Dividiendo la inversión entre el beneficio mensual", "Multiplicando la inversión por el beneficio", "Sumando inversión y beneficio", "Indica en cuántos meses se recupera lo invertido."),
        ("abc", "En Matricería: ¿qué es el beneficio mensual de una mejora?", "La diferencia respecto de la situación actual", "El costo de la mejora", "El total de residuos", "Es lo que mejora cada mes."),
        ("=", "{F} ¿Cuántos kg de acero se venden en la situación actual, con el 50 % de 600 kg?", "600*50//100", "Se multiplica por el porcentaje y se divide por 100.", " kg"),
        ("=", "{F} ¿Cuántos kg de acero se venden con la mejora, con el 90 % de 600 kg?", "600*90//100", "Se multiplica por el porcentaje y se divide por 100.", " kg"),
        ("=", "{F} ¿Cuántos kg más de acero se venden con la mejora?", "540-300", "Se resta lo vendido actualmente a lo vendido con la mejora.", " kg"),
        ("=", "{F} ¿Cuánto más ingresa por la chatarra con la mejora, a $200 por kg?", "240*200", "Se multiplican los kg adicionales por el precio.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántos kg más se reciclan de plástico con la mejora, del 40 % al 80 % de 200 kg?", "200*80//100-200*40//100", "Se calcula el reciclaje con cada porcentaje y se resta.", " kg"),
        ("=", "{F} ¿Cuánto se ahorra en retiro de peligrosos, al bajar de 150 a 100 kg, a $1.000 por kg?", "(150-100)*1000", "Se resta los kg que bajan y se multiplica por el costo.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuál es el beneficio mensual total, sumando el mayor ingreso de $48.000 y el ahorro de retiro de $50.000?", "48000+50000", "Se suman el mayor ingreso y el ahorro.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuesta la inversión total, con la bandeja y las etiquetas?", "60000+5000", "Se suman los dos costos.", " pesos de ejemplo"),
        ("abc", "{F} Con un beneficio de $98.000 al mes y una inversión de $65.000, ¿qué conclusión corresponde?", "La mejora se justifica: la inversión se recupera en menos de un mes", "No se justifica, porque cuesta dinero", "No se puede decidir", "El beneficio mensual supera la inversión."),
        ("abc", "{F} Un jefe dice: «no invirtamos, gastar en residuos no sirve». ¿Qué respuesta es correcta?", "Los datos muestran que se recupera la inversión rápido y además se protege el ambiente", "Tiene razón, no sirve", "Solo sirve si lo exige la norma", "La mejora tiene beneficio económico y ambiental."),
    ],
    ctx=("abc", "El gerente de ejemplo duda de invertir $65.000 para ahorrar. ¿Qué dos números le muestras?", "El beneficio mensual y el plazo de recuperación de la inversión", "El color de los recipientes", "El número de trabajadores", "Con esos números se decide la inversión."),
    sc=[
        ("En Matricería: ¿cuánto es el 90 % de 600 kg?", "540 kg", "Se multiplica por 90 y se divide por 100."),
        ("En Matricería: ¿cómo se calcula el plazo de recuperación?", "Inversión dividida por beneficio mensual", "Muestra en cuántos meses se recupera."),
        ("En Matricería: ¿qué reduce una buena segregación?", "El costo de retiro de residuos peligrosos", "Menos residuos peligrosos cuesta menos retirar."),
    ],
    op=("Ficha de ejemplo: un taller genera 400 kg de chatarra y vende el 50 %; con una mejora vende el 80 %. Precio: $150 por kg. Los peligrosos bajan de 100 a 80 kg, con costo de retiro de $1.000 por kg. La inversión es de $60.000. Escribe (a) los kg adicionales vendidos, (b) el mayor ingreso, (c) el ahorro de retiro, (d) el plazo de recuperación con el beneficio total.",
        "(a) 80 % de 400 son 320; 50 % son 200; 120 kg más. (b) 120 × 150 = 18.000 pesos de ejemplo. (c) 20 × 1.000 = 20.000 pesos de ejemplo. (d) El beneficio es 38.000 al mes y 60.000 ÷ 38.000 es menos de 2, es decir 2 meses redondeando hacia arriba.",
        ["calcula los kg adicionales", "calcula el ingreso", "calcula el ahorro", "calcula el plazo"],
        ["hoja con las cuatro respuestas"],
        ["no comparar con la situación actual", "olvidar el ahorro de retiro", "dividir al revés"],
        "Pregunta: «¿cuánto vendía antes y cuánto vende ahora?». Si duda, pídele que calcule ambas situaciones."),
    reinforce="Inventa un taller con porcentajes de venta antes y después de una mejora y calcula los kg adicionales vendidos.",
    extend="Explica con un ejemplo por qué una mejora ambiental puede pagarse sola.",
)
