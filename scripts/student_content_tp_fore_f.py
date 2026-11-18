"""Forestal TP 3.º y 4.º medio: OAE-05 (control de patógenos: conceptos, monitoreo, decisión y documentos). Solo conceptos y cálculos en papel; sin dosis, mezclas ni procedimientos de aplicación."""
from __future__ import annotations

from tp_fore_common import AVISO, EMER, build

O5 = "TP-FORE-3y4-OAE-05"

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En el sector 3 del «Vivero Demo» aparecen plantas de «especie A» con manchas oscuras en las hojas. "
     "Peligros anotados en la bodega de productos de uso sanitario: contacto con la piel, inhalación de vapores, derrames, almacenamiento inadecuado y envases vacíos acumulados (36 envases; el gestor autorizado retira 12 por visita).")
build(
    O5, 1, F,
    use="Aprenderé qué es un patógeno, qué métodos de control existen en términos generales, cuáles son los peligros de los productos de uso sanitario y las reglas de seguridad y de manejo de residuos, sin aprender a usarlos.",
    prior=["Sé qué es un vivero.", "Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé dividir números enteros."],
    explain=[
        "Un patógeno es un organismo, como un hongo, una bacteria o un virus, que causa una enfermedad en una planta. La enfermedad es una alteración del funcionamiento normal de la planta. Para cuidar las plantas se usan métodos preventivos, que buscan evitar que el patógeno aparezca o se propague, y métodos curativos, que actúan cuando el problema ya existe. Los métodos pueden ser químicos, orgánicos o biológicos; sus diferencias se estudian en las próximas clases.",
        "Los productos de uso sanitario pueden ser peligrosos para las personas y el ambiente: el contacto con la piel, la inhalación de vapores, los derrames y el mal almacenamiento son los peligros principales. Se controlan con la jerarquía: prevenir para no necesitar el producto, sustituir por uno menos peligroso, almacenar en una bodega adecuada, reglas y capacitación, y el equipo de protección personal como última barrera. Los envases vacíos se entregan a un gestor autorizado; nunca se reutilizan ni se tiran a la basura común.",
        f"La elección del método, su preparación y su uso son tareas de personal capacitado y autorizado, bajo la norma sanitaria, ambiental y laboral vigente. Este cuaderno no entrega dosis, mezclas ni formas de aplicación. {EMER} {AVISO}",
    ],
    vocab=[("patógeno", "organismo que causa una enfermedad en una planta"), ("enfermedad de la planta", "alteración del funcionamiento normal de la planta"), ("método preventivo", "método que busca evitar que el patógeno aparezca o se propague"), ("método curativo", "método que actúa cuando el problema ya existe"), ("producto de uso sanitario", "producto destinado a cuidar la salud de las plantas"), ("hoja de datos de seguridad", "documento que informa sobre los peligros de un producto y cómo actuar ante un accidente"), ("gestor autorizado", "empresa autorizada para retirar y tratar residuos peligrosos")],
    worked=[
        ("Preventivo o curativo", "En un vivero de ejemplo se ordena y se mantiene limpio el sector para evitar que aparezca una enfermedad. ¿Qué tipo de método es?", ["Se actúa antes de que exista el problema.", "Evitar que aparezca es la definición de un método preventivo."], "Preventivo"),
        ("Visitas de un gestor", "Un vivero de ejemplo acumula 30 envases vacíos y el gestor autorizado retira 10 por visita. ¿Cuántas visitas hacen falta?", ["Se divide el total entre lo que retira en cada visita.", "30 ÷ 10 = 3."], "3 visitas"),
    ],
    mistakes=[("Creer que cualquier envase vacío puede reutilizarse para guardar agua o alimentos.", "Los envases de productos de uso sanitario conservan restos peligrosos.", "Se entregan a un gestor autorizado según el plan de residuos."),
              ("Creer que leer la hoja de datos de seguridad habilita para manipular el producto.", "La manipulación exige personal capacitado y autorizado.", "Usa la hoja para entender los peligros y deja la tarea a quien corresponde.")],
    T=[
        ("abc", "En Forestal: ¿qué es un patógeno de una planta?", "Un organismo, como un hongo o una bacteria, que causa una enfermedad en la planta", "Un producto que protege a la planta de las enfermedades", "El material en el que crecen las raíces", "El patógeno es el organismo causante; los productos y el sustrato son otros elementos."),
        ("abc", "En Forestal: ¿qué diferencia hay entre un método preventivo y uno curativo?", "El preventivo evita que el problema aparezca y el curativo actúa cuando ya existe", "El preventivo siempre usa productos y el curativo nunca", "El preventivo se usa en bosques y el curativo en viveros", "Se distinguen por el momento de actuar, no por el lugar ni por el uso de productos."),
        ("abc", "En Forestal: ¿para qué sirve la hoja de datos de seguridad de un producto?", "Para informar sobre sus peligros y cómo actuar ante un accidente", "Para fijar el precio al que se vende", "Para autorizar a cualquier persona a manipularlo", "La hoja informa peligros y medidas; no fija precios ni autoriza personas."),
        ("=", "{F} ¿Cuántas visitas del gestor autorizado se necesitan para retirar todos los envases vacíos acumulados?", "36//12", "Se divide el total de envases entre los que se retiran en cada visita.", " visitas"),
        ("abc", "{F} ¿Qué corresponde hacer con los envases vacíos acumulados?", "Entregarlos a un gestor autorizado según el plan de residuos", "Reutilizarlos para guardar agua o alimentos", "Botarlos al basurero común", "Los envases conservan restos peligrosos y exigen gestión autorizada."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «contacto del producto con la piel»?", "Que la persona sufra irritación o intoxicación", "El producto guardado en su envase", "Que cambie el color del envase", "El riesgo es la posibilidad de daño a la persona; el producto es la fuente del peligro."),
        ("abc", "{F} Reemplazar un producto muy peligroso por otro menos peligroso, cuando el plan lo permite, es un control de nivel:", "De sustitución", "De EPP", "Administrativo", "Sustituir es cambiar la fuente de peligro por una menos dañina."),
        ("abc", "{F} Un letrero en la bodega que dice «solo personal autorizado» es un control de tipo:", "Administrativo, porque informa y ordena una conducta", "De ingeniería, porque cambia físicamente el lugar", "De eliminación, porque quita los productos", "El letrero informa y regula, pero no cambia físicamente el lugar."),
        ("abc", "{F} Una compañera dice: «leí la hoja de datos de seguridad, así que puedo preparar una mezcla». ¿Qué respuesta es correcta?", "Es falso: preparar y usar productos exige personal capacitado y autorizado", "Es cierto, si usa guantes", "Es cierto, si otra persona la observa", "Leer una hoja no habilita para manipular productos."),
        ("abc", "Durante una visita de ejemplo, una persona se desmaya cerca de la bodega de productos. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a la bodega a sacarla rápido", "Sacudirla para que reaccione y llevarla a la oficina", "Intervenir sin formación puede causar otra intoxicación; se avisa a quienes pueden actuar."),
        ("abc", "En Forestal: ¿por qué es mejor prevenir que depender de productos de uso sanitario?", "Porque prevenir reduce la necesidad de productos y con ello la exposición de las personas", "Porque los productos de uso sanitario nunca sirven", "Porque prevenir siempre es gratis", "Prevenir actúa sobre el origen y reduce el peligro para el personal."),
        ("=", "Un vivero de ejemplo genera 9 envases vacíos por mes. ¿En cuántos meses se juntan 36 envases?", "36//9", "Se divide el total de envases entre los que se generan cada mes.", " meses"),
        ("abc", "{F} ¿Qué medida de la bodega es un control de ingeniería?", "Ventilación y estanterías con contención de derrames", "Una charla de capacitación al inicio del año", "Entregar guantes a todo el personal", "Ventilación y contención cambian el lugar; la charla es administrativa y los guantes son EPP."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por preparar «unas mezclas» en su vivero, porque «tú ya sabes de eso por clases». ¿Qué respondes?", "Que no, porque esa tarea exige personal autorizado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si usas guantes y mascarilla", "Que sí, si es una cantidad pequeña", "El EPP o la cantidad no reemplazan la autorización, la formación ni la norma vigente."),
    sc=[
        ("En Forestal: ¿qué es un patógeno?", "Un organismo que causa una enfermedad en una planta", "El patógeno es el causante de la enfermedad."),
        ("¿Qué se hace con un envase vacío de un producto de uso sanitario?", "Se entrega a un gestor autorizado", "Los envases vacíos conservan restos de producto peligrosos."),
        ("¿Quién prepara y usa los productos de uso sanitario?", "Personal capacitado y autorizado", "La manipulación exige formación y autorización."),
    ],
    op=("Ficha de ejemplo: el «Vivero Muestra» acumula 45 envases vacíos de productos de uso sanitario y el gestor autorizado retira 15 por visita. Peligros anotados: derrames y almacenamiento inadecuado. Escribe (a) cuántas visitas hacen falta, (b) un control administrativo para el almacenamiento, (c) un control de ingeniería para los derrames, (d) por qué este cuaderno no te habilita para manipular los productos.",
        "(a) 45 ÷ 15 = 3 visitas. (b) Una regla de acceso a la bodega solo para personal autorizado, con un registro de entradas. (c) Estanterías con contención de derrames y buena ventilación. (d) Porque la manipulación exige personal capacitado y autorizado, la norma vigente y elementos de protección.",
        ["calcula las visitas", "propone un control administrativo", "propone un control de ingeniería", "explica por qué no habilita"],
        ["hoja con las cuatro respuestas"],
        ["no dividir los envases entre lo que retira el gestor", "proponer solo el EPP", "creer que leer habilita para usar productos"],
        "Pregunta: «¿qué control actúa sobre el lugar y no depende de las personas?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe una oración que distinga un método preventivo de uno curativo con un ejemplo inventado.",
    extend="Explica con un ejemplo por qué los envases vacíos de productos de uso sanitario no deben reutilizarse.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (documentos y datos de ejemplo, inventados). Lote L-40 de «especie A», 300 plantas. Se revisaron 60 plantas y 6 muestran síntomas: manchas oscuras en las hojas. Sobre algunas hojas se ve un polvillo gris, que es una estructura del propio patógeno. "
     "Documentos del vivero: el registro de monitoreo (cuántas plantas se revisan y cuántas tienen síntomas), la etiqueta de cada producto (usos permitidos, precauciones y advertencias), la hoja de datos de seguridad y el registro de aplicaciones, que llena personal autorizado.")
build(
    O5, 2, F,
    use="Aprenderé los conceptos de síntoma, signo, monitoreo e incidencia, los métodos químicos, orgánicos y biológicos en términos generales, los documentos del control de patógenos y los roles.",
    prior=["Sé qué es un patógeno y un método preventivo o curativo.", "Sé calcular un porcentaje simple.", "Sé qué es una muestra."],
    explain=[
        "Una planta enferma muestra síntomas, que son los cambios que se observan en ella, como manchas en las hojas. Los signos son estructuras visibles del propio patógeno, como un polvillo sobre la hoja. El monitoreo es revisar cada cierto tiempo una muestra de plantas y registrar cuántas tienen síntomas. La incidencia es el porcentaje de plantas revisadas que tienen síntomas. Un buen monitoreo permite detectar un problema a tiempo y decidir con datos.",
        "El manejo integrado combina varios métodos. Un método químico usa productos fabricados por la industria; uno orgánico usa sustancias de origen natural permitidas; uno biológico usa organismos vivos que reducen al patógeno. Cada producto trae una etiqueta con sus usos permitidos y sus advertencias, y una hoja de datos de seguridad. No existen productos «inofensivos»: todos exigen precauciones. Solo el profesional responsable decide qué método usar, y personal autorizado lo ejecuta y lo anota en el registro de aplicaciones.",
        f"Los productos, sus cantidades y sus formas de uso los fijan la etiqueta, el profesional responsable y la norma vigente; aquí no se entregan. {EMER} {AVISO}",
    ],
    vocab=[("síntoma", "cambio que se observa en la planta enferma"), ("signo", "estructura visible del propio patógeno sobre la planta"), ("monitoreo", "revisión periódica de una muestra de plantas con registro de lo observado"), ("incidencia", "porcentaje de plantas revisadas que tienen síntomas"), ("método químico", "método que usa productos fabricados por la industria"), ("método orgánico", "método que usa sustancias de origen natural permitidas"), ("método biológico", "método que usa organismos vivos que reducen al patógeno"), ("etiqueta", "documento del producto con sus usos permitidos, precauciones y advertencias")],
    worked=[
        ("Calcular la incidencia", "En un monitoreo de ejemplo se revisan 50 plantas y 5 tienen síntomas. ¿Cuál es la incidencia?", ["5 ÷ 50 son 10 de cada 100.", "La incidencia es 10 %."], "10 %"),
        ("Síntoma o signo", "Un registro de ejemplo anota «hojas amarillas» y «polvillo blanco sobre las hojas». ¿Cuál es síntoma y cuál es signo?", ["Un cambio en la planta es un síntoma.", "Un polvillo del propio patógeno es un signo."], "Hojas amarillas: síntoma; polvillo blanco: signo"),
    ],
    mistakes=[("Creer que si un producto es «natural» no necesita precauciones.", "Un producto de origen natural también puede ser peligroso.", "Lee su etiqueta y su hoja de datos de seguridad, y que lo use personal autorizado."),
              ("Concluir sobre todo el lote revisando solo las plantas más sanas.", "La muestra deja de representar al lote.", "Revisa una muestra sin elegir solo las plantas buenas.")],
    T=[
        ("abc", "En Forestal: ¿qué es un síntoma en una planta enferma?", "Un cambio que se observa en la planta, como manchas en las hojas", "Una estructura visible del propio patógeno", "Un producto que se aplica sobre la planta", "Un síntoma es un cambio de la planta; el polvillo del patógeno es un signo."),
        ("abc", "En Forestal: ¿qué es un signo de una enfermedad?", "Una estructura visible del propio patógeno, como un polvillo sobre la hoja", "Un cambio de color de las hojas de la planta", "El registro del monitoreo del vivero", "El signo pertenece al patógeno; el cambio de color es un síntoma."),
        ("abc", "En Forestal: ¿qué es el control biológico?", "El uso de organismos vivos que reducen al patógeno", "El uso de productos fabricados por la industria", "El uso de sustancias de origen natural permitidas", "Control biológico significa usar organismos vivos; los productos industriales son métodos químicos y las sustancias naturales, métodos orgánicos."),
        ("=", "{F} ¿Cuál es la incidencia en la muestra revisada?", "6*100//60", "Se divide las plantas con síntomas entre las revisadas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas de las plantas revisadas no muestran síntomas?", "60-6", "Se restan las plantas con síntomas a las revisadas.", " plantas"),
        ("=", "{F} Si la proporción de la muestra se mantiene en todo el lote, ¿cuántas plantas con síntomas se estiman en las 300 del lote?", "300*6//60", "Se aplica a todo el lote la proporción de la muestra, 6 de cada 60.", " plantas"),
        ("abc", "{F} ¿Qué documento informa los usos permitidos y las advertencias de un producto?", "La etiqueta del producto", "El registro de monitoreo", "El registro de aplicaciones", "La etiqueta es el documento del producto; los registros anotan lo observado o lo realizado."),
        ("abc", "{F} ¿Quién decide qué método de control usar?", "El profesional responsable", "El personal que prepara los productos", "El proveedor que los vende", "Decide el profesional responsable; el proveedor vende y el personal ejecuta."),
        ("abc", "{F} Una compañera ofrece «un producto sin etiqueta que sirvió en otro vivero». ¿Qué respuesta es correcta?", "No usarlo: sin etiqueta no se conocen usos ni advertencias, y se consulta al profesional responsable", "Usarlo si funcionó en otro lugar", "Usarlo si la dosis es pequeña", "Sin etiqueta no se puede saber si el producto es adecuado ni cómo protegerse."),
        ("abc", "En Forestal: ¿cuál es un ejemplo de método preventivo?", "Mantener el vivero limpio y ordenado y usar plantas sanas", "Esperar a ver si la enfermedad desaparece sola", "Actuar solo cuando ya hay síntomas en todo el lote", "Un método preventivo actúa antes de que aparezca o se extienda el problema."),
        ("abc", "En Forestal: ¿por qué se monitorea de forma regular un lote de plantas?", "Para detectar un problema a tiempo y decidir con datos", "Para eliminar el patógeno con la sola revisión", "Para aplicar un producto apenas aparezca una mancha", "El monitoreo informa, pero no elimina el problema ni obliga a actuar de inmediato."),
        ("=", "{F} Si el vivero tiene 1.500 plantas de la misma especie y se mantuviera esta incidencia, ¿cuántas plantas con síntomas se estimarían?", "1500*10//100", "Se calcula el 10 % de las plantas del vivero.", " plantas"),
        ("abc", "{F} Un compañero revisó solo las 10 plantas más cercanas a la puerta y concluye sobre todo el lote. ¿Qué limitación tiene su conclusión?", "La muestra es pequeña y poco representativa del lote entero", "Ninguna, porque las plantas cercanas siempre son las más enfermas", "Que debería revisar solo plantas sanas", "Una muestra pequeña y concentrada en un solo lugar puede no representar al lote."),
    ],
    ctx=("abc", "Te ofrecen trabajo preparando mezclas con una «receta» que un amigo usa en su vivero. ¿Qué respondes?", "Que no, porque preparar mezclas exige personal autorizado, etiqueta y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si la receta es de confianza", "Que sí, si trabajas con ventana abierta", "Una receta informal no reemplaza la etiqueta, la formación ni la autorización."),
    sc=[
        ("En Forestal: ¿qué es la incidencia?", "El porcentaje de plantas revisadas que tienen síntomas", "La incidencia relaciona plantas con síntomas y plantas revisadas."),
        ("¿Qué es un síntoma?", "Un cambio que se observa en la planta enferma", "Los síntomas son cambios de la propia planta."),
        ("¿Quién decide el método de control?", "El profesional responsable", "La decisión técnica es del profesional responsable."),
    ],
    op=("Ficha de ejemplo: lote L-60 de «especie B», 400 plantas. Monitoreo: se revisaron 80 plantas y 4 tienen síntomas (hojas con manchas); en una hoja se ve un polvillo blanco. Escribe (a) la incidencia, (b) cuántas plantas con síntomas se estiman en el lote, (c) cuál dato es síntoma y cuál es signo, (d) quién decide qué método usar y qué documento informa las advertencias del producto.",
        "(a) 4 ÷ 80 = 5 %. (b) 400 × 4 ÷ 80 = 20 plantas. (c) Las manchas son un síntoma; el polvillo blanco es un signo. (d) Decide el profesional responsable; las advertencias están en la etiqueta y en la hoja de datos de seguridad.",
        ["calcula la incidencia", "estima el total del lote", "distingue síntoma y signo", "nombra rol y documento"],
        ["hoja con las cuatro respuestas"],
        ["confundir síntoma con signo", "no multiplicar por el tamaño del lote", "creer que el proveedor decide el método"],
        "Pregunta: «¿qué se observa en la planta y qué pertenece al patógeno?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un monitoreo de 40 plantas con 2 con síntomas y calcula la incidencia.",
    extend="Explica con un ejemplo por qué un producto de origen natural también necesita precauciones.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (monitoreo de ejemplo, inventado). «Vivero Demo», semana 20, «especie A». Sector 1: 500 plantas revisadas, 30 con síntomas. Sector 2: 150 plantas revisadas, 27 con síntomas. Sector 3: 250 plantas revisadas, 25 con síntomas. "
     "Umbral de ejemplo del plan: si la incidencia de un sector supera 12 %, se informa de inmediato al profesional responsable.")
build(
    O5, 3, F,
    use="Aprenderé a analizar una tabla de monitoreo por sectores: calcular incidencias, compararlas con un umbral y decidir qué informar y a quién.",
    prior=["Sé calcular la incidencia.", "Sé qué es un porcentaje y una muestra.", "Sé qué es un registro."],
    explain=[
        "Un umbral es un valor a partir del cual se debe decidir o informar. En el monitoreo se calcula la incidencia de cada sector y se compara con el umbral del plan. Comparar solo la cantidad de plantas con síntomas engaña, porque los sectores revisados pueden tener tamaños distintos: lo correcto es comparar porcentajes. Por ejemplo, 12 plantas con síntomas en una revisión de 400 son 3 %, y menos preocupantes que 6 en una revisión de 20, que son 30 %.",
        "La severidad es qué tan grave es el daño en cada planta afectada, y es distinta de la incidencia, que dice cuántas plantas están afectadas. Cuando un sector supera el umbral, no se actúa por cuenta propia: se informa de inmediato al profesional responsable, con el registro, la fecha y el sector. Cuando está bajo el umbral, se sigue monitoreando. Siempre se anota el dato tal como es, aunque sea incómodo.",
        f"El análisis lo hace el profesional responsable; tú practicas los cálculos y el razonamiento. {EMER} {AVISO}",
    ],
    vocab=[("umbral", "valor a partir del cual se debe decidir o informar"), ("severidad", "qué tan grave es el daño en cada planta afectada"), ("sector", "parte del vivero que se revisa por separado"), ("comparar porcentajes", "usar la incidencia y no la cantidad de plantas para comparar sectores")],
    worked=[
        ("Comparar con el umbral", "Un umbral de ejemplo es 10 %. Un sector revisó 200 plantas y 30 tienen síntomas. ¿Lo supera?", ["30 ÷ 200 son 15 de cada 100.", "15 % es mayor que 10 %."], "Sí, lo supera"),
        ("Dos sectores", "El sector A de ejemplo tiene 8 plantas con síntomas en 40 revisadas y el sector B tiene 12 en 120 revisadas. ¿Cuál tiene mayor incidencia?", ["A: 8 ÷ 40 = 20 %.", "B: 12 ÷ 120 = 10 %."], "El sector A"),
    ],
    mistakes=[("Comparar sectores solo por la cantidad de plantas con síntomas.", "Los sectores pueden tener distinta cantidad de plantas revisadas.", "Compara las incidencias, es decir, los porcentajes."),
              ("Aplicar algo por cuenta propia cuando un sector supera el umbral.", "La decisión corresponde al profesional responsable.", "Informa de inmediato con el registro, la fecha y el sector.")],
    T=[
        ("abc", "En Forestal: ¿qué es la incidencia de un sector?", "El porcentaje de plantas revisadas con síntomas", "La gravedad del daño en cada planta", "La cantidad de productos que tiene la bodega", "La incidencia mide cuántas plantas están afectadas, no la gravedad."),
        ("abc", "En Forestal: ¿qué es la severidad de una enfermedad?", "Qué tan grave es el daño en cada planta afectada", "El porcentaje de plantas que tienen síntomas", "La cantidad de plantas revisadas", "La severidad habla de la gravedad del daño, distinta de la incidencia."),
        ("abc", "En Forestal: ¿qué es un umbral en el monitoreo?", "Un valor a partir del cual se debe decidir o informar", "El precio máximo de un producto", "El número de plantas de un lote", "El umbral marca cuándo se activa una decisión."),
        ("=", "{F} ¿Cuál es la incidencia del sector 1?", "30*100//500", "Se divide las plantas con síntomas entre las revisadas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es la incidencia del sector 2?", "27*100//150", "Se divide las plantas con síntomas entre las revisadas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es la incidencia del sector 3?", "25*100//250", "Se divide las plantas con síntomas entre las revisadas y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué sector supera el umbral del plan?", "El sector 2, con 18 %", "El sector 1, con 6 %", "El sector 3, con 10 %", "Solo el sector 2 supera el 12 % del plan."),
        ("=", "{F} ¿Cuántas plantas con síntomas hay en total en los tres sectores?", "30+27+25", "Se suman las plantas con síntomas de cada sector.", " plantas"),
        ("=", "{F} ¿Cuántas plantas se revisaron en total en los tres sectores?", "500+150+250", "Se suman las plantas revisadas de cada sector.", " plantas"),
        ("abc", "{F} ¿Qué corresponde hacer en el sector 2?", "Informar de inmediato al profesional responsable con el registro, la fecha y el sector", "Aplicar un producto por cuenta propia ese mismo día", "Esperar al próximo mes para ver si cambia", "Superar el umbral exige informar; la decisión la toma el profesional responsable."),
        ("abc", "{F} Un compañero dice que el sector 1 está peor que el 3 porque tiene más plantas con síntomas, 30 frente a 25. ¿Qué respuesta es correcta?", "Es falso: la incidencia del sector 1 es 6 % y la del 3 es 10 %", "Es cierto: más plantas con síntomas siempre es peor", "Es cierto: el sector 1 tiene más plantas revisadas", "Se compara la incidencia y no la cantidad, porque los sectores tienen tamaños distintos."),
        ("=", "{F} Si el sector 2 tuviera 600 plantas en total y se mantuviera su incidencia, ¿cuántas plantas con síntomas se esperarían?", "600*18//100", "Se calcula el 18 % de las 600 plantas.", " plantas"),
        ("abc", "{F} Antes de ejecutar cualquier medida que decida el profesional, ¿qué debe verificarse?", "Que la medida esté en el plan, que el producto esté autorizado y que la ejecute personal autorizado", "Solo que el producto sea barato", "Solo que se ejecute apenas llegue al vivero", "La medida debe cumplir el plan, la norma y la autorización del personal."),
    ],
    ctx=("abc", "Llegará una visita al vivero y alguien propone anotar una incidencia menor en el sector 2 para «no alarmar». ¿Qué corresponde?", "Anotar el dato real e informar al profesional responsable, y avisar a un adulto responsable si hay presión", "Bajar el dato para que no se note", "No anotar nada ese día", "Un registro alterado impide decidir con datos y puede aumentar el daño."),
    sc=[
        ("En Forestal: ¿cómo se comparan dos sectores de distinto tamaño?", "Por su incidencia, es decir, por el porcentaje", "Los porcentajes permiten comparar tamaños distintos."),
        ("¿Qué se hace si un sector supera el umbral?", "Se informa de inmediato al profesional responsable", "El profesional responsable decide la medida."),
        ("¿Qué mide la severidad?", "Qué tan grave es el daño en cada planta afectada", "La severidad es un concepto distinto de la incidencia."),
    ],
    op=("Ficha de ejemplo: «Vivero Muestra», sector A: 200 plantas revisadas, 16 con síntomas; sector B: 100 revisadas, 15 con síntomas; sector C: 400 revisadas, 28 con síntomas. Umbral de ejemplo: 10 %. Escribe (a) la incidencia de cada sector, (b) qué sectores superan el umbral, (c) qué haces con el sector que supera el umbral y a quién informas, (d) por qué no basta comparar solo la cantidad de plantas con síntomas.",
        "(a) A: 8 %; B: 15 %; C: 7 %. (b) Solo el sector B. (c) Se informa de inmediato al profesional responsable con registro, fecha y sector; no se actúa por cuenta propia. (d) Porque los sectores tienen tamaños distintos y el porcentaje permite compararlos.",
        ["calcula las tres incidencias", "identifica el sector sobre el umbral", "informa en vez de actuar", "justifica comparar porcentajes"],
        ["hoja con las cuatro respuestas"],
        ["comparar solo cantidades", "decidir la medida por cuenta propia", "calcular mal un porcentaje"],
        "Pregunta: «¿cómo comparas sectores de tamaños distintos?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos sectores con distinta cantidad de plantas revisadas y compara sus incidencias.",
    extend="Explica con un ejemplo por qué una misma cantidad de plantas con síntomas puede ser grave en un sector y poco grave en otro.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (costos de ejemplo, inventados). Lote L-50: 2.000 plantas, valor de $300 cada una. Incidencia estimada de la enfermedad: 15 %. Sin ninguna medida, se pierden todas las plantas afectadas. "
     "Medida curativa decidida por el profesional responsable: costo de $40.000 y se estima que salva 200 de las plantas afectadas. "
     "Medida preventiva, de haberse aplicado antes: costo de $15.000 y la incidencia habría sido de 5 %.")
build(
    O5, 4, F,
    use="Aprenderé a comparar en papel la pérdida económica con y sin medida de control, y a recordar que el costo no es el único criterio: también cuentan las personas y el ambiente.",
    prior=["Sé calcular la incidencia.", "Sé calcular porcentajes simples.", "Sé multiplicar y sumar números enteros."],
    explain=[
        "La pérdida económica es el valor de las plantas que se pierden. Se calcula multiplicando las plantas perdidas por el valor de cada una. Para decidir si una medida conviene se hace un análisis costo-beneficio: se compara lo que cuesta la medida con lo que permite evitar perder. Por ejemplo, si una medida cuesta $10.000 y evita perder $25.000, conviene en lo económico; si evitara perder solo $6.000, no.",
        "Una buena comparación suma, para cada alternativa, el costo de la medida y la pérdida que queda, y elige la de menor total. Además de lo económico siempre se revisan el riesgo para las personas y el ambiente y el cumplimiento de la norma. Una medida más barata que expone a las personas o daña el ambiente puede ser inaceptable. La decisión es del profesional responsable.",
        f"Todos los valores son de ejemplo y los cálculos son de planificación. {EMER} {AVISO}",
    ],
    vocab=[("pérdida económica", "valor de las plantas que se pierden"), ("costo-beneficio", "comparación entre lo que cuesta una medida y lo que permite evitar perder"), ("valor por planta", "precio de ejemplo de cada planta"), ("costo total de una alternativa", "costo de la medida más la pérdida que queda")],
    worked=[
        ("Pérdida económica", "En un lote de ejemplo se pierden 50 plantas de $200 cada una. ¿Cuál es la pérdida?", ["Se multiplican las plantas perdidas por su valor.", "50 × 200 = 10.000."], "$10.000"),
        ("Costo total", "Una medida de ejemplo cuesta $5.000 y deja una pérdida de $7.000. ¿Cuál es el costo total de esa alternativa?", ["Se suman el costo de la medida y la pérdida que queda.", "5.000 + 7.000 = 12.000."], "$12.000"),
    ],
    mistakes=[("Elegir siempre la medida más barata sin sumar la pérdida que queda.", "Una medida barata puede dejar una pérdida grande.", "Compara costo total, que suma medida y pérdida."),
              ("Usar solo el criterio económico para decidir.", "También cuentan las personas, el ambiente y la norma.", "Revisa riesgo para las personas y ambiente antes de decidir.")],
    T=[
        ("abc", "En Forestal: ¿qué es la pérdida económica por una enfermedad?", "El valor de las plantas que se pierden", "El costo del producto que se compra", "La ganancia de la venta de las plantas sanas", "La pérdida económica mide lo que se deja de ganar por plantas perdidas."),
        ("abc", "En Forestal: ¿qué es el análisis costo-beneficio de una medida?", "Comparar lo que cuesta la medida con lo que permite evitar perder", "Sumar los precios de todos los productos", "Elegir siempre la medida más barata", "Se compara costo con lo evitado; el precio más bajo no decide solo."),
        ("abc", "En Forestal: ¿por qué se compara también con no hacer ninguna medida?", "Para saber si la medida realmente mejora el resultado", "Para evitar registrar la decisión", "Porque no hacer nada siempre es lo mejor", "El caso sin medida sirve de referencia para ver si la medida mejora."),
        ("=", "{F} ¿Cuántas plantas afectadas se estiman en el lote?", "2000*15//100", "Se calcula el 15 % de las 2.000 plantas.", " plantas"),
        ("=", "{F} ¿Cuál es la pérdida económica si no se toma ninguna medida?", "(2000*15//100)*300", "Se multiplican las plantas afectadas por el valor de cada una.", " pesos"),
        ("=", "{F} ¿Cuántos pesos vale lo que salva la medida curativa?", "200*300", "Se multiplican las plantas salvadas por su valor.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total con la medida curativa, sumando su costo y la pérdida que queda?", "40000+(2000*15//100-200)*300", "Se suma el costo de la medida con el valor de las plantas afectadas que no se salvan.", " pesos"),
        ("abc", "{F} Comparando con no hacer nada, ¿conviene la medida curativa en lo económico?", "Sí, porque su costo total es menor que la pérdida sin medida", "No, porque la medida cuesta $40.000", "Da lo mismo, porque la pérdida es igual", "El total con la medida es 70.000 y la pérdida sin medida es 90.000."),
        ("=", "{F} ¿Cuál habría sido el costo total con la medida preventiva, sumando su costo y la pérdida que queda?", "15000+(2000*5//100)*300", "Se suma el costo de la medida con el valor de las plantas afectadas con incidencia de 5 %.", " pesos"),
        ("abc", "{F} Comparando las tres alternativas, ¿qué conclusión es correcta?", "La preventiva habría salido más barata, pero solo sirve si se aplica antes de que aparezca el problema", "La curativa siempre es mejor que la preventiva", "No hacer nada es lo más barato", "Los totales son 45.000, 70.000 y 90.000, pero la preventiva ya no es posible si el problema existe."),
        ("abc", "{F} Si la medida curativa salvara solo 100 plantas, ¿qué conclusión es correcta?", "No convendría: su costo total sería 100.000, más que los 90.000 sin medida", "Convendría igual, porque salva algunas plantas", "Daría exactamente lo mismo que sin medida", "Con 100 plantas salvadas quedan 200 perdidas: 40.000 + 60.000 = 100.000."),
        ("=", "{F} ¿Cuántos pesos se ahorran con la medida curativa frente a no hacer nada?", "(2000*15//100)*300-(40000+(2000*15//100-200)*300)", "Se resta el costo total con la medida a la pérdida sin medida.", " pesos"),
        ("abc", "{F} Además del costo, ¿qué otro criterio debe revisarse antes de elegir una medida?", "El riesgo para las personas y el ambiente y el cumplimiento de la norma", "Solo el color del envase del producto", "Nada más, porque el costo decide", "Una medida barata pero peligrosa o ilegal no es aceptable."),
    ],
    ctx=("abc", "Un proveedor te ofrece un producto «milagroso» barato, sin registro ni etiqueta, y dice que lo aplicarás en el vivero. ¿Qué respondes?", "Que no, porque sin registro ni etiqueta no es aceptable, y que lo consultarás con un adulto responsable", "Que sí, si es más barato que los demás", "Que sí, si lo prueban primero en pocas plantas", "Lo económico no basta: un producto sin registro ni etiqueta no cumple la norma ni da información."),
    sc=[
        ("En Forestal: ¿cómo se calcula la pérdida económica?", "Plantas perdidas por su valor", "La pérdida es el valor de lo que se pierde."),
        ("¿Qué suma el costo total de una alternativa?", "El costo de la medida y la pérdida que queda", "El costo total incluye lo gastado y lo perdido."),
        ("¿Qué más se revisa además del costo?", "El riesgo para personas y ambiente y la norma", "El costo no es el único criterio."),
    ],
    op=("Ficha de ejemplo (datos de ejemplo): lote L-70 de 1.000 plantas, $400 cada una; incidencia estimada 20 %. Sin medida se pierden las plantas afectadas. Medida curativa: costo de $30.000 y salva 120 plantas afectadas. Escribe (a) las plantas afectadas y la pérdida sin medida, (b) el costo total con la medida curativa, (c) si conviene y cuánto se ahorra, (d) qué otros criterios revisarías antes de decidir.",
        "(a) 1.000 × 20 ÷ 100 = 200 plantas; 200 × 400 = 80.000 pesos. (b) 30.000 + (200 − 120) × 400 = 30.000 + 32.000 = 62.000 pesos. (c) Sí conviene: se ahorran 18.000 pesos. (d) El riesgo para las personas, el efecto en el ambiente y el cumplimiento de la norma; la decisión es del profesional responsable.",
        ["calcula las plantas afectadas y la pérdida", "calcula el costo total", "interpreta el ahorro", "nombra criterios no económicos"],
        ["hoja con las cuatro respuestas"],
        ["olvidar las plantas que no se salvan", "considerar solo el costo de la medida", "no revisar criterios no económicos"],
        "Pregunta: «¿qué pérdida queda aun con la medida?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un lote con valor por planta y calcula su pérdida si se afecta el 10 % de las plantas.",
    extend="Explica con un ejemplo por qué una medida más barata no es siempre la mejor.",
)

# ============================================================ OAE-05, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas; los puntajes son de ejemplo, de 1 a 3, donde 3 es lo más favorable). Se comparan tres tipos de método de control. "
     "Método químico: efectividad 3; riesgo para las personas 1; efecto ambiental 1; costo 2. Método orgánico: efectividad 2; riesgo para las personas 2; efecto ambiental 2; costo 2. "
     "Método biológico: efectividad 2; riesgo para las personas 3; efecto ambiental 3; costo 1. "
     "Registro de aplicaciones del sector 2, con 5 datos obligatorios (fecha, sector, producto autorizado, responsable autorizado, residuos gestionados): tiene 4 de los 5 datos; falta «residuos gestionados».")
build(
    O5, 5, F,
    use="Aprenderé a comparar métodos de control con varios criterios y a verificar la calidad de un registro de aplicaciones, sin aprender a usar productos.",
    prior=["Sé qué son los métodos químicos, orgánicos y biológicos.", "Sé sumar y calcular porcentajes simples.", "Sé qué es un registro."],
    explain=[
        "Comparar métodos de control no es elegir el «más fuerte». Se usan criterios: la efectividad, el riesgo para las personas, el efecto en el ambiente y el costo. Para compararlos se puede asignar un puntaje a cada criterio y sumarlos, pero el resultado depende de qué criterios se incluyen y de cuánto pesa cada uno. Si un criterio es más importante, como el riesgo para las personas, puede contar doble. Los puntajes de esta clase son de ejemplo y no describen productos reales.",
        "La jerarquía de controles también se aplica aquí: antes de usar un producto peligroso se prefiere prevenir, sustituir por algo menos peligroso o usar un método de menor riesgo. La calidad del trabajo se verifica con el registro de aplicaciones, que debe tener todos sus datos obligatorios y estar firmado por un responsable. Si falta un dato, se completa con información verificada, nunca con datos supuestos, y el registro no se archiva como terminado.",
        f"La elección final la hace el profesional responsable con la norma vigente; la ejecución, personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("criterio", "regla o aspecto que se usa para comparar alternativas"), ("ponderación", "peso que se da a un criterio, por ejemplo contarlo doble"), ("registro de aplicaciones", "documento donde personal autorizado anota fecha, sector, producto y responsable"), ("dato obligatorio", "dato que no puede faltar en un registro"), ("método de menor riesgo", "método que expone menos a las personas y al ambiente")],
    worked=[
        ("Sumar puntajes", "Una alternativa de ejemplo tiene puntajes 3, 2, 2 y 1. ¿Cuál es su puntaje total?", ["Se suman todos los puntajes.", "3 + 2 + 2 + 1 = 8."], "8 puntos"),
        ("Ponderar un criterio", "Si el segundo criterio cuenta doble, ¿cuál es el total de esa alternativa?", ["El segundo puntaje, 2, cuenta dos veces: 4.", "3 + 4 + 2 + 1 = 10."], "10 puntos"),
    ],
    mistakes=[("Elegir el método solo por su efectividad.", "También cuentan el riesgo para las personas, el ambiente y el costo.", "Compara con todos los criterios del plan."),
              ("Completar un dato faltante de un registro con lo que «seguramente» ocurrió.", "Un dato supuesto falsea el registro.", "Se completa con información verificada por el responsable.")],
    T=[
        ("abc", "En Forestal: ¿qué es un método de menor riesgo para controlar una enfermedad?", "Uno que expone menos a las personas y al ambiente", "Uno que cuesta menos pesos por planta", "Uno que se usa menos veces al año", "El riesgo se refiere a la exposición de personas y ambiente, no al precio ni a la frecuencia."),
        ("abc", "En Forestal: ¿qué es la ponderación de un criterio?", "El peso que se le da a un criterio, por ejemplo, contarlo doble", "El precio de un producto de control", "El número de plantas que se revisan", "La ponderación indica qué tan importante es un criterio."),
        ("abc", "En Forestal: ¿por qué un método de control no se elige solo por su efectividad?", "Porque también cuentan el riesgo para las personas, el ambiente y el costo", "Porque la efectividad no se puede medir", "Porque todos los métodos son igualmente efectivos", "Un método efectivo pero muy riesgoso o dañino puede ser inaceptable."),
        ("=", "{F} ¿Cuál es el puntaje total del método químico?", "3+1+1+2", "Se suman los puntajes de los cuatro criterios.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total del método orgánico?", "2+2+2+2", "Se suman los puntajes de los cuatro criterios.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total del método biológico?", "2+3+3+1", "Se suman los puntajes de los cuatro criterios.", " puntos"),
        ("abc", "{F} Según el total simple de puntos, ¿qué método obtiene el mayor puntaje?", "El biológico", "El químico, porque es el más efectivo", "El orgánico", "El biológico suma 9, el orgánico 8 y el químico 7."),
        ("abc", "{F} ¿Qué desventaja tiene el método químico en esta ficha?", "Mayor riesgo para las personas y mayor efecto ambiental, con puntajes de 1", "Menor efectividad que los otros métodos", "Mayor costo que todos los otros métodos", "En la ficha, el químico tiene los puntajes más bajos en riesgo y ambiente."),
        ("=", "{F} Si el riesgo para las personas cuenta doble, ¿cuál es el puntaje total del método orgánico?", "2+2*2+2+2", "Se duplica el puntaje del riesgo para las personas y se suman los demás.", " puntos"),
        ("abc", "{F} ¿Qué conclusión corresponde sobre cómo se elige el método?", "Depende de los criterios y su ponderación, y lo decide el profesional responsable", "Siempre se elige el biológico", "Siempre se elige el químico, por ser el más efectivo", "El resultado cambia con los criterios y su peso; no hay una regla fija."),
        ("=", "{F} ¿Qué porcentaje de los datos obligatorios tiene el registro del sector 2?", "4*100//5", "Se divide los datos presentes entre los obligatorios y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué corresponde hacer con el registro que no tiene «residuos gestionados»?", "Completarlo con información verificada por el responsable antes de archivarlo", "Archivarlo así porque tiene 80 % de los datos", "Completar el dato con lo que seguramente ocurrió", "Un registro incompleto no se da por terminado; se completa con datos verificados."),
        ("abc", "{F} La empresa prefiere el producto de mayor efectividad aunque tenga un riesgo alto. ¿Qué debería intentarse primero según la jerarquía de controles?", "Buscar una alternativa menos peligrosa o prevenir para no necesitar el producto", "Entregar un EPP más caro", "Aumentar las horas de exposición del personal", "La jerarquía prefiere eliminar o sustituir antes de depender del EPP."),
    ],
    ctx=("abc", "Un vendedor te presiona a recomendar su producto a un vivero amigo porque «es el más efectivo». No conoces su riesgo ni su registro. ¿Qué haces?", "No recomendarlo y sugerir consultar al profesional responsable, porque falta información sobre riesgo y registro", "Recomendarlo si el vendedor te regala una muestra", "Recomendarlo porque es el más efectivo", "Sin información sobre riesgo y registro no se puede recomendar ningún producto, y los regalos no cambian eso."),
    sc=[
        ("En Forestal: ¿qué criterios se usan para comparar métodos de control?", "Efectividad, riesgo para las personas, efecto ambiental y costo", "Se comparan varios criterios, no solo la efectividad."),
        ("¿Qué se hace con un registro con datos faltantes?", "Se completa con información verificada antes de archivarlo", "Un dato supuesto falsea el registro."),
        ("¿Qué prefiere la jerarquía de controles frente a un producto peligroso?", "Prevenir, eliminar o sustituir antes que depender del EPP", "El EPP es la última barrera."),
    ],
    op=("Ficha de ejemplo (puntajes de 1 a 3, donde 3 es lo más favorable): método X: efectividad 3, riesgo para las personas 1, efecto ambiental 2, costo 3; método Y: efectividad 2, riesgo para las personas 3, efecto ambiental 3, costo 2. Registro de ejemplo con 5 datos obligatorios, de los cuales 4 están presentes. Escribe (a) el puntaje total de X y de Y, (b) los totales si el riesgo para las personas cuenta doble y cuál gana, (c) qué porcentaje de datos del registro está presente, (d) qué haces con el registro incompleto.",
        "(a) X: 3 + 1 + 2 + 3 = 9; Y: 2 + 3 + 3 + 2 = 10. (b) X: 3 + 2 + 2 + 3 = 10; Y: 2 + 6 + 3 + 2 = 13; gana Y. (c) 4 ÷ 5 = 80 %. (d) Se completa el dato faltante con información verificada por el responsable y recién después se archiva.",
        ["suma bien los puntajes", "aplica la ponderación", "interpreta el registro incompleto", "no inventa datos"],
        ["hoja con las cuatro respuestas"],
        ["sumar sin duplicar el criterio ponderado", "archivar un registro incompleto", "completar datos supuestos"],
        "Pregunta: «¿qué criterio cuenta doble?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos alternativas con cuatro puntajes cada una y súmalas.",
    extend="Explica con un ejemplo por qué el resultado de una comparación con puntajes depende de qué criterios se incluyen.",
)
