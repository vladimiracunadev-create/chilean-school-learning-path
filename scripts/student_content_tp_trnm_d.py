"""Tripulación de Naves Mercantes y Especiales TP 3.º y 4.º medio: OAE-07 (reposición y reparación de piezas de equipos de cubierta como conceptos, listas de piezas y registros) y OAE-08 (supervivencia en el mar, primeros auxilios, seguridad de la vida humana y combate de incendio: solo conceptos, planillas y reglas generales). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_trnm_common import AVISO, EMER, build

O7 = "TP-TRNM-3y4-OAE-07"
O8 = "TP-TRNM-3y4-OAE-08"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En la cubierta de la «Nave Demo» hay 4 equipos con sistemas distintos: una grúa con sistema hidráulico (usa aceite a presión), un huinche con sistema electromecánico (motor eléctrico y piezas mecánicas), "
     "un cabrestante con sistema neumático (usa aire a presión) y una escotilla con sistema mecánico. Peligros anotados: fluido a presión que puede salir por una fuga, energía almacenada, partes que se mueven, cargas suspendidas y aceite hidráulico usado.")
build(
    O7, 1, F,
    use="Aprenderé qué significan reponer y reparar piezas, qué tipos de sistemas tienen los equipos de cubierta, qué peligros tienen y por qué esas tareas las hace solo personal autorizado.",
    prior=["Sé qué son los equipos de maniobra.", "Sé qué es un plan de mantenimiento y qué es la energía almacenada.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Reponer una pieza es cambiar una pieza desgastada por otra nueva; reparar es devolver una pieza a buen estado. El desgaste es la pérdida de material por el uso y el deterioro es el daño por el paso del tiempo, los golpes o la corrosión. Los equipos de cubierta pueden tener sistemas mecánicos (piezas que se mueven), electromecánicos (motor eléctrico más piezas mecánicas), hidráulicos (aceite a presión) y neumáticos (aire a presión). Reponer o reparar se hace según el manual del fabricante y la norma vigente, y solo lo hace personal autorizado.",
        "Los peligros de estas tareas son los fluidos a presión, que pueden salir por una fuga con fuerza y lesionar; la energía almacenada en resortes, cañerías o cables; las partes que se mueven; y las cargas suspendidas. El aceite hidráulico usado es un residuo y no se vierte al mar. Un ejemplo con otra nave: una manguera hidráulica con un abultamiento es una señal de deterioro que se informa y se registra, no se manipula.",
        f"Este cuaderno enseña los conceptos, los documentos y los cálculos de planilla; no enseña a reponer ni a reparar piezas. {EMER} {AVISO}",
    ],
    vocab=[("reponer", "cambiar una pieza desgastada por una nueva"), ("reparar", "devolver una pieza a buen estado"), ("desgaste", "pérdida de material por el uso"), ("deterioro", "daño por el tiempo, los golpes o la corrosión"), ("sistema hidráulico", "sistema que funciona con aceite a presión"), ("sistema neumático", "sistema que funciona con aire a presión"), ("sistema electromecánico", "sistema con motor eléctrico y piezas mecánicas")],
    worked=[
        ("Clasificar un sistema", "En una nave de ejemplo un equipo funciona con aire a presión. ¿Qué tipo de sistema es?", ["El aire a presión es propio de un sistema neumático.", "El aceite a presión sería hidráulico."], "Neumático"),
        ("Peligro y riesgo", "En una nave de ejemplo una manguera hidráulica tiene una fuga fina de aceite a presión. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el chorro de aceite a presión.", "El riesgo es que lesione a una persona cercana."], "Peligro: el chorro de aceite a presión; riesgo: que lesione a una persona"),
    ],
    mistakes=[("Creer que si el equipo está apagado se puede cambiar una pieza sin riesgo.", "Puede conservar energía almacenada o fluido a presión.", "Solo personal autorizado lo interviene, con los permisos de la norma vigente."),
              ("Creer que una fuga pequeña no es peligrosa.", "Un chorro a presión, aunque fino, puede lesionar.", "Informa la fuga y no te acerques ni la toques.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué significa reponer una pieza de un equipo?", "Cambiar una pieza desgastada por una nueva", "Devolver una pieza a buen estado sin cambiarla", "Anotar la pieza en un registro", "Reponer es cambiar por una nueva; reparar es devolver a buen estado."),
        ("abc", "En Tripulación de Naves: ¿qué es el desgaste de una pieza?", "La pérdida de material por el uso", "El cambio de color por la luz", "El aumento de peso por la humedad", "El desgaste es pérdida de material causada por el uso."),
        ("abc", "{F} ¿Cuál equipo de la ficha usa un sistema neumático?", "El cabrestante", "La grúa", "La escotilla", "El cabrestante usa aire a presión; la grúa usa aceite a presión."),
        ("=", "{F} Si cada equipo de la ficha tiene 3 piezas con desgaste registradas, ¿cuántas piezas con desgaste hay en total?", "4*3", "Se multiplican los equipos de la ficha por las piezas de cada uno.", " piezas"),
        ("abc", "{F} ¿Cuál es el riesgo asociado a una fuga de fluido a presión?", "Que el chorro lesione a una persona cercana", "Que el equipo cambie de color", "Que la bodega se llene de repuestos", "El riesgo es un daño a las personas; el color y la bodega no lo son."),
        ("abc", "{F} ¿Quién repone o repara las piezas de los equipos de cubierta?", "Personal autorizado, según el manual del fabricante", "Cualquier tripulante que sepa cómo", "Un visitante con herramientas propias", "Estas tareas exigen autorización, formación y el manual del fabricante."),
        ("=", "{F} Cada reposición de una pieza del sistema hidráulico deja 5 litros de aceite usado. Con 6 reposiciones, ¿cuántos litros de residuo se generan?", "6*5", "Se multiplican las reposiciones por los litros de cada una.", " litros"),
        ("=", "{F} Si los envases de residuo son de 10 litros, ¿cuántos envases se llenan con los residuos de 6 reposiciones de 5 litros?", "(6*5)//10", "Se dividen los litros de residuo entre la capacidad de cada envase.", " envases"),
        ("abc", "{F} Para el peligro de las mangueras con fluido a presión, ¿cuál medida es de nivel más efectivo?", "Instalar una cubierta protectora fija sobre las mangueras", "Colocar un letrero que diga «peligro, presión»", "Entregar gafas a cada persona", "La cubierta cambia el lugar; el letrero informa y las gafas son EPP."),
        ("abc", "Durante una visita de ejemplo una manguera se rompe y un chorro de aceite alcanza a una persona. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, dar la alarma y avisar a un adulto responsable y a emergencias", "Acercarte para tapar la fuga con la mano", "Tirar de la manguera para alejarla", "Acercarse a un chorro a presión puede causar otra lesión; se da la alarma y se avisa."),
        ("abc", "{F} Un compañero dice: «como el huinche está apagado, puedo cambiarle una pieza sin permiso». ¿Qué respuesta es correcta?", "Es falso: puede tener energía almacenada y solo personal autorizado lo interviene", "Es cierto, porque apagado no tiene peligro", "Es cierto, si usa guantes", "Un equipo apagado puede conservar energía; los guantes no reemplazan la autorización."),
        ("=", "{F} El plan prevé 2 reposiciones por equipo al año. ¿Cuántas reposiciones hay en 3 años entre los 4 equipos de la ficha?", "4*2*3", "Se multiplican los equipos por las reposiciones anuales y por los años.", " reposiciones"),
        ("abc", "{F} Una persona nota una manguera con una grieta. ¿Qué corresponde a una persona en formación?", "Informar al responsable para que se registre, sin manipular la manguera", "Cubrir la grieta con cinta y seguir", "Cortar la parte agrietada", "Una pieza dañada se informa y se registra; no se manipula sin autorización."),
    ],
    ctx=("abc", "Un conocido te ofrece «ayudarlo a cambiar una manguera hidráulica» de la grúa de una nave porque es «rápido». ¿Qué respondes?", "Que no, porque esa tarea exige instructor autorizado, norma vigente y elementos de protección, y que lo consultarás con un adulto responsable", "Que sí, si el equipo está apagado", "Que sí, si usas guantes y gafas", "Un equipo apagado puede tener presión residual y el EPP no reemplaza la autorización."),
    sc=[
        ("En Tripulación de Naves: ¿qué es un sistema hidráulico?", "Un sistema que funciona con aceite a presión", "Hidráulico se asocia a aceite a presión."),
        ("¿Qué es el deterioro de una pieza?", "El daño por el tiempo, los golpes o la corrosión", "El deterioro no depende solo del uso."),
        ("¿Dónde se guarda el aceite hidráulico usado?", "En envases rotulados, para entregarlo según la norma vigente", "El aceite usado es un residuo y no se vierte al mar."),
    ],
    op=("En la cubierta de la «Nave Ejemplo» (caso de ejemplo) una grúa hidráulica tiene una manguera con una fuga fina de aceite junto a un pasillo que usa el personal. Escribe (a) el peligro y el riesgo, (b) un control de ingeniería, (c) qué debe hacer una persona en formación al verla, (d) cómo se maneja el aceite usado que deja la tarea.",
        "(a) Peligro: el chorro de aceite a presión; riesgo: que lesione a alguien o que alguien resbale. (b) Una cubierta protectora fija sobre la manguera o una barrera que aleje el pasillo. (c) No acercarse ni tocar la fuga, informar al oficial y registrarla. (d) Se guarda en envases rotulados y se entrega según la norma vigente; no se vierte al mar.",
        ["identifica peligro y riesgo", "propone un control de ingeniería", "indica que informa y no interviene", "explica el manejo del residuo"],
        ["hoja con las cuatro respuestas"],
        ["confundir peligro con riesgo", "proponer que la persona en formación repare la fuga", "proponer verter el aceite"],
        "Pregunta: «¿qué puede pasar y a quién?». Si no responde, pídele que relea los peligros de la explicación."),
    reinforce="Haz una tabla con los cuatro tipos de sistema, cómo funciona cada uno y un equipo de cubierta que lo use.",
    extend="Explica con un ejemplo por qué un equipo apagado puede seguir siendo peligroso.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (extracto de una lista de piezas, de ejemplo). Grúa hidráulica de ejemplo. P-101: sello hidráulico, vida útil 2.000 horas, stock 3. P-102: rodamiento, vida útil 4.000 horas, stock 1. "
     "P-103: manguera, vida útil 3.000 horas, stock 5. P-104: filtro, vida útil 1.000 horas, stock 6.")
build(
    O7, 2, F,
    use="Aprenderé a leer una lista de piezas, qué es la vida útil y el stock de repuestos, y qué documentos intervienen en la reposición de una pieza.",
    prior=["Sé qué es reponer y reparar.", "Sé qué es el stock y el manual del fabricante.", "Sé dividir números enteros."],
    explain=[
        "La lista de piezas, o despiece, es el documento del fabricante que enumera las piezas de un equipo con su código. El código de pieza identifica cada pieza para pedir la correcta. La vida útil es el número de horas de funcionamiento que se espera que dure una pieza antes de reponerla. El stock es la cantidad de repuestos en bodega. Una pieza original es la que indica el fabricante en su manual; otra pieza que no está en el manual puede no calzar ni resistir.",
        "Para reponer una pieza se necesita una orden de trabajo que registre el código, la hora del horómetro y quién la hizo. El plazo de entrega es el tiempo entre pedir un repuesto y recibirlo, y obliga a pedir con anticipación. Un ejemplo con otro equipo: una pieza con vida útil de 1.500 horas se repone 2 veces en 3.000 horas. El código erróneo en un pedido puede traer una pieza distinta de la necesaria.",
        f"Las piezas las repone personal autorizado; la persona en formación lee la lista y registra. {EMER} {AVISO}",
    ],
    vocab=[("lista de piezas", "documento del fabricante que enumera las piezas de un equipo con su código"), ("código de pieza", "identificador de cada pieza para pedir la correcta"), ("vida útil", "horas de funcionamiento que se espera que dure una pieza"), ("stock", "cantidad de repuestos en bodega"), ("pieza original", "la que indica el fabricante en su manual"), ("plazo de entrega", "tiempo entre pedir un repuesto y recibirlo")],
    worked=[
        ("Reposiciones por horas", "Una pieza de ejemplo tiene vida útil de 1.500 horas. ¿Cuántas reposiciones hay en 4.500 horas?", ["Se divide el total de horas entre la vida útil.", "4.500 ÷ 1.500."], "3 reposiciones"),
        ("Leer un código", "Una lista de ejemplo dice «P-210: válvula, stock 2». ¿Qué pieza es y cuántas hay en bodega?", ["El código P-210 identifica la pieza.", "El stock dice cuántas hay."], "Una válvula; hay 2 en bodega"),
    ],
    mistakes=[("Pedir una pieza solo por su nombre, sin el código.", "Varias piezas pueden tener nombres parecidos.", "Usa siempre el código de la lista de piezas."),
              ("Alargar la vida útil de una pieza para ahorrar.", "La vida útil la define el fabricante y no se cambia por ahorro.", "Respeta la vida útil y repón según el plan.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es la vida útil de una pieza?", "Las horas de funcionamiento que se espera que dure antes de reponerla", "El tiempo que tarda en llegar desde la bodega", "El precio que costó cuando era nueva", "La vida útil es una duración esperada en horas de funcionamiento."),
        ("abc", "En Tripulación de Naves: ¿para qué sirve el código de una pieza?", "Para identificar y pedir la pieza correcta", "Para saber cuánto pesa la pieza", "Para decidir cuándo se hace el relevo", "El código identifica exactamente la pieza que se necesita."),
        ("abc", "{F} ¿Cuál pieza de la ficha tiene la mayor vida útil?", "P-102, el rodamiento, con 4.000 horas", "P-103, la manguera, con 3.000 horas", "P-104, el filtro, con 1.000 horas", "La mayor vida útil de la lista es la de P-102."),
        ("=", "{F} ¿Cuántas piezas hay en bodega sumando el stock de las cuatro piezas?", "3+1+5+6", "Se suman los stocks de P-101, P-102, P-103 y P-104.", " piezas"),
        ("abc", "{F} ¿Cuál pieza de la ficha tiene el stock más bajo?", "P-102, con 1 en bodega", "P-101, con 3 en bodega", "P-104, con 6 en bodega", "P-102 tiene solo 1 unidad en bodega."),
        ("abc", "{F} Se pide un sello hidráulico usando el código P-102. ¿Qué ocurre?", "Llegaría un rodamiento y no el sello, porque el código es de otra pieza", "Llegaría el sello correcto, porque el nombre manda", "Llegaría la manguera de P-103", "El código identifica la pieza: P-102 es el rodamiento."),
        ("=", "{F} ¿Cuántas reposiciones del filtro P-104 corresponden en 4.000 horas de funcionamiento?", "4000//1000", "Se divide el total de horas entre la vida útil.", " reposiciones"),
        ("=", "{F} ¿Cuántas reposiciones del sello P-101 corresponden en 6.000 horas de funcionamiento?", "6000//2000", "Se divide el total de horas entre la vida útil.", " reposiciones"),
        ("abc", "{F} ¿Alcanza el stock del sello P-101 para 8.000 horas de funcionamiento?", "No, porque se necesitan 4 y hay 3", "Sí, porque hay 3 en bodega", "Sí, porque el stock mínimo siempre alcanza", "8.000 horas piden 4 sellos y hay 3: faltaría 1."),
        ("abc", "{F} Un compañero dice: «el filtro P-104 dura 1.000 horas, pero lo alargamos a 2.000 para ahorrar». ¿Qué respuesta es correcta?", "Es falso: la vida útil la fija el fabricante y se repone según el plan", "Es cierto, porque ahorrar es lo más importante", "Es cierto, si el filtro se ve limpio", "La vida útil no se alarga por ahorro; puede haber riesgo de falla."),
        ("abc", "{F} Un instructor de ejemplo sugiere reemplazar el sello por otra pieza «parecida» que no figura en la lista. ¿Qué corresponde?", "No usarla: debe ser la pieza que indica el manual del fabricante", "Usarla, porque es más barata", "Usarla, si se anota en la orden de trabajo", "La pieza debe ser la indicada por el fabricante; una parecida puede no calzar ni resistir."),
        ("=", "{F} Si la grúa funciona 8 horas al día, ¿cuántos días pasan hasta que el rodamiento P-102 completa su vida útil?", "4000//8", "Se divide la vida útil entre las horas de funcionamiento por día.", " días"),
        ("abc", "{F} La orden de trabajo para reponer una pieza trae el código de otra pieza. ¿Qué corresponde?", "Devolverla a quien la emitió para corregir el código antes del pedido", "Pedir la pieza igual y esperar a ver qué llega", "Cambiar el código a mano sin avisar", "Un código erróneo trae una pieza equivocada; se corrige en la orden."),
    ],
    ctx=("abc", "Al revisar la bodega de ejemplo notas que de P-102 queda 1 unidad y el plazo de entrega es largo. ¿Qué haces?", "Informar al responsable que el stock es bajo para que se pida con anticipación", "Esperar a que se agote", "Anotar que hay 3 para evitar problemas", "Informar un stock bajo permite pedir a tiempo; falsear el dato provoca faltantes."),
    sc=[
        ("En Tripulación de Naves: ¿qué es el stock?", "La cantidad de repuestos en bodega", "El stock es lo disponible en bodega."),
        ("¿Para qué sirve el código de pieza?", "Para pedir la pieza correcta", "El código evita confundir piezas parecidas."),
        ("¿Quién define la vida útil de una pieza?", "El fabricante", "La vida útil se indica en el manual del fabricante."),
    ],
    op=("Extracto de lista de piezas de ejemplo de un huinche: Q-11, correa, vida útil 1.500 horas, stock 2; Q-12, rodamiento, vida útil 3.000 horas, stock 1; Q-13, sello, vida útil 500 horas, stock 8. Escribe (a) cuántas reposiciones de Q-13 hay en 3.000 horas, (b) si alcanza el stock de Q-13 para esas horas, (c) cuántas reposiciones de Q-11 hay en 4.500 horas y si alcanza el stock, (d) qué código usarías para pedir un rodamiento y por qué.",
        "(a) 3.000 ÷ 500 = 6 reposiciones. (b) Sí, hay 8. (c) 4.500 ÷ 1.500 = 3 reposiciones; no alcanza, porque hay 2. (d) Q-12, porque el código identifica la pieza correcta y no basta el nombre.",
        ["calcula las reposiciones de Q-13", "verifica el stock", "calcula y verifica Q-11", "usa el código para pedir"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "no comparar con el stock", "pedir por el nombre"],
        "Pregunta: «¿cuántas veces cabe la vida útil en las horas totales?». Si no responde, pídele que escriba la división."),
    reinforce="Inventa una lista de tres piezas con código, vida útil y stock, y calcula las reposiciones en 6.000 horas.",
    extend="Explica por qué no se repone una pieza con un repuesto que no figura en el manual del fabricante.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (hoja de vida de ejemplo). Horas usadas desde la última reposición, vida útil y stock. P-101: sello, 1.900 horas usadas, vida útil 2.000 horas, stock 3. P-102: rodamiento, 2.000 horas, vida útil 4.000, stock 1. "
     "P-103: manguera, 2.800 horas, vida útil 3.000, stock 5. P-104: filtro, 500 horas, vida útil 1.000, stock 6. Regla de ejemplo de la planilla: se programa reponer una pieza cuando sus horas usadas llegan al 90 % de su vida útil.")
build(
    O7, 3, F,
    use="Aprenderé a leer una hoja de vida de piezas, a aplicar una regla de ejemplo para programar reposiciones y a informar lo que corresponde.",
    prior=["Sé qué es la vida útil y el stock.", "Sé calcular un porcentaje simple.", "Sé restar números enteros."],
    explain=[
        "En una hoja de vida de piezas se anotan las horas usadas de cada una desde su última reposición. Con una regla de la planilla se decide cuándo programar la reposición: por ejemplo, cuando las horas usadas llegan al 90 % de la vida útil. El límite de la regla es vida útil × porcentaje ÷ 100. Si las horas usadas son iguales o mayores que el límite, la pieza se programa para reponer; si no, falta tiempo. También se revisa el stock para saber si hay repuesto.",
        "Un ejemplo con otra pieza: vida útil 1.000 horas, regla del 80 %, límite 800 horas. Con 750 horas usadas, faltan 50 horas para el límite; con 820 horas usadas, ya se debe programar la reposición. La planilla solo programa y avisa; reponer la pieza lo hace personal autorizado y se registra en una orden de trabajo.",
        f"El porcentaje de esta clase es solo de ejemplo; los reales los fija el fabricante. {EMER} {AVISO}",
    ],
    vocab=[("hoja de vida de piezas", "registro de horas usadas de cada pieza desde su última reposición"), ("límite de la regla", "vida útil por el porcentaje de la regla, dividido por 100"), ("programar una reposición", "dejar planificado que una pieza se debe reponer"), ("horas usadas", "horas de funcionamiento desde la última reposición"), ("stock disponible", "repuestos que hay en bodega")],
    worked=[
        ("Calcular un límite", "Una pieza de ejemplo tiene vida útil de 1.200 horas y la regla es 75 %. ¿Cuál es el límite?", ["Límite = vida útil × porcentaje ÷ 100.", "1.200 × 75 ÷ 100."], "900 horas"),
        ("Decidir", "Esa pieza tiene 950 horas usadas. ¿Se programa la reposición?", ["El límite es 900 horas.", "950 supera 900."], "Sí, se programa la reposición"),
    ],
    mistakes=[("Esperar a que las horas usadas lleguen a la vida útil completa.", "La regla programa antes, para que haya tiempo y repuesto.", "Compara con el límite de la regla, no con la vida útil."),
              ("Programar la reposición sin revisar el stock.", "Sin repuesto en bodega la reposición no se puede hacer.", "Revisa el stock y pide con anticipación.")],
    T=[
        ("=", "{F} ¿Cuál es el límite de la regla para el sello P-101?", "2000*90//100", "Se calcula el 90 % de la vida útil del sello.", " horas"),
        ("abc", "{F} ¿Se programa la reposición del sello P-101?", "Sí, porque 1.900 horas superan el límite de 1.800", "No, porque 1.900 es menor que 2.000", "No, porque hay 3 en stock", "La regla compara con 1.800 horas y no con la vida útil completa."),
        ("=", "{F} ¿Cuántas horas faltan para que el sello P-101 llegue a su vida útil completa?", "2000-1900", "Se resta las horas usadas a la vida útil.", " horas"),
        ("=", "{F} ¿Cuál es el límite de la regla para la manguera P-103?", "3000*90//100", "Se calcula el 90 % de la vida útil de la manguera.", " horas"),
        ("abc", "{F} ¿Se programa la reposición de la manguera P-103?", "Sí, porque 2.800 horas superan el límite de 2.700", "No, porque 2.800 es menor que 3.000", "No, porque hay 5 en stock", "2.800 horas están por encima del límite de 2.700."),
        ("abc", "{F} ¿Se programa la reposición del rodamiento P-102?", "No, porque 2.000 horas están bajo el límite de 3.600", "Sí, porque tiene solo 1 en stock", "Sí, porque 2.000 horas es la mitad de la vida útil", "El límite es 3.600 horas; 2.000 no lo alcanza."),
        ("=", "{F} ¿Cuál es el límite de la regla para el rodamiento P-102?", "4000*90//100", "Se calcula el 90 % de la vida útil del rodamiento.", " horas"),
        ("=", "{F} ¿Cuántas horas faltan para que el filtro P-104 llegue al límite de la regla?", "1000*90//100-500", "Se calcula el límite del filtro y se resta las horas usadas.", " horas"),
        ("abc", "{F} ¿Cuántas piezas de la ficha deben programarse para reponer?", "Dos: el sello P-101 y la manguera P-103", "Una: solo el sello P-101", "Las cuatro, porque todas tienen horas usadas", "Solo P-101 y P-103 superan el límite de su regla."),
        ("abc", "{F} Un compañero dice que el sello P-101 puede esperar porque aún no cumple su vida útil. ¿Qué respuesta es correcta?", "Es falso: la regla programa antes, al llegar al límite del 90 %", "Es cierto, porque la vida útil manda", "Es cierto, si el stock es alto", "La regla del 90 % programa la reposición antes de la vida útil completa."),
        ("abc", "{F} ¿Cuál es el informe correcto sobre el sello P-101 al oficial de máquinas?", "«El sello P-101 lleva 1.900 horas, sobre el límite de 1.800; stock 3; se programa la reposición»", "«El sello está viejo»", "«Cambié el sello P-101»", "El informe completo da horas, límite, stock y estado."),
        ("=", "{F} Si el filtro P-104 trabaja 20 horas por semana desde las 500 horas, ¿en cuántas semanas llegará a su límite?", "(1000*90//100-500)//20", "Se calculan las horas que faltan y se dividen entre las horas semanales.", " semanas"),
        ("abc", "{F} ¿Hay stock para reponer las dos piezas que superan el límite?", "Sí, porque hay 3 sellos P-101 y 5 mangueras P-103", "No, porque hay solo 1 rodamiento", "No, porque falta el filtro P-104", "Las dos piezas por reponer tienen stock en bodega."),
    ],
    ctx=("abc", "Una persona de ejemplo te dice: «anota 1.700 horas en el sello P-101 para que no figure en la lista de reposición». ¿Qué respondes?", "Que se anotan las horas reales e informas que se debe programar la reposición", "Que sí, porque ella manda", "Que sí, pero solo por esta semana", "Falsear las horas puede dejar una pieza gastada en uso."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calcula el límite de la regla?", "Vida útil por el porcentaje de la regla, dividido por 100", "Así se obtiene el momento de programar la reposición."),
        ("¿Qué se revisa además de las horas usadas?", "El stock de repuestos", "Sin repuesto no se puede reponer."),
        ("¿Quién repone la pieza?", "Personal autorizado", "La planilla solo programa y avisa."),
    ],
    op=("Hoja de vida de ejemplo: R-1, correa, 1.600 horas usadas, vida útil 2.000, stock 2; R-2, rodamiento, 700 horas usadas, vida útil 3.000, stock 0. Regla de ejemplo: se programa la reposición al llegar al 80 % de la vida útil. Escribe (a) el límite de cada pieza, (b) cuál se programa para reponer, (c) qué problema hay con el stock de R-2 y qué informarías, (d) quién hace la reposición.",
        "(a) R-1: 2.000 × 80 ÷ 100 = 1.600 horas. R-2: 3.000 × 80 ÷ 100 = 2.400 horas. (b) R-1, porque sus 1.600 horas alcanzan el límite. (c) No hay stock de R-2; aunque aún no toca, se informa para pedirlo con anticipación. (d) Personal autorizado.",
        ["calcula los límites", "decide cuál se programa", "detecta el problema de stock", "indica quién repone"],
        ["hoja con las cuatro respuestas"],
        ["comparar con la vida útil completa", "olvidar el stock", "decir que la persona en formación repone"],
        "Pregunta: «¿cuál es el límite de cada pieza?». Si no responde, pídele que calcule el 80 % de cada vida útil."),
    reinforce="Inventa una hoja de vida con tres piezas y marca cuáles se programan con una regla del 85 %.",
    extend="Explica por qué se programa la reposición antes de que la pieza llegue a su vida útil completa.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (precios y plazos de ejemplo). Una pieza X cuesta $35.000 y tiene vida útil de 2.000 horas; el equipo funciona 4.000 horas al año. Stock en bodega: 3 piezas; stock mínimo: 2 piezas. "
     "Plazo de entrega de ejemplo: 30 días. Cada reposición deja 5 litros de aceite hidráulico usado, que se guardan en envases rotulados de 10 litros.")
build(
    O7, 4, F,
    use="Aprenderé a calcular reposiciones, costos y residuos de una pieza durante un año, y a decidir cuándo pedir más repuestos.",
    prior=["Sé qué es la vida útil, el stock y el plazo de entrega.", "Sé multiplicar y dividir números enteros.", "Sé qué es un residuo."],
    explain=[
        "Con la vida útil y las horas de funcionamiento al año se calcula cuántas reposiciones hay: reposiciones = horas del año ÷ vida útil. Con eso se calculan los repuestos, el costo anual, multiplicando las reposiciones por el precio, y el residuo, multiplicando las reposiciones por los litros de cada una. El stock mínimo es la cantidad bajo la cual hay que pedir más; el plazo de entrega obliga a pedir antes de llegar a ese mínimo.",
        "Un ejemplo con otra pieza: vida útil 1.000 horas, 3.000 horas al año, precio $20.000, stock 5 y mínimo 2. Son 3 reposiciones, un costo de $60.000, y el stock baja a 2 al final del año, por lo que habría que pedir antes. Comprar muchas piezas de una vez ocupa espacio y dinero y puede dejar piezas deterioradas en bodega.",
        f"Estos cálculos planifican compras y registros; la reposición física la hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("reposiciones al año", "horas de funcionamiento del año divididas entre la vida útil"), ("costo anual", "reposiciones del año por el precio de la pieza"), ("stock mínimo", "cantidad bajo la cual hay que pedir más"), ("plazo de entrega", "tiempo entre pedir un repuesto y recibirlo"), ("residuo", "material usado que se maneja según la norma vigente")],
    worked=[
        ("Costo anual", "Una pieza de ejemplo se repone 3 veces al año y cuesta $12.000. ¿Cuánto cuesta al año?", ["Se multiplican las reposiciones por el precio.", "3 × $12.000."], "$36.000"),
        ("Stock restante", "Hay 5 piezas y se usan 3 en el año. ¿Cuántas quedan?", ["Se restan las piezas usadas al stock.", "5 − 3."], "2 piezas"),
    ],
    mistakes=[("Pedir solo cuando el stock llega a cero.", "El plazo de entrega puede dejar la bodega vacía antes de que llegue el pedido.", "Pide cuando el stock llega al mínimo."),
              ("Comprar muchas piezas de una vez «por si acaso».", "Ocupa espacio y dinero y las piezas pueden deteriorarse.", "Compra según el plan y el stock mínimo.")],
    T=[
        ("=", "{F} ¿Cuántas reposiciones de la pieza X hay en un año?", "4000//2000", "Se divide las horas del año entre la vida útil.", " reposiciones"),
        ("=", "{F} ¿Cuánto cuestan al año las reposiciones de la pieza X?", "(4000//2000)*35000", "Se multiplican las reposiciones del año por el precio de la pieza.", " pesos"),
        ("abc", "En Tripulación de Naves: ¿cuándo conviene pedir más repuestos?", "Cuando el stock llega al mínimo, para que llegue antes de agotarse", "Solo cuando el stock llega a cero", "Cuando sobra espacio en la bodega", "El stock mínimo es la señal de pedido anticipado."),
        ("=", "{F} ¿Cuántas piezas quedan en la bodega después de las reposiciones del año?", "3-(4000//2000)", "Se restan las piezas usadas al stock.", " piezas"),
        ("abc", "{F} Al final del año, ¿qué situación tiene el stock respecto del stock mínimo?", "Queda bajo el mínimo, porque 1 es menor que 2, y hay que pedir", "Queda sobre el mínimo, porque 1 es menor que 3", "Queda igual que el mínimo", "Con 1 pieza se está por debajo del mínimo de 2."),
        ("=", "{F} ¿Cuántos litros de aceite usado dejan las reposiciones del año?", "(4000//2000)*5", "Se multiplican las reposiciones del año por los litros de cada una.", " litros"),
        ("=", "{F} ¿Cuántos envases de 10 litros se llenan con el aceite usado del año?", "((4000//2000)*5)//10", "Se dividen los litros de residuo entre la capacidad de cada envase.", " envases"),
        ("=", "{F} ¿Cuánto cuestan las reposiciones de 3 años?", "(4000//2000)*3*35000", "Se multiplican las reposiciones por los años y por el precio.", " pesos"),
        ("abc", "{F} ¿Por qué se pide antes de que el stock llegue a cero?", "Porque el plazo de entrega es de 30 días y la bodega podría quedar vacía", "Porque las piezas se venden más baratas si se piden antes", "Porque el stock mínimo no se puede alcanzar", "El plazo de entrega obliga a pedir con anticipación."),
        ("=", "{F} ¿Cada cuántos meses se repone la pieza X, si el equipo funciona la misma cantidad de horas cada mes?", "12*2000//4000", "Se calcula la fracción del año en que se completa la vida útil y se pasa a meses.", " meses"),
        ("abc", "{F} Un compañero propone comprar 20 piezas de una vez para no preocuparse. ¿Qué argumento va en contra?", "Ocupa espacio y dinero, y las piezas pueden deteriorarse en bodega", "Las piezas no se pueden comprar de a muchas", "El stock mínimo prohíbe comprar más de 3", "Un exceso de stock inmoviliza recursos y puede deteriorarse."),
        ("=", "{F} Si el precio de la pieza sube a $42.000, ¿cuántos pesos más se pagan al año?", "(42000-35000)*(4000//2000)", "Se multiplica el aumento de precio por las reposiciones del año.", " pesos"),
        ("abc", "{F} Una persona nota que el stock bajó al mínimo y no hay pedido en curso. ¿Qué corresponde?", "Informar al responsable para que se haga el pedido", "Esperar a que llegue a cero", "Pedirlo por su cuenta sin avisar", "Informar permite que quien está autorizado haga el pedido a tiempo."),
    ],
    ctx=("abc", "En la planilla de ejemplo notas que el costo anual calculado no coincide con el de un compañero. ¿Qué corresponde?", "Revisar juntos las reposiciones y el precio, y corregir el error", "Aceptar el valor del compañero sin revisarlo", "Anotar un valor intermedio para quedar de acuerdo", "Un cálculo se resuelve revisando los datos, no por acuerdo."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calculan las reposiciones del año?", "Horas del año divididas entre la vida útil", "Así se sabe cuántas veces se repone la pieza."),
        ("¿Qué es el stock mínimo?", "La cantidad bajo la cual hay que pedir más", "Avisa antes de quedarse sin repuestos."),
        ("¿Por qué se calculan los residuos?", "Para tener envases y registros suficientes", "El residuo se entrega según la norma vigente."),
    ],
    op=("Planilla de ejemplo: una pieza cuesta $15.000, vida útil 1.500 horas; el equipo funciona 4.500 horas al año; stock 4; mínimo 2; cada reposición deja 4 litros de residuo. Escribe (a) cuántas reposiciones hay al año, (b) el costo anual, (c) cuántas piezas quedan en bodega y si hay que pedir, (d) cuántos litros de residuo se generan.",
        "(a) 4.500 ÷ 1.500 = 3 reposiciones. (b) 3 × $15.000 = $45.000. (c) 4 − 3 = 1 pieza, bajo el mínimo de 2: hay que pedir. (d) 3 × 4 = 12 litros.",
        ["calcula las reposiciones", "calcula el costo", "compara el stock con el mínimo", "calcula el residuo"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "olvidar el stock mínimo", "olvidar los residuos"],
        "Pregunta: «¿cuántas reposiciones hay al año?». Si no responde, pídele que escriba la división de horas."),
    reinforce="Inventa una pieza con precio y vida útil y calcula el costo de reponerla durante 2 años.",
    extend="Explica qué pasa con el plazo de entrega si la bodega queda sin repuesto justo antes de una reposición.",
)

# ============================================================ OAE-07, clase 5
F = ("Ficha 5 (opciones de ejemplo; costos de ejemplo). Opción 1: reponer con una pieza original nueva, $80.000, dura 4.000 horas. Opción 2: reparar la pieza usada (el manual la admite), $30.000, dura 1.000 horas. "
     "Opción 3: reponer con una pieza genérica que no está en el manual, $50.000, dura 4.000 horas. Criterio obligatorio: el trabajo debe estar admitido por el manual del fabricante. Criterio de elección: menor costo por cada 1.000 horas de uso.")
build(
    O7, 5, F,
    use="Aprenderé a comparar reponer y reparar con criterios, a calcular el costo por horas de uso y a verificar la calidad de un registro.",
    prior=["Sé qué es reponer y reparar.", "Sé qué es el criterio obligatorio.", "Sé dividir números enteros."],
    explain=[
        "Para decidir entre reponer y reparar se comparan opciones con criterios. Primero se aplica el criterio obligatorio: las opciones que no están admitidas por el manual del fabricante se descartan. Luego, entre las que quedan, se elige la de menor costo por cada 1.000 horas de uso. Ese costo se calcula dividiendo el precio entre las horas que dura y multiplicando por 1.000, o, más simple, dividiendo el precio entre los miles de horas de duración.",
        "Un ejemplo con otras opciones: una pieza nueva de $60.000 que dura 3.000 horas cuesta $20.000 por cada 1.000 horas; una reparación de $15.000 que dura 500 horas cuesta $30.000 por 1.000 horas. Verificar la calidad es comprobar que la orden de trabajo diga qué pieza se usó, con su código, y que coincida con la opción elegida.",
        f"La decisión final es del jefe de máquinas; la persona en formación calcula e informa. {EMER} {AVISO}",
    ],
    vocab=[("opción", "una de las alternativas entre las que se elige"), ("costo por 1.000 horas", "precio de la opción dividido entre los miles de horas que dura"), ("admitido por el manual", "indicado o permitido por el fabricante"), ("pieza genérica", "pieza que no es la indicada por el fabricante"), ("verificar la calidad", "comprobar que el registro coincide con lo decidido")],
    worked=[
        ("Costo por 1.000 horas", "Una pieza de ejemplo cuesta $60.000 y dura 3.000 horas. ¿Cuánto cuesta por cada 1.000 horas?", ["3.000 horas son 3 miles de horas.", "Se divide $60.000 entre 3."], "$20.000"),
        ("Descartar una opción", "Una opción de ejemplo es muy barata, pero no está admitida por el manual. ¿Se elige?", ["El criterio obligatorio es que el manual la admita.", "Una opción que no lo cumple se descarta."], "No, se descarta"),
    ],
    mistakes=[("Elegir la opción más barata sin revisar si el manual la admite.", "El criterio obligatorio va primero.", "Aplica primero el criterio obligatorio."),
              ("Comparar solo el precio y no cuánto dura.", "Una pieza barata que dura poco puede costar más por hora.", "Compara el costo por 1.000 horas de uso.")],
    T=[
        ("=", "{F} ¿Cuánto cuesta por cada 1.000 horas de uso la opción 1?", "80000//4", "Se divide el precio entre los 4 miles de horas que dura.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta por cada 1.000 horas de uso la opción 2?", "30000//1", "Se divide el precio entre el 1 mil de horas que dura.", " pesos"),
        ("abc", "{F} ¿Cumple la opción 3 con el criterio obligatorio?", "No, porque la pieza genérica no está en el manual del fabricante", "Sí, porque dura lo mismo que la opción 1", "Sí, porque es más barata que la opción 1", "El criterio obligatorio pide que el manual la admita, y la opción 3 no lo cumple."),
        ("=", "{F} ¿Cuánto costaría por cada 1.000 horas la opción 3, aunque no cumpla el criterio?", "50000//4", "Se divide el precio entre los 4 miles de horas que dura.", " pesos"),
        ("abc", "{F} ¿Qué opción se elige según los criterios?", "La opción 1, porque cumple el criterio y tiene menor costo por 1.000 horas que la 2", "La opción 3, porque es la más barata por 1.000 horas", "La opción 2, porque cuesta menos en precio", "La opción 3 se descarta y entre la 1 y la 2 gana la de menor costo por 1.000 horas."),
        ("abc", "{F} ¿Por qué no se elige la opción 3 aunque sea más barata por 1.000 horas?", "Porque no cumple el criterio obligatorio del manual del fabricante", "Porque dura menos que la opción 1", "Porque cuesta más que la opción 2", "El criterio obligatorio se aplica antes del costo."),
        ("=", "{F} ¿Cuánto más cuesta por 1.000 horas la opción 2 que la opción 1?", "30000-80000//4", "Se resta el costo por 1.000 horas de la opción 1 al de la opción 2.", " pesos"),
        ("=", "{F} Para 8.000 horas de uso, ¿cuánto costaría la opción 1?", "(8000//4000)*80000", "Se calculan las piezas nuevas necesarias y se multiplican por el precio.", " pesos"),
        ("=", "{F} Para 8.000 horas de uso, ¿cuánto costaría la opción 2?", "(8000//1000)*30000", "Se calculan las reparaciones necesarias y se multiplican por el precio.", " pesos"),
        ("abc", "{F} Una orden de trabajo de la opción 1 dice «pieza genérica». ¿Qué corresponde?", "Devolverla para aclarar, porque no coincide con la opción elegida", "Archivarla, porque dice una pieza", "Corregirla a mano sin avisar", "La orden debe decir la pieza original elegida; si no coincide, se aclara con quien la hizo."),
        ("abc", "{F} Un compañero dice: «elijamos la opción 3, que es la más barata por hora». ¿Qué respuesta es correcta?", "Es falso: la opción 3 no cumple el criterio obligatorio y se descarta", "Es cierto, porque el menor costo manda", "Es cierto, si el oficial no se entera", "El criterio obligatorio del manual se aplica antes que el costo."),
        ("=", "{F} ¿Cuánto se ahorra en 8.000 horas de uso al elegir la opción 1 en vez de la opción 2?", "(8000//1000)*30000-(8000//4000)*80000", "Se resta el costo total de la opción 1 al de la opción 2.", " pesos"),
        ("abc", "{F} Si el manual no admitiera la reparación, ¿qué pasaría con la opción 2?", "Se descartaría, porque no cumpliría el criterio obligatorio", "Seguiría compitiendo por su menor precio", "Se elegiría igual si el oficial lo pide", "Lo que no está admitido por el manual se descarta."),
    ],
    ctx=("abc", "El jefe de máquinas de ejemplo te pide ayuda para decidir entre reponer y reparar. ¿Qué le presentas?", "Los costos por 1.000 horas de las opciones y cuáles están admitidas por el manual, para que decida", "Solo el precio más bajo", "Solo la opción que tú prefieres", "Una buena presentación muestra los datos y el criterio obligatorio."),
    sc=[
        ("En Tripulación de Naves: ¿qué se aplica primero al comparar opciones de reposición?", "El criterio obligatorio del manual", "Lo que no cumple se descarta."),
        ("¿Cómo se compara el costo entre opciones?", "Por cada 1.000 horas de uso", "Así se considera cuánto dura cada una."),
        ("¿Quién decide la opción final?", "El jefe de máquinas", "La persona en formación calcula e informa."),
    ],
    op=("Opciones de ejemplo: A, pieza original nueva, $120.000, dura 6.000 horas; B, reparar la pieza usada (el manual la admite), $24.000, dura 1.000 horas; C, pieza genérica que no está en el manual, $60.000, dura 6.000 horas. Criterio obligatorio: admitido por el manual. Criterio de elección: menor costo por 1.000 horas. Escribe (a) cuál se descarta y por qué, (b) el costo por 1.000 horas de A y de B, (c) cuál se elige, (d) qué datos debe tener la orden de trabajo de la opción elegida.",
        "(a) C, porque no está admitida por el manual. (b) A: $120.000 ÷ 6 = $20.000; B: $24.000 ÷ 1 = $24.000. (c) Se elige A, porque cumple el criterio obligatorio y cuesta menos por 1.000 horas. (d) Código de la pieza, hora del horómetro, quién la hizo y fecha.",
        ["aplica el criterio obligatorio", "calcula el costo por 1.000 horas", "elige según el criterio", "indica los datos de la orden"],
        ["hoja con las cuatro respuestas"],
        ["elegir C por precio", "no dividir por los miles de horas", "olvidar aplicar el criterio de elección"],
        "Pregunta: «¿cuántos miles de horas dura cada opción?». Si no responde, pídele que escriba la división."),
    reinforce="Inventa tres opciones de reposición con precio y duración y calcula el costo por 1.000 horas.",
    extend="Explica por qué una pieza barata que dura poco puede ser más cara a largo plazo.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Nave Demo» tiene 26 personas a bordo, 28 chalecos salvavidas, 3 balsas salvavidas con capacidad de ejemplo de 10 personas cada una y 12 extintores. "
     "Peligros anotados: agua fría, incendio y humo, escora peligrosa y mal tiempo.")
build(
    O8, 1, F,
    use="Aprenderé qué es una emergencia a bordo, cómo se organiza la seguridad de la vida humana en el mar y por qué la supervivencia se aprende solo con instructor autorizado.",
    prior=["Sé qué es la jerarquía de controles.", "Sé qué es una alarma y un punto de reunión.", "Sé multiplicar y restar números enteros."],
    explain=[
        "Una emergencia es una situación que pone en peligro vidas o la nave, como un incendio, una caída al agua o una escora peligrosa. La alarma general es la señal con que se avisa a toda la nave; su forma la fija la norma vigente. El cuadro de obligaciones es una lista que asigna a cada persona su función y su punto de reunión en una emergencia. El equipo de flotación, como el chaleco salvavidas, ayuda a mantenerse a flote. Los primeros auxilios son la ayuda inmediata que da una persona capacitada mientras llega ayuda profesional.",
        "El agua fría es un peligro porque puede causar hipotermia, que es un enfriamiento peligroso del cuerpo. Las técnicas de supervivencia, de primeros auxilios y de combate de incendios se aprenden con instructor autorizado, equipo de protección y práctica supervisada. Este cuaderno no enseña ninguna de esas técnicas ni el uso de botes, balsas o extintores. Un ejemplo con otra nave: un chaleco con una correa dañada se informa y se retira del uso, sin repararlo por cuenta propia.",
        f"La regla general es: no acercarse a la zona de riesgo ni entrar al agua, dar la alarma y avisar. {EMER} {AVISO}",
    ],
    vocab=[("emergencia", "situación que pone en peligro vidas o la nave"), ("alarma general", "señal que avisa a toda la nave, fijada por la norma vigente"), ("cuadro de obligaciones", "lista que asigna a cada persona su función y su punto de reunión"), ("equipo de flotación", "equipo que ayuda a mantenerse a flote, como el chaleco salvavidas"), ("hipotermia", "enfriamiento peligroso del cuerpo"), ("primeros auxilios", "ayuda inmediata de una persona capacitada mientras llega ayuda profesional")],
    worked=[
        ("Contar chalecos", "Una nave de ejemplo tiene 20 personas y 24 chalecos. ¿Cuántos chalecos sobran?", ["Se resta el número de personas a los chalecos.", "24 − 20."], "4 chalecos"),
        ("Clasificar una conducta", "En una nave de ejemplo se oye la alarma general. ¿Qué hace una persona en formación?", ["Cumplir una función del cuadro de obligaciones exige formación, y una persona en formación no la tiene.", "Por eso mantiene la calma, sigue las indicaciones de un adulto responsable y avisa; no actúa por su cuenta."], "Mantiene la calma, sigue las indicaciones de un adulto responsable y no actúa por su cuenta"),
    ],
    mistakes=[("Creer que tener un chaleco permite rescatar a otra persona del agua.", "El chaleco protege a quien lo lleva; el rescate exige formación y equipo.", "No entres al agua: da la alarma y avisa."),
              ("Creer que leer sobre supervivencia basta para actuar en una emergencia.", "Las técnicas se aprenden con instructor autorizado y práctica supervisada.", "Este cuaderno da conceptos; la práctica es con instructor.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es una emergencia?", "Una situación que pone en peligro vidas o la nave", "Una tarea del plan de mantenimiento", "Un cambio de guardia", "La emergencia es un peligro grave y no una tarea de rutina."),
        ("abc", "En Tripulación de Naves: ¿qué es el cuadro de obligaciones?", "Una lista que asigna a cada persona su función y su punto de reunión", "Un registro de las lecturas de instrumentos", "Un plan de compra de repuestos", "El cuadro asigna funciones y puntos de reunión para las emergencias."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al agua fría?", "La hipotermia, es decir, un enfriamiento peligroso del cuerpo", "Que los chalecos se mojen más rápido", "Que el equipo de máquinas consuma más", "El riesgo del agua fría es el enfriamiento peligroso de la persona."),
        ("=", "{F} ¿Cuántos chalecos sobran respecto del número de personas a bordo?", "28-26", "Se resta el número de personas al de chalecos.", " chalecos"),
        ("=", "{F} ¿Cuántas plazas hay en total en las balsas salvavidas de la ficha?", "3*10", "Se multiplican las balsas por la capacidad de cada una.", " plazas"),
        ("abc", "{F} Se declara un incendio. ¿Qué corresponde a una persona en formación?", "No acercarse a la zona de riesgo, dar la alarma y avisar a un adulto responsable y a emergencias", "Acercarse con un extintor para apagarlo", "Cerrar las puertas y esperar sola", "El combate de incendios exige formación y equipo; la conducta general es dar la alarma y avisar."),
        ("=", "{F} ¿Cuántas plazas libres quedan en las balsas, si las 26 personas ocuparan una plaza cada una?", "30-26", "Se resta el número de personas a las plazas de las balsas.", " plazas"),
        ("=", "{F} Si los 12 extintores se reparten por igual en 4 zonas de la nave, ¿cuántos extintores hay en cada zona?", "12//4", "Se divide el número de extintores entre las zonas.", " extintores"),
        ("abc", "En una nave de ejemplo, ¿qué control es el más efectivo contra el peligro de incendio de un trapo con aceite?", "Guardar el trapo en un recipiente cerrado para residuos y lejos de fuentes de calor", "Poner un letrero que diga «peligro de incendio»", "Entregar guantes a cada persona", "Guardarlo correctamente evita el peligro; el letrero y los guantes no lo quitan."),
        ("abc", "Durante una visita de ejemplo, una persona cae al agua desde la pasarela de una nave. ¿Qué corresponde?", "No acercarte a la zona de riesgo ni entrar al agua, dar la alarma y avisar a un adulto responsable y a emergencias", "Lanzarte al agua con tu chaleco para ayudarla", "Acercarte al borde para estirarle un cabo", "Un chaleco no autoriza a intervenir; entrar al agua o acercarse puede causar otro accidente."),
        ("abc", "{F} Un compañero dice que, con chaleco puesto, puede lanzarse al agua a rescatar a alguien. ¿Qué respuesta es correcta?", "Es falso: el chaleco protege a quien lo lleva y el rescate exige formación y equipo", "Es cierto, porque el chaleco permite rescatar a cualquiera", "Es cierto, si la persona está cerca", "El chaleco no sustituye la formación en rescate."),
        ("=", "{F} Si 6 de las 26 personas ya llegaron a su punto de reunión, ¿cuántas faltan por llegar?", "26-6", "Se restan las personas que llegaron al total.", " personas"),
        ("abc", "En Tripulación de Naves: ¿por qué las técnicas de supervivencia se practican con instructor autorizado?", "Porque requieren formación, equipo y práctica supervisada para no ponerse en riesgo", "Porque se aprenden mejor con una guía escrita", "Porque no hay peligro si se practica solo", "Practicar sin instructor puede causar accidentes; la supervisión protege."),
    ],
    ctx=("abc", "Un conocido que trabaja en un buque te propone enseñarte a usar una balsa salvavidas durante una visita, «porque es fácil». ¿Qué respondes?", "Que no, porque esa práctica exige instructor autorizado, norma vigente y elementos de protección, incluido equipo de flotación, y que lo hablarás con un adulto responsable", "Que sí, si te pones un chaleco", "Que sí, si el mar está calmo", "Un chaleco o un mar calmo no reemplazan la formación ni la autorización."),
    sc=[
        ("En Tripulación de Naves: ¿qué es la alarma general?", "La señal que avisa a toda la nave de una emergencia", "La alarma general activa el cuadro de obligaciones."),
        ("¿Qué es la hipotermia?", "Un enfriamiento peligroso del cuerpo", "El agua fría puede causar hipotermia en una persona."),
        ("¿Qué hace una persona en formación ante un incendio?", "No se acerca, da la alarma y avisa", "El combate de incendios lo hace personal capacitado."),
    ],
    op=("En la «Nave Ejemplo» (caso de ejemplo) hay 22 personas a bordo, 24 chalecos y 2 balsas de 12 plazas cada una. Peligros anotados: agua fría y humo. Escribe (a) cuántos chalecos sobran, (b) cuántas plazas hay en las balsas y si alcanzan para todas las personas, (c) el riesgo del agua fría, (d) qué hace una persona en formación si ve humo en un pasillo.",
        "(a) 24 − 22 = 2 chalecos. (b) 2 × 12 = 24 plazas, que alcanzan para las 22 personas. (c) La hipotermia. (d) No se acerca al humo, da la alarma y avisa a un adulto responsable y a emergencias.",
        ["calcula los chalecos que sobran", "calcula las plazas y compara", "identifica el riesgo del agua fría", "indica la conducta ante el humo"],
        ["hoja con las cuatro respuestas"],
        ["no comparar plazas con personas", "proponer apagar el fuego", "proponer entrar al agua"],
        "Pregunta: «¿qué hace una persona sin formación ante una emergencia?». Si no responde, pídele que relea la última parte de la explicación."),
    reinforce="Escribe tres emergencias posibles a bordo y, para cada una, la regla general de conducta.",
    extend="Explica por qué un cuadro de obligaciones debe conocerse antes de que ocurra una emergencia.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (inspección de ejemplo). Extintor E1: última revisión hace 11 meses; extintor E2: última revisión hace 13 meses. Chalecos: 28, todos con la cinta reflectante visible. "
     "Botiquín: contenido completo salvo 2 apósitos que faltan. Regla de ejemplo de la planilla: cada extintor se revisa cada 12 meses.")
build(
    O8, 2, F,
    use="Aprenderé qué son los equipos de seguridad y de emergencia, qué dice el triángulo del fuego, y cómo se leen y se informan las inspecciones.",
    prior=["Sé qué es una emergencia y un cuadro de obligaciones.", "Sé qué significa «vencido» en un plan.", "Sé restar números enteros."],
    explain=[
        "El extintor es un equipo portátil con un agente para apagar fuegos pequeños, y lo usa solo personal capacitado. El botiquín es una caja con insumos de primeros auxilios. Las vías de escape son los caminos señalizados para salir de un lugar. Los equipos de seguridad se revisan con una frecuencia fijada por el plan y la norma vigente, y cada revisión se anota. Una inspección vencida es la que pasó el plazo sin hacerse.",
        "El triángulo del fuego dice que, para que haya fuego, deben juntarse tres elementos: combustible (lo que arde), calor (una fuente de temperatura alta) y oxígeno. La prevención busca que no se junten: por ejemplo, un trapo con aceite (combustible) no se guarda cerca de una fuente de calor. Un ejemplo con otra nave: una caja de cartón junto a una estufa junta combustible y calor. Este cuaderno no enseña a apagar fuegos.",
        f"Si un equipo está vencido, dañado o incompleto, se informa y se registra. {EMER} {AVISO}",
    ],
    vocab=[("extintor", "equipo portátil con un agente para apagar fuegos pequeños, usado por personal capacitado"), ("botiquín", "caja con insumos de primeros auxilios"), ("vía de escape", "camino señalizado para salir de un lugar"), ("triángulo del fuego", "idea de que el fuego necesita combustible, calor y oxígeno juntos"), ("inspección vencida", "revisión cuyo plazo pasó sin haberse hecho")],
    worked=[
        ("Detectar una inspección vencida", "Un extintor de ejemplo se revisó hace 14 meses y la regla es cada 12 meses. ¿Está vencida su inspección?", ["14 meses supera los 12 de la regla.", "Se pasó por 2 meses."], "Sí, vencida por 2 meses"),
        ("Aplicar el triángulo del fuego", "Una caja de papel está junto a una lámpara que se calienta mucho. ¿Qué dos elementos del fuego se acercan?", ["El papel es combustible.", "La lámpara caliente aporta calor."], "Combustible y calor"),
    ],
    mistakes=[("Creer que cualquier persona puede usar un extintor sin formación.", "El extintor lo usa personal capacitado.", "Da la alarma y avisa; no combatas el fuego sin formación."),
              ("Dejar un equipo vencido sin informar porque «parece que funciona».", "La inspección vencida no garantiza el funcionamiento.", "Informa y registra la inspección vencida.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es un extintor?", "Un equipo portátil para apagar fuegos pequeños, usado por personal capacitado", "Un instrumento que mide la temperatura", "Un tipo de alarma sonora", "El extintor es un equipo de combate de incendios y no un instrumento ni una alarma."),
        ("abc", "En Tripulación de Naves: ¿qué dice el triángulo del fuego?", "Que el fuego necesita combustible, calor y oxígeno juntos", "Que el fuego solo ocurre en las máquinas", "Que el fuego depende solo del agua", "El triángulo del fuego nombra los tres elementos que deben juntarse."),
        ("abc", "{F} ¿Qué extintor de la ficha tiene la inspección vencida?", "E2, porque lleva 13 meses y la regla es 12", "E1, porque lleva 11 meses", "Ninguno, porque ambos funcionan", "E2 pasó el plazo de 12 meses de la regla."),
        ("=", "{F} ¿Por cuántos meses está vencida la inspección del extintor E2?", "13-12", "Se resta el plazo de la regla a los meses desde la última revisión.", " meses"),
        ("=", "{F} ¿Cuántos meses faltan para que venza la inspección del extintor E1?", "12-11", "Se resta los meses transcurridos al plazo de la regla.", " meses"),
        ("abc", "{F} ¿Qué se informa del botiquín de la ficha?", "Que faltan 2 apósitos, para que se repongan", "Que está completo", "Que debe cambiarse por completo", "El botiquín tiene dos faltantes que se informan y se reponen."),
        ("abc", "{F} Un trapo con aceite se guarda junto a una fuente de calor. ¿Qué elementos del fuego se están acercando?", "Combustible y calor", "Solo oxígeno", "Agua y calor", "El trapo con aceite es combustible y la fuente de calor aporta calor."),
        ("=", "{F} Si cada extintor se revisa cada 12 meses, ¿cuántas revisiones hace un mismo extintor en 3 años?", "36//12", "Se divide el período en meses entre la frecuencia de la regla.", " revisiones"),
        ("=", "{F} Si cada revisión de extintor tarda 10 minutos y hay 12 extintores, ¿cuántos minutos se necesitan para revisarlos todos?", "12*10", "Se multiplican los extintores por los minutos de cada revisión.", " minutos"),
        ("abc", "En la sala de ejemplo una persona ve una llama pequeña en un tacho de basura. ¿Qué corresponde a una persona en formación?", "No acercarse, dar la alarma y avisar a un adulto responsable y a emergencias", "Acercarse y apagarla con un extintor", "Arrojar agua sobre el tacho", "Combatir un fuego exige formación; la conducta general es dar la alarma y avisar."),
        ("abc", "{F} Un compañero dice que puede usar el extintor E2 vencido «porque seguro funciona». ¿Qué respuesta es correcta?", "Es falso: un equipo vencido se informa y solo personal capacitado decide su uso", "Es cierto, si se ve en buen estado", "Es cierto, si el fuego es pequeño", "La inspección vencida no garantiza el funcionamiento."),
        ("abc", "{F} ¿Cuál es el informe correcto de la inspección del extintor E2?", "«Extintor E2, inspección vencida por 1 mes; se solicita su revisión»", "«El extintor está bien»", "«Revisé el extintor E2 por mi cuenta»", "El informe correcto indica el equipo, el estado y la acción solicitada."),
        ("abc", "En Tripulación de Naves: ¿por qué se rotulan las vías de escape?", "Para que cualquier persona las reconozca y salga con rapidez", "Para decorar los pasillos", "Para que solo el personal las use", "Las vías de escape se señalizan para evacuar con claridad."),
    ],
    ctx=("abc", "En una visita de ejemplo ves que un extintor está tapado por cajas. La persona a cargo dice: «déjalo, ya lo saben». ¿Qué corresponde?", "Informar al oficial a cargo para que el extintor quede visible y accesible", "Dejarlo tapado", "Retirar el extintor para ordenar", "Un extintor tapado no se puede encontrar en una emergencia."),
    sc=[
        ("En Tripulación de Naves: ¿qué elementos necesita el fuego?", "Combustible, calor y oxígeno", "Esos son los tres elementos del triángulo del fuego."),
        ("¿Qué se hace con una inspección vencida?", "Se informa y se registra", "La inspección vencida se corrige con una revisión."),
        ("¿Quién usa un extintor?", "Personal capacitado", "El uso del extintor exige formación y práctica."),
    ],
    op=("Inspección de ejemplo de la «Nave Ejemplo»: extintor F1, 10 meses desde la última revisión; extintor F2, 15 meses; botiquín completo; regla de ejemplo: revisar cada 12 meses. Una caja de cartón está junto a un calefactor. Escribe (a) qué extintor está vencido y por cuántos meses, (b) cuántos meses faltan para el otro, (c) qué dos elementos del fuego se acercan en la caja junto al calefactor, (d) qué debes hacer al notarlo.",
        "(a) F2, vencido por 3 meses. (b) A F1 le faltan 2 meses. (c) Combustible (el cartón) y calor (el calefactor). (d) Informar al responsable para que se separen, sin mover el calefactor encendido ni intervenir.",
        ["detecta el extintor vencido", "calcula los meses", "aplica el triángulo del fuego", "indica que informa"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "no nombrar los elementos del fuego", "decir que apaga el fuego"],
        "Pregunta: «¿cuál es el plazo de la regla?». Si no responde, pídele que lo compare con cada extintor."),
    reinforce="Inventa tres equipos de seguridad con su última revisión y marca cuáles estarían vencidos con una regla de 6 meses.",
    extend="Explica con un ejemplo cómo la prevención evita que se junten los elementos del fuego.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (cuadro de obligaciones y simulacro de papel, de ejemplo). A bordo hay 25 personas. Punto de reunión A: 10 personas; punto B: 8 personas; punto C: 7 personas. Registro de un simulacro de papel: se presentan 10 en A, 7 en B y 7 en C. "
     "La persona que falta figura en el cuadro como «tripulante 14» del punto B. El simulacro de papel tenía 5 minutos de plazo de ejemplo; la última persona llegó a los 6 minutos.")
build(
    O8, 3, F,
    use="Aprenderé a leer un cuadro de obligaciones, a hacer un recuento en un punto de reunión y a informar quién falta sin ponerme en riesgo.",
    prior=["Sé qué es un cuadro de obligaciones.", "Sé calcular porcentajes simples.", "Sé sumar y restar números enteros."],
    explain=[
        "En un simulacro, que es un ensayo de una emergencia, cada persona va a su punto de reunión. El recuento es contar las personas presentes en cada punto y compararlas con el cuadro de obligaciones. Si el número presente es menor que el esperado, hay una persona faltante, que se informa al oficial a cargo con su nombre o número y el punto al que pertenece. El porcentaje de personas presentes es los presentes ÷ los esperados × 100.",
        "Nadie sale a buscar por su cuenta a la persona que falta, porque podría entrar a una zona de riesgo: se informa y el oficial decide quién actúa. Un ejemplo con otra nave: en un punto se esperan 12 personas y se presentan 11, es decir, el 91 % aproximadamente; se informa «falta 1 persona del punto». El simulacro se registra en un acta con fecha, personas presentes, faltantes y firma.",
        f"Este simulacro es de papel: en la vida real se practica con instructor autorizado. {EMER} {AVISO}",
    ],
    vocab=[("simulacro", "ensayo de una emergencia para practicar el cuadro de obligaciones"), ("recuento", "conteo de las personas presentes en un punto de reunión"), ("persona faltante", "persona esperada en un punto que no se presentó"), ("acta de simulacro", "registro con fecha, presentes, faltantes y firma"), ("punto de reunión", "lugar donde se junta cada grupo en una emergencia")],
    worked=[
        ("Recuento", "En un punto de ejemplo se esperan 9 personas y se presentan 8. ¿Cuántas faltan?", ["Se resta lo presente a lo esperado.", "9 − 8."], "1 persona"),
        ("Qué hacer con un faltante", "Falta una persona en un punto de reunión de ejemplo. ¿Qué haces tú, como persona en formación?", ["No sales a buscarla por tu cuenta.", "Informas al oficial a cargo con su número y su punto."], "Informar al oficial a cargo con su número y su punto"),
    ],
    mistakes=[("Salir a buscar por tu cuenta a una persona que falta.", "Puedes entrar a una zona de riesgo y generar otro accidente.", "Informa al oficial a cargo y espera su decisión."),
              ("Informar «falta alguien» sin decir quién ni de qué punto.", "Sin esos datos no se sabe a quién buscar.", "Informa el número o nombre y el punto de reunión.")],
    T=[
        ("=", "{F} ¿Cuántas personas hay en total en los tres puntos, según el cuadro de obligaciones?", "10+8+7", "Se suman las personas esperadas en cada punto.", " personas"),
        ("=", "{F} ¿Cuántas personas se presentaron en el simulacro?", "10+7+7", "Se suman las personas presentes en cada punto.", " personas"),
        ("abc", "{F} ¿Qué punto de reunión quedó incompleto?", "El punto B, porque se esperaban 8 y se presentaron 7", "El punto A, porque se esperaban 10", "El punto C, porque se presentaron 7", "Solo en el punto B el número presente es menor que el esperado."),
        ("=", "{F} ¿Cuántas personas faltan en total?", "25-(10+7+7)", "Se resta el total de presentes al total esperado.", " persona"),
        ("abc", "{F} ¿Cuál es el informe correcto sobre la persona que falta?", "«Falta el tripulante 14 del punto de reunión B»", "«Falta alguien»", "«Falta una persona de otro punto»", "El informe correcto dice quién falta y a qué punto pertenece."),
        ("abc", "{F} Una persona en formación quiere ir a buscar al tripulante 14 por los pasillos. ¿Qué corresponde?", "No ir por su cuenta: informar al oficial a cargo para que decida", "Ir a buscarlo, porque conoce la nave", "Esperar sin avisar a nadie", "Salir a buscar a alguien puede llevar a una zona de riesgo; decide el oficial."),
        ("=", "{F} ¿Qué porcentaje de las personas esperadas se presentó?", "(10+7+7)*100//25", "Se dividen los presentes entre los esperados y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos minutos pasó la última persona del plazo del simulacro?", "6-5", "Se resta el plazo a lo que tardó la última persona.", " minuto"),
        ("abc", "{F} ¿Qué datos debe tener el acta del simulacro de la ficha?", "Fecha, personas presentes, faltantes y firma", "Solo la firma", "Solo la fecha", "Un acta completa tiene fecha, presentes, faltantes y firma."),
        ("abc", "Se produce una emergencia de ejemplo y falta una persona en un punto de reunión. ¿Qué corresponde según las reglas generales?", "No acercarse a la zona de riesgo, dar la alarma e informar al oficial a cargo y a emergencias que falta una persona", "Regresar a la nave a buscarla", "Esperar a ver si llega sola", "Volver a una zona de riesgo es peligroso; se informa a quienes pueden actuar."),
        ("abc", "{F} Un compañero dice: «voy yo a buscarlo, que lo conozco». ¿Qué respuesta es correcta?", "Es falso: nadie sale a buscar por su cuenta; se informa al oficial", "Es cierto, si lleva un chaleco", "Es cierto, si va acompañado", "El chaleco o la compañía no eliminan el riesgo."),
        ("=", "{F} Si los tiempos de llegada por punto fueron A, 4 minutos; B, 6 minutos y C, 5 minutos, ¿cuál fue el tiempo promedio?", "(4+6+5)//3", "Se suman los tiempos y se dividen entre los puntos.", " minutos"),
        ("abc", "En Tripulación de Naves: ¿por qué se hace un recuento en el punto de reunión?", "Para saber si falta alguien y poder informarlo con rapidez", "Para decidir quién maneja la nave", "Para ordenar los equipos de máquinas", "El recuento permite detectar a quien falta."),
    ],
    ctx=("abc", "En un simulacro de ejemplo, un compañero te dice: «anota que estamos todos, así el acta queda bien». ¿Qué respondes?", "Que se anota la verdad, incluido el faltante, e informas al oficial", "Que sí, porque el acta debe verse bien", "Que lo anotas y avisas después", "Falsear el acta oculta un problema que se podría corregir."),
    sc=[
        ("En Tripulación de Naves: ¿qué es un recuento?", "El conteo de las personas presentes en un punto de reunión", "El recuento detecta a las personas que faltan."),
        ("¿Qué se informa de una persona faltante?", "Quién es y de qué punto es", "Con esos datos se puede decidir cómo actuar."),
        ("¿Quién decide cómo buscar a quien falta?", "El oficial a cargo", "Nadie busca por su cuenta y decide el oficial."),
    ],
    op=("Cuadro de obligaciones de ejemplo: 20 personas; punto A, 8; punto B, 6; punto C, 6. En un simulacro de papel se presentan 8 en A, 6 en B y 5 en C. Plazo de ejemplo: 4 minutos; la última persona llega a los 7. Escribe (a) cuántas personas se presentaron y cuántas faltan, (b) qué punto está incompleto, (c) el porcentaje de presentes, (d) qué debe hacer una persona en formación respecto de la persona que falta.",
        "(a) Se presentaron 19 y falta 1. (b) El punto C. (c) 19 × 100 ÷ 20 = 95 %. (d) No sale a buscarla por su cuenta; informa al oficial a cargo quién falta y de qué punto.",
        ["cuenta presentes y faltantes", "identifica el punto incompleto", "informa el resultado", "indica que no busca por su cuenta"],
        ["hoja con las cuatro respuestas"],
        ["olvidar decir quién falta", "salir a buscar por su cuenta", "falsear el acta"],
        "Pregunta: «¿cuántas personas esperabas en cada punto?». Si no responde, pídele que escriba la resta por punto."),
    reinforce="Inventa un cuadro de obligaciones con tres puntos y un registro de simulacro con una persona faltante.",
    extend="Explica por qué es mejor informar a quien está a cargo que buscar a la persona faltante por cuenta propia.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (planilla de ejemplo; valores de ejemplo). A bordo hay 26 personas. Hay 3 balsas salvavidas con capacidad de 10 personas cada una y 28 chalecos. "
     "Regla de ejemplo: las plazas en balsas deben cubrir a todas las personas a bordo, y debe haber al menos 2 chalecos de reserva además de uno por persona. Si suben 4 visitantes de ejemplo, la planilla debe recalcularse.")
build(
    O8, 4, F,
    use="Aprenderé a comparar en una planilla los equipos de salvamento con el número de personas y a recalcular cuando cambian los datos.",
    prior=["Sé qué es un cuadro de obligaciones y el equipo de flotación.", "Sé sumar, restar y multiplicar números enteros.", "Sé comparar un valor con una regla."],
    explain=[
        "Una planilla de equipos de salvamento compara lo que hay con lo que exige la regla. La capacidad total de las balsas es el número de balsas por las plazas de cada una. Los chalecos necesarios son los de cada persona más los de reserva que pida la regla. Si lo que hay es mayor o igual que lo necesario, cumple; si es menor, el faltante es lo necesario menos lo que hay. Cuando cambia el número de personas, se recalcula.",
        "Un ejemplo con otra nave: 15 personas, 2 balsas de 8 plazas (16 plazas) y 17 chalecos con una regla de 2 de reserva: las plazas cubren a las personas, pero los chalecos necesarios son 17 y hay 17, por lo tanto cumple justo. Los números de la regla son de ejemplo; los reales los fija la norma vigente. La planilla no usa ni prepara equipos: solo informa si falta algo.",
        f"Si la planilla no cumple, se informa al oficial a cargo y no se decide por cuenta propia. {EMER} {AVISO}",
    ],
    vocab=[("capacidad total de balsas", "número de balsas por las plazas de cada una"), ("plaza", "lugar para una persona en una balsa"), ("chalecos necesarios", "uno por persona más los de reserva que pida la regla"), ("faltante", "lo necesario menos lo que hay"), ("recalcular", "volver a calcular cuando cambian los datos")],
    worked=[
        ("Capacidad de balsas", "Una nave de ejemplo tiene 2 balsas de 8 plazas. ¿Cuántas plazas hay en total?", ["Se multiplican las balsas por las plazas de cada una.", "2 × 8."], "16 plazas"),
        ("Chalecos necesarios", "Una nave de ejemplo tiene 15 personas y la regla pide 2 chalecos de reserva. ¿Cuántos chalecos se necesitan?", ["Se necesita uno por persona más la reserva.", "15 + 2."], "17 chalecos"),
    ],
    mistakes=[("Olvidar los chalecos de reserva al calcular los necesarios.", "La regla suma una reserva a un chaleco por persona.", "Suma siempre la reserva."),
              ("No recalcular cuando suben más personas.", "Los números cambian y la planilla puede dejar de cumplir.", "Recalcula cada vez que cambia el número de personas.")],
    T=[
        ("=", "{F} ¿Cuántas plazas hay en total en las balsas?", "3*10", "Se multiplican las balsas por las plazas de cada una.", " plazas"),
        ("abc", "{F} ¿Cubren las plazas de las balsas a las 26 personas a bordo?", "Sí, porque 30 plazas son más que 26 personas", "No, porque hay 3 balsas y 26 personas", "No, porque faltan balsas", "30 plazas superan las 26 personas."),
        ("=", "{F} ¿Cuántos chalecos se necesitan según la regla?", "26+2", "Se suman las 26 personas y los 2 chalecos de reserva.", " chalecos"),
        ("abc", "{F} ¿Cumple la regla de chalecos con los 28 que hay?", "Sí, porque hay 28 y se necesitan 28", "No, porque hay 28 y se necesitan 30", "No, porque no hay reserva", "Los 28 chalecos igualan lo que pide la regla."),
        ("=", "{F} Si suben los 4 visitantes, ¿cuántas personas hay a bordo?", "26+4", "Se suman los visitantes a las personas a bordo.", " personas"),
        ("abc", "{F} Con los visitantes, ¿cubren las plazas de las balsas a todas las personas?", "Sí, porque 30 plazas igualan a 30 personas", "No, porque 30 plazas son menos que 30 personas", "No, porque hay 3 balsas", "Con 30 plazas para 30 personas, cada persona tiene su plaza."),
        ("=", "{F} Con los visitantes, ¿cuántos chalecos se necesitan?", "(26+4)+2", "Se suman las personas con visitantes y los chalecos de reserva.", " chalecos"),
        ("=", "{F} Con los visitantes, ¿cuántos chalecos faltan?", "(26+4)+2-28", "Se resta lo que hay a lo que se necesita.", " chalecos"),
        ("abc", "{F} Con los visitantes, ¿qué debe informar la planilla?", "Que faltan 4 chalecos para cumplir la regla", "Que cumple con todo", "Que faltan balsas", "Los chalecos necesarios son 32 y hay 28; las plazas alcanzan justo."),
        ("abc", "{F} Un compañero dice: «como las plazas alcanzan, no importa que falten chalecos». ¿Qué respuesta es correcta?", "Es falso: la regla exige las dos cosas, y los chalecos faltan", "Es cierto, porque las balsas son lo más importante", "Es cierto, si los visitantes son pocos", "La regla exige plazas y chalecos; incumplir uno ya es un incumplimiento."),
        ("abc", "{F} Una persona en formación nota que la planilla no cumple. ¿Qué corresponde?", "Informar al oficial a cargo y no decidir por su cuenta", "Anotar que cumple para que los visitantes puedan subir", "Descontar los chalecos de reserva de la regla", "La decisión sobre los visitantes es del oficial; se informa el incumplimiento."),
        ("=", "{F} Si se agregara una cuarta balsa de 10 plazas, ¿cuántas plazas sobrarían para las 30 personas?", "(3*10+10)-(26+4)", "Se suman las plazas de la nueva balsa y se restan las personas.", " plazas"),
        ("abc", "En Tripulación de Naves: ¿por qué la planilla se recalcula cuando cambia el número de personas?", "Porque los equipos necesarios dependen del número de personas", "Porque las balsas cambian de tamaño solas", "Porque la regla cambia cada día", "Con más personas, lo necesario aumenta."),
    ],
    ctx=("abc", "En una planilla de ejemplo, una persona te dice: «anota 32 chalecos aunque solo hay 28, así podemos recibir a los visitantes». ¿Qué respondes?", "Que se anota lo que realmente hay e informas el faltante", "Que sí, porque el oficial no revisa", "Que sí, y consigues los chalecos después", "Falsear la planilla pone en riesgo a las personas en una emergencia."),
    sc=[
        ("En Tripulación de Naves: ¿cuántos chalecos pide la regla?", "Uno por persona más los de reserva", "La reserva se suma al número de personas."),
        ("¿Cómo se calcula la capacidad total de las balsas?", "Número de balsas por plazas de cada una", "Así se obtienen las plazas totales."),
        ("¿Quién decide si suben más personas?", "El oficial a cargo", "La persona en formación calcula e informa."),
    ],
    op=("Planilla de ejemplo de la «Nave Ejemplo»: 20 personas; 2 balsas de 12 plazas; 21 chalecos; regla de ejemplo: plazas para todos y 2 chalecos de reserva además de uno por persona. Suben 3 visitantes de ejemplo. Escribe (a) las plazas totales y si cubren a las 20 personas, (b) los chalecos necesarios y si cumple, (c) lo que ocurre con los visitantes, (d) qué informarías al oficial.",
        "(a) 2 × 12 = 24 plazas, que cubren a las 20 personas. (b) 20 + 2 = 22 chalecos necesarios; hay 21, no cumple. (c) Con los 3 visitantes: 23 personas; las 24 plazas siguen cubriendo, pero los chalecos necesarios son 25 y faltan 4. (d) «La planilla no cumple la regla de chalecos: faltan 1 chaleco sin visitantes y 4 con los 3 visitantes».",
        ["calcula las plazas", "calcula los chalecos necesarios", "recalcula con visitantes", "informa el faltante"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la reserva", "no recalcular con los visitantes", "falsear el número de chalecos"],
        "Pregunta: «¿cuántos chalecos se necesitan con y sin visitantes?». Si no responde, pídele que escriba las dos sumas."),
    reinforce="Inventa una planilla con balsas y chalecos y recalcula qué pasa si sube el número de personas.",
    extend="Explica por qué no basta con tener plazas en balsas si faltan chalecos.",
)

# ============================================================ OAE-08, clase 5
F = ("Ficha 5 (alternativas de ejemplo). Planes de simulacros de papel para 24 personas. Plan A: un simulacro al mes de 30 minutos. Plan B: un simulacro cada 3 meses de 120 minutos. "
     "Criterio obligatorio de ejemplo: cada persona participa en un simulacro al menos cada 2 meses. Criterio de elección: menor tiempo total al año. Acta de ejemplo: línea 1, fecha, 24 presentes, firma del oficial; línea 2, fecha, sin número de presentes, sin firma.")
build(
    O8, 5, F,
    use="Aprenderé a comparar planes de simulacros con criterios y a verificar que un acta esté completa.",
    prior=["Sé qué es un simulacro y un acta.", "Sé qué es un criterio obligatorio.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Para comparar planes de simulacros se aplican los mismos criterios a todos. El criterio obligatorio fija una exigencia mínima, por ejemplo, que cada persona participe cada cierto número de meses; los planes que no la cumplen se descartan. El criterio de elección sirve para escoger entre los que quedan, como el menor tiempo total al año. El tiempo total anual es el número de simulacros del año por la duración de cada uno.",
        "Verificar un acta es comprobar que cada línea tenga fecha, número de presentes y firma. Una línea incompleta se devuelve a quien la hizo para que la complete con datos reales, sin inventar nada. Un ejemplo con otros planes: uno hace 6 simulacros de 20 minutos al año (uno cada 2 meses) y otro 3 de 50 (uno cada 4 meses); si la exigencia es participar cada 3 meses, el primero cumple y el segundo se descarta. Los simulacros reales se realizan solo con instructor autorizado.",
        f"Elegir el plan es una decisión del oficial a cargo y de la persona responsable de la seguridad. {EMER} {AVISO}",
    ],
    vocab=[("plan de simulacros", "calendario de ensayos de emergencia con su frecuencia y duración"), ("criterio obligatorio", "exigencia mínima que debe cumplir un plan"), ("tiempo total anual", "simulacros del año por la duración de cada uno"), ("acta completa", "acta con fecha, presentes y firma en cada línea"), ("frecuencia", "cada cuánto tiempo se repite algo")],
    worked=[
        ("Tiempo anual", "Un plan de ejemplo hace 4 simulacros al año de 60 minutos. ¿Cuántos minutos suma al año?", ["Se multiplican los simulacros por su duración.", "4 × 60."], "240 minutos"),
        ("Aplicar el criterio", "Un plan de ejemplo hace un simulacro cada 4 meses y la exigencia es participar cada 3 meses. ¿Cumple?", ["Cada 4 meses es más espaciado que cada 3.", "No cumple la exigencia."], "No cumple"),
    ],
    mistakes=[("Elegir el plan más corto sin revisar si cumple la frecuencia exigida.", "El criterio obligatorio va primero.", "Aplica primero el criterio obligatorio."),
              ("Completar una línea de acta con datos inventados.", "Un dato inventado falsea el registro.", "Devuelve la línea a quien la hizo.")],
    T=[
        ("=", "{F} ¿Cuántos simulacros hay al año en el plan A, que hace uno cada mes?", "12*1", "Hay uno al mes y un año tiene 12 meses, por lo tanto son 12 simulacros.", " simulacros"),
        ("=", "{F} ¿Cuántos minutos suma al año el plan A?", "12*30", "Se multiplican los simulacros del año por la duración de cada uno.", " minutos"),
        ("abc", "{F} ¿Cumple el plan A con el criterio obligatorio?", "Sí, porque cada persona participa cada mes y eso es menos de 2 meses", "No, porque cada simulacro dura solo 30 minutos", "No, porque hace demasiados simulacros", "Un simulacro al mes cumple la exigencia de participar al menos cada 2 meses."),
        ("=", "{F} ¿Cuántos simulacros hay al año en el plan B?", "12//3", "Se divide el año en meses entre la frecuencia en meses.", " simulacros"),
        ("=", "{F} ¿Cuántos minutos suma al año el plan B?", "(12//3)*120", "Se multiplican los simulacros del año por la duración de cada uno.", " minutos"),
        ("abc", "{F} ¿Cumple el plan B con el criterio obligatorio?", "No, porque cada persona participa cada 3 meses y la exigencia es cada 2", "Sí, porque dura más cada simulacro", "Sí, porque son pocos simulacros", "Cada 3 meses es más espaciado que cada 2."),
        ("abc", "{F} ¿Qué plan se elige según los criterios?", "El plan A, porque cumple el criterio obligatorio y B no", "El plan B, porque suma menos simulacros", "Ninguno, porque ambos toman tiempo", "El plan B se descarta por no cumplir la frecuencia exigida."),
        ("=", "{F} ¿Cuántos minutos menos al año suma el plan A que el plan B?", "(12//3)*120-12*30", "Se resta el tiempo anual del plan A al del plan B.", " minutos"),
        ("=", "{F} ¿Cuántas horas suma al año el plan A?", "(12*30)//60", "Se dividen los minutos del año entre 60.", " horas"),
        ("abc", "{F} ¿Qué falta en la línea 2 del acta?", "El número de presentes y la firma", "La fecha", "Nada, porque tiene fecha", "La línea tiene fecha, pero no dice cuántas personas se presentaron y no está firmada."),
        ("abc", "{F} Un compañero propone completar la línea 2 con «24 presentes» para que se vea completa. ¿Qué corresponde?", "Devolverla a quien la hizo para que la complete con datos reales", "Completarla, porque la línea 1 dice 24", "Borrar la línea", "Un acta se completa con datos reales de quien registró el simulacro."),
        ("=", "{F} Con 24 personas, ¿cuántos minutos-persona suma un simulacro del plan A?", "24*30", "Se multiplican las personas por los minutos del simulacro.", " minutos-persona"),
        ("abc", "{F} Un compañero dice: «elijamos el plan B porque hace menos reuniones». ¿Qué respuesta es correcta?", "Es falso: el plan B no cumple el criterio obligatorio", "Es cierto, porque menos reuniones es siempre mejor", "Es cierto, si el oficial lo prefiere", "El criterio obligatorio de frecuencia se aplica antes que el tiempo."),
    ],
    ctx=("abc", "En una planilla de ejemplo, una persona te pide que cambies la frecuencia exigida de 2 meses a 4 meses para que el plan B cumpla. ¿Qué respondes?", "Que no se cambia un criterio de seguridad para favorecer un plan, y que lo informas al oficial", "Que sí, porque así se ahorra tiempo", "Que sí, pero solo en la copia", "Alterar un criterio de seguridad para favorecer una opción pone en riesgo a las personas."),
    sc=[
        ("En Tripulación de Naves: ¿qué se hace con un plan que no cumple el criterio obligatorio?", "Se descarta", "Un plan que no cumple queda fuera de la comparación."),
        ("¿Qué datos tiene una línea completa de un acta?", "Fecha, número de presentes y firma", "Con esos datos se reconstruye lo ocurrido."),
        ("¿Quién realiza los simulacros reales?", "Se hacen con instructor autorizado", "Este cuaderno solo planifica en papel."),
    ],
    op=("Planes de ejemplo para 30 personas. Plan X: un simulacro cada 2 meses de 45 minutos. Plan Y: un simulacro cada 4 meses de 90 minutos. Criterio obligatorio de ejemplo: participar al menos cada 3 meses. Criterio de elección: menor tiempo total al año. Acta de ejemplo: línea 1, fecha, 30 presentes, firma; línea 2, fecha, 28 presentes, sin firma. Escribe (a) cuál plan cumple el criterio obligatorio, (b) los minutos anuales de ese plan, (c) qué falta en la línea 2, (d) qué haces con esa línea.",
        "(a) El plan X, porque participa cada 2 meses, menos de 3; el plan Y se descarta porque es cada 4 meses. (b) 12 ÷ 2 = 6 simulacros; 6 × 45 = 270 minutos. (c) La firma. (d) Se devuelve a quien la hizo para que la firme, sin inventar la firma.",
        ["aplica el criterio obligatorio", "calcula los minutos anuales", "detecta lo que falta en el acta", "indica qué hacer con la línea incompleta"],
        ["hoja con las cuatro respuestas"],
        ["elegir Y por ser más corto", "olvidar multiplicar por los simulacros", "inventar la firma"],
        "Pregunta: «¿cada cuántos meses participa cada persona en cada plan?». Si no responde, pídele que lo compare con la exigencia."),
    reinforce="Inventa dos planes de simulacros con frecuencia y duración y escribe cuál cumple una exigencia de cada 3 meses.",
    extend="Explica por qué un acta completa ayuda a mejorar el siguiente simulacro.",
)
