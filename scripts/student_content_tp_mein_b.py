"""Mecánica Industrial (tronco) TP 3.º medio: OAE-04 (mantenimiento preventivo de herramientas, solo pautas y registros) y OAE-05 (sujeción, pulido y ajuste: elementos, ajustes y residuos, solo conceptos y cálculo). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_mein_common import AVISO, EMER, build

O4 = "TP-MEIN-3-OAE-04"
O5 = "TP-MEIN-3-OAE-05"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El pañol, o bodega de herramientas, del «Taller Demo» registra 14 herramientas manuales, 6 eléctricas, 4 neumáticas (funcionan con aire comprimido) y 2 hidráulicas (funcionan con un fluido a presión). "
     "Peligros anotados: mango flojo, cable dañado, manguera de aire con fuga, fluido a presión que puede inyectarse bajo la piel y aceite derramado. Ninguna herramienta tiene hoja de vida.")
build(
    O4, 1, F,
    use="Aprenderé qué es el mantenimiento preventivo, qué tipos de herramientas hay en un taller, qué peligros tienen y cómo se rotula una herramienta defectuosa.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé sumar y multiplicar enteros.", "Sé que las herramientas se guardan en un pañol."],
    explain=[
        "El mantenimiento preventivo se hace antes de que ocurra la falla, siguiendo una pauta de mantenimiento: una lista de tareas con su frecuencia, basada en el manual del fabricante. El mantenimiento correctivo, en cambio, se hace después de la falla. Las herramientas pueden ser manuales, eléctricas, neumáticas (con aire comprimido) o hidráulicas (con un fluido a presión), y cada tipo tiene sus peligros. La hoja de vida de una herramienta es el registro de su historial de mantenimiento y de fallas.",
        "Una herramienta defectuosa se rotula como fuera de servicio y se entrega a personal autorizado; no se sigue usando ni se repara de manera improvisada. Los aceites usados y los trapos con aceite son residuos que van a un punto de acopio del taller según la norma vigente, nunca al desagüe ni a la basura común. El pañolero lleva el registro, el mecánico de mantenimiento interviene y el supervisor autoriza.",
        f"Las intervenciones las hace personal autorizado con el manual del fabricante; aquí solo se aprenden los conceptos. {EMER} {AVISO}",
    ],
    vocab=[("mantenimiento preventivo", "el que se hace antes de la falla, según una pauta"), ("mantenimiento correctivo", "el que se hace después de la falla"), ("pauta de mantenimiento", "lista de tareas con su frecuencia, basada en el manual del fabricante"), ("hoja de vida", "registro del historial de mantenimiento y fallas de una herramienta"), ("herramienta neumática", "la que funciona con aire comprimido"), ("herramienta hidráulica", "la que funciona con un fluido a presión"), ("fuera de servicio", "rótulo de una herramienta defectuosa que no debe usarse")],
    worked=[
        ("Preventivo o correctivo", "Una lijadora eléctrica de ejemplo se revisa cada mes, aunque funciona bien. ¿Qué tipo de mantenimiento es?", ["Se revisa antes de que falle.", "Eso es mantenimiento preventivo."], "Preventivo"),
        ("Tipo de herramienta", "Una herramienta de ejemplo funciona con aire que llega por una manguera. ¿Qué tipo es?", ["El aire comprimido mueve la herramienta.", "Se llama neumática."], "Neumática"),
    ],
    mistakes=[("Seguir usando una herramienta con el cable dañado «hasta terminar el trabajo».", "Un cable dañado expone a una descarga eléctrica.", "Rotúlala fuera de servicio y avisa a personal autorizado."),
              ("Botar un trapo con aceite en la basura común.", "Es un residuo que debe ir a un punto de acopio.", "Deposítalo donde indique la norma vigente y el taller.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es el mantenimiento preventivo?", "El que se hace antes de la falla, según una pauta", "El que se hace después de que la herramienta falla", "El que se hace solo cuando el supervisor lo pide", "El preventivo anticipa la falla; el correctivo la repara después."),
        ("abc", "En Mecánica Industrial: ¿qué es una herramienta neumática?", "La que funciona con aire comprimido", "La que funciona con un fluido a presión", "La que funciona con electricidad", "Neumática significa aire comprimido; hidráulica, fluido a presión."),
        ("abc", "En Mecánica Industrial: ¿qué es la hoja de vida de una herramienta?", "El registro de su historial de mantenimiento y fallas", "El manual de uso que entrega el fabricante", "La orden de compra con que se adquirió", "La hoja de vida guarda el historial de la herramienta."),
        ("=", "{F} ¿Cuántas herramientas tiene el pañol en total?", "14+6+4+2", "Se suman las herramientas de los cuatro tipos.", " herramientas"),
        ("abc", "{F} ¿Qué peligro de la lista se asocia a las herramientas hidráulicas?", "El fluido a presión que puede inyectarse bajo la piel", "El cable dañado", "El mango flojo", "Las hidráulicas trabajan con fluido a presión; el cable y el mango son de otras herramientas."),
        ("abc", "{F} Una herramienta eléctrica tiene el cable dañado. ¿Qué corresponde?", "Rotularla fuera de servicio y entregarla a personal autorizado", "Taparlo con cinta y seguir hasta terminar el día", "Guardarla en el pañol sin avisar", "Un cable dañado no se improvisa: se retira de servicio y se informa."),
        ("=", "{F} Cada herramienta eléctrica lleva una inspección visual por semana y un mes de ejemplo tiene 4 semanas. ¿Cuántas inspecciones de herramientas eléctricas se registran en el mes?", "6*4", "Se multiplican las herramientas eléctricas por las semanas del mes.", " inspecciones"),
        ("=", "{F} Cada herramienta neumática requiere 3 revisiones al mes y cada hidráulica requiere 2. ¿Cuántas revisiones suman al mes ambos tipos?", "4*3+2*2", "Se multiplican las herramientas de cada tipo por sus revisiones y se suman.", " revisiones"),
        ("abc", "{F} Como ninguna herramienta tiene historial, ¿qué documento conviene crear primero?", "Una hoja de vida para cada herramienta", "Un plano de despiece de cada herramienta", "Una matriz de peligros de todo el pueblo", "La hoja de vida registra el historial que hoy falta."),
        ("abc", "{F} Un compañero dice: «si la herramienta funciona hoy, no necesita mantenimiento preventivo». ¿Qué respuesta es correcta?", "Es falso: el preventivo se hace antes de la falla justamente para evitarla", "Es cierto, porque el mantenimiento solo se hace al fallar", "Es cierto, si la herramienta es nueva", "El mantenimiento preventivo se planifica aunque la herramienta funcione."),
        ("abc", "En una visita a un taller de ejemplo, un chorro de fluido a presión de una manguera hidráulica alcanza la mano de una persona. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Taparle la herida con un paño y seguir trabajando", "Ayudarla a limpiar el fluido de la mano con tus manos", "Una lesión por fluido a presión es grave aunque se vea pequeña; se pide ayuda de inmediato."),
        ("=", "{F} Se crea una hoja de vida por herramienta y en una jornada de ejemplo se completan 8. ¿Cuántas jornadas se necesitan, contando la última aunque no se llene?", "(26+7)//8", "Se divide el total entre 8 redondeando hacia arriba, sumando 7 antes de dividir.", " jornadas"),
        ("abc", "En Mecánica Industrial: ¿qué se hace con un trapo con aceite usado tras limpiar herramientas?", "Se deposita en el punto de acopio de residuos del taller según la norma vigente", "Se bota en la basura común", "Se deja en el piso para usarlo de nuevo mañana", "Los trapos con aceite son residuos y no van a la basura común."),
    ],
    ctx=("abc", "El supervisor de un taller de ejemplo dice: «no hay tiempo para el mantenimiento preventivo, arreglamos cuando falle». Como estudiante, ¿qué propones?", "Programar la pauta, porque prevenir evita fallas, paradas y accidentes", "Aceptarlo porque el supervisor decide", "Usar las herramientas hasta que se rompan", "El preventivo reduce fallas y riesgos, y se planifica con anticipación."),
    sc=[
        ("En Mecánica Industrial: ¿qué es una herramienta hidráulica?", "La que funciona con un fluido a presión", "Hidráulica significa que usa un fluido a presión."),
        ("En Mecánica Industrial: ¿qué se hace con una herramienta defectuosa?", "Se rotula fuera de servicio y se entrega a personal autorizado", "No se sigue usando ni se repara de forma improvisada."),
        ("En Mecánica Industrial: ¿qué indica una pauta de mantenimiento?", "Las tareas y su frecuencia", "La pauta organiza qué se hace y cada cuánto."),
    ],
    op=("Ficha de ejemplo: el pañol de otro taller tiene 9 herramientas manuales, 3 eléctricas y 2 neumáticas, y ninguna tiene pauta ni hoja de vida. Un peligro anotado es una manguera de aire con fuga. Escribe (a) cuántas herramientas hay en total, (b) qué documento conviene crear para cada una, (c) qué harías con la manguera con fuga y quién interviene, (d) por qué conviene el mantenimiento preventivo.",
        "(a) 9 + 3 + 2 = 14 herramientas. (b) Una hoja de vida y una pauta de mantenimiento basada en el manual del fabricante. (c) Rotular la manguera fuera de servicio y avisar a personal autorizado, que es quien interviene. (d) Porque evita fallas, paradas y accidentes al actuar antes de la falla.",
        ["suma bien las herramientas", "nombra los documentos", "indica rotular y avisar", "explica el sentido de lo preventivo"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal", "proponer reparar la manguera por cuenta propia", "confundir preventivo con correctivo"],
        "Pregunta: «¿esto se hace antes o después de la falla?». Si duda, pídele que relea la definición de mantenimiento preventivo."),
    reinforce="Escribe una diferencia entre mantenimiento preventivo y correctivo con un ejemplo inventado de cada uno.",
    extend="Explica con un ejemplo por qué una herramienta rotulada fuera de servicio no se guarda junto a las demás sin aviso.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (pauta de mantenimiento de ejemplo, inventada, para un taladro eléctrico de mano ficticio; no reemplaza el manual del fabricante). Diaria: inspección visual del cable y la carcasa, y limpieza exterior. "
     "Semanal: revisión del estado del mango y de los accesorios. Mensual: anotar el estado en la hoja de vida. Anual: revisión interna por un servicio técnico autorizado. "
     "Regla: la frecuencia manda; una tarea vencida se informa al supervisor. Un mes de ejemplo tiene 20 días hábiles y 4 semanas.")
build(
    O4, 2, F,
    use="Aprenderé a leer una pauta de mantenimiento, a distinguir qué tareas puede hacer cada rol y a contar cuántas tareas generan las frecuencias.",
    prior=["Sé qué es el mantenimiento preventivo.", "Sé qué es una hoja de vida.", "Sé multiplicar enteros."],
    explain=[
        "Una pauta de mantenimiento lista tareas con su frecuencia: diaria, semanal, mensual o anual. El manual del fabricante manda sobre cualquier costumbre del taller. Hay tareas de inspección, como mirar el cable o el mango, que realiza el usuario capacitado, y tareas de intervención interna, que realiza personal autorizado o un servicio técnico del fabricante. Una tarea vencida es la que se pasó de su fecha sin hacerse.",
        "La orden de trabajo pide y registra una tarea de mantenimiento, con su fecha y quien la hizo. El planificador programa las órdenes, el mecánico de mantenimiento las ejecuta, el supervisor las revisa y el pañolero mantiene el registro de las herramientas. Si una pauta no existe o es dudosa, se consulta el manual del fabricante.",
        f"No se interviene ninguna herramienta con este cuaderno. {EMER} {AVISO}",
    ],
    vocab=[("frecuencia", "cada cuánto tiempo se repite una tarea"), ("inspección visual", "revisión mirando el estado, sin desarmar nada"), ("intervención interna", "tarea que abre o toca el interior de la herramienta"), ("tarea vencida", "la que se pasó de su fecha sin hacerse"), ("orden de trabajo", "documento que pide y registra una tarea de mantenimiento"), ("planificador", "quien programa las tareas de mantenimiento")],
    worked=[
        ("Contar tareas", "Una tarea de ejemplo se hace cada 5 días hábiles y se revisan 15 días hábiles. ¿Cuántas veces se hace?", ["15 dividido en 5 es 3.", "Se hace 3 veces."], "3 veces"),
        ("Quién interviene", "Una pauta de ejemplo dice «revisar el interior del motor». ¿Quién la hace?", ["Es una intervención interna.", "La hace personal autorizado o un servicio técnico."], "Personal autorizado o servicio técnico"),
    ],
    mistakes=[("Hacer una intervención interna porque «es fácil».", "Las intervenciones internas las hace personal autorizado con el manual del fabricante.", "Registra la necesidad y pide la orden de trabajo."),
              ("Cambiar la frecuencia de una tarea porque «ya la hicimos hace poco».", "La frecuencia de la pauta manda.", "Cumple la pauta o pide al planificador que la revise.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es una orden de trabajo de mantenimiento?", "El documento que pide y registra una tarea de mantenimiento", "El plano de una pieza de la herramienta", "El certificado de calibración de un instrumento", "La orden de trabajo pide y deja registro de la tarea."),
        ("abc", "En Mecánica Industrial: ¿qué es una intervención interna?", "Una tarea que abre o toca el interior de la herramienta", "Una revisión visual de la carcasa", "Una limpieza exterior", "Interna significa que toca el interior y por eso la hace personal autorizado."),
        ("abc", "En Mecánica Industrial: ¿quién programa las tareas de mantenimiento?", "El planificador", "El pañolero", "El proveedor de las herramientas", "El planificador organiza las tareas; el pañolero lleva el registro."),
        ("abc", "{F} ¿Qué tarea de la pauta es de frecuencia semanal?", "La revisión del estado del mango y de los accesorios", "La inspección visual del cable", "La revisión interna por un servicio técnico", "El mango y los accesorios se revisan una vez por semana; el cable, todos los días."),
        ("abc", "{F} ¿Qué tarea de la pauta es una intervención interna?", "La revisión interna anual por un servicio técnico autorizado", "La inspección visual diaria", "Anotar el estado en la hoja de vida", "Solo la revisión interna abre la herramienta."),
        ("abc", "{F} Según la pauta, ¿qué se hace con una tarea vencida?", "Se informa al supervisor", "Se omite hasta la próxima vez", "Se anota como hecha para cumplir", "La regla de la ficha dice que se informa al supervisor."),
        ("=", "{F} ¿Cuántas inspecciones visuales diarias del cable se registran en un mes de ejemplo?", "20*1", "Hay una inspección por cada día hábil.", " inspecciones"),
        ("=", "{F} Un taller tiene 5 taladros iguales. ¿Cuántas revisiones semanales del mango se registran en un mes de ejemplo en todos los taladros?", "5*4", "Se multiplican los taladros por las semanas del mes.", " revisiones"),
        ("=", "{F} Con 5 taladros iguales, ¿cuántas tareas diarias, semanales y mensuales suman en un mes de ejemplo, contando una diaria por día, una semanal por semana y una mensual por mes?", "5*(20+4+1)", "Se suman las tareas de un taladro y se multiplican por los taladros.", " tareas"),
        ("abc", "{F} Un compañero propone omitir la inspección diaria del cable porque el taladro es nuevo. ¿Qué respuesta es correcta?", "No corresponde: la pauta exige la inspección diaria aunque la herramienta sea nueva", "Corresponde, porque las herramientas nuevas no fallan", "Corresponde, si se anota que se hizo", "La pauta manda y no depende de la antigüedad."),
        ("abc", "{F} Un mecánico del taller propone abrir el taladro «solo para mirar» sin orden de trabajo. ¿Qué respuesta es correcta?", "No corresponde: la intervención interna requiere orden de trabajo y personal o servicio autorizado", "Corresponde, porque mirar no hace daño", "Corresponde, si lo hace de noche", "Abrir una herramienta es una intervención interna que exige autorización."),
        ("=", "{F} El servicio técnico cobra $12.000 de ejemplo por cada revisión anual y se revisan 5 taladros. ¿Cuánto suma el costo anual de esas revisiones?", "12000*5", "Se multiplica el costo de una revisión por el número de taladros.", " pesos de ejemplo"),
        ("En un taller de ejemplo, una herramienta se revisa cada 10 días hábiles. ¿Cuántas revisiones corresponden en 60 días hábiles?", "6 revisiones", "Se divide los 60 días hábiles entre la frecuencia de 10."),
    ],
    ctx=("abc", "En un taller de ejemplo, una persona dice: «yo mismo cambio las piezas internas, no hace falta la orden». Como estudiante, ¿qué propones?", "Pedir una orden de trabajo y que la intervención interna la haga personal autorizado", "Dejar que lo haga porque tiene experiencia", "Cambiar la pauta para que lo permita", "Las intervenciones internas requieren orden y autorización."),
    sc=[
        ("En Mecánica Industrial: ¿qué manda sobre la costumbre del taller?", "El manual del fabricante y la pauta", "La pauta se basa en el manual del fabricante."),
        ("En Mecánica Industrial: ¿qué es una inspección visual?", "Una revisión mirando el estado, sin desarmar", "Se mira, no se abre ni se desarma."),
        ("En Mecánica Industrial: ¿qué es una tarea vencida?", "La que se pasó de su fecha sin hacerse", "La vencida debe informarse al supervisor."),
    ],
    op=("Ficha de ejemplo: la pauta de una lijadora ficticia dice: diaria, inspección visual del cable (1 vez por día hábil); semanal, revisión del mango (1 vez por semana); mensual, anotar el estado en la hoja de vida (1 vez); anual, revisión interna por un servicio técnico. Un mes de ejemplo tiene 20 días hábiles y 4 semanas. Escribe (a) cuántas tareas de un mes genera la lijadora, (b) cuáles tareas puede hacer el usuario capacitado, (c) cuál exige personal autorizado, (d) qué haces si encuentras la tarea mensual vencida.",
        "(a) 20 + 4 + 1 = 25 tareas. (b) La inspección visual del cable, la revisión del mango y anotar en la hoja de vida. (c) La revisión interna anual. (d) Informar al supervisor, porque una tarea vencida se informa.",
        ["calcula las tareas del mes", "separa tareas de usuario y de personal autorizado", "indica qué hacer con una tarea vencida"],
        ["hoja con las cuatro respuestas"],
        ["olvidar alguna frecuencia", "asignar la revisión interna al usuario", "omitir informar al supervisor"],
        "Pregunta: «¿esta tarea abre la herramienta?». Si duda, pídele que relea la definición de intervención interna."),
    reinforce="Inventa una pauta con una tarea diaria, una semanal y una mensual, y cuenta cuántas tareas genera en un mes de 20 días hábiles y 4 semanas.",
    extend="Explica con un ejemplo por qué el pañolero y el mecánico de mantenimiento no cumplen la misma función.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (hoja de vida de ejemplo, inventada, de la herramienta H-07). Pauta: inspección visual cada 30 días. Registro: día 1, inspección sin observaciones; día 31, inspección sin observaciones; día 55, un operario anota «cable con un corte superficial», sin acción; "
     "día 61, inspección sin observaciones; día 70, la herramienta falla por un cable cortado y queda fuera de servicio; día 100, hoy. Costos de ejemplo: la reparación correctiva cuesta $18.000; la inspección preventiva cuesta $2.000.")
build(
    O4, 3, F,
    use="Aprenderé a leer una hoja de vida, a detectar tareas atrasadas, observaciones sin acción y las causas de una falla en un caso escrito.",
    prior=["Sé qué es una pauta de mantenimiento.", "Sé restar números enteros.", "Sé qué es una hoja de vida."],
    explain=[
        "Una hoja de vida es útil cuando se lee con la pauta al lado. Se calcula el atraso de una tarea restando a la fecha de hoy el día de la última ejecución y comparándolo con la frecuencia. Una observación es una nota sobre una anomalía; si queda sin acción, el problema sigue y puede terminar en falla. La causa inmediata de una falla es lo que la produce directamente, como un cable cortado; la causa de fondo es lo que permitió que ocurriera, como una observación que nadie atendió.",
        "El análisis de una falla no busca culpables sino causas, para evitar que se repita. Se registra qué ocurrió, qué se hizo y cuánto costó. Comparar el costo del mantenimiento preventivo con el correctivo ayuda a decidir si la pauta se justifica.",
        f"El análisis es de papel; no se interviene ninguna herramienta. {EMER} {AVISO}",
    ],
    vocab=[("atraso", "días transcurridos desde la última ejecución menos la frecuencia"), ("observación", "nota sobre una anomalía detectada"), ("causa inmediata", "lo que produce directamente la falla"), ("causa de fondo", "lo que permitió que la falla ocurriera"), ("acción correctiva", "medida para reparar o evitar que se repita el problema")],
    worked=[
        ("Calcular el atraso", "Una tarea de ejemplo tiene frecuencia de 20 días y se hizo por última vez el día 10. Hoy es el día 45. ¿Cuántos días de atraso tiene?", ["Pasaron 45 menos 10, es decir 35 días.", "35 menos 20 son 15 días de atraso."], "15 días"),
        ("Causa de fondo", "En un taller de ejemplo se rompe un mango flojo que se había anotado hace dos semanas sin acción. ¿Cuál es la causa de fondo?", ["La causa inmediata es el mango flojo que se rompe.", "La causa de fondo es la observación sin acción."], "La observación sin acción"),
    ],
    mistakes=[("Anotar una observación y dejarla sin acción.", "El problema sigue y puede producir una falla.", "Toda observación debe generar una acción o una consulta al supervisor."),
              ("Buscar a quién culpar en vez de las causas.", "Culpar no evita que se repita la falla.", "Describe causa inmediata y causa de fondo, y propone acciones.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es una causa inmediata de una falla?", "Lo que produce directamente la falla", "Lo que permitió que la falla ocurriera", "Lo que se hizo después para repararla", "La causa inmediata actúa directamente; la de fondo explica por qué pudo ocurrir."),
        ("abc", "En Mecánica Industrial: ¿qué es una acción correctiva?", "Una medida para reparar o evitar que se repita el problema", "Una nota que describe la anomalía", "La frecuencia de una tarea de la pauta", "La acción correctiva actúa sobre el problema; la nota es solo una observación."),
        ("abc", "En Mecánica Industrial: ¿qué es una observación en una hoja de vida?", "Una nota sobre una anomalía detectada", "La reparación de la anomalía", "El costo de la reparación", "La observación avisa de la anomalía y debe generar una acción."),
        ("=", "{F} ¿Cuántos días pasaron entre la última inspección sin observaciones y la falla de la herramienta?", "70-61", "Se resta el día de la inspección al día de la falla.", " días"),
        ("abc", "{F} ¿Cuál fue la causa inmediata de la falla de la herramienta H-07?", "El cable cortado", "La observación sin acción del día 55", "La inspección del día 61", "El corte del cable produjo directamente la falla."),
        ("abc", "{F} ¿Cuál fue la causa de fondo?", "La observación del día 55 que quedó sin acción", "El cable que se cortó", "La pauta de 30 días", "La observación se anotó pero nadie actuó, y eso permitió la falla."),
        ("=", "{F} Hoy es el día 100 y la herramienta H-07 sigue fuera de servicio. ¿Cuántos días lleva fuera de servicio?", "100-70", "Se resta el día de la falla al día de hoy.", " días"),
        ("=", "{F} ¿Cuántos pesos más cuesta la reparación correctiva que una inspección preventiva?", "18000-2000", "Se resta el costo de la inspección al de la reparación.", " pesos de ejemplo"),
        ("=", "{F} Con el costo de una reparación correctiva se podrían pagar varias inspecciones preventivas. ¿Cuántas inspecciones de $2.000 caben en $18.000?", "18000//2000", "Se divide el costo correctivo entre el de una inspección.", " inspecciones"),
        ("abc", "{F} Un jefe dice: «el día 55 solo era un corte superficial, no era necesario actuar». ¿Qué respuesta es correcta?", "Es dudoso: una observación debe generar una acción o una consulta, porque un corte superficial puede empeorar", "Es correcto, porque lo superficial nunca causa fallas", "Es correcto, si la herramienta funcionaba", "Una anomalía sin acción puede terminar en falla, como ocurrió."),
        ("abc", "{F} Se propone sancionar a la persona que usó la herramienta el día 70. ¿Qué respuesta es más adecuada?", "Analizar las causas y mejorar el sistema, porque la observación del día 55 no se atendió", "Sancionarla, porque la herramienta falló en sus manos", "No hacer nada, porque las fallas son inevitables", "El análisis busca causas para evitar que se repita, no culpables."),
        ("=", "{F} Si cada día fuera de servicio la herramienta deja sin trabajar a una persona con un costo de ejemplo de $5.000 por día, ¿cuánto cuesta la parada de los 30 días que lleva fuera de servicio?", "5000*30", "Se multiplica el costo por día por los días de parada.", " pesos de ejemplo"),
        ("abc", "En una visita a un taller de ejemplo, una persona recibe una descarga eléctrica de una herramienta con el cable dañado. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Tomar a la persona del brazo para separarla", "Desenchufar la herramienta con las manos mojadas", "Intervenir sin formación puede causar otro accidente eléctrico."),
    ],
    ctx=("abc", "Un compañero de ejemplo dice: «la herramienta ya falló, para qué analizar». ¿Qué respondes?", "Que se analizan las causas para evitar que la falla se repita en otras herramientas", "Que tiene razón, porque ya no hay remedio", "Que se debe buscar a quien la usó para sancionarlo", "El análisis de causas evita fallas futuras."),
    sc=[
        ("En Mecánica Industrial: ¿qué se calcula para saber si una tarea está atrasada?", "Los días desde la última ejecución menos la frecuencia", "El atraso compara el tiempo transcurrido con la frecuencia."),
        ("En Mecánica Industrial: ¿qué debe generar una observación en la hoja de vida?", "Una acción o una consulta al supervisor", "Una observación sin acción puede terminar en falla."),
        ("En Mecánica Industrial: ¿cuál es el objetivo de analizar una falla?", "Encontrar causas para evitar que se repita", "El análisis busca causas, no culpables."),
    ],
    op=("Ficha de ejemplo: hoja de vida de la herramienta H-12. Pauta: inspección cada 20 días. Día 1 inspección sin observaciones; día 21 inspección con la nota «mango flojo» sin acción; día 41 no se hizo la inspección; día 50 el mango se rompe y una persona sufre un golpe leve. Hoy es el día 70. Escribe (a) la causa inmediata, (b) una causa de fondo, (c) cuántos días de atraso tiene la inspección desde el día 21, (d) una acción correctiva.",
        "(a) El mango roto. (b) La observación del día 21 sin acción y la inspección del día 41 que no se hizo. (c) Desde el día 21 hasta el 70 pasaron 49 días; 49 − 20 = 29 días de atraso. (d) Programar la inspección, atender toda observación con una acción y rotular fuera de servicio las herramientas con anomalías.",
        ["distingue causa inmediata y de fondo", "calcula el atraso", "propone una acción correctiva"],
        ["hoja con las cuatro respuestas"],
        ["confundir causa inmediata con causa de fondo", "calcular mal el atraso", "buscar culpables"],
        "Pregunta: «¿qué permitió que el mango se rompiera?». Si responde el mango, pídele que relea la causa de fondo."),
    reinforce="Escribe una falla inventada con su causa inmediata y su causa de fondo.",
    extend="Explica con un ejemplo por qué comparar el costo preventivo con el correctivo ayuda a decidir una pauta.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (indicadores de mantenimiento de ejemplo, inventados). Trimestre de ejemplo de 60 días hábiles para el parque de herramientas del «Taller Demo». Tareas preventivas programadas: 150. Tareas preventivas realizadas: 135. "
     "Fallas correctivas del trimestre: 9, con un costo de ejemplo de $20.000 cada una. Costo de ejemplo de cada tarea preventiva: $1.500. Horas de ejemplo disponibles de las herramientas en el trimestre: 4.800; horas detenidas por falla: 480.")
build(
    O4, 4, F,
    use="Aprenderé a calcular el cumplimiento de la pauta, la disponibilidad y el costo preventivo y correctivo con datos de ejemplo, y a sacar una conclusión.",
    prior=["Sé multiplicar, dividir y restar enteros.", "Sé qué es un porcentaje de números redondos.", "Sé qué es el mantenimiento preventivo y el correctivo."],
    explain=[
        "El cumplimiento de la pauta compara las tareas realizadas con las programadas: se calcula multiplicando las realizadas por 100 y dividiendo por las programadas, y se expresa en porcentaje. La disponibilidad compara las horas en que las herramientas estuvieron listas para usarse con las horas totales: las horas disponibles menos las detenidas, multiplicadas por 100 y divididas por las horas totales.",
        "El costo preventivo es la suma del costo de todas las tareas preventivas realizadas; el costo correctivo es la suma de las fallas por su costo. Si el cumplimiento sube, se espera que bajen las fallas y el costo correctivo. Un indicador sin interpretación no sirve: se compara con una meta y se propone una acción.",
        f"Todos los números son de ejemplo y el cálculo es solo en papel. {EMER} {AVISO}",
    ],
    vocab=[("cumplimiento de la pauta", "porcentaje de tareas preventivas realizadas sobre las programadas"), ("disponibilidad", "porcentaje de horas en que las herramientas están listas para usarse"), ("costo preventivo", "suma del costo de las tareas preventivas realizadas"), ("costo correctivo", "suma del costo de las fallas reparadas"), ("meta", "valor que se quiere alcanzar en un indicador")],
    worked=[
        ("Calcular el cumplimiento", "En un mes de ejemplo se programan 40 tareas y se realizan 30. ¿Qué porcentaje de cumplimiento hay?", ["Se multiplican las realizadas por 100: 3.000.", "3.000 dividido en 40 son 75."], "75 %"),
        ("Costo correctivo", "En un periodo de ejemplo hay 4 fallas y cada una cuesta $25.000. ¿Cuánto suma el costo correctivo?", ["Se multiplica el costo de una falla por el número de fallas.", "4 por 25.000 son 100.000."], "$100.000"),
    ],
    mistakes=[("Calcular el cumplimiento dividiendo las programadas por las realizadas.", "Se invierte la relación y el porcentaje queda mal.", "Divide siempre lo realizado entre lo programado."),
              ("Calcular un indicador y no sacar conclusión.", "Un número sin comparación con una meta no orienta ninguna acción.", "Compara con la meta y propone qué hacer.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿cómo se calcula el cumplimiento de la pauta?", "Tareas realizadas por 100 dividido por las programadas", "Tareas programadas por 100 dividido por las realizadas", "Horas detenidas dividido por horas totales", "Se mide lo realizado respecto de lo programado."),
        ("abc", "En Mecánica Industrial: ¿qué mide la disponibilidad de las herramientas?", "El porcentaje de horas en que están listas para usarse", "El número de fallas del trimestre", "El costo de las tareas preventivas", "La disponibilidad compara horas disponibles con horas totales."),
        ("abc", "En Mecánica Industrial: ¿qué es una meta de un indicador?", "El valor que se quiere alcanzar", "El resultado de la última medición", "El costo de una reparación", "La meta es el objetivo con que se compara el resultado."),
        ("=", "{F} ¿Qué porcentaje de cumplimiento de la pauta tuvo el trimestre?", "135*100//150", "Se multiplican las realizadas por 100 y se dividen por las programadas.", " %"),
        ("=", "{F} ¿Cuántas tareas preventivas quedaron sin realizar?", "150-135", "Se resta lo realizado a lo programado.", " tareas"),
        ("=", "{F} ¿Cuántos pesos de ejemplo suma el costo correctivo del trimestre?", "9*20000", "Se multiplica el costo de una falla por el número de fallas.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántos pesos de ejemplo suma el costo preventivo, con las tareas realizadas?", "135*1500", "Se multiplica el costo de una tarea por las tareas realizadas.", " pesos de ejemplo"),
        ("=", "{F} ¿Qué porcentaje de disponibilidad tuvieron las herramientas?", "(4800-480)*100//4800", "Se resta las horas detenidas, se multiplica por 100 y se divide por las horas totales.", " %"),
        ("abc", "{F} Si la meta de cumplimiento es 95 %, ¿qué conclusión corresponde?", "No se cumple la meta: el cumplimiento fue 90 %", "Se cumple la meta, porque 90 es un número alto", "Se supera la meta, porque hubo más tareas realizadas que fallas", "El resultado de 90 % es menor que la meta."),
        ("abc", "{F} Un jefe dice: «gastamos $202.500 en preventivo y $180.000 en correctivo, así que el preventivo no sirve». ¿Qué observación es correcta?", "Falta comparar con lo que habrían costado más fallas y paradas si no hubiera preventivo", "Tiene razón, porque el preventivo costó más", "Tiene razón, porque el correctivo siempre es más barato", "La comparación debe considerar las fallas y paradas evitadas."),
        ("abc", "{F} ¿Qué acción conviene proponer ante el cumplimiento bajo la meta?", "Revisar por qué quedaron tareas sin hacer y reprogramarlas", "Borrar las tareas pendientes de la pauta", "Anotar que se hicieron todas", "La causa del incumplimiento se corrige, no se oculta."),
        ("=", "{F} Si el trimestre siguiente se realizan las 15 tareas pendientes más las 150 nuevas programadas, ¿cuántas tareas preventivas hay en total?", "15+150", "Se suman las pendientes y las nuevas programadas.", " tareas"),
        ("Un taller de ejemplo tiene 200 horas totales y 20 detenidas en un mes, y otro tiene 400 horas totales y 60 detenidas. ¿Cuál tiene mayor disponibilidad?", "El primero, con 90 % frente a 85 %", "El primero tiene 180 por 100 dividido en 200, es decir 90 %; el segundo, 340 por 100 dividido en 400, es decir 85 %."),
    ],
    ctx=("abc", "En una reunión de ejemplo, el supervisor muestra un cumplimiento de 70 % y dice que «está bien». ¿Qué le propones?", "Compararlo con la meta y revisar qué tareas quedaron pendientes", "Aceptar el número sin comparar", "Eliminar las tareas pendientes de la pauta", "Un indicador se interpreta con una meta y una acción."),
    sc=[
        ("En Mecánica Industrial: ¿qué porcentaje es 30 tareas hechas de 40 programadas?", "75 %", "Treinta por cien dividido en cuarenta es setenta y cinco."),
        ("En Mecánica Industrial: ¿qué suma el costo correctivo?", "El costo de todas las fallas reparadas", "Se suma cada falla por su costo."),
        ("En Mecánica Industrial: ¿qué hay que hacer después de calcular un indicador?", "Compararlo con una meta y proponer una acción", "Un indicador sin interpretación no orienta decisiones."),
    ],
    op=("Ficha de ejemplo: un mes de ejemplo de otro taller tiene 80 tareas preventivas programadas y 60 realizadas, con costo de $1.000 cada una; hubo 3 fallas correctivas de $15.000 cada una. Meta de cumplimiento: 90 %. Escribe (a) el cumplimiento, (b) el costo preventivo y el correctivo, (c) si cumple la meta, (d) una acción.",
        "(a) 60 × 100 ÷ 80 = 75 %. (b) Preventivo: 60 × 1.000 = 60.000; correctivo: 3 × 15.000 = 45.000 pesos de ejemplo. (c) No cumple la meta de 90 %. (d) Reprogramar las 20 tareas pendientes y revisar por qué no se hicieron.",
        ["calcula el cumplimiento", "calcula ambos costos", "compara con la meta", "propone una acción"],
        ["hoja con los cálculos y la conclusión"],
        ["invertir la relación del cumplimiento", "mezclar el costo preventivo y el correctivo", "no concluir"],
        "Pregunta: «¿lo realizado va arriba o abajo en la división?». Si duda, pídele que relea la definición de cumplimiento."),
    reinforce="Inventa tareas programadas y realizadas y calcula el cumplimiento con números que den un entero.",
    extend="Explica con un ejemplo por qué un cumplimiento más alto debería disminuir el costo correctivo.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Taller Demo» arma y ajusta conjuntos con uniones apernadas y termina superficies con abrasivos. Peligros anotados: proyección de partículas, ruido, polvo metálico, vibración de las herramientas, "
     "herramienta que se suelta o se rompe, atrapamiento por ropa suelta o pelo largo y aceite derramado. Residuos del área: limaduras y polvo metálico, discos abrasivos gastados, trapos con aceite y aceite usado. Personas en el turno: 10.")
build(
    O5, 1, F,
    use="Aprenderé qué son la sujeción, el pulido y el ajuste, qué peligros tienen estos trabajos y qué residuos generan.",
    prior=["Sé qué es un peligro y un control.", "Sé la jerarquía de controles.", "Sé que algunos residuos tienen un punto de acopio."],
    explain=[
        "La sujeción es unir o fijar piezas con elementos de fijación, como pernos, tuercas, tornillos y arandelas, o mantener una pieza firme mientras se trabaja en ella. El pulido es mejorar el acabado de una superficie retirando material con abrasivos, es decir, materiales duros que desgastan. El ajuste es lograr que dos piezas encajen con el juego o el apriete que pide el plano. Se hacen con herramientas manuales o eléctricas.",
        "Los peligros más comunes son la proyección de partículas, el ruido, el polvo, la vibración, la herramienta que se suelta, el atrapamiento por ropa suelta o pelo largo y los derrames. Se controlan con resguardos instalados de fábrica que no se retiran, con orden y limpieza, con capacitación y, al final, con EPP: protección para ojos, oídos, vías respiratorias y manos, y ropa ajustada.",
        f"Los residuos se separan y van al punto de acopio según la norma vigente; no se vierten al desagüe. Estas tareas las hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("sujeción", "unir o fijar piezas, o mantener una pieza firme mientras se trabaja"), ("elemento de fijación", "perno, tuerca, tornillo o arandela que une piezas"), ("pulido", "mejorar el acabado de una superficie retirando material con abrasivos"), ("abrasivo", "material duro que desgasta una superficie"), ("ajuste", "encaje entre dos piezas con un juego o apriete determinado"), ("resguardo", "barrera física instalada de fábrica que impide el contacto con una parte peligrosa")],
    worked=[
        ("Elegir el control", "Una herramienta de ejemplo trae de fábrica una cubierta sobre el disco giratorio. ¿Qué tipo de control es y qué no debe hacerse con ella?", ["La cubierta es una barrera física, un control de ingeniería.", "No se retira ni se modifica."], "Control de ingeniería; no se retira"),
        ("Segregar residuos", "Un taller de ejemplo genera limaduras metálicas y un trapo con aceite. ¿Van en el mismo recipiente?", ["Son residuos de naturaleza distinta.", "Se separan en puntos de acopio distintos."], "No, se separan"),
    ],
    mistakes=[("Retirar la cubierta de una herramienta porque estorba.", "El resguardo impide el contacto con la parte peligrosa.", "No se retira; si estorba, se consulta a la jefatura."),
              ("Usar ropa suelta o pelo largo suelto cerca de piezas giratorias.", "Pueden quedar atrapados.", "Mantén la ropa ajustada y el pelo recogido, según la norma del taller.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es un abrasivo?", "Un material duro que desgasta una superficie", "Un aceite que lubrica una superficie", "Un perno que une dos superficies", "El abrasivo desgasta; el aceite lubrica y el perno une."),
        ("abc", "En Mecánica Industrial: ¿qué es el ajuste entre dos piezas?", "El encaje con el juego o apriete que pide el plano", "La pintura que se les aplica", "El número de piezas que se arman", "El ajuste describe cómo encajan dos piezas."),
        ("abc", "En Mecánica Industrial: ¿qué es la sujeción?", "Unir o fijar piezas, o mantener una pieza firme mientras se trabaja", "Cortar una pieza en dos partes", "Pintar una pieza ya terminada", "La sujeción incluye fijar y mantener firme una pieza."),
        ("abc", "{F} ¿Qué peligro de la lista se previene mejor con ropa ajustada y pelo recogido?", "El atrapamiento", "El ruido", "El polvo metálico", "La ropa suelta y el pelo largo pueden quedar atrapados."),
        ("abc", "{F} ¿Cuál de estos residuos requiere un punto de acopio distinto del de las limaduras metálicas?", "Los trapos con aceite", "El polvo metálico", "Las limaduras", "El aceite exige un manejo propio; las limaduras y el polvo son residuos metálicos."),
        ("abc", "{F} Una cubierta instalada de fábrica sobre un disco giratorio es un control:", "De ingeniería", "Administrativo", "De EPP", "La cubierta es una barrera física."),
        ("=", "{F} Cada persona del turno recibe 2 pares de tapones para los oídos al mes. ¿Cuántos pares se necesitan al mes?", "10*2", "Se multiplican las personas por los pares que recibe cada una.", " pares"),
        ("=", "{F} Cada persona usa 3 discos abrasivos por semana y el taller trabaja 4 semanas. ¿Cuántos discos gastados se generan en el mes?", "10*3*4", "Se multiplican personas, discos y semanas.", " discos"),
        ("abc", "{F} La matriz dice «ruido». ¿Cuál de estas medidas es un control administrativo?", "Rotar al personal para limitar el tiempo de exposición", "Instalar una cabina que encierre la máquina", "Usar protectores auditivos", "Rotar es una regla de organización; la cabina es de ingeniería y los protectores son EPP."),
        ("abc", "{F} Un compañero dice: «retiro el resguardo del disco solo hoy, para llegar mejor a la pieza». ¿Qué respuesta es correcta?", "No corresponde: el resguardo no se retira, y si estorba se consulta a la jefatura", "Corresponde, si trabaja con cuidado", "Corresponde, si usa guantes", "Retirar un resguardo expone al contacto con la parte giratoria."),
        ("abc", "En una visita a un taller de ejemplo, un disco se rompe y una persona recibe un golpe con fragmentos. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Recoger los fragmentos con las manos", "Pedirle a la persona que siga trabajando", "Los fragmentos pueden causar otro daño; se llama a quienes pueden actuar."),
        ("=", "El taller de ejemplo genera 12 kg de limaduras a la semana y 3 kg de trapos con aceite a la semana. ¿Cuántos kg de residuos suma en 4 semanas?", "(12+3)*4", "Se suman los residuos de una semana y se multiplican por las semanas.", " kg"),
        ("abc", "En Mecánica Industrial: ¿qué se hace con el aceite usado de un taller?", "Se almacena en un recipiente rotulado hasta su retiro según la norma vigente", "Se vierte al desagüe del taller", "Se mezcla con las limaduras", "El aceite usado es un residuo que no se vierte al desagüe."),
    ],
    ctx=("abc", "Un familiar de ejemplo te pide «lija esto con la herramienta eléctrica del garaje, es rápido». ¿Qué respondes?", "Que no, porque usar herramientas eléctricas exige instructor autorizado y protección, y que consultarás a un adulto responsable", "Que sí, si usas gafas", "Que sí, mientras no haya nadie cerca", "Este cuaderno no habilita para operar herramientas eléctricas."),
    sc=[
        ("En Mecánica Industrial: ¿qué es un elemento de fijación?", "Un perno, tuerca, tornillo o arandela que une piezas", "Estos elementos fijan unas piezas con otras."),
        ("En Mecánica Industrial: ¿qué hacer con los trapos con aceite?", "Llevarlos al punto de acopio según la norma", "No se botan a la basura común."),
        ("En Mecánica Industrial: ¿qué es el pulido?", "Mejorar el acabado de una superficie con abrasivos", "El pulido retira material para mejorar la superficie."),
    ],
    op=("Ficha de ejemplo: en un área de un taller trabajan 6 personas con herramientas eléctricas y abrasivos. Peligros anotados: proyección de partículas, polvo metálico y ruido. Residuos: polvo metálico, discos gastados y trapos con aceite. Escribe (a) un control de ingeniería para el ruido, (b) un control administrativo, (c) el EPP que se suma, (d) cómo se manejan los residuos. No describas cómo se usa la herramienta.",
        "(a) Una cabina o barrera que reduzca el ruido. (b) Rotar al personal para limitar la exposición y señalizar la zona. (c) Protección auditiva, ocular y respiratoria, como última barrera. (d) Se separan en recipientes rotulados y se llevan al punto de acopio según la norma vigente, sin verter al desagüe.",
        ["propone un control de ingeniería", "propone un control administrativo", "nombra el EPP", "describe el manejo de residuos"],
        ["hoja con las cuatro respuestas"],
        ["proponer solo EPP", "mezclar los residuos", "describir cómo se usa la herramienta"],
        "Pregunta: «¿qué medida reduce el ruido sin depender de una persona?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe tres peligros de pulir una pieza y un control para cada uno.",
    extend="Explica con un ejemplo por qué un resguardo no se retira aunque estorbe.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (lista de materiales y tabla de ejemplo, inventadas). Designación de rosca: «M10 × 40» significa rosca métrica de 10 mm de diámetro y 40 mm de largo. Unión de ejemplo: 4 pernos M10 × 40, 4 tuercas M10 y 8 arandelas M10. "
     "Tabla de par de apriete DE EJEMPLO (no sirve para trabajar): M8, 15 unidades de ejemplo; M10, 30 unidades de ejemplo; M12, 55 unidades de ejemplo. Granos de abrasivo: 60 es grueso, 120 es medio y 240 es fino; a mayor número, más fino.")
build(
    O5, 2, F,
    use="Aprenderé a leer designaciones de pernos, una lista de materiales de una unión, una tabla de par de apriete de ejemplo y el grano de un abrasivo.",
    prior=["Sé qué es un elemento de fijación.", "Sé multiplicar enteros.", "Sé leer una tabla."],
    explain=[
        "Un perno se une con una tuerca, y la arandela reparte la presión. Su designación indica el tipo de rosca y sus medidas: M10 × 40 es una rosca métrica de 10 mm de diámetro y 40 mm de largo. La lista de materiales de una unión anota cuántos pernos, tuercas y arandelas lleva. El par de apriete es el esfuerzo de giro con que se aprieta una unión; lo fija el fabricante o el proyecto y se lee en una tabla, porque apretar de más o de menos daña la unión.",
        "El grano indica qué tan grueso o fino es un abrasivo: a menor número, más grueso y más material retira; a mayor número, más fino y mejor acabado. Los valores de esta ficha son de ejemplo y no sirven para ningún trabajo real.",
        f"Las uniones las aprieta personal autorizado con la herramienta y el valor que fijan el fabricante y la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("perno", "elemento de fijación con rosca que se une a una tuerca"), ("tuerca", "pieza con rosca interior que se une a un perno"), ("arandela", "pieza plana que reparte la presión de la unión"), ("designación M10 × 40", "rosca métrica de 10 mm de diámetro y 40 mm de largo"), ("par de apriete", "esfuerzo de giro con que se aprieta una unión"), ("grano", "número que indica qué tan grueso o fino es un abrasivo")],
    worked=[
        ("Leer una designación", "Un perno de ejemplo se designa M12 × 60. ¿Qué diámetro y qué largo tiene?", ["La letra M indica rosca métrica.", "El primer número es el diámetro y el segundo, el largo."], "12 mm de diámetro y 60 mm de largo"),
        ("Elegir un grano", "Se necesita un acabado muy fino y hay abrasivos de grano 80, 180 y 400. ¿Cuál es el más fino?", ["A mayor número, más fino.", "El mayor número es 400."], "El de grano 400"),
    ],
    mistakes=[("Creer que un perno M10 × 40 tiene 40 mm de diámetro.", "El primer número es el diámetro y el segundo, el largo.", "Lee primero el diámetro y luego el largo."),
              ("Usar un valor de par de apriete que alguien recuerda.", "El valor lo fija el fabricante o el proyecto, y se lee en la tabla.", "Consulta la tabla vigente del fabricante.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué indica la designación de rosca M10 × 40?", "Rosca métrica de 10 mm de diámetro y 40 mm de largo", "Rosca métrica de 40 mm de diámetro y 10 mm de largo", "Rosca de 10 vueltas y 40 mm de ancho", "El primer número es el diámetro y el segundo, el largo."),
        ("abc", "En Mecánica Industrial: ¿para qué sirve la arandela en una unión apernada?", "Para repartir la presión de la unión", "Para cortar el perno al largo justo", "Para reemplazar a la tuerca", "La arandela reparte la presión de la unión."),
        ("abc", "En Mecánica Industrial: ¿qué es el par de apriete?", "El esfuerzo de giro con que se aprieta una unión", "El número de pernos de una unión", "La longitud del perno", "El par de apriete es un esfuerzo de giro."),
        ("=", "{F} ¿Cuántas piezas de fijación suman pernos, tuercas y arandelas de la unión?", "4+4+8", "Se suman pernos, tuercas y arandelas.", " piezas"),
        ("abc", "{F} ¿Qué abrasivo de la ficha retira más material y deja el acabado más grueso?", "El de grano 60", "El de grano 120", "El de grano 240", "A menor número de grano, el abrasivo es más grueso."),
        ("abc", "{F} ¿Qué pernos de la unión corresponden a la tabla de par de apriete en la fila M10?", "Los M10 × 40", "Los M8", "Los M12", "La fila M10 corresponde al diámetro 10 mm."),
        ("=", "{F} Una máquina de ejemplo lleva 6 uniones iguales a la de la ficha. ¿Cuántas arandelas se necesitan?", "6*8", "Se multiplican las uniones por las arandelas de cada una.", " arandelas"),
        ("=", "{F} ¿Cuántas unidades de ejemplo más pide la fila M12 que la fila M8?", "55-15", "Se resta el par de la fila M8 al de la fila M12.", " unidades de ejemplo"),
        ("=", "{F} Una unión de ejemplo usa 4 pernos M12 y cada uno se aprieta a lo indicado en la tabla. ¿Cuántas unidades de ejemplo suman los pares de los 4 pernos?", "4*55", "Se multiplican los pernos por el par de cada uno.", " unidades de ejemplo"),
        ("abc", "{F} Un compañero dice: «aprieto más fuerte que lo de la tabla, así queda más segura». ¿Qué respuesta es correcta?", "Es falso: apretar de más puede dañar la rosca o las piezas, y el valor lo fija el fabricante", "Es cierto, porque más apriete es siempre mejor", "Es cierto, si la tuerca es nueva", "El valor de la tabla evita apretar de más o de menos."),
        ("abc", "{F} Se necesita un acabado fino. Un compañero propone empezar con el grano 240 sobre una superficie con marcas profundas. ¿Qué observación es correcta?", "Un grano fino retira poco material y no quita marcas profundas; para ese trabajo sirve uno más grueso", "Es lo mejor, porque el más fino siempre sirve", "Es lo mejor, si se hace más rápido", "El grano fino no elimina marcas profundas con eficacia."),
        ("=", "{F} Una orden pide 3 máquinas con 6 uniones cada una. ¿Cuántos pernos M10 × 40 se necesitan, con 4 pernos por unión?", "3*6*4", "Se multiplican máquinas, uniones y pernos por unión.", " pernos"),
        ("En una lista de ejemplo hay pernos M8 × 30, M10 × 40, M12 × 50 y M10 × 60. ¿Cuántos tienen 10 mm de diámetro?", "2 pernos", "Los M10 × 40 y M10 × 60 tienen 10 mm de diámetro."),
    ],
    ctx=("abc", "Una persona de ejemplo te dice: «no necesitas la tabla, yo sé cuánto apretar de memoria». ¿Qué respondes?", "Que el valor lo fija el fabricante o el proyecto y se consulta en la tabla vigente", "Que sí, porque la memoria basta", "Que se apriete hasta que cueste girar", "Un valor de memoria puede ser incorrecto."),
    sc=[
        ("En Mecánica Industrial: ¿qué significa M12 × 60?", "Rosca métrica de 12 mm de diámetro y 60 mm de largo", "El primer número es el diámetro y el segundo, el largo."),
        ("En Mecánica Industrial: ¿qué grano es más fino, 120 o 240?", "El 240", "A mayor número de grano, más fino es el abrasivo."),
        ("En Mecánica Industrial: ¿quién fija el par de apriete?", "El fabricante o el proyecto", "El valor viene de una fuente técnica y no de la memoria."),
    ],
    op=("Ficha de ejemplo: lista de una unión: 6 pernos M8 × 25, 6 tuercas M8 y 12 arandelas M8. Tabla de ejemplo: M8, 15 unidades de ejemplo; M10, 30 unidades de ejemplo. Escribe (a) qué diámetro y largo tiene cada perno, (b) cuántas piezas de fijación lleva la unión, (c) cuántas unidades de ejemplo suman los pares de los 6 pernos, (d) por qué no se aprieta «a ojo».",
        "(a) 8 mm de diámetro y 25 mm de largo. (b) 6 + 6 + 12 = 24 piezas. (c) 6 × 15 = 90 unidades de ejemplo. (d) Porque el valor lo fija el fabricante o el proyecto; apretar de más o de menos daña la unión.",
        ["lee la designación", "suma las piezas", "calcula la suma de pares", "explica por qué no se aprieta a ojo"],
        ["hoja con las cuatro respuestas"],
        ["invertir diámetro y largo", "olvidar alguna pieza", "decir que se aprieta de memoria"],
        "Pregunta: «¿el 25 es el diámetro o el largo?». Si duda, pídele que relea la designación."),
    reinforce="Inventa dos designaciones de pernos y escribe el diámetro y el largo de cada una.",
    extend="Explica con un ejemplo por qué se parte de un grano grueso y se avanza hacia uno fino.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (caso de ejemplo con medidas en µm, inventadas; 20.000 µm son 20 mm). Plano: agujero con medidas entre 20.000 y 20.021 µm. Eje 1 (de ejemplo): entre 19.959 y 19.980 µm. Eje 2 (de ejemplo): entre 20.035 y 20.048 µm. "
     "Definiciones del taller: el juego es la diferencia entre el agujero y el eje cuando el agujero es mayor; el apriete es la diferencia cuando el eje es mayor que el agujero. "
     "Juego mínimo = agujero mínimo menos eje máximo; juego máximo = agujero máximo menos eje mínimo. Un resultado negativo indica apriete.")
build(
    O5, 3, F,
    use="Aprenderé a calcular el juego o el apriete entre un eje y un agujero con medidas en µm y a decidir qué tipo de ajuste es.",
    prior=["Sé que 1 mm tiene 1.000 µm.", "Sé restar números enteros, incluso con resultado negativo.", "Sé qué es un eje y un agujero."],
    explain=[
        "Cuando un eje entra en un agujero, la diferencia entre sus medidas decide cómo encajan. Si el agujero es mayor que el eje queda un juego y el eje se mueve; si el eje es mayor que el agujero hay un apriete y la unión queda firme. El plano no da una medida exacta sino un intervalo entre un valor máximo y uno mínimo, por eso se calculan un juego mínimo y un juego máximo.",
        "Juego mínimo es el agujero mínimo menos el eje máximo, y juego máximo es el agujero máximo menos el eje mínimo. Si los dos son positivos, el ajuste es con juego; si los dos son negativos, es con apriete; si uno es positivo y el otro negativo, es indeterminado, porque según las piezas reales puede quedar juego o apriete.",
        f"Es un cálculo en papel; no se arma ni se ajusta ninguna pieza. {EMER} {AVISO}",
    ],
    vocab=[("juego", "diferencia entre el agujero y el eje cuando el agujero es mayor"), ("apriete", "diferencia entre el eje y el agujero cuando el eje es mayor"), ("ajuste con juego", "ajuste en que el juego mínimo y el máximo son positivos"), ("ajuste con apriete", "ajuste en que el juego mínimo y el máximo son negativos"), ("ajuste indeterminado", "ajuste en que según las piezas puede quedar juego o apriete"), ("intervalo", "medidas entre un valor mínimo y uno máximo")],
    worked=[
        ("Calcular el juego", "Un agujero de ejemplo mide entre 30.000 y 30.025 µm y un eje, entre 29.970 y 29.990 µm. ¿Cuánto es el juego mínimo y el máximo?", ["Mínimo: 30.000 menos 29.990 son 10 µm.", "Máximo: 30.025 menos 29.970 son 55 µm."], "Juego mínimo 10 µm y juego máximo 55 µm"),
        ("Clasificar el ajuste", "Un ajuste de ejemplo tiene juego mínimo de −5 µm y juego máximo de 30 µm. ¿De qué tipo es?", ["Uno de los valores es negativo y el otro positivo.", "Entonces puede quedar juego o apriete."], "Indeterminado"),
    ],
    mistakes=[("Restar el eje mínimo al agujero mínimo para el juego mínimo.", "El juego mínimo se calcula con el eje máximo.", "Usa agujero mínimo menos eje máximo."),
              ("Decir «con apriete» cuando solo uno de los dos valores es negativo.", "Si uno es positivo y el otro negativo, es indeterminado.", "Mira los signos de ambos resultados.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es un apriete entre un eje y un agujero?", "La diferencia cuando el eje es mayor que el agujero", "La diferencia cuando el agujero es mayor que el eje", "La suma de las medidas del eje y del agujero", "El apriete aparece cuando el eje es mayor y la unión queda firme."),
        ("abc", "En Mecánica Industrial: ¿cuándo un ajuste es indeterminado?", "Cuando el juego mínimo es negativo y el máximo es positivo", "Cuando ambos juegos son positivos", "Cuando ambos juegos son negativos", "Según las piezas reales puede quedar juego o apriete."),
        ("abc", "En Mecánica Industrial: ¿cómo se calcula el juego máximo?", "Agujero máximo menos eje mínimo", "Agujero mínimo menos eje máximo", "Eje máximo menos agujero mínimo", "El juego máximo combina el agujero más grande con el eje más pequeño."),
        ("=", "{F} ¿Cuánto vale el juego mínimo del agujero con el eje 1, en µm?", "20000-19980", "Se resta el eje máximo al agujero mínimo.", " µm"),
        ("=", "{F} ¿Cuánto vale el juego máximo del agujero con el eje 1, en µm?", "20021-19959", "Se resta el eje mínimo al agujero máximo.", " µm"),
        ("abc", "{F} ¿Qué tipo de ajuste forman el agujero y el eje 1?", "Con juego, porque ambos juegos son positivos", "Con apriete, porque el eje es menor", "Indeterminado, porque hay dos medidas", "Los juegos 20 y 62 µm son ambos positivos."),
        ("=", "{F} ¿Cuánto vale el juego mínimo del agujero con el eje 2, en µm? Un resultado negativo indica apriete.", "20000-20048", "Se resta el eje máximo al agujero mínimo.", " µm"),
        ("=", "{F} ¿Cuánto vale el juego máximo del agujero con el eje 2, en µm?", "20021-20035", "Se resta el eje mínimo al agujero máximo.", " µm"),
        ("abc", "{F} ¿Qué tipo de ajuste forman el agujero y el eje 2?", "Con apriete, porque ambos resultados son negativos", "Con juego, porque el agujero es de 20.000 µm", "Indeterminado, porque la diferencia es pequeña", "Los resultados −48 y −14 µm son negativos."),
        ("abc", "{F} Un compañero dice: «el eje 1 y el eje 2 sirven igual porque miden casi 20 mm». ¿Qué respuesta es correcta?", "Es falso: el eje 1 deja juego y el eje 2 queda con apriete, y el plano pide un ajuste determinado", "Es cierto, porque la diferencia es de micrones", "Es cierto, si se mide con un instrumento digital", "En ajustes, los micrones cambian el comportamiento de la unión."),
        ("abc", "{F} El plano pide que el eje gire libremente dentro del agujero. ¿Qué eje cumple?", "El eje 1, que tiene juego", "El eje 2, que tiene apriete", "Ninguno de los dos, porque tienen intervalos", "El giro libre exige juego y el eje 1 lo tiene."),
        ("=", "{F} Se fabrican 7 ejes del tipo 1 y 3 del tipo 2, y todos se arman con un agujero del plano. ¿Qué porcentaje de los ejes quedará con apriete?", "3*100//10", "Solo los 3 ejes del tipo 2 forman ajuste con apriete, sobre un total de 10 ejes.", " %"),
        ("Un agujero de ejemplo mide entre 40.000 y 40.025 µm y un eje, entre 40.010 y 40.030 µm. ¿Qué tipo de ajuste forman?", "Indeterminado, porque el juego mínimo es −30 µm y el máximo es 15 µm", "El mínimo es 40.000 menos 40.030, que da −30; el máximo es 40.025 menos 40.010, que da 15."),
    ],
    ctx=("abc", "En un taller de ejemplo, alguien dice: «el eje entra a mano, así que es un ajuste con juego». ¿Qué respondes?", "Que se confirma con las medidas y el plano, porque la sensación puede engañar", "Que sí, porque basta con probar", "Que se pruebe a golpes hasta que entre", "El ajuste se define por medidas, no por la sensación al armar."),
    sc=[
        ("En Mecánica Industrial: ¿qué es un juego?", "La diferencia cuando el agujero es mayor que el eje", "El juego permite que el eje se mueva."),
        ("En Mecánica Industrial: ¿qué indica un resultado negativo al restar?", "Un apriete", "Negativo significa que el eje es mayor que el agujero."),
        ("En Mecánica Industrial: ¿cómo se calcula el juego mínimo?", "Agujero mínimo menos eje máximo", "El juego mínimo combina agujero más pequeño con eje más grande."),
    ],
    op=("Ficha de ejemplo: un agujero mide entre 50.000 y 50.025 µm. Eje A: entre 49.950 y 49.975 µm. Eje B: entre 50.030 y 50.050 µm. Escribe (a) el juego mínimo y el máximo con el eje A, (b) el tipo de ajuste con A, (c) el juego mínimo y el máximo con el eje B, (d) el tipo de ajuste con B.",
        "(a) Mínimo: 50.000 − 49.975 = 25 µm; máximo: 50.025 − 49.950 = 75 µm. (b) Con juego. (c) Mínimo: 50.000 − 50.050 = −50 µm; máximo: 50.025 − 50.030 = −5 µm. (d) Con apriete.",
        ["calcula juegos con A", "clasifica con A", "calcula con B", "clasifica con B"],
        ["hoja con los cuatro resultados"],
        ["restar con el eje equivocado", "ignorar el signo", "clasificar sin calcular"],
        "Pregunta: «¿qué medidas usas para el juego mínimo?». Si duda, pídele que relea la definición."),
    reinforce="Inventa un agujero y un eje con intervalos y calcula el juego mínimo y el máximo.",
    extend="Explica con un ejemplo por qué un ajuste indeterminado puede ser un problema en una pieza que debe girar libre.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (pedido de ejemplo, inventado). El «Taller Demo» debe armar 15 soportes. Cada soporte lleva 6 pernos M10 × 40, 6 tuercas M10 y 12 arandelas M10. En bodega hay 80 pernos, 90 tuercas y 200 arandelas. "
     "Costos de ejemplo: perno $120; tuerca $60; arandela $20. Cada soporte requiere pulir 4 superficies y cada disco abrasivo alcanza para 10 superficies. Cada disco cuesta $900. Cada soporte genera 200 g de limaduras de ejemplo.")
build(
    O5, 4, F,
    use="Aprenderé a calcular necesidades de materiales, faltantes, costos, abrasivos y residuos de un pedido, con datos de ejemplo.",
    prior=["Sé multiplicar y dividir enteros.", "Sé comparar lo que hay con lo que se necesita.", "Sé pasar gramos a kilogramos."],
    explain=[
        "Un pedido se convierte en una lista de necesidades multiplicando lo que lleva una unidad por el número de unidades. Luego se compara con el inventario: lo que hay en bodega menos lo que se necesita da el sobrante (si es positivo) o el faltante (si es negativo, tomando su valor sin signo). El costo de materiales es la suma de cada cantidad por su precio.",
        "Los abrasivos se calculan con su rendimiento: si un disco alcanza para cierto número de superficies, se divide el total de superficies entre ese rendimiento y se redondea hacia arriba, porque no se compran discos a medias. Los residuos también se cuentan: las limaduras totales se calculan por unidad y se expresan en kilogramos.",
        f"Es un cálculo en papel con datos de ejemplo; no se ejecuta ninguna tarea. {EMER} {AVISO}",
    ],
    vocab=[("necesidad", "cantidad total que pide un pedido"), ("inventario", "cantidad que hay en bodega"), ("faltante", "cantidad que falta para cubrir la necesidad"), ("sobrante", "cantidad que queda después de cubrir la necesidad"), ("rendimiento", "cuántas superficies alcanza a trabajar un disco abrasivo")],
    worked=[
        ("Calcular una necesidad", "Un pedido de ejemplo es de 8 conjuntos y cada uno lleva 5 pernos. ¿Cuántos pernos se necesitan?", ["Se multiplican los conjuntos por los pernos de cada uno.", "8 por 5 son 40."], "40 pernos"),
        ("Redondear hacia arriba", "Se deben trabajar 45 superficies y cada disco alcanza para 10. ¿Cuántos discos se compran?", ["45 dividido en 10 da 4 y sobran 5 superficies.", "Para esas 5 hace falta un disco más."], "5 discos"),
    ],
    mistakes=[("Comprar solo los discos de la división exacta y dejar superficies sin cubrir.", "Una división con resto exige un disco más.", "Redondea hacia arriba cuando sobran superficies."),
              ("Mezclar gramos y kilogramos al sumar residuos.", "Las unidades distintas no se suman directamente.", "Convierte todo a una misma unidad antes de sumar.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es el inventario de una bodega?", "La cantidad que hay disponible", "La cantidad que pide el pedido", "El costo de cada pieza", "El inventario es lo que hay en bodega."),
        ("abc", "En Mecánica Industrial: ¿qué es un faltante?", "La cantidad que falta para cubrir la necesidad", "La cantidad que sobra después de cubrir la necesidad", "El precio extra de un material", "El faltante es la parte de la necesidad que no está en bodega."),
        ("abc", "En Mecánica Industrial: ¿por qué los discos abrasivos se redondean hacia arriba?", "Porque no se compran discos a medias y las superficies restantes también hay que cubrir", "Porque los discos siempre rinden más de lo indicado", "Porque así se baja el costo", "Un resto de superficies exige un disco más."),
        ("=", "{F} ¿Cuántos pernos se necesitan para los 15 soportes?", "15*6", "Se multiplican los soportes por los pernos de cada uno.", " pernos"),
        ("=", "{F} ¿Cuántas arandelas se necesitan para los 15 soportes?", "15*12", "Se multiplican los soportes por las arandelas de cada uno.", " arandelas"),
        ("=", "{F} ¿Cuántos pernos faltan, si en bodega hay 80 y se necesitan 90?", "90-80", "Se resta el inventario a la necesidad.", " pernos"),
        ("=", "{F} ¿Cuántas arandelas sobran después de cubrir el pedido?", "200-15*12", "Se resta la necesidad al inventario.", " arandelas"),
        ("=", "{F} ¿Cuánto cuestan los pernos, las tuercas y las arandelas de un soporte?", "6*120+6*60+12*20", "Se suma cada cantidad por su precio.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántas superficies hay que pulir en los 15 soportes?", "15*4", "Se multiplican los soportes por las superficies de cada uno.", " superficies"),
        ("=", "{F} ¿Cuántos discos abrasivos se compran para pulir 60 superficies, si cada disco alcanza para 10 superficies?", "60//10", "Se dividen las superficies entre el rendimiento de un disco.", " discos"),
        ("abc", "{F} Un compañero dice: «en bodega hay 90 tuercas y se necesitan 90, así que no falta nada». ¿Qué respuesta es correcta?", "Es cierto para las tuercas, pero faltan 10 pernos y no se puede armar todo el pedido", "Es cierto, y se puede armar todo el pedido", "Es falso, porque faltan tuercas", "Las tuercas alcanzan, pero faltan pernos."),
        ("=", "{F} ¿Cuántos kg de limaduras de ejemplo generan los 15 soportes?, usando 1 kg = 1.000 g.", "15*200//1000", "Se multiplican los soportes por los gramos de cada uno y se pasan a kilogramos.", " kg"),
        ("=", "{F} Para completar el pedido hay que comprar los pernos que faltan al precio de ejemplo de $120 cada uno. ¿Cuánto cuesta la compra?", "10*120", "Se multiplican los pernos faltantes por su precio.", " pesos de ejemplo"),
    ],
    ctx=("abc", "El jefe de un taller de ejemplo pide «compra los discos justos para 45 superficies, rinden 10 cada uno». ¿Qué cantidad propones?", "5 discos, porque sobran 5 superficies que también hay que cubrir", "4 discos, porque 45 dividido en 10 es 4", "6 discos, para tener muchos de repuesto", "Un resto obliga a comprar un disco más."),
    sc=[
        ("En Mecánica Industrial: ¿cómo se calcula una necesidad total?", "Multiplicando lo que lleva una unidad por el número de unidades", "La necesidad total depende de cada unidad y del pedido."),
        ("En Mecánica Industrial: ¿qué es un sobrante?", "Lo que queda en bodega después de cubrir la necesidad", "El sobrante se calcula restando la necesidad al inventario."),
        ("En Mecánica Industrial: ¿qué se hace antes de sumar gramos y kilogramos?", "Convertirlos a una misma unidad", "No se suman unidades distintas sin convertir."),
    ],
    op=("Ficha de ejemplo: un pedido de 12 bases. Cada base lleva 4 pernos, 4 tuercas y 8 arandelas. En bodega hay 40 pernos, 50 tuercas y 100 arandelas. Costos de ejemplo: perno $100, tuerca $50, arandela $10. Escribe (a) cuántos pernos, tuercas y arandelas se necesitan, (b) cuál falta y cuánto, (c) cuánto cuesta comprar lo que falta, (d) una conclusión.",
        "(a) Pernos: 12 × 4 = 48; tuercas: 48; arandelas: 12 × 8 = 96. (b) Faltan 8 pernos (48 − 40). (c) 8 × 100 = 800 pesos de ejemplo. (d) Con las tuercas y las arandelas disponibles solo falta comprar 8 pernos para armar el pedido completo.",
        ["calcula las necesidades", "identifica el faltante", "calcula el costo", "concluye"],
        ["hoja con las cuatro respuestas"],
        ["no comparar con la bodega", "equivocarse de precio", "no concluir"],
        "Pregunta: «¿qué hay en bodega y qué se necesita?». Si duda, pídele que arme una tabla con ambas columnas."),
    reinforce="Inventa un pedido con tres materiales y calcula necesidades y faltantes.",
    extend="Explica con un ejemplo por qué hay que redondear hacia arriba al comprar discos abrasivos.",
)
