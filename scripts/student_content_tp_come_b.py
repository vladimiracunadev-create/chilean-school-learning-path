"""Construcciones Metálicas TP 3.º y 4.º medio: OAE-04 (mecanizar y conformar: conceptos, hoja de ruta, ajustes, costos), OAE-05 (armar y montar: documentos, recepción, verificación) y OAE-06 (mantenimiento básico). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_come_common import AVISO, EMER, build

O4 = "TP-COME-3y4-OAE-04"
O5 = "TP-COME-3y4-OAE-05"
O6 = "TP-COME-3y4-OAE-06"

# ============================================================ OAE-04, clase 1
F = ("Ficha 14 (caso de ejemplo, inventado). El taller de mecanizado de «Estructuras Demo» tiene 12 máquinas: 4 taladros, 3 esmeriles, 2 sierras, 1 plegadora y 2 tornos. "
     "Peligros anotados: partes giratorias que pueden atrapar ropa o cabello, proyección de virutas y chispas, ruido, bordes filosos, aceite en el piso y piezas pesadas. "
     "Inspección de ejemplo: 9 de las 12 máquinas tienen su resguardo (cubierta física sobre la parte peligrosa) completo y 3 no. Cada máquina tiene un botón de parada de emergencia.")
build(
    O4, 1, F,
    use="Aprenderé qué es mecanizar y conformar piezas, qué peligros tienen las máquinas de un taller y cómo funcionan los resguardos, la parada de emergencia y la autorización de los operadores.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé calcular porcentajes sencillos.", "Sé que una tarea de riesgo exige autorización."],
    explain=[
        "Mecanizar es darle forma o medida a una pieza con máquinas y herramientas que retiran material; conformar es darle forma sin retirarlo, por ejemplo doblándolo. Un taller de este tipo tiene taladros, esmeriles, sierras, plegadoras y tornos. Sus peligros principales son las partes giratorias, que pueden atrapar ropa, cabello o manos; la proyección de virutas y chispas; el ruido; los bordes filosos; el aceite derramado y las piezas pesadas.",
        "El resguardo es una cubierta física que impide tocar una parte peligrosa en movimiento, y es un control de ingeniería: protege aunque la persona se descuide. La parada de emergencia detiene la máquina rápidamente, pero actúa cuando ya hay un problema y no reemplaza al resguardo. Los carteles y las reglas, como mantener el cabello recogido y no usar ropa suelta ni joyas cerca de partes giratorias, son controles administrativos, y el EPP, como los lentes y los protectores auditivos, es la última barrera.",
        f"Solo opera una máquina quien tiene formación y autorización; la norma vigente y el taller fijan las condiciones. Una máquina sin su resguardo completo se informa y no se usa. {EMER} {AVISO}",
    ],
    vocab=[("mecanizar", "dar forma o medida a una pieza retirando material con máquinas y herramientas"), ("conformar", "dar forma a una pieza sin retirar material, por ejemplo doblándola"), ("resguardo", "cubierta física que impide tocar una parte peligrosa en movimiento"), ("parada de emergencia", "botón que detiene la máquina rápidamente ante un peligro"), ("atrapamiento", "riesgo de que una parte en movimiento sujete ropa, cabello o manos"), ("operador autorizado", "persona con formación y permiso para operar una máquina")],
    worked=[
        ("Clasificar una medida", "Un taller de ejemplo cubre con una malla fija la correa de una máquina para que nadie pueda tocarla. ¿Qué tipo de control es?", ["La malla cambia físicamente la máquina.", "Una cubierta física es un control de ingeniería."], "De ingeniería"),
        ("Porcentaje con resguardo", "En otro taller de ejemplo, 14 de 20 máquinas tienen su resguardo completo. ¿Qué porcentaje es?", ["Se multiplican por 100 las máquinas con resguardo y se divide entre el total.", "14 por 100 son 1.400, y 1.400 entre 20 son 70."], "70 %"),
    ],
    mistakes=[("Creer que la parada de emergencia hace innecesario el resguardo.", "La parada actúa cuando el problema ya ocurrió; el resguardo evita el contacto desde antes.", "Usa los dos: primero el resguardo y, además, la parada."),
              ("Usar una máquina sin resguardo completo «solo por hoy».", "El peligro de atrapamiento existe igual y el riesgo aumenta.", "No la uses: informa al responsable y espera a personal autorizado.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es mecanizar una pieza?", "Darle forma o medida con máquinas y herramientas que retiran material", "Unir dos piezas con pernos", "Pintarla para protegerla de la corrosión", "Mecanizar trabaja la forma de la pieza; unir y pintar son otras etapas."),
        ("abc", "En Construcciones Metálicas: ¿qué es un resguardo de máquina?", "Una cubierta física que impide tocar una parte peligrosa en movimiento", "Un cartel que prohíbe acercarse", "Un guante que usa el operador", "El resguardo es una barrera física, distinta de un cartel o del EPP."),
        ("abc", "En Construcciones Metálicas: ¿para qué sirve la parada de emergencia de una máquina?", "Para detenerla rápido ante un peligro, sin reemplazar las demás medidas", "Para apagarla al terminar el turno", "Para reducir el ruido", "La parada sirve en una emergencia; no sustituye al resguardo."),
        ("=", "{F} ¿Cuántas máquinas hay en el taller sumando los cinco tipos?", "4+3+2+1+2", "Se suman taladros, esmeriles, sierras, plegadora y tornos.", " máquinas"),
        ("=", "{F} ¿Cuántas máquinas no tienen su resguardo completo?", "12-9", "Se resta al total las que sí lo tienen.", " máquinas"),
        ("=", "{F} ¿Qué porcentaje de las máquinas tiene su resguardo completo?", "9*100//12", "Se multiplican por 100 las máquinas con resguardo y se divide entre el total.", " %"),
        ("abc", "{F} ¿Qué tipo de control es el resguardo de una máquina?", "De ingeniería, porque cambia físicamente la máquina", "Administrativo, porque es una regla", "EPP, porque protege a la persona", "El resguardo actúa sobre la máquina y no depende de la persona."),
        ("abc", "{F} Un cartel pide mantener el cabello recogido y sin ropa suelta cerca de partes giratorias. ¿Qué es ese cartel?", "Un control administrativo; el peligro de atrapamiento sigue existiendo", "Un control de ingeniería, porque está pegado a la máquina", "Una eliminación del peligro", "Un cartel ordena una conducta; no quita la parte giratoria."),
        ("abc", "{F} Un operador retiró el resguardo de una sierra para «ver mejor» la pieza. ¿Qué corresponde?", "Informar al responsable: la máquina no se usa hasta que personal autorizado la deje con su resguardo completo", "Seguir con más cuidado, porque ve mejor", "Seguir si el operador tiene experiencia", "La experiencia no reemplaza el resguardo; el atrapamiento puede ocurrir igual."),
        ("abc", "Durante una visita de ejemplo, la manga de una persona queda atrapada en una parte giratoria de una máquina. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a soltar la manga", "Tirar de la persona para sacarla rápido", "Intervenir sin formación puede causar más daño; se avisa a quienes pueden actuar."),
        ("abc", "{F} ¿Por qué un resguardo es más efectivo que pedir al operador que «tenga cuidado»?", "Porque impide el contacto aunque la persona se descuide, sin depender de su atención", "Porque así el operador no necesita estar atento", "Porque el resguardo hace menos ruido", "Una barrera física protege incluso en un descuido."),
        ("=", "{F} Se reparan los resguardos de 2 de las 3 máquinas que no los tenían completos. ¿Cuántas máquinas quedan con resguardo completo?", "9+2", "Se suman las reparadas a las que ya tenían resguardo completo.", " máquinas"),
        ("abc", "{F} Un practicante dice que «el botón de parada de emergencia hace innecesarios los resguardos». ¿Qué respondes?", "Es falso: la parada actúa cuando ya ocurrió el problema y el resguardo lo evita desde antes", "Es cierto, porque detiene todo", "Es cierto, si se presiona rápido", "Una parada rápida no evita el primer contacto con la parte peligrosa."),
    ],
    ctx=("abc", "El jefe de turno te dice que uses un taladro sin su resguardo «porque el del repuesto no llegó». ¿Qué respondes?", "Que no lo usarás y que avisarás al responsable, porque una máquina sin resguardo completo no se opera", "Que lo usarás con mucho cuidado", "Que lo usarás si es solo un agujero", "El resguardo es una protección necesaria; la urgencia no la reemplaza."),
    sc=[
        ("En Construcciones Metálicas: ¿qué diferencia hay entre mecanizar y conformar?", "Mecanizar retira material; conformar da forma sin retirarlo", "La diferencia está en si se retira o no material."),
        ("En Construcciones Metálicas: ¿qué tipo de control es un resguardo?", "De ingeniería", "Es una barrera física sobre la máquina."),
        ("En Construcciones Metálicas: ¿quién puede operar una máquina?", "Solo una persona con formación y autorización", "La operación exige formación y permiso, no solo interés."),
    ],
    op=("Caso de ejemplo: otro taller tiene 25 máquinas y 20 con resguardo completo. Peligros anotados en una sierra: partes en movimiento, chispas y ruido. Escribe (a) qué porcentaje de las máquinas tiene resguardo completo, (b) un control de ingeniería para la sierra, (c) un control administrativo, (d) por qué la parada de emergencia no reemplaza al resguardo.",
        "(a) 20 × 100 ÷ 25 = 80 %. (b) Un resguardo fijo que cubra la hoja en movimiento. (c) Un cartel de uso solo por personal autorizado y una regla de no usarla sin resguardo. (d) Porque la parada actúa cuando el problema ya ocurrió y el resguardo lo evita desde antes.",
        ["calcula el porcentaje", "propone un control de ingeniería", "propone un control administrativo", "explica el límite de la parada"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre 20 en vez de entre 25", "proponer solo EPP", "decir que la parada reemplaza al resguardo"],
        "Pregunta: «¿qué evita el contacto antes de que ocurra?». Si no responde, pídele que relea la sección del resguardo."),
    reinforce="Escribe tres máquinas de un taller con un peligro y un control para cada una, indicando su nivel de la jerarquía.",
    extend="Explica con un ejemplo por qué la jerarquía de controles prefiere un resguardo a un cartel.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 15 (hoja de ruta de ejemplo, inventada) de la pieza «soporte S1»: operación 10, aserrado del perfil; 20, taladrado de 4 agujeros; 30, esmerilado de los bordes; 40, plegado de una aleta; control final. "
     "Tiempos de ejemplo por soporte: aserrado 6 min, taladrado 12 min, esmerilado 5 min, plegado 7 min. Se fabrican 24 soportes.")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario de las operaciones de mecanizado y conformado (taladrado, esmerilado, aserrado, plegado, cilindrado, doblado y forjadura) y a leer una hoja de ruta, sin aprender a ejecutarlas.",
    prior=["Sé qué es mecanizar y conformar.", "Sé multiplicar y sumar tiempos.", "Sé que la autorización es necesaria para operar máquinas."],
    explain=[
        "Cada operación tiene un nombre. El taladrado hace agujeros en una pieza con una broca que gira. El esmerilado desgasta un borde o una superficie con una muela abrasiva. El aserrado corta el material con una sierra. El plegado dobla una plancha en línea recta con una máquina llamada plegadora. El cilindrado da forma cilíndrica a una pieza que gira en un torno. El doblado curva barras o perfiles. La forjadura da forma al metal calentado golpeándolo. Aquí solo se aprende qué es cada una, no cómo se ejecuta.",
        "La hoja de ruta es el documento que ordena las operaciones de una pieza, indica la máquina de cada una y su tiempo, y termina con el control final. Se lee junto con el plano de la pieza, que fija medidas y tolerancias. Si la hoja de ruta parece tener un error de orden, no se corrige por cuenta propia: se registra y se consulta a quien la emitió. El tiempo total de una pieza es la suma de los tiempos de sus operaciones.",
        f"Cada máquina la opera personal formado y autorizado; el jefe de taller organiza el trabajo y un mantenedor autorizado la repara. {EMER} {AVISO}",
    ],
    vocab=[("taladrado", "hacer agujeros con una broca que gira"), ("esmerilado", "desgastar un borde o una superficie con una muela abrasiva"), ("aserrado", "cortar con una sierra"), ("plegado", "doblar una plancha en línea recta con una plegadora"), ("cilindrado", "dar forma cilíndrica a una pieza que gira en un torno"), ("doblado", "curvar barras o perfiles"), ("forjadura", "dar forma al metal calentado golpeándolo"), ("hoja de ruta", "documento que ordena las operaciones de una pieza y sus máquinas")],
    worked=[
        ("Reconocer una operación", "Una hoja de ruta de ejemplo dice «hacer agujeros de 8 mm con broca». ¿Qué operación es?", ["Se hacen agujeros con una broca que gira.", "Esa descripción corresponde al taladrado."], "Taladrado"),
        ("Tiempo de una pieza", "Una pieza de ejemplo pasa por operaciones de 4, 9 y 3 minutos. ¿Cuánto tarda en total?", ["Se suman los tiempos de las operaciones.", "4 más 9 más 3 son 16."], "16 minutos"),
    ],
    mistakes=[("Confundir plegado con aserrado.", "El plegado dobla la plancha; el aserrado la corta.", "Recuerda: plegar dobla y aserrar corta."),
              ("Corregir por cuenta propia el orden de una hoja de ruta.", "El orden lo fijó quien la emitió, y un cambio puede afectar la calidad o la seguridad.", "Registra la duda y consúltala al responsable.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es el taladrado?", "Hacer agujeros en una pieza con una broca que gira", "Desgastar un borde con una muela abrasiva", "Doblar una plancha en línea recta", "El taladrado hace agujeros; desgastar es esmerilar y doblar es plegar."),
        ("abc", "En Construcciones Metálicas: ¿qué es el cilindrado?", "Dar forma cilíndrica a una pieza que gira en un torno", "Cortar una pieza con una sierra", "Curvar una barra para formar un aro", "El cilindrado se hace en un torno; curvar una barra es doblado."),
        ("abc", "En Construcciones Metálicas: ¿qué operación se define por golpear metal calentado para darle forma?", "La forjadura", "El plegado", "El taladrado", "La forjadura combina calor y golpes; plegar y taladrar no calientan el metal."),
        ("abc", "{F} ¿Qué operación de la hoja de ruta desgasta los bordes con una muela abrasiva?", "El esmerilado", "El aserrado", "El plegado", "El esmerilado usa una muela abrasiva para desgastar bordes."),
        ("=", "{F} Se fabrican 24 soportes. ¿Cuántos agujeros se taladran en total?", "4*24", "Se multiplican los agujeros por soporte por la cantidad de soportes.", " agujeros"),
        ("abc", "En Construcciones Metálicas: ¿qué documento ordena las operaciones de una pieza y la máquina de cada una?", "La hoja de ruta", "La matriz de peligros", "La lista de piezas de una lámina", "La hoja de ruta ordena operaciones; la matriz y la lista cumplen otras funciones."),
        ("abc", "{F} ¿Qué diferencia hay entre aserrado y plegado?", "El aserrado corta el material; el plegado lo dobla sin cortarlo", "El aserrado dobla y el plegado corta", "Los dos cortan, pero con máquinas distintas", "Cortar y doblar son acciones distintas sobre la pieza."),
        ("=", "{F} ¿Cuántos minutos tarda un soporte en sus cuatro operaciones?", "6+12+5+7", "Se suman los tiempos de las cuatro operaciones.", " minutos"),
        ("=", "{F} ¿Cuántas horas tardan en total los 24 soportes con esos tiempos?", "24*(6+12+5+7)//60", "Se multiplica el tiempo de un soporte por 24 y se pasa a horas.", " horas"),
        ("abc", "{F} ¿Por qué se exige operador autorizado aunque el soporte sea una pieza simple?", "Porque el peligro está en la máquina y no en lo simple de la pieza", "Porque las piezas simples son más caras", "Porque los planos no se pueden leer sin autorización", "La formación y la autorización se exigen por el riesgo de operar la máquina."),
        ("abc", "{F} Un compañero cree que la hoja de ruta tiene un error de orden y dice que la corregirá por su cuenta. ¿Qué corresponde?", "Registrar la duda y consultarla a quien emitió la hoja de ruta", "Corregirla y seguir trabajando", "Ignorarla y trabajar a su criterio", "El orden de las operaciones lo fija quien emite el documento."),
        ("abc", "{F} Un jefe propone saltarse el esmerilado «porque se ve bien». ¿Qué corresponde?", "Consultar: la hoja de ruta fija las operaciones y omitir una la decide el responsable", "Saltarlo, porque la ruta es solo una sugerencia", "Hacer el esmerilado antes del aserrado", "Una operación omitida puede afectar la calidad; no la decide el operador."),
        ("abc", "{F} El plegado de la aleta está en la operación 40. ¿Qué máquina se menciona en esta clase para esa operación?", "La plegadora", "El torno", "La sierra", "El plegado se hace con una plegadora."),
    ],
    ctx=("abc", "El turno anterior dejó una nota: «cambié el orden de las operaciones porque me pareció mejor». ¿Qué haces?", "Registrar el cambio y consultar al jefe de taller antes de continuar", "Seguir con el orden de la nota sin avisar", "Volver al orden original sin avisar", "Un cambio respecto de la hoja de ruta debe ser revisado por el responsable."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es el esmerilado?", "Desgastar un borde o una superficie con una muela abrasiva", "El esmerilado desgasta con una muela abrasiva."),
        ("¿Qué indica una hoja de ruta?", "Las operaciones de una pieza, su orden y su máquina", "Ordena el trabajo de fabricación de una pieza."),
        ("¿Cómo se calcula el tiempo total de una pieza?", "Sumando los tiempos de sus operaciones", "Cada operación suma su tiempo al total."),
    ],
    op=("Hoja de ruta de ejemplo de una placa «P9»: operación 10, aserrado, 6 min; 20, taladrado de 6 agujeros, 9 min; 30, esmerilado, 3 min. Se fabrican 30 placas. Escribe (a) cuántos agujeros se taladran en total, (b) cuántos minutos tarda una placa, (c) cuántas horas tardan las 30 placas, (d) qué haces si la hoja de ruta parece tener un error.",
        "(a) 6 × 30 = 180 agujeros. (b) 6 + 9 + 3 = 18 minutos. (c) 30 × 18 = 540 minutos, es decir, 9 horas. (d) Registro la duda y la consulto a quien emitió la hoja de ruta, sin corregirla por mi cuenta.",
        ["calcula los agujeros", "suma los tiempos", "pasa a horas", "indica qué hacer con una duda"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por las piezas", "no pasar los minutos a horas", "corregir la hoja por cuenta propia"],
        "Pregunta: «¿cuántas horas son 540 minutos?». Si no responde, pídele que divida entre 60."),
    reinforce="Escribe una hoja de ruta de tres operaciones para una pieza inventada, con tiempos, y calcula su tiempo total.",
    extend="Explica con un ejemplo por qué el orden de las operaciones de una hoja de ruta importa.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 16 (datos de ejemplo, inventados). Un lote de 60 piezas pasa por tres máquinas, una de cada tipo: taladro, 4 min por pieza; esmeril, 3 min por pieza; plegadora, 5 min por pieza. "
     "Cada máquina tiene 480 min útiles por turno. Costo de ejemplo de la hora de máquina: taladro $12.000, esmeril $9.000, plegadora $18.000. Una hora tiene 60 minutos.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso de planificación de máquinas en papel: tiempos por máquina, cuello de botella, capacidad por turno y costo del lote.",
    prior=["Sé qué es una hoja de ruta.", "Sé multiplicar, dividir y pasar minutos a horas.", "Sé comparar números."],
    explain=[
        "Para planificar un lote se calcula cuántos minutos necesita cada máquina: se multiplica el tiempo por pieza por la cantidad de piezas. La máquina que necesita más minutos es el cuello de botella, la etapa más lenta, que limita cuántas piezas salen. La capacidad por turno es los minutos útiles divididos entre el tiempo por pieza. Si los minutos que necesita el lote no superan los del turno, el lote cabe en un turno.",
        "El costo de una máquina para el lote es sus horas de uso por la tarifa de la hora: los minutos se dividen entre 60 para pasar a horas. El costo total es la suma de las tres máquinas. Mejorar el cuello de botella aumenta la producción; mejorar otra etapa no. Los minutos libres de una máquina son los del turno menos los que usa el lote.",
        f"Estos cálculos son de planilla y orientan al responsable; no autorizan a nadie a usar una máquina. Solo personal autorizado opera. {EMER} {AVISO}",
    ],
    vocab=[("cuello de botella", "etapa más lenta, que limita cuántas piezas salen"), ("capacidad por turno", "piezas que una máquina procesa en los minutos útiles de un turno"), ("minutos útiles", "minutos del turno disponibles para trabajar"), ("tarifa de la hora", "costo de ejemplo por hora de máquina")],
    worked=[
        ("Minutos de una máquina", "Una máquina de ejemplo tarda 7 min por pieza y el lote tiene 40 piezas. ¿Cuántos minutos necesita?", ["Se multiplica el tiempo por pieza por la cantidad.", "7 por 40 son 280."], "280 minutos"),
        ("Capacidad por turno", "Con 360 min útiles y 9 min por pieza, ¿cuántas piezas procesa una máquina de ejemplo en un turno?", ["Se dividen los minutos del turno entre el tiempo por pieza.", "360 entre 9 son 40."], "40 piezas"),
    ],
    mistakes=[("Elegir como cuello de botella la máquina más cara.", "El cuello de botella es la más lenta, no la más cara.", "Compara los minutos que necesita cada máquina."),
              ("Olvidar pasar los minutos a horas antes de aplicar la tarifa.", "La tarifa es por hora y el resultado sale 60 veces mayor.", "Divide los minutos entre 60.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es un cuello de botella en un proceso?", "La etapa más lenta, que limita cuántas piezas salen", "La máquina más cara del taller", "La pieza más pesada del lote", "El cuello de botella se define por velocidad, no por precio ni peso."),
        ("=", "{F} ¿Cuántos minutos necesita el taladro para las 60 piezas?", "60*4", "Se multiplica el tiempo por pieza por la cantidad de piezas.", " minutos"),
        ("=", "{F} ¿Cuántos minutos necesita el esmeril para las 60 piezas?", "60*3", "Se multiplica el tiempo por pieza por la cantidad de piezas.", " minutos"),
        ("=", "{F} ¿Cuántos minutos necesita la plegadora para las 60 piezas?", "60*5", "Se multiplica el tiempo por pieza por la cantidad de piezas.", " minutos"),
        ("abc", "{F} ¿Cuál es el cuello de botella del lote?", "La plegadora, porque necesita más minutos", "El taladro, porque es la primera máquina", "El esmeril, porque es la más barata", "Necesita más minutos la plegadora; eso la hace la etapa más lenta."),
        ("=", "{F} ¿Cuántas piezas por turno puede procesar la plegadora?", "480//5", "Se dividen los minutos del turno entre el tiempo por pieza.", " piezas"),
        ("abc", "{F} ¿El lote de 60 piezas cabe en un turno de la plegadora?", "Sí, porque necesita 300 minutos y el turno tiene 480", "No, porque necesita más de 480 minutos", "No se puede saber sin conocer el costo", "El lote cabe si sus minutos no superan los del turno."),
        ("=", "{F} ¿Cuántos pesos cuesta el uso de la plegadora para este lote?", "300*18000//60", "Se pasan los minutos a horas y se multiplican por la tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el lote completo sumando las tres máquinas?", "(240*12000+180*9000+300*18000)//60", "Se suma el costo de cada máquina, con minutos pasados a horas.", " pesos"),
        ("abc", "{F} Se agrega una segunda plegadora igual, que reparte el trabajo por mitades. ¿Qué pasa con el cuello de botella?", "La plegadora baja a 150 minutos y el taladro, con 240, pasa a ser el cuello de botella", "No cambia, porque el lote es el mismo", "El esmeril pasa a ser el cuello de botella", "Con 150 minutos la plegadora deja de ser la más lenta; ahora lo es el taladro."),
        ("=", "{F} ¿Cuántos minutos libres le quedan al esmeril en un turno después de procesar el lote?", "480-180", "Se restan los minutos del lote a los minutos útiles del turno.", " minutos"),
        ("abc", "{F} El jefe quiere adelantar el lote y un compañero propone usar la plegadora sin que el operador a cargo lo autorice. ¿Qué corresponde?", "No hacerlo: solo opera personal autorizado y la planificación se consulta con el jefe", "Hacerlo si es un turno corto", "Hacerlo si el operador está en colación", "La autorización para operar no depende del apuro ni de la hora."),
        ("abc", "{F} ¿Por qué conviene analizar el cuello de botella antes de comprar otra máquina?", "Porque comprar una máquina que no es la más lenta no aumenta la producción", "Porque el cuello de botella es siempre la máquina más antigua", "Porque conviene comprar una máquina nueva para cada etapa por igual", "Mejorar una etapa que no es la más lenta no cambia cuántas piezas salen."),
    ],
    ctx=("abc", "Una compañera ve que la planilla de otro lote asigna 520 minutos a una máquina con turno de 480. ¿Qué haces?", "Avisar al responsable: el lote no cabe en un turno y hay que replanificar", "Dejar la planilla como está", "Quitar 40 minutos de la planilla", "Si los minutos superan los del turno, el lote no cabe y se replanifica."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calculan los minutos de una máquina para un lote?", "Tiempo por pieza por cantidad de piezas", "Es el producto del tiempo por pieza y la cantidad."),
        ("¿Cómo se calcula la capacidad por turno?", "Minutos útiles del turno divididos entre el tiempo por pieza", "Dice cuántas piezas caben en el turno."),
        ("¿Qué máquina es el cuello de botella?", "La que necesita más minutos para el lote", "Es la etapa más lenta del proceso."),
    ],
    op=("Caso de ejemplo: un lote de 50 piezas pasa por una sierra (6 min por pieza) y un taladro (4 min por pieza). Turno de 480 min útiles; tarifa de ejemplo: sierra $10.000 la hora, taladro $12.000 la hora. Escribe (a) los minutos que necesita cada máquina, (b) cuál es el cuello de botella, (c) si el lote cabe en un turno de esa máquina, (d) el costo total del lote.",
        "(a) Sierra: 50 × 6 = 300 min; taladro: 50 × 4 = 200 min. (b) La sierra, porque necesita más minutos. (c) Sí, porque 300 no supera 480. (d) Sierra: 300 ÷ 60 = 5 h × 10.000 = 50.000; taladro: 200 minutos a $12.000 la hora son 40.000; total 90.000 pesos.",
        ["calcula los minutos", "identifica el cuello de botella", "verifica el turno", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["confundir el cuello de botella con la máquina más barata", "no pasar minutos a horas", "olvidar sumar el costo del taladro"],
        "Pregunta: «¿qué máquina necesita más minutos?». Si responde el taladro, pídele que compare 300 y 200."),
    reinforce="Inventa un lote de 20 piezas que pasa por dos máquinas y calcula los minutos de cada una.",
    extend="Explica con un ejemplo por qué agregar capacidad en una etapa que no es el cuello de botella no sirve.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 17 (datos de ejemplo, inventados; las medidas son pequeñas para calcular con enteros). Plano de un eje y de su agujero: el eje debe medir entre 22 y 23 mm de diámetro; el agujero, entre 24 y 25 mm. "
     "Ajuste con holgura: el agujero es siempre mayor que el eje. Holgura mínima = diámetro mínimo del agujero − diámetro máximo del eje. Holgura máxima = diámetro máximo del agujero − diámetro mínimo del eje. "
     "Una barra de 30 mm de diámetro se reduce en un torno a 24 mm; el material que se retira por cada lado es la mitad de la diferencia de diámetros. Regla de la planilla: holgura máxima admitida de 3 mm.")
build(
    O4, 4, F,
    use="Aprenderé en papel qué son los ajustes con holgura y con apriete, a calcular holguras con rangos de medidas y a calcular el material que se retira al reducir un diámetro.",
    prior=["Sé qué es una tolerancia.", "Sé restar y dividir entre 2.", "Sé qué es el cilindrado."],
    explain=[
        "Un eje es una pieza cilíndrica que entra en un agujero. Cuando el agujero es mayor que el eje queda un espacio libre, la holgura, y el ajuste es con holgura. Cuando el eje es mayor que el agujero, el ajuste es con apriete: el eje entra con presión. El plano da rangos y no una sola medida, porque ninguna máquina deja una medida exacta; el rango define hasta dónde la pieza sigue funcionando.",
        "Con rangos, la holgura mínima se calcula restando el diámetro máximo del eje al mínimo del agujero, y la máxima restando el mínimo del eje al máximo del agujero. Una pieza cumple si su medida está dentro de su rango. Para reducir un diámetro, el material que se retira por cada lado es la mitad de la diferencia entre el diámetro inicial y el final. Estas cuentas son de planilla y no enseñan a operar el torno.",
        f"Las medidas del plano las verifica personal con instrumentos calibrados y se registran; un instrumento con certificado vencido deja la lectura en duda. {EMER} {AVISO}",
    ],
    vocab=[("eje", "pieza cilíndrica que entra en un agujero"), ("holgura", "espacio libre entre el eje y el agujero cuando el agujero es mayor"), ("apriete", "situación en que el eje es mayor que el agujero y entra con presión"), ("ajuste", "relación entre las medidas de un eje y su agujero"), ("diámetro", "medida de un cilindro de lado a lado pasando por el centro")],
    worked=[
        ("Calcular una holgura", "En otro ejemplo, un eje mide 18 mm y su agujero 20 mm. ¿Qué holgura hay?", ["La holgura es el diámetro del agujero menos el del eje.", "20 menos 18 son 2."], "2 mm"),
        ("Material retirado", "Una barra de ejemplo de 34 mm se reduce a 28 mm. ¿Cuánto se retira por cada lado?", ["La diferencia de diámetros es 34 menos 28, es decir, 6.", "Por cada lado se retira la mitad, 3."], "3 mm por lado"),
    ],
    mistakes=[("Dar el par por bueno porque eje y agujero miden lo mismo.", "Si son iguales no hay holgura y el eje supera su máximo, fuera de lo que pide el plano.", "Compara cada medida con su propio rango."),
              ("Calcular el material retirado por cada lado como la diferencia completa.", "La diferencia de diámetros se reparte entre los dos lados.", "Divide la diferencia entre 2.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es una holgura entre un eje y su agujero?", "El espacio libre que queda porque el agujero es mayor que el eje", "El caso en que el eje es mayor que el agujero", "La tolerancia de la longitud del eje", "La holgura existe cuando el agujero supera al eje."),
        ("abc", "En Construcciones Metálicas: ¿qué es un ajuste con apriete?", "Uno en que el eje es mayor que el agujero y entra con presión", "Uno en que el agujero es mayor que el eje", "Uno en que los dos miden exactamente lo mismo", "El apriete ocurre cuando el eje supera al agujero."),
        ("abc", "{F} ¿El ajuste del plano es con holgura o con apriete?", "Con holgura, porque el agujero (24 a 25 mm) es mayor que el eje (22 a 23 mm)", "Con apriete, porque el eje es más largo", "Con apriete, porque el plano da rangos", "Los rangos del agujero están por sobre los del eje, de modo que queda espacio libre."),
        ("=", "{F} ¿Cuál es la holgura mínima del ajuste, en milímetros?", "24-23", "Se resta el diámetro máximo del eje al mínimo del agujero.", " mm"),
        ("=", "{F} ¿Cuál es la holgura máxima del ajuste, en milímetros?", "25-22", "Se resta el diámetro mínimo del eje al máximo del agujero.", " mm"),
        ("=", "{F} ¿Cuántos milímetros se retiran por cada lado al reducir la barra de 30 a 24 mm?", "(30-24)//2", "Se divide entre 2 la diferencia de diámetros.", " mm"),
        ("abc", "{F} Se mide un eje de 24 mm y un agujero de 24 mm. ¿Qué se concluye?", "Está fuera de lo que pide el plano: el eje supera su máximo de 23 mm", "Cumple, porque miden lo mismo", "Cumple, porque el agujero está dentro de su rango", "Cada pieza se compara con su rango; el eje de 24 mm lo supera."),
        ("abc", "{F} Un eje mide 22 mm y el agujero 25 mm. ¿Cumple el plano?", "Sí, ambos están dentro de sus rangos y la holgura es 3 mm", "No, porque la holgura es demasiado grande", "No, porque el eje es menor que el agujero", "Ambas medidas están en rango y la holgura llega justo al máximo admitido."),
        ("=", "{F} Otro par tiene un eje de 22 mm y un agujero de 24 mm. ¿Qué holgura tiene?", "24-22", "Se resta el eje al agujero.", " mm"),
        ("abc", "{F} ¿Por qué el plano da rangos y no una sola medida para el eje y el agujero?", "Porque ninguna máquina deja una medida exacta y el rango define hasta dónde la pieza sigue funcionando", "Porque así se ahorra tinta en el plano", "Porque el rango permite elegir la medida que se prefiera", "El rango reconoce la variación real y fija el límite aceptable."),
        ("=", "{F} Se reduce otra barra de 40 a 32 mm. ¿Cuántos milímetros se retiran por cada lado?", "(40-32)//2", "Se divide entre 2 la diferencia de diámetros.", " mm"),
        ("abc", "{F} Las lecturas son: eje 23 mm y agujero 24 mm, pero el instrumento tiene el certificado vencido. ¿Qué corresponde?", "No dar por buena la medición hasta calibrar el instrumento", "Aceptar el par, porque las cifras están en rango", "Restar 1 mm a cada lectura", "Un instrumento sin calibración vigente deja las lecturas en duda."),
        ("abc", "{F} Un agujero de 25 mm y un eje de 21 mm dan una holgura de 4 mm. ¿Qué se concluye?", "No cumple: el eje de 21 mm está bajo su mínimo y la holgura supera los 3 mm admitidos", "Cumple, porque el agujero está en rango", "Cumple, porque 4 mm es una holgura pequeña", "Ni el eje ni la holgura cumplen lo que pide el plano."),
    ],
    ctx=("abc", "Un operador dice que un eje que entra «apretado» en un agujero está bien, porque «entra con fuerza». El plano pide ajuste con holgura. ¿Qué respondes?", "Que no cumple el plano: si entra con fuerza hay apriete, y se registra y se informa", "Que está bien, porque entra", "Que lo lijen hasta que entre sin registrar", "El plano manda; un apriete donde se pide holgura es una no conformidad."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calcula la holgura mínima?", "Mínimo del agujero menos máximo del eje", "Es el peor caso: el agujero más pequeño con el eje más grande."),
        ("¿Cómo se calcula el material que se retira por lado al reducir un diámetro?", "La diferencia de diámetros dividida entre 2", "La diferencia se reparte entre los dos lados."),
        ("¿Qué diferencia hay entre holgura y apriete?", "En la holgura el agujero es mayor; en el apriete el eje es mayor", "La relación entre los diámetros distingue ambos ajustes."),
    ],
    op=("Plano de ejemplo: eje entre 14 y 15 mm; agujero entre 16 y 17 mm; holgura máxima admitida 3 mm. Una barra de 26 mm se reduce a 14 mm. Escribe (a) la holgura mínima, (b) la holgura máxima y si cumple lo admitido, (c) cuánto material se retira por lado, (d) qué haces si el instrumento tiene el certificado vencido.",
        "(a) 16 − 15 = 1 mm. (b) 17 − 14 = 3 mm, que cumple lo admitido porque no lo supera. (c) (26 − 14) ÷ 2 = 6 mm por lado. (d) No doy por buenas las lecturas hasta que lo calibren y lo informo al responsable.",
        ["calcula la holgura mínima", "calcula la máxima y la compara", "calcula el material por lado", "indica qué hacer con el instrumento"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "no dividir entre 2", "usar un instrumento vencido"],
        "Pregunta: «¿cuál eje y cuál agujero producen la holgura máxima?». Si no responde, pídele que relea la fórmula."),
    reinforce="Inventa un eje y un agujero con rangos y calcula su holgura mínima y máxima.",
    extend="Explica con un ejemplo por qué una pieza puede estar rechazada aunque su medida se vea «casi igual».",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 18 (datos de ejemplo, inventados). Dos rutas de fabricación para una misma pieza. Ruta A: tres operaciones de 20 min cada una, en tres máquinas. Ruta B: dos operaciones de 35 min cada una, en dos máquinas. "
     "Tarifa de ejemplo: $250 por minuto, igual para ambas rutas. Muestra de control de la ruta A: 25 piezas, 2 fuera de tolerancia. Muestra de la ruta B: 20 piezas, 3 fuera de tolerancia. "
     "Criterio de aceptación de ejemplo: hasta 10 % de piezas fuera de tolerancia.")
build(
    O4, 5, F,
    use="Aprenderé a comparar dos rutas de fabricación por tiempo, costo y calidad, a calcular el porcentaje de piezas fuera de tolerancia y a decidir con datos.",
    prior=["Sé qué es una hoja de ruta y una tolerancia.", "Sé calcular porcentajes.", "Sé que un registro debe decir la verdad."],
    explain=[
        "Una ruta de fabricación es la secuencia de operaciones y máquinas por las que pasa una pieza. Una misma pieza puede hacerse con rutas distintas, y para elegir se comparan el tiempo, el costo y la calidad. El tiempo es la suma de los tiempos de las operaciones; el costo, en esta clase, es el tiempo por la tarifa por minuto. La calidad se mide con una muestra de control: se revisan algunas piezas y se calcula el porcentaje fuera de tolerancia.",
        "Una ruta se acepta si su porcentaje de piezas fuera de tolerancia no supera el criterio. Si dos rutas cumplen, conviene la más barata; si una no cumple, no se elige aunque sea más barata o conocida. Elegir «porque siempre se hizo así» no es un argumento verificable. El resultado de una muestra se registra tal como salió: no se repite hasta que cuadre ni se anota un valor distinto.",
        f"Estas comparaciones son de planilla, con valores de ejemplo; la decisión final la toma el responsable. {EMER} {AVISO}",
    ],
    vocab=[("ruta de fabricación", "secuencia de operaciones y máquinas por las que pasa una pieza"), ("muestra de control", "grupo de piezas que se revisan para estimar la calidad del lote"), ("fuera de tolerancia", "con una medida que no cumple el rango del plano"), ("criterio de aceptación", "regla escrita que dice cuándo un resultado se acepta")],
    worked=[
        ("Costo de una ruta", "Una ruta de ejemplo tiene dos operaciones de 15 min y la tarifa es de $200 por minuto. ¿Cuánto cuesta por pieza?", ["El tiempo es 2 por 15, es decir, 30 minutos.", "30 por 200 son 6.000."], "$6.000"),
        ("Porcentaje fuera de tolerancia", "En una muestra de ejemplo de 50 piezas, 5 están fuera de tolerancia. ¿Qué porcentaje es?", ["Se multiplican por 100 las piezas fuera y se divide entre la muestra.", "5 por 100 son 500, y 500 entre 50 son 10."], "10 %"),
    ],
    mistakes=[("Elegir la ruta más barata sin mirar la calidad.", "Una ruta barata que produce muchas piezas fuera de tolerancia genera rechazos y gasto.", "Primero verifica el criterio de calidad y luego compara costos."),
              ("Repetir la muestra hasta que dé cero piezas fuera.", "Se oculta la calidad real de la ruta.", "Registra el resultado real y deja que el responsable decida.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es una ruta de fabricación?", "La secuencia de operaciones y máquinas por las que pasa una pieza", "El camino del camión de despacho", "La lista de peligros del taller", "La ruta describe el proceso de fabricación, no el transporte ni los peligros."),
        ("=", "{F} ¿Cuántos minutos tarda una pieza en la ruta A?", "3*20", "Se multiplican las operaciones por los minutos de cada una.", " minutos"),
        ("=", "{F} ¿Cuántos minutos tarda una pieza en la ruta B?", "2*35", "Se multiplican las operaciones por los minutos de cada una.", " minutos"),
        ("=", "{F} ¿Cuántos pesos cuesta una pieza en la ruta A?", "60*250", "Se multiplica el tiempo de la pieza por la tarifa por minuto.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta una pieza en la ruta B?", "70*250", "Se multiplica el tiempo de la pieza por la tarifa por minuto.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta la ruta B que la ruta A por pieza?", "70*250-60*250", "Se resta el costo de la ruta A al costo de la ruta B.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de la muestra de la ruta A está fuera de tolerancia?", "2*100//25", "Se multiplican por 100 las piezas fuera y se divide entre la muestra.", " %"),
        ("=", "{F} ¿Qué porcentaje de la muestra de la ruta B está fuera de tolerancia?", "3*100//20", "Se multiplican por 100 las piezas fuera y se divide entre la muestra.", " %"),
        ("abc", "{F} Con el criterio de la ficha, ¿qué ruta cumple?", "La A, porque su 8 % no supera el 10 % y la B, con 15 %, sí lo supera", "La B, porque es más lenta y por eso más cuidadosa", "Ambas, porque las dos tienen piezas buenas", "El criterio compara el porcentaje con el máximo, no la lentitud."),
        ("abc", "{F} ¿Por qué conviene la ruta A aunque tenga una operación más que la B?", "Porque cuesta menos por pieza y además cumple el criterio de calidad", "Porque usa más máquinas", "Porque la ruta B no se puede registrar", "La decisión se apoya en costo y calidad, no en la cantidad de operaciones."),
        ("=", "{F} Para 40 piezas, ¿cuántos pesos se ahorran al elegir la ruta A en lugar de la B?", "40*(70*250-60*250)", "Se multiplica la diferencia de costo por pieza por la cantidad de piezas.", " pesos"),
        ("abc", "{F} El jefe pide mantener la ruta B «porque ya la conocemos». ¿Qué argumento con datos puedes darle?", "Que la B cuesta más por pieza y supera el máximo permitido de piezas fuera de tolerancia", "Que la B es más nueva", "Que la A hace más ruido", "Un argumento con datos usa costo y calidad medidos."),
        ("abc", "{F} Una muestra de la ruta A de 25 piezas se repite hasta lograr 0 piezas fuera de tolerancia. ¿Qué corresponde?", "Registrar el resultado real de la muestra y no repetirla hasta que cuadre", "Repetir hasta lograr 0", "Anotar 0 sin medir", "Un registro verdadero muestra la calidad real, aunque no sea perfecta."),
    ],
    ctx=("abc", "Una compañera propone anotar solo la mejor de tres muestras de la ruta B para que se vea más bonita en el informe. ¿Qué respondes?", "Que se informan todas las muestras con sus valores reales, porque ocultar resultados falsea la decisión", "Que sí, porque es la que se ve mejor", "Que sí, si el jefe no pregunta", "Una decisión con datos requiere todos los datos reales."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calcula el costo por pieza de una ruta?", "Tiempo por pieza por tarifa por minuto", "El costo crece con el tiempo y la tarifa."),
        ("¿Qué se compara para aceptar una ruta por calidad?", "El porcentaje fuera de tolerancia con el criterio", "El criterio fija el máximo permitido."),
        ("¿Qué se hace con una muestra mala?", "Se registra tal como salió", "El registro refleja la calidad real."),
    ],
    op=("Caso de ejemplo: Ruta X, dos operaciones de 25 min, muestra de 20 piezas con 1 fuera de tolerancia. Ruta Y, una operación de 45 min, muestra de 25 piezas con 5 fuera de tolerancia. Tarifa de ejemplo: $300 por minuto; criterio: hasta 10 % fuera de tolerancia. Escribe (a) el tiempo y el costo por pieza de cada ruta, (b) el porcentaje fuera de tolerancia de cada una, (c) qué ruta cumple y conviene, (d) qué haces si el jefe pide anotar una muestra distinta de la real.",
        "(a) X: 50 min y 15.000 pesos; Y: 45 min y 13.500 pesos. (b) X: 1 × 100 ÷ 20 = 5 %; Y: 5 × 100 ÷ 25 = 20 %. (c) La X cumple el criterio (5 % no supera 10 %), aunque cueste más; la Y no cumple. (d) Registro la muestra real y lo informo al responsable.",
        ["calcula tiempo y costo", "calcula los porcentajes", "decide con el criterio", "defiende el registro real"],
        ["hoja con las cuatro respuestas"],
        ["elegir la ruta más barata sin mirar la calidad", "dividir entre el total de piezas equivocado", "anotar una muestra distinta de la real"],
        "Pregunta: «¿la ruta más barata cumple el criterio de calidad?». Si responde que sí, pídele que calcule el porcentaje de Y."),
    reinforce="Inventa dos rutas para una pieza con tiempo y porcentaje de rechazo y decide cuál conviene con un criterio del 10 %.",
    extend="Explica con un ejemplo por qué una ruta más barata puede terminar costando más si rechaza muchas piezas.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 19 (caso de ejemplo, inventado). La empresa ficticia «Montajes Livianos Demo» arma en una obra un galpón de ejemplo de 20 m de largo con 5 pórticos, es decir, 5 estructuras iguales formadas por dos pilares y una viga cada una. "
     "Peligros anotados: trabajo en altura, caída de objetos, piezas que se izan con grúa, viento, terreno irregular y cercanía de líneas eléctricas. Dotación: 1 jefe de obra, 1 prevencionista y 8 montajistas. La obra tiene 3 zonas delimitadas.")
build(
    O5, 1, F,
    use="Aprenderé qué es una construcción metálica liviana, qué es un pórtico, qué peligros tiene un montaje y cómo se ordenan las medidas, sin aprender a ejecutarlo.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé multiplicar y restar.", "Sé que una tarea de riesgo exige autorización."],
    explain=[
        "Una construcción metálica liviana es una estructura de acero de poco peso por metro cuadrado, como un galpón, una bodega o un edificio de pocos pisos. Un pórtico es una estructura formada por pilares y una viga, y un galpón se arma con varios pórticos iguales. Armar y montar es unir los elementos y dejarlos en su lugar según los planos, ya sea en el taller o en la obra. Este cuaderno no enseña a hacerlo: enseña vocabulario, documentos y reglas de seguridad.",
        "El trabajo en altura es una tarea con riesgo de caer a un nivel inferior, y la norma vigente exige formación y medidas específicas. Los controles se ordenan como siempre: prefabricar piezas en el taller para reducir el tiempo en altura (eliminar o sustituir), barandas y redes instaladas por personal autorizado (ingeniería), plan de montaje, permisos y zonas delimitadas (administrativos) y arnés de seguridad (EPP). El arnés es la última barrera porque solo actúa cuando la persona ya cayó. Si sube el viento, el responsable de la obra decide suspender las tareas según el plan.",
        f"Las piezas que se izan, las zonas bajo carga y el terreno se manejan con personal capacitado y según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("construcción liviana", "estructura de acero de poco peso por m², como un galpón"), ("pórtico", "estructura formada por pilares y una viga"), ("montaje", "unir los elementos y dejarlos en su lugar según los planos"), ("trabajo en altura", "tarea con riesgo de caer a un nivel inferior"), ("arnés de seguridad", "EPP que sujeta a la persona si cae, la última barrera"), ("zona delimitada", "área señalizada a la que solo entra personal autorizado")],
    worked=[
        ("Contar pilares", "Un galpón de ejemplo tiene 4 pórticos de dos pilares cada uno. ¿Cuántos pilares son?", ["Se multiplican los pórticos por los pilares de cada uno.", "4 por 2 son 8."], "8 pilares"),
        ("Clasificar un control", "Se instala una red que retiene objetos que caen, colocada por personal autorizado. ¿Qué tipo de control es?", ["La red cambia físicamente el lugar.", "Una barrera física es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que el arnés basta para trabajar en altura sin otras medidas.", "El arnés actúa cuando la caída ya ocurrió; los otros controles buscan evitarla.", "Primero se elimina o se controla el riesgo de caída; el arnés se suma."),
              ("Decidir por cuenta propia seguir trabajando con viento fuerte.", "La decisión de suspender es del responsable según el plan y la norma vigente.", "Consulta y acata la decisión del responsable de la obra.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es un pórtico de un galpón?", "Una estructura formada por pilares y una viga", "Una puerta grande de entrada", "Una pieza horizontal que sostiene la cubierta", "El pórtico combina pilares y viga; una pieza horizontal de cubierta es otra pieza distinta del pórtico."),
        ("abc", "En Construcciones Metálicas: ¿qué es el trabajo en altura?", "Una tarea con riesgo de caer a un nivel inferior", "Cualquier tarea hecha en un edificio de varios pisos", "Una tarea con herramientas pesadas", "Lo que define el trabajo en altura es el riesgo de caída."),
        ("abc", "En Construcciones Metálicas: ¿quién fija las medidas exigidas para el trabajo en altura?", "La norma vigente y el plan de la obra", "Cada montajista según su experiencia", "El proveedor de las piezas", "Las medidas son comunes y obligatorias; no dependen de la experiencia individual."),
        ("=", "{F} ¿Cuántos pilares tiene el galpón?", "5*2", "Se multiplican los pórticos por los pilares de cada uno.", " pilares"),
        ("=", "{F} ¿Cuántas piezas principales, entre pilares y vigas, suman los 5 pórticos?", "5*3", "Cada pórtico lleva dos pilares y una viga, es decir, tres piezas.", " piezas"),
        ("abc", "{F} Un pórtico se prefabrica armado en el taller para reducir el tiempo de trabajo en altura en la obra. ¿Qué nivel de la jerarquía es?", "Eliminar o sustituir parte del peligro, porque reduce el tiempo en altura", "EPP, porque protege a las personas", "Administrativo, porque es una regla", "Hacer en el taller parte del trabajo reduce el peligro en su origen."),
        ("abc", "{F} Una baranda temporal instalada por personal autorizado en el borde de una zona de trabajo es:", "Un control de ingeniería", "Un EPP", "Un control administrativo", "La baranda es una barrera física que impide la caída sin depender de la persona."),
        ("=", "{F} ¿Cuántas personas hay en la obra sumando jefe, prevencionista y montajistas?", "1+1+8", "Se suman las tres partes de la dotación.", " personas"),
        ("abc", "{F} Aumenta el viento durante la jornada. ¿Quién decide si se suspenden las tareas en altura?", "El responsable de la obra, según el plan y la norma vigente, y todos acatan", "Cada montajista según cuán seguro se sienta", "El proveedor de las piezas", "La decisión es del responsable y se aplica a todos por igual."),
        ("abc", "{F} Un joven en práctica dice que ya sabe armar pórticos porque vio un video. ¿Qué corresponde?", "Ver un video no lo habilita: necesita formación, instructor autorizado y norma vigente", "Puede hacerlo si usa arnés", "Puede hacerlo si trabaja en un pórtico bajo", "Ni un video ni el EPP reemplazan la formación y la autorización."),
        ("abc", "En una visita de ejemplo a una obra, una persona cae desde una estructura baja. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte y moverla para ver si puede levantarse", "Esperar a que termine la jornada", "Mover a una persona caída sin formación puede agravar sus lesiones."),
        ("abc", "{F} ¿Por qué el arnés de seguridad es la última barrera y no la primera?", "Porque solo actúa cuando la persona ya cayó, mientras los otros controles evitan la caída", "Porque es incómodo de usar", "Porque lo exige la ley solo en invierno", "Evitar la caída es mejor que detenerla una vez que ocurre."),
        ("=", "{F} En cada una de las 3 zonas delimitadas trabajan a la vez 2 montajistas. ¿Cuántos de los 8 montajistas quedan fuera de las zonas?", "8-3*2", "Se restan a los montajistas los que están dentro de las zonas.", " montajistas"),
    ],
    ctx=("abc", "El jefe de obra de ejemplo te dice: «sube a ayudar con la viga, tú ya viste cómo se hace». ¿Qué respondes?", "Que no, porque trabajar en altura exige formación, autorización y norma vigente, y que consultarás a un adulto responsable", "Que sí, si te prestan un arnés", "Que sí, pero solo por un rato", "Ver una tarea no habilita para hacerla; el arnés no reemplaza la formación."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es un pórtico?", "Una estructura de pilares y una viga", "Es la unidad que se repite para formar un galpón."),
        ("¿Qué es el trabajo en altura?", "Una tarea con riesgo de caer a un nivel inferior", "El riesgo de caída define la tarea."),
        ("¿Quién decide suspender las tareas por viento?", "El responsable de la obra, según el plan", "La decisión es del responsable y vale para todos."),
    ],
    op=("Caso de ejemplo: una obra arma una bodega de 6 pórticos de dos pilares y una viga cada uno; los peligros anotados son caída desde altura y caída de herramientas sobre un pasillo. Escribe (a) cuántos pilares tiene la bodega, (b) un control de ingeniería para el pasillo, (c) un control administrativo, (d) por qué el arnés es la última barrera.",
        "(a) 6 × 2 = 12 pilares. (b) Una cubierta o marquesina física sobre el pasillo, instalada por personal autorizado. (c) Una zona delimitada con señal y orden de no pasar mientras dura el montaje. (d) Porque solo actúa cuando la persona ya cayó; los otros controles buscan evitar la caída.",
        ["calcula los pilares", "propone un control de ingeniería", "propone un control administrativo", "explica el arnés"],
        ["hoja con las cuatro respuestas"],
        ["olvidar que cada pórtico lleva dos pilares", "proponer solo EPP", "decir que el arnés evita la caída"],
        "Pregunta: «¿qué hace el arnés después de la caída o antes?». Si responde antes, pídele que relea la explicación."),
    reinforce="Escribe tres peligros de un montaje y un control para cada uno, indicando su nivel de la jerarquía.",
    extend="Explica con un ejemplo por qué prefabricar en el taller reduce el riesgo de un montaje.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 20 (plano de montaje y lista de materiales de ejemplo, inventados) de un galpón de 5 pórticos. Marcas: P1, pilar; V1, viga de pórtico; C1, costanera (pieza horizontal que une los pórticos y sostiene la cubierta); "
     "A1, arriostre (pieza diagonal que da rigidez); B1, placa base (apoya el pilar sobre la fundación); PA, perno de anclaje (fija la placa base a la fundación). "
     "Lista de materiales del galpón: P1 ×10, V1 ×5, C1 ×24, A1 ×8, B1 ×10; cada placa base lleva 4 PA. La guía de despacho trae C1 ×22 y las demás marcas completas.")
build(
    O5, 2, F,
    use="Aprenderé el nombre y la función de las piezas de un galpón, a leer una lista de materiales y un plano de montaje, y qué hacen el ITO, el jefe de obra y el prevencionista.",
    prior=["Sé qué es un pórtico.", "Sé sumar y multiplicar.", "Sé qué es una marca y una lista de piezas."],
    explain=[
        "Un galpón se compone de piezas con funciones propias. El pilar es la pieza vertical; la viga de pórtico cruza de pilar a pilar; la costanera es una pieza horizontal que une los pórticos y sostiene la cubierta; el arriostre es una pieza diagonal que da rigidez e impide que la estructura se deforme hacia los lados; la placa base apoya el pilar sobre la fundación, que es la base de hormigón, y reparte su carga; y los pernos de anclaje fijan la placa base a la fundación.",
        "El plano de montaje identifica cada pieza por su marca y muestra dónde va. La lista de materiales cuenta cuántas piezas lleva la obra de cada marca. La guía de despacho es el documento que acompaña lo enviado y se compara con la lista al recibirlo. La revisión del plano debe ser la vigente: una marca puede repetirse entre revisiones aunque las medidas cambien.",
        f"El ITO revisa que lo montado cumpla planos y especificaciones; el jefe de obra organiza el trabajo; el prevencionista vela por la seguridad; y el personal autorizado ejecuta. Un faltante o una duda se registran y se informan. {EMER} {AVISO}",
    ],
    vocab=[("costanera", "pieza horizontal que une los pórticos y sostiene la cubierta"), ("arriostre", "pieza diagonal que da rigidez a la estructura"), ("placa base", "placa que apoya el pilar sobre la fundación y reparte su carga"), ("perno de anclaje", "perno que fija la placa base a la fundación"), ("fundación", "base de hormigón sobre la que se apoya la estructura"), ("guía de despacho", "documento que acompaña lo enviado y se compara con la lista de materiales")],
    worked=[
        ("Contar pernos", "En una estructura de ejemplo hay 6 placas base y cada una lleva 4 pernos de anclaje. ¿Cuántos pernos son?", ["Se multiplican las placas por los pernos de cada una.", "6 por 4 son 24."], "24 pernos"),
        ("Detectar un faltante", "La lista de ejemplo pide 12 arriostres y la guía trae 10. ¿Cuántos faltan?", ["Se resta lo que trae la guía a lo que pide la lista.", "12 menos 10 son 2."], "Faltan 2"),
    ],
    mistakes=[("Reemplazar una pieza que falta por otra «parecida» para no atrasar.", "Cada pieza cumple una función y sus medidas las fija el proyecto.", "Registra el faltante y pide la reposición al responsable."),
              ("Creer que si la marca coincide el plano es el mismo.", "Una marca puede repetirse en revisiones con medidas distintas.", "Verifica la letra de revisión vigente.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es una costanera?", "Una pieza horizontal que une los pórticos y sostiene la cubierta", "Una pieza que une la placa base con el suelo", "Una pieza diagonal que da rigidez", "La costanera es horizontal y sostiene la cubierta; la diagonal es el arriostre."),
        ("abc", "En Construcciones Metálicas: ¿qué hace un arriostre?", "Da rigidez e impide que la estructura se deforme hacia los lados", "Cubre el techo", "Apoya el pilar sobre la fundación", "El arriostre es una diagonal que evita la deformación lateral."),
        ("abc", "En Construcciones Metálicas: ¿qué función tiene la placa base?", "Apoyar el pilar sobre la fundación y repartir su carga", "Unir las vigas entre sí", "Sostener la cubierta", "La placa base es el apoyo del pilar en la fundación."),
        ("=", "{F} ¿Cuántos pernos de anclaje necesita el galpón, con 4 por cada placa base?", "10*4", "Se multiplican las placas base por los pernos de cada una.", " pernos"),
        ("=", "{F} ¿Cuántas piezas suma la lista de materiales entre P1, V1, C1, A1 y B1?", "10+5+24+8+10", "Se suman las cantidades de las cinco marcas.", " piezas"),
        ("abc", "{F} ¿Para qué sirve el plano de montaje?", "Para identificar cada pieza por su marca y saber dónde va", "Para calcular su precio", "Para dibujar cómo se fabrica cada agujero", "El plano de montaje ubica las piezas; el precio y la fabricación se ven en otros documentos."),
        ("abc", "{F} ¿Qué documento se compara con la lista de materiales para saber si llegó lo que se envió?", "La guía de despacho", "El permiso de trabajo", "El certificado de calibración", "La guía de despacho acompaña lo enviado."),
        ("=", "{F} ¿Cuántas costaneras C1 faltan respecto de la lista?", "24-22", "Se resta lo que trae la guía a lo que pide la lista.", " costaneras"),
        ("abc", "{F} Faltan costaneras. ¿Qué corresponde?", "Registrar el faltante y avisar al responsable antes de armar sin ellas", "Reemplazarlas por otra pieza parecida", "Armar y ver si alcanzan", "Un faltante se registra y se informa; no se sustituye por intuición."),
        ("abc", "{F} ¿Por qué cada pieza lleva una marca visible?", "Para identificarla y ubicarla según el plano sin confundirla con otra parecida", "Para facilitar el transporte en camión", "Para que el cliente la reconozca", "La marca es el vínculo entre la pieza y el plano de montaje."),
        ("abc", "En Construcciones Metálicas: ¿quién responde de revisar que lo montado cumpla los planos y las especificaciones y lo deja registrado?", "El ITO, inspector técnico de obra", "El prevencionista", "El proveedor de las piezas", "La función de verificar lo construido es del ITO."),
        ("=", "{F} Tres galpones iguales a este necesitan cada uno el mismo número de pernos de anclaje. ¿Cuántos pernos son en total?", "3*10*4", "Se multiplican galpones, placas base y pernos por placa.", " pernos"),
        ("abc", "{F} Un compañero dice: «como la marca V1 es igual en todas las revisiones, no importa mirar la letra de revisión». ¿Qué respondes?", "Que sí importa: la revisión vigente puede cambiar medidas aunque la marca se repita", "Que tiene razón, la marca basta", "Que basta con la última que llegó por correo", "La marca no garantiza que el plano sea el vigente."),
    ],
    ctx=("abc", "Al recibir las piezas de otra obra de ejemplo, notas que la guía de despacho trae 7 arriostres y la lista pide 8. El jefe te dice «no importa, con 7 alcanza». ¿Qué haces?", "Registrar el faltante y pedir al responsable que lo gestione antes de seguir", "Armar con 7 y ver", "Fabricar 1 arriostre con lo que haya", "Un faltante se informa; las piezas no se improvisan sin plano ni autorización."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es un perno de anclaje?", "Un perno que fija la placa base a la fundación", "Une la estructura con su base de hormigón."),
        ("¿Qué compara la recepción de materiales?", "La guía de despacho con la lista de materiales", "Así se detectan faltantes antes de armar."),
        ("¿Qué hace el ITO?", "Revisa que lo montado cumpla planos y especificaciones", "Verifica lo construido y deja registro escrito."),
    ],
    op=("Lista de materiales de ejemplo de una bodega: P1 ×8, V1 ×4, C1 ×18, B1 ×8; cada placa base lleva 4 pernos de anclaje. La guía de despacho trae C1 ×16 y las demás marcas completas. Escribe (a) cuántas piezas suma la lista, (b) cuántos pernos de anclaje se necesitan, (c) cuántas costaneras faltan, (d) qué haces con el faltante.",
        "(a) 8 + 4 + 18 + 8 = 38 piezas. (b) 8 × 4 = 32 pernos. (c) 18 − 16 = 2 costaneras. (d) Registro el faltante y aviso al responsable para que gestione la reposición, sin reemplazarlas por otras piezas.",
        ["suma la lista", "calcula los pernos", "calcula el faltante", "indica qué hacer"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por 4", "no restar bien el faltante", "reemplazar la pieza por una parecida"],
        "Pregunta: «¿quién debe gestionar la reposición?». Si responde tú, pídele que relea el rol del responsable."),
    reinforce="Haz una tabla con marca, nombre y función de las seis piezas del galpón.",
    extend="Explica con un ejemplo por qué se compara la guía con la lista el mismo día de la recepción.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 21 (datos de ejemplo, inventados). Recepción de las piezas de un galpón. Lista de materiales / llegaron / observación: P1, 10 / 10 / sin observación; V1, 5 / 5 / sin observación; C1, 24 / 22 / faltan; A1, 8 / 8 / sin observación; B1, 10 / 10 / una con golpe visible, anotada como dañada. "
     "Masas de ejemplo: cada P1, 100 kg; cada V1, 400 kg. Camión de ejemplo con carga útil de 3.000 kg; la carga no puede superar la carga útil. Una espera por reposición cuesta $40.000 por día a la obra.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso de recepción de piezas en papel: comparar lista, guía y lo recibido, registrar faltantes y daños, y calcular masas y camiones.",
    prior=["Sé qué es una lista de materiales y una guía de despacho.", "Sé sumar, restar y dividir.", "Sé que un registro debe decir la verdad."],
    explain=[
        "La recepción de materiales en obra consiste en comparar lo que llega con la lista de materiales y la guía de despacho, y registrar las diferencias: faltantes, sobrantes o piezas dañadas. Se hace el mismo día de la llegada, porque después ya no se puede saber si la pieza faltó en el despacho, en el camino o en la obra. Una pieza dañada se anota y se informa al responsable, que decide qué hacer; no se esconde ni se usa «a ver si resulta».",
        "Con las masas de ejemplo se calcula cuánto pesa lo que se transporta: se multiplica la cantidad de cada pieza por su masa y se suman los resultados. La cantidad de camiones es la masa total dividida entre la carga útil; como la carga no puede superar la carga útil, no se llena un camión más allá de ese límite. Esta cuenta orienta la planilla; los límites reales los fija la norma vigente y el transportista.",
        f"El faltante se resuelve pidiendo la reposición al responsable; no se fabrican piezas sin plano ni autorización. {EMER} {AVISO}",
    ],
    vocab=[("recepción de materiales", "comparar lo que llega con la lista y la guía y registrar diferencias"), ("faltante", "pieza que está en la lista y no llegó"), ("pieza dañada", "pieza que llegó con un daño visible"), ("carga útil", "masa máxima que un camión puede transportar"), ("reposición", "nuevo envío de una pieza que faltó o llegó dañada")],
    worked=[
        ("Masa de un grupo de piezas", "Una obra de ejemplo recibe 6 piezas de 250 kg cada una. ¿Cuál es la masa total?", ["Se multiplican las piezas por la masa de cada una.", "6 por 250 son 1.500."], "1.500 kg"),
        ("Camiones necesarios", "Una carga de ejemplo de 7.500 kg se transporta en camiones de 2.500 kg de carga útil. ¿Cuántos camiones se necesitan?", ["Se divide la masa total entre la carga útil.", "7.500 entre 2.500 son 3."], "3 camiones"),
    ],
    mistakes=[("Postergar el registro de diferencias «para el final de la semana».", "Después ya no se sabe dónde se produjo el faltante o el daño.", "Registra las diferencias el mismo día de la recepción."),
              ("Usar una pieza dañada porque «parece estar bien».", "Un daño visible puede afectar su resistencia o su ajuste.", "Regístrala como dañada y deja que el responsable decida.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es la recepción de materiales en una obra?", "Comparar lo que llega con la lista y la guía de despacho y registrar las diferencias", "Guardar las piezas sin revisarlas", "Pintar las piezas que llegan", "La recepción verifica lo llegado contra los documentos."),
        ("=", "{F} ¿Cuántas costaneras C1 faltan?", "24-22", "Se resta lo que llegó a lo que pide la lista.", " costaneras"),
        ("abc", "{F} ¿Qué corresponde con la placa base que llegó golpeada?", "Registrarla como dañada e informar al responsable, que decide qué hacer", "Usarla igual si parece estar bien", "Esconderla entre las demás", "Una pieza dañada se informa; la decisión no es del montajista."),
        ("=", "{F} ¿Cuántas piezas llegaron en total?", "10+5+22+8+10", "Se suman las cantidades que llegaron de cada marca.", " piezas"),
        ("=", "{F} ¿Cuántas piezas deberían haber llegado según la lista?", "10+5+24+8+10", "Se suman las cantidades de la lista.", " piezas"),
        ("=", "{F} ¿Cuántas piezas llegaron sin ningún daño visible?", "10+5+22+8+10-1", "Se resta la pieza dañada al total de piezas que llegaron.", " piezas"),
        ("=", "{F} ¿Cuántos kilogramos pesan juntos los P1 y los V1?", "10*100+5*400", "Se multiplica la cantidad de cada marca por su masa y se suma.", " kg"),
        ("abc", "{F} ¿Cuántos camiones hacen falta para los P1 y los V1?", "1 camión, porque la masa es exactamente la carga útil y no la supera", "2 camiones, porque 3.000 kg es el límite", "3 camiones, porque hay dos marcas distintas", "La carga puede igualar la carga útil, pero no superarla."),
        ("=", "{F} ¿Cuántos camiones se necesitan para los P1 y los V1 de 4 galpones iguales?", "4*3000//3000", "Se divide la masa total entre la carga útil de cada camión.", " camiones"),
        ("abc", "{F} ¿Por qué se registran las diferencias el mismo día de la recepción?", "Porque después ya no se puede saber si faltó en el despacho, en el camino o en la obra", "Porque la guía de despacho vence ese día", "Porque los proveedores solo atienden ese día", "El registro oportuno permite atribuir el problema y reclamar la reposición."),
        ("abc", "{F} Faltan costaneras y un compañero propone fabricar «unas rápidas» en la obra. ¿Qué corresponde?", "Registrar el faltante y pedir al responsable que gestione la reposición", "Fabricarlas con lo que haya", "Cambiar el plano para que no las pida", "No se fabrican piezas sin plano ni autorización; los planos los cambia el proyectista."),
        ("=", "{F} Si la reposición de las costaneras demora 3 días, ¿cuántos pesos cuesta la espera a la obra?", "3*40000", "Se multiplican los días de espera por el costo diario.", " pesos"),
        ("abc", "{F} Para evitar este faltante en el futuro, ¿qué control podría agregarse al despacho?", "Contar y comparar las piezas con la lista al cargar el camión y firmar la guía", "Despachar sin lista para ahorrar tiempo", "Pedir siempre el doble de piezas", "Un control en el origen detecta el faltante antes de que salga el camión."),
    ],
    ctx=("abc", "Al contar las piezas de otra obra de ejemplo, ves que la guía dice 12 arriostres y llegaron 11, pero el conductor se va apurado. ¿Qué haces?", "Registrar el faltante en la guía antes de que el camión se retire e informar al responsable", "Dejarlo pasar para no demorar al conductor", "Firmar la guía como completa", "Firmar completa una guía con faltante impide reclamar después."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calcula la masa de un grupo de piezas iguales?", "Cantidad de piezas por masa de cada una", "Es el producto de la cantidad y la masa unitaria."),
        ("En Construcciones Metálicas: ¿cómo se calculan los camiones necesarios?", "Masa total dividida entre la carga útil", "La carga no puede superar la carga útil."),
        ("¿Cuándo se registran las diferencias de una recepción?", "El mismo día en que llegan las piezas", "Después no se puede atribuir el origen del problema."),
    ],
    op=("Caso de ejemplo: llegan 12 piezas de 150 kg y 6 piezas de 300 kg. La guía dice 12 y 7, respectivamente. Camión de 3.000 kg de carga útil. Escribe (a) la masa total que llegó, (b) cuántas piezas de 300 kg faltan, (c) cuántos camiones se necesitan para lo llegado, (d) qué haces antes de que el camión se retire.",
        "(a) 12 × 150 + 6 × 300 = 1.800 + 1.800 = 3.600 kg. (b) 7 − 6 = 1 pieza. (c) 3.600 ÷ 3.000 es más de 1, de modo que se necesitan 2 camiones si no pueden superar la carga útil. (d) Registro el faltante en la guía y lo informo al responsable.",
        ["calcula la masa", "calcula el faltante", "decide los camiones", "registra el faltante"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por la masa de cada pieza", "firmar la guía completa", "superar la carga útil"],
        "Pregunta: «¿3.600 kg caben en un camión de 3.000 kg?». Si responde que sí, pídele que compare ambos números."),
    reinforce="Inventa una recepción con cuatro marcas y señala dos diferencias que registrarías.",
    extend="Explica con un ejemplo por qué firmar una guía incompleta como completa puede costar dinero a la obra.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 22 (valores de ejemplo, no normativos). Pilar de 6.000 mm de altura. Verticalidad de ejemplo: el desplome máximo admitido es la altura dividida entre 500. Desplomes medidos en tres pilares: P-1, 11 mm; P-2, 12 mm; P-3, 14 mm. "
     "Base rectangular de pernos de anclaje de 1.200 × 900 mm, con diagonal teórica de 1.500 mm; diagonales medidas: 1.499 mm y 1.502 mm; diferencia máxima admitida entre diagonales: 2 mm. "
     "Nivel de una placa base: plano 100 mm, tolerancia ± 3 mm; lecturas: 102 mm y 104 mm.")
build(
    O5, 4, F,
    use="Aprenderé a verificar en papel el montaje de una estructura: desplome de un pilar, escuadra de una base de pernos y nivel de una placa, aplicando tolerancias de ejemplo y registrando.",
    prior=["Sé qué es una tolerancia y una no conformidad.", "Sé dividir y restar.", "Sé que un registro debe decir la verdad."],
    explain=[
        "Montar una estructura bien es dejarla en su posición según el plano, y eso se verifica. La vertical se llama plomo, y el desplome es la desviación horizontal de un elemento respecto de la vertical. El nivel mide si una superficie está en la altura que pide el plano. El replanteo es trasladar al terreno los ejes y puntos del plano para ubicar la obra. Cada verificación compara una lectura con un valor de plano y su tolerancia, y se registra.",
        "En esta clase la tolerancia de verticalidad es de ejemplo: el desplome máximo es la altura dividida entre 500. Una base de pernos rectangular se comprueba por sus diagonales, que deben diferir dentro de lo admitido, como en el control de un marco. El nivel de una placa se acepta si la lectura está entre el valor del plano menos la tolerancia y el valor más la tolerancia, y los límites se aceptan.",
        f"Un elemento fuera de tolerancia no se corrige con improvisaciones: se registra como no conformidad y el responsable decide la corrección. Aquí solo se calcula. {EMER} {AVISO}",
    ],
    vocab=[("plomo", "dirección vertical"), ("desplome", "desviación horizontal de un elemento respecto de la vertical"), ("nivel", "altura de una superficie respecto de la que pide el plano"), ("replanteo", "trasladar al terreno los ejes y puntos del plano"), ("escuadra", "condición de un marco rectangular con diagonales iguales dentro de lo admitido")],
    worked=[
        ("Desplome máximo", "Con la regla de altura entre 500, ¿cuál es el desplome máximo de un pilar de ejemplo de 4.000 mm?", ["Se divide la altura entre 500.", "4.000 entre 500 son 8."], "8 mm"),
        ("Nivel aceptable", "Una placa de ejemplo debe estar a 250 mm con tolerancia ± 2 mm y se lee 253 mm. ¿Se acepta?", ["Los límites son 248 y 252 mm.", "253 supera el máximo de 252."], "Se rechaza y se registra"),
    ],
    mistakes=[("Dar la base de pernos por buena porque cada diagonal está cerca del valor teórico.", "Lo que se compara es la diferencia entre las dos diagonales.", "Resta una diagonal a la otra y compárala con lo admitido."),
              ("Corregir a la fuerza un pilar fuera de plomo.", "Una corrección improvisada puede dañar la estructura o crear un peligro.", "Registra la no conformidad e informa al responsable.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es el desplome de un pilar?", "La desviación horizontal del pilar respecto de la vertical", "La altura total del pilar", "El hundimiento de la fundación", "El desplome mide cuánto se aparta el pilar de la vertical."),
        ("abc", "En Construcciones Metálicas: ¿qué es el replanteo?", "Trasladar al terreno las líneas y puntos del plano para ubicar la obra", "Dibujar de nuevo el plano", "Pesar las piezas antes de enviarlas", "El replanteo lleva el plano al terreno; no redibuja ni pesa."),
        ("abc", "{F} ¿Qué se compara para saber si la base de pernos está en escuadra?", "Que las dos diagonales difieran dentro de lo admitido", "Que cada diagonal sea igual a un lado", "Que la suma de las diagonales sea 3.000 mm", "Un rectángulo en escuadra tiene diagonales iguales dentro de la tolerancia."),
        ("=", "{F} ¿Cuántos milímetros de desplome máximo admite un pilar de 6.000 mm?", "6000//500", "Se divide la altura entre 500.", " mm"),
        ("abc", "{F} ¿Se acepta P-2, con 12 mm de desplome?", "Se acepta, porque está justo en el límite de 12 mm", "Se rechaza, porque llegó al límite", "Se rechaza, porque 12 es mayor que 11", "Los límites se aceptan; solo se rechaza lo que los supera."),
        ("abc", "{F} ¿Se acepta P-3, con 14 mm?", "Se rechaza, porque supera el máximo de 12 mm", "Se acepta, porque la diferencia es de solo 2 mm", "Se acepta, porque P-1 y P-2 cumplen", "Cada pilar se evalúa por separado frente al máximo."),
        ("=", "{F} ¿Cuántos milímetros difieren entre sí las dos diagonales medidas de la base?", "1502-1499", "Se resta la diagonal menor a la mayor.", " mm"),
        ("abc", "{F} ¿Qué se concluye de la base de pernos?", "Está fuera de escuadra: 3 mm supera los 2 mm admitidos", "Está bien: el promedio de las diagonales es casi 1.500", "Está bien: cada diagonal está a 2 mm o menos de 1.500", "Se compara la diferencia entre diagonales y no el promedio ni cada una por separado."),
        ("=", "{F} ¿Cuál es el nivel máximo aceptable de la placa base, en milímetros?", "100+3", "Se suma la tolerancia al valor del plano.", " mm"),
        ("abc", "{F} ¿Se acepta la placa con lectura de 104 mm?", "Se rechaza, porque supera el máximo de 103 mm", "Se acepta, porque solo difiere 4 mm del plano", "Se acepta, porque está dentro de ± 5 mm", "La tolerancia de la ficha es ± 3 mm, no ± 5 mm."),
        ("abc", "{F} El pilar P-3, fuera de tolerancia, ya está en su sitio. Un compañero propone «corregirlo a la fuerza con un tirante improvisado». ¿Qué corresponde?", "No improvisar: registrar la no conformidad e informar al responsable para que decida la corrección", "Corregirlo ahora", "Dejarlo así sin registro", "Una corrección improvisada puede crear un peligro mayor."),
        ("=", "{F} Con la misma regla, ¿cuántos milímetros de desplome máximo admite un pilar de 8.000 mm?", "8000//500", "Se divide la altura entre 500.", " mm"),
        ("abc", "{F} El registro de ejemplo anota «pilares: cumplen» y los tres pilares medidos son P-1, P-2 y P-3. ¿Es correcto?", "No: P-3 está fuera de tolerancia y el registro debe decirlo", "Sí: dos de tres cumplen, que es la mayoría", "Sí: la tolerancia es solo una sugerencia", "Un registro verdadero muestra el pilar que no cumple."),
    ],
    ctx=("abc", "Al verificar una estructura de ejemplo, el jefe te pide dejar sin anotar un pilar que se pasó 2 mm del máximo «porque es poco». ¿Qué respondes?", "Que se registra con su valor real como no conformidad y se informa al responsable", "Que no se anota si es poco", "Que se anota como cumple", "El tamaño del incumplimiento no autoriza a ocultarlo."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es el plomo?", "La dirección vertical", "El plomo es la referencia de la vertical."),
        ("¿Cómo se acepta una lectura de nivel?", "Si está entre el valor del plano menos y más la tolerancia", "Los límites del rango también se aceptan."),
        ("¿Qué se hace con un elemento fuera de tolerancia?", "Se registra y se informa al responsable", "La corrección la decide el responsable."),
    ],
    op=("Caso de ejemplo: un pilar de 5.000 mm (desplome máximo: altura entre 500) con desplome medido de 9 mm; una placa a 150 mm con tolerancia ± 2 mm y lectura de 153 mm; una base de 800 × 600 mm con diagonal teórica de 1.000 mm, diagonales medidas de 1.001 y 999 mm y diferencia máxima admitida de 3 mm. Escribe (a) el desplome máximo y si el pilar cumple, (b) si la placa cumple, (c) si la base está en escuadra, (d) cómo registrarías lo que no cumpla.",
        "(a) 5.000 ÷ 500 = 10 mm, y 9 mm cumple. (b) Los límites son 148 y 152 mm, y 153 mm no cumple. (c) La diferencia es 2 mm, no supera 3 mm: está en escuadra. (d) Con su valor real, como no conformidad, informando al responsable.",
        ["calcula el desplome máximo", "evalúa la placa", "evalúa la escuadra", "describe el registro"],
        ["hoja con las cuatro respuestas"],
        ["aceptar una lectura que supera el máximo", "comparar con una diagonal en vez de con la diferencia", "no registrar la no conformidad"],
        "Pregunta: «¿cuál es el límite máximo de nivel de la placa?». Si responde 150, pídele que relea la tolerancia."),
    reinforce="Inventa una altura de pilar, calcula su desplome máximo con altura entre 500 y escribe una lectura que cumpla y otra que no.",
    extend="Explica con un ejemplo por qué la escuadra de una base de pernos importa antes de apoyar el pilar.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 23 (caso de ejemplo, inventado). En «Estructuras Demo» hay 24 equipos: 8 máquinas, 10 herramientas eléctricas manuales, 4 instrumentos de medición y 2 equipos de limpieza. "
     "Peligros del mantenimiento anotados: energía residual (el equipo se mueve o arranca solo aunque parezca apagado), partes giratorias, cables dañados, aceites y solventes. Pauta de mantenimiento al día: 18 de los 24 equipos.")
build(
    O6, 1, F,
    use="Aprenderé qué es el mantenimiento básico, qué peligros tiene intervenir equipos, qué es el bloqueo y etiquetado y qué tareas les corresponden a quienes usan los equipos y cuáles a los mantenedores autorizados.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé calcular porcentajes.", "Sé que una tarea de riesgo exige autorización."],
    explain=[
        "El mantenimiento es el conjunto de cuidados que mantienen un instrumento, una herramienta o una máquina funcionando de forma segura y confiable. El mantenimiento básico que corresponde a quien usa el equipo es inspeccionarlo antes de usarlo, mantenerlo limpio y ordenado, guardarlo bien, registrar lo que observa y reportar cualquier falla. Las intervenciones técnicas, como abrir una máquina, las hace un mantenedor autorizado. El equipo dañado se rotula como fuera de servicio y se informa.",
        "Intervenir un equipo tiene peligros propios. La energía residual es la que queda en un equipo aunque parezca apagado y puede moverlo, hacerlo arrancar o descargarse. Por eso, antes de intervenir, personal autorizado aplica el bloqueo y etiquetado, una medida en que deja el equipo sin energía y lo marca para que nadie lo encienda. Esa medida la definen la empresa y la norma vigente, y este cuaderno no la enseña. Un interruptor apagado no basta.",
        f"La pauta de mantenimiento es el documento que dice qué revisar y cada cuánto. Registrar y reportar es una conducta de seguridad: ayuda a evitar fallas mayores. {EMER} {AVISO}",
    ],
    vocab=[("mantenimiento", "cuidados que mantienen un equipo funcionando de forma segura"), ("energía residual", "energía que queda en un equipo aunque parezca apagado"), ("bloqueo y etiquetado", "medida en que personal autorizado deja un equipo sin energía y lo marca antes de intervenirlo"), ("pauta de mantenimiento", "documento que dice qué revisar en un equipo y cada cuánto"), ("fuera de servicio", "equipo rotulado para que nadie lo use"), ("mantenedor autorizado", "persona con formación y permiso para intervenir equipos")],
    worked=[
        ("Porcentaje de pautas al día", "En otra sección de ejemplo, 7 de 10 equipos tienen su pauta al día. ¿Qué porcentaje es?", ["Se multiplican por 100 los equipos al día y se divide entre el total.", "7 por 100 son 700, y 700 entre 10 son 70."], "70 %"),
        ("Equipo dañado", "Un operador de ejemplo encuentra el mango de una herramienta rajado antes de usarla. ¿Qué corresponde?", ["Una herramienta dañada no se usa.", "Se rotula como fuera de servicio y se informa al responsable."], "No usarla, rotularla e informar"),
    ],
    mistakes=[("Creer que un equipo con el interruptor apagado está seguro para intervenir.", "Puede quedar energía residual o alguien puede encenderlo.", "Solo personal autorizado interviene, tras dejarlo sin energía y marcarlo."),
              ("Arreglar por cuenta propia un cable dañado con cinta y seguir usando la herramienta.", "Es una reparación improvisada que deja el peligro activo.", "Deja de usarla, rotúlala e informa al responsable.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es el mantenimiento?", "El conjunto de cuidados que mantienen un equipo funcionando de forma segura", "La compra de equipos nuevos", "La reparación que solo se hace después de un accidente", "El mantenimiento incluye cuidados previos y no solo reparaciones."),
        ("abc", "En Construcciones Metálicas: ¿qué es la energía residual?", "Energía que queda en un equipo aunque parezca apagado y puede moverlo o dañarlo", "La energía que gasta al encenderse", "El calor que despide mientras trabaja", "La energía residual persiste después de apagar el equipo."),
        ("abc", "En Construcciones Metálicas: ¿qué es el bloqueo y etiquetado?", "Una medida en que personal autorizado deja un equipo sin energía y lo marca antes de intervenirlo", "Poner un candado en la bodega de herramientas", "Pegar una etiqueta con el precio del equipo", "Es una medida de seguridad para intervenir equipos, no un candado de bodega."),
        ("=", "{F} ¿Cuántos equipos hay en total?", "8+10+4+2", "Se suman máquinas, herramientas, instrumentos y equipos de limpieza.", " equipos"),
        ("=", "{F} ¿Cuántos equipos no tienen su pauta de mantenimiento al día?", "24-18", "Se resta al total los equipos que sí la tienen.", " equipos"),
        ("=", "{F} ¿Qué porcentaje de los equipos tiene su pauta al día?", "18*100//24", "Se multiplican por 100 los equipos al día y se divide entre el total.", " %"),
        ("abc", "{F} Un operador nota un cable dañado en una herramienta eléctrica. ¿Qué corresponde?", "Dejar de usarla, rotularla como fuera de servicio y avisar al responsable", "Cubrir el cable con cinta y seguir", "Usarla hasta terminar el turno", "Un cable dañado es un peligro; arreglarlo a la rápida lo deja activo."),
        ("abc", "{F} Un practicante quiere abrir una máquina para «ver qué tiene», sin que nadie la haya dejado sin energía. ¿Qué corresponde?", "No intervenirla: abrir equipos es tarea de personal autorizado tras dejarlos sin energía", "Abrirla si está apagada con el interruptor", "Abrirla si usa guantes", "Un interruptor apagado no elimina la energía residual."),
        ("abc", "{F} Una etiqueta de «equipo fuera de servicio» pegada a una herramienta es:", "Un control administrativo, porque informa y ordena no usarla", "Un control de ingeniería", "Un EPP", "La etiqueta informa; no cambia físicamente el equipo."),
        ("abc", "En una visita de ejemplo, una máquina arranca sola mientras alguien la limpia y le atrapa la mano. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a tirar de la mano atrapada", "Esperar a ver si se suelta sola", "Intervenir sin formación puede agravar el daño; se avisa a quienes pueden actuar."),
        ("abc", "{F} ¿Por qué un interruptor apagado no basta para intervenir una máquina?", "Porque puede quedar energía residual o alguien puede encenderla, y por eso se bloquea y etiqueta", "Porque los interruptores no funcionan", "Porque apagar ensucia la máquina", "El riesgo de un arranque inesperado persiste mientras no se aplique el bloqueo."),
        ("=", "{F} Se ponen al día las pautas de 4 de los 6 equipos atrasados. ¿Cuántos equipos quedan con pauta al día?", "18+4", "Se suman los equipos puestos al día a los que ya la tenían.", " equipos"),
        ("abc", "{F} Con 22 de 24 equipos al día, el jefe dice «ya está, no hay más que hacer». ¿Qué respondes?", "Que faltan 2 equipos y que la pauta debe cumplirse siempre, no solo cuando se mide", "Que estás de acuerdo con el jefe", "Que 22 es suficiente si los equipos restantes son de baja importancia", "Una pauta incompleta deja equipos sin cuidado y con riesgo."),
    ],
    ctx=("abc", "Una compañera propone engrasar y revisar «rápido» un taladro de otro taller de ejemplo mientras sigue enchufado, porque «es solo un minuto». ¿Qué respondes?", "Que no: intervenir un equipo es tarea de personal autorizado y con el equipo sin energía, y que avisarás al responsable", "Que sí, si ella tiene cuidado", "Que sí, si usan guantes", "Un equipo enchufado puede moverse o descargarse; la intervención no se hace a la rápida."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es la energía residual?", "Energía que queda en un equipo aunque parezca apagado", "Puede mover o hacer arrancar el equipo inesperadamente."),
        ("¿Quién interviene técnicamente un equipo?", "Un mantenedor autorizado", "La intervención exige formación y permiso."),
        ("¿Qué se hace con un equipo dañado?", "Se rotula fuera de servicio y se informa", "Así nadie lo usa mientras no se repare."),
    ],
    op=("Caso de ejemplo: una sección tiene 20 equipos y 16 con pauta al día; un compañero encuentra un esmeril con el cable pelado. Escribe (a) qué porcentaje tiene su pauta al día, (b) qué haces con el esmeril, (c) por qué no se interviene un equipo solo con apagar el interruptor, (d) qué tipo de control es la etiqueta de fuera de servicio.",
        "(a) 16 × 100 ÷ 20 = 80 %. (b) Dejo de usarlo, lo rotulo como fuera de servicio y aviso al responsable. (c) Porque puede quedar energía residual o alguien puede encenderlo; por eso personal autorizado lo bloquea y etiqueta. (d) Un control administrativo, porque informa y ordena no usarlo.",
        ["calcula el porcentaje", "indica qué hacer con el esmeril", "explica la energía residual", "clasifica la etiqueta"],
        ["hoja con las cuatro respuestas"],
        ["arreglar el cable con cinta", "creer que el interruptor basta", "confundir la etiqueta con un control de ingeniería"],
        "Pregunta: «¿quién interviene el esmeril después?». Si responde que tú, pídele que relea la sección de mantenedores."),
    reinforce="Escribe tres cuidados básicos que le corresponden a quien usa una herramienta, sin intervenirla.",
    extend="Explica con un ejemplo por qué reportar un ruido extraño en una máquina es una conducta de seguridad.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 24 (tabla de ejemplo, inventada). Torno T1: mantenimiento preventivo cada 200 horas de uso; horas de uso acumuladas, 650; último preventivo realizado a las 600 horas; se usa 50 horas por semana. "
     "Esmeril E2: se reparó tras una falla. Pie de metro D3: calibración anual. Taladro K4: se cambió un componente porque una medición de vibración mostró desgaste. "
     "Definiciones del taller: preventivo es el que se hace antes de la falla, según calendario; correctivo, el que se hace después de la falla; predictivo, el que se decide según la medición del estado del equipo.")
build(
    O6, 2, F,
    use="Aprenderé los tipos de mantenimiento (preventivo, correctivo y predictivo), qué es la hoja de vida, la pauta y la orden de mantenimiento, y a calcular cuándo toca el siguiente preventivo.",
    prior=["Sé qué es el mantenimiento básico.", "Sé sumar, restar y dividir.", "Sé que un registro debe decir la verdad."],
    explain=[
        "El mantenimiento preventivo se hace antes de que el equipo falle, según un calendario o un número de horas de uso. El correctivo se hace después de la falla para repararla. El predictivo se decide según una medición del estado del equipo, como la vibración o la temperatura, que anticipa el desgaste. Los tres buscan que el equipo funcione de forma segura, pero el preventivo y el predictivo intentan evitar la falla y el correctivo llega cuando ya ocurrió.",
        "Los documentos del mantenimiento son tres. La pauta de mantenimiento dice qué revisar y cada cuánto. La orden de mantenimiento encarga una intervención concreta a un mantenedor autorizado. La hoja de vida es el historial de un equipo: horas de uso, fallas, intervenciones y calibraciones. Para saber cuándo toca el siguiente preventivo se suma la frecuencia a las horas del último, y las horas que restan son esa meta menos las horas acumuladas.",
        f"Quien usa el equipo anota lo que observa, como un ruido extraño, y avisa; las intervenciones las hace el mantenedor autorizado. {EMER} {AVISO}",
    ],
    vocab=[("preventivo", "mantenimiento que se hace antes de la falla, según calendario u horas de uso"), ("correctivo", "mantenimiento que se hace después de la falla"), ("predictivo", "mantenimiento que se decide según la medición del estado del equipo"), ("hoja de vida", "historial de un equipo con horas, fallas e intervenciones"), ("orden de mantenimiento", "encargo de una intervención concreta a un mantenedor autorizado")],
    worked=[
        ("Reconocer el tipo", "En otro taller de ejemplo, una bomba se reparó después de que dejó de funcionar. ¿Qué tipo de mantenimiento fue?", ["Se hizo después de la falla.", "Eso es mantenimiento correctivo."], "Correctivo"),
        ("Próximo preventivo", "Un equipo de ejemplo tiene preventivo cada 150 horas y el último fue a las 450 horas. ¿A cuántas horas toca el siguiente?", ["Se suma la frecuencia al último.", "450 más 150 son 600."], "A las 600 horas"),
    ],
    mistakes=[("Creer que si el equipo funciona bien se puede saltar el preventivo.", "El preventivo busca evitar fallas antes de que se noten.", "Cumple el calendario de la pauta."),
              ("Dejar de anotar un ruido extraño por parecer poco importante.", "Ese aviso puede evitar una falla mayor y el historial queda incompleto.", "Anótalo y avisa al responsable.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es el mantenimiento preventivo?", "El que se hace antes de la falla, según calendario u horas de uso", "El que se hace después de que el equipo se rompe", "El que se decide solo cuando el jefe lo pide", "Preventivo significa anticiparse a la falla."),
        ("abc", "En Construcciones Metálicas: ¿qué es el mantenimiento correctivo?", "El que se hace después de la falla para repararla", "El que se hace según un calendario", "El que se decide según la vibración medida", "El correctivo ocurre cuando la falla ya existe."),
        ("abc", "En Construcciones Metálicas: ¿qué es el mantenimiento predictivo?", "El que se decide según una medición del estado del equipo", "El que se hace siempre cada mes", "El que se hace sin avisar a nadie", "Predictivo se apoya en mediciones que anticipan el desgaste."),
        ("abc", "{F} ¿Qué tipo de mantenimiento fue la reparación del esmeril E2?", "Correctivo, porque se hizo tras una falla", "Preventivo, porque se hizo en el taller", "Predictivo, porque se midió el esmeril", "La reparación después de la falla es correctiva."),
        ("abc", "{F} ¿Qué tipo fue el cambio de componente del taladro K4?", "Predictivo, porque la medición de vibración mostró desgaste", "Correctivo, porque falló el taladro", "Preventivo, porque se cambió por calendario", "La decisión se apoyó en una medición del estado, es predictiva."),
        ("=", "{F} ¿A cuántas horas de uso toca el próximo mantenimiento preventivo del torno T1?", "600+200", "Se suma la frecuencia a las horas del último preventivo.", " horas"),
        ("=", "{F} ¿Cuántas horas de uso le quedan al torno T1 hasta ese preventivo?", "600+200-650", "Se resta a la meta las horas acumuladas.", " horas"),
        ("abc", "{F} ¿Qué documento registra el historial de un equipo, con horas de uso, fallas e intervenciones?", "La hoja de vida", "La orden de trabajo de fabricación", "La matriz de peligros", "La hoja de vida es el historial del equipo."),
        ("abc", "{F} ¿Qué diferencia hay entre el mantenimiento preventivo y el correctivo?", "El preventivo se hace antes de la falla y el correctivo después de ella", "El preventivo lo hace cualquier persona y el correctivo un especialista", "Ninguna, son nombres distintos del mismo mantenimiento", "La diferencia está en el momento respecto de la falla."),
        ("abc", "{F} Un operador no anota que oyó un ruido extraño en T1. ¿Por qué es un error?", "Porque ese aviso puede evitar una falla mayor y el historial queda incompleto", "Porque los ruidos son siempre normales", "Porque anotar reemplaza la reparación", "Un aviso a tiempo permite intervenir antes de que la falla crezca."),
        ("abc", "En Construcciones Metálicas: ¿quién realiza el mantenimiento técnico de una máquina?", "Un mantenedor autorizado", "Quien tenga tiempo libre", "Cualquier operador, si usa guantes", "La intervención técnica exige formación y autorización."),
        ("=", "{F} ¿En cuántas semanas llega T1 a su próximo preventivo, con el uso semanal de la ficha?", "(600+200-650)//50", "Se divide las horas que faltan entre las horas de uso por semana.", " semanas"),
        ("abc", "{F} Un compañero propone saltarse el preventivo porque «T1 funciona bien». ¿Qué respondes?", "Que el preventivo busca evitar fallas antes de que se noten, y su calendario lo fija la pauta", "Que tiene razón, si no falla no se hace", "Que se salta si hay apuro", "El calendario existe justamente para anticiparse a fallas que aún no se ven."),
    ],
    ctx=("abc", "El jefe de turno de ejemplo te dice que anotes en la hoja de vida que el preventivo se hizo, aunque se atrasó dos semanas. ¿Qué respondes?", "Que se anota la fecha real del preventivo, con el atraso, porque la hoja de vida debe decir la verdad", "Que se anota la fecha en que debía hacerse", "Que no se anota nada", "La hoja de vida es un registro verdadero; no se ajusta al calendario."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es la hoja de vida de un equipo?", "El historial con horas de uso, fallas e intervenciones", "Permite conocer el estado y la historia del equipo."),
        ("¿Cómo se calcula el próximo preventivo?", "Sumando la frecuencia a las horas del último", "Marca la meta de horas para la siguiente intervención."),
        ("¿Qué tipo de mantenimiento se apoya en mediciones del estado?", "El predictivo", "Las mediciones permiten anticipar el desgaste del equipo."),
    ],
    op=("Caso de ejemplo: una sierra tiene preventivo cada 120 horas, el último fue a las 360 horas y lleva 440 horas acumuladas; se usa 20 horas por semana. Un compresor se reparó tras fallar y un ventilador se cambió porque la vibración medida subió. Escribe (a) a qué horas toca el próximo preventivo, (b) cuántas semanas faltan, (c) qué tipo de mantenimiento fue cada reparación, (d) qué documento registra todo.",
        "(a) 360 + 120 = 480 horas. (b) 480 − 440 = 40 horas, que son 2 semanas. (c) El compresor: correctivo; el ventilador: predictivo. (d) La hoja de vida del equipo.",
        ["calcula la meta de horas", "calcula las semanas", "clasifica los tipos", "nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["olvidar sumar la frecuencia", "confundir correctivo con predictivo", "no nombrar la hoja de vida"],
        "Pregunta: «¿qué se midió en el ventilador antes de cambiarlo?». Si no responde, pídele que relea el mantenimiento predictivo."),
    reinforce="Inventa tres equipos y clasifica una intervención de cada uno como preventiva, correctiva o predictiva.",
    extend="Explica con un ejemplo por qué la hoja de vida ayuda a decidir cuándo cambiar un equipo.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 25 (datos de ejemplo, inventados). Inventario de cinco instrumentos con el tiempo transcurrido desde su última calibración: I-1, huincha, hace 5 meses; I-2, pie de metro digital, hace 11 meses; I-3, pie de metro análogo, hace 13 meses; I-4, escuadra, hace 8 meses; I-5, nivel, hace 12 meses. "
     "Regla de la pauta de ejemplo: calibración cada 12 meses; el instrumento se considera vigente hasta el mes 12 inclusive. Herramientas manuales: 10 en el taller, 9 con inspección previa registrada hoy; una tiene el mango rajado. Costo de ejemplo de calibrar un instrumento: $2.000.")
build(
    O6, 3, F,
    use="Aprenderé en papel los cuidados generales de los instrumentos y las herramientas manuales, a revisar fechas de calibración y a registrar la inspección previa.",
    prior=["Sé qué es una calibración y un certificado.", "Sé restar y calcular porcentajes.", "Sé que un equipo dañado no se usa."],
    explain=[
        "Los instrumentos de medición se cuidan para que sus lecturas sean confiables: se guardan limpios, secos y protegidos de golpes, y no se usan como si fueran otra herramienta. Su calibración se repite según la pauta y su fecha se registra; un instrumento con calibración vencida no se usa para un control formal hasta que lo calibren. Los meses que faltan para el vencimiento son la frecuencia menos los meses transcurridos.",
        "Las herramientas manuales se inspeccionan antes de usarlas, a simple vista: mango sano, sin grietas, piezas firmes, cables sin daño. Esa inspección previa se registra. Una herramienta dañada se retira de uso, se rotula como fuera de servicio y se informa; no se repara con soluciones improvisadas. Mantener esos registros permite ver qué equipos están al día y cuáles requieren atención.",
        f"Estos cuidados orientan; la calibración la hace un servicio autorizado y la reparación, un mantenedor autorizado. {EMER} {AVISO}",
    ],
    vocab=[("calibración vigente", "calibración dentro del plazo que fija la pauta"), ("inspección previa", "revisión a simple vista de una herramienta antes de usarla"), ("fuera de servicio", "equipo rotulado para que nadie lo use"), ("servicio autorizado", "entidad habilitada para calibrar instrumentos")],
    worked=[
        ("Meses que faltan", "Con calibración cada 12 meses, un instrumento de ejemplo fue calibrado hace 9 meses. ¿Cuántos meses le faltan?", ["Se resta lo transcurrido a la frecuencia.", "12 menos 9 son 3."], "3 meses"),
        ("Porcentaje inspeccionado", "En otro taller de ejemplo, 14 de 20 herramientas tuvieron inspección previa. ¿Qué porcentaje es?", ["Se multiplican por 100 las inspeccionadas y se divide entre el total.", "14 por 100 son 1.400, y 1.400 entre 20 son 70."], "70 %"),
    ],
    mistakes=[("Seguir usando un instrumento vencido «porque da lecturas parecidas».", "Sin calibración vigente no se sabe cuánto se equivoca.", "No lo uses para un control formal y envíalo a calibrar."),
              ("Envolver con cinta el mango rajado y seguir trabajando.", "Es una reparación improvisada que deja el peligro activo.", "Retira la herramienta, rotúlala e informa.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿cómo se guarda un instrumento de medición?", "Limpio, seco y protegido de golpes", "Suelto en una caja con herramientas pesadas", "Húmedo, para que no se seque", "Los golpes y la humedad dañan la lectura del instrumento."),
        ("abc", "En Construcciones Metálicas: ¿por qué se inspecciona una herramienta antes de usarla?", "Para detectar daños visibles y no usarla si está dañada", "Para que se caliente", "Para registrar quién la usó", "La inspección previa busca daños que puedan causar un accidente."),
        ("=", "{F} ¿Cuántos meses le faltan para vencer a la huincha I-1?", "12-5", "Se resta lo transcurrido a la frecuencia de calibración.", " meses"),
        ("=", "{F} ¿Cuántos meses le faltan para vencer al pie de metro digital I-2?", "12-11", "Se resta lo transcurrido a la frecuencia de calibración.", " mes"),
        ("abc", "{F} ¿Qué instrumento está vencido según la regla de la ficha?", "Solo I-3, calibrado hace 13 meses", "I-3 e I-5", "Ninguno", "La regla acepta hasta el mes 12 inclusive; solo I-3 lo supera."),
        ("abc", "{F} ¿Qué corresponde hacer con I-3?", "No usarlo para un control formal y enviarlo a calibrar", "Usarlo hasta fin de mes", "Cambiar la fecha en la tabla", "Un instrumento vencido deja la medida en duda hasta calibrarlo."),
        ("=", "{F} ¿Cuántos de los cinco instrumentos están vigentes?", "5-1", "Se resta al total el instrumento vencido.", " instrumentos"),
        ("=", "{F} ¿Qué porcentaje de los instrumentos está vigente?", "4*100//5", "Se multiplican por 100 los vigentes y se divide entre el total.", " %"),
        ("abc", "{F} Un compañero dice que I-5, calibrado hace 12 meses, ya venció. ¿Qué respondes?", "Según la regla sigue vigente hasta el mes 12 inclusive, pero conviene programar su calibración ya", "Tiene razón: venció", "Está vigente por 6 meses más", "El plazo incluye el mes 12; aun así, se programa antes de pasarlo."),
        ("abc", "{F} En la inspección previa se encuentra una herramienta con el mango rajado. ¿Qué corresponde?", "No usarla, rotularla como fuera de servicio y avisar", "Usarla con guantes gruesos", "Envolver el mango con cinta y usarla", "Un mango rajado puede romperse en uso; no se repara a la rápida."),
        ("=", "{F} ¿Qué porcentaje de las herramientas manuales tuvo inspección previa registrada hoy?", "9*100//10", "Se multiplican por 100 las inspeccionadas y se divide entre el total.", " %"),
        ("abc", "En Construcciones Metálicas: ¿por qué se registra el resultado de la inspección previa de las herramientas?", "Para tener evidencia de qué se revisó y detectar fallas que se repiten", "Para llenar el cuaderno del taller", "Para que la herramienta dure más sin revisarla", "El registro prueba la revisión y muestra patrones de falla."),
        ("=", "{F} Se programa calibrar los instrumentos vencidos o que vencen dentro de 1 mes o antes (I-2, I-3 e I-5). ¿Cuántos pesos cuesta?", "3*2000", "Se multiplican los instrumentos por el costo de calibrar cada uno.", " pesos"),
    ],
    ctx=("abc", "Un compañero usa un pie de metro de otro taller de ejemplo cuyo certificado venció hace tres meses, «porque nadie lo va a notar». ¿Qué le dices?", "Que no se usa para un control formal hasta calibrarlo, y que se informa al responsable", "Que lo use si lo cuida", "Que reste 1 mm a cada lectura", "La honestidad del control exige instrumentos con calibración vigente."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calculan los meses que faltan para vencer?", "Frecuencia de calibración menos meses transcurridos", "Resta cuánto se ha usado del plazo."),
        ("En Construcciones Metálicas: ¿qué se hace con una herramienta dañada?", "Se retira de uso, se rotula y se informa", "Evita que alguien la use por error."),
        ("¿Cómo se guarda un instrumento de medición?", "Limpio, seco y protegido de golpes", "Así conserva la confiabilidad de sus lecturas."),
    ],
    op=("Inventario de ejemplo: J-1, escuadra, calibrada hace 7 meses; J-2, huincha, hace 12 meses; J-3, nivel, hace 14 meses; J-4, pie de metro, hace 10 meses. Pauta de 12 meses, vigente hasta el mes 12 inclusive. De 8 herramientas manuales, 6 tuvieron inspección previa. Escribe (a) cuántos meses le faltan a J-1, (b) qué instrumentos están vencidos, (c) el porcentaje de herramientas inspeccionadas, (d) qué haces con un instrumento vencido.",
        "(a) 12 − 7 = 5 meses. (b) Solo J-3, con 14 meses. (c) 6 × 100 ÷ 8 = 75 %. (d) No lo uso para un control formal, lo rotulo y lo envío a calibrar, informando al responsable.",
        ["calcula los meses", "identifica el vencido", "calcula el porcentaje", "indica qué hacer"],
        ["hoja con las cuatro respuestas"],
        ["marcar J-2 como vencido", "dividir mal el porcentaje", "seguir usando el vencido"],
        "Pregunta: «¿J-2, a 12 meses, está vencido?». Si responde que sí, pídele que relea la regla."),
    reinforce="Haz una tabla de tres herramientas inventadas con la fecha de su última inspección y una columna «¿al día?».",
    extend="Explica con un ejemplo por qué es mejor programar la calibración antes de que venza.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 26 (datos de ejemplo, inventados). Torno T1, plan actual por mes: 200 horas programadas; 10 horas detenido por preventivo; 30 horas detenido por fallas; un preventivo de $50.000 y un correctivo de $180.000. "
     "Plan propuesto por mes: 200 horas programadas; 2 preventivos (20 horas detenido, $50.000 cada uno); 10 horas detenido por fallas, con un correctivo de $180.000 cada tres meses (equivale a $60.000 por mes). "
     "Disponibilidad = horas operativas × 100 ÷ horas programadas; horas operativas = horas programadas − horas detenido.")
build(
    O6, 4, F,
    use="Aprenderé a calcular la disponibilidad de un equipo y el costo mensual de su mantenimiento, y a comparar dos planes con datos para decidir.",
    prior=["Sé qué es el mantenimiento preventivo y correctivo.", "Sé calcular porcentajes.", "Sé que un registro debe decir la verdad."],
    explain=[
        "La disponibilidad de un equipo es la proporción del tiempo programado en que estuvo operativo. Se calcula restando a las horas programadas las horas detenido, multiplicando por 100 y dividiendo entre las horas programadas. Una disponibilidad alta significa que el equipo está listo cuando se lo necesita. Un equipo detenido por fallas pierde disponibilidad y además cuesta más, porque un correctivo suele ser más caro que un preventivo.",
        "Para comparar dos planes de mantenimiento se calculan, para cada uno, las horas operativas, la disponibilidad y el costo mensual, que es la suma del costo de las intervenciones. El mejor plan es el que logra más disponibilidad con un costo razonable, y la decisión se apoya en estos datos, no en la costumbre. Para que el cálculo sirva, las horas detenidas y los costos deben anotarse tal como ocurrieron.",
        f"Es una comparación de planilla con valores de ejemplo; la decisión final la toma el responsable. {EMER} {AVISO}",
    ],
    vocab=[("disponibilidad", "proporción del tiempo programado en que el equipo está operativo"), ("horas programadas", "horas en que se planea usar el equipo"), ("horas operativas", "horas programadas menos las horas detenido"), ("costo mensual", "suma de los costos de las intervenciones del mes")],
    worked=[
        ("Calcular disponibilidad", "Una máquina de ejemplo tiene 80 horas programadas y 8 horas detenida. ¿Qué disponibilidad tiene?", ["Las horas operativas son 80 menos 8, es decir, 72.", "72 por 100 son 7.200, y 7.200 entre 80 son 90."], "90 %"),
        ("Costo mensual", "Un plan de ejemplo tiene 2 intervenciones de $30.000 y una de $90.000 en el mes. ¿Cuál es el costo mensual?", ["Se multiplican las dos primeras: 2 por 30.000 son 60.000.", "Se suma la tercera: 60.000 más 90.000 son 150.000."], "$150.000"),
    ],
    mistakes=[("Dejar sin multiplicar por 100 y escribir 0,8 como disponibilidad.", "El resultado debe expresarse en porcentaje.", "Multiplica por 100: 0,8 es 80 %."),
              ("Dejar de anotar las horas detenidas para que la disponibilidad se vea mejor.", "Sin datos reales no se pueden tomar buenas decisiones.", "Registra las horas tal como ocurrieron.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué mide la disponibilidad de un equipo?", "La proporción del tiempo programado en que estuvo operativo", "Cuántas piezas produjo", "El tiempo que tardó en repararse", "La disponibilidad compara horas operativas con horas programadas."),
        ("=", "{F} ¿Cuántas horas operativas tuvo T1 en el plan actual?", "200-10-30", "Se restan a las horas programadas las horas detenido.", " horas"),
        ("=", "{F} ¿Qué disponibilidad tiene T1 en el plan actual?", "(200-10-30)*100//200", "Se multiplican por 100 las horas operativas y se divide entre las programadas.", " %"),
        ("=", "{F} ¿Cuántos pesos cuesta el mantenimiento mensual del plan actual?", "50000+180000", "Se suman el preventivo y el correctivo.", " pesos"),
        ("=", "{F} ¿Cuántas horas operativas tendría T1 en el plan propuesto?", "200-20-10", "Se restan a las horas programadas las horas detenido.", " horas"),
        ("=", "{F} ¿Qué disponibilidad tendría T1 en el plan propuesto?", "(200-20-10)*100//200", "Se multiplican por 100 las horas operativas y se divide entre las programadas.", " %"),
        ("=", "{F} ¿Cuántos pesos costaría el mantenimiento mensual del plan propuesto?", "2*50000+60000", "Se suman dos preventivos y la parte mensual del correctivo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos al mes se ahorrarían con el plan propuesto?", "(50000+180000)-(2*50000+60000)", "Se resta el costo propuesto al costo actual.", " pesos"),
        ("abc", "{F} ¿Qué plan conviene según los datos?", "El propuesto: sube la disponibilidad de 80 % a 85 % y baja el costo mensual", "El actual, porque tiene menos preventivos", "Ninguno, porque ambos detienen la máquina", "El plan propuesto mejora la disponibilidad y el costo a la vez."),
        ("abc", "{F} ¿Por qué más mantenimiento preventivo puede reducir el costo total aunque cueste cada mes?", "Porque evita fallas que detienen más tiempo y cuestan más que las intervenciones planificadas", "Porque el preventivo es gratis", "Porque con preventivo las fallas desaparecen siempre", "El preventivo es un gasto planificado que evita gastos mayores."),
        ("abc", "{F} Un jefe propone no anotar las horas detenidas para que la disponibilidad se vea mejor. ¿Qué corresponde?", "Registrar los datos reales, porque sin ellos no se pueden tomar buenas decisiones", "No anotarlas", "Anotar solo la mitad", "Un dato falso lleva a decisiones equivocadas."),
        ("=", "{F} Si las horas programadas subieran a 250 y las horas detenido fueran las del plan propuesto (30 en total), ¿cuántas horas operativas tendría?", "250-30", "Se restan las horas detenido a las programadas.", " horas"),
        ("abc", "{F} Un compañero calcula 160 ÷ 200 = 0,8 y escribe «0,8 %» para el plan actual. ¿Qué error cometió?", "Olvidó multiplicar por 100: 0,8 equivale a 80 %", "Debió dividir entre 160", "No cometió ningún error", "La disponibilidad se expresa en porcentaje; 0,8 es la fracción 80/100."),
    ],
    ctx=("abc", "El supervisor de ejemplo quiere informar «disponibilidad 95 %» cuando los datos reales dan 80 %, para cumplir una meta. ¿Qué respondes?", "Que se informa el valor real de 80 %, y que si la meta no se cumple se estudian las causas", "Que informes 95 % para cumplir", "Que informes 90 % por si acaso", "Un indicador falso impide mejorar y es una falta de honestidad."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calcula la disponibilidad?", "Horas operativas por 100, divididas entre horas programadas", "Compara el tiempo operativo con el programado."),
        ("¿Cómo se calcula el costo mensual del mantenimiento?", "Sumando el costo de las intervenciones del mes", "Cada intervención del mes aporta su propio costo."),
        ("¿Qué hace falta para decidir entre dos planes?", "Datos reales de horas y costos de cada plan", "Sin datos reales la comparación no sirve."),
    ],
    op=("Plan actual de otra máquina de ejemplo: 100 horas programadas al mes, 10 horas detenida por preventivo y 20 por fallas; un preventivo de $40.000 y un correctivo de $120.000 al mes. Plan propuesto: 2 preventivos de $40.000 y 6 horas detenida por fallas con un correctivo de $48.000 equivalente por mes; el detenido por preventivo sube a 14 horas. Escribe (a) la disponibilidad del plan actual, (b) la del propuesto, (c) el costo mensual de cada plan, (d) qué plan conviene.",
        "(a) 100 − 10 − 20 = 70 horas; 70 × 100 ÷ 100 = 70 %. (b) 100 − 14 − 6 = 80 horas; 80 × 100 ÷ 100 = 80 %. (c) Actual: 40.000 + 120.000 = 160.000 pesos; propuesto: 2 × 40.000 + 48.000 = 128.000 pesos. (d) El propuesto, porque sube la disponibilidad y baja el costo.",
        ["calcula la disponibilidad actual", "calcula la propuesta", "calcula los costos", "decide con datos"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por 100", "no restar las horas de preventivo", "elegir sin comparar costos"],
        "Pregunta: «¿qué plan tiene más horas operativas?». Si no responde, pídele que reste las horas detenido de cada uno."),
    reinforce="Inventa una máquina con 100 horas programadas, calcula la disponibilidad con 12 horas detenida y escribe el cálculo.",
    extend="Explica con un ejemplo por qué una disponibilidad falsa puede producir un accidente o un gasto.",
)
