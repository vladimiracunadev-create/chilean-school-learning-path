"""Acuicultura TP 3.º y 4.º medio: OAE-01 (reproductores) y OAE-02 (manejo). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_acui_common import AVISO, EMER, build

O1 = "TP-ACUI-3y4-OAE-01"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El criadero ficticio «Criadero Demo» mantiene 60 reproductores de «especie A» en estanques bajo techo para obtener huevos y larvas. "
     "Peligros anotados: piso mojado y resbaladizo alrededor de los estanques, bordes de estanque sin baranda, bombas eléctricas cerca del agua y una bodega con productos de uso sanitario.")
build(
    O1, 1, F,
    use="Aprenderé qué es un reproductor, cómo se pasa de gameto a larva, qué es la bioseguridad y cómo se ordenan las medidas de prevención en un criadero.",
    prior=["Sé leer una ficha escrita y una lista de datos.", "Sé sumar, restar, multiplicar y dividir números enteros.", "Sé que los animales acuáticos necesitan agua de buena calidad."],
    explain=[
        "Un criadero es una instalación donde se obtienen huevos y larvas de especies hidrobiológicas, es decir, que viven en el agua. Los reproductores son los animales adultos que se mantienen para producir descendencia. Sus gametos son las células sexuales: el óvulo de la hembra y el espermio del macho. La fecundación es la unión de un óvulo con un espermio; de ella resulta un embrión, que después se desarrolla hasta ser una larva, la cría que sale del huevo.",
        "Un criadero trabaja en un ambiente controlado: un lugar donde se regulan el agua, la temperatura y la luz. Allí la bioseguridad reúne las medidas para evitar que una enfermedad entre, salga o se propague entre grupos de animales. El manejo ético exige tratar a los animales evitando sufrimiento innecesario y cumpliendo la norma vigente. Todo trabajo tiene peligros, que son fuentes de daño, y riesgos, que son la posibilidad de que ese daño ocurra.",
        f"La jerarquía de controles ordena la prevención de la más a la menos efectiva: eliminar el peligro, sustituirlo, aplicar controles de ingeniería (cambios físicos del lugar), controles administrativos (reglas, señales y capacitación) y, al final, el equipo de protección personal (EPP). El agua y la electricidad juntas son un peligro serio. {EMER} {AVISO}",
    ],
    vocab=[("criadero", "instalación donde se obtienen huevos y larvas de especies que viven en el agua"), ("reproductor", "animal adulto mantenido para producir descendencia"), ("gameto", "célula sexual: óvulo o espermio"), ("fecundación", "unión de un óvulo con un espermio"), ("larva", "cría que sale del huevo"), ("ambiente controlado", "lugar donde se regulan el agua, la temperatura y la luz"), ("bioseguridad", "medidas para evitar que una enfermedad entre, salga o se propague"), ("peligro", "fuente con capacidad de causar daño"), ("riesgo", "posibilidad de que un peligro cause daño"), ("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("EPP", "equipo de protección personal, la última barrera"), ("manejo ético", "trato que evita sufrimiento innecesario y cumple la norma vigente")],
    worked=[
        ("Peligro y riesgo", "En una sala de ejemplo, la escalera de ingreso está húmeda y sin antideslizante. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la escalera húmeda, porque puede causar daño.", "El riesgo es que alguien resbale al subir y se lastime."], "Peligro: la escalera húmeda; riesgo: que alguien resbale y se lastime"),
        ("Clasificar un control", "Un criadero de ejemplo escribe una regla: nadie entra solo a la sala de estanques durante la noche. ¿A qué nivel de la jerarquía corresponde?", ["La regla ordena una conducta, pero no cambia el lugar.", "Las reglas, señales y capacitación son controles administrativos."], "Control administrativo"),
    ],
    mistakes=[("Creer que usar guantes y botas basta para trabajar seguro en cualquier tarea de un criadero.", "El EPP es la última barrera: no quita el peligro y protege solo a quien lo usa.", "Primero se elimina o se controla el peligro; el EPP se suma a esas medidas."),
              ("Creer que leer una ficha de criadero habilita para hacer las labores que describe.", "Las labores de riesgo exigen autorización, instructor y norma vigente.", "Aprende aquí el concepto y deja la labor a personal autorizado.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es un reproductor?", "Un animal adulto mantenido para producir descendencia", "Una cría recién salida del huevo que aún no se alimenta", "Un ejemplar de tamaño comercial destinado a la venta", "El reproductor es el adulto que aporta gametos; la cría es larva y el de tamaño comercial es otro tipo de ejemplar."),
        ("abc", "En Acuicultura: ¿qué es la fecundación?", "La unión de un óvulo con un espermio", "El paso de la larva a un estanque más grande", "El momento en que una cría empieza a comer", "La fecundación une dos gametos; el traslado y la alimentación son otras etapas."),
        ("abc", "En Acuicultura: ¿qué es la bioseguridad?", "Las medidas para evitar que una enfermedad entre, salga o se propague en un cultivo", "Las medidas para que los animales crezcan más rápido", "El permiso que autoriza usar un terreno cerca del mar", "La bioseguridad previene el contagio; la velocidad de crecimiento y los permisos son otros temas."),
        ("=", "En el criadero de ejemplo, 60 reproductores se reparten en grupos de 12 por estanque para que un contagio no alcance a todos. ¿Cuántos estanques hacen falta?", "60//12", "Se divide el total de reproductores entre los que caben en cada estanque.", " estanques"),
        ("abc", "{F} Un compañero dice que las bombas eléctricas cerca del agua son un riesgo. ¿Cuál es el riesgo correcto?", "Que una persona reciba una descarga si hay contacto entre agua y electricidad", "La bomba misma, guardada en su lugar", "Que los reproductores coman menos", "El riesgo es la posibilidad de daño; la bomba guardada es el peligro y el apetito es otro asunto."),
        ("abc", "{F} Una baranda fija en el borde del estanque, instalada por personal autorizado, es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla escrita", "De EPP, porque protege a quien se acerca", "La baranda modifica el lugar y no depende de que cada persona la recuerde."),
        ("abc", "{F} Una persona propone usar las mismas botas y los mismos baldes en dos salas distintas para ahorrar. ¿Qué principio de bioseguridad se descuida?", "Evitar llevar enfermedades de una sala a otra", "Mantener la temperatura del agua estable", "Alimentar a los reproductores a la misma hora", "Compartir elementos entre salas puede trasladar un contagio de un grupo a otro."),
        ("abc", "{F} Una estudiante dice: «leí la ficha, así que puedo aplicar un producto de uso sanitario a los reproductores». ¿Qué respuesta es correcta?", "Es falso: aplicar productos exige personal autorizado y norma vigente", "Es cierto, si usa guantes", "Es cierto, si otra persona la mira", "Leer una ficha no habilita para una tarea de riesgo; guantes o compañía tampoco."),
        ("abc", "Durante una visita de ejemplo a un criadero, una persona cae a un estanque. ¿Qué corresponde según las reglas generales?", "No acercarte al borde ni entrar al agua, y avisar a un adulto responsable y a emergencias", "Entrar al agua para sacarla lo antes posible", "Esperar a que salga sola antes de avisar", "Entrar al agua pone en peligro a otra persona; se avisa a quienes pueden actuar."),
        ("abc", "En Acuicultura: ¿por qué retirar un peligro del lugar es más efectivo que entregar un EPP?", "Porque el peligro desaparece para todos y el EPP protege solo a quien lo usa", "Porque el EPP elimina el peligro, pero es más caro", "Porque el EPP solo se usa cuando falla la capacitación", "Los niveles altos actúan sobre el peligro mismo; el EPP no lo elimina."),
        ("=", "Una bodega de ejemplo guarda 24 envases de productos de uso sanitario y cada estante admite 6. ¿Cuántos estantes se necesitan?", "24//6", "Se divide el total de envases entre los que admite cada estante.", " estantes"),
        ("abc", "{F} Para el riesgo de las bombas eléctricas cerca del agua, ¿qué medida de nivel más efectivo se podría sumar a una regla escrita?", "Un corte automático de corriente instalado por personal autorizado", "Otro cartel con la misma advertencia", "Pedir a cada persona que use botas", "El corte automático es un control de ingeniería; el cartel es administrativo y las botas son EPP."),
        ("abc", "En Acuicultura: ¿qué exige el manejo ético de las especies?", "Evitar sufrimiento innecesario y cumplir la norma vigente", "Reducir el costo aunque los animales sufran", "Cumplir solo lo que decida cada trabajador", "El manejo ético protege el bienestar de los animales y se rige por la norma."),
    ],
    ctx=("abc", "Un conocido te invita a ayudarle en su centro de cultivo un fin de semana, subiendo a una balsa sin chaleco ni autorización. ¿Qué respondes?", "Que no, porque esa tarea exige instructor autorizado, equipo de flotación y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque con un poco de cuidado basta", "Que sí, pero solo si hace buen tiempo", "El buen tiempo no reemplaza la autorización, el equipo de flotación ni la norma."),
    sc=[
        ("En Acuicultura: ¿qué es un gameto?", "Una célula sexual: óvulo o espermio", "El gameto es la célula que aporta cada reproductor."),
        ("¿Qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
        ("¿Qué es una larva?", "La cría que sale del huevo", "La larva es la etapa posterior al embrión."),
    ],
    op=("El criadero ficticio «Criadero Demo» anota una tarea de ejemplo: caminar junto a los estanques por un borde mojado y sin baranda para revisar la bodega. Escribe (a) cuál es el peligro del borde y cuál el riesgo asociado, (b) un control administrativo, (c) un control de ingeniería, (d) por qué el EPP no basta y quién hace la tarea.",
        "(a) Peligro: borde mojado y sin baranda; riesgo: que la persona resbale, caiga al estanque y se lastime. (b) Una regla escrita que solo permita el paso con el borde seco y en compañía. (c) Una baranda fija y una superficie antideslizante instaladas por personal autorizado. (d) El EPP es la última barrera: no quita el peligro y protege solo a quien lo usa; la tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "no aclarar que la tarea la hace personal autorizado"],
        "Pregunta: «¿qué control cambia el borde y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el nivel de ingeniería."),
    reinforce="Escribe la jerarquía de controles en orden y pon junto a cada nivel un ejemplo inventado de un criadero.",
    extend="Explica con un ejemplo por qué una charla de seguridad es un control administrativo y no reemplaza una medida de ingeniería.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (registro de ejemplo, inventado). Criadero Demo, lote R-04 de «especie B»: 48 reproductores, 20 machos y 28 hembras, comprados el mismo día a un proveedor registrado. "
     "Cada hembra aporta 2.000 huevos en la temporada (dato de ejemplo). Documentos del criadero: la ficha del lote (origen, fecha, cantidad y sexo), la bitácora de alimentación (qué comió cada día) y el registro de cuarentena (separación y observación de animales recién llegados).")
build(
    O1, 2, F,
    use="Aprenderé los conceptos de fecundidad, relación de sexos y cuarentena, los documentos de un lote de reproductores y los roles de quienes trabajan con ellos.",
    prior=["Sé qué es un reproductor, un gameto y la bioseguridad.", "Sé leer un registro escrito.", "Sé multiplicar, restar y dividir números enteros."],
    explain=[
        "Los reproductores se identifican por lotes: un lote es el grupo de animales de la misma especie y origen que se maneja junto. La fecundidad es el número de huevos que produce una hembra. La relación de sexos indica cuántos machos y cuántas hembras hay en un lote. La trazabilidad es poder seguir la historia del lote: de dónde viene, qué cuidados recibió y cuántos animales quedan.",
        "Cuando llegan animales nuevos se aplica una cuarentena: un tiempo en que se mantienen separados y en observación antes de juntarlos con otros, como medida de bioseguridad. Los documentos que respaldan el trabajo son la ficha del lote, la bitácora de alimentación y el registro de cuarentena. Un registro útil dice qué se anotó, cuánto, cuándo y quién lo hizo, y nunca se altera para que «se vea mejor».",
        f"Cada rol tiene su función. El jefe del criadero organiza la producción. El técnico en acuicultura decide los cuidados de cada lote. El prevencionista asesora en riesgos del trabajo. El personal autorizado ejecuta las labores que la norma le permite. {EMER} {AVISO}",
    ],
    vocab=[("lote", "grupo de animales de la misma especie y origen que se maneja junto"), ("fecundidad", "número de huevos que produce una hembra"), ("relación de sexos", "cuántos machos y cuántas hembras hay en un lote"), ("trazabilidad", "posibilidad de seguir la historia de un lote"), ("cuarentena", "tiempo de separación y observación de animales recién llegados"), ("ficha del lote", "documento con origen, fecha, cantidad y sexo de un lote"), ("bitácora de alimentación", "registro de lo que comió el lote cada día"), ("prevencionista", "persona que asesora en prevención de riesgos del trabajo")],
    worked=[
        ("Calcular huevos", "Un lote de ejemplo tiene 12 hembras y cada una aporta 800 huevos. ¿Cuántos huevos se esperan en total?", ["Cada hembra aporta 800 huevos.", "12 por 800 es 9.600."], "9.600 huevos"),
        ("Elegir el documento", "El técnico de un criadero de ejemplo quiere saber el proveedor y la fecha de compra de un lote. ¿Qué documento consulta?", ["Proveedor y fecha son datos de identificación del lote.", "Eso se anota en la ficha del lote."], "La ficha del lote"),
    ],
    mistakes=[("Anotar una cantidad distinta de la real para que el registro «cuadre» con la compra.", "Un registro alterado hace perder la trazabilidad y oculta un problema real.", "Se anota la cantidad real, se informa la diferencia al técnico y se revisa el documento."),
              ("Creer que la ficha del lote reemplaza la bitácora de alimentación.", "La ficha identifica el lote; la bitácora dice qué comió cada día.", "Consulta cada documento para lo que fue hecho.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la fecundidad de una hembra?", "El número de huevos que produce", "El porcentaje de huevos que llegan a larva", "La edad a la que llega al criadero", "La fecundidad cuenta los huevos que produce; el porcentaje de larvas mide otra cosa."),
        ("abc", "En Acuicultura: ¿qué es la cuarentena de animales recién llegados?", "Un tiempo de separación y observación antes de juntarlos con otros", "Un tiempo en que se les entrega alimento extra", "El plazo en que se vende el lote", "La cuarentena es una medida de bioseguridad que separa y observa."),
        ("abc", "En Acuicultura: ¿para qué sirve la ficha de un lote de reproductores?", "Para identificar el lote y dar trazabilidad: origen, fecha, cantidad y sexo", "Para fijar el precio de venta de cada animal", "Para autorizar el uso de un equipo", "La ficha da trazabilidad; el precio y las autorizaciones son otros documentos."),
        ("=", "{F} ¿Cuántos huevos se esperan en la temporada si todas las hembras del lote aportan lo indicado?", "28*2000", "Se multiplica el número de hembras por los huevos de cada una.", " huevos"),
        ("abc", "{F} ¿Qué documento sirve para anotar día a día lo que comió el lote?", "La bitácora de alimentación", "La ficha del lote", "El registro de cuarentena", "La bitácora guarda la alimentación diaria; la ficha identifica el lote y la cuarentena registra el aislamiento."),
        ("=", "{F} ¿Cuántas hembras más que machos hay en el lote?", "28-20", "Se resta el número de machos al de hembras.", " hembras"),
        ("abc", "{F} ¿Qué rol del criadero se dedica a asesorar en prevención de riesgos?", "El prevencionista", "El jefe del criadero", "El personal autorizado que ejecuta las labores", "El prevencionista asesora en riesgos; el jefe organiza y el personal ejecuta."),
        ("abc", "{F} Llegan 12 reproductores nuevos de otro proveedor. ¿Qué corresponde según la bioseguridad?", "Mantenerlos en cuarentena separada y anotarlos en una ficha de lote propia", "Mezclarlos de inmediato con el lote R-04 para ahorrar espacio", "Anotarlos dentro del lote R-04 sin ficha propia", "Los animales de otro origen se separan y se registran aparte para no perder trazabilidad."),
        ("=", "{F} Esta temporada 6 hembras del lote no aportan huevos. ¿Cuántos huevos se esperan ahora?", "(28-6)*2000", "Se restan las hembras que no aportan y se multiplica por los huevos de cada una.", " huevos"),
        ("abc", "{F} Una anotación dice solo «comieron bien», sin fecha, cantidad ni nombre de quien la escribió. ¿Por qué es un registro débil?", "Porque sin fecha, cantidad ni responsable no se puede verificar ni seguir su historia", "Porque la alimentación nunca debe registrarse", "Porque los registros solo valen si están escritos en computador", "La trazabilidad exige saber cuándo, cuánto y quién anotó el dato."),
        ("abc", "{F} Un compañero propone anotar 30 hembras en lugar de 28 porque «se verá mejor ante el jefe». ¿Qué corresponde?", "No alterar el dato: se anota la cantidad real", "Anotar 30 si después se corrige", "Anotar 29 para que la diferencia sea menor", "Un registro alterado oculta la realidad, sea poco o mucho."),
        ("abc", "{F} Un compañero dice: «leí la ficha del lote, así que puedo seleccionar reproductores yo solo». ¿Qué respuesta es correcta?", "Es falso: la selección la hace personal capacitado y autorizado; la ficha informa, no habilita", "Es cierto, porque la ficha trae toda la información", "Es cierto, si usa guantes", "Una ficha no reemplaza la formación ni la autorización."),
        ("abc", "{F} La compra de ejemplo decía 48 animales y la ficha del lote anota 47. ¿Qué es lo más adecuado?", "Informar la diferencia al técnico con ambos documentos como respaldo, sin cambiar ningún número", "Cambiar la ficha a 48 sin avisar", "Esperar un mes por si se corrige sola", "Una diferencia se informa con evidencia; ocultarla impide corregirla."),
    ],
    ctx=("abc", "Una compañera te propone «arreglar» las cantidades de la ficha antes de la visita de una fiscalizadora. ¿Qué respondes?", "Que no, porque un registro no se altera, y que cualquier duda se consulta con el técnico o un adulto responsable", "Que sí, pero solo las cantidades más llamativas", "Que sí, si después se corrige en la próxima visita", "Alterar un registro oculta la realidad, aunque sea poco o temporal."),
    sc=[
        ("En Acuicultura: ¿qué es un lote?", "Un grupo de animales de igual especie y origen que se maneja junto", "El lote permite manejar y seguir juntos a animales de iguales características."),
        ("¿Qué es la trazabilidad?", "Poder seguir la historia de un lote", "La trazabilidad permite saber el origen y los cuidados de cada lote."),
        ("¿Qué se hace con una diferencia entre dos documentos?", "Se informa al técnico sin cambiar ningún número", "Se informa con evidencia para poder corregir el problema."),
    ],
    op=("Ficha de ejemplo: lote R-09 de «especie A», 36 hembras y 24 machos, cada hembra aporta 1.500 huevos de ejemplo. Llegaron 10 animales nuevos de otro proveedor. Escribe (a) cuántos huevos se esperan en total, (b) en qué documento se anota el origen del lote, (c) qué haces con los 10 animales nuevos según la bioseguridad, (d) qué rol consultarías si dudas sobre un riesgo del trabajo.",
        "(a) 36 × 1.500 = 54.000 huevos. (b) En la ficha del lote. (c) Se mantienen en cuarentena separada y se anotan en una ficha de lote propia. (d) Al prevencionista. Las labores con animales las hace personal autorizado.",
        ["calcula bien los huevos", "nombra el documento correcto", "aplica cuarentena y ficha propia", "nombra el rol adecuado"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar por los machos en vez de las hembras", "juntar los animales nuevos con el lote", "confundir el rol del prevencionista con el del jefe"],
        "Pregunta: «¿qué pasa con la trazabilidad si se mezclan los lotes?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una ficha de lote de tres líneas (especie A o B, hembras y huevos por hembra) y calcula los huevos esperados.",
    extend="Explica con un ejemplo por qué el técnico y el prevencionista no cumplen la misma función.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (registro de ejemplo, inventado). Criadero Demo, tres tandas de huevos de «especie A». Tanda 1: 2.000 huevos puestos, 1.600 fecundados, 1.200 eclosionados. "
     "Tanda 2: 2.500 puestos, 2.000 fecundados, 1.000 eclosionados. Tanda 3: 1.500 puestos, 900 fecundados, 720 eclosionados. Metas de ejemplo: fecundación mínima de 70 %, eclosión mínima de 65 %.")
build(
    O1, 3, F,
    use="Aprenderé a analizar el registro de una tanda de huevos: calcular tasas de fecundación y de eclosión, compararlas con una meta y proponer causas probables que hay que comprobar.",
    prior=["Sé qué es la fecundación y la bioseguridad.", "Sé calcular un porcentaje con números enteros.", "Sé leer una tabla escrita."],
    explain=[
        "Analizar un caso en papel significa leer los datos, compararlos con lo esperado, decidir qué significan y proponer acciones. Una tanda es un grupo de huevos obtenidos juntos. La tasa de fecundación es el porcentaje de huevos puestos que fueron fecundados: se calcula fecundados × 100 ÷ puestos. La tasa de eclosión es el porcentaje de huevos fecundados que eclosionan, es decir, que se abren y dejan salir la larva: eclosionados × 100 ÷ fecundados.",
        "Una meta es el valor que se espera alcanzar; una desviación es un valor que queda por debajo (o fuera) de esa meta. Una causa probable es una explicación posible que todavía hay que comprobar con más registros: dos hechos que coinciden no prueban que uno cause el otro. Cuando un dato queda bajo la meta se informa al técnico con el registro como respaldo, sin cambiarlo.",
        f"Estas decisiones las toman el técnico y la jefatura con personal capacitado; aquí aprendes a razonar con los datos de un registro escrito. {EMER} {AVISO}",
    ],
    vocab=[("tanda", "grupo de huevos obtenidos juntos"), ("tasa de fecundación", "porcentaje de huevos puestos que fueron fecundados"), ("eclosión", "momento en que el huevo se abre y sale la larva"), ("tasa de eclosión", "porcentaje de huevos fecundados que eclosionan"), ("meta", "valor que se espera alcanzar"), ("desviación", "valor que queda fuera de lo esperado"), ("causa probable", "explicación posible que todavía hay que comprobar")],
    worked=[
        ("Tasa de fecundación", "Una tanda de ejemplo tiene 500 huevos puestos y 400 fecundados. ¿Cuál es la tasa de fecundación?", ["Se multiplica 400 por 100: 40.000.", "Se divide entre 500: 40.000 ÷ 500 es 80."], "80 %"),
        ("Comparar con una meta", "Una tanda de ejemplo tiene una tasa de eclosión de 60 % y la meta de ejemplo es 65 %. ¿Cumple la meta?", ["Se compara 60 con 65.", "60 es menor que 65."], "No cumple: queda 5 puntos bajo la meta"),
    ],
    mistakes=[("Concluir la causa de un resultado bajo solo porque coincidió con otro hecho ese día.", "Que dos hechos coincidan no prueba que uno cause el otro.", "Anótala como causa probable y compruébala con más datos."),
              ("Subir una tasa baja a la meta para que el registro se vea mejor.", "El dato real es la base de cualquier decisión.", "Se deja el dato y se informa al técnico con el registro.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la tasa de fecundación?", "El porcentaje de huevos puestos que fueron fecundados", "El porcentaje de larvas que sobreviven un mes", "El número de huevos que produce cada hembra", "La tasa de fecundación compara fecundados con puestos."),
        ("abc", "En Acuicultura: ¿qué es la tasa de eclosión?", "El porcentaje de huevos fecundados que eclosionan", "El porcentaje de huevos puestos que se perdieron", "El peso medio de las larvas al nacer", "La eclosión se mide sobre los huevos fecundados, no sobre los perdidos."),
        ("abc", "En Acuicultura: ¿qué es una meta de producción?", "Un valor que se espera alcanzar y con el que se comparan los datos", "El dato más alto que se registró en el criadero", "El nombre del lote que se analiza", "La meta es el valor esperado; el dato más alto o el nombre del lote no sirven para comparar."),
        ("=", "{F} ¿Cuál es la tasa de fecundación de la tanda 3? (en %)", "900*100//1500", "Se multiplican los fecundados por 100 y se dividen entre los puestos.", " %"),
        ("=", "{F} ¿Cuál es la tasa de eclosión de la tanda 2? (en %)", "1000*100//2000", "Se multiplican los eclosionados por 100 y se dividen entre los fecundados.", " %"),
        ("abc", "{F} ¿Qué tanda quedó bajo la meta de fecundación?", "La tanda 3", "La tanda 1", "La tanda 2", "Solo la tanda 3 tiene 60 %, bajo el 70 % de la meta; las otras tienen 80 %."),
        ("abc", "{F} ¿Qué tanda quedó bajo la meta de eclosión?", "La tanda 2", "La tanda 3", "La tanda 1", "La tanda 2 eclosionó 50 %, bajo el 65 % de la meta; la 1 tiene 75 % y la 3 tiene 80 %."),
        ("=", "{F} ¿Cuántos huevos fecundados hubo entre las tres tandas?", "1600+2000+900", "Se suman los huevos fecundados de las tres tandas.", " huevos"),
        ("abc", "{F} Un técnico dice que la baja fecundación de la tanda 3 se debe a la calidad de los reproductores. ¿Qué conclusión es adecuada?", "Es una causa probable que hay que comprobar con más registros", "Queda demostrado, porque el resultado fue bajo", "No puede haber ninguna relación entre ambos datos", "Un solo registro permite plantear una causa probable, pero no probarla."),
        ("=", "{F} ¿Cuántos huevos eclosionaron entre las tres tandas?", "1200+1000+720", "Se suman los huevos eclosionados de las tres tandas.", " huevos"),
        ("abc", "{F} ¿Qué corresponde hacer primero con el dato de la tanda 2?", "Informarlo al técnico con el registro como respaldo", "Subir el dato a 65 % para cumplir la meta", "Dejar de anotar esa tanda en el registro", "Un dato bajo la meta se informa; cambiarlo u ocultarlo impide mejorar."),
        ("=", "{F} Si la meta de fecundación de 70 % se aplicara a los huevos puestos de la tanda 2, ¿cuántos huevos fecundados serían como mínimo?", "2500*70//100", "Se multiplican los huevos puestos por 70 y se dividen entre 100.", " huevos"),
        ("abc", "{F} Una compañera propone anotar 70 % en la tanda 3 para que cumpla. ¿Qué respondes?", "Que los datos reales no se cambian: se deja 60 % y se informa", "Que sí, si lo corrige después", "Que sí, porque el 70 % es la meta", "Cambiar un dato oculta el problema y hace perder la trazabilidad."),
    ],
    ctx=("abc", "La jefa de un criadero de ejemplo te pide rellenar con números inventados una tanda que no se registró. ¿Qué haces?", "No inventar datos y avisar a un adulto responsable, como tu profesor o profesora de especialidad", "Inventar solo los números más bajos", "Inventarlos y avisar después", "Inventar datos falsifica el registro; ante la presión se consulta a un adulto responsable."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula la tasa de eclosión?", "Eclosionados × 100 ÷ fecundados", "La eclosión se mide sobre los huevos fecundados."),
        ("¿Qué es una causa probable?", "Una explicación posible que hay que comprobar", "Una causa probable se verifica con más datos."),
        ("¿Qué se hace con un dato bajo la meta?", "Se informa al técnico sin cambiarlo", "El dato real permite tomar decisiones."),
    ],
    op=("Ficha de ejemplo: tanda de «especie B», 4.000 huevos puestos, 3.000 fecundados y 1.800 eclosionados. Metas de ejemplo: fecundación 70 %, eclosión 65 %. Escribe (a) la tasa de fecundación, (b) la tasa de eclosión, (c) cuál meta se cumple y cuál no, (d) una causa probable del resultado más bajo, indicando que hay que comprobarla.",
        "(a) 3.000 × 100 ÷ 4.000 = 75 %. (b) 1.800 × 100 ÷ 3.000 = 60 %. (c) La fecundación cumple, porque 75 es mayor que 70; la eclosión no, porque 60 es menor que 65. (d) Una causa probable es que alguna condición del agua o del origen de los huevos no fuera adecuada; hay que comprobarlo con más registros.",
        ["calcula la tasa de fecundación", "calcula la tasa de eclosión", "compara con cada meta", "presenta la causa como probable"],
        ["hoja con las cuatro respuestas"],
        ["dividir la eclosión entre los huevos puestos", "tomar la causa como segura", "olvidar comparar con la meta"],
        "Pregunta: «¿sobre qué cantidad se calcula la eclosión?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una tanda con huevos puestos, fecundados y eclosionados, y calcula las dos tasas.",
    extend="Explica por qué la tasa de eclosión se calcula sobre los huevos fecundados y no sobre los puestos.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (registro de ejemplo, inventado). Estanque E-1 del Criadero Demo: volumen de 40 m3, 50 reproductores de «especie A» con peso medio de 4 kg cada uno. "
     "Densidad máxima del plan de ejemplo para planilla: 6 kg por m3. Ración diaria de ejemplo: 2 % de la biomasa.")
build(
    O1, 4, F,
    use="Aprenderé a calcular la biomasa, la densidad y la ración diaria de un estanque de reproductores con datos de ejemplo y a compararlas con el plan.",
    prior=["Sé qué es un reproductor y un lote.", "Sé multiplicar, dividir y calcular un porcentaje con números enteros.", "Sé comparar un dato con un máximo."],
    explain=[
        "La biomasa es el peso total de los animales de una unidad de cultivo y se calcula multiplicando el número de animales por su peso medio. La densidad de cultivo es la biomasa dividida por el volumen del estanque, y se expresa en kilos por metro cúbico (kg/m3). Para decidir se compara la densidad con el máximo que fija el plan de manejo, el documento donde el técnico escribe cuántos animales caben y qué cuidados corresponden.",
        "La ración diaria es la cantidad de alimento de un día; muchas veces se fija como un porcentaje de la biomasa. Por ejemplo, un grupo de 10 animales de 2 kg tiene 20 kg de biomasa, y una ración de 5 % sería 1 kg. Si la densidad supera el máximo, no se improvisa: se informa al técnico, que decide con el plan de manejo si hace falta otra unidad de cultivo.",
        f"Todos los números de esta clase son de ejemplo para una planilla: los valores reales dependen de la especie y de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("biomasa", "peso total de los animales de una unidad de cultivo"), ("peso medio", "peso promedio de un animal del grupo"), ("densidad de cultivo", "biomasa dividida por el volumen, en kg por m3"), ("plan de manejo", "documento que fija cuántos animales caben y qué cuidados se hacen"), ("ración diaria", "cantidad de alimento de un día, a menudo un porcentaje de la biomasa"), ("unidad de cultivo", "estanque, jaula u otro recipiente donde viven los animales")],
    worked=[
        ("Calcular densidad", "Un estanque de ejemplo de 5 m3 tiene 10 animales de 2 kg cada uno. ¿Cuál es su densidad?", ["Biomasa: 10 × 2 = 20 kg.", "Densidad: 20 ÷ 5 = 4 kg por m3."], "4 kg por m3"),
        ("Calcular ración", "La biomasa de un grupo de ejemplo es 300 kg y la ración es 3 % de la biomasa. ¿Cuántos kilos se indican por día?", ["300 × 3 = 900.", "900 ÷ 100 = 9."], "9 kg por día"),
    ],
    mistakes=[("Calcular la densidad dividiendo el número de animales entre el volumen, sin usar el peso.", "La densidad de cultivo del plan se expresa en peso por volumen, no en cantidad.", "Primero se calcula la biomasa y luego se divide entre el volumen."),
              ("Entregar más ración «porque los animales tienen hambre» sin consultar el plan.", "La ración la fija el plan; cambiarla a criterio propio altera el cultivo.", "Si hay dudas, se consulta al técnico antes de cambiar nada.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la biomasa de un estanque?", "El peso total de los animales que contiene", "El número de animales que contiene", "El volumen de agua del estanque", "La biomasa es peso total; el número de animales y el volumen son otros datos."),
        ("abc", "En Acuicultura: ¿qué es la densidad de cultivo?", "La biomasa dividida por el volumen, en kg por m3", "El número de estanques de un criadero", "El peso de un solo animal", "La densidad relaciona la biomasa con el volumen disponible."),
        ("abc", "En Acuicultura: ¿qué es una ración diaria?", "La cantidad de alimento que se entrega en un día", "El total de animales alimentados en un año", "El horario de apertura del criadero", "La ración mide alimento por día; los otros datos no lo miden."),
        ("=", "{F} ¿Cuántos kg de biomasa tiene el estanque?", "50*4", "Se multiplica el número de reproductores por el peso medio.", " kg"),
        ("=", "{F} ¿Cuál es la densidad del estanque, en kg por m3?", "50*4//40", "Se divide la biomasa entre el volumen del estanque.", " kg por m3"),
        ("=", "{F} ¿Cuántos kg de margen hay entre la biomasa actual y la biomasa máxima que permite la densidad máxima del plan?", "6*40-200", "Se calcula la biomasa máxima (densidad máxima por volumen) y se resta la biomasa actual.", " kg"),
        ("=", "{F} ¿Cuántos reproductores más de 4 kg cabrían sin superar la densidad máxima?", "40//4", "Se divide el margen de biomasa de 40 kg entre el peso medio.", " reproductores"),
        ("=", "{F} ¿Cuántos kg de alimento indica la ración diaria?", "200*2//100", "Se multiplica la biomasa por 2 y se divide entre 100.", " kg"),
        ("=", "{F} Se traslada a otro estanque a 10 reproductores. ¿Cuál es la nueva densidad, en kg por m3?", "(50-10)*4//40", "Se calcula la nueva biomasa con 40 reproductores y se divide entre el volumen.", " kg por m3"),
        ("abc", "{F} Se agregan 20 reproductores de 4 kg al estanque. ¿Qué ocurre con la densidad?", "Sube a 7 kg por m3 y supera el máximo del plan, por lo que se informa al técnico", "Baja a 4 kg por m3 y queda dentro del plan", "Se mantiene en 5 kg por m3 porque el volumen no cambia", "La biomasa sube a 280 kg; entre 40 m3 da 7, sobre el máximo de 6."),
        ("abc", "{F} ¿Quién decide trasladar reproductores entre estanques?", "El técnico, según el plan de manejo, con personal autorizado", "Cualquier compañero que vea el estanque lleno", "La persona que llegó primero esa mañana", "Las decisiones de manejo las toma quien tiene la responsabilidad técnica, no cualquier persona."),
        ("abc", "{F} Una persona propone entregar el doble de ración «porque los reproductores se ven flacos». ¿Qué corresponde?", "Seguir el plan y consultar al técnico si hay una duda", "Entregar el doble porque no pasa nada", "Dejar sin alimento ese día para compensar", "La ración se cambia solo por decisión técnica documentada."),
        ("abc", "{F} Para calcular la densidad, además del peso y la cantidad de reproductores, ¿qué dato hace falta?", "El volumen del estanque", "La temperatura ambiente de la bodega", "El nombre del proveedor", "La densidad en kg por m3 necesita el volumen."),
    ],
    ctx=("abc", "Un amigo que cultiva en su casa te pide que le confirmes por mensaje cuántos animales puede poner en su estanque. ¿Qué respondes?", "Que no puedes decidirlo por él: depende de la especie, del plan de manejo y de la norma, y que consulte a un técnico autorizado", "Que ponga todos los que quepan", "Que ponga el doble porque son pequeños", "La cantidad la fija el plan de manejo, no una opinión sin datos."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula la biomasa?", "Número de animales por peso medio", "La biomasa es el peso total del grupo."),
        ("¿En qué unidad se expresa la densidad de cultivo del ejemplo?", "En kg por m3", "Relaciona la biomasa con el volumen."),
        ("¿Qué se hace si la densidad supera el máximo del plan?", "Se informa al técnico", "La decisión de mover animales la toma el técnico."),
    ],
    op=("Ficha de ejemplo: estanque E-2 de 30 m3 con 20 reproductores de «especie B» de 6 kg cada uno. Densidad máxima del plan de ejemplo: 5 kg por m3. Ración de ejemplo: 5 % de la biomasa. Escribe (a) la biomasa, (b) la densidad, (c) si cumple el máximo del plan y cuántos kg de margen tiene, (d) los kg de ración diaria.",
        "(a) 20 × 6 = 120 kg. (b) 120 ÷ 30 = 4 kg por m3. (c) Cumple, porque 4 es menor que 5; la biomasa máxima sería 5 × 30 = 150 kg, así que hay 30 kg de margen. (d) 120 × 5 ÷ 100 = 6 kg.",
        ["calcula la biomasa", "calcula la densidad", "compara con el máximo y el margen", "calcula la ración"],
        ["hoja con las cuatro respuestas"],
        ["dividir la cantidad de animales entre el volumen", "olvidar el máximo del plan", "confundir ración con biomasa"],
        "Pregunta: «¿qué dato falta para pasar de biomasa a densidad?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un estanque con volumen, cantidad de animales y peso medio, y calcula su biomasa y su densidad.",
    extend="Explica por qué la densidad que fija el plan no la decide cada trabajador por su cuenta.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Criadero Demo evalúa comprar 40 reproductores de «especie A». Opción 1: $50.000 cada uno (de ejemplo), con certificado de origen y sanidad; "
     "costo de la cuarentena: $200.000 en total. Opción 2: $35.000 cada uno, sin certificado de origen ni de sanidad. Pérdida de ejemplo si un lote sin certificado trae una enfermedad: $3.000.000.")
build(
    O1, 5, F,
    use="Aprenderé a comparar dos alternativas de compra de reproductores con costos y bioseguridad, y a verificar la calidad de un registro antes de decidir.",
    prior=["Sé qué es la cuarentena y la trazabilidad.", "Sé multiplicar, sumar y dividir números enteros.", "Sé leer una ficha con costos."],
    explain=[
        "Comparar alternativas significa poner lado a lado las opciones con los mismos criterios: costo, documentos que las respaldan y riesgo. El costo total es la suma de todos los gastos de una opción; no basta mirar el precio por unidad. El certificado de origen y sanidad es el documento del proveedor que indica de dónde vienen los animales y su condición sanitaria; sin él no hay trazabilidad completa.",
        "Una opción más barata puede salir más cara si aumenta el riesgo de perder el lote, por lo que el riesgo también se compara. Verificar la calidad de un registro es comprobar que esté completo, con fecha y responsable, que las cifras cuadren y que coincida con los otros documentos; si algo no coincide se informa y no se corrige a escondidas. La decisión final la toma la jefatura con el técnico; el estudiante entrega la comparación escrita.",
        f"Los costos y las pérdidas de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("costo total", "suma de todos los gastos de una opción"), ("certificado de origen y sanidad", "documento del proveedor con la procedencia y la condición sanitaria de los animales"), ("alternativa", "una de las opciones entre las que hay que elegir"), ("criterio", "aspecto con que se comparan las opciones"), ("verificar", "comprobar que un dato o registro está completo y cuadra")],
    worked=[
        ("Costo total", "Una opción de ejemplo compra 10 animales a $20.000 cada uno y paga $30.000 de transporte. ¿Cuál es el costo total?", ["Animales: 10 × 20.000 = 200.000.", "Se suma el transporte: 200.000 + 30.000 = 230.000."], "$230.000"),
        ("Comparar con riesgo", "La opción X cuesta $100.000 y no tiene certificado; la opción Y cuesta $120.000 y sí lo tiene. ¿Por qué no se elige X solo por el precio?", ["X ahorra $20.000.", "Sin certificado no se puede comprobar el origen y el riesgo sanitario es mayor."], "Porque el ahorro no compensa la pérdida de trazabilidad y el mayor riesgo"),
    ],
    mistakes=[("Elegir la opción más barata sin revisar los documentos que la respaldan.", "El precio por unidad no incluye el riesgo ni los costos de bioseguridad.", "Compara costo total, documentos y riesgo."),
              ("Corregir en secreto una cifra que no cuadra entre dos documentos.", "Una corrección oculta impide saber cuál documento era el correcto.", "Se informa la diferencia al técnico con ambos documentos.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es el costo total de una opción de compra?", "La suma de todos los gastos de esa opción", "El precio de un solo animal", "La ganancia esperada al vender", "El costo total incluye todos los gastos, no solo el precio unitario."),
        ("abc", "En Acuicultura: ¿qué es un certificado de origen y sanidad?", "Un documento del proveedor con la procedencia y la condición sanitaria de los animales", "Un permiso para usar una embarcación", "Un registro de la alimentación diaria", "Ese certificado respalda el origen sanitario; los otros documentos tienen otras funciones."),
        ("abc", "En Acuicultura: ¿qué significa verificar un registro?", "Comprobar que está completo, tiene fecha y responsable y cuadra con otros documentos", "Copiarlo a mano con otra letra", "Guardarlo sin leerlo", "Verificar es comprobar; copiar o guardar no comprueba nada."),
        ("=", "{F} ¿Cuál es el costo total de la opción 1?", "40*50000+200000", "Se multiplica el precio por los 40 animales y se suma la cuarentena.", " pesos"),
        ("=", "{F} ¿Cuál es el costo de la opción 2?", "40*35000", "Se multiplica el precio por los 40 animales.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta la opción 1 que la opción 2?", "(40*50000+200000)-(40*35000)", "Se resta el costo de la opción 2 al de la opción 1.", " pesos"),
        ("abc", "{F} ¿Qué opción permite tener trazabilidad completa del origen de los animales?", "La opción 1, porque tiene certificado", "La opción 2, porque es más barata", "Ambas por igual", "La trazabilidad del origen la da el certificado, que solo tiene la opción 1."),
        ("abc", "{F} ¿Por qué la opción 2 no se elige automáticamente por ser más barata?", "Porque sin certificado no se puede comprobar el origen y aumenta el riesgo sanitario", "Porque el precio por animal de la opción 2 es mayor que el de la opción 1", "Porque la cuarentena solo se cobra en la opción 2", "El ahorro no compensa el riesgo cuando faltan los documentos."),
        ("=", "{F} Si la opción 2 trajera la enfermedad de ejemplo, ¿cuántos pesos más costaría que la opción 1 sumando la pérdida?", "(40*35000+3000000)-(40*50000+200000)", "Se suma la pérdida al costo de la opción 2 y se resta el costo de la opción 1.", " pesos"),
        ("abc", "{F} La guía de compra dice 40 animales y la ficha del lote anota 38. ¿Qué es lo más adecuado?", "Informar la diferencia al técnico con ambos documentos, sin cambiar números", "Cambiar la ficha a 40 sin avisar", "Esperar a que alguien lo note", "Una diferencia se informa con evidencia; corregirla a escondidas oculta el problema."),
        ("=", "{F} ¿Cuál es el costo por animal de la opción 1, contando la cuarentena?", "(40*50000+200000)//40", "Se divide el costo total de la opción 1 entre los 40 animales.", " pesos"),
        ("abc", "{F} ¿Quién toma la decisión final de compra y qué aporta el estudiante?", "La jefatura con el técnico; el estudiante aporta la comparación escrita", "El estudiante, porque hizo los cálculos", "El proveedor, porque conoce a los animales", "La decisión es de quien tiene la responsabilidad, y la comparación escrita la apoya."),
        ("abc", "{F} Una persona propone recibir los animales directo en la sala principal para ahorrar tiempo y saltarse la cuarentena. ¿Qué corresponde?", "Mantener la cuarentena, porque es una medida de bioseguridad", "Saltarla, porque el tiempo vale más", "Saltarla si los animales parecen sanos", "La cuarentena protege al resto de los animales aunque los recién llegados parezcan sanos."),
    ],
    ctx=("abc", "Un vendedor te ofrece animales muy baratos «sin papeles» para tu proyecto escolar. ¿Qué haces?", "Rechazo la oferta y lo consulto con mi profesor o profesora, porque sin documentos no hay trazabilidad", "Los compro y los mezclo con los demás", "Los compro si son más de diez", "Sin documentos no se puede asegurar el origen sanitario."),
    sc=[
        ("En Acuicultura: ¿qué es el costo total?", "La suma de todos los gastos de una opción", "El costo total incluye precio, transporte, cuarentena y otros gastos."),
        ("¿Qué documento respalda el origen sanitario?", "El certificado de origen y sanidad", "Sin él no hay trazabilidad completa."),
        ("¿Quién decide la compra final?", "La jefatura con el técnico", "El estudiante entrega la comparación escrita."),
    ],
    op=("Ficha de ejemplo: el criadero compara 20 reproductores de «especie B». Opción 1: $60.000 cada uno con certificado y $100.000 de cuarentena. Opción 2: $45.000 cada uno sin certificado. Escribe (a) el costo total de cada opción, (b) la diferencia, (c) dos criterios, además del costo, para comparar, (d) quién decide la compra final.",
        "(a) Opción 1: 20 × 60.000 + 100.000 = 1.300.000 pesos; opción 2: 20 × 45.000 = 900.000 pesos. (b) 1.300.000 − 900.000 = 400.000 pesos. (c) Documentos que respaldan el origen (certificado) y riesgo sanitario; también la trazabilidad. (d) La jefatura con el técnico.",
        ["calcula ambos costos", "calcula la diferencia", "nombra dos criterios", "indica quién decide"],
        ["hoja con las cuatro respuestas"],
        ["comparar solo el precio unitario", "olvidar la cuarentena", "decidir la compra por cuenta propia"],
        "Pregunta: «¿qué costo no aparece en el precio por unidad?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos opciones de compra con costos y calcula el costo total de cada una.",
    extend="Explica con un ejemplo cuándo una opción más barata sale más cara.",
)

O2 = "TP-ACUI-3y4-OAE-02"

# ============================================================ OAE-02, clase 1
F = ("Ficha 6 (caso de ejemplo, inventado). El centro ficticio «Centro Demo» cultiva 8.000 peces de «especie A» en una balsa jaula (estructura flotante con una red que contiene a los peces). "
     "Peligros anotados: trabajo sobre una estructura flotante con oleaje, cabos tensos, equipos eléctricos en la balsa, productos de uso sanitario en una bodega y trabajo con poca visibilidad al amanecer.")
build(
    O2, 1, F,
    use="Aprenderé qué labores de manejo existen en un centro de cultivo, qué es un plan de manejo y cómo se ordenan las medidas de prevención en esas labores.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé qué es la bioseguridad.", "Sé sumar, restar, multiplicar y dividir números enteros."],
    explain=[
        "El manejo de un cultivo reúne las labores con que se cuida a los animales hasta que están listos para la cosecha: la selección (separar a los animales según un criterio, como el tamaño), la alimentación, el desdoble (repartir un grupo en más unidades de cultivo para bajar la densidad), el muestreo (medir una parte del grupo para estimar el total) y los tratamientos (cuidados de salud indicados por un profesional). Todas se hacen según el plan de manejo, el documento que fija qué labores se realizan, cada cuánto y con qué parámetros.",
        "Los parámetros ambientales son las condiciones del agua que importan al cultivo, como la temperatura y el oxígeno disuelto (la cantidad de oxígeno que hay en el agua). Si salen del rango que fija el plan, los animales pueden sufrir daño, por lo que se registran y se informan. Una balsa jaula es una estructura flotante con una red donde viven los peces; trabajar sobre ella implica riesgos de caída al agua, golpes por cabos tensos y descargas eléctricas.",
        f"Para prevenir se aplica la jerarquía de controles: eliminar el peligro, sustituirlo, controles de ingeniería, controles administrativos y, al final, el EPP, que incluye el equipo de flotación. Los tratamientos y el uso de productos los hace solo personal autorizado, según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("manejo", "conjunto de labores con que se cuida a los animales de un cultivo"), ("selección", "separación de animales según un criterio, como el tamaño"), ("desdoble", "reparto de un grupo en más unidades de cultivo para bajar la densidad"), ("muestreo", "medición de una parte del grupo para estimar el total"), ("tratamiento", "cuidado de salud indicado por un profesional y aplicado por personal autorizado"), ("plan de manejo", "documento que fija qué labores se hacen, cada cuánto y con qué parámetros"), ("parámetro ambiental", "condición del agua que importa al cultivo, como la temperatura o el oxígeno disuelto"), ("oxígeno disuelto", "cantidad de oxígeno que hay en el agua"), ("balsa jaula", "estructura flotante con una red donde viven los peces")],
    worked=[
        ("Peligro y riesgo", "En un muelle de ejemplo hay un cabo tirante cruzando el pasillo. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el cabo tirante, que puede causar daño.", "El riesgo es que alguien tropiece, caiga o se golpee."], "Peligro: el cabo tirante; riesgo: que alguien tropiece, caiga o se golpee"),
        ("Clasificar un control", "Un centro de ejemplo entrega a cada trabajador un chaleco de flotación para su uso en el muelle. ¿A qué nivel de la jerarquía corresponde?", ["El chaleco protege solo a quien lo usa.", "Lo que protege a la persona y no quita el peligro es EPP."], "EPP"),
    ],
    mistakes=[("Creer que cambiar la ración o separar animales «a ojo» es parte del manejo de cualquiera.", "Las labores de manejo siguen el plan y las hace personal autorizado.", "Aprende el concepto y consulta el plan antes de cualquier decisión."),
              ("Creer que un chaleco de flotación elimina el peligro de caer al agua.", "El equipo de flotación es EPP: reduce el daño, pero el peligro sigue.", "Se suman controles de ingeniería, como barandas, y reglas de trabajo.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la selección de animales?", "Separarlos según un criterio, como el tamaño", "Entregarles alimento a todos por igual", "Contar los que murieron en la semana", "La selección separa por un criterio; alimentar y contar muertos son otras labores."),
        ("abc", "En Acuicultura: ¿qué es un desdoble?", "Repartir un grupo en más unidades de cultivo para bajar la densidad", "Juntar varios grupos en una sola unidad de cultivo", "Cambiar el nombre de un lote en el registro", "El desdoble reparte animales en más unidades; juntarlos subiría la densidad."),
        ("abc", "En Acuicultura: ¿qué es un muestreo?", "Medir una parte del grupo para estimar el total", "Pesar a todos los animales uno por uno cada día", "Elegir al azar qué documento se guarda", "El muestreo mide una parte para estimar el total sin medir a todos."),
        ("=", "Una jaula de ejemplo con 9.000 peces se divide en 3 jaulas con igual cantidad. ¿Cuántos peces quedan en cada una?", "9000//3", "Se divide el total de peces entre el número de jaulas.", " peces"),
        ("abc", "{F} ¿Cuál es el riesgo de trabajar sobre la balsa con oleaje?", "Que una persona pierda el equilibrio y caiga al agua", "La balsa misma, flotando en su lugar", "Que los peces coman menos esa mañana", "El riesgo es la posibilidad de daño; la balsa es el lugar y el apetito de los peces es otro asunto."),
        ("abc", "{F} Un chaleco de flotación usado por cada trabajador es un control de tipo:", "EPP, porque protege solo a quien lo usa", "De ingeniería, porque cambia la balsa", "De eliminación, porque quita el oleaje", "El chaleco no cambia el lugar ni elimina el peligro; protege a quien lo lleva."),
        ("abc", "{F} Una baranda perimetral fija en la balsa, instalada por personal autorizado, es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una norma escrita", "De EPP, porque protege a quien se acerca", "La baranda modifica la estructura y no depende de que cada persona la recuerde."),
        ("abc", "{F} Una regla escrita que suspende los trabajos sobre la balsa cuando el plan lo indica por condiciones del mar es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque modifica la balsa", "De EPP, porque protege el cuerpo", "Las reglas y suspensiones de trabajo son controles administrativos."),
        ("abc", "{F} Durante una visita de ejemplo, una persona cae al agua desde la balsa. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo ni entrar al agua, y avisar a un adulto responsable y a emergencias", "Lanzarte al agua para ayudarla de inmediato", "Esperar un rato a ver si logra salir sola", "Entrar al agua puede producir otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "{F} Un compañero dice: «con solo leer la ficha puedo aplicar un producto de uso sanitario a los peces». ¿Qué respuesta es correcta?", "Es falso: los tratamientos los hace personal autorizado según la norma vigente", "Es cierto, si usa guantes", "Es cierto, si lo hace de noche", "Leer una ficha no habilita para aplicar productos; los guantes o la hora no cambian eso."),
        ("=", "En el Centro Demo trabajan 36 personas y a cada charla de seguridad caben 12. ¿Cuántas charlas se necesitan para que todas asistan?", "36//12", "Se divide el total de personas entre las que caben en cada charla.", " charlas"),
        ("abc", "En Acuicultura: ¿qué documento fija qué labores de manejo se hacen, cada cuánto y con qué parámetros?", "El plan de manejo", "La guía de despacho", "El certificado de seguridad del chaleco", "El plan de manejo define labores y parámetros; los otros documentos tienen otra función."),
        ("abc", "En Acuicultura: ¿por qué se vigila el oxígeno disuelto al hacer labores de manejo?", "Porque valores fuera del rango del plan pueden dañar a los animales", "Porque el oxígeno disuelto indica el precio del alimento", "Porque solo se registra para llenar la planilla", "Los parámetros ambientales fuera de rango pueden afectar la salud de los animales."),
    ],
    ctx=("abc", "Una compañera te propone ayudarle el fin de semana en la bodega de un centro de cultivo, donde «solo hay que mezclar unos productos». ¿Qué respondes?", "Que no, porque manipular productos exige personal autorizado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque con guantes basta", "Que sí, si la mezcla es pequeña", "El tamaño de la mezcla y los guantes no reemplazan la autorización ni la norma."),
    sc=[
        ("En Acuicultura: ¿qué es un muestreo?", "Medir una parte del grupo para estimar el total", "El muestreo evita medir uno por uno a todos los animales."),
        ("¿Qué es un desdoble?", "Repartir un grupo en más unidades de cultivo para bajar la densidad", "El desdoble reduce la cantidad de animales por unidad."),
        ("¿Quién aplica los tratamientos?", "Personal autorizado, según la norma vigente", "Los tratamientos exigen personal autorizado y norma vigente."),
    ],
    op=("El centro ficticio «Centro Demo» anota una tarea de ejemplo: subir a la balsa al amanecer con poca visibilidad para revisar la bodega. Escribe (a) el peligro y el riesgo asociado, (b) un control administrativo, (c) un control de ingeniería, (d) qué EPP se suma y por qué no basta como único control.",
        "(a) Peligro: poca visibilidad sobre una estructura flotante; riesgo: que una persona tropiece y caiga al agua. (b) Una regla escrita que solo permita subir con luz suficiente y en compañía. (c) Barandas fijas y alumbrado instalados por personal autorizado. (d) El equipo de flotación; no basta porque es la última barrera y no quita el peligro.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer solo el EPP", "no mencionar el equipo de flotación"],
        "Pregunta: «¿qué control cambia el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el último párrafo."),
    reinforce="Escribe las cinco labores de manejo y una frase propia que explique cada una.",
    extend="Explica por qué un equipo de flotación no reemplaza una baranda fija.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 7 (registro de ejemplo, inventado). Centro Demo, jaula J-1 con 8.000 peces de «especie A». Muestreo de 10 peces, pesos en gramos: 350, 380, 400, 420, 360, 440, 390, 410, 370 y 380. "
     "Documentos del centro: el plan de manejo, el registro de muestreo (fecha, jaula, cantidad medida, pesos y responsable) y la bitácora de tratamientos (qué producto, quién lo indicó, quién lo aplicó y cuándo).")
build(
    O2, 2, F,
    use="Aprenderé los conceptos de muestra, peso medio y representatividad, los documentos de las labores de manejo y los roles de quienes las ejecutan.",
    prior=["Sé qué es un muestreo y un plan de manejo.", "Sé calcular un promedio.", "Sé pasar de gramos a kilos con números enteros."],
    explain=[
        "En un muestreo se mide una muestra, es decir, una parte del grupo, y con ella se estima el peso medio, que es el promedio de los pesos: se suman los pesos y se dividen por la cantidad medida. Para estimar la biomasa se multiplica el número de animales por el peso medio; como 1 kg tiene 1.000 g, un peso en gramos se divide entre 1.000 para pasarlo a kilos. Una muestra es representativa cuando refleja al grupo y no solo a los más grandes o a los más pequeños.",
        "Los documentos dejan evidencia de lo que se hizo. El plan de manejo fija las labores. El registro de muestreo anota fecha, jaula, cuántos animales se midieron y sus pesos. La bitácora de tratamientos anota qué producto se usó, quién lo indicó y quién lo aplicó. Un registro útil nunca se borra ni se cambia para «verse mejor».",
        f"Los roles se reparten así: el jefe del centro organiza la producción, el técnico decide las labores según el plan, el prevencionista asesora en riesgos del trabajo y el personal autorizado ejecuta las labores que la norma le permite. {EMER} {AVISO}",
    ],
    vocab=[("muestra", "parte del grupo que se mide para estimar el total"), ("peso medio", "promedio de los pesos de los animales medidos"), ("representativa", "muestra que refleja al grupo completo"), ("registro de muestreo", "documento con fecha, jaula, cantidad medida, pesos y responsable"), ("bitácora de tratamientos", "registro de qué producto se usó, quién lo indicó y quién lo aplicó"), ("jefe del centro", "persona que organiza la producción del centro de cultivo")],
    worked=[
        ("Peso medio", "Cinco peces de ejemplo pesan 200, 220, 240, 260 y 280 gramos. ¿Cuál es el peso medio?", ["Suma: 200 + 220 + 240 + 260 + 280 = 1.200.", "Se divide entre 5: 1.200 ÷ 5 = 240."], "240 g"),
        ("Elegir el documento", "El técnico de un centro de ejemplo quiere saber quién aplicó un tratamiento y en qué fecha. ¿Qué documento consulta?", ["Quién, qué y cuándo del tratamiento son datos de un registro de tratamientos.", "Eso se anota en la bitácora de tratamientos."], "La bitácora de tratamientos"),
    ],
    mistakes=[("Medir solo a los peces más grandes porque «son más fáciles de ver».", "La muestra deja de representar al grupo y el peso medio sale mayor que el real.", "La muestra debe reflejar al grupo completo; el técnico define cómo elegirla."),
              ("Borrar un peso extraño de la planilla para que el promedio «se vea normal».", "Un dato real, aunque raro, es evidencia; borrarlo altera el registro.", "Se deja el dato y se informa al técnico para que decida.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es una muestra en un muestreo?", "Una parte del grupo que se mide para estimar el total", "El grupo completo, medido uno por uno", "El documento donde se guardan los pesos", "La muestra es una parte del grupo; el total y el documento son otras cosas."),
        ("abc", "En Acuicultura: ¿qué es el peso medio de un grupo?", "El promedio de los pesos de los animales medidos", "El peso del animal más grande", "El peso total del alimento entregado", "El peso medio es el promedio, no un valor extremo ni el alimento."),
        ("abc", "En Acuicultura: ¿para qué sirve la bitácora de tratamientos?", "Para anotar qué producto se usó, quién lo indicó y quién lo aplicó", "Para fijar el precio de venta de los peces", "Para medir el oxígeno disuelto cada día", "La bitácora deja evidencia de los tratamientos; el precio y el oxígeno son otros asuntos."),
        ("=", "{F} ¿Cuál es el peso medio de la muestra, en gramos?", "(350+380+400+420+360+440+390+410+370+380)//10", "Se suman los diez pesos y se dividen entre 10.", " g"),
        ("=", "{F} ¿Cuántos gramos separan al pez más liviano del más pesado de la muestra?", "440-350", "Se resta el peso menor al peso mayor.", " g"),
        ("abc", "{F} ¿Qué documento guarda los pesos medidos y quién los midió?", "El registro de muestreo", "La bitácora de tratamientos", "El plan de manejo", "El registro de muestreo anota pesos y responsable; la bitácora de tratamientos y el plan cumplen otras funciones."),
        ("=", "{F} Con el peso medio de la muestra, ¿cuántos kg de biomasa se estiman para la jaula J-1?", "8000*390//1000", "Se multiplica el número de peces por el peso medio y se pasa de gramos a kilos.", " kg"),
        ("abc", "{F} Un compañero propone medir solo a los 10 peces más grandes que ve cerca de la superficie. ¿Qué problema tiene?", "La muestra no representa al grupo y el peso medio sale mayor que el real", "Ninguno, porque 10 peces siempre alcanzan", "Que se necesitarían más gramos para medirlos", "Una muestra sesgada entrega un dato que no refleja a todo el grupo."),
        ("abc", "{F} ¿Qué rol del centro asesora en la prevención de riesgos del trabajo?", "El prevencionista", "El jefe del centro", "El personal autorizado que ejecuta las labores", "El prevencionista asesora en riesgos; el jefe organiza y el personal ejecuta."),
        ("=", "{F} Si se estima un peso medio de 400 g en lugar del calculado, ¿cuántos kg de biomasa se estimarían?", "8000*400//1000", "Se multiplica el número de peces por 400 g y se pasa a kilos.", " kg"),
        ("abc", "{F} El registro de muestreo no tiene fecha ni responsable. ¿Por qué es débil?", "Porque sin fecha ni responsable no se puede verificar ni seguir su historia", "Porque los muestreos no deben registrarse", "Porque solo vale si se escribe con computador", "La trazabilidad exige saber cuándo y quién anotó el dato."),
        ("abc", "{F} Un compañero dice: «leí la ficha, así que puedo hacer el muestreo yo solo». ¿Qué respuesta es correcta?", "Es falso: las labores de manejo las hace personal capacitado y autorizado; la ficha informa, no habilita", "Es cierto, porque el muestreo es solo anotar números", "Es cierto, si hay buen tiempo", "La ficha no reemplaza la formación, la autorización ni el equipo de flotación cuando corresponde."),
        ("abc", "{F} Un peso de la muestra parece muy distinto de los demás y alguien quiere borrarlo. ¿Qué corresponde?", "Dejar el dato anotado e informar al técnico para que decida", "Borrarlo para que el promedio se vea normal", "Cambiarlo por 390 para que cuadre", "Un dato real no se borra ni se cambia; el técnico decide qué hacer."),
    ],
    ctx=("abc", "Una compañera te propone anotar un muestreo «de memoria» porque no alcanzó a hacerlo, para que el registro de la semana esté completo. ¿Qué respondes?", "Que no, porque anotar datos que no se midieron es falsificar un registro, y que se lo contarás a un adulto responsable", "Que sí, pero con números parecidos a los de la semana pasada", "Que sí, si después hace el muestreo de verdad", "Un registro falso oculta la realidad, aunque después se corrija."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula el peso medio?", "Se suman los pesos y se divide por la cantidad medida", "El peso medio es un promedio."),
        ("¿Qué es una muestra representativa?", "Una que refleja al grupo completo", "Una muestra sesgada entrega un dato errado."),
        ("¿Qué se hace con un dato raro en el registro?", "Se deja y se informa al técnico", "Un dato real no se borra."),
    ],
    op=("Ficha de ejemplo: jaula J-2 con 5.000 peces de «especie B». Muestreo de 5 peces con pesos en gramos: 600, 640, 580, 620 y 660. Escribe (a) el peso medio, (b) la biomasa estimada en kg, (c) en qué documento se anota el muestreo y qué datos lleva, (d) por qué la muestra debe ser representativa.",
        "(a) 600 + 640 + 580 + 620 + 660 = 3.100; 3.100 ÷ 5 = 620 g. (b) 5.000 × 620 ÷ 1.000 = 3.100 kg. (c) En el registro de muestreo: fecha, jaula, cantidad medida, pesos y responsable. (d) Porque si solo refleja a los más grandes o a los más pequeños, el peso medio y la biomasa salen errados.",
        ["calcula el peso medio", "estima la biomasa en kg", "nombra el documento y sus datos", "explica la representatividad"],
        ["hoja con las cuatro respuestas"],
        ["olvidar pasar de gramos a kilos", "dividir por 10 en vez de por 5", "creer que cualquier muestra sirve"],
        "Pregunta: «¿qué pasaría con el promedio si midieras solo los peces más grandes?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un muestreo de cinco pesos en gramos, calcula su peso medio y estima la biomasa de 2.000 animales.",
    extend="Explica con un ejemplo por qué un muestreo no necesita medir a todos los animales.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 8 (registro de ejemplo, inventado). Centro Demo, jaula J-3, «especie A». Al inicio del periodo: 8.000 peces de 250 g. Al final: 7.600 peces de 350 g. Alimento entregado en el periodo: 1.320 kg. "
     "Metas de ejemplo: factor de conversión alimenticia (FCA) máximo de 3 y mortalidad máxima de 6 %. Jaula J-4 del mismo centro: 5.000 peces al inicio y 450 peces muertos en el periodo.")
build(
    O2, 3, F,
    use="Aprenderé a analizar el registro de un periodo de cultivo: calcular la ganancia de biomasa, el factor de conversión alimenticia y la mortalidad, y compararlos con las metas.",
    prior=["Sé calcular biomasa y peso medio.", "Sé calcular un porcentaje con números enteros.", "Sé pasar de gramos a kilos."],
    explain=[
        "Para analizar un periodo de cultivo se compara el inicio con el final. La ganancia de biomasa es la biomasa final menos la inicial. El factor de conversión alimenticia, FCA, indica cuántos kilos de alimento se usaron por cada kilo de biomasa ganada: se calcula alimento ÷ ganancia de biomasa, y un valor menor significa que el alimento se aprovechó mejor. La mortalidad es el porcentaje de animales que murieron: muertos × 100 ÷ animales iniciales.",
        "Los resultados se comparan con las metas del plan. Un resultado fuera de la meta es una desviación y se informa al técnico con los registros como respaldo. Una causa probable es una explicación posible que hay que comprobar con más datos, porque dos hechos que coinciden no prueban que uno cause el otro. Nunca se cambian cifras para que el resultado cumpla la meta.",
        f"Las decisiones sobre los animales las toman el técnico y la jefatura con personal autorizado; aquí solo analizas los datos de un registro escrito. {EMER} {AVISO}",
    ],
    vocab=[("ganancia de biomasa", "biomasa final menos biomasa inicial"), ("factor de conversión alimenticia (FCA)", "kilos de alimento usados por cada kilo de biomasa ganada"), ("mortalidad", "porcentaje de animales que murieron respecto de los iniciales"), ("desviación", "valor que queda fuera de la meta"), ("causa probable", "explicación posible que todavía hay que comprobar")],
    worked=[
        ("Calcular FCA", "En un periodo de ejemplo se entregan 600 kg de alimento y la biomasa gana 300 kg. ¿Cuál es el FCA?", ["FCA = alimento ÷ ganancia.", "600 ÷ 300 = 2."], "2"),
        ("Calcular mortalidad", "De 2.000 animales de ejemplo mueren 100. ¿Cuál es la mortalidad?", ["100 × 100 = 10.000.", "10.000 ÷ 2.000 = 5."], "5 %"),
    ],
    mistakes=[("Calcular la ganancia de biomasa restando el número de peces en vez de la biomasa.", "La ganancia es en kilos de biomasa, no en cantidad de peces.", "Primero se calcula la biomasa inicial y la final, y luego se restan."),
              ("Ajustar la mortalidad para que cumpla la meta.", "El dato real es la base para decidir.", "Se deja el dato y se informa al técnico.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es el factor de conversión alimenticia (FCA)?", "Los kilos de alimento usados por cada kilo de biomasa ganada", "El porcentaje de animales que murieron en el periodo", "El peso medio de los animales al inicio", "El FCA relaciona alimento con ganancia de biomasa."),
        ("abc", "En Acuicultura: ¿qué es la mortalidad de un periodo?", "El porcentaje de animales que murieron respecto de los iniciales", "El peso de los animales que murieron", "El número de jaulas con animales", "La mortalidad se expresa como porcentaje de los animales iniciales."),
        ("abc", "En Acuicultura: ¿qué indica un FCA menor?", "Que se aprovechó mejor el alimento para ganar biomasa", "Que los animales comieron más alimento", "Que murieron menos animales", "Un FCA bajo significa menos alimento por kilo ganado."),
        ("=", "{F} ¿Cuántos kg de biomasa tenía la jaula J-3 al inicio?", "8000*250//1000", "Se multiplica el número de peces por el peso medio y se pasa a kilos.", " kg"),
        ("=", "{F} ¿Cuántos kg de biomasa tenía la jaula J-3 al final?", "7600*350//1000", "Se multiplica el número de peces finales por el peso medio y se pasa a kilos.", " kg"),
        ("=", "{F} ¿Cuántos kg ganó la biomasa de la jaula J-3 en el periodo?", "7600*350//1000-8000*250//1000", "Se resta la biomasa inicial a la final.", " kg"),
        ("=", "{F} ¿Cuál es el FCA de la jaula J-3?", "1320//(7600*350//1000-8000*250//1000)", "Se divide el alimento entregado entre la ganancia de biomasa.", ""),
        ("=", "{F} ¿Cuál es la mortalidad de la jaula J-3, en %?", "(8000-7600)*100//8000", "Se calculan los peces muertos, se multiplican por 100 y se dividen entre los iniciales.", " %"),
        ("abc", "{F} ¿Qué resultado de la jaula J-3 cumple las metas de ejemplo?", "Cumple ambas, porque el FCA es 2 (máximo 3) y la mortalidad es 5 % (máximo 6 %)", "No cumple ninguna", "Cumple solo la de FCA", "FCA 2 es menor que 3 y mortalidad 5 % es menor que 6 %."),
        ("=", "{F} ¿Cuál es la mortalidad de la jaula J-4, en %?", "450*100//5000", "Se multiplican los muertos por 100 y se dividen entre los peces iniciales.", " %"),
        ("abc", "{F} La jaula J-4 quedó sobre la mortalidad máxima. ¿Qué corresponde hacer primero?", "Informar al técnico con el registro como respaldo", "Cambiar el dato a 6 % para que cumpla", "No anotar la mortalidad de esa jaula", "Una desviación se informa; cambiar u ocultar el dato impide corregir el problema."),
        ("abc", "{F} Se sospecha que la alta mortalidad de J-4 se debe a la temperatura del agua. ¿Qué conclusión es adecuada?", "Es una causa probable que hay que comprobar con los registros del agua", "Queda demostrado porque el resultado fue alto", "No puede tener ninguna relación con el agua", "Una sospecha se verifica con datos antes de afirmarla."),
        ("abc", "{F} Una persona propone aumentar la ración de J-4 sin consultar al técnico «para recuperar peso». ¿Qué corresponde?", "Seguir el plan y consultar al técnico antes de cambiar la ración", "Aumentarla al doble porque no pasa nada", "Suspender la alimentación sin avisar", "Los cambios de ración los decide el técnico con el plan."),
    ],
    ctx=("abc", "El jefe de un centro de ejemplo te pide que cambies la mortalidad de una jaula en la planilla porque «se ve mal». ¿Qué haces?", "No alterar el registro y avisar a un adulto responsable, como tu profesor o profesora de especialidad", "Cambiar solo algunos números", "Cambiarlo y avisar después", "Alterar un registro oculta la realidad; ante la presión se consulta a un adulto responsable."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula el FCA?", "Alimento entregado ÷ ganancia de biomasa", "El FCA mide el aprovechamiento del alimento."),
        ("¿Cómo se calcula la mortalidad?", "Muertos × 100 ÷ animales iniciales", "La mortalidad se mide sobre los animales iniciales."),
        ("¿Qué es una causa probable?", "Una explicación posible que hay que comprobar", "Una causa probable se verifica con más datos."),
    ],
    op=("Ficha de ejemplo: jaula J-5 de «especie B»: 2.500 peces de 800 g al inicio y 2.400 peces de 1.000 g al final; alimento entregado 1.200 kg. Metas de ejemplo: FCA máximo de 4 y mortalidad máxima de 6 %. Escribe (a) la ganancia de biomasa en kg, (b) el FCA, (c) la mortalidad, (d) si cumple las metas.",
        "(a) Inicial: 2.500 × 800 ÷ 1.000 = 2.000 kg; final: 2.400 × 1.000 ÷ 1.000 = 2.400 kg; ganancia: 400 kg. (b) FCA: 1.200 ÷ 400 = 3. (c) Mortalidad: 100 × 100 ÷ 2.500 = 4 %. (d) Cumple ambas metas: 3 es menor que 4 y 4 % es menor que 6 %.",
        ["calcula la ganancia", "calcula el FCA", "calcula la mortalidad", "compara con las metas"],
        ["hoja con las cuatro respuestas"],
        ["restar peces en lugar de kilos", "dividir al revés el FCA", "calcular la mortalidad sobre los finales"],
        "Pregunta: «¿qué cantidad va en el denominador del FCA?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un periodo con peces iniciales, finales, pesos y alimento, y calcula la ganancia de biomasa y la mortalidad.",
    extend="Explica por qué un FCA bajo y una mortalidad alta pueden aparecer en la misma jaula.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 9 (registro de ejemplo, inventado). Centro Demo, jaula J-6 de «especie A»: volumen de 500 m3, 12.000 peces de 500 g cada uno. Densidad máxima del plan de ejemplo para planilla: 10 kg por m3. "
     "Ración diaria de ejemplo: 2 % de la biomasa. Precio de ejemplo del alimento: $1.500 por kg.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular la densidad de una jaula, compararla con el plan y estimar cuántos animales habría que repartir en otra unidad.",
    prior=["Sé calcular biomasa y densidad.", "Sé pasar de gramos a kilos.", "Sé calcular un porcentaje con números enteros."],
    explain=[
        "Para decidir si una unidad de cultivo está sobrecargada se aplica un criterio: se calcula la biomasa (animales × peso medio, pasando gramos a kilos), se divide entre el volumen para obtener la densidad y se compara con la densidad máxima del plan de manejo. La biomasa máxima de la unidad es la densidad máxima multiplicada por el volumen. La biomasa excedente es la que sobra sobre ese máximo.",
        "Si hay excedente, se puede estimar cuántos animales corresponden a esa biomasa dividiéndola entre el peso medio de un animal (en kilos). Ese número sirve para planificar en papel cuántos animales deberían repartirse en otra unidad (un desdoble); cómo se hace, cuándo y quién lo hace lo decide el técnico con personal autorizado, porque es una labor de riesgo. El estudiante solo calcula, anota el resultado y lo informa.",
        f"Los precios y las densidades de esta clase son de ejemplo para una planilla. {EMER} {AVISO}",
    ],
    vocab=[("densidad máxima", "máximo de kilos por metro cúbico que permite el plan de manejo"), ("biomasa máxima", "densidad máxima multiplicada por el volumen de la unidad"), ("biomasa excedente", "biomasa que sobra sobre la biomasa máxima"), ("sobrecargada", "unidad de cultivo cuya densidad supera el máximo del plan")],
    worked=[
        ("Biomasa máxima y excedente", "Una jaula de ejemplo de 100 m3 tiene 1.500 kg de biomasa y el máximo del plan es 12 kg por m3. ¿Cuánto sobra?", ["Biomasa máxima: 12 × 100 = 1.200 kg.", "Excedente: 1.500 − 1.200 = 300 kg."], "300 kg de excedente"),
        ("Animales para repartir", "Con 300 kg de excedente y animales de 2 kg cada uno, ¿cuántos animales habría que repartir?", ["Se divide el excedente entre el peso de cada animal.", "300 ÷ 2 = 150."], "150 animales"),
    ],
    mistakes=[("Repartir animales por cuenta propia apenas se calcula un excedente.", "El cálculo orienta, pero la decisión y la labor son del técnico y del personal autorizado.", "Anota el resultado e infórmalo al técnico."),
              ("Dividir el excedente en kilos entre el peso del animal en gramos.", "Las unidades no coinciden y el resultado sale mil veces distinto.", "Pasa el peso a kilos antes de dividir.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la densidad máxima del plan?", "El máximo de kg por m3 que permite el plan de manejo", "El número máximo de jaulas de un centro", "El peso máximo de un animal en la cosecha", "La densidad máxima limita los kg por m3 de una unidad."),
        ("abc", "En Acuicultura: ¿qué es la biomasa excedente?", "La biomasa que sobra sobre la biomasa máxima de la unidad", "La biomasa que falta para llegar al máximo", "El peso del alimento no consumido", "El excedente es la biomasa por encima del máximo; lo que falta es el margen."),
        ("abc", "En Acuicultura: ¿cómo se obtiene la biomasa máxima de una jaula?", "Multiplicando la densidad máxima por el volumen", "Sumando los pesos de los animales más grandes", "Dividiendo el volumen entre el peso medio", "La biomasa máxima se calcula con la densidad máxima y el volumen."),
        ("=", "{F} ¿Cuántos kg de biomasa tiene la jaula J-6?", "12000*500//1000", "Se multiplica el número de peces por su peso y se pasa a kilos.", " kg"),
        ("=", "{F} ¿Cuál es la densidad de la jaula J-6, en kg por m3?", "12000*500//1000//500", "Se divide la biomasa entre el volumen de la jaula.", " kg por m3"),
        ("=", "{F} ¿Cuál es la biomasa máxima que permite el plan para esta jaula?", "10*500", "Se multiplica la densidad máxima por el volumen.", " kg"),
        ("=", "{F} ¿Cuántos kg de biomasa excedente tiene la jaula?", "12000*500//1000-10*500", "Se resta la biomasa máxima a la biomasa actual.", " kg"),
        ("=", "{F} ¿A cuántos peces equivale el excedente? (peces de 500 g)", "(12000*500//1000-10*500)*1000//500", "Se pasa el excedente a gramos y se divide entre el peso de cada pez.", " peces"),
        ("=", "{F} Si se repartieran en otra jaula 2.000 peces, ¿cuál sería la densidad de J-6, en kg por m3?", "(12000-2000)*500//1000//500", "Se calcula la biomasa con 10.000 peces y se divide entre el volumen.", " kg por m3"),
        ("=", "{F} ¿Cuántos kg de alimento indica la ración diaria?", "12000*500//1000*2//100", "Se calcula la biomasa y se toma 2 % de ella.", " kg"),
        ("=", "{F} ¿Cuánto cuesta en pesos la ración de un día, con el precio de ejemplo del alimento?", "120*1500", "Se multiplican los kilos de la ración por el precio de cada kilo.", " pesos"),
        ("abc", "{F} Una persona calculó el excedente y propone repartir los peces de inmediato sin avisar a nadie. ¿Qué corresponde?", "Anotar el resultado e informar al técnico, que decide con personal autorizado", "Hacerlo de inmediato porque el cálculo ya está hecho", "Esperar a que otra persona lo haga sin comentarlo", "El cálculo orienta, pero la decisión y la labor son de personal autorizado."),
        ("abc", "{F} No hay otra jaula disponible y la densidad supera el máximo. ¿Qué es lo más adecuado?", "Informar al técnico para que decida con el plan de manejo", "Dejar los peces como están sin avisar", "Subir el máximo del plan en la planilla", "Cambiar el máximo del plan o callarse oculta el problema; la decisión es del técnico."),
    ],
    ctx=("abc", "Un conocido te pide que le calcules por mensaje cuántos peces debe «sacar» de su jaula en el mar para no pasarse del máximo. ¿Qué respondes?", "Que puedes practicar el cálculo en papel, pero que sacar peces es una labor de personas autorizadas y que debe consultar a un técnico", "Que los saque él mismo hoy", "Que saque la mitad sin medir", "El cálculo es conceptual; la labor en el mar exige autorización y equipo de seguridad."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula la biomasa máxima de una jaula?", "Densidad máxima × volumen", "La biomasa máxima depende de la densidad máxima y del volumen."),
        ("¿Qué es la biomasa excedente?", "La biomasa que sobra sobre el máximo", "El excedente es la parte que supera el máximo."),
        ("¿Quién decide repartir animales en otra unidad?", "El técnico, con personal autorizado", "Repartir animales es una labor de riesgo que exige autorización."),
    ],
    op=("Ficha de ejemplo: jaula J-7 de «especie B»: 200 m3 y 8.000 peces de 250 g. Densidad máxima del plan de ejemplo: 8 kg por m3. Escribe (a) la biomasa en kg, (b) la densidad, (c) la biomasa máxima y el excedente, (d) a cuántos peces equivale el excedente y quién decide qué hacer.",
        "(a) 8.000 × 250 ÷ 1.000 = 2.000 kg. (b) 2.000 ÷ 200 = 10 kg por m3. (c) Biomasa máxima: 8 × 200 = 1.600 kg; excedente: 2.000 − 1.600 = 400 kg. (d) 400 × 1.000 ÷ 250 = 1.600 peces; la decisión la toma el técnico con personal autorizado.",
        ["calcula la biomasa", "calcula la densidad", "calcula máximo y excedente", "interpreta quién decide"],
        ["hoja con las cuatro respuestas"],
        ["dividir en gramos y kilos mezclados", "decidir repartir los peces por cuenta propia", "olvidar el máximo del plan"],
        "Pregunta: «¿qué unidad usas para el peso del pez cuando divides?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una jaula con volumen, peces y peso, y calcula su biomasa y su densidad.",
    extend="Explica por qué calcular un excedente no autoriza a repartir los animales por cuenta propia.",
)
