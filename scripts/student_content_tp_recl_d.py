"""Refrigeración y Climatización TP 3.º y 4.º medio: OAE-08 (mantenimiento preventivo y correctivo: planes, costos y registros) y OAE-09 (recuperación, reciclaje y almacenamiento de refrigerantes: conceptos, trazabilidad y balances). Solo conceptos y planillas, con datos de ejemplo; sin procedimientos."""
from __future__ import annotations

from tp_recl_common import AVISO, EMER, build

O8 = "TP-RECL-3y4-OAE-08"
O9 = "TP-RECL-3y4-OAE-09"

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Un almacén ficticio tiene una vitrina refrigerada. Tipos de mantenimiento: preventivo (programado, antes de la falla), correctivo (después de la falla) y predictivo (según datos de la condición del equipo). "
     "Costos de ejemplo: una mantención preventiva $60.000; una reparación correctiva $350.000. El plan del fabricante pide 2 mantenciones preventivas al año.")
build(
    O8, 1, F,
    use="Aprenderé qué es el mantenimiento preventivo, correctivo y predictivo, por qué se hace, qué riesgos tiene y por qué un equipo se asegura antes de intervenirlo.",
    prior=["Sé qué es un manual del fabricante.", "Sé calcular costos.", "Sé qué es un permiso de trabajo."],
    explain=[
        "El mantenimiento es el conjunto de acciones para que un equipo siga funcionando según los parámetros del manual del fabricante. El mantenimiento preventivo es programado y se hace antes de que ocurra una falla. El correctivo se hace después de que el equipo falla. El predictivo usa datos de la condición del equipo, como su consumo, para anticipar problemas. Mantener bien un equipo mejora la seguridad, reduce el consumo de energía, alarga su vida útil y cuida el medio ambiente.",
        "Mantener tiene riesgos: energía eléctrica, presión del refrigerante, partes que giran y, a veces, altura. Antes de intervenir se asegura que el equipo no pueda energizarse por error, con una medida llamada bloqueo y etiquetado: la aplica personal autorizado según el procedimiento de la empresa y la norma vigente. Este cuaderno no describe cómo hacerlo. Quien trabaja lleva EPP y permiso de trabajo cuando corresponde, y todo queda registrado.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("mantenimiento preventivo", "mantenimiento programado que se hace antes de que ocurra una falla"), ("mantenimiento correctivo", "mantenimiento que se hace después de que el equipo falla"), ("mantenimiento predictivo", "mantenimiento que usa datos de la condición del equipo para anticipar problemas"), ("vida útil", "tiempo durante el cual un equipo funciona bien"), ("bloqueo y etiquetado", "medida que impide que un equipo se energice mientras alguien trabaja en él; la aplica personal autorizado"), ("parámetros del fabricante", "valores correctos de funcionamiento que indica el manual")],
    worked=[
        ("Costo anual del preventivo", "Un plan de ejemplo pide 3 mantenciones al año a $40.000 cada una. ¿Cuánto cuesta al año?", ["Se multiplica el número de mantenciones por su costo.", "3 por 40.000 son 120.000."], "$120.000"),
        ("Tipo de mantenimiento", "Un equipo de ejemplo se detiene y se llama a un técnico para repararlo. ¿Qué tipo de mantenimiento es?", ["Se hace después de la falla.", "Es mantenimiento correctivo."], "Correctivo"),
    ],
    mistakes=[("Pensar que si un equipo no falla no necesita mantención.", "Las fallas aparecen cuando el desgaste ya avanzó.", "Programa el preventivo según el manual."),
              ("Intervenir un equipo en marcha «solo un minuto».", "Hay riesgo de descarga o de partes que giran.", "Asegura el equipo con personal autorizado antes de intervenir.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es el mantenimiento preventivo?", "El que se programa y se hace antes de que ocurra una falla", "El que se hace después de que el equipo se detiene", "El que se hace solo cuando el cliente reclama", "Preventivo significa anticiparse a la falla con trabajo programado."),
        ("abc", "¿Qué es el mantenimiento correctivo?", "El que se hace después de que el equipo falla", "El que se programa para evitar una falla", "El que usa datos de consumo para anticipar problemas", "El correctivo responde a una falla ya ocurrida."),
        ("abc", "¿Para qué se usa el bloqueo y etiquetado?", "Para impedir que un equipo se energice mientras alguien trabaja en él", "Para marcar los equipos que ya fueron pagados", "Para identificar el color de los cables", "El bloqueo y etiquetado evita que se energice el equipo mientras se interviene."),
        ("=", "{F} ¿Cuánto cuestan al año las mantenciones preventivas del plan?", "2*60000", "Se multiplica el número de mantenciones por su costo.", " pesos"),
        ("=", "{F} Si en un año ocurren 2 reparaciones correctivas, ¿cuánto cuestan?", "2*350000", "Se multiplica el número de reparaciones por su costo.", " pesos"),
        ("=", "{F} ¿Cuánto más cuestan las 2 reparaciones correctivas que las mantenciones preventivas del año?", "2*350000-2*60000", "Se resta el costo anual del preventivo del costo de las reparaciones.", " pesos"),
        ("abc", "{F} ¿Qué tipo de mantenimiento es el que se hace cuando la vitrina ya dejó de enfriar?", "Correctivo", "Preventivo", "Predictivo", "Se hace después de la falla, por lo que es correctivo."),
        ("abc", "{F} Un ayudante quiere limpiar una pieza del equipo en marcha «solo un minuto». ¿Qué corresponde?", "No hacerlo: se interviene con el equipo asegurado por personal autorizado", "Hacerlo con guantes", "Hacerlo si el cliente está presente", "Ni los guantes ni la presencia del cliente reemplazan asegurar el equipo."),
        ("abc", "{F} ¿Qué logra el mantenimiento preventivo?", "Reducir fallas, consumo y riesgos antes de que ocurran", "Eliminar para siempre la necesidad de reparar", "Reemplazar el manual del fabricante", "El preventivo anticipa problemas; no los elimina para siempre."),
        ("abc", "{F} Un cliente dice: «si no está fallando, no hace falta mantenerlo». ¿Qué respuesta es correcta?", "El desgaste avanza aunque no haya falla; el preventivo busca evitarla", "Tiene razón: solo se mantiene lo que falla", "Tiene razón si el equipo es nuevo", "El desgaste existe antes de la falla; el preventivo se hace por eso."),
        ("=", "{F} Si el preventivo evita una de las 2 reparaciones correctivas, ¿cuánto cuesta el año (2 preventivas y 1 correctiva)?", "2*60000+350000", "Se suman las dos mantenciones preventivas y la reparación correctiva que queda.", " pesos"),
        ("=", "{F} Comparando 2 correctivas sin preventivo con el caso de 2 preventivas y 1 correctiva, ¿cuánto se ahorra?", "2*350000-(2*60000+350000)", "Se resta el costo con preventivo del costo sin preventivo.", " pesos"),
        ("abc", "Alguien recibe una descarga eléctrica durante una mantención y sigue en contacto con la energía. ¿Qué indican las reglas generales?", "No tocarlo, avisar a un adulto responsable y llamar a emergencias", "Tirar de su ropa para separarlo", "Tocarlo para comprobar si respira", "Tocar a quien sigue en contacto puede transmitir la descarga a quien ayuda."),
    ],
    ctx=("abc", "Una técnica de ejemplo llega a un local y el equipo está funcionando con un ruido anormal. Su compañero quiere abrirlo sin asegurarlo. ¿Qué corresponde?", "Pedir que se asegure el equipo por personal autorizado antes de cualquier intervención", "Abrirlo rápido para revisar el ruido", "Esperar a que el cliente lo abra", "Un equipo en marcha no se abre; se asegura antes de intervenir."),
    sc=[
        ("En Refrigeración: ¿cuándo se hace el mantenimiento preventivo?", "Antes de que ocurra una falla, de forma programada", "Se programa según el manual del fabricante."),
        ("¿Qué impide el bloqueo y etiquetado?", "Que el equipo se energice mientras alguien trabaja", "Esa medida la aplica solo personal autorizado, no cualquier persona."),
        ("En refrigeración: ¿quién interviene un equipo?", "Personal autorizado, con norma vigente y EPP", "Este cuaderno no habilita para trabajar ni para intervenir equipos."),
    ],
    op=("Datos de ejemplo del «Local Calafate» (ficticio): una mantención preventiva cuesta $50.000; una reparación correctiva, $280.000; el plan pide 3 preventivas al año. "
        "Escribe (a) el costo anual del plan preventivo, (b) el costo de 2 correctivas, (c) cuánto cuesta el año con el plan preventivo y 1 correctiva, (d) qué se asegura antes de intervenir un equipo y quién lo hace.",
        "(a) 3 por 50.000 son 150.000. (b) 2 por 280.000 son 560.000. (c) 150.000 más 280.000 son 430.000 pesos. (d) Se asegura que el equipo no pueda energizarse por error (bloqueo y etiquetado) y lo hace personal autorizado.",
        ["calcula el costo del plan", "calcula las correctivas", "suma el año con preventivo", "nombra el aseguramiento y quién lo aplica"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por el número de visitas", "decir que cualquiera asegura el equipo", "intervenir en marcha"],
        "Pregunta: «¿qué impide el bloqueo y etiquetado?». Si no responde, pídele que relea el párrafo de riesgos."),
    reinforce="Escribe los tres tipos de mantenimiento y un ejemplo inventado de cada uno.",
    extend="Explica con un ejemplo por qué una mantención programada puede costar menos que una reparación de emergencia.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (plan de mantención de ejemplo, inventado, para un equipo). Tarea / cada cuántos meses / duración: revisión de filtros / 3 / 1 h; revisión general / 6 / 3 h; limpieza de los componentes de intercambio de calor / 12 / 4 h; "
     "revisión del registro de refrigerante en la bitácora / 4 / 1 h. Parámetro del manual de ejemplo: ΔT entre 6 y 10 °C. Costo de la hora de trabajo de ejemplo: $12.000.")
build(
    O8, 2, F,
    use="Aprenderé qué documentos ordenan el mantenimiento: plan, orden de trabajo, hoja de vida y bitácora, y a calcular tareas y horas de un plan.",
    prior=["Sé qué es una bitácora.", "Sé qué es un manual del fabricante.", "Sé dividir y multiplicar."],
    explain=[
        "El plan de mantención es una lista de tareas con su frecuencia, es decir, cada cuánto tiempo se repiten, y su duración. Se arma a partir del manual del fabricante, que fija los parámetros y los intervalos. La orden de trabajo (OT) es el documento que encarga una tarea concreta a una persona, con fecha, equipo y firma al terminar. La hoja de vida del equipo reúne sus datos, sus mantenciones y sus fallas, y ayuda a decidir qué hacer. Un repuesto es una pieza de reemplazo, y el stock es la cantidad que hay disponible.",
        "Sin una orden de trabajo firmada no hay constancia de que una tarea se hizo. El cumplimiento del plan es el porcentaje de tareas realizadas respecto de las programadas. El intervalo de una tarea no lo cambia quien la ejecuta: lo modifica quien responde del plan, con respaldo del manual. Este cuaderno trabaja con tareas descritas por su nombre; no explica cómo se ejecutan, porque eso lo hace personal autorizado.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("plan de mantención", "lista de tareas con su frecuencia y duración"), ("orden de trabajo (OT)", "documento que encarga una tarea concreta, con fecha, equipo y firma al terminar"), ("hoja de vida del equipo", "documento que reúne datos, mantenciones y fallas de un equipo"), ("repuesto", "pieza de reemplazo"), ("stock", "cantidad de repuestos disponibles"), ("cumplimiento del plan", "porcentaje de tareas realizadas respecto de las programadas")],
    worked=[
        ("Veces al año", "Una tarea de ejemplo se repite cada 4 meses. ¿Cuántas veces se hace en un año?", ["Un año tiene 12 meses.", "12 dividido por 4 son 3."], "3 veces"),
        ("Porcentaje de cumplimiento", "Un plan de ejemplo programa 20 tareas y se realizan 15. ¿Qué cumplimiento es?", ["15 dividido por 20 es 0,75.", "Multiplicado por 100 es 75 %."], "75 %"),
    ],
    mistakes=[("Alargar el intervalo de una tarea «para ahorrar».", "El intervalo lo fija el manual y puede evitar fallas.", "Consulta a quien responde del plan."),
              ("Dar por hecha una tarea sin orden de trabajo firmada.", "No queda constancia de que se hizo.", "Exige la orden firmada al terminar.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es un plan de mantención?", "Una lista de tareas con su frecuencia y su duración", "Una lista de los repuestos que hay en bodega", "El historial de fallas de un equipo", "El plan ordena las tareas en el tiempo; los repuestos y fallas se registran en otros documentos."),
        ("abc", "¿Qué es la hoja de vida de un equipo?", "El documento que reúne sus datos, sus mantenciones y sus fallas", "La lista de tareas programadas del año", "El contrato con el cliente", "La hoja de vida acumula el historial de un equipo para decidir qué hacer."),
        ("abc", "¿Qué es una orden de trabajo?", "El documento que encarga una tarea concreta, con fecha, equipo y firma al terminar", "El permiso para cobrar la tarea", "La lista de precios de los repuestos", "La orden encarga y deja constancia de una tarea concreta."),
        ("=", "{F} ¿Cuántas veces al año se revisan los filtros?", "12//3", "Se divide el año en meses por el intervalo de la tarea.", " veces"),
        ("=", "{F} ¿Cuántas tareas del plan se programan en total en un año (sumando todas las repeticiones)?", "12//3+12//6+12//12+12//4", "Se suman las veces al año de cada tarea.", " tareas"),
        ("=", "{F} ¿Cuántas horas de trabajo suma el plan en un año?", "12//3*1+12//6*3+12//12*4+12//4*1", "Se multiplica cada tarea por su duración y sus repeticiones y se suman.", " horas"),
        ("=", "{F} ¿Cuánto cuesta la mano de obra del plan en un año?", "(12//3*1+12//6*3+12//12*4+12//4*1)*12000", "Se multiplican las horas anuales por el costo de la hora.", " pesos"),
        ("abc", "{F} ¿De dónde se toman los valores de referencia, como el ΔT, para mantener el equipo?", "Del manual del fabricante", "De la memoria del técnico", "De un equipo parecido de otra marca", "Los valores correctos los fija el fabricante en su manual."),
        ("abc", "{F} Un técnico propone alargar el intervalo de los filtros de 3 a 6 meses «para ahorrar». ¿Qué corresponde?", "No cambiarlo por cuenta propia: lo fija el manual y lo modifica quien responde del plan", "Cambiarlo si el cliente está de acuerdo", "Cambiarlo si los filtros se ven limpios", "El intervalo es parte del plan y solo lo modifica quien responde de él."),
        ("abc", "{F} Una tarea figura como hecha, pero no hay orden de trabajo firmada. ¿Qué problema hay?", "No hay constancia de que se hizo", "Ninguno, porque basta con que alguien lo recuerde", "Que la tarea cuesta más", "Sin orden firmada no se puede comprobar que se hizo."),
        ("=", "{F} Se hicieron 8 de las 10 tareas programadas en el período. ¿Qué porcentaje de cumplimiento es?", "8*100//10", "Se divide lo hecho por lo programado y se multiplica por 100.", " %"),
        ("=", "{F} Si el costo de la hora sube de $12.000 a $15.000, ¿cuánto sube el costo anual de mano de obra del plan?", "(12//3*1+12//6*3+12//12*4+12//4*1)*(15000-12000)", "Se multiplican las horas anuales por el alza del costo de la hora.", " pesos"),
        ("abc", "{F} El repuesto de filtros está agotado (stock 0) y el plan pide reemplazarlo pronto. ¿Qué corresponde?", "Informar al supervisor para reponer el repuesto antes de la fecha; no usar uno que no corresponda", "Usar un filtro de otro equipo parecido", "Omitir la tarea sin avisar", "Un repuesto incorrecto o una tarea omitida en silencio generan riesgos y falta de registro."),
    ],
    ctx=("abc", "Una supervisora de ejemplo ve que dos técnicos anotaron la misma tarea en órdenes de trabajo distintas con fechas diferentes. ¿Qué hace?", "Aclara cuál es la orden vigente y deja una sola versión", "Deja ambas sin aclarar", "Borra la más antigua sin consultar", "Dos órdenes contradictorias se aclaran para tener una sola versión vigente."),
    sc=[
        ("En Refrigeración: ¿qué es una orden de trabajo?", "El documento que encarga una tarea concreta y deja constancia al firmarse", "Sin orden firmada no hay constancia."),
        ("¿Cómo se obtiene el número de veces al año de una tarea?", "Dividiendo 12 meses por su intervalo en meses", "Así se calcula cuántas veces se repite."),
        ("¿Quién cambia el intervalo de una tarea del plan?", "Quien responde del plan, con respaldo del manual", "Quien ejecuta no lo cambia por su cuenta."),
    ],
    op=("Plan de ejemplo del «Hotel Maitenes» (ficticio): inspección de filtros cada 2 meses (1 h); revisión general cada 6 meses (3 h); registro en bitácora cada 3 meses (1 h). Hora de trabajo de ejemplo: $10.000. "
        "Escribe (a) cuántas veces al año se hace cada tarea, (b) las horas anuales del plan, (c) el costo anual de mano de obra, (d) qué documento prueba que una tarea se hizo.",
        "(a) Filtros: 12 dividido por 2 son 6; revisión general: 2; bitácora: 4. (b) 6 por 1 más 2 por 3 más 4 por 1 son 16 horas. (c) 16 por 10.000 son 160.000 pesos. (d) La orden de trabajo firmada.",
        ["calcula las veces al año", "calcula las horas", "calcula el costo", "nombra el documento"],
        ["hoja con los cálculos"],
        ["dividir al revés", "olvidar la duración de cada tarea", "decir que basta con recordarlo"],
        "Pregunta: «¿qué prueba que se hizo la tarea?». Si no responde, pídele que relea el papel de la orden de trabajo."),
    reinforce="Inventa un plan con tres tareas, su frecuencia y su duración, y calcula las horas de un año.",
    extend="Explica con un ejemplo por qué la hoja de vida de un equipo ayuda a decidir el próximo mantenimiento.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (calendario de ejemplo, inventado). Tres equipos: A, con visita preventiva cada 3 meses y 2 h por visita; B, cada 6 meses y 3 h por visita; C, cada 6 meses y 4 h por visita. "
     "Hay un solo técnico con jornadas de 8 horas. Costo de la hora de trabajo de ejemplo: $12.000. Estado al cierre del primer semestre: A, 2 visitas programadas y 2 realizadas; B, 1 programada y 1 realizada; C, 1 programada y 0 realizadas.")
build(
    O8, 3, F,
    use="Aprenderé a armar un calendario de mantención, a calcular visitas, horas, jornadas y costos, y a medir el cumplimiento de un semestre.",
    prior=["Sé qué es un plan de mantención.", "Sé calcular veces al año y horas.", "Sé calcular porcentajes."],
    explain=[
        "Un calendario de mantención reparte las visitas del plan en el tiempo. Para cada equipo se calculan las visitas al año dividiendo 12 meses por el intervalo, y las horas multiplicando las visitas por la duración. La suma de las horas indica cuántas jornadas necesita el técnico: se divide por las horas de una jornada y se redondea hacia arriba, porque no se contratan fracciones de jornada. El costo de mano de obra es el total de horas por el costo de la hora.",
        "Al cerrar un período se mide el cumplimiento: las visitas realizadas divididas por las programadas, por 100. Una visita no realizada no se borra: se registra el motivo y se reprograma con una nueva fecha, que aprueba quien responde del plan. Un equipo sin visitas por mucho tiempo acumula riesgo, aunque parezca funcionar bien. Todo queda en la bitácora y en órdenes de trabajo firmadas.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("calendario de mantención", "reparto de las visitas del plan en el tiempo"), ("jornada", "tiempo de trabajo de un día, en este caso 8 horas"), ("reprogramar", "fijar una nueva fecha para una visita que no se realizó"), ("cumplimiento del período", "visitas realizadas divididas por las programadas, por 100"), ("carga de trabajo", "total de horas que demanda un plan")],
    worked=[
        ("Jornadas necesarias", "Un plan de ejemplo suma 20 horas y una jornada tiene 8 horas. ¿Cuántas jornadas se necesitan?", ["20 dividido por 8 da 2 y sobran 4 horas.", "Se redondea hacia arriba: 3 jornadas."], "3 jornadas"),
        ("Cumplimiento del período", "En un semestre de ejemplo se programaron 5 visitas y se hicieron 4. ¿Qué cumplimiento es?", ["4 dividido por 5 es 0,8.", "Multiplicado por 100 es 80 %."], "80 %"),
    ],
    mistakes=[("Borrar del calendario una visita que no se hizo.", "Se pierde el registro del atraso y del riesgo acumulado.", "Registra el motivo y reprograma con nueva fecha."),
              ("Redondear hacia abajo las jornadas necesarias.", "Quedarían horas de trabajo sin cubrir.", "Redondea hacia arriba.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es reprogramar una visita?", "Fijar una nueva fecha para una visita que no se realizó", "Cancelarla definitivamente", "Cobrarla dos veces", "Reprogramar mantiene la visita en el plan con una nueva fecha."),
        ("abc", "¿Qué mide el cumplimiento de un período?", "Las visitas realizadas respecto de las programadas", "El costo de las visitas respecto del presupuesto", "La cantidad de equipos de un cliente", "El cumplimiento compara lo realizado con lo programado."),
        ("abc", "¿Por qué se registra el motivo de una visita no realizada?", "Porque permite entender el atraso y decidir cómo reprogramar", "Porque es un requisito del manual de cocina", "Porque así el equipo no necesita mantención", "Registrar el motivo deja constancia y ayuda a decidir qué hacer."),
        ("=", "{F} ¿Cuántas visitas al año tiene el equipo A?", "12//3", "Se divide el año en meses por el intervalo del equipo.", " visitas"),
        ("=", "{F} ¿Cuántas visitas al año suman los tres equipos?", "12//3+12//6+12//6", "Se suman las visitas anuales de A, B y C.", " visitas"),
        ("=", "{F} ¿Cuántas horas de trabajo suma el calendario en un año?", "12//3*2+12//6*3+12//6*4", "Se multiplican las visitas de cada equipo por su duración y se suman.", " horas"),
        ("=", "{F} ¿Cuánto cuesta la mano de obra anual del calendario?", "(12//3*2+12//6*3+12//6*4)*12000", "Se multiplican las horas anuales por el costo de la hora.", " pesos"),
        ("=", "{F} ¿Cuántas jornadas de 8 horas necesita el técnico en el año, redondeando hacia arriba?", "(22+7)//8", "Se divide el total de 22 horas por 8, redondeando hacia arriba.", " jornadas"),
        ("=", "{F} ¿Qué porcentaje de las visitas programadas del primer semestre se realizó?", "3*100//4", "Se suman las 3 visitas realizadas, se dividen por las 4 programadas y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué visita del primer semestre no se realizó?", "La del equipo C", "La del equipo B", "Las de los equipos A y B", "La ficha indica 1 programada y 0 realizadas para C."),
        ("abc", "{F} Un técnico dice que la visita de C «no importa» porque el equipo funciona. ¿Qué responde el supervisor?", "Que se registra el motivo y se reprograma, porque un equipo sin visitas acumula riesgo", "Que se borra la visita del calendario", "Que se espera a que falle", "Un equipo que funciona igual necesita su preventivo; se reprograma con registro."),
        ("=", "{F} Se agrega un equipo D con 2 visitas al año de 3 horas cada una. ¿Cuántas horas anuales suma el calendario?", "22+2*3", "Se suman a las 22 horas anuales las horas del equipo D.", " horas"),
        ("abc", "{F} Dos órdenes de trabajo del mismo equipo tienen la misma fecha y distinto contenido. ¿Qué corresponde?", "Aclararlo con el supervisor y dejar una sola versión vigente", "Usar la que tenga la letra más legible", "Hacer ambas tareas sin consultar", "Dos documentos contradictorios se aclaran con quien responde del plan."),
    ],
    ctx=("abc", "Una jefa de mantención de ejemplo recibe una visita no realizada porque el técnico se enfermó. ¿Qué hace?", "Registra el motivo y reprograma la visita con una nueva fecha", "Borra la visita para que no figure atrasada", "Marca la visita como realizada", "Marcar como hecha una visita que no se hizo es adulterar un registro."),
    sc=[
        ("En Refrigeración: ¿cómo se obtienen las jornadas necesarias?", "Dividiendo las horas por las de una jornada y redondeando hacia arriba", "No se contratan fracciones de jornada."),
        ("¿Cómo se mide el cumplimiento de un período?", "Realizadas dividido por programadas, por 100", "Así se compara lo hecho con lo previsto."),
        ("¿Qué se hace con una visita que no se realizó?", "Se registra el motivo y se reprograma", "No se borra ni se marca como hecha."),
    ],
    op=("Calendario de ejemplo de la «Sala Laurel» (ficticia): equipo P, visita cada 4 meses de 2 horas; equipo Q, cada 6 meses de 3 horas. Jornada de 8 horas; hora de trabajo $10.000. Primer semestre: P, 1 programada y 1 realizada; Q, 1 programada y 0 realizadas. "
        "Escribe (a) las visitas anuales de cada equipo, (b) las horas anuales y su costo, (c) el cumplimiento del semestre y (d) qué haces con la visita de Q.",
        "(a) P: 12 dividido por 4 son 3; Q: 2. (b) 3 por 2 más 2 por 3 son 12 horas; 12 por 10.000 son 120.000 pesos. (c) 1 de 2 es 50 %. (d) Registro el motivo y reprogramo la visita con una nueva fecha.",
        ["calcula las visitas anuales", "calcula horas y costo", "calcula el cumplimiento", "registra y reprograma"],
        ["hoja con los cálculos"],
        ["dividir al revés", "borrar la visita no realizada", "olvidar el costo"],
        "Pregunta: «¿qué haces con la visita de Q?». Si no responde, pídele que relea la regla de reprogramar con registro."),
    reinforce="Inventa un calendario con dos equipos y calcula las horas anuales y las jornadas necesarias.",
    extend="Explica con un ejemplo por qué una visita sin hacer no debe aparecer como realizada.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). Un equipo tiene 8 años de antigüedad y una vida útil esperada de ejemplo de 10 años. Costo de reemplazo: $1.200.000. Reparación correctiva propuesta: $700.000. "
     "Costo anual de la mantención preventiva: $120.000. Criterio de ejemplo de la empresa: se recomienda reemplazar si el costo de la reparación supera el 50 % del costo de reemplazo. "
     "Disponibilidad = horas en que el equipo estuvo disponible dividido por las horas del período, por 100; en un mes de 720 horas estuvo disponible 648 horas.")
build(
    O8, 4, F,
    use="Aprenderé a decidir con datos entre reparar o reemplazar un equipo, a calcular el costo por año de vida útil y la disponibilidad.",
    prior=["Sé calcular porcentajes.", "Sé qué es la vida útil.", "Sé comparar costos."],
    explain=[
        "Cuando un equipo falla hay que decidir si se repara o se reemplaza. Un criterio común compara el costo de la reparación con una parte del costo de reemplazo: si la supera, se recomienda reemplazar. Además se mira la vida útil restante, que es la vida útil esperada menos la antigüedad. El costo por año de vida útil se obtiene dividiendo el costo entre los años que se espera obtener del equipo; permite comparar opciones que duran distinto tiempo.",
        "La disponibilidad mide qué parte del tiempo el equipo estuvo listo para funcionar: horas disponibles dividido por horas del período, por 100. Es un indicador del servicio que da el mantenimiento. La decisión final la toma quien responde del plan, con el informe y el cliente; quien ejecuta no decide solo. Los valores de este caso son de ejemplo y sirven para calcular en planilla.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("costo de reemplazo", "costo de comprar e instalar un equipo nuevo"), ("vida útil restante", "vida útil esperada menos la antigüedad"), ("costo por año de vida útil", "costo dividido entre los años que se espera obtener del equipo"), ("disponibilidad", "horas disponibles dividido por las horas del período, por 100"), ("criterio de reemplazo", "regla que compara el costo de reparar con el de reemplazar")],
    worked=[
        ("Aplicar el criterio", "Con un criterio de ejemplo del 50 %, un equipo cuyo reemplazo cuesta $800.000 tiene una reparación de $300.000. ¿Se recomienda reemplazar?", ["El 50 % de 800.000 es 400.000.", "300.000 no supera 400.000: se recomienda reparar."], "No: se recomienda reparar"),
        ("Costo por año", "Una reparación de ejemplo cuesta $400.000 y el equipo durará 4 años más. ¿Cuánto cuesta por año de vida útil?", ["Se divide el costo entre los años.", "400.000 dividido por 4 son 100.000."], "$100.000 por año"),
    ],
    mistakes=[("Reparar siempre porque la reparación cuesta menos que un equipo nuevo.", "Puede costar más por año de vida útil.", "Compara el criterio y el costo por año."),
              ("Decidir solo, sin informar a quien responde del plan.", "La decisión requiere el informe y la aprobación.", "Informa y espera la decisión.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es la vida útil restante de un equipo?", "La vida útil esperada menos su antigüedad", "La antigüedad sumada a la vida útil esperada", "El tiempo que falta para el próximo preventivo", "La vida útil restante es lo que queda: vida útil esperada menos antigüedad."),
        ("abc", "¿Qué mide la disponibilidad de un equipo?", "La parte del tiempo en que estuvo listo para funcionar", "El gasto de energía por hora", "La cantidad de repuestos en bodega", "La disponibilidad compara horas disponibles con horas del período."),
        ("abc", "¿Qué es un criterio de reemplazo?", "Una regla que compara el costo de reparar con el de reemplazar", "El permiso para botar un equipo", "El precio de un equipo nuevo", "El criterio es una regla de decisión, no un permiso ni un precio."),
        ("=", "{F} ¿A cuánto equivale el 50 % del costo de reemplazo?", "1200000*50//100", "Se calcula el 50 % del costo de reemplazo.", " pesos"),
        ("abc", "{F} Según el criterio de ejemplo, ¿qué se recomienda?", "Reemplazar, porque la reparación supera el 50 % del costo de reemplazo", "Reparar, porque cuesta menos que el reemplazo", "No hacer nada", "La reparación de $700.000 supera los $600.000 del 50 %."),
        ("=", "{F} ¿Cuánto supera la reparación al 50 % del costo de reemplazo?", "700000-1200000*50//100", "Se resta el 50 % del costo de reemplazo del costo de la reparación.", " pesos"),
        ("=", "{F} ¿Cuántos años de vida útil le quedan al equipo?", "10-8", "Se resta la antigüedad de la vida útil esperada.", " años"),
        ("=", "{F} ¿Qué porcentaje de disponibilidad tuvo el equipo en el mes?", "648*100//720", "Se divide las horas disponibles entre las del período y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas horas no estuvo disponible el equipo en el mes?", "720-648", "Se resta las horas disponibles de las horas del mes.", " horas"),
        ("abc", "{F} Un compañero dice: «como la reparación cuesta menos que el equipo nuevo, siempre conviene reparar». ¿Qué respuesta es correcta?", "No siempre: el criterio compara con el 50 % del reemplazo y también cuenta la vida útil restante", "Tiene razón: lo más barato siempre conviene", "Tiene razón si el equipo está en garantía", "La reparación supera el límite del criterio y deja poca vida útil."),
        ("=", "{F} ¿Cuánto cuesta por año de vida útil restante la reparación de $700.000?", "700000//2", "Se divide el costo de la reparación entre los 2 años que le quedan al equipo.", " pesos"),
        ("=", "{F} Si el equipo nuevo cumpliera su vida útil esperada de 10 años, ¿cuánto cuesta por año de vida útil?", "1200000//10", "Se divide el costo de reemplazo entre los 10 años de vida útil.", " pesos"),
        ("abc", "{F} ¿Quién toma la decisión final de reparar o reemplazar?", "Quien responde del plan de mantención, con el informe y el cliente", "El técnico que hizo la inspección, sin consultar", "El primero que lea el informe", "La decisión corresponde a quien responde del plan; el técnico informa."),
    ],
    ctx=("abc", "Un cliente de ejemplo quiere reparar un equipo viejo «para no gastar», aunque el costo por año de vida útil es mucho mayor que el de uno nuevo. ¿Qué hace la supervisora?", "Le presenta la comparación de costos por año y la decisión queda registrada", "Repara sin explicar nada", "Reemplaza el equipo sin consultar", "Una decisión informada se apoya en datos y se registra."),
    sc=[
        ("En Refrigeración: ¿cómo se calcula el costo por año de vida útil?", "Dividiendo el costo entre los años de vida útil", "Permite comparar opciones que duran distinto tiempo."),
        ("En refrigeración: ¿cómo se calcula la disponibilidad?", "Horas disponibles dividido por horas del período, por 100", "Mide el servicio que entrega el equipo."),
        ("¿Quién decide reparar o reemplazar?", "Quien responde del plan, con el informe", "El técnico informa y no decide solo."),
    ],
    op=("Datos de ejemplo del «Local Arrayán» (ficticio): costo de reemplazo $900.000; reparación propuesta $500.000; criterio: reemplazar si la reparación supera el 50 % del reemplazo; antigüedad 6 años; vida útil esperada 10 años; en un mes de 720 horas estuvo disponible 576 horas. "
        "Escribe (a) el 50 % del costo de reemplazo y qué se recomienda, (b) la vida útil restante, (c) el costo por año de la reparación, (d) la disponibilidad del mes.",
        "(a) El 50 % de 900.000 son 450.000; como 500.000 lo supera, se recomienda reemplazar. (b) 10 menos 6 son 4 años. (c) 500.000 dividido por 4 son 125.000 pesos por año. (d) 576 por 100 dividido por 720 son 80 %.",
        ["calcula el 50 % y aplica el criterio", "calcula la vida útil restante", "calcula el costo por año", "calcula la disponibilidad"],
        ["hoja con los cálculos"],
        ["comparar con el costo completo en vez del 50 %", "dividir al revés", "olvidar multiplicar por 100"],
        "Pregunta: «¿contra qué valor comparas la reparación?». Si no responde, pídele que relea el criterio de reemplazo."),
    reinforce="Inventa un equipo con costo de reemplazo y de reparación, y aplica un criterio del 50 %.",
    extend="Explica con un ejemplo por qué el costo por año de vida útil ayuda a comparar reparar y reemplazar.",
)

# ============================================================ OAE-09, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Un taller ficticio, «Frío Sur», recibe 3 equipos fuera de uso. Las placas indican cargas nominales de ejemplo de 2 kg, 3 kg y 5 kg de refrigerante. "
     "Reglas generales: el refrigerante lo recupera un técnico certificado, se guarda en contenedores aprobados y nunca se libera al ambiente. Riesgos anotados: presión alta, congelación al contacto con la piel, "
     "desplazamiento del aire respirable en espacios cerrados, incendio en algunos fluidos y contaminación.")
build(
    O9, 1, F,
    use="Aprenderé qué significan recuperar, reciclar, regenerar y destruir un refrigerante, por qué no se libera al ambiente y quién puede manejarlo.",
    prior=["Sé qué es un refrigerante y sus riesgos.", "Sé qué es un técnico certificado.", "Sé qué es el PCG."],
    explain=[
        "Al terminar la vida de un equipo o al intervenirlo, el refrigerante no se suelta al ambiente. Recuperar es retirar el refrigerante de un equipo y guardarlo en un contenedor sin procesarlo. Reciclar es limpiarlo de forma básica para volver a usarlo. Regenerar es reprocesarlo en una planta autorizada hasta que cumple una calidad definida. Destruir es eliminarlo con un proceso autorizado cuando no puede reutilizarse. El contenedor aprobado es el recipiente que la norma vigente acepta para guardar refrigerante, y debe llevar su etiqueta.",
        "Estas tareas las realiza un técnico certificado, con los equipos y contenedores apropiados y con EPP, según la norma de buenas prácticas vigente. Liberar refrigerante daña el medio ambiente y está regulado. Los riesgos son los mismos de cualquier refrigerante: presión alta, congelación y desplazamiento del aire respirable en espacios cerrados. Este cuaderno no explica cómo recuperar: solo conceptos y reglas generales de seguridad.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("recuperar", "retirar el refrigerante de un equipo y guardarlo en un contenedor sin procesarlo"), ("reciclar", "limpiar de forma básica el refrigerante recuperado para volver a usarlo"), ("regenerar", "reprocesar el refrigerante en una planta autorizada hasta una calidad definida"), ("destruir", "eliminar el refrigerante con un proceso autorizado"), ("contenedor aprobado", "recipiente que la norma vigente acepta para guardar refrigerante"), ("carga nominal", "cantidad de refrigerante que indica la placa del equipo")],
    worked=[
        ("Suma de cargas", "Tres equipos de ejemplo tienen cargas nominales de 1 kg, 4 kg y 2 kg. ¿Cuántos kg suman?", ["Se suman las cargas de los tres equipos.", "1 más 4 más 2 son 7."], "7 kg"),
        ("Elegir el término", "Un refrigerante de ejemplo se retira de un equipo y se guarda en un contenedor sin procesarlo. ¿Cómo se llama esta acción?", ["No se limpia ni se reprocesa.", "Se llama recuperar."], "Recuperar"),
    ],
    mistakes=[("Dejar escapar «lo poco que queda» de un equipo fuera de uso.", "Daña el medio ambiente y la norma vigente lo regula.", "Avisa a un adulto responsable; lo recupera un técnico certificado."),
              ("Confundir recuperar con reciclar.", "Recuperar es retirar y guardar; reciclar es limpiar para reutilizar.", "Relaciona cada término con lo que se hace al fluido.")],
    T=[
        ("abc", "En Refrigeración: ¿qué significa recuperar un refrigerante?", "Retirarlo de un equipo y guardarlo en un contenedor sin procesarlo", "Limpiarlo de forma básica para volver a usarlo", "Eliminarlo con un proceso autorizado", "Recuperar es retirar y guardar; limpiarlo es reciclar y eliminarlo es destruir."),
        ("abc", "¿Qué significa reciclar un refrigerante?", "Limpiarlo de forma básica para volver a usarlo", "Retirarlo del equipo y guardarlo sin procesarlo", "Reprocesarlo en una planta hasta una calidad definida", "Reciclar es una limpieza básica para reutilizar; regenerar es el reproceso en planta."),
        ("abc", "¿Qué significa regenerar un refrigerante?", "Reprocesarlo en una planta autorizada hasta cumplir una calidad definida", "Soltarlo al ambiente en pequeñas cantidades", "Cambiarle la etiqueta al contenedor", "Regenerar es reprocesar hasta una calidad definida, en una planta autorizada."),
        ("=", "{F} ¿Cuántos kg de carga nominal suman los tres equipos?", "2+3+5", "Se suman las tres cargas nominales de las placas.", " kg"),
        ("abc", "{F} ¿Quién recupera el refrigerante de los equipos?", "Un técnico certificado, con equipos y contenedores apropiados", "Cualquier ayudante del taller", "El cliente que trajo los equipos", "La recuperación exige certificación; el ayudante o el cliente no están habilitados."),
        ("abc", "{F} ¿Por qué no se libera el refrigerante al ambiente?", "Porque daña el medio ambiente y la norma vigente lo regula", "Porque el refrigerante se vuelve más caro", "Porque se necesita más espacio en el taller", "La liberación daña el ambiente y está regulada por la norma vigente."),
        ("=", "{F} La recuperación de cada equipo toma 2 horas de ejemplo y el técnico certificado cobra $30.000 por hora de ejemplo. ¿Cuánto cuesta recuperar los 3 equipos?", "3*2*30000", "Se multiplican los equipos, las horas por equipo y el valor por hora.", " pesos"),
        ("abc", "{F} Un ayudante propone dejar escapar «lo poco que queda» del equipo más pequeño. ¿Qué corresponde?", "No hacerlo: lo recupera un técnico certificado y nunca se libera al ambiente", "Hacerlo si es menos de un kilo", "Hacerlo si hay ventilación en el taller", "No existe una cantidad pequeña aceptable para liberar; la norma exige recuperar."),
        ("=", "{F} Se recuperaron 9 kg de los 10 kg de carga nominal total. ¿Cuántos kg de diferencia hay que explicar en el registro?", "10-9", "Se resta lo recuperado de la carga nominal total.", " kg"),
        ("abc", "{F} Un compañero propone anotar 10 kg recuperados para que el registro «cuadre». ¿Qué respuesta es correcta?", "No: anotar un dato falso es adulterar el registro; se informa la diferencia", "Sí: así el registro queda completo", "Sí, si el supervisor no pregunta", "El registro debe reflejar lo real; la diferencia se investiga, no se tapa."),
        ("abc", "{F} Un técnico se siente mal cerca de los contenedores y hay un olor extraño. ¿Qué indican las reglas generales?", "No entrar ni tocar, avisar a un adulto responsable y llamar a emergencias", "Entrar a ayudarlo sin protección", "Esperar a que se le pase antes de avisar", "Entrar sin protección sumaría más afectados; se avisa de inmediato."),
        ("=", "{F} Si cada kg de refrigerante fugado equivale a 400 kg de dióxido de carbono (índice de ejemplo), ¿cuánto equivalen 3 kg fugados?", "3*400", "Se multiplican los kg por el índice de calentamiento global de ejemplo.", " kg"),
        ("abc", "{F} El cliente pide rellenar un contenedor que no tiene etiqueta. ¿Qué corresponde?", "No usar contenedores sin etiqueta ni aprobación y avisar al supervisor", "Rellenarlo y etiquetarlo después", "Rellenarlo si parece limpio", "Un contenedor sin etiqueta o sin aprobación no se usa."),
    ],
    ctx=("abc", "Una joven de ejemplo en práctica ve que un técnico suelta refrigerante de un equipo viejo para «vaciarlo rápido». ¿Qué corresponde?", "No participar y avisar al supervisor o a un adulto responsable", "Ayudar para terminar antes", "Grabar un video y subirlo a redes", "Soltar refrigerante daña el ambiente y la norma lo prohíbe; se avisa a quien tiene autoridad."),
    sc=[
        ("En Refrigeración: ¿qué es recuperar un refrigerante?", "Retirarlo del equipo y guardarlo en un contenedor sin procesarlo", "Es el primer paso antes de reciclar, regenerar o destruir."),
        ("¿Quién recupera el refrigerante?", "Un técnico certificado, según la norma vigente", "Este cuaderno no habilita para trabajar ni para intervenir equipos."),
        ("¿Qué se hace ante una fuga o una persona afectada?", "No entrar ni tocar, avisar a un adulto responsable y a emergencias", "Nunca se improvisa ante una fuga."),
    ],
    op=("Caso de ejemplo del taller «Hielo Sur» (ficticio): llegan 2 equipos fuera de uso con cargas nominales de 4 kg y 6 kg. Se recuperaron 9 kg en total. El técnico certificado cobra $28.000 por hora de ejemplo y cada recuperación toma 2 horas. "
        "Escribe (a) los kg de carga nominal total, (b) cuántos kg de diferencia hay que explicar, (c) cuánto cuesta recuperar los 2 equipos, (d) qué haces con la diferencia de kg.",
        "(a) 4 más 6 son 10 kg. (b) 10 menos 9 es 1 kg. (c) 2 por 2 por 28.000 son 112.000 pesos. (d) La informo al supervisor para investigarla y no cambio el registro para que cuadre.",
        ["suma las cargas", "calcula la diferencia", "calcula el costo", "informa en vez de ajustar"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "anotar un dato falso", "decir que dejaría escapar el resto"],
        "Pregunta: «¿qué haces con 1 kg de diferencia?». Si no responde, pídele que relea la regla de no adulterar registros."),
    reinforce="Escribe los cuatro destinos de un refrigerante (recuperar, reciclar, regenerar y destruir) con una frase para cada uno.",
    extend="Explica con un ejemplo por qué recuperar es mejor que dejar escapar el refrigerante de un equipo viejo.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 2 (hoja de trazabilidad de ejemplo, inventada). Columnas: fecha, equipo, kg recuperados, técnico, contenedor. Fila 1: 05/03, E1, 2 kg, técnico T1, contenedor C1. Fila 2: 05/03, E2, 3 kg, técnico T1, contenedor C1. "
     "Fila 3: 06/03, E3, 5 kg, técnico sin anotar, contenedor C2.")
build(
    O9, 2, F,
    use="Aprenderé qué es la trazabilidad de un refrigerante, qué documentos la respaldan y cómo se detectan campos faltantes en una hoja.",
    prior=["Sé qué es recuperar un refrigerante.", "Sé qué es un registro.", "Sé sumar."],
    explain=[
        "La trazabilidad es la posibilidad de saber de dónde vino un refrigerante, quién lo recuperó, cuándo, cuánto era y dónde está. Se logra con documentos: la hoja de trazabilidad anota por cada recuperación la fecha, el equipo, los kg, el técnico y el contenedor; la etiqueta del contenedor identifica su contenido y el responsable; y el documento de transporte acompaña los traslados. Un contenedor aprobado es el único lugar donde se guarda el fluido recuperado.",
        "Una hoja completa tiene todos sus campos llenos. Si falta un dato, no se inventa: se consulta a quien lo sabe y se completa con su firma. Rellenar un campo con un dato supuesto es adulterar el registro. La hoja debe completarse antes de mover los contenedores, para que el destino de cada kilo quede escrito. La norma vigente define qué registros deben conservarse; este cuaderno solo trabaja con planillas de ejemplo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("trazabilidad", "posibilidad de saber de dónde vino un refrigerante, quién lo recuperó, cuándo, cuánto era y dónde está"), ("hoja de trazabilidad", "documento donde cada recuperación queda anotada con sus datos"), ("etiqueta del contenedor", "rótulo que identifica el contenido y al responsable"), ("documento de transporte", "documento que acompaña el traslado e identifica contenido, origen y destino"), ("campo", "casilla de una hoja donde se anota un dato")],
    worked=[
        ("Contar filas completas", "Una hoja de ejemplo tiene 4 filas y a 1 le falta el campo técnico. ¿Cuántas filas están completas?", ["Una fila está incompleta.", "4 menos 1 son 3."], "3 filas"),
        ("Kg en un contenedor", "Dos filas de ejemplo, de 2 kg y 4 kg, van al mismo contenedor. ¿Cuántos kg tiene?", ["Se suman los kg de las dos filas.", "2 más 4 son 6."], "6 kg"),
    ],
    mistakes=[("Completar un campo vacío con lo que «seguro fue».", "Un dato supuesto es adulterar el registro.", "Consulta a quien lo sabe y que lo firme."),
              ("Mover los contenedores antes de completar la hoja.", "El destino de cada kilo queda sin registro.", "Completa y revisa la hoja antes de mover.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es la trazabilidad de un refrigerante?", "Poder saber de dónde vino, quién lo recuperó, cuándo, cuánto era y dónde está", "El precio de cada kilo recuperado", "La velocidad con que se recupera", "La trazabilidad sigue el recorrido del fluido; el precio o la velocidad son otros datos."),
        ("abc", "¿Qué es un contenedor aprobado?", "El recipiente que la norma vigente acepta para guardar refrigerante", "Cualquier recipiente que esté vacío", "Un recipiente que el taller prefiere por su color", "Solo los recipientes aceptados por la norma vigente sirven para guardar el fluido."),
        ("abc", "¿Qué debe identificar la etiqueta de un contenedor?", "El contenido y al responsable, según la norma vigente", "El precio y el nombre del cliente", "Solo la fecha de compra del contenedor", "La etiqueta identifica qué contiene y quién responde, no el precio."),
        ("=", "{F} ¿Cuántos kg suma la hoja en total?", "2+3+5", "Se suman los kg de las tres filas.", " kg"),
        ("=", "{F} ¿Cuántos kg tiene el contenedor C1?", "2+3", "Se suman los kg de las filas 1 y 2, que van a C1.", " kg"),
        ("abc", "{F} ¿Qué campo falta en la fila 3?", "El técnico", "La fecha", "El contenedor", "La fila 3 tiene fecha y contenedor, pero el técnico no está anotado."),
        ("=", "{F} ¿Cuántas filas de la hoja están completas?", "3-1", "Se resta del total de filas la que tiene un campo faltante.", " filas"),
        ("abc", "{F} ¿Por qué importa anotar al técnico en cada fila?", "Porque deja constancia de quién es responsable de esa recuperación", "Porque así el técnico cobra más", "Porque el contenedor lo exige por su color", "Quien recuperó el fluido debe quedar identificado para la trazabilidad."),
        ("abc", "{F} Un compañero propone anotar T1 en la fila 3 «porque seguro fue él». ¿Qué respuesta es correcta?", "No: se consulta al responsable; un dato supuesto es adulterar el registro", "Sí: así la hoja queda completa", "Sí, si T1 no se entera", "Un dato supuesto no es un hecho; se consulta y firma quien lo sabe."),
        ("=", "{F} Si por cada kg recuperado se cobra una gestión de ejemplo de $2.500, ¿cuánto se cobra por el total de la hoja?", "10*2500", "Se multiplican los kg totales por el valor de cada kg.", " pesos"),
        ("abc", "{F} En la hoja, el contenedor de la fila 2 se anotó como C2 por error. ¿Qué problema produce?", "Se pierde la trazabilidad: no se sabe en qué contenedor está cada kilo", "Ninguno, porque ambos contenedores son iguales", "Que el técnico debe volver a recuperar el fluido", "Un contenedor mal anotado impide saber dónde está cada kg."),
        ("=", "{F} Cada uno de los 2 contenedores recibió 5 kg del total. ¿Qué porcentaje del total tiene cada contenedor?", "5*100//10", "Se divide lo que tiene un contenedor entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} El supervisor pide completar la hoja antes de mover los contenedores. ¿Cuál es la razón?", "Para que el destino de cada kg quede registrado antes del traslado", "Para que los contenedores pesen menos", "Para ahorrar etiquetas", "Si se mueven antes, el registro del origen y del destino puede perderse."),
    ],
    ctx=("abc", "Una bodeguera de ejemplo recibe un contenedor con una etiqueta ilegible. ¿Qué hace?", "No lo mueve ni lo usa y avisa al supervisor para identificar su contenido", "Lo rotula de nuevo con lo que cree que contiene", "Lo mezcla con otro contenedor etiquetado", "Un contenido sin identificar no se mueve ni se mezcla; se identifica por canales seguros."),
    sc=[
        ("En Refrigeración: ¿qué anota una hoja de trazabilidad?", "Fecha, equipo, kg recuperados, técnico y contenedor", "Así se puede seguir el recorrido del fluido."),
        ("¿Qué se hace con un campo faltante?", "Se consulta a quien lo sabe y se completa con su firma", "Un dato supuesto es adulterar el registro."),
        ("¿Cuándo se completa la hoja?", "Antes de mover los contenedores", "Así el destino de cada kg queda escrito."),
    ],
    op=("Hoja de ejemplo del taller «Cumbre» (ficticio): fila 1, 10/04, equipo F1, 4 kg, técnico T2, contenedor K1; fila 2, 10/04, equipo F2, 6 kg, técnico T2, contenedor K1; fila 3, 11/04, equipo F3, 3 kg, técnico T3, contenedor sin anotar. "
        "Escribe (a) los kg totales de la hoja, (b) los kg del contenedor K1, (c) qué campo falta y qué haces, (d) por qué se completa antes de mover los contenedores.",
        "(a) 4 más 6 más 3 son 13 kg. (b) 4 más 6 son 10 kg. (c) Falta el contenedor de la fila 3; consulto a quien recuperó o a T3 y lo completo con su firma, sin suponerlo. (d) Para que el destino de cada kg quede registrado antes del traslado.",
        ["suma los kg", "suma el contenedor", "detecta el campo faltante y no lo inventa", "explica la razón de completar antes"],
        ["hoja con las cuatro respuestas"],
        ["completar el campo con un dato supuesto", "sumar mal los kg", "mover los contenedores antes"],
        "Pregunta: «¿por qué no escribes el contenedor que supones?». Si no responde, pídele que relea la regla del dato supuesto."),
    reinforce="Inventa una hoja de trazabilidad con tres filas y deja un campo vacío para que otra persona lo detecte.",
    extend="Explica con un ejemplo qué podría pasar si un contenedor no tiene etiqueta ni registro.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 3 (planilla mensual de ejemplo, inventada, de un taller ficticio). Ingresos de refrigerante recuperado: semana 1, 12 kg; semana 2, 8 kg; semana 3, 15 kg; semana 4, 5 kg. "
     "Contenedores llenados registrados: C1, 18 kg; C2, 14 kg; C3, 6 kg. Salidas: 20 kg enviados a regeneración y 18 kg enviados a destrucción, todo desde esos contenedores; al cierre del mes no queda refrigerante almacenado. Índice de calentamiento global de ejemplo: 400.")
build(
    O9, 3, F,
    use="Aprenderé a hacer un balance de masa de un mes: comparar lo que entró con lo que salió o quedó almacenado, y qué hacer con una diferencia.",
    prior=["Sé sumar y restar.", "Sé qué es la trazabilidad.", "Sé qué es el PCG."],
    explain=[
        "El balance de masa compara lo que entró con lo que salió y con lo que quedó almacenado. Si todo se registró bien, lo que entra es igual a lo que sale más lo que queda. Cuando las cifras no coinciden aparece una diferencia no explicada, que se expresa en kg y también como porcentaje del total que entró. La diferencia puede deberse a un error de registro, a una pesada mal hecha o a una pérdida; por eso nunca se «arregla» una cifra para que cuadre.",
        "Ante una diferencia se informa al supervisor, que decide cómo investigarla: revisa las hojas de trazabilidad de cada semana y los pesajes de los contenedores. Mientras no se conozca la causa no se afirma ninguna. Si pudo haber una fuga, se estima su impacto ambiental con el PCG, y se avisa para su revisión por personal autorizado. Los números de este caso son de ejemplo y sirven para calcular en planilla.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("balance de masa", "comparación de lo que entró con lo que salió y con lo que quedó almacenado"), ("diferencia no explicada", "cantidad que no coincide entre lo que entró y lo que salió o quedó"), ("ingreso", "refrigerante recuperado que entra al taller"), ("salida", "refrigerante que sale del taller hacia regeneración o destrucción"), ("pesaje", "medición de la masa de un contenedor")],
    worked=[
        ("Calcular una diferencia", "En un mes de ejemplo entraron 30 kg y salieron 26 kg, sin nada almacenado. ¿Cuál es la diferencia no explicada?", ["Se resta lo que salió de lo que entró.", "30 menos 26 son 4."], "4 kg"),
        ("Porcentaje de la diferencia", "Una diferencia de ejemplo de 3 kg sobre 60 kg que entraron. ¿Qué porcentaje es?", ["3 dividido por 60 es 0,05.", "Multiplicado por 100 es 5 %."], "5 %"),
    ],
    mistakes=[("Sumar kilos a un contenedor para que el balance cuadre.", "Es adulterar el registro y oculta una posible pérdida.", "Informa la diferencia al supervisor."),
              ("Afirmar que la diferencia fue una fuga sin pruebas.", "Puede ser un error de registro o de pesada.", "Presenta la diferencia y pide investigarla.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es un balance de masa?", "Comparar lo que entró con lo que salió y con lo que quedó almacenado", "Pesar el taller completo", "Calcular el costo de los contenedores", "El balance compara entradas con salidas y existencias; no pesa el taller ni calcula costos."),
        ("abc", "¿Qué es una diferencia no explicada?", "Una cantidad que no coincide entre lo que entró y lo que salió o quedó", "Una diferencia de precio entre dos proveedores", "Una diferencia de color entre dos contenedores", "La diferencia no explicada es la cantidad que no cuadra en el balance."),
        ("abc", "¿Qué se hace con una diferencia no explicada?", "Se informa al supervisor para investigarla", "Se suma a un contenedor para que cuadre", "Se borra de la planilla", "Una diferencia se investiga; no se tapa ni se borra."),
        ("=", "{F} ¿Cuántos kg ingresaron en el mes?", "12+8+15+5", "Se suman los ingresos de las cuatro semanas.", " kg"),
        ("=", "{F} ¿Cuántos kg suman los contenedores llenados?", "18+14+6", "Se suman los kg de los tres contenedores.", " kg"),
        ("=", "{F} ¿Cuántos kg suman las salidas?", "20+18", "Se suman los kg enviados a regeneración y a destrucción.", " kg"),
        ("=", "{F} ¿Cuántos kg de diferencia hay entre lo que ingresó y lo que suman los contenedores llenados?", "(12+8+15+5)-(18+14+6)", "Se resta el total de contenedores del total de ingresos.", " kg"),
        ("=", "{F} ¿Qué porcentaje de lo que ingresó es la diferencia?", "((12+8+15+5)-(18+14+6))*100//(12+8+15+5)", "Se divide la diferencia entre el total que ingresó y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Se puede afirmar que la diferencia es una fuga?", "No: puede ser un error de registro o de pesada; hay que investigarla", "Sí: toda diferencia es una fuga", "Sí, si el supervisor lo supone", "Sin pruebas no se afirma una causa; se investiga."),
        ("abc", "{F} Un compañero propone sumar 2 kg a C3 para que el balance cuadre. ¿Qué respuesta es correcta?", "No: sería adulterar el registro; se informa la diferencia", "Sí: así el balance queda perfecto", "Sí, si lo hace antes de que llegue el supervisor", "Un número cambiado para que cuadre oculta una posible pérdida."),
        ("=", "{F} Si la diferencia fuera una fuga del fluido de índice de ejemplo 400, ¿cuántos kg de dióxido de carbono equivaldría?", "((12+8+15+5)-(18+14+6))*400", "Se multiplican los kg de diferencia por el índice de calentamiento global.", " kg"),
        ("=", "{F} ¿Cuántos kg ingresaron en promedio por semana?", "(12+8+15+5)//4", "Se divide el total del mes entre las 4 semanas.", " kg"),
        ("abc", "{F} El supervisor decide investigar la diferencia. ¿Qué revisa primero?", "Las hojas de trazabilidad de cada semana y los pesajes de los contenedores", "El color de los contenedores", "El precio de la regeneración", "La diferencia está en las cifras: se revisan los registros y los pesajes."),
    ],
    ctx=("abc", "Una asistente de ejemplo nota que el balance del mes tiene una diferencia pequeña y piensa en «redondear» las cifras. ¿Qué corresponde?", "No redondear: informar la diferencia exacta al supervisor", "Redondear para que cuadre", "Esperar al mes siguiente a ver si desaparece", "Una diferencia pequeña igual se informa; redondear la oculta."),
    sc=[
        ("En Refrigeración: ¿cómo se calcula la diferencia de un balance de masa?", "Restando lo que salió o quedó almacenado de lo que entró", "Si todo está bien registrado, la diferencia es cero."),
        ("¿Qué se hace con una diferencia no explicada?", "Se informa al supervisor y se investiga", "No se ajustan cifras para que cuadre."),
        ("¿Cómo se estima el impacto ambiental de una posible fuga?", "Multiplicando los kg por el índice de calentamiento global", "Un mayor índice significa más impacto por kg."),
    ],
    op=("Planilla de ejemplo del taller «Alba» (ficticio): ingresos del mes: 15 kg, 20 kg y 5 kg. Contenedores llenados: 20 kg y 18 kg. Salidas: 38 kg, y no queda nada almacenado. Índice de calentamiento global de ejemplo: 300. "
        "Escribe (a) cuántos kg ingresaron y cuántos suman los contenedores, (b) la diferencia y qué porcentaje es, (c) qué haces con la diferencia, (d) cuántos kg de dióxido de carbono equivaldría si fuera una fuga.",
        "(a) Ingresaron 40 kg; los contenedores suman 38 kg. (b) La diferencia es 2 kg; 2 por 100 dividido por 40 son 5 %. (c) La informo al supervisor para investigarla, sin cambiar cifras. (d) 2 por 300 son 600 kg.",
        ["suma los ingresos y los contenedores", "calcula la diferencia", "informa en vez de ajustar", "calcula el equivalente ambiental"],
        ["hoja con los cálculos"],
        ["ajustar una cifra", "afirmar que es una fuga", "restar al revés"],
        "Pregunta: «¿qué haces con los 2 kg de diferencia?». Si no responde, pídele que relea la regla de informar sin ajustar."),
    reinforce="Inventa un mes con tres ingresos y dos contenedores y calcula la diferencia.",
    extend="Explica con un ejemplo por qué un balance que siempre cuadra perfecto puede ser sospechoso.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 4 (contenedores de ejemplo, inventados). Un contenedor aprobado de ejemplo tiene una capacidad de 50 kg y un límite de llenado de 60 % de esa capacidad (el valor real lo fijan el fabricante del contenedor y la norma vigente). "
     "Se deben almacenar 70 kg de refrigerante recuperado. Hay 3 contenedores vacíos disponibles. Costo de gestión de ejemplo: $1.800 por kg.")
build(
    O9, 4, F,
    use="Aprenderé qué es el límite de llenado de un contenedor, a calcular cuántos contenedores se necesitan y a decidir qué hacer cuando no alcanzan.",
    prior=["Sé calcular porcentajes.", "Sé redondear hacia arriba.", "Sé qué es un contenedor aprobado."],
    explain=[
        "Un contenedor no se llena hasta su capacidad total. El límite de llenado es la cantidad máxima de fluido que puede contener, menor que su capacidad, para dejar un espacio de seguridad porque el fluido se expande con el calor. El límite se expresa como porcentaje de la capacidad; el valor real lo fijan el fabricante del contenedor y la norma vigente. Nunca se supera, aunque falte poco para terminar.",
        "Para saber cuántos contenedores se necesitan se calcula el límite en kg de uno, y se divide el total a almacenar por ese límite, redondeando hacia arriba. Si no alcanzan, no se sobrecargan: se pide otro contenedor aprobado. Un contenedor dañado, sin etiqueta o sin aprobación se saca de servicio y se avisa al supervisor. El manejo y el traslado los hace personal certificado; este cuaderno solo calcula en planilla.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("capacidad", "cantidad máxima que cabe físicamente en un contenedor"), ("límite de llenado", "cantidad máxima de fluido que se permite guardar, menor que la capacidad"), ("espacio de seguridad", "parte del contenedor que se deja libre porque el fluido se expande con el calor"), ("fuera de servicio", "estado de un contenedor que no puede usarse"), ("sobrecargar", "llenar un contenedor por encima de su límite")],
    worked=[
        ("Límite en kg", "Un contenedor de ejemplo tiene capacidad de 40 kg y un límite de llenado de 50 %. ¿Cuántos kg puede guardar?", ["El 50 % de 40 es 20.", "Ese es el límite en kg."], "20 kg"),
        ("Cuántos contenedores", "Se deben guardar 90 kg y cada contenedor admite 40 kg. ¿Cuántos contenedores se necesitan?", ["90 dividido por 40 da 2 y sobran 10 kg.", "Se redondea hacia arriba: 3."], "3 contenedores"),
    ],
    mistakes=[("Llenar un contenedor al 100 % para usar menos contenedores.", "El fluido se expande y no queda espacio de seguridad.", "Respeta el límite de llenado."),
              ("Usar un contenedor con una abolladura profunda porque «aguanta».", "Puede fallar bajo presión.", "Sácalo de servicio y avisa al supervisor.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es el límite de llenado de un contenedor?", "La cantidad máxima de fluido que se permite guardar, menor que su capacidad", "La cantidad de fluido que cabe físicamente en él", "El peso del contenedor vacío", "El límite de llenado es menor que la capacidad para dejar espacio de seguridad."),
        ("abc", "¿Por qué un contenedor no se llena al 100 %?", "Porque el fluido se expande con el calor y hay que dejar un espacio de seguridad", "Porque así sobra más fluido para vender", "Porque los contenedores siempre vienen con fluido", "El espacio libre permite que el fluido se expanda sin riesgo."),
        ("abc", "¿Quién fija el límite de llenado real?", "El fabricante del contenedor y la norma vigente", "El técnico que lo llena, según su experiencia", "El cliente del taller", "El límite real lo fijan el fabricante del contenedor y la norma vigente."),
        ("=", "{F} ¿Cuántos kg puede guardar un contenedor según el límite de llenado?", "50*60//100", "Se calcula el 60 % de la capacidad de 50 kg.", " kg"),
        ("=", "{F} ¿Cuántos contenedores se necesitan para almacenar los 70 kg?", "(70+29)//30", "Se divide el total entre el límite de 30 kg, redondeando hacia arriba.", " contenedores"),
        ("=", "{F} Con los 3 contenedores disponibles llenados hasta su límite, ¿cuántos kg de capacidad útil sobran después de guardar los 70 kg?", "3*30-70", "Se resta lo que se guarda de la capacidad útil total de los tres contenedores.", " kg"),
        ("=", "{F} ¿Cuánto cuesta la gestión de los 70 kg a la tarifa de ejemplo?", "70*1800", "Se multiplican los kg por el costo de gestión de cada kg.", " pesos"),
        ("abc", "{F} Un técnico propone llenar un contenedor al 100 % para usar menos contenedores. ¿Qué corresponde?", "No hacerlo: se respeta el límite de llenado y se usa otro contenedor", "Hacerlo si el contenedor es nuevo", "Hacerlo si el taller tiene poco espacio", "El límite de llenado no se supera; la falta de espacio no justifica un riesgo."),
        ("=", "{F} Si el límite de llenado fuera de 40 % en vez de 60 %, ¿cuántos kg guardaría cada contenedor?", "50*40//100", "Se calcula el 40 % de la capacidad de 50 kg.", " kg"),
        ("=", "{F} Con ese límite de 20 kg por contenedor, ¿cuántos contenedores se necesitan para los 70 kg?", "(70+19)//20", "Se divide el total entre 20 kg, redondeando hacia arriba.", " contenedores"),
        ("abc", "{F} Con el límite de 20 kg se necesitan 4 contenedores y solo hay 3. ¿Qué corresponde?", "Pedir otro contenedor aprobado y no sobrecargar los que hay", "Llenar más los 3 contenedores", "Dejar parte del fluido sin guardar", "Si no alcanzan, se consigue otro contenedor aprobado; no se sobrecargan ni se deja fluido suelto."),
        ("abc", "{F} Se detecta un contenedor con una abolladura profunda. ¿Qué corresponde?", "No usarlo, rotularlo fuera de servicio y avisar al supervisor", "Usarlo solo hasta la mitad", "Repararlo golpeándolo", "Un contenedor dañado puede fallar bajo presión; se saca de servicio."),
        ("=", "{F} El tercer contenedor recibió solo 10 kg. ¿Cuántos kg le faltan para llegar a su límite de llenado?", "30-10", "Se resta lo que tiene del límite de llenado de 30 kg.", " kg"),
    ],
    ctx=("abc", "Una jefa de taller de ejemplo ve que un contenedor se llenó por encima de su límite por apuro. ¿Qué corresponde?", "Detener la operación, avisar al supervisor y dejar que personal certificado lo resuelva", "Dejarlo así hasta mañana", "Probar a mano si se ve inflado", "Un contenedor sobrecargado es un riesgo; no se manipula sin personal certificado."),
    sc=[
        ("En Refrigeración: ¿cómo se calcula el límite de llenado en kg?", "Aplicando el porcentaje a la capacidad", "El 60 % de 50 kg es 30 kg."),
        ("¿Cómo se calcula el número de contenedores?", "Dividiendo el total por el límite y redondeando hacia arriba", "No se usan fracciones de contenedor."),
        ("¿Qué se hace con un contenedor dañado?", "Se saca de servicio y se avisa al supervisor", "Un contenedor dañado puede fallar bajo presión y causar un accidente."),
    ],
    op=("Datos de ejemplo del taller «Brisa» (ficticio): contenedores de 40 kg de capacidad con un límite de llenado del 50 %; hay que almacenar 90 kg; hay 3 contenedores; gestión de $1.500 por kg. "
        "Escribe (a) el límite en kg de un contenedor, (b) cuántos contenedores se necesitan, (c) qué haces si solo hay 3, (d) el costo de gestión de los 90 kg.",
        "(a) El 50 % de 40 son 20 kg. (b) 90 dividido por 20 da 4 y sobran 10 kg, por lo que se necesitan 5 contenedores. (c) Pido dos contenedores más aprobados y no sobrecargo los tres. (d) 90 por 1.500 son 135.000 pesos.",
        ["calcula el límite", "redondea hacia arriba", "no sobrecarga", "calcula el costo"],
        ["hoja con los cálculos"],
        ["llenar al 100 %", "redondear hacia abajo", "olvidar el costo"],
        "Pregunta: «¿por qué no llenas los tres contenedores más allá del límite?». Si no responde, pídele que relea el espacio de seguridad."),
    reinforce="Inventa un contenedor con capacidad y límite de llenado, y calcula cuántos se necesitan para una cantidad que elijas.",
    extend="Explica con un ejemplo por qué el espacio de seguridad de un contenedor importa cuando hace calor.",
)

# ============================================================ OAE-09, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas). Opciones para 40 kg de refrigerante recuperado: reciclar para reutilizar en el mismo taller (solo si un análisis de calidad lo permite), $500 por kg; regenerar en una planta autorizada, $900 por kg; "
     "destruir en una instalación autorizada, $1.600 por kg. Puntajes de 1 a 5 (5 es lo mejor), costo / aprovechamiento del material / cumplimiento de la norma: reciclar, 5 / 4 / 3; regenerar, 3 / 5 / 5; destruir, 1 / 1 / 5. "
     "Pesos: costo 1, aprovechamiento 2, cumplimiento 3. Lista de verificación documental de 6 puntos: hoja de trazabilidad completa, contenedores etiquetados, certificado del técnico vigente, destino autorizado indicado, documento de transporte y firma del supervisor; se cumplieron 5 y falta el documento de transporte.")
build(
    O9, 5, F,
    use="Aprenderé a comparar los destinos de un refrigerante recuperado con costos y puntajes, y a verificar la documentación antes de trasladar contenedores.",
    prior=["Sé qué significan recuperar, reciclar, regenerar y destruir.", "Sé calcular un puntaje ponderado.", "Sé qué es la trazabilidad."],
    explain=[
        "El refrigerante recuperado puede reciclarse, regenerarse o destruirse. Cada opción se compara con criterios: el costo, el aprovechamiento del material, que mide cuánto del fluido vuelve a usarse, y el cumplimiento de la norma. Con los puntajes y los pesos se calcula un puntaje ponderado. La destrucción se reserva para el fluido que no puede reutilizarse ni regenerarse, porque no lo aprovecha. Reciclar solo es posible si un análisis de calidad lo permite.",
        "Antes de trasladar los contenedores se verifica la documentación con una lista de control. El destino debe ser un lugar autorizado y el traslado va acompañado de su documento de transporte. Si falta un punto, no se mueven los contenedores ni se firma hasta cumplirlo. La elección final la aprueba el responsable según la norma vigente; quien calcula en planilla solo propone.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("aprovechamiento", "cuánto del material vuelve a usarse"), ("destino autorizado", "lugar o planta que cuenta con autorización para recibir y tratar el refrigerante"), ("análisis de calidad", "revisión que dice si un fluido recuperado puede reutilizarse"), ("lista de verificación documental", "lista de documentos y registros que deben estar completos antes de actuar"), ("puntaje ponderado", "suma de cada puntaje multiplicado por el peso de su criterio")],
    worked=[
        ("Costo de un destino", "Reciclar 10 kg cuesta $400 por kg en un ejemplo. ¿Cuánto cuesta?", ["Se multiplica el precio por kg por los kg.", "10 por 400 son 4.000."], "$4.000"),
        ("Puntaje ponderado", "Una opción de ejemplo tiene puntajes 4 en costo (peso 1) y 5 en cumplimiento (peso 3). ¿Cuál es su puntaje ponderado?", ["4 por 1 son 4 y 5 por 3 son 15.", "4 más 15 son 19."], "19 puntos"),
    ],
    mistakes=[("Elegir siempre la opción más barata sin mirar el cumplimiento de la norma.", "Puede no estar permitida o no ser segura.", "Compara todos los criterios con su peso."),
              ("Mover los contenedores sin el documento de transporte.", "No queda constancia del origen ni del destino.", "Espera a tener los documentos completos.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es un destino autorizado?", "Un lugar o planta autorizado para recibir y tratar el refrigerante", "Cualquier bodega que acepte los contenedores", "El taller donde se recuperó el fluido", "Un destino autorizado cuenta con permiso para tratar el fluido; una bodega cualquiera no."),
        ("abc", "¿Cuándo se destruye un refrigerante?", "Cuando no puede reutilizarse ni regenerarse", "Cuando sobra espacio en el taller", "Cuando el cliente prefiere no esperar", "La destrucción es el último recurso porque no aprovecha el fluido."),
        ("abc", "¿Qué documento acompaña el traslado de un contenedor?", "El documento de transporte, que identifica contenido, origen y destino", "La factura del equipo original", "El manual del fabricante del equipo", "El documento de transporte deja constancia del traslado."),
        ("=", "{F} ¿Cuánto cuesta reciclar los 40 kg?", "40*500", "Se multiplican los kg por el precio de reciclar cada kg.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta regenerar los 40 kg?", "40*900", "Se multiplican los kg por el precio de regenerar cada kg.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta destruir los 40 kg?", "40*1600", "Se multiplican los kg por el precio de destruir cada kg.", " pesos"),
        ("=", "{F} ¿Cuál es el puntaje ponderado de reciclar?", "5*1+4*2+3*3", "Cada puntaje de reciclar se multiplica por el peso de su criterio y se suma.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje ponderado de regenerar?", "3*1+5*2+5*3", "Cada puntaje de regenerar se multiplica por el peso de su criterio y se suma.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje ponderado de destruir?", "1*1+1*2+5*3", "Cada puntaje de destruir se multiplica por el peso de su criterio y se suma.", " puntos"),
        ("abc", "{F} Según los puntajes ponderados, ¿qué opción aparece primera?", "Regenerar, con 28 puntos", "Reciclar, con 22 puntos", "Destruir, con 18 puntos", "Regenerar suma 28, reciclar 22 y destruir 18."),
        ("abc", "{F} Un compañero dice: «destruir es lo más seguro, así que siempre es mejor». ¿Qué respuesta es correcta?", "No siempre: destruir cuesta más y aprovecha menos; se elige según la calidad del fluido y la norma vigente", "Sí: lo más seguro es siempre lo mejor sin mirar el costo", "Sí, porque destruir aprovecha todo el material", "Destruir no aprovecha el material y es la opción de mayor costo en la ficha."),
        ("=", "{F} ¿Cuánto más cuesta destruir los 40 kg que regenerarlos?", "40*1600-40*900", "Se resta el costo de regenerar del costo de destruir.", " pesos"),
        ("abc", "{F} Falta el documento de transporte. ¿Qué corresponde?", "No mover los contenedores ni firmar hasta contar con él", "Mover los contenedores y presentar el documento después", "Firmar la lista para que parezca completa", "Un punto documental pendiente impide trasladar y firmar."),
    ],
    ctx=("abc", "Un transportista de ejemplo llega a retirar los contenedores y el taller aún no tiene el documento de transporte. ¿Qué hace el supervisor?", "No entrega los contenedores hasta completar el documento", "Los entrega y completa el documento en el camino", "Los entrega si el transportista promete devolver una copia", "Sin documento de transporte no hay constancia del traslado; no se entrega."),
    sc=[
        ("En Refrigeración: ¿qué criterios se comparan al elegir un destino?", "Costo, aprovechamiento y cumplimiento de la norma", "El puntaje ponderado resume la comparación."),
        ("¿Cuándo se destruye un refrigerante?", "Cuando no puede reutilizarse ni regenerarse", "Destruir es el último recurso, cuando nada más se puede aprovechar."),
        ("¿Qué se verifica antes de trasladar los contenedores?", "Que la documentación esté completa", "Falta un documento: no se mueve ni se firma."),
    ],
    op=("Alternativas de ejemplo del taller «Austral» (ficticio) para 20 kg: regenerar a $900 por kg con puntajes costo / aprovechamiento / cumplimiento 3 / 5 / 5; destruir a $1.600 por kg con puntajes 1 / 1 / 5. Pesos: costo 1, aprovechamiento 2, cumplimiento 3. Lista documental de 5 puntos, 4 cumplidos; falta la firma del supervisor. "
        "Escribe (a) el costo de cada opción, (b) el puntaje ponderado de cada una, (c) qué opción propones y por qué, (d) qué haces con el punto que falta.",
        "(a) Regenerar: 20 por 900 son 18.000; destruir: 20 por 1.600 son 32.000. (b) Regenerar: 3 más 10 más 15 son 28; destruir: 1 más 2 más 15 son 18. (c) Propongo regenerar, porque tiene mayor puntaje y menor costo, si la calidad del fluido lo permite; lo aprueba el responsable. (d) No muevo los contenedores ni firmo hasta que el supervisor firme.",
        ["calcula los costos", "calcula los puntajes", "propone con fundamento", "no mueve ni firma con un punto pendiente"],
        ["hoja con los cálculos y la propuesta"],
        ["olvidar el peso", "elegir solo por costo", "mover los contenedores con un punto pendiente"],
        "Pregunta: «¿qué haces con la firma que falta?». Si no responde, pídele que relea la regla de la lista de verificación."),
    reinforce="Escribe los cuatro destinos de un refrigerante recuperado y un criterio con que compararías dos de ellos.",
    extend="Explica con un ejemplo por qué la documentación completa protege tanto al ambiente como a las personas.",
)
