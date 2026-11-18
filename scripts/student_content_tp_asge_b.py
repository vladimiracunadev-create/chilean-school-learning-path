"""Asistencia en Geología TP 3.º y 4.º medio: OAE-04 (sondajes y movimientos de tierra), OAE-05 (muestras geológicas) y OAE-06 (minerales a simple vista). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_asge_common import AVISO, EMER, build

O4 = "TP-ASGE-3y4-OAE-04"
O5 = "TP-ASGE-3y4-OAE-05"
O6 = "TP-ASGE-3y4-OAE-06"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Proyecto Sierra Demo» de la empresa ficticia «Minera Demo» prevé una plataforma de sondaje (superficie plana habilitada para ubicar la máquina perforadora) y, aparte, una calicata "
     "(excavación poco profunda para observar el suelo y la roca superficial). Peligros anotados: partes giratorias de la máquina, ruido, polvo, paredes de la calicata que pueden derrumbarse, tránsito de maquinaria pesada en el camino de acceso, "
     "derrame de aceite o combustible y piso resbaladizo. El área de trabajo se delimita con cinta y señales formando un cuadrado de 20 metros por lado, con la máquina al centro (dato de ejemplo).")
build(
    O4, 1, F,
    use="Aprenderé qué son un sondaje, una plataforma y una calicata, qué peligros tiene la perforación y el movimiento de tierra y cómo se ordenan las medidas de prevención, sin aprender a operar ninguna máquina.",
    prior=["Sé qué es un campamento de prospección.", "Sé distinguir peligro y riesgo.", "Sé la jerarquía de controles."],
    explain=[
        "Un sondaje es una perforación que se hace en el terreno para obtener muestras de roca desde profundidad. Los movimientos de tierra son excavaciones, como las zanjas o las calicatas, que remueven suelo para observar y obtener muestras. Estas tareas usan maquinaria y equipos y las hace personal autorizado, siguiendo el programa del proyecto, las características del terreno y el tipo de muestra que se necesita. La plataforma de sondaje es la superficie plana habilitada para ubicar la máquina perforadora.",
        "Los peligros son muchos: partes que giran, ruido, polvo, paredes de excavación que se derrumban, maquinaria en movimiento y derrames. La jerarquía de controles ordena las medidas: eliminar o alejar, sustituir, controles de ingeniería (por ejemplo, cubiertas fijas sobre partes giratorias), controles administrativos (señales, permisos de ingreso, capacitación) y, al final, el EPP, como casco y protección auditiva. Por eso el área de trabajo se delimita y solo entra personal autorizado. Además se cuida el ambiente: las perforaciones y excavaciones se cierran o restauran según el plan ambiental y la norma vigente.",
        f"Este cuaderno no enseña a operar perforadoras ni a excavar: eso lo hace personal autorizado con la norma vigente de la autoridad minera. {EMER} {AVISO}",
    ],
    vocab=[("sondaje", "perforación del terreno para obtener muestras de roca desde profundidad"), ("calicata", "excavación poco profunda para observar y muestrear suelo y roca superficial"), ("plataforma de sondaje", "superficie plana habilitada para ubicar la máquina perforadora"), ("movimiento de tierra", "excavación o traslado de suelo y roca, como zanjas o calicatas"), ("área delimitada", "zona marcada con cinta, señales o barreras donde solo entra personal autorizado"), ("derrumbe", "caída repentina de material desde una pared o talud")],
    worked=[
        ("Peligro y riesgo", "Una excavación de ejemplo tiene paredes sin resguardo y un montón de material apilado justo en su borde. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la pared sin resguardo y el material apilado en el borde.", "El riesgo es que la pared se derrumbe o el material caiga y atrape o golpee a una persona."], "Peligro: pared sin resguardo y material en el borde; riesgo: derrumbe o caída de material sobre una persona"),
        ("Clasificar un control", "Se instala una cubierta fija que impide tocar las partes giratorias de una máquina de ejemplo. ¿A qué nivel de la jerarquía corresponde?", ["La cubierta cambia físicamente la máquina.", "Un cambio físico del equipo o del lugar es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que casco y protección auditiva bastan para estar cerca de una perforadora.", "El EPP es la última barrera y no quita los peligros de la máquina.", "Primero se delimita el área, se restringe el acceso y se aplican controles de ingeniería; el EPP se suma."),
              ("Creer que quien leyó este cuaderno puede ayudar a manejar una perforadora o una excavadora.", "Operar maquinaria exige formación, autorización y norma vigente.", "Aprende aquí el concepto y deja la operación a personal autorizado.")],
    T=[
        ("abc", "En Geología: ¿qué es un sondaje?", "Una perforación del terreno para obtener muestras de roca desde profundidad", "Un dibujo con las curvas de nivel de un sector", "Un documento que autoriza excavar un terreno", "El sondaje es una perforación; el dibujo es un plano y el documento es un permiso."),
        ("abc", "En Geología: ¿qué es una calicata?", "Una excavación poco profunda para observar y muestrear suelo y roca superficial", "Una perforación profunda que extrae un cilindro de roca", "Una zona del campamento donde se guardan muestras", "La calicata es una excavación superficial; el cilindro de roca sale de un sondaje."),
        ("abc", "En Geología: ¿qué es la plataforma de sondaje?", "La superficie plana habilitada para ubicar la máquina perforadora", "La caja donde se guardan los testigos", "El camino de acceso para los vehículos", "La plataforma es el lugar de la máquina; la caja y el camino son otras cosas."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a las paredes de la calicata?", "Que se derrumben y atrapen o lesionen a una persona cercana", "Que la calicata quede poco profunda", "Que el polvo cambie el color de la roca", "El riesgo es la posibilidad de daño a personas; la profundidad y el color no son un daño."),
        ("abc", "{F} Una cubierta fija sobre las partes giratorias de la máquina, instalada por el fabricante y personal autorizado, es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque informa a las personas", "De EPP, porque protege a quien se acerca", "La cubierta modifica el equipo; informar o equipar a las personas son otros niveles."),
        ("abc", "{F} Las señales y un permiso escrito para ingresar al área delimitada son controles de tipo:", "Administrativo, porque ordenan quién puede entrar y cómo", "De ingeniería, porque cambian el terreno", "De eliminación, porque quitan la máquina", "Señales y permisos ordenan la conducta, pero no cambian el lugar ni quitan el peligro."),
        ("=", "{F} Si la cinta se vende en rollos de 50 metros, ¿cuántos rollos hacen falta para rodear todo el cuadrado de la ficha?", "(20*4+49)//50", "Se calcula el perímetro, 4 lados de 20 metros, y se divide entre 50 subiendo al entero.", " rollos"),
        ("abc", "{F} Una estudiante dice: «leí la ficha, así que puedo ayudar a manejar la perforadora en un terreno real». ¿Qué respuesta es correcta?", "Es falso: operar maquinaria exige formación, autorización y norma vigente", "Es cierto, si usa casco y protección auditiva", "Es cierto, si el operador está a su lado", "Un caso en papel no habilita para operar; el EPP o la compañía tampoco."),
        ("abc", "Durante una visita de ejemplo, ves que la pared de una excavación se desmorona con una persona cerca. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte al borde para tirar de la persona", "Bajar a la excavación a ayudarla a salir", "Acercarte a un derrumbe puede provocar otro; se avisa a quienes pueden actuar."),
        ("abc", "En Geología: ¿por qué las personas ajenas al trabajo deben mantenerse fuera del área delimitada?", "Porque allí hay maquinaria y peligros que solo maneja personal autorizado y capacitado", "Porque así se evita que vean los datos del proyecto", "Porque la máquina solo funciona si no hay público", "El área se delimita por seguridad, no por reserva de datos ni por el funcionamiento de la máquina."),
        ("abc", "{F} El jefe del sondaje dice: «basta con que cada uno use casco y protección auditiva». ¿Cuál es la mejor objeción?", "Que el EPP es la última barrera y antes deben aplicarse delimitación, controles de ingeniería y capacitación", "Ninguna, porque el EPP elimina todos los peligros", "Que el casco y la protección auditiva nunca deben usarse", "El EPP protege solo a quien lo usa y no quita el peligro; se suma a los otros controles."),
        ("=", "{F} Si se pone una señal cada 10 metros de cinta, ¿cuántas señales se necesitan en todo el perímetro del cuadrado?", "(20*4)//10", "Se divide el perímetro entre la separación de las señales.", " señales"),
        ("abc", "Durante una visita de ejemplo, notas un derrame de aceite en la plataforma de sondaje. ¿Qué corresponde según las reglas generales?", "No acercarte ni intentar limpiarlo, avisar a un adulto responsable y a emergencias", "Cubrirlo con tierra y seguir trabajando", "Limpiarlo tú mismo con ropa para que nadie resbale", "Un derrame se informa; intervenir sin formación puede causar un accidente o contaminar más."),
    ],
    ctx=("abc", "Un conocido te ofrece trabajo de ayudante en la plataforma de un sondaje «porque ya viste cómo funciona en clases». ¿Qué respondes?", "Que no, porque esa tarea exige formación, autorización y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque con casco basta", "Que sí, pero solo para mirar de cerca", "Haber visto el concepto no habilita para trabajar junto a maquinaria; acercarse solo a mirar tampoco es seguro."),
    sc=[
        ("En Geología: ¿qué es un sondaje?", "Una perforación del terreno para obtener muestras de roca desde profundidad", "El sondaje permite obtener muestras desde el interior del terreno."),
        ("En el trabajo de perforación: ¿quién entra al área delimitada de trabajo?", "Solo el personal autorizado y capacitado", "El área se restringe porque tiene peligros de maquinaria."),
        ("En el trabajo de sondajes y excavaciones geológicas: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
    ],
    op=("El proyecto ficticio «Proyecto Cresta Demo» planifica una plataforma de sondaje de ejemplo. Peligros anotados: ruido fuerte de la máquina, piso resbaladizo tras la lluvia y tránsito de camiones por el camino de acceso. Escribe (a) cuál es el peligro del ruido y cuál el riesgo, (b) un control administrativo para limitar la exposición al ruido, (c) un control de ingeniería para reducirlo en su origen, (d) por qué el EPP no basta, (e) qué debe hacer una persona que vea a un camión perder el control cerca de la plataforma.",
        "(a) Peligro: el ruido fuerte de la máquina; riesgo: daño auditivo en las personas expuestas. (b) Limitar el tiempo de exposición y señalizar la zona de ruido con un permiso de ingreso. (c) Encerrar o amortiguar la fuente de ruido con una cubierta o cabina que lo reduzca, instalada por personal autorizado. (d) Porque el EPP es la última barrera: no reduce el ruido ni quita el peligro y protege solo a quien lo usa. (e) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias. La operación real la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta", "indica no acercarse y avisar"],
        ["hoja con las cinco respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "responder que se acerca a ayudar"],
        "Pregunta: «¿qué control actúa sobre la fuente del ruido y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe la jerarquía de controles en orden y pon junto a cada nivel un ejemplo inventado de una plataforma de sondaje.",
    extend="Explica con un ejemplo por qué un permiso de ingreso es un control administrativo y no reemplaza una barrera física.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). «Proyecto Sierra Demo». Orden de perforación del sondaje SD-01: tipo diamantino, azimut 90 (hacia el Este), inclinación de 60 grados bajo la horizontal, profundidad programada de 150 metros. "
     "Planilla de sondaje del primer día: perforados de 0 a 40 metros. Las cajas de testigos de ejemplo almacenan 5 metros de testigo cada una y cada caja llena pesa 25 kilos. "
     "Roles: jefe de sondaje, perforista (personal autorizado que opera la máquina), geólogo de sondaje y asistente de geología.")
build(
    O4, 2, F,
    use="Aprenderé los conceptos de sondaje diamantino, circulación reversa, testigo, ripios, collar y tramo, los documentos de un sondaje y el rol de cada persona, para leer una planilla en papel.",
    prior=["Sé qué es un sondaje y una plataforma.", "Sé leer una planilla escrita.", "Sé restar, multiplicar y dividir números enteros."],
    explain=[
        "Hay dos tipos frecuentes de sondaje. En el diamantino, una corona con diamantes corta la roca y se extrae un cilindro llamado testigo. En el de circulación reversa se recuperan fragmentos pequeños de roca llamados ripios. El collar es el punto donde empieza el sondaje en la superficie. El azimut indica hacia dónde se dirige (90 es el Este y 180 el Sur) y la inclinación, qué ángulo forma con la horizontal. Un tramo es un intervalo entre dos profundidades, por ejemplo de 10 a 20 metros, que mide 10 metros.",
        "La orden de perforación es el documento que dice dónde, con qué dirección, de qué tipo y hasta qué profundidad se perforará. La planilla de sondaje registra día a día los metros perforados, los tramos y la cantidad de testigo obtenida. Los testigos se guardan en cajas rotuladas, ordenadas por profundidad. Un registro útil dice qué se hizo, cuándo y quién lo anotó, y no se cambia para que coincida con lo programado.",
        f"El jefe de sondaje coordina; el perforista, personal autorizado, opera la máquina; el geólogo de sondaje dirige el registro geológico; el asistente de geología apoya con registros y datos, fuera de las zonas de riesgo. {EMER} {AVISO}",
    ],
    vocab=[("testigo", "cilindro de roca que se extrae en un sondaje diamantino"), ("ripios", "fragmentos pequeños de roca que se recuperan en una perforación de circulación reversa"), ("collar", "punto donde empieza el sondaje en la superficie"), ("inclinación", "ángulo que forma el sondaje con la horizontal"), ("tramo", "intervalo entre dos profundidades de un sondaje"), ("orden de perforación", "documento que define dónde, cómo y hasta qué profundidad se perfora"), ("planilla de sondaje", "registro diario de metros, tramos y testigo obtenido")],
    worked=[
        ("Largo de un tramo", "Una planilla de ejemplo anota un tramo de 35 a 50 metros. ¿Cuánto mide el tramo?", ["Se resta la profundidad inicial a la final.", "50 menos 35 son 15 metros."], "15 metros"),
        ("Cajas necesarias", "Un sondaje de ejemplo de 60 metros usa cajas de 6 metros de testigo. ¿Cuántas cajas se llenan si se recupera todo el testigo?", ["Se divide el total entre lo que cabe en cada caja.", "60 dividido por 6 da 10 cajas."], "10 cajas"),
    ],
    mistakes=[("Creer que el collar es el punto más profundo del sondaje.", "El collar es el inicio, en la superficie.", "El punto más profundo es el fondo del sondaje; el collar es donde empieza."),
              ("Cambiar los metros de la planilla para que coincidan con el programa.", "El registro debe reflejar lo realmente perforado.", "Se anota el valor real y se informa la diferencia con lo programado.")],
    T=[
        ("abc", "En Geología: ¿qué es un testigo de sondaje?", "Un cilindro de roca que se extrae en un sondaje diamantino", "Un trozo de cinta que delimita la plataforma", "La planilla donde se anotan los metros perforados", "El testigo es el cilindro de roca; la cinta y la planilla son otras cosas."),
        ("abc", "En Geología: ¿qué son los ripios de una perforación?", "Fragmentos pequeños de roca que se recuperan en la circulación reversa", "Cilindros largos de roca que se guardan en cajas", "Piezas metálicas de la máquina que se reemplazan", "Los ripios son fragmentos pequeños de roca; los cilindros son los testigos."),
        ("abc", "En Geología: ¿qué es el collar de un sondaje?", "El punto donde empieza el sondaje en la superficie", "El último tramo perforado, el más profundo", "La caja donde se guardan los testigos", "El collar es el inicio en superficie; no es el fondo ni una caja."),
        ("abc", "{F} ¿Qué documento define dónde, con qué dirección y hasta qué profundidad se perforará?", "La orden de perforación", "La planilla de sondaje", "La caja de testigos", "La orden fija lo programado; la planilla registra lo realizado."),
        ("abc", "{F} ¿Qué documento registra día a día los metros perforados y los tramos?", "La planilla de sondaje", "La orden de perforación", "El croquis del campamento", "La planilla es el registro diario; la orden es el programa."),
        ("=", "{F} Después del primer día, ¿cuántos metros faltan para llegar a la profundidad programada?", "150-40", "Se resta lo perforado a la profundidad programada.", " metros"),
        ("=", "{F} ¿Cuántas cajas se llenan con los 40 metros del primer día, si se recupera todo el testigo?", "40//5", "Se divide la longitud perforada entre los metros que caben en cada caja.", " cajas"),
        ("=", "{F} ¿Cuántas cajas harían falta para los 150 metros programados, si se recupera todo el testigo?", "150//5", "Se divide la profundidad programada entre los metros por caja.", " cajas"),
        ("abc", "{F} Según la orden de perforación, ¿hacia dónde se dirige el sondaje SD-01?", "Hacia el Este, porque su azimut es 90", "Hacia el Sur, porque su azimut es 90", "Hacia el Norte, porque su inclinación es 60", "El azimut 90 apunta al Este; la inclinación es el ángulo con la horizontal."),
        ("abc", "{F} Un compañero dice que el collar de SD-01 está a 150 metros de profundidad. ¿Qué respuesta es correcta?", "Es falso: el collar es el inicio en la superficie, y 150 metros es la profundidad programada", "Es cierto, porque el collar es el final del sondaje", "Es cierto, si el sondaje es diamantino", "El collar marca el comienzo en la superficie, no el fondo."),
        ("abc", "En otro sondaje de ejemplo, la planilla del primer día anota 45 metros perforados, pero las cajas llenas cubren solo 40 metros. ¿Qué corresponde?", "Revisar la diferencia con el geólogo de sondaje y anotar la explicación, sin ajustar los números", "Cambiar la planilla a 40 para que coincida", "Cambiar las cajas para que cubran 45", "Una diferencia entre registros se investiga y se explica; no se acomoda."),
        ("=", "{F} ¿Cuántos kilos pesan en total las cajas llenas del primer día?", "8*25", "Se multiplica el número de cajas por el peso de cada una.", " kilos"),
        ("abc", "{F} Cada caja llena pesa 25 kilos. ¿Qué control es adecuado para moverlas?", "Usar ayudas mecánicas o repartir la carga entre varias personas, según la norma vigente", "Que la persona más fuerte las lleve sola", "Apilar varias cajas para llevarlas de una sola vez", "Las cargas pesadas se mueven con ayudas o entre varias personas; levantarlas solo o apilarlas aumenta el riesgo de lesión."),
    ],
    ctx=("abc", "Un compañero te propone «ajustar» en la planilla de sondaje los metros del primer día para que calcen con el programa antes de que llegue la jefa. ¿Qué respondes?", "Que no se alteran los registros y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, si la diferencia es pequeña", "Que sí, y se corrige después de la visita", "Alterar un registro oculta la realidad; ante la duda se consulta a un adulto responsable."),
    sc=[
        ("En Geología: ¿qué es un testigo de sondaje?", "Un cilindro de roca que se extrae en un sondaje diamantino", "El testigo guarda la roca tal como estaba en profundidad."),
        ("En el registro de un sondaje: ¿qué es un tramo?", "Un intervalo entre dos profundidades, como de 10 a 20 metros", "El largo del tramo se obtiene restando las profundidades."),
        ("¿Qué documento fija lo programado para un sondaje?", "La orden de perforación", "La orden define dónde, cómo y hasta dónde se perfora."),
    ],
    op=("Ficha de ejemplo: «Proyecto Ladera Demo». Orden del sondaje SD-07: diamantino, azimut 180, inclinación de 70 grados bajo la horizontal, profundidad programada de 120 metros. Primer día: perforados de 0 a 30 metros. Las cajas de ejemplo almacenan 6 metros de testigo cada una. Escribe (a) hacia dónde se dirige el sondaje, (b) cuántos metros faltan después del primer día, (c) cuántas cajas se llenan con los 30 metros, (d) en qué documento se anotan los metros de cada día.",
        "(a) Hacia el Sur, porque el azimut 180 apunta al Sur. (b) 120 − 30 = 90 metros. (c) 30 ÷ 6 = 5 cajas. (d) En la planilla de sondaje. La perforación real la hace personal autorizado.",
        ["interpreta bien el azimut", "calcula bien los metros que faltan", "calcula bien las cajas", "nombra la planilla de sondaje"],
        ["hoja con las cuatro respuestas"],
        ["confundir azimut con inclinación", "restar al revés", "confundir orden con planilla"],
        "Pregunta: «¿qué dato de la orden indica hacia dónde va el sondaje?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un tramo de un sondaje, escribe de qué profundidad a qué profundidad va y calcula cuánto mide.",
    extend="Explica con un ejemplo por qué la planilla y la orden de perforación no cumplen la misma función.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (planilla de ejemplo, inventada). Sondaje diamantino SD-03 del «Proyecto Sierra Demo». Cada tramo se perfora en 10 metros. Metros de testigo recuperados por tramo: de 0 a 10 metros, 9; de 10 a 20, 8; de 20 a 30, 5; de 30 a 40, 10; "
     "y el tramo de 40 a 50 metros aparece anotado con 11 metros recuperados. Criterio de ejemplo del proyecto (los valores reales los fija el proyecto): un tramo es aceptable si su recuperación es de 80 por ciento o más.")
build(
    O4, 3, F,
    use="Aprenderé a analizar una planilla de sondaje en papel: calcular la recuperación por tramo, compararla con un criterio, detectar valores imposibles e informar sin acomodar los datos.",
    prior=["Sé qué es un testigo, un tramo y una planilla de sondaje.", "Sé calcular porcentajes sencillos.", "Sé comparar una medida con un criterio."],
    explain=[
        "La recuperación de un tramo es el porcentaje de testigo que se obtuvo respecto de lo que se perforó. Se calcula dividiendo los metros recuperados entre los metros perforados y multiplicando por 100. Por ejemplo, 8 metros recuperados de 10 perforados dan una recuperación de 80 por ciento. El criterio de aceptación dice a partir de qué porcentaje un tramo se considera aceptable.",
        "Una recuperación baja significa que se obtuvo poco testigo; puede deberse, por ejemplo, a roca muy fracturada o a otras causas que hay que confirmar, y puede hacer que la muestra no represente bien la roca. No se saca ninguna conclusión sobre el contenido mineral de ese tramo: se informa al geólogo de sondaje. Un valor imposible, como recuperar más metros que los perforados, indica un error de registro o de medición: se revisa la medición original y se corrige con firma, sin borrar.",
        f"El análisis real lo hace el geólogo de sondaje. Aquí practicas el razonamiento con números de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("recuperación", "porcentaje de testigo obtenido respecto de lo perforado"), ("criterio de aceptación", "regla que dice a partir de qué valor un resultado se acepta"), ("valor imposible", "dato que no puede ser cierto, como recuperar más de lo perforado"), ("fracturada", "roca con muchas grietas, que se rompe con facilidad"), ("representatividad", "capacidad de una muestra de reflejar bien el conjunto")],
    worked=[
        ("Recuperación de un tramo", "En un tramo de ejemplo de 10 metros se recuperan 7 metros de testigo. ¿Cuál es la recuperación?", ["Se divide: 7 ÷ 10 = 0,7.", "Multiplicado por 100 da 70 por ciento."], "70 por ciento"),
        ("Cumplir un criterio", "Un tramo de ejemplo de 30 metros recupera 24 metros y el criterio exige 80 por ciento o más. ¿Cumple?", ["24 ÷ 30 = 0,8, que equivale a 80 por ciento.", "80 es igual al mínimo exigido, así que cumple."], "Sí, cumple con exactamente 80 por ciento"),
    ],
    mistakes=[("Concluir que un tramo con poca recuperación no tiene mineral.", "La recuperación mide cuánto testigo se obtuvo, no su contenido mineral.", "Se informa la baja recuperación y no se saca conclusión sobre el contenido."),
              ("Aceptar un tramo con más metros recuperados que perforados, porque «más es mejor».", "Es un valor imposible: señala un error de registro o de medición.", "Se revisa la medición original y se corrige con firma.")],
    T=[
        ("abc", "En Geología: ¿qué es la recuperación de un tramo de sondaje?", "El porcentaje de testigo obtenido respecto de los metros perforados", "El porcentaje de mineral que contiene la roca", "La profundidad final del sondaje", "La recuperación compara testigo con lo perforado; no mide el contenido mineral."),
        ("abc", "En Geología: ¿qué indica una recuperación baja en un tramo?", "Que se obtuvo poco testigo respecto de lo perforado, y que la causa debe confirmarse", "Que la roca de ese tramo no contiene minerales", "Que el sondaje terminó antes de lo programado", "Poca recuperación es poco testigo; no dice nada del contenido mineral ni del término del sondaje."),
        ("abc", "En Geología: ¿qué es un valor imposible en una planilla de sondaje?", "Un dato que no puede ser cierto, como recuperar más metros que los perforados", "Un dato anotado con lápiz en vez de tinta", "Un dato que cumple el criterio de aceptación", "Un valor imposible contradice la lógica del registro y obliga a revisar."),
        ("=", "{F} ¿Cuál es la recuperación en porcentaje del tramo de 0 a 10 metros?", "(9*100)//10", "Se multiplican los metros recuperados por 100 y se dividen entre los 10 perforados.", " por ciento"),
        ("=", "{F} ¿Cuál es la recuperación en porcentaje del tramo de 10 a 20 metros?", "(8*100)//10", "Se multiplican los metros recuperados por 100 y se dividen entre los 10 perforados.", " por ciento"),
        ("=", "{F} ¿Cuál es la recuperación en porcentaje del tramo de 20 a 30 metros?", "(5*100)//10", "Se multiplican los metros recuperados por 100 y se dividen entre los 10 perforados.", " por ciento"),
        ("abc", "{F} ¿Qué tramos entre 0 y 40 metros cumplen el criterio de 80 por ciento o más?", "De 0 a 10, de 10 a 20 y de 30 a 40", "Solo de 0 a 10 y de 30 a 40", "De 0 a 10, de 10 a 20 y de 20 a 30", "Los tramos con 90, 80 y 100 por ciento cumplen; el de 50 por ciento no."),
        ("=", "{F} ¿Cuál es la recuperación en porcentaje del conjunto de los cuatro primeros tramos, de 0 a 40 metros?", "((9+8+5+10)*100)//40", "Se suman los metros recuperados, se multiplican por 100 y se dividen entre los 40 perforados.", " por ciento"),
        ("abc", "{F} ¿Qué corresponde con el tramo de 20 a 30 metros, que tiene baja recuperación?", "Informar al geólogo de sondaje y anotar el dato, sin suponer la causa ni el contenido mineral", "Borrar el tramo de la planilla para no afectar el promedio", "Anotar que el tramo no tiene mineral", "La baja recuperación se informa; borrar o suponer oculta el dato o inventa conclusiones."),
        ("abc", "{F} El tramo de 40 a 50 metros aparece con 11 metros recuperados. ¿Qué corresponde?", "Reconocer un valor imposible, revisar la medición original y corregir con firma", "Aceptarlo como 110 por ciento, porque es mejor", "Cambiarlo a 10 sin avisar a nadie", "Recuperar más de lo perforado es imposible; se revisa en lugar de aceptar o acomodar."),
        ("abc", "{F} Un compañero dice: «como el conjunto de los cuatro tramos da 80 por ciento, todos los tramos están bien». ¿Qué respuesta es correcta?", "Es falso: el tramo de 20 a 30 metros tiene solo 50 por ciento y no cumple", "Es cierto, porque el criterio se aplica solo al total", "Es cierto, porque 80 por ciento es el promedio", "El criterio de la ficha se aplica a cada tramo; un promedio puede ocultar un tramo bajo."),
        ("=", "{F} ¿Cuántos metros de testigo no se recuperaron en el conjunto de los cuatro primeros tramos?", "40-(9+8+5+10)", "Se restan los metros recuperados a los metros perforados.", " metros"),
        ("abc", "{F} Una geóloga se interesa por el tramo de baja recuperación. ¿Qué conviene hacer?", "Informar y dejar constancia para que se decida cómo tratar ese tramo, sin sacar conclusiones sobre su contenido mineral", "Sacar conclusiones sobre su contenido con el testigo que se recuperó", "No volver a mencionar el tramo en los informes", "La baja recuperación puede afectar la representatividad; se deja constancia y se decide con quien corresponde."),
    ],
    ctx=("abc", "Una compañera te sugiere cambiar los 5 metros del tramo de 20 a 30 por 8, «para que la planilla quede perfecta» antes de una visita. ¿Qué respondes?", "Que no se alteran los registros y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, si lo corrige después", "Que sí, pero solo ese tramo", "Alterar un dato oculta un problema real; ante la duda se consulta a un adulto responsable."),
    sc=[
        ("En Geología: ¿cómo se calcula la recuperación de un tramo?", "Se divide lo recuperado entre lo perforado y se multiplica por 100", "La recuperación es un porcentaje de testigo respecto de lo perforado."),
        ("En un sondaje: ¿qué se hace con un valor imposible?", "Se revisa la medición original y se corrige con firma, sin borrar", "Un valor imposible señala un error de registro o de medición."),
        ("¿Qué se informa ante una recuperación baja?", "El dato, sin concluir nada sobre el contenido mineral", "La causa debe confirmarse y el contenido mineral no se supone."),
    ],
    op=("Planilla de ejemplo del sondaje SD-08, «Proyecto Pampa Demo». Tramos de 10 metros con metros recuperados: de 0 a 10, 10 metros; de 10 a 20, 7 metros; de 20 a 30, 6 metros. Criterio de ejemplo: recuperación de 70 por ciento o más. Escribe (a) la recuperación de cada tramo, (b) qué tramos cumplen, (c) qué harías con el tramo que no cumple, (d) qué harías si otro tramo apareciera con 12 metros recuperados de 10 perforados.",
        "(a) 100 por ciento, 70 por ciento y 60 por ciento. (b) Cumplen los tramos de 0 a 10 y de 10 a 20; el de 20 a 30 no. (c) Informar al geólogo de sondaje y anotar el dato, sin concluir sobre el contenido mineral. (d) Es un valor imposible: revisar la medición original y corregir con firma. Todo lo hace el geólogo de sondaje.",
        ["calcula bien cada recuperación", "identifica los tramos que cumplen", "informa sin concluir sobre el mineral", "trata el valor imposible sin acomodarlo"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "concluir que no hay mineral", "cambiar el dato para que cumpla"],
        "Pregunta: «¿qué número va multiplicado por 100 y entre cuál se divide?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres tramos de 10 metros con sus metros recuperados y calcula la recuperación de cada uno.",
    extend="Explica por qué una baja recuperación no permite afirmar que una roca no tiene mineral.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (programa de ejemplo, inventado). «Proyecto Sierra Demo»: el sondaje SD-04 tiene una profundidad programada de 120 metros. Avance de ejemplo: 24 metros por turno y 2 turnos al día. Las cajas de testigos almacenan 5 metros cada una. "
     "Meta de recuperación de ejemplo: 85 por ciento o más. Además se programan 4 calicatas de 3 metros de largo, 2 de ancho y 2 de profundidad; los camiones de ejemplo transportan 8 metros cúbicos por viaje. "
     "Criterio de detención de ejemplo: ante una tormenta, un camino resbaladizo o una condición insegura, el supervisor autorizado detiene el trabajo y se registra el motivo.")
build(
    O4, 4, F,
    use="Aprenderé a calcular en papel avances, días de trabajo, cajas, volúmenes de excavación y metas de recuperación, y a registrar con honestidad lo que realmente se hizo y las detenciones.",
    prior=["Sé qué es un sondaje, un tramo y una caja de testigos.", "Sé multiplicar y dividir números enteros.", "Sé calcular porcentajes sencillos."],
    explain=[
        "El avance de un sondaje es la cantidad de metros que se perforan en un tiempo, por ejemplo por turno. Con el avance diario y la profundidad programada se calculan los días necesarios; si la división no es exacta, se redondea hacia arriba. Las cajas de testigos se calculan dividiendo los metros entre lo que cabe en cada caja. La meta de recuperación permite calcular cuántos metros de testigo se esperan como mínimo: se multiplica la longitud perforada por el porcentaje y se divide por 100.",
        "En un movimiento de tierra el volumen de una excavación en forma de caja se calcula multiplicando largo por ancho por profundidad y se expresa en metros cúbicos; con él se calcula cuántos viajes de camión hacen falta. Los cálculos se actualizan con los datos reales. Si se detiene el trabajo por seguridad, se registra la detención, su motivo y el avance real, sin anotar metros que no se perforaron. La decisión de detener o seguir la toma el supervisor autorizado.",
        f"Estos cálculos los revisa el jefe de sondaje. Aquí aprendes el razonamiento con números de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("avance", "metros perforados en un tiempo, por ejemplo por turno"), ("turno", "período de trabajo de un equipo"), ("volumen", "espacio que ocupa un material, medido en metros cúbicos"), ("meta de recuperación", "porcentaje de testigo que se espera obtener como mínimo"), ("criterio de detención", "condición que obliga a detener el trabajo y registrar el motivo")],
    worked=[
        ("Días de trabajo", "Un sondaje de ejemplo de 90 metros avanza 30 metros por turno con 1 turno al día. ¿Cuántos días necesita?", ["Se divide la profundidad entre el avance diario.", "90 dividido por 30 da 3 días."], "3 días"),
        ("Volumen de una zanja", "Una zanja de ejemplo mide 5 metros de largo, 1 de ancho y 2 de profundidad. ¿Qué volumen remueve?", ["Se multiplica largo por ancho por profundidad.", "5 × 1 × 2 son 10 metros cúbicos."], "10 metros cúbicos"),
    ],
    mistakes=[("Anotar el avance programado cuando el real fue menor, para no atrasar el programa.", "El registro falso impide recalcular plazos y oculta problemas.", "Se anota el avance real y se recalcula el plan."),
              ("Redondear hacia abajo los días necesarios, por ejemplo 2,5 días a 2.", "Con 2 días no se alcanza la profundidad programada.", "Cuando no se puede usar una fracción de día de trabajo, se redondea hacia arriba.")],
    T=[
        ("abc", "En Geología: ¿qué es el avance de un sondaje?", "Los metros que se perforan en un tiempo determinado, como un turno", "La profundidad total programada del sondaje", "El porcentaje de testigo que se recupera", "El avance mide metros por tiempo; la profundidad programada y la recuperación son otros datos."),
        ("abc", "En Geología: ¿qué es el volumen de una excavación en forma de caja?", "El espacio que ocupa el material removido, que se obtiene multiplicando largo por ancho por profundidad", "La suma del largo y el ancho de la excavación", "La distancia entre la excavación y el camino", "El volumen se calcula multiplicando tres medidas, no sumándolas."),
        ("abc", "En Geología: ¿qué es un criterio de detención del trabajo?", "Una condición que obliga a detener el trabajo y registrar el motivo", "Un permiso para trabajar más horas seguidas", "La meta de metros que se debe perforar cada día", "El criterio de detención protege a las personas ante una condición insegura."),
        ("=", "{F} ¿Cuántos metros se perforan por día con el avance de la ficha?", "24*2", "Se multiplica el avance de un turno por los turnos del día.", " metros"),
        ("=", "{F} ¿Cuántos días de trabajo necesita SD-04, redondeando hacia arriba?", "(120+47)//48", "Se suman 47 antes de dividir entre 48 para subir al siguiente entero.", " días"),
        ("=", "{F} ¿Cuántas cajas de testigos se llenarían con los 120 metros si se recuperara todo?", "120//5", "Se divide la profundidad entre los metros que caben en cada caja.", " cajas"),
        ("=", "{F} ¿Qué volumen remueve una calicata de la ficha, en metros cúbicos?", "3*2*2", "Se multiplican largo, ancho y profundidad.", " metros cúbicos"),
        ("=", "{F} ¿Qué volumen remueven las 4 calicatas juntas, en metros cúbicos?", "4*3*2*2", "Se multiplica el volumen de una calicata por el número de calicatas.", " metros cúbicos"),
        ("=", "{F} ¿Cuántos viajes de camión hacen falta para transportar el material de las 4 calicatas?", "(4*3*2*2)//8", "Se divide el volumen total entre lo que lleva cada camión por viaje.", " viajes"),
        ("abc", "{F} Durante una tormenta el camino de acceso queda resbaladizo y el supervisor ordena detener los trabajos. ¿Qué corresponde registrar?", "La detención, su motivo y el avance real, sin anotar metros que no se perforaron", "El avance programado del día, para no atrasar el informe", "Nada, porque solo se registra lo que se perfora", "Se registra la realidad, incluida la detención y su motivo."),
        ("abc", "{F} Un compañero propone anotar 48 metros aunque solo se perforaron 36, para no atrasar el programa. ¿Qué corresponde responder?", "Que no se falsea el registro: se anota el avance real y se recalcula el plan", "Que sí, porque se recuperará el atraso después", "Que sí, si se avisa solo al supervisor", "Anotar un avance falso impide recalcular y oculta problemas."),
        ("=", "{F} Con la meta de recuperación de la ficha, ¿cuántos metros de testigo se esperan como mínimo en los 120 metros?", "(120*85)//100", "Se multiplica la longitud por el porcentaje y se divide entre 100.", " metros"),
        ("abc", "{F} Con un avance real de 18 metros por turno, ¿qué debe hacerse con el programa?", "Recalcular los días necesarios con el dato real y avisar al jefe del proyecto", "Mantener los días calculados, para no modificar el programa", "Anotar 24 metros por turno en la planilla", "El programa se recalcula con datos reales; mantenerlo o falsear el avance no cambia los metros perforados."),
    ],
    ctx=("abc", "Un conocido te pide que calcules en tu cuaderno cuántos días tomará un sondaje real «para ganar tiempo», sin consultar a nadie. ¿Qué respondes?", "Que los números del cuaderno son de ejemplo y que el cálculo real lo hace el jefe de sondaje con datos reales; lo consultarás con un adulto responsable", "Que sí, porque el método está bien", "Que sí, pero redondeando hacia abajo", "Los valores son de ejemplo; los reales los fija y revisa quien dirige el sondaje."),
    sc=[
        ("En Geología: ¿qué es el avance de un sondaje?", "Los metros que se perforan en un tiempo determinado", "El avance permite calcular los días necesarios."),
        ("En un movimiento de tierra: ¿cómo se calcula el volumen de una excavación en forma de caja?", "Multiplicando largo por ancho por profundidad", "El volumen se obtiene multiplicando las tres medidas."),
        ("¿Qué se registra cuando el trabajo se detiene por seguridad?", "La detención, su motivo y el avance real", "Se registra la realidad, no lo programado."),
    ],
    op=("Ficha de ejemplo: sondaje SD-09, «Proyecto Pampa Demo», profundidad programada de 100 metros; avance de 20 metros por turno y 2 turnos al día; cajas de 4 metros; meta de recuperación de 80 por ciento. Una calicata de 4 metros de largo, 2 de ancho y 1 de profundidad. Escribe (a) cuántos días necesita el sondaje, (b) cuántas cajas se llenarían si se recuperara todo, (c) cuántos metros de testigo se esperan como mínimo, (d) qué volumen tiene la calicata.",
        "(a) 20 × 2 = 40 metros al día; 100 ÷ 40 = 2,5, se sube a 3 días. (b) 100 ÷ 4 = 25 cajas. (c) 100 × 80 ÷ 100 = 80 metros. (d) 4 × 2 × 1 = 8 metros cúbicos. Los cálculos reales los revisa el jefe de sondaje.",
        ["calcula los días y sube al entero", "calcula bien las cajas", "calcula bien la meta de testigo", "calcula bien el volumen"],
        ["hoja con las cuatro respuestas"],
        ["redondear hacia abajo los días", "sumar en vez de multiplicar el volumen", "olvidar las unidades"],
        "Pregunta: «¿cuántos metros se perforan por día y cuántos faltan?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula los días de un sondaje inventado de 90 metros con avance de 20 metros por turno y 1 turno al día.",
    extend="Explica con un ejemplo por qué se registra una detención por seguridad y no se «recupera» en el papel.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La bodega de muestras del campamento del «Proyecto Altiplano Demo» guarda bolsas de muestras rotuladas. Cada bolsa llena pesa 3 kilos y cada nivel de la estantería admite 45 kilos (datos de ejemplo); la estantería tiene 4 niveles. "
     "Peligros anotados: levantar y mover bolsas y cajas pesadas, bordes filosos de los fragmentos de roca, polvo, estantería sobrecargada, rótulos ilegibles o mal copiados, mezcla de muestras y bolsas dejadas sin protección en el terreno.")
build(
    O5, 1, F,
    use="Aprenderé qué es una muestra geológica y por qué importan su representatividad, su rótulo y su registro, qué peligros tiene manejarlas y qué controles se aplican, sin aprender a tomar muestras en terreno.",
    prior=["Sé qué es un sondaje y un testigo.", "Sé distinguir peligro y riesgo.", "Sé la jerarquía de controles."],
    explain=[
        "Una muestra geológica es una porción de roca, suelo o sedimento que se toma para estudiarla y que debe representar al conjunto del que sale. Tomar, rotular, envasar y almacenar son etapas de un proceso que sigue procedimientos e instructivos, es decir, documentos de la empresa que dicen cómo hacer cada tarea; este cuaderno no los reproduce y la tarea la hace personal autorizado. La muestra debe ser representativa y no contaminarse, es decir, no mezclarse con material ajeno que cambie sus resultados.",
        "Cada muestra tiene un rótulo con un código único y un registro; la cadena de custodia anota quién tuvo la muestra, cuándo y dónde, desde que se toma hasta que llega al laboratorio. Los registros se guardan en el data room, la carpeta o archivo ordenado donde la empresa conserva los documentos del proyecto. Hay peligros físicos, como levantar cargas pesadas o cortarse con bordes filosos, y peligros de información, como un rótulo mal copiado, que puede hacer perder el valor de una muestra. Los controles siguen la jerarquía: por ejemplo, un límite de peso por nivel de estantería es administrativo y los guantes son EPP.",
        f"Esta tarea exige instructor autorizado y norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("muestra geológica", "porción de roca, suelo o sedimento que se toma para estudiarla"), ("representatividad", "capacidad de una muestra de reflejar bien el conjunto del que sale"), ("contaminación", "mezcla de la muestra con material ajeno que cambia sus resultados"), ("instructivo", "documento de la empresa que dice cómo hacer una tarea"), ("cadena de custodia", "registro de quién tuvo la muestra, cuándo y dónde"), ("data room", "carpeta o archivo ordenado donde la empresa guarda los registros del proyecto")],
    worked=[
        ("Peligro y riesgo", "En una bodega de ejemplo hay cajas muy pesadas en el nivel más alto de una estantería. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la carga pesada en el nivel más alto.", "El riesgo es que una caja caiga o que alguien se lesione al bajarla."], "Peligro: carga pesada en un nivel alto; riesgo: que caiga una caja o que alguien se lesione al bajarla"),
        ("Clasificar un control", "Una estantería débil de una bodega de ejemplo se reemplaza por otra más resistente, con topes que impiden que las cajas se deslicen. ¿A qué nivel de la jerarquía corresponde?", ["El cambio modifica físicamente el lugar de almacenaje.", "Un cambio físico del equipo o del lugar es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que una muestra bien tomada sirve aunque su rótulo esté incompleto.", "Sin código único ni registro no se sabe de dónde viene y no se puede usar para decidir.", "Cada muestra lleva su rótulo completo y su registro desde el inicio."),
              ("Creer que leer este cuaderno habilita para tomar muestras en un terreno real.", "Tomar muestras exige instructor autorizado, instructivos de la empresa y norma vigente.", "Aprende aquí el concepto y deja la toma de muestras a personal autorizado.")],
    T=[
        ("abc", "En Geología: ¿qué es una muestra geológica?", "Una porción de roca, suelo o sedimento que se toma para estudiarla y que representa al conjunto", "Un dibujo del terreno con sus curvas de nivel", "Un documento que autoriza perforar un sondaje", "La muestra es material físico; el dibujo y el documento son otras cosas."),
        ("abc", "En Geología: ¿qué es la contaminación de una muestra?", "Que se mezcle con material ajeno que cambia sus resultados", "Que la muestra pese más de lo previsto", "Que el rótulo tenga la letra poco legible", "La contaminación es una mezcla con material ajeno; el peso y la letra son otros problemas."),
        ("abc", "En Geología: ¿qué es la cadena de custodia de una muestra?", "El registro de quién tuvo la muestra, cuándo y dónde, desde que se toma hasta el laboratorio", "La cadena con que se amarran las cajas durante el traslado", "La lista de precios de los análisis", "La cadena de custodia es un registro de responsables; no es un amarre ni una lista de precios."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a los rótulos mal copiados?", "Que una muestra se confunda con otra y los resultados queden mal asignados", "Que las bolsas pesen más", "Que la estantería se llene demasiado rápido", "El riesgo es la confusión de muestras; el peso y el espacio son otros asuntos."),
        ("abc", "{F} ¿Cuál de los peligros de la ficha es de información y no físico?", "Los rótulos ilegibles o mal copiados", "Los bordes filosos de los fragmentos", "La estantería sobrecargada", "Un rótulo erróneo daña la información; los bordes y la sobrecarga pueden lesionar el cuerpo."),
        ("abc", "{F} Un letrero con el límite de peso por nivel y una revisión periódica de la estantería son controles de tipo:", "Administrativo, porque informan y ordenan lo que se debe cumplir", "De ingeniería, porque cambian la estantería", "De EPP, porque protegen a la persona que levanta", "Un letrero y una revisión no cambian la estantería ni equipan a nadie."),
        ("=", "{F} ¿Cuántas bolsas llenas admite como máximo cada nivel de la estantería?", "45//3", "Se divide el peso máximo del nivel entre el peso de cada bolsa.", " bolsas"),
        ("=", "{F} ¿Cuántas bolsas llenas admite como máximo toda la estantería?", "4*(45//3)", "Se multiplican los niveles por las bolsas que admite cada nivel.", " bolsas"),
        ("abc", "{F} Una estudiante dice: «leí la ficha, así que puedo tomar muestras en el terreno». ¿Qué respuesta es correcta?", "Es falso: tomar muestras exige instructor autorizado, instructivos de la empresa y norma vigente", "Es cierto, si usa guantes y casco", "Es cierto, si registra bien cada muestra", "Un caso en papel no habilita para tomar muestras; el EPP o el registro tampoco."),
        ("abc", "Durante una visita de ejemplo, ves que una estantería con cajas se inclina hacia un pasillo con personas. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a sostener la estantería con las manos", "Sacar rápido las cajas del nivel más alto", "Intervenir sin formación puede causar un accidente mayor; se avisa a quienes pueden actuar."),
        ("abc", "En Geología: ¿por qué una muestra mal rotulada es un problema aunque esté bien tomada?", "Porque no se sabe de dónde viene y sus resultados no sirven para decidir", "Porque pesa más que las demás", "Porque ya no se puede guardar en una estantería", "Sin rótulo y registro, el resultado no se puede ligar a un lugar del terreno."),
        ("=", "{F} Se dejan 20 bolsas llenas en un solo nivel de la estantería. ¿Cuántos kilos exceden el máximo del nivel?", "20*3-45", "Se calcula el peso de las bolsas y se resta el máximo del nivel.", " kilos"),
        ("abc", "{F} Un asistente propone dejar bolsas de muestras abiertas en el terreno «un rato» para no cargarlas. ¿Qué corresponde?", "Que no: las muestras sin protección se contaminan o se pierden, y los residuos no se dejan en el terreno; se informa al responsable", "Que sí, si el clima está despejado", "Que sí, si se anota la hora en que se dejaron", "Una muestra desprotegida pierde valor y puede dañar el ambiente; el clima despejado no lo evita."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por «guardar y mover muestras» de su pequeña faena sin registros, porque «es solo ordenar bolsas». ¿Qué respondes?", "Que no, porque sin registros ni autorización se pierde la trazabilidad, y que lo consultarás con un adulto responsable", "Que sí, porque ordenar bolsas es fácil", "Que sí, si cada bolsa pesa poco", "Las muestras exigen registro y autorización; sin ellos pierden su valor y puede haber riesgos."),
    sc=[
        ("En Geología: ¿qué es la representatividad de una muestra?", "La capacidad de reflejar bien el conjunto del que sale", "Una muestra representativa permite decidir sobre el conjunto."),
        ("En el manejo de muestras: ¿qué es la cadena de custodia?", "El registro de quién tuvo la muestra, cuándo y dónde", "La cadena de custodia permite seguir la historia de la muestra."),
        ("¿Dónde conserva la empresa los registros del proyecto?", "En el data room, una carpeta o archivo ordenado", "El data room ordena los documentos de cada proyecto."),
    ],
    op=("Bodega de muestras de ejemplo del «Proyecto Cuenca Demo»: bolsas de 2 kilos; cada nivel de la estantería admite 30 kilos; la estantería tiene 5 niveles; una bolsa tiene el rótulo ilegible. Escribe (a) cuántas bolsas admite cada nivel, (b) cuántas admite toda la estantería, (c) un peligro de información y su riesgo, (d) un control administrativo, (e) qué haces si ves caer una caja desde un nivel alto en una visita real.",
        "(a) 30 ÷ 2 = 15 bolsas. (b) 5 × 15 = 75 bolsas. (c) Peligro: rótulo ilegible; riesgo: que la muestra se confunda con otra y sus resultados queden mal asignados. (d) Un letrero con el límite de peso por nivel y una revisión periódica. (e) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias. La tarea real la hace personal autorizado.",
        ["calcula bien las bolsas por nivel", "calcula bien las bolsas de toda la estantería", "distingue peligro y riesgo de información", "propone un control administrativo", "indica no acercarse y avisar"],
        ["hoja con las cinco respuestas"],
        ["multiplicar en vez de dividir", "proponer solo EPP", "responder que se acerca a ayudar"],
        "Pregunta: «¿qué pasa con los resultados si no se sabe de qué lugar es una muestra?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un rótulo con cinco datos para una bolsa de muestra y marca cuál de ellos es el código único.",
    extend="Explica con un ejemplo por qué el rótulo y el registro son tan importantes como la muestra misma.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). «Proyecto Altiplano Demo», lote 7. El lote tiene 40 muestras regulares de testigo; además se incluyen 2 duplicados (segunda muestra del mismo intervalo), 2 blancos (material sin mineral de interés) y 1 estándar (muestra de concentración conocida), todas en bolsas rotuladas. "
     "Ejemplo de rótulo: código M-0145; proyecto Altiplano Demo; fecha de ejemplo 12 de marzo; sondaje SD-02, intervalo de 20 a 22 metros; tipo testigo; responsable R2. Documentos: planilla de muestras, hoja de envío y cadena de custodia. "
     "Roles: geólogo jefe, asistente de geología, encargado de bodega de muestras y recepción del laboratorio.")
build(
    O5, 2, F,
    use="Aprenderé los tipos de muestra, qué son un duplicado, un blanco y un estándar, qué datos lleva un rótulo, los documentos de una muestra y el rol de cada persona, para leer una planilla en papel.",
    prior=["Sé qué es una muestra y la cadena de custodia.", "Sé leer una planilla escrita.", "Sé sumar y dividir números enteros."],
    explain=[
        "Según su origen, una muestra puede ser de roca (un fragmento), de testigo (un trozo del cilindro de un sondaje), de suelo o sedimento, o de ripios. Además de las muestras regulares se agregan muestras de control para comprobar la calidad de los resultados: el duplicado es una segunda muestra del mismo punto o intervalo, que permite ver si el resultado se repite; el blanco es material sin mineral de interés que sirve para detectar contaminación; el estándar es una muestra de concentración conocida que permite revisar si el laboratorio mide bien.",
        "El rótulo lleva un código único, el proyecto, la fecha, la ubicación o el intervalo, el tipo de muestra y el responsable. La planilla de muestras reúne todos esos datos de cada muestra; la hoja de envío lista lo que viaja al laboratorio; la cadena de custodia anota cada traspaso de responsable. Un registro útil se completa en el momento y no se cambia para que «se vea mejor».",
        f"El geólogo jefe define qué se necesita; el asistente de geología apoya con registros; el encargado de bodega recibe y guarda las muestras; la recepción del laboratorio las recibe y confirma lo que llega. {EMER} {AVISO}",
    ],
    vocab=[("muestra duplicada", "segunda muestra del mismo punto o intervalo, para comprobar si el resultado se repite"), ("blanco", "material sin mineral de interés que se agrega para detectar contaminación"), ("estándar", "muestra de concentración conocida que sirve para revisar al laboratorio"), ("rótulo", "etiqueta con los datos que identifican una muestra"), ("planilla de muestras", "registro con los datos de cada muestra"), ("hoja de envío", "lista de las muestras que viajan al laboratorio")],
    worked=[
        ("Total de bolsas", "Un lote de ejemplo tiene 30 muestras regulares, 1 duplicado y 1 blanco. ¿Cuántas bolsas se rotulan?", ["Se suman las muestras regulares y las de control.", "30 + 1 + 1 son 32 bolsas."], "32 bolsas"),
        ("Elegir el documento", "El encargado de bodega quiere dejar constancia de a quién entrega una caja de muestras y en qué fecha. ¿Qué documento usa?", ["Se trata de un traspaso de responsable.", "Ese registro es la cadena de custodia."], "La cadena de custodia"),
    ],
    mistakes=[("Creer que el blanco es una muestra sin importancia.", "El blanco sirve para detectar contaminación: si sale con mineral, algo se mezcló.", "El blanco se registra y se analiza como cualquier otra muestra."),
              ("Dejar el responsable en blanco del rótulo para completarlo después.", "Sin responsable no se puede seguir la cadena de custodia.", "Se completa en el momento, con fecha y responsable.")],
    T=[
        ("abc", "En Geología: ¿qué es una muestra duplicada?", "Una segunda muestra del mismo punto o intervalo para comprobar si el resultado se repite", "La misma bolsa registrada dos veces en la planilla", "Una muestra de otro sondaje con el mismo código", "El duplicado es una segunda muestra real; registrar dos veces una bolsa es un error de registro."),
        ("abc", "En Geología: ¿qué es un blanco?", "Material sin mineral de interés que se agrega para detectar contaminación", "Una bolsa que quedó vacía por error", "Una muestra con la etiqueta en blanco", "El blanco es un control con material limpio; no es una bolsa vacía ni sin rótulo."),
        ("abc", "En Geología: ¿qué es un estándar en un lote de muestras?", "Una muestra de concentración conocida que sirve para revisar si el laboratorio mide bien", "La muestra más común del lote", "La bolsa de mayor peso", "El estándar es un control de concentración conocida."),
        ("abc", "{F} ¿Qué dato del rótulo permite distinguir una muestra de todas las demás?", "El código único", "El nombre del proyecto", "El tipo de muestra", "Muchas muestras comparten proyecto y tipo; el código único es el que no se repite."),
        ("abc", "{F} ¿Qué documento acompaña a la muestra anotando cada traspaso de responsable?", "La cadena de custodia", "La planilla de muestras", "El rótulo de la bolsa", "La cadena registra quién tuvo la muestra y cuándo; la planilla reúne sus datos."),
        ("=", "{F} ¿Cuántas bolsas se rotulan en el lote, sumando regulares y de control?", "40+2+2+1", "Se suman las muestras regulares, los duplicados, los blancos y el estándar.", " bolsas"),
        ("=", "{F} ¿Cada cuántas muestras regulares hay un duplicado en el lote?", "40//2", "Se divide el número de muestras regulares entre el número de duplicados.", " muestras"),
        ("abc", "{F} ¿Para qué sirve incluir blancos en el lote?", "Para detectar si hubo contaminación durante el manejo o el análisis", "Para aumentar la cantidad de mineral del lote", "Para reemplazar las muestras que se pierdan", "El blanco no contiene mineral de interés, así que un resultado alto delata contaminación."),
        ("abc", "{F} El rótulo de una bolsa dice solo «testigo, 20–22 metros». ¿Qué datos le faltan?", "El código único, el proyecto, la fecha y el responsable", "El peso de la bolsa y el color de la roca", "La temperatura del día y el nombre del conductor", "El rótulo debe tener los datos que identifican la muestra y permiten seguirla."),
        ("abc", "{F} ¿Quién recibe las muestras en la bodega y las registra al guardarlas?", "El encargado de bodega de muestras", "El geólogo jefe, en la oficina", "La recepción del laboratorio", "El encargado de bodega recibe y guarda; la recepción del laboratorio recibe lo que llega a él."),
        ("abc", "{F} Un compañero propone no anotar en la planilla cuáles son los duplicados «para simplificar». ¿Qué respuesta es correcta?", "Es falso: se registran para poder interpretar luego los resultados de control", "Es cierto, porque se pueden adivinar después", "Es cierto, si el laboratorio también los ignora", "Sin registro de qué bolsa es un control, sus resultados no se pueden interpretar."),
        ("=", "{F} Si las 45 bolsas viajan en cajas de 9 bolsas, ¿cuántas cajas se necesitan?", "(40+2+2+1)//9", "Se divide el total de bolsas entre las que caben en cada caja.", " cajas"),
        ("abc", "{F} Al laboratorio llegan 44 bolsas y la hoja de envío dice 45. ¿Qué corresponde?", "Anotar la diferencia de una bolsa en la cadena de custodia, informar y buscar la bolsa antes de cerrar el registro", "Cambiar la hoja de envío a 44 para que coincida", "Esperar a que aparezca sola sin anotar nada", "Una diferencia se registra y se investiga; acomodar el número oculta la pérdida."),
    ],
    ctx=("abc", "Un compañero te dice que se puede completar el responsable de los rótulos al final del día, «de memoria». ¿Qué respondes?", "Que los datos se anotan en el momento y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, si se acuerdan bien", "Que sí, si lo firma el jefe sin revisar", "Un dato anotado de memoria puede fallar y rompe la cadena de custodia."),
    sc=[
        ("En Geología: ¿qué es un blanco?", "Material sin mineral de interés que se agrega para detectar contaminación", "El blanco es un control de contaminación."),
        ("En el manejo de muestras: ¿qué dato del rótulo identifica a cada muestra?", "El código único", "El código único no se repite entre muestras."),
        ("¿Qué documento anota cada traspaso de responsable de una muestra?", "La cadena de custodia", "La cadena de custodia sigue a la muestra hasta el laboratorio."),
    ],
    op=("Ficha de ejemplo: lote 9 del «Proyecto Cresta Demo», con 50 muestras regulares, 2 duplicados, 1 blanco y 1 estándar. Las bolsas viajan en cajas de 9 bolsas. Escribe (a) cuántas bolsas se rotulan, (b) cuántas cajas se necesitan, subiendo al entero, (c) tres datos que debe llevar el rótulo de cada bolsa, (d) qué documento anota quién entrega y quién recibe las cajas.",
        "(a) 50 + 2 + 1 + 1 = 54 bolsas. (b) 54 ÷ 9 = 6 cajas. (c) Por ejemplo, código único, fecha y responsable. (d) La cadena de custodia. La tarea real la hace personal autorizado.",
        ["suma bien las bolsas", "calcula bien las cajas", "nombra tres datos del rótulo", "nombra la cadena de custodia"],
        ["hoja con las cuatro respuestas"],
        ["olvidar las muestras de control", "confundir planilla con cadena de custodia", "dejar el rótulo sin código"],
        "Pregunta: «¿qué muestras son de control y cuáles regulares?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un lote con 20 muestras regulares y las de control que quieras, y calcula cuántas bolsas se rotulan.",
    extend="Explica con un ejemplo por qué un blanco con mineral alto es una señal de alerta.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (planilla de ejemplo, inventada). Sondaje SD-02 del «Proyecto Altiplano Demo»; todas las muestras son de testigo y cada una cubre 2 metros. Planilla: "
     "M-201, intervalo de 0 a 2 m, 3 de abril, responsable R1; M-202, de 2 a 4 m, 3 de abril, R1; M-203, de 4 a 6 m, 3 de abril, R1; M-203, de 6 a 8 m, 3 de abril, R2; M-205, de 8 a 10 m, 4 de abril, R2; M-206, de 10 a 12 m, sin fecha, R2. "
     "La hoja de envío lista 6 bolsas; la recepción del laboratorio anotó que recibió 5. Los códigos deben ser correlativos (cada uno es el siguiente al anterior) y no repetirse.")
build(
    O5, 3, F,
    use="Aprenderé a analizar una planilla de muestras en papel: detectar códigos repetidos, saltos en la secuencia y datos faltantes, y comparar la hoja de envío con la recepción, informando sin acomodar los datos.",
    prior=["Sé qué datos lleva un rótulo.", "Sé qué es la cadena de custodia.", "Sé sumar y restar números enteros."],
    explain=[
        "Analizar una planilla de muestras significa revisar cada fila con los mismos criterios. El código debe ser único y correlativo: si un código se repite, dos muestras distintas no se pueden distinguir, y si falta un número en la secuencia puede haber una muestra faltante o mal codificada. Cada fila debe tener todos sus datos: un registro incompleto, por ejemplo sin fecha, no permite seguir la historia de la muestra. Los intervalos de un mismo sondaje deben ser continuos y no superponerse.",
        "Luego se compara lo despachado con lo recibido: si la hoja de envío dice 6 bolsas y el laboratorio recibió 5, hay una diferencia que se anota en la cadena de custodia, se informa y se investiga. Los errores no se acomodan ni se suponen: un código repetido se resuelve revisando la bolsa y la libreta original, y un dato faltante se confirma con quien lo anotó. Las correcciones se hacen tachando, con fecha y firma.",
        f"Estos análisis los hace el asistente de geología bajo la supervisión del geólogo jefe. {EMER} {AVISO}",
    ],
    vocab=[("código repetido", "dos muestras distintas con el mismo código, que impide distinguirlas"), ("correlativo", "que sigue el orden consecutivo, sin saltos ni repeticiones"), ("registro incompleto", "registro al que le falta un dato obligatorio"), ("intervalo continuo", "intervalo que empieza donde termina el anterior"), ("diferencia de custodia", "disparidad entre lo despachado y lo recibido")],
    worked=[
        ("Salto en la secuencia", "Una planilla de ejemplo lista los códigos P-31, P-32, P-34 y P-35. ¿Qué observación corresponde?", ["Los códigos deben ser consecutivos.", "Falta P-33: puede haber una muestra faltante o mal codificada."], "Falta P-33 y debe revisarse"),
        ("Despachado y recibido", "Una hoja de envío de ejemplo lista 12 bolsas y el laboratorio recibió 12. ¿Hay diferencia de custodia?", ["Se comparan 12 y 12.", "Coinciden, así que no hay diferencia que informar."], "No hay diferencia"),
    ],
    mistakes=[("Rellenar un dato faltante con lo que «seguro fue».", "Un dato supuesto puede ser falso y arruina la trazabilidad.", "Se confirma con la libreta original o con quien lo anotó, y se corrige con firma."),
              ("Cambiar la hoja de envío para que coincida con lo que llegó.", "Se oculta la pérdida de una bolsa.", "Se anota la diferencia en la cadena de custodia, se informa y se busca la bolsa.")],
    T=[
        ("abc", "En Geología: ¿qué es un código repetido en una planilla de muestras?", "Dos muestras distintas con el mismo código, lo que impide distinguirlas", "Una muestra con un código más largo que las demás", "Una muestra registrada con la letra M", "Un código repetido hace que no se pueda saber a cuál muestra pertenece cada dato."),
        ("abc", "En Geología: ¿qué significa que los códigos sean correlativos?", "Que siguen un orden consecutivo, sin saltos ni repeticiones", "Que todos empiezan con la misma letra", "Que se anotan siempre en orden alfabético", "Correlativo significa consecutivo; un salto señala algo por revisar."),
        ("abc", "En Geología: ¿qué es un registro incompleto?", "Un registro al que le falta un dato obligatorio, como la fecha", "Un registro escrito con lápiz", "Un registro con más de seis filas", "El registro incompleto carece de datos obligatorios."),
        ("abc", "{F} ¿Qué error tienen las dos filas que llevan el código M-203?", "Dos muestras distintas tienen el mismo código", "Las dos muestras fueron tomadas en días distintos", "Las dos filas tienen la misma fecha", "El mismo código para intervalos distintos impide distinguirlas."),
        ("abc", "{F} ¿Qué código falta en la secuencia de la planilla?", "M-204", "M-207", "M-200", "Entre M-203 y M-205 falta el consecutivo M-204."),
        ("abc", "{F} ¿Qué dato falta en la fila M-206?", "La fecha", "El responsable", "El intervalo", "La fila indica «sin fecha»; el responsable R2 y el intervalo sí están."),
        ("=", "{F} ¿Cuántos metros de sondaje cubren en total las 6 muestras, si los intervalos son continuos?", "6*2", "Se multiplican las muestras por los metros que cubre cada una.", " metros"),
        ("=", "{F} ¿Cuántas filas de la planilla no tienen ningún problema?", "6-3", "Se restan a las seis filas las tres con problema: las dos M-203 y la M-206.", " filas"),
        ("=", "{F} ¿Cuántas bolsas faltan entre lo despachado y lo recibido?", "6-5", "Se resta lo recibido a lo despachado.", " bolsa"),
        ("abc", "{F} ¿Qué corresponde hacer con la bolsa que falta?", "Anotar la diferencia en la cadena de custodia, informar y buscar la bolsa", "Cambiar la hoja de envío a 5 bolsas", "No hacer nada, porque una bolsa no cambia el lote", "Una diferencia se registra y se investiga; cambiar la hoja oculta la pérdida."),
        ("abc", "{F} ¿Cómo se resuelve el código repetido de M-203?", "Revisando la bolsa física y la libreta original, y corrigiendo con firma", "Eligiendo el código que parezca mejor", "Borrando una de las filas de la planilla", "El error se resuelve con la evidencia original y no por conveniencia."),
        ("abc", "{F} Un compañero completa la fecha de M-206 con «4 de abril» porque «seguro fue ese día». ¿Qué corresponde responder?", "Que no se supone: la fecha se confirma con la libreta original o con quien la anotó", "Que sí, porque las otras muestras cercanas tienen esa fecha", "Que sí, si el laboratorio lo acepta", "Un dato supuesto puede ser falso; se confirma con la fuente."),
        ("abc", "{F} ¿Qué orden de análisis de la planilla es el adecuado?", "Revisar código, intervalo, fecha y responsable de cada fila, comparar con la hoja de envío y la recepción, informar y corregir con firma", "Corregir primero los códigos a mano, y revisar después si algo coincide", "Revisar solo la primera y la última fila, porque las del medio son iguales", "El análisis revisa cada fila y compara con los otros documentos antes de corregir."),
    ],
    ctx=("abc", "Un compañero propone borrar de la planilla de práctica las dos filas M-203 «para que se vea limpia» antes de entregarla. ¿Qué respondes?", "Que no se borran filas y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, si se vuelve a escribir una", "Que sí, porque una planilla limpia vale más", "Borrar filas oculta errores y rompe la trazabilidad; las correcciones se hacen con firma."),
    sc=[
        ("En Geología: ¿qué significa que los códigos de muestras sean correlativos?", "Que siguen un orden consecutivo, sin saltos ni repeticiones", "Un salto o una repetición señala algo que revisar."),
        ("En una planilla de muestras: ¿qué se hace con un dato faltante?", "Se confirma con la fuente original, no se supone", "Un dato supuesto puede ser falso."),
        ("¿Qué se hace si la hoja de envío y la recepción no coinciden?", "Se anota la diferencia en la cadena de custodia y se busca la muestra", "La diferencia se investiga y se informa."),
    ],
    op=("Planilla de ejemplo del «Proyecto Pampa Demo», sondaje SD-11, intervalos de 3 metros: N-51, de 0 a 3 m, 7 de mayo, R1; N-52, de 3 a 6 m, 7 de mayo, R1; N-53, de 6 a 9 m, sin fecha, R2; N-55, de 9 a 12 m, 8 de mayo, R2. La hoja de envío lista 4 bolsas y el laboratorio recibió 3. Escribe (a) qué código falta en la secuencia, (b) qué dato falta y en qué fila, (c) cuántos metros cubren las 4 muestras, (d) qué haces con la diferencia entre la hoja de envío y la recepción.",
        "(a) Falta N-54. (b) Falta la fecha, en la fila N-53. (c) 4 × 3 = 12 metros. (d) Se anota la diferencia de una bolsa en la cadena de custodia, se informa y se busca la bolsa. Todo se corrige con firma, sin suponer datos.",
        ["detecta el salto de código", "detecta el dato faltante", "calcula bien los metros", "trata la diferencia sin acomodar"],
        ["hoja con las cuatro respuestas"],
        ["no ver el salto N-54", "suponer la fecha", "cambiar la hoja de envío"],
        "Pregunta: «¿qué número debería seguir a N-53?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una planilla de cuatro muestras con un salto en los códigos y un dato faltante, y escribe qué errores tiene.",
    extend="Explica con un ejemplo por qué un dato supuesto es peor que un dato faltante.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). «Proyecto Altiplano Demo», sondaje SD-05 de 150 metros, con muestras de testigo que cubren 2 metros cada una. Controles de ejemplo (los reales los fija el proyecto): 1 duplicado cada 25 muestras regulares y 1 blanco cada 15 muestras regulares. "
     "Cada bolsa llena pesa 3 kilos y las cajas de despacho llevan 10 bolsas. El primer código del lote es M-0301 y los códigos son correlativos.")
build(
    O5, 4, F,
    use="Aprenderé a calcular en papel cuántas muestras y controles genera un sondaje, cuántas bolsas, cajas y kilos hay que despachar y cómo se codifican, y a ordenar versiones de los registros en el data room.",
    prior=["Sé qué son un duplicado y un blanco.", "Sé multiplicar y dividir números enteros.", "Sé redondear hacia arriba cuando no se puede usar una fracción."],
    explain=[
        "El intervalo de muestreo es la longitud de roca que representa cada muestra. Para saber cuántas muestras regulares genera un sondaje se divide su longitud entre el intervalo. Las muestras de control se calculan según la frecuencia que fije el proyecto: si hay un duplicado cada 25 muestras, se divide el número de muestras regulares entre 25. El total a rotular suma muestras regulares y de control.",
        "Con el total se calculan las cajas de despacho, dividiendo entre las bolsas por caja y subiendo al entero, y el peso, multiplicando por los kilos de cada bolsa. Los códigos son correlativos: si el primero es M-0101 y hay 40 bolsas, el último es el 40.º, es decir, el que resulta de sumar 39 al primero. Si se pierde una bolsa, su código no se reutiliza: se anota la pérdida y se informa. En el data room se guardan las versiones de la planilla con fecha y responsable, sin sobrescribir el historial.",
        f"Estos cálculos los revisa el geólogo jefe. Aquí aprendes el razonamiento con números de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("intervalo de muestreo", "longitud de roca que representa cada muestra"), ("muestra de control", "muestra extra, como un duplicado o un blanco, que comprueba la calidad de los resultados"), ("frecuencia de control", "cada cuántas muestras regulares se incluye un control"), ("despacho", "envío de las muestras al laboratorio"), ("versión", "estado de un documento en una fecha, que se guarda sin borrar las anteriores")],
    worked=[
        ("Cantidad de muestras", "Un sondaje de ejemplo de 60 metros se muestrea cada 3 metros. ¿Cuántas muestras regulares genera?", ["Se divide la longitud entre el intervalo.", "60 dividido por 3 da 20 muestras."], "20 muestras"),
        ("Controles y cajas", "Con 20 muestras regulares y un duplicado cada 10 muestras, ¿cuántas bolsas se rotulan, y cuántas cajas de 6 bolsas, sin otros controles?", ["Duplicados: 20 ÷ 10 = 2, y bolsas: 20 + 2 = 22.", "22 dividido por 6 es 3,67: se sube a 4 cajas."], "22 bolsas y 4 cajas"),
    ],
    mistakes=[("Reutilizar el código de una bolsa perdida para una muestra nueva.", "Se confunde la historia de ambas muestras y se rompe la trazabilidad.", "Se anota la pérdida con su explicación y se informa; el código no se reutiliza."),
              ("Sobrescribir la planilla cada día con el mismo nombre de archivo.", "Se pierde el historial y no se sabe qué cambió ni quién lo cambió.", "Se guardan versiones con fecha y responsable en el data room.")],
    T=[
        ("abc", "En Geología: ¿qué es el intervalo de muestreo?", "La longitud de roca que representa cada muestra, por ejemplo 2 metros", "El tiempo que pasa entre dos análisis del laboratorio", "La distancia entre el campamento y el sondaje", "El intervalo de muestreo es una longitud de roca por muestra."),
        ("abc", "En Geología: ¿qué es una muestra de control?", "Una muestra extra, como un duplicado o un blanco, que comprueba la calidad de los resultados", "La primera muestra de cada sondaje", "La muestra que se guarda en una vitrina", "Las muestras de control no son más muestras de roca de interés, sino comprobaciones de calidad."),
        ("abc", "En Geología: ¿qué es el data room de un proyecto?", "Una carpeta o archivo ordenado donde la empresa guarda los registros del proyecto", "El cuarto donde se guardan las muestras", "La sala de reuniones del campamento", "El data room guarda documentos y datos, no muestras ni reuniones."),
        ("=", "{F} ¿Cuántas muestras regulares genera el sondaje SD-05?", "150//2", "Se divide la longitud del sondaje entre los metros que cubre cada muestra.", " muestras"),
        ("=", "{F} ¿Cuántos duplicados se incluyen en total?", "(150//2)//25", "Se divide el número de muestras regulares entre la frecuencia de duplicados.", " duplicados"),
        ("=", "{F} ¿Cuántos blancos se incluyen en total?", "(150//2)//15", "Se divide el número de muestras regulares entre la frecuencia de blancos.", " blancos"),
        ("=", "{F} ¿Cuántas bolsas se rotulan en total, sumando regulares, duplicados y blancos?", "75+3+5", "Se suman las muestras regulares y las de control.", " bolsas"),
        ("=", "{F} Si el primer código es el 301 y hay 83 bolsas, ¿cuál es el número del último código del lote?", "301+83-1", "Se suma el total de bolsas al primer número y se resta 1.", ""),
        ("=", "{F} ¿Cuántas cajas de despacho se necesitan, subiendo al entero?", "(83+9)//10", "Se suman 9 antes de dividir entre 10 para subir al siguiente entero.", " cajas"),
        ("=", "{F} ¿Cuántos kilos pesan en total las 83 bolsas?", "83*3", "Se multiplican las bolsas por el peso de cada una.", " kilos"),
        ("abc", "{F} La última caja lleva solo 3 bolsas. ¿Qué conviene anotar en la hoja de envío?", "Cuántas bolsas lleva cada caja y los códigos de las bolsas de cada una, incluida la última", "Solo el número total de cajas", "Solo el peso total del lote", "Con el detalle por caja se puede verificar en el laboratorio que llegó todo."),
        ("abc", "{F} Se pierde la bolsa del código M-0320. ¿Qué corresponde?", "Anotar la pérdida con su explicación, informar y no reutilizar el código", "Usar el código M-0320 para una muestra nueva", "Renumerar todas las bolsas siguientes", "Reutilizar o renumerar rompe la trazabilidad; la pérdida se registra."),
        ("abc", "{F} Un asistente guarda la planilla cada día con el mismo nombre, sobrescribiendo el archivo anterior. ¿Qué conviene?", "Guardar versiones con fecha y responsable en el data room, sin sobrescribir el historial", "Seguir sobrescribiendo, porque solo importa la última", "Borrar las versiones viejas cuando termine la semana", "Conservar versiones permite saber qué cambió, cuándo y quién lo cambió."),
    ],
    ctx=("abc", "Un conocido te pide que prepares con estos cálculos el despacho de muestras de su pequeña faena real, sin consultar a nadie. ¿Qué respondes?", "Que los números del cuaderno son de ejemplo y que el despacho real lo prepara personal autorizado con los instructivos del proyecto; lo consultarás con un adulto responsable", "Que sí, porque los cálculos están bien", "Que sí, si cambias los códigos para no confundir", "Los valores son de ejemplo; los reales los fija el proyecto y los revisa personal autorizado."),
    sc=[
        ("En Geología: ¿cómo se calcula el número de muestras regulares de un sondaje?", "Se divide la longitud del sondaje entre el intervalo de muestreo", "El intervalo de muestreo es el largo de roca de cada muestra."),
        ("En la preparación de un despacho de muestras: ¿cuándo se redondea hacia arriba?", "Cuando se calculan cajas y no se puede usar una fracción de caja", "Una fracción de caja no existe."),
        ("¿Qué se hace con el código de una bolsa perdida?", "No se reutiliza: se anota la pérdida y se informa", "Reutilizarlo confundiría la historia de dos muestras."),
    ],
    op=("Ficha de ejemplo: sondaje SD-12, «Proyecto Cuenca Demo», de 120 metros, con muestras cada 2 metros; un duplicado cada 20 muestras regulares y un blanco cada 30; cada bolsa pesa 2 kilos; cajas de 8 bolsas; el primer código es el 501. Escribe (a) cuántas muestras regulares hay, (b) cuántas bolsas se rotulan en total, (c) cuántas cajas se necesitan, subiendo al entero, (d) cuál es el último número de código.",
        "(a) 120 ÷ 2 = 60 muestras. (b) Duplicados: 60 ÷ 20 = 3; blancos: 60 ÷ 30 = 2; total 60 + 3 + 2 = 65 bolsas. (c) 65 ÷ 8 = 8,1, se sube a 9 cajas. (d) 501 + 65 − 1 = 565. Los cálculos reales los revisa el geólogo jefe.",
        ["calcula las muestras regulares", "suma bien los controles", "sube al entero las cajas", "calcula bien el último código"],
        ["hoja con las cuatro respuestas"],
        ["olvidar los controles", "redondear hacia abajo las cajas", "olvidar restar 1 en el último código"],
        "Pregunta: «¿cuántas bolsas hay en total antes de calcular las cajas?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula las muestras regulares de un sondaje inventado de 80 metros con muestras cada 2 metros.",
    extend="Explica con un ejemplo por qué conviene guardar versiones de una planilla en lugar de sobrescribirla.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En la «Sala de revisión Demo» de la empresa ficticia «Minera Demo» hay una mesa con 6 muestras de ejemplo, con etiqueta: cuarzo, calcita, pirita, calcopirita, galena y magnetita; cada muestra pesa 400 gramos (dato de ejemplo). "
     "Peligros anotados: fragmentos con bordes filosos, polvo al manipular las muestras, manos sin lavar después de tocarlas (algunos minerales, como la galena, contienen plomo), iluminación insuficiente, cajas pesadas y la tentación de probar u oler de cerca una muestra.")
build(
    O6, 1, F,
    use="Aprenderé qué es un mineral y qué es una roca, qué significa observar de forma macroscópica, por qué estimar la calidad a simple vista no reemplaza al laboratorio y qué reglas de higiene y prevención se aplican al revisar muestras.",
    prior=["Sé qué es una muestra geológica y su rótulo.", "Sé distinguir peligro y riesgo.", "Sé la jerarquía de controles."],
    explain=[
        "Un mineral es una sustancia sólida natural, inorgánica, con composición química definida y estructura ordenada, como el cuarzo o la calcita. Una roca es un agregado de uno o más minerales. Observar de forma macroscópica es mirar la muestra a simple vista o con una lupa de mano, sin análisis de laboratorio. Con esa observación se pueden reconocer propiedades como el color, la textura y la dureza, y estimar si la muestra tiene minerales de interés y en qué proporción.",
        "La calidad de un mineral, es decir, cuánto elemento útil contiene, se llama ley y solo se confirma con análisis de laboratorio: la observación macroscópica es una estimación inicial, no una medición. Revisar muestras tiene peligros: bordes filosos, polvo, bolsas pesadas y manos contaminadas. Algunos minerales contienen metales que no deben ingerirse, por eso nunca se prueban, no se huelen de cerca, no se come ni se bebe en la mesa de revisión y se lavan las manos al terminar. Los controles siguen la jerarquía: reglas de higiene (administrativo) y guantes y lentes (EPP).",
        f"Esta tarea exige instructor autorizado y norma vigente; las muestras reales no se rompen ni se manipulan sin autorización. {EMER} {AVISO}",
    ],
    vocab=[("mineral", "sustancia sólida natural, inorgánica, de composición química definida y estructura ordenada"), ("roca", "agregado de uno o más minerales"), ("macroscópico", "observado a simple vista o con lupa de mano"), ("ley", "cantidad de elemento útil que contiene un mineral o una roca, confirmada por laboratorio"), ("estimación", "valor aproximado que se confirma después con una medición")],
    worked=[
        ("Peligro y riesgo", "Una mesa de revisión de ejemplo tiene bolsas abiertas con polvo de roca y no hay lavamanos cerca. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el polvo de roca y las manos sin lavar.", "El riesgo es respirar el polvo o ingerir restos si se come sin lavarse."], "Peligro: polvo de roca y manos sin lavar; riesgo: inhalar o ingerir restos de mineral"),
        ("Clasificar un control", "Una regla escrita prohíbe comer y beber en la mesa de revisión de muestras. ¿A qué nivel de la jerarquía corresponde?", ["Una regla escrita ordena la conducta.", "No cambia el lugar ni equipa a nadie: es administrativo."], "Control administrativo"),
    ],
    mistakes=[("Creer que se puede probar o oler de cerca una muestra para identificarla.", "Algunos minerales son tóxicos y el polvo puede dañar el cuerpo.", "Se observa con lupa a distancia y se registra lo que se ve."),
              ("Creer que identificar un mineral a simple vista dice cuánto vale la muestra.", "El valor depende de la ley, que se confirma con laboratorio.", "La observación macroscópica es una estimación inicial.")],
    T=[
        ("abc", "En Geología: ¿qué es un mineral?", "Una sustancia sólida natural, inorgánica, de composición química definida y estructura ordenada", "Cualquier roca grande que se encuentra en una faena", "Un material fabricado en un laboratorio", "Un mineral es natural y de composición definida; las rocas y los materiales fabricados son otra cosa."),
        ("abc", "En Geología: ¿qué es una roca?", "Un agregado de uno o más minerales", "Un único cristal puro de un solo mineral", "Un mineral que ya fue analizado en laboratorio", "La roca es un conjunto de minerales; un cristal único sería un mineral."),
        ("abc", "En Geología: ¿qué significa observar una muestra de forma macroscópica?", "Mirarla a simple vista o con lupa de mano, sin análisis de laboratorio", "Mirarla con un microscopio electrónico", "Medir su concentración con un instrumento de laboratorio", "Macroscópico significa visible a simple vista o con lupa simple."),
        ("abc", "{F} ¿Por qué se pide lavarse las manos después de manipular muestras, aunque parezcan inofensivas?", "Porque algunos minerales contienen metales, como el plomo, que no deben ingerirse", "Porque las muestras se mojan con facilidad", "Porque las manos sucias borran los rótulos", "El riesgo es ingerir restos de minerales dañinos; el agua y los rótulos no son la razón."),
        ("abc", "{F} Una regla escrita que prohíbe comer y beber en la mesa de revisión es un control de tipo:", "Administrativo, porque ordena la conducta de las personas", "De ingeniería, porque cambia la mesa", "De EPP, porque protege el cuerpo de quien la usa", "Una regla escrita no cambia el lugar ni es un equipo personal."),
        ("abc", "{F} Guantes y lentes de seguridad usados al revisar las muestras son controles de tipo:", "EPP, porque protegen solo a quien los usa", "De eliminación, porque quitan el polvo", "Administrativo, porque son una regla escrita", "El EPP protege a la persona pero no elimina el peligro."),
        ("=", "{F} ¿Cuántos gramos pesan juntas las 6 muestras de la mesa?", "6*400", "Se multiplica el número de muestras por el peso de cada una.", " gramos"),
        ("abc", "{F} Un estudiante dice: «para identificar un mineral hay que probarlo con la lengua». ¿Qué respuesta es correcta?", "Es falso: las muestras no se prueban ni se huelen de cerca, porque algunos minerales son dañinos", "Es cierto, si la muestra está limpia", "Es cierto, si se lava después con agua", "Probar una muestra puede ser dañino y no es un método de identificación seguro."),
        ("abc", "Durante una visita de ejemplo, se rompe una caja con muestras y se levanta mucho polvo en la sala. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a barrer el polvo con las manos", "Soplar el polvo para que se disperse", "El polvo puede dañar; se avisa a quienes pueden actuar y no se interviene sin formación."),
        ("abc", "En Geología: ¿por qué la identificación macroscópica no basta para decir cuánto vale una muestra?", "Porque la calidad, o ley, se confirma con análisis de laboratorio", "Porque a simple vista no se puede ver ninguna propiedad", "Porque el laboratorio siempre da el mismo resultado", "La observación es una estimación inicial; la ley se mide en laboratorio."),
        ("abc", "{F} Un compañero acerca una muestra a su nariz «para ver a qué huele». ¿Qué corresponde?", "Que no se huele de cerca ni se prueba: se observa con lupa a distancia", "Que se puede, si la muestra es pequeña", "Que se puede, si se hace una sola vez", "El tamaño o la frecuencia no vuelven segura la inhalación de polvo de una muestra."),
        ("=", "{F} Si cada bandeja de la sala admite 3 muestras de 400 gramos, ¿cuántos gramos pesa cada bandeja llena?", "3*400", "Se multiplican las muestras de una bandeja por el peso de cada una.", " gramos"),
        ("abc", "{F} El jefe pide revisar todas las muestras sin guantes ni lavamanos porque «es más rápido». ¿Cuál es la mejor respuesta?", "Que la rapidez no justifica el riesgo: se aplican reglas de higiene, lavamanos y guantes", "Que está bien, porque son pocas muestras", "Que está bien, si se revisan en silencio", "Los controles de higiene protegen la salud aunque haya pocas muestras."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por revisar y romper unas rocas de su faena «porque ya sabes distinguir minerales». ¿Qué respondes?", "Que no, porque manipular y romper rocas exige personal autorizado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si te pones guantes", "Que sí, si usas un martillo pequeño", "Haber estudiado el concepto no habilita para manipular o romper rocas."),
    sc=[
        ("En Geología: ¿qué es un mineral?", "Una sustancia sólida natural, inorgánica, de composición química definida y estructura ordenada", "Un mineral tiene composición definida y estructura ordenada."),
        ("En la revisión de muestras: ¿qué significa observar de forma macroscópica?", "Mirar a simple vista o con lupa de mano, sin laboratorio", "Lo macroscópico se ve sin instrumentos de laboratorio."),
        ("¿Qué confirma la calidad, o ley, de una muestra?", "El análisis de laboratorio", "La observación a simple vista es solo una estimación."),
    ],
    op=("Mesa de revisión de ejemplo del «Proyecto Pampa Demo»: 7 muestras de 300 gramos cada una, fragmentos con bordes filosos y una lámpara que ilumina poco. Escribe (a) cuántos gramos pesan las 7 muestras, (b) el peligro de los bordes filosos y su riesgo, (c) un control administrativo y un EPP, (d) por qué la observación a simple vista no confirma la ley de una muestra, (e) qué haces si ves caer a una persona con una caja pesada de muestras en una visita real.",
        "(a) 7 × 300 = 2.100 gramos. (b) Peligro: los bordes filosos de los fragmentos; riesgo: cortarse las manos. (c) Administrativo: una regla escrita de revisar las muestras solo con buena iluminación y sobre una bandeja; EPP: guantes y lentes. (d) Porque la ley se confirma con análisis de laboratorio y la observación es una estimación inicial. (e) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias. La revisión real la hace personal autorizado.",
        ["calcula bien el peso total", "distingue peligro y riesgo", "propone un control administrativo y un EPP", "explica que la ley se confirma en laboratorio", "indica no acercarse y avisar"],
        ["hoja con las cinco respuestas"],
        ["llamar riesgo al borde filoso mismo", "afirmar que se puede conocer la ley a simple vista", "responder que se acerca a mover la caja"],
        "Pregunta: «¿qué pasa si alguien prueba una muestra con la boca?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres reglas de higiene para una mesa de revisión de muestras y di si cada una es administrativa o de EPP.",
    extend="Explica con un ejemplo por qué una estimación a simple vista puede equivocarse.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (tabla de referencia de ejemplo, con minerales conocidos y propiedades generales). Cuarzo: brillo vítreo, incoloro o blanco, raya blanca, sin planos de exfoliación (rompe en superficies curvas), dureza 7. "
     "Calcita: brillo vítreo, blanca, raya blanca, exfoliación en tres direcciones, dureza 3. Pirita: brillo metálico, amarillo latón pálido, raya negra verdosa. Calcopirita: brillo metálico, amarillo latón más intenso, raya negra verdosa. "
     "Galena: brillo metálico, gris plomo, raya gris plomo, muy pesada para su tamaño, exfoliación cúbica. Magnetita: negra, brillo metálico, raya negra, atrae un imán. "
     "Escala de dureza de Mohs: 1 talco, 2 yeso, 3 calcita, 4 fluorita, 5 apatito, 6 ortoclasa, 7 cuarzo, 8 topacio, 9 corindón, 10 diamante. Un mineral raya a otro si es más duro. Documento: la ficha de descripción macroscópica (registro de lo observado con fecha y responsable).")
build(
    O6, 2, F,
    use="Aprenderé las propiedades que se observan en un mineral (color, raya, brillo, dureza, exfoliación y fractura), la escala de Mohs y cómo se registra la observación en una ficha, usando una tabla de referencia.",
    prior=["Sé qué es un mineral y qué significa macroscópico.", "Sé leer una tabla escrita.", "Sé restar números enteros."],
    explain=[
        "Para distinguir un mineral a simple vista se combinan varias propiedades, porque una sola puede engañar. El color es lo primero que se ve, pero puede variar de una muestra a otra. La raya es el color del polvo del mineral al frotarlo sobre porcelana sin esmaltar y es más constante que el color. El brillo es la forma en que refleja la luz: metálico, como en la pirita, o no metálico, como el brillo vítreo del cuarzo. La textura es el tamaño y la forma de los granos.",
        "La dureza es la resistencia de un mineral a ser rayado. La escala de Mohs la ordena de 1 a 10 con minerales de referencia; un mineral raya a otro si es más duro, y si no se rayan entre sí tienen una dureza parecida. La exfoliación es la propiedad de romperse en planos lisos; cuando el mineral rompe en superficies irregulares o curvas se llama fractura. Otras propiedades son el peso relativo, si es muy pesado para su tamaño, y el magnetismo, si atrae un imán.",
        f"La observación se anota en la ficha de descripción macroscópica, con fecha y responsable, y no se altera. El geólogo identifica, el asistente de geología registra y el laboratorio confirma. {EMER} {AVISO}",
    ],
    vocab=[("raya", "color del polvo de un mineral al frotarlo sobre porcelana sin esmaltar"), ("brillo", "manera en que un mineral refleja la luz, metálico o no metálico"), ("dureza", "resistencia de un mineral a ser rayado"), ("escala de Mohs", "lista de 10 minerales de referencia ordenados de menor a mayor dureza"), ("exfoliación", "propiedad de romperse en planos lisos"), ("fractura", "forma de romperse en superficies irregulares o curvas"), ("textura", "tamaño y forma de los granos de una roca o mineral")],
    worked=[
        ("Comparar durezas", "Un mineral de ejemplo raya a la fluorita y es rayado por la ortoclasa. ¿Entre qué valores de la escala de Mohs está su dureza?", ["Rayar a la fluorita significa que es más duro que 4.", "Ser rayado por la ortoclasa significa que es más blando que 6."], "Entre 4 y 6"),
        ("Raya y color", "Dos minerales de ejemplo tienen el mismo color verde, pero uno deja raya blanca y el otro raya verde clara. ¿Qué indica esa diferencia?", ["El color puede coincidir en minerales distintos.", "La raya difiere, así que se trata de minerales diferentes."], "Son minerales diferentes, aunque se vean del mismo color"),
    ],
    mistakes=[("Identificar un mineral solo por su color.", "El color puede variar o coincidir entre minerales distintos.", "Se combinan varias propiedades, como raya, brillo y dureza."),
              ("Creer que un mineral de dureza 7 es rayado por uno de dureza 3.", "El mineral más duro raya al más blando, no al revés.", "El cuarzo (7) raya a la calcita (3), y la calcita no raya al cuarzo.")],
    T=[
        ("abc", "En Geología: ¿qué es la raya de un mineral?", "El color de su polvo al frotarlo sobre porcelana sin esmaltar", "El surco que deja al ser rayado por otro mineral", "La línea por donde se rompe en planos lisos", "La raya es el color del polvo, no un surco ni un plano de ruptura."),
        ("abc", "En Geología: ¿qué es el brillo de un mineral?", "La manera en que refleja la luz, por ejemplo metálico o vítreo", "El tamaño de sus granos", "La resistencia que tiene a ser rayado", "El brillo describe cómo refleja la luz; el tamaño de grano es la textura y la resistencia es la dureza."),
        ("abc", "En Geología: ¿qué es la dureza de un mineral?", "Su resistencia a ser rayado", "Su peso en una balanza", "Su capacidad de atraer un imán", "La dureza mide la resistencia a ser rayado; el peso y el magnetismo son otras propiedades."),
        ("abc", "{F} ¿Qué mineral de la tabla tiene exfoliación en tres direcciones?", "La calcita", "El cuarzo", "La pirita", "La tabla indica exfoliación en tres direcciones para la calcita; el cuarzo no tiene planos de exfoliación."),
        ("abc", "{F} ¿Qué mineral tiene brillo metálico, color amarillo latón pálido y raya negra verdosa?", "La pirita", "La galena", "El cuarzo", "La pirita es la que tiene ese color y esa raya; la galena es gris plomo y el cuarzo, vítreo."),
        ("=", "{F} ¿Cuántos puntos de la escala de Mohs separan la dureza del cuarzo de la de la calcita?", "7-3", "Se resta la dureza de la calcita a la del cuarzo.", " puntos"),
        ("abc", "{F} Entre la calcita y el apatito, ¿cuál raya a cuál?", "El apatito raya a la calcita, porque es más duro (5 contra 3)", "La calcita raya al apatito, porque tiene exfoliación", "Ninguno raya al otro, porque tienen dureza parecida", "El más duro raya al más blando: 5 raya a 3."),
        ("abc", "{F} Un mineral raya al yeso y es rayado por la calcita. ¿Entre qué valores de la escala está su dureza?", "Entre 2 y 3", "Entre 3 y 7", "Entre 1 y 2", "Rayar al yeso lo hace más duro que 2; ser rayado por la calcita lo hace más blando que 3."),
        ("abc", "{F} ¿Por qué la raya es más confiable que el color para distinguir minerales?", "Porque el color puede variar entre muestras del mismo mineral y la raya es más constante", "Porque la raya siempre es negra", "Porque el color no se puede ver con luz natural", "La raya depende menos de impurezas y del aspecto superficial que el color."),
        ("abc", "{F} Una muestra incolora rompe en superficies curvas, sin planos lisos. ¿Qué propiedad describe esa rotura?", "Fractura, porque no hay planos lisos de ruptura", "Exfoliación, porque se rompe en superficies", "Raya, porque deja un polvo", "La exfoliación exige planos lisos; las superficies curvas son fractura."),
        ("abc", "{F} Una asistente anota en la ficha «mineral bonito, brilla mucho». ¿Por qué es una descripción débil?", "Porque no describe propiedades observables como color, raya, brillo, dureza o exfoliación", "Porque las fichas no admiten comentarios", "Porque «brilla» es una propiedad que nunca se anota", "Un registro útil describe propiedades que otro pueda comprobar."),
        ("=", "{F} ¿Cuántos minerales de la escala de Mohs son más duros que la calcita?", "10-3", "Se restan al total de 10 minerales los que llegan hasta la calcita, que es el tercero.", " minerales"),
        ("abc", "{F} Un compañero dice: «como el diamante tiene dureza 10, el cuarzo, de dureza 7, lo raya». ¿Qué respuesta es correcta?", "Es falso: el diamante es más duro y raya al cuarzo, no al revés", "Es cierto, porque el cuarzo es más común", "Es cierto, porque 7 es un valor mayor que 3", "El más duro raya al más blando; 10 es mayor que 7."),
    ],
    ctx=("abc", "Una compañera te propone anotar en la ficha de descripción la propiedad que «debería» tener cada muestra, sin observarla, para terminar antes. ¿Qué respondes?", "Que no se anota lo que no se observó y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, si coincide con el nombre del mineral", "Que sí, y se corrige si alguien lo nota", "Anotar lo no observado falsea el registro."),
    sc=[
        ("En Geología: ¿qué es la dureza?", "La resistencia de un mineral a ser rayado", "La escala de Mohs ordena minerales según su dureza."),
        ("En la identificación de minerales: ¿qué es la exfoliación?", "La propiedad de romperse en planos lisos", "Si no hay planos lisos, la rotura se llama fractura."),
        ("¿Qué mineral raya a cuál: uno de dureza 7 o uno de dureza 3?", "El de dureza 7 raya al de dureza 3", "El mineral más duro raya al más blando."),
    ],
    op=("Ficha de ejemplo, con la escala de Mohs de esta clase. Una muestra del «Proyecto Cuenca Demo» es gris plomo, de brillo metálico, deja raya gris plomo y se rompe en pequeños cubos. Otra es incolora, de brillo vítreo, raya blanca, sin planos de exfoliación, y raya a la ortoclasa pero no al topacio. Escribe (a) qué propiedades de la primera muestra usarías para comparar con la tabla, (b) entre qué valores está la dureza de la segunda, (c) por qué no usarías solo el color, (d) qué debe llevar la ficha de descripción de cada muestra.",
        "(a) Color, brillo, raya y exfoliación. (b) Entre 6 y 8, porque raya a la ortoclasa, de 6, y no raya al topacio, de 8. (c) Porque el color puede variar entre muestras o coincidir entre minerales distintos. (d) Las propiedades observadas, la fecha y el responsable. La identificación definitiva y la ley las confirma el laboratorio.",
        ["nombra propiedades útiles", "acota la dureza con la escala", "explica por qué no basta el color", "indica fecha y responsable en la ficha"],
        ["hoja con las cuatro respuestas"],
        ["usar solo el color", "invertir quién raya a quién", "olvidar fecha y responsable"],
        "Pregunta: «¿qué mineral de la escala es el más cercano por abajo y cuál por arriba?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Usa la escala de Mohs de esta clase para decidir qué mineral raya a cuál en tres pares inventados.",
    extend="Explica con un ejemplo por qué se necesitan varias propiedades para identificar un mineral.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (observaciones de ejemplo, inventadas). Tabla de referencia, con minerales conocidos y propiedades generales: cuarzo, brillo vítreo, raya blanca, dureza 7, sin exfoliación; calcita, brillo vítreo, raya blanca, dureza 3, exfoliación en tres direcciones; "
     "pirita, brillo metálico, amarillo latón pálido, raya negra verdosa, dureza 6; calcopirita, brillo metálico, amarillo latón más intenso, raya negra verdosa, dureza entre 3 y 4; galena, brillo metálico, gris plomo, raya gris plomo, dureza entre 2 y 3, muy pesada, exfoliación cúbica; "
     "magnetita, negra, brillo metálico, raya negra, atrae un imán. Escala de Mohs: 3 calcita, 4 fluorita, 5 apatito, 6 ortoclasa, 7 cuarzo, 8 topacio. "
     "Observaciones: muestra A, gris plomo, brillo metálico, raya gris plomo, se rompe en pequeños cubos y es muy pesada para su tamaño; muestra B, amarillo latón pálido, brillo metálico, raya negra verdosa, raya al apatito; "
     "muestra C, amarillo latón intenso, brillo metálico, raya negra verdosa, es rayada por la fluorita; muestra D, negra, brillo metálico, raya negra, atrae un imán; "
     "muestra E, incolora, brillo vítreo, raya blanca, sin exfoliación, raya a la ortoclasa; muestra F, anotada como cuarzo, pero con brillo metálico y raya negra verdosa. "
     "Criterio de ejemplo del proyecto: las muestras con sulfuros de cobre, como la calcopirita, pasan a análisis prioritario del laboratorio.")
build(
    O6, 3, F,
    use="Aprenderé a analizar en papel una ficha de observaciones: comparar las propiedades con una tabla de referencia, descartar candidatos, detectar observaciones contradictorias y decidir qué muestras pasan a análisis prioritario.",
    prior=["Sé las propiedades de un mineral: color, raya, brillo, dureza y exfoliación.", "Sé usar la escala de Mohs.", "Sé leer una tabla escrita."],
    explain=[
        "Para identificar una muestra se comparan sus propiedades con una tabla de referencia. Conviene usar al menos dos propiedades que distingan a los candidatos: si dos minerales comparten color y brillo, como la pirita y la calcopirita, se distinguen por la dureza o por otro dato. Descartar un candidato significa excluirlo porque una propiedad observada no coincide con la suya. Una observación contradictoria es la que no coincide con el mineral que se había supuesto.",
        "Cuando hay contradicción no se deja el nombre más cómodo: se reobserva la muestra, se revisa la tabla y se consulta a quien corresponde. La identificación a simple vista es una estimación; el criterio del proyecto decide qué muestras pasan antes al laboratorio, por ejemplo las que parecen tener sulfuros de cobre. El laboratorio confirma el mineral y la ley. Nunca se concluye el valor de una muestra solo por su aspecto.",
        f"Estos análisis los hace el geólogo con apoyo del asistente de geología; aquí practicas el razonamiento. {EMER} {AVISO}",
    ],
    vocab=[("descartar", "excluir un candidato porque una propiedad observada no coincide con la suya"), ("observación contradictoria", "propiedad observada que no coincide con el mineral que se había supuesto"), ("análisis prioritario", "análisis de laboratorio que se hace antes por el posible interés de la muestra"), ("sulfuro", "mineral formado por azufre combinado con uno o más metales"), ("reobservar", "volver a mirar una muestra para comprobar una propiedad")],
    worked=[
        ("Descartar candidatos", "Una muestra de ejemplo es incolora, de brillo vítreo y raya blanca, y es rayada por el cuarzo. ¿Puede ser cuarzo?", ["Si es rayada por el cuarzo, es más blanda que 7.", "El cuarzo tiene dureza 7: la muestra no puede ser cuarzo."], "No puede ser cuarzo"),
        ("Observación contradictoria", "Una ficha de ejemplo dice «galena», pero la muestra es incolora, de brillo vítreo y no es pesada. ¿Qué corresponde?", ["La galena es gris plomo, metálica y muy pesada.", "Hay contradicción: se reobserva la muestra y se consulta antes de dejar el nombre."], "Reobservar y consultar; no dejar «galena»"),
    ],
    mistakes=[("Dejar anotado un nombre cuando una propiedad observada lo contradice.", "Un nombre equivocado puede llevar a decisiones equivocadas.", "Se reobserva, se compara con la tabla y se consulta."),
              ("Dar por seguro el valor de una muestra solo porque se parece a un mineral de interés.", "La ley y la identificación definitiva las confirma el laboratorio.", "La muestra se envía a análisis; no se concluye el valor por su aspecto.")],
    T=[
        ("abc", "En Geología: ¿qué significa descartar un candidato al identificar un mineral?", "Excluirlo porque una propiedad observada no coincide con la suya", "Escribir su nombre en la ficha para revisarlo después", "Elegirlo por ser el más común", "Descartar es excluir un mineral cuando una propiedad no coincide."),
        ("abc", "En Geología: ¿qué es una observación contradictoria?", "Una propiedad observada que no coincide con el mineral que se había supuesto", "Una observación escrita por dos personas", "Una observación hecha con lupa", "La contradicción aparece cuando una propiedad no calza con el nombre supuesto."),
        ("abc", "En Geología: ¿qué es una muestra de análisis prioritario?", "Una muestra que, según el criterio del proyecto, pasa antes al laboratorio por su posible interés", "Una muestra que ya fue analizada dos veces", "La muestra de mayor peso del lote", "El análisis prioritario se decide con el criterio del proyecto, no por el peso ni por repetición."),
        ("abc", "{F} ¿Qué mineral de la tabla corresponde a la muestra A?", "Galena", "Pirita", "Calcita", "Gris plomo, raya gris plomo, cubos y muy pesada son propiedades de la galena."),
        ("abc", "{F} ¿Qué mineral de la tabla corresponde a la muestra E?", "Cuarzo", "Calcita", "Magnetita", "Vítreo, raya blanca, sin exfoliación y capaz de rayar la ortoclasa (6) indica dureza 7: cuarzo."),
        ("abc", "{F} ¿Qué mineral de la tabla corresponde a la muestra D?", "Magnetita", "Galena", "Pirita", "Negra, raya negra y atracción por el imán caracterizan a la magnetita."),
        ("abc", "{F} Las muestras B y C son ambas amarillo latón, metálicas y de raya negra verdosa. ¿Qué propiedad permite distinguirlas?", "La dureza: B raya al apatito y C es rayada por la fluorita", "El color, que es exactamente el mismo", "La raya, que es distinta en cada una", "Color, brillo y raya coinciden; la dureza las separa."),
        ("abc", "{F} ¿Qué mineral de la tabla es la muestra B?", "Pirita, porque su dureza es mayor que 5", "Calcopirita, porque su dureza está entre 3 y 4", "Galena, porque es metálica", "Rayar al apatito (5) implica dureza mayor que 5, que corresponde a la pirita (6)."),
        ("abc", "{F} ¿Qué mineral de la tabla es la muestra C?", "Calcopirita, porque su dureza es menor que 4", "Pirita, porque su dureza es 6", "Cuarzo, porque brilla", "Ser rayada por la fluorita (4) implica dureza menor que 4, como la calcopirita."),
        ("abc", "{F} Según el criterio de ejemplo del proyecto, ¿qué muestra pasa a análisis prioritario?", "La muestra C, por ser calcopirita, un sulfuro de cobre", "La muestra B, por ser más dura", "La muestra A, por ser más pesada", "El criterio prioriza sulfuros de cobre; la calcopirita es el de la tabla."),
        ("abc", "{F} La muestra F está anotada como cuarzo, pero tiene brillo metálico y raya negra verdosa. ¿Qué corresponde?", "Reconocer una contradicción, reobservarla y consultar antes de dejar el nombre", "Dejar «cuarzo», porque ya está anotado", "Cambiar la raya a blanca para que coincida", "El cuarzo tiene brillo vítreo y raya blanca; la ficha se corrige con evidencia, no al revés."),
        ("abc", "{F} Un compañero dice: «B y C son el mismo mineral, porque son amarillas y metálicas». ¿Qué respuesta es correcta?", "Es falso: difieren en dureza y por eso son pirita y calcopirita", "Es cierto, porque el color es igual", "Es cierto, porque ambas tienen raya negra verdosa", "Color y raya coinciden, pero la dureza demuestra que son minerales distintos."),
        ("abc", "{F} ¿Cuántas de las muestras A a E tienen brillo metálico?", "Cuatro: A, B, C y D", "Tres: A, B y C", "Cinco: A, B, C, D y E", "E es de brillo vítreo; las otras cuatro son metálicas."),
    ],
    ctx=("abc", "Una compañera te sugiere anotar «calcopirita» en las muestras B y F, aunque no calcen, «para que el lote tenga más cobre». ¿Qué respondes?", "Que no se anotan nombres que la observación no respalda y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, porque más cobre es mejor", "Que sí, y se corrige después del análisis", "Un nombre no respaldado falsea el registro y puede llevar a decisiones equivocadas."),
    sc=[
        ("En Geología: ¿qué se hace cuando una propiedad observada contradice el nombre anotado?", "Se reobserva la muestra y se consulta antes de dejar el nombre", "Una contradicción se resuelve con evidencia."),
        ("En la identificación de minerales: ¿cuántas propiedades conviene usar para distinguir candidatos parecidos?", "Al menos dos que los distingan", "Una sola propiedad puede coincidir entre minerales distintos."),
        ("¿Quién confirma el mineral y la ley de una muestra?", "El laboratorio", "La observación a simple vista es una estimación."),
    ],
    op=("Ficha de ejemplo con la tabla de esta clase. Muestra X: blanca, brillo vítreo, raya blanca, se rompe en planos lisos en tres direcciones y es rayada por la fluorita. Muestra Y: amarillo latón intenso, brillo metálico, raya negra verdosa, raya a la calcita y es rayada por la fluorita. Muestra Z: gris plomo, brillo metálico, raya gris plomo y se rompe en pequeños cubos. Criterio de ejemplo: pasan a análisis prioritario las muestras con sulfuros de cobre. Escribe (a) qué mineral es cada muestra, (b) qué propiedad distingue a Y de una pirita, (c) cuál pasa a análisis prioritario y por qué, (d) qué haces si X estuviera anotada como cuarzo.",
        "(a) X es calcita, Y es calcopirita y Z es galena. (b) La dureza: Y es rayada por la fluorita (menor que 4), mientras la pirita tiene dureza 6. (c) Y, porque es calcopirita, un sulfuro de cobre. (d) Es una contradicción: el cuarzo no tiene planos de exfoliación y es más duro que la fluorita, así que se reobserva, se consulta y no se deja el nombre. El laboratorio confirma.",
        ["identifica los tres minerales", "usa la dureza para distinguir", "aplica el criterio de análisis prioritario", "trata la contradicción sin dejar el nombre"],
        ["hoja con las cuatro respuestas"],
        ["usar solo el color", "invertir la dureza de Y y de la pirita", "dejar el nombre contradictorio"],
        "Pregunta: «¿qué propiedad separa a un mineral amarillo blando de uno amarillo duro?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una muestra con cuatro propiedades y usa la tabla de esta clase para decidir qué mineral podría ser.",
    extend="Explica con un ejemplo por qué una contradicción en una ficha debe resolverse antes de enviar la muestra.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (conteos de ejemplo, inventados). «Proyecto Cuenca Demo». Tres muestras revisadas con lupa, con fragmentos contados uno a uno. Muestra 1: 40 fragmentos, de los cuales 22 son de cuarzo, 10 de calcopirita y 8 de pirita. "
     "Muestra 2: 50 fragmentos, de los cuales 5 son de calcopirita. Muestra 3: 20 fragmentos, de los cuales 8 son de calcopirita. "
     "Criterio de clasificación visual de ejemplo (los reales los fija el proyecto): proporción de calcopirita de 30 por ciento o más, clase alta; de 15 por ciento o más y menos de 30, clase media; menos de 15 por ciento, clase baja. "
     "Datos de dureza de la tabla de referencia: calcita 3, fluorita 4; calcopirita entre 3 y 4, galena entre 2 y 3, cuarzo 7. Una cuarta hoja de conteo anota 12 de cuarzo, 9 de pirita y 22 de calcopirita, con un total de 40 fragmentos.")
build(
    O6, 4, F,
    use="Aprenderé a estimar la calidad de una muestra a simple vista con un criterio de clasificación visual: calcular la proporción de un mineral, clasificarla como alta, media o baja y reconocer los límites de esa estimación.",
    prior=["Sé identificar minerales por sus propiedades.", "Sé calcular porcentajes sencillos.", "Sé comparar un valor con un criterio."],
    explain=[
        "La proporción visual de un mineral es el porcentaje de fragmentos observados que corresponden a ese mineral; se calcula dividiendo los fragmentos de ese mineral entre el total contado y multiplicando por 100. Por ejemplo, 6 fragmentos de 30 son 20 por ciento. El criterio de clasificación visual del proyecto asigna una clase, alta, media o baja, según esa proporción; así se estima la calidad a simple vista.",
        "Esa clase es una estimación inicial: no mide la ley ni reemplaza al laboratorio, porque la proporción visual de fragmentos no es lo mismo que la concentración del elemento útil. Si el conteo no cuadra, por ejemplo si los fragmentos por mineral suman más que el total, hay un error de conteo: se recuenta y se corrige con firma, sin ajustar números para que calcen. La dureza también ayuda a identificar un fragmento: si raya a un mineral y es rayado por otro, su dureza está entre ambos.",
        f"La clasificación real la hace el geólogo con apoyo del asistente de geología; el laboratorio confirma. {EMER} {AVISO}",
    ],
    vocab=[("proporción visual", "porcentaje de fragmentos observados que corresponden a un mineral"), ("criterio de clasificación visual", "regla del proyecto que asigna una clase alta, media o baja según la proporción observada"), ("conteo", "recuento de fragmentos uno a uno"), ("clase alta, media o baja", "categoría de interés estimada a simple vista"), ("error de conteo", "falla en la cuenta de fragmentos, que se corrige con firma")],
    worked=[
        ("Proporción visual", "En una muestra de ejemplo se cuentan 25 fragmentos, de los cuales 5 son de galena. ¿Qué proporción visual tiene la galena?", ["Se divide: 5 ÷ 25 = 0,2.", "Multiplicado por 100 da 20 por ciento."], "20 por ciento"),
        ("Clasificar con un criterio", "Con un criterio de ejemplo (alta desde 40 por ciento, media desde 20 y menos de 40, baja bajo 20), ¿qué clase corresponde a una proporción de 20 por ciento?", ["20 no es menor que 20, así que no es baja.", "20 es mayor o igual que 20 y menor que 40: clase media."], "Clase media"),
    ],
    mistakes=[("Creer que la clase alta asegura que la muestra tiene mucha ley.", "La clase visual estima proporciones de fragmentos, no la concentración del elemento útil.", "La ley se confirma con análisis de laboratorio."),
              ("Ajustar los conteos para que sumen el total.", "Oculta un error de conteo.", "Se recuenta y se corrige con firma.")],
    T=[
        ("abc", "En Geología: ¿qué es la proporción visual de un mineral en una muestra?", "El porcentaje de fragmentos observados que corresponden a ese mineral", "La concentración del elemento útil medida en laboratorio", "El peso del mineral en gramos", "La proporción visual se cuenta sobre fragmentos; la concentración la mide el laboratorio."),
        ("abc", "En Geología: ¿qué es un criterio de clasificación visual?", "Una regla del proyecto que asigna una clase alta, media o baja según la proporción observada", "El orden alfabético de los nombres de los minerales", "La lista de minerales que se pueden tocar", "El criterio convierte una proporción en una clase."),
        ("abc", "En Geología: ¿por qué la clase visual debe confirmarse en laboratorio?", "Porque es una estimación a simple vista y la ley la mide el laboratorio", "Porque el laboratorio siempre repite la clase visual", "Porque a simple vista no se pueden contar fragmentos", "La clase visual estima proporciones; la ley es otra medida."),
        ("=", "{F} ¿Qué porcentaje de los fragmentos de la muestra 1 es de calcopirita?", "(10*100)//40", "Se multiplican los fragmentos de calcopirita por 100 y se dividen entre el total.", " por ciento"),
        ("=", "{F} ¿Qué porcentaje de los fragmentos de la muestra 1 es de pirita?", "(8*100)//40", "Se multiplican los fragmentos de pirita por 100 y se dividen entre el total.", " por ciento"),
        ("=", "{F} ¿Qué porcentaje de los fragmentos de la muestra 1 es de cuarzo?", "(22*100)//40", "Se multiplican los fragmentos de cuarzo por 100 y se dividen entre el total.", " por ciento"),
        ("abc", "{F} ¿Qué clase visual corresponde a la muestra 1, por su proporción de calcopirita?", "Media", "Alta", "Baja", "25 por ciento está entre 15 y menos de 30, que es la clase media."),
        ("=", "{F} ¿Qué porcentaje de los fragmentos de la muestra 2 es de calcopirita?", "(5*100)//50", "Se multiplican los fragmentos de calcopirita por 100 y se dividen entre el total.", " por ciento"),
        ("abc", "{F} ¿Qué clase visual corresponde a la muestra 3, con 8 fragmentos de calcopirita sobre 20?", "Alta, porque tiene 40 por ciento", "Media, porque tiene 25 por ciento", "Baja, porque tiene menos de 15 por ciento", "8 sobre 20 es 40 por ciento, que supera el 30 por ciento de la clase alta."),
        ("abc", "{F} Un fragmento raya a la calcita y es rayado por la fluorita. ¿Con qué mineral de la ficha es compatible su dureza?", "Calcopirita, que tiene dureza entre 3 y 4", "Galena, que tiene dureza entre 2 y 3", "Cuarzo, que tiene dureza 7", "Rayar a la calcita lo hace más duro que 3 y ser rayado por la fluorita, más blando que 4."),
        ("abc", "{F} La cuarta hoja de conteo anota 12 de cuarzo, 9 de pirita y 22 de calcopirita, con un total de 40 fragmentos. ¿Qué corresponde?", "Detectar un error de conteo, porque 12 + 9 + 22 suman 43, recontar y corregir con firma", "Aceptarla, porque el total está anotado", "Cambiar los 22 por 19 para que sumen 40", "La suma de los minerales supera el total; se recuenta en lugar de acomodar."),
        ("abc", "{F} Un compañero dice que la muestra 2, de clase baja, «seguro no tiene valor». ¿Qué respuesta es correcta?", "Es falso: la clase es una estimación visual; el valor lo confirma el laboratorio", "Es cierto, porque la clase baja significa cero ley", "Es cierto, porque la clase baja se descarta siempre del lote", "La clase visual no mide la ley, así que no permite afirmar que no tiene valor."),
        ("abc", "{F} Una compañera propone anotar «alta» para la muestra 1 para que pase antes al laboratorio. ¿Qué corresponde responder?", "Que no se altera la clase: la muestra 1 es media y se informa con los datos reales", "Que sí, porque así se gana tiempo", "Que sí, si se avisa al laboratorio por teléfono", "La clase se asigna con el criterio y los conteos reales; cambiarla falsea el registro."),
    ],
    ctx=("abc", "Un conocido te pide estimar «cuánto cobre tiene» un montón de rocas de su terreno mirándolas, para venderlas. ¿Qué respondes?", "Que a simple vista solo se puede estimar y que la ley la mide un laboratorio; lo consultarás con un adulto responsable", "Que sí, y le das una cifra segura", "Que sí, si las rocas son amarillas", "La ley no se puede conocer con certeza a simple vista; hace falta análisis de laboratorio."),
    sc=[
        ("En Geología: ¿cómo se calcula la proporción visual de un mineral?", "Se divide los fragmentos de ese mineral entre el total y se multiplica por 100", "La proporción visual es un porcentaje de fragmentos."),
        ("En la estimación visual de calidad: ¿qué mide la clase alta, media o baja?", "La proporción de fragmentos de un mineral, no la ley", "La ley la mide el laboratorio."),
        ("¿Qué se hace con un conteo que no cuadra?", "Se recuenta y se corrige con firma, sin ajustar números", "Un conteo erróneo se corrige con evidencia."),
    ],
    op=("Ficha de ejemplo del «Proyecto Pampa Demo». Criterio de ejemplo: calcopirita de 40 por ciento o más, clase alta; de 20 por ciento o más y menos de 40, clase media; menos de 20 por ciento, clase baja. Muestra P: 50 fragmentos, 30 de cuarzo y 20 de calcopirita. Muestra Q: 20 fragmentos, 2 de calcopirita. Escribe (a) el porcentaje de calcopirita de P y de Q, (b) la clase de cada una, (c) por qué la clase no asegura la ley, (d) qué haces si una hoja de conteo suma más fragmentos que el total anotado.",
        "(a) P: 20 × 100 ÷ 50 = 40 por ciento; Q: 2 × 100 ÷ 20 = 10 por ciento. (b) P es clase alta; Q es clase baja. (c) Porque la clase estima proporciones de fragmentos y la ley, la concentración del elemento útil, se mide en laboratorio. (d) Se recuenta y se corrige con firma, sin ajustar números. Todo lo hace el geólogo con apoyo del asistente.",
        ["calcula bien ambos porcentajes", "aplica bien el criterio", "explica que la ley la mide el laboratorio", "trata el error de conteo sin ajustarlo"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "afirmar que la clase alta asegura mucha ley", "ajustar los números para que sumen"],
        "Pregunta: «¿qué número se multiplica por 100 y entre cuál se divide?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una muestra con 20 fragmentos y calcula el porcentaje de un mineral de tu elección.",
    extend="Explica con un ejemplo por qué una clase visual alta no garantiza una ley alta.",
)
