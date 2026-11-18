"""Forestal TP 3.º y 4.º medio: OAE-01 (manejos culturales en vivero), clases 1 a 3. Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_fore_common import AVISO, EMER, build

O1 = "TP-FORE-3y4-OAE-01"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El vivero ficticio «Vivero Demo» produce plantas de «especie A» y «especie B» en bandejas, bajo una sombreadera (estructura de malla que da sombra). "
     "Peligros anotados: piso mojado y resbaladizo, herramientas manuales cortantes, una bodega con productos de uso sanitario, calor en verano y bandejas llenas que pesan 8 kg cada una (dato de ejemplo).")
build(
    O1, 1, F,
    use="Aprenderé qué es un vivero forestal, qué son los manejos culturales, cómo se distinguen peligro y riesgo y cómo se ordenan las medidas de prevención en un vivero.",
    prior=["Sé leer una ficha escrita y una lista de datos.", "Sé sumar, restar, multiplicar y dividir números enteros.", "Sé que las plantas necesitan luz, agua y temperatura adecuadas."],
    explain=[
        "Un vivero forestal es el lugar donde se producen plantas de especies forestales hasta que están listas para llevarlas al terreno. Allí se cuida la luminosidad (cuánta luz recibe la planta), la temperatura y la humedad que necesita cada especie en cada etapa de su vida; esa etapa se llama estado fenológico. Los manejos culturales son las labores de cuidado del cultivo: los hay nutricionales (alimentar a la planta), sanitarios (cuidar su salud) y ambientales (cuidar el entorno).",
        "Todo trabajo tiene peligros, es decir, fuentes de daño, y riesgos, que son la posibilidad de que ese daño ocurra. La jerarquía de controles ordena las medidas de prevención de la más a la menos efectiva: eliminar el peligro, sustituirlo por otro menor, aplicar controles de ingeniería (cambios físicos del lugar), aplicar controles administrativos (reglas, señales, horarios y capacitación) y, al final, el equipo de protección personal (EPP), que protege solo a quien lo usa y no quita el peligro.",
        f"Un vivero debe cumplir la normativa laboral y la ambiental, y por eso se documenta: hay hojas de datos de seguridad de los productos y registros del trabajo. Los productos de uso sanitario se guardan, se usan y se desechan solo según la norma vigente y por personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("vivero forestal", "lugar donde se producen plantas forestales hasta llevarlas al terreno"), ("estado fenológico", "etapa del ciclo de vida de la planta en que se encuentra"), ("manejo cultural", "labor de cuidado del cultivo, como controlar la luz, el agua o el orden de las plantas"), ("sombreadera", "estructura de malla que da sombra a las plantas"), ("peligro", "fuente con capacidad de causar daño"), ("riesgo", "posibilidad de que un peligro cause daño"), ("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Peligro y riesgo", "En un vivero de ejemplo hay una zanja de riego sin tapa junto al pasillo. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la zanja sin tapa, porque puede causar daño.", "El riesgo es que una persona que camina por el pasillo caiga dentro y se lastime."], "Peligro: la zanja sin tapa; riesgo: que alguien caiga en ella y se lastime"),
        ("Clasificar un control", "En un vivero de ejemplo se cambia un producto de uso sanitario por otro menos dañino. ¿A qué nivel de la jerarquía corresponde?", ["El peligro, el producto, no desaparece, pero se reduce.", "Reemplazar algo por otra cosa menos dañina es sustituir."], "Sustitución"),
    ],
    mistakes=[("Creer que usar guantes basta para trabajar seguro con cualquier producto.", "El EPP es la última barrera: no quita el peligro y protege solo a quien lo usa.", "Primero se elimina o se controla el peligro; el EPP se suma a esas medidas."),
              ("Creer que leer una ficha de vivero habilita para hacer las labores que describe.", "Las labores de riesgo exigen autorización, instructor y norma vigente.", "Aprende aquí el concepto y deja la labor a personal autorizado.")],
    T=[
        ("abc", "En Forestal: ¿qué es un vivero forestal?", "Un lugar donde se producen plantas forestales hasta que están listas para llevarlas al terreno", "Un predio donde se cosechan los árboles adultos para venderlos", "Una bodega donde se guardan las herramientas y los documentos de una faena", "El vivero produce las plantas; la cosecha y la bodega son otras instalaciones."),
        ("abc", "En Forestal: ¿qué es el estado fenológico de una planta?", "La etapa de su ciclo de vida en que se encuentra", "La cantidad de agua que recibe cada día", "El tipo de envase en que está creciendo", "El estado fenológico indica la etapa de vida; el agua y el envase son otros factores del manejo."),
        ("abc", "En Forestal: ¿qué son los manejos culturales de un vivero?", "Las labores de cuidado del cultivo, como controlar la luz, el agua y el orden de las plantas", "Los permisos que autorizan vender plantas a otras empresas", "Los dibujos que muestran cómo se ubican las bandejas", "Los manejos culturales son labores de cuidado; los permisos y los dibujos son documentos."),
        ("=", "En el vivero de ejemplo trabajan 45 personas y a cada charla de seguridad caben 15. ¿Cuántas charlas se necesitan para que todas asistan?", "45//15", "Se divide el total de personas entre las que caben en cada charla.", " charlas"),
        ("abc", "{F} Una cubierta fija y antideslizante sobre el pasillo mojado, instalada por personal autorizado, es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla escrita", "De EPP, porque protege a quien camina", "La cubierta modifica el lugar y no depende de que cada persona la recuerde."),
        ("abc", "{F} Un letrero que dice «piso mojado, avance con precaución» es un control de tipo:", "Administrativo, porque informa y ordena una conducta", "De ingeniería, porque cambia el piso", "De eliminación, porque quita el agua", "Un letrero solo informa; no cambia el piso ni quita el agua."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la bodega con productos de uso sanitario?", "Que una persona sufra daño por contacto con un producto", "El producto guardado en sus envases", "Que falte espacio para ordenar las bandejas", "El riesgo es la posibilidad de daño; el producto guardado es el peligro, y el espacio es un problema de orden."),
        ("abc", "{F} Una estudiante dice: «leí la ficha, así que puedo aplicar un producto de uso sanitario en el vivero». ¿Qué respuesta es correcta?", "Es falso: aplicar productos exige personal autorizado, norma vigente y EPP", "Es cierto, si usa guantes", "Es cierto, si otra persona la mira", "Leer una ficha no habilita para una tarea de riesgo; guantes o compañía tampoco."),
        ("abc", "Durante una visita de ejemplo a un vivero, una estantería con bandejas se vuelca y una persona queda atrapada. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a levantar la estantería para sacarla", "Tirar de la ropa de la persona para sacarla rápido", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "En Forestal: ¿por qué sustituir un peligro es mejor que entregar guantes a todo el personal?", "Porque la sustitución reduce el peligro en su origen y los guantes protegen solo a quien los usa", "Porque los guantes eliminan el peligro por completo, pero son más caros", "Porque la sustitución solo se usa cuando el EPP ya falló", "Los niveles altos de la jerarquía actúan sobre el peligro; el EPP no lo elimina."),
        ("=", "{F} Un carro de ejemplo admite como máximo 64 kg. ¿Cuántas bandejas llenas, de las que indica la ficha, caben como máximo?", "64//8", "Se divide la carga máxima del carro entre el peso de cada bandeja.", " bandejas"),
        ("abc", "{F} El jefe del vivero propone solo más pausas con agua para controlar el calor. ¿Qué medida de nivel más efectivo se podría sumar?", "Una sombra fija de malla sobre la zona de trabajo, que cambia el lugar", "Un recordatorio escrito en la pared sobre tomar agua", "Pedir a cada persona que lleve ropa adicional", "La sombra fija es un control de ingeniería; el recordatorio es del mismo nivel que las pausas y la ropa es EPP."),
        ("abc", "En Forestal: ¿qué institución fiscaliza el cumplimiento de la normativa laboral en una empresa forestal?", "La Dirección del Trabajo", "El Servicio de Impuestos Internos", "El Instituto Nacional de Estadísticas", "La Dirección del Trabajo fiscaliza lo laboral; las otras instituciones tienen funciones tributarias y estadísticas."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por ayudar en su vivero mezclando unos productos que «ya sabes manejar porque lo viste en clases». ¿Qué respondes?", "Que no, porque esa tarea exige instructor autorizado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque con guantes basta", "Que sí, pero solo si la mezcla es pequeña", "Haber visto el concepto en clases no habilita para manipular productos; el tamaño de la mezcla tampoco."),
    sc=[
        ("En Forestal: ¿qué es un peligro?", "Una fuente que puede causar daño, como un piso resbaladizo", "El peligro es la fuente; el riesgo es la posibilidad de daño."),
        ("En el trabajo forestal: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
        ("¿Qué es un manejo cultural en un vivero?", "Una labor de cuidado del cultivo, como controlar la luz o el agua", "Los manejos culturales son labores de cuidado de las plantas."),
    ],
    op=("El vivero ficticio «Vivero Demo» anota una tarea de ejemplo: acarrear a mano bandejas llenas por un pasillo mojado. Peligros anotados: piso resbaladizo y bandejas pesadas. Escribe (a) cuál es el peligro del piso y cuál el riesgo asociado, (b) un control administrativo para el pasillo, (c) un control de ingeniería para el mismo pasillo, (d) por qué el EPP no basta.",
        "(a) Peligro: piso mojado y resbaladizo; riesgo: que la persona resbale, caiga y se lastime. (b) Un letrero de aviso y un horario de acarreo cuando el pasillo está seco. (c) Una superficie antideslizante fija o un drenaje que evite que el agua se acumule. (d) Porque el EPP es la última barrera: no quita el peligro y protege solo a quien lo usa. La tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "no aclarar que la tarea la hace personal autorizado"],
        "Pregunta: «¿qué control actúa sobre el pasillo y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el nivel de ingeniería."),
    reinforce="Escribe la jerarquía de controles en orden y pon junto a cada nivel un ejemplo inventado de un vivero.",
    extend="Explica con un ejemplo por qué una charla de seguridad es un control administrativo y no reemplaza una medida de ingeniería.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (registro de ejemplo, inventado). Vivero Demo, sector 1. Lote L-07 de «especie A»: 400 plantas, una por cavidad, en estado fenológico de crecimiento inicial. Una bandeja tiene 40 cavidades. "
     "Condiciones recomendadas de ejemplo para esa etapa: temperatura entre 15 y 25 grados; sustrato húmedo sin encharcar; sombra parcial. "
     "Documentos del vivero: la pauta de manejo (qué cuidados se hacen y cada cuánto), el registro diario de condiciones (las lecturas de cada día) y la ficha del lote (origen, cantidad y etapa).")
build(
    O1, 2, F,
    use="Aprenderé los conceptos de propagación, sustrato, lote y trazabilidad, los documentos de un vivero y los roles de quienes trabajan en él.",
    prior=["Sé qué es un vivero y qué es un manejo cultural.", "Sé leer un registro escrito.", "Sé restar y dividir números enteros."],
    explain=[
        "Las plantas de un vivero se obtienen por propagación. La propagación sexual parte de semillas; la vegetativa, de partes de una planta madre, como un trozo de tallo. Las semillas se hacen germinar en una cama o bandeja llamada almácigo, y las plantas jóvenes pueden pasarse después a un envase individual. El sustrato es el material en el que crecen las raíces, y cada cavidad es el hueco de una bandeja donde crece una planta.",
        "Un lote es un grupo de plantas de la misma especie, origen y fecha que se maneja junto. La trazabilidad es poder seguir la historia del lote: de dónde viene, qué cuidados recibió y cuántas plantas quedaron. Para eso sirven los documentos: la ficha del lote, la pauta de manejo y el registro diario. Un registro útil dice qué se midió, cuánto, cuándo y quién lo anotó, y nunca se borra ni se cambia para que «se vea mejor».",
        f"Cada rol tiene su función. El jefe de vivero organiza la producción y los plazos. El encargado técnico decide los cuidados de cada lote. El prevencionista asesora en prevención de riesgos. El personal autorizado ejecuta las labores que la norma le permite. {EMER} {AVISO}",
    ],
    vocab=[("propagación", "forma de obtener nuevas plantas, por semilla o por partes de una planta madre"), ("almácigo", "cama o bandeja donde germinan las semillas"), ("sustrato", "material en el que crecen las raíces de la planta"), ("cavidad", "hueco de una bandeja donde crece una planta"), ("lote", "grupo de plantas de igual especie, origen y fecha que se maneja junto"), ("trazabilidad", "posibilidad de seguir la historia de un lote"), ("pauta de manejo", "documento que dice qué cuidados se hacen y cada cuánto"), ("registro diario", "documento con las lecturas de cada día")],
    worked=[
        ("Contar bandejas", "Un lote de ejemplo tiene 300 plantas, una por cavidad, y cada bandeja tiene 50 cavidades. ¿Cuántas bandejas ocupa?", ["Cada bandeja contiene 50 plantas.", "300 dividido por 50 es 6."], "6 bandejas"),
        ("Elegir el documento", "El encargado de un vivero de ejemplo quiere saber de dónde vino un lote y cuántas plantas tenía al inicio. ¿Qué documento consulta?", ["Origen y cantidad son datos de identificación del lote.", "Eso se anota en la ficha del lote."], "La ficha del lote"),
    ],
    mistakes=[("Anotar una lectura incómoda con otro valor para que cumpla el rango.", "Un registro alterado hace perder la trazabilidad y oculta un problema real.", "Se anota el valor real, se marca como fuera de rango y se informa al encargado."),
              ("Creer que la ficha del lote reemplaza la pauta de manejo.", "La ficha identifica el lote; la pauta dice qué cuidados se hacen y cada cuánto.", "Consulta cada documento para lo que fue hecho.")],
    T=[
        ("abc", "En Forestal: ¿qué es la propagación vegetativa?", "Obtener nuevas plantas a partir de partes de una planta madre", "Obtener nuevas plantas únicamente a partir de semillas", "Mover plantas ya crecidas de un vivero a otro", "En la vegetativa no se usan semillas sino partes de la planta madre."),
        ("abc", "En Forestal: ¿qué es el sustrato de un vivero?", "El material en el que crecen las raíces de la planta", "El producto con que se cuida la salud de las plantas", "El agua que recibe la planta en cada riego", "El sustrato es el medio de las raíces; el agua y los productos son otros elementos del manejo."),
        ("abc", "En Forestal: ¿para qué sirve la ficha de un lote?", "Para identificar el lote y dar trazabilidad: especie, cantidad, origen y etapa", "Para fijar el precio de venta de cada planta", "Para autorizar el uso de una máquina", "La ficha del lote da trazabilidad; el precio y las autorizaciones son otros documentos."),
        ("=", "{F} ¿Cuántas bandejas ocupa el lote de la ficha?", "400//40", "Se divide el total de plantas entre las cavidades de cada bandeja.", " bandejas"),
        ("abc", "{F} ¿Qué documento de la ficha sirve para anotar día a día la temperatura que se observa?", "El registro diario de condiciones", "La pauta de manejo", "La ficha del lote", "El registro diario guarda las lecturas de cada día; la pauta dice qué cuidados hacer y la ficha identifica el lote."),
        ("abc", "{F} ¿Qué dato de la ficha indica el estado fenológico del lote?", "Crecimiento inicial", "Lote L-07", "Sombra parcial", "El estado fenológico es la etapa de vida, que la ficha nombra como crecimiento inicial."),
        ("abc", "{F} ¿Qué rol del vivero se dedica a asesorar en prevención de riesgos?", "El prevencionista", "El jefe de vivero", "El personal autorizado que ejecuta las labores", "El prevencionista asesora en riesgos; el jefe organiza la producción y el personal ejecuta labores."),
        ("=", "{F} Del lote se descartan 36 plantas por estar débiles. ¿Cuántas plantas quedan en el lote?", "400-36", "Se restan las plantas descartadas al total del lote.", " plantas"),
        ("abc", "{F} Una lectura de ejemplo de 27 grados queda por sobre el máximo recomendado. ¿Qué corresponde hacer con ese dato?", "Anotarlo tal cual, marcarlo como fuera de rango e informar al encargado técnico", "Anotar 25 para que cumpla el rango", "No anotarlo, porque el rango solo se revisa a fin de mes", "El valor real se registra e informa; cambiarlo o no anotarlo oculta el problema."),
        ("abc", "{F} Un compañero dice: «leí la ficha del lote, así que puedo manejar la propagación yo solo». ¿Qué respuesta es correcta?", "Es falso: los manejos los hace personal capacitado y autorizado; la ficha informa, no habilita", "Es cierto, porque la ficha trae toda la información", "Es cierto, si trabaja con guantes", "Una ficha no reemplaza la formación ni la autorización."),
        ("abc", "{F} Dos días seguidos el registro marca 27 y 28 grados. ¿Qué es lo más adecuado?", "Comunicar ambas lecturas al encargado con el registro como respaldo", "Esperar un mes por si se corrige sola", "Promediarlas con lecturas de la semana anterior para que no se note", "Un problema repetido se informa con evidencia; ocultarlo impide corregirlo."),
        ("=", "{F} El jefe pide entregar 520 plantas de especie A y solo existe el lote de la ficha. ¿Cuántas bandejas más de 40 plantas hay que producir?", "(520-400)//40", "Se calcula cuántas plantas faltan y se divide entre las que caben en cada bandeja.", " bandejas"),
        ("abc", "{F} Un registro dice solo «sustrato húmedo», sin fecha ni nombre de quien lo anotó. ¿Por qué es un registro débil?", "Porque sin fecha ni responsable no se puede seguir su historia ni verificarlo", "Porque la humedad del sustrato nunca debe anotarse", "Porque los registros solo valen si están escritos en computador", "La trazabilidad exige saber cuándo y quién anotó el dato."),
    ],
    ctx=("abc", "Una compañera te propone «arreglar» los números del registro diario antes de la visita de una revisora. ¿Qué respondes?", "Que no, porque un registro no se altera, y que cualquier duda se consulta con el encargado o un adulto responsable", "Que sí, pero solo los números más llamativos", "Que sí, si después se corrige en la próxima visita", "Alterar un registro oculta la realidad, aunque sea poco o temporal."),
    sc=[
        ("En Forestal: ¿qué es un lote?", "Un grupo de plantas de igual especie, origen y fecha que se maneja junto", "El lote permite manejar y seguir juntas a plantas de iguales características."),
        ("En el trabajo forestal: ¿qué es la trazabilidad?", "Poder seguir la historia de un lote", "La trazabilidad permite saber el origen y los cuidados de cada lote."),
        ("¿Qué se debe hacer con una lectura fuera de rango?", "Anotarla tal cual e informar al encargado", "Se registra el dato real para poder tomar decisiones."),
    ],
    op=("Ficha de ejemplo: lote L-12 de «especie B», 350 plantas en bandejas de 25 cavidades, etapa de crecimiento inicial, temperatura recomendada de ejemplo entre 12 y 22 grados. Una lectura del día marca 24. Escribe (a) cuántas bandejas ocupa el lote, (b) en qué documento se anota la lectura del día, (c) qué haces con la lectura de 24 y a quién la informas, (d) qué rol consultarías si dudas sobre un riesgo del trabajo.",
        "(a) 350 ÷ 25 = 14 bandejas. (b) En el registro diario de condiciones. (c) Se anota tal cual, 24, se marca como fuera de rango y se informa al encargado técnico del vivero. (d) Al prevencionista. Las labores las hace personal autorizado.",
        ["calcula bien las bandejas", "nombra el documento correcto", "no altera la lectura y la informa", "nombra el rol adecuado"],
        ["hoja con las cuatro respuestas"],
        ["dividir mal", "cambiar la lectura para que cumpla el rango", "confundir el rol del prevencionista con el del jefe"],
        "Pregunta: «¿qué pasa con la trazabilidad si se cambia el dato?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una ficha de lote de tres líneas (especie A o B, cantidad y etapa) y calcula las bandejas necesarias con 30 cavidades por bandeja.",
    extend="Explica con un ejemplo por qué el encargado técnico y el prevencionista no cumplen la misma función.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (registro de ejemplo, inventado). Vivero Demo, sector 2, «especie B». Rango de temperatura recomendado de ejemplo: 12 a 22 grados. "
     "Lecturas de la semana, una por día, en grados: lunes 18; martes 20; miércoles 23; jueves 24; viernes 21; sábado 19; domingo 15. "
     "Humedad del sustrato anotada por el técnico: lunes húmedo; miércoles seco; viernes húmedo. Riego registrado: lunes, miércoles y viernes.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un registro de condiciones: encontrar desviaciones, calcular un promedio, proponer causas probables y elegir medidas según la jerarquía de controles.",
    prior=["Sé qué es un registro diario y un rango recomendado.", "Sé sumar, restar y dividir números enteros.", "Sé la jerarquía de controles."],
    explain=[
        "Analizar un caso en papel significa leer los datos, compararlos con lo recomendado, decidir qué significan y proponer acciones. Una desviación es un valor que queda fuera del rango recomendado. El promedio de varios valores se calcula sumándolos y dividiendo por la cantidad de valores; por ejemplo, el promedio de 4, 6 y 8 es 6. Mirar el promedio ayuda a ver la tendencia, pero no reemplaza revisar cada día, porque un promedio normal puede esconder un día peligroso.",
        "Una causa probable es una explicación posible de la desviación que todavía hay que comprobar: dos hechos que coinciden un día no prueban que uno cause el otro. Para proponer medidas se usa la jerarquía de controles: primero actuar sobre el origen, luego los controles de ingeniería, después los administrativos y al final el EPP. Después de aplicar una medida se verifica con nuevos registros que el problema realmente bajó.",
        f"Estas decisiones las toman el encargado técnico y la jefatura con personal capacitado; aquí aprendes a razonar con los datos de un registro escrito. {EMER} {AVISO}",
    ],
    vocab=[("desviación", "valor que queda fuera del rango recomendado"), ("promedio", "suma de los valores dividida por la cantidad de valores"), ("causa probable", "explicación posible de un problema que todavía hay que comprobar"), ("tendencia", "dirección en que cambian los datos con el tiempo"), ("verificar", "comprobar con nuevos datos que una medida funcionó")],
    worked=[
        ("Detectar desviaciones", "Un rango de ejemplo va de 10 a 20 grados y las lecturas de cuatro días son 12, 21, 18 y 9. ¿Cuáles son desviaciones?", ["Se compara cada lectura con 10 y 20.", "21 supera el máximo y 9 está bajo el mínimo."], "21 y 9"),
        ("Promedio", "Cuatro lecturas de ejemplo son 10, 14, 16 y 20. ¿Cuál es su promedio?", ["Se suman: 10 + 14 + 16 + 20 = 60.", "Se divide entre 4: 60 ÷ 4 = 15."], "15 grados"),
    ],
    mistakes=[("Concluir que una desviación tiene una causa solo porque ocurrió el mismo día que otro hecho.", "Que dos hechos coincidan no prueba que uno cause el otro.", "Anótala como causa probable y compruébala con más datos."),
              ("Borrar una lectura alta para que el registro se vea mejor.", "El dato real es la base de cualquier decisión.", "Se deja el dato y se explica o se verifica con un instrumento calibrado.")],
    T=[
        ("abc", "En Forestal: ¿qué es una desviación en un registro de condiciones de vivero?", "Un valor que queda fuera del rango recomendado", "Cualquier valor anotado con lápiz", "El promedio de todos los días", "La desviación se define por salir del rango recomendado, no por cómo se anota."),
        ("abc", "En Forestal: ¿qué es una causa probable?", "Una explicación posible de la desviación que todavía hay que comprobar", "La sanción que se aplica a quien anotó el dato", "El rango recomendado de la especie", "La causa probable es una hipótesis que se verifica con más datos."),
        ("abc", "En Forestal: ¿cómo se calcula un promedio?", "Sumando los valores y dividiendo por la cantidad de valores", "Restando el valor menor al valor mayor", "Eligiendo el valor que se anotó primero", "El promedio es la suma dividida por la cantidad; restar menor y mayor da la diferencia entre ellos."),
        ("=", "{F} ¿Cuántos grados por sobre el máximo del rango estuvo la lectura más alta de la semana?", "24-22", "Se resta el máximo del rango a la lectura más alta.", " grados"),
        ("abc", "{F} ¿Qué días de la semana quedaron fuera del rango?", "Miércoles y jueves", "Solo el jueves", "Jueves y viernes", "El miércoles 23 y el jueves 24 superan el máximo de 22; el viernes marca 21, que cumple."),
        ("=", "{F} ¿Cuál fue el promedio de las siete lecturas de la semana?", "(18+20+23+24+21+19+15)//7", "Se suman las siete lecturas y se dividen por 7.", " grados"),
        ("abc", "{F} Una de las dos desviaciones coincide con humedad «seca» en el sustrato, el miércoles. ¿Qué conclusión es adecuada?", "Hay una relación posible que conviene verificar con más registros", "Queda demostrado que el calor siempre seca el sustrato", "No puede haber ninguna relación entre ambos datos", "Un solo día no prueba una relación, pero tampoco permite descartarla."),
        ("abc", "{F} ¿Qué medida frente al calor del sector se clasifica como control de ingeniería?", "Instalar una malla fija que dé más sombra al sector", "Pegar un cartel que recuerde revisar la temperatura", "Pedir al personal que use un sombrero", "La malla cambia el lugar; el cartel es administrativo y el sombrero es EPP."),
        ("=", "En el sector 3 de ejemplo las lecturas de cinco días son 14, 16, 18, 20 y 22 grados. ¿Cuál es su promedio?", "(14+16+18+20+22)//5", "Se suman las cinco lecturas y se dividen por 5.", " grados"),
        ("abc", "{F} Un compañero propone borrar la lectura del jueves porque «afea el registro». ¿Qué responde?", "Que los datos reales no se borran: se dejan y se explican", "Que sí, si anota el rango recomendado al lado", "Que sí, si pone 22 para que cumpla", "Borrar o cambiar un dato impide analizar el problema y hace perder la trazabilidad."),
        ("abc", "{F} El técnico sospecha que la lectura del jueves fue un error del instrumento. ¿Qué corresponde?", "Verificarla con un instrumento calibrado antes de concluir", "Descartarla sin revisar porque le parece alta", "Darla por cierta y no revisar el instrumento", "Descartar o aceptar sin verificar son ambas conclusiones sin evidencia."),
        ("abc", "{F} ¿Qué orden de acciones corresponde después de ver las dos desviaciones?", "Registrar y avisar, buscar causas probables, proponer controles de la jerarquía y verificar después con nuevos registros", "Proponer un control de inmediato, buscar la causa después y no verificar", "Esperar tres semanas más de lecturas antes de avisar a alguien", "Se informa de inmediato, se analiza, se actúa y se comprueba el resultado."),
        ("=", "{F} Supón que una sombra fija baja cada lectura 3 grados (dato de ejemplo). ¿Cuál sería el nuevo valor máximo de la semana?", "24-3", "Se resta la baja de 3 grados a la lectura más alta.", " grados"),
    ],
    ctx=("abc", "La jefa del vivero de ejemplo te pide cambiar algunos números del registro antes de que llegue una visita. ¿Qué haces?", "No alterar el registro y avisar a un adulto responsable, como tu profesor o profesora de especialidad", "Cambiar solo los números más altos", "Cambiarlos y avisar después", "Alterar un registro oculta la realidad; ante la presión se consulta a un adulto responsable."),
    sc=[
        ("En Forestal: ¿qué es una desviación?", "Un valor fuera del rango recomendado", "Desviación es salir del rango recomendado."),
        ("En el trabajo forestal: ¿cómo se calcula un promedio?", "Se suman los valores y se divide por la cantidad", "El promedio resume varios valores en uno."),
        ("En el trabajo forestal: ¿qué se hace después de aplicar una medida?", "Verificar con nuevos registros que funcionó", "Verificar permite saber si el problema bajó."),
    ],
    op=("Ficha de ejemplo: sector 4, «especie A», rango recomendado de 10 a 20 grados. Lecturas de ejemplo de seis días: 12, 14, 21, 17, 19, 25. Escribe (a) qué días son desviaciones y por cuántos grados superan el máximo, (b) el promedio de las seis lecturas, (c) una causa probable de las desviaciones, indicando que hay que comprobarla, (d) un control de ingeniería y un control administrativo.",
        "(a) Los días de 21 y de 25: superan el máximo en 1 y en 5 grados. (b) 12 + 14 + 21 + 17 + 19 + 25 = 108; 108 ÷ 6 = 18 grados. (c) Poca sombra en las horas de más calor; hay que comprobarlo con más registros. (d) Ingeniería: una malla fija de sombra; administrativo: un horario de riego en las horas frescas.",
        ["identifica las desviaciones y su magnitud", "calcula o interpreta el promedio", "presenta la causa como probable", "propone dos controles de niveles distintos"],
        ["hoja con las cuatro respuestas"],
        ["tomar la causa como segura", "olvidar las dos desviaciones", "proponer solo el EPP"],
        "Pregunta: «¿cómo sabrías que la causa es la correcta?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una semana de lecturas con dos desviaciones y calcula su promedio con cuatro días.",
    extend="Explica por qué un promedio normal puede ocultar un día fuera de rango.",
)
