"""Montaje Industrial TP 3.º y 4.º medio: OAE-07 (fijar en su sitio: conceptos, programa de obra y cálculos de fijaciones) y OAE-08 (mantenimiento básico: conceptos, registros y planificación). Sin procedimientos operativos."""
from __future__ import annotations

from tp_moin_common import AVISO, EMER, build

O7 = "TP-MOIN-3y4-OAE-07"
O8 = "TP-MOIN-3y4-OAE-08"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (orden de montaje de ejemplo, inventada). Elementos por fijar: 4 pilares metálicos, 2 paneles prefabricados de hormigón, 1 estanque, 1 bomba, 30 m de cañería y 1 bandeja de cables. "
     "Peligros anotados: caída de piezas, atrapamiento entre piezas, trabajo en altura, ruido de herramientas y energía eléctrica en la bandeja de cables. Equipo de trabajo de ejemplo: 1 jefe de terreno, 1 prevencionista y 6 montajistas.")
build(
    O7, 1, F,
    use="Aprenderé qué significa fijar en su sitio los distintos elementos de un montaje, qué peligros tiene, por qué el trabajo es en equipo y qué tareas quedan reservadas a personal autorizado.",
    prior=["Sé qué es la jerarquía de controles.", "Sé qué es un permiso de trabajo.", "Sé qué es un plan y una zona de exclusión."],
    explain=[
        "Fijar en su sitio es dejar un elemento asegurado en su posición definitiva, según las especificaciones del proyecto: con anclajes, pernos, soldadura o apoyos. Se fijan estructuras metálicas, elementos prefabricados de hormigón, calderería (estanques y piezas de chapa), equipos mecánicos como una bomba, ductos y cañerías, y sistemas eléctricos, de instrumentación y de aislamiento. Para esto se usan herramientas manuales, eléctricas y neumáticas, que funcionan con aire a presión.",
        "El trabajo es en colaboración: cada persona tiene un rol, hay una charla de inicio donde se informan los peligros del día y se acuerdan las señales de comunicación. Los peligros son la caída de piezas, el atrapamiento entre piezas y estructuras, la caída desde altura, el ruido y la proyección de partículas de las herramientas, la energía eléctrica y el aire a presión. Los sistemas eléctricos solo los interviene un instalador autorizado, y la Superintendencia de Electricidad y Combustibles (SEC) fiscaliza las instalaciones eléctricas y de gas. El trabajo en altura exige capacitación, equipo certificado y permiso.",
        f"{EMER} Este cuaderno no enseña a fijar, apretar ni conectar nada. {AVISO}",
    ],
    vocab=[("fijar en su sitio", "dejar un elemento asegurado en su posición definitiva según las especificaciones"), ("calderería", "piezas de chapa como estanques y recipientes"), ("atrapamiento", "quedar una parte del cuerpo aprisionada entre piezas, estructuras o partes móviles"), ("charla de inicio", "reunión previa donde se informan los peligros del día, los roles y las señales"), ("herramienta neumática", "herramienta que funciona con aire a presión"), ("SEC", "Superintendencia de Electricidad y Combustibles, que fiscaliza las instalaciones eléctricas y de gas")],
    worked=[
        ("Reconocer el peligro", "Una persona de ejemplo pasa la mano entre una pieza que se desplaza y una estructura fija. ¿Qué peligro corre?", ["La mano puede quedar aprisionada entre ambas.", "Ese peligro se llama atrapamiento."], "Atrapamiento"),
        ("Cantidad de tramos", "Una cañería de ejemplo de 24 m se instala en tramos de 6 m. ¿Cuántos tramos son?", ["Se divide el largo total entre el largo de cada tramo.", "24 entre 6 son 4."], "4 tramos"),
    ],
    mistakes=[("Pensar que trabajar en equipo permite que cualquiera haga cualquier tarea.", "Cada tarea de riesgo tiene personal autorizado y un rol definido.", "Respeta los roles y consulta al supervisor antes de hacer algo distinto."),
              ("Omitir la charla de inicio porque «el trabajo es el mismo de ayer».", "Los peligros y las condiciones del lugar pueden haber cambiado.", "Participa en la charla y confirma peligros, roles y señales del día.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué significa fijar en su sitio una estructura o un equipo?", "Dejarlo asegurado en su posición definitiva, según las especificaciones", "Cambiarlo de lugar cada vez que se necesita", "Pintarlo para identificarlo", "Fijar es asegurar la posición definitiva; mover o pintar son otras tareas."),
        ("abc", "En Montaje Industrial: ¿qué es el atrapamiento?", "Quedar una parte del cuerpo aprisionada entre piezas, estructuras o partes móviles", "Caer desde una altura", "Respirar humos de una soldadura", "El atrapamiento es el aprisionamiento por piezas; la caída y los humos son otros peligros."),
        ("abc", "¿Qué institución fiscaliza las instalaciones eléctricas en Chile?", "La Superintendencia de Electricidad y Combustibles (SEC)", "El Servicio de Impuestos Internos", "El Instituto Nacional de Estadísticas", "La SEC fiscaliza la seguridad de las instalaciones eléctricas y de gas."),
        ("=", "{F} ¿Cuántas personas forman el equipo de trabajo de la ficha?", "1+1+6", "Se suman el jefe de terreno, el prevencionista y los montajistas.", " personas"),
        ("abc", "{F} ¿Qué peligro de la ficha se relaciona con la bandeja de cables?", "La energía eléctrica", "El ruido de las herramientas", "El atrapamiento entre piezas", "La ficha asocia la bandeja con energía eléctrica."),
        ("abc", "{F} ¿Quién puede intervenir el sistema eléctrico de la bandeja de cables?", "Un instalador eléctrico autorizado", "Cualquier montajista que use guantes", "El jefe de terreno por sí solo, sin autorización", "Las instalaciones eléctricas exigen personal autorizado por la entidad fiscalizadora."),
        ("=", "{F} La cañería de 30 m se instala en tramos de 6 m. ¿Cuántos tramos son?", "30//6", "Se divide el largo total entre el largo de cada tramo.", " tramos"),
        ("abc", "{F} Un cartel que dice «obligatorio usar protección auditiva» por el ruido de las herramientas debe ser de color:", "Azul, porque indica una obligación", "Rojo, porque indica una prohibición", "Verde, porque indica salvamento", "Las obligaciones se señalan en azul."),
        ("abc", "{F} Contra el atrapamiento entre piezas, ¿qué medida es de tipo administrativo?", "Una charla de inicio con señales y comunicación acordadas", "Una barrera física que impida acercarse", "Un guante resistente", "Las reglas, las señales y la capacitación son controles administrativos."),
        ("abc", "{F} Un montajista dice: «puedo trabajar sin charla de inicio, ya me sé el trabajo». ¿Qué respuesta es correcta?", "Es falso: la charla informa los peligros, los roles y las señales de este día y lugar", "Es cierto, si lleva años en el oficio", "Es cierto, si el trabajo es parecido al de ayer", "Las condiciones cambian y todos deben saber peligros y señales."),
        ("abc", "Durante una visita de ejemplo, un panel de hormigón se desplaza y una persona queda aprisionada contra una estructura. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Empujar el panel con otras personas", "Acercarte a revisar si respira", "Intervenir sin formación puede provocar otro atrapamiento; se avisa a quienes pueden actuar."),
        ("=", "{F} Cada montajista trabaja 8 horas al día. ¿Cuántas horas de trabajo suman los 6 montajistas en 5 días?", "6*8*5", "Se multiplican montajistas, horas por día y días.", " horas"),
        ("abc", "{F} La jefa propone que un montajista conecte la bandeja de cables «porque es sencillo». ¿Qué respuesta es correcta?", "No: el sistema eléctrico lo interviene solo un instalador autorizado", "Sí, si desconecta antes la energía por su cuenta", "Sí, si hay un compañero mirando", "Una intervención eléctrica sin autorización puede causar una descarga grave."),
    ],
    ctx=("abc", "Un conocido de ejemplo te ofrece pagarte por ayudar a instalar una bomba y su conexión eléctrica en una planta pequeña. ¿Qué respondes?", "Que no, porque instalar equipos y sistemas eléctricos exige personal autorizado, norma vigente y EPP, y que consultarás a un adulto responsable", "Que sí, si trabajas solo con herramientas manuales", "Que sí, si te explican la conexión en el lugar", "Un estudiante no está habilitado para instalar equipos ni intervenir sistemas eléctricos."),
    sc=[
        ("En Montaje Industrial: ¿qué es la charla de inicio?", "La reunión previa donde se informan peligros, roles y señales", "Permite que todos sepan los peligros del día."),
        ("¿Quién interviene los sistemas eléctricos de un montaje?", "Un instalador autorizado", "Las instalaciones eléctricas exigen personal con autorización vigente."),
        ("¿Qué es el atrapamiento?", "Quedar una parte del cuerpo aprisionada entre piezas o partes móviles", "Es un peligro propio de piezas que se desplazan."),
    ],
    op=("Orden de ejemplo: fijar 3 pilares, 5 m de ducto y una bandeja de cables. Equipo: 1 supervisor y 4 montajistas, 8 horas al día. Peligros anotados: caída de piezas, trabajo en altura y energía eléctrica. Escribe (a) cuántas personas forman el equipo, (b) cuántas horas de trabajo suman los montajistas en 3 días, (c) un control administrativo para la caída de piezas, (d) quién puede intervenir la parte eléctrica.",
        "(a) 1 + 4 = 5 personas. (b) 4 × 8 × 3 = 96 horas. (c) Una charla de inicio con señales acordadas y una zona de exclusión señalizada. (d) Un instalador eléctrico autorizado.",
        ["suma el equipo", "calcula las horas", "propone un control administrativo", "indica quién interviene lo eléctrico"],
        ["hoja con las cuatro respuestas"],
        ["no sumar al supervisor", "olvidar los días", "decir que un montajista puede conectar lo eléctrico"],
        "Pregunta: «¿quién puede hacer la parte eléctrica?». Si no responde, pídele que relea el párrafo de la SEC."),
    reinforce="Escribe cinco elementos que se fijan en un montaje y un peligro propio de cada uno.",
    extend="Explica con un ejemplo por qué una charla de inicio puede evitar un accidente aunque el trabajo se repita todos los días.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (lista de recepción de piezas de ejemplo, inventada). Pedido y llegada: columna C1, pedidas 6 y llegadas 6; viga B1, pedidas 10 y llegadas 9; arriostre R1, pedidos 12 y llegados 12; placa base PB, pedidas 6 y llegadas 6. "
     "De las 6 columnas C1 llegadas, una trae la marca ilegible. Especificación de anclaje de ejemplo: 6 pernos de anclaje por placa base. La lámina vigente es la revisión D; el montajista tiene en la mano la revisión C.")
build(
    O7, 2, F,
    use="Aprenderé los documentos que respaldan la fijación de elementos, cómo se registra la recepción de piezas y qué rol cumple cada persona.",
    prior=["Sé qué es una lámina de plano y su revisión.", "Sé leer una lista de piezas.", "Sé multiplicar y sumar números enteros."],
    explain=[
        "Antes de fijar, se reciben las piezas: se comprueba la marca, la cantidad y el estado de cada una contra la lista de piezas y el plano, y se registran los faltantes, los sobrantes y los daños. Una pieza con la marca ilegible se aparta y se informa, porque podría ubicarse mal. La placa base es la placa de acero en el pie de una columna, que se apoya y se ancla al hormigón con pernos de anclaje. Plomo es la vertical y nivel es la horizontal; se verifican con instrumentos calibrados.",
        "Los documentos de la fijación son el plano de montaje en su revisión vigente, la lista de piezas, la especificación de anclajes (tipo, diámetro y cantidad), las instrucciones de trabajo y los registros de recepción. Una instrucción de trabajo es un documento que redacta personal competente para describir las tareas y sus precauciones, y que se lee antes de comenzar. Los roles son el jefe de terreno, el supervisor de montaje, los montajistas, el topógrafo que verifica posiciones, el ITO que revisa que se cumpla el proyecto y el prevencionista.",
        f"El registro refleja lo que realmente llegó: nunca se anota como recibido lo que falta. {EMER} {AVISO}",
    ],
    vocab=[("recepción de piezas", "comprobación de marca, cantidad y estado de las piezas contra la lista y el plano"), ("placa base", "placa de acero en el pie de una columna, que se apoya y se ancla"), ("perno de anclaje", "perno que fija una placa base al hormigón"), ("instrucción de trabajo", "documento redactado por personal competente que describe tareas y precauciones"), ("plomo", "posición vertical"), ("nivel", "posición horizontal")],
    worked=[
        ("Revisar una recepción", "Un pedido de ejemplo pide 8 pilares y llegan 7. ¿Cuántos faltan?", ["Se resta lo llegado a lo pedido.", "8 menos 7 es 1."], "Falta 1 pilar"),
        ("Pernos de anclaje", "Una especificación de ejemplo pide 4 pernos por placa base y hay 5 placas. ¿Cuántos pernos hacen falta?", ["Se multiplican las placas por los pernos de cada una.", "5 por 4 son 20."], "20 pernos"),
    ],
    mistakes=[("Anotar como recibida una pieza que falta porque «va a llegar».", "El registro deja de reflejar la realidad y se pierde el control de faltantes.", "Registra lo recibido y deja el faltante informado."),
              ("Usar una pieza de marca ilegible porque «parece la de siempre».", "Podría instalarse en un lugar equivocado.", "Apártala e informa al supervisor para identificarla con la lista.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es una placa base?", "La placa de acero en el pie de una columna, que se apoya y se ancla", "Un tipo de pintura anticorrosiva", "Una herramienta de medida", "La placa base conecta la columna con la fundación; no es pintura ni herramienta."),
        ("abc", "En Montaje Industrial: ¿qué es la recepción de piezas?", "Comprobar marca, cantidad y estado de las piezas contra la lista y el plano, y registrar diferencias", "Comprar las piezas al proveedor", "Montar las piezas en su lugar", "La recepción verifica lo que llega; comprar y montar son otras etapas."),
        ("abc", "En Montaje Industrial: ¿qué es una instrucción de trabajo?", "Un documento redactado por personal competente que describe las tareas y sus precauciones", "Un consejo verbal de un compañero", "Un dibujo a escala", "La instrucción de trabajo es un documento escrito y revisado, no una opinión."),
        ("=", "{F} ¿Cuántas piezas se pidieron en total?", "6+10+12+6", "Se suman las piezas pedidas de las cuatro marcas.", " piezas"),
        ("=", "{F} ¿Cuántas piezas llegaron en total?", "6+9+12+6", "Se suman las piezas llegadas de las cuatro marcas.", " piezas"),
        ("abc", "{F} ¿Qué marca llegó incompleta?", "La viga B1, con 9 de 10", "El arriostre R1", "La placa base PB", "Solo la viga B1 llegó en menor cantidad que la pedida."),
        ("=", "{F} ¿Cuántos pernos de anclaje exige la especificación para todas las placas base?", "6*6", "Se multiplican las placas base por los pernos de cada una.", " pernos"),
        ("abc", "{F} ¿Qué corresponde con la columna de marca ilegible?", "Apartarla, registrar el hallazgo e informar al supervisor para identificarla con la lista", "Instalarla donde parezca que calza", "Marcarla a su gusto", "Una pieza sin identificación segura no se usa; se informa y se aclara."),
        ("abc", "{F} ¿Qué revisión del plano debe usar el montajista?", "La D, que es la vigente", "La C, porque es la que tiene en la mano", "La que le parezca más clara", "Solo la revisión vigente respalda el trabajo."),
        ("abc", "{F} Un compañero dice: «falta una viga pero la cuento como llegada, ya vendrá». ¿Qué respuesta es correcta?", "No: el registro refleja lo recibido y el faltante se informa", "Sí, para que el registro quede completo", "Sí, si el proveedor lo promete", "Un registro falso impide controlar faltantes y atrasos."),
        ("abc", "{F} Un montajista dice que una columna «quedó a plomo a ojo». ¿Por qué eso no basta?", "Porque la verticalidad se verifica con instrumentos calibrados y se registra", "Porque el plomo no importa", "Porque las columnas siempre quedan a plomo", "Una verificación sin instrumento ni registro no es evidencia."),
        ("=", "{F} Si la viga faltante llega mañana y se recibe 1 unidad, ¿cuántas piezas habrán llegado en total?", "6+9+12+6+1", "Se suman las piezas llegadas y la viga que llega después.", " piezas"),
        ("abc", "{F} Se propone reemplazar la viga faltante por otra de marca distinta que «tiene casi el mismo largo». ¿Quién debe decidirlo?", "El proyectista, y queda registrado", "El montajista que la instalará", "El que transporta las piezas", "Un cambio de pieza es un cambio de diseño."),
    ],
    ctx=("abc", "El supervisor de ejemplo te pide firmar la recepción como «completa», aunque falta una viga y una columna tiene la marca ilegible. ¿Qué respondes?", "Que no puedo firmar algo que no es cierto: se registran el faltante y la marca ilegible", "Que sí, para no atrasar la obra", "Que sí, pero firmando con otro nombre", "Firmar una recepción incorrecta es falsear un registro."),
    sc=[
        ("En Montaje Industrial: ¿qué se comprueba en la recepción de piezas?", "Marca, cantidad y estado contra la lista y el plano", "Así se detectan faltantes y daños antes de fijar."),
        ("¿Qué se hace con una pieza de marca ilegible?", "Se aparta y se informa al supervisor", "Podría instalarse en un lugar equivocado."),
        ("¿Qué revisión del plano se usa?", "La vigente", "Las revisiones antiguas pueden tener datos ya cambiados."),
    ],
    op=("Ficha de ejemplo: pedido y llegada: pilar P5, pedidos 8 y llegados 8; viga V5, pedidas 12 y llegadas 10; placa base, pedidas 8 y llegadas 8. Especificación: 4 pernos de anclaje por placa base. Escribe (a) cuántas piezas se pidieron y cuántas llegaron, (b) cuántas faltan y de qué marca, (c) cuántos pernos de anclaje se necesitan, (d) cómo registrarías el faltante.",
        "(a) Pedidas: 8 + 12 + 8 = 28; llegadas: 8 + 10 + 8 = 26. (b) Faltan 2 vigas V5. (c) 8 placas por 4 pernos son 32 pernos. (d) Anotando 10 vigas llegadas de 12 pedidas, con el faltante de 2 informado al supervisor.",
        ["suma pedidas y llegadas", "identifica el faltante", "calcula los pernos", "describe un registro fiel"],
        ["hoja con las cuatro respuestas"],
        ["anotar como llegada lo que falta", "restar mal", "olvidar multiplicar los pernos"],
        "Pregunta: «¿qué haces si falta una pieza?». Si no responde, pídele que relea la regla de registrar lo recibido."),
    reinforce="Escribe una lista de recepción de ejemplo con tres marcas, lo pedido y lo llegado, y marca los faltantes.",
    extend="Explica con un ejemplo por qué un registro fiel de recepción evita errores más adelante.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (programa de obra de ejemplo, descrito por escrito; un diagrama de Gantt es una barra por tarea sobre una escala de días). Tarea A, recepción de piezas: 1 día, sin tareas previas. Tarea B, verificación de ejes y placas base: 1 día, después de A. "
     "Tarea C, fijación de columnas: 3 días, después de B. Tarea D, fijación de vigas: 2 días, después de C. Tarea E, fijación de arriostres: 2 días, después de C. Tarea F, revisión del ITO: 1 día, después de D y de E. D y E pueden hacerse al mismo tiempo. "
     "En cada tarea participan 4 personas.")
build(
    O7, 3, F,
    use="Aprenderé a leer un programa de obra descrito como diagrama de Gantt, a reconocer tareas predecesoras y ruta crítica, y a ver cómo el trabajo simultáneo afecta plazo y seguridad.",
    prior=["Sé sumar números enteros.", "Sé qué es una tarea y una duración.", "Sé qué es una zona de exclusión."],
    explain=[
        "Un programa de obra ordena las tareas en el tiempo. El diagrama de Gantt dibuja cada tarea como una barra horizontal sobre una escala de días; el largo de la barra es la duración. Una tarea predecesora es la que debe terminar antes de que otra comience. Dos tareas sin dependencia entre sí pueden hacerse en paralelo, es decir, al mismo tiempo. La ruta crítica es la cadena de tareas más larga: si una tarea de esa cadena se atrasa, se atrasa toda la obra. Una tarea fuera de la ruta crítica tiene holgura, días que puede atrasarse sin cambiar el plazo.",
        "Para calcular el plazo se suman las duraciones de las tareas en cadena y, cuando hay tareas en paralelo, se cuenta solo la más larga. Una tarea que depende de dos predecesoras comienza cuando termina la última. El trabajo simultáneo ahorra tiempo, pero pone más personas y más piezas en la misma zona, y eso aumenta los riesgos de atrapamiento y de caída de piezas; por eso el prevencionista revisa el programa.",
        f"Este programa es de papel y de ejemplo: no autoriza a iniciar ninguna tarea. {EMER} {AVISO}",
    ],
    vocab=[("diagrama de Gantt", "gráfico de barras horizontales que muestra las tareas sobre una escala de tiempo"), ("tarea predecesora", "tarea que debe terminar antes de que otra comience"), ("tareas en paralelo", "tareas que se hacen al mismo tiempo"), ("ruta crítica", "cadena de tareas más larga; su atraso atrasa toda la obra"), ("holgura", "días que una tarea puede atrasarse sin cambiar el plazo"), ("persona-día", "trabajo de una persona durante un día")],
    worked=[
        ("Plazo con paralelo", "Tareas de ejemplo: P dura 2 días; Q y R, después de P, duran 3 y 1 días y se hacen al mismo tiempo; S dura 1 día después de Q y R. ¿Cuántos días dura todo?", ["En paralelo se cuenta la más larga, 3 días.", "2 más 3 más 1 son 6 días."], "6 días"),
        ("Persona-días", "Una tarea de ejemplo ocupa a 3 personas durante 4 días. ¿Cuántas persona-días son?", ["Se multiplican las personas por los días.", "3 por 4 son 12."], "12 persona-días"),
    ],
    mistakes=[("Sumar las duraciones de tareas en paralelo como si fueran en cadena.", "Las tareas simultáneas ocupan los mismos días.", "En paralelo cuenta solo la tarea más larga."),
              ("Poner más personas en la misma zona para terminar antes sin consultar.", "Más personas juntas aumentan el riesgo de atrapamiento y de caída de piezas.", "Revisa el programa con el prevencionista antes de cambiarlo.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué muestra un diagrama de Gantt?", "Las tareas como barras sobre una escala de tiempo", "El plano de la obra con cotas", "El presupuesto por partida", "El Gantt representa tareas y duraciones; el plano y el presupuesto son otros documentos."),
        ("abc", "En Montaje Industrial: ¿qué es una tarea predecesora?", "La que debe terminar antes de que otra comience", "La que cuesta más dinero", "La que hace el jefe de terreno", "Predecesora indica orden de dependencia, no costo ni responsable."),
        ("abc", "En Montaje Industrial: ¿qué es la ruta crítica de un programa?", "La cadena de tareas más larga; si se atrasa, se atrasa toda la obra", "La ruta por donde circulan los camiones", "La tarea más peligrosa", "La ruta crítica determina el plazo total del programa."),
        ("=", "{F} ¿Cuántos días sumarían las seis tareas si se hicieran una tras otra?", "1+1+3+2+2+1", "Se suman las duraciones de las seis tareas.", " días"),
        ("=", "{F} ¿Cuántos días dura el programa, haciendo D y E al mismo tiempo?", "1+1+3+2+1", "Se suman A, B, C, la más larga de D y E, y F.", " días"),
        ("abc", "{F} Contando el primer día como el día 1, ¿qué tarea comienza el día 3?", "La tarea C, de fijación de columnas", "La tarea D", "La tarea B", "A ocupa el día 1, B el día 2 y C comienza el día 3."),
        ("abc", "{F} ¿En qué días ocurren las tareas D y E?", "En los días 6 y 7", "En los días 3 y 4", "En los días 8 y 9", "C ocupa los días 3 a 5, y D y E van a continuación."),
        ("abc", "{F} ¿Qué tarea no puede comenzar hasta que terminen D y E?", "La tarea F, de revisión del ITO", "La tarea C", "La tarea A", "F depende de las dos tareas, por eso espera a la última."),
        ("=", "{F} Si E durara 3 días en lugar de 2, ¿cuántos días duraría el programa?", "1+1+3+3+1", "La tarea más larga entre D y E pasa a ser E, de 3 días.", " días"),
        ("abc", "{F} Un compañero dice: «D se atrasó un día y E no, así que el programa no cambia». ¿Qué respuesta es correcta?", "Es falso: F espera a ambas, D pasa a durar 3 días y el programa dura 9", "Es cierto, porque E sigue siendo de 2 días", "Es cierto, si se agregan personas a E", "F comienza cuando termina la última predecesora, que ahora es D."),
        ("abc", "{F} Para ganar tiempo se propone hacer D y E con 12 personas en la misma zona. ¿Qué advertencia corresponde?", "Más personas en la misma zona aumentan el riesgo de atrapamiento y de caída de piezas; lo revisa el prevencionista", "Ninguna, más personas siempre es más seguro", "Que se trabaje más rápido", "El trabajo simultáneo cambia el riesgo y debe evaluarse."),
        ("=", "{F} Con 4 personas en cada tarea, ¿cuántas persona-días suma el programa completo (cada tarea con su duración)?", "4*(1+1+3+2+2+1)", "Se multiplican las personas por la suma de los días de todas las tareas.", " persona-días"),
        ("=", "{F} Si cada persona-día cuesta $35.000 (valor de ejemplo), ¿cuánto cuesta el programa completo?", "4*(1+1+3+2+2+1)*35000", "Se multiplican las persona-días por el valor de cada una.", " pesos"),
    ],
    ctx=("abc", "El jefe de ejemplo te dice: «saltemos la tarea B, la verificación de ejes, para ganar un día». ¿Qué respondes?", "Que B es predecesora de C: sin verificar ejes y placas, la fijación podría quedar mal ubicada, y que se consulte al ITO", "Que sí, porque un día se recupera después", "Que sí, si C se hace más lento", "La verificación evita errores de posición que costarían mucho más que un día."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula la duración de tareas en paralelo?", "Se cuenta solo la más larga", "Las tareas en paralelo ocurren en los mismos días."),
        ("¿Qué pasa si se atrasa una tarea de la ruta crítica?", "Se atrasa toda la obra", "Una tarea de la ruta crítica no tiene holgura."),
        ("¿Qué riesgo aumenta con más personas en la misma zona?", "El atrapamiento y la caída de piezas", "Hay más movimiento en un mismo espacio."),
    ],
    op=("Programa de ejemplo: tarea G, 2 días, sin previas; tarea H, 3 días, después de G; tarea I, 2 días, después de G; tarea J, 1 día, después de H e I. H e I pueden hacerse al mismo tiempo. En cada tarea participan 3 personas. Escribe (a) cuántos días dura el programa, (b) qué tarea tiene holgura y cuántos días, (c) cuántas persona-días suma, (d) una advertencia de seguridad para H e I en paralelo.",
        "(a) 2 + 3 + 1 = 6 días. (b) La tarea I, que dura 2 días y puede atrasarse 1 día sin cambiar el plazo. (c) 3 × (2 + 3 + 2 + 1) = 24 persona-días. (d) Con H e I a la vez hay más personas y piezas en la zona, y el prevencionista debe revisar el riesgo de atrapamiento y de caída de piezas.",
        ["calcula el plazo", "identifica la holgura", "calcula las persona-días", "advierte sobre el riesgo del trabajo simultáneo"],
        ["hoja con las cuatro respuestas"],
        ["sumar las dos tareas en paralelo", "decir que I está en la ruta crítica", "no mencionar la seguridad"],
        "Pregunta: «¿qué tarea determina cuándo empieza J?». Si no responde, pídele que relea la regla de las dos predecesoras."),
    reinforce="Dibuja con barras de papel un programa de ejemplo de cuatro tareas y marca cuál está en la ruta crítica.",
    extend="Explica con un ejemplo por qué una tarea con holgura puede atrasarse sin afectar el plazo, pero no indefinidamente.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (cálculo de fijaciones de ejemplo, inventado). Cañería de 30 m con soportes cada 3 m (valor de ejemplo, no normativo), con un soporte al comienzo y otro al final; cada soporte se fija con 2 pernos. "
     "Ducto de 18 m armado con tramos de 2 m; cada unión entre tramos lleva 6 pernos. Bandeja de cables de 24 m armada con tramos de 3 m. Precio de ejemplo: $150 por perno.")
build(
    O7, 4, F,
    use="Aprenderé a calcular en papel la cantidad de soportes, tramos, uniones y pernos de una cañería, un ducto y una bandeja, y por qué las separaciones las fija el proyecto.",
    prior=["Sé dividir y multiplicar números enteros.", "Sé qué es un tramo y una unión.", "Sé qué es una especificación técnica."],
    explain=[
        "Para contar elementos en línea se usa una regla: la cantidad de soportes es el largo dividido por la separación más uno, si hay soporte al comienzo y al final, porque hay un soporte más que espacios entre ellos. La cantidad de uniones entre tramos es la cantidad de tramos menos uno, porque cada unión conecta dos tramos vecinos. Los pernos totales se obtienen multiplicando las uniones o los soportes por los pernos de cada uno.",
        "Un soporte sostiene una cañería, un ducto o una bandeja en su posición. La separación entre soportes y la cantidad de pernos por unión son datos de diseño: dependen del material, del diámetro y de la carga, y los fija el proyecto. Si en la obra parece necesario cambiarlos, se consulta al proyectista. En una cubicación se cuenta primero los elementos y después se multiplica por el precio.",
        f"Estos cálculos son de planilla, con cifras de ejemplo. Fijar soportes, armar ductos o conectar bandejas reales exige personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("soporte", "elemento que sostiene una cañería, un ducto o una bandeja en su posición"), ("tramo", "parte de una línea entre dos uniones"), ("unión entre tramos", "punto donde se conectan dos tramos vecinos"), ("bandeja de cables", "canal metálico que sostiene cables eléctricos"), ("dato de diseño", "valor que fija el proyecto y no se cambia en obra sin autorización")],
    worked=[
        ("Contar soportes", "Una cañería de ejemplo de 20 m lleva soportes cada 4 m, con uno al comienzo y otro al final. ¿Cuántos soportes son?", ["Hay 20 entre 4, es decir 5 espacios.", "Hay un soporte más que espacios: 6."], "6 soportes"),
        ("Contar uniones", "Un ducto de ejemplo tiene 7 tramos. ¿Cuántas uniones entre tramos tiene?", ["Cada unión conecta dos tramos vecinos.", "Hay un tramo más que uniones: 7 menos 1 son 6."], "6 uniones"),
    ],
    mistakes=[("Contar los soportes dividiendo el largo entre la separación y olvidar el del extremo.", "Hay un soporte más que espacios.", "Suma uno al resultado de la división."),
              ("Cambiar la separación entre soportes porque «parece sobrada».", "Es un dato de diseño que depende de la carga y del material.", "Consulta al proyectista antes de cambiar cualquier dato de diseño.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es un soporte de cañería?", "Un elemento que sostiene la cañería en su posición", "Un producto que protege contra la corrosión", "Un instrumento que mide la presión", "El soporte mantiene la cañería en su lugar; la protección y la medición son otras funciones."),
        ("abc", "En Montaje Industrial: ¿qué es una unión entre tramos de ducto?", "El punto donde se conectan dos tramos vecinos", "El extremo libre del ducto", "El soporte que sostiene el ducto", "Una unión conecta dos tramos; el extremo libre no conecta con otro."),
        ("abc", "En Montaje Industrial: ¿por qué la separación entre soportes la fija el proyecto?", "Porque depende del material, el diámetro y la carga, y se calcula y especifica", "Porque se elige según lo que sobre de material", "Porque la decide el montajista que instala", "Es un dato de diseño que no se improvisa en obra."),
        ("=", "{F} ¿Cuántos soportes necesita la cañería, con uno al comienzo y otro al final?", "30//3+1", "Se divide el largo entre la separación y se suma el soporte del extremo.", " soportes"),
        ("=", "{F} ¿Cuántos pernos llevan todos los soportes de la cañería?", "(30//3+1)*2", "Se multiplican los soportes por los pernos de cada uno.", " pernos"),
        ("=", "{F} ¿Cuántos tramos de ducto hay?", "18//2", "Se divide el largo total entre el largo de cada tramo.", " tramos"),
        ("=", "{F} ¿Cuántas uniones entre tramos tiene el ducto?", "18//2-1", "Hay una unión menos que tramos.", " uniones"),
        ("=", "{F} ¿Cuántos pernos llevan todas las uniones del ducto?", "(18//2-1)*6", "Se multiplican las uniones por los pernos de cada una.", " pernos"),
        ("=", "{F} ¿Cuántas uniones entre tramos tiene la bandeja de cables?", "24//3-1", "Hay una unión menos que tramos.", " uniones"),
        ("abc", "{F} Un compañero cuenta 10 soportes para la cañería porque divide 30 entre 3. ¿Qué error comete?", "Olvida el soporte del extremo: hay un soporte más que espacios", "Debió multiplicar 30 por 3", "No comete ningún error", "Con soporte en ambos extremos, los soportes superan a los espacios en uno."),
        ("abc", "{F} En obra se piensa que 4 m entre soportes «alcanza igual». ¿Qué corresponde?", "Consultar al proyectista: la separación es un dato de diseño", "Cambiarla, porque ahorra pernos", "Cambiarla solo en el tramo del medio", "Los datos de diseño los cambia el proyectista, no la obra."),
        ("=", "{F} ¿Cuánto cuestan los pernos de los soportes de la cañería y de las uniones del ducto juntos?", "((30//3+1)*2+(18//2-1)*6)*150", "Se suman los pernos de soportes y uniones y se multiplican por el precio de cada perno.", " pesos"),
        ("=", "{F} Si un montajista puede fijar 5 soportes por día, ¿cuántos días necesita un montajista para los soportes de la cañería, redondeando hacia arriba?", "(30//3+1+4)//5", "Se divide el total de soportes entre los que fija por día, redondeando hacia arriba.", " días"),
    ],
    ctx=("abc", "Un supervisor de ejemplo te pide el cálculo de pernos para el pedido de hoy y te dice: «cuenta 10 soportes, que la cañería es de 30 m con soportes cada 3 m». ¿Qué respondes?", "Que son 11 soportes porque hay uno en cada extremo, y que se compra con ese dato", "Que son 10, porque 30 entre 3 es 10", "Que son 9, porque el primero no se cuenta", "Con soportes en los dos extremos hay un soporte más que espacios."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calculan los soportes de una línea con soporte en ambos extremos?", "Largo entre separación, más uno", "Hay un soporte más que espacios."),
        ("¿Cuántas uniones hay entre 9 tramos?", "8 uniones", "Hay una unión menos que tramos."),
        ("¿Quién cambia la separación entre soportes?", "El proyectista", "Es un dato de diseño que fija el proyectista."),
    ],
    op=("Ficha de ejemplo: cañería de 24 m con soportes cada 4 m, uno al comienzo y otro al final, y 2 pernos por soporte. Ducto de 12 m con tramos de 3 m y 4 pernos por unión. Precio de ejemplo: $200 por perno. Escribe (a) los soportes y sus pernos, (b) los tramos y las uniones del ducto, (c) los pernos de las uniones, (d) el costo de todos los pernos.",
        "(a) 24 ÷ 4 + 1 = 7 soportes; 7 × 2 = 14 pernos. (b) 12 ÷ 3 = 4 tramos; 4 − 1 = 3 uniones. (c) 3 × 4 = 12 pernos. (d) (14 + 12) × 200 = 5.200 pesos.",
        ["calcula soportes y pernos", "calcula tramos y uniones", "calcula los pernos de las uniones", "calcula el costo"],
        ["hoja con los cuatro cálculos"],
        ["olvidar el soporte del extremo", "contar tantas uniones como tramos", "olvidar multiplicar por el precio"],
        "Pregunta: «¿cuántas uniones hay entre 4 tramos?». Si no responde, pídele que relea la regla de las uniones."),
    reinforce="Calcula en papel los soportes de una cañería de 18 m con soportes cada 3 m, con uno al comienzo y otro al final.",
    extend="Explica con un ejemplo por qué una separación de soportes es un dato de diseño y no una decisión de obra.",
)

# ============================================================ OAE-07, clase 5
F = ("Ficha 5 (programas de ejemplo, inventados). Programa A: 10 días con 6 personas por día. Programa B: 8 días con 8 personas por día. Valor de ejemplo: $40.000 por persona-día. "
     "Regla de seguridad de ejemplo, no normativa: en una misma zona no pueden trabajar más de 7 personas a la vez, por riesgo de atrapamiento y de caída de piezas; el programa que la incumple se descarta. "
     "Protocolo de recepción de las fijaciones de ejemplo: 10 puntos revisados; 9 cumplen y 1 no cumple.")
build(
    O7, 5, F,
    use="Aprenderé a comparar programas de obra por costo, plazo y seguridad, a aplicar una regla de seguridad que descarta una alternativa y a verificar la calidad con un protocolo de recepción.",
    prior=["Sé qué es una persona-día.", "Sé qué es una regla de descarte.", "Sé calcular un porcentaje simple."],
    explain=[
        "Al comparar alternativas de programa se calculan el plazo, las persona-días y el costo, y se revisan las reglas de seguridad. Las persona-días son los días de duración por la cantidad de personas, y el costo es las persona-días por el valor de cada una. Un programa más corto no siempre es mejor: si incumple una regla de seguridad, se descarta aunque termine antes.",
        "La calidad de las fijaciones se verifica con un protocolo de recepción: un documento con puntos que se revisan al terminar, cada uno marcado como cumple o no cumple, con fecha y firma de quienes revisan. El porcentaje de cumplimiento es los puntos que cumplen por 100, entre los revisados. Un punto que no cumple es una no conformidad que se registra y se informa al ITO antes de firmar la entrega. Firmar un protocolo es asumir responsabilidad por lo que dice.",
        f"Las comparaciones y los protocolos son de papel y con cifras de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("persona-día", "trabajo de una persona durante un día"), ("regla de seguridad de ejemplo", "condición inventada que sirve para practicar el descarte de una alternativa"), ("protocolo de recepción", "documento con puntos revisados al terminar, marcados como cumple o no cumple, con fecha y firma"), ("porcentaje de cumplimiento", "puntos que cumplen por 100, divididos entre los revisados"), ("entrega", "traspaso formal de un trabajo terminado a quien lo recibe")],
    worked=[
        ("Costo de un programa", "Un programa de ejemplo tiene 5 días con 4 personas por día, a $30.000 la persona-día. ¿Cuánto cuesta?", ["Persona-días: 5 por 4 son 20.", "Costo: 20 por 30.000 son 600.000."], "600.000 pesos"),
        ("Descartar por seguridad", "Un programa de ejemplo termina en 6 días pero pone 9 personas en una zona donde la regla admite 7. ¿Se elige?", ["Incumple la regla de seguridad.", "Se descarta aunque sea corto."], "No, se descarta"),
    ],
    mistakes=[("Elegir el programa más corto sin mirar las reglas de seguridad.", "Un programa inseguro se descarta antes de comparar plazo o costo.", "Aplica primero las reglas de seguridad."),
              ("Firmar el protocolo con un punto que no cumple.", "Se oculta un defecto y se asume una responsabilidad falsa.", "Registra la no conformidad e informa al ITO antes de firmar.")],
    T=[
        ("abc", "En Montaje Industrial: ¿cuándo se descarta un programa de obra aunque sea más corto?", "Cuando incumple una regla de seguridad, como superar el máximo de personas en una zona", "Cuando cuesta un poco más", "Cuando lo propone alguien nuevo", "La seguridad es una condición previa; el plazo corto no la reemplaza."),
        ("abc", "En Montaje Industrial: ¿qué es un protocolo de recepción de fijaciones?", "Un documento con puntos que se revisan al terminar, marcados como cumple o no cumple y firmados", "Una lista de precios de pernos", "Un permiso para comenzar el trabajo", "El protocolo deja constancia punto por punto de la revisión final."),
        ("abc", "En Montaje Industrial: ¿qué se hace con un punto del protocolo que no cumple?", "Registrarlo como no conformidad e informar al ITO antes de firmar", "Borrarlo para que el protocolo quede limpio", "Marcarlo como cumple si es un punto menor", "Una no conformidad abierta se informa; no se oculta."),
        ("=", "{F} ¿Cuántas persona-días tiene el programa A?", "10*6", "Se multiplican los días por las personas de cada día.", " persona-días"),
        ("=", "{F} ¿Cuántas persona-días tiene el programa B?", "8*8", "Se multiplican los días por las personas de cada día.", " persona-días"),
        ("=", "{F} ¿Cuánto cuesta el programa A?", "10*6*40000", "Se multiplican las persona-días por el valor de cada una.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el programa B?", "8*8*40000", "Se multiplican las persona-días por el valor de cada una.", " pesos"),
        ("abc", "{F} ¿Qué programa incumple la regla de seguridad de ejemplo?", "El B, con 8 personas a la vez", "El A, con 6 personas a la vez", "Ninguno", "La regla admite hasta 7 personas y el programa B pone 8."),
        ("abc", "{F} ¿Qué programa se elige aplicando la regla de seguridad?", "El A, porque el B se descarta aunque termine antes", "El B, porque termina antes", "Ninguno, hay que repetir todo", "El descarte por seguridad elimina a B antes de comparar costos."),
        ("abc", "{F} Un compañero dice: «B termina 2 días antes, elijámoslo y veamos cómo acomodar a la gente». ¿Qué respuesta es correcta?", "No: la regla de seguridad descarta a B; ganar tiempo no justifica el riesgo", "Sí, porque dos días valen la pena", "Sí, si el costo es parecido", "Una regla de seguridad no se negocia por plazo."),
        ("=", "{F} ¿Qué porcentaje de los puntos del protocolo cumple?", "9*100//10", "Se multiplica por 100 lo que cumple y se divide entre el total de puntos.", " %"),
        ("=", "{F} ¿Cuántos días más tarda el programa A que el B?", "10-8", "Se resta la duración de B a la de A.", " días"),
        ("abc", "{F} Un jefe pide firmar el protocolo como «10 de 10» para entregar hoy. ¿Qué respuesta es correcta?", "No: el punto que no cumple se registra y se informa antes de firmar", "Sí, porque es solo un punto", "Sí, si se corrige el protocolo después", "Firmar un protocolo falso oculta una no conformidad."),
    ],
    ctx=("abc", "La jefa de ejemplo te dice: «elige el programa B, la gente se acomoda y ahorramos 2 días». ¿Qué respondes?", "Que B incumple la regla de seguridad de 7 personas a la vez y que se elige A, dejando constancia de la decisión", "Que sí, porque 2 días son importantes", "Que sí, si los trabajadores aceptan", "La regla de seguridad es un límite que no depende de la aceptación."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula el costo de un programa?", "Persona-días por el valor de cada una", "El costo depende de personas y días."),
        ("¿Qué se hace con un programa que incumple una regla de seguridad?", "Se descarta", "La seguridad va antes que el plazo."),
        ("¿Qué se hace con un punto del protocolo que no cumple?", "Se registra e informa al ITO", "No se oculta ni se compensa."),
    ],
    op=("Ficha de ejemplo: programa P: 12 días con 5 personas por día; programa Q: 9 días con 7 personas por día; valor de $35.000 por persona-día. Regla de seguridad de ejemplo: no más de 6 personas a la vez en una zona. Un protocolo de 10 puntos tiene 8 que cumplen. Escribe (a) el costo de P y de Q, (b) qué programa incumple la regla, (c) cuál se elige y por qué, (d) el porcentaje de cumplimiento del protocolo y qué hacer con el punto que no cumple.",
        "(a) P: 12 × 5 × 35.000 = 2.100.000 pesos; Q: 9 × 7 × 35.000 = 2.205.000 pesos. (b) Q, con 7 personas a la vez. (c) P, porque Q se descarta por la regla de seguridad. (d) 8 × 100 ÷ 10 = 80 %; registrar el punto como no conformidad e informar al ITO antes de firmar.",
        ["calcula los dos costos", "identifica el programa que incumple", "elige con la regla de seguridad", "calcula el cumplimiento y la acción"],
        ["hoja con los cálculos y la decisión"],
        ["elegir Q por ser más corto", "olvidar multiplicar por el valor", "no informar la no conformidad"],
        "Pregunta: «¿quién gana si una opción es más barata pero incumple la regla?». Si no responde, pídele que relea la regla de descarte."),
    reinforce="Calcula las persona-días y el costo de un programa de 6 días con 4 personas por día, a $25.000 la persona-día.",
    extend="Explica con un ejemplo por qué firmar un protocolo es asumir una responsabilidad.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (taller de ejemplo, inventado). El taller tiene 3 equipos: un esmeril de banco, un compresor de aire y un taladro de columna. Plan de mantenimiento de ejemplo: esmeril, cada 3 meses; compresor, cada 2 meses; taladro, cada 6 meses. "
     "Peligros anotados: partes móviles, energía eléctrica, aire a presión que queda dentro del equipo, superficies calientes y partículas que pueden proyectarse.")
build(
    O8, 1, F,
    use="Aprenderé qué es el mantenimiento y sus tipos, por qué es una tarea de seguridad, qué peligros tiene y por qué un equipo en mantenimiento no debe poder ponerse en marcha.",
    prior=["Sé qué es la jerarquía de controles.", "Sé qué es un permiso de trabajo.", "Sé dividir números enteros."],
    explain=[
        "El mantenimiento es el conjunto de acciones para que los instrumentos, herramientas, máquinas y equipos sigan funcionando y sean seguros. El mantenimiento preventivo se hace según un plan para evitar fallas; el correctivo se hace después de que algo falla; el predictivo se decide según mediciones de la condición del equipo. El mantenimiento básico comprende la limpieza, la inspección, el registro y las acciones sencillas que indica el manual del fabricante; lo demás es de técnicos especializados.",
        "Un equipo en mantenimiento puede tener energía peligrosa: electricidad, aire a presión que queda almacenado, piezas que giran o se mueven, calor y resortes tensos. Por eso un equipo en mantenimiento no debe poder ponerse en marcha por error. Esto se logra con un procedimiento de bloqueo y etiquetado que define la empresa y se aprende con un instructor autorizado; este cuaderno no lo describe. Una herramienta dañada es un peligro, y reportarla es parte del mantenimiento.",
        f"{EMER} Nunca intervengas una máquina en casa o en un taller sin instructor autorizado. {AVISO}",
    ],
    vocab=[("mantenimiento preventivo", "el que se hace según un plan para evitar fallas"), ("mantenimiento correctivo", "el que se hace después de una falla para recuperar el funcionamiento"), ("mantenimiento predictivo", "el que se decide según mediciones de la condición del equipo"), ("mantenimiento básico", "limpieza, inspección, registro y acciones sencillas indicadas por el manual"), ("energía peligrosa", "electricidad, presión almacenada, movimiento o calor que puede lesionar"), ("bloqueo y etiquetado", "procedimiento de la empresa para que un equipo no se ponga en marcha mientras se interviene")],
    worked=[
        ("Clasificar", "Una máquina de ejemplo se detiene por una falla y se repara para que vuelva a funcionar. ¿Qué tipo de mantenimiento es?", ["La intervención ocurre después de la falla.", "Eso es mantenimiento correctivo."], "Correctivo"),
        ("Frecuencia al año", "Un equipo de ejemplo se revisa cada 4 meses. ¿Cuántas revisiones hay al año?", ["Un año tiene 12 meses.", "12 entre 4 son 3."], "3 revisiones"),
    ],
    mistakes=[("Creer que basta con apagar un equipo para trabajar seguro sobre él.", "Puede quedar energía almacenada o alguien podría ponerlo en marcha.", "Se usa el procedimiento de bloqueo de la empresa, con personal capacitado."),
              ("Dejar sin reportar una herramienta dañada para seguir trabajando.", "Una herramienta dañada puede lesionar a quien la use después.", "Repórtala al supervisor para que se retire y se repare.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es el mantenimiento preventivo?", "El que se hace según un plan para evitar fallas", "El que se hace después de que el equipo falla", "El que se hace solo si el operador lo pide", "Preventivo significa anticiparse a la falla con un plan."),
        ("abc", "En Montaje Industrial: ¿qué es el mantenimiento correctivo?", "El que se hace después de una falla para recuperar el funcionamiento", "El que se hace con un plan antes de que falle", "El que se hace comprando un equipo nuevo siempre", "Correctivo corrige una falla que ya ocurrió."),
        ("abc", "En Montaje Industrial: ¿por qué un equipo en mantenimiento no debe poder ponerse en marcha?", "Porque una puesta en marcha inesperada puede atrapar o lesionar a quien lo interviene", "Porque el equipo se gasta más", "Porque el plan de mantenimiento lo prohíbe por costumbre", "El riesgo real es la lesión por un arranque inesperado."),
        ("=", "{F} ¿Cuántos mantenimientos al año tiene el compresor, si se hace cada 2 meses?", "12//2", "Se divide el número de meses del año entre la frecuencia.", " mantenimientos"),
        ("=", "{F} ¿Cuántos mantenimientos al año tiene el esmeril?", "12//3", "Se divide el número de meses del año entre la frecuencia.", " mantenimientos"),
        ("abc", "{F} ¿Qué equipo del plan se revisa con más tiempo entre un mantenimiento y el siguiente?", "El taladro, cada 6 meses", "El compresor, cada 2 meses", "El esmeril, cada 3 meses", "El intervalo más largo del plan es el del taladro, de 6 meses."),
        ("=", "{F} ¿Cuántos mantenimientos programados suman los tres equipos en un año?", "12//3+12//2+12//6", "Se suman los mantenimientos anuales de cada equipo.", " mantenimientos"),
        ("abc", "{F} ¿Qué peligro de la ficha sigue presente en el compresor aunque esté apagado?", "El aire a presión que queda dentro del equipo", "La proyección de partículas del taladro", "El ruido del esmeril", "La presión almacenada no desaparece al apagar el equipo."),
        ("abc", "{F} Un compañero quiere abrir el compresor «solo un momento» sin avisar. ¿Qué corresponde?", "No hacerlo: es una intervención de personal autorizado, con procedimiento y bloqueo de energías", "Hacerlo con cuidado, porque es rápido", "Hacerlo si está apagado", "Abrir un equipo con presión almacenada exige procedimiento y autorización."),
        ("abc", "{F} Un compañero dice: «con dejar apagado el taladro basta para trabajar sin riesgo». ¿Qué respuesta es correcta?", "Es falso: apagar no asegura que no se ponga en marcha ni que no haya energía almacenada; se usa el procedimiento de bloqueo de la empresa", "Es cierto, si lo desenchufa otro compañero", "Es cierto, si lleva guantes", "Apagar no es lo mismo que dejar el equipo sin energía y asegurado."),
        ("abc", "Durante una visita de ejemplo a un taller, el brazo de una persona queda atrapado en una máquina. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar mover las partes de la máquina para liberarlo", "Esperar a que se libere solo", "Intervenir sin formación puede causar nuevas lesiones; se avisa a quienes pueden actuar."),
        ("=", "{F} Cada mantenimiento del compresor toma 3 horas de personal capacitado. ¿Cuántas horas suma al año?", "12//2*3", "Se multiplican los mantenimientos anuales por las horas de cada uno.", " horas"),
        ("abc", "{F} El taller propone atrasar el mantenimiento preventivo del esmeril para ahorrar. ¿Qué advertencia corresponde?", "Atrasarlo aumenta la probabilidad de falla y de accidente; se evalúa con el supervisor", "Ninguna, porque nada cambia", "Que lo atrase solo un día", "El mantenimiento preventivo reduce fallas y riesgos; atrasarlo suele costar más."),
    ],
    ctx=("abc", "Un familiar de ejemplo te pide que desarmes su compresor «para ver por qué no funciona», con lo que aprendiste. ¿Qué respondes?", "Que no, porque puede tener presión y electricidad, y que se lleve a un técnico autorizado", "Que sí, si lo desenchufas antes", "Que sí, si usas guantes y lentes", "Aprender conceptos no habilita para intervenir equipos con energía almacenada."),
    sc=[
        ("En Montaje Industrial: ¿cuál es la diferencia entre mantenimiento preventivo y correctivo?", "El preventivo es antes de la falla y el correctivo, después", "Uno se anticipa y el otro repara."),
        ("¿Qué energías puede tener un equipo apagado?", "Presión almacenada, calor, resortes o electricidad", "Apagar no siempre elimina la energía."),
        ("¿Qué se hace con una herramienta dañada?", "Se reporta al supervisor para retirarla y repararla", "Una herramienta dañada es un peligro."),
    ],
    op=("Taller de ejemplo: una prensa se revisa cada 4 meses, una bomba cada 3 meses y una sierra cada 6 meses. Peligros: movimiento de piezas, presión almacenada y electricidad. Escribe (a) cuántos mantenimientos al año tiene cada equipo, (b) cuántos en total, (c) por qué no basta con apagar un equipo antes de intervenirlo, (d) quién hace la intervención.",
        "(a) Prensa: 12 ÷ 4 = 3; bomba: 12 ÷ 3 = 4; sierra: 12 ÷ 6 = 2. (b) 3 + 4 + 2 = 9. (c) Porque puede haber energía almacenada y alguien podría ponerlo en marcha; se usa el procedimiento de bloqueo de la empresa. (d) Personal capacitado y autorizado, con instructor y norma vigente.",
        ["calcula los mantenimientos de cada equipo", "suma el total", "explica por qué apagar no basta", "indica quién interviene"],
        ["hoja con las cuatro respuestas"],
        ["dividir mal el año", "creer que apagar elimina toda la energía", "decir que un estudiante puede intervenir"],
        "Pregunta: «¿qué energías pueden quedar en un equipo apagado?». Si no responde, pídele que relea el párrafo de energía peligrosa."),
    reinforce="Escribe un ejemplo de mantenimiento preventivo, uno correctivo y uno predictivo en un taller inventado.",
    extend="Explica con un ejemplo por qué reportar una herramienta dañada es parte del mantenimiento.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (hoja de vida de ejemplo, inventada). Equipo: compresor C-1. Registros: a las 1.000 horas de uso, cambio de filtro; a las 1.250 horas, inspección preventiva; a las 1.400 horas, falla de una manguera; a las 1.400 horas, cambio de la manguera. "
     "Plan de ejemplo: inspección preventiva cada 250 horas de uso. Horómetro actual: 1.690 horas.")
build(
    O8, 2, F,
    use="Aprenderé qué documentos usa el mantenimiento, cómo se lee una hoja de vida, quién hace cada tarea y para qué sirve el orden en el lugar de trabajo.",
    prior=["Sé qué es el mantenimiento preventivo y el correctivo.", "Sé leer una tabla.", "Sé sumar y restar números enteros."],
    explain=[
        "El mantenimiento se apoya en documentos. El plan de mantenimiento fija qué se hace, a qué equipo y cada cuánto, ya sea por tiempo o por horas de uso medidas con un horómetro. La hoja de vida de un equipo registra su historia: cada inspección, cambio de pieza y falla, con fecha o con horas de uso. La orden de trabajo de mantenimiento autoriza y registra una intervención. El manual del fabricante indica lo que corresponde hacer y con qué repuestos. La lista de verificación ordena lo que se inspecciona.",
        "Los roles son el operador, que inspecciona a diario y avisa de anomalías; el técnico de mantenimiento, que ejecuta las intervenciones que le corresponden; el supervisor, que prioriza y firma; la bodega, que controla repuestos; y el prevencionista. Para mantener el lugar ordenado se usan las 5S: clasificar, ordenar, limpiar, estandarizar y mantener la disciplina. Un lugar ordenado y limpio evita tropiezos, incendios y pérdidas de herramientas.",
        f"Los registros de este cuaderno son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("plan de mantenimiento", "documento que fija qué se hace, a qué equipo y cada cuánto"), ("hoja de vida", "registro de la historia de un equipo: inspecciones, cambios y fallas"), ("orden de trabajo de mantenimiento", "documento que autoriza y registra una intervención"), ("horómetro", "instrumento que cuenta las horas de uso de un equipo"), ("5S", "método de orden y limpieza: clasificar, ordenar, limpiar, estandarizar y mantener la disciplina"), ("repuesto", "pieza de reemplazo de un equipo")],
    worked=[
        ("Próxima inspección", "Un equipo de ejemplo se inspecciona cada 500 horas y la última fue a las 2.000 horas. ¿A qué hora de uso corresponde la siguiente?", ["Se suma la frecuencia a la última inspección.", "2.000 más 500 son 2.500 horas."], "A las 2.500 horas"),
        ("Contar registros", "La hoja de vida de ejemplo de otro equipo anota 3 inspecciones y 2 fallas. ¿Cuántos registros tiene?", ["Se suman las inspecciones y las fallas.", "3 más 2 son 5."], "5 registros"),
    ],
    mistakes=[("No anotar en la hoja de vida una intervención pequeña.", "Sin registro se pierde la historia y se repiten fallas.", "Anota toda intervención, con fecha u horas de uso y quién la hizo."),
              ("Confundir el plan de mantenimiento con la hoja de vida.", "El plan dice qué se hará; la hoja registra lo que ya ocurrió.", "Usa el plan para programar y la hoja para consultar la historia.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es la hoja de vida de un equipo?", "El registro de su historia de inspecciones, cambios y fallas", "El plan de lo que se hará en el futuro", "El manual de uso del fabricante", "La hoja de vida registra lo ocurrido; el plan programa lo futuro."),
        ("abc", "En Montaje Industrial: ¿qué indica un horómetro?", "Las horas de uso acumuladas de un equipo", "La temperatura del equipo", "La presión del aire", "El horómetro cuenta horas de uso, útiles para programar mantenimientos."),
        ("abc", "En Montaje Industrial: ¿qué documento autoriza y registra una intervención de mantenimiento?", "La orden de trabajo de mantenimiento", "La lámina de planos", "La lista de precios", "La orden de trabajo deja constancia de lo que se intervino."),
        ("=", "{F} ¿A cuántas horas de uso corresponde la siguiente inspección preventiva, contando desde la última de la hoja de vida?", "1250+250", "Se suma la frecuencia del plan a la hora de la última inspección.", " horas"),
        ("=", "{F} ¿Cuántas horas de uso transcurrieron entre el cambio de filtro y la falla de la manguera?", "1400-1000", "Se resta la hora del cambio de filtro a la hora de la falla.", " horas"),
        ("abc", "{F} ¿Qué tipo de mantenimiento fue el cambio de manguera a las 1.400 horas?", "Correctivo, porque ocurrió después de una falla", "Preventivo, porque se cambió una pieza", "Predictivo, porque se midió algo", "El cambio fue consecuencia de una falla, por eso es correctivo."),
        ("=", "{F} ¿Cuántas horas de uso lleva el compresor desde la última inspección preventiva, con el horómetro actual?", "1690-1250", "Se resta la hora de la última inspección al valor actual del horómetro.", " horas"),
        ("=", "{F} ¿Cuántas horas de atraso tiene la inspección preventiva, comparando el horómetro actual con la hora en que correspondía?", "1690-(1250+250)", "Se resta la hora de vencimiento al valor actual del horómetro.", " horas"),
        ("abc", "{F} ¿Qué corresponde con una inspección preventiva atrasada?", "Informar al supervisor para programarla pronto con una orden de trabajo", "Dejarla para cuando falle el equipo", "Anotar que ya se hizo", "Un atraso se informa y se corrige; los registros deben ser veraces."),
        ("abc", "{F} Un compañero dice: «si el filtro cambiado a las 1.000 horas sigue bien, no hace falta anotar nada más». ¿Qué respuesta es correcta?", "Es falso: toda intervención e inspección se anota en la hoja de vida", "Es cierto, si el filtro está limpio", "Es cierto, si lo recuerda de memoria", "Sin registro no hay historia confiable del equipo."),
        ("abc", "¿Qué función tiene el operador en el mantenimiento?", "Inspeccionar a diario y avisar de anomalías", "Reparar cualquier falla por su cuenta", "Cambiar el plan de mantenimiento", "El operador es la primera línea de detección, no el reparador."),
        ("abc", "En las 5S de ejemplo, ¿qué significa «clasificar»?", "Separar lo necesario de lo que sobra en el lugar de trabajo", "Pintar las paredes del taller", "Registrar las horas de uso", "Clasificar es la primera S: se retira lo innecesario."),
        ("=", "{F} Si el plan pidiera la inspección cada 200 horas en lugar de 250, ¿a qué hora correspondería la siguiente desde la última de 1.250?", "1250+200", "Se suma la nueva frecuencia a la hora de la última inspección.", " horas"),
    ],
    ctx=("abc", "El supervisor de ejemplo te pide anotar «inspección hecha» en la hoja de vida, aunque no se hizo. ¿Qué respondes?", "Que no puedo anotar algo que no ocurrió: la inspección se programa y se registra cuando se hace", "Que sí, para no atrasar los informes", "Que sí, pero con una fecha anterior", "Un registro falso quita confianza al mantenimiento y puede ocultar un riesgo."),
    sc=[
        ("En Montaje Industrial: ¿qué registra la hoja de vida de un equipo?", "Sus inspecciones, cambios y fallas", "Es la historia registrada del equipo en el tiempo."),
        ("¿Cómo se calcula cuándo corresponde la siguiente inspección por horas de uso?", "Hora de la última inspección más la frecuencia", "La frecuencia se cuenta desde la última."),
        ("¿Qué hace el operador ante una anomalía?", "Avisa al supervisor o al técnico", "El operador detecta anomalías y las reporta al supervisor."),
    ],
    op=("Hoja de vida de ejemplo del equipo T-1: a las 800 horas, inspección preventiva; a las 950 horas, falla de un rodamiento; a las 950 horas, cambio del rodamiento. Plan: inspección cada 300 horas. Horómetro actual: 1.200 horas. Escribe (a) a qué hora corresponde la siguiente inspección, (b) si está atrasada y por cuántas horas, (c) qué tipo de mantenimiento fue el cambio del rodamiento, (d) qué harías con el atraso.",
        "(a) 800 + 300 = 1.100 horas. (b) Sí: 1.200 − 1.100 = 100 horas de atraso. (c) Correctivo, porque ocurrió después de una falla. (d) Informar al supervisor para programarla con una orden de trabajo, sin alterar el registro.",
        ["calcula la hora de vencimiento", "calcula el atraso", "clasifica el cambio", "propone informar y programar"],
        ["hoja con las cuatro respuestas"],
        ["contar la frecuencia desde 0", "decir que no hay atraso", "proponer anotar la inspección como hecha"],
        "Pregunta: «¿desde qué hora se cuenta la frecuencia?». Si no responde, pídele que relea el ejemplo de la próxima inspección."),
    reinforce="Inventa una hoja de vida de tres registros para una herramienta y calcula cuándo vence su próxima inspección.",
    extend="Explica con un ejemplo por qué un lugar ordenado con las 5S es también un lugar más seguro.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Equipo D-1, mes de ejemplo: 200 horas programadas de trabajo. Paradas del mes: 12 horas por mantenimiento preventivo y 8 horas por una falla. "
     "Costo de ejemplo: cada hora de parada preventiva cuesta $20.000 y cada hora de parada por falla cuesta $60.000 (incluye la producción perdida). Disponibilidad = horas en que el equipo pudo trabajar, divididas por las horas programadas, por 100. "
     "Alternativa de ejemplo: aumentar el mantenimiento preventivo a 18 horas al mes, lo que evitaría la falla.")
build(
    O8, 3, F,
    use="Aprenderé a analizar un caso de mantenimiento, a calcular la disponibilidad de un equipo y el costo de las paradas y a comparar el mantenimiento preventivo con el correctivo.",
    prior=["Sé qué es el mantenimiento preventivo y el correctivo.", "Sé calcular un porcentaje simple.", "Sé multiplicar y sumar números enteros."],
    explain=[
        "La disponibilidad mide qué parte del tiempo programado un equipo pudo trabajar. Se calcula restando a las horas programadas las horas de parada, y dividiendo el resultado entre las horas programadas, por 100. Una parada preventiva se programa y su costo es conocido; una parada por falla es inesperada y suele costar más, porque se pierde producción y se repara con urgencia.",
        "Para decidir cuánto mantenimiento preventivo conviene, se compara el costo de las paradas preventivas con el de las fallas que evitan. Esta comparación es un criterio de planificación y no reemplaza lo que indica el manual del fabricante ni lo que decide el supervisor. En seguridad, una falla repentina también es un riesgo para las personas, no solo un costo.",
        f"Estas cifras son de ejemplo para practicar el cálculo. {EMER} {AVISO}",
    ],
    vocab=[("disponibilidad", "porcentaje del tiempo programado en que un equipo pudo trabajar"), ("parada preventiva", "parada programada para hacer mantenimiento preventivo"), ("parada por falla", "parada inesperada por una falla"), ("horas programadas", "horas en que se espera que el equipo trabaje"), ("producción perdida", "lo que se deja de producir mientras el equipo está detenido")],
    worked=[
        ("Calcular la disponibilidad", "Un equipo de ejemplo tiene 100 horas programadas y 10 horas de parada. ¿Qué disponibilidad tiene?", ["Pudo trabajar 100 menos 10, es decir 90 horas.", "90 por 100 entre 100 es 90 %."], "90 %"),
        ("Costo de una parada", "Una parada de ejemplo dura 5 horas y cada hora cuesta $30.000. ¿Cuánto cuesta?", ["Se multiplican las horas por el costo de cada hora.", "5 por 30.000 son 150.000."], "150.000 pesos"),
    ],
    mistakes=[("Medir la disponibilidad dividiendo las horas de parada entre las programadas.", "Eso da el porcentaje de parada y no el de disponibilidad.", "Divide las horas en que pudo trabajar entre las programadas."),
              ("Creer que no hacer mantenimiento preventivo siempre ahorra dinero.", "Las fallas suelen costar más y exponen a las personas.", "Compara costos y riesgos antes de recortar mantenimiento.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué mide la disponibilidad de un equipo?", "La parte del tiempo programado en que pudo trabajar", "El precio que costó el equipo", "La cantidad de piezas que produce por hora", "La disponibilidad compara horas trabajadas posibles con horas programadas."),
        ("abc", "En Montaje Industrial: ¿por qué una parada por falla suele costar más que una preventiva?", "Porque es inesperada, se pierde producción y se repara con urgencia", "Porque el repuesto siempre es más caro", "Porque dura menos tiempo", "La urgencia y la producción perdida encarecen la falla."),
        ("abc", "En Montaje Industrial: ¿qué indica la frase «horas programadas»?", "Las horas en que se espera que el equipo trabaje", "Las horas en que el equipo está en mantenimiento", "Las horas de descanso del operador", "Las horas programadas son la base para medir la disponibilidad."),
        ("=", "{F} ¿Cuántas horas pudo trabajar el equipo D-1 en el mes?", "200-12-8", "Se restan las dos paradas a las horas programadas.", " horas"),
        ("=", "{F} ¿Qué disponibilidad tuvo el equipo D-1 en el mes?", "(200-12-8)*100//200", "Se divide las horas disponibles entre las programadas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuánto costó la parada preventiva del mes?", "12*20000", "Se multiplican las horas de parada por el costo de cada hora.", " pesos"),
        ("=", "{F} ¿Cuánto costó la parada por falla del mes?", "8*60000", "Se multiplican las horas de parada por el costo de cada hora.", " pesos"),
        ("=", "{F} ¿Cuánto costaron las dos paradas del mes juntas?", "12*20000+8*60000", "Se suman los costos de la parada preventiva y de la parada por falla.", " pesos"),
        ("=", "{F} ¿Cuánto costaría la parada preventiva si se aumentara a 18 horas al mes?", "18*20000", "Se multiplican las horas de parada preventiva por el costo de cada hora.", " pesos"),
        ("abc", "{F} Si la alternativa evitara la falla, ¿qué ocurriría con el costo mensual de paradas?", "Bajaría de 720.000 a 360.000 pesos", "Subiría de 360.000 a 720.000 pesos", "Se mantendría igual", "El costo con la falla es 720.000 y con la alternativa solo 360.000."),
        ("abc", "{F} Un compañero dice: «si no hacemos mantenimiento, la disponibilidad sube porque el equipo no se detiene». ¿Qué respuesta es correcta?", "Es falso: sin mantenimiento aumentan las fallas y la disponibilidad real baja", "Es cierto, si el equipo es nuevo", "Es cierto, mientras no se escuche ruido", "Las fallas generan paradas más largas y peligrosas que el mantenimiento programado."),
        ("abc", "{F} ¿Qué otro factor, además del costo, conviene considerar al comparar ambas alternativas?", "El riesgo para las personas de una falla repentina del equipo", "El color del equipo", "El nombre del proveedor", "Una falla repentina también puede lesionar a quien trabaja con el equipo."),
        ("=", "{F} ¿Cuántos pesos se ahorrarían al mes con la alternativa, respecto del costo actual de las paradas?", "(12*20000+8*60000)-18*20000", "Se resta el costo de la alternativa al costo actual de las dos paradas.", " pesos"),
    ],
    ctx=("abc", "El jefe de ejemplo te dice: «recorta el mantenimiento preventivo, total solo cuesta». ¿Qué respondes con los datos de la ficha?", "Que hay que comparar: en el caso de ejemplo, una falla costó más que el preventivo y además era un riesgo para las personas", "Que sí, porque lo preventivo nunca sirve", "Que sí, mientras el equipo siga funcionando", "Las cifras del caso muestran que la falla puede costar más que prevenirla."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula la disponibilidad?", "Horas en que pudo trabajar entre horas programadas, por 100", "Mide qué parte del tiempo programado trabajó."),
        ("¿Qué parada suele costar más, la preventiva o la de falla?", "La parada por falla", "Es inesperada y se pierde producción."),
        ("¿Qué riesgo agrega una falla repentina?", "Un riesgo de lesión para las personas", "No es solo un costo económico."),
    ],
    op=("Caso de ejemplo: el equipo K-1 tuvo 160 horas programadas en un mes, con 4 horas de parada preventiva y 12 horas de parada por falla. Costo de ejemplo: $15.000 por hora preventiva y $50.000 por hora de falla. Escribe (a) las horas en que pudo trabajar, (b) la disponibilidad, (c) el costo total de las dos paradas, (d) una razón de seguridad para evitar fallas.",
        "(a) 160 − 4 − 12 = 144 horas. (b) 144 × 100 ÷ 160 = 90 %. (c) 4 × 15.000 + 12 × 50.000 = 60.000 + 600.000 = 660.000 pesos. (d) Una falla repentina puede lesionar a quien trabaja con el equipo.",
        ["calcula las horas trabajadas", "calcula la disponibilidad", "calcula el costo total", "da una razón de seguridad"],
        ["hoja con los cuatro cálculos"],
        ["dividir las horas de parada", "olvidar una de las paradas", "ver la falla solo como costo"],
        "Pregunta: «¿qué horas se restan de las programadas?». Si no responde, pídele que relea el cálculo de la disponibilidad."),
    reinforce="Calcula la disponibilidad de un equipo con 100 horas programadas y 15 horas de parada.",
    extend="Explica con un ejemplo por qué una parada programada puede ser mejor que una falla aunque dure lo mismo.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (planificación de ejemplo, inventada). Equipo G-1: mantenimiento cada 250 horas de uso; la última fue a las 1.000 horas; horómetro actual: 1.190 horas; uso de 20 horas por semana. "
     "Instrumento I-1: calibración cada 12 meses; su certificado vence al final del mes 9 y hoy es el final del mes 7. Mantenimientos del año con cambio de filtro: 8; filtros en bodega: 3; precio de ejemplo: $4.500 por filtro.")
build(
    O8, 4, F,
    use="Aprenderé a programar mantenimientos por horas de uso y calibraciones por fecha, a calcular repuestos por comprar y su costo y a mantener la planificación al día sin alterar registros.",
    prior=["Sé qué es una hoja de vida y un horómetro.", "Sé qué es un certificado de calibración.", "Sé dividir y multiplicar números enteros."],
    explain=[
        "Para programar el mantenimiento por horas de uso, se calcula la hora de vencimiento sumando la frecuencia a la última intervención, se resta el horómetro actual para saber cuántas horas faltan y se divide entre las horas de uso por semana para saber en cuántas semanas llega. Las calibraciones de los instrumentos se programan por fecha: se resta el mes actual al mes de vencimiento y se agenda la calibración antes de que venza, porque un instrumento con certificado vencido no se usa en controles formales.",
        "Los repuestos se calculan comparando lo que se necesitará con lo que hay en bodega: si hay menos de lo necesario, la diferencia se compra. Una buena planificación evita compras de apuro, paradas innecesarias y mantenimientos atrasados. El plan se ajusta con el supervisor, y los registros solo se corrigen para reflejar lo que realmente ocurrió.",
        f"Estos cálculos son de planilla y de ejemplo; las frecuencias reales las fija el manual del fabricante y el plan de la empresa. {EMER} {AVISO}",
    ],
    vocab=[("hora de vencimiento", "hora de uso en que corresponde el siguiente mantenimiento"), ("calibración programada", "calibración agendada antes de que venza el certificado"), ("repuesto por comprar", "diferencia entre lo necesario y lo que hay en bodega"), ("planificación", "ordenar con anticipación qué se hará, cuándo y con qué recursos"), ("stock", "cantidad de repuestos disponibles en bodega")],
    worked=[
        ("Semanas que faltan", "Un equipo de ejemplo debe mantenerse a las 2.000 horas, el horómetro marca 1.940 y se usa 15 horas por semana. ¿En cuántas semanas llega?", ["Faltan 2.000 menos 1.940, es decir 60 horas.", "60 entre 15 son 4 semanas."], "4 semanas"),
        ("Repuestos por comprar", "Se necesitan 10 sellos de ejemplo y hay 4 en bodega. ¿Cuántos hay que comprar?", ["Se resta lo disponible a lo necesario.", "10 menos 4 son 6."], "6 sellos"),
    ],
    mistakes=[("Contar la frecuencia desde cero y no desde la última intervención.", "El vencimiento se corre y el mantenimiento se hace tarde o temprano.", "Suma la frecuencia a la hora de la última intervención."),
              ("Dejar vencer el certificado de un instrumento y seguir usándolo.", "Sus lecturas quedan en duda y no sirven en controles formales.", "Agenda la calibración antes del vencimiento.")],
    T=[
        ("abc", "En Montaje Industrial: ¿cómo se calcula la hora de vencimiento del siguiente mantenimiento?", "Se suma la frecuencia a la hora de la última intervención", "Se resta la frecuencia al horómetro actual", "Se multiplica el horómetro por la frecuencia", "El vencimiento se cuenta desde la última intervención."),
        ("abc", "En Montaje Industrial: ¿cuándo se agenda la calibración de un instrumento?", "Antes de que venza su certificado", "Después de que falle", "Solo cuando el jefe lo recuerde", "Un certificado vencido deja el instrumento sin uso en controles formales."),
        ("abc", "En Montaje Industrial: ¿qué es el stock de repuestos?", "La cantidad de repuestos disponibles en bodega", "El precio de los repuestos", "La lista de equipos a mantener", "El stock se compara con lo necesario para saber qué comprar."),
        ("=", "{F} ¿A qué hora de uso corresponde el siguiente mantenimiento de G-1?", "1000+250", "Se suma la frecuencia a la hora de la última intervención.", " horas"),
        ("=", "{F} ¿Cuántas horas de uso faltan para el siguiente mantenimiento de G-1?", "1000+250-1190", "Se resta el horómetro actual a la hora de vencimiento.", " horas"),
        ("=", "{F} ¿En cuántas semanas llega G-1 al siguiente mantenimiento?", "(1000+250-1190)//20", "Se dividen las horas que faltan entre las horas de uso por semana.", " semanas"),
        ("=", "{F} ¿Cuántos meses faltan para que venza el certificado de I-1?", "9-7", "Se resta el mes actual al mes de vencimiento.", " meses"),
        ("=", "{F} ¿Cuántos filtros hay que comprar para los mantenimientos del año?", "8-3", "Se resta lo disponible en bodega a lo necesario.", " filtros"),
        ("=", "{F} ¿Cuánto cuestan los filtros que hay que comprar?", "(8-3)*4500", "Se multiplican los filtros por comprar por el precio de cada uno.", " pesos"),
        ("abc", "{F} ¿Qué corresponde hacer con la calibración de I-1?", "Agendarla antes de que termine el mes 9", "Esperar a que venza para ver si falla", "Seguir usándolo con el certificado vencido", "Se agenda con anticipación para no quedar sin instrumento."),
        ("abc", "{F} Un compañero dice: «G-1 se mantiene a las 1.250 horas, pero si pasa un poco no pasa nada». ¿Qué respuesta es correcta?", "Hay que programar la intervención antes o en esa hora; atrasarla aumenta el riesgo de falla", "Es cierto, porque la frecuencia es solo una sugerencia", "Es cierto si el equipo se oye normal", "El plan se cumple; los atrasos se informan y se reprograman."),
        ("=", "{F} Si el uso subiera a 30 horas por semana, ¿en cuántas semanas llegaría G-1 al siguiente mantenimiento?", "(1000+250-1190)//30", "Se dividen las horas que faltan entre las nuevas horas de uso por semana.", " semanas"),
        ("abc", "{F} Se descubre que en la bodega hay 3 filtros, pero 1 está dañado. ¿Qué corresponde?", "Contar 2 filtros utilizables y actualizar el stock y la compra", "Contar los 3 para no complicar", "Usar el dañado igual", "El stock debe reflejar lo realmente utilizable."),
    ],
    ctx=("abc", "El supervisor de ejemplo te pide: «anota que I-1 se calibró este mes, para que no se bloquee el uso del instrumento». No se ha calibrado. ¿Qué respondes?", "Que no puedo anotar eso: la calibración se agenda y se registra cuando se hace", "Que sí, para evitar bloqueos", "Que sí, si se calibra después", "Un registro falso deja al instrumento sin respaldo y falsea todos los controles que use."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calculan las semanas que faltan para un mantenimiento por horas?", "Horas que faltan divididas por horas de uso semanales", "Se convierte el tiempo restante a semanas."),
        ("¿Cuándo se agenda la calibración de un instrumento?", "Antes de que venza su certificado", "Así no se queda sin instrumento calibrado."),
        ("¿Cómo se calculan los repuestos por comprar?", "Necesarios menos los que hay en bodega", "Se compra solo la diferencia entre lo necesario y lo disponible."),
    ],
    op=("Ficha de ejemplo: el equipo H-1 se mantiene cada 400 horas; la última fue a las 2.000 horas; el horómetro marca 2.300; se usa 25 horas por semana. El instrumento I-2 vence al final del mes 11 y hoy es el final del mes 8. Se necesitan 6 sellos y hay 2 en bodega, a $3.000 cada uno. Escribe (a) la hora del siguiente mantenimiento de H-1, (b) en cuántas semanas llega, (c) cuántos meses faltan para el vencimiento de I-2, (d) cuántos sellos se compran y cuánto cuestan.",
        "(a) 2.000 + 400 = 2.400 horas. (b) Faltan 100 horas; 100 ÷ 25 = 4 semanas. (c) 11 − 8 = 3 meses. (d) 6 − 2 = 4 sellos; 4 × 3.000 = 12.000 pesos.",
        ["calcula el vencimiento", "calcula las semanas", "calcula los meses", "calcula repuestos y costo"],
        ["hoja con los cuatro cálculos"],
        ["contar la frecuencia desde cero", "olvidar restar el horómetro", "comprar todos los sellos sin restar el stock"],
        "Pregunta: «¿desde qué hora se cuenta la frecuencia?». Si no responde, pídele que relea el ejemplo de semanas que faltan."),
    reinforce="Calcula en papel cuántos filtros hay que comprar si se necesitan 12 y hay 5 en bodega.",
    extend="Explica con un ejemplo por qué agendar la calibración antes del vencimiento evita detener controles.",
)

# FIN
