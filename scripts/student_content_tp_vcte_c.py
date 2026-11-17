"""Vestuario y Confección Textil TP (3.º y 4.º medio): OAE-06 (confección: secuencia de operaciones, tiempos, balanceo y cronograma; solo conceptos y cálculos), OAE-07 (terminaciones, planchado y empaquetado: etiquetado, composición y embalaje en términos de especificaciones) y OAE-08 (control de calidad: defectos, tolerancias y muestreo). Todo en papel, con datos de ejemplo."""
from __future__ import annotations

from tp_vcte_common import build

O6 = "TP-VCTE-3y4-OAE-06"
O7 = "TP-VCTE-3y4-OAE-07"
O8 = "TP-VCTE-3y4-OAE-08"
LIM = " Esto es aprendizaje conceptual en papel, con datos de ejemplo: la práctica en un taller de confección requiere instructor/docente de la especialidad y norma vigente; este cuaderno no te habilita para trabajar. Ante un accidente, avisa a un adulto responsable y a emergencias."
LIMX = " Las máquinas de coser, las planchas, el vapor, las tijeras, las agujas y los productos químicos se estudian aquí solo como concepto: su uso requiere instructor/docente de la especialidad y norma vigente; este cuaderno no te habilita para trabajar. Ante un accidente, avisa a un adulto responsable y a emergencias."

# ============================================================ OAE-06, clase 1
F = ("Ficha 22 (taller de confección de ejemplo, inventado). La confección es la etapa en que se unen las piezas cortadas siguiendo la secuencia de operaciones de la ficha técnica (lista ordenada de operaciones con sus tiempos), con los insumos requeridos y la maquinaria apropiada, controlando la calidad y la seguridad. "
     "Formas de organizar el trabajo: producción individual (una persona hace toda la prenda), por módulos (un equipo pequeño hace varias operaciones) y por línea (cada persona hace una operación y la prenda avanza). "
     "Roles: la supervisora de línea organiza al personal; las operarias realizan las operaciones; el control de calidad inspecciona durante el proceso. Reglas generales: la secuencia de la ficha no se cambia sin aprobación; las máquinas las usa solo personal capacitado y autorizado; se hacen pausas activas; el apuro no justifica saltarse una medida de seguridad ni un control de calidad.")
build(
    O6, 1, F,
    use="Aprenderé a situar la confección en un taller: cómo se organiza el trabajo, qué roles hay, qué riesgos existen y qué reglas se aplican; este cuaderno no enseña a coser.",
    prior=["Conozco la ficha técnica, el corte y los tipos de máquinas.", "Sé dividir y multiplicar con enteros.", "Sé que las máquinas requieren personal capacitado."],
    explain=[
        "En Vestuario y Confección Textil, la confección es la etapa en que se unen las piezas cortadas para formar la prenda. El orden de las operaciones está en la secuencia de operaciones de la ficha técnica, una lista ordenada con el tiempo de cada una. El trabajo se puede organizar de tres formas: individual, cuando una persona hace toda la prenda; por módulos, cuando un equipo pequeño hace varias operaciones; y por línea, cuando cada persona hace una operación y la prenda avanza. La línea conviene para grandes cantidades de un mismo modelo y la producción individual para pocas unidades o prendas a medida.",
        "El control de calidad se hace durante el proceso y no solo al final, porque así se detecta un defecto a tiempo y no se siguen fabricando prendas con el mismo error. La supervisora de línea organiza al personal, las operarias realizan las operaciones y el control de calidad inspecciona. La secuencia de la ficha no se cambia por cuenta propia: cualquier mejora se propone a la supervisora y la aprueban quienes responden por la ficha.",
        "Los riesgos son los pinchazos, el atrapamiento, el ruido, el calor, la pelusa y la mala postura por trabajar sentada muchas horas con movimientos repetidos. Se previenen con pausas activas, ajuste de la silla y la altura de trabajo, protecciones en las máquinas y personal capacitado. Si ocurre un accidente se avisa a un adulto responsable y a emergencias." + LIMX,
    ],
    vocab=[("confección", "etapa en que se unen las piezas cortadas para formar la prenda"), ("secuencia de operaciones", "lista ordenada de operaciones con su tiempo"), ("producción por línea", "cada persona hace una operación y la prenda avanza"), ("producción por módulos", "un equipo pequeño hace varias operaciones"), ("pausa activa", "pausa breve con movimientos para descansar el cuerpo"), ("control en proceso", "inspección durante la confección, no solo al final")],
    worked=[
        ("Elegir la organización", "Un taller de ejemplo debe hacer 1.000 prendas iguales del mismo modelo. ¿Qué organización conviene, individual o por línea?", ["Son muchas prendas iguales.", "Conviene la línea, porque reparte el trabajo por operación."], "Por línea"),
        ("Decidir ante el apuro", "Un pedido de ejemplo se atrasa y alguien propone omitir el control en proceso. ¿Qué corresponde?", ["El apuro no justifica saltarse un control.", "Se informa la situación a la jefatura y se busca otra solución."], "No omitir el control"),
    ],
    mistakes=[("Cambiar el orden de dos operaciones porque «así es más cómodo».", "La secuencia de la ficha está aprobada y puede afectar el resultado.", "Propón el cambio a la supervisora."),
              ("Trabajar toda la jornada sentada sin pausas.", "Produce fatiga y dolores.", "Haz pausas activas y ajusta la silla.")],
    T=[
        ("abc", "En Vestuario y Confección Textil: ¿qué es la secuencia de operaciones?", "Una lista ordenada de operaciones con su tiempo", "El dibujo de la prenda sobre una figura", "La lista de telas disponibles", "La secuencia indica qué se hace y en qué orden; el dibujo con figura es el figurín."),
        ("abc", "{F} ¿Cómo es la producción por línea?", "Cada persona hace una operación y la prenda avanza", "Una persona hace toda la prenda", "Un equipo pequeño hace varias operaciones", "Eso describe la línea; las otras son individual y por módulos."),
        ("abc", "{F} ¿Quién organiza al personal en la línea?", "La supervisora de línea", "El control de calidad", "La operaria de la última operación", "La ficha asigna la organización a la supervisora."),
        ("abc", "{F} ¿Qué dice la ficha sobre cambiar la secuencia de operaciones?", "No se cambia sin aprobación", "Se puede cambiar si es más rápido", "Se puede cambiar si lo pide una operaria", "La secuencia está aprobada y solo cambia con autorización."),
        ("abc", "En Vestuario y Confección Textil: ¿por qué se controla la calidad durante el proceso y no solo al final?", "Para detectar a tiempo un defecto y no seguir fabricando con el mismo error", "Para tener más registros que guardar", "Para que las operarias terminen antes", "Controlar en el proceso evita repetir el mismo defecto en muchas prendas."),
        ("abc", "{F} Un equipo de 5 personas hace varias operaciones de una prenda. ¿Qué forma de organización es?", "Producción por módulos", "Producción individual", "Producción por línea", "Un equipo pequeño que hace varias operaciones es un módulo."),
        ("=", "Un taller de ejemplo tiene 30 operarias organizadas en módulos de 5 personas. ¿Cuántos módulos hay?", "30//5", "Se divide el total de personas por las integrantes de cada módulo.", " módulos"),
        ("abc", "{F} La supervisora pide omitir un control en proceso para terminar un pedido atrasado. ¿Qué corresponde?", "No omitirlo e informar a la jefatura para buscar otra solución", "Omitirlo solo esta vez", "Pedir a las operarias que controlen al final", "El apuro no justifica saltarse un control de calidad."),
        ("abc", "Una operaria con 8 horas sentada y sin pausas siente dolor de cuello. ¿Qué medida general corresponde?", "Hacer pausas activas, ajustar la silla y la altura de trabajo, y avisar", "Seguir trabajando hasta que pase", "Trabajar más rápido para terminar antes", "Las pausas y el ajuste del puesto previenen la fatiga y los dolores."),
        ("abc", "Una operaria cree que otra secuencia es más rápida y la aplica sin avisar. ¿Qué es lo correcto?", "Proponer la mejora a la supervisora para que se evalúe y apruebe", "Aplicarla si le sale bien", "Aplicarla solo en prendas urgentes", "Una mejora debe evaluarse y aprobarse antes de cambiar la ficha."),
        ("abc", "Veinte prendas salieron con el mismo defecto porque nadie controló hasta el final. ¿Qué habría evitado el problema?", "Un control en proceso que lo detectara en las primeras prendas", "Producir menos prendas", "Cambiar el color del hilo", "El control en proceso detecta el defecto antes de repetirlo."),
        ("=", "Un taller de ejemplo tiene 4 módulos que producen 55 prendas por día cada uno. ¿En cuántos días cumple un pedido de 880 prendas?", "880//(4*55)", "Se divide el pedido por la producción diaria de todos los módulos.", " días"),
        ("abc", "{F} Una operaria invierte el orden de dos operaciones de la secuencia porque «le resulta más cómodo». ¿Qué puede ocurrir?", "La prenda puede no poder completarse bien o salir con un defecto, porque la secuencia es un orden aprobado", "Nada, porque el orden da igual", "Aumenta siempre la calidad", "La secuencia fija un orden en que algunas operaciones dependen de otras."),
    ],
    ctx=("abc", "{F} Un taller recibe un pedido de 2.000 poleras iguales. ¿Qué organización y qué control conviene?", "Producción por línea con control de calidad en proceso", "Producción individual con control solo al final", "Producción individual sin control", "Muchas prendas iguales se reparten por operación y se controlan durante el proceso."),
    sc=[
        ("En Vestuario y Confección Textil: ¿cuál es la diferencia entre producción por línea y por módulos?", "En la línea cada persona hace una operación; en el módulo un equipo hace varias", "Cambia cómo se reparte el trabajo."),
        ("¿Qué se hace antes de cambiar la secuencia de la ficha?", "Se propone y se obtiene aprobación", "Solo quienes aprueban la ficha pueden cambiarla."),
        ("¿Para qué sirven las pausas activas?", "Para prevenir la fatiga y los dolores", "Descansan el cuerpo de los movimientos repetidos."),
    ],
    op=("Un taller de ejemplo debe confeccionar 1.500 poleras iguales y 5 chaquetas a medida. Escribe: (a) qué organización usarías para cada pedido y por qué, (b) un control que harías durante el proceso y (c) una medida de prevención de salud para las operarias.",
        "(a) Las 1.500 poleras iguales, por línea, porque se reparte el trabajo por operación; las 5 chaquetas a medida, de forma individual, porque son pocas y distintas. (b) Revisar las primeras prendas de cada operación para detectar un defecto antes de repetirlo. (c) Hacer pausas activas y ajustar la silla y la altura de trabajo.",
        ["elige la organización para cada pedido y la justifica", "propone un control en proceso", "indica una medida de salud"],
        ["hoja con los tres puntos"],
        ["usar línea para prendas a medida", "dejar el control para el final", "no dar ninguna medida de salud"],
        "Pregunta: «¿cuándo conviene la línea?». Debe responder cuando hay muchas prendas iguales."),
    reinforce="Escribe una tabla con las tres formas de organizar la confección y un ejemplo de pedido para cada una.",
    extend="Explica con un ejemplo inventado por qué una mejora a la secuencia debe aprobarse antes de aplicarse.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 23 (secuencia de operaciones de ejemplo, polera PE-14, inventada). Operación 1, unir hombros: 1 minuto. Operación 2, unir mangas: 2 minutos. Operación 3, cerrar costados: 3 minutos. Operación 4, terminar el bajo: 4 minutos. Cada operación la hace una operaria. "
     "Tiempo estándar: el tiempo que se asigna a una operación hecha con método y ritmo normales. Turno efectivo: 420 minutos. Insumos por polera: 1 etiqueta de talla, 1 etiqueta de composición y 120 cm de hilo.")
build(
    O6, 2, F,
    use="Aprenderé los documentos y conceptos de la confección (secuencia, tiempo estándar, capacidad, cuello de botella y balanceo) y a calcular con ellos.",
    prior=["Conozco la secuencia de operaciones.", "Sé dividir con enteros.", "Sé leer una tabla de tiempos."],
    explain=[
        "El tiempo estándar es el tiempo que se asigna a una operación hecha con método y ritmo normales; lo determina un estudio de tiempos que aprueba la jefatura. La suma de los tiempos estándar de todas las operaciones es el tiempo total de la prenda. La capacidad de una operación en un turno es el tiempo efectivo del turno dividido por el tiempo estándar de esa operación, y dice cuántas prendas puede hacer una operaria en un turno.",
        "En una línea, la operación de menor capacidad es el cuello de botella y limita la producción de toda la línea, porque las demás no pueden producir más de lo que esa operación deja pasar. Balancear la línea es repartir las operaciones y las personas de modo que las capacidades sean parejas y ninguna operación acumule prendas esperando. Para eso se puede asignar más de una operaria a la operación más lenta.",
        "La ficha también lista los insumos requeridos por prenda, como etiquetas e hilo. Con ellos se calcula cuánto material se necesita para un pedido multiplicando por la cantidad. Los tiempos estándar no se modifican por cuenta propia: si una operaria cree que son incorrectos, lo informa a la supervisora." + LIM,
    ],
    vocab=[("tiempo estándar", "tiempo asignado a una operación hecha con método y ritmo normales"), ("tiempo total de la prenda", "suma de los tiempos estándar de todas las operaciones"), ("capacidad de una operación", "prendas que se pueden hacer en un turno: tiempo del turno dividido por el tiempo de la operación"), ("cuello de botella", "operación de menor capacidad, que limita toda la línea"), ("balancear la línea", "repartir operaciones y personas para que las capacidades sean parejas")],
    worked=[
        ("Capacidad de una operación", "En un turno de ejemplo de 360 minutos efectivos, una operación tiene 6 minutos de tiempo estándar. ¿Cuántas prendas se pueden hacer?", ["Se divide el tiempo del turno por el tiempo de la operación.", "360 ÷ 6 = 60."], "60 prendas"),
        ("Identificar el cuello de botella", "Una línea de ejemplo tiene capacidades de 90, 60 y 120 prendas por turno. ¿Cuál limita la producción?", ["Limita la menor capacidad.", "Es la de 60 prendas."], "La operación de 60 prendas"),
    ],
    mistakes=[("Agregar personas a la operación más rápida para producir más.", "La línea sigue limitada por el cuello de botella.", "Agrega apoyo a la operación más lenta."),
              ("Cambiar un tiempo estándar porque «a mí me sale en menos».", "El tiempo estándar lo fija un estudio de tiempos.", "Informa a la supervisora.")],
    T=[
        ("=", "{F} ¿Cuál es el tiempo total de una polera, en minutos?", "1+2+3+4", "Se suman los tiempos estándar de las cuatro operaciones.", " minutos"),
        ("abc", "{F} ¿Qué operación demora más?", "La operación 4, terminar el bajo", "La operación 1, unir hombros", "La operación 2, unir mangas", "El bajo tiene el mayor tiempo estándar, 4 minutos."),
        ("abc", "En Vestuario y Confección Textil: ¿qué es el tiempo estándar?", "El tiempo asignado a una operación hecha con método y ritmo normales", "El tiempo más corto que alguien logró una vez", "El tiempo total del turno", "El tiempo estándar se fija con un estudio de tiempos y no con un caso aislado."),
        ("=", "{F} ¿Cuántas prendas puede hacer una operaria en la operación 3 en un turno?", "420//3", "Se divide el turno efectivo por el tiempo estándar de la operación.", " prendas"),
        ("=", "{F} ¿Cuántas prendas puede hacer una operaria en la operación 4 en un turno?", "420//4", "Se divide el turno efectivo por el tiempo de la operación 4.", " prendas"),
        ("abc", "{F} Con una operaria por operación, ¿cuál es el cuello de botella?", "La operación 4, porque tiene la menor capacidad", "La operación 1, porque va primero", "La operación 3, porque va en el medio", "La menor capacidad la tiene la operación de mayor tiempo."),
        ("=", "{F} ¿Cuántas poleras produce la línea en un turno, con una operaria por operación?", "420//4", "La línea produce lo que permite el cuello de botella.", " poleras"),
        ("abc", "En Vestuario y Confección Textil: ¿qué significa balancear una línea?", "Repartir operaciones y personas para que las capacidades sean parejas", "Hacer que todas las operarias trabajen más rápido", "Aumentar el tiempo estándar de cada operación", "Balancear busca parejar las capacidades y que no se acumulen prendas."),
        ("=", "{F} ¿Cuántos metros de hilo se necesitan para 200 poleras?", "200*120//100", "Se multiplican los cm por polera por el pedido y se pasan a metros.", " metros"),
        ("abc", "{F} La supervisora propone agregar operarias a la operación 1 para aumentar la producción. ¿Qué ocurre?", "No aumenta la producción de la línea, porque el cuello de botella sigue siendo la operación 4", "Aumenta mucho la producción", "Se reduce el tiempo total de la prenda", "Una operación más rápida no sube la producción mientras el cuello de botella no cambie."),
        ("abc", "Una operaria mide que ella hace la operación 3 en 2 minutos y propone cambiar la ficha. ¿Qué corresponde?", "Informar a la supervisora, porque el tiempo estándar lo fija un estudio de tiempos aprobado", "Cambiar el tiempo en la ficha", "Hacer solo esa operación", "Un tiempo individual no reemplaza al estándar aprobado."),
        ("=", "{F} Se asigna una segunda operaria a la operación 4, de modo que dos operarias la hacen a la vez. ¿Cuántas poleras produce ahora la línea por turno?", "420//3", "La operación 4 sube a 210, pero la operación 3 pasa a ser el nuevo cuello de botella con 140.", " poleras"),
        ("abc", "{F} ¿Por qué no se cambia el orden de las operaciones de la secuencia?", "Porque algunas operaciones dependen de otras y la secuencia está aprobada", "Porque el orden siempre es alfabético", "Porque el cambio aumenta el tiempo estándar", "El orden es parte de la ficha aprobada y asegura un resultado coherente."),
    ],
    ctx=("=", "{F} Un pedido es de 300 poleras. ¿Cuántos turnos necesita la línea actual (una operaria por operación) para completarlo, redondeando hacia arriba?", "(300+420//4-1)//(420//4)", "Se divide el pedido por la producción de un turno y se redondea hacia arriba.", " turnos"),
    sc=[
        ("En Vestuario y Confección Textil: ¿cómo se calcula la capacidad de una operación en un turno?", "Dividiendo el turno efectivo por su tiempo estándar", "Indica cuántas prendas puede hacer en el turno."),
        ("¿Qué limita la producción de una línea?", "El cuello de botella", "Es la operación de menor capacidad."),
        ("¿Quién fija el tiempo estándar?", "Un estudio de tiempos aprobado por la jefatura", "Un tiempo individual no lo reemplaza."),
    ],
    op=("Secuencia de ejemplo de un delantal: operación 1, 2 minutos; operación 2, 5 minutos; operación 3, 3 minutos; turno efectivo de 420 minutos; una operaria por operación. Escribe: (a) la capacidad de cada operación, (b) el cuello de botella y cuánto produce la línea, (c) qué operación reforzarías con una segunda operaria y (d) cuántas prendas por turno produciría entonces la línea.",
        "(a) Operación 1: 210. Operación 2: 84. Operación 3: 140. (b) La operación 2, con 84 prendas por turno; la línea produce 84. (c) Reforzaría la operación 2 con una segunda operaria. (d) La operación 2 pasa a 168, y el nuevo cuello de botella es la operación 3 con 140; la línea produce 140.",
        ["calcula las tres capacidades", "identifica el cuello de botella", "propone reforzar la operación más lenta", "calcula el nuevo cuello de botella"],
        ["hoja con los cuatro puntos"],
        ["reforzar la operación más rápida", "olvidar el nuevo cuello de botella", "dividir al revés"],
        "Pregunta: «¿qué pasa si ahora aumentas la operación 1?». Debe responder que la línea sigue limitada por la operación 3."),
    reinforce="Con una secuencia inventada de tres operaciones y un turno de 360 minutos, calcula las capacidades y el cuello de botella.",
    extend="Explica con un ejemplo inventado por qué agregar personas a una operación rápida no aumenta la producción.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 24 (análisis de una línea de ejemplo, inventada). Línea de 4 operaciones con una operaria cada una; turno efectivo de 420 minutos; tiempos estándar: operación 1, 2 minutos; operación 2, 3 minutos; operación 3, 4 minutos; operación 4, 6 minutos. "
     "Costo de ejemplo de una operaria: $28.000 por día. Se observa que las prendas se acumulan esperando antes de la operación 4. Pedido: 280 poleras.")
build(
    O6, 3, F,
    use="Aprenderé a analizar un caso de confección en papel: ubicar el cuello de botella, probar alternativas de reparto de personal y comparar el costo por prenda.",
    prior=["Conozco el tiempo estándar y la capacidad.", "Sé dividir con enteros.", "Sé calcular un costo por unidad."],
    explain=[
        "Al analizar una línea se calcula la capacidad de cada operación y se identifica el cuello de botella, que es la operación de menor capacidad. Una señal visible es que las prendas se acumulan esperando antes de esa operación. La producción de la línea es igual a la capacidad del cuello de botella, aunque otras operaciones puedan producir más.",
        "Para mejorar se prueban alternativas, como asignar una segunda operaria a la operación más lenta. Pero al reforzarla, el cuello de botella puede pasar a otra operación, y hay que calcular de nuevo. Cada alternativa tiene un costo: más operarias significan más costo por día, pero también más prendas por día, y el costo por prenda es el costo diario dividido por las prendas del día.",
        "La decisión compara la producción, el costo por prenda y el plazo del pedido, y se registra con los cálculos. Ninguna alternativa justifica saltarse controles de calidad ni medidas de seguridad. Quien decide es la supervisora junto con la jefatura de producción." + LIM,
    ],
    vocab=[("acumulación de prendas", "prendas que esperan antes de una operación lenta"), ("alternativa", "una forma distinta de repartir al personal"), ("costo por prenda", "costo del día dividido por las prendas del día"), ("nuevo cuello de botella", "la operación que pasa a limitar al reforzar la anterior"), ("plazo del pedido", "tiempo disponible para entregarlo")],
    worked=[
        ("Costo por prenda", "Una línea de ejemplo con 3 operarias de $20.000 por día produce 60 prendas al día. ¿Cuál es el costo por prenda?", ["El costo del día es 3 × 20.000 = 60.000.", "60.000 ÷ 60 = 1.000."], "$1.000"),
        ("Nuevo cuello de botella", "Una línea de ejemplo tiene capacidades 100, 50 y 80. Se duplica la operación de 50, que pasa a 100. ¿Cuál es ahora el cuello de botella?", ["Las capacidades son 100, 100 y 80.", "La menor es 80."], "La operación de 80"),
    ],
    mistakes=[("Reforzar la operación equivocada porque es la que más se ve trabajando.", "La mejora debe ir al cuello de botella.", "Calcula las capacidades antes de decidir."),
              ("Comparar alternativas solo por la producción, sin el costo.", "Más personal también cuesta más.", "Calcula el costo por prenda.")],
    T=[
        ("=", "{F} ¿Cuántas prendas por turno puede hacer la operación 1?", "420//2", "Se divide el turno efectivo por el tiempo estándar.", " prendas"),
        ("=", "{F} ¿Cuántas prendas por turno puede hacer la operación 4?", "420//6", "Se divide el turno efectivo por 6 minutos.", " prendas"),
        ("abc", "{F} ¿Cuál es el cuello de botella de la línea actual?", "La operación 4", "La operación 1", "La operación 3", "Tiene la menor capacidad y ahí se acumulan las prendas."),
        ("=", "{F} Después de un turno con la línea actual, ¿cuántas poleras faltan para completar el pedido de 280?", "280-420//6", "Se resta la producción de la línea al pedido.", " poleras"),
        ("abc", "{F} Se agrega una operaria a la operación 1. ¿Qué efecto tiene en la producción de la línea?", "Ninguno, porque el cuello de botella sigue siendo la operación 4", "La duplica", "La reduce", "Una operación que no limita no aumenta la producción."),
        ("=", "{F} Se agrega una segunda operaria a la operación 4. ¿Cuántas poleras produce ahora la línea por turno?", "420//4", "La operación 4 sube a 140, pero la operación 3 queda como cuello de botella con 105.", " poleras"),
        ("abc", "{F} Con esa segunda operaria en la operación 4, ¿cuál es el nuevo cuello de botella?", "La operación 3", "La operación 4", "La operación 1", "Con 105 prendas es ahora la de menor capacidad."),
        ("=", "{F} Se agregan segundas operarias en las operaciones 3 y 4. ¿Cuántas poleras produce entonces la línea por turno?", "420//3", "Las operaciones 3 y 4 suben a 210 y 140; el cuello pasa a ser 140, el de las operaciones 2 y 4.", " poleras"),
        ("=", "{F} ¿Cuál es el costo de mano de obra por polera con la línea original?", "4*28000//(420//6)", "Se divide el costo diario de 4 operarias por las prendas del día.", " pesos"),
        ("=", "{F} ¿Cuál es el costo de mano de obra por polera con las 6 operarias, cuando la línea produce 140 poleras por turno?", "6*28000//(420//3)", "Se divide el costo diario de 6 operarias por las prendas del día.", " pesos"),
        ("abc", "{F} ¿Por qué el costo por polera baja al pasar de 4 a 6 operarias?", "Porque la producción diaria sube más que el costo diario", "Porque las operarias ganan menos", "Porque se acorta el tiempo estándar", "El costo diario sube de 112.000 a 168.000, pero la producción pasa de 70 a 140."),
        ("abc", "{F} Se propone poner 3 operarias en la operación 4 con una sola operaria en la operación 3. ¿Conviene?", "No, porque la operación 3 sigue limitando y no aumenta la producción", "Sí, porque más personas siempre producen más", "Sí, porque la operación 4 es la más lenta", "Mientras la operación 3 tenga 105, esa es la producción de la línea."),
        ("abc", "El jefe pide cumplir el pedido más rápido omitiendo el control de calidad en proceso. ¿Qué corresponde?", "Mantener el control y buscar mejoras en el reparto del personal", "Omitir el control esta vez", "Pedir que controle solo la supervisora al final", "Un control de calidad o de seguridad no se omite para ganar tiempo."),
    ],
    ctx=("abc", "{F} Una operaria dice: «ya me tienen con la operación 4 y se me acumulan prendas, no doy abasto». ¿Qué respuesta es adecuada?", "Revisar las capacidades y evaluar reforzar esa operación, sin apurar a la operaria", "Pedir que trabaje más rápido", "Ignorar el comentario", "Una acumulación indica un cuello de botella; la solución es el reparto, no apurar."),
    sc=[
        ("En Vestuario y Confección Textil: ¿dónde se acumulan las prendas en una línea?", "Antes del cuello de botella", "Esa operación deja pasar menos prendas de las que llegan."),
        ("¿Qué pasa al reforzar el cuello de botella?", "Puede aparecer un nuevo cuello de botella", "Hay que calcular de nuevo las capacidades."),
        ("¿Cómo se calcula el costo por prenda?", "Costo diario dividido por las prendas del día", "Relaciona el costo del día con la producción del día."),
    ],
    op=("Línea de ejemplo de un delantal: operación 1, 3 minutos; operación 2, 5 minutos; operación 3, 4 minutos; una operaria por operación, turno de 420 minutos y $28.000 por operaria al día. "
        "Escribe: (a) la capacidad de cada operación, (b) el cuello de botella, (c) el costo por prenda con la línea actual y (d) cuántas prendas por turno produciría la línea con una segunda operaria en la operación 2 y cuál sería el nuevo cuello de botella.",
        "(a) 140, 84 y 105. (b) La operación 2, con 84. (c) 3 × 28.000 = 84.000 por día; 84.000 ÷ 84 = 1.000 pesos por prenda. (d) La operación 2 pasaría a 168 y el nuevo cuello de botella sería la operación 3 con 105; la línea produciría 105 prendas por turno, más que las 84 actuales, aunque el costo diario subiría a 4 × 28.000 = 112.000.",
        ["calcula las tres capacidades", "identifica el cuello de botella", "calcula el costo diario", "analiza la alternativa con el nuevo cuello"],
        ["hoja con los cuatro puntos"],
        ["reforzar la operación equivocada", "olvidar el nuevo cuello de botella", "no calcular el costo diario"],
        "Pregunta: «¿qué operación sería ahora el cuello de botella?». Debe responder la operación 3."),
    reinforce="Inventa una línea de tres operaciones y encuentra su cuello de botella con un turno de 360 minutos.",
    extend="Explica con un ejemplo inventado por qué reforzar una operación puede cambiar el cuello de botella.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 25 (cronograma de ejemplo, inventado). Pedido: 840 poleras. Línea de 4 operaciones con una operaria cada una; tiempos estándar: 3, 4, 4 y 5 minutos; turno efectivo de 420 minutos; un turno por día. "
     "Eficiencia de la línea: tiempo total de la prenda dividido por (número de operarias por el tiempo de la operación más lenta), por 100. Costo de ejemplo de mano de obra: $50 por minuto de tiempo estándar. "
     "El cliente exige la entrega en 8 días hábiles (días de trabajo normales).")
build(
    O6, 4, F,
    use="Aprenderé a aplicar criterios con datos: calcular la producción diaria, los días de un cronograma, la eficiencia de la línea y el costo de mano de obra de un pedido.",
    prior=["Conozco la capacidad y el cuello de botella.", "Sé dividir y multiplicar con enteros.", "Sé calcular porcentajes."],
    explain=[
        "Un cronograma de producción indica cuántos días se necesitan para cumplir un pedido: se divide el pedido por la producción diaria de la línea, que es la capacidad del cuello de botella, y se redondea hacia arriba. Si el plazo del cliente es menor, hay que mejorar el reparto del personal, ajustar el plazo con el cliente o ambas cosas, pero no se sacrifican controles de calidad ni de seguridad.",
        "La eficiencia de la línea mide qué tan parejo está el trabajo: es el tiempo total de la prenda dividido por el número de operarias multiplicado por el tiempo de la operación más lenta, por 100. Una eficiencia de 100 % significa que todas las operaciones tienen el mismo tiempo y nadie espera. Una eficiencia baja indica desequilibrio en el reparto.",
        "El costo de mano de obra de una prenda es el tiempo total de la prenda por el costo de cada minuto, y el del pedido se obtiene multiplicando por las prendas. Todos los cálculos se guardan para que la jefatura los revise y se informan al cliente con honestidad." + LIM,
    ],
    vocab=[("cronograma de producción", "plan que indica en cuántos días se cumple un pedido"), ("producción diaria", "prendas que produce la línea en un día"), ("eficiencia de la línea", "tiempo total dividido por operarias por tiempo de la operación más lenta, por 100"), ("día hábil", "día de trabajo normal"), ("desequilibrio", "diferencia grande entre las capacidades de las operaciones")],
    worked=[
        ("Días de un pedido", "Un pedido de ejemplo de 500 prendas y una línea que produce 60 por día. ¿Cuántos días necesita?", ["500 ÷ 60 = 8,33.", "Se redondea hacia arriba: 9."], "9 días"),
        ("Eficiencia de una línea", "Una línea de ejemplo con 3 operarias tiene tiempos de 3, 4 y 5 minutos. ¿Cuál es su eficiencia?", ["Tiempo total 12; 3 operarias por 5 minutos son 15.", "12 × 100 ÷ 15 = 80."], "80 %"),
    ],
    mistakes=[("Dividir el pedido por la capacidad de la operación más rápida.", "La producción real la fija el cuello de botella.", "Divide por la capacidad de la operación más lenta."),
              ("Prometer un plazo imposible al cliente para cerrar el trato.", "Si no se cumple, se pierde la confianza.", "Informa un plazo que los cálculos respalden.")],
    T=[
        ("=", "{F} ¿Cuál es el tiempo total de una polera?", "3+4+4+5", "Se suman los tiempos estándar de las operaciones.", " minutos"),
        ("=", "{F} ¿Cuántas prendas puede hacer la operación 1 en un turno?", "420//3", "Se divide el turno efectivo por su tiempo.", " prendas"),
        ("=", "{F} ¿Cuántas prendas puede hacer la operación más lenta en un turno?", "420//5", "Se divide el turno por el tiempo de la operación de 5 minutos.", " prendas"),
        ("=", "{F} ¿Cuántas poleras produce la línea por día?", "420//5", "La línea produce lo que permite su cuello de botella.", " poleras"),
        ("=", "{F} ¿Cuántos días necesita la línea para cumplir el pedido?", "(840+84-1)//84", "Se divide el pedido por la producción diaria, redondeando hacia arriba.", " días"),
        ("abc", "{F} ¿Por qué se usa la producción del cuello de botella para el cronograma?", "Porque ninguna operación puede entregar más prendas de las que deja pasar la más lenta", "Porque es la operación más barata", "Porque es la primera de la secuencia", "La línea entrega lo que permite la operación más lenta."),
        ("=", "{F} ¿Cuál es la eficiencia de la línea (porcentaje)?", "(3+4+4+5)*100//(4*5)", "Se divide el tiempo total por operarias por el tiempo más lento y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es el costo de mano de obra de una polera?", "(3+4+4+5)*50", "Se multiplica el tiempo total de la prenda por el costo por minuto.", " pesos"),
        ("=", "{F} ¿Cuál es el costo de mano de obra de todo el pedido?", "840*(3+4+4+5)*50", "Se multiplica el costo de una polera por las 840 poleras.", " pesos"),
        ("abc", "{F} El cliente exige la entrega en 8 días hábiles. ¿Qué observación es correcta?", "Con la línea actual se necesitan 10 días, por lo que no se alcanza el plazo", "Se alcanza el plazo porque 8 es menor que 10", "Se alcanza el plazo si se omiten los controles", "Con 84 poleras por día, en 8 días se hacen 672."),
        ("=", "{F} En 8 días, ¿cuántas poleras faltarían respecto del pedido con la línea actual?", "840-8*84", "Se resta lo producido en 8 días al total del pedido.", " poleras"),
        ("=", "{F} Se agrega una segunda operaria en la operación más lenta. Ahora las operaciones de 4 minutos son las más lentas. ¿En cuántos días se cumple el pedido?", "840//(420//4)", "La línea pasa a producir 105 por día y 840 entre 105 son 8 días.", " días"),
        ("abc", "{F} El jefe propone cumplir el plazo acortando un control de calidad en proceso. ¿Qué corresponde?", "Cumplirlo con el reparto del personal y mantener los controles", "Acortar el control y avisar después", "Eliminar el control de seguridad", "Los controles no se sacrifican por el plazo."),
    ],
    ctx=("=", "Otro pedido de ejemplo: 600 delantales con una línea que produce 60 por día. ¿En cuántos días se cumple?", "600//60", "Se divide el pedido por la producción diaria.", " días"),
    sc=[
        ("En Vestuario y Confección Textil: ¿cómo se calculan los días de un pedido?", "Dividiendo el pedido por la producción diaria y redondeando hacia arriba", "Hay que cubrir todas las prendas."),
        ("¿Qué mide la eficiencia de la línea?", "Qué tan parejo está el trabajo entre operaciones", "Una eficiencia baja indica desequilibrio entre las operaciones."),
        ("¿Se pueden omitir controles para cumplir un plazo?", "No", "Los controles de calidad y de seguridad no se sacrifican."),
    ],
    op=("Datos de ejemplo: pedido de 1.050 buzos; línea de 3 operarias con tiempos de 3, 5 y 4 minutos; turno efectivo de 420 minutos; $40 por minuto de tiempo estándar; plazo de 12 días hábiles. "
        "Escribe: (a) cuántos buzos produce la línea por día, (b) cuántos días necesita, (c) si cumple el plazo, (d) la eficiencia de la línea y (e) el costo de mano de obra del pedido.",
        "(a) 420 ÷ 5 = 84 por día. (b) 1.050 ÷ 84 = 12,5, es decir 13 días. (c) No cumple: se necesitan 13 días y el plazo es de 12. (d) Tiempo total 12; 3 × 5 = 15; 12 × 100 ÷ 15 = 80 %. (e) 12 × 40 = 480 por buzo; 480 × 1.050 = 504.000 pesos.",
        ["calcula la producción diaria con el cuello de botella", "calcula los días", "compara con el plazo", "calcula el costo de mano de obra"],
        ["hoja con los cinco puntos"],
        ["usar la capacidad de la operación rápida", "decir que cumple el plazo", "omitir el costo de mano de obra"],
        "Pregunta: «¿qué le dirías al cliente?». Debe proponer ajustar el reparto o el plazo, sin omitir controles."),
    reinforce="Calcula los días de un pedido inventado de 400 prendas con una línea que produce 50 por día.",
    extend="Explica con un ejemplo inventado por qué es mejor informar al cliente un plazo respaldado por cálculos.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 26 (sección de terminaciones de ejemplo, inventada). Las terminaciones son las tareas finales de la prenda: revisión, limpieza de hilos sobrantes, colocación de etiquetas, planchado, doblado y empaquetado. "
     "Roles: la encargada de terminaciones organiza el trabajo; el control de calidad revisa antes de empacar; la bodega de producto terminado recibe las cajas. Riesgos: quemaduras por plancha y vapor, esfuerzo repetitivo, manipulación de cajas y permanecer de pie. "
     "Reglas generales: el planchado y el vapor los usa solo personal capacitado y autorizado; la etiqueta debe coincidir con la ficha técnica; las cajas se rotulan; las cargas pesadas se mueven con ayuda; ante un accidente se avisa a un adulto responsable y a emergencias. La norma vigente regula qué datos lleva la etiqueta.")
build(
    O7, 1, F,
    use="Aprenderé a situar la etapa de terminaciones, planchado y empaquetado: qué tareas incluye, qué roles y riesgos hay y qué reglas se aplican; este cuaderno no enseña a planchar.",
    prior=["Conozco la confección y la ficha técnica.", "Sé sumar y multiplicar.", "Sé que las planchas con vapor tienen riesgos."],
    explain=[
        "Las terminaciones son las tareas finales de una prenda: la revisión, la limpieza de hilos sobrantes, la colocación de etiquetas, el planchado, el doblado y el empaquetado. El empaquetado protege la prenda y la deja lista para el despacho, con cada prenda en su bolsa y las bolsas en cajas rotuladas. Todo se hace según la ficha técnica, que también indica qué insumos se usan, como bolsas, etiquetas y cajas.",
        "El planchado y el vapor usan calor y presentan riesgo de quemaduras, por lo que los usa solo personal capacitado y autorizado, y la mantención de los equipos corresponde a personal autorizado. Otros riesgos son el esfuerzo repetitivo, estar de pie por muchas horas y mover cajas pesadas, que se previenen con pausas, ayuda para las cargas y buen orden del puesto.",
        "La etiqueta debe coincidir con la ficha técnica y con lo que exige la norma vigente sobre los datos que lleva, como composición, cuidado y talla. El control de calidad revisa antes de empacar, porque corregir una prenda ya empacada es más costoso. Si ocurre un accidente se avisa a un adulto responsable y a emergencias." + LIMX,
    ],
    vocab=[("terminaciones", "tareas finales de la prenda, como etiquetas, planchado y empaque"), ("empaquetado", "proteger y agrupar las prendas para el despacho"), ("etiqueta", "rótulo cosido o pegado a la prenda con datos como talla, composición y cuidado"), ("producto terminado", "prenda lista para entregar"), ("rotular una caja", "escribir en ella modelo, talla, cantidad y lote")],
    worked=[
        ("Ubicar una tarea", "Una prenda de ejemplo ya fue empacada y alguien descubre una etiqueta equivocada. ¿Qué pudo evitarse?", ["El control debía hacerse antes de empacar.", "Se evitó haber revisado antes de empacar."], "Revisar antes de empacar"),
        ("Aplicar una regla", "Una caja de ejemplo llega a la bodega sin rotular. ¿Qué dice la regla de la ficha?", ["La ficha pide rotular las cajas.", "Debe rotularse antes de recibirla."], "Debe rotularse"),
    ],
    mistakes=[("Empacar sin revisar «porque ya está planchada».", "Un defecto empacado es más costoso de corregir.", "Revisa antes de empacar."),
              ("Mover una caja pesada sin ayuda «para no esperar».", "Hay riesgo de lesión de espalda.", "Pide ayuda o usa un apoyo.")],
    T=[
        ("abc", "En Vestuario y Confección Textil: ¿qué incluyen las terminaciones?", "La colocación de etiquetas, el planchado, el doblado y el empaquetado", "Solo el corte de la tela", "Solo el diseño del figurín", "Las terminaciones son las tareas finales de la prenda."),
        ("abc", "{F} ¿Quién revisa la prenda antes de empacar?", "El control de calidad", "La bodega de producto terminado", "La encargada de terminaciones", "La ficha asigna esa revisión al control de calidad."),
        ("abc", "{F} ¿Con qué debe coincidir la etiqueta?", "Con la ficha técnica", "Con la última etiqueta que se vio", "Con lo que prefiera la operaria", "La regla pide que la etiqueta coincida con la ficha."),
        ("abc", "{F} ¿Quién usa el planchado y el vapor?", "Solo personal capacitado y autorizado", "Cualquier estudiante en práctica", "Quien tenga más prisa", "El calor y el vapor tienen riesgo de quemaduras."),
        ("abc", "{F} ¿Qué riesgo es típico del planchado con vapor?", "Las quemaduras", "El atrapamiento por la cortadora", "El ruido de la bodega", "El calor y el vapor producen quemaduras."),
        ("abc", "En Vestuario y Confección Textil: ¿para qué se rotula una caja?", "Para que se identifique qué contiene sin abrirla", "Para que pese menos", "Para decidir el color de la prenda", "El rótulo con modelo, talla, cantidad y lote identifica el contenido."),
        ("=", "Una sección de terminaciones de ejemplo empaca 18 cajas al día de 24 prendas cada una. ¿Cuántas prendas empaca al día?", "18*24", "Se multiplican las cajas por las prendas de cada caja.", " prendas"),
        ("abc", "{F} Llegan cajas a la bodega sin rotular. ¿Qué corresponde?", "Pedir que se rotulen antes de recibirlas", "Recibirlas y rotular después", "Recibirlas y guardar el contenido a memoria", "La regla de la ficha pide cajas siempre rotuladas."),
        ("abc", "{F} Una operaria quiere mover sola una caja muy pesada. ¿Qué corresponde?", "Pedir ayuda o usar un medio de apoyo", "Levantarla rápido para no esperar", "Arrastrarla sin avisar", "La regla general pide ayuda para las cargas pesadas."),
        ("abc", "Alguien propone empacar de inmediato y revisar la calidad al final del día. ¿Qué observación es correcta?", "Conviene revisar antes de empacar, porque corregir lo empacado cuesta más", "Está bien, porque revisar al final es lo mismo", "Está bien si hay prisa", "Una revisión previa evita desempacar y rehacer."),
        ("abc", "Una plancha deja de calentar de manera pareja. ¿Qué corresponde hacer a la operaria?", "Dejar de usarla y avisar a la jefatura, sin intentar repararla", "Subir el vapor hasta que funcione", "Cambiar la plancha con otra sin avisar", "Una falla en un equipo con calor se informa; la reparación la hace personal autorizado."),
        ("=", "En una bodega de ejemplo hay 200 cajas de 24 poleras y 30 cajas de 12 poleras. ¿Cuántas poleras hay en total?", "200*24+30*12", "Se calculan las poleras de cada tipo de caja y se suman.", " poleras"),
        ("abc", "{F} Una prenda con una etiqueta de talla distinta a la ficha pasa el planchado. ¿Dónde se debería haber detectado?", "En la revisión antes de empacar, comparando la etiqueta con la ficha", "En el despacho al cliente", "En la tienda", "Comparar la etiqueta con la ficha es parte de la revisión previa al empaque."),
    ],
    ctx=("abc", "{F} Una estudiante en práctica ve una caja llena y sin rótulo en el pasillo. ¿Qué corresponde?", "Avisar a la encargada para que se rotule o se guarde en su lugar", "Dejarla donde está", "Rotularla ella con lo que cree que lleva", "La encargada decide; no se adivina el contenido."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué son las terminaciones?", "Las tareas finales de la prenda", "Incluyen etiquetas, planchado, doblado y empaque."),
        ("¿Con qué debe coincidir la etiqueta?", "Con la ficha técnica y con la norma vigente", "Así la prenda queda correctamente identificada."),
        ("¿Quién usa el planchado y el vapor?", "Personal capacitado y autorizado", "El calor y el vapor tienen riesgo de quemaduras."),
    ],
    op=("Una sección de terminaciones de ejemplo debe empacar 600 poleras en cajas de 24 unidades. Escribe: (a) cuántas cajas completas se llenan, (b) qué revisarías antes de empacar, (c) qué datos escribirías en el rótulo de cada caja y (d) una medida de prevención para quien mueve las cajas.",
        "(a) 600 ÷ 24 = 25 cajas. (b) Que la etiqueta coincida con la ficha técnica y que la prenda no tenga defectos. (c) Modelo, talla, cantidad y lote. (d) Pedir ayuda o usar un medio de apoyo para mover las cajas pesadas.",
        ["divide para las cajas", "nombra una revisión previa", "lista los datos del rótulo", "indica una medida de prevención"],
        ["hoja con los cuatro puntos"],
        ["multiplicar en lugar de dividir", "no revisar antes de empacar", "no rotular la caja"],
        "Pregunta: «¿qué pasaría si una caja no tiene rótulo?». Debe responder que no se sabe qué contiene y se pueden mezclar tallas."),
    reinforce="Escribe en una tabla cinco tareas de terminaciones y el riesgo principal de cada una.",
    extend="Explica con un ejemplo inventado por qué se revisa la prenda antes de empacarla.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 27 (etiquetado y empaque de ejemplo, inventado). Etiqueta de composición: 60 % algodón y 40 % poliéster (los porcentajes de fibras suman 100 %). Etiqueta de cuidado de ejemplo, en texto: lavar a máquina con agua fría; no usar cloro; planchar a baja temperatura; no usar secadora. Etiqueta de talla: M. "
     "Embalaje: cada polera va en una bolsa; las bolsas van en cajas de cartón de 24 unidades de una misma talla; la caja se rotula con modelo, talla, cantidad y lote. Lote: conjunto de prendas hechas en las mismas condiciones. Lista de empaque: documento que indica qué lleva cada caja. Los valores son de ejemplo y no reemplazan la norma vigente de etiquetado.")
build(
    O7, 2, F,
    use="Aprenderé los documentos y términos del etiquetado y el empaque (composición, cuidado, talla, lote y lista de empaque) y qué rol responde por cada uno.",
    prior=["Conozco las terminaciones y su riesgo.", "Sé sumar y multiplicar.", "Sé calcular porcentajes sencillos."],
    explain=[
        "La etiqueta de composición indica de qué fibras está hecha la prenda, con sus porcentajes; esos porcentajes deben sumar 100 %. La etiqueta de cuidado indica cómo lavar, planchar y secar la prenda, escrita en palabras o con símbolos estandarizados. La etiqueta de talla indica el tamaño. Los datos exactos que se exigen los fija la norma vigente, y la etiqueta debe coincidir con la ficha técnica.",
        "El embalaje protege las prendas: cada una va en una bolsa, y las bolsas van en cajas de cartón con una cantidad fija de prendas de una misma talla. La caja se rotula con modelo, talla, cantidad y lote. El lote es el conjunto de prendas hechas en las mismas condiciones, y permite rastrear un problema hasta su origen. La lista de empaque indica qué lleva cada caja y sirve para comprobar el despacho.",
        "Cada documento tiene un responsable: la diseñadora define la etiqueta en la ficha, la encargada de terminaciones la aplica, el control de calidad la verifica y la bodega recibe las cajas. Si hay diferencias entre la etiqueta, la ficha y la caja, no se despacha hasta aclararlas." + LIM,
    ],
    vocab=[("etiqueta de composición", "etiqueta que indica las fibras de la prenda y sus porcentajes"), ("etiqueta de cuidado", "etiqueta que indica cómo lavar, planchar y secar"), ("lote", "conjunto de prendas hechas en las mismas condiciones"), ("lista de empaque", "documento que indica qué lleva cada caja"), ("rastrear", "seguir un producto hasta su origen")],
    worked=[
        ("Revisar los porcentajes", "Una etiqueta de ejemplo dice 70 % algodón y 25 % poliéster. ¿Suman 100 %?", ["70 + 25 = 95.", "Faltan 5 puntos."], "No suman 100 %"),
        ("Usar la lista de empaque", "Una lista de ejemplo dice que una caja lleva 12 prendas de talla S. Al abrirla hay 12 de talla M. ¿Qué corresponde?", ["El contenido no coincide con el rótulo.", "No se despacha hasta aclararlo."], "No despachar y aclarar"),
    ],
    mistakes=[("Escribir porcentajes de composición que no suman 100 %.", "La etiqueta pierde sentido y puede incumplir la norma.", "Verifica que sumen 100 %."),
              ("Mezclar tallas en una caja rotulada con una sola talla.", "El cliente recibe prendas distintas a lo anunciado.", "Una caja, una talla.")],
    T=[
        ("abc", "{F} ¿Qué indica la etiqueta de composición?", "De qué fibras está hecha la prenda y en qué porcentajes", "Cómo lavar la prenda", "La talla de la prenda", "La composición lista las fibras; el cuidado indica cómo lavar."),
        ("abc", "{F} ¿Qué indica la etiqueta de cuidado?", "Cómo lavar, planchar y secar la prenda", "De qué fibras está hecha la prenda", "En qué caja va la prenda", "El cuidado indica cómo mantener la prenda."),
        ("=", "{F} Si la composición tiene 60 % algodón, ¿qué porcentaje debe tener el resto, que es poliéster?", "100-60", "Los porcentajes de todas las fibras suman 100 %.", " %"),
        ("abc", "En Vestuario y Confección Textil: ¿qué es un lote?", "Un conjunto de prendas hechas en las mismas condiciones", "Una caja de cartón", "Una etiqueta de talla", "El lote permite rastrear un problema hasta su origen."),
        ("abc", "{F} ¿Qué datos se escriben en el rótulo de la caja?", "Modelo, talla, cantidad y lote", "Solo el nombre del cliente", "Solo el color de la prenda", "La ficha lista modelo, talla, cantidad y lote."),
        ("abc", "{F} ¿Qué documento indica qué lleva cada caja?", "La lista de empaque", "La etiqueta de composición", "La orden de corte", "La lista de empaque se usa para comprobar el despacho."),
        ("=", "{F} Una orden de ejemplo pide 480 poleras talla M. ¿Cuántas cajas se llenan?", "480//24", "Se divide el total de prendas por las que lleva cada caja.", " cajas"),
        ("abc", "{F} Una etiqueta de ejemplo dice 55 % algodón y 35 % poliéster. ¿Qué problema tiene?", "Los porcentajes suman 90 % y no 100 %", "Está bien, porque suma más de 50 %", "Está bien, porque tiene algodón", "Los porcentajes de las fibras deben sumar 100 %."),
        ("abc", "{F} Al abrir una caja rotulada con talla M se encuentran poleras talla S. ¿Qué corresponde?", "No despachar hasta aclarar el error y corregir el rótulo o el contenido", "Despachar igual, porque son poleras", "Cambiar el rótulo y despachar sin informar", "El contenido debe coincidir con el rótulo y con la lista de empaque."),
        ("abc", "¿Quién define qué etiqueta lleva una prenda en la ficha técnica?", "La diseñadora, según la ficha y la norma vigente", "La bodega de producto terminado", "El cliente final", "La etiqueta se define en la ficha técnica, cuya responsable es la diseñadora."),
        ("abc", "Un cliente reclama por una prenda y el taller quiere saber de qué día salió. ¿Qué dato de la caja ayuda a rastrearla?", "El lote", "El color de la caja", "La cantidad de prendas de la caja", "El lote identifica las condiciones en que se hizo la prenda."),
        ("=", "Una lista de empaque de ejemplo anota 14 cajas de 24 poleras y 1 caja de 18 poleras. ¿Cuántas poleras hay en total?", "14*24+18", "Se calculan las poleras de las cajas completas y se suma la caja parcial.", " poleras"),
        ("abc", "El taller decide cambiar a una caja de 30 unidades. ¿Qué documentos deben actualizarse?", "La ficha y la lista de empaque, con una nueva versión", "Solo el color de la caja", "Ninguno", "Si cambia el embalaje, debe actualizarse la ficha para que todos lo sepan."),
    ],
    ctx=("=", "{F} Para un pedido de 360 poleras, el taller usa cajas de 24 unidades. ¿Cuántas cajas se llenan?", "360//24", "Se divide el total de poleras por las que lleva cada caja.", " cajas"),
    sc=[
        ("En Vestuario y Confección Textil: ¿a cuánto deben sumar los porcentajes de la etiqueta de composición?", "100 %", "Son las partes de la prenda completa."),
        ("¿Qué es la lista de empaque?", "El documento que indica qué lleva cada caja", "Sirve para comprobar el despacho contra el pedido."),
        ("¿Qué se hace si el contenido de una caja no coincide con el rótulo?", "No se despacha hasta aclararlo", "Evita entregar prendas distintas a las anunciadas."),
    ],
    op=("Etiqueta de ejemplo de un pantalón: «50 % algodón, 40 % poliéster, 15 % viscosa». Pedido: 360 pantalones talla L en cajas de 12 unidades. Escribe: (a) si la etiqueta es correcta y qué falta, (b) cuántas cajas se llenan, (c) qué escribirías en el rótulo de cada caja y (d) qué harías si una caja trae pantalones de otra talla.",
        "(a) Los porcentajes suman 105 %; se pasan 5 puntos de 100 %, por lo que hay que corregir la etiqueta. (b) 360 ÷ 12 = 30 cajas. (c) Modelo, talla L, cantidad 12 y lote. (d) No despachar hasta aclarar y corregir el contenido o el rótulo.",
        ["suma los porcentajes", "divide para las cajas", "lista los datos del rótulo", "propone no despachar"],
        ["hoja con los cuatro puntos"],
        ["dar por buena la etiqueta", "multiplicar en lugar de dividir", "despachar con error"],
        "Pregunta: «¿en cuánto se pasa la suma de 100 %?». Debe responder que en 5 puntos."),
    reinforce="Inventa una etiqueta de composición de tres fibras que sume 100 % y una lista de empaque de dos cajas.",
    extend="Explica con un ejemplo inventado por qué el lote ayuda a atender un reclamo.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 28 (revisión previa al despacho de ejemplo, inventada). Ficha técnica del modelo BL-3, lote 12: composición 60 % algodón y 40 % poliéster; talla M; cajas de 24 unidades de una sola talla, rotuladas con modelo, talla, cantidad y lote. "
     "Resultados de la revisión, numerados del 1 al 5 (solo las diferencias con la ficha son hallazgos): (1) las etiquetas del lote dicen 65 % algodón y 40 % poliéster; (2) las etiquetas de cuidado coinciden con la ficha; (3) 3 cajas están rotuladas sin el lote; (4) la caja 5 tiene 22 poleras en lugar de 24; (5) una caja tiene 24 poleras, pero 2 son talla L. "
     "Cantidad total de cajas del lote: 10.")
build(
    O7, 3, F,
    use="Aprenderé a analizar un caso en papel: comparar etiquetas y cajas con la ficha, clasificar los hallazgos y decidir si el lote se despacha.",
    prior=["Conozco la etiqueta de composición y el rótulo de la caja.", "Sé sumar porcentajes.", "Sé restar cantidades."],
    explain=[
        "La revisión previa al despacho compara lo que hay con lo que dice la ficha técnica. Se revisan tres cosas: las etiquetas de cada prenda, el contenido de las cajas y los rótulos. Cada diferencia es un hallazgo. Un hallazgo se clasifica según su efecto: si afecta lo que el cliente recibe o lo que exige la norma, es importante; si solo falta un dato de orden interno, es menor, pero igual se corrige.",
        "Un lote se despacha solo si no tiene hallazgos importantes sin resolver. Para resolverlos se corrige el error, se vuelve a revisar y se registra. Las etiquetas con porcentajes que no suman 100 % o con una talla distinta a la caja se corrigen antes de despachar. Un rótulo sin lote impide rastrear un problema y también se completa.",
        "El registro de la revisión anota los hallazgos, la decisión, las acciones y quién las hizo. No se oculta ni se modifica un hallazgo para despachar más rápido. Si hay dudas, decide la jefatura de calidad." + LIM,
    ],
    vocab=[("hallazgo", "diferencia encontrada al comparar con la ficha"), ("hallazgo importante", "diferencia que afecta lo que recibe el cliente o lo que exige la norma"), ("corregir y revisar de nuevo", "arreglar el error y comprobar que quedó bien"), ("registro de la revisión", "anotación de hallazgos, decisión y responsables"), ("jefatura de calidad", "persona que decide ante las dudas de calidad")],
    worked=[
        ("Clasificar un hallazgo", "En una revisión de ejemplo, una etiqueta de talla dice L en una caja de talla M. ¿Es un hallazgo importante?", ["Afecta lo que recibe el cliente.", "Sí, es importante."], "Sí, importante"),
        ("Decidir con los hallazgos", "Un lote de ejemplo tiene un hallazgo importante sin resolver. ¿Se despacha?", ["Solo se despacha sin hallazgos importantes pendientes.", "No se despacha."], "No se despacha"),
    ],
    mistakes=[("Despachar el lote «y corregir después» porque el cliente lo necesita.", "Se entrega algo distinto a lo anunciado.", "Corrige y revisa antes de despachar."),
              ("Cambiar el registro de la revisión para que no figure un hallazgo.", "Oculta un problema y es una falta de ética.", "Registra todo lo encontrado.")],
    T=[
        ("abc", "{F} ¿Qué problema tiene la etiqueta del hallazgo 1?", "Los porcentajes suman 105 % y no coinciden con la ficha", "Falta la talla", "Dice poliéster en lugar de algodón", "65 más 40 es 105, y la ficha pide 60 y 40."),
        ("=", "{F} ¿Cuántas poleras faltan en la caja 5?", "24-22", "Se resta lo que tiene la caja a lo que debería tener.", " poleras"),
        ("abc", "{F} ¿Cuál de los cinco resultados indica que algo coincide con la ficha y no requiere corrección?", "El resultado 2, el de las etiquetas de cuidado", "El resultado 1, el de composición", "El resultado 5, el de la talla L", "El resultado 2 indica que las etiquetas de cuidado coinciden, así que no es una diferencia."),
        ("abc", "{F} ¿Por qué es importante el hallazgo de las 2 poleras talla L en una caja de talla M?", "Porque el cliente recibiría prendas distintas de lo anunciado", "Porque la caja pesa más", "Porque la talla L es más cara", "El rótulo no coincide con el contenido."),
        ("=", "{F} ¿Cuántas cajas del lote no tienen hallazgos en el rótulo, sabiendo que 3 están rotuladas sin lote?", "10-3", "Se restan las cajas con hallazgo de rótulo del total.", " cajas"),
        ("abc", "{F} ¿Se puede despachar el lote tal como está?", "No, porque tiene hallazgos importantes sin resolver", "Sí, porque la mayoría de las cajas está bien", "Sí, porque el cliente espera el lote", "Hay etiquetas con porcentajes incorrectos y una caja con tallas mezcladas."),
        ("abc", "{F} ¿Por qué se completa el lote en los rótulos de las 3 cajas?", "Para poder rastrear un problema hasta su origen", "Para que el cartón pese más", "Para cambiar el color de la caja", "El lote permite rastrear un problema."),
        ("=", "{F} Si se corrige la etiqueta del hallazgo 1 sin cambiar el 40 % de poliéster, ¿qué porcentaje de algodón debe decir?", "100-40", "Los porcentajes de las fibras deben sumar 100 %.", " %"),
        ("=", "{F} A la caja 5 se le agregan 2 poleras. ¿Cuántas poleras tiene entonces?", "22+2", "Se suman las poleras que se agregan a las que ya tenía.", " poleras"),
        ("abc", "El jefe de producción dice: «despachemos hoy y corregimos las etiquetas la próxima semana». ¿Qué corresponde?", "Corregir y revisar de nuevo antes de despachar", "Despachar hoy", "Despachar solo las cajas bien rotuladas sin avisar", "Los hallazgos importantes se resuelven antes de entregar."),
        ("abc", "Un revisor propone borrar del registro el hallazgo de la caja 5 «porque es solo una caja». ¿Qué observación es correcta?", "No se debe borrar: el registro debe reflejar todo lo encontrado", "Se puede borrar si es solo una", "Se puede borrar si el cliente no se entera", "Ocultar un hallazgo es una falta de ética y de calidad."),
        ("=", "{F} De los 5 resultados del informe, uno indica que algo coincide con la ficha. ¿Cuántos hallazgos requieren corrección?", "5-1", "Se restan los hallazgos que coinciden con la ficha al total.", " hallazgos"),
        ("abc", "Tras corregir, el revisor vuelve a revisar el lote. ¿Qué debe anotar?", "Los hallazgos corregidos, la nueva revisión, la decisión y quién la hizo", "Solo la fecha", "Solo que está todo bien", "El registro debe permitir que otra persona reconstruya la decisión."),
    ],
    ctx=("abc", "{F} El cliente llama para pedir que se despache el lote hoy aunque falten correcciones. ¿Qué responde un taller que cuida la calidad?", "Informar los hallazgos y el nuevo plazo, sin despachar con errores", "Despachar para no perder al cliente", "Despachar solo con las cajas buenas sin avisar", "Se entrega lo prometido o se informa con honestidad lo pendiente."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué es un hallazgo?", "Una diferencia encontrada al comparar con la ficha", "Se registra para poder corregirla después."),
        ("¿Cuándo se despacha un lote?", "Cuando no tiene hallazgos importantes sin resolver", "Así el cliente recibe lo prometido."),
        ("¿Se puede cambiar un registro para ocultar un hallazgo?", "No", "El registro debe reflejar lo encontrado."),
    ],
    op=("Revisión de ejemplo del lote 7 (24 prendas por caja, talla L): hallazgos: etiquetas de composición con 45 % algodón y 45 % poliéster; una caja con 23 prendas; dos cajas con rótulo sin talla. Pedido: 8 cajas. "
        "Escribe: (a) qué hallazgos son importantes y por qué, (b) cuántas prendas faltan, (c) si despachas y por qué y (d) qué anotarías en el registro.",
        "(a) La etiqueta, porque los porcentajes suman 90 % y no 100 %; la caja de 23 prendas, porque el cliente recibiría menos de lo anunciado; los rótulos sin talla, porque impiden identificar el contenido. (b) Falta 1 prenda. (c) No se despacha hasta corregir las etiquetas, completar la caja y rotular las cajas. (d) Los tres hallazgos, la decisión, las acciones, quién las hizo y la fecha.",
        ["identifica la suma de 90 %", "calcula la prenda que falta", "decide no despachar", "propone un registro"],
        ["hoja con los cuatro puntos"],
        ["despachar con hallazgos", "no revisar la suma de porcentajes", "no registrar la decisión"],
        "Pregunta: «¿qué falta para llegar a 100 %?». Debe responder 10 puntos."),
    reinforce="Inventa una revisión con tres hallazgos de un lote y decide si se despacha.",
    extend="Explica con un ejemplo inventado por qué ocultar un hallazgo daña la confianza del cliente.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 29 (pedido de empaque de ejemplo, inventado). Pedido de poleras: talla S, 48 unidades; talla M, 120 unidades; talla L, 72 unidades. Cajas de 24 unidades de una misma talla. "
     "Peso de ejemplo de una polera con su bolsa: 180 g (gramos). Peso de una caja de cartón vacía: 600 g. Una persona puede mover sola una caja de hasta 8.000 g (valor de ejemplo, no reemplaza la norma vigente sobre manipulación de cargas). "
     "Fibras de una polera de ejemplo, por peso: 90 g de algodón y 60 g de poliéster.")
build(
    O7, 4, F,
    use="Aprenderé a aplicar criterios con datos: calcular cajas, pesos y composición de fibras para el empaque y el etiquetado.",
    prior=["Conozco el rótulo de la caja y la lista de empaque.", "Sé multiplicar y dividir con enteros.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Para empacar un pedido se calcula, por cada talla, las cajas necesarias dividiendo las prendas por las que lleva cada caja. Como cada caja lleva una sola talla, no se mezclan las tallas para completar una caja; si queda una caja parcial, se rotula con su cantidad real. El total de cajas es la suma de las cajas de cada talla.",
        "El peso de una caja es el peso de las prendas más el peso de la caja vacía. Se compara con el máximo que una persona puede mover sola; si lo supera, se pide ayuda o se usa un apoyo. La composición de una prenda se calcula con los pesos de sus fibras: el porcentaje de cada fibra es su peso dividido por el peso total de las fibras, por 100.",
        "Los resultados se anotan en la lista de empaque y la etiqueta debe coincidir con ellos. Si el cálculo no coincide con la ficha técnica, se avisa antes de continuar. Los valores usados son de ejemplo; los reales los fijan la ficha y la norma vigente." + LIM,
    ],
    vocab=[("caja parcial", "caja con menos prendas que el máximo"), ("peso de la caja", "peso de las prendas más el de la caja vacía"), ("gramo", "unidad de peso (g)"), ("porcentaje de una fibra", "peso de la fibra dividido por el peso total de las fibras, por 100"), ("lista de empaque", "documento que indica qué lleva cada caja")],
    worked=[
        ("Cajas de una talla", "Un pedido de ejemplo de 60 unidades de talla XL y cajas de 24. ¿Cuántas cajas se necesitan?", ["60 ÷ 24 = 2,5.", "Se redondea hacia arriba: 3, con una caja parcial."], "3 cajas"),
        ("Composición por peso", "Una prenda de ejemplo tiene 150 g de una fibra y 50 g de otra. ¿Qué porcentaje es la primera?", ["El total es 200 g.", "150 × 100 ÷ 200 = 75."], "75 %"),
    ],
    mistakes=[("Completar una caja con prendas de otra talla para que quede llena.", "El cliente recibe tallas mezcladas.", "Rotula una caja parcial con la cantidad real."),
              ("Olvidar el peso de la caja vacía al calcular lo que pesa.", "El peso total resulta menor del real.", "Suma el peso de las prendas y el de la caja.")],
    T=[
        ("=", "{F} ¿Cuántas cajas se llenan con las poleras talla M?", "120//24", "Se divide la cantidad de la talla por las prendas de cada caja.", " cajas"),
        ("=", "{F} ¿Cuántas cajas se llenan con las poleras talla S?", "48//24", "Se divide la cantidad por las 24 prendas de cada caja.", " cajas"),
        ("=", "{F} ¿Cuántas cajas se llenan con las poleras talla L?", "72//24", "Se divide la cantidad por las 24 prendas de cada caja.", " cajas"),
        ("=", "{F} ¿Cuántas cajas hay en total en el pedido?", "48//24+120//24+72//24", "Se suman las cajas de cada talla.", " cajas"),
        ("=", "{F} ¿Cuánto pesan las prendas de una caja completa, en gramos?", "24*180", "Se multiplican las prendas por el peso de cada una.", " g"),
        ("=", "{F} ¿Cuánto pesa una caja completa con su cartón, en gramos?", "24*180+600", "Al peso de las prendas se suma el peso de la caja vacía.", " g"),
        ("abc", "{F} ¿Puede una persona mover sola una caja completa según el valor de ejemplo?", "Sí, porque 4.920 g es menor que el máximo de 8.000 g", "No, porque 4.920 g supera el máximo", "No, porque la caja tiene 24 prendas", "El peso de la caja es 4.920 g, menor que 8.000 g."),
        ("=", "{F} ¿Qué porcentaje de la polera es de algodón?", "90*100//(90+60)", "Se divide el peso del algodón por el peso total de fibras y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de la polera es de poliéster?", "60*100//(90+60)", "Se divide el peso del poliéster por el total de fibras y se multiplica por 100.", " %"),
        ("abc", "{F} Los porcentajes de la polera, ¿cómo deben anotarse en la etiqueta?", "60 % algodón y 40 % poliéster, que suman 100 %", "60 % algodón y 60 % poliéster", "50 % algodón y 40 % poliéster", "Las fibras se anotan con sus porcentajes calculados, que suman 100 %."),
        ("=", "El pedido de otra talla XL es de 50 poleras y las cajas son de 24. ¿Cuántas poleras llevará la caja parcial?", "50-2*24", "Se resta lo que ocupan las cajas completas al total.", " poleras"),
        ("abc", "Para completar una caja parcial de talla XL, un compañero propone agregar 5 poleras de talla L. ¿Qué observación es correcta?", "No corresponde, porque cada caja lleva una sola talla; se rotula la cantidad real", "Corresponde, para que quede llena", "Corresponde si el cliente no lo nota", "El cliente espera una talla por caja y la lista de empaque debe coincidir."),
        ("abc", "El peso de la caja de cartón cambia por un cartón más resistente de 900 g. ¿Qué debe hacerse?", "Recalcular el peso total y comparar de nuevo con el máximo de ejemplo", "Mantener el cálculo anterior", "Quitar el cartón al calcular", "Un cambio de insumo cambia el peso total."),
    ],
    ctx=("=", "{F} Una caja parcial de talla XL lleva 14 poleras. ¿Cuánto pesa con su cartón, en gramos?", "14*180+600", "Se multiplican las prendas por su peso y se suma el cartón.", " g"),
    sc=[
        ("En Vestuario y Confección Textil: ¿cómo se calculan las cajas de una talla?", "Dividiendo las prendas por las que lleva cada caja, redondeando hacia arriba", "Si sobran prendas hay una caja parcial."),
        ("¿Se mezclan tallas para completar una caja?", "No", "Cada caja lleva una sola talla."),
        ("¿Cómo se calcula el porcentaje de una fibra?", "Peso de la fibra dividido por el peso total de fibras, por 100", "Así los porcentajes suman 100 %."),
    ],
    op=("Pedido de ejemplo de pantalones: talla 38, 36 unidades; talla 40, 60 unidades; cajas de 12 unidades; cada pantalón con su bolsa pesa 400 g; la caja vacía pesa 700 g. "
        "Escribe: (a) cuántas cajas se llenan de cada talla, (b) cuánto pesa una caja completa y (c) si una persona puede moverla sola si el máximo de ejemplo es 8.000 g.",
        "(a) Talla 38: 3 cajas. Talla 40: 5 cajas. (b) 12 × 400 + 700 = 5.500 g. (c) Sí, porque 5.500 g es menor que 8.000 g.",
        ["calcula las cajas de cada talla", "suma el cartón al peso", "compara con el máximo"],
        ["hoja con los tres puntos"],
        ["mezclar tallas", "olvidar el peso de la caja", "decir que no puede moverla sin comparar"],
        "Pregunta: «¿qué pasaría si el pedido fuera de 40 pantalones talla 40?». Debe responder que habría 3 cajas completas y una parcial de 4."),
    reinforce="Con un pedido inventado de tres tallas y cajas de 20 unidades, calcula las cajas de cada talla.",
    extend="Explica con un ejemplo inventado por qué no se mezclan tallas en una caja.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 30 (control de calidad de un taller de ejemplo, inventado). El control de calidad comprueba que los productos cumplan la ficha técnica y el formato estándar de la empresa. Se hace en tres momentos: al recibir las telas e insumos, durante la confección (en proceso) y al terminar la prenda (final). "
     "Documentos: la ficha técnica con sus medidas, la prenda de muestra aprobada (referencia con la que se comparan las demás) y la hoja de inspección (registro de lo revisado). Roles: la inspectora de calidad revisa y registra; la supervisora corrige el proceso; la jefatura decide. "
     "Reglas generales: se registra siempre lo encontrado, aunque sea desfavorable; no se alteran datos ni se presiona a la inspectora para aprobar; la iluminación del puesto de revisión debe ser adecuada y se hacen pausas visuales; ante un accidente se avisa a un adulto responsable y a emergencias.")
build(
    O8, 1, F,
    use="Aprenderé a situar el control de calidad en un taller: sus momentos, documentos, roles, riesgos y reglas de ética.",
    prior=["Conozco la ficha técnica y las medidas.", "Sé comparar un dato con otro.", "Sé qué es una tolerancia."],
    explain=[
        "En Vestuario y Confección Textil, el control de calidad comprueba que los productos cumplan la ficha técnica y el formato estándar de la empresa. Se hace en tres momentos: al recibir telas e insumos, durante la confección y al terminar la prenda. Así los problemas se detectan en el momento más temprano posible, cuando corregirlos cuesta menos.",
        "Los documentos del control son la ficha técnica, la prenda de muestra aprobada, que es la referencia con la que se comparan las demás, y la hoja de inspección, que registra lo revisado. La inspectora de calidad revisa y registra, la supervisora corrige el proceso y la jefatura decide qué hacer con lo que no cumple. El registro debe ser honesto y completo.",
        "La ética del control exige no alterar datos ni presionar para aprobar. Las condiciones de trabajo importan: buena iluminación para revisar, pausas visuales y una mesa a la altura adecuada. Las herramientas de corte, como las tijeras de hilos, se manejan solo por personal capacitado. Ante un accidente se avisa a un adulto responsable y a emergencias." + LIMX,
    ],
    vocab=[("control de calidad", "comprobación de que el producto cumple la ficha técnica y el formato estándar"), ("prenda de muestra aprobada", "prenda de referencia con la que se comparan las demás"), ("hoja de inspección", "registro de lo que se revisó"), ("inspectora de calidad", "persona que revisa y registra"), ("formato estándar", "forma de presentar el producto que fija la empresa")],
    worked=[
        ("Ubicar el momento del control", "Al llegar un rollo de tela se revisa si tiene manchas. ¿En qué momento del control está?", ["Es antes de la confección.", "Es el control de recepción de telas e insumos."], "Control al recibir telas e insumos"),
        ("Aplicar una regla ética", "Un jefe pide a la inspectora anotar «aprobado» aunque encontró un defecto. ¿Qué corresponde?", ["La regla pide registrar siempre lo encontrado.", "No debe anotar aprobado."], "Registrar el defecto"),
    ],
    mistakes=[("Controlar solo al final «porque ahí se ve todo».", "Los defectos se descubren tarde y se repiten.", "Controla también al recibir y en proceso."),
              ("Aprobar una prenda porque el cliente la necesita ya.", "Se entrega algo que no cumple la ficha.", "Registra el defecto y decide según los criterios.")],
    T=[
        ("abc", "En Vestuario y Confección Textil: ¿qué comprueba el control de calidad?", "Que el producto cumpla la ficha técnica y el formato estándar", "Que la tela sea la más barata", "Que la prenda sea de moda", "El control compara el producto con lo especificado."),
        ("abc", "{F} ¿Cuáles son los tres momentos del control?", "Al recibir telas e insumos, en proceso y al terminar la prenda", "Solo al final", "Solo en el despacho", "La ficha lista tres momentos para detectar problemas temprano."),
        ("abc", "{F} ¿Qué es la prenda de muestra aprobada?", "La prenda de referencia con la que se comparan las demás", "La prenda más cara", "La primera que se cosió", "La muestra aprobada es la referencia del control."),
        ("abc", "{F} ¿Qué es la hoja de inspección?", "El registro de lo que se revisó", "El manual de la máquina", "La orden de corte", "La hoja de inspección documenta el control."),
        ("abc", "{F} ¿Qué rol revisa y registra?", "La inspectora de calidad", "La supervisora", "La jefatura", "La ficha asigna esa tarea a la inspectora."),
        ("abc", "En Vestuario y Confección Textil: ¿por qué conviene controlar al recibir las telas?", "Porque un defecto de la tela se detecta antes de gastar trabajo en ella", "Porque así se paga menos al proveedor", "Porque no es necesario controlar después", "Detectar temprano evita perder confección en material defectuoso."),
        ("=", "Un taller de ejemplo revisa 5 rollos al recibirlos y encuentra defectos en 1. ¿Cuántos rollos no tienen defectos?", "5-1", "Se restan los rollos con defecto del total revisado.", " rollos"),
        ("abc", "{F} Un jefe pide anotar «aprobado» aunque se encontró un defecto. ¿Qué corresponde?", "Registrar el defecto y no anotar aprobado", "Anotar aprobado para no atrasar", "Anotar aprobado y corregir después", "La regla pide registrar siempre lo encontrado."),
        ("abc", "{F} La inspectora tiene poca luz en su mesa y se le cansa la vista. ¿Qué medida corresponde?", "Pedir mejorar la iluminación y hacer pausas visuales", "Revisar más rápido", "Revisar con menos cuidado", "La iluminación adecuada y las pausas previenen la fatiga visual."),
        ("abc", "Una inspectora siente presión de la supervisora para aprobar un lote con un defecto. ¿Qué corresponde?", "Registrar lo encontrado y avisar a la jefatura de la presión", "Aprobar para evitar conflictos", "Cambiar la fecha de la hoja de inspección", "El registro honesto debe mantenerse aunque haya presión."),
        ("abc", "El control de calidad rechaza una polera. ¿En qué documento se apoya?", "En la ficha técnica y la prenda de muestra aprobada", "En una impresión personal", "En lo que opine el cliente final", "El rechazo se justifica con documentos de referencia."),
        ("=", "Un control en proceso revisa 10 prendas cada hora durante 6 horas. ¿Cuántas prendas se revisan en total?", "10*6", "Se multiplican las prendas por hora por las horas.", " prendas"),
        ("abc", "Una inspectora se hace un corte pequeño con unas tijeras de hilos. ¿Qué corresponde?", "Avisar de inmediato a un adulto responsable y a emergencias", "Seguir trabajando sin avisar", "Esconder el corte para no perder el turno", "Todo accidente se informa a un adulto responsable."),
    ],
    ctx=("abc", "{F} El taller recibe un rollo con una mancha visible. ¿Qué corresponde registrar en la hoja de inspección?", "La mancha, su ubicación y la decisión de la jefatura", "Que el rollo está bien", "Nada, porque aún no es una prenda", "El control en recepción registra lo encontrado."),
    sc=[
        ("En Vestuario y Confección Textil: ¿cuáles son los momentos del control de calidad?", "Al recibir, en proceso y al terminar", "Así se detectan los problemas temprano."),
        ("¿Qué se hace con un defecto que se encuentra?", "Se registra", "No se oculta ni se altera."),
        ("¿Para qué sirve la prenda de muestra aprobada?", "Para comparar las demás prendas", "Es la referencia que se usa en el control."),
    ],
    op=("Situación de ejemplo: una inspectora revisa poleras y encuentra en una de ellas un botón suelto en una prenda infantil, en otra una costura abierta y en otra un hilo suelto. La supervisora le dice que apruebe el lote porque «el cliente espera». "
        "Escribe: (a) qué hallazgos registrarías, (b) qué le responderías a la supervisora, (c) en qué documentos te apoyas y (d) una medida para cuidar la vista de la inspectora.",
        "(a) Un botón suelto, una costura abierta y un hilo suelto, con la prenda y la fecha. (b) Que se debe registrar lo encontrado y que la decisión final la toma la jefatura. (c) En la ficha técnica y en la prenda de muestra aprobada. (d) Buena iluminación y pausas visuales.",
        ["registra los tres hallazgos", "se niega a aprobar por presión", "nombra los documentos de referencia", "propone una medida de salud"],
        ["hoja con los cuatro puntos"],
        ["aprobar por presión", "no mencionar el botón suelto", "no registrar nada"],
        "Pregunta: «¿quién decide qué hacer con el lote?». Debe responder la jefatura."),
    reinforce="Escribe los tres momentos del control de calidad y un ejemplo de defecto que se detectaría en cada uno.",
    extend="Explica con un ejemplo inventado por qué una inspectora no debe aprobar por presión.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 31 (criterios de calidad de ejemplo, inventados; los reales los fijan la ficha técnica, el cliente y la norma vigente). Clasificación de defectos: crítico, el que puede dañar a quien usa la prenda o incumple una norma (por ejemplo, un botón suelto en una prenda infantil); "
     "mayor, el que afecta el uso o se ve de forma notoria (por ejemplo, una costura abierta o una mancha grande); menor, el que casi no afecta (por ejemplo, un hilo suelto pequeño). Muestreo: se revisa una parte del lote, la muestra, para juzgar el lote completo. "
     "Criterio de aceptación de ejemplo para una muestra de 50 prendas: 0 defectos críticos, hasta 3 mayores y hasta 6 menores. No conformidad: incumplimiento de un requisito de la ficha. Acción correctiva: lo que se hace para corregir la causa y que no se repita.")
build(
    O8, 2, F,
    use="Aprenderé los conceptos del control de calidad (tipos de defecto, muestreo, criterio de aceptación, no conformidad y acción correctiva) y a clasificar defectos.",
    prior=["Conozco los momentos del control.", "Sé comparar un número con un máximo.", "Sé qué es una tolerancia."],
    explain=[
        "Los defectos se clasifican según su gravedad. Un defecto crítico puede dañar a quien usa la prenda o incumplir una norma, como un botón suelto en una prenda infantil, porque un niño podría llevárselo a la boca. Un defecto mayor afecta el uso o se ve de forma notoria, como una costura abierta. Un defecto menor casi no afecta, como un hilo suelto pequeño. La clasificación define qué tan estricto es el criterio.",
        "Como revisar todas las prendas puede ser lento o inviable, se hace muestreo: se revisa una parte del lote, que es la muestra, y se juzga el lote completo con un criterio de aceptación. Ese criterio fija cuántos defectos de cada tipo se aceptan en la muestra; en este cuaderno los valores son de ejemplo. Si la muestra supera el máximo en algún tipo, el lote no se acepta.",
        "Una no conformidad es un incumplimiento de un requisito de la ficha. Cuando se encuentra una, se registra y se define una acción correctiva, que busca corregir la causa para que no se repita. El inspector registra lo que encuentra sin alterar los datos." + LIM,
    ],
    vocab=[("defecto crítico", "defecto que puede dañar a quien usa la prenda o incumple una norma"), ("defecto mayor", "defecto que afecta el uso o se ve de forma notoria"), ("defecto menor", "defecto que casi no afecta"), ("muestra", "parte del lote que se revisa para juzgar el lote completo"), ("criterio de aceptación", "máximo de defectos de cada tipo que acepta el lote"), ("no conformidad", "incumplimiento de un requisito de la ficha"), ("acción correctiva", "acción que corrige la causa para que no se repita")],
    worked=[
        ("Clasificar un defecto", "Una prenda de ejemplo tiene una mancha grande y visible en el frente. ¿Qué tipo de defecto es?", ["Se ve de forma notoria.", "Es un defecto mayor."], "Mayor"),
        ("Aplicar un criterio", "Un criterio de ejemplo acepta hasta 2 defectos mayores en una muestra y se encuentran 3. ¿Se acepta el lote?", ["3 supera el máximo de 2.", "No se acepta."], "No se acepta"),
    ],
    mistakes=[("Clasificar un botón suelto de una prenda infantil como menor.", "Puede dañar a un niño y es un defecto crítico.", "Evalúa el riesgo para quien usa la prenda."),
              ("Aceptar el lote porque la muestra «casi» cumple.", "El criterio es un máximo exacto.", "Compara cada tipo de defecto con su máximo.")],
    T=[
        ("abc", "{F} ¿Cómo se clasifica un botón suelto en una prenda infantil?", "Como defecto crítico", "Como defecto menor", "Como defecto mayor", "Puede dañar a un niño, por eso es crítico."),
        ("abc", "{F} ¿Cómo se clasifica una costura abierta?", "Como defecto mayor", "Como defecto crítico", "Como defecto menor", "Afecta el uso de la prenda y se ve de forma notoria."),
        ("abc", "{F} ¿Cómo se clasifica un hilo suelto pequeño?", "Como defecto menor", "Como defecto mayor", "Como defecto crítico", "Casi no afecta el uso de la prenda."),
        ("abc", "En Vestuario y Confección Textil: ¿qué es la muestra?", "Una parte del lote que se revisa para juzgar el lote completo", "La prenda más bonita del lote", "El lote completo", "La muestra representa al lote y evita revisar cada prenda."),
        ("abc", "{F} ¿Qué es una acción correctiva?", "Lo que se hace para corregir la causa y que no se repita", "Registrar el defecto en la hoja", "Rechazar el lote sin explicar", "La acción correctiva actúa sobre la causa."),
        ("abc", "{F} ¿Qué es una no conformidad?", "Un incumplimiento de un requisito de la ficha", "Un defecto cualquiera sin importancia", "Una aprobación del cliente", "La no conformidad es un incumplimiento de lo especificado."),
        ("abc", "{F} ¿Cuántos defectos críticos acepta el criterio de ejemplo en una muestra de 50?", "Ninguno", "Hasta 3", "Hasta 6", "El criterio acepta 0 críticos; 3 y 6 son los máximos de mayores y menores."),
        ("abc", "{F} Una muestra de 50 tiene 0 críticos, 3 mayores y 6 menores. ¿Se acepta el lote?", "Sí, porque cada tipo está dentro de su máximo", "No, porque tiene defectos", "No, porque hay 9 defectos en total", "Los máximos son 0, 3 y 6, y se cumplen justo."),
        ("abc", "{F} Una muestra de 50 tiene 0 críticos, 2 mayores y 7 menores. ¿Se acepta el lote?", "No, porque los menores superan el máximo de 6", "Sí, porque tiene pocos mayores", "Sí, porque no hay críticos", "Basta que un tipo supere su máximo para no aceptar el lote."),
        ("=", "{F} Una muestra de 50 prendas tiene 4 mayores. ¿Cuántos mayores sobran sobre el máximo aceptado?", "4-3", "Se restan los defectos aceptados a los encontrados.", " mayores"),
        ("abc", "Un revisor dice: «como el defecto crítico es solo una prenda de 50, aceptemos el lote». ¿Qué observación es correcta?", "El criterio de ejemplo acepta 0 críticos, así que el lote no se acepta", "Tiene razón, porque es una sola prenda", "Se acepta si el defecto es pequeño", "Un defecto crítico no se acepta aunque sea uno."),
        ("abc", "Un lote tiene muchas manchas porque la tela se manchó en la bodega. ¿Cuál es una acción correctiva adecuada?", "Corregir las condiciones de almacenamiento para que no se repita", "Cambiar el color de la ficha", "Anotar solo «mala suerte»", "La acción correctiva actúa sobre la causa del defecto."),
        ("=", "Se revisa una muestra de 80 prendas de un lote de 800. ¿Qué porcentaje del lote se revisa?", "80*100//800", "Se divide la muestra por el lote y se multiplica por 100.", " %"),
    ],
    ctx=("abc", "{F} Un lote de poleras infantiles tiene una muestra con 1 botón suelto, 2 costuras abiertas y 4 hilos sueltos. ¿Se acepta el lote?", "No, porque hay un defecto crítico y el criterio acepta 0", "Sí, porque los mayores y menores están en el máximo", "Sí, porque los críticos son pocos", "El botón suelto es crítico y el máximo es cero."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué diferencia hay entre defecto crítico y menor?", "El crítico puede dañar a quien usa la prenda; el menor casi no afecta", "La clasificación define qué tan estricto es el criterio."),
        ("¿Para qué sirve el muestreo?", "Para juzgar el lote revisando una parte", "Así se evita revisar todas las prendas del lote."),
        ("¿Qué busca una acción correctiva?", "Corregir la causa para que no se repita", "Actúa sobre el origen del problema."),
    ],
    op=("Criterio de ejemplo para una muestra de 40 prendas: 0 críticos, hasta 2 mayores y hasta 5 menores. Se encontraron: 1 costura abierta, 1 mancha grande, 3 hilos sueltos y 1 cierre que se traba. "
        "Escribe: (a) la clasificación de cada defecto, (b) si se acepta el lote y por qué, y (c) una acción correctiva posible.",
        "(a) Costura abierta: mayor. Mancha grande: mayor. Hilos sueltos: menores. Cierre que se traba: mayor, porque afecta el uso. (b) No se acepta: hay 3 mayores y el máximo es 2. (c) Revisar el proveedor de cierres y reforzar el control en proceso de las costuras.",
        ["clasifica correctamente los defectos", "compara cada tipo con su máximo", "propone una acción correctiva"],
        ["hoja con los tres puntos"],
        ["clasificar el cierre como menor", "sumar todos los defectos juntos", "no proponer acción correctiva"],
        "Pregunta: «¿cuántos defectos mayores hay?». Debe responder 3."),
    reinforce="Inventa cinco defectos de una prenda y clasifica cada uno como crítico, mayor o menor.",
    extend="Explica con un ejemplo inventado por qué los criterios de aceptación fijan máximos por cada tipo de defecto.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 32 (informe de inspección de ejemplo, inventado). Lote de 600 camisas del modelo CA-6. Muestra: 50 camisas. Criterio de aceptación de ejemplo: 0 críticos, hasta 3 mayores y hasta 6 menores. "
     "Hallazgos de la muestra: críticos, 0; mayores, 4 (2 costuras abiertas, 1 mancha grande y 1 botón mal pegado que se desprende); menores, 5 (hilos sueltos). Decisión posible: aceptar, rechazar o aceptar tras reinspección (revisión repetida) de las prendas corregidas. "
     "Reproceso: corregir una prenda defectuosa; tiempo de ejemplo 10 minutos por prenda y $50 por minuto de mano de obra.")
build(
    O8, 3, F,
    use="Aprenderé a analizar un informe de inspección en papel: comparar los hallazgos con el criterio, decidir sobre el lote y estimar el costo de corregirlo.",
    prior=["Conozco los tipos de defecto y el criterio de aceptación.", "Sé comparar números con un máximo.", "Sé calcular un porcentaje."],
    explain=[
        "Para analizar un informe de inspección se comparan los hallazgos de la muestra con el criterio de aceptación, tipo por tipo. Si en cualquier tipo se supera el máximo, el lote no se acepta tal como está. Entonces se puede rechazar o, si es posible, corregir las prendas defectuosas y repetir la inspección, lo que se llama reinspección. La decisión la toma la jefatura con los datos del informe.",
        "El porcentaje de defectos de una muestra es la cantidad de prendas defectuosas dividida por el tamaño de la muestra, por 100. Sirve para comparar lotes distintos. El reproceso es la corrección de una prenda defectuosa; tiene un costo que se calcula multiplicando el tiempo por el costo de la mano de obra. Antes de elegir entre rechazar y reprocesar, se comparan ambos costos.",
        "Todo queda en el informe: los hallazgos, el criterio, la decisión, las acciones y los responsables. Un defecto crítico no se negocia: nunca se acepta. Si el análisis muestra una causa repetida, se propone una acción correctiva para que no se repita." + LIM,
    ],
    vocab=[("reinspección", "revisión repetida de las prendas corregidas"), ("reproceso", "corrección de una prenda defectuosa"), ("porcentaje de defectos", "prendas defectuosas dividido por la muestra, por 100"), ("rechazar un lote", "no aceptarlo tal como está"), ("informe de inspección", "registro de hallazgos, criterio y decisión")],
    worked=[
        ("Calcular el porcentaje de defectos", "En una muestra de ejemplo de 40 prendas hay 4 defectuosas. ¿Qué porcentaje es?", ["4 ÷ 40 = 0,1.", "En porcentaje, 4 × 100 ÷ 40 = 10."], "10 %"),
        ("Costo de reproceso", "Corregir una prenda de ejemplo cuesta 15 minutos a $40 el minuto. ¿Cuánto cuesta corregir 6 prendas?", ["Una prenda cuesta 15 × 40 = 600.", "Seis prendas cuestan 6 × 600 = 3.600."], "$3.600"),
    ],
    mistakes=[("Aceptar el lote porque en total hay pocos defectos.", "El criterio mira cada tipo por separado.", "Compara cada tipo con su máximo."),
              ("Reprocesar sin calcular el costo.", "Puede costar más que rechazar o negociar.", "Compara ambos costos.")],
    T=[
        ("abc", "{F} ¿Los defectos mayores cumplen el criterio?", "No, porque hay 4 y el máximo es 3", "Sí, porque 4 es poco", "Sí, porque el total de defectos es menor que 10", "El criterio acepta hasta 3 mayores y se encontraron 4."),
        ("abc", "{F} ¿Los defectos menores cumplen el criterio?", "Sí, porque hay 5 y el máximo es 6", "No, porque hay hilos sueltos", "No, porque 5 es más que 3", "Los 5 menores están dentro del máximo de 6."),
        ("abc", "{F} ¿Se acepta el lote tal como está?", "No, porque los mayores superan el máximo", "Sí, porque no hay defectos críticos", "Sí, porque los menores cumplen", "Basta que un tipo supere su máximo para no aceptar el lote tal como está."),
        ("=", "{F} ¿Cuántos defectos mayores sobran respecto del máximo aceptado?", "4-3", "Se restan los defectos aceptados a los encontrados.", " defecto mayor"),
        ("=", "{F} ¿Cuántas prendas defectuosas hay en la muestra, suponiendo que cada hallazgo es de una prenda distinta?", "0+4+5", "Se suman los hallazgos de los tres tipos.", " prendas"),
        ("=", "{F} ¿Qué porcentaje de la muestra tiene un defecto, con ese supuesto?", "(0+4+5)*100//50", "Se divide la cantidad de prendas con defecto por la muestra y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuánto cuesta reprocesar una prenda defectuosa?", "10*50", "Se multiplica el tiempo por el costo por minuto.", " pesos"),
        ("=", "{F} ¿Cuánto costaría reprocesar solo las 4 prendas con defectos mayores?", "4*10*50", "Se multiplica la cantidad por el costo de reproceso de una prenda.", " pesos"),
        ("abc", "{F} Si se reprocesan las 4 prendas con defectos mayores, ¿qué corresponde antes de aceptar el lote?", "Una reinspección que compruebe que quedaron corregidas", "Aceptarlo sin revisar", "Dar por corregidas las prendas por haberlas reprocesado", "La reinspección verifica que la corrección resultó."),
        ("abc", "La jefatura propone aceptar el lote para cumplir el plazo, aunque supera el máximo. ¿Qué corresponde?", "Informar la no conformidad y reprocesar o negociar con el cliente, sin esconderla", "Aceptarlo en silencio", "Cambiar el criterio sin avisar", "No se acepta un lote que incumple sin informar."),
        ("abc", "{F} Los 2 hallazgos de costuras abiertas indican una posible causa común. ¿Cuál es una acción correctiva adecuada?", "Revisar la causa de la costura abierta en el proceso y reforzar el control en proceso", "Anotar «mala suerte»", "Cambiar el color del hilo sin analizar", "La acción correctiva busca la causa y evita repetirla."),
        ("=", "Una muestra de 80 prendas tiene 8 defectuosas. ¿Qué porcentaje de defectos es?", "8*100//80", "Se divide las prendas defectuosas entre la muestra y se multiplica por 100.", " %"),
        ("abc", "{F} Un revisor omite en el informe el botón que se desprende porque «ya se arregló». ¿Qué observación es correcta?", "Debe quedar registrado el hallazgo y su corrección", "Está bien omitirlo, porque se arregló", "Está bien omitirlo si nadie lo vio", "El informe debe reflejar todo lo encontrado, aunque se haya corregido."),
    ],
    ctx=("=", "{F} Si se rechazara el lote de 600 camisas y se perdiera $3.000 por camisa en producción, ¿cuánto se perdería?", "600*3000", "Se multiplican las camisas por el costo de cada una.", " pesos"),
    sc=[
        ("En Vestuario y Confección Textil: ¿cuándo no se acepta un lote?", "Cuando algún tipo de defecto supera su máximo", "Basta que un tipo exceda el máximo."),
        ("¿Para qué sirve la reinspección?", "Para comprobar que las prendas corregidas quedaron bien", "Verifica que la corrección realmente funcionó en las prendas."),
        ("¿Se oculta un hallazgo ya corregido?", "No", "El informe refleja todo lo encontrado."),
    ],
    op=("Informe de ejemplo: lote de 400 pantalones; muestra de 50; criterio: 0 críticos, hasta 2 mayores y hasta 5 menores. Hallazgos: 1 crítico (cierre que se desprende), 1 mayor y 6 menores. Reproceso: 12 minutos por prenda a $50 el minuto. "
        "Escribe: (a) qué tipos incumplen el criterio, (b) tu decisión, (c) el costo de reprocesar las 8 prendas con hallazgos suponiendo que cada hallazgo es de una prenda distinta y (d) una acción correctiva.",
        "(a) Los críticos (hay 1 y el máximo es 0) y los menores (hay 6 y el máximo es 5). (b) No se acepta el lote; se reprocesan las prendas y se hace una reinspección. (c) 8 × 12 × 50 = 4.800 pesos. (d) Revisar el origen del cierre defectuoso y reforzar el control al recibir los cierres.",
        ["detecta los dos tipos que incumplen", "decide con reinspección", "calcula el costo de reproceso", "propone una acción correctiva"],
        ["hoja con los cuatro puntos"],
        ["aceptar el lote por tener pocos defectos totales", "olvidar el crítico", "no calcular el costo"],
        "Pregunta: «¿se negocia un defecto crítico?». Debe responder que no, nunca se acepta."),
    reinforce="Inventa un informe con tres tipos de defecto y decide si se acepta el lote con un criterio dado.",
    extend="Explica con un ejemplo inventado por qué se compara el costo de reprocesar con el de rechazar.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 33 (control de medidas de ejemplo, inventado). Ficha técnica del modelo PE-20, talla M, medidas de la prenda terminada en cm, con tolerancia de ejemplo: ancho de pecho 50 (± 1); largo total 64 (± 1); largo de manga 19 (± 1); ancho de hombros 38 (± 1). "
     "Prendas medidas en la muestra, en el mismo orden (pecho, largo, manga, hombros): prenda 1: 50, 65, 19, 38. Prenda 2: 52, 64, 18, 38. Prenda 3: 49, 62, 20, 39. Prenda 4: 50, 64, 19, 36. Una prenda cumple si todas sus medidas están dentro de la tolerancia.")
build(
    O8, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: verificar si las medidas de una muestra cumplen la ficha con una tolerancia y calcular el porcentaje de cumplimiento.",
    prior=["Conozco la tolerancia y la ficha técnica.", "Sé restar y comparar.", "Sé calcular un porcentaje."],
    explain=[
        "Para verificar una medida se calcula la diferencia entre la medida real y la de la ficha, sin importar el signo. Si esa diferencia es igual o menor que la tolerancia, la medida cumple; si es mayor, no cumple. Una prenda cumple solo si todas sus medidas cumplen. Esto se registra en una tabla de control de medidas, con la medida pedida, la medida real y el resultado.",
        "El porcentaje de cumplimiento de una muestra es la cantidad de prendas que cumplen dividida por las prendas medidas, por 100. Si una medida falla de forma repetida en varias prendas, es señal de un problema en el proceso o en el molde, y se propone una acción correctiva. Si falla solo en una prenda, puede ser un error aislado.",
        "Las mediciones se hacen siempre de la misma manera, tal como lo indica la ficha, por ejemplo, con la prenda extendida. Los valores y las tolerancias de este cuaderno son de ejemplo. La decisión final la toma la jefatura de calidad." + LIM,
    ],
    vocab=[("diferencia", "resultado de restar la menor medida a la mayor, sin signo"), ("medida real", "medida tomada en la prenda"), ("porcentaje de cumplimiento", "prendas que cumplen dividido por las medidas, por 100"), ("error aislado", "falla que aparece en una sola prenda"), ("falla repetida", "falla que aparece en varias prendas")],
    worked=[
        ("Verificar una medida", "Una medida de ejemplo pide 30 cm con tolerancia de 1 cm y la prenda mide 32 cm. ¿Cumple?", ["La diferencia es 2 cm.", "2 es mayor que 1: no cumple."], "No cumple"),
        ("Porcentaje de cumplimiento", "De 5 prendas de ejemplo, 4 cumplen. ¿Cuál es el porcentaje de cumplimiento?", ["4 × 100 ÷ 5 = 80.", "El porcentaje es 80."], "80 %"),
    ],
    mistakes=[("Considerar solo una medida de la prenda y dar por buena toda la prenda.", "Una prenda cumple solo si todas sus medidas cumplen.", "Verifica cada medida."),
              ("Restar la medida pedida a la real y dejar un resultado negativo sin interpretarlo.", "Importa cuánto se aleja, no el signo.", "Usa la diferencia sin signo.")],
    T=[
        ("=", "{F} ¿Cuál es la diferencia de largo total de la prenda 1 respecto de la ficha?", "65-64", "Se resta la medida de la ficha a la medida real.", " cm"),
        ("abc", "{F} ¿Cumple la prenda 1?", "Sí, porque todas sus diferencias son de 1 cm o menos", "No, porque su largo es 65", "No, porque tiene una medida distinta", "El largo difiere en 1 cm, igual a la tolerancia, y las demás coinciden."),
        ("=", "{F} ¿Cuál es la diferencia de ancho de pecho de la prenda 2?", "52-50", "Se resta la medida de la ficha a la medida real.", " cm"),
        ("abc", "{F} ¿Cumple la prenda 2?", "No, porque su ancho de pecho difiere en 2 cm", "Sí, porque el largo coincide", "Sí, porque la manga se acerca", "El pecho difiere en 2 cm y supera la tolerancia de 1 cm."),
        ("abc", "{F} ¿Cumple la prenda 3?", "No, porque su largo difiere en 2 cm", "Sí, porque su pecho difiere solo en 1 cm", "Sí, porque sus hombros difieren en 1 cm", "El largo es 62 y la ficha pide 64; la diferencia de 2 cm supera la tolerancia."),
        ("abc", "{F} ¿Cumple la prenda 4?", "No, porque sus hombros difieren en 2 cm", "Sí, porque tres medidas coinciden", "Sí, porque los hombros se acercan a la ficha", "Los hombros miden 36 y la ficha pide 38; la diferencia de 2 supera la tolerancia."),
        ("=", "{F} Fallan las prendas 2, 3 y 4. ¿Cuántas de las 4 prendas medidas cumplen la ficha?", "4-3", "Solo la prenda 1 tiene todas sus medidas dentro de la tolerancia.", " prenda"),
        ("=", "{F} ¿Cuál es el porcentaje de cumplimiento de la muestra?", "1*100//4", "Se divide las prendas que cumplen por las medidas y se multiplica por 100.", " %"),
        ("abc", "{F} La medida de largo falla en una sola prenda. ¿Qué es más razonable pensar?", "Que puede ser un error aislado, aunque conviene revisarlo", "Que todo el lote tiene un problema grave", "Que la ficha está mal", "Una sola falla puede ser aislada; la repetición sugiere un problema de proceso."),
        ("abc", "{F} Las fallas son de medidas distintas en prendas distintas, y la muestra es pequeña. ¿Qué corresponde recomendar?", "Medir más prendas para saber si la falla se repite", "Aceptar el lote", "Cambiar las tolerancias de la ficha", "Una muestra pequeña con fallas variadas necesita más datos antes de decidir."),
        ("abc", "Un revisor mide con la prenda estirada y otro con la prenda extendida plana. ¿Qué problema hay?", "Los resultados no son comparables porque no se mide de la misma manera", "No hay problema, porque da igual", "Siempre da el mismo resultado", "La ficha define cómo medir para que las mediciones sean comparables."),
        ("=", "Otra muestra de ejemplo tiene 20 prendas y 17 cumplen. ¿Qué porcentaje de cumplimiento tiene?", "17*100//20", "Se divide las prendas que cumplen por las medidas y se multiplica por 100.", " %"),
        ("abc", "El jefe de producción propone ampliar la tolerancia de la ficha a ± 2 cm para que más prendas cumplan. ¿Qué corresponde?", "No cambiarla por conveniencia; la tolerancia solo cambia con la aprobación de quienes responden por la ficha", "Cambiarla, porque aumenta el porcentaje", "Cambiarla solo en esta muestra", "La tolerancia se fija en la ficha y no se ajusta para aprobar un lote."),
    ],
    ctx=("abc", "{F} Se informa al cliente el resultado de la muestra. ¿Qué informe es honesto?", "Que 1 de 4 prendas cumple, con las medidas que fallan y una acción correctiva", "Que el lote cumple porque tres medidas coinciden", "Que el lote está perfecto", "El informe honesto muestra datos reales y las acciones propuestas."),
    sc=[
        ("En Vestuario y Confección Textil: ¿cuándo cumple una medida?", "Cuando la diferencia con la ficha es igual o menor que la tolerancia", "Se compara la diferencia sin signo con la tolerancia."),
        ("¿Cuándo cumple una prenda?", "Cuando todas sus medidas cumplen", "Una medida fuera de la tolerancia basta para que no cumpla."),
        ("¿Qué indica una falla repetida?", "Un posible problema en el proceso o en el molde", "Una falla en varias prendas no es casualidad."),
    ],
    op=("Ficha de ejemplo del modelo DE-5: ancho de pecho 60 (± 1) y largo total 72 (± 1). Medidas de 5 prendas (pecho, largo): 1: 60, 72; 2: 61, 73; 3: 58, 72; 4: 60, 70; 5: 59, 71. "
        "Escribe: (a) cuáles prendas cumplen, (b) el porcentaje de cumplimiento, (c) qué medida falla con más frecuencia y (d) una acción correctiva posible.",
        "(a) Cumplen las prendas 1, 2 y 5. La 3 falla en el pecho (58) y la 4 falla en el largo (70). (b) 3 × 100 ÷ 5 = 60 %. (c) Fallan una vez el pecho y una vez el largo, sin una repetición clara. (d) Medir más prendas y revisar el molde y el proceso de las medidas que fallan.",
        ["verifica cada prenda con la tolerancia", "calcula el porcentaje", "analiza la repetición", "propone una acción correctiva"],
        ["hoja con los cuatro puntos"],
        ["considerar solo una medida", "olvidar el signo de la diferencia", "no proponer una acción"],
        "Pregunta: «¿la prenda 5 cumple?». Debe responder que sí, porque sus diferencias son de 1 cm."),
    reinforce="Inventa una ficha con dos medidas y cuatro prendas medidas, y calcula cuántas cumplen.",
    extend="Explica con un ejemplo inventado por qué no se cambia la tolerancia para aprobar un lote.",
)
