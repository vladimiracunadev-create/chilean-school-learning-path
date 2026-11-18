"""Forestal TP 3.º y 4.º medio: OAE-04 (intervención de un rodal según plan de manejo: vocabulario, documentos, planificación y costos). Solo conceptos y cálculos en papel; sin procedimientos de volteo, desrame, madereo ni carguío."""
from __future__ import annotations

from tp_fore_common import AVISO, EMER, build

O4 = "TP-FORE-3y4-OAE-04"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Faena Demo, rodal de 12 ha. Etapas del plan: volteo, desrame, madereo y carguío. Jornadas programadas de ejemplo: volteo y desrame, 5; madereo, 3; carguío, 2. "
     "Peligros anotados: caída de árboles y de ramas, trozas que ruedan, máquinas en movimiento, ruido, polvo y terreno con pendiente. "
     "El plan define una zona de exclusión: un área donde solo puede estar el personal autorizado de la etapa en curso.")
build(
    O4, 1, F,
    use="Aprenderé el vocabulario de las etapas de una faena forestal (volteo, desrame, madereo y carguío), sus peligros principales y las reglas generales de seguridad, sin aprender a ejecutarlas.",
    prior=["Sé qué es un plan de manejo.", "Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé calcular porcentajes simples."],
    explain=[
        "Intervenir un rodal es hacer en él los trabajos que fija el plan de manejo. En una faena forestal se distinguen etapas con nombre propio. El volteo es la etapa en que los árboles son derribados. El desrame es el retiro de las ramas de un árbol ya caído. El madereo es el traslado de las trozas, que son los tramos de tronco, hasta la cancha de acopio, el lugar donde se juntan y ordenan antes de cargarlas. El carguío es la carga de las trozas en camiones.",
        "Estas son de las tareas más peligrosas del sector. Los peligros principales son la caída de árboles y ramas, las trozas que ruedan, las máquinas en movimiento, el ruido y el terreno con pendiente. Para controlarlos se usan la jerarquía de controles, la zona de exclusión, la señalización, la coordinación entre etapas para que no coincidan personas en una misma zona y los equipos de protección personal como última barrera. Los ejecutan solo personas formadas, certificadas y autorizadas.",
        f"Este cuaderno no explica cómo se ejecuta ninguna de estas tareas ni habilita para hacerlas. {EMER} {AVISO}",
    ],
    vocab=[("volteo", "etapa en que los árboles son derribados"), ("desrame", "retiro de las ramas de un árbol ya caído"), ("troza", "tramo de tronco de un largo definido"), ("madereo", "traslado de las trozas hasta la cancha de acopio"), ("cancha de acopio", "lugar donde se juntan y ordenan las trozas antes de cargarlas"), ("carguío", "carga de las trozas en camiones"), ("zona de exclusión", "área donde solo puede estar el personal autorizado de la etapa en curso")],
    worked=[
        ("Reconocer la etapa", "En una faena de ejemplo, un equipo traslada trozas desde donde quedaron hasta la cancha de acopio. ¿Cómo se llama esa etapa?", ["Trasladar trozas hasta la cancha de acopio es la definición de una etapa.", "Esa etapa se llama madereo."], "Madereo"),
        ("Porcentaje de una etapa", "Una faena de ejemplo programa 20 jornadas y 5 son de carguío. ¿Qué porcentaje es?", ["5 ÷ 20 son 25 de cada 100.", "Es el 25 % de las jornadas."], "25 %"),
    ],
    mistakes=[("Creer que conocer el vocabulario de las etapas habilita para participar en una faena.", "Las etapas las ejecuta personal formado, certificado y autorizado.", "Aprende aquí los conceptos y deja la ejecución a personal autorizado."),
              ("Entrar «un momento» a la zona de exclusión para mirar de cerca.", "En esa zona solo está el personal autorizado de la etapa en curso.", "Observa desde fuera, con autorización y acompañado de un adulto responsable.")],
    T=[
        ("abc", "En Forestal: ¿qué es el volteo en una faena?", "La etapa en que los árboles son derribados", "La etapa en que las trozas se trasladan a la cancha de acopio", "La etapa en que las trozas se cargan en camiones", "El volteo es el derribo; el traslado es el madereo y la carga en camión es el carguío."),
        ("abc", "En Forestal: ¿qué es el madereo?", "El traslado de las trozas hasta la cancha de acopio", "El retiro de las ramas de un árbol caído", "La carga de las trozas en camiones", "El madereo mueve las trozas; retirar ramas es desrame y cargar camiones es carguío."),
        ("abc", "En Forestal: ¿qué es una cancha de acopio?", "Un lugar donde se juntan y ordenan las trozas antes de cargarlas", "Un sector donde se hacen caer los árboles", "Una oficina donde se guardan los planos de la faena", "La cancha de acopio es una zona de almacenamiento temporal de trozas."),
        ("=", "{F} ¿Cuántas jornadas programadas tiene la faena en total?", "5+3+2", "Se suman las jornadas de las tres etapas programadas.", " jornadas"),
        ("=", "{F} ¿Qué porcentaje de las jornadas programadas corresponde al madereo?", "3*100//(5+3+2)", "Se divide las jornadas de madereo entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «trozas que ruedan»?", "Que una persona sea golpeada o atrapada por una troza en movimiento", "La troza que está almacenada en la cancha", "Que la faena se atrase un día", "El riesgo es la posibilidad de daño a una persona; la troza es la fuente del peligro."),
        ("abc", "{F} ¿Qué es la zona de exclusión del plan?", "Un área donde solo puede estar el personal autorizado de la etapa en curso", "Un área donde se guarda el combustible de las máquinas", "Un área abierta para las visitas de la faena", "La zona de exclusión limita el acceso por el peligro de la etapa."),
        ("abc", "{F} Una estudiante de visita pregunta si puede entrar a la zona de exclusión «solo a mirar». ¿Qué respuesta es correcta?", "No: solo entra el personal autorizado de la etapa en curso, y ella mira desde fuera con un adulto responsable", "Sí, si usa casco", "Sí, si va acompañada de un trabajador de la faena", "El casco y la compañía no reemplazan la autorización ni el control del acceso."),
        ("abc", "Durante una visita de ejemplo, un árbol cae sobre un trabajador y queda atrapado. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a levantar el tronco", "Intentar sacar al trabajador tirándolo de la ropa", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "{F} Cerrar el acceso a la zona de exclusión con una barrera física es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla", "De EPP, porque protege a las personas", "Una barrera modifica el lugar y no depende de que cada persona obedezca."),
        ("abc", "{F} ¿Qué ventaja tiene programar las etapas para que no coincidan en la misma zona?", "Reduce la cantidad de personas expuestas al mismo tiempo a los peligros", "Aumenta la velocidad de todas las máquinas", "Elimina la necesidad de la zona de exclusión", "Coordinar etapas disminuye la exposición simultánea, pero no reemplaza la zona de exclusión."),
        ("=", "{F} Si las jornadas de la ficha cuestan $250.000 en volteo y desrame, $150.000 en madereo y $300.000 en carguío (valores de ejemplo, por jornada), ¿cuánto cuesta la faena?", "5*250000+3*150000+2*300000", "Se multiplica cada etapa por su costo por jornada y se suman los resultados.", " pesos"),
        ("abc", "{F} Se propone adelantar el madereo sin esperar a que termine el desrame de la misma zona. ¿Qué problema aparece?", "Se mezclarían etapas en una misma zona, lo que aumenta la exposición y no respeta el plan", "Ninguno, porque ahorrar tiempo siempre es mejor", "Que se pagaría menos por jornada", "Mezclar etapas en una zona aumenta los peligros y contradice la coordinación del plan."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por ayudar a «juntar trozas» en un campo vecino los fines de semana, sin contrato ni autorización. ¿Qué respondes?", "Que no, porque esas tareas exigen personal autorizado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si trabajas con guantes", "Que sí, si es por pocas horas", "Sin autorización, formación ni plan de seguridad, el EPP o la duración no hacen segura la tarea."),
    sc=[
        ("En Forestal: ¿qué es el desrame?", "El retiro de las ramas de un árbol ya caído", "Desrame es retirar las ramas del árbol caído."),
        ("¿Quién puede estar en la zona de exclusión?", "Solo el personal autorizado de la etapa en curso", "La zona de exclusión restringe el acceso por el peligro."),
        ("¿Qué haces ante un accidente en una faena?", "No acercarme, avisar a un adulto responsable y a emergencias", "No se interviene sin formación porque se puede agravar el daño."),
    ],
    op=("Ficha de ejemplo: «Faena Muestra», 9 ha. Jornadas programadas de ejemplo: volteo y desrame, 6; madereo, 3; carguío, 3. Peligros anotados: caída de ramas y máquinas en movimiento. Escribe (a) el total de jornadas y el porcentaje que es madereo, (b) un control administrativo para las máquinas en movimiento, (c) un control de ingeniería para la zona de exclusión, (d) por qué conocer las etapas no te habilita para trabajar en una faena.",
        "(a) 6 + 3 + 3 = 12 jornadas; madereo es 3 ÷ 12 = 25 %. (b) Un horario y una regla de que las máquinas se mueven solo cuando la zona está despejada, comunicado por la jefatura. (c) Una barrera física que cierre el acceso a la zona. (d) Porque esas tareas las ejecuta personal formado, certificado y autorizado, con norma vigente.",
        ["calcula el total de jornadas", "propone un control administrativo", "propone un control de ingeniería", "explica que no basta con conocer el vocabulario"],
        ["hoja con las cuatro respuestas"],
        ["confundir las etapas", "proponer solo el EPP", "creer que el vocabulario habilita para la tarea"],
        "Pregunta: «¿quién ejecuta estas etapas?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe en orden las cuatro etapas de una faena y una definición de una línea de cada una.",
    extend="Explica con un ejemplo por qué la zona de exclusión es un control más efectivo que pedir a todos que tengan cuidado.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (documentos de una faena de ejemplo, inventados). Plan de cosecha del rodal 5: 10 ha, volumen autorizado de ejemplo de 1.200 m³. Mapa de la faena (descrito): al norte, el sector de intervención; al sur, la cancha de acopio; al este, el camino de salida; al oeste, la franja de protección de un curso de agua, que no se interviene. "
     "Registro de producción del día 3: 30 trozas del producto P1 (volumen medio de ejemplo, 2 m³ por troza) y 40 trozas del producto P2 (1 m³ por troza). Volumen acumulado hasta el día 2: 500 m³. "
     "Las guías de despacho de ese día suman 60 trozas despachadas.")
build(
    O4, 2, F,
    use="Aprenderé los documentos de una faena forestal (plan de cosecha, mapa de la faena, registro de producción y guía de despacho), el concepto de volumen autorizado y los roles que intervienen.",
    prior=["Sé qué son las etapas de una faena.", "Sé qué es un plan de manejo.", "Sé multiplicar, sumar y calcular porcentajes simples."],
    explain=[
        "La faena se organiza con documentos. El plan de cosecha deriva del plan de manejo y programa dónde, cuándo y cuánto volumen se interviene. El mapa de la faena muestra los sectores, la cancha de acopio, el camino de salida, la zona de exclusión y las áreas protegidas. El registro de producción anota cada día cuántas trozas y de qué producto se obtuvieron; un producto es un tipo de troza clasificada por su largo, su diámetro y su uso. La guía de despacho acompaña la carga y dice qué se transporta, cuánto, desde dónde y hacia dónde.",
        "El volumen autorizado es el máximo que el plan permite intervenir, y nunca se supera: al alcanzarlo se detiene el trabajo y, si hace falta más, se pide modificar el plan. Un registro honesto refleja lo realmente producido y se concilia con las guías de despacho y con el inventario de la cancha de acopio: lo producido menos lo despachado debe coincidir con lo que queda en cancha.",
        f"Cada rol cumple su función: el jefe de faena organiza el trabajo, el prevencionista asesora en riesgos, el personal autorizado ejecuta y la autoridad forestal fiscaliza. {EMER} {AVISO}",
    ],
    vocab=[("plan de cosecha", "documento que programa dónde, cuándo y cuánto volumen se interviene"), ("mapa de la faena", "mapa con sectores, cancha de acopio, camino de salida, zona de exclusión y áreas protegidas"), ("producto", "tipo de troza clasificada por largo, diámetro y uso"), ("registro de producción", "documento que anota cada día cuántas trozas de cada producto se obtuvieron"), ("guía de despacho", "documento que acompaña la carga e indica qué, cuánto, desde dónde y hacia dónde se transporta"), ("volumen autorizado", "máximo volumen que el plan permite intervenir")],
    worked=[
        ("Volumen de un registro", "Un registro de ejemplo anota 20 trozas de 3 m³ y 10 trozas de 2 m³. ¿Cuál es el volumen del día?", ["20 × 3 = 60 m³ y 10 × 2 = 20 m³.", "60 + 20 = 80 m³."], "80 m³"),
        ("Cuánto queda por intervenir", "Un plan de ejemplo autoriza 900 m³ y se llevan 350 m³. ¿Cuánto volumen queda autorizado?", ["Se resta lo hecho al volumen autorizado.", "900 − 350 = 550."], "550 m³"),
    ],
    mistakes=[("Seguir trabajando después de alcanzar el volumen autorizado «porque queda madera».", "El plan fija un máximo que no se puede superar.", "Al llegar al máximo se detiene el trabajo y se pide modificar el plan si hace falta."),
              ("Anotar en el registro lo que «debería» haberse producido y no lo real.", "Un registro falso impide controlar el plan y la producción.", "Anota solo lo realmente producido, con fecha y responsable.")],
    T=[
        ("abc", "En Forestal: ¿qué es una troza?", "Un tramo de tronco de un largo definido", "Una rama delgada que se retira del árbol", "La raíz principal del árbol", "La troza es un tramo del tronco; las ramas y las raíces son otras partes."),
        ("abc", "En Forestal: ¿qué es un plan de cosecha?", "Un documento que programa dónde, cuándo y cuánto volumen se interviene", "Un listado de los pagos del personal", "Un registro de los accidentes del año", "El plan de cosecha ordena la intervención dentro de lo que autoriza el plan de manejo."),
        ("abc", "En Forestal: ¿para qué sirve una guía de despacho?", "Para acompañar la carga e indicar qué se transporta, cuánto, desde dónde y hacia dónde", "Para autorizar el uso de una máquina", "Para fijar el precio de venta de la madera", "La guía identifica la carga en tránsito; no autoriza máquinas ni fija precios."),
        ("=", "{F} ¿Cuántos m³ suman las trozas del producto P1 del día 3?", "30*2", "Se multiplica el número de trozas por el volumen medio de cada una.", " m³"),
        ("=", "{F} ¿Cuántos m³ tiene el registro de producción del día 3?", "30*2+40*1", "Se suman los volúmenes de los dos productos.", " m³"),
        ("=", "{F} ¿Cuál es el volumen acumulado al terminar el día 3?", "500+30*2+40*1", "Se suma el volumen del día 3 al acumulado hasta el día 2.", " m³"),
        ("=", "{F} ¿Qué porcentaje del volumen autorizado se ha cosechado al terminar el día 3?", "(500+30*2+40*1)*100//1200", "Se divide lo cosechado entre el volumen autorizado y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué documento de la ficha muestra dónde está la zona de intervención y la franja que no se interviene?", "El mapa de la faena", "La guía de despacho", "El registro de producción", "El mapa muestra sectores y áreas protegidas; la guía y el registro informan cantidades."),
        ("abc", "{F} ¿Qué rol asesora en prevención de riesgos y revisa las condiciones de seguridad de la faena?", "El prevencionista de riesgos", "El transportista que retira la carga", "El comprador de las trozas", "El prevencionista asesora en riesgos; los otros roles tienen funciones de transporte o compra."),
        ("abc", "{F} ¿Qué corresponde cuando el volumen acumulado alcance el volumen autorizado?", "Detener la intervención y pedir la modificación del plan si se necesita más", "Seguir mientras queden árboles en el sector", "Pedir permiso de palabra al transportista", "El volumen autorizado es un máximo; para exceder se modifica el plan."),
        ("=", "{F} Si cada día se produce el mismo volumen del día 3, ¿cuántos días más hacen falta para alcanzar el volumen autorizado?", "(1200-(500+30*2+40*1))//(30*2+40*1)", "Se resta lo cosechado al volumen autorizado y se divide por el volumen de cada día.", " días"),
        ("abc", "{F} El registro del día informa 70 trozas y las guías de despacho suman 60 trozas despachadas. ¿Es una contradicción?", "No necesariamente: pueden quedar 10 trozas en la cancha de acopio, lo que se confirma con su inventario", "Sí, hay un error en las guías", "Sí, las 10 trozas se perdieron", "Producidas menos despachadas debe coincidir con lo que queda en cancha."),
        ("abc", "{F} Un jefe pide anotar en el registro más trozas que las producidas para «cumplir la meta». ¿Qué corresponde?", "No alterar el registro y avisar a un adulto responsable", "Anotar el número que pide el jefe", "Anotar la mitad de la diferencia", "Un registro falso impide controlar el plan; ante la presión se consulta a un adulto responsable."),
    ],
    ctx=("abc", "Una persona te pide una copia del registro de producción de la faena de ejemplo para venderla a otra empresa. ¿Qué haces?", "No entregarla sin autorización y consultar a un adulto responsable, porque es información de la empresa", "Entregarla si te pagan", "Entregarla si no tiene fechas", "Los registros de una empresa se manejan con autorización; no se entregan por pago."),
    sc=[
        ("En Forestal: ¿qué es un producto en una faena?", "Un tipo de troza clasificada por largo, diámetro y uso", "El producto se define por las características de la troza."),
        ("¿Qué pasa al alcanzar el volumen autorizado?", "Se detiene la intervención", "El plan fija un máximo que no se puede superar."),
        ("¿Qué documento acompaña la carga de un camión?", "La guía de despacho", "La guía informa qué se transporta, cuánto y hacia dónde."),
    ],
    op=("Ficha de ejemplo: faena «Muestra 2», volumen autorizado de ejemplo de 800 m³. Registro del día 2: 20 trozas del producto P1 (3 m³ por troza) y 30 trozas del producto P2 (1 m³ por troza). Acumulado hasta el día 1: 200 m³. Escribe (a) el volumen del día 2, (b) el acumulado al terminar el día 2, (c) cuánto volumen queda autorizado, (d) qué documento confirmaría cuántas trozas salieron de la faena.",
        "(a) 20 × 3 + 30 × 1 = 90 m³. (b) 200 + 90 = 290 m³. (c) 800 − 290 = 510 m³. (d) Las guías de despacho, que se concilian con el inventario de la cancha de acopio.",
        ["calcula el volumen del día", "calcula el acumulado", "calcula lo que queda autorizado", "nombra el documento correcto"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el volumen medio de cada troza", "no sumar el acumulado", "confundir la guía con el registro"],
        "Pregunta: «¿qué documento acompaña a la carga?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un registro de producción con dos productos y calcula su volumen.",
    extend="Explica con un ejemplo por qué la guía de despacho y el registro de producción no son lo mismo.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado; los rendimientos y capacidades son de ejemplo). En la cancha de acopio hay 480 m³ de trozas para trasladar y despachar. "
     "Rendimientos por jornada, un solo equipo por etapa: volteo y desrame, 80 m³; madereo, 60 m³; carguío, 120 m³. "
     "Un camión de ejemplo tiene capacidad de carga máxima de 30 m³, según el documento del vehículo; cada viaje de ida y vuelta demora 4 horas. Costo de un viaje: $90.000 (ejemplo).")
build(
    O4, 3, F,
    use="Aprenderé a analizar una faena en papel: rendimientos por etapa, cuello de botella, capacidad de carga de un camión y número de viajes.",
    prior=["Sé qué son las etapas de una faena y la cancha de acopio.", "Sé dividir números enteros.", "Sé calcular costos con multiplicaciones."],
    explain=[
        "Las etapas de una faena forman una cadena: cada una recibe lo que dejó la anterior. El rendimiento de una etapa es el volumen que procesa por jornada. La etapa más lenta, la que necesita más jornadas para el mismo volumen, se llama cuello de botella, porque limita el ritmo de toda la cadena: acelerar otra etapa no sirve de mucho si el cuello de botella sigue igual. Por ejemplo, si una etapa procesa 30 m³ por jornada y otra 90, la primera es la que marca el ritmo.",
        "La capacidad de carga de un camión es el máximo de carga que puede llevar según el documento del vehículo. No se supera nunca: sobrecargar compromete la seguridad y es una infracción. El número de viajes se calcula dividiendo el volumen por la capacidad y, si no es exacto, se redondea hacia arriba, porque un viaje parcial igual es un viaje. Todos estos cálculos son de planificación; el transporte y la carga los hace personal autorizado.",
        f"En una faena real los datos los entregan el plan, el fabricante y la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("cuello de botella", "etapa más lenta de una cadena, que limita el ritmo de todas"), ("capacidad de carga", "máximo de carga que un vehículo puede llevar según su documento"), ("viaje de ida y vuelta", "recorrido completo de salida y regreso del camión"), ("rendimiento por jornada", "volumen que procesa una etapa en un día de trabajo")],
    worked=[
        ("Jornadas de una etapa", "Una etapa de ejemplo procesa 40 m³ por jornada y hay 200 m³. ¿Cuántas jornadas necesita?", ["Se divide el volumen entre el rendimiento.", "200 ÷ 40 = 5."], "5 jornadas"),
        ("Viajes de un camión", "Hay 100 m³ para despachar en un camión de ejemplo de 25 m³ por viaje. ¿Cuántos viajes hacen falta?", ["Se divide el volumen entre la capacidad.", "100 ÷ 25 = 4."], "4 viajes"),
    ],
    mistakes=[("Acelerar una etapa que no es el cuello de botella para terminar antes.", "El ritmo de la cadena sigue limitado por la etapa más lenta.", "Identifica primero el cuello de botella."),
              ("Cargar más que la capacidad del camión para ahorrar un viaje.", "Sobrecargar compromete la seguridad y es una infracción.", "Programa los viajes necesarios con la capacidad indicada.")],
    T=[
        ("abc", "En Forestal: ¿qué es un cuello de botella en una faena?", "La etapa más lenta, que limita el ritmo de toda la cadena", "La etapa más peligrosa de la faena", "La etapa que más cuesta en pesos", "El cuello de botella se define por la velocidad, no por el peligro ni el costo."),
        ("abc", "En Forestal: ¿qué es la capacidad de carga de un camión?", "El máximo de carga que puede llevar según el documento del vehículo", "Todo lo que cabe en la caja si se aprietan las trozas", "La cantidad de combustible que lleva", "La capacidad de carga es un límite fijado y documentado."),
        ("abc", "En Forestal: ¿por qué no se debe exceder la capacidad de carga de un camión?", "Porque se compromete la seguridad y se infringe la norma", "Porque se pierde la guía de despacho", "Porque las trozas se secan más rápido", "La sobrecarga es un riesgo y una infracción."),
        ("=", "{F} ¿Cuántas jornadas necesita la etapa de volteo y desrame para 480 m³?", "480//80", "Se divide el volumen entre el rendimiento por jornada.", " jornadas"),
        ("=", "{F} ¿Cuántas jornadas necesita la etapa de madereo para 480 m³?", "480//60", "Se divide el volumen entre el rendimiento por jornada.", " jornadas"),
        ("=", "{F} ¿Cuántas jornadas necesita la etapa de carguío para 480 m³?", "480//120", "Se divide el volumen entre el rendimiento por jornada.", " jornadas"),
        ("abc", "{F} ¿Cuál es el cuello de botella de la cadena?", "El madereo, con 8 jornadas", "El volteo y desrame, con 6 jornadas", "El carguío, con 4 jornadas", "La etapa que necesita más jornadas para el mismo volumen es la más lenta."),
        ("=", "{F} ¿Cuántos viajes hacen falta para despachar los 480 m³?", "480//30", "Se divide el volumen entre la capacidad de carga del camión.", " viajes"),
        ("=", "{F} ¿Cuántas horas de camión se necesitan en total para esos viajes?", "(480//30)*4", "Se multiplican los viajes por las horas de cada viaje.", " horas"),
        ("=", "{F} Con dos camiones iguales trabajando a la vez y jornadas de 8 horas, ¿cuántas jornadas se necesitan?", "((480//30)*4)//2//8", "Se reparten las horas de camión entre los dos y se dividen entre las horas de una jornada.", " jornadas"),
        ("abc", "{F} Se agrega un segundo equipo de madereo y el madereo baja a 4 jornadas. ¿Cuál pasa a ser el cuello de botella?", "El volteo y desrame, con 6 jornadas", "El madereo, que sigue siendo el más lento", "Ya no existe ningún cuello de botella", "Con madereo en 4, el volteo y desrame con 6 jornadas es la etapa más lenta."),
        ("=", "{F} ¿Cuánto cuestan en pesos todos los viajes?", "(480//30)*90000", "Se multiplican los viajes por el costo de cada uno.", " pesos"),
        ("abc", "{F} Para reducir viajes, un conductor propone cargar 36 m³ en lugar de 30 m³. ¿Qué respuesta es correcta?", "No: no se supera la capacidad indicada y se programan los viajes necesarios", "Sí, si las trozas quedan bien aseguradas", "Sí, si el camino es corto", "La capacidad de carga es un límite documentado que no se excede por ninguna razón."),
    ],
    ctx=("abc", "Durante una visita, un conductor te invita a subir a la cabina para «ver cómo se carga». ¿Qué respondes?", "Que no, porque estás fuera de las zonas de trabajo autorizadas, y que lo consultarás con un adulto responsable", "Que sí, si te pones el cinturón", "Que sí, si va despacio", "Las zonas de carga son de acceso restringido a personal autorizado."),
    sc=[
        ("En Forestal: ¿cómo se obtienen las jornadas de una etapa?", "Dividiendo el volumen entre el rendimiento por jornada", "Así se sabe cuántos días de trabajo se necesitan."),
        ("En el trabajo forestal: ¿qué es un cuello de botella?", "La etapa más lenta de la cadena", "Limita el ritmo de toda la cadena."),
        ("¿Se puede superar la capacidad de carga de un camión?", "No, nunca", "La sobrecarga compromete la seguridad y es una infracción."),
    ],
    op=("Ficha de ejemplo (datos de ejemplo): 360 m³ de trozas. Rendimientos por jornada: volteo y desrame, 90 m³; madereo, 40 m³; carguío, 60 m³. Camión de capacidad máxima 20 m³ por viaje; cada viaje demora 3 horas y cuesta $60.000. Escribe (a) las jornadas de cada etapa, (b) cuál es el cuello de botella, (c) cuántos viajes hacen falta y su costo total, (d) por qué no conviene cargar más que la capacidad.",
        "(a) Volteo y desrame: 360 ÷ 90 = 4; madereo: 360 ÷ 40 = 9; carguío: 360 ÷ 60 = 6. (b) El madereo, con 9 jornadas. (c) 360 ÷ 20 = 18 viajes; 18 × 60.000 = 1.080.000 pesos. (d) Porque compromete la seguridad y es una infracción.",
        ["calcula jornadas por etapa", "identifica el cuello de botella", "calcula viajes y costo", "justifica el límite de carga"],
        ["hoja con las cuatro respuestas"],
        ["no dividir por el rendimiento", "elegir la etapa más rápida como cuello", "proponer sobrecargar"],
        "Pregunta: «¿cuál etapa necesita más jornadas?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres rendimientos por jornada y un volumen, y calcula cuál etapa es el cuello de botella.",
    extend="Explica con un ejemplo por qué acelerar una etapa que no es el cuello de botella no acorta el plazo total.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (costos de ejemplo, inventados). Faena Demo: 480 m³ de trozas vendibles, obtenidos de un volumen estimado de 500 m³. Volumen autorizado por el plan: 600 m³. "
     "Costo por m³ de ejemplo: volteo y desrame, $3.000; madereo, $2.000; carguío, $1.000; transporte, $4.000. Precio de venta de ejemplo: $14.000 por m³ de troza vendible.")
build(
    O4, 4, F,
    use="Aprenderé a calcular en papel el costo unitario, el margen, la utilidad, el aprovechamiento y el cumplimiento del plan de una faena, y a no recortar costos de seguridad.",
    prior=["Sé calcular ingreso menos costo.", "Sé calcular porcentajes simples.", "Sé qué es el volumen autorizado."],
    explain=[
        "El costo unitario es el costo de producir cada metro cúbico: se obtiene sumando los costos por m³ de todas las etapas. El margen por m³ es el precio de venta menos el costo unitario. La utilidad total es el margen por el volumen vendido, o el ingreso menos el costo total. El aprovechamiento es el porcentaje del volumen estimado que se convierte en trozas vendibles; la parte que no se aprovecha se llama merma. Por ejemplo, de 200 m³ estimados con 190 vendibles, el aprovechamiento es 95 % y la merma es 5 %.",
        "El cumplimiento del plan se mide comparando lo cosechado con el volumen autorizado. Si bajan los precios, el margen disminuye, pero eso no autoriza a recortar la capacitación, la señalización ni los controles de seguridad: esos costos son obligatorios. Un buen análisis presenta los cálculos paso a paso, con unidades, y sus datos son de ejemplo hasta que se reemplazan por los de la empresa.",
        f"Estos cálculos los hace la jefatura con el profesional forestal; tú aprendes a leerlos y a verificarlos. {EMER} {AVISO}",
    ],
    vocab=[("costo unitario", "costo de producir cada metro cúbico"), ("margen por m³", "precio de venta menos costo unitario"), ("utilidad", "ingreso total menos costo total"), ("aprovechamiento", "porcentaje del volumen estimado que se convierte en trozas vendibles"), ("merma", "parte del volumen que no se aprovecha"), ("cumplimiento del plan", "comparación entre lo cosechado y el volumen autorizado")],
    worked=[
        ("Margen por m³", "Un costo unitario de ejemplo es $8.000 y el precio de venta es $12.000. ¿Cuál es el margen por m³?", ["Se resta el costo unitario al precio.", "12.000 − 8.000 = 4.000."], "$4.000 por m³"),
        ("Aprovechamiento", "De un volumen estimado de 400 m³ de ejemplo se obtienen 380 m³ vendibles. ¿Cuál es el aprovechamiento?", ["380 ÷ 400 son 95 de cada 100.", "El aprovechamiento es 95 %."], "95 %"),
    ],
    mistakes=[("Confundir costo unitario con costo total.", "El unitario es por cada m³; el total es por todo el volumen.", "Multiplica el costo unitario por el volumen para obtener el costo total."),
              ("Recortar capacitación o señalización para mejorar el margen.", "Los costos de seguridad son obligatorios y protegen a las personas.", "Revisa otros costos con el responsable, nunca los de seguridad.")],
    T=[
        ("abc", "En Forestal: ¿qué es la merma de una faena?", "La parte del volumen estimado que no se aprovecha como troza vendible", "La ganancia total de la venta", "El volumen que se agrega sobre lo autorizado", "La merma es la pérdida de volumen aprovechable."),
        ("abc", "En Forestal: ¿qué es el costo unitario de una faena?", "El costo de producir cada metro cúbico", "El costo total de toda la faena", "El precio al que se vende cada metro cúbico", "El costo unitario se expresa por metro cúbico, no por toda la faena."),
        ("abc", "En Forestal: ¿cómo se calcula el margen por m³?", "Precio de venta menos costo unitario", "Costo unitario menos precio de venta", "Precio de venta más costo unitario", "El margen es lo que queda de cada m³ después de cubrir su costo."),
        ("=", "{F} ¿Cuál es el costo unitario total por m³ sumando las cuatro etapas?", "3000+2000+1000+4000", "Se suman los costos por m³ de las cuatro etapas.", " pesos por m³"),
        ("=", "{F} ¿Cuál es el margen por m³?", "14000-(3000+2000+1000+4000)", "Se resta el costo unitario total al precio de venta.", " pesos por m³"),
        ("=", "{F} ¿Cuánto cuesta producir los 480 m³ vendibles?", "480*(3000+2000+1000+4000)", "Se multiplica el costo unitario total por el volumen vendible.", " pesos"),
        ("=", "{F} ¿Cuál es el ingreso por vender los 480 m³?", "480*14000", "Se multiplica el volumen vendible por el precio de venta.", " pesos"),
        ("=", "{F} ¿Cuál es la utilidad total de la faena?", "480*14000-480*(3000+2000+1000+4000)", "Se resta el costo total al ingreso total.", " pesos"),
        ("=", "{F} ¿Qué porcentaje del volumen estimado se aprovechó?", "480*100//500", "Se divide el volumen vendible entre el volumen estimado y se multiplica por 100.", " %"),
        ("abc", "{F} Si la merma de la faena es de 4 %, ¿qué significa?", "Que de cada 100 m³ estimados, 4 no se aprovechan", "Que de cada 100 m³ estimados, solo 4 se aprovechan", "Que el precio sube 4 % por cada m³", "La merma es la parte que no se aprovecha, aquí el 4 % del volumen estimado."),
        ("=", "{F} ¿Qué porcentaje del volumen autorizado se ha cosechado?", "480*100//600", "Se divide el volumen cosechado entre el autorizado y se multiplica por 100.", " %"),
        ("=", "{F} Si el precio de venta bajara a $11.000 por m³ (supuesto de ejemplo), ¿cuál sería la utilidad por los 480 m³?", "480*(11000-(3000+2000+1000+4000))", "Se calcula el nuevo margen por m³ y se multiplica por el volumen.", " pesos"),
        ("abc", "{F} Con ese precio más bajo, un compañero propone ahorrar omitiendo la capacitación y la señalización de la faena. ¿Qué respuesta es correcta?", "No: los costos de seguridad no se recortan; se revisan otros costos con el responsable", "Sí, porque la señalización no produce madera", "Sí, si es solo por una vez", "La seguridad no es un costo opcional: protege a las personas y es obligatoria."),
    ],
    ctx=("abc", "Te ofrecen dinero en efectivo por ayudar un fin de semana a cargar trozas en un predio vecino, «sin papeles ni permisos». ¿Qué respondes?", "Que no, porque esas tareas exigen personal autorizado, contrato y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si pagan bien", "Que sí, si lo haces con un amigo", "Sin autorización, contrato ni plan de seguridad la tarea no es segura ni legal, aunque paguen."),
    sc=[
        ("En Forestal: ¿cómo se calcula la utilidad total?", "Ingreso total menos costo total", "La utilidad es lo que queda después de pagar los costos."),
        ("¿Qué es el aprovechamiento?", "El porcentaje del volumen estimado que se convierte en trozas vendibles", "Mide cuánto del volumen estimado se aprovecha."),
        ("¿Se pueden recortar los costos de seguridad para mejorar el margen?", "No, son obligatorios y protegen a las personas", "La seguridad no se negocia por costo."),
    ],
    op=("Ficha de ejemplo (datos de ejemplo): faena «Muestra 4». Se estimaron 300 m³ y se obtuvieron 270 m³ vendibles. Volumen autorizado: 450 m³. Costo por m³: volteo y desrame, $2.500; madereo, $1.500; carguío, $1.000; transporte, $3.000. Precio de venta: $12.000 por m³. Escribe (a) el costo unitario y el margen por m³, (b) la utilidad total, (c) el aprovechamiento y el porcentaje del volumen autorizado cosechado, (d) por qué no se recortaría el gasto en seguridad si bajara el precio.",
        "(a) 2.500 + 1.500 + 1.000 + 3.000 = 8.000 pesos por m³; 12.000 − 8.000 = 4.000 de margen. (b) 270 × 4.000 = 1.080.000 pesos. (c) 270 ÷ 300 = 90 %; 270 ÷ 450 = 60 %. (d) Porque los costos de seguridad son obligatorios y protegen a las personas.",
        ["calcula el costo unitario y el margen", "calcula la utilidad total", "calcula los porcentajes", "justifica no recortar la seguridad"],
        ["hoja con las cuatro respuestas"],
        ["confundir costo unitario con total", "olvidar usar el volumen vendible", "proponer recortar capacitación"],
        "Pregunta: «¿qué costos no pueden recortarse y por qué?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un costo por m³ para tres etapas y un precio de venta, y calcula el margen por m³.",
    extend="Explica con un ejemplo por qué una merma alta puede reducir la utilidad aunque el precio sea bueno.",
)
