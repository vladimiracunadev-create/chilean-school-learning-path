"""Agropecuaria TP 3.º medio: OAE-03 (reproducción vegetal), OAE-04 (alimentación y pesaje pecuarios) y OAE-05 (residuos), 4 clases cada una. Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_agro_common import AVISO, EMER, build

O3 = "TP-AGRO-3-OAE-03"
O4 = "TP-AGRO-3-OAE-04"
O5 = "TP-AGRO-3-OAE-05"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Vivero Demo» es un establecimiento ficticio que produce plantas hortícolas y frutales para vender. Reproduce unas especies por semilla y otras por estacas (trozos de tallo que forman raíces). "
     "Peligros anotados: tijeras y cuchillos de injertar muy afilados, un invernadero con calor en verano, sustratos que levantan polvo, bandejas llenas que pesan 10 kg cada una (dato de ejemplo) y un desinfectante guardado en una repisa baja.")
build(
    O3, 1, F,
    use="Aprenderé qué es reproducir una planta, cuál es la diferencia entre reproducción sexual y asexual, qué exige la norma sanitaria y qué peligros tiene un vivero.",
    prior=["Sé que las plantas nacen de semillas o de partes de otras plantas.", "Sé qué es un peligro y un riesgo.", "Sé dividir números enteros."],
    explain=[
        "Reproducir una planta es obtener plantas nuevas. La reproducción sexual usa semillas. La reproducción asexual, o vegetativa, usa partes de una planta madre: una estaca es un trozo de tallo que forma raíces, y un injerto une una yema de una planta con otra planta que tiene raíces, llamada portainjerto. Las plantas hechas por estaca o injerto son copias de la planta madre; las que nacen de semilla pueden ser algo distintas entre sí.",
        "La norma sanitaria vigente cuida que el material vegetal no lleve plagas: las semillas y plantas que se venden deben cumplir los controles que fija la autoridad sanitaria agrícola, y el material no se traslada sin autorización. Un vivero tiene peligros como herramientas cortantes, calor, polvo, cargas pesadas y productos guardados. La jerarquía de controles ordena las medidas: eliminar, sustituir, cambiar el lugar, dar reglas y, al final, usar equipo de protección personal (EPP).",
        f"Guardar el desinfectante en un lugar cerrado y alto es un control de ingeniería; una regla que prohíbe usar cuchillos sin autorización es administrativa. Las tareas con herramientas cortantes las hace personal capacitado. {EMER} {AVISO}",
    ],
    vocab=[("reproducción sexual", "obtención de plantas nuevas a partir de semillas"), ("reproducción asexual", "obtención de plantas nuevas a partir de partes de una planta madre"), ("estaca", "trozo de tallo que forma raíces y da una planta nueva"), ("injerto", "unión de una yema de una planta con otra planta que tiene raíces"), ("portainjerto", "planta con raíces sobre la que se hace el injerto"), ("planta madre", "planta de la que se toma el material para reproducir"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Reproducción sexual o asexual", "En un vivero de ejemplo se obtienen plantas nuevas a partir de trozos de tallo de una planta madre. ¿Es reproducción sexual o asexual?", ["No se usan semillas.", "Se usan partes de la planta madre, o sea, es reproducción asexual."], "Asexual"),
        ("Clasificar un control", "En un vivero de ejemplo se instala un piso antideslizante en la sala donde se preparan los sustratos. ¿Qué tipo de control es?", ["El piso cambia físicamente el lugar de trabajo.", "Cambiar el lugar es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que una planta nacida de estaca es distinta de su planta madre.", "La estaca es una parte de la planta madre, por eso es su copia.", "Las estacas e injertos copian a la planta madre; las semillas pueden variar."),
              ("Creer que leer sobre injertos habilita para usar un cuchillo de injertar.", "Las herramientas cortantes exigen formación y autorización.", "Aprende aquí el concepto y deja el corte a personal capacitado.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la reproducción sexual de una planta?", "Obtener plantas nuevas a partir de semillas", "Obtener plantas nuevas a partir de trozos de tallo", "Mover plantas de un vivero a otro", "La sexual usa semillas; los trozos de tallo son reproducción asexual."),
        ("abc", "En Agropecuaria: ¿qué es una estaca?", "Un trozo de tallo que forma raíces y da una planta nueva", "Una semilla envuelta en una cáscara dura", "Una planta con raíces sobre la que se hace un injerto", "La estaca es un trozo de tallo; la planta con raíces del injerto es el portainjerto."),
        ("abc", "En Agropecuaria: ¿qué es un portainjerto?", "La planta con raíces sobre la que se hace el injerto", "La yema que se une a otra planta", "El trozo de tallo que forma raíces solo", "El portainjerto aporta las raíces; la yema es lo que se injerta."),
        ("=", "{F} Un carro de ejemplo admite como máximo 60 kg de carga. ¿Cuántas bandejas llenas, de las que indica la ficha, admite como máximo?", "60//10", "Se divide la carga máxima del carro entre el peso de cada bandeja.", " bandejas"),
        ("abc", "{F} Guardar el desinfectante en una repisa alta con puerta y llave es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla escrita", "De EPP, porque protege al personal", "La repisa cerrada cambia el lugar y no depende de que alguien lo recuerde."),
        ("abc", "{F} Una regla que dice «los cuchillos de injertar solo los usa personal autorizado» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el cuchillo", "De sustitución, porque cambia la herramienta", "Una regla escrita es administrativa; no cambia la herramienta."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a las tijeras y cuchillos muy afilados?", "Que una persona sufra un corte al usarlos", "Que las herramientas estén afiladas", "Que falte espacio en el invernadero", "El riesgo es la posibilidad de daño; el filo es el peligro."),
        ("abc", "{F} Un estudiante dice: «ya entendí cómo se injerta, así que puedo hacerlo con el cuchillo del vivero». ¿Qué respuesta es correcta?", "Es falso: usar herramientas cortantes exige formación, autorización y norma vigente", "Es cierto, si lleva guantes", "Es cierto, si va despacio", "Conocer el concepto no habilita para el corte; guantes o lentitud tampoco bastan."),
        ("abc", "{F} En una visita, una persona se corta con una herramienta y sangra mucho. ¿Qué corresponde según las reglas generales?", "No manipular la herramienta ni la herida, avisar a un adulto responsable y a emergencias", "Quitar la herramienta con las manos", "Esperar a que deje de sangrar sola", "Se avisa a quienes pueden prestar ayuda; manipular sin formación puede empeorar la lesión."),
        ("abc", "En Agropecuaria: ¿por qué las plantas por estaca son copias de la planta madre?", "Porque son una parte de ella y tienen su misma información", "Porque se riegan igual que la planta madre", "Porque nacen del mismo tipo de semilla", "Una parte de la planta conserva sus características; las semillas mezclan información."),
        ("abc", "{F} Se propone solo entregar guantes contra los cortes. ¿Qué medida es más efectiva en la jerarquía de controles?", "Que solo personal capacitado use las herramientas y se guarden bajo llave", "Que cada persona tenga un par de guantes de repuesto", "Pedir a todos que trabajen más rápido", "Controlar quién usa las herramientas y dónde se guardan actúa sobre el peligro; el guante es EPP."),
        ("=", "{F} El vivero tiene 12 carros de 6 bandejas llenas cada uno. ¿Cuántos kilos pesan todas esas bandejas?", "12*6*10", "Se calculan las bandejas totales y se multiplican por el peso de cada una.", " kg"),
        ("abc", "En Agropecuaria: ¿por qué el traslado de plantas entre zonas puede necesitar autorización sanitaria?", "Porque el material vegetal podría llevar una plaga a otra zona", "Porque las plantas pesan demasiado", "Porque las plantas no pueden salir del vivero", "La norma sanitaria busca evitar la dispersión de plagas con el material vegetal."),
    ],
    ctx=("abc", "Un vecino te ofrece pagarte por injertar sus frutales «porque ya viste cómo se hace en clases». ¿Qué respondes?", "Que no, porque esa tarea exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, con tijeras pequeñas", "Que sí, solo si son pocos árboles", "Haber visto el concepto no habilita para cortar ni injertar; la cantidad de árboles no cambia eso."),
    sc=[
        ("En Agropecuaria: ¿qué es la reproducción asexual?", "Obtener plantas nuevas a partir de partes de una planta madre", "La reproducción asexual no usa semillas sino partes de la planta madre."),
        ("En el trabajo agrícola: ¿qué institución cuida la sanidad del material vegetal?", "La autoridad sanitaria agrícola", "Esa autoridad fija los controles para evitar la dispersión de plagas."),
        ("En Agropecuaria: ¿qué es un injerto?", "La unión de una yema con una planta que tiene raíces", "El injerto une la yema con el portainjerto."),
    ],
    op=("El «Vivero Demo» anota una tarea de ejemplo: preparar estacas con tijeras de podar en una sala con piso mojado y poca luz. Escribe (a) el peligro del piso mojado y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) por qué la tarea la hace solo personal capacitado.",
        "(a) Peligro: piso mojado; riesgo: que alguien resbale y se lastime con las tijeras en la mano. (b) Una regla de no trabajar con tijeras en el piso mojado y un letrero. (c) Una cubierta antideslizante fija y mejor iluminación. (d) Porque las herramientas cortantes exigen formación, autorización y norma vigente; este cuaderno no habilita para trabajar.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué lo hace personal capacitado"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al piso mojado", "proponer solo guantes", "decir que el cuaderno habilita"],
        "Pregunta: «¿qué control cambia el piso y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el tercer párrafo."),
    reinforce="Escribe una lista con tres plantas de tu entorno y di si crees que se reproducen por semilla, por estaca o por injerto.",
    extend="Explica con un ejemplo por qué una persona podría preferir una planta por estaca antes que una por semilla.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (etiqueta de semilla de ejemplo, inventada). Especie: lechuga. Lote: L-21. Poder germinativo: 90 % (de cada 100 semillas, germinan 90). Pureza: 98 % (de cada 100 gramos, 98 son semilla de la especie). Contenido del envase: 200 gramos. "
     "Plan de producción de ejemplo: obtener 900 plantas. Otros documentos del vivero: el registro de siembra (qué se sembró, cuándo y cuánto) y la etiqueta del lote de plantas.")
build(
    O3, 2, F,
    use="Aprenderé qué son el poder germinativo, la pureza, el almácigo y el trasplante, cómo se lee una etiqueta de semilla y qué rol cumple cada persona en la reproducción de plantas.",
    prior=["Sé qué es la reproducción sexual y asexual.", "Sé calcular porcentajes enteros.", "Sé dividir números enteros."],
    explain=[
        "El poder germinativo es el porcentaje de semillas que germinan, es decir, que dan origen a una plántula. La pureza es el porcentaje del peso de un envase que corresponde a semilla de la especie, sin tierra ni semillas de otras plantas. Ambos datos están en la etiqueta de la semilla, junto con la especie y el lote. Un lote es un grupo de semillas de igual origen y fecha que se maneja junto.",
        "Las semillas suelen germinar en un almácigo, una bandeja o cama donde nacen muchas plántulas juntas; después se pasan a un envase o al suelo en un trabajo llamado trasplante. El plan de producción dice cuántas plantas se necesitan; el registro de siembra anota lo sembrado. El viverista ejecuta las labores, el jefe de producción organiza el plan y el técnico supervisa la calidad y la sanidad.",
        f"Una etiqueta se lee y se respeta tal cual: no se cambia el lote ni el porcentaje para que el producto parezca mejor. {EMER} {AVISO}",
    ],
    vocab=[("poder germinativo", "porcentaje de semillas que germinan"), ("pureza", "porcentaje del peso del envase que es semilla de la especie"), ("lote", "grupo de semillas de igual origen y fecha"), ("plántula", "planta muy joven que acaba de germinar"), ("almácigo", "bandeja o cama donde germinan muchas semillas juntas"), ("trasplante", "paso de una plántula a su envase o lugar definitivo"), ("registro de siembra", "documento que anota qué, cuándo y cuánto se sembró")],
    worked=[
        ("Semillas que germinan", "Un lote de ejemplo tiene poder germinativo de 80 % y se siembran 500 semillas. ¿Cuántas germinan?", ["80 % significa 80 de cada 100.", "500 tiene 5 grupos de 100, y 5 por 80 es 400."], "400 plántulas"),
        ("Semillas necesarias", "Con un poder germinativo de ejemplo de 50 %, ¿cuántas semillas se necesitan para obtener 100 plántulas?", ["Germina la mitad.", "Para 100 plántulas se necesita el doble de semillas."], "200 semillas"),
    ],
    mistakes=[("Creer que si germina 90 % basta sembrar tantas semillas como plantas se necesitan.", "Un 10 % de las semillas no germina.", "Se calcula con el poder germinativo cuántas semillas sembrar."),
              ("Confundir pureza con poder germinativo.", "La pureza habla del peso del envase; el poder germinativo, de las semillas que nacen.", "Lee cada porcentaje con su definición.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el poder germinativo de un lote de semillas?", "El porcentaje de semillas que germinan", "El porcentaje del peso del envase que es semilla pura", "El número de semillas que caben en un envase", "El poder germinativo cuenta semillas que nacen; la pureza se refiere al peso."),
        ("abc", "En Agropecuaria: ¿qué es la pureza de un lote de semillas?", "El porcentaje del peso del envase que es semilla de la especie", "El porcentaje de semillas que germinan", "El tiempo que tardan en germinar", "La pureza mide cuánto del peso es semilla de la especie."),
        ("abc", "En Agropecuaria: ¿qué es un almácigo?", "Una bandeja o cama donde germinan muchas semillas juntas", "El paso de una plántula a su lugar definitivo", "El documento que anota lo sembrado", "El almácigo es el lugar de germinación; el paso a otro lugar es el trasplante."),
        ("=", "{F} Si se siembran 400 semillas del lote, ¿cuántas se espera que germinen?", "400*90//100", "Se calcula el poder germinativo sobre el total sembrado.", " plántulas"),
        ("=", "{F} ¿Cuántos gramos del envase son semilla pura de la especie?", "200*98//100", "Se calcula el porcentaje de pureza sobre el peso del envase.", " gramos"),
        ("abc", "{F} ¿Qué dato de la etiqueta identifica al grupo de semillas que se maneja junto?", "El lote L-21", "La especie lechuga", "El contenido de 200 gramos", "El lote identifica al grupo; la especie y el peso son otros datos."),
        ("abc", "{F} ¿Qué documento anotaría cuántas semillas se sembraron y en qué fecha?", "El registro de siembra", "La etiqueta de la semilla", "El plan de producción", "El registro anota lo realizado; la etiqueta describe la semilla y el plan, lo que se espera producir."),
        ("=", "{F} Según el plan, se necesitan 900 plantas y germina el 90 %. ¿Cuántas semillas hay que sembrar?", "900*100//90", "Se divide el objetivo entre el poder germinativo, expresado como porcentaje.", " semillas"),
        ("abc", "{F} Una compañera dice: «con una pureza de 98 % germinarán 98 de cada 100 semillas». ¿Qué respuesta es correcta?", "Es falso: la pureza no mide la germinación, la mide el poder germinativo", "Es cierto, porque ambos números significan lo mismo", "Es cierto, si las semillas son nuevas", "La pureza se refiere al peso del envase; la germinación es otro dato."),
        ("abc", "{F} El jefe de producción pide cambiar en la etiqueta el 90 % por un 95 % «para que se venda mejor». ¿Qué corresponde?", "Rechazarlo: la etiqueta no se altera y se usa el dato real", "Aceptarlo, porque es solo un número", "Aceptarlo, si el lote es nuevo", "Alterar la etiqueta falsea el documento y perjudica al comprador."),
        ("=", "{F} Se siembran 1.000 semillas de otro lote de lechuga con poder germinativo de 75 %. ¿Cuántas plántulas no germinan?", "1000-1000*75//100", "Se resta del total las plántulas que germinan.", " semillas"),
        ("abc", "{F} Si el poder germinativo fuera 50 % en vez de 90 %, ¿qué pasaría con las semillas que hay que sembrar para el mismo plan?", "Habría que sembrar más semillas", "Habría que sembrar menos semillas", "Habría que sembrar las mismas", "Con menos germinación se necesitan más semillas para obtener las mismas plantas."),
        ("abc", "En Agropecuaria: ¿por qué conviene conocer el poder germinativo antes de sembrar?", "Para calcular cuántas semillas sembrar y evitar quedarse sin plantas", "Para saber cuánto cuesta el envase", "Para elegir el color de la bandeja", "Con ese dato se planifica la siembra para llegar a la cantidad de plantas deseada."),
    ],
    ctx=("abc", "Una conocida te muestra una bolsa de semillas sin etiqueta y te pide que adivines su poder germinativo. ¿Qué respondes?", "Que no se puede saber sin la etiqueta o el análisis del lote, y que conviene consultar a un técnico", "Que seguro es 100 %", "Que seguro es 50 %", "Sin etiqueta o análisis no hay dato verificable; cualquier número sería inventado."),
    sc=[
        ("En Agropecuaria: ¿qué indica el poder germinativo de 80 %?", "Que germinan 80 de cada 100 semillas", "El poder germinativo cuenta cuántas semillas nacen."),
        ("En el trabajo agrícola: ¿qué es un trasplante?", "El paso de una plántula a su envase o lugar definitivo", "El trasplante ocurre después de la germinación."),
        ("En Agropecuaria: ¿quién organiza el plan de producción de un vivero?", "El jefe de producción", "El jefe de producción organiza el plan y los plazos."),
    ],
    op=("Etiqueta de ejemplo: especie tomate; lote T-08; poder germinativo 80 %; pureza 96 %; envase de 100 gramos. Plan de ejemplo: obtener 400 plantas. Escribe (a) cuántas semillas hay que sembrar, (b) cuántos gramos del envase son semilla pura, (c) qué documento anota lo sembrado, (d) qué haces si la etiqueta se ve borrosa.",
        "(a) 400 × 100 ÷ 80 = 500 semillas. (b) 100 × 96 ÷ 100 = 96 gramos. (c) El registro de siembra. (d) No invento el dato: lo informo al jefe de producción o al técnico para obtener el dato real.",
        ["calcula las semillas", "calcula los gramos de semilla pura", "nombra el documento", "no inventa el dato borroso"],
        ["hoja con las cuatro respuestas"],
        ["dividir por 100 en vez de por 80", "confundir pureza con germinación", "inventar el dato borroso"],
        "Pregunta: «¿por qué se siembran más semillas que plantas?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula cuántas semillas germinan si siembras 600 con un poder germinativo de ejemplo de 70 %.",
    extend="Explica con un ejemplo por qué la etiqueta de un lote de semillas es un documento importante para quien compra.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). El «Vivero Demo» debe elegir cómo reproducir dos especies. Especie 1: una hortaliza de ciclo corto que se vende por cantidad; no importa que cada planta sea algo distinta y la semilla es barata y fácil de conseguir. "
     "Especie 2: un frutal de una variedad valiosa cuyas semillas no dan plantas iguales a la madre; sus estacas no forman raíces con facilidad. Se necesita que todas las plantas den la misma fruta que la planta madre. "
     "Métodos (conceptos): semilla (barata, plantas algo distintas entre sí), estaca (copia de la madre, solo si la especie forma raíces) e injerto (copia la variedad sobre un portainjerto; lo hace personal capacitado).")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso de reproducción de plantas y a elegir, con evidencias, entre semilla, estaca e injerto según las características de la especie y el plan de producción.",
    prior=["Sé qué son la reproducción sexual y asexual.", "Sé qué es una estaca y un injerto.", "Sé leer una ficha con datos."],
    explain=[
        "El método de reproducción se elige según la especie y el plan de producción. La semilla es barata y rápida, pero las plantas pueden ser algo distintas entre sí; sirve cuando la uniformidad no es esencial. La estaca copia a la planta madre, pero solo funciona si la especie forma raíces con facilidad. El injerto también copia la variedad, aprovechando las raíces de un portainjerto, y se usa cuando ni la semilla ni la estaca sirven.",
        "Para analizar un caso se leen primero las condiciones de cada especie: qué se quiere lograr, qué permite la especie y qué cuesta. Luego se descarta con evidencia: si las semillas de una especie no dan plantas iguales a la madre, la semilla no cumple; si sus estacas no enraízan, la estaca tampoco. Lo que queda es el método posible. La decisión final la toma el técnico del vivero.",
        f"Un buen análisis nombra el método elegido, cita dos evidencias y dice qué cambiaría si una condición cambiara. El injerto exige herramientas cortantes: solo lo hace personal capacitado. {EMER} {AVISO}",
    ],
    vocab=[("uniformidad", "que todas las plantas sean parecidas entre sí"), ("enraizar", "formar raíces un trozo de planta"), ("variedad", "grupo de plantas de una especie con características propias"), ("método", "forma de hacer un trabajo"), ("evidencia", "dato del caso que respalda una decisión"), ("plan de producción", "documento que dice cuántas plantas y cuándo se necesitan")],
    worked=[
        ("Elegir con una condición", "Una especie de ejemplo enraíza muy bien en estaca y se quiere copiar a la planta madre. ¿Qué método sirve?", ["Se quiere una copia de la madre.", "La especie enraíza, así que la estaca sirve."], "Estaca"),
        ("Descartar con evidencia", "Una especie de ejemplo no enraíza en estaca y sus semillas no dan plantas iguales a la madre. ¿Qué método queda?", ["La semilla no da copias.", "La estaca no enraíza."], "Injerto"),
    ],
    mistakes=[("Elegir la semilla solo porque es la más barata.", "Si se necesita uniformidad, la semilla puede no cumplir.", "Se revisa si el método cumple lo que pide el plan antes de mirar el costo."),
              ("Dar una conclusión sin citar evidencia del caso.", "Sin dato del caso la decisión no se puede verificar.", "Cita dos evidencias, como el objetivo y lo que permite la especie.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué significa que una planta enraíce?", "Que un trozo de planta forma raíces", "Que la planta pierde sus hojas", "Que la planta se marchita por falta de agua", "Enraizar es formar raíces; lo demás son otros procesos."),
        ("abc", "En Agropecuaria: ¿qué es la uniformidad de un lote de plantas?", "Que todas las plantas sean parecidas entre sí", "Que todas las plantas midan exactamente cero", "Que todas las plantas tengan el mismo precio", "La uniformidad es parecido entre plantas; precio y medida exacta no la definen."),
        ("abc", "En Agropecuaria: ¿qué es una variedad de una especie?", "Un grupo de plantas con características propias dentro de la especie", "Un conjunto de especies distintas", "El lugar donde se cultiva la especie", "La variedad es un grupo dentro de la especie."),
        ("abc", "{F} ¿Qué método conviene a la Especie 1?", "Semilla, porque es barata y la uniformidad no es esencial", "Injerto, porque exige copiar la variedad", "Estaca, porque no enraíza", "La Especie 1 no exige uniformidad y la semilla cuesta poco."),
        ("abc", "{F} ¿Qué evidencia descarta la semilla para la Especie 2?", "Sus semillas no dan plantas iguales a la madre", "La semilla es barata", "La especie es una hortaliza de ciclo corto", "Para copiar la variedad la semilla no sirve porque no reproduce a la madre."),
        ("abc", "{F} ¿Qué evidencia descarta la estaca para la Especie 2?", "Sus estacas no forman raíces con facilidad", "Se vende por cantidad", "La variedad es de ciclo corto", "Si la estaca no enraíza, no da plantas nuevas."),
        ("abc", "{F} ¿Qué método conviene a la Especie 2?", "Injerto, porque copia la variedad sobre un portainjerto", "Semilla, porque es barata", "Estaca, porque enraíza fácil", "Las otras dos opciones están descartadas por la ficha."),
        ("abc", "{F} Una estudiante dice: «ya sé qué método sirve, así que haré yo los injertos en el vivero». ¿Qué respuesta es correcta?", "Es falso: el injerto lo hace personal capacitado y autorizado", "Es cierto, si usa guantes", "Es cierto, si hace pocos", "El análisis en papel no habilita para usar herramientas cortantes."),
        ("=", "{F} Se injertan 150 plantas y prenden 120. ¿Qué porcentaje prendió?", "120*100//150", "Se divide lo que prendió entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} Si de pronto las estacas de la Especie 2 enraizaran muy bien, ¿qué método adicional podría analizarse?", "La estaca, porque también copia a la planta madre", "La semilla, porque ahora copia a la madre", "Ninguno, porque el injerto es el único posible", "Si enraíza bien, la estaca cumple el objetivo de copiar la variedad."),
        ("abc", "{F} Un viverista detecta en un lote de injertos una planta con señales de plaga. ¿Qué corresponde?", "Avisar al técnico del vivero, que decide las medidas sanitarias, sin mover el material", "Llevar el material a otro vivero", "Mezclar la planta con las demás", "Mover material con plaga puede dispersarla; la norma sanitaria exige avisar."),
        ("=", "{F} Se necesitan 360 injertos y la experiencia de ejemplo dice que prenden 80 de cada 100. ¿Cuántos injertos hay que hacer?", "360*100//80", "Se divide lo que se necesita entre el porcentaje que prende.", " injertos"),
        ("abc", "En Agropecuaria: ¿por qué un injerto copia la variedad de la planta de la que viene la yema?", "Porque la yema conserva las características de su planta de origen", "Porque el portainjerto decide la fruta", "Porque el injerto es una semilla", "La yema aporta las características de la variedad; el portainjerto aporta las raíces."),
    ],
    ctx=("abc", "Un conocido te muestra un árbol frutal muy bueno y te pide que le «hagas copias» sacando semillas de la fruta. ¿Qué le explicas?", "Que las semillas pueden dar plantas distintas, y que para copiar se usan estacas o injertos con un técnico", "Que las semillas siempre copian al árbol", "Que no se puede reproducir un frutal", "Las semillas mezclan información; copiar una variedad requiere métodos asexuales."),
    sc=[
        ("En Agropecuaria: ¿qué método copia a la planta madre aprovechando las raíces de otra?", "El injerto", "El injerto une la yema con las raíces del portainjerto."),
        ("En el trabajo agrícola: ¿qué ventaja tiene la semilla?", "Es barata y fácil de conseguir", "La semilla es económica, aunque las plantas pueden variar."),
        ("En Agropecuaria: ¿cuántas evidencias debe citar una decisión técnica en esta clase?", "Al menos dos", "Dos evidencias permiten verificar la decisión."),
    ],
    op=("Caso de ejemplo del «Vivero Demo»: la Especie 3 es una planta ornamental fácil de enraizar en estaca; se quiere que las plantas sean iguales entre sí y se venden por unidad. La Especie 4 es una hortaliza barata de semilla que se vende por cantidad y no necesita uniformidad. Escribe (a) el método para la Especie 3 y una evidencia, (b) el método para la Especie 4 y una evidencia, (c) cuál método exige herramientas cortantes y quién lo hace, (d) qué cambiaría si la Especie 3 no enraizara.",
        "(a) Estaca, porque se quiere uniformidad y enraíza fácil. (b) Semilla, porque es barata y no se necesita uniformidad. (c) La estaca y el injerto usan herramientas cortantes; las hace personal capacitado. (d) Habría que analizar el injerto con el técnico.",
        ["elige bien el método de la especie 3 con evidencia", "elige bien el método de la especie 4 con evidencia", "indica que lo hace personal capacitado", "dice qué cambiaría"],
        ["hoja con las cuatro respuestas"],
        ["elegir sin citar evidencia", "decidir hacer el corte por cuenta propia"],
        "Pregunta: «¿qué dice la ficha sobre la uniformidad y sobre el enraizamiento?». Si no responde, pídele que relea la segunda parte de la explicación."),
    reinforce="Escribe para dos plantas inventadas qué método de reproducción elegirías y una evidencia para cada una.",
    extend="Explica con un ejemplo por qué la semilla puede dar plantas algo distintas entre sí.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Pedido: 2.700 plantas de una hortaliza. Poder germinativo de las semillas: 80 %. Pérdida al trasplantar: se pierde 10 % de las plántulas (llegan a planta 90 de cada 100). "
     "Bandejas de almácigo de 250 cavidades (una semilla por cavidad). Precio de ejemplo: $5 por semilla.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular cuántas semillas y bandejas se necesitan para un pedido, considerando la germinación y las pérdidas.",
    prior=["Sé qué es el poder germinativo.", "Sé multiplicar y dividir enteros.", "Sé calcular porcentajes enteros."],
    explain=[
        "Para producir un número de plantas se calcula hacia atrás, desde el pedido hasta las semillas. Primero se cuentan las plantas que deben salir; luego se calcula cuántas plántulas hay que tener antes del trasplante, porque parte se pierde; y por último, cuántas semillas hay que sembrar, porque no todas germinan. Cada paso se calcula dividiendo por el porcentaje de éxito y multiplicando por 100.",
        "Con las semillas se calculan las bandejas: cada cavidad recibe una semilla, y el número de bandejas es el total de semillas dividido entre las cavidades de cada bandeja. Si no sale exacto, se redondea hacia arriba, porque no se puede tener una bandeja a medias. El costo de las semillas es su número por el precio unitario.",
        f"Todas las cifras de esta clase son de ejemplo: las reales dependen de la especie, del lote y del técnico del vivero. {EMER} {AVISO}",
    ],
    vocab=[("pedido", "cantidad de plantas que se debe entregar"), ("pérdida", "plantas que no llegan a la etapa siguiente"), ("cavidad", "hueco de una bandeja donde crece una planta"), ("éxito", "porcentaje que sí germina o sobrevive"), ("precio unitario", "precio de una sola unidad")],
    worked=[
        ("Plántulas necesarias", "Un pedido de ejemplo es de 900 plantas y llega a planta el 75 % de las plántulas. ¿Cuántas plántulas se necesitan?", ["Se divide el pedido por el éxito.", "900 por 100 dividido por 75 es 1.200."], "1.200 plántulas"),
        ("Bandejas", "Se necesitan 1.200 semillas de ejemplo y cada bandeja tiene 100 cavidades. ¿Cuántas bandejas se usan?", ["Se divide el total entre las cavidades.", "1.200 entre 100 es 12."], "12 bandejas"),
    ],
    mistakes=[("Restar el porcentaje de pérdida al pedido en vez de calcular hacia atrás.", "Con la pérdida se necesita más, no menos, de lo que se entrega.", "Se divide el pedido por el porcentaje de éxito."),
              ("Olvidar la germinación al calcular las semillas.", "Parte de las semillas no nace.", "Calcula primero las plántulas y luego las semillas.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el pedido en un plan de vivero?", "La cantidad de plantas que se debe entregar", "La cantidad de semillas que caben en un envase", "La bandeja donde germinan las semillas", "El pedido se mide en plantas entregadas; las semillas son lo que se siembra."),
        ("abc", "En Agropecuaria: ¿por qué se necesitan más plántulas que plantas entregadas?", "Porque parte de las plántulas se pierde al trasplantar", "Porque las plántulas son más baratas", "Porque las plantas crecen más rápido", "Con pérdidas, hay que partir con más de lo que se entrega."),
        ("abc", "En Agropecuaria: ¿qué hay que hacer si el número de bandejas no sale exacto?", "Redondear hacia arriba, porque no se puede tener una bandeja a medias", "Redondear hacia abajo y dejar semillas sin sembrar", "Sembrar más de una semilla por cavidad", "Se necesita una bandeja completa para las semillas que sobran."),
        ("=", "{F} ¿Cuántas plántulas se necesitan antes del trasplante para entregar el pedido?", "2700*100//90", "Se divide el pedido por el porcentaje de plántulas que llega a planta.", " plántulas"),
        ("=", "{F} ¿Cuántas semillas hay que sembrar para obtener esas plántulas?", "2700*100//90*100//80", "Se divide las plántulas necesarias por el porcentaje de germinación.", " semillas"),
        ("=", "{F} ¿Cuántas bandejas de almácigo se necesitan?", "2700*100//90*100//80//250", "Se divide el total de semillas entre las cavidades de cada bandeja.", " bandejas"),
        ("=", "{F} ¿Cuánto cuestan las semillas del pedido?", "2700*100//90*100//80*5", "Se multiplica el número de semillas por el precio de cada una.", " pesos"),
        ("=", "{F} Si el poder germinativo fuera 75 % y la pérdida se mantuviera, ¿cuántas semillas habría que sembrar?", "2700*100//90*100//75", "Se calculan las plántulas y se divide entre el nuevo porcentaje de germinación.", " semillas"),
        ("abc", "{F} Una estudiante calcula las plántulas restando 10 % a 2.700. ¿Cuál es el error?", "Con pérdidas hay que dividir por el éxito, porque se necesita más que el pedido", "Ninguno, porque restar 10 % es correcto", "El error es no sumar el precio", "Restar reduce la cantidad cuando en realidad se debe partir con más."),
        ("abc", "{F} El jefe de producción dice que, para ahorrar, se siembren solo 2.700 semillas. ¿Qué pasaría?", "No se llegaría al pedido, porque parte no germina y parte se pierde al trasplantar", "Se llegaría justo al pedido", "Sobrarían plantas", "Con germinación y pérdidas, 2.700 semillas dan menos de 2.700 plantas."),
        ("=", "{F} Con las semillas sembradas calculadas, ¿cuántas plántulas germinan?", "2700*100//90*100//80*80//100", "Se aplica el poder germinativo a las semillas sembradas.", " plántulas"),
        ("abc", "{F} Un operario sugiere dejar fuera de la bandeja a las plántulas «de aspecto débil» y no registrarlo. ¿Qué corresponde?", "Registrar la pérdida real e informar al técnico", "No registrarlo, porque son pocas", "Ocultarlo para que el porcentaje se vea mejor", "Los registros deben mostrar la pérdida real para planificar bien."),
        ("abc", "En Agropecuaria: ¿por qué se calcula «hacia atrás» desde el pedido?", "Porque cada etapa tiene pérdidas y hay que partir con más cantidad", "Porque las semillas se cuentan al final", "Porque el pedido siempre es menor que las semillas", "Las pérdidas de cada etapa obligan a aumentar la cantidad inicial."),
    ],
    ctx=("abc", "Un vecino te pide una cifra rápida: «¿cuántas semillas compro para 1.000 plantas?». ¿Qué respondes?", "Que necesitas el poder germinativo y las pérdidas esperadas, y que conviene consultar a un técnico", "Que compre 1.000 exactas", "Que compre 1.100 siempre", "La cantidad depende de la germinación y de las pérdidas, que son datos del lote."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula hacia atrás las plántulas necesarias?", "Dividiendo el pedido por el porcentaje de éxito", "Con pérdidas se necesita más cantidad que el pedido."),
        ("En el trabajo agrícola: ¿qué se hace si las bandejas no salen exactas?", "Se redondea hacia arriba", "No se puede usar una bandeja a medias."),
        ("En Agropecuaria: ¿cuántas semillas va en cada cavidad según la ficha?", "Una", "La ficha asigna una semilla por cavidad."),
    ],
    op=("Datos de ejemplo del «Vivero Demo»: pedido de 1.800 plantas; poder germinativo 90 %; llega a planta el 80 % de las plántulas; bandejas de 200 cavidades; precio de $4 por semilla. Escribe (a) las plántulas necesarias antes del trasplante, (b) las semillas que hay que sembrar, (c) las bandejas, (d) el costo de las semillas.",
        "(a) 1.800 × 100 ÷ 80 = 2.250 plántulas. (b) 2.250 × 100 ÷ 90 = 2.500 semillas. (c) 2.500 ÷ 200 = 12,5; se redondean a 13 bandejas. (d) 2.500 × 4 = $10.000.",
        ["calcula las plántulas", "calcula las semillas", "redondea las bandejas hacia arriba", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["restar el porcentaje en vez de dividir", "no redondear hacia arriba las bandejas"],
        "Pregunta: «¿hay que partir con más o con menos que el pedido?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula las semillas necesarias para 450 plantas con poder germinativo de 90 % y sin pérdidas al trasplante.",
    extend="Explica con un ejemplo por qué ocultar las plántulas débiles en el registro perjudica la planificación.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Plantel Demo» es un establecimiento ficticio con 120 cerdos de engorda en corrales. El alimento se guarda en un silo y se mezcla en una mezcladora; el pesaje se hace con una balanza de piso. "
     "Peligros anotados: animales grandes que empujan o muerden, piso mojado, polvo de alimento, un silo (espacio cerrado), una mezcladora con partes móviles y gases acumulados en las fosas donde se junta el purín (mezcla de excrementos y agua).")
build(
    O4, 1, F,
    use="Aprenderé qué son la alimentación y el pesaje en un plantel pecuario, qué peligros tiene el trabajo con animales y cómo se ordenan las medidas de prevención.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Un plantel pecuario es un establecimiento donde se crían animales con fines productivos, como carne, leche o huevos. La alimentación es el conjunto de alimentos y agua que reciben los animales; el pesaje es medir su peso con una balanza para saber si crecen como se espera. Ambos se hacen según la especie, el sistema de crianza y el destino de la producción. Los animales se tratan con respeto: el bienestar animal es que vivan sin hambre, sed, dolor ni miedo excesivos.",
        "El trabajo en un plantel tiene peligros: animales que empujan o muerden, pisos mojados, polvo, silos cerrados, máquinas con partes móviles y fosas con gases. En un silo o una fosa no se entra, porque puede faltar aire o haber gases que dañan. Hay también riesgo de zoonosis, que son enfermedades que pasan de los animales a las personas, y por eso importan la higiene y la ropa de trabajo.",
        f"La jerarquía de controles aplica: una protección fija sobre las partes móviles de la mezcladora es un control de ingeniería; un letrero «prohibido entrar al silo» es administrativo. Las tareas con animales y con equipos las hace personal capacitado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("plantel pecuario", "establecimiento donde se crían animales con fines productivos"), ("alimentación", "alimentos y agua que reciben los animales"), ("pesaje", "medición del peso de los animales con una balanza"), ("bienestar animal", "vivir sin hambre, sed, dolor ni miedo excesivos"), ("zoonosis", "enfermedad que pasa de los animales a las personas"), ("purín", "mezcla de excrementos y agua de un plantel"), ("espacio cerrado", "lugar con poca ventilación, como un silo o una fosa, donde puede faltar aire")],
    worked=[
        ("Peligro y riesgo", "En un plantel de ejemplo hay una fosa de purín sin tapa junto al corral. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la fosa sin tapa, con gases.", "El riesgo es que una persona caiga o respire los gases y se dañe."], "Peligro: la fosa sin tapa con gases; riesgo: caída o intoxicación"),
        ("Clasificar un control", "Un plantel de ejemplo instala una tapa fija con cerradura en una fosa. ¿Qué tipo de control es?", ["La tapa cambia el lugar.", "Cambiar el lugar es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que se puede entrar a un silo o una fosa «solo un momento».", "Puede faltar aire o haber gases que dañan en segundos.", "No se entra: lo hace personal autorizado con equipos y norma vigente."),
              ("Creer que pesar a un animal es solo «ponerlo en la balanza».", "El manejo de animales exige formación para evitar daños a personas y animales.", "Aprende aquí el concepto y deja el manejo a personal capacitado.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es un plantel pecuario?", "Un establecimiento donde se crían animales con fines productivos", "Un campo donde se siembran forrajes", "Una bodega donde se guardan herramientas", "El plantel pecuario es donde se crían animales; el forraje es otro cultivo."),
        ("abc", "En Agropecuaria: ¿qué es el bienestar animal?", "Vivir sin hambre, sed, dolor ni miedo excesivos", "Que el animal engorde lo más rápido posible", "Que el animal tenga una balanza propia", "El bienestar es la condición del animal; engordar rápido no lo garantiza."),
        ("abc", "En Agropecuaria: ¿qué es una zoonosis?", "Una enfermedad que pasa de los animales a las personas", "Un tipo de alimento para animales", "Una balanza para pesar animales", "La zoonosis es la enfermedad que se contagia entre animales y personas."),
        ("=", "{F} Cada cerdo consume 3 kg de alimento por día (dato de ejemplo). ¿Cuántos kilos de alimento se necesitan al día para los animales de la ficha?", "120*3", "Se multiplica el número de animales por el consumo diario de cada uno.", " kg"),
        ("abc", "{F} Una protección fija sobre las partes móviles de la mezcladora es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque es una regla", "De EPP, porque protege a quien se acerca", "La protección es una parte física del equipo y no depende de que alguien la recuerde."),
        ("abc", "{F} Un letrero «prohibido entrar al silo sin autorización» es un control de tipo:", "Administrativo, porque informa y ordena una conducta", "De ingeniería, porque cambia el silo", "De eliminación, porque quita el silo", "El letrero informa; no cambia el silo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a los gases de las fosas de purín?", "Que una persona respire los gases y sufra una intoxicación", "Los gases acumulados en la fosa", "Que el purín sea abono", "El riesgo es la posibilidad de daño; los gases acumulados son el peligro."),
        ("abc", "{F} Una estudiante dice: «puedo entrar al silo con una linterna a revisar el alimento». ¿Qué respuesta es correcta?", "Es peligroso: no se entra a espacios cerrados y lo hace personal autorizado", "Es correcto, si avisa a una compañera", "Es correcto, si entra solo un minuto", "En un espacio cerrado puede faltar aire; la compañía o el tiempo no cambian eso."),
        ("abc", "{F} En una visita, una persona cae a una fosa de purín. ¿Qué corresponde según las reglas generales?", "No acercarte, avisar a un adulto responsable y a emergencias", "Meterte a ayudarla", "Taparte la nariz e inclinarte sobre la fosa", "Entrar o inclinarse expone a los gases; se avisa a quienes tienen el equipo y la formación."),
        ("abc", "En Agropecuaria: ¿por qué no se entra a un espacio cerrado como un silo?", "Porque puede faltar aire o acumularse gases que dañan en pocos segundos", "Porque el alimento se ensucia", "Porque la puerta es pesada", "La falta de aire y los gases son un peligro mortal en un espacio cerrado."),
        ("abc", "{F} Se propone solo entregar mascarillas por el polvo del alimento. ¿Qué medida es más efectiva?", "Cambiar el sistema de manejo para generar menos polvo, como humedecer o cerrar la zona", "Dar el mismo tipo de mascarilla a más personas", "Pedir que se respire por la boca", "Reducir el polvo en su origen está más arriba que la mascarilla (EPP)."),
        ("=", "{F} El silo guarda 7.200 kg de alimento y se gastan 360 kg por día. ¿Para cuántos días alcanza?", "7200//360", "Se divide el alimento guardado entre el gasto diario.", " días"),
        ("abc", "En Agropecuaria: ¿por qué la higiene del personal ayuda a evitar la zoonosis?", "Porque reduce el contacto con microbios que pueden pasar de los animales a las personas", "Porque hace crecer más rápido a los animales", "Porque evita que los animales se ensucien", "Lavarse las manos y usar ropa limpia corta el paso de microbios."),
    ],
    ctx=("abc", "Un conocido que cría cerdos te pide que le ayudes a pesar a los animales «porque son mansos y es fácil». ¿Qué respondes?", "Que no, porque el manejo de animales exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, si son pocos", "Que sí, si no se mueven mucho", "Los animales, aunque parezcan mansos, pueden reaccionar de forma imprevista; el manejo exige formación."),
    sc=[
        ("En Agropecuaria: ¿qué es el pesaje?", "Medir el peso de los animales con una balanza", "El pesaje permite saber si los animales crecen como se espera."),
        ("En el trabajo pecuario: ¿se entra a un silo o a una fosa sin autorización?", "No, porque puede faltar aire o haber gases", "Los espacios cerrados son peligrosos y solo los trata personal autorizado."),
        ("En Agropecuaria: ¿qué es el purín?", "Una mezcla de excrementos y agua de un plantel", "El purín se junta en fosas y emite gases."),
    ],
    op=("El «Plantel Demo» anota una tarea de ejemplo: limpiar a mano una fosa de purín que se tapó, sin ventilar, un día de calor. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a una persona desmayada dentro de la fosa.",
        "(a) Peligro: gases acumulados en la fosa; riesgo: que la persona respire los gases y se desmaye o se intoxique. (b) Una regla de «no entrar a la fosa sin autorización» y un letrero. (c) Una tapa fija y un sistema de ventilación, instalados por personal autorizado. (d) No me acerco ni entro, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no entra y avisa"],
        ["hoja con las cuatro respuestas"],
        ["proponer entrar a rescatar", "llamar riesgo a los gases", "proponer solo mascarilla"],
        "Pregunta: «¿qué control cambia el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el tercer párrafo de la explicación."),
    reinforce="Escribe tres peligros de un plantel pecuario y el riesgo asociado a cada uno.",
    extend="Explica con un ejemplo por qué el EPP no reemplaza a una tapa fija en una fosa.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (tabla y registro de ejemplo, inventados). Cerdos de engorda del «Plantel Demo». Tabla de requerimientos (valores de ejemplo): etapa de inicio, de 20 a 40 kg, 1 kg de alimento por día; etapa de crecimiento, de 40 a 70 kg, 2 kg por día; etapa de terminación, de 70 a 110 kg, 3 kg por día. "
     "Registro de pesaje de un lote de ejemplo (promedio por animal): día 1, 40 kg; día 21, 61 kg. Documentos: la tabla de requerimientos, el registro de alimentación (qué y cuánto se dio) y el registro de pesaje.")
build(
    O4, 2, F,
    use="Aprenderé los conceptos de nutrientes, ración, requerimiento, etapa productiva, ganancia diaria de peso y conversión, cómo se lee un registro de alimentación y pesaje y qué rol cumple cada persona.",
    prior=["Sé qué es el pesaje y la alimentación.", "Sé leer una tabla de datos.", "Sé dividir números enteros."],
    explain=[
        "Los animales necesitan nutrientes: energía, proteína, fibra, minerales, vitaminas y agua. La ración es la cantidad y mezcla de alimentos que recibe un animal en un día. El requerimiento es la cantidad de nutrientes que necesita según su especie y su etapa productiva, es decir, el momento de su ciclo, como inicio, crecimiento o terminación. Alimentar de más o de menos afecta al animal y al costo.",
        "El peso vivo es el peso del animal en vida. La ganancia diaria de peso es lo que aumenta de peso cada día: se calcula restando el peso inicial al final y dividiendo por los días. La conversión alimenticia dice cuántos kilos de alimento se usan para ganar un kilo de peso; mientras más baja, más eficiente es el lote. Una balanza se revisa y se registra: en el pesaje se anota fecha, lote y peso.",
        f"Quien formula la ración es un nutricionista animal o un médico veterinario; el encargado de alimentación la entrega según el registro. Las dudas sobre la salud de un animal se derivan al veterinario. {EMER} {AVISO}",
    ],
    vocab=[("ración", "cantidad y mezcla de alimentos que recibe un animal en un día"), ("requerimiento", "nutrientes que necesita un animal según su especie y etapa"), ("etapa productiva", "momento del ciclo del animal, como inicio, crecimiento o terminación"), ("peso vivo", "peso del animal en vida"), ("ganancia diaria de peso", "kilos que gana un animal por día"), ("conversión alimenticia", "kilos de alimento por cada kilo de peso ganado"), ("registro de pesaje", "documento que anota fecha, lote y peso")],
    worked=[
        ("Ganancia diaria", "Un lote de ejemplo pesa 30 kg el día 1 y 50 kg el día 40. ¿Cuántos kilos ganó por día en promedio?", ["Ganó 50 menos 30, o sea 20 kg.", "20 kg en 40 días son medio kilo por día: 500 gramos."], "500 gramos por día"),
        ("Conversión", "El mismo lote consumió 60 kg de alimento por animal y ganó 20 kg. ¿Cuál es la conversión alimenticia?", ["Se dividen los kilos de alimento entre los kilos ganados.", "60 entre 20 es 3."], "3 kg de alimento por cada kg ganado"),
    ],
    mistakes=[("Creer que mientras más alimento reciba un animal, mejor.", "Un exceso aumenta el costo y puede dañar al animal.", "Se entrega la ración que fija el requerimiento de su etapa."),
              ("Anotar un peso aproximado «de memoria» en el registro.", "Un registro sin dato real no sirve para decidir.", "Se anota el peso medido con la balanza revisada.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la ración de un animal?", "La cantidad y mezcla de alimentos que recibe en un día", "El peso del animal al nacer", "La balanza donde se pesa", "La ración es lo que come en un día; el peso y la balanza son otros conceptos."),
        ("abc", "En Agropecuaria: ¿qué es el requerimiento de un animal?", "Los nutrientes que necesita según su especie y etapa", "La cantidad de agua que cae en el corral", "El precio del alimento", "El requerimiento depende de la especie y de la etapa productiva."),
        ("abc", "En Agropecuaria: ¿qué indica la conversión alimenticia?", "Los kilos de alimento usados por cada kilo de peso ganado", "Los días que tarda un animal en crecer", "El precio de cada kilo de carne", "La conversión relaciona alimento consumido y peso ganado."),
        ("=", "{F} ¿Cuántos kilos de alimento por día corresponden a un cerdo en etapa de crecimiento, según la tabla, si hay 50 cerdos de ese lote?", "50*2", "Se multiplica el requerimiento diario de un animal por el número de animales.", " kg"),
        ("abc", "{F} ¿En qué etapa está un cerdo de 55 kg según la tabla?", "Crecimiento", "Inicio", "Terminación", "55 kg está entre 40 y 70, que es la etapa de crecimiento."),
        ("abc", "{F} ¿Qué documento anotaría qué alimento y cuánto se dio a un lote?", "El registro de alimentación", "El registro de pesaje", "La tabla de requerimientos", "El registro de alimentación guarda lo entregado; el pesaje guarda pesos y la tabla fija lo requerido."),
        ("=", "{F} ¿Cuántos kilos ganó por animal el lote entre el día 1 y el día 21?", "61-40", "Se resta el peso inicial al peso del día 21.", " kg"),
        ("=", "{F} ¿Cuántos kilos por día ganó por animal el lote entre el día 1 y el 21?", "(61-40)//21", "Se divide lo ganado entre los días transcurridos.", " kg por día"),
        ("abc", "{F} Si el lote consumió 63 kg de alimento por animal en ese período, ¿cuál fue la conversión alimenticia?", "3 kg de alimento por kg ganado", "1 kg de alimento por kg ganado", "21 kg de alimento por kg ganado", "63 entre los 21 kg ganados da 3."),
        ("abc", "{F} Un encargado dice: «como un cerdo de 80 kg es grande, le doy 5 kg de alimento por día». ¿Qué respuesta es correcta?", "Es incorrecto: la tabla de ejemplo indica 3 kg por día para esa etapa", "Es correcto, porque mientras más come, mejor", "Es correcto, si come con apetito", "Se entrega lo que fija el requerimiento de la etapa, no más por intuición."),
        ("abc", "{F} Un animal del lote parece decaído y no quiere comer. ¿Qué corresponde?", "Avisar al encargado y al médico veterinario, sin medicarlo por cuenta propia", "Darle una dosis de un medicamento de otro animal", "Aumentarle el alimento hasta que coma", "Las dudas de salud las evalúa el veterinario; medicar sin indicación puede dañar."),
        ("=", "{F} Un lote de 40 cerdos en terminación recibe la ración de la tabla. ¿Cuántos kilos de alimento por día necesita el lote?", "40*3", "Se multiplica la ración diaria por el número de animales.", " kg"),
        ("abc", "En Agropecuaria: ¿por qué conviene que la balanza se revise antes de pesar?", "Porque un instrumento mal ajustado entrega datos falsos", "Porque el animal se asusta menos", "Porque la balanza gasta menos", "Si la balanza no está bien ajustada, los pesos registrados no son confiables."),
    ],
    ctx=("abc", "Una conocida que cría pollos te pide que le entregues una ración exacta «para que engorden más rápido». ¿Qué respondes?", "Que la ración la define un nutricionista o veterinario según la especie y la etapa", "Que dé el doble de alimento", "Que dé solo maíz", "La ración depende de la especie y de la etapa; un exceso o un solo alimento pueden dañar."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula la ganancia diaria de peso?", "Peso final menos peso inicial, dividido por los días", "La ganancia diaria resume cuánto sube el peso por día."),
        ("En el trabajo pecuario: ¿qué se hace ante un animal decaído?", "Se avisa al encargado y al veterinario", "La salud del animal la evalúa el médico veterinario."),
        ("En Agropecuaria: ¿qué anota el registro de pesaje?", "La fecha, el lote y el peso", "El registro guarda los datos para seguir el crecimiento."),
    ],
    op=("Tabla de ejemplo (aves de engorda): etapa 1, 1 kg de alimento por día cada 10 aves; etapa 2, 2 kg por día cada 10 aves. Registro de ejemplo de un lote de 100 aves en etapa 2: peso promedio de 800 gramos el día 1 y de 1.400 gramos el día 15. Escribe (a) cuántos kilos de alimento por día necesita el lote en etapa 2, (b) cuántos gramos ganó por ave en total, (c) cuántos gramos ganó por ave por día, (d) a quién consultas si un ave se ve decaída.",
        "(a) 100 ÷ 10 = 10 grupos; 10 × 2 = 20 kg por día. (b) 1.400 − 800 = 600 gramos. (c) 600 ÷ 15 = 40 gramos por día. (d) Al encargado y al médico veterinario; no la medico yo.",
        ["calcula el alimento del lote", "calcula la ganancia total", "calcula la ganancia diaria", "deriva al veterinario"],
        ["hoja con las cuatro respuestas"],
        ["no dividir por los días", "dar un medicamento por cuenta propia"],
        "Pregunta: «¿cuántos grupos de 10 aves hay en 100?». Si no responde, pídele que relea la tabla."),
    reinforce="Calcula la ganancia diaria de un lote inventado que pasa de 25 a 55 kg en 30 días.",
    extend="Explica con un ejemplo por qué la conversión alimenticia sirve para comparar dos lotes.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Lote B del «Plantel Demo»: 100 cerdos. Semana 1: consumo de 300 kg de alimento por día y peso promedio de 50 kg. Semana 3: consumo de 240 kg por día y peso promedio de 52 kg. "
     "Observaciones anotadas: los bebederos de un corral gotean y dejan el piso mojado; el alimento guardado en una bolsa abierta huele a humedad; cinco animales están apartados porque tosen.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso de alimentación y pesaje con registros, a relacionar los datos con posibles causas y a decidir a quién derivar lo que excede mi rol.",
    prior=["Sé qué es la ganancia diaria y la conversión.", "Sé leer un registro con datos.", "Sé calcular porcentajes enteros."],
    explain=[
        "Para analizar un caso se leen los registros y se buscan cambios. Si el consumo de alimento baja y el peso casi no sube, algo está fallando: puede ser la calidad del alimento, la disponibilidad de agua o la salud de los animales. Un alimento con olor a humedad puede tener hongos que dañan; los bebederos que gotean mojan el piso y pueden provocar caídas y enfermedades.",
        "Quien analiza el caso no diagnostica ni medica: describe lo observado con datos y avisa a quien corresponde. El encargado de alimentación revisa el alimento y el agua; el médico veterinario evalúa a los animales que tosen. Los animales con síntomas se apartan solo si lo indica el encargado y lo hace personal capacitado, porque acercarse a animales enfermos tiene riesgos.",
        f"El análisis deja una conclusión con al menos dos evidencias y una derivación clara. Nunca se alimenta con alimento dañado ni se da un medicamento por cuenta propia. {EMER} {AVISO}",
    ],
    vocab=[("consumo", "cantidad de alimento que come un lote"), ("síntoma", "señal visible de que un animal puede estar enfermo"), ("moho", "hongo que crece en alimentos húmedos"), ("derivar", "avisar a quien corresponde para que decida"), ("evidencia", "dato del caso que respalda una conclusión"), ("registro", "documento que guarda datos para decidir")],
    worked=[
        ("Calcular una variación", "El consumo de un lote de ejemplo baja de 200 kg a 150 kg por día. ¿Cuántos kilos bajó?", ["Se resta el consumo nuevo al antiguo.", "200 menos 150."], "50 kg por día"),
        ("Decidir a quién derivar", "En un plantel de ejemplo hay animales con tos. ¿A quién se avisa?", ["Evaluar la salud animal no es función de quien registra pesos.", "La salud de los animales la evalúa el médico veterinario."], "Al encargado y al médico veterinario"),
    ],
    mistakes=[("Culpar a una sola causa sin mirar el resto de los datos.", "Varias causas pueden producir el mismo síntoma.", "Se listan las evidencias y se deriva al especialista."),
              ("Dar un medicamento «para que se mejore» a un animal con tos.", "Solo el médico veterinario puede indicar un tratamiento.", "Se avisa al encargado y al veterinario.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el moho en un alimento?", "Un hongo que crece cuando el alimento está húmedo", "Un nutriente que aporta energía", "Un envase para guardar el alimento", "El moho es un hongo que daña el alimento."),
        ("abc", "En Agropecuaria: ¿qué es un síntoma en un animal?", "Una señal visible de que podría estar enfermo", "Un registro de su peso", "Un alimento especial", "El síntoma es una señal; el registro y el alimento son otras cosas."),
        ("abc", "En Agropecuaria: ¿qué significa derivar un problema de salud animal?", "Avisar a quien corresponde para que decida", "Darle un tratamiento propio al animal", "Ocultarlo para evitar una inspección", "Derivar es avisar al especialista; tratar por cuenta propia es riesgoso."),
        ("=", "{F} ¿Cuántos kilos por día bajó el consumo entre la semana 1 y la semana 3?", "300-240", "Se resta el consumo de la semana 3 al de la semana 1.", " kg"),
        ("=", "{F} ¿Cuántos kilos aumentó el peso promedio entre la semana 1 y la semana 3?", "52-50", "Se resta el peso inicial al peso de la semana 3.", " kg"),
        ("abc", "{F} ¿Qué evidencia de la ficha sugiere un problema con el alimento?", "El alimento de una bolsa abierta huele a humedad", "El peso aumentó 2 kg", "Los bebederos son de metal", "El olor a humedad apunta a moho."),
        ("abc", "{F} ¿Qué evidencia de la ficha sugiere un problema de agua o de piso mojado?", "Los bebederos de un corral gotean y mojan el piso", "El consumo es de 300 kg", "El lote tiene 100 cerdos", "El goteo es una falla de la instalación de agua."),
        ("abc", "{F} ¿A quién se avisa por los cinco animales que tosen?", "Al encargado y al médico veterinario", "Solo al encargado del silo", "A ninguno, porque son pocos", "La salud animal la evalúa el veterinario."),
        ("abc", "{F} Una compañera dice: «ya sé qué tienen los cerdos y les daré un medicamento». ¿Qué respuesta es correcta?", "Es incorrecto: el diagnóstico y el tratamiento los hace el médico veterinario", "Es correcto, si la dosis es pequeña", "Es correcto, si lo hace de noche", "Solo el veterinario puede diagnosticar y recetar."),
        ("abc", "{F} El encargado ordena apartar a los cinco animales que tosen. ¿Quién debe hacerlo?", "Personal capacitado y autorizado, no una estudiante", "Cualquier visitante que pase", "Una estudiante, con guantes", "Mover animales exige formación y autorización."),
        ("=", "{F} Si el consumo vuelve a 300 kg por día en 100 cerdos, ¿cuántos kilos consume cada cerdo por día?", "300//100", "Se divide el consumo total entre el número de animales.", " kg"),
        ("abc", "{F} Alguien propone mezclar el alimento con olor a humedad con alimento nuevo «para que rinda». ¿Qué corresponde?", "Rechazarlo, apartar el alimento dañado y avisar al encargado", "Aceptarlo, porque rinde más", "Aceptarlo, si se mezcla bien", "El alimento con moho puede dañar a los animales; no se diluye."),
        ("abc", "En Agropecuaria: ¿por qué un consumo menor con poco aumento de peso es una señal de alerta?", "Porque indica que algo falla en el alimento, el agua o la salud", "Porque indica que el lote es muy eficiente", "Porque indica que los animales ya no necesitan comer", "Menos consumo y poco peso pueden señalar un problema que hay que investigar."),
    ],
    ctx=("abc", "Una conocida te dice que sus cerdos comen menos y te pide que le recomiendes un medicamento. ¿Qué respondes?", "Que no puedes recomendarlo y que debe consultar a un médico veterinario", "Que les dé el mismo que usó el año pasado", "Que les dé vitaminas al azar", "Solo un veterinario puede indicar un tratamiento después de evaluar a los animales."),
    sc=[
        ("En Agropecuaria: ¿qué se hace con un alimento con olor a humedad?", "Se aparta y se avisa al encargado", "El alimento con moho puede dañar a los animales."),
        ("En el trabajo pecuario: ¿quién diagnostica una enfermedad animal?", "El médico veterinario", "Diagnosticar una enfermedad es función del médico veterinario."),
        ("En Agropecuaria: ¿qué dos datos muestran que algo falla en el lote B?", "El consumo bajó y el peso casi no subió", "El consumo y el peso se mueven juntos al crecer los animales."),
    ],
    op=("Caso de ejemplo del «Plantel Demo»: Lote C de 80 animales. Semana 1: consumo de 160 kg por día y peso promedio de 30 kg; semana 3: consumo de 120 kg por día y peso promedio de 31 kg. Observación: el agua de un bebedero sale turbia. Escribe (a) cuánto bajó el consumo, (b) cuánto subió el peso promedio, (c) una causa posible que veas en el caso, (d) a quién avisas y qué no haces.",
        "(a) 160 − 120 = 40 kg por día. (b) 31 − 30 = 1 kg. (c) El agua turbia del bebedero. (d) Aviso al encargado y al médico veterinario; no medico ni diagnostico por cuenta propia.",
        ["calcula la baja del consumo", "calcula el aumento de peso", "cita una causa del caso", "deriva sin medicar"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "medicar por cuenta propia", "decir una causa sin evidencia"],
        "Pregunta: «¿qué dato del caso te llama la atención sobre el agua?». Si no responde, pídele que relea el caso."),
    reinforce="Escribe tres cosas que revisarías en los registros si un lote deja de ganar peso y a quién derivarías cada una.",
    extend="Explica con un ejemplo por qué es útil escribir las evidencias antes de proponer una causa.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Lote de 50 animales del «Plantel Demo». Peso promedio inicial: 30 kg. Peso promedio final: 90 kg a los 120 días. Alimento consumido por todo el lote: 9.000 kg. "
     "Precio del alimento: $400 por kilo (dato de ejemplo).")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular ganancia de peso, conversión alimenticia y costo de alimentación de un lote.",
    prior=["Sé qué son la ganancia diaria y la conversión.", "Sé multiplicar y dividir enteros.", "Sé leer un registro con datos."],
    explain=[
        "Con los registros de un lote se calculan indicadores que ayudan a decidir. La ganancia total por animal es el peso final menos el inicial. La ganancia de todo el lote es esa ganancia por el número de animales. La ganancia diaria es la ganancia por animal dividida por los días. La conversión alimenticia es el alimento total consumido dividido por la ganancia total del lote.",
        "El costo de alimentación es el alimento consumido por su precio. El costo por kilo ganado resulta de dividir el costo de alimentación entre los kilos ganados por el lote, o multiplicar la conversión por el precio del alimento. Con estos números se compara un lote con otro y se detecta si hay un problema, pero la conclusión la entrega el técnico, que mira también la salud, el bienestar y el mercado.",
        f"Las cifras de esta clase son de ejemplo: los valores reales dependen de la especie, de la raza y del sistema de crianza. {EMER} {AVISO}",
    ],
    vocab=[("ganancia total", "peso final menos peso inicial"), ("ganancia del lote", "ganancia por animal por el número de animales"), ("conversión alimenticia", "kilos de alimento por cada kilo de peso ganado"), ("costo de alimentación", "alimento consumido por su precio"), ("costo por kilo ganado", "costo de alimentación dividido por los kilos ganados"), ("indicador", "número que resume cómo va un proceso")],
    worked=[
        ("Ganancia del lote", "Un lote de ejemplo de 20 animales pasa de 20 a 45 kg por animal. ¿Cuántos kilos gana el lote?", ["Cada animal gana 45 menos 20, o sea 25 kg.", "25 por 20 animales."], "500 kg"),
        ("Costo por kilo", "El lote anterior consumió 1.500 kg de alimento y el kilo costó $300 (valores de ejemplo). ¿Cuánto costó la alimentación?", ["Se multiplica el alimento por el precio.", "1.500 por 300."], "$450.000"),
    ],
    mistakes=[("Calcular la conversión con la ganancia de un solo animal y el alimento de todo el lote.", "Se mezclan magnitudes de distinto tamaño.", "Usa la ganancia del lote con el alimento del lote."),
              ("Concluir que un lote es bueno solo por su conversión baja.", "La salud y el bienestar también importan.", "El técnico mira los indicadores junto con el estado de los animales.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la ganancia total por animal?", "El peso final menos el peso inicial", "El peso inicial más el peso final", "El peso que tiene al nacer", "La ganancia es la diferencia entre el peso final y el inicial."),
        ("abc", "En Agropecuaria: ¿qué es el costo de alimentación de un lote?", "El alimento consumido por su precio", "El precio de la balanza", "El sueldo del encargado", "El costo de alimentación multiplica kilos de alimento por precio."),
        ("abc", "En Agropecuaria: ¿qué es un indicador productivo?", "Un número que resume cómo va un proceso", "Una señal de peligro del corral", "Un animal que sirve de ejemplo", "Un indicador resume el desempeño; no es un animal ni una señal de peligro."),
        ("=", "{F} ¿Cuántos kilos ganó cada animal del lote?", "90-30", "Se resta el peso inicial al peso final.", " kg"),
        ("=", "{F} ¿Cuántos kilos ganó todo el lote?", "(90-30)*50", "Se multiplica la ganancia por animal por el número de animales.", " kg"),
        ("=", "{F} ¿Cuál es la conversión alimenticia del lote, en kilos de alimento por kilo ganado?", "9000//((90-30)*50)", "Se divide el alimento total entre los kilos ganados por el lote.", " kg"),
        ("=", "{F} ¿Cuánto costó la alimentación de todo el lote?", "9000*400", "Se multiplica el alimento total por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuánto costó, en promedio, producir cada kilo ganado por el lote?", "9000*400//((90-30)*50)", "Se divide el costo de alimentación entre los kilos ganados por el lote.", " pesos"),
        ("=", "{F} ¿Cuántos gramos ganó por día, en promedio, cada animal?", "(90-30)*1000//120", "Se convierte la ganancia a gramos y se divide entre los días.", " gramos"),
        ("abc", "{F} Un encargado calcula la conversión dividiendo 9.000 por 60, la ganancia de un solo animal. ¿Cuál es el error?", "Mezcla el alimento de todo el lote con la ganancia de un animal", "Ninguno, porque 60 es la ganancia correcta", "El error es dividir en vez de multiplicar", "Hay que usar la ganancia de todo el lote, 3.000 kg."),
        ("abc", "{F} Un lote vecino de ejemplo tiene una conversión de 4. ¿Cuál lote fue más eficiente?", "El lote de la ficha, porque necesita menos alimento por kilo ganado", "El lote vecino, porque 4 es mayor", "Los dos por igual", "Una conversión menor significa menos alimento por kilo ganado."),
        ("abc", "{F} Un encargado quiere bajar el costo reduciendo a la mitad la ración que fijó el nutricionista «para ahorrar». ¿Qué corresponde?", "Rechazarlo: la ración la fija el requerimiento y el nutricionista, no el ahorro", "Aceptarlo, porque el alimento es caro", "Aceptarlo, si lo hace solo una semana", "Una ración insuficiente daña el crecimiento y el bienestar."),
        ("abc", "En Agropecuaria: ¿por qué la conversión sola no basta para evaluar un lote?", "Porque también cuentan la salud, el bienestar y las condiciones del mercado", "Porque la conversión es un dato falso", "Porque los lotes no se pueden comparar", "Un indicador es una parte de la evaluación completa."),
    ],
    ctx=("abc", "Un conocido te muestra los números de su lote y te pide que le digas, sin conocer sus animales, si debe vender o seguir engordando. ¿Qué respondes?", "Que los indicadores ayudan, pero la decisión la toma el técnico con más datos", "Que venda de inmediato", "Que siga engordando siempre", "La decisión depende de más factores que un solo indicador."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula el costo de alimentación?", "Alimento consumido por su precio", "El costo es el producto de kilos y precio."),
        ("En el trabajo pecuario: ¿qué significa una conversión más baja?", "Que se usa menos alimento por kilo ganado", "Una conversión menor indica un lote más eficiente."),
        ("En Agropecuaria: ¿cómo se calcula la ganancia del lote?", "La ganancia por animal por el número de animales", "La ganancia del lote suma la de todos los animales."),
    ],
    op=("Datos de ejemplo del «Plantel Demo»: lote de 40 animales; peso inicial promedio 25 kg; peso final promedio 85 kg; alimento consumido por todo el lote 7.200 kg; precio del alimento $350 el kilo. Escribe (a) los kilos ganados por el lote, (b) la conversión alimenticia, (c) el costo de alimentación, (d) por qué la conversión no basta para evaluar el lote.",
        "(a) (85 − 25) × 40 = 2.400 kg. (b) 7.200 ÷ 2.400 = 3 kg de alimento por kg ganado. (c) 7.200 × 350 = $2.520.000. (d) Porque también importan la salud, el bienestar y el mercado, y la conclusión la entrega el técnico.",
        ["calcula la ganancia del lote", "calcula la conversión", "calcula el costo", "explica el límite del indicador"],
        ["hoja con las cuatro respuestas"],
        ["usar la ganancia de un animal", "no multiplicar por el precio", "concluir solo con la conversión"],
        "Pregunta: «¿cuántos kilos ganó cada animal y cuántos animales son?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la ganancia de un lote de 10 animales que pasa de 20 a 50 kg por animal, y su conversión si consumió 450 kg de alimento.",
    extend="Explica con un ejemplo por qué dos lotes con la misma conversión pueden tener condiciones de bienestar distintas.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Predio Demo» es un establecimiento ficticio de 30 hectáreas con huerto y un pequeño plantel de cerdos. Genera restos de poda y cosecha, guano y purín, envases vacíos de productos de uso sanitario, plástico de cobertura, aceite usado de maquinaria y cartones. "
     "Peligros anotados: envases con restos de producto, gases y caída en la fosa de purín, derrames de aceite, fuego si se quema residuos, y moscas y roedores en acopios descubiertos.")
build(
    O5, 1, F,
    use="Aprenderé qué son los residuos de un proceso productivo agropecuario, por qué la legislación exige manejarlos y disponerlos bien, y cuáles son los peligros de su manejo.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé dividir números enteros."],
    explain=[
        "Un residuo es todo material que queda de un proceso y ya no se usa en él. En un predio hay residuos orgánicos, como restos de poda, guano y purín; residuos inorgánicos, como plásticos y cartones; y residuos peligrosos, como los envases vacíos de productos de uso sanitario y el aceite usado, que pueden dañar a las personas y al ambiente. Manejar es separar, guardar y registrar; disponer es dar el destino final.",
        "La legislación vigente obliga a manejar los residuos sin dañar la salud ni el ambiente: no se botan a canales, no se queman por cuenta propia y los peligrosos se entregan solo a gestores autorizados. Un gestor autorizado es una empresa con permiso de la autoridad sanitaria y ambiental para retirar, transportar o eliminar residuos. Mal manejados, los residuos contaminan el agua y el suelo y atraen moscas y roedores.",
        f"Los peligros del manejo son el contacto con envases con restos de producto, la fosa de purín y el fuego. Un acopio cerrado y rotulado es un control de ingeniería. Estas tareas las hace personal capacitado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("residuo", "material que queda de un proceso y ya no se usa en él"), ("residuo orgánico", "residuo de origen vegetal o animal que se descompone"), ("residuo peligroso", "residuo que puede dañar a las personas o al ambiente"), ("gestor autorizado", "empresa con permiso para retirar, transportar o eliminar residuos"), ("manejo", "separar, guardar y registrar los residuos"), ("disposición final", "destino final que se da a un residuo"), ("contaminación", "daño al agua, al suelo o al aire por residuos mal manejados")],
    worked=[
        ("Clasificar un residuo", "En un predio de ejemplo queda un tambor de aceite usado de la maquinaria. ¿Es orgánico, inorgánico no peligroso o peligroso?", ["El aceite usado puede dañar al ambiente y a las personas.", "Por eso es un residuo peligroso."], "Peligroso"),
        ("Clasificar un control", "Un predio de ejemplo instala una tapa fija con cierre en el tambor donde junta el aceite usado. ¿Qué tipo de control es?", ["La tapa fija cambia físicamente el envase.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que quemar los residuos es una forma segura de eliminarlos.", "La quema libera humo y puede causar incendios o contaminar.", "Se entregan a gestores autorizados o se valorizan según la norma vigente."),
              ("Creer que un envase vacío de producto sanitario es un residuo común.", "Puede conservar restos del producto y dañar.", "Se maneja como residuo peligroso y lo retira un gestor autorizado.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es un residuo?", "Un material que queda de un proceso y ya no se usa en él", "Un producto nuevo que se acaba de comprar", "Un insumo que se guarda para sembrar", "Un residuo es lo que sobra de un proceso."),
        ("abc", "En Agropecuaria: ¿qué es un residuo peligroso?", "Un residuo que puede dañar a las personas o al ambiente", "Un residuo que se descompone rápido", "Un residuo de color oscuro", "Lo peligroso se define por el daño posible, no por su color o su descomposición."),
        ("abc", "En Agropecuaria: ¿qué es un gestor autorizado de residuos?", "Una empresa con permiso para retirar, transportar o eliminar residuos", "Una persona que trabaja en el predio", "Un camión del predio", "El gestor autorizado cuenta con permiso de la autoridad."),
        ("=", "{F} El plantel genera 40 kg de guano por día (dato de ejemplo). ¿Cuántos kilos genera en una semana de 7 días?", "40*7", "Se multiplica la producción diaria por los días de la semana.", " kg"),
        ("abc", "{F} Una bodega con piso impermeable, techo y llave para los envases peligrosos es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla", "De EPP, porque protege al personal", "La bodega es una estructura física y no depende de que alguien la recuerde."),
        ("abc", "{F} Una regla que dice «los envases peligrosos se entregan solo al gestor autorizado» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el envase", "De sustitución, porque cambia el gestor", "Una regla escrita es un control de tipo administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a los acopios descubiertos de residuos?", "Que atraigan moscas y roedores que pueden contaminar y enfermar", "El acopio mismo en el suelo", "Que ocupen poco espacio", "El riesgo es la posibilidad de daño; el acopio descubierto es el peligro."),
        ("abc", "{F} Una estudiante dice: «puedo quemar los cartones y el plástico para limpiar rápido el predio». ¿Qué respuesta es correcta?", "Es incorrecto: la quema se rige por la norma vigente y puede causar incendios", "Es correcto, si hay poco viento", "Es correcto, si es de noche", "Quemar residuos sin autorización contamina y puede iniciar un incendio."),
        ("abc", "{F} Durante una visita se inicia fuego en un acopio de cartones. ¿Qué corresponde según las reglas generales?", "No acercarte, avisar a un adulto responsable y a emergencias", "Apagarlo con las manos", "Tirar agua sin saber qué hay en el acopio", "Acercarse puede provocar una quemadura; se avisa a quienes pueden actuar."),
        ("abc", "En Agropecuaria: ¿por qué los residuos peligrosos no se mezclan con la basura común?", "Porque pueden dañar a las personas y al ambiente si se manejan mal", "Porque pesan demasiado", "Porque son de menor tamaño", "Su manejo especial evita daños en la salud y en el ambiente."),
        ("abc", "{F} Se propone solo dar guantes para tocar los envases con restos de producto. ¿Qué medida es más efectiva?", "Guardarlos tapados en una bodega cerrada y entregarlos al gestor autorizado", "Dar guantes de repuesto", "Pedir a las personas que no los toquen cuando puedan", "Reducir la exposición en su origen está más arriba que el guante."),
        ("=", "{F} El predio genera 800 kg de plástico de cobertura al mes y un camión del reciclador retira 200 kg por viaje. ¿Cuántos viajes se necesitan?", "800//200", "Se divide el plástico entre los kilos que se retiran en cada viaje.", " viajes"),
        ("abc", "En Agropecuaria: ¿por qué un acopio cerrado y rotulado es mejor que uno abierto?", "Porque evita contaminación y deja claro qué residuo contiene", "Porque ocupa menos espacio", "Porque no necesita registro", "El cierre y el rótulo previenen contaminación y errores."),
    ],
    ctx=("abc", "Un vecino te ofrece dejarte sus envases vacíos de un producto sanitario «porque a ti te sirve para guardar agua». ¿Qué respondes?", "Que no, porque son residuos peligrosos y se entregan a un gestor autorizado", "Que sí, si los lavas con agua", "Que sí, si no los usas para beber", "Los envases pueden conservar restos de producto; no se reutilizan."),
    sc=[
        ("En Agropecuaria: ¿qué tipo de residuo es el aceite usado?", "Peligroso", "El aceite usado puede dañar al ambiente."),
        ("En el trabajo agrícola: ¿se queman los residuos por cuenta propia?", "No, la quema se rige por la norma vigente", "La quema puede contaminar y causar incendios."),
        ("En Agropecuaria: ¿qué es la disposición final?", "El destino final que se da a un residuo", "La disposición final cierra el ciclo de manejo."),
    ],
    op=("El «Predio Demo 2» anota una tarea de ejemplo: juntar en un patio abierto, junto a un canal, envases vacíos de productos de uso sanitario y aceite usado en tambores sin tapa. Escribe (a) el peligro del patio abierto junto al canal y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves un derrame que llega al canal.",
        "(a) Peligro: residuos peligrosos sin cierre junto al canal; riesgo: que lluvias o derrames contaminen el agua y dañen a las personas. (b) Una regla de entregar los residuos peligrosos solo al gestor autorizado y un registro de retiros. (c) Una bodega cerrada con piso impermeable. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca al derrame y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer limpiar el derrame sin formación", "no avisar"],
        "Pregunta: «¿qué control evita el contacto con los residuos aunque alguien se olvide de la regla?». Si no responde, pídele que relea el tercer párrafo."),
    reinforce="Clasifica en orgánicos, inorgánicos no peligrosos o peligrosos estos residuos inventados: cáscaras, botellas plásticas, aceite usado.",
    extend="Explica con un ejemplo por qué un gestor autorizado es necesario para los residuos peligrosos.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (registro de ejemplo, inventado). Registro de generación y retiro del «Predio Demo 2» en un mes de ejemplo: restos vegetales, 6 toneladas, destino compostaje propio; plástico de cobertura, 800 kg, destino reciclador autorizado; "
     "envases vacíos de productos de uso sanitario, 40 kg, destino gestor autorizado de residuos peligrosos; aceite usado, 120 litros, destino gestor autorizado. Otros documentos: el comprobante de entrega (lo que recibe el gestor) y la hoja de datos de seguridad de cada producto.")
build(
    O5, 2, F,
    use="Aprenderé la jerarquía de manejo de residuos, qué es el compostaje y el purín, cómo se leen los documentos de generación y retiro y qué roles participan.",
    prior=["Sé clasificar un residuo en orgánico, inorgánico o peligroso.", "Sé leer un registro con datos.", "Sé sumar y restar enteros."],
    explain=[
        "La jerarquía de manejo ordena las acciones de la mejor a la peor: reducir lo que se genera, reutilizar, reciclar, valorizar (darle un uso útil, como hacer compost) y, como último recurso, eliminar. El compostaje es la descomposición controlada de residuos orgánicos que da compost, un abono. El purín y el guano también se pueden valorizar como abono, bajo la norma vigente, para no contaminar el agua ni el suelo.",
        "Los documentos dejan evidencia: el registro de generación y retiro anota qué residuo, cuánto y a dónde fue; el comprobante de entrega prueba que el gestor lo recibió; la hoja de datos de seguridad dice los peligros de cada producto y qué hacer con sus envases. El encargado ambiental lleva los registros, el prevencionista asesora en riesgos y el gestor autorizado retira y trata los residuos peligrosos.",
        f"Un registro de residuos no se altera ni se completa «de memoria»; si falta un dato, se informa. {EMER} {AVISO}",
    ],
    vocab=[("reducir", "generar menos residuos desde el origen"), ("reciclar", "convertir un residuo en un material nuevo"), ("valorizar", "darle un uso útil a un residuo, como hacer compost"), ("compostaje", "descomposición controlada de residuos orgánicos que da abono"), ("comprobante de entrega", "documento que prueba que el gestor recibió el residuo"), ("hoja de datos de seguridad", "documento con los peligros de un producto y su manejo")],
    worked=[
        ("Ordenar en la jerarquía", "Un predio de ejemplo convierte restos de poda en compost. ¿Qué acción de la jerarquía es?", ["El residuo recibe un uso útil como abono.", "Eso es valorizar."], "Valorizar"),
        ("Total de residuos", "Un registro de ejemplo anota 3 toneladas de restos vegetales y 2 toneladas de cartón en el mes. ¿Cuántas toneladas suman?", ["Se suman las dos cantidades.", "3 más 2."], "5 toneladas"),
    ],
    mistakes=[("Creer que reciclar y valorizar son lo mismo que eliminar.", "Eliminar es el último recurso de la jerarquía.", "Primero se reduce, reutiliza, recicla o valoriza."),
              ("Entregar un residuo peligroso sin pedir el comprobante.", "Sin comprobante no hay prueba de dónde terminó el residuo.", "Se guarda el comprobante de entrega junto al registro.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué significa valorizar un residuo?", "Darle un uso útil, como hacer compost con residuos orgánicos", "Botarlo lo más lejos posible", "Quemarlo para reducir su volumen", "Valorizar es darle un uso útil; botar o quemar no lo hace."),
        ("abc", "En Agropecuaria: ¿qué es el compostaje?", "La descomposición controlada de residuos orgánicos que da abono", "La mezcla de residuos peligrosos en una fosa", "La quema de rastrojos en el campo", "El compostaje es descomposición controlada de materia orgánica."),
        ("abc", "En Agropecuaria: ¿para qué sirve el comprobante de entrega de un residuo?", "Para probar que el gestor lo recibió", "Para fijar el precio del residuo", "Para guardar el residuo", "El comprobante da evidencia de la entrega."),
        ("=", "{F} ¿Cuántos kilos suman el plástico de cobertura y los envases de productos de uso sanitario del registro?", "800+40", "Se suman los kilos de ambos residuos.", " kg"),
        ("abc", "{F} ¿Qué destino tienen los envases de productos de uso sanitario según el registro?", "Gestor autorizado de residuos peligrosos", "Compostaje propio", "Reciclador autorizado", "El registro anota ese destino para los envases con restos de producto."),
        ("abc", "{F} ¿Qué acción de la jerarquía corresponde al compostaje propio de los restos vegetales?", "Valorizar", "Eliminar", "Reducir", "El compost da un uso útil al residuo."),
        ("abc", "{F} ¿Qué documento dice los peligros de un producto de uso sanitario y qué hacer con sus envases?", "La hoja de datos de seguridad", "El comprobante de entrega", "El registro de generación y retiro", "La hoja de datos describe el producto; el comprobante prueba la entrega y el registro anota cantidades."),
        ("abc", "{F} ¿Quién retira y trata los residuos peligrosos?", "El gestor autorizado", "El encargado de la huerta", "Un vecino con camioneta", "Solo el gestor autorizado tiene permiso para retirar y tratar residuos peligrosos."),
        ("=", "{F} El registro anota 120 litros de aceite usado. Si un tambor de ejemplo contiene 20 litros, ¿cuántos tambores se llenan?", "120//20", "Se divide el volumen total entre la capacidad de cada tambor.", " tambores"),
        ("abc", "{F} Un encargado dice: «el gestor ya vino, no hace falta guardar el comprobante». ¿Qué respuesta es correcta?", "Es incorrecto: el comprobante prueba la entrega y se guarda con el registro", "Es correcto, porque con el registro basta", "Es correcto, si el gestor es conocido", "Sin comprobante no hay evidencia verificable de la entrega."),
        ("abc", "{F} El encargado ambiental no tiene el dato de los litros de aceite del mes y sugiere anotar un número parecido. ¿Qué corresponde?", "No inventar el dato: informar que falta y registrar la cantidad real", "Anotar 100 litros", "Dejar la línea del aceite fuera", "Un registro con datos inventados no sirve y falsea la información."),
        ("=", "{F} Considera que 1 litro de aceite pesa 1 kg en este ejemplo. ¿Cuántos kilos se entregan a gestores autorizados de residuos peligrosos?", "40+120", "Se suman los envases peligrosos y el aceite usado, que van al gestor autorizado.", " kg"),
        ("abc", "En Agropecuaria: ¿por qué «reducir» está primero en la jerarquía de manejo de residuos?", "Porque el residuo que no se genera no necesita manejo ni transporte", "Porque es el más barato de tratar", "Porque siempre se puede reducir a cero", "Reducir evita el problema desde el origen."),
    ],
    ctx=("abc", "Una conocida te pide ayuda para que el registro de residuos de su predio «parezca más ordenado» anotando retiros que no ocurrieron. ¿Qué respondes?", "Que no, porque un registro anota solo lo ocurrido, y que consultarás con un adulto responsable", "Que sí, si después se retiran", "Que sí, pero solo algunos", "Un registro falso pierde valor y puede ocultar un mal manejo."),
    sc=[
        ("En Agropecuaria: ¿cuál es el último recurso de la jerarquía de manejo?", "Eliminar", "Eliminar solo se usa si lo anterior no es posible."),
        ("En el trabajo agrícola: ¿qué documento prueba que el gestor recibió el residuo?", "El comprobante de entrega", "El comprobante da evidencia verificable de la entrega."),
        ("En Agropecuaria: ¿qué es compostar?", "Descomponer de forma controlada residuos orgánicos para obtener abono", "El compostaje valoriza los residuos orgánicos."),
    ],
    op=("Registro de ejemplo del «Predio Demo 3»: guano, 5 toneladas, destino compostaje propio; botellas plásticas, 300 kg, destino reciclador autorizado; envases vacíos de productos de uso sanitario, 25 kg, destino gestor autorizado; aceite usado, 60 litros, destino gestor autorizado. Escribe (a) qué residuos son peligrosos, (b) cuántos kilos de envases y aceite van al gestor (1 litro de aceite pesa 1 kg en este ejemplo), (c) qué acción de la jerarquía es el compostaje, (d) qué documento pides al gestor.",
        "(a) Los envases de productos de uso sanitario y el aceite usado. (b) 25 + 60 = 85 kg. (c) Valorizar. (d) El comprobante de entrega.",
        ["identifica los residuos peligrosos", "suma bien los kilos", "nombra la acción de la jerarquía", "nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["incluir las botellas entre los peligrosos", "no pedir comprobante"],
        "Pregunta: «¿qué residuos pueden dañar a las personas o al ambiente?». Si no responde, pídele que relea el primer párrafo de la clase 1."),
    reinforce="Ordena las acciones de la jerarquía de manejo de residuos de la mejor a la peor y pon un ejemplo inventado de cada una.",
    extend="Explica con un ejemplo por qué el registro de residuos protege al predio ante una revisión.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (listado de ejemplo, inventado). Residuos del mes del «Predio Demo 3»: R1, cajas de cartón; R2, restos de poda; R3, envases vacíos de un producto de uso sanitario; R4, aceite usado de maquinaria; R5, guano de cerdo; R6, botellas plásticas de bebida del personal; R7, trapos con aceite; R8, bolsas rotas de plástico de cobertura. "
     "Categorías: A, orgánico que se puede valorizar; B, inorgánico reciclable; C, residuo peligroso que va a gestor autorizado.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un listado de residuos en papel, a clasificar cada uno con evidencia y a decidir su destino según la legislación vigente.",
    prior=["Sé qué son residuos orgánicos, inorgánicos y peligrosos.", "Sé la jerarquía de manejo de residuos.", "Sé sumar y comparar enteros."],
    explain=[
        "Para clasificar un residuo se hacen tres preguntas: ¿viene de una planta o un animal y se descompone?, ¿es un material como plástico, cartón o vidrio que se puede reciclar?, ¿tuvo contacto con un producto peligroso o es peligroso por sí mismo? Un trapo que tuvo contacto con aceite se vuelve peligroso, aunque el trapo sea de tela. Si hay duda, se trata como peligroso hasta consultar a un técnico.",
        "Cada categoría tiene un destino: los orgánicos se valorizan, por ejemplo con compost; los inorgánicos reciclables van a un reciclador autorizado; los peligrosos se guardan en una bodega cerrada y se entregan a un gestor autorizado con comprobante. Mezclar categorías es el error más común: un residuo peligroso mezclado con uno reciclable contamina todo el grupo y lo vuelve peligroso.",
        f"El análisis deja la clasificación, la evidencia y el destino de cada residuo. Nunca se quema ni se bota a un canal. {EMER} {AVISO}",
    ],
    vocab=[("clasificar", "ordenar un residuo en su categoría"), ("contaminar", "volver peligroso algo limpio por contacto con un residuo peligroso"), ("reciclable", "material que se puede convertir en un material nuevo"), ("bodega de residuos", "lugar cerrado y rotulado donde se guardan residuos"), ("rotular", "poner un letrero que dice qué contiene un lugar o envase")],
    worked=[
        ("Clasificar un residuo", "Un residuo de ejemplo son cáscaras y restos de cosecha. ¿Es orgánico, inorgánico reciclable o peligroso?", ["Vienen de plantas y se descomponen.", "Son residuos orgánicos que se pueden valorizar."], "Orgánico, valorizable"),
        ("Residuo que se contamina", "Un trapo de ejemplo se usó para secar aceite usado. ¿Cómo se clasifica?", ["El aceite usado es peligroso.", "El trapo tuvo contacto con él y también es peligroso."], "Peligroso"),
    ],
    mistakes=[("Clasificar un trapo con aceite como residuo común porque «es de tela».", "El contacto con aceite lo vuelve peligroso.", "Se clasifica según el contacto que tuvo."),
              ("Mezclar el plástico reciclable con envases de productos sanitarios.", "El plástico mezclado se contamina y ya no se puede reciclar.", "Cada categoría se guarda por separado.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué significa que un residuo se contamine por contacto con otro?", "Que se vuelve peligroso al tocar un residuo peligroso", "Que se descompone más rápido", "Que se vuelve reciclable", "La contaminación por contacto vuelve peligroso al residuo limpio."),
        ("abc", "En Agropecuaria: ¿para qué se rotula una bodega de residuos?", "Para indicar qué residuo contiene y evitar mezclas", "Para que el residuo ocupe menos espacio", "Para que el residuo se descomponga", "El rótulo informa y previene errores."),
        ("abc", "En Agropecuaria: ¿qué hacer con un residuo del que se duda si es peligroso?", "Tratarlo como peligroso hasta consultar a un técnico", "Mezclarlo con la basura común", "Quemarlo para salir de la duda", "La duda se resuelve con prudencia y con un técnico."),
        ("abc", "{F} ¿A qué categoría pertenece R2, los restos de poda?", "A, orgánico que se puede valorizar", "B, inorgánico reciclable", "C, peligroso", "Los restos de poda vienen de plantas y se pueden compostar."),
        ("abc", "{F} ¿A qué categoría pertenece R1, las cajas de cartón?", "B, inorgánico reciclable", "A, orgánico valorizable", "C, peligroso", "El cartón es un material reciclable."),
        ("abc", "{F} ¿A qué categoría pertenece R3, los envases vacíos de un producto de uso sanitario?", "C, residuo peligroso", "B, inorgánico reciclable", "A, orgánico valorizable", "Pueden conservar restos de producto y dañar."),
        ("abc", "{F} ¿A qué categoría pertenece R7, los trapos con aceite?", "C, residuo peligroso", "A, orgánico valorizable", "B, inorgánico reciclable", "El trapo tuvo contacto con aceite usado."),
        ("abc", "{F} ¿A qué categoría pertenece R5, el guano de cerdo?", "A, orgánico que se puede valorizar", "C, peligroso", "B, inorgánico reciclable", "El guano es orgánico y puede valorizarse como abono bajo la norma vigente."),
        ("abc", "{F} ¿A qué categoría pertenece R6, las botellas plásticas de bebida?", "B, inorgánico reciclable", "A, orgánico valorizable", "C, peligroso", "El plástico limpio es un material que se puede reciclar."),
        ("abc", "{F} Una compañera dice que R8, las bolsas rotas de plástico de cobertura, deben quemarse porque «ya están rotas». ¿Qué respuesta es correcta?", "Es incorrecto: son plásticos reciclables y no se queman por cuenta propia", "Es correcto, porque rotas no sirven", "Es correcto, si es de noche", "El plástico roto sigue siendo reciclable; quemar contamina."),
        ("abc", "{F} ¿Qué residuos del listado van a gestor autorizado?", "R3, R4 y R7", "Solo R3 y R4", "R3, R4, R7 y R6", "La categoría C incluye envases, aceite usado y trapos con aceite; las botellas son reciclables."),
        ("abc", "{F} Alguien propone guardar R3 y R6 en el mismo saco «para ahorrar espacio». ¿Qué corresponde?", "Rechazarlo: el peligroso contamina al reciclable y se guardan por separado", "Aceptarlo, porque ahorra espacio", "Aceptarlo, si se tapa el saco", "Mezclar categorías vuelve peligroso al grupo."),
        ("abc", "En Agropecuaria: ¿por qué es útil separar los residuos desde donde se generan?", "Porque evita mezclas y facilita el reciclaje y la entrega a gestores", "Porque así se generan más residuos", "Porque se evita rotular", "Separar desde el origen reduce contaminación y trabajo."),
    ],
    ctx=("abc", "Un conocido te muestra una bolsa con restos de poda y envases de productos sanitarios mezclados y te pide que le digas dónde botarla. ¿Qué respondes?", "Que separe los residuos y que los envases se entreguen a un gestor autorizado", "Que la bote entera a la basura", "Que la queme en el patio", "Mezclados, los orgánicos se contaminan; la norma exige separar y entregar los peligrosos al gestor."),
    sc=[
        ("En Agropecuaria: ¿a qué categoría pertenece el cartón limpio?", "Inorgánico reciclable", "El cartón es un material que se puede reciclar."),
        ("En el trabajo agrícola: ¿qué pasa si se mezcla un residuo peligroso con uno reciclable?", "El grupo se contamina y se vuelve peligroso", "Mezclar categorías pierde el material reciclable."),
        ("En Agropecuaria: ¿qué se hace con los residuos peligrosos?", "Se entregan a un gestor autorizado con comprobante", "El gestor autorizado trata los residuos peligrosos."),
    ],
    op=("Listado de ejemplo del «Predio Demo 4»: S1, aceite usado; S2, restos de hortalizas; S3, bidones plásticos limpios; S4, envases de un producto sanitario vacío; S5, guano de aves; S6, cajas de cartón. Categorías: A, orgánico valorizable; B, inorgánico reciclable; C, peligroso. Escribe (a) la categoría de cada residuo, (b) cuántos van a gestor autorizado, (c) un riesgo de mezclar S1 con S3, (d) qué haces si ves humo en el acopio.",
        "(a) S1 C; S2 A; S3 B; S4 C; S5 A; S6 B. (b) 2 residuos: S1 y S4. (c) Que el aceite contamine los bidones y ya no se puedan reciclar. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["clasifica bien los seis residuos", "cuenta los peligrosos", "explica un riesgo de mezclar", "no se acerca al humo y avisa"],
        ["hoja con las cuatro respuestas"],
        ["clasificar el cartón como peligroso", "proponer apagar el fuego sin formación"],
        "Pregunta: «¿qué residuos pueden dañar a personas o ambiente?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Clasifica cuatro residuos inventados de un campo en las categorías A, B y C y escribe el destino de cada uno.",
    extend="Explica con un ejemplo por qué una duda se resuelve tratando el residuo como peligroso.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). El «Predio Demo» genera en un mes: 6.000 kg de residuos orgánicos, 1.000 kg de plásticos y cartones reciclables y 200 kg de residuos peligrosos. "
     "De los orgánicos se compostan 4.600 kg; de los reciclables se envían a un reciclador 800 kg. Los peligrosos van a gestor autorizado. El camión del gestor retira como máximo 100 kg por viaje.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular el porcentaje de residuos valorizados o reciclados y el número de retiros necesarios.",
    prior=["Sé la jerarquía de manejo de residuos.", "Sé multiplicar y dividir enteros.", "Sé calcular porcentajes enteros."],
    explain=[
        "Para saber si un predio maneja bien sus residuos se calculan indicadores. El total generado es la suma de las categorías. El porcentaje de valorización es lo valorizado o reciclado dividido por el total generado y multiplicado por 100. Un porcentaje mayor indica que menos residuos terminan eliminados. El indicador sirve para comparar meses y detectar si el predio mejora.",
        "También se calcula la logística: el número de viajes que necesita un gestor es el total a retirar dividido por lo que lleva el camión en cada viaje, y si no sale exacto se redondea hacia arriba. Con esos datos se planifica el espacio del acopio y se evita que se junten residuos peligrosos durante demasiado tiempo. Todo se registra con fecha y cantidad.",
        f"Los números son de ejemplo: los reales dependen del predio y de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("total generado", "suma de todos los residuos de un período"), ("porcentaje de valorización", "valorizado o reciclado dividido por el total, por 100"), ("logística", "organización de los retiros y los traslados"), ("acopio", "lugar donde se guardan los residuos antes de su retiro"), ("indicador", "número que resume cómo va un proceso")],
    worked=[
        ("Porcentaje valorizado", "Un predio de ejemplo genera 500 kg de residuos y valoriza o recicla 300 kg. ¿Qué porcentaje es?", ["Se divide 300 entre 500, que son 3 quintos.", "3 quintos son 60 de cada 100."], "60 %"),
        ("Viajes", "Hay que retirar 250 kg y el camión lleva 100 kg por viaje. ¿Cuántos viajes?", ["250 entre 100 da 2 y sobran 50.", "Se redondea hacia arriba."], "3 viajes"),
    ],
    mistakes=[("Contar como valorizados los residuos que solo se guardaron.", "Guardar no es valorizar ni reciclar.", "Solo cuentan los que se compostaron, reciclaron o entregaron para su uso útil."),
              ("Redondear hacia abajo los viajes necesarios.", "Quedarían residuos sin retirar.", "Se redondea hacia arriba.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el total generado de residuos?", "La suma de todas las categorías de residuos de un período", "Solo los residuos peligrosos", "Solo lo que se recicla", "El total suma todas las categorías."),
        ("abc", "En Agropecuaria: ¿qué indica el porcentaje de valorización?", "Qué parte del total se valorizó o recicló", "Cuánto cuesta cada residuo", "Cuántas veces se retiró el camión", "El porcentaje relaciona lo valorizado con el total."),
        ("abc", "En Agropecuaria: ¿qué es el acopio de residuos?", "El lugar donde se guardan antes de su retiro", "El camión que los retira", "El documento que los registra", "El acopio es un lugar; el camión y el documento son otros elementos."),
        ("=", "{F} ¿Cuántos kilos de residuos se generaron en total en el mes?", "6000+1000+200", "Se suman las tres categorías de residuos.", " kg"),
        ("=", "{F} ¿Cuántos kilos se valorizaron o reciclaron en total (compostados y enviados al reciclador)?", "4600+800", "Se suman lo compostado y lo enviado al reciclador.", " kg"),
        ("=", "{F} ¿Qué porcentaje de lo generado en total se valorizó o recicló?", "(4600+800)*100//(6000+1000+200)", "Se divide lo valorizado entre el total generado y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos viajes necesita el gestor para retirar los residuos peligrosos?", "200//100", "Se divide el total peligroso entre lo que lleva el camión por viaje.", " viajes"),
        ("=", "{F} Si el mes siguiente los residuos peligrosos suben a 300 kg, ¿cuántos viajes hacen falta?", "300//100", "Se divide el total peligroso entre los 100 kg que lleva cada viaje.", " viajes"),
        ("=", "{F} ¿Cuántos kilos de residuos orgánicos no se compostaron?", "6000-4600", "Se resta lo compostado al total orgánico.", " kg"),
        ("abc", "{F} Una compañera cuenta como valorizados los 1.400 kg de orgánicos que «están guardados en un patio». ¿Cuál es el error?", "Guardar no es valorizar: solo cuenta lo compostado o usado", "Ninguno, porque están dentro del predio", "El error es sumar los orgánicos", "Valorizar es darle un uso útil, no guardarlo."),
        ("abc", "{F} Los residuos peligrosos se acumulan seis meses porque el gestor «viene cuando puede». ¿Qué corresponde?", "Coordinar retiros más seguidos y controlar el acopio, según la norma vigente", "Dejarlos acumular, porque no pasa nada", "Quemarlos para ahorrar espacio", "El acopio de peligrosos tiene condiciones y plazos que fija la norma."),
        ("abc", "{F} Si el mes siguiente se compostan 5.000 kg en vez de 4.600, ¿cómo cambia el porcentaje de valorización?", "Sube", "Baja", "Se mantiene", "Más residuos valorizados con el mismo total elevan el porcentaje."),
        ("abc", "En Agropecuaria: ¿por qué conviene calcular el porcentaje de valorización mes a mes?", "Para ver si el predio mejora o empeora y corregir a tiempo", "Para saber cuánto pesa el camión", "Para evitar registrar los residuos", "Comparar meses muestra tendencias y permite corregir."),
    ],
    ctx=("abc", "Un conocido te pregunta si su predio «lo está haciendo bien con los residuos» y te pasa tres números sueltos. ¿Qué respondes?", "Que necesitas el total, lo valorizado y lo peligroso para calcular indicadores, y que la evaluación la hace un técnico", "Que seguro está bien", "Que seguro está mal", "Sin datos completos y sin un técnico no se puede evaluar."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula el porcentaje de valorización?", "Lo valorizado entre el total, por 100", "El porcentaje compara lo valorizado con el total."),
        ("En el trabajo agrícola: ¿qué se hace si los viajes no salen exactos?", "Se redondea hacia arriba", "Si no, quedarían residuos sin retirar."),
        ("En Agropecuaria: ¿qué cuenta como valorizado?", "Lo compostado, reciclado o con otro uso útil", "Guardar no da un uso útil."),
    ],
    op=("Datos de ejemplo del «Predio Demo 5»: en un mes se generaron 3.000 kg de orgánicos, 500 kg de reciclables y 100 kg de peligrosos; se compostaron 2.200 kg y se enviaron 500 kg al reciclador; el camión del gestor retira como máximo 50 kg por viaje. Escribe (a) el total generado, (b) el porcentaje valorizado o reciclado, (c) los viajes para retirar los peligrosos, (d) qué haces con los residuos peligrosos mientras esperas el retiro.",
        "(a) 3.000 + 500 + 100 = 3.600 kg. (b) (2.200 + 500) × 100 ÷ 3.600 = 75 %. (c) 100 ÷ 50 = 2 viajes. (d) Se guardan en una bodega cerrada y rotulada, y los maneja personal autorizado.",
        ["calcula el total", "calcula el porcentaje", "calcula los viajes", "describe el acopio seguro"],
        ["hoja con las cuatro respuestas"],
        ["no sumar las tres categorías", "calcular mal los viajes", "dejar los peligrosos al aire libre"],
        "Pregunta: «¿qué suma da el total generado?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el porcentaje de valorización de un mes inventado con 800 kg generados y 600 kg valorizados.",
    extend="Explica con un ejemplo por qué es importante coordinar los retiros de residuos peligrosos.",
)
