"""Forestal TP 3.º y 4.º medio: OAE-08 (máquinas y herramientas forestales: categorías, documentos, señalética, rendimientos y comparación; solo conceptos y cálculos en papel). Sin procedimientos de uso ni de operación."""
from __future__ import annotations

from tp_fore_common import AVISO, EMER, build

O8 = "TP-FORE-3y4-OAE-08"

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Faena Demo: 6 herramientas manuales, 3 herramientas motorizadas de mano y 2 máquinas de mayor tamaño, todas ficticias. "
     "Peligros anotados: ruido, vibración, partes móviles, proyección de partículas, atrapamiento y cansancio. "
     "Dotación: 20 personas, de las cuales 8 tienen autorización vigente para operar equipos motorizados (dato de ejemplo). Regla interna de ejemplo: una pausa de 15 minutos al terminar cada bloque de 2 horas de trabajo con equipos motorizados.")
build(
    O8, 1, F,
    use="Aprenderé las categorías de máquinas y herramientas forestales, sus peligros principales, qué significa tener autorización para operar y qué reglas generales protegen a las personas, sin aprender a operar ninguna.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé calcular porcentajes simples.", "Sé qué es el manual del fabricante."],
    explain=[
        "En las faenas forestales se distinguen tres categorías de equipos. Las herramientas manuales funcionan con la fuerza de la persona. Las herramientas motorizadas de mano tienen un motor propio y se sostienen con las manos. Las máquinas de mayor tamaño son equipos grandes que se desplazan y se operan desde una cabina o un puesto. Cada categoría tiene peligros propios: ruido, vibración (un movimiento oscilante que el equipo transmite al cuerpo), partes móviles, proyección de partículas, atrapamiento y cansancio.",
        "Solo opera un equipo motorizado quien tiene una autorización vigente, es decir, el reconocimiento escrito de que está capacitado para ese equipo, de acuerdo con las especificaciones del fabricante y la norma vigente. La experiencia previa o ser mayor de edad no reemplazan la autorización. Los peligros se controlan con la jerarquía de controles: eliminar o sustituir, protecciones físicas, reglas como pausas y turnos, y como última barrera el EPP.",
        f"Este cuaderno no explica cómo se opera ninguna herramienta ni máquina. {EMER} {AVISO}",
    ],
    vocab=[("herramienta manual", "herramienta que funciona con la fuerza de la persona"), ("herramienta motorizada de mano", "herramienta con motor propio que se sostiene con las manos"), ("máquina de mayor tamaño", "equipo grande que se desplaza y se opera desde una cabina o un puesto"), ("vibración", "movimiento oscilante que un equipo transmite al cuerpo"), ("autorización de operador", "reconocimiento escrito de que una persona está capacitada para operar un equipo"), ("pausa", "descanso programado para reducir el cansancio y la exposición")],
    worked=[
        ("Clasificar un equipo", "Un equipo de ejemplo tiene motor propio y se sostiene con las manos. ¿A qué categoría pertenece?", ["Tiene motor propio, así que no es manual.", "Se sostiene con las manos, así que no es una máquina de mayor tamaño."], "Herramienta motorizada de mano"),
        ("Porcentaje autorizado", "En un equipo de ejemplo de 25 personas, 10 tienen autorización vigente. ¿Qué porcentaje es?", ["10 ÷ 25 son 40 de cada 100.", "El porcentaje es 40 %."], "40 %"),
    ],
    mistakes=[("Creer que la experiencia previa reemplaza la autorización vigente.", "La autorización acredita la capacitación para ese equipo y esa norma.", "Opera solo quien tiene autorización vigente."),
              ("Creer que un equipo pequeño es seguro para cualquier persona.", "Las herramientas motorizadas de mano también tienen peligros graves.", "Se usan solo con autorización, instructor y norma vigente.")],
    T=[
        ("abc", "En Forestal: ¿qué es una herramienta motorizada de mano?", "Una herramienta con motor propio que se sostiene con las manos", "Una herramienta que funciona con la fuerza de la persona", "Una máquina grande que se opera desde una cabina", "La motorizada de mano tiene motor propio y se sostiene; la manual no tiene motor."),
        ("abc", "En Forestal: ¿qué es la autorización de un operador?", "El reconocimiento escrito de que una persona está capacitada para operar un equipo", "El permiso para llevarse un equipo a la casa", "El contrato de compra de un equipo", "La autorización acredita la capacitación para operar un equipo determinado."),
        ("abc", "En Forestal: ¿qué es la vibración como peligro de un equipo?", "Un movimiento oscilante que el equipo transmite al cuerpo", "El sonido muy fuerte que produce el motor", "El temblor del terreno por la lluvia", "La vibración se transmite al cuerpo desde el equipo; el ruido es otro peligro."),
        ("=", "{F} ¿Cuántos equipos tiene la faena en total?", "6+3+2", "Se suman los equipos de las tres categorías.", " equipos"),
        ("=", "{F} ¿Qué porcentaje de la dotación tiene autorización vigente para operar equipos motorizados?", "8*100//20", "Se divide las personas autorizadas entre la dotación y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas personas de la dotación no tienen autorización vigente?", "20-8", "Se restan las personas autorizadas al total de la dotación.", " personas"),
        ("abc", "{F} ¿Quién puede operar los equipos motorizados de la faena?", "Solo el personal con autorización vigente", "Cualquier persona con experiencia previa", "Cualquier persona mayor de edad", "La experiencia o la edad no reemplazan una autorización vigente."),
        ("abc", "{F} Un compañero sin autorización dice: «soy bueno con las motorizadas, la uso solo un rato». ¿Qué respuesta es correcta?", "No puede usarla: sin autorización vigente no se opera un equipo motorizado", "Puede usarla si es un rato corto", "Puede usarla si lleva casco", "La autorización es obligatoria, sin importar el tiempo ni el EPP."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «ruido»?", "Que la persona sufra daño en la audición", "El ruido que se escucha en la faena", "Que el equipo se vea desordenado", "El riesgo es la posibilidad de daño; el ruido es la fuente del peligro."),
        ("abc", "{F} La protección auditiva obligatoria es un control de nivel:", "EPP, la última barrera, que protege solo a quien la usa", "De eliminación, porque quita el ruido", "De ingeniería, porque cambia el equipo", "La protección auditiva no quita el ruido; protege a quien la usa."),
        ("abc", "{F} Frente al ruido, ¿qué control es más efectivo que la protección auditiva?", "Sustituir por un equipo más silencioso o aislar la fuente del ruido", "Entregar más protectores a cada persona", "Pedir a todos que trabajen más rápido", "Actuar sobre la fuente es mejor que depender solo del EPP."),
        ("=", "{F} En una jornada de 8 horas, ¿cuántos minutos de pausa se acumulan con la regla interna de la ficha?", "(8//2)*15", "Se calculan los bloques de 2 horas y se multiplican por los minutos de pausa.", " minutos"),
        ("abc", "Durante una visita de ejemplo, una máquina se vuelca cerca de la faena y una persona queda atrapada. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a mover la máquina", "Intentar sacar a la persona entre varias personas", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
    ],
    ctx=("abc", "Un amigo te propone usar sin permiso una herramienta motorizada de la empresa de su familia «para practicar un rato». ¿Qué respondes?", "Que no, porque operar un equipo exige autorización, instructor y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si el equipo está nuevo", "Que sí, si usas guantes", "Un equipo nuevo o unos guantes no reemplazan la autorización ni el instructor."),
    sc=[
        ("En Forestal: ¿qué es una herramienta manual?", "Una herramienta que funciona con la fuerza de la persona", "No tiene motor propio y se acciona con la fuerza de la persona."),
        ("¿Quién opera un equipo motorizado?", "Solo quien tiene autorización vigente", "La autorización acredita la capacitación para ese equipo."),
        ("¿Qué es el último nivel de la jerarquía de controles?", "El equipo de protección personal (EPP)", "El EPP protege solo a quien lo usa y no quita el peligro."),
    ],
    op=("Ficha de ejemplo: «Faena Muestra» tiene 8 herramientas manuales, 4 herramientas motorizadas de mano y 3 máquinas de mayor tamaño. La dotación es de 30 personas, de las cuales 12 tienen autorización vigente. Peligros anotados: ruido y vibración. Regla interna de ejemplo: una pausa de 10 minutos al terminar cada bloque de 2 horas con equipos motorizados. Escribe (a) cuántos equipos hay y qué porcentaje del personal está autorizado, (b) los minutos de pausa en una jornada de 8 horas, (c) un control más efectivo que el EPP para el ruido, (d) por qué la experiencia previa no basta para operar.",
        "(a) 8 + 4 + 3 = 15 equipos; 12 ÷ 30 = 40 %. (b) 4 bloques × 10 = 40 minutos. (c) Sustituir por un equipo más silencioso o aislar la fuente. (d) Porque se necesita una autorización vigente que acredita la capacitación para ese equipo, además de instructor y norma vigente.",
        ["calcula equipos y porcentaje", "calcula las pausas", "propone un control más efectivo que el EPP", "explica por qué la experiencia no basta"],
        ["hoja con las cuatro respuestas"],
        ["no sumar los tres tipos de equipos", "proponer solo el EPP", "creer que la experiencia reemplaza la autorización"],
        "Pregunta: «¿qué documento acredita que una persona puede operar un equipo?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe una oración que distinga una herramienta manual de una motorizada y una máquina de mayor tamaño.",
    extend="Explica con un ejemplo por qué las pausas programadas son un control administrativo para la vibración.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (señales y lista de verificación de ejemplo, inventadas). Señales de un taller de ejemplo, descritas por escrito: S1, círculo con borde rojo y una raya, «prohibido el paso a personal no autorizado»; "
     "S2, círculo azul, «uso obligatorio de casco»; S3, triángulo amarillo, «precaución, partes móviles»; S4, rectángulo verde, «salida de emergencia». "
     "Lista de verificación previa al uso (revisada por personal autorizado) con 5 ítems: protecciones en su lugar; combustible sin fugas; EPP disponible; zona despejada; autorización vigente. "
     "Resultado de una revisión de ejemplo: 4 ítems cumplen; el ítem «protecciones en su lugar» no cumple.")
build(
    O8, 2, F,
    use="Aprenderé los documentos y las señales de la seguridad con máquinas y herramientas: manual, ficha técnica, señalética, lista de verificación previa al uso y roles.",
    prior=["Sé las categorías de equipos y qué es la autorización.", "Sé calcular porcentajes simples.", "Sé qué es una lista de verificación."],
    explain=[
        "El manual del fabricante y la ficha técnica son los documentos que describen cada equipo: usos permitidos, límites y mantención. La señalética usa formas y colores normalizados para que todas las personas la entiendan rápido: en general, las señales de prohibición tienen un círculo con borde rojo, las de obligación son círculos azules, las de advertencia son triángulos amarillos y las de salida de emergencia o seguridad son verdes. Una señal informa, pero no impide físicamente un riesgo, por eso es un control administrativo.",
        "La lista de verificación previa al uso es un documento con puntos que el personal autorizado revisa antes de usar un equipo. Si un ítem no cumple, el equipo no se usa hasta corregirlo y la persona responsable lo anota. Cada rol cumple su función: el operador autorizado revisa y usa, el jefe de faena decide, el prevencionista asesora en riesgos y el mecánico autorizado repara. Nadie firma una revisión sin haberla hecho.",
        f"Estos documentos se leen aquí en papel; la revisión real de un equipo la hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("señalética", "conjunto de señales con formas y colores normalizados"), ("señal de prohibición", "señal con círculo de borde rojo que indica lo que no se debe hacer"), ("señal de obligación", "señal con círculo azul que indica lo que se debe hacer"), ("señal de advertencia", "señal con triángulo amarillo que indica un peligro"), ("lista de verificación previa al uso", "documento con puntos que revisa personal autorizado antes de usar un equipo"), ("ficha técnica", "documento con las características y los límites de un equipo")],
    worked=[
        ("Leer una señal", "Una señal de ejemplo es un círculo azul que dice «uso obligatorio de protección auditiva». ¿Qué tipo de señal es?", ["El círculo azul es de obligación.", "Indica lo que se debe hacer."], "De obligación"),
        ("Porcentaje de una lista", "Una lista de ejemplo tiene 8 ítems y 6 cumplen. ¿Qué porcentaje no cumple?", ["No cumplen 8 − 6 = 2 ítems.", "2 ÷ 8 son 25 de cada 100."], "25 %"),
    ],
    mistakes=[("Firmar una lista de verificación sin revisar los ítems para ahorrar tiempo.", "Una revisión firmada pero no hecha oculta riesgos.", "Se firma solo lo que se revisó."),
              ("Creer que una señal impide físicamente el peligro.", "Una señal informa, pero no impide el acceso por sí sola.", "Combina señales con barreras físicas cuando se pueda.")],
    T=[
        ("abc", "En Forestal: ¿cómo es, en general, una señal de prohibición?", "Un círculo con borde rojo", "Un círculo azul", "Un triángulo amarillo", "Las señales de prohibición usan círculos con borde rojo; las de obligación son azules."),
        ("abc", "En Forestal: ¿qué indica una señal de obligación?", "Una acción que se debe cumplir, como usar casco", "Un peligro del lugar, como partes móviles", "La salida en caso de emergencia", "La obligación manda hacer algo; la advertencia avisa de un peligro."),
        ("abc", "En Forestal: ¿qué es la lista de verificación previa al uso de un equipo?", "Un documento con puntos que revisa personal autorizado antes de usarlo", "Un documento con el precio de compra del equipo", "Un manual para aprender a operar el equipo", "La lista verifica condiciones antes del uso; no enseña ni fija precios."),
        ("=", "{F} ¿Qué porcentaje de los ítems de la lista cumple en la revisión de ejemplo?", "4*100//5", "Se divide los ítems que cumplen entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué indica la señal S3?", "Precaución por la presencia de partes móviles", "Prohibido el paso a personal no autorizado", "Uso obligatorio de casco", "S3 es un triángulo amarillo, es decir, una advertencia."),
        ("abc", "{F} Según la señal S1, ¿quién puede pasar a la zona?", "Solo el personal autorizado", "Cualquier persona con casco", "Cualquier persona acompañada", "La señal prohíbe el paso a quienes no estén autorizados."),
        ("abc", "{F} El ítem «protecciones en su lugar» no cumple. ¿Qué corresponde?", "No usar el equipo hasta corregirlo, y anotarlo", "Usarlo si el trabajo es corto", "Marcar el ítem como cumple", "Con un ítem de protección en falta el equipo no se usa."),
        ("abc", "{F} ¿Qué señal indica el camino de salida en una emergencia?", "S4, el rectángulo verde", "S2, el círculo azul", "S1, el círculo con borde rojo", "El verde indica salida de emergencia o seguridad."),
        ("=", "{F} Si se coloca una señal de cada tipo en cada una de 5 zonas del taller, ¿cuántas señales se necesitan?", "4*5", "Se multiplican los tipos de señal por las zonas.", " señales"),
        ("abc", "En Forestal: ¿por qué la señalética usa formas y colores normalizados?", "Para que cualquier persona la entienda rápido y sin ambigüedad", "Para decorar el taller", "Para reemplazar la capacitación del personal", "La normalización permite una comprensión inmediata, pero no reemplaza la formación."),
        ("abc", "{F} ¿Una señal S1 reemplaza una barrera física que cierre el acceso?", "No: informa, pero no impide físicamente el paso", "Sí: basta con la señal para controlar el acceso", "Sí, si la señal es de color rojo", "La señal es un control administrativo, menos efectivo que una barrera."),
        ("=", "Una faena de ejemplo tiene 11 equipos y la revisión previa de cada uno toma 10 minutos de personal autorizado. ¿Cuántos minutos se necesitan para revisar todos?", "11*10", "Se multiplican los equipos por los minutos de cada revisión.", " minutos"),
        ("abc", "{F} Un operador autorizado dice que la señal «uso obligatorio de casco» no aplica porque solo se acercará un momento. ¿Qué respuesta es correcta?", "Aplica a cualquier persona que esté en la zona, aunque sea un momento", "No aplica a los operadores autorizados", "No aplica si el momento es corto", "Las señales de obligación rigen para quien entre a la zona, sin importar el tiempo."),
    ],
    ctx=("abc", "Un compañero te pide firmar la lista de verificación previa al uso de un equipo sin haberla revisado, porque «ya es tarde». ¿Qué respondes?", "Que no firmas lo que no has revisado, y avisas a un adulto responsable", "Que sí, porque la lista es un trámite", "Que firmas, pero solo la mitad", "Firmar sin revisar oculta riesgos y es una falta grave."),
    sc=[
        ("En Forestal: ¿de qué color es una señal de advertencia?", "Es un triángulo amarillo", "La advertencia avisa de un peligro."),
        ("¿Qué se hace si un ítem de la lista no cumple?", "No se usa el equipo hasta corregirlo", "Un ítem en falta compromete la seguridad."),
        ("¿Una señal impide físicamente un peligro?", "No, informa y es un control administrativo", "Solo una barrera física impide el acceso."),
    ],
    op=("Ficha de ejemplo: lista de verificación de un equipo de ejemplo con 5 ítems (protecciones en su lugar; combustible sin fugas; EPP disponible; zona despejada; autorización vigente). Resultado: 3 ítems cumplen y 2 no cumplen: «combustible sin fugas» y «zona despejada». Señales del taller: un círculo azul «uso obligatorio de casco», un triángulo amarillo «precaución, partes móviles» y un círculo con borde rojo «prohibido el paso». Escribe (a) el porcentaje de ítems que cumple, (b) qué haces con el equipo, (c) qué tipo de señal es cada una de las tres señales, (d) por qué una señal no reemplaza una barrera física.",
        "(a) 3 ÷ 5 = 60 %. (b) No se usa el equipo hasta corregir los ítems que no cumplen, y se anota. (c) El círculo azul es de obligación, el triángulo amarillo es de advertencia y el círculo con borde rojo es de prohibición. (d) Porque la señal informa, pero no impide físicamente el acceso ni depende del equipo.",
        ["calcula el porcentaje", "decide no usar el equipo", "clasifica las tres señales", "explica el límite de una señal"],
        ["hoja con las cuatro respuestas"],
        ["marcar cumple lo que no cumple", "confundir advertencia con prohibición", "creer que la señal basta"],
        "Pregunta: «¿de qué color es una señal de obligación?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Dibuja o describe con palabras una señal de advertencia, una de obligación y una de prohibición, con su color y su forma.",
    extend="Explica con un ejemplo por qué la lista de verificación previa al uso es un control administrativo.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (registro de inspección de ejemplo, inventado). Observaciones de una jornada en la Faena Demo: A, un operador usó un equipo motorizado con la autorización vencida; B, una persona trabajó cerca de un equipo ruidoso sin protección auditiva; "
     "C, la lista de verificación previa al uso estaba completa y firmada; D, la zona de exclusión estaba señalizada; E, un operador usó un equipo que vibra durante 6 horas, y la regla interna de ejemplo permite un máximo de 4 horas por día. "
     "Renovar la autorización y la capacitación de una persona cuesta $50.000 (dato de ejemplo). Hay 3 operadores con la autorización vencida.")
build(
    O8, 3, F,
    use="Aprenderé a analizar un registro de inspección: reconocer no conformidades, calcular el cumplimiento, proponer acciones correctivas según la jerarquía y registrar sin ocultar nada.",
    prior=["Sé qué es un control administrativo, de ingeniería y de EPP.", "Sé calcular porcentajes simples.", "Sé qué es una lista de verificación."],
    explain=[
        "Una no conformidad es un incumplimiento de un requisito, como una autorización vencida o un equipo usado más horas de lo permitido. El cumplimiento se calcula dividiendo las observaciones que cumplen entre el total y multiplicando por 100. Para cada no conformidad se define una acción correctiva, una medida que corrige el problema y evita que se repita, con responsable y plazo. Las acciones se piensan con la jerarquía de controles: primero actuar sobre la fuente y las barreras físicas y después las reglas y el EPP.",
        "Todo se registra tal como ocurrió, aunque no haya habido lesionados. Registrar permite corregir y demostrar que se actuó. Nunca se modifica el registro para que «cumpla»: cambiar un dato oculta el problema y expone a las personas. Antes de una visita de la autoridad se corrige lo que se pueda y se registran las acciones, pero no se ocultan las no conformidades.",
        f"La inspección real la hacen personas capacitadas; aquí solo analizas un registro escrito. {EMER} {AVISO}",
    ],
    vocab=[("no conformidad", "incumplimiento de un requisito"), ("acción correctiva", "medida que corrige una no conformidad y evita que se repita"), ("cumplimiento", "porcentaje de observaciones que cumplen sobre el total"), ("responsable", "persona a quien se asigna una acción"), ("plazo", "fecha límite para completar una acción")],
    worked=[
        ("Detectar una no conformidad", "Un registro de ejemplo dice: «equipo usado con una protección retirada». ¿Es cumplimiento o no conformidad?", ["Usar un equipo sin una protección incumple un requisito.", "Es una no conformidad."], "No conformidad"),
        ("Calcular el cumplimiento", "En una inspección de ejemplo hay 10 observaciones y 7 cumplen. ¿Qué porcentaje cumple?", ["7 ÷ 10 son 70 de cada 100.", "El cumplimiento es 70 %."], "70 %"),
    ],
    mistakes=[("Modificar el registro para que parezca que todo cumple.", "Oculta el problema y mantiene el riesgo.", "Se deja el registro y se agrega la acción correctiva."),
              ("Dar por terminada una acción correctiva sin responsable ni plazo.", "Sin responsable ni plazo no se sabe quién la hace ni cuándo.", "Cada acción lleva responsable y plazo.")],
    T=[
        ("abc", "En Forestal: ¿qué es una no conformidad?", "Un incumplimiento de un requisito", "El cumplimiento de un requisito", "El nombre de un equipo de la faena", "La no conformidad es el incumplimiento, y se corrige con una acción."),
        ("abc", "En Forestal: ¿qué es una acción correctiva?", "Una medida que corrige una no conformidad y evita que se repita", "Una nueva presentación del mismo registro", "Un aviso a las personas ajenas a la faena", "La acción correctiva corrige y previene la repetición."),
        ("abc", "En Forestal: ¿por qué se registran las observaciones aunque nadie se haya lesionado?", "Porque permite corregir los problemas y demostrar que se actuó", "Porque sirve para castigar a quien las cometió", "Porque no se necesita registrar si nadie se lesionó", "Registrar permite corregir causas antes de que ocurra un accidente."),
        ("=", "{F} ¿Qué porcentaje de las observaciones cumple?", "2*100//5", "Se divide las observaciones que cumplen entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas observaciones son no conformidades?", "5-2", "Se restan las observaciones que cumplen al total.", " observaciones"),
        ("abc", "{F} ¿Qué observaciones son no conformidades?", "A, B y E", "C y D", "Solo la A", "A, B y E incumplen un requisito; C y D cumplen."),
        ("=", "{F} ¿Cuántas horas excede el uso del equipo que vibra a lo permitido por la regla interna?", "6-4", "Se resta el máximo permitido a las horas usadas.", " horas"),
        ("abc", "{F} ¿Qué acción correctiva corresponde para la observación A?", "Retirar al operador de la tarea con equipos motorizados hasta renovar su autorización y su capacitación", "Dejarlo seguir con una supervisión informal", "Renovar la autorización por escrito sin capacitación", "Operar con autorización vencida incumple la norma; hay que renovar con capacitación."),
        ("abc", "{F} ¿Qué corresponde frente a la observación B?", "Exigir la protección auditiva y revisar si se puede reducir el ruido con un equipo más silencioso o aislando la fuente", "Retirar el cartel de uso obligatorio de protección auditiva", "Esperar al próximo mes para decidir", "El EPP es obligatorio hoy, pero la jerarquía pide actuar también sobre la fuente."),
        ("abc", "{F} ¿Qué acción correctiva es adecuada para la observación E?", "Reprogramar las tareas y las pausas para que nadie supere el máximo diario", "Aumentar el máximo diario a 6 horas", "Anotar 4 horas en el registro para que cumpla", "Se corrige la organización del trabajo; cambiar el límite o el dato falsea el control."),
        ("abc", "{F} Reprogramar tareas y pausas para limitar la exposición es un control de tipo:", "Administrativo", "De ingeniería", "De EPP", "Es una regla de organización del trabajo, es decir, un control administrativo."),
        ("=", "{F} ¿Cuánto cuesta renovar la autorización y la capacitación de los 3 operadores con la autorización vencida?", "3*50000", "Se multiplican las personas por el costo de cada renovación.", " pesos"),
        ("abc", "{F} Antes de una visita de la autoridad, ¿qué corresponde hacer con las no conformidades?", "Corregirlas y registrar las acciones, sin ocultarlas", "Borrarlas del registro", "No hacer nada, para no llamar la atención", "Ocultar o borrar una no conformidad expone a las personas."),
    ],
    ctx=("abc", "El jefe te pide marcar como «cumple» la observación A en el registro porque «ya lo vamos a renovar». ¿Qué respondes?", "Que el registro debe reflejar lo ocurrido, y que lo consultarás con un adulto responsable", "Que sí, si se renueva esa semana", "Que sí, pero con lápiz", "El registro refleja lo observado; la acción correctiva se anota aparte."),
    sc=[
        ("En Forestal: ¿qué es una no conformidad?", "Un incumplimiento de un requisito", "Es lo que se corrige con una acción."),
        ("¿Qué lleva cada acción correctiva?", "Un responsable y un plazo", "Así se sabe quién la hace y cuándo."),
        ("¿Se puede modificar un registro para que cumpla?", "No, se registra lo ocurrido", "Cambiarlo oculta el problema y mantiene el riesgo para todos."),
    ],
    op=("Ficha de ejemplo: registro de una jornada con 5 observaciones. Cumplen: la zona de exclusión señalizada y la lista de verificación previa completa. No cumplen: un operador con la autorización vencida; una persona sin protección auditiva; un equipo que vibra usado 5 horas con un máximo de 3 horas por día (regla de ejemplo). Renovar una autorización cuesta $40.000 (de ejemplo). Escribe (a) el porcentaje de cumplimiento, (b) cuántas horas se excedió el equipo que vibra, (c) una acción correctiva para el equipo que vibra, (d) el costo de renovar la autorización de 2 operadores.",
        "(a) 2 ÷ 5 = 40 %. (b) 5 − 3 = 2 horas. (c) Reprogramar tareas y pausas para que nadie supere el máximo diario, con responsable y plazo. (d) 2 × 40.000 = 80.000 pesos.",
        ["identifica el cumplimiento", "calcula el exceso de horas", "propone una acción correctiva con sentido", "calcula el costo de renovar"],
        ["hoja con las cuatro respuestas"],
        ["no calcular la proporción", "proponer cambiar el límite", "anotar un dato falso para que cumpla"],
        "Pregunta: «¿qué acción evita que se repita el exceso de horas?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres observaciones de una jornada y clasifica cuáles son no conformidades.",
    extend="Explica con un ejemplo por qué una acción correctiva necesita responsable y plazo.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). Hay que procesar 400 m³ de trozas. Equipo X, herramienta motorizada de mano: rendimiento 2 m³ por hora, costo horario $6.000 (combustible, mantención y operador). "
     "Equipo Y, máquina de mayor tamaño: rendimiento 10 m³ por hora, costo horario $50.000. El plan da una ventana de 60 horas de trabajo. "
     "Si se usan varios equipos X a la vez, cada uno lo maneja una persona autorizada; el equipo Y lo maneja una sola persona autorizada.")
build(
    O8, 4, F,
    use="Aprenderé a calcular en papel el rendimiento, el costo horario, las horas de trabajo y las horas-persona de exposición, y a decidir con costo y seguridad a la vez.",
    prior=["Sé qué es rendimiento y jornada.", "Sé multiplicar y dividir números enteros.", "Sé calcular costos con multiplicaciones."],
    explain=[
        "El rendimiento de un equipo es la cantidad que produce por hora, por ejemplo metros cúbicos por hora. El costo horario es el costo de usar el equipo durante una hora: combustible, mantención, operador y otros gastos. Con ellos se calculan las horas necesarias, que son la cantidad total dividida por el rendimiento, y el costo total, que son las horas por el costo horario. El costo por m³ se obtiene dividiendo el costo horario por el rendimiento.",
        "Las horas-persona de exposición son la suma de las horas que cada persona está expuesta a los peligros del trabajo: si dos personas trabajan 10 horas cada una, son 20 horas-persona. Una alternativa más barata puede exponer a más personas durante más tiempo. Por eso la decisión considera el costo, el plazo y la exposición a la vez, y la toma el responsable con los datos. Los datos de esta clase son de ejemplo.",
        f"Nada de lo que se calcula aquí habilita para operar un equipo. {EMER} {AVISO}",
    ],
    vocab=[("rendimiento", "cantidad que un equipo produce por hora"), ("costo horario", "costo de usar un equipo durante una hora"), ("costo por m³", "costo horario dividido por el rendimiento"), ("horas-persona de exposición", "suma de las horas que cada persona está expuesta a los peligros"), ("ventana de trabajo", "plazo máximo de horas que fija el plan")],
    worked=[
        ("Horas necesarias", "Un equipo de ejemplo rinde 5 m³ por hora y hay que procesar 100 m³. ¿Cuántas horas necesita?", ["Se divide la cantidad entre el rendimiento.", "100 ÷ 5 = 20."], "20 horas"),
        ("Horas-persona", "Tres personas trabajan 8 horas cada una expuestas a un peligro. ¿Cuántas horas-persona de exposición son?", ["Se multiplica el número de personas por las horas de cada una.", "3 × 8 = 24."], "24 horas-persona"),
    ],
    mistakes=[("Decidir solo por el menor costo horario.", "Un equipo de menor costo horario puede costar más por m³ y exponer más tiempo a las personas.", "Compara costo por m³, plazo y exposición."),
              ("Contar solo las horas del equipo y no las de las personas.", "Varias personas expuestas suman más horas-persona.", "Multiplica personas por horas.")],
    T=[
        ("abc", "En Forestal: ¿qué es el rendimiento de un equipo?", "La cantidad que produce por hora", "La cantidad de personas que necesita", "El precio al que fue comprado", "El rendimiento mide producción por tiempo."),
        ("abc", "En Forestal: ¿qué es el costo horario de un equipo?", "El costo de usar el equipo durante una hora", "El precio de compra del equipo", "El sueldo mensual del operador", "El costo horario agrupa los gastos de una hora de uso."),
        ("abc", "En Forestal: ¿qué son las horas-persona de exposición?", "La suma de las horas que cada persona está expuesta a los peligros", "Las horas que el equipo permanece apagado", "Las horas que el taller está abierto", "Cuenta a todas las personas expuestas y el tiempo de cada una."),
        ("=", "{F} ¿Cuántas horas necesita un solo equipo X para procesar los 400 m³?", "400//2", "Se divide la cantidad entre el rendimiento por hora.", " horas"),
        ("=", "{F} ¿Cuántas horas necesitan cuatro equipos X trabajando a la vez?", "400//(2*4)", "Se divide la cantidad entre el rendimiento conjunto de los cuatro equipos.", " horas"),
        ("=", "{F} ¿Cuántas horas necesita el equipo Y para los 400 m³?", "400//10", "Se divide la cantidad entre el rendimiento por hora.", " horas"),
        ("abc", "{F} ¿Qué alternativa cumple la ventana de 60 horas con un solo equipo?", "Solo el equipo Y, que necesita 40 horas", "Solo el equipo X, que necesita 200 horas", "Los dos equipos cumplen la ventana", "Un equipo X necesita 200 horas, que superan las 60; el equipo Y necesita 40."),
        ("=", "{F} ¿Cuánto cuesta procesar los 400 m³ con el equipo X, en total?", "(400//2)*6000", "Se multiplican las horas necesarias por el costo horario.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta procesar los 400 m³ con el equipo Y, en total?", "(400//10)*50000", "Se multiplican las horas necesarias por el costo horario.", " pesos"),
        ("=", "{F} ¿Cuántas horas-persona más de exposición tiene la alternativa de cuatro equipos X que la del equipo Y?", "4*(400//(2*4))-(400//10)", "Se calculan las horas-persona de cada alternativa y se resta.", " horas-persona"),
        ("abc", "{F} ¿Qué conclusión es correcta al comparar X con Y?", "Y cuesta más pero expone a menos horas-persona; la decisión considera ambos criterios y la toma el responsable", "X es mejor, porque siempre debe elegirse el más barato", "Y es mejor, porque es el más caro", "Se compara costo y exposición a la vez; ni el menor costo ni el mayor precio deciden solos."),
        ("=", "{F} Si el costo horario de Y bajara a $40.000, ¿cuánto costaría procesar los 400 m³ con Y?", "(400//10)*40000", "Se multiplican las horas necesarias por el nuevo costo horario.", " pesos"),
        ("abc", "{F} Un jefe propone que una sola persona use el equipo X las 200 horas seguidas «para ahorrar personal». ¿Qué respuesta es correcta?", "No: la exposición se limita con turnos, pausas y personal autorizado", "Sí, si lleva protección auditiva", "Sí, si el trabajo es solo de día", "Superar la exposición permitida pone en riesgo a la persona; el EPP no reemplaza los turnos y las pausas."),
    ],
    ctx=("abc", "Te sugieren comprar un equipo usado «sin manual ni ficha técnica» porque cuesta la mitad. ¿Qué respondes?", "Que no, porque sin manual ni ficha técnica no se conocen usos ni límites, y que lo consultarás con un adulto responsable", "Que sí, porque cuesta la mitad", "Que sí, si el vendedor lo recomienda", "El precio no reemplaza la documentación del fabricante necesaria para usarlo con seguridad."),
    sc=[
        ("En Forestal: ¿cómo se calculan las horas necesarias?", "Dividiendo la cantidad entre el rendimiento", "El rendimiento indica cuánto se hace por hora."),
        ("En el trabajo forestal: ¿cómo se calcula el costo total de una alternativa?", "Horas necesarias por costo horario", "El costo total suma las horas de uso."),
        ("¿Qué se mira además del costo?", "La exposición a los peligros y el plazo", "Una alternativa barata puede exponer más."),
    ],
    op=("Ficha de ejemplo (datos de ejemplo): hay que procesar 300 m³. Equipo A, motorizado de mano: 3 m³ por hora, $5.000 por hora. Equipo B, máquina de mayor tamaño: 15 m³ por hora, $60.000 por hora. Ventana: 40 horas. Cada equipo lo maneja una persona autorizada. Escribe (a) las horas de un equipo A y de un equipo B, (b) cuál cumple la ventana con un solo equipo, (c) el costo total de cada alternativa con un solo equipo, (d) un criterio que no es dinero que revisarías.",
        "(a) A: 300 ÷ 3 = 100 horas; B: 300 ÷ 15 = 20 horas. (b) Solo B, con 20 horas. (c) A: 100 × 5.000 = 500.000 pesos; B: 20 × 60.000 = 1.200.000 pesos. (d) La exposición de las personas a los peligros y el cumplimiento de la autorización y la norma.",
        ["calcula las horas", "compara con la ventana", "calcula los costos totales", "nombra un criterio no económico"],
        ["hoja con las cuatro respuestas"],
        ["no dividir por el rendimiento", "comparar solo costo horario", "olvidar la ventana"],
        "Pregunta: «¿qué pasa con las personas expuestas si el trabajo dura más horas?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un equipo con rendimiento y costo horario y calcula cuánto cuesta procesar 120 m³.",
    extend="Explica con un ejemplo por qué el equipo de menor costo horario no siempre es el más barato en total.",
)

# ============================================================ OAE-08, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas; todos los datos son de ejemplo). Se debe procesar un trabajo de 160 m³. Requisitos mínimos, todos obligatorios: (1) operador con autorización vigente; (2) manual del fabricante disponible; (3) mantención al día; (4) protecciones en su lugar. "
     "Equipo P: cumple los 4 requisitos; costo horario $6.000; rendimiento 2 m³ por hora. Equipo Q: cumple 1, 2 y 4, pero su mantención está vencida; costo horario $9.000; rendimiento 4 m³ por hora. "
     "Equipo R: cumple los 4 requisitos; costo horario $20.000; rendimiento 8 m³ por hora. Parte diario del trabajo de ejemplo: 5 datos obligatorios, de los cuales 4 están presentes; falta «incidentes del día».")
build(
    O8, 5, F,
    use="Aprenderé a comparar equipos con requisitos mínimos y costo por m³, y a verificar la calidad de un parte diario sin dejar datos obligatorios en blanco.",
    prior=["Sé calcular rendimiento y costo horario.", "Sé qué es una lista de verificación.", "Sé calcular porcentajes simples."],
    explain=[
        "Al elegir un equipo se aplican primero los requisitos mínimos, es decir, las condiciones obligatorias que debe cumplir para poder usarse, como la autorización del operador, el manual, la mantención al día y las protecciones en su lugar. Un equipo que no cumple un requisito mínimo queda descartado, aunque sea barato. Entre los que quedan se compara el costo por m³, que es el costo horario dividido por el rendimiento, y el tiempo total, porque un equipo de costo horario alto puede ser más barato por m³.",
        "La calidad del registro se verifica comprobando que el parte diario tenga todos sus datos obligatorios. Si un dato falta, no se deja en blanco ni se inventa: se anota lo realmente ocurrido, incluyendo «ninguno» cuando de verdad no hubo incidentes, pero solo después de verificarlo. Un parte completo permite controlar la producción, los costos y la seguridad.",
        f"La elección final la hace el jefe de faena con el prevencionista. {EMER} {AVISO}",
    ],
    vocab=[("requisito mínimo", "condición obligatoria que un equipo debe cumplir para poder usarse"), ("costo por m³", "costo horario dividido por el rendimiento"), ("parte diario", "registro de lo realizado cada día de trabajo"), ("dato obligatorio", "dato que no puede faltar en un registro"), ("descartar", "dejar fuera una alternativa que incumple un requisito mínimo")],
    worked=[
        ("Descartar por un requisito", "Un equipo de ejemplo no tiene manual del fabricante disponible. ¿Se puede elegir?", ["El manual es un requisito mínimo.", "Si no cumple uno, queda descartado."], "No, queda descartado"),
        ("Costo por m³", "Un equipo de ejemplo tiene un costo horario de $12.000 y rinde 4 m³ por hora. ¿Cuál es su costo por m³?", ["Se divide el costo horario entre el rendimiento.", "12.000 ÷ 4 = 3.000."], "$3.000 por m³"),
    ],
    mistakes=[("Elegir un equipo por su bajo costo aunque incumpla un requisito mínimo.", "Un requisito mínimo no se negocia por precio.", "Descarta los que no cumplen y compara entre los restantes."),
              ("Dejar en blanco un dato obligatorio del parte diario.", "Un parte incompleto no sirve para controlar nada.", "Verifica el dato y anótalo, aunque sea «ninguno».")],
    T=[
        ("abc", "En Forestal: ¿qué es un requisito mínimo para elegir un equipo?", "Una condición obligatoria que debe cumplir para poder usarse", "Una condición deseable pero que se puede omitir", "El precio máximo que se puede pagar", "Un requisito mínimo es obligatorio; no se omite por conveniencia."),
        ("abc", "En Forestal: ¿cómo se calcula el costo por m³ de un equipo?", "Dividiendo el costo horario entre el rendimiento", "Multiplicando el costo horario por el rendimiento", "Restando el rendimiento al costo horario", "El costo por m³ es el costo de una hora repartido entre lo que se produce en una hora."),
        ("abc", "En Forestal: ¿por qué un equipo con la mantención vencida no se elige aunque sea barato?", "Porque incumple un requisito mínimo y aumenta el riesgo de falla", "Porque el precio no importa", "Porque la mantención solo importa al comprar el equipo", "La mantención al día es un requisito obligatorio por seguridad."),
        ("=", "{F} ¿Cuál es el costo por m³ del equipo P?", "6000//2", "Se divide el costo horario entre el rendimiento.", " pesos por m³"),
        ("=", "{F} ¿Cuál es el costo por m³ del equipo Q?", "9000//4", "Se divide el costo horario entre el rendimiento.", " pesos por m³"),
        ("=", "{F} ¿Cuál es el costo por m³ del equipo R?", "20000//8", "Se divide el costo horario entre el rendimiento.", " pesos por m³"),
        ("abc", "{F} ¿Qué equipos pueden elegirse según los requisitos mínimos?", "P y R", "Q y R", "Los tres equipos", "Q incumple el requisito de mantención al día y queda descartado."),
        ("=", "{F} ¿Cuántas horas necesita el equipo P para los 160 m³?", "160//2", "Se divide la cantidad entre el rendimiento por hora.", " horas"),
        ("=", "{F} ¿Cuántas horas necesita el equipo R para los 160 m³?", "160//8", "Se divide la cantidad entre el rendimiento por hora.", " horas"),
        ("=", "{F} ¿Cuántos pesos más cuesta el trabajo completo con P que con R?", "(160//2)*6000-(160//8)*20000", "Se calcula el costo total de cada equipo y se restan.", " pesos"),
        ("abc", "{F} Entre los equipos que cumplen los requisitos, ¿cuál conviene?", "El equipo R, porque tiene menor costo por m³ y menos horas de trabajo", "El equipo P, porque tiene el menor costo horario", "El equipo Q, porque tiene el menor costo por m³", "R cuesta 2.500 por m³ frente a 3.000 de P, y Q ya está descartado."),
        ("=", "{F} ¿Qué porcentaje de los datos obligatorios tiene el parte diario?", "4*100//5", "Se divide los datos presentes entre los obligatorios y se multiplica por 100.", " %"),
        ("abc", "{F} Falta el dato «incidentes del día». ¿Qué corresponde?", "Verificarlo y anotar el incidente real o «ninguno» si de verdad no hubo", "Dejarlo en blanco", "Anotar «ninguno» sin verificar", "Un dato obligatorio se completa con información verificada."),
    ],
    ctx=("abc", "El dueño quiere usar el equipo Q porque «es el más barato por m³», aunque tiene la mantención vencida. ¿Qué respondes?", "Que no se usa un equipo que incumple un requisito mínimo, y que lo consultarás con un adulto responsable", "Que sí, si se hace la mantención la semana siguiente", "Que sí, si el operador es muy cuidadoso", "Un requisito mínimo incumplido descarta el equipo mientras no se corrija."),
    sc=[
        ("En Forestal: ¿qué ocurre con un equipo que incumple un requisito mínimo?", "Queda descartado mientras no lo cumpla", "Los requisitos mínimos son obligatorios y no se negocian por precio."),
        ("¿Cómo se calcula el costo por m³?", "Costo horario dividido por el rendimiento", "Reparte el costo de una hora en lo que se produce."),
        ("¿Se puede dejar un dato obligatorio en blanco?", "No, se verifica y se anota", "Un parte incompleto no sirve para controlar."),
    ],
    op=("Ficha de ejemplo (datos de ejemplo): trabajo de 120 m³. Equipo C: cumple los 4 requisitos mínimos, $4.000 por hora, 2 m³ por hora. Equipo D: no tiene autorización vigente para su operador, $6.000 por hora, 6 m³ por hora. Equipo E: cumple los 4 requisitos, $18.000 por hora, 12 m³ por hora. Escribe (a) el costo por m³ de cada equipo, (b) qué equipos pueden elegirse, (c) cuál conviene y su costo total, (d) qué haces si en un parte diario falta un dato obligatorio.",
        "(a) C: 4.000 ÷ 2 = 2.000; D: 6.000 ÷ 6 = 1.000; E: 18.000 ÷ 12 = 1.500. (b) C y E; D se descarta por no tener autorización vigente. (c) Conviene E: cuesta menos por m³ y termina antes; su costo total es 120 × 1.500 = 180.000 pesos y dura 10 horas, frente a 240.000 pesos y 60 horas de C. (d) Se verifica el dato y se anota lo real, incluso «ninguno» si de verdad no hubo.",
        ["calcula el costo por m³", "descarta el equipo que incumple", "compara con costo y tiempo", "no deja datos en blanco"],
        ["hoja con las cuatro respuestas"],
        ["elegir un equipo descartado por ser barato", "no calcular el costo por m³", "dejar el dato en blanco"],
        "Pregunta: «¿por qué se descarta el equipo D?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres equipos con costo horario y rendimiento y calcula el costo por m³ de cada uno.",
    extend="Explica con un ejemplo por qué un equipo de mayor costo horario puede resultar más barato por m³.",
)
