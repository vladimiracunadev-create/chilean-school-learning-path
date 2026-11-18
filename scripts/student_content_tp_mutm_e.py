"""Muebles y Terminaciones en Madera (3.º y 4.º medio TP): OAE-09 (mantención de maquinaria y afilado de herramientas de corte como planificación, registros y reglas de seguridad, sin procedimientos) y OAE-10 (embalar y rotular muebles: documentos, trazabilidad, listas de empaque y cálculos de insumos, en papel). Datos de ejemplo."""
from __future__ import annotations

from tp_mutm_common import AVISO, EMER, build

O9 = "TP-MUTM-3y4-OAE-09"
O10 = "TP-MUTM-3y4-OAE-10"
TAIL = f"{EMER} {AVISO}"

# ============================================================ OAE-09, clase 1
F = ("Ficha 1 (taller de ejemplo, inventado). El taller ficticio «Carpintería Los Boldos» tiene 6 máquinas y 2 técnicos de mantención autorizados. Una máquina tiene una etiqueta de «no operar». "
     "Riesgos anotados: arranque inesperado de una máquina durante una intervención, partes móviles, chispas y partículas al afilar herramientas de corte, herramientas de corte con filo, ruido y polvo. "
     "Medidas anotadas: manual del fabricante disponible, bloqueo de energía y etiqueta de «no operar» colocados por personal autorizado antes de cualquier intervención, lentes y protección auditiva, afilado solo por personal capacitado y orden en la zona de trabajo.")
build(
    O9, 1, F,
    use="Aprenderé qué es la mantención de máquinas y el afilado de herramientas de corte y qué riesgos tienen, sin ningún procedimiento de intervención.",
    prior=["Sé qué es la jerarquía de controles.", "Sé qué es un EPP.", "Sé restar y multiplicar."],
    explain=[
        "La mantención básica de maquinaria y equipos es el conjunto de tareas que los mantiene en buen estado de funcionamiento y seguro; el afilado devuelve el filo a las herramientas de corte. Ambas tareas se hacen de acuerdo con las indicaciones del fabricante, que están en su manual. Cómo se hacen lo enseña un instructor autorizado y no se explica en este cuaderno, porque una máquina intervenida de forma incorrecta puede causar cortes, atrapamientos o amputaciones.",
        "El mayor riesgo es el arranque inesperado: si alguien enciende una máquina mientras otra persona la interviene, puede haber un accidente grave. Por eso existe el bloqueo de energía con etiqueta de «no operar»: una medida que solo coloca y retira personal autorizado. Otros riesgos son las partes móviles, las chispas y partículas al afilar, el ruido y el polvo. Según la jerarquía de controles, el EPP es el último nivel y no reemplaza ni la autorización ni el bloqueo.",
        TAIL,
    ],
    vocab=[("mantención", "tareas que mantienen una máquina en buen estado y segura"), ("afilado", "tarea que devuelve el filo a una herramienta de corte"), ("manual del fabricante", "documento con las indicaciones del fabricante para el equipo"), ("bloqueo de energía", "medida que impide el arranque de una máquina durante una intervención"), ("etiqueta de no operar", "aviso que prohíbe usar una máquina"), ("arranque inesperado", "puesta en marcha de una máquina mientras alguien la interviene")],
    worked=[
        ("Reconocer el documento", "Una persona de ejemplo quiere saber qué indica el fabricante para mantener una máquina. ¿Qué documento consulta?", ["Las indicaciones del fabricante están en su manual.", "El manual describe lo que corresponde al equipo."], "El manual del fabricante"),
        ("Contar máquinas", "Un taller de ejemplo tiene 9 máquinas y 2 están fuera de servicio. ¿Cuántas están disponibles?", ["Se restan las que están fuera de servicio.", "9 menos 2 son 7."], "7 máquinas"),
    ],
    mistakes=[("Creer que basta apagar la máquina con el interruptor para intervenirla.", "Otra persona podría encenderla sin saber que está siendo intervenida.", "Se usa el bloqueo de energía con etiqueta, colocado por personal autorizado."),
              ("Afilar una herramienta de corte sin capacitación porque «parece fácil».", "Un error causa cortes y proyección de partículas.", "Solo el personal capacitado afila, según las indicaciones del fabricante.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es la mantención de una máquina?", "El conjunto de tareas que la mantienen en buen estado y segura", "La compra de una máquina nueva", "El diseño de un mueble que la use", "La mantención conserva el funcionamiento seguro de la máquina."),
        ("abc", "¿Qué es el arranque inesperado de una máquina?", "Que se ponga en marcha mientras alguien la interviene", "Que se apague sola al terminar el turno", "Que cambie de color por el uso", "El arranque inesperado es un accidente grave durante una intervención."),
        ("=", "{F} ¿Cuántas máquinas no tienen etiqueta de «no operar»?", "6-1", "Se restan las máquinas con etiqueta del total.", " máquinas"),
        ("abc", "{F} ¿Quién coloca y retira el bloqueo de energía según la ficha?", "El personal autorizado", "Cualquier persona que pase", "El proveedor desde su oficina", "La ficha indica que el bloqueo lo coloca personal autorizado."),
        ("abc", "{F} ¿Dónde se consultan las indicaciones de mantención de un equipo?", "En el manual del fabricante", "En el plano del mueble", "En la lista de corte", "Las indicaciones del equipo las da su fabricante."),
        ("abc", "{F} ¿Qué riesgo de la ficha se produce al afilar herramientas de corte?", "Chispas y partículas", "Intoxicación por solventes", "Caída desde altura", "La ficha anota chispas y partículas al afilar."),
        ("=", "{F} Cada técnico de mantención recibe lentes y protección auditiva. ¿Cuántas piezas de EPP se entregan a los 2 técnicos?", "2*2", "Se multiplican los técnicos por las dos piezas de cada uno.", " piezas"),
        ("abc", "{F} Una persona ve una máquina con etiqueta de «no operar» y la enciende «para probar». ¿Qué corresponde?", "No: la etiqueta prohíbe usarla y se avisa al responsable", "Sí: probarla es parte de su trabajo", "Sí, si usa lentes", "La etiqueta prohíbe su uso hasta que personal autorizado la retire."),
        ("abc", "{F} Una máquina vibra de forma extraña. ¿Qué corresponde hacer al operador?", "Dejar de usarla y avisar al responsable", "Seguir usándola hasta terminar", "Intentar repararla con una herramienta", "Una falla se informa y la máquina no se usa."),
        ("ab", "{F} Un estudiante dice: «con apagar el interruptor basta para intervenir una máquina». ¿Qué respuesta es correcta?", "No: se usa el bloqueo de energía con etiqueta por personal autorizado", "Sí: el interruptor es suficiente", "La ficha incluye bloqueo y etiqueta como medida aparte."),
        ("abc", "{F} Una estudiante dice: «sé qué es afilar, puedo afilar una herramienta». ¿Qué respuesta es correcta?", "No: afilar exige instructor autorizado y norma vigente", "Sí: conocer el término la habilita", "Sí, con lentes y guantes", "Saber un término no habilita ni el EPP reemplaza la capacitación."),
        ("=", "{F} Si cada máquina tiene 3 partes móviles señalizadas (dato de ejemplo), ¿cuántas partes móviles hay en las 6 máquinas?", "6*3", "Se multiplican las máquinas por las partes móviles de cada una.", " partes"),
        ("abc", "{F} ¿Qué datos mínimos lleva el registro de una máquina con etiqueta de no operar?", "Cuál es, desde cuándo, quién la bloqueó y por qué", "Solo su color", "Solo el nombre del fabricante", "Un registro útil dice cuál, desde cuándo, quién y por qué."),
    ],
    ctx=("abc", "En un taller de ejemplo, una máquina arranca mientras un técnico la interviene y le atrapa la mano. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar liberar la mano sin avisar", "Seguir trabajando con las demás máquinas", "Ante un atrapamiento se pide ayuda a quien está autorizado y a emergencias."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿qué es el arranque inesperado?", "Que una máquina se ponga en marcha durante una intervención", "Es el riesgo principal al intervenir equipos."),
        ("¿Quién coloca el bloqueo de energía?", "El personal autorizado", "El bloqueo lo coloca y lo retira quien está habilitado."),
        ("¿Dónde están las indicaciones de mantención de un equipo?", "En el manual del fabricante", "Las indicaciones las da el fabricante del equipo."),
    ],
    op=("Taller de ejemplo «Taller Quillay» (ficticio): 8 máquinas y 3 técnicos autorizados; 2 máquinas tienen etiqueta de «no operar». Cada técnico recibe lentes y protección auditiva. Riesgos: arranque inesperado y partículas al afilar. Escribe (a) cuántas máquinas no tienen etiqueta, (b) cuántas piezas de EPP se entregan, (c) qué medida evita el arranque inesperado y (d) qué haces si una máquina atrapa la mano de alguien.",
        "(a) 8 menos 2 son 6. (b) 3×2 son 6 piezas. (c) El bloqueo de energía con etiqueta, colocado por personal autorizado. (d) No me acerco a la zona de riesgo, aviso a un adulto responsable y a emergencias.",
        ["calcula las máquinas sin etiqueta", "calcula el EPP entregado", "nombra el bloqueo de energía", "avisa sin acercarse al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["decir que apagar el interruptor basta", "proponer liberar la mano sin ayuda", "confundir el manual con el plano"],
        "Pregunta: «¿por qué no basta con apagar el interruptor?». Si no responde, pídele que relea la explicación."),
    reinforce="Escribe con tus palabras qué es el arranque inesperado y por qué es un riesgo.",
    extend="Explica por qué el afilado de herramientas de corte lo hace personal capacitado y no cualquier trabajador.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 2 (hoja de vida de una máquina de ejemplo, inventada). Máquina ficticia «M-3». Horas de uso acumuladas: 460. Intervalo de mantención preventiva de ejemplo: cada 120 horas de uso; la última se hizo a las 360 horas. "
     "Registro de mantenciones: a las 120 horas (preventiva), a las 240 horas (preventiva), a las 300 horas (correctiva por una falla) y a las 360 horas (preventiva). "
     "Roles: operador, que reporta fallas; técnico de mantención autorizado, que interviene; jefe de producción, que programa; prevencionista, que revisa los riesgos. Repuestos en bodega de ejemplo: 4 correas y 2 filtros.")
build(
    O9, 2, F,
    use="Aprenderé qué documentos se usan en la mantención: manual, plan de mantención, hoja de vida y orden de trabajo, y la diferencia entre mantención preventiva y correctiva.",
    prior=["Sé qué es la mantención.", "Sé sumar y restar.", "Sé qué es un registro."],
    explain=[
        "La mantención preventiva es la que se programa antes de que ocurra una falla, por ejemplo cada cierto número de horas de uso. La mantención correctiva es la que se hace después de que ocurrió una falla. El plan de mantención ordena cuándo se hace cada una; la hoja de vida de la máquina registra cada intervención con su fecha, sus horas de uso, el tipo de mantención y quién la hizo. La orden de trabajo de mantención es el documento que autoriza una intervención y que firma quien la ejecuta.",
        "Los roles se reparten así: el operador reporta las fallas pero no las repara; el técnico de mantención autorizado interviene; el jefe de producción programa los tiempos y el prevencionista revisa los riesgos. Los repuestos tienen un inventario: si falta un repuesto crítico, se pide con anticipación. Todos los valores de esta clase son de ejemplo; los intervalos reales los indica el manual del fabricante.",
        TAIL,
    ],
    vocab=[("mantención preventiva", "mantención programada antes de que ocurra una falla"), ("mantención correctiva", "mantención que se hace después de una falla"), ("hoja de vida", "registro de todas las intervenciones de una máquina"), ("orden de trabajo de mantención", "documento que autoriza y registra una intervención"), ("repuesto", "pieza de recambio de una máquina"), ("horas de uso", "tiempo que una máquina lleva funcionando")],
    worked=[
        ("Tipo de mantención", "Una máquina de ejemplo se revisa cada 100 horas aunque funcione bien. ¿Qué tipo de mantención es?", ["Se programa antes de cualquier falla.", "Es una mantención preventiva."], "Preventiva"),
        ("Próxima mantención", "Una máquina de ejemplo se mantiene cada 80 horas y la última fue a las 160. ¿A qué hora de uso toca la próxima?", ["Se suma el intervalo a la última mantención.", "160 más 80 son 240."], "A las 240 horas"),
    ],
    mistakes=[("Confundir mantención correctiva con preventiva.", "La correctiva sigue a una falla y la preventiva se anticipa.", "Se pregunta si la falla ya ocurrió."),
              ("Dejar que el operador repare una falla porque «sabe cómo».", "Reparar exige personal autorizado y bloqueo de energía.", "El operador reporta y el técnico autorizado interviene.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es la mantención correctiva?", "La que se hace después de que ocurrió una falla", "La que se programa antes de cualquier falla", "La compra de una máquina nueva", "La correctiva sigue a la falla; la preventiva se anticipa."),
        ("abc", "¿Qué registra la hoja de vida de una máquina?", "Cada intervención con fecha, horas de uso, tipo y quién la hizo", "El precio de los muebles que fabrica", "El nombre de los clientes", "La hoja de vida lleva la historia de la máquina."),
        ("=", "{F} ¿A qué hora de uso toca la próxima mantención preventiva (última a las 360 horas, cada 120)?", "360+120", "Se suma el intervalo a la última mantención preventiva.", " horas"),
        ("=", "{F} ¿Cuántas horas faltan para esa próxima mantención (480 menos las 460 acumuladas)?", "480-460", "Se restan las horas acumuladas de la hora de la próxima mantención.", " horas"),
        ("=", "{F} ¿Cuántas mantenciones registra la hoja de vida?", "2+1+1", "Se suman las preventivas de las 120 y 240 horas, la correctiva y la preventiva de las 360 horas.", " mantenciones"),
        ("abc", "{F} ¿Qué mantención fue la de las 300 horas?", "Correctiva, por una falla", "Preventiva, por programa", "Auditoría", "La hoja la registra como correctiva por una falla."),
        ("abc", "{F} ¿Qué rol reporta las fallas?", "El operador", "El técnico de mantención", "El prevencionista", "El operador reporta y no repara."),
        ("abc", "{F} ¿Qué rol interviene en la máquina?", "El técnico de mantención autorizado", "El operador", "El jefe de producción", "La intervención corresponde al técnico autorizado."),
        ("=", "{F} Si cada mantención preventiva usa 2 filtros de ejemplo y quedan 2 filtros en bodega, ¿cuántos filtros faltarían para las próximas 3 mantenciones preventivas?", "3*2-2", "Se multiplican las mantenciones por los filtros de cada una y se restan los que hay.", " filtros"),
        ("ab", "{F} Un operador dice: «yo reparo la falla, soy el que más conoce la máquina». ¿Qué respuesta es correcta?", "No: el operador reporta y el técnico autorizado interviene", "Sí: el operador repara las fallas", "La ficha separa el rol del operador y el del técnico."),
        ("abc", "{F} Una estudiante dice: «ya entiendo el plan de mantención, puedo intervenir la máquina». ¿Qué respuesta es correcta?", "No: intervenir exige instructor autorizado y norma vigente", "Sí: entender el plan habilita", "Sí, con EPP", "Entender un plan no habilita para intervenir máquinas."),
        ("abc", "{F} Quedan 2 filtros en bodega y la próxima mantención preventiva usa 2. ¿Qué conviene hacer?", "Pedir repuestos con anticipación para no quedar sin ellos", "Esperar a que se agoten", "Comprar un repuesto cualquiera sin revisar", "Un repuesto crítico se pide antes de que se acabe."),
        ("abc", "{F} La hoja de vida registra la mantención de las 300 horas como correctiva. ¿Qué información debería agregar el técnico para que sirva al análisis?", "La causa de la falla, la pieza cambiada y la fecha", "Solo el color de la máquina", "Solo el nombre del operador que la usó", "La causa y la pieza cambiada permiten decidir acciones preventivas."),
    ],
    ctx=("abc", "En el taller de ejemplo, un técnico interviene una máquina y un operador la enciende por error. ¿Qué respuesta es correcta?", "Evitarlo con el bloqueo de energía y la etiqueta colocados por personal autorizado", "Confiar en que nadie la encienda", "Gritar para avisar a todos", "El bloqueo con etiqueta protege durante cualquier intervención."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿Qué es la mantención preventiva?", "La que se programa antes de que ocurra una falla", "La preventiva se anticipa al problema antes de que ocurra."),
        ("En Muebles y Terminaciones en Madera: ¿para qué sirve la hoja de vida?", "Para registrar cada intervención de la máquina", "Permite conocer la historia de la máquina."),
        ("¿Quién interviene una máquina?", "El técnico de mantención autorizado", "Reparar exige autorización y bloqueo de energía."),
    ],
    op=("Hoja de vida de ejemplo «Máquina M-9» (ficticia): horas de uso acumuladas, 290; intervalo de mantención preventiva de ejemplo, cada 100 horas; la última preventiva fue a las 200 horas; hubo una correctiva a las 250. Repuestos en bodega: 3 correas. Escribe (a) a qué hora de uso toca la próxima preventiva, (b) cuántas horas faltan, (c) qué rol reporta una falla y (d) qué rol la repara.",
        "(a) 200+100 son 300 horas. (b) 300 menos 290 son 10 horas. (c) El operador. (d) El técnico de mantención autorizado.",
        ["calcula la próxima mantención", "calcula las horas que faltan", "nombra al operador", "nombra al técnico autorizado"],
        ["hoja con las cuatro respuestas"],
        ["confundir la correctiva con la preventiva", "restar al revés", "decir que el operador repara"],
        "Pregunta: «¿qué hora de uso se toma como última mantención?». Si no responde, pídele que relea la ficha."),
    reinforce="Escribe una mantención preventiva y una correctiva de ejemplo para una máquina de taller.",
    extend="Explica por qué conviene pedir un repuesto antes de quedarse sin él.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 3 (registro de detenciones de ejemplo, inventado). Semana de 40 horas programadas por máquina. Horas detenidas por mantención o falla: máquina M-1, 4 horas; M-2, 8 horas; M-3, 2 horas; M-4, 10 horas. "
     "La disponibilidad es el porcentaje de las horas programadas en que la máquina estuvo operativa. Meta de ejemplo: disponibilidad de al menos 85 %. Causas anotadas: M-2, correa cortada (falla); M-4, falta de un repuesto crítico en bodega.")
build(
    O9, 3, F,
    use="Aprenderé a analizar un registro de detenciones: calcular la disponibilidad de cada máquina, compararla con una meta y relacionarla con sus causas.",
    prior=["Sé qué es la mantención preventiva y correctiva.", "Sé calcular porcentajes sencillos.", "Sé restar."],
    explain=[
        "La disponibilidad mide cuánto del tiempo programado una máquina estuvo lista para trabajar. Se calcula restando las horas detenidas de las horas programadas, multiplicando el resultado por 100 y dividiendo por las horas programadas. Si la disponibilidad es igual o mayor que la meta, la máquina cumple; si es menor, se analizan las causas de las detenciones y se decide una acción.",
        "Las causas se anotan en el registro para ver patrones: una falla por una pieza gastada puede evitarse con mantención preventiva; una detención por falta de repuesto se evita con un inventario mejor planificado. Analizar el registro no habilita para intervenir las máquinas: la intervención la hace personal autorizado, con bloqueo de energía y según el manual del fabricante. En esta clase las horas y las metas son de ejemplo.",
        TAIL,
    ],
    vocab=[("disponibilidad", "porcentaje de las horas programadas en que la máquina estuvo operativa"), ("horas programadas", "horas en que se planificó usar la máquina"), ("horas detenidas", "horas en que la máquina no pudo trabajar"), ("causa", "origen de una detención"), ("meta", "valor mínimo que se desea alcanzar")],
    worked=[
        ("Calcular la disponibilidad", "Una máquina de ejemplo tiene 20 horas programadas y 4 detenidas. ¿Qué disponibilidad tiene?", ["Operativa: 20 menos 4 son 16 horas.", "16 por 100 dividido en 20 son 80."], "80 %"),
        ("Aplicar una meta", "Con una meta de ejemplo de 90 %, una máquina tiene 80 %. ¿Cumple?", ["Se compara 80 con 90.", "80 es menor que 90."], "No cumple"),
    ],
    mistakes=[("Calcular la disponibilidad dividiendo solo las horas detenidas.", "Se obtiene el porcentaje de detención y no el de disponibilidad.", "Primero se restan las horas detenidas de las programadas."),
              ("Intervenir la máquina «para mejorar el indicador».", "Intervenir exige personal autorizado y bloqueo de energía.", "Se informa al jefe de producción y decide el técnico autorizado.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué mide la disponibilidad de una máquina?", "El porcentaje de las horas programadas en que estuvo operativa", "El precio de sus repuestos", "El ruido que produce", "La disponibilidad compara tiempo operativo y tiempo programado."),
        ("abc", "¿Qué se hace si la disponibilidad es menor que la meta?", "Se analizan las causas de las detenciones y se decide una acción", "Se ignora el resultado", "Se cambia la meta para que cumpla", "La meta se mantiene y se analizan las causas."),
        ("=", "{F} ¿Cuántas horas estuvo operativa M-1?", "40-4", "Se restan las horas detenidas de las horas programadas.", " horas"),
        ("=", "{F} ¿Qué disponibilidad tiene M-1 (36 horas operativas de 40)?", "36*100//40", "Se multiplican las horas operativas por 100 y se divide por las programadas.", " %"),
        ("=", "{F} ¿Qué disponibilidad tiene M-2 (32 horas operativas de 40)?", "32*100//40", "Se multiplican las horas operativas por 100 y se divide por las programadas.", " %"),
        ("=", "{F} ¿Qué disponibilidad tiene M-3 (38 horas operativas de 40)?", "38*100//40", "Se multiplican las horas operativas por 100 y se divide por las programadas.", " %"),
        ("=", "{F} ¿Qué disponibilidad tiene M-4 (30 horas operativas de 40)?", "30*100//40", "Se multiplican las horas operativas por 100 y se divide por las programadas.", " %"),
        ("abc", "{F} ¿Qué máquinas cumplen la meta de 85 % como mínimo?", "M-1 y M-3", "M-2 y M-4", "Solo M-4", "M-1 tiene 90 % y M-3 tiene 95 %, ambas sobre 85 %."),
        ("=", "{F} ¿Cuántas horas se detuvieron en total las cuatro máquinas?", "4+8+2+10", "Se suman las horas detenidas de cada máquina.", " horas"),
        ("abc", "{F} ¿Qué acción conviene para la detención de M-4, causada por falta de un repuesto?", "Planificar el inventario de repuestos críticos", "Cambiar la meta de disponibilidad", "Retirar la máquina del registro", "La causa es el inventario, por lo que esa acción la ataca."),
        ("ab", "{F} Un jefe dice: «M-2 tuvo una falla, así que ignoramos su registro». ¿Qué respuesta es correcta?", "No: la falla se registra y se analiza su causa", "Sí: las fallas no cuentan", "La ficha anota la correa cortada como causa."),
        ("abc", "{F} Una estudiante dice: «sé calcular la disponibilidad, puedo reparar M-2». ¿Qué respuesta es correcta?", "No: reparar exige instructor autorizado, bloqueo de energía y norma vigente", "Sí: calcular habilita para reparar", "Sí, con EPP", "Un cálculo en papel no habilita para intervenir una máquina."),
        ("abc", "{F} Una máquina tiene 100 % de disponibilidad en una semana. ¿Qué se concluye con seguridad?", "Que no tuvo horas detenidas esa semana", "Que nunca va a fallar", "Que no necesita mantención preventiva", "La disponibilidad refleja la semana y no asegura el futuro."),
    ],
    ctx=("abc", "En el taller de ejemplo, un jefe presiona para mejorar la disponibilidad y propone que un operador sin autorización arregle la máquina detenida. ¿Qué respuesta es correcta?", "No: solo el técnico autorizado interviene, con bloqueo de energía", "Sí: es más rápido y mejora el indicador", "Sí, si usa lentes", "La meta no justifica intervenir sin autorización ni bloqueo."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿Cómo se calcula la disponibilidad?", "Horas operativas por 100 dividido en horas programadas", "Compara el tiempo operativo con el programado."),
        ("En Muebles y Terminaciones en Madera: ¿para qué se anotan las causas de las detenciones?", "Para ver patrones y decidir acciones", "Las causas orientan qué acción tomar."),
        ("¿Quién interviene una máquina detenida por falla?", "El técnico de mantención autorizado", "La intervención exige autorización y bloqueo de energía."),
    ],
    op=("Registro de ejemplo «Taller Peumo» (ficticio): semana de 50 horas programadas. Detenciones: máquina A, 5 horas por falla de una correa; máquina B, 10 horas por falta de un repuesto; máquina C, 0 horas. Meta de ejemplo: disponibilidad mínima de 85 %. Escribe (a) la disponibilidad de cada máquina, (b) cuáles cumplen la meta, (c) una acción para la causa de B y (d) qué rol interviene la máquina A.",
        "(a) A: 45×100÷50 es 90 %; B: 40×100÷50 es 80 %; C: 100 %. (b) A y C. (c) Planificar el inventario de repuestos críticos. (d) El técnico de mantención autorizado.",
        ["calcula las tres disponibilidades", "identifica las que cumplen", "propone una acción para el repuesto", "nombra al técnico autorizado"],
        ["hoja con las cuatro respuestas"],
        ["calcular solo con las horas detenidas", "proponer intervenir sin autorización", "olvidar la máquina C"],
        "Pregunta: «¿qué horas se restan de cuáles?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula la disponibilidad de una máquina con 25 horas programadas y 5 horas detenidas.",
    extend="Explica por qué una buena mantención preventiva puede mejorar la disponibilidad.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 4 (comparación de costos de ejemplo, inventada). Costo de ejemplo de una hora de máquina detenida: $15.000. Opción 1, mantención preventiva programada: 2 horas de detención y repuestos por $20.000. "
     "Opción 2, mantención correctiva tras una falla: 10 horas de detención y repuestos por $60.000. Herramientas de corte del taller ficticio: 12 en uso, y se desea tener 1 de reserva por cada 4 en uso. Un afilado externo cuesta $5.000 por herramienta de ejemplo.")
build(
    O9, 4, F,
    use="Aprenderé a comparar en papel el costo de la mantención preventiva y de la correctiva y a planificar herramientas de reserva y afilados, con datos de ejemplo.",
    prior=["Sé multiplicar y sumar.", "Sé qué es mantención preventiva y correctiva.", "Sé qué es una herramienta de reserva."],
    explain=[
        "Comparar la mantención preventiva y la correctiva incluye el costo directo, que son los repuestos, y el costo de la detención, que es la cantidad de horas detenidas multiplicada por el costo de cada hora. Una falla imprevista suele detener más tiempo que una mantención programada, porque no se puede planificar, y por eso la correctiva suele salir más cara aunque los repuestos parezcan baratos. El cálculo ayuda a justificar un plan de mantención preventiva.",
        "Para las herramientas de corte, el taller planifica una reserva: un número de herramientas afiladas listas para reemplazar a las que se retiran del uso para afilarlas, de modo que la producción no se detenga. El afilado puede hacerse en el taller por personal capacitado o con un servicio externo; en ambos casos se hace según las indicaciones del fabricante y con las medidas de seguridad, que este cuaderno no detalla. Todos los costos son de ejemplo.",
        TAIL,
    ],
    vocab=[("costo de detención", "horas detenidas multiplicadas por el costo de cada hora"), ("costo directo", "costo de los repuestos de una mantención"), ("herramienta de reserva", "herramienta afilada lista para reemplazar a otra"), ("servicio externo", "empresa que presta un servicio fuera del taller"), ("plan de mantención", "programación de las mantenciones")],
    worked=[
        ("Costo de detención", "Una máquina de ejemplo se detiene 3 horas y cada hora detenida cuesta $10.000. ¿Cuánto cuesta la detención?", ["Se multiplican las horas por el costo de cada hora.", "3 por 10.000 son 30.000."], "$30.000"),
        ("Herramientas de reserva", "Un taller de ejemplo usa 20 herramientas y quiere 1 de reserva por cada 5 en uso. ¿Cuántas reservas necesita?", ["Se divide las herramientas en uso por 5.", "20 dividido en 5 son 4."], "4 herramientas de reserva"),
    ],
    mistakes=[("Comparar solo el costo de los repuestos.", "Se olvida el costo de las horas de detención.", "Se suman repuestos y costo de detención."),
              ("Afilar herramientas sin tener reservas y detener la producción.", "El afilado deja sin herramientas a la máquina.", "Se planifican herramientas de reserva.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué incluye el costo de una mantención además de los repuestos?", "El costo de las horas de máquina detenida", "El precio del mueble terminado", "El precio de las tablas", "La detención de la máquina también cuesta dinero."),
        ("abc", "¿Para qué sirve una herramienta de reserva?", "Para reemplazar a otra mientras se afila y no detener la producción", "Para ocupar espacio en la bodega", "Para usarla sin afilar", "La reserva evita detener la producción."),
        ("=", "{F} ¿Cuánto cuesta la detención de la opción 1 (2 horas)?", "2*15000", "Se multiplican las horas por el costo de cada hora.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la detención de la opción 2 (10 horas)?", "10*15000", "Se multiplican las horas por el costo de cada hora.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la opción 1 (detención de 30.000 más repuestos de 20.000)?", "30000+20000", "Se suman la detención y los repuestos.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la opción 2 (detención de 150.000 más repuestos de 60.000)?", "150000+60000", "Se suman la detención y los repuestos.", " pesos"),
        ("=", "{F} ¿Cuánto más cara es la opción 2 que la 1?", "210000-50000", "Se resta el costo de la opción 1 del de la opción 2.", " pesos"),
        ("abc", "{F} Según el cálculo, ¿qué opción conviene económicamente?", "La mantención preventiva", "La mantención correctiva", "Cuestan lo mismo", "La preventiva cuesta $50.000 y la correctiva $210.000."),
        ("=", "{F} ¿Cuántas herramientas de reserva necesita el taller (1 por cada 4 en uso, 12 en uso)?", "12//4", "Se dividen las herramientas en uso por 4.", " herramientas"),
        ("=", "{F} ¿Cuántas herramientas hay en total entre las en uso y las de reserva?", "12+3", "Se suman las herramientas en uso y las de reserva.", " herramientas"),
        ("=", "{F} ¿Cuánto cuesta afilar con el servicio externo las 12 herramientas en uso?", "12*5000", "Se multiplican las herramientas por el costo de cada afilado.", " pesos"),
        ("ab", "{F} Un jefe dice: «esperamos la falla, los repuestos son más baratos que una mantención». ¿Qué respuesta es correcta?", "No: la correctiva incluye muchas horas detenidas y sale más cara", "Sí: nunca conviene programar", "La ficha compara 10 horas de detención con 2 horas."),
        ("abc", "{F} Una estudiante dice: «ya sé calcular costos de mantención, puedo afilar herramientas». ¿Qué respuesta es correcta?", "No: afilar exige instructor autorizado y norma vigente", "Sí: calcular costos habilita para afilar", "Sí, con lentes", "Calcular costos en papel no habilita para trabajar con herramientas."),
    ],
    ctx=("abc", "En el taller de ejemplo, una herramienta de corte mal afilada salta y una persona recibe un golpe en la cara. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Quitarle el protector para ver el daño", "Seguir con el trabajo para no atrasar", "Una lesión en la cara se informa a quien corresponde y a emergencias."),
    sc=[
        ("¿Cómo se calcula el costo de detención?", "Horas detenidas por el costo de cada hora", "Es el valor del tiempo perdido."),
        ("En Muebles y Terminaciones en Madera: ¿por qué conviene una mantención preventiva?", "Porque evita detenciones largas y costosas", "Programada, la detención es más corta."),
        ("¿Para qué se planifican herramientas de reserva?", "Para no detener la producción mientras se afila", "La reserva reemplaza a la herramienta que se retira."),
    ],
    op=("Cálculo de ejemplo «Taller Ñire» (ficticio): costo de una hora detenida, $12.000. Mantención preventiva: 3 horas y repuestos por $18.000. Mantención correctiva: 8 horas y repuestos por $50.000. El taller usa 16 herramientas de corte y quiere 1 de reserva por cada 4 en uso. Escribe (a) el costo total de la preventiva, (b) el costo total de la correctiva, (c) cuál conviene y (d) cuántas herramientas de reserva necesita.",
        "(a) 3×12.000 son 36.000 y con repuestos 54.000. (b) 8×12.000 son 96.000 y con repuestos 146.000. (c) La preventiva. (d) 16÷4 son 4 herramientas de reserva.",
        ["calcula el costo de la preventiva", "calcula el costo de la correctiva", "compara", "calcula las reservas"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el costo de detención", "dividir al revés las reservas", "olvidar sumar los repuestos"],
        "Pregunta: «¿qué se suma además de los repuestos?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula el costo de 6 horas detenidas con un costo de $9.000 por hora.",
    extend="Explica qué datos adicionales tomaría un jefe de taller para decidir entre afilar en el taller o con un servicio externo.",
)

# ============================================================ OAE-10, clase 1
F = ("Ficha 5 (zona de despacho de ejemplo, inventada). En el taller ficticio «Carpintería Los Boldos» la zona de despacho tiene 3 personas y prepara 10 bultos para un camión. Regla interna de ejemplo: un bulto de más de 17 kg lo mueven dos personas. "
     "Riesgos anotados: manipulación manual de cargas, caída de bultos apilados, golpes en esquinas, cortes con flejes o cuchillos de corte de cartón, acumulación de cartón y plástico que puede incendiarse y tránsito de vehículos en el patio. "
     "Medidas anotadas: bultos apilados solo hasta una altura de ejemplo de 3 niveles, guantes, calzado de seguridad, zona de despacho señalizada, retiro programado de cartón y plástico, y personal autorizado para equipos de carga.")
build(
    O10, 1, F,
    use="Aprenderé qué es embalar y rotular un mueble para su despacho y qué riesgos tiene la zona de despacho, sin ningún procedimiento de embalaje.",
    prior=["Sé qué es la jerarquía de controles.", "Sé qué es un EPP.", "Sé sumar y restar."],
    explain=[
        "Embalar es proteger un mueble, puerta, ventana, moldura o tabique para que llegue al cliente sin daños, y rotular es ponerle una etiqueta con la información que permite identificarlo y seguirlo hasta el destino. El embalaje cuida la integridad y la calidad del producto; el rótulo permite la trazabilidad, es decir, saber qué es, de qué lote es y adónde va. Un bulto es cada unidad embalada que se despacha. Cómo se embala lo enseña un instructor autorizado y no se explica aquí.",
        "La zona de despacho tiene riesgos propios: se mueven cargas a mano, los bultos apilados pueden caer, se usan flejes y elementos de corte, y el cartón y el plástico acumulados pueden incendiarse. Según la jerarquía de controles, primero se organiza el espacio y las cargas, con reglas como mover entre dos personas los bultos pesados, y al final se usan guantes y calzado. El EPP no reemplaza la autorización para manejar equipos de carga.",
        TAIL,
    ],
    vocab=[("embalaje", "protección del producto para que llegue sin daños"), ("rotular", "poner una etiqueta con la información del producto"), ("bulto", "unidad embalada que se despacha"), ("trazabilidad", "posibilidad de saber qué es un producto, de qué lote es y adónde va"), ("fleje", "banda que sujeta un bulto"), ("integridad", "que el producto llegue completo y sin daños")],
    worked=[
        ("Contar bultos", "Un despacho de ejemplo tiene 12 bultos y 5 pesan más de 17 kg. ¿Cuántos pesan 17 kg o menos?", ["Se restan los bultos pesados del total.", "12 menos 5 son 7."], "7 bultos"),
        ("Reconocer la etiqueta", "Una persona de ejemplo quiere saber de qué lote es un bulto sin abrirlo. ¿Qué mira?", ["La etiqueta lleva el código de lote.", "Así se mantiene la trazabilidad."], "La etiqueta o rótulo del bulto"),
    ],
    mistakes=[("Apilar bultos sin límite para aprovechar el espacio.", "Una pila muy alta puede caer.", "Se respeta la altura máxima y se organiza el espacio."),
              ("Mover un bulto pesado entre una sola persona porque «se puede».", "Se aumenta el riesgo de lesión.", "Se aplica la regla de mover entre dos personas los bultos pesados.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es rotular un bulto?", "Ponerle una etiqueta con la información que permite identificarlo", "Cubrirlo con plástico para protegerlo", "Medir su peso con una balanza", "Rotular es etiquetar; cubrir es parte del embalaje."),
        ("abc", "¿Qué es la trazabilidad de un producto despachado?", "Saber qué es, de qué lote es y adónde va", "Que llegue más rápido al cliente", "Que sea más barato de transportar", "La trazabilidad es el seguimiento de la historia del producto."),
        ("=", "{F} ¿Cuántos bultos pesan 17 kg o menos si 4 de los 10 pesan más?", "10-4", "Se restan los bultos pesados del total.", " bultos"),
        ("abc", "{F} ¿Qué dice la regla interna de ejemplo sobre un bulto de más de 17 kg?", "Lo mueven dos personas", "Lo mueve una sola persona con guantes", "No se despacha", "La regla indica que los bultos pesados los mueven dos personas."),
        ("abc", "{F} ¿Qué riesgo de la ficha se relaciona con el cartón y el plástico acumulados?", "Que puedan incendiarse", "El ruido de las máquinas", "La intoxicación por solventes", "El material acumulado es combustible y puede incendiarse con facilidad."),
        ("=", "{F} Cada una de las 3 personas recibe guantes y calzado de seguridad. ¿Cuántas piezas de EPP se entregan?", "3*2", "Se multiplican las personas por las dos piezas de cada una.", " piezas"),
        ("abc", "{F} ¿Hasta cuántos niveles se apilan los bultos según la ficha?", "Hasta 3 niveles", "Hasta 6 niveles", "Sin límite", "La ficha fija un máximo de ejemplo de 3 niveles."),
        ("=", "{F} Si en cada nivel hay 4 bultos y se apilan los 3 niveles permitidos, ¿cuántos bultos hay en la pila?", "4*3", "Se multiplican los bultos de cada nivel por los niveles.", " bultos"),
        ("abc", "{F} Una persona ve que la pila tiene 5 niveles. ¿Qué corresponde?", "Avisar al responsable para reducirla al máximo permitido", "Agregar un nivel más", "Apoyarse en ella para comprobar", "Una pila más alta que lo permitido puede caer."),
        ("ab", "{F} Un compañero dice: «con guantes puedo manejar el equipo de carga sin autorización». ¿Qué respuesta es correcta?", "No: el EPP no reemplaza la autorización para equipos de carga", "Sí: los guantes bastan", "La ficha pide personal autorizado para equipos de carga."),
        ("abc", "{F} Una estudiante dice: «sé qué es embalar, puedo embalar un mueble». ¿Qué respuesta es correcta?", "No: embalar exige instructor autorizado y norma vigente", "Sí: conocer el término la habilita", "Sí, con calzado", "Conocer un término no habilita para trabajar."),
        ("=", "{F} Si un camión lleva 10 bultos y hay 25 por despachar en total, ¿cuántos viajes se necesitan (redondeando hacia arriba)?", "(25+9)//10", "Se divide 25 en 10 y se redondea hacia arriba porque sobran bultos.", " viajes"),
        ("abc", "{F} ¿Qué datos mínimos lleva el registro de un bulto dañado?", "Cuál es, qué daño tiene, quién lo vio y cuándo", "Solo su peso", "Solo el nombre del conductor", "Un registro útil dice cuál, qué daño, quién y cuándo."),
    ],
    ctx=("abc", "En una zona de despacho de ejemplo, una pila de bultos cae sobre una persona. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Mover los bultos sin ayuda", "Esperar a que se levante sola", "Se avisa a quien corresponde y a emergencias; no se improvisa con la pila."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿qué es un bulto?", "Una unidad embalada que se despacha", "Cada unidad embalada se llama bulto."),
        ("¿Quién mueve un bulto de más de 17 kg según la regla de ejemplo?", "Dos personas", "La regla reduce el esfuerzo por persona."),
        ("¿Para qué sirve el rótulo?", "Para identificar y seguir el producto hasta el destino", "El rótulo permite la trazabilidad del producto hasta su destino."),
    ],
    op=("Despacho de ejemplo «Taller Quillay» (ficticio): 4 personas preparan 14 bultos; 6 pesan más de 17 kg (regla de ejemplo: los mueven dos personas). Cada persona recibe guantes y calzado de seguridad. Apilado máximo de ejemplo: 2 niveles. Escribe (a) cuántos bultos no son pesados, (b) cuántas piezas de EPP se entregan, (c) cuántos bultos caben en una pila de 2 niveles con 5 por nivel y (d) qué haces si una pila cae sobre alguien.",
        "(a) 14 menos 6 son 8 bultos. (b) 4×2 son 8 piezas. (c) 5×2 son 10 bultos. (d) No me acerco a la zona de riesgo, aviso a un adulto responsable y a emergencias.",
        ["calcula los bultos no pesados", "calcula el EPP entregado", "calcula la pila", "avisa sin acercarse al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["apilar sin límite", "mover un bulto pesado entre una persona", "intentar levantar la pila sin ayuda"],
        "Pregunta: «¿por qué hay una altura máxima de apilado?». Si no responde, pídele que relea la explicación."),
    reinforce="Escribe con tus palabras la diferencia entre embalar y rotular con un ejemplo.",
    extend="Explica por qué el cartón y el plástico acumulados son un riesgo de seguridad.",
)

# ============================================================ OAE-10, clase 2
F = ("Ficha 6 (documentos de despacho de ejemplo, inventados). Etiqueta de un bulto: código de producto «CM-ej 204», lote «L-ej 15», cliente (ficticio) «Cliente Ejemplo», destino «Bodega Sur de ejemplo», número de bulto «2 de 3», símbolos de manipulación: «frágil» y «este lado hacia arriba». "
     "Lista de empaque: 3 bultos por mueble. Guía de despacho: documento que acompaña la carga y lista los bultos. Registro electrónico de ejemplo (una planilla): una fila por bulto con código, lote, fecha, destino y responsable. "
     "Roles: despachador, bodeguero, transportista y cliente que recibe.")
build(
    O10, 2, F,
    use="Aprenderé qué datos lleva el rótulo de un bulto, qué es la lista de empaque, la guía de despacho y el registro electrónico, y qué rol cumple cada persona.",
    prior=["Sé qué es un bulto y la trazabilidad.", "Sé multiplicar.", "Sé leer una tabla."],
    explain=[
        "El rótulo de un bulto lleva los datos que permiten identificarlo y seguirlo: código del producto, lote, cliente, destino, número de bulto sobre el total y símbolos de manipulación. Los símbolos de manipulación son dibujos normalizados que indican cómo tratar el bulto, por ejemplo «frágil» o «este lado hacia arriba». La lista de empaque enumera el contenido de cada bulto; la guía de despacho acompaña la carga y lista los bultos que viajan.",
        "El registro electrónico es una planilla donde se anota, en forma digital, una fila por bulto con código, lote, fecha, destino y responsable; en este cuaderno se lee y se completa en papel. Su valor es la trazabilidad: si hay un reclamo, el registro permite saber qué lote y quién despachó. Los roles son el despachador, que prepara; el bodeguero, que entrega la carga; el transportista, que la lleva; y el cliente, que recibe y firma. Todos los datos de esta clase son inventados.",
        TAIL,
    ],
    vocab=[("rótulo", "etiqueta con los datos de identificación del bulto"), ("lote", "conjunto de producto fabricado junto, identificado con un código"), ("símbolo de manipulación", "dibujo normalizado que indica cómo tratar un bulto"), ("lista de empaque", "documento que enumera el contenido de cada bulto"), ("registro electrónico", "planilla digital con una fila por bulto"), ("transportista", "persona que lleva la carga al destino")],
    worked=[
        ("Leer una etiqueta", "Una etiqueta de ejemplo dice «bulto 3 de 5». ¿Cuántos bultos quedan por ver si este es el tercero?", ["Se restan los bultos vistos del total.", "5 menos 3 son 2."], "2 bultos"),
        ("Contar bultos de un pedido", "Un pedido de ejemplo tiene 4 muebles y cada uno viaja en 2 bultos. ¿Cuántos bultos son?", ["Se multiplican los muebles por los bultos de cada uno.", "4 por 2 son 8."], "8 bultos"),
    ],
    mistakes=[("Confundir la lista de empaque con la guía de despacho.", "Una enumera el contenido de cada bulto y la otra los bultos que viajan.", "Se usa cada documento según su función."),
              ("Poner una etiqueta con el número de bulto equivocado.", "El destinatario creerá que falta un bulto.", "Se revisa que el número sobre el total sea correcto.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es una lista de empaque?", "Un documento que enumera el contenido de cada bulto", "Una factura de compra de madera", "El plano del mueble", "La lista de empaque detalla qué hay en cada bulto."),
        ("abc", "¿Qué es un símbolo de manipulación en un bulto?", "Un dibujo normalizado que indica cómo tratarlo", "El nombre del transportista", "El precio del producto", "El símbolo comunica cómo manipular el bulto."),
        ("abc", "{F} ¿Cuál es el código del producto en la etiqueta?", "CM-ej 204", "L-ej 15", "Bodega Sur de ejemplo", "El código del producto es CM-ej 204; L-ej 15 es el lote."),
        ("abc", "{F} ¿Qué símbolo de manipulación indica que el producto se puede romper?", "Frágil", "Este lado hacia arriba", "No apilar", "«Frágil» advierte que el producto se puede romper."),
        ("=", "{F} ¿Cuántos bultos lleva un pedido de 7 muebles?", "7*3", "Se multiplican los muebles por los 3 bultos de cada uno.", " bultos"),
        ("=", "{F} Si el bulto es «2 de 3», ¿cuántos bultos del mismo mueble faltan por ver?", "3-2", "Se resta el número de este bulto del total del mueble.", " bulto"),
        ("abc", "{F} ¿Qué documento acompaña la carga y lista los bultos que viajan?", "La guía de despacho", "La lista de empaque", "El registro electrónico", "La guía acompaña la carga durante el viaje."),
        ("abc", "{F} ¿Qué rol lleva la carga al destino?", "El transportista", "El despachador", "El bodeguero", "El transportista traslada la carga desde el taller hasta el destino."),
        ("abc", "{F} ¿Qué datos lleva cada fila del registro electrónico?", "Código, lote, fecha, destino y responsable", "Solo el color del bulto", "Solo el peso", "La ficha indica esos cinco datos."),
        ("abc", "{F} Una etiqueta dice «bulto 4 de 3». ¿Qué corresponde?", "Detectar el error y corregir la etiqueta antes de despachar", "Despachar igual", "Cambiar el total para que cuadre", "El número no puede ser mayor que el total; se corrige antes de despachar."),
        ("ab", "{F} Un compañero dice: «la lista de empaque y la guía de despacho son lo mismo». ¿Qué respuesta es correcta?", "No: una enumera el contenido de cada bulto y la otra lista los bultos que viajan", "Sí: son sinónimos", "La ficha las presenta como documentos distintos."),
        ("abc", "{F} Una estudiante dice: «sé leer el rótulo, puedo manejar el equipo de carga». ¿Qué respuesta es correcta?", "No: manejar equipos exige personal autorizado y norma vigente", "Sí: leer un rótulo habilita", "Sí, con guantes", "Leer un rótulo no habilita para manejar equipos."),
        ("=", "{F} Si hay 5 muebles y se registra una fila por bulto (3 bultos por mueble), ¿cuántas filas tiene el registro electrónico?", "5*3", "Se multiplican los muebles por los bultos de cada uno.", " filas"),
    ],
    ctx=("abc", "En la zona de despacho de ejemplo, un bulto rotulado «frágil» se cae y un vidrio roto hiere a una persona. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Recoger los vidrios con las manos", "Seguir cargando el camión", "Ante una herida se avisa a quien corresponde y a emergencias."),
    sc=[
        ("¿Qué datos de identificación lleva el rótulo de un bulto?", "Código, lote, cliente, destino, número de bulto y símbolos", "Esos datos permiten identificar y seguir el producto."),
        ("En Muebles y Terminaciones en Madera: ¿para qué sirve el registro electrónico?", "Para la trazabilidad de los bultos despachados", "Permite saber qué lote y quién despachó."),
        ("¿Qué rol recibe y firma la entrega?", "El cliente", "La firma del cliente confirma la recepción."),
    ],
    op=("Documentos de ejemplo «Taller Ñire» (ficticio): pedido de 6 muebles; cada mueble viaja en 2 bultos. Etiqueta de un bulto: código «CM-ej 305», lote «L-ej 22», destino «Bodega Norte de ejemplo», «bulto 1 de 2», símbolos «frágil» y «este lado hacia arriba». Escribe (a) cuántos bultos hay, (b) cuántas filas tiene el registro electrónico, (c) qué datos lleva cada fila y (d) qué haces si una etiqueta dice «bulto 3 de 2».",
        "(a) 6×2 son 12 bultos. (b) 12 filas, una por bulto. (c) Código, lote, fecha, destino y responsable. (d) Detecto el error y corrijo la etiqueta antes de despachar.",
        ["calcula los bultos", "calcula las filas", "enumera los datos", "detecta el error de etiqueta"],
        ["hoja con las cuatro respuestas"],
        ["confundir lista de empaque con guía de despacho", "olvidar multiplicar por los muebles", "despachar con la etiqueta equivocada"],
        "Pregunta: «¿qué datos permiten la trazabilidad?». Si no responde, pídele que relea la explicación."),
    reinforce="Escribe una etiqueta de ejemplo con cinco datos para un bulto de una cómoda.",
    extend="Explica cómo ayuda el registro electrónico a resolver un reclamo del cliente.",
)

# ============================================================ OAE-10, clase 3
F = ("Ficha 7 (verificación de un despacho de ejemplo, inventada). Pedido de 6 bultos. Pesos de ejemplo, en kg: B1: 12; B2: 18; B3: 25; B4: 9; B5: 14; B6: 20. "
     "Regla de ejemplo: un bulto de más de 17 kg lo mueven dos personas. La lista de empaque anota 6 bultos; la guía de despacho anota 7. En la etiqueta de B4 el destino dice «Bodega Este de ejemplo» y el pedido va a «Bodega Sur de ejemplo». "
     "Capacidad de ejemplo del camión: 100 kg en total.")
build(
    O10, 3, F,
    use="Aprenderé a analizar un despacho en papel: comparar documentos, calcular pesos, aplicar una regla de manipulación y detectar errores de rotulado.",
    prior=["Sé qué es la lista de empaque y la guía de despacho.", "Sé sumar.", "Sé comparar números."],
    explain=[
        "Verificar un despacho es comparar lo que dicen los documentos con lo que hay: la lista de empaque, la guía de despacho y los rótulos deben coincidir en cantidad de bultos y en destino. Si no coinciden, no se despacha: se anota la diferencia y se avisa al responsable. Después se suman los pesos de los bultos para comprobar que no superan la capacidad del transporte, y se identifican los bultos que, según la regla interna, deben moverse entre dos personas.",
        "Cada diferencia se registra con el nombre de quien la detectó. Un destino equivocado en una etiqueta es un error grave porque el bulto llegará a otro lugar y se pierde la trazabilidad. Estos controles se hacen en papel antes de cargar; mover cargas y usar el camión lo hace personal autorizado. Los pesos, las capacidades y las reglas de esta clase son de ejemplo.",
        TAIL,
    ],
    vocab=[("coincidir", "que dos documentos digan lo mismo"), ("capacidad de carga", "peso máximo que puede llevar un transporte"), ("peso total", "suma de los pesos de todos los bultos"), ("destino", "lugar adonde va el bulto"), ("diferencia", "dato que no coincide entre dos documentos")],
    worked=[
        ("Sumar pesos", "Tres bultos de ejemplo pesan 10, 15 y 20 kg. ¿Cuánto pesan en total?", ["Se suman los tres pesos.", "10 más 15 más 20 son 45."], "45 kg"),
        ("Comparar con la capacidad", "Un camión de ejemplo carga 40 kg y los bultos pesan 45 kg. ¿Se pueden llevar todos?", ["Se compara 45 con 40.", "45 supera la capacidad."], "No, superan la capacidad"),
    ],
    mistakes=[("Despachar con documentos que no coinciden «para no perder el viaje».", "El cliente puede recibir menos bultos o en otro destino.", "Se anota la diferencia y se avisa al responsable antes de despachar."),
              ("Cargar el camión sobre su capacidad.", "Es un riesgo de accidente y de daño.", "Se suman los pesos y se respeta la capacidad.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es la capacidad de carga de un transporte?", "El peso máximo que puede llevar", "El número de personas que lo conducen", "El tiempo que tarda en llegar", "La capacidad de carga es un límite de peso."),
        ("abc", "¿Qué se hace si los documentos de un despacho no coinciden?", "Se anota la diferencia y se avisa al responsable antes de despachar", "Se despacha igual para no atrasar", "Se cambia un documento para que cuadre", "No se despacha con diferencias sin resolver."),
        ("=", "{F} ¿Cuántos kg pesan en total los 6 bultos?", "12+18+25+9+14+20", "Se suman los pesos de los seis bultos.", " kg"),
        ("abc", "{F} ¿Qué bultos deben moverse entre dos personas según la regla de ejemplo?", "B2, B3 y B6", "B1, B4 y B5", "Solo B3", "B2, B3 y B6 pesan más de 17 kg."),
        ("=", "{F} ¿Cuántos bultos pesan más de 17 kg?", "1+1+1", "Se cuenta cada bulto sobre 17 kg: B2, B3 y B6.", " bultos"),
        ("abc", "{F} ¿Se pueden llevar los 6 bultos en el camión de 100 kg?", "Sí, pesan 98 kg y la capacidad es 100 kg", "No, pesan más de 100 kg", "No, porque un bulto pesa más de 17 kg", "98 kg no superan los 100 kg de capacidad."),
        ("=", "{F} ¿Cuántos kg sobran de la capacidad del camión después de cargar los 6 bultos?", "100-98", "Se resta el peso total de la capacidad.", " kg"),
        ("=", "{F} ¿Cuántos bultos de diferencia hay entre la guía de despacho y la lista de empaque?", "7-6", "Se resta lo anotado en la lista de lo anotado en la guía.", " bulto"),
        ("abc", "{F} ¿Qué error de rotulado hay en el bulto B4?", "Su destino no coincide con el del pedido", "Su peso es demasiado alto", "Su número de bulto es mayor al total", "La etiqueta dice Bodega Este y el pedido va a Bodega Sur."),
        ("abc", "{F} ¿Qué corresponde hacer con el bulto B4?", "Corregir la etiqueta antes de despachar y registrar la diferencia", "Despacharlo igual", "Cambiar el destino del pedido", "Un destino equivocado se corrige antes de salir."),
        ("ab", "{F} Un compañero dice: «B2 pesa 18 kg, apenas más que 17, lo muevo yo solo». ¿Qué respuesta es correcta?", "No: la regla pide dos personas para más de 17 kg", "Sí: 1 kg de diferencia no importa", "La ficha fija la regla en más de 17 kg."),
        ("abc", "{F} Una estudiante dice: «ya verifiqué el despacho en papel, puedo conducir el camión». ¿Qué respuesta es correcta?", "No: conducir y mover cargas exige personal autorizado y norma vigente", "Sí: verificar habilita para conducir", "Sí, con guantes", "Una verificación en papel no habilita para operar vehículos ni equipos."),
        ("=", "{F} Si se agrega un séptimo bulto de 6 kg, ¿cuántos kg pesarían en total los 7 bultos?", "98+6", "Se suma el nuevo bulto al peso total de 98 kg.", " kg"),
    ],
    ctx=("abc", "En la zona de carga de ejemplo, un camión retrocede sin señalero y casi atropella a una persona que verificaba bultos. ¿Qué respuesta es correcta?", "Avisar al responsable y no acercarse a los vehículos en movimiento", "Seguir verificando cerca del camión", "Poner el pie detrás del camión para detenerlo", "Los vehículos en movimiento son un riesgo; se avisa a quien corresponde."),
    sc=[
        ("¿Qué se compara al verificar un despacho?", "La lista de empaque, la guía de despacho y los rótulos", "Los documentos del despacho deben coincidir entre sí y con la carga."),
        ("En Muebles y Terminaciones en Madera: ¿qué se hace con un bulto de más de 17 kg según la regla de ejemplo?", "Lo mueven dos personas", "La regla reduce el esfuerzo por persona."),
        ("¿Qué pasa si el peso total supera la capacidad del camión?", "No se puede cargar todo junto", "Cargar sobre la capacidad es un riesgo."),
    ],
    op=("Despacho de ejemplo «Taller Peumo» (ficticio): 5 bultos de 8, 16, 22, 11 y 19 kg. Regla de ejemplo: más de 17 kg, dos personas. Capacidad del camión: 70 kg. La lista de empaque anota 5 bultos y la guía de despacho 4. Escribe (a) el peso total, (b) cuántos bultos requieren dos personas, (c) si el camión puede llevarlos todos y (d) qué haces con la diferencia entre documentos.",
        "(a) 8+16+22+11+19 son 76 kg. (b) 2 bultos: 22 y 19 kg. (c) No: 76 kg superan los 70 kg. (d) Anoto la diferencia y aviso al responsable antes de despachar.",
        ["suma los pesos", "cuenta los bultos pesados", "compara con la capacidad", "registra la diferencia"],
        ["hoja con las cuatro respuestas"],
        ["no sumar todos los bultos", "despachar con diferencias", "contar mal los bultos pesados"],
        "Pregunta: «¿por qué se cuentan los bultos sobre 17 kg?». Si no responde, pídele que relea la regla."),
    reinforce="Suma los pesos de cuatro bultos de ejemplo de 7, 13, 19 y 21 kg y cuenta cuáles pesan más de 17 kg.",
    extend="Explica por qué un destino equivocado en una etiqueta es un error grave de trazabilidad.",
)

# ============================================================ OAE-10, clase 4
F = ("Ficha 8 (cálculo de insumos de embalaje de ejemplo, inventado). Pedido de 30 muebles; cada mueble viaja en 2 bultos. Cada bulto usa 4 esquineros de cartón. Merma de ejemplo de 10 % sobre los esquineros. "
     "Un rollo de film cubre 15 bultos (dato de ejemplo). Peso promedio de ejemplo de un bulto: 20 kg. Capacidad de un camión de ejemplo: 1.100 kg. Un camión no puede llevar más de 55 bultos de ese peso.")
build(
    O10, 4, F,
    use="Aprenderé a calcular en papel los insumos de embalaje, el número de viajes y el código de trazabilidad de un pedido, con datos de ejemplo.",
    prior=["Sé calcular una merma.", "Sé dividir con resto.", "Sé qué es la trazabilidad."],
    explain=[
        "Planificar un despacho en papel combina cuatro cálculos. Los bultos son los muebles multiplicados por los bultos de cada uno. Los insumos de embalaje, como los esquineros de cartón, se obtienen multiplicando los bultos por los esquineros de cada uno y sumando la merma. Los rollos de film se calculan dividiendo los bultos por los que cubre cada rollo, redondeando hacia arriba. Los viajes se calculan dividiendo el peso total por la capacidad del camión, también hacia arriba.",
        "Cada bulto lleva un código de trazabilidad que combina datos como producto, lote y número de bulto, para que el registro permita seguirlo. Un cambio de cantidad en el pedido obliga a recalcular todo y a actualizar los registros. El trabajo físico de embalar, rotular y cargar lo hace personal autorizado; estos cálculos son de planilla y sus números son inventados.",
        TAIL,
    ],
    vocab=[("esquinero", "pieza que protege las esquinas de un bulto"), ("film", "plástico que envuelve un bulto"), ("código de trazabilidad", "combinación de datos que identifica cada bulto"), ("viaje", "trayecto de un camión cargado"), ("recalcular", "volver a calcular cuando cambia un dato")],
    worked=[
        ("Bultos de un pedido", "Un pedido de ejemplo tiene 12 muebles y cada uno va en 3 bultos. ¿Cuántos bultos son?", ["Se multiplican los muebles por los bultos de cada uno.", "12 por 3 son 36."], "36 bultos"),
        ("Rollos de film", "Un rollo de ejemplo cubre 8 bultos y hay 30. ¿Cuántos rollos se necesitan?", ["30 dividido en 8 da 3 y sobran 6.", "Se redondea hacia arriba."], "4 rollos"),
    ],
    mistakes=[("Olvidar la merma de los esquineros.", "Algunos se dañan y faltarían para el último bulto.", "Se suma la merma a la cantidad calculada."),
              ("Despachar en un solo viaje un peso mayor que la capacidad.", "Es un riesgo para el vehículo y las personas.", "Se calculan los viajes redondeando hacia arriba.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿para qué sirve un esquinero de un bulto?", "Para proteger las esquinas del bulto", "Para pegar la etiqueta", "Para medir el peso", "El esquinero protege las esquinas de los golpes."),
        ("abc", "¿Para qué sirve el código de trazabilidad de un bulto?", "Para identificar cada bulto y seguirlo en los registros", "Para decorar la etiqueta", "Para reducir el peso", "El código permite seguir cada bulto."),
        ("=", "{F} ¿Cuántos bultos tiene el pedido?", "30*2", "Se multiplican los muebles por los bultos de cada uno.", " bultos"),
        ("=", "{F} ¿Cuántos esquineros se necesitan sin merma para los 60 bultos?", "60*4", "Se multiplican los bultos por los esquineros de cada uno.", " esquineros"),
        ("=", "{F} ¿Cuántos esquineros hay que comprar con la merma de 10 % (240 esquineros)?", "240*110//100", "Se calcula el 110 % de la cantidad: el total más la merma de 10 %.", " esquineros"),
        ("=", "{F} ¿Cuántos rollos de film se necesitan para 60 bultos, si cada rollo cubre 15?", "(60+14)//15", "Se divide 60 en 15 y se redondea hacia arriba si queda resto.", " rollos"),
        ("=", "{F} ¿Cuántos kg pesan en total los 60 bultos de 20 kg?", "60*20", "Se multiplican los bultos por el peso de cada uno.", " kg"),
        ("=", "{F} ¿Cuántos viajes se necesitan para 1.200 kg con un camión de 1.100 kg, redondeando hacia arriba?", "(1200+1099)//1100", "Se divide 1.200 en 1.100 y se redondea hacia arriba porque sobra peso.", " viajes"),
        ("abc", "{F} Un camión cargado con 55 bultos de 20 kg, ¿cumple la capacidad de 1.100 kg?", "Sí, justo: pesa 1.100 kg", "No: pesa más de 1.100 kg", "No: pesa menos de 1.000 kg", "55 por 20 son 1.100 kg, igual a la capacidad."),
        ("abc", "{F} El cliente añade 5 muebles al pedido. ¿Qué corresponde?", "Recalcular los bultos, los insumos y los registros", "Mantener los cálculos originales", "Cargar más bultos sin avisar", "Un cambio de cantidad obliga a recalcular todo."),
        ("ab", "{F} Un compañero dice: «no hace falta sumar la merma de los esquineros». ¿Qué respuesta es correcta?", "No: la merma cubre esquineros dañados y evita quedarse cortos", "Sí: la merma nunca es necesaria", "La ficha incluye una merma de ejemplo de 10 %."),
        ("abc", "{F} Una estudiante dice: «ya calculé el embalaje, puedo embalar y cargar el camión». ¿Qué respuesta es correcta?", "No: embalar y cargar exige personal autorizado y norma vigente", "Sí: calcular habilita para embalar", "Sí, con guantes", "Un cálculo en papel no habilita para trabajar ni operar equipos."),
        ("=", "{F} Si el pedido fuera de 40 muebles, ¿cuántos bultos serían?", "40*2", "Se multiplican los muebles por los bultos de cada uno.", " bultos"),
    ],
    ctx=("abc", "En la zona de carga de ejemplo, el jefe quiere cargar 70 bultos en un solo viaje para ahorrar, aunque supere la capacidad del camión. ¿Qué respuesta es correcta?", "No: se respeta la capacidad y se programan más viajes", "Sí: ahorrar es lo más importante", "Sí, si se amarra bien", "Sobrecargar un camión es un riesgo de accidente."),
    sc=[
        ("¿Qué se hace con el resto al calcular los rollos de film?", "Se compra un rollo más", "Un rollo incompleto igual se compra entero."),
        ("En Muebles y Terminaciones en Madera: ¿qué hay que hacer si cambia la cantidad del pedido?", "Recalcular bultos, insumos y registros", "Todos los cálculos dependen de la cantidad."),
        ("¿Por qué se respeta la capacidad de carga del camión?", "Porque sobrecargarlo es un riesgo de accidente", "La capacidad es un límite de seguridad."),
    ],
    op=("Planificación de ejemplo «Taller Quillay» (ficticio): 20 muebles; cada uno viaja en 3 bultos; cada bulto usa 4 esquineros; merma de ejemplo de 25 % sobre los esquineros; un rollo de film cubre 12 bultos; peso de ejemplo de un bulto: 15 kg; capacidad del camión: 600 kg. Escribe (a) los bultos, (b) los esquineros con la merma, (c) los rollos de film y (d) los viajes.",
        "(a) 20×3 son 60 bultos. (b) 60×4 son 240 y con 25 % son 300 esquineros. (c) 60÷12 son 5 rollos. (d) 60×15 son 900 kg; 900÷600 da 1 y sobran 300: 2 viajes.",
        ["calcula los bultos", "calcula esquineros con merma", "calcula los rollos", "calcula los viajes"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la merma", "redondear hacia abajo", "olvidar multiplicar por los bultos"],
        "Pregunta: «¿por qué se redondea hacia arriba el número de viajes?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula los rollos de film que se necesitan para 50 bultos si cada rollo cubre 12.",
    extend="Explica qué datos de un bulto conviene incluir en su código de trazabilidad.",
)
