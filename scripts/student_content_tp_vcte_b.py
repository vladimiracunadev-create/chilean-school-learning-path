"""Vestuario y Confección Textil TP (3.º y 4.º medio): OAE-03 (marcar y cortar telas: consumo, rendimiento y eficiencia; solo conceptos y cálculos), OAE-04 (máquinas industriales y semiindustriales: solo conceptos, manual y seguridad) y OAE-05 (mantenimiento y regulación de máquinas: solo conceptos, registros y cálculos). Todo en papel, con datos de ejemplo."""
from __future__ import annotations

from tp_vcte_common import build

O3 = "TP-VCTE-3y4-OAE-03"
O4 = "TP-VCTE-3y4-OAE-04"
O5 = "TP-VCTE-3y4-OAE-05"
LIM = " Esto es aprendizaje conceptual en papel, con datos de ejemplo: la práctica en un taller de confección requiere instructor/docente de la especialidad y norma vigente; este cuaderno no te habilita para trabajar. Ante un accidente, avisa a un adulto responsable y a emergencias."
LIMX = " Las tijeras, las cortadoras, las agujas, las máquinas de coser, las planchas y el vapor se estudian aquí solo como concepto: su uso, ajuste y mantención requieren instructor/docente de la especialidad y norma vigente; este cuaderno no te habilita para trabajar. Ante un accidente, avisa a un adulto responsable y a emergencias."

# ============================================================ OAE-03, clase 1
F = ("Ficha 10 (sala de corte de ejemplo, inventada). El corte es la etapa que separa de la tela las piezas de la prenda, según la ficha técnica y los moldes. Se puede hacer en forma manual (con tijeras) o con máquina (cortadoras), siempre por personal capacitado y autorizado. "
     "El jefe de corte lee la orden de corte y la ficha: modelo, tipo de tela, consumo y cantidad de prendas. El tendido es la disposición de la tela en capas sobre la mesa; la marcada es la distribución de los moldes sobre la tela para aprovecharla. "
     "Reglas generales: no se corta sin orden de corte; los rollos pesados se mueven con ayuda o medios de apoyo; cualquier defecto de la tela se avisa antes de cortar; la pelusa se mantiene a raya con orden, limpieza y ventilación.")
build(
    O3, 1, F,
    use="Aprenderé a situar la etapa de corte: qué se hace en ella, qué conceptos usa, quién responde y qué riesgos y reglas existen.",
    prior=["Conozco la ficha técnica y los moldes.", "Sé multiplicar y dividir con enteros.", "Sé que la tela se compra en rollos."],
    explain=[
        "En Vestuario y Confección Textil, el corte transforma la tela de un rollo en las piezas que luego se coserán. Antes del corte se prepara el tendido, que es la tela dispuesta en capas, y la marcada, que es la distribución de los moldes sobre la tela de modo que se aproveche al máximo. La ficha técnica indica el tipo de tela y el consumo, es decir, cuánta tela usa una prenda; la orden de corte indica cuántas prendas y de qué talla.",
        "El rendimiento es cuántas prendas salen de una cantidad de tela, y la merma es la tela que se pierde o sobra porque no cabe una pieza. Un buen corte busca gastar solo la tela necesaria y registrar la merma para detectar desperdicio. El corte puede ser manual o con máquina, pero siempre lo ejecuta personal capacitado, con las protecciones y la autorización correspondiente.",
        "Los riesgos son los cortes, el atrapamiento de manos, el levantamiento de rollos pesados, el estar de pie por muchas horas y la pelusa en el aire. Las reglas generales incluyen pedir ayuda o usar apoyos para mover rollos, hacer pausas, mantener la mesa ordenada y avisar si la tela trae manchas o roturas antes de cortarla. Si ocurre un accidente se avisa de inmediato a un adulto responsable y a emergencias." + LIMX,
    ],
    vocab=[("corte", "etapa que separa de la tela las piezas de la prenda"), ("tendido", "tela dispuesta en capas sobre la mesa"), ("marcada", "distribución de los moldes sobre la tela para aprovecharla"), ("consumo", "cantidad de tela que usa una prenda"), ("rendimiento", "cuántas prendas salen de una cantidad de tela"), ("merma", "tela que se pierde o sobra porque no cabe una pieza"), ("orden de corte", "documento que indica cuántas prendas y de qué talla cortar")],
    worked=[
        ("Calcular el rendimiento", "Un rollo de ejemplo tiene 40 metros y cada falda consume 2 metros. ¿Cuántas faldas rinde el rollo?", ["Se divide el largo del rollo por el consumo.", "40 ÷ 2 = 20."], "20 faldas"),
        ("Decidir ante un defecto", "Al abrir un rollo de ejemplo se ve una mancha grande. ¿Qué corresponde antes de cortar?", ["Un defecto en la tela puede aparecer en las piezas.", "Se avisa al jefe de corte o a calidad antes de cortar."], "Avisar antes de cortar"),
    ],
    mistakes=[("Levantar un rollo pesado sin ayuda «para no esperar».", "El esfuerzo sobre la espalda puede provocar una lesión.", "Pide ayuda o usa un medio de apoyo."),
              ("Cortar sin mirar la orden de corte porque «ya se sabe cuántas prendas son».", "Puede cortarse una talla o una cantidad equivocada.", "Revisa la orden de corte antes de empezar.")],
    T=[
        ("abc", "En Vestuario y Confección Textil: ¿qué es el consumo de tela?", "La cantidad de tela que usa una prenda", "La cantidad de prendas que salen de un rollo", "La tela que se pierde en el corte", "El consumo es por prenda; el rendimiento es prendas por tela y la merma es lo que se pierde."),
        ("abc", "{F} ¿Quién puede ejecutar el corte con máquina según la ficha?", "Personal capacitado y autorizado", "Cualquier persona que haya mirado cortar", "Quien termine antes sus tareas", "La ficha pide personal capacitado y autorizado para el corte."),
        ("abc", "{F} ¿Qué documento indica cuántas prendas y de qué talla se cortan?", "La orden de corte", "La carta de colores", "El dibujo plano", "La orden de corte detalla las cantidades y tallas."),
        ("abc", "En Vestuario y Confección Textil: ¿qué es la merma?", "La tela que se pierde o sobra porque no cabe una pieza", "La tela que se compra de más para tener repuesto", "La tela que se usa para el hilo", "La merma es el desperdicio que se registra para mejorar el consumo."),
        ("abc", "{F} ¿Qué es la marcada?", "La distribución de los moldes sobre la tela para aprovecharla", "La tela dispuesta en capas sobre la mesa", "La orden que indica las tallas a cortar", "La marcada ubica los moldes; el tendido dispone la tela en capas."),
        ("abc", "{F} ¿Qué regla corresponde para mover los rollos pesados?", "Pedir ayuda o usar medios de apoyo", "Levantarlos entre pausas sin ayuda", "Arrastrarlos por el suelo sin avisar", "La ficha pide ayuda o apoyos para evitar lesiones de espalda."),
        ("=", "Un rollo de ejemplo tiene 60 metros y cada camisa consume 2 metros. ¿Cuántas camisas rinde el rollo?", "60//2", "Se divide el largo del rollo por el consumo de cada camisa.", " camisas"),
        ("abc", "{F} Al revisar un rollo, aparece una zona con rotura. ¿Qué corresponde?", "Avisar al jefe de corte o a calidad antes de cortar", "Cortar igual y ver qué pasa", "Cortar solo esa zona sin avisar", "Un defecto detectado a tiempo evita piezas dañadas."),
        ("abc", "Una cortadora está encendida y un compañero sin capacitación pide usarla «solo un momento». ¿Qué corresponde?", "Negarse y recordar que solo el personal capacitado y autorizado la usa", "Dejarlo si promete tener cuidado", "Dejarlo si el jefe no está", "La autorización y la capacitación no se reemplazan por la buena intención."),
        ("abc", "Un cortador dice: «ya lo hice antes, no necesito autorización formal». ¿Qué corresponde pensar?", "La práctica no reemplaza la capacitación ni la autorización del taller", "Tiene razón, porque la experiencia basta", "Solo necesita autorización los lunes", "La autorización es un requisito de seguridad, aunque se tenga experiencia."),
        ("abc", "El taller registra la merma de cada orden. ¿Para qué sirve ese registro?", "Para detectar desperdicio y mejorar el aprovechamiento de la tela", "Para decidir el color de la próxima colección", "Para fijar el sueldo del cortador", "El registro permite comparar y corregir pérdidas de tela."),
        ("=", "La ficha indica 2 metros por prenda. El taller programa 120 prendas y compra 245 metros. ¿Cuántos metros se compraron de más que los necesarios, sin considerar merma?", "245-120*2", "Se calcula lo necesario y se resta de lo comprado.", " metros"),
        ("abc", "Dos cortadores de ejemplo dan consumos distintos para el mismo modelo: 2 y 3 metros. ¿Qué documento debe resolver la diferencia?", "La ficha técnica aprobada, que fija el consumo del modelo", "La opinión de quien tenga más años", "El promedio de ambos valores", "El consumo oficial del modelo está en la ficha aprobada."),
    ],
    ctx=("abc", "{F} Una estudiante en práctica ve que la mesa de corte está llena de retazos y pelusa. ¿Qué corresponde?", "Avisar al jefe de corte para ordenar y limpiar, porque el desorden aumenta los riesgos", "Cortar igual para no atrasarse", "Dejar la limpieza para fin de mes", "El orden y la limpieza son parte de las reglas generales de prevención."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué diferencia hay entre consumo y rendimiento?", "El consumo es tela por prenda; el rendimiento es prendas por cantidad de tela", "Son dos formas de expresar la relación entre tela y prendas."),
        ("¿Quién ejecuta el corte con máquina?", "Personal capacitado y autorizado", "El riesgo de las cortadoras exige formación."),
        ("¿Qué se hace al ver un defecto en la tela?", "Se avisa antes de cortar", "Cortar con defectos daña las piezas y desperdicia tela."),
    ],
    op=("Un taller de ejemplo recibe una orden de corte para 25 chaquetas; la ficha indica un consumo de 3 metros por chaqueta y el rollo disponible tiene 80 metros. Escribe: (a) los metros necesarios, (b) cuántas chaquetas rinde el rollo, (c) una regla de seguridad para mover el rollo y (d) qué harías si el rollo trae una mancha.",
        "(a) 25 × 3 = 75 metros. (b) 80 ÷ 3 = 26 chaquetas (con 2 metros sobrantes). (c) Pedir ayuda o usar un medio de apoyo para moverlo. (d) Avisar al jefe de corte o a calidad antes de cortar.",
        ["calcula los metros necesarios", "calcula el rendimiento con división entera", "enuncia una regla de seguridad", "indica avisar antes de cortar"],
        ["hoja con los cuatro puntos"],
        ["multiplicar en lugar de dividir en (b)", "decidir cortar con la mancha", "levantar el rollo solo"],
        "Pregunta: «¿sobra o falta tela?». Debe responder que alcanza para 26 chaquetas, es decir, para las 25 pedidas."),
    reinforce="Escribe con tus palabras qué es el consumo, el rendimiento y la merma, con un ejemplo inventado de cada uno.",
    extend="Explica con un ejemplo inventado por qué avisar de un defecto antes de cortar ahorra tela.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 11 (orden de corte de ejemplo, inventada). Orden de corte N.º 8. Modelo: PE-14. Tela: algodón de punto azul marino, con ancho útil de 150 cm (ancho de la tela que se puede usar, sin los bordes). Consumo según la ficha: 1 metro por polera. "
     "Cantidades: talla S, 20; talla M, 40; talla L, 30. Merma prevista: 4 metros. Responsable: el jefe de corte. Documentos: la orden de corte (cuántas piezas, de qué talla y de qué tela) y la hoja de marcada (diagrama de cómo se distribuyen los moldes en la tela).")
build(
    O3, 2, F,
    use="Aprenderé los documentos y conceptos del corte (orden de corte, hoja de marcada, ancho útil, consumo y merma) y qué rol responde por cada uno.",
    prior=["Conozco el corte, el consumo y la merma.", "Sé sumar y multiplicar.", "Sé leer una orden con cantidades."],
    explain=[
        "La orden de corte indica cuántas prendas y de qué talla se cortan, con qué tela y quién responde. La hoja de marcada muestra cómo se distribuyen los moldes sobre la tela. El ancho útil es el ancho de la tela que realmente se puede usar, sin los bordes; si el ancho útil cambia, la distribución de los moldes y el consumo pueden cambiar. Por eso estos datos deben coincidir con la ficha técnica.",
        "Los metros de tela necesarios se calculan multiplicando el consumo de la ficha por el total de prendas. A ese valor se agrega la merma prevista para obtener los metros que se piden a bodega. Si la tela viene en rollos, se pide una cantidad de rollos completos que cubra los metros necesarios, y se redondea hacia arriba, porque un rollo no se puede pedir por partes.",
        "El jefe de corte responde por la orden, la hoja de marcada y el registro de la merma real. Quien corta no cambia el consumo ni la marcada por cuenta propia: si algo no coincide con la ficha, lo avisa. La bodega de telas entrega lo pedido y registra la salida." + LIM,
    ],
    vocab=[("hoja de marcada", "diagrama de cómo se distribuyen los moldes en la tela"), ("ancho útil", "ancho de la tela que se puede usar, sin los bordes"), ("merma prevista", "metros de tela que se calculan como pérdida inevitable"), ("rollo completo", "rollo de tela que no se divide al pedirlo"), ("bodega de telas", "lugar que guarda y entrega las telas")],
    worked=[
        ("Metros con merma", "Una orden de ejemplo pide 50 prendas con consumo de 2 metros y merma prevista de 3 metros. ¿Cuántos metros se piden?", ["Se calcula 50 × 2 = 100.", "Se suma la merma: 100 + 3 = 103."], "103 metros"),
        ("Rollos que se piden", "Con 103 metros necesarios y rollos de 30 metros, ¿cuántos rollos se piden?", ["103 ÷ 30 da 3 y sobran 13 metros.", "Con 3 rollos no alcanza; se piden 4."], "4 rollos"),
    ],
    mistakes=[("Redondear hacia abajo la cantidad de rollos porque «faltan solo unos metros».", "Esos metros faltantes dejan prendas sin cortar.", "Redondea hacia arriba al pedir rollos."),
              ("Cambiar la marcada porque «así cabe mejor» sin avisar al jefe de corte.", "La marcada y el consumo deben coincidir con la ficha aprobada.", "Avisa y espera una decisión.")],
    T=[
        ("abc", "{F} ¿Qué documento indica cuántas piezas cortar y de qué talla?", "La orden de corte", "La hoja de marcada", "La tabla de medidas", "La orden de corte detalla las cantidades; la hoja de marcada muestra la distribución."),
        ("=", "{F} ¿Cuántas poleras se cortan en total?", "20+40+30", "Se suman las cantidades de las tres tallas.", " poleras"),
        ("abc", "{F} ¿Qué es el ancho útil?", "El ancho de la tela que se puede usar, sin los bordes", "El ancho de la mesa de corte", "El ancho del molde con margen", "El ancho útil es el de la tela realmente utilizable."),
        ("=", "{F} Sin considerar merma, ¿cuántos metros de tela se necesitan?", "(20+40+30)*1", "Se multiplica el total de prendas por el consumo de la ficha.", " metros"),
        ("=", "{F} ¿Cuántos metros se piden a bodega, considerando la merma prevista?", "(20+40+30)*1+4", "A los metros necesarios se agrega la merma prevista.", " metros"),
        ("abc", "En Vestuario y Confección Textil: ¿qué es el rendimiento?", "La cantidad de prendas que salen de una cantidad de tela", "La tela que se pierde en el corte", "El ancho de la tela", "El rendimiento relaciona prendas y tela; la pérdida es la merma."),
        ("=", "{F} La bodega tiene 120 metros de esa tela. Después de entregar los metros pedidos, ¿cuántos metros quedan?", "120-((20+40+30)*1+4)", "Se resta lo entregado a lo que había.", " metros"),
        ("abc", "{F} La orden no indica el ancho útil de la tela. ¿Qué riesgo hay?", "Que la marcada y el consumo sean distintos a los de la ficha", "Que cambie el color de la polera", "Que la orden se vuelva más barata", "El ancho útil afecta la distribución de los moldes y el consumo."),
        ("abc", "{F} ¿Quién responde por el registro de la merma real?", "El jefe de corte", "El encargado de bodega", "El cliente", "La ficha indica que el jefe de corte es el responsable."),
        ("abc", "¿Por qué se prevé una merma al calcular los metros?", "Porque siempre quedan pérdidas inevitables que la tela no puede evitar", "Porque la ficha obliga a pedir siempre el doble de tela", "Porque el cortador no sabe medir", "La merma prevista reconoce el desperdicio inevitable y evita quedarse corto."),
        ("abc", "Llega un rollo con ancho útil de 140 cm en lugar de los 150 cm que dice la orden. ¿Qué corresponde?", "Avisar al jefe de corte para revisar la marcada y el consumo antes de cortar", "Cortar igual con la marcada original", "Cambiar el ancho en la orden a escondidas", "Un ancho menor puede obligar a cambiar la marcada y aumentar el consumo."),
        ("=", "Una orden de ejemplo tiene 70 prendas, consumo de 3 metros por prenda y merma prevista de 10 metros. Los rollos son de 50 metros. ¿Cuántos rollos completos hay que pedir?", "(70*3+10+50-1)//50", "Se calculan los metros y se divide redondeando hacia arriba.", " rollos"),
        ("abc", "Otra orden necesita 130 metros y el rollo es de 40 metros. Un compañero pide 3 rollos porque 130 ÷ 40 es 3,25 y «se redondea a 3». ¿Qué observación es correcta?", "Con 3 rollos solo hay 120 metros; faltan 10, así que hay que pedir 4", "3 rollos alcanzan, porque el decimal es pequeño", "Se deben pedir 5 rollos para estar seguros", "Se redondea hacia arriba porque los 10 metros que faltan no pueden quedar sin cubrir."),
    ],
    ctx=("=", "{F} El taller recibe 3 rollos de 30 metros para esta orden. ¿Alcanza la tela para los metros pedidos? Escribe cuántos metros sobran o faltan (si faltan, con signo negativo).", "3*30-((20+40+30)*1+4)", "Se compara el total de los rollos con los metros pedidos.", " metros"),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué muestra la hoja de marcada?", "Cómo se distribuyen los moldes en la tela", "Es el diagrama de la distribución."),
        ("¿Cómo se calculan los metros necesarios?", "Multiplicando el consumo por el total de prendas", "El consumo se expresa siempre por cada prenda."),
        ("¿Se redondea hacia arriba o hacia abajo la cantidad de rollos?", "Hacia arriba", "Un rollo no se puede pedir por partes y no puede faltar tela."),
    ],
    op=("Orden de corte de ejemplo: 45 faldas con consumo de 2 metros por falda y merma prevista de 5 metros. Los rollos son de 40 metros. Escribe: (a) los metros necesarios con merma, (b) cuántos rollos completos pides, (c) cuántos metros sobran y (d) qué harías si un rollo llega con un ancho útil menor al de la orden.",
        "(a) 45 × 2 + 5 = 95 metros. (b) 3 rollos (120 metros), porque 2 rollos solo dan 80. (c) 120 − 95 = 25 metros. (d) Avisar al jefe de corte para revisar la marcada y el consumo antes de cortar.",
        ["calcula los metros con merma", "redondea hacia arriba", "calcula el sobrante", "indica avisar al jefe de corte"],
        ["hoja con los cuatro puntos"],
        ["olvidar la merma", "pedir 2 rollos", "cortar sin avisar del ancho"],
        "Pregunta: «¿por qué no bastan 2 rollos?». Debe responder que 2 rollos dan 80 metros y se necesitan 95."),
    reinforce="Escribe una orden de corte inventada de una prenda con tres tallas y calcula el total de prendas.",
    extend="Explica con un ejemplo inventado por qué se redondea hacia arriba al pedir rollos.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 12 (comparación de marcadas de ejemplo, inventada). Se cortan 6 poleras de la talla M con la misma superficie de moldes: 48.600 cm² (centímetros cuadrados). Ancho útil de la tela: 150 cm. "
     "Eficiencia de la marcada: porcentaje de la tela usada que ocupan los moldes (área de moldes dividida por el área de tela usada, por 100); el resto es merma. Marcada A: largo 400 cm, todas las piezas respetan el sentido del hilo que pide la ficha. "
     "Marcada B: largo 360 cm, pero 2 piezas están giradas fuera del sentido del hilo que pide la ficha. Orden: 15 marcadas del mismo tipo. Área de tela usada: ancho útil por largo.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso de corte en papel: comparar dos marcadas por eficiencia y por cumplimiento de la ficha, y decidir cuál se aprueba.",
    prior=["Conozco la marcada y la merma.", "Sé multiplicar y dividir con enteros.", "Sé qué es un porcentaje."],
    explain=[
        "La eficiencia de una marcada indica qué parte de la tela usada ocupan los moldes. Se calcula dividiendo el área de los moldes por el área de la tela usada y multiplicando por 100. El área de la tela usada es el ancho útil por el largo de la marcada. Cuanto mayor es la eficiencia, menos merma hay; por eso se busca una marcada que gaste poca tela.",
        "Pero la eficiencia no es el único criterio. La marcada debe respetar las condiciones de la ficha, como el sentido del hilo de la tela. Si una pieza se gira fuera del sentido del hilo, la prenda puede deformarse o verse distinta, aunque se ahorre tela. Entonces una marcada que ahorra más pero incumple la ficha no se aprueba tal como está: se corrige o se descarta.",
        "Al decidir, se anotan la eficiencia, el largo, el cumplimiento de la ficha y quién aprueba. Si al corregir una marcada su eficiencia cambia, se calcula de nuevo y se vuelve a comparar. El ahorro de tela nunca justifica incumplir la ficha." + LIM,
    ],
    vocab=[("eficiencia de la marcada", "porcentaje de la tela usada que ocupan los moldes"), ("área de tela usada", "ancho útil por largo de la marcada"), ("sentido del hilo", "dirección de los hilos de la tela que fija cómo se ubica cada molde"), ("centímetros cuadrados", "unidad para medir áreas pequeñas (cm²)"), ("aprobar", "dar por buena una marcada porque cumple todos los criterios")],
    worked=[
        ("Calcular la eficiencia", "Una marcada de ejemplo usa una tela de 20.000 cm² y los moldes ocupan 15.000 cm². ¿Cuál es la eficiencia?", ["Se divide 15.000 entre 20.000 y se multiplica por 100.", "15.000 × 100 ÷ 20.000 = 75."], "75 %"),
        ("Comparar con un criterio de la ficha", "Una marcada de ejemplo tiene 92 % de eficiencia, pero una pieza está fuera del sentido del hilo. ¿Se aprueba?", ["Incumple una condición de la ficha.", "No se aprueba tal como está."], "No se aprueba"),
    ],
    mistakes=[("Elegir la marcada de mayor eficiencia sin revisar el sentido del hilo.", "Una pieza mal ubicada puede deformar la prenda.", "Revisa todas las condiciones de la ficha antes de comparar la eficiencia."),
              ("Calcular el área de la tela usada con el ancho total y no con el ancho útil.", "Los bordes no se pueden usar y falsean el cálculo.", "Usa el ancho útil por el largo.")],
    T=[
        ("=", "{F} ¿Cuál es la eficiencia de la marcada A (porcentaje)?", "48600*100//(150*400)", "Se divide el área de moldes por el área de tela usada y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es la eficiencia de la marcada B (porcentaje)?", "48600*100//(150*360)", "Se divide el área de moldes por el área de tela de la marcada B.", " %"),
        ("abc", "{F} ¿Qué marcada tiene mayor eficiencia?", "La marcada B", "La marcada A", "Ambas tienen la misma", "B usa menos tela para los mismos moldes, por lo que su eficiencia es mayor."),
        ("abc", "{F} ¿Por qué no se puede aprobar la marcada B tal como está?", "Porque 2 piezas están fuera del sentido del hilo que pide la ficha", "Porque usa menos tela que A", "Porque su largo es menor que 400 cm", "Una condición de la ficha no se puede incumplir para ahorrar tela."),
        ("=", "{F} ¿Cuántos cm² de tela usa la marcada A más que la B?", "150*400-150*360", "Se restan las áreas de tela usadas.", " cm²"),
        ("abc", "En Vestuario y Confección Textil: si una marcada tiene baja eficiencia, ¿qué significa?", "Que hay mucha merma porque los moldes ocupan poca de la tela usada", "Que la tela es de mejor calidad", "Que se usaron menos moldes de los pedidos", "Menor eficiencia significa más tela sin aprovechar."),
        ("=", "{F} Si se hacen las 15 marcadas del tipo A, ¿cuántos cm de largo de tela se usan en total?", "15*400", "Se multiplica el largo de una marcada por el número de marcadas.", " cm"),
        ("=", "{F} Si fuera posible usar la marcada B en las 15 marcadas, ¿cuántos cm de tela se ahorrarían respecto de A?", "15*(400-360)", "Se multiplica el ahorro por marcada por el número de marcadas.", " cm"),
        ("abc", "{F} ¿Qué corresponde pedir al responsable de la marcada B?", "Corregir las 2 piezas, recalcular la eficiencia y presentarla de nuevo", "Mantenerla y avisar después", "Cortar ya con la marcada B", "Una marcada con piezas mal ubicadas se corrige y se vuelve a evaluar."),
        ("abc", "{F} El jefe dice: «aprueba B igual, porque ahorra tela». ¿Qué corresponde responder?", "Que el ahorro no justifica incumplir la ficha, y que B debe corregirse", "Que tiene razón, porque la tela es cara", "Que se apruebe B solo para esta orden", "La ficha aprobada manda; el ahorro no autoriza a incumplirla."),
        ("abc", "El encargado anota solo «marcada B, no aprobada». ¿Qué le falta al registro?", "La eficiencia, el motivo del rechazo y quién decidió", "El color de la tela", "El nombre del cliente", "Un registro completo explica el motivo y deja la responsabilidad."),
        ("=", "{F} La marcada B corregida queda con un largo de 405 cm. ¿Cuál es su eficiencia?", "48600*100//(150*405)", "Se calcula el área de moldes sobre el área nueva de tela usada.", " %"),
        ("abc", "{F} Con la marcada B corregida (largo 405 cm) y la marcada A (largo 400 cm), ¿qué conviene aprobar?", "La marcada A, porque cumple la ficha y tiene mayor eficiencia que B corregida", "La marcada B corregida, porque era la más eficiente al inicio", "Ninguna, porque no se puede decidir", "B corregida tiene 80 % y A tiene 81 %; ambas cumplen y A gasta menos."),
    ],
    ctx=("abc", "{F} Una compañera asegura que la marcada B era mejor porque usa 40 cm menos. ¿Cuál es la respuesta más completa?", "Usaba menos tela, pero incumplía el sentido del hilo; corregida pierde esa ventaja", "Tiene razón, porque usar menos tela siempre es mejor", "Se equivoca, porque B usaba más tela que A", "La ventaja de B desaparece al cumplir la ficha, y por eso se compara de nuevo."),
    sc=[
        ("En Vestuario y Confección Textil: ¿cómo se calcula la eficiencia de una marcada?", "Área de moldes dividida por área de tela usada, por 100", "Indica qué parte de la tela usada ocupan los moldes."),
        ("¿Qué criterio manda sobre el ahorro de tela?", "Cumplir las condiciones de la ficha", "Una marcada que incumple la ficha no se aprueba."),
        ("¿Qué se hace con una marcada que incumple el sentido del hilo?", "Se corrige y se vuelve a calcular", "La corrección puede cambiar su eficiencia."),
    ],
    op=("Caso de ejemplo: dos marcadas para 4 faldas con 36.000 cm² de moldes y ancho útil de 150 cm. Marcada P: largo 300 cm, sentido del hilo respetado. Marcada Q: largo 250 cm, una pieza fuera del sentido del hilo. "
        "Escribe: (a) la eficiencia de cada marcada, (b) cuál no se puede aprobar y por qué, (c) qué dirías para registrar la decisión.",
        "(a) P: 36.000 × 100 ÷ (150 × 300) = 80 %. Q: 36.000 × 100 ÷ (150 × 250) = 96 %. (b) Q no se aprueba, porque una pieza está fuera del sentido del hilo que pide la ficha. (c) «Marcada P aprobada, 80 %, cumple la ficha; marcada Q no aprobada por una pieza fuera del sentido del hilo; decide el jefe de corte».",
        ["calcula ambas eficiencias", "rechaza Q por incumplir la ficha", "redacta un registro con el motivo"],
        ["hoja con los tres puntos"],
        ["aprobar Q por ser más eficiente", "calcular con el ancho equivocado", "no indicar el motivo"],
        "Pregunta: «¿una eficiencia alta basta para aprobar la marcada?». Debe responder que no, porque también debe cumplir la ficha."),
    reinforce="Con un área de moldes y dos largos inventados, calcula la eficiencia de dos marcadas.",
    extend="Explica con un ejemplo inventado por qué una marcada más eficiente no siempre es la mejor.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 13 (pedido de ejemplo, inventado). Pedido: 120 camisas. Consumo según la ficha: 2 metros por camisa. Merma prevista: 12 metros. Rollos de 80 metros. Precio de la tela: $3.000 el metro. "
     "Medición real hecha en una prueba de corte: 215 cm por camisa. Rendimiento por rollo: prendas que salen de un rollo (largo del rollo dividido por el consumo).")
build(
    O3, 4, F,
    use="Aprenderé a aplicar criterios con datos: calcular metros, rollos, costo de tela y comparar el consumo de la ficha con el consumo real.",
    prior=["Conozco el consumo, la merma y el rendimiento.", "Sé multiplicar y dividir con enteros.", "Sé pedir rollos completos."],
    explain=[
        "Para un pedido, los metros necesarios son el consumo por prenda multiplicado por la cantidad de prendas. A ese valor se agrega la merma prevista y se obtienen los metros que se piden. Si la tela viene en rollos, se divide por el largo del rollo y se redondea hacia arriba. El costo de la tela es el precio por metro multiplicado por los metros pedidos.",
        "El rendimiento por rollo se calcula dividiendo el largo del rollo por el consumo de una prenda y tomando la parte entera. Con él se sabe cuántas prendas completas salen de un rollo. Si un rollo trae metros que no se pueden usar, como una zona dañada, esos metros se restan de lo disponible.",
        "A veces la medición real del consumo difiere de la ficha. Se compara con la ficha, se calcula la diferencia por prenda y para el pedido completo, y se informa al jefe de corte para revisar la marcada. No se cambia la ficha por cuenta propia: solo la diseñadora y el jefe de producción pueden aprobar un nuevo consumo." + LIM,
    ],
    vocab=[("metros necesarios", "consumo por prenda por cantidad de prendas"), ("rendimiento por rollo", "prendas completas que salen de un rollo"), ("consumo real", "cantidad de tela que se mide en una prueba de corte"), ("diferencia de consumo", "consumo real menos consumo de la ficha"), ("redondear hacia arriba", "subir al siguiente número entero para cubrir lo que falta")],
    worked=[
        ("Rendimiento por rollo", "Un rollo de ejemplo de 90 metros y un consumo de 3 metros por abrigo. ¿Cuántos abrigos rinde el rollo?", ["Se divide 90 entre 3.", "90 ÷ 3 = 30."], "30 abrigos"),
        ("Costo de tela", "Una orden de ejemplo pide 45 metros de tela a $2.000 el metro. ¿Cuánto cuesta?", ["Se multiplica el precio por los metros.", "45 × 2.000 = 90.000."], "$90.000"),
    ],
    mistakes=[("Calcular los rollos redondeando 3,15 a 3 «porque es lo más cercano».", "Con 3 rollos faltan metros y no se terminan las prendas.", "Redondea hacia arriba: 4 rollos."),
              ("Modificar la ficha porque la prueba de corte dio otro consumo.", "La ficha solo la cambian quienes la aprueban.", "Informa la diferencia al jefe de corte.")],
    T=[
        ("=", "{F} ¿Cuántos metros necesita el pedido, sin considerar la merma?", "120*2", "Se multiplica el consumo por prenda por la cantidad de camisas.", " metros"),
        ("=", "{F} ¿Cuántos metros se piden con la merma prevista?", "120*2+12", "A los metros necesarios se suma la merma.", " metros"),
        ("=", "{F} ¿Cuántas camisas rinde un rollo?", "80//2", "Se divide el largo del rollo por el consumo de una camisa.", " camisas"),
        ("=", "{F} ¿Cuántos rollos completos se piden para el pedido con merma?", "(120*2+12+80-1)//80", "Se dividen los metros pedidos por el largo del rollo, redondeando hacia arriba.", " rollos"),
        ("=", "{F} ¿Cuánto cuesta la tela de los metros pedidos?", "(120*2+12)*3000", "Se multiplican los metros pedidos por el precio por metro.", " pesos"),
        ("abc", "En Vestuario y Confección Textil: ¿por qué se incluye la merma al pedir tela?", "Para cubrir las pérdidas inevitables y no quedar corto", "Para que sobre tela y venderla", "Para aumentar el consumo de la ficha", "La merma prevista evita que falte tela para las últimas prendas."),
        ("=", "{F} Si se piden los rollos completos calculados, ¿cuántos metros sobran de ellos?", "((120*2+12+80-1)//80)*80-(120*2+12)", "Se resta lo pedido al total de los rollos.", " metros"),
        ("=", "{F} La prueba de corte dio un consumo real de 215 cm. ¿Cuántos metros más se necesitarían para las 120 camisas respecto de la ficha?", "120*(215-200)//100", "Se calcula la diferencia por camisa en cm, se multiplica por 120 y se pasa a metros.", " metros"),
        ("abc", "{F} El consumo real supera al de la ficha. ¿Qué corresponde?", "Registrar la diferencia y avisar al jefe de corte para revisar la marcada", "Cambiar la ficha a 215 cm por cuenta propia", "Ignorarla, porque es una sola prueba", "La diferencia se informa; solo quienes aprueban la ficha pueden cambiarla."),
        ("abc", "{F} El jefe quiere pedir solo 3 rollos, es decir 240 metros, «porque alcanza para los 240 metros de las camisas». ¿Qué observación es correcta?", "No alcanza, porque faltan los 12 metros de merma prevista", "Alcanza, porque 240 es exactamente lo necesario", "Alcanza, porque la merma no hace falta", "Con 240 metros no se cubren los 252 que incluyen la merma."),
        ("abc", "Un compañero calcula el costo de la tela como 4 rollos × $3.000, porque pidió 4 rollos. ¿Qué error comete?", "Usa el precio por metro como si fuera por rollo; debe multiplicar por los metros", "Debió multiplicar por la merma", "Debió dividir por el largo del rollo", "El precio es por metro, así que se multiplica por los metros pedidos y no por los rollos."),
        ("=", "{F} Uno de los rollos trae 10 metros inutilizables por una zona dañada. Si se piden los rollos calculados, ¿cuántos metros sobran después de cubrir el pedido con merma?", "((120*2+12+80-1)//80)*80-10-(120*2+12)", "Se resta lo inutilizable del total y luego lo pedido.", " metros"),
        ("abc", "{F} Un rollo llegó con 10 metros dañados, pero el pedido igual se cumple con los otros. ¿Qué es lo más seguro de registrar?", "El defecto, los metros inutilizables y quién lo informó", "Nada, porque no afectó el pedido", "Solo el nombre del proveedor", "Registrar el defecto permite reclamar y mejorar el control de recepción."),
    ],
    ctx=("=", "Otro pedido de ejemplo: 90 abrigos con consumo de 3 metros, merma prevista de 9 metros y rollos de 50 metros. ¿Cuántos rollos completos hay que pedir?", "(90*3+9+50-1)//50", "Se calculan los metros con merma y se dividen por el largo del rollo, redondeando hacia arriba.", " rollos"),
    sc=[
        ("En Vestuario y Confección Textil: ¿cómo se calcula el rendimiento por rollo?", "Dividiendo el largo del rollo por el consumo de una prenda", "Así se sabe cuántas prendas completas salen."),
        ("¿Se redondea hacia arriba o hacia abajo la cantidad de rollos?", "Hacia arriba", "Un rollo no se pide por partes y no puede faltar tela."),
        ("¿Quién aprueba un nuevo consumo?", "La diseñadora y el jefe de producción", "El corte solo informa la diferencia."),
    ],
    op=("Datos de ejemplo: pedido de 60 delantales; consumo de la ficha 2 metros por delantal; merma prevista 6 metros; rollos de 50 metros; tela a $1.800 el metro; consumo real medido en prueba 210 cm. "
        "Escribe: (a) los metros pedidos con merma, (b) los rollos completos, (c) el costo de los metros pedidos y (d) cuántos metros más usarían los 60 delantales con el consumo real y qué harías.",
        "(a) 60 × 2 + 6 = 126 metros. (b) 3 rollos, porque 2 rollos dan solo 100. (c) 126 × 1.800 = 226.800 pesos. (d) 60 × (210 − 200) ÷ 100 = 6 metros más; se registra la diferencia y se avisa al jefe de corte para revisar la marcada.",
        ["calcula metros con merma", "redondea hacia arriba", "calcula el costo", "calcula la diferencia con el consumo real", "propone informar"],
        ["hoja con los cuatro puntos"],
        ["no incluir la merma", "pedir 2 rollos", "cambiar la ficha por cuenta propia"],
        "Pregunta: «¿qué haces con la diferencia de 6 metros?». Debe responder que la registra y avisa al jefe de corte."),
    reinforce="Calcula los metros, los rollos y el costo de un pedido inventado de 30 chaquetas.",
    extend="Explica con un ejemplo inventado por qué la medición real puede diferir de la ficha.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 14 (sala de máquinas de ejemplo, inventada). Máquina recta: une piezas con una costura. Overlock: une y remata el borde de las telas. Cortadora: separa capas de tela. Prensa de fusionado: une una tela con una entretela (tela de refuerzo) usando calor y presión. "
     "Plancha industrial con vapor: da forma y acabado a la prenda. Riesgos: pinchazos con agujas, atrapamiento de manos, cabello o ropa suelta, cortes, quemaduras por calor y vapor, descarga eléctrica, ruido y mala postura. "
     "Reglas generales: se sigue el manual de operaciones; solo personal capacitado y autorizado usa las máquinas; las guardas (protecciones fijas que cubren partes peligrosas) permanecen instaladas; los ajustes y reparaciones los hace personal autorizado; "
     "ante un accidente se avisa a un adulto responsable y a emergencias.")
build(
    O4, 1, F,
    use="Aprenderé a situar el trabajo con máquinas de confección: qué tipos existen, qué riesgos tienen y qué reglas generales se aplican; este cuaderno no enseña a operarlas.",
    prior=["Conozco las etapas de la confección.", "Sé qué es una ficha técnica.", "Sé que las máquinas requieren capacitación."],
    explain=[
        "En Vestuario y Confección Textil se usan máquinas industriales, que son de uso continuo en fábricas, y semiindustriales, que son de menor capacidad. Algunas cosen (la máquina recta une piezas y la overlock une y remata bordes), otras cortan (la cortadora), otras fusionan (la prensa de fusionado une una tela con una entretela, que es una tela de refuerzo, con calor y presión) y otras planchan (la plancha industrial da forma y acabado con calor y vapor).",
        "Cada máquina tiene riesgos propios: pinchazos con las agujas, atrapamiento de manos, cabello o ropa suelta, cortes, quemaduras por calor y vapor, descargas eléctricas, ruido y mala postura. Las guardas son protecciones fijas que cubren las partes peligrosas y no se retiran. Quien opera debe estar capacitado y autorizado, tener el cabello recogido, evitar prendas sueltas y seguir el manual de operaciones.",
        "Los ajustes, las reparaciones y la mantención los hace personal autorizado, nunca el operario por cuenta propia. Si se nota un ruido extraño, una protección faltante o un cable dañado, se deja de usar la máquina y se avisa a la jefatura. Ante un accidente se avisa a un adulto responsable y a emergencias." + LIMX,
    ],
    vocab=[("máquina industrial", "máquina de uso continuo en una fábrica"), ("máquina semiindustrial", "máquina de menor capacidad que la industrial"), ("entretela", "tela de refuerzo que se une a otra tela"), ("guarda", "protección fija que cubre partes peligrosas de una máquina"), ("manual de operaciones", "documento con las instrucciones y advertencias de una máquina"), ("atrapamiento", "riesgo de que una parte del cuerpo o la ropa quede atrapada")],
    worked=[
        ("Asociar máquina y función", "Una máquina une dos piezas y remata el borde. ¿Cuál es?", ["Unir y rematar el borde es la función de la overlock.", "La recta solo une con una costura."], "La overlock"),
        ("Asociar riesgo y máquina", "Una plancha industrial con vapor. ¿Qué riesgo es característico?", ["Usa calor y vapor.", "El riesgo característico es la quemadura."], "Quemaduras"),
    ],
    mistakes=[("Retirar una guarda porque «estorba y trabaja más rápido».", "La guarda protege contra atrapamientos y cortes.", "No retires protecciones y avisa si hay un problema."),
              ("Usar una máquina con el cabello suelto «solo un momento».", "El cabello puede quedar atrapado.", "Recoge el cabello y evita prendas sueltas.")],
    T=[
        ("abc", "En Vestuario y Confección Textil: ¿qué hace una prensa de fusionado?", "Une una tela con una entretela usando calor y presión", "Corta capas de tela", "Remata el borde de las telas", "La prensa une telas con calor y presión; cortar es función de la cortadora."),
        ("abc", "{F} ¿Qué máquina une y remata el borde de las telas?", "La overlock", "La máquina recta", "La cortadora", "La ficha asigna a la overlock unir y rematar."),
        ("abc", "{F} ¿Qué riesgo es típico de la plancha industrial con vapor?", "Las quemaduras por calor y vapor", "Los pinchazos con agujas", "El atrapamiento por la cortadora", "Calor y vapor producen quemaduras; las agujas están en las máquinas de coser."),
        ("abc", "{F} ¿Qué es una guarda?", "Una protección fija que cubre partes peligrosas de la máquina", "Un manual de operaciones", "Una marca para emparejar piezas", "La guarda es una protección y debe permanecer instalada."),
        ("abc", "{F} ¿Quién puede usar las máquinas según la ficha?", "Solo personal capacitado y autorizado", "Cualquier estudiante en práctica", "Quien las haya visto usar", "La ficha exige capacitación y autorización."),
        ("abc", "En Vestuario y Confección Textil: ¿por qué es riesgoso tener el cabello suelto cerca de una máquina?", "Porque puede quedar atrapado en partes móviles", "Porque ensucia la tela", "Porque la máquina se calienta", "El cabello suelto puede enredarse en piezas que se mueven."),
        ("=", "En un turno de 8 horas con 1 hora total de pausas, una máquina de ejemplo produce 12 piezas por hora de trabajo. ¿Cuántas piezas produce en el turno?", "(8-1)*12", "Se multiplican las horas de trabajo por las piezas por hora.", " piezas"),
        ("abc", "{F} Una guarda está desmontada porque «estorbaba». ¿Qué corresponde?", "No usar la máquina y avisar a la jefatura para que se reponga", "Usarla con cuidado", "Usarla solo con materiales livianos", "Sin la protección instalada la máquina no se debe usar."),
        ("abc", "{F} Una estudiante en práctica pide probar la cortadora. ¿Qué corresponde responder?", "Que no puede hacerlo sin capacitación, autorización y un docente de la especialidad", "Que lo haga si promete tener cuidado", "Que lo haga si nadie la ve", "La autorización y la capacitación no se reemplazan por promesas."),
        ("abc", "Una operadora se pincha un dedo con una aguja y dice «no es nada». ¿Qué corresponde?", "Avisar de inmediato a un adulto responsable y a emergencias", "Seguir trabajando sin avisar", "Guardar silencio para no perder tiempo", "Todo accidente se informa a un adulto responsable."),
        ("abc", "El ruido de una sala de máquinas es alto durante todo el turno. ¿Qué medida general corresponde?", "Aplicar las medidas de protección que indique la jefatura y la norma vigente", "Subir el volumen de la radio", "Trabajar sin pausas para terminar antes", "El ruido se controla con medidas definidas por la jefatura y la norma."),
        ("=", "Una sala de ejemplo tiene 18 máquinas y un tercio está en mantención ese día. ¿Cuántas máquinas están disponibles?", "18-18//3", "Se resta a las 18 máquinas las que están en mantención.", " máquinas"),
        ("abc", "Un operario nota un cable pelado en una plancha y dice «mañana lo aviso». ¿Qué corresponde?", "Dejar de usarla y avisar de inmediato a la jefatura", "Seguir usándola con cuidado", "Cubrir el cable con cinta y seguir", "Un cable dañado es un riesgo eléctrico; se avisa y no se usa."),
    ],
    ctx=("abc", "{F} Un estudiante nuevo ve a un compañero quitar la guarda de una máquina para ir más rápido. ¿Qué corresponde?", "Avisar a la jefatura o al docente de la especialidad", "Imitarlo para no quedar atrás", "Callar para no tener problemas", "Retirar una guarda es un riesgo; lo correcto es avisar."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué máquina corta capas de tela?", "La cortadora", "Es la máquina destinada a separar las capas."),
        ("¿Quién hace los ajustes y reparaciones de una máquina?", "Personal autorizado", "Un operario sin autorización no los hace."),
        ("¿Qué se hace ante un accidente?", "Se avisa a un adulto responsable y a emergencias", "Es la regla general de la ficha."),
    ],
    op=("Sala de máquinas de ejemplo. Una estudiante en práctica observa: una overlock sin guarda, una operadora con el cabello suelto y una plancha con un cable pelado. Escribe: (a) el riesgo de cada situación, (b) qué le pedirías a la jefatura en cada caso y (c) una regla general que valga para las tres.",
        "(a) Overlock sin guarda: atrapamiento o cortes. Cabello suelto: que quede atrapado. Cable pelado: descarga eléctrica. (b) Reponer la guarda y no usar la máquina; recoger el cabello antes de operar; dejar de usar la plancha hasta que la repare personal autorizado. (c) Solo personal capacitado y autorizado opera, y ante cualquier problema se avisa a la jefatura.",
        ["identifica un riesgo en cada caso", "propone una acción para cada caso", "enuncia una regla general"],
        ["hoja con los tres puntos"],
        ["decir que la estudiante repare por su cuenta", "no detectar el riesgo eléctrico", "no avisar a la jefatura"],
        "Pregunta: «¿qué debe hacer una estudiante en práctica ante un riesgo?». Debe responder que avisar a la jefatura o al docente."),
    reinforce="Haz una tabla con cuatro máquinas, su función y un riesgo de cada una.",
    extend="Explica con un ejemplo inventado por qué una guarda no se retira aunque el trabajo vaya más lento.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 15 (extracto de un manual de operaciones de ejemplo, inventado, máquina recta MR-1). Sección 1, uso previsto: unir telas livianas y medianas; no usar con cuero grueso ni cartón. "
     "Sección 2, advertencias: solo personal capacitado; guardas instaladas; desconectar de la energía antes de una mantención, que hace personal autorizado. Sección 3, símbolos: triángulo amarillo = peligro; círculo azul = acción obligatoria. "
     "Sección 4, mantención: limpieza al terminar cada turno, con la máquina desconectada; revisión de lubricación cada 40 horas de trabajo (valor de ejemplo). Roles: el operario usa la máquina; el supervisor controla el trabajo; el técnico de mantención repara; el prevencionista de riesgos vigila el cumplimiento de las medidas de seguridad.")
build(
    O4, 2, F,
    use="Aprenderé a leer un manual de operaciones y a distinguir los documentos y roles que hay alrededor de una máquina; no aprenderé a operarla.",
    prior=["Conozco los tipos de máquinas y sus riesgos.", "Sé multiplicar y dividir.", "Sé que las guardas no se retiran."],
    explain=[
        "El manual de operaciones es el documento del fabricante que explica para qué sirve una máquina, qué advertencias tiene y cómo debe mantenerse. Se organiza en secciones: el uso previsto, que dice qué materiales y tareas admite; las advertencias de seguridad; los símbolos de la máquina, como un triángulo amarillo de peligro o un círculo azul de acción obligatoria; y la mantención, con las tareas y su frecuencia. Una máquina solo se usa para su uso previsto.",
        "Alrededor de la máquina hay roles distintos. El operario usa la máquina siguiendo el manual y avisa de cualquier anomalía. El supervisor controla el trabajo y decide qué máquina se usa. El técnico de mantención hace las reparaciones y los ajustes. El prevencionista de riesgos vigila que se cumplan las medidas de seguridad. Cada uno responde por lo suyo y nadie hace el trabajo de otro sin autorización.",
        "Cuando algo no se entiende, no se adivina: se pregunta al supervisor o se pide una copia del manual. Si el manual falta o está en otro idioma, se informa a la jefatura y no se opera hasta tenerlo. Las frecuencias de mantención del manual, como cada 40 horas de trabajo, se convierten en un calendario según las horas de uso." + LIMX,
    ],
    vocab=[("uso previsto", "tareas y materiales para los que el fabricante diseñó la máquina"), ("advertencia", "aviso de seguridad del manual"), ("símbolo de seguridad", "dibujo que indica peligro u obligación"), ("operario", "persona que usa la máquina"), ("supervisor", "persona que controla el trabajo"), ("técnico de mantención", "persona autorizada que repara y ajusta"), ("prevencionista de riesgos", "profesional que vigila el cumplimiento de la seguridad")],
    worked=[
        ("Leer el uso previsto", "Un manual de ejemplo dice: «uso previsto: telas livianas; no usar con cuero grueso». ¿Se puede usar con cuero grueso?", ["El manual lo excluye del uso previsto.", "No se debe usar para esa tarea."], "No"),
        ("Convertir horas en días", "Una revisión se hace cada 30 horas de trabajo y la máquina trabaja 6 horas al día. ¿Cada cuántos días de trabajo es la revisión?", ["Se divide 30 entre 6.", "30 ÷ 6 = 5."], "Cada 5 días de trabajo"),
    ],
    mistakes=[("Usar una máquina para algo que su manual excluye porque «la fuerza alcanza».", "Se puede dañar la máquina o producir un accidente.", "Usa la máquina solo para su uso previsto."),
              ("Interpretar un símbolo «a ojo» sin preguntar.", "Se puede ignorar un peligro.", "Pregunta al supervisor qué significa.")],
    T=[
        ("abc", "{F} ¿Qué sección dice para qué materiales sirve la máquina?", "La sección 1, de uso previsto", "La sección 3, de símbolos", "La sección 4, de mantención", "El uso previsto define las tareas y materiales admitidos."),
        ("abc", "{F} ¿Quién repara y ajusta la máquina?", "El técnico de mantención", "El operario", "El prevencionista de riesgos", "La ficha asigna las reparaciones al técnico de mantención."),
        ("abc", "{F} ¿Qué significa el triángulo amarillo?", "Peligro", "Acción obligatoria", "Uso permitido", "El manual indica que el triángulo amarillo señala peligro."),
        ("abc", "En Vestuario y Confección Textil: ¿para qué sirve el manual de operaciones?", "Para conocer el uso previsto, las advertencias y la mantención de una máquina", "Para saber cuánto cuesta la tela", "Para elegir los colores de la colección", "El manual del fabricante informa sobre uso, seguridad y mantención."),
        ("=", "{F} Si la máquina trabaja 8 horas al día, ¿cada cuántos días de trabajo corresponde la revisión de lubricación?", "40//8", "Se divide la frecuencia en horas por las horas diarias.", " días"),
        ("abc", "{F} ¿Se puede usar la MR-1 para unir cartón grueso?", "No, porque no es parte del uso previsto", "Sí, si se avanza lentamente", "Sí, si el supervisor lo pide", "El manual excluye el cartón; la presión de un supervisor no cambia eso."),
        ("=", "{F} Una máquina trabaja 6 horas al día. ¿En cuántos días de trabajo llega a 120 horas, momento de su tercera revisión de lubricación?", "120//6", "Se divide el total de horas por las horas de cada día.", " días"),
        ("abc", "{F} Un operario ve un símbolo en la máquina que no entiende. ¿Qué corresponde?", "Preguntar al supervisor antes de usarla", "Suponer que no es importante", "Pedir a un compañero que adivine", "Un símbolo de seguridad no se adivina."),
        ("abc", "{F} ¿Quién vigila que se cumplan las medidas de seguridad?", "El prevencionista de riesgos", "El operario", "El técnico de mantención", "Esa función corresponde al prevencionista de riesgos."),
        ("abc", "El manual de una máquina nueva está en otro idioma y nadie lo entiende. ¿Qué corresponde?", "Informar a la jefatura y no operar la máquina hasta contar con el manual comprensible", "Operarla igual, observando", "Pedir a un compañero que explique de memoria", "Sin instrucciones comprensibles no se opera una máquina."),
        ("abc", "{F} El operario hace la limpieza de la MR-1 con la máquina conectada para ahorrar tiempo. ¿Qué dice la ficha?", "La limpieza se hace con la máquina desconectada", "Se permite si es breve", "Solo se prohíbe en turnos largos", "La ficha pide la máquina desconectada para evitar accidentes."),
        ("=", "Una sala tiene 10 máquinas MR-1 y cada revisión de lubricación demora 15 minutos. ¿Cuántos minutos demoran las revisiones de todas?", "10*15", "Se multiplica el número de máquinas por el tiempo de cada revisión.", " minutos"),
        ("abc", "{F} Un supervisor pide usar la MR-1 con cartón grueso «porque no hay otra máquina». ¿Qué corresponde?", "Recordar que el manual lo excluye y pedir una máquina adecuada", "Cumplir la orden, porque es el supervisor", "Usar la máquina sin guardas para que quepa el cartón", "El manual del fabricante manda sobre una orden verbal."),
    ],
    ctx=("abc", "{F} Se programa la mantención de la MR-1 y el supervisor pide que la haga el operario «porque es más barato». ¿Qué corresponde?", "Que la haga el técnico de mantención o personal autorizado, con la máquina desconectada", "Que la haga el operario si tiene tiempo", "Que la haga quien esté más cerca", "La mantención es una tarea de personal autorizado."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué es el uso previsto de una máquina?", "Las tareas y materiales para los que fue diseñada", "El fabricante lo define en el manual."),
        ("¿Qué hace el técnico de mantención?", "Repara y ajusta las máquinas", "Es el personal autorizado para esas tareas."),
        ("¿Qué se hace con un símbolo que no se entiende?", "Se pregunta al supervisor", "Un símbolo de seguridad no se debe adivinar."),
    ],
    op=("Extracto de ejemplo del manual de una cortadora C-2: uso previsto: telas livianas y medianas en capas delgadas; advertencia: usar solo con guardas instaladas; mantención: revisión de la cuchilla cada 80 horas de trabajo por un técnico autorizado. "
        "La máquina trabaja 8 horas al día. Escribe: (a) cada cuántos días de trabajo es la revisión, (b) quién la hace, (c) qué harías si un supervisor pide cortar capas muy gruesas y (d) qué rol vigila la seguridad.",
        "(a) 80 ÷ 8 = 10 días de trabajo. (b) Un técnico autorizado. (c) Recordar que las capas muy gruesas no están en el uso previsto y pedir una máquina adecuada. (d) El prevencionista de riesgos.",
        ["convierte horas en días", "indica al técnico autorizado", "se apoya en el uso previsto", "nombra al prevencionista"],
        ["hoja con los cuatro puntos"],
        ["dividir al revés", "decir que la hace el operario", "cumplir la orden contra el manual"],
        "Pregunta: «¿qué documento manda si el supervisor y el manual no coinciden?». Debe responder que el manual del fabricante y la norma vigente, y que se consulta a la jefatura."),
    reinforce="Inventa cuatro secciones de un manual de una máquina y escribe una frase de cada una.",
    extend="Explica con un ejemplo inventado por qué un operario no debe hacer tareas de mantención sin autorización.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 16 (informe de un cuasi accidente de ejemplo, inventado). Un cuasi accidente es un hecho que pudo causar daño y no lo causó. Hechos: a las 11:00, una operadora retiró la guarda de una overlock porque «se enredaban los hilos»; no hubo lesión. "
     "La supervisora no estaba en la sala; el manual no estaba a mano; la operadora había tenido una sola hora de capacitación (dato de ejemplo). Causa inmediata: la guarda retirada. Causas de fondo: falta de supervisión, falta del manual y capacitación insuficiente. "
     "Medidas posibles: reponer la guarda, avisar al técnico de mantención, reforzar la capacitación, tener el manual a mano y asignar una supervisión en la sala. Registro de cuasi accidentes del taller: 12 en 4 meses.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso en papel: distinguir un cuasi accidente de un accidente, separar la causa inmediata de las causas de fondo y proponer medidas.",
    prior=["Conozco las reglas generales de seguridad con máquinas.", "Sé leer un informe breve.", "Sé dividir con enteros."],
    explain=[
        "Un accidente es un hecho que causa daño a una persona; un cuasi accidente es un hecho que pudo causar daño y no lo causó. Los cuasi accidentes también se registran porque muestran dónde puede ocurrir un accidente. Ante un accidente real, se avisa de inmediato a un adulto responsable y a emergencias; este cuaderno no entrega indicaciones de primeros auxilios ni diagnósticos.",
        "Para analizar un caso se separan los hechos, la causa inmediata y las causas de fondo. La causa inmediata es lo que ocurrió justo antes del hecho, como una guarda retirada. Las causas de fondo son las condiciones que lo permitieron, como la falta de supervisión, de manual o de capacitación. Las medidas deben actuar sobre las causas de fondo y no solo sobre la inmediata, porque si no el problema se repite.",
        "El informe del caso registra qué pasó, cuándo, quién lo informó, las causas y las medidas acordadas con responsables y plazos. El objetivo no es buscar culpables, sino prevenir que se repita. Quien presencia un hecho lo avisa a la jefatura y no esconde información." + LIMX,
    ],
    vocab=[("accidente", "hecho que causa daño a una persona"), ("cuasi accidente", "hecho que pudo causar daño y no lo causó"), ("causa inmediata", "lo que ocurrió justo antes del hecho"), ("causa de fondo", "condición que permitió que el hecho ocurriera"), ("medida correctiva", "acción para evitar que el hecho se repita"), ("informe del caso", "registro de hechos, causas y medidas")],
    worked=[
        ("Clasificar un hecho", "Una operadora de ejemplo resbala con un charco y logra sujetarse sin caer. ¿Es accidente o cuasi accidente?", ["No hubo daño, pero pudo haberlo.", "Eso es un cuasi accidente."], "Cuasi accidente"),
        ("Separar causas", "Una máquina de ejemplo se usó sin guarda porque nadie supervisaba. ¿Cuál es la causa de fondo?", ["La falta de guarda fue lo inmediato.", "La falta de supervisión permitió que ocurriera."], "La falta de supervisión"),
    ],
    mistakes=[("Archivar un cuasi accidente porque «no pasó nada».", "Sin registro no se corrige la condición que puede causar el próximo accidente.", "Regístralo y analiza sus causas."),
              ("Culpar solo a la operadora y no cambiar nada más.", "Las causas de fondo seguirán allí.", "Actúa sobre supervisión, manual y capacitación.")],
    T=[
        ("abc", "{F} ¿Cómo se clasifica el hecho de la overlock?", "Como un cuasi accidente, porque no hubo lesión", "Como un accidente, porque pudo haber lesión", "No se clasifica, porque no hubo lesión", "Un cuasi accidente es un hecho que pudo causar daño y no lo causó."),
        ("abc", "{F} ¿Cuál fue la causa inmediata?", "La guarda retirada", "La falta de capacitación", "La falta de manual", "Es lo que ocurrió justo antes del hecho; las otras son causas de fondo."),
        ("abc", "{F} ¿Cuál de estas es una causa de fondo?", "La falta de supervisión en la sala", "La guarda retirada", "Los hilos enredados", "La falta de supervisión permitió que se retirara la guarda."),
        ("abc", "En Vestuario y Confección Textil: ¿qué diferencia hay entre accidente y cuasi accidente?", "El accidente causa daño y el cuasi accidente pudo causarlo y no lo causó", "El cuasi accidente causa daño y el accidente no", "Ninguna, son lo mismo", "La diferencia es si hubo o no daño a una persona."),
        ("=", "{F} Según el registro del taller, ¿cuántos cuasi accidentes hubo en promedio por mes?", "12//4", "Se divide el total de cuasi accidentes por los meses.", " por mes"),
        ("abc", "{F} ¿Por qué se registran los cuasi accidentes?", "Porque muestran dónde puede ocurrir un accidente", "Porque sirven para castigar a alguien", "Porque reemplazan los accidentes", "El registro permite prevenir antes del daño."),
        ("abc", "{F} ¿Cuál es una medida adecuada para una causa de fondo?", "Reforzar la capacitación y asignar supervisión en la sala", "Pedir a la operadora que tenga más cuidado", "Cambiar el color de la máquina", "Una medida de fondo corrige las condiciones que permitieron el hecho."),
        ("abc", "{F} La supervisora propone solo reponer la guarda. ¿Qué observación es correcta?", "Es necesaria, pero conviene actuar también sobre las causas de fondo", "Es suficiente, porque la causa fue la guarda", "Es innecesaria, porque no hubo lesión", "Si solo se repone la guarda, falta supervisión, manual y capacitación."),
        ("=", "Tras aplicar las medidas, los cuasi accidentes bajaron de 12 a 6 en un período igual de 4 meses. ¿En qué porcentaje bajaron?", "(12-6)*100//12", "Se divide la baja entre el valor inicial y se multiplica por 100.", " %"),
        ("abc", "Una operadora sufre un corte y su compañero dice: «no cuentes nada, nos regañarán a todos». ¿Qué corresponde?", "Avisar a un adulto responsable y a emergencias, sin ocultar nada", "Guardar silencio para evitar problemas", "Esperar a ver si mejora sin avisar", "Ante un accidente, se avisa de inmediato y no se oculta."),
        ("abc", "Un jefe quiere que el informe diga «error de la operadora» y no registre la falta de manual. ¿Cuál es el problema?", "Se ocultan las causas de fondo y el hecho puede repetirse", "El informe quedaría demasiado largo", "La operadora quedaría sin turno ese día", "Sin las causas de fondo, las medidas no corrigen el problema."),
        ("=", "En un taller de ejemplo hubo 20 cuasi accidentes en 5 meses. Si siguen al mismo ritmo, ¿cuántos habrá en 8 meses?", "20//5*8", "Se calcula el promedio mensual y se multiplica por los meses.", " cuasi accidentes"),
        ("abc", "{F} Se asigna la medida «tener el manual a mano» sin responsable ni plazo. ¿Qué falta?", "Un responsable y una fecha para que se cumpla", "El nombre de la máquina", "El número de operarios", "Una medida sin responsable ni plazo se olvida."),
    ],
    ctx=("abc", "{F} Una estudiante en práctica presencia un hecho parecido en otro taller. ¿Qué es lo correcto?", "Avisar al docente o a la jefatura de lo que vio", "Resolverlo ella misma con las máquinas", "No decir nada, porque no era su taller", "Avisar permite que alguien responsable corrija la condición."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué es un cuasi accidente?", "Un hecho que pudo causar daño y no lo causó", "Se registra para prevenir un accidente."),
        ("¿Sobre qué causas deben actuar las medidas?", "Sobre las causas de fondo", "Corregir solo la inmediata deja el problema abierto."),
        ("¿A quién se avisa ante un accidente?", "A un adulto responsable y a emergencias", "Es la regla general de este cuaderno."),
    ],
    op=("Caso de ejemplo: una operadora de una plancha industrial deja el equipo encendido y se va a almorzar; la supervisora estaba en una reunión; nadie se quemó. Escribe: (a) si es accidente o cuasi accidente, (b) una causa inmediata, (c) dos causas de fondo posibles y (d) dos medidas con un responsable cada una.",
        "(a) Cuasi accidente, porque nadie se lesionó. (b) El equipo quedó encendido y sin supervisión. (c) Falta de supervisión en el horario de almuerzo y falta de una regla para apagar y rotular la plancha. (d) La supervisora establece un turno de vigilancia; el prevencionista de riesgos define y comunica la regla de apagado.",
        ["clasifica el hecho", "identifica la causa inmediata", "propone dos causas de fondo", "asigna medidas con responsables"],
        ["hoja con los cuatro puntos"],
        ["clasificarlo como accidente", "culpar solo a la operadora", "no asignar responsables"],
        "Pregunta: «¿qué pasaría si nadie registra este hecho?». Debe responder que la condición podría repetirse hasta producir un accidente."),
    reinforce="Inventa un cuasi accidente de un taller y separa su causa inmediata de dos causas de fondo.",
    extend="Explica con un ejemplo inventado por qué registrar un cuasi accidente protege a las personas.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 17 (selección de máquinas de ejemplo, inventada). Capacidad de ejemplo por máquina: máquina recta (unir piezas): 60 unidades por hora; overlock (unir y rematar bordes): 80 unidades por hora; prensa de fusionado (unir tela con entretela): 100 unidades por hora; plancha industrial (dar acabado): 120 unidades por hora. "
     "Turno de 7 horas efectivas de trabajo. Pedido: 480 poleras. Cada polera pasa por una operación en cada máquina de la lista que su ficha indique. La polera del pedido pasa por la máquina recta, la overlock y la plancha, pero no por la prensa de fusionado. "
     "Regla: la máquina se elige según la operación que pide la ficha técnica y su manual de operaciones, no por la que esté libre.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: asociar la operación con la máquina y calcular cuántas máquinas hacen falta para cumplir un pedido.",
    prior=["Conozco los tipos de máquinas.", "Sé multiplicar y dividir con enteros.", "Sé que las máquinas se eligen según la ficha."],
    explain=[
        "Cada operación de la ficha técnica tiene una máquina adecuada. Unir piezas lo hace la máquina recta; unir y rematar bordes, la overlock; unir una tela con una entretela, la prensa de fusionado; y dar acabado, la plancha industrial. Elegir una máquina por estar libre y no por la operación que pide la ficha es un error: puede dañar la prenda o la máquina, y puede ser un riesgo.",
        "La capacidad de una máquina es cuántas unidades produce por hora. Con ella se calcula cuánto produce en un turno multiplicando por las horas efectivas, y cuántas máquinas hacen falta dividiendo el pedido por esa capacidad del turno y redondeando hacia arriba. Si una operación tiene menor capacidad, es el cuello de botella: limita la producción de toda la línea.",
        "Estos cálculos son planificación en papel. Cuántas máquinas se asignan, quién las opera y cómo se ajustan lo define la jefatura con personal autorizado y el manual del fabricante." + LIMX,
    ],
    vocab=[("capacidad", "unidades que produce una máquina por hora"), ("turno efectivo", "horas de trabajo reales, sin pausas"), ("cuello de botella", "operación de menor capacidad que limita a toda la línea"), ("operación", "tarea de la ficha técnica, como unir o dar acabado"), ("planificación", "cálculo previo de recursos para cumplir un pedido")],
    worked=[
        ("Producción de un turno", "Una máquina de ejemplo produce 50 unidades por hora y el turno efectivo es de 6 horas. ¿Cuánto produce en el turno?", ["Se multiplica la capacidad por las horas.", "50 × 6 = 300."], "300 unidades"),
        ("Cuántas máquinas hacen falta", "Un pedido de ejemplo de 700 unidades y una máquina que produce 300 por turno. ¿Cuántas máquinas hacen falta?", ["700 ÷ 300 = 2,33.", "Se redondea hacia arriba: 3."], "3 máquinas"),
    ],
    mistakes=[("Usar la plancha para rematar bordes «porque estaba libre».", "Cada máquina sirve para su operación.", "Elige la máquina que indica la ficha."),
              ("Calcular las máquinas con 8 horas cuando el turno efectivo es de 7.", "Las pausas no producen, así que no cuentan.", "Usa las horas efectivas.")],
    T=[
        ("abc", "{F} ¿Qué máquina corresponde a la operación de unir piezas?", "La máquina recta", "La plancha industrial", "La prensa de fusionado", "La máquina recta une piezas; la plancha da acabado y la prensa une con entretela."),
        ("=", "{F} ¿Cuántas unidades produce una máquina recta en el turno?", "60*7", "Se multiplica la capacidad por hora por las horas efectivas.", " unidades"),
        ("=", "{F} ¿Cuántas unidades produce una overlock en el turno?", "80*7", "Se multiplican las unidades por hora por las horas del turno.", " unidades"),
        ("abc", "{F} ¿Por qué el pedido no pasa por la prensa de fusionado?", "Porque la ficha de la polera no indica unir con entretela", "Porque la prensa es la más lenta", "Porque está en mantención", "Cada operación se aplica solo si la ficha técnica la pide."),
        ("=", "{F} ¿Cuántas máquinas rectas hacen falta para producir las 480 poleras en un turno?", "(480+60*7-1)//(60*7)", "Se divide el pedido por lo que produce una máquina en el turno, redondeando hacia arriba.", " máquinas"),
        ("=", "{F} ¿Cuántas overlock hacen falta para las 480 poleras en un turno?", "(480+80*7-1)//(80*7)", "Se divide el pedido por la producción de una overlock en el turno, redondeando hacia arriba.", " overlock"),
        ("abc", "{F} Entre las máquinas por las que pasa la polera, ¿cuál es el cuello de botella por su menor capacidad?", "La máquina recta", "La plancha industrial", "La overlock", "La recta produce 60 por hora, menos que la overlock y la plancha."),
        ("=", "{F} ¿Cuántas poleras produce una plancha industrial en el turno?", "120*7", "Se multiplica la capacidad por hora por las horas efectivas.", " poleras"),
        ("abc", "{F} Un compañero propone rematar los bordes en la plancha «porque está libre». ¿Qué observación es correcta?", "La ficha pide la overlock para esa operación; no se elige por estar libre", "Puede hacerse porque ambas son máquinas", "Es correcto si es solo una vez", "La máquina se elige por la operación de la ficha y su manual."),
        ("abc", "Un supervisor calcula las máquinas usando 8 horas, aunque el turno efectivo es de 7. ¿Qué error comete?", "Considera horas en que la máquina no produce y le salen menos máquinas de las necesarias", "Usa muchas horas y le salen demasiadas máquinas", "Ninguno, porque 8 horas es lo habitual", "Con más horas de las reales, la producción calculada es mayor que la verdadera."),
        ("abc", "{F} ¿Por qué conviene identificar el cuello de botella antes de asignar máquinas?", "Porque limita la producción de toda la línea", "Porque es la máquina más cara", "Porque es la que más ruido hace", "Aumentar otras operaciones no sube la producción mientras el cuello de botella no cambie."),
        ("=", "Una línea de ejemplo tiene una operación que produce 40 unidades por hora, otra 55 y otra 70, en un turno de 7 horas. ¿Cuántas unidades por turno puede producir toda la línea?", "40*7", "La línea produce lo que permite su operación más lenta.", " unidades"),
        ("abc", "{F} El pedido sube a 960 poleras. ¿Qué cambia en el cálculo de máquinas rectas?", "Se divide el nuevo pedido por 420 y se redondea hacia arriba", "Se mantiene igual, porque la máquina no cambia", "Se resta el nuevo pedido a 420", "Más unidades por turno requieren más máquinas o más turnos."),
    ],
    ctx=("=", "{F} El pedido de 480 poleras debe cumplirse con las máquinas disponibles: 1 recta, 1 overlock y 1 plancha. ¿Cuántas poleras faltan por producir después de un turno, según el cuello de botella?", "480-60*7", "La línea produce lo que permite la operación más lenta; se resta del pedido.", " poleras"),
    sc=[
        ("En Vestuario y Confección Textil: ¿cómo se elige la máquina para una operación?", "Según la operación de la ficha técnica y el manual", "No se elige por estar libre."),
        ("¿Qué horas se usan para calcular la producción?", "Las horas efectivas de trabajo", "Las pausas no producen, así que no cuentan."),
        ("¿Qué es el cuello de botella?", "La operación de menor capacidad", "Esa operación limita la producción de toda la línea."),
    ],
    op=("Datos de ejemplo: pedido de 840 delantales; máquina recta 70 unidades por hora; plancha industrial 105 unidades por hora; turno de 6 horas efectivas; cada delantal pasa por la recta y por la plancha. "
        "Escribe: (a) lo que produce cada máquina en un turno, (b) cuántas máquinas de cada tipo hacen falta, (c) cuál es el cuello de botella y (d) por qué no se asigna la plancha a unir piezas.",
        "(a) Recta: 70 × 6 = 420. Plancha: 105 × 6 = 630. (b) Rectas: 840 ÷ 420 = 2. Planchas: 840 ÷ 630 = 1,33, es decir 2. (c) La máquina recta, de menor capacidad. (d) Porque la plancha da acabado, y cada operación va en la máquina que indica la ficha.",
        ["calcula la producción por turno", "redondea hacia arriba", "identifica el cuello de botella", "explica que cada máquina sirve a su operación"],
        ["hoja con los cuatro puntos"],
        ["usar horas de más", "no redondear hacia arriba", "elegir la máquina por estar libre"],
        "Pregunta: «¿por qué 1,33 máquinas no sirve?». Debe responder que una máquina no se puede usar por partes; se redondea a 2."),
    reinforce="Con tres máquinas y tres capacidades inventadas, calcula la producción de un turno de 6 horas de cada una.",
    extend="Explica con un ejemplo inventado por qué mejorar una máquina que no es el cuello de botella no sube la producción.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 18 (mantención de máquinas de ejemplo, inventada). La mantención cuida las máquinas para que funcionen bien. Mantención preventiva: tareas planificadas antes de que haya una falla, como limpieza, lubricación y revisión según el manual del fabricante. Mantención correctiva: reparación después de una falla. "
     "Bitácora de la máquina: registro de revisiones, fallas y reparaciones. Un técnico de mantención autorizado hace la mantención; el operario avisa de ruidos, vibraciones, olores o fallas. Una máquina en mantención se rotula «no operar» y se deja desconectada de la energía por el personal autorizado. "
     "Riesgos: energía eléctrica, partes móviles, agujas, calor de las planchas y aceites o grasas (productos químicos). Regla: la mantención la hace solo personal autorizado, siguiendo el manual del fabricante.")
build(
    O5, 1, F,
    use="Aprenderé a situar la mantención de máquinas: tipos de mantención, roles, registros y riesgos; este cuaderno no enseña a reparar ni a regular una máquina.",
    prior=["Conozco los tipos de máquinas y sus riesgos.", "Sé que las máquinas tienen manual.", "Sé que solo personal autorizado las ajusta."],
    explain=[
        "En Vestuario y Confección Textil, la mantención mantiene las máquinas funcionando bien y seguras. La mantención preventiva se planifica antes de que haya una falla e incluye limpieza, lubricación y revisión según el manual del fabricante. La mantención correctiva se hace después de una falla, para repararla. La preventiva es más barata a largo plazo, porque evita paradas inesperadas.",
        "Cada mantención se registra en la bitácora de la máquina, que anota la fecha, la tarea, quién la hizo y el resultado. El operario no hace la mantención, pero sí avisa de ruidos, vibraciones, olores o fallas. Una máquina en mantención se rotula «no operar» y la deja desconectada de la energía el personal autorizado, para que nadie la encienda por error.",
        "Los riesgos son eléctricos, de partes móviles, de agujas, de calor y de productos químicos como aceites y grasas. Por eso la mantención solo la hace personal autorizado, con el manual y las medidas de seguridad. Ante un accidente se avisa a un adulto responsable y a emergencias." + LIMX,
    ],
    vocab=[("mantención preventiva", "tareas planificadas antes de una falla"), ("mantención correctiva", "reparación después de una falla"), ("bitácora de la máquina", "registro de revisiones, fallas y reparaciones"), ("rotulado «no operar»", "aviso de que la máquina no debe usarse"), ("anomalía", "ruido, vibración, olor o falla que se sale de lo normal"), ("lubricante", "aceite o grasa que reduce el roce")],
    worked=[
        ("Clasificar la mantención", "Una máquina de ejemplo se detiene por una falla y se repara. ¿Qué tipo de mantención es?", ["Se hace después de la falla.", "Es mantención correctiva."], "Correctiva"),
        ("Rol ante una anomalía", "Un operario de ejemplo nota un ruido extraño en su máquina. ¿Qué corresponde?", ["El operario no hace la mantención.", "Avisa al supervisor o al técnico y deja de usarla."], "Avisar y dejar de usarla"),
    ],
    mistakes=[("Intentar reparar la máquina uno mismo «porque es solo un ajuste».", "Un ajuste mal hecho puede dañar la máquina o causar un accidente.", "Avisa al técnico autorizado."),
              ("Encender una máquina rotulada «no operar» porque «ya debe estar lista».", "Puede haber alguien trabajando en ella.", "Respeta el rotulado hasta que lo retire el personal autorizado.")],
    T=[
        ("abc", "En Vestuario y Confección Textil: ¿qué es la mantención preventiva?", "Tareas planificadas antes de que haya una falla", "La reparación que se hace después de una falla", "El cambio de una máquina vieja", "La preventiva se adelanta a la falla; la correctiva la repara."),
        ("abc", "{F} ¿Quién hace la mantención de las máquinas?", "Un técnico de mantención autorizado", "Cualquier operario con tiempo", "Un estudiante en práctica", "La ficha asigna la mantención al personal autorizado."),
        ("abc", "{F} ¿Qué es la bitácora de la máquina?", "El registro de revisiones, fallas y reparaciones", "El manual del fabricante", "El plano de la sala", "La bitácora deja constancia de lo que ocurre con la máquina."),
        ("abc", "{F} ¿Qué debe hacer el operario ante un ruido anormal?", "Avisar y dejar de usar la máquina", "Seguir trabajando y avisar al final del turno", "Abrirla para ver qué pasa", "El operario avisa; no repara ni sigue trabajando."),
        ("abc", "En Vestuario y Confección Textil: ¿por qué la mantención preventiva suele ser más conveniente?", "Porque evita paradas inesperadas por fallas", "Porque no necesita registros", "Porque la hace cualquier persona", "Planificar antes de la falla evita detener la producción."),
        ("abc", "{F} ¿Para qué sirve rotular una máquina como «no operar»?", "Para que nadie la encienda por error mientras se trabaja en ella", "Para que el cliente sepa que está terminada", "Para ahorrar energía", "El aviso previene accidentes durante la mantención."),
        ("=", "En una sala de ejemplo hay 15 máquinas y cada una tiene una revisión preventiva de 2 horas al mes. ¿Cuántas horas de revisión hay en el mes?", "15*2", "Se multiplica el número de máquinas por las horas de cada revisión.", " horas"),
        ("abc", "{F} Una máquina tiene el rótulo «no operar». Un operario la necesita y piensa en retirarlo. ¿Qué corresponde?", "No retirarlo; solo lo retira el personal autorizado", "Retirarlo si tiene prisa", "Retirarlo si nadie lo ve", "El rótulo protege a quien está trabajando en la máquina."),
        ("abc", "{F} Un operario quiere cambiar él mismo una pieza de la máquina para ahorrar tiempo. ¿Cuál es el riesgo principal?", "Hacerlo sin autorización puede causar un accidente o dañar la máquina", "Que la máquina se vuelva más rápida", "Que la bitácora quede demasiado larga", "Solo el personal autorizado conoce el procedimiento seguro."),
        ("abc", "Un supervisor propone no registrar en la bitácora una revisión «porque no se encontró nada». ¿Qué observación es correcta?", "Se debe registrar igual, porque comprueba que la máquina se revisó", "Es correcto, porque no hubo falla", "Solo se registran las reparaciones caras", "El registro de revisiones sin hallazgos también demuestra la mantención."),
        ("abc", "Los lubricantes son aceites y grasas. ¿Qué regla general corresponde?", "Se manipulan según el manual y las indicaciones del personal autorizado", "Se pueden mezclar según el gusto del operario", "Se usan sin guardar ningún aviso", "Los productos químicos requieren las medidas que indican el manual y la norma vigente."),
        ("=", "Una máquina de ejemplo estuvo detenida 4 horas por una falla y otras 2 horas por una revisión planificada. ¿Cuántas horas estuvo detenida en total?", "4+2", "Se suman las horas de ambas paradas.", " horas"),
        ("abc", "Dos máquinas de ejemplo: una con revisiones periódicas y otra sin mantención. La segunda se detiene por fallas con frecuencia. ¿Qué conclusión es razonable?", "Es probable que la falta de mantención preventiva influya en las fallas", "Las fallas no tienen relación con la mantención", "Solo la primera necesita bitácora", "La mantención preventiva reduce las fallas, aunque no las elimina por completo."),
    ],
    ctx=("abc", "{F} Una estudiante en práctica ve que una máquina vibra mucho mientras trabaja. ¿Qué corresponde?", "Avisar al docente o a la jefatura y no usar la máquina", "Apoyar la máquina con la mano para frenar la vibración", "Esperar al fin de turno para avisar", "Una vibración fuerte es una anomalía que se informa de inmediato."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué diferencia hay entre mantención preventiva y correctiva?", "La preventiva es antes de la falla y la correctiva después", "Una previene y la otra repara."),
        ("¿Quién hace la mantención?", "El técnico de mantención autorizado", "La mantención no la hace el operario."),
        ("¿Qué se rotula durante la mantención?", "«No operar»", "Evita que alguien encienda la máquina."),
    ],
    op=("Situación de ejemplo: en un taller, una máquina recta hace un ruido nuevo y la bitácora muestra que su última revisión fue hace seis meses. Escribe: (a) qué tipo de mantención faltó, (b) qué debe hacer el operario, (c) quién interviene y (d) qué se anota en la bitácora.",
        "(a) La mantención preventiva. (b) Dejar de usar la máquina y avisar al supervisor o al técnico. (c) El técnico de mantención autorizado. (d) La fecha, la anomalía, la tarea realizada, quién la hizo y el resultado.",
        ["identifica la mantención preventiva", "indica avisar y dejar de usar", "nombra al técnico autorizado", "describe qué anotar"],
        ["hoja con los cuatro puntos"],
        ["decir que el operario repara", "no registrar la intervención", "seguir usando la máquina"],
        "Pregunta: «¿qué pasa si la máquina se detiene en plena producción?». Debe responder que se detiene el trabajo y se pierde producción."),
    reinforce="Escribe cuatro anomalías que un operario debe avisar y a quién las avisa.",
    extend="Explica con un ejemplo inventado por qué una máquina se rotula «no operar» durante la mantención.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 19 (plan de mantención de ejemplo, inventado). Máquina recta: limpieza al terminar cada turno; lubricación cada 40 horas de trabajo; revisión de la correa cada 200 horas. Plancha con vapor: revisión de mangueras de vapor cada 120 horas; limpieza del depósito de agua cada semana. "
     "Cortadora: revisión de la cuchilla por un técnico autorizado cada 80 horas. Consumibles (partes que se gastan con el uso y se reponen): agujas e hilos; su reposición la hace personal autorizado. "
     "Documentos: el manual del fabricante, el plan de mantención, la bitácora y la orden de trabajo (documento que pide y registra una intervención). Horas de uso por día: máquina recta 8; plancha 6; cortadora 4.")
build(
    O5, 2, F,
    use="Aprenderé los documentos y conceptos de la mantención (plan, bitácora, orden de trabajo, consumibles y frecuencia en horas) y a convertir frecuencias en un calendario.",
    prior=["Conozco la mantención preventiva y la correctiva.", "Sé dividir con enteros.", "Sé leer una tabla de frecuencias."],
    explain=[
        "El plan de mantención es el documento que lista, para cada máquina, las tareas preventivas y su frecuencia, ya sea en tiempo (cada semana) o en horas de trabajo. Se basa en el manual del fabricante. La bitácora registra lo que se hizo; la orden de trabajo es el documento que pide una intervención y registra quién la hizo, cuándo y con qué resultado.",
        "Los consumibles son partes que se gastan con el uso y se reponen, como agujas e hilos. Un repuesto es una pieza que reemplaza a otra dañada. Que algo sea consumible no significa que cualquiera lo cambie: la reposición la hace personal autorizado, y se registra. La frecuencia en horas se convierte en días dividiendo por las horas de uso diarias, para saber cuándo toca la próxima tarea.",
        "Un buen plan evita que dos tareas importantes queden a la vez y deja a cada máquina con su fecha. Si no se cumple una tarea del plan, se registra el motivo y se reprograma. Quien lee el plan no lo cambia por su cuenta: lo modifica el responsable de mantención." + LIMX,
    ],
    vocab=[("plan de mantención", "documento que lista tareas preventivas y su frecuencia"), ("orden de trabajo", "documento que pide y registra una intervención"), ("consumible", "parte que se gasta con el uso y se repone"), ("repuesto", "pieza que reemplaza a otra dañada"), ("frecuencia", "cada cuánto tiempo u horas se repite una tarea"), ("reprogramar", "fijar una nueva fecha para una tarea que no se cumplió")],
    worked=[
        ("Convertir horas en días", "Una tarea se repite cada 60 horas de trabajo y la máquina trabaja 6 horas al día. ¿Cada cuántos días toca?", ["Se divide 60 entre 6.", "60 ÷ 6 = 10."], "Cada 10 días de trabajo"),
        ("Distinguir documentos", "Un papel pide una intervención en una máquina y registra quién la hizo. ¿Qué documento es?", ["No es el plan, que lista tareas.", "Es la orden de trabajo."], "La orden de trabajo"),
    ],
    mistakes=[("Cambiar la frecuencia del plan porque «no hace falta tanta lubricación».", "La frecuencia viene del manual y la fija el responsable.", "Propón el cambio al responsable de mantención."),
              ("Cambiar una aguja sin registrarlo porque «es un consumible».", "Sin registro se pierde la trazabilidad del desgaste.", "Pide que lo haga personal autorizado y se anote.")],
    T=[
        ("abc", "{F} ¿Qué documento lista las tareas preventivas y su frecuencia?", "El plan de mantención", "La orden de corte", "La carta de colores", "El plan de mantención ordena las tareas por máquina."),
        ("abc", "{F} ¿Cuáles son consumibles según la ficha?", "Las agujas y los hilos", "Las mangueras de vapor", "La cuchilla de la cortadora", "La ficha nombra agujas e hilos como consumibles."),
        ("=", "{F} Con las horas de uso por día de la ficha, ¿cada cuántos días de trabajo toca la lubricación de la máquina recta?", "40//8", "Se divide la frecuencia en horas por las horas diarias de uso.", " días"),
        ("=", "{F} ¿Cada cuántos días de trabajo toca la revisión de las mangueras de la plancha?", "120//6", "Se divide la frecuencia en horas por las horas diarias de uso.", " días"),
        ("abc", "{F} ¿Quién hace la revisión de la cuchilla de la cortadora?", "Un técnico autorizado", "El operario de la cortadora", "El jefe de bodega", "La ficha indica que la revisión la hace un técnico autorizado."),
        ("abc", "En Vestuario y Confección Textil: ¿qué es una orden de trabajo?", "Un documento que pide y registra una intervención en una máquina", "El manual del fabricante", "La lista de lo que hay en bodega", "La orden de trabajo deja constancia de la intervención."),
        ("=", "{F} ¿Cada cuántos días de trabajo toca la revisión de la cuchilla de la cortadora?", "80//4", "Se divide la frecuencia en horas por las horas diarias de la cortadora.", " días"),
        ("=", "{F} ¿Cada cuántos días de trabajo toca la revisión de la correa de la máquina recta?", "200//8", "Se divide 200 horas por las 8 horas de uso diarias.", " días"),
        ("abc", "{F} Un operario cambia una aguja y no lo anota «porque es consumible». ¿Qué problema hay?", "No queda registro del desgaste y la reposición no la hizo personal autorizado", "Ninguno, porque las agujas no se registran", "Que la aguja deja de ser consumible", "El registro y la autorización se mantienen incluso en consumibles."),
        ("abc", "El técnico propone dejar para la semana próxima una tarea del plan que no se cumplió. ¿Qué corresponde?", "Registrar el motivo y reprogramar la tarea con una nueva fecha", "Olvidarla hasta que haya falla", "Marcarla como hecha", "Reprogramar deja trazabilidad y no oculta que no se hizo."),
        ("abc", "Un operario dice: «el plan está de más, la lubricación cada 40 horas es excesiva». ¿Qué corresponde?", "Proponer el cambio al responsable de mantención, apoyándose en el manual", "Cambiar el plan por su cuenta", "Ignorar la tarea desde hoy", "El plan lo modifica el responsable."),
        ("=", "En un plan de ejemplo, una tarea se repite cada 90 horas y la máquina trabaja 6 horas diarias. Si la última se hizo hoy, ¿en cuántos días de trabajo toca la siguiente?", "90//6", "Se divide la frecuencia en horas por las horas de uso diarias.", " días"),
        ("abc", "{F} Dos tareas del plan coinciden el mismo día en todas las máquinas de la sala. ¿Qué es lo más razonable?", "Repartir las tareas en fechas distintas para no detener toda la producción", "Hacerlas todas el mismo día", "Cancelar una de las dos", "El plan se organiza para que no queden todas las máquinas detenidas a la vez."),
    ],
    ctx=("=", "{F} La plancha trabaja 6 horas diarias y su limpieza del depósito es semanal, de lunes a viernes (5 días de trabajo por semana). ¿Cuántas horas de uso acumula entre dos limpiezas?", "6*5", "Se multiplican las horas diarias por los días de trabajo de la semana.", " horas"),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué es un consumible?", "Una parte que se gasta con el uso y se repone", "Las agujas y los hilos son ejemplos."),
        ("¿Cómo se convierte una frecuencia en horas a días?", "Dividiendo por las horas de uso diarias", "Así se sabe cuándo toca la tarea."),
        ("¿Quién cambia la frecuencia del plan?", "El responsable de mantención", "Un operario no cambia el plan por su cuenta."),
    ],
    op=("Plan de ejemplo para una overlock: limpieza al terminar cada turno; lubricación cada 50 horas; revisión de la cuchilla cada 100 horas por un técnico autorizado. La overlock trabaja 5 horas al día. "
        "Escribe: (a) cada cuántos días toca la lubricación, (b) cada cuántos días toca la cuchilla, (c) quién hace la revisión de la cuchilla y (d) qué documento pide la intervención y registra quién la hizo.",
        "(a) 50 ÷ 5 = 10 días de trabajo. (b) 100 ÷ 5 = 20 días de trabajo. (c) Un técnico autorizado. (d) La orden de trabajo.",
        ["divide correctamente", "indica al técnico autorizado", "nombra la orden de trabajo"],
        ["hoja con los cuatro puntos"],
        ["dividir al revés", "decir que la revisión la hace el operario", "confundir orden de trabajo con plan"],
        "Pregunta: «¿qué documento muestra todas las tareas de una máquina?». Debe responder que el plan de mantención."),
    reinforce="Inventa un plan de tres tareas para una máquina y convierte sus frecuencias en días de trabajo.",
    extend="Explica con un ejemplo inventado por qué un plan evita que todas las máquinas se detengan a la vez.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 20 (bitácora de ejemplo de la máquina recta R-2, inventada). Registro de marzo: día 3, falla de la correa, detenida 4 horas (correctiva). Día 10, lubricación a las 40 horas, detenida 1 hora (preventiva). Día 18, la operadora informa un ruido anormal; revisión de 2 horas (correctiva). "
     "Día 25, reposición de la aguja, una consumible, por personal autorizado, 1 hora (preventiva). Horas programadas de trabajo del mes: 160. Costo de ejemplo de cada hora detenida: $12.000 por producción perdida.")
build(
    O5, 3, F,
    use="Aprenderé a analizar una bitácora en papel: clasificar las paradas, calcular las horas detenidas y decidir si hace falta reforzar la mantención preventiva.",
    prior=["Conozco la bitácora y los tipos de mantención.", "Sé sumar y restar.", "Sé calcular un porcentaje con enteros."],
    explain=[
        "La bitácora permite analizar una máquina con datos: cuántas paradas tuvo, de qué tipo y cuántas horas estuvo detenida. Se clasifica cada parada como preventiva, si estaba planificada, o correctiva, si fue por una falla. Si hay muchas paradas correctivas y pocas preventivas, es señal de que la mantención preventiva es insuficiente.",
        "Las horas detenidas se suman para obtener el tiempo de parada del mes, y se restan de las horas programadas para obtener las horas operativas. La disponibilidad es el porcentaje de las horas programadas en que la máquina estuvo operativa: horas operativas dividido por horas programadas, por 100. También se estima el costo de las paradas, multiplicando las horas detenidas por el costo de cada hora.",
        "Con el análisis se proponen medidas: reforzar la revisión de la pieza que falla, reprogramar tareas y capacitar a los operarios en avisar a tiempo. Las decisiones se registran con sus datos. La mantención misma la hace personal autorizado." + LIMX,
    ],
    vocab=[("horas programadas", "horas en que la máquina debía trabajar"), ("horas operativas", "horas programadas menos las horas detenidas"), ("disponibilidad", "porcentaje de las horas programadas en que la máquina estuvo operativa"), ("parada correctiva", "detención causada por una falla"), ("parada preventiva", "detención planificada para una mantención")],
    worked=[
        ("Calcular la disponibilidad", "Una máquina de ejemplo tenía 100 horas programadas y estuvo detenida 10 horas. ¿Cuál es su disponibilidad?", ["Las horas operativas son 100 − 10 = 90.", "90 × 100 ÷ 100 = 90."], "90 %"),
        ("Costo de las paradas", "Una máquina de ejemplo estuvo detenida 5 horas y cada hora detenida cuesta $8.000. ¿Cuánto cuestan las paradas?", ["Se multiplica el costo por hora por las horas.", "5 × 8.000 = 40.000."], "$40.000"),
    ],
    mistakes=[("Dar por buena una máquina porque «hoy funciona» sin mirar la bitácora.", "El historial muestra si hay fallas repetidas.", "Analiza la bitácora antes de concluir."),
              ("Sumar solo las paradas por falla y olvidar las preventivas.", "Todas las paradas reducen las horas operativas.", "Suma todas las horas detenidas.")],
    T=[
        ("abc", "{F} ¿Cuántas paradas correctivas hubo en marzo?", "Dos: la correa y el ruido anormal", "Una: solo la correa", "Cuatro: todas las paradas", "Las correctivas son las que ocurrieron por falla: la del día 3 y la del día 18."),
        ("abc", "{F} ¿Cuántas paradas preventivas hubo?", "Dos: la lubricación y la reposición de la aguja", "Una: solo la lubricación", "Ninguna", "La lubricación y la reposición estaban planificadas."),
        ("=", "{F} ¿Cuántas horas estuvo detenida la máquina en total en marzo?", "4+1+2+1", "Se suman las horas de todas las paradas.", " horas"),
        ("=", "{F} ¿Cuántas horas operativas tuvo la máquina en el mes?", "160-(4+1+2+1)", "Se restan las horas detenidas a las programadas.", " horas"),
        ("=", "{F} ¿Cuál fue la disponibilidad de la máquina en el mes (porcentaje)?", "(160-(4+1+2+1))*100//160", "Se divide las horas operativas por las programadas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál fue el costo de las horas detenidas por fallas?", "(4+2)*12000", "Se multiplican las horas de parada correctiva por el costo de cada hora.", " pesos"),
        ("=", "{F} ¿Cuánto costó el total de las horas detenidas, preventivas y correctivas?", "(4+1+2+1)*12000", "Se multiplican todas las horas detenidas por el costo por hora.", " pesos"),
        ("abc", "{F} Dos de las cuatro paradas fueron correctivas. ¿Qué conclusión es razonable?", "Conviene revisar la correa y reforzar el aviso temprano de anomalías", "La máquina no necesita ninguna mantención", "Basta con lubricar más veces", "Las fallas repetidas señalan dónde reforzar la preventiva."),
        ("abc", "{F} La operadora informó el ruido el día 18. ¿Qué rol cumplió?", "Avisó una anomalía y no intentó repararla", "Reparó la máquina", "Cambió el plan de mantención", "El operario avisa de las anomalías; la reparación es de personal autorizado."),
        ("abc", "Un supervisor concluye: «como la disponibilidad fue alta, no hay nada que mejorar». ¿Qué observación es correcta?", "Aun con disponibilidad alta, hay dos fallas que conviene analizar para evitar repeticiones", "Tiene razón, porque la disponibilidad lo resume todo", "Se equivoca, porque la disponibilidad no sirve", "El indicador no reemplaza el análisis de las causas de las fallas."),
        ("abc", "Un técnico anota en la bitácora «arreglado» sin fecha ni horas. ¿Qué falta?", "La fecha, las horas, la tarea y quién la hizo", "El color de la máquina", "El nombre del cliente", "Un registro útil permite calcular horas y revisar la historia."),
        ("=", "Otra máquina de ejemplo tenía 200 horas programadas y estuvo detenida 30 horas. ¿Cuál fue su disponibilidad?", "(200-30)*100//200", "Se calculan las horas operativas y se divide por las programadas.", " %"),
        ("abc", "La máquina R-2 de ejemplo tuvo una disponibilidad de 95 % y otra máquina de 85 %. ¿Qué observación es correcta?", "La de 95 % estuvo operativa una mayor parte del tiempo programado", "La de 85 % estuvo operativa más tiempo, porque tuvo más mantenciones", "Son equivalentes, porque ambas superan el 80 %", "Mayor disponibilidad significa más tiempo operativo sobre el programado."),
    ],
    ctx=("abc", "{F} La jefatura debe decidir si cambiar la correa antes de su fecha de revisión. ¿Qué dato de la bitácora apoya la decisión?", "La falla de la correa el día 3, que causó 4 horas de parada correctiva", "El color de la máquina", "El número de operarias", "La bitácora muestra la historia de fallas de la pieza."),
    sc=[
        ("En Vestuario y Confección Textil: ¿cómo se calcula la disponibilidad?", "Horas operativas dividido por horas programadas, por 100", "Es el porcentaje del tiempo programado en que la máquina estuvo operativa."),
        ("¿Qué indica una cantidad alta de paradas correctivas?", "Que la mantención preventiva puede ser insuficiente", "Las fallas frecuentes señalan puntos a reforzar."),
        ("¿Qué rol tiene el operario ante una anomalía?", "Avisar", "No repara; informa a quien corresponde."),
    ],
    op=("Bitácora de ejemplo de una overlock en un mes con 160 horas programadas: día 5, lubricación de 1 hora; día 12, falla de la cuchilla, 3 horas detenida; día 20, ruido informado y revisión de 2 horas; día 27, reposición de consumibles de 2 horas. Costo de cada hora detenida: $9.000. "
        "Escribe: (a) las horas detenidas, (b) la disponibilidad, (c) el costo de las paradas y (d) una medida que propondrías.",
        "(a) 1 + 3 + 2 + 2 = 8 horas. (b) (160 − 8) × 100 ÷ 160 = 95 %. (c) 8 × 9.000 = 72.000 pesos. (d) Reforzar la revisión de la cuchilla y pedir al responsable de mantención ajustar el plan.",
        ["suma las horas detenidas", "calcula las horas operativas", "calcula el costo", "propone una medida con responsable"],
        ["hoja con los cuatro puntos"],
        ["olvidar alguna parada", "restar mal las horas operativas", "proponer que el operario repare"],
        "Pregunta: «¿qué parada fue correctiva?». Debe responder la cuchilla y el ruido, porque ocurrieron por falla."),
    reinforce="Inventa una bitácora de cuatro paradas y clasifica cada una como preventiva o correctiva.",
    extend="Explica con un ejemplo inventado por qué una alta disponibilidad no basta para dar por buena una máquina.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 21 (planificación de mantención de ejemplo, inventada). Taller con 6 máquinas rectas, 4 overlock y 2 planchas. Revisión preventiva mensual: recta, 2 horas por máquina; overlock, 3 horas; plancha, 4 horas. "
     "Un técnico autorizado trabaja 6 horas diarias en revisiones (dato de ejemplo). Costo de ejemplo del técnico: $9.000 por hora. Costo de ejemplo de una hora de máquina detenida: $15.000. Una falla correctiva de ejemplo detiene la máquina 10 horas.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar criterios con datos: calcular las horas de mantención preventiva de un mes, su costo y compararlo con el costo de una falla.",
    prior=["Conozco el plan de mantención y la bitácora.", "Sé multiplicar y dividir con enteros.", "Sé comparar costos."],
    explain=[
        "Para planificar la mantención preventiva de un mes se calcula cuántas horas requieren todas las máquinas: se multiplica el número de máquinas de cada tipo por las horas de su revisión y se suman los resultados. Con las horas diarias que trabaja el técnico se obtienen los días necesarios, dividiendo y redondeando hacia arriba. Así se evita que la mantención quede sin tiempo asignado.",
        "El costo de la mantención preventiva es el de las horas del técnico y de las horas en que cada máquina está detenida. El costo de una falla correctiva incluye la reparación y la producción perdida por las horas detenidas, y suele ser mayor que el de la preventiva. Comparar ambos costos ayuda a decidir, pero la seguridad no se negocia por ahorro.",
        "El plan se entrega al responsable de mantención y a la jefatura de producción para coordinar fechas con los pedidos. Todo cálculo queda por escrito para que otra persona lo revise." + LIMX,
    ],
    vocab=[("horas de revisión", "tiempo de mantención que requiere cada máquina"), ("producción perdida", "unidades o dinero que se dejan de producir por una parada"), ("costo preventivo", "costo del técnico y de la parada planificada"), ("costo correctivo", "costo de reparar y de la parada por falla"), ("redondear hacia arriba", "subir al siguiente número entero para cubrir lo que falta")],
    worked=[
        ("Horas de revisión de un tipo", "Una sala de ejemplo tiene 5 máquinas con revisión de 2 horas cada una. ¿Cuántas horas suman?", ["Se multiplica el número de máquinas por las horas.", "5 × 2 = 10."], "10 horas"),
        ("Días del técnico", "Con 10 horas de revisión y un técnico que trabaja 4 horas diarias en ellas, ¿cuántos días necesita?", ["10 ÷ 4 = 2,5.", "Se redondea hacia arriba: 3."], "3 días"),
    ],
    mistakes=[("Redondear hacia abajo los días del técnico porque «sobra un poquito».", "Quedan horas de revisión sin hacer.", "Redondea hacia arriba."),
              ("Omitir el costo de la máquina detenida al comparar preventiva con correctiva.", "La parada también cuesta por la producción perdida.", "Incluye la producción perdida.")],
    T=[
        ("=", "{F} ¿Cuántas horas de revisión mensual necesitan las máquinas rectas?", "6*2", "Se multiplica el número de máquinas por las horas de cada revisión.", " horas"),
        ("=", "{F} ¿Cuántas horas de revisión mensual necesitan las overlock?", "4*3", "Se multiplica el número de overlock por las horas de revisión de cada una.", " horas"),
        ("=", "{F} ¿Cuántas horas de revisión mensual necesitan las planchas?", "2*4", "Se multiplica el número de planchas por las horas de su revisión.", " horas"),
        ("=", "{F} ¿Cuántas horas de revisión necesita el taller en total en el mes?", "6*2+4*3+2*4", "Se suman las horas de los tres tipos de máquinas.", " horas"),
        ("=", "{F} ¿Cuántos días de trabajo necesita el técnico para completar las revisiones del mes?", "(6*2+4*3+2*4+6-1)//6", "Se dividen las horas totales por las horas diarias, redondeando hacia arriba.", " días"),
        ("abc", "{F} ¿Por qué se redondean hacia arriba los días del técnico?", "Porque un día incompleto igual debe usarse para terminar las horas que faltan", "Porque conviene que el técnico trabaje más", "Porque así se obtiene un número más bajo", "Si se redondea hacia abajo, quedan revisiones sin hacer."),
        ("=", "{F} ¿Cuánto cuestan las horas del técnico para todas las revisiones del mes?", "(6*2+4*3+2*4)*9000", "Se multiplican las horas totales por el costo por hora del técnico.", " pesos"),
        ("=", "{F} Si cada máquina está detenida solo durante su revisión, ¿cuánto cuesta la producción perdida por las revisiones de las 6 rectas?", "6*2*15000", "Se multiplican máquinas, horas de revisión y costo por hora detenida.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la producción perdida por una falla correctiva de una máquina?", "10*15000", "Se multiplican las horas de la falla por el costo de cada hora detenida.", " pesos"),
        ("abc", "{F} Comparando la producción perdida de la revisión de una recta (2 horas) con la de una falla correctiva (10 horas), ¿qué se concluye?", "La falla correctiva pierde más producción que una revisión preventiva", "La revisión pierde más que la falla", "Cuestan lo mismo", "La falla detiene 10 horas y la revisión solo 2."),
        ("abc", "El jefe propone eliminar las revisiones de las planchas para ahorrar horas de técnico. ¿Cuál es el riesgo principal?", "Aumenta la probabilidad de fallas y de riesgos de seguridad por calor y vapor", "No hay riesgo, porque las planchas no fallan", "Se reducirían las ventas", "La mantención preventiva reduce fallas y riesgos."),
        ("=", "Un taller de ejemplo hace un plan con 20 horas de revisión mensual y un técnico que dedica 5 horas diarias. ¿Cuántos días necesita?", "(20+5-1)//5", "Se dividen las horas por las horas diarias, redondeando hacia arriba.", " días"),
        ("abc", "{F} Un compañero sugiere que la bodega haga una revisión de las planchas «para ahorrar al técnico». ¿Qué corresponde?", "Dejarla al personal autorizado, siguiendo el manual y el plan", "Aceptar si tiene buena voluntad", "Aceptar si lo hace el fin de semana", "La mantención de equipos con calor y vapor solo la hace personal autorizado."),
    ],
    ctx=("=", "{F} El taller agrega 2 máquinas rectas más al plan, con la misma revisión mensual. ¿Cuántas horas de revisión mensual necesita ahora el taller en total?", "(6+2)*2+4*3+2*4", "Se recalculan las horas con 8 máquinas rectas y se suman los otros tipos.", " horas"),
    sc=[
        ("En Vestuario y Confección Textil: ¿cómo se calculan las horas de revisión de un tipo de máquina?", "Multiplicando el número de máquinas por las horas de cada revisión", "Así se obtiene el tiempo total por tipo."),
        ("¿Cómo se calculan los días que necesita el técnico?", "Dividiendo las horas totales por las horas diarias y redondeando hacia arriba", "Hay que cubrir todas las horas."),
        ("¿Qué costo se suma al de una falla correctiva además de la reparación?", "La producción perdida por las horas detenidas", "La parada también cuesta por la producción perdida."),
    ],
    op=("Taller de ejemplo con 3 máquinas rectas (revisión de 2 horas cada una), 2 overlock (3 horas) y 1 plancha (4 horas). El técnico trabaja 4 horas diarias en revisiones y cuesta $8.000 por hora; una hora de máquina detenida cuesta $10.000. "
        "Escribe: (a) las horas totales, (b) los días del técnico, (c) el costo de las horas del técnico y (d) cuánta producción se pierde en la revisión de una máquina recta (2 horas) y cuánta en una falla de 8 horas de una máquina, y qué concluyes.",
        "(a) 3 × 2 + 2 × 3 + 4 = 16 horas. (b) 16 ÷ 4 = 4 días. (c) 16 × 8.000 = 128.000 pesos. (d) La revisión de una recta pierde 2 × 10.000 = 20.000 de producción; la falla de 8 horas pierde 8 × 10.000 = 80.000 y además suma la reparación, es decir, cuatro veces más; la preventiva evita esas paradas inesperadas.",
        ["suma las horas por tipo", "divide para los días", "calcula el costo del técnico", "compara la producción perdida de una revisión con la de una falla"],
        ["hoja con los cuatro puntos"],
        ["olvidar la plancha", "redondear hacia abajo", "ignorar la producción perdida"],
        "Pregunta: «¿cuánto cuesta una hora de máquina detenida?». Debe responder $10.000 y relacionarlo con la producción perdida."),
    reinforce="Inventa un taller con tres tipos de máquinas y calcula las horas totales de revisión de un mes.",
    extend="Explica con un ejemplo inventado por qué la mantención preventiva suele costar menos que las fallas.",
)
