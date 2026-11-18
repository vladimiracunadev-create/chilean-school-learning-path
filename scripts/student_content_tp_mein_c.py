"""Mecánica Industrial (tronco) TP 3.º medio: OAE-06 (higiene, seguridad industrial y medioambiente: conceptos, documentos e indicadores) y OAE-07 (procedimientos y normas de fabricación: documentos, trazabilidad y cálculo). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_mein_common import AVISO, EMER, build

O6 = "TP-MEIN-3-OAE-06"
O7 = "TP-MEIN-3-OAE-07"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Taller Demo» tiene 40 trabajadores. En un año de ejemplo registró 2 accidentes del trabajo con baja, 1 enfermedad profesional sospechada (pérdida de audición por ruido sostenido) "
     "y 6 incidentes sin lesión, también llamados casi accidentes. Agentes presentes en el taller: ruido, polvo metálico, vapores de un solvente de limpieza y aceite en el piso.")
build(
    O6, 1, F,
    use="Aprenderé la diferencia entre accidente del trabajo, enfermedad profesional e incidente, qué buscan la higiene y la seguridad industrial y qué instituciones y comités intervienen.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé la jerarquía de controles.", "Sé que hay normas laborales."],
    explain=[
        "Un accidente del trabajo es una lesión que una persona sufre a causa o con ocasión de su trabajo. Una enfermedad profesional es un daño a la salud causado directamente por el trabajo, como la pérdida de audición por ruido sostenido; aparece con el tiempo. Un incidente o casi accidente es un hecho que pudo causar daño y no lo causó, y sirve para aprender antes de que ocurra uno grave. La higiene industrial se ocupa de los agentes del ambiente que dañan la salud, como el ruido, el polvo o los vapores; la seguridad industrial se ocupa de evitar accidentes.",
        "La Dirección del Trabajo fiscaliza la normativa laboral. El Comité Paritario de Higiene y Seguridad reúne representantes de la empresa y de los trabajadores para vigilar la prevención. El reglamento interno de orden, higiene y seguridad fija las reglas de cada empresa. El cuidado del medio ambiente evita que residuos, derrames y emisiones dañen el entorno, y se rige por la norma vigente.",
        f"Todo accidente o incidente se informa. {EMER} {AVISO}",
    ],
    vocab=[("accidente del trabajo", "lesión que sufre una persona a causa o con ocasión de su trabajo"), ("enfermedad profesional", "daño a la salud causado directamente por el trabajo"), ("incidente", "hecho que pudo causar daño y no lo causó"), ("higiene industrial", "estudio y control de los agentes del ambiente que dañan la salud"), ("seguridad industrial", "prevención de accidentes en el trabajo"), ("Comité Paritario", "grupo de representantes de la empresa y de los trabajadores que vigila la prevención")],
    worked=[
        ("Clasificar un hecho", "Una persona de ejemplo se corta una mano mientras trabaja en un taller. ¿Es accidente, enfermedad profesional o incidente?", ["Hay una lesión producida en el trabajo.", "Es un accidente del trabajo."], "Accidente del trabajo"),
        ("Clasificar otro hecho", "Una pieza de ejemplo cae a un metro de una persona, sin tocarla. ¿Qué es?", ["Pudo causar daño y no lo causó.", "Es un incidente."], "Incidente"),
    ],
    mistakes=[("No informar un incidente porque «no pasó nada».", "Un incidente muestra una condición peligrosa que puede causar un accidente.", "Todo incidente se informa para corregir la causa."),
              ("Llamar enfermedad profesional a una lesión inmediata.", "La enfermedad profesional aparece con el tiempo por una exposición.", "Distingue lesión inmediata (accidente) de daño por exposición.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es una enfermedad profesional?", "Un daño a la salud causado directamente por el trabajo", "Una lesión inmediata por un golpe en un taller", "Una enfermedad cualquiera que tiene un trabajador", "La enfermedad profesional se debe al trabajo y aparece con la exposición."),
        ("abc", "En Mecánica Industrial: ¿qué es un incidente?", "Un hecho que pudo causar daño y no lo causó", "Una lesión grave en un taller", "Una enfermedad por ruido", "El incidente no produce lesión, pero avisa de un peligro."),
        ("abc", "En Mecánica Industrial: ¿qué reúne el Comité Paritario de Higiene y Seguridad?", "Representantes de la empresa y de los trabajadores", "Solo a los dueños de la empresa", "Solo a los inspectores del Estado", "Paritario significa que participan ambas partes."),
        ("=", "{F} ¿Cuántos hechos suman los accidentes con baja y los incidentes sin lesión del año?", "2+6", "Se suman los accidentes y los incidentes.", " hechos"),
        ("abc", "{F} Un hecho del caso es «pérdida de audición por ruido sostenido». ¿Cómo se clasifica?", "Enfermedad profesional sospechada", "Accidente del trabajo", "Incidente", "Es un daño por exposición que aparece con el tiempo."),
        ("abc", "{F} ¿Cuál agente de la lista es objeto de la higiene industrial?", "Los vapores del solvente de limpieza", "La puerta de un casillero", "El cartel de la entrada", "Los vapores son un agente del ambiente que daña la salud."),
        ("=", "{F} Un indicador de ejemplo es accidentes con baja por cada 100 trabajadores. ¿Cuánto vale con los datos de la ficha?", "2*100//40", "Se multiplican los accidentes por 100 y se dividen por los trabajadores.", " accidentes por cada 100 trabajadores"),
        ("=", "{F} Se propone dar una charla de seguridad a todos los trabajadores en grupos de 8 personas. ¿Cuántos grupos se necesitan?", "40//8", "Se dividen los trabajadores entre las personas de cada grupo.", " grupos"),
        ("abc", "{F} El aceite en el piso pasa a la matriz de peligros. ¿Cuál es el riesgo asociado?", "Que alguien resbale y se lesione", "Que el aceite se acabe", "Que el piso cambie de color", "El riesgo es el daño posible que produce el peligro."),
        ("abc", "{F} Un compañero dice: «los 6 incidentes no cuentan porque nadie se lesionó». ¿Qué respuesta es correcta?", "Es falso: los incidentes se informan y se analizan porque avisan de peligros antes de un accidente", "Es cierto, porque sin lesión no hay nada que informar", "Es cierto, si ocurrieron en horario de colación", "Los incidentes permiten corregir causas antes de un daño."),
        ("abc", "En una visita a un taller de ejemplo, una persona cae al piso y no responde. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Moverla rápidamente a otro lugar", "Darle algo de beber", "Mover o dar líquidos sin formación puede agravar el daño; se pide ayuda."),
        ("=", "{F} Para el ruido se compran protectores auditivos y se entregan 2 pares por trabajador al año. ¿Cuántos pares se compran para los 40 trabajadores?", "40*2", "Se multiplican los trabajadores por los pares de cada uno.", " pares"),
        ("abc", "En Mecánica Industrial: ¿qué institución fiscaliza el cumplimiento de la normativa laboral en un taller?", "La Dirección del Trabajo", "El Servicio de Impuestos Internos", "El Instituto Nacional de Estadísticas", "La Dirección del Trabajo fiscaliza lo laboral; las otras instituciones tienen funciones tributarias y estadísticas."),
    ],
    ctx=("abc", "En un taller de ejemplo, un compañero dice: «mejor no avisar del casi accidente, para que no nos reten». Como estudiante, ¿qué propones?", "Informarlo, porque un incidente permite corregir una causa antes de que alguien se lesione", "Callar para evitar problemas", "Esperar a que ocurra un accidente grave", "Informar el incidente es parte de la prevención."),
    sc=[
        ("En Mecánica Industrial: ¿qué es un accidente del trabajo?", "Una lesión que ocurre a causa o con ocasión del trabajo", "El accidente produce una lesión inmediata en el trabajo."),
        ("En Mecánica Industrial: ¿qué se ocupa de evitar accidentes?", "La seguridad industrial", "La higiene se ocupa de los agentes del ambiente."),
        ("En Mecánica Industrial: ¿qué se hace con un incidente?", "Se informa y se analiza", "El incidente avisa de un peligro que se debe corregir."),
    ],
    op=("Ficha de ejemplo: en un taller de 25 trabajadores hubo 1 accidente con baja, 4 incidentes sin lesión y 1 caso de pérdida de audición por ruido sostenido. Escribe (a) cómo clasificas cada tipo de hecho, (b) cuántos accidentes con baja hubo por cada 100 trabajadores, (c) qué harías con los incidentes, (d) qué agente del ambiente es el del caso de la audición.",
        "(a) El accidente con baja es accidente del trabajo; los 4 sin lesión son incidentes; la pérdida de audición es enfermedad profesional sospechada. (b) 1 × 100 ÷ 25 = 4 por cada 100 trabajadores. (c) Informarlos y analizar sus causas para corregirlas. (d) El ruido.",
        ["clasifica los hechos", "calcula el indicador", "propone informar y analizar", "nombra el agente"],
        ["hoja con las cuatro respuestas"],
        ["llamar enfermedad profesional a un accidente", "calcular mal el indicador", "proponer callar los incidentes"],
        "Pregunta: «¿la lesión ocurrió de golpe o con el tiempo?». Si duda, pídele que relea las definiciones."),
    reinforce="Escribe un ejemplo inventado de accidente, uno de incidente y uno de enfermedad profesional.",
    extend="Explica con un ejemplo por qué un incidente sin lesión puede ser más útil para prevenir que ignorarlo.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (señales y documentos de ejemplo, inventados). Código de señales de ejemplo: prohibición, círculo rojo con una diagonal; advertencia, triángulo amarillo; obligación, círculo azul; emergencia y evacuación, cuadrado o rectángulo verde. "
     "Señales del taller: S1 «no fumar», S2 «peligro: cargas suspendidas», S3 «uso obligatorio de protección auditiva», S4 «salida de emergencia». "
     "Documento A: hoja de datos de seguridad de un solvente de ejemplo, que informa peligros, primeros auxilios generales y almacenamiento. Documento B: registro de entrega de EPP, con nombre, fecha y firma. Documento C: matriz de peligros.")
build(
    O6, 2, F,
    use="Aprenderé a leer señales, la hoja de datos de seguridad, el registro de EPP y la matriz de peligros, y qué rol cumple cada persona de la prevención.",
    prior=["Sé qué es un peligro y un control.", "Sé qué es un EPP.", "Sé leer una lista con códigos."],
    explain=[
        "Las señales de seguridad usan colores y formas que se entienden sin leer: las de prohibición son círculos rojos con una diagonal, las de advertencia son triángulos amarillos, las de obligación son círculos azules y las de emergencia son verdes. La hoja de datos de seguridad (HDS) describe un producto químico: sus peligros, cómo almacenarlo y las medidas generales ante un accidente. El registro de entrega de EPP deja constancia de quién recibió qué y cuándo.",
        "La matriz de peligros lista los peligros de un lugar y sus controles. El prevencionista de riesgos asesora y vigila la prevención, el Comité Paritario revisa y propone mejoras, la supervisión hace cumplir las reglas del área y cada trabajador debe cumplirlas y avisar de las condiciones inseguras. Las personas tienen derecho a ser informadas de los riesgos de su trabajo.",
        f"Los documentos se leen y se respetan; este cuaderno no enseña a manipular productos químicos. {EMER} {AVISO}",
    ],
    vocab=[("señal de prohibición", "círculo rojo con una diagonal que indica algo que no se debe hacer"), ("señal de advertencia", "triángulo amarillo que avisa de un peligro"), ("señal de obligación", "círculo azul que indica algo que se debe hacer"), ("señal de emergencia", "señal verde que indica salidas o ayuda"), ("hoja de datos de seguridad", "documento que informa peligros y almacenamiento de un producto químico"), ("prevencionista de riesgos", "profesional que asesora y vigila la prevención")],
    worked=[
        ("Leer una señal", "Un cartel de ejemplo muestra un triángulo amarillo con un rayo. ¿Qué tipo de señal es?", ["El triángulo amarillo es la forma de una advertencia.", "Avisa de un peligro, en este caso eléctrico."], "Señal de advertencia"),
        ("Elegir un documento", "Una persona de ejemplo quiere saber cómo almacenar un producto químico. ¿Qué documento consulta?", ["Necesita información de peligros y almacenamiento.", "Eso lo informa la hoja de datos de seguridad."], "La hoja de datos de seguridad"),
    ],
    mistakes=[("Ignorar una señal de advertencia porque «ya conozco el lugar».", "La señal avisa de peligros aunque el lugar sea conocido.", "Respeta todas las señales y avisa si faltan o están dañadas."),
              ("Usar un producto sin consultar su hoja de datos de seguridad.", "Se desconocen sus peligros y su almacenamiento.", "Consulta la HDS antes de cualquier tarea con ese producto, con personal autorizado.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué forma y color tiene una señal de prohibición?", "Círculo rojo con una diagonal", "Triángulo amarillo", "Círculo azul", "La prohibición se marca con círculo rojo y diagonal."),
        ("abc", "En Mecánica Industrial: ¿qué informa una hoja de datos de seguridad?", "Peligros, almacenamiento y medidas generales ante un accidente con el producto", "El precio y el proveedor del producto", "Cuántas personas trabajan con el producto", "La HDS describe el producto y sus peligros."),
        ("abc", "En Mecánica Industrial: ¿qué es un registro de entrega de EPP?", "Un documento con nombre, fecha y firma de quien recibió el EPP", "Un plano del lugar donde se guarda el EPP", "La lista de peligros del taller", "El registro deja constancia de la entrega."),
        ("abc", "{F} ¿Qué tipo de señal es S2 «peligro: cargas suspendidas»?", "De advertencia, un triángulo amarillo", "De prohibición, un círculo rojo", "De emergencia, un cuadrado verde", "S2 avisa de un peligro, por lo que es una advertencia."),
        ("abc", "{F} ¿Qué tipo de señal es S3 «uso obligatorio de protección auditiva»?", "De obligación, un círculo azul", "De advertencia, un triángulo amarillo", "De prohibición, un círculo rojo", "S3 indica algo que se debe hacer."),
        ("abc", "{F} ¿Qué señal del taller se representa con un rectángulo verde?", "S4 «salida de emergencia»", "S1 «no fumar»", "S2 «peligro: cargas suspendidas»", "Las señales de emergencia y evacuación son verdes."),
        ("=", "{F} El taller tiene 4 señales distintas y cada una se repite en 3 sectores. ¿Cuántos carteles se necesitan?", "4*3", "Se multiplican las señales por los sectores.", " carteles"),
        ("=", "{F} El registro B muestra que en un mes se entregaron 18 pares de guantes, 12 protectores auditivos y 9 caretas. ¿Cuántos EPP se entregaron en total?", "18+12+9", "Se suman las entregas de los tres elementos.", " elementos"),
        ("abc", "{F} Una persona necesita saber qué hacer en general si el solvente salpica a alguien. ¿Qué documento consulta?", "El documento A, la hoja de datos de seguridad", "El documento B, el registro de entrega de EPP", "El documento C, la matriz de peligros", "La HDS informa medidas generales ante un accidente con el producto."),
        ("abc", "{F} Un supervisor dice: «la señal S1 está rota; da lo mismo, todos saben que no se fuma». ¿Qué respuesta es correcta?", "Es falso: la señal debe repararse o reponerse y avisarse si falta", "Es cierto, porque la señal no importa", "Es cierto, si hay otra en el pasillo", "Las señales comunican el riesgo a todos, incluidas personas nuevas."),
        ("abc", "{F} Un trabajador nuevo dice que no sabe qué hacer con el solvente. ¿Qué corresponde?", "Pedir la hoja de datos de seguridad y la inducción antes de cualquier tarea, con personal autorizado", "Probar con poca cantidad para ver qué pasa", "Preguntar a un compañero de otro turno que lo vio una vez", "Las personas tienen derecho a ser informadas de los riesgos antes de trabajar."),
        ("=", "{F} El taller imprime la HDS del solvente en 3 copias por sector y tiene 5 sectores. ¿Cuántas copias imprime?", "3*5", "Se multiplican las copias por los sectores.", " copias"),
        ("abc", "En una visita a un taller de ejemplo, un producto químico se derrama y una persona tose y se lagrimea. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a recoger el producto con un trapo", "Mezclarlo con otro líquido para neutralizarlo", "Un derrame de químicos exige personal formado; tú avisas."),
    ],
    ctx=("abc", "En una charla de ejemplo, un compañero cree que «la señal verde significa que se puede entrar a cualquier lado». ¿Qué le explicas?", "Que el verde señala salidas y ayuda en una emergencia, no permiso de entrada", "Que tiene razón", "Que el verde es una prohibición", "Las señales verdes son de emergencia y evacuación."),
    sc=[
        ("En Mecánica Industrial: ¿qué color tienen las señales de obligación?", "Azul", "Las señales de obligación son círculos azules."),
        ("En Mecánica Industrial: ¿qué documento informa sobre los peligros de un producto químico?", "La hoja de datos de seguridad", "La HDS describe peligros y almacenamiento."),
        ("En Mecánica Industrial: ¿quién asesora y vigila la prevención en una empresa?", "El prevencionista de riesgos", "Es el profesional encargado de asesorar la prevención."),
    ],
    op=("Ficha de ejemplo: un taller tiene estas señales: R1 «prohibido el paso», R2 «peligro: piso resbaladizo», R3 «uso obligatorio de casco» y R4 «punto de reunión». Escribe (a) el tipo de cada señal, (b) su color y forma, (c) cuántos carteles se necesitan si cada señal se repite en 3 puertas, (d) qué documento consultarías para conocer los peligros de un producto químico.",
        "(a) y (b) R1 prohibición, círculo rojo con diagonal; R2 advertencia, triángulo amarillo; R3 obligación, círculo azul; R4 emergencia, verde. (c) 4 × 3 = 12 carteles. (d) La hoja de datos de seguridad del producto.",
        ["clasifica las señales", "asocia color y forma", "calcula los carteles", "nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["confundir advertencia con prohibición", "calcular mal los carteles", "nombrar un documento equivocado"],
        "Pregunta: «¿la señal dice qué no hacer, qué avisa o qué hacer?». Si duda, pídele que relea los colores."),
    reinforce="Dibuja cuatro señales de ejemplo con su color y forma y escribe qué indica cada una.",
    extend="Explica con un ejemplo por qué una señal dañada debe reponerse aunque todos conozcan el lugar.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (informe de incidente de ejemplo, inventado). Hecho: una persona resbaló sobre aceite en el pasillo junto a una máquina y no se lesionó (incidente). Datos del informe: la máquina gotea aceite desde hace una semana; "
     "no hay bandeja bajo la máquina; la limpieza del pasillo no figura en ninguna pauta; el mantenimiento de la máquina está atrasado 15 días; la persona iba apurada y llevaba calzado común. El aceite del piso se recogió con trapos. Medidas propuestas por el equipo: M1, instalar una bandeja de contención bajo la máquina; M2, inspección diaria del pasillo; M3, entregar calzado antideslizante; M4, reponer la pauta de mantenimiento de la máquina.")
build(
    O6, 3, F,
    use="Aprenderé a analizar en papel un incidente: separar hechos, causas inmediatas y de fondo, elegir medidas por nivel de la jerarquía y cuidar el medio ambiente.",
    prior=["Sé qué es un incidente.", "Sé la jerarquía de controles.", "Sé la diferencia entre causa inmediata y de fondo."],
    explain=[
        "Un informe de incidente describe qué pasó, dónde y cuándo, y separa los hechos de las opiniones. La causa inmediata es lo que produjo directamente el hecho; las causas de fondo son las condiciones que lo permitieron, como falta de mantenimiento, de pautas o de contención. No se busca culpar sino corregir el sistema. Las medidas se ordenan por la jerarquía de controles: las de ingeniería primero y las de EPP al final.",
        "El aceite derramado y los trapos con aceite son residuos que se manejan según el plan del taller y la norma vigente: se contienen, se depositan en el punto de acopio y no se vierten al desagüe. Un informe incluye también medidas de seguimiento, con responsable y plazo, y se revisa después para ver si funcionaron.",
        f"El análisis es de papel; no se interviene ninguna máquina. {EMER} {AVISO}",
    ],
    vocab=[("informe de incidente", "documento que describe el hecho y analiza sus causas"), ("contención", "barrera o recipiente que retiene un derrame"), ("seguimiento", "revisión posterior para ver si una medida funcionó"), ("responsable", "persona asignada a ejecutar una medida"), ("plazo", "fecha límite de una medida")],
    worked=[
        ("Causa inmediata", "En un informe de ejemplo, una persona tropieza con una manguera tendida. ¿Cuál es la causa inmediata?", ["Lo que produjo el hecho directamente es la manguera tendida.", "La causa de fondo sería la falta de orden."], "La manguera tendida"),
        ("Medida de ingeniería", "En otro caso de ejemplo se propone instalar una barrera física en vez de entregar un cartel. ¿Qué nivel de la jerarquía de controles representa la barrera?", ["La barrera cambia el lugar.", "Es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Culpar a la persona que resbaló y cerrar el caso.", "Las causas de fondo seguirían presentes y el hecho se repetiría.", "Analiza el sistema y propone medidas sobre las causas."),
              ("Verter el aceite derramado al desagüe para limpiar rápido.", "El aceite daña el medio ambiente y es un residuo.", "Se contiene y se lleva al punto de acopio según la norma.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es una causa de fondo de un incidente?", "Una condición que permitió que el hecho ocurriera", "Lo que produjo el hecho directamente", "La persona a quien se atribuye el hecho", "La causa de fondo explica por qué pudo ocurrir el hecho."),
        ("abc", "En Mecánica Industrial: ¿para qué sirve el seguimiento de una medida?", "Para ver si la medida funcionó", "Para elegir a quién sancionar", "Para archivar el informe sin revisarlo", "El seguimiento comprueba si la medida fue efectiva."),
        ("abc", "En Mecánica Industrial: ¿qué es una contención en el caso de un derrame?", "Una barrera o recipiente que retiene el derrame", "Un cartel que avisa del derrame", "Un trapo que se bota con la basura común", "Contener es retener el derrame para que no se extienda."),
        ("abc", "{F} ¿Cuál es la causa inmediata del incidente de la ficha?", "El aceite derramado sobre el pasillo", "El mantenimiento atrasado", "La falta de una pauta de limpieza", "El aceite en el piso produjo directamente el resbalón."),
        ("abc", "{F} ¿Cuál de estos datos es una causa de fondo?", "La falta de una bandeja bajo la máquina que gotea", "El calzado común de la persona", "El apuro de la persona", "La falta de contención permitió que el aceite llegara al pasillo."),
        ("abc", "{F} ¿Qué tipo de control es la medida M1, la bandeja de contención?", "De ingeniería", "Administrativo", "De EPP", "La bandeja cambia el lugar y retiene el derrame."),
        ("abc", "{F} ¿Qué tipo de control es la medida M3, el calzado antideslizante?", "EPP", "De ingeniería", "De sustitución", "El calzado protege a quien lo usa y no quita el peligro."),
        ("=", "{F} La máquina gotea hace 7 días y el mantenimiento lleva 15 días de atraso. ¿Cuántos días más de atraso que de goteo hay?", "15-7", "Se resta los días de goteo a los de atraso.", " días"),
        ("=", "{F} Un equipo asigna 4 medidas y cada una tarda 2 jornadas de ejemplo en ejecutarse, una después de la otra. ¿Cuántas jornadas toman las 4 medidas?", "4*2", "Se multiplican las medidas por las jornadas de cada una.", " jornadas"),
        ("abc", "{F} Se propone que, para ahorrar, solo se entregue calzado antideslizante y no se instale la bandeja. ¿Qué observación es correcta?", "El calzado no elimina la fuga ni el derrame; conviene instalar la bandeja y además entregar calzado", "Es mejor, porque el calzado es el control más efectivo", "Es mejor, porque la bandeja es solo un cartel", "El EPP es la última barrera y no quita el peligro."),
        ("abc", "{F} Un jefe dice: «la persona iba apurada, es su culpa». ¿Qué respuesta es adecuada?", "El análisis debe incluir las causas de fondo, como la fuga, la falta de pauta y el mantenimiento atrasado", "Tiene razón, y el informe debe cerrarse", "Tiene razón, y hay que sancionar", "Sin corregir las causas de fondo, el hecho puede repetirse."),
        ("abc", "{F} El aceite recogido con trapos debe:", "Llevarse al punto de acopio de residuos según la norma vigente", "Verterse al desagüe", "Botarse a la basura común", "El aceite y los trapos con aceite son residuos con acopio propio."),
        ("=", "{F} Se recogieron 3 kg de trapos con aceite por semana durante 4 semanas hasta reparar la fuga. ¿Cuántos kg de residuo se generaron?", "3*4", "Se multiplican los kg por semana por las semanas.", " kg"),
    ],
    ctx=("abc", "Tras un incidente de ejemplo, el jefe propone «limpiar todo y no escribir nada, para no tener problemas». Como estudiante, ¿qué propones?", "Escribir el informe, analizar las causas y proponer medidas con responsable y plazo", "No escribir nada, porque no hubo lesión", "Escribir solo el nombre de la persona", "El informe permite corregir las causas antes de un daño."),
    sc=[
        ("En Mecánica Industrial: ¿qué nivel de la jerarquía es una bandeja de contención?", "Control de ingeniería", "Cambia el lugar y retiene el derrame."),
        ("En Mecánica Industrial: ¿qué nunca se hace con el aceite derramado?", "Verterlo al desagüe", "El aceite daña el medio ambiente."),
        ("En Mecánica Industrial: ¿qué incluye un informe de incidente además del hecho?", "Causas, medidas, responsables y plazos", "Con eso se corrige el sistema y se hace seguimiento."),
    ],
    op=("Ficha de ejemplo: una pieza cae de un estante sin lesionar a nadie. Datos: el estante estaba sobrecargado; no hay un límite de peso rotulado; el estante no se revisa; la persona dejó la pieza en el borde. Medidas propuestas: N1, rotular el límite de peso; N2, revisión mensual del estante; N3, reforzar el estante con un soporte; N4, pedir a las personas que dejen las piezas al fondo. Escribe (a) la causa inmediata, (b) una causa de fondo, (c) qué medida es de ingeniería, (d) cuál es administrativa.",
        "(a) La pieza dejada en el borde del estante sobrecargado. (b) No hay límite de peso rotulado ni revisión del estante. (c) N3, el soporte, que cambia el lugar. (d) N2, la revisión mensual (también N1 y N4 son administrativas).",
        ["distingue causa inmediata y de fondo", "clasifica medidas por nivel"],
        ["hoja con las cuatro respuestas"],
        ["culpar a la persona", "proponer solo EPP", "confundir ingeniería con administrativa"],
        "Pregunta: «¿esa medida cambia el lugar o ordena una conducta?». Si duda, pídele que relea los niveles de la jerarquía."),
    reinforce="Escribe un incidente inventado con su causa inmediata, una causa de fondo y una medida por nivel.",
    extend="Explica con un ejemplo por qué el seguimiento es parte del informe de un incidente.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (indicadores de seguridad de ejemplo, inventados). Año de ejemplo del «Taller Demo»: promedio de 50 trabajadores. Accidentes con baja: 3. Días perdidos por esos accidentes: 25. Incidentes informados: 20. "
     "Capacitaciones de seguridad: 4 al año de 2 horas cada una, para los 50 trabajadores. Año anterior de ejemplo: 5 accidentes con baja y 60 días perdidos con 50 trabajadores. Meta de ejemplo: menos de 5 accidentes con baja por cada 100 trabajadores.")
build(
    O6, 4, F,
    use="Aprenderé a calcular la tasa de accidentabilidad y la de siniestralidad, a compararlas con el año anterior y con una meta, y a calcular horas de capacitación.",
    prior=["Sé multiplicar y dividir enteros.", "Sé comparar dos números.", "Sé qué es un accidente con baja."],
    explain=[
        "La tasa de accidentabilidad se calcula multiplicando los accidentes con baja por 100 y dividiendo por el número promedio de trabajadores: indica cuántos accidentes hubo por cada 100 trabajadores. La tasa de siniestralidad se calcula multiplicando los días perdidos por 100 y dividiendo por los trabajadores: indica cuántos días de trabajo se perdieron por cada 100 trabajadores. Una baja permite al trabajador no asistir por la lesión.",
        "Para decidir si algo mejoró se compara con el año anterior y con una meta. Si la tasa baja, hubo mejora. Una tasa baja no prueba por sí sola que el taller sea seguro: se mira también la cantidad de incidentes informados y la capacitación. Las horas de capacitación se calculan multiplicando las sesiones por sus horas y por el número de personas.",
        f"Los números son de ejemplo y el cálculo es de papel. {EMER} {AVISO}",
    ],
    vocab=[("tasa de accidentabilidad", "accidentes con baja por cada 100 trabajadores"), ("tasa de siniestralidad", "días perdidos por cada 100 trabajadores"), ("días perdidos", "días de trabajo que se pierden por la lesión"), ("meta", "valor que se quiere alcanzar o no superar"), ("horas-persona", "horas de una actividad multiplicadas por el número de personas")],
    worked=[
        ("Tasa de accidentabilidad", "Un taller de ejemplo tiene 20 trabajadores y 2 accidentes con baja. ¿Cuál es la tasa de accidentabilidad?", ["Se multiplican 2 por 100: 200.", "200 dividido en 20 son 10."], "10 accidentes por cada 100 trabajadores"),
        ("Horas-persona", "Una charla de ejemplo dura 1 hora y asisten 12 personas. ¿Cuántas horas-persona suma?", ["Se multiplican las horas por las personas.", "1 por 12 son 12."], "12 horas-persona"),
    ],
    mistakes=[("Comparar solo la cantidad de accidentes entre talleres de tamaño distinto.", "Un taller grande tiene más accidentes posibles que uno pequeño.", "Compara las tasas por cada 100 trabajadores."),
              ("Creer que una tasa baja significa que no hay peligros.", "La tasa solo cuenta los hechos ocurridos.", "Mira también los incidentes y los controles.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué indica la tasa de accidentabilidad?", "Cuántos accidentes con baja hay por cada 100 trabajadores", "Cuántos días de trabajo se perdieron en total", "Cuántas capacitaciones hubo en el año", "La accidentabilidad cuenta accidentes por cada 100 trabajadores."),
        ("abc", "En Mecánica Industrial: ¿qué indica la tasa de siniestralidad?", "Cuántos días se perdieron por cada 100 trabajadores", "Cuántos accidentes hubo por cada 100 trabajadores", "Cuántos incidentes se informaron", "La siniestralidad mide la gravedad en días perdidos."),
        ("abc", "En Mecánica Industrial: ¿qué son las horas-persona?", "Las horas de una actividad multiplicadas por el número de personas", "Las horas que dura la jornada", "Las horas de descanso del taller", "Las horas-persona suman el tiempo total de todas las personas."),
        ("=", "{F} ¿Cuál es la tasa de accidentabilidad del año de ejemplo del taller?", "3*100//50", "Se multiplican los accidentes por 100 y se dividen por los trabajadores.", " por cada 100 trabajadores"),
        ("=", "{F} ¿Cuál es la tasa de siniestralidad del año de ejemplo?", "25*100//50", "Se multiplican los días perdidos por 100 y se dividen por los trabajadores.", " días por cada 100 trabajadores"),
        ("=", "{F} ¿Cuál fue la tasa de accidentabilidad del año anterior?", "5*100//50", "Se aplica la misma fórmula con los datos del año anterior.", " por cada 100 trabajadores"),
        ("=", "{F} ¿Cuántos días perdidos menos hubo este año que el anterior?", "60-25", "Se resta los días perdidos de este año a los del anterior.", " días"),
        ("abc", "{F} ¿Se cumple la meta de menos de 5 accidentes con baja por cada 100 trabajadores?", "No, porque la tasa del año es 6 y 6 no es menor que 5", "Sí, porque 6 es menor que el 10 del año anterior", "Sí, porque la tasa bajó respecto del año anterior", "La tasa de 6 supera la meta de menos de 5."),
        ("=", "{F} ¿Cuántas horas-persona suman las capacitaciones del año?", "4*2*50", "Se multiplican sesiones, horas por sesión y personas.", " horas-persona"),
        ("abc", "{F} Un jefe dice: «la accidentabilidad bajó de 10 a 6, así que el taller está seguro y ya no hacen falta capacitaciones». ¿Qué respuesta es correcta?", "Es falso: la tasa mejoró, pero sigue sobre la meta y hay 20 incidentes que analizar", "Es cierto, porque la tasa bajó", "Es cierto, porque no hubo muertes", "Una mejora no justifica dejar la prevención."),
        ("abc", "{F} Un taller de 100 trabajadores tuvo 6 accidentes con baja y este taller, con 50 trabajadores, tuvo 3. ¿Qué afirmación es correcta?", "Tienen la misma tasa de accidentabilidad", "El taller de 100 tiene la mitad de la tasa", "El taller de 50 tiene el doble de la tasa", "Ambos tienen 6 accidentes por cada 100 trabajadores."),
        ("=", "{F} Si el próximo año el taller tuviera 2 accidentes con baja con el mismo promedio de trabajadores, ¿cuál sería la tasa de accidentabilidad?", "2*100//50", "Se multiplican los accidentes por 100 y se dividen por los trabajadores.", " por cada 100 trabajadores"),
        ("En un taller de ejemplo se pierden 40 días con 20 trabajadores y en otro se pierden 60 días con 40 trabajadores. ¿Cuál tiene mayor siniestralidad?", "El primero, con 200 frente a 150", "El primero tiene 40 por 100 dividido en 20, es decir 200; el segundo, 60 por 100 dividido en 40, es decir 150."),
    ],
    ctx=("abc", "En una reunión de ejemplo, un jefe dice: «tuvimos 3 accidentes, el otro taller tuvo 5, estamos mejor». El otro taller tiene 200 trabajadores y el nuestro 50. ¿Qué respondes?", "Que hay que comparar tasas por cada 100 trabajadores, no la cantidad de accidentes", "Que tiene razón, porque 3 es menor que 5", "Que da lo mismo cuántos trabajadores haya", "Para comparar talleres de distinto tamaño se usan tasas."),
    sc=[
        ("En Mecánica Industrial: ¿cómo se calcula la tasa de accidentabilidad?", "Accidentes por 100 dividido por los trabajadores", "Se multiplica por 100 y se divide por los trabajadores."),
        ("En Mecánica Industrial: ¿qué se compara además del año anterior?", "Una meta", "La meta dice si el resultado es aceptable."),
        ("En Mecánica Industrial: ¿qué mide la siniestralidad?", "Los días perdidos por cada 100 trabajadores", "Mide la gravedad en días de trabajo perdidos."),
    ],
    op=("Ficha de ejemplo: otro taller tiene 25 trabajadores, 1 accidente con baja y 10 días perdidos. Año anterior: 2 accidentes con baja y 30 días perdidos. Meta: menos de 5 accidentes con baja por cada 100 trabajadores. Escribe (a) la tasa de accidentabilidad de este año, (b) la tasa de siniestralidad de este año, (c) si se cumple la meta, (d) si mejoró respecto del año anterior.",
        "(a) 1 × 100 ÷ 25 = 4. (b) 10 × 100 ÷ 25 = 40. (c) Sí, porque 4 es menor que 5. (d) Sí: el año anterior fue 8 de accidentabilidad y 120 de siniestralidad, ambas mayores.",
        ["calcula la accidentabilidad", "calcula la siniestralidad", "compara con la meta", "compara con el año anterior"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por 100", "comparar solo accidentes y no tasas", "no usar la meta"],
        "Pregunta: «¿multiplicaste por 100 antes de dividir?». Si no, pídele que relea la fórmula."),
    reinforce="Inventa un taller con trabajadores, accidentes y días perdidos y calcula sus dos tasas con números que den un entero.",
    extend="Explica con un ejemplo por qué una tasa baja no prueba que el taller sea seguro.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Taller Demo» fabrica bridas de acero para una planta de ejemplo. El cliente exige cumplir una norma de fabricación y entregar documentos: plano aprobado, certificado del material, "
     "registro de inspección y certificado de calidad del lote. Peligro anotado: una brida que no cumple podría fallar en la planta del cliente y causar un accidente. Personal del área de calidad del taller: 4 personas.")
build(
    O7, 1, F,
    use="Aprenderé qué es una norma, cuándo es obligatoria, qué es un procedimiento y por qué la calidad también es seguridad.",
    prior=["Sé qué es un plano y una tolerancia.", "Sé qué es una no conformidad.", "Sé que algunas reglas son obligatorias."],
    explain=[
        "Una norma es un documento técnico que fija requisitos acordados para un producto o una actividad. Hay normas nacionales, como las normas chilenas (NCh), que se elaboran con el Instituto Nacional de Normalización, y normas internacionales, como las de la Organización Internacional de Normalización (ISO). Una norma es voluntaria, pero se vuelve obligatoria cuando una ley, un reglamento o un contrato la exige.",
        "Un procedimiento es un documento que describe cómo debe hacerse una actividad dentro de una empresa, para que se haga siempre de la misma manera. La calidad es cumplir los requisitos del cliente y de la norma; en piezas que soportan presión o carga, un incumplimiento puede causar un accidente, por eso calidad y seguridad van juntas. La trazabilidad es poder seguir el historial de un producto desde el material hasta la entrega.",
        f"Las normas reales se consultan en su versión vigente; aquí solo se aprenden los conceptos. {EMER} {AVISO}",
    ],
    vocab=[("norma", "documento técnico que fija requisitos acordados"), ("NCh", "sigla de las normas chilenas"), ("norma internacional", "norma elaborada por organismos de muchos países, como ISO"), ("procedimiento", "documento que describe cómo se hace una actividad en una empresa"), ("calidad", "cumplimiento de los requisitos del cliente y de la norma"), ("trazabilidad", "posibilidad de seguir el historial de un producto")],
    worked=[
        ("Norma obligatoria", "Un contrato de ejemplo dice «las piezas deben cumplir la norma X». ¿La norma es obligatoria para ese trabajo?", ["La norma es voluntaria por sí sola.", "Pero el contrato la exige, así que se vuelve obligatoria."], "Sí, por el contrato"),
        ("Trazabilidad", "Un taller de ejemplo anota el número del lote del material de cada pieza. ¿Qué logra?", ["Puede seguir el historial de la pieza.", "Eso es trazabilidad."], "Trazabilidad"),
    ],
    mistakes=[("Creer que una norma es solo un consejo que se puede ignorar.", "Cuando un contrato o una ley la exige es obligatoria.", "Revisa qué normas exige el contrato o la ley."),
              ("Hacer una actividad de memoria cuando existe un procedimiento.", "Los procedimientos aseguran que se haga siempre igual.", "Consulta el procedimiento vigente.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es una norma?", "Un documento técnico que fija requisitos acordados", "Una herramienta que mide piezas", "Un permiso que firma el cliente", "La norma fija requisitos; no es una herramienta ni un permiso."),
        ("abc", "En Mecánica Industrial: ¿qué es la trazabilidad?", "La posibilidad de seguir el historial de un producto", "La rapidez con que se fabrica una pieza", "El precio de una pieza", "La trazabilidad permite saber de dónde viene y qué pasó con una pieza."),
        ("abc", "En Mecánica Industrial: ¿cuándo se vuelve obligatoria una norma voluntaria?", "Cuando una ley, un reglamento o un contrato la exige", "Cuando el taller lo prefiere", "Cuando el cliente es de otro país", "La exigencia legal o contractual hace obligatoria una norma."),
        ("abc", "{F} ¿Qué es la sigla NCh?", "Las normas chilenas", "Una norma internacional de calidad", "El nombre del cliente de la planta", "NCh es la sigla de las normas chilenas."),
        ("abc", "{F} ¿Qué documento de los que pide el cliente muestra de qué material y de qué lote viene la brida?", "El certificado del material", "El plano aprobado", "El registro de inspección", "El certificado del material identifica material y lote."),
        ("abc", "{F} ¿Por qué la calidad de la brida también es un tema de seguridad?", "Porque una brida que no cumple podría fallar y causar un accidente", "Porque la brida debe ser de color llamativo", "Porque el cliente lo pide por costumbre", "La falla de una pieza que soporta carga puede causar un accidente."),
        ("=", "{F} Cada persona de calidad revisa 15 bridas por turno. ¿Cuántas bridas revisan las 4 personas por turno?", "4*15", "Se multiplican las personas por las bridas de cada una.", " bridas"),
        ("=", "El taller fabrica lotes de 60 bridas y el cliente pide 5 lotes. ¿Cuántas bridas son en total?", "60*5", "Se multiplican las bridas de un lote por los lotes.", " bridas"),
        ("abc", "{F} El contrato dice que las bridas deben cumplir una norma. Un compañero dice que la norma es solo voluntaria y puede omitirse. ¿Qué respuesta es correcta?", "Es falso: el contrato la hace obligatoria para este trabajo", "Es cierto, porque la norma es voluntaria", "Es cierto, si el taller es pequeño", "El contrato convierte la norma en obligatoria."),
        ("abc", "{F} El jefe quiere entregar la brida sin el certificado del material porque «el acero es el mismo de siempre». ¿Qué respuesta es correcta?", "No corresponde: el cliente exige el certificado y sirve para la trazabilidad", "Corresponde, si el acero parece bueno", "Corresponde, si el cliente no se da cuenta", "El cliente pide el documento y respalda el material."),
        ("abc", "En una visita a una planta de ejemplo, una brida falla y escapa un fluido caliente. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a apretar la unión", "Tapar el escape con tu ropa", "Intervenir sin formación puede causar quemaduras."),
        ("=", "{F} Si cada una de las 4 personas de calidad revisa 15 bridas y el lote es de 60, ¿cuántos turnos de revisión se necesitan para un lote?", "60//(4*15)", "Se dividen las bridas del lote entre lo que revisa el equipo por turno.", " turno"),
        ("Un contrato de ejemplo exige cumplir una norma internacional de ISO y un cliente propone usar una norma interna del taller más suave. ¿Qué corresponde?", "Cumplir lo que exige el contrato", "El contrato fija los requisitos y no los decide el taller."),
    ],
    ctx=("abc", "Un cliente de ejemplo pregunta si las piezas cumplen la norma que pidió. El taller tiene el certificado del material, pero no el registro de inspección. ¿Qué propones?", "Completar el registro de inspección antes de entregar y explicar al cliente qué documentos respaldan el cumplimiento", "Entregar igual y decir que cumple", "Anotar un registro falso", "El cumplimiento se respalda con documentos reales."),
    sc=[
        ("En Mecánica Industrial: ¿qué es un procedimiento?", "Un documento que describe cómo se hace una actividad", "Asegura que la actividad se haga siempre igual."),
        ("En Mecánica Industrial: ¿qué son las NCh?", "Las normas chilenas", "NCh es la sigla de las normas chilenas."),
        ("En Mecánica Industrial: ¿qué permite la trazabilidad?", "Seguir el historial de un producto", "Se sabe de dónde viene el material y qué se hizo."),
    ],
    op=("Ficha de ejemplo: un taller fabrica ejes que el cliente usará en una máquina de la que dependen personas. El cliente exige el plano aprobado, el certificado del material y el registro de inspección. Escribe (a) qué documento prueba de qué material es el eje, (b) qué documento prueba que las medidas se controlaron, (c) por qué la calidad de este eje también es seguridad, (d) qué pasa si falta uno de los documentos.",
        "(a) El certificado del material. (b) El registro de inspección. (c) Porque un eje que no cumple podría fallar y causar un accidente. (d) No se entrega hasta completarlo, porque el cliente lo exige y respalda la trazabilidad.",
        ["nombra el certificado del material", "nombra el registro de inspección", "relaciona calidad y seguridad", "indica qué hacer si falta un documento"],
        ["hoja con las cuatro respuestas"],
        ["confundir los documentos", "decir que entregar sin documentos es lo mismo", "no relacionar calidad y seguridad"],
        "Pregunta: «¿qué documento muestra el material y cuál las medidas?». Si duda, pídele que relea las definiciones."),
    reinforce="Escribe tres documentos que un cliente puede exigir para una pieza y para qué sirve cada uno.",
    extend="Explica con un ejemplo por qué una norma voluntaria puede ser obligatoria para un trabajo concreto.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (hoja de ruta de ejemplo, inventada). Pieza: brida B-1. Operaciones en orden: Op10, corte de la barra de acero, puesto de corte, 5 min; Op20, mecanizado, puesto de torneado, 20 min; Op30, taladrado de los agujeros, puesto de taladro, 8 min; "
     "Op40, control dimensional, puesto de calidad, 6 min; Op50, embalaje y rotulado, puesto de despacho, 4 min. Observaciones de la hoja: cada operación se firma al terminar; el control Op40 usa un instrumento con certificado vigente. "
     "Otros documentos: plan de calidad, instrucción de trabajo, informe de no conformidad y acción correctiva.")
build(
    O7, 2, F,
    use="Aprenderé a leer una hoja de ruta, a distinguir plan de calidad, instrucción de trabajo, no conformidad y acción correctiva, y a reconocer los roles.",
    prior=["Sé qué es un procedimiento.", "Sé qué es una no conformidad.", "Sé sumar tiempos en minutos."],
    explain=[
        "La hoja de ruta lista, en orden, las operaciones por las que pasa una pieza, con su puesto de trabajo y su tiempo. Cada operación se firma al terminar, y así queda un registro. El plan de calidad dice qué se controla, con qué instrumento y con qué criterio. La instrucción de trabajo detalla cómo se hace una operación concreta, y solo la usa personal autorizado.",
        "Cuando algo no cumple, se emite un informe de no conformidad que describe el hecho, y se decide qué hacer con la pieza. Una acción correctiva elimina la causa para que no se repita. El jefe de producción coordina, el área de calidad controla y registra, el operario autorizado ejecuta y el cliente recibe y puede auditar.",
        f"Se leen y se respetan los documentos; este cuaderno no explica cómo se hace ninguna operación. {EMER} {AVISO}",
    ],
    vocab=[("hoja de ruta", "lista ordenada de operaciones de una pieza con su puesto y su tiempo"), ("plan de calidad", "documento que dice qué se controla, con qué y con qué criterio"), ("instrucción de trabajo", "documento que detalla cómo se hace una operación concreta"), ("informe de no conformidad", "documento que describe un incumplimiento"), ("acción correctiva", "medida que elimina la causa de un incumplimiento"), ("auditoría", "revisión de que se cumplen los documentos y las normas")],
    worked=[
        ("Sumar tiempos", "Una hoja de ruta de ejemplo tiene operaciones de 10, 15 y 7 minutos. ¿Cuántos minutos suma?", ["Se suman los tres tiempos.", "10 más 15 más 7 son 32."], "32 minutos"),
        ("Elegir el documento", "Una persona de ejemplo necesita saber qué se controla en una pieza y con qué instrumento. ¿Qué documento consulta?", ["Esa información la da un documento de control.", "Es el plan de calidad."], "El plan de calidad"),
    ],
    mistakes=[("Usar una instrucción de trabajo sin estar autorizado para esa operación.", "Las operaciones las hace personal autorizado.", "Consulta con la jefatura quién está autorizado."),
              ("Archivar un informe de no conformidad sin acción correctiva.", "La causa seguiría presente y el incumplimiento se repetiría.", "Define una acción correctiva con responsable y plazo.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es una hoja de ruta?", "Una lista ordenada de las operaciones de una pieza con su puesto y su tiempo", "Un mapa del taller con las salidas de emergencia", "Un plano de la pieza con sus cotas", "La hoja de ruta ordena las operaciones de fabricación."),
        ("abc", "En Mecánica Industrial: ¿qué es un plan de calidad?", "El documento que dice qué se controla, con qué instrumento y con qué criterio", "La lista de las personas autorizadas", "El horario de los turnos", "El plan de calidad organiza los controles."),
        ("abc", "En Mecánica Industrial: ¿qué es una acción correctiva?", "Una medida que elimina la causa de un incumplimiento", "El descarte de la pieza defectuosa", "La firma del jefe en el informe", "La acción correctiva ataca la causa para que no se repita."),
        ("=", "{F} ¿Cuántos minutos suman las cinco operaciones de la hoja de ruta?", "5+20+8+6+4", "Se suman los tiempos de las cinco operaciones.", " minutos"),
        ("abc", "{F} ¿En qué puesto se hace el control dimensional?", "En el puesto de calidad", "En el puesto de torneado", "En el puesto de despacho", "Op40 se hace en el puesto de calidad."),
        ("abc", "{F} ¿Qué operación va justo después del mecanizado?", "El taladrado de los agujeros", "El corte de la barra", "El embalaje y rotulado", "En la hoja de ruta Op30 sigue a Op20."),
        ("=", "{F} Hay que fabricar 12 bridas. ¿Cuántos minutos se necesitan solo para el mecanizado de todas ellas?", "12*20", "Se multiplican las bridas por el tiempo de mecanizado de cada una.", " minutos"),
        ("=", "{F} ¿Cuántos minutos más tarda el mecanizado que el taladrado?", "20-8", "Se resta el tiempo del taladrado al del mecanizado.", " minutos"),
        ("abc", "{F} ¿Cuántas operaciones deben quedar firmadas para una brida terminada?", "Las cinco, una por cada operación", "Solo la última", "Solo el control dimensional", "La hoja exige firmar cada operación al terminar."),
        ("abc", "{F} Al finalizar el control, se halla una brida con una medida fuera de tolerancia. ¿Qué documento corresponde emitir?", "Un informe de no conformidad", "Una nueva hoja de ruta", "Un plan de calidad distinto", "El incumplimiento se registra en un informe de no conformidad."),
        ("abc", "{F} Un operario sugiere firmar todas las operaciones al final del turno, de memoria. ¿Qué respuesta es correcta?", "No corresponde: cada operación se firma al terminar para que el registro sea fiel", "Corresponde, porque ahorra tiempo", "Corresponde, si recuerda todo", "El registro firmado en el momento evita errores."),
        ("=", "{F} Si el taller trabaja 8 horas de 60 minutos por turno, ¿cuántas bridas completas se pueden terminar en un turno con la suma de tiempos de la hoja, considerando solo piezas completas, si se hace una por una?", "8*60//43", "Se convierten las horas a minutos y se dividen por los 43 minutos de cada brida.", " bridas"),
        ("Un informe de no conformidad de ejemplo dice «medida fuera de tolerancia». La acción correctiva es revisar el instrumento de medición del puesto. ¿Qué causa se está atacando?", "Un posible error del instrumento de medición", "La acción apunta a la causa posible: un instrumento descalibrado."),
    ],
    ctx=("abc", "Un cliente de ejemplo hace una auditoría y pide la hoja de ruta firmada de una brida. El taller solo tiene firmas en 3 de las 5 operaciones. ¿Qué propones?", "Reconocer la falta, registrar la no conformidad y asegurar que cada operación se firme al terminar", "Firmar ahora las dos faltantes con fecha anterior", "Decir que se perdió la hoja", "El registro debe ser fiel y no se falsifica."),
    sc=[
        ("En Mecánica Industrial: ¿qué lista la hoja de ruta?", "Las operaciones en orden con su puesto y tiempo", "Ordena las operaciones de fabricación de la pieza."),
        ("En Mecánica Industrial: ¿qué documento describe un incumplimiento?", "El informe de no conformidad", "Registra qué ocurrió y qué se decide."),
        ("En Mecánica Industrial: ¿qué es una auditoría?", "Una revisión de que se cumplen los documentos y las normas", "Comprueba el cumplimiento de lo escrito."),
    ],
    op=("Ficha de ejemplo: hoja de ruta de la pieza P-9: Op10 corte, 4 min; Op20 mecanizado, 15 min; Op30 control dimensional, 5 min; Op40 embalaje, 3 min. Se fabrican 10 piezas. Escribe (a) cuántos minutos suma la hoja de una pieza, (b) cuántos minutos de mecanizado necesitan las 10 piezas, (c) qué operación es el control, (d) qué documento emitirías si una pieza no cumple.",
        "(a) 4 + 15 + 5 + 3 = 27 minutos. (b) 10 × 15 = 150 minutos. (c) Op30. (d) Un informe de no conformidad.",
        ["suma los tiempos", "calcula el mecanizado", "identifica el control", "nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["olvidar una operación", "multiplicar todos los tiempos por 10", "nombrar un documento equivocado"],
        "Pregunta: «¿qué operación es el control?». Si duda, pídele que relea la hoja."),
    reinforce="Inventa una hoja de ruta de cuatro operaciones con tiempos y calcula el total por pieza.",
    extend="Explica con un ejemplo por qué firmar cada operación al terminar ayuda a una auditoría.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (caso de trazabilidad de ejemplo, inventado). Lote L-45 de 50 bridas. El certificado del material indica la colada C-9, es decir, el lote de acero del que salió la barra. El registro de lote anota: inspeccionadas 50; con no conformidad 2 (números 17 y 33, por una medida fuera de tolerancia); "
     "bridas despachadas al cliente: 48. Meses después, el cliente reclama por una brida cuyo rótulo dice L-45, número 21. Hallazgos de una auditoría de ejemplo: H1, falta una firma en una operación del lote L-47; H2, el instrumento del control tiene el certificado vencido en el lote L-48; H3, todo conforme en el lote L-49.")
build(
    O7, 3, F,
    use="Aprenderé a seguir la trazabilidad de una pieza en documentos, a clasificar hallazgos de una auditoría y a decidir qué acción corresponde, en un caso escrito.",
    prior=["Sé qué es la trazabilidad.", "Sé qué es una no conformidad.", "Sé leer un registro de lote."],
    explain=[
        "Con la trazabilidad se puede ir de una pieza al lote y del lote al material. El rótulo de la pieza indica su lote y su número; el registro de lote dice cuántas piezas se inspeccionaron, cuáles tuvieron no conformidad y cuántas se despacharon; el certificado del material indica la colada. Si hay un reclamo, estos documentos permiten saber qué piezas pueden estar afectadas.",
        "Una auditoría revisa que lo hecho coincida con lo escrito. Un hallazgo puede ser una conformidad (todo cumple), una observación (algo menor que mejorar) o una no conformidad (un incumplimiento de un requisito). Cada no conformidad exige una acción correctiva con responsable y plazo. Las piezas con no conformidad no se despachan.",
        f"El análisis es de papel con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("colada", "lote de acero fundido del que sale el material"), ("registro de lote", "documento con inspecciones, no conformidades y despachos de un lote"), ("rótulo", "etiqueta de la pieza con su lote y número"), ("hallazgo", "resultado de una auditoría sobre un punto revisado"), ("observación", "hallazgo menor que se puede mejorar")],
    worked=[
        ("Ubicar un lote", "Una pieza de ejemplo trae el rótulo L-12, número 5. ¿Qué documento permite ver si esa pieza tuvo no conformidad?", ["El rótulo da el lote.", "El registro de lote anota las no conformidades."], "El registro de lote del lote L-12"),
        ("Clasificar un hallazgo", "En una auditoría de ejemplo se encuentra una firma faltante en una operación. ¿Qué hallazgo es?", ["Es un incumplimiento del requisito de firmar.", "Es una no conformidad."], "No conformidad"),
    ],
    mistakes=[("Despachar una pieza con no conformidad porque «es leve».", "Las piezas con no conformidad no se despachan sin una decisión formal.", "Retenla y registra la decisión."),
              ("Ignorar un reclamo de cliente porque el lote «era bueno».", "Se debe usar la trazabilidad para verificar el caso.", "Revisa rótulo, registro de lote y certificado.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es la colada de un certificado de material?", "El lote de acero fundido del que salió el material", "La fecha de entrega al cliente", "El número de piezas del lote", "La colada identifica el origen del material."),
        ("abc", "En Mecánica Industrial: ¿qué es un hallazgo de auditoría?", "El resultado de la revisión de un punto, que puede ser conformidad, observación o no conformidad", "Una pieza defectuosa", "El nombre de quien auditó", "El hallazgo describe lo encontrado en un punto revisado."),
        ("abc", "En Mecánica Industrial: ¿qué se hace con una pieza con no conformidad?", "No se despacha hasta tomar una decisión formal", "Se despacha si la diferencia es leve", "Se pinta para esconder el defecto", "La pieza con no conformidad se retiene y se decide formalmente."),
        ("abc", "{F} ¿Qué datos del rótulo permiten ubicar la brida reclamada?", "El lote L-45 y el número 21", "La colada C-9 y el número 21", "Solo el nombre del cliente", "El rótulo da lote y número de pieza."),
        ("=", "{F} ¿Cuántas bridas quedaron en la fábrica y no se despacharon?", "50-48", "Se resta lo despachado al total del lote.", " bridas"),
        ("abc", "{F} ¿Qué dos bridas del lote tuvieron no conformidad?", "La 17 y la 33", "La 21 y la 33", "La 17 y la 21", "El registro anota 17 y 33; la 21 es la reclamada."),
        ("abc", "{F} Para saber de qué material salió la brida reclamada, ¿qué documento consulta?", "El certificado del material, por la colada C-9", "El registro de inspección de otra pieza", "La hoja de ruta de otro lote", "La colada se indica en el certificado."),
        ("abc", "{F} El hallazgo H1, una firma faltante, se clasifica como:", "No conformidad", "Conformidad", "Observación sin importancia", "Falta un requisito de la hoja de ruta."),
        ("abc", "{F} El hallazgo H2 indica que el instrumento del control tiene el certificado vencido. ¿Qué corresponde?", "Registrarlo como no conformidad y revisar las mediciones hechas con ese instrumento", "Ignorarlo si las piezas parecen buenas", "Renovar el certificado y no revisar nada más", "Las mediciones con un instrumento vencido quedan en duda."),
        ("=", "{F} Si los lotes L-47, L-48 y L-49 tienen el mismo tamaño que L-45, ¿cuántas bridas hay en esos tres lotes?", "3*50", "Se multiplican los lotes por las bridas de cada uno.", " bridas"),
        ("abc", "{F} El cliente exige que se revisen todas las bridas del lote L-45. Un jefe dice que basta mirar la reclamada. ¿Qué respuesta es adecuada?", "Conviene revisar el lote con la trazabilidad, porque puede haber otras piezas afectadas", "Basta con la reclamada", "No se revisa nada, porque ya se despachó", "La trazabilidad sirve para encontrar piezas afectadas."),
        ("abc", "{F} Las bridas 17 y 33 se despacharon por error al cliente. ¿Qué corresponde hacer?", "Informar al cliente, retirarlas si es posible y registrar una acción correctiva", "Esperar a que el cliente reclame", "Cambiar los números del registro", "Un despacho erróneo se informa y se corrige."),
        ("=", "{F} Entre las 48 bridas despachadas, la reclamada es una. ¿Cuántas bridas despachadas no han generado reclamo?", "48-1", "Se resta la reclamada a las despachadas.", " bridas"),
    ],
    ctx=("abc", "El cliente de ejemplo reclama por una pieza, y el jefe dice «eso fue hace meses, no hay forma de saber». ¿Qué propones?", "Buscar por el rótulo el lote, el registro de lote y el certificado del material", "No investigar", "Culpar al cliente", "La trazabilidad permite investigar piezas ya despachadas."),
    sc=[
        ("En Mecánica Industrial: ¿qué indica el rótulo de una pieza?", "Su lote y su número", "Con ellos se ubica el registro de lote."),
        ("En Mecánica Industrial: ¿qué es una observación de auditoría?", "Un hallazgo menor que se puede mejorar", "No es un incumplimiento pero conviene mejorarlo."),
        ("En Mecánica Industrial: ¿qué exige cada no conformidad?", "Una acción correctiva con responsable y plazo", "La acción correctiva elimina la causa."),
    ],
    op=("Ficha de ejemplo: lote M-10 de 40 ejes. Certificado del material: colada D-3. Registro de lote: 40 inspeccionados; 1 con no conformidad (el número 8); 39 despachados. Un cliente reclama por un eje con rótulo M-10, número 22. Escribe (a) qué datos usas para ubicar el eje, (b) qué documento te dice la colada, (c) si el eje 8 pudo haberse despachado y qué harías, (d) qué acción tomarías por el reclamo.",
        "(a) El lote M-10 y el número 22. (b) El certificado del material. (c) No debía despacharse; el eje 8 estaba retenido, y se verifica que no esté entre los 39 despachados. (d) Revisar el registro de lote y el certificado, buscar si otras piezas pueden estar afectadas y definir una acción correctiva.",
        ["usa lote y número", "nombra el certificado", "razona sobre la pieza retenida", "propone una acción"],
        ["hoja con las cuatro respuestas"],
        ["confundir lote con colada", "despachar la pieza con no conformidad", "no investigar el reclamo"],
        "Pregunta: «¿qué dato une la pieza con el lote?». Si duda, pídele que relea el rótulo."),
    reinforce="Inventa un lote con rótulo, colada y una pieza con no conformidad, y escribe cómo seguirías su trazabilidad.",
    extend="Explica con un ejemplo por qué un instrumento con certificado vencido debe registrarse como no conformidad.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (planilla de producción y calidad de ejemplo, inventada). Pedido de 480 bridas. Tiempo de ciclo por brida: 43 minutos de ruta total; el puesto cuello de botella (el más lento) es el mecanizado, de 20 minutos por brida, y marca el ritmo de la línea. "
     "Minutos disponibles por día en el puesto de mecanizado: 480. En el primer lote de 100 bridas se rechazaron 8. Costo de ejemplo de una brida: $6.000; precio de venta de ejemplo: $9.000. Gasto de ejemplo de rehacer una brida rechazada: $6.000.")
build(
    O7, 4, F,
    use="Aprenderé a calcular el ritmo de una línea, el porcentaje de rechazo, el costo de la mala calidad y el plazo de un pedido con datos de ejemplo.",
    prior=["Sé multiplicar y dividir enteros.", "Sé qué es un porcentaje.", "Sé qué es un cuello de botella."],
    explain=[
        "El cuello de botella es el puesto más lento de la ruta: marca cuántas piezas se pueden terminar por día, aunque los otros puestos sean más rápidos. Las piezas por día se calculan dividiendo los minutos disponibles entre el tiempo del cuello de botella. Los días de un pedido se calculan dividiendo las piezas pedidas entre las piezas por día, redondeando hacia arriba.",
        "El porcentaje de rechazo es las piezas rechazadas por 100 dividido por las piezas inspeccionadas. El costo de la mala calidad es lo que se gasta por rehacer o descartar las piezas rechazadas. Reducir el rechazo mejora el plazo, el costo y la seguridad, y se logra eliminando causas con acciones correctivas.",
        f"Los números son de ejemplo y el cálculo es de papel. {EMER} {AVISO}",
    ],
    vocab=[("cuello de botella", "puesto más lento que marca el ritmo de la línea"), ("piezas por día", "minutos disponibles divididos por el tiempo del puesto más lento"), ("porcentaje de rechazo", "piezas rechazadas por 100 dividido por las inspeccionadas"), ("costo de la mala calidad", "gasto por rehacer o descartar piezas rechazadas"), ("plazo", "días necesarios para completar un pedido")],
    worked=[
        ("Piezas por día", "Un puesto de ejemplo tarda 10 minutos por pieza y dispone de 480 minutos al día. ¿Cuántas piezas por día alcanza?", ["Se divide 480 entre 10.", "480 dividido en 10 son 48."], "48 piezas por día"),
        ("Porcentaje de rechazo", "En un lote de ejemplo se inspeccionan 50 piezas y se rechazan 5. ¿Qué porcentaje de rechazo hay?", ["Se multiplican 5 por 100: 500.", "500 dividido en 50 son 10."], "10 %"),
    ],
    mistakes=[("Calcular las piezas por día con el tiempo total de la ruta en vez del cuello de botella.", "El ritmo lo marca el puesto más lento, no la suma de todos.", "Usa el tiempo del cuello de botella."),
              ("Redondear hacia abajo los días de un pedido.", "Faltarían piezas al terminar el último día completo.", "Redondea hacia arriba cuando sobran piezas.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es el cuello de botella de una línea?", "El puesto más lento, que marca el ritmo", "El puesto más rápido", "El puesto donde se guardan las piezas", "El cuello de botella limita cuántas piezas salen por día."),
        ("abc", "En Mecánica Industrial: ¿cómo se calcula el porcentaje de rechazo?", "Piezas rechazadas por 100 dividido por las inspeccionadas", "Piezas inspeccionadas por 100 dividido por las rechazadas", "Piezas despachadas por 100 dividido por las rechazadas", "El rechazo compara lo rechazado con lo inspeccionado."),
        ("abc", "En Mecánica Industrial: ¿qué es el costo de la mala calidad?", "El gasto por rehacer o descartar piezas rechazadas", "El precio al que se vende la pieza", "El costo del instrumento de medición", "Es el gasto causado por piezas que no cumplen."),
        ("=", "{F} ¿Cuántas bridas por día alcanza el puesto de mecanizado?", "480//20", "Se dividen los minutos disponibles entre el tiempo por brida.", " bridas"),
        ("=", "{F} ¿Cuántos días se necesitan para producir las 480 bridas del pedido, con las bridas por día del mecanizado?", "480//24", "Se dividen las piezas pedidas entre las piezas por día.", " días"),
        ("=", "{F} ¿Qué porcentaje de rechazo tuvo el primer lote?", "8*100//100", "Se multiplican los rechazos por 100 y se dividen por las inspeccionadas.", " %"),
        ("=", "{F} ¿Cuánto cuesta rehacer las bridas rechazadas del primer lote, a $6.000 cada una?", "8*6000", "Se multiplican las rechazadas por el costo de rehacer una.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántos pesos de ejemplo de margen deja una brida, entre el precio de venta y el costo?", "9000-6000", "Se resta el costo al precio de venta.", " pesos de ejemplo"),
        ("=", "{F} Si el rechazo del primer lote se mantuviera en todo el pedido, ¿cuántas bridas se rechazarían de las 480?", "480*8//100", "Se multiplica el pedido por el porcentaje de rechazo y se divide por 100.", " bridas"),
        ("abc", "{F} Un jefe dice: «el tiempo de ciclo de 43 minutos define cuántas bridas salen por día». ¿Qué respuesta es correcta?", "Es falso: el ritmo lo marca el puesto más lento, el mecanizado de 20 minutos", "Es cierto, porque suma todas las operaciones", "Es cierto, si hay un solo operario", "Cuando las operaciones son de puestos distintos, el cuello de botella manda."),
        ("abc", "{F} Se propone acelerar el embalaje, que dura 4 minutos, para producir más bridas por día. ¿Qué observación es correcta?", "Poco ayuda, porque el cuello de botella es el mecanizado", "Ayuda mucho, porque todo cuenta igual", "Ayuda, porque el embalaje es lo más importante", "Mejorar un puesto que no es el cuello de botella no cambia el ritmo."),
        ("=", "{F} Si el rechazo se reduce a 4 bridas por cada 100, ¿cuánto se ahorra al rehacer en un lote de 100, respecto de las 8 rechazadas, a $6.000 cada una?", "(8-4)*6000", "Se calcula la diferencia de rechazos y se multiplica por el costo.", " pesos de ejemplo"),
        ("Un puesto de ejemplo dispone de 480 minutos al día y cada pieza tarda 25 minutos. ¿Cuántas piezas completas alcanza por día?", "19 piezas", "480 dividido en 25 da 19 y sobran 5 minutos, que no alcanzan para otra pieza."),
    ],
    ctx=("abc", "El cliente de ejemplo pide el pedido en 15 días y el cálculo da 20 días con el ritmo actual. ¿Qué propones?", "Informar el plazo real y revisar cómo mejorar el cuello de botella y reducir el rechazo", "Prometer los 15 días sin cambiar nada", "Acelerar el embalaje solamente", "El plazo se basa en el ritmo real del puesto más lento."),
    sc=[
        ("En Mecánica Industrial: ¿cómo se calculan las piezas por día?", "Minutos disponibles divididos por el tiempo del puesto más lento", "El ritmo lo marca el cuello de botella."),
        ("En Mecánica Industrial: ¿cómo se redondean los días de un pedido?", "Hacia arriba", "Si sobran piezas, se necesita un día más."),
        ("En Mecánica Industrial: ¿qué reduce el costo de la mala calidad?", "Eliminar causas con acciones correctivas", "Menos rechazo implica menos gasto por rehacer."),
    ],
    op=("Ficha de ejemplo: un pedido de 200 piezas. El puesto más lento tarda 30 minutos por pieza y dispone de 480 minutos al día. En un lote de 50 piezas se rechazaron 5; rehacer una cuesta $4.000. Escribe (a) las piezas por día, (b) los días del pedido, (c) el porcentaje de rechazo del lote, (d) el costo de rehacer las rechazadas.",
        "(a) 480 ÷ 30 = 16 piezas por día. (b) 200 ÷ 16 = 12,5; se redondea hacia arriba, 13 días. (c) 5 × 100 ÷ 50 = 10 %. (d) 5 × 4.000 = 20.000 pesos de ejemplo.",
        ["calcula las piezas por día", "calcula los días con redondeo", "calcula el rechazo", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["usar el tiempo total de la ruta", "no redondear hacia arriba", "dividir al revés el rechazo"],
        "Pregunta: «¿qué puesto marca el ritmo?». Si duda, pídele que relea el cuello de botella."),
    reinforce="Inventa una ruta con cuatro operaciones y señala cuál es el cuello de botella y por qué.",
    extend="Explica con un ejemplo por qué mejorar un puesto que no es el cuello de botella no aumenta las piezas por día.",
)
