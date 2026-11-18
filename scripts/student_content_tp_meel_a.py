"""Mecánica Industrial, mención Mantenimiento Electromecánico, 4.º medio: OAM-01 (mantenimiento preventivo: pautas y bitácora), OAM-02 (comprobar funcionamiento: instrumentos y magnitudes eléctricas) y OAM-03 (instalar componentes: lectura de planos, selección en tablas de ejemplo y verificación documental). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_meel_common import AVISO, EMER, build

O1 = "TP-MEEL-4-OAM-01"
O2 = "TP-MEEL-4-OAM-02"
O3 = "TP-MEEL-4-OAM-03"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Una planta de ejemplo tiene una bomba de agua ficticia B-12 accionada por un motor eléctrico. Componentes: motor, acople (unión entre el motor y la bomba), bomba, tubería con válvulas y tablero eléctrico de comando. "
     "Peligros anotados: energía eléctrica, partes giratorias, fluido caliente, energía almacenada (presión en la tubería), ruido y derrame de aceite. Plan anual de ejemplo: 4 intervenciones con la bomba detenida y 12 inspecciones con la bomba funcionando.")
build(
    O1, 1, F,
    use="Aprenderé qué es el mantenimiento electromecánico, la diferencia entre trabajar con la máquina funcionando o detenida, qué energías son peligrosas y qué institución fiscaliza lo eléctrico.",
    prior=["Sé qué es el mantenimiento preventivo.", "Sé la jerarquía de controles.", "Sé sumar y multiplicar enteros."],
    explain=[
        "El mantenimiento electromecánico cuida equipos que combinan partes mecánicas, como ejes y rodamientos, y partes eléctricas, como motores y tableros. El mantenimiento preventivo se hace antes de la falla, siguiendo las pautas del fabricante y la bitácora de funcionamiento, que es el registro de horas, temperaturas, ruidos y fallas. Algunas tareas se hacen con la máquina funcionando, como observar y registrar variables desde puntos seguros; otras exigen la máquina detenida.",
        "Detener una máquina no basta si queda energía: la energía eléctrica, la presión, el calor y los resortes cargados son energías que pueden dañar. Por eso las empresas usan el bloqueo y etiquetado, un control administrativo que evita que una energía se active por error mientras alguien trabaja; su secuencia la fija el procedimiento de la empresa y la aplica personal autorizado. La Superintendencia de Electricidad y Combustibles (SEC) fiscaliza lo eléctrico y los combustibles. Los aceites y residuos se manejan según la norma vigente.",
        f"Este cuaderno no enseña a intervenir ningún equipo. {EMER} {AVISO}",
    ],
    vocab=[("mantenimiento electromecánico", "cuidado de equipos con partes mecánicas y eléctricas"), ("bitácora de funcionamiento", "registro de horas, variables, ruidos y fallas de una máquina"), ("acople", "unión entre el eje de un motor y el de otra máquina"), ("energía almacenada", "energía que queda en el equipo aunque esté detenido, como presión o resortes"), ("bloqueo y etiquetado", "control administrativo que evita que una energía se active por error"), ("SEC", "Superintendencia de Electricidad y Combustibles")],
    worked=[
        ("Energía almacenada", "Una tubería de ejemplo sigue con presión aunque la bomba esté detenida. ¿Qué tipo de peligro es?", ["La presión es energía que queda en el equipo.", "Es energía almacenada."], "Energía almacenada"),
        ("Tipo de control", "Una empresa de ejemplo exige un candado y una tarjeta en el interruptor mientras alguien trabaja. ¿Qué tipo de control es?", ["Es una regla de la empresa que evita una activación por error.", "Es un control administrativo."], "Control administrativo"),
    ],
    mistakes=[("Creer que una máquina detenida ya no tiene peligros.", "Puede quedar energía almacenada, calor o piezas que giran por inercia.", "Considera todas las energías del equipo, según el procedimiento de la empresa."),
              ("Creer que leer sobre bloqueo habilita para aplicarlo.", "Su secuencia la fija la empresa y la aplica personal autorizado.", "Aprende el concepto y deja la aplicación a quien corresponde.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es el mantenimiento electromecánico?", "El cuidado de equipos con partes mecánicas y eléctricas", "El cuidado de instalaciones de agua potable", "La fabricación de piezas en serie", "Es la combinación de mecánica y electricidad en los equipos."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es una bitácora de funcionamiento?", "El registro de horas, variables, ruidos y fallas de una máquina", "El plano de ubicación de la planta", "El manual de venta del equipo", "La bitácora acumula el historial de funcionamiento."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es el bloqueo y etiquetado?", "Un control administrativo que evita que una energía se active por error", "Una barrera física que impide tocar una pieza", "Un instrumento que mide la energía", "Es una regla de la empresa que protege a quien trabaja."),
        ("=", "{F} ¿Cuántas intervenciones en total tiene el plan anual de la bomba?", "4+12", "Se suman las intervenciones con la bomba detenida y las inspecciones con la bomba funcionando.", " intervenciones"),
        ("abc", "{F} ¿Cuál de los peligros de la ficha sigue presente aunque se detenga la bomba?", "La energía almacenada, como la presión en la tubería", "El ruido de la bomba funcionando", "El movimiento del acople en marcha", "Detener la bomba corta el ruido y el giro, pero la presión puede quedar."),
        ("abc", "{F} ¿Qué institución fiscaliza lo eléctrico de una planta?", "La SEC", "El Servicio de Impuestos Internos", "La Dirección del Trabajo", "La SEC fiscaliza electricidad y combustibles; la Dirección del Trabajo fiscaliza lo laboral."),
        ("=", "{F} La bitácora anota 3 horas de inspección por cada inspección con la bomba funcionando. ¿Cuántas horas suman las 12 inspecciones del año?", "12*3", "Se multiplican las inspecciones por las horas de cada una.", " horas"),
        ("=", "{F} Cada intervención con la bomba detenida requiere 5 personas. ¿Cuántas personas-intervención suman las 4 intervenciones del año?", "4*5", "Se multiplican las intervenciones por las personas de cada una.", " personas-intervención"),
        ("abc", "{F} La matriz del taller dice «derrame de aceite». ¿Cuál es una medida de ingeniería?", "Instalar una bandeja de contención bajo el equipo", "Colocar un cartel de aviso", "Usar calzado antideslizante", "La bandeja es una barrera física; el cartel es administrativo y el calzado es EPP."),
        ("abc", "{F} Un practicante dice: «como la bomba está detenida, puedo abrir el tablero sin riesgo». ¿Qué respuesta es correcta?", "Es falso: puede haber energía eléctrica, y solo personal autorizado, según el procedimiento de la empresa, interviene", "Es cierto, porque detenida significa sin energía", "Es cierto, si usa guantes", "Detenida no implica sin energía; el tablero lo interviene personal autorizado."),
        ("abc", "En una visita a una planta de ejemplo, una persona recibe una descarga eléctrica de un tablero y queda inmóvil. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Tocarla para separarla del tablero", "Echarle agua para que reaccione", "Tocarla o mojar el lugar puede electrocutarte; se llama a quienes pueden actuar."),
        ("=", "{F} El plan anual repite las 4 intervenciones con la bomba detenida en 6 bombas iguales a la B-12. ¿Cuántas intervenciones detenidas se hacen en total?", "4*6", "Se multiplican las intervenciones por las bombas.", " intervenciones"),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué se hace con el aceite usado de un equipo?", "Se almacena en un recipiente rotulado hasta su retiro según la norma vigente", "Se vierte al desagüe de la planta", "Se mezcla con agua para botarlo", "El aceite usado es un residuo que se maneja con la norma."),
    ],
    ctx=("abc", "Un jefe de ejemplo dice: «la bomba ya está parada, ayúdame a abrir el tablero, es rápido». ¿Qué respondes?", "Que solo personal autorizado interviene según el procedimiento de la empresa, y que consultarás a un adulto responsable", "Que sí, porque está parada", "Que sí, con guantes", "Un tablero puede tener energía y este cuaderno no habilita para intervenirlo."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué es energía almacenada?", "La que queda en el equipo aunque esté detenido", "Puede ser presión, calor o resortes cargados."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué institución fiscaliza lo eléctrico?", "La SEC", "La SEC fiscaliza electricidad y combustibles."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué tipo de control es el bloqueo y etiquetado?", "Un control administrativo", "Es una regla de la empresa que previene activaciones por error."),
    ],
    op=("Ficha de ejemplo: un compresor ficticio C-3 tiene un motor eléctrico, un tanque con aire a presión, una correa de transmisión y un tablero. Peligros anotados: energía eléctrica, aire a presión, partes giratorias y ruido. Escribe (a) cuál de esos peligros es energía almacenada, (b) un control de ingeniería, (c) un control administrativo, (d) por qué detener el compresor no elimina todos los peligros. No describas cómo se interviene.",
        "(a) El aire a presión en el tanque. (b) Un resguardo sobre la correa de transmisión. (c) El bloqueo y etiquetado y una señal de acceso solo para personal autorizado. (d) Porque puede quedar energía almacenada, como la presión del tanque, o energía eléctrica en el tablero.",
        ["identifica la energía almacenada", "propone un control de ingeniería", "propone un control administrativo", "explica por qué detener no elimina todo"],
        ["hoja con las cuatro respuestas"],
        ["decir que detenido es igual a sin energía", "proponer solo EPP", "describir cómo se interviene el equipo"],
        "Pregunta: «¿qué energía queda aunque el compresor esté parado?». Si duda, pídele que relea la definición de energía almacenada."),
    reinforce="Escribe tres energías que pueden quedar en un equipo detenido y un control para cada una.",
    extend="Explica con un ejemplo por qué detener un equipo no reemplaza el bloqueo y etiquetado.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (pauta y bitácora de ejemplo, inventadas, para la bomba ficticia B-12; no reemplazan el manual del fabricante). Pauta del fabricante de ejemplo: inspección visual y de ruidos cada 100 horas de operación; revisión de lubricación cada 500 horas; "
     "revisión del acople cada 1.000 horas; revisión general por personal autorizado cada 4.000 horas. Bitácora: horas de operación acumuladas hoy, 2.350; última revisión de lubricación a las 2.000 horas; último acople a las 1.000 horas; última revisión general a las 0 horas. "
     "Registros: temperatura del cojinete (pieza que sostiene el eje), 58 °C, límite del fabricante de ejemplo 80 °C.")
build(
    O1, 2, F,
    use="Aprenderé a leer una pauta por horas de operación y una bitácora, a calcular cuándo corresponde cada tarea y qué rol interviene.",
    prior=["Sé qué es una pauta de mantenimiento.", "Sé restar y comparar enteros.", "Sé qué es una bitácora."],
    explain=[
        "Muchas pautas se escriben por horas de operación y no por fecha: cada cierto número de horas acumuladas corresponde una tarea. La bitácora anota las horas acumuladas y cuándo se hizo cada tarea por última vez. La próxima ejecución se calcula sumando el intervalo a la última ejecución; si las horas actuales ya la superaron, la tarea está vencida. El cojinete es la pieza que sostiene un eje y permite que gire; su temperatura se compara con el límite del fabricante.",
        "El manual del fabricante manda sobre cualquier costumbre. El planificador programa las tareas, el técnico de mantenimiento autorizado las ejecuta, el supervisor las aprueba y el operador de la planta informa de ruidos o cambios que nota. Una variable fuera del límite se informa de inmediato y no se espera a la próxima revisión.",
        f"Se leen y se calculan documentos; no se interviene ningún equipo. {EMER} {AVISO}",
    ],
    vocab=[("horas de operación", "tiempo acumulado que el equipo ha funcionado"), ("intervalo", "cantidad de horas entre dos ejecuciones de una tarea"), ("tarea vencida", "la que ya superó su momento de ejecución"), ("cojinete", "pieza que sostiene un eje y permite que gire"), ("límite del fabricante", "valor que una variable no debe superar")],
    worked=[
        ("Próxima ejecución", "Una tarea de ejemplo se hace cada 300 horas y la última vez fue a las 1.200 horas. ¿A qué hora de operación corresponde la próxima?", ["Se suma el intervalo a la última ejecución.", "1.200 más 300 son 1.500."], "A las 1.500 horas"),
        ("Tarea vencida", "Un equipo de ejemplo lleva 2.600 horas y una tarea debía hacerse a las 2.500 horas. ¿Está vencida?", ["Las horas actuales superan las 2.500.", "La tarea ya pasó su momento."], "Sí, está vencida por 100 horas"),
    ],
    mistakes=[("Contar las horas desde que el equipo se instaló y no desde la última ejecución de la tarea.", "El intervalo se cuenta desde la última vez que se hizo.", "Resta las horas actuales menos las de la última ejecución."),
              ("Esperar a la próxima revisión cuando una variable supera el límite.", "Superar el límite puede dañar el equipo o causar un accidente.", "Informa de inmediato a la jefatura.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué son las horas de operación?", "El tiempo acumulado que el equipo ha funcionado", "El horario de trabajo del técnico", "Las horas en que el equipo está apagado", "Muchas pautas se miden por el funcionamiento acumulado."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es un cojinete?", "La pieza que sostiene un eje y permite que gire", "El cable que alimenta al motor", "La válvula que regula el fluido", "El cojinete soporta el eje en su giro."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿cómo se calcula la próxima ejecución de una tarea por horas?", "Se suma el intervalo a la hora de la última ejecución", "Se resta el intervalo a las horas acumuladas totales", "Se multiplica el intervalo por las horas actuales", "La próxima ejecución parte de la última más el intervalo."),
        ("=", "{F} ¿Cuántas horas han pasado desde la última revisión de lubricación?", "2350-2000", "Se resta la hora de la última lubricación a las horas actuales.", " horas"),
        ("abc", "{F} ¿Cuál es la tarea de intervalo más largo de la pauta?", "La revisión general por personal autorizado, cada 4.000 horas", "La inspección visual, cada 100 horas", "La revisión del acople, cada 1.000 horas", "4.000 horas es el intervalo mayor."),
        ("abc", "{F} ¿Qué dice la bitácora sobre la temperatura del cojinete?", "Está en 58 °C, por debajo del límite de 80 °C", "Está en 80 °C, justo en el límite", "Está en 100 °C, sobre el límite", "El valor registrado es 58 °C y el límite es 80 °C."),
        ("=", "{F} ¿A qué hora de operación corresponde la próxima revisión de lubricación?", "2000+500", "Se suma el intervalo a la última ejecución.", " horas"),
        ("=", "{F} ¿A qué hora de operación corresponde el próximo acople, según su intervalo?", "1000+1000", "Se suma el intervalo a la hora de la última revisión del acople.", " horas"),
        ("abc", "{F} Con 2.350 horas acumuladas, ¿qué tarea está vencida?", "La revisión del acople, que correspondía a las 2.000 horas", "La revisión general, que corresponde a las 4.000 horas", "La revisión de lubricación, que corresponde a las 2.500 horas", "El acople venció a las 2.000 horas; las otras aún no cumplen su momento."),
        ("abc", "{F} Un operador nota un ruido nuevo en el cojinete. ¿Qué corresponde?", "Informarlo de inmediato a la jefatura y registrarlo en la bitácora", "Esperar a la próxima inspección programada", "Acercar la mano para sentir la vibración", "Un cambio en el ruido puede anunciar una falla y se informa de inmediato."),
        ("abc", "{F} Un técnico dice: «la temperatura de 58 °C es baja, así que puedo saltarme la revisión del acople». ¿Qué respuesta es correcta?", "Es falso: la pauta se cumple por horas y no por una sola variable", "Es cierto, porque la temperatura manda", "Es cierto, si el equipo suena normal", "Cada tarea tiene su propio intervalo."),
        ("=", "{F} Si la bomba opera 20 horas por día, ¿en cuántos días llegará a las 4.000 horas de la revisión general desde las 2.350 acumuladas? Redondea hacia arriba.", "(4000-2350+19)//20", "Se restan las horas acumuladas a las 4.000 y se divide por las horas por día, redondeando hacia arriba.", " días"),
        ("Una tarea de ejemplo se hace cada 250 horas. Un equipo lleva 1.020 horas y la última ejecución fue a las 750. ¿Cuántas horas de atraso tiene la tarea?", "20 horas de atraso", "La próxima era a las 1.000 horas (750 más 250) y el equipo lleva 1.020, así que está vencida por 20 horas."),
    ],
    ctx=("abc", "Un técnico de ejemplo dice: «la pauta dice cada 1.000 horas, pero yo lo cambio cuando se me ocurre». ¿Qué propones?", "Seguir la pauta del fabricante y consultar al planificador si hay motivos para cambiar el intervalo", "Aceptarlo porque tiene experiencia", "Eliminar la tarea de la pauta", "El manual del fabricante manda sobre la costumbre."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cómo se sabe si una tarea por horas está vencida?", "Comparando las horas actuales con la última ejecución más el intervalo", "La tarea vence cuando las horas actuales superan ese valor."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué manda sobre la costumbre del taller?", "El manual del fabricante", "La pauta se basa en el manual del fabricante."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se hace si una variable supera el límite?", "Se informa de inmediato", "Esperar puede dañar el equipo o causar un accidente."),
    ],
    op=("Ficha de ejemplo: un ventilador ficticio V-2 tiene una pauta por horas de operación: inspección cada 200 horas; revisión de lubricación cada 600 horas; revisión general cada 3.000 horas. Bitácora: horas acumuladas 1.450; última inspección a las 1.400; última lubricación a las 1.200; última revisión general a las 0. Temperatura del cojinete 70 °C, límite de ejemplo 85 °C. Escribe (a) a qué hora corresponde la próxima inspección, (b) si la lubricación está vencida, (c) cuántas horas faltan para la revisión general, (d) si la temperatura está dentro del límite.",
        "(a) 1.400 + 200 = 1.600 horas. (b) Corresponde a las 1.800 horas; con 1.450 aún no está vencida. (c) 3.000 − 1.450 = 1.550 horas. (d) Sí, 70 °C es menor que 85 °C.",
        ["calcula la próxima inspección", "evalúa la lubricación", "calcula las horas restantes", "compara con el límite"],
        ["hoja con las cuatro respuestas"],
        ["sumar al revés", "contar desde cero", "ignorar el límite"],
        "Pregunta: «¿desde cuándo cuentas el intervalo?». Si duda, pídele que relea la regla de la próxima ejecución."),
    reinforce="Inventa una pauta con tres tareas por horas y calcula la próxima ejecución de cada una.",
    extend="Explica con un ejemplo por qué una pauta por horas es más precisa que una por fecha para un equipo que trabaja pocos días.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (tendencia de una bitácora de ejemplo, inventada, de una bomba ficticia B-20). Temperatura del cojinete en °C registrada en cada inspección, una cada 100 horas de operación: 60, 61, 63, 67, 72, 78. "
     "Límite del fabricante de ejemplo: 80 °C. Vibración, en unidades de ejemplo: 3, 3, 4, 5, 7, 9; límite de ejemplo 20. Ruido: «normal» en las primeras cuatro inspecciones y «ruido nuevo» en las dos últimas. "
     "Regla del taller de ejemplo: si una variable sube en dos inspecciones seguidas y supera el 85 % de su límite, se adelanta el mantenimiento y se informa a la jefatura. Costo de ejemplo de una parada programada: $50.000; de una falla imprevista: $400.000.")
build(
    O1, 3, F,
    use="Aprenderé a leer la tendencia de una bitácora, a aplicar una regla de adelanto y a comparar el costo de una parada programada con el de una falla.",
    prior=["Sé leer una serie de números.", "Sé calcular un porcentaje de números redondos.", "Sé qué es un límite del fabricante."],
    explain=[
        "Una tendencia es el cambio de una variable a lo largo del tiempo. Mirar solo el último valor puede engañar: un valor bajo el límite que sube cada vez avisa de un problema antes de la falla. Por eso la bitácora se lee en serie. Una regla del taller puede decir cuándo adelantar el mantenimiento, por ejemplo cuando una variable sube varias veces seguidas y se acerca a su límite.",
        "El 85 % de un límite se calcula multiplicando el límite por 85 y dividiéndolo por 100. Una parada programada cuesta menos que una falla imprevista, que además puede dañar otras piezas y poner en riesgo a las personas. La decisión de adelantar el mantenimiento la toma la jefatura con los datos de la bitácora.",
        f"El análisis es de papel con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("tendencia", "cambio de una variable a lo largo del tiempo"), ("adelantar el mantenimiento", "hacer la tarea antes de la fecha prevista"), ("parada programada", "detención del equipo planificada con anticipación"), ("falla imprevista", "falla que ocurre sin aviso y detiene el equipo"), ("porcentaje del límite", "parte del límite que alcanza una variable")],
    worked=[
        ("Calcular el 85 %", "El límite de ejemplo de una variable es 200. ¿Cuánto es el 85 % del límite?", ["Se multiplica 200 por 85: 17.000.", "17.000 dividido en 100 son 170."], "170"),
        ("Leer una tendencia", "Una variable de ejemplo registra 20, 22, 25 y 29 en cuatro inspecciones. ¿Sube o baja?", ["Cada valor es mayor que el anterior.", "La variable sube en cada inspección."], "Sube"),
    ],
    mistakes=[("Mirar solo el último valor y concluir que no pasa nada porque está bajo el límite.", "Una tendencia ascendente avisa antes de superar el límite.", "Lee toda la serie y aplica la regla."),
              ("Esperar a que la falla ocurra porque la parada programada «es un gasto».", "La falla imprevista cuesta más y es más peligrosa.", "Compara costos y riesgos antes de decidir.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es una tendencia en una bitácora?", "El cambio de una variable a lo largo del tiempo", "El último valor registrado", "El límite del fabricante", "La tendencia se ve comparando varios registros."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es una falla imprevista?", "Una falla que ocurre sin aviso y detiene el equipo", "Una detención planificada con anticipación", "Una revisión mensual de la pauta", "Imprevista significa que no se planificó."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿por qué conviene leer toda la serie de la bitácora y no solo el último valor?", "Porque una tendencia ascendente avisa de un problema antes de superar el límite", "Porque el último valor siempre está equivocado", "Porque la serie reemplaza al manual del fabricante", "La serie muestra el cambio en el tiempo."),
        ("=", "{F} ¿Cuántos °C subió la temperatura del cojinete entre la primera y la última inspección?", "78-60", "Se resta la primera lectura a la última.", " °C"),
        ("=", "{F} ¿Cuántos °C faltan para llegar al límite del fabricante desde la última inspección?", "80-78", "Se resta la última lectura al límite.", " °C"),
        ("abc", "{F} ¿En qué inspecciones apareció el «ruido nuevo»?", "En las dos últimas", "En las dos primeras", "En todas", "La ficha indica ruido normal en las primeras cuatro."),
        ("=", "{F} ¿Cuánto vale el 85 % del límite de temperatura de 80 °C?", "80*85//100", "Se multiplica el límite por 85 y se divide por 100.", " °C"),
        ("=", "{F} ¿Cuánto vale el 85 % del límite de vibración de 20 unidades de ejemplo?", "20*85//100", "Se multiplica el límite por 85 y se divide por 100, sin considerar decimales.", " unidades"),
        ("abc", "{F} Con la regla del taller, ¿qué corresponde hacer?", "Adelantar el mantenimiento e informar a la jefatura, porque la temperatura sube y supera el 85 % del límite", "Esperar, porque la temperatura aún no llega a 80 °C", "Ignorar la temperatura, porque la vibración está bajo 20", "La temperatura sube en inspecciones seguidas y supera 68 °C."),
        ("abc", "{F} Un jefe dice: «no hay problema, 78 °C está bajo el límite de 80». ¿Qué respuesta es correcta?", "Es insuficiente: la serie sube en cada inspección y hay ruido nuevo, así que la regla manda adelantar el mantenimiento", "Es correcto, porque está bajo el límite", "Es correcto, si el ruido es normal", "Una tendencia ascendente cercana al límite exige actuar."),
        ("abc", "{F} Un practicante dice: «mido la temperatura del cojinete tocándolo con la mano para confirmar». ¿Qué respuesta es correcta?", "No corresponde: tocar una máquina en funcionamiento es peligroso, y la medición la hace personal autorizado con un instrumento", "Corresponde, porque la mano es sensible", "Corresponde, si lleva guantes", "Una pieza caliente o en movimiento puede causar daño."),
        ("=", "{F} Si se adelanta el mantenimiento con una parada programada en lugar de esperar una falla, ¿cuánto se ahorra, por diferencia de costo?", "400000-50000", "Se resta el costo de la parada programada al de la falla imprevista.", " pesos de ejemplo"),
        ("=", "{F} Una planta de ejemplo tiene 5 bombas con la misma tendencia. Si se adelanta el mantenimiento en todas, ¿cuánto cuestan las 5 paradas programadas?", "5*50000", "Se multiplica el costo de una parada por las bombas.", " pesos de ejemplo"),
    ],
    ctx=("abc", "El supervisor de ejemplo dice: «la bomba sigue andando, esperemos a ver si falla». La bitácora muestra temperatura y vibración subiendo. ¿Qué propones?", "Aplicar la regla del taller, adelantar el mantenimiento e informar a la jefatura", "Esperar a que falle", "Borrar los registros altos", "La tendencia ascendente justifica actuar antes de la falla."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cuánto es el 85 % de 400?", "340", "Se multiplica 200 por 85 y se divide por 100."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué costo es mayor, el de una parada programada o el de una falla imprevista?", "El de la falla imprevista", "La falla puede dañar otras piezas y detener la producción."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿quién decide adelantar el mantenimiento?", "La jefatura, con los datos de la bitácora", "La decisión se apoya en los registros."),
    ],
    op=("Ficha de ejemplo: temperatura del cojinete de otra bomba, en °C, en seis inspecciones: 58, 60, 63, 66, 69, 72. Límite de ejemplo: 80 °C. Regla del taller: se adelanta el mantenimiento si la variable sube en inspecciones seguidas y supera el 85 % del límite. Escribe (a) el 85 % del límite, (b) si la última lectura lo supera, (c) si se adelanta el mantenimiento y por qué, (d) cuántos °C faltan para el límite.",
        "(a) 80 × 85 ÷ 100 = 68 °C. (b) Sí, 72 supera 68. (c) Sí, porque sube en inspecciones seguidas y supera el 85 % del límite. (d) 80 − 72 = 8 °C.",
        ["calcula el 85 %", "compara la última lectura", "aplica la regla", "calcula los °C restantes"],
        ["hoja con las cuatro respuestas"],
        ["mirar solo el último valor", "calcular mal el 85 %", "no aplicar la regla"],
        "Pregunta: «¿la variable sube en cada inspección?». Si duda, pídele que compare cada valor con el anterior."),
    reinforce="Inventa una serie de seis lecturas que suban y decide si aplicarías una regla de adelanto con tus propios números.",
    extend="Explica con un ejemplo por qué una falla imprevista es más riesgosa que una parada programada.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (planificación mensual de ejemplo, inventada). Una planta de ejemplo tiene 6 bombas iguales. Cada bomba opera 600 horas al mes. Pauta de ejemplo: inspección cada 100 horas (2 horas de trabajo cada vez); lubricación cada 300 horas (3 horas de trabajo); revisión general cada 3.000 horas (24 horas de trabajo). "
     "El taller tiene 2 técnicos autorizados que trabajan 8 horas por día en 20 días hábiles al mes. Costo de ejemplo de una hora de técnico: $9.000. Costo de ejemplo de una hora de parada no programada de una bomba: $30.000.")
build(
    O1, 4, F,
    use="Aprenderé a convertir una pauta por horas en cargas de trabajo mensuales, a comprobar si el equipo de técnicos alcanza y a calcular costos de ejemplo.",
    prior=["Sé multiplicar y dividir enteros.", "Sé qué es una pauta por horas.", "Sé calcular horas de trabajo."],
    explain=[
        "Para saber cuánto trabajo genera una pauta se divide las horas de operación del mes entre el intervalo de cada tarea y se multiplica por las horas de trabajo que toma la tarea. Eso da las horas-técnico del mes. La capacidad del equipo se calcula multiplicando los técnicos por las horas diarias y por los días hábiles. Si la carga supera la capacidad, el plan no se puede cumplir y se debe pedir más personal o reprogramar.",
        "El costo de mano de obra de las tareas es las horas-técnico por el costo por hora. Una buena planificación compara la carga con la capacidad y el costo preventivo con el de las paradas no programadas, y deja registro. Las tareas con intervención las hace personal autorizado.",
        f"Los números son de ejemplo y el cálculo es de papel. {EMER} {AVISO}",
    ],
    vocab=[("horas-técnico", "horas de trabajo de los técnicos"), ("carga de trabajo", "horas-técnico que pide un plan"), ("capacidad", "horas-técnico que el equipo puede entregar"), ("reprogramar", "cambiar la fecha de una tarea"), ("costo de mano de obra", "horas-técnico por el costo de cada hora")],
    worked=[
        ("Carga de una tarea", "Una tarea de ejemplo se hace cada 200 horas de operación y toma 2 horas de trabajo. Un equipo opera 400 horas al mes. ¿Cuántas horas-técnico pide al mes?", ["400 dividido en 200 son 2 veces.", "2 veces por 2 horas son 4."], "4 horas-técnico"),
        ("Capacidad", "Tres técnicos de ejemplo trabajan 6 horas por día durante 10 días. ¿Cuántas horas-técnico entregan?", ["Se multiplican técnicos, horas y días.", "3 por 6 por 10 son 180."], "180 horas-técnico"),
    ],
    mistakes=[("Calcular la carga sin multiplicar por el número de equipos.", "Cada equipo genera su propia carga.", "Multiplica la carga de un equipo por los equipos iguales."),
              ("Comparar la carga con las horas del mes en vez de la capacidad real.", "Los técnicos no trabajan las 24 horas del día.", "Calcula la capacidad con técnicos, horas diarias y días hábiles.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué son las horas-técnico?", "Las horas de trabajo de los técnicos", "Las horas que opera un equipo", "Las horas de parada de la planta", "Las horas-técnico miden trabajo humano, no operación del equipo."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es la capacidad del equipo de técnicos?", "Las horas-técnico que puede entregar", "Las horas-técnico que pide el plan", "El costo de una hora de técnico", "La capacidad es lo que el equipo puede aportar."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué se hace si la carga supera la capacidad?", "Se pide más personal o se reprograma", "Se omiten las tareas sin informar", "Se anotan como hechas", "El plan debe ser cumplible o ajustarse con informe."),
        ("=", "{F} ¿Cuántas inspecciones al mes necesita cada bomba?", "600//100", "Se dividen las horas de operación entre el intervalo.", " inspecciones"),
        ("=", "{F} ¿Cuántas horas-técnico pide al mes la lubricación de una bomba?", "600//300*3", "Se calculan las lubricaciones del mes y se multiplican por sus horas de trabajo.", " horas-técnico"),
        ("=", "{F} ¿Cuántas horas-técnico pide al mes las inspecciones de una bomba?", "600//100*2", "Se calculan las inspecciones del mes y se multiplican por sus horas.", " horas-técnico"),
        ("=", "{F} Considerando solo inspecciones y lubricación, ¿cuántas horas-técnico pide al mes la planta con las 6 bombas?", "6*(600//100*2+600//300*3)", "Se suma la carga de una bomba y se multiplica por las 6 bombas.", " horas-técnico"),
        ("=", "{F} ¿Cuántas horas-técnico entrega al mes el equipo de técnicos?", "2*8*20", "Se multiplican técnicos, horas por día y días hábiles.", " horas-técnico"),
        ("=", "{F} Cada bomba necesita su revisión general cada 3.000 horas de operación. ¿Cuántos meses de operación pasan entre una revisión general y la siguiente, a 600 horas al mes?", "3000//600", "Se dividen las horas del intervalo entre las horas de operación por mes.", " meses"),
        ("abc", "{F} Un jefe dice: «con 2 técnicos alcanza para todo y sobran horas». ¿Qué conclusión corresponde con los números de la planilla?", "Hay que comparar la carga mensual total con la capacidad de 320 horas-técnico antes de afirmarlo", "Es cierto siempre que haya 2 técnicos", "Es cierto si no hay inspecciones", "La capacidad se compara con la carga calculada."),
        ("abc", "{F} Un técnico propone omitir las lubricaciones del mes para no pasarse de la capacidad. ¿Qué respuesta es correcta?", "No corresponde: se reprograma o se pide más personal, informando a la jefatura", "Corresponde, porque la lubricación es menos importante", "Corresponde, si lo anota como hecho", "No se omiten tareas ocultándolo ante la jefatura."),
        ("=", "{F} Si el equipo gasta 108 horas-técnico en el mes, ¿cuánto cuesta la mano de obra a $9.000 la hora?", "108*9000", "Se multiplican las horas-técnico por el costo de cada hora.", " pesos de ejemplo"),
        ("Una parada no programada de una bomba dura 5 horas. ¿Cuánto cuesta, a $30.000 la hora de ejemplo?", "150.000 pesos de ejemplo", "Se multiplican las 5 horas por el costo de cada hora."),
    ],
    ctx=("abc", "El jefe de ejemplo pide un plan mensual y no sabe si el equipo alcanza. ¿Qué dos cálculos le propones?", "La carga de trabajo del plan y la capacidad del equipo de técnicos", "Solo el costo de los repuestos", "Solo el número de bombas", "Para decidir se compara carga con capacidad."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cómo se calcula la capacidad mensual?", "Técnicos por horas diarias por días hábiles", "Se multiplica lo que el equipo puede entregar."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se multiplica para obtener la carga de una tarea?", "Las veces por mes por las horas de trabajo de cada vez", "La carga es lo que pide el plan."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se hace si el plan no alcanza?", "Se pide más personal o se reprograma", "Se informa y se ajusta el plan."),
    ],
    op=("Ficha de ejemplo: 4 ventiladores operan 400 horas al mes. Pauta: inspección cada 100 horas (2 horas de trabajo) y lubricación cada 200 horas (3 horas de trabajo). El taller tiene 1 técnico que trabaja 8 horas por día en 20 días. Costo de ejemplo: $8.000 por hora-técnico. Escribe (a) la carga mensual de un ventilador, (b) la carga de los 4, (c) si la capacidad alcanza, (d) el costo de la mano de obra del mes.",
        "(a) Inspecciones: 400 ÷ 100 × 2 = 8 horas; lubricación: 400 ÷ 200 × 3 = 6 horas; total 14 horas. (b) 4 × 14 = 56 horas-técnico. (c) La capacidad es 1 × 8 × 20 = 160 horas, por lo que alcanza. (d) 56 × 8.000 = 448.000 pesos de ejemplo.",
        ["calcula la carga de un ventilador", "calcula la carga total", "compara con la capacidad", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por los equipos", "comparar con las horas del mes", "equivocarse de costo"],
        "Pregunta: «¿cuántas veces al mes se hace cada tarea?». Si duda, pídele que divida las horas de operación entre el intervalo."),
    reinforce="Inventa una pauta con dos tareas y calcula la carga mensual de tres equipos iguales.",
    extend="Explica con un ejemplo por qué comparar la carga con la capacidad evita prometer un plan imposible.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Una cinta transportadora ficticia deja de funcionar. Síntomas anotados por el operador: el motor eléctrico no parte; huele a quemado cerca del tablero; el reductor (caja que baja la velocidad del giro) hace un ruido metálico; la correa patina. "
     "Peligros anotados: energía eléctrica, partes giratorias, calor, energía almacenada y ruido. Equipos de medición del taller: multímetro (mide voltaje, corriente y resistencia), pinza amperimétrica (mide corriente sin abrir el circuito), termómetro infrarrojo y manómetro.")
build(
    O2, 1, F,
    use="Aprenderé qué es un diagnóstico, qué instrumentos se usan para comprobar un equipo, qué riesgos tiene medir y quién puede hacerlo.",
    prior=["Sé qué es el mantenimiento electromecánico.", "Sé qué son las energías de un equipo.", "Sé qué es un instrumento de medición."],
    explain=[
        "Comprobar el funcionamiento es verificar si un equipo se comporta como pide el fabricante. El diagnóstico parte de los síntomas, que es lo que se observa, como un ruido o un olor, y busca la causa, que es lo que produce el problema. Un síntoma puede tener varias causas posibles, por eso se mide y se compara con el manual. Los problemas pueden ser eléctricos, mecánicos, hidráulicos o neumáticos.",
        "Los instrumentos más comunes son el multímetro, que mide voltaje, corriente y resistencia; la pinza amperimétrica, que mide corriente; el termómetro infrarrojo, que mide temperatura a distancia, y el manómetro, que mide presión. Medir en un equipo con energía tiene riesgos eléctricos y mecánicos, por lo que solo lo hace personal autorizado con la formación y la norma vigente, según la SEC en lo eléctrico.",
        f"Aquí se aprende a interpretar datos y no a medir. {EMER} {AVISO}",
    ],
    vocab=[("diagnóstico", "análisis que va de los síntomas a la causa del problema"), ("síntoma", "lo que se observa de un problema, como un ruido o un olor"), ("causa", "lo que produce el problema"), ("multímetro", "instrumento que mide voltaje, corriente y resistencia"), ("pinza amperimétrica", "instrumento que mide corriente"), ("manómetro", "instrumento que mide presión")],
    worked=[
        ("Síntoma o causa", "Un operador de ejemplo dice: «la correa patina». ¿Es un síntoma o una causa?", ["Lo observa desde fuera, sin explicar por qué ocurre.", "Es un síntoma."], "Un síntoma"),
        ("Elegir el instrumento", "Se quiere saber la presión de un circuito de aire de ejemplo. ¿Qué instrumento corresponde?", ["La presión se mide con un instrumento específico.", "Ese instrumento es el manómetro."], "El manómetro"),
    ],
    mistakes=[("Cambiar una pieza sin medir, solo por el síntoma.", "Un síntoma puede tener varias causas y se cambiaría la pieza equivocada.", "Mide, compara con el manual y luego decide."),
              ("Creer que leer sobre instrumentos habilita para medir en equipos con energía.", "Medir exige formación, autorización y norma vigente.", "Aprende a interpretar datos y deja la medición a personal autorizado.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es un síntoma?", "Lo que se observa de un problema, como un ruido o un olor", "Lo que produce el problema", "El instrumento con que se mide el problema", "El síntoma se observa; la causa explica por qué ocurre."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué mide un manómetro?", "La presión", "El voltaje", "La resistencia", "El manómetro mide presión; el multímetro mide magnitudes eléctricas."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es un diagnóstico?", "El análisis que va de los síntomas a la causa del problema", "La reparación del equipo", "El cambio de una pieza", "El diagnóstico busca la causa antes de decidir."),
        ("abc", "{F} ¿Cuál de los síntomas de la ficha es de tipo mecánico?", "El ruido metálico del reductor", "El olor a quemado del tablero", "El motor que no parte", "El ruido metálico del reductor apunta a piezas mecánicas."),
        ("abc", "{F} ¿Qué instrumento de la ficha mide temperatura a distancia?", "El termómetro infrarrojo", "El multímetro", "El manómetro", "El infrarrojo mide temperatura sin tocar."),
        ("abc", "{F} ¿Qué instrumento de la ficha mide corriente?", "La pinza amperimétrica", "El manómetro", "El termómetro infrarrojo", "La pinza amperimétrica mide corriente; el manómetro mide presión."),
        ("=", "{F} ¿Cuántos síntomas anotó el operador?", "4", "Se cuentan los síntomas de la ficha: motor, olor, ruido y correa.", " síntomas"),
        ("=", "{F} La planta tiene 8 cintas iguales y el taller revisa 2 por día. ¿Cuántos días toma revisarlas todas?", "8//2", "Se dividen las cintas entre las que se revisan por día.", " días"),
        ("abc", "{F} El «olor a quemado» cerca del tablero sugiere un riesgo eléctrico. ¿Qué corresponde?", "Informar de inmediato y que solo personal autorizado revise", "Abrir el tablero para mirar", "Rociar el tablero con agua", "Un olor a quemado puede indicar un recalentamiento o un incendio en inicio."),
        ("abc", "{F} Un practicante dice: «cambio el motor de inmediato, que es lo que no parte». ¿Qué respuesta es correcta?", "Primero se mide y diagnostica: la causa puede ser eléctrica, mecánica o de control", "Es correcto, porque el síntoma ya lo dice", "Es correcto, si el motor es antiguo", "El síntoma no entrega la causa."),
        ("abc", "{F} El operador sugiere medir la corriente del motor con el equipo funcionando. ¿Qué respuesta es correcta?", "Solo personal autorizado mide, con la formación y la norma vigente, y no un estudiante", "Cualquier persona con un multímetro puede hacerlo", "Se puede hacer si se usa casco", "Medir en equipos con energía exige autorización."),
        ("=", "{F} El taller anota 3 mediciones por equipo en 6 equipos. ¿Cuántas mediciones registra?", "3*6", "Se multiplican las mediciones por los equipos.", " mediciones"),
        ("abc", "Durante una visita a una planta de ejemplo, un motor eléctrico humea y se oye un chispazo. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte para desconectarlo", "Tirar agua sobre el motor", "Intervenir sin formación puede causar una descarga o un incendio mayor."),
    ],
    ctx=("abc", "Un compañero de ejemplo dice: «el multímetro es fácil, midamos el tablero de la cinta». ¿Qué respondes?", "Que medir en un equipo con energía exige personal autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, si vamos con cuidado", "Que sí, si el tablero parece apagado", "Este cuaderno no habilita para medir en equipos con energía."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué mide un multímetro?", "Voltaje, corriente y resistencia", "Es el instrumento eléctrico básico de un taller."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se hace antes de cambiar una pieza?", "Se mide y se diagnostica", "Un síntoma puede tener varias causas."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿quién mide en un equipo con energía?", "Personal autorizado", "Exige formación, autorización y norma vigente para hacerlo."),
    ],
    op=("Ficha de ejemplo: una prensa ficticia deja de subir su presión. Síntomas anotados: la aguja del manómetro marca menos que lo normal; hay un siseo cerca de una unión; el motor funciona sin problemas. Instrumentos del taller: multímetro, manómetro y termómetro infrarrojo. Escribe (a) cuáles son síntomas, (b) qué instrumento se usa para presión, (c) dos causas posibles del siseo que un diagnóstico debería verificar y (d) quién hace la medición.",
        "(a) La baja presión en el manómetro, el siseo y el funcionamiento normal del motor. (b) El manómetro. (c) Una fuga en una unión o una manguera dañada. (d) Personal autorizado.",
        ["identifica los síntomas", "elige el instrumento", "propone causas posibles", "indica quién mide"],
        ["hoja con las cuatro respuestas"],
        ["confundir síntoma con causa", "cambiar una pieza sin diagnóstico", "decir que mide cualquiera"],
        "Pregunta: «¿esto se observa o es lo que lo produce?». Si duda, pídele que relea síntoma y causa."),
    reinforce="Escribe dos síntomas inventados de un equipo y dos causas posibles para cada uno.",
    extend="Explica con un ejemplo por qué un mismo síntoma puede tener varias causas.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (magnitudes y relaciones de ejemplo; solo para calcular en papel). Voltaje en volts (V); corriente en amperes (A); resistencia en ohms (Ω); potencia en watts (W). Relaciones de ejemplo: voltaje = corriente × resistencia; potencia = voltaje × corriente. "
     "Placa de ejemplo de un motor ficticio: 400 V; 10 A. Una resistencia de ejemplo de 20 Ω con 5 A de corriente. Un calefactor ficticio con 200 V y 4 A. "
     "Tabla de valores esperados de ejemplo para un motor sano: corriente medida hasta 11 A; temperatura de la carcasa hasta 70 °C.")
build(
    O2, 2, F,
    use="Aprenderé las magnitudes eléctricas básicas y sus unidades, a calcular con las relaciones de ejemplo y a comparar un valor medido con una tabla de valores esperados.",
    prior=["Sé multiplicar y dividir enteros.", "Sé qué es un instrumento de medición.", "Sé leer una tabla."],
    explain=[
        "El voltaje (V) es el empuje que mueve la electricidad, la corriente (A) es la cantidad de electricidad que circula, la resistencia (Ω) es la oposición al paso de la corriente y la potencia (W) es la energía que se usa por segundo. En los ejemplos de este cuaderno se relacionan así: voltaje = corriente × resistencia, y potencia = voltaje × corriente. Con ellas se calcula una magnitud si se conocen las otras dos.",
        "La placa de un motor es una etiqueta con sus datos nominales, como el voltaje y la corriente para los que fue hecho. Una tabla de valores esperados dice cuánto se acepta que mida un equipo sano; un valor medido por sobre lo esperado indica un problema posible. Las mediciones reales se hacen con instrumentos por personal autorizado, con la norma vigente y la SEC en lo eléctrico.",
        f"Los números son de ejemplo, solo para calcular en papel. {EMER} {AVISO}",
    ],
    vocab=[("voltaje", "magnitud eléctrica medida en volts (V)"), ("corriente", "cantidad de electricidad que circula, medida en amperes (A)"), ("resistencia", "oposición al paso de la corriente, medida en ohms (Ω)"), ("potencia", "energía que se usa por segundo, medida en watts (W)"), ("placa", "etiqueta de un equipo con sus datos nominales"), ("valor esperado", "valor que se acepta para un equipo sano")],
    worked=[
        ("Calcular el voltaje", "En un circuito de ejemplo la resistencia es de 10 Ω y la corriente de 3 A. ¿Cuántos volts hay?", ["voltaje es corriente por resistencia.", "3 por 10 son 30."], "30 V"),
        ("Calcular la potencia", "Un aparato de ejemplo trabaja con 100 V y 2 A. ¿Cuántos watts usa?", ["potencia es voltaje por corriente.", "100 por 2 son 200."], "200 W"),
    ],
    mistakes=[("Confundir voltaje con corriente.", "El voltaje se mide en V y la corriente en A y son magnitudes distintas.", "Escribe siempre la unidad con el número."),
              ("Usar las relaciones de ejemplo para dimensionar una instalación real.", "Los valores reales los fija el proyecto y la norma vigente.", "Úsalas solo para entender y calcular en papel.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿en qué unidad se mide la corriente?", "En amperes (A)", "En volts (V)", "En ohms (Ω)", "La corriente se mide en amperes."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es la resistencia eléctrica?", "La oposición al paso de la corriente", "La cantidad de electricidad que circula", "La energía que se usa por segundo", "La resistencia se opone al paso de la corriente."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es la placa de un motor?", "Una etiqueta con sus datos nominales", "Una pieza que lo protege de golpes", "El manual de mantenimiento", "La placa informa los datos para los que fue hecho."),
        ("=", "{F} ¿Cuántos volts hay en la resistencia de 20 Ω con 5 A?", "5*20", "Se aplica voltaje igual a corriente por resistencia.", " V"),
        ("=", "{F} ¿Cuántos watts usa el calefactor ficticio?", "200*4", "Se aplica potencia igual a voltaje por corriente.", " W"),
        ("abc", "{F} ¿Cuál es la corriente indicada en la placa del motor?", "10 A", "400 A", "11 A", "La placa dice 400 V y 10 A; 11 A es el límite esperado."),
        ("=", "{F} ¿Cuántos watts usa el motor, con los datos de su placa?", "400*10", "Se multiplica el voltaje por la corriente.", " W"),
        ("=", "En un circuito de ejemplo hay 60 V y 3 A. Si voltaje = corriente × resistencia, ¿cuántos ohms tiene la resistencia?", "60//3", "La resistencia es el voltaje dividido por la corriente.", " Ω"),
        ("=", "Un aparato de ejemplo usa 600 W con 200 V. Si potencia = voltaje × corriente, ¿cuántos amperes circulan?", "600//200", "La corriente es la potencia dividida por el voltaje.", " A"),
        ("abc", "{F} Un motor sano de la ficha mide 9 A en uso. ¿Qué conclusión corresponde con la tabla de valores esperados?", "Está dentro de lo esperado, porque 9 A no supera los 11 A", "Está fuera de lo esperado, porque 9 es distinto de 10", "No se puede concluir nada", "La tabla acepta hasta 11 A."),
        ("abc", "{F} Un motor mide 14 A y la tabla acepta hasta 11 A. ¿Qué corresponde?", "Informar a la jefatura: la corriente supera lo esperado y puede haber un problema eléctrico o mecánico", "Ignorarlo, porque 14 es un número cercano a 10", "Anotar 11 A en el registro", "Un valor sobre el límite se informa y se investiga."),
        ("abc", "{F} Un practicante dice: «con estas fórmulas puedo calcular el cable de la instalación del taller». ¿Qué respuesta es correcta?", "Es falso: son relaciones de ejemplo; la instalación real la dimensiona personal autorizado con la norma vigente", "Es cierto, porque las fórmulas son exactas", "Es cierto, si usa los datos de la placa", "Las fórmulas del cuaderno son de ejemplo para aprender."),
        ("=", "Una planta de ejemplo tiene 5 motores iguales al de la ficha, cada uno con 400 V y 10 A. ¿Cuántos watts suman con esas relaciones?", "5*400*10", "Se multiplica el voltaje por la corriente de cada motor y por los 5 motores.", " W"),
    ],
    ctx=("abc", "Un técnico de ejemplo mide 15 A en un motor cuya placa dice 10 A y la tabla acepta hasta 11 A. ¿Qué propones?", "Informar el valor a la jefatura y que personal autorizado investigue la causa", "Anotar 10 A para que coincida con la placa", "Esperar a que falle", "Un valor sobre el esperado se registra tal cual y se investiga."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cómo se relacionan voltaje, corriente y resistencia en los ejemplos?", "Voltaje es corriente por resistencia", "Es la relación que se usa en los cálculos de papel."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿cómo se calcula la potencia en los ejemplos?", "Voltaje por corriente", "La potencia usa voltaje y corriente."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se hace con un valor medido sobre el límite esperado?", "Se informa y se investiga", "No se oculta ni se cambia."),
    ],
    op=("Ficha de ejemplo: la placa de un motor ficticio dice 200 V y 6 A. Una resistencia de ejemplo de 8 Ω tiene 5 A. Tabla de valores esperados de ejemplo: corriente hasta 7 A. Se midieron 9 A. Escribe (a) la potencia del motor según la placa, (b) los volts de la resistencia, (c) si la corriente medida está dentro de lo esperado, (d) qué haces con ese dato.",
        "(a) 200 × 6 = 1.200 W. (b) 5 × 8 = 40 V. (c) No, 9 A supera los 7 A esperados. (d) Registrarlo tal cual e informar a la jefatura para que personal autorizado investigue.",
        ["calcula la potencia", "calcula los volts", "compara con lo esperado", "propone informar"],
        ["hoja con las cuatro respuestas"],
        ["sumar en vez de multiplicar", "alterar el dato", "no informar"],
        "Pregunta: «¿la tabla acepta hasta cuánto?». Si duda, pídele que relea el valor esperado."),
    reinforce="Inventa un aparato con voltaje y corriente y calcula su potencia; luego inventa un valor esperado y un valor medido y compáralos.",
    extend="Explica con un ejemplo por qué una corriente medida sobre lo esperado puede indicar un problema mecánico y no solo eléctrico.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (registro de mediciones de ejemplo, inventado; las tomó personal autorizado). Cinta transportadora ficticia con motor de placa 400 V y 10 A. Tabla de valores esperados de ejemplo: corriente hasta 11 A; temperatura de la carcasa hasta 70 °C; temperatura del reductor hasta 65 °C; presión del circuito de lubricación entre 3 y 5 unidades de ejemplo. "
     "Mediciones del día: corriente 14 A; temperatura de la carcasa 85 °C; temperatura del reductor 90 °C; presión de lubricación 2 unidades de ejemplo. Síntomas: el motor se calienta; el reductor suena. Última lubricación del reductor: hace 3.000 horas de operación; la pauta pide cada 500.")
build(
    O2, 3, F,
    use="Aprenderé a leer un registro de mediciones, a compararlo con valores esperados, a proponer causas posibles y a decidir qué informar sin intervenir.",
    prior=["Sé comparar un valor con un límite.", "Sé qué es un síntoma y una causa.", "Sé que las mediciones las hace personal autorizado."],
    explain=[
        "Un diagnóstico por comparación contrasta cada medición con su valor esperado y clasifica lo que está dentro y fuera de lo esperado. Cuando varias variables fallan a la vez, se busca una causa común. Una corriente alta con calentamiento del motor y un reductor muy caliente puede indicar una sobrecarga mecánica; una presión de lubricación baja con una lubricación atrasada apunta a falta de lubricante. Son hipótesis a verificar, no certezas.",
        "El informe del diagnóstico anota los valores medidos, los esperados, lo que está fuera, las hipótesis y la recomendación, que puede ser detener el equipo por una decisión de la jefatura. La intervención la hace personal autorizado con el manual del fabricante. Una recomendación sin evidencia no sirve.",
        f"Es un análisis de papel. {EMER} {AVISO}",
    ],
    vocab=[("hipótesis", "explicación posible que debe verificarse"), ("sobrecarga mecánica", "esfuerzo mayor que el que el equipo debería soportar"), ("lubricante", "aceite o grasa que reduce el roce entre piezas"), ("causa común", "una causa que explica varios síntomas a la vez"), ("recomendación", "propuesta que sale del diagnóstico")],
    worked=[
        ("Comparar con lo esperado", "Una temperatura de ejemplo de 72 °C se compara con un límite esperado de 70 °C. ¿Está dentro de lo esperado?", ["72 es mayor que 70.", "Supera el límite."], "No, supera el límite"),
        ("Causa común", "Un equipo de ejemplo tiene el motor caliente, una corriente alta y un ruido metálico. ¿Qué tipo de hipótesis puede explicar los tres síntomas?", ["Los tres pueden venir de un esfuerzo excesivo.", "Una sobrecarga mecánica es una causa común posible."], "Una sobrecarga mecánica"),
    ],
    mistakes=[("Presentar una hipótesis como si fuera una certeza.", "Una hipótesis debe verificarse antes de actuar.", "Escribe «posible causa» y propone cómo verificarla."),
              ("Informar solo los valores que están fuera y omitir los que están dentro.", "Los valores dentro de lo esperado también orientan el diagnóstico.", "Anota todas las mediciones y su comparación.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es una hipótesis en un diagnóstico?", "Una explicación posible que debe verificarse", "Una causa ya demostrada", "Un valor medido con un instrumento", "La hipótesis aún no está comprobada."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es una sobrecarga mecánica?", "Un esfuerzo mayor que el que el equipo debería soportar", "Un exceso de lubricante", "Una falla del instrumento de medición", "La sobrecarga exige más esfuerzo del que el equipo soporta."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es una causa común?", "Una causa que explica varios síntomas a la vez", "La causa más frecuente de todas las fallas", "El síntoma más visible", "Busca un origen único para varios síntomas."),
        ("=", "{F} ¿Cuántos A supera la corriente medida el valor esperado máximo?", "14-11", "Se resta el valor esperado a la corriente medida.", " A"),
        ("=", "{F} ¿Cuántos °C supera la temperatura del reductor el valor esperado máximo?", "90-65", "Se resta el valor esperado a la temperatura medida.", " °C"),
        ("abc", "{F} ¿Cuántas de las cuatro mediciones del día están fuera de lo esperado?", "Las cuatro", "Solo dos", "Solo una", "Corriente, dos temperaturas y presión están fuera de lo esperado."),
        ("=", "{F} ¿Cuántas horas de operación se pasó la lubricación del reductor, respecto de lo que pide la pauta?", "3000-500", "Se resta el intervalo de la pauta a las horas transcurridas.", " horas"),
        ("=", "{F} ¿Cuántas lubricaciones se debieron hacer en esas 3.000 horas, con intervalo de 500?", "3000//500", "Se divide el tiempo transcurrido entre el intervalo.", " lubricaciones"),
        ("abc", "{F} ¿Qué hipótesis relaciona la presión de lubricación baja, el reductor caliente y la lubricación atrasada?", "Falta de lubricante en el reductor, a verificar por personal autorizado", "Un error del multímetro", "Un exceso de voltaje en la red", "La lubricación baja y atrasada explica el calentamiento."),
        ("abc", "{F} Un practicante dice: «ya sé qué falla: es la falta de lubricante, voy a engrasar de inmediato». ¿Qué respuesta es correcta?", "No corresponde: es una hipótesis a verificar y la intervención la hace personal autorizado con el manual", "Corresponde, porque está seguro", "Corresponde, si lo hace rápido", "Una hipótesis no autoriza a intervenir."),
        ("abc", "{F} Un jefe pregunta qué incluye el informe. ¿Cuál es la respuesta más completa?", "Valores medidos, valores esperados, lo que está fuera, hipótesis y recomendación", "Solo la conclusión", "Solo los valores medidos", "El informe debe permitir revisar el razonamiento."),
        ("=", "{F} Si la corriente subiera en la siguiente medición a 15 A, ¿cuántos A estaría sobre el esperado de 11 A?", "15-11", "Se resta el esperado a la nueva medición.", " A"),
        ("En una planta de ejemplo hay 4 mediciones fuera de lo esperado en un equipo y 2 en otro. ¿Cuántas mediciones fuera de lo esperado hay entre los dos?", "6 mediciones", "Se suman las mediciones de ambos equipos."),
    ],
    ctx=("abc", "El jefe de ejemplo pide una decisión rápida sobre la cinta. El registro muestra cuatro variables fuera de lo esperado. ¿Qué recomendarías?", "Informar los datos y recomendar que la jefatura evalúe detener el equipo para que personal autorizado intervenga", "Seguir operando hasta fin de turno", "Medir de nuevo con una herramienta cualquiera", "Varias variables fuera de lo esperado justifican evaluar detener el equipo."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cómo se compara una medición?", "Con su valor esperado", "La comparación muestra si está dentro o fuera."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué es una causa común?", "Una causa que explica varios síntomas", "Puede unir síntomas distintos en un solo origen."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué nunca se debe presentar como certeza?", "Una hipótesis", "Debe verificarse antes de decidir cualquier intervención."),
    ],
    op=("Ficha de ejemplo: un ventilador ficticio con valores esperados: corriente hasta 8 A, temperatura del motor hasta 75 °C, vibración hasta 6 unidades de ejemplo. Mediciones: corriente 10 A; temperatura 80 °C; vibración 9. Síntomas: ruido nuevo. Última revisión de los rodamientos: hace 8.000 horas; la pauta pide cada 4.000. Escribe (a) cuántas mediciones están fuera de lo esperado, (b) cuánto supera cada una el valor esperado, (c) una hipótesis, (d) una recomendación.",
        "(a) Las tres. (b) Corriente: 2 A; temperatura: 5 °C; vibración: 3 unidades. (c) Desgaste o falta de revisión de los rodamientos, atrasada en 4.000 horas, a verificar. (d) Informar a la jefatura y proponer que personal autorizado revise los rodamientos.",
        ["cuenta las mediciones fuera de lo esperado", "calcula las diferencias", "formula una hipótesis", "propone una recomendación"],
        ["hoja con las cuatro respuestas"],
        ["presentar la hipótesis como certeza", "omitir mediciones", "recomendar intervenir sin autorización"],
        "Pregunta: «¿qué dato apunta a los rodamientos?». Si duda, pídele que relea la pauta y la última revisión."),
    reinforce="Inventa tres mediciones con sus valores esperados y clasifícalas como dentro o fuera.",
    extend="Explica con un ejemplo por qué una hipótesis se verifica antes de intervenir.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (cálculo de consumo y de costo de ejemplo). Motor ficticio de la cinta: 400 V y 10 A; potencia = voltaje × corriente. Funciona 16 horas por día durante 20 días al mes. Un kilowatt-hora (kWh) es la energía de 1.000 W durante 1 hora. "
     "Precio de ejemplo de la energía: $100 por kWh. Con una falla, el motor consume 14 A en vez de 10 A con el mismo voltaje. Tabla de valores esperados de ejemplo: corriente hasta 11 A.")
build(
    O2, 4, F,
    use="Aprenderé a calcular la potencia, el consumo en kWh y el costo de ejemplo de un motor sano y de uno con falla, y a decidir con esos datos.",
    prior=["Sé qué es potencia y su relación con voltaje y corriente.", "Sé multiplicar y dividir enteros.", "Sé pasar W a kW."],
    explain=[
        "La potencia de un motor, en los ejemplos, es el voltaje por la corriente, en watts. La energía consumida se mide en kilowatt-hora (kWh): un kilowatt-hora es la energía de 1.000 W durante 1 hora. Para calcularla se multiplica la potencia en kW por las horas de funcionamiento; para pasar de W a kW se divide por 1.000. El costo es los kWh por el precio de cada kWh.",
        "Una falla que aumenta la corriente aumenta la potencia y el costo de energía, y además calienta el equipo. Comparar el consumo de un motor sano con el de uno con falla ayuda a decidir si conviene reparar de inmediato. Los precios y valores de este cuaderno son de ejemplo.",
        f"El cálculo es de papel; no se mide ningún motor. {EMER} {AVISO}",
    ],
    vocab=[("kilowatt (kW)", "mil watts"), ("kilowatt-hora (kWh)", "energía de 1.000 W durante 1 hora"), ("consumo", "energía que usa un equipo en un periodo"), ("costo de energía", "kWh multiplicados por el precio de cada kWh"), ("sobreconsumo", "consumo mayor que el esperado")],
    worked=[
        ("Calcular el consumo", "Un aparato de ejemplo tiene 2 kW y funciona 5 horas. ¿Cuántos kWh consume?", ["Se multiplican los kW por las horas.", "2 por 5 son 10."], "10 kWh"),
        ("Pasar de W a kW", "Un motor de ejemplo tiene 3.000 W. ¿Cuántos kW son?", ["Se divide por 1.000.", "3.000 dividido en 1.000 son 3."], "3 kW"),
    ],
    mistakes=[("Multiplicar los watts por las horas y llamar al resultado kWh.", "Para kWh la potencia debe estar en kW.", "Divide los watts por 1.000 antes de multiplicar."),
              ("Ignorar el costo de una falla que sube el consumo.", "El sobreconsumo se paga todos los meses.", "Calcula el costo adicional y compáralo con la reparación.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es un kilowatt-hora?", "La energía de 1.000 W durante 1 hora", "La potencia de 1 W durante 1.000 horas", "La corriente de 1 A durante 1 hora", "Un kWh combina potencia en kW y tiempo en horas."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es el sobreconsumo?", "Un consumo mayor que el esperado", "Un consumo igual al esperado", "El precio de la energía", "Sobre indica por encima de lo esperado."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿cómo se pasa de W a kW?", "Dividiendo por 1.000", "Multiplicando por 1.000", "Sumando 1.000", "Un kilowatt equivale a 1.000 watts."),
        ("=", "{F} ¿Cuántos watts tiene el motor sano?", "400*10", "Se multiplica el voltaje por la corriente.", " W"),
        ("=", "{F} ¿Cuántas horas al mes funciona el motor?", "16*20", "Se multiplican las horas por día por los días del mes.", " horas"),
        ("=", "{F} ¿Cuántos kWh consume el motor sano en el mes?", "400*10//1000*16*20", "Se pasa la potencia a kW y se multiplica por las horas del mes.", " kWh"),
        ("=", "{F} ¿Cuántos pesos de ejemplo cuesta la energía del motor sano en el mes?", "400*10//1000*16*20*100", "Se multiplican los kWh por el precio.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántos watts tiene el motor con la falla, con 14 A?", "400*14", "Se multiplica el voltaje por la corriente con falla.", " W"),
        ("=", "{F} ¿Cuántos kWh más consume al mes el motor con la falla, con 5.600 W frente a 4.000 W?", "(5600-4000)*16*20//1000", "Se calcula la diferencia en W, se multiplica por las horas y se pasa a kWh.", " kWh"),
        ("abc", "{F} ¿Qué dice la tabla de valores esperados sobre la corriente de 14 A?", "Supera los 11 A, así que está fuera de lo esperado", "Está dentro de lo esperado", "No se puede comparar", "El límite esperado es 11 A."),
        ("abc", "{F} Un jefe dice: «el sobreconsumo es pequeño, no vale la pena revisarlo». ¿Qué respuesta es correcta?", "Hay que calcular el costo adicional y considerar que una corriente alta también calienta el equipo y puede causar una falla mayor", "Tiene razón, porque la diferencia es de unos pesos", "Tiene razón, porque el motor sigue funcionando", "El sobreconsumo se paga todos los meses y avisa de un problema."),
        ("=", "{F} Con el costo adicional de energía del mes, ¿cuántos pesos de ejemplo pierde al mes la falla? Usa los 512 kWh adicionales y el precio de $100 por kWh.", "512*100", "Se multiplican los kWh adicionales por el precio.", " pesos de ejemplo"),
        ("Un motor de ejemplo de 2.000 W funciona 10 horas por día en 20 días. ¿Cuántos kWh consume al mes?", "400 kWh", "2 kW por 200 horas dan 400 kWh."),
    ],
    ctx=("abc", "El jefe de ejemplo duda si reparar un motor que consume más de lo esperado. ¿Qué datos le propones calcular?", "El consumo y el costo adicional de energía, y compararlos con el costo de la reparación y los riesgos", "Solo el color del motor", "Solo el precio del motor nuevo", "La decisión se apoya en consumo, costo y riesgo."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cuántos kWh consume un aparato de 2 kW en 5 horas?", "10 kWh", "Se multiplican los kW por las horas."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué aumenta una falla que sube la corriente?", "El consumo y el calentamiento", "Más corriente significa más potencia y más calor."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿cómo se calcula el costo de energía?", "kWh por el precio de cada kWh", "Se multiplica el consumo por el precio."),
    ],
    op=("Ficha de ejemplo: un motor ficticio de 200 V y 10 A funciona 10 horas por día durante 20 días al mes. Precio de ejemplo: $100 por kWh. Con una falla consume 15 A. Escribe (a) los kWh que consume el motor sano al mes, (b) los kWh con la falla, (c) la diferencia en pesos de ejemplo al mes, (d) una recomendación.",
        "(a) 200 × 10 = 2.000 W = 2 kW; 2 × 200 horas = 400 kWh. (b) 200 × 15 = 3.000 W = 3 kW; 3 × 200 = 600 kWh. (c) 600 − 400 = 200 kWh; 200 × 100 = 20.000 pesos de ejemplo. (d) Informar la falla para que personal autorizado la revise, porque el sobreconsumo y el calentamiento aumentan el costo y el riesgo.",
        ["calcula el consumo sano", "calcula el consumo con falla", "calcula la diferencia en pesos", "recomienda una acción"],
        ["hoja con las cuatro respuestas"],
        ["no pasar W a kW", "olvidar las horas del mes", "no recomendar nada"],
        "Pregunta: «¿usaste kW o W para los kWh?». Si duda, pídele que divida los watts por 1.000."),
    reinforce="Inventa un motor con voltaje y corriente y calcula su consumo mensual en kWh con horas y días de ejemplo.",
    extend="Explica con un ejemplo por qué una corriente alta no solo cuesta más sino que también calienta el equipo.",
)

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Una planta de ejemplo prepara el tablero de comando de una cinta transportadora ficticia: un tablero con protecciones, un contactor (interruptor que comanda un motor a distancia), un sensor que detecta cajas y un controlador programable (PLC), que ejecuta una lógica de control. "
     "Peligros anotados: contacto con partes energizadas, arco eléctrico, quemaduras, incendio por mala conexión, caída de herramientas, atrapamiento por la cinta. Documentos: plano eléctrico, lista de materiales y registro de pruebas.")
build(
    O3, 1, F,
    use="Aprenderé qué es instalar un sistema eléctrico y automatizado desde el punto de vista de sus documentos y riesgos, quién puede hacerlo y qué rol cumple la SEC.",
    prior=["Sé qué son voltaje, corriente y resistencia.", "Sé la jerarquía de controles.", "Sé que lo eléctrico lo fiscaliza la SEC."],
    explain=[
        "Instalar sistemas eléctricos, electrónicos y automatizados es dejar en su lugar y listos para funcionar tableros, motores, sensores y controladores, siguiendo planos, listas de materiales y la normativa eléctrica. Un sensor detecta una condición, como la presencia de una caja; un actuador, como un motor o un contactor, hace una acción; el controlador programable (PLC) decide qué hacer según una lógica. Los riesgos principales son el contacto con partes energizadas, el arco eléctrico, las quemaduras y el incendio por una mala conexión.",
        "En Chile, las instalaciones eléctricas deben cumplir la normativa que fiscaliza la Superintendencia de Electricidad y Combustibles (SEC) y las hacen personas con la autorización correspondiente. El registro de pruebas deja constancia de las verificaciones. Cada tarea se realiza con un procedimiento y un permiso de trabajo de la empresa.",
        f"Aquí solo se aprenden conceptos y documentos; este cuaderno no enseña a instalar ni a conectar. {EMER} {AVISO}",
    ],
    vocab=[("instalación eléctrica", "conjunto de equipos y conductores que llevan electricidad a los equipos"), ("contactor", "interruptor que comanda un motor a distancia"), ("sensor", "dispositivo que detecta una condición"), ("actuador", "dispositivo que realiza una acción, como un motor"), ("controlador programable (PLC)", "equipo que decide qué hacer según una lógica programada"), ("arco eléctrico", "descarga eléctrica que produce calor y luz intensos")],
    worked=[
        ("Sensor o actuador", "Un dispositivo de ejemplo detecta que una caja llega al final de la cinta. ¿Es un sensor o un actuador?", ["Detecta una condición.", "Es un sensor."], "Un sensor"),
        ("Documento de respaldo", "Una empresa de ejemplo quiere dejar constancia de las verificaciones hechas a un tablero. ¿Qué documento usa?", ["Las verificaciones se anotan en un registro.", "Es el registro de pruebas."], "El registro de pruebas"),
    ],
    mistakes=[("Creer que cualquier persona con herramientas puede hacer una instalación eléctrica.", "La normativa exige personas autorizadas y fiscalizadas por la SEC.", "Aprende el concepto y deja la instalación a quien está autorizado."),
              ("Pensar que un tablero sin carga no tiene peligro.", "Puede tener partes energizadas y energía almacenada.", "Considera siempre el procedimiento de la empresa.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es un sensor?", "Un dispositivo que detecta una condición", "Un dispositivo que realiza una acción", "Un cable que lleva la electricidad", "El sensor detecta; el actuador actúa."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es un contactor?", "Un interruptor que comanda un motor a distancia", "Un instrumento que mide la corriente", "Una pieza que sostiene un eje", "El contactor comanda un motor desde un circuito de control."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es el arco eléctrico?", "Una descarga que produce calor y luz intensos", "Un tipo de cable", "Un instrumento de medición", "El arco eléctrico es un peligro por calor y quemaduras."),
        ("abc", "{F} ¿Cuál de los componentes de la ficha decide qué hacer según una lógica?", "El controlador programable (PLC)", "El sensor", "El contactor", "El PLC ejecuta la lógica; el sensor detecta y el contactor actúa."),
        ("abc", "{F} ¿Qué documento de la ficha deja constancia de las verificaciones hechas?", "El registro de pruebas", "La lista de materiales", "El plano eléctrico", "El registro de pruebas anota las verificaciones."),
        ("abc", "{F} ¿Qué institución fiscaliza lo eléctrico?", "La SEC", "El Servicio de Impuestos Internos", "El Instituto Nacional de Estadísticas", "La SEC fiscaliza electricidad y combustibles."),
        ("=", "{F} ¿Cuántos peligros anotó la planta?", "6", "Se cuentan los peligros: contacto, arco, quemaduras, incendio, caída de herramientas y atrapamiento.", " peligros"),
        ("=", "{F} La planta prepara 4 tableros iguales con 1 sensor y 1 contactor cada uno. ¿Cuántos sensores y contactores se necesitan en total?", "4*(1+1)", "Se suman los dos componentes por tablero y se multiplica por los tableros.", " componentes"),
        ("abc", "{F} Una barrera física que impide tocar partes energizadas dentro del tablero es un control:", "De ingeniería", "Administrativo", "De EPP", "La barrera cambia el lugar sin depender de la conducta."),
        ("abc", "{F} Un practicante dice: «con el plano ya puedo conectar el tablero». ¿Qué respuesta es correcta?", "Es falso: la instalación la hace personal autorizado, con procedimiento y norma vigente, y este cuaderno no habilita para hacerla", "Es cierto, porque el plano lo dice todo", "Es cierto, si usa guantes", "El plano no sustituye la autorización ni el procedimiento."),
        ("abc", "En una visita a una planta de ejemplo, un tablero hace un destello fuerte y una persona queda con quemaduras. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Tocarla para ver su estado", "Abrir el tablero para apagarlo", "Un arco eléctrico puede repetirse; se pide ayuda."),
        ("=", "{F} Si cada tablero requiere 3 pruebas registradas y hay 4 tableros, ¿cuántas pruebas se registran?", "3*4", "Se multiplican las pruebas por los tableros.", " pruebas"),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué rol tiene el registro de pruebas?", "Dejar constancia de las verificaciones hechas", "Reemplazar el plano eléctrico", "Autorizar a cualquier persona a instalar", "El registro respalda lo hecho y permite revisarlo."),
    ],
    ctx=("abc", "Un amigo de ejemplo te dice: «instalemos un tomacorriente nuevo en el taller de tu casa, es fácil». ¿Qué respondes?", "Que una instalación eléctrica la hace personal autorizado con la norma vigente, y que consultarás a un adulto responsable", "Que sí, si cortamos la luz", "Que sí, si vemos un video", "Este cuaderno no habilita para instalar ni conectar."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué hace el PLC?", "Decide qué hacer según una lógica", "El controlador ejecuta la lógica programada."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué sigla corresponde a la Superintendencia de Electricidad y Combustibles?", "SEC", "Es la superintendencia de electricidad y combustibles."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿quién puede hacer una instalación eléctrica?", "Personal autorizado", "La normativa exige autorización para instalar."),
    ],
    op=("Ficha de ejemplo: una planta prepara el comando de una bomba con un sensor de nivel, un contactor, un PLC y un tablero. Peligros anotados: partes energizadas, arco eléctrico y quemaduras. Escribe (a) cuál componente es el sensor y cuál el actuador, (b) qué documento deja constancia de las pruebas, (c) un control de ingeniería para el contacto con partes energizadas, (d) quién hace la instalación. No describas cómo se conecta.",
        "(a) El sensor de nivel detecta; el contactor es el actuador. (b) El registro de pruebas. (c) Una cubierta o barrera dentro del tablero que impida tocar partes energizadas. (d) Personal autorizado, con la norma vigente.",
        ["distingue sensor y actuador", "nombra el documento", "propone un control de ingeniería", "indica quién instala"],
        ["hoja con las cuatro respuestas"],
        ["confundir sensor con actuador", "proponer solo EPP", "describir cómo se conecta"],
        "Pregunta: «¿este dispositivo detecta o actúa?». Si duda, pídele que relea las definiciones."),
    reinforce="Escribe un sensor, un actuador y un controlador de un sistema inventado de tu elección.",
    extend="Explica con un ejemplo por qué un tablero sin carga puede seguir siendo peligroso.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (documentos y símbolos descritos por escrito, de ejemplo, inventados). Plano eléctrico E-01 del tablero de una cinta ficticia, revisión B. Símbolos de la leyenda: un círculo con una M es un motor; un rectángulo con una X es un contactor; un rombo es un sensor; "
     "un rectángulo con las letras PLC es el controlador; una línea gruesa es un conductor de potencia (el que lleva la corriente al motor) y una línea fina es un conductor de control (el que lleva señales). Lista de materiales: 1 motor, 1 contactor, 2 sensores, 1 PLC, 12 m de conductor de potencia, 20 m de conductor de control, 6 abrazaderas de fijación. "
     "Rótulos del tablero: Q1 (protección general), K1 (contactor), S1 y S2 (sensores).")
build(
    O3, 2, F,
    use="Aprenderé a leer símbolos de un plano eléctrico descrito por escrito, una lista de materiales y los rótulos de un tablero, y qué hace cada rol en la instalación.",
    prior=["Sé qué es un sensor y un actuador.", "Sé leer una lista de materiales.", "Sé multiplicar enteros."],
    explain=[
        "Un plano eléctrico usa símbolos para representar los componentes: un círculo con M para un motor, un rectángulo con X para un contactor, un rombo para un sensor. La leyenda explica cada símbolo. Los conductores de potencia llevan la corriente al motor y se dibujan más gruesos; los de control llevan señales y se dibujan más finos. Los rótulos, como Q1, K1 o S1, identifican cada componente del tablero y deben coincidir con el plano y con la etiqueta física.",
        "La lista de materiales anota cuántos componentes y cuántos metros de conductor se necesitan. Las abrazaderas de fijación sujetan los conductores. Cuando el plano y la lista no coinciden, se consulta al proyectista y no se corrige por cuenta propia. El instalador autorizado ejecuta, el supervisor revisa y el inspector verifica el cumplimiento.",
        f"Aquí solo se leen documentos. {EMER} {AVISO}",
    ],
    vocab=[("leyenda", "lista que explica los símbolos de un plano"), ("conductor de potencia", "el que lleva la corriente al motor"), ("conductor de control", "el que lleva señales de control"), ("rótulo", "código que identifica un componente en el plano y en el tablero"), ("abrazadera", "pieza que sujeta conductores"), ("proyectista", "persona que diseña el sistema y emite el plano")],
    worked=[
        ("Leer un símbolo", "Un símbolo de ejemplo es un rombo. Según la leyenda del plano, ¿qué representa?", ["La leyenda dice que el rombo es un sensor.", "El rombo representa un sensor."], "Un sensor"),
        ("Contar materiales", "Una lista de ejemplo trae 3 contactores y 5 sensores. ¿Cuántos componentes suma?", ["Se suman las cantidades.", "3 más 5 son 8."], "8 componentes"),
    ],
    mistakes=[("Confundir un conductor de control con uno de potencia.", "Llevan magnitudes muy distintas y por eso se distinguen en el plano.", "Mira el grosor de la línea y la leyenda."),
              ("Corregir el plano a mano cuando la lista no coincide.", "Solo el proyectista modifica el diseño.", "Registra la diferencia y consúltala.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es la leyenda de un plano?", "La lista que explica los símbolos", "El título de la lámina", "El nombre de quien aprobó el plano", "La leyenda traduce símbolos a significados."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué lleva un conductor de potencia?", "La corriente que llega al motor", "Solo señales de control", "El aire comprimido del circuito", "El conductor de potencia alimenta al motor."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿para qué sirven los rótulos Q1, K1 o S1?", "Para identificar cada componente en el plano y en el tablero", "Para indicar la potencia de cada componente", "Para señalar el color de los conductores", "Los rótulos permiten reconocer cada componente."),
        ("abc", "{F} Según la leyenda, ¿qué representa el círculo con una M?", "Un motor", "Un contactor", "Un sensor", "La leyenda dice que el círculo con M es un motor."),
        ("abc", "{F} ¿Qué rótulo identifica el contactor?", "K1", "Q1", "S1", "La ficha dice que K1 es el contactor."),
        ("=", "{F} ¿Cuántos componentes principales suma la lista, contando motor, contactor, sensores y PLC?", "1+1+2+1", "Se suman las cantidades de los cuatro componentes.", " componentes"),
        ("=", "{F} Se fabrican 5 tableros iguales con la lista de la ficha. ¿Cuántos metros de conductor de control se necesitan?", "20*5", "Se multiplican los metros por tablero por los tableros.", " m"),
        ("=", "{F} ¿Cuántas abrazaderas se necesitan para 3 tableros iguales?", "6*3", "Se multiplican las abrazaderas por tablero por los tableros.", " abrazaderas"),
        ("abc", "{F} ¿Qué línea del plano representa el conductor que lleva señales de los sensores?", "La línea fina", "La línea gruesa", "El círculo con M", "Las señales se llevan por conductores de control, dibujados finos."),
        ("abc", "{F} La lista de materiales dice 2 sensores, pero el plano muestra 3 rombos. ¿Qué corresponde?", "Registrar la diferencia y consultarla al proyectista, sin corregirla por cuenta propia", "Usar siempre el número de la lista", "Usar siempre el número del plano", "Una discrepancia se consulta con quien emitió el documento."),
        ("abc", "{F} Un instalador propone cambiar el rótulo S2 por S3 en la etiqueta del tablero porque «queda más ordenado». ¿Qué respuesta es correcta?", "No corresponde: el rótulo debe coincidir con el plano; el cambio lo aprueba el proyectista", "Corresponde, porque es solo un nombre", "Corresponde, si lo anota a lápiz", "Un rótulo distinto del plano genera errores."),
        ("=", "{F} Si el plano tiene 12 m de conductor de potencia y se usa 1 abrazadera cada 2 m, ¿cuántas abrazaderas se necesitan solo para ese conductor?", "12//2", "Se divide la longitud entre la separación entre abrazaderas.", " abrazaderas"),
        ("En una lista de ejemplo hay Q1, Q2, K1 y S1. ¿Cuántos rótulos comienzan con la letra Q?", "2 rótulos", "Son Q1 y Q2; los demás comienzan con K y S."),
    ],
    ctx=("abc", "Un instalador de ejemplo dice: «el plano está mal, yo lo hago como creo». Como estudiante, ¿qué propones?", "Registrar la duda y consultarla al proyectista y al supervisor antes de cualquier trabajo", "Aceptar que haga lo que cree", "Cambiar el plano con lápiz", "El diseño lo corrige quien lo emitió."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué explica la leyenda?", "Los símbolos del plano", "Traduce cada símbolo a su significado."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿quién modifica el diseño del sistema?", "El proyectista", "Solo quien diseñó el sistema puede cambiarlo."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué debe coincidir con el plano?", "Los rótulos de los componentes", "Evita errores al identificar las piezas del tablero."),
    ],
    op=("Ficha de ejemplo: plano E-04 de un tablero ficticio. Leyenda: círculo con M, motor; rectángulo con X, contactor; rombo, sensor. Lista: 2 motores, 2 contactores, 4 sensores, 30 m de conductor de control, 8 abrazaderas. Rótulos: K1 y K2 (contactores), M1 y M2 (motores). Escribe (a) qué representa un rombo, (b) cuántos componentes principales suma la lista, (c) cuántos metros de conductor de control se necesitan para 3 tableros iguales, (d) qué haces si el plano muestra 5 rombos.",
        "(a) Un sensor. (b) 2 + 2 + 4 = 8 componentes. (c) 30 × 3 = 90 m. (d) Registrar la diferencia y consultarla al proyectista, sin corregirla por cuenta propia.",
        ["lee el símbolo", "suma los componentes", "calcula los metros", "propone consultar"],
        ["hoja con las cuatro respuestas"],
        ["leer mal la leyenda", "sumar mal", "corregir el plano por cuenta propia"],
        "Pregunta: «¿qué dice la leyenda del rombo?». Si duda, pídele que subraye el símbolo en la leyenda."),
    reinforce="Inventa una leyenda de tres símbolos y una lista de componentes y suma las cantidades.",
    extend="Explica con un ejemplo por qué un rótulo distinto del plano puede generar un error.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (tabla de ejemplo, solo para practicar la lectura; NO sirve para dimensionar instalaciones reales). Motor de ejemplo con 10 A. Regla de ejemplo (inventada): la capacidad del conductor y de la protección debe ser mayor o igual a la corriente del motor por 3 y dividida por 2. "
     "Conductores de ejemplo: tipo A, 15 A; tipo B, 25 A; tipo C, 40 A. Protecciones de ejemplo: P1, 16 A; P2, 25 A; P3, 40 A. Costo de ejemplo por metro: tipo A, $800; tipo B, $1.400; tipo C, $2.500. Se necesitan 20 m de conductor.")
build(
    O3, 3, F,
    use="Aprenderé a leer una tabla de selección de ejemplo, a aplicar una regla de ejemplo y a elegir en papel el componente más económico que cumple, sin dimensionar instalaciones reales.",
    prior=["Sé multiplicar y dividir enteros.", "Sé comparar números.", "Sé leer una tabla."],
    explain=[
        "Seleccionar un componente es elegir, de una tabla, el que cumple las condiciones del equipo. Primero se calcula el valor mínimo que debe cumplir el componente con la regla; luego se buscan en la tabla las opciones cuyo valor sea igual o mayor; entre las que cumplen, se elige la más económica o la que ofrezca el margen pedido. Una capacidad menor que la requerida no cumple, por barata que sea.",
        "Una protección es un dispositivo que corta o limita la corriente si esta es peligrosa; no puede tener capacidad menor que la corriente de uso ni mayor que la capacidad del conductor que protege, según la norma. En este ejercicio solo se practica la lectura de una tabla de ejemplo. Los valores reales los fija el proyecto, el fabricante y la norma vigente de la SEC.",
        f"Es un ejercicio de papel con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("capacidad", "corriente máxima que soporta un componente"), ("regla de ejemplo", "criterio inventado solo para practicar"), ("protección", "dispositivo que corta o limita la corriente peligrosa"), ("margen", "diferencia entre la capacidad y el valor mínimo requerido"), ("opción que cumple", "componente cuya capacidad es igual o mayor que la requerida")],
    worked=[
        ("Calcular el mínimo", "Un motor de ejemplo usa 8 A y la regla de ejemplo pide la corriente por 3 y dividida por 2. ¿Qué capacidad mínima requiere?", ["8 por 3 son 24.", "24 dividido en 2 son 12."], "12 A"),
        ("Elegir de la tabla", "Se requieren al menos 12 A y hay componentes de 6 A, 12 A y 20 A. ¿Qué opciones cumplen?", ["Cumplen las de capacidad igual o mayor que 12.", "Son las de 12 A y 20 A."], "Las de 12 A y 20 A"),
    ],
    mistakes=[("Elegir la opción más barata aunque su capacidad sea menor que la requerida.", "No cumple la condición mínima.", "Primero filtra las que cumplen y luego elige la más económica."),
              ("Usar esta tabla de ejemplo para una instalación real.", "Los valores reales los fija el proyecto y la norma vigente.", "Úsala solo para practicar la lectura.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es la capacidad de un conductor?", "La corriente máxima que soporta", "El largo que tiene el rollo", "El voltaje de la red", "La capacidad es el máximo de corriente que soporta."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué hace una protección?", "Corta o limita la corriente cuando es peligrosa", "Mide el voltaje del motor", "Comanda el motor a distancia", "La protección actúa frente a corrientes peligrosas."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué significa una opción que cumple en una tabla de selección?", "Que su capacidad es igual o mayor que la requerida", "Que es la más barata", "Que es la de mayor capacidad de todas", "Cumplir es alcanzar el mínimo requerido."),
        ("=", "{F} ¿Cuántos A de capacidad mínima requiere el conductor del motor, según la regla de ejemplo?", "10*3//2", "Se multiplica la corriente por 3 y se divide por 2.", " A"),
        ("abc", "{F} ¿Qué tipos de conductor de la tabla cumplen con el mínimo?", "Los tipos A, B y C", "Solo los tipos B y C", "Solo el tipo C", "Los tres tienen capacidad igual o mayor que 15 A."),
        ("abc", "{F} ¿Cuál es la protección más pequeña de la tabla que cumple con el mínimo?", "P1, de 16 A", "P2, de 25 A", "P3, de 40 A", "P1 es la menor capacidad que alcanza el mínimo de 15 A."),
        ("=", "{F} ¿Cuántos pesos de ejemplo cuestan los 20 m del conductor tipo A?", "20*800", "Se multiplican los metros por el costo por metro.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántos pesos de ejemplo más cuestan los 20 m del conductor tipo B que los del tipo A?", "20*1400-20*800", "Se resta el costo de los 20 m de tipo A al de tipo B.", " pesos de ejemplo"),
        ("abc", "{F} Si solo se mira el costo y la capacidad mínima, ¿qué conductor se elegiría en este ejercicio de papel?", "El tipo A, porque cumple y es el más barato", "El tipo C, porque tiene la mayor capacidad", "El tipo B, porque es intermedio", "El tipo A cumple 15 A y es el más económico."),
        ("abc", "{F} Un compañero propone usar P3, de 40 A, para el conductor tipo A de 15 A porque «protege más». ¿Qué respuesta es correcta?", "Es incorrecto: la protección no debe superar la capacidad del conductor que protege, porque no cortaría a tiempo", "Es correcto, porque más capacidad protege mejor", "Es correcto, si el motor es nuevo", "Una protección mayor que el conductor no lo resguarda."),
        ("abc", "{F} Un instalador dice: «uso la tabla de este cuaderno para el tablero real de mi taller». ¿Qué respuesta es correcta?", "Es falso: la tabla es solo de ejemplo y los valores reales los fija el proyecto, el fabricante y la norma vigente", "Es cierto, porque la tabla es oficial", "Es cierto, si el motor coincide", "El cuaderno no sirve para dimensionar instalaciones reales."),
        ("=", "{F} Si el motor fuera de 16 A en vez de 10 A, ¿cuántos A mínimos requeriría el conductor según la regla de ejemplo?", "16*3//2", "Se multiplica la corriente por 3 y se divide por 2.", " A"),
        ("Un motor de ejemplo requiere un mínimo de 20 A y hay conductores de 15 A, 25 A y 40 A. ¿Cuál es el más pequeño que cumple?", "El de 25 A", "El de 15 A no alcanza los 20 A; el de 25 A es el menor que los supera."),
    ],
    ctx=("abc", "Un proveedor de ejemplo ofrece un conductor más barato de menor capacidad que la requerida. ¿Qué propones?", "No elegirlo, porque no cumple el mínimo, y consultar al proyectista por opciones", "Elegirlo porque es más barato", "Elegirlo si es solo por una semana", "Un componente debe cumplir antes de comparar precios."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿cuánto es el mínimo de 8 A por 3 dividido en 2?", "12 A", "Se multiplican 8 y 3 y se divide por 2."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se hace primero al seleccionar de una tabla?", "Filtrar las opciones que cumplen el mínimo", "Después se elige la más económica."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿quién fija los valores reales de una instalación?", "El proyecto, el fabricante y la norma vigente", "El cuaderno solo practica la lectura."),
    ],
    op=("Ficha de ejemplo: un motor ficticio usa 16 A. Regla de ejemplo: capacidad mínima igual a la corriente por 3 y dividida por 2. Conductores de ejemplo: tipo X, 15 A, $700 el metro; tipo Y, 25 A, $1.200 el metro; tipo Z, 40 A, $2.000 el metro. Se necesitan 10 m. Escribe (a) la capacidad mínima, (b) qué tipos cumplen, (c) cuál eliges por costo y cuánto cuestan los 10 m, (d) por qué esta tabla no sirve para una instalación real.",
        "(a) 16 × 3 ÷ 2 = 24 A. (b) Los tipos Y y Z; el X (15 A) no alcanza. (c) El tipo Y; 10 × 1.200 = 12.000 pesos de ejemplo. (d) Porque es una tabla de ejemplo; los valores reales los fija el proyecto, el fabricante y la norma vigente.",
        ["calcula el mínimo", "filtra las opciones", "elige y calcula el costo", "explica el límite del ejercicio"],
        ["hoja con las cuatro respuestas"],
        ["elegir la opción que no cumple", "calcular mal el mínimo", "usar la tabla para una instalación real"],
        "Pregunta: «¿qué opciones alcanzan el mínimo?». Si duda, pídele que marque las que cumplen antes de mirar el costo."),
    reinforce="Inventa una regla y una tabla de tres componentes y elige el más económico que cumple.",
    extend="Explica con un ejemplo por qué una protección mayor que el conductor que protege no cumple su función.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (condición del lugar y grado de protección, de ejemplo). Grado de protección IP: dos cifras. La primera (0 a 6) indica la protección contra sólidos, como polvo; la segunda (0 a 8) indica la protección contra líquidos, como agua. "
     "Lugares de ejemplo: L1, sala seca y limpia; L2, bodega con polvo en el aire; L3, patio con lluvia ocasional y salpicaduras. Tableros de ejemplo: T1, IP20; T2, IP54; T3, IP65. "
     "Regla de ejemplo del taller: para polvo, la primera cifra debe ser 5 o más; para agua con salpicaduras, la segunda cifra debe ser 4 o más. Precio de ejemplo: T1, $60.000; T2, $90.000; T3, $130.000.")
build(
    O3, 4, F,
    use="Aprenderé a leer un grado de protección IP, a relacionar la condición del lugar con el tablero adecuado y a calcular costos de ejemplo.",
    prior=["Sé qué es un tablero eléctrico.", "Sé comparar números.", "Sé sumar y multiplicar enteros."],
    explain=[
        "La condición física del lugar, como el polvo, la humedad, la temperatura o las salpicaduras, determina qué equipo puede instalarse. El grado de protección IP lo expresa con dos cifras: la primera indica la protección contra sólidos, como el polvo, y la segunda contra líquidos, como el agua. A mayor cifra, mayor protección. Un tablero IP20 sirve en un lugar seco y limpio; uno IP65 resiste polvo y chorros de agua.",
        "Elegir un tablero con un IP menor que el que pide el lugar expone a fallas y accidentes; elegir uno con IP muy alto sin necesidad encarece sin beneficio. La regla de ejemplo del taller fija el mínimo de cada cifra. Los valores reales dependen del proyecto, el fabricante y la norma vigente. También se considera la fijación del equipo a una base firme.",
        f"Es un análisis de papel con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("grado de protección IP", "dos cifras que indican la protección contra sólidos y contra líquidos"), ("primera cifra IP", "protección contra sólidos, como el polvo"), ("segunda cifra IP", "protección contra líquidos, como el agua"), ("condición física del lugar", "polvo, humedad, temperatura o salpicaduras del sitio de instalación"), ("fijación", "forma en que un equipo se sujeta a una base firme")],
    worked=[
        ("Leer un IP", "Un equipo de ejemplo es IP43. ¿Qué indican sus cifras?", ["La primera cifra, 4, es la protección contra sólidos.", "La segunda cifra, 3, es la protección contra líquidos."], "Sólidos 4 y líquidos 3"),
        ("Cumplir una regla", "Una regla de ejemplo pide que la segunda cifra sea 5 o más. ¿Cumple un equipo IP64?", ["La segunda cifra es 4.", "4 es menor que 5."], "No cumple"),
    ],
    mistakes=[("Leer las dos cifras IP como un solo número.", "Cada cifra mide una protección distinta.", "Lee la primera para sólidos y la segunda para líquidos."),
              ("Elegir un equipo solo por el precio.", "Un IP insuficiente expone a fallas y accidentes.", "Primero cumple la regla del lugar y luego compara precios.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué indica la primera cifra del grado IP?", "La protección contra sólidos, como el polvo", "La protección contra líquidos", "La potencia del equipo", "La primera cifra se refiere a sólidos."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué indica la segunda cifra del grado IP?", "La protección contra líquidos, como el agua", "La protección contra sólidos", "El voltaje máximo", "La segunda cifra se refiere a líquidos."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es la condición física del lugar?", "El polvo, la humedad, la temperatura o las salpicaduras del sitio", "El precio del tablero", "La potencia del motor", "Describe cómo es el ambiente donde se instala el equipo."),
        ("abc", "{F} ¿Qué tableros cumplen la regla de ejemplo para el lugar L2, con polvo?", "T2 y T3, porque su primera cifra es 5 o más", "Solo T1", "Solo T3", "T2 y T3 tienen primera cifra 5 y 6."),
        ("abc", "{F} ¿Qué tableros cumplen la regla de agua con salpicaduras para el lugar L3, patio con lluvia ocasional y salpicaduras?", "T2 y T3, porque ambos tienen segunda cifra 4 o más", "T1 y T2", "Solo T1", "T2 tiene segunda cifra 4 y T3 tiene 5."),
        ("abc", "{F} ¿Qué tablero sirve en el lugar L1, sala seca y limpia?", "Cualquiera de los tres, y el más económico es T1", "Solo T3", "Ninguno", "El lugar L1 no pide protección especial."),
        ("=", "{F} ¿Cuántos pesos de ejemplo cuestan 4 tableros T2 para una bodega?", "4*90000", "Se multiplican los tableros por el precio.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántos pesos de ejemplo más cuesta T3 que T1?", "130000-60000", "Se resta el precio de T1 al de T3.", " pesos de ejemplo"),
        ("=", "{F} Para el lugar L2 se necesitan 3 tableros y se elige el más económico que cumple. ¿Cuántos pesos de ejemplo cuestan?", "3*90000", "El más económico que cumple para polvo es T2.", " pesos de ejemplo"),
        ("abc", "{F} Un jefe propone T1 para el patio L3 porque es el más barato. ¿Qué respuesta es correcta?", "Es incorrecto: T1 es IP20 y no cumple la regla para salpicaduras", "Es correcto, porque cuesta menos", "Es correcto, si llueve poco", "El IP20 no protege contra el agua."),
        ("abc", "{F} Un compañero dice: «el IP65 es el mejor para todo, usémoslo siempre». ¿Qué observación es correcta?", "Cuesta más y solo conviene cuando el lugar lo exige", "Es lo mejor porque siempre da más seguridad por el mismo precio", "No sirve en ningún lugar", "Un IP muy alto sin necesidad encarece."),
        ("=", "{F} Una planta necesita 2 tableros para L2 y 1 para L3, eligiendo el más económico que cumple en cada caso. ¿Cuántos pesos de ejemplo cuesta el total?", "2*90000+1*90000", "En ambos casos el más económico que cumple es T2.", " pesos de ejemplo"),
        ("Un equipo de ejemplo es IP54 y la regla pide primera cifra 5 o más y segunda 5 o más. ¿Cumple?", "No, porque la segunda cifra es 4", "La primera cifra cumple, pero la segunda es menor que 5."),
    ],
    ctx=("abc", "Un proveedor de ejemplo ofrece un tablero IP20 para una bodega con polvo diciendo que «es igual de bueno». ¿Qué respondes?", "Que el grado IP debe cumplir la condición del lugar y que el IP20 no protege contra el polvo", "Que sí, si es más barato", "Que sí, si lo limpian cada semana", "El IP debe corresponder a la condición física del lugar."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué indica IP65?", "Sólidos 6 y líquidos 5", "La primera cifra es sólidos y la segunda, líquidos."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se mira primero al elegir un tablero?", "La condición del lugar", "El lugar fija la protección mínima."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué sucede con un IP muy alto sin necesidad?", "Encarece sin beneficio", "Conviene lo que el lugar exige."),
    ],
    op=("Ficha de ejemplo: lugares: M1, sala seca y limpia; M2, taller con polvo; M3, exterior con salpicaduras. Tableros: A, IP20, $50.000; B, IP54, $80.000; C, IP66, $120.000. Regla de ejemplo: para polvo, primera cifra 5 o más; para salpicaduras, segunda cifra 4 o más. Escribe (a) qué tablero elegirías para M1, (b) para M2, (c) para M3, (d) el costo total de uno para cada lugar.",
        "(a) A, el más económico. (b) B, porque cumple la primera cifra 5 y es el más económico. (c) B o C: B tiene segunda cifra 4, que cumple; el más económico es B. (d) 50.000 + 80.000 + 80.000 = 210.000 pesos de ejemplo.",
        ["elige para cada lugar", "usa la regla", "calcula el costo total"],
        ["hoja con las cuatro respuestas"],
        ["leer las cifras al revés", "elegir solo por precio", "sumar mal"],
        "Pregunta: «¿qué cifra se mira para el polvo?». Si duda, pídele que relea la regla."),
    reinforce="Inventa tres lugares con su condición y elige un grado IP para cada uno con la regla de ejemplo.",
    extend="Explica con un ejemplo por qué un grado IP alto no es necesario en todos los lugares.",
)

# ============================================================ OAM-03, clase 5
F = ("Ficha 5 (comparación de alternativas, de ejemplo). Se debe elegir un sensor para una cinta. Alternativa S-A: precio $20.000, vida útil de ejemplo 5.000 horas, protección IP54, garantía 6 meses. "
     "Alternativa S-B: precio $30.000, vida útil de ejemplo 10.000 horas, protección IP65, garantía 12 meses. Alternativa S-C: precio $15.000, vida útil de ejemplo 2.000 horas, protección IP20, garantía 3 meses. "
     "El lugar es una bodega con polvo y exige primera cifra IP 5 o más. La cinta funciona 2.000 horas al año. Lista de verificación de calidad de ejemplo: plano vigente revisado; componentes con certificado; rótulos coinciden; registro de pruebas completo; residuos de embalaje gestionados.")
build(
    O3, 5, F,
    use="Aprenderé a comparar alternativas con criterios, a calcular el costo por hora de vida útil y a usar una lista de verificación para revisar la calidad de lo documentado.",
    prior=["Sé qué es un grado IP.", "Sé dividir enteros.", "Sé qué es un registro de pruebas."],
    explain=[
        "Comparar alternativas es contrastar opciones con criterios claros: precio, vida útil, protección IP, garantía. Primero se descartan las que no cumplen una condición obligatoria, como el IP que exige el lugar. Entre las que cumplen, se comparan costos. El costo por hora de vida útil se calcula dividiendo el precio entre las horas de vida útil: indica cuánto cuesta el componente por cada hora que dura.",
        "Verificar la calidad es comprobar que todo lo documentado esté completo y coherente con una lista de verificación: plano vigente revisado, componentes con certificado, rótulos coincidentes, registro de pruebas completo y residuos gestionados. Una lista incompleta no se firma. La decisión la toma la jefatura y se deja por escrito.",
        f"Es un análisis de papel con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("criterio", "característica con que se compara una alternativa"), ("condición obligatoria", "requisito que una alternativa debe cumplir para ser considerada"), ("vida útil", "tiempo durante el cual un componente cumple su función"), ("costo por hora de vida útil", "precio dividido por las horas de vida útil"), ("lista de verificación", "lista de puntos que se comprueban uno a uno"), ("garantía", "plazo en que el proveedor responde por fallas")],
    worked=[
        ("Costo por hora", "Un sensor de ejemplo cuesta $12.000 y dura 3.000 horas. ¿Cuánto cuesta por hora de vida útil?", ["Se divide el precio entre las horas.", "12.000 dividido en 3.000 son 4."], "$4 por hora"),
        ("Descartar", "Un lugar exige primera cifra IP 5 o más. Una alternativa de ejemplo es IP44. ¿Se descarta?", ["La primera cifra es 4.", "4 es menor que 5, así que no cumple."], "Sí, se descarta"),
    ],
    mistakes=[("Elegir la alternativa más barata sin revisar si cumple la condición obligatoria.", "Un componente que no cumple no sirve aunque sea barato.", "Primero descarta las que no cumplen y luego compara costos."),
              ("Firmar la lista de verificación con puntos incompletos.", "La firma indica que todo se verificó.", "Completa cada punto o registra la observación.")],
    T=[
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es una condición obligatoria al comparar alternativas?", "Un requisito que una alternativa debe cumplir para ser considerada", "El criterio que menos importa", "La alternativa más barata", "Si no se cumple, la alternativa se descarta."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿cómo se calcula el costo por hora de vida útil?", "Se divide el precio entre las horas de vida útil", "Se multiplica el precio por las horas de vida útil", "Se suma el precio y las horas de garantía", "Mide cuánto cuesta cada hora de vida del componente."),
        ("abc", "En Mecánica Industrial, mención Mantenimiento: ¿qué es una lista de verificación?", "Una lista de puntos que se comprueban uno a uno", "Un plano de la instalación", "Un contrato de venta", "Se marca cada punto una vez verificado."),
        ("abc", "{F} ¿Qué alternativas cumplen la primera cifra IP 5 o más que exige la bodega?", "S-A y S-B", "Solo S-C", "S-B y S-C", "S-A es IP54 y S-B es IP65; S-C es IP20."),
        ("=", "{F} ¿Cuánto cuesta por hora de vida útil la alternativa S-A?", "20000//5000", "Se divide el precio entre las horas de vida útil.", " pesos de ejemplo por hora"),
        ("=", "{F} Con la diferencia de precio entre S-B y S-A, ¿cuántos pesos de ejemplo más cuesta S-B?", "30000-20000", "Se resta el precio de S-A al de S-B.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántos años completos dura S-A, funcionando 2.000 horas al año?", "5000//2000", "Se divide la vida útil entre las horas por año, en años completos.", " años"),
        ("=", "{F} ¿Cuántos años completos dura S-B, funcionando 2.000 horas al año?", "10000//2000", "Se divide la vida útil entre las horas por año.", " años"),
        ("abc", "{F} Si se comparan los dos sensores que cumplen por costo por hora de vida útil, ¿cuál resulta mejor?", "S-B, con 3 pesos de ejemplo por hora frente a 4 de S-A", "S-A, porque tiene menor precio", "Ambos cuestan lo mismo por hora", "30.000 dividido en 10.000 es 3 y 20.000 dividido en 5.000 es 4."),
        ("abc", "{F} Un jefe dice: «elegimos S-C porque es el más barato». ¿Qué respuesta es correcta?", "Es incorrecto: S-C no cumple la condición obligatoria de IP para la bodega con polvo", "Es correcto, porque es el más barato", "Es correcto, si la garantía es corta", "Una alternativa que no cumple se descarta sin importar el precio."),
        ("abc", "{F} Falta el certificado de uno de los componentes y el registro de pruebas está completo. ¿Qué corresponde con la lista de verificación?", "No firmarla hasta obtener el certificado o registrar la observación", "Firmarla porque el registro está completo", "Borrar el punto del certificado", "La lista no se firma con puntos incompletos."),
        ("=", "{F} La cinta funciona 2.000 horas al año y se instalan 4 sensores S-B. ¿Cuántos pesos de ejemplo cuestan los 4 sensores?", "4*30000", "Se multiplican los sensores por el precio.", " pesos de ejemplo"),
        ("Un sensor de ejemplo cuesta $24.000 y dura 8.000 horas; otro cuesta $18.000 y dura 3.000 horas. ¿Cuál tiene menor costo por hora de vida útil?", "El primero, con 3 pesos por hora frente a 6", "24.000 dividido en 8.000 son 3 y 18.000 dividido en 3.000 son 6."),
    ],
    ctx=("abc", "Un proveedor de ejemplo ofrece un componente muy barato sin certificado. ¿Qué propones?", "No aceptarlo mientras no tenga certificado, porque la lista de verificación lo exige", "Aceptarlo para ahorrar", "Aceptarlo si el proveedor es conocido", "Un componente sin certificado no cumple la verificación."),
    sc=[
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué se hace primero al comparar alternativas?", "Descartar las que no cumplen la condición obligatoria", "Después se comparan los costos de las que cumplen."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué mide el costo por hora de vida útil?", "Cuánto cuesta el componente por cada hora que dura", "Precio dividido en horas de vida útil."),
        ("En Mecánica Industrial, mención Mantenimiento: ¿qué hacer si falta un punto de la lista de verificación?", "No firmarla hasta completarlo", "La firma indica que todo se verificó."),
    ],
    op=("Ficha de ejemplo: dos alternativas de un contactor para un lugar con polvo, que exige primera cifra IP 5 o más. CT-1: $25.000, 5.000 horas, IP54. CT-2: $18.000, 4.000 horas, IP20. Lista de verificación: plano vigente, certificado, rótulo, registro de pruebas. Escribe (a) qué alternativa cumple la condición obligatoria, (b) su costo por hora de vida útil, (c) qué ocurre con la otra, (d) qué haces si falta el certificado.",
        "(a) CT-1, porque su primera cifra es 5. (b) 25.000 ÷ 5.000 = 5 pesos de ejemplo por hora. (c) CT-2 se descarta, aunque sea más barata, porque no cumple el IP. (d) No firmar la lista hasta obtener el certificado o registrar la observación.",
        ["identifica la alternativa que cumple", "calcula el costo por hora", "descarta la otra", "decide con la lista de verificación"],
        ["hoja con las cuatro respuestas"],
        ["elegir por precio", "dividir al revés", "firmar la lista incompleta"],
        "Pregunta: «¿cuál cumple primero la condición del lugar?». Si duda, pídele que relea la regla."),
    reinforce="Inventa tres alternativas con precio y vida útil y calcula el costo por hora de cada una.",
    extend="Explica con un ejemplo por qué una garantía larga no compensa un IP insuficiente.",
)
