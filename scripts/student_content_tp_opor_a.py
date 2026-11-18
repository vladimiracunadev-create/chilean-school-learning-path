"""Operaciones Portuarias TP 3.º y 4.º medio: OAE-01 (movilización y distribución de cargas, trámites y cronogramas) y OAE-02 (estiba y desestiba como planilla). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_opor_common import AVISO, EMER, build

O1 = "TP-OPOR-3y4-OAE-01"
O2 = "TP-OPOR-3y4-OAE-02"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). «Terminal Demo» es un terminal portuario ficticio que opera las 24 horas, en turnos de 6 horas con 18 personas por turno. Tiene un sitio de atraque (lugar del muelle donde se ubica una nave), "
     "un patio de contenedores y una bodega. Al recinto ingresan en promedio 14 camiones por hora. Peligros anotados: camiones y vehículos de carga que circulan entre las zonas, cargas suspendidas, el borde del muelle junto al agua y personas que cruzan por las rutas de camiones.")
build(
    O1, 1, F,
    use="Aprenderé qué es el sistema portuario, cómo se mueve y se distribuye la carga, qué es un cronograma y cómo se ordenan las medidas de prevención en un recinto portuario.",
    prior=["Sé leer una ficha escrita y una tabla simple.", "Sé sumar, restar, multiplicar y dividir números enteros.", "Sé que una carga viaja por mar, por tierra o por aire."],
    explain=[
        "El sistema portuario es el conjunto de muelles, terminales, accesos y servicios por donde la carga pasa entre el transporte marítimo y el terrestre. La movilización es el traslado de la carga dentro del recinto, y la distribución es su envío a cada destino. La carga puede ser general (piezas sueltas de formas y tamaños distintos), a granel (sin envase y en grandes cantidades, como los cereales) o en contenedor (caja metálica cerrada de tamaño estándar). Cada actividad se ordena en un cronograma, un calendario con hora de inicio y duración.",
        "En un recinto portuario hay peligros, que son fuentes de daño, y riesgos, que son la posibilidad de que ese daño ocurra. Las medidas de prevención se ordenan en la jerarquía de controles, de la más a la menos efectiva: eliminar el peligro, sustituirlo, aplicar controles de ingeniería (barreras o cambios físicos del lugar), aplicar controles administrativos (letreros, reglas, permisos y capacitación) y, al final, el equipo de protección personal (EPP), que protege solo a quien lo usa y no quita el peligro.",
        f"El trabajo en el puerto se rige por la norma vigente, y la autoridad marítima y portuaria y la Dirección del Trabajo fiscalizan su cumplimiento. {EMER} {AVISO}",
    ],
    vocab=[("sistema portuario", "conjunto de muelles, terminales, accesos y servicios por donde pasa la carga"), ("sitio de atraque", "lugar del muelle donde se ubica una nave"), ("carga a granel", "carga sin envase que se mueve suelta en grandes cantidades"), ("contenedor", "caja metálica cerrada de tamaño estándar para transportar carga"), ("cronograma", "calendario de actividades con hora de inicio y duración"), ("peligro", "fuente con capacidad de causar daño"), ("riesgo", "posibilidad de que un peligro cause daño"), ("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Peligro y riesgo", "En una bodega de ejemplo hay bultos apilados a gran altura junto a un pasillo de paso. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la pila alta de bultos, porque puede causar daño.", "El riesgo es que alguno caiga sobre una persona que pasa por el pasillo."], "Peligro: la pila alta de bultos; riesgo: que caiga sobre una persona"),
        ("Clasificar un control", "Un puerto de ejemplo entrega calzado de seguridad a todo su personal. ¿A qué nivel de la jerarquía corresponde?", ["El calzado se lleva puesto y protege a cada persona.", "Lo que se usa sobre el cuerpo para protegerse es un equipo de protección personal."], "Equipo de protección personal (EPP)"),
    ],
    mistakes=[("Creer que usar casco y chaleco basta para trabajar seguro en cualquier zona del puerto.", "El EPP es la última barrera: no quita el peligro y protege solo a quien lo usa.", "Primero se elimina o se controla el peligro; el EPP se suma a esas medidas."),
              ("Creer que conocer el recinto o haber leído una ficha habilita para operar equipos.", "Las tareas de riesgo exigen autorización, instructor y norma vigente.", "Aprende aquí el concepto y deja la tarea a personal autorizado.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es el sistema portuario?", "El conjunto de muelles, terminales, accesos y servicios por donde la carga pasa entre el transporte marítimo y el terrestre", "La nave que transporta la carga entre dos puertos", "El documento que autoriza la entrada de una carga a un país", "El sistema es el conjunto de instalaciones y servicios; la nave y el documento son solo partes de la operación."),
        ("abc", "En Operaciones Portuarias: ¿qué es la carga a granel?", "Carga sin envase individual que se mueve suelta en grandes cantidades, como cereales o minerales", "Carga ordenada dentro de cajas metálicas cerradas de tamaño estándar", "Carga que viene en piezas sueltas de formas y tamaños distintos, como máquinas o cajones", "El granel va suelto y sin envase; las cajas metálicas son contenedores y las piezas sueltas son carga general."),
        ("abc", "En Operaciones Portuarias: ¿qué es un cronograma?", "Un calendario de actividades con su hora de inicio y su duración", "Una lista de los pesos de cada bulto", "Un registro de los accidentes ocurridos en el mes", "El cronograma ordena las actividades en el tiempo; los pesos y los accidentes se anotan en otros registros."),
        ("abc", "{F} Un letrero que avisa «cruce de camiones» en una de las rutas del recinto es un control de tipo:", "Administrativo, porque informa y ordena una conducta", "De ingeniería, porque cambia físicamente la ruta", "De eliminación, porque quita el cruce", "Un letrero solo informa; no cambia la ruta ni quita el peligro."),
        ("abc", "{F} Personal autorizado instala una reja fija que impide acercarse al borde del muelle fuera de las zonas de trabajo. ¿Qué tipo de control es?", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla de acceso", "De EPP, porque protege a quien camina", "Una reja fija modifica el lugar y no depende de que cada persona la recuerde."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a las personas que cruzan por las rutas de camiones?", "Que un camión atropelle a una persona", "Que los camiones lleguen con retraso al recinto", "Que las rutas del recinto tengan demasiados letreros", "El riesgo es la posibilidad de daño; el retraso y los letreros no son daños a las personas."),
        ("=", "{F} ¿Cuántas personas trabajan en un día completo, sumando todos los turnos de la ficha?", "24//6*18", "Se calcula cuántos turnos de 6 horas hay en 24 horas y se multiplica por las personas de cada turno.", " personas"),
        ("=", "En una inducción de seguridad de ejemplo caben 12 personas por grupo y cada grupo dura 3 horas. Si hay 48 personas por inducir, ¿cuántas horas de inducción se necesitan en total?", "48//12*3", "Se calculan los grupos y se multiplican por las horas de cada grupo.", " horas"),
        ("abc", "{F} Un compañero dice: «conozco bien las zonas del terminal, así que puedo conducir un vehículo de carga sin curso». ¿Qué respuesta es correcta?", "Es falso: conducir exige formación, autorización y norma vigente", "Es cierto, si conduce despacio", "Es cierto, si lleva chaleco reflectante", "Conocer el recinto no habilita para operar vehículos; ir despacio o usar chaleco tampoco."),
        ("abc", "Durante una visita de ejemplo a un terminal, una persona cae al agua junto al muelle. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo ni entrar al agua, avisar a un adulto responsable y a emergencias", "Acercarte al borde para estirarle la mano", "Meterte al agua a ayudarla, porque sabes nadar", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "En Operaciones Portuarias: ¿por qué el EPP es el último nivel de la jerarquía de controles?", "Porque no elimina el peligro y protege solo a quien lo usa; si falla, la persona queda expuesta", "Porque solo se usa de noche, cuando hay menos visibilidad", "Porque su uso es voluntario en las zonas de trabajo", "El EPP no quita el peligro, por eso se usa después de las otras medidas."),
        ("=", "{F} ¿Cuántos camiones ingresan al recinto en un día de operación continua, según el promedio de la ficha?", "14*24", "Se multiplican los camiones por hora por las 24 horas del día.", " camiones"),
        ("abc", "{F} Para reducir el riesgo de atropello, ¿cuál medida es de nivel más efectivo en la jerarquía de controles?", "Rediseñar el recinto para que ninguna ruta de personas cruce una ruta de camiones", "Poner un cartel de velocidad máxima en cada ruta", "Entregar un chaleco reflectante a cada persona", "Eliminar el cruce quita el peligro; el cartel es administrativo y el chaleco es EPP."),
    ],
    ctx=("abc", "Un conocido que trabaja en un puerto te propone acompañarlo al muelle a «dar una mano» con unas cargas porque «es fácil y rápido». ¿Qué respondes?", "Que no, porque trabajar en un muelle exige instructor autorizado, norma vigente y elementos de protección, y que lo consultarás con un adulto responsable", "Que sí, si te presta un casco", "Que sí, pero solo cerca de la entrada del muelle", "Un casco o la cercanía a la entrada no reemplazan la autorización ni la formación."),
    sc=[
        ("En Operaciones Portuarias: ¿qué es un riesgo?", "La posibilidad de que un peligro cause daño", "El riesgo es la posibilidad de daño; el peligro es la fuente."),
        ("En el puerto: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
        ("¿Qué es un sitio de atraque?", "El lugar del muelle donde se ubica una nave", "Es la posición del muelle que se destina a la nave."),
    ],
    op=("En el patio de «Terminal Demo» (caso de ejemplo) una ruta de camiones cruza sin separación el camino que usa el personal de oficina para ir al comedor. Peligros anotados: camiones en movimiento y poca visibilidad en la esquina. Escribe (a) cuál es el peligro y cuál el riesgo asociado, (b) un control administrativo para ese cruce, (c) un control de ingeniería para el mismo cruce, (d) por qué el EPP no basta.",
        "(a) Peligro: los camiones que circulan por la ruta que cruza el camino del personal; riesgo: que un camión atropelle a una persona. (b) Un letrero de cruce y un horario o una regla de circulación para el personal. (c) Una barrera fija que separe el camino peatonal de la ruta de camiones. (d) Porque el EPP es la última barrera: no quita el peligro y protege solo a quien lo usa. La tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "no aclarar que la tarea la hace personal autorizado"],
        "Pregunta: «¿qué control cambia el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el nivel de ingeniería."),
    reinforce="Escribe la jerarquía de controles en orden y pon junto a cada nivel un ejemplo inventado de un terminal portuario.",
    extend="Explica con un ejemplo por qué un cronograma bien hecho también ayuda a prevenir accidentes en un recinto portuario.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (documentos descritos por escrito, de ejemplo, inventados). Conocimiento de embarque CE-1021: embarcador «Exportadora Demo»; consignatario «Importadora Ejemplo»; mercancía: 120 bultos de repuestos; "
     "puerto de carga «Puerto A»; puerto de descarga «Puerto B» (puertos ficticios). Lista de embalaje del mismo embarque: caja tipo 1, 80 cajas (cada caja es un bulto) de 25 kg cada una; caja tipo 2, 40 cajas (cada caja es un bulto) de 40 kg cada una. "
     "Manifiesto de la «Nave Demo»: reúne 5 conocimientos de embarque, que suman 640 bultos.")
build(
    O1, 2, F,
    use="Aprenderé qué documentos acompañan a la carga, qué dato aporta cada uno, qué roles intervienen y cómo se detectan diferencias entre documentos.",
    prior=["Sé leer una lista con cantidades y pesos.", "Sé sumar y multiplicar números enteros.", "Sé qué es un cronograma."],
    explain=[
        "La carga viaja acompañada de documentos. El conocimiento de embarque lo emite el transportista: acredita que recibió la carga y registra quién la envía, quién la recibe, qué es y por dónde viaja. La lista de embalaje detalla el contenido, la cantidad y el peso de cada tipo de bulto. El manifiesto de carga reúne todos los conocimientos de embarque que lleva una nave. Un documento no reemplaza a otro: se usan juntos para verificar la carga.",
        "Cada rol tiene su función. El embarcador entrega la carga para que sea transportada. El consignatario es quien la recibe en destino. El agente de naves representa a la nave y a su empresa ante el puerto. El tarjador cuenta y registra los bultos que pasan por una zona de control. Si lo contado no coincide con el documento hay una diferencia: un faltante si hay menos bultos que los declarados, y un sobrante si hay más. Se registra por escrito y se informa a quien emitió el documento.",
        f"Un documento ya emitido no se cambia a mano para que cuadre: lo corrige quien lo emitió. Las reglas de cada documento dependen de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("conocimiento de embarque", "documento del transportista que acredita que recibió la carga y registra su viaje"), ("lista de embalaje", "documento que detalla contenido, cantidad y peso de cada tipo de bulto"), ("manifiesto de carga", "lista de los conocimientos de embarque que lleva una nave"), ("embarcador", "quien entrega la carga para ser transportada"), ("consignatario", "quien recibe la carga en destino"), ("agente de naves", "representante de la nave y su empresa ante el puerto"), ("tarjador", "persona que cuenta y registra los bultos"), ("faltante y sobrante", "menos o más bultos que los declarados en el documento")],
    worked=[
        ("Sumar un manifiesto", "Un manifiesto de ejemplo reúne tres conocimientos de embarque con 200, 150 y 90 bultos. ¿Cuántos bultos declara el manifiesto?", ["Cada conocimiento declara una parte de la carga de la nave.", "Se suman 200, 150 y 90."], "440 bultos"),
        ("Identificar un rol", "«Comercial Ficticia» recibe en destino la mercancía que figura a su nombre en un conocimiento de embarque. ¿Qué rol cumple?", ["Quien recibe la carga en destino es el consignatario.", "El nombre figura en el conocimiento como receptor."], "Consignatario"),
    ],
    mistakes=[("Creer que el manifiesto, el conocimiento y la lista de embalaje son el mismo documento.", "Cada uno cumple una función distinta y se usan juntos para verificar la carga.", "Anota para qué sirve cada documento antes de revisarlos."),
              ("Corregir a mano un documento ya emitido para que cuadre con lo contado.", "Solo quien emitió el documento puede corregirlo, y la diferencia debe quedar registrada.", "Registra la diferencia y avisa a quien emitió el documento.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es un conocimiento de embarque?", "El documento del transportista que acredita que recibió la carga y registra quién la envía, quién la recibe y su viaje", "La lista de las personas que trabajan en el turno de una nave", "El plano que muestra dónde se guarda la carga en la bodega", "El conocimiento es el documento del transportista; los turnos y los planos son otros registros."),
        ("abc", "En Operaciones Portuarias: ¿qué es el manifiesto de carga de una nave?", "La lista de los conocimientos de embarque que lleva esa nave", "La lista de embalaje de un solo bulto", "El permiso para que la nave atraque en el muelle", "El manifiesto reúne la carga de toda la nave; la lista de embalaje se refiere a un embarque."),
        ("abc", "En Operaciones Portuarias: ¿quién es el consignatario?", "Quien recibe la carga en destino", "Quien entrega la carga para ser transportada", "Quien cuenta los bultos en la zona de control", "El consignatario es el receptor; el que entrega es el embarcador y el que cuenta es el tarjador."),
        ("abc", "{F} ¿Qué rol cumple «Exportadora Demo» en el embarque de la ficha?", "Embarcador, porque entrega la carga para que sea transportada", "Consignatario, porque la recibe en destino", "Agente de naves, porque representa a la nave", "Según el conocimiento, Exportadora Demo es quien envía la carga."),
        ("abc", "{F} ¿Qué documento de la ficha detalla cuántas unidades hay de cada tipo de caja y cuánto pesa cada una?", "La lista de embalaje", "El conocimiento de embarque", "El manifiesto de la nave", "La lista de embalaje detalla tipos de caja y pesos; el conocimiento solo declara el total de bultos."),
        ("abc", "En Operaciones Portuarias: ¿qué rol cuenta y registra los bultos que pasan por una zona de control?", "El tarjador", "El consignatario", "El agente de naves", "El tarjador cuenta y registra; el consignatario recibe y el agente representa a la nave."),
        ("=", "{F} ¿Cuántos kilogramos pesan en total las cajas de la lista de embalaje?", "80*25+40*40", "Se multiplican las unidades de cada tipo por su peso y se suman los dos resultados.", " kg"),
        ("=", "{F} Sin contar el conocimiento CE-1021, ¿cuántos bultos suman los otros conocimientos del manifiesto?", "640-120", "Al total del manifiesto se le restan los bultos del conocimiento CE-1021.", " bultos"),
        ("abc", "{F} ¿Coinciden los bultos de la lista de embalaje con los del conocimiento de embarque?", "Sí, ambos documentos suman 120 bultos", "No, la lista suma 100 bultos", "No, la lista suma 140 bultos", "La lista suma 80 + 40 = 120 bultos, igual que el conocimiento."),
        ("abc", "{F} Al descargar, un tarjador de ejemplo cuenta 118 bultos del conocimiento CE-1021. ¿Cómo se llama la diferencia y qué corresponde?", "Faltante de 2 bultos, que se registra por escrito y se informa a quien corresponde", "Sobrante de 2 bultos, que se registra por escrito y se informa a quien corresponde", "No hay diferencia, porque el manifiesto manda sobre el conocimiento y no hay que registrar nada", "Hay 2 bultos menos que los declarados: es un faltante y se registra."),
        ("abc", "En Operaciones Portuarias: ¿por qué conviene que la lista de embalaje y el conocimiento de embarque declaren la misma cantidad de bultos?", "Porque así la carga se verifica contra ambos documentos y se evitan reclamos y retrasos", "Porque la lista de embalaje reemplaza al conocimiento cuando se parecen", "Porque el manifiesto de la nave no admite diferencias menores a 10 bultos", "Los documentos se usan para verificarse entre sí; si no coinciden hay que investigar."),
        ("=", "{F} ¿Cuántos kilogramos pesa en promedio un bulto del embarque, dividiendo el peso total de la lista de embalaje entre los bultos del conocimiento?", "(80*25+40*40)//120", "Se calcula el peso total de la lista y se divide entre los bultos declarados.", " kg"),
        ("abc", "Un cliente de ejemplo pide cambiar a mano la cantidad de un conocimiento ya emitido para que cuadre con lo contado. ¿Qué corresponde?", "Registrar la diferencia y consultar a quien emitió el documento", "Cambiarlo a mano si el cliente lo pide con su firma", "Anotar la cantidad contada en el manifiesto y dejar el conocimiento como está, sin avisar", "Un documento emitido lo corrige quien lo emitió, y la diferencia queda registrada."),
    ],
    ctx=("abc", "En un turno de ejemplo, una persona de la oficina te dice: «el conocimiento dice 50 bultos y llegaron 47, pero anota 50 para que no haya problemas». Como persona en formación, ¿qué respondes?", "Que se debe registrar lo contado, informar el faltante y no alterar el registro", "Que anotas 50, porque la oficina decide", "Que anotas 50 en lápiz para poder borrarlo después", "Alterar un registro oculta un faltante real; lo correcto es dejar constancia y avisar."),
    sc=[
        ("En Operaciones Portuarias: ¿qué documento reúne todos los conocimientos de embarque de una nave?", "El manifiesto de carga", "El manifiesto agrupa todos los conocimientos de embarque de la nave."),
        ("¿Qué es un sobrante?", "Que hay más bultos que los declarados en el documento", "El sobrante es un exceso de bultos respecto de lo declarado."),
        ("¿Quién emite el conocimiento de embarque?", "El transportista", "El conocimiento acredita que el transportista recibió la carga."),
    ],
    op=("Documentos de ejemplo: el conocimiento CE-2040 declara 60 bultos de textiles. La lista de embalaje del mismo embarque dice: caja tipo 1, 30 unidades de 12 kg cada una; caja tipo 2, 24 unidades de 10 kg cada una. Escribe (a) cuántos bultos suma la lista, (b) cuántos kilogramos pesa en total, (c) si coincide con el conocimiento y cuál es la diferencia, (d) qué se hace con esa diferencia.",
        "(a) 30 + 24 = 54 bultos. (b) 30 × 12 + 24 × 10 = 360 + 240 = 600 kg. (c) No coincide: el conocimiento declara 60 y la lista suma 54, es decir, faltan 6 bultos en la lista. (d) Se registra la diferencia por escrito y se informa a quien emitió los documentos, sin corregirlos a mano.",
        ["suma bien los bultos", "calcula el peso total", "compara y nombra la diferencia", "indica que se registra y se informa"],
        ["hoja con las cuatro respuestas"],
        ["sumar los bultos sin multiplicar los pesos por las unidades", "corregir un documento a mano", "no registrar la diferencia"],
        "Pregunta: «¿quién puede corregir un documento emitido?». Si no responde, pídele que relea el último párrafo de la explicación."),
    reinforce="Inventa un manifiesto con tres conocimientos de embarque y súmalos.",
    extend="Explica con un ejemplo la diferencia entre un faltante y un sobrante y a quién se informa.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (cronograma de ejemplo, inventado). La «Nave Demo» atraca a las 6 horas en Terminal Demo; las horas van en formato de 24 horas. Actividad A, recepción de documentos: inicio 6, dura 2 horas. "
     "B, descarga de contenedores al patio: inicio 8, dura 8 horas. C, control de bultos: inicio 9, dura 7 horas, en paralelo con B. D, despacho de camiones: comienza cuando terminan B y C, dura 3 horas. "
     "E, cierre de documentos: comienza al terminar D, dura 2 horas. Ritmo del despacho: 18 camiones por hora.")
build(
    O1, 3, F,
    use="Aprenderé a leer un cronograma de una operación portuaria, a calcular horas de término y desfases y a decidir qué hacer cuando una actividad se atrasa.",
    prior=["Sé sumar y restar horas enteras.", "Sé qué es un cronograma.", "Sé que una nave llega a un muelle y su carga se descarga."],
    explain=[
        "Un cronograma ordena las actividades de una operación con su hora de inicio y su duración. La hora de término es la hora de inicio más la duración. Una actividad predecesora es la que debe terminar antes de que otra pueda comenzar, y la siguiente se llama sucesora. Dos actividades son paralelas cuando se hacen en un mismo período, con horarios que se cruzan.",
        "Si una actividad se atrasa, aparece un desfase: la diferencia entre la hora real y la hora programada. El atraso se traslada a las sucesoras que dependen de ella. Lo correcto es registrar la hora real, avisar a las áreas afectadas y reprogramar. No se acortan controles ni se anota la hora programada como si se hubiera cumplido: eso oculta el problema y puede causar errores o accidentes.",
        f"Los cronogramas se fijan según la planificación general y la norma vigente de cada área. {EMER} {AVISO}",
    ],
    vocab=[("hora de término", "hora de inicio más la duración"), ("actividad predecesora", "la que debe terminar antes de que otra pueda comenzar"), ("actividad sucesora", "la que empieza cuando termina su predecesora"), ("actividades paralelas", "las que se hacen en un mismo período, con horarios que se cruzan"), ("desfase", "diferencia entre la hora real y la programada"), ("reprogramar", "fijar de nuevo los horarios de las actividades siguientes")],
    worked=[
        ("Hora de término", "Una actividad de ejemplo empieza a las 10 y dura 5 horas. ¿A qué hora termina?", ["La hora de término es la hora de inicio más la duración.", "10 más 5 son 15."], "A las 15 horas"),
        ("Calcular un desfase", "Una actividad de ejemplo estaba programada para terminar a las 14 y terminó a las 17. ¿Cuál es el desfase?", ["El desfase es la hora real menos la hora programada.", "17 menos 14 son 3."], "3 horas de atraso"),
    ],
    mistakes=[("Contar mal las horas de actividades paralelas, sumando sus duraciones como si fueran una tras otra.", "Las actividades paralelas ocurren al mismo tiempo: pesa la que termina más tarde.", "Dibuja una línea de tiempo y marca dónde se cruzan."),
              ("Anotar la hora programada en vez de la real cuando hay un atraso.", "El registro debe reflejar lo ocurrido; si no, nadie puede reprogramar ni investigar.", "Anota la hora real y avisa el desfase a las áreas siguientes.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es una actividad predecesora en un cronograma?", "La que debe terminar antes de que otra pueda comenzar", "La que aparece al final de la lista", "La que dura más horas que las demás", "Predecesora es la que condiciona a otra; su lugar en la lista o su duración no la definen."),
        ("abc", "En Operaciones Portuarias: ¿qué es el desfase en un cronograma?", "La diferencia entre la hora real y la hora programada de una actividad", "El tiempo que dura una actividad sin interrupciones", "La cantidad de personas asignadas a cada actividad", "El desfase mide la diferencia entre lo real y lo programado."),
        ("abc", "En Operaciones Portuarias: ¿qué significa que dos actividades sean paralelas?", "Que se hacen en un mismo período, con horarios que se cruzan", "Que una empieza solo cuando la otra termina", "Que ambas las hace la misma persona", "Paralelas son las que ocurren al mismo tiempo."),
        ("abc", "{F} ¿Qué dos actividades de la ficha son paralelas?", "B (descarga) y C (control de bultos)", "A (recepción) y B (descarga)", "D (despacho) y E (cierre)", "B va de 8 a 16 y C de 9 a 16, así que se cruzan; A termina cuando B comienza."),
        ("=", "{F} Si no hay atrasos, ¿a qué hora puede comenzar el despacho D como más temprano?", "8+8", "D espera a que terminen B y C; B termina a las 8 + 8 y C a las 9 + 7, ambas a la misma hora.", " horas"),
        ("abc", "{F} ¿Cuál es la actividad de mayor duración de la ficha?", "B, que dura 8 horas", "C, que dura 7 horas", "D, que dura 3 horas", "Comparando las duraciones, la descarga B es la más larga."),
        ("=", "{F} Si no hay atrasos, ¿cuántas horas pasan desde el inicio de A hasta el término de E?", "(8+8+3+2)-6", "E termina a la hora de inicio de D más 3 y más 2; se resta la hora de inicio de A.", " horas"),
        ("=", "{F} B se atrasa y termina 2 horas más tarde que lo programado, mientras C termina a su hora. ¿A qué hora termina E?", "(8+8+2)+3+2", "D comienza cuando termina B atrasada; a esa hora se suman las 3 horas de D y las 2 de E.", " horas"),
        ("=", "{F} Con el ritmo de despacho de la ficha, ¿cuántas horas toma despachar 72 camiones?", "72//18", "Se divide el total de camiones entre los que salen por hora.", " horas"),
        ("abc", "{F} Un jefe propone iniciar D a las 15 «para ganar tiempo». ¿Qué problema tiene la propuesta?", "D debe esperar a B y C, que terminan a las 16; despachar antes sacaría carga aún sin descargar ni controlar", "D no puede empezar antes de las 16 porque a esa hora llegan los camiones", "Ninguno: D solo depende de A, que ya terminó", "D es sucesora de B y C, no de A; empezar antes rompe el orden del cronograma."),
        ("abc", "En Operaciones Portuarias: ¿por qué se registra el desfase cuando una actividad se atrasa?", "Para avisar a las áreas siguientes y reprogramar, dejando constancia de la hora real", "Para anotar en el cronograma la hora programada como si se hubiera cumplido", "Para que la actividad atrasada se apure acortando sus controles", "Registrar la hora real permite reprogramar sin ocultar el problema."),
        ("=", "{F} ¿Cuántas horas se ahorran por hacer B y C en paralelo, comparado con hacer A, B, C, D y E una tras otra, sin esperas?", "(2+8+7+3+2)-((8+8+3+2)-6)", "Se suman todas las duraciones y se resta el tiempo real del cronograma con B y C en paralelo.", " horas"),
        ("abc", "{F} B se atrasa 2 horas. ¿Qué medida de planificación es válida?", "Reprogramar las actividades siguientes y avisar el nuevo horario a las áreas afectadas", "Acortar el control de bultos para recuperar las 2 horas", "Anotar en el registro la hora programada en lugar de la hora real", "Reprogramar es legítimo; recortar controles o falsear horas oculta el problema."),
    ],
    ctx=("abc", "En un turno de ejemplo, la jefatura te pide anotar que la descarga terminó a las 16, aunque terminó a las 18, «para que no haya reclamos». Como persona en formación, ¿qué respondes?", "Que el registro debe decir la hora real y que el atraso se informa a quien corresponde", "Que lo anotas, porque la jefatura manda", "Que lo anotas en lápiz para borrarlo si hay reclamo", "Un registro falso impide reprogramar y puede ocultar causas del atraso."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calcula la hora de término de una actividad?", "Sumando la duración a la hora de inicio", "La hora de término se obtiene sumando la duración al inicio."),
        ("¿Qué es un desfase?", "La diferencia entre la hora real y la programada", "Mide el atraso o el adelanto respecto de lo que estaba previsto."),
        ("¿Qué hacer cuando una actividad se atrasa?", "Registrar la hora real, avisar y reprogramar", "Se informa el desfase para que las áreas siguientes ajusten su trabajo."),
    ],
    op=("Cronograma de ejemplo: P, inicio 7, dura 3 horas. Q, inicio 7, dura 5 horas, en paralelo con P. R comienza cuando terminan P y Q y dura 2 horas. Escribe (a) a qué hora termina P y a qué hora termina Q, (b) a qué hora comienza y termina R, (c) a qué hora termina R si Q se atrasa 2 horas, (d) qué se hace con el atraso.",
        "(a) P termina a las 10 y Q a las 12. (b) R comienza a las 12 y termina a las 14. (c) Q termina a las 14, R comienza a las 14 y termina a las 16. (d) Se registra la hora real, se informa el desfase a las áreas afectadas y se reprograman las actividades siguientes.",
        ["calcula bien las horas de término", "reconoce que R depende de P y Q", "calcula el efecto del atraso", "indica registrar, avisar y reprogramar"],
        ["hoja con las cuatro respuestas"],
        ["sumar las duraciones de P y Q", "comenzar R antes de que termine Q", "no mencionar el registro del atraso"],
        "Pregunta: «¿qué actividad hace esperar a R?». Si no responde, pídele que relea la definición de predecesora."),
    reinforce="Inventa un cronograma de tres actividades con inicio y duración y calcula la hora de término de cada una.",
    extend="Explica con un ejemplo por qué dos actividades paralelas no suman sus duraciones.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (caso de ejemplo, inventado). Terminal Demo debe repartir 960 bultos entre tres destinos internos: bodega A (capacidad de ejemplo: 400 bultos), bodega B (300 bultos) y el patio (400 bultos). "
     "El traslado se hace con 4 camiones internos de ejemplo: cada uno lleva 20 bultos por viaje y cada viaje, de ida y vuelta, dura 15 minutos. El turno dura 6 horas.")
build(
    O1, 4, F,
    use="Aprenderé a repartir una carga entre destinos respetando sus capacidades y a calcular viajes, rendimiento y tiempos para cumplir un cronograma.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé pasar minutos a horas.", "Sé leer un cronograma sencillo."],
    explain=[
        "Para distribuir una carga hay que respetar la capacidad de cada destino, que es la cantidad máxima de bultos que puede recibir. Una distribución es válida si ningún destino supera su capacidad y si la suma de lo asignado es igual al total del lote: no deben quedar bultos sin destino ni destinos con bultos que no existen.",
        "El rendimiento es la cantidad de carga que se mueve en una unidad de tiempo. El tiempo de ciclo es lo que tarda un camión interno en completar un viaje de ida y vuelta. El número de viajes es el total de bultos dividido entre los bultos que lleva cada camión por viaje; si se reparte entre varios camiones, cada uno hace una parte de esos viajes, y su tiempo de trabajo es el número de viajes por el tiempo de ciclo.",
        f"Todos los datos de capacidades, camiones y tiempos de esta clase son de ejemplo; los reales dependen del puerto y de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("capacidad", "cantidad máxima de bultos que un destino puede recibir"), ("distribución válida", "reparto que no supera la capacidad de ningún destino y suma el total del lote"), ("rendimiento", "cantidad de carga que se mueve en una unidad de tiempo"), ("tiempo de ciclo", "tiempo de un viaje de ida y vuelta de un camión interno"), ("lote", "conjunto de bultos que se mueve en una misma operación")],
    worked=[
        ("Contar viajes", "Un lote de ejemplo tiene 600 bultos y cada camión lleva 25 por viaje. Se usan 3 camiones. ¿Cuántos viajes hace cada uno?", ["Viajes totales: 600 dividido en 25 son 24.", "Entre 3 camiones, cada uno hace 24 dividido en 3, o sea 8."], "8 viajes por camión"),
        ("Validar una distribución", "Capacidades de ejemplo: bodega X, 200 bultos; bodega Y, 150. Se proponen 120 para X y 160 para Y. ¿Es válida?", ["X recibe 120, que no supera 200.", "Y recibe 160, que supera su capacidad de 150."], "No es válida: Y excede su capacidad"),
    ],
    mistakes=[("Repartir el lote en partes iguales sin mirar la capacidad de cada destino.", "Un destino pequeño puede quedar sobrepasado aunque la suma sea correcta.", "Compara cada cantidad asignada con la capacidad del destino."),
              ("Olvidar que el tiempo de ciclo es de ida y vuelta y usar solo el tiempo de ida.", "El camión no queda disponible hasta volver.", "Usa el tiempo del viaje completo en el cálculo.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es el rendimiento de una operación?", "La cantidad de carga que se mueve en una unidad de tiempo, por ejemplo, bultos por hora", "El dinero que cuesta mover cada bulto", "El tiempo total que dura el turno de trabajo", "El rendimiento mide carga por tiempo; el costo y la duración del turno son otros datos."),
        ("abc", "En Operaciones Portuarias: ¿qué es la capacidad de una bodega al planificar la distribución?", "La cantidad máxima de bultos que puede recibir", "La cantidad de bultos que hay hoy en ella", "El número de personas que pueden entrar a ella", "La capacidad es un máximo; lo que hay hoy es la ocupación."),
        ("abc", "En Operaciones Portuarias: ¿qué es el tiempo de ciclo de un camión interno?", "El tiempo que tarda en completar un viaje de ida y vuelta", "El tiempo que el camión está estacionado en el patio", "El tiempo que dura el turno completo", "El ciclo incluye ida y regreso; el estacionamiento o el turno son otros tiempos."),
        ("abc", "{F} Se propone asignar 420 bultos a la bodega A, 300 a la bodega B y 240 al patio. ¿Es válida la distribución?", "No, porque la bodega A superaría su capacidad de 400 bultos", "Sí, porque los tres destinos suman 960 bultos", "No, porque cada destino debe recibir la misma cantidad", "Aunque la suma sea 960, A recibiría más de lo que admite."),
        ("abc", "{F} ¿Cuál distribución respeta las capacidades y reparte los 960 bultos?", "Bodega A: 400; bodega B: 260; patio: 300", "Bodega A: 400; bodega B: 300; patio: 300", "Bodega A: 350; bodega B: 320; patio: 290", "La primera suma 960 y no excede ningún destino; la segunda suma 1.000 y la tercera supera a la bodega B."),
        ("abc", "{F} ¿Qué datos de la ficha se usan para calcular cuántos viajes se necesitan en total?", "Los bultos totales y los bultos que lleva cada camión por viaje", "La duración del turno y la capacidad de las bodegas", "La capacidad del patio y el número de camiones", "Los viajes salen de dividir el total de bultos entre la carga de cada viaje."),
        ("=", "{F} ¿Cuántos viajes se necesitan en total para trasladar los 960 bultos?", "960//20", "Se divide el total de bultos entre los que lleva un camión por viaje.", " viajes"),
        ("=", "{F} Con los 4 camiones de la ficha, ¿cuántas horas trabaja cada uno para trasladar los 960 bultos?", "960//20//4*15//60", "Se calculan los viajes, se reparten entre los camiones, se multiplican por el ciclo en minutos y se pasan a horas.", " horas"),
        ("=", "Otro lote de ejemplo tiene 840 bultos, se usan 6 camiones que llevan 28 bultos por viaje y cada viaje dura 20 minutos. ¿Cuántos minutos trabaja cada camión?", "840//28//6*20", "Se calculan los viajes totales, los de cada camión y se multiplican por el ciclo.", " minutos"),
        ("abc", "{F} Un camión sale de servicio y quedan 3. ¿La operación sigue cabiendo en el turno de 6 horas?", "Sí, porque cada camión necesitaría 4 horas", "No, porque con menos camiones la operación nunca termina", "Sí, porque los camiones restantes trabajan más rápido", "Con 3 camiones cada uno hace 16 viajes de 15 minutos, 240 minutos, menos que las 6 horas."),
        ("abc", "En Operaciones Portuarias: ¿por qué conviene comprobar que la suma de la distribución sea igual al total del lote?", "Para que no queden bultos sin destino ni destinos con bultos que no existen", "Para que todos los destinos reciban la misma cantidad", "Para que los camiones hagan siempre el mismo número de viajes", "La suma debe cerrar con el lote; el reparto no tiene por qué ser igual."),
        ("=", "{F} Con el reparto bodega A 380, bodega B 280 y patio 300, ¿cuántos bultos de capacidad libre quedan en total?", "(400+300+400)-(380+280+300)", "Se resta lo asignado a la capacidad total de los tres destinos.", " bultos"),
        ("abc", "{F} El turno exige terminar el traslado en 2 horas como máximo, con camiones de las mismas características. ¿Cuántos camiones se necesitan como mínimo?", "6 camiones, porque cada uno hace 8 viajes en 2 horas y se necesitan 48", "4 camiones, porque ya alcanzan en 3 horas", "8 camiones, porque cada uno haría solo 6 viajes", "En 2 horas, 120 minutos, cada camión hace 8 viajes de 15 minutos; 48 viajes entre 8 son 6."),
    ],
    ctx=("abc", "En una práctica de ejemplo, un compañero propone repartir el lote «un poco más de lo que cabe» en la bodega pequeña, «porque después se acomoda». ¿Qué respondes?", "Que no se puede superar la capacidad y que hay que repartir el exceso a otro destino o consultar a la jefatura", "Que sí, si el exceso es solo de algunos bultos", "Que sí, porque la bodega después se amplía", "La capacidad es un límite del destino; superarla genera riesgo y desorden."),
    sc=[
        ("En Operaciones Portuarias: ¿cuándo es válida una distribución?", "Cuando ningún destino supera su capacidad y la suma es el total del lote", "Debe cumplir la capacidad de cada destino y el total."),
        ("¿Cómo se calculan los viajes totales?", "Dividiendo los bultos totales entre los bultos por viaje", "Cada viaje lleva una cantidad fija de bultos, por eso se divide."),
        ("¿Qué es el tiempo de ciclo?", "El tiempo de un viaje de ida y vuelta", "El camión queda disponible para otro viaje solo al regresar."),
    ],
    op=("Terminal Demo debe repartir 500 bultos entre la bodega M (capacidad de ejemplo: 300 bultos) y la bodega N (capacidad de ejemplo: 250 bultos). Se usan 5 camiones internos de ejemplo que llevan 20 bultos por viaje; cada viaje de ida y vuelta dura 12 minutos. Escribe (a) una distribución válida, (b) cuántos viajes se necesitan en total, (c) cuántos viajes hace cada camión, (d) cuántos minutos trabaja cada camión.",
        "(a) Por ejemplo, bodega M: 300 y bodega N: 200 (suman 500 y no superan las capacidades). (b) 500 ÷ 20 = 25 viajes. (c) 25 ÷ 5 = 5 viajes por camión. (d) 5 × 12 = 60 minutos.",
        ["propone una distribución que suma 500 y respeta capacidades", "calcula bien los viajes totales", "reparte los viajes entre los camiones", "calcula los minutos de cada camión"],
        ["hoja con las cuatro respuestas"],
        ["superar la capacidad de una bodega", "no sumar el total del lote", "usar solo el tiempo de ida"],
        "Pregunta: «¿la suma de tu reparto es 500?». Si no responde, pídele que sume y compare con las capacidades."),
    reinforce="Inventa un lote con tres destinos y sus capacidades, y escribe una distribución válida y una inválida.",
    extend="Explica con un ejemplo por qué no basta mirar el tiempo de ida para calcular cuánto trabaja un camión.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Terminal Demo debe despachar 720 bultos con camiones internos de ejemplo que llevan 24 bultos por viaje; cada viaje, de ida y vuelta, dura 20 minutos. "
     "Plan P: 5 camiones. Plan Q: 2 camiones. Cada camión cuesta $35.000 por turno, sin importar las horas que trabaje (precio de ejemplo). El plazo de la operación es de 6 horas. "
     "Al terminar se concilian los registros: la guía de salida informa 720 bultos y el recibo del destino informa 717.")
build(
    O1, 5, F,
    use="Aprenderé a comparar dos planes de movilización por costo y plazo, a verificar la calidad con una lista de verificación y a conciliar los registros de salida y recepción.",
    prior=["Sé calcular viajes, rendimiento y tiempo de ciclo.", "Sé comparar dos cantidades de dinero.", "Sé qué es un faltante."],
    explain=[
        "Para elegir entre dos planes se comparan los mismos datos: el plazo exigido, el tiempo que toma cada plan y su costo. Un plan sirve si cumple el plazo; entre los que cumplen, conviene el de menor costo. Terminar antes no siempre es mejor: cuenta también lo que cuesta, y un plan más rápido que el plazo exigido puede costar más sin necesidad.",
        "La calidad de una operación se verifica con una lista de verificación: una lista de puntos que se revisan uno por uno antes de dar la tarea por terminada. Una parte clave es conciliar los registros, es decir, comparar dos registros de la misma carga, como la guía de salida y el recibo del destino, y explicar las diferencias. El principio de cero faltas es la meta de que ningún documento o dato salga con errores u omisiones.",
        f"Si hay una diferencia, por ejemplo un faltante, se registra por escrito y se informa a quien corresponde; no se cambia un registro para que cuadre. Los precios y tiempos de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("plazo", "tiempo máximo permitido para terminar una operación"), ("conciliar", "comparar dos registros de la misma carga y explicar las diferencias"), ("lista de verificación", "lista de puntos que se revisan uno por uno antes de cerrar una tarea"), ("cero faltas", "meta de que ningún documento o dato salga con errores u omisiones"), ("faltante", "menos bultos que los declarados")],
    worked=[
        ("Comparar dos planes", "Un lote de ejemplo de 480 bultos se despacha en camiones de 20 bultos por viaje y 15 minutos por viaje. Plan X: 4 camiones, $30.000 cada uno. Plan Y: 6 camiones, $30.000 cada uno. El plazo es de 2 horas. ¿Qué plan conviene?", ["Los viajes son 480 dividido en 20, o sea 24. Con 4 camiones son 6 viajes cada uno, 90 minutos; con 6 camiones son 4 viajes cada uno, 60 minutos.", "Ambos cumplen el plazo de 120 minutos. El plan X cuesta $120.000 y el plan Y, $180.000."], "El plan X, porque cumple el plazo y cuesta menos"),
        ("Conciliar registros", "La guía de salida de un lote de ejemplo dice 300 bultos y el recibo del destino dice 305. ¿Qué diferencia hay y qué corresponde?", ["305 menos 300 son 5 bultos de más en el recibo.", "Es un sobrante, que se registra por escrito y se informa a quien corresponde."], "Sobrante de 5 bultos, que se registra e informa"),
    ],
    mistakes=[("Elegir siempre el plan que termina primero.", "Puede costar más sin que el plazo lo exija.", "Entre los planes que cumplen el plazo, elige el de menor costo."),
              ("Cambiar el recibo para que coincida con la guía de salida.", "Oculta una diferencia real que hay que investigar.", "Registra la diferencia y avisa a quien corresponde.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es conciliar los registros de una carga?", "Comparar dos registros de la misma carga y explicar las diferencias", "Unir dos registros en uno solo y borrar el segundo", "Copiar el registro del destino en el del origen", "Conciliar es comparar y explicar; unir, borrar o copiar oculta diferencias."),
        ("abc", "En Operaciones Portuarias: ¿qué es una lista de verificación?", "Una lista de puntos que se revisan uno por uno antes de dar una tarea por terminada", "Una lista de las personas autorizadas a entrar al recinto", "Un calendario con los turnos del mes", "La lista de verificación sirve para controlar la calidad de una tarea antes de cerrarla."),
        ("abc", "En Operaciones Portuarias: ¿qué significa el principio de cero faltas en los registros?", "Que la meta es que ningún documento o dato salga con errores u omisiones", "Que ninguna persona puede faltar a su turno", "Que no se permite registrar las diferencias encontradas", "Cero faltas se refiere a errores y omisiones en documentos, no a la asistencia."),
        ("=", "{F} ¿Cuántos viajes se necesitan en total para despachar los 720 bultos?", "720//24", "Se divide el total de bultos entre los que lleva cada camión por viaje.", " viajes"),
        ("=", "{F} ¿Cuántos pesos cuesta el plan P, que usa 5 camiones?", "5*35000", "Se multiplica el número de camiones por el costo de cada uno por turno.", " pesos"),
        ("=", "{F} ¿Cuántas horas tarda el plan Q, que usa 2 camiones, en despachar los 720 bultos?", "720//24//2*20//60", "Se calculan los viajes, se reparten entre 2 camiones, se multiplican por el ciclo y se pasan a horas.", " horas"),
        ("abc", "{F} ¿Qué plan conviene si el plazo es de 6 horas?", "El plan Q, porque cumple el plazo y cuesta menos", "El plan P, porque termina antes", "Ninguno, porque ambos superan el plazo", "Ambos cumplen el plazo y el plan Q cuesta menos."),
        ("abc", "{F} Si el plazo fuera de solo 3 horas, ¿qué plan serviría?", "El plan P, porque es el único que termina dentro de ese plazo", "El plan Q, porque es el más barato", "Ninguno, porque 3 horas no alcanzan para 720 bultos", "El plan Q tarda más que 3 horas, así que solo el plan P cumple."),
        ("abc", "{F} La guía de salida dice 720 bultos y el recibo del destino, 717. ¿Qué corresponde?", "Registrar un faltante de 3 bultos e informar a quien corresponde para investigarlo", "Corregir el recibo para que diga 720 y cerrar la operación", "Cerrar la operación porque la diferencia es pequeña", "Una diferencia, por pequeña que sea, se registra e investiga; no se altera el recibo."),
        ("=", "{F} ¿Cuántos pesos más cuesta el plan P que el plan Q?", "5*35000-2*35000", "Se resta el costo del plan Q al costo del plan P.", " pesos"),
        ("abc", "En Operaciones Portuarias: ¿por qué no conviene elegir siempre el plan que termina antes?", "Porque también cuenta el costo: conviene el plan más barato que cumpla el plazo", "Porque el plan más rápido siempre incumple el plazo del turno", "Porque terminar antes obliga a omitir la lista de verificación", "El mejor plan equilibra plazo y costo; la rapidez extra no siempre se necesita."),
        ("abc", "{F} Un compañero dice: «elijamos el plan Q y, para ahorrar, no revisemos la conciliación al final». ¿Qué respuesta es correcta?", "Es falso: la conciliación detecta diferencias como el faltante y se hace con cualquier plan", "Es cierto: la conciliación solo se hace en los planes con más camiones", "Es cierto: si se cumple el plazo, los registros no necesitan revisión", "Cumplir el plazo no garantiza que los registros coincidan."),
        ("abc", "{F} Se pide un plan que termine en 1 hora, con camiones de las mismas características. ¿Cuántos camiones se necesitan como mínimo?", "10 camiones, porque cada uno hace 3 viajes en una hora y se necesitan 30", "5 camiones, como en el plan P", "15 camiones, porque cada uno haría solo 2 viajes", "En 60 minutos cada camión hace 3 viajes de 20 minutos; 30 viajes entre 3 son 10."),
    ],
    ctx=("abc", "Al cerrar una operación de ejemplo, la lista de verificación tiene un punto sin revisar y tu compañero dice: «márcalo como hecho, seguro está bien». ¿Qué respondes?", "Que primero se revisa el punto y solo entonces se marca; si no se puede, se informa", "Que lo marcas, porque seguro está bien", "Que lo marcas y lo revisas la próxima semana", "Marcar sin revisar vuelve falsa la lista y puede dejar pasar errores."),
    sc=[
        ("En Operaciones Portuarias: ¿qué plan conviene cuando hay varios que cumplen el plazo?", "El de menor costo", "Entre los que cumplen, se elige el más barato."),
        ("¿Qué se hace si el recibo del destino no coincide con la guía de salida?", "Se registra la diferencia por escrito y se informa a quien corresponde", "No se cambia el registro para que cuadre."),
        ("En el puerto: ¿para qué sirve una lista de verificación?", "Para revisar punto por punto antes de cerrar una tarea", "Ayuda a controlar la calidad de la tarea antes de cerrarla."),
    ],
    op=("Terminal Demo debe despachar 600 bultos con camiones internos de ejemplo que llevan 25 bultos por viaje; cada viaje de ida y vuelta dura 30 minutos. Plan M: 4 camiones. Plan N: 2 camiones. Cada camión cuesta $20.000 por turno (precio de ejemplo). El plazo es de 7 horas. Escribe (a) cuántos viajes se necesitan, (b) cuántas horas tarda cada plan, (c) cuánto cuesta cada plan, (d) qué plan eliges y por qué.",
        "(a) 600 ÷ 25 = 24 viajes. (b) Plan M: 24 ÷ 4 = 6 viajes por camión, 6 × 30 = 180 minutos = 3 horas. Plan N: 24 ÷ 2 = 12 viajes por camión, 12 × 30 = 360 minutos = 6 horas. (c) Plan M: 4 × 20.000 = $80.000. Plan N: 2 × 20.000 = $40.000. (d) El plan N: cumple el plazo de 7 horas y cuesta menos.",
        ["calcula los viajes", "calcula las horas de cada plan", "calcula el costo de cada plan", "elige el plan que cumple el plazo y cuesta menos"],
        ["hoja con las cuatro respuestas"],
        ["elegir el plan solo por ser el más rápido", "olvidar pasar los minutos a horas", "no comparar con el plazo"],
        "Pregunta: «¿los dos planes cumplen el plazo?». Si no responde, pídele que compare las horas de cada plan con 7."),
    reinforce="Inventa dos planes con distinto número de camiones, calcula el costo de cada uno y decide cuál conviene para un plazo que elijas.",
    extend="Explica con un ejemplo por qué un faltante se registra y no se corrige en el recibo.",
)
