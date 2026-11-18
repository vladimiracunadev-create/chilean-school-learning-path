"""Forestal TP 3.º y 4.º medio: OAE-07 (mantención de máquinas y herramientas forestales como planificación y registros). Solo conceptos y cálculos en papel; sin procedimientos de reparación ni de uso."""
from __future__ import annotations

from tp_fore_common import AVISO, EMER, build

O7 = "TP-FORE-3y4-OAE-07"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). «Taller Demo» atiende 3 herramientas motorizadas de mano y 2 máquinas de mayor tamaño, todas ficticias. "
     "Peligros anotados en el taller: partes móviles, energía acumulada (la que una máquina puede conservar aunque esté apagada, por ejemplo en resortes o en presión), combustibles y lubricantes, superficies calientes, ruido y cargas pesadas. "
     "Residuos del taller: 18 litros de aceite usado acumulados; el gestor autorizado retira 6 litros por visita (dato de ejemplo). Cada máquina o herramienta del taller necesita 3 horas de revisión al mes (dato de ejemplo).")
build(
    O7, 1, F,
    use="Aprenderé qué es la mantención preventiva y la correctiva, qué peligros hay en un taller forestal, qué reglas generales protegen a las personas y cómo se manejan los residuos, sin aprender a reparar nada.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé dividir y multiplicar números enteros.", "Sé qué es un registro."],
    explain=[
        "La mantención es el conjunto de cuidados que mantienen una máquina o una herramienta en buen estado. La mantención preventiva son revisiones y cuidados programados para evitar fallas. La mantención correctiva es la reparación de una falla que ya ocurrió. Todo parte del manual del fabricante, el documento que indica las especificaciones, el uso y la pauta de mantención recomendados para ese equipo. Un taller bien organizado privilegia la mantención preventiva, porque una falla inesperada suele ser más peligrosa y más cara.",
        "Un taller tiene peligros propios: partes móviles, energía acumulada, combustibles y lubricantes, superficies calientes, ruido y cargas pesadas. Se controlan con la jerarquía de controles: eliminar o sustituir lo peligroso, usar protecciones físicas como las guardas fijas, aplicar reglas y capacitación, y como última barrera el EPP. Para evitar que una máquina se active durante una mantención, la empresa tiene un procedimiento de bloqueo de energía que ejecuta solo personal autorizado. Los aceites y otros residuos peligrosos se entregan a un gestor autorizado.",
        f"Este cuaderno no enseña a reparar ni a desarmar ninguna máquina. {EMER} {AVISO}",
    ],
    vocab=[("mantención preventiva", "revisiones y cuidados programados para evitar fallas"), ("mantención correctiva", "reparación de una falla que ya ocurrió"), ("manual del fabricante", "documento con las especificaciones, el uso y la pauta de mantención de un equipo"), ("energía acumulada", "energía que una máquina puede conservar aunque esté apagada, por ejemplo en resortes o en presión"), ("guarda fija", "protección física que cubre una parte móvil"), ("bloqueo de energía", "procedimiento de la empresa, ejecutado por personal autorizado, para impedir que una máquina se active durante una mantención"), ("gestor autorizado", "empresa autorizada para retirar y tratar residuos peligrosos")],
    worked=[
        ("Preventiva o correctiva", "Un taller de ejemplo cambia una pieza porque se rompió y la máquina quedó detenida. ¿Qué tipo de mantención es?", ["La pieza se rompió antes de la intervención.", "Reparar una falla ya ocurrida es mantención correctiva."], "Correctiva"),
        ("Visitas del gestor", "Un taller de ejemplo acumula 30 litros de aceite usado y el gestor retira 10 litros por visita. ¿Cuántas visitas hacen falta?", ["Se divide el total entre lo que retira cada visita.", "30 ÷ 10 = 3."], "3 visitas"),
    ],
    mistakes=[("Creer que leer el manual del fabricante habilita para reparar una máquina.", "La mantención la hace personal autorizado y con el bloqueo de energía de la empresa.", "Usa el manual para entender la pauta y deja la tarea a personal autorizado."),
              ("Creer que una máquina apagada no tiene energía y es segura de tocar.", "Puede conservar energía acumulada, por ejemplo en resortes o en presión.", "El bloqueo de energía lo hace personal autorizado según el procedimiento de la empresa.")],
    T=[
        ("abc", "En Forestal: ¿qué es la mantención preventiva de una máquina?", "Las revisiones y los cuidados programados para evitar fallas", "La reparación de una falla que ya ocurrió", "El reemplazo de la máquina cada año aunque funcione", "La preventiva se programa antes de que haya falla; la correctiva repara una falla ya ocurrida."),
        ("abc", "En Forestal: ¿qué es la mantención correctiva?", "La reparación de una falla que ya ocurrió", "Las revisiones programadas para evitar fallas", "La compra de una máquina nueva", "La correctiva actúa sobre una falla existente."),
        ("abc", "En Forestal: ¿qué es el manual del fabricante?", "Un documento con las especificaciones, el uso y la pauta de mantención de un equipo", "Un documento que fija el precio de venta", "Un permiso para operar la máquina", "El manual describe el equipo; no es un precio ni un permiso."),
        ("=", "{F} ¿Cuántas visitas del gestor autorizado hacen falta para retirar el aceite usado acumulado?", "18//6", "Se divide el total de litros entre los que retira cada visita.", " visitas"),
        ("abc", "{F} ¿Qué corresponde hacer con el aceite usado del taller?", "Entregarlo a un gestor autorizado según el plan de residuos peligrosos", "Verterlo en una zanja de drenaje", "Guardarlo en cualquier envase sin rotular", "El aceite usado es un residuo peligroso y requiere gestión autorizada."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «energía acumulada»?", "Que una parte se mueva o libere energía de forma inesperada y cause daño", "La energía que se ahorra al apagar la máquina", "Que el taller gaste más electricidad", "El riesgo es la posibilidad de daño; la energía acumulada es la fuente del peligro."),
        ("abc", "{F} Una guarda fija que cubre una parte móvil es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla escrita", "De EPP, porque protege al personal", "La guarda es una barrera física que no depende de que alguien la recuerde."),
        ("=", "{F} ¿Cuántas horas de revisión al mes necesita el taller para todos sus equipos?", "(3+2)*3", "Se suman los equipos y se multiplican por las horas de cada uno.", " horas"),
        ("abc", "{F} Un compañero dice: «leí el manual, así que puedo reparar la máquina yo solo». ¿Qué respuesta es correcta?", "Es falso: la mantención la hace personal autorizado con el bloqueo de energía de la empresa", "Es cierto, si usa guantes", "Es cierto, si apaga la máquina", "Una máquina apagada puede conservar energía acumulada; el manual no habilita para reparar."),
        ("abc", "Durante una visita de ejemplo a un taller, una máquina atrapa la mano de un trabajador. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a apagar la máquina tú mismo", "Intentar sacar la mano a tirones", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "En Forestal: ¿por qué un taller prefiere la mantención preventiva?", "Porque reduce las fallas inesperadas, que suelen ser más peligrosas y más caras", "Porque elimina la necesidad de toda reparación", "Porque no requiere ningún registro", "La preventiva reduce fallas, pero no las elimina ni evita registrar."),
        ("=", "En un taller de ejemplo se generan 3 litros de aceite usado por semana. ¿En cuántas semanas se juntan 18 litros?", "18//3", "Se divide el total de litros entre los que se generan por semana.", " semanas"),
        ("abc", "{F} Un letrero «máquina en mantención, no encender» es un control de tipo:", "Administrativo, y no reemplaza el bloqueo de energía hecho por personal autorizado", "De ingeniería, porque impide encender la máquina", "De EPP, porque protege a las personas", "El letrero informa, pero no impide físicamente que la máquina se active."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por ayudarlo a «arreglar» su herramienta motorizada en el garaje, porque «tú ya sabes de mantención». ¿Qué respondes?", "Que no, porque esa tarea exige personal autorizado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si la herramienta está apagada", "Que sí, si usas guantes y lentes", "Una herramienta apagada puede conservar energía y el EPP no reemplaza la autorización."),
    sc=[
        ("En Forestal: ¿qué es la mantención correctiva?", "La reparación de una falla que ya ocurrió", "La correctiva actúa después de la falla."),
        ("¿Qué es la energía acumulada?", "La que una máquina puede conservar aunque esté apagada", "Una máquina apagada puede seguir siendo peligrosa."),
        ("En el trabajo forestal: ¿qué se hace con el aceite usado?", "Se entrega a un gestor autorizado", "El aceite usado es un residuo peligroso."),
    ],
    op=("Ficha de ejemplo: «Taller Muestra» atiende 4 herramientas motorizadas y 2 máquinas de mayor tamaño; cada equipo necesita 2 horas de revisión al mes (dato de ejemplo). Acumula 24 litros de aceite usado y el gestor autorizado retira 8 litros por visita. Peligros anotados: partes móviles y energía acumulada. Escribe (a) las horas de revisión al mes, (b) las visitas del gestor, (c) un control de ingeniería para las partes móviles, (d) por qué leer el manual no te habilita para reparar.",
        "(a) (4 + 2) × 2 = 12 horas. (b) 24 ÷ 8 = 3 visitas. (c) Una guarda fija que cubra las partes móviles. (d) Porque la mantención exige personal autorizado, el bloqueo de energía de la empresa y la norma vigente.",
        ["calcula las horas", "calcula las visitas del gestor", "propone un control de ingeniería", "explica por qué no habilita"],
        ["hoja con las cuatro respuestas"],
        ["no sumar todos los equipos", "creer que apagada significa segura", "proponer solo el EPP"],
        "Pregunta: «¿una máquina apagada puede tener energía?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe una oración que distinga mantención preventiva de correctiva con un ejemplo inventado de taller.",
    extend="Explica con un ejemplo por qué una guarda fija protege mejor que pedir a todos que tengan cuidado.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (hoja de vida de ejemplo, inventada). Máquina M-1 (una máquina ficticia de la empresa). Horómetro actual: 1.180 horas. Última mantención preventiva: a las 1.000 horas. "
     "Pauta del manual de ejemplo: mantención cada 250 horas de uso. Trabaja 10 horas por día. "
     "Repuestos: cada mantención de la pauta usa 2 repuestos del tipo R (dato de ejemplo) y hay 7 en bodega. Roles del taller: jefe de taller, mecánico autorizado, operador, prevencionista y bodeguero.")
build(
    O7, 2, F,
    use="Aprenderé los documentos y conceptos de la mantención: hoja de vida, horómetro, intervalo, orden de trabajo, repuestos y los roles del taller.",
    prior=["Sé qué es mantención preventiva y correctiva.", "Sé restar, sumar y dividir números enteros.", "Sé qué es un registro."],
    explain=[
        "La hoja de vida de una máquina es el registro de su historia: horas de uso, mantenciones, fallas y repuestos. El horómetro es un instrumento que cuenta las horas de funcionamiento. La pauta de mantención del manual fija un intervalo, es decir, cada cuántas horas de uso corresponde una mantención. Para saber cuánto falta, se calcula la diferencia entre el horómetro en que toca la mantención y el horómetro actual. Por ejemplo, una máquina con una mantención cada 100 horas que la tuvo a las 500 horas, la necesita de nuevo a las 600.",
        "La orden de trabajo es el documento que autoriza y registra un trabajo de mantención, con responsable, fecha y detalle. Un repuesto es una pieza que reemplaza a otra del equipo, y el stock es la cantidad disponible en bodega. Cada rol cumple su función: el jefe de taller programa, el mecánico autorizado ejecuta la mantención, el operador usa la máquina y avisa si nota algo raro, el prevencionista asesora en riesgos y el bodeguero controla los repuestos. Un registro falso o adelantado oculta riesgos y no se hace.",
        f"Los intervalos y los repuestos reales los fija el manual del fabricante; aquí son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("hoja de vida", "registro de la historia de una máquina: horas, mantenciones, fallas y repuestos"), ("horómetro", "instrumento que cuenta las horas de funcionamiento"), ("intervalo de mantención", "horas de uso entre una mantención y la siguiente según la pauta"), ("orden de trabajo", "documento que autoriza y registra un trabajo de mantención"), ("repuesto", "pieza que reemplaza a otra del equipo"), ("stock", "cantidad de repuestos disponibles en bodega")],
    worked=[
        ("Próxima mantención", "Una máquina de ejemplo tuvo su mantención a las 800 horas y su intervalo es de 150 horas. ¿A qué horómetro toca la siguiente?", ["Se suma el intervalo al horómetro de la última mantención.", "800 + 150 = 950."], "A las 950 horas"),
        ("Horas que faltan", "El horómetro actual de esa máquina es 910. ¿Cuántas horas faltan para la mantención?", ["Se resta el horómetro actual al de la mantención.", "950 − 910 = 40."], "40 horas"),
    ],
    mistakes=[("Anotar una mantención como hecha antes de ejecutarla para «tener el registro al día».", "Un registro adelantado es falso y oculta el riesgo.", "Se anota solo lo ejecutado, con fecha y responsable."),
              ("Seguir operando una máquina que hace un ruido extraño «hasta fin de turno».", "Un ruido inusual puede indicar una falla que se agrava.", "El operador avisa al jefe de taller y espera la evaluación.")],
    T=[
        ("abc", "En Forestal: ¿qué es la hoja de vida de una máquina?", "El registro de su historia: horas, mantenciones, fallas y repuestos", "El documento con el precio de compra", "El manual para quien opera la máquina", "La hoja de vida sirve para dar seguimiento a la historia de la máquina."),
        ("abc", "En Forestal: ¿qué es un horómetro?", "Un instrumento que cuenta las horas de funcionamiento", "Un instrumento que mide la temperatura del motor", "Un indicador del nivel de combustible", "El horómetro cuenta horas de uso; otras características se miden con otros instrumentos."),
        ("abc", "En Forestal: ¿qué es una orden de trabajo de mantención?", "Un documento que autoriza y registra un trabajo de mantención", "Un permiso para operar la máquina", "Una factura de compra de repuestos", "La orden de trabajo ordena y deja constancia del trabajo."),
        ("=", "{F} ¿Cuántas horas de uso han pasado desde la última mantención?", "1180-1000", "Se resta el horómetro de la última mantención al horómetro actual.", " horas"),
        ("=", "{F} ¿A qué horómetro toca la próxima mantención según la pauta?", "1000+250", "Se suma el intervalo al horómetro de la última mantención.", " horas"),
        ("=", "{F} ¿Cuántas horas faltan para la próxima mantención?", "1000+250-1180", "Se resta el horómetro actual al horómetro en que toca la mantención.", " horas"),
        ("=", "{F} Si la máquina trabaja las horas diarias indicadas, ¿en cuántos días llega a la próxima mantención?", "(1000+250-1180)//10", "Se dividen las horas que faltan entre las horas de trabajo por día.", " días"),
        ("abc", "{F} ¿Qué rol ejecuta la mantención de la máquina?", "El mecánico autorizado", "El operador que la usa", "El bodeguero que guarda los repuestos", "El mecánico autorizado ejecuta la mantención; el operador la usa y avisa."),
        ("abc", "{F} Un operador nota un ruido extraño en la máquina M-1. ¿Qué corresponde?", "Informar al jefe de taller y no seguir operándola hasta que se evalúe", "Seguir operando hasta que termine el turno", "Intentar repararla en terreno con las herramientas que tenga", "Un ruido anormal puede indicar una falla; se informa y se evalúa antes de continuar."),
        ("abc", "{F} Un compañero propone anotar en la hoja de vida la mantención que toca en 7 días para «tenerla al día». ¿Qué respuesta es correcta?", "No: solo se anota lo ejecutado, con fecha y responsable", "Sí, si después se hace igual", "Sí, si se anota con lápiz", "Un registro adelantado es falso y puede ocultar riesgos."),
        ("abc", "{F} ¿Qué ocurre si se supera el intervalo de mantención de la pauta?", "Aumenta el riesgo de fallas y se incumple la pauta del fabricante", "No ocurre nada, porque el intervalo es solo una sugerencia", "Se alarga la vida útil de la máquina", "Superar el intervalo desprotege la máquina y a las personas que la usan."),
        ("=", "{F} Con el stock y el consumo por mantención de la ficha, ¿cuántas mantenciones completas se pueden cubrir con los repuestos de bodega?", "7//2", "Se divide el stock entre los repuestos que usa cada mantención.", " mantenciones"),
        ("abc", "{F} ¿Qué cambio de intervalo exige más cuidado y autorización del responsable?", "Alargarlo respecto de lo que indica el manual", "Acortarlo respecto de lo que indica el manual", "Ninguno, porque cualquier cambio es igual", "Alargar el intervalo aumenta el riesgo de fallas y se aparta de la pauta del fabricante."),
    ],
    ctx=("abc", "El jefe te pide «postergar un poco» la mantención de la máquina M-1 para no frenar la producción esta semana. ¿Qué respondes?", "Que la pauta del fabricante no se posterga por producción, y que lo consultarás con un adulto responsable", "Que sí, si es solo por una semana", "Que sí, si el operador es muy cuidadoso", "El intervalo protege a las personas y la máquina; no se cambia por conveniencia."),
    sc=[
        ("En Forestal: ¿qué es el intervalo de mantención?", "Las horas de uso entre una mantención y la siguiente", "El intervalo viene en la pauta del manual."),
        ("¿Quién ejecuta la mantención?", "El mecánico autorizado", "La mantención la hace personal autorizado."),
        ("¿Qué se anota en la hoja de vida?", "Solo lo que realmente se ejecutó, con fecha y responsable", "Un registro adelantado es falso y puede ocultar riesgos."),
    ],
    op=("Ficha de ejemplo (datos de ejemplo): máquina M-4, horómetro actual 2.460 horas; última mantención a las 2.400 horas; intervalo del manual: 200 horas; trabaja 10 horas por día. Cada mantención usa 3 repuestos y hay 10 en bodega. Escribe (a) a qué horómetro toca la próxima mantención, (b) cuántas horas y cuántos días faltan, (c) cuántas mantenciones completas cubre el stock, (d) qué haces si el operador nota un ruido extraño.",
        "(a) 2.400 + 200 = 2.600 horas. (b) 2.600 − 2.460 = 140 horas; 140 ÷ 10 = 14 días. (c) 10 ÷ 3 = 3 mantenciones completas. (d) Se informa al jefe de taller y no se sigue operando hasta que se evalúe.",
        ["calcula el horómetro de la próxima mantención", "calcula horas y días que faltan", "calcula las mantenciones del stock", "indica qué hacer ante un ruido extraño"],
        ["hoja con las cuatro respuestas"],
        ["usar el horómetro actual en vez del de la última mantención", "redondear mal el stock", "seguir operando con un ruido extraño"],
        "Pregunta: «¿desde qué horómetro se cuenta el intervalo?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una máquina con horómetro actual, última mantención e intervalo, y calcula cuántas horas faltan.",
    extend="Explica con un ejemplo por qué un registro adelantado es peor que un registro atrasado.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (hojas de vida de ejemplo, inventadas). Máquina M-A: horómetro 1.560, última mantención a las 1.500, intervalo 100 horas, trabaja 8 horas por día, costo de la mantención $60.000. "
     "Máquina M-B: horómetro 3.120, última mantención a las 3.000, intervalo 250 horas, trabaja 10 horas por día, costo de la mantención $150.000. "
     "Máquina M-C: horómetro 840, última mantención a las 800, intervalo 50 horas, trabaja 5 horas por día, costo de la mantención $30.000.")
build(
    O7, 3, F,
    use="Aprenderé a analizar varias hojas de vida: calcular cuándo toca la mantención de cada máquina, priorizar y programar el taller, y reaccionar si falta un repuesto.",
    prior=["Sé calcular el horómetro de la próxima mantención.", "Sé dividir números enteros.", "Sé qué es una orden de trabajo."],
    explain=[
        "Analizar un caso es comparar varias máquinas a la vez. Para cada una se calcula en qué horómetro toca su mantención y cuántas horas faltan; luego se divide por las horas diarias de uso para saber en cuántos días llega. Priorizar es ordenar las tareas según su urgencia o su riesgo: se atiende primero la máquina a la que le queda menos tiempo, y no la que tiene el horómetro total más alto, porque el total no dice cuándo toca la mantención.",
        "Con el orden de prioridad se programa el taller con órdenes de trabajo, fechas y repuestos. Si falta un repuesto, se informa y se reprograma, y la máquina no se usa más allá de su intervalo mientras llega. Tampoco se improvisa con un repuesto que el fabricante no indica. Los costos de las mantenciones se suman para presupuestar. Todo se registra en las hojas de vida.",
        f"La programación la hace el jefe de taller; la ejecución, personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("priorizar", "ordenar las tareas según su urgencia o su riesgo"), ("programación del taller", "calendario de las mantenciones con fechas, responsables y repuestos"), ("presupuesto", "cálculo del gasto previsto"), ("horas diarias de uso", "horas que trabaja una máquina cada día")],
    worked=[
        ("Días hasta la mantención", "Una máquina de ejemplo tiene 60 horas por delante y trabaja 6 horas por día. ¿En cuántos días llega a su mantención?", ["Se divide las horas que faltan entre las horas diarias.", "60 ÷ 6 = 10."], "10 días"),
        ("Presupuestar", "Dos mantenciones de ejemplo cuestan $45.000 y $70.000. ¿Cuánto suman?", ["Se suman ambos costos.", "45.000 + 70.000 = 115.000."], "$115.000"),
    ],
    mistakes=[("Atender primero la máquina con el horómetro total más alto.", "El total acumulado no dice cuándo toca la mantención.", "Compara las horas que faltan para el próximo intervalo."),
              ("Usar un repuesto distinto al indicado por el fabricante porque está disponible.", "Un repuesto no indicado puede fallar y causar accidentes.", "Se informa, se reprograma y se espera el repuesto correcto.")],
    T=[
        ("abc", "En Forestal: ¿qué es el intervalo de mantención de una máquina?", "Las horas de uso entre una mantención y la siguiente según la pauta", "Las horas que el taller permanece abierto cada día", "El tiempo que dura cada reparación", "El intervalo se mide en horas de uso de la máquina."),
        ("abc", "En Forestal: ¿qué significa priorizar las mantenciones de un taller?", "Ordenarlas según su urgencia o su riesgo", "Hacer primero la que sea más fácil", "Hacer primero la más barata", "Priorizar es ordenar según la urgencia, no según la facilidad o el costo."),
        ("abc", "En Forestal: ¿por qué se prioriza por horas restantes y no por el horómetro total?", "Porque lo que importa es qué tan cerca está cada máquina de su intervalo", "Porque el horómetro total no puede conocerse", "Porque da lo mismo cuál se atienda primero", "El total acumulado no dice cuándo toca la mantención."),
        ("=", "{F} ¿Cuántas horas le faltan a la máquina M-A para su próxima mantención?", "1500+100-1560", "Se suma el intervalo al horómetro de la última mantención y se resta el actual.", " horas"),
        ("=", "{F} ¿Cuántas horas le faltan a la máquina M-B para su próxima mantención?", "3000+250-3120", "Se suma el intervalo al horómetro de la última mantención y se resta el actual.", " horas"),
        ("=", "{F} ¿Cuántas horas le faltan a la máquina M-C para su próxima mantención?", "800+50-840", "Se suma el intervalo al horómetro de la última mantención y se resta el actual.", " horas"),
        ("=", "{F} ¿En cuántos días llega la máquina M-C a su mantención?", "(800+50-840)//5", "Se dividen las horas que faltan entre las horas diarias de uso.", " días"),
        ("=", "{F} ¿En cuántos días llega la máquina M-A a su mantención?", "(1500+100-1560)//8", "Se dividen las horas que faltan entre las horas diarias de uso.", " días"),
        ("=", "{F} ¿En cuántos días llega la máquina M-B a su mantención?", "(3000+250-3120)//10", "Se dividen las horas que faltan entre las horas diarias de uso.", " días"),
        ("abc", "{F} ¿Qué máquina debe programarse primero?", "La M-C, porque es la que llega antes a su mantención", "La M-B, porque tiene el horómetro más alto", "La M-A, porque es la del medio", "La M-C llega en 2 días; M-A en 5 y M-B en 13."),
        ("=", "{F} ¿Cuánto cuestan en total las tres mantenciones?", "60000+150000+30000", "Se suman los costos de las tres mantenciones.", " pesos"),
        ("abc", "{F} El día antes de la mantención de la M-C falta el repuesto indicado por el fabricante. ¿Qué corresponde?", "Informar, reprogramar y no usar la máquina más allá de su intervalo mientras llega el repuesto", "Seguir usándola hasta que llegue el repuesto", "Colocar un repuesto parecido de otra máquina", "Un repuesto no indicado o una máquina fuera de intervalo aumentan el riesgo de falla."),
        ("abc", "{F} Un compañero propone no programar la M-C porque es «la más nuevecita». ¿Qué respuesta es correcta?", "No: la mantención depende del intervalo y de las horas de uso, no de lo nueva que parezca", "Sí, porque las máquinas nuevas no necesitan mantención", "Sí, si el operador la cuida mucho", "El intervalo de la pauta se cumple en todas las máquinas, nuevas o antiguas."),
    ],
    ctx=("abc", "Un jefe de turno te pide que «marques como hecha» la mantención de la M-C porque están apurados, y que la hagas después. ¿Qué respondes?", "Que no, porque un registro adelantado es falso, y que lo consultarás con un adulto responsable", "Que sí, si la haces el día siguiente", "Que sí, si lo anotas con otro color", "El registro debe reflejar lo realmente ejecutado."),
    sc=[
        ("En Forestal: ¿cómo se calculan los días hasta la mantención?", "Dividiendo las horas que faltan entre las horas diarias de uso", "Así se traducen las horas a días de calendario."),
        ("¿Qué máquina se atiende primero?", "La que llega antes a su intervalo", "La urgencia depende de lo que falta, no del total acumulado."),
        ("¿Qué se hace si falta el repuesto correcto?", "Se informa, se reprograma y la máquina no se usa fuera de intervalo", "No se improvisa con un repuesto que el fabricante no indica."),
    ],
    op=("Ficha de ejemplo (datos de ejemplo): máquina X, horómetro 940, última mantención a las 900, intervalo 80 horas, trabaja 4 horas por día, costo $50.000. Máquina Y, horómetro 2.050, última mantención a las 2.000, intervalo 100 horas, trabaja 10 horas por día, costo $90.000. Escribe (a) las horas y los días que le faltan a cada máquina, (b) cuál se programa primero, (c) el costo total de ambas, (d) qué haces si falta el repuesto de la que se programa primero.",
        "(a) X: 900 + 80 − 940 = 40 horas, 10 días; Y: 2.000 + 100 − 2.050 = 50 horas, 5 días. (b) La Y, porque llega antes. (c) 50.000 + 90.000 = 140.000 pesos. (d) Se informa, se reprograma y la máquina no se usa más allá de su intervalo mientras llega el repuesto.",
        ["calcula horas y días de cada máquina", "elige la prioridad con los días", "suma los costos", "propone qué hacer sin improvisar"],
        ["hoja con las cuatro respuestas"],
        ["priorizar por el horómetro total", "olvidar dividir por las horas diarias", "proponer un repuesto distinto"],
        "Pregunta: «¿cuál llega antes a su mantención, en días?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos máquinas con horas que faltan y horas diarias, y decide cuál se atiende primero.",
    extend="Explica con un ejemplo por qué una máquina con horómetro alto puede no ser la más urgente.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (costos de ejemplo, inventados). Una máquina trabaja 1.000 horas al año (dato de ejemplo) y su pauta pide una mantención preventiva cada 250 horas, con un costo de $90.000 cada una. "
     "Si no se hace mantención preventiva, se estiman 2 fallas al año; cada falla cuesta $600.000 de reparación y deja la máquina 5 días detenida, con un costo de parada de $50.000 por día. "
     "Se programan 200 horas de trabajo al mes; en un mes con mantención preventiva la máquina está detenida 10 horas, y en un mes con una falla, 40 horas.")
build(
    O7, 4, F,
    use="Aprenderé a comparar en papel el costo de la mantención preventiva con el de las fallas, y a calcular la disponibilidad de una máquina, sin recortar la seguridad.",
    prior=["Sé calcular costos con multiplicaciones y sumas.", "Sé calcular porcentajes simples.", "Sé qué es mantención preventiva y correctiva."],
    explain=[
        "Un análisis de costos de mantención compara el costo de prevenir con el costo de las fallas. El costo de una falla incluye la reparación y el costo de parada, que es lo que se pierde cada día en que la máquina no trabaja. La disponibilidad es el porcentaje del tiempo programado en que la máquina está en condiciones de trabajar: se calcula dividiendo las horas disponibles entre las programadas y multiplicando por 100. Por ejemplo, con 100 horas programadas y 8 detenidas, la disponibilidad es 92 %.",
        "En el análisis siempre se agregan criterios que no son de dinero: la seguridad de las personas y el cumplimiento de la pauta del fabricante. Una falla inesperada puede ser peligrosa, y por eso la mantención preventiva no se posterga por cumplir metas de producción. Los datos de esta clase son de ejemplo: los reales salen de las hojas de vida y de las cotizaciones.",
        f"El análisis lo hace el jefe de taller con los datos del registro; tú practicas los cálculos. {EMER} {AVISO}",
    ],
    vocab=[("costo de parada", "pérdida que produce cada día en que la máquina está detenida"), ("disponibilidad", "porcentaje del tiempo programado en que la máquina está en condiciones de trabajar"), ("falla", "pérdida de la capacidad de la máquina de funcionar como debe"), ("costo de reparación", "gasto de arreglar una falla")],
    worked=[
        ("Costo de una falla", "Una falla de ejemplo cuesta $200.000 de reparación y deja la máquina 3 días detenida a $40.000 por día. ¿Cuánto cuesta en total?", ["La parada cuesta 3 × 40.000 = 120.000.", "200.000 + 120.000 = 320.000."], "$320.000"),
        ("Disponibilidad", "En un mes de ejemplo se programan 160 horas y la máquina queda detenida 16. ¿Cuál es la disponibilidad?", ["Horas disponibles: 160 − 16 = 144.", "144 ÷ 160 son 90 de cada 100."], "90 %"),
    ],
    mistakes=[("Contar solo el costo de reparación de una falla.", "La máquina detenida también tiene un costo de parada.", "Suma reparación y costo de parada."),
              ("Postergar la mantención preventiva para cumplir una meta de producción.", "Se aumenta el riesgo de fallas y de accidentes.", "La pauta del fabricante y la seguridad no se postergan.")],
    T=[
        ("abc", "En Forestal: ¿qué es la disponibilidad de una máquina?", "El porcentaje del tiempo programado en que está en condiciones de trabajar", "El porcentaje de máquinas que se compraron en el año", "El total de horas que ha trabajado desde su compra", "La disponibilidad relaciona horas disponibles con horas programadas."),
        ("abc", "En Forestal: ¿qué es el costo de parada de una máquina?", "La pérdida que produce cada día en que está detenida", "El costo de comprar los repuestos", "El precio de una máquina nueva", "El costo de parada se refiere al tiempo sin trabajar."),
        ("abc", "En Forestal: ¿qué compara un análisis de costos entre mantención preventiva y correctiva?", "El costo de prevenir frente al costo de las fallas, incluidas las paradas", "Solo el precio de los repuestos de cada una", "Solo las horas de uso de cada una", "El análisis considera todos los costos, no solo los repuestos."),
        ("=", "{F} ¿Cuántas mantenciones preventivas se hacen al año?", "1000//250", "Se divide las horas anuales entre el intervalo de la pauta.", " mantenciones"),
        ("=", "{F} ¿Cuánto cuestan al año las mantenciones preventivas?", "(1000//250)*90000", "Se multiplican las mantenciones por el costo de cada una.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta en total una falla, sumando reparación y parada?", "600000+5*50000", "Se suma el costo de reparación con el costo de los 5 días de parada.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan al año las fallas estimadas si no se hace mantención preventiva?", "2*(600000+5*50000)", "Se multiplica el costo de una falla por el número de fallas estimadas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos se ahorran al año con la mantención preventiva frente a no hacerla?", "2*(600000+5*50000)-(1000//250)*90000", "Se resta el costo de la preventiva al costo estimado de las fallas.", " pesos"),
        ("abc", "{F} Con los datos de ejemplo, ¿qué conclusión es correcta?", "Conviene la mantención preventiva, porque su costo anual es menor que el de las fallas estimadas", "Conviene no hacer mantención, porque la preventiva cuesta $360.000", "Da lo mismo, porque ambas cuestan igual", "La preventiva cuesta 360.000 al año y las fallas estimadas 1.700.000."),
        ("=", "{F} ¿Cuál es la disponibilidad en un mes con mantención preventiva?", "(200-10)*100//200", "Se resta las horas detenidas a las programadas y se divide por las programadas.", " %"),
        ("=", "{F} ¿Cuál es la disponibilidad en un mes con una falla?", "(200-40)*100//200", "Se resta las horas detenidas a las programadas y se divide por las programadas.", " %"),
        ("abc", "{F} Si con mantención preventiva todavía ocurriera una falla, ¿seguiría conviniendo en el ejemplo?", "Sí: 360.000 + 850.000 = 1.210.000, menos que 1.700.000", "No: ya no conviene, porque ocurrió una falla", "Da lo mismo, porque el total es igual", "Incluso con una falla, el total con preventiva es menor que el estimado sin ella."),
        ("abc", "{F} Un jefe propone saltarse la mantención del trimestre para cumplir la meta de producción. ¿Qué respuesta es correcta?", "No: la pauta del fabricante y la seguridad no se postergan por metas, y se consulta a un adulto responsable", "Sí, si la máquina todavía funciona bien", "Sí, si el operador tiene experiencia", "Que la máquina funcione hoy no garantiza que no falle en el intervalo omitido."),
    ],
    ctx=("abc", "Un proveedor te ofrece un repuesto «compatible» sin ficha técnica y más barato, para ahorrar en la mantención. ¿Qué respondes?", "Que no se usa un repuesto sin las especificaciones del fabricante, y que lo consultarás con un adulto responsable", "Que sí, si el precio es la mitad", "Que sí, si el proveedor dice que lo usa mucha gente", "Un repuesto sin especificaciones puede fallar; lo barato no reemplaza el cumplimiento del fabricante."),
    sc=[
        ("En Forestal: ¿qué incluye el costo de una falla?", "La reparación y el costo de parada", "El costo de parada se suma al de reparación."),
        ("En el trabajo forestal: ¿cómo se calcula la disponibilidad?", "Horas disponibles divididas entre las programadas, por 100", "La disponibilidad se expresa como porcentaje."),
        ("¿Se postergan las mantenciones por cumplir metas?", "No, la seguridad y la pauta no se postergan", "Postergar aumenta el riesgo de fallas y de accidentes."),
    ],
    op=("Ficha de ejemplo (datos de ejemplo): una máquina trabaja 900 horas al año; su pauta pide mantención cada 150 horas, a $70.000 cada una. Sin preventiva se estiman 3 fallas al año; cada falla cuesta $400.000 de reparación y 4 días detenida a $30.000 por día. Se programan 180 horas al mes; con una falla queda detenida 36 horas. Escribe (a) el costo anual de la preventiva, (b) el costo anual de las fallas estimadas, (c) cuánto se ahorra, (d) la disponibilidad en un mes con falla y qué criterio no económico revisarías.",
        "(a) 900 ÷ 150 = 6 mantenciones; 6 × 70.000 = 420.000 pesos. (b) Una falla cuesta 400.000 + 4 × 30.000 = 520.000; 3 fallas cuestan 1.560.000. (c) 1.560.000 − 420.000 = 1.140.000 pesos. (d) (180 − 36) ÷ 180 = 144 ÷ 180 = 80 %. Se revisa además la seguridad de las personas y el cumplimiento de la pauta del fabricante.",
        ["calcula la preventiva", "calcula las fallas con la parada", "calcula el ahorro", "calcula la disponibilidad y nombra un criterio no económico"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el costo de parada", "dividir mal para la disponibilidad", "decidir solo por dinero"],
        "Pregunta: «¿qué se pierde cada día que la máquina está detenida?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una falla con reparación y días de parada y calcula su costo total.",
    extend="Explica con un ejemplo por qué la seguridad es un criterio de la mantención aparte del costo.",
)
