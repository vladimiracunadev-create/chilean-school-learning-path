"""Asistencia en Geología TP 3.º y 4.º medio: OAE-01 (campamentos), OAE-02 (equipos) y OAE-03 (levantamientos topográficos). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_asge_common import AVISO, EMER, build

O1 = "TP-ASGE-3y4-OAE-01"
O2 = "TP-ASGE-3y4-OAE-02"
O3 = "TP-ASGE-3y4-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La empresa ficticia «Minera Demo» planifica el campamento del «Proyecto Quebrada Demo», una prospección de diez días para 12 personas. "
     "El sitio propuesto es una terraza plana junto a una quebrada seca, al pie de una ladera con piedras sueltas. Peligros anotados: caída de rocas desde la ladera, posible crecida repentina de agua en la quebrada tras lluvias, "
     "noches muy frías, una cocina a gas en el comedor, restos de comida y un centro asistencial a tres horas de ruta (dato de ejemplo). Cada carpa dormitorio de ejemplo aloja a 4 personas.")
build(
    O1, 1, F,
    use="Aprenderé qué es una prospección y un campamento de terreno, cómo se distinguen peligro y riesgo, qué controles ordena la jerarquía de prevención y por qué esta tarea exige personal autorizado y norma vigente.",
    prior=["Sé leer una ficha escrita y una lista de datos.", "Sé sumar, multiplicar y dividir números enteros.", "Sé que el clima y el terreno cambian el riesgo de un lugar."],
    explain=[
        "Una prospección es la etapa de búsqueda de zonas donde puede haber minerales; para obtener muestras geológicas el equipo suele trabajar lejos de las ciudades. Por eso necesita un campamento: un lugar temporal con dormitorios, comedor, baños, bodega, manejo de residuos y comunicación. El proyecto de prospección es el plan que dice dónde, cuántos días y con cuántas personas se trabajará. Un campamento se organiza (se planifica), se instala (queda funcionando, a cargo de personal autorizado) y se desarma (se retira todo y el sitio queda como estaba).",
        "Todo lugar tiene peligros, que son fuentes de daño, y riesgos, que son la posibilidad de que ese daño ocurra. La jerarquía de controles ordena las medidas de la más a la menos efectiva: eliminar el peligro o alejarse de él, sustituirlo, aplicar controles de ingeniería (cambios físicos), aplicar controles administrativos (reglas, señales, horarios, capacitación) y, al final, el equipo de protección personal (EPP), que no quita el peligro. Además se protege el medio ambiente: los residuos, el agua y los combustibles se manejan según el plan ambiental del proyecto y no se dejan en el terreno.",
        f"La actividad minera está regulada: la autoridad minera fiscaliza la seguridad según la norma vigente, y el terreno se usa con permiso de su dueño. {EMER} {AVISO}",
    ],
    vocab=[("prospección", "etapa de búsqueda de zonas con posibles minerales"), ("campamento", "lugar temporal de alojamiento, comida, aseo y bodega para un equipo que trabaja lejos"), ("proyecto de prospección", "plan que define dónde, cuánto tiempo y con cuántas personas se trabajará"), ("peligro", "fuente con capacidad de causar daño"), ("riesgo", "posibilidad de que un peligro cause daño"), ("aluvión", "flujo repentino de agua con barro y piedras que baja por una quebrada"), ("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Peligro y riesgo", "En un campamento de ejemplo, la entrada del comedor tiene un piso de tablones mojado y resbaloso. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el piso mojado, porque puede causar daño.", "El riesgo es que alguien resbale, caiga y se lesione."], "Peligro: el piso mojado; riesgo: que alguien resbale y se lesione"),
        ("Clasificar un control", "En un campamento de ejemplo se decide trasladar un dormitorio desde el pie de una ladera inestable a una terraza lejana. ¿A qué nivel de la jerarquía corresponde?", ["Con el traslado la persona ya no queda expuesta a la ladera.", "Quitar o alejar la exposición al peligro es el primer nivel."], "Eliminación o alejamiento del peligro"),
    ],
    mistakes=[("Creer que cualquier terreno plano es un buen lugar para un campamento.", "Un lugar plano puede estar en el cauce de una quebrada o bajo una ladera inestable.", "Antes de elegir el sitio se identifican los peligros del entorno y se aleja el campamento de ellos."),
              ("Creer que leer este cuaderno habilita para instalar un campamento en un terreno real.", "La instalación exige instructor autorizado, norma vigente y permisos del dueño del terreno.", "Aprende aquí el concepto y deja la instalación a personal autorizado.")],
    T=[
        ("abc", "En Geología: ¿qué es un campamento de prospección?", "Un lugar temporal de alojamiento, comida, aseo y bodega para un equipo que trabaja lejos", "Una oficina fija de la empresa donde se archivan los planos del proyecto", "Una mina en explotación con maquinaria pesada y turnos continuos", "El campamento es temporal y sirve de apoyo al equipo; las oficinas y las minas son otras instalaciones."),
        ("abc", "En Geología: ¿qué es un aluvión?", "Un flujo repentino de agua con barro y piedras que baja por una quebrada", "Un tipo de mineral que se forma en el fondo de las quebradas", "Un documento que autoriza instalar un campamento", "El aluvión es un fenómeno del terreno; no es ni un mineral ni un documento."),
        ("abc", "En Geología: ¿qué es el proyecto de prospección?", "El plan que define dónde, cuántos días y con cuántas personas se buscará y se obtendrán muestras", "El informe final que entrega las concentraciones de cada muestra", "El permiso del dueño del terreno para entrar a él", "El proyecto es el plan inicial; el informe y el permiso son otros documentos."),
        ("=", "{F} Llegan 4 personas más al campamento de la ficha, y se mantiene el número de personas por carpa. ¿Cuántas carpas dormitorio hacen falta en total?", "(12+4)//4", "Se suman las personas y se divide entre las que caben en cada carpa.", " carpas"),
        ("abc", "{F} ¿Qué corresponde con los restos de comida del campamento, según la protección del medio ambiente?", "Manejarlos y retirarlos según el plan ambiental del proyecto, sin dejarlos en el terreno", "Enterrarlos en la quebrada seca para que no se vean", "Quemarlos junto a las carpas para reducir su volumen", "Los residuos se retiran según el plan ambiental; enterrarlos o quemarlos daña el entorno y es riesgoso."),
        ("abc", "En Geología: ¿qué institución fiscaliza la seguridad de la actividad minera según la norma vigente?", "La autoridad minera", "El Servicio de Impuestos Internos", "El dueño del terreno donde se instala el campamento", "La seguridad minera la fiscaliza la autoridad minera; el servicio de impuestos revisa tributos y el dueño del terreno solo autoriza el uso."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la quebrada seca junto al campamento?", "Que una crecida repentina tras lluvias arrastre carpas y lesione a las personas", "Que la quebrada tenga poca agua en verano", "Que el suelo de la terraza sea plano", "El riesgo es la posibilidad de daño por la crecida; la quebrada misma es el peligro."),
        ("abc", "{F} Trasladar los dormitorios a una terraza elevada, lejos de la quebrada y de la ladera, es un control de tipo:", "Eliminación o alejamiento, porque quita la exposición al peligro", "Administrativo, porque cambia un horario de trabajo", "De EPP, porque protege a cada persona", "Alejarse del peligro es el primer nivel de la jerarquía; no es un horario ni un equipo personal."),
        ("abc", "{F} Un letrero con las rutas de salida y un simulacro de emergencia son controles de tipo:", "Administrativo, porque informan y organizan la conducta de las personas", "De ingeniería, porque cambian el terreno del campamento", "De eliminación, porque quitan el peligro de la ladera", "Letreros y simulacros informan y ordenan, pero no modifican el lugar ni quitan el peligro."),
        ("abc", "{F} Una estudiante dice: «leí la ficha y el cuaderno, así que puedo ayudar a instalar un campamento en un terreno real». ¿Qué respuesta es correcta?", "Es falso: instalar un campamento exige instructor autorizado, norma vigente y permisos", "Es cierto, si usa casco y botas", "Es cierto, si va con compañeros de curso", "Leer un caso en papel no habilita para trabajar en terreno; el EPP o la compañía tampoco."),
        ("abc", "Durante una visita de ejemplo, ves que de una ladera próxima a las carpas caen piedras. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a sacar de las carpas los objetos de valor", "Subir a la ladera para ver de dónde se desprenden las piedras", "Acercarse a un derrumbe puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("=", "{F} Cada persona consume 3 raciones de comida al día (dato de ejemplo). ¿Cuántas raciones se necesitan para todo el campamento de la ficha durante sus diez días?", "12*10*3", "Se multiplican personas, días y raciones diarias por persona.", " raciones"),
        ("abc", "{F} El jefe dice: «la ladera nunca se ha caído, basta con un letrero que avise del peligro». ¿Cuál es la mejor objeción?", "Un letrero es un control administrativo y no quita el peligro; conviene alejar el campamento de la ladera", "Ninguna, porque un letrero equivale a eliminar el peligro", "Que un letrero solo sirve si está escrito en inglés", "El letrero informa pero la ladera sigue ahí; aun así es útil como complemento, no como único control."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por ayudar a instalar un campamento en un cerro «porque ya viste cómo se hace en clases». ¿Qué respondes?", "Que no, porque esa tarea exige instructor autorizado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque con botas y casco basta", "Que sí, pero solo si es por un día", "Haber visto el concepto en clases no habilita para trabajar en terreno; la duración tampoco."),
    sc=[
        ("En Geología: ¿qué es un peligro?", "Una fuente que puede causar daño, como una ladera con piedras sueltas", "El peligro es la fuente; el riesgo es la posibilidad de daño."),
        ("En el trabajo geológico en terreno: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
        ("¿Qué es un campamento de prospección?", "Un lugar temporal de alojamiento, comida, aseo y bodega para un equipo que trabaja lejos", "El campamento da apoyo temporal al equipo que obtiene las muestras."),
    ],
    op=("El campamento ficticio «Campamento Alfa Demo» alojaría a 8 personas durante una semana, en un lugar junto a un camino de tierra y al pie de una pendiente de piedras sueltas. Escribe (a) cuál es el peligro de la pendiente y cuál el riesgo asociado, (b) un control de eliminación o alejamiento, (c) un control administrativo, (d) por qué el EPP no basta, (e) qué debe hacer una persona que vea caer piedras hacia las carpas.",
        "(a) Peligro: la pendiente de piedras sueltas; riesgo: que una persona sea golpeada por una piedra o resbale. (b) Instalar el campamento en un lugar plano y lejos de la pendiente. (c) Un letrero con la ruta de salida y un simulacro de emergencia. (d) Porque el EPP es la última barrera: no quita el peligro y protege solo a quien lo usa. (e) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias. La instalación la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control de eliminación o alejamiento", "propone un control administrativo", "explica por qué el EPP no basta", "indica no acercarse y avisar"],
        ["hoja con las cinco respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "responder que se acerca a ayudar"],
        "Pregunta: «¿qué control quita la exposición y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe la jerarquía de controles en orden y pon junto a cada nivel un ejemplo inventado de un campamento de prospección.",
    extend="Explica con un ejemplo por qué un simulacro es un control administrativo y no reemplaza alejarse de un peligro.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). «Campamento Cerro Demo», 10 personas. Documentos del campamento: el croquis (dibujo que ubica 3 carpas dormitorio de 4 plazas, 1 comedor, 2 baños, 1 bodega y 1 zona de residuos), "
     "la lista de verificación (una casilla «sí/no» por cada ítem revisado, con fecha y firma), el inventario (qué materiales hay y cuántos), la bitácora (registro diario de hechos y decisiones) y el plan de emergencia (quién avisa, a quién y cómo se sale). "
     "Inventario del primer día: 36 bidones de agua; consumo previsto de ejemplo: 4 bidones por día. Roles: jefe de campamento, geólogo jefe, asistente de geología, prevencionista de riesgos y encargado de logística.")
build(
    O1, 2, F,
    use="Aprenderé los documentos de un campamento de terreno (croquis, lista de verificación, inventario, bitácora y plan de emergencia), los roles del equipo y por qué los registros no se alteran.",
    prior=["Sé qué es un campamento de prospección.", "Sé leer un registro escrito.", "Sé restar y dividir números enteros."],
    explain=[
        "Un campamento se ordena con documentos. El croquis es un dibujo que ubica cada zona: dormitorios, comedor, baños, bodega y residuos. La lista de verificación es una pauta con casillas para comprobar, ítem por ítem, que algo está listo. El inventario dice qué materiales hay y en qué cantidad. La bitácora es el registro diario donde se anotan hechos, decisiones y novedades. El plan de emergencia dice quién avisa, a quién y cómo se sale del lugar.",
        "La higiene exige separar las zonas: los baños y los residuos van lejos del comedor y de la fuente de agua. Un registro útil dice qué se revisó, cuándo y quién lo firmó, y nunca se llena de antemano ni se cambia para que «se vea mejor»: si no se anota la realidad, no se puede decidir bien ni desarmar el campamento con todo cuadrado.",
        f"Cada rol tiene su función: el jefe de campamento coordina; el geólogo jefe dirige el trabajo geológico; el asistente de geología apoya con registros y datos; el prevencionista asesora en riesgos; el encargado de logística lleva el inventario y los abastecimientos. {EMER} {AVISO}",
    ],
    vocab=[("croquis", "dibujo simple que ubica las zonas de un campamento"), ("lista de verificación", "pauta con casillas para comprobar ítem por ítem que algo está listo"), ("inventario", "lista de los materiales que hay y su cantidad"), ("bitácora", "registro diario de hechos y decisiones"), ("plan de emergencia", "documento que dice quién avisa, a quién y cómo se sale del lugar"), ("prevencionista de riesgos", "persona que asesora en prevención de accidentes"), ("encargado de logística", "persona que lleva el inventario y los abastecimientos")],
    worked=[
        ("Calcular un saldo", "Un inventario de ejemplo anota 30 bolsas de basura. Se usaron 18. ¿Cuántas quedan?", ["Se resta lo usado al total.", "30 menos 18 es 12."], "12 bolsas"),
        ("Elegir el documento", "La asistente quiere dejar anotado cada noche cuántas personas durmieron en el campamento y qué incidentes hubo. ¿Qué documento usa?", ["Es un registro diario de hechos.", "Ese registro es la bitácora."], "La bitácora"),
    ],
    mistakes=[("Marcar «sí» en la lista de verificación antes de revisar para ahorrar tiempo.", "Una lista llenada de antemano no refleja la realidad y engaña a quien la lee.", "Cada casilla se marca solo después de comprobar el ítem, con fecha y firma."),
              ("Creer que el croquis reemplaza al plan de emergencia.", "El croquis ubica las zonas; el plan dice quién avisa y cómo se actúa.", "Cada documento se usa para lo que fue hecho.")],
    T=[
        ("abc", "En Geología: ¿qué es una bitácora de campamento?", "Un registro diario donde se anotan hechos, decisiones y novedades de la jornada", "Un dibujo que ubica los dormitorios y la bodega", "Una lista de materiales con sus cantidades", "La bitácora guarda lo que ocurre cada día; el dibujo es el croquis y la lista es el inventario."),
        ("abc", "En Geología: ¿qué es un croquis de campamento?", "Un dibujo simple que ubica cada zona del campamento", "Un permiso que autoriza el uso del terreno", "La pauta con casillas que se marcan tras revisar cada ítem", "El croquis es un dibujo; el permiso y la pauta de verificación son otros documentos."),
        ("abc", "En Geología: ¿para qué sirve una lista de verificación?", "Para comprobar ítem por ítem que algo está listo, con fecha y firma de quien revisó", "Para registrar la hora de llegada de cada vehículo", "Para dibujar el recorrido hacia el centro asistencial", "La lista de verificación certifica revisiones; no registra llegadas ni dibuja recorridos."),
        ("abc", "{F} ¿Qué documento de la ficha define quién avisa a emergencias y cómo se sale del campamento ante un accidente?", "El plan de emergencia", "El inventario", "La lista de verificación", "El plan de emergencia organiza las acciones ante accidentes; el inventario solo cuenta materiales."),
        ("abc", "{F} ¿Qué rol del campamento lleva el inventario y los abastecimientos?", "El encargado de logística", "El prevencionista de riesgos", "El geólogo jefe", "Logística controla materiales; el prevencionista asesora en riesgos y el geólogo jefe dirige el trabajo geológico."),
        ("=", "{F} ¿Cuántas camas quedan libres con las 3 carpas dormitorio del croquis, si ya hay 10 personas?", "3*4-10", "Se calculan las plazas totales y se restan las personas.", " camas"),
        ("abc", "{F} En el croquis la zona de residuos aparece dibujada junto al comedor y a la toma de agua. ¿Qué observación corresponde?", "Debe alejarse del comedor y del agua para cuidar la higiene", "Está bien porque así se retiran más rápido los residuos", "Debe quedar dentro de la bodega para que no huela", "Los residuos se separan del comedor y del agua; ponerlos al lado contamina."),
        ("abc", "{F} En la lista de verificación la casilla «baños listos» está en «sí», pero sin fecha ni firma. ¿Por qué es un registro débil?", "Porque sin fecha ni responsable no se puede saber quién revisó ni cuándo", "Porque los baños nunca deben incluirse en una lista de verificación", "Porque la casilla debería estar siempre en «no»", "Un registro sin fecha ni firma no puede verificarse ni atribuirse a nadie."),
        ("=", "{F} Con el consumo previsto de ejemplo, ¿para cuántos días alcanzan los bidones del primer día?", "36//4", "Se dividen los bidones disponibles entre los que se consumen cada día.", " días"),
        ("abc", "{F} Una asistente dice: «el croquis es solo un dibujo, no hace falta guardarlo». ¿Qué respuesta es correcta?", "Es falso: el croquis sirve de respaldo para ordenar y para verificar después que todo se retiró", "Es cierto, porque el dibujo no tiene valor como documento", "Es cierto, si ya se recuerda dónde quedó cada carpa", "El croquis deja constancia de la ubicación; la memoria de las personas no es un respaldo."),
        ("abc", "{F} Se quiere dejar constancia de quién decidió cambiar la bodega de lugar, qué día y por qué. ¿Dónde se anota?", "En la bitácora, con fecha y responsable", "En el inventario, junto al nombre de cada bidón", "En la lista de verificación de los baños", "La bitácora registra decisiones con fecha y responsable; el inventario cuenta materiales."),
        ("abc", "{F} Al final del tercer día el inventario marca 22 bidones, pero según 36 iniciales y 4 por día debería marcar 24. ¿Qué corresponde?", "Comparar inventario y bitácora, buscar la diferencia de 2 bidones y registrar la explicación", "Cambiar el inventario a 24 para que coincida", "Ignorar la diferencia porque son pocos bidones", "Una diferencia se investiga y se anota; igualar el número sin explicación oculta el problema."),
        ("abc", "{F} Un compañero propone llenar la lista de verificación del día siguiente hoy, «para ganar tiempo». ¿Cuál es la mejor respuesta?", "Que no, porque la lista debe reflejar lo que realmente se comprobó cada día", "Que sí, si después se corrigen solo los ítems con problemas", "Que sí, siempre que se firme con otra letra", "Un registro adelantado no certifica nada; se firma solo lo comprobado."),
    ],
    ctx=("abc", "Un compañero te dice que los números del inventario se pueden «ajustar» antes de la visita de la jefa, porque faltan unos bidones. ¿Qué respondes?", "Que no se altera un registro y que la diferencia se informa a un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, pero solo si faltan pocos", "Que sí, y se avisa después", "Alterar un registro oculta el problema; ante la duda se consulta a un adulto responsable."),
    sc=[
        ("En Geología: ¿qué es un inventario?", "La lista de los materiales que hay y su cantidad", "El inventario permite saber qué hay y cuánto queda."),
        ("En el trabajo de terreno geológico: ¿qué es la bitácora?", "El registro diario de hechos y decisiones", "La bitácora deja constancia de lo ocurrido cada día."),
        ("En un campamento de prospección geológica: ¿qué se hace con una diferencia entre dos registros?", "Se investiga, se anota la explicación y se informa", "Una diferencia real se informa para poder decidir con datos."),
    ],
    op=("Ficha de ejemplo: «Campamento Meseta Demo», 8 personas, 2 carpas dormitorio de 4 plazas. Inventario del primer día: 48 bolsas de basura; consumo previsto de ejemplo: 6 bolsas por día. Escribe (a) cuántos días alcanzan las bolsas, (b) en qué documento anotarías que se decidió mover la bodega y quién lo decidió, (c) qué haces si el inventario del día dos marca 40 bolsas y debería marcar 36, (d) qué rol consultarías si dudas de un riesgo del campamento.",
        "(a) 48 ÷ 6 = 8 días. (b) En la bitácora, con fecha y responsable. (c) Se compara con la bitácora, se busca la diferencia de 4 bolsas, se anota tal cual y se informa al encargado de logística. (d) Al prevencionista de riesgos. Todo se hace por personal autorizado.",
        ["calcula bien los días", "nombra la bitácora", "no altera el registro y lo informa", "nombra el rol adecuado"],
        ["hoja con las cuatro respuestas"],
        ["dividir mal", "cambiar el inventario para que coincida", "confundir el rol del prevencionista con el de logística"],
        "Pregunta: «¿qué pasa con la confianza en el registro si se cambia el dato?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un inventario de tres materiales de campamento con su cantidad y calcula para cuántos días alcanza uno de ellos.",
    extend="Explica con un ejemplo por qué el croquis y el plan de emergencia no cumplen la misma función.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (plan de ejemplo, inventado). «Campamento Loma Demo», 9 personas, 7 días. Criterios de ejemplo del proyecto (la norma vigente puede exigir otros valores): los baños deben quedar a 30 metros o más de la fuente de agua; "
     "la zona de residuos, a 25 metros o más del comedor; los dormitorios, a 50 metros o más de la ladera; la bodega, a 60 metros o más de la quebrada. "
     "Distancias medidas en el croquis: baños a fuente de agua, 20 metros; residuos a comedor, 37 metros; dormitorios a ladera, 35 metros; bodega a quebrada, 80 metros. "
     "Cada persona genera 2 kilos de residuos por día (dato de ejemplo).")
build(
    O1, 3, F,
    use="Aprenderé a analizar el plan de un campamento en papel: comparar distancias con un criterio, detectar incumplimientos, proponer medidas ordenadas por la jerarquía de controles y verificar después.",
    prior=["Sé qué documentos tiene un campamento.", "Sé sumar, restar y multiplicar números enteros.", "Sé la jerarquía de controles."],
    explain=[
        "Analizar un caso en papel significa leer los datos, compararlos con un criterio, decidir qué significan y proponer acciones. Un criterio es la regla con que se compara; aquí son distancias mínimas de separación, es decir, la menor distancia permitida entre dos instalaciones. Un incumplimiento ocurre cuando la medida real queda por debajo del mínimo; la diferencia se calcula restando la medida real al mínimo exigido.",
        "Cumplir una distancia mínima reduce el riesgo, pero no elimina el peligro: una bodega a 80 metros de una quebrada sigue estando cerca de una posible crecida. Frente a un incumplimiento se proponen medidas con la jerarquía de controles: primero alejar o eliminar, luego controles de ingeniería, después administrativos y al final el EPP. Después de aplicar una medida se vuelve a medir para verificar que ahora se cumple.",
        f"Los datos reales los mide personal autorizado y los criterios los fija el proyecto según la norma vigente; aquí solo practicas el razonamiento con números de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("criterio", "regla con la que se compara una medida"), ("distancia mínima de separación", "menor distancia permitida entre dos instalaciones"), ("incumplimiento", "situación en que una medida no alcanza lo exigido por el criterio"), ("holgura", "diferencia por encima del mínimo exigido"), ("verificar", "volver a comprobar con nuevos datos que una medida funcionó")],
    worked=[
        ("Cumple o no cumple", "Un criterio de ejemplo exige que un estanque de combustible quede a 40 metros o más de las carpas. El croquis mide 55 metros. ¿Cumple y con cuánta holgura?", ["55 es mayor que 40, así que cumple.", "55 menos 40 son 15 metros de holgura."], "Cumple, con 15 metros de holgura"),
        ("Calcular lo que falta", "Otro criterio de ejemplo exige 45 metros entre un comedor y un pozo de aguas servidas. El croquis mide 28 metros. ¿Cuánto falta?", ["28 es menor que 45, así que no cumple.", "45 menos 28 son 17 metros."], "No cumple; faltan 17 metros"),
    ],
    mistakes=[("Creer que si una distancia cumple, el peligro desapareció.", "La distancia mínima reduce el riesgo, pero la quebrada o la ladera siguen existiendo.", "Se mantienen otros controles: plan de emergencia, rutas de salida y vigilancia del clima."),
              ("Marcar «cumple» una medida que no alcanza el mínimo para no atrasar la instalación.", "Un registro falso oculta un incumplimiento real.", "Se anota la medida real, se informa el incumplimiento y se propone una corrección.")],
    T=[
        ("abc", "En Geología: ¿qué es un criterio de revisión de un campamento?", "La regla con la que se compara una medida real, como una distancia mínima", "La medida real que se anota en el croquis", "El permiso firmado por el dueño del terreno", "El criterio es la regla de comparación; la medida real es el dato que se compara."),
        ("abc", "En Geología: ¿qué es un incumplimiento?", "Una situación en que la medida real no alcanza lo que exige el criterio", "Una medida que supera ampliamente el mínimo", "El registro diario de un campamento", "El incumplimiento aparece cuando la medida queda por debajo de lo exigido."),
        ("abc", "En Geología: ¿qué significa «distancia mínima de separación» entre dos instalaciones?", "La menor distancia permitida entre ellas", "La mayor distancia que se puede medir en un croquis", "La distancia que recorre una persona entre ambas en un día", "Un mínimo es el valor más bajo permitido; medir menos que eso incumple."),
        ("=", "{F} ¿Cuántos metros le faltan a la separación entre baños y fuente de agua para llegar al mínimo?", "30-20", "Se resta la medida real al mínimo exigido.", " metros"),
        ("abc", "{F} ¿Qué pares de instalaciones incumplen su criterio?", "Baños con fuente de agua, y dormitorios con ladera", "Residuos con comedor, y bodega con quebrada", "Solo baños con fuente de agua", "Baños (20 de 30) y dormitorios (35 de 50) quedan bajo el mínimo; los otros dos lo superan."),
        ("=", "{F} ¿Cuántos metros por sobre el mínimo está la separación entre residuos y comedor?", "37-25", "Se resta el mínimo a la medida real.", " metros"),
        ("abc", "{F} ¿Qué medida corresponde para los dormitorios, según la jerarquía de controles?", "Trasladar las carpas hasta quedar al menos a 50 metros de la ladera", "Entregar un casco a cada persona y dejar las carpas donde están", "Pegar un letrero en cada carpa y no moverlas", "Alejar elimina la exposición, que es el nivel más efectivo; casco y letrero actúan en niveles inferiores."),
        ("abc", "{F} Tras trasladar los baños, se mide de nuevo y marca 34 metros. ¿Qué conclusión corresponde?", "Ahora cumple, porque 34 supera el mínimo de 30", "No cumple, porque debería medir exactamente 30", "No se puede concluir nada sin volver a dibujar todo el croquis", "El criterio pide 30 metros o más, y 34 es mayor que 30."),
        ("abc", "{F} Un compañero dice: «como la bodega está a 80 metros de la quebrada y cumple, la quebrada ya no es un peligro». ¿Qué respuesta es correcta?", "Es falso: la distancia reduce el riesgo, pero la quebrada sigue siendo un peligro por crecidas", "Es cierto, porque cumplir un mínimo elimina cualquier peligro", "Es cierto, porque 80 es mayor que 60", "Cumplir un mínimo disminuye el riesgo; el peligro de la crecida no desaparece."),
        ("abc", "{F} La jefa te pide marcar «cumple» en dormitorios aunque midan 35 metros, para no atrasar la instalación. ¿Qué haces?", "No lo marco: anoto la medida real, informo el incumplimiento y consulto a un adulto responsable", "Lo marco y lo corrijo la próxima semana", "Lo marco, pero escribo 50 en la medida", "Marcar «cumple» sin cumplir es un registro falso; la medida real se anota e informa."),
        ("=", "{F} ¿Cuántos kilos de residuos se generan en total durante los siete días?", "9*7*2", "Se multiplican personas, días y kilos diarios por persona.", " kilos"),
        ("abc", "{F} ¿Qué orden de análisis es el adecuado?", "Leer los datos, compararlos con el criterio, detectar incumplimientos, proponer medidas por jerarquía y volver a medir", "Proponer medidas primero, medir al final y no comparar con el criterio", "Medir una sola vez al inicio y confiar en que las medidas funcionaron", "El análisis parte de los datos y termina verificando; saltarse pasos deja problemas sin comprobar."),
        ("abc", "{F} Se propone dejar a los baños donde están y entregar mascarillas al personal. ¿Qué observación corresponde?", "La mascarilla es EPP: no corrige la distancia, que se resuelve alejando los baños de la fuente de agua", "Es correcto, porque el EPP basta para cumplir cualquier distancia", "Es correcto, porque las mascarillas aumentan la distancia entre instalaciones", "El EPP protege a la persona, pero la medida no cumple el criterio de separación."),
    ],
    ctx=("abc", "Una compañera dice que en el croquis de ejemplo se pueden «acomodar» las distancias para que todo cumpla antes de la entrega. ¿Qué respondes?", "Que no se alteran las medidas y que cualquier duda se consulta con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, pero solo las distancias más grandes", "Que sí, y después se corrige si alguien lo nota", "Alterar medidas oculta incumplimientos reales; ante la duda se consulta a un adulto responsable."),
    sc=[
        ("En Geología: ¿qué es un criterio de revisión?", "La regla con la que se compara una medida real", "El criterio permite decidir si algo cumple o no cumple."),
        ("En el campamento de terreno: ¿cómo se calcula cuánto falta para llegar a un mínimo?", "Se resta la medida real al mínimo exigido", "La diferencia entre el mínimo y la medida real es lo que falta."),
        ("¿Qué se hace después de aplicar una medida correctiva?", "Se vuelve a medir para verificar que ahora cumple", "Verificar con nueva medición confirma que la medida funcionó."),
    ],
    op=("Ficha de ejemplo: «Campamento Altiplano Demo». Criterios de ejemplo: comedor a 40 metros o más de la zona de residuos; carpas a 30 metros o más de un camino de tránsito de vehículos. Medidas del croquis: comedor a residuos, 32 metros; carpas a camino, 50 metros. Escribe (a) qué par incumple y cuántos metros faltan, (b) con cuántos metros de holgura cumple el otro, (c) una medida de la jerarquía para corregir el incumplimiento, (d) cómo verificarías que quedó bien.",
        "(a) Comedor a residuos: 32 es menor que 40, faltan 8 metros. (b) Carpas a camino: 50 − 30 = 20 metros de holgura. (c) Alejar la zona de residuos del comedor hasta quedar a 40 metros o más. (d) Volver a medir en el croquis y anotar el nuevo valor con fecha y responsable. Todo lo hace personal autorizado.",
        ["detecta el par que incumple", "calcula bien los metros que faltan", "calcula bien la holgura", "propone una medida de alta jerarquía", "propone verificar con nueva medición"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "proponer solo EPP", "no verificar después"],
        "Pregunta: «¿qué número comparas con qué número?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos criterios de distancia y dos medidas del croquis; indica cuál cumple y cuál no, y calcula la diferencia.",
    extend="Explica por qué cumplir una distancia mínima no elimina del todo un peligro.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). «Campamento Meseta Demo», 14 personas durante 6 días. Valores de ejemplo (los reales los fija el proyecto según la norma vigente): consumo de agua de 12 litros por persona al día; "
     "bidones de 24 litros; 1 kilo de residuos por persona al día; bolsas de residuos con capacidad de 12 kilos; carpas dormitorio para 4 personas. Se prevé una reserva de un día extra de agua para todo el equipo.")
build(
    O1, 4, F,
    use="Aprenderé a calcular en papel las cantidades de un campamento: agua, envases, residuos y carpas, redondeando hacia arriba cuando corresponde, agregando una reserva y verificando el balance al desarmar.",
    prior=["Sé qué documentos tiene un campamento.", "Sé multiplicar y dividir números enteros.", "Sé comparar una medida con un criterio."],
    explain=[
        "Para calcular lo que necesita un campamento se multiplican personas, días y consumo por persona. Con el total se calcula cuántos envases hacen falta dividiendo entre la capacidad de cada uno. Cuando la división no es exacta y no se puede entregar una fracción de carpa o de envase, se redondea hacia arriba: 3,5 carpas significa 4 carpas, porque con 3 quedarían personas sin lugar.",
        "Una reserva es una cantidad extra que se lleva por si algo se atrasa o se pierde; se suma al total calculado. Todos los valores del cálculo son supuestos: los reales los fija el proyecto, según la norma vigente. Al desarmar, el balance de materiales compara lo que entró, lo que se consumió y lo que sale: si las cuentas no cuadran, falta algo por ubicar y no se cierra el campamento hasta explicar la diferencia.",
        f"Estos cálculos los revisa el encargado de logística con el jefe de campamento. Aquí aprendes el razonamiento con números de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("consumo", "cantidad que usa una persona en un tiempo, por ejemplo litros al día"), ("capacidad", "cantidad máxima que cabe en un envase o recinto"), ("redondear hacia arriba", "subir al siguiente entero cuando no se puede usar una fracción"), ("reserva", "cantidad extra que se lleva por si algo se atrasa o se pierde"), ("balance de materiales", "comparación de lo que entró, lo consumido y lo que sale")],
    worked=[
        ("Agua y envases", "Un equipo de ejemplo de 5 personas trabaja 3 días con 10 litros por persona al día, y se usan envases de 25 litros. ¿Cuántos envases hacen falta?", ["Total: 5 × 3 × 10 = 150 litros.", "150 dividido por 25 da 6 envases exactos."], "6 envases"),
        ("Redondeo hacia arriba", "Un equipo de ejemplo de 9 personas usa carpas de 4 plazas. ¿Cuántas carpas necesita?", ["9 dividido por 4 es 2,25, no es entero.", "Con 2 carpas quedan personas sin lugar: se sube a 3."], "3 carpas"),
    ],
    mistakes=[("Redondear 3,5 carpas a 3 porque «la mitad no cuenta».", "Con 3 carpas quedarían personas sin lugar donde dormir.", "Cuando no se puede usar una fracción se redondea hacia arriba."),
              ("Dar un resultado sin unidad ni supuestos, por ejemplo «1008».", "Nadie puede verificar un número sin saber si son litros, kilos o bidones ni qué consumo se supuso.", "Se anota la unidad y los supuestos del cálculo.")],
    T=[
        ("abc", "En Geología: ¿qué significa redondear hacia arriba al calcular carpas?", "Subir al siguiente entero cuando no se puede usar una fracción de carpa", "Bajar al entero anterior para ahorrar material", "Dejar el decimal tal cual en la lista de compras", "Una fracción de carpa no existe; si faltan plazas se sube al siguiente entero."),
        ("abc", "En Geología: ¿qué es una reserva de agua en un campamento?", "Una cantidad extra que se lleva por si algo se atrasa o se pierde", "El agua que ya se consumió en el primer día", "El agua que se anota en la bitácora como gasto", "La reserva es un margen de seguridad que se suma al cálculo."),
        ("abc", "En Geología: ¿qué es el balance de materiales al desarmar un campamento?", "Comparar lo que entró, lo que se consumió y lo que sale, para comprobar que no queda nada", "Pesar cada material en una balanza de precisión", "Dibujar de nuevo el croquis con las carpas", "El balance compara entradas, consumos y salidas; no es una pesada ni un dibujo."),
        ("=", "{F} ¿Cuántos litros de agua se consumen en total durante los seis días, sin contar la reserva?", "14*6*12", "Se multiplican personas, días y litros diarios por persona.", " litros"),
        ("=", "{F} ¿Cuántos bidones de 24 litros se necesitan para ese consumo?", "(14*6*12)//24", "Se divide el consumo total entre la capacidad de cada bidón.", " bidones"),
        ("=", "{F} ¿Cuántas bolsas de residuos se llenan en total durante los seis días?", "(14*6*1)//12", "Se calculan los kilos totales y se dividen entre los que caben en cada bolsa.", " bolsas"),
        ("=", "{F} ¿Cuántas carpas dormitorio hacen falta, redondeando hacia arriba?", "(14+3)//4", "Se suman 3 antes de dividir entre 4 para subir al siguiente entero.", " carpas"),
        ("=", "{F} Con la reserva de un día extra de agua, ¿cuántos litros hay que llevar en total?", "14*6*12+14*12", "Se suma al consumo total el consumo de un día de todo el equipo.", " litros"),
        ("abc", "{F} El valor de 12 litros por persona al día es:", "Un dato de ejemplo; el real lo fija el proyecto según la norma vigente", "El mínimo legal para cualquier campamento del país", "El consumo medido en todos los campamentos de prospección", "El valor está rotulado de ejemplo; los reales dependen del proyecto y de la norma vigente."),
        ("abc", "{F} El jefe propone bajar el agua a 6 litros por persona al día «para ahorrar bidones». ¿Cuál es la mejor objeción?", "Que el valor debe respetar lo que fije el proyecto y la norma vigente, porque reducirlo sin criterio compromete la salud y la higiene", "Ninguna, porque menos agua siempre es más seguro", "Que los bidones de 24 litros solo sirven para el agua de la cocina", "El agua es un insumo de salud e higiene; el recorte debe basarse en la norma, no en el ahorro."),
        ("abc", "{F} Al desarmar, el balance anota: entraron 42 bidones llenos, se consumió el agua de 36 y se cuentan 4 bidones aún llenos. ¿Qué corresponde concluir?", "Faltan 2 bidones por ubicar y no se cierra el balance hasta explicarlo", "Cuadra, porque se usaron casi todos", "Sobran 2 bidones, que se pueden dejar en el terreno", "42 menos 36 menos 4 da 2; la diferencia se busca y se registra, no se deja en el terreno."),
        ("=", "{F} Si el equipo creciera a 16 personas con los mismos días y consumos, ¿cuántos bidones de 24 litros más que los 42 originales harían falta?", "(16*6*12)//24-42", "Se calcula el total de bidones con 16 personas y se resta los 42 iniciales.", " bidones"),
        ("abc", "{F} Un asistente dice que 3,5 carpas se redondean a 3. ¿Cuál es el efecto de ese error con 14 personas?", "Dos personas quedarían sin lugar, así que hay que subir a 4 carpas", "Ninguno, porque en una carpa siempre caben más personas", "Sobrarían 2 carpas, que se devuelven", "Tres carpas alojan 12 personas, y hay 14."),
    ],
    ctx=("abc", "Una compañera te ofrece «adelantar» la lista de compras de un campamento real con estos cálculos de clase, sin consultar al encargado. ¿Qué respondes?", "Que los números del cuaderno son de ejemplo y que los reales los calcula personal autorizado; lo consultarás con un adulto responsable", "Que sí, porque los cálculos están bien hechos", "Que sí, pero redondeando hacia abajo para ahorrar", "Los valores son de ejemplo: los reales dependen del proyecto y de la norma vigente."),
    sc=[
        ("En Geología: ¿qué es una reserva?", "Una cantidad extra que se lleva por si algo se atrasa o se pierde", "La reserva agrega un margen a lo calculado."),
        ("En el cálculo de un campamento: ¿cuándo se redondea hacia arriba?", "Cuando no se puede usar una fracción de carpa o de envase", "Una fracción de envase no existe, así que se sube al siguiente entero."),
        ("¿Qué se debe anotar junto a un resultado calculado?", "La unidad y los supuestos del cálculo", "Con unidad y supuestos otra persona puede verificarlo."),
    ],
    op=("Ficha de ejemplo: «Campamento Salar Demo», 10 personas durante 5 días. Valores de ejemplo: 10 litros de agua por persona al día; bidones de 25 litros; carpas dormitorio para 4 personas. Escribe (a) el consumo total de agua, (b) cuántos bidones hacen falta, (c) cuántas carpas hacen falta, (d) por qué los números son de ejemplo y quién decide los reales.",
        "(a) 10 × 5 × 10 = 500 litros. (b) 500 ÷ 25 = 20 bidones. (c) 10 ÷ 4 = 2,5, se sube a 3 carpas. (d) Porque son supuestos del ejercicio: los reales los fija el proyecto según la norma vigente y los calcula personal autorizado.",
        ["calcula bien el consumo", "calcula bien los bidones", "redondea hacia arriba las carpas", "explica que los valores son de ejemplo"],
        ["hoja con las cuatro respuestas"],
        ["redondear hacia abajo las carpas", "olvidar las unidades", "presentar los valores como reales"],
        "Pregunta: «¿qué pasaría con las personas si pones 2 carpas?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el agua y los bidones de un equipo inventado de 6 personas durante 4 días, con 10 litros por persona al día y bidones de 20 litros.",
    extend="Explica con un ejemplo por qué una reserva puede ser necesaria aunque el cálculo haya sido exacto.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Proyecto Salar Demo» de la empresa ficticia «Minera Demo» debe trasladar al campamento un generador portátil de 80 kilos, una bomba de agua de 35 kilos, dos cajas de instrumentos de 12 kilos cada una y un receptor de posicionamiento satelital. "
     "El camino es de tierra, con pendientes y tramos resbaladizos tras la lluvia. Peligros anotados: levantar y mover cargas pesadas a mano, un vehículo cargado en camino irregular, combustible del generador, partes con filo o calientes y cajas que pueden caerse. Las masas son datos de ejemplo.")
build(
    O2, 1, F,
    use="Aprenderé qué son los equipos, instrumentos y accesorios de una prospección, qué peligros tiene su traslado y cómo se ordenan las medidas de prevención, sin aprender a instalarlos ni a usarlos.",
    prior=["Sé qué es un campamento de prospección.", "Sé distinguir peligro y riesgo.", "Sé la jerarquía de controles."],
    explain=[
        "En una prospección se usan equipos, instrumentos y accesorios. Un equipo es una máquina o conjunto que realiza un trabajo, como un generador de electricidad o una bomba de agua. Un instrumento sirve para medir u orientarse, como una brújula o un receptor de posicionamiento satelital. Un accesorio es una pieza complementaria, como un cable, una batería o un trípode. Transportar significa llevar todo esto hasta el lugar de trabajo y devolverlo, con registro de lo que sale y lo que vuelve.",
        "Trasladar cargas tiene peligros propios: el manejo manual de cargas puede lesionar la espalda, un vehículo cargado se vuelve inestable en caminos irregulares, el combustible puede derramarse o encenderse y una caja mal sujeta puede caer. Las medidas se ordenan con la jerarquía de controles: por ejemplo, usar ayudas mecánicas o repartir la carga entre varias personas son controles de ingeniería u organizativos, y los guantes y el calzado son EPP. Los límites de peso y las formas de transporte las fija la norma vigente.",
        f"Toda instalación o armado de un equipo debe seguir las indicaciones del fabricante y hacerlo personal autorizado; este cuaderno no enseña esos pasos. {EMER} {AVISO}",
    ],
    vocab=[("equipo", "máquina o conjunto que realiza un trabajo, como un generador"), ("instrumento", "aparato que sirve para medir u orientarse, como una brújula"), ("accesorio", "pieza complementaria de un equipo, como un cable o una batería"), ("manejo manual de cargas", "levantar o mover cargas con las manos, sin máquinas"), ("indicaciones del fabricante", "instrucciones oficiales de quien fabricó el equipo"), ("carga útil", "peso máximo que un vehículo puede llevar")],
    worked=[
        ("Clasificar un objeto", "Un asistente de ejemplo anota estos objetos: una brújula, una bomba de agua y un cable de extensión. ¿Cómo se clasifica cada uno?", ["La brújula sirve para orientarse: es un instrumento.", "La bomba hace un trabajo: es un equipo, y el cable es un accesorio."], "Brújula: instrumento; bomba: equipo; cable: accesorio"),
        ("Peligro de traslado", "Un compresor de ejemplo se lleva en la parte trasera de una camioneta sin amarras, por un camino con baches. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la carga sin sujetar, que puede moverse.", "El riesgo es que el compresor se desplace o caiga y lesione a alguien o dañe el vehículo."], "Peligro: carga sin sujetar; riesgo: que se desplace o caiga y cause daño"),
    ],
    mistakes=[("Creer que si se puede levantar una carga, entonces se puede cargar sin ayuda.", "El manejo manual de cargas tiene límites fijados por la norma vigente y puede causar lesiones.", "Se usan ayudas mecánicas o varias personas, según lo que indique la norma."),
              ("Creer que leer sobre un equipo habilita para armarlo o encenderlo.", "El armado y el uso siguen las indicaciones del fabricante y los hace personal autorizado.", "Aprende aquí el concepto y deja el armado a personal autorizado.")],
    T=[
        ("abc", "En Geología: ¿qué es un instrumento de terreno?", "Un aparato que sirve para medir u orientarse, como una brújula", "Una máquina que genera electricidad para el campamento", "Una pieza complementaria como un cable", "El instrumento mide u orienta; el generador es un equipo y el cable es un accesorio."),
        ("abc", "En Geología: ¿qué es un accesorio?", "Una pieza complementaria de un equipo, como una batería o un cable", "Un documento que acompaña al equipo", "El conjunto completo de máquinas de un proyecto", "El accesorio es una pieza que complementa; los documentos y los conjuntos son otra cosa."),
        ("abc", "En Geología: ¿qué es la carga útil de un vehículo?", "El peso máximo que ese vehículo puede llevar", "El peso del vehículo vacío", "El combustible que cabe en su estanque", "La carga útil es el máximo que se puede transportar; el peso vacío es otra cosa."),
        ("abc", "{F} ¿Cuál de los objetos de la ficha es un instrumento?", "El receptor de posicionamiento satelital", "El generador portátil", "La bomba de agua", "El receptor sirve para ubicarse; el generador y la bomba son equipos que realizan un trabajo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a mover a mano el generador de 80 kilos?", "Que una persona se lesione la espalda o que el generador caiga sobre ella", "Que el generador consuma combustible", "Que el generador sea de color oscuro", "El riesgo es la posibilidad de daño; el consumo y el color no son un daño a las personas."),
        ("abc", "{F} Usar una ayuda mecánica o repartir la carga entre varias personas, según indique la norma vigente, es un control de tipo:", "Ingeniería u organización del trabajo, porque cambia cómo se mueve la carga", "De EPP, porque protege el cuerpo de cada persona", "De eliminación, porque la carga desaparece", "Cambiar el modo de mover la carga actúa sobre el trabajo; el EPP solo protege a quien lo usa."),
        ("=", "{F} ¿Cuántos kilos pesan juntas las dos cajas de instrumentos, el generador y la bomba?", "12+12+80+35", "Se suman los pesos de los cuatro bultos de la ficha.", " kilos"),
        ("abc", "{F} Un estudiante dice: «leí la ficha, así que puedo conectar y encender el generador del proyecto». ¿Qué respuesta es correcta?", "Es falso: el armado y la puesta en marcha siguen el manual del fabricante y los hace personal autorizado", "Es cierto, si usa guantes", "Es cierto, si el generador es pequeño", "Una ficha en papel no habilita para operar equipos; los guantes o el tamaño tampoco."),
        ("abc", "{F} Durante el traslado, una caja se resbala de la camioneta y un vehículo cercano se detiene bruscamente. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a levantar la caja de inmediato", "Mover el vehículo para despejar el camino", "En una zona de riesgo, acercarse sin formación puede causar otro accidente."),
        ("abc", "En Geología: ¿por qué conviene que dos personas trasladen una caja pesada en lugar de una sola?", "Porque repartir la carga reduce el riesgo de lesión, si la norma vigente lo permite", "Porque con dos personas el peso de la caja disminuye", "Porque así se evita registrar el traslado", "El peso de la caja no cambia, pero repartirlo reduce el esfuerzo de cada persona."),
        ("abc", "{F} El combustible del generador se transporta en un recipiente sin tapa y sin rotular. ¿Cuál es la observación correcta?", "Es un incumplimiento: el combustible se transporta según la norma vigente, en envases adecuados y rotulados", "Está bien si el recipiente es pequeño", "Está bien porque el combustible no cambia de lugar", "Los combustibles exigen envases adecuados y rotulación según la norma vigente."),
        ("=", "{F} Un vehículo de ejemplo tiene una carga útil de 200 kilos. ¿Cuántos kilos le sobran luego de cargar los bultos de la ficha?", "200-(12+12+80+35)", "Se resta el peso total de los bultos a la carga útil.", " kilos"),
        ("abc", "{F} El conductor dice que el camino está resbaladizo y propone viajar igual para no atrasarse. ¿Cuál es la mejor respuesta?", "Informar al jefe y esperar una decisión de personal autorizado, antes de arriesgar a las personas y a la carga", "Viajar más rápido para llegar antes de otra lluvia", "Cargar más peso para dar estabilidad al vehículo", "Un camino con riesgo se informa y se decide por la autoridad responsable; apurarse o sobrecargar aumenta el riesgo."),
    ],
    ctx=("abc", "Un familiar te pide que lo ayudes a levantar y mover un generador pesado de su taller «como en la clase de geología». ¿Qué respondes?", "Que no, porque mover cargas pesadas y equipos exige formación y norma vigente, y que consultarás con un adulto responsable", "Que sí, si es solo un momento", "Que sí, si te pones guantes", "Haber visto el concepto en clases no habilita para mover cargas pesadas; el tiempo o los guantes no cambian el riesgo."),
    sc=[
        ("En Geología: ¿qué es un equipo?", "Una máquina o conjunto que realiza un trabajo, como un generador", "El equipo hace un trabajo; el instrumento mide u orienta."),
        ("En el trabajo de terreno: ¿qué es el manejo manual de cargas?", "Levantar o mover cargas con las manos, sin máquinas", "El manejo manual de cargas puede lesionar y tiene límites fijados por la norma."),
        ("¿Quién arma y pone en marcha un equipo de terreno?", "Personal autorizado, siguiendo las indicaciones del fabricante", "El armado exige formación y seguir el manual del fabricante."),
    ],
    op=("Ficha de ejemplo: el proyecto ficticio «Proyecto Cordón Demo» debe trasladar al campamento un compresor de 60 kilos, una caja de instrumentos de 15 kilos, una bomba de agua de 25 kilos y una balanza de campo de 10 kilos. Escribe (a) cuáles son equipos, cuál instrumento y cuál accesorio posible, (b) un peligro del traslado y su riesgo, (c) un control de ingeniería u organización para mover la carga, (d) qué deberías hacer si observas que una carga se cae durante un traslado real.",
        "(a) Equipos: compresor y bomba de agua; instrumento: la balanza de campo; accesorio posible: un cable o una batería. (b) Peligro: carga pesada de 60 kilos movida a mano; riesgo: lesión de espalda o caída de la carga. (c) Usar una ayuda mecánica o repartir la carga entre varias personas, según la norma vigente. (d) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias. El traslado real lo hace personal autorizado.",
        ["clasifica equipo, instrumento y accesorio", "distingue peligro y riesgo", "propone un control de ingeniería u organización", "indica no acercarse y avisar"],
        ["hoja con las cuatro respuestas"],
        ["llamar equipo a la balanza", "proponer solo guantes", "responder que se acerca a ayudar"],
        "Pregunta: «¿qué control cambia cómo se mueve la carga y no depende de la fuerza de una persona?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Haz una lista inventada de seis objetos de una prospección y clasifícalos en equipo, instrumento o accesorio.",
    extend="Explica con un ejemplo por qué el EPP no corrige un traslado mal planificado.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). «Proyecto Cuenca Demo». Lista de equipos del proyecto: un generador portátil, una balanza de campo y un receptor de posicionamiento. "
     "Documentos: el manual del fabricante (usos permitidos, límites, mantención y advertencias), la hoja de vida de cada equipo (historial de mantenciones y calibraciones), el certificado de calibración (fecha y vigencia), "
     "el acta de entrega (qué equipos salen de bodega, quién los entrega y quién los recibe) y la hoja de ruta del traslado. "
     "Datos de ejemplo: el generador lleva 150 horas de uso y su manual pide mantención cada 200 horas; la balanza fue calibrada hace 120 días y su certificado vale 180 días; el certificado del receptor venció hace 10 días. "
     "Roles: encargado de bodega, conductor autorizado, técnico de mantención, geólogo jefe y asistente de geología.")
build(
    O2, 2, F,
    use="Aprenderé qué son la calibración y la mantención preventiva, qué documentos acompañan a un equipo de terreno y qué rol cumple cada persona, para saber qué se consulta antes de enviarlo a trabajar.",
    prior=["Sé distinguir equipo, instrumento y accesorio.", "Sé qué es un registro.", "Sé restar y dividir números enteros."],
    explain=[
        "Cada equipo de terreno tiene documentos. El manual del fabricante dice para qué se puede usar, qué límites tiene y cada cuánto necesita mantención; se siguen siempre sus indicaciones. La hoja de vida es el historial del equipo: mantenciones, calibraciones y reparaciones. El certificado de calibración dice cuándo se calibró un instrumento y hasta cuándo vale. El acta de entrega deja constancia de qué sale de bodega, quién lo entrega y quién lo recibe.",
        "La calibración consiste en comparar un instrumento con un patrón y ajustarlo para que mida bien; vence con el tiempo y, vencida, el instrumento no debe usarse en el proyecto hasta recalibrarlo. La mantención preventiva son revisiones periódicas que se hacen antes de que el equipo falle, por ejemplo cada cierto número de horas de uso. Un registro útil dice qué se hizo, cuándo, con cuántas horas y quién lo firmó.",
        f"Cada rol tiene su función: el encargado de bodega entrega y recibe equipos; el conductor autorizado maneja el vehículo; el técnico de mantención hace y registra las mantenciones; el asistente de geología apoya con registros y datos. {EMER} {AVISO}",
    ],
    vocab=[("manual del fabricante", "documento oficial de quien fabricó el equipo, con usos, límites y mantención"), ("hoja de vida", "historial de mantenciones, calibraciones y reparaciones de un equipo"), ("calibración", "comparar un instrumento con un patrón y ajustarlo para que mida bien"), ("vigencia", "tiempo durante el cual un certificado o una calibración es válido"), ("mantención preventiva", "revisión periódica que se hace antes de que el equipo falle"), ("acta de entrega", "documento que deja constancia de qué equipo se entrega y a quién")],
    worked=[
        ("Días que quedan", "Un instrumento de ejemplo se calibra cada 100 días y fue calibrado hace 85 días. ¿Cuántos días le quedan de vigencia?", ["La vigencia total es 100 días.", "100 menos 85 son 15 días."], "15 días"),
        ("Elegir el documento", "El técnico de un proyecto de ejemplo quiere saber cuándo se cambió por última vez el filtro de una bomba y cuántas horas de uso tenía en ese momento. ¿Qué documento consulta?", ["Se necesita el historial del equipo.", "El historial de mantenciones está en la hoja de vida."], "La hoja de vida del equipo"),
    ],
    mistakes=[("Creer que un instrumento calibrado una vez sirve para siempre.", "La calibración tiene vigencia y vence; después el instrumento puede medir mal.", "Se revisa la fecha del certificado y se recalibra antes de que venza."),
              ("Anotar «mantención ok» sin fecha, horas ni firma.", "Sin esos datos no se puede comprobar qué se hizo ni cuándo toca la siguiente.", "Se anota qué se hizo, cuándo, con cuántas horas de uso y quién lo firmó.")],
    T=[
        ("abc", "En Geología: ¿qué es la calibración de un instrumento?", "Compararlo con un patrón y ajustarlo para que mida correctamente", "Limpiar su estuche antes de guardarlo", "Anotar su peso en la lista de equipos", "La calibración asegura que el instrumento mida bien; limpiar o pesar no lo hace."),
        ("abc", "En Geología: ¿qué es la mantención preventiva de un equipo?", "Revisiones periódicas que se hacen antes de que el equipo falle", "Reparaciones que se hacen solo después de una falla", "El traslado del equipo a la bodega al terminar el proyecto", "La mantención preventiva se hace antes de la falla; reparar después de la falla es correctiva."),
        ("abc", "En Geología: ¿para qué sirve el manual del fabricante?", "Para conocer los usos permitidos, los límites y la mantención que indica quien fabricó el equipo", "Para registrar quién retiró el equipo de la bodega", "Para dibujar la ruta del traslado hasta el campamento", "El manual contiene las indicaciones del fabricante; el acta y la hoja de ruta son otros documentos."),
        ("abc", "{F} ¿Qué documento de la ficha muestra el historial de mantenciones y calibraciones de un equipo?", "La hoja de vida", "El acta de entrega", "La hoja de ruta", "La hoja de vida guarda el historial; el acta registra entregas y la hoja de ruta el traslado."),
        ("abc", "{F} ¿Qué documento deja constancia de qué equipos salen de la bodega y quién los recibe?", "El acta de entrega", "El manual del fabricante", "El certificado de calibración", "El acta registra la entrega; el manual y el certificado informan sobre el equipo."),
        ("=", "{F} ¿Cuántas horas de uso le faltan al generador para llegar a su mantención?", "200-150", "Se resta lo usado al número de horas que indica el manual.", " horas"),
        ("=", "{F} ¿Cuántos días de vigencia le quedan al certificado de la balanza?", "180-120", "Se resta el tiempo transcurrido a la vigencia total del certificado.", " días"),
        ("abc", "{F} ¿Quién puede manejar el vehículo que traslada los equipos?", "El conductor autorizado por la empresa", "Cualquier integrante del equipo que ya haya viajado de acompañante", "El asistente de geología que leyó la hoja de ruta", "Conducir exige autorización; haber viajado o leer un documento no lo reemplaza."),
        ("abc", "{F} Un equipo llega a la bodega sin su manual del fabricante. ¿Qué corresponde?", "Informar al encargado, no usarlo hasta contar con las indicaciones y registrar la falta", "Usarlo igual, porque otros equipos parecidos funcionan igual", "Pedir a un compañero que recuerde cómo se usa", "Sin indicaciones del fabricante no se debe usar un equipo; recordar o suponer no las reemplaza."),
        ("abc", "{F} ¿Qué corresponde hacer con el receptor de posicionamiento, cuyo certificado venció hace 10 días?", "No usarlo para el proyecto hasta recalibrarlo y registrarlo en su hoja de vida", "Usarlo, porque 10 días no cambian nada", "Cambiar la fecha del certificado para que figure vigente", "Un certificado vencido exige recalibrar; alterarlo es falsear un registro."),
        ("abc", "{F} El técnico anota «mantención ok» sin fecha, horas ni firma. ¿Por qué es un registro débil?", "Porque sin esos datos no se puede comprobar qué se hizo ni cuándo toca la próxima", "Porque las mantenciones nunca se anotan por escrito", "Porque el registro debería llevar solo la fecha", "Un registro útil dice qué, cuándo, con cuántas horas y quién; con menos datos no sirve."),
        ("=", "{F} Si el generador se usa 5 horas al día, ¿en cuántos días llega a las 200 horas de su mantención?", "(200-150)//5", "Se calculan las horas que faltan y se dividen entre las horas de uso diario.", " días"),
        ("abc", "{F} Antes de enviar el generador a terreno se quiere saber si le toca mantención y qué límites de uso tiene. ¿Qué documentos se consultan?", "La hoja de vida para el historial y el manual del fabricante para los límites", "Solo el acta de entrega", "Solo la lista de equipos del proyecto", "El historial está en la hoja de vida y los límites en el manual; el acta y la lista no los contienen."),
    ],
    ctx=("abc", "Un compañero te propone cambiar la fecha del certificado de calibración de un instrumento «para que no lo detengan en la revisión». ¿Qué respondes?", "Que no se altera un certificado y que lo hablarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, si solo cambia una fecha", "Que sí, y se recalibra cuando haya tiempo", "Alterar un documento oculta un problema real; ante la duda se consulta a un adulto responsable."),
    sc=[
        ("En Geología: ¿qué es la calibración?", "Comparar un instrumento con un patrón y ajustarlo para que mida bien", "La calibración mantiene la confiabilidad de las mediciones."),
        ("En el trabajo de terreno: ¿qué documento muestra el historial de un equipo?", "La hoja de vida del equipo", "La hoja de vida reúne mantenciones y calibraciones."),
        ("¿Qué se debe hacer con un certificado de calibración vencido?", "No usar el instrumento hasta recalibrarlo y registrarlo", "Un instrumento descalibrado puede entregar datos erróneos."),
    ],
    op=("Ficha de ejemplo: «Proyecto Pampa Demo». Una bomba de agua lleva 90 horas de uso y su manual pide mantención cada 120 horas. Un instrumento fue calibrado hace 70 días y su certificado vale 90 días. El equipo se usará 5 horas al día. Escribe (a) cuántas horas le faltan a la bomba para su mantención, (b) en cuántos días llega a ese número de horas, (c) cuántos días de vigencia le quedan al instrumento, (d) qué documento consultas para ver el historial de la bomba.",
        "(a) 120 − 90 = 30 horas. (b) 30 ÷ 5 = 6 días. (c) 90 − 70 = 20 días. (d) La hoja de vida de la bomba. Las mantenciones y calibraciones las hace personal autorizado.",
        ["calcula bien las horas que faltan", "calcula bien los días", "calcula bien la vigencia", "nombra la hoja de vida"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "confundir hoja de vida con acta de entrega", "olvidar la unidad"],
        "Pregunta: «¿qué número es el total y cuál el ya usado?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa la hoja de vida de un instrumento con la fecha de calibración, la vigencia y los días restantes.",
    extend="Explica con un ejemplo por qué la calibración vencida puede perjudicar los datos de un proyecto.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (plan de traslado de ejemplo, inventado). «Proyecto Quebrada Alta Demo». Un vehículo de ejemplo tiene una carga útil de 300 kilos. Bultos por trasladar al campamento: un compresor de 110 kilos, un generador de 90 kilos, una bomba de 35 kilos, "
     "dos cajas de instrumentos de 15 kilos cada una y dos bidones de combustible, de 25 kilos cada uno. El plan inicial lleva todo en un solo viaje, con los bidones sin amarras junto a los pasajeros. "
     "La ruta tiene 48 kilómetros y se avanza a 24 kilómetros por hora (datos de ejemplo).")
build(
    O2, 3, F,
    use="Aprenderé a analizar en papel un plan de traslado de equipos: sumar pesos, detectar una sobrecarga, repartir en viajes, revisar el transporte de combustible y verificar con el acta de entrega.",
    prior=["Sé qué es carga útil.", "Sé qué documentos acompañan a un equipo.", "Sé sumar, restar y dividir números enteros."],
    explain=[
        "Un plan de traslado dice qué se lleva, en qué vehículo, por qué ruta y quién es responsable. Para analizarlo se suman los pesos de los bultos y se compara el total con la carga útil del vehículo. Si el total es mayor, hay una sobrecarga: llevar más peso del permitido. La sobrecarga se corrige repartiendo en más viajes o usando otro vehículo, nunca anotando un peso falso.",
        "Los combustibles viajan en envases adecuados, rotulados, sujetos y separados de las personas, según la norma vigente. La hoja de ruta indica el camino, los puntos de control y los horarios previstos; si hay un atraso, se informa y se actualiza. Después del traslado se verifica comparando lo despachado en el acta de entrega con lo recibido en el campamento: si no coincide, se busca la diferencia antes de cerrar el registro.",
        f"El plan real lo prepara y aprueba personal autorizado. Aquí practicas el razonamiento con números de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("plan de traslado", "documento que dice qué se lleva, en qué vehículo, por qué ruta y quién responde"), ("sobrecarga", "llevar más peso que la carga útil del vehículo"), ("hoja de ruta", "documento con el camino, los puntos de control y los horarios previstos"), ("amarra", "correa o cuerda que sujeta una carga para que no se mueva"), ("verificar", "comprobar con otro dato que lo planificado se cumplió")],
    worked=[
        ("Detectar sobrecarga", "Un vehículo de ejemplo tiene carga útil de 400 kilos y debe llevar bultos de 150, 130 y 140 kilos. ¿Hay sobrecarga?", ["Se suman: 150 + 130 + 140 = 420 kilos.", "420 es mayor que 400: hay sobrecarga de 20 kilos."], "Sí, hay sobrecarga de 20 kilos"),
        ("Dos viajes", "Los mismos bultos se reparten en dos viajes: el primero con 150 y 130 kilos y el segundo con 140 kilos. ¿Se cumple la carga útil?", ["Primer viaje: 150 + 130 = 280, menor que 400.", "Segundo viaje: 140, menor que 400."], "Sí, ambos viajes cumplen"),
    ],
    mistakes=[("Corregir una sobrecarga anotando un peso menor en el plan.", "El registro falso no cambia el peso real y pone en riesgo a las personas y al vehículo.", "Se reparte la carga en más viajes o se usa otro vehículo, y el peso real se anota."),
              ("Creer que un atraso en la hoja de ruta se arregla viajando más rápido.", "Apurarse en un camino difícil aumenta el riesgo de accidente.", "Se informa el atraso al jefe, que decide, y se actualiza la hoja de ruta.")],
    T=[
        ("abc", "En Geología: ¿qué es una sobrecarga de un vehículo?", "Llevar más peso que su carga útil", "Llevar menos peso que su carga útil", "Viajar con el estanque lleno de combustible", "La sobrecarga es superar la carga útil; llevar menos o cargar combustible no lo es."),
        ("abc", "En Geología: ¿qué es un plan de traslado?", "Un documento que dice qué se lleva, en qué vehículo, por qué ruta y quién responde", "Un certificado de calibración del vehículo", "Un registro de las horas de uso de un instrumento", "El plan organiza el traslado; los certificados y registros de horas son otros documentos."),
        ("abc", "En Geología: ¿para qué sirve una hoja de ruta?", "Para indicar el camino, los puntos de control y los horarios previstos del viaje", "Para anotar los resultados de un análisis de muestras", "Para fijar el precio de cada equipo", "La hoja de ruta planifica el viaje; los resultados y los precios son otros asuntos."),
        ("=", "{F} ¿Cuántos kilos pesan en total los bultos del plan inicial?", "110+90+35+15+15+25+25", "Se suman los pesos de todos los bultos de la ficha.", " kilos"),
        ("=", "{F} ¿Cuántos kilos de sobrecarga tiene el plan inicial?", "(110+90+35+15+15+25+25)-300", "Se resta la carga útil al peso total de los bultos.", " kilos"),
        ("abc", "{F} ¿Qué corrección corresponde a la sobrecarga?", "Repartir los bultos en dos viajes, sin superar los 300 kilos en cada uno", "Viajar más despacio con todo en un solo viaje", "Anotar en el plan un peso menor para los bidones", "La sobrecarga se corrige repartiendo la carga; la lentitud o un registro falso no cambian el peso real."),
        ("=", "{F} Si el primer viaje lleva el compresor, el generador y la bomba, ¿cuántos kilos le sobran respecto de la carga útil?", "300-(110+90+35)", "Se resta el peso de los tres bultos a la carga útil.", " kilos"),
        ("=", "{F} Con ese primer viaje, ¿cuántos kilos lleva el segundo viaje con los demás bultos?", "15+15+25+25", "Se suman los pesos de las cajas y de los bidones.", " kilos"),
        ("abc", "{F} ¿Qué observación corresponde al plan que lleva los bidones sin amarras junto a los pasajeros?", "Debe corregirse: el combustible va en envases adecuados, sujeto y separado de las personas, según la norma vigente", "Está bien si se viaja despacio", "Está bien porque los bidones son pequeños", "El combustible exige envases adecuados, sujeción y separación, aunque se viaje despacio."),
        ("abc", "{F} Un compañero propone sacar un bidón de la lista para que no figure sobrecarga, pero cargarlo igual. ¿Qué corresponde responder?", "Que es falsear el registro: se informa la sobrecarga y se hace otro viaje", "Que está bien, porque el vehículo aguanta", "Que está bien si el bidón está lleno solo a medias", "Sacar un bulto de la lista no cambia el peso real y oculta el riesgo."),
        ("=", "{F} ¿Cuántas horas de conducción hay en total si se hacen dos viajes de ida y vuelta por la ruta de la ficha?", "(48//24)*2*2", "Se calculan las horas de ida, se duplican por la vuelta y se multiplican por dos viajes.", " horas"),
        ("abc", "{F} El primer viaje se atrasa una hora por el camino resbaladizo. ¿Qué conviene hacer?", "Informar al jefe del campamento y actualizar la hoja de ruta", "Acelerar para compensar el atraso", "No informar y esperar que nadie lo note", "Un atraso se informa y se decide con el responsable; apurarse en un camino resbaladizo aumenta el riesgo."),
        ("abc", "{F} Después del traslado se quiere comprobar que todo llegó. ¿Qué comparación sirve?", "Lo despachado según el acta de entrega contra lo recibido en el campamento", "El color de los bultos en el plan contra el color en el campamento", "La cantidad de combustible del vehículo contra el peso del compresor", "La verificación compara lo despachado con lo recibido; los otros datos no prueban que llegó todo."),
    ],
    ctx=("abc", "Un conductor de ejemplo te dice que cargará de más la camioneta de un familiar «porque total son pocos kilos» y te pide que lo anotes bien en la planilla. ¿Qué respondes?", "Que no se anota un peso falso y que avisarás a un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, si son pocos kilos", "Que sí, pero que lo repartan después", "Un registro falso oculta un riesgo real; ante la duda se consulta a un adulto responsable."),
    sc=[
        ("En Geología: ¿qué es la carga útil?", "El peso máximo que un vehículo puede llevar", "La carga útil es el límite que no se debe superar."),
        ("En el traslado de equipos de terreno: ¿qué se hace ante una sobrecarga?", "Se reparte la carga en más viajes o se usa otro vehículo", "La sobrecarga se corrige repartiendo el peso, no ocultándolo."),
        ("¿Cómo se verifica que un traslado se cumplió?", "Comparando lo despachado en el acta con lo recibido en el campamento", "La comparación detecta diferencias entre lo enviado y lo recibido."),
    ],
    op=("Ficha de ejemplo: «Proyecto Cordillera Demo». Un vehículo de ejemplo tiene carga útil de 260 kilos. Bultos: una bomba de 80 kilos, un generador de 95 kilos, una caja de instrumentos de 20 kilos y tres bidones de combustible de 25 kilos cada uno. Escribe (a) el peso total, (b) si hay sobrecarga y de cuántos kilos, (c) cómo repartirías los bultos en dos viajes sin superar la carga útil, (d) qué documento usarías para comprobar después que todo llegó.",
        "(a) 80 + 95 + 20 + 75 = 270 kilos. (b) Sí: 270 − 260 = 10 kilos de sobrecarga. (c) Por ejemplo, primer viaje con la bomba, la caja y los tres bidones separados de las personas (175 kilos), y segundo viaje con el generador (95 kilos). (d) El acta de entrega, comparando lo despachado con lo recibido. El traslado real lo hace personal autorizado.",
        ["suma bien el peso", "detecta la sobrecarga y su magnitud", "propone un reparto que cumple la carga útil", "nombra el acta de entrega"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal", "anotar un peso falso", "repartir de modo que un viaje supere la carga útil"],
        "Pregunta: «¿qué viaje queda con más kilos y cuánto?». Si no responde, pídele que sume cada viaje por separado."),
    reinforce="Inventa un plan con cuatro bultos y un vehículo de 200 kilos; calcula si hay sobrecarga y propón dos viajes.",
    extend="Explica por qué el combustible no debe viajar junto a los pasajeros, aun en un viaje corto.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). «Proyecto Valle Demo», cinco días de trabajo. Datos de ejemplo (los reales los indica el manual del fabricante): un generador portátil funciona 6 horas al día y consume 3 litros por hora; "
     "los bidones de combustible son de 20 litros; el generador lleva 170 horas de uso y su manual pide mantención cada 200 horas. Un instrumento se usa 6 horas al día con baterías de 8 horas de autonomía; el proyecto dispone de 3 baterías y no hay recarga en terreno.")
build(
    O2, 4, F,
    use="Aprenderé a calcular en papel el combustible, las baterías y las horas de uso de los equipos de un proyecto, comparando con los datos del manual del fabricante y con la mantención pendiente.",
    prior=["Sé qué documentos acompañan a un equipo.", "Sé multiplicar y dividir números enteros.", "Sé redondear hacia arriba cuando no se puede usar una fracción."],
    explain=[
        "El consumo por hora es la cantidad de combustible que usa un equipo en una hora de funcionamiento. Para saber cuánto se necesita en un proyecto se multiplican horas diarias, días y consumo por hora; luego se divide entre la capacidad de cada bidón y, si la división no es exacta, se redondea hacia arriba. La autonomía de una batería es el tiempo que funciona un instrumento con una carga completa; las horas de uso del proyecto se comparan con la autonomía total de las baterías disponibles.",
        "Las horas de uso también se suman a las que ya tiene el equipo, para saber si alcanzará el límite de mantención que indica el manual. Si en el proyecto el equipo llega a ese límite, se programa la mantención antes de seguir usándolo. Si el manual del fabricante entrega un dato distinto del supuesto de la ficha, manda el del manual y se recalcula. Un cálculo útil dice las unidades y los supuestos, y se actualiza si un día se usa más de lo previsto.",
        f"Estos cálculos los revisan el encargado de bodega y el técnico de mantención. Aquí aprendes el razonamiento, no el uso de los equipos. {EMER} {AVISO}",
    ],
    vocab=[("consumo por hora", "cantidad de combustible que usa un equipo en una hora de funcionamiento"), ("autonomía", "tiempo que funciona un instrumento con una carga completa de batería"), ("capacidad nominal", "valor máximo que indica el fabricante para un equipo o un envase"), ("horas de uso", "tiempo acumulado de funcionamiento de un equipo"), ("recalcular", "volver a calcular cuando cambia un dato")],
    worked=[
        ("Combustible de un proyecto", "Una bomba de ejemplo funciona 4 horas al día durante 3 días y consume 2 litros por hora. Los bidones son de 12 litros. ¿Cuántos bidones hacen falta?", ["Litros: 4 × 3 × 2 = 24.", "24 dividido por 12 da 2 bidones exactos."], "2 bidones"),
        ("Baterías", "Un instrumento de ejemplo se usa 10 horas en total y cada batería dura 4 horas. ¿Cuántas baterías se necesitan sin recarga?", ["10 dividido por 4 es 2,5.", "No existe media batería: se sube a 3."], "3 baterías"),
    ],
    mistakes=[("Redondear 4,5 bidones a 4 para ahorrar un bidón.", "Con 4 bidones falta combustible y el equipo se detiene antes de terminar.", "Se redondea hacia arriba y se agrega la reserva que fije el proyecto."),
              ("Usar el consumo de la ficha aunque el manual del fabricante indique otro.", "El manual manda: el supuesto de una ficha puede estar equivocado.", "Se usa el dato del manual y se recalcula.")],
    T=[
        ("abc", "En Geología: ¿qué es la autonomía de una batería?", "El tiempo que funciona un instrumento con una carga completa", "El peso de la batería en el estuche", "El tiempo que demora en cargarse al máximo", "La autonomía mide cuánto funciona el instrumento por carga, no su peso ni la duración de la carga."),
        ("abc", "En Geología: ¿qué es el consumo por hora de un generador?", "La cantidad de combustible que usa en una hora de funcionamiento", "El total de combustible que cabe en su estanque", "La cantidad de ruido que produce en una hora", "El consumo por hora es el gasto de combustible, no la capacidad del estanque ni el ruido."),
        ("abc", "En Geología: ¿qué es la capacidad nominal de un equipo según su manual?", "El valor máximo que indica el fabricante para su uso", "El valor promedio que midió el último operador", "El valor mínimo con que el equipo funciona", "La capacidad nominal es un máximo fijado por el fabricante."),
        ("=", "{F} ¿Cuántos litros de combustible consume el generador durante los cinco días?", "6*3*5", "Se multiplican horas diarias, consumo por hora y días.", " litros"),
        ("=", "{F} ¿Cuántos bidones de 20 litros se necesitan, redondeando hacia arriba?", "(6*3*5+19)//20", "Se suman 19 antes de dividir entre 20 para subir al siguiente entero.", " bidones"),
        ("=", "{F} ¿Cuántas horas se usa el instrumento durante los cinco días?", "6*5", "Se multiplican las horas diarias por los días.", " horas"),
        ("=", "{F} ¿Cuántas horas de trabajo cubren en total las tres baterías disponibles?", "3*8", "Se multiplica la autonomía de cada batería por la cantidad de baterías.", " horas"),
        ("=", "{F} ¿Cuántas baterías hacen falta para cubrir todas las horas de uso, redondeando hacia arriba?", "(6*5+7)//8", "Se suman 7 antes de dividir entre 8 para subir al siguiente entero.", " baterías"),
        ("abc", "{F} ¿Qué ocurre con la mantención del generador al terminar los cinco días?", "Llega a las 200 horas que pide el manual, así que debe programarse la mantención antes de seguir usándolo", "Queda muy lejos del límite, por lo que no hay que hacer nada", "Se salta una mantención porque 200 es solo una sugerencia", "170 horas más 30 de uso suman 200, justo el límite del manual."),
        ("abc", "{F} Un compañero calcula 4,5 bidones, encarga 4 y dice que «alcanza». ¿Cuál es la consecuencia?", "Faltarían 10 litros de combustible, porque 4 bidones traen 80 litros y se necesitan 90", "Sobrarían 10 litros, que se guardan de reserva", "No pasa nada, porque el generador consume menos al final", "4 bidones de 20 litros son 80 litros, y el consumo calculado es 90."),
        ("abc", "{F} El manual indica un consumo de 4 litros por hora, mayor que el de la ficha. ¿Qué valor se usa?", "El del manual del fabricante, y se recalcula todo", "El de la ficha, porque ya está calculado", "El menor de los dos, para ahorrar combustible", "El manual del fabricante manda; el supuesto de la ficha se reemplaza."),
        ("=", "{F} Con el consumo de 4 litros por hora del manual, ¿cuántos litros más que con el supuesto de la ficha se necesitan en los cinco días?", "6*4*5-6*3*5", "Se calcula el consumo con ambos valores y se restan.", " litros"),
        ("abc", "{F} Un día de lluvia se usa el generador 9 horas en vez de 6. ¿Qué corresponde?", "Anotar las horas reales y recalcular el combustible y la mantención restantes", "No anotar nada, porque fue un solo día", "Anotar 6 horas para que coincida con lo planificado", "Los datos reales se registran y se recalcula; anotar lo previsto falsea el historial."),
    ],
    ctx=("abc", "Un conocido te pide que le calcules cuánto combustible dejar al generador de una obra real «con los números del cuaderno». ¿Qué respondes?", "Que los números del cuaderno son de ejemplo y que el cálculo real lo hace personal autorizado con el manual del fabricante; lo consultarás con un adulto responsable", "Que sí, porque el método está bien", "Que sí, si agregas un poco más por si acaso", "Los valores son de ejemplo; el consumo real lo da el manual del equipo."),
    sc=[
        ("En Geología: ¿qué es el consumo por hora?", "La cantidad de combustible que usa un equipo en una hora de funcionamiento", "El consumo por hora permite calcular el combustible del proyecto."),
        ("En el cálculo de un proyecto de terreno: ¿qué dato manda si difiere del supuesto?", "El del manual del fabricante", "El manual es la fuente oficial del fabricante."),
        ("¿Qué se hace si un día se usa un equipo más horas de lo previsto?", "Se anotan las horas reales y se recalcula", "Los datos reales permiten decidir mejor."),
    ],
    op=("Ficha de ejemplo: «Proyecto Estero Demo», cuatro días. Una bomba funciona 5 horas al día y consume 2 litros por hora; los bidones son de 15 litros. Un instrumento se usa 7 horas al día y cada batería dura 6 horas, con 4 baterías disponibles y sin recarga. Escribe (a) los litros totales, (b) los bidones necesarios, (c) las horas de uso del instrumento y si las baterías alcanzan, (d) qué haces si el manual indica un consumo distinto.",
        "(a) 5 × 2 × 4 = 40 litros. (b) 40 ÷ 15 = 2,67, se sube a 3 bidones. (c) 7 × 4 = 28 horas; 4 baterías × 6 horas = 24 horas, así que no alcanzan: faltan 4 horas y se necesitan 5 baterías. (d) Se usa el dato del manual del fabricante y se recalcula.",
        ["calcula bien los litros", "redondea hacia arriba los bidones", "compara horas de uso y autonomía", "indica que manda el manual"],
        ["hoja con las cuatro respuestas"],
        ["redondear hacia abajo", "olvidar que no hay recarga", "usar el supuesto en vez del manual"],
        "Pregunta: «¿cuántas horas cubren las baterías y cuántas necesitas?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el combustible de un generador inventado de 4 horas al día, 2 litros por hora y 5 días, con bidones de 10 litros.",
    extend="Explica con un ejemplo por qué conviene recalcular cuando un equipo se usa más de lo previsto.",
)

# ============================================================ OAE-02, clase 5
F = ("Ficha 5 (comparación de ejemplo, inventada). El «Proyecto Cuenca Demo» exige, para el receptor de posicionamiento de ejemplo, un error máximo de 5 metros y una autonomía de al menos 12 horas, para un proyecto de 90 días. "
     "Alternativa 1: error de 3 metros, autonomía de 10 horas por batería, masa de 400 gramos; una batería adicional suma 10 horas de autonomía y 150 gramos. "
     "Alternativa 2: error de 8 metros, autonomía de 14 horas, masa de 650 gramos. El certificado de calibración de ejemplo de la alternativa elegida vale 60 días.")
build(
    O2, 5, F,
    use="Aprenderé a comparar alternativas de equipos con los requisitos de un proyecto, a decidir con datos y a verificar la calidad al recibirlos con una inspección de recepción y el certificado de calibración.",
    prior=["Sé qué es una calibración y su vigencia.", "Sé qué es el acta de entrega.", "Sé sumar y restar números enteros."],
    explain=[
        "Comparar alternativas significa poner los datos de cada opción frente a los requisitos del proyecto. Un requisito es una condición mínima que el equipo debe cumplir; por ejemplo, un error máximo permitido, que es el mayor desvío aceptado entre lo que mide el instrumento y el valor real. Primero se comprueba qué alternativas cumplen todos los requisitos, con sus accesorios si hacen falta; después se usan criterios secundarios, como la masa o el costo. Una alternativa que no cumple un requisito no se elige aunque sea liviana o barata.",
        "Verificar la calidad es comprobar que lo recibido sirve. En la inspección de recepción se revisa que el equipo esté completo, sin daños y con sus documentos: manual, certificado de calibración y hoja de vida. Las faltas se anotan en el acta, se informan y el equipo no se usa hasta resolverlas. Si el certificado vence antes del fin del proyecto, se programa una nueva calibración.",
        f"Las compras y la recepción real las hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("requisito", "condición mínima que un equipo debe cumplir para servir al proyecto"), ("error máximo", "mayor desvío permitido entre lo que mide un instrumento y el valor real"), ("criterio secundario", "criterio que se usa para decidir entre alternativas que ya cumplen los requisitos"), ("inspección de recepción", "revisión al recibir un equipo: que esté completo, sin daños y con sus documentos"), ("alternativa", "una de las opciones entre las que se elige")],
    worked=[
        ("Cumplir un requisito", "Un proyecto de ejemplo exige una autonomía de al menos 8 horas. Una opción tiene 6 horas y otra tiene 9. ¿Cuál cumple?", ["La opción de 6 horas es menor que 8.", "La opción de 9 horas supera las 8."], "La opción de 9 horas"),
        ("Sumar un accesorio", "La opción de 6 horas permite agregar una batería de 3 horas. ¿Cumple ahora el requisito de 8 horas?", ["Se suman 6 y 3, que dan 9 horas.", "9 es mayor que 8, así que cumple."], "Sí, con 9 horas"),
    ],
    mistakes=[("Elegir la alternativa más liviana antes de comprobar los requisitos.", "La masa es un criterio secundario: si no cumple el requisito, el equipo no sirve.", "Se comprueban los requisitos y luego se desempata con los criterios secundarios."),
              ("Dar por buena una recepción sin mirar manual ni certificado.", "Un equipo sin documentos no se puede verificar ni usar con seguridad.", "Se revisa lo recibido, se anotan las faltas en el acta y se informa antes de usarlo.")],
    T=[
        ("abc", "En Geología: ¿qué es un requisito del proyecto para un equipo?", "Una condición mínima que el equipo debe cumplir para servir al trabajo", "La preferencia de color que tiene el jefe", "El peso del vehículo que lo traslada", "El requisito es una condición del proyecto; los gustos y el vehículo son otra cosa."),
        ("abc", "En Geología: ¿qué es el error máximo de un instrumento?", "El mayor desvío permitido entre lo que mide y el valor real", "El número de veces que puede usarse al día", "La cantidad de baterías que admite", "El error máximo limita cuánto puede equivocarse la medición."),
        ("abc", "En Geología: ¿qué es la inspección de recepción de un equipo?", "Revisar al recibirlo que esté completo, sin daños y con sus documentos", "Probarlo en terreno antes de firmar el acta", "Comprarlo al proveedor más cercano", "La inspección de recepción es una revisión al llegar; no es una prueba en terreno ni una compra."),
        ("abc", "{F} ¿Qué alternativa cumple por sí sola el requisito de error máximo de 5 metros?", "La alternativa 1, que tiene un error de 3 metros", "La alternativa 2, que tiene un error de 8 metros", "Ninguna, porque 5 es menor que ambos errores", "3 metros no supera el máximo de 5; 8 metros sí lo supera."),
        ("abc", "{F} ¿Qué alternativa cumple por sí sola el requisito de autonomía de 12 horas?", "La alternativa 2, que tiene 14 horas", "La alternativa 1, que tiene 10 horas", "Ambas, porque las dos pasan de 10 horas", "14 supera las 12 horas exigidas; 10 horas no las alcanza."),
        ("=", "{F} ¿Cuántas horas de autonomía tiene la alternativa 1 con una batería adicional?", "10+10", "Se suma la autonomía de la batería adicional a la del equipo.", " horas"),
        ("abc", "{F} ¿Qué decisión se justifica con los datos de la ficha?", "La alternativa 1 con batería adicional, porque cumple ambos requisitos", "La alternativa 2, porque tiene la mayor autonomía", "La alternativa 1 sin accesorios, porque es la más liviana", "Solo la alternativa 1 con batería cumple error y autonomía a la vez."),
        ("=", "{F} ¿Cuántos gramos pesa la alternativa 1 con la batería adicional?", "400+150", "Se suma la masa de la batería a la del equipo.", " gramos"),
        ("abc", "{F} ¿Por qué no basta elegir la alternativa más liviana?", "Porque primero deben cumplirse los requisitos del proyecto y la masa es un criterio secundario", "Porque las alternativas livianas nunca funcionan", "Porque la masa no se puede medir en gramos", "La masa sirve para desempatar entre opciones que ya cumplen los requisitos."),
        ("abc", "{F} Al recibir el equipo elegido falta el cable de carga y no viene el manual. ¿Qué corresponde?", "Anotar las faltas en el acta, informar al encargado y no usarlo hasta completar lo que falta", "Firmar el acta sin anotar nada y buscar el manual después", "Usarlo sin cable ni manual, porque funciona", "Las faltas se registran y se informan; usar sin manual impide seguir las indicaciones del fabricante."),
        ("abc", "{F} El certificado de la alternativa elegida vale 60 días y el proyecto dura 90. ¿Qué conclusión corresponde?", "No cubre todo el proyecto, y debe programarse una nueva calibración antes de que venza", "Cubre todo el proyecto, porque 60 días es mucho tiempo", "No importa, porque la calibración solo se pide al comprar", "60 días son menos que 90; la calibración se renueva antes del vencimiento."),
        ("=", "{F} ¿Cuántos días del proyecto quedarían sin certificado vigente si no se recalibra?", "90-60", "Se resta la vigencia del certificado a la duración del proyecto.", " días"),
        ("abc", "{F} Un compañero dice: «las dos alternativas cumplen algo, así que da igual cuál se elija». ¿Qué respuesta es correcta?", "Es falso: se elige la que cumple todos los requisitos, aunque necesite un accesorio", "Es cierto, porque cumplir algo basta", "Es cierto, siempre que la elegida sea la más cara", "Cumplir parte de los requisitos no basta; se elige la opción que cumple todos."),
    ],
    ctx=("abc", "Un proveedor de ejemplo te ofrece un instrumento «sin certificado de calibración, pero que funciona perfecto». ¿Qué respondes?", "Que sin certificado no se puede comprobar que mida bien y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, porque el instrumento se ve nuevo", "Que sí, y se calibra al final del proyecto", "Sin certificado no hay evidencia de que el instrumento mida dentro del error permitido."),
    sc=[
        ("En Geología: ¿qué es un requisito del proyecto?", "Una condición mínima que el equipo debe cumplir", "El requisito fija lo mínimo que debe cumplir el equipo."),
        ("En la recepción de equipos de terreno: ¿qué se hace si falta un documento?", "Se anota la falta en el acta, se informa y no se usa el equipo", "Sin documentos no se puede verificar el equipo."),
        ("¿Qué criterio va primero al comparar alternativas?", "Los requisitos del proyecto", "Los criterios secundarios solo desempatan entre opciones que cumplen."),
    ],
    op=("Ficha de ejemplo: el «Proyecto Humedal Demo» exige un instrumento con error máximo de 4 metros y autonomía de al menos 16 horas. Alternativa A: error de 2 metros, autonomía de 10 horas, y una batería adicional suma 8 horas. Alternativa B: error de 6 metros, autonomía de 20 horas. Escribe (a) qué alternativa cumple el error máximo, (b) cuántas horas tiene la alternativa A con una batería adicional, (c) qué alternativa eliges y por qué, (d) dos cosas que revisarías en la recepción.",
        "(a) La alternativa A, porque 2 es menor que 4. (b) 10 + 8 = 18 horas. (c) La alternativa A con batería adicional, porque cumple error y autonomía; la B no cumple el error. (d) Que esté completo y sin daños, y que traiga manual y certificado de calibración vigente. La compra y recepción reales las hace personal autorizado.",
        ["identifica qué alternativa cumple el error", "calcula bien la autonomía", "decide con los requisitos y lo justifica", "nombra dos revisiones de recepción"],
        ["hoja con las cuatro respuestas"],
        ["elegir por la autonomía sola", "olvidar el accesorio", "no mencionar los documentos"],
        "Pregunta: «¿qué requisito incumple la alternativa B?». Si no responde, pídele que compare 6 con 4."),
    reinforce="Inventa dos alternativas con error y autonomía distintos, define un requisito para cada dato y decide cuál elegirías.",
    extend="Explica con un ejemplo por qué la inspección de recepción es una forma de verificar la calidad.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (plano de ejemplo, inventado). «Proyecto Cerro Demo». El plano topográfico de ejemplo tiene escala 1:5.000 (1 centímetro del plano equivale a 50 metros reales) y una cuadrícula de coordenadas Este y Norte cada 100 metros. "
     "El sitio de faena S-1 está en E 1.200 y N 3.400. El plano marca una zona de exclusión (labores antiguas abandonadas y un talud inestable) cuyo borde oeste está en E 1.500. "
     "La ruta hacia S-1 mide 14 centímetros en el plano y se camina a 70 metros por minuto. Peligros anotados: leer mal una coordenada, labores antiguas sin señalizar, niebla, pendientes con piedras sueltas y falla del receptor de posicionamiento.")
build(
    O3, 1, F,
    use="Aprenderé qué es un levantamiento topográfico, qué es una faena y una zona de exclusión, por qué leer mal un plano es un riesgo y qué controles se usan para ubicarse con seguridad en papel.",
    prior=["Sé leer una ficha escrita y una cuadrícula.", "Sé multiplicar y dividir números enteros.", "Sé distinguir peligro y riesgo."],
    explain=[
        "Un levantamiento topográfico es el conjunto de mediciones del terreno que se dibujan en un plano para mostrar su forma y la ubicación de puntos importantes. La faena es el lugar y las labores donde se realiza el trabajo. Un plano usa una escala: en la escala 1:5.000, 1 centímetro del plano equivale a 5.000 centímetros reales, es decir, 50 metros. Los puntos se ubican con coordenadas, un par de números: la coordenada Este (hacia la derecha) y la coordenada Norte (hacia arriba).",
        "Leer mal un plano es peligroso: un número mal copiado puede llevar a una persona a un sitio equivocado, por ejemplo cerca de una zona de exclusión, un área marcada donde no se debe entrar por el peligro que tiene, como labores antiguas abandonadas o un talud inestable. Los controles de la jerarquía son, por ejemplo, cercar físicamente la zona con una barrera (ingeniería), dibujarla en el plano y exigir que todos lo revisen (administrativo) y revisar las coordenadas entre dos personas.",
        f"Los levantamientos y las rutas reales los define personal autorizado según la norma vigente de la autoridad minera. {EMER} {AVISO}",
    ],
    vocab=[("levantamiento topográfico", "mediciones del terreno que se dibujan en un plano"), ("faena", "lugar y labores donde se realiza el trabajo"), ("escala", "relación entre una medida del plano y la medida real"), ("coordenadas", "par de números, Este y Norte, que ubican un punto"), ("zona de exclusión", "área marcada donde no se debe entrar por su peligro"), ("labor abandonada", "excavación antigua que ya no se usa y puede ser peligrosa"), ("talud", "ladera o borde inclinado de un terreno o de una excavación")],
    worked=[
        ("Peligro y riesgo", "Un plano de ejemplo no marca una labor antigua que sí existe en el terreno. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la labor antigua sin señalizar.", "El riesgo es que una persona se acerque sin saberlo y sufra una caída o un derrumbe."], "Peligro: labor antigua sin señalizar; riesgo: que una persona se acerque sin saberlo y se lesione"),
        ("Clasificar un control", "Se dibuja en el plano una zona de exclusión alrededor de la labor y se hace firmar a todo el equipo que la conoce. ¿A qué nivel de la jerarquía corresponde?", ["Dibujar e informar no cambia el lugar.", "Es una regla e información para las personas: nivel administrativo."], "Control administrativo"),
    ],
    mistakes=[("Creer que si el plano no marca un peligro, entonces no existe.", "Un plano puede estar incompleto o desactualizado.", "Se confirma con personal autorizado y se respetan las zonas de exclusión vigentes."),
              ("Creer que leer este cuaderno habilita para entrar a una faena o a una zona de exclusión.", "Entrar a terrenos mineros exige autorización, instructor y norma vigente.", "Aprende aquí el concepto y deja el trabajo en terreno a personal autorizado.")],
    T=[
        ("abc", "En Geología: ¿qué es un levantamiento topográfico?", "El conjunto de mediciones del terreno que se dibujan en un plano", "Una lista de las muestras tomadas en un campamento", "Un informe con la concentración de cada mineral", "El levantamiento mide y dibuja el terreno; las listas de muestras y los análisis son otra cosa."),
        ("abc", "En Geología: ¿qué es una faena?", "El lugar y las labores donde se realiza el trabajo", "El turno de descanso del personal", "El dibujo de un plano con su escala", "La faena es el lugar de trabajo; el turno y el plano son otra cosa."),
        ("abc", "En Geología: ¿qué es una zona de exclusión?", "Un área marcada donde no se debe entrar por el peligro que tiene", "Un área reservada para el comedor del campamento", "Un sector del plano sin ninguna medición", "La zona de exclusión se marca por su peligro; no es un sector de servicio ni un vacío del plano."),
        ("=", "{F} Un tramo mide 6 centímetros en el plano. ¿Cuántos metros reales son?", "6*50", "Se multiplican los centímetros del plano por los 50 metros de cada centímetro.", " metros"),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la zona de exclusión del plano?", "Que una persona entre por error y caiga o sea alcanzada por material que se desprenda", "Que la cuadrícula del plano quede incompleta", "Que la escala sea 1:5.000", "El riesgo es la posibilidad de daño a una persona; la cuadrícula y la escala son datos del plano."),
        ("=", "{F} ¿Cuántos metros al Este de S-1 está el borde de la zona de exclusión?", "1500-1200", "Se resta la coordenada Este de S-1 a la del borde.", " metros"),
        ("abc", "{F} Dibujar la zona de exclusión en el plano y exigir que todo el equipo lo revise es un control de tipo:", "Administrativo, porque informa y ordena la conducta", "De ingeniería, porque cambia físicamente el terreno", "De EPP, porque protege a cada persona", "Dibujar y revisar informa, pero no cambia el terreno ni equipa a nadie."),
        ("abc", "{F} Cercar físicamente la zona con una barrera y una señal, hecho por personal autorizado, es un control de tipo:", "De ingeniería, porque cambia el lugar y no depende de que alguien lo recuerde", "Administrativo, porque es una regla escrita", "De EPP, porque protege a la persona", "La barrera modifica el lugar; las reglas escritas y el EPP son otros niveles."),
        ("abc", "{F} Una estudiante dice: «con este plano en el cuaderno ya puedo ir sola a la faena». ¿Qué respuesta es correcta?", "Es falso: entrar a una faena exige autorización, instructor y norma vigente", "Es cierto, si lleva el plano impreso", "Es cierto, si evita la zona de exclusión", "Un plano en papel no habilita para entrar a un terreno minero; evitar una zona tampoco."),
        ("abc", "Durante una visita de ejemplo, ves que una persona se acerca a un talud del que caen piedras. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Correr a tirar de la persona hacia atrás", "Gritar desde el borde y acercarte si no responde", "Acercarse a un talud que se desprende puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "En Geología: ¿por qué conviene que dos personas revisen las coordenadas anotadas antes de salir a terreno?", "Porque un número mal copiado puede llevar a ubicarse en un sitio equivocado, incluso peligroso", "Porque así se evita calcular la escala del plano", "Porque dos personas leen más rápido que una sola", "Una revisión doble detecta errores de copia que pueden poner a alguien en riesgo."),
        ("=", "{F} ¿Cuántos minutos se tarda en recorrer la ruta de 14 centímetros del plano?", "(14*50)//70", "Se pasa la ruta a metros y se divide entre los metros que se caminan por minuto.", " minutos"),
        ("abc", "{F} El jefe dice: «la zona de exclusión es muy grande, mejor recortarla en el plano para llegar más rápido a S-1». ¿Cuál es la mejor respuesta?", "No se recorta: se respeta la zona y se busca otra ruta aprobada por personal autorizado", "Se recorta, si se camina con cuidado", "Se recorta solo un poco, para no atrasar el trabajo", "La zona de exclusión existe por el peligro; reducirla en el plano no lo elimina."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por guiar a unos curiosos hasta una antigua faena abandonada «porque ya sabes leer planos». ¿Qué respondes?", "Que no, porque entrar a una faena abandonada es peligroso y exige personal autorizado, y que lo consultarás con un adulto responsable", "Que sí, si llevas el plano y una linterna", "Que sí, pero solo hasta la entrada", "Haber aprendido a leer un plano no habilita para guiar en un lugar peligroso."),
    sc=[
        ("En Geología: ¿qué es una zona de exclusión?", "Un área marcada donde no se debe entrar por su peligro", "La zona de exclusión protege a las personas de un peligro conocido."),
        ("En un plano topográfico: ¿qué indica la escala?", "La relación entre una medida del plano y la medida real", "Con la escala se pasan centímetros del plano a metros reales."),
        ("¿Para qué se usan las coordenadas?", "Para ubicar un punto con un par de números, Este y Norte", "Las coordenadas permiten ubicar un punto con precisión."),
    ],
    op=("Plano de ejemplo del «Proyecto Pampa Demo»: escala 1:2.000 (1 centímetro equivale a 20 metros), zona de exclusión alrededor de un talud con piedras sueltas, y un sitio de faena S-2 a 18 centímetros del campamento. Escribe (a) cuántos metros reales hay hasta S-2, (b) cuál es el peligro de la zona de exclusión y cuál el riesgo, (c) un control administrativo (que no sea dibujarla en el plano) y uno de ingeniería para esa zona, (d) qué haces si ves a alguien entrar a esa zona en una visita real.",
        "(a) 18 × 20 = 360 metros. (b) Peligro: el talud con piedras sueltas; riesgo: que una persona sea golpeada por piedras que se desprendan. (c) Administrativo: una regla escrita de no pasar de las señales y una charla breve al equipo; ingeniería: cercar con barrera y señal, hecho por personal autorizado. (d) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias. El trabajo real lo hace personal autorizado.",
        ["convierte bien la escala", "distingue peligro y riesgo", "propone un control administrativo y uno de ingeniería", "indica no acercarse y avisar"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar por la escala equivocada", "llamar riesgo a la fuente del daño", "responder que se acerca a ayudar"],
        "Pregunta: «¿cuántos metros vale cada centímetro del plano?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un tramo de 9 centímetros en un plano de escala 1:5.000 y calcula cuántos metros reales mide.",
    extend="Explica con un ejemplo por qué un plano desactualizado puede ser un peligro.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). Plano topográfico del «Sector Loma Demo», escala 1:2.000, con una leyenda (qué significa cada símbolo), un norte dibujado, una cuadrícula de coordenadas y curvas de nivel con equidistancia de 10 metros: "
     "las curvas tienen cotas 2.400, 2.410, 2.420 y 2.430. Puntos topográficos de ejemplo: el vértice V1, en E 1.000, N 2.000 y cota 2.400, y el vértice V2, en E 1.300, N 2.400 y cota 2.430. "
     "Las mediciones se anotan en la libreta de terreno (registro con fecha, responsable y valor medido). Roles: topógrafo, geólogo jefe y asistente de geología.")
build(
    O3, 2, F,
    use="Aprenderé los conceptos de cota, curvas de nivel, equidistancia, punto topográfico y escala, los documentos de un levantamiento y el rol de cada persona, para leer un plano en papel.",
    prior=["Sé qué es un levantamiento y una zona de exclusión.", "Sé leer coordenadas Este y Norte.", "Sé restar y multiplicar números enteros."],
    explain=[
        "En un plano topográfico la cota es la altura de un punto sobre un nivel de referencia. Las curvas de nivel son líneas que unen puntos con igual cota; la equidistancia es la diferencia de cota entre dos curvas consecutivas. Si las curvas aparecen muy juntas, el terreno es más empinado; si están separadas, es más suave. Un punto topográfico, como un vértice o un hito, es un punto con coordenadas y cota conocidas, que sirve de referencia.",
        "La leyenda explica los símbolos y colores del plano. La escala permite pasar medidas del plano a medidas reales: en 1:2.000, 1 centímetro del plano son 20 metros. Para hallar la distancia horizontal entre dos puntos se usa la diferencia de coordenadas: distancia al cuadrado igual a la diferencia Este al cuadrado más la diferencia Norte al cuadrado, y la distancia es la raíz cuadrada de esa suma, como en el teorema de Pitágoras. La libreta de terreno guarda las mediciones tal cual se hicieron: un error se tacha con una línea y se anota el valor correcto con fecha y firma, sin borrar.",
        f"El topógrafo hace el levantamiento; el geólogo jefe decide qué se necesita del terreno; el asistente de geología apoya con registros y lectura de datos. {EMER} {AVISO}",
    ],
    vocab=[("cota", "altura de un punto sobre un nivel de referencia"), ("curva de nivel", "línea que une puntos con la misma cota"), ("equidistancia", "diferencia de cota entre dos curvas de nivel consecutivas"), ("punto topográfico", "punto con coordenadas y cota conocidas, usado como referencia"), ("leyenda", "parte del plano que explica sus símbolos y colores"), ("libreta de terreno", "registro con fecha, responsable y valor de cada medición")],
    worked=[
        ("Desnivel", "Dos puntos de un plano de ejemplo tienen cotas 850 y 880. ¿Cuál es el desnivel entre ellos?", ["El desnivel es la diferencia de cota.", "880 menos 850 son 30 metros."], "30 metros"),
        ("Distancia horizontal", "Dos puntos de ejemplo difieren en 6 metros al Este y 8 metros al Norte. ¿Qué distancia horizontal hay entre ellos?", ["Se calcula: 6 al cuadrado más 8 al cuadrado es 36 + 64 = 100.", "La raíz de 100 es 10."], "10 metros"),
    ],
    mistakes=[("Confundir cota con distancia en el plano.", "La cota es una altura; la distancia horizontal se calcula con las coordenadas Este y Norte.", "Se lee la cota para las alturas y las coordenadas para las posiciones."),
              ("Borrar un valor de la libreta de terreno y escribir encima.", "Un registro borrado pierde la trazabilidad y puede ocultar un error.", "Se tacha con una línea, se anota el valor correcto con fecha y firma.")],
    T=[
        ("abc", "En Geología: ¿qué es una cota en un plano topográfico?", "La altura de un punto sobre un nivel de referencia", "La distancia entre dos puntos en el plano", "La inclinación del terreno medida en porcentaje", "La cota es una altura; la distancia y la pendiente se calculan con otros datos."),
        ("abc", "En Geología: ¿qué son las curvas de nivel?", "Líneas que unen puntos del terreno con la misma cota", "Líneas que muestran el recorrido de los vehículos", "Líneas que separan terrenos de distintos dueños", "Las curvas de nivel representan el relieve uniendo puntos de igual altura."),
        ("abc", "En Geología: ¿qué es la equidistancia de un plano topográfico?", "La diferencia de cota entre dos curvas de nivel consecutivas", "La distancia en metros entre dos vértices del plano", "La escala del plano expresada en centímetros", "La equidistancia es una diferencia de altura, no de posición."),
        ("abc", "{F} ¿Qué documento registra las mediciones tal como se hicieron, con fecha y responsable?", "La libreta de terreno", "La leyenda del plano", "El norte dibujado en el plano", "La libreta guarda mediciones; la leyenda explica símbolos y el norte da orientación."),
        ("abc", "{F} ¿Qué parte del plano explica el significado de los símbolos y colores?", "La leyenda", "La equidistancia", "La libreta de terreno", "La leyenda es la clave de lectura del plano."),
        ("=", "{F} ¿Cuántos metros de desnivel hay entre los vértices V1 y V2?", "2430-2400", "Se resta la cota menor a la cota mayor.", " metros"),
        ("=", "{F} ¿Cuántos metros al Norte está V2 respecto de V1?", "2400-2000", "Se resta la coordenada Norte de V1 a la de V2.", " metros"),
        ("abc", "{F} V2 está 300 metros al Este y 400 al Norte de V1. ¿Qué distancia horizontal hay entre ellos?", "500 metros", "700 metros", "100 metros", "Con 300 y 400 la distancia es la raíz de 90.000 + 160.000, que es 500; 700 sumaría ambas diferencias sin calcular la hipotenusa."),
        ("=", "{F} ¿Cuántas curvas de nivel distintas hay entre las cotas 2.400 y 2.430, incluyendo ambas?", "(2430-2400)//10+1", "Se divide el desnivel entre la equidistancia y se suma 1 para incluir ambas.", " curvas"),
        ("abc", "{F} En una ladera las curvas de nivel aparecen muy juntas. ¿Qué indica eso?", "Que el terreno es más empinado en ese sector", "Que el terreno es plano", "Que la cota es menor que en el resto del plano", "Curvas juntas significan que la altura cambia rápido en poca distancia."),
        ("abc", "{F} Una asistente borra un valor de la libreta porque «se leyó mal» y escribe el correcto sin dejar rastro. ¿Qué corresponde?", "Tachar con una línea, anotar el valor correcto con fecha y firma, sin borrar", "Está bien si el valor nuevo es correcto", "Está bien si nadie lo vio", "Un registro no se borra: se tacha para que quede la trazabilidad del cambio."),
        ("abc", "{F} Un compañero dice: «V2 tiene mayor cota, así que está más al Norte». ¿Qué respuesta es correcta?", "Es falso: la cota es una altura y la posición Norte se lee en la coordenada Norte", "Es cierto, porque más alto siempre es más al Norte", "Es cierto, si la equidistancia es 10 metros", "Cota y coordenada Norte miden cosas distintas: altura y posición."),
        ("=", "{F} ¿Cuántos centímetros ocupa en el plano la distancia de 500 metros entre V1 y V2, a escala 1:2.000?", "(500*100)//2000", "Se pasan los metros a centímetros y se divide entre la escala.", " centímetros"),
    ],
    ctx=("abc", "Un compañero te dice que, para que la libreta de terreno quede «limpia», conviene copiarla de nuevo omitiendo los errores. ¿Qué respondes?", "Que no se omiten errores y que cualquier duda se consulta con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, si queda más ordenada", "Que sí, si se conserva solo la copia nueva", "Omitir errores borra la trazabilidad; los errores se tachan y se corrigen con firma."),
    sc=[
        ("En Geología: ¿qué es una cota?", "La altura de un punto sobre un nivel de referencia", "La cota indica qué tan alto está un punto."),
        ("En un plano topográfico: ¿qué indican las curvas de nivel muy juntas?", "Un terreno más empinado", "La altura cambia rápido cuando las curvas están juntas."),
        ("¿Cómo se corrige un error en la libreta de terreno?", "Se tacha con una línea y se anota el valor correcto con fecha y firma", "Así queda constancia del error y de su corrección."),
    ],
    op=("Plano de ejemplo del «Sector Altos Demo»: equidistancia de 5 metros; punto A en E 500, N 800 y cota 1.200; punto B en E 650, N 1.000 y cota 1.215; escala 1:5.000. Escribe (a) el desnivel entre A y B, (b) cuántos metros al Este y al Norte está B respecto de A, (c) la distancia horizontal entre A y B, (d) cuántas curvas de nivel hay entre ambas cotas, incluyendo ambas.",
        "(a) 1.215 − 1.200 = 15 metros. (b) 150 metros al Este y 200 al Norte. (c) 250 metros, porque 150 y 200 forman un triángulo de lados 3, 4 y 5 multiplicados por 50. (d) 15 ÷ 5 + 1 = 4 curvas.",
        ["calcula bien el desnivel", "calcula bien las diferencias de coordenadas", "obtiene la distancia horizontal", "cuenta las curvas incluyendo ambas"],
        ["hoja con las cuatro respuestas"],
        ["confundir cota con coordenada", "sumar las diferencias en vez de usar la distancia horizontal", "olvidar sumar 1 al contar curvas"],
        "Pregunta: «¿qué dato mide altura y cuáles miden posición?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos puntos con sus coordenadas y cotas, y calcula el desnivel y las diferencias Este y Norte.",
    extend="Explica con un ejemplo por qué la libreta de terreno no se borra.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Plano del «Sector Mesa Demo». Puntos topográficos: P1 en E 2.000, N 5.000, cota 1.800; P2 en E 2.300, N 5.400, cota 1.830; P3 en E 2.300, N 5.700, cota 1.860. "
     "El plano marca una zona de exclusión (labores antiguas) y la línea recta entre P1 y P2 cruza esa zona. Ruta alternativa: de P1 a Q, en E 2.300 y N 5.000, y de Q a P2, sin cruzar la zona. "
     "La libreta de terreno anota el sitio de faena S-3 en E 2.300 y N 5.070, pero el plano lo ubica en E 2.300 y N 5.700. Se camina a 70 metros por minuto.")
build(
    O3, 3, F,
    use="Aprenderé a analizar en papel un levantamiento: calcular distancias y pendientes entre puntos, comparar rutas, descartar rutas que cruzan una zona de exclusión y detectar errores de copia en una libreta de terreno.",
    prior=["Sé leer coordenadas Este y Norte y cotas.", "Sé calcular desnivel y distancia horizontal.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "La pendiente de un tramo mide su inclinación y se calcula como desnivel dividido por la distancia horizontal, multiplicado por 100 para expresarla en porcentaje. Por ejemplo, un desnivel de 20 metros en 200 metros de distancia horizontal da una pendiente de 10 por ciento. A mayor porcentaje, más empinado es el tramo. Comparar rutas significa calcular distancia, pendiente y tiempo de cada una, pero sin dejar de lado el criterio de seguridad: una ruta que cruza una zona de exclusión se descarta aunque sea más corta.",
        "Un error de transposición es anotar los dígitos de un número en otro orden, como 5.700 escrito 5.070. Es un error frecuente al copiar coordenadas, y puede ubicar un sitio a cientos de metros de su lugar real. Cuando la libreta y el plano no coinciden, no se elige uno al azar: se avisa al topógrafo, se revisa la medición original y se corrige con firma. Si el plano es antiguo, se usa el plano vigente.",
        f"Estos análisis los aprueba personal autorizado; aquí practicas el razonamiento. {EMER} {AVISO}",
    ],
    vocab=[("pendiente", "inclinación de un tramo: desnivel dividido por distancia horizontal, por 100"), ("ruta alternativa", "camino distinto que evita un peligro aunque sea más largo"), ("error de transposición", "error de copia que cambia el orden de los dígitos de un número"), ("plano vigente", "versión actual y aprobada de un plano"), ("discrepancia", "diferencia entre dos registros de un mismo dato")],
    worked=[
        ("Pendiente", "Un tramo de ejemplo sube 15 metros en 300 metros de distancia horizontal. ¿Cuál es su pendiente?", ["Se divide el desnivel entre la distancia: 15 ÷ 300 = 0,05.", "Multiplicado por 100 da 5 por ciento."], "5 por ciento"),
        ("Rodeo más largo", "Una ruta directa de ejemplo mide 250 metros y cruza una zona de exclusión. El rodeo mide 100 más 300 metros. ¿Cuánto más largo es el rodeo y se usa?", ["El rodeo mide 100 + 300 = 400 metros.", "400 menos 250 son 150 metros más; igual se usa, porque la directa cruza la zona."], "150 metros más largo; se usa el rodeo"),
    ],
    mistakes=[("Elegir la ruta más corta aunque cruce una zona de exclusión.", "La zona de exclusión existe por un peligro real y no se cruza.", "Se usa el rodeo, aunque sea más largo, y se informa al jefe."),
              ("Resolver una discrepancia entre libreta y plano eligiendo el dato que «parece mejor».", "Puede ser un error de copia en cualquiera de los dos registros.", "Se avisa al topógrafo, se revisa la medición original y se corrige con firma.")],
    T=[
        ("abc", "En Geología: ¿qué es la pendiente de un tramo de terreno?", "Su inclinación, calculada como desnivel dividido por distancia horizontal, por 100", "La suma de las cotas de sus dos extremos", "El largo del tramo medido en el plano", "La pendiente relaciona altura con distancia horizontal; no es una suma ni un largo."),
        ("abc", "En Geología: ¿qué es un error de transposición?", "Anotar los dígitos de un número en otro orden, como 5.700 escrito 5.070", "Perder una hoja de la libreta de terreno", "Cambiar la escala del plano sin avisar", "La transposición cambia el orden de los dígitos; no es una pérdida de hoja ni un cambio de escala."),
        ("abc", "En Geología: ¿qué es una discrepancia entre dos registros?", "Una diferencia entre dos registros de un mismo dato", "Un registro más largo que otro", "Un dato que coincide en ambos registros", "Una discrepancia es una diferencia que se debe investigar."),
        ("=", "{F} ¿Cuántos metros de distancia horizontal hay entre P2 y P3, que están en la misma coordenada Este?", "5700-5400", "Se resta la coordenada Norte de P2 a la de P3.", " metros"),
        ("=", "{F} ¿Cuántos metros de desnivel hay entre P1 y P2?", "1830-1800", "Se resta la cota de P1 a la de P2.", " metros"),
        ("=", "{F} ¿Cuál es la pendiente en porcentaje del tramo recto de P1 a P2, de 500 metros de distancia horizontal?", "(30*100)//500", "Se divide el desnivel entre la distancia horizontal y se multiplica por 100.", " por ciento"),
        ("=", "{F} ¿Cuál es la pendiente en porcentaje del tramo de P2 a P3?", "(30*100)//300", "Se calcula el desnivel de 30 metros dividido entre 300 metros, por 100.", " por ciento"),
        ("abc", "{F} ¿Qué tramo es más empinado, comparando sus pendientes?", "De P2 a P3, que tiene 10 por ciento", "De P1 a P2, que tiene 6 por ciento", "Ambos tienen la misma inclinación", "10 por ciento es mayor que 6 por ciento, aunque el desnivel de ambos sea el mismo."),
        ("=", "{F} ¿Cuántos metros más largo es el rodeo por Q que el tramo recto de 500 metros entre P1 y P2?", "(300+400)-500", "Se suma el recorrido del rodeo y se resta la ruta recta.", " metros"),
        ("abc", "{F} ¿Qué ruta corresponde elegir entre P1 y P2?", "El rodeo por Q, porque el tramo recto cruza la zona de exclusión", "El tramo recto, si se camina rápido", "El tramo recto, pero cruzando solo por la parte más angosta", "Una zona de exclusión no se cruza; el rodeo es más largo, pero evita el peligro."),
        ("=", "{F} ¿Cuántos minutos se demora el rodeo de 700 metros?", "700//70", "Se divide el largo del rodeo entre los metros que se caminan por minuto.", " minutos"),
        ("abc", "{F} La libreta anota S-3 en N 5.070 y el plano en N 5.700. ¿Qué tipo de error es probable y qué corresponde?", "Una transposición de dígitos; hay que avisar al topógrafo y revisar la medición original antes de ubicar el sitio", "Una diferencia de escala; se promedian ambos valores", "Un error del plano; se usa siempre la libreta", "Los dígitos están en otro orden; no se elige un dato sin revisar la medición original."),
        ("abc", "{F} El topógrafo informa que el plano está desactualizado y que la zona de exclusión creció hacia el Este. ¿Qué conviene hacer?", "Usar el plano vigente y revisar de nuevo la ruta antes de aprobarla", "Mantener el plano antiguo, porque ya fue aprobado", "Corregir a mano el plano antiguo sin avisar a nadie", "Se trabaja con el plano vigente; corregir a mano sin avisar crea otro riesgo."),
    ],
    ctx=("abc", "Un compañero te propone «tomar el atajo» por una zona marcada como exclusión en un plano de práctica, porque ahorra 10 minutos. ¿Qué respondes?", "Que no se cruza la zona de exclusión y que lo hablarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, si van rápido", "Que sí, pero solo una vez", "Una zona de exclusión existe por un peligro real; ahorrar tiempo no justifica cruzarla."),
    sc=[
        ("En Geología: ¿cómo se calcula la pendiente en porcentaje?", "Se divide el desnivel entre la distancia horizontal y se multiplica por 100", "La pendiente relaciona altura y distancia horizontal."),
        ("En la lectura de planos: ¿qué ruta se descarta aunque sea más corta?", "La que cruza una zona de exclusión", "La seguridad pesa más que la distancia."),
        ("¿Qué se hace ante una discrepancia entre la libreta y el plano?", "Se avisa al topógrafo y se revisa la medición original", "La corrección se hace con la medición original y con firma."),
    ],
    op=("Plano de ejemplo del «Sector Cresta Demo»: A en E 1.000, N 1.000, cota 900; B en E 1.600, N 1.800, cota 940. El tramo recto entre A y B cruza una zona de exclusión; el rodeo pasa por C, en E 1.600 y N 1.000. Escribe (a) la distancia horizontal entre A y B (diferencias de 600 y 800 metros), (b) la pendiente en porcentaje del tramo A-B, (c) cuántos metros más largo es el rodeo por C que el tramo recto y cuál usarías, (d) qué haces si la libreta anota B en N 1.080 y el plano en N 1.800.",
        "(a) 1.000 metros, porque 600 y 800 forman un triángulo de lados 3, 4 y 5 por 200. (b) 40 ÷ 1.000 × 100 = 4 por ciento. (c) El rodeo mide 600 + 800 = 1.400 metros, 400 más que el recto; se usa el rodeo porque el recto cruza la zona de exclusión. (d) Es probable un error de transposición: aviso al topógrafo y reviso la medición original antes de ubicar el sitio.",
        ["obtiene la distancia horizontal", "calcula bien la pendiente", "descarta la ruta que cruza la zona", "trata la discrepancia sin elegir al azar"],
        ["hoja con las cuatro respuestas"],
        ["usar la distancia recta sin considerar la zona", "dividir mal la pendiente", "elegir un dato de la discrepancia sin revisar"],
        "Pregunta: «¿qué dato divides entre cuál para obtener la pendiente?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos puntos con cota y una distancia horizontal exacta, y calcula la pendiente en porcentaje.",
    extend="Explica con un ejemplo por qué el rodeo más largo puede ser la mejor decisión.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). Plano del «Sector Meseta Demo», escala 1:2.500 (1 centímetro del plano equivale a 25 metros). El punto de partida A está en E 4.000 y N 7.000. "
     "La faena F-1 queda a 400 metros de A, con azimut 90 (hacia el Este). La faena F-2 queda a 300 metros de F-1, con azimut 0 (hacia el Norte). El desnivel entre F-1 y F-2 es de 33 metros. "
     "Criterios de ejemplo del proyecto: pendiente máxima del camino, 12 por ciento; tolerancia de ubicación, 5 metros en cada coordenada (los valores reales los fija la norma vigente). El receptor marca para F-2: E 4.398 y N 7.303.")
build(
    O3, 4, F,
    use="Aprenderé a ubicar puntos con azimut y distancia, a convertir medidas del plano con la escala, a comparar una pendiente con un criterio y a verificar una ubicación con una tolerancia, todo con datos de ejemplo.",
    prior=["Sé qué son coordenadas, escala y pendiente.", "Sé calcular desnivel y distancia horizontal.", "Sé comparar una medida con un criterio."],
    explain=[
        "El azimut es el ángulo que se mide desde el Norte hacia la derecha, en el sentido de los punteros del reloj, para indicar una dirección: azimut 0 es hacia el Norte, 90 hacia el Este, 180 hacia el Sur y 270 hacia el Oeste. Si desde un punto se avanza una distancia en azimut 90, la coordenada Este aumenta esa distancia y la Norte no cambia; en azimut 0, aumenta la Norte y no cambia la Este.",
        "La tolerancia es el desvío máximo aceptado entre el punto real y el punto del plano. Para verificar una ubicación se calcula la diferencia en cada coordenada y se compara con la tolerancia; si una diferencia la supera, no se da por buena la ubicación: se revisa si hay un error de lectura o de copia, se repite la verificación con otro punto de referencia y se informa. Redondear coordenadas «para que se vea ordenado» pierde precisión y puede mover un punto más que la tolerancia.",
        f"Las ubicaciones reales las determina y verifica personal autorizado con instrumentos calibrados. {EMER} {AVISO}",
    ],
    vocab=[("azimut", "ángulo medido desde el Norte hacia la derecha que indica una dirección"), ("tolerancia", "desvío máximo aceptado entre el punto real y el del plano"), ("criterio de aceptación", "regla que dice cuándo un resultado se acepta"), ("punto de referencia", "punto conocido que sirve para comprobar otra ubicación"), ("precisión", "cercanía entre una medida y el valor que se busca")],
    worked=[
        ("Ubicar por azimut", "Desde un punto de ejemplo en E 1.000 y N 2.000 se avanzan 150 metros con azimut 180. ¿Dónde se llega?", ["Azimut 180 es hacia el Sur: la coordenada Norte disminuye.", "El Este no cambia y el Norte queda en 2.000 menos 150, que es 1.850."], "E 1.000 y N 1.850"),
        ("Verificar con tolerancia", "Un punto de ejemplo debería estar en N 3.200 y el receptor marca 3.204. La tolerancia es de 5 metros. ¿Cumple?", ["La diferencia es 3.204 menos 3.200, que son 4 metros.", "4 es menor que 5."], "Cumple"),
    ],
    mistakes=[("Redondear todas las coordenadas a la centena para que el plano se vea ordenado.", "Puede mover un punto hasta 50 metros, mucho más que la tolerancia.", "Se anotan las coordenadas con la precisión que exige el proyecto."),
              ("Aceptar una ubicación fuera de tolerancia porque «seguro es un error del receptor».", "Sin comprobar, no se sabe si el error es del receptor, de la copia o del plano.", "Se revisa, se repite la verificación con otro punto de referencia y se informa.")],
    T=[
        ("abc", "En Geología: ¿qué es el azimut?", "El ángulo medido desde el Norte hacia la derecha que indica una dirección", "La altura de un punto sobre el nivel del mar", "La distancia entre dos puntos en el plano", "El azimut indica dirección; la altura es la cota y la distancia es otro dato."),
        ("abc", "En Geología: ¿qué dirección indica un azimut de 180?", "Hacia el Sur", "Hacia el Este", "Hacia el Norte", "Desde el Norte, 90 es Este, 180 es Sur y 270 es Oeste."),
        ("abc", "En Geología: ¿qué es la tolerancia en la ubicación de un punto?", "El desvío máximo aceptado entre el punto real y el del plano", "El número de puntos que se pueden ubicar al día", "La escala del plano en centímetros", "La tolerancia fija cuánto desvío se acepta."),
        ("=", "{F} Un tramo mide 16 centímetros en el plano. ¿Cuántos metros reales son?", "16*25", "Se multiplican los centímetros por los 25 metros de cada centímetro.", " metros"),
        ("=", "{F} ¿Cuál es la coordenada Este de F-1?", "4000+400", "En azimut 90 se suma la distancia a la coordenada Este.", ""),
        ("=", "{F} ¿Cuál es la coordenada Norte de F-2?", "7000+300", "En azimut 0 se suma la distancia a la coordenada Norte de F-1.", ""),
        ("abc", "{F} ¿Qué azimut tendría el recorrido de regreso, de F-2 a F-1?", "180, hacia el Sur", "0, hacia el Norte", "90, hacia el Este", "F-2 está al Norte de F-1; volver es ir hacia el Sur, y el azimut del Sur es 180."),
        ("=", "{F} ¿Cuál es la pendiente en porcentaje del tramo de F-1 a F-2?", "(33*100)//300", "Se divide el desnivel entre la distancia horizontal y se multiplica por 100.", " por ciento"),
        ("abc", "{F} ¿Cumple ese tramo el criterio de pendiente máxima de 12 por ciento?", "Sí, porque 11 es menor que 12", "No, porque 11 es mayor que 10", "No se puede saber sin medir de nuevo el plano", "La pendiente calculada es de 11 por ciento, que no supera el máximo."),
        ("abc", "{F} El receptor marca para F-2 la posición dada. Con una tolerancia de 5 metros en cada coordenada, ¿cumple?", "Sí, porque las diferencias son 2 metros al Este y 3 al Norte", "No, porque no coincide exactamente", "No, porque la diferencia al Norte es mayor que la del Este", "Las diferencias de 2 y 3 metros son menores que la tolerancia de 5."),
        ("abc", "{F} Otra lectura marca N 7.330 en lugar de 7.303. ¿Qué corresponde hacer?", "No aceptar el punto, revisar si hay error de lectura o de copia, repetir con otro punto de referencia e informar", "Aceptarlo, porque la diferencia es solo un poco mayor", "Corregir el plano para que coincida con la lectura", "27 metros superan la tolerancia de 5; se investiga en vez de acomodar el dato."),
        ("=", "{F} ¿Cuántos centímetros ocupa en el plano el tramo de 300 metros de F-1 a F-2?", "300//25", "Se divide la distancia real entre los metros que vale cada centímetro.", " centímetros"),
        ("abc", "{F} Un compañero redondea todas las coordenadas a la centena para que el plano se vea ordenado. ¿Qué efecto tiene?", "Pierde precisión: puede desplazar un punto hasta 50 metros, mucho más que la tolerancia", "Ninguno, porque el redondeo solo afecta la estética", "Mejora la precisión al eliminar los dígitos pequeños", "Redondear a la centena puede mover un punto hasta 50 metros y supera la tolerancia de 5."),
    ],
    ctx=("abc", "Una compañera te propone corregir las coordenadas de un plano de práctica para que todos los puntos «calcen» con la tolerancia antes de entregarlo. ¿Qué respondes?", "Que no se acomodan los datos y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, pero solo los que se pasan por poco", "Que sí, y se avisa después de entregar", "Acomodar datos oculta un error que puede ubicar mal una faena."),
    sc=[
        ("En Geología: ¿qué es el azimut?", "El ángulo medido desde el Norte hacia la derecha que indica una dirección", "El azimut permite indicar una dirección con un número."),
        ("En la verificación de una ubicación: ¿con qué se compara la diferencia entre el punto real y el del plano?", "Con la tolerancia fijada para el proyecto", "La tolerancia dice cuánto desvío se acepta."),
        ("¿Qué se hace si una lectura supera la tolerancia?", "Se revisa, se repite con otro punto de referencia y se informa", "Un dato fuera de tolerancia no se acomoda: se investiga."),
    ],
    op=("Plano de ejemplo del «Sector Quebrada Demo», escala 1:5.000 (1 centímetro equivale a 50 metros). El punto A está en E 3.000 y N 6.000. La faena G-1 queda a 500 metros de A con azimut 270, y el desnivel hacia G-1 es de 20 metros. Criterio de ejemplo: pendiente máxima de 5 por ciento y tolerancia de 4 metros en cada coordenada. Escribe (a) cuántos centímetros ocupa el tramo en el plano, (b) las coordenadas de G-1, (c) si cumple la pendiente, (d) si una lectura de E 2.497 y N 6.001 cumple la tolerancia.",
        "(a) 500 ÷ 50 = 10 centímetros. (b) Azimut 270 es hacia el Oeste: el Este disminuye, E 3.000 − 500 = 2.500 y N 6.000. (c) 20 ÷ 500 × 100 = 4 por ciento, que es menor que 5: cumple. (d) Diferencias de 3 metros al Este y 1 al Norte, menores que 4: cumple. Todo se verifica con personal autorizado.",
        ["convierte bien la escala", "ubica G-1 con el azimut correcto", "calcula y compara la pendiente", "verifica la tolerancia en cada coordenada"],
        ["hoja con las cuatro respuestas"],
        ["sumar al Este con azimut 270", "olvidar multiplicar por 100 en la pendiente", "comparar solo una coordenada"],
        "Pregunta: «¿hacia dónde apunta el azimut 270 y qué coordenada cambia?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Desde un punto inventado en E 2.000 y N 3.000, avanza 200 metros con azimut 0 y escribe las nuevas coordenadas.",
    extend="Explica con un ejemplo por qué una lectura fuera de tolerancia no se corrige acomodando el dato.",
)
