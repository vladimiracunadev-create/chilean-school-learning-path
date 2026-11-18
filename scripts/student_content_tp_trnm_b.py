"""Tripulación de Naves Mercantes y Especiales TP 3.º y 4.º medio: OAE-03 (mantenimiento básico como plan y registro) y OAE-04 (equipos de maniobra: conceptos, capacidades y registros). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_trnm_common import AVISO, EMER, build

O3 = "TP-TRNM-3y4-OAE-03"
O4 = "TP-TRNM-3y4-OAE-04"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El plan de mantenimiento de la «Nave Demo» lista 8 equipos del área de máquinas, con 3 tareas por equipo cada mes. El área tiene 4 personas por turno. "
     "Peligros anotados: superficies calientes, energía almacenada en los equipos (presión, resortes o electricidad), aceite usado que puede contaminar el mar y herramientas manuales.")
build(
    O3, 1, F,
    use="Aprenderé qué es el mantenimiento básico, cómo se ordena en un plan, qué peligros tiene y por qué cuidar el medio ambiente es parte del trabajo.",
    prior=["Sé qué hay en el área de máquinas de una nave.", "Sé qué es la jerarquía de controles.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "El mantenimiento es el conjunto de tareas que se hacen para que un equipo siga funcionando bien y de forma segura. El mantenimiento básico reúne las tareas simples del plan de mantenimiento, que es el documento que lista los equipos, las tareas y cada cuánto se hacen. Esas tareas se hacen siguiendo el manual del fabricante, que trae las especificaciones del equipo, y por personal autorizado con sus implementos de seguridad. Este cuaderno enseña a leer y planificar, no a intervenir equipos.",
        "Un equipo detenido puede seguir siendo peligroso, porque puede conservar energía almacenada: presión en una cañería, electricidad en un cable o un resorte tensado. Por eso solo personal autorizado, con los permisos y el aislamiento de energía que fija la norma vigente, interviene un equipo. El cuidado del medio ambiente también es parte del plan: los residuos, como el aceite usado, se guardan en envases rotulados y se entregan según la norma vigente; no se vierten al mar. Un ejemplo con otra nave: un trapo con aceite se guarda en un recipiente cerrado para residuos y no se arroja por la borda.",
        f"Cada tarea hecha o pendiente se anota en un registro con fecha y responsable. {EMER} {AVISO}",
    ],
    vocab=[("mantenimiento", "tareas que mantienen un equipo funcionando bien y de forma segura"), ("plan de mantenimiento", "documento que lista equipos, tareas y cada cuánto se hacen"), ("manual del fabricante", "documento del fabricante con las especificaciones del equipo"), ("energía almacenada", "energía que un equipo detenido aún conserva, como presión o electricidad"), ("residuo", "material usado que no sirve y debe manejarse según la norma vigente"), ("implementos de seguridad", "equipos de protección que usa el personal autorizado")],
    worked=[
        ("Leer un plan", "Un plan de ejemplo lista 5 equipos con 2 tareas por equipo cada mes. ¿Cuántas tareas hay en un mes?", ["Cada equipo tiene 2 tareas.", "Se multiplican 5 equipos por 2 tareas."], "10 tareas al mes"),
        ("Un residuo", "En una nave de ejemplo queda aceite usado después de una tarea del plan. ¿Dónde se guarda según el cuidado del medio ambiente?", ["El aceite usado es un residuo y puede contaminar el mar.", "Se guarda en un envase rotulado y se entrega según la norma vigente."], "En un envase rotulado, para entregarlo según la norma vigente"),
    ],
    mistakes=[("Creer que un equipo detenido es seguro de intervenir.", "Puede conservar energía almacenada, como presión o electricidad.", "Solo personal autorizado interviene un equipo, con los permisos de la norma vigente."),
              ("Creer que verter poco aceite al mar no importa.", "Todo vertido contamina el medio marino y está regulado por la norma vigente.", "Guarda los residuos en envases rotulados y entrégalos según la norma vigente.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es un plan de mantenimiento?", "El documento que lista los equipos, las tareas y cada cuánto se hacen", "El registro de las lecturas de una ronda de instrumentos", "La lista de repuestos que hay en la bodega", "El plan lista equipos, tareas y frecuencias; las lecturas y los repuestos se anotan en otros documentos."),
        ("abc", "En Tripulación de Naves: ¿qué es el manual del fabricante?", "El documento del fabricante con las especificaciones e indicaciones del equipo", "El reglamento general de la nave escrito por la tripulación", "El registro de horas de las guardias", "El manual es la fuente de las especificaciones del equipo; no es un reglamento de la nave."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la energía almacenada en un equipo?", "Que una parte se mueva o libere presión de forma inesperada y lesione a alguien", "Que el plan de mantenimiento quede desactualizado", "Que falte aceite en la bodega", "El riesgo es un daño a las personas; el plan y la bodega no lo son."),
        ("=", "{F} ¿Cuántas tareas de mantenimiento hay en un mes, según el plan?", "8*3", "Se multiplican los equipos del plan por las tareas de cada equipo.", " tareas"),
        ("abc", "{F} Después de una tarea queda aceite usado. ¿Qué corresponde para cuidar el medio ambiente?", "Guardarlo en un envase rotulado y entregarlo según la norma vigente", "Verterlo al mar si es poco", "Mezclarlo con el agua del fondo de la nave para diluirlo", "El aceite usado es un residuo regulado; verterlo o diluirlo contamina el medio marino."),
        ("abc", "{F} ¿Por qué un equipo detenido puede seguir siendo peligroso?", "Porque puede conservar energía almacenada, como presión o electricidad", "Porque los equipos detenidos siempre se calientan más", "Porque el manual del fabricante lo prohíbe", "Un equipo detenido puede conservar presión o electricidad que se libera de forma inesperada."),
        ("=", "{F} ¿Cuántas tareas hay en 3 meses, según el plan?", "8*3*3", "Se multiplican las tareas de un mes por los 3 meses.", " tareas"),
        ("=", "{F} Si las tareas de un mes se repartieran en la planilla por igual entre las personas de un turno, ¿cuántas tareas le tocarían a cada persona?", "8*3//4", "Se calculan las tareas del mes y se dividen entre las 4 personas del turno.", " tareas"),
        ("abc", "{F} ¿Qué medida actúa sobre el peligro de las superficies calientes y no solo sobre la persona?", "Cubrirlas con una aislación fija", "Entregar guantes a cada persona", "Colocar un letrero de aviso", "La aislación cambia el lugar; los guantes son EPP y el letrero solo informa."),
        ("abc", "En el área de máquinas de ejemplo una persona queda inmóvil junto a un equipo con un cable pelado. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, dar la alarma y avisar a un adulto responsable y a emergencias", "Tocarla para apartarla del equipo", "Apagar el equipo con la mano", "Tocar a la persona o al equipo puede causar otro accidente; se da la alarma y se avisa."),
        ("abc", "{F} Un compañero dice: «como el equipo está detenido, puedo intervenirlo sin permiso». ¿Qué respuesta es correcta?", "Es falso: puede conservar energía y solo personal autorizado lo interviene", "Es cierto, porque no hay peligro si no funciona", "Es cierto, si usa guantes", "Un equipo detenido puede tener energía almacenada; los guantes no reemplazan la autorización."),
        ("=", "{F} Cada equipo del plan genera 4 litros de aceite usado al mes. Si los envases para residuos son de 16 litros, ¿cuántos envases se llenan en un mes?", "8*4//16", "Se calculan los litros del mes y se dividen entre la capacidad de cada envase.", " envases"),
        ("abc", "{F} Una tarea del plan no se pudo hacer por falta de un repuesto. ¿Qué corresponde?", "Registrarla como pendiente con el motivo e informar al oficial de máquinas", "Anotarla como realizada para no atrasar el plan", "Borrarla del plan", "Un registro honesto deja constancia de lo pendiente y de su causa."),
    ],
    ctx=("abc", "Un conocido te ofrece «ayudarlo a cambiar el aceite» del motor de la nave de un familiar para ganar experiencia. ¿Qué respondes?", "Que no, porque esa tarea exige personal autorizado, instructor y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si vas con guantes", "Que sí, si el motor está apagado", "Un equipo apagado puede tener energía almacenada y los guantes no reemplazan la autorización."),
    sc=[
        ("En Tripulación de Naves: ¿qué es la energía almacenada?", "La energía que un equipo detenido aún conserva", "Un equipo detenido puede mantener presión o electricidad."),
        ("¿Dónde se guarda un residuo como el aceite usado?", "En un envase rotulado, para entregarlo según la norma vigente", "El residuo no se vierte al mar."),
        ("¿Quién interviene los equipos según el plan?", "Personal autorizado", "Intervenir un equipo exige autorización y formación."),
    ],
    op=("Plan de ejemplo de la «Nave Ejemplo»: 6 equipos con 2 tareas por equipo cada mes; cada tarea genera 3 litros de aceite usado. Peligros anotados: superficie caliente y energía almacenada. Escribe (a) cuántas tareas hay al mes, (b) cuántos litros de aceite usado se generan, (c) cómo se maneja ese residuo, (d) por qué la persona en formación no interviene el equipo y qué hace en cambio.",
        "(a) 6 × 2 = 12 tareas. (b) 12 × 3 = 36 litros. (c) Se guarda en envases rotulados y se entrega según la norma vigente; no se vierte al mar. (d) Porque el equipo puede conservar energía almacenada y solo personal autorizado lo interviene; la persona en formación lee el plan, registra y avisa al oficial.",
        ["calcula las tareas del mes", "calcula los litros de residuo", "explica el manejo del residuo", "explica por qué no interviene el equipo"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por los equipos", "proponer verter el aceite", "proponer que la persona en formación intervenga"],
        "Pregunta: «¿cuántas tareas hay en total y cuántos litros genera cada una?». Si no responde, pídele que escriba las dos multiplicaciones."),
    reinforce="Escribe un plan de ejemplo con tres equipos y dos tareas por equipo, y calcula cuántas tareas hay al mes.",
    extend="Explica con un ejemplo por qué cuidar el medio ambiente forma parte de un plan de mantenimiento.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (extracto de plan, de ejemplo, inventado). Generador 1: inspección de filtros cada 500 horas de funcionamiento. Bomba de achique: inspección del sello cada 250 horas. Compresor: cambio de aceite cada 1.000 horas. "
     "Orden de trabajo OT-17: equipo, bomba de achique; tarea, inspección del sello; estado, pendiente; responsable, sin asignar.")
build(
    O3, 2, F,
    use="Aprenderé la diferencia entre mantenimiento preventivo y correctivo y qué documentos y roles intervienen en el mantenimiento de una nave.",
    prior=["Sé qué es un plan de mantenimiento.", "Sé qué es el manual del fabricante.", "Sé dividir números enteros."],
    explain=[
        "El mantenimiento preventivo se hace antes de que el equipo falle, según el plan, por ejemplo cada cierto número de horas de funcionamiento. El mantenimiento correctivo se hace después de una falla, para dejar el equipo en condiciones de volver a funcionar. La inspección es una revisión para detectar desgaste o problemas. Las horas de funcionamiento se leen en un horómetro, un instrumento que cuenta las horas que un equipo ha trabajado.",
        "El trabajo se ordena con documentos. La orden de trabajo pide una tarea y registra el equipo, qué se hizo, cuándo, quién la hizo y qué repuestos usó; un repuesto es una pieza que reemplaza a otra desgastada. La hoja de vida de un equipo es su historial de horas y de tareas. La hoja de datos de seguridad de un producto, como un aceite, dice qué peligros tiene. El jefe de máquinas decide el plan; el tripulante en formación lee, registra y avisa.",
        f"Un ejemplo con otra nave: una bomba con inspección cada 300 horas lleva 900 horas desde la última, es decir, le corresponden tres inspecciones. {EMER} {AVISO}",
    ],
    vocab=[("mantenimiento preventivo", "el que se hace antes de la falla, según el plan"), ("mantenimiento correctivo", "el que se hace después de una falla"), ("inspección", "revisión para detectar desgaste o problemas"), ("horómetro", "instrumento que cuenta las horas de funcionamiento de un equipo"), ("orden de trabajo", "documento que pide una tarea y registra quién, cuándo y con qué repuestos se hizo"), ("hoja de vida", "historial de horas y tareas de un equipo"), ("repuesto", "pieza que reemplaza a otra desgastada"), ("hoja de datos de seguridad", "documento que dice qué peligros tiene un producto")],
    worked=[
        ("Clasificar un mantenimiento", "Un compresor de ejemplo se revisa cada 800 horas aunque funcione bien. ¿Es preventivo o correctivo?", ["La revisión se hace según el plan y antes de una falla.", "Lo que se hace antes de la falla es preventivo."], "Mantenimiento preventivo"),
        ("Contar tareas por horas", "Una bomba de ejemplo se inspecciona cada 200 horas. ¿Cuántas inspecciones corresponden en 1.000 horas?", ["Se divide el total de horas entre las horas de cada inspección.", "1.000 ÷ 200."], "5 inspecciones"),
    ],
    mistakes=[("Creer que mantenimiento correctivo y preventivo son lo mismo.", "El preventivo se hace antes de la falla y el correctivo después de ella.", "Pregúntate si el equipo ya falló."),
              ("Creer que la orden de trabajo es opcional si la tarea fue pequeña.", "Sin registro no se sabe quién hizo qué ni cuándo.", "Toda tarea se anota con fecha y responsable.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es el mantenimiento preventivo?", "El que se hace antes de la falla, según el plan", "El que se hace después de una falla", "El que se hace solo cuando el oficial lo pide", "El preventivo se anticipa a la falla; el correctivo es posterior a ella."),
        ("abc", "En Tripulación de Naves: ¿qué es un horómetro?", "Un instrumento que cuenta las horas de funcionamiento de un equipo", "Un instrumento que mide la temperatura del aceite", "Un registro de las guardias de la tripulación", "El horómetro cuenta horas de trabajo del equipo; la temperatura la mide un termómetro."),
        ("abc", "En Tripulación de Naves: ¿qué registra una orden de trabajo?", "La tarea, el equipo, quién la hizo, cuándo y con qué repuestos", "Solo la fecha de compra del equipo", "Solo el nombre del fabricante", "La orden de trabajo es el registro de una tarea concreta y sus responsables."),
        ("abc", "{F} La inspección de filtros del generador 1 cada 500 horas es un mantenimiento:", "Preventivo, porque está en el plan y se hace antes de una falla", "Correctivo, porque revisa filtros", "Correctivo, porque se hace con horómetro", "Una tarea planificada por horas es preventiva; el correctivo se hace tras una falla."),
        ("abc", "{F} ¿Cuál es el estado de la orden de trabajo OT-17 de la ficha?", "Pendiente y sin responsable asignado", "Realizada por el jefe de máquinas", "Cancelada por falta de repuestos", "La ficha dice estado pendiente y responsable sin asignar."),
        ("abc", "{F} ¿Qué documento registra el historial de horas y de tareas de un equipo?", "La hoja de vida del equipo", "La hoja de datos de seguridad del aceite", "El manual del fabricante", "La hoja de vida es el historial; el manual y la hoja de seguridad tienen otro fin."),
        ("=", "{F} ¿Cuántas inspecciones del sello de la bomba de achique corresponden en 1.000 horas de funcionamiento?", "1000//250", "Se divide el total de horas entre las horas de cada inspección.", " inspecciones"),
        ("=", "{F} ¿Cuántas inspecciones de filtros corresponden al generador 1 en 3.000 horas de funcionamiento?", "3000//500", "Se divide el total de horas entre las horas de cada inspección.", " inspecciones"),
        ("abc", "{F} ¿Quién decide el plan de mantenimiento de los equipos de máquinas de una nave?", "El jefe de máquinas", "El tripulante en formación", "El fabricante de otra nave", "El plan lo decide el jefe de máquinas; la persona en formación lee y registra."),
        ("abc", "El compresor de una nave de ejemplo se detiene por una falla y se repara. ¿Qué tipo de mantenimiento es esa reparación?", "Correctivo, porque se hace después de la falla", "Preventivo, porque el equipo se vuelve a usar", "Ninguno, porque no estaba en el plan", "Reparar tras una falla es mantenimiento correctivo, esté o no en el plan."),
        ("abc", "{F} Una orden de trabajo se completa sin hora ni responsable. ¿Qué problema tiene?", "No se sabe quién hizo la tarea ni cuándo, y no sirve como registro", "Ninguno, porque basta con anotar el equipo", "Que el equipo queda más seguro", "Sin hora ni responsable el registro no permite saber qué ocurrió."),
        ("=", "{F} La bomba de achique lleva 600 horas desde su última inspección del sello. ¿Cuántas inspecciones completas debieron hacerse en ese tiempo?", "600//250", "Se divide el tiempo transcurrido entre las horas de cada inspección y se cuentan las completas.", " inspecciones"),
        ("abc", "{F} Un compañero dice: «el cambio de aceite del compresor lo hago yo, porque ya vi cómo se hace». ¿Qué respuesta es correcta?", "Es falso: la tarea la hace personal autorizado con el manual y la orden de trabajo", "Es cierto, si ya lo vio una vez", "Es cierto, si se anota después en el plan", "Haber visto una tarea no autoriza a hacerla."),
    ],
    ctx=("abc", "Al revisar la hoja de vida de una bomba de ejemplo notas que la última tarea anotada no tiene fecha. La persona a cargo dice: «no importa, ponle la fecha de hoy». ¿Qué corresponde?", "Informar que falta el dato y no inventar la fecha", "Ponerle la fecha de hoy, porque ella manda", "Borrar la tarea de la hoja de vida", "Una fecha inventada falsea el historial; se informa que falta el dato."),
    sc=[
        ("En Tripulación de Naves: ¿cuándo se hace un mantenimiento correctivo?", "Después de una falla", "Correctivo significa corregir una falla ya ocurrida."),
        ("¿Qué es un repuesto?", "Una pieza que reemplaza a otra desgastada", "El repuesto sustituye una pieza que ya no sirve."),
        ("¿Qué instrumento cuenta las horas de funcionamiento?", "El horómetro", "El horómetro mide horas de trabajo."),
    ],
    op=("Plan de ejemplo: motor auxiliar, inspección de la correa cada 400 horas; bomba de enfriamiento, inspección del sello cada 300 horas. Hoja de vida: el motor lleva 1.600 horas desde su instalación y la bomba, 1.200 horas. Escribe (a) cuántas inspecciones de correa corresponden al motor, (b) cuántas inspecciones de sello corresponden a la bomba, (c) qué tipo de mantenimiento son esas inspecciones y por qué, (d) qué debe registrar una orden de trabajo.",
        "(a) 1.600 ÷ 400 = 4 inspecciones. (b) 1.200 ÷ 300 = 4 inspecciones. (c) Preventivo, porque se hacen según el plan y antes de una falla. (d) La tarea, el equipo, quién la hizo, cuándo y con qué repuestos.",
        ["calcula las inspecciones del motor", "calcula las inspecciones de la bomba", "clasifica el mantenimiento", "indica qué registra una orden de trabajo"],
        ["hoja con las cuatro respuestas"],
        ["confundir preventivo con correctivo", "dividir por el equipo equivocado", "olvidar quién y cuándo en la orden de trabajo"],
        "Pregunta: «¿cada cuántas horas se hace cada inspección?». Si no responde, pídele que escriba la división."),
    reinforce="Escribe tres ejemplos inventados de mantenimiento preventivo y uno de correctivo.",
    extend="Explica por qué la hoja de vida de un equipo ayuda a decidir el mantenimiento.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (hoja de vida de ejemplo, inventada). Horas actuales del horómetro y última tarea hecha. Generador 1: 1.650 horas; última inspección de filtros a las 1.200 horas; se repite cada 500 horas. "
     "Bomba de achique: 1.100 horas; última inspección del sello a las 800 horas; se repite cada 250 horas. Compresor: 3.400 horas; último cambio de aceite a las 3.000 horas; se repite cada 1.000 horas.")
build(
    O3, 3, F,
    use="Aprenderé a leer una hoja de vida, a calcular cuándo toca la próxima tarea de un plan y a informar las tareas vencidas o próximas.",
    prior=["Sé qué es un plan de mantenimiento y un horómetro.", "Sé sumar y restar números enteros.", "Sé qué es una orden de trabajo."],
    explain=[
        "Para saber cuándo toca una tarea se usa la hoja de vida. La hora de la próxima tarea es la hora de la última más lo que se repite: próxima = última + cada cuántas horas. Las horas que faltan son la próxima menos las horas actuales del horómetro. Si las horas actuales ya pasaron la hora de la próxima tarea, la tarea está vencida, y las horas de retraso son las actuales menos la próxima.",
        "Un ejemplo con otro equipo: una bomba con la última inspección a las 400 horas, que se repite cada 300 horas, tiene la próxima a las 700 horas; si el horómetro marca 650 horas, faltan 50 horas, y si marcara 720, estaría vencida por 20 horas. Una tarea vencida o próxima se informa al oficial de máquinas, que decide cuándo se hace; la persona en formación no la hace por su cuenta.",
        f"Se informa primero lo vencido, luego lo próximo y al final lo lejano, siempre con las horas exactas. {EMER} {AVISO}",
    ],
    vocab=[("próxima tarea", "hora del horómetro en la que toca la siguiente tarea del plan"), ("vencida", "tarea cuya hora del plan ya pasó sin haberse hecho"), ("horas de retraso", "horas actuales menos la hora de la próxima tarea"), ("horas que faltan", "hora de la próxima tarea menos las horas actuales"), ("prioridad", "orden en que se informan o atienden las tareas")],
    worked=[
        ("Calcular la próxima", "Un equipo de ejemplo tuvo su última inspección a las 900 horas y se repite cada 400. ¿A qué hora toca la próxima?", ["Próxima = última + lo que se repite.", "900 + 400."], "A las 1.300 horas"),
        ("Detectar un retraso", "El horómetro de ese equipo marca 1.350 horas. ¿Está vencida su tarea? ¿Por cuántas horas?", ["La próxima toca a las 1.300 horas y el horómetro ya la pasó.", "Se resta 1.350 − 1.300."], "Sí, vencida por 50 horas"),
    ],
    mistakes=[("Calcular la próxima tarea sumando a las horas actuales y no a la hora de la última tarea.", "El plan cuenta desde la última tarea hecha, no desde hoy.", "Suma lo que se repite a la hora de la última tarea."),
              ("Creer que una tarea con pocas horas de retraso no se informa.", "Una tarea vencida se informa siempre, aunque el retraso sea corto.", "Informa toda tarea vencida y las próximas con sus horas.")],
    T=[
        ("=", "{F} ¿Cuántas horas de funcionamiento lleva el generador 1 desde su última inspección de filtros?", "1650-1200", "Se resta la hora de la última inspección a las horas actuales.", " horas"),
        ("=", "{F} ¿A qué hora del horómetro toca la próxima inspección de filtros del generador 1?", "1200+500", "Se suma lo que se repite a la hora de la última inspección.", " horas"),
        ("abc", "En Tripulación de Naves: ¿qué significa que una tarea del plan está vencida?", "Que la hora que fijaba el plan ya pasó sin haberse hecho", "Que la tarea se hizo antes de lo previsto", "Que el equipo ya no se usa", "Vencida significa que se pasó la hora del plan sin cumplirla."),
        ("=", "{F} ¿Cuántas horas faltan para la próxima inspección de filtros del generador 1?", "1700-1650", "Se resta las horas actuales a la hora de la próxima inspección.", " horas"),
        ("abc", "{F} ¿Qué equipo tiene una tarea vencida?", "La bomba de achique, porque su próxima inspección tocaba a las 1.050 horas y el horómetro marca 1.100", "El generador 1, porque su horómetro supera 1.200 horas", "El compresor, porque su horómetro supera 3.000 horas", "Solo la bomba tiene el horómetro por encima de la hora de su próxima tarea."),
        ("=", "{F} ¿Por cuántas horas está vencida la inspección del sello de la bomba de achique?", "1100-(800+250)", "Se calcula la hora de la próxima inspección y se resta a las horas actuales.", " horas"),
        ("=", "{F} ¿Cuántas horas faltan para el próximo cambio de aceite del compresor?", "(3000+1000)-3400", "Se calcula la hora del próximo cambio y se restan las horas actuales.", " horas"),
        ("abc", "{F} ¿En qué orden se informan las tres tareas de la ficha?", "Primero la bomba (vencida), luego el generador 1 (faltan 50 horas) y luego el compresor (faltan 600 horas)", "Primero el compresor, luego el generador 1 y al final la bomba", "Primero el generador 1, luego el compresor y la bomba no se informa", "Se informa primero lo vencido, luego lo próximo y al final lo lejano."),
        ("=", "{F} Si el generador 1 funciona 10 horas al día, ¿en cuántos días llegará a la hora de su próxima inspección?", "(1200+500-1650)//10", "Se calculan las horas que faltan y se dividen entre las horas diarias.", " días"),
        ("abc", "{F} La inspección de la bomba está vencida. ¿Qué corresponde a una persona en formación?", "Informarlo al oficial de máquinas y registrar la tarea como vencida, sin hacerla por su cuenta", "Hacer la inspección para ponerse al día", "Cambiar la hora del plan para que no figure vencida", "Informar es lo correcto; hacer la tarea o alterar el plan es inseguro e incorrecto."),
        ("abc", "{F} Un compañero dice que no hay que informar el generador 1 porque faltan «solo 50 horas». ¿Qué respuesta es correcta?", "Es falso: las tareas próximas se informan para programarlas con anticipación", "Es cierto, porque solo se informa lo vencido", "Es cierto, porque 50 horas es poco", "Informar con anticipación permite programar la tarea antes de que venza."),
        ("=", "{F} Si la bomba de achique se inspecciona recién a las 1.120 horas, ¿cuántas horas de retraso tuvo respecto de su plan?", "1120-(800+250)", "Se calcula la hora de la próxima inspección y se resta a la hora real.", " horas"),
        ("abc", "{F} ¿Cuál es el resumen correcto del estado de las tres tareas de la ficha?", "Una vencida, una que vence en 50 horas y una que vence en 600 horas", "Las tres están vencidas", "Ninguna está vencida ni próxima", "Cada tarea se compara con su propia hora de próxima inspección."),
    ],
    ctx=("abc", "En una visita de ejemplo, una persona a cargo te pide: «anota que la inspección de la bomba se hizo a las 1.050 horas, aunque no se hizo, para no tener tareas vencidas». ¿Qué respondes?", "Que no, porque se debe registrar lo que realmente ocurrió e informar el retraso", "Que sí, porque ella es responsable", "Que sí, pero lo anotas a lápiz", "Falsear un registro oculta un retraso y puede dejar un equipo sin revisión."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calcula la hora de la próxima tarea?", "Hora de la última tarea más lo que se repite", "La cuenta parte de la última tarea hecha."),
        ("¿Cómo se calculan las horas de retraso?", "Horas actuales menos la hora de la próxima tarea", "El retraso mide cuánto se pasó la hora del plan."),
        ("¿Qué se hace con una tarea vencida?", "Se registra e informa al oficial de máquinas", "La persona en formación no decide ni hace la tarea."),
    ],
    op=("Hoja de vida de ejemplo: el motor auxiliar marca 2.300 horas; última inspección a las 2.000 horas; se repite cada 250 horas. El compresor marca 900 horas; último cambio de aceite a las 500 horas; se repite cada 500 horas. Escribe (a) a qué hora toca la próxima tarea de cada equipo, (b) cuál equipo tiene una tarea vencida y por cuántas horas, (c) cuántas horas faltan para la tarea del otro equipo, (d) cómo informarías el estado al oficial.",
        "(a) Motor: 2.000 + 250 = 2.250 horas. Compresor: 500 + 500 = 1.000 horas. (b) El motor, vencida por 2.300 − 2.250 = 50 horas. (c) Al compresor le faltan 1.000 − 900 = 100 horas. (d) «Motor auxiliar: inspección vencida por 50 horas; compresor: cambio de aceite en 100 horas».",
        ["calcula la hora de la próxima tarea", "detecta la tarea vencida", "calcula las horas que faltan", "informa con prioridad"],
        ["hoja con las cuatro respuestas"],
        ["sumar a las horas actuales", "no informar lo próximo", "informar sin las horas exactas"],
        "Pregunta: «¿desde qué hora se cuenta cada tarea?». Si no responde, pídele que relea la primera parte de la explicación."),
    reinforce="Inventa una hoja de vida con dos equipos y calcula cuál tarea toca primero.",
    extend="Explica por qué conviene informar una tarea próxima antes de que venza.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (planilla de ejemplo; precios y cantidades de ejemplo). La inspección de filtros del generador 1 usa 2 filtros de $12.000 cada uno y se hace cada 500 horas. El generador funciona 6.000 horas al año. "
     "En la bodega hay 10 filtros de ese tipo. Cada inspección deja 8 litros de aceite usado, que se guardan en envases rotulados de 24 litros.")
build(
    O3, 4, F,
    use="Aprenderé a calcular cantidades, costos y residuos de un plan de mantenimiento, y a controlar el stock de repuestos.",
    prior=["Sé qué es una orden de trabajo y un repuesto.", "Sé multiplicar, dividir y restar números enteros.", "Sé qué es un residuo."],
    explain=[
        "Un plan de mantenimiento también se calcula en planilla. Las tareas por año se obtienen dividiendo las horas de funcionamiento del año entre cada cuántas horas se hace la tarea. Con eso se calcula cuántos repuestos se usan y cuánto cuestan. El stock es la cantidad de repuestos que hay en bodega y el stock mínimo es la cantidad bajo la cual hay que pedir más para no quedarse sin ellos.",
        "Los residuos también se calculan: los litros de aceite usado por tarea, multiplicados por las tareas del año, dan los litros que hay que guardar y entregar según la norma vigente. Un ejemplo con otra nave: una tarea cada 1.000 horas, con 3.000 horas al año, son 3 tareas; si cada tarea usa 3 repuestos de $5.000, se gastan 9 repuestos y $45.000. Todos los precios y cantidades de esta clase son de ejemplo.",
        f"Los cálculos sirven para planificar compras y registros; la tarea física la hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("stock", "cantidad de repuestos que hay en la bodega"), ("stock mínimo", "cantidad bajo la cual hay que pedir más repuestos"), ("costo anual", "gasto total de un año"), ("horas de funcionamiento al año", "horas que un equipo trabaja en un año"), ("rotulado", "con una etiqueta que indica su contenido")],
    worked=[
        ("Tareas por año", "Un equipo de ejemplo funciona 4.000 horas al año y su tarea se repite cada 1.000. ¿Cuántas tareas hay al año?", ["Se divide las horas del año entre lo que se repite.", "4.000 ÷ 1.000."], "4 tareas"),
        ("Costo de repuestos", "Cada tarea usa 3 repuestos de $5.000 de ejemplo. ¿Cuánto cuestan los repuestos de 4 tareas?", ["Los repuestos de las 4 tareas son 3 × 4 = 12.", "Se multiplica 12 × $5.000."], "$60.000"),
    ],
    mistakes=[("Calcular las tareas del año dividiendo por 12 meses en vez de por las horas que se repite.", "El plan se cuenta por horas de funcionamiento, no por meses.", "Divide las horas del año entre lo que se repite la tarea."),
              ("Olvidar el residuo que deja cada tarea.", "El residuo se acumula y debe guardarse y entregarse según la norma vigente.", "Calcula también los litros de residuo del año.")],
    T=[
        ("=", "{F} ¿Cuántas inspecciones de filtros se hacen al año?", "6000//500", "Se dividen las horas del año entre lo que se repite la inspección.", " inspecciones"),
        ("=", "{F} ¿Cuánto cuestan los filtros de una inspección?", "2*12000", "Se multiplican los filtros por su precio.", " pesos"),
        ("abc", "En Tripulación de Naves: ¿qué es el stock mínimo de un repuesto?", "La cantidad en bodega bajo la cual hay que pedir más", "La cantidad máxima que cabe en la bodega", "El precio más bajo del repuesto", "El stock mínimo es una señal de pedido; no es el máximo ni un precio."),
        ("=", "{F} ¿Cuántos filtros se usan al año?", "(6000//500)*2", "Se calculan las inspecciones del año y se multiplican por los filtros de cada una.", " filtros"),
        ("=", "{F} ¿Cuánto cuestan en el año los filtros de las inspecciones?", "(6000//500)*2*12000", "Se multiplican los filtros del año por su precio.", " pesos"),
        ("=", "{F} Con el stock de bodega, ¿cuántos filtros faltan comprar para cubrir el año?", "(6000//500)*2-10", "Se restan los filtros en bodega a los que se usan en el año.", " filtros"),
        ("=", "{F} ¿Cuántos litros de aceite usado se generan en el año?", "(6000//500)*8", "Se multiplican las inspecciones del año por los litros de cada una.", " litros"),
        ("=", "{F} ¿Cuántos envases de 24 litros se llenan con el aceite usado del año?", "((6000//500)*8)//24", "Se dividen los litros de residuo entre la capacidad de cada envase.", " envases"),
        ("abc", "{F} ¿Cuál es el mejor registro de la entrega de un envase de aceite usado?", "Fecha, tipo de residuo, litros y quién lo entrega", "Solo la palabra «residuo»", "Ningún registro, porque el envase ya está rotulado", "Un registro útil dice qué, cuánto, cuándo y quién; el rótulo del envase no lo reemplaza."),
        ("abc", "{F} El stock mínimo de ejemplo es de 4 filtros. ¿Con cuántos filtros en bodega se debe pedir más?", "Cuando queden 4 o menos", "Solo cuando queden 0", "Cuando queden 10", "El stock mínimo avisa antes de quedarse sin repuestos."),
        ("abc", "{F} Una persona propone alargar la inspección de 500 a 1.000 horas para ahorrar filtros. ¿Qué corresponde?", "No cambiarlo: la frecuencia la fija el plan según el manual y solo la modifica quien está autorizado", "Cambiarlo, porque se ahorra dinero", "Cambiarlo, si se anota en el registro", "La frecuencia es una decisión técnica que no se cambia por ahorro."),
        ("=", "{F} Si el precio de cada filtro subiera a $15.000, ¿cuántos pesos más costaría el consumo anual de filtros?", "(15000-12000)*(6000//500)*2", "Se multiplica el aumento de precio por los filtros que se usan en el año.", " pesos"),
        ("abc", "En Tripulación de Naves: ¿por qué conviene calcular los residuos del año antes de que se generen?", "Para tener envases y registros suficientes y entregarlos según la norma vigente", "Para que no se generen residuos", "Para verter el exceso al mar", "Calcular permite preparar envases y registros; no evita ni justifica verter residuos."),
    ],
    ctx=("abc", "Al revisar la planilla notas que el stock de filtros llegó a 0 y la inspección vence mañana. La persona a cargo dice: «usa los filtros usados de la bolsa, total sirven». ¿Qué corresponde?", "Informar al oficial de máquinas la falta de repuestos y no usar piezas desgastadas", "Usar los filtros usados, porque ella lo ordena", "Anotar que se cambiaron los filtros aunque no sea cierto", "Reutilizar piezas desgastadas o falsear el registro es inseguro; se informa la falta."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calculan las tareas del año?", "Horas del año divididas por lo que se repite la tarea", "El plan se cuenta por horas de funcionamiento."),
        ("¿Qué es el stock?", "La cantidad de repuestos que hay en bodega", "El stock es lo que hay disponible."),
        ("¿Qué se calcula además de los repuestos?", "Los residuos que deja cada tarea", "Los residuos también se guardan y se entregan según la norma vigente."),
    ],
    op=("Planilla de ejemplo: una tarea se hace cada 1.000 horas y usa 3 repuestos de $8.000 de ejemplo; deja 5 litros de residuo. El equipo funciona 5.000 horas al año y hay 6 repuestos en bodega. Escribe (a) cuántas tareas hay al año, (b) cuántos repuestos y cuánto cuestan, (c) cuántos repuestos faltan comprar, (d) cuántos litros de residuo se generan.",
        "(a) 5.000 ÷ 1.000 = 5 tareas. (b) 5 × 3 = 15 repuestos; 15 × $8.000 = $120.000. (c) 15 − 6 = 9 repuestos. (d) 5 × 5 = 25 litros.",
        ["calcula las tareas del año", "calcula repuestos y costo", "calcula los que faltan comprar", "calcula el residuo"],
        ["hoja con las cuatro respuestas"],
        ["dividir por los meses", "olvidar multiplicar por los repuestos de cada tarea", "no calcular el residuo"],
        "Pregunta: «¿cuántas tareas hay al año?». Si no responde, pídele que escriba la división de horas."),
    reinforce="Inventa una tarea de mantenimiento con su frecuencia y repuestos y calcula el costo anual.",
    extend="Explica qué ocurriría si el stock llegara a cero justo antes de una tarea del plan.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (opciones de ejemplo; costos de ejemplo). Una bomba funciona 2.000 horas al año. Opción 1, mantenimiento preventivo: una inspección cada 500 horas, de $40.000 cada una. "
     "Opción 2, esperar la falla: se estima 1 falla cada 1.000 horas; cada reparación cuesta $300.000 y deja la bomba fuera de servicio. Criterio obligatorio: el equipo no debe quedar fuera de servicio por una falla evitable. Criterio de elección: menor costo anual.")
build(
    O3, 5, F,
    use="Aprenderé a comparar mantenimiento preventivo y correctivo con criterios, y a verificar la calidad de un registro de mantenimiento.",
    prior=["Sé la diferencia entre preventivo y correctivo.", "Sé calcular tareas y costos anuales.", "Sé multiplicar números enteros."],
    explain=[
        "Comparar opciones de mantenimiento es evaluar cada una con los mismos criterios. Hay criterios obligatorios, como que el equipo no quede fuera de servicio por una falla evitable, y criterios de elección, como el menor costo anual. Primero se aplican los obligatorios; las opciones que no los cumplen se descartan, y entre las que quedan se elige la de menor costo. El costo anual de cada opción se calcula multiplicando el número de tareas o fallas del año por su costo.",
        "Verificar la calidad de un registro es comprobar que está completo: fecha, equipo, tarea, horas del horómetro, responsable y repuestos usados. Un ejemplo con otra nave: una orden con fecha, equipo y tarea, pero sin responsable ni horas, está incompleta y no permite saber quién la hizo. Un registro incompleto se devuelve a quien lo emitió para que lo complete; no se completa inventando datos.",
        f"Elegir entre opciones es una decisión del jefe de máquinas; la persona en formación calcula, compara e informa. {EMER} {AVISO}",
    ],
    vocab=[("opción", "una de las alternativas entre las que se elige"), ("falla evitable", "falla que un buen plan preventivo habría podido impedir"), ("fuera de servicio", "equipo que no puede usarse"), ("registro completo", "registro con fecha, equipo, tarea, horas, responsable y repuestos"), ("costo anual", "gasto total de un año")],
    worked=[
        ("Costo de una opción", "Una opción de ejemplo hace 3 inspecciones al año de $20.000 cada una. ¿Cuánto cuesta al año?", ["Se multiplican las inspecciones por su costo.", "3 × $20.000."], "$60.000"),
        ("Registro incompleto", "Una orden de ejemplo trae fecha, equipo y tarea, pero no responsable. ¿Está completa?", ["Un registro completo necesita también el responsable.", "Falta ese dato."], "No, falta el responsable"),
    ],
    mistakes=[("Elegir la opción más barata sin revisar el criterio obligatorio.", "Una opción que deja el equipo fuera de servicio por una falla evitable se descarta aunque cueste menos.", "Aplica primero los criterios obligatorios."),
              ("Completar un registro con datos inventados para que quede completo.", "Un dato inventado falsea el registro.", "Devuelve el registro a quien lo emitió para que lo complete.")],
    T=[
        ("=", "{F} ¿Cuántas inspecciones preventivas se hacen al año en la opción 1?", "2000//500", "Se dividen las horas del año entre lo que se repite la inspección.", " inspecciones"),
        ("=", "{F} ¿Cuánto cuesta al año la opción 1?", "(2000//500)*40000", "Se multiplican las inspecciones del año por el costo de cada una.", " pesos"),
        ("abc", "{F} ¿Cumple la opción 2 con el criterio obligatorio?", "No, porque cada falla deja la bomba fuera de servicio", "Sí, porque la reparación tiene un costo conocido y planificado", "Sí, porque la bomba se repara", "Esperar la falla deja el equipo fuera de servicio por una falla evitable."),
        ("=", "{F} ¿Cuántas fallas se estiman al año en la opción 2?", "2000//1000", "Se dividen las horas del año entre las horas por falla.", " fallas"),
        ("=", "{F} ¿Cuánto cuesta al año la opción 2?", "(2000//1000)*300000", "Se multiplican las fallas del año por el costo de cada reparación.", " pesos"),
        ("abc", "{F} ¿Qué opción se elige según los criterios de la ficha?", "La opción 1, porque cumple el criterio obligatorio y cuesta menos al año", "La opción 2, porque cada reparación no tiene inspecciones", "Ninguna, porque las dos tienen costos", "La opción 1 cumple el obligatorio y su costo anual es menor."),
        ("=", "{F} ¿Cuántos pesos ahorra al año la opción 1 respecto de la opción 2?", "(2000//1000)*300000-(2000//500)*40000", "Se resta el costo anual de la opción 1 al de la opción 2.", " pesos"),
        ("=", "{F} Si cada inspección de la opción 1 costara $120.000, ¿cuánto costaría esa opción al año?", "(2000//500)*120000", "Se multiplican las inspecciones del año por el nuevo costo.", " pesos"),
        ("abc", "{F} Con el costo de $120.000 por inspección, ¿qué opción sigue siendo la preferida?", "La opción 1, porque cumple el obligatorio y cuesta menos que la opción 2", "La opción 2, porque ahora es la más barata", "Ninguna, porque cambió el costo", "480.000 pesos de la opción 1 siguen siendo menos que 600.000 de la opción 2."),
        ("abc", "{F} Una orden de trabajo de ejemplo trae fecha, equipo, tarea y horas, pero sin firma ni responsable. ¿Qué corresponde?", "Devolverla a quien la emitió para que la complete", "Completarla con el nombre de quien tú creas que la hizo", "Archivarla sin cambios porque tiene fecha", "Un registro incompleto se completa por su emisor, sin inventar datos."),
        ("abc", "En Tripulación de Naves: ¿por qué un buen plan preventivo reduce también riesgos de seguridad?", "Porque evita fallas inesperadas del equipo mientras la nave opera", "Porque elimina la necesidad de personal autorizado", "Porque hace innecesarios los registros", "Las fallas inesperadas pueden causar accidentes; el plan las anticipa."),
        ("=", "{F} Si de las 4 inspecciones del año solo se cumplen 3, ¿qué porcentaje del plan se cumplió?", "3*100//4", "Se calcula la parte cumplida sobre el total y se pasa a porcentaje.", " %"),
        ("abc", "{F} Un compañero dice: «con el porcentaje cumplido ya basta, no hace falta saber cuál inspección faltó». ¿Qué respuesta es correcta?", "Es falso: hay que registrar cuál quedó pendiente y por qué", "Es cierto, porque el porcentaje resume todo", "Es cierto, si el porcentaje supera 50 %", "Un porcentaje no dice qué tarea quedó pendiente ni su causa."),
    ],
    ctx=("abc", "El jefe de máquinas de ejemplo te pide ayuda para decidir entre dos opciones de mantenimiento. Una cuesta menos pero deja al equipo fuera de servicio por fallas evitables. ¿Qué le presentas?", "Los costos de ambas y que la más barata no cumple el criterio obligatorio, para que él decida", "Solo el costo más bajo, para que decida rápido", "Solo la opción que cumple, sin mencionar la otra", "Una buena comparación muestra los datos de ambas y el criterio que decide."),
    sc=[
        ("En Tripulación de Naves: ¿qué se aplica primero al comparar opciones?", "Los criterios obligatorios", "Las opciones que no los cumplen se descartan."),
        ("¿Qué datos tiene un registro completo?", "Fecha, equipo, tarea, horas, responsable y repuestos", "Con esos datos se sabe qué se hizo y quién lo hizo."),
        ("¿Quién decide la opción de mantenimiento?", "El jefe de máquinas", "La persona en formación calcula e informa."),
    ],
    op=("Opciones de ejemplo para un ventilador que funciona 3.000 horas al año. Opción A: inspección preventiva cada 1.000 horas, $25.000 cada una. Opción B: esperar la falla, 1 falla cada 1.500 horas, $150.000 por reparación y el ventilador queda fuera de servicio. Criterio obligatorio: no quedar fuera de servicio por una falla evitable. Escribe (a) el costo anual de cada opción, (b) cuál cumple el criterio obligatorio, (c) cuál se elige y cuánto ahorra, (d) qué datos debe tener la orden de trabajo de la opción elegida.",
        "(a) A: 3 inspecciones × $25.000 = $75.000. B: 2 fallas × $150.000 = $300.000. (b) La opción A. (c) La opción A, que ahorra $225.000 al año. (d) Fecha, equipo, tarea, horas del horómetro, responsable y repuestos usados.",
        ["calcula el costo anual de cada opción", "aplica el criterio obligatorio", "elige y calcula el ahorro", "indica los datos de la orden de trabajo"],
        ["hoja con las cuatro respuestas"],
        ["elegir solo por costo", "olvidar contar las fallas del año", "no incluir al responsable"],
        "Pregunta: «¿cuántas inspecciones y cuántas fallas hay al año?». Si no responde, pídele que escriba las dos divisiones."),
    reinforce="Inventa dos opciones de mantenimiento con costos y escribe un criterio obligatorio para compararlas.",
    extend="Explica por qué un registro completo ayuda a comparar opciones de mantenimiento.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En la cubierta de la «Nave Demo» hay 2 grúas, 1 pluma, 2 huinches y 1 cabrestante. La nave aplica un sistema de gestión de seguridad (ISM). "
     "Peligros anotados: cargas suspendidas, cabos y cables tensos que pueden soltarse con fuerza, partes giratorias, cubierta mojada y mal tiempo.")
build(
    O4, 1, F,
    use="Aprenderé qué son los equipos de maniobra, qué peligros tienen, qué es un sistema de gestión de la seguridad y por qué solo personal autorizado los opera.",
    prior=["Sé qué es la cubierta de una nave.", "Sé qué es la jerarquía de controles.", "Sé sumar y multiplicar números enteros."],
    explain=[
        "Los equipos de maniobra son los equipos de cubierta que mueven cargas y cabos, como las grúas, las plumas, los huinches y los cabrestantes. Sus peligros son las cargas suspendidas, los cabos y cables tensos que pueden soltarse con fuerza, las partes giratorias y la cubierta mojada. Se previenen con la jerarquía de controles: barandas y zonas protegidas, reglas, señalética, permisos y, al final, el EPP. Este cuaderno no enseña a operar estos equipos.",
        "El sistema de gestión de la seguridad (ISM, por sus siglas internacionales) es el conjunto de políticas, responsabilidades, procedimientos y registros con que una nave gestiona la seguridad. Incluye una persona designada como responsable, registros de inspecciones y un registro de no conformidades, que son los desvíos detectados respecto de lo exigido. Cuando hay mal tiempo, decidir si se trabaja en cubierta corresponde al oficial a cargo, según la norma vigente.",
        f"Un ejemplo con otra nave: una grúa con un cable deshilachado se registra como no conformidad y se informa al responsable. {EMER} {AVISO}",
    ],
    vocab=[("equipo de maniobra", "equipo de cubierta que mueve cargas o cabos"), ("grúa", "equipo que eleva y desplaza cargas"), ("huinche", "equipo que enrolla un cable o cabo para elevar o arrastrar"), ("cabrestante", "equipo de eje vertical que recoge cabos"), ("carga suspendida", "carga que cuelga de un equipo de izado"), ("ISM", "sistema de gestión de la seguridad de la nave"), ("no conformidad", "desvío detectado respecto de lo exigido")],
    worked=[
        ("Peligro y riesgo", "En una nave de ejemplo un cabo tenso pasa junto a un lugar de paso. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el cabo tenso, porque puede soltarse con fuerza.", "El riesgo es que golpee a una persona que pasa."], "Peligro: el cabo tenso; riesgo: que golpee a una persona"),
        ("Registrar una no conformidad", "Una nave de ejemplo detecta que una baranda de la cubierta está suelta. ¿Cómo se registra?", ["La baranda suelta es un desvío respecto de lo exigido.", "Se anota como no conformidad y se informa al responsable."], "Como no conformidad, informada al responsable"),
    ],
    mistakes=[("Creer que conocer los equipos permite operarlos.", "Operar equipos de maniobra exige formación, autorización y norma vigente.", "Aprende el concepto y deja la operación a personal autorizado."),
              ("Creer que el mal tiempo lo decide cualquier tripulante.", "La decisión de trabajar en cubierta con mal tiempo es del oficial a cargo.", "Informa lo que observas y espera la decisión del oficial.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué son los equipos de maniobra?", "Equipos de cubierta que mueven cargas y cabos", "Equipos del área de máquinas que producen electricidad", "Instrumentos que miden la velocidad de la nave", "Los equipos de maniobra mueven cargas y cabos; los generadores y los instrumentos son otra cosa."),
        ("abc", "En Tripulación de Naves: ¿qué es el sistema ISM de una nave?", "Un sistema de gestión de la seguridad con políticas, responsables y registros", "Un instrumento para medir el rumbo", "Un tipo de grúa de cubierta", "El ISM es un sistema de gestión, no un equipo ni un instrumento."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a una carga suspendida?", "Que la carga caiga o golpee a una persona", "Que la cubierta se vea más desordenada", "Que el equipo consuma más electricidad", "El riesgo es un daño a las personas; el orden y el consumo no lo son."),
        ("=", "{F} ¿Cuántos equipos de maniobra hay en la cubierta de la ficha?", "2+1+2+1", "Se suman las grúas, la pluma, los huinches y el cabrestante.", " equipos"),
        ("abc", "{F} Una baranda fija que impide entrar a la zona bajo una carga suspendida es un control de:", "Ingeniería, porque cambia físicamente el lugar", "Administrativo, porque ordena una conducta", "EPP, porque protege a cada persona", "La baranda es una barrera física y no depende de que cada persona la recuerde."),
        ("abc", "{F} Hay mal tiempo en la cubierta. ¿Quién decide si se trabaja con los equipos?", "El oficial a cargo, según la norma vigente", "El tripulante en formación", "Cualquier persona que esté en cubierta", "La decisión corresponde al oficial a cargo, no a quien está en formación."),
        ("=", "{F} Cada equipo de la ficha tiene 3 registros de inspección al mes. ¿Cuántos registros hay en un mes?", "(2+1+2+1)*3", "Se suman los equipos de la ficha y se multiplican por los registros de cada uno.", " registros"),
        ("=", "{F} ¿Cuántos registros de inspección hay en el año, con los 3 mensuales de cada equipo?", "(2+1+2+1)*3*12", "Se calculan los registros del mes y se multiplican por los 12 meses.", " registros"),
        ("abc", "{F} Un cabo tenso pasa junto al lugar donde una persona suele detenerse. ¿Cuál medida es de nivel más efectivo?", "Cambiar la ruta del cabo para que no pase por ese lugar", "Colocar un letrero que avise «cabo tenso»", "Entregar un casco a la persona", "Cambiar la ruta quita el peligro del lugar; el letrero informa y el casco es EPP."),
        ("abc", "Durante una visita de ejemplo, una carga suspendida se balancea de forma peligrosa cerca de ti. ¿Qué corresponde?", "Alejarte de la zona de riesgo, dar la alarma y avisar a un adulto responsable y a emergencias", "Acercarte para sujetar la carga con las manos", "Pasar por debajo rápido para salir del lugar", "Acercarse o pasar bajo la carga es peligroso; se da la alarma y se avisa."),
        ("abc", "{F} Un compañero dice: «si ya conozco la grúa, puedo operarla cuando el oficial no mira». ¿Qué respuesta es correcta?", "Es falso: operar exige formación, autorización y norma vigente", "Es cierto, si conoce el equipo", "Es cierto, si la carga es liviana", "Conocer un equipo no autoriza a operarlo."),
        ("=", "{F} Si cada equipo exigiera 2 personas autorizadas y todos operaran a la vez en un plan de papel, ¿cuántas personas se necesitarían?", "(2+1+2+1)*2", "Se suman los equipos de la ficha y se multiplican por las personas de cada equipo.", " personas"),
        ("abc", "{F} Una persona nota un cable deshilachado en un equipo. ¿Qué corresponde a una persona en formación?", "Informarlo al responsable para que se registre como no conformidad, sin usar el equipo", "Seguir usando el equipo con cuidado", "Cortar la parte dañada del cable", "Un cable dañado se informa y se registra; no se usa ni se interviene sin autorización."),
    ],
    ctx=("abc", "Un conocido que trabaja en una nave te invita a cubierta para «aprender a manejar la grúa» en un día de viento fuerte. ¿Qué respondes?", "Que no, porque exige instructor autorizado, norma vigente y elementos de protección, y que lo consultarás con un adulto responsable", "Que sí, si él supervisa", "Que sí, si te presta un casco y un chaleco", "Ni la supervisión informal ni un casco reemplazan la autorización y la formación."),
    sc=[
        ("En Tripulación de Naves: ¿qué es una no conformidad?", "Un desvío detectado respecto de lo exigido", "La no conformidad se registra e informa al responsable."),
        ("¿Quién decide si se trabaja en cubierta con mal tiempo?", "El oficial a cargo", "La decisión no la toma una persona en formación."),
        ("¿Qué es una carga suspendida?", "Una carga que cuelga de un equipo de izado", "La carga suspendida puede caer o golpear a alguien."),
    ],
    op=("En la cubierta de la «Nave Ejemplo» (caso de ejemplo) hay un cabrestante con un cabo tenso que cruza un pasillo que el personal usa para ir a proa, y la cubierta está mojada. Escribe (a) los dos peligros, (b) el riesgo de cada uno, (c) un control de ingeniería para el pasillo, (d) qué hace una persona en formación al ver esa situación.",
        "(a) El cabo tenso que cruza el pasillo y la cubierta mojada. (b) Que el cabo golpee a una persona; que alguien resbale. (c) Una baranda o una ruta alternativa que impida cruzar la zona del cabo. (d) No se acerca a la zona de riesgo, avisa al oficial a cargo y al responsable para que lo registre como no conformidad.",
        ["identifica los dos peligros", "señala el riesgo de cada uno", "propone un control de ingeniería", "indica que avisa y no interviene"],
        ["hoja con las cuatro respuestas"],
        ["confundir peligro con riesgo", "proponer solo EPP", "proponer que la persona en formación mueva el cabo"],
        "Pregunta: «¿qué puede pasar y a quién?». Si no responde, pídele que relea los peligros de la ficha."),
    reinforce="Haz una lista de los equipos de maniobra de la ficha y escribe qué peligro principal tiene cada uno.",
    extend="Explica con un ejemplo por qué registrar las no conformidades ayuda a prevenir accidentes.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (equipos de ejemplo, inventados). G1: grúa eléctrica, capacidad de placa 20 t. P1: pluma con un huinche de accionamiento manual, capacidad de placa 15 t. H1: huinche eléctrico, capacidad de placa 5 t. "
     "C1: cabrestante neumático, capacidad de placa 10 t. Un bulto de ejemplo lleva una etiqueta en forma de rombo con una llama dibujada.")
build(
    O4, 2, F,
    use="Aprenderé a distinguir los equipos de maniobra por su función y su tipo de accionamiento, a leer la capacidad de placa y a reconocer la etiqueta de una mercancía peligrosa.",
    prior=["Sé qué son los equipos de maniobra.", "Sé qué es el ISM.", "Sé sumar y restar números enteros."],
    explain=[
        "Cada equipo de maniobra tiene una función. El huinche enrolla un cable o un cabo para elevar o arrastrar. El cabrestante, de eje vertical, recoge cabos. La grúa eleva y desplaza cargas, y la pluma es un brazo que sostiene el cable de izado. Según cómo se accionan, pueden ser manuales (con fuerza de personas), neumáticos (con aire a presión) o eléctricos (con un motor eléctrico). La capacidad de placa es la carga máxima que el fabricante indica en la placa del equipo y no se debe sobrepasar.",
        "Las mercancías peligrosas son sustancias que pueden dañar a las personas, a la nave o al medio ambiente. Se reconocen por etiquetas en forma de rombo, con un dibujo y un color que indican el tipo de peligro, como una llama para lo inflamable. Además, cada producto tiene su hoja de datos de seguridad, que explica sus peligros. Solo personal capacitado las maneja, según la norma vigente. Un ejemplo con otra nave: un rombo con una calavera avisa de una sustancia tóxica.",
        f"Las señales y los pictogramas del equipo se respetan siempre; si algo no se entiende, se pregunta al oficial. {EMER} {AVISO}",
    ],
    vocab=[("huinche", "equipo que enrolla un cable o cabo para elevar o arrastrar"), ("cabrestante", "equipo de eje vertical que recoge cabos"), ("pluma", "brazo que sostiene el cable de izado"), ("accionamiento", "forma en que se mueve un equipo: manual, neumático o eléctrico"), ("capacidad de placa", "carga máxima indicada por el fabricante en la placa del equipo"), ("mercancía peligrosa", "sustancia que puede dañar personas, la nave o el ambiente"), ("hoja de datos de seguridad", "documento que explica los peligros de un producto")],
    worked=[
        ("Tipo de accionamiento", "Un equipo de ejemplo funciona con un motor eléctrico. ¿Cuál es su accionamiento?", ["El accionamiento es la forma en que se mueve.", "Con motor eléctrico es eléctrico."], "Eléctrico"),
        ("Leer una placa", "La placa de un huinche de ejemplo dice 8 t. ¿Qué significa?", ["La placa trae la capacidad máxima.", "Es la carga que no se debe sobrepasar."], "Su capacidad es de 8 toneladas y no se debe sobrepasar"),
    ],
    mistakes=[("Creer que un equipo manual no necesita autorización porque no tiene motor.", "Un equipo manual también puede causar daño y exige formación.", "Todo equipo de maniobra lo opera personal autorizado."),
              ("Interpretar una etiqueta de rombo sin mirar su dibujo y su color.", "El dibujo y el color indican el tipo de peligro.", "Lee el dibujo, el color y la hoja de datos de seguridad.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué hace un huinche?", "Enrolla un cable o cabo para elevar o arrastrar", "Produce electricidad para la nave", "Mide la profundidad bajo la nave", "El huinche enrolla cables; la electricidad la produce un generador y la profundidad la mide una ecosonda."),
        ("abc", "En Tripulación de Naves: ¿qué es la capacidad de placa de un equipo?", "La carga máxima indicada por el fabricante en la placa", "La carga mínima para que funcione", "El peso del equipo vacío", "La capacidad de placa es el máximo, no el mínimo ni el peso del equipo."),
        ("abc", "{F} ¿Cuál equipo de la ficha tiene accionamiento neumático?", "El cabrestante C1", "La grúa G1", "El huinche H1", "Según la ficha, C1 es neumático; G1 y H1 son eléctricos."),
        ("abc", "{F} ¿Qué equipo de la ficha tiene la mayor capacidad de placa?", "La grúa G1, con 20 t", "La pluma P1, con 15 t", "El cabrestante C1, con 10 t", "La capacidad mayor es la de G1: 20 t."),
        ("abc", "{F} ¿Qué indica la etiqueta en forma de rombo con una llama?", "Que la mercancía puede inflamarse", "Que la mercancía es muy pesada", "Que la mercancía es frágil", "La llama en una etiqueta de rombo indica peligro de inflamabilidad."),
        ("=", "{F} ¿Cuántas toneladas más de capacidad tiene la grúa G1 que el huinche H1?", "20-5", "Se resta la capacidad del huinche a la de la grúa.", " t"),
        ("=", "{F} ¿Cuál es la capacidad total, en toneladas, de los equipos de accionamiento eléctrico de la ficha?", "20+5", "Se suman las capacidades de G1 y H1, que son los eléctricos.", " t"),
        ("abc", "{F} ¿Cuál equipo de la ficha es de accionamiento manual?", "El huinche de la pluma P1", "El huinche H1", "El cabrestante C1", "La ficha dice que el huinche de la pluma P1 se acciona manualmente."),
        ("abc", "{F} ¿Para qué sirve la hoja de datos de seguridad de un producto?", "Para conocer sus peligros", "Para saber su precio", "Para conocer el peso de cada bulto", "La hoja de datos explica los peligros del producto."),
        ("abc", "{F} Una carga de 6 t se quiere asociar al huinche H1 en la planilla. ¿Qué dice la placa?", "Que no corresponde, porque supera su capacidad de 5 t", "Que corresponde, porque 6 t es cercano a 5 t", "Que corresponde, porque el huinche es eléctrico", "La carga supera la capacidad de placa de 5 t, por lo tanto no corresponde."),
        ("abc", "{F} Un compañero dice que el huinche manual de la pluma no necesita autorización porque no tiene motor. ¿Qué respuesta es correcta?", "Es falso: todo equipo de maniobra lo opera personal autorizado", "Es cierto, porque solo los eléctricos son peligrosos", "Es cierto, si la carga es pequeña", "La falta de motor no elimina el peligro ni la necesidad de autorización."),
        ("=", "{F} Si se agrega un cabrestante neumático de 8 t, ¿cuál sería la capacidad total de los equipos neumáticos?", "10+8", "Se suma la capacidad del cabrestante de la ficha a la del nuevo.", " t"),
        ("abc", "{F} El rombo del bulto tiene la etiqueta ilegible. ¿Qué corresponde?", "No manipular el bulto e informar al responsable para identificar su contenido", "Suponer que es inflamable y manipularlo con cuidado", "Rasparlo para ver si es una sustancia común", "Una etiqueta ilegible impide conocer el peligro; se informa y no se manipula."),
    ],
    ctx=("abc", "En una visita de ejemplo ves un huinche manual y alguien te dice: «pruébalo, que no tiene motor y no pasa nada». ¿Qué respondes?", "Que no, porque cualquier equipo de maniobra exige autorización y formación", "Que sí, si lo haces despacio", "Que sí, si hay alguien cerca", "Que sea manual no lo vuelve seguro; la autorización sigue siendo necesaria."),
    sc=[
        ("En Tripulación de Naves: ¿qué es un cabrestante?", "Un equipo de eje vertical que recoge cabos", "El cabrestante recoge cabos; el huinche enrolla cables."),
        ("¿Qué significa una etiqueta en forma de rombo?", "Que la mercancía es peligrosa; el dibujo indica el tipo de peligro", "El rombo identifica mercancías peligrosas y su dibujo indica el tipo."),
        ("¿Qué tipos de accionamiento tienen los equipos de maniobra?", "Manual, neumático y eléctrico", "Son las tres formas de mover un equipo que nombra el plan."),
    ],
    op=("Equipos de ejemplo: E1, grúa eléctrica de 12 t; E2, huinche manual de 3 t; E3, cabrestante neumático de 6 t. Un bulto lleva un rombo con una calavera dibujada. Escribe (a) el accionamiento de cada equipo, (b) cuál tiene mayor capacidad y por cuánto supera a E2, (c) qué indica el rombo y qué documento se consulta, (d) por qué E2 también exige autorización.",
        "(a) E1 eléctrico, E2 manual, E3 neumático. (b) E1, con 12 t; supera a E2 por 9 t. (c) Que la sustancia es tóxica; se consulta su hoja de datos de seguridad. (d) Porque un equipo manual también puede causar daño y todo equipo de maniobra lo opera personal autorizado.",
        ["identifica el accionamiento", "compara las capacidades", "interpreta la etiqueta y el documento", "explica la autorización"],
        ["hoja con las cuatro respuestas"],
        ["confundir manual con neumático", "olvidar restar", "decir que el equipo manual no necesita autorización"],
        "Pregunta: «¿cómo se mueve cada equipo?». Si no responde, pídele que relea la primera parte de la explicación."),
    reinforce="Haz una tabla con cuatro equipos de maniobra, su función y su tipo de accionamiento.",
    extend="Explica por qué la capacidad de placa no debe sobrepasarse aunque el equipo parezca resistente.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (planilla de verificación documental, de ejemplo). Equipos de la «Nave Ejemplo»: grúa E1, capacidad de placa 20 t; pluma E2, 15 t; huinche E3, 5 t. "
     "Regla de la planilla de ejemplo: la carga no debe superar el 80 % de la capacidad de placa. Cargas de ejemplo para registrar: carga X, 3 t; carga Y, 9 t; carga Z, 14 t. (Valores de ejemplo, no reales.)")
build(
    O4, 3, F,
    use="Aprenderé a verificar en una planilla si una carga cumple con la capacidad de placa de un equipo y la regla de ejemplo, y a informar los resultados.",
    prior=["Sé qué es la capacidad de placa.", "Sé calcular un porcentaje simple.", "Sé comparar números enteros."],
    explain=[
        "Una planilla de verificación compara cada carga con la capacidad de placa del equipo asociado. Para eso se calcula el límite de la regla: límite = capacidad de placa × porcentaje de la regla ÷ 100. Una carga cumple si es menor o igual que el límite y no cumple si lo supera. La verificación se hace antes y en papel; no autoriza a mover ninguna carga.",
        "Un ejemplo con otros valores: un equipo de capacidad 10 t con una regla de ejemplo del 70 % tiene un límite de 7 t; una carga de 6 t cumple y una de 8 t no cumple. Cuando una carga no cumple, la persona en formación informa al oficial a cargo, que decide otro equipo o dividir la carga. Los porcentajes de esta clase son solo de ejemplo; los valores reales los fija la norma vigente y el fabricante.",
        f"La planilla se completa con datos reales de la placa, nunca con suposiciones. {EMER} {AVISO}",
    ],
    vocab=[("planilla de verificación", "hoja que compara cada carga con la capacidad de un equipo"), ("límite de la regla", "capacidad de placa por el porcentaje de la regla, dividido por 100"), ("cumple", "carga menor o igual que el límite"), ("no cumple", "carga mayor que el límite"), ("carga", "peso que se pretende mover con un equipo")],
    worked=[
        ("Calcular un límite", "Un equipo de ejemplo tiene capacidad de placa de 30 t y la regla es 60 %. ¿Cuál es el límite?", ["Límite = capacidad × porcentaje ÷ 100.", "30 × 60 ÷ 100."], "18 t"),
        ("Verificar una carga", "Una carga de ejemplo de 20 t se asocia a ese equipo. ¿Cumple?", ["El límite es 18 t.", "20 t supera 18 t."], "No cumple"),
    ],
    mistakes=[("Comparar la carga con la capacidad de placa completa y no con el límite de la regla.", "La regla fija un límite menor que la capacidad de placa.", "Calcula primero el límite y compara con él."),
              ("Aceptar una carga que supera el límite «por poco».", "Un exceso, por pequeño que sea, no cumple la regla.", "Informa al oficial y propone otra opción en la planilla.")],
    T=[
        ("=", "{F} ¿Cuál es el límite de la regla, en toneladas, para la grúa E1?", "20*80//100", "Se calcula el 80 % de la capacidad de placa de E1.", " t"),
        ("=", "{F} ¿Cuál es el límite de la regla, en toneladas, para la pluma E2?", "15*80//100", "Se calcula el 80 % de la capacidad de placa de E2.", " t"),
        ("abc", "{F} ¿Cumple la carga X con el huinche E3, cuyo límite es 4 t?", "Sí, porque 3 t no supera 4 t", "No, porque 3 t es cercano a 5 t", "No, porque el huinche es el equipo más pequeño", "La carga de 3 t es menor que el límite de 4 t."),
        ("abc", "{F} ¿Cumple la carga Y con el huinche E3?", "No, porque 9 t supera el límite de 4 t", "Sí, porque 9 t es menor que 15 t", "Sí, porque el huinche es eléctrico", "La carga de 9 t supera el límite del huinche, que es 4 t."),
        ("abc", "{F} ¿Cumple la carga Z con la pluma E2?", "No, porque 14 t supera el límite de 12 t", "Sí, porque 14 t es menor que 15 t", "Sí, porque la pluma tiene mayor capacidad que el huinche", "La regla compara con el límite de 12 t y no con la capacidad de placa de 15 t."),
        ("abc", "{F} ¿Cumple la carga Z con la grúa E1?", "Sí, porque 14 t no supera el límite de 16 t", "No, porque 14 t es cercano a 20 t", "No, porque es la carga más pesada", "Con un límite de 16 t la carga de 14 t cumple."),
        ("=", "{F} ¿Cuántas toneladas de margen queda entre la carga Z y el límite de la grúa E1?", "16-14", "Se resta la carga al límite de la grúa.", " t"),
        ("=", "{F} ¿Cuál es el límite, en toneladas, del huinche E3?", "5*80//100", "Se calcula el 80 % de la capacidad de placa del huinche.", " t"),
        ("abc", "{F} ¿Cuántas de las tres cargas cumplen con la grúa E1?", "Las tres, porque todas son menores o iguales que 16 t", "Solo dos, porque Z se acerca al límite", "Solo una, porque X es la más liviana", "Las cargas de 3, 9 y 14 t son menores o iguales que 16 t."),
        ("abc", "{F} ¿Cuál es el informe correcto para la carga Y con el huinche E3?", "«La carga Y de 9 t no cumple con el huinche E3, límite 4 t; se informa al oficial»", "«La carga Y cumple porque el huinche es eléctrico»", "«Se anotó 4 t para la carga Y para que cumpla»", "El informe declara el resultado con datos y no altera la carga."),
        ("abc", "{F} Un compañero dice que «14 t es casi 12 t, así que la pluma E2 sirve para la carga Z». ¿Qué respuesta es correcta?", "Es falso: un exceso, aunque sea pequeño, no cumple la regla", "Es cierto, porque la diferencia es de solo 2 t", "Es cierto, porque la placa dice 15 t", "La regla fija un límite que no se sobrepasa, por poco que sea."),
        ("=", "{F} ¿Qué porcentaje de la capacidad de placa de la grúa E1 representa la carga Z?", "14*100//20", "Se divide la carga entre la capacidad de placa y se multiplica por 100.", " %"),
        ("abc", "{F} El oficial pide listar las cargas que cumplen con la pluma E2. ¿Cuáles son?", "X y Y, porque 3 t y 9 t no superan 12 t", "Solo X, porque Y es mayor que 5 t", "Las tres, porque la pluma tiene capacidad de 15 t", "Con un límite de 12 t cumplen X y Y; Z lo supera."),
    ],
    ctx=("abc", "En la planilla de ejemplo, una persona te dice: «la carga Y no cumple con E3, pero anótala como que sí, el oficial no se va a dar cuenta». ¿Qué respondes?", "Que se debe registrar el resultado real e informar al oficial", "Que anotas «cumple» para evitar problemas", "Que anotas «cumple» y avisas después", "Falsear la planilla oculta un incumplimiento que puede causar un accidente."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calcula el límite de la regla?", "Capacidad de placa por el porcentaje de la regla, dividido por 100", "Así se obtiene el máximo que permite la regla de la planilla."),
        ("¿Cuándo una carga cumple?", "Cuando es menor o igual que el límite", "Cumple si no supera el límite."),
        ("¿Qué se hace si una carga no cumple?", "Se informa al oficial a cargo", "El oficial decide otro equipo o dividir la carga."),
    ],
    op=("Planilla de ejemplo: equipo F1, capacidad de placa 30 t; equipo F2, 10 t; regla de ejemplo del 70 %. Cargas de ejemplo: M, 6 t; N, 15 t; O, 21 t. Escribe (a) el límite de cada equipo, (b) cuáles cargas cumplen con F1, (c) si la carga M cumple con F2, (d) cómo informarías la carga N con F2.",
        "(a) F1: 30 × 70 ÷ 100 = 21 t. F2: 10 × 70 ÷ 100 = 7 t. (b) M (6 t), N (15 t) y O (21 t), porque ninguna supera 21 t. (c) Sí: 6 t es menor que 7 t, por lo tanto cumple. (d) «La carga N de 15 t no cumple con F2, límite 7 t; se informa al oficial».",
        ["calcula el límite de cada equipo", "verifica las cargas con F1", "verifica la carga M con F2", "redacta el informe de la carga N"],
        ["hoja con las cuatro respuestas"],
        ["comparar con la capacidad de placa", "no calcular el porcentaje", "no informar el incumplimiento"],
        "Pregunta: «¿cuál es el límite de cada equipo?». Si no responde, pídele que calcule el porcentaje primero."),
    reinforce="Inventa tres cargas y dos equipos y completa una planilla de verificación.",
    extend="Explica por qué la regla fija un límite menor que la capacidad de placa.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (planilla de ejemplo; valores de ejemplo). Se deben mover, en un plan de papel, 48 t de carga repartidas en bultos de 12 t con una grúa de capacidad de placa de 20 t. Regla de ejemplo: la carga de cada izada no debe superar el 80 % de la capacidad de placa. "
     "Cada izada dura 6 minutos en el plan. El registro ISM del mes tiene 9 no conformidades, de las cuales 6 están cerradas.")
build(
    O4, 4, F,
    use="Aprenderé a planificar en planilla cuántas izadas y cuánto tiempo requiere un traslado de carga, aplicando una regla de ejemplo, y a leer un registro de no conformidades.",
    prior=["Sé calcular el límite de una regla en porcentaje.", "Sé multiplicar y dividir números enteros.", "Sé qué es una no conformidad."],
    explain=[
        "Una izada es un movimiento de una carga con un equipo, desde que se levanta hasta que se deja. Para planificar en papel se verifica primero que cada bulto cumpla el límite de la regla; si cumple, las izadas necesarias son la carga total dividida entre la carga de cada izada, y el tiempo del plan es el número de izadas por el tiempo de cada una. La utilización es qué porcentaje de la capacidad de placa se usa en una izada: carga ÷ capacidad × 100.",
        "Un ejemplo con otros valores: 30 t en bultos de 6 t con una grúa de 10 t son 5 izadas; si cada una dura 4 minutos, el plan es de 20 minutos, y cada izada usa el 60 % de la capacidad. El registro de no conformidades se lee con la misma lógica: las abiertas son las detectadas menos las cerradas, y cada una debe tener responsable y fecha de cierre. Estos cálculos se hacen antes y no autorizan a operar la grúa.",
        f"Los tiempos de un plan son estimaciones: el oficial a cargo decide según las condiciones reales. {EMER} {AVISO}",
    ],
    vocab=[("izada", "movimiento de una carga con un equipo, de que se levanta a que se deja"), ("utilización", "porcentaje de la capacidad de placa que usa una carga"), ("no conformidad abierta", "desvío detectado que aún no se corrige"), ("no conformidad cerrada", "desvío detectado que ya se corrigió y se registró"), ("plan de papel", "cálculo hecho en planilla antes de cualquier trabajo")],
    worked=[
        ("Contar izadas", "Un plan de ejemplo mueve 36 t en bultos de 9 t. ¿Cuántas izadas son?", ["Se divide la carga total entre la carga de cada izada.", "36 ÷ 9."], "4 izadas"),
        ("Utilización", "Un bulto de 9 t se mueve con un equipo de capacidad de placa de 15 t. ¿Qué porcentaje de la capacidad usa?", ["Utilización = carga ÷ capacidad × 100.", "9 × 100 ÷ 15."], "60 %"),
    ],
    mistakes=[("Calcular las izadas sin verificar antes que el bulto cumple la regla.", "Si el bulto no cumple, el plan no sirve aunque la cuenta cuadre.", "Verifica primero el límite y después calcula las izadas."),
              ("Creer que un tiempo del plan es una promesa.", "Las condiciones reales pueden cambiar el tiempo.", "Presenta el tiempo como estimación y deja decidir al oficial.")],
    T=[
        ("=", "{F} ¿Cuál es el límite de la regla, en toneladas, para la grúa de la ficha?", "20*80//100", "Se calcula el 80 % de la capacidad de placa.", " t"),
        ("abc", "{F} ¿Cumple el bulto de 12 t con la regla de la ficha?", "Sí, porque 12 t no supera el límite de 16 t", "No, porque 12 t es mayor que 10 t", "No, porque el bulto es más pesado que la mitad de la carga total", "El límite es 16 t y el bulto de 12 t no lo supera."),
        ("=", "{F} ¿Qué porcentaje de la capacidad de placa usa una izada con un bulto de 12 t?", "12*100//20", "Se divide la carga entre la capacidad y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas izadas se necesitan para mover las 48 t en bultos de 12 t?", "48//12", "Se divide la carga total entre la carga de cada izada.", " izadas"),
        ("=", "{F} ¿Cuántos minutos dura el plan completo con 4 izadas de 6 minutos cada una?", "(48//12)*6", "Se multiplican las izadas por los minutos de cada una.", " minutos"),
        ("abc", "{F} Si los bultos fueran de 18 t, ¿qué pasaría con el plan?", "No cumpliría, porque 18 t supera el límite de 16 t", "Cumpliría, porque 18 t es menor que 20 t", "Cumpliría, porque habría menos izadas", "El límite es 16 t; un bulto de 18 t lo supera."),
        ("=", "{F} Si el plan usara bultos de 8 t, ¿cuántas izadas se necesitarían para las 48 t?", "48//8", "Se divide la carga total entre la nueva carga por izada.", " izadas"),
        ("=", "{F} Con bultos de 8 t y 6 minutos por izada, ¿cuántos minutos dura el plan?", "(48//8)*6", "Se multiplican las izadas por los minutos de cada una.", " minutos"),
        ("=", "{F} ¿Cuántas no conformidades abiertas hay en el registro ISM del mes?", "9-6", "Se restan las cerradas a las detectadas.", " no conformidades"),
        ("abc", "{F} Un compañero dice que el plan durará exactamente 24 minutos. ¿Qué respuesta es correcta?", "Es una estimación: las condiciones reales pueden cambiar el tiempo y decide el oficial", "Es exacto, porque está calculado", "Es exacto, si se hace con rapidez", "Los tiempos de un plan son estimaciones sujetas a las condiciones."),
        ("abc", "{F} Una compañera propone subir la regla al 100 % porque la placa dice 20 t. ¿Qué corresponde?", "No cambiarla: solo la modifica quien está autorizado y no se cambia para ahorrar tiempo", "Cambiarla, porque la placa lo permite", "Cambiarla, si se anota en el registro", "La regla de seguridad no se altera para ahorrar tiempo."),
        ("=", "{F} Si se agregan 2 minutos de espera entre una izada y otra en el plan, y cada una de las 4 izadas incluye su espera, ¿cuántos minutos dura el plan?", "(48//12)*(6+2)", "Se suman los minutos de cada izada y su espera y se multiplican por las izadas.", " minutos"),
        ("abc", "{F} ¿Qué debe tener cada no conformidad abierta del registro ISM?", "Un responsable y una fecha de cierre", "Solo el nombre de quien la detectó", "Ningún dato hasta que se cierre", "Cada no conformidad abierta se sigue con responsable y fecha de cierre."),
    ],
    ctx=("abc", "En una planilla de ejemplo, un compañero calcula 5 izadas para 48 t en bultos de 12 t. Tú calculas 4. ¿Qué corresponde?", "Revisar juntos la división de 48 entre 12 y corregir el error", "Aceptar su resultado, porque lleva más tiempo", "Anotar un número intermedio para quedar de acuerdo", "Un cálculo se resuelve revisando la operación, no por acuerdo."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calculan las izadas?", "Carga total dividida entre la carga de cada izada", "Así se obtiene cuántas veces se mueve una carga."),
        ("¿Qué es la utilización?", "El porcentaje de la capacidad de placa que usa una carga", "Se calcula como carga ÷ capacidad × 100."),
        ("¿Cómo se calculan las no conformidades abiertas?", "Detectadas menos cerradas", "Las abiertas son las que faltan por corregir."),
    ],
    op=("Plan de ejemplo: mover 60 t en bultos de 10 t con un equipo de capacidad de placa de 25 t; regla de ejemplo del 80 %; cada izada dura 5 minutos. El registro ISM tiene 7 no conformidades detectadas y 4 cerradas. Escribe (a) el límite de la regla y si el bulto cumple, (b) cuántas izadas y cuántos minutos, (c) qué porcentaje de la capacidad usa cada izada, (d) cuántas no conformidades siguen abiertas.",
        "(a) 25 × 80 ÷ 100 = 20 t; el bulto de 10 t cumple. (b) 60 ÷ 10 = 6 izadas; 6 × 5 = 30 minutos (estimación). (c) 10 × 100 ÷ 25 = 40 %. (d) 7 − 4 = 3.",
        ["verifica el límite", "calcula izadas y tiempo", "calcula la utilización", "calcula las no conformidades abiertas"],
        ["hoja con las cuatro respuestas"],
        ["no verificar el límite antes", "dividir mal las izadas", "presentar el tiempo como exacto"],
        "Pregunta: «¿cuántas veces cabe el bulto en la carga total?». Si no responde, pídele que escriba la división."),
    reinforce="Inventa un plan de papel con una carga total y bultos y calcula izadas y minutos.",
    extend="Explica por qué un plan de papel no reemplaza la decisión del oficial a cargo.",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 5 (alternativas de ejemplo; valores de ejemplo). Se deben mover 36 t en bultos de 9 t. Equipo M: capacidad de placa 10 t, cada izada dura 5 minutos. Equipo N: capacidad de placa 15 t, cada izada dura 8 minutos. "
     "Criterio obligatorio: la carga de cada izada no debe superar el 80 % de la capacidad de placa. Criterio de elección: menor tiempo total. Lista de verificación documental del equipo N: placa legible, sí; registro de inspección al día, sí; señalética visible, no; responsable designado, sí.")
build(
    O4, 5, F,
    use="Aprenderé a comparar alternativas de equipos con criterios, a verificar una lista documental y a decidir qué se informa y qué se registra.",
    prior=["Sé calcular el límite de la regla y las izadas.", "Sé qué es una no conformidad.", "Sé calcular un porcentaje simple."],
    explain=[
        "Para comparar alternativas se aplican primero los criterios obligatorios y se descartan las opciones que no los cumplen; entre las que quedan se usa el criterio de elección, como el menor tiempo. Un equipo que tarda menos pero no cumple la regla de seguridad queda descartado. Los resultados se presentan con los cálculos para que el oficial a cargo pueda revisarlos.",
        "Verificar la calidad documental es revisar una lista de verificación: cada ítem se marca como cumple o no cumple, y el porcentaje de cumplimiento es los ítems cumplidos ÷ los ítems totales × 100. Un ítem que no cumple se registra como no conformidad, se informa al responsable y se sigue hasta cerrarla. Un ejemplo con otro equipo: de 5 ítems se cumplen 4, o sea 80 %, y el ítem faltante se registra aunque el porcentaje sea alto.",
        f"Decidir qué equipo se usa y si se puede trabajar corresponde al oficial a cargo, según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("alternativa", "una de las opciones entre las que se elige"), ("lista de verificación", "lista de ítems que se marcan como cumple o no cumple"), ("porcentaje de cumplimiento", "ítems cumplidos dividido por ítems totales, por 100"), ("criterio obligatorio", "regla que debe cumplirse para que una opción siga en la comparación"), ("registrar", "dejar un dato por escrito con fecha y responsable")],
    worked=[
        ("Aplicar el criterio obligatorio", "Un equipo de ejemplo de 10 t con una regla del 80 % mueve bultos de 9 t. ¿Cumple?", ["El límite es 10 × 80 ÷ 100 = 8 t.", "El bulto de 9 t supera 8 t."], "No cumple"),
        ("Porcentaje de cumplimiento", "Una lista de ejemplo tiene 5 ítems y se cumplen 3. ¿Qué porcentaje se cumple?", ["Se divide 3 entre 5.", "3 × 100 ÷ 5."], "60 %"),
    ],
    mistakes=[("Elegir el equipo más rápido sin revisar la regla de seguridad.", "Un equipo que no cumple el criterio obligatorio se descarta aunque sea más rápido.", "Aplica primero el criterio obligatorio."),
              ("Dejar sin registro un ítem que no cumple porque el porcentaje es alto.", "Cada ítem que no cumple es una no conformidad que debe registrarse.", "Registra cada ítem faltante, sin importar el porcentaje.")],
    T=[
        ("=", "{F} ¿Cuál es el límite de la regla, en toneladas, para el equipo M?", "10*80//100", "Se calcula el 80 % de la capacidad de placa de M.", " t"),
        ("abc", "{F} ¿Cumple el equipo M con el criterio obligatorio?", "No, porque el bulto de 9 t supera su límite de 8 t", "Sí, porque 9 t es menor que 10 t", "Sí, porque M tarda menos por izada", "El criterio compara con el límite de 8 t y no con la capacidad completa."),
        ("=", "{F} ¿Cuál es el límite de la regla, en toneladas, para el equipo N?", "15*80//100", "Se calcula el 80 % de la capacidad de placa de N.", " t"),
        ("abc", "{F} ¿Cumple el equipo N con el criterio obligatorio?", "Sí, porque 9 t no supera su límite de 12 t", "No, porque N tarda más por izada", "No, porque N es más grande que lo necesario", "El bulto de 9 t es menor que el límite de 12 t."),
        ("=", "{F} ¿Cuántas izadas se necesitan para mover las 36 t en bultos de 9 t?", "36//9", "Se divide la carga total entre la carga de cada izada.", " izadas"),
        ("=", "{F} ¿Cuántos minutos tardaría el equipo N en el plan?", "(36//9)*8", "Se multiplican las izadas por los minutos de cada una.", " minutos"),
        ("=", "{F} ¿Cuántos minutos tardaría el equipo M si cumpliera la regla?", "(36//9)*5", "Se multiplican las izadas por los minutos de cada una.", " minutos"),
        ("abc", "{F} ¿Qué equipo se elige según los criterios de la ficha?", "El equipo N, porque es el único que cumple el criterio obligatorio", "El equipo M, porque tarda menos", "Ninguno, porque ambos tardan", "M queda descartado por no cumplir la regla de seguridad."),
        ("=", "{F} ¿Qué porcentaje de cumplimiento tiene la lista de verificación del equipo N?", "3*100//4", "Se dividen los ítems cumplidos entre los ítems totales y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué corresponde con el ítem «señalética visible» que no se cumple en el equipo N?", "Registrarlo como no conformidad e informar al responsable", "Ignorarlo, porque el porcentaje es alto", "Marcarlo como «sí» para que la lista quede completa", "Todo ítem que no cumple se registra como no conformidad."),
        ("abc", "{F} Un compañero dice: «como el equipo N cumple 75 %, no hace falta corregir lo que falta». ¿Qué respuesta es correcta?", "Es falso: cada ítem que no cumple debe registrarse y cerrarse", "Es cierto, porque 75 % es suficiente", "Es cierto, si el equipo es el más rápido", "Un porcentaje alto no justifica dejar sin registro un ítem faltante."),
        ("abc", "En Tripulación de Naves: ¿por qué no se puede elegir un equipo solo por ser el más rápido?", "Porque primero debe cumplir el criterio obligatorio de seguridad", "Porque la rapidez nunca importa", "Porque el equipo más rápido siempre falla", "La seguridad es un criterio obligatorio que se aplica antes que el tiempo."),
        ("=", "{F} ¿Cuántos minutos más tarda el equipo N que lo que tardaría M si cumpliera la regla?", "(36//9)*8-(36//9)*5", "Se resta el tiempo de M al tiempo de N.", " minutos"),
    ],
    ctx=("abc", "Ante la comparación de la ficha, un compañero te pide que «borres el criterio de seguridad para que gane M, que es más rápido». ¿Qué respondes?", "Que no, porque el criterio obligatorio de seguridad no se borra y se informa al oficial", "Que sí, porque la rapidez es lo que importa", "Que sí, pero solo en la copia", "Alterar un criterio de seguridad para favorecer una opción pone en riesgo a las personas."),
    sc=[
        ("En Tripulación de Naves: ¿qué se hace con una opción que no cumple el criterio obligatorio?", "Se descarta", "Una opción que no cumple queda fuera de la comparación."),
        ("A bordo: ¿cómo se calcula el porcentaje de cumplimiento?", "Ítems cumplidos entre ítems totales, por 100", "Así se obtiene qué parte de la lista se cumple."),
        ("¿Quién decide qué equipo se usa?", "El oficial a cargo", "La persona en formación calcula e informa."),
    ],
    op=("Alternativas de ejemplo para mover 40 t en bultos de 10 t. Equipo S: capacidad de placa 12 t, cada izada dura 4 minutos. Equipo T: capacidad de placa 20 t, cada izada dura 6 minutos. Criterio obligatorio: no superar el 80 % de la capacidad de placa. Criterio de elección: menor tiempo total. Lista documental del equipo T: placa legible, sí; registro al día, no; señalética visible, sí; responsable designado, sí. Escribe (a) si cada equipo cumple el criterio obligatorio, (b) cuánto tarda el equipo que cumple, (c) el porcentaje de cumplimiento de la lista de T, (d) qué haces con el ítem que no cumple.",
        "(a) S: el límite es 12 × 80 ÷ 100 = 9,6 t y el bulto de 10 t lo supera, no cumple. T: el límite es 16 t, cumple. (b) 40 ÷ 10 = 4 izadas; 4 × 6 = 24 minutos. (c) 3 × 100 ÷ 4 = 75 %. (d) Se registra como no conformidad, se informa al responsable y se sigue hasta cerrarla.",
        ["aplica el criterio obligatorio a cada equipo", "calcula el tiempo", "calcula el porcentaje de cumplimiento", "registra el ítem faltante"],
        ["hoja con las cuatro respuestas"],
        ["elegir S por rapidez", "no calcular el límite", "ignorar el ítem que no cumple"],
        "Pregunta: «¿cuál es el límite de cada equipo?». Si no responde, pídele que calcule el 80 % de cada capacidad."),
    reinforce="Inventa dos equipos con sus capacidades y tiempos y escribe cuál se elige y por qué.",
    extend="Explica por qué un porcentaje alto de cumplimiento no elimina la necesidad de registrar lo que falta.",
)
