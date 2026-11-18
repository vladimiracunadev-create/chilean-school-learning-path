"""Pesquería TP 3.º y 4.º medio: OAE-06 (implementos y utensilios: mantención como planificación y registros) y OAE-07 (planes y proyectos de manejo pesquero). Todo con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_pesq_common import AVISO, EMER, build

O6 = "TP-PESQ-3y4-OAE-06"
O7 = "TP-PESQ-3y4-OAE-07"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller de «Caleta Demo» guarda 36 implementos de ejemplo de la faena (artes, cabos, boyas y cajas). Regla de ejemplo: se revisan 6 implementos por semana. "
     "Peligros anotados: herramientas con filo y puntas, un equipo con partes en movimiento que se mantiene con el piso mojado, un enchufe cerca de la zona húmeda, productos de pintura y limpieza en envases sin rótulo y trabajo en el muelle sin baranda.")
build(
    O6, 1, F,
    use="Aprenderé qué son los implementos de una faena, la mantención preventiva y la correctiva, y cómo se previenen los peligros de un taller de caleta con la jerarquía de controles.",
    prior=["Sé qué son peligro, riesgo y jerarquía de controles.", "Sé qué es una faena y un registro.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Los implementos y utensilios de una faena son los equipos y objetos con que se trabaja: artes de pesca, cabos, boyas, cajas y herramientas. Armarlos, mantenerlos y repararlos exige conocimiento, herramientas y autorización; aquí solo se estudian los conceptos y los registros. La mantención preventiva es la que se planifica antes de que el implemento falle; la mantención correctiva es la que se hace después de una falla. La reparación es corregir un daño para volver a usar el implemento.",
        "Los requisitos legales y de seguridad los fija la norma vigente de la autoridad nacional y, en lo internacional, los tratados que la autoridad aplica; se cumplen con registros y revisiones. Los peligros de un taller se controlan con la jerarquía de controles: eliminar el peligro, sustituirlo, cambiar el lugar con protecciones fijas, ordenar el trabajo con reglas y, al final, usar EPP. Los equipos con partes en movimiento los mantiene solo personal autorizado, según la norma vigente.",
        f"Un implemento con una falla que afecta la seguridad se retira de uso hasta que personal autorizado lo repare o lo reemplace. {EMER} {AVISO}",
    ],
    vocab=[("implemento", "equipo u objeto con que se trabaja en una faena"), ("mantención preventiva", "mantención planificada antes de que el implemento falle"), ("mantención correctiva", "mantención hecha después de una falla"), ("reparación", "corrección de un daño para volver a usar un implemento"), ("retirar de uso", "dejar un implemento fuera de servicio hasta que se repare"), ("personal autorizado", "personas formadas a quienes la norma permite hacer la tarea")],
    worked=[
        ("Peligro y riesgo", "En un taller de ejemplo, una lima con filo queda sobre una mesa a la altura de las manos. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la lima con filo sobre la mesa.", "El riesgo es que una persona se corte al pasar la mano."], "Peligro: la lima con filo; riesgo: que alguien se corte"),
        ("Clasificar una mantención", "Una boya de ejemplo se revisa cada 3 meses, aunque no haya fallado. ¿Qué tipo de mantención es?", ["La revisión se planifica antes de la falla.", "Esa es una mantención preventiva."], "Mantención preventiva"),
    ],
    mistakes=[("Creer que se debe esperar a que un implemento falle para revisarlo.", "Esperar la falla puede causar un accidente y encarece la reparación.", "Se planifica la mantención preventiva con registros."),
              ("Creer que leer sobre la reparación de un implemento habilita para repararlo.", "Reparar un equipo con riesgo exige formación y autorización.", "Aprende aquí el concepto y deja la tarea a personal autorizado.")],
    T=[
        ("abc", "En Pesquería: ¿qué es la mantención preventiva de un implemento?", "La que se planifica antes de que falle", "La que se hace después de una falla", "La que se hace solo cuando hay tiempo libre", "La preventiva se adelanta a la falla; la correctiva la sigue."),
        ("abc", "En Pesquería: ¿qué es la mantención correctiva de un implemento?", "La que se hace después de una falla", "La que se planifica antes de la falla", "La que reemplaza los registros", "La correctiva responde a una falla ya ocurrida."),
        ("abc", "En Pesquería: ¿qué es un implemento de faena?", "Un equipo u objeto con que se trabaja, como un cabo, una boya o una caja", "El permiso para pescar", "El registro de lo capturado", "El implemento es un objeto de trabajo; el permiso y el registro son documentos."),
        ("=", "{F} ¿Cuántas semanas se necesitan para revisar los 36 implementos?", "36//6", "Se divide el total de implementos entre los que se revisan por semana.", " semanas"),
        ("abc", "{F} Una protección fija sobre las partes en movimiento del equipo, instalada por personal autorizado, es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque ordena una conducta", "De EPP, porque protege a quien se acerca", "La protección modifica el equipo y no depende de que alguien lo recuerde."),
        ("abc", "{F} Una lista de verificación previa a cada trabajo del taller es un control de tipo:", "Administrativo, porque ordena el trabajo", "De ingeniería, porque cambia el taller", "De EPP, porque protege el cuerpo", "Una lista ordena conductas; no cambia el taller ni es un equipo personal."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a las herramientas con filo y puntas?", "Que una persona sufra un corte o una herida", "La herramienta con filo misma, que es la fuente del daño", "Que la herramienta se oxide con el tiempo", "El riesgo es el daño posible a una persona; la herramienta es el peligro."),
        ("abc", "{F} Un compañero dice: «con buenos guantes puedo reparar el equipo con partes en movimiento». ¿Qué respuesta es correcta?", "Es falso: el EPP no elimina el atrapamiento y solo personal autorizado mantiene el equipo, según la norma vigente", "Es cierto, si el equipo se mueve despacio", "Es cierto, si otra persona lo mira", "Los guantes no quitan el peligro de atrapamiento."),
        ("abc", "En una visita de ejemplo al taller ves que una persona queda atrapada por un equipo. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a apagar el equipo tú mismo", "Tirar de la persona para sacarla rápido", "Intervenir sin formación puede causar más daño; se avisa a quienes pueden actuar."),
        ("abc", "En Pesquería: ¿por qué la mantención preventiva reduce riesgos?", "Porque detecta el desgaste antes de que el implemento falle durante la faena", "Porque elimina la necesidad de registros", "Porque hace que los implementos duren para siempre", "Detectar el desgaste a tiempo evita fallas y accidentes."),
        ("abc", "{F} Para el peligro del enchufe cerca de la zona húmeda, ¿qué medida de nivel más efectivo corresponde?", "Separar físicamente la zona húmeda del equipo eléctrico, con un cambio hecho por personal autorizado", "Pegar un cartel que diga «cuidado»", "Pedir que cada persona use botas", "El cambio físico es de ingeniería; el cartel es administrativo y las botas son EPP."),
        ("=", "{F} Si cada semana de revisión de 6 implementos demora 2 horas, ¿cuántas horas demora revisar los 36?", "36//6*2", "Se calculan las semanas y se multiplican por las horas de cada semana.", " horas"),
        ("abc", "{F} Una estudiante dice: «leí la ficha, así que puedo armar y reparar implementos de una faena». ¿Qué respuesta es correcta?", "Es falso: armar y reparar exige formación, autorización y norma vigente, y este cuaderno no habilita para trabajar", "Es cierto, si usa guantes", "Es cierto, si trabaja con otra persona", "Leer una ficha no habilita para trabajar."),
    ],
    ctx=("abc", "Un conocido te pide ayudarlo a «arreglar» un equipo de su taller con partes en movimiento, con el equipo funcionando. ¿Qué respondes?", "Que no, porque esa tarea exige personal autorizado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque solo es un ajuste pequeño", "Que sí, si usas guantes", "Un ajuste pequeño con el equipo en movimiento sigue siendo peligroso."),
    sc=[
        ("En Pesquería: ¿qué es la mantención preventiva?", "La que se planifica antes de que el implemento falle", "La preventiva evita fallas y accidentes."),
        ("En Pesquería: ¿qué se hace con un implemento con una falla que afecta la seguridad?", "Se retira de uso hasta que personal autorizado lo repare o lo reemplace", "Un implemento defectuoso no debe usarse."),
        ("En pesquería: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
    ],
    op=("El taller ficticio de «Caleta Demo» anota una tarea de ejemplo: mantener un equipo con partes en movimiento sobre piso mojado, con un enchufe a un metro y envases sin rótulo. Escribe (a) un peligro y su riesgo, (b) un control de ingeniería, (c) un control administrativo, (d) por qué el EPP no basta y quién hace la tarea.",
        "(a) Peligro: el equipo con partes en movimiento; riesgo: atrapamiento. También sirve el piso mojado con el enchufe (riesgo de descarga). (b) Una protección fija sobre el equipo o separar físicamente el enchufe de la zona húmeda, por personal autorizado. (c) Una lista de verificación y rótulos obligatorios en los envases. (d) El EPP es la última barrera y no quita el peligro; la tarea la hace personal autorizado, según la norma vigente.",
        ["distingue peligro y riesgo", "propone un control de ingeniería", "propone un control administrativo", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer solo el EPP", "no aclarar que la tarea la hace personal autorizado"],
        "Pregunta: «¿qué control cambia el equipo o el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres peligros de un taller inventado y, para cada uno, un control de un nivel distinto de la jerarquía.",
    extend="Explica con un ejemplo por qué la mantención preventiva suele costar menos que la correctiva.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). Hoja de vida de la red R-1: puesta en servicio en el mes 1; 600 horas de uso; vida útil estimada de ejemplo, 1.000 horas; reparaciones por desgaste en los meses 4 y 7. "
     "Inventario de ejemplo del taller: boyas, 45 en stock y stock mínimo 20; cabos, 12 en stock y stock mínimo 15; cajas, 80 en stock y stock mínimo 30. Una orden de trabajo de ejemplo anota qué se hace, a qué implemento, quién la autoriza y la fecha.")
build(
    O6, 2, F,
    use="Aprenderé los conceptos de hoja de vida, vida útil, stock mínimo y orden de trabajo, y los roles de quienes planifican, autorizan y ejecutan la mantención de los implementos.",
    prior=["Sé qué son la mantención preventiva y la correctiva.", "Sé calcular un porcentaje con números enteros.", "Sé que los registros no se alteran."],
    explain=[
        "La hoja de vida de un implemento es el documento donde se anota su historia: cuándo entró en servicio, cuántas horas se usó y qué reparaciones tuvo. La vida útil es el tiempo o las horas que se espera que el implemento sirva con seguridad; el porcentaje de vida útil usada es las horas de uso por 100, divididas por la vida útil. Por ejemplo, un cabo con 300 horas de una vida útil de 1.200 horas lleva usado el 25 %.",
        "El inventario es la lista de lo que hay en el taller. El stock mínimo es la cantidad más baja que debe haber de un insumo; si el stock está por debajo, hay que reponer. Un repuesto es una pieza que reemplaza a otra gastada. La orden de trabajo es el documento que autoriza una tarea de mantención e indica qué se hace, dónde, quién la autoriza y cuándo.",
        f"Los roles: el encargado de mantención planifica y lleva las hojas de vida; el bodeguero controla el stock; el patrón decide si un implemento sale a faena; el personal autorizado ejecuta las tareas. {EMER} {AVISO}",
    ],
    vocab=[("hoja de vida", "documento con la historia de un implemento: uso y reparaciones"), ("vida útil", "tiempo u horas que se espera que el implemento sirva con seguridad"), ("inventario", "lista de lo que hay en el taller"), ("stock mínimo", "cantidad más baja que debe haber de un insumo"), ("repuesto", "pieza que reemplaza a otra gastada"), ("orden de trabajo", "documento que autoriza una tarea de mantención"), ("encargado de mantención", "persona que planifica la mantención y lleva las hojas de vida"), ("bodeguero", "persona que controla el stock")],
    worked=[
        ("Vida útil usada", "Un cabo de ejemplo tiene 360 horas de uso y una vida útil de 1.200 horas. ¿Qué porcentaje usó?", ["Se multiplica 360 por 100: 36.000.", "36.000 dividido en 1.200 es 30."], "30 %"),
        ("Revisar un stock", "En un inventario de ejemplo hay 8 cajas y el stock mínimo es 10. ¿Qué corresponde?", ["8 es menor que 10.", "El stock está bajo el mínimo: hay que reponer."], "Reponer: está bajo el mínimo"),
    ],
    mistakes=[("Dejar de anotar una reparación pequeña en la hoja de vida.", "Sin ella no se ve si el desgaste se repite.", "Todas las reparaciones se anotan, con fecha y responsable."),
              ("Creer que un stock sobre el mínimo asegura que los implementos están en buen estado.", "El stock solo cuenta la cantidad, no el estado.", "El estado se revisa con la mantención y la hoja de vida.")],
    T=[
        ("abc", "En Pesquería: ¿qué es la hoja de vida de un implemento?", "El documento con su historia de uso y reparaciones", "El permiso para usar el implemento", "La lista de precios de los repuestos", "La hoja de vida registra la historia del implemento."),
        ("abc", "En Pesquería: ¿qué es el stock mínimo de un insumo?", "La cantidad más baja que debe haber en el taller", "La cantidad máxima que cabe en la bodega", "El precio más bajo del insumo", "Bajo el stock mínimo hay que reponer."),
        ("abc", "En Pesquería: ¿qué es una orden de trabajo de mantención?", "El documento que autoriza una tarea e indica qué se hace, dónde, quién la autoriza y cuándo", "La anotación de cuánto se capturó", "El plano de la caleta", "La orden de trabajo organiza y autoriza la tarea."),
        ("=", "{F} ¿Cuántas horas de vida útil le quedan a la red R-1?", "1000-600", "Se restan las horas de uso de la vida útil.", " horas"),
        ("=", "{F} ¿Qué porcentaje de su vida útil ha usado la red R-1?", "600*100//1000", "Se multiplican las horas de uso por 100 y se dividen entre la vida útil.", " %"),
        ("abc", "{F} ¿Qué insumo está bajo el stock mínimo?", "Los cabos, con 12 en stock y un mínimo de 15", "Las boyas, con 45 en stock", "Las cajas, con 80 en stock", "Solo los cabos tienen menos que su mínimo."),
        ("=", "{F} ¿Cuántos cabos faltan para llegar al stock mínimo?", "15-12", "Se resta el stock actual del mínimo.", " cabos"),
        ("abc", "{F} ¿Qué documento consultas para saber cuántas reparaciones ha tenido la red R-1?", "La hoja de vida", "El inventario del taller", "La orden de trabajo de otra red", "La hoja de vida guarda la historia de cada implemento."),
        ("abc", "{F} ¿Cuántas reparaciones por desgaste ha tenido la red R-1?", "2 reparaciones, en los meses 4 y 7", "1 reparación, en el mes 4", "3 reparaciones, en los meses 1, 4 y 7", "La ficha anota reparaciones en los meses 4 y 7; el mes 1 fue la puesta en servicio."),
        ("abc", "{F} Un compañero dice que, como las boyas superan el stock mínimo, no hay que revisarlas. ¿Qué respuesta es correcta?", "Es falso: el stock cuenta cantidad, no estado; la revisión de las boyas es otra tarea", "Es cierto: si hay suficientes, están en buen estado", "Es cierto si las boyas son nuevas", "El stock y el estado son datos distintos."),
        ("abc", "{F} Un compañero propone no anotar la reparación del mes 7 porque fue pequeña. ¿Qué pasa con la hoja de vida?", "Se pierde parte del historial y no se ve que el desgaste se repite", "No pasa nada, porque una reparación pequeña no importa", "Mejora, porque queda más corta", "El historial completo permite ver el desgaste repetido."),
        ("=", "{F} Si cada cabo cuesta 3.500 pesos de ejemplo, ¿cuánto cuesta reponer los que faltan para llegar al stock mínimo?", "(15-12)*3500", "Se multiplican los cabos faltantes por el costo de cada uno.", " pesos"),
        ("abc", "{F} Una estudiante dice: «leí la ficha, así que puedo autorizar y ejecutar reparaciones». ¿Qué respuesta es correcta?", "Es falso: la autoriza el responsable y la ejecuta personal autorizado; tu parte es leer y registrar con veracidad", "Es cierto, si anota la orden de trabajo", "Es cierto, si el stock está completo", "Leer una ficha no autoriza ni habilita para reparar."),
    ],
    ctx=("abc", "Alguien te pide cambiar las horas de uso de una red en la hoja de vida para que «parezca más nueva» antes de venderla. ¿Qué respondes?", "Que no, porque un registro no se altera, y que lo consultarás con un adulto responsable", "Que sí, solo unas pocas horas", "Que sí, si la red se ve bien", "Alterar las horas de uso oculta el desgaste y puede causar un accidente."),
    sc=[
        ("En Pesquería: ¿cómo se calcula el porcentaje de vida útil usada?", "Horas de uso por 100, divididas por la vida útil", "El porcentaje relaciona uso y vida útil."),
        ("En Pesquería: ¿qué rol controla el stock del taller?", "El bodeguero", "El bodeguero cuenta y repone los insumos."),
        ("En Pesquería: ¿qué se hace cuando un insumo está bajo el stock mínimo?", "Se repone", "Bajo el mínimo hay que reponer."),
    ],
    op=("Documentos de ejemplo: hoja de vida del cabo C-2, con 450 horas de uso, vida útil de 900 horas y una reparación en el mes 3; inventario: boyas, 10 en stock y mínimo 12; cajas, 30 en stock y mínimo 25. Una boya cuesta 4.000 pesos de ejemplo. Escribe (a) el porcentaje de vida útil usada del cabo y las horas que le quedan, (b) qué insumo está bajo el mínimo y cuánto cuesta reponerlo, (c) qué documento consultas para el historial, (d) por qué no se altera la hoja de vida.",
        "(a) 450 × 100 ÷ 900 = 50 %; le quedan 900 − 450 = 450 horas. (b) Las boyas: faltan 2 y reponerlas cuesta 2 × 4.000 = 8.000 pesos. (c) La hoja de vida. (d) Porque un registro alterado oculta el desgaste real y puede causar un accidente. Reponer o reparar lo hace personal autorizado.",
        ["calcula el porcentaje y las horas", "identifica el insumo y el costo", "nombra el documento", "explica por qué no se altera"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre las horas de uso", "olvidar calcular el costo", "alterar la hoja de vida"],
        "Pregunta: «¿entre qué número divides para obtener el porcentaje?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa la hoja de vida de un implemento con horas de uso y vida útil, y calcula el porcentaje usado.",
    extend="Explica con un ejemplo por qué la hoja de vida ayuda a decidir cuándo reemplazar un implemento.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (historial de ejemplo, inventado). Dos carros de transporte del taller, X e Y, durante 6 meses. Carro X, sin plan de mantención preventiva; fallas por mes, de los meses 1 a 6: 1, 0, 2, 3, 4 y 6. "
     "Carro Y, con mantención preventiva mensual; fallas por mes: 0, 1, 0, 1, 0 y 0. Costo de ejemplo de una reparación correctiva: 60.000 pesos por falla. Costo de ejemplo de una mantención preventiva: 20.000 pesos por mes.")
build(
    O6, 3, F,
    use="Aprenderé a analizar el historial de fallas de dos implementos, a leer una tendencia, a comparar costos de mantención preventiva y correctiva y a decidir qué se informa.",
    prior=["Sé qué son la mantención preventiva y correctiva.", "Sé qué es una tendencia.", "Sé sumar y multiplicar números enteros."],
    explain=[
        "Una falla es el momento en que un implemento deja de cumplir su función. El historial de fallas es la lista de fallas por período. Una falla recurrente es una falla que se repite; si las fallas aumentan mes a mes, la tendencia es creciente, y eso suele indicar desgaste. Una causa probable es una explicación posible que se debe comprobar con la hoja de vida y la revisión del equipo.",
        "El costo total de un implemento en un período es el costo de las mantenciones preventivas más el costo de las reparaciones correctivas. Para comparar dos implementos se calcula cada costo total con las mismas reglas. Por ejemplo, un implemento con 2 fallas a 50.000 pesos cada una y 4 mantenciones a 10.000 pesos tiene un costo total de 140.000 pesos.",
        f"Un implemento con una falla que afecta la seguridad se retira de uso, se informa al encargado de mantención y lo repara personal autorizado. Todos los costos son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("falla", "momento en que un implemento deja de cumplir su función"), ("historial de fallas", "lista de fallas por período"), ("falla recurrente", "falla que se repite"), ("tendencia creciente", "comportamiento en que los valores suben mes a mes"), ("costo total", "costo de mantenciones preventivas más reparaciones correctivas")],
    worked=[
        ("Calcular un costo total", "Un implemento de ejemplo tuvo 3 fallas a 40.000 pesos y 2 mantenciones a 15.000 pesos. ¿Cuál es el costo total?", ["Las fallas cuestan 3 por 40.000, es decir, 120.000.", "Las mantenciones cuestan 2 por 15.000, es decir, 30.000; el total es 150.000."], "150.000 pesos"),
        ("Leer una tendencia", "Las fallas por mes de un implemento de ejemplo son 1, 2, 3 y 5. ¿Qué tendencia muestran?", ["Cada mes hay más fallas que el anterior.", "La tendencia es creciente."], "Tendencia creciente"),
    ],
    mistakes=[("Concluir que las fallas son azar y que no hay nada que hacer.", "Un aumento mes a mes suele indicar desgaste que se puede prevenir.", "Se revisa el historial y se planifica la mantención preventiva."),
              ("Decidir que la mantención preventiva no sirve porque aun así hubo fallas.", "Hubo muchas menos fallas que sin ella.", "Se compara el costo total y el número de fallas.")],
    T=[
        ("abc", "En Pesquería: ¿qué es una falla recurrente de un implemento?", "Una falla que se repite", "Una falla que ocurre una sola vez", "Una falla que nunca se registra", "Una falla recurrente es la que se repite en el tiempo."),
        ("abc", "En Pesquería: ¿qué muestra una tendencia creciente de fallas?", "Que las fallas aumentan mes a mes, lo que suele indicar desgaste", "Que el implemento mejora con el uso", "Que las fallas son iguales todos los meses", "Si las fallas suben, el desgaste probablemente avanza."),
        ("abc", "En Pesquería: ¿qué es el costo total de mantención de un implemento?", "El costo de las preventivas más el de las reparaciones correctivas", "El precio al que se vendió el implemento", "El costo de comprar uno nuevo", "El costo total suma ambos tipos de gasto."),
        ("=", "{F} ¿Cuántas fallas tuvo el carro X en los 6 meses?", "1+0+2+3+4+6", "Se suman las fallas de cada mes.", " fallas"),
        ("=", "{F} ¿Cuánto costaron las reparaciones del carro X en los 6 meses?", "(1+0+2+3+4+6)*60000", "Se multiplican las fallas totales por el costo de cada reparación.", " pesos"),
        ("=", "{F} ¿Cuántas fallas tuvo el carro Y en los 6 meses?", "0+1+0+1+0+0", "Se suman las fallas de cada mes.", " fallas"),
        ("=", "{F} ¿Cuál es el costo total del carro Y en los 6 meses?", "2*60000+6*20000", "Se suman las reparaciones y las mantenciones preventivas de los seis meses.", " pesos"),
        ("abc", "{F} ¿Qué carro tuvo el menor costo total en los 6 meses?", "El carro Y, con 240.000 pesos frente a 960.000 pesos del carro X", "El carro X, porque no pagó mantenciones", "Ambos costaron lo mismo", "El carro X gastó 960.000 pesos en reparaciones; el Y, 240.000 en total."),
        ("=", "{F} ¿Cuántos pesos menos costó el carro Y que el carro X?", "(1+0+2+3+4+6)*60000-(2*60000+6*20000)", "Se resta el costo total de Y del costo total de X.", " pesos"),
        ("abc", "{F} ¿Qué indica que las fallas del carro X aumenten mes a mes desde el mes 2?", "Un desgaste creciente que justifica revisar el carro y planificar mantención preventiva", "Que las fallas se deben al azar y no hay nada que hacer", "Que el carro mejora con el uso", "Un aumento mes a mes es una señal de desgaste."),
        ("abc", "{F} Un compañero dice que la mantención preventiva no sirve porque el carro Y igual tuvo 2 fallas. ¿Qué respuesta es correcta?", "Es falso: Y tuvo muchas menos fallas que X y costó menos en total", "Es cierto, porque ninguna mantención evita fallas", "Es cierto, porque Y gastó en mantención", "Comparar con X muestra que la preventiva redujo fallas y costo."),
        ("=", "{F} Si el costo de cada mantención preventiva subiera a 40.000 pesos al mes, ¿cuál sería el costo total del carro Y en los 6 meses?", "2*60000+6*40000", "Se suman las reparaciones y las mantenciones con el nuevo costo.", " pesos"),
        ("abc", "{F} Un carro de transporte tiene una rueda floja. ¿Qué corresponde?", "Retirarlo de uso, informar al encargado de mantención y que lo repare personal autorizado", "Seguir usándolo con más cuidado", "Ajustarlo con lo que haya a mano", "Un implemento con falla de seguridad no se usa hasta repararse por personal autorizado."),
    ],
    ctx=("abc", "Alguien te propone no anotar las fallas del carro X «para no complicar el taller». ¿Qué respondes?", "Que no, porque sin historial no se puede planificar la mantención, y que lo consultarás con un adulto responsable", "Que sí, porque son pocas", "Que sí, si se arreglan solas", "Sin registro se pierde la información que previene accidentes."),
    sc=[
        ("En Pesquería: ¿cómo se calcula el costo total de un implemento?", "Reparaciones más mantenciones preventivas", "El costo total suma los dos tipos de gasto."),
        ("En Pesquería: ¿qué es una falla recurrente?", "Una falla que se repite", "Una falla recurrente indica un problema de fondo."),
        ("En Pesquería: ¿qué se hace con un implemento con falla de seguridad?", "Se retira de uso y lo repara personal autorizado", "Usarlo así expone a las personas."),
    ],
    op=("Historial de ejemplo de 4 meses: implemento P, sin preventiva, fallas 1, 2, 3 y 4; implemento Q, con preventiva mensual, fallas 0, 1, 0 y 0. Reparación de ejemplo: 50.000 pesos por falla; preventiva de ejemplo: 10.000 pesos por mes. Escribe (a) las fallas totales de cada uno, (b) el costo total de cada uno, (c) qué tendencia tiene P, (d) qué harías con un implemento con falla de seguridad.",
        "(a) P: 1 + 2 + 3 + 4 = 10 fallas; Q: 1 falla. (b) P: 10 × 50.000 = 500.000 pesos; Q: 1 × 50.000 + 4 × 10.000 = 90.000 pesos. (c) Creciente: cada mes tiene más fallas. (d) Retirarlo de uso, informar al encargado de mantención y que lo repare personal autorizado.",
        ["suma las fallas", "calcula los costos totales", "lee la tendencia", "aplica la regla de retirar de uso"],
        ["hoja con las cuatro respuestas"],
        ["olvidar sumar las mantenciones de Q", "decir que sigue en uso con más cuidado", "no identificar la tendencia"],
        "Pregunta: «¿qué dos gastos se suman en el costo total?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa el historial de fallas de dos implementos y calcula cuál cuesta menos en seis meses.",
    extend="Explica por qué una tendencia creciente de fallas debe informarse aunque cada falla sea pequeña.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (plan de mantención de ejemplo, inventado). Cinco cabos del taller, con las horas de uso desde su última revisión: cabo A, 150; cabo B, 420; cabo C, 610; cabo D, 380; cabo E, 90. "
     "Regla de ejemplo: un cabo se revisa cuando llega a 200 horas de uso desde su última revisión. Costo de ejemplo de una revisión: 8.000 pesos. Cada cabo se usa 800 horas al año (dato de ejemplo).")
build(
    O6, 4, F,
    use="Aprenderé a aplicar un plan de mantención por horas de uso: calcular horas hasta la revisión, atrasos, revisiones pendientes y costos anuales con datos de ejemplo.",
    prior=["Sé qué son la mantención preventiva y la hoja de vida.", "Sé multiplicar, dividir, sumar y restar números enteros.", "Sé comparar un dato con una regla."],
    explain=[
        "Un plan de mantención por horas fija un intervalo: cada cuántas horas de uso se revisa un implemento. Una revisión está pendiente cuando las horas de uso desde la última revisión llegan al intervalo o lo superan. Las horas de atraso son las horas de uso menos el intervalo. Las horas que faltan para la revisión son el intervalo menos las horas de uso.",
        "Para estimar el costo anual de un plan se calcula cuántas revisiones por año necesita cada implemento, dividiendo las horas de uso anual entre el intervalo, y se multiplica por el costo de cada revisión y por el número de implementos. Por ejemplo, con un intervalo de 100 horas y 500 horas al año, hay 5 revisiones por implemento al año.",
        f"Un implemento con la revisión pendiente y un gran atraso se retira de uso hasta que personal autorizado lo revise. Cambiar un intervalo exige evidencia y autorización; no se hace por ahorro. Los números son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("intervalo de revisión", "horas de uso entre una revisión y la siguiente"), ("revisión pendiente", "revisión cuyas horas ya llegaron al intervalo o lo superaron"), ("horas de atraso", "horas de uso menos el intervalo"), ("horas hasta la revisión", "intervalo menos horas de uso"), ("plan de mantención", "documento que fija cuándo y cómo se planifica cada mantención")],
    worked=[
        ("Horas hasta la revisión", "Un cabo de ejemplo tiene 120 horas de uso y el intervalo es 300. ¿Cuántas horas le faltan?", ["Se resta el uso del intervalo.", "300 menos 120 es 180."], "180 horas"),
        ("Revisiones por año", "Un implemento de ejemplo se usa 900 horas al año y el intervalo es 300. ¿Cuántas revisiones necesita por año?", ["Se dividen las horas anuales entre el intervalo.", "900 dividido en 300 es 3."], "3 revisiones por año"),
    ],
    mistakes=[("Seguir usando un cabo con un gran atraso porque aún no se ha cortado.", "La regla se basa en horas de uso, no en la falla.", "Con la revisión pendiente, se retira de uso hasta revisarlo."),
              ("Ampliar el intervalo para ahorrar sin evidencia.", "Menos revisiones pueden dejar pasar un desgaste peligroso.", "Los cambios se hacen con evidencia y autorización.")],
    T=[
        ("abc", "En Pesquería: ¿qué es el intervalo de revisión de un implemento?", "Las horas de uso entre una revisión y la siguiente", "El precio de cada revisión", "El número de implementos del taller", "El intervalo mide el uso entre revisiones."),
        ("abc", "En Pesquería: ¿qué son las horas de atraso de un implemento?", "Las horas de uso que pasaron del intervalo", "Las horas que faltan para la revisión", "Las horas que demora una revisión", "El atraso es lo que se pasó del intervalo."),
        ("abc", "En Pesquería: ¿cuándo está pendiente la revisión de un cabo?", "Cuando sus horas de uso llegan al intervalo o lo superan", "Cuando el cabo se ve sucio", "Cuando se compra uno nuevo", "La regla se basa en horas de uso."),
        ("=", "{F} ¿Cuántas horas le faltan al cabo A para su revisión?", "200-150", "Se resta el uso del intervalo.", " horas"),
        ("=", "{F} ¿Cuántas horas de atraso tiene el cabo B?", "420-200", "Se resta el intervalo de las horas de uso.", " horas"),
        ("abc", "{F} ¿Qué cabo tiene el mayor atraso?", "El cabo C, con 410 horas de atraso", "El cabo B, con 220 horas de atraso", "El cabo D, con 180 horas de atraso", "C acumula 610 menos 200, que es 410 horas de atraso."),
        ("abc", "{F} ¿Cuántos cabos tienen la revisión pendiente?", "3 cabos: B, C y D", "2 cabos: B y C", "5 cabos: todos", "Solo B, C y D llegaron a las 200 horas o las superaron."),
        ("=", "{F} ¿Cuánto cuestan las revisiones pendientes, a costo de ejemplo?", "3*8000", "Se multiplican las revisiones pendientes por el costo de cada una.", " pesos"),
        ("=", "{F} ¿Cuántas horas de atraso suman los cabos B, C y D?", "(420-200)+(610-200)+(380-200)", "Se suman las horas de atraso de los tres cabos.", " horas"),
        ("abc", "{F} Un compañero dice que el cabo C se puede usar igual porque no se ha cortado. ¿Qué respuesta es correcta?", "Es falso: la regla exige revisión por horas de uso, no por falla, y C queda fuera de uso hasta revisarse", "Es cierto: sin falla no hay problema", "Es cierto si se usa con más cuidado", "La mantención preventiva se adelanta a la falla."),
        ("abc", "{F} Una compañera propone anotar que el cabo C ya fue revisado para «ponerse al día» con el plan. ¿Qué respondes?", "Que no: anotar una revisión que no se hizo falsea el registro; se informa el atraso", "Que sí, si lo revisa más tarde", "Que sí, si el cabo se ve bien", "Un registro falso oculta el atraso y expone a las personas."),
        ("=", "{F} ¿Cuánto costaría al año la mantención de los 5 cabos con este plan?", "5*(800//200)*8000", "Se multiplican los cabos por las revisiones anuales y por el costo de cada una.", " pesos"),
        ("abc", "{F} Alguien propone ampliar el intervalo a 400 horas para ahorrar. ¿Qué respondes?", "Que no sin evidencia ni autorización: menos revisiones pueden dejar pasar un desgaste peligroso", "Que sí, porque cuesta menos", "Que sí, si el cabo es nuevo", "Un cambio de intervalo se justifica con evidencia, no con ahorro."),
    ],
    ctx=("abc", "Un conocido te dice que sus cabos «nunca se revisan y nunca pasa nada». ¿Qué respondes?", "Que la mantención preventiva se hace antes de la falla, y que lo consultarás con un adulto responsable o la autoridad marítima", "Que si no pasa nada, no hay problema", "Que se revisan solo al cortarse", "Que no haya fallas no prueba que el cabo esté en buen estado."),
    sc=[
        ("En Pesquería: ¿cómo se calculan las horas que faltan para una revisión?", "Intervalo menos horas de uso", "Lo que falta es lo que resta hasta el intervalo."),
        ("En Pesquería: ¿cómo se calculan las revisiones anuales de un implemento?", "Horas de uso al año divididas por el intervalo", "El uso anual dividido por el intervalo da las revisiones."),
        ("En Pesquería: ¿qué se hace con un cabo con la revisión pendiente?", "Se retira de uso hasta que personal autorizado lo revise", "La revisión pendiente es una alerta de seguridad."),
    ],
    op=("Plan de ejemplo: intervalo de 250 horas; cuatro cabos con 100, 260, 480 y 249 horas de uso; revisión de ejemplo a 6.000 pesos; cada cabo se usa 750 horas al año. Escribe (a) qué cabos tienen la revisión pendiente, (b) las horas de atraso del cabo con mayor atraso, (c) el costo de las revisiones pendientes, (d) el costo anual de los cuatro cabos.",
        "(a) Tienen la revisión pendiente los cabos de 260 y 480 horas; el de 249 aún no, porque le falta 1 hora. (b) El de 480 horas: 480 − 250 = 230 horas de atraso. (c) 2 × 6.000 = 12.000 pesos. (d) 750 ÷ 250 = 3 revisiones por cabo; 4 × 3 × 6.000 = 72.000 pesos. Las revisiones las hace personal autorizado.",
        ["identifica las revisiones pendientes", "calcula el mayor atraso", "calcula el costo pendiente", "calcula el costo anual"],
        ["hoja con las cuatro respuestas"],
        ["contar el cabo de 249 horas", "olvidar multiplicar por los cabos", "restar mal el intervalo"],
        "Pregunta: «¿qué cabos llegaron a 250 horas o más?». Si no responde, pídele que compare cada uno con el intervalo."),
    reinforce="Inventa un plan con intervalo y cinco implementos con horas de uso, y marca cuáles están pendientes.",
    extend="Explica por qué la regla por horas de uso protege más que esperar a que el implemento falle.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (alternativas y lista de ejemplo, inventadas). Implemento M: reemplazo 100.000 pesos, reparación 40.000 pesos, la falla no afecta la seguridad. Implemento N: reemplazo 75.000 pesos, reparación 45.000 pesos, la falla no afecta la seguridad. "
     "Implemento P: reemplazo 100.000 pesos, reparación 20.000 pesos, la falla afecta un elemento de seguridad. Regla de ejemplo: se repara si el costo de la reparación es a lo más el 50 % del costo de reemplazo y la falla no afecta la seguridad; en otro caso se reemplaza. "
     "Lista de control de una mantención de ejemplo: línea 1, «reparación hecha», sin fecha; línea 2, «repuesto usado», sin código; línea 3, «autorizada por», sin firma.")
build(
    O6, 5, F,
    use="Aprenderé a comparar reparar con reemplazar según una regla y costos de ejemplo, y a verificar la calidad de una lista de control de mantención.",
    prior=["Sé calcular un porcentaje con números enteros.", "Sé qué son la hoja de vida y la orden de trabajo.", "Sé que los registros no se alteran."],
    explain=[
        "Reparar o reemplazar un implemento se decide con una regla y no solo con el precio. Una regla de ejemplo compara el costo de la reparación con el de reemplazo: si la reparación cuesta a lo más la mitad y la falla no afecta la seguridad, se repara; si no, se reemplaza. Dar de baja es retirar definitivamente un implemento del servicio y anotarlo en su hoja de vida.",
        "La verificación de calidad de una mantención es la revisión que comprueba que la tarea se hizo y se registró bien: fecha, repuesto usado con su código, resultado de la prueba y firma de quien la autorizó. Un registro sin fecha, sin código o sin firma pierde la trazabilidad y debe completarse con quien corresponde, no con datos inventados.",
        f"Cuando la falla afecta un elemento de seguridad, el implemento se retira de uso aunque la reparación sea barata, hasta que personal autorizado decida. Los costos son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("reemplazo", "cambio de un implemento por otro nuevo"), ("dar de baja", "retirar definitivamente un implemento del servicio"), ("verificación de calidad de una mantención", "revisión que comprueba que la tarea se hizo y se registró bien"), ("código de repuesto", "identificación del repuesto usado"), ("regla de reparación", "condición que decide si se repara o se reemplaza")],
    worked=[
        ("Aplicar la regla", "Un implemento de ejemplo cuesta 80.000 pesos reemplazarlo y 20.000 repararlo, y la falla no afecta la seguridad. La regla pide a lo más 50 %. ¿Qué corresponde?", ["20.000 por 100 dividido entre 80.000 es 25 %.", "25 % es menor que 50 %: se repara."], "Repararlo"),
        ("Falla de seguridad", "Un implemento de ejemplo tiene una reparación barata, pero la falla afecta un elemento de seguridad. ¿Qué corresponde?", ["La regla exige que la falla no afecte la seguridad.", "Se retira de uso y decide personal autorizado."], "Retirarlo de uso y que decida personal autorizado"),
    ],
    mistakes=[("Elegir siempre lo más barato entre reparar y reemplazar.", "Una reparación barata de un elemento de seguridad puede dejar un riesgo.", "Se aplica la regla de reparación y se prioriza la seguridad."),
              ("Completar una línea de la lista con una fecha o un código que no se conocen.", "Un dato inventado falsea la trazabilidad.", "Se pide a quien hizo la tarea que complete la línea con el dato real.")],
    T=[
        ("abc", "En Pesquería: al decidir entre reparar y reemplazar, ¿qué criterio va primero?", "Que la falla no afecte la seguridad de las personas", "El menor costo de la reparación", "El color del implemento", "Si la falla afecta la seguridad, se retira de uso aunque la reparación sea barata."),
        ("abc", "En Pesquería: ¿qué significa dar de baja un implemento?", "Retirarlo definitivamente del servicio y anotarlo", "Lavarlo para usarlo de nuevo", "Cambiarle el nombre en el inventario", "Dar de baja es retirar definitivamente."),
        ("abc", "En Pesquería: ¿qué comprueba la verificación de calidad de una mantención?", "Que la tarea se hizo y se registró con fecha, repuesto y firma", "Que la herramienta quedó limpia", "Que el implemento es el más caro del taller", "La verificación se centra en la tarea y su registro."),
        ("=", "{F} ¿Qué porcentaje del costo de reemplazo es la reparación del implemento M?", "40000*100//100000", "Se multiplica el costo de reparación por 100 y se divide entre el de reemplazo.", " %"),
        ("=", "{F} ¿Qué porcentaje del costo de reemplazo es la reparación del implemento N?", "45000*100//75000", "Se multiplica el costo de reparación por 100 y se divide entre el de reemplazo.", " %"),
        ("abc", "{F} ¿Qué corresponde con el implemento M según la regla?", "Repararlo, porque su reparación es el 40 % del reemplazo y no afecta la seguridad", "Reemplazarlo, porque todo se reemplaza", "Repararlo, porque nunca se reemplaza nada", "40 % es menor que 50 % y no hay riesgo de seguridad."),
        ("=", "{F} ¿Cuántos pesos se ahorran al reparar el implemento M en lugar de reemplazarlo?", "100000-40000", "Se resta el costo de reparación del de reemplazo.", " pesos"),
        ("abc", "{F} ¿Qué corresponde con el implemento N según la regla?", "Reemplazarlo, porque su reparación es el 60 % del reemplazo y supera el 50 %", "Repararlo, porque la reparación es más barata", "Dejarlo sin hacer nada", "La regla manda reemplazar cuando la reparación supera el 50 %, aunque cueste menos."),
        ("=", "{F} ¿Cuántos pesos más cuesta reemplazar el implemento N que repararlo?", "75000-45000", "Se resta el costo de reparación del de reemplazo.", " pesos"),
        ("abc", "{F} El implemento P tiene una reparación barata, pero la falla afecta un elemento de seguridad. ¿Qué corresponde?", "Retirarlo de uso y reemplazarlo o repararlo solo si lo decide personal autorizado", "Repararlo porque es barato", "Seguir usándolo hasta que falle del todo", "La seguridad prima sobre el costo de la reparación."),
        ("abc", "{F} ¿Qué criterio de calidad falla en las tres líneas de la lista de control?", "La trazabilidad, porque falta fecha, código y firma", "La limpieza, porque está sucia", "La puntualidad, porque llegó tarde", "Sin fecha, código y firma no se puede seguir la historia de la tarea."),
        ("=", "{F} El taller tiene 4 implementos como M y 3 como N. Si repara los M y reemplaza los N, ¿cuánto gasta?", "4*40000+3*75000", "Se suman las reparaciones de los M y los reemplazos de los N.", " pesos"),
        ("abc", "{F} Alguien propone reparar el implemento N igual, por ser más barato hoy, y anotarlo como «reemplazado». ¿Qué respondes?", "Que no: falsear el registro es grave, y se aplica la regla de reparación", "Que sí, porque es más barato", "Que sí, si nadie lo revisa", "Un registro falso oculta una decisión que no cumple la regla."),
    ],
    ctx=("abc", "Alguien te pide firmar «autorizada por» en una orden de mantención en lugar de la persona responsable, para ahorrar tiempo. ¿Qué respondes?", "Que no, porque nadie firma por otra persona, y que lo consultarás con un adulto responsable", "Que sí, si es una firma sencilla", "Que sí, si después se avisa", "La firma deja constancia de responsabilidad y no se suple."),
    sc=[
        ("En Pesquería: ¿qué se hace con un implemento cuya falla afecta la seguridad?", "Se retira de uso y decide personal autorizado", "La seguridad prima sobre el costo."),
        ("En Pesquería: ¿qué datos lleva una buena lista de control de mantención?", "Fecha, repuesto con código y firma de quien autoriza", "Esos datos permiten seguir la historia de la tarea."),
        ("En Pesquería: ¿cuándo se repara un implemento según la regla de ejemplo?", "Si la reparación cuesta a lo más el 50 % del reemplazo y la falla no afecta la seguridad", "Es la regla de ejemplo de la ficha."),
    ],
    op=("Alternativas de ejemplo: implemento R, reemplazo 125.000 pesos, reparación 50.000, falla sin riesgo de seguridad; implemento S, reemplazo 90.000, reparación 20.000, falla en un elemento de seguridad. Regla de ejemplo: reparar si la reparación cuesta a lo más 50 % del reemplazo y la falla no afecta la seguridad. Escribe (a) el porcentaje de la reparación de R, (b) qué corresponde con R, (c) qué corresponde con S y por qué, (d) qué haces con una línea sin firma en la lista de control.",
        "(a) 50.000 × 100 ÷ 125.000 = 40 %. (b) Repararlo, porque es menos del 50 % y la falla no afecta la seguridad. (c) S se retira de uso y decide personal autorizado, porque la falla afecta la seguridad aunque la reparación sea barata. (d) Pedir que quien debe autorizar firme; nadie firma por otra persona ni se inventa un dato.",
        ["calcula el porcentaje", "aplica la regla a R", "prioriza la seguridad en S", "no suple la firma"],
        ["hoja con las cuatro respuestas"],
        ["reparar S por ser barata", "dividir entre el costo de reparación", "firmar por otra persona"],
        "Pregunta: «¿qué condición debe cumplirse además del costo?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres implementos con costos de reparación y reemplazo, y decide con la regla de ejemplo.",
    extend="Explica por qué una reparación barata de un elemento de seguridad no siempre conviene.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La organización ficticia «Organización Demo» agrupa a 24 socios con 12 embarcaciones en «Caleta Demo», un lugar de desembarque y trabajo de pescadores artesanales. Quiere redactar un plan de manejo y un proyecto para mejorar el muelle. "
     "Peligros anotados en el muelle: sin barandas, desembarque a oscuras, rampa resbaladiza y una grúa de descarga sin zona demarcada. El proyecto de ejemplo de barandas e iluminación cuesta 2.000.000 de pesos; el programa de fomento de ejemplo aporta el 70 % y la organización pone el resto.")
build(
    O7, 1, F,
    use="Aprenderé qué son un plan de manejo pesquero, un proyecto, una caleta y el fomento pesquero, por qué se exige veracidad al redactarlos y cómo se previenen los peligros de la infraestructura de una caleta.",
    prior=["Sé qué son peligro, riesgo y jerarquía de controles.", "Sé calcular un porcentaje con números enteros.", "Sé que los registros no se alteran."],
    explain=[
        "Una caleta pesquera es un lugar de desembarque y de trabajo de pescadores artesanales. Un plan de manejo pesquero es el documento que ordena cómo se usa y se cuida un recurso o una zona, con objetivos, medidas y control. Un proyecto es un conjunto de actividades con un objetivo, un plazo y un presupuesto. El emprendimiento es una iniciativa para generar ingresos, y el ordenamiento es la organización del uso de la zona y del recurso.",
        "El fomento pesquero son los programas nacionales y regionales que apoyan a las organizaciones con orientaciones y recursos, según la norma vigente. El sistema de control de captura es el conjunto de registros y revisiones que verifica que lo capturado respete la cuota y las vedas. Al redactar un plan o un proyecto se exige veracidad: no se inventan datos ni se inflan costos para obtener fondos.",
        f"Los peligros de la infraestructura de una caleta, como un muelle sin baranda, se controlan con la jerarquía de controles. Redactar un proyecto no habilita para construirlo: las obras las hace personal autorizado, con los permisos que fije la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("caleta pesquera", "lugar de desembarque y de trabajo de pescadores artesanales"), ("plan de manejo pesquero", "documento que ordena cómo se usa y se cuida un recurso o una zona"), ("proyecto", "conjunto de actividades con objetivo, plazo y presupuesto"), ("emprendimiento", "iniciativa para generar ingresos"), ("ordenamiento", "organización del uso de la zona y del recurso"), ("fomento pesquero", "programas nacionales y regionales de apoyo a las organizaciones"), ("sistema de control de captura", "registros y revisiones que verifican que lo capturado respeta la cuota y las vedas")],
    worked=[
        ("Peligro y riesgo", "En el muelle de una caleta de ejemplo, un tramo de tablones está suelto. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el tramo de tablones suelto.", "El riesgo es que una persona tropiece o caiga al agua y se lastime."], "Peligro: el tablón suelto; riesgo: tropezar o caer y lastimarse"),
        ("Calcular un aporte", "Un proyecto de ejemplo cuesta 1.000.000 de pesos y el programa aporta el 40 %. ¿Cuánto aporta el programa?", ["Se multiplica 1.000.000 por 40: 40.000.000.", "40.000.000 dividido en 100 es 400.000."], "400.000 pesos"),
    ],
    mistakes=[("Inflar el costo de un proyecto para recibir más fondos.", "Es falsear un dato y puede ser un incumplimiento de las bases del programa.", "Se declara el costo real y se consulta con la directiva y un adulto responsable."),
              ("Creer que redactar un proyecto de obra habilita para ejecutar la obra.", "Las obras exigen personal autorizado y permisos.", "Se redacta el proyecto y se encarga la ejecución a quien corresponde.")],
    T=[
        ("abc", "En Pesquería: ¿qué es un plan de manejo pesquero?", "El documento que ordena cómo se usa y se cuida un recurso o una zona, con objetivos, medidas y control", "El registro de lo capturado en una faena", "El contrato de venta con un comprador", "El plan de manejo ordena el uso del recurso; el registro y el contrato son otros documentos."),
        ("abc", "En Pesquería: ¿qué es un proyecto?", "Un conjunto de actividades con un objetivo, un plazo y un presupuesto", "Un permiso para pescar una especie", "Una lista de los socios de una organización", "Un proyecto se define por su objetivo, su plazo y su presupuesto."),
        ("abc", "En Pesquería: ¿qué es una caleta pesquera?", "Un lugar de desembarque y de trabajo de pescadores artesanales", "Un tipo de red de pesca", "Una zona donde está prohibido capturar", "La caleta es un lugar; la red y la veda son otros conceptos."),
        ("=", "{F} ¿Cuántos pesos aporta el programa de fomento al proyecto?", "2000000*70//100", "Se multiplica el costo por 70 y se divide entre 100.", " pesos"),
        ("abc", "{F} Barandas fijas e iluminación fija en el muelle, instaladas por personal autorizado, son controles de tipo:", "De ingeniería, porque cambian físicamente el lugar", "Administrativo, porque ordenan una conducta", "De EPP, porque protegen a quien camina", "Las barandas y la iluminación modifican el muelle y no dependen de que alguien las recuerde."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a un muelle sin barandas?", "Que una persona caiga al agua desde el borde y se lastime", "El muelle sin barandas mismo, que es la fuente del daño", "Que la organización tenga menos socios", "El riesgo es el daño posible a una persona; el muelle sin baranda es el peligro."),
        ("=", "{F} ¿Cuántos pesos debe aportar la organización?", "2000000-2000000*70//100", "Se restan al costo total los pesos que aporta el programa.", " pesos"),
        ("abc", "{F} Un dirigente propone declarar un costo de 2.500.000 de pesos para recibir más fondos, aunque el real es 2.000.000. ¿Qué respondes?", "Que no: se declara el costo real y se consulta con un adulto responsable", "Que sí, si después se devuelve el sobrante", "Que sí, porque otras organizaciones lo hacen", "Inflar un costo es falsear un dato."),
        ("abc", "En una visita de ejemplo a una caleta ves humo en una caseta de herramientas. ¿Qué corresponde según las reglas generales?", "Alejarte, avisar a un adulto responsable y a emergencias, sin intentar apagar el fuego", "Entrar a ver qué se quema", "Buscar agua y apagarlo tú", "Un fuego exige personal formado; tu acción es alejarte y avisar."),
        ("abc", "En Pesquería: ¿por qué un plan de manejo incluye un sistema de control de captura?", "Porque permite verificar que lo capturado respeta la cuota y las vedas, y cuidar el recurso", "Porque así se evita registrar las capturas", "Porque reemplaza la cuota", "El control verifica el cumplimiento de las medidas del plan."),
        ("abc", "{F} Para el desembarque a oscuras, ¿qué medida de nivel más efectivo se podría sumar a una regla escrita?", "Iluminación fija del muelle instalada por personal autorizado", "Otro cartel con la misma advertencia", "Pedir a cada socio que lleve su linterna", "La iluminación fija es de ingeniería; el cartel es administrativo y la linterna es un elemento personal."),
        ("=", "{F} Si los 24 socios aportan por partes iguales lo que debe poner la organización, ¿cuánto aporta cada socio?", "(2000000-2000000*70//100)//24", "Se divide el aporte de la organización entre el número de socios.", " pesos"),
        ("abc", "{F} Una estudiante dice: «si redacto el proyecto, ya puedo construir las barandas». ¿Qué respuesta es correcta?", "Es falso: las obras las hace personal autorizado con los permisos que fije la norma vigente", "Es cierto, si compra los materiales", "Es cierto, si lo hace con otras personas", "Redactar un proyecto no habilita para ejecutar obras."),
    ],
    ctx=("abc", "Un comprador te ofrece dinero por escribir en un proyecto de ejemplo que sus bodegas son parte de la caleta, aunque no lo son. ¿Qué respondes?", "Que no, porque los datos de un proyecto deben ser veraces, y que lo consultarás con un adulto responsable", "Que sí, si el dinero es suficiente", "Que sí, si es un detalle pequeño", "Un dato falso en un proyecto es una falta y perjudica a la organización."),
    sc=[
        ("En Pesquería: ¿qué es el fomento pesquero?", "Programas nacionales y regionales que apoyan a las organizaciones", "El fomento ofrece orientaciones y recursos según la norma vigente."),
        ("En Pesquería: ¿qué es el ordenamiento de una caleta?", "La organización del uso de la zona y del recurso", "El ordenamiento ordena quién usa qué y cómo."),
        ("En Pesquería: ¿qué se exige al redactar un proyecto para pedir fondos?", "Veracidad: no inventar datos ni inflar costos", "La veracidad protege a la organización y al programa."),
    ],
    op=("Caso de ejemplo: una organización ficticia de 20 socios quiere un proyecto para iluminar su muelle y poner barandas, con un costo de 1.500.000 pesos de ejemplo. El programa de fomento de ejemplo aporta el 60 %. El muelle no tiene barandas y el desembarque es a oscuras. Escribe (a) cuánto aporta el programa y cuánto la organización, (b) un peligro y su riesgo, (c) un control de ingeniería, (d) qué datos no podrías inventar en el proyecto y por qué.",
        "(a) El programa aporta 1.500.000 × 60 ÷ 100 = 900.000 pesos; la organización, 600.000. (b) Peligro: muelle sin barandas; riesgo: que alguien caiga al agua y se lastime. (c) Barandas fijas e iluminación fija, instaladas por personal autorizado. (d) No se pueden inventar costos, cantidad de socios ni datos de captura, porque un dato falso es una falta y perjudica a la organización. Las obras las hace personal autorizado.",
        ["calcula los aportes", "distingue peligro y riesgo", "propone un control de ingeniería", "explica la exigencia de veracidad"],
        ["hoja con las cuatro respuestas"],
        ["calcular el aporte con el porcentaje equivocado", "llamar riesgo a la fuente del daño", "aceptar inflar un costo"],
        "Pregunta: «¿qué porcentaje del costo pone la organización?». Si no responde, pídele que reste de 100 el porcentaje del programa."),
    reinforce="Escribe en tres líneas qué es un plan de manejo, un proyecto y un sistema de control de captura, con un ejemplo inventado de cada uno.",
    extend="Explica con un ejemplo por qué la veracidad de un proyecto protege a toda la organización.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (plan de ejemplo, inventado). «Organización Demo», plan de manejo de la especie A. Objetivo general: mantener la captura anual bajo la cuota de ejemplo. Objetivo específico 1: registrar todas las capturas en planilla. Objetivo específico 2: medir tallas todos los meses. "
     "Indicador 1: porcentaje de desembarques con planilla completa, meta 100 %. Indicador 2: número de muestras de tallas por mes, meta 4. Medio de verificación: las planillas archivadas. "
     "Presupuesto de ejemplo: planillas, 50.000 pesos; capacitación, 300.000 pesos; balanza, 450.000 pesos. Resultados del primer mes: 240 desembarques, 216 con planilla completa; 3 muestras de tallas. "
     "Roles: la directiva presenta el plan; el asesor técnico apoya; los socios ejecutan y aportan datos veraces; la autoridad pesquera evalúa y fiscaliza.")
build(
    O7, 2, F,
    use="Aprenderé las partes de un plan de manejo: objetivos, metas, indicadores, medios de verificación, actividades, responsables, cronograma y presupuesto, y los roles que intervienen.",
    prior=["Sé qué es un plan de manejo y un proyecto.", "Sé calcular un porcentaje con números enteros.", "Sé qué son una planilla y un registro."],
    explain=[
        "Un plan se ordena en partes. El objetivo general es lo que se quiere lograr en grande; los objetivos específicos son resultados concretos que contribuyen a él. Una meta es el valor que se espera alcanzar. Un indicador es una medida que permite saber si se logra un objetivo, y el medio de verificación es el documento que prueba el valor del indicador, como una planilla archivada. Las actividades son las tareas, cada una con un responsable y un plazo.",
        "El cronograma es el calendario de las actividades. El presupuesto es el costo estimado de cada actividad y el total. Un objetivo bien formulado tiene un verbo, un resultado medible y un plazo; «registrar mejor» es vago, mientras que «registrar el 100 % de los desembarques en planilla durante el año» se puede medir. Por ejemplo, con meta de 20 muestras y 15 hechas, el cumplimiento es 75 %.",
        f"Los roles: la directiva presenta el plan en nombre de la organización; el asesor técnico apoya; los socios ejecutan y aportan datos veraces; la autoridad pesquera evalúa y fiscaliza según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("objetivo general", "lo que se quiere lograr en grande"), ("objetivo específico", "resultado concreto y medible que contribuye al objetivo general"), ("meta", "valor que se espera alcanzar"), ("indicador", "medida que permite saber si se logra un objetivo"), ("medio de verificación", "documento que prueba el valor de un indicador"), ("cronograma", "calendario de las actividades"), ("presupuesto", "costo estimado de cada actividad y total"), ("directiva", "grupo que representa a la organización y presenta el plan")],
    worked=[
        ("Calcular un indicador", "Un plan de ejemplo anota 80 desembarques y 56 con planilla completa. ¿Cuál es el porcentaje?", ["Se multiplica 56 por 100: 5.600.", "5.600 dividido en 80 es 70."], "70 %"),
        ("Distinguir meta e indicador", "En un plan de ejemplo, «número de muestras por mes» es el valor que se mide y «6 muestras por mes» es lo que se espera. ¿Cuál es el indicador y cuál la meta?", ["El indicador es lo que se mide.", "La meta es el valor esperado."], "Indicador: número de muestras por mes; meta: 6 muestras por mes"),
    ],
    mistakes=[("Formular un objetivo vago, como «mejorar los registros», sin valor ni plazo.", "No se puede saber si se logró.", "Se agrega un valor medible y un plazo."),
              ("Llamar meta a lo que se mide y indicador a lo que se espera.", "Se invierten las dos ideas.", "El indicador es la medida; la meta es el valor esperado.")],
    T=[
        ("abc", "En Pesquería: ¿qué es un indicador de un plan de manejo?", "Una medida que permite saber si se logra un objetivo", "El valor máximo de la cuota", "El nombre de la organización", "El indicador mide el avance hacia el objetivo."),
        ("abc", "En Pesquería: ¿qué es un objetivo específico de un plan?", "Un resultado concreto y medible que contribuye al objetivo general", "El presupuesto total del plan", "La lista de socios que firman", "Un objetivo específico es un resultado concreto y medible."),
        ("abc", "En Pesquería: ¿qué es un medio de verificación?", "El documento que prueba el valor de un indicador, como una planilla archivada", "La persona que escribe el plan", "El permiso para pescar", "El medio de verificación respalda el indicador."),
        ("=", "{F} ¿Cuál es el presupuesto total del plan?", "50000+300000+450000", "Se suman los costos de las tres actividades.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de los desembarques del primer mes tuvo planilla completa?", "216*100//240", "Se multiplican por 100 las planillas completas y se dividen entre los desembarques.", " %"),
        ("abc", "{F} ¿Qué indicador corresponde al objetivo específico 1?", "El porcentaje de desembarques con planilla completa", "El número de socios de la organización", "El precio por kilo de la especie A", "El objetivo 1 trata de registrar todas las capturas."),
        ("=", "{F} ¿Qué porcentaje de la meta de muestras de tallas se cumplió el primer mes?", "3*100//4", "Se multiplican por 100 las muestras hechas y se dividen entre la meta.", " %"),
        ("=", "{F} ¿Cuántos desembarques del primer mes no tuvieron planilla completa?", "240-216", "Se restan los desembarques con planilla completa del total.", " desembarques"),
        ("abc", "{F} ¿Qué rol presenta el plan en nombre de la organización?", "La directiva", "La autoridad pesquera", "El asesor técnico", "La directiva representa a la organización; la autoridad evalúa y el asesor apoya."),
        ("abc", "{F} ¿Por qué cada actividad del plan debe tener un responsable y un plazo?", "Porque sin ellos nadie sabe quién la hace ni cuándo, y no se puede verificar", "Porque así el plan se ve más largo", "Porque el plazo reemplaza al presupuesto", "El responsable y el plazo hacen exigible y verificable cada actividad."),
        ("abc", "{F} Un compañero propone como objetivo específico «registrar mejor». ¿Qué le falta?", "Un valor medible y un plazo, por ejemplo registrar el 100 % de los desembarques", "Nada, porque ya es un buen objetivo", "Un precio de venta", "Sin valor ni plazo no se puede saber si se logró."),
        ("=", "{F} Si la balanza se compra con un aporte del programa del 60 %, ¿cuántos pesos pone la organización?", "450000-450000*60//100", "Se restan del costo de la balanza los pesos que aporta el programa.", " pesos"),
        ("abc", "{F} Alguien propone anotar 100 % en el informe del primer mes aunque el resultado fue 90 %. ¿Qué respondes?", "Que no: el informe debe reflejar el resultado real, y se consulta con un adulto responsable", "Que sí, si se mejora en el segundo mes", "Que sí, porque la diferencia es pequeña", "Un informe falso oculta el problema y perjudica la evaluación del plan."),
    ],
    ctx=("abc", "Un dirigente te pide agregar al plan un indicador que no se podrá medir, pero que «suena bien» ante el programa de fomento. ¿Qué respondes?", "Que no, porque un indicador debe poder medirse con un medio de verificación, y que lo consultarás con un adulto responsable", "Que sí, porque nadie lo revisará", "Que sí, si se explica en el informe final", "Un indicador que no se puede medir no sirve para evaluar el avance."),
    sc=[
        ("En Pesquería: ¿qué diferencia hay entre indicador y meta?", "El indicador es lo que se mide y la meta es el valor esperado", "Uno es la medida y la otra es el valor que se quiere alcanzar."),
        ("En Pesquería: ¿qué es un cronograma?", "El calendario de las actividades", "El cronograma ordena las actividades en el tiempo."),
        ("En Pesquería: ¿qué rol evalúa y fiscaliza el plan?", "La autoridad pesquera", "La autoridad pesquera evalúa según la norma vigente."),
    ],
    op=("Plan de ejemplo: objetivo específico «medir tallas todos los meses»; indicador: número de muestras por mes, meta 5; presupuesto: capacitación 200.000 pesos, planillas 40.000 pesos y balanza 360.000 pesos; en el primer mes se hicieron 4 muestras y hubo 150 desembarques, 120 con planilla completa. Escribe (a) el presupuesto total, (b) el cumplimiento de la meta de muestras, (c) el porcentaje de desembarques con planilla completa, (d) un medio de verificación para cada indicador.",
        "(a) 200.000 + 40.000 + 360.000 = 600.000 pesos. (b) 4 × 100 ÷ 5 = 80 %. (c) 120 × 100 ÷ 150 = 80 %. (d) Para las muestras, la planilla de muestreo de tallas archivada; para los desembarques, las planillas de desembarque archivadas. Los datos deben ser veraces.",
        ["suma el presupuesto", "calcula el cumplimiento", "calcula el porcentaje de planillas", "nombra los medios de verificación"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre las muestras hechas", "confundir meta e indicador", "no nombrar el medio de verificación"],
        "Pregunta: «¿qué documento prueba el valor de cada indicador?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe un objetivo específico inventado con un indicador, una meta y un medio de verificación.",
    extend="Explica con un ejemplo por qué un indicador sin medio de verificación no sirve para evaluar un plan.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (diagnóstico de ejemplo, inventado). «Caleta Demo», especie A. Desembarques por año: año 1, 200.000 kg; año 2, 180.000 kg; año 3, 162.000 kg. En una muestra de tallas, el 30 % está bajo la talla mínima de ejemplo. "
     "Problemas detectados, con puntaje de 1 a 3 en gravedad, urgencia y factibilidad: problema A, baja de desembarques y de tallas: 3, 2 y 2; problema B, muelle sin barandas ni iluminación: 3, 3 y 3; problema C, falta de organización para vender: 2, 1 y 2. "
     "Regla de ejemplo: el problema prioritario es el de mayor puntaje total.")
build(
    O7, 3, F,
    use="Aprenderé a analizar el diagnóstico de una caleta, a leer tendencias, a priorizar problemas con una matriz y a formular un objetivo específico medible.",
    prior=["Sé qué son un plan de manejo, un objetivo y un indicador.", "Sé calcular una variación porcentual y una tendencia.", "Sé sumar números enteros."],
    explain=[
        "Un diagnóstico es el análisis de la situación de una caleta antes de planificar: reúne datos, detecta problemas y explica sus causas probables, que son explicaciones posibles que hay que comprobar. Una tendencia es el comportamiento de un dato en el tiempo; si los desembarques bajan año a año, la tendencia es decreciente. La caída porcentual entre dos años es (anterior − actual) × 100 ÷ anterior.",
        "Para decidir por dónde empezar se usa una matriz de priorización: una tabla que da puntaje a cada problema según criterios, como gravedad, urgencia y factibilidad, y suma los puntajes. El problema prioritario es el de mayor puntaje. Después se formula un objetivo específico con un verbo, un resultado medible y un plazo. Por ejemplo, con puntajes 2, 2 y 3, el total es 7.",
        f"En un diagnóstico no se oculta ni se inventa ningún dato, aunque preocupe a los socios. La seguridad de las personas pesa mucho en la gravedad. {EMER} {AVISO}",
    ],
    vocab=[("diagnóstico", "análisis de la situación antes de planificar"), ("tendencia decreciente", "comportamiento en que los valores bajan en el tiempo"), ("caída porcentual", "(anterior − actual) × 100 ÷ anterior"), ("matriz de priorización", "tabla que da puntaje a los problemas según criterios y los suma"), ("problema prioritario", "problema con mayor puntaje total"), ("gravedad", "cuánto daño produce un problema"), ("urgencia", "cuán pronto hay que actuar"), ("factibilidad", "cuán posible es resolver el problema")],
    worked=[
        ("Calcular una caída", "Los desembarques de ejemplo bajan de 500 kg a 400 kg. ¿Cuál es la caída porcentual?", ["La diferencia es 100 kg.", "100 por 100 dividido entre 500 es 20."], "20 %"),
        ("Priorizar", "Dos problemas de ejemplo tienen puntajes 3, 3 y 1 el primero, y 2, 2 y 2 el segundo. ¿Cuál es prioritario?", ["El primero suma 7.", "El segundo suma 6, así que gana el primero."], "El primero, con 7 puntos"),
    ],
    mistakes=[("Omitir un dato del diagnóstico para no preocupar a los socios.", "Un diagnóstico incompleto lleva a decisiones equivocadas.", "Se incluyen todos los datos y se explican con calma."),
              ("Formular el objetivo como «mejorar el muelle» sin valor ni plazo.", "No se puede saber si se cumplió.", "Se agrega un resultado medible y un plazo.")],
    T=[
        ("abc", "En Pesquería: ¿qué es un diagnóstico de una caleta?", "El análisis de la situación antes de planificar, con datos y problemas detectados", "El plan de actividades del próximo año", "El registro de una sola faena", "El diagnóstico describe la situación; el plan y el registro son otros documentos."),
        ("abc", "En Pesquería: ¿qué es una matriz de priorización?", "Una tabla que da puntaje a los problemas según criterios y los suma", "Una lista de los socios por orden alfabético", "Un calendario de las faenas", "La matriz suma puntajes de criterios para decidir."),
        ("abc", "En Pesquería: ¿qué es el problema prioritario?", "El problema con el mayor puntaje total en la matriz", "El problema que menos cuesta", "El primero que alguien menciona", "La prioridad sale de la matriz, no de quién habla primero."),
        ("=", "{F} ¿Qué porcentaje cayeron los desembarques del año 1 al año 2?", "(200000-180000)*100//200000", "Se divide la caída entre el valor anterior y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje cayeron los desembarques del año 2 al año 3?", "(180000-162000)*100//180000", "Se divide la caída entre el valor anterior y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué tendencia muestran los desembarques de los tres años?", "Decreciente: bajan año a año", "Creciente: suben año a año", "Estable: no cambian", "Cada año es menor que el anterior."),
        ("=", "{F} ¿Cuál es el puntaje total del problema A?", "3+2+2", "Se suman la gravedad, la urgencia y la factibilidad.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total del problema B?", "3+3+3", "Se suman la gravedad, la urgencia y la factibilidad.", " puntos"),
        ("abc", "{F} ¿Cuál es el problema prioritario según la regla de la ficha?", "El problema B, con 9 puntos", "El problema A, con 7 puntos", "El problema C, con 5 puntos", "B tiene el mayor puntaje total."),
        ("abc", "{F} ¿Por qué el problema B va primero aunque los desembarques estén bajando?", "Porque compromete la seguridad de las personas y se puede resolver pronto, y la matriz le da mayor puntaje", "Porque el muelle es más caro que el recurso", "Porque la matriz solo mira el muelle", "La matriz dio más puntos a B por gravedad, urgencia y factibilidad."),
        ("abc", "{F} ¿Qué objetivo específico para el problema B está bien formulado?", "Instalar barandas e iluminación fija en el muelle en 6 meses, con personal autorizado", "Mejorar el muelle", "Hacer que todo funcione mejor", "Un buen objetivo tiene un resultado medible y un plazo."),
        ("=", "{F} ¿Cuántos kilos suman los desembarques de los tres años?", "200000+180000+162000", "Se suman los desembarques anuales.", " kg"),
        ("abc", "{F} Un dirigente propone omitir del diagnóstico el 30 % de ejemplares bajo la talla mínima «para no preocupar a los socios». ¿Qué respondes?", "Que no: el diagnóstico debe incluir todos los datos veraces, y que lo consultarás con un adulto responsable", "Que sí, si lo informas verbalmente", "Que sí, porque los socios no entienden los porcentajes", "Omitir un dato lleva a decisiones equivocadas."),
    ],
    ctx=("abc", "Alguien te pide cambiar el puntaje de seguridad del muelle en la matriz para que otro proyecto quede primero. ¿Qué respondes?", "Que no, porque los puntajes deben reflejar los datos, y que lo consultarás con un adulto responsable", "Que sí, si después se corrige", "Que sí, si es solo un punto", "Manipular un puntaje falsea la priorización."),
    sc=[
        ("En Pesquería: ¿cómo se calcula la caída porcentual entre dos años?", "Caída por 100, dividida por el valor anterior", "La caída se mide respecto del valor anterior."),
        ("En Pesquería: ¿qué criterios usa la matriz de la ficha?", "Gravedad, urgencia y factibilidad", "Son los tres criterios con que se dio puntaje."),
        ("En Pesquería: ¿qué tiene un objetivo específico bien formulado?", "Un resultado medible y un plazo", "Sin medida y plazo no se puede evaluar."),
    ],
    op=("Diagnóstico de ejemplo: desembarques de 300.000 kg, 270.000 kg y 243.000 kg en tres años; problemas: A, baja de desembarques (puntajes 3, 2 y 2); B, rampa resbaladiza y sin iluminación (3, 3 y 2); C, falta de hielo para conservar (2, 2 y 2). Escribe (a) la caída porcentual de cada año, (b) el puntaje total de cada problema, (c) cuál es prioritario, (d) un objetivo específico medible para ese problema.",
        "(a) Del año 1 al 2: 30.000 × 100 ÷ 300.000 = 10 %; del año 2 al 3: 27.000 × 100 ÷ 270.000 = 10 %. (b) A: 7; B: 8; C: 6. (c) El problema B, con 8 puntos. (d) Por ejemplo, instalar iluminación fija y una superficie antideslizante en la rampa en 6 meses, con personal autorizado. Los datos deben ser veraces.",
        ["calcula las caídas", "suma los puntajes", "elige el problema prioritario", "formula un objetivo medible"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre el valor actual", "elegir el problema A por intuición", "formular un objetivo sin plazo"],
        "Pregunta: «¿qué problema suma más puntos?». Si no responde, pídele que sume los tres criterios de cada problema."),
    reinforce="Inventa un diagnóstico con dos problemas y puntajes, y decide cuál es prioritario.",
    extend="Explica por qué la gravedad de un problema de seguridad pesa mucho al priorizar.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (proyecto de emprendimiento de ejemplo, inventado). La organización ficticia quiere vender producto en el mercado local con cadena de frío. Inversión inicial: 3.000.000 de pesos. El programa de fomento de ejemplo aporta el 60 % de la inversión y no cubre los gastos mensuales. "
     "Ingresos mensuales de ejemplo: 700.000 pesos. Costos mensuales de ejemplo: 400.000 pesos.")
build(
    O7, 4, F,
    use="Aprenderé a aplicar criterios económicos a un proyecto: margen mensual, aporte propio y período de recuperación de la inversión, y a probar el efecto de cambiar un supuesto.",
    prior=["Sé qué son un presupuesto y un indicador.", "Sé calcular el margen como ingreso menos costo.", "Sé multiplicar, dividir y restar números enteros."],
    explain=[
        "La inversión inicial es el gasto que se hace una vez para comenzar, como comprar equipos. El ingreso mensual es lo que se obtiene cada mes por vender; el costo mensual es lo que se gasta cada mes para operar. El margen mensual es el ingreso mensual menos el costo mensual. El período de recuperación es el número de meses que demora el margen en igualar lo que puso la organización, y se calcula dividiendo esa inversión entre el margen mensual.",
        "El aporte propio es la parte de la inversión que pone la organización, es decir, el total menos lo que aporta el programa. Un supuesto es un dato que se da por cierto para calcular, como los ingresos mensuales; si el supuesto cambia, el resultado cambia, por eso se prueban escenarios. Por ejemplo, con inversión de 900.000 pesos y margen de 150.000 al mes, la recuperación es de 6 meses.",
        f"Estos cálculos son de ejemplo y el programa real fija sus propias bases. Un proyecto serio presenta supuestos y escenarios veraces, no solo el caso favorable. {EMER} {AVISO}",
    ],
    vocab=[("inversión inicial", "gasto que se hace una vez para comenzar"), ("ingreso mensual", "lo que se obtiene cada mes por vender"), ("costo mensual", "lo que se gasta cada mes para operar"), ("margen mensual", "ingreso mensual menos costo mensual"), ("aporte propio", "parte de la inversión que pone la organización"), ("período de recuperación", "meses que demora el margen en igualar la inversión propia"), ("supuesto", "dato que se da por cierto para calcular"), ("escenario", "resultado del cálculo con otros supuestos")],
    worked=[
        ("Calcular el aporte propio", "Una inversión de ejemplo es de 800.000 pesos y el programa aporta el 50 %. ¿Cuánto pone la organización?", ["El programa aporta 400.000 pesos.", "800.000 menos 400.000 es 400.000."], "400.000 pesos"),
        ("Período de recuperación", "Con un aporte propio de 400.000 pesos y un margen de 100.000 al mes, ¿cuántos meses se tarda en recuperar la inversión?", ["Se divide el aporte propio entre el margen mensual.", "400.000 dividido en 100.000 es 4."], "4 meses"),
    ],
    mistakes=[("Presentar solo el escenario más favorable al programa de fomento.", "Oculta riesgos y puede llevar a decisiones equivocadas.", "Se presentan los supuestos reales y escenarios de riesgo."),
              ("Olvidar incluir los costos mensuales para que el proyecto se vea más rentable.", "Un margen sin costos es falso.", "El margen se calcula siempre con ingresos menos costos.")],
    T=[
        ("abc", "En Pesquería: ¿qué es la inversión inicial de un proyecto?", "El gasto que se hace una vez para comenzar, como comprar equipos", "El gasto mensual de operación", "El ingreso que se espera cada mes", "La inversión es un gasto inicial; los costos mensuales se repiten."),
        ("abc", "En Pesquería: ¿qué es el período de recuperación de la inversión propia?", "Los meses que demora el margen en igualar lo que puso la organización", "El plazo para presentar el proyecto", "La vida útil de los equipos", "La recuperación compara margen e inversión propia."),
        ("abc", "En Pesquería: ¿qué es un supuesto de un proyecto?", "Un dato que se da por cierto para calcular, como los ingresos mensuales", "Un resultado ya comprobado", "Una obligación de la norma", "Un supuesto puede cambiar y por eso se prueban escenarios."),
        ("=", "{F} ¿Cuál es el margen mensual del proyecto?", "700000-400000", "Se resta el costo mensual del ingreso mensual.", " pesos"),
        ("=", "{F} ¿Cuántos pesos aporta el programa de fomento a la inversión?", "3000000*60//100", "Se multiplica la inversión por 60 y se divide entre 100.", " pesos"),
        ("=", "{F} ¿Cuántos pesos pone la organización como aporte propio?", "3000000-3000000*60//100", "Se resta de la inversión total lo que aporta el programa.", " pesos"),
        ("=", "{F} ¿Cuántos meses tardaría en recuperarse toda la inversión de 3.000.000 de pesos sin el aporte del programa?", "3000000//(700000-400000)", "Se divide la inversión total entre el margen mensual.", " meses"),
        ("=", "{F} ¿Cuántos meses tarda la organización en recuperar su aporte propio?", "(3000000-3000000*60//100)//(700000-400000)", "Se divide el aporte propio entre el margen mensual.", " meses"),
        ("abc", "{F} ¿Qué gastos no cubre el programa de fomento de la ficha?", "Los costos mensuales de operación, que la organización paga con sus ingresos", "La inversión inicial completa", "Ningún gasto, porque lo cubre todo", "La ficha dice que el programa aporta una parte de la inversión y no cubre los gastos mensuales."),
        ("abc", "{F} Un compañero dice que, como el período de recuperación es corto, el proyecto no tiene riesgo. ¿Qué respuesta es correcta?", "Es falso: si los ingresos bajan o los costos suben, el plazo se alarga, por eso se prueban escenarios", "Es cierto: un plazo corto elimina el riesgo", "Es cierto si el programa aporta más del 50 %", "Los supuestos pueden cambiar y alterar el resultado."),
        ("abc", "{F} Alguien propone no incluir los costos mensuales para que el proyecto parezca más rentable. ¿Qué respondes?", "Que no: sin los costos el margen es falso, y que lo consultarás con un adulto responsable", "Que sí, si el programa no lo pide", "Que sí, si se agregan después", "Omitir los costos falsea el resultado del proyecto."),
        ("=", "{F} Si los ingresos mensuales bajaran a 600.000 pesos, ¿en cuántos meses se recuperaría el aporte propio?", "(3000000-3000000*60//100)//(600000-400000)", "Se divide el aporte propio entre el nuevo margen mensual.", " meses"),
        ("=", "{F} Si los costos mensuales subieran a 550.000 pesos con ingresos de 700.000, ¿en cuántos meses se recuperaría el aporte propio?", "(3000000-3000000*60//100)//(700000-550000)", "Se divide el aporte propio entre el nuevo margen mensual.", " meses"),
    ],
    ctx=("abc", "Un conocido te pide que, en un proyecto de ejemplo, escribas ingresos mensuales mayores a los reales para convencer al programa de fomento. ¿Qué respondes?", "Que no, porque los supuestos deben ser veraces, y que lo consultarás con un adulto responsable", "Que sí, solo un poco", "Que sí, si el programa no revisa", "Un supuesto inflado engaña al programa y pone en riesgo a la organización."),
    sc=[
        ("En Pesquería: ¿cómo se calcula el margen mensual de un proyecto?", "Ingreso mensual menos costo mensual", "El margen es lo que queda tras pagar los costos."),
        ("En Pesquería: ¿cómo se calcula el período de recuperación?", "Aporte propio dividido por el margen mensual", "Se compara lo invertido con lo que deja cada mes."),
        ("En Pesquería: ¿para qué se prueban escenarios en un proyecto?", "Para ver cómo cambia el resultado si cambian los supuestos", "Los supuestos pueden fallar y hay que anticiparlo."),
    ],
    op=("Proyecto de ejemplo: inversión de 2.000.000 de pesos; el programa de ejemplo aporta el 50 %; ingresos mensuales de ejemplo, 500.000 pesos; costos mensuales, 300.000 pesos. Escribe (a) el margen mensual, (b) el aporte propio, (c) los meses en recuperar el aporte propio, (d) los meses si los ingresos bajan a 400.000 pesos y qué indica eso.",
        "(a) 500.000 − 300.000 = 200.000 pesos. (b) 2.000.000 − 1.000.000 = 1.000.000 pesos. (c) 1.000.000 ÷ 200.000 = 5 meses. (d) El margen baja a 100.000 pesos y la recuperación sube a 10 meses: un supuesto distinto cambia el resultado, por eso se prueban escenarios.",
        ["calcula el margen", "calcula el aporte propio", "calcula la recuperación", "prueba un escenario y lo interpreta"],
        ["hoja con las cuatro respuestas"],
        ["dividir la inversión total en vez del aporte propio", "olvidar los costos mensuales", "no interpretar el escenario"],
        "Pregunta: «¿qué cantidad divides entre el margen mensual?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un proyecto con inversión, ingresos y costos mensuales, y calcula la recuperación en dos escenarios.",
    extend="Explica por qué un proyecto con recuperación corta puede igual ser riesgoso.",
)

# ============================================================ OAE-07, clase 5
F = ("Ficha 5 (alternativas y borrador de ejemplo, inventados). Dos proyectos para Caleta Demo, con puntaje de 1 a 3 en seguridad, factibilidad, costo y ambiente; el criterio seguridad pesa el doble. "
     "Proyecto P1, barandas e iluminación del muelle: seguridad 3, factibilidad 2, costo 2, ambiente 3. Proyecto P2, galpón de venta: seguridad 2, factibilidad 3, costo 3, ambiente 2. "
     "Borrador de presupuesto de ejemplo: letreros, 100.000 pesos; barandas, 600.000; iluminación, 250.000; capacitación, 150.000; total declarado, 1.000.000. "
     "Cronograma del borrador: A1, meses 1 a 3; A2, meses 4 a 9; A3, meses 10 a 14. El programa de ejemplo financia proyectos de hasta 12 meses. En el borrador, la capacitación no tiene responsable y el objetivo específico 2 no tiene indicador.")
build(
    O7, 5, F,
    use="Aprenderé a comparar proyectos con criterios ponderados y a verificar la coherencia de un borrador: presupuesto, cronograma, responsables e indicadores.",
    prior=["Sé qué son un presupuesto, un cronograma y un indicador.", "Sé sumar y restar números enteros.", "Sé que los datos de un proyecto deben ser veraces."],
    explain=[
        "Para comparar proyectos se usan criterios con puntaje, y a veces un criterio pesa más que otro: eso es la ponderación. Si la seguridad pesa el doble, su puntaje se multiplica por 2 antes de sumar. Por ejemplo, con seguridad 2, factibilidad 3 y costo 1, el total ponderado es 4 más 3 más 1, es decir, 8. Gana el proyecto de mayor total, y la seguridad no se sacrifica por ahorrar.",
        "Verificar la coherencia de un borrador es comprobar que sus partes se correspondan: cada objetivo con su indicador, cada actividad con un responsable y un plazo, el total del presupuesto con la suma de sus partidas y el cronograma con el plazo máximo del programa. Una incoherencia no se oculta: se corrige el borrador con el dato verificado y se deja registro del cambio.",
        f"Un plan o proyecto solo se ejecuta con personal autorizado y la norma vigente; este cuaderno solo practica la redacción en papel. {EMER} {AVISO}",
    ],
    vocab=[("ponderación", "dar más peso a un criterio más importante"), ("total ponderado", "suma de puntajes después de aplicar los pesos"), ("coherencia", "correspondencia entre las partes de un plan"), ("partida", "línea de un presupuesto con su costo"), ("plazo máximo", "límite de meses que fija el programa"), ("responsable", "persona asignada a una actividad")],
    worked=[
        ("Total ponderado", "Un proyecto de ejemplo tiene seguridad 3, factibilidad 1 y costo 2, y la seguridad pesa el doble. ¿Cuál es el total?", ["La seguridad ponderada es 3 por 2, es decir, 6.", "6 más 1 más 2 es 9."], "9 puntos"),
        ("Verificar un total", "Un presupuesto de ejemplo tiene partidas de 200.000 y 300.000 pesos y declara un total de 600.000. ¿Es coherente?", ["La suma de las partidas es 500.000.", "El total declarado es 600.000: no coincide."], "No es coherente: la suma es 500.000"),
    ],
    mistakes=[("Elegir un proyecto por el costo sin considerar la ponderación de la seguridad.", "El costo ya está en el puntaje y la seguridad pesa más.", "Se compara el total ponderado."),
              ("Dejar el total declarado distinto de la suma de las partidas.", "Un presupuesto incoherente pierde credibilidad.", "Se corrige el total con la suma verificada y se anota el cambio.")],
    T=[
        ("abc", "En Pesquería: ¿qué es la ponderación de un criterio?", "Darle más peso a un criterio más importante", "Borrar el criterio con menor puntaje", "Sumar los puntajes sin cambios", "Ponderar cambia el peso de un criterio en el total."),
        ("abc", "En Pesquería: ¿qué es la coherencia de un plan o proyecto?", "Que objetivos, actividades, indicadores y presupuesto se correspondan entre sí", "Que el texto sea lo más largo posible", "Que todas las actividades duren lo mismo", "La coherencia es correspondencia entre las partes."),
        ("abc", "En Pesquería: ¿qué es una partida de un presupuesto?", "Una línea con el costo de una actividad o compra", "El total final de un proyecto", "El nombre del responsable", "Cada partida tiene su costo y se suman para obtener el total."),
        ("=", "{F} ¿Cuál es el total ponderado del proyecto P1?", "3*2+2+2+3", "Se multiplica la seguridad por 2 y se suman los demás puntajes.", " puntos"),
        ("=", "{F} ¿Cuál es el total ponderado del proyecto P2?", "2*2+3+3+2", "Se multiplica la seguridad por 2 y se suman los demás puntajes.", " puntos"),
        ("abc", "{F} ¿Qué proyecto conviene según el total ponderado?", "El proyecto P1, con 13 puntos", "El proyecto P2, con 12 puntos", "Ambos, porque tienen puntajes parecidos", "P1 suma más que P2 con la seguridad ponderada."),
        ("=", "{F} ¿Cuántos pesos suman las cuatro partidas del presupuesto?", "100000+600000+250000+150000", "Se suman los costos de las cuatro partidas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos de diferencia hay entre la suma de las partidas y el total declarado?", "100000+600000+250000+150000-1000000", "Se resta el total declarado de la suma de las partidas.", " pesos"),
        ("abc", "{F} ¿Qué actividad del cronograma supera el plazo máximo del programa?", "La A3, porque llega hasta el mes 14", "La A1, porque empieza en el mes 1", "La A2, porque dura 6 meses", "El programa financia hasta 12 meses y A3 llega al mes 14."),
        ("=", "{F} ¿Cuántos meses se pasa el cronograma del plazo máximo del programa?", "14-12", "Se resta el plazo máximo del último mes del cronograma.", " meses"),
        ("abc", "{F} ¿Qué corresponde hacer con la diferencia entre la suma de las partidas y el total declarado?", "Corregir el borrador con la suma verificada y dejar registro del cambio", "Dejar el total declarado para no cambiar el documento", "Quitar una partida para que cuadre sin avisar", "Una incoherencia se corrige con el dato verificado y se registra."),
        ("abc", "{F} Un compañero dice que P2 conviene porque tiene mejor puntaje de factibilidad y costo. ¿Qué respuesta es correcta?", "Es falso: con la seguridad ponderada, P1 suma 13 y P2 suma 12", "Es cierto: factibilidad y costo deciden", "Es cierto si P2 es más barato", "La ponderación da más peso a la seguridad y cambia el total."),
        ("abc", "{F} La capacitación no tiene responsable en el borrador. ¿Qué corresponde?", "Asignar un responsable con nombre, acordado con la organización, antes de presentar el borrador", "Dejarla sin responsable porque la hará cualquiera", "Asignar a la autoridad pesquera como responsable", "Cada actividad necesita un responsable acordado."),
    ],
    ctx=("abc", "Alguien te pide cambiar el plazo del borrador a 12 meses sin cambiar las actividades, para que el programa lo acepte. ¿Qué respondes?", "Que no, porque el cronograma debe reflejar la realidad, y que lo consultarás con un adulto responsable", "Que sí, si el programa no revisa", "Que sí, porque son solo dos meses", "Un cronograma falso perjudica la ejecución y la rendición del proyecto."),
    sc=[
        ("En Pesquería: ¿cómo se calcula el total ponderado cuando la seguridad pesa el doble?", "Se multiplica la seguridad por 2 y se suman los demás puntajes", "La ponderación cambia el peso de la seguridad."),
        ("En Pesquería: ¿qué se verifica en la coherencia de un presupuesto?", "Que el total declarado sea igual a la suma de las partidas", "El total debe corresponder a sus partes."),
        ("En Pesquería: ¿qué necesita cada actividad de un plan?", "Un responsable y un plazo", "Sin ellos no se puede exigir ni verificar."),
    ],
    op=("Alternativas de ejemplo: proyecto Q1, seguridad 3, factibilidad 3, costo 1, ambiente 2; proyecto Q2, seguridad 2, factibilidad 3, costo 3, ambiente 3; la seguridad pesa el doble. Borrador: partidas de 300.000, 450.000 y 150.000 pesos, con total declarado de 800.000 pesos; actividad B1 hasta el mes 11 con plazo máximo de 12; el objetivo 1 no tiene indicador. Escribe (a) el total ponderado de cada proyecto, (b) cuál conviene, (c) la suma real de las partidas y la diferencia, (d) qué corriges en el borrador.",
        "(a) Q1: 3 × 2 + 3 + 1 + 2 = 12; Q2: 2 × 2 + 3 + 3 + 3 = 13. (b) Q2, con 13 puntos. (c) 300.000 + 450.000 + 150.000 = 900.000; la diferencia con el total declarado es 100.000. (d) Corregir el total a 900.000 con registro del cambio y agregar un indicador al objetivo 1; el plazo de la actividad B1 sí cumple, porque 11 es menor que 12.",
        ["calcula los totales ponderados", "elige el proyecto", "suma las partidas y halla la diferencia", "propone correcciones coherentes"],
        ["hoja con las cuatro respuestas"],
        ["olvidar duplicar la seguridad", "no sumar bien las partidas", "decir que B1 supera el plazo"],
        "Pregunta: «¿qué criterio se multiplica por 2?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos proyectos con cuatro puntajes y calcula cuál conviene con la seguridad ponderada.",
    extend="Explica por qué un total declarado que no coincide con la suma de las partidas debilita un proyecto.",
)
